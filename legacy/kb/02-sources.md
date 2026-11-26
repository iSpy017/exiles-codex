# Source Registry

Tier 1 = official · 2 = data refs · 3 = guide sites · 4 = economy data · 5 = community (leads only)
"Reachable" = whether Claude can read it (tested 2026-11-17; updated 2026-11-25).

| Source | URL | Tier | Use | Reachable | Last checked |
|---|---|---|---|---|---|
| PoE2 official site / announcements | https://www.pathofexile.com/poe2 | 1 | patch notes, announcements | Plain fetch: NO (needs JavaScript). Built-in browser on David's PC: YES — open, wait ~5 s, get_page_text | 2026-11-23 |
| **PoE2 Full release page** | https://pathofexile2.com/fullrelease | 1 | 1.0 feature reveal: A5–6 counts, Shadow/Duelist mechanics, Conquerors systems, Reforging, commanders, faction war, uniques/supports/tree | YES via built-in browser only (read in full 2026-11-23) | 2026-11-23 |
| GGG forum (patch notes, staff posts) | https://www.pathofexile.com/forum | 1 | patch notes, dev clarifications | YES — forum thread loaded fully | 2026-11-17 |
| GGG 1.0 press release (2026-11-11) | https://www.pathofexile.com/forum/view-thread/4013917/page/1 | 1 | 1.0 scope; named reworks (Mercenary, Infernalist, Blood Mage, Acolyte of Chayula) | YES | 2026-11-17 |
| GGG ExileCon 2026 announcements thread | https://www.pathofexile.com/forum/view-thread/4012710 | 1 | headline 1.0 items only | YES | 2026-11-17 |
| GGG 1.0 patch notes | (not published yet) | 1 | the 1.0 refresh | Not out as of 2026-11-25 web search (cheatcc 1.0 page also says not yet published); expected ~1 week before 11 Dec (Exiled Bench citing Maxroll, tier 5) | 2026-11-25 |
| GGG Developer Docs (API reference) | https://www.pathofexile.com/developer/docs/reference | 1 | Currency Exchange API docs | YES via web fetch | 2026-11-17 |
| GGG Currency Exchange API (live data) | https://web.poecdn.com/api/currency-exchange/poe2/<hour-timestamp> | 1 | hourly historical digests per currency pair, all leagues: volume_traded, lowest/highest stock & ratio. No id = first hour of history (empty). | YES via web fetch only (shell proxy refuses host). ~1.7 MB per hour; fetch truncates at 100k chars → spot checks of named pairs only. Item ids map via RePoE base_items (CurrencyModValues = Divine, CurrencyRerollRare = Chaos, CurrencyAddModToRare = Exalted, suffix 2/3 = Greater/Perfect). | 2026-11-17 |
| **Dev interview transcripts (ExileCon 2026 "Behind the Scenes Interview with Jonathan & Mark About 1.0"; Thailand interview)** | David-supplied YouTube transcripts (project attachments) | 1 (staff statements) via ASR | 1.0 design statements: Conquerors, crit-on-tree removal, balance, crafting. Auto-generated transcript, imperfect — names/numbers garbled in places, flagged [INFERRED]. Re-check against the 1.0 patch notes. | YES (attached by David) | 2026-11-17 |
| **RePoE PoE2 export (game-data JSON)** | https://github.com/repoe-fork/poe2 | 2 | raw game data: keywords (in-game definitions), mods, base items, skill gems, uniques, ascendancies, classes, world areas, augments, passive trees, stat translations | YES — bulk download via git (GitHub allowed in workspace). Snapshot 2026-11-17 = game version 0.5.5.9 (version.txt). Updated automatically each game patch. | 2026-11-17 |
| PoE2DB | https://poe2db.tw/us/ | 2 | game-data numbers, mods, tiers, gems, atlas, quests; formatted pages | YES via web fetch, one page at a time (pages truncate at 100k chars — use offset for the rest; Quest page is 160k chars, read in two parts 2026-11-23; Minions 387k, Mana 330k, Life 460k chars). NO bulk download from the workspace (proxy 403). Local crawl corpus exists ([[tools/poe2db-corpus]]) but needs David's folder grant each session — refused 2026-11-25. Has a 1.0 section. | 2026-11-25 |
| PoE2 Wiki (official community wiki, GGG-hosted) | https://www.poe2wiki.net | 2 | mechanics, items, gems, version history | Plain fetch: NO (Anubis bot protection v1.27.0). Built-in browser on David's PC: YES — navigate, wait ~5 s for Anubis, then read with get_page_text. Faster: from a wiki tab, page JavaScript can call `/api.php?action=parse&page=<Title>&prop=text&format=json&redirects=1` and strip tables/tooltips. **Rate limit:** after ~20 API calls in a few minutes (2026-11-25) the site returned HTTP 429 and a Cloudflare checkbox check — not clicked (bot checks are the user's to complete). Space calls out; ask David to clear the check if needed. Also readable via search snippets. | 2026-11-25 |
| Maxroll PoE2 | https://maxroll.gg/poe2 | 3 | builds, strategy, levelling, patch previews | PARTLY — some guide pages fetched earlier on 2026-11-17; news and tier-list pages now refuse fetches (robots). Claims about Maxroll seen only on third-party sites or search snippets are unverified. "Everything New In PoE2 1.0" and "ExileCon 2026 Recap" seen as snippets 2026-11-23 (used in strategy/official-1.0-reveal, flagged). | 2026-11-23 |
| Mobalytics PoE2 | https://mobalytics.gg/poe-2 | 3 | builds, strategy, mechanics hub, patch-notes hubs | YES — mechanics guides have mixed update dates (some 2024-12, Regeneration 2025-09-17, Mana 2026-11-13); check each page's date | 2026-11-25 |
| Vulkk | https://vulkk.com | 3 | patch overviews (0.2.0g, 0.5.0) | yes (search) | 2026-11-17 |
| poe.ninja PoE2 | https://poe.ninja/poe2 | 4 | prices (exchange overview for currency-type items, trade listings for uniques), builds | NO — economy pages render client-side (fetch returns no tables); shell proxy refuses the host. API docs page (https://poe.ninja/docs/api) IS readable. Get prices via David's paste/screenshot. [INFERRED] built-in browser may work like the official site — untested. | 2026-11-17 |
| poe2scout | https://poe2scout.com | 4 | unique + currency price history (Exalt-relative) | NO — client-rendered page; shell proxy refuses the host | 2026-11-17 |
| David's own price pulls | claude/data/*.csv, claude/reveal-notes-and-price-findings.md, claude/flipping-strategy.md | 4 | dated poe.ninja data (Runes of Aldur / Forbidden Rites, 2026-11-10 & 11-17) | YES (project docs) | 2026-11-17 |
| Creator YouTube transcripts (5): Sekhemas Mirrors currency farm; "Why Rarity is Not Essential for Farming"; "Evaluating Loot and Item Tiers in PoE 2"; "How to Learn and Copy PoE2 Builds"; "PoE2 New Player Atlas Strategy Guide"; plus "ExileCon Highlights and Path of Exile 2 Impressions" | David-supplied (project attachments) | 5 | leads / creator opinion only; prices undated; ASR errors. Used in strategy/sekhemas-currency-farm, rarity-value, atlas-starter-strategy, build-copy-method, items/loot-pickup-heuristics | YES (attached by David) | 2026-11-17 |
| kami-labs.fr patch-note summaries + tier-list summaries | https://kami-labs.fr/en/path-of-exile-2/ | 5 | lead only — patch dates; summary of Fubgun's 0.5.5 tier list; always verify | yes | 2026-11-17 |
| 1.0 reveal summaries: Exiled Bench, accountshark, koni_pu3 (note.com) | https://www.exiledbench.com/blog/poe2-1-0-crafting-changes · https://accountshark.net/blog/path-of-exile-2-1-0-full-release-december-11-shadow-duelist-conquerors-of-wraeclast-exilecon-2026 · https://note.com/koni_pu3/n/n23ea171383fd | 5 | corroboration of tier-1 reveal counts; patch-notes timing lead. accountshark sells accounts → leads only | yes (search snippets) | 2026-11-23 |
| Reddit r/PathOfExile2 etc. | — | 5 | leads only, verify vs 1–3 | not tested | not yet |

