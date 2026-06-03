# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.8.0] — 2026-06-03

### Added — RAG retrieval at the document-feed layer (roadmap TOP-7: infinity->RAG, re-scoped)
- New `orchestrator/retriever.py`: lexical BM25 retriever (`rank_bm25`, pure Python + numpy — no model, no API, no daemon, no Docker). Two jobs, both at the document-feed layer:
  - R1 intra-document: replaces the blind `document[:doc_window]` truncation in the tribunal (`_call_agent`) and sub-agent spawner with role-relevant chunk retrieval, so long documents no longer silently lose everything past the window.
  - R2 jurisdictional corpus: optional injection of relevant local-corpus passages, selected per resolved domain via `JURISDICTION_CORPUS_MAP` (`catalogs.py`) and loaded from `corpus/<id>.txt|.jsonl`. Ships EMPTY (mechanism now, content later).
- New `corpus/` directory (README + .gitkeep) for jurisdictional corpora.
- `RuntimeContext.corpus` selector field, resolved by `ContextBuilder`.
- Config: `rag` block + `tribunal.parent_report_window` in `config.example.json` and the `main.py` runtime default. Config-izes the previously hardcoded `parent_report[:1000]` cut (closes the "windows-by-config" inconsistency).

### Architecture (re-scope vs roadmap)
- The roadmap premise "RAG jurisdictional in ContextBuilder" was corrected against the live code: `ContextBuilder` is document-free, so it only SELECTS the corpus; retrieval + injection live at the document-feed layer. `infinity`/Docker rejected as overkill for single-document forensic audits — embedded BM25 keeps the agent zero-infra.

### Non-breaking guarantee
- Strictly additive: if a document fits the window AND no corpus is mapped, OR `rank_bm25` is unavailable, the legacy `[:N]` feed is preserved byte-for-byte. Only long documents / mapped corpora activate retrieval.

### Dependencies
- `+ rank_bm25>=0.2.2` (orchestrator/requirements.txt).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + orchestrator product-face -> v3.8.0. Module docstrings and skills unchanged (content-based). Skill count unchanged (6).

### JARP_CERTIFIED: DS v3.8.0 — PA-20260603-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.8.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.7.0 full-coverage baseline (19/19 unchanged). Scope: v3.8.0 delta — `orchestrator/retriever.py` (BM25; R1 intra-document + R2 jurisdictional corpus), tribunal/spawner document-feed integration, `RuntimeContext.corpus` + `JURISDICTION_CORPUS_MAP`, config (`rag` block + `parent_report_window`), dual-version barrido (base + router + 19 variants + product-face), docs. RULE 08 self-audit L0 (PA-20260603-001) PASS first. Functional evidence: retriever unit 12/12 + runtime integration test (module graph imports, `ctx.corpus` resolves, RAG helpers execute without API, byte-identical fallback, long-doc clause retrieval). Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 1 LATENT (accepted) → `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. LATENT D-v38-01: `doc_top_k` default skew (retriever signature 5 vs config/orchestrator 6) — non-functional (config authoritative), accepted, align on next retriever touch. infinity/Docker rejected (overkill for single-document forensic audit; embedded BM25 keeps zero-infra). RAG re-scoped: ContextBuilder is document-free → selects corpus only; retrieval at the document-feed layer. Supersedes PA-20260602-002 (DS v3.7.0). `JARP_BENCHMARK_LIVE` advances to v3.8.0. Valid until 30/08/2026 or DS v4.0.0.

## [3.7.0] — 2026-06-02

### Added — Context Degradation forensic lens (roadmap TOP-7 item #6)
- New skill #6 `context-degradation` (v1.0.0, adapted from Agent-Skills-for-Context-Engineering, MIT): five degradation patterns (lost-in-middle, poisoning, distraction, confusion, clash) + four-bucket mitigation (Write/Select/Compress/Isolate). Detection lens only — does NOT alter the deterministic verdict or severity taxonomy.
- P04 Code: RULE C05 (blind `[:N]` truncation of structured output → lost-in-middle → SERIOUS) + 5 Failure Catalog rows + CONTEXT_PIPELINE/LLM_INTEGRATION taxonomy row.
- P07 Cybersecurity: RULE CY06 (untrusted content poisoning a context that drives a privileged action → SERIOUS, FATAL via Rule 09) + 5 Failure Catalog rows + AGENT_LLM_ARCHITECTURE taxonomy row. Complements CY05 lethal-trifecta.
- Skills registry: 5 → 6 (system_prompt.md Composition map + catalogs.py SKILLS_CATALOG).

