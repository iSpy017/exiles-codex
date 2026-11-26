---
title: Budget Tiers (SSF → high budget)
status: done
tracker_topic: "Budget tiers (SSF → high)"
tracker_note: "done (cut-offs [INFERRED]; volatile)"
defaults: v=0.5.x vol=volatile
---

Version: 0.5.x / 0.5.5 sources (researched 2026-11-17). Volatility: volatile — divine-denominated costs only make sense inside one league and one week of it.
Status note: GGG has no official budget tiers. The tier boundaries below are my own working definitions [INFERRED], anchored on sourced examples.

## Working tier definitions [INFERRED]
@ v=0.5.x vol=volatile conf=inferred date=2026-11-17
| Tier | Rough cost | What it means |
|---|---|---|
| SSF / self-found | 0 trade | Everything from drops and your own crafts |
| Starter | ≤ 5 div to farm T15 | Matches the 5-div T15 test ([[strategy/league-start-framework]]) |
| Mid | ~5–50 div | Key uniques, good crafted weapon, starting juiced maps |
| High | 50 div → mirrors | Chase uniques, multi-step crafts, pinnacle/uber farming |

- src: tier boundaries mine [INFERRED]; 5-div gate from [[strategy/league-start-framework]] (video transcript, tier 3/5); examples below
- conf: [INFERRED] — reason: guides label builds "budget/SSF" vs "expensive/multi-mirror" without shared numbers, so I need fixed cut-offs to compare candidates

## Sourced anchors
@ v=0.5.5 vol=volatile conf=single-source date=2026-11-17 missing=src
- SSF/very-low-budget: Fubgun's whole 0.5.5 starter list is framed for SSF or very low budget ([Kami-labs summary](https://kami-labs.fr/en/path-of-exile-2/tier-list-league-start-poe2-0-5-5/), tier 5, 2026-09-02).
- Starter: Spark Stormweaver comes online with Adonia's at ~2–5 div (same source, 0.5.5, undated price).
- Starter → high on one build: Fubgun's Ice Shot Deadeye has an "early" variant for SSF/light trade; endgame gear (quiver/amulet crafts, Heart of the Well, Headhunter) is expensive ([Mobalytics Ice Shot Deadeye](https://mobalytics.gg/poe-2/builds/ice-shot-deadeye), tier 3, updated 2026-09-12).
- "Scales to multi-mirror": Twisters Gemling and Galvanic Tactician per Fubgun (Kami-labs, tier 5).
- High: Immortal Witchhunter Frostbolt loop — budget and expensive PoB snapshots exist; one user reported ~600 div for the expensive setup (poe2-1.0-launch-brief.md, Mobalytics Lazy Exile guide, tier 3 + user report tier 5).

- conf: single-source each

## SSF / self-found crafting baseline
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
A self-found rare usually goes: essence for the third affix and upgrade to rare → exalts for the 4th–5th affix → desecrate for the last affix.
- src: Mobalytics SSF Crafting [S090], tier 3, retrieved 2026-11-17; consistent with [[crafting/approach]] and [[crafting/desecration]]
- notes: 1.0 adds Reforging (Crimson Iron) and Blood Veils (reveal notes, secondhand) → may change the SSF path.


## Budget denomination drifts within a league
@ v=0.5 vol=volatile conf=single-source date=2026-11-10
In Runes of Aldur, 1 div went from 38 ex (day 1) to 61 (day 3), 406 (day 30) and 549 late. A "5 div" target on day 1 is a very different amount of exalts than on day 30.
- src: claude/reveal-notes-and-price-findings.md (poe.ninja pull, 2026-11-10), tier 4; [[economy/league-lifecycle]]
- v: 0.5 (Runes of Aldur)
- notes: practical rule [INFERRED]: on days 1–3 price starter upgrades in exalts, not divines.


## Where a starter's first divines should go (sourced lists)
@ v=0.5 vol=may-change conf=confirmed date=2026-11-17
The framework's first-upgrade list: weapon, +skill levels, spirit, movement speed, defences, resists. Maxroll's levelling stat priority: movement speed > resists > life > base damage > damage scaling > defences.
- src: [[strategy/league-start-framework]]; Maxroll Comprehensive League Start Leveling Guide [S032], tier 3; retrieved 2026-11-17
- v: 0.2–0.5
- conf: confirmed (lists agree on movement speed, resists, weapon)
- notes: per-candidate upgrade lists go in claude/starter-decision-sheet.md (gate 4) on patch day.


## Investment cut-off
@ v=1.0 vol=stable conf=single-source date=2026-11-17
Stop spending on the starter once the next divine doesn't make more money (e.g. 5 div that doubles clear: yes; 20 div for +10% damage when you already one-shot: no).
- src: [[strategy/league-start-framework]] (tier 3/5), retrieved 2026-11-17
- v: pre-1.0 opinion
