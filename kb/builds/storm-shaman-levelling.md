---
title: Storm Shaman — campaign levelling (super-sweat skip route)
status: partial
tracker_topic: "Own build — Storm Shaman levelling"
tracker_note: "partial (Acts 1–4 0.5 data; Acts 5–6 pending; Thunderstorm Drench cap needs gem 18 before high maps)"
---

Status: partial — Acts 1–4 from 0.5.x data; Acts 5–6 placeholders until 1.0 notes. Design → [[builds/storm-shaman]]. Pivot → [[builds/storm-shaman-pivot]].
Rule for this doc: gem levels/rewards are 0.5.x; supports are PoE2DB's own per-gem recommendations (0.5.x) and WILL be re-picked after the 1.0 support rebalance.

## Gem timeline (when each piece comes online)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
| Skill | Tier | Earliest source (0.5) | Gem level → char level |
|---|---|---|---|
| Spark | 1 | Act 1 "Reaching Clearfell" uncut skill L1 | L1 → any |
| Flame Wall | 1 | any L1 uncut skill drop (Act 1) | L1 → any |
| Thunderstorm | 5 | Act 1 "The Trail of Corruption" uncut skill L5 (ilvl 15) | L5 → 14 |
| Arctic Armour (spirit) | 4 | uncut spirit L4 (drop level 11) | L4 → 10 |
| Elemental Weakness | 7 | Act 2 "The Trail of Corruption" uncut skill L7 (ilvl 23) | L7 → 22 |
| Tornado | 11 | Act 3 "Treasures of Utzaal" uncut skill L11 (ilvl 41) | L11 → 41 |
- src: tiers poe2db:Skill_Gems, tier 2, crawl 2026-11-23; quest rewards [[campaign/quest-rewards]] (PoE2DB Quest, tier 2); drop levels [[gems/uncut-gems]]; char levels [[gems/gem-levels]]
- conf: single-source per row
- notes: Tornado is the late piece (~level 41). Don't spend the Act 3 L11 uncut on anything else. Uncut L11 can also drop from drop level 42 ([[gems/uncut-gems]]).


## Starting links (0.5 recommendations, re-pick at 1.0)
@ v=0.5 vol=? conf=single-source date=2026-11-23 fill=v missing=vol
- Spark: Pierce I / Prolonged Duration I / Zenith I (tier 1) → Pierce II etc. (tier 3) → Lightning Exposure, Rapid Casting II (tier 4).
- Flame Wall: Prolonged Duration I / Fortress I / Zenith I → Fire Exposure (tier 4) → Ignite III (tier 5).
- Tornado: Magnified Area I / Prolonged Duration I / Slow Potency → Swift Affliction II (tier 3) → Advancing Storm (tier 4).
- Thunderstorm: Magnified Area I / Prolonged Duration I / Coursing Current → Lightning Penetration (tier 2 — merged into Elemental Penetration in 1.0) → Lightning Exposure.
- Support level gates: support L2 from drop level 16 (Act 2 start), L3 from 33 (Act 3 start) ([[campaign/quest-rewards]]).

- src: "Recommended Support Gems" on each gem page (poe2db:Spark, poe2db:Flame_Wall, poe2db:Tornado, poe2db:Thunderstorm), tier 2, crawl 2026-11-23
- conf: single-source; usefulness for this build [INFERRED]

## Gear breakpoints (caster: follow +levels, not weapon base)
@ v=0.5 vol=? conf=? fill=v missing=vol,conf
- Staff: +2 all spells from ilvl 5, +3 from 25; one element +2 from 18, +3–4 from 36. Wand: +1 all at 5, +2 at 25. Amulet: +1 all spells at 10. Item level ≈ area level in the campaign.
- src: [[builds/levelling-gear]] (game data mods.json, tier 2)
- Practical [INFERRED]: check vendors at areas 18, 25, 36 for a staff/wand with +lightning or +all spell levels — that's the damage upgrade, not the base.
- Boots movement speed: 10% (1) · 15% (16) · 20% (33) · 25% (46) ([[builds/levelling-gear]]).
- Act 1 vendors cap at ilvl 15 → buy Grand flasks early Act 2 ([[builds/levelling-gear]], Maxroll 0.2-era).


## Act checklists (take / skip on the skip route)
Format: what to take, why. All rewards 0.5.x ([[campaign/permanent-rewards]]).
- **Act 1:** Clearfell quest gem (Spark). Beira +10% cold res (needed: cold 30–40% for Count Geonor). King in the Mists +30 spirit → Arctic Armour. Trail of Corruption L5 → Thunderstorm. Crowbell / Una's Lute points only if on the path. Salvage Bench (Artificer's shards).
- **Act 2:** L5 skill from Earning Passage → spare (or second Spark level). Trail of Corruption L7 → Elemental Weakness. Kabala + Dekhara points. Spires of Deshar +10% lightning res (easy to miss). Balbala's Barya → Sekhemas → ascendancy points 1–2: **Turning of the Seasons**. Fire res before Rudja.
- **Act 3:** Treasures of Utzaal L11 → **Tornado** (≈ char 41). Ignagduk +30 spirit. Blackjaw +10% fire res. Xyclucian key → Trial of Chaos → points 3–4: **Reactive Growth**. Venom vial: 30% elemental ailment threshold [INFERRED best pick for an elemental-defence Shaman]. Skip the Sacrificial Heart if it doesn't drop fast.
- **Act 4:** L12 skill gems from Blind Beast / Shrike / Whakapanu / Abandoned Prison → level Tornado/Spark. Ring choice (res), amulet choice (Int/attribute). Yama tattoo → +5% to your weakest res. Omniphobia/Ancestors points if near the path (disputed sources → [[conflicts]]).
- **Acts 5–6 (1.0):** unknown — 24 areas, 18 bosses ([[campaign/act-5]]). Expect the Interlude rewards (spirit, points, life) to move here; fill on patch day.
- **Conquerors campaign missions:** 20+ missions / 70+ POIs ([[strategy/official-1.0-reveal]]). Take the ones on the path; gold matters for troops ([[economy/gold]]).

## Play pattern while levelling [INFERRED from gem text]
- Acts 1–2: drop a Flame Wall ahead, spam Spark through it. Bosses: wall under the boss + Spark.
- From ~22: Elemental Weakness on bosses. From ~41: Tornado onto the wall for bosses and big packs; Thunderstorm when shock helps.
- Resist checkpoints: cold before Geonor, fire before Rudja and the Azak Bog boss ([[builds/levelling-gear]]).
