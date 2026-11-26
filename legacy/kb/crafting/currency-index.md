# Currency index (crafting & utility)

Scope: every core currency in the 0.5.5.9 game data with its effect and drop level. Quality currency → [[items/quality]]. Corruption currency → [[corruption]]. Essences → [[essences]]. Omens → [[omens]]. Bones → [[desecration]]. Prices → economy batch. Effects are paraphrased from the in-game text.

Source for every entry unless noted: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) (StackableCurrency descriptions + drop_level), tier 2 (game data 0.5.5.9), retrieved 2026-11-17. Version 0.5.5.9. Volatility: may-change.

## Rarity upgrades (normal → magic → rare)
- Claim:
  - Orb of Transmutation (drop 1): normal → magic with 1 mod. Greater (46), Perfect (72) versions.
  - Orb of Augmentation (1): add a mod to a magic item. Greater (46), Perfect (72).
  - Orb of Alteration (2): reforge a magic item with new random mods.
  - Regal Orb (5): magic → rare, adding 1 mod. Greater (72), Perfect (79).
  - Orb of Alchemy (5): normal or magic → rare with 4 random mods.
  - Orb of Chance (12): normal → unique, or destroys the item.
- Confidence: single-source (game data); tiers confirmed by [Poe-Vault Currency & Crafting](https://www.poe-vault.com/poe2/guides/currency-and-crafting), tier 3

## Rare-item crafting
- Claim:
  - Exalted Orb (5): add a random mod to a rare. Greater (72), Perfect (79).
  - Chaos Orb (12): remove a random mod and add a new random one. Greater (72), Perfect (79).
  - Orb of Annulment (35): remove a random mod from an item.
  - Fracturing Orb: fracture (lock permanently) a random mod on a rare with at least 4 mods.
  - Divine Orb (35): reroll the numeric values of an item's mods.
  - Blessed Orb (35): reroll implicit values. Sacred Orb (35): reroll base defence values on armour.
  - Orb of Scouring (12): remove all mods.
  - Hinekora's Lock (46): preview the result of the next currency used on the item; any change removes the preview.
  - Mirror of Kalandra (35): create a mirrored copy.
- Confidence: single-source (game data)
- Notes: Exalted Orbs were the low-value unit late in Forbidden Rites ([[league-lifecycle-pricing]]).

## Greater / Perfect = minimum modifier level
- Claim: Greater and Perfect versions add mods with a minimum modifier level: Greater Exalted / Chaos (and Regal) 35, Perfect 50; Greater Transmutation / Augmentation 55, Perfect 70. They can't fully block a mod type — if every tier of a mod is below the minimum, its highest tier the item level allows stays in the pool.
- Version: 0.3+ (still 0.5.x)
- Volatility: may-change
- Source: [poe2wiki Greater Exalted Orb](https://www.poe2wiki.net/wiki/Greater_Exalted_Orb), [poe2wiki Perfect Exalted Orb](https://www.poe2wiki.net/wiki/Perfect_Exalted_Orb), [poe2wiki Greater Orb of Transmutation](https://www.poe2wiki.net/wiki/Greater_Orb_of_Transmutation), tier 2; [Mobalytics 0.3 crafting changes](https://mobalytics.gg/poe-2/guides/0-3-crafting-changes), tier 3; GGG forum thread [3851605](https://www.pathofexile.com/forum/view-thread/3851605), tier 5; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Greater/Perfect Regal 35/50 is [INFERRED] by analogy to Exalt/Chaos — no direct source found. Keyword "Minimum Modifier Level" also blocks use on items below that ilvl ([[affix-tiers]]). At higher levels, lower-tier drops partly roll up into Greater/Perfect drops (poe2wiki Currency item).

## Sockets and gems
- Claim:
  - Artificer's Orb (5): add an augment socket to a martial weapon, wand, staff or armour ([[sockets-augments]]).
  - Orb of Extraction: destroy an equipment item, returning its non-socket-bound augments.
  - Lesser / Greater / Perfect Jeweller's Orb (25 / 45 / 65): set a skill gem to 3 / 4 / 5 support sockets.
  - Gemcutter's Prism (12): gem quality.
  - Prime / Secondary Regrading Lens: change the quality type of a skill / support gem with quality.
  - Facetor's Lens: add stored experience to a gem, up to its max level.
  - Perfect Flux (75): upgrade the skills on an item to level 20.
- Confidence: single-source (game data)
- Notes: Regrading Lenses imply alternate gem quality types exist in data — conflicts with [[gems/quality]] "alt qualities not found" (marked partial there). [INFERRED] may be data-only; verify in game.

## Utility
- Claim: Scroll of Wisdom (identify), Portal Scroll, Orb of Regret (one passive refund point, drop 12), an atlas passive refund currency, Harbinger's Orb (reforge a map item into a higher tier), Orb of Horizons (68, reforge a map item into another of the same tier).
- Confidence: single-source (game data)
- Notes: Shards: Transmutation, Alteration, Alchemy, Chance, Regal, Chaos, Exalted, Annulment, Fracturing, Ancient, Mirror, Artificer's, Binding, Horizon, Harbinger's — 10 shards make an orb (Artificer's confirmed by Maxroll; others [INFERRED] same rule).

## League / Vaal temple currency (0.5)
- Claim: Ancient Orb (reforge a unique as another of the same class), Architect's Orb, Crystallised Corruption (double-corrupt a gem, may destroy), Core Destabiliser (modify a soul core, may destroy), Ancient Infuser (corrupt a tablet), Vaal Cultivation Orb, four Orbs of Sacrifice (Yaomac's weapon/quiver, Kopec's armour, Kamasa's jewellery, Yugul's jewel — upgrade the corruption enchant on a rare and remove a random mod), Vaal Infusers (quality over cap), Liquid Verisium (start a Runic Remnant encounter — Expedition).
- Confidence: single-source (game data)
- Notes: → [[vaal-temple]], [[expedition]].

## In data but probably not live
- Claim: PoE1-style items exist in the export: Chromatic Orb, Orb of Fusing, Orb of Binding, Orb of Dominance, Eldritch Orb of Annulment, Simple/Prime/Awakened/Elevated Sextants, Hollow Fossil, Vials.
- Confidence: [INFERRED] — shared data tables with PoE1; none appear in PoE2 crafting guides checked (Maxroll, Poe-Vault). Ignore unless seen in game.