### Notes
- Telephone-game NOT re-worked: already resolved in v3.4 (R1 FUGA#1/#3). This bump adds the outward-facing audit lens, not a re-implementation.
- Atomic §4.14.1 bump: all 19 domain variants + router + product-face → v3.7.0.
- Deferred to v3.8.0 (with infinity/RAG): hardening DS's own residual `[:N]` cuts in prompt_engine/spawner — the very pattern C05 now audits in third parties.

### JARP_CERTIFIED: DS v3.7.0 — PA-20260602-002 ✅

Level 1 — JARP DEEP full-coverage 7-axis forensic audit of `dark-strategist-agent` v3.7.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002). Scope: base + router + 19 domain variants + 6 skills + orchestrator product-face + docs + v3.7.0 additions (context-degradation forensic lens: skill #6 v1.0.0 adapted from Agent-Skills-for-Context-Engineering MIT, RULE C05/CY06, +10 Failure Catalog rows P04/P07, AGENT_LLM_ARCHITECTURE taxonomy). FULL COVERAGE (19/19). Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT → `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. NOT confirmatory (skill #6 expanded the documented surface): one finding caught and resolved pre-cert — D-v37-01 (MODERATE, stale skill-count/listing drift in README badge/table/[SKILLS:N] + CLAUDE count/tree/table; functional surfaces Composition map + SKILLS_CATALOG were already correct at 6; replica of D-v36-01). Telephone-game NOT re-worked — already resolved v3.4 (R1 FUGA#1/#3). Supersedes PA-20260602-001 (DS v3.6.0). `JARP_BENCHMARK_LIVE` advances to v3.7.0. Valid until 30/08/2026 or DS v4.0.0.

## [3.6.0] — 2026-06-02

### Minor — Legal & Finance Forensic Matrix (knowledge-work-plugins incorporation)

Roadmap TOP-7 item #4 (knowledge-work-plugins legal+finance). 25 forensic
incorporations into P03 Legal + P05 Financial. Atomic version-stamp bump per
§4.14.1. Does NOT touch the 9-unit spawner roster (domain content only).

#### New content
- docs/legal_finance_forensic_matrix.md — annotated provenance of the 25 incorporations,
  the 4 financial decompositions, the SOX deficiency->tier map, and the non-binding
  Severity x Likelihood scoring.
- P03 Legal: +Severity x Likelihood prioritization metadata (NON-BINDING, RULE LG07);
  +9 Failure Catalog rows (L01 NDA non-solicit/non-compete/carveouts/playbook-deviation/
  MSA-gap/surviving-obligation, L04 vendor-PII-without-DPA, L06 missing-approval/
  unmapped-jurisdiction); BLOCK 1 header extended (Likelihood, Risk Score).
- P05 Financial: +4 variance decomposition lenses (Price/Volume, Rate/Mix,
  Headcount/Comp, Spend Category); +RULE F05/F06/F07/F08; +9 Failure Catalog rows
  (SOX material-weakness/significant-deficiency/control-deficiency, significant-account-
  without-control, GL-subledger-unreconciled, reconciling-items-no-aging, material-
  variance-undecomposed, GAAP-presentation-nonconformity, materiality-threshold-
  undeclared); +Severity x Likelihood metadata (cross-domain consistency).

#### Design invariant preserved
- Deterministic verdict (>=1 FATAL -> INVIABLE) UNCHANGED. Severity x Likelihood is
  non-binding triage metadata only — never alters the binding 4-tier scale or verdict.
- SOX deficiency severity maps NATIVELY to the 4-tier scale (RULE F07) — no probabilism.

#### Discarded source skills (no forensic contact)
- Legal: legal-response, signature-request, brief, meeting-briefing.
- Finance: journal-entry, journal-entry-prep, close-management.

#### Pending
- Re-certification (supersedes PA-20260601-004) — expected NOT confirmatory
  (expanded P03/P05 surface). Run after this release lands.

---

## [Certification] — 2026-06-02

### JARP_CERTIFIED: DS v3.6.0 — PA-20260602-001 ✅

Level 1 — JARP DEEP full-coverage 7-axis forensic audit of `dark-strategist-agent` v3.6.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002). Scope: base + router + 19 domain variants + 5 skills + orchestrator product-face + docs + v3.6.0 additions (legal+finance forensic matrix: Severity×Likelihood non-binding metadata, 4 variance decompositions, SOX deficiency tier map, 18 new Failure Catalog rows P03/P05, docs/legal_finance_forensic_matrix.md). FULL COVERAGE (19/19). Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT → `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. NOT confirmatory (expanded P03/P05 surface): two findings caught and resolved pre-cert — C-v36-01 (LATENT, monotonic catalog order L01/L04/L06+financial, fixed 73e3de2) + D-v36-01 (MODERATE, stale row counts +12->+18 / +10->+9, fixed 73e3de2). Supersedes PA-20260601-004 (DS v3.5.0). `JARP_BENCHMARK_LIVE` advances to v3.6.0. Valid until 30/08/2026 or DS v4.0.0.

---

## [Certification] — 2026-06-01

### JARP_CERTIFIED: DS v3.5.0 — PA-20260601-004 ✅

Level 1 — JARP DEEP full-coverage 7-axis forensic audit of `dark-strategist-agent` v3.5.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002). Scope: base + router + 19 domain variants + 5 skills + orchestrator product-face + docs + v3.5.0 additions (UNIT-INGEST, UNIT-FACTCHECK, UNIT-PSYCH 80+ catalog, stop-slop scorer, P07 RULE CY05). FULL COVERAGE (19/19). Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT → `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. NOT confirmatory (expanded surface): two findings caught and resolved pre-cert — C-P07-01 (LATENT, Failure Catalog ordering, fixed 0a234ff) + D-UNIT-01 (MODERATE, 8→9 unit-count drift, fixed 3d1c29e). Supersedes PA-20260601-002 (DS v3.4.0). `JARP_BENCHMARK_LIVE` advances to v3.5.0. Valid until 30/08/2026 or DS v4.0.0.