## Using the RePoE export
- Clone (fast, English files only): `git clone --depth 1 --filter=blob:none --no-checkout https://github.com/repoe-fork/poe2`, then sparse-checkout the needed `data/*.json` files. ~30 MB for keywords, mods, base_items, skill_gems, uniques, ascendancies, characters, world_areas, augments.
- It is a working copy in Claude's session workspace only — re-clone each session; never paste raw JSON into project docs (paraphrase + cite).
- Caveats: contains legacy/unused PoE1-era entries (e.g. characters.json lists 12 classes incl. Marauder, Duelist, Shadow, Templar; ascendancies.json has 37 ids incl. placeholders; PoE1 currency like Chromatic/Fusing/sextants; Omen of Recombination after the Recombinator's removal). Also "[DNT]" placeholder bases. Cross-check lists against poe2db/poe2wiki before treating an entry as live in-game.
- base_items.json `drop_level` = earliest item level a base drops at; mods.json `required_level` = item level needed to roll the mod. Charm entries also carry charges_max, charges_per_use and duration (tenths of a second).
- uniques.json is from game files; drop restrictions are not in game data (Path of Building's hand-maintained unique list exists at github.com/repoe-fork/pob-data).
- Licence: RePoE code repo LICENSE.md; game data © Grinding Gear Games.

## Licences
- poe2db.tw and poe2wiki.net: content under CC BY-NC-SA 3.0 (https://creativecommons.org/licenses/by-nc-sa/3.0/) unless otherwise noted. Personal, non-commercial library with a link back on every entry satisfies attribution; any doc that reuses their content stays under the same licence if shared. Project rule to paraphrase still applies.

## Blocked (RMT / seller marketing — never cite)
u4gm, mmoexp, aoeah, iggm, and similar currency-seller sites. Treat timesaver.gg, boostmatch.gg, skycoach, xboosty, lfcarry, instant-carry, accountshark and similar boosting/currency/account-selling blogs as tier 5 leads only.

## Untrustworthy — do not cite
- `*.pages.dev` "Path of Exile 2 Wiki" sites (e.g. guide-path-of-exile-2-wiki.pages.dev, poe2guides.pages.dev, earlyguides.pages.dev) and similar SEO content farms. They impersonate a wiki and contradict each other on basic numbers (unique counts, ascendancy counts). Treat as AI-generated filler.
- Generic aggregator blogs (deltiasgaming, keengamer, mithrie, lootlore web.app, geekyinc, everythingedinburgh, guides-factory, etc.): tier 5 at best.
- Tier-5 AI research dumps (e.g. glama.ai MCP "POE2 research" markdown — its ailment formulas are PoE1-derived): leads only.

## Per-guide pages
| Guide | URL | Tier | Version / updated | Used in |
|---|---|---|---|---|
| Mobalytics 0.5 League Starter Tier List | https://mobalytics.gg/poe-2/tier-list | 3 | 0.5, no date | builds/starter-archetypes |
| Mobalytics How To: Campaign Martial Weapons | https://mobalytics.gg/poe-2/guides/campaign-martial-weapon-crafting | 3 | 2025-12-11 | builds/levelling-gear |
| Maxroll Comprehensive League Start Leveling Guide | https://maxroll.gg/poe2/getting-started/comprehensive-league-start-leveling-guide | 3 | 2025-04-06 (0.2; Cruel-era) | builds/levelling-gear, defence-checklist, budget-tiers |
| Mobalytics SSF Crafting | https://mobalytics.gg/poe-2/guides/ssf-crafting | 3 | 0.5.x | builds/budget-tiers |
| Mobalytics Fubgun Ice Shot Deadeye (endgame) | https://mobalytics.gg/poe-2/builds/ice-shot-deadeye | 3 | 0.5.5, 2026-09-12 | strategy/practice-build-0.5.5, defence-checklist |
| Mobalytics Fubgun Ice Shot Deadeye levelling | https://mobalytics.gg/poe-2/builds/ice-shot-deadeye-leveling-guide | 3 | 0.5.5, 2026-09-12 | strategy/practice-build-0.5.5 |
| Mobalytics Mana | https://mobalytics.gg/poe-2/guides/mana | 3 | 2026-11-13 | mechanics/mana-costs |
| Mobalytics Regeneration | https://mobalytics.gg/poe-2/guides/regeneration | 3 | 2025-09-17 | mechanics/recovery, mana-costs |
| Kami-labs: Fubgun's 0.5.5 tier list | https://kami-labs.fr/en/path-of-exile-2/tier-list-league-start-poe2-0-5-5/ | 5 (summary of tier-3 creator) | 2026-09-02 | builds/starter-archetypes, budget-tiers |
| Grindout leveling guide | https://grindout.com/poe-2/guides/leveling | 5 | undated | builds/levelling-gear |
| Switchblade Gaming HC guide / Titan guide | https://www.switchbladegaming.com/path-of-exile-2/hardcore-guide/ · https://www.switchbladegaming.com/path-of-exile-2/warrior-titan-build/ | 5 | 0.5 | builds/defence-checklist; mechanics/area-projectiles (√ radius) |
| lfcarry / geekyinc tier lists | https://lfcarry.com/guides/poe2-tier-list · https://www.geekyinc.com/path-of-exile-2-tier-list-1-0-classes-ascendancies/ | 5 | 2026-11-16 / ~2026-11-11 | builds/starter-archetypes (usage share, unverified) |
| poe2wiki Passive Skill Tree (respec gold table) | https://www.poe2wiki.net/wiki/Passive_Skill_Tree | 2 | 0.5.x, read via built-in browser 2026-11-17 | classes/respec |
| poe2wiki Receiving damage (order of operations) | https://www.poe2wiki.net/wiki/Receiving_damage | 2 | rev 133460, read via built-in browser 2026-11-25; page flagged "adapted from poewiki, re-test" | mechanics/damage-calculation |
| poe2wiki Cost, Skill speed, Dual wielding, Modifier, Bleeding, Area of effect | https://www.poe2wiki.net/wiki/Cost (etc.) | 2 | revs 134828 / 130082 / 135854 / 135639 / 132925 / 109096, 2026-11-25 | mechanics/mana-costs, attack-cast-speed, damage-calculation, bleed, area-projectiles |
| PoE2DB Charms | https://poe2db.tw/us/Charms | 2 | 0.5.5.9 | mechanics/charms |
| PoE2DB Quest | https://poe2db.tw/us/Quest | 2 | 0.5.x (no version on page), read 2026-11-23 | campaign/quest-rewards, act-5, act-6; conflicts (Act 2 relic, Act 4 points) |
