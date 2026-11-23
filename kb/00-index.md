# KB Index

Last updated: 2026-11-23 (batch 18: official 1.0 reveal page, quest rewards, Acts 5–6 counts; endgame still deferred to 1.0 notes)

## Control docs
- kb/00-index.md — this map
- kb/01-coverage-tracker.md — every in-scope topic with status and research batch (source of truth for the dashboard)
- kb/02-sources.md — source registry: URL, tier, reachability, licences, RePoE game-data usage, do-not-cite list
- kb/03-changelog.md — dated log of library changes
- kb/04-conflicts.md — source disagreements (open and resolved-by-game-data)

## Dashboard
- Coverage dashboard: https://claude.ai/artifact/9FU4XgSiCzDjeZMfwnr4Au — reads tracker.csv exported from 01-coverage-tracker.md
- kb/tools/md_to_csv.py — converts the tracker MD to the dashboard CSV. Re-run and re-upload after every tracker change.

## Mechanics — offence & ailments
- kb/mechanics/damage-types-conversion.md — 5 damage types, mitigation per type, two-step conversion, overconversion, gain-as-extra (0.5.x)
- kb/mechanics/hits-vs-dot.md — hit vs DoT, what skips DoT, ailment damage locked at the hit, ES bypass (0.5.5.9)
- kb/mechanics/crit.md — crit chance/bonus basics, scaling order, lucky and bifurcated crits, monster crit conflict (0.5.x; needs-1.0-check: crit chance leaves the tree in 1.0)
- kb/mechanics/attack-cast-speed.md — weapon vs skill speed, skill speed additivity, action speed, Onslaught (partial)
- kb/mechanics/area-projectiles.md — AoE definition, area-vs-radius, Presence 4 m, projectile behaviour order (partial)
- kb/mechanics/accuracy.md — hit chance formula, 5% floor, distance penalty 2–9 m, Dex +8 accuracy, entropy (0.5.5.9)
- kb/mechanics/ailments-overview.md — the 7 ailments, chance vs buildup vs explicit-chance, ailment threshold = ½ life, Primed %, stacking rule (0.5.5.9)
- kb/mechanics/ignite.md — 20%/s of fire hit, 4 s, Flammability 1% per 5% threshold, ignited ground, aggravated/compounding (0.5.5.9)
- kb/mechanics/chill-freeze.md — chill 30–50% slow, freeze buildup, monster threshold ≈ max life (numbers unpublished), Brittle (partial)
- kb/mechanics/shock-electrocute.md — shock 20% increased damage taken, 1% per 4% threshold, electrocute from specific skills only (partial)
- kb/mechanics/poison.md — 20%/s of phys+chaos, 2 s, explicit chance, stack limit 1 (0.5.5.9)
- kb/mechanics/bleed.md — 15%/s of phys, 5 s, +100% moving/aggravated, Corrupted Blood separate (partial)
- kb/mechanics/exposure-penetration.md — exposure −20%/4 s, rarity reduction, penetration hits-only and floors at 0% (0.5.5.9)

## Mechanics — defences
- kb/mechanics/resistances.md — 75% default / 90% hard cap, campaign penalty −60% by endgame (0.5.x schedule, 1.0 check), monster res mods
- kb/mechanics/armour.md — phys-hit DR vs hit size, formula (10× vs 12× conflict), movement-speed penalties, Armour Break/Sundered/Riven/Crushed
- kb/mechanics/evasion.md — evade formula, 95% cap, entropy, red-flash weakness, distance interplay
- kb/mechanics/energy-shield.md — ES basics, 4 s delay + 12.5%/s recharge, ES leech, Guard, Runic Ward
- kb/mechanics/block.md — block negates hit but not stun, 50% default / 90% hard cap, active vs passive, Parry
- kb/mechanics/deflection.md — exists since 0.3, 40% of hit prevented, works on red-flash attacks, cap conflict
- kb/mechanics/stun.md — light vs heavy stun, player stun threshold = life, phys/melee multipliers, Primed/Crushing Blows/Daze (partial; no monster numbers published)

