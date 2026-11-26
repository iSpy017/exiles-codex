---
title: Mana Costs & Mana Pool
status: partial
tracker_topic: "Mana costs & regen (cost multiplier stacking)"
tracker_note: "partial (pool + 4% regen sourced; Int +2 mana confirmed by PoE2DB; upfront vs per-second costs; multiplier stacking [INFERRED] from PoE1)"
---

Status: partial (0.5.x) — PoE2-specific statement of how cost multipliers stack not found (also absent from the PoE2DB corpus, checked 2026-11-25). Re-check at 1.0 (support rebalance).

## How costs are paid
@ v=0.5.x vol=may-change conf=single-source date=2026-11-25
A skill's cost is paid every use, spread over a short window during activation. Cancelling mid-use (e.g. dodge roll) stops the rest of the cost but refunds nothing already paid.

- src: poe2wiki Cost [S680], tier 2, rev 134828, read via built-in browser 2026-11-25

## Granted / triggered skills cost 0 by default
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
Most granted skills and skills not cast directly (triggered skills, Blink) have a base cost of 0. Cost-adding effects (e.g. Archmage's extra % max mana) still give them a cost, unless the skill has no cost at all (e.g. Impending Doom's Doom Blast). Default attacks never have a cost.

- src: poe2wiki Cost, tier 2, 2026-11-25; poe2db:Keywords ("Default Attacks never have any cost"), tier 2, crawl 2026-11-23

## Upfront vs per-second costs
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
An upfront cost is a flat amount ("3 Mana"); a per-second cost ("3 Mana per second") is not. Matters for "Take Mana Costs as Damage": upfront costs hit you, per-second costs become damage over time.

- src: poe2db:Keywords, tier 2, crawl 2026-11-23
- conf: single-source (game keyword text)

## Support "Cost & Reservation Multiplier"
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
Many PoE2 supports carry a "Cost & Reservation Multiplier" (e.g. Embitter, Heft 120%; Impending Doom 130%). Some supports show none.
- src: support tooltips on poe2wiki Receiving damage [S719] and poe2wiki Cost [S680], tier 2, 2026-11-25; poe2wiki List of support gems [S625] (search snippet, 0.1.1g-era list), tier 2
- vol: may-change (1.0 support rebalance)
- conf: confirmed (multiple tooltips)
- notes: PoE2DB's Gem page has an early-access note saying supports had only a "Cost Multiplier"; current tooltips show "Cost & Reservation Multiplier" — treat the note as stale.


## Stacking several multipliers
@ v=0.5.x vol=may-change conf=inferred date=2026-11-25 missing=src
[INFERRED] Multipliers multiply together: final cost = base cost × M1 × M2 × … (two 120% supports = 144%, not 140%).
- Reason: this is the PoE1 rule ([GGG forum 1429554](https://www.pathofexile.com/forum/view-thread/1429554), PoE1, tier 5) and the multiplier is shown the same way in PoE2; tier-5 glama.ai research doc states the same. No PoE2 tier 1–2 statement found. Verify: socket two 120% supports on a skill with a known cost and read the tooltip.

- conf: [INFERRED]: PoE1 rule + same stat name in PoE2

## Mana pool
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
Characters start with 34 base mana at level 1 and gain +4 max mana per level. Intelligence gives +2 max mana per point (its only inherent bonus).

- src: Mobalytics Mana [S077] (dated 2026-11-13), tier 3, 2026-11-25; poe2db:Intelligence (+2 mana per Int), tier 2, crawl 2026-11-23
- conf: confirmed for +2 per Int; single-source for 34 base and +4/level (an undated early-access Google doc, tier 5, also says +4 per level)

## Base mana regeneration
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
Players regenerate 4% of max mana per second by default. Most "% increased mana regeneration rate" mods scale this base (e.g. 14% increased → 4.56%/s).
- src: poe2wiki Mana regeneration [S703], tier 2 (search snippet); Mobalytics Mana [S077] and Mobalytics Regeneration [S082], tier 3; retrieved 2026-11-25
- notes: see [[mechanics/recovery]] for how regen and recovery-rate multipliers combine (conflict open).


## Sustain check (worked, for build docs)
- Regen/s = max mana × 0.04 × (1 + inc regen) × more regen. Compare with cost × casts/s.
- E.g. 400 mana, 40% inc regen → 22.4/s. A 20-mana spell at 1.5 casts/s costs 30/s → net −7.6/s, empty in ~53 s without leech/flasks. [INFERRED] arithmetic only; check the cost tooltip, which already includes support multipliers.

## Still to source
- PoE2 statement of multiplier stacking; cost efficiency vs reduced cost (both appear in data, e.g. Zenith II "increased Mana cost Efficiency"); Archmage/Mana Tempest cost interactions.
