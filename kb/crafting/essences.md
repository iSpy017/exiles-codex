# Essences

Scope: essence tiers, what each family adds, corrupted essences. Version 0.5.5.9 unless noted. Farming essences → endgame/atlas (batch 13).

## Tiers and what they do
- Claim: Lesser, normal and Greater essences upgrade a magic item to rare and add one guaranteed mod. Perfect essences — and the special "corrupted" essences — work on rares: they remove a random mod and add a guaranteed one.
- Version: 0.5.5.9 (rework in 0.3)
- Volatility: may-change
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) essence descriptions, tier 2 (game data); [poe2wiki Essence](https://www.poe2wiki.net/wiki/Essence), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Some guides (game8) still describe essences as normal → magic — that's pre-0.3 behaviour; ignore. Omens of Sinistral/Dextral Crystallisation make Perfect/corrupted essences remove only a prefix/suffix ([[omens]]). Essences drop from monsters frozen in essences (poe2wiki).

## Drop levels by tier (game data)
- Claim: Lesser 20–25 (some base families 1) · normal 40 · Greater 60 · Perfect 72. The six special families (Alacrity, Command, Grounding, Insulation, Opulence, Thawing) are drop level 1 at every tier in the export.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json `drop_level`, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data). poe2wiki shows Lesser Essence of the Body drop level 25 — agrees.
- Notes: The drop-level-1 entries are [INFERRED] to have other gating (area/content) rather than truly dropping from level 1.

## Families and what they add
- Claim:
  - Body — life (e.g. Lesser: +30–39 on armour/belt, +20–29 on jewellery; normal: +85–99 on belt/body/helmet/shield, +70–84 on amulet/boots/gloves/ring; Greater: +100–119 / +85–99; Perfect: body armour 8–10% increased max life).
  - Mind — mana. Enhancement — % armour/evasion/ES on armour.
  - Abrasion — flat physical on martial weapons. Flames / Electricity / Ice — flat fire / lightning / cold on martial weapons (Perfect Flames: 15–20% of damage as extra fire on 1H/bow).
  - Insulation / Thawing / Grounding / Ruin — fire / cold / lightning / chaos resistance on armour, belts, jewellery.
  - Infinite — attributes on any equipment. Opulence — item rarity on helmet/gloves/boots/jewellery.
  - Battle (attack), Sorcery (caster), Haste (speed), Seeking (crit, [INFERRED] from name), Command (minion), Alacrity (not sourced).
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Essence](https://www.poe2wiki.net/wiki/Essence), tier 2; [poe2db Essence](https://poe2db.tw/us/Essence), tier 2; [Mobalytics Essences](https://mobalytics.gg/poe-2/guides/essences), [Mobalytics Lolcohol essence guide](https://mobalytics.gg/poe-2/profile/lolcohol/guides/essence-guide-poe-2), [Mobalytics Paintmaster essence farm](https://mobalytics.gg/poe-2/guides/paintmasters-essence-farm), tier 3; [Poe-Vault](https://www.poe-vault.com/poe2/guides/currency-and-crafting), tier 3; retrieved 2026-11-17
- Confidence: confirmed for Body/Mind/Flames/resistances (wiki + poe2db + Mobalytics); others single tier-3
- Notes: Conflict on Ice — one Mobalytics table lists it as spell crit, others say cold damage. Logged in [[04-conflicts]]. Essence-only mods exist in data (`is_essence_only`), e.g. the Perfect Body life% mod is level 72 ([poe2wiki modifier page](https://www.poe2wiki.net/wiki/Modifier:EssenceIncreasedLifePercent1)).

## Corrupted essences
- Claim: Essence of Hysteria, Delirium, Horror, Insanity, the Abyss and the Breach — each removes a random mod from a rare and adds a guaranteed one (special lists per item type; Hysteria has a list of mods by equipment type per Mobalytics).
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json (`CurrencyCorruptedEssence*`), tier 2; [Mobalytics Paintmaster essence farm](https://mobalytics.gg/poe-2/guides/paintmasters-essence-farm), tier 3; retrieved 2026-11-17
- Confidence: single-source for effects per slot
- Notes: Exact mod lists per corrupted essence not yet captured — add in craft-costs (batch 9) if a target craft needs one.
