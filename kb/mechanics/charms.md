---
title: Charms
status: done
tracker_topic: "Charms"
tracker_note: "done (0.5.5.9; 13 bases; slot-cap conflict open; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17; base list added batch 17). Re-check at 1.0.

## What charms are
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Charms are equipped trinkets that fire a defensive effect automatically when their condition is met. Like flasks they need charges; kills give charges equal to half the monster's Power; checkpoints and wells fully refill them.

- src: RePoE poe2 keywords.json "Charms" [S002], tier 2 game data; poe2db:Keywords, tier 2; retrieved 2026-11-17
- conf: single-source (same game text)

## Charm bases (13)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
13 charm bases. All hold 40 charges except Golden (80). Duration, charges per use and required level below; trigger → effect paraphrased.

| Charm | Lvl | Charges/use | Duration | Trigger → effect |
|---|---|---|---|---|
| Ruby | 5 | 20 | 4 s | hit by Fire → +25% fire res |
| Sapphire | 5 | 20 | 4 s | hit by Cold → +25% cold res |
| Topaz | 5 | 20 | 4 s | hit by Lightning → +25% lightning res |
| Stone | 8 | 20 | 3 s | when Stunned → can't be Stunned |
| Silver | 10 | 20 | 3 s | when Slowed → MS unaffected by slows |
| Thawing | 12 | 40 | 3 s | when Frozen → freeze immunity |
| Staunching | 18 | 30 | 3 s | when Bleeding starts → bleed immunity |
| Antidote | 24 | 20 | 3 s | when Poisoned → poison immunity |
| Dousing | 32 | 30 | 3 s | when Ignited → ignite immunity |
| Grounding | 32 | 30 | 3 s | when Shocked → shock immunity |
| Amethyst | 40 | 30 | 4 s | hit by Chaos → +18% chaos res |
| Cleansing | 40 | 20 | 3 s | when Cursed → curse immunity |
| Golden | 50 | 80 (all) | 1 s | on killing Rare/Unique → 15% increased item rarity |

- src: RePoE base_items.json (charges_max / charges_per_use / duration / drop_level), tier 2, retrieved 2026-11-17; poe2db:Charms (trigger/effect text and same numbers), tier 2, retrieved 2026-11-17
- conf: confirmed (numbers agree across both; effect text from PoE2DB)
- notes: Charge cost per use is high vs 40 max: Thawing uses all 40 (one use per refill). Charm res charms are the only cheap way to push a res past cap temporarily → [[mechanics/resistances]]. Ruby/Sapphire/Topaz = 3 slots' worth of elemental cover; ailment-immunity charms cover one ailment each.


## Slots
@ v=0.5.x vol=may-change conf=conflict date=2026-11-17
Keywords state a cap of 3 charm slots. Belts provide them — most belts roll (1–3) slots; some uniques/passives/items add more.
- src: game keywords "Charms" (cap 3), tier 2; poe2db:Charms, tier 2; poe2wiki Wide Belt [S734], tier 2; retrieved 2026-11-17
- conf: conflict — PoE2DB lists bonus-slot sources (e.g. Bijouborne +2, Elevore +1–2) that look like they exceed 3 → kb/04-conflicts.md
- notes: Keelhaul showed "Charm Slots: 1" in its 0.1.1 history, so slot rules have changed over patches.


## Charges and modifiers
@ v=0.5.x vol=? conf=single-source date=2026-11-17 missing=vol
Ancient Blooms (Vivid) give 5 charges to all charms. Siphon auras remove 3 charges from enemies' ... (as PoE2DB words it, "from enemies") every 3 s within 3.6 m — [INFERRED] wording unclear; monster mod "Siphons Flask Charges" drains charm charges (keywords). Charm quality: each 1% = 1% increased charm duration.
- Modifier families on items: reduced charges used (e.g. Ryslatha's Coil, Ornate Belt; Pragmatism removes cost), increased charges gained (Double Belt, Golden Obi, Bijouborne), increased duration (Soul Tether, Long Belt), increased effect on you (Woodland Aspect, Magnum Opus).
- src: poe2db:Charms, tier 2, retrieved 2026-11-17; Mobalytics unique belts list, tier 3
- notes: Warbringer's Turtle Charm (ascendancy) changes max block — see [[mechanics/block]]. Cast on Charm Use is a meta gem → [[gems/meta-trigger]].
