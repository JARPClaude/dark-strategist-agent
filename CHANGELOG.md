# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.20.0] - 2026-06-13

### Fixed — Confidence false-positive on tribunal collapse (LW-5, correctness)
- `orchestrator/tribunal_transversal.py`: `_apply_confidence` set `agents_consulted = len(all_outputs)`, counting agents that errored out (connection error / BUDGET_EXCEEDED / parse-fail — appended to `all_outputs` with an `"error"` key and no `findings`). On a 100% tribunal collapse (0 findings), `compute_confidence`'s clean-verdict HIGH branch (`driver_finding_count==0`) then reported HIGH confidence over zero analysis — a misleading auditability signal.
- `agents_consulted` now counts only contributing agents (`isinstance(o, dict) and "error" not in o`). A fully-collapsed tribunal -> `agents_consulted=0` -> `n<2` -> LOW. Genuinely-clean verdicts from healthy agents still reach HIGH (the legitimate clean branch is preserved). Fix is 100% inside `_apply_confidence`; `compute_confidence` (schema.py), `Finding`, and `final_verdict` untouched.

### Tests
- `orchestrator/test_apply_confidence.py`: +3 cases (16->24 checks). C10 collapsed tribunal (5 errored, clean) -> LOW + `agents_consulted==0` + verdict intact; C11 partial coverage (2 healthy + 3 errored) -> MODERATE + `agents_consulted==2`; C12 no-regression (3 healthy corroborating + 2 errored) -> `agents_consulted==3`, corroboration intact, HIGH. `final_verdict` invariance asserted.

### Versioning
- Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.20.0 (bump_manual). Product-face (base + router + 19 variants + README + CLAUDE) -> v3.20.0 (bump_stamps). Module docstrings frozen at origin. No config knob added. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Confidence remains metadata only. `_apply_confidence` writes only `confidence`, `agents_consulted`, `multi_agent_confirmed` — never `final_verdict` or any `Finding`. Regression: `test_apply_confidence.py` 24/24 + `test_confidence.py` 10/10 (compute_confidence untouched). LIVE collapse e2e (DS-36E093BE, dead-backend forced 100% tribunal collapse, $0 — 0/40 calls): 7 agents connection-error -> 0 contributing -> Confidence LOW (pre-fix would have reported HIGH on zero findings); verdict SOLID UNDER PRESSURE via deterministic fallback; confidence-gated escalation fired once (LOW), failed under the dead backend, and stopped — bounded and honest (the escalation short-circuit on zero coverage is logged as LW-6, out of scope).

### JARP_CERTIFIED: DS v3.20.0 — PA-20260613-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.20.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.19.0 baseline (forensic surface unchanged). Scope: v3.20.0 delta — confidence false-positive on tribunal collapse (LW-5): `_apply_confidence` now grounds `agents_consulted` on contributing (non-errored) agents only, so a 100% collapse yields LOW instead of HIGH over zero analysis; `test_apply_confidence.py` 16->24; atomic banner bump (operator banners main x2 / wizard / transparency report -> v3.20.0; module docstrings frozen). RULE 08 self-audit L0 (PA-20260613-001) PASS first. Functional evidence on the real machine (post-apply + post-bump): `test_apply_confidence.py` 24/24 + `test_confidence.py` 10/10 + LIVE collapse e2e (DS-36E093BE, $0, 0/40 calls): 7 agents connection-error -> Confidence LOW, deterministic-fallback verdict, escalation bounded. The change lives entirely in `_apply_confidence` (post-verdict metadata): writes only confidence/agents_consulted/multi_agent_confirmed; `compute_confidence`, `Finding`, `final_verdict` byte-identical/untouched. Forensic surface (19 variants + 7 skills + base + router CONTENT) byte-identical except stamps. No real-person impersonation; no prompt/skill change. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (deterministic agent-coverage rule, orthogonal to the verdict). Non-forensic orchestrator-layer fix -> CONFIRMATORY re-cert. Supersedes PA-20260612-002 (DS v3.19.0). `JARP_BENCHMARK_LIVE` advances to v3.20.0. Valid until 13/09/2026 or DS v4.0.0. Backlog: LW-5 CLOSED; LW-6 logged (escalation short-circuit when agent coverage is zero — escalating into a dead backend is bounded but wasteful); LW-4 (positional domain tie-break, optional); P5 extension P14/P20.

---

## [3.19.0] - 2026-06-12

### Fixed — Confidence corroboration fragility (LW-2, correctness)
- `orchestrator/tribunal_transversal.py`: `_apply_confidence` cross-agent corroboration was exact-match on `(severity, normalized title)` over RAW agent findings. Two independent agents rarely word a title identically, AND the synthesizer rewrites the unified titles — so unanimous consensus recorded `Confirmed by 2+: 0` and `driver_corroborated=False`, biasing the (NON-BINDING) confidence systematically LOW. TWO divergences closed: (1) intra-raw title divergence between agents; (2) the synthesizer↔raw gap — `driver_corroborated` compared SYNTHESIZER titles against the RAW-title set, two string spaces that never met.
- New corroboration contract (deterministic, NON-BINDING): similarity on `title + evidence` token overlap via the existing `overlap_score` (reused from the provenance layer — same alnum tokenizer, no new infra, no embeddings), threshold `rag.corroboration_min_overlap` (default 4), SAME severity required, with the legacy exact-title match kept as a floor (strict superset → no regression). `driver_corroborated` now compares the synthesizer finding against the corroborated RAW findings by the same similarity, crossing the synthesizer↔raw gap. `evidence` anchors to the document (objective), discriminating "same defect" from shared title scaffolding ("missing X clause" vs "missing Y clause").
- Fix is 100% inside `_apply_confidence`. `compute_confidence` (schema.py), `Finding`, and `final_verdict` are untouched.

