---
title: Spirit gems (Persistent/Buff) — index and table
status: done
tracker_topic: "Spirit gems (non-minion persistents) — list + per-level"
tracker_note: "done (0.5.x; 42 gems; Grim Feast 30 spirit [INFERRED])"
defaults: v=0.5.x
merged_from: [spirit-gems.md, spirit-gems-2.md]
data: [data/poe2db/Spirit_Gems.tsv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for non-minion persistents in the 0.5.x corpus. Per-level numbers in [[gems/spirit-gems]]. Grim Feast spirit cost not stated (see gaps).
Version: 0.5.x only (not checked against 1.0).
Source summary: PoE2DB gem pages and Spirit Gems list, crawl 2026-11-23, tier 2.

## Table (spirit = reservation shown on gem page; weapon req = "Requires" line)
| Gem | Tier | Spirit | Weapon req | One-line effect |
|---|---|---|---|---|
| Grim Feast | 4 | not shown | none | Reviving minions drop remnants; consume to revive minions |
| Withering Presence | 4 | 30 | none | Aura; periodically Withers enemies in Presence |
| Convalescence | 4 | 30 | none | Usable skill: instant ES recharge + uninterruptible buff |
| Blasphemy | 8 | 60 per curse | none | Meta: socketed curses become auras |
| Barrier Invocation | 8 | 30 | none | Meta: energy from ES damage triggers spells |
| Cast on Critical | 14 | 100 | none | Meta: energy on crits triggers spells |
| Plague Bearer | 4 | 30 | none | Stores poison damage, releases as nova |
| Wind Dancer | 4 | 30 | Martial weapon | Evasion stages; hit consumes them for knockback blast |
| Herald of Plague | 8 | 30 | Martial weapon | Kill poisoned enemy: spread poison, may Hinder |
| Combat Frenzy | 8 | 30 | none | Frenzy charge on Freeze/Electrocute/Pin (rate-limited) |
| Mirage Archer | 8 | 60 | Bow/Spear/Crossbow | Dodge roll makes a mirage using socketed ranged attacks |
| Alchemist's Boon | 14 | 30 | none | Passive flask charges; flask recovery shared with allies |
| Iron Ward | 4 | 30 | none | Stores mitigated physical damage, releases as spike nova |
| Magma Barrier | 4 | 30 | Shield | Block chance; lava-imbued shield triggers Magma Spray |
| Scavenged Plating | 4 | 30 | none | Armour-break kills give stacks: armour + thorns |
| Herald of Ash | 4 | 30 | Martial weapon | Overkill explosion ignites nearby enemies |
| Time of Need | 8 | 30 | none | Periodic heal + clears curses/ailments |
| Overwhelming Presence | 8 | 30 | none | Aura: lower enemy stun and ailment thresholds |
| Berserk | 14 | 30 | none | More rage effect; lose life while not losing rage |
| Dread Banner | 14 | 30 | none | Glory banner: max ele res, ailment threshold, flask charges |
| Mana Remnants | 4 | 30 | none | Ailment kills/crits spawn mana remnants |
| Blink | 8 | 60 | none | Replaces dodge roll with teleport spell |
| Siphon Elements | 8 | 30 | none | Freeze/shock/ignite may spawn infusion remnants |
| Elemental Invocation | 8 | 60 | none | Meta: energy from ailments triggers spells |
| Archmage | 14 | 100 | none | Spells: extra lightning from max mana, extra mana cost |
| Cast on Elemental Ailment | 14 | 100 | none | Meta: energy from ailments triggers spells |
| Elemental Conflux | 14 | 60 | none | More damage with a randomly rotating element |
| Herald of Blood | 4 | 30 | Martial weapon | Blood-loss kills explode (physical) |
| Trail of Caltrops | 8 | 30 | none | Dodge scatters 3 maiming caltrops |
| Trinity | 14 | 100 | none | Affinity stacks: more elemental damage |
| War Banner | 4 | 30 | none | Glory banner: attack damage/speed/accuracy |
| Attrition | 4 | 30 | none | More hit damage vs rares/uniques over time; culling |
| Defiance Banner | 8 | 30 | none | Glory banner: armour/evasion/move speed |
| Shard Scavenger | 8 | 30 | Crossbow | Consuming freeze/shock/ignite/broken armour reloads |
| Charge Regulation | 14 | 30 | none | Charge-based buffs, consumes charges periodically |
| Ghost Dance | 4 | 30 | none | Ghost shrouds: hit grants ES based on evasion |
| Lingering Illusion | 8 | 30 | none | Dodge makes decoy; destroyed decoy drops power-charge remnant |
| Cast on Dodge | 14 | 100 | none | Meta: dodge-roll energy triggers spells |
| Reaper's Invocation | 14 | 30 | none | Meta: melee kills give energy |
| Briarpatch | 4 | 30 | none | Stores phys attack damage; spell cast makes thorny ground |
| Savage Fury | 4 | 30 | none | Spend fury: beast frenzy, onslaught, life loss |
| Barkskin | 8 | 30 | none | ES lost on hit becomes armour |
| Eternal Rage | 14 | 100 | none | Constant rage regeneration |
| Feral Invocation | 14 | 60 | Talismans | Meta: mana spent gives energy for shapeshift attacks |

## Cross-references (not repeated)
- Arctic Armour, Herald of Ice: [[gems/cold-spell-gems]]. Herald of Thunder: [[gems/bow-attack-gems]].
- Minion-tagged persistents (Ravenous Swarm, Raging Spirits, Rhoa Mount, Wolf Pack, Sacrifice, Cast on Minion Death): [[gems/minion-skills]] (assumed covered per task brief; Sacrifice and Cast on Minion Death not re-read for stats beyond a check).

## Uncut spirit gem pool
@ v=0.5.x vol=stable conf=single-source date=2026-11-23
Uncut Spirit Gems exist at levels 4–20; the level-4 one creates a gem at level 4, levels 5–20 create a gem or level an existing gem to that level.
- src: poe2db:Uncut_Spirit_Gems, tier 2, crawl 2026-11-23
- notes: Tier 4/8/14 groups come from [PoE2DB Spirit Gems](https://poe2db.tw/us/Spirit_Gems). Page groups gems under labels Occult, Bow, Mace, Elemental, Spear, Crossbow, Quarterstaff, Primal; label meaning is not explained on the page. [INFERRED] tier = lowest uncut gem level that can roll that gem (page does not say so; groups match 4/8/14 only).


## Gem level to character level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
gem level 1/2/3/4/5/6/7/8/9/10 needs char level 0/3/6/10/14/18/22/26/31/36; 11–20 needs 41/46/52/58/64/66/72/78/84/90. Single-gem pages agree (L10=36, L20=90).

- src: poe2db:Spirit_Gems, tier 2, crawl 2026-11-23
- conf: confirmed (same table on every gem page)

## Weapon-set rule
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
only four pages carry "must be active in both Weapon Sets": Blink, Convalescence, Eternal Rage, Sacrifice. No enemy-level cap appears on any gem page read.
- src: PoE2DB gem pages (Blink, Convalescence, Eternal_Rage, Sacrifice), tier 2, crawl 2026-11-23
- notes: per-weapon-set spirit: [[mechanics/spirit-reservation]]. Others (e.g. Archmage) show no such line.


<!-- merged from kb/gems/spirit-gems-2.md -->
Part title: Spirit gems — numbers at gem level 1 / 10 / 20

Status: done for the gems in [[gems/spirit-gems]] (minion persistents and Arctic Armour/Herald of Ice/Herald of Thunder excluded). Values are the level-table column PoE2DB shows for each gem's headline stat.
Version: 0.5.x. Source for every row: the gem's own PoE2DB page (e.g. [Archmage](https://poe2db.tw/us/Archmage)), tier 2, crawl 2026-11-23. Confidence: single-source each.
Volatility: may-change. Spirit cost is flat across gem levels on all pages read (no level scaling seen); table's "Mana" column on Grim Feast is a label quirk (see notes).

## Defensive / utility
| Gem | L1 | L10 | L20 |
|---|---|---|---|
| Time of Need | heal 17, every 10 s | 166, 9.1 s | 628, 8.1 s (also clears curses, ele ailments) |
| Barkskin | armour = 43% of ES lost | 52% | 62% (6 s; capped by item armour on equipped armour) |
| Ghost Dance | shroud every 12 s | 11.1 s | 10.1 s (max 3; hit gives ES regen 2% of evasion/s) |
| Iron Ward | stores 100% mitigated phys, cap 65 | 280%, cap 1980 | 480%, cap 22886 (nova 6 m, 200% more stun buildup) |
| Magma Barrier | +25% block; spray 4–6 off-hand fire | 40–60 | 103–155 (fully imbued in 8 s) |
| Scavenged Plating | thorns 2–2 per stack | 17–25 | 43–64 (4% more armour/stack, max 10, 8 s) |
| Convalescence | buff 3 s | 3.45 s | 3.95 s (30 s cooldown, 20 mana) |
| Blink | teleport 4 m | 4.4 m | 4.9 m (cooldown 4.5 to 3.5 s across levels) |
| Alchemist's Boon | 0.17 charges/s; 15% shared | 0.2; 24% | 0.23; 34% |
| Charge Regulation | speed 20 / crit 20 / def 15 | 23 / 23 / 17 | 25 / 26 / 20 (consumes one of each charge per 10 s) |
| Mana Remnants | 28 mana per remnant | 120 | 281 (25% on ailment kill; crit remnant max once/2 s; 8 s) |

## Offensive / damage
| Gem | L1 | L10 | L20 |
|---|---|---|---|
| Archmage | +8% max mana added cost | 7.1% | 6.1% (4% extra lightning per 100 max mana, fixed) |
| Elemental Conflux | 40% more dmg, random element | 49% | 59% (re-roll every 8 s) |
| Berserk | 40% inc rage effect | 49% | 59% (loses 0.1% max life per rage/s) |
| Attrition | max 40% more vs rare/unique; culling at 40 s | 49%; 36 s | 59%; 31 s |
| Trinity | 1% more ele dmg per 30 affinity; +5 affinity/hit | 3%; +9 | 6%; +13 (lose 3 of other types) |
| Eternal Rage | 0.25 rage/s | 2.5 | 5 |
| Savage Fury | 20% more dmg + onslaught | 24% | 29% (lose 3% max life/s; 0.5 s per fury) |
| Herald of Ash | ignite 16.67% of overkill | 19.67% | 23% (needs overkill ≥20% max life; radius 1.2 m; 3 s) |
| Herald of Blood | explosion 4–6 phys; 40% aggravate bleed | 41–62; 49% | 107–160; 59% (15% of blood loss; 1.5 m) |
| Herald of Plague | spread radius 1.5 m, 10% hinder | 1.6 m; 19% | 1.8 m; 29% |
| Plague Bearer | stores 4% poison, cap 43 | cap 1320 | cap 15257 (nova 1.8 m) |
| Wind Dancer | stage every 1.5 s; blast 20% | 1.32 s; 41% | 1.12 s; 82% (3 stages, 10% more evasion each) |
| Trail of Caltrops | 6–9 phys, 35% | 62–92, 72% | 159–238, 143% (3 per dodge, max 20) |
| Briarpatch | stores 1%, cap 9 | cap 64 | cap 256 (3 m patch, 6 s, 8 s between) |
| Withering Presence | wither every 1.8 s | 1.62 s | 1.42 s (wither lasts 6 s) |
| Combat Frenzy | frenzy charge every 8 s max | 7.1 s | 6.1 s |
| Shard Scavenger | min 7 s between | 6.55 s | 6.05 s (buff 3 s) |
| Siphon Elements | 5% remnant chance (fixed); pickup range bonus blank | +18% pickup range | +38% |
| Mirage Archer | mirage 5.05 s | 5.5 s | 6 s (10 s cooldown, mirage 30% less damage) |
| Lingering Illusion | extra-remnant chance not shown | 36% | 76% (decoy 3 s; 10 mana) |
| Overwhelming Presence | stun threshold -15%, ailment -15% | -20%, -19% | -25%, -24% |

## Banners (200 glory to place, 6 m radius; duration 6 / 7.8 / 9.8 s at L1/10/20)
- War Banner: 25% more attack damage, 50% inc accuracy, 25% inc attack speed (values listed are fixed, not level-scaled).
- Defiance Banner: 30% more armour and evasion, 30% inc move speed.
- Dread Banner: +4% max ele res, 60% more ele ailment threshold, 0.5 flask charges/s.

## Meta gems (energy: increased-energy-gained % at L1 none / L10 / L20)
| Gem | L10 | L20 | Energy rule |
|---|---|---|---|
| Cast on Critical | 27% | 57% | 1 per Power on crit; spells deal 20% less damage |
| Cast on Elemental Ailment | 27% | 57% | freeze 10/Power, ignite 1, shock 1 |
| Cast on Dodge | 27% | 57% | 2 per metre dodged |
| Barrier Invocation | 27% | 57% | 1 per 10 ES lost; max 500 |
| Elemental Invocation | 32% | 68% | as CoEA; max 500 |
| Reaper's Invocation | 27% | 57% | 30 per Power on melee kill; max 500 |
| Feral Invocation | 27% | 57% | 1 per 20 mana spent; max 500 |
| Blasphemy | 46% (curses 50% less magnitude at L1) | 41% less at L20 | reserves 60 per curse |

## Grim Feast and quirks
- Grim Feast: remnant stores 35% of minion max life, lasts 8 s; stored cap 47 / 10643 / 66124 at L1/10/20; minion level 2 / 20 / 40. The page has no "Reservation" line; its table column labelled Mana reads 0 at L1 then 30 from L2 on, which matches the known label quirk ([[gems/minion-skills]]) but is [INFERRED] to mean 30 spirit (value equals the tier-4 norm; L1 zero unexplained).
- Sacrifice: not tabulated here (minion-tagged).
