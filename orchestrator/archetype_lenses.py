"""
Dark Strategist -- Archetype Lenses (P2)

Structured adversarial perspectives that enrich the P1 confidence-gated escalation
round (TribunalTransversal._run_escalation_round). Each lens is an ABSTRACT scrutiny
angle -- never an impersonation of a real person (fabricated authority is forbidden by
design). Lenses are pure data + pure functions: no API calls, deterministic, testable.

Plugs into the existing Forense layer (NO new agent type). During an escalation round
each FOR-ESC-* agent is assigned one lens; the lens shapes HOW it re-examines the
verdict-driving findings, producing diverse independent angles that strengthen (or
honestly fail to strengthen) cross-agent corroboration.

NON-BINDING: lenses change deliberation quality, never the severity-driven verdict.

Module docstring + catalog are content-based/frozen (do NOT bump every minor; only when
the catalog content itself changes).
"""

#--- Frozen catalog. Order is significant: the first entries form the highest-value
#--- complementary pair (refute-first + extend-first), because max_escalation_agents
#--- defaults to 2. Abstract roles only -- NO real persons, NO fabricated authority.
ARCHETYPE_LENSES = (
    {
        "id": "FALSIFIER",
        "label": "The Falsifier",
        "angle": ("Adopt a refutation-first stance. Actively try to DISPROVE each "
                  "verdict-driving finding: steelman the document against it, surface the "
                  "strongest counter-evidence, and state whether the finding survives. "
                  "Corroborate a finding ONLY if it withstands disproof."),
    },
    {
        "id": "FAILURE_MODE_HUNTER",
        "label": "The Failure-Mode Hunter",
        "angle": ("Assume the panel UNDERSTATED risk. Hunt for additional failure modes, "
                  "second-order effects, and edge cases tied to the verdict-driving findings "
                  "that the first pass missed. Report new findings with concrete evidence."),
    },
    {
        "id": "EVIDENCE_AUDITOR",
        "label": "The Evidence Auditor",
        "angle": ("Challenge the evidentiary chain. For each verdict-driving finding demand "
                  "the document evidence that backs it and flag any claim resting on "
                  "assumption, correlation-as-causation, or invented metrics (e.g. "
                  "'consensus implies efficiency'). Downgrade unsupported claims."),
    },
    {
        "id": "INCENTIVE_AUDITOR",
        "label": "The Incentive Auditor",
        "angle": ("Examine incentives and adversarial actors. Ask who benefits from the "
                  "claims under scrutiny, where incentives are misaligned, and how the "
                  "proposal could be gamed or captured. Tie every finding to evidence."),
    },
    {
        "id": "SYSTEMIC_LENS",
        "label": "The Systemic Lens",
        "angle": ("Take a systemic, second-order view. Examine interactions, externalities, "
                  "and downstream consequences beyond each finding's immediate scope. "
                  "Surface emergent risks with evidence."),
    },
)


def select_lenses(n):
    """Deterministically select the first n archetype lenses, capped at catalog size.

    Pure. Returns independent dict copies (mutating a returned lens never corrupts the
    frozen catalog). n<=0 / None / non-numeric -> empty list.
    """
    if n is None:
        return []
    try:
        n = int(n)
    except (TypeError, ValueError):
        return []
    if n <= 0:
        return []
    return [dict(lens) for lens in ARCHETYPE_LENSES[:n]]


def build_lens_directive(lens, round_no, focus):
    """Compose the full escalation directive for a single lens. Pure.

    `focus` is the pipe-joined titles of the verdict-driving findings. Tolerates a
    None/empty lens (falls back to a neutral adversarial reviewer) and empty focus.
    """
    lens = lens or {}
    angle = lens.get("angle", ("Independently re-examine the verdict-driving findings and "
                               "corroborate or refute them with evidence."))
    label = lens.get("label", "Adversarial reviewer")
    try:
        round_no = int(round_no)
    except (TypeError, ValueError):
        round_no = 1
    return ("ESCALATION ROUND %d -- LENS: %s. Confidence is LOW. %s "
            "Verdict-driving findings under scrutiny: %s"
            % (round_no, label, angle, focus or "low-corroboration verdict"))
