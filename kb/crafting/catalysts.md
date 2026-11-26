---
title: Catalysts
status: done
tracker_topic: "Catalysts"
tracker_note: "done (0.5.5.9 game data)"
defaults: v=0.5.5.9
---

Scope: catalyst types, what they do, where from. Prices → economy batch. Version 0.5.5.9.

## What catalysts do
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Catalysts are Breach-exclusive currency that add a special quality type to jewellery (or, refined versions, to jewels). Each type boosts one category of mods; applying one replaces any other quality type on the item. Each 1% of catalyst quality = 1% increased magnitude of the matching mods.
- src: RePoE poe2 keywords.json "Catalysts" + base_items.json descriptions, tier 2 (game data); poe2wiki Catalyst [S674], poe2wiki Quality [S717], tier 2; retrieved 2026-11-17
- notes: Max catalyst quality is 20% by default ([[items/quality]]); Vaal Catalysing Infuser can push rings/amulets past 20% with a chance to corrupt. Omen of Catalysing Exaltation: next Exalted Orb consumes all catalyst quality to raise the chance of that mod type ([[omens]]).


## Jewellery catalysts (rings/amulets, drop level 30)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Adaptive (attributes) · Carapace (armour/evasion/ES) · Chayula's (chaos) · Esh's (lightning) · Flesh (life) · Necrotic (minion) · Neural (mana) · Reaver (attack) · Sibilant (caster) · Skittering (speed) · Tul's (cold) · Uul-Netol's (physical) · Xoph's (fire).

- src: RePoE base_items.json (`CurrencyJewelleryQuality*`), tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Jewel catalysts (Refined, drop level 50)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Refined versions of all 13 types, applying the same quality types to jewels.
- src: RePoE base_items.json (`CurrencyJewelQuality*`), tier 2; poe2wiki Refined Necrotic Catalyst [S720], tier 2 (acquired by birthing a Lavish Wombgift at the Genesis Tree); retrieved 2026-11-17
- notes: Wombgifts / Genesis Tree = Breach system → [[breach]] (batch 14). Practical value: a 20% catalyst on a jewel or amulet with several mods of one category = ~20% more of those mods. [INFERRED from the 1%-per-1% rule]
