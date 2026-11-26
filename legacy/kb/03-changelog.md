# Changelog

## 2026-11-26 — Batch 22 (minion gems + Storm Shaman engine gem tables)
- Checked: 1.0 patch notes still not published (web search 2026-11-26 returns only early-access patches). Endgame stays deferred.
- Source: PoE2DB corpus (crawl 2026-11-23), still unpacked in the session workspace; gem pages parsed with a script.
- New docs:
  - gems/minion-skills (partial) — engravable minion gems by tier with spirit/mana at gem 1/10/20, plus minion skills from uniques, tree, ascendancy, class and 0.5 league content; sceptre "Minions have X% increased maximum Life" ladder (ilvl 2 → 80, 21–25% → 46–50%). Key finding: level-scaled persistent minion gems get cheaper with gem level (Skeletal Brute 165 → 54 → 48 spirit). PoE2DB labels that table column "Mana"; values match the Reservation line → [INFERRED] spirit.
  - gems/elemental-caster-gems (done) — Spark (incl. Cold-Infused 12–17 spark circle), Flame Wall (ignite value, added fire/lightning to projectiles), Tornado (tier 11; phys + per-absorbed-element DPS), Thunderstorm. Key finding for the own build: **Thunderstorm's Drench has an enemy-level cap** (gem 16 → 76, gem 17 → 78, gem 18+ none shown) — Drench does nothing on T13+ at gem 16 and on T15+ at gem 17 [INFERRED arithmetic from waystone levels].
- Updated: mechanics/minions (spirit section rewritten from per-gem data; minion level = 2 × gem level now confirmed across every minion gem; PoE2DB's 12 s base resummon stat noted beside the wiki's 7 s revive figure — not reconciled, [INFERRED]).
- Tracker: 2 new gem rows; minions row and Storm Shaman build rows annotated. Index updated. Tracker presented to David.
- Conflicts: none new (the 7 s vs 12 s minion revive numbers may measure different things — logged as a note in mechanics/minions, not a conflict yet).
- Follow-up: builds/storm-shaman-levelling should get the Thunderstorm gem-18 note on its next edit. Dashboard CSV not regenerated (re-run kb/tools/md_to_csv.py).

## 2026-11-25 — Batch 21 (campaign boss data, Acts 1–4)
- Source route: David connected C:\PoE2\poe2db mid-session; PoE2DB corpus (crawl 2026-11-23) staged and unpacked. Boss pages parsed with a script (tools kept in the session workspace only) → life/damage multipliers, resistances, per-skill "% more" values, phys→element conversion, cooldowns, the "cannot be avoided by dodge roll or evaded or blocked" stat, summon skills, ailment-buildup boosts.
- New docs (partial): campaign/boss-data-acts-1-2 (22 bosses) and campaign/boss-data-acts-3-4 (23 bosses). Stat blocks only; fight choreography still uncaptured (needs tier 1–3 text, not internal skill ids).
- Findings worth flagging: Count Geonor's thrust projectile = 160% more, 75% cold, pierces, 500% more freeze buildup, unavoidable; Act 2 bosses mostly resist fire (7/10), Act 3 too (6/11 at 45–90%); Act 4 shifts to cold/lightning; Benedictus has 8 unavoidable skills; most act-ending bosses carry at least one unavoidable 150–350% more hit.
- Parser fix logged: PoE2DB splits highlighted resistance values onto two lines (e.g. "90" / "%", "-15" / "%") — first pass misread them as missing. Several bosses list 90%; monster default max res is 75% → recorded as [INFERRED] "acts as 75% unless max res raised".
- Updated: campaign/act-1…act-4 status lines now point to the boss-data docs; mechanics/recovery (+ Strength gives +2 life per point, PoE2DB); mechanics/mana-costs (Int +2 mana confirmed by PoE2DB; upfront vs per-second costs; default attacks cost nothing; PoE2DB Gem page "Cost Multiplier only" note marked stale). Corpus has no statement on cost-multiplier stacking, AoE radius scaling or base life per level.
- Conflicts: none new.
- Tracker: new row "Campaign boss data, Acts 1–4" (partial); act rows and recovery/mana rows updated. Index updated. Dashboard CSV not regenerated (re-run kb/tools/md_to_csv.py).