### Tests
- `orchestrator/test_apply_confidence.py` (NEW): 16-check offline suite ($0) exercising the REAL `_apply_confidence` via `__new__` (no client/config) — legacy exact-title superset (no regression), divergent-title same-defect now corroborates (the LW-2 bug), synthesizer↔raw gap crossed via the evidence bridge, scaffold guard (different defects sharing "missing/clause/section" do NOT corroborate at threshold 4), same-severity guard, n<2 → LOW, clean n≥3 → HIGH, ≥2 unresolved → LOW despite corroboration, multi-finding-uncorroborated → MODERATE, and `final_verdict` invariance in every case.
- `orchestrator/config.example.json`: `rag.corroboration_min_overlap` (4) declared (code already defaulted).

### Versioning
- Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.19.0 (bump_manual). Product-face (base + router + 19 variants + README + CLAUDE) -> v3.19.0 (bump_stamps). Module docstrings frozen at origin (tribunal v3.0.0; main/wizard v3.10.0). No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Confidence is metadata only (consistent with RULE LG07/F08; Sev×Likelihood NON-BINDING). `_apply_confidence` writes only `confidence`, `agents_consulted`, and `multi_agent_confirmed` — never `final_verdict` or any `Finding`. The deterministic verdict (>=1 FATAL -> INVIABLE) is untouched. Regression: `test_apply_confidence.py` 16/16 + `test_confidence.py` 10/10 (compute_confidence untouched) + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP). LIVE cert-grade e2e (`claude-opus-4-7`, adversarial Legal contract, TRIBUNAL_FULL 10 agents): synthesizer ran LIVE (no fallback), `Confirmed by 2+: 5` + `Conflicts resolved: 5`, verdict INVIABLE (7 FATAL, deterministic), Confidence HIGH legitimately (FATAL tier corroborated, 0 unresolved). Pre-fix this consensus would have recorded ~0 confirmed — the rewritten-title synthesizer↔raw cross (Divergence 2) and the divergent-title intra-agent grouping (Divergence 1) both exercised live.

### JARP_CERTIFIED: DS v3.19.0 — PA-20260612-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.19.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.18.0 baseline (forensic surface unchanged). Scope: v3.19.0 delta — confidence-corroboration fragility fix (LW-2): `_apply_confidence` rewritten to similarity-based corroboration (title+evidence `overlap_score`, `rag.corroboration_min_overlap` default 4, same-severity, legacy exact-title floor), `driver_corroborated` crosses the synthesizer↔raw gap; `test_apply_confidence.py` added (16/16); `corroboration_min_overlap` declared in config.example.json; atomic banner bump (operator banners main x2 / wizard / transparency report -> v3.19.0; module docstrings frozen). RULE 08 self-audit L0 (PA-20260612-001) PASS first. Functional evidence on the real machine (post-apply + post-bump): `test_apply_confidence.py` 16/16 + `test_confidence.py` 10/10 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP) with `c_fallback_intact` + `e_monotonic_verdict` (INVIABLE) + `r2_byo_corpus` (`legacy_byte_identical=True`) PASS; PLUS a LIVE cert-grade e2e on `claude-opus-4-7` (adversarial Legal contract, TRIBUNAL_FULL 10 agents) with the synthesizer running LIVE (no fallback): `Confirmed by 2+: 5`, `Conflicts resolved: 5`, verdict INVIABLE (7 FATAL, deterministic per the Verdict Decision Table), Confidence HIGH legitimately — exercising BOTH the divergent-title intra-agent grouping AND the rewritten-title synthesizer↔raw cross. The change lives entirely in `_apply_confidence` (post-verdict metadata): it writes only confidence/agents_consulted/multi_agent_confirmed; `compute_confidence`, `Finding`, and `final_verdict` are byte-identical/untouched. Forensic surface (19 variants + 7 skills + base + router CONTENT) byte-identical except stamps. No real-person impersonation; no prompt/skill change. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (deterministic similarity rule with same-severity guard + conservative floor, orthogonal to the verdict). Non-forensic orchestrator-layer fix -> CONFIRMATORY re-cert. Supersedes PA-20260611-002 (DS v3.18.0). `JARP_BENCHMARK_LIVE` advances to v3.19.0. Valid until 12/09/2026 or DS v4.0.0. WATCH CLEARED: `b_unified_output` live-model JSON shape — the standing environmental gap from v3.16–v3.18 — was finally exercised by this release's live cert-grade e2e (synthesizer produced a valid UnifiedVerdictOutput live, no fallback). Backlog: LW-5 logged — when the tribunal fails 100% (0 findings), confidence reports HIGH on zero analysis (false-positive observed during the no-credit run); out of LW-2 scope, queued for a future cycle.

---

## [3.18.0] - 2026-06-11

### Fixed — Signal-provenance granularity (LW-3, UX)
- `orchestrator/retriever.py`: `load_corpus_files` gains `txt_atomic_lines` (default False). The signals channel now loads `.txt` ONE PASSAGE PER LINE, so time-sensitive observations on consecutive lines are individually addressable for provenance; the corpus channel keeps the paragraph (blank-line) split, because a clause/law spanning consecutive lines must stay ONE passage for BM25 grounding. Per-channel by construction — the corpus load path is byte-identical.
- `orchestrator/tribunal_transversal.py`: the signals load loop now calls `load_corpus_files(_p, txt_atomic_lines=True)`; the corpus load `load_corpus_files(_byo)` is unchanged (default). Before the fix, signals on consecutive lines collapsed into a single passage and `_attribute_signal_provenance` mapped every finding to one signal index; now each finding attributes to its specific signal line.
- Robustness: a loop-variable shadow in the first draft (`raw = f.read()` inside `for raw in paths`) was renamed to `txt` pre-cert — functionally inert today but a latent footgun, removed before ship.

