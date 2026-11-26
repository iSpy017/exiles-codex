# Spirit gems (Persistent/Buff) — index and table

Status: done for non-minion persistents in the 0.5.x corpus. Per-level numbers in [[gems/spirit-gems-2]]. Grim Feast spirit cost not stated (see gaps).
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
- Arctic Armour, Herald of Ice: [[gems/cold-spell-gems]]. Herald of Thunder: [[gems/bow-attack-gems-2]].
- Minion-tagged persistents (Ravenous Swarm, Raging Spirits, Rhoa Mount, Wolf Pack, Sacrifice, Cast on Minion Death): [[gems/minion-skills]] (assumed covered per task brief; Sacrifice and Cast on Minion Death not re-read for stats beyond a check).

## Uncut spirit gem pool
- Claim: Uncut Spirit Gems exist at levels 4–20; the level-4 one creates a gem at level 4, levels 5–20 create a gem or level an existing gem to that level.
- Version: 0.5.x | Volatility: stable | Confidence: single-source
- Source: [PoE2DB Uncut Spirit Gems](https://poe2db.tw/us/Uncut_Spirit_Gems), tier 2, crawl 2026-11-23
- Notes: Tier 4/8/14 groups come from [PoE2DB Spirit Gems](https://poe2db.tw/us/Spirit_Gems). Page groups gems under labels Occult, Bow, Mace, Elemental, Spear, Crossbow, Quarterstaff, Primal; label meaning is not explained on the page. [INFERRED] tier = lowest uncut gem level that can roll that gem (page does not say so; groups match 4/8/14 only).

## Gem level to character level
- Claim: gem level 1/2/3/4/5/6/7/8/9/10 needs char level 0/3/6/10/14/18/22/26/31/36; 11–20 needs 41/46/52/58/64/66/72/78/84/90. Single-gem pages agree (L10=36, L20=90).
- Version: 0.5.x | Volatility: may-change | Source: [PoE2DB Spirit Gems](https://poe2db.tw/us/Spirit_Gems), tier 2, crawl 2026-11-23 | Confidence: confirmed (same table on every gem page)

## Weapon-set rule
- Claim: only four pages carry "must be active in both Weapon Sets": Blink, Convalescence, Eternal Rage, Sacrifice. No enemy-level cap appears on any gem page read.
- Version: 0.5.x | Volatility: may-change | Source: PoE2DB gem pages (Blink, Convalescence, Eternal_Rage, Sacrifice), tier 2, crawl 2026-11-23 | Confidence: single-source
- Notes: per-weapon-set spirit: [[mechanics/spirit-reservation]]. Others (e.g. Archmage) show no such line.
