# Minion base stats: multipliers and rules
Status: partial. Per-minion Life/Damage/attack-time multipliers done for 17 minions. Not found: Unearth Bone Construct, Spiraling Conspiracy flock, Spectre (depends on bound monster), Ravenous Swarm/Raging Spirit exact in-game life use. Per-level values are in [[gems/minion-stats-2]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked for 1.0.
Sources: PoE2DB gem pages (each embeds the summoned minion's monster block) and PoE2DB Monster / Minions pages, tier 2.

## Gem level to minion level
- Claim: minion level = 2 x gem level (gem 1 = L2, gem 10 = L20, gem 20 = L40, gem 40 = L80). Applies to every minion gem checked.
- Version: 0.5.x | Volatility: may-change
- Source: [PoE2DB Minions](https://poe2db.tw/us/Minions) table "Minion Gem Level /40" (Minion.txt lines 11, 20, 30), tier 2, crawl 2026-11-23. Same column on [Skeletal Warrior](https://poe2db.tw/us/Skeletal_Warrior) level table.
- Confidence: confirmed (PoE2DB Minions page and each gem page's "Minion Level" column agree)
- Notes: +levels to minion skills raise this ([[mechanics/minions]]).

## How minion life/damage is built (PoE2DB display)
- Claim: each minion monster has a Life % and Damage % multiplier. PoE2DB's block shows "Minion Life" = (Monster Stats table "Minion Life" for that level) x Life %, and "Minion Damage" = ("Minion Damage" column) x Damage %. Checked at L68 on Animated Weapon (100%: 6,930 / 969), Raging Spirit (25%/70%: 1,733 / 678), Skeletal Warrior (88%/70%: 6,098 / 678). The block also shows plain "Life" = Monster-table "Life" column x Life % (L68 100% = 8,257).
- Version: 0.5.x | Volatility: may-change
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster) "Monster Stats" row 68 (Monster.txt line 649, row `68 | 233.12 | 708 | 1251 | 8257 | 3451 | 28634 | 6930 | 968.76`); Skeletal_Warrior.txt lines 2440-2510; Raging_Spirits.txt 2677-2745; Animated_Weapon.txt. Tier 2, crawl 2026-11-23.
- Confidence: confirmed (arithmetic matches on 3 pages)
- Notes: PoE2DB does not say which of "Life" vs "Minion Life" the game applies to player minions. Not settled here; see Conflicts in report. [INFERRED] the "Minion Life" column is the one for player minions because the label says so and it is shown on minion-only blocks.

## Basic-attack hit
- Claim: a minion's basic attack range = Monster-table "Damage" column x Damage %, spread by the damage-spread % (Skeletal Warrior L68: 163, range 114-212 at +-30%; Raging Spirit 163, 131-196 at +-20%).
- Version: 0.5.x | Volatility: may-change
- Source: Skeletal_Warrior.txt "Basic Attack Base Damage: 114 — 212" (~line 2515); Raging_Spirits.txt "131 — 196". Tier 2, crawl 2026-11-23.
- Confidence: confirmed (2 pages, arithmetic matches)
- Notes: skill damage % (e.g. Brute strike 180% of base, Arsonist Explosive Demise 300%) multiplies on top, per gem pages.

## Skeleton minions (multipliers)
- Claim: Life % / Damage % / attack time (s) / extras. All show 0% resist in the PoB data block; see element note below.
| Minion | Life | Dmg | Atk s | Extras |
|---|---|---|---|---|
| Skeletal Warrior | 88% | 70% | 1 | +50% armour, 30% block |
| Skeletal Brute | 120% | 200% | 1.75 | +70% armour, model 120% |
| Skeletal Reaver | 70% | 46% | 0.83 | +20% armour |
| Skeletal Frost Mage | 53% | 60% | 1 | ES 15% of life |
| Skeletal Arsonist | 55% | 70% | 1 | ES 10% of life |
| Skeletal Sniper | 55% | 115% | 1.5 | none |
| Skeletal Cleric | 53% | 65% | 1 | ES 15% of life |
| Skeletal Storm Mage | 53% | 65% | 1 | ES 15% of life |
- Version: 0.5.x | Volatility: may-change
- Source: monster blocks at the bottom of PoE2DB gem pages: [Skeletal Warrior](https://poe2db.tw/us/Skeletal_Warrior) Life line 2440; [Brute](https://poe2db.tw/us/Skeletal_Brute) 2643; [Reaver](https://poe2db.tw/us/Skeletal_Reaver) 2518; [Frost Mage](https://poe2db.tw/us/Skeletal_Frost_Mage) 2210; [Arsonist](https://poe2db.tw/us/Skeletal_Arsonist) 2416; [Sniper](https://poe2db.tw/us/Skeletal_Sniper) 2308; [Cleric](https://poe2db.tw/us/Skeletal_Cleric) 505; [Storm Mage](https://poe2db.tw/us/Skeletal_Storm_Mage) 1941. Tier 2, crawl 2026-11-23.
- Confidence: confirmed for Life/Damage (monster block and the PoB-format block on the same page agree, e.g. Frost Mage life 0.53, damage 0.6)
- Notes: Warrior is granted by some sceptres and cannot be engraved since 0.2.0 (Skeletal_Warrior.txt line 155); Sniper is the replacement gem. Spirit reservation at gem 1/10/20: Warrior 60/22/20 (table "Mana" column = spirit, header reads Reservation 60-20), Brute 165/54/48, Reaver 90/33/30, Frost Mage 120/43/39, Arsonist 90/42/39, Sniper 90/33/30, Cleric 60/22/20, Storm Mage 120/42/39 (level-table rows). First 2 Warriors have no reservation.

## Other minions (multipliers)
| Minion (gem) | Life | Dmg | Atk s | Extras |
|---|---|---|---|---|
| Raised Zombie (Raise Zombie) | 70% | 75% | 1.25 | duration 20 s, limit 10 |
| Raging Spirit | 25% | 70% | 1 | +40% attack speed |
| Ravenous Swarm | 70% | 84% | 1 | untargetable swarms, max 3 |
| Rhoa Companion (Rhoa Mount) | 200% | 200% | 1.23 | +50% armour, +50% evasion |
| Wolf Companion (Wolf Pack) | 110% | 70% | 0.8 | +30% evasion |
| Azmerian Wolf | 270% | 243% | 1 | +30% evasion; attack skill 250%, dash 700%, 7.5 s cd |
| Mist Raven | 150% | 150% | 1 | +100% evasion |
| Infernal Hound (ascendancy) | 88% | 125% | 0.75 | +50% armour, +50% evasion |
| Demon Magus (meta) | 150% | 100% | 1 | ES 50% of life, accuracy 340%, range 80 |
- Version: 0.5.x | Volatility: may-change
- Source: [Raise Zombie](https://poe2db.tw/us/Raise_Zombie) Life line 2490; [Raging Spirits](https://poe2db.tw/us/Raging_Spirits) 2677; [Ravenous Swarm](https://poe2db.tw/us/Ravenous_Swarm) 2579; [Rhoa Companion](https://poe2db.tw/us/Rhoa_Companion) 17; [Wolf Companion](https://poe2db.tw/us/Wolf_Companion) 13; [Azmerian Wolf](https://poe2db.tw/us/Azmerian_Wolf) 2826; [Mist Raven](https://poe2db.tw/us/Mist_Raven) 2646; [Summon Infernal Hound](https://poe2db.tw/us/Summon_Infernal_Hound) 2441; [Demon Magus](https://poe2db.tw/us/Demon_Magus) 416. Tier 2, crawl 2026-11-23.
- Confidence: single-source per minion (PoE2DB block + PoB-format block agree)
- Notes: [INFERRED] Wolf Pack wolves = Wolf Companion and Rhoa Mount's mount = Rhoa Companion: gem pages Wolf_Pack.txt / Rhoa_Mount.txt do not name the monster; matched by name only. Zombie "Empowered" zombies: 30% less damage taken, +100-253% more hit damage (gem 1-20), +25% move speed (Raise_Zombie.txt level table). Demon Magus is a meta gem, 100 spirit.

## Resistances
- Claim: the minion blocks show Resistance 0% on all four elements for almost every minion. Exceptions shown as 50%: Arsonist fire, Frost Mage cold, Storm Mage lightning, Infernal Hound fire (display order fire/cold/lightning/chaos matches the element of each mage). PoB-format data in the same pages says 0 for these, so the display and the data block disagree.
- Version: 0.5.x | Volatility: may-change
- Source: Skeletal_Frost_Mage.txt ~2212-2218 (cold 50%) vs ~2371 (coldResist = 0); Skeletal_Arsonist.txt; Skeletal_Storm_Mage.txt; Summon_Infernal_Hound.txt. Tier 2, crawl 2026-11-23.
- Confidence: [INFERRED]: order fire/cold/lightning/chaos taken from the PoB block's key order and the element of each mage; PoE2DB does not label the four cells.
- Notes: unresolved, in report Conflicts. Player-side minion resistance mods: see [[mechanics/minions]].
