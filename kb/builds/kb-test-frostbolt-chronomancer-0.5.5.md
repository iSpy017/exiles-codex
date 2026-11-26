---
title: KB-test build — Frostbolt Chronomancer → Sekhemas (0.5.5)
status: partial
tracker_topic: "KB-test build — Frostbolt Chronomancer (0.5.5)"
tracker_note: "partial (KB-only; damage confidence low/low–med/med/low; increased/more rule now sourced in mechanics/damage-calculation — doc text not yet updated; gaps: tree notables, mana check, ×29 boss-life reading, ascendancy pathing)"
defaults: v=0.5.5 vol=may-change
---

Status: partial · Version: 0.5.5 (Forbidden Rites rules) · Written 2026-11-23 from project docs only (KB test) · Volatility: may-change
Damage maths → [[builds/kb-test-frostbolt-chronomancer-damage-0.5.5]]. Trade softcore, day-1 start, zero trade until maps.

## a. Why this class / ascendancy / skill
@ v=0.5.5 vol=may-change conf=single-source date=2026-11-23 fill=v,vol missing=src
Sorceress (Int 15 start, [[classes/index]]) → ES as the main layer ([[builds/defence-checklist]] step 4). Chronomancer for Now and Again (repeatable spells 20% chance to Repeat) and Phased Form (30% less damage now, 30% of the hit 4 s later) ([[classes/sorceress-ascendancies]]). Frostbolt: tier 5, Repeatable, pierces all, 2.4 m explosion, 0.80 s cast, 12% crit ([[gems/cold-spell-gems]]).
- Spells ignore accuracy, so no 2–9 m distance penalty ([[mechanics/accuracy]]); damage comes from gem level, which floor drops raise ([[builds/levelling-gear]]).

| | Frostbolt Chronomancer (pick) | Frostbolt Stormweaver | Titan armour-break slam | Pathfinder poison bow |
|---|---|---|---|---|
| Clear | Pierce + explosion; slow projectile 2.8 m/s | Same | Melee range | Projectiles, distance penalty ([[mechanics/accuracy]]) |
| Single target | ×1.2 Repeat (Now and Again) | No damage node; chill/shock nodes | Fully Broken +20% phys taken, Sundered +20% more ([[mechanics/armour]]) | Poison stack limit 1 ([[mechanics/poison]]) |
| Defence | ES + Phased Form | ES + Force of Will (20% from mana) | Armour, but 5% MS penalty ([[mechanics/armour]]) | Evasion; fails vs red-flash ([[mechanics/evasion]]) |
| Cost | Self-found staff/wand +levels | Same | Weapon recraft at 11/16/28/33 ([[builds/levelling-gear]]) | Same |
| Levelling speed | Weak Act 1 boss (45% cold res) | Same | Fubgun: Titan falls off after 20–30 h ([[builds/starter-archetypes]]) | Bow loop well documented |
| Farm fit (Sekhemas) | ES counts toward Honour ([[endgame/sekhemas]]); ranged avoids hits [INFERRED] | Same | Melee eats hits → Honour loss [INFERRED] | Ranged, but evasion only vs attacks |
- Stormweaver lost only on node text: Constant Gale (permanent Arcane Surge) would fix mana — its one real edge.

- conf: single-source per fact; the overall pick is [INFERRED].

## b. Gem timeline (0.5.x quest rewards — [[campaign/quest-rewards]])
| Char lvl | Gem | Source |
|---|---|---|
| 1 | Ice Nova (tier 1) | Reaching Clearfell, uncut skill L1 |
| ~4 | Unleash (support T1) | Treacherous Ground uncut support (ilvl 4) |
| ~11 | Arctic Armour (T4, 30 spirit) | King in the Mists: uncut spirit L4 + 30 spirit ([[campaign/act-1]]) |
| ~14 | **Frostbolt** (T5) | Trail of Corruption uncut skill L5 (ilvl 15), or any L5 uncut from area 15 ([[gems/uncut-gems]]) |
| ~16–20 | Considered Casting (T2) | Act 2 uncut supports (ilvl 20–21) |
| ~22 | Elemental Weakness (T7) | Act 2 Trail of Corruption uncut skill L7 (ilvl 23) |
| ~33 | Deliberation (T3), Inexorable Critical I | uncut support L3 from ilvl 33 |
| ~45 | Rapid Casting II, Cold Exposure (T4) | uncut support L4 from ilvl 45 |
| ~55 | Cold Mastery (T5) | uncut support L5 from ilvl 55 (Interludes) |
- Use Act 3/4 uncut skill L11–13 rewards to level Frostbolt / EW; gem level capped by char level ([[gems/gem-levels]]).
- Keep EW's level ≥ the area's level cap (L10 → 52, L14 → 72, L17 → 78) or it does nothing ([[gems/cold-spell-gems]]).
- Support sockets: 2 base; Jeweller's Lesser/Greater/Perfect → 3/4/5 ([[gems/socketing-limits]]).

