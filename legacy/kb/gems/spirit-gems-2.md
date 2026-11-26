# Spirit gems — numbers at gem level 1 / 10 / 20

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
