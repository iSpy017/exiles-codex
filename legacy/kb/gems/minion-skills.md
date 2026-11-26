# Minion Skill Gems (list, tiers, spirit by level)

Status: partial (0.5.x). Base minion life/damage per minion level not in the sources checked. Re-check at 1.0 (support rebalance; Infernalist and Blood Mage reworks may change minion gems).
Source for every row: the gem's PoE2DB page (e.g. [Skeletal Warrior](https://poe2db.tw/us/Skeletal_Warrior)), tier 2, local crawl 2026-11-23 ([[tools/poe2db-corpus]]), extracted 2026-11-26. Confidence: single-source (game data).

## Rules seen on every minion gem page
- Claim: Minion level = 2 × gem level on every minion gem extracted (gem 1 → 2, gem 10 → 20, gem 20 → 40). Matches [[mechanics/minions]].
- Claim: For persistent minion gems with a level-scaled reservation, **spirit cost falls as the gem levels** — e.g. Skeletal Brute 165 → 54 → 48 spirit at gem 1 / 10 / 20. The PoE2DB level table labels this column "Mana", but its values match the gem's "Reservation: (X — Y) Spirit" line → [INFERRED] it is the spirit reservation.
- Claim: Skeletal Warrior's first 2 minions have no base spirit reservation.
- Version: 0.5.x · Volatility: may-change
- Confidence: single-source; column reading [INFERRED] (strong — values match exactly)
- Notes: level the gem before adding more minion types — the same spirit buys more minions at higher gem level [INFERRED from the tables].

## Engravable minion gems (from uncut skill gems)
| Gem | Tier | Type | Spirit / cost (gem 1 → 10 → 20) | What it does (paraphrased) |
|---|---|---|---|---|
| Unearth | 1 | spell | mana 7 → 26 → 76 | bone spikes damage enemies (4–6 → 117–176 phys); corpses become Bone Constructs (limit 8 → 14 → 20) |
| Skeletal Arsonist | 3 | persistent | 90 → 42 → 39 spirit | reviving skeletons that can detonate other low-life minions (fire) |
| Raging Spirits | 4 | persistent buff | 30 spirit | your own skills also summon short-lived flaming skulls that rush enemies |
| Ravenous Swarm | 4 | persistent buff | 30 spirit | untargetable insect swarms pursue nearby enemies (duration 6 → 7.8 → 9.8 s) |
| Grim Feast | 4 | persistent buff | 0 → 30 → 30 | collects stored minion life (cap 47 → 10,643 → 66,124) |
| Skeletal Frost Mage | 5 | persistent | 120 → 43 → 39 spirit | cold skeleton casters |
| Raise Zombie | 5 | spell (temporary) | mana 10 → 35 → 102 | short-lived zombies from corpses; empowered zombies 100 → 155 → 253% more hit damage |
| Pain Offering | 5 | offering | mana 25 → 59 → 110 | skewer a Skeleton; aura gives minions 20→24→29% inc attack/cast speed and 20→38→58% inc damage |
| Bind Spectre | 7 | persistent | mana 22 → 53 → 99 to bind | captures a defeated monster's spirit; the gem becomes "Spectre: <monster>" (50 spirit on the Spectre page) |
| Tame Beast | 7 | companion | mana 22 → 53 → 99 | wisps engulf a beast to tame it as a companion |
| Wolf Pack | 8 | persistent companion | 60 spirit (gem page) | pack of 3 → 4 → 6 wolves |
| Cast on Minion Death | 8 | meta | — | triggers socketed spells when minions die |
| Skeletal Reaver | 9 | persistent | 90 → 33 → 30 spirit | physical skeletons that can enrage |
| Bone Offering | 11 | offering | mana 25 → 59 → 110 | shield your minions (15 → 20 → 25% reduced hit damage taken) |
| Skeletal Storm Mage | 11 | persistent | 120 → 42 → 39 spirit | lightning strike on dead skeletons |
| Skeletal Brute | 13 | persistent | 165 → 54 → 48 spirit | physical warcry/payoff brute |
| Skeletal Cleric | 13 | persistent | 60 → 22 → 20 spirit | heals minions, revives fallen skeletons |
| Soul Offering | 13 | offering | mana 32 → 76 → 141 | buff for you: 20 → 47 → 77% inc spell damage |
| Sacrifice | 14 | persistent | 60 spirit | lets skills use your undead reviving minions as corpses; minions revive 59 → 50 → 40% more slowly |
| Rhoa Mount | 14 | persistent companion | 100 spirit | mountable Rhoa companion (weapon condition on page) |
| Skeletal Warrior | — (tier not shown) | persistent | 60 → 22 → 20 spirit (first 2 free) | reviving melee skeletons |
| Skeletal Sniper | — (page missing header) | persistent | 90 → 33 → 30 spirit | skeleton archers |
| Dark Pact | — | spell | — | chaos nova from a minion (1–3 → 52–97 chaos at gem 20) |
| Abyssal Pact | — | spell | cost 0 | sacrifices 1 → 20% of a minion's max life as phys damage around it |
| Detonate Minion | — | attack (Dex) | cd 3 s | 300% attack damage; targets minions at or below 30 → 333 → 1,096 life |

## Minion skills from other sources (not uncut-gem drops)
- Unique items: Azmerian Wolf, Azmerian Swarms, Mist Raven (PoE2DB "Unique" source tag).
- Passive tree / ascendancy: Wild Protector (bear spirit), Kelari's Malediction (corpse beetles, max 4 → 6 → 8); the three Djinn — Kelari (sand), Navira (water), Ruzhan (flame) — are invulnerable persistent minions ([[classes/sorceress-ascendancies]], Disciple of Varashta).
- Class/other: Summon Companion (Mercenary companion that uses socketed ammunition), Manifest Weapon (copy of your main hand), Cackling Companions (6 → 7 → 9 hyenas), Demon Magus (100 spirit; casts socketed spells), Hydra Familiar (60 spirit meta), Spirit Vessel, Summon Infernal Hound, Supporting Fire, His Grave Command, Pounce (werewolf, limit 4 → 6 wolves).
- League/runeshape: Skyfall, Wardbound Minions, Eternal March, Verisium Manifestations (30 spirit) — 0.5 Runes of Aldur content → [[crafting/league-crafting]]; [INFERRED] may not exist in 1.0.
- Ignore: "[DNT]" / "[DNT-UNUSED]" entries (Dominating Aura, Lightless Stalker).
- Version 0.5.x · Confidence: single-source; "which source grants it" read from PoE2DB page tags.

## Gear that scales minions (example ladder)
- Sceptre suffix "Minions have X% increased maximum Life": of the Mentor (ilvl 2) 21–25% → Tutor (16) 26–30 → Director (32) 31–35 → Headmaster (48) 36–40 → Administrator (64) 41–45 → Rector (80) 46–50.
- Source: [PoE2DB Minions](https://poe2db.tw/us/Minions) mod table, tier 2, crawl 2026-11-23 · single-source.

## Still to source
- Minion base life and damage per minion level; per-skill minion count limits for skeletons; Spectre spirit by monster; Infernal Hound / Wolf Pack per-level reservation.
