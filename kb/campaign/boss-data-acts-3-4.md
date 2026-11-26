---
title: Campaign Boss Data — Acts 3–4 (0.5.x)
status: partial
tracker_topic: "Campaign boss data, Acts 1–4 (res, hit sizes, unavoidable skills, adds)"
tracker_note: "partial (45 bosses from PoE2DB stat blocks, 0.5.x; choreography not captured; 90% res reading [INFERRED]; rebuild at 1.0)"
defaults: conf=single-source
---

Status: partial — game-data stat blocks only; fight choreography not captured. Re-check at 1.0 (Act 4's role may change; Acts 5–6 added).
Source for every row: the boss's PoE2DB page (e.g. Doryani, Royal Thaumaturge [S234]), tier 2, local crawl 2026-11-23 ([[notes/tools/poe2db-corpus]]), parsed 2026-11-25. Confidence: single-source (game data) for every number.
How to read the columns (life/dmg %, res order, "unavoidable", internal ids, 90% res note): see [[campaign/boss-data-acts-1-2]].

## Act 3 (area levels 33–45)
| Boss (area) | Life / Dmg | Res F/C/L/X | Damage beyond phys | Biggest hits | Unavoidable | Adds |
|---|---|---|---|---|---|---|
| Rootdredge (Sandswept Marsh) | 240% / 200% | −15/90/0/0 | fire | — (caster) | 1 (detonate dead, cd 12.5 s) | — |
| Mighty Silverfist (Jungle Ruins) | 250% / 463% | 0/0/0/0 | none | rect slam **200% more, unavoidable** | 2 (slam, sunder) | — |
| Xyclucian, the Chimera (Chimeral Wetlands) | 288% / 250% | 15/15/15/0 | fire, cold, lightning, chaos | ground slam 150% more (cd 10 s); one skill has **300% more ignite magnitude** | 0 | — |
| Blackjaw, the Remnant (Machinarium) | 263% / 281% | 90/−15/0/0 | fire (50% conv. spins) | triple slam finisher 175% more; fire spins 120% more | 0 | — |
| Zicoatl, Warden of the Core (Jiquani's Sanctum) | 288% / 208% | 45/45/−15/0 | lightning | — (caster) | 0 | — |
| Ignagduk, the Bog Witch (Azak Bog) | 288% / 250% | 90/−15/0/0 | fire | — (caster) | 0 | bone spears |
| Mektul, the Forgemaster (Molten Vault) | 300% / 250% | 90/−15/0/0 | fire (50–70% conv.) | lava leap 250% more, 70% fire; fissure warcry spikes 200% more | 0 | — |
| The Queen of Filth (Apex of Filth) | 288% / 300% | 0/0/0/0 | chaos, fire | corpse ball splat **200% more, unavoidable**; roll slam **100% more, unavoidable** | 2 | inbreds |
| Ketzuli, High Priest of the Sun (Temple of Kopec) | 288% / 250% | 90/−30/0/0 | fire | — (caster: suns, sun wall, "neutron star") | 0 | 5 summon skills |
| Viper Napuatzi (Utzaal) | 288% / 250% | 15/15/15/0 | chaos, fire, lightning | snake wave 150% more | 0 | — |
| Doryani, Royal Thaumaturge (Black Chambers) | 330% / 300% | 45/0/45/0 | fire, lightning | — (spell damage) | 0 | — |

## Act 4 (area levels 46–53)
| Boss (area) | Life / Dmg | Res F/C/L/X | Damage beyond phys | Biggest hits | Unavoidable | Adds |
|---|---|---|---|---|---|---|
| The Blind Beast (Isle of Kin) | 300% / 250% | 0/0/90/0 | lightning | — | 0 | — |
| Krutog, Lord of Kin (Volcanic Warrens) | 350% / 250% | 0/0/45/0 | lightning | multi-slam final impact **100% more, unavoidable** | 2 | — |
| Captain Hartlin (Journey's End) | 288% / 283% | 0/90/0/0 | fire, cold | ghost anchor 200% more, 30% fire; cannon shots 100% more, 40–50% fire | 0 | — |
| Omniphobia, Fear Manifest (Journey's End, Dark Mists) | 150% / 300% | 0/0/0/0 | none | — | 1 (geometry leap slam) | — |
| Yama the White (Halls of the Dead) | 263% / 338% | 0/0/0/0 | chaos | — | 0 | — |
| Diamora, Song of Death (Singing Caverns) | 288% / 283% | 0/90/−15/0 | cold (80% conv. wave smashes) | — | 3 (double/triple wave smash, 80% cold) | — |
| The Prisoner (Solitary Confinement) | 350% / 288% | 0/90/0/0 | cold | mega spear ground slam **145% more, unavoidable**; spear slam 105% more (cd 15 s); fist slam 100% more (cd 7 s); one skill 100% more freeze buildup | 3 (+ ice crystal explode, death wave) | — |
| Scourge of the Skies (Shrike Island) | 132% / 121% | 0/0/0/0 | none | vomit sprays 150% more (cd 30 s); spike impale 150% more | 0 | dogs (4 summon skills) |
| Torvian, Hand of the Saviour (Arastas) | 288% / 250% | 0/0/0/0 | none | axe shockwaves 180% more (×3 stages) | 0 | — |
| Benedictus, First Herald of Utopia (Excavation) | 269% / 250% | 0/0/90/0 | lightning | — (spells: pillar crush, lightning barrage, donut slam) | **8** | boulders, raise-and-raze |
| Tavakai, the Chieftain (Heart of the Tribe) | 338% / 285% | 45/0/0/0 | none | spirit chieftain slam **175% more, unavoidable** (cd 21 s); jade sunder wave 125% more | 2 (+ hook toss, cd 25 s) | — |
| Great White One (Whakapanu Island) | 288% / 300% | 0/90/−15/0 | none | sandnado burst 275% more; landing 180% more | 0 | burrowed fins |

## Patterns worth knowing (Acts 3–4)
- [INFERRED] from the tables: Act 3 is the fire-resist act — 6 of 11 bosses show 45–90% fire res, and several have negative cold. A fire-only skill will feel weaker on Act 3 bosses; carry a second element or penetration/exposure ([[mechanics/exposure-penetration]]).
- [INFERRED] Act 4 shifts to cold and lightning res (Hartlin, Diamora, Prisoner, Great White 90% cold; Blind Beast, Benedictus 90% lightning).
- Benedictus has the most unavoidable skills of any campaign boss parsed (8) — expect to move, not dodge-roll. Reason: stat count above.
- Freeze threats: The Prisoner (100% more freeze buildup) and Count Geonor in Act 1 (500%) — check cold res and freeze mitigation ([[mechanics/chill-freeze]]).
