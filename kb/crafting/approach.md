# Deterministic vs gamble crafting (0.5 rules)

Scope: the rules that limit crafting in 0.5, the standard crafting sequence, and which tools are deterministic. Costs → [[craft-costs]].

## The 0.5 rule: one crafted mod, one desecrated mod
- Claim: Since 0.5, every method that guarantees a mod (essences, alloys, etc.) makes a "crafted" mod, and an item can hold only one crafted mod at a time. Desecrated mods are not crafted mods, but an item can hold only one desecrated mod. So you can't stack several essences on one item anymore.
- Version: 0.5.0+
- Volatility: may-change (likely revisited in 1.0)
- Source: RePoE poe2 keywords.json "Crafted Modifiers" (one per item), tier 2 (game data 0.5.5.9); 0.5.0 patch-note text quoted in GGG forum thread [3932540](https://web.poecdn.com/forum/view-thread/3932540/page/99), tier 5 (quote of tier-1 notes); Boostmatch 0.5 patch summary, tier 5; retrieved 2026-11-17
- Confidence: confirmed (game text + quoted patch notes)
- Notes: Crafted mods show in lighter blue. Before 0.5 (0.3–0.4), stacking a Perfect Essence on top of a regular one was a common weapon-craft step (forum post). Old guides using multiple essences are invalid for 0.5.

## Deterministic tools (control what you get)
- Claim: Essence / Alloy (one guaranteed mod) · Desecration (choose 1 of 3 at the Well of Souls) · Fracturing Orb (lock a mod) · prefix/suffix omens (Sinistral/Dextral Exaltation, Coronation, Erasure, Annulment, Necromancy, Crystallisation) · Omen of Whittling (removes the lowest-level mod) · Hinekora's Lock (preview the next currency result) · Greater/Perfect orbs (raise the mod-level floor).
- Version: 0.5.5.9
- Volatility: may-change
- Source: game data (see [[currency-index]], [[omens]], [[essences]], [[desecration]]), tier 2; retrieved 2026-11-17
- Confidence: confirmed (individual effects); the grouping is mine

## Gamble tools
- Claim: Exalted / Chaos / Alchemy / Annulment without omens (random mod added or removed), Divine (values), Vaal Orb, Architect's Orb, Orb of Chance.
- Version: 0.5.5.9
- Volatility: stable
- Source: game data, tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Common sequences (guides, 0.5)
- Claim:
  - SSF/budget: find or make a magic base with 2 good mods → essence for a 3rd mod and rare upgrade → Exalt for 4th and 5th → desecrate for the last mod.
  - Budget weapon (Mobalytics Paintmaster): high-ilvl base, Greater Essence of Abrasion (flat phys), desecrate a prefix with Omen of Sinistral Necromancy.
  - Fix a near-finished item: Perfect/corrupted essence + Crystallisation omen to swap out a specific prefix or suffix, then desecrate.
  - Jewels: fracture one strong mod, then chaos-spam the rest (Mobalytics Perra, Jun 2026) — jewels named among the most profitable crafts.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics SSF Crafting](https://mobalytics.gg/poe-2/guides/ssf-crafting), [Mobalytics Paintmaster recoup Chronomancer crafting](https://mobalytics.gg/poe-2/profile/paintmaster/guides/recoup-chronomancer-gear-crafting-guide), [Mobalytics Perra PoE2 Crafting Guide](https://mobalytics.gg/poe-2/profile/perra/guides/poe2-crafting-guide) (updated 2026-06-30), tier 3; retrieved 2026-11-17
- Confidence: single-source each (tier 3)
- Notes: The essence-then-desecrate pattern respects the one-crafted + one-desecrated limit. Several 0.5 guides say crafting got swingier and that buying a finished item is often cheaper than chasing a multi-mod craft (Timesaver, tier 5, RMT — lead only). [INFERRED] For your plan: craft-to-sell (jewels, simple 2–3-mod bases) suits a currency-focused player; buy own BiS.

## Gear-level crafting for the league start
- Claim: Guides from 0.5 recommend essences for the first rare upgrade on levelling and early-map gear because they turn a decent magic base rare with one guaranteed mod.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics SSF Crafting](https://mobalytics.gg/poe-2/guides/ssf-crafting), [poe2wiki Essence](https://www.poe2wiki.net/wiki/Essence), tier 2–3; retrieved 2026-11-17
- Confidence: [INFERRED] from guide sequences — no guide states it as a rule
- Notes: Check exchange prices for essences and quality currency before using them on levelling gear ([[league-lifecycle-pricing]]).
