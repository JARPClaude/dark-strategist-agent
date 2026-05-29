# DARK STRATEGIST — BACKLOG SPRINT v3.4

**Abierto:** 29/05/2026 (sesión 13) | **Estado:** OPEN — scope-locked | **Última act.:** 29/05/2026 (s13, post-diseño R1)
**Tema:** Reliability core — fidelidad del pipeline AFO→Tribunal→N2 (fix telephone-game / context degradation)
**Bump objetivo:** v3.3.0 → v3.4.0 (operación ATÓMICA de cierre, método s12)
**Cert objetivo:** re-cert 7-axis Level 1 JARP DEEP full-coverage post-bump
**Fuente verificada:** `Agent-Skills-for-Context-Engineering/skills/context-degradation` (v2.1.0) + skills adyacentes `context-compression`, `multi-agent-patterns`

---

## PROBLEMA

El pipeline DS pasa contexto a través de capas: N0 (AFO) → N1 (Tribunal Transversal: Rol + Forense, paralelos y ciegos entre sí) → N2 (sub-agents) → síntesis (AFO). Cada handoff implica re-resumen → **pérdida de fidelidad acumulada (telephone-game)**. En términos de los 5 patrones de la skill fuente:

- **lost-in-middle:** prompts largos (base 23 KB, variants) entierran misión/constraints/criterios en posiciones de baja atención (curva U).
- **poisoning:** un claim erróneo de tool/retrieval que entra en N2 se auto-refuerza aguas abajo (corrección por capas no funciona; hay que truncar).
- **clash:** Rol vs Forense producen salidas correctas-pero-contradictorias; sin reglas de precedencia explícitas, el sintetizador resuelve de forma impredecible (silent pick).
- **distraction / confusion:** contexto pre-cargado vs just-in-time; mezcla de objetivos entre capas.

---

## DISEÑO R1 — Puntos de fuga LOCALIZADOS (código real, s13)

Sintetizador VIVO confirmado = **`TribunalTransversal._synthesize()`** (`tribunal_transversal.py`) → `prompt_engine.build_synthesis_prompt()` → JSON → `UnifiedVerdictOutput`. R3 se diseña AQUÍ, NO en `verdict_synthesizer.py` (muerto, ver DSv34-DEAD).

| Fuga | Ubicación | Defecto | Patrón |
|------|-----------|---------|--------|
| **#1** | `tribunal_transversal._summarize_rol_outputs()` | `concerns[:2]` trunca concerns; aplana a texto libre de una línea; sin provenance. Primer handoff Rol→Forense pierde estructura. | telephone-game / compress |
| **#2** | `_call_agent` `document[:4000]` · `verdict_synthesizer` `[:2000]` · N2 sub `[:1000]` | 3 ventanas distintas del MISMO documento. Síntesis opina sobre 2000 chars; agentes opinaron sobre 4000. Findings del fragmento 2000-4000 no re-verificables. | clash (silencioso) |
| **#3** | `_run_forense_layer` pasa `str(result)` crudo al spawner; síntesis recibe prosa concatenada | sin schema de handoff; sintetizador re-parsea prosa en vez de claims estructurados. | compress / telephone-game |
| **#4** | RESUELTA (lectura) | `verdict_synthesizer.py` + `tribunal.py` = código muerto. Ver DSv34-DEAD. | n/a |

### Contrato propuesto — `HandoffPacket` (Pydantic)
```
HandoffPacket:
  layer_id: str                    # "ROL-03", "FOR-02", "N2-UNIT-QUANT"
  verified_claims: list[Claim]     # claim + severity + evidence + source_layer (provenance)
  open_questions: list[str]        # lo no resuelto, pasa explícito a la siguiente capa
  document_window: tuple[int,int]  # (start, end) — qué fragmento vio ESTA capa
  truncated: bool
```
Cada capa consume SOLO el packet upstream, nunca re-resume el raw. Ataca los 5 patrones: provenance (poisoning), ventana explícita (clash), claims estructurados (telephone-game), open_questions (confusion).

### Orden de ejecución R1 (decidido s13)
1. **FUGA #2** — unificar las 3 ventanas de truncado a una constante única con provenance de ventana. Quirúrgico, bajo riesgo, prerequisito de `document_window`. ← **EN CURSO**
2. **FUGA #1** — `HandoffPacket` en `_summarize_rol_outputs` (elimina `concerns[:2]`).
3. **FUGA #3** — claims estructurados al sintetizador vivo.

