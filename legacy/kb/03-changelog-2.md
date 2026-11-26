# Changelog — part 2 (from 2026-11-26, agent pipeline)

Continues [[03-changelog]] (part 1 ends at batch 22). Newest first.

## 2026-11-26 — Batches 23–37 (agent pipeline)
- **How the work was done:** David asked for a multi-agent pipeline. The coordinator (Opus, main chat) splits work into batches. Sonnet workers draft docs in parallel from the local PoE2DB corpus ([[tools/poe2db-corpus]], crawl 2026-11-23, tier 2), each with a report listing every claim to check. Haiku inspectors re-check each claim and 3–6 spot checks against the corpus and give a y/n verdict; one "n" means FAIL and the batch goes back to its worker with the feedback. Only the coordinator publishes, after a PASS, merging with any existing doc. Live status board: https://claude.ai/artifact/CSC5SzfErnMn3PdE9TxZJs
- **Checked:** 1.0 patch notes still not out. Endgame stays deferred.
- **Rework rounds:** b24 (tagging, paraphrase, two wording issues), b25 (poise mapping marked [INFERRED], citations), b28 (twice: Zarokh drop readings, drop-disabled count 21 → 22), b30 (derive script pairing bug). All passed on re-check.
- **Safety incident:** one re-inspector ran a read-only shell command on David's computer, and two inspectors created stray one-minute reminders. Briefs now carry a hard rule: no device tools, no scheduled tasks. Reminders were not deleted on the agents' behalf; they are harmless.

### New docs
- gems/bow-attack-gems, -2, -3, -4 (b23, b31) — per-level bow attack gem tables (Ice Shot, Lightning Arrow, Lightning Rod and others). Done (0.5.x).
- classes/druid-ascendancies (b26) — Shaman and Oracle node text. Done (0.5.x).
- items/rune-effects, items/soul-core-idol-effects (b27) — augment effects by slot. Partial. Shaman's Wisdom of the Maji and a Fox Idol in body armour grant Bonded rune effects.
- gems/elemental-supports, gems/elemental-supports-damage (b32). Partial.
- gems/lineage-drop-sources (b29) — drop source and effect for 77 lineage supports; 11 show no source. Done (0.5.x).
- crafting/essence-table, crafting/essence-table-high (b24) — every essence tier × item class with ranges, mod levels and drop levels. Done (0.5.x).
- items/uniques-drop-sources (b28) — 111 uniques with a drop tag (22 "Drop disabled", 89 with a named boss or league); boss-by-boss lists. Partial.
- items/uniques-caster (b28) — 15 caster/elemental uniques (not a ranking). Partial.
- gems/spirit-gems, gems/spirit-gems-2 (b34) — 42 non-minion persistent gems with tier, spirit, weapon requirement, and level 1/10/20 numbers; only Blink, Convalescence, Eternal Rage and Sacrifice must be active in both weapon sets. Done (0.5.x).
- mechanics/shapeshifting, items/talismans (b37) — forms, Rage rules, sources and spenders, Glory, Apocalypse, Talisman bases and unique Talismans. Partial (Talisman → form map missing; spells in form [INFERRED]).

### Updated docs
- mechanics/monster-life (b30) — full L1–100 base-life table. Zarokh at 75 ≈ 4.0M life (was 3.6M).
- gems/quality (b29) — alternate gem quality not obtainable in 0.5.x. Status → done.
- items/quality (b27) — currency targets, drop levels and gold costs; per-use amount still unknown.
- crafting/essences (b24) — rewritten from game data; Ice = cold damage, Seeking = crit; corrupted essence table. Status → done. Older entries kept under "Carried over".
- crafting/desecration (b24) — bone table with item-level / mod-level restrictions, omens, Mark of the Abyssal Lord, Abyssal Eyes. Still partial.
- mechanics/chill-freeze, shock-electrocute, stun (b25) — PoE2DB numbers merged with older entries. Stun: heavy stun 2 s base; poise stats as the stun bar are [INFERRED]. Electrocute skills and supports listed. All still partial.

