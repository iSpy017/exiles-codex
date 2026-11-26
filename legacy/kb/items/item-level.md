# Item level & drop level

Scope: how item level is set, drop level, waystone tier → area level, which content unlocks top mod tiers. Version 0.5.x unless noted.

## Item level = level of the source
- Claim: An item's level is the monster level of what dropped it (monster level = area level, +1 for magic/rare monsters, +2 for bosses, +1 more in irradiated maps or maps with Coalesced Corruption — these stack). Chests and other non-monster sources drop at area level. Some encounter difficulty modifiers raise area level by up to +2.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Level](https://poe2wiki.net/wiki/Level), [poe2wiki Item](https://poe2wiki.net/wiki/Item), tier 2, retrieved 2026-11-17
- Confidence: confirmed (two wiki pages agree)
- Notes: Item level is fixed at drop and can't be raised later [INFERRED]: no currency for it found so far; one tier-5 site says the same. Matters for crafting bases.

## Drop level
- Claim: Most items have a drop level = minimum area/monster level needed to drop. For equipment it usually equals the base's required level.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Item (Drop level)](https://www.poe2wiki.net/wiki/Drop_level), tier 2; RePoE base_items.json `drop_level`, tier 2, retrieved 2026-11-17
- Confidence: confirmed
- Notes: Highest equipment drop levels in data: 80 (armour pieces, foci), 79 (most weapons), 65 (amulets, belts, sceptres, quivers, wands, claws), 52 (rings). Uncut gem drop levels → [[uncut-gems]].

## Waystone tier → area level
- Claim: Tier 1 = area level 65, +1 per tier, Tier 16 = 80. T7 = 71, T11 = 75, T15 = 79. T16 can't drop normally — you get it by corrupting a T15 (25% chance of tier ±1).
- Version: 0.5.x
- Volatility: may-change (1.0 atlas rework)
- Source: [poe2wiki Level](https://poe2wiki.net/wiki/Level), tier 2; [PoE2DB Waystones](https://poe2db.tw/us/Waystones), tier 2; [poe2wiki Waystone (Tier 16)](https://poe2wiki.net/wiki/Waystone_(Tier_16)), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Waystone drop levels: T1 = 58 (poe2wiki Waystone (Tier 1)). Full mechanics → endgame/waystones.

## What each map tier unlocks (top-tier mods)
- Claim: Using the ladders in [[affix-tiers]]:
  - ilvl 71+ (T7 map, or rare/boss in T5–6): 36–40% res tier on rings; 175–189 life on body armours.
  - ilvl 75+ (T11): 190–199 life; 155–169% phys tier.
  - ilvl 80 (T16, or a rare in T15 = 80, boss in T14 = 80): 200–214 life (top).
  - ilvl 82 (boss in T16, or rare in irradiated/corrupted T16): top res (41–45%), top movement speed (35%), top % phys (170–179%).
  - ilvl 83: needed only for a couple of mods (local chaos damage).
- Version: 0.5.5.9
- Volatility: may-change
- Source: derived from RePoE mods.json (tier 2) + poe2wiki Level monster-level rules (tier 2), retrieved 2026-11-17
- Confidence: [INFERRED] — my arithmetic combining two sourced rules; the exact +1/+2 stacking per content type needs an in-game check.
- Notes: Answers the video's "T7 = better mod tiers" claim ([[league-start-framework]]): yes — T7 is where the second-from-top tiers of many mods start to roll. The very top tiers need ilvl 80–82, i.e. T15/T16 rares and bosses. Crafting-base buying rule: ilvl 82 for best mods; 75+ is fine for mid-tier crafts.

## XP penalty vs area level
- Claim: Full XP if the area level is within 3 + (character level ÷ 16) of your level. E.g. at L60 you can run T1–2 (65–66) penalty-free; from about L72 to L88, T15 is penalty-free.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Endgame power leveling](https://mobalytics.gg/poe-2/guides/endgame-power-leveling-experience-gain), tier 3, retrieved 2026-11-17
- Confidence: single-source
- Notes: Relevant to the skip route and the early-map plan. → campaign/levelling-routes, strategy/skip-route.
