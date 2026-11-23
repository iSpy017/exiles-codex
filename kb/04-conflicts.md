# Source Conflicts

Format:
## <topic>
- Doc: kb/<path>
- Source A: [title](url), tier N, version, date — says X
- Source B: [title](url), tier N, version, date — says Y
- Status: open | resolved (how, date)

Game-data tie-breaker: RePoE PoE2 export (keywords.json, game version 0.5.5.9) is the in-game keyword text extracted from the game files — tier 2, authoritative for its version. Where it agrees with one side, the conflict is marked "resolved by game data" but both original claims are kept here.

## Monster critical damage bonus
- Doc: kb/mechanics/crit.md
- Source A: [poe2wiki Critical hit](https://poe2wiki.net/wiki/Critical_hit), tier 2, 0.5.x, 2026-11-17 — monsters have 40% less bonus critical damage than players (implies +60%)
- Source B: [Mobalytics Critical Hits](https://mobalytics.gg/poe-2/guides/critical-hits), tier 3, undated, 2026-11-17 — default monster crit damage bonus is 30%
- Status: open. Game-data keyword text only gives the player default (+100%). Check monster stat data or poe2wiki version history.

## Distance where accuracy penalty maxes out
- Doc: kb/mechanics/accuracy.md
- Source A: [poe2wiki Accuracy](https://poe2wiki.net/wiki/Accuracy), tier 2, 0.5.x, 2026-11-17 — up to 90% less accuracy for targets further than 12 m
- Source B: [Mobalytics Accuracy](https://mobalytics.gg/poe-2/guides/accuracy), tier 3, undated, 2026-11-17 — linear up to 90% less at 9 to 12 m or more
- Source C: [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2 (game data 0.5.5.9), 2026-11-17 — no penalty within 2 m, up to 90% less beyond 9 m
- Status: resolved by game data (2026-11-17): 9 m for 0.5.5.9. Wiki's 12 m likely an older value.

## Presence base radius
- Doc: kb/mechanics/area-projectiles.md
- Source A: [poe2wiki Presence](https://poe2wiki.net/wiki/Presence), tier 2, 0.5.x, 2026-11-17 — base radius 6 m
- Source B: [Mobalytics Presence](https://mobalytics.gg/poe-2/guides/presence), tier 3, undated, 2026-11-17 — radius 4 m by default
- Source C: [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2 (game data 0.5.5.9), 2026-11-17 — 4 m default; changed only by Presence Area modifiers, not skill area
- Status: resolved by game data (2026-11-17): 4 m for 0.5.5.9.

## Do damage modifiers apply to ailments after the hit?
- Doc: kb/mechanics/hits-vs-dot.md
- Source A: [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2, 2026-11-17 — ailments from a hit calculate damage from that hit and don't then get damage modifiers applied directly
- Source B: [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), tier 2, 2026-11-17 — modifiers to damage with ailments, DoT modifiers and generic damage modifiers all apply to damaging ailments
- Source C: [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2) "Hit Damage", "Ignite", "Poison", "Bleeding", tier 2 (game data 0.5.5.9), 2026-11-17 — magnitude is set from the hit and "not further affected by any modifiers to the damage you deal"
- Status: resolved by game data (2026-11-17) in favour of A for 0.5.5.9. Source B likely describes an older (early-access) model. Magnitude modifiers still apply when the ailment is created — [INFERRED] from the "Buff/Debuff Magnitude" keyword.

## Poison base: phys only, or phys + chaos?
- Doc: kb/mechanics/poison.md
- Source A: [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3, updated 2026-02-23 — 20% of the hit's physical damage
- Source B: game keywords "Poison" (0.5.5.9), [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), [Mobalytics Poison](https://mobalytics.gg/poe-2/guides/poison) — 20% of physical + chaos
- Status: resolved (2026-11-17): phys + chaos. Source A treated as an omission on a summary page.

## Armour formula constant (10× or 12× damage)
- Doc: kb/mechanics/armour.md
- Source A: [Mobalytics Armour](https://mobalytics.gg/poe-2/guides/armour), tier 3, updated 2025-09-11 — DR = Armour ÷ (Armour + 10 × damage)
- Source B: GGG forum player post ([3684920](https://web.poecdn.com/forum/view-thread/3684920)) and Steam discussion, tier 5, early access (≈Dec 2024) — DR = Armour ÷ (Armour + 12 × damage)
- Source C: [poe2wiki "Protect me from harm"](https://poe2wiki.net/wiki/Protect_me_from_harm), tier 2 — uses 12 × damage in a keystone-specific formula
- Status: open, leaning A (newest; B predates later armour changes). Game keyword text has no formula. Check poe2wiki "Armour" page version history via browser.

## Deflection chance cap
- Doc: kb/mechanics/deflection.md
- Source A: [Mobalytics Deflection](https://mobalytics.gg/poe-2/guides/deflection), tier 3 — capped at 95%
- Source B: [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection), tier 2 — no minimum or maximum deflect chance
- Status: open. Formula (150 × (1 − A/(A+0.12D))) only from Mobalytics; an older Reddit-quoted formula differs (tier 5). Verify on poe2wiki via browser.

## One copy of each support gem per character?
- Doc: kb/gems/socketing-limits.md
- Source A: [poe2wiki Skill gem](https://poe2wiki.net/wiki/Skill_gem), [poe2wiki Gem](https://poe2wiki.net/wiki/Gem), tier 2, 2026-11-17 — only one copy of a support gem can be socketed across all your skills
- Source B: [poe2wiki Spirit Gem](https://www.poe2wiki.net/wiki/Spirit_Gem) version history, tier 2, 2026-11-17 — "removed the restriction of having one of each support gem per character; use as many copies as you like" (lineage supports keep a one-copy limit)
- Status: open, leaning B (it's a version-history entry, so newer than A's page text). Patch number of the change not visible in snippet. Check in game or patch notes.

## Jeweller's Orb socket steps
- Doc: kb/gems/socketing-limits.md
- Source A: [Poe-Vault Currency and Crafting](https://www.poe-vault.com/poe2/guides/currency-and-crafting), tier 3 — Lesser sets a gem to 2 support sockets, Greater sets it to 3 (overwriting)
- Source B: [PoE2DB early-access notes](https://poe2db.tw/kr/markdown_raw?oldid=986), tier 2 (old text) — Lesser upgrades 2 → 3, Greater 3 → 4 (Perfect → 5)
- Source C: [Mobalytics Skill Gem System](https://mobalytics.gg/poe-2/guides/skill-gem-system), tier 3 — gems start with 2, up to 5 via Jeweller's Orbs
- Source D: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) currency text, tier 2 (game data 0.5.5.9) — Lesser "sets a Skill Gem to have 3 Support Gem Sockets", Greater 4, Perfect 5
- Status: resolved by game data (2026-11-17): Lesser = 3, Greater = 4, Perfect = 5 (each sets the count). Matches B's steps; A is wrong for 0.5.5.9.

## Trial of Chaos level for ascendancy points 5–6
- Doc: kb/classes/ascendancy-trials.md
- Source A: [Maxroll Trials of Ascendancy](https://maxroll.gg/poe2/getting-started/trials-of-ascendancy), tier 3, 2026-11-17 — Inscribed Ultimatum level 75+, 10 rounds
- Source B: [Mobalytics Respec Ascendancy](https://mobalytics.gg/poe-2/guides/respec-ascendancy), tier 3; game8, tier 5; 2026-11-17 — level 65+, 10 rounds
- Source C: [poe2wiki Ascension Trial](https://www.poe2wiki.net/wiki/Ascension_Trial) version history, tier 2 — 10-chamber trials lowered from 75 to 65 (7-chamber from 60 to 55)
- Status: resolved (2026-11-17) in favour of 65 via the wiki version history; Maxroll text predates the change.

## Attribute node switch cost
- Doc: kb/classes/respec.md, kb/classes/passive-tree.md
- Source A: [poe2wiki Passive tree](https://poe2wiki.net/wiki/Passive_tree), tier 2 — switching a +5 attribute node costs half a respec
- Source B: [poe2wiki Respec](https://poe2wiki.net/wiki/Respec), tier 2 — same gold cost as respeccing one passive
- Source C: [poe2wiki Passive Skill Tree](https://www.poe2wiki.net/wiki/Passive_Skill_Tree), tier 2, read in browser 2026-11-17 — "half the gold cost as refunding one passive"; the Respec URL now redirects to this page
- Status: resolved-leaning-half (2026-11-17): Respec page redirects to the page that says half; B likely a stale page version. Not verified in game.

## Does respec cost depend on node depth?
- Doc: kb/classes/respec.md
- Source A: [Maxroll Passive Tree](https://maxroll.gg/poe2/resources/poe-2-passive-tree-and-dual-specialization), tier 3, 2026-11-17 — price changes with level and how deep in the tree the node is; also GamesRadar/Gfinity (tier 5) say depth
- Source B: [poe2wiki Passive Skill Tree](https://www.poe2wiki.net/wiki/Passive_Skill_Tree), tier 2, 2026-11-17 — cost rises with character level only; table is by level; Prima (tier 5) says "purely based on your level", all points cost the same when hovered
- Status: open, leaning B (table + in-game hover claim). Maxroll text may be from early access. Check in game.

## Charm slot cap vs bonus slots
- Doc: kb/mechanics/charms.md
- Source A: game keywords "Charms" (RePoE 0.5.5.9), tier 2, 2026-11-17 — max charm slots capped at 3
- Source B: [PoE2DB Charms](https://poe2db.tw/us/Charms), tier 2, 2026-11-17 — belts roll (1–3) plus items/passives add more (Bijouborne +2, Elevore +1–2, Idol of Maxarius +1…); the page itself notes this looks inconsistent with a cap of 3
- Status: open. Probably the cap clips the total, but unverified. Check in game.

## Item level of drops from a T15 map (creator vs derived rule)
- Doc: kb/items/loot-pickup-heuristics.md, kb/items/item-level.md
- Source A: YouTube transcript "Evaluating Loot and Item Tiers in PoE 2", tier 5, 0.5.x, ingested 2026-11-17 (auto-generated transcript) — items from a T15 map (level 79 monsters) "always" drop as ilvl 79; ilvl 82 needs a T16 map + irradiated tablet + corrupted/cleansed area with +1 map level
- Source B: [kb/items/item-level.md](https://poe2wiki.net/wiki/Level), tier 2 (derived from poe2wiki Level), 2026-11-17 — monster level = area level, +1 for magic/rare, +2 for bosses, +1 more in irradiated or Coalesced Corruption maps; T15 = area level 79, so rares in T15 drop at 80 and bosses at 81
- Status: open, leaning B (A is a simplification; the 82 route in A is consistent with B). Check in game.

## Is the quality exceptional-base bonus worth it? (value judgement, not a fact conflict)
- Doc: kb/items/loot-pickup-heuristics.md, kb/items/rarity.md
- Source A: [kb/items/rarity.md](https://www.poe2wiki.net/wiki/Exceptional_items), tier 2 — Exceptional bases come with >20% quality (max 30%) or an extra augment socket
- Source B: transcript above, tier 5 — quality-type exceptionals are "worthless right now"; only extra-socket ones matter
- Status: not a factual conflict; market opinion. Re-check with prices at 1.0.

## Mod tier numbering direction
- Doc: kb/items/affix-tiers.md
- Source A: [Mobalytics Crafting Basics pt 1](https://mobalytics.gg/poe-2/guides/crafting-basics-part-1), tier 3, 2026-11-17 — "the closer you are to Tier 1, the better"
- Source B: [poe2wiki Tier](https://poe2wiki.net/wiki/Tier), tier 2, 2026-11-17 — higher number = more powerful; reverse of PoE1. GGG forum threads 3665378 / 3679890 (tier 5) — players describe PoE2 tiers counting upward
- Status: resolved (2026-11-17) in favour of B. A reads as PoE1 wording carried over.

## Quality added per quality currency
- Doc: kb/items/quality.md
- Source A: [poe2db Armourer's Scrap](https://poedb.tw/pt/markdown_raw?oldid=1720) community-wiki text, tier 2 (copied PoE1 text) — normal +5%, magic +2%, rare/unique +1%
- Source B: [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality), tier 2 — amount depends on item level; higher ilvl = less. In-game help text (as shown on poe2db JP/KR pages) — more effective on low-ilvl, non-unique items
- Status: resolved (2026-11-17) in favour of B (game text). Exact amounts per ilvl still unknown — check in game.

## Vaal Orb socket outcome on caster weapons
- Doc: kb/items/corruption.md
- Source A: [poe2wiki Corrupt](https://www.poe2wiki.net/wiki/Corrupt), tier 2 — socket outcome applies to weapons including sceptres, and armour
- Source B: [poe2wiki Corrupted](https://poe2wiki.net/wiki/Corrupted), tier 2 — socket outcome for martial weapons and armour; caster weapons instead get ±10% quality (to 23%)
- Status: open. Likely two page versions from different patches. Check the Corrupt page version history.

## Essence of Ice effect
- Doc: kb/crafting/essences.md
- Source A: [Mobalytics Lolcohol essence guide](https://mobalytics.gg/poe-2/profile/lolcohol/guides/essence-guide-poe-2), tier 3 — function table lists Ice as "Critical Hit Chance for Spells"
- Source B: [Mobalytics Paintmaster essence farm](https://mobalytics.gg/poe-2/guides/paintmasters-essence-farm), tier 3; [Poe-Vault](https://www.poe-vault.com/poe2/guides/currency-and-crafting), tier 3 — Ice adds a cold modifier (flat cold on martial weapons)
- Status: open, leaning B (two sources; A may be a table parsing/row error seen only via search snippet). Check poe2wiki Essence of Ice page.

## Do alternate gem quality types exist?
- Doc: kb/gems/quality.md, kb/crafting/currency-index.md
- Source A: kb/gems/quality.md (batch 5) — no alternate qualities found in sources checked ([INFERRED] absent)
- Source B: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2), tier 2 (game data 0.5.5.9) — Prime/Secondary Regrading Lens: "change the type of quality of a skill/support gem with quality to another random quality"
- Status: open. Lens items imply quality types exist at least in data; may be unreleased. Check in game / poe2db gem quality pages.

## Who runs the Currency Exchange and when it unlocks
- Doc: kb/economy/currency-exchange.md
- Source A: [poe2wiki Currency exchange market](https://www.poe2wiki.net/wiki/Currency_exchange), tier 2 — since 0.3 Ange runs it, unlocked in Act 4 (marked undocumented change)
- Source B: [Mobalytics Currency Exchange](https://mobalytics.gg/poe-2/guides/currency-exchange), tier 3 — Finn (Act 1), Risu (Act 2), Alva (Act 3, endgame and hideout); Maxroll says unlocked by completing the campaign
- Source C: Timesaver gold guide, tier 5 — via Faustus from Act 6
- Status: open, leaning A for 0.5 (newest version-history entry). Check in game; re-check for 1.0 campaign.

## Currency Exchange gold fee scaling
- Doc: kb/economy/currency-exchange.md
- Source A: [Maxroll Trade in PoE2](https://maxroll.gg/poe2/guides/trade-in-path-of-exile-2), tier 3 — fee scales with the number of items traded
- Source B: [poewiki Currency Exchange Market](https://www.poewiki.net/wiki/Currency_Exchange_Market), tier 2 (PoE1 implementation) — fixed gold cost per item, by item rarity, scaling linearly with the ratio
- Source C: [Sportskeeda exchange guide](https://sportskeeda.com/mmo/path-exile-2-poe2-currency-exchange-guide), tier 5 — fee based on quantity wanted; quantity expended has no bearing
- Status: open. poe2wiki's per-item gold cost table (Scroll of Wisdom 1, Gemcutter's Prism 1,000) fits "per-item cost × quantity". Check in game by placing two orders of different sizes.

## Act 2 relic altar (Valley of the Titans) options
- Doc: kb/campaign/act-2.md
- Source A: [PoE2DB Act 2](https://poe2db.tw/us/Act_2), tier 2 — choose (changeable): 30% increased charm charges gained, or 15% increased mana recovery from flasks
- Source B: [Mobalytics 0.5 campaign checklist](https://mobalytics.gg/poe-2/guides/0-5-campaign-checklist-stats-rewards-skillpoints-and-more), tier 3 (2026-06-02) — +1 charm slot with a choice of 30% charm charges gained or charm effect duration
- Source C: [PoE2DB Quest](https://poe2db.tw/us/Quest) quest-reward table, tier 2, 2026-11-23 — either 30% increased charm charges + a charm slot, or 30% increased charm effect duration + a charm slot
- Status: open, now leaning B (C, from the same site as A, agrees with B; A is likely an older page version). Check in game; re-check for 1.0.

## Act 4 weapon-set point sources
- Doc: kb/campaign/act-4.md
- Source A: [PoE2DB Act 4](https://poe2db.tw/us/Act_4), tier 2 — points from Yama the White (Halls of the Dead) and Navali (Trial of the Ancestors)
- Source B: [Mobalytics 0.5 campaign checklist](https://mobalytics.gg/poe-2/guides/0-5-campaign-checklist-stats-rewards-skillpoints-and-more), tier 3 — points from Omniphobia (Journey's End) and Yama the White
- Source C: [poe2wiki Quest reward](https://www.poe2wiki.net/wiki/Quest_reward), tier 2 — Isle of Kin: The Blind Beast +2; [Mobalytics Act 4 buffs](https://mobalytics.gg/poe-2/guides/act-4-buffs) says Blind Beast reward changed in 0.4
- Source D: [PoE2DB Quest](https://poe2db.tw/us/Quest) quest-reward table, tier 2, 2026-11-23 — Omniphobia +2 and Trail of the Ancestors +2; The Blind Beast gives a Blank Greater Rune (not points)
- Status: open, leaning Omniphobia + Ancestors (D) — PoE2DB's two pages disagree with each other; D agrees with B on Omniphobia and with A on the Ancestors trial. All agree on 4 points total in 0.5. Moot if 1.0 reworks Act 4 — check then.

## Boots 30% movement speed tier name
- Doc: kb/builds/levelling-gear.md
- Source A: game data mods.json (RePoE 0.5.5.9), tier 2 — MovementVelocity5 = "Cheetah's", 30%, level 65
- Source B: [Grindout leveling guide](https://grindout.com/poe-2/guides/leveling), tier 5 — "Sokaris's", 30%, level 65
- Status: open (cosmetic — value and level agree). Check an item in game or on PoE2DB.

## Conquerors campaign points of interest count (1.0)
- Doc: kb/strategy/official-1.0-reveal.md
- Source A: [PoE2 Full release page](https://pathofexile2.com/fullrelease), tier 1, 2026-11-23 — "over 70 new points of interest" across the campaign, plus 20+ campaign missions
- Source B: [Maxroll Everything New In PoE2 1.0](https://maxroll.gg/poe2/news/everything-new-in-path-of-exile-2-1-0), tier 3, seen only as a search snippet 2026-11-23 (Maxroll refuses fetches) — the league "adds 17 new points of interest"
- Status: open, leaning A (tier 1). B may count something narrower (e.g. one act or one POI type) or be a typo. Check the patch notes.

## Is Master-at-Arms available on day one?
- Doc: kb/classes/index.md, poe2-1.0-launch-brief.md
- Source A: poe2-1.0-launch-brief.md (project doc, from Steam vs press text) — Master-at-Arms possibly not day one
- Source B: [PoE2 Full release page](https://pathofexile2.com/fullrelease), tier 1, 2026-11-23 — "In 1.0, we are introducing two Ascendancy Classes for Duelist", then presents Master-at-Arms
- Status: resolved (2026-11-23) in favour of B (tier 1). Knight isn't named on that page but is named elsewhere ([[classes/index]]).
