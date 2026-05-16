# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.0.0] — 2026-05-14

### Major Release — Tribunal Transversal + Dynamic Prompts + Structured Output

This release is the most significant architectural evolution of Dark Strategist. It introduces the Tribunal Transversal (two-layer agent architecture), dynamic prompt generation (replacing 15 static files), Pydantic structured output (replacing free-text parsing), the `regime` field for environment calibration, and the Medical domain.

---

#### Core Architecture Change — Tribunal Transversal

**v2.x (Tribunal Adversarial):**
```
Agentes Forenses → read document directly → produce findings
```

**v3.0 (Tribunal Transversal):**
```
Layer 1: Agentes de Rol    → simulate the domain environment
Layer 2: Agentes Forenses  → audit the simulation + document
AFO: synthesizes both layers → UnifiedVerdictOutput
```

The key distinction: in v3.0, all agents belong to the domain, but serve different functions. Rol agents simulate stakeholders; Forense agents audit the quality and veracity of what emerges from that simulation.

---

#### New Files

1. **`orchestrator/catalogs.py`** — ROLE_CATALOG (15 domains × Rol + Forense agents), SSM_CATALOG (15 domains × personas), DOMAIN_MAP (keyword → domain), REGIME_MAP (6 regimes with calibration), DOMAIN_TOOLS (15 domains × tools). Single source of truth for all domain knowledge.

2. **`orchestrator/schema.py`** — Pydantic models: Finding, AgentVerdictOutput, UnifiedVerdictOutput, RuntimeContext. Structured output replaces free-text parsing. Enables programmatic comparison of tribunal agent verdicts.

3. **`orchestrator/prompt_engine.py`** — PromptEngine with master templates: MASTER_TEMPLATE (Forense agents), ROLE_AGENT_TEMPLATE (Rol agents), SYNTHESIS_TEMPLATE (AFO synthesis). Dynamic prompt building from RuntimeContext — no static files required.

4. **`orchestrator/context_builder.py`** — ContextBuilder. Validates case dict, resolves domain from type + subscenario keywords, assigns Rol/Forense agents, SSM personas, tools, and regime description. Single entry point for runtime context.

5. **`orchestrator/tribunal_transversal.py`** — TribunalTransversal class (replaces tribunal.py for v3.0 cases). Two-layer execution: _run_rol_layer() (parallel, blind) → _run_forense_layer() (audits simulation) → _synthesize() → SSM → Transparency Report.

6. **`prompts/system_prompt_medical.md`** — Medical / Clinical domain variant. UNIT-INQUISITOR + UNIT-QUANT co-primary. Covers clinical protocols, regulatory submissions, healthcare business plans, informed consent, clinical trial design. RULE MD1-MD4.

---

#### Key Concepts Introduced

**Regime:** A new field that calibrates analysis intensity and framing before any agent runs.
| Regime | Description |
|--------|-------------|
| standard | Balanced perspective — default |
| adversarial | Maximum pressure — assume worst case |
| breakout | High volatility / trend conditions |
| crisis | Capital preservation priority |
| regulatory | Compliance-first lens |
| fast_track | Rapid assessment — 4 levels |
| comparative | N≥2 solutions — cross-evaluation |

**Dynamic Prompts:** The PromptEngine builds prompts at runtime from the master template + RuntimeContext. Adding a new domain requires only a new entry in catalogs.py — no new .md file.

**VerdictOutput (Pydantic):** Every agent now returns a structured, validated JSON output. The AFO synthesizer can programmatically compare verdicts, count severities, and detect conflicts without parsing text.

**Medical Domain:** New domain with 7 document types, 11-item failure catalog, 4 domain rules (RULE MD1-MD4), and domain-specific War Room orchestration.

---

#### Updated Files

- **`orchestrator/main.py`** — New v3.0 CLI: `--type`, `--subscenario`, `--objective`, `--regime`. v2.x `--document` flag preserved for backward compatibility.
- **`orchestrator/config.example.json`** — max_calls_total increased to 40 (two layers)
- **`orchestrator/router.md`** — Medical domain added to catalog (P15)

---

#### CLI Reference v3.0.0

```bash
# v3.0 case-based (recommended)
python main.py --type contract --subscenario alquiler --objective "identify risks" --regime adversarial

# With Tribunal Transversal
python main.py --type finance --subscenario investment_review --objective "evaluate viability" --tribunal

# With SSM
python main.py --type medical --subscenario clinical_review --objective "protocol risks" --tribunal --ssm

# Full pipeline
python main.py --type trading --subscenario XAUUSD --objective "buy sell wait" --regime breakout --tribunal --ssm --ssm-scale MACRO

# v2.x compatibility
python main.py --document doc.txt --tribunal --ssm
```

---

#### Backward Compatibility

v2.9.0 files are preserved:
- `tribunal.py` — still functional for `--document` mode
- All 15 `prompts/system_prompt_*.md` — still used as fallback
- All SSM module files — unchanged
- All notification/logging infrastructure — unchanged

---

#### Pending — v3.0 Roadmap

- [ ] Update `system_prompt_router.md` with Medical domain (P15)
- [ ] example_04 — COMPARATIVE MODE with Tribunal Transversal
- [ ] example_05 — OPTIMIZATION MODE with SSM
- [ ] Looker Studio dashboard template
- [ ] Cloud Function update for v3.0 case-based API

---

## [2.9.0] — 2026-05-13

SSM (Simulación Social Masiva) + Transparency Report. 4-round interaction engine.
MICRO/MESO/MACRO scales. SSM activation logic by verdict.

---

## [2.8.0] — 2026-05-13

AFO + Tribunal Adversarial. Budget Controller. Sub-Agent Spawner. Verdict Synthesizer.

---

## [2.7.0] — 2026-05-12

Autonomous Router + 11 Domain Prompts + Python Infrastructure.

---

## [2.6.1] — 2026-05-06

Trading + Legal domain variants.

---

## [2.6.0] — 2026-05-05

SAT Intelligence Doctrine + KAC + ACH + Deception Detection + Verdict Verification.

---

## [2.5.x] — 2026-04-25

MVP_THRESHOLD | Operational Modes | COMPARATIVE | OPTIMIZATION | FAST_TRACK | UNIT-PSYCH.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, Blocks 0–6.
