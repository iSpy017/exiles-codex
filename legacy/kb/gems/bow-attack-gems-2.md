# Bow attack gems (2/2): Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder

Status: done for these four (levels 1-21 rows from PoE2DB). Companion: [[gems/bow-attack-gems]]. Not covered: Rain of Arrows, Snipe, Tornado Shot, Rapid Shot, Barrage, Spiral Volley, Explosive Shot (pages exist in corpus, not read).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB [Escape Shot](https://poe2db.tw/us/Escape_Shot), [Freezing Salvo](https://poe2db.tw/us/Freezing_Salvo), [Gas Arrow](https://poe2db.tw/us/Gas_Arrow), [Herald of Thunder](https://poe2db.tw/us/Herald_of_Thunder); tier 2.
Columns: gem level | character level required (Dex required) | mana | attack damage % | extra. Level 21 has no requirement shown.
Build context: [[builds/ice-shot-deadeye-levelling-0.5.5]], [[strategy/practice-build-0.5.5]].

## Escape Shot
- Claim: Tier 1. Tags: Attack, AoE, Projectile, Trigger, Cold. No attack-speed line; adds 0.7 s to total attack time. Mana (11-74). Bow required. Converts 80% physical to cold. Projectile count cannot be modified. Impact radius 2.4 m.
- Mechanic: leap backwards, firing an icy arrow at the spot you left; chills/freezes enemies there and spawns Ice Fragments on impact. Fragments: 100% cold conversion, detonate after 2.5 s, explosion radius 2 m, 80% more projectile speed, 7 to 11 fragments by level (12 at level 21). Fragment damage (60-187)%.
- Level-scaling: 300% more Chill magnitude and Freeze buildup at level 1, +15 per level, 585% at level 20.
- Quality: up to 120% more Freeze buildup; up to 40% increased damage with hits against Frozen enemies.
- Recommended supports: 1 Cold Attunement, Ice Bite I, Deep Freeze; 2 Freeze, Frost Nexus, Short Fuse I; 3 Magnified Area II, Alignment I; 4 Cold Exposure, Culling Strike I, Short Fuse II; 5 Close Combat II, Holy Descent, Long Fuse II.

| Lv | Req (Dex) | Mana | Atk dmg % | Fragment dmg % | Chill/Freeze more % | Fragments |
|---|---|---|---|---|---|---|
| 1 | 0 (4) | 11 | 65 | 60 | 300 | 7 |
| 5 | 14 (28) | 18 | 94 | 85 | 360 | 8 |
| 7 | 22 (41) | 23 | 110 | 98 | 390 | 8 |
| 10 | 36 (65) | 31 | 133 | 115 | 435 | 9 |
| 12 | 46 (82) | 38 | 152 | 127 | 465 | 9 |
| 14 | 58 (103) | 45 | 173 | 140 | 495 | 10 |
| 16 | 66 (116) | 54 | 199 | 154 | 525 | 10 |
| 18 | 78 (137) | 63 | 229 | 170 | 555 | 11 |
| 20 | 90 (157) | 74 | 265 | 187 | 585 | 11 |
| 21 | - | 80 | 286 | 196 | 600 | 12 |

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: pairs with Freezing Salvo, which detonates nearby Ice Fragments. Column reading (fragment dmg = 4th value, fragment count) is mine from header ranges, [INFERRED]: values match the page's (60-187)% and (7-11) ranges.

## Freezing Salvo
- Claim: Tier 3. Tags: Attack, AoE, Projectile, Cold, Repeatable. No attack-speed line. Mana (15-105). Bow required. Converts 80% physical to cold. Impact radius 1.2 m.
- Mechanic: gains a Seal every 0.75 s, max 10 (quality up to +4 max Seals). Using it fires a projectile and breaks Seals; it repeats once per Seal broken. Each normal repeat also repeats once more at a different Ice Fragment in its area, detonating that fragment at once. Projectile-count modifiers add repeats instead.
- Quality: up to 40% more Freeze buildup; up to +4 max Seals.
- Recommended supports: 1 Cold Attunement, Concentrated Area, Ice Bite I; 2 Cold Penetration, Freeze, Embitter; 3 Close Combat I, Alignment I, Stoicism I; 4 Execute II, Alignment II, Hit and Run; 5 Projectile Acceleration III, Close Combat II, Cold Mastery.

| Lv | Req (Dex) | Mana | Atk dmg % | Chill/Freeze more % |
|---|---|---|---|---|
| 1 | 0 (4) | 15 | 48 | 30 |
| 5 | 14 (28) | 26 | 68 | 38 |
| 7 | 22 (41) | 33 | 79 | 42 |
| 10 | 36 (65) | 44 | 92 | 48 |
| 12 | 46 (82) | 54 | 101 | 52 |
| 14 | 58 (103) | 64 | 112 | 56 |
| 16 | 66 (116) | 76 | 123 | 60 |
| 18 | 78 (137) | 90 | 136 | 64 |
| 20 | 90 (157) | 105 | 150 | 68 |
| 21 | - | 113 | 157 | 70 |

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: 0.5.0 unified Seal rules across Unleash/Expand/Salvo/Freezing Salvo; the "Salvo" support also appears in the Ice Shot and Lightning Arrow recommendations.

## Gas Arrow
- Claim: Tier 7. Tags: Attack, AoE, Projectile, Fire, Chaos, Duration, Repeatable. No attack-speed line. Mana (9-62). Bow required. Impact radius 1.8 m.
- Mechanic: arrow lands on the ground and leaves a poison gas cloud (4 s, radius 1.8 m, +20% radius per second up to +80%, limit 6 clouds). The cloud poisons without hitting; it detonates when hit by a Detonator skill or touched by an Ignited enemy, causing a fire explosion (100% physical to fire).
- Quality: +0.4 m impact/cloud radius and up to 20% more fire damage.
- Recommended supports: 1 Fire Attunement, Prolonged Duration I, Corrosion; 2 Bursting Plague, Deadly Poison I, Commiserate; 3 Magnified Area II, Salvo, Persistent Ground II; 4 Overabundance II, Deadly Poison II, Nova Projectiles II; 5 Poison III, Chaos Mastery, Persistent Ground III.

| Lv | Req (Dex) | Mana | Arrow % | Cloud % | Explosion % |
|---|---|---|---|---|---|
| 1 | 0 (4) | 9 | 30 | 70 | 90 |
| 5 | 14 (28) | 15 | 43 | 100 | 128 |
| 7 | 22 (41) | 19 | 49 | 115 | 147 |
| 10 | 36 (65) | 26 | 57 | 134 | 172 |
| 12 | 46 (82) | 32 | 63 | 148 | 190 |
| 14 | 58 (103) | 38 | 70 | 163 | 209 |
| 16 | 66 (116) | 45 | 77 | 180 | 231 |
| 18 | 78 (137) | 53 | 85 | 198 | 255 |
| 20 | 90 (157) | 62 | 94 | 218 | 281 |
| 21 | - | 67 | 98 | 229 | 295 |

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: header ranges (30-94, 70-218, 90-281) match the three columns.

## Herald of Thunder (not a bow-only skill)
- Claim: Tier 4 Spirit gem (page title "Uncut Spirit Gem"). Tags: Attack, Persistent, AoE, Lightning, Herald, Payoff. Reserves 30 Spirit. Works with any martial weapon.
- Mechanic: while active, killing a Shocked enemy with a non-Herald Attack hit makes your next 2 Attack hits (3 from level 11, 4 at level 21) also call lightning bolts that damage surrounding enemies; bolt radius 1 m, cannot be evaded, 100% physical to lightning.
- Quality: up to +2 bolt-triggering hits; up to 20% increased lightning damage from the buff.
- Recommended supports: 1 Concentrated Area, Precision I; 2 Maim, Herbalism I; 3 Elemental Focus, Deadly Herald; 4 Precision II, Living Lightning II; 5 Blind II, Culling Strike II.

| Lv | Req (Dex) | Bolt dmg % | Hits |
|---|---|---|---|
| 1 | 0 (4) | 30 | 2 |
| 5 | 14 (28) | 44 | 2 |
| 7 | 22 (41) | 51 | 2 |
| 10 | 36 (65) | 62 | 2 |
| 12 | 46 (82) | 70 | 3 |
| 14 | 58 (103) | 80 | 3 |
| 16 | 66 (116) | 92 | 3 |
| 18 | 78 (137) | 106 | 3 |
| 20 | 90 (157) | 122 | 3 |
| 21 | - | 132 | 4 |

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: no attack speed line. The level-table block shows "Mana: 30", the same number as the 30 Spirit reservation — [INFERRED] the same label quirk as minion gem pages, where spirit appears under a "Mana" label ([[gems/minion-skills]]); no separate use cost found. The page also lists a second table under "The Coming Calamity" (unique-item version, same values, no Dex column).
