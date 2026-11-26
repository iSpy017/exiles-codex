---
title: Critical Hits
status: needs-1.0-check
tracker_topic: "Critical strikes"
tracker_note: "needs-1.0-check (0.5.x; GGG says crit chance leaves the passive tree in 1.0; monster crit conflict resolved by game data 2026-11-23)"
---

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Base critical damage bonus
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
A crit deals +100% damage (200% of the hit) by default for players and minions.
- src: poe2db:Keywords, tier 2; poe2wiki Critical hit [S609], tier 2; Mobalytics Critical Hits [S058], tier 3; retrieved 2026-11-17
- notes: "Critical Damage Bonus" = PoE1's crit multi. It's a separate multiplier from every other damage multiplier.


## Monster crit damage
@ v=0.5.x vol=may-change conf=conflict date=2026-11-17
Monsters crit for less than players. Exact value disputed.

- src: poe2wiki says 40% less bonus; Mobalytics says default 30% — see kb/04-conflicts.md
- conf: conflict (unresolved)

## Base crit chance source
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
Attacks use the weapon's crit chance; spells (and some other skills) use the chance listed on the skill and ignore the weapon.

- src: poe2db:Keywords, tier 2; poe2wiki Critical strike chance [S683], tier 2; retrieved 2026-11-17

## Increased crit chance is relative to base
@ v=0.5.x vol=stable conf=single-source date=2026-11-17
"% increased Critical Hit Chance" multiplies the base: 100% increased on a 7% base = 14%.
- src: poe2wiki Critical strike chance [S683], tier 2, retrieved 2026-11-17
- notes: low-base weapons gain little from increased crit — base matters most.


## Scaling crit damage
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Crit damage bonus scales with flat "+X% to Critical Damage Bonus" (added first), then "increased", then "more" modifiers.

- src: poe2wiki Critical hit [S609], tier 2; Maxroll Damage Scaling [S033], tier 3; retrieved 2026-11-17
- conf: confirmed (order of flat first: wiki only)

## DoT can't crit; ailments from crits benefit
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Damage over time can't crit, but damaging ailments applied by a crit are calculated from the crit's damage, so they're bigger.

- src: Mobalytics Critical Hits [S058], tier 3, retrieved 2026-11-17
- conf: single-source (consistent with [[mechanics/hits-vs-dot]] "ailment built from final hit")

## Crit prevention wins
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
"Can't crit" effects (e.g. Resolute Technique) override "always crit" effects.

- src: poe2wiki Critical hit [S609], tier 2, retrieved 2026-11-17

## Lucky crit
@ v=0.5.x vol=stable conf=single-source date=2026-11-17
Lucky means roll twice and keep the better result.

- src: poe2db:Keywords, tier 2, retrieved 2026-11-17

## Bifurcated crits
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
With bifurcated crits, the crit chance is rolled twice. One success = normal crit. Two successes = crit damage bonus applied twice to that hit. Luck applies to each roll separately.

- src: poe2wiki Critical Hits [S682] and poe2wiki Crit [S681], tier 2, retrieved 2026-11-17

## Not yet sourced
- Crit chance cap (95%?) — only found in a tier-5 doc. [INFERRED] likely capped like PoE1; verify.
- Accuracy overcap → crit (Amazon) — see [[mechanics/accuracy]].
