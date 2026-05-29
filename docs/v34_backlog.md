# DARK STRATEGIST — BACKLOG SPRINT v3.4

**Abierto:** 29/05/2026 (sesión 13) | **Estado:** OPEN — scope-locked
**Tema:** Reliability core — fidelidad del pipeline AFO→Tribunal→N2 (fix telephone-game / context degradation)
**Bump objetivo:** v3.3.0 → v3.4.0 (operación ATÓMICA de cierre, método s12)
**Cert objetivo:** re-cert 7-axis Level 1 JARP DEEP full-coverage post-bump
**Fuente verificada:** `Agent-Skills-for-Context-Engineering/skills/context-degradation` (v2.1.0) + skills adyacentes `context-compression`, `multi-agent-patterns`

---

## PROBLEMA

El pipeline DS pasa contexto a través de capas: N0 (AFO) → N1 (Tribunal Transversal: Rol + Forense, paralelos y ciegos entre sí) → N2 (sub-agents) → de vuelta a VerdictSynthesizer. Cada handoff implica re-resumen → **pérdida de fidelidad acumulada (telephone-game)**. En términos de los 5 patrones de la skill fuente:

- **lost-in-middle:** prompts largos (base 23 KB, variants) entierran misión/constraints/criterios en posiciones de baja atención (curva U).
- **poisoning:** un claim erróneo de tool/retrieval que entra en N2 se auto-refuerza aguas abajo (corrección por capas no funciona; hay que truncar).
- **clash:** Rol vs Forense producen salidas correctas-pero-contradictorias; sin reglas de precedencia explícitas, el VerdictSynthesizer resuelve de forma impredecible (silent pick).
- **distraction / confusion:** contexto pre-cargado vs just-in-time; mezcla de objetivos entre capas.

## SCOPE v3.4 — Rebanada 1 (Reliability core)

| ID | Ítem | Patrón | Criterio de aceptación |
|----|------|--------|------------------------|
| **R1** | **Handoff fidelity contract N0→N1→N2** — schema acotado (verified claims + provenance + open questions) en cada transición; ninguna capa re-resume el contexto crudo upstream, solo el schema. | compress / telephone-game | Schema de handoff definido y documentado; cada transición de capa consume SOLO el schema, no el raw upstream. |
| **R2** | **Placement curva-U en prompts** — misión/constraints al inicio, criterios de veredicto al final; anchors estructurales en el medio. | lost-in-middle | base + 19 variants colocan mission/constraints al inicio y verdict-criteria al cierre; check añadido a self-audit §4.14. |
| **R3** | **Clash annotation en reconciliación Tribunal** — VerdictSynthesizer marca contradicciones Rol↔Forense con fuente + precedencia ANTES de sintetizar. | clash | Synthesizer emite anotación estructurada de conflicto (qué, fuente, precedencia); prohibido silent pick. |
| **R4** | **Circuit-breaker de poisoning en N2** — validar tool/retrieval antes de entrar a contexto; trackear provenance; recovery = truncar (no layering). | poisoning | AAD/Spawner registra provenance de claims; protocolo de recovery = truncate-to-before, no corrección encima. |
| **R5** | **Umbrales de degradación en BudgetController** — trigger de compaction a ~70% del onset del modelo, no al límite. | non-linear cliff | Trigger de compaction documentado y cableado a límites (calls=40, n2_per_n1=3); re-benchmark trimestral anotado. |

**Transversal:** self-audit §4.14 gana checks nuevos (A-series) para R1–R5. La filosofía de versionado dual sigue vigente: solo cara-de-producto + variants bumpean a v3.4.0; docstrings de módulo conservan su content-version salvo cambio real de contenido.

## FUERA DE SCOPE (diferido)

- 4× Bajo (markitdown UNIT-INGEST, fact-checker UNIT-FACTCHECK, stop-slop AFO post-proc, marketingskills UNIT-PSYCH) → rebanada v3.4 posterior.
- Wizard CLI → rebanada UX propia.
- knowledge-work-plugins (legal+finance matrices) → Medio, posterior.
- infinity + RAG jurisdiccional → **v4.0** (Docker + corpus, infra pesada). NO mezclar.

## MÉTODO (validado s12)

clon en sandbox del remote HEAD → diseño por ítem → implementación con asserts de unicidad → patch único `git apply` → dry-run en clon fresco → JARP commit/push vía GitHub Desktop → post-push verify por SHA. Bump = operación atómica única al cierre del sprint.

## RIESGO / BLAST-RADIUS

**ALTO.** Toca el core (AFO, tribunal_transversal.py, VerdictSynthesizer, BudgetController) + base/variant prompts. Mitigación: diseño + GO por ítem, sin big-bang; sub-commits permitidos durante el sprint pero el bump de versión es atómico al cierre. R3 y R4 son los de mayor riesgo (lógica de síntesis y spawning).

## PASOS SIGUIENTES (esperan GO)

1. **[GO requerido]** Diseño R1: leer `orchestrator/tribunal_transversal.py` + sección AFO de `system_prompt.md` + lógica de VerdictSynthesizer para localizar los puntos exactos de handoff y pérdida. (Lectura de fuente — no inventar dónde fuga.)
2. Definir el handoff schema y validarlo contra un caso real.
3. Continuar R2→R5 secuencial con GO entre ítems.
