# Desecration & abyssal bones

Scope: desecrated mods, bones, Well of Souls, Abyssal lords' mods. Abyss encounters themselves → [[abyss]] (batch 14). Version 0.5.x unless noted.

## What desecration does
- Claim: Desecrating an item adds one unrevealed desecrated mod (removing a random mod if the item is full). An item with a desecrated mod can't be desecrated again. You reveal it at the Well of Souls and choose one of three offered mods.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE poe2 keywords.json "Desecrated Modifiers", tier 2 (game data); [poe2wiki Abyss](https://www.poe2wiki.net/wiki/Abyss), tier 2; [Mobalytics Lolcohol abyss crafting](https://mobalytics.gg/poe-2/profile/lolcohol/guides/abyss-and-desecration-crafting-poe-2-0-3), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: The wiki says an offered mod is sometimes one that can't normally roll on that item. Omen of Abyssal Echoes lets you reroll the three options once ([[omens]]). Omen of Light makes the next Annulment remove only desecrated mods — the way to redo a bad reveal [INFERRED from omen text].

## Well of Souls
- Claim: Unlocked in Act 2 — the quest starts on entering the Mastodon Badlands; clear the Lightless Passage to reach it. Afterwards it's reachable from the map screen.
- Version: 0.3+ (0.5.x)
- Volatility: may-change (1.0 campaign changes)
- Source: [poe2wiki The Well of Souls (quest)](https://www.poe2wiki.net/wiki/The_Well_of_Souls_(quest)), tier 2; [Poe-Vault Rise of the Abyssal guide](https://www.poe-vault.com/poe2/guides/rise-of-the-abyssal-league-guide), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Optional quest — decide whether the skip route takes it. → strategy/skip-route.

## Bones (game data)
- Claim: Collarbone = rare amulet, ring or belt · Jawbone = rare weapon or quiver · Rib = rare armour · Cranium = rare jewel · Vertebrae = rare waystone. Tiers by drop level: Gnawed 25 (collarbone, jawbone, rib) · Preserved 61 (+ Cranium and Vertebrae at 65) · Ancient 75. Altered Collarbone: jewellery with a chance for "otherworldly" mods (Breach-linked).
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) (`AbyssalBenchTicket*`), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Gnawed bones reportedly work only up to item level 64 and can't roll lord mods (timesaver.gg, tier 5 — RMT-adjacent, lead only). Tiers set mod level and max item level (vulkk, tier 5). Verify bone min mod level / max ilvl in game.

## Abyssal lords' mods
- Claim: Endgame desecration can offer mods tied to three Abyssal liches — Amanamu, Ulaman, Kurgal (e.g. "Amanamu's" prefixes at mod level 65 such as increased armour from equipped body armour on amulets). Omens of the Liege / Sovereign / Blackblooded force Amanamu / Ulaman / Kurgal mods on weapon or jewellery desecration.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Desecrated modifier](https://www.poe2wiki.net/wiki/Desecrated_mod), [poe2wiki Omen of the Sovereign](https://www.poe2wiki.net/wiki/Omen_of_the_Sovereign), tier 2; [Mobalytics Abyss crafting](https://mobalytics.gg/poe-2/guides/abyss-crafting), tier 3; RePoE base_items.json omen text; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Each lord can be fought for targeted rolls via Kulemak's Invitation at the Well (Poe-Vault, tier 3). Jewels' desecrated mods ("Lightless"/"of the Abyss") don't work with lord omens (wiki). Unstable Desecration (Timeless Jewels etc.): desecrate with Preserved Cranium, rising destroy chance per use (keyword).
