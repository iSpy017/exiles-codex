# Bleeding

Version: game data 0.5.5.9 (researched 2026-11-17; stacking added 2026-11-25). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Basics
- Claim: Bleeding deals physical damage over time, 5 s default, and bypasses Energy Shield.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; [poe2wiki Bleeding](https://www.poe2wiki.net/wiki/Bleeding), tier 2, rev 132925, 2026-11-25
- Confidence: confirmed

## Needs an explicit bleed chance
- Claim: Damage doesn't create bleed chance; a stated source of bleed chance is required. Physical hit damage sets its strength.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2, 2026-11-17; poe2wiki Bleeding, tier 2, 2026-11-25
- Confidence: confirmed

## Bleed damage
- Claim: Base bleed = 15% of the hit's pre-mitigation physical damage per second. Not changed by your damage modifiers afterwards. Enemy mitigation reducers (e.g. Shock) raise it; hit-only effects (e.g. Armour Break) don't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), tier 2; poe2wiki Bleeding, tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3
- Confidence: confirmed

## Moving / Aggravated: +100%
- Claim: Bleed deals 100% extra damage while the target moves, or always if Aggravated (the bonus doesn't double up if an aggravated target also moves). Aggravated bleeds count the target as moving until they expire. Each bleed is aggravated independently; an aggravate effect hits all bleeds currently on the target (unless stated) but not ones applied later.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", "Aggravated Bleeding", tier 2; poe2wiki Ailment + Bleeding, tier 2; Mobalytics Ailments, tier 3
- Confidence: confirmed
- Notes: "On aggravating any bleeding" weapon effects only fire if the hit actually aggravates at least one not-yet-aggravated bleed (game keywords).

## Stacking: only the strongest bleed ticks
- Claim: Bleeds don't stack. Each instance keeps its own duration, but only the highest-damage one deals damage. So bleed = one big hit, not many fast hits.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Bleeding](https://www.poe2wiki.net/wiki/Bleeding) Mechanics section, tier 2, rev 132925, read via built-in browser 2026-11-25
- Confidence: confirmed (bleed-specific wiki statement + general "same-type debuffs don't stack" rule)
- Notes: replaces the earlier [INFERRED] entry. The untrusted "stacks additively" claim stays uncited.

## Rupture, Blood Loss, Incision
- Rupture: a ruptured bleed deals its damage faster (no number on the page).
- Blood Loss: running total of physical DoT damage (incl. bleed) a target has taken; shown as a dark red bar; some skills consume it.
- Incision: stacking debuff, +10% chance to inflict bleed per stack; all stacks removed when the target starts bleeding.
- Version: 0.5.x, volatility may-change
- Source: poe2wiki Bleeding, tier 2, 2026-11-25
- Confidence: single-source each

## Corrupted Blood is not Bleeding
- Claim: Corrupted Blood is a separate physical DoT debuff (up to 10 per target) and ignores all bleed stats.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Corrupted Blood", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
