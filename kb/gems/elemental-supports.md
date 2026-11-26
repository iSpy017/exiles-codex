---
title: Elemental Supports (part 1): area, duration, limit, ground, storm, echo, mastery
status: partial
tracker_topic: "Elemental supports + damage values"
tracker_note: "partial (0.5.x)"
defaults: v=0.5.x
---
Status: partial (part 1 of 2; part 2 = [[gems/elemental-supports-damage]]). Not covered: Unleash, Multishot I, Considered Casting, Cold Penetration, Deliberation, Inexorable Critical I, Rapid Casting II, Cold Exposure, Cold Mastery (see [[gems/caster-supports]]); tier system in [[gems/support-tiers]].
Version: 0.5.x-era PoE2DB data, crawl 2026-11-23. NOT checked against 1.0.
Source summary: one PoE2DB page per support gem; "Compatible" lists = the page's "Skill Gems" table (PoE2DB's list, tier-1..14 skill gems), checked only against Spark / Flame Wall / Tornado / Thunderstorm / Elemental Weakness.

## Summary table (both parts)
Tier = support tier. "Mult" = header Cost Multiplier; "n/s" = header shows none, implicit line says Mana 100%. Attr = +5 of that stat.
| Support | Tier | Mult | Attr | Main effect | Category |
|---|---|---|---|---|---|
| Magnified Area I | 1 | 130% | Int | 35% increased AoE | Increased Area of Effect |
| Magnified Area II | 3 | 130% | Int | 45% increased AoE | Increased Area of Effect |
| Concentrated Area | 1 | n/s | Int | 30% more area damage, 50% less AoE | Concentrated Area |
| Expand | 5 | 120% | Int | up to 3 Seals, 30% inc AoE per Seal | Seal, Increased AoE |
| Prolonged Duration I | 1 | 120% | Str | 30% more skill effect duration | Prolonged Duration |
| Prolonged Duration II | 3 | 120% | Str | 35% more duration | Prolonged Duration |
| Prolonged Duration III | none shown | n/s | Str | 60% more duration, 16 s cooldown | Prolonged Duration |
| Overabundance I | 1 | n/s | Dex | +1 Limit, 50% less duration | Overabundance |
| Overabundance II | 4 | n/s | Dex | +1 Limit, 40% less duration | Overabundance |
| Persistent Ground I | 2 | n/s | Str | 50% inc ground surface duration | Persistent Ground |
| Persistent Ground II | 3 | n/s | Str | as I + surfaces only end by expiry | Persistent Ground |
| Persistent Ground III | 5 | n/s | Str | as II + 30% less enemy cooldown recovery | Persistent Ground |
| Advancing Storm | 4 | n/s | Int | Storm skills start at you, move to target | Advancing Storm |
| Spell Echo | 2 | 150% | Int | Echo 1x, 30% less cast speed | Spell Echo |
| Burning Inscription | 4 | 110% | Int | Ignited Ground after Inscription expires | Burning Inscription |
| Lightning Mastery | 5 | n/s | Int | +1 level Lightning skills | Mastery |
| Fire Mastery | 5 | n/s | Int | +1 level Fire skills | Mastery |
| Coursing Current | 1 | n/s | Int | on Shock, chaining lightning (6 chains) to Drenched | Coursing Current |
| Shock Conduction | 2 | 120% | Int | 50% chance shock spreads 2.5 m | Shock Conduction |
| Shock Conduction II | none shown | 120% | Int | as I + always shocks Drenched | Shock Conduction |
| Living Lightning I | 2 | n/s | Int | triggered lightning minions, limit 5 | Living Lightning |
| Living Lightning II | 4 | n/s | Int | limit 8, scales w/ Str/Dex | Living Lightning |
| Elemental Discharge | 3 | n/s | Int | consume ailments -> trigger discharge | Elemental Discharge |
| Lightning Penetration | 2 | 120% | Dex | pen 30% lightning res | Lightning Penetration |
| Fire Penetration I | 2 | 120% | Str | pen 30% fire res | Fire Penetration |
| Fire Penetration II | 5 | 120% | Str | ignore fire res | Fire Penetration |
| Lightning Exposure | 4 | 120% | Dex | Exposure 8 s on Shock | Lightning Exposure |
| Fire Exposure | 4 | 120% | Str | Exposure 8 s on Ignite | Fire Exposure |
| Ignite I | 1 | 120% | Str | 100% more Flammability magnitude | Ignite |
Levels: every gem except Coursing Current and Living Lightning I/II shows "Level Effect /1" (single level, Requires Level 0). Those three show "/40" tables, but only for the triggered skill; the triggered skill copies the level of the gem it is socketed in. All use the rule: cannot socket two supports of the same Category on one skill.

## Magnified Area I / II
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
I = tier 1, 130% mult, +5 Int, 35% increased AoE. II = tier 3, 130% mult, +5 Int, 45% increased AoE. Category "Increased Area of Effect" (one per skill; also shared with Expand). Supports any AoE skill. Page notes 0.4.0 removed II's old damage penalty.
- src: poe2db:Magnified_Area_I, poe2db:Magnified_Area_II «II», tier 2, crawl 2026-11-23
- notes: lists include Thunderstorm and Tornado (both); Elemental Weakness (II only). Spark and Flame Wall not listed.


