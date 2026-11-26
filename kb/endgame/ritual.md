---
title: Ritual (endgame league mechanic)
status: partial
tracker_topic: "Ritual"
tracker_note: "partial (0.5.x; tribute/reroll costs not in corpus; recheck 1.0)"
defaults: v=0.5.x
---

Status: partial. Not found in corpus: Tribute per kill, Favour prices, defer cost formula, full unique reward pool, King phases.
Version: 0.5.x (PoE2DB crawl 2026-11-23). 1.0 not checked.
Sources: PoE2DB Ritual, boss, item and Version pages. Tag `atlas-dependent` marks atlas-reliant facts (no passive content recorded).

## Encounter loop
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Altars absorb monsters killed inside their circle. After enough kills you activate the altar and the same monsters are resurrected. Kill them again to earn Tribute. Tribute buys Favours (rewards) from the altar.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23
- conf: single-source (PoE2DB item/description text; wiki blurb on same page agrees)
- notes: Later rituals in an area also spawn earlier revived monsters, so late altars are the biggest fights.


## Reroll and defer
@ v=0.5.x vol=volatile conf=single-source date=2026-11-23
The Favour list can be rerolled for a Tribute cost. A Favour can be deferred: you pay part of its price and it comes back later. The exact costs are not in the corpus.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23 poe2db:Version_0.5.5.
- notes: Party members get their own limited reward list that cannot be rerolled (0.5.5). Free reroll mods exist on tablets/atlas (see tablet table).  Freythorn rituals never show deferred items (0.5.0), to avoid losing items on re-entry at a higher level.


## Reward screen (decision rows)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
| Situation | What you can buy / do | Source |
|---|---|---|
| Endgame (maps) altar | Reward screen offers only Uniques or Omens (0.5.0 note) | Ritual, Version_0.5.0 |
| Campaign altar | Levelling currency and gear; boss rituals carry forward; Uniques after the series (0.5.5) | Version_0.5.5 |
| Leftover Tribute | Can be offered to the King to obtain An Audience with the King (Crux key) | Ritual, Legacy_of_the_Maji |
Rewards in the endgame screen are Uniques or Omens. Omens are meta-crafting consumables, active while in inventory.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23; poe2db:Version_0.5.0, tier 2
- v: 0.5.x (rule from 0.5.0)
- conf: confirmed (Ritual page and Version_0.5.0 agree)
- notes: PoE2DB's Ritual page names Sinistral Exaltation, Greater Exaltation, Dextral Annulment and Ritual Precursor Tablet as unique rewards.


## Omen list (as linked from Ritual)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Omens linked from Ritual (stack 10, active while in inventory): Refreshment (refill flask/charm charges at Low Life), Resurgence (refill Life/Mana/ES at Low Life), Amelioration (prevent 75% XP loss on death), Whittling (Chaos Orb removes lowest-level mod), Sinistral/Dextral Erasure (Chaos Orb removes only prefixes/suffixes), Sinistral/Dextral Alchemy (max prefixes/suffixes), Sinistral/Dextral Coronation (Regal adds only prefix/suffix), Greater Exaltation (Exalted adds two mods), Sinistral/Dextral Exaltation (only prefix/suffix), Greater Annulment (removes two mods), Sinistral/Dextral Annulment (removes only prefixes/suffixes).
- src: poe2db:Ritual, tier 2, crawl 2026-11-23
- notes: Not stated to be the complete reward pool.


## Ritual types (encounter variants)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Type | Effect | Weight | Min level |
|---|---|---|---|
| Contaminated | Waves of blood through the site | 100 | 65 |
| Infested | Rat tornadoes | 100 | 65 |
| Tainted | Chaotic boils that explode when touched | 100 | 65 |
| Smothered | Chaotic plants that release explosive pods | 100 | 65 |
| Sapping | Elemental cloud: slows you, lowers your elemental resistances, raises monster resistances | 100 | 65 |
| Queen's | The Queen in the Mists guards the ritual | 44 | 65 |
Types roll by weight from level 65. Five types weight 100, Queen's 44; Prowling, Fractured, Plagued and Croaking have weight 0.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23
- notes: `atlas-dependent`: Queen's rituals need an atlas node. The Queen in the Mists boss (Life mult 250%, damage 250%) can drop three corrupted Idols (0.5.0).


