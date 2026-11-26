# Bow attack gems (1/2): Ice Shot, Lightning Arrow, Lightning Rod

Status: done for these three (levels 1-21 rows from PoE2DB). Companion: [[gems/bow-attack-gems-2]] (Escape Shot, Freezing Salvo, Gas Arrow, Herald of Thunder).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB gem pages [Ice Shot](https://poe2db.tw/us/Ice_Shot), [Lightning Arrow](https://poe2db.tw/us/Lightning_Arrow), [Lightning Rod](https://poe2db.tw/us/Lightning_Rod); tier 2.
Build context: [[builds/ice-shot-deadeye-levelling-0.5.5]], [[strategy/practice-build-0.5.5]]. Table columns: gem level | character level required | Dex required | mana cost | Attack Damage % of base. Level 21 has no requirement shown (only reachable via +gem-level effects, [INFERRED]: PoE2DB lists blank requirements for 21+).

## Ice Shot
- Claim: Tier 9 gem. Tags: Attack, Projectile, Cold, Repeatable. Attack speed 90% of base. Attack damage (95-344)% of base over gem levels 1-20. Mana (6-40). Projectile speed 32.6 m/s. Requires a bow. Arrow converts 80% of physical to cold; 50% more Chill magnitude; 25% more Freeze buildup (on the arrow).
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source (one PoE2DB page; header ranges match table)
- Notes: version history says 0.5.0 removed the shards' 25% more Freeze buildup; 0.4.0 raised conversion to 80%. Table's 4th value is 100% at every level (meaning not stated on page); see report Conflicts.

## Lightning Arrow
- Claim: Tier 1 gem. Tags: Attack, AoE, Projectile, Lightning, Chaining, Repeatable. Attack speed 90% of base. Attack damage (80-250)% of base at levels 1-20. Mana (6-40). Projectile speed 54 m/s. Requires a bow. Projectile converts 80% of physical to lightning; the chain beam converts 100%.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: table shows beams as "N, 1"; I read the first number as the beam count (matches the page's "(2-4)" header); the trailing 1 is unexplained. 0.5.0: multiple beams can no longer chain onto the same target. 0.5.4b fix: Lightning Arrow could not chain to rods created by Shockchain Arrow.

## Lightning Rod
- Claim: Tier 1 gem. Tags: Attack, AoE, Projectile, Sustained, Lightning, Duration, Repeatable. Attack speed 120% of base. Attack damage (26-94)% at levels 1-20. Mana (4-30). Projectile speed 32.6 m/s. Bow required. 100% physical converted to lightning.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: version history (0.2.0) says arrows vanish after 6 chains, but the current page says 8 (no entry for the change); see report Conflicts. 0.4.0 cut the active-rod limit from 20 to 10.
