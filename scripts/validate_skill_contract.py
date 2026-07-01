#!/usr/bin/env python3
"""Validate the Story Forge skill contract without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_REFERENCES = [
    "story-craft-checklists.md",
    "genre-patterns.md",
    "dialogue-style-guide.md",
    "revision-rubric.md",
    "scene-templates.md",
    "acceptance-tests.md",
    "original-series-development.md",
    "mature-content-guidelines.md",
    "pacing-doctor.md",
    "novel-completion-coach.md",
    "prose-style-lab.md",
    "publishing-package.md",
]

REQUIRED_RUNTIME_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "scripts/create_novel_project.py",
    "scripts/validate_skill_contract.py",
    "assets/novel-project-template/project-brief.md",
    "assets/novel-project-template/chapter-tracker.md",
    "assets/novel-project-template/continuity-ledger.md",
    "assets/novel-project-template/character-bible.md",
    "assets/novel-project-template/revision-plan.md",
]

REQUIRED_REPO_FILES = [
    "README.md",
    "LICENSE",
    "VERSION",
    "docs/index.html",
    "docs/app.js",
    "docs/styles.css",
    "docs/assets/story-forge-hero.png",
    "docs/assets/story-forge-hero.webp",
    "docs/assets/story-forge-workflow.png",
    "docs/assets/story-forge-workflow.webp",
    "docs/assets/story-forge-continuity.png",
    "docs/assets/story-forge-continuity.webp",
    ".github/workflows/pages.yml",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/skill_improvement.yml",
    ".github/pull_request_template.md",
]

REQUIRED_SKILL_TERMS = [
    "Novel Completion Coach Mode",
    "Pacing Doctor Mode",
    "Mature 18+ Mode",
    "Prose Style Lab Mode",
    "Publishing Package Mode",
    "references/prose-style-lab.md",
    "references/publishing-package.md",
]

TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".html", ".css", ".js", ".txt"}
FORBIDDEN_TERMS = ["master" + "-novelist"]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_text: str) -> dict[str, str]:
    if not skill_text.startswith("---\n"):
        return {}
    end = skill_text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in skill_text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def iter_text_files(root: Path) -> list[Path]:
    ignored_parts = {".git"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ignored_parts.intersection(path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def check_contract(root: Path) -> list[Check]:
    checks: list[Check] = []
    repo_mode = (root / "README.md").is_file() or (root / "docs").is_dir() or (root / ".github").is_dir()
    skill_path = root / "SKILL.md"
    skill_text = read_text(skill_path) if skill_path.is_file() else ""
    frontmatter = parse_frontmatter(skill_text)

    checks.append(Check("frontmatter name", frontmatter.get("name") == "story-forge"))
    checks.append(Check("frontmatter description", len(frontmatter.get("description", "")) >= 120))

    for rel in REQUIRED_RUNTIME_FILES:
        checks.append(Check(f"runtime file: {rel}", (root / rel).is_file()))

    if repo_mode:
        for rel in REQUIRED_REPO_FILES:
            checks.append(Check(f"repo file: {rel}", (root / rel).is_file()))

    for ref in REQUIRED_REFERENCES:
        checks.append(Check(f"reference exists: {ref}", (root / "references" / ref).is_file()))
        checks.append(Check(f"SKILL references {ref}", f"references/{ref}" in skill_text))

    for term in REQUIRED_SKILL_TERMS:
        checks.append(Check(f"SKILL term: {term}", term in skill_text))

    tests_path = root / "references" / "acceptance-tests.md"
    tests_text = read_text(tests_path) if tests_path.is_file() else ""
    test_count = len(re.findall(r"^## Test ", tests_text, flags=re.MULTILINE))
    checks.append(Check("acceptance tests >= 24", test_count >= 24, f"found {test_count}"))

    if repo_mode:
        examples_dir = root / "examples"
        example_count = len(list(examples_dir.glob("*.md"))) if examples_dir.is_dir() else 0
        checks.append(Check("examples >= 6", example_count >= 6, f"found {example_count}"))

        docs_index = read_text(root / "docs" / "index.html") if (root / "docs" / "index.html").is_file() else ""
        checks.append(Check("Pages uses WebP picture fallback", "<picture" in docs_index and ".webp" in docs_index and ".png" in docs_index))
        checks.append(Check("Pages has four language controls", all(token in docs_index for token in ['data-lang="zh-Hant"', 'data-lang="en"', 'data-lang="ja"', 'data-lang="ko"'])))

        version = read_text(root / "VERSION").strip() if (root / "VERSION").is_file() else ""
        checks.append(Check("VERSION is v0.2.0", version == "v0.2.0", version))

    forbidden_hits: list[str] = []
    for path in iter_text_files(root):
        text = read_text(path)
        lower = text.lower()
        for term in FORBIDDEN_TERMS:
            if term in lower:
                forbidden_hits.append(str(path.relative_to(root)))
    checks.append(Check("forbidden terms absent", not forbidden_hits, ", ".join(forbidden_hits)))

    return checks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".", type=Path, help="Story Forge repository or installed skill directory.")
    args = parser.parse_args(argv)

    root = args.skill_dir.resolve()
    checks = check_contract(root)
    failed = [check for check in checks if not check.ok]

    for check in checks:
        status = "PASS" if check.ok else "FAIL"
        detail = f" ({check.detail})" if check.detail else ""
        print(f"{status}: {check.name}{detail}")

    if failed:
        print(f"\n{len(failed)} check(s) failed.", file=sys.stderr)
        return 1

    print(f"\nAll {len(checks)} contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
