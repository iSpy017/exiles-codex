# Bleeding

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Basics
- Claim: Bleeding deals physical damage over time, 5 s default, and bypasses Energy Shield.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Needs an explicit bleed chance
- Claim: Damage doesn't create bleed chance; a stated source of bleed chance is required. Physical hit damage sets its strength.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Bleed damage
- Claim: Base bleed = 15% of the hit's pre-mitigation physical damage per second. Not changed by your damage modifiers afterwards. Enemy mitigation reducers (e.g. Shock) raise it; hit-only effects (e.g. Armour Break) don't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", tier 2; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Moving / Aggravated: +100%
- Claim: Bleed deals 100% extra damage while the target moves, or always if Aggravated. Aggravated bleeds count the target as moving until they expire. Each bleed is aggravated independently; an aggravate effect hits all bleeds currently on the target (unless stated) but not ones applied later.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Bleeding", "Aggravated Bleeding", tier 2; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: "On aggravating any bleeding" weapon effects only fire if the hit actually aggravates at least one not-yet-aggravated bleed (game keywords "Aggravating any Bleeding").

## Stacking
- Claim: [INFERRED] Only the strongest bleed deals damage, per the general "same-type debuffs don't stack" rule ([poe2wiki Poisonous](https://www.poe2wiki.net/wiki/Poisonous)). No bleed-specific tier 1–2 statement found; one untrusted site claims bleeds stack additively — not cited.
- Version: 0.5.x
- Volatility: may-change
- Confidence: [INFERRED]: general debuff rule; verify on poe2wiki Bleeding page.

## Corrupted Blood is not Bleeding
- Claim: Corrupted Blood is a separate physical DoT debuff (up to 10 per target) and ignores all bleed stats.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Corrupted Blood", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
