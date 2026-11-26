---
title: Soul core effects 1 (tiers 1-3 named, sources)
status: done
tracker_topic: "Soul core & idol effects"
tracker_note: "done (0.5.x; all soul cores, 31 idols, Ancient Augments; drop sources partial; 2 slot conflicts)"
defaults: v=0.5.x
merged_from: [soul-core-idol-effects.md, soul-core-idol-effects-2.md, soul-core-idol-effects-3.md, soul-core-idol-effects-4.md]
data: [data/poe2db/Amanamus_Gaze.tsv, data/poe2db/Atmohuas_Soul_Core_of_Retreat.tsv, data/poe2db/Bear_Idol.tsv, data/poe2db/Boar_Idol.tsv, data/poe2db/Carved_Cunning.tsv, data/poe2db/Cat_Idol.tsv, data/poe2db/Citaqualotls_Soul_Core_of_Foulness.tsv, data/poe2db/Emergent_Vigour.tsv, data/poe2db/Fox_Idol.tsv, data/poe2db/Idol_of_Alira.tsv, data/poe2db/Idol_of_the_Martyr.tsv, data/poe2db/Idol_of_the_Pharisee.tsv]  # generated from the crawl; query these instead of reading the tables
---

- Status: done for item list; drop sources partial
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-item pages and Soul Core / Idol / Ancient Augment index pages, tier 2.

## Soul core tiers 1-2 (plain "Soul Core of X", 16 cores)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Drop level 35; no level requirement shown. Tags tier1 (Citaqualotl, Opiloti, Tacati, Topotante) and tier2 (rest). Effect per slot below.
| Soul core | Tier | Req/drop | Limit | Effect by slot | Socket into |
|---|---|---|---|---|---|
| Soul Core of Atmohua | T2 | -/35 | - | Martial Weapon: Convert 40% of Requirements to Strength ; Armour: Convert 40% of Requirements to Strength | a Weapon or Armour |
| Soul Core of Azcapa | T2 | -/35 | - | Martial Weapon: +15 to Spirit ; Gloves: 10% increased Quantity of Gold Dropped by Slain Enemies | a Weapon or a pair of Gloves |
| Soul Core of Cholotl | T2 | -/35 | - | Martial Weapon: Convert 40% of Requirements to Dexterity ; Armour: Convert 40% of Requirements to Dexterity | a Weapon or Armour |
| Soul Core of Citaqualotl | T1 | -/35 | - | Martial Weapon: 40% increased Elemental Damage with Attacks ; Armour: +6% to all Elemental Resistances | a Weapon or Armour |
| Soul Core of Jiquani | T2 | -/35 | 1 | Martial Weapon: Recover 5% of maximum Life on Kill ; Body Armours: 5% increased maximum Life | a Weapon or a Body Armour |
| Soul Core of Opiloti | T1 | -/35 | 1 | Martial Weapon: 40% increased Magnitude of Bleeding you inflict ; Helmets: 25% increased Pin duration | a Weapon or a Helmet |
| Soul Core of Puhuarte | T2 | -/35 | 1 | Martial Weapon: 40% increased Ignite Magnitude ; Gloves: +2% to Maximum Fire Resistance | a Weapon or a pair of Gloves |
| Soul Core of Quipolatl | T2 | -/35 | - | Martial Weapon: 5% increased Attack Speed ; Boots: 15% reduced Slowing Potency of Debuffs on You | a Weapon or a pair of Boots |
| Soul Core of Tacati | T1 | -/35 | - | Martial Weapon: 25% increased Magnitude of Poison you inflict ; Armour: +13% to Chaos Resistance | a Weapon or Armour |
| Soul Core of Ticaba | T2 | -/35 | 1 | Martial Weapon: +5% to Critical Damage Bonus ; Body Armours: Hits against you have 50% reduced Critical Damage Bonus ; Shields and Bucklers: Hits against you have 50% reduced Critical Damage Bonus | a Weapon, a Body Armour or a Shield |
| Soul Core of Topotante | T1 | -/35 | 1 | Martial Weapon: Attacks with this Weapon Penetrate 25% Elemental Resistances ; Boots: 25% reduced Effect of Non-Damaging Ailments on you | a Weapon or a pair of Boots |
| Soul Core of Tzamoto | T2 | -/35 | 1 | Martial Weapon: 60% increased Freeze Buildup ; Helmets: +2% to Maximum Cold Resistance | a Weapon or a Helmet |
| Soul Core of Vizoma | T2 | -/35 | 1 | Martial Weapon: +150 to Accuracy Rating ; Wand or Staff: 30% increased Critical Hit Chance for Spells | a Weapon |
| Soul Core of Xopec | T2 | -/35 | 1 | Martial Weapon: 25% increased Magnitude of Shock you inflict ; Boots: +2% to Maximum Lightning Resistance | a Weapon or a pair of Boots |
| Soul Core of Zalatl | T2 | -/35 | 1 | Martial Weapon: Recover 4% of maximum Mana on Kill ; Helmets: 5% increased maximum Mana | a Weapon or a Helmet |
| Soul Core of Zantipi | T2 | -/35 | - | Martial Weapon: Convert 40% of Requirements to Intelligence ; Armour: Convert 40% of Requirements to Intelligence | a Weapon or Armour |
- src: poe2db:Soul_Core_of_Atmohua, poe2db:Soul_Core_of_Azcapa, poe2db:Soul_Core_of_Cholotl and the rest at https://poe2db.tw/us/Soul_Core_of_<Name>; poe2db:Soul_Core, tier 2, crawl 2026-11-23
- notes: Soul Core of Vizoma page shows no Currency Exchange gold cost. Drop source not stated on item pages. Attribute cores (Atmohua/Cholotl/Zantipi) convert 40% of item requirements to Str/Dex/Int.