### Tests
- `orchestrator/test_signals_granularity.py` (NEW): 6-check offline suite ($0) — default `.txt` collapses consecutive lines (legacy preserved); atomic mode = one passage per line; atomic drops blank lines; CORPUS guard (default paragraph/blank-line split keeps a multi-line clause as ONE passage); repro shape (header + blank + 4 consecutive signals: default 2 passages, atomic 6); and an e2e granularity check (two findings over two distinct signal lines attribute to DISTINCT `signal_index`).

### Versioning
- Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.18.0 (bump_manual). Product-face (base + router + 19 variants + README + CLAUDE) -> v3.18.0 (bump_stamps). Module docstrings frozen at origin (retriever.py stays v3.10.0; context_builder/tribunal v3.0.0); feature-landing refs frozen (tribunal provenance v3.15.0). No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-forensic guarantee
- The fix lives entirely in the orchestrator signals-load + post-verdict report layer. The corpus grounding path is byte-identical (`smoke_test_e2e.py` `r2_byo_corpus` reports `legacy_byte_identical=True`). Provenance is deterministic and POST-verdict: it reads the already-final `unified` and writes only the transparency report — it touches neither `final_verdict` nor any `Finding`. The deterministic verdict (>=1 FATAL -> INVIABLE) is untouched. Regression: `test_signals_granularity.py` 6/6 (incl. live e2e distinct-index) + `test_provenance.py` 12/12 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking). Live load-level confirmation: a real `--signals` run reported `Ext.signals: ACTIVE — 6 evidence passage(s)` (atomic split active end-to-end; pre-fix would be 2).

### JARP_CERTIFIED: DS v3.18.0 — PA-20260611-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.18.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.17.0 baseline (forensic surface unchanged). Scope: v3.18.0 delta — signal-provenance granularity (LW-3): `load_corpus_files` `txt_atomic_lines` per-channel `.txt` split (signals per-line; corpus paragraph byte-identical), signals load loop wired with `txt_atomic_lines=True`, loop-variable shadow renamed pre-cert, `test_signals_granularity.py` added (6/6 incl. e2e distinct-index), atomic banner bump (operator banners main x2 / wizard / transparency report -> v3.18.0; module docstrings frozen). RULE 08 self-audit L0 (PA-20260611-001) PASS first. Functional evidence on the real machine (post-apply + post-bump): `test_signals_granularity.py` 6/6 + `test_provenance.py` 12/12 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` (INVIABLE) + `r2_byo_corpus` (`legacy_byte_identical=True`) PASS; plus a live `--signals` run confirming `Ext.signals: ACTIVE — 6 evidence passage(s)` (atomic split active end-to-end). The change lives entirely in the orchestrator signals-load + post-verdict report layer: provenance reads the final `unified` and writes only the report; it computes nothing on the verdict path. Forensic surface (19 variants + 7 skills + base + router CONTENT) byte-identical except stamps; corpus grounding path byte-identical (`r2_byo_corpus`); module docstrings frozen (retriever.py stays v3.10.0). No real-person impersonation; no prompt/skill change. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (per-channel deterministic load + post-verdict auditability hint, orthogonal to the verdict). Non-forensic orchestrator-layer fix -> CONFIRMATORY re-cert. Supersedes PA-20260607-002 (DS v3.17.0). `JARP_BENCHMARK_LIVE` advances to v3.18.0. Valid until 11/09/2026 or DS v4.0.0. WATCH: `b_unified_output` SKIPs in a clean offline shell (no key) and, with a dummy key + offline proxy, PASSes via the deterministic-fallback shape (agents connection-error -> fallback -> valid UnifiedVerdictOutput); the live-model JSON shape remains unexercised — same standing environmental gap as v3.16/v3.17, non-blocking.

---

## [3.17.0] - 2026-06-07

### Fixed — Domain resolver false-match (LW-1, correctness)
- `orchestrator/context_builder.py`: `_resolve_domain` matched DOMAIN_MAP keys as raw substrings of the subscenario, so 2-3 char abbreviation keys ("ma"/"ops"/"hr"/"sop") false-matched any stem merely containing those letters (e.g. "transformation" -> Financial via "ma", "threshold" -> HR via "hr"), mis-routing real documents to the wrong variant / Failure Catalog in --document mode (the subscenario is the filename stem). TWO defects closed: (1) substring bleed; (2) order-dependence — the legacy resolver returned the FIRST substring match in DOMAIN_MAP insertion order, silently coupling routing to dict layout.
- New resolution contract (deterministic, order-invariant): separators (_ - . spaces) normalized; keys evaluated MOST-SPECIFIC FIRST (longest keyword, alphabetical tie-break); short abbreviation keys (<=3 chars) match WHOLE TOKENS only; compound/multi-word keys match as a normalized phrase; longer single-word keys match a whole token OR a token prefix ("cyber" still resolves "cybersecurity"). No key removed. Exact-type fast path unchanged.

### Tests
- `orchestrator/test_domain_resolver.py` (NEW): 23-check offline suite ($0) — LW-1 repro (transformation vs board_proposal), short-key bleed killed (no false Financial/HR/Operations), short keys still match as whole tokens (M&A/ops/hr/nda), long-key prefix tolerance preserved ("cyber"->Cybersecurity), compound/phrase keys (real_estate/series_a/market_entry), exact-type fast path, multi-domain collisions (most-specific wins), no-match -> General.

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.17.0 (bump_stamps). Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.17.0 (bump_manual). Module docstrings frozen at origin (context_builder.py stays v3.0.0). No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-forensic guarantee
- The fix lives entirely in the orchestrator routing layer (pre-verdict): it selects WHICH variant/Failure Catalog loads from the filename stem; it computes nothing on the verdict path. The forensic surface (19 variants + 7 skills + base + router CONTENT) is byte-identical except stamps. The deterministic verdict (>=1 FATAL -> INVIABLE) is untouched. Regression: `test_domain_resolver.py` 23/23 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking); every non-binding layer (confidence/escalation/lenses/signals/provenance/reputational) unchanged.

