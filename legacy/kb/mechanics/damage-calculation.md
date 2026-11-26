# Damage Calculation (order of operations, increased vs more)

Status: done (0.5.x). Re-check at 1.0.
Main source: [poe2wiki Receiving damage](https://www.poe2wiki.net/wiki/Receiving_damage) (redirect target of "Damage_calculation"), tier 2, rev 133460, read via built-in browser 2026-11-25. The page carries a wiki banner: adapted from the PoE1 wiki, order of operations "may need to be re-tested". Treat order details as may-change.

## Increased/reduced add; more/less multiply
- Claim: All increased and reduced modifiers that apply to a piece of damage (including conditional ones) are summed into one multiplier. Each more/less modifier is a separate multiplier, multiplied against the others. Exception: repeats of one more/less stat from the same source add up first (e.g. "10% more per stage" at 5 stages = 50% more, not 1.1^5).
- Worked example (wiki): spell with fire + lightning, 50% inc fire, 30% inc lightning, 10% inc spell → fire ×1.6, lightning ×1.4.
- Version: 0.5.x
- Volatility: stable
- Source: poe2wiki Receiving damage, tier 2, 2026-11-25; [glama.ai attack-damage research](https://glama.ai/mcp/servers/@HivemindOverlord/poe2-mcp), tier 5 (agrees, lead only)
- Confidence: single-source (tier 2). [INFERRED] also consistent with every PoE2 support saying "X% more" as a separate line and with the KB's earlier kb-test maths.
- Notes: fills the gap flagged in [[builds/kb-test-frostbolt-chronomancer-damage-0.5.5]] (increased/more rule was [INFERRED] there).

## Outgoing hit order (attacker side)
1. **Flat damage** = base damage (weapon for attacks, gem for spells; unarmed and minions have their own) + all added damage. Min and max add separately per type.
2. **Conversion** in two steps: (a) skill conversion (from the gem, or a granted skill), then (b) global conversion (items, buffs, supports, passives). Regular conversion over 100% of a type is scaled down to 100% at each step. "Gain X% as extra" stacks additively within a step, multiplicatively across the two steps. Embitter-type supports act on both steps.
3. **Damage multipliers**: increased (summed) and more (each multiplied). Min/max-only modifiers (e.g. Heft's more max phys) apply after conversion.
4. **Crit**: multiply by crit damage bonus (default +100%). If the target could evade, evasion re-rolls here and can downgrade the crit to a normal hit.
5. **Roll** a value in the min–max range. Lucky = roll twice keep higher; unlucky = keep lower. Doesn't affect crit/ailment/block rolls.
6. **Double/triple damage** effects apply after all other offensive modifiers.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Receiving damage, tier 2, 2026-11-25
- Confidence: single-source; conversion detail agrees with [[mechanics/damage-types-conversion]].

## Incoming hit order (defender side)
1. **Avoid the hit**: manual dodge, dodge-roll avoidance frames, projectile avoidance, evasion. Only these stop on-hit effects entirely.
2. "Before being hit" effects (e.g. Defiance of Destiny).
3. Attacker's damage (steps above).
4. "Cannot take X damage" removes damage (not counted as prevented).
5. **Damage taken as** another type: all shifts at once, one shift only, not proportional past 100%. Shifted damage is mitigated only as its final type.
6. **Mitigation**: cannot-take again (counts as prevented) → immunities → damage avoidance → **damage reduction (armour, % phys DR) before resistances** (reverse of PoE1) → resistances (exposure and area penalties here; penetration after, floors at 0%).
7. **Damage taken modifiers**: flat first, then summed increased/reduced, then each more/less.
8. **Deflection** (after damage-taken modifiers; still counts for ailments).
9. **Stun / Pin / ailment buildup** rolled on damage at this point.
10. **Block** (full or partial, e.g. Turtle Charm). Doesn't stop stun or freeze. Since 0.4.0 blocked damage counts as "prevented".
11. **Resource loss**: redirection to minions (e.g. Loyalty) → buffs that absorb (Guard, Sorcery Ward) → ES → MoM-style mana share → life-loss prevention (Grasping Wounds: delayed over 4 s) → life. "Avoid death from hits" leaves you at 1 life; can't save you from DoT/life loss.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Receiving damage, tier 2, 2026-11-25
- Confidence: single-source (wiki itself says re-test)
- Notes: chaos removes 2× ES and is applied to ES first when mixed; bleed and poison bypass ES ([[mechanics/energy-shield]], [[mechanics/hits-vs-dot]]). Deflection placement matters for [[mechanics/deflection]]; block placement matters for [[mechanics/block]].

## Damage over time
- Claim: DoT follows the same rules but never hits, so evasion/armour/block don't apply. DoT ticks at the start of each server frame, after over-time recovery and before hits. Ailments from a hit take a % of the hit's pre-mitigation damage, scaled only by ailment magnitude (no second damage-mod dip), then get mitigated on their own.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Receiving damage, tier 2, 2026-11-25
- Confidence: confirmed (matches game keywords in [[mechanics/hits-vs-dot]] and the resolved conflict "Do damage modifiers apply to ailments after the hit?")

## Weapon-local modifiers
- Claim: Local "% increased Physical Damage" on a martial weapon multiplies the weapon's base phys (after local flat added phys) — it isn't pooled with global increased damage. Several local sources (e.g. Iron Rune) add together. Still works if the phys is later converted. Local % attack speed and local crit bonus are likewise multiplicative with global sources.
- Example (wiki): base 50–100 + adds 25–50 + 100% local inc → 150–300 phys.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Modifier](https://www.poe2wiki.net/wiki/Modifier), tier 2, rev 135639, 2026-11-25
- Confidence: single-source
