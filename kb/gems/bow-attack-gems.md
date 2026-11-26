---
title: Bow attack gems (1/2): Ice Shot, Lightning Arrow, Lightning Rod
status: done
tracker_topic: "Bow attack gems — per-level (Ice Shot, Lightning Arrow, Lightning Rod, …)"
tracker_note: "done (0.5.x; 2 conflicts: Lightning Rod chains, Ice Shot shards)"
defaults: v=0.5.x
merged_from: [bow-attack-gems.md, bow-attack-gems-2.md, bow-attack-gems-3.md, bow-attack-gems-4.md]
---

Status: done for these three (levels 1-21 rows from PoE2DB). Companion: [[gems/bow-attack-gems]] (Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB gem pages poe2db:Ice_Shot, poe2db:Lightning_Arrow, poe2db:Lightning_Rod; tier 2.
Build context: [[builds/ice-shot-deadeye-levelling-0.5.5]], [[strategy/practice-build-0.5.5]]. Table columns: gem level | character level required | Dex required | mana cost | Attack Damage % of base. Level 21 has no requirement shown (only reachable via +gem-level effects, [INFERRED]: PoE2DB lists blank requirements for 21+).

## Ice Shot
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 9 gem. Tags: Attack, Projectile, Cold, Repeatable. Attack speed 90% of base. Attack damage (95-344)% of base over gem levels 1-20. Mana (6-40). Projectile speed 32.6 m/s. Requires a bow. Arrow converts 80% of physical to cold; 50% more Chill magnitude; 25% more Freeze buildup (on the arrow).
- Mechanic (paraphrased): fires an icy arrow that, on hit, sprays a cone of ice shards. Shards are a second stat set: all physical converted to cold, base 8-11 projectiles, 300-degree total spread, 45 spread radius.
- Quality: up to +30% more Chill magnitude (stat shown as 0-30) and up to 40% reduced movement-speed penalty while using skills when moving.
- Level-capped effects: none found; shard projectile count shows only as a range (8-11), no per-level breakdown on the page.
- Recommended supports (PoE2DB, by tier): 1 Cold Attunement, Chain I, Ice Bite I; 2 Longshot I, Elemental Armament II, Frozen Spite; 3 Pierce II, Salvo, Deliberation; 4 Projectile Acceleration II, Spectral Volley, Nova Projectiles II; 5 Pierce III, Alignment III.

| Lv | Req char lv / Dex | Mana | Attack dmg % |
|---|---|---|---|
| 1 | 0 / 4 | 6 | 95 |
| 5 | 14 / 28 | 10 | 136 |
| 7 | 22 / 41 | 12 | 158 |
| 10 | 36 / 65 | 17 | 188 |
| 12 | 46 / 82 | 20 | 210 |
| 14 | 58 / 103 | 24 | 237 |
| 16 | 66 / 116 | 29 | 267 |
| 18 | 78 / 137 | 34 | 303 |
| 20 | 90 / 157 | 40 | 344 |
| 21 | - | 43 | 367 |

- conf: single-source (one PoE2DB page; header ranges match table)
- notes: version history says 0.5.0 removed the shards' 25% more Freeze buildup; 0.4.0 raised conversion to 80%. Table's 4th value is 100% at every level (meaning not stated on page); see report Conflicts.


## Lightning Arrow
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 1 gem. Tags: Attack, AoE, Projectile, Lightning, Chaining, Repeatable. Attack speed 90% of base. Attack damage (80-250)% of base at levels 1-20. Mana (6-40). Projectile speed 54 m/s. Requires a bow. Projectile converts 80% of physical to lightning; the chain beam converts 100%.
- Mechanic: the charged arrow, on hitting an enemy or wall, fires chaining lightning beams at nearby enemies; the arrow itself cannot chain; beam targeting radius 3.2 m. Beams hit up to 2 additional enemies at levels 1-9, 3 at levels 10-19, 4 at level 20+. Beam stat set shows "Chains 2 times". Interacts with [[gems/bow-attack-gems]] Lightning Rod: arrows stuck in ground can be chained to; Lightning Arrow causes rod bursts with a 100 ms delay override (0.4.0 note: burst at most once per 0.1 s).
- Quality: up to 40% more chance to Shock; up to 30% chance for lightning damage with hits to be lucky.
- Recommended supports: 1 Lightning Attunement, Chain I, Innervate; 2 Shock Conduction, Electrocute, Volt (names space-separated on page; boundaries not certain); 3 Fork, Salvo, Charged Shots I; 4 Projectile Acceleration II, Spectral Volley, Nova Projectiles II; 5 Chain III, Alignment III, Charged Shots II.

| Lv | Req char lv / Dex | Mana | Attack dmg % | Extra beams |
|---|---|---|---|---|
| 1 | 0 / 4 | 6 | 80 | 2 |
| 5 | 14 / 28 | 10 | 114 | 2 |
| 7 | 22 / 41 | 12 | 131 | 2 |
| 10 | 36 / 65 | 17 | 153 | 3 |
| 12 | 46 / 82 | 21 | 169 | 3 |
| 14 | 58 / 103 | 25 | 186 | 3 |
| 16 | 66 / 116 | 29 | 205 | 3 |
| 18 | 78 / 137 | 35 | 226 | 3 |
| 20 | 90 / 157 | 40 | 250 | 4 |
| 21 | - | 44 | 262 | 4 |

- notes: table shows beams as "N, 1"; I read the first number as the beam count (matches the page's "(2-4)" header); the trailing 1 is unexplained. 0.5.0: multiple beams can no longer chain onto the same target. 0.5.4b fix: Lightning Arrow could not chain to rods created by Shockchain Arrow.


## Lightning Rod
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 1 gem. Tags: Attack, AoE, Projectile, Sustained, Lightning, Duration, Repeatable. Attack speed 120% of base. Attack damage (26-94)% at levels 1-20. Mana (4-30). Projectile speed 32.6 m/s. Bow required. 100% physical converted to lightning.
- Mechanic: arrow drops from above, bursts (2 m radius) and stays stuck; chaining lightning beams can chain to it, after which it charges briefly and bursts again. Lightning Arrow shortens that delay. Arrow lasts up to 20 s, vanishes after being chained to 8 times, max 10 active arrows.
- Quality: up to 20% chance of an additional burst on impact; up to 20% more attack speed.
- Level-capped effects: none found.
- Recommended supports: 1 Multishot I, Magnified Area I, Elemental Armament I; 2 Elemental Armament II, Overreach, Durability; 3 Elemental Focus, Alignment I, Deliberation; 4 Execute II, Alignment II; 5 Blind II, Elemental Armament III, Charged Shots II.

| Lv | Req char lv / Dex | Mana | Attack dmg % |
|---|---|---|---|
| 1 | 0 / 4 | 4 | 26 |
| 5 | 14 / 28 | 7 | 37 |
| 7 | 22 / 41 | 9 | 43 |
| 10 | 36 / 65 | 13 | 51 |
| 12 | 46 / 82 | 15 | 58 |
| 14 | 58 / 103 | 18 | 65 |
| 16 | 66 / 116 | 22 | 73 |
| 18 | 78 / 137 | 26 | 83 |
| 20 | 90 / 157 | 30 | 94 |
| 21 | - | 33 | 100 |

- notes: version history (0.2.0) says arrows vanish after 6 chains, but the current page says 8 (no entry for the change); see report Conflicts. 0.4.0 cut the active-rod limit from 20 to 10.


<!-- merged from kb/gems/bow-attack-gems-2.md -->
Part title: Bow attack gems (2/2): Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder

Status: done for these four (levels 1-21 rows from PoE2DB). Companion: [[gems/bow-attack-gems]]. Not covered: Rain of Arrows, Snipe, Tornado Shot, Rapid Shot, Barrage, Spiral Volley, Explosive Shot (pages exist in corpus, not read).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB poe2db:Escape_Shot, poe2db:Freezing_Salvo, poe2db:Gas_Arrow, poe2db:Herald_of_Thunder; tier 2.
Columns: gem level | character level required (Dex required) | mana | attack damage % | extra. Level 21 has no requirement shown.
Build context: [[builds/ice-shot-deadeye-levelling-0.5.5]], [[strategy/practice-build-0.5.5]].

## Escape Shot
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 1. Tags: Attack, AoE, Projectile, Trigger, Cold. No attack-speed line; adds 0.7 s to total attack time. Mana (11-74). Bow required. Converts 80% physical to cold. Projectile count cannot be modified. Impact radius 2.4 m.
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

- notes: pairs with Freezing Salvo, which detonates nearby Ice Fragments. Column reading (fragment dmg = 4th value, fragment count) is mine from header ranges, [INFERRED]: values match the page's (60-187)% and (7-11) ranges.


## Freezing Salvo
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 3. Tags: Attack, AoE, Projectile, Cold, Repeatable. No attack-speed line. Mana (15-105). Bow required. Converts 80% physical to cold. Impact radius 1.2 m.
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

- notes: 0.5.0 unified Seal rules across Unleash/Expand/Salvo/Freezing Salvo; the "Salvo" support also appears in the Ice Shot and Lightning Arrow recommendations.


## Gas Arrow
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 7. Tags: Attack, AoE, Projectile, Fire, Chaos, Duration, Repeatable. No attack-speed line. Mana (9-62). Bow required. Impact radius 1.8 m.
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

- notes: header ranges (30-94, 70-218, 90-281) match the three columns.


## Herald of Thunder (not a bow-only skill)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 4 Spirit gem (page title "Uncut Spirit Gem"). Tags: Attack, Persistent, AoE, Lightning, Herald, Payoff. Reserves 30 Spirit. Works with any martial weapon.
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

- notes: no attack speed line. The level-table block shows "Mana: 30", the same number as the 30 Spirit reservation — [INFERRED] the same label quirk as minion gem pages, where spirit appears under a "Mana" label ([[gems/minion-skills]]); no separate use cost found. The page also lists a second table under "The Coming Calamity" (unique-item version, same values, no Dex column).


<!-- merged from kb/gems/bow-attack-gems-3.md -->
Part title: Bow attack gems (3/4): Rain of Arrows, Snipe, Tornado Shot

Status: done for these three (levels 1-21 rows from PoE2DB). Companions: [[gems/bow-attack-gems]] (Ice Shot, Lightning Arrow, Lightning Rod), [[gems/bow-attack-gems]] (Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder), [[gems/bow-attack-gems]] (Spiral Volley, Rapid Shot, Explosive Shot, Barrage).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: poe2db:Rain_of_Arrows, poe2db:Snipe, poe2db:Tornado_Shot; tier 2.
Table columns: gem level | character level required / Dex required | mana | other columns as labelled. Level 21 has no requirement shown on PoE2DB ([INFERRED]: blank for levels beyond 20, reachable only via +gem-level effects). All three require a bow.

## Rain of Arrows
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 9. Tags: Attack, AoE, Projectile, Sustained. Attack speed 80% of base. Attack damage (50-181)% of base at levels 1-20. Mana (15-103). Projectile speed 32.6 m/s.
- Mechanic (paraphrased): fires arrows into the air that rain down in a 3.6 m radius area (impact radius 0.7 m). One arrow lands every 0.08 s; each enemy can be hit only once per 0.12 s; max 1 rain at a time. Fires (30-39) arrows, and 150% more arrows if a Frenzy Charge was consumed (the skill consumes one when available). Projectile speed modifiers also change the landing frequency. The skill can be performed while moving (movement speed penalty while performing, like other bow skills).
- Quality: up to 20% faster arrow fall and up to 20% more damage.
- Recommended supports (PoE2DB): 1 Brutality I, Perpetual Charge, Pin I; 2 Brutality II, Armour Break I, Heightened Charges; 3 Longshot II, Alignment I, Deliberation; 4 Alignment II, Incision, Impale; 5 Bleed IV, Brutality III, Stoicism II.

| Lv | Req char lv / Dex | Mana | Attack dmg % | Arrows (base) |
|---|---|---|---|---|
| 1 | 0 / 4 | 15 | 50 | 30 |
| 5 | 14 / 28 | 26 | 72 | 32 |
| 7 | 22 / 41 | 32 | 83 | 33 |
| 10 | 36 / 65 | 44 | 99 | 34 |
| 12 | 46 / 82 | 53 | 111 | 35 |
| 14 | 58 / 103 | 63 | 125 | 36 |
| 16 | 66 / 116 | 75 | 141 | 37 |
| 18 | 78 / 137 | 88 | 159 | 38 |
| 20 | 90 / 157 | 103 | 181 | 39 |
| 21 | - | 111 | 193 | 40 |

- conf: single-source (header ranges 50-181, 30-39, 15-103 match table)
- notes: table shows damage as "N%, N%, N%" (three identical values) and arrows as "N, 1, 1"; I read the first value of each, which matches the header ranges. The extra 1s are unexplained. Version history: 0.5.0 fixed extra-projectile chance stats not applying to skills like this.


## Snipe
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 3. Tags: Attack, AoE, Projectile, Cold, Channelling, Payoff, Repeatable. Attack speed 45% of base. Mana cost is per second: (17.55-118.57)/s (table rounds to whole numbers). Projectile speed 32.6 m/s.
- Mechanic (paraphrased): channel to charge the bow, then release. A release with Perfect Timing (window 300 ms base) makes the arrow explode on impact and consume Freeze from the directly hit enemy; consuming Freeze enhances the explosion into a separate "Icy Blast" stat set. Arrow attack-speed modifiers also affect the skill's cost. Minimum channel time 300 ms (hidden stat).
- Damage by stat set, levels 1-20: arrow (100-312)%; Explosion (400-1449)%, radius 2.5 m; Icy Blast (630-3067)%, radius 3 m, converts 100% physical to cold, with (31-50)% more damage vs explosions originating from a Unique enemy.
- Quality: explosion radius up to +0.4 m, up to 20% longer Perfect Timing window, up to 20% more attack speed.
- Recommended supports (PoE2DB): 1 Brutality I, Hourglass, Window of Opportunity I; 2 Brutality II, Longshot I; 3 Bleed II, Steadfast II, Deadly Resolve; 4 Execute II, Impale, Perfection; 5 Bleed III, Brutality III, Heft.

| Lv | Req char lv / Dex | Mana/s | Arrow % | Explosion % | Icy Blast % | Unique more dmg % |
|---|---|---|---|---|---|---|
| 1 | 0 / 4 | 18 | 100 | 400 | 630 | 31 |
| 5 | 14 / 28 | 30 | 142 | 573 | 912 | 35 |
| 7 | 22 / 41 | 37 | 164 | 664 | 1074 | 37 |
| 10 | 36 / 65 | 51 | 191 | 790 | 1326 | 40 |
| 12 | 46 / 82 | 61 | 211 | 886 | 1536 | 42 |
| 14 | 58 / 103 | 73 | 233 | 997 | 1798 | 44 |
| 16 | 66 / 116 | 86 | 257 | 1125 | 2127 | 46 |
| 18 | 78 / 137 | 101 | 283 | 1275 | 2541 | 48 |
| 20 | 90 / 157 | 119 | 312 | 1449 | 3067 | 50 |
| 21 | - | 128 | 327 | 1545 | 3374 | 51 |

- conf: single-source (each column's level 1/20 values match the page's header ranges)
- notes: table lists the arrow value three times, then Explosion, then Icy Blast; last column = "% more damage vs Unique-origin explosions". Version history: 0.5.0 lowered the damage numbers (arrow 133-343 to 121-312 at levels 3-20 per the log; explosion and Icy Blast changed too) and allowed Mirage Archer to use channelled skills; 0.4.0 removed the Heavy Stun interaction. Synergy with Freeze sources: [[gems/bow-attack-gems]] Ice Shot is a cold bow gem.


## Tornado Shot
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 11. Tags: Attack, AoE, Projectile, Physical, Duration, Repeatable, Wind. Attack speed 120% of base. Attack damage (50-156)% of base. Mana (13-88). Projectile speed 21.73 m/s.
- Mechanic (paraphrased): fires a shot skyward that creates a Tornado where it lands. The Tornado deals physical damage over time, (4.3-208.7) per second at levels 1-20, and Hinders enemies inside. Arrows (also thrown spears and crossbow bolts) fired at it are sucked in and it spits out 3 copies of each, in a ring. Copied projectiles deal (41-60)% less damage, travel at most 6 m, and cannot be copied again. Limit 1 Tornado, max duration 15 s. Projectile damage modifiers apply to the DoT; impact radius 1 m.
- Quality: copied projectiles deal up to +15% more damage; up to +2 to the Tornado limit.
- Recommended supports (PoE2DB): 1 Prolonged Duration I, Overabundance I, Slow Potency; 2 Maim, Durability; 3 Magnified Area II, Prolonged Duration II; 4 Efficiency II, Overabundance II; 5 Blind II, Physical Mastery, Elemental Armament III.

| Lv | Req char lv / Dex | Mana | Attack dmg % | Tornado DoT /s |
|---|---|---|---|---|
| 1 | 0 / 4 | 13 | 50 | 4.3 |
| 5 | 14 / 28 | 22 | 71 | 16 |
| 7 | 22 / 41 | 28 | 82 | 25 |
| 10 | 36 / 65 | 37 | 96 | 43.9 |
| 12 | 46 / 82 | 45 | 106 | 61.4 |
| 14 | 58 / 103 | 54 | 116 | 84.5 |
| 16 | 66 / 116 | 64 | 128 | 114.9 |
| 18 | 78 / 137 | 76 | 141 | 155.2 |
| 20 | 90 / 157 | 88 | 156 | 208.7 |
| 21 | - | 96 | 164 | 241.8 |

- notes: table damage column is "N%, N%, N%, 100%"; I read the first value (matches header 50-156). The fourth value (constant 100%) is unexplained on the page. 0.4.0 only added the Wind tag.


<!-- merged from kb/gems/bow-attack-gems-4.md -->
Part title: Bow attack gems (4/4): Spiral Volley, Rapid Shot, Explosive Shot, Barrage

Status: done for these four (levels 1-21 rows from PoE2DB). Companions: [[gems/bow-attack-gems]], [[gems/bow-attack-gems]], [[gems/bow-attack-gems]] (Rain of Arrows, Snipe, Tornado Shot).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB poe2db:Spiral_Volley, poe2db:Rapid_Shot, poe2db:Explosive_Shot, poe2db:Barrage; tier 2.
Weapon: Spiral Volley needs a bow; Rapid Shot and Explosive Shot need a CROSSBOW (not bows; included because PoE2DB groups them with bow gems); Barrage needs bow or spear. Level 21 has no requirement shown ([INFERRED]: blank beyond level 20).

## Spiral Volley
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 13. Tags: Attack, Projectile, Sustained. No attack-speed line shown. Attack damage (66-206)% of base. Mana (6-64). Projectile speed 32.6 m/s.
- Mechanic (paraphrased): loads a volley of enchanted arrows and fires them in a circle while spinning forward, aiming straight at targets where possible. Fires 25 arrows; each target can be hit only once; adds 0.4 s to total attack time. Consumes Frenzy Charges: 30% more damage per charge consumed, 100% more damage if any was consumed, and the arrows Chain 1 time per charge consumed.
- Quality: up to +4 projectiles; up to 30% chance for charge-consumption benefits to be doubled.
- Recommended supports (PoE2DB): 1 Brutality I, Perpetual Charge, Hourglass; 2 Chain II, Brutality II, Ricochet I; 3 Alignment I, Gambleshot, Stoicism I; 4 Alignment II, Hit and Run, Impale; 5 Brutality III, Heft.

| Lv | Req char lv / Dex | Mana | Attack dmg % |
|---|---|---|---|
| 1 | 0 / 4 | 6 | 66 |
| 5 | 14 / 28 | 11 | 94 |
| 7 | 22 / 41 | 15 | 108 |
| 10 | 36 / 65 | 22 | 126 |
| 12 | 46 / 82 | 27 | 139 |
| 14 | 58 / 103 | 34 | 154 |
| 16 | 66 / 116 | 42 | 169 |
| 18 | 78 / 137 | 52 | 187 |
| 20 | 90 / 157 | 64 | 206 |
| 21 | - | 71 | 216 |

- notes: damage column shown as three identical values; first read. Version history: 0.4.0 raised damage at levels 13-20 to 146-206% (from 133-187%); 0.2.0 raised per-charge bonus to 30% (from 20%) and made the first arrow fire straight ahead.


## Rapid Shot (crossbow)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 5. Tags: Attack, Ammunition, Projectile, Fire. Requires Str and Dex (4-86 each). Reload action: loads 100 bolts per clip (hidden stat shows action queue time 1000 ms). Fire stat set: attack speed 550% of base, 0 mana per shot, attack damage (26-94)% of base, projectile speed 32.5 m/s, converts 60% physical to fire. Load/reload mana cost (27-186).
- Mechanic (paraphrased): heat builds on the crossbow as you fire; at max heat (26-45 by level) you cannot fire or reload for 10 s. Other skills can consume Heat for bonuses. Using the skill again reloads the clip.
- Quality: up to +15 Maximum Heat and a second line of up to +30 Maximum Heat (both shown as separate stats on page).
- Recommended supports: 1 Fire Attunement, Rapid Attacks I, Multishot I; 2 Multishot II, Elemental Armament II, Fresh Clip I; 3 Immolate, Mobility, Gambleshot; 4 Eternal Flame III, Nimble Reload, Fresh Clip II; 5 Pierce III, Stoicism II.

| Lv | Req char lv | Str / Dex | Mana | Attack dmg % | Max Heat |
|---|---|---|---|---|---|
| 1 | 0 | 4 / 4 | 27 | 26 | 26 |
| 5 | 14 | 17 / 17 | 46 | 37 | 30 |
| 7 | 22 | 24 / 24 | 58 | 43 | 32 |
| 10 | 36 | 37 / 37 | 79 | 51 | 35 |
| 12 | 46 | 46 / 46 | 95 | 58 | 37 |
| 14 | 58 | 57 / 57 | 114 | 65 | 39 |
| 16 | 66 | 64 / 64 | 135 | 73 | 41 |
| 18 | 78 | 75 / 75 | 159 | 83 | 43 |
| 20 | 90 | 86 / 86 | 186 | 94 | 45 |
| 21 | - | - | 201 | 100 | 46 |

- notes: table damage cell is "100%, 100%, 100%, N%"; the 4th value matches the header (26-94), so I used it. Max Heat cell is "N, 1"; first value matches header 26-45.


## Explosive Shot (crossbow)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 7. Tags: Attack, AoE, Ammunition, Projectile, Fire, Detonator. Str and Dex (4-86 each). Reload: 30% less reload speed, +1 bolt per clip. Fire stat set: attack speed 70% of base, 0 mana per shot, projectile speed 23.4 m/s, 30% physical to fire. Load mana cost (9-64).
- Mechanic (paraphrased): flaming bolt explodes on impact; the explosion also detonates Grenades in its area. Explosion: attack damage (130-405)% of base, 80% physical to fire, radius (2.4-3) m, knockback stat present.
- Quality: up to +2 bolts loaded per clip; up to 30% more Ignite magnitude for the explosion.
- Recommended supports: 1 Ignite I, Elemental Armament I, Double Barrel I; 2 Multishot II, Fiery Death, Double Barrel II; 3 Ignite II, Longshot II, Deliberation; 4 Fire Exposure, Nimble Reload, Nova Projectiles II; 5 Fire Penetration II, Ignite III, Ammo Conservation III.

| Lv | Req char lv | Str / Dex | Mana | Explosion dmg % | Radius (m) |
|---|---|---|---|---|---|
| 1 | 0 | 4 / 4 | 9 | 130 | 2.4 |
| 5 | 14 | 17 / 17 | 16 | 185 | 2.5 |
| 7 | 22 | 24 / 24 | 20 | 213 | 2.6 |
| 10 | 36 | 37 / 37 | 27 | 249 | 2.7 |
| 12 | 46 | 46 / 46 | 33 | 274 | 2.7 |
| 14 | 58 | 57 / 57 | 39 | 303 | 2.8 |
| 16 | 66 | 64 / 64 | 46 | 334 | 2.9 |
| 18 | 78 | 75 / 75 | 54 | 368 | 2.9 |
| 20 | 90 | 86 / 86 | 64 | 405 | 3 |
| 21 | - | - | 69 | 426 | 3 |

- notes: the table's 4th damage value (130-405) matches the header's attack damage range; the first three are 100% at every level (meaning not stated). The page header's "Attack Damage (130-405)%" is the explosion stat set's. Version history: only a 0.4.0 armour-break fix.


## Barrage
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Tier 5. Tags: Spell, Buff, Duration. Cast time 0.70 s, cooldown 2.00 s. Requires Dex (4-157). Mana (11-51). Weapon: bow or spear.
- Mechanic (paraphrased): empowers your next Repeatable bow or projectile-spear attack: it repeats 2 extra times, plus 1 more per Frenzy Charge consumed (the skill consumes them). Repeats deal 50% less damage. Cooldown gets extra time equal to (410-600)% of the empowered skill's attack time, capped at 30 s. Buff lasts at most 5 s.
- Quality: repeats deal up to +5% more damage; up to 20% chance not to remove charges on use.
- Recommended supports: 1 Perpetual Charge; 2 Lifetap, Heightened Charges; 3 Prolonged Duration II, Cooldown Recovery I; 4 Efficiency II, Cooldown Recovery II; 5 Second Wind III.

| Lv | Req char lv / Dex | Mana | Cooldown added (% of attack time) |
|---|---|---|---|
| 1 | 0 / 4 | 11 | 600 |
| 5 | 14 / 28 | 18 | 560 |
| 7 | 22 / 41 | 21 | 540 |
| 10 | 36 / 65 | 27 | 510 |
| 12 | 46 / 82 | 31 | 490 |
| 14 | 58 / 103 | 36 | 470 |
| 16 | 66 / 116 | 41 | 450 |
| 18 | 78 / 137 | 46 | 430 |
| 20 | 90 / 157 | 51 | 410 |
| 21 | - | 54 | 400 |

- notes: the cap (30 s) is the second value in the table cell at every level. Damage cell is 100% x3 at every level (the 50% less repeat damage is a fixed stat). Version history: 0.2.0 set repeat damage to 50% less and reduced the cooldown scaling; 0.1.0e raised base repeats to +2. Only skills tagged Repeatable/"Barrageable" are affected.
