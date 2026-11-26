---
title: Resistances & Caps
status: done
tracker_topic: "Resistances & caps"
tracker_note: "done (0.5.x; penalty schedule needs 1.0 check)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0 — campaign penalty WILL change (1.0 removes Interludes, adds Acts 5–6).
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What resistances do
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Fire, cold, lightning and chaos resistance each reduce damage of that type, up to a maximum. Fire/cold/lightning are the elemental resistances.
- src: gear, passives, quest rewards. game keywords "Resistances", tier 2; Mobalytics Resistances [S083], tier 3; retrieved 2026-11-17 poe2wiki Chaos resistance [S677], tier 2.
- notes: e.g. 1000 fire damage at 75% fire res → 250 taken. Each point matters more near the cap: 60→70% cuts damage taken by a quarter (400→300 per 1000).


## Caps
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Default maximum for elemental and chaos resistance is 75%. Maximum resistance can't go above 90%. "Uncapped" resistance (shown in brackets on the character panel) is your total before the cap; "overcapped" is the amount above your max.

- src: game keywords "Maximum Resistances", "Uncapped Resistance", "Overcapped Resistance", tier 2; poe2wiki Maximum Resistances [S704], tier 2; retrieved 2026-11-17

## Campaign penalty (0.5.x schedule)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Elemental resistance drops by 10% around each act end up to Act 4, then by area level through the Interludes: −10% (Act 2), −20% (Act 3), −30% (Act 4), −40% (area level 54–59), −50% (60–64), −60% (65+, endgame). It's permanent and unavoidable.
- src: poe2wiki Chaos Resistance [S605] (table), poe2wiki Maximum Resistances [S704], tier 2; Mobalytics Resistances [S083] (−10% per act), tier 3; GGG forum player answers (−60% endgame), tier 5; retrieved 2026-11-17
- vol: may-change — needs-1.0-check (Interludes removed in 1.0)
- conf: confirmed for −60% endgame total; single-source for the area-level breakpoints
- notes: game keyword text only says elemental res "are lowered as you progress". Practical: endgame needs 135% uncapped per element to sit at 75% — [INFERRED] arithmetic. Campaign quests give some permanent resistance back → [[campaign/permanent-rewards]]. Does the penalty also hit chaos? The wiki table sits on the chaos page but wording says "elemental" — verify.


## Lowering enemy resistance
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Exposure, curses and other reductions can push enemy resistance negative (more damage taken). "Ignore resistance" treats it as 0%. "Resisted by other value" replaces the target's resistance with a fixed value that penetration can't touch. Penetration only works on hits and stops at 0%.
- src: game keywords "Exposure", "Ignoring Resistances", "Resisted by Other Value", "Resistance Penetration", tier 2; Mobalytics Resistances [S083], tier 3; retrieved 2026-11-17
- notes: detail in [[mechanics/exposure-penetration]].


## Monster resistance mods
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
"Fire/Cold/Lightning Resistant" monster mods give +50% to that resistance and +10% to its maximum; "Chaos Resistant" gives +50% chaos res; an "Elemental Resistance Aura" gives allies within 5 m +35% to all elemental res.
- src: game keywords (monster modifier entries), tier 2, retrieved 2026-11-17
- conf: single-source (game data)