### JARP_CERTIFIED: DS v3.17.0 — PA-20260607-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.17.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.16.0 baseline (forensic surface unchanged). Scope: v3.17.0 delta — domain-resolver correctness fix (LW-1): `_resolve_domain` rewritten boundary-aware + most-specific-first + order-invariant (substring-bleed and order-dependence closed), `test_domain_resolver.py` added (23/23), atomic §4.14.1 bump (product-face + operator banners main x2 / wizard / transparency report -> v3.17.0; module docstrings frozen). RULE 08 self-audit L0 (PA-20260607-001) PASS first. Functional evidence on the real machine (post-apply + post-bump): `test_domain_resolver.py` 23/23 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` (INVIABLE) + `r2_byo_corpus` PASS. The change lives entirely in the orchestrator routing layer (pre-verdict): it selects WHICH variant/Failure Catalog loads from the filename stem; it computes nothing on the verdict path (`_resolve_domain` is upstream of synthesis). Forensic surface (19 variants + 7 skills + base + router CONTENT) byte-identical except stamps; module docstrings frozen (context_builder.py stays v3.0.0). No real-person impersonation; no prompt/skill change. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (deterministic, order-invariant routing rule, orthogonal to the verdict). Non-forensic orchestrator-layer fix -> CONFIRMATORY re-cert. Supersedes PA-20260606-006 (DS v3.16.0). `JARP_BENCHMARK_LIVE` advances to v3.17.0. Valid until 07/09/2026 or DS v4.0.0.

---

## [3.16.0] - 2026-06-06

### Added - Reputational-risk forensic lens (skill #7, value-add P5)
- `skills/reputational-risk/SKILL.md` (NEW): detection lens for five reputational patterns - misrepresentation/over-claim, broken-promise, stakeholder-betrayal, association-contamination, silence-in-crisis - each with detection + audit signals. Activates in Media (P11), Marketing (P16), Strategy (P19). Detection lens only: it names and detects; severity is bound by the variant Failure Catalog; it never computes or alters the verdict (`VERDICT_IMPACT: NONE`).
- `orchestrator/catalogs.py`: `SKILLS_CATALOG` gains `reputational-risk` (registry-only path entry; no logic).
- `prompts/system_prompt.md`: skill #7 added to the Skills-layer composition map.
- `prompts/system_prompt_marketing.md`: RULE MK05 (broken-promise) + 1 Failure-Catalog row (SERIOUS). Over-claim reuses existing MK04 / unverifiable-claim rows (no duplication).
- `prompts/system_prompt_media.md`: RULES M05 (silence-in-crisis) / M06 (association-contamination) / M07 (over-claim) + 3 Failure-Catalog rows.
- `prompts/system_prompt_strategy.md`: RULES ST05 (stakeholder-betrayal) / ST06 (association-contamination) / ST07 (silence-in-crisis) + 3 Failure-Catalog rows.
- Scope: v1.0.0 binds P11/P16/P19 only; Public Sector (P14) and Startup (P20) are deferred (the lens does not fire where no Failure-Catalog rows bind severity).