## 2026-11-25 — Batch 20 (mechanics gap-fill)
- Checked: 1.0 patch notes still not published (web search 2026-11-25). Endgame stays deferred.
- Source route: PoE2DB corpus folder access was refused this session, so poe2wiki was read through the built-in browser (MediaWiki parse API via page JavaScript — strips to prose). After ~20 calls the wiki switched to a Cloudflare check with a checkbox (HTTP 429); not clicked. Remaining lookups via web search/fetch (Mobalytics, poe2wiki snippets).
- New docs:
  - mechanics/damage-calculation (done) — increased adds / more multiplies (same-source more stacks additively), full outgoing and incoming order of operations, armour before resistances, deflection after damage-taken mods, block after stun/ailment rolls, DoT timing, weapon-local mods. poe2wiki "Receiving damage" (tier 2) flags its own order as needing re-test.
  - mechanics/mana-costs (partial) — cost paid over activation (no refund on cancel), triggered/granted skills cost 0, support cost multipliers; stacking multiplicative is [INFERRED] from PoE1; mana pool 34 + 4/level + 2/Int (Mobalytics); 4%/s base regen (confirmed).
- Updated:
  - mechanics/bleed → done: only the strongest bleed deals damage (poe2wiki Bleeding, replaces [INFERRED]); Rupture, Blood Loss, Incision (+10% bleed chance per stack).
  - mechanics/attack-cast-speed (still partial): use-time formula, 33 ms server-frame cap (~30.3 actions/s), action speed separate, local attack speed multiplicative, dual wielding rules (same class; no caster/spear/flail; no inherent bonus; Parry needs off-hand sword; combined-hit crit rule).
  - mechanics/recovery (still partial): base regen (mana 4%/s; life/ES none), how flat/%/increased/more/recovery-rate regen combine.
  - mechanics/area-projectiles (still partial): poe2wiki AoE page checked — no mechanics text; √ radius rule still tier 5 only (more player measurements added); dodge roll gives no AoE avoidance.
- Conflicts: 2 new open (dual-wield combined vs separate hits; regen rate vs recovery rate multiplier). 1 resolved conflict got a 4th agreeing source (ailments not double-dipping damage mods).
- Follow-up not done: builds/kb-test-frostbolt-chronomancer-damage-0.5.5 still marks the increased/more rule [INFERRED] — update text to cite mechanics/damage-calculation on next edit. Dashboard CSV not regenerated (re-run kb/tools/md_to_csv.py).

## 2026-11-23 — KB-test build written (Frostbolt Chronomancer, 0.5.5)
- New docs (partial): builds/kb-test-frostbolt-chronomancer-0.5.5 (design, gem timeline, ascendancy order, gear breakpoints, act checklist, strengths/weaknesses, first 5 map upgrades, Sekhemas pivot + respec gold, 8-step defence) and builds/kb-test-frostbolt-chronomancer-damage-0.5.5 (4 checkpoints with sourced multipliers, swing table). Project docs only — no web, no build guides; off-limits docs not read.
- Results: CP1 Geonor 40–88 DPS vs ~9,200 [INFERRED ×29] → 105–230 s; CP2 2.4–6k; CP3 6.5–11.8k; CP4 17.7–33.8k vs Zarokh ~3.6M at area 75 → 105–205 s; Desperate Alliance runs not viable at mid budget.
- Updated: gems/cold-spell-gems (Frostbolt table extended to L28; EW res values per level).
- Design changes vs first outline: Stormweaver → Chronomancer (node text); Herald of Ice dropped (martial weapon only); Cold Penetration only vs bosses with positive cold res after Elemental Weakness.
- New tracker rows (todo): mana costs & regen (cost-multiplier stacking).
- Tracker + index updated. Dashboard CSV not regenerated (re-run kb/tools/md_to_csv.py).

