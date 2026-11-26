# Minion stats by minion level (derived)
Status: partial. Derived from [[gems/minion-stats]] multipliers x PoE2DB Monster Stats table. Excludes Bone Constructs, Spectres, Spiraling Conspiracy (no data found).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked for 1.0.
Sources: PoE2DB Monster page "Monster Stats" table, tier 2; minion multipliers from gem pages.

## Monster Stats table rows (minion levels 2 / 20 / 40 / 80)
- Claim: PoE2DB's Monster Stats table lists per monster level: Damage, Evasion, Accuracy, Life, Armour, Experience, Minion Life, Minion Damage.
| Lvl | Damage | Life | Armour | Minion Life | Minion Damage |
|---|---|---|---|---|---|
| 2 (gem 1) | 10.26 | 20 | 8 | 83 | 4.42 |
| 20 (gem 10) | 37.29 | 249 | 127 | 886 | 50.39 |
| 40 (gem 20) | 90.02 | 1253 | 599 | 2490 | 204.04 |
| 80 (gem 40) | 333.78 | 31065 | 6867 | 10084 | 1776.43 |
- Version: 0.5.x | Volatility: may-change
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster), Monster.txt lines 583 (L2), 601 (L20), 621 (L40), 661 (L80), tier 2, crawl 2026-11-23.
- Confidence: single-source
- Notes: Minion Life is higher than Monster Life up to level 63 and lower from level 64 (6077 vs 6203) (L66: 6492 vs 7079; L40: 2490 vs 1253). Level 100 row: Minion Life 17980 (line 681).

## Derived minion life (Minion Life column x Life %)
- Claim: [INFERRED] life = column value x Life %, rounded. Basis: PoE2DB's own L68 blocks follow this exactly (see [[gems/minion-stats]]); no source states the in-game formula or whether quality/support/passive "more/increased Life" is applied after.
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
- Version: 0.5.x | Volatility: may-change
- Source: arithmetic on Monster.txt lines 583/601/621 (Minion Life 83 / 886 / 2490) and Life % from [[gems/minion-stats]].
- Confidence: [INFERRED]: applying the L68-verified multiplication to other levels; e.g. Warrior L2 = 83 x 0.88 = 73.04.
- Notes: Mages' ES = 15% of this (Arsonist 10%, Demon Magus 50%): Frost Mage L68 ES 551 = 3673 x 0.15 (Skeletal_Frost_Mage.txt ~2283). Using the plain "Life" column instead gives much lower low-level values (Warrior L2 = 20 x 0.88 = 18; L20 219; L40 1103).

## Derived minion damage (Minion Damage column x Damage %)
- Claim: [INFERRED] "Minion Damage" = column x Damage %. Same method as life.
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
- Version: 0.5.x | Volatility: may-change
- Source: arithmetic on Monster.txt Minion Damage 4.42 / 50.39 / 204.04.
- Confidence: [INFERRED]: PoE2DB shows both "Minion Damage" and "Damage" per block; which one a basic attack uses is unclear. The listed basic-attack range matches the plain Damage column: Warrior L68 163 = 233.12 x 0.7, range 114-212.
- Notes: Basic-attack midpoint via Damage column x Damage % (L2/L20/L40): Warrior 7.2 / 26.1 / 63.0; Brute 20.5 / 74.6 / 180.0 (basic attack only; Initial Strike is 180% of base per gem page); Sniper 11.8 / 42.9 / 103.5; Zombie 7.7 / 28.0 / 67.5.

## Armour at L68 (observed)
- Claim: Minion Armour at L68: base 2,413 for 0% bonus minions ([INFERRED]: back-derived from the per-minion values, not a column on the page); Warrior (+50%) 6,033; Reaver (+20%) 3,861; Brute (+70%) 7,480; Rhoa (+50%) 6,033. Fits base x (1 + 3 x bonus) — [INFERRED] pattern, not stated by PoE2DB. Plain "Armour" column shows base x (1 + bonus), e.g. Warrior 3,620.
- Version: 0.5.x | Volatility: may-change
- Source: Skeletal_Warrior.txt ~2507-2512; Skeletal_Reaver.txt ~2585; Skeletal_Brute.txt ~2710; Rhoa_Companion.txt ~86. Tier 2, crawl 2026-11-23.
- Confidence: [INFERRED]: the 3x relation fitted by me on 4 data points; not stated by PoE2DB.
- Notes: no armour column value at L2/20/40 derived (Minion Armour column not in the Monster Stats table).