### Tests
- `orchestrator/test_reputational_risk.py` (NEW): 14-check offline suite ($0) - SKILL.md structure + five named patterns + `VERDICT_IMPACT: NONE`; `SKILLS_CATALOG` registration + path; activation-subset-binding (active P11/P16/P19 variants carry `[reputational-risk:]` tags); scope discipline (P14/P20 NOT bound); structural no-verdict-impact (markdown-only skill - `reputational` appears in orchestrator/*.py only in `catalogs.py`, never in verdict logic).

### Versioning
- Atomic 4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.16.0 (bump_stamps). Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.16.0 (bump_manual). SKILL.md frozen at v1.0.0; catalogs.py module docstring frozen at origin; feature-landing comments frozen. No verdict-logic change.

### Non-binding guarantee
- The reputational-risk skill is a markdown detection lens. It produces findings; severity is assigned ONLY by the P11/P16/P19 Failure Catalog rows, consistent with each variant's Severity Taxonomy; from there findings feed the deterministic monotonic verdict table like any other finding. The skill computes nothing and references no verdict path (structural guarantee - markdown cannot touch `final_verdict`). The verdict stays severity-driven (>=1 FATAL -> INVIABLE; RULE LG07/F08). Unlike the P1-P4 metadata family, reputational findings carry real catalog-bound severity and CAN sink a verdict - the correct forensic behavior.

### JARP_CERTIFIED: DS v3.16.0 — PA-20260606-006 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.16.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.15.0 baseline (verdict engine unchanged). Scope: v3.16.0 delta — reputational-risk forensic lens (skill #7): `skills/reputational-risk/SKILL.md` (5 patterns — over-claim, broken-promise, stakeholder-betrayal, association-contamination, silence-in-crisis); `SKILLS_CATALOG` registry entry; composition-map bullet in base; 7 domain RULES + 7 Failure-Catalog rows across P11 Media (M05/M06/M07) / P16 Marketing (MK05) / P19 Strategy (ST05/ST06/ST07); `test_reputational_risk.py` added; atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260606-005) PASS first. Functional evidence on the real machine (post-apply): `test_reputational_risk.py` 14/14 + `test_provenance.py` 12/12 + `test_signals.py` 11/11 + `test_archetype_lenses.py` 10/10 + `test_escalation.py` 10/10 + `test_confidence.py` 10/10 + `test_wizard.py` 7/7 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with the full `run()` building the transparency report clean (banner bump verified non-breaking). Skill is a markdown detection lens: it names and detects; severity is bound ONLY by the P11/P16/P19 Failure Catalog (consistent with each Severity Taxonomy); it computes nothing and references no verdict path — structural no-verdict-impact (markdown cannot touch `final_verdict`; `reputational` absent from every orchestrator verdict module). Unlike the P1–P4 metadata family, reputational findings carry real catalog-bound severity and feed the deterministic monotonic table like any other finding; the verdict stays severity-driven (>=1 FATAL -> INVIABLE; RULE LG07/F08). Scope discipline: v1.0.0 binds P11/P16/P19 only; P14/P20 deferred (activation⊆binding enforced by test). No duplication: over-claim in Marketing reuses existing MK04. No real-person impersonation. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (abstract neutral forensic patterns). Non-forensic detection/feed-layer bump → CONFIRMATORY re-cert. Supersedes PA-20260606-004 (DS v3.15.0). `JARP_BENCHMARK_LIVE` advances to v3.16.0. Valid until 06/09/2026 or DS v4.0.0. WATCH: reputational lens through a real model not yet exercised live (`b_unified_output` SKIP — no API key; same environmental gap as escalation/lenses/signals/provenance); non-blocking.

---

## [3.15.0] — 2026-06-06

### Added — Signal-provenance attribution in the transparency report (value-add)
- `orchestrator/retriever.py`: new pure helper `overlap_score(a, b)` — count of DISTINCT shared tokens using the same alnum tokenizer as BM25 retrieval. Used ONLY by the provenance layer; deterministic, no API, no network.
- `orchestrator/tribunal_transversal.py`: signals are now loaded path-tagged (`_active_signals_tagged = [(source, passage)]`); the agent feed (`_active_signals`) is the SAME passage list projected, so the P4 feed stays byte-identical. New `_attribute_signal_provenance(unified)` attributes each consolidated Finding (evidence + description) to the external signal passage it most overlaps, above a configurable floor; results surface as a `SIGNAL PROVENANCE` block in the transparency report. Computed POST-verdict in `run()`.
- `orchestrator/config.example.json`: `rag.provenance_min_overlap` (3) — attribution floor; below it a finding is left unattributed (prefer no attribution over stopword noise).

### Tests
- `orchestrator/test_provenance.py` (NEW): 12-check offline suite ($0) — overlap_score correctness (shared/disjoint/case), no-signals graceful empty, right-source attribution, floor honored + configurable, best-overlap wins, record shape (severity/source/snippet), multi-tier spread, and a GOLDEN independence check (attribution mutates neither `final_verdict` nor the findings).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.15.0 (bump_stamps). Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.15.0 (bump_manual). Module/feature docstrings frozen at origin. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Provenance runs POST-verdict: it reads the already-final `unified` and writes only the transparency report; it touches neither `final_verdict` nor any `Finding`. The verdict stays severity-driven (>=1 FATAL -> INVIABLE; RULE LG07/F08). The golden check in `test_provenance.py` proves verdict + findings invariance; smoke `e_monotonic_verdict` + `c_fallback_intact` stay green. Attribution is a heuristic auditability hint ("likely originating signal"), explicitly NOT causal proof.

### JARP_CERTIFIED: DS v3.15.0 — PA-20260606-004 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.15.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.14.0 baseline (forensic surface unchanged). Scope: v3.15.0 delta — signal-provenance attribution (`overlap_score` pure helper; path-tagged signals load with byte-identical agent feed; `_attribute_signal_provenance` post-verdict token-overlap with configurable `rag.provenance_min_overlap` floor; `SIGNAL PROVENANCE` transparency-report block), `test_provenance.py` added, atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260606-003) PASS first. Functional evidence on the real machine (post-apply): `test_provenance.py` 12/12 (incl. GOLDEN independence) + `test_signals.py` 11/11 + `test_archetype_lenses.py` 10/10 + `test_escalation.py` 10/10 + `test_confidence.py` 10/10 + `test_wizard.py` 7/7 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with the full `run()` building the transparency report clean. Verdict invariant verified: provenance reads the final verdict and writes only the report; `final_verdict` and findings unchanged (golden check); the verdict stays severity-driven. No real-person impersonation. Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (provenance is a post-verdict auditability hint, orthogonal to the verdict). Non-forensic feed/report-layer bump. Supersedes PA-20260606-002 (DS v3.14.0). `JARP_BENCHMARK_LIVE` advances to v3.15.0. Valid until 06/09/2026 or DS v4.0.0. WATCH: live signals injection + provenance through a real model not yet exercised (`b_unified_output` SKIP — no API key; same environmental gap as escalation/lenses/signals); non-blocking.

---

## [3.14.0] — 2026-06-06

### Added — External-signals evidence channel (value-add P4)
- `orchestrator/retriever.py`: `build_agent_context` gains a `signals`/`signals_top_k` channel — a DISTINCT, separately-labelled feed `[EXTERNAL SIGNALS - TIME-SENSITIVE EVIDENCE]` injected after the `[JURISDICTIONAL CORPUS - REFERENCE GROUNDING]` block, budget-aware, with `drop_zero_overlap=True` (pure-noise passages never injected). The in-band directive states signals are EVIDENCE that MAY substantiate a Finding under the normal severity rule — NOT a verdict input — so the channel needs no `prompt_engine` change. Reuses `load_corpus_files` + the BM25 `Retriever` (no new infra, no network).
- `orchestrator/schema.py`: `RuntimeContext.signals_paths` (BYO per-case; None = no signals). Distinct from `corpus_paths`: corpus GROUNDS, signals are time-sensitive EVIDENCE.
- `orchestrator/main.py`: new `--signals <path...>` flag (same formats as `--corpus`) wired into both case dicts via `signals_paths`.
- `orchestrator/context_builder.py`: passthrough `signals_paths`.
- `orchestrator/tribunal_transversal.py`: loads signals via `load_corpus_files(ctx.signals_paths)`, feeds them into every agent's doc context, and surfaces an `Ext.signals` provenance line in the transparency report.
- `orchestrator/wizard.py`: optional step 8 "Attach external signals?" -> synthesizes `--signals`, delegates to the same parser.
- `orchestrator/config.example.json`: `rag.signals_top_k` (3) declared (code already defaulted).

### Tests
- `orchestrator/test_signals.py` (NEW): 11-check offline suite ($0) — legacy byte-identical degradation, distinct EXTERNAL-SIGNALS label, in-band non-binding directive, relevant-signal inclusion, zero-overlap rejection, corpus+signals coexistence + ordering, tiny-budget safety, channel separation, and a GOLDEN invented-causality check (>=1 FATAL -> INVIABLE, severity-driven and signal-independent).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.14.0. Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.14.0. Module/feature docstrings + lens catalog frozen at origin. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Signals only alter `build_agent_context` (the text agents read). The verdict is computed from Findings in `_synthesize`/`_deterministic_synthesis`, which never see signals — so the channel is STRUCTURALLY incapable of altering `final_verdict` (severity-driven: >=1 FATAL -> INVIABLE; consistent with RULE LG07/F08). Regression confirms `e_monotonic_verdict` + `c_fallback_intact` green; the golden check proves verdict invariance.

### JARP_CERTIFIED: DS v3.14.0 — PA-20260606-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.14.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.13.0 baseline (19/19 unchanged). Scope: v3.14.0 delta — external-signals evidence channel (`build_agent_context` signals feed: distinct `[EXTERNAL SIGNALS]` label + in-band non-binding directive + `drop_zero_overlap`; `RuntimeContext.signals_paths`; `--signals` flag in both case dicts; ContextBuilder passthrough; tribunal load + feed + transparency provenance; wizard step 8; `rag.signals_top_k`), `test_signals.py` added, atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260606-001) PASS first. Functional evidence on the real machine (post-apply): `test_signals.py` 11/11 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` + `r2_byo_corpus` PASS; full pipeline imports clean. One robustness defect caught/fixed pre-cert — the v1 edit script wrote each edit from the original file snapshot, clobbering multi-edit files to the last edit only (NameError `has_signals`); fixed by chaining edits per file on the evolving text + re-applied clean (14 edits / 6 files). Verdict invariant verified: signals only shape the agent-facing context; the verdict path never sees signals (golden check); `final_verdict` stays severity-driven. No real-person impersonation. Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (signals are a deliberation-evidence enrichment, orthogonal to the verdict). Non-forensic feed-layer bump. Supersedes PA-20260605-002 (DS v3.13.0). `JARP_BENCHMARK_LIVE` advances to v3.14.0. Valid until 06/09/2026 or DS v4.0.0. WATCH: live signals injection through a real model not yet exercised (`b_unified_output` SKIP — no API key; same environmental gap as escalation/lenses); non-blocking.

---

## [3.13.0] — 2026-06-05

### Added — Archetype lenses for the escalation round (value-add P2)
- `orchestrator/archetype_lenses.py` (NEW): frozen catalog of 5 abstract adversarial lenses (FALSIFIER, FAILURE_MODE_HUNTER, EVIDENCE_AUDITOR, INCENTIVE_AUDITOR, SYSTEMIC_LENS) + pure helpers `select_lenses(n)` (deterministic; returns dict copies so the catalog can never be mutated by a caller) and `build_lens_directive(lens, round_no, focus)`. No API, no I/O. Lenses are ABSTRACT roles — never an impersonation of a real person (fabricated authority forbidden by design).
- `orchestrator/tribunal_transversal.py`: `_run_escalation_round` now assigns one archetype lens per `FOR-ESC-*` agent (deterministic order; the first complementary pair — refute-first + extend-first — runs under the default `max_escalation_agents=2`). Each lens shapes HOW the agent re-examines the verdict-driving findings; `FOR-ESC-*` ids preserved so cross-agent corroboration counts them as independent. `result["lens"]` tagged; `_maybe_escalate` records applied lenses; the transparency report surfaces them. `build_lens_directive(None, …)` degrades to a neutral directive when agents exceed the catalog, so offline/no-API runs never crash.
- Catalog + module docstring are content-based/frozen (do not bump every minor).

### Tests
- `orchestrator/test_archetype_lenses.py`: 10-check offline suite (catalog integrity, order contract, `select_lenses` cap/degenerate/coercion/determinism/isolation, `build_lens_directive` embedding + graceful degradation). No API.

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.13.0. Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.13.0. Module/feature docstrings + lens catalog frozen at origin. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Lenses change deliberation quality, never the verdict. Escalation remains a deliberation-budget decision (consistent with RULE LG07/F08); the deterministic verdict (FATAL->INVIABLE) is untouched. Regression confirms `e_monotonic_verdict` + `c_fallback_intact` green and the gate's no-op paths never touch the synthesizer.

### JARP_CERTIFIED: DS v3.13.0 — PA-20260605-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.13.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.12.0 baseline (19/19 unchanged). Scope: v3.13.0 delta — archetype lenses (`archetype_lenses.py` NEW: 5 abstract lenses + pure `select_lenses`/`build_lens_directive`; one lens per `FOR-ESC-*` agent in `_run_escalation_round`; `result["lens"]` + `_maybe_escalate` lens record + transparency surfacing; graceful None-lens degradation), `test_archetype_lenses.py` added, atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260605-001) PASS first. Functional evidence on the real machine (post-apply): `test_archetype_lenses.py` 10/10 + `test_escalation.py` 10/10 + `test_confidence.py` 10/10 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` PASS; full pipeline imports `tribunal`->`archetype_lenses` clean. Verdict invariant verified: lenses only shape escalation directives + tag provenance; `final_verdict` stays severity-driven; escalation gate no-op paths never invoke synthesis. No real-person impersonation in the catalog (abstract roles only). Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (lenses are a deliberation-quality enrichment, orthogonal to the verdict). Supersedes PA-20260604-004 (DS v3.12.0). `JARP_BENCHMARK_LIVE` advances to v3.13.0. Valid until 05/09/2026 or DS v4.0.0.

---

## [3.12.0] — 2026-06-04

### Added — Confidence-gated escalation (value-add P1)
- `orchestrator/schema.py`: new `should_escalate(confidence, rounds_done, max_rounds, remaining_agents, enabled)` — pure deterministic gate. NON-BINDING: decides only whether to spend more deliberation; never alters `final_verdict` (severity-driven: >=1 FATAL -> INVIABLE).
- `orchestrator/tribunal_transversal.py`: `_maybe_escalate` hooked after synthesis. When `confidence == LOW` and agent budget remains, runs a bounded extra forensic pass (`_run_escalation_round`, distinct `FOR-ESC-*` ids so cross-agent corroboration counts them as independent) on the verdict-driving findings, re-synthesizes, and recomputes confidence. Capped at `max_escalation_rounds`. Degrades gracefully (errors captured) so offline/no-API runs never crash.
- Confidence may remain LOW after escalating (honest — never inflated). Builds directly on P3's deterministic confidence.
- `orchestrator/main.py` + `config.example.json`: `escalation_enabled` (true), `max_escalation_rounds` (1), `max_escalation_agents` (2).
- Transparency report surfaces a CONFIDENCE block (level + escalation status: triggered/rounds/before->after).

### Tests
- `orchestrator/test_escalation.py`: 10-case offline truth table for `should_escalate` (no API).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.12.0. Operator-visible orchestrator banners (main/wizard/transparency report) -> v3.12.0. Module/feature docstrings frozen at origin. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Escalation is a deliberation-budget decision, not a verdict input (consistent with RULE LG07/F08; confidence NON-BINDING). The deterministic verdict (FATAL->INVIABLE) is untouched; regression confirms `e_monotonic_verdict` + `c_fallback_intact` green, and the gate's no-op paths never touch the synthesizer.

### JARP_CERTIFIED: DS v3.12.0 — PA-20260604-004 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.12.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.11.0 baseline (19/19 unchanged). Scope: v3.12.0 delta — confidence-gated escalation (`should_escalate` pure gate + `_maybe_escalate`/`_run_escalation_round` hooked after synthesis; bounded extra forensic round on LOW confidence, distinct `FOR-ESC-*` ids, re-synthesize + recompute; capped at `max_escalation_rounds`; budget-gated; graceful offline degradation), `test_escalation.py` added, escalation config keys, atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260604-003) PASS first. Functional evidence on the real machine (post-bump): `test_escalation.py` 10/10 + `test_confidence.py` 10/10 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` PASS. Verdict invariant verified: escalation gate no-op paths never invoke synthesis and never alter `final_verdict` (severity-driven). Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (escalation is a deliberation-budget decision, orthogonal to the verdict). Non-forensic confirmatory bump. Supersedes PA-20260604-002 (DS v3.11.0). `JARP_BENCHMARK_LIVE` advances to v3.12.0. Valid until 04/09/2026 or DS v4.0.0.

---

## [3.11.0] — 2026-06-04

### Added — Deterministic auditable confidence (value-add P3)
- `orchestrator/schema.py`: new `compute_confidence(agents_consulted, driver_corroborated, driver_finding_count, unresolved_conflicts)` — pure, deterministic, NON-BINDING. Never alters `final_verdict` (severity-driven: >=1 FATAL -> INVIABLE).
- `orchestrator/tribunal_transversal.py`: confidence now computed in BOTH synthesis paths (`_synthesize` LLM + `_deterministic_synthesis` fallback) via new `_apply_confidence`. Replaces the fallback's hardcoded `"MODERATE"` and the LLM's free-form self-assessment with a derived value.
- `agents_consulted` and `multi_agent_confirmed` are now grounded deterministically from cross-agent corroboration (the fallback previously left them empty).
- Rule: LOW if <2 agents, or the verdict hinges on a single uncorroborated finding, or >=2 unresolved clashes; HIGH if >=3 agents, 0 unresolved clashes, and the verdict-driving tier is clean or multi-agent-confirmed; MODERATE otherwise.

### Changed — transparency
- Verdict + transparency report label confidence as a NON-BINDING auditability signal (corroboration/conflict), explicitly not a probability of real-world success or efficiency guarantee.

### Tests
- `orchestrator/test_confidence.py`: 10-case offline truth table for `compute_confidence` (no API).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.11.0. Operator-visible orchestrator banners (main/wizard/transparency report) -> v3.11.0. Module docstrings frozen at architecture origin unchanged. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Confidence is metadata only (consistent with RULE LG07/F08; Sev×Likelihood NON-BINDING). The deterministic verdict (FATAL->INVIABLE) is untouched; regression confirms `e_monotonic_verdict` + `c_fallback_intact` green.

### JARP_CERTIFIED: DS v3.11.0 — PA-20260604-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.11.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.10.0 baseline (19/19 unchanged). Scope: v3.11.0 delta — deterministic auditable confidence (`compute_confidence` + `_apply_confidence` wired into BOTH synthesis paths; `agents_consulted` + `multi_agent_confirmed` grounded deterministically), NON-BINDING (never alters the severity-driven FATAL->INVIABLE verdict; consistent with RULE LG07/F08), `test_confidence.py` added, atomic §4.14.1 bump (product-face + operator-visible orchestrator banners -> v3.11.0; module docstrings frozen at origin). RULE 08 self-audit L0 (PA-20260604-001) PASS first. Functional evidence on the real machine (post-bump): `test_confidence.py` 10/10 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` PASS. Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (confidence rule symmetric, orthogonal to verdict). Non-forensic confirmatory bump. Supersedes PA-20260603-006 (DS v3.10.0). `JARP_BENCHMARK_LIVE` advances to v3.11.0. Valid until 04/09/2026 or DS v4.0.0.

---

## [3.10.0] — 2026-06-03

### Added — BYO per-case reference corpus (roadmap: corpus R2, re-scoped)
- Re-scoped corpus R2 from "pre-load laws per jurisdiction" (does not scale) to a BYO per-case mechanism. The repo holds no laws; the operator attaches reference texts for their own case via `--corpus`.
- `orchestrator/retriever.py`: new `load_corpus_files(paths)` — loads `.jsonl/.txt/.md` directly and PDF/DOCX/PPTX/XLSX/HTML via UNIT-INGEST (markitdown, lazy) + chunk. Any jurisdiction; nothing pre-loaded.
- `orchestrator/main.py`: new `--corpus <path...>` flag (nargs) wired into both case dicts via `corpus_paths`.
- `orchestrator/wizard.py`: optional step 7 "Attach reference texts?" → synthesizes `--corpus`, delegates to the same parser (s23 pattern).
- `orchestrator/{schema,context_builder,tribunal_transversal}.py`: additive `corpus_paths` + passthrough + BYO branch (`load_corpus_files` if BYO, else `load_corpus(ctx.corpus)` map fallback; empty -> no-op). `JURISDICTION_CORPUS_MAP` stays `{}` (optional hook).

### Changed — R2 relevance floor (anti-noise)
- R2 floor switched from BM25-score to TOKEN-OVERLAP (`query(..., drop_zero_overlap=True)`). A score floor false-negatives on tiny corpora (BM25 IDF=0 for relevant terms); overlap is robust to corpus size. R1 path unchanged (default `False`, byte-identical).

### Dependencies
- `+ pydantic>=2.0.0` (orchestrator/requirements.txt) — was transitive via anthropic; now declared (closes pre-existing LATENT).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.10.0 (23 files, 69 stamp lines). No prompt/skill CONTENT changed; no roster/verdict-logic change. Skills 6, domains 20 (unchanged).

### Non-forensic guarantee
- v3.10.0 touches the orchestrator feed-layer only. Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. "corpus R2" roadmap item CLOSED as a MECHANISM (BYO operator input), not repo-curated data.

### JARP_CERTIFIED: DS v3.10.0 — PA-20260603-006 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.10.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.9.0 baseline (19/19 unchanged). Scope: v3.10.0 delta — BYO per-case corpus (`--corpus`, `load_corpus_files`, wizard step 7, `corpus_paths`), R2 token-overlap floor, `pydantic>=2.0.0`, atomic §4.14.1 barrido (23 files, 69 lines). RULE 08 self-audit L0 (PA-20260603-005) PASS first. Functional evidence on the real machine: `test_wizard.py` 7/7 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) + `byo_check.py` GREEN (BYO loader + R2 injection + overlap-floor noise rejection + byte-identical legacy, live BM25, no key). One robustness defect caught/fixed pre-cert — initial BM25-score floor false-negatived on tiny corpora (IDF=0); switched to token-overlap. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. Non-forensic feed-layer bump. Supersedes PA-20260603-004 (DS v3.9.0). `JARP_BENCHMARK_LIVE` advances to v3.10.0. Valid until 03/09/2026 or DS v4.0.0.

---

## [3.9.0] — 2026-06-03

### Added — Interactive Wizard CLI (roadmap v3.9.0)
- New `orchestrator/wizard.py`: guided interactive flag builder for non-technical operators (closes the KIMI/Copilot gap). Pure `build_command(answers)` (deterministic, unit-tested) + `run_wizard()` (the only I/O). Walks domain (20) -> canonical `--type` token, Legal sub-area drill-down (L01-L12), subscenario, objective, regime (7), Tribunal (auto/1/3/5/7), SSM (MICRO/MESO/MACRO). Emits the equivalent `python main.py ...` command and offers to run it.
- `main.py`: new `--wizard` flag. The wizard SYNTHESIZES argv and re-parses it through the SAME argparse parser, so the guided path is byte-for-byte equivalent to manual flags. No existing path altered.
- New `orchestrator/test_wizard.py`: 5-case unit suite over `build_command`.

### Fixed — D-v38-01 (LATENT carried from the v3.8.0 cert)
- `orchestrator/retriever.py`: `build_agent_context` default `doc_top_k` aligned 5 -> 6 to match config/orchestrator (config was authoritative; the "next retriever touch" the v3.8.0 cert flagged). `query(top_k=5)` left untouched (out of scope). Module docstring left at v3.8.0 (content-based).

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.9.0 (23 files, 69 stamp lines). No prompt/skill CONTENT changed; no roster/verdict-logic change. Skills 6, domains 20 (unchanged).

### Non-forensic guarantee
- v3.9.0 touches the orchestrator product-face only. The forensic surface (19 variants + 6 skills + base + router CONTENT) is byte-identical except version stamps.

### JARP_CERTIFIED: DS v3.9.0 — PA-20260603-004 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.9.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.8.0 baseline (19/19 unchanged). Scope: v3.9.0 delta — `wizard.py` (NEW), `test_wizard.py` (NEW), `main.py --wizard`, `retriever.py` doc_top_k alignment (D-v38-01), atomic §4.14.1 stamp barrido. RULE 08 self-audit L0 (PA-20260603-003) PASS first. Functional evidence: `test_wizard.py` 5/5 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, needs live key — non-blocking) + interactive wizard flow validated live (correct argv, re-parse parity). Three doc-consistency findings caught and resolved pre-cert — D-v39-01 (MODERATE, CLAUDE.md bottom status `ACTIVE — v3.8.0` not caught by the anchored stamp pass) + D-v39-02 (MODERATE, CLAUDE.md repo tree missing wizard.py/test_wizard.py) + D-v39-03 (LATENT, README+CLAUDE roadmap tables missing the v3.9.0 row). Prior LATENT D-v38-01 CLOSED. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS`. Non-forensic bump. Supersedes PA-20260603-002 (DS v3.8.0). `JARP_BENCHMARK_LIVE` advances to v3.9.0. Valid until 30/08/2026 or DS v4.0.0.

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
