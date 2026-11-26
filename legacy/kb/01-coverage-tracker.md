# Coverage Tracker

Last updated: 2026-11-26 (batches 23–46 complete via agent pipeline; endgame 0.5.x baselines added in wave 6: Sonnet workers → Haiku inspectors → coordinator publish; atlas passives and atlas/waystones/tablets wait for 1.0 — patch notes not out as of 2026-11-26)

## Core mechanics — kb/mechanics/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Damage types & conversion | mechanics/damage-types-conversion.md | done (0.5.x; recheck 1.0) | 1 |
| Hits vs damage over time | mechanics/hits-vs-dot.md | done (0.5.x; recheck 1.0) | 1 |
| Critical strikes | mechanics/crit.md | needs-1.0-check (0.5.x; GGG says crit chance leaves the passive tree in 1.0; monster crit conflict resolved by game data 2026-11-23) | 1 |
| Attack & cast speed | mechanics/attack-cast-speed.md | partial (use-time formula, frame cap, dual wield added 2026-11-25; weapon base rates by class missing; 1 conflict) | 1, 20 |
| Area of effect & projectiles | mechanics/area-projectiles.md | partial (area-vs-radius √ rule still tier 5 only; poe2wiki AoE page has no mechanics text; PoE2DB corpus has none either) | 1, 20 |
| Accuracy | mechanics/accuracy.md | done (0.5.x; recheck 1.0; 1 conflict) | 1 |
| Ailments overview + buildup thresholds | mechanics/ailments-overview.md | done (0.5.5.9; recheck 1.0) | 2 |
| Ignite | mechanics/ignite.md | done (0.5.5.9; recheck 1.0) | 2 |
| Chill & freeze | mechanics/chill-freeze.md | partial (PoE2DB numbers added; monster threshold ≈ max life; no numeric threshold/formula in game data) | 2, 25 |
| Shock & electrocute | mechanics/shock-electrocute.md | partial (electrocute skills/supports listed; numeric monster thresholds not in data) | 2, 25 |
| Poison | mechanics/poison.md | done (0.5.5.9; recheck 1.0) | 2 |
| Bleed | mechanics/bleed.md | done (0.5.x; stacking = strongest only, poe2wiki 2026-11-25; recheck 1.0) | 2, 20 |
| Exposure & penetration | mechanics/exposure-penetration.md | done (0.5.5.9; recheck 1.0) | 2 |
| Resistances & caps | mechanics/resistances.md | done (0.5.x; penalty schedule needs 1.0 check) | 3 |
| Armour | mechanics/armour.md | done (0.5.5.9; formula conflict open) | 3 |
| Evasion | mechanics/evasion.md | done (0.5.5.9; recheck 1.0) | 3 |
| Energy shield | mechanics/energy-shield.md | done (0.5.5.9; recheck 1.0) | 3 |
| Block | mechanics/block.md | done (0.5.x; recheck 1.0) | 3 |
| Deflection (exists, since 0.3) | mechanics/deflection.md | done (0.5.x; cap conflict open) | 3 |
| Stun & heavy stun | mechanics/stun.md | partial (heavy stun 2 s base, poise stats [INFERRED]; per-monster thresholds missing; 15% vs 10% floor conflict) | 3, 25 |
| Life, mana, recoup, leech, regen | mechanics/recovery.md | partial (base regen: mana 4%/s, life/ES none; Str +2 life per point; base life + life per level missing; 1 conflict) | 4, 20, 21 |
| Flasks | mechanics/flasks.md | done (0.5.x; recheck 1.0) | 4 |
| Charms | mechanics/charms.md | done (0.5.5.9; 13 bases; slot-cap conflict open; recheck 1.0) | 4 |
| Spirit & reservation | mechanics/spirit-reservation.md | done (0.5.x; campaign spirit needs 1.0 check) | 4 |
| Minions | mechanics/minions.md | partial (base life/damage scaling added — derived values [INFERRED]; Life vs Minion Life column unresolved; Bone Construct/Spectre stats missing) | 4, 17, 22, 39 |
| Totems | mechanics/totems.md | done (0.5.x; recheck 1.0) | 4 |
| Dodge roll | mechanics/dodge-roll.md | done (0.5.x; recheck 1.0) | 4 |
| Weapon swap / weapon sets | mechanics/weapon-swap.md | done (0.5.x; points need 1.0 check) | 4 |
| Skill combos & interactions | mechanics/skill-interactions.md | done (0.5.5.9 game data only) | 4 |
| Monster life, rarity multipliers, monster res | mechanics/monster-life.md | done (0.5.x; derived from PoE2DB monster pages; Unique ×29 on boss page life is [INFERRED]; levels 57–64 / 75–78 missing) | 19 |
| Damage formula (increased adds / more multiplies) + order of operations | mechanics/damage-calculation.md | done (0.5.x; poe2wiki Receiving damage; wiki flags order for re-test; recheck 1.0) | 19, 20 |
| Shapeshifting, Rage, Glory (Druid) | mechanics/shapeshifting.md | partial (forms, Rage rules/sources/spenders, Glory; Talisman→form map missing; spells-in-form [INFERRED]) | 37 |
| Mana costs & regen (cost multiplier stacking) | mechanics/mana-costs.md | partial (pool + 4% regen sourced; Int +2 mana confirmed by PoE2DB; upfront vs per-second costs; multiplier stacking [INFERRED] from PoE1) | 19, 20, 21 |

