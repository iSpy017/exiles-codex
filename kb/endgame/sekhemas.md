---
title: Trial of the Sekhemas (0.5.x baseline)
status: partial
tracker_topic: "Trial of the Sekhemas"
tracker_note: "partial (0.5.x; + Baryas, rooms, relic slots/mods, Reliquary keys; Honour-loss % and Test Barya sources missing)"
merged_from: [sekhemas.md, sekhemas-2.md]
---

Status: partial — written 2026-11-23 for the 0.5.5 kb-test build. Endgame docs are otherwise deferred to the 1.0 notes (David, 2026-11-17); treat this as the 0.5 baseline and re-check at 1.0.
Source unless noted: poe2db:Trial_of_the_Sekhemas, poe2db:Honour, poe2db:Honour_Resistance, poe2db:Keywords, tier 2, crawl 2026-11-23 ([[notes/tools/poe2db-corpus]]). Single-source (game-data derived).
Profit view (creator, tier 5) → [[strategy/sekhemas-currency-farm]]. Ascendancy points and Barya levels → [[classes/ascendancy-trials]].

## Honour
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
Honour is a resource used only inside the trial. A percentage of the damage you take from enemies is also taken from Honour; at zero Honour the trial fails. Starting and max Honour = max Life + max ES + max Runic Ward (+ max Mana if you have Mind Over Matter). Honour Resistance = you lose that much less Honour; capped at 75% by default, never above 90%.
- conf: single-source (game keyword text)
- notes: the % of damage that becomes Honour loss is not stated → gap. [INFERRED] build implications: (1) avoiding hits matters more than recovering from them; (2) ES counts toward Honour like life, so an ES build has a bigger Honour pool; (3) mana only counts with Mind Over Matter.


## Floors and bosses
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src,vol
Four floors: Test of Strength (boss Rattlecage, the Earthbreaker), Test of Will (Terracotta Sentinels), Test of Cunning (Ashar, the Sand Mother), Test of Time (Zarokh, the Temporal). Higher-level Baryas unlock more floors.
- Room types include timed (Hourglass), Ritual, Chalice, Escape, Gauntlet, Collapsing Cavern; reward rooms: Sacred Water fountains, Pledges, Honour shrines (Halani: restore + Sacred Water; Ahkeli: big restore + Affliction; Orbala: restore + Boon; Tabana: restore), Merchant, Bronze/Silver keys.
- A 4-floor run = 32 rooms ([[classes/ascendancy-trials]], poe2wiki).


## Afflictions (debuffs) that hit an ES caster hardest
- Corrosive Concoction (major): no armour, evasion or ES. Shattered Shield (minor): 50% less ES. Orb of Negation (major): non-unique relics have no effect. Worn Sandals (minor): 30% reduced movement speed if hit recently. Fiendish Wings (minor): monsters 25% increased attack/cast/move speed, can't be slowed below base.
- [INFERRED] Corrosive Concoction and Shattered Shield also cut max Honour for an ES build (Honour = life + ES) — check whether max Honour updates mid-run.

## Useful Boons / Pledges
- Lustrous Lacquer: 50% more armour/evasion/ES. Orbala Statuette: 25% more max Honour. Black Pearl: traps deal 50% reduced damage. Adrenaline Vial: restore Honour on entering a boss room.
- Pledge to the Powerful: 50% less Honour lost in boss rooms, 100% more in non-boss rooms. Pledge to the Guileful: open 1 reward chest per room without a key (take phys damage). Pledge to the Deserted: 50% cheaper merchant, no Sacred Water from monsters.

## Unique relics (Zarokh drops)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src,vol
- The Last Flame (Incense): Zarokh drops Temporalis; damage taken can't be Absorbed; max Honour is 1; only Trials level 80+.
- The Desperate Alliance (Vase): Zarokh drops Against the Darkness; **Zarokh deals 100% more damage and takes 75% less damage**.
- The Burden of Leadership (Tapestry): Zarokh drops Sekhema's Resolve; rooms are unknown on the Trial Map.
- The Peacemaker's Draught (Amphora): Zarokh drops 1 additional Barya; your armour, evasion and ES are zero.
- The Changing Seasons (Seal): Zarokh drops Sandstorm Visage; can't restore Honour.
- All are destroyed when applied.
- notes: Desperate Alliance = 4× Zarokh's effective life (75% less damage taken) and double his damage → the Against the Darkness farm needs much more DPS and defence than a plain run [INFERRED arithmetic]. Peacemaker's Draught zeroes ES — a pure ES build can't use it.