## Soul core tier 3, named cores (15 non-Jiquani)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
All limit 1, req lvl 50, drop level 65.
| Soul core | Tier | Req/drop | Limit | Effect by slot | Socket into |
|---|---|---|---|---|---|
| Atmohua's Soul Core of Retreat | T3 | 50/65 | 1 | Body Armours: 40% increased Energy Shield from Equipped Focus ; Foci: 30% increased Energy Shield from Equipped Body Armour | a Body Armour or a Focus |
| Cholotl's Soul Core of War | T3 | 50/65 | 1 | Bows: Projectiles have 20% chance to Chain an additional time from terrain | a Bow |
| Citaqualotl's Soul Core of Foulness | T3 | 50/65 | 1 | Martial Weapon: Adds 19 to 29 Chaos damage | a Martial Weapon |
| Estazunti's Soul Core of Convalescence | T3 | 50/65 | 1 | Boots: 15% increased speed of Recoup Effects ; Helmets: 10% of Damage taken Recouped as Life | a pair of Boots or a Helmet |
| Guatelitzi's Soul Core of Endurance | T3 | 50/65 | 1 | Martial Weapon: 50% chance when you gain an Endurance Charge to gain an additional Endurance Charge ; Wand or Staff: 50% chance when you gain an Endurance Charge to gain an additional Endurance Charge | a Weapon |
| Hayoxi's Soul Core of Heatproofing | T3 | 50/65 | 1 | Helmets: +40% of Armour also applies to Cold Damage | a Helmet or Sceptre |
| Opiloti's Soul Core of Assault | T3 | 50/65 | 1 | Martial Weapon: 50% chance when you gain a Frenzy Charge to gain an additional Frenzy Charge ; Wand or Staff: 50% chance when you gain a Frenzy Charge to gain an additional Frenzy Charge | a Weapon |
| Quipolatl's Soul Core of Flow | T3 | 50/65 | 1 | Helmets: 8% increased Skill Effect Duration, 8% increased Cooldown Recovery Rate | a Helmet |
| Tacati's Soul Core of Affliction | T3 | 50/65 | 1 | Helmets: Enemies you Curse have -5% to Chaos Resistance | a Helmet |
| Topotante's Soul Core of Dampening | T3 | 50/65 | 1 | Gloves: +40% of Armour also applies to Fire Damage | a pair of Gloves |
| Tzamoto's Soul Core of Ferocity | T3 | 50/65 | 1 | Helmets: +4 to Maximum Rage | a Helmet |
| Uromoti's Soul Core of Attenuation | T3 | 50/65 | 1 | Boots: 20% increased Curse Duration, 20% increased Poison Duration | a pair of Boots |
| Xipocado's Soul Core of Dominion | T3 | 50/65 | 1 | Wand or Staff: Minions deal 40% increased Damage with Command Skills ; Sceptres: Minions deal 40% increased Damage with Command Skills | a Wand, a Staff or a Sceptre |
| Xopec's Soul Core of Power | T3 | 50/65 | 1 | Martial Weapon: 50% chance when you gain a Power Charge to gain an additional Power Charge ; Wand or Staff: 50% chance when you gain a Power Charge to gain an additional Power Charge | a Weapon |
| Zalatl's Soul Core of Insulation | T3 | 50/65 | 1 | Boots: +40% of Armour also applies to Lightning Damage | a pair of Boots |
- src: poe2db:Atmohuas_Soul_Core_of_Retreat, poe2db:Cholotls_Soul_Core_of_War, poe2db:Citaqualotls_Soul_Core_of_Foulness and the rest at https://poe2db.tw/us/<Page>, tier 2, crawl 2026-11-23
- notes: Page names drop the apostrophe, e.g. Hayoxis_Soul_Core_of_Heatproofing. Citaqualotl/Guatelitzi/Jiquani/Quipolatl Theses are a separate set (see [[items/soul-core-idol-effects]]).


