# DARK STRATEGIST — BACKLOG SPRINT v3.4

**Abierto:** 29/05/2026 (sesión 13) | **Estado:** REBANADA 1 CÓDIGO-COMPLETA — pendiente regresión + bump | **Última act.:** 29/05/2026 (s13, R1-R5 done)
**Tema:** Reliability core — fidelidad del pipeline AFO→Tribunal→N2 (fix telephone-game / context degradation)
**Bump objetivo:** v3.3.0 → v3.4.0 (operación ATÓMICA de cierre, método s12)
**Cert objetivo:** re-cert 7-axis Level 1 JARP DEEP full-coverage post-bump
**Fuente verificada:** `Agent-Skills-for-Context-Engineering/skills/context-degradation` (v2.1.0) + skills adyacentes `context-compression`, `multi-agent-patterns`

---

## PROBLEMA

El pipeline DS pasa contexto a través de capas: N0 (AFO) → N1 (Tribunal Transversal: Rol + Forense, paralelos y ciegos entre sí) → N2 (sub-agents) → síntesis (AFO). Cada handoff implicaba re-resumen → **pérdida de fidelidad acumulada (telephone-game)**. Resuelto en los 5 patrones de la skill fuente (ver tabla R1-R5).

---

## ESTADO: REBANADA 1 (Reliability core) — CÓDIGO COMPLETO ✅

Sintetizador VIVO confirmado = **`TribunalTransversal._synthesize()`** → `prompt_engine.build_synthesis_prompt()` → JSON → `UnifiedVerdictOutput`. (NO `verdict_synthesizer.py` — muerto, ver DSv34-DEAD.)

**Decisión de diseño:** en lugar de un `HandoffPacket` Pydantic nuevo (over-engineering para handoffs serializados a string), se usaron **ventanas gobernadas por config** + **emisión estructurada con provenance**. Mismo patrón `config["tribunal"].get(...)`. **Ningún límite eliminado** — todos hechos configurables (regla JARP: no romper edge-case coverage).

| ID | Patrón | Commit | Fix | Estado |
|----|--------|--------|-----|--------|
| **R1·#2** | clash (doc) | `fe007a7` | Ventana doc unificada N1=N2 (antes 4000 vs 3000). SSM excluida. `doc_window` (4000). | ✅ |
| **R1·#1** | telephone-game | `f808cda` | Handoff Rol→Forense full-fidelity. `concerns[:2]` eliminado; pasa assumptions/info_demanded/stance_reasoning/perspective con provenance `[ROL-NN]`. `handoff_window` (8000). | ✅ |
| **R1·#3** | compress | `c35b4db` | Findings ESTRUCTURADOS al sintetizador (severity/title/desc/evidence/root_cause + key_risks + omissions) vs prosa cruda. `synthesis_window` (1500) fallback. | ✅ |
| **R2** | lost-in-middle | — | **NO-OP VERIFICADO.** Los 21 prompts YA cumplen curva-U (MISSION en primer ~10%, VERDICT en último ~10-25%). Verificado empíricamente en 6 prompts representativos. Reordenar = riesgo sin beneficio. La parte válida (check §4.14) → ver TRANSVERSAL. | ✅ |
| **R3** | clash | `d27ef18` | Clash annotation protocol en SYNTHESIS_TEMPLATE: separa clash-resolution (precedencia FORENSE>ROL + record estructurado) de severity-escalation. Prohíbe silent pick. UNRESOLVED→confidence LOW. Schema `conflicts_detected` description actualizada (tipo list[str] sin cambios, len() intacto). | ✅ |
| **R4** | poisoning | `5d7d0b0` | Circuit-breaker en `_spawn_permanent`: parent_report marcado UNVERIFIED, document=PRIMARY SOURCE, instrucción de flag si no se sostiene + provenance en retorno. Temporary no afectado (parte solo del doc). | ✅ |
| **R5** | non-linear cliff | `86b87e4` | `check_context_budget()` no-bloqueante, alert al 70% del context budget, cableado en handoff Rol→Forense. Compactador real diferido (sprint propio). + fix DSv34-BUDGET (default 30→40). | ✅ |

**Compile gate:** todo el orchestrator (`*.py` + `ssm/*.py`) compila; config.example.json válido. Verificado en remoto HEAD `86b87e4`.

---