## Concentrated Area
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 1, +5 Int, 30% more area damage, 50% less AoE. Header shows no Cost Multiplier; implicit Mana 100%.
- src: poe2db:Concentrated_Area, tier 2, 2026-11-23
- notes: listed skills include none of Spark/Flame Wall/Tornado/Thunderstorm/Elemental Weakness.


## Expand
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 5, 120% mult, +5 Int. Max 3 Seals; a Seal is gained every 200% of cast time; 30% increased AoE per Seal broken. Spells you cast yourself only; cannot support channelling, cooldown, or skills already gaining Seals. Categories: Seal and Increased AoE.
- src: poe2db:Expand, tier 2, 2026-11-23
- notes: lists Thunderstorm, Tornado. Expand's PoE2DB version table carries a generic 1.0.0 line about the support gem and passive tree rework, so Expand MUST be re-checked at 1.0 (do not dismiss). Unleash/Salvo share the Seal rules ([[gems/caster-supports]]).


## Prolonged Duration I / II / III
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
I = tier 1, 120%, +5 Str, 30% more duration. II = tier 3, 120%, +5 Str, 35% more. III = no tier shown, +5 Str, 60% more duration, applies a 16 s cooldown, cannot support skills that already have a cooldown. Category "Prolonged Duration".
- src: poe2db:Prolonged_Duration_I «I», poe2db:Prolonged_Duration_II «II», poe2db:Prolonged_Duration_III «III», tier 2, 2026-11-23
- notes: I and II both list Spark, Flame Wall, Thunderstorm, Tornado. III's header has no Cost Multiplier (implicit 100%). III excludes Persistent, Triggered, totem skills per its type filter.


## Overabundance I / II (III noted)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
raises a skill's "Limit" (only effects worded "Limit") at the cost of duration. I = tier 1, +5 Dex, +1 Limit, 50% less duration. II = tier 4, +5 Dex, +1 Limit, 40% less duration. III (no tier) doubles Limits but curses you with a random curse when you use the skill; cannot support Persistent skills. No Cost Multiplier in headers (implicit 100%).
- src: poe2db:Overabundance_I «I», poe2db:Overabundance_II «II», poe2db:Overabundance_III «III», tier 2, 2026-11-23
- notes: lists (I, II) include Orb of Storms, Volcano, Firestorm, totems; none of David's five. Category "Overabundance". Same family as Advancing Storm (Morgana's Tempest).


## Persistent Ground I / II / III
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
all +5 Str, 50% increased duration of ground surfaces from supported skills. I = tier 2. II = tier 3, surfaces can only end by expiring. III = tier 5, same, plus surfaces apply "Suppressive Ground": 30% less Cooldown Recovery Rate. No Cost Multiplier in headers (implicit 100%). Category "Persistent Ground".
- src: poe2db:Persistent_Ground_I «I», poe2db:Persistent_Ground_II «II», poe2db:Persistent_Ground_III «III», tier 2, 2026-11-23
- notes: allowed type "CreatesGroundEffect". I lists Lightning Warp, Incinerate, Oil Grenade/Barrage; III adds Ice Nova, Storm Lance etc. None of David's five listed (Flame Wall not listed).


## Advancing Storm
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 4, +5 Int, no header Cost Multiplier (implicit Mana 100%). Storm skills originate from you and travel toward the target location. Version line: 0.5.0 lets it support any Storm skill under any condition (previously only spells you use yourself). Category "Advancing Storm".
- src: poe2db:Advancing_Storm, tier 2, 2026-11-23
- notes: lists Thunderstorm, Tornado. Same family as Overabundance (Morgana's Tempest).


## Spell Echo
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 2, 150% mult, +5 Int. Supported "Cascadable" spells you use yourself Echo 1 time; 30% less cast speed; echoes get 40% increased AoE. Excludes Triggered, Persistent skills.
- src: poe2db:Spell_Echo, tier 2, 2026-11-23
- notes: PoE2DB lists only Bone Cage, Comet, Hexblast; none of David's five. A 0.3.0c note says Orb of Storms was unintentionally unsupportable. Unleash is in [[gems/caster-supports]].


## Burning Inscription
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
tier 4, 110% mult, +5 Int. Once a supported skill's Runic Inscription runs out, this fires and leaves a 2 m patch of Ignited Ground lasting 4 s; enemies on it are ignited as though hit for fire damage worth 20% of your maximum Mana. Allowed skill types: curses and ground-rune skills.
- src: poe2db:Burning_Inscription, tier 2, 2026-11-23
- notes: lists Elemental Weakness (tier 7) plus Enfeeble, Temporal Chains, Vulnerability, Despair, Profane Ritual. Mult 110% since 0.2.0 (was 100%).


## Lightning Mastery / Fire Mastery
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
both tier 5, +5 Int, +1 level to supported Lightning / Fire skills; not for skills without levels. No header mult (implicit 100%). Category "Mastery".
- src: poe2db:Lightning_Mastery, poe2db:Fire_Mastery, tier 2, 2026-11-23
- notes: Lightning lists Spark, Thunderstorm. Fire lists Flame Wall, Elemental Weakness. Cold Mastery in [[gems/caster-supports]].
