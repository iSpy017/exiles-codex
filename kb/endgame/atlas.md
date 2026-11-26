---
title: Atlas (structure, maps, nodes, biomes, towers, citadels, corruption)
status: partial
tracker_topic: "Atlas overview"
tracker_note: "partial (0.5.x baseline, all atlas-dependent; no passive tree)"
defaults: v=0.5.x
---
Status: partial. Covers structure and decision rows only. Atlas passive tree excluded. Exact 1.0 atlas changes unknown; everything tagged atlas-dependent may be replaced.
Version: 0.5.x (PoE2DB crawl 2026-11-23).
Sources: PoE2DB Atlas, Waystones, Map_Node, Biome, Precursor_Towers, Citadel, Corruption, Cleansed, Revival_Availability (tier 2).

## Atlas = map-node world
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Endgame travel is via Map Nodes on the Atlas. Click a node next to an area you already completed, put a waystone in the Map Device, traverse. A node needs a waystone; Landmark Areas are the exception (reusable, no waystone).
- src: poe2db:Waystones, tier 2, crawl 2026-11-23
- conf: confirmed (Waystone + Waystones pages agree)
- notes: Tags: atlas-dependent. Hub is the Ziggurat Refuge. See [[endgame/waystones]].


## Map completion / failure
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
A Map is completed by killing its Map Boss. A failed Map can be re-run but has no extra content (essences, shrines, strongboxes) and is not corrupted; tablets cannot be used on it. Wiki text on the Waystone page says dying removes access to that map (older early-access wording) so paths must route around it.
- src: poe2db:Map_Node, tier 2, crawl 2026-11-23
- conf: single-source (the "dying blocks the map" line is from old intro text; see report conflicts)
- notes: Tags: atlas-dependent. Node states on the legend: accessible, in progress, complete, failed.


## Map Boss tiers
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Every endgame map has a Map Boss; killing it completes the map. Powerful Map Bosses are tougher, have better drops, and often drop waystones one tier higher. Deadly Map Boss and Powerful Map Boss appear as separate legend icons.
- src: poe2db:Map_Boss, poe2db:Powerful_Map_Boss, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Chance of spawn depends on atlas passives/tablets (not recorded here).


## Revivals per map
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Most endgame content caps deaths before the area locks. After a boss-fight death the Map Owner can respawn everyone into a fresh boss instance. More modifiers on the waystone = fewer revivals.
- src: poe2db:Revival_Availability, tier 2, crawl 2026-11-23
- notes: Exact revival counts per mod count not found. Map Owner = player who made the area ([PoE2DB Map_Owner](https://poe2db.tw/us/Map_Owner)).


## Biomes
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Maps sit in Grass, Forest, Swamp, Desert, Mountain or Water biomes (common); cities and special biomes are rarer. Each biome has its own bonus list on PoE2DB (e.g. Swamp: experience/pack size; Mountain: rare chests/strongboxes). Some biome bonuses unlock only via atlas passives.
- src: poe2db:Biome, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Per-biome pages: Grass_Biome_3A_*, Swamp_Biome_3A_*, etc. in PoE2DB; full list not copied. Water also covers Expedition ocean/island areas.


## Precursor Towers
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Towers are special map nodes spread over the Atlas. Finishing one (kill the boss, then activate the Precursor Beacon at the end) reveals a large radius of nearby nodes and rewards a tablet. Tower bosses at area level 65: Precursor Displacer and Precursor Extractor.
- src: poe2db:Precursor_Towers, poe2db:Precursor_Tower, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Reward shown is an Irradiated Tablet (iLv70) at Normal. Tablets can add content to maps; tablet table lives in other docs.


## Irradiated
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Irradiated areas get +1 monster level. Irradiated Tablets add it to a map; one tablet variant can only target Precursor Tower maps.
- src: poe2db:Irradiated, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent.


## Corruption in the Atlas
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Some atlas regions are corrupted. Corrupted maps carry an extra modifier. Killed monsters close together coalesce into stronger "abomination" monsters. A Corrupted Nexus is guarded by a Corrupted Boss; killing the boss cleanses the Nexus.
- src: poe2db:Corruption, poe2db:Corrupted_Boss, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. 15 "EndGame Corrupt Mods" listed on PoE2DB; examples: monsters deal 20-30% more damage but have 20-30% less life, or the reverse with +life; some trade drop quantity for XP (100-150% more XP, -60 to -40 quantity). Link, not copied: [PoE2DB Corruption](https://poe2db.tw/us/Corruption). Reward-side mods include extra shrines, strongboxes, essences, Obelisks of Corruption.


## Cleansing
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
A cleansed area may add an extra modifier and spawns "Cleansed" monster packs (typical modifier: 20-30 additional packs). Variants include extra gold, extra Azmeri Spirit, +1 monster level, or loot trades (e.g. -60 to -40 item quantity for +150-200% rarity). Obelisks of Cleansing give a 10-second buff (100% item rarity, 50% more defences, 30% of damage as extra lightning).
- src: poe2db:Cleansed, poe2db:Obelisk_of_Cleansing, tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Cleansed monster list (Fettered ...) and stat table: see PoE2DB page.


## Citadels
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Three citadel types: Copper (Faridun cities), Iron (Ezomyte cities), Stone (Vaal cities). Each is reached with a Tier 15+ waystone and its boss drops a Faded / Ancient / Weathered Crisis Fragment respectively. Waystone drop chance increases give a chance of extra fragments. Collect all three types' fragments to enter the Burning Monolith.
- src: poe2db:Citadel, tier 2, crawl 2026-11-23
- conf: confirmed (Citadel + Waystones pages)
- notes: Tags: atlas-dependent. T15 = area 79 per [[endgame/waystones]]. Burning Monolith fight not covered here (see pinnacle docs). Invasion/Summoning Circle citadel-boss chances are atlas passives, omitted.


## Map content legend (objectives)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Map content icons: Powerful Map Boss, Breach, Expedition, Delirium Mirror, Ritual Altars, Abyss, Vaal Beacons, Irradiated, Notable Location, Great Beast, and others; objectives include rare monsters, strongboxes, shrines, essences, rogue exiles, azmeri spirits, summoning circles, checkpoints.
- src: poe2db:Waystones (Map Legends / Map Content), tier 2, crawl 2026-11-23
- notes: Tags: atlas-dependent. Which content spawns depends on atlas/tablets; see mechanic docs under endgame/.
