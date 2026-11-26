---
title: Monster life, rarity multipliers & resistances
status: done
tracker_topic: "Monster life, rarity multipliers, monster res"
tracker_note: "done (0.5.x; derived from PoE2DB monster pages; Unique ×29 on boss page life is [INFERRED]; levels 57–64 / 75–78 missing)"
defaults: v=0.5.x
---

Version: 0.5.x (PoE2DB crawl 2026-11-23). Re-check at 1.0 (Acts 5–6, atlas rework).
Status: done for 0.5.x — explicit L1–100 base-life table found (batch 30, 2026-11-26), cross-checked against 2,051 monster records.

## Base monster life by level (Normal rarity, Life multiplier 100%)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
PoE2DB's Monster page has a "Monster Stats" table with base Life for every monster level 1–100 (before the monster's own Life % and before rarity). Values:
  | Lvl | Life | Lvl | Life | Lvl | Life | Lvl | Life | Lvl | Life |
  |---|---|---|---|---|---|---|---|---|---|
  | 1 | 15 | 21 | 276 | 41 | 1,353 | 61 | 5,147 | 81 | 31,997 |
  | 2 | 20 | 22 | 305 | 42 | 1,462 | 62 | 5,478 | 82 | 32,956 |
  | 3 | 24 | 23 | 335 | 43 | 1,578 | 63 | 5,829 | 83 | 33,945 |
  | 4 | 28 | 24 | 366 | 44 | 1,705 | 64 | 6,203 | 84 | 34,963 |
  | 5 | 33 | 25 | 400 | 45 | 1,841 | 65 | 6,555 | 85 | 36,012 |
  | 6 | 38 | 26 | 434 | 46 | 1,967 | 66 | 7,079 | 86 | 37,093 |
  | 7 | 45 | 27 | 472 | 47 | 2,101 | 67 | 7,646 | 87 | 38,206 |
  | 8 | 50 | 28 | 510 | 48 | 2,244 | 68 | 8,257 | 88 | 39,352 |
  | 9 | 58 | 29 | 551 | 49 | 2,395 | 69 | 8,918 | 89 | 40,532 |
  | 10 | 67 | 30 | 593 | 50 | 2,556 | 70 | 11,148 | 90 | 41,748 |
  | 11 | 78 | 31 | 637 | 51 | 2,726 | 71 | 11,984 | 91 | 43,001 |
  | 12 | 89 | 32 | 683 | 52 | 2,909 | 72 | 12,882 | 92 | 44,291 |
  | 13 | 103 | 33 | 731 | 53 | 3,102 | 73 | 13,849 | 93 | 45,619 |
  | 14 | 118 | 34 | 790 | 54 | 3,307 | 74 | 14,887 | 94 | 46,988 |
  | 15 | 134 | 35 | 853 | 55 | 3,525 | 75 | 18,609 | 95 | 48,398 |
  | 16 | 158 | 36 | 921 | 56 | 3,756 | 76 | 20,005 | 96 | 49,850 |
  | 17 | 178 | 37 | 995 | 57 | 4,002 | 77 | 21,505 | 97 | 51,345 |
  | 18 | 200 | 38 | 1,074 | 58 | 4,264 | 78 | 23,118 | 98 | 52,885 |
  | 19 | 224 | 39 | 1,160 | 59 | 4,540 | 79 | 24,852 | 99 | 54,472 |
  | 20 | 249 | 40 | 1,253 | 60 | 4,834 | 80 | 31,065 | 100 | 56,106 |
