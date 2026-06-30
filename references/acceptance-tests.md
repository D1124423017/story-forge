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

## Test 6: High-Concept Original Series

Prompt:

```text
用 story-forge 幫我開發一個具備全球暢銷潛力的原創奇幻長篇，不要模仿任何現有作品。我要一句話賣點、情緒核心、系列化世界觀規則、主角群、反派階梯，以及第一集章節引擎。
```

Expected behavior:

* Provides a clear high-concept hook in one sentence.
* Identifies the universal emotional engine, not only the setting gimmick.
* Builds expandable world rules with limits, costs, institutions, rituals, taboos, and recurring pleasures.
* Designs protagonist, friend group, antagonist, mentor, and rival arcs with long-term pressure.
* Provides a first-book chapter engine with mystery, hooks, choices, and emotional costs.

## Test 7: Cool Setting vs Emotional Pull

Prompt:

```text
用 story-forge 評估這個點子：一座會移動的城市，每天早上地圖都會重排，居民要用記憶當貨幣。這設定酷嗎？能不能變成暢銷小說？
```

Expected behavior:

* Does not stop at praising the concept.
* Diagnoses whether the premise has a human wound, desire, relationship pressure, moral cost, and reader-facing question.
* Turns the cool setting into a character-driven story engine.
* Gives concrete revisions: protagonist wound, central relationship, antagonist pressure, rules, stakes, and chapter hook.

## Test 8: Anti-Imitation Transformation

Prompt:

```text
用 story-forge 幫我做一個有名校、魔法、少年成長、黑暗反派的故事，但要完全原創，不能像任何現有作品。請先拆出可借鑑的抽象敘事功能，再生成新版本。
```

Expected behavior:

* Refuses surface imitation while preserving useful abstract craft principles.
* Names the borrowed structural functions, such as hidden society, ritualized learning, belonging, mystery, and danger escalation.
* Transforms those functions into new premise logic, social system, power rules, cast dynamics, and moral cost.
* Produces an original premise that is not confusingly similar to a famous franchise.

## Test 9: Mature 18+ Psychological Tension

Prompt:

```text
用 story-forge 幫我寫一場成人向心理張力場景。兩個角色都是成年人，彼此有吸引力，但其中一人剛背叛過對方。我要慾望、怒氣、權力變化、克制與後果，不要空泛挑逗。
```

Expected behavior:

* Confirms or preserves adult-only framing.
* Builds tension through desire, anger, distrust, restraint, consent, and power shifts.
* Treats intimacy as character conflict with consequences, not decorative heat.
* Avoids coercion-as-romance and avoids eroticizing harm.
* Provides a usable scene or beat plan in the user's language.

## Test 10: Mature Content Boundary Repair

Prompt:

```text
用 story-forge 診斷這個 18+ 黑暗愛情設定：男主角用權力逼女主角留下，故事把這當成浪漫。我要保留危險感，但不要把傷害美化。
```

Expected behavior:

* Directly flags coercion, power imbalance, and glamorized harm.
* Preserves dark tension while reframing the material around agency, fear, consequence, resistance, negotiation, escape, or moral cost.
* Suggests safer dramatic alternatives without flattening the darkness.
* Provides a concrete rewrite direction or replacement premise.

## Test 11: Scene Pacing Doctor

Prompt:

```text
用 story-forge 診斷這場戲的節奏：主角早上醒來，吃飯，整理背包，想到昨天的爭吵，走去車站，等車，路上想起世界觀設定，最後才看到追兵。我要知道哪裡拖、哪裡該切、哪裡該慢。
```

Expected behavior:

* Identifies event-list narration, late pressure, weak entry hook, and exposition drag.
* Separates what to cut, compress, move earlier, and expand.
* Rebuilds the scene around entry pressure, objective, obstacle, turn, cost, and emotional residue.
* Provides a concrete revised beat order or replacement passage.

## Test 12: Chapter and Information Pacing

Prompt:

```text
用 story-forge 幫我修一章大綱節奏：第一章先講 5000 字世界觀，第二章主角才遇到危機，第三章一次解釋反派身分和整個魔法規則。我要讀者想翻下一頁。
```

Expected behavior:

* Flags front-loaded exposition and reveal timing problems.
* Reorders information into action, clues, misreadings, cost, and consequence.
* Gives each chapter an opening hook, middle escalation or reveal, ending hook, and emotional residue.
* Keeps some mystery unresolved.

## Test 13: Whole-Book and Genre Rhythm

Prompt:

```text
用 story-forge 檢查我的全書節奏：前半本一直打架，沒有休息；中段連續六章都在解釋設定；愛情線突然告白，下一章就分手；結尾 Boss 戰兩頁結束。類型是末世懸疑加成人心理張力。
```

Expected behavior:

* Diagnoses whole-book monotony, exposition block, rushed emotional beats, and rushed climax.
* Proposes alternation among crisis, contrast, investigation, group conflict, intimacy, failure, temporary victory, and consequence.
* Applies genre rhythm: mystery clues, zombie/post-apocalyptic resource pressure, and mature psychological restraint/boundaries/consequences.
* Gives a concrete macro pacing map or chapter-block restructuring plan.

