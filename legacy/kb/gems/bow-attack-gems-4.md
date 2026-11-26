# Bow attack gems (4/4): Spiral Volley, Rapid Shot, Explosive Shot, Barrage

Status: done for these four (levels 1-21 rows from PoE2DB). Companions: [[gems/bow-attack-gems]], [[gems/bow-attack-gems-2]], [[gems/bow-attack-gems-3]] (Rain of Arrows, Snipe, Tornado Shot).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is checked against 1.0.
Sources: PoE2DB [Spiral Volley](https://poe2db.tw/us/Spiral_Volley), [Rapid Shot](https://poe2db.tw/us/Rapid_Shot), [Explosive Shot](https://poe2db.tw/us/Explosive_Shot), [Barrage](https://poe2db.tw/us/Barrage); tier 2.
Weapon: Spiral Volley needs a bow; Rapid Shot and Explosive Shot need a CROSSBOW (not bows; included because PoE2DB groups them with bow gems); Barrage needs bow or spear. Level 21 has no requirement shown ([INFERRED]: blank beyond level 20).

## Spiral Volley
- Claim: Tier 13. Tags: Attack, Projectile, Sustained. No attack-speed line shown. Attack damage (66-206)% of base. Mana (6-64). Projectile speed 32.6 m/s.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: damage column shown as three identical values; first read. Version history: 0.4.0 raised damage at levels 13-20 to 146-206% (from 133-187%); 0.2.0 raised per-charge bonus to 30% (from 20%) and made the first arrow fire straight ahead.

## Rapid Shot (crossbow)
- Claim: Tier 5. Tags: Attack, Ammunition, Projectile, Fire. Requires Str and Dex (4-86 each). Reload action: loads 100 bolts per clip (hidden stat shows action queue time 1000 ms). Fire stat set: attack speed 550% of base, 0 mana per shot, attack damage (26-94)% of base, projectile speed 32.5 m/s, converts 60% physical to fire. Load/reload mana cost (27-186).
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: table damage cell is "100%, 100%, 100%, N%"; the 4th value matches the header (26-94), so I used it. Max Heat cell is "N, 1"; first value matches header 26-45.

## Explosive Shot (crossbow)
- Claim: Tier 7. Tags: Attack, AoE, Ammunition, Projectile, Fire, Detonator. Str and Dex (4-86 each). Reload: 30% less reload speed, +1 bolt per clip. Fire stat set: attack speed 70% of base, 0 mana per shot, projectile speed 23.4 m/s, 30% physical to fire. Load mana cost (9-64).
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: the table's 4th damage value (130-405) matches the header's attack damage range; the first three are 100% at every level (meaning not stated). The page header's "Attack Damage (130-405)%" is the explosion stat set's. Version history: only a 0.4.0 armour-break fix.

## Barrage
- Claim: Tier 5. Tags: Spell, Buff, Duration. Cast time 0.70 s, cooldown 2.00 s. Requires Dex (4-157). Mana (11-51). Weapon: bow or spear.
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

- Version: 0.5.x | Volatility: may-change | Confidence: single-source
- Notes: the cap (30 s) is the second value in the table cell at every level. Damage cell is 100% x3 at every level (the 50% less repeat damage is a fixed stat). Version history: 0.2.0 set repeat damage to 50% less and reduced the cooldown scaling; 0.1.0e raised base repeats to +2. Only skills tagged Repeatable/"Barrageable" are affected.
