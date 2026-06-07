---
name: reputational-risk
version: 1.0.0
description: Forensic lens for diagnosing reputational risk in public-facing claims, brand positioning, strategic commitments, and stakeholder-facing decisions under audit. Five predictable patterns (misrepresentation/over-claim, broken-promise, stakeholder-betrayal, association-contamination, silence-in-crisis) with detection signals. Activates in Media (P11), Marketing (P16), and Strategy (P19) when the audited document makes a public claim, a public commitment, or a decision whose foreseeable second-order effect is loss of trust, credibility, or standing with an audience, customer base, partner, or the public. Detection lens; severity bound by the variant Failure Catalog, never alters the verdict.
origin: original — Dark Strategist native forensic lens (v3.16.0)
---

# Reputational Risk - Forensic Lens
# Skill for Dark Strategist - Technical Specification
# Location: skills/reputational-risk/SKILL.md

---

## Purpose

Equip Dark Strategist to audit reputational risk as a measurable forensic failure mode - not a vague "PR concern" - when the document under audit makes a public-facing claim, a public commitment, or a decision whose foreseeable effect is the erosion or destruction of trust with an audience, customer base, partner, regulator, or the public. Reputational damage is not random: it manifests through five distinct, predictable patterns, each with detection signals. This skill supplies the forensic vocabulary; the P11 (Media), P16 (Marketing), and P19 (Strategy) variants supply the auto-severity Failure Catalog rows that bind findings to the verdict.

This skill does NOT modify the deterministic verdict, severity taxonomy, or Rule 09. It is a detection lens, not a verdict driver. Reputational findings carry severity ONLY through the variant Failure Catalog - and from there feed the deterministic monotonic verdict table like any other finding. The lens itself computes nothing.

---

## The Five Reputational Risk Patterns

### 1. Misrepresentation / Over-claim
A public claim exceeds what the proponent can substantiate: inflated superlatives, greenwashing, unverifiable "best/first/only" assertions, performance promises without evidence.
Detection: claims stated as fact without traceable support; comparative or absolute superlatives ("the safest", "100% secure", "carbon-neutral") with no cited basis; benefit framing that omits material conditions.
Audit signal: marketing or positioning copy asserting outcomes the underlying mechanism cannot guarantee; claim survivability not testable against declared data.
Cross-link: distinct from a factual error (UNIT-FACTCHECK) - here the risk is the public, attributable exposure created by asserting it at scale.

### 2. Broken-promise
A commitment made publicly is later reversed or quietly abandoned: pricing guarantees, policy pledges, stated values, roadmap commitments.
Detection: a current decision contradicts a prior public commitment; "temporary" reversals with no sunset; value statements unsupported by the mechanism that would honor them.
Audit signal: the document reverses or hollows out a previously published promise without acknowledging the trust cost or a migration path for those who relied on it.

### 3. Stakeholder-betrayal
The proposal benefits the proponent at the visible expense of a stakeholder who extended trust: customers, employees, community, partners.
Detection: value capture that transfers cost or risk onto a trusting party; asymmetry between who decides and who bears the downside; silent change to terms relied upon.
Audit signal: a mechanism whose upside accrues to the proponent while a foreseeable, attributable harm lands on a named stakeholder group - and the document does not disclose or mitigate it.

### 4. Association-contamination
Reputational risk inherited from who or what the proponent is tied to: partners, endorsers, channels, funding sources, supply chain, platform.
Detection: dependence on an entity carrying its own reputational liability; endorsement or co-branding with an unvetted party; funding/affiliation that conflicts with the stated public position.
Audit signal: the plan binds the proponent's standing to a third party whose conduct it neither controls nor screens, with no contingency for that party's reputational failure.

