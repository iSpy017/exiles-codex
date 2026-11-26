# Tablets (Precursor Tablets)

Status: partial. Covers item class, types, uniques, mod-pool decision rows. Missing: per-type mod weights (PoE2DB says unavailable), exact drop rates, number of tablets allowed per map, rarity-specific mod counts, how Map Device slots work.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB pages Tablets, Tablet, per-type Tablet pages, Precursor_Towers, Waystones. Tags: atlas-dependent where noted.

## What tablets are
- Claim: Tablets are items placed in the Map Device to add extra endgame mechanics to maps on your Atlas. Each tablet has a number of "uses remaining".
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablets](https://poe2db.tw/us/Tablets), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Map Device item page in corpus has no tablet text. Mechanic detail: [[endgame/breach]], [[endgame/delirium]], [[endgame/ritual]], [[endgame/expedition]], [[endgame/abyss]].

## Base type table
- Claim: 8 base types exist, all drop level 65, item class Tablet, can be normal/magic/rare/unique. Base effect and base uses:

| Tablet | Base effect | Base uses |
|---|---|---|
| Breach | adds an Otherworldly Breach to a map | 10 |
| Expedition | adds a Kalguuran Expedition | 10 |
| Delirium | adds a Mirror of Delirium | 10 |
| Ritual | adds Ritual Altars | 10 |
| Irradiated | adds Irradiated to a map | 10 |
| Overseer | empowers the Map Boss | 10 |
| Abyss | adds Abysses | 10 |
| Temple | adds Vaal Beacons (Incursion tag) | 10 |

- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablet](https://poe2db.tw/us/Tablet), tier 2, crawl 2026-11-23; per-type pages e.g. [PoE2DB Breach Tablet](https://poe2db.tw/us/Breach_Tablet)
- Confidence: confirmed (summary list and per-type pages agree)
- Notes: Irradiated base is 10 uses here, but its uniques show 1 use (see uniques).

## Uses / charges
- Claim: Tablets are limited by uses remaining (10 on every base; 1 on 3 Irradiated uniques and the Abyss unique). A failed map cannot take tablets; a failed map can be re-run but loses extra content (essences, shrines, strongboxes) and is not corrupted.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablet](https://poe2db.tw/us/Tablet), [PoE2DB Tablets](https://poe2db.tw/us/Tablets), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Atlas passive "Curiously Durable Stone" gives a % chance to not consume tablet uses when opening maps (needs defeating the Precursor Fortress pinnacle boss). `atlas-dependent`; passive-tree content not recorded here. Whether uses drop per map opened vs per map completed: not found in sources.

## Use in Precursor Towers
- Claim: Precursor Tower maps are ancient structures on the Atlas; completing one (defeat boss, then activate the Precursor Beacon) reveals a large area and rewards a tablet. The listed normal reward is an Irradiated Tablet, item level 70.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Precursor Towers](https://poe2db.tw/us/Precursor_Towers), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: `atlas-dependent`. Unique tablet "The Grand Project" can only be applied to Precursor Tower maps. The pool of 90 tower mods (below) is listed on the Tablet page under "Precursor Towers Mods".

## Rarity and mods
- Claim: Mod pool page lists 90 mods (13 prefix, 77 suffix, all level 1). Mixed pool: generic map mods plus mechanic-specific ones tagged breach, delirium, ritual, expedition, abyss, incursion. Which mods roll on which tablet type: not shown (weights unavailable per PoE2DB).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablet](https://poe2db.tw/us/Tablet), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Full list: [PoE2DB Tablet](https://poe2db.tw/us/Tablet#PrecursorTowersMods) - not copied.

Decision rows (value ranges, 0.5.x):

| Goal | Mod (range) | Slot |
|---|---|---|
| Waystone drops | +(30-40)% Quantity of Waystones found in map (appears in hybrid mods, both prefix and suffix; Tablet page lines ~220-285) | prefix or suffix |
| Waystone drops | (18-30)% Quantity of Waystones dropped by Map Bosses | suffix |
| Boss loot | (13-20)% item quantity / (35-60)% item rarity from Map Bosses | suffix |
| Map difficulty | Monsters (10-15)% increased Effectiveness | prefix |
| Map loot | (8-12)% item rarity in map | prefix |
| Pack density | (5-7)% pack size; (25-35)% more rare monsters | prefix |
| Gold / XP | (25-35)% gold; (12-18)% experience | prefix |
| Chaos | (1-2) additional random map modifiers | suffix |
| Abyss | (20-40)% chance for four additional Abysses; 1 additional Abyss | suffix |
| Ritual | altars allow (1-3) additional rerolls | suffix |
| Breach | (30-60)% more Wombgifts / Hiveblood | suffix |
| Content | (70-100)% chance to contain strongboxes / shrines / essences / Azmeri / Rogue Exiles | suffix |

- Notes on rarity: unique tablets are listed as separate items; upgrading tablets to Rare comes from atlas passives "Reverse Transcription" and "Partial Translation" (each also +1 max modifier). `atlas-dependent`. Base-type pages show enable_rarity: normal, magic, rare, unique. Magic/rare mod counts: not found.

## Unique tablets
- Claim: PoE2DB lists 9 unique tablets.

| Unique | Type | Uses | Effect (short) |
|---|---|---|---|
| Wraeclast Besieged | Breach | 10 | Hives get (2-5) more waves; breaches (-10 to 20)% pack size; unstable breaches +120 s to collapse and (2-5) extra rares when stabilised |
| Clear Skies | Delirium | 10 | Fog never dissipates; fog (-10 to 10)% deliriousness |
| Freedom of Faith | Ritual | 10 | Favours cost (10-15)% more Tribute; twice as many rerolls |
| The Grand Project | Irradiated | 1 | Tower maps only; completing tower makes nearby maps accessible |
| Visions of Paradise | Irradiated | 1 | If map not previously Irradiated, completing it adds Irradiation instead |
| Mastered Domain | Irradiated | 1 | Map also counts as a Water map |
| Season of the Hunt | Overseer | 10 | Map Bosses hunted by Azmeri Spirits |
| Cruel Hegemony | Overseer | 10 | Map Bosses get 1 additional modifier |
| Unforeseen Consequences | Abyss | 1 | More Waystones found; extra rares from Abysses; (14-18) extra Abysses; map overrun by the Abyssal; large abyss-quantity penalty (-75) |

- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablet](https://poe2db.tw/us/Tablet), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: No unique Expedition or Temple tablet found. Unforeseen Consequences: exact "% more Waystones" value appears split in source; not recorded. Drop restrictions: not found.

## How they drop
- Claim: Sources found: (1) Precursor Tower completion; (2) the item Liquid Disgust (stack 1/10) makes players in area 18% Delirious and gives 30% increased Tablets found in area; (3) atlas passives: Rogue Exiles can drop an additional Tablet, % increased Quantity of Tablets found. (4) Pinnacle maps (Arbiter of Ash, Arbiter of Divinity) carry a stat "pinnacle boss drops X corrupted rare tablets" - X not stated. Some Waystones-page map entries (e.g. Hive Fortress, Breach) carry a "map drop no league tablets" stat; exact meaning not explained.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Tablets](https://poe2db.tw/us/Tablets), [PoE2DB Waystones](https://poe2db.tw/us/Waystones), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: `atlas-dependent`. [INFERRED]: general monster drops of tablets likely exist because drop level 65 is given, but no drop-source text found.

## Waystone interaction
- Claim: A Waystones page entry "Energized Ley Lines" doubles the effect of tablets used on the area; some atlas passives scale Waystone modifier effect per tablet affecting the map.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Waystones](https://poe2db.tw/us/Waystones), [PoE2DB Tablets](https://poe2db.tw/us/Tablets), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: `atlas-dependent`.
