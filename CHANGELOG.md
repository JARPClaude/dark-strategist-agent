# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.1.0] — 2026-05-15

### Major Release — GOAP A* Planner + Legal Taxonomy (12 Sub-areas)

#### 1. GOAP A* Planner — Dynamic AFO Planning

**`orchestrator/goap_planner.py`** — Replaces the fixed Swarm Activation Score with Goal-Oriented Action Planning using A* search.

**Why:** The Swarm Activation Score was rigid — "IF INVIABLE → 5 agents" regardless of domain, budget, or regime. The GOAP planner evaluates the full planning space and finds the optimal action sequence given all constraints simultaneously.

**How it works:**
- `WorldState` — represents current audit state (domain, verdict, agents deployed, budget remaining)
- `GoalState` — defines what a successful audit looks like (synthesis_done, ssm_required)
- `Action` — each possible step (INITIAL_AUDIT, ROL_LAYER_STANDARD, FORENSE_LAYER_FULL, SSM_MESO, etc.)
- A* search — finds minimum-cost path from current state to goal state
- `heuristic()` — admissible estimate of remaining cost (never overestimates → optimal plan guaranteed)

**Fixed vs GOAP comparison:**
```
Fixed (v2.x):  IF verdict=INVIABLE → 5 agents (ignores budget, domain, regime)
GOAP (v3.1):   Given budget=15, domain=Legal, regime=adversarial →
               ROL:3 + FORENSE:3 + UNIT-INQUISITOR:1 = 7 calls (optimal)
```

**Integration:** `GOAPPlanner.plan(ctx, run_ssm, preliminary_verdict)` returns:
- `plan` — ordered list of Action objects
- `total_cost` — tokens/calls required
- `rol_agents`, `forense_agents` — counts
- `ssm_scale` — MICRO/MESO/MACRO or None
- `tribunal_label` — SINGLE/TRIBUNAL_LIGHT/TRIBUNAL_FULL/TRIBUNAL_MAX
- `reasoning` — human-readable plan explanation

**Fallback:** If A* fails (no plan found within max_iterations), deterministic fallback plan activates automatically.

---

#### 2. Legal Taxonomy — 12 Practice Sub-areas

Source: `anthropics/claude-for-legal` (Apache 2.0) — adapted for Dark Strategist forensic audit.

**`prompts/system_prompt_legal.md`** — Updated with 12 legal practice sub-areas:

| ID | Sub-area | Primary Risk |
|----|----------|-------------|
| L01 | Commercial Legal | Unlimited liability, IP ownership |
| L02 | Corporate / M&A | Undisclosed liabilities, synergy claims |
| L03 | Employment | Misclassification, non-compete enforceability |
| L04 | Privacy | GDPR/CCPA compliance, consent validity |
| L05 | Product Legal | False advertising, warranty gaps |
| L06 | Regulatory | Reporting gaps, jurisdictional conflicts |
| L07 | AI Governance | AI output IP, bias monitoring, vendor liability |
| L08 | IP Legal | Chain of title, OSS contamination |
| L09 | Litigation | Jurisdictional defects, damages calculation |
| L10 | Real Estate Legal | Title gaps, zoning violations |
| L11 | Finance Legal | Covenant breach, cross-default |
| L12 | Public Regulatory | Procurement irregularities, political risk |

New features in legal prompt:
- Sub-area auto-detection via signal words
- Per-sub-area War Room orchestration table
- Per-sub-area failure catalog with auto-severity
- L07 AI Governance as dedicated sub-area (first explicit AI legal audit protocol)
- RULE L6: AI governance under precautionary principle when regulation absent

**`orchestrator/catalogs.py`** — Updated with:
- `LEGAL_SUBAREA_MAP` — keyword → sub-area (L01-L12) auto-detection
- `LEGAL_SUBAREA_LABELS` — sub-area codes to human names
- `LEGAL_SUBAREA_ROLES` — specialized Rol + Forense agents per sub-area
- Enhanced `Legal` entry in `ROLE_CATALOG` with 5 Rol + 5 Forense agents
- `DOMAIN_MAP` expanded with legal keywords (nda, msa, gdpr, dsar, trademark, employment, litigation, ai governance)
- `DOMAIN_TOOLS` Legal entry updated with `sub_area_detection` + `ip_chain_audit`

---

#### Architecture Impact

- AFO now has two planning modes:
  - `GOAP_MODE`: dynamic A* planning (default when GOAPPlanner is instantiated)
  - `FIXED_MODE`: Swarm Activation Score fallback (preserved for backward compat)
- Legal domain now has 3-layer specificity:
  - Domain level: "Legal"
  - Sub-area level: L01-L12 (auto-detected or declared)
  - Agent level: sub-area-specific Rol + Forense from LEGAL_SUBAREA_ROLES

---

#### Pending — v3.1 Roadmap

- [ ] Integrate GOAPPlanner into TribunalTransversal.run()
- [ ] ContextBuilder: auto-detect legal sub-area and override roles
- [ ] Trust scoring for temporary sub-agents (Ruflo-inspired)
- [ ] example_04 — COMPARATIVE MODE with Tribunal Transversal
- [ ] example_05 — OPTIMIZATION MODE with SSM
- [ ] Cloud Function update for v3.0/v3.1 case-based API

---

## [3.0.0] — 2026-05-14

Tribunal Transversal (2-layer). Dynamic Prompt Engine. Pydantic VerdictOutput.
RuntimeContext + ContextBuilder. GOAP foundation. Medical domain (16 total).

---

## [2.9.0] — 2026-05-13

SSM + Transparency Report. 4-round interaction. MICRO/MESO/MACRO scales.

---

## [2.8.0] — 2026-05-13

AFO + Tribunal Adversarial. Budget Controller. Sub-Agent Spawner. Verdict Synthesizer.

---

## [2.7.0] — 2026-05-12

Autonomous Router + 11 Domain Prompts + Python Infrastructure.

---

## [2.6.x] — 2026-05-05/06

SAT Intelligence Doctrine + 4 Skills. Trading + Legal domain variants.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, Blocks 0–6.