---

## [3.5.0] — 2026-06-01

### Minor — Ingestion + Fact-Check + Behavioral Catalog + Prose Scorer + P07 Hardening

Five capability additions (v3.3/v3.4 roadmap TOP-7 low-effort batch + s19
governance-classified lethal-trifecta). Atomic version-stamp bump per §4.14.1.

#### New capabilities
- UNIT-INGEST (orchestrator/ingest.py) — markitdown document preprocessor
  (PDF/DOCX/PPTX/XLSX/HTML -> Markdown), graceful fallback, never crashes the
  pipeline. Hooked at main.py document load. NOT a finding-emitter.
- UNIT-FACTCHECK (orchestrator/sub_agent_spawner.py) — new permanent N2 forensic
  sub-agent: claim/statistic/source validation; anti-fabrication (UNVERIFIED).
- UNIT-PSYCH expansion (sub_agent_spawner.py + docs/psych_bias_catalog.md) —
  bias catalog ~15 -> 80+ across 8 families.
- stop-slop (orchestrator/slop_filter.py) — stdlib-only 5-dim prose scorer
  (35/50 threshold; any saturated dimension forces REVIEW), score-only advisory
  block in the transparency report; never mutates findings or verdict.
- lethal-trifecta -> P07 Cybersecurity (system_prompt_cybersecurity.md) —
  RULE CY05 (FATAL) + 2 monotonic Failure Catalog rows.

#### Version-stamp alignment (atomic, §4.14.1)
- base, router (->v3.5.0-ROUTER), 19 variants (vX.5.0-DOMAIN + BASE_PROTOCOL
  v3.5.0), README, CLAUDE.md bumped to 3.5.0. Product-face: main.py +
  tribunal_transversal.py Transparency Report header -> v3.5.0.
  sub_agent_spawner.py content-version 2.8.0 -> 2.9.0. Other module docstrings
  left at content-introduction versions (content-based, per v3.4.0 precedent).

#### Certification status
- v3.5.0 CERTIFIED — PA-20260601-004 (Level 1 JARP DEEP, full coverage 19/19,
  0/0/0/0). Supersedes PA-20260601-002. Two pre-cert findings resolved:
  C-P07-01 (catalog ordering) + D-UNIT-01 (unit-count drift). See [Certification].

---

