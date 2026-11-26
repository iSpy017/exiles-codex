# Ritual (endgame league mechanic)

Status: partial. Not found in corpus: Tribute per kill, Favour prices, defer cost formula, full unique reward pool, King phases.
Version: 0.5.x (PoE2DB crawl 2026-11-23). 1.0 not checked.
Sources: PoE2DB Ritual, boss, item and Version pages. Tag `atlas-dependent` marks atlas-reliant facts (no passive content recorded).

## Encounter loop
- Claim: Altars absorb monsters killed inside their circle. After enough kills you activate the altar and the same monsters are resurrected. Kill them again to earn Tribute. Tribute buys Favours (rewards) from the altar.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: single-source (PoE2DB item/description text; wiki blurb on same page agrees)
- Notes: Later rituals in an area also spawn earlier revived monsters, so late altars are the biggest fights.

## Reroll and defer
- Claim: The Favour list can be rerolled for a Tribute cost. A Favour can be deferred: you pay part of its price and it comes back later. The exact costs are not in the corpus.
- Version: 0.5.x
- Volatility: volatile
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Party members get their own limited reward list that cannot be rerolled (0.5.5). Free reroll mods exist on tablets/atlas (see tablet table).  Freythorn rituals never show deferred items (0.5.0), to avoid losing items on re-entry at a higher level. Source: [PoE2DB Version_0.5.5](https://poe2db.tw/us/Version_0.5.5).

## Reward screen (decision rows)
| Situation | What you can buy / do | Source |
|---|---|---|
| Endgame (maps) altar | Reward screen offers only Uniques or Omens (0.5.0 note) | Ritual, Version_0.5.0 |
| Campaign altar | Levelling currency and gear; boss rituals carry forward; Uniques after the series (0.5.5) | Version_0.5.5 |
| Leftover Tribute | Can be offered to the King to obtain An Audience with the King (Crux key) | Ritual, Legacy_of_the_Maji |
- Claim: Rewards in the endgame screen are Uniques or Omens. Omens are meta-crafting consumables, active while in inventory.
- Version: 0.5.x (rule from 0.5.0)
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23; [PoE2DB Version_0.5.0](https://poe2db.tw/us/Version_0.5.0), tier 2
- Confidence: confirmed (Ritual page and Version_0.5.0 agree)
- Notes: PoE2DB's Ritual page names Sinistral Exaltation, Greater Exaltation, Dextral Annulment and Ritual Precursor Tablet as unique rewards.

## Omen list (as linked from Ritual)
- Claim: Omens linked from Ritual (stack 10, active while in inventory): Refreshment (refill flask/charm charges at Low Life), Resurgence (refill Life/Mana/ES at Low Life), Amelioration (prevent 75% XP loss on death), Whittling (Chaos Orb removes lowest-level mod), Sinistral/Dextral Erasure (Chaos Orb removes only prefixes/suffixes), Sinistral/Dextral Alchemy (max prefixes/suffixes), Sinistral/Dextral Coronation (Regal adds only prefix/suffix), Greater Exaltation (Exalted adds two mods), Sinistral/Dextral Exaltation (only prefix/suffix), Greater Annulment (removes two mods), Sinistral/Dextral Annulment (removes only prefixes/suffixes).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Not stated to be the complete reward pool.

## Ritual types (encounter variants)
| Type | Effect | Weight | Min level |
|---|---|---|---|
| Contaminated | Waves of blood through the site | 100 | 65 |
| Infested | Rat tornadoes | 100 | 65 |
| Tainted | Chaotic boils that explode when touched | 100 | 65 |
| Smothered | Chaotic plants that release explosive pods | 100 | 65 |
| Sapping | Elemental cloud: slows you, lowers your elemental resistances, raises monster resistances | 100 | 65 |
| Queen's | The Queen in the Mists guards the ritual | 44 | 65 |
- Claim: Types roll by weight from level 65. Five types weight 100, Queen's 44; Prowling, Fractured, Plagued and Croaking have weight 0.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: `atlas-dependent`: Queen's rituals need an atlas node. The Queen in the Mists boss (Life mult 250%, damage 250%) can drop three corrupted Idols (0.5.0).

## Tablets and map mods (atlas-dependent)
| Source | Effect |
|---|---|
| Ritual Tablet (base) | Adds Ritual Altars to a Map; 10 uses |
| Freedom of Faith (unique tablet) | Favours cost (10-15)% increased Tribute; can reroll twice as many times |
| Suffix Sacrifice | Sacrificed monsters give (18-30)% increased Tribute |
| Dogma / Devotion / Appeal | Reroll / defer cost (20-30)% reduced; deferred Favours return (25-40)% sooner |
| Prayers / Occult | (1-3) extra rerolls / (3-6)% chance a reroll is free |
| Foundling / Cult / Omens | Revived monsters (35-70)% more likely Magic / (25-40)% Rare; Favours (35-70)% more likely Omens |
- Claim: Rows are tablet craft mods and the unique tablet from the Ritual page misc-mod table.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Using more than one Ritual Tablet adds an extra altar if possible (0.5.5). Mysterious Altars quest rewards a Ritual Tablet (item level 70) and Ritualistic Book of Knowledge I ([Mysterious_Altars](https://poe2db.tw/us/Mysterious_Altars)).

## Quest chain to the pinnacle
- Claim: Legacy of the Maji (speak to Aoife) runs: complete all rituals in a map, travel to Caer Tarth, offer Tribute to get An Audience with the King, use it on the atlas to reveal the Crux of Nothingness, defeat the King, return with the Head of the King, place it on the Effigy, select 5 maps for the Rite of the Nameless, bring back the effigy pieces.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Legacy_of_the_Maji](https://poe2db.tw/us/Legacy_of_the_Maji), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: The Head of the King is a key dropped by the King (0.5.0) used in Caer Tarth to start the Rite of the Nameless. The Rite is a sequence of 5 maps; monsters from earlier rituals and the map boss reappear in later maps, the unique boss of each map appears only in that map's final ritual, and each map after the first has extra modifiers. Each map awards one pinnacle key element (0.5.0). Effigy pieces: Tangled Torso, Mossy Arm, Frayed Cloth, Brittle Arm, Ragged Cloth.

## Keys and fragments
| Item | Role |
|---|---|
| An Audience with the King | Required to reveal the Crux of Nothingness |
| Head of the King | King kill proof; starts Rite |
| Call of the Shadows (stack 1/5) | Attach five to the effigy in Caer Tarth to perform the Rite |
- Claim: Roles read from the item pages. Prices are not recorded here (PoE2DB panels name no league); see [PoE2DB economy](https://poe2db.tw/us/Economy).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB An_Audience_With_The_King](https://poe2db.tw/us/An_Audience_With_The_King), [Call_of_the_Shadows](https://poe2db.tw/us/Call_of_the_Shadows), [Head_of_the_King](https://poe2db.tw/us/Head_of_the_King), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: 0.5.1 notes call Call of the Shadows the tradeable fragment that starts the Bodach pinnacle fight.

## Bosses
| Boss | Area | Area level | Stats on PoE2DB |
|---|---|---|---|
| The King in the Mists | Crux of Nothingness (page text: Waystone Tier 14 or higher) | 80 | Arena table life 3,378,319 for both forms; armour 5,764 (form 1) and 7,925 (form 2); a third value 11,649 sits under the Energy Shield header column (equals 10% of the 116,494 base Life shown on the boss page); Life mult 375%, damage 188%, exp 300% |
| The Bodach | Caer Tarth (Rite pinnacle) | 79 | Arena table life 13,116,886; armour 7,945; Life mult 1820%, damage 320%, exp 400% |
- Claim: The King has a second form (stat flag "monster has second form") and is a Tier-3 map boss in form 2 with rarity +4800, quantity +800 and 25% chance to drop a map key of at least the current tier. Caer Tarth mods: boss drops corrupted rare tablets, 5% rare socket currency chance, 10% special gem chance.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Crux_of_Nothingness](https://poe2db.tw/us/Crux_of_Nothingness), [The_King_in_the_Mists](https://poe2db.tw/us/The_King_in_the_Mists), [Caer_Tarth](https://poe2db.tw/us/Caer_Tarth), [The_Bodach](https://poe2db.tw/us/The_Bodach), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Followers roam the Crux maze (0.5.3). Players cannot gain or lose experience there. Fight phases: not found in corpus.

## Unique drops tied to bosses
| Boss | Uniques (PoE2DB limit tag) |
|---|---|
| The King in the Mists | Beetlebite, From Nothing, Ingenuity, Pragmatism, The Burden of Shadows |
| The Bodach | Forgotten Warden, Liminal Coil, Periphery, Sylvan's Effigy, Vestige of Darkness |
| Ritual (unique tablet) | Freedom of Faith |
- Claim: PoE2DB gives each unique a limit tag naming the boss. From Nothing (jewel, radius small 1000) also states it drops from the King at the Crux at Difficulty 4.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB From_Nothing](https://poe2db.tw/us/From_Nothing), [The_King_in_the_Mists](https://poe2db.tw/us/The_King_in_the_Mists), [The_Bodach](https://poe2db.tw/us/The_Bodach), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Each unique page also shows "Dropped by: The Market"; meaning not explained in corpus. Mod values: link the item pages.

## Farm decision notes
- Claim: Value levers are Tribute gain, free or cheaper rerolls, Omen share of Favours and altar count per map; all depend on tablet/atlas setup.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Ritual](https://poe2db.tw/us/Ritual), tier 2, crawl 2026-11-23
- Confidence: [INFERRED]: synthesis of the tablet mod table; no source ranks the levers.
- Notes: Foretold Bounty (Rite maps) puts a named item in the first Favour list. `atlas-dependent`.
