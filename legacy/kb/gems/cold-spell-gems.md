# Cold spell & cold persistent gems (per-level data)

Version: 0.5.x (PoE2DB crawl 2026-11-23, game data 0.5.x era). Re-check at 1.0 (support rebalance, tree overhaul).
Source for every row unless noted: PoE2DB gem pages in the local corpus → [[tools/poe2db-corpus]]. Cite as [PoE2DB <Page>](https://poe2db.tw/us/<Page>), tier 2, crawl 2026-11-23. Single-source (game-data derived); spot-check in game.
Columns: gem level → required char level (same schedule as [[gems/gem-levels]]) → hit damage range.

## Frostbolt
- Claim: Tier 5 spell (needs an uncut skill gem L5+). Tags: Spell, AoE, Projectile, Cold, Repeatable. Cast time 0.80 s, base crit 12%, projectile speed 2.8 m/s. Slow piercing projectile that explodes on hitting terrain (explosion radius 2.4 m). Projectile has (100→195)% more chill magnitude. Can be cast while moving (−70% movement speed while casting). Quality: up to 20% more projectile damage after piercing, up to 40% more projectile speed.
- Per level (projectile cold dmg · explosion cold dmg · mana):
  | Gem | Char | Projectile | Explosion | Mana |
  |---|---|---|---|---|
  | 1 | 0 | 5–8 | 9–13 | 5 |
  | 3 | 6 | 9–14 | 16–24 | 8 |
  | 5 | 14 | 15–23 | 26–39 | 10 |
  | 6 | 18 | 19–28 | 32–47 | 12 |
  | 7 | 22 | 23–34 | 38–57 | 14 |
  | 9 | 31 | 32–48 | 53–80 | 18 |
  | 10 | 36 | 38–56 | 62–93 | 20 |
  | 11 | 41 | 44–66 | 72–108 | 22 |
  | 12 | 46 | 51–76 | 83–124 | 25 |
  | 13 | 52 | 58–87 | 95–143 | 28 |
  | 14 | 58 | 67–100 | 109–163 | 32 |
  | 15 | 64 | 76–114 | 124–186 | 35 |
  | 16 | 66 | 87–130 | 141–211 | 39 |
  | 17 | 72 | 99–148 | 159–239 | 44 |
  | 18 | 78 | 112–168 | 180–270 | 48 |
  | 19 | 84 | 127–190 | 204–305 | 53 |
  | 20 | 90 | 144–216 | 230–344 | 59 |
  | 21 | — | 162–244 | 259–388 | 65 |
  | 22 | — | 184–275 | 291–437 | 72 |
  | 23 | — | 207–311 | 327–491 | 79 |
  | 24 | — | 234–351 | 368–552 | 87 |
  | 25 | — | 264–396 | 413–620 | 96 |
  | 26 | — | 298–446 | 464–697 | 105 |
  | 27 | — | 336–503 | 521–782 | 115 |
  | 28 | — | 379–568 | 586–878 | 126 |
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Frostbolt](https://poe2db.tw/us/Frostbolt), tier 2, crawl 2026-11-23 (page lists levels to 40)
- Confidence: single-source
- Notes: levels above 20 come from +level gear/supports ([[builds/levelling-gear]]) or corruption ([[gems/gem-levels]]). Whether one target can take both the projectile hit and the explosion is not stated on the page → [INFERRED] yes for the first target the bolt hits before a wall; test in game. PoE2DB "recommended supports": Multishot I, Projectile Acceleration I, Unleash (T1); Multishot II, Ricochet I, Considered Casting (T2); Inexorable Critical I, Deliberation (T3); Rapid Casting II, Ricochet II (T4); Projectile Acceleration III, Cold Mastery (T5) → [[gems/caster-supports]].

## Ice Nova
- Claim: Tier 1 spell (any uncut skill gem). Tags: Spell, AoE, Cold, Duration, Nova, Repeatable. Cast time 1.00 s, base crit 12%. Wave of ice around you with knockback; **cast near a Frostbolt projectile, it originates from the projectile instead**. Consumes a Cold Infusion if available to leave Chilled Ground. (100→157)% more chill magnitude and freeze buildup.
- Per level (cold dmg · mana): L1 6–8 (7) · L3 9–13 (10) · L5 14–21 (13) · L7 21–31 (17) · L9 29–44 (22) · L10 34–51 (25) · L12 46–69 (32) · L14 61–91 (40) · L16 79–119 (49). A second damage column on the page (L1 15–22 → L16 265–397) is unlabelled in the crawl text — [INFERRED] the Cold-Infusion-empowered value; verify.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Ice Nova](https://poe2db.tw/us/Ice_Nova), tier 2, crawl 2026-11-23
- Confidence: single-source

## Arctic Armour (persistent)
- Claim: Tier 4, 30 spirit, instant, 0.25 s cooldown. Icy barrier gains stages; a melee attack that hits you removes a stage and deals cold spell damage to the attacker. 100% more chill magnitude, 100% more freeze buildup. Quality: up to 20% increased armour per stage.
- Per level (dmg per stage · seconds per stage · max stages): L1 3–5 · 1.25 s · 2 | L4 8–12 · 1.13 · 3 | L10 25–38 · 0.98 · 3 | L11 29–44 · 0.95 · 4 | L14 46–68 · 0.88 · 4 | L20 101–152 · 0.73 · 5.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Arctic Armour](https://poe2db.tw/us/Arctic_Armour), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: retaliation vs melee only — no ranged/spell protection. Spirit → [[mechanics/spirit-reservation]].

## Herald of Ice (persistent) — needs a martial weapon
- Claim: Tier 4, 30 spirit. **Requires any martial weapon.** Shattering an enemy with a non-Herald attack hit causes an icy explosion dealing (70→286)% attack damage, 1.6 m radius, 100% phys→cold, can't be evaded. Quality: up to 20% increased cold damage.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Herald of Ice](https://poe2db.tw/us/Herald_of_Ice), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: **not usable by a wand/staff caster** — attack-triggered and martial-weapon-gated.

## Elemental Weakness (curse)
- Claim: Tier 7, cast time 0.70 s. Curses all targets in an area after 1.5 s. Curse inflicts −40% (L1) to −59% (L20) elemental resistances; radius 1.5 → 3.1 m; duration ~6–7.4 s. **Curse does not apply to enemies above a level cap that rises with gem level**: L1 → 20, L5 → 32, L10 → 52, L12 → 61, L14 → 72, L16 → 76, L17 → 78; from L18 no cap shown (0 = none, [INFERRED]). Res values: L10 −49, L12 −51, L14 −53, L16 −55, L17 −56.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Elemental Weakness](https://poe2db.tw/us/Elemental_Weakness), tier 2, crawl 2026-11-23
- Confidence: single-source; "0 = no cap" reading [INFERRED]
- Notes: curse effect is reduced on tougher enemies (15% less Magic, 30% Rare, 50% Unique) → [[mechanics/skill-interactions]]. So vs a Unique boss: −40% × 0.5 = −20% [INFERRED arithmetic]. Gem must be high enough for the area level, or the curse does nothing.