## Relic inventory
- 12 slots, unlocked by completing floors (Strength, Will, Cunning, Time).

## Zarokh, the Temporal
- Life 750% of base, 7% ES from life; page level 22 = 2,288 life before rarity; elemental res 15% each on the page (PoB spectre data: 0%) → kb/04-conflicts.md. Effective life at a given Barya level → [[mechanics/monster-life]].

## Unique rewards (names)
- Temporalis (body armour), Sandstorm Visage (helmet), Sekhema's Resolve / Safrin's Resolve (rings), Against the Darkness (Time-Lost Diamond), Grand Spectrum (Ruby/Emerald/Sapphire). Mods on PoE2DB page; prices → [[strategy/sekhemas-currency-farm]] (tier 5, undated).

<!-- merged from kb/endgame/sekhemas-2.md -->
Part title: Trial of the Sekhemas — part 2 (Baryas, rooms, relics, keys)

Status: partial. Companion to [[endgame/sekhemas]] (Honour, floors, afflictions, boons, pledges, unique relics, Zarokh). Missing: where the four Test Baryas drop (source not in corpus), Djinn Barya tablet/atlas sources beyond the lines below, full relic mod lists for non-Urn bases.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked for 1.0.

## Barya items (the entry coins)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Entry items are class "Trial Coins": Djinn Barya (drop level 24), plus Test of Strength, Will, Cunning and Time Barya (each drop level 65, internal ids SanctumFloor1 to 4). All are used at the Relic Altar inside the Trial; right-clicking shows the Trials in progress. Test Baryas are tagged not for sale. Balbala's Barya is the campaign quest item.
- src: poe2db:Djinn_Barya, poe2db:Test_of_Strength_Barya, poe2db:Trial_Coins, tier 2, crawl 2026-11-23
- conf: confirmed (item pages agree)
- notes: [INFERRED] each Test Barya opens the floor of the same name (the floor names and ids match); no page states it. Tag atlas-dependent.


## Trial count and ascension points by Barya
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
A PoE2DB ascendancy page lists the ladder: Balbala's Barya (1 floor, area level 22), Djinn Barya for 2 floors (level 38), 3 floors (level 60), 4 floors (level 80). Clearing floor 1/2/3/4 gives 2/4/6/8 Ascension points in total. The page text also says the third trial can be done as a skip for 6 points. Elzarah, the Cobra Lord (Sel Khari Sanctuary) drops a one-time Djinn Barya for the third set of points (added 0.3.1, also for characters who already killed her).
- src: poe2db:Ascendancy_class lines 2473-2523, poe2db:Version_0.3.1 line 164, tier 2, crawl 2026-11-23
- conf: single-source for the ladder; confirmed for the Elzarah drop (2 pages)
- notes: the ascendancy page is community-edited wiki text; wording is rough. Balbala, the Traitor drops Balbala's Barya in Act 2 (quest reward also lists an Urn Relic).


## Where Djinn Baryas come from in endgame
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Endgame list of Trial of the Sekhemas rewards: Jewels, Djinn Barya, Relics. Map boss modifier "Sekhema's Student" makes the map boss drop a Djinn Barya. Strongbox suffixes at level 24 add 1 or 3 extra Djinn Baryas.
- src: poe2db:EndGame lines 336-340, poe2db:Maps line 1563, poe2db:Strongbox lines 1048 and 1064, tier 2, crawl 2026-11-23
- conf: single-source each
- notes: atlas-dependent.


## Campaign vs endgame version
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The campaign instance is Act 2 data (id Sanctum_1 to Sanctum_4, area level 22, entrance via Trial of Ascendancy at The Ardura Caravan). Endgame floors are gated by the Test Baryas (drop level 65). From 0.5.5 the Trial has inherent bonuses starting at area level 65 (rare and magic monster chance and pack size, extra rare mods, boss item quality and quantity, Exceptional item drops) because atlas passive bonuses do not apply inside the Trial.
- src: poe2db:Trial_of_the_Sekhemas lines 1111-1145, poe2db:Version_0.5.5 line 153, tier 2, crawl 2026-11-23
- notes: atlas-dependent. Floor page names Terracotta Sentinels for Test of Will; the Act 2 area data names Rafiq of the Frozen Spring and Hadi of the Flaming River for floor 2. Not reconciled (see report).


