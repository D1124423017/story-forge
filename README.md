# story-forge

<picture>
  <source srcset="docs/assets/story-forge-hero.webp" type="image/webp">
  <img src="docs/assets/story-forge-hero.png" alt="Story Forge hero">
</picture>

**story-forge** is a Codex Agent Skill for fiction writing, revision, dialogue coaching, story diagnosis, pacing repair, novel completion coaching, genre analysis, narrative design, mature 18+ themes, and original series development.

[Open the multilingual guide](https://d1124423017.github.io/story-forge/) · [Source skill](SKILL.md) · [Novel Completion Coach](references/novel-completion-coach.md) · [Examples](examples/)

Languages: [中文](#中文使用教學) · [English](#english-guide) · [日本語](#日本語ガイド) · [한국어](#한국어-가이드)

## Purpose

story-forge helps Codex act as a strict novelist, story doctor, pacing doctor, long-form novel completion coach, dialogue coach, genre analyst, continuity guardian, mature-content story editor, and original high-concept story development partner.

## What it does

| Mode | What it helps with |
| --- | --- |
| Novel Completion Coach | Launch a novel, build a full-book roadmap, write chapter by chapter, diagnose writer's block, track continuity, and revise by draft stage. |
| Pacing Doctor | Fix dragging setup, rushed climaxes, weak chapter hooks, reveal timing, event-list narration, and whole-book rhythm. |
| Story Doctor | Diagnose weak scenes, flat conflict, missing costs, unclear motivation, continuity breaks, and genre promise failures. |
| Dialogue Coach | Rewrite character-specific dialogue with subtext, pressure, interruption, and distinct voice. |
| Mature 18+ Editor | Handle adult themes with consent awareness, psychological consequence, boundaries, and character truth. |
| Prose Style Lab | Diagnose POV distance, sentence rhythm, imagery, narrative density, cold/warm tone, and humor. |
| Publishing Package | Prepare query letters, synopsis, blurbs, serial launch plans, and chapter title strategies. |

## Structure

* SKILL.md: core skill instructions and trigger description
* agents/openai.yaml: Codex UI metadata and invocation prompt
* references/: writing checklists, genre patterns, dialogue guide, mature-content rules, pacing doctor rules, novel completion coaching, prose style lab, publishing package guidance, revision rubric, scene templates, acceptance tests, and original series-development guidance
* assets/novel-project-template/: reusable project files for long-form fiction workspaces
* scripts/: project creation and skill contract validation helpers
* examples/: high-standard example outputs for common workflows

## Installation / Update

Use this repository as the source repo:

```powershell
git clone https://github.com/D1124423017/story-forge.git
cd story-forge
```

The installed Codex skill should contain runtime files only:

```text
C:\Users\lenny\.codex\skills\story-forge
```

Runtime files are:

```text
SKILL.md
agents/
references/
scripts/
assets/novel-project-template/
```

Do not treat the installed Codex directory as the main Git repo. Keep commits and pushes in the source repo.

## Create a Novel Project Workspace

```powershell
python scripts/create_novel_project.py --title "失名之城" --out "C:\Users\lenny\OneDrive\Desktop"
```

This creates:

```text
project-brief.md
chapter-tracker.md
continuity-ledger.md
character-bible.md
revision-plan.md
```

## Validation

```powershell
python scripts/validate_skill_contract.py --skill-dir .
node --check docs/app.js
git diff --check
```

## 中文使用教學

在 Codex 裡明確呼叫：

```text
用 $story-forge 幫我啟動一個長篇小說專案。我的靈感是：一個會忘記死者名字的城市。
```

常用指令：

```text
用 $story-forge 幫我做全書路線圖：開場、第一轉折、中段反轉、低谷、高潮、結局餘韻。
```

```text
用 $story-forge 陪我寫第七章。先定本章目標、衝突、揭露、代價、鉤子，再寫正文。
```

```text
用 $story-forge 診斷我為什麼卡稿。目前劇情是...
```

```text
用 $story-forge 幫我安排修稿。請分成初稿、結構稿、角色稿、節奏稿、對話稿、文風稿。
```

## English Guide

Invoke it in Codex with:

```text
Use $story-forge to launch a long-form novel project. My idea is: a city that forgets the names of the dead.
```

Useful prompts:

```text
Use $story-forge to build a full-book roadmap: opening, first turn, midpoint reversal, low point, climax, and ending residue.
```

```text
Use $story-forge to help me write Chapter 7. First define the chapter goal, conflict, reveal, cost, and hook, then draft the prose.
```

## 日本語ガイド

Codex で次のように呼び出します。

```text
$story-forge を使って長編小説プロジェクトを始めたい。着想は、死者の名前を忘れていく都市です。
```

よく使う依頼：

```text
$story-forge で全体ロードマップを作って。開幕、第一転換点、中盤反転、どん底、クライマックス、余韻を入れて。
```

```text
$story-forge で第七章を書きたい。先に目的、対立、開示、代償、フックを決めてから本文を書いて。
```

## 한국어 가이드

Codex에서 이렇게 호출합니다.

```text
$story-forge로 장편 소설 프로젝트를 시작하고 싶어. 아이디어는 죽은 사람의 이름을 잊어가는 도시야.
```

자주 쓰는 요청:

```text
$story-forge로 전체 소설 로드맵을 만들어줘. 오프닝, 첫 전환점, 중반 반전, 저점, 클라이맥스, 결말 여운을 넣어줘.
```

```text
$story-forge로 7장을 함께 써줘. 먼저 장 목표, 갈등, 공개 정보, 대가, 훅을 정하고 본문을 써줘.
```

## Suggested usage

Use this skill when working on fiction, scripts, game narrative, character arcs, dialogue, scenes, chapters, long-form roadmaps, whole-book pacing, information reveals, worldbuilding, story revision, first-draft completion, second-draft restructuring, final revision, writer's block diagnosis, mature 18+ themes, high-concept premises, series bibles, chapter engines, or original alternatives to famous-story inspiration.

## Examples

Start with these examples when calibrating the skill:

* [Novel launch](examples/01-novel-launch.md)
* [Chapter companion](examples/02-chapter-companion.md)
* [Writer's block diagnosis](examples/03-writers-block-diagnosis.md)
* [Continuity ledger](examples/04-continuity-ledger.md)
* [Second-draft restructure](examples/05-second-draft-restructure.md)
* [Mature boundary repair](examples/06-mature-boundary-repair.md)

## Version

Current version: `v0.2.0`

## GitHub Pages

The multilingual guide lives in `docs/` and is deployed by `.github/workflows/pages.yml`.

If GitHub Pages is not visible yet, open the repository settings and set Pages to **GitHub Actions**. The next push to `main` will deploy the guide.