## [Certification] — 2026-06-01
### JARP_CERTIFIED: DS v3.4.0 — PA-20260601-002 ✅
Full 7-axis forensic audit (Level 1 — JARP DEEP) executed by `prompt-architect-agent` v1.3.0 (JARP_CERTIFIED PA-20260527-002) over the complete v3.4.0 release: base + router + 19 domain variants + 5 skills + orchestrator product-face + docs. FULL COVERAGE (19/19 domain variants). Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT → `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. Confirmatory re-cert (v3.4.0 changed synthesis/provenance/dead-code, not the prompt/skill surface). Supersedes PA-20260529-001 (DS v3.3.0). `JARP_BENCHMARK_LIVE` advances to v3.4.0. Valid until 30/08/2026 or DS v4.0.0.

## [3.4.0] — 2026-05-31

### Minor — Synthesis Shape Contract + Live Transparency Provenance + Dead-Code Removal

First release validated against a live `claude-opus-4-7` end-to-end run (E2E regression gate, blocker (b) cleared). Three substantive changes plus the atomic version-stamp alignment per §4.14.1.

#### DSv34-SHAPE — Synthesis output contract (prompt_engine.py)
- `SYNTHESIS_TEMPLATE` OUTPUT FORMAT previously showed empty findings arrays with no object schema, so the live model abbreviated MODERATE/LATENT entries and the Pydantic `Finding` validation rejected them (missing `severity`/`evidence`/`root_cause`).
- Pinned the full six-field finding object shape in all four `*_findings` arrays + an explicit instruction not to abbreviate or merge findings into `multi_agent_confirmed`. The `Finding` schema (strict, 5 required fields) is unchanged — the prompt was under-specifying the contract, not the validator over-constraining it.

#### DSv34-PROV — Live transparency provenance restored (tribunal_transversal.py)
- The live `_build_transparency_report` had dropped the sub-agent provenance block that the (now-removed) `tribunal.py` rendered. Restored: `_init_transparency` gains the `sub_agents` key; `run()` collects `sub_agents_used` from the Forense layer (defensive `.get()`/`isinstance`); the report renders a `SUB-AGENTES FORENSES (N2)` block (permanent + temporary) between Layer 2 and Verdict Summary.

#### DSv34-DEAD — Dead modules removed
- Deleted `orchestrator/tribunal.py` and `orchestrator/verdict_synthesizer.py` (orphaned since the v3.0 Tribunal Transversal migration; verified zero importers — only `tribunal.py` referenced `verdict_synthesizer`). Synthesis lives in `TribunalTransversal._synthesize` with a deterministic fallback.
- Synced the "v2.x preserved / coexisting for backward compatibility" narrative in `CLAUDE.md` (repository structure tree) and `prompts/system_prompt.md` (Composition map) to reflect the removal.

#### DSv34-SYNTH — Accepted characteristic (no code change)
- The live LLM synthesis parses cleanly only for low-finding-density documents; for finding-rich documents the JSON exceeds the output budget / malforms and the deterministic fallback (a designed, validated component — `c_fallback_intact`) produces the verdict. Accepted as designed graceful degradation, not a defect. Documented for future hardening if a synthesis-purity requirement emerges.

#### Version-stamp alignment (atomic, §4.14.1)
- base, router (→v3.4.0-ROUTER), 19 variants (vX.4.0-DOMAIN + BASE_PROTOCOL v3.4.0), README, CLAUDE.md bumped to 3.4.0.
- Product-face stamps in orchestrator updated: main.py (entry/argparse/runtime print) and tribunal_transversal.py Transparency Report header → v3.4.0. Module-level docstrings left at their content-introduction versions (content-based versioning, consistent with skills).
- §4.14/§4.14.1 rule examples refreshed to the current minor (router v3.4.x ↔ agent v3.4.x).

#### Certification status
- v3.4.0 NOT yet certified at time of this entry. Re-cert (7-axis Level 1 JARP DEEP, full coverage) pending — will supersede PA-20260529-001.

---

## [Certification] — 2026-05-29

### JARP_CERTIFIED: DS v3.3.0 — PA-20260529-001 ✅

Full 7-axis forensic audit (Level 1 — JARP DEEP) executed by `prompt-architect-agent` v1.3.0 (JARP_CERTIFIED PA-20260527-002) over the complete v3.3.0 release: 21 prompts + 5 skills + orchestrator product-face + docs. FULL COVERAGE (19/19 domain variants) — supersedes the reduced 47% sample of PA-20260525-001.

Findings: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT.

A6 coherence verified end-to-end: 19/19 variant footers reference BASE_PROTOCOL v3.3.0; router-agent minor stamps matched (3.3.x / 3.3.x); router UNKNOWN_DOMAIN versionless placeholder confirmed non-finding; §4.14.1 Domain Variant Contract governs all variants. DSv33-06 (identity-lock) formally deferred — not a pending finding.

```
[JARP_CERTIFIED: v3.3.0 — PA-20260529-001]
[AUDIT_DATE: 2026-05-29]
[AUDITOR: THE PROMPT ARCHITECT — prompt-architect-agent v1.3.0]
[SCOPE: LEVEL 1 — JARP DEEP — FULL COVERAGE]
[FINDINGS: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT]
[SUPERSEDES: PA-20260525-001 (v3.2.2, reduced conformance 47%)]
[NEXT_REVIEW: 2026-08-27 or major version]
```

---

## [3.3.0] — 2026-05-29

### Minor — Prompt-Sweep Cycle Closure + Skills Metadata Normalization

Closes the full prompt-sweep audit cycle (B1-B5) opened in the v3.3 sprint. 26 artifacts reviewed (21 prompts + 5 skills). No behavioral changes — this release is metadata normalization, version-stamp alignment, and documentation truth-up. Atomic bump per §4.14.1.

#### §4.14.1 validated end-to-end
- 19/19 domain variants confirmed COMPLIANT against the Domain Variant Contract — 0 contract violations across the catalog.
- Legal deep pass: 12/12 sub-area catalogs verified complete (6 historically-flagged catalogs L05/L06/L09/L10/L11/L12 confirmed present since v3.1.0 remote).
- Confirmed non-findings: LGv33-01 (Legal BLOCK 7 is the canonical Contract-permitted example), LGv33-02 (2-letter prefix is the only naming requirement).

#### Skills metadata normalized (DSv33-S01 + DSv33-S02)
- Added `version:` field to frontmatter of 4 structural skills (kac-assumption-audit, ach-competing-explanations, deception-detection, verdict-verification) — stamped 2.6.0 (introduction version, per content-based skill versioning).
- Converted `adaptive-autonomous-drive/SKILL.md` from markdown-comment header to valid YAML frontmatter (name + version 3.2.0 + description). Load path unaffected (SKILLS_CATALOG resolves by explicit path, not auto-discovery — DSv33-S02 confirmed MODERATE, latent portability risk only).

#### Version-stamp alignment (atomic, §4.14.1)
- base, router (→v3.3.0-ROUTER), 19 variants (vX.3.0-DOMAIN + BASE_PROTOCOL v3.3.0), README, CLAUDE.md bumped to 3.3.0.
- Product-face stamps in orchestrator updated: main.py (entry/argparse/runtime print) and tribunal_transversal.py Transparency Report header → v3.3.0. Module-level docstrings left at their content-introduction versions (content-based versioning, consistent with skills).
- OBS-1 resolved: variant header provenance normalized in-sweep.

#### Diagnostic audits (no cert impact)
- PA-20260528-001 (B1), PA-20260528-002 (B4+B5) — diagnostic finding-sweeps, not certifications.

#### Deferred (not in this release)
- DSv33-06 (identity-lock + critical-rule reinforcement in base) — requires dedicated design + §4.14 self-audit. Deferred to its own cycle.

---

## [Certification] — 2026-05-25

### JARP_CERTIFIED: DS v3.2.2 — PA-20260525-001 ✅

Reduced conformance check against Contract §4.14.1 executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001) over base + router + 6 of 19 domain variants (sample: P02 Trading, P03 Legal, P08 Agro, P15 Medical, P16 Marketing, P19 Strategy — 47% file coverage).

**Findings (new):** 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT

**Contract compliance verification:**
- Output Format Contract — PASS (all 6 sampled variants declare explicit inheritance + adaptations, no implicit inheritance)
- Footer Contract — PASS (canonical 3-line footer present in all sampled variants)
- Severity Mapping Contract — PASS (no Failure Catalog row contradicts Severity Taxonomy)
- Naming Convention Contract — PASS (T, LG, A, MD, MK, ST prefixes correct and consistent with 2-letter immutable rule)
- Versioning Contract — PASS (BASE_PROTOCOL footer references point to v3.2.2)

**Targeted checks:**
- P03 Legal Geofence monotonicity — PASS (tier-shift rule sums independently, capped at FATAL, pre-shift severity preserved for traceability)
- P08 Agro Yield reclassification SERIOUS — PASS (justification documented in variant)
- Router bind rule — PASS (v3.2.0-ROUTER ↔ Agent v3.2.2, minor versions aligned per §4.14)

**Cascade status:**
- `PA-20260524-001` (PA-agent v1.1.0) — ACTIVE (auditor authority confirmed)
- `PA-20260525-001` (DS v3.2.2) — ACTIVE ✅
- `PA-20260426-002` (DS v2.5.1) — remains VOID

**Validity:** 90 days (until 2026-08-23) OR major version bump (v4.0.0).

**Residual debt:** Sprint v3.3 — 38 MODERATE + 23 LATENT findings carried from the original DS-CERT-v3.2.0 batch (non-blocking).

---

## [3.2.2] — 2026-05-24

### Patch — DS-CERT-v3.2.0 Batch Closure (PA-20260524-002)

Triggered by the JARP DEEP Level 1 audit batch `DS-CERT-v3.2.0` executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001). Sub-batches B3 through B8 found 19 SERIOUS bloqueantes across 17 of 19 domain variants. v3.2.2 resolves all 19 via a single architectural intervention — the Domain Variant Contract (§4.14.1) — applied uniformly across the catalog.

#### Architectural intervention — §4.14.1 Domain Variant Contract (new)

Added a new sub-section to `system_prompt.md` §4.14 PROTOCOL GOVERNANCE: **Domain Variant Contract**. The Contract binds every `prompts/system_prompt_<domain>.md` to four sub-contracts:

- **Output Format Contract** — every variant must declare an `## OUTPUT FORMAT` section that explicitly inherits BLOCK 0–6 from base. Variants may extend BLOCK 1 with domain-specific fields and may add BLOCKs ≥7 for domain-mandatory sections (e.g., Legal BLOCK 7 = AI_DISCLAIMER). Implicit inheritance is no longer permitted.
- **Footer Contract** — every variant ends with the canonical footer block:
  ```
  [PROTOCOL_STATUS: ACTIVE — vX.Y.Z-DOMAIN]
  [BASE_PROTOCOL: system_prompt.md vA.B.C]
  [CONTRACT: §4.14.1 — Domain Variant Contract]
  ```
