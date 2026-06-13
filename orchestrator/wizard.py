"""
Dark Strategist v3.10.0 — Interactive Wizard
Guided CLI for non-technical users. Walks the operator through domain, subscenario,
objective, regime, Tribunal and SSM, then SYNTHESIZES the exact argv that main.py
already understands. The wizard never re-implements pipeline logic: it builds the
flag list and main.py re-parses it through the same argparse parser.

Separation of concerns:
  build_command(answers)  -> pure, deterministic, unit-testable (no I/O).
  run_wizard()            -> interactive prompts + confirmation (the only I/O).
"""
from __future__ import annotations

#--- Domain -> canonical --type token. Each token resolves to the domain via
#--- catalogs.DOMAIN_MAP (verified). "general" falls through to General by design.
DOMAIN_CHOICES = [
    ("Trading",          "trading"),
    ("Legal",            "legal"),
    ("Financial",        "finance"),
    ("Cloud",            "cloud"),
    ("Code",             "code"),
    ("Cybersecurity",    "cyber"),
    ("Agriculture",      "agro"),
    ("Real Estate",      "real_estate"),
    ("Science",          "science"),
    ("Medical",          "medical"),
    ("Media",            "media"),
    ("E-Commerce",       "ecommerce"),
    ("Telecom",          "telecom"),
    ("Public Sector",    "public"),
    ("Marketing",        "marketing"),
    ("Operations",       "operations"),
    ("Human Resources",  "hr"),
    ("Strategy",         "strategy"),
    ("Startup",          "startup"),
    ("General",          "general"),
]

#--- Legal sub-area drill-down. Label + representative subscenario keyword
#--- (keyword is a catalogs.LEGAL_SUBAREA_MAP entry that also feeds the Legal Phase 0).
LEGAL_SUBAREAS = [
    ("L01 Commercial (NDA/MSA/SOW/SaaS)",        "nda"),
    ("L02 Corporate / M&A",                      "merger"),
    ("L03 Employment",                           "employment"),
    ("L04 Privacy (GDPR/DSAR/DPA)",              "gdpr"),
    ("L05 Product (ToS/EULA/Warranty)",          "terms of service"),
    ("L06 Regulatory",                           "regulatory filing"),
    ("L07 AI Governance",                        "ai governance"),
    ("L08 IP (Trademark/Patent/Copyright)",      "trademark"),
    ("L09 Litigation",                           "litigation"),
    ("L10 Real Estate Legal (Lease/Title)",      "lease"),
    ("L11 Finance Legal (Loan/Covenant)",        "loan agreement"),
    ("L12 Public Regulatory (Tender/RFP)",       "government contract"),
]

#--- Mirror of main.py argparse choices. Kept explicit so the wizard surfaces the
#--- full set without importing argparse internals.
REGIMES = ["standard", "adversarial", "breakout", "crisis",
           "regulatory", "fast_track", "comparative"]
AGENT_SIZES = [1, 3, 5, 7]
SSM_SCALES = ["MICRO", "MESO", "MACRO"]

DEFAULT_OBJECTIVE = "identify risks and failure modes"


def build_command(answers: dict) -> list:
    """Pure function: maps collected answers to the argv list main.py expects.

    answers keys:
      type (str, required)        subscenario (str, required)
      objective (str, required)   regime (str, required)
      tribunal (bool)             agents (int|None)  -> None = auto-size
      ssm (bool)                  ssm_scale (str)
      corpus (list[str]|None)     -> BYO per-case reference file paths (optional)
    """
    args = [
        "--type", answers["type"],
        "--subscenario", answers["subscenario"],
        "--objective", answers["objective"],
        "--regime", answers["regime"],
    ]
    if answers.get("tribunal"):
        args.append("--tribunal")
        agents = answers.get("agents")
        if agents in AGENT_SIZES:
            args += ["--agents", str(agents)]  #--- omit => auto-size by Swarm score
    if answers.get("ssm"):
        args.append("--ssm")
        args += ["--ssm-scale", answers.get("ssm_scale", "MESO")]
    corpus = answers.get("corpus") or []
    if corpus:
        args.append("--corpus")
        args += [str(p) for p in corpus]  #--- BYO per-case reference texts (any jurisdiction)
    signals = answers.get("signals") or []
    if signals:
        args.append("--signals")
        args += [str(p) for p in signals]  #--- BYO per-case external signals (time-sensitive evidence)
    return args


def format_command(args: list) -> str:
    """Renders argv as a copy-pasteable command, quoting tokens with spaces."""
    parts = ["python main.py"]
    for a in args:
        parts.append(f'"{a}"' if " " in a else a)
    return " ".join(parts)


#--- ── Interactive layer (I/O only) ───────────────────────────────────────────

