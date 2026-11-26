---
title: Omens
status: done
tracker_topic: "Omens"
tracker_note: "done (0.5.5.9 game data)"
---

Scope: what omens do, full 0.5.5.9 list grouped by target currency. Prices → economy batch.

## How omens work
@ v=0.5.5.9 vol=stable conf=single-source date=2026-11-17
An omen does nothing on its own. While it's active in your inventory it changes the next use of a specific currency (or the next instance of an event), then is consumed.
- src: RePoE poe2 base_items.json [S002] (item class Omen, 45 items), tier 2 (game data), retrieved 2026-11-17
- conf: single-source (game text pattern: "While this item is active in your inventory your next …")
- notes: The King in the Mists always drops an omen; strong ones (e.g. Sinistral Annulment) are rare ([Mobalytics](https://mobalytics.gg/poe-2/guides/drop-rates-the-king-in-the-mists), tier 3). Ritual is the main omen source — [INFERRED], check in endgame/ritual. Directly relevant to your Ritual farm option.


## Exalted Orb omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Sinistral Exaltation (prefix only) · Dextral Exaltation (suffix only) · Greater Exaltation (adds two mods) · Homogenising Exaltation (adds a mod of the same type as one already on the item) · Catalysing Exaltation (consumes all catalyst quality to raise the chance of that mod type).
- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Greater Exaltation + Perfect Exalted Orb: both added mods follow the level-50 minimum rules ([[currency-index]]; GGG forum thread 3851632, tier 5).


## Chaos Orb omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Sinistral Erasure (removes only a prefix) · Dextral Erasure (removes only a suffix) · Whittling (removes the lowest-level mod). Waystone-only: Chaotic Effectiveness / Monsters / Quantity / Rarity (replace all mods with ones that don't grant monster effectiveness / monster rarity / pack size / item rarity).
- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Whittling + Chaos = cheap "remove the worst mod" step.


## Annulment omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Sinistral Annulment (prefixes only) · Dextral Annulment (suffixes only) · Greater Annulment (removes two mods) · Light (removes only desecrated mods).

- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Regal / Alchemy omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Sinistral / Dextral Coronation (Regal adds only prefix / suffix) · Homogenising Coronation (Regal adds a mod of a type already on the item) · Sinistral / Dextral Alchemy (Alchemy gives max prefixes / max suffixes).

- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Essence omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Sinistral / Dextral Crystallisation — the next Perfect or Corrupted essence removes only a prefix / only a suffix.
- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: → [[essences]].


## Desecration omens
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Sinistral / Dextral Necromancy (desecration adds only prefix / suffix) · Abyssal Echoes (reroll the three revealed options once) · Putrefaction (desecration replaces all mods with up to 6 unrevealed mods and corrupts the item) · the Blackblooded / the Liege / the Sovereign (weapon or jewellery desecration guarantees a Kurgal / Amanamu / Ulaman mod).
- src: RePoE base_items.json, tier 2; poe2wiki Omen of the Sovereign [S708], tier 2; retrieved 2026-11-17
- conf: confirmed (game data + wiki for Sovereign)
- notes: The wiki says the lord omen also blocks the other two lords' mods. → [[desecration]].


## Other currency omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Corruption (next Vaal Orb always changes something) · Sanctification (next Divine on a rare sanctifies it) · the Blessed (next Divine rerolls implicits only) · Chance (next Orb of Chance won't destroy the item) · the Ancients (next Orb of Chance turns the item into a random unique of the same class) · Recombination (no text in data).
- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Omen of Recombination has no description in the export — feeds into the recombinator check (crafting/recombinator, batch 9).


## Non-crafting omens
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Amelioration (prevents 75% of XP loss on death) · Answered Prayers (extra shrine effect) · Bartering (next sale's gold value misjudged) · Gambling (50% chance a gamble costs no gold and keeps the omen) · Refreshment (refill flask/charm charges at Low Life) · Resurgence (full life/mana/ES at Low Life) · Reinforcements (next rogue exile summons an ally) · Secret Compartments (next strongbox reopenable) · the Hunt (next possessed monster releases all Azmeri spirits).
- src: RePoE base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Amelioration is useful when pushing XP at high level. Drop levels: most omens 1; Catalysing/Homogenising/Greater Annulment/Crystallisation/Whittling/Chance 75; Sinistral/Dextral Annulment & Erasure, Sanctification, Blessed 80.
