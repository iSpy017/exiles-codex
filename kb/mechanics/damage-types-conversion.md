# Damage Types & Conversion

Version note: all entries researched 2026-11-17 against 0.5.x sources (live league 0.5.5). Re-check at 1.0.
Access note: poe2wiki pages are blocked to direct fetch (Anubis); poe2wiki claims below come from search-engine snippets of those pages.

## The five damage types
- Claim: Five types: Physical, Fire, Cold, Lightning, Chaos. Fire, Cold, Lightning are the elemental types.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, retrieved 2026-11-17
- Confidence: single-source (consistent with every other page read)

## How each type is mitigated / special behaviour
- Claim: Physical is reduced by Armour (the only type that is), the others by their matching resistance. Chaos is the rarest type and strips double its value from Energy Shield. Fire hits build Flammability (→ Ignite); Cold hits apply Chill and build Freeze but cannot build Heavy Stun; Lightning hits can Shock.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: details per ailment in batch 2 docs; armour/res in [[mechanics/armour]], [[mechanics/resistances]]

## Conversion: two-step order
- Claim: Conversion happens in two steps: conversion built into the skill (skill gem, item- or ascendancy-granted skill) first, then every other source (gear, tree, global effects) applies to what's left.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Damage Conversion](https://poe2db.tw/us/Damage_conversion), tier 2; [poe2wiki Conversion](https://www.poe2wiki.net/wiki/Convert), tier 2; both retrieved 2026-11-17
- Confidence: confirmed

## Converted damage scales only as its final type
- Claim: Once converted, damage scales with modifiers for its new type only; the original type's modifiers no longer apply (e.g. phys→fire is not boosted by increased physical damage). This is a change from PoE1.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Damage conversion](https://poe2wiki.net/wiki/Damage_conversion), tier 2; [PoE2DB Damage Conversion](https://poe2db.tw/Damage_Conversion), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Any type → any type, no loops
- Claim: Damage can convert from any type to any other with no fixed order (PoE1 had a strict order). All conversion is applied at once, so damage can't convert twice and loops are impossible.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Overconversion](https://poe2wiki.net/wiki/Overconversion), tier 2; [Mobalytics Damage Conversion](https://mobalytics.gg/poe-2/guides/damage-conversion), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Overconversion
- Claim: If either step adds up to more than 100% of a type, it's scaled down proportionally to 100%.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Overconversion](https://poe2wiki.net/wiki/Overconversion), tier 2, retrieved 2026-11-17
- Confidence: single-source

## When conversion is calculated
- Claim: Conversion is applied after flat added damage is combined with base damage, but before any increased/more modifiers.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Damage conversion](https://poe2wiki.net/wiki/Damage_conversion), tier 2; [Mobalytics Damage Conversion](https://mobalytics.gg/poe-2/guides/damage-conversion), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: exception — weapon-local conversion on some weapons applies before the weapon's own local mods (quality, added phys, % phys), so those local mods don't boost the converted portion. Source: [poe2wiki Conversion](https://www.poe2wiki.net/wiki/Convert), single-source.

## "Gain as extra"
- Claim: "Gain X% of [type] as extra [type]" adds new damage while leaving the original intact (regular conversion removes it). It follows the same two-step process. Gained damage scales with the new type's modifiers only.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Overconversion](https://poe2wiki.net/wiki/Overconversion), tier 2; [poe2wiki Conversion](https://poe2wiki.net/wiki/Convert/edit?redlink=1), tier 2; retrieved 2026-11-17
- Confidence: single-source (one wiki, two pages)

## Hits only
- Claim: Conversion and gain only affect hits; damage over time can't be converted or gained.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Damage Conversion](https://poe2db.tw/us/Damage_conversion), tier 2; [poe2wiki Damage conversion](https://poe2wiki.net/wiki/Damage_conversion), tier 2; [Mobalytics](https://mobalytics.gg/poe-2/guides/damage-conversion), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: see [[mechanics/hits-vs-dot]]

## Non-damage conversion
- Claim: Stat conversion (e.g. evasion → armour) works the same way: the converted part scales with the new stat's modifiers only.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Conversion (Gains)](https://poe2wiki.net/wiki/Gains), tier 2, retrieved 2026-11-17
- Confidence: single-source
