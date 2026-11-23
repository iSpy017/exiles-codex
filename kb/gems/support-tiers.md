# Support Gem Tiers

Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17). Re-check at 1.0 (reveal notes: big support rebalance, elemental penetration supports merged — see poe2-1.0-launch-brief.md).

## Tiers 1–5
- Claim: Support gems have tiers 1–5; an Uncut Support Gem of level ≥ the tier is needed to engrave one. Many supports come in numbered versions (I/II/III) at increasing tiers, e.g. Pierce I tier 1 → Pierce III tier 5; Chain I tier 1; Fork tier 3.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE skill_gems.json `crafting_level` ([repoe-fork/poe2](https://github.com/repoe-fork/poe2)), tier 2; [poe2wiki Engraving](https://poe2wiki.net/wiki/Engraving), [poe2wiki List of support gems](https://poe2wiki.net/wiki/List_of_support_gems), [poe2wiki Pierce](https://www.poe2wiki.net/wiki/Pierce), [poe2wiki Chained](https://www.poe2wiki.net/wiki/Chained), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: multi-tier supports were introduced in 0.3.0 ([poe2wiki Spirit Gem](https://www.poe2wiki.net/wiki/Spirit_Gem) version history).

## Counts (game data, engravable supports)
- Tier 1: 84 · Tier 2: 107 · Tier 3: 109 · Tier 4: 80 · Tier 5: 71. Plus 191 tier-0 supports — lineage (88) and supports only granted by items/ascendancies, not engravable.
- Uncut support gem L2 drops from item level 16, L3 33, L4 45, L5 55 → tier-5 supports only realistically from area ~55+ ([[gems/uncut-gems]]).
- Version: 0.5.5.9
- Source: RePoE skill_gems.json + base_items.json, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data); tier-0 interpretation [INFERRED] from lineage count = 88 of them.

## Categories
- Claim: Each support has a Category (e.g. Pierce, Chain, Fork, Herbalism); you can't socket two supports of the same category in one skill (so Pierce I + Pierce III can't share a skill).
- Version: 0.5.x
- Source: [poe2wiki Spirit Gem](https://www.poe2wiki.net/wiki/Spirit_Gem), [poe2wiki Pierce](https://www.poe2wiki.net/wiki/Pierce), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Engraving support list
- Full engravable list with tiers lives in game data (skill_gems.json, gem_type "support", crafting_level 1–5). Not copied here to keep the doc small; pull on demand.