## Floor room sets (reward rooms and special rooms)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Each of the four floors can hold five trial types (Hourglass, Chalice, Escape, Gauntlet, Ritual) plus: Fountain (large or standard Sacred Water), Pledge to Kochai, five Honour shrines (Halani: restore Honour and gain Sacred Water; Ahkeli: large restore plus an Affliction; Orbala: restore plus a Boon; Galai: wind blessings; Tabana: restore), Merchant, Bronze/Silver/Gold Key rooms and Bronze/Silver/Golden Cache rooms. Floor-unique rooms: Collapsing Cavern (Strength), Ceremonial Chamber (Will), Sand Pit (Cunning), Outside of Time (Time). Keys drop from rooms or monsters; after each floor a set of caches opens with the matching key.
- src: poe2db:Trial_of_the_Sekhemas lines 1980-2208, poe2db:Trial_of_the_Sekhema_Keys, tier 2, crawl 2026-11-23
- conf: confirmed (2 pages)
- notes: Relic Locker added to every end-of-floor reward room in 0.4.0. Reforging Bench at the Trial entrance (0.5.0). Balbala has an Identify Items option (0.5.5c). Pledge effects are in the existing doc.


## Relic slots, shapes and unlocks
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The relic inventory has 12 listed cells that unlock 3 per floor: Cunning unlocks 3, Strength 3, Will 3, Time 3 (cells given by coordinates on the page). Relic bases and shapes (width x height): Urn 1x2, Amphora 1x3, Vase 1x4, Seal 2x1, Coffer 2x2, Tapestry 3x1, Incense 4x1. Mod pools: Urn 58 mods, Amphora 43, Vase 38, Seal 58, Coffer 38, Tapestry 43, Incense 38. Unique relics are consumed when applied to a Trial.
- src: poe2db:Trial_of_the_Sekhemas lines 2209-2222, poe2db:Urn_Relic line 6, tier 2, crawl 2026-11-23
- notes: [INFERRED] the unlock is by clearing that floor's test, from the "Complete the Test of X" labels. Shapes read from the base ids (SanctumRelic1x2 etc.); Vase/Seal/Coffer/Tapestry/Incense pages show the same pattern.


## Relic mod highlights (Urn Relic, top tiers)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Top-tier ranges and required item levels on the Urn Relic: max Life 21-25% (level 76); max Honour 25-30% (76); Honour restored 25-29% (80); Sacred Water at start 50-59 (76); Honour Resistance +20-22% (76); Movement Speed 7-10% (78); Armour, Evasion and ES 50-70% (75); relic quantity 16-20% (80); key quantity 21-25% (75); reduced Slowing Potency 16-20% (76); reduced enemy crit damage bonus 20-25% (76); traps deal 8-10% reduced damage (78); double Sacred Water from monsters up to 11-15% (70) and from fountains up to 11-15% (70); Dodge Roll +0.5-0.7 metres (70).
- src: poe2db:Urn_Relic lines 90-143, tier 2, crawl 2026-11-23
- notes: 0.4.0 cut Acrobatic trap-damage reduction to 5-7% (previously 12-15%) and removed Light-footed ([PoE2DB Version_0.4.0](https://poe2db.tw/us/Version_0.4.0) lines 580-582). The Fragment Stash Tab holds Baryas (Version_0.5.0 line 432). Mod weights are not in game files. Honour Resistance is capped 75% by default (existing doc).


## Zarokh Reliquary Keys
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Zarokh's Reliquary Key (generic, drop level 35, single use) opens a Reliquary portal at The Reliquary Vault (area level 65). Specific keys name the unique they yield: Against the Darkness, Blessed Bonds, Sandstorm Visage, Sekhema's Resolve, Temporalis.
- src: poe2db:Zarokhs_Reliquary_Key, poe2db:The_Reliquary_Vault, tier 2, crawl 2026-11-23
- conf: confirmed (5 key pages agree)
- notes: how the keys drop is not found in corpus. Blessed Bonds is not on the Trial page unique list.


## Zarokh hourglass failure (0.3.0)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Missing hourglasses in the Zarokh fight no longer fails the Trial. It damages Honour and Zarokh enters a secondary phase where hourglasses and the slow debuff persist at a slower rate. Escape Menu respawn returns you to the Trial entrance.
- src: poe2db:Version_0.3.0 lines 528 and 549, tier 2, crawl 2026-11-23
- v: 0.3.0 (patch note); current 0.5.x behaviour not re-checked
- notes: later notes may supersede it.
