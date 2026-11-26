# Expedition (endgame league mechanic, Kalguuran / Runes of Aldur form)

Status: partial. Core loop, tablets, Remnants, Runic mods, Logbooks, Grand Expeditions, bosses, keys, uniques and currency done. Not found in corpus: explosive counts for normal Expeditions, per-recipe reward tables (link only), Remnant wave numbers, boss phase mechanics, Tomb of the Fallen Knight boss stats.
Version: 0.5.x (PoE2DB crawl 2026-11-23). 1.0 not checked.
Sources: PoE2DB pages Expedition, Expedition_Logbook, Expedition_Tablet, Verisium_Remnant, Verisium, Liquid_Verisium, boss pages, Version_0.5.x notes. Tag `atlas-dependent` marks facts tied to atlas layout, waystone tier or atlas passives (passive content itself not recorded).

## What it is
- Claim: Expeditions are Kalguuran burial sites. You set explosives in a chain to dig up Verisium Remnants, monsters and chests. A Remnant's modifiers apply to monsters and chests unearthed by the same explosive that destroys it and by later explosives in the chain.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Expedition](https://poe2db.tw/us/Expedition), tier 2, crawl 2026-11-23
- Confidence: single-source (blurb on the page, agrees with Version_0.5.0 notes)
- Notes: This is the Runes of Aldur rework. Version_0.5.5 moved Farrow, Dannig and Expedition into the core atlas including Standard, and Expeditions can be found from Act 4 onward ([PoE2DB Version_0.5.5](https://poe2db.tw/us/Version_0.5.5)). Expedition Tablets cannot be obtained in the Runes of Aldur league itself (same note). Related: [[endgame/ritual]].

## Tablets (atlas-dependent)
| Tablets in a map | Effect |
|---|---|
| 1 | Adds a Kalguuran Expedition |
| 2 | Adds a Verisium Remnant; +35% Expedition density |
| 3 | Adds another Kalguuran Expedition |
| 4 | Adds another Verisium Remnant; another +35% density |
- Claim: Base Expedition Tablet adds a Kalguuran Expedition, has 10 uses, and drops from level 65. Unique tablet Forgotten By Time: monsters in your maps spawn with half their Life missing and Runic Monsters are duplicated.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Version_0.5.5](https://poe2db.tw/us/Version_0.5.5), [Expedition_Tablet](https://poe2db.tw/us/Expedition_Tablet), [Expedition](https://poe2db.tw/us/Expedition), tier 2, crawl 2026-11-23
- Confidence: confirmed (Version note and tablet page agree on the base effect)
- Notes: Tablet craft mods are on the Expedition page misc-mod table; link rather than copy.

## Explosives and Runic Monsters
- Claim: Runic Monsters are the strong monsters unearthed in Expeditions and are more common when you use explosives on larger markers. Logbook map mods can raise explosive radius, count and placement range by (25-50)%.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Expedition](https://poe2db.tw/us/Expedition), [Expedition_Logbook](https://poe2db.tw/us/Expedition_Logbook), tier 2, crawl 2026-11-23
- Confidence: confirmed (both pages)
- Notes: Grand Expeditions allow 15 placed explosives (down from 20) since 0.5.3. Verisium Sentries follow you once unearthed and add Runic modifiers to monsters in the area. Vaal Relics work like Remnants.

## Remnants, runes and recipes
- Claim: Each Verisium Remnant has rune slots and starts with one rune inscribed. The inscribed runes choose which reward you may craft (Runeshape recipes). You then fight waves of Verisium-infused monsters to receive the reward. Slot count at launch ranged 2 to 10, rarer at higher counts but allowing rarer items. Extra runeshapes add waves and add Runic modifiers to monsters each wave.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Verisium_Remnant](https://poe2db.tw/us/Verisium_Remnant), [Version_0.5.0](https://poe2db.tw/us/Version_0.5.0), tier 2, crawl 2026-11-23
- Confidence: confirmed (both pages)
- Notes: Recipes offer Alloys, currency, gems, runes and uniques; full list with 322 entries: [PoE2DB Runeshape_Combinations](https://poe2db.tw/us/Runeshape_Combinations) (the number column there is unlabelled in the crawl, so it is not recorded). Remnants pick a random rune slot to propagate (0.5.4).

## Runic Monster modifiers
- Claim: The page lists 62 Remnant mods: reward suffixes (+20% quantity, +40/60% rarity, +100/200% experience, duplicated Runic Monsters, Azmeri Spirit, 10% corrupted drops) and danger prefixes (damage-type immunities, always-crit hits, 30% hit avoidance, hexproof, extra damage as element, +30% resistances). The Logbook wiki blurb warns that many Remnant mods can brick a build.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Expedition](https://poe2db.tw/us/Expedition), [Expedition_Logbook](https://poe2db.tw/us/Expedition_Logbook), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Reward mods mention Artifacts, but Artifact currencies are marked unusable (see Vendors).

## Verisium, Anvil and Liquid Verisium
- Claim: Verisium is a stackable currency (stack 1000) used at the Verisium Anvil. Runeforging adds Runic Ward to armour; armour below level 55 gets it without downside, higher-level armour trades some base defence (0.5.0). Liquid Verisium instantly starts a Runic Remnant encounter with a random inscription; Farrow sells it for Verisium after the Feeling Lucky Expedition atlas passive is taken.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Verisium](https://poe2db.tw/us/Verisium), [Liquid_Verisium](https://poe2db.tw/us/Liquid_Verisium), [Version_0.5.0](https://poe2db.tw/us/Version_0.5.0), [Version_0.5.4](https://poe2db.tw/us/Version_0.5.4), tier 2
- Confidence: confirmed
- Notes: Prices not recorded (see [PoE2DB economy](https://poe2db.tw/us/Economy)). `atlas-dependent` for the Farrow sale. Runic Ward absorbs a lethal hit (you drop to 1 Life), regenerates 5% per second by default; monsters can have it and cannot be culled while they do ([PoE2DB Runic_Ward](https://poe2db.tw/us/Runic_Ward)). Eventide Petals is made at the Anvil from Veridical Chain, Exceptional Verisium x40 and one Olroth's Crest of the Sun.

## Logbooks and Grand Expeditions (atlas-dependent)
- Claim: An Expedition Logbook (drop level 78) is consumed at a Logbook Expedition node on the atlas and reveals an Ocean Biome. Every section revealed has at least one Grand Expedition (0.5.2). Grand Expeditions are larger Expeditions with special Remnants and have 1 to 2 map modifiers (0.5.4); they exist only in Ocean Biomes revealed by Logbooks.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Expedition_Logbook](https://poe2db.tw/us/Expedition_Logbook), [Version_0.5.2](https://poe2db.tw/us/Version_0.5.2), [Version_0.5.4](https://poe2db.tw/us/Version_0.5.4), tier 2
- Confidence: confirmed
- Notes: Max Remnants in a Grand Expedition rises with Waystone tier, highest at Tier 15+ (0.5.3). Logbook mods include Remnants with 5/6/7+ rune slots, a Power Rune Remnant, rarest-of-one-roll Remnants and +(1-3) Remnants.

## Keys: Sagas
| Item | Effect |
|---|---|
| Olroth's Saga | Next Logbook guarantees an Olroth encounter in the revealed biome |
| Medved's Saga | Guarantees Medved |
| Vorana's Saga | Guarantees Vorana |
| Uhtred's Saga | Guarantees Uhtred |
| Aldur's Saga | Next Logbook adds special modifiers to revealed Grand Expedition areas |
- Claim: Sagas are Omens (drop level 78, stack 10) that you activate in inventory before using a Logbook.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Olroths_Saga](https://poe2db.tw/us/Olroths_Saga), [Aldurs_Saga](https://poe2db.tw/us/Aldurs_Saga), tier 2
- Confidence: single-source
- Notes: Prices not recorded (PoE2DB panels name no league); see [PoE2DB economy](https://poe2db.tw/us/Economy). The Aberration meteor rain stops on its death (0.5.4).

## Bosses
| Boss | Logbook mod level | Arena | Life mult | Damage mult | Stats on PoE2DB |
|---|---|---|---|---|---|
| Medved (Feller of Heroes / the Fallen Seer) | 68 | Sprawling Jungle | 313% | 288% | Level 65 Life 20,517 |
| Vorana, Last to Fall | 68 | Mournful Cliffside | 313% | 288% | Level 65 Life 20,517 |
| Uhtred (Covetous Traitor / the Stardrinker) | 75 | Secluded Temple | 375% | 280% | Level 65 Life 24,581 |
| Olroth, Origin of the Fall | 81 | Obscure Island, Kalguuran Tomb (area level 80) | 352% | 300% | Level 80 Life 109,349 (page lines 196-204) |
| The Aberration | not a logbook mod | Ruins of Kingsmarch | 990% | 320% | Level 79 Life 246,035 |
- Claim: Medved, Vorana, Uhtred and Olroth became powerful map bosses with notably more Life in 0.5.4b. Olroth is tier 3 with rarity +4800; Medved and Vorana are tier 2 with +1600.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Expedition_Logbook](https://poe2db.tw/us/Expedition_Logbook), [Olroth](https://poe2db.tw/us/Olroth_2C_Origin_of_the_Fall), [Kalguuran_Tomb](https://poe2db.tw/us/Kalguuran_Tomb), [Version_0.5.4b](https://poe2db.tw/us/Version_0.5.4b), tier 2
- Confidence: single-source
- Notes: Each boss page's own stat block predates the map-boss fix, so real Life is higher. Boss fight mechanics: not found in corpus. The Aberration is the boss of Ruins of Kingsmarch on PoE2DB.

## Boss drops and uniques
| Source | Drops (PoE2DB) |
|---|---|
| Olroth | Uniques Svalinn, Keeper of the Arc, Olroth's Resolve, Olrovasara, Heroic Tragedy; lineage support Uhtred's Exodus |
| Medved | Lineage support Vorana's Siege |
| Uhtred | Lineage support Uhtred's Rite |
| The Aberration | Lineage support Olroth's Conviction |
| Expedition (generic limit tag) | Uhtred's Chalice, Eventide Petals |
- Claim: Uniques carry a limit tag naming Olroth or Expedition. Styrn in the Tomb of the Fallen Knight always drops an Expedition Logbook (0.5.3).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Svalinn](https://poe2db.tw/us/Svalinn), [Olroths_Conviction](https://poe2db.tw/us/Olroths_Conviction), [Version_0.5.3](https://poe2db.tw/us/Version_0.5.3), tier 2
- Confidence: single-source
- Notes: Lineage support values: link each gem page. The Grand Expedition quest rewards each Logbook type and boss defeat grants Expedition atlas points (0.5.4); skipped as atlas passive content.

## Vendors and legacy currency
- Claim: Dannig's faction items (Broken Circle Artifact, Black Scythe Artifact, Order Artifact, Sun Artifact) and Exotic Coinage each show "no longer usable" on their own pages (Broken Circle, Black Scythe, Order, Sun, Exotic Coinage). Farrow and the Verisium Anvil are the live Expedition services. Rog, Gwennen and Tujen pages exist, but their 0.5.x roles are not described in the corpus.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Broken_Circle_Artifact](https://poe2db.tw/us/Broken_Circle_Artifact), [Exotic_Coinage](https://poe2db.tw/us/Exotic_Coinage), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Remnant mods still reference Artifact quantity; treated as leftover text.
