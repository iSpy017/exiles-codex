# Chill & Freeze

Version: game data 0.5.5.9 (researched 2026-11-17; thresholds added batch 17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Chill
- Claim: Chill slows the target. Lasts 2 s on players, 8 s on non-players by default. Cold hits chill automatically (no chance needed). Magnitude depends on chilling damage vs the target's elemental ailment threshold, between 30% and a default max of 50%; a chill under 30% is ignored, so small hits can fail to chill.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Chill", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments) (durations), tier 3; retrieved 2026-11-17
- Confidence: confirmed (durations); single-source for 30%/50% (game data)
- Notes: "Slow magnitude" modifiers scale only the slow part of a debuff. Chilled Ground chills anyone standing in it, 6 s default.

## Freeze
- Claim: Freeze stops the target moving or acting, 4 s by default. Cold hit damage adds Freeze buildup; the target freezes at 100% buildup. Monster killed while frozen shatters (corpse destroyed).
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Freeze", "Frozen", tier 2; [Mobalytics Freeze](https://mobalytics.gg/poe-2/guides/freeze), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: "Increased Freeze Buildup" mods give no base chance to freeze on their own (Mobalytics). Blocking a hit doesn't stop its buildup (poe2wiki Freeze).

## Monster freeze/ailment thresholds (batch 17)
- Claim: For most monsters the ailment threshold equals max life; stronger monsters (some Rares, all Unique bosses) have a lower threshold relative to life. Exact per-level/per-boss values are not published. Buildup size is the hit's cold damage relative to that threshold; the exact formula "is not known" per poe2wiki.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Chill](https://mobalytics.gg/poe-2/guides/chill), tier 3; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment) and [Contributes](https://poe2wiki.net/wiki/Contributes), tier 2 (via search snippet); retrieved 2026-11-17
- Confidence: confirmed (2 sources agree on threshold ≈ max life for normal monsters); formula unknown
- Notes: PoE2DB's Stun/Keywords pages give no threshold values either (fetched 2026-11-17). Don't use the PoE1-derived formulas in tier-5 "research" dumps (glama.ai) — unverified for PoE2.

## Boss freeze resistance
- Claim: Each time a boss is frozen (directly or via buildup), its freeze threshold rises, then decays back to base over time.
- Version: 0.5.x
- Source: [poe2wiki Freeze](https://poe2wiki.net/wiki/Freeze) (search snippet), tier 2, retrieved 2026-11-17
- Confidence: single-source; decay rate/step size not stated

## Primed for Freeze
- Claim: Primed at 40% buildup (Normal), 50% (Magic), 60% (Rare), 70% (Unique).
- Version: 0.5.5.9
- Source: game keywords "Primed for Freeze", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Freeze on players
- Claim: Your elemental ailment threshold (default half max life) reduces Freeze buildup you take. Thawing Charm gives freeze immunity → [[mechanics/charms]].
- Version: 0.5.5.9
- Source: game keywords "Elemental Ailment Threshold", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Cold can't heavy stun
- Claim: Cold hits build Freeze instead and can't build Heavy Stun.
- Version: 0.5.x
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: → [[mechanics/stun]]

## Brittle (cold-related)
- Claim: Brittle gives hits up to +6% crit chance against the target, scaled by the cold damage of the hit that applied it; 4 s.
- Version: 0.5.5.9
- Source: game keywords "Brittle", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Still not sourced
- Numeric monster freeze thresholds; buildup decay rate; boss freeze-threshold step.