## c. Passives and ascendancy
- Tree: Int side; spell/cold damage, ES, cast speed. Notable names/values not in KB ([[classes/passive-tree]]) → gap; plan in-game.
- Ascendancy order: (1–2) Now and Again · (3–4) Phased Form · (5–6) Apex of the Moment (20% slow in Presence) · (7–8) one of Unbound Encore / Ultimate Command after reading the skill text (gap). Pathing small nodes unknown — may cost a point.
- Points: Act 2 Sekhemas quest (1 floor) → 1–2; Act 3 Trial of Chaos (4 trials) → 3–4; Barya AL 60+ (3 floors) → 5–6; Barya AL 75+ (4 floors, Zarokh) → 7–8 ([[classes/ascendancy-trials]]). The 7–8 run = the farm gate.

## d. Gear breakpoints
@ v=0.5.5 vol=may-change conf=? date=2026-11-23 fill=v,vol missing=conf
| Level | Weapon | Other |
|---|---|---|
| 2–5 | Wand +1 cold (ilvl 2) / +1 all (5); Staff +2 all (5) | Boots 10% MS (ilvl 1) |
| 8 | Wand 35–44% spell or cold % | Amulet +1 all spells (ilvl 10) |
| 16–18 | Staff +2 cold (18), % mods 89–108 (16) | Boots 15% (16) |
| 25 | Staff +3 all | Sapphire/Topaz rings for res |
| 33–36 | Staff +3–4 cold (36), % 109–128 (33) | Boots 20% (33) |
| 46 | % 129–148 | Boots 25% (46) |
| 55 | Staff +5–6 cold | Cold Mastery |
| 65+ | Staff % 149–188 (60), crit 80–89% (59) | Boots 30% (65) |
- src: [[builds/levelling-gear]], [[items/caster-mod-tiers]]. Staff over wand: staff % rolls are roughly double ([[items/caster-mod-tiers]]); rares cap at 3 prefixes, so +level competes with % mods ([[items/rarity]]).
- Resists: cold for Geonor (Beira +10%); fire before Rudja (Act 2) and the Azak Bog boss (Act 3) ([[builds/levelling-gear]]). Endgame penalty −60% → ~135% gear res per element ([[builds/defence-checklist]]).
- Check exchange prices before using whetstones/baubles etc. on levelling gear ([[strategy/league-lifecycle-pricing]]).


## e. Act-by-act checklist
- **Act 1:** Take Beira (+10% cold), King in the Mists (+30 spirit → Arctic Armour), Candlemass (+20 life). Crowbell / Lute weapon-set points: take if on route ([[campaign/act-1]]). Geonor: 45% cold res, ~9,200 life [INFERRED ×29] — expect 2–4 min; use the % spell wand, Unleash, kite while Arctic Armour chills his melee hits.
- **Act 2:** Sekhemas quest run (points 1–2). Sisters of Garukhan +10% lightning res (easy to miss). Kabala + Dekhara weapon-set points. Relic altar: charm option (conflict open). Jamanra, the Abomination: −15% cold res, ~111k → cold is strong here ([[campaign/act-2]], [[mechanics/monster-life]]).
- **Act 3:** +30 spirit, +10% fire res; Trial of Chaos (points 3–4); Treasures of Utzaal uncut L11; Legacy of the Vaal → free T1 waystone ([[campaign/act-3]], [[campaign/quest-rewards]]). Doryani ~176k [INFERRED].
- **Act 4:** take ring (Sapphire/Topaz for res) and amulet choices; L12 uncut gems; Dark Mists L13 (ilvl 55) ([[campaign/quest-rewards]]). 5% mana reward ([[campaign/act-4]]).
- **Interludes:** 8 points, 40 spirit, 5% life; ring/amulet/gem choices at ilvl 55 ([[campaign/interludes]]). Area 54–56 → first Cold Mastery and +5–6 cold staff rolls.

