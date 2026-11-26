---
title: Trial of Chaos (Inscribed Ultimatum)
status: partial
tracker_topic: "Trial of Chaos"
tracker_note: "partial (0.5.x; reward tables, Fate key differences missing; recheck 1.0)"
defaults: v=0.5.x
---

Status: partial. Structure, lengths, modifier families, wagers, boss stats and keys done. Missing: reward table per room, exact boss mechanics, how Inscribed Ultimatums drop in endgame, scaling of rewards.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB pages The Trial of Chaos, Inscribed Ultimatum, The Trials of Chaos (quest), Chimeral Inscribed Ultimatum, Ruin, Fate keys.
Tags: may-change.

## Entry and quest
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Act 3 quest "The Trials of Chaos" gives the Chimeral Inscribed Ultimatum (area level 38, 4 trials). Bring it to the Temple of Chaos, take a fresh Ultimatum from the Trialmaster each attempt, place it in the Temple Offering, complete the challenges. Quest completion grants 2 Ascendancy Points.
- src: poe2db:The_Trials_of_Chaos; poe2db:Chimeral_Inscribed_Ultimatum, tier 2, crawl 2026-11-23
- notes: Ascendancy use: [[classes/ascendancy-trials]].


## Inscribed Ultimatum item and trial length
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
The endgame key is the Inscribed Ultimatum (drop level 39, not for sale). Trial length by item level: level 1 gives 4 trials, level 60 gives 7, level 75 gives 10. The page gives no explicit room or boss count per run. Seven encounter types: kill-all, survive, implant Soul Cores, escort a statue, sacrifice monsters, destroy idols, boss.
- src: poe2db:Inscribed_Ultimatum, tier 2, crawl 2026-11-23
- vol: may-change `atlas-dependent` (how keys and higher item levels are obtained is not in the corpus)
- conf: confirmed (same table on [PoE2DB The Trial of Chaos](https://poe2db.tw/us/The_Trial_of_Chaos))
- notes: Room and boss counts per run: not found in the corpus pages read.


## Round loop: modifiers, wagers, rewards
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Each room you choose a modifier (a handicap on the run, tiers 1-5; a few exist only at tiers 1/3/5) and a reward. Wager-style modifiers are the high-risk picks. Reward currency list on the page (21 entries) includes Artificer's Orb x20, Chaos Orb x10, Exalted Orb x20, Divine Orb x2 and x5, Orb of Annulment x3, plus Soul Cores. Wager of Danger offers boss-room modifiers at max tier and an extra reward. Wager of Chaos has two versions: one upgrades 2 chosen modifiers and adds 1 extra reward per room; the other upgrades all chosen modifiers and adds 2 extra rewards per room (raw lines 1192-1200).
- src: poe2db:The_Trial_of_Chaos, tier 2, crawl 2026-11-23
- notes: Full wager list: link above. Wager of Ruin makes an invulnerable Shade stalk you, sets Ruin to 5, and makes unique trial bosses drop a Rare Unique. Reaching 7 Ruin fails the run ([PoE2DB Ruin](https://poe2db.tw/us/Ruin)).


## Modifier families (decision rows)
| Modifier | Values by tier (1 to 5) | Practical effect |
|---|---|---|
| Reduced Recovery | 20/35/50/65/80% reduced life, mana, ES recovery | Hurts regen builds |
| Lessened Reach | 20/35/50/65/80% less AoE and projectile speed | Hurts clear/AoE |
| Damaged Defences | 20/35/50/65/80% less armour, evasion, ES | Hurts all defences |
| Reduced Resistances | -15/-25/-35/-45/-55% ele res; max res -5/-10/-15 from III | Check res cap |
| Drought | 20/40/60/80% less charges, V none | Flask/charm builds |
| Deadly Monsters | 100/200/300/400/500% inc crit chance | Crit damage risk |
| Chaotic Monsters | 5/11/17/23/29% extra as Chaos | Needs chaos res |
| Resistant Monsters | +10/20/30/40/50% all res | Slows kills |
| Enraged Bosses | tiers 1/3/5: +30/60/100% toughness, +10/20/30% damage | Boss time |
| Escalating Damage Taken | tiers 1/3/5: +1% per 2.5/1.75/1 s, up to 50% | Fast rooms matter |
Others (traps, turrets, Stalking Shade, Petrification Statues, Heart Tethers, Random Projectiles, Occasional Impotence, Blood Mist) are listed on the PoE2DB page; not copied. Source for all rows: [PoE2DB The Trial of Chaos](https://poe2db.tw/us/The_Trial_of_Chaos), tier 2, crawl 2026-11-23.

## Trial bosses and Trialmaster
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Campaign version (area level 38) bosses: Uxmal, the Beastlord (89,700 life), Chetza, the Feathered Plague (77,865), Bahlak, the Sky Seer (77,865), and The Trialmaster (233,595 life, 546 armour, resistances 75/75/75 per PoE2DB). The final chamber drops keys to a door; the page only says some claim the Trialmaster resides there, which is a rumour, not confirmed.
- src: poe2db:The_Trial_of_Chaos, tier 2, crawl 2026-11-23
- notes: Pinnacle fight detail belongs to batch 43. Unique drops listed on the page: Glimpse of Chaos, Hateforge, Mahuxotl's Machination, The Adorned, Zerphi's Genesis; mods in [[items/uniques-drop-sources]].


## Fate keys and Reliquary key
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Cowardly Fate, Deadly Fate and Victorious Fate are keys used at the final door of the Trial to fight the Trialmaster. The Trialmaster's Reliquary Key opens a portal at The Reliquary Vault (map level 65), single use.
- src: poe2db:Cowardly_Fate; poe2db:The_Trialmasters_Reliquary_Key «PoE2DB The Trialmaster's Reliquary Key», tier 2, crawl 2026-11-23
- notes: Difference between the three Fates: not found in corpus. Prices omitted (volatile).


## Soul Cores
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The Trial can offer Soul Cores (about 20 types, such as Tacati for poison magnitude and chaos res, Azcapa for Spirit). Per-slot values on [PoE2DB The Trial of Chaos](https://poe2db.tw/us/The_Trial_of_Chaos).
- src: poe2db:The_Trial_of_Chaos, tier 2, crawl 2026-11-23
- notes: Soul core library: [[items/soul-core-idol-effects]].
