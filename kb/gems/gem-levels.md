---
title: Gem Level vs Character Level
status: done
tracker_topic: "Gem level vs character level requirements"
tracker_note: "done (0.5.x; recheck 1.0)"
defaults: v=0.5.x
---

Version: 0.5.x / game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.

## Required character level per gem level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Gem level → required character level (persistent/skill gem example, Herald of Ice):

| Gem lvl | Char lvl | Gem lvl | Char lvl |
|---|---|---|---|
| 1 | — (0) | 11 | 41 |
| 2 | 3 | 12 | 46 |
| 3 | 6 | 13 | 52 |
| 4 | 10 | 14 | 58 |
| 5 | 14 | 15 | 64 |
| 6 | 18 | 16 | 66 |
| 7 | 22 | 17 | 72 |
| 8 | 26 | 18 | 78 |
| 9 | 31 | 19 | 84 |
| 10 | 36 | 20 | 90 |

- src: poe2db:Herald_of_Ice level table, tier 2, retrieved 2026-11-17; endpoints cross-checked: Mobalytics High Level Gems [S070] (L20 needs char 90), Mobalytics spell gem database [S047] (persistent gem levels 4–20 require char 10–90), tier 3
- conf: confirmed (L4 = 10, L20 = 90); single-source for the middle rows
- notes: [INFERRED] the same schedule applies to all skill/spirit gems (the Mobalytics ranges match for every gem listed) — spot-check another gem when convenient. Attribute requirements also rise with level and +5 per socketed support ([[gems/socketing-limits]]).


## Answers the spirit-gem seed question
- L8 spirit gem → char level 26 · L9 → 31 · L10 → 36 · L12 → 46.
- So the [[strategy/league-lifecycle-pricing]] play (sell campaign L8, buy L10/L12) needs char 36 for L10 and 46 for L12.

## Uncut gems make gems at their own level
@ v=0.5.x vol=? conf=confirmed date=2026-11-17 missing=vol
An uncut gem engraves a gem at the uncut gem's level; the same uncut gems also level up existing gems. Higher uncut gems drop in higher-level areas.
- Details in [[gems/uncut-gems]].

- src: poe2wiki Skill gem [S635], poe2wiki Uncut gem [S729], tier 2; Poe-Vault Gems Guide [S661], tier 3; retrieved 2026-11-17

## Gem levels above 20
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Level 20 is the normal cap. Corrupting (Vaal Orb) can add +1 level, and the +1 stays as you level it — so corrupt a low gem, then raise it with a L20 uncut gem to reach L21. Item/support bonuses ("+X to level") stack on top.
- src: Maxroll Corruption outcomes [S039], tier 3; Mobalytics Level 21 gems guide [S075], tier 3; poe2wiki Corrupted [S608] (corrupted gems can still be levelled with uncut gems), tier 2; retrieved 2026-11-17
- notes: Mobalytics' method uses an Omen of Corruption with the Vaal Orb → [[crafting/omens]], [[items/corruption]].
