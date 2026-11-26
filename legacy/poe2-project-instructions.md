# PoE2 1.0 League Start — Project Instructions

## Purpose
Plan and run David's Path of Exile 2 1.0 league start (Conquerors of Wraeclast, launches 11 Dec 2026 PST). Pick the league starter / main farmer, plan leveling, atlas, crafting and money-making, then fund a second "comfy" AFK character.

## Player profile
- Trade league, Softcore.
- Played every Early Access season since Dec 2024. Knows the game; skip beginner explanations.
- Launch week: ~12 hours/day.
- Playstyle for the farmer: walk around and kill everything, low thinking, no struggle. Goal = most efficient currency farming. Fun/active builds come later, paid for by the farmer.
- Risk tolerance: glass cannon is fine through the campaign and early maps if damage is high (player skill covers it). By the time maps scale (red maps / juiced), the build MUST have real layered defences, because skill can't stop big one-shots. Score starters on "defence ceiling once geared", not just early tankiness.
- Sell curve (David's thresholds): Act 1 anything >= 1 ex; Act 2 >= 3 ex; Act 3+ (power spike) >= 10 ex; maps >= 50 ex.
- Campaign style (changed 17 Nov, replaces 10 Nov "near-complete campaign + 100% league mechanic"): super-sweat skip route. Practised route, skip anything that doesn't give permanent power, needed gems/items or real currency. League-mechanic content in the campaign only where its reward beats the time cost — decide per encounter type once 1.0 notes are out.
- Target: reach maps on day 1.
- Character 2 (later): comfy semi-AFK loop build (reference: Lazy Exile's Immortal Witchhunter Frostbolt Infinite Loop, 0.5.5). Only if the loop survives 1.0 changes.

## Agreed plan
1. Character 1 = main farmer from day one. Level the same character (best campaign skills for that class), respec into the farming setup at early maps. No separate leveler + reroll.
2. Farm first, build second (17 Nov): choose the most profitable farm, then the starter that farms it best. Main focus: the new league mechanic; leaning Ritual or Vaal temple; Expedition logbooks liked for easy early currency. Final farm = whatever is most profitable (pre-launch ranking, re-checked on poe.ninja days 2–3).
3. Starter filter: clear speed, farm fit, defence ceiling by red maps, campaign speed; must pass the 5-div T15 test. Weights and gates in claude/starter-decision-sheet.md.
4. Pick the starter only after the 1.0 patch notes drop (expected about a week before launch). Pre-notes shortlist: Lightning Arrow Deadeye (safe incumbent), Knight Duelist, reworked Infernalist, Blood Mage/Exsanguinate. Shadow ruled out as a starter (too timing-heavy).
5. Early money: new league mechanic (castles, commanders, Hunting Grounds, Reforging material), sell drops, bulk via Currency Exchange, specialise atlas on 1–2 mechanics.
6. From day 3: flipping per the Day-3+ Flipping Strategy doc (https://claude.ai/artifact/4QWdyXdUWboAGq3P4vZUTW).
7. Character 2 = AFK loop farmer, built with currency from character 1.
8. Progression guide (leveling, trade checkpoints, crafting playbook): written only AFTER the build is decided. Agreed outline: day-by-day timeline; campaign skip route + pickups + weapon self-crafting + gold use; trade checkpoints with budgets; map-tier checkpoints (T1–6 push / T7 loot awareness / T11 crafting / T15 farm gate, per kb/strategy/league-start-framework.md); atlas start; red-map defence gate checklist; crafting playbook; not-for-sale ladder; wealth targets per day.

## Gearing / crafting rules (draft, 10 Nov, pre-patch-notes, [INFERRED] thresholds)
- Acts 1–2: no trading; self-craft weapon (Transmute/Aug/Regal/essence). Don't spend gold on gambling (troops need gold).
- Act 3 spike: first trade session; weapon first, then MS boots + resists; cap ~50% of liquid wealth.
- Craft only if expected cost of known-outcome steps <= 60% of cheapest equivalent listing; stop-loss = that listing's price.
- Known-outcome steps only (essence, omens, desecration, Fracturing); no blind Chaos spam.
- Not-for-sale ladder: relax search to top 2–3 mods + open affix -> buy near-miss and finish it -> self-craft capped at 2x closest item and <= 25% of wealth per slot, only for slots that unlock content -> wait for supply (days 3–7).
- Keep a 20–30% of liquid wealth reserve for own-gear crafting once farming is stable.
- Investment cut-off (17 Nov): once the starter farms T15 reliably, spend only if the next divine raises income; otherwise save for the real build.

## Deliverables so far
- Price baseline + 1.0 watchlist dashboard: https://claude.ai/artifact/BKwLBrYZUhPz8k9abReiPA (refresh with 1.0 data on day 2). Raw CSVs in claude/data/.
- Day-3+ flipping strategy doc: https://claude.ai/artifact/4QWdyXdUWboAGq3P4vZUTW (project copy: claude/flipping-strategy.md)
- Starter decision sheet: claude/starter-decision-sheet.md (re-weighted 17 Nov)
- Reveal notes digest + price findings: claude/reveal-notes-and-price-findings.md
- Loot filter custom top block (skeleton): claude/loot-filter-custom-top.filter
- Knowledge library (17 Nov): kb/ — index kb/00-index.md; coverage dashboard https://claude.ai/artifact/9FU4XgSiCzDjeZMfwnr4Au

## Loot filter
- Keep Lazy Exile's "casino" sounds; item tiers are NOT hers — tier by value (NeverSink/FilterBlade economy tiers), 3 value tiers, plus crafting highlights (ilvl 82+ bases, Abyssal Bones, omens, Reforging material, jewels).
- Sound pack: Lazy_Filtersound.zip, unzips to a `Lazy_Filtersound` subfolder in the filter folder. 6veryvaluable = T1 payout; 2currency = T2 currency; 3uniques = T2 uniques/jewels; 1maybevaluable = T3 crafting bases; 4maps / 5highmaps = waystones.
- One FilterBlade strictness per stage of the sell curve (Soft / Regular / Semi-Strict / Strict / Very Strict).
- Fill tier lists after 1.0 launch (200+ new bases, new currency). PC only for custom sounds.

## Working rules
- Always state which patch the info is for (0.5.x vs 1.0). 0.5 builds/numbers are unproven in 1.0 until patch notes confirm.
- Research current info (patch notes, poe.ninja, build guides) before answering anything time-sensitive; cite sources.
- Never invent mod values, gem names, node names, prices or interactions. Mark anything unsourced as [INFERRED] + why.
- Prices: check poe.ninja / trade at the time; never quote stale prices as current.
- Lead with the answer, keep it short. Batch questions in one message.
- Flag plainly when a build or approach won't fit the playstyle/goal above.

## Open items
- 1.0 patch notes: full balance, support gem and unique changes. Next session trigger: patch notes out -> rank farms -> score starters -> pick build -> write progression guide.
- Farm profitability ranking (new league mechanic vs Ritual vs Vaal temple vs Expedition, plus others) — research pre-launch from 0.5.5 evidence + 1.0 reveal notes.
- Super-sweat skip route: needs campaign route research (acts, layouts, required pickups) — 1.0 adds Acts 5–6 and removes Interludes.
- Launch hour (SAST).
- Master-at-Arms (Duelist) on day one?
- Commander loot value vs manual mapping; faction rarity bonus size.
- Does the Frostbolt/Mirror of Refraction loop survive 1.0?
- Exact 1.0 names/classes for new currency (Crimson Iron, Blood Veils per reveal notes) — verify for the filter.
