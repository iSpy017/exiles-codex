---
title: Corruption
status: done
tracker_topic: "Corruption"
tracker_note: "done (0.5.x)"
defaults: v=0.5.x
---

Scope: what corrupted means, Vaal Orb outcomes by item type, double corruption, sanctification, corrupted implicit pool. Version 0.5.x unless noted. Corrupted maps/monsters → endgame.

## Corrupted items
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Items can drop corrupted or be corrupted with a Vaal Orb, changing them unpredictably. Most crafting can't be used on corrupted items afterwards. There's no penalty for wearing them.
- src: RePoE poe2 keywords.json "Corrupted Items", tier 2 (game data), retrieved 2026-11-17
- conf: confirmed ([poe2wiki Corrupted](https://poe2wiki.net/wiki/Corrupted) same text)
- notes: Vaal Orb drop level 35 (game data). A Vaal Orb can't target an already-corrupted item.


## Vaal Orb outcomes: non-unique equipment
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
25% each — no change; reroll up to three mods into new ones; add a special Vaal enchantment; add a socket ignoring the socket limit.
- src: poe2wiki Corrupt [S679], tier 2; Maxroll Corruption Outcomes [S039], tier 3; retrieved 2026-11-17
- notes: Conflict on caster weapons: one wiki version says the socket outcome applies to all weapons incl. sceptres; another says martial weapons + armour only, with caster weapons getting ±10% quality (up to 23%) instead. Logged in [[conflicts]]. Items with no socket slot (rings, amulets, belts) effectively get ~50% no change (wiki notes "pseudo no change"). Omen of Corruption removes the no-change outcome for most items (Maxroll).


## Vaal Orb outcomes: uniques
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
No change; divine-like reroll of mod values at 0.78–1.22× normal range (can go above/below normal); add a Vaal enchant; special outcome for some uniques.
- src: Maxroll Corruption Outcomes [S039], tier 3; Mobalytics Vaal Corrupting [S091], tier 3; retrieved 2026-11-17
- conf: confirmed (two tier-3)
- notes: Odds per outcome for uniques not confirmed by tier 1–2.


## Vaal Orb outcomes: gems and waystones
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Skill gems can gain +1 level (kept as the gem levels — up to 21) or lose a support socket, among other outcomes (Mobalytics gives 12.5% each for those two). Waystones: 25% tier ±1 with mods rerolled (only way to T16), other outcomes add mods/implicits; the only clearly bad outcome is −1 tier.
- src: Mobalytics Vaal Corrupting [S091], tier 3; poe2wiki Waystone [S732], tier 2; Maxroll Rolling Waystones [S042], tier 3; retrieved 2026-11-17
- conf: confirmed for waystone tier change; single-source for gem odds
- notes: Corrupted gems can still level but can't gain quality. Early use: vaal spare gems for a 4th/5th support socket instead of buying Jeweller's (Maxroll). Gem levels → [[gem-levels]].


## Corruption-only implicits (examples)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
The corruption mod pool is slot-specific. Examples: helmet +20–30 spirit, +1 max power charge, +1–3% max cold res; body armour 3–5% additional phys DR, 10–20% damage recouped as life, +1% max ele res; boots 3–5% MS, +1–3% max lightning res; gloves 10–15% ele penetration, +1 max frenzy charge, gold quantity; belt +1 max endurance charge, +1–3% max fire res; amulet 3% phys attack leech, +1% max ele res; all armour 15–25% increased defences of its type.
- src: RePoE mods.json (`generation_type: corrupted`, 108 mods), tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Corrupted helmets with spirit are likely valuable for spirit-hungry builds [INFERRED]; price in economy batch.


## Corruption altars
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
There are one-use corruption altars in the campaign — Act 2 Vaal Ruins, and Act 3 Jiquani's Sanctum ("Paquate's Mechanism"), once per character.
- src: poe2wiki Corrupt [S679], tier 2; outof.games, tier 5; retrieved 2026-11-17
- vol: may-change (1.0 campaign changes)
- conf: single-source (tier 2) — re-check in campaign batch
- notes: Use on a spare skill gem for a socket/+1 [INFERRED: low risk].


## Double corruption and related currency
@ v=0.5 vol=may-change conf=confirmed date=2026-11-17
Architect's Orb works on a corrupted equipment or jewel item: 50% add a second corrupted enchant, 50% destroy it. Vaal Cultivation Orb replaces 1–2 mods on a corrupted Vaal unique with Vaal cultivation mods, or turns a non-Vaal unique into a random corrupted unique of the same class. Both come from the Vaal temple (Fate of the Vaal league).
- src: RePoE base_items.json (Architect's Orb text), tier 2; poe2wiki Vaal Cultivation Orb [S731], tier 2; Mobalytics Vaal currency [S092], tier 3; retrieved 2026-11-17
- v: 0.4/0.5 (league mechanic)
- vol: may-change (league content may change in 1.0)
- conf: confirmed (50/50 single-source tier 3; game text says "or destroys it")
- notes: → [[vaal-temple]].


## Sanctified items
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Sanctifying multiplies each mod's values by a random 78–122% (independently), then locks the item (most crafting no longer works).
- src: RePoE keywords.json "Sanctified Items", tier 2; poe2wiki Omen of Sanctification [S707], tier 2; retrieved 2026-11-17