## 2026-11-23 — Batch 19 (damage-maths data for the 0.5.5 kb-test build)
- Why: the kb-test build design found the KB had no per-level gem damage, support values, monster life or ascendancy node text. Filled from the local PoE2DB corpus ([[tools/poe2db-corpus]], tier 2, crawl 2026-11-23) and RePoE mods.json (tier 2, pulled 2026-11-23).
- New docs:
  - gems/cold-spell-gems (done) — Frostbolt (tier 5; full damage table), Ice Nova, Arctic Armour, Herald of Ice (**needs a martial weapon** — not caster-usable), Elemental Weakness (curse has an enemy-level cap tied to gem level: L10 → 52, L14 → 72, L17 → 78).
  - gems/caster-supports (done) — Unleash, Multishot I, Considered Casting (35% more), Cold Penetration (30%), Deliberation (20% more), Inexorable Critical I, Rapid Casting II, Cold Exposure, Cold Mastery.
  - mechanics/monster-life (done) — base monster life per level (derived from 500+ PoE2DB monster pages: L15 134 · L31 637 · L53 3,102 · L65 6,555 · L79 24,852), rarity life multipliers (Magic ×2.48, Rare ×8, Unique ×29), worked boss life, monster resistance column order (Fire/Cold/Lightning/Chaos), Count Geonor 45% cold res.
  - classes/sorceress-ascendancies (done for 0.5) — Stormweaver, Chronomancer, Disciple node text; Arcane Surge values.
  - endgame/sekhemas (partial, 0.5 baseline) — Honour (= life + ES + ward), Honour Resistance cap 75/90, floors/bosses, afflictions, boons, pledges, unique relic text. Written early for the test; rest of endgame stays deferred to 1.0 notes.
  - items/caster-mod-tiers (done) — % spell / % cold / cast speed / spell crit / ES mod ladders by item level (RePoE).
- Conflicts: 1 resolved by game data (monster crit damage bonus = +30%); 2 new open (Cold Exposure trigger wording; Zarokh elemental res 15% vs 0%).
- Still a gap: no explicit "increased adds / more multiplies" rule anywhere in the corpus or KB (only "these bonuses are multiplicative" for specific effects). Mod tier tables are not in the PoE2DB crawl (JavaScript-rendered) — use RePoE. Item base ES/damage values not yet captured. Exact Honour-loss % not published.
- Known typo: mechanics/monster-life "PooE2DB" in the resistances section → fix on next edit.
- Tracker + index updated. Dashboard CSV not regenerated (re-run kb/tools/md_to_csv.py).

