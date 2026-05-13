# CHANGELOG — Dark Strategist Agent

All significant changes to the system prompt and agent structure are documented here.
Format: [VERSION] — DATE — Description

---

## [2.7.0] — 2026-05-12

### Major Release — Autonomous Router + 11 Domain Prompts + Full Infrastructure

This release transforms dark-strategist-agent from a manually-selected prompt system into a **fully autonomous document auditing platform**. The agent detects the domain, selects the correct prompt, and — when no prompt exists — constructs a dynamic calibration, executes the audit, and notifies the design team via Slack, GitHub Issues, and Google Sheets without user intervention.

#### New Prompts (12 total)

1. `prompts/system_prompt_router.md` — Router Agent. 14-entry catalog, UNKNOWN_DOMAIN protocol, DOMAIN_EXPANSION_RECOMMENDED block.
2. `prompts/system_prompt_code.md` — Code Review. UNIT-TECH primary. ABAP, Java, .NET, Python, JS. RULE C1–C4.
3. `prompts/system_prompt_financial.md` — Financial/M&A/Valuation. UNIT-QUANT primary. RULE F1–F4.
4. `prompts/system_prompt_cloud.md` — Cloud/SaaS/PaaS/IaaS. UNIT-TECH primary. Auto-calibrates by layer. RULE CL1–CL4.
5. `prompts/system_prompt_cybersecurity.md` — Cybersecurity/Systems Audit. UNIT-TECH + UNIT-COMPLIANCE co-primary. RULE CY1–CY4.
6. `prompts/system_prompt_agro.md` — Agriculture/Livestock/Mining. UNIT-BIO primary. RULE A1–A4.
7. `prompts/system_prompt_realestate.md` — Real Estate. UNIT-MARKET + UNIT-QUANT co-primary. RULE RE1–RE4.
8. `prompts/system_prompt_science.md` — Science/R&D/Clinical. UNIT-QUANT + UNIT-PSYCH. RULE S1–S4.
9. `prompts/system_prompt_media.md` — Media/Content Creators. UNIT-MARKET primary. RULE M1–M4.
10. `prompts/system_prompt_ecommerce.md` — E-Commerce/D2C. UNIT-MARKET primary. RULE EC1–EC4.
11. `prompts/system_prompt_telecom.md` — Telecom/Infrastructure. UNIT-GEO + UNIT-INQUISITOR. RULE T1–T4.
12. `prompts/system_prompt_publicsector.md` — Public Sector/Government. UNIT-COMPLIANCE + UNIT-GEO. RULE PS1–PS4.

#### New Infrastructure

`orchestrator/` — Python pipeline: main.py, router.py, notifier.py, sheets_logger.py, requirements.txt, config.example.json
`infrastructure/cloud_function/` — Google Cloud Function: main.py, requirements.txt
`DEPLOY.md` — Full deployment guide: local → Sheets → Slack → GitHub → Cloud Functions → Looker Studio

#### Architecture Impact

- `prompts/` now contains 15 files: 1 base + 1 router + 11 domain + 2 existing
- UNKNOWN_DOMAIN: dynamic calibration + notifications — zero user intervention
- Globally deployable via Cloud Function HTTP endpoint

#### Pending — v2.7 Roadmap

- [ ] example_04 — COMPARATIVE MODE worked example
- [ ] example_05 — OPTIMIZATION MODE worked example
- [ ] UNIT-PSYCH extended bias catalog
- [ ] Looker Studio dashboard template
- [ ] .env template

---

## [2.6.1] — 2026-05-06

### Patch Release — Trading & Legal Domain Variants

1. `prompts/system_prompt_trading.md` — UNIT-QUANT primary. MQL5, Pine Script v6, EURUSD, XAUUSD. RULE T1/T2/T3.
2. `prompts/system_prompt_legal.md` — UNIT-INQUISITOR primary. Geofence Legal. AI Disclaimer mandatory. RULE L1/L2/L3.

---

## [2.6.0] — 2026-05-05

### Major Release — SAT Intelligence Doctrine + 4 Audit Skills

Source: `Blevene/structured-analysis-skill` (Apache 2.0), `obra/superpowers` (MIT).

1. `docs/sat_intelligence_doctrine.md` — 8 axioms, 9-bias map, 12 SAT techniques, Evidence Quality Framework.
2. `skills/kac-assumption-audit/SKILL.md` — KAC. Iron Law: no FATAL without KAC.
3. `skills/ach-competing-explanations/SKILL.md` — ACH. Rank by inconsistency count.
4. `skills/deception-detection/SKILL.md` — 5 checks. Random weakness vs. deliberate concealment.
5. `skills/verdict-verification/SKILL.md` — 18-point checklist + Premortem. Iron Law: no VERDICT without gate.

---

## [2.5.1] — 2026-04-25

§4.22 Industry & Business Taxonomy. Phase 0 INDUSTRY + GIRO DE NEGOCIO split. §4.6 expanded.

---

## [2.5.0] — 2026-04-25

§4.16 MVP_THRESHOLD | §4.17 Operational Modes | §4.18 COMPARATIVE | §4.19 OPTIMIZATION + PROJECTION_MATRIX | §4.20 FAST_TRACK | §4.21 UNIT-PSYCH.

---

## [2.4.0] — 2026-04-24

MIT License. §4.14 Governance. §4.15 Deprecation. Self-Audit DS-20260423-001.

---

## [2.3.0] — 2026-04-21

ES/EN Map. War Room threshold. Geofence expanded. VERSION_TRACK. UNIT-BIO. REPORT_ID.

---

## [2.2.0] — 2026-04-20

Deterministic verdict. Rule 10. NEGLECT_DETECTED. §4.13 Activation Matrix. Block 5 integrity.

---

## [2.1.0] — 2026-04-20

War Room. Sectoral Agnosticism. Micro-Agent Catalog. Geofence Audit. Rules 09/10. Red Line Rule.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, 8 behavioral rules, Blocks 0–6, Dual-Language Protocol.