### Conflicts
- New: Lightning Rod chains (6 vs 8), Ice Shot shard damage, unique count 441 vs 448, Zarokh drops (3 readings), Aberration / Vessel drop lists, light-stun floor 15% vs 10%, Regrading Lens target, Druid spells-active blurb, shapeshift trigger, "Deferred" unique variants. → [[04-conflicts-2]]
- Resolved: Essence of Ice (game data), alternate gem quality (0.5.x: not obtainable).

### Unique mod tables (b35, b36) — published 2026-11-26 afternoon
- b35: 10 armour docs, 229 uniques + 4 Demigod items with no readable mods. Failed first inspection (worker wrongly said no "Drop disabled" pages exist — 22 do; 12 armour ones were missing) → fixed, re-check PASS. Coordinator removed a stray separator (The Coming Calamity) and an internal stat string (Vestige of Darkness).
- b36: 12 docs (weapons, caster weapons, quivers, rings, amulets, belts, jewels, flasks, charms). Failed first inspection on 4 tags; worker proved 3 boss tags and 1 league tag from item-page lines; Keelhaul rewritten from the 0.5.5 block. Coordinator replaced placeholder text on Fury of the King and Mageblood. PoE2DB has no unique daggers, claws, swords, axes or flails in 0.5.x.
- Usage limit hit mid-check (~11:45); resumed 15:05.

### Wave 5 (b38, b39)
- b39 minion base stats: gems/minion-stats, minion-stats-2 (new, partial) + mechanics/minions merged. Inspector FAIL on one untagged derived number and a rounding slip; coordinator fixed both. 2 new conflicts (minion res display vs data; Life vs Minion Life column).
- b38 runes, soul cores, idols: 12 docs, PASS. rune-effects and soul-core-idol-effects rewritten (old b27 partials fully superseded), 10 new part docs. Coordinator removed lore flavour text copied verbatim from Aldur rune pages (inspector missed it), filled empty Claim lines, fixed a cross-reference. Bonded granted only by Shaman's Wisdom of the Maji and a Fox Idol in body armour. 2 new conflicts.

### Wave 6 — endgame baselines (lean pipeline)
- David un-deferred endgame (2026-11-26): build 0.5.x baselines now, tag atlas-dependent facts, leave atlas passives until 1.0. KB storage rework parked (tracker row).
- Pipeline changes: lint.py (word count, empty fields, placeholders, 15-word prose copies, cited-line number check), inspectors check raw lines + 10 random doc rows, publish per batch, control docs per wave.
- Published: endgame/breach, delirium (b40), ritual, expedition (b41), abyss, trial-of-chaos (b42), pinnacle-bosses, pinnacle-bosses-2, uber-bosses (b43). All four failed first inspection (prices without league, overstated claims, wrong citations) and passed after one rework each; coordinator verified fixes against raw lines instead of re-inspecting.
- Rule applied: every price removed where PoE2DB names no league (link economy pages instead).
- Agent-rule breaches this wave: one inspector attempted device_bash (blocked), one listed scheduled tasks read-only.

### Wave 7 — atlas-dependent endgame (b44–b46)
- Published: endgame/atlas, waystones (b44), tablets (b45), vaal-temple, sekhemas-2 (b46). All partial, 0.5.x, atlas-dependent.
- Usage-saving change: no Haiku inspectors this wave; coordinator spot-checked 2–3 claims per batch against raw lines (lint covers cited-line numbers). Caught 1 error (waystone-quantity mod is prefix and suffix, not suffix only) and 2 bad links.
- Sekhemas additions published as a part-2 doc instead of rewriting the original.

### Follow-ups
- mechanics/recovery: Rage loss also pauses after taking damage (b37).
- builds/storm-shaman-levelling: Thunderstorm needs gem 18 before high maps.
- builds/kb-test damage doc: Zarokh 4.0M; cite mechanics/damage-calculation.
- classes/index: Master-at-Arms day one.
- mechanics/shapeshifting: 3 copied phrases flagged by lint — reword.
- Index additions are in [[00-index-2]] until the main index is next rewritten.
