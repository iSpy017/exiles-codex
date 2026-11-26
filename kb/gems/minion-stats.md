---
title: Minion base stats: multipliers and rules
status: partial
tracker_topic: "Minion base stats — multipliers + derived life/damage by level"
tracker_note: "partial (17 minions; L2/20/40 values [INFERRED]; 2 conflicts)"
defaults: v=0.5.x
merged_from: [minion-stats.md, minion-stats-2.md]
---
Status: partial. Per-minion Life/Damage/attack-time multipliers done for 17 minions. Not found: Unearth Bone Construct, Spiraling Conspiracy flock, Spectre (depends on bound monster), Ravenous Swarm/Raging Spirit exact in-game life use. Per-level values are in [[gems/minion-stats]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked for 1.0.
Sources: PoE2DB gem pages (each embeds the summoned minion's monster block) and PoE2DB Monster / Minions pages, tier 2.

## Gem level to minion level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
minion level = 2 x gem level (gem 1 = L2, gem 10 = L20, gem 20 = L40, gem 40 = L80). Applies to every minion gem checked.
- src: poe2db:Minions table "Minion Gem Level /40" (Minion.txt lines 11, 20, 30), tier 2, crawl 2026-11-23. Same column on poe2db:Skeletal_Warrior level table.
- conf: confirmed (PoE2DB Minions page and each gem page's "Minion Level" column agree)
- notes: +levels to minion skills raise this ([[mechanics/minions]]).


## How minion life/damage is built (PoE2DB display)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
each minion monster has a Life % and Damage % multiplier. PoE2DB's block shows "Minion Life" = (Monster Stats table "Minion Life" for that level) x Life %, and "Minion Damage" = ("Minion Damage" column) x Damage %. Checked at L68 on Animated Weapon (100%: 6,930 / 969), Raging Spirit (25%/70%: 1,733 / 678), Skeletal Warrior (88%/70%: 6,098 / 678). The block also shows plain "Life" = Monster-table "Life" column x Life % (L68 100% = 8,257).
- src: poe2db:Monster "Monster Stats" row 68 (Monster.txt line 649, row `68 | 233.12 | 708 | 1251 | 8257 | 3451 | 28634 | 6930 | 968.76`); Skeletal_Warrior.txt lines 2440-2510; Raging_Spirits.txt 2677-2745; Animated_Weapon.txt. Tier 2, crawl 2026-11-23.
- conf: confirmed (arithmetic matches on 3 pages)
- notes: PoE2DB does not say which of "Life" vs "Minion Life" the game applies to player minions. Not settled here; see Conflicts in report. [INFERRED] the "Minion Life" column is the one for player minions because the label says so and it is shown on minion-only blocks.


## Basic-attack hit
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
a minion's basic attack range = Monster-table "Damage" column x Damage %, spread by the damage-spread % (Skeletal Warrior L68: 163, range 114-212 at +-30%; Raging Spirit 163, 131-196 at +-20%).
- src: Skeletal_Warrior.txt "Basic Attack Base Damage: 114 — 212" (~line 2515); Raging_Spirits.txt "131 — 196". Tier 2, crawl 2026-11-23.
- conf: confirmed (2 pages, arithmetic matches)
- notes: skill damage % (e.g. Brute strike 180% of base, Arsonist Explosive Demise 300%) multiplies on top, per gem pages.


## Skeleton minions (multipliers)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Life % / Damage % / attack time (s) / extras. All show 0% resist in the PoB data block; see element note below.
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
- src: monster blocks at the bottom of PoE2DB gem pages: poe2db:Skeletal_Warrior Life line 2440; poe2db:Skeletal_Brute «Brute» 2643; poe2db:Skeletal_Reaver «Reaver» 2518; poe2db:Skeletal_Frost_Mage «Frost Mage» 2210; poe2db:Skeletal_Arsonist «Arsonist» 2416; poe2db:Skeletal_Sniper «Sniper» 2308; poe2db:Skeletal_Cleric «Cleric» 505; poe2db:Skeletal_Storm_Mage «Storm Mage» 1941. Tier 2, crawl 2026-11-23.
- conf: confirmed for Life/Damage (monster block and the PoB-format block on the same page agree, e.g. Frost Mage life 0.53, damage 0.6)
- notes: Warrior is granted by some sceptres and cannot be engraved since 0.2.0 (Skeletal_Warrior.txt line 155); Sniper is the replacement gem. Spirit reservation at gem 1/10/20: Warrior 60/22/20 (table "Mana" column = spirit, header reads Reservation 60-20), Brute 165/54/48, Reaver 90/33/30, Frost Mage 120/43/39, Arsonist 90/42/39, Sniper 90/33/30, Cleric 60/22/20, Storm Mage 120/42/39 (level-table rows). First 2 Warriors have no reservation.


## Other minions (multipliers)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
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
- src: poe2db:Raise_Zombie Life line 2490; poe2db:Raging_Spirits 2677; poe2db:Ravenous_Swarm 2579; poe2db:Rhoa_Companion 17; poe2db:Wolf_Companion 13; poe2db:Azmerian_Wolf 2826; poe2db:Mist_Raven 2646; poe2db:Summon_Infernal_Hound 2441; poe2db:Demon_Magus 416. Tier 2, crawl 2026-11-23.
- conf: single-source per minion (PoE2DB block + PoB-format block agree)
- notes: [INFERRED] Wolf Pack wolves = Wolf Companion and Rhoa Mount's mount = Rhoa Companion: gem pages Wolf_Pack.txt / Rhoa_Mount.txt do not name the monster; matched by name only. Zombie "Empowered" zombies: 30% less damage taken, +100-253% more hit damage (gem 1-20), +25% move speed (Raise_Zombie.txt level table). Demon Magus is a meta gem, 100 spirit.


## Resistances
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
the minion blocks show Resistance 0% on all four elements for almost every minion. Exceptions shown as 50%: Arsonist fire, Frost Mage cold, Storm Mage lightning, Infernal Hound fire (display order fire/cold/lightning/chaos matches the element of each mage). PoB-format data in the same pages says 0 for these, so the display and the data block disagree.
- src: Skeletal_Frost_Mage.txt ~2212-2218 (cold 50%) vs ~2371 (coldResist = 0); Skeletal_Arsonist.txt; Skeletal_Storm_Mage.txt; Summon_Infernal_Hound.txt. Tier 2, crawl 2026-11-23.
- conf: [INFERRED]: order fire/cold/lightning/chaos taken from the PoB block's key order and the element of each mage; PoE2DB does not label the four cells.
- notes: unresolved, in report Conflicts. Player-side minion resistance mods: see [[mechanics/minions]].


<!-- merged from kb/gems/minion-stats-2.md -->
Part title: Minion stats by minion level (derived)
Status: partial. Derived from [[gems/minion-stats]] multipliers x PoE2DB Monster Stats table. Excludes Bone Constructs, Spectres, Spiraling Conspiracy (no data found).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked for 1.0.
Sources: PoE2DB Monster page "Monster Stats" table, tier 2; minion multipliers from gem pages.

## Monster Stats table rows (minion levels 2 / 20 / 40 / 80)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
PoE2DB's Monster Stats table lists per monster level: Damage, Evasion, Accuracy, Life, Armour, Experience, Minion Life, Minion Damage.
| Lvl | Damage | Life | Armour | Minion Life | Minion Damage |
|---|---|---|---|---|---|
| 2 (gem 1) | 10.26 | 20 | 8 | 83 | 4.42 |
| 20 (gem 10) | 37.29 | 249 | 127 | 886 | 50.39 |
| 40 (gem 20) | 90.02 | 1253 | 599 | 2490 | 204.04 |
| 80 (gem 40) | 333.78 | 31065 | 6867 | 10084 | 1776.43 |
- src: poe2db:Monster, Monster.txt lines 583 (L2), 601 (L20), 621 (L40), 661 (L80), tier 2, crawl 2026-11-23.
- notes: Minion Life is higher than Monster Life up to level 63 and lower from level 64 (6077 vs 6203) (L66: 6492 vs 7079; L40: 2490 vs 1253). Level 100 row: Minion Life 17980 (line 681).


## Derived minion life (Minion Life column x Life %)
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
[INFERRED] life = column value x Life %, rounded. Basis: PoE2DB's own L68 blocks follow this exactly (see [[gems/minion-stats]]); no source states the in-game formula or whether quality/support/passive "more/increased Life" is applied after.
| Minion | L2 | L20 | L40 |
|---|---|---|---|
| Skeletal Warrior | 73 | 780 | 2191 |
| Skeletal Brute | 100 | 1063 | 2988 |
| Skeletal Reaver | 58 | 620 | 1743 |
| Skeletal Frost Mage / Storm Mage / Cleric | 44 | 470 | 1320 |
| Skeletal Arsonist / Sniper | 46 | 487 | 1370 |
| Raised Zombie / Ravenous Swarm | 58 | 620 | 1743 |
| Raging Spirit | 21 | 222 | 622.5 (≈623) |
| Rhoa Companion | 166 | 1772 | 4980 |
| Wolf Companion | 91 | 975 | 2739 |
| Azmerian Wolf | 224 | 2392 | 6723 |
| Mist Raven / Demon Magus | 124 | 1329 | 3735 |
| Infernal Hound | 73 | 780 | 2191 |
- src: arithmetic on Monster.txt lines 583/601/621 (Minion Life 83 / 886 / 2490) and Life % from [[gems/minion-stats]].
- conf: [INFERRED]: applying the L68-verified multiplication to other levels; e.g. Warrior L2 = 83 x 0.88 = 73.04.
- notes: Mages' ES = 15% of this (Arsonist 10%, Demon Magus 50%): Frost Mage L68 ES 551 = 3673 x 0.15 (Skeletal_Frost_Mage.txt ~2283). Using the plain "Life" column instead gives much lower low-level values (Warrior L2 = 20 x 0.88 = 18; L20 219; L40 1103).


## Derived minion damage (Minion Damage column x Damage %)
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
[INFERRED] "Minion Damage" = column x Damage %. Same method as life.
| Minion | L2 | L20 | L40 |
|---|---|---|---|
| Skeletal Warrior / Arsonist / Raging Spirit / Wolf Companion | 3.1 | 35.3 | 142.8 |
| Skeletal Brute / Rhoa Companion | 8.8 | 100.8 | 408.1 |
| Skeletal Reaver | 2.0 | 23.2 | 93.9 |
| Skeletal Frost Mage | 2.7 | 30.2 | 122.4 |
| Skeletal Cleric / Storm Mage | 2.9 | 32.8 | 132.6 |
| Skeletal Sniper | 5.1 | 57.9 | 234.6 |
| Raised Zombie | 3.3 | 37.8 | 153.0 |
| Ravenous Swarm | 3.7 | 42.3 | 171.4 |
| Azmerian Wolf | 10.7 | 122.4 | 495.8 |
| Mist Raven | 6.6 | 75.6 | 306.1 |
| Infernal Hound | 5.5 | 63.0 | 255.0 |
| Demon Magus | 4.4 | 50.4 | 204.0 |
- src: arithmetic on Monster.txt Minion Damage 4.42 / 50.39 / 204.04.
- conf: [INFERRED]: PoE2DB shows both "Minion Damage" and "Damage" per block; which one a basic attack uses is unclear. The listed basic-attack range matches the plain Damage column: Warrior L68 163 = 233.12 x 0.7, range 114-212.
- notes: Basic-attack midpoint via Damage column x Damage % (L2/L20/L40): Warrior 7.2 / 26.1 / 63.0; Brute 20.5 / 74.6 / 180.0 (basic attack only; Initial Strike is 180% of base per gem page); Sniper 11.8 / 42.9 / 103.5; Zombie 7.7 / 28.0 / 67.5.


## Armour at L68 (observed)
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
Minion Armour at L68: base 2,413 for 0% bonus minions ([INFERRED]: back-derived from the per-minion values, not a column on the page); Warrior (+50%) 6,033; Reaver (+20%) 3,861; Brute (+70%) 7,480; Rhoa (+50%) 6,033. Fits base x (1 + 3 x bonus) — [INFERRED] pattern, not stated by PoE2DB. Plain "Armour" column shows base x (1 + bonus), e.g. Warrior 3,620.
- src: Skeletal_Warrior.txt ~2507-2512; Skeletal_Reaver.txt ~2585; Skeletal_Brute.txt ~2710; Rhoa_Companion.txt ~86. Tier 2, crawl 2026-11-23.
- conf: [INFERRED]: the 3x relation fitted by me on 4 data points; not stated by PoE2DB.
- notes: no armour column value at L2/20/40 derived (Minion Armour column not in the Monster Stats table).