- **Severity Mapping Contract** — Failure Catalog rows must be internally consistent with the variant's Severity Taxonomy definitions. Geofence escalation rules must be monotonic — severity escalates by N tiers capped at FATAL, never skipping tiers or leaving input severities undefined.
- **Naming Convention Contract** — generic rules use numeric IDs (RULE 01–10 reserved for base). Domain-specific rules use 2-letter prefix + number: T for Trading, LG for Legal, CY for Cybersecurity, CL for Cloud, A for Agro, RE for RealEstate, S for Science, M for Media, EC for Ecommerce, TC for Telecom (distinct from T), PS for PublicSector, MD for Medical, MK for Marketing, OP for Operations, HR for HR, ST for Strategy, SU for Startup, C for Code, F for Financial. Two-letter prefixes are immutable.
- **Versioning Contract** — domain variant version stamps track the composed-agent minor version; BASE_PROTOCOL footer references must always point to the current composed-agent base version.

#### Resolved findings — 19 SERIOUS bloqueantes

**Pattern #SIS-1 — Output Format absent (15 SERIOUS resolved):**
Variants P04 Code, P05 Financial, P06 Cloud, P07 Cybersecurity, P08 Agro, P09 RealEstate, P10 Science, P11 Media, P12 Ecommerce, P13 Telecom, P14 PublicSector, P15 Medical, P16 Marketing, P17 Operations, P18 HR, P19 Strategy, P20 Startup — all received an explicit `## OUTPUT FORMAT` section declaring base inheritance + domain extensions per the Contract. P02 Trading (already compliant) and P03 Legal (already compliant with BLOCK 7 AI_DISCLAIMER) updated for consistency only.