## Soul core sources and related items
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Corpus statements: Atziri's Temple unique boss drops additional Soul Cores ([Atziris Temple](https://poe2db.tw/us/Atziris_Temple)); the Trialmaster in the Trial of Chaos occasionally offers Soul Cores ([The Trial of Chaos](https://poe2db.tw/us/The_Trial_of_Chaos)); a 0.1.1e note says Soul Cores no longer drop outside The Temple of Chaos (old, may be outdated); Thesis cores can sometimes be obtained by modifying a soul core with a Core Destabiliser (drop level 1, 250 gold; modifies a soul core unpredictably with a chance to destroy it, [Core Destabiliser](https://poe2db.tw/us/Core_Destabiliser)). Large/Medium/Small Soul Core and Vaal Soul Core are quest/instance items, not augments.
- src: poe2db:Soul_Core, poe2db:Version_0.1.1e, poe2db:Citaqualotls_Thesis «Citaqualotl's Thesis», tier 2, crawl 2026-11-23
- conf: single-source per statement
- notes: Which tier 1-4 cores drop from which source is not stated anywhere in the corpus.


<!-- merged from kb/items/soul-core-idol-effects-2.md -->
Part title: Soul core effects 2 (Jiquani, Atziri), animal idols (drop lvl 35), corrupted idols

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-item pages and Soul Core / Idol / Ancient Augment index pages, tier 2.

## Jiquani's Soul Core of X (13 cores, +1 skill level)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
All limit 1, req lvl 50, drop level 65, socket into a Weapon. Each gives +1 to level of all skill gems of one tag:
| Core of | Effect |
|---|---|
| Abundance | Weapon: +1 to Level of all Plant Skill Gems |
| Automation | Weapon: +1 to Level of all Totem Skill Gems |
| Malediction | Weapon: +1 to Level of all Curse Skills |
| Munitions | Weapon: +1 to Level of all Grenade Skill Gems |
| Quaking | Weapon: +1 to Level of all Slam Skill Gems |
| Radiance | Weapon: +1 to Level of all Herald Skill Gems |
| Rallying | Weapon: +1 to Level of all Warcry Skill Gems |
| Rippling | Weapon: +1 to Level of all Nova Skill Gems |
| Severing | Weapon: +1 to Level of all Strike Skill Gems |
| Snares | Weapon: +1 to Level of all Hazard Skill Gems |
| Squalls | Weapon: +1 to Level of all Wind Skill Gems |
| Targeting | Weapon: +1 to Level of all Mark Skills |
| Thundering | Weapon: +1 to Level of all Storm Skill Gems |
- src: poe2db:Jiquanis_Soul_Core_of_Abundance and the rest at https://poe2db.tw/us/Jiquanis_Soul_Core_of_<Name>, tier 2, crawl 2026-11-23
- notes: Version_0.5.5 notes mention Jiquani's Soul Core of Rallying (Rally page).


