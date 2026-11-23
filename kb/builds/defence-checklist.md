# Defensive Layering Checklist

Version: built from the 0.5.5.9 mechanics docs + 0.5.x guides (researched 2026-11-17). Every number points at its mechanics doc; re-check those at 1.0 (passive tree rebuilt, ailments reworked).
Use: run it at each map-tier checkpoint ([[strategy/league-start-framework]]) and as gate 1 in claude/starter-decision-sheet.md.

## 1. Resistances
- Claim: Cap fire, cold and lightning at 75%. After the full campaign penalty (−60% in 0.5) that means ~135% uncapped per element. Each point near the cap matters most: 50% resistance takes double the damage of 75%.
- Version: 0.5.x
- Volatility: may-change — penalty total changes with 1.0's Acts 5–6
- Source: [[mechanics/resistances]] (poe2wiki, game keywords, tier 2); [Maxroll Comprehensive League Start Leveling Guide](https://maxroll.gg/poe2/getting-started/comprehensive-league-start-leveling-guide) (50% vs 75% = double damage), tier 3; retrieved 2026-11-17
- Confidence: confirmed; 135% is [INFERRED] arithmetic
- Check: all three at 75% after each act's penalty; overcap as a buffer vs curses/exposure.

## 2. Chaos resistance
- Claim: Chaos also caps at 75%. Chaos removes double its value from energy shield. One 0.5.5 endgame guide targets 30–50% chaos res.
- Version: 0.5.5
- Volatility: may-change
- Source: [[mechanics/resistances]], [[mechanics/energy-shield]] (game data, tier 2); [Mobalytics Fubgun Ice Shot Deadeye](https://mobalytics.gg/poe-2/builds/ice-shot-deadeye) (30–50% target), tier 3; retrieved 2026-11-17
- Confidence: confirmed (mechanics); single-source (target)
- Check: positive chaos res before red maps; higher for ES builds.

## 3. Pool size (life / ES)
- Claim: Life and ES are the buffer every other layer protects. Your stun threshold equals max life, so a small pool also means more stuns.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [[mechanics/stun]], [[mechanics/energy-shield]] (game keywords, tier 2), retrieved 2026-11-17
- Confidence: single-source (game data)
- Check: pool grows with each tier; ES builds also watch the 4 s recharge delay (12.5%/s after).

## 4. One primary mitigation layer, matched to your attribute
- Claim: Pick the layer your class's tree side supports — Str → armour, Dex → evasion + deflection, Int → energy shield — and invest in it consistently.
- Version: 0.5
- Volatility: may-change
- Source: [Switchblade Gaming HC guide](https://www.switchbladegaming.com/path-of-exile-2/hardcore-guide/) (0.5), tier 5; matches attribute/defence alignment in [[items/bases-implicits]]; retrieved 2026-11-17
- Confidence: [INFERRED] as a rule (tier 5 + game-data alignment)
- What each layer does / doesn't do:
  - Armour: strong vs small physical hits, weak vs big ones, nothing vs DoT. Also slows you (body armour/shield). → [[mechanics/armour]]
  - Evasion: avoids attack hits, entropy-based (no bad streaks), 95% cap; doesn't stop red-flash boss attacks or DoT; useless while heavily stunned. → [[mechanics/evasion]]
  - Deflection: mostly from "% of evasion" mods; deflected hits lose 40%; works vs red-flash attacks. Cap disputed (conflicts doc). → [[mechanics/deflection]]
  - Energy shield: absorbs before life; bleed and poison bypass it; chaos does double. → [[mechanics/energy-shield]]

## 5. Recovery
- Claim: Mitigation buys time; recovery refills. Leech: one instance per resource, hits only, stops when full. Recoup: % of damage taken back over 8 s. ES recharge after 4 s. Flasks and checkpoints refill.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [[mechanics/recovery]], [[mechanics/flasks]] (game keywords, tier 2), retrieved 2026-11-17
- Confidence: single-source (game data)
- Check: at least one recovery source that works mid-fight without pressing a button.

## 6. Avoidance extras (block, dodge roll)
- Claim: Block negates a hit but you still take its stun; default max 50%; some boss skills (red glow) can't be blocked. Raising a shield builds heavy-stun buildup. Dodge roll is always available.
- Version: 0.5.x
- Volatility: may-change
- Source: [[mechanics/block]], [[mechanics/dodge-roll]] (game keywords, poe2wiki, tier 2), retrieved 2026-11-17
- Confidence: confirmed (50% cap); single-source otherwise

## 7. Stun and ailments
- Claim: A hit at or above your max life always stuns you. Heavily stunned players can't block, deflect or evade. Maxroll recommends a Stone Charm against repeated stuns while levelling. Charms trigger on ailments/conditions ([[mechanics/charms]]).
- Version: 0.5.5.9 / 0.2 (charm advice)
- Volatility: may-change — 1.0 reveal notes say ailments become harder to apply but stronger (secondhand)
- Source: [[mechanics/stun]] (game keywords, tier 2); [Maxroll Comprehensive League Start Leveling Guide](https://maxroll.gg/poe2/getting-started/comprehensive-league-start-leveling-guide), tier 3; claude/reveal-notes-and-price-findings.md; retrieved 2026-11-17
- Confidence: single-source each
- Check: freeze/stun answer by red maps (charm, "can't be" effects, enough life).

## 8. DoT blind spots
- Claim: Armour, evasion, deflection and block only act on hits. Bleed and poison skip ES. Life loss isn't damage, so mitigation doesn't stop it.
- Version: 0.5.5.9
- Volatility: stable
- Source: [[mechanics/armour]], [[mechanics/energy-shield]], [[mechanics/recovery]] (game keywords, tier 2), retrieved 2026-11-17
- Confidence: confirmed (armour, ES); evasion/block vs DoT [INFERRED] from "hits" wording
- Check: chaos/ele res + regen or flask removal cover DoT.

## Quick pass order (when something feels bad)
Order from guides [INFERRED where noted]: (1) resists capped → (2) movement speed and pool → (3) one primary layer → (4) recovery → (5) stun/freeze answer → (6) chaos res → (7) extras. Maxroll's levelling stat priority (movement speed > resists > life > damage > defences) agrees on the first three steps; the rest is my ordering [INFERRED] from what each layer covers.

## Death-recap habit
- 1.0 adds a death summary screen (reveal notes, secondhand). Use it to name the missing layer instead of guessing → re-check at 1.0.