## Mechanics — resources & systems
- kb/mechanics/recovery.md — leech (1 instance, 1 s, 40k cap), recoup over 8 s, regen sources, Low = 35%, overflow 1.5×, life loss, rage, checkpoints (partial)
- kb/mechanics/flasks.md — 1 life + 1 mana slot, recovery over time wasted at full, charges by monster power, example bases
- kb/mechanics/charms.md — 13 charm bases (level, charges/use, duration, effect), charges = ½ power, slot cap conflict (done)
- kb/mechanics/spirit-reservation.md — spirit for persistents, per-weapon-set spirit, 100 from campaign, sceptre 100 implicit, free item/ascendancy persistents
- kb/mechanics/minions.md — persistent/reviving/temporary, companions (1), minion level = 2× gem level, commands, offerings (partial)
- kb/mechanics/totems.md — not minions, use your stats, base limit 1 shared, Ancestral Bond, Embankment auras
- kb/mechanics/dodge-roll.md — avoids projectiles + non-AoE in first half, not AoE; Unwavering Stance/Bulwark; sprint +50% MS
- kb/mechanics/weapon-swap.md — two sets, auto-swap, 24 weapon-set points (convert, not extra), combo/surges lost on swap
- kb/mechanics/skill-interactions.md — triggers, meta gems + energy, persistent/herald/link/aura, combo, marks, curses, infusions, surges

