# Item quality

Scope: quality on equipment, flasks, charms, jewellery. Gem quality → [[gems/quality]]. Version 0.5.5.9 unless noted.

## What quality does per item type
- Claim: Default max 20%. Martial weapons: 1% more physical damage per 1%. Armour: 1% more armour/evasion/ES/Runic Ward per 1%. Flasks: 1% more life/mana recovery per 1%. Charms: 1% increased duration per 1%. Rings/amulets: quality type boosts a category of mods. Skill gems and items that grant skills: skill-specific bonus.
- Version: 0.5.5.9
- Volatility: stable
- Source: RePoE poe2 keywords.json "Quality", "Maximum Quality", tier 2 (game data), retrieved 2026-11-17; [poe2db Quality](https://poe2db.tw/us/Quality), tier 2
- Confidence: confirmed
- Notes: Wands/staves: +1% to inherent skill quality per 1%; sceptres: 1% more spirit per 1% (u4gm page, tier 5 — RMT site, lead only; [INFERRED] matches wiki's "inherent skill quality" note). Verify sceptre line in crafting batch.

## Quality currencies
- Claim: Blacksmith's Whetstone (martial weapons), Arcanist's Etcher (wand, staff, sceptre), Armourer's Scrap (armour), Glassblower's Bauble (flasks), Gemcutter's Prism (gems), Catalysts (rings/amulets — add a quality type that boosts one mod category and replaces other quality types). Charm quality can't be raised manually.
- Version: 0.5.5.9
- Volatility: stable
- Source: RePoE base_items.json descriptions, tier 2; [poe2wiki Catalyst](https://www.poe2wiki.net/wiki/Catalyst), [poe2wiki Exceptional items](https://www.poe2wiki.net/wiki/Exceptional_items), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Drop levels in data: whetstone/etcher/scrap 5, bauble 12. Catalysts come from Breach (wiki). Catalyst types seen: Adaptive (attributes), Carapace (defences), Chayula's (chaos), Esh's (lightning), Tul's (cold), Uul-Netol's (physical), Flesh (life), Neural (mana), Reaver (attack), Sibilant (caster), Skittering (speed) — list partly from tier-5 source, confirm in crafting batch. Late-league prices of these → [[league-lifecycle-pricing]].

## How much quality one currency adds
- Claim: In PoE2 the amount per use depends on item level — the higher the ilvl, the less each currency adds — and the in-game help text says they're more effective on low-ilvl, non-unique items.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality), tier 2; in-game help text as shown on [poe2db Armourer's Scrap (JP)](https://poedb.tw/jp/Armourers_Scrap), tier 2; retrieved 2026-11-17
- Confidence: confirmed (wiki + game text). Exact amounts per ilvl not found.
- Notes: Conflict with PoE1-style "5% normal / 2% magic / 1% rare" text on poe2db's community-wiki section. Logged in [[04-conflicts]]. Practical: quality normal/low-ilvl bases before crafting; expect 1% steps on endgame rares [INFERRED].

## Going above 20%
- Claim: Vaal Infusers (Armourer's, Blacksmith's, Arcanist's, Catalysing) add quality above the max by up to 10%, with a chance to corrupt. Items found in very high-level areas can drop with up to 30% quality (but quality currency still stops at 20%). Exceptional items can roll over 20% (max 30%). Breach Rings: +20% / +25% to max quality implicit.
- Version: 0.2.0g+ (drops to 30%); Infusers 0.5.x
- Volatility: may-change
- Source: RePoE base_items.json descriptions, tier 2; [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality) version history, tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Corrupt outcome on caster weapons can move quality ±10% up to 23% — see [[corruption]].
