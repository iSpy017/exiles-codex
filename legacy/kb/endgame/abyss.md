# Abyss (league mechanic, encounter and rewards)

Status: partial. Encounter flow, factions, depths, key items and Well of Souls done. Missing: per-faction fissure boss stats, Abyssal Trove drop tables, endgame Abyss spawn rates (not in corpus).
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against the 1.0 release.
Sources: PoE2DB pages Abyssal Modifiers, Abyssal Depths, Abyssal Fissure, The Well of Souls, Abyss Tablet, key and gaze item pages.
Tags: may-change; `atlas-dependent` marks facts tied to atlas or tablet setup. No atlas passive content here (only names of subtree nodes that PoE2DB shows).

## Encounter flow
- Claim: An Abyss is a pit with fissures branching out. Monsters spawned near it are weakened. Kill them and the fissures close. When fissures reach the pit, it activates and spawns a large Abyssal pack; clear that to close the pit.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Abyssal Modifiers](https://poe2db.tw/us/Abyssal_Modifiers), tier 2, crawl 2026-11-23
- Confidence: confirmed (same text also on [PoE2DB Abyssal Depths](https://poe2db.tw/us/Abyssal_Depths))
- Notes: Weakened monsters' rarity decides the rarity of the emerging Abyssal, which steals some or all of their modifiers. Stolen mods on Rare Abyssals can upgrade to Abyssal Modifiers.

## Factions and monster groups
- Claim: Three Abyssal monster groups exist: Lightless, Blackblooded, Legion of the Pit. An area generally has one group. Abyssal Fissure areas hold Abysses of one faction only, where the closing area holds that faction's boss; the deeper you go, the denser and tougher the Abyssal spawns.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Abyssal Modifiers](https://poe2db.tw/us/Abyssal_Modifiers); [PoE2DB Abyssal Fissure](https://poe2db.tw/us/Abyssal_Fissure), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Faction names that appear on gear/skill text: Ulaman, Amanamu, Kurgal (Abyssal Fissure subtree text lists these three plus "Any Faction"). A subtree node named Balance of Power lets you pick the faction in non-Fissure Abysses (`atlas-dependent`; not detailed here).

## Abyssal Modifiers and Lichborn
- Claim: Abyssal Modifiers are upgrades of stolen mods. They can rarely become the stronger Lichborn Modifiers. Subtree nodes shown on the page raise the chance of both (Close to the Surface: Abyss Tablets add +25% chance for Abyssal and for Lichborn mods and +4% pack size in Abyssal Depths; Unholy Influence: +100% each, requires closing the Northern Abyssal Wounds).
- Version: 0.5.x
- Volatility: may-change `atlas-dependent`
- Source: [PoE2DB Abyssal Modifiers](https://poe2db.tw/us/Abyssal_Modifiers), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Individual mod lists not extracted; see [PoE2DB Abyssal Modifiers](https://poe2db.tw/us/Abyssal_Modifiers).

## Abyssal Depths
- Claim: Closing the final Abyss in an area can open the Abyssal Depths dungeon instead of a normal reward. All Rares inside have an Abyssal Modifier. The last room has a stronger Rare with a Lichborn plus an Abyssal modifier; killing it unlocks chests that drop Preserved Bone, and rarely extra Omens and Lineage Supports. A Depths subtree node gives +10% chance for Abysses to lead to Depths; another gives 25% chance for a Boss in Level 78+ Depths (and 25% for an Ulaman pit near the map boss to hold the Incubator Queen).
- Version: 0.5.x
- Volatility: may-change `atlas-dependent`
- Source: [PoE2DB Abyssal Depths](https://poe2db.tw/us/Abyssal_Depths), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: The page also lists three act-2 Depths layouts (area level 22, 1 extra Abyssal mod on natural Rares): Lightless (Abomination 19,459 life, Moray 14,152), Blackblooded and Pit variants (Strider of the Pit 19,459 life). Those are campaign values only.

## Preserved Bones and desecration
- Claim: Abyssal Troves and Depths chests drop Preserved Bones; each bone desecrates one Rare item of a class (Preserved Rib: Rare Armour, drop level 61; Preserved Vertebrae: Rare Waystone, drop level 65). Mark of the Abyssal Lord: desecrating an item with this mod always removes it and adds an unrevealed Desecrated mod of a higher tier.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Preserved Rib](https://poe2db.tw/us/Preserved_Rib); [PoE2DB Preserved Vertebrae](https://poe2db.tw/us/Preserved_Vertebrae); [PoE2DB Mark of the Abyssal Lord](https://poe2db.tw/us/Mark_of_the_Abyssal_Lord), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes: Revealing, bone types and mod pools live in [[crafting/desecration]]; not repeated here.

## Well of Souls (link to desecration)
- Claim: Act 2 optional quest "The Well of Souls": reach Lightless Passage from Mastodon Badlands, enter the Well (area level 22), use it. On completion you can reveal Desecrated modifiers. The same name is also an endgame pinnacle area (Act 10 tag, level 79) with boss Vessel of Kulemak: 1,873,841 life, 6,810 armour, 6,462 energy shield, 1.47 attack time, 1,099 damage (PoE2DB base stats). Players cannot gain or lose experience there.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB The Well of Souls](https://poe2db.tw/us/The_Well_of_Souls), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Boss mechanics and loot: see pinnacle-boss doc (batch 43), not covered here. Reveal procedure: [[crafting/desecration]].

## Key and entry items (decision rows)
| Item | What it does | Source / notes |
|---|---|---|
| Kulemak's Invitation | Cannot be used directly; with it in inventory the Well of Souls shows a "Jump In" option. Drops from Abyssal bosses per the wiki text. | [PoE2DB Kulemak's Invitation](https://poe2db.tw/us/Kulemaks_Invitation); wiki text there says the result of jumping is "currently unknown" |
| Abyss Tablet | Adds Abysses to a map; 10 uses (normal). Unique version "Unforeseen Consequences": (14-18) extra Abysses, 1 use, Map overrun by Abyssal. Drop level 65. | [PoE2DB Abyss Tablet](https://poe2db.tw/us/Abyss_Tablet) `atlas-dependent` |
| Kulemak's Dominion | Lineage support (Offering skills); dropped by Large Abyssal Troves; spells also affect around Offerings but deal 50% less damage that way. | [PoE2DB Kulemak's Dominion](https://poe2db.tw/us/Kulemaks_Dominion) |

## Abyssal Eyes (augments from Abyssals)
- Claim: Abyssal Eyes are socketable augments (require level 60, limited to 1 each, drop level 65). Four known: Amanamu's, Kurgal's, Ulaman's, Tecrod's Gaze. Effects differ by item slot. Example: Amanamu's Gaze on boots gives 1% movement speed per 15 Spirit (cap 40%) and removes other movement speed modifiers except Sprinting.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Abyssal Eye](https://poe2db.tw/us/Abyssal_Eye); [PoE2DB Amanamu's Gaze](https://poe2db.tw/us/Amanamus_Gaze), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Full per-slot lines on the Abyssal Eye page; link rather than copy. Prices change daily; not recorded.

## Lineage supports tied to the lords
- Claim: Amanamu's Tithe (Persistent Minions: 50% chance on Minion death for an Abyssal Monster Modifier for 20 s, max 3), Kurgal's Leash (Unholy Might 15 s on Command), Kulemak's Dominion (see table).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Amanamu's Tithe](https://poe2db.tw/us/Amanamus_Tithe); [PoE2DB Kurgal's Leash](https://poe2db.tw/us/Kurgals_Leash), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes: Drop sources of lineages: [[gems/lineage-drop-sources]].