- src: poe2db:Monster "Monster Stats" table, tier 2, crawl 2026-11-23
- conf: confirmed — the table agrees with values derived from 2,051 monster records (page Life ÷ that record's Life %) at all 48 levels where pages exist (within 0.1% from L10 up; ~1% at L2–L8 from integer rounding). Verified by two inspection passes, batch 30.
- notes: the page says values exclude map affixes, monster buffs, altars and atlas bonuses. The table steps up ~25% at L69→70, L74→75 and L79→80 (and +8% at L65→66) — [INFERRED] reading of the numbers; cause not stated. The same table also gives per-level monster Damage, Evasion, Accuracy, Armour, XP, Minion Life and Minion Damage (e.g. Damage L15 28.23, L45 108.46, L65 212.36, L79 324.19, L100 584.05).
- History: before 2026-11-26 this doc held derived values only, with L57–64 and L75–78 missing and two "outliers" at L65/L68. Those outliers were a pairing error (each record's own Life % gives the table value exactly) and are withdrawn.


## Rarity life multipliers
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Magic monsters +148% life (×2.48), Rare +700% (×8), Unique +2,800% (×29), all "final" (multiplicative). Extra players add +10% (Magic), +30% (Rare), +85% (Unique) life each; normal monsters +50% per extra player. Rarity also gives energy shield +21% / +100% / +400%, and Unique monsters deal 35% less damage.
- src: poe2db:Monster — "Monster Magic/Rare/Unique Stats" tables (monster_life_+%_final_from_rarity), tier 2, crawl 2026-11-23
- conf: single-source (game data), re-verified batch 30
- notes: [INFERRED] the "Level N Life X" on boss pages excludes the rarity multiplier, so a Unique boss's real life ≈ page value × 29. Reason: Count Geonor's page value (318) would otherwise die to a few level-5 spells; check against a boss's health bar in game. The ×29 multiplier itself is sourced; only its use on boss-page values is inferred.


## Worked boss life ([INFERRED]: page life × 29 for Unique)
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23 fill=v,vol
| Boss | Area (level) | Life % | Page life | ×29 Unique |
|---|---|---|---|---|
| Count Geonor | Ogham Manor (15) | 237% | 318 | ~9,200 |
| Jamanra, the Risen King | Halani Gates (20) | 333% | 829 | ~24,000 |
| Jamanra, the Abomination | Dreadnought (31) | 600% | 3,822 | ~111,000 |
| Doryani, Royal Thaumaturge | Black Chambers (45) | 330% | 6,075 | ~176,000 |
| Tavakai, the Chieftain | Heart of the Tribe (53) | 338% | 10,485 | ~304,000 |
| Zarokh, the Temporal | Sekhemas (22 page; scales with Barya level) | 750% | 2,288 at 22 | at 75: 18,609 × 7.5 × 29 ≈ 4.0 M |
| The Arbiter of Ash | Burning Monolith (74) | 990% | 147,381 | ~4.3 M |
| The Arbiter of Divinity | Origin Tower (79) | 990% | 246,035 | ~7.1 M |
- src: PoE2DB pages above, tier 2, crawl 2026-11-23; ×29 column [INFERRED]
- notes: Zarokh at 75 was ~3.6 M in the first version (it used an estimated ~16,500 base at L75); the explicit table gives 18,609 → ~4.0 M. [[builds/kb-test-frostbolt-chronomancer-damage-0.5.5]] now uses 4.0 M (updated 2026-11-27). Zarokh's level follows the Djinn Barya's area level ([[classes/ascendancy-trials]]) [INFERRED]. The Desperate Alliance relic makes Zarokh take 75% less damage (= ×4 effective life) and deal 100% more ([[endgame/sekhemas]]). Campaign boss stat blocks → [[campaign/boss-data-acts-1-2]], [[campaign/boss-data-acts-3-4]].


## Monster resistances
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
PoE2DB lists monster resistances in the order Fire / Cold / Lightning / Chaos (confirmed by Moltenmettle, a fire monster: 90 / −15 / 0 / 0). Monster default max resistance 75%.
- Examples: Count Geonor **45% cold**; Jamanra, the Abomination 45% fire / −15% cold / 45% lightning; Tavakai 45% fire; Zarokh 15% all elements on PoE2DB stats (PoB spectre data shows 0% — conflict).
- src: PoE2DB monster pages + poe2db:Monster "Monster Default" (base_maximum_all_resistances_% 75), tier 2, crawl 2026-11-23
- conf: single-source; column order [INFERRED] from one fire monster (strong); Zarokh value → kb/04-conflicts.md
- notes: map/rarity mods add more resistance → [[mechanics/resistances]].


## Monster crit damage (resolves an open conflict)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=v,vol
Monster default critical damage bonus = 30%.

- src: poe2db:Monster "Monster Default" (base_critical_hit_damage_bonus 30); boss pages show "Critical Damage Bonus +30%", tier 2, crawl 2026-11-23
- conf: single-source game data; agrees with Mobalytics (30%) vs poe2wiki (40% less) → kb/04-conflicts.md "Monster critical damage bonus" resolved by game data.

## Monster Power / Effectiveness
- Power: average monster 1; strong 2–3; × rarity (Normal 1, Magic 2, Rare 5); Uniques always 20 ([PoE2DB Monster Power](https://poe2db.tw/us/Monster_Power)). Used by flask/charm charges ([[mechanics/charms]]).
- Effectiveness: per 2% increased, monsters gain 2% more toughness, 1% more XP, 1% more item quantity ([PoE2DB Monster Effectiveness](https://poe2db.tw/us/Monster_Effectiveness)). Corrupted/juiced maps raise effectiveness → [[strategy/atlas-starter-strategy]].
