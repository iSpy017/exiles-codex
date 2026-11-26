---
title: Elemental Supports (part 2): lightning/fire triggers, ailments, penetration, exposure
status: partial
tracker_topic: "Elemental supports + damage values"
tracker_note: "partial (0.5.x)"
defaults: v=0.5.x
---
Status: partial (summary table lives in [[gems/elemental-supports]]). Not covered: Unleash, Multishot I, Considered Casting, Cold Penetration, Deliberation, Inexorable Critical I, Rapid Casting II, Cold Exposure, Cold Mastery ([[gems/caster-supports]]). Elemental Penetration is NOT a gem: its PoE2DB page is a passive-tree/mastery node (see Gaps in report).
Version: 0.5.x-era PoE2DB data, crawl 2026-11-23. NOT checked against 1.0.
Source summary: one PoE2DB page per gem; "lists" = page's Skill Gems table, checked vs Spark / Flame Wall / Tornado / Thunderstorm / Elemental Weakness.

## Coursing Current
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 1, +5 Int, no header Cost Multiplier (implicit Mana 100%). When a Hit from the supported skill Shocks, triggers Coursing Current: a chaining lightning projectile from the Shocked enemy to a nearby Drenched enemy, chains 6 times, only collides with Drenched targets, no chain to previous targets, 0.20 s cooldown (6 uses), 10% crit chance, projectile speed 42.5 m/s. Damage 1-11 lightning at gem level 1 up to 8-294 at level 20 (table runs to 40). Categories: Spell, Projectile, Trigger, Lightning, Chaining. Page category "Coursing Current".
- src: poe2db:Coursing_Current, tier 2, 2026-11-23
- notes: lists Thunderstorm only. Triggered skill copies the socket gem's level. Pairs with Shock Conduction II (always shocks Drenched).


## Shock Conduction / Shock Conduction II
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
I = tier 2, 120%, +5 Int: when a hit shocks, there is a 50% chance every enemy within 2.5 m is shocked too. II = no tier in header, 120%, +5 Int: keeps that spread and additionally guarantees a shock on Drenched targets. Same Category "Shock Conduction". Version tables on both pages carry a 0.5.0 line "Shock Conduction II: can no longer be obtained".
- src: poe2db:Shock_Conduction «I», poe2db:Shock_Conduction_II «II», tier 2, 2026-11-23
- notes: both list Thunderstorm (I also Arc, Orb of Storms). II being unobtainable is [INFERRED] from the version line (wording ambiguous on whether it also applies to I): flag for recheck.


## Living Lightning I / II
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
triggered on dealing lightning damage with the supported skill; creates 1 lightning minion (30 s, converts 100% phys to lightning, attacks every 0.14 s, chains 3, disperses after 3 attacks); minion level based on the triggering skill. I = tier 2, +5 Int, limit 5 minions, 0.20 s cooldown (5 uses). II = tier 4, +5 Int, limit 8 minions (8 uses), minions get 1% increased damage per 5 of your Str and 1% increased attack speed per 10 of your Dex. Categories: Minion, Trigger, Lightning, Duration. Category "Living Lightning". No header mult (implicit Mana 100%).
- src: poe2db:Living_Lightning «I», poe2db:Living_Lightning_II «II», tier 2, 2026-11-23
- notes: I lists Thunderstorm; II lists Thunderstorm too. 0.5.0 note: I no longer replaces minions at max.


## Elemental Discharge
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 3, +5 Int, no header mult (implicit Mana 100%). Supported spell Consumes Freeze/Shock/Ignite on hit to trigger a Discharge (2 m radius, 1 s cooldown, 10% crit). The supported skill cannot inflict Freeze, Shock or Ignite itself. Discharge damage matches consumed ailments: fire 40-60% of your Int, cold 80-120% of Int, lightning 1-120% of Int. Cannot support minion skills or skills that already Consume ailments. Family "Catalysing Elements".
- src: poe2db:Elemental_Discharge, tier 2, 2026-11-23
- notes: lists Arc, Thunderstorm. Conflicts with shock-focused supports (it stops the skill shocking): see [[gems/elemental-supports]] Shock Conduction.


## Lightning Penetration
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 2, 120%, +5 Dex; supported Hits penetrate 30% lightning resistance. Category "Lightning Penetration".
- src: poe2db:Lightning_Penetration, tier 2, 2026-11-23
- notes: lists Arc, Thunderstorm, Lightning Conduit (Spark not listed). Cold Penetration in [[gems/caster-supports]].


## Fire Penetration I / II
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
I = tier 2, 120%, +5 Str, pen 30% fire res. II = tier 5, 120%, +5 Str, hits ignore enemy fire resistance. Category "Fire Penetration".
- src: poe2db:Fire_Penetration_I «I», poe2db:Fire_Penetration_II «II», tier 2, 2026-11-23
- notes: none of David's five listed (Flame Wall not listed).


## Lightning Exposure / Fire Exposure
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
both tier 4, 120%, Exposure for 8 s on Shocking (Lightning, +5 Dex) / Igniting (Fire, +5 Str). Categories "Lightning Exposure" / "Fire Exposure"; tags Duration.
- src: poe2db:Lightning_Exposure, poe2db:Fire_Exposure, tier 2, 2026-11-23
- notes: Lightning lists Spark, Thunderstorm; Fire lists Flame Wall. Exposure magnitude not on page. Cold Exposure in [[gems/caster-supports]].


## Ignite I
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 1, 120%, +5 Str: supported hits have 100% more Flammability magnitude. Category "Ignite".
- src: poe2db:Ignite_I, tier 2, 2026-11-23
- notes: list: Fireball, Molten Blast, Incinerate etc.; none of David's five. Ignite II/III pages exist, not read.
