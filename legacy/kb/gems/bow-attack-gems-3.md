# Bow attack gems (3/4): Rain of Arrows, Snipe, Tornado Shot

Status: done for these three (levels 1-21 rows from PoE2DB). Companions: [[gems/bow-attack-gems]] (Ice Shot, Lightning Arrow, Lightning Rod), [[gems/bow-attack-gems-2]] (Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder), [[gems/bow-attack-gems-4]] (Spiral Volley, Rapid Shot, Explosive Shot, Barrage).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: [PoE2DB Rain of Arrows](https://poe2db.tw/us/Rain_of_Arrows), [Snipe](https://poe2db.tw/us/Snipe), [Tornado Shot](https://poe2db.tw/us/Tornado_Shot); tier 2.
Table columns: gem level | character level required / Dex required | mana | other columns as labelled. Level 21 has no requirement shown on PoE2DB ([INFERRED]: blank for levels beyond 20, reachable only via +gem-level effects). All three require a bow.

## Rain of Arrows
- Claim: Tier 9. Tags: Attack, AoE, Projectile, Sustained. Attack speed 80% of base. Attack damage (50-181)% of base at levels 1-20. Mana (15-103). Projectile speed 32.6 m/s.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source (header ranges 50-181, 30-39, 15-103 match table)
- Notes: table shows damage as "N%, N%, N%" (three identical values) and arrows as "N, 1, 1"; I read the first value of each, which matches the header ranges. The extra 1s are unexplained. Version history: 0.5.0 fixed extra-projectile chance stats not applying to skills like this.

## Snipe
- Claim: Tier 3. Tags: Attack, AoE, Projectile, Cold, Channelling, Payoff, Repeatable. Attack speed 45% of base. Mana cost is per second: (17.55-118.57)/s (table rounds to whole numbers). Projectile speed 32.6 m/s.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source (each column's level 1/20 values match the page's header ranges)
- Notes: table lists the arrow value three times, then Explosion, then Icy Blast; last column = "% more damage vs Unique-origin explosions". Version history: 0.5.0 lowered the damage numbers (arrow 133-343 to 121-312 at levels 3-20 per the log; explosion and Icy Blast changed too) and allowed Mirage Archer to use channelled skills; 0.4.0 removed the Heavy Stun interaction. Synergy with Freeze sources: [[gems/bow-attack-gems]] Ice Shot is a cold bow gem.

## Tornado Shot
- Claim: Tier 11. Tags: Attack, AoE, Projectile, Physical, Duration, Repeatable, Wind. Attack speed 120% of base. Attack damage (50-156)% of base. Mana (13-88). Projectile speed 21.73 m/s.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: table damage column is "N%, N%, N%, 100%"; I read the first value (matches header 50-156). The fourth value (constant 100%) is unexplained on the page. 0.4.0 only added the Wind tag.
