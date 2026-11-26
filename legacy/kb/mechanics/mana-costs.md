# Mana Costs & Mana Pool

Status: partial (0.5.x) — PoE2-specific statement of how cost multipliers stack not found (also absent from the PoE2DB corpus, checked 2026-11-25). Re-check at 1.0 (support rebalance).

## How costs are paid
- Claim: A skill's cost is paid every use, spread over a short window during activation. Cancelling mid-use (e.g. dodge roll) stops the rest of the cost but refunds nothing already paid.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Cost](https://www.poe2wiki.net/wiki/Cost), tier 2, rev 134828, read via built-in browser 2026-11-25
- Confidence: single-source

## Granted / triggered skills cost 0 by default
- Claim: Most granted skills and skills not cast directly (triggered skills, Blink) have a base cost of 0. Cost-adding effects (e.g. Archmage's extra % max mana) still give them a cost, unless the skill has no cost at all (e.g. Impending Doom's Doom Blast). Default attacks never have a cost.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Cost, tier 2, 2026-11-25; [PoE2DB Keywords](https://poe2db.tw/us/Keywords) ("Default Attacks never have any cost"), tier 2, crawl 2026-11-23
- Confidence: confirmed

## Upfront vs per-second costs
- Claim: An upfront cost is a flat amount ("3 Mana"); a per-second cost ("3 Mana per second") is not. Matters for "Take Mana Costs as Damage": upfront costs hit you, per-second costs become damage over time.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source (game keyword text)

## Support "Cost & Reservation Multiplier"
- Claim: Many PoE2 supports carry a "Cost & Reservation Multiplier" (e.g. Embitter, Heft 120%; Impending Doom 130%). Some supports show none.
- Version: 0.5.x
- Volatility: may-change (1.0 support rebalance)
- Source: support tooltips on [poe2wiki Receiving damage](https://www.poe2wiki.net/wiki/Receiving_damage) and [poe2wiki Cost](https://www.poe2wiki.net/wiki/Cost), tier 2, 2026-11-25; [poe2wiki List of support gems](https://poe2wiki.net/wiki/List_of_support_gems) (search snippet, 0.1.1g-era list), tier 2
- Confidence: confirmed (multiple tooltips)
- Notes: PoE2DB's Gem page has an early-access note saying supports had only a "Cost Multiplier"; current tooltips show "Cost & Reservation Multiplier" — treat the note as stale.

## Stacking several multipliers
- Claim: [INFERRED] Multipliers multiply together: final cost = base cost × M1 × M2 × … (two 120% supports = 144%, not 140%).
- Reason: this is the PoE1 rule ([GGG forum 1429554](https://www.pathofexile.com/forum/view-thread/1429554), PoE1, tier 5) and the multiplier is shown the same way in PoE2; tier-5 glama.ai research doc states the same. No PoE2 tier 1–2 statement found. Verify: socket two 120% supports on a skill with a known cost and read the tooltip.
- Version: 0.5.x
- Volatility: may-change
- Confidence: [INFERRED]: PoE1 rule + same stat name in PoE2

## Mana pool
- Claim: Characters start with 34 base mana at level 1 and gain +4 max mana per level. Intelligence gives +2 max mana per point (its only inherent bonus).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Mana](https://mobalytics.gg/poe-2/guides/mana) (dated 2026-11-13), tier 3, 2026-11-25; [PoE2DB Intelligence](https://poe2db.tw/us/Intelligence) (+2 mana per Int), tier 2, crawl 2026-11-23
- Confidence: confirmed for +2 per Int; single-source for 34 base and +4/level (an undated early-access Google doc, tier 5, also says +4 per level)

## Base mana regeneration
- Claim: Players regenerate 4% of max mana per second by default. Most "% increased mana regeneration rate" mods scale this base (e.g. 14% increased → 4.56%/s).
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Mana regeneration](https://www.poe2wiki.net/wiki/Mana_regeneration), tier 2 (search snippet); [Mobalytics Mana](https://mobalytics.gg/poe-2/guides/mana) and [Mobalytics Regeneration](https://mobalytics.gg/poe-2/guides/regeneration), tier 3; retrieved 2026-11-25
- Confidence: confirmed
- Notes: see [[mechanics/recovery]] for how regen and recovery-rate multipliers combine (conflict open).

## Sustain check (worked, for build docs)
- Regen/s = max mana × 0.04 × (1 + inc regen) × more regen. Compare with cost × casts/s.
- E.g. 400 mana, 40% inc regen → 22.4/s. A 20-mana spell at 1.5 casts/s costs 30/s → net −7.6/s, empty in ~53 s without leech/flasks. [INFERRED] arithmetic only; check the cost tooltip, which already includes support multipliers.

## Still to source
- PoE2 statement of multiplier stacking; cost efficiency vs reduced cost (both appear in data, e.g. Zenith II "increased Mana cost Efficiency"); Archmage/Mana Tempest cost interactions.
