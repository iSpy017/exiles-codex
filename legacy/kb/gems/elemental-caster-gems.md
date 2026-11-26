# Elemental caster gems — Spark, Flame Wall, Tornado, Thunderstorm (per-level data)

Status: done for 0.5.x. Re-check at 1.0 (support rebalance, tree overhaul). These are the engine gems of [[builds/storm-shaman]].
Source for every table: the gem's PoE2DB page ([Spark](https://poe2db.tw/us/Spark), [Flame Wall](https://poe2db.tw/us/Flame_Wall), [Tornado](https://poe2db.tw/us/Tornado), [Thunderstorm](https://poe2db.tw/us/Thunderstorm)), tier 2, local crawl 2026-11-23 ([[tools/poe2db-corpus]]), extracted 2026-11-26. Confidence: single-source (game data). "Char" = required character level (same schedule as [[gems/gem-levels]]).

## Spark
- Claim: Tier 1 spell, cast time 0.70 s. Erratic projectiles that run along the ground until they hit or expire (2 s duration); projectiles fired together can hit the same target at most once per 0.66 s. **Consumes a Cold Infusion if available** to fire many icy sparks in a circle dealing cold and lightning.
- | Gem | Char | Mana | Lightning dmg | Projectiles | Cold-infused cold dmg | Cold-infused projectiles |
  |---|---|---|---|---|---|---|
  | 1 | 0 | 5 | 1–10 | 4 | 7–11 | 12 |
  | 5 | 14 | 10 | 1–26 | 5 | 22–33 | 13 |
  | 7 | 22 | 13 | 2–39 | 6 | 33–49 | 13 |
  | 10 | 36 | 19 | 3–64 | 6 | 54–81 | 14 |
  | 12 | 46 | 24 | 5–86 | 7 | 73–109 | 14 |
  | 14 | 58 | 30 | 6–114 | 7 | 96–144 | 15 |
  | 16 | 66 | 37 | 8–148 | 8 | 125–187 | 15 |
  | 18 | 78 | 46 | 10–191 | 8 | 161–242 | 16 |
  | 20 | 90 | 56 | 13–245 | 9 | 207–310 | 16 |
  | 21 | — | 62 | 15–277 | 9 | 233–350 | 17 |
- Notes: the cold columns are the Cold-Infused version ([INFERRED] from the column labels + gem text "consumes a Cold Infusion… many sparks in a circle"; version history: added in 0.3.0). Spark's wide lightning range (1 to max) makes the average hit about half the max.
- Version history (PoE2DB): 0.2.0 — 4–9 projectiles at gem 1–20 (was 6–14).

## Flame Wall
- Claim: Tier 1 spell, cast time 1.00 s. Wall of fire in front of you that ignites everything in it; projectiles you or allies fire through it gain added fire damage; consumes a Lightning Infusion if possible to also add lightning to those projectiles.
- | Gem | Char | Mana | Ignites as if dealing | Wall fire DPS | Length (m) | Duration (s) | Added fire to projectiles | Infused: added lightning |
  |---|---|---|---|---|---|---|---|---|
  | 1 | 0 | 10 | 5–8 | 1.8 | 5.0 | 4.5 | 2–3 | 1–4 |
  | 5 | 14 | 20 | 16–24 | 5.3 | 5.4 | 4.9 | 5–7 | 1–12 |
  | 7 | 22 | 26 | 24–37 | 8.1 | 5.6 | 5.1 | 7–10 | 1–16 |
  | 10 | 36 | 38 | 41–62 | 13.7 | 5.9 | 5.4 | 10–15 | 1–24 |
  | 12 | 46 | 48 | 57–85 | 18.8 | 6.1 | 5.6 | 13–19 | 2–31 |
  | 14 | 58 | 60 | 77–115 | 25.4 | 6.3 | 5.8 | 16–24 | 2–38 |
  | 16 | 66 | 74 | 103–154 | 33.9 | 6.5 | 6.0 | 19–29 | 2–46 |
  | 18 | 78 | 91 | 137–205 | 45.1 | 6.7 | 6.2 | 23–35 | 3–55 |
  | 20 | 90 | 111 | 181–271 | 59.6 | 6.9 | 6.4 | 27–41 | 3–65 |
  | 21 | — | 123 | 208–311 | 68.5 | 7.0 | 6.5 | 29–44 | 4–70 |
