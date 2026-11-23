# Caster / cold support gems (effect values)

Version: 0.5.x (PoE2DB crawl 2026-11-23). Re-check at 1.0 — GGG announced a support rebalance and merged elemental penetration supports ([[gems/support-tiers]]).
Source for every entry: PoE2DB support pages in the local corpus ([[tools/poe2db-corpus]]), tier 2, crawl 2026-11-23. Single-source (game-data derived).
Rules: one support per Category per skill; tier = minimum uncut support level ([[gems/support-tiers]]). Uncut support L2 drops from ilvl 16, L3 33, L4 45, L5 55 ([[gems/uncut-gems]]).

| Support | Tier | Category | Effect (all values "final" multipliers where it says more/less) | Cost mult. | Attr |
|---|---|---|---|---|---|
| Unleash | 1 | Seal | Repeatable spells you cast yourself gain a Seal every 200% of cast time, max 2 Seals; each Seal broken = 1 Repeat; **50% less damage when Repeating**. Can't support cooldown skills | 150% | +5 Int |
| Multishot I | 1 | Additional Projectiles | +2 projectiles; **35% less damage**; 20% less skill speed | 100% | +5 Dex |
| Considered Casting | 2 | Considered Casting | Spells you cast yourself: **35% more damage**, 15% less cast speed | 115% | +5 Int |
| Cold Penetration | 2 | Cold Penetration | Hits **penetrate 30% cold resistance** | 120% | +5 Int |
| Deliberation | 3 | Deliberation | Skills usable while moving: **20% more damage**, 30% more movement-speed penalty while using | 100% | +5 Dex |
| Inexorable Critical I | 3 | Inexorable Critical | +10% increased crit chance per second, up to 100%; lost when the skill crits | 120% | +5 Int |
| Rapid Casting II | 4 | Rapid Casting | 20% increased cast speed | 100% | +5 Int |
| Cold Exposure | 4 | Cold Exposure | Inflict Exposure for 8 s on **critical hit with cold damage** | 120% | +5 Int |
| Cold Mastery | 5 | Mastery | +1 level to supported cold skills | 100% | +5 Int |

- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Unleash](https://poe2db.tw/us/Unleash), [Multishot I](https://poe2db.tw/us/Multishot_I), [Considered Casting](https://poe2db.tw/us/Considered_Casting), [Cold Penetration](https://poe2db.tw/us/Cold_Penetration), [Deliberation](https://poe2db.tw/us/Deliberation), [Inexorable Critical I](https://poe2db.tw/us/Inexorable_Critical_I), [Rapid Casting II](https://poe2db.tw/us/Rapid_Casting_II), [Cold Exposure](https://poe2db.tw/us/Cold_Exposure), [Cold Mastery](https://poe2db.tw/us/Cold_Mastery), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes:
  - Considered Casting history: 40% → 35% more damage and cost 100% → 115% in 0.2.0 (page version history).
  - Cold Exposure page header says "when it inflicts Freeze" but the stat line says "on Critical Hit with Cold Damage" → recorded in kb/04-conflicts.md; the stat line is the game text [INFERRED: header is stale description].
  - Exposure default = −20% elemental res for 4 s ([[mechanics/exposure-penetration]]); this support overrides duration to 8 s.
  - Penetration is hits-only and floors at 0% ([[mechanics/exposure-penetration]]).
  - Cost multipliers stack on the skill's mana cost [INFERRED: "Cost Multiplier" wording]; exact stacking (multiply vs add) unverified → mana gap.
  - Attribute requirement: +5 to the gem's attribute per socketed support ([[gems/socketing-limits]]).

## Inexorable Critical — effective crit [INFERRED arithmetic]
- On a 12% base spell (Frostbolt/Ice Nova), the support ramps 0 → 100% increased over 10 s and resets on crit. Average extra crit depends on cast rate and hit count; with many hits per second the bonus resets quickly. Treat as +20–50% increased crit chance on bosses, near 0 in packs. Reason: reset-on-crit + crit chance 12–24% per hit. Verify in PoB.

## Unleash — damage per cast [INFERRED arithmetic]
- With 2 Seals stored: 1 normal hit + 2 Repeats at 50% less = 1 + 0.5 + 0.5 = 2.0× one cast's damage, but Seals refill only every 2× cast time each. Sustained value is a burst tool, not a flat multiplier. Verify in PoB.