## Soul core tier 4: Atziri's cores (4, socket-bound)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Limit 1, req lvl 50, drop level 65; socket-bound (permanent):
| Core | Slot effect |
|---|---|
| Atziri's Soul Core of Alacrity | SB Gloves: 1% increased Skill Speed for each Corrupted Item Equipped, Corrupting will always result in change |
| Atziri's Soul Core of Devotion | SB Helmets: 1% increased Spirit for each Corrupted Item Equipped, Corrupting will always result in change |
| Atziri's Soul Core of Inoculation | SB Boots: +2% to Chaos Resistance for each Corrupted Item Equipped, Corrupting will always result in change |
| Atziri's Soul Core of Vitality | SB Body Armours: 1% increased Maximum Life for each Corrupted Item Equipped, Corrupting will always result in change |
- src: poe2db:Atziris_Soul_Core_of_Alacrity, poe2db:Atziris_Soul_Core_of_Devotion, poe2db:Atziris_Soul_Core_of_Inoculation, poe2db:Atziris_Soul_Core_of_Vitality, tier 2, crawl 2026-11-23
- notes: Socket-bound augments cannot be removed or replaced; Orb of Extraction returns non-socket-bound augments only ([Socket-bound Augments](https://poe2db.tw/us/Socket-bound_Augments)).


## Animal idols, drop level 35 (9)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
No level requirement shown.
| Idol | Type | Req/drop | Limit | Slot effects | Bonded | Socket into |
|---|---|---|---|---|---|---|
| Bear Idol | wild | -/35 | - | Helmets: 10% increased Area of Effect ; Sceptres: Allies in your Presence deal 12 to 18 added Attack Physical Damage | Helmets: 12% increased Reservation Efficiency of Companion Skills ; Sceptres: 40% increased Attack Damage while Shapeshifted | a Helmet or Sceptre |
| Boar Idol | wild | -/35 | - | Gloves: Gain 1 Rage on Melee Hit ; Sceptres: Allies in your Presence Regenerate 0.5% of your Maximum Life per second | Gloves: 25% increased Warcry Cooldown Recovery Rate ; Sceptres: 25% increased Life Regeneration rate while Shapeshifted | Gloves or a Sceptre |
| Cat Idol | vivid | -/35 | - | Gloves: 25% increased Accuracy Rating ; Sceptres: Allies in your Presence have 14% increased Critical Hit Chance | Gloves: 30% increased Charm Charges gained ; Sceptres: 25% increased Critical Hit Chance while Shapeshifted | Gloves or a Sceptre |
| Owl Idol | primal | -/35 | - | Foci: 12% increased Cooldown Recovery Rate ; Sceptres: Allies in your Presence have 10% increased Cast Speed | Foci: 20% increased effect of Archon Buffs on you ; Sceptres: 10% increased Skill Speed while Shapeshifted | a Focus or a Sceptre |
| Ox Idol | wild | -/35 | - | Shields and Bucklers: 15% increased Block chance ; Sceptres: Allies in your Presence have +12% to all Elemental Resistances | Shields and Bucklers: 15% chance for Damage of Enemies Hitting you to be Unlucky ; Sceptres: +20% of Armour also applies to Elemental Damage while Shapeshifted | a Shield, a Buckler or a Sceptre |
| Primate Idol | primal | -/35 | - | Helmets: Minions have 15% increased maximum Life ; Sceptres: Allies in your Presence deal 40% increased Damage | Helmets: Remnants can be collected from 30% further away ; Sceptres: 40% increased Damage while Shapeshifted | a Helmet or Sceptre |
| Snake Idol | primal | -/35 | - | Gloves: 8% increased Curse Magnitudes ; Sceptres: Allies in your Presence have 10% increased Attack Speed | Gloves: Remnants you create have 15% increased effect ; Sceptres: 10% increased Skill Speed while Shapeshifted | Gloves or a Sceptre |
| Stag Idol | vivid | -/35 | 1 | Helmets: Projectiles have 15% chance to Fork ; Sceptres: Allies in your Presence deal 1 to 40 added Attack Lightning Damage | Helmets: Projectiles have 25% chance for an additional Projectile when Forking ; Sceptres: 40% increased Attack Damage while Shapeshifted | a Helmet or Sceptre |
| Wolf Idol | vivid | -/35 | - | Gloves: 15% increased Magnitude of Bleeding you inflict ; Sceptres: Allies in your Presence have 20% increased Critical Damage Bonus | Gloves: 25% reduced Magnitude of Bleeding on You ; Sceptres: 25% increased Critical Hit Chance while Shapeshifted | Gloves or a Sceptre |
- src: poe2db:Bear_Idol, poe2db:Boar_Idol, poe2db:Cat_Idol and the rest at https://poe2db.tw/us/<Name>_Idol; poe2db:Idol, tier 2, crawl 2026-11-23
- notes: Idols are Azmeri-made Augments. Bonded lines need Shaman Wisdom of the Maji or a Fox Idol on the body armour (see [[items/rune-effects]]). Idolatry (Spirit Walker, Huntress) scales with idols equipped ([Idolatry](https://poe2db.tw/us/Idolatry)). Type = wild/vivid/primal/sacred tag from the item.


## Corrupted idols (3)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Req lvl 50, drop level 65, limit 1.
| Idol | Type | Req/drop | Limit | Slot effects | Bonded | Socket into |
|---|---|---|---|---|---|---|
| Idol of the Martyr | corrupted | 50/65 | 1 | Martial Weapon, ; Wand or Staff: 25% reduced Spirit, Meta Skills gain 40% increased Energy ; Sceptres: 40% reduced Presence Area of Effect, Aura Skills have 25% increased Magnitudes | Martial Weapon, ; Wand or Staff: Invocated skills have 25% increased Maximum Energy, Meta Skills have 25% reduced Reservation Efficiency ; Sceptres: Allies in your Presence Regenerate 3% of your Maximum Life per second, 25% reduced Life Regeneration rate | a Weapon |
| Idol of the Pharisee | corrupted | 50/65 | 1 | Martial Weapon, ; Wand or Staff: 30% reduced maximum Mana, Gain 2% of Damage as Extra Physical Damage per ten percent missing Mana ; Sceptres: 30% reduced Mana Cost Efficiency of Command Skills, Minions deal 60% increased Damage with Command Skills | Martial Weapon, ; Wand or Staff: 30% reduced Mana Cost Efficiency, 12% increased Skill Speed while on Low Mana ; Sceptres: 25% reduced Reservation Efficiency of Minion Skills, Temporary Minion Skills have +2 to Limit of Minions summoned | a Weapon |
| Idol of the Sycophant | corrupted | 50/65 | 1 | Martial Weapon, ; Wand or Staff: -20% to all Elemental Resistances, Gain 20% of Damage as Extra Damage of a random Element ; Sceptres: Companions in your Presence have -20% to all Elemental Resistances, Companions in your Presence Gain 20% of Damage as Extra Damage of a random Element | Martial Weapon, ; Wand or Staff: -20% to Chaos Resistance, Gain 20% of Damage as Extra Chaos Damage ; Sceptres: Allies in your Presence Gain 20% of Damage as Extra Chaos Damage, Companions in your Presence have -20% to Chaos Resistance | a Weapon |
- src: poe2db:Idol_of_the_Martyr, poe2db:Idol_of_the_Pharisee, poe2db:Idol_of_the_Sycophant, tier 2, crawl 2026-11-23
- notes: Ritual page: the boss The Queen in the Mists (needs a specific Atlas node) can drop three new corrupted idols ([Ritual](https://poe2db.tw/us/Ritual)); "Those Who Hear" gives Possessed monsters 50% increased chance to drop Idols (Level 75+ areas, requires completing the Burning Monolith, on the Idol page). Version_0.3.1: Idol of Estazunti is a map fragment (Sealed Vault), not an augment.


<!-- merged from kb/items/soul-core-idol-effects-3.md -->
Part title: Idol effects (named and rare animal idols, drop lvl 65)

- Status: done for item list; drop sources partial
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-item pages and Soul Core / Idol / Ancient Augment index pages, tier 2.

## Named and rare animal idols, drop level 65 (19)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Req lvl 50 for named idols; Fox and Rabbit (sacred) show no requirement.
| Idol | Type | Req/drop | Limit | Slot effects | Bonded | Socket into |
|---|---|---|---|---|---|---|
| Fox Idol | sacred | -/65 | 1 | Body Armours: Idols socketed in this item gain the benefits of their Bonded modifiers, display additional socketable mods for idols [1] ; Sceptres: 50% increased Presence Area of Effect | Body Armours: +5% to Quality of all Skills ; Sceptres: Minions have 30% increased Area of Effect | a Body Armour or Sceptre |
| Hawk Idol | primal | 50/65 | 1 | Body Armours: 10% increased Deflection Rating ; Sceptres: Companions have 12% increased Attack Speed | Body Armours: +12% to Cold Resistance ; Sceptres: 8% increased Attack Speed while your Companion is in your Presence | a Body Armour or Sceptre |
| Idol of Alira | primal | 50/65 | 1 | Helmets: 15% chance when you gain a Power Charge to gain an additional Power Charge ; Sceptres: If you would gain a Power Charge, Allies in your Presence gain that Charge instead | Helmets: +1 to Maximum Power Charges ; Sceptres: 40% increased maximum Energy Shield if you've consumed a Power Charge Recently | a Helmet or Sceptre |
| Idol of Eeshta | primal | 50/65 | 1 | Helmets: 15% increased Cost Efficiency ; Sceptres: 15% increased Mana Recovery rate while your Companion is in your Presence | Helmets: Meta Skills have 15% increased Reservation Efficiency ; Sceptres: 8% increased Life Recovery Rate while your Companion is in your Presence | a Helmet or Sceptre |
| Idol of Egrin | vivid | 50/65 | 1 | Helmets: Enemies you Curse take 6% increased Damage ; Sceptres: 20% increased Curse Duration | Helmets: 20% increased Area of Effect of Curses ; Sceptres: Curse zones erupt after 20% reduced delay | a Helmet or Sceptre |
| Idol of Eramir | sacred | 50/65 | 1 | Body Armours: Skills have 10% chance to not remove Charges but still count as consuming them ; Sceptres: Allies in your Presence share Charges with you | Body Armours: 15% chance for Charms you use to not consume Charges ; Sceptres: 25% increased Endurance, Frenzy and Power Charge Duration | a Body Armour or Sceptre |
| Idol of Greust | primal | 50/65 | 1 | Shields: +25% of Armour also applies to Elemental Damage ; Bucklers: Gain Deflection Rating equal to 20% of Evasion Rating ; Sceptres: Companions deal 10% more Damage for each different type of dead Companion you have | Shields: 12% increased Damage for each type of Elemental Ailment on Enemy ; Bucklers: 12% increased Damage for each type of Elemental Ailment on Enemy ; Sceptres: Recover 3% of maximum Life when one of your Minions is Revived | a Shield, a Buckler or a Sceptre |
| Idol of Grold | wild | 50/65 | 1 | Boots: 50% increased total Power counted by Warcries ; Sceptres: 15% increased Damage per each different Companion in your Presence | Boots: 30% increased Glory generation ; Sceptres: 15% increased Reservation Efficiency of Companion Skills | Gloves or a Sceptre |
| Idol of Kraityn | vivid | 50/65 | 1 | Gloves: 15% chance when you gain a Frenzy Charge to gain an additional Frenzy Charge ; Sceptres: If you would gain a Frenzy Charge, Allies in your Presence gain that Charge instead | Gloves: +1 to Maximum Frenzy Charges ; Sceptres: 40% increased Evasion Rating if you've consumed a Frenzy Charge Recently | Gloves or a Sceptre |
| Idol of Maxarius | vivid | 50/65 | 1 | Body Armours: +1 Charm Slots ; Sceptres: Flasks gain 0.2 charges per Second | Body Armours: Storm Skills have +1 to Limit ; Sceptres: 20% increased Life and Mana Recovery from Flasks | a Body Armour or Sceptre |
| Idol of Oak | wild | 50/65 | 1 | Boots: 15% chance when you gain an Endurance Charge to gain an additional Endurance Charge ; Sceptres: If you would gain an Endurance Charge, Allies in your Presence gain that Charge instead | Boots: +1 to Maximum Endurance Charges ; Sceptres: 40% increased Armour if you've consumed an Endurance Charge Recently | Boots or a Sceptre |
| Idol of Ralakesh | primal | 50/65 | 1 | Helmets: 8% increased Reservation Efficiency of Minion Skills ; Sceptres: 40% increased Armour, Evasion and Energy Shield while your Companion is in your Presence | Helmets: Minions Revive 8% faster ; Sceptres: Companions have 25% increased maximum Life | a Helmet or Sceptre |
| Idol of Silk | wild | 50/65 | 1 | Shields: 15% increased Block chance while your Companion is in your Presence ; Bucklers: companions gain onslaught when you parry [1] ; Sceptres: Companions in your Presence gain 1 Rage on hit | Shields: +3% to maximum Block chance ; Bucklers: 30% increased Parry Range ; Sceptres: Companions have 30% increased Area of Effect | a Shield, Buckler or a Sceptre |
| Idol of Sirrius | vivid | 50/65 | 1 | Gloves: 8% increased Attack Speed ; Sceptres: Allies in your Presence have 8% increased Movement Speed | Gloves: 20% reduced Slowing Potency of Debuffs on You ; Sceptres: 4% increased Movement Speed | Gloves or a Sceptre |
| Idol of Thruldana | primal | 50/65 | 1 | Martial Weapon: 25% reduced Poison Duration, Targets can be affected by +1 of your Poisons at the same time ; Sceptres: Allies in your Presence deal 13 to 27 added Attack Chaos Damage | Martial Weapon: Gain 13% of Physical Damage as extra Chaos Damage ; Sceptres: 15% increased Withered Magnitude | a Martial Weapon or a Sceptre |
| Idol of Yeena | sacred | 50/65 | 1 | Boots: 30% increased Skill Effect Duration with Plant Skills ; Sceptres: Plants have a 25% chance to immediately Overgrow when they enter your Presence for the first time | Boots: Plants have a 25% chance to immediately Overgrow when they enter your Presence for the first time ; Sceptres: 30% increased Skill Effect Duration with Plant Skills | Boots or a Sceptre |
| Panther Idol | wild | 50/65 | 1 | Body Armours: +10% of Armour also applies to Chaos Damage ; Sceptres: Minions have +20% to Chaos Resistance | Body Armours: +8% to Chaos Resistance ; Sceptres: Minions have 20% additional Physical Damage Reduction | a Body Armour or Sceptre |
| Rabbit Idol | sacred | -/65 | 1 | Body Armours: 12% increased Rarity of Items found ; Sceptres: 15% increased Spirit | Body Armours: 10% increased Quantity of Gold Dropped by Slain Enemies ; Sceptres: Minions have 30% increased Cooldown Recovery Rate for Command Skills | a Body Armour or Sceptre |
| Stoat Idol | vivid | 50/65 | 1 | Body Armours: 5% of Damage taken bypasses Energy Shield ; Sceptres: Companions have 25% increased maximum Life | Body Armours: +12% to Lightning Resistance ; Sceptres: 25% increased Damage while your Companion is in your Presence | a Body Armour or Sceptre |
- src: poe2db:Fox_Idol, poe2db:Hawk_Idol, poe2db:Idol_of_Alira and the rest at https://poe2db.tw/us/<Page>, tier 2, crawl 2026-11-23
- notes: Fox Idol: idols socketed in the same body armour gain their Bonded modifiers (display additional socketable mods for idols).


<!-- merged from kb/items/soul-core-idol-effects-4.md -->
Part title: Ancient Augments (Gaze, Thesis, Emergent, Carved, Raven-Touched Shard)

- Status: done for item list; drop sources partial
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-item pages and Soul Core / Idol / Ancient Augment index pages, tier 2.

## Ancient Augments: Abyssal Eye "Gaze" (4) and Vaal "Thesis" soul cores (4)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Ancient Augments have strong single effects; only one Ancient Augment may be socketed at a time. All: limit 1, req lvl 60, drop level 65, 1500 gold on Currency Exchange, usable in Weapon or Armour sockets; effects differ per slot.
| Augment | Effect (slot) | Bonded |
|---|---|---|
| Amanamu's Gaze | Helmets: Remove a Damaging Ailment when you use a Command Skill ; Body Armours: +2 to Armour per 1 Spirit ; Boots: 1% increased Movement Speed per 15 Spirit, up to a maximum of 40% Other Modifiers to Movement Speed except for Sprinting do not apply | - |
| Tecrod's Gaze | Body Armours: Regenerate 1.5% of maximum Life per second ; Gloves: 25% increased Life Cost Efficiency ; Boots: 10% increased Movement Speed when on Low Life | - |
| Kurgal's Gaze | Helmets: Increases and Reductions to Life Regeneration Rate also apply to Mana Regeneration Rate ; Gloves: 40% increased effect of Arcane Surge on you ; Boots: 15% increased Mana Cost Efficiency if you haven't Dodge Rolled Recently | - |
| Ulaman's Gaze | Helmets: +1 to Accuracy Rating per 1 Item Evasion Rating on Equipped Helmet ; Gloves: Critical Hit chance is Lucky against Parried enemies ; Body Armours: Prevent +3% of Damage from Deflected Hits | - |
| Guatelitzi's Thesis | Helmets: Gain Armour equal to 35% of Life Lost from Hits in the past 8 seconds ; Body Armours: 10% of Physical Damage prevented Recouped as Life ; Boots: Lose 5% of maximum Life per second while Sprinting, 25% increased Movement Speed while Sprinting | - |
| Citaqualotl's Thesis | Body Armours: You Recoup 50% of Damage taken by your Offerings as Life ; Gloves: One of your Persistent Minions revives when an Offering expires ; Boots: Sacrifice 10% of maximum Life to gain that much Guard when you Dodge Roll | - |
| Jiquani's Thesis | Helmets: +1 to maximum Mana per 3 Item Armour on Equipped Helmet ; Gloves: Energy Shield Recharge starts after spending a total of 2000 Mana, no more than once every 2 seconds ; Boots: Increases and Reductions to Movement Speed also apply to Energy Shield Recharge Rate | - |
| Quipolatl's Thesis | Helmets: A random Skill that requires Glory generates 50% of its maximum Glory when your Marks Activate ; Gloves: Your Energy Shield Recharge starts when your Minions are Reformed ; Body Armours: +75% of Armour also applies to Chaos Damage while on full Energy Shield | - |
- src: poe2db:Ancient_Augment, poe2db:Amanamus_Gaze «Amanamu's Gaze», poe2db:Jiquanis_Thesis «Jiquani's Thesis», tier 2, crawl 2026-11-23
- notes: Thesis pages say they have drop restrictions and can sometimes be obtained by modifying a soul core with a Core Destabiliser (Citaqualotl/Guatelitzi/Jiquani/Quipolatl pages). Gaze drop source not stated. Gazes have no Bonded line on the index.


## Ancient Augments: Emergent (4) and Carved (4) runes
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Same limits as above (one Ancient Augment at a time, req 60, drop 65, 1500 gold).
| Augment | Effect (slot) | Bonded |
|---|---|---|
| Emergent Vigour | Helmets: +1 to maximum Life per 8 Armour on Equipped Helmet ; Body Armours: Gain Maximum Energy Shield equal to 50% of total Strength Requirements of Equipped Armour Items ; Boots: Hits against you have no Critical Damage Bonus while on Consecrated Ground | Helmets: +20 to Spirit ; Body Armours: +20 to Strength ; Boots: 20% increased Effect of Consecrated Ground you create |
| Emergent Possibility | Body Armours: 15% of Chaos Damage from Hits taken as Damage of a random Element ; Gloves: Gain 1% of Damage as Extra Damage of a random Element per Rune Socketed in Equipped Items ; Boots: 50% increased Runic Ward Regeneration Rate while Sprinting | Body Armours: +13% to Chaos Resistance ; Gloves: 20% increased Elemental Damage ; Boots: 15% increased Runic Ward Cost Efficiency |
| Emergent Protection | Helmets: Gain 1 Endurance Charge on reaching Low Life, only once every 2 seconds ; Gloves: Banners also grant 2% of Life Regenerated per second to affected targets ; Boots: When you stop Sprinting, gain Guard equal to 4% of maximum Life per second spent Sprinting, up to a maximum of 20%, for 4 seconds | Helmets: 40% increased Endurance Charge Duration ; Gloves: Regenerate 0.5% of maximum Life per second ; Boots: 20% increased Guard gained |
| Emergent Instinct | Helmets: Targets that are Blinded, Maimed, and Bleeding cannot Evade your Hits ; Gloves: Regenerate 5% of maximum Life per Second if you have used a Command Skill Recently ; Body Armours: Thorns Damage is Lucky against targets with Fully Broken Armour | Helmets: 30% increased Immobilisation buildup ; Gloves: 20% increased Life Regeneration rate ; Body Armours: 30% increased Thorns damage |
| Carved Cunning | Helmets: Enemies which are on Full Life cannot Evade your Hits ; Body Armours: Prevent +5% of Damage from Deflected Hits if you've Deflected no Hits Recently ; Boots: Gain Onslaught for 4 seconds when your Marks Activate | Helmets: 30% increased Accuracy Rating ; Body Armours: 8% increased Deflection Rating ; Boots: Buffs on you expire 10% slower |
| Carved Majesty | Body Armours: +3 to Spirit per Idol socketed in your Equipment ; Gloves: Companions gain Onslaught for 4 seconds on Hitting your Marked targets ; Boots: 1% increased Movement Speed while Sprinting per Persistent Minion | Body Armours: 5% increased Spirit ; Gloves: Companions deal 30% increased Damage ; Boots: Minions have 12% increased maximum Life |
| Carved Mischief | Helmets: Gain Guard equal to 10% of maximum Life for 4 seconds on taking Savage Hit ; Gloves: +5% to maximum Block chance if you've Blocked with a raised Shield Recently ; Body Armours: 200% increased Stun Threshold if you've been Stunned Recently | Helmets: Buffs on you expire 10% slower ; Gloves: 20% increased Block chance ; Body Armours: 25% increased Stun Threshold |
| Carved Tenacity | Helmets: Enemies have no Critical Damage Bonus for 4 seconds after you Blind them ; Gloves: Enemies you Critically Hit get 100% reduced Life Regeneration Rate for 4 seconds ; Boots: Your speed is Unaffected by Slows while Sprinting | Helmets: 20% increased Blind Effect ; Gloves: 15% increased Critical Hit Chance ; Boots: 8% increased Movement Speed while Sprinting |
- src: poe2db:Ancient_Augment, poe2db:Emergent_Vigour, poe2db:Carved_Cunning, tier 2, crawl 2026-11-23
- notes: Tagged as runes on the item pages. Carved Majesty counts idols in your equipment. Drop source not stated.


## Raven-Touched Shard
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Socket-bound augment for Helmets only: grants the Raven-Touched modifier set (effect text on the item is just 'Raven-Touched'). Limit 1, req lvl 60, drop level 65, 1500 gold on Currency Exchange; cannot be retrieved or replaced once socketed.
- src: poe2db:Raven-Touched_Shard, tier 2, crawl 2026-11-23
- notes: What the Raven-Touched modifier does is not described on the page.
