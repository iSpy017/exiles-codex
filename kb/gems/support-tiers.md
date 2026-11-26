---
title: Support Gem Tiers
status: done
tracker_topic: "Support tiers"
tracker_note: "done (0.5.5.9; 1.0 support rebalance)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17). Re-check at 1.0 (reveal notes: big support rebalance, elemental penetration supports merged — see poe2-1.0-launch-brief.md).

## Tiers 1–5
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Support gems have tiers 1–5; an Uncut Support Gem of level ≥ the tier is needed to engrave one. Many supports come in numbered versions (I/II/III) at increasing tiers, e.g. Pierce I tier 1 → Pierce III tier 5; Chain I tier 1; Fork tier 3.
- src: RePoE skill_gems.json `crafting_level` (repoe-fork/poe2 [S002]), tier 2; poe2wiki Engraving [S614], poe2wiki List of support gems [S625], poe2wiki Pierce [S713], poe2wiki Chained [S675], tier 2; retrieved 2026-11-17
- notes: multi-tier supports were introduced in 0.3.0 ([poe2wiki Spirit Gem](https://www.poe2wiki.net/wiki/Spirit_Gem) version history).


## Counts (game data, engravable supports)
@ v=0.5.5.9 vol=? conf=single-source date=2026-11-17 missing=vol
- Tier 1: 84 · Tier 2: 107 · Tier 3: 109 · Tier 4: 80 · Tier 5: 71. Plus 191 tier-0 supports — lineage (88) and supports only granted by items/ascendancies, not engravable.
- Uncut support gem L2 drops from item level 16, L3 33, L4 45, L5 55 → tier-5 supports only realistically from area ~55+ ([[gems/uncut-gems]]).

- src: RePoE skill_gems.json + base_items.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data); tier-0 interpretation [INFERRED] from lineage count = 88 of them.

## Categories
@ v=0.5.x vol=? conf=single-source date=2026-11-17 missing=vol
Each support has a Category (e.g. Pierce, Chain, Fork, Herbalism); you can't socket two supports of the same category in one skill (so Pierce I + Pierce III can't share a skill).

- src: poe2wiki Spirit Gem [S724], poe2wiki Pierce [S713], tier 2, retrieved 2026-11-17

## Engraving support list
- Full engravable list with tiers lives in game data (skill_gems.json, gem_type "support", crafting_level 1–5). Not copied here to keep the doc small; pull on demand.