## 2026-11-23 — Own build: Storm Shaman (1.0 skeleton) + tools
- New docs (partial): builds/storm-shaman, storm-shaman-levelling, storm-shaman-pivot. Built from first principles at David's request — no build guides. Sources: library docs + PoE2DB corpus crawl 2026-11-23 (tier 2; gem pages Spark, Flame Wall, Tornado, Thunderstorm, Elemental Weakness, Arctic Armour, Apocalypse; Shaman, Oracle; Ritual; Conquerors of Wraeclast league/gems).
- Decisions: farm = Ritual (provisional, re-rank with day 2–3 prices); excluded classes = Shadow + reworked (Mercenary, Infernalist, Blood Mage, Chayula); engine = Spark through Flame Wall (clear) → Tornado absorbing ignited ground + Thunderstorm + Elemental Weakness (Ritual/bosses); Druid → Shaman for Presence exposure and Reactive Growth.
- New 1.0 data seen in the corpus: Elemental Penetration support (30% pen, hits only) on PoE2DB's Conquerors gems page — consistent with the reported merge of element penetration supports.
- New tools docs indexed: tools/poe2db-corpus, tools/codex-app (Exile's Codex now on GitHub Pages, 87 item classes / 26,374 mods parsed from the crawl).
- Tracker: added rows for the three build docs. Open: Flame Wall's ignited area counting as an "Elemental Ground Surface" for Tornado (verify in game); Shaman Rage cost vs Druidic Champion.

## 2026-11-23 — Batch 18 (official 1.0 reveal + quest rewards)
- Checked: 1.0 patch notes not published yet (web search 2026-11-23); Exiled Bench (citing Maxroll) says they come ~1 week before 11 Dec. All `todo` rows are still deferred to them, so this batch filled partial docs.
- New doc: strategy/official-1.0-reveal (done, tier 1) — pathofexile2.com/fullrelease read in full via the built-in browser. Covers F2P launch, A5+A6 = 24 areas / 18 bosses / 20+ Champion Rares, Shadow (Stealth, traps, Assassin), Duelist (Ready/Sand/Blood Stances, Master-at-Arms), Conquerors (70+ campaign POIs, 20+ missions, stronghold with 3 factions and 20+ buildings each, Reforging into fractured mods, Blood Lord storyline, up to 3 commanders running maps/Towers/Tablets, 100+ castle faction war after the storyline), 40+ new / 70+ reworked uniques, support rebalance, jewel sockets moved into clusters, Mercenary background reload.
- Updated: campaign/act-5, act-6 (official counts; PoE2DB "Act 5" quests in 0.5 data flagged [INFERRED] as early 1.0 content; PoE2DB "Act 6" = 0.5 Interludes). campaign/quest-rewards partial → done for 0.5 (per-quest rewards Acts 1–4, Interludes, map quests from PoE2DB Quest; rebuild at 1.0).
- Conflicts: 2 new — Conquerors POI count (official 70+ vs Maxroll snippet 17, open); Master-at-Arms day one (resolved by tier 1). 2 updated with a PoE2DB Quest source — Act 2 relic altar now leaning Mobalytics (charm slot + charges or duration); Act 4 weapon-set points now leaning Omniphobia + Trail of the Ancestors.
- Tracker: added missing row for builds/ice-shot-deadeye-levelling (partial) and the reveal doc. Index and sources registry updated (fullrelease page readable via built-in browser only; PoE2DB Quest page; reveal-summary blogs as tier 5).
- Not done: classes/index text still says Master-at-Arms day-one uncertain via launch brief → fix on next edit. Dashboard CSV not regenerated this batch (re-run kb/tools/md_to_csv.py). charms.md garbled Siphon-aura sentence still pending.

## 2026-11-17 — Ice Shot Deadeye levelling playbook
- New doc: builds/ice-shot-deadeye-levelling-0.5.5 (partial) — act-by-act follow-along for the practice char. Merges Mobalytics levelling + endgame guides (tier 3, single-source) with KB act docs, levelling-gear, ascendancy-trials, gem-levels.
- Open items in the doc: exact passive order, L24 skill-swap contents, ascendancy point cost per node, weapon-set point layout ([ML] shows 20 per set vs KB 24 from quests), which campaign source gives an L8 spirit gem.
- Not updated: 01-coverage-tracker (no row for this doc yet), 04-conflicts (relic-altar/Act 4 reward differences between [ML] and PoE2DB not re-logged; existing entries cover them).

## 2026-11-17 — Transcript ingest (8 YouTube transcripts: 2 dev-interview sets + 5 creator videos)
- Source handling: David confirmed all are YouTube transcripts and the interviews are with the game dev (Jonathan/Mark, ExileCon 2026 and a Thailand interview). Transcripts are auto-generated (ASR) and imperfect — dev-interview claims recorded as tier 1 via ASR; creator videos tier 5 (leads only). Garbled names flagged [INFERRED] (e.g. "Sarcophagus/Sirus/Zeratul" ≈ Sekhemas/boss; "Runes of Aether" ≈ Aldur).
- New docs (all done): strategy/dev-statements-1.0-league (Conquerors: 3 faction castles, commanders, troops, hunting grounds, gold self-funding, repeatable pinnacles, no Ubers until balanced), strategy/dev-statements-1.0-balance (crit chance off the tree, nerf stance, necrotic poison, Shadow + Duelist, third Act 4 trial cut, fractured-item crafting + ~15 new currencies, five-mod jewel exploit = bug, permanent campaign rewards unchanged for now), strategy/sekhemas-currency-farm, strategy/rarity-value, strategy/atlas-starter-strategy, strategy/build-copy-method, items/loot-pickup-heuristics.
- Status flip: mechanics/crit → needs-1.0-check (GGG says crit chance leaves the passive tree in 1.0). Tier-5 patch rumours (Cast on Crit removal, gaseous poison, Chayula Threads of Chaos, +levels nerf) recorded as unverified only.
- Conflicts: 1 new open (T15 map drop item level: creator "always 79" vs item-level.md +1 rare / +2 boss); 1 value-judgement note (exceptional-base quality bonus). Both in 04-conflicts.
- Housekeeping done: index (this batch + batch 17 status changes), sources registry (poe2wiki-via-browser, transcripts), conflicts rewritten.
- Tracker 109 rows; dashboard dataset v19.
- Still to fix: charms.md garbled Siphon-aura sentence (fix on next edit).

## 2026-11-17 — Batch 17 (partial-doc fill, mechanics + respec)
- Updated: mechanics/charms (done — 13 bases with level, charges/use, duration, trigger → effect; RePoE + PoE2DB agree), classes/respec (done — full L1–100 gold-per-point table from poe2wiki), mechanics/chill-freeze, shock-electrocute (still partial — monster ailment threshold ≈ max life for normal monsters, lower for Unique bosses/some Rares; no numeric values published; boss freeze threshold rises per freeze then decays), mechanics/minions (still partial — minion level = 2× gem level, no general inheritance rule, spirit examples).
- Checked, no new data: mechanics/stun (PoE2DB Stun page gives no monster thresholds, heavy-stun duration or immunity length), mechanics/recovery (only 0.2% max life/s node values; base regen not stated). Both stay partial.
- Conflicts: 2 new open — respec cost depends on node depth (Maxroll) vs level only (poe2wiki); charm slot cap 3 vs bonus-slot items. 1 moved to resolved-leaning — attribute node switch = half a refund (poe2wiki Respec URL now redirects to the page saying half).
- Source note: poe2wiki.net IS readable through the built-in browser — Anubis passes after ~5 s wait; tables hidden behind "Expand" can be read with page JavaScript. PoE2DB Minions page is 387k chars; only the first 100k read.
- Dropped: tier-5 glama.ai "research" ailment formulas (PoE1-derived, not PoE2) — not recorded as facts. Timesaver "5× ascendancy refund" downgraded to tier 5 (boosting/currency site).
- Not done (needs David): craft-costs omen/essence/bone prices — waiting on poe.ninja saves.
- Tracker + dashboard CSV updated (102 rows; dashboard dataset v18).

## 2026-11-17 — Batch 16 (builds) + endgame deferral + practice-build pick
- Endgame (15 topics) deferred to the 1.0 patch notes at David's request.
- New docs (done, 0.5.x): builds/starter-archetypes, budget-tiers, levelling-gear, defence-checklist.
- New doc: strategy/practice-build-0.5.5 (Ice Shot Deadeye, levelled on Lightning Arrow; answer to David's practice question).
- New tier-1 source: GGG 1.0 press release (2026-11-11) — named reworks: Mercenary, Infernalist, Blood Mage, Acolyte of Chayula.
- Game data used: weapon base drop levels, MS boot tiers, spell +level mod tiers.
- Conflicts: 1 new open — name of the 30% boots MS tier.
- Maxroll pages now refuse fetches (robots) — Maxroll claims via third parties marked unverified.

## 2026-11-17 — Batch 12 (campaign II) — campaign section first pass complete
- New docs: campaign/interludes (done — 0.5 reference, removal in 1.0 confirmed by GGG quotes); act-4, act-5, act-6, quest-rewards, levelling-routes (partial).
- Act 4 from PoE2DB + game data (zones 46–53, bosses, rewards). Acts 5–6: announcement-level only (Act 5 = Oriath, ExileCon demo; Steam announcement confirms six acts on 11 Dec). PoE2DB 1.0 note "Act 5 is 2 interludes long" recorded with [INFERRED] reading.
- Quest rewards: Act 1 uncut-gem rewards, league-mechanic guaranteed rewards, uncut gem level by drop level (poe2wiki).
- Levelling routes: 0.5 navigation cues, speed benchmarks, routing principles.
- Conflicts: 1 new open — which Act 4 bosses give the weapon-set points (PoE2DB vs Mobalytics vs poe2wiki).
- Tracker + dashboard CSV updated.

## 2026-11-17 — Batch 11 (campaign I) + price snapshot
- Price snapshot: parsed David's saved poe.ninja Currency page (Forbidden Rites, 2026-11-17) → economy/price-snapshot-2026-11-17.md (1 div ≈ 11 chaos ≈ 528 ex). crafting/craft-costs.md updated with unit costs + EV examples (still partial: omens/essences/bones not on the Currency tab).
- New docs: campaign/area-levels, permanent-rewards (done); act-1, act-2, act-3 (partial — boss mechanics not captured).
- 0.5 totals: 24 weapon-set points, 100 spirit, +10% each ele res, +20 life + 5% life, 5% mana.
- Conflicts: 1 new open — Act 2 relic altar options.

## 2026-11-17 — Batch 10 (economy) — economy section complete
- New docs: economy/currency-exchange, trade-site, gold, price-sites, league-lifecycle, value-retention.
- New tier-1 source: GGG Currency Exchange API (hourly historical digests); live-tested via web fetch.
- poe.ninja / poe2scout unreachable from workspace; prices come from David's pastes/CSVs.
- Conflicts: 2 new open — exchange NPC/unlock; exchange gold-fee scaling.

## 2026-11-17 — Batch 9 (crafting II) — crafting section complete
- New docs: crafting/catalysts, league-crafting, recombinator, approach (done); craft-costs (partial).
- Recombinator removed in 0.5; one crafted + one desecrated mod per item since 0.5.

## 2026-11-17 — Batch 8 (uniques + crafting I)
- New docs: items/uniques-index, uniques-armour, uniques-other (partial); crafting/currency-index, omens (done); essences, desecration (partial).
- Jeweller's Orb conflict resolved by game data (3/4/5 sockets); 2 new open conflicts (Essence of Ice, alt gem quality).

## 2026-11-17 — Batch 7 (items)
- New docs: items/bases-implicits, rarity, affix-tiers, item-level, corruption (done); quality, sockets-augments (partial). 3 conflicts (2 resolved).

## 2026-11-17 — Batch 6 (classes)
- New docs: classes/index, ascendancy-trials, weapon-set-points (done); respec (partial); passive-tree (needs-1.0-check). 1 resolved + 1 open conflict.

## 2026-11-17 — Batch 5 (gems)
- New docs: gems/uncut-gems, gem-levels, support-tiers, lineage-supports, socketing-limits, meta-trigger (done); quality (partial). L8/L10/L12 spirit gem level reqs resolved (26/36/46).

## 2026-11-17 — Batch 4 (resources & systems) — core mechanics complete
- New docs: mechanics/flasks, spirit-reservation, totems, dodge-roll, weapon-swap, skill-interactions (done); recovery, charms, minions (partial).

## 2026-11-17 — Batch 3 (defences)
- New docs: mechanics/resistances, armour, evasion, energy-shield, block, deflection (done); stun (partial). 2 conflicts.

## 2026-11-17 — Plan decisions (pacing, farm-first)
- David's decisions: super-sweat skip route; farm-fit + 5-div T15 gate; farm = most profitable (leaning new league mechanic, Ritual, Vaal temple; likes Expedition logbooks).

## 2026-11-17 — Video transcript ingested
- Added kb/strategy/league-start-framework.md.

## 2026-11-17 — Batch 2 (ailments)
- New docs: mechanics/ailments-overview, ignite, poison, exposure-penetration (done); chill-freeze, shock-electrocute, bleed (partial).

## 2026-11-17 — Bulk game-data source added
- RePoE PoE2 export (game 0.5.5.9) added to 02-sources as tier 2.

## 2026-11-17 — Tracker dashboard
- Built "PoE2 KB Coverage Tracker" dashboard (https://claude.ai/artifact/9FU4XgSiCzDjeZMfwnr4Au).

## 2026-11-17 — Source reachability check / Phase 0
- poe2wiki.net blocked (Anubis); control docs (00–04) created; tracker populated (95 rows, batches 1–16).
