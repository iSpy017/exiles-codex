---
title: Expedition (endgame league mechanic, Kalguuran / Runes of Aldur form)
status: partial
tracker_topic: "Expedition"
tracker_note: "partial (0.5.x Runes of Aldur form; explosive counts/recipes not in corpus; recheck 1.0)"
defaults: v=0.5.x
---

Status: partial. Core loop, tablets, Remnants, Runic mods, Logbooks, Grand Expeditions, bosses, keys, uniques and currency done. Not found in corpus: explosive counts for normal Expeditions, per-recipe reward tables (link only), Remnant wave numbers, boss phase mechanics, Tomb of the Fallen Knight boss stats.
Version: 0.5.x (PoE2DB crawl 2026-11-23). 1.0 not checked.
Sources: PoE2DB pages Expedition, Expedition_Logbook, Expedition_Tablet, Verisium_Remnant, Verisium, Liquid_Verisium, boss pages, Version_0.5.x notes. Tag `atlas-dependent` marks facts tied to atlas layout, waystone tier or atlas passives (passive content itself not recorded).

## What it is
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Expeditions are Kalguuran burial sites. You set explosives in a chain to dig up Verisium Remnants, monsters and chests. A Remnant's modifiers apply to monsters and chests unearthed by the same explosive that destroys it and by later explosives in the chain.
- src: poe2db:Expedition, tier 2, crawl 2026-11-23
- conf: single-source (blurb on the page, agrees with Version_0.5.0 notes)
- notes: This is the Runes of Aldur rework. Version_0.5.5 moved Farrow, Dannig and Expedition into the core atlas including Standard, and Expeditions can be found from Act 4 onward ([PoE2DB Version_0.5.5](https://poe2db.tw/us/Version_0.5.5)). Expedition Tablets cannot be obtained in the Runes of Aldur league itself (same note). Related: [[endgame/ritual]].


## Tablets (atlas-dependent)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
| Tablets in a map | Effect |
|---|---|
| 1 | Adds a Kalguuran Expedition |
| 2 | Adds a Verisium Remnant; +35% Expedition density |
| 3 | Adds another Kalguuran Expedition |
| 4 | Adds another Verisium Remnant; another +35% density |
Base Expedition Tablet adds a Kalguuran Expedition, has 10 uses, and drops from level 65. Unique tablet Forgotten By Time: monsters in your maps spawn with half their Life missing and Runic Monsters are duplicated.
- src: poe2db:Version_0.5.5, poe2db:Expedition_Tablet, poe2db:Expedition, tier 2, crawl 2026-11-23
- conf: confirmed (Version note and tablet page agree on the base effect)
- notes: Tablet craft mods are on the Expedition page misc-mod table; link rather than copy.


## Explosives and Runic Monsters
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Runic Monsters are the strong monsters unearthed in Expeditions and are more common when you use explosives on larger markers. Logbook map mods can raise explosive radius, count and placement range by (25-50)%.
- src: poe2db:Expedition, poe2db:Expedition_Logbook, tier 2, crawl 2026-11-23
- conf: confirmed (both pages)
- notes: Grand Expeditions allow 15 placed explosives (down from 20) since 0.5.3. Verisium Sentries follow you once unearthed and add Runic modifiers to monsters in the area. Vaal Relics work like Remnants.


## Remnants, runes and recipes
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Each Verisium Remnant has rune slots and starts with one rune inscribed. The inscribed runes choose which reward you may craft (Runeshape recipes). You then fight waves of Verisium-infused monsters to receive the reward. Slot count at launch ranged 2 to 10, rarer at higher counts but allowing rarer items. Extra runeshapes add waves and add Runic modifiers to monsters each wave.
- src: poe2db:Verisium_Remnant, poe2db:Version_0.5.0, tier 2, crawl 2026-11-23
- conf: confirmed (both pages)
- notes: Recipes offer Alloys, currency, gems, runes and uniques; full list with 322 entries: [PoE2DB Runeshape_Combinations](https://poe2db.tw/us/Runeshape_Combinations) (the number column there is unlabelled in the crawl, so it is not recorded). Remnants pick a random rune slot to propagate (0.5.4).


## Runic Monster modifiers
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The page lists 62 Remnant mods: reward suffixes (+20% quantity, +40/60% rarity, +100/200% experience, duplicated Runic Monsters, Azmeri Spirit, 10% corrupted drops) and danger prefixes (damage-type immunities, always-crit hits, 30% hit avoidance, hexproof, extra damage as element, +30% resistances). The Logbook wiki blurb warns that many Remnant mods can brick a build.
- src: poe2db:Expedition, poe2db:Expedition_Logbook, tier 2, crawl 2026-11-23
- notes: Reward mods mention Artifacts, but Artifact currencies are marked unusable (see Vendors).


## Verisium, Anvil and Liquid Verisium
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Verisium is a stackable currency (stack 1000) used at the Verisium Anvil. Runeforging adds Runic Ward to armour; armour below level 55 gets it without downside, higher-level armour trades some base defence (0.5.0). Liquid Verisium instantly starts a Runic Remnant encounter with a random inscription; Farrow sells it for Verisium after the Feeling Lucky Expedition atlas passive is taken.
- src: poe2db:Verisium, poe2db:Liquid_Verisium, poe2db:Version_0.5.0, poe2db:Version_0.5.4, tier 2
- notes: Prices not recorded (see [PoE2DB economy](https://poe2db.tw/us/Economy)). `atlas-dependent` for the Farrow sale. Runic Ward absorbs a lethal hit (you drop to 1 Life), regenerates 5% per second by default; monsters can have it and cannot be culled while they do ([PoE2DB Runic_Ward](https://poe2db.tw/us/Runic_Ward)). Eventide Petals is made at the Anvil from Veridical Chain, Exceptional Verisium x40 and one Olroth's Crest of the Sun.


## Logbooks and Grand Expeditions (atlas-dependent)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
An Expedition Logbook (drop level 78) is consumed at a Logbook Expedition node on the atlas and reveals an Ocean Biome. Every section revealed has at least one Grand Expedition (0.5.2). Grand Expeditions are larger Expeditions with special Remnants and have 1 to 2 map modifiers (0.5.4); they exist only in Ocean Biomes revealed by Logbooks.
- src: poe2db:Expedition_Logbook, poe2db:Version_0.5.2, poe2db:Version_0.5.4, tier 2
- notes: Max Remnants in a Grand Expedition rises with Waystone tier, highest at Tier 15+ (0.5.3). Logbook mods include Remnants with 5/6/7+ rune slots, a Power Rune Remnant, rarest-of-one-roll Remnants and +(1-3) Remnants.


## Keys: Sagas
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Item | Effect |
|---|---|
| Olroth's Saga | Next Logbook guarantees an Olroth encounter in the revealed biome |
| Medved's Saga | Guarantees Medved |
| Vorana's Saga | Guarantees Vorana |
| Uhtred's Saga | Guarantees Uhtred |
| Aldur's Saga | Next Logbook adds special modifiers to revealed Grand Expedition areas |
Sagas are Omens (drop level 78, stack 10) that you activate in inventory before using a Logbook.
- src: poe2db:Olroths_Saga, poe2db:Aldurs_Saga, tier 2
- notes: Prices not recorded (PoE2DB panels name no league); see [PoE2DB economy](https://poe2db.tw/us/Economy). The Aberration meteor rain stops on its death (0.5.4).


## Bosses
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Boss | Logbook mod level | Arena | Life mult | Damage mult | Stats on PoE2DB |
|---|---|---|---|---|---|
| Medved (Feller of Heroes / the Fallen Seer) | 68 | Sprawling Jungle | 313% | 288% | Level 65 Life 20,517 |
| Vorana, Last to Fall | 68 | Mournful Cliffside | 313% | 288% | Level 65 Life 20,517 |
| Uhtred (Covetous Traitor / the Stardrinker) | 75 | Secluded Temple | 375% | 280% | Level 65 Life 24,581 |
| Olroth, Origin of the Fall | 81 | Obscure Island, Kalguuran Tomb (area level 80) | 352% | 300% | Level 80 Life 109,349 (page lines 196-204) |
| The Aberration | not a logbook mod | Ruins of Kingsmarch | 990% | 320% | Level 79 Life 246,035 |
Medved, Vorana, Uhtred and Olroth became powerful map bosses with notably more Life in 0.5.4b. Olroth is tier 3 with rarity +4800; Medved and Vorana are tier 2 with +1600.
- src: poe2db:Expedition_Logbook, poe2db:Olroth_2C_Origin_of_the_Fall «Olroth», poe2db:Kalguuran_Tomb, poe2db:Version_0.5.4b, tier 2
- notes: Each boss page's own stat block predates the map-boss fix, so real Life is higher. Boss fight mechanics: not found in corpus. The Aberration is the boss of Ruins of Kingsmarch on PoE2DB.


## Boss drops and uniques
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Source | Drops (PoE2DB) |
|---|---|
| Olroth | Uniques Svalinn, Keeper of the Arc, Olroth's Resolve, Olrovasara, Heroic Tragedy; lineage support Uhtred's Exodus |
| Medved | Lineage support Vorana's Siege |
| Uhtred | Lineage support Uhtred's Rite |
| The Aberration | Lineage support Olroth's Conviction |
| Expedition (generic limit tag) | Uhtred's Chalice, Eventide Petals |
Uniques carry a limit tag naming Olroth or Expedition. Styrn in the Tomb of the Fallen Knight always drops an Expedition Logbook (0.5.3).
- src: poe2db:Svalinn, poe2db:Olroths_Conviction, poe2db:Version_0.5.3, tier 2
- notes: Lineage support values: link each gem page. The Grand Expedition quest rewards each Logbook type and boss defeat grants Expedition atlas points (0.5.4); skipped as atlas passive content.


## Vendors and legacy currency
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Dannig's faction items (Broken Circle Artifact, Black Scythe Artifact, Order Artifact, Sun Artifact) and Exotic Coinage each show "no longer usable" on their own pages (Broken Circle, Black Scythe, Order, Sun, Exotic Coinage). Farrow and the Verisium Anvil are the live Expedition services. Rog, Gwennen and Tujen pages exist, but their 0.5.x roles are not described in the corpus.
- src: poe2db:Broken_Circle_Artifact, poe2db:Exotic_Coinage, tier 2, crawl 2026-11-23
- notes: Remnant mods still reference Artifact quantity; treated as leftover text.

## Remnant waves and rune carry-over (poe2wiki)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-27
A detonated Verisium Remnant spawns waves of defenders: one fewer wave than it has runes; its runes empower monsters or add hazards left to right. Each detonated remnant also passes one highlighted rune to the monsters of every later explosion in the chain. Starting without choosing a runeshape picks one at random. Explosives must sit within range of the detonator or the previous explosive; the chain moves to the next explosive once most summoned monsters are dead. Shattering a cleared remnant gives the chosen reward, some Verisium and sometimes Crests for Runeforging.
- src: poe2wiki Expedition [S743], tier 2, retrieved 2026-11-27 (rev 135464)
- notes: explosive count and radius per tier still not on the page. Runes of Aldur (0.5) form; [[crafting/league-crafting]].
