#!/usr/bin/env python3
"""Create a Story Forge novel project workspace from bundled templates."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

TEMPLATE_FILES = [
    "project-brief.md",
    "chapter-tracker.md",
    "continuity-ledger.md",
    "character-bible.md",
    "revision-plan.md",
]


def clean_title(title: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", title.strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    return cleaned


def render_template(text: str, title: str, language: str) -> str:
    today = dt.date.today().isoformat()
    return (
        text.replace("{{TITLE}}", title)
        .replace("{{LANGUAGE}}", language)
        .replace("{{CREATED_DATE}}", today)
    )


def create_project(title: str, out_dir: Path, language: str) -> Path:
    if language != "zh-Hant":
        raise ValueError("Only zh-Hant templates are currently supported.")

    safe_title = clean_title(title)
    if not safe_title:
        raise ValueError("Project title cannot be empty after sanitization.")

    root = Path(__file__).resolve().parents[1]
    template_dir = root / "assets" / "novel-project-template"
    if not template_dir.is_dir():
        raise FileNotFoundError(f"Template directory not found: {template_dir}")

    missing = [name for name in TEMPLATE_FILES if not (template_dir / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing template file(s): {', '.join(missing)}")

    project_dir = out_dir.expanduser().resolve() / safe_title
    if project_dir.exists():
        raise FileExistsError(f"Refusing to overwrite existing project: {project_dir}")

    project_dir.mkdir(parents=True)
    try:
        for name in TEMPLATE_FILES:
            source = template_dir / name
            target = project_dir / name
            rendered = render_template(source.read_text(encoding="utf-8"), safe_title, language)
            target.write_text(rendered, encoding="utf-8", newline="\n")
    except Exception:
        shutil.rmtree(project_dir, ignore_errors=True)
        raise

    return project_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Novel project title.")
    parser.add_argument("--out", required=True, type=Path, help="Directory where the project folder will be created.")
    parser.add_argument("--language", default="zh-Hant", choices=["zh-Hant"], help="Template language.")
    args = parser.parse_args(argv)

    try:
        project_dir = create_project(args.title, args.out, args.language)
    except Exception as exc:  # noqa: BLE001 - command-line tool should print clean errors
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Created novel project: {project_dir}")
    for name in TEMPLATE_FILES:
        print(f"- {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