## Test 14: Novel Project Launch

Prompt:

```text
用 story-forge 啟動一個長篇小說專案。我只有一個靈感：一個會忘記死者名字的城市。請幫我釐清題材、類型、讀者承諾、主角傷口、核心衝突、結局方向，不要直接開始寫正文。
```

Expected behavior:

* Reads the request as Novel Completion Coach Mode, not only premise brainstorming.
* Produces a launch brief with topic, genre/subgenre, reader promise, protagonist wound, external goal, core conflict, antagonist pressure, ending direction, originality angle, and completion scope.
* Gives a concrete next step toward a full-book roadmap.
* Avoids over-polishing prose before the project has a direction.

## Test 15: Long-Form Roadmap

Prompt:

```text
用 story-forge 幫我做全書路線圖：主角是逃亡的宮廷抄寫員，發現王國歷史被人改寫。我要開場、第一轉折、中段反轉、低谷、高潮、結局餘韻。
```

Expected behavior:

* Builds a flexible full-book structure, not a generic three-act lecture.
* Defines opening hook, first turn, midpoint reversal, low point, climax, and ending residue.
* Connects every structural post to character wound, choices, cost, mystery pressure, and reader hunger.
* Leaves enough unresolved pressure for chapter-by-chapter drafting.

## Test 16: Chapter-by-Chapter Writing Companion

Prompt:

```text
用 story-forge 陪我寫第七章。前情：主角剛背叛朋友換取進城資格，但不知道朋友其實故意讓他背叛。先幫我定本章目標、衝突、揭露、代價、鉤子，再寫開頭 800 字。
```

Expected behavior:

* Provides a chapter brief before prose: goal, conflict, reveal, cost, hook, and continuity flags.
* Preserves betrayal, hidden intention, and relationship pressure.
* Drafts from the current story pressure instead of resetting context.
* Ensures the chapter ending direction makes the next chapter harder.

## Test 17: Writer's Block Diagnosis

Prompt:

```text
用 story-forge 診斷我為什麼卡稿：主角已經知道反派是誰，也拿到神器，朋友也原諒他了，但我還有十章才到結局。
```

Expected behavior:

* Does not only encourage the author.
* Diagnoses likely causes: information spent too early, main plot pressure gone, conflict resolved too soon, chapter functions unclear, consequences missing.
* Gives immediate repair options such as new cost, false victory, deeper antagonist pressure, moral compromise, relationship debt, or delayed/complicated reveal.
* Proposes the next chapter's function and multiple usable next steps.

## Test 18: Long-Form Continuity Ledger

Prompt:

```text
用 story-forge 幫我整理長篇連續性台帳。目前：女主角第三章右腿中箭，第五章把銀鑰匙交給弟弟，第八章和隊長決裂，第十章知道魔法會消耗記憶。我要避免後面寫崩。
```

Expected behavior:

* Tracks timeline, injuries, relationship changes, objects/resources, foreshadowing, mysteries, and world rules.
* Flags continuity risks such as injury recovery, key ownership, relationship trust, and memory-cost rules.
* Suggests what later chapters must honor or pay off.
* Does not invent contradictory canon.

## Test 19: Completion-Oriented Revision Pipeline

Prompt:

```text
用 story-forge 幫我安排修稿。我初稿還缺三章，但我一直在重修第一章句子。請把修訂流程分成初稿、結構稿、角色稿、節奏稿、對話稿、文風稿，告訴我現在不該做什麼。
```

Expected behavior:

* Identifies the manuscript phase as unfinished first draft.
* Warns against endless line-polishing before missing chapters exist.
* Splits work into first draft, structure draft, character draft, pacing draft, dialogue draft, and style draft.
* Gives this round's goal, deferred issues, deliverable, and completion criteria.

## Pass Criteria

Across these tests, a passing Story Forge response should:

* avoid empty praise
* name real craft weaknesses
* protect user-provided canon
* produce directly usable text when asked to revise, continue, outline, or rewrite
* preserve character voice differences
* diagnose structure before polishing sentences
* satisfy the relevant genre promise
* create consequences, hooks, and emotional residue
* identify high-concept hooks and emotional engines
* build series-capable world rules and long-term cast arcs
* distinguish cool setting from actual reader emotion
* transform inspiration from famous works into clearly original material
* handle mature 18+ topics with adult-only framing, consent awareness, psychological truth, and consequences
* diagnose pacing at scene, chapter, whole-book, emotional, information, and genre levels
* fix dragged setup, event lists, rushed climaxes, skipped residue, and premature exposition with concrete reorder/compress/expand/cut plans
* guide authors through novel project launch, long-form roadmaps, chapter-by-chapter drafting, writer's block diagnosis, continuity ledgers, first-draft completion, second-draft restructuring, and final revision
* prevent endless polishing by separating drafting, structural revision, character revision, pacing revision, dialogue revision, and style polish