**Pattern #SIS-2 — Naming collision risk (15 LATENT resolved):**
All domain variants renumbered to the §4.14.1 Naming Convention. Specifically: P13 Telecom rules T1-T4 → TC01-TC04 (eliminates direct collision with P02 Trading T1-T3). All other variants normalized to 2-digit padded numbering (e.g., CY1 → CY01, MD1 → MD01, ST1 → ST01).

**Pattern #SIS-3 — BASE_PROTOCOL footer inconsistency (15 LATENT resolved):**
All 19 variants now declare the canonical footer per the Footer Contract, pointing to `system_prompt.md v3.2.2`. Stale references (v2.5.1, v2.6.1) and missing references (P04 Code, P05 Financial, others) all corrected uniformly.

**Punctual fix — P03 Legal Geofence non-monotonic (1 SERIOUS resolved — B3.2.1):**
Geofence severity calibration table replaced with monotonic tier-shift rules. Each qualifying condition adds N tiers to underlying finding severity, capped at FATAL. Applied conditions stack additively. Pre-shift severity recorded in finding for traceability. The previous fixed-mapping rows (which left SERIOUS input severities undefined under "no independent judiciary") are replaced.

**Punctual fix — P08 Agro Yield mis-classified (1 SERIOUS resolved — B4 finding):**
"Yield above regional benchmark without documented justification" reclassified from 🔴 FATAL → 🟠 SERIOUS. The previous FATAL contradicted the variant's own severity taxonomy definition (FATAL = biological impossibility). Yield overestimation is overstatement, not impossibility. With documented justification (technical irrigation, improved seeds), the finding is removed entirely rather than escalated.

