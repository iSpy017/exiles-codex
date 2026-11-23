# Armour (and Armour Break)

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What armour does
- Claim: Armour reduces damage from hits — by default only physical hits. Its reduction depends on hit size: strong vs small hits, weak vs big ones. It does nothing against damage over time (bleed, Corrupted Blood).
- Version: 0.5.5.9
- Volatility: stable
- Source: game keywords "Armour", tier 2; [Mobalytics Armour](https://mobalytics.gg/poe-2/guides/armour) (updated 2025-09-11), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Formula
- Claim: Damage reduction = Armour ÷ (Armour + 10 × physical hit damage). E.g. armour 5× the hit → 33.3% reduction.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Armour](https://mobalytics.gg/poe-2/guides/armour), tier 3, retrieved 2026-11-17
- Confidence: conflict — older sources say 12× → see kb/04-conflicts.md "Armour formula constant"
- Notes: Physical damage reduction is capped at 90% ([INFERRED] from PoE1 wiki and old poedb text; not yet seen on a PoE2 tier-2 page — verify). Some mechanics let armour apply to other damage types (e.g. "X% of Armour also applies to Elemental Damage" mods; [poe2wiki Receiving damage](https://poe2wiki.net/wiki/Receiving_damage)).

## Armour movement-speed penalty
- Claim: Wearing armour slows you. Body armour: pure Str −5%, hybrid Str/Dex or Str/Int −4%, pure Dex or Int −3%. Shields: pure Str −3%, hybrid −1.5%, pure Dex/Int none. Only body armour and shields count.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Armour Movement Penalties", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: relevant for the clear-speed criterion in claude/starter-decision-sheet.md.

## Item armour
- Claim: Stats that reference "item armour" use the number shown on the item (its quality and local mods), not your global armour modifiers.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Item Armour", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Armour Break (offence)
- Claim: Some effects lower a target's armour. At 0 it's "Fully Broken" for 12 s (4 s on players): no armour benefit, and non-players take 20% increased physical hit damage. Players break 3× as much armour on Normal monsters and 2× on Magic. Breaking below 0 gives negative armour (more phys damage taken), capped at the enemy's base armour.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Armour Break", "Armour Break below 0", tier 2; [poe2wiki Armour Break](https://www.poe2wiki.net/wiki/Broken_armour), tier 2; retrieved 2026-11-17
- Confidence: confirmed (definition); single-source for numbers (game data)
- Related debuffs: Sundered Armour — on fully broken enemies, +20% more phys hit damage taken, stacks with Fully Broken. Riven Armour — stores 5% of a hit's pre-mitigation phys and adds it to your later attack hits; Riven/Sundered targets can't be broken further. Crushed — −15% physical damage reduction, can go negative. Armour break doesn't affect bleed damage. (All game keywords, single-source.)
