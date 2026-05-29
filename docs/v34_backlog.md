# DARK STRATEGIST — BACKLOG SPRINT v3.4

**Abierto:** 29/05/2026 (sesión 13) | **Estado:** OPEN — R1 CERRADO | **Última act.:** 29/05/2026 (s13, R1 done)
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

## R1 — CERRADO ✅ (3 fugas resueltas + verificadas por SHA en remoto)

Sintetizador VIVO confirmado = **`TribunalTransversal._synthesize()`** (`tribunal_transversal.py`) → `prompt_engine.build_synthesis_prompt()` → JSON → `UnifiedVerdictOutput`. R3 se diseña AQUÍ, NO en `verdict_synthesizer.py` (muerto, ver DSv34-DEAD).

**Decisión de diseño clave:** en lugar de un `HandoffPacket` Pydantic nuevo (over-engineering para handoffs que terminan serializados a string en prompts), R1 se resolvió con **3 ventanas gobernadas por config** + **emisión estructurada con provenance**. Mismo patrón `config["tribunal"].get(...)` ya establecido. Ningún límite eliminado — todos hechos configurables.

| Fuga | Commit | Fix | Config key |
|------|--------|-----|------------|
| **#2** | `fe007a7` | Ventana de documento unificada N1=N2 (antes 4000 vs 3000). SSM excluida (post-veredicto). | `doc_window` (4000) |
| **#1** | `f808cda` | Handoff Rol→Forense full-fidelity. `concerns[:2]` eliminado; ahora pasa `assumptions_made`, `information_demanded`, `stance_reasoning`, `role_perspective` con provenance `[ROL-NN]`. | `handoff_window` (8000) |
| **#3** | `c35b4db` | Findings ESTRUCTURADOS al sintetizador vivo (severity/title/desc/evidence/root_cause + key_risks + omissions) en vez de prosa cruda `[:1500]`. Raw como fallback gobernado. | `synthesis_window` (1500) |
| **#4** | (lectura s13) | RESUELTA. `verdict_synthesizer.py` + `tribunal.py` = código muerto → DSv34-DEAD. | n/a |

**Criterio de aceptación R1: CUMPLIDO.** Cada transición consume datos estructurados con provenance, no raw re-resumido; truncados unificados y gobernados; 0 residuos hardcoded verificados en remoto (HEAD `c35b4db`).

**Regresión PENDIENTE (antes del bump):** doc end-to-end con varios Rol agents debe correr y confirmar (a) prompt del Forense no revienta `max_tokens` con handoff a 8000, (b) síntesis sigue produciendo `UnifiedVerdictOutput` válido, (c) `_deterministic_synthesis` intacto.

---

## SCOPE v3.4 — Rebanada 1 (Reliability core)

| ID | Ítem | Patrón | Estado |
|----|------|--------|--------|
| **R1** | **Handoff fidelity contract N0→N1→N2** — 3 ventanas gobernadas + emisión estructurada con provenance. | compress / telephone-game | ✅ **CERRADO** (#2+#1+#3) |
| **R2** | **Placement curva-U en prompts** — misión/constraints al inicio, criterios de veredicto al final; anchors estructurales en el medio. | lost-in-middle | ⏳ siguiente |
| **R3** | **Clash annotation en síntesis** — `TribunalTransversal._synthesize()` marca contradicciones Rol↔Forense con fuente + precedencia ANTES de sintetizar. | clash | pendiente |
| **R4** | **Circuit-breaker de poisoning en N2** — validar tool/retrieval antes de entrar a contexto; trackear provenance; recovery = truncar (no layering). | poisoning | pendiente |
| **R5** | **Umbrales de degradación en BudgetController** — trigger de compaction a ~70% del onset del modelo, no al límite. | non-linear cliff | pendiente |

**Transversal:** self-audit §4.14 gana checks nuevos (A-series) para R1–R5. Versionado dual vigente: solo cara-de-producto + variants bumpean a v3.4.0; docstrings de módulo conservan su content-version salvo cambio real de contenido.

---

## DEUDA DESCUBIERTA EN v3.4

| ID | Severidad | Item | Decisión |
|----|-----------|------|----------|
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` (v2.9.0) + `verdict_synthesizer.py` (v2.8.0) = legacy huérfanos. `main.py` solo cablea `TribunalTransversal`. Cadena muerta: `main → ✗ → tribunal.py → verdict_synthesizer.py`. Riesgo: confunde auditorías de versionado, infla superficie de cert, un futuro Claude podría editarlos creyéndolos vivos. | **BORRAR en el bump atómico de cierre v3.4.** git conserva la historia; borrar es más limpio que `legacy/`. |
| **DSv34-BUDGET** | 🟢 LOW | `budget_controller.py` default `max_calls_total=30` vs `config.example.json`=40 y decisiones vigentes ("calls 40"). Discrepancia de default. | Alinear default a 40 en el bump de cierre. No vale commit propio. |
| **DSv34-HISTORY** | 🟢 LOW (registro) | El remoto tiene historial git de UN solo commit raíz (`03821d1`, bootstrap masivo con mensaje de FUGA#2 pegado). NO contiene la historia de 13 sesiones que la continuity asume. Compatible con patrón OneDrive+git re-bootstrap. | Anotar en continuity. NO investigar salvo que JARP lo pida. No bloquea trabajo (base de código correcta y verificada). |

---

## FUERA DE SCOPE (diferido)

- 4× Bajo (markitdown UNIT-INGEST, fact-checker UNIT-FACTCHECK, stop-slop AFO post-proc, marketingskills UNIT-PSYCH) → rebanada v3.4 posterior.
- Wizard CLI → rebanada UX propia.
- knowledge-work-plugins (legal+finance matrices) → Medio, posterior.
- infinity + RAG jurisdiccional → **v4.0** (Docker + corpus, infra pesada). NO mezclar.

## MÉTODO (validado s12, re-validado s13)

clon en sandbox del remote HEAD → diseño por ítem → implementación con asserts de unicidad → patch único `git apply` → dry-run en clon fresco → entrega F&R a JARP → JARP commit/push vía GitHub Desktop → post-push verify por SHA en clon nuevo. Bump = operación atómica única al cierre del sprint. Borrado DSv34-DEAD + DSv34-BUDGET entran en ese mismo bump.

**Lección s13:** el patch vive en el sandbox de Claude, NO en el disco de JARP. Entregar SIEMPRE como F&R explícito (no asumir que JARP puede correr `git apply` sobre un .patch que no tiene). Verificar post-push por SHA en clon nuevo es obligatorio — un commit puede subir con mensaje correcto y contenido equivocado (capturado s13).

## RIESGO / BLAST-RADIUS

**ALTO.** Toca el core (`tribunal_transversal.py`, `prompt_engine.py`, `sub_agent_spawner.py`, `budget_controller.py`, `schema.py`) + base/variant prompts. Mitigación: diseño + GO por ítem, sin big-bang; sub-commits durante el sprint pero el bump de versión es atómico al cierre. R3 y R4 = mayor riesgo (síntesis y spawning). **Regresión obligatoria** antes del bump.

## PASOS SIGUIENTES

1. ✅ R1 CERRADO (FUGA #2 `fe007a7` + #1 `f808cda` + #3 `c35b4db`).
2. ⏳ **R2** — placement curva-U en base + 19 variants (lost-in-middle). Mayor superficie (21 prompts), riesgo medio.
3. R3 → R4 → R5, GO entre ítems. Bump atómico + borrado código muerto + regresión + re-cert al cierre.