#### Findings deferred to v3.3 (non-blocking) — RESOLVED in [3.3.0]

- 38 MODERATE findings from the batch (sub-area Failure Catalogs missing for Legal L05/L06/L09/L10/L11/L12; multi-day batch resumption rules in prompt-architect-agent; comparative mode Phase 0 collection scope; etc.)
- 22 LATENT findings (most resolved at root by §4.14.1 — residuals closed in [3.3.0] prompt-sweep cycle)
- 1 LATENT residual from B2-RE.1 ("v2.5.1 forensic base" wording in ARCHITECTURAL LAYERS section)

#### Cascade impact recorded

- `PA-20260426-002` (Dark Strategist v2.5.1 certification, issued by `prompt-architect-agent` v1.0.0 before its decertification) → **VOID** as of this release. Superseded by v3.2.2 certification pending re-audit.
- The DS-CERT-v3.2.0 batch master `PA-20260524-002` is closed with this release. New certification under v3.2.2 will require a re-audit pass against the auditor v1.1.0 standards — to be scheduled in the next session.

#### Files modified

- `prompts/system_prompt.md` — v3.2.0 → v3.2.2 + §4.14.1 Domain Variant Contract added + BLOCK 1 dual-language label rule
- `prompts/system_prompt_trading.md` — v2.6.0-TRADING → v3.2.2-TRADING + footer
- `prompts/system_prompt_legal.md` — v3.1.0-LEGAL → v3.2.2-LEGAL + monotonic Geofence + LG-series naming + footer
- `prompts/system_prompt_code.md` — v2.7.0-CODE → v3.2.2-CODE + Output Format + C-series + footer + ABAP guideline reference
- `prompts/system_prompt_financial.md` — v2.7.0-FINANCIAL → v3.2.2-FINANCIAL + Output Format + F-series + threshold ladder + footer
- `prompts/system_prompt_cloud.md` — v2.7.0-CLOUD → v3.2.2-CLOUD + Output Format + CL-series + footer
- `prompts/system_prompt_cybersecurity.md` — v2.7.0-CYBERSECURITY → v3.2.2-CYBERSECURITY + Output Format + CY-series + footer
- `prompts/system_prompt_agro.md` — v2.7.0-AGRO → v3.2.2-AGRO + Output Format + A-series + Yield reclassified SERIOUS + footer
- `prompts/system_prompt_realestate.md` — v2.7.0-REALESTATE → v3.2.2-REALESTATE + Output Format + RE-series + footer
- `prompts/system_prompt_science.md` — v2.7.0-SCIENCE → v3.2.2-SCIENCE + Output Format + S-series + footer
- `prompts/system_prompt_media.md` — v2.7.0-MEDIA → v3.2.2-MEDIA + Output Format + M-series + footer
- `prompts/system_prompt_ecommerce.md` — v2.7.0-ECOMMERCE → v3.2.2-ECOMMERCE + Output Format + EC-series + footer
- `prompts/system_prompt_telecom.md` — v2.7.0-TELECOM → v3.2.2-TELECOM + Output Format + TC-series (renamed from T to avoid Trading collision) + footer
- `prompts/system_prompt_publicsector.md` — v2.7.0-PUBLICSECTOR → v3.2.2-PUBLICSECTOR + Output Format + PS-series + footer
- `prompts/system_prompt_medical.md` — v3.0.0-MEDICAL → v3.2.2-MEDICAL + Output Format + MD-series + footer
- `prompts/system_prompt_marketing.md` — v3.2.0-MARKETING → v3.2.2-MARKETING + Output Format + MK-series + footer
- `prompts/system_prompt_operations.md` — v3.2.0-OPERATIONS → v3.2.2-OPERATIONS + Output Format + OP-series + footer
- `prompts/system_prompt_hr.md` — v3.2.0-HR → v3.2.2-HR + Output Format + HR-series + footer
- `prompts/system_prompt_strategy.md` — v3.2.0-STRATEGY → v3.2.2-STRATEGY + Output Format + ST-series + footer
- `prompts/system_prompt_startup.md` — v3.2.0-STARTUP → v3.2.2-STARTUP + Output Format + SU-series + footer
- `CHANGELOG.md` — this entry

Total files modified: **21** (1 base + 19 domain variants + CHANGELOG).

#### Version bump rationale