## Gems — kb/gems/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Uncut skill / spirit / support gems | gems/uncut-gems.md | done (0.5.5.9; recheck 1.0) | 5 |
| Gem level vs character level requirements | gems/gem-levels.md | done (0.5.x; recheck 1.0) | 5 |
| Quality & alternate qualities | gems/quality.md | done (0.5.x; alt gem quality not obtainable — Secondary Regrading Lens "Not in game") | 5, 29 |
| Support tiers | gems/support-tiers.md | done (0.5.5.9; 1.0 support rebalance) | 5 |
| Lineage supports (list from tier 1–2) | gems/lineage-supports.md | done (0.5.5.9 list) | 5 |
| Lineage supports — drop sources & effects | gems/lineage-drop-sources.md | done (0.5.x; 77 gems, 11 with no source shown) | 29 |
| Socketing & gem slot limits | gems/socketing-limits.md | done (0.5.x; Jeweller's resolved, 1 conflict open) | 5 |
| Meta & trigger gems | gems/meta-trigger.md | done (0.5.5.9; sources of tier-0 metas partial) | 5 |
| Cold spell / cold persistent gems — per-level data | gems/cold-spell-gems.md | done (0.5.x; Frostbolt L1–28, Ice Nova, Arctic Armour, Herald of Ice, Elemental Weakness) | 19 |
| Caster / cold support effect values | gems/caster-supports.md | done (0.5.x; 9 supports; 1 conflict) | 19 |
| Storm Shaman engine gems — per-level data | gems/elemental-caster-gems.md | done (0.5.x; Spark incl. Cold-Infused, Flame Wall, Tornado, Thunderstorm with Drench level cap) | 22 |
| Minion skill gems — list, tiers, spirit by level | gems/minion-skills.md | partial (≈25 engravable + other-source minion skills) | 22 |
| Minion base stats — multipliers + derived life/damage by level | gems/minion-stats.md, gems/minion-stats-2.md | partial (17 minions; L2/20/40 values [INFERRED]; 2 conflicts) | 39 |
| Bow attack gems — per-level (Ice Shot, Lightning Arrow, Lightning Rod, …) | gems/bow-attack-gems.md … -4.md | done (0.5.x; 2 conflicts: Lightning Rod chains, Ice Shot shards) | 23, 31 |
| Elemental supports + damage values | gems/elemental-supports.md, gems/elemental-supports-damage.md | partial (0.5.x) | 32 |
| Spirit gems (non-minion persistents) — list + per-level | gems/spirit-gems.md, gems/spirit-gems-2.md | done (0.5.x; 42 gems; Grim Feast 30 spirit [INFERRED]) | 34 |
| Per-gem damage tables for other skills | gems/<topic>.md | todo (pull on demand from PoE2DB corpus) | 19+ |

## Classes — kb/classes/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Class & ascendancy index (enumerate from tier 1–2) | classes/index.md | done (0.5.5.9 + 1.0 announced; Master-at-Arms day-one now confirmed tier 1 — apply on next edit; rebuild at 1.0) | 6 |
| Ascendancy trials & point acquisition | classes/ascendancy-trials.md | done (0.5.x; recheck 1.0) | 6 |
| Passive tree: attributes, keystones, notables | classes/passive-tree.md | needs-1.0-check (0.5.5.9 baseline; tree overhauled in 1.0; jewel sockets move into clusters) | 6 |
| Weapon-set passive points | classes/weapon-set-points.md | done (0.5.x; recheck 1.0) | 6 |
| Respec costs | classes/respec.md | done (0.5.x; full L1–100 gold table; depth conflict open; recheck 1.0) | 6 |
| Sorceress ascendancies — node text | classes/sorceress-ascendancies.md | done (0.5.x; node pathing/adjacency not captured; granted-skill text missing) | 19 |
| Druid ascendancies (Shaman, Oracle) — node text | classes/druid-ascendancies.md | done (0.5.x; recheck 1.0) | 26 |
| Per-class / per-ascendancy docs (others) | classes/<name>.md | todo (deferred to 1.0 notes; shortlist first) | 6+ |

## Items — kb/items/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Item bases & implicits | items/bases-implicits.md | done (0.5.5.9; recheck 1.0 for new bases) | 7 |
| Rarity | items/rarity.md | done (0.5.x) | 7 |
| Affix tiers & mod groups | items/affix-tiers.md | done (0.5.5.9) | 7 |
| Item level & drop level | items/item-level.md | done (0.5.x; atlas may change in 1.0; 1 conflict) | 7 |
| Quality | items/quality.md | partial (amount per use still unknown; PoE2DB crawl has none) | 7, 27 |
| Sockets, runes, soul cores, idols | items/sockets-augments.md | partial | 7 |
| Rune effects by slot | items/rune-effects.md … -8.md | done (0.5.x; every rune incl. Warding, Ancient, named, Aldur, 63 Legacy runes; Bonded effects; drop sources not in corpus) | 27, 38 |
| Soul core & idol effects | items/soul-core-idol-effects.md … -4.md | done (0.5.x; all soul cores, 31 idols, Ancient Augments; drop sources partial; 2 slot conflicts) | 27, 38 |
| Corruption | items/corruption.md | done (0.5.x) | 7 |
| Uniques by slot + drop restrictions | items/uniques-index.md, uniques-armour.md, uniques-other.md | partial (names done) | 8 |
| Unique drop sources (boss/league tags, drop-disabled) | items/uniques-drop-sources.md | partial (0.5.x; 111 tagged, 22 disabled; Zarokh/Aberration/Vessel conflicts) | 28 |
| Uniques for caster/elemental builds | items/uniques-caster.md | partial (15 picks, not a ranking) | 28 |
| Unique armour mods by slot | items/uniques-mods-body-1..3, helmet-1..2, gloves-1..2, boots, shields-1..2 | done (0.5.x; 229 tabulated + 4 Demigod items with no readable mods; implicits omitted) | 35 |
| Unique weapon/jewellery/jewel/flask/charm mods | items/uniques-mods-weapons-1..3, caster-weapons-1..2, quivers, jewellery-1..4, jewels, flasks-charms | partial (0.5.x; all groups listed; mod separators approximate, some placeholder text from PoE2DB) | 36 |
| Talismans — bases, implicits, uniques | items/talismans.md | partial (form per base missing) | 37 |
| Caster & ES mod tiers by item level | items/caster-mod-tiers.md | done (0.5.x RePoE; base ES / weapon base damage not captured) | 19 |

## Crafting — kb/crafting/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Currency index (every orb + effect) | crafting/currency-index.md | done (0.5.5.9 game data) | 8 |
| Omens | crafting/omens.md | done (0.5.5.9 game data) | 8 |
| Essences | crafting/essences.md + essence-table.md + essence-table-high.md | done (0.5.x game data, all tiers; Ice conflict resolved; drop sources gap) | 8, 24 |
| Desecration & abyssal bones | crafting/desecration.md | partial (bone table + restrictions done; Ancient min-mod-level vs pool unclear; drop sources missing) | 8, 24 |
| Catalysts | crafting/catalysts.md | done (0.5.5.9 game data) | 9 |
| Verisium & other league crafting | crafting/league-crafting.md | done (0.5 Runes of Aldur; 1.0 Reforging announced — see strategy/official-1.0-reveal) | 9 |
| Recombinator (verify it exists) | crafting/recombinator.md | done (removed in 0.5; recheck 1.0) | 9 |
| Deterministic vs gamble crafting | crafting/approach.md | done (0.5 one-crafted-mod rule) | 9 |
| Expected cost of common crafts | crafting/craft-costs.md | partial (currency priced 2026-11-17; omens/essences/bones missing — waiting on David's poe.ninja saves) | 9 |

## Economy — kb/economy/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Currency Exchange & order book | economy/currency-exchange.md | done (0.5.x; 2 conflicts open) | 10 |
| Trade site & bulk exchange | economy/trade-site.md | done (0.5.x; bulk tab unconfirmed) | 10 |
| Gold & its uses | economy/gold.md | done (0.5.x + 1.0 Conquerors note) | 10 |
| Reading poe.ninja / poe2scout (vol/hr vs rate) | economy/price-sites.md | done (sites unreachable from workspace) | 10 |
| Price lifecycle across a league | economy/league-lifecycle.md | done (0.5 user data; volatile) | 10 |
| What holds value vs decays | economy/value-retention.md | done (0.5 user data; volatile) | 10 |
| Price snapshot (Currency, Forbidden Rites) | economy/price-snapshot-2026-11-17.md | done (volatile, dated) | 10 |

## Campaign — kb/campaign/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Area levels | campaign/area-levels.md | done (0.5.5.9; 1.0 restructure) | 11 |
| Act 1 | campaign/act-1.md | partial (zones/bosses/rewards; boss stat blocks now in boss-data-acts-1-2; fight choreography missing) | 11, 21 |
| Act 2 | campaign/act-2.md | partial (zones/bosses/rewards; boss stat blocks in boss-data-acts-1-2; choreography missing; relic conflict now leaning B) | 11, 21 |
| Act 3 | campaign/act-3.md | partial (zones/bosses/rewards; boss stat blocks in boss-data-acts-3-4; choreography missing) | 11, 21 |
| Act 4 | campaign/act-4.md | partial (zones/bosses/rewards; boss stat blocks in boss-data-acts-3-4; choreography missing; point-source conflict, 4th source added) | 12, 21 |
| Campaign boss data, Acts 1–4 (res, hit sizes, unavoidable skills, adds) | campaign/boss-data-acts-1-2.md, campaign/boss-data-acts-3-4.md | partial (45 bosses from PoE2DB stat blocks, 0.5.x; choreography not captured; 90% res reading [INFERRED]; rebuild at 1.0) | 21 |
| Act 5 (1.0) | campaign/act-5.md | partial (official counts: 24 areas / 18 bosses across A5+A6; possible A5 quests in 0.5 data; needs 1.0 notes) | 12, 18 |
| Act 6 (1.0) | campaign/act-6.md | partial (official counts; 0.5 "Act 6" data = Interludes; needs 1.0 notes) | 12, 18 |
| Interludes (removal in 1.0) | campaign/interludes.md | done (0.5 reference; removal confirmed by GGG quotes; retire at 1.0) | 12 |
| Permanent rewards (points, spirit, res, life) | campaign/permanent-rewards.md | done (0.5 totals; 1.0 will change) | 11 |
| Quest gem & item rewards | campaign/quest-rewards.md | done (0.5 Acts 1–4 + Interludes + map quests, PoE2DB single-source; rebuild at 1.0) | 12, 18 |
| Levelling routes | campaign/levelling-routes.md | partial (principles + benchmarks; 1.0 route pending) | 12 |

## Endgame — kb/endgame/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| Atlas overview | endgame/atlas.md | partial (0.5.x baseline, all atlas-dependent; no passive tree) | 13, 44 |
| Waystones & tiers | endgame/waystones.md | partial (0.5.x; T1–16 = area 65–80; T16 source not found; atlas-dependent) | 13, 44 |
| Tablets | endgame/tablets.md | partial (0.5.x; 8 bases, 9 uniques, mod decision rows; weights/drop rates missing) | 13, 45 |
| Atlas passives | endgame/atlas-passives.md | todo (deferred to 1.0 — tree changing; David 2026-11-26) | 13 |
| Breach | endgame/breach.md | done (0.5.x baseline; atlas-dependent parts tagged; recheck 1.0) | 14, 40 |
| Delirium | endgame/delirium.md | done (0.5.x baseline; Simulacrum final boss unclear; recheck 1.0) | 14, 40 |
| Ritual | endgame/ritual.md | partial (0.5.x; tribute/reroll costs not in corpus; recheck 1.0) | 14, 41 |
| Expedition | endgame/expedition.md | partial (0.5.x Runes of Aldur form; explosive counts/recipes not in corpus; recheck 1.0) | 14, 41 |
| Abyss | endgame/abyss.md | partial (0.5.x; fissure boss stats, trove tables missing; recheck 1.0) | 14, 42 |
| Trial of Chaos | endgame/trial-of-chaos.md | partial (0.5.x; reward tables, Fate key differences missing; recheck 1.0) | 14, 42 |
| Trial of the Sekhemas | endgame/sekhemas.md, sekhemas-2.md | partial (0.5.x; + Baryas, rooms, relic slots/mods, Reliquary keys; Honour-loss % and Test Barya sources missing) | 14, 19, 46 |
| Atziri's Temple (Vaal temple) | endgame/vaal-temple.md | partial (0.5.x; rooms, medallions, devices, Atziri/Architect; phase mechanics missing) | 14, 46 |
| Conquerors league mechanic (1.0) | endgame/conquerors-league.md | todo (deferred to 1.0 patch notes; official pre-notes facts staged in strategy/official-1.0-reveal) | 14 |
| Pinnacle bosses + keys/fragments | endgame/pinnacle-bosses.md, pinnacle-bosses-2.md | partial (0.5.x roster, keys, stats, biggest hits; some key drop sources missing; recheck 1.0) | 15, 43 |
| Uber bosses | endgame/uber-bosses.md | partial (0.5.x: no uber tier — quest vs farm versions; farm stats missing) | 15, 43 |

## Builds — kb/builds/
| Topic | Doc | Status | Batch |
|---|---|---|---|
| League starter archetypes | builds/starter-archetypes.md | done (0.5.5 meta; volatile; rebuild at 1.0) | 16 |
| Budget tiers (SSF → high) | builds/budget-tiers.md | done (cut-offs [INFERRED]; volatile) | 16 |
| Levelling gear breakpoints | builds/levelling-gear.md | done (0.5.5.9; 1.0 adds bases; 1 conflict) | 16 |
| Defensive layering checklist | builds/defence-checklist.md | done (0.5.5.9 mechanics; recheck 1.0) | 16 |
| Ice Shot Deadeye levelling playbook (practice) | builds/ice-shot-deadeye-levelling-0.5.5.md | partial (0.5.5, single-source; open items listed in doc) | 17 |
| Own build — Storm Shaman (design) | builds/storm-shaman.md | partial (1.0 skeleton; lock on patch day; engine gem numbers now in gems/elemental-caster-gems) | own, 22 |
| Own build — Storm Shaman levelling | builds/storm-shaman-levelling.md | partial (Acts 1–4 0.5 data; Acts 5–6 pending; Thunderstorm Drench cap needs gem 18 before high maps) | own, 22 |
| Own build — Storm Shaman pivot + maps | builds/storm-shaman-pivot.md | partial (costs TBD at launch) | own |
| KB-test build — Frostbolt Chronomancer (0.5.5) | builds/kb-test-frostbolt-chronomancer-0.5.5.md + builds/kb-test-frostbolt-chronomancer-damage-0.5.5.md | partial (KB-only; damage confidence low/low–med/med/low; increased/more rule now sourced in mechanics/damage-calculation — doc text not yet updated; gaps: tree notables, mana check, ×29 boss-life reading, ascendancy pathing) | test |

## Strategy — kb/strategy/
| Topic | Doc | Status |
|---|---|---|
| League lifecycle pricing (seed) | strategy/league-lifecycle-pricing.md | done (0.5.5, volatile) |
| Player profile (seed) | strategy/my-profile.md | done |
| League start framework (video transcript) | strategy/league-start-framework.md | done (pre-1.0 opinion) |
| Farm profitability ranking (pre-launch) | strategy/farm-ranking.md | todo (deferred with endgame) |
| Super-sweat campaign skip route | strategy/skip-route.md | todo — needs 1.0 acts |
| 0.5.5 practice build for 1.0 | strategy/practice-build-0.5.5.md | done (volatile; re-judge at 1.0) |
| 1.0 dev statements — league mechanic (interviews) | strategy/dev-statements-1.0-league.md | done (tier-1 interviews, pre-notes; volatile) |
| 1.0 dev statements — balance/classes/crafting | strategy/dev-statements-1.0-balance.md | done (tier-1 interviews + tier-5 rumours; volatile) |
| 1.0 official reveal page (pathofexile2.com/fullrelease) | strategy/official-1.0-reveal.md | done (tier 1, announcement; merge into topic docs at 1.0 refresh) |
| Sekhemas currency profit centres (creator) | strategy/sekhemas-currency-farm.md | done (tier 5, 0.5.x, undated prices; volatile) |
| Rarity value (creator vs dev) | strategy/rarity-value.md | done (0.5.5 + 1.0 stance) |
| Atlas starter strategy (creator) | strategy/atlas-starter-strategy.md | done (tier 5, 0.5.5; rebuild at 1.0) |
| Build pick/learn/copy method | strategy/build-copy-method.md | done (method, tier 5) |
| Loot pickup heuristics | items/loot-pickup-heuristics.md | done (tier 5, 0.5.x; 1 conflict) |
| KB storage rework (how docs are stored/optimised) | — | todo (parked by David 2026-11-26) |
