---
title: Storm Shaman — own build, core design (1.0 skeleton)
status: partial
tracker_topic: "Own build — Storm Shaman (design)"
tracker_note: "partial (1.0 skeleton; lock on patch day; engine gem numbers now in gems/elemental-caster-gems)"
---

Status: partial — design skeleton, written 2026-11-23 before the 1.0 patch notes. Every gem/node fact is 0.5.x-era PoE2DB data unless tagged 1.0; lock links and nodes on patch day (checklist at the end). Built from first principles — no build guides used.
Companion docs: [[builds/storm-shaman-levelling]] (campaign) · [[builds/storm-shaman-pivot]] (maps, farm pivot, AFK char).
PoE2DB source = local crawl of 2026-11-23 ([[notes/tools/poe2db-corpus]]), tier 2. Cited as "PoE2DB <Page>".

## 1. Farm pick (provisional): Ritual
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Ritual is the pick. Ritual Altars are where omens come from (PoE2DB Ritual item list shows Ritual dropping Whittling, Sinistral/Dextral Erasure, Alchemy, Coronation, Exaltation, Greater Exaltation/Annulment and more), and omens are endgame crafting tools that keep demand all league. The King in the Mists, Ritual's boss, has his own unique table (Pragmatism, The Burden of Shadows, Beetlebite, From Nothing, Ingenuity).
- src: poe2db:Ritual, tier 2, crawl 2026-11-23; value pattern [[economy/value-retention]]; omen effects [[crafting/omens]]
- v: 0.5.x data
- conf: confirmed (omen source); farm profitability [INFERRED]: no 1.0 price data exists — re-rank on poe.ninja days 2–3 per [[strategy/league-start-framework]] ("don't marry your farm")
- notes: Expedition stays the early-currency side farm you liked. Conquerors (castles, commanders) runs alongside any farm; its endgame rules aren't published yet ([PoE2DB Conquerors of Wraeclast league](https://poe2db.tw/us/Conquerors_of_Wraeclast_league) = reveal text only).


## 2. What the farm demands → build requirements
- Ritual: monsters spawn around you inside a confined circle; needs AoE + defence ([[strategy/league-start-framework]], creator view, tier 3/5).
- Your sheet: clear speed 25%, farm fit 20%, defence by red maps 15%, campaign speed 15%, low-thinking 10%, patch risk 10%; gates incl. 5-div T15 test (claude/starter-decision-sheet.md).
- Patch-proof rules [INFERRED from 1.0 statements]: (a) no crit dependence — crit chance leaves the tree ([[strategy/dev-statements-1.0-balance]]); (b) scale through things outside the tree — gem levels and weapon +levels — because the tree is overhauled ([[strategy/official-1.0-reveal]]); (c) no lineage gem or chase unique; (d) class not on the rework list (you excluded Mercenary, Infernalist, Blood Mage, Chayula; Shadow out).

