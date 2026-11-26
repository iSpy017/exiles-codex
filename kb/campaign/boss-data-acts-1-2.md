---
title: Campaign Boss Data — Acts 1–2 (0.5.x)
status: partial
tracker_topic: "Campaign boss data, Acts 1–4 (res, hit sizes, unavoidable skills, adds)"
tracker_note: "partial (45 bosses from PoE2DB stat blocks, 0.5.x; choreography not captured; 90% res reading [INFERRED]; rebuild at 1.0)"
defaults: conf=single-source
data: [data/poe2db/Count_Geonor.tsv]  # generated from the crawl; query these instead of reading the tables
---

Status: partial — game-data stat blocks only; fight choreography (what to do) not captured. Re-check at 1.0 (campaign rework; bosses may be retuned).
Source for every row: the boss's PoE2DB page (PoE2DB [S009] → page named after the boss, e.g. poe2db:Count_Geonor), tier 2, local crawl 2026-11-23 ([[notes/tools/poe2db-corpus]]), parsed with a script on 2026-11-25. Confidence: single-source (game data) for every number.

## How to read this
- **Life % / Dmg %** — the monster type's life and damage multipliers shown on PoE2DB. Real boss life also needs the level base and the Unique rarity multiplier → [[mechanics/monster-life]].
- **Res** — Fire / Cold / Lightning / Chaos, as PoE2DB lists them (column order per [[mechanics/monster-life]]). Several bosses show 90%; monster default max res is 75% per PoE2DB "Monster Default", so [INFERRED] 90% acts as 75% unless the boss also has raised max res. Treat as "heavily resists" either way.
- **Biggest hits** — the skills with the largest "X% more Attack damage" on the skill itself, with any built-in phys→element conversion. These are skill base values; the page notes they exclude the monster's damage %, rarity bonuses and map mods.
- **Unavoidable** — skills carrying the stat "base skill cannot be avoided by dodge roll or evaded or blocked". Only positioning (leave the area) or raw mitigation/life deals with these. Skills marked only "cannot be blocked" are not counted here.
- Skill names are PoE2DB internal ids (in-game names mostly aren't on the page). Descriptive words in ids (Slam, Charge, Summon…) are a guide, not a promise — [INFERRED].
- Spell-heavy bosses show flat spell damage, not "% more", so "biggest hits" can be empty for them.

## Act 1 (area levels 1–15)
| Boss (area) | Life / Dmg | Res F/C/L/X | Damage beyond phys | Biggest hits | Unavoidable | Adds |
|---|---|---|---|---|---|---|
| The Bloated Miller (Riverbank) | 105% / 190% | 0/0/0/0 | none | `SwollenMillerSlam` 150% more (cd 9 s) | 0 (charges can't be blocked) | zombie hordes |
| Beira of the Rotten Pack (Clearfell) | 98% / 133% | −15/90/0/0 | cold spells (ice spear, nova, frost waves) | — (spells) | 0 | wolves |
| The Devourer (Mud Burrow) | 115% / 220% | 0/0/0/0 | chaos (50% conversion on acid tail slams) | `GAMudBurrowerHeadSlam` 300% more (cd 12 s); burrow emerge 200% more | 1 (`DivePush`) | maggots/grubs |
| The Rust King (Red Vale) | 138% / 375% | 45/0/−15/0 | lightning beam + nova | `RustKingHurricaneProjectile` 130% more, pierces (cd 15 s) | 5 (hurricane burst, combo slam stages) | skeletons |
| Lachlann of Endless Lament (Cemetery) | 168% / 300% | 0/0/0/0 | cold (40% conv. storms) | `BitterGuyBrutusSlam` **275% more, unavoidable** (cd 20 s); slams 190% more (cd 7 s) | 1 | wife + swarm |
| Draven, the Eternal Praetor (Mausoleum) | 163% / 313% | 45/0/0/0 | fire (Blazing Lance 60% conv.) | empowered cleave 110% more (cd 9 s) | 1 (lance burn) | — |
| Asinia, the Praetor's Consort (Tomb) | 175% / 300% | 0/45/0/0 | fire (mortars 60% conv.) | large delayed blast 149–224 phys (spell) | 1 (bone storm) | yes |
| The Crowbell (Hunting Grounds) | 163% / 375% | 0/0/0/0 | none | leap slam 200% more; enraged leap 135% more (cd 5 s) | 2 (double slam) | — |
| The King in the Mists (Freythorn) | 175% / 156% | 0/0/0/35 | chaos | `GAVoodooKingVineSlam` **200% more, 30% chaos, unavoidable** (cd 15 s) | 4 (incl. bug bomb) | effigies |
| The Executioner (Ogham Village) | 188% / 400% | 45/0/0/0 | fire (mega slam 75% conv.) | mega slam 350% more (cd 12 s); guillotine drop **350% more, unavoidable** | 6 | taunt summon |
| Candlemass, the Living Rite (Ogham Manor) | 140% / 260% | 45/45/0/0 | fire (40–80% conv.) | lacerate 280% more, 80% fire | 0 | — |
| Count Geonor (Ogham Manor) | 237% / 280% | 0/45/0/0 | cold (30–75% conv.) | lacerate slam finisher 300% more, 60% cold; backwards charge cleave 270% more; thrust projectile **160% more, 75% cold, pierces, 500% more freeze buildup, unavoidable** | 2 (thrust + its projectile) | werewolves |

Notes:
- Geonor's thrust projectile is the act's main freeze threat (500% more freeze buildup) — relevant to [[mechanics/chill-freeze]] and cold res before the fight. Its 45% cold res is already used in [[builds/kb-test-frostbolt-chronomancer-damage-0.5.5]].
- PoE2DB also lists "Geonor, the Putrid Wolf" (305% life) with area "The Iron Citadel" — [INFERRED] the corrupted endgame/boss-rush version, not the Act 1 fight.

## Act 2 (area levels 16–31)
| Boss (area) | Life / Dmg | Res F/C/L/X | Damage beyond phys | Biggest hits | Unavoidable | Adds |
|---|---|---|---|---|---|---|
| Rathbreaker (Vastiri Outskirts) | 203% / 281% | −15/45/0/0 | none | `GARathbreakerSlam` **235% more, unavoidable**; enrage slam **150% more, unavoidable** (cd 5 s) | 2 | pack spawn |
| Rudja, the Dread Engineer (Mawdun Mine) | 225% / 275% | 90/−30/0/0 | fire | — | 1 (suicide explosion, 50% fire) | — |
| Balbala, the Traitor (Traitor's Passage) | 188% / 250% | 45/−15/0/0 | fire (Firestorm) | hide-and-seek slam **250% more, 40% fire, unavoidable**; whirl 180% more (cd 13.5 s) | 2 (slam, rune explode) | clones, daggers |
| Jamanra, the Risen King (Halani Gates) | 333% / 375% | 45/−15/45/0 | lightning (70% conv.) | sword slam **150% more, 70% lightning, unavoidable** (cd 32 s) | 1 | — |
| Kabala, Constrictor Queen (Keth) | 266% / 240% | 0/90/0/0 | none listed | — (casts Vulnerability) | 1 (tail swipe detonation) | — |
| Zalmarath, the Colossus (Titan Grotto) | 300% / 313% | 90/−30/0/0 | fire + lightning | stab 125% more; arm slams 113–120% more (cd 8 s) | 3 (slap, hammer slam, flame walk) | wisps |
| Azarian, the Forsaken Son (Buried Shrines) | 250% / 300% | 90/0/0/0 | fire | double slam 125% more | 1 (cyclone, 75% fire, cd 8 s) | — |
| Ekbab, Ancient Steed (Bone Pits) | 200% / 270% | 0/0/0/0 | none | — | 1 (charge) | — |
| Tor Gul, the Defiler (Spires of Deshar) | 300% / 350% | 90/0/0/0 | fire (50% conv.) | head slam **150% more, unavoidable** (cd 12 s); sweeps **100% more, unavoidable** | 7 (sweeps, head slam body) | — |
| Jamanra, the Abomination (Dreadnought) | 600% / 200% | 45/−15/45/0 | lightning | glass sword slam **350% more, 35% lightning, unavoidable** (cd 18 s); axe cleave **300% more, 25% lightning, unavoidable** (cd 26 s) | 3 (+ beacon lightning bolt) | — |

## Patterns worth knowing (Acts 1–2)
- [INFERRED] from the tables: most story and act-ending bosses (Lachlann, Executioner, Geonor, both Jamanras, Tor Gul, Rathbreaker, Balbala) have at least one unavoidable hit of 150–350% more. Dodge roll won't save you from those; leave the area or out-mitigate them. Reason: counted directly from the "cannot be avoided" stat above.
- Fire res is the common boss resist in Act 2 (7 of 10 show 45–90% fire); cold is often negative there. [INFERRED] relevant for a fire levelling skill. Reason: column counts in the table.
