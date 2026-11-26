---
title: Armour (and Armour Break)
status: done
tracker_topic: "Armour"
tracker_note: "done (0.5.5.9; formula conflict open)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What armour does
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Armour reduces damage from hits — by default only physical hits. Its reduction depends on hit size: strong vs small hits, weak vs big ones. It does nothing against damage over time (bleed, Corrupted Blood).

- src: game keywords "Armour", tier 2; Mobalytics Armour [S053] (updated 2025-09-11), tier 3; retrieved 2026-11-17

## Formula
@ v=0.5.x vol=may-change conf=conflict date=2026-11-17
Damage reduction = Armour ÷ (Armour + 10 × physical hit damage). E.g. armour 5× the hit → 33.3% reduction.
- src: Mobalytics Armour [S053], tier 3, retrieved 2026-11-17
- conf: conflict — older sources say 12× → see kb/04-conflicts.md "Armour formula constant"
- notes: Physical damage reduction is capped at 90% ([INFERRED] from PoE1 wiki and old poedb text; not yet seen on a PoE2 tier-2 page — verify). Some mechanics let armour apply to other damage types (e.g. "X% of Armour also applies to Elemental Damage" mods; [poe2wiki Receiving damage](https://poe2wiki.net/wiki/Receiving_damage)).


## Armour movement-speed penalty
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Wearing armour slows you. Body armour: pure Str −5%, hybrid Str/Dex or Str/Int −4%, pure Dex or Int −3%. Shields: pure Str −3%, hybrid −1.5%, pure Dex/Int none. Only body armour and shields count.
- src: game keywords "Armour Movement Penalties", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: relevant for the clear-speed criterion in claude/starter-decision-sheet.md.


## Item armour
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Stats that reference "item armour" use the number shown on the item (its quality and local mods), not your global armour modifiers.

- src: game keywords "Item Armour", tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Armour Break (offence)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Some effects lower a target's armour. At 0 it's "Fully Broken" for 12 s (4 s on players): no armour benefit, and non-players take 20% increased physical hit damage. Players break 3× as much armour on Normal monsters and 2× on Magic. Breaking below 0 gives negative armour (more phys damage taken), capped at the enemy's base armour.
- Related debuffs: Sundered Armour — on fully broken enemies, +20% more phys hit damage taken, stacks with Fully Broken. Riven Armour — stores 5% of a hit's pre-mitigation phys and adds it to your later attack hits; Riven/Sundered targets can't be broken further. Crushed — −15% physical damage reduction, can go negative. Armour break doesn't affect bleed damage. (All game keywords, single-source.)
- src: game keywords "Armour Break", "Armour Break below 0", tier 2; poe2wiki Armour Break [S673], tier 2; retrieved 2026-11-17
- conf: confirmed (definition); single-source for numbers (game data)
