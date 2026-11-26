---
title: Storm Shaman — early maps, Ritual pivot, AFK second character
status: partial
tracker_topic: "Own build — Storm Shaman pivot + maps"
tracker_note: "partial (costs TBD at launch)"
---

Status: partial — plan written 2026-11-23, pre-1.0. Prices are "TBD at launch" on purpose (no 1.0 economy yet). Design → [[builds/storm-shaman]]. Campaign → [[builds/storm-shaman-levelling]].

## Map checkpoints (from your framework)
- T1–6: push only — fix res, damage, movement ([[strategy/league-start-framework]]).
- T7: start reading drops; ilvl 71+ unlocks the second-best tiers of many mods ([[items/item-level]]).
- T11+: start crafting. T15: the "job done" gate — clears, sustains waystones, kills bosses, completes Ritual without dying.
- Every checkpoint: run [[builds/defence-checklist]].

## First upgrades (5-div T15 test, gate 4)
@ v=? vol=? conf=? date=2026-11-23 missing=v,vol
| # | Upgrade | Why | Unlock | Cost |
|---|---|---|---|---|
| 1 | Staff with +all spells / +lightning or +fire levels | Spells scale with gem level | +4 all at ilvl 55, +5–6 at 78; one element +5–6 at 55, +7 at 81 | TBD at launch |
| 2 | Amulet +2 all spell skills | Same | ilvl 41 (+3 at 75) | TBD |
| 3 | Res-capped armour/ES pieces | Gate 1 | 135% uncapped per element after −60% penalty (0.5) | TBD |
| 4 | Spirit: Solar Amulet (+10–15 implicit) or corrupted helmet (+20–30) | Run Arctic Armour + a second persistent | amulet drop 30 | TBD |
| 5 | Movement speed boots 25–30% | Clear weight 25% | ilvl 46 / 65 | TBD |
- Rule: on days 1–3 price upgrades in exalts, not divines ([[builds/budget-tiers]]).

- src: [[builds/levelling-gear]] (+levels table, game data), [[items/bases-implicits]] (Solar Amulet), [[items/corruption]] (helmet spirit), [[mechanics/resistances]], tier 2
- conf: unlock levels single-source (game data); ordering [INFERRED] from the scaling logic in [[builds/storm-shaman]] §4

## The pivot: starter → Ritual farmer
- Claim [INFERRED]: same class, same skills — the pivot is mostly gear and passive emphasis, not a reroll. Starter mode = Spark through Flame Wall for clear. Farmer mode = Flame Wall + Tornado (absorbs ignited ground) + Thunderstorm + Elemental Weakness inside the Ritual circle, with Presence exposure from Turning of the Seasons. Spark stays for mapping between altars.
- Reason: Tornado pulls monsters together and keeps damaging them in place, which matches Ritual's spawn-around-you waves ([[builds/storm-shaman]] §1–4). Your gate 3 (one character, respec at early maps) is met with no reroll.
- What changes: (1) passives shift from projectile/clear toward DoT, area, duration and defence once the 1.0 tree is known; (2) Tornado and Thunderstorm get the better links; (3) more spirit for a second persistent.
- Respec cost [INFERRED arithmetic]: ~40 points at L70 ≈ 85,800 gold, at L60 ≈ 62,000 (0.5 gold table, [[classes/respec]]). Budget the gold before the respec; Conquerors troops also cost gold ([[economy/gold]]).
- Sell from the starter: levelling staffs/wands with +levels (others levelling want them early) [INFERRED from the league-start demand pattern in [[strategy/league-lifecycle-pricing]]].

## Ritual play notes
@ v=? vol=? conf=single-source date=2026-11-23 missing=v,vol
- Ritual: kill monsters inside the circle, activate, kill the revived waves for Tribute, spend Tribute on Favours; Favours can be rerolled (costs Tribute) or deferred. Ritual Tablet adds altars to a map (10 uses).
- Build fit [INFERRED]: pre-place Flame Wall + Tornado before activating; Thunderstorm on the densest side; stand central so Presence exposure covers the ring.
- Endgame atlas/Ritual docs are still deferred to the 1.0 notes ([[coverage]]).

- src: poe2db:Ritual, tier 2, crawl 2026-11-23 (0.5.x)

## AFK second character (brief)
@ v=? vol=? conf=confirmed date=2026-11-23 missing=v,vol
1.0 commanders take troops and Waystones and clear maps for you in real time; up to three as the stronghold grows; they can also run Towers or hunt rewards with Tablets.
- Plan [INFERRED]: the Storm Shaman builds the stronghold; commanders are the "AFK" income lever. A second character only if commanders turn out to be capped per character — check on patch day ([[strategy/dev-statements-1.0-league]]: first commander after the first castle, the other two after the pinnacle).

- src: poe2db:Conquerors_of_Wraeclast_league (GGG reveal text), [[strategy/official-1.0-reveal]], tier 1
- conf: confirmed (announcement)

## Patch-day checks (this doc)
- [ ] +level mod tiers on staves/wands/amulets unchanged?
- [ ] Ritual altar/omen rules and Tribute in 1.0
- [ ] Commanders: per account or per character?
- [ ] Fill the cost column from poe.ninja days 1–3.
