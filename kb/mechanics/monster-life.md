# Monster life, rarity multipliers & resistances

Version: 0.5.x (PoE2DB crawl 2026-11-23). Re-check at 1.0 (Acts 5–6, atlas rework).
Method: every PoE2DB monster page shows a Life % multiplier and "Level N · Life X" at its area level. Base life at level N = X ÷ (Life%/100). I computed this for every monster page in the corpus ([[tools/poe2db-corpus]]); values agree across all monsters at the same level (spread ≤1 except at 65/68, see notes).

## Base monster life by level (Life multiplier 100%, Normal rarity)
- Claim:
  | Lvl | Life | Lvl | Life | Lvl | Life |
  |---|---|---|---|---|---|
  | 5 | 33 | 31 | 637 | 53 | 3,102 |
  | 10 | 67 | 33 | 731 | 54 | 3,307 |
  | 15 | 134 | 36 | 921 | 55 | 3,525 |
  | 16 | 158 | 40 | 1,253 | 56 | 3,756 |
  | 20 | 249 | 45 | 1,841 | 65 | 6,555 |
  | 22 | 305 | 46 | 1,967 | 68 | 8,257 |
  | 30 | 593 | 47 | 2,101 | 74 | 14,887 |
  | | | 52 | 2,909 | 79 | 24,852 |
  | | | | | 80 | 31,065 |
- Version: 0.5.x · Volatility: may-change
- Source: derived from PoE2DB monster pages (e.g. [Count Geonor](https://poe2db.tw/us/Count_Geonor), [Zarokh, the Temporal](https://poe2db.tw/us/Zarokh,_the_Temporal), [The Arbiter of Divinity](https://poe2db.tw/us/The_Arbiter_of_Divinity)), tier 2, crawl 2026-11-23; 500+ pages used
- Confidence: single-source, internally consistent ([INFERRED] derivation — my arithmetic)
- Notes: the page says the values exclude map affixes, monster buffs, altars and atlas bonuses. Levels 75–78 and 57–64 have no monster pages in the crawl; [INFERRED] ~+11% per level from 74→79 (14,887 → 24,852) gives ~16,500 at 75. Level 65 had a low outlier (5,462) and 68 a high one (16,514) — one-off monster variants, ignored.

## Rarity life multipliers
- Claim: Magic monsters +148% life (×2.48), Rare +700% (×8), Unique +2,800% (×29), all "final" (multiplicative). Extra players add +10% (Magic), +30% (Rare), +85% (Unique) life each. Unique monsters also deal 35% less damage from rarity.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster) — "Monster Magic/Rare/Unique Stats" tables (monster_life_+%_final_from_rarity), tier 2, crawl 2026-11-23
- Confidence: single-source (game data)
- Notes: [INFERRED] the "Level N Life X" on boss pages excludes the rarity multiplier, so a Unique boss's real life ≈ page value × 29. Reason: Count Geonor's page value (318) would otherwise die to a few level-5 spells; check against a boss's health bar in game.

## Worked boss life ([INFERRED]: page life × 29 for Unique)
| Boss | Area (level) | Life % | Page life | ×29 Unique |
|---|---|---|---|---|
| Count Geonor | Ogham Manor (15) | 237% | 318 | ~9,200 |
| Jamanra, the Risen King | Halani Gates (20) | 333% | 829 | ~24,000 |
| Jamanra, the Abomination | Dreadnought (31) | 600% | 3,822 | ~111,000 |
| Doryani, Royal Thaumaturge | Black Chambers (45) | 330% | 6,075 | ~176,000 |
| Tavakai, the Chieftain | Heart of the Tribe (53) | 338% | 10,485 | ~304,000 |
| Zarokh, the Temporal | Sekhemas (22 page; scales with Barya level) | 750% | 2,288 at 22 | at 75: ~16,500 × 7.5 × 29 ≈ 3.6 M |
| The Arbiter of Ash | Burning Monolith (74) | 990% | 147,381 | ~4.3 M |
| The Arbiter of Divinity | Origin Tower (79) | 990% | 246,035 | ~7.1 M |
- Source: PoE2DB pages above, tier 2, crawl 2026-11-23; ×29 column [INFERRED]
- Notes: Zarokh's level follows the Djinn Barya's area level ([[classes/ascendancy-trials]]) [INFERRED]. The Desperate Alliance relic makes Zarokh take 75% less damage (= ×4 effective life) and deal 100% more ([[endgame/sekhemas]]).

## Monster resistances
- Claim: PoE2DB lists monster resistances in the order Fire / Cold / Lightning / Chaos (confirmed by Moltenmettle, a fire monster: 90 / −15 / 0 / 0). Monster default max resistance 75%.
- Examples: Count Geonor **45% cold**; Jamanra, the Abomination 45% fire / −15% cold / 45% lightning; Tavakai 45% fire; Zarokh 15% all elements on PooE2DB stats (PoB spectre data shows 0% — conflict).
- Version: 0.5.x · Volatility: may-change
- Source: PoE2DB monster pages + [PoE2DB Monster](https://poe2db.tw/us/Monster) "Monster Default" (base_maximum_all_resistances_% 75), tier 2, crawl 2026-11-23
- Confidence: single-source; column order [INFERRED] from one fire monster (strong); Zarokh value → kb/04-conflicts.md
- Notes: map/rarity mods add more resistance → [[mechanics/resistances]].

## Monster crit damage (resolves an open conflict)
- Claim: Monster default critical damage bonus = 30%.
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster) "Monster Default" (base_critical_hit_damage_bonus 30); boss pages show "Critical Damage Bonus +30%", tier 2, crawl 2026-11-23
- Confidence: single-source game data; agrees with Mobalytics (30%) vs poe2wiki (40% less) → kb/04-conflicts.md "Monster critical damage bonus" resolved by game data.

## Monster Power / Effectiveness
- Power: average monster 1; strong 2–3; × rarity (Normal 1, Magic 2, Rare 5); Uniques always 20 ([PoE2DB Monster Power](https://poe2db.tw/us/Monster_Power)). Used by flask/charm charges ([[mechanics/charms]]).
- Effectiveness: per 2% increased, monsters gain 2% more toughness, 1% more XP, 1% more item quantity ([PoE2DB Monster Effectiveness](https://poe2db.tw/us/Monster_Effectiveness)). Corrupted/juiced maps raise effectiveness → [[strategy/atlas-starter-strategy]].
