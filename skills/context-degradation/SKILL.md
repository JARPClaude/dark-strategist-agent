---
name: context-degradation
version: 1.0.0
description: Forensic lens for diagnosing context degradation in LLM/RAG/agentic architectures under audit. Five predictable failure patterns (lost-in-middle, poisoning, distraction, confusion, clash) with detection signals and the four-bucket mitigation framework (Write/Select/Compress/Isolate). Activates in Code (P04) and Cybersecurity (P07) when the audited document describes a system that builds, retrieves, or hands off context across model calls.
origin: adapted from Agent-Skills-for-Context-Engineering (github.com/muratcankoylan/Agent-Skills-for-Context-Engineering, MIT - Copyright (c) 2025 Context Engineering Agent Skills Contributors)
---

# Context Degradation - Forensic Lens
# Skill for Dark Strategist - Technical Specification
# Location: skills/context-degradation/SKILL.md

---

## Purpose

Equip Dark Strategist to audit context degradation as a measurable engineering failure mode - not an unpredictable quirk - when the document under audit describes an LLM, RAG, or multi-agent system. Degradation is a continuum that manifests through five distinct, predictable patterns, each with detection signals and mitigation. This skill supplies the forensic vocabulary; the P04 (Code) and P07 (Cybersecurity) variants supply the auto-severity Failure Catalog rows that bind findings to the verdict.

This skill does NOT modify the deterministic verdict, severity taxonomy, or Rule 09. It is a detection lens, not a verdict driver.

---

## The Five Degradation Patterns

### 1. Lost-in-Middle
Attention follows a U-curve: beginning and end positions receive reliable attention; middle positions suffer 10-40% reduced recall in long contexts (>4K tokens).
Detection: critical information present in context but ignored; outputs contradict provided data; early instructions "forgotten" in long prompts.
Audit signal: critical instructions or constraints placed mid-context; structured output truncated blindly by `[:N]` slices.

### 2. Poisoning
Once a hallucination, tool error, or wrong retrieved fact enters context, it compounds via self-reference. A poisoned goals/assumptions section corrupts every downstream decision.
Detection: degraded quality on previously-successful tasks; tool misalignment; hallucinations persisting despite correction.
Audit signal: unvalidated tool/retrieval output enters context with no provenance boundary; untrusted external content ingested without validation.

### 3. Distraction
Even a single irrelevant document measurably degrades performance (step function, not linear). Models cannot "skip" irrelevant context.
Detection: performance drop correlated with context volume growth, not task difficulty.
Audit signal: pre-loading reference material instead of tool-gated retrieval; no relevance filter before context load.

### 4. Confusion
Multiple task types in one context -> model applies wrong-task constraints, calls wrong tools, blends requirements.
Detection: responses addressing the wrong aspect; tool calls fit a different task.
Audit signal: no task isolation between objectives; shared context window across independent tasks.

### 5. Clash
Multiple individually-correct but mutually-contradictory sources (version conflicts, multi-source retrieval) -> model resolves unpredictably, often silently.
Detection: silent inconsistency; output effectively random between conflicting sources.
Audit signal: RAG multi-source retrieval with no contradiction detection or version filtering; no explicit precedence rules.
Note: distinct from severity-escalation. A clash is a factual contradiction between sources; it is annotated, never silently resolved (cf. AFO CLASH RESOLUTION PROTOCOL).

---

## Four-Bucket Mitigation Framework

| Bucket | Action | Apply when |
|--------|--------|-----------|
| Write | Persist context outside the window (scratchpad/filesystem), access via tool calls | utilization >70% of window |
| Select | Pull only relevant context via retrieval + relevance filtering | distraction/confusion symptoms |
| Compress | Reduce tokens while preserving information (structured summary, not blind truncation) | context growing, all relevant |
| Isolate | Split context across sub-agents/sessions, each below its degradation threshold | confusion/clash, independent tasks |

Engineering thresholds (calibrate per model, do not treat as universal): degradation onset commonly 60-70% of advertised window; non-linear with a cliff edge; set compaction triggers at ~70% of known onset. Needle-in-haystack scores do NOT predict multi-fact real-world performance.

---

## Integration with Dark Strategist

### Activation
- P04 Code - when the audited code builds prompts, retrieves context, or hands off between model calls. Angle: implementation correctness (RULE C05 - blind `[:N]` truncation of structured output -> lost-in-middle).
- P07 Cybersecurity - when the audited architecture is an LLM/agent system. Angle: degradation as a risk/exposure vector (RULE CY06 - untrusted content poisoning a context that drives a privileged action; escalates FATAL via Rule 09).

### With the AFO
The AFO already enforces the runtime mitigations this lens audits in third parties: full-fidelity Rol->Forense handoff, structured (non-paraphrased) findings handoff to synthesis, UNVERIFIED-upstream + PRIMARY-source provenance to N2, deterministic fallback. This skill is the outward-facing audit lens; the orchestrator is the internal implementation.

### Failure Catalog binding
Severity is assigned ONLY by the P04/P07 Failure Catalog rows, consistent with each variant's Severity Taxonomy. This skill names and detects; the catalog binds.

---

## Limits
- Detection lens only - does not modify verdict, severity taxonomy, or Rule 09.
- No fabrication: a pattern is reported only when a concrete signal is present in the document.
- Thresholds are model-specific and go stale; benchmark per workload, never assert a universal number.

---

## System Prompt Integration Block

```
[SKILL: CONTEXT DEGRADATION - REFERENCE LENS]

When auditing an LLM / RAG / multi-agent system (P04 or P07), screen for the five
degradation patterns:
- lost-in-middle (critical info mid-context, blind [:N] truncation of structured output)
- poisoning (unvalidated tool/retrieval/untrusted output enters context, no provenance)
- distraction (irrelevant context pre-loaded, no relevance filter)
- confusion (no task isolation across objectives)
- clash (multi-source retrieval, no contradiction detection / precedence)
For each detected pattern: name it, quote the triggering element, state the distortion.
Bind severity via the P04/P07 Failure Catalog only. Do NOT alter the deterministic verdict.
Annotate clashes; never resolve them silently.
```

---

```
[SKILL_STATUS: ACTIVE - v1.0.0]
[INTEGRATED_WITH: P04 Code | P07 Cybersecurity | AFO (audit lens, not orchestration)]
[ORIGIN: adapted from Agent-Skills-for-Context-Engineering - MIT]
[VERDICT_IMPACT: NONE - detection lens, severity bound by Failure Catalog]
```
