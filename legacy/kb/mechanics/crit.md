# Critical Hits

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Base critical damage bonus
- Claim: A crit deals +100% damage (200% of the hit) by default for players and minions.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; [poe2wiki Critical hit](https://poe2wiki.net/wiki/Critical_hit), tier 2; [Mobalytics Critical Hits](https://mobalytics.gg/poe-2/guides/critical-hits), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: "Critical Damage Bonus" = PoE1's crit multi. It's a separate multiplier from every other damage multiplier.

## Monster crit damage
- Claim: Monsters crit for less than players. Exact value disputed.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki says 40% less bonus; Mobalytics says default 30% — see kb/04-conflicts.md
- Confidence: conflict (unresolved)

## Base crit chance source
- Claim: Attacks use the weapon's crit chance; spells (and some other skills) use the chance listed on the skill and ignore the weapon.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; [poe2wiki Critical strike chance](https://www.poe2wiki.net/wiki/Critical_strike_chance), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Increased crit chance is relative to base
- Claim: "% increased Critical Hit Chance" multiplies the base: 100% increased on a 7% base = 14%.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Critical strike chance](https://www.poe2wiki.net/wiki/Critical_strike_chance), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: low-base weapons gain little from increased crit — base matters most.

## Scaling crit damage
- Claim: Crit damage bonus scales with flat "+X% to Critical Damage Bonus" (added first), then "increased", then "more" modifiers.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Critical hit](https://poe2wiki.net/wiki/Critical_hit), tier 2; [Maxroll Damage Scaling](https://maxroll.gg/poe2/getting-started/damage-scaling), tier 3; retrieved 2026-11-17
- Confidence: confirmed (order of flat first: wiki only)

## DoT can't crit; ailments from crits benefit
- Claim: Damage over time can't crit, but damaging ailments applied by a crit are calculated from the crit's damage, so they're bigger.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Critical Hits](https://mobalytics.gg/poe-2/guides/critical-hits), tier 3, retrieved 2026-11-17
- Confidence: single-source (consistent with [[mechanics/hits-vs-dot]] "ailment built from final hit")

## Crit prevention wins
- Claim: "Can't crit" effects (e.g. Resolute Technique) override "always crit" effects.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Critical hit](https://poe2wiki.net/wiki/Critical_hit), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Lucky crit
- Claim: Lucky means roll twice and keep the better result.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Bifurcated crits
- Claim: With bifurcated crits, the crit chance is rolled twice. One success = normal crit. Two successes = crit damage bonus applied twice to that hit. Luck applies to each roll separately.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Critical Hits](https://www.poe2wiki.net/wiki/Critical_Hits) and [poe2wiki Crit](https://www.poe2wiki.net/wiki/Crit), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Not yet sourced
- Crit chance cap (95%?) — only found in a tier-5 doc. [INFERRED] likely capped like PoE1; verify.
- Accuracy overcap → crit (Amazon) — see [[mechanics/accuracy]].