Patch (`3.2.1` → `3.2.2`). The changes resolve declared gaps in v3.2.0 (Output Format inconsistencies across the domain catalog, naming collision risks, footer drift). One architectural addition (§4.14.1 Contract) but no new agent capability, no orchestrator change, no new domain. Patch is the honest bump — neither minor (would imply new features) nor major (would imply architecture change). The Contract is governance enforcement of pre-existing intent.

---

## [3.2.1] — 2026-05-24

### Patch — B2 Sub-batch Fixes (DS-CERT-v3.2.0 batch / PA-20260524-002 / B2/B9)

Triggered by the JARP DEEP Level 1 audit batch `DS-CERT-v3.2.0` executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001). Sub-batch B2/B9 found 1 CRITICAL + 2 SERIOUS findings affecting `prompts/system_prompt.md` and `prompts/system_prompt_router.md`. This patch resolves the bloqueantes; remaining MODERATE findings are deferred to v3.3.

#### Resolved findings

**🔴 CRITICAL — B2.5 (router):** PROMPT CATALOG and Step 2 keyword extraction had not been updated since v2.7.0-ROUTER (12/05/2026). 6 of 20 domain prompts (P15 medical, P16 marketing, P17 operations, P18 hr, P19 strategy, P20 startup) were physically present in `prompts/` but unreachable via routing — 30% of the catalog was operationally inaccessible.

- Extended PROMPT CATALOG with P15-P20 rows.
- Extended Step 2 keyword catalog with domain-specific signals.
- Added Disambiguation Rules section for overlapping signals.
- Added new routing rule R8: catalog completeness.

**🟠 SERIOUS — B2.1 (system_prompt.md):** File header stamped v2.5.1 while composed agent was at v3.2.0.

- Updated version stamp from `2.5.1` to `3.2.0`.
- Added section `ARCHITECTURAL LAYERS — v3.2.0` documenting composition.
- Updated final status block.

**🟠 SERIOUS — B2.6 (router):** Router version stamp out of sync with composed agent.

- Bumped router header to `Version: 3.2.0-ROUTER`.
- Updated `CATALOG_VERSION` to `3.2.0 — 19 domain prompts + 1 base (P01 General)`.
- Added rule in `system_prompt.md` §4.14: router version stamp must match composed agent minor version.

---

## [3.2.0] — 2026-05-15

### Major Release — Adaptive Autonomous Drive + 5 New Domains

#### 1. Skill: Adaptive Autonomous Drive

**`skills/adaptive-autonomous-drive/SKILL.md`**

Formalizes the autonomous operational layer of Dark Strategist as an official skill. Six internal modules: GoalEngine, MotivationModel, StateMemory, AutonomousLoop, SafetyGuard, SelfEvaluation.

---

#### 2. Five New Domain Variants

| File | Domain | Primary Unit | Rules |
|------|--------|--------------|-------|
| `system_prompt_marketing.md` | Marketing | UNIT-MARKET | MK1–MK4 |
| `system_prompt_operations.md` | Operations | UNIT-TECH | OP1–OP4 |
| `system_prompt_hr.md` | Human Resources | UNIT-COMPLIANCE | HR1–HR4 |
| `system_prompt_strategy.md` | Strategy | UNIT-MARKET | ST1–ST4 |
| `system_prompt_startup.md` | Startup | UNIT-QUANT | SU1–SU5 |

Each domain includes: document taxonomy (7 types), Phase 0 intake protocol, severity taxonomy with domain rules, 7-level forensic analysis, failure catalog with auto-severity, and War Room orchestration table.

---

#### 3. Catalogs Updated

**`orchestrator/catalogs.py`** — v3.2.0:
- ROLE_CATALOG: 5 new domains added
- SSM_CATALOG: 5 new domain persona sets added
- DOMAIN_MAP: 30+ new keyword mappings for new domains
- DOMAIN_TOOLS: 5 new domain tool sets added
- SKILLS_CATALOG: maps all 5 active skills including adaptive-autonomous-drive

**Total domains: 20**

---

#### Patch — 2026-05-23 (documental, no version bump)

- Fixed inconsistent domain count claim in v3.2.0 section
- Default LLM model in orchestrator updated to `claude-opus-4-7`

---

## [3.1.0] — 2026-05-15

GOAP A* Planner + Legal 12 Sub-area Taxonomy (L01-L12 including L07 AI Governance).

---

## [3.0.0] — 2026-05-14

Tribunal Transversal + Dynamic Prompt Engine + Pydantic VerdictOutput + Medical domain.

---

## [2.9.0] — 2026-05-13

SSM + Transparency Report. 4-round interaction. MICRO/MESO/MACRO.

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
