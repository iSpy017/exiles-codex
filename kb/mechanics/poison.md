---
title: Poison
status: done
tracker_topic: "Poison"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Basics
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Poison deals chaos damage over time, 2 s default, and bypasses Energy Shield.

- src: game keywords "Poison", tier 2; poe2wiki Poisons [S715], tier 2; Mobalytics Ailments [S052], tier 3; retrieved 2026-11-17

## Needs an explicit poison chance
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Damage never creates poison chance — you need a stated source of poison chance. Physical and chaos hit damage then set its strength.

- src: game keywords "Poison", tier 2; poe2wiki Poisons [S715], tier 2; retrieved 2026-11-17

## Poison damage
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Base poison = 20% of the hit's pre-mitigation physical + chaos damage, per second. Your damage modifiers don't change it afterwards. Enemy mitigation reducers (e.g. Shock) increase it; hit-only effects (e.g. penetration) don't.
- src: game keywords "Poison", tier 2; poe2wiki Ailment [S601], tier 2; Mobalytics Poison [S080], tier 3; retrieved 2026-11-17
- notes: Mobalytics' general ailments page lists only "Physical" in the base — its poison page says phys+chaos, matching game data; treated as an omission, not a conflict.


## Stack limit
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Default limit is 1 active poison per target. All poisons stay with their own timers, but only the highest-damage ones up to your stack limit deal damage. The limit also governs poisons from your minions/other sources. Raised by e.g. the Escalating Poison support and passive notables (named in Mobalytics: Stacking Toxins, Building Toxins).
- src: poe2wiki Poisons [S715], tier 2; Mobalytics Poison [S080], tier 3; Mobalytics Ailments [S052], tier 3; retrieved 2026-11-17
- conf: confirmed (limit 1 + highest-first); named sources single-source (verify names in skill_gems.json / passive tree)
- notes: big change from PoE1 where poisons stacked freely.