## g. Why it's good
**Strengths**
1. Spells skip accuracy and its 2–9 m penalty → full damage at range ([[mechanics/accuracy]]).
2. Gem level is the main lever: Frostbolt L15 → L20 = 250 → 467 avg hit (+87%) ([[gems/cold-spell-gems]]), and +level mods roll on floor staffs from ilvl 5 ([[builds/levelling-gear]]).
3. Honour = life + ES (+ward) — the ES layer is also the Sekhemas fail-resource ([[endgame/sekhemas]]); Phased Form cuts burst hits.

**Weaknesses → mitigation**
1. Act 1 boss 45% cold res → % spell wand over +1 level, Unleash, Arctic Armour chill; accept a slow kill ([[mechanics/monster-life]]).
2. ES blind spots: chaos does double to ES, bleed/poison bypass it, stun threshold = life ([[builds/defence-checklist]]) → chaos res 30–50%, keep a life floor, Stone/Thawing charms ([[mechanics/charms]]).
3. Mana: support cost multipliers (Unleash 150%, Considered 115%, Cold Pen 120%) stack on Frostbolt's 10–59 mana ([[gems/caster-supports]]); regen not in KB → drop Unleash after Act 2, mana regen on wand/focus slots [INFERRED].
- Also: Desperate Alliance Zarokh ×4 life is out of reach at mid budget ([[builds/kb-test-frostbolt-chronomancer-damage-0.5.5]]).

**Gear dependence**
- CP2–3 assume a self-found staff with +levels and two % prefixes — low case is one % prefix (~×0.57 vs high).
- CP4 assumes a bought ilvl 55+ staff (+5–6 cold) and ilvl 59+ crit suffix; ilvl 78+ (+5–6 all) only from T13+ maps ([[items/item-level]]).
- ES base values on armour not in KB (gap) → pool size unestimated.

## h. Map transition — first 5 upgrades
1. Boots 25–30% MS (ilvl 46 / 65) — top levelling stat priority ([[builds/levelling-gear]]).
2. Resists to 75% after −60% (~135% gear) + positive chaos res ([[builds/defence-checklist]]).
3. Staff ilvl 55+ with +5–6 cold → +2–3 gem levels (biggest damage jump).
4. Cold Mastery + 4th/5th support socket (Greater/Perfect Jeweller's, [[gems/socketing-limits]]).
5. % ES body/helmet (80–100% tiers at ilvl 60–65, [[items/caster-mod-tiers]]).
- Budget test: ≤5 div to farm T15 ([[builds/budget-tiers]]); price in exalts on days 1–3.

## i. Pivot to the farm
- What changes: tree swaps levelling damage nodes for ES/cast speed [INFERRED]; supports go Considered + Deliberation + Cold Mastery + Rapid Casting II (+ Cold Pen only vs bosses with positive cold res after EW); collect AL 60+ / 75+ Djinn Baryas from maps ([[classes/ascendancy-trials]]).
- Farm loop: 4-floor runs → jewels, relics, ascendancy carries (strongest early league; party max 6) ([[strategy/sekhemas-currency-farm]]). Sell Desperate Alliance relics; sell medium relics (merchant choice/price, honour res). Sweep profit into Divines each session ([[economy/value-retention]]).
- Respec cost: refund 20–40 points at L80 = 2,904 gold each → ~58k–116k gold ([[classes/respec]]; gold is untradeable, respec is a gold sink → [[economy/gold]]). No ascendancy change → no 5× ascendancy refund.

## j. Defence checklist (8 steps, [[builds/defence-checklist]])
1. **Res:** 75% each after −60% → ~135% on gear ([[mechanics/resistances]]).
2. **Chaos:** 30–50%; chaos does double to ES ([[mechanics/energy-shield]]).
3. **Pool:** ES + life floor; Honour = life + ES ([[endgame/sekhemas]]). ES base values gap.
4. **Primary layer:** ES (Int). Recharge after 4 s at 12.5%/s ([[mechanics/energy-shield]]).
5. **Recovery:** ES recharge + flasks ([[mechanics/flasks]]); no leech planned.
6. **Avoidance:** dodge roll ([[mechanics/dodge-roll]]); Apex 20% slow; Frostbolt chill.
7. **Stun/ailments:** stun threshold = life ([[mechanics/stun]]) → life floor; Thawing Charm vs freeze, Stone Charm vs stun ([[mechanics/charms]]).
8. **DoT:** bleed/poison skip ES → chaos res + flask/charm removal (Staunching / Antidote charms from Act 3 Tribal Vengeance, [[campaign/quest-rewards]]).
- Sekhemas afflictions that zero or halve ES (Corrosive Concoction, Shattered Shield) are the run-killers ([[endgame/sekhemas]]).