## 3. Engine choice
| Concept | Act-1 start | Crit-free | Ritual fit | Clear | Verdict |
|---|---|---|---|---|---|
| **Spark + Flame Wall → Tornado/Thunderstorm (Druid)** | yes (both tier 1) | yes (DoT + hits) | high (pull + zones in circle) | good (Spark) | **pick** |
| Ice Nova caster (Sorceress) | yes (tier 1) | yes | high (self nova) | medium | Sorceress flagged as GGG's least-liked core loop → change risk ([[strategy/dev-statements-1.0-balance]]) |
| Shockwave Totem warrior | tier 3 | yes | high | low | Warrior getting new mechanics in 1.0 → risk; clear too slow for the 25% weight |
| Bow lightning (Ranger) | yes | partly | medium | high | that's the existing incumbent — not an own build |
- Gem tiers from [PoE2DB Skill Gems](https://poe2db.tw/us/Skill_Gems), tier 2. Scoring of the rows is [INFERRED] (my judgement against section 2).

## 4. The engine (how the damage works)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
**Spark** (tier 1, lightning spell) fires 4–9 erratic projectiles that run along the ground — the clear skill. **Flame Wall** (tier 1) ignites everything in its area and adds fire damage to projectiles fired through it by you and allies; up to 3 walls. **Tornado** (tier 11) is a physical damage-over-time storm that pulls enemies in, and absorbs any elemental ground surface it overlaps, dealing extra DoT of that element (6.1–292.2/s per element vs 3–146.1/s base phys, gem L1–20). **Thunderstorm** (tier 5) drops a lightning storm that Drenches enemies: 50% more chance to be shocked, 25% more freeze buildup.
- Loop [INFERRED from the gem texts]: maps — wall in front, Spark through it (lightning + added fire, ignites from the wall). Ritual/bosses — Flame Wall + Tornado on top (Tornado absorbs ignited ground → fire DoT added), Thunderstorm for shock, curse with Elemental Weakness (tier 7, −40 to −59% ele res). Tornado damage is DoT, so it can't crit and penetration doesn't help it — exposure and curses do ([[mechanics/exposure-penetration]]).
- Open → narrowed (crawl check 2026-11-27): Tornado absorbs the debuff of an **Elemental Ground Surface** it overlaps and then deals extra damage of that element (poe2db:Tornado, tier 2). Flame Wall's own text only says the wall ignites what's inside it and adds fire to projectiles through it; it never mentions creating Ignited Ground, and the Ignited Ground page's 18 references don't include Flame Wall (poe2db:Flame_Wall, poe2db:Ignited_Ground, tier 2, crawl 2026-11-23). So "Tornado absorbs Flame Wall" is **not supported by game data** [INFERRED from absence: still test in game, but don't plan on it].
- Gear that fixes it without ground: four level-42 unique rings (Runes of Aldur, 0.5) make Wind skills such as Tornado count as boosted by a ground type — Berek's Respite (Ignited, plus fire/lightning res), Berek's Grip (Shocked, cold/lightning res), Berek's Pass (Chilled, fire/cold res), The Taming (all elemental res; Wind skills count as boosted by Ignited, Shocked **and** Chilled Ground at once, and can be boosted by several surfaces) (data/unique_mods.csv; poe2db pages of each ring, tier 2, crawl 2026-11-23). One The Taming alone covers all three elements; or Respite + Grip for fire + lightning [INFERRED: assumes "counts as boosted" grants the same extra-element damage as absorbing; check the in-game tooltip]. Field report: Spud the King's 0.5.5 Tornado Druid wore The Taming and says Tornado then had fire, lightning and cold effects ([S750] ~15:35–15:52, tier 5, video 2026-11-24). All 0.5 data; recheck at 1.0.

- src: poe2db:Spark, poe2db:Flame_Wall, poe2db:Tornado, poe2db:Thunderstorm, tier 2, crawl 2026-11-23
- conf: single-source (game-data text)

## 5. Class & ascendancy: Druid → Shaman
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Shaman (Druid) nodes: Turning of the Seasons — enemies in your Presence have Exposure, and you gain 10% of damage as extra damage of a random element; Reactive Growth — 10% less elemental damage taken plus adaptations to the highest element of each hit you take (10% less per matching adaptation, max 3); Avatar of Evolution — doubles adaptation effect, 5 s duration, takes 5% of physical as each element; Druidic Champion — every 2 Rage grants 1% more spell damage; Furious Wellspring — no inherent Rage loss, regenerate 6% max Rage/s, +7 max Rage but skills cost +5 Rage; Sacred Flow — +40 Spirit per empty charm slot; Bringer of the Apocalypse — grants Apocalypse (builds Glory from elemental hits, then triggers elemental disasters for 12 s).
- Why Shaman over Oracle [INFERRED]: Presence exposure is exactly the Ritual geometry (spawns all around you) and boosts DoT, which penetration can't; Reactive Growth is a defence layer that needs no gear. Oracle's best nodes lean on crit ("Forced Outcome: Inevitable Critical Hits") — against rule (a) ([PoE2DB Oracle](https://poe2db.tw/us/Oracle)).
- Point order [INFERRED]: Turning of the Seasons (1–2) → Reactive Growth (3–4) → Druidic Champion + Furious Wellspring (5–6) → Avatar of Evolution or Sacred Flow (7–8). Risk: Furious Wellspring's +5 Rage cost per skill may drain the Rage that Druidic Champion needs — test in 0.5.5 before committing.
- Rage budget for that risk [INFERRED arithmetic from node/keyword text]: with Furious Wellspring, max Rage ≈ 37 (30 base + 7; +3 more from the small Rage node) and regen 6%/s ≈ 2.2–2.4 Rage/s (more with mana-regen-rate mods), while every cast costs +5 Rage — so regen alone pays for only about one cast every 2 s. The gap has to come from Rage on hit: Druidic Prowess (max 3 stacks) makes spell hits grant 3 Rage per stack, and only one hit per 0.5 s can grant Rage, so at most ≈ 18 Rage/s at 3 stacks — enough for ~3 casts/s, but nothing at 0 stacks. Prowess sources in the 0.5 crawl are all Talisman-bound: Amor Mandragora (unique Changeling Talisman, level 1) and the Legacy of Amor Mandragora rune (Talismans, level 65) give 1 Prowess per 20 Rage spent; Ancient Rune of Animosity (Talismans, level 30) gives 2 Prowess on Heavy Stunning a Rare/Unique (poe2db:Amor_Mandragora, poe2db:Legacy_of_Amor_Mandragora, poe2db:Ancient_Rune_of_Animosity, tier 2). With Wellspring each cast spends 5 Rage, so Amor Mandragora would add a stack every 4 casts [INFERRED arithmetic] — but a Talisman puts you in its animal form, and whether spells work while shapeshifted is still unknown ([[mechanics/shapeshifting]], poe2db:Furious_Wellspring, poe2db:Druidic_Prowess, tier 2, crawl 2026-11-23). Whether a cast with too little Rage is blocked is also unstated; by analogy with mana (a support exists that lets skills ignore insufficient mana) it probably is [INFERRED]. Plan: Druidic Champion only pays off with a steady Rage source too (Rage otherwise drains), so the key test in 0.5.5 is Amor Mandragora: can Spark/Tornado be cast while its form is active? If not, skip Furious Wellspring (and Druidic Champion has no steady Rage source).
- Attributes: Druid starts 11 Str / 7 Dex / 11 Int ([[classes/index]]); Spark/Flame Wall need Int, Tornado/Thunderstorm need Str + Int (PoE2DB gem pages) — natural fit.

- src: poe2db:Shaman, poe2db:Apocalypse, tier 2, crawl 2026-11-23; rework list [[builds/starter-archetypes]]
- v: 0.5.x (Druid ascendancies are not on the 1.0 rework list)
- conf: single-source (game data)

## 6. Defence plan (by [[builds/defence-checklist]])
- Res capped (Shaman +3% all ele; Reactive Growth 10% less ele taken on top). Primary layer: armour + ES hybrid (Str/Int side) [INFERRED]. Recovery: TBD on 1.0 tree. Stun/freeze: Thawing + Stone charms unless Sacred Flow spirit is wanted ([[mechanics/charms]]). Arctic Armour (spirit tier 4, 30 spirit) bursts cold on melee hitters ([PoE2DB Arctic Armour](https://poe2db.tw/us/Arctic_Armour)).

## 7. Patch-day checklist
- [ ] Spark, Flame Wall, Tornado, Thunderstorm, Elemental Weakness numbers and tiers unchanged?
- [ ] Support rebalance: Lightning/Fire Penetration merged into Elemental Penetration (1.0 gem: 30% pen, hits only — [PoE2DB Conquerors gems](https://poe2db.tw/us/Conquerors_of_Wraeclast_gems)); re-pick links.
- [ ] Shaman nodes unchanged? Rage interaction (Druidic Champion vs Furious Wellspring cost).
- [ ] Ailments "harder to apply but stronger" (secondhand) — affects ignite/shock reliance.
- [ ] Ritual still in 1.0 atlas and omens still Ritual-sourced; re-rank farm with day 2–3 prices.
- [ ] Gates 1–4 on the decision sheet; score vs the other candidates.
