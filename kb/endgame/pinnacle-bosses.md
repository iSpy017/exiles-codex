---
title: Pinnacle Bosses: Roster, Unlock Keys, Areas
status: partial
tracker_topic: "Pinnacle bosses + keys/fragments"
tracker_note: "partial (0.5.x roster, keys, stats, biggest hits; Triskelion + Raven's Reflection sources added 2026-11-27; recheck 1.0)"
defaults: v=0.5.x
merged_from: [pinnacle-bosses.md, pinnacle-bosses-2.md]
---

Status: partial. Roster, keys, area levels done. Exact drop rates for keys not in corpus. Stat profiles and big hits: [[endgame/pinnacle-bosses]]. Uber/quest-vs-farm versions: [[endgame/uber-bosses]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here checked against 1.0.
Sources: PoE2DB map/boss/item pages and 0.5.x patch-note pages (tier 2), local corpus.
Tag `atlas-dependent` = depends on atlas layout, waystone tier or atlas passives.

## Roster (map pages tagged pinnacle_boss, plus Kosis and Kulemak)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
PoE2DB tags six pinnacle-boss map areas, all Area Level 79 except the Burning Monolith (74): Burning Monolith (Arbiter of Ash), Origin Tower (Arbiter of Divinity), Twisted Domain (Xesht), Caer Tarth (The Bodach), Ruins of Kingsmarch (The Aberration), Withered Willow (The Raven Trickster). The Well of Souls endgame variant (Vessel of Kulemak, area 79) is a seventh. Kosis is the Simulacrum-encounter boss, not a map boss.
- src: poe2db:The_Burning_Monolith, poe2db:Twisted_Domain, poe2db:The_Origin_Tower, poe2db:Caer_Tarth, poe2db:Ruins_of_Kingsmarch, poe2db:The_Withered_Willow, poe2db:The_Well_of_Souls, tier 2, crawl 2026-11-23
- conf: single-source (area pages), consistent across pages
- notes: Sirus-style "uber ladder" not found; see [[endgame/uber-bosses]].


## Shared pinnacle-area rules
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Pinnacle map areas (Monolith, Origin Tower, Caer Tarth, Kingsmarch, Willow) list: players cannot gain or lose XP, unlimited revivals, 1 corrupted rare tablet drop, 5% rare socket-currency chance, 10% special gem drop chance (stat lines as shown, "% chance" units per the stat name). Twisted Domain lists no-XP and no league tablets but no revival line. 0.5.1 fix note: monster levels of these areas could rise to 82 before the quest version was killed with your own quest fragment.
- src: poe2db:The_Burning_Monolith, poe2db:Twisted_Domain, poe2db:Version_0.5.1 «0.5.1 notes», tier 2, crawl 2026-11-23
- notes: [INFERRED] level 82 is the repeatable (non-quest) version's level, because the fix says levels rose to 82 only after the quest kill; the notes do not state the non-quest level outright. `atlas-dependent`.


## The Arbiter of Ash (The Burning Monolith, area 74)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Entry needs three different Crisis Fragments, one from each Citadel type: Ancient from the Iron Citadel, Faded from the Copper Citadel, Weathered from the Stone Citadel. Each Citadel needs a Tier 15+ waystone; extra waystone drop chance can give extra fragments. Fragments are slotted into a door inside the Monolith. The Monolith itself needs the Ancient Gateway completed (quest chain).
- src: poe2db:Iron_Citadel, poe2db:Copper_Citadel, poe2db:Stone_Citadel, poe2db:Ancient_Crisis_Fragment, poe2db:The_Burning_Monolith, tier 2, crawl 2026-11-23
- conf: confirmed (Citadel pages + Monolith page agree)
- notes: Citadel bosses: Count Geonor (Iron, area 80), Jamanra the Abomination (Copper, 80), Doryani Royal Thaumaturge plus Doryani's Triumph (Stone, 80). `atlas-dependent` (waystone tier, drop-chance passives). Quest versions of fragments come from two Enigma Chambers (Count Geonor, Doryani); see [[endgame/uber-bosses]].


## The Arbiter of Divinity (The Origin Tower, area 79)
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
Needs an Origin Core, made by combining one Origin Spark and one Origin Cradle inside the Origin Tower. Tower access line: complete the Burning Monolith first. Spark/Cradle come from Phyx (Patriarch Halls) and Phya (Matriarch Halls), both area 65, Tier 15+ waystones; Spark and Cradle also tradeable on the Currency Exchange.
- src: poe2db:Origin_Core, poe2db:The_Origin_Tower, poe2db:The_Patriarch_Halls, poe2db:The_Matriarch_Halls, poe2db:Version_0.5.5c «0.5.5c notes», tier 2, crawl 2026-11-23
- conf: [INFERRED] that the Halls bosses are the Spark/Cradle source (0.5.5c note says you must be present when the Hall bosses die to pick up Spark/Cradle; the Hall pages themselves do not list the item)
- notes: Non-quest Origin Core kill completes the whole Precursor Fortress for the map owner (0.5.5 note). `atlas-dependent`.


## Xesht, We That Are One (Twisted Domain, area 79)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Breach pinnacle. Breachlord Sac is a map-fragment item (listed among the Keepers of the Flame quest rewards on the Breach page, also on the Currency Exchange); its text says to bring it to the Dreamer in the Monastery of the Keepers. 0.5.0 notes: Breach Fortresses hold bosses Tul and Esh whose kill gives a key to the existing Breach pinnacle boss. Which of the two (Sac vs Tul/Esh key) opens the repeatable fight is not stated in the corpus.
- src: poe2db:Breachlord_Sac, poe2db:Breach, poe2db:Twisted_Domain, poe2db:Version_0.5.0 «0.5.0 notes», tier 2, crawl 2026-11-23
- conf: single-source; ambiguity noted
- notes: Xesht also appears in "Boss Rush Area 3" (area 35, a separate boss-rush chain); not detailed here. Twisted Domain mods: Breach timer 45,000 ms initial, 150,000 ms to portal, 200% more breach chest-ring and catalyst quantity. `atlas-dependent`.


## The Bodach (Caer Tarth, area 79)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Ritual pinnacle. Perform the Rite of the Nameless at the effigy in Caer Tarth. Needs five "Call of the Shadows" (stack of 5, tradeable) or the five effigy pieces dropped from completing all altars in each Rite map. 0.5.0: killing The King in the Mists drops Head of the King (bring to Aoife in Caer Tarth to begin the Rite); each Rite map awards one element of the pinnacle key.
- src: poe2db:Call_of_the_Shadows, poe2db:Rite_of_the_Nameless, poe2db:Head_of_the_King, poe2db:Version_0.5.0 «0.5.0 notes», tier 2, crawl 2026-11-23
- notes: Rite = chain of 5 maps; bosses reappear in later maps (0.5.0 note). `atlas-dependent`.


## The Aberration (Ruins of Kingsmarch / Fallen Star, area 79)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Expedition (Runes of Aldur) pinnacle. Key is The Triskelion Reforged, made at the Verisium Anvil from Shattered Triskelion; use it at the Fallen Star after speaking to Makoru in the Ruins of Kingsmarch. Tradeable (Currency Exchange listing).
- src: poe2db:The_Triskelion_Reforged, poe2db:Shattered_Triskelion, tier 2, crawl 2026-11-23
- notes: Shattered Triskelion drops from Olroth, Origin of the Fall (drop-restricted, drop level 1) — poe2wiki Shattered Triskelion [S745], tier 2, retrieved 2026-11-27.


## The Raven Trickster (The Withered Willow, area 79)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Delirium pinnacle. Key: Raven's Reflection, brought to the Mirror in the Withered Willow. Separate Delirium pinnacle encounter: Simulacrum (see Kosis).
- src: poe2db:Ravens_Reflection «PoE2DB Raven's Reflection», poe2db:Delirium, tier 2, crawl 2026-11-23
- notes: Raven's Reflection is obtained by completing the Simulacrum (drop-restricted) — poe2wiki Raven's Reflection [S746], tier 2, retrieved 2026-11-27. The wiki names the place to use it "The Withered Hollow", PoE2DB "The Withered Willow" ([[conflicts]] C053).


## Kosis, The Revelation (Simulacrum)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Delirium page lists the Simulacrum encounter plus Kosis as the Delirium "Pinnacle Boss". Simulacrum = 300 Simulacrum Splinters combined, then applied to a Delirium-fogged map with at least 100% Deliriousness. Simulacrum of Delusion maps: area 80, Tier 14+ waystone.
- src: poe2db:Simulacrum, poe2db:Simulacrum_Splinter, poe2db:Simulacrum_of_Delusion, poe2db:Delirium, tier 2, crawl 2026-11-23
- notes: Kosis' wave placement and the area level at which he spawns inside a Simulacrum are not in the corpus. `atlas-dependent`.


## Vessel of Kulemak (The Well of Souls endgame variant, area 79)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Abyss pinnacle. Key: Kulemak's Invitation (reward line of the "Abyssal Power" quest; item text points to the Well). 0.5.4b notes: the pinnacle key is consumed on interaction.
- src: poe2db:Abyssal_Power, poe2db:Kulemaks_Invitation «Kulemak's Invitation», poe2db:The_Well_of_Souls, poe2db:Version_0.5.4b «0.5.4b notes», tier 2, crawl 2026-11-23
- notes: 0.5.1 notes mention Kulemak difficulty increases; PoE2DB marks some Kosis drops "(Difficulty 2+/4)"; scale not explained in corpus.


## Key prices
@ v=0.5.x vol=volatile conf=? date=2026-11-23
Not recorded. PoE2DB's economy panels name no league, so figures are omitted per project rule. Check live prices on [PoE2DB economy fragments](https://poe2db.tw/us/Economy_Fragments) or poe.ninja at league start, with date and league.
- src: none (omitted)
- conf: n/a
- notes: Keys are tradeable on the Currency Exchange per 0.5.1 notes (Call of the Shadows, Origin fragments).


<!-- merged from kb/endgame/pinnacle-bosses-2.md -->
Part title: Pinnacle Bosses: Stat Profiles and Biggest Hits

Status: partial. Life/res/armour and top skill hits per boss done. Phase mechanics, dodge timing and per-skill damage types beyond the top entries not covered (see PoE2DB pages). Unlock paths: [[endgame/pinnacle-bosses]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB area pages (map table rows) and boss pages (stat block, skill blocks), tier 2.

## Stat table (area-page rows)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Rows from each pinnacle area page. Life = value in the map table. Res columns are unlabelled on the page; order fire / cold / lightning / chaos, confirmed against 0.5.5 notes for Ash and Divinity. "Dmg" = monster base damage column, not a skill hit.

| Boss | Lvl | Life | Armour | ES | Fire/Cold/Light/Chaos res | Dmg | Atk time |
|---|---|---|---|---|---|---|---|
| Arbiter of Ash | 74 | 4,274,058 | 4,099 | none shown | 30 / -30 / 0 / 0 | 802 | 2.0874 |
| Arbiter of Divinity | 79 | 7,135,009 | 6,356 | 24,603 | -30 / 0 / 30 / 0 | 661 | 1.47 |
| Xesht | 79 | 10,378,195 | 4,540 | 17,893 | 30 / 30 / 30 / 0 | 620 | 1.47 |
| The Bodach | 79 | 13,116,886 | 7,945 | none shown | 0 / 0 / 0 / 0 | 661 | 1.3083 |
| The Aberration | 79 | 7,135,009 | 6,810 | none shown | 30 / 0 / 0 / 0 | 661 | 1.47 |
| Raven Trickster | 79 | 7,135,009 | 5,221 | 24,603 | 0 / 0 / 0 / 0 | 929 | 1.47 |
| Vessel of Kulemak | 79 | 1,873,841 | 6,810 | 6,462 | 0 / 0 / 0 / 0 | 1,099 | 1.47 |

- src: poe2db:The_Burning_Monolith, poe2db:The_Origin_Tower, poe2db:Twisted_Domain, poe2db:Caer_Tarth, poe2db:Ruins_of_Kingsmarch, poe2db:The_Withered_Willow, poe2db:The_Well_of_Souls, poe2db:Version_0.5.5 «0.5.5 notes», tier 2, crawl 2026-11-23
- vol: may-change (0.5.4 lowered several pinnacle resistances; 0.5.5 removed all-elemental resist on Ash, Divinity, Raven Trickster)
- conf: confirmed for Ash and Divinity res order (map table + 0.5.5 note); single-source for others
- notes: Vessel of Kulemak's table life is far below the other L79 bosses; boss page says 260% life vs 990% for Divinity. Table excludes map affixes, atlas bonuses and buffs. `atlas-dependent`.


## Life method check
@ v=0.5.x vol=stable conf=inferred date=2026-11-23
Map-table life equals the boss page's stat-block life times 29: Ash 147,381 x 29 = 4,274,049 (table 4,274,058); Xesht 357,869 x 29 = 10,378,201 (table 10,378,195); Kulemak 64,615 x 29 = 1,873,835 (table 1,873,841). Page life percentages: Ash 990%, Divinity 990%, Aberration 990%, Raven 990%, Xesht 1440%, Bodach 1820%, Kulemak 260%.
- src: poe2db:The_Arbiter_of_Ash, poe2db:Xesht_2C_We_That_Are_One «Xesht», poe2db:Vessel_of_Kulemak, tier 2, crawl 2026-11-23
- conf: [INFERRED]: the x29 unique factor is the library method ([[mechanics/monster-life]]); the three matches above (within rounding) support it, the pages do not state "29".
- notes: Kosis page life (L68 stat block) 10,321 with ES 1,032; x29 gives about 299,300 [INFERRED]; Kosis is a delirium boss tier 2 (not tier 3), 125% life, 0 res.


## Biggest hits per boss (skill-block values)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Largest single "Deals X to Y" skill entries on each boss page, with PoE2DB's "cannot be avoided by dodge roll or evaded or blocked" flag where shown (A = flagged). Values are the skill block as displayed, before map, atlas and rarity multipliers.
  - Ash: Flame Seed "donut nuke" 18,307-27,461 Fire (A); Bullet Hell high hit 18,307-27,461 Fire (A, channel, 55 s cooldown); Pulsing Ball 915-1,373 Fire; ordinary melee attacks base 1,007-1,510.
  - Divinity: Extendo Spear combo volatile explosion 1,323-3,969 Lightning; Storm Blink Bolt 860-2,580 Lightning (A); Spear Toss impact (GAAoDP1_SpearTossImpact) attack base 830-1,245 with 45% more attack damage (A); the separate Spear Toss projectile skill (MPAAoDP1_SpearToss) shows 95% less attack damage.
  - Xesht: Pistol Flick Sonic Wave 2,540-3,810 Physical (A); Head fireball impact 2,540-3,810 Fire; Hand Clap Blast 2,540-3,810 Physical; Multi-Flick impact 1,588-2,382 Physical (A); hand slams attack base 778-1,167 with 200% more attack damage (A).
  - Bodach: Vacuum Vomit 2,117-3,175 Physical; Bombard impact 1,058-1,588 Physical; head slam attack base 830-1,245, 120% more (flag text: not avoidable by dodge roll or block); phase-2 meteor slams flagged.
  - Aberration: Combo Beam 2,117-3,175 Cold; Verisium Storm/Torpedo 1,058-1,588 Physical; Mortar 445-667 Physical (A).
  - Raven Trickster: Frost Comet, Big Boy Beam, Pillar Fall each 2,117-3,175 (Cold/Physical/Physical); Volatile Flame Blast 1,958-2,937 Lightning (A); Phase Change Blast 212-318 Physical (A).
  - Vessel of Kulemak: Cleave 1,852-2,778 Cold; green Cleave 1,482-2,223 Physical; no unavoidable flag found in the top six.
  - Kosis: top skill 215-646 Lightning (no flag found); L68 stat block.
- src: poe2db:The_Arbiter_of_Ash, poe2db:The_Arbiter_of_Divinity, poe2db:Xesht_2C_We_That_Are_One «Xesht», poe2db:The_Bodach, poe2db:The_Aberration, poe2db:The_Raven_Trickster, poe2db:Vessel_of_Kulemak, poe2db:Kosis_2C_The_Revelation «Kosis», poe2db:Version_0.5.4 «0.5.4 notes», tier 2, crawl 2026-11-23
- vol: may-change (0.5.4: Ash chaos-sphere bonus reduced, sphere damage buff 30 s to 20 s)
- conf: single-source. Pages show multiple variant blocks (Ash page has a second, level-68 standalone block); numbers above are from the first (area) block.
- notes: Ash's unavoidable fire hit is about 5x or more any other boss's top hit as displayed; whether in-game it is a one-shot check is not in the corpus. Resist your own fire hard for Ash [INFERRED from the 18k-27k Fire unavoidable entries]. `atlas-dependent` for scaling.


## Resistance history
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
0.5.4 notes: several pinnacle bosses had resistances lowered. 0.5.5: Ash now has fire resistance and cold vulnerability instead of all-elemental resistance; Divinity has lightning resistance and fire vulnerability; Raven Trickster lost all-elemental resistance; Omniphobia also lost it.
- src: poe2db:Version_0.5.4 «PoE2DB 0.5.4 notes», poe2db:Version_0.5.5 «0.5.5 notes», tier 2, crawl 2026-11-23
- conf: confirmed (notes + current table rows)
- notes: Tune damage type by boss: Ash -30 cold, Divinity -30 fire (table rows).


## Drops
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Unique and key drops per boss are on the boss pages; do not repeat here. See [[items/uniques-drop-sources]]. Non-unique extras noted on PoE2DB: Xesht also lists Xesht's Reliquary Key plus four breach uniques as additional drops; Raven Trickster lists Raven-Touched Shard; Aberration lists Starlit Ore variants and Olroth's Conviction.
- src: poe2db:Xesht_2C_We_That_Are_One «PoE2DB Xesht», poe2db:The_Raven_Trickster, poe2db:The_Aberration, tier 2, crawl 2026-11-23
- notes: drop rates not on pages.
