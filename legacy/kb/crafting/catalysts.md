# Catalysts

Scope: catalyst types, what they do, where from. Prices → economy batch. Version 0.5.5.9.

## What catalysts do
- Claim: Catalysts are Breach-exclusive currency that add a special quality type to jewellery (or, refined versions, to jewels). Each type boosts one category of mods; applying one replaces any other quality type on the item. Each 1% of catalyst quality = 1% increased magnitude of the matching mods.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE poe2 keywords.json "Catalysts" + base_items.json descriptions, tier 2 (game data); [poe2wiki Catalyst](https://www.poe2wiki.net/wiki/Catalyst), [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Max catalyst quality is 20% by default ([[items/quality]]); Vaal Catalysing Infuser can push rings/amulets past 20% with a chance to corrupt. Omen of Catalysing Exaltation: next Exalted Orb consumes all catalyst quality to raise the chance of that mod type ([[omens]]).

## Jewellery catalysts (rings/amulets, drop level 30)
- Claim: Adaptive (attributes) · Carapace (armour/evasion/ES) · Chayula's (chaos) · Esh's (lightning) · Flesh (life) · Necrotic (minion) · Neural (mana) · Reaver (attack) · Sibilant (caster) · Skittering (speed) · Tul's (cold) · Uul-Netol's (physical) · Xoph's (fire).
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json (`CurrencyJewelleryQuality*`), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Jewel catalysts (Refined, drop level 50)
- Claim: Refined versions of all 13 types, applying the same quality types to jewels.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json (`CurrencyJewelQuality*`), tier 2; [poe2wiki Refined Necrotic Catalyst](https://www.poe2wiki.net/wiki/Refined_Necrotic_Catalyst), tier 2 (acquired by birthing a Lavish Wombgift at the Genesis Tree); retrieved 2026-11-17
- Confidence: confirmed
- Notes: Wombgifts / Genesis Tree = Breach system → [[breach]] (batch 14). Practical value: a 20% catalyst on a jewel or amulet with several mods of one category = ~20% more of those mods. [INFERRED from the 1%-per-1% rule]