## ⚠️ REGRESIÓN E2E — BLOQUEANTE ANTES DEL BUMP

NO se ha ejecutado el pipeline contra un documento real (>1 mes certificado sin uso real = opción E pendiente). Antes del bump v3.4.0 hay que correr un doc end-to-end y confirmar:
- (a) prompt del Forense NO revienta `max_tokens` con handoff a 8000 + varios Rol agents.
- (b) síntesis sigue produciendo `UnifiedVerdictOutput` válido (parser JSON + clash records con el formato pedido).
- (c) `_deterministic_synthesis` (fallback) intacto.
- (d) `check_context_budget` dispara correctamente; provenance R4 presente en sub-agentes.
- (e) veredicto determinista coherente (≥1 FATAL → INVIABLE).

**Riesgo de haber apilado R1-R5 sin probar:** si la regresión falla, hay 6 commits que desenredar. Confrontado con JARP s13; JARP eligió apilar. Decisión respetada.

---

## OPERACIÓN DE CIERRE v3.4 (pendiente, requiere GO)

1. **Regresión E2E** (bloqueante, arriba).
2. **Bump atómico v3.3.0 → v3.4.0** (método s12): cara-de-producto (main.py, tribunal Transparency Report header) + 19 variants + router + base + skills si cambian. Docstrings de módulo NO (content-based). Los módulos tocados en v3.4 (budget_controller 2.8.0, sub_agent_spawner 2.8.0, prompt_engine, schema 3.0.0, tribunal_transversal 3.0.0) suben su content-version SOLO si su contenido cambió (sí lo hizo en varios).
3. **Borrado código muerto** (DSv34-DEAD): `tribunal.py` + `verdict_synthesizer.py`.
4. **Self-audit §4.14** + checks nuevos (incluido el invariante curva-U de R2).
5. **Re-cert 7-axis full-coverage** post-bump.
6. **Doc cleanup**: CHANGELOG entry [3.4.0], continuity v12, jarp-toolkit entry #30, README/CLAUDE.

---

## DEUDA

| ID | Severidad | Item | Decisión |
|----|-----------|------|----------|
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` + `verdict_synthesizer.py` = legacy huérfanos. | BORRAR en bump de cierre. |
| **DSv34-BUDGET** | ✅ RESUELTA | default 30 vs 40. | Corregido en R5 (`86b87e4`). |
| **DSv34-HISTORY** | 🟢 LOW (registro) | Remoto = historial de UN commit raíz (`03821d1`, bootstrap con mensaje FUGA#2 pegado). NO la historia de 13 sesiones. Patrón OneDrive+git re-bootstrap. | Anotado en continuity. NO investigar salvo pedido. No bloquea (base correcta y verificada). |

---

## TRANSVERSAL — check §4.14 nuevo (de R2)

Añadir a self-audit §4.14 un check del **invariante curva-U**: MISSION/IDENTITY en el primer tercio del prompt, VERDICT/OUTPUT FORMAT en el último tercio. Previene regresión de placement en futuras ediciones. Es prevención, no reordenamiento (los prompts ya cumplen). Se diseña/cablea en la operación de cierre junto a los demás checks A-series.

---

## FUERA DE SCOPE (diferido)

- 4× Bajo (markitdown UNIT-INGEST, fact-checker UNIT-FACTCHECK, stop-slop AFO post-proc, marketingskills UNIT-PSYCH) → rebanada v3.4 posterior.
- Wizard CLI → rebanada UX propia.
- knowledge-work-plugins (legal+finance matrices) → Medio, posterior.
- infinity + RAG jurisdiccional → **v4.0** (Docker + corpus, infra pesada). NO mezclar.

## MÉTODO (validado s12, re-validado s13)

clon sandbox del remote HEAD → diseño por ítem → Python con asserts unicidad → patch único `git apply` → dry-run clon fresco → **entrega F&R a JARP** → JARP commit/push GitHub Desktop → post-push verify por SHA en clon nuevo.

**Lecciones s13:** (1) el patch vive en el sandbox de Claude, NO en disco de JARP → entregar SIEMPRE F&R explícito. (2) Verificar post-push por SHA en clon nuevo es obligatorio — un commit puede subir con mensaje correcto y contenido equivocado (capturado s13, commit `03821d1`). (3) Verificar premisas del backlog contra el archivo real antes de codificar (R2 resultó no-op).
