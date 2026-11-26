# Waystones
Status: partial. Tier table, drops, mods overview done. Not found: mod weights, per-rarity mod counts, Vaal/corruption outcomes on waystones, drop-chance percentages.
Version: 0.5.x (PoE2DB crawl 2026-11-23). No 1.0 check done; the tier/area-level mapping may change.
Sources: PoE2DB Waystones, Waystone (Tier N) pages, Waystone_Tier_Progression (tier 2).

## Tier to area level
- Claim: Waystone tier N sets area level 64+N (T1 = 65 ... T16 = 80). Drop level of the item is 58 for T1, then 66 (T2) rising by 1 per tier to 80 (T16).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystones](https://poe2db.tw/us/Waystones), [PoE2DB Waystone (Tier 16)](https://poe2db.tw/us/Waystone__28Tier_16_29), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Tags: atlas-dependent. Waystones are single-use. All 16 base types carry the corruptible flag; normal, magic, rare, unique rarities are allowed. Recheck for the new patch.

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
- Claim: Penalty at level 65 and above is -60 to resistances (steps: 54 = -40, 60 = -50, 65 = -60). So every waystone tier carries the max listed penalty.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystones](https://poe2db.tw/us/Waystones) (Level Resist Penalty), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: [INFERRED] "all tiers carry -60": table tops out at 65 and waystones start at 65.

## Upgrading by vendor recipe
- Claim: Three waystones of one tier combine into one of the next tier up (Three to One Reforge bench craft). Ladder seen from T1 to T2 up to T14 to T15. No T15 to T16 recipe appears on the T15 or T16 pages.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystone (Tier 1)](https://poe2db.tw/us/Waystone__28Tier_1_29), tier 2, crawl 2026-11-23
- Confidence: single-source (each tier page repeats pattern)
- Notes: T16 is not shown as a recipe output in the corpus; T16 source (drops) not found. [INFERRED] vendor ladder stops at T15 because no T15 input row exists.

## Tier progression from drops
- Claim: Only the final Powerful Map Boss in an area can drop a waystone higher than the area's tier. The final rare monster of a map can drop a waystone equal to the map's tier. Chance falls as tier goes up; waystone mods raise it. Cartographer's Strongboxes also drop waystones.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystone_Tier_Progression](https://poe2db.tw/us/Waystone_Tier_Progression), [PoE2DB Map_Objective_Waystone_Drops](https://poe2db.tw/us/Map_Objective_Waystone_Drops), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Tags: atlas-dependent (boss quantity bonuses come from atlas passives and tablets, e.g. "of Pathways": 18-30% more waystones from map bosses, on a tablet). Exact percentages not found.

## Waystone mods: tradeoff pattern
- Claim: Each explicit mod makes monsters harder AND adds a bonus line (more waystones found, item rarity, pack size, or magic/rare monster count). Typical bonus sizes seen: waystones found +10%/15%/20%/25% more; rarity +10-16% more; pack size +6-10% more.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystones](https://poe2db.tw/us/Waystones) (Waystones Mods /107), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Full 107-row list: link, not copied. Each row lists both a prefix/suffix tag and the reward line. Mod level shows 1 for all rows in the crawl; no tier gating visible.

## Mod picks that matter (examples)
- Claim: Decision rows. Danger-flavoured mods to check before running: -4% to -10% maximum player resistances (suffix, +10% pack size, +25% waystones); extra-element prefixes (5-24% as extra Fire/Cold/Lightning/Chaos); armour break; poison/bleed on hit; reduced flask charges; less life/ES recovery; less cooldown recovery; periodic Enfeeble/Temporal Chains/Elemental Weakness curses; ground patches (ignite/chill/shock). Waystones-found boosters sit on the heavier mods (e.g. 25% more with +2/+3 projectiles or faster monsters).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystones](https://poe2db.tw/us/Waystones), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Tags: atlas-dependent for the "worth it" judgment. No weights (PoE2DB: modifier weight information cannot be obtained from game files).

## Rerolling mods: Chaos Orb and omens
- Claim: Chaos Orb works as a reroll; four Omens make the next Chaos Orb replace all waystone mods with mods that avoid one reward type: Chaotic Rarity (no item rarity), Chaotic Quantity (no pack size), Chaotic Monsters (no monster rarity), Chaotic Effectiveness (no monster effectiveness).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Chaos_Orb](https://poe2db.tw/us/Chaos_Orb), [PoE2DB Omen_of_Chaotic_Quantity](https://poe2db.tw/us/Omen_of_Chaotic_Quantity), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Details of other currencies on waystones not found in the corpus. Omen docs: [[crafting/omens]].

## Corruption of waystones
- Claim: Waystone base types carry the "can be corrupted" flag. Vaal Orb corrupts any item unpredictably and corrupted items cannot be modified again. Specific waystone outcomes were not found.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystone (Tier 16)](https://poe2db.tw/us/Waystone__28Tier_16_29), [PoE2DB Vaal_Orb](https://poe2db.tw/us/Vaal_Orb), tier 2, crawl 2026-11-23
- Confidence: [INFERRED]: flag exists, but no waystone-specific Vaal outcome page was read.
- Notes: Rare-waystone "desecrated" mods exist (19 listed, Abyssal-flavoured). Link: [PoE2DB Waystones](https://poe2db.tw/us/Waystones).

## Waystone tier gates
- Claim: Citadels require Tier 15+ waystones. Higher tiers also unlock higher-tier atlas passives (wiki line).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Citadel](https://poe2db.tw/us/Citadel), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Tags: atlas-dependent. See [[endgame/atlas]].