## Gems
- kb/gems/uncut-gems.md — skill (L1–20) / spirit (L4–20) / support (L1–5) uncut gems, drop levels, tier gating, active + persistent tiers (4/8/14)
- kb/gems/gem-levels.md — gem level → char level table (L8=26, L10=36, L12=46, L20=90), corruption to L21
- kb/gems/quality.md — Gemcutter's Prism +5% each, 20% max, quality before corruption; alt qualities conflict (Regrading Lenses in data) (partial)
- kb/gems/support-tiers.md — support tiers 1–5, counts per tier, numbered support lines, category rule
- kb/gems/lineage-supports.md — can't engrave, drop-only, one copy each; full 0.5.5.9 list; 0.5.x price climb
- kb/gems/socketing-limits.md — 9 skill slots, 2→5 support sockets (Jeweller's Lesser/Greater/Perfect = 3/4/5), +5 attribute per support, duplicate rules
- kb/gems/meta-trigger.md — meta gem list by tier (engravable vs granted), trigger tag count

## Classes
- kb/classes/index.md — 8 live classes / 22 ascendancies (0.5.5.9) with start attributes; 1.0 adds Shadow (Assassin, Infiltrator) + Duelist (Knight, Master-at-Arms) → 10 / 26 (Master-at-Arms day one confirmed tier 1, 2026-11-23)
- kb/classes/ascendancy-trials.md — 8 points, 2 per trial step; Sekhemas (Djinn Barya) vs Trial of Chaos (Inscribed Ultimatum) point schedule; changing ascendancy
- kb/classes/passive-tree.md — 0.5.5.9 baseline: 984 notables, 33 keystones (listed), 18 jewel sockets; attribute nodes (needs-1.0-check)
- kb/classes/weapon-set-points.md — 24 (+1) from campaign, Books of Specialisation, Witchhunter Weapon Master (100)
- kb/classes/respec.md — Hooded One / Doryani, full gold-per-point table L1–100, attribute-node switch = half (leaning), ascendancy refund (done)

## Items
- kb/items/bases-implicits.md — what a base decides, base counts, culture tags, full ring/amulet/belt implicit lists with drop levels
- kb/items/rarity.md — 4 rarities, 1+1 / 3+3 affix limits, hidden 10-tier rarity roll, Unidentified Tier 2–5 mod culling, Exceptional items, unique tiers
- kb/items/affix-tiers.md — mod level/group/weights, higher tier = better in PoE2, example ladders (life, res, MS, %phys), special mod kinds
- kb/items/item-level.md — ilvl = monster level (+1 magic/rare, +2 boss), waystone T1=65…T16=80, what each tier unlocks (ilvl 82 for top mods), XP penalty; 1 conflict
- kb/items/quality.md — quality effect per type, quality currencies + catalysts, amount scales down with ilvl, Vaal Infusers / 30% drops (partial)
- kb/items/sockets-augments.md — augments (runes/soul cores/idols), max sockets (2 body/2H, 1 other), Artificer's Orb, augment level ladders (partial)
- kb/items/corruption.md — Vaal Orb outcomes (gear/uniques/gems/waystones), corruption implicit pool, altars, Architect's Orb, Vaal Cultivation, sanctified
- kb/items/loot-pickup-heuristics.md — creator pick-up rules: value tiers, unid tier 0–5, per-class rules, exceptional/chanceable bases, disenchant outputs (tier 5, unverified; ilvl claim conflicts)
- kb/items/uniques-index.md — 441 uniques by class count, how uniques work, sources, Common→Mythic tiers, boss-restricted list (partial, early-access tables)
- kb/items/uniques-armour.md — unique names: body armour, helmet, gloves, boots, shield (0.5.5.9)
- kb/items/uniques-other.md — unique names: weapons, off-hands, rings, amulets, belts, jewels, charms, flasks (0.5.5.9)

## Crafting
- kb/crafting/currency-index.md — every core orb with effect + drop level; Greater/Perfect min mod levels (35/50, 55/70); sockets/gem/utility/Vaal currency; PoE1 data leftovers
- kb/crafting/omens.md — 45 omens grouped by target (Exalt, Chaos, Annul, Regal/Alch, essence, desecration, Divine/Vaal/Chance, non-crafting)
- kb/crafting/essences.md — Lesser/normal/Greater (magic→rare) vs Perfect/corrupted (rare: remove + add), drop levels, families and effects (partial)
- kb/crafting/desecration.md — unrevealed mod → choose 1 of 3 at Well of Souls (Act 2), bone types/tiers, Amanamu/Ulaman/Kurgal mods + omens (partial)
- kb/crafting/catalysts.md — 13 jewellery + 13 Refined jewel catalysts, 1% mod magnitude per 1% quality, Breach-only
- kb/crafting/league-crafting.md — 0.5 Runes of Aldur: Remnants, Verisium, Runeforging (Runic Ward), Alloys, unique runeforging, Fluxes, unlock by act (1.0 Reforging → strategy/official-1.0-reveal)
- kb/crafting/recombinator.md — removed in 0.5; how it worked; omen leftover in data
- kb/crafting/approach.md — 0.5 one-crafted + one-desecrated mod rule, deterministic vs gamble tools, common guide sequences
- kb/crafting/craft-costs.md — expected-cost method (cost ÷ p), unit costs per step (Forbidden Rites 2026-11-17), EV examples; omens/essences/bones unpriced (partial)

## Economy
- kb/economy/currency-exchange.md — order book, instant vs limit orders, blocking orders, gold fee (no refund), 10 orders, Ange Act 4 (conflict), order book in-game only, Exalt base unit
- kb/economy/trade-site.md — 3 trade methods, async trade via Merchant's Tabs/Faustus (buyer pays gold fee), trade2 instant-buyout filter
- kb/economy/gold.md — untradeable, league-bound; sinks (respec, gambling, exchange/async fees); 1.0 Conquerors troops cost campaign gold
- kb/economy/price-sites.md — GGG hourly exchange API (tier 1, live-tested), poe.ninja exchange overview (~hourly, volume per hour), poe2scout; how to read
- kb/economy/league-lifecycle.md — Exalt inflation (38 → 549 ex/div), day 1–3 / week 1 / mid / late patterns with 0.5 numbers
- kb/economy/price-snapshot-2026-11-17.md — poe.ninja Currency tab, Forbidden Rites, 2026-11-17: 1 div ≈ 11 chaos ≈ 528 ex; all core orbs priced; volume/hour
- kb/economy/value-retention.md — what holds (Divines, endgame crafting currency, lineage, fragments, week-1 league chase items) vs decays; David's 1.0 rules

## Campaign (0.5.5.9 — 1.0 restructures)
- kb/campaign/area-levels.md — area level ranges per act (A1 1–15, A2 16–31, A3 33–45, A4 46–53, Interludes 54–56, maps 65+)
- kb/campaign/act-1.md — Ogham zones/levels/bosses, permanent rewards (4 pts, 30 spirit, 10% cold, 20 life, Salvage Bench) (partial)
- kb/campaign/act-2.md — Vastiri zones/bosses, rewards (4 pts, 10% lightning, relic choice — conflict), Well of Souls, Sekhemas (partial)
- kb/campaign/act-3.md — Vaal jungle zones/bosses, rewards (4 pts, 30 spirit, 10% fire, utility choice, Reforging Bench) (partial)
- kb/campaign/act-4.md — Kingsmarch islands zones/bosses (46–53), rewards (4 pts — source conflict, 5% mana, lesson/tattoo/flask choices) (partial)
- kb/campaign/act-5.md — 1.0: Oriath; A5+A6 = 24 areas, 18 bosses, 20+ Champion Rares (tier 1); possible A5 quests in 0.5 data [INFERRED] (partial)
- kb/campaign/act-6.md — 1.0: final act; official A5+A6 counts; 0.5 "Act 6" data = Interludes (partial)
- kb/campaign/interludes.md — 0.5 three Interludes (zones, rewards: 8 pts, 40 spirit, 5% life); removed in 1.0 per GGG
- kb/campaign/permanent-rewards.md — 0.5 totals (24 pts, 100 spirit, 10% each res, 20 life + 5%, 5% mana), by act incl. Act 4 + Interludes
- kb/campaign/quest-rewards.md — per-quest gem/item rewards Acts 1–4 + Interludes + map quests (PoE2DB, 0.5), league-mechanic rewards, uncut gem level by drop level (done; rebuild at 1.0)
- kb/campaign/levelling-routes.md — 0.5 navigation cues, speed benchmarks (<5 h twink), routing principles, XP penalty (partial)

## Builds (0.5.x; rebuild on 1.0 patch day)
- kb/builds/ice-shot-deadeye-levelling-0.5.5.md — act-by-act practice playbook: gems/supports by level, ascendancy order, gear breakpoints (11/16/28/33), per-act pickups, totals, post-campaign path (0.5.5, [ML]/[ME] single-source; open items listed)
- kb/builds/starter-archetypes.md — 0.5 Mobalytics ascendancy tiers, Fubgun 0.5.5 starter tiers, recurring archetypes, 1.0 official rework list (Mercenary, Infernalist, Blood Mage, Chayula)
- kb/builds/budget-tiers.md — working tier cut-offs (SSF / ≤5 div / 5–50 / 50+), sourced anchors, SSF craft baseline, divine drift, first-divine priorities
- kb/builds/levelling-gear.md — weapon base drop levels by class, martial craft loop (11/16/28/33), caster +level mod breakpoints, boots MS tiers, campaign resist checkpoints
- kb/builds/defence-checklist.md — 8-step layering checklist (res, chaos, pool, primary layer, recovery, avoidance, stun/ailments, DoT) linked to mechanics docs

## Strategy
- kb/strategy/official-1.0-reveal.md — tier-1 full-release page: launch/F2P, A5–6 counts, Shadow (Stealth, traps, Assassin), Duelist (Stances, Master-at-Arms), Conquerors (campaign missions/POIs, stronghold, Reforging → fractured mods, Blood Lord, commanders, 100+ castle faction war), uniques/supports/tree
- kb/strategy/dev-statements-1.0-league.md — dev interviews (ExileCon 2026, ASR): Conquerors league mechanic — 3 faction castles, commanders, troops, hunting grounds, gold, pinnacle repeatability, no Ubers yet (tier 1 via transcript)
- kb/strategy/dev-statements-1.0-balance.md — dev interviews: crit chance off the tree, nerf stance, necrotic poison, Shadow + Duelist, Act 4 trial cut, fractured-item crafting + ~15 new currencies, jewel exploit; unverified rumours flagged
- kb/strategy/sekhemas-currency-farm.md — creator view: Sekhemas jewels/relics/carries profit centres (tier 5, undated prices, 1.0 changes crit jewels)
- kb/strategy/rarity-value.md — creator claim that rarity isn't essential for farming vs dev stance on rarity
- kb/strategy/atlas-starter-strategy.md — 0.5.5 atlas loop and Jade Isles farm (tier 5, unverified)
- kb/strategy/build-copy-method.md — pick / learn / copy method for builds; no game-data claims
- kb/strategy/league-start-framework.md — effort tiers, farm-first build choice, 5-div T15 test, map-tier checkpoints (T1–6/T7/T11/T15), investment cut-off; compared with David's plan (from video transcript)
- kb/strategy/league-lifecycle-pricing.md — late-league uncut spirit gem spike (with L8/L10/L12 level reqs) and crafting-currency prices (0.5.5 Forbidden Rites, volatile)
- kb/strategy/practice-build-0.5.5.md — 0.5.5 practice pick for 1.0: Ice Shot Deadeye levelled on Lightning Arrow; what carries over, what won't, tweaks
- kb/strategy/my-profile.md — player profile: hours, league type, goals, effort tier (super-sweat), farm leanings

## Topic folders still empty (see tracker)
endgame/ (deferred to 1.0 patch notes)