## Tablets and map mods (atlas-dependent)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Source | Effect |
|---|---|
| Ritual Tablet (base) | Adds Ritual Altars to a Map; 10 uses |
| Freedom of Faith (unique tablet) | Favours cost (10-15)% increased Tribute; can reroll twice as many times |
| Suffix Sacrifice | Sacrificed monsters give (18-30)% increased Tribute |
| Dogma / Devotion / Appeal | Reroll / defer cost (20-30)% reduced; deferred Favours return (25-40)% sooner |
| Prayers / Occult | (1-3) extra rerolls / (3-6)% chance a reroll is free |
| Foundling / Cult / Omens | Revived monsters (35-70)% more likely Magic / (25-40)% Rare; Favours (35-70)% more likely Omens |
Rows are tablet craft mods and the unique tablet from the Ritual page misc-mod table.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23
- notes: Using more than one Ritual Tablet adds an extra altar if possible (0.5.5). Mysterious Altars quest rewards a Ritual Tablet (item level 70) and Ritualistic Book of Knowledge I ([Mysterious_Altars](https://poe2db.tw/us/Mysterious_Altars)).


## Quest chain to the pinnacle
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Legacy of the Maji (speak to Aoife) runs: complete all rituals in a map, travel to Caer Tarth, offer Tribute to get An Audience with the King, use it on the atlas to reveal the Crux of Nothingness, defeat the King, return with the Head of the King, place it on the Effigy, select 5 maps for the Rite of the Nameless, bring back the effigy pieces.
- src: poe2db:Legacy_of_the_Maji, tier 2, crawl 2026-11-23
- notes: The Head of the King is a key dropped by the King (0.5.0) used in Caer Tarth to start the Rite of the Nameless. The Rite is a sequence of 5 maps; monsters from earlier rituals and the map boss reappear in later maps, the unique boss of each map appears only in that map's final ritual, and each map after the first has extra modifiers. Each map awards one pinnacle key element (0.5.0). Effigy pieces: Tangled Torso, Mossy Arm, Frayed Cloth, Brittle Arm, Ragged Cloth.


## Keys and fragments
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Item | Role |
|---|---|
| An Audience with the King | Required to reveal the Crux of Nothingness |
| Head of the King | King kill proof; starts Rite |
| Call of the Shadows (stack 1/5) | Attach five to the effigy in Caer Tarth to perform the Rite |
Roles read from the item pages. Prices are not recorded here (PoE2DB panels name no league); see [PoE2DB economy](https://poe2db.tw/us/Economy).
- src: poe2db:An_Audience_With_The_King, poe2db:Call_of_the_Shadows, poe2db:Head_of_the_King, tier 2, crawl 2026-11-23
- notes: 0.5.1 notes call Call of the Shadows the tradeable fragment that starts the Bodach pinnacle fight.


## Bosses
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Boss | Area | Area level | Stats on PoE2DB |
|---|---|---|---|
| The King in the Mists | Crux of Nothingness (page text: Waystone Tier 14 or higher) | 80 | Arena table life 3,378,319 for both forms; armour 5,764 (form 1) and 7,925 (form 2); a third value 11,649 sits under the Energy Shield header column (equals 10% of the 116,494 base Life shown on the boss page); Life mult 375%, damage 188%, exp 300% |
| The Bodach | Caer Tarth (Rite pinnacle) | 79 | Arena table life 13,116,886; armour 7,945; Life mult 1820%, damage 320%, exp 400% |
The King has a second form (stat flag "monster has second form") and is a Tier-3 map boss in form 2 with rarity +4800, quantity +800 and 25% chance to drop a map key of at least the current tier. Caer Tarth mods: boss drops corrupted rare tablets, 5% rare socket currency chance, 10% special gem chance.
- src: poe2db:Crux_of_Nothingness, poe2db:The_King_in_the_Mists, poe2db:Caer_Tarth, poe2db:The_Bodach, tier 2, crawl 2026-11-23
- notes: Followers roam the Crux maze (0.5.3). Players cannot gain or lose experience there. Fight phases: not found in corpus.


## Unique drops tied to bosses
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Boss | Uniques (PoE2DB limit tag) |
|---|---|
| The King in the Mists | Beetlebite, From Nothing, Ingenuity, Pragmatism, The Burden of Shadows |
| The Bodach | Forgotten Warden, Liminal Coil, Periphery, Sylvan's Effigy, Vestige of Darkness |
| Ritual (unique tablet) | Freedom of Faith |
PoE2DB gives each unique a limit tag naming the boss. From Nothing (jewel, radius small 1000) also states it drops from the King at the Crux at Difficulty 4.
- src: poe2db:From_Nothing, poe2db:The_King_in_the_Mists, poe2db:The_Bodach, tier 2, crawl 2026-11-23
- notes: Each unique page also shows "Dropped by: The Market"; meaning not explained in corpus. Mod values: link the item pages.


## Farm decision notes
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
Value levers are Tribute gain, free or cheaper rerolls, Omen share of Favours and altar count per map; all depend on tablet/atlas setup.
- src: poe2db:Ritual, tier 2, crawl 2026-11-23
- conf: [INFERRED]: synthesis of the tablet mod table; no source ranks the levers.
- notes: Foretold Bounty (Rite maps) puts a named item in the first Favour list. `atlas-dependent`.
