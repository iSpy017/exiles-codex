# Pinnacle Bosses: Stat Profiles and Biggest Hits

Status: partial. Life/res/armour and top skill hits per boss done. Phase mechanics, dodge timing and per-skill damage types beyond the top entries not covered (see PoE2DB pages). Unlock paths: [[endgame/pinnacle-bosses]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB area pages (map table rows) and boss pages (stat block, skill blocks), tier 2.

## Stat table (area-page rows)
- Claim: Rows from each pinnacle area page. Life = value in the map table. Res columns are unlabelled on the page; order fire / cold / lightning / chaos, confirmed against 0.5.5 notes for Ash and Divinity. "Dmg" = monster base damage column, not a skill hit.

| Boss | Lvl | Life | Armour | ES | Fire/Cold/Light/Chaos res | Dmg | Atk time |
|---|---|---|---|---|---|---|---|
| Arbiter of Ash | 74 | 4,274,058 | 4,099 | none shown | 30 / -30 / 0 / 0 | 802 | 2.0874 |
| Arbiter of Divinity | 79 | 7,135,009 | 6,356 | 24,603 | -30 / 0 / 30 / 0 | 661 | 1.47 |
| Xesht | 79 | 10,378,195 | 4,540 | 17,893 | 30 / 30 / 30 / 0 | 620 | 1.47 |
| The Bodach | 79 | 13,116,886 | 7,945 | none shown | 0 / 0 / 0 / 0 | 661 | 1.3083 |
| The Aberration | 79 | 7,135,009 | 6,810 | none shown | 30 / 0 / 0 / 0 | 661 | 1.47 |
| Raven Trickster | 79 | 7,135,009 | 5,221 | 24,603 | 0 / 0 / 0 / 0 | 929 | 1.47 |
| Vessel of Kulemak | 79 | 1,873,841 | 6,810 | 6,462 | 0 / 0 / 0 / 0 | 1,099 | 1.47 |

- Version: 0.5.x
- Volatility: may-change (0.5.4 lowered several pinnacle resistances; 0.5.5 removed all-elemental resist on Ash, Divinity, Raven Trickster)
- Source: [PoE2DB The Burning Monolith](https://poe2db.tw/us/The_Burning_Monolith), [The Origin Tower](https://poe2db.tw/us/The_Origin_Tower), [Twisted Domain](https://poe2db.tw/us/Twisted_Domain), [Caer Tarth](https://poe2db.tw/us/Caer_Tarth), [Ruins of Kingsmarch](https://poe2db.tw/us/Ruins_of_Kingsmarch), [The Withered Willow](https://poe2db.tw/us/The_Withered_Willow), [The Well of Souls](https://poe2db.tw/us/The_Well_of_Souls), [0.5.5 notes](https://poe2db.tw/us/Version_0.5.5), tier 2, crawl 2026-11-23
- Confidence: confirmed for Ash and Divinity res order (map table + 0.5.5 note); single-source for others
- Notes: Vessel of Kulemak's table life is far below the other L79 bosses; boss page says 260% life vs 990% for Divinity. Table excludes map affixes, atlas bonuses and buffs. `atlas-dependent`.

## Life method check
- Claim: Map-table life equals the boss page's stat-block life times 29: Ash 147,381 x 29 = 4,274,049 (table 4,274,058); Xesht 357,869 x 29 = 10,378,201 (table 10,378,195); Kulemak 64,615 x 29 = 1,873,835 (table 1,873,841). Page life percentages: Ash 990%, Divinity 990%, Aberration 990%, Raven 990%, Xesht 1440%, Bodach 1820%, Kulemak 260%.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB The Arbiter of Ash](https://poe2db.tw/us/The_Arbiter_of_Ash), [Xesht](https://poe2db.tw/us/Xesht_2C_We_That_Are_One), [Vessel of Kulemak](https://poe2db.tw/us/Vessel_of_Kulemak), tier 2, crawl 2026-11-23
- Confidence: [INFERRED]: the x29 unique factor is the library method ([[mechanics/monster-life]]); the three matches above (within rounding) support it, the pages do not state "29".
- Notes: Kosis page life (L68 stat block) 10,321 with ES 1,032; x29 gives about 299,300 [INFERRED]; Kosis is a delirium boss tier 2 (not tier 3), 125% life, 0 res.

## Biggest hits per boss (skill-block values)
- Claim: Largest single "Deals X to Y" skill entries on each boss page, with PoE2DB's "cannot be avoided by dodge roll or evaded or blocked" flag where shown (A = flagged). Values are the skill block as displayed, before map, atlas and rarity multipliers.
  - Ash: Flame Seed "donut nuke" 18,307-27,461 Fire (A); Bullet Hell high hit 18,307-27,461 Fire (A, channel, 55 s cooldown); Pulsing Ball 915-1,373 Fire; ordinary melee attacks base 1,007-1,510.
  - Divinity: Extendo Spear combo volatile explosion 1,323-3,969 Lightning; Storm Blink Bolt 860-2,580 Lightning (A); Spear Toss impact (GAAoDP1_SpearTossImpact) attack base 830-1,245 with 45% more attack damage (A); the separate Spear Toss projectile skill (MPAAoDP1_SpearToss) shows 95% less attack damage.
  - Xesht: Pistol Flick Sonic Wave 2,540-3,810 Physical (A); Head fireball impact 2,540-3,810 Fire; Hand Clap Blast 2,540-3,810 Physical; Multi-Flick impact 1,588-2,382 Physical (A); hand slams attack base 778-1,167 with 200% more attack damage (A).
  - Bodach: Vacuum Vomit 2,117-3,175 Physical; Bombard impact 1,058-1,588 Physical; head slam attack base 830-1,245, 120% more (flag text: not avoidable by dodge roll or block); phase-2 meteor slams flagged.
  - Aberration: Combo Beam 2,117-3,175 Cold; Verisium Storm/Torpedo 1,058-1,588 Physical; Mortar 445-667 Physical (A).
  - Raven Trickster: Frost Comet, Big Boy Beam, Pillar Fall each 2,117-3,175 (Cold/Physical/Physical); Volatile Flame Blast 1,958-2,937 Lightning (A); Phase Change Blast 212-318 Physical (A).
  - Vessel of Kulemak: Cleave 1,852-2,778 Cold; green Cleave 1,482-2,223 Physical; no unavoidable flag found in the top six.
  - Kosis: top skill 215-646 Lightning (no flag found); L68 stat block.
- Version: 0.5.x
- Volatility: may-change (0.5.4: Ash chaos-sphere bonus reduced, sphere damage buff 30 s to 20 s)
- Source: [PoE2DB The Arbiter of Ash](https://poe2db.tw/us/The_Arbiter_of_Ash), [The Arbiter of Divinity](https://poe2db.tw/us/The_Arbiter_of_Divinity), [Xesht](https://poe2db.tw/us/Xesht_2C_We_That_Are_One), [The Bodach](https://poe2db.tw/us/The_Bodach), [The Aberration](https://poe2db.tw/us/The_Aberration), [The Raven Trickster](https://poe2db.tw/us/The_Raven_Trickster), [Vessel of Kulemak](https://poe2db.tw/us/Vessel_of_Kulemak), [Kosis](https://poe2db.tw/us/Kosis_2C_The_Revelation), [0.5.4 notes](https://poe2db.tw/us/Version_0.5.4), tier 2, crawl 2026-11-23
- Confidence: single-source. Pages show multiple variant blocks (Ash page has a second, level-68 standalone block); numbers above are from the first (area) block.
- Notes: Ash's unavoidable fire hit is about 5x or more any other boss's top hit as displayed; whether in-game it is a one-shot check is not in the corpus. Resist your own fire hard for Ash [INFERRED from the 18k-27k Fire unavoidable entries]. `atlas-dependent` for scaling.

## Resistance history
- Claim: 0.5.4 notes: several pinnacle bosses had resistances lowered. 0.5.5: Ash now has fire resistance and cold vulnerability instead of all-elemental resistance; Divinity has lightning resistance and fire vulnerability; Raven Trickster lost all-elemental resistance; Omniphobia also lost it.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB 0.5.4 notes](https://poe2db.tw/us/Version_0.5.4), [0.5.5 notes](https://poe2db.tw/us/Version_0.5.5), tier 2, crawl 2026-11-23
- Confidence: confirmed (notes + current table rows)
- Notes: Tune damage type by boss: Ash -30 cold, Divinity -30 fire (table rows).

## Drops
- Claim: Unique and key drops per boss are on the boss pages; do not repeat here. See [[items/uniques-drop-sources]]. Non-unique extras noted on PoE2DB: Xesht also lists Xesht's Reliquary Key plus four breach uniques as additional drops; Raven Trickster lists Raven-Touched Shard; Aberration lists Starlit Ore variants and Olroth's Conviction.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Xesht](https://poe2db.tw/us/Xesht_2C_We_That_Are_One), [The Raven Trickster](https://poe2db.tw/us/The_Raven_Trickster), [The Aberration](https://poe2db.tw/us/The_Aberration), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: drop rates not on pages.
