---
title: Defensive Layering Checklist
status: done
tracker_topic: "Defensive layering checklist"
tracker_note: "done (0.5.5.9 mechanics; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: built from the 0.5.5.9 mechanics docs + 0.5.x guides (researched 2026-11-17). Every number points at its mechanics doc; re-check those at 1.0 (passive tree rebuilt, ailments reworked).
Use: run it at each map-tier checkpoint ([[strategy/league-start-framework]]) and as gate 1 in claude/starter-decision-sheet.md.

## 1. Resistances
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Cap fire, cold and lightning at 75%. After the full campaign penalty (−60% in 0.5) that means ~135% uncapped per element. Each point near the cap matters most: 50% resistance takes double the damage of 75%.
- Check: all three at 75% after each act's penalty; overcap as a buffer vs curses/exposure.

- src: [[mechanics/resistances]] (poe2wiki, game keywords, tier 2); Maxroll Comprehensive League Start Leveling Guide [S032] (50% vs 75% = double damage), tier 3; retrieved 2026-11-17
- vol: may-change — penalty total changes with 1.0's Acts 5–6
- conf: confirmed; 135% is [INFERRED] arithmetic

## 2. Chaos resistance
@ v=0.5.5 vol=may-change conf=confirmed date=2026-11-17
Chaos also caps at 75%. Chaos removes double its value from energy shield. One 0.5.5 endgame guide targets 30–50% chaos res.
- Check: positive chaos res before red maps; higher for ES builds.

- src: [[mechanics/resistances]], [[mechanics/energy-shield]] (game data, tier 2); Mobalytics Fubgun Ice Shot Deadeye [S045] (30–50% target), tier 3; retrieved 2026-11-17
- conf: confirmed (mechanics); single-source (target)

## 3. Pool size (life / ES)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Life and ES are the buffer every other layer protects. Your stun threshold equals max life, so a small pool also means more stuns.
- Check: pool grows with each tier; ES builds also watch the 4 s recharge delay (12.5%/s after).

- src: [[mechanics/stun]], [[mechanics/energy-shield]] (game keywords, tier 2), retrieved 2026-11-17
- conf: single-source (game data)

## 4. One primary mitigation layer, matched to your attribute
@ v=0.5 vol=may-change conf=inferred date=2026-11-17
Pick the layer your class's tree side supports — Str → armour, Dex → evasion + deflection, Int → energy shield — and invest in it consistently.
- What each layer does / doesn't do:
  - Armour: strong vs small physical hits, weak vs big ones, nothing vs DoT. Also slows you (body armour/shield). → [[mechanics/armour]]
  - Evasion: avoids attack hits, entropy-based (no bad streaks), 95% cap; doesn't stop red-flash boss attacks or DoT; useless while heavily stunned. → [[mechanics/evasion]]
  - Deflection: mostly from "% of evasion" mods; deflected hits lose 40%; works vs red-flash attacks. Cap disputed (conflicts doc). → [[mechanics/deflection]]
  - Energy shield: absorbs before life; bleed and poison bypass it; chaos does double. → [[mechanics/energy-shield]]

- src: Switchblade Gaming HC guide [S736] (0.5), tier 5; matches attribute/defence alignment in [[items/bases-implicits]]; retrieved 2026-11-17
- conf: [INFERRED] as a rule (tier 5 + game-data alignment)

## 5. Recovery
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Mitigation buys time; recovery refills. Leech: one instance per resource, hits only, stops when full. Recoup: % of damage taken back over 8 s. ES recharge after 4 s. Flasks and checkpoints refill.
- Check: at least one recovery source that works mid-fight without pressing a button.

- src: [[mechanics/recovery]], [[mechanics/flasks]] (game keywords, tier 2), retrieved 2026-11-17
- conf: single-source (game data)

## 6. Avoidance extras (block, dodge roll)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Block negates a hit but you still take its stun; default max 50%; some boss skills (red glow) can't be blocked. Raising a shield builds heavy-stun buildup. Dodge roll is always available.

- src: [[mechanics/block]], [[mechanics/dodge-roll]] (game keywords, poe2wiki, tier 2), retrieved 2026-11-17
- conf: confirmed (50% cap); single-source otherwise

## 7. Stun and ailments
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
A hit at or above your max life always stuns you. Heavily stunned players can't block, deflect or evade. Maxroll recommends a Stone Charm against repeated stuns while levelling. Charms trigger on ailments/conditions ([[mechanics/charms]]).
- Check: freeze/stun answer by red maps (charm, "can't be" effects, enough life).

- src: [[mechanics/stun]] (game keywords, tier 2); Maxroll Comprehensive League Start Leveling Guide [S032], tier 3; claude/reveal-notes-and-price-findings.md; retrieved 2026-11-17
- v: 0.5.5.9 / 0.2 (charm advice)
- vol: may-change — 1.0 reveal notes say ailments become harder to apply but stronger (secondhand)
- conf: single-source each

## 8. DoT blind spots
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Armour, evasion, deflection and block only act on hits. Bleed and poison skip ES. Life loss isn't damage, so mitigation doesn't stop it.
- Check: chaos/ele res + regen or flask removal cover DoT.

- src: [[mechanics/armour]], [[mechanics/energy-shield]], [[mechanics/recovery]] (game keywords, tier 2), retrieved 2026-11-17
- conf: confirmed (armour, ES); evasion/block vs DoT [INFERRED] from "hits" wording

## Quick pass order (when something feels bad)
Order from guides [INFERRED where noted]: (1) resists capped → (2) movement speed and pool → (3) one primary layer → (4) recovery → (5) stun/freeze answer → (6) chaos res → (7) extras. Maxroll's levelling stat priority (movement speed > resists > life > damage > defences) agrees on the first three steps; the rest is my ordering [INFERRED] from what each layer covers.

## Death-recap habit
- 1.0 adds a death summary screen (reveal notes, secondhand). Use it to name the missing layer instead of guessing → re-check at 1.0.
