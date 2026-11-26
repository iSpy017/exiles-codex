---
title: Deterministic vs gamble crafting (0.5 rules)
status: done
tracker_topic: "Deterministic vs gamble crafting"
tracker_note: "done (0.5 one-crafted-mod rule)"
---

Scope: the rules that limit crafting in 0.5, the standard crafting sequence, and which tools are deterministic. Costs → [[craft-costs]].

## The 0.5 rule: one crafted mod, one desecrated mod
@ v=0.5.0 vol=may-change conf=confirmed date=2026-11-17
Since 0.5, every method that guarantees a mod (essences, alloys, etc.) makes a "crafted" mod, and an item can hold only one crafted mod at a time. Desecrated mods are not crafted mods, but an item can hold only one desecrated mod. So you can't stack several essences on one item anymore.
- src: RePoE poe2 keywords.json "Crafted Modifiers" (one per item), tier 2 (game data 0.5.5.9); 0.5.0 patch-note text quoted in GGG forum thread 3932540 [S652], tier 5 (quote of tier-1 notes); Boostmatch 0.5 patch summary, tier 5; retrieved 2026-11-17
- v: 0.5.0+
- vol: may-change (likely revisited in 1.0)
- conf: confirmed (game text + quoted patch notes)
- notes: Crafted mods show in lighter blue. Before 0.5 (0.3–0.4), stacking a Perfect Essence on top of a regular one was a common weapon-craft step (forum post). Old guides using multiple essences are invalid for 0.5.


## Deterministic tools (control what you get)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Essence / Alloy (one guaranteed mod) · Desecration (choose 1 of 3 at the Well of Souls) · Fracturing Orb (lock a mod) · prefix/suffix omens (Sinistral/Dextral Exaltation, Coronation, Erasure, Annulment, Necromancy, Crystallisation) · Omen of Whittling (removes the lowest-level mod) · Hinekora's Lock (preview the next currency result) · Greater/Perfect orbs (raise the mod-level floor).

- src: game data (see [[currency-index]], [[omens]], [[essences]], [[desecration]]), tier 2; retrieved 2026-11-17
- conf: confirmed (individual effects); the grouping is mine

## Gamble tools
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Exalted / Chaos / Alchemy / Annulment without omens (random mod added or removed), Divine (values), Vaal Orb, Architect's Orb, Orb of Chance.

- src: game data, tier 2; retrieved 2026-11-17

## Common sequences (guides, 0.5)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17

  - SSF/budget: find or make a magic base with 2 good mods → essence for a 3rd mod and rare upgrade → Exalt for 4th and 5th → desecrate for the last mod.
  - Budget weapon (Mobalytics Paintmaster): high-ilvl base, Greater Essence of Abrasion (flat phys), desecrate a prefix with Omen of Sinistral Necromancy.
  - Fix a near-finished item: Perfect/corrupted essence + Crystallisation omen to swap out a specific prefix or suffix, then desecrate.
  - Jewels: fracture one strong mod, then chaos-spam the rest (Mobalytics Perra, Jun 2026) — jewels named among the most profitable crafts.
- src: Mobalytics SSF Crafting [S090], Mobalytics Paintmaster recoup Chronomancer crafting [S096], Mobalytics Perra PoE2 Crafting Guide [S097] (updated 2026-06-30), tier 3; retrieved 2026-11-17
- conf: single-source each (tier 3)
- notes: The essence-then-desecrate pattern respects the one-crafted + one-desecrated limit. Several 0.5 guides say crafting got swingier and that buying a finished item is often cheaper than chasing a multi-mod craft (Timesaver, tier 5, RMT — lead only). [INFERRED] For your plan: craft-to-sell (jewels, simple 2–3-mod bases) suits a currency-focused player; buy own BiS.


## Gear-level crafting for the league start
@ v=0.5.x vol=may-change conf=inferred date=2026-11-17
Guides from 0.5 recommend essences for the first rare upgrade on levelling and early-map gear because they turn a decent magic base rare with one guaranteed mod.
- src: Mobalytics SSF Crafting [S090], poe2wiki Essence [S692], tier 2–3; retrieved 2026-11-17
- conf: [INFERRED] from guide sequences — no guide states it as a rule
- notes: Check exchange prices for essences and quality currency before using them on levelling gear ([[league-lifecycle-pricing]]).
