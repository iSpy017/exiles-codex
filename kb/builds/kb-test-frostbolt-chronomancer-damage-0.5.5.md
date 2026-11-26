---
title: KB-test build — Frostbolt Chronomancer: damage maths (0.5.5)
status: partial
tracker_topic: "KB-test build — Frostbolt Chronomancer (0.5.5)"
tracker_note: "partial (KB-only; damage confidence low/low–med/med/low; increased/more rule now sourced in mechanics/damage-calculation — doc text not yet updated; gaps: tree notables, mana check, ×29 boss-life reading, ascendancy pathing)"
defaults: v=0.5.5 vol=may-change
---

Status: partial · Version: 0.5.5 (Forbidden Rites rules) · Written 2026-11-23 from project docs only · Volatility: may-change
Main doc → [[builds/kb-test-frostbolt-chronomancer-0.5.5]].

## Damage rules used
- Hit = (projectile + explosion) cold damage from the gem table ([[gems/cold-spell-gems]]). Spells take base damage, cast time and crit from the skill, not the weapon ([[mechanics/attack-cast-speed]]).
- [INFERRED] "increased" modifiers are summed into one multiplier; each "more"/"less" multiplies separately. Reason: no KB or corpus doc states this rule in general (KB gap, tracker row "Damage formula"); the KB does treat crit bonus as its own multiplier ([[mechanics/crit]]) and gem "more" values as separate ([[gems/caster-supports]]).
- Crit: +100% default bonus, spells use the skill's base chance (12% Frostbolt); increased crit chance multiplies the base ([[mechanics/crit]]). Expected multiplier = 1 + crit chance × 1.0.
- Resistance: damage × (1 − enemy res). Curses −50% effect on Unique, −30% Rare ([[mechanics/skill-interactions]]). Penetration is hits-only and can't push res below 0% ([[mechanics/exposure-penetration]]).
- Cast speed: increased cast speed and skill speed add together ([[mechanics/attack-cast-speed]]); Considered Casting's 15% less cast speed multiplies.
- Chronomancer "Now and Again": 20% chance to Repeat → ×1.2 average [INFERRED: one extra full-damage cast per Repeat] ([[classes/sorceress-ascendancies]]).
- Boss life = page life × 29 for Unique rarity — [INFERRED] reading ([[mechanics/monster-life]]); if wrong, boss life is 29× lower.
- Passive tree % damage: no notable values in the KB ([[classes/passive-tree]] lists keystones only) → assumed ranges, flagged per checkpoint.
- Both projectile and explosion hit the boss: [INFERRED] (gem text doesn't say). If only the explosion hits, damage ×0.62; projectile only ×0.38 (from the L20 split 180 vs 287 avg).

## Checkpoint 1 — Count Geonor (Ogham Manor, area 15), char ~14–15
@ v=0.5.5 vol=may-change conf=? date=2026-11-23 fill=v,vol missing=src
| Step | Value | Source |
|---|---|---|
| Frostbolt L5 (char 14) | (15–23) + (26–39) = 19 + 32.5 = **51.5** | cold-spell-gems |
| …or L6 via +1 wand (ilvl 5) | 23.5 + 39.5 = **63** | levelling-gear |
| Increased: wand 35–44% spell dmg (ilvl 8) **or** the +1 level (one magic prefix), tree 0–15% [INFERRED] | ×1.0–1.59 | caster-mod-tiers, rarity |
| More: none — Considered Casting is tier 2 (uncut support L2 drops from ilvl 16) | ×1.0 | caster-supports, uncut-gems |
| Geonor 45% cold res | ×0.55 | monster-life |
| Crit 12% | ×1.12 | crit |
| Casts/s: 1/0.8 = 1.25; + 9–12% cast speed suffix | 1.25–1.40 | cold-spell-gems, caster-mod-tiers |
| Unleash (tier 1): 2 Seals, one per 200% cast time, Repeats at 50% less | ×1.0–1.25 [INFERRED] | caster-supports |
- Low: 51.5 × 1.0 × 0.55 × 1.12 × 1.25 = **40 DPS**. High: 51.5 × 1.59 × 0.55 × 1.12 × 1.40 × 1.25 = **88 DPS** (the % wand beats +1 level here: ×1.44 vs ×1.22).
- Geonor: 318 page life × 29 ≈ **9,200** [INFERRED] → **105–230 s**. If the ×29 reading is wrong: 318 life → 4–8 s.
- Clear: Frostbolt pierces all targets; explosion radius 2.4 m on terrain; Ice Nova can originate from the bolt ([[gems/cold-spell-gems]]). Area-15 normal monster = 134 life at 100% life multiplier ([[mechanics/monster-life]]); a 51.5 hit vs 0% res kills one in ~3 hits [INFERRED arithmetic].
- Enough? KB has no act-boss kill-time benchmark (gap). 2–4 min is slow; Arctic Armour chills him on his melee hits (Geonor's PoE2DB tags show a one-hand-sword melee) [INFERRED].

- conf: **low** — limited by the ×29 reading and the both-parts-hit assumption.

## Checkpoint 2 — Campaign end (Act 4, area 53), char ~52
@ v=0.5.5 vol=may-change conf=? date=2026-11-23 fill=v,vol missing=src
- Proxy boss: Tavakai, the Chieftain (Heart of the Tribe, 53): 10,485 page × 29 ≈ **304k**, res 45% fire / 0% cold ([[mechanics/monster-life]]). Exact final Act 4 boss not in the KB (gap); this is the highest-life Act 4 page found.
| Step | Low | High | Source |
|---|---|---|---|
| Gem: L12–13 (char 46/52) + staff +3 all (ilvl 25) or +3–4 cold (ilvl 36) → L15 / L17 | 95 + 155 = **250** | 123.5 + 199 = **322.5** | cold-spell-gems, levelling-gear |
| Increased: staff spell% 129–148 + cold% 129–148 (ilvl 46) + tree 20–40% [INFERRED]; low case = only one % prefix | ×2.5 | ×4.4 | caster-mod-tiers |
| More: Considered Casting 35% × Deliberation 20% | ×1.62 | ×1.62 | caster-supports |
| Cold Penetration: useless (0% res; pen floors at 0) | — | — | exposure-penetration |
| Elemental Weakness L12 (cap 61 ≥ 53): −51% × 0.5 Unique = −25.5% | ×1.255 | ×1.255 | cold-spell-gems, skill-interactions |
| Crit: base 12%; staff spell crit 60–69% at ilvl 28 → 19–20% | ×1.12 | ×1.20 | crit, caster-mod-tiers |
| Casts/s: 1.25 × (1 + staff 26–31% + Chronomancer 6%) × 0.85 | 1.40 | 1.45 | caster-mod-tiers, sorceress-ascendancies |
| Now and Again | ×1.2 | ×1.2 | sorceress-ascendancies |
- Low 250 × 2.5 × 1.62 × 1.255 × 1.12 × 1.40 × 1.2 = **2,400 DPS**; High 322.5 × 4.4 × 1.62 × 1.255 × 1.20 × 1.45 × 1.2 = **6,000 DPS**.
- Tavakai ≈ 304k → **50–125 s**. Rares at 53: 3,102 × 8 = ~25k → 4–10 s.

- conf: **low–medium** — limited by self-found staff prefixes (3-prefix limit, [[items/rarity]]) and the ×29 reading.

## Checkpoint 3 — First maps (T1–T4, area 65–68), self-found, char ~66
@ v=0.5.5 vol=may-change conf=? date=2026-11-23 fill=v,vol missing=src
| Step | Low | High | Source |
|---|---|---|---|
| Gem L16 (char 66) + staff +3–4 cold (36) or +5 (55) + Cold Mastery +1 (support L5 from ilvl 55) → L20 / L22 | 180 + 287 = **467** | 229.5 + 364 = **593.5** | cold-spell-gems, caster-supports |
| Increased: staff % prefixes at ilvl 33–60 + tree 30–60% [INFERRED] | ×3.5 | ×4.6 | caster-mod-tiers |
| More: Considered × Deliberation | ×1.62 | ×1.62 | caster-supports |
| EW L14 (cap 72): −53% × 0.5 vs Unique; map-boss res unknown, assume 0% [INFERRED] | ×1.265 | ×1.265 | cold-spell-gems |
| Crit | ×1.12 | ×1.20 | crit |
| Casts/s (staff 31%, Chrono 6%, ×0.85) | 1.46 | 1.47 | caster-mod-tiers |
| Now and Again | ×1.2 | ×1.2 | — |
- Low **6,500 DPS**; High **11,800 DPS**.
- Targets: normal monster at 65 = 6,555 × life%; rare = 6,555 × 8 ≈ **52k** → 4–8 s; per-cast hit 3.3–5.6k → 2–4 casts per normal monster [INFERRED arithmetic]. Map-boss life % not in KB (gap): at 300% × 29 ≈ 570k → 50–90 s.
- Clear-relevant: pierce all + 2.4 m explosion; projectile speed 2.8 m/s is slow — Multishot I adds +2 projectiles for 35% less damage and 20% less skill speed if clear lags ([[gems/caster-supports]]).

- conf: **medium** — limited by map-boss life % and tree % increased.

## Checkpoint 4 — Farm-ready, mid budget (5–50 div, [[builds/budget-tiers]]), Sekhemas area 75
@ v=0.5.5 vol=may-change conf=? date=2026-11-23 fill=v,vol missing=src
- Target: Zarokh at Barya area 75: base 18,609 (L75 row of the base-life table, [[mechanics/monster-life]]) × 750% × 29 ≈ **4.0M** (first version used an interpolated ~16,500 → 3.6M); res 15% (PoE2DB) or 0% (PoB) — conflict in [[conflicts]].
| Step | Low | High | Source |
|---|---|---|---|
| Gem L18 (char 78) + bought staff +5–6 cold (ilvl 55) + Cold Mastery + amulet +1–2 (ilvl 10/41) → L25 / L27 | 330 + 516.5 = **846.5** | 419.5 + 651.5 = **1,071** | cold-spell-gems, levelling-gear |
| Increased: staff spell 149–188 + cold 149–188 (ilvl 60) + tree 50–100% [INFERRED] | ×4.5 | ×5.8 | caster-mod-tiers |
| More: Considered × Deliberation; 5th socket Rapid Casting II (20% cast speed) instead of Cold Pen (EW already takes res below 0) | ×1.62 | ×1.62 | caster-supports, exposure-penetration |
| Res: 15% − 27.5% (EW L16/17 × 0.5) = −12.5% → ×1.125; if base 0% → ×1.275 | ×1.125 | ×1.275 | cold-spell-gems, monster-life |
| Crit: staff 80–89% (ilvl 59) → 21.6–22.7% | ×1.22 | ×1.22 | caster-mod-tiers |
| Casts/s: 1.25 × (1 + 38–43% + 6% + 20%) × 0.85 | 1.74 | 1.80 | caster-mod-tiers, caster-supports |
| Now and Again | ×1.2 | ×1.2 | — |
- Low **17,700 DPS**; High **33,800 DPS** → Zarokh **120–229 s** (4.0M ÷ DPS; was 105–205 s at 3.6M).
- Desperate Alliance relic: Zarokh takes 75% less damage (×4 life) and deals 100% more ([[endgame/sekhemas]]) → 8–15 min. **Not viable at this budget** — sell those relics (creator did the same early: [[strategy/sekhemas-currency-farm]]).

- conf: **low** — limited by staff ilvl 78+ availability, tree %, Zarokh area-75 life (interpolated), res conflict.

## Swing table — which input moves the result most
| Input | Swing | Fix |
|---|---|---|
| ×29 Unique life reading | ×29 on every boss kill time | Watch Geonor's health bar vs one Frostbolt hit |
| Projectile + explosion both hit | ×0.38–1.0 | Training dummy / PoB 0.5.5 |
| Tree % increased damage | ±25–40% | PoB tree for a level-66 / 78 Sorceress |
| Staff prefixes (3 max) | ×1.8 between low/high CP2 | Real drops |
| Increased-vs-more convention | if wrong, all numbers invalid | Source poe2wiki Damage page |
