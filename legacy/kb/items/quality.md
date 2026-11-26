# Item quality

Scope: quality on equipment, flasks, charms, jewellery. Gem quality → [[gems/quality]]. Version 0.5.5.9 unless noted. Updated batch 27 (2026-11-26).
Status: partial — the amount of quality one currency adds is still unknown.

## What quality does per item type
- Claim: Default max 20%. Martial weapons: 1% more physical damage per 1%. Armour: 1% more armour/evasion/ES/Runic Ward per 1%. Flasks: 1% more life/mana recovery per 1%. Charms: 1% increased duration per 1%. Rings/amulets: quality type boosts a category of mods. Skill gems and items that grant skills: skill-specific bonus.
- Version: 0.5.5.9
- Volatility: stable
- Source: RePoE poe2 keywords.json "Quality", "Maximum Quality", tier 2 (game data), retrieved 2026-11-17; [PoE2DB Quality](https://poe2db.tw/us/Quality), [PoE2DB Maximum Quality](https://poe2db.tw/us/Maximum_Quality), tier 2, crawl 2026-11-23
- Confidence: confirmed (game data + PoE2DB agree)
- Notes: Wands/staves: +1% to inherent skill quality per 1%; sceptres: 1% more spirit per 1% (u4gm page, tier 5 — RMT site, lead only; [INFERRED] matches wiki's "inherent skill quality" note). PoE2DB's Quality summary lists no wand/staff/sceptre effect, so this stays unverified.

## Quality currencies
- Claim: Blacksmith's Whetstone (martial weapons), Arcanist's Etcher (wand, staff, sceptre), Armourer's Scrap (armour), Glassblower's Bauble (flasks), Gemcutter's Prism (skill gems), Cartographer's Chisel (maps), Catalysts (rings/amulets — add a quality type that boosts one mod category and replaces other quality types; Refined Catalysts do the same for jewels). Charm quality can't be raised manually. All stack to 20.
- Drop level / Currency Exchange gold: Scrap 5 / 250; Etcher 5 / 500; Bauble 12 / 750; Prism 12 / 1,000; Whetstone drop level 5 (gold not shown on its page).
- Version: 0.5.x
- Volatility: stable
- Source: RePoE base_items.json descriptions, tier 2; [PoE2DB Armourer's Scrap](https://poe2db.tw/us/Armourers_Scrap), [Arcanist's Etcher](https://poe2db.tw/us/Arcanists_Etcher), [Glassblower's Bauble](https://poe2db.tw/us/Glassblowers_Bauble), [Gemcutter's Prism](https://poe2db.tw/us/Gemcutters_Prism), tier 2, crawl 2026-11-23; [poe2wiki Catalyst](https://www.poe2wiki.net/wiki/Catalyst), tier 2
- Confidence: confirmed
- Notes: Catalysts come from Breach → [[crafting/catalysts]]. Late-league prices of these → [[strategy/league-lifecycle-pricing]].

## How much quality one currency adds
- Claim: In PoE2 the amount per use depends on item level — the higher the ilvl, the less each currency adds — and the in-game help text says they're more effective on low-ilvl, non-unique items. No exact amounts found.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality), tier 2; in-game help text as shown on [poe2db Armourer's Scrap (JP)](https://poedb.tw/jp/Armourers_Scrap), tier 2; retrieved 2026-11-17
- Confidence: confirmed (wiki + game text) for the direction; amounts unknown
- Notes: The English PoE2DB crawl (2026-11-23) has no table of amounts by item level or rarity on any quality-currency page (batch 27). A tier-5 article ([Sportskeeda](https://www.sportskeeda.com/mmo/path-exile-2-poe2-improve-equipment-quality-how-what), 2026-11-26) mentions about 3% from one Armourer's Scrap — [INFERRED] lead only, no item level given. Conflict with PoE1-style "5% normal / 2% magic / 1% rare" text → [[04-conflicts]]. Practical: quality normal/low-ilvl bases before crafting; expect small steps on endgame rares [INFERRED]. Check in game.

## Going above 20%
- Claim: Vaal Infusers (Armourer's, Blacksmith's, Arcanist's, Catalysing — armour / martial weapon / wand-staff-sceptre / ring-amulet) add quality above the max by up to 10%, with a chance to corrupt; stack 10. Items found in very high-level areas can drop with up to 30% quality (quality currency still stops at 20%). Exceptional items can roll over 20% (max 30%). Breach Rings: +20% / +25% to max quality implicit; Essence of the Breach gives jewellery +20% max quality.
- Version: 0.2.0g+ (drops to 30%); Infusers 0.5.x
- Volatility: may-change
- Source: RePoE base_items.json descriptions, tier 2; [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality) version history, tier 2; [PoE2DB Quality](https://poe2db.tw/us/Quality), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Corrupt outcome on caster weapons can move quality ±10% up to 23% — see [[items/corruption]].
