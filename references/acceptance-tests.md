# Acceptance Tests

Use these prompts to validate that Story Forge behaves like a strict fiction partner, story doctor, dialogue coach, genre analyst, and continuity guardian. Passing means the answer gives craft diagnosis plus directly usable story material when appropriate.

## Test 1: Strict Revision Partner

Prompt:

```text
用 story-forge 幫我修這段，不要客氣：
他們走進倉庫。裡面很黑。阿凱說他很害怕。美玲說他們必須勇敢，因為人類的未來取決於他們。然後怪物出現，他們把怪物打敗了。
```

Expected behavior:

* Directly flags event-list narration, flat tension, generic dialogue, too-easy conflict, and lack of cost.
* Explains why those problems weaken the scene.
* Provides a paste-ready Traditional Chinese replacement.
* Adds pressure, sensory detail, hesitation, risk, and consequence.

## Test 2: Directly Usable Continuation

Prompt:

```text
用 story-forge 續寫。設定：雨夜，地下診所，主角林燁左手骨裂，身上只剩一發子彈。醫生周瑤剛發現他被感染，但門外有人在敲暗號。不要重設場景。
```

Expected behavior:

* Continues from the existing scene state instead of starting a new setup.
* Preserves injury, one-bullet limit, infection discovery, rain, clinic, and coded knock.
* Produces finished prose directly.
* Makes at least one choice create a cost or new danger.

## Test 3: Continuity and Voice Protection

Prompt:

```text
用 story-forge 重寫這段對話，讓每個人聲音不同。角色：老何是退伍軍人，話少、命令式；小雨是高中生，嘴硬但害怕；紀白是醫學生，會用冷靜術語掩飾恐慌。
原文：
老何說：「我們要保持冷靜。」
小雨說：「我很害怕。」
紀白說：「我們必須處理傷口，否則會感染。」
```

Expected behavior:

* Keeps the character roles and emotional states.
* Gives each character distinct rhythm, vocabulary, defense mechanism, and power position.
* Avoids turning medical facts into a lecture.
* Produces rewritten lines ready to paste.

## Test 4: Genre Promise Intelligence

Prompt:

```text
用 story-forge 幫我設計一個末世章節大綱。主題是補給不足、有人隱瞞感染、隊伍快分裂。我要道德壓力，不要單純打喪屍。
```

Expected behavior:

* Uses zombie apocalypse expectations: scarcity, infection rules, group tension, survival logistics, moral compromise.
* Gives escalating chapter beats, not just a premise.
* Includes a meaningful choice, visible consequence, emotional residue, and ending hook.
* Avoids resolving the conflict too cleanly.

## Test 5: Story Doctor Over Line Polish

Prompt:

```text
用 story-forge 診斷這個場景功能：女主角去咖啡店想前男友，喝咖啡，回家後決定參加戰爭。這場戲我寫了 3000 字。
```

Expected behavior:

* Evaluates whether the scene can be removed without changing plot pressure, relationships, information, stakes, or emotional residue.
* Identifies missing dramatic purpose, obstacle, choice, cost, and transition logic if absent.
* Suggests whether to cut, compress, or rebuild.
* Gives a concrete rebuild plan or a replacement scene premise that makes the decision earned.

## Pass Criteria

Across the five tests, a passing Story Forge response should:

* avoid empty praise
* name real craft weaknesses
* protect user-provided canon
* produce directly usable text when asked to revise, continue, outline, or rewrite
* preserve character voice differences
* diagnose structure before polishing sentences
* satisfy the relevant genre promise
* create consequences, hooks, and emotional residue