- Notes: "Ignites as though dealing X" = the ignite is calculated from that value, not from the wall's DPS ([[mechanics/ignite]]: 20%/s of the fire hit). Flame Wall's mana cost is about double Spark's at every level — [INFERRED arithmetic] run a sustain check ([[mechanics/mana-costs]]).

## Tornado
- Claim: Tier 11 spell, cast time 0.75 s. Storm that pulls enemies in and deals physical damage over time; overlapping an Elemental Ground Surface absorbs that surface's debuff, applies it inside the Tornado and adds DoT of that element. Spell damage modifiers apply to the debuff's DoT. Radius 3 m, duration 8 s, limit 1 Tornado. Needs Str and Int.
- | Gem | Char | Mana | Phys DPS | DPS per absorbed element |
  |---|---|---|---|---|
  | 1 | 0 | 10 | 3 | 6.1 |
  | 5 | 14 | 20 | 11.2 | 22.4 |
  | 10 | 36 | 37 | 30.7 | 61.4 |
  | 12 | 46 | 47 | 43 | 86 |
  | 14 | 58 | 59 | 59.2 | 118.3 |
  | 16 | 66 | 73 | 80.5 | 160.9 |
  | 18 | 78 | 90 | 108.6 | 217.3 |
  | 20 | 90 | 110 | 146.1 | 292.2 |
  | 21 | — | 121 | 169.3 | 338.6 |
- Notes: tier 11 means you can't engrave it until an uncut skill gem of level 11+ ([[gems/uncut-gems]]) — [INFERRED] so it arrives mid/late campaign, not at league start. Limit 1 — one Tornado at a time.

## Thunderstorm
- Claim: Tier 5 spell, cast time 0.90 s, castable while moving. Storm (2.3 m radius, 12 s, limit 1) hits one target every 0.35 s, each enemy at most once per 0.5 s. Enemies inside are **Drenched**: 50% more chance to be shocked, 25% more freeze buildup, lingering 2 s. **Drench has an enemy-level cap tied to gem level.**
- | Gem | Char | Mana | Lightning dmg | Can't Drench enemies above level |
  |---|---|---|---|---|
  | 1 | 0 | 12 | 1–5 | 20 |
  | 5 | 14 | 23 | 1–16 | 32 |
  | 7 | 22 | 30 | 1–24 | 39 |
  | 10 | 36 | 44 | 1–41 | 52 |
  | 12 | 46 | 55 | 1–56 | 61 |
  | 14 | 58 | 69 | 2–76 | 72 |
  | 15 | 64 | 77 | 2–88 | 74 |
  | 16 | 66 | 86 | 3–102 | 76 |
  | 17 | 72 | 95 | 3–117 | 78 |
  | 18 | 78 | 105 | 3–135 | 0 (no cap shown) |
  | 20 | 90 | 129 | 5–179 | 0 |
- Notes: [INFERRED] "0" = no cap; the cap schedule (L14 72, L16 76, L17 78) is the same as Elemental Weakness's curse cap ([[gems/cold-spell-gems]]). Practical consequence [INFERRED arithmetic, waystone T1 = area 65 per [[items/item-level]]; magic/rare monsters +1]: gem 16 stops working on T12 rares and all of T13+ (area 77); gem 17 stops on T14 rares and T15+ (area 79). Get gem 18 (or +level gear) before high-tier maps. Quality adds up to 5% more freeze, 10% more shock chance, 20% more area.

## Recommended supports (PoE2DB's own list, not tested)
- Thunderstorm: Magnified Area I, Prolonged Duration I, Coursing Current (T1); Lightning Penetration, Shock Conduction, Living Lightning (T2); Magnified Area II, Prolonged Duration II, Elemental Discharge (T3); Lightning Exposure, Living Lightning II, Advancing Storm (T4); Expand, Lightning Mastery (T5).
- Source: PoE2DB Thunderstorm page, tier 2 · single-source. Use as a shortlist only ([[builds/storm-shaman-levelling]]).
