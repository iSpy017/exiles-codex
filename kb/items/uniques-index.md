# Uniques — rules, tiers, drop restrictions

Scope: how uniques work and where boss-restricted ones come from. Name lists → [[uniques-armour]], [[uniques-other]]. Full boss loot tables → endgame/pinnacle-bosses (batch 15). Version 0.5.x unless noted.

## Count
- Claim: The 0.5.5.9 game data has 441 distinct unique names (alternate art removed): body armour 73, helmet 53, ring 39, gloves 37, shield 30, amulet 26, boots 25, mace 24, belt 21, jewel 13, charm 12, bow 11, spear 10, staff 10, sceptre 9, focus 8, quiver 8, wand 8, warstaff (quarterstaff) 7, flask 6, talisman 6, crossbow 5.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 uniques.json](https://github.com/repoe-fork/poe2), tier 2, retrieved 2026-11-17 (counted by me)
- Confidence: [INFERRED] data count — poe2wiki's [Unique](https://www.poe2wiki.net/wiki/Unique) page gives 395 released uniques incl. modifier variants (older page snapshot). Difference likely = unreleased/data-only entries and version drift. Not logged as a conflict — different counting basis.

## How uniques work
- Claim: Uniques have their own fixed mod lists (often mods that can't roll normally), usually keep the base's implicit, and most reforge/add/remove currency doesn't work on them.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Unique](https://www.poe2wiki.net/wiki/Unique), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: What does work: Divine Orb (values), Vaal Orb ([[corruption]]), Ancient Orb (reforge into another unique of the same class), Vaal Cultivation Orb, sanctification. Game data text for these in [[currency-index]].

## Where uniques come from
- Claim: Global drops from monsters and chests; Orb of Chance on a normal base (can destroy it); gambling at the Gambler; and drop-restricted uniques that come from specific bosses or mechanics.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Unique](https://www.poe2wiki.net/wiki/Unique), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: Omen of Chance stops the Orb of Chance destroying the item; Omen of the Ancients makes it upgrade to a random unique of the same class (game data, [[omens]]).

## Unique rarity tiers
- Claim: Uniques sit in four hidden tiers — Common, Uncommon, Rare, Mythic; the tier is rolled first, then a unique within it.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Unique item](https://poe2wiki.net/wiki/Unique_item), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: Patch 0.2.1 reworked Mythic drops (e.g. Headhunter, Astramentis, Mjölner) to make them farmable ([Poe-Vault](https://poe-vault.com/poe2/news/mythic-uniques-finally-get-a-drop-rate-buff-in-poe-2), tier 3).

## Boss-restricted uniques (partial)
- Claim:
  - King in the Mists (Ritual pinnacle): Beetlebite, Ingenuity; also reported The Burden of Shadows, Pragmatism, From Nothing (rarer). Always drops an omen too.
  - Arbiter of Ash: Ab Aeterno, Morior Invictus, Sine Aequo, Solus Ipse (common); Prism of Belief, Sacred Flame (Difficulty 4, rarer).
  - Simulacrum (wave 15): Collapsing Horizon, Megalomaniac (rare).
  - Xesht (Breach pinnacle): Beyond Reach (among others).
- Version: early access → 0.5.x; lists differ by source date
- Volatility: may-change (bosses moved in 0.5; Arbiter relocated, new apex Arbiter of Divinity per tier-5 guide)
- Source: [Maxroll Boss Loot Table Cheat Sheet](https://maxroll.gg/poe2/resources/boss-loot-table-cheat-sheet), tier 3 (updated 2025-01-07); [Mobalytics King in the Mists drop rates](https://mobalytics.gg/poe-2/guides/drop-rates-the-king-in-the-mists), tier 3; [poe2wiki The King in the Mists](https://poe2wiki.net/wiki/The_King_in_the_Mists), tier 2; Prima Games and kami-labs boss tables, tier 5; retrieved 2026-11-17
- Confidence: single-source per boss, mostly tier 3 and dated (early access)
- Notes: poe2wiki notes that since a later patch, difficulty-scaled bosses can drop all their uniques at any difficulty, with rare ones rarer at low difficulty. Re-verify every boss table against 1.0 in batch 15. Price relevance (Ingenuity, Prism of Belief, From Nothing) → economy batch.