def _ask_choice(title: str, options: list, default_index: int | None = None) -> int:
    """Prints a numbered menu and returns the chosen 0-based index."""
    print(f"\n{title}")
    for i, label in enumerate(options, 1):
        print(f"  {i}. {label}")
    suffix = f" [default {default_index + 1}]" if default_index is not None else ""
    while True:
        raw = input(f"Select{suffix}: ").strip()
        if not raw and default_index is not None:
            return default_index
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print("  ! Invalid selection, try again.")


def _ask_yes_no(question: str, default: bool = False) -> bool:
    d = "Y/n" if default else "y/N"
    while True:
        raw = input(f"{question} [{d}]: ").strip().lower()
        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  ! Please answer y or n.")


def _ask_text(question: str, default: str | None = None) -> str:
    suffix = f" [default: {default}]" if default else ""
    while True:
        raw = input(f"{question}{suffix}: ").strip()
        if raw:
            return raw
        if default is not None:
            return default
        print("  ! This field is required.")


def run_wizard() -> tuple:
    """Drives the interactive flow. Returns (argv_list, should_run)."""
    print("=" * 60)
    print("DARK STRATEGIST v3.21.0 — INTERACTIVE WIZARD")
    print("Answer the prompts; I'll build the command for you.")
    print("=" * 60)

    #--- 1. Domain -> --type
    d_idx = _ask_choice("DOMAIN:", [c[0] for c in DOMAIN_CHOICES])
    domain_label, type_token = DOMAIN_CHOICES[d_idx]

    #--- 2. Subscenario (Legal gets a sub-area drill-down)
    if type_token == "legal":
        s_idx = _ask_choice("LEGAL SUB-AREA:", [s[0] for s in LEGAL_SUBAREAS])
        suggested = LEGAL_SUBAREAS[s_idx][1]
        subscenario = _ask_text(
            "Subscenario (Enter to accept the sub-area keyword)", default=suggested)
    else:
        examples = {
            "trading": "XAUUSD", "finance": "investment_review",
            "code": "abap_module", "startup": "seed_pitch",
        }
        ex = examples.get(type_token, "describe_the_case")
        subscenario = _ask_text(f"Subscenario (e.g. {ex})")

    #--- 3. Objective
    objective = _ask_text("Objective", default=DEFAULT_OBJECTIVE)

    #--- 4. Regime
    r_idx = _ask_choice("REGIME:", REGIMES, default_index=0)
    regime = REGIMES[r_idx]

    #--- 5. Tribunal Transversal
    tribunal = _ask_yes_no("Activate Tribunal Transversal?", default=False)
    agents = None
    if tribunal:
        size_labels = ["Auto (Swarm Activation Score)"] + [str(n) for n in AGENT_SIZES]
        a_idx = _ask_choice("TRIBUNAL SIZE:", size_labels, default_index=0)
        agents = None if a_idx == 0 else AGENT_SIZES[a_idx - 1]

    #--- 6. SSM
    ssm = _ask_yes_no("Activate SSM (Simulacion Social Masiva)?", default=False)
    ssm_scale = "MESO"
    if ssm:
        sc_idx = _ask_choice("SSM SCALE:", SSM_SCALES, default_index=1)
        ssm_scale = SSM_SCALES[sc_idx]

    #--- 7. BYO per-case reference corpus (optional; any jurisdiction)
    corpus = []
    if _ask_yes_no("Attach reference texts (laws/standards) for grounding?", default=False):
        print("  Enter file paths one per line (.jsonl/.txt/.md or PDF/DOCX). Blank to finish.")
        while True:
            p = input("  path: ").strip()
            if not p:
                break
            corpus.append(p)

    #--- 8. BYO per-case external signals (optional; time-sensitive evidence)
    signals = []
    if _ask_yes_no("Attach external signals (news/data/reports) as evidence?", default=False):
        print("  Enter file paths one per line (.jsonl/.txt/.md or PDF/DOCX). Blank to finish.")
        while True:
            p = input("  path: ").strip()
            if not p:
                break
            signals.append(p)

    answers = {
        "type": type_token, "subscenario": subscenario, "objective": objective,
        "regime": regime, "tribunal": tribunal, "agents": agents,
        "ssm": ssm, "ssm_scale": ssm_scale, "corpus": corpus, "signals": signals,
    }
    argv = build_command(answers)

    print("\n" + "=" * 60)
    print(f"DOMAIN: {domain_label}  |  TYPE: {type_token}")
    print("EQUIVALENT COMMAND:")
    print(f"  {format_command(argv)}")
    print("=" * 60)

    should_run = _ask_yes_no("Run this analysis now?", default=True)
    return argv, should_run


if __name__ == "__main__":
    run_wizard()