### 5. Silence-in-crisis
No credible response capability for a foreseeable reputational hit: no crisis-comms plan, no escalation path, no designated owner, no holding position.
Detection: a foreseeable adverse event (data breach, recall, public allegation, partner scandal) with no documented response; reliance on "we'll handle it if it happens".
Audit signal: the document identifies or implies an exposure but contains no detection-to-response mechanism - the vacuum is filled adversarially by the fastest, most hostile narrative.

---

## Exposure Containment (reference, not mandate)

| Lever | Action | Apply when |
|-------|--------|-----------|
| Substantiate | Bind every public claim to traceable evidence before it ships | over-claim symptoms |
| Honor-or-disclose | Keep the public commitment, or disclose the reversal with a migration path | broken-promise symptoms |
| Realign | Remove the asymmetry, or disclose and compensate the bearing stakeholder | stakeholder-betrayal symptoms |
| Screen | Vet and contingency-plan around every reputational dependency | association-contamination symptoms |
| Pre-stage | Designate owner + holding position + escalation path before the event | silence-in-crisis symptoms |

These are audit reference levers, not a scoring rubric. Severity is bound by the Failure Catalog, never by this table.

---

## Integration with Dark Strategist

### Activation
- P11 Media - when the audited document involves content, brand, audience, sponsorships, or platform/partner associations. Angle: association-contamination, over-claim, silence-in-crisis (prefix M).
- P16 Marketing - when the audited document makes public-facing claims, brand positioning, or campaign promises. Angle: misrepresentation/over-claim, broken-promise (prefix MK).
- P19 Strategy - when the strategy carries public commitments, partnerships, stakeholder trade-offs, or moves with foreseeable public backlash. Angle: stakeholder-betrayal, association-contamination, silence-in-crisis (prefix ST).

Scope note: v1.0.0 binds in P11/P16/P19 only. Public Sector (P14) and Startup (P20) are candidate extensions for a later version and are NOT active here - the lens does not fire where no Failure Catalog rows exist to bind severity.

### Failure Catalog binding
Severity is assigned ONLY by the P11/P16/P19 Failure Catalog rows, consistent with each variant's Severity Taxonomy. This skill names and detects; the catalog binds. Rule 09 applies: a LATENT reputational risk that triggers systemic collapse at Level 7 escalates to FATAL.

### With the AFO
The lens is outward-facing (audits the document's public exposure); it does not interact with orchestration internals. It produces findings; the Tribunal consolidates them; the deterministic table computes the verdict.

---

## Limits
- Detection lens only - does not modify verdict, severity taxonomy, or Rule 09.
- No fabrication: a pattern is reported only when a concrete signal is present in the document. No assumed scandals, no speculative outrage.
- Not a sentiment oracle: this lens audits structural reputational exposure, not predicted public mood.
- Severity bound exclusively by the variant Failure Catalog - never by this file.

---

## System Prompt Integration Block

```
[SKILL: REPUTATIONAL RISK - REFERENCE LENS]

When auditing a public claim, public commitment, or stakeholder-facing decision (P11,
P16, or P19), screen for the five reputational patterns:
- misrepresentation/over-claim (unsubstantiated public claim, superlative without basis)
- broken-promise (public commitment reversed/hollowed without disclosure or migration path)
- stakeholder-betrayal (proponent upside, foreseeable attributable harm to a trusting party)
- association-contamination (standing bound to an unvetted/uncontrolled third party)
- silence-in-crisis (foreseeable reputational hit with no detection-to-response mechanism)
For each detected pattern: name it, quote the triggering element, state the exposure.
Bind severity via the P11/P16/P19 Failure Catalog only. Do NOT alter the deterministic verdict.
Report only on a concrete signal present in the document - no speculative outrage.
```

---

```
[SKILL_STATUS: ACTIVE - v1.0.0]
[INTEGRATED_WITH: P11 Media | P16 Marketing | P19 Strategy]
[ORIGIN: original - Dark Strategist native forensic lens]
[VERDICT_IMPACT: NONE - detection lens, severity bound by Failure Catalog]
```
