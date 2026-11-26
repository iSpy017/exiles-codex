---
title: Waystones
status: partial
tracker_topic: "Waystones & tiers"
tracker_note: "partial (0.5.x; T1–16 = area 65–80; T16 source not found; atlas-dependent)"
defaults: v=0.5.x
---
Status: partial. Tier table, drops, mods overview done. Not found: mod weights, per-rarity mod counts, Vaal/corruption outcomes on waystones, drop-chance percentages.
Version: 0.5.x (PoE2DB crawl 2026-11-23). No 1.0 check done; the tier/area-level mapping may change.
Sources: PoE2DB Waystones, Waystone (Tier N) pages, Waystone_Tier_Progression (tier 2).

## Tier to area level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Waystone tier N sets area level 64+N (T1 = 65 ... T16 = 80). Drop level of the item is 58 for T1, then 66 (T2) rising by 1 per tier to 80 (T16).
- src: poe2db:Waystones, poe2db:Waystone__28Tier_16_29 «PoE2DB Waystone (Tier 16)», tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Waystones are single-use. All 16 base types carry the corruptible flag; normal, magic, rare, unique rarities are allowed. Recheck for the new patch.

| Tier | Area lvl | Tier | Area lvl |
|---|---|---|---|
| 1 | 65 | 9 | 73 |
| 2 | 66 | 10 | 74 |
| 3 | 67 | 11 | 75 |
| 4 | 68 | 12 | 76 |
| 5 | 69 | 13 | 77 |
| 6 | 70 | 14 | 78 |
| 7 | 71 | 15 | 79 |
| 8 | 72 | 16 | 80 |


## Resistance penalty by area level
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Penalty at level 65 and above is -60 to resistances (steps: 54 = -40, 60 = -50, 65 = -60). So every waystone tier carries the max listed penalty.
- src: poe2db:Waystones (Level Resist Penalty), tier 2, crawl 2026-11-23
- notes: [INFERRED] "all tiers carry -60": table tops out at 65 and waystones start at 65.


## Upgrading by vendor recipe
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Three waystones of one tier combine into one of the next tier up (Three to One Reforge bench craft). Ladder seen from T1 to T2 up to T14 to T15. No T15 to T16 recipe appears on the T15 or T16 pages.
- src: poe2db:Waystone__28Tier_1_29 «PoE2DB Waystone (Tier 1)», tier 2, crawl 2026-11-23
- conf: single-source (each tier page repeats pattern)
- notes: T16 is not shown as a recipe output in the corpus; T16 source (drops) not found. [INFERRED] vendor ladder stops at T15 because no T15 input row exists.


## Tier progression from drops
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Only the final Powerful Map Boss in an area can drop a waystone higher than the area's tier. The final rare monster of a map can drop a waystone equal to the map's tier. Chance falls as tier goes up; waystone mods raise it. Cartographer's Strongboxes also drop waystones.
- src: poe2db:Waystone_Tier_Progression, poe2db:Map_Objective_Waystone_Drops, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent (boss quantity bonuses come from atlas passives and tablets, e.g. "of Pathways": 18-30% more waystones from map bosses, on a tablet). Exact percentages not found.


## Waystone mods: tradeoff pattern
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Each explicit mod makes monsters harder AND adds a bonus line (more waystones found, item rarity, pack size, or magic/rare monster count). Typical bonus sizes seen: waystones found +10%/15%/20%/25% more; rarity +10-16% more; pack size +6-10% more.
- src: poe2db:Waystones (Waystones Mods /107), tier 2, crawl 2026-11-23
- notes: Full 107-row list: link, not copied. Each row lists both a prefix/suffix tag and the reward line. Mod level shows 1 for all rows in the crawl; no tier gating visible.


## Mod picks that matter (examples)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Decision rows. Danger-flavoured mods to check before running: -4% to -10% maximum player resistances (suffix, +10% pack size, +25% waystones); extra-element prefixes (5-24% as extra Fire/Cold/Lightning/Chaos); armour break; poison/bleed on hit; reduced flask charges; less life/ES recovery; less cooldown recovery; periodic Enfeeble/Temporal Chains/Elemental Weakness curses; ground patches (ignite/chill/shock). Waystones-found boosters sit on the heavier mods (e.g. 25% more with +2/+3 projectiles or faster monsters).
- src: poe2db:Waystones, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent for the "worth it" judgment. No weights (PoE2DB: modifier weight information cannot be obtained from game files).


## Rerolling mods: Chaos Orb and omens
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Chaos Orb works as a reroll; four Omens make the next Chaos Orb replace all waystone mods with mods that avoid one reward type: Chaotic Rarity (no item rarity), Chaotic Quantity (no pack size), Chaotic Monsters (no monster rarity), Chaotic Effectiveness (no monster effectiveness).
- src: poe2db:Chaos_Orb, poe2db:Omen_of_Chaotic_Quantity, tier 2, crawl 2026-11-23
- notes: Details of other currencies on waystones not found in the corpus. Omen docs: [[crafting/omens]].


## Corruption of waystones
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
Waystone base types carry the "can be corrupted" flag. Vaal Orb corrupts any item unpredictably and corrupted items cannot be modified again. Specific waystone outcomes were not found.
- src: poe2db:Waystone__28Tier_16_29 «PoE2DB Waystone (Tier 16)», poe2db:Vaal_Orb, tier 2, crawl 2026-11-23
- conf: [INFERRED]: flag exists, but no waystone-specific Vaal outcome page was read.
- notes: Rare-waystone "desecrated" mods exist (19 listed, Abyssal-flavoured). Link: [PoE2DB Waystones](https://poe2db.tw/us/Waystones).


## Waystone tier gates
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Citadels require Tier 15+ waystones. Higher tiers also unlock higher-tier atlas passives (wiki line).
- src: poe2db:Citadel, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. See [[endgame/atlas]].