---

## SCOPE v3.4 — Rebanada 1 (Reliability core)

| ID | Ítem | Patrón | Criterio de aceptación |
|----|------|--------|------------------------|
| **R1** | **Handoff fidelity contract N0→N1→N2** — `HandoffPacket`; ninguna capa re-resume el raw upstream, solo el packet. | compress / telephone-game | Schema definido y cableado; cada transición consume el packet, no el raw; truncado unificado. |
| **R2** | **Placement curva-U en prompts** — misión/constraints al inicio, criterios de veredicto al final; anchors estructurales en el medio. | lost-in-middle | base + 19 variants colocan mission/constraints al inicio y verdict-criteria al cierre; check añadido a self-audit §4.14. |
| **R3** | **Clash annotation en síntesis** — `TribunalTransversal._synthesize()` marca contradicciones Rol↔Forense con fuente + precedencia ANTES de sintetizar. | clash | Anotación estructurada de conflicto (qué, fuente, precedencia); prohibido silent pick. |
| **R4** | **Circuit-breaker de poisoning en N2** — validar tool/retrieval antes de entrar a contexto; trackear provenance; recovery = truncar (no layering). | poisoning | AAD/Spawner registra provenance; recovery = truncate-to-before, no corrección encima. |
| **R5** | **Umbrales de degradación en BudgetController** — trigger de compaction a ~70% del onset del modelo, no al límite. | non-linear cliff | Trigger documentado y cableado a límites (calls=40, n2_per_n1=3); re-benchmark trimestral anotado. |

**Transversal:** self-audit §4.14 gana checks nuevos (A-series) para R1–R5. Versionado dual vigente: solo cara-de-producto + variants bumpean a v3.4.0; docstrings de módulo conservan su content-version salvo cambio real de contenido.

---

## DEUDA DESCUBIERTA EN v3.4

| ID | Severidad | Item | Decisión |
|----|-----------|------|----------|
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` (v2.9.0) + `verdict_synthesizer.py` (v2.8.0) = legacy huérfanos. `main.py` solo cablea `TribunalTransversal`. Cadena muerta: `main → ✗ → tribunal.py → verdict_synthesizer.py`. Riesgo: confunde auditorías de versionado, infla superficie de cert, un futuro Claude podría editarlos creyéndolos vivos. | **BORRAR en el bump atómico de cierre v3.4.** git conserva la historia; borrar es más limpio que `legacy/`. |

---

## FUERA DE SCOPE (diferido)

- 4× Bajo (markitdown UNIT-INGEST, fact-checker UNIT-FACTCHECK, stop-slop AFO post-proc, marketingskills UNIT-PSYCH) → rebanada v3.4 posterior.
- Wizard CLI → rebanada UX propia.
- knowledge-work-plugins (legal+finance matrices) → Medio, posterior.
- infinity + RAG jurisdiccional → **v4.0** (Docker + corpus, infra pesada). NO mezclar.

## MÉTODO (validado s12)

clon en sandbox del remote HEAD → diseño por ítem → implementación con asserts de unicidad → patch único `git apply` → dry-run en clon fresco → JARP commit/push vía GitHub Desktop → post-push verify por SHA. Bump = operación atómica única al cierre del sprint. Borrado DSv34-DEAD entra en ese mismo bump.

## RIESGO / BLAST-RADIUS

**ALTO.** Toca el core (`tribunal_transversal.py`, `prompt_engine.py`, `sub_agent_spawner.py`, `budget_controller.py`, `schema.py`) + base/variant prompts. Mitigación: diseño + GO por ítem, sin big-bang; sub-commits permitidos durante el sprint pero el bump de versión es atómico al cierre. R3 y R4 = mayor riesgo (síntesis y spawning). **Regresión obligatoria:** doc end-to-end debe producir el mismo veredicto determinista; `_deterministic_synthesis` no debe romperse.

## PASOS SIGUIENTES

1. ✅ Diseño R1 + FUGA #4 resuelta (s13).
2. **EN CURSO:** FUGA #2 — unificar truncados.
3. FUGA #1 (`HandoffPacket`) → FUGA #3 → R2 → R3 → R4 → R5, GO entre ítems.
