# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 30/05/2026 (sesión 15 — e3-e6 cerrada + offline gate extendido GREEN) | **Para:** Sesión 16
**Reemplaza:** v13 del 29/05/2026 (sesión 14)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v14.md`
**⚠️ BORRADO en este cierre:** `dark-strategist-continuity-prompt_v13.md` eliminado del repo (autorizado por JARP s15). v14 es el ÚNICO continuity vigente. Actualizar también el archivo del PROYECTO claude.ai (subir v14, quitar v13).

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 15 (resumen ejecutivo)

Sesión de cierre de deuda barata + arranque (sin completar) de la regresión E2E. Sin tocar código del core. Tres frentes:

### 1. e3-e6 (cross-refs CHANGELOG DS↔PA-agent) 🟢 — CERRADA y verificada por contenido en remoto
Diagnóstico read-only de ambos CHANGELOGs (clon público, grep). **La premisa literal de e3-e6 NO se sostenía** (patrón R2: deuda heredada sin verificar contra archivo):
- Todas las cross-refs históricas (cert IDs, ventanas 90d, ciclo SUSPECT→VOID de DS v2.5.1) son **mutuamente consistentes y correctas por fecha**. Tocarlas = falsear registro histórico (lección s14). → **NO-OP / ACEPTADA.**
- **Única asimetría real accionable:** PA-agent emitió `PA-20260529-001` (cert full-coverage DS v3.3.0, ejecutada por PA v1.3.0) pero **su propio CHANGELOG no lo registraba** (grep: 0 menciones). El log de DS sí, `.claude-init` Nota#7 sí. Append-only de un registro verídico faltante — NO falsea historia, NO toca system_prompt → sin re-cert, sin gate.

Fix vía Ruta 3 (F&R → JARP commit GitHub Desktop), 1 commit en `prompt-architect-agent/CHANGELOG.md`:
| Ítem | Fix | Verificado |
|------|-----|-----------|
| Asimetría auditor↔auditee | Append bloque `## [Audit Activity] — 2026-05-29` sobre anchor `## [1.3.0] — 2026-05-27` (registro de `PA-20260529-001`). | ✅ remoto HEAD `f92a9cf`, blob `75d35ec8`, `PA-20260529-001`×2, anchor [1.3.0]×1 intacto |

PA-agent **versión sin cambios** (sigue v1.3.0 / PA-20260527-002). Solo se logueó actividad de auditoría.

### 2. Regresión E2E — ARRANCADA, offline GREEN, ONLINE pendiente de key
JARP aportó **doc de prueba real** (resuelve requisito #2 del gate): contrato de arrendamiento (Miraflores, depto 706 + estacionamiento). Convertido docx→md vía `markitdown` (entry #58). **23.025 chars** (>4000 con margen ~5.7×). **Stakeholders ricos:** 5 personas / 3 roles funcionales (ARRENDADORES = propietario + cónyuge, **representados por apoderada** [poder Partida 16108231] → 3ª perspectiva real de agencia; ARRENDATARIOS = 2 personas). Ganchos forenses P03 Legal: inmueble **en trámite de independización/inscripción** (se arrienda sin título inscrito), acuerdo previo 31/01 vs inicio 01/02. **PII presente (4 DNI) → el doc NO entra al repo, solo input local.**

Entregado `smoke_test_e2e.py` (helper, fuera del repo/surface certificado). **v2** ejecuta la lógica R1/R3/R4/R5 offline vía inputs sintéticos + stub del cliente LLM (sin key, sin red). **Validado por Claude en sandbox contra módulos reales del clon Y confirmado por JARP en su entorno: 9 PASS / 3 SKIP / 0 FAIL.**

| Check | R | Qué ejecuta | Estado |
|---|---|---|---|
| config_keys | — | 5 ventanas v3.4 presentes | ✅ |
| c_fallback_intact | — | `_deterministic_synthesis` → `UnifiedVerdictOutput` | ✅ |
| e_monotonic_verdict | — | ≥1 FATAL → INVIABLE | ✅ |
| r5_budget_fires | R5 | `check_context_budget` alerta al 70% (22400/32000), safe debajo | ✅ |
| r1_handoff_window | R1#1 | `build_forense_prompt` trunca sim Rol a handoff_window=8000 | ✅ |
| r1_3_structured | R1#3 | `build_synthesis_prompt` emite findings estructurados (no prosa) | ✅ |
| r3_clash_protocol | R3 | prompt síntesis carga CLASH PROTOCOL (shape+PRECEDENCE+conflicts_detected) | ✅ |
| r1_synthesis_window | R1#3 | fallback raw respeta synthesis_window=1500 | ✅ |
| r4_poisoning_markers | R4 | `_spawn_permanent` marca parent UNVERIFIED + doc PRIMARY + provenance dict | ✅ |
| a_run_no_maxtokens | (a) | pipeline vivo sin reventar max_tokens | ⏸️ SKIP (sin key) |
| b_unified_output | (b) | salida real del modelo → `UnifiedVerdictOutput` válido + clash records | ⏸️ SKIP (sin key) |
| d_budget_provenance | (d) | marcadores budget/provenance en transparency report vivo | ⏸️ SKIP (sin key) |

---

## ⚠️⚠️ GATE DURO — NO BUMPEAR SIN REGRESIÓN VIVA ⚠️⚠️

**INTACTO. El offline gate (incl. lógica R1/R3/R4/R5) está GREEN, pero NO cierra el gate.** Lo irreductible que SOLO se valida con key (corrida viva):
- **(a)** ¿el prompt Forense real (MASTER_TEMPLATE + handoff 8000 × N Rol agents) revienta `max_tokens`? Solo se sabe con el prompt armado real + respuesta del modelo.
- **(b)** ¿la salida real del modelo parsea a `UnifiedVerdictOutput` válido con clash records? Depende de que el modelo devuelva el JSON con shape correcto.
- **(d)** marcadores budget/provenance presentes en el transparency report vivo.

Estos 3 son justo el riesgo que motivó el gate (6 commits R1-R5 apilados sin corrida viva). El stub NO los sustituye.

**Único blocker restante: API key de Anthropic.** JARP declaró s15 que **aún no la tiene** (consistente s13). Una corrida es acotada (1 doc, 5 agentes TRIBUNAL_FULL, tope 40 calls) → costo chico/predecible; recomendado límite de gasto bajo en console.

**Cómo correr la parte ONLINE cuando JARP tenga key:**
```
cd /d "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\orchestrator"
set ANTHROPIC_API_KEY=sk-ant-...   (NO setx — no persistir el secreto)
python smoke_test_e2e.py "C:\Users\jrodr\Downloads\smoke_contract.txt" 5
```
Esperado si todo va bien: 12 PASS / 0 SKIP / 0 FAIL → gate cleared → bump v3.4 desbloqueado.

---

## OPERACIÓN DE CIERRE v3.4 (tras regresión VIVA, requiere GO por fase)

1. **Regresión E2E VIVA** (a/b/d con key) ← bloqueante, arriba. Offline ya GREEN.
2. **Bump atómico v3.3.0 → v3.4.0** (método s12): cara-de-producto (main.py print/--help, tribunal_transversal Transparency Report header) + 19 variants + router + base + skills si su contenido cambió. **Módulos content-version a subir:** `budget_controller.py`, `sub_agent_spawner.py`, `prompt_engine.py`, `schema.py`, `tribunal_transversal.py`. Docstrings NO-tocados conservan versión (regla dual s12). **NOTA:** `budget_controller.py` y `sub_agent_spawner.py` aún declaran `Version: 2.8.0` en docstring (content-based — subir solo si su contenido cambia en el bump).
3. **Borrado código muerto (DSv34-DEAD):** `orchestrator/tribunal.py` + `orchestrator/verdict_synthesizer.py` + sincronizar `CLAUDE.md` L84/L87 y `prompts/system_prompt.md` L38 (quitar narrativa "v2.x preserved / coexisting"). Justifica meterlo en el bump (re-cert ya prevista aquí).
4. **Self-audit §4.14** + checks A-series, incluido **invariante curva-U** (R2): MISSION primer tercio, VERDICT último tercio.
5. **Re-cert 7-axis Level 1 JARP DEEP full-coverage** post-bump (supersedes PA-20260529-001).
6. **Doc cleanup:** CHANGELOG [3.4.0], jarp-toolkit entry #30, README/CLAUDE, continuity v15.

---

## DEUDA TÉCNICA — POST-SESIÓN 15

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **REGRESIÓN-ONLINE** | 🔴 BLOQUEANTE | a/b/d sin correr (sin API key). | Único blocker del bump v3.4. Script listo y validado offline. Correr cuando haya key. |
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` + `verdict_synthesizer.py` huérfanos (confirmado muerto s14) + narrativa en CLAUDE.md/system_prompt.md. | BORRAR en bump de cierre v3.4 (NO antes — doble re-cert). |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone. | Sin urgencia. Caveat OneDrive al reclonar. |
| **DSv34-HISTORY** | 🟢 ACEPTADA | Remoto = historial de UN commit raíz. Patrón OneDrive+git re-bootstrap. | Registro permanente. NO investigar salvo pedido. No bloquea. |

**CERRADAS s15:** e3-e6 (asimetría auditor logueada; resto NO-OP).
**CERRADAS s14:** `.claude-init Nota#7`, `TK-COSMETIC`.
**CERRADAS s13:** R1-R5 (código), DSv34-BUDGET (R5), DSv34-FUGA#4.

---

## ESTADO ACTUAL VERIFICADO (30/05/2026 fin de sesión 15)

### Repo dark-strategist-agent
- **Versión declarada:** **v3.3.0** (bump a v3.4.0 = operación de cierre PENDIENTE — gate de regresión viva).
- **Cert vigente:** `PA-20260529-001` ACTIVE (full coverage v3.3.0). v3.4 NO certificado (código no bumpeado ni probado vivo — correcto).
- **config["tribunal"] keys v3.4 presentes:** `doc_window`(4000), `handoff_window`(8000), `synthesis_window`(1500), `context_budget_chars`(32000), `context_alert_percent`(70). default `max_calls_total`=40.
- **Default model:** `claude-opus-4-7`.
- **Código muerto presente** (a borrar en bump): `orchestrator/tribunal.py`, `orchestrator/verdict_synthesizer.py`.
- **Helper local (NO commitear):** `orchestrator/smoke_test_e2e.py` — test runner v2, fuera del surface certificado. Si aparece en GitHub Desktop, descartar/no incluir en bump.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. **Editado s15:** `CHANGELOG.md` += bloque `[Audit Activity] — 2026-05-29` (registro de PA-20260529-001). HEAD `f92a9cf`. Versión del agente SIN cambios.

### Repo jarp-toolkit
- Sin cambios s15. (.claude-init Nota#7 = DS v3.3.0 / PA-20260529-001; entry #30 = Architecture v3.3.0, desde s14.)

### Artefactos de prueba (locales, fuera de repos)
- `C:\Users\jrodr\Downloads\smoke_contract.txt` — contrato convertido (PII, NUNCA al repo).
- `smoke_test_e2e.py` v2 — en `orchestrator/` local (helper, no commitear).

---

## PROTOCOLO DE INICIO PARA SESIÓN 16

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo (v14).
2. Cargar este prompt (v14) + `docs/v34_backlog.md`.
3. **PHASE 0 — Verificación rápida:**
   - Confirmar v13 ya NO existe en el repo (borrado s15); v14 es el único continuity.
   - 5 config keys v3.4 presentes. Cert registry: DS v3.3.0 (PA-20260529-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
   - Confirmar bloque `[Audit Activity] — 2026-05-29` en `prompt-architect-agent/CHANGELOG.md` (grep `PA-20260529-001` → 2).
4. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 12 SESIONES (4-15).** Prioridad #1 en userPreferences. Ya confrontado sin filtro s12+s13; señalado de nuevo s15 (1 vez, sin acoso). Si JARP vuelve a no elegir A: asumir prioridad real ≠ escrita; NO re-confrontar.
   - **(C) Regresión E2E VIVA + cierre v3.4** — continuación natural. **Bloqueante = API key.** Si JARP ya tiene key: correr la parte online del smoke-test (comando arriba) → si verde, proceder al bump. Si no tiene key: no se puede avanzar el bump; ofrecer otra rebanada.
   - **(B) Otra rebanada v3.4** — NO empezar sin cerrar la 1 (regla anti-apilamiento). DSv34-DEAD pertenece al bump (no suelto).
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+cara-de-producto siguen minor del agente; skills+docstrings de módulo = content-based).

**De s13 (vigentes):**
- **Sintetizador VIVO = `TribunalTransversal._synthesize()` → `build_synthesis_prompt`.** `verdict_synthesizer.py` + `tribunal.py` MUERTOS (main no los cablea). NO editarlos creyéndolos vivos — borrar en cierre.
- **Ventanas de contexto gobernadas por config, NO hardcoded.** Patrón `config["tribunal"].get("X_window", default)`. Nunca eliminar un límite — hacerlo configurable.
- **Distinguir clash de severity-escalation.** Clash = contradicción factual → precedencia + record. Severity disagreement → escalado. NO colapsar.
- **Poisoning: marcar frontera de confianza.** Claim upstream = UNVERIFIED; document = PRIMARY. Recovery = verificar contra fuente, no corregir encima.
- **Verificar premisas del backlog contra el archivo real ANTES de codificar.** No fabricar trabajo.
- **NO bumpear ni certificar sobre código no ejecutado** (gate de regresión).

**De s14 (vigentes):**
- **No falsear registro histórico al "limpiar" versiones.** Distinguir label de estado actual (actualizable) de marcador "NEW (vX)"/"Previous cert" (histórico, intocable).
- **Borrar código muerto NO es aislado si la doc viva lo declara intencional.** Si toca system prompt certificado, va en el bump.
- **Diagnóstico read-only antes de cerrar deuda.** Clon público + grep revela dependencias ocultas.

**Reforzadas s15:**
- **La premisa de una deuda heredada se verifica contra el archivo ANTES de "arreglarla" (patrón R2 confirmado de nuevo).** e3-e6 venía descrita como "4 cross-refs stale"; el grep mostró que eran registro histórico consistente. El único fix real era una asimetría distinta (cert no logueado en el auditor). No fabricar N ediciones para cerrar un label.
- **Validar el harness/script contra los módulos reales ANTES de entregarlo.** El v2 se corrió en sandbox (clon DS + requirements) hasta 9/9 verde antes de pasárselo a JARP. No entregar scripts sin probar.
- **El stub de LLM cubre la LÓGICA (construcción de prompts, budget, provenance) pero NO el comportamiento vivo (max_tokens real, parseo JSON real).** Offline GREEN de-riskea, no cierra el gate.
- **Secretos: nunca pedir la API key en el chat.** El secreto vive en `set` (sesión), no en `setx` (registro). El test corre local con la key de JARP, no en el sandbox de Claude.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full (over-engineering) | compactador real de tokens (sprint propio, diferido).

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v14.md` (v13 borrado s15)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — clone anónimo falla; usar GitHub MCP o download_url autenticado).
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = read/verify estándar.
- **Sandbox bash:** clonar repos públicos (DS, PA) para grep/sed/patch es MÁS barato que API reads. Patrón validado s12-s15.
- **Conversión docx→md:** `markitdown` (entry #58) requiere `pip install "markitdown[docx]"`.
- **Método de edición = Ruta 3 (F&R explícito a JARP).** El patch vive en sandbox de Claude, NO en disco de JARP. `github:create_or_update_file` prohibido (límite ~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep del marcador esperado), no solo por rotación de SHA o mensaje del commit.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` (v2). Offline = sin key (9 checks). Online = `set ANTHROPIC_API_KEY` + mismo comando (3 checks a/b/d). NO commitear el helper. NO mover `smoke_contract.txt` (PII) al repo.

### Commit sugerido para cierre sesión 15 (continuity v14 + borrado v13)
```
docs: continuity v14 (session 15 close — e3-e6 closed + offline gate GREEN)

Session 15 — closed e3-e6 (auditor-side asymmetry: logged PA-20260529-001 in
prompt-architect-agent CHANGELOG; rest of e3-e6 = NO-OP, historical record
consistent). Started E2E regression: real rental contract as test doc (#2 met),
delivered+validated smoke_test_e2e.py v2 (offline R1/R3/R4/R5 logic GREEN,
9 PASS / 3 SKIP / 0 FAIL on both sandbox and JARP env).

NEW FILE:
- dark-strategist-continuity-prompt_v14.md: replaces v13 for session 16.

DELETED:
- dark-strategist-continuity-prompt_v13.md

STATE:
- e3-e6 CLOSED. PA-agent CHANGELOG logged audit activity (version unchanged v1.3.0).
- E2E offline gate GREEN incl. R1/R3/R4/R5 logic via LLM stub.
- HARD GATE intact: ONLINE checks (a,b,d) still need API key. Bump v3.4 blocked.
- DS still v3.3.0, still PA-20260529-001. Trading deferred 12 sessions (4-15).
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 15

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.3.0 | PA-20260529-001 | ✅ ACTIVE (full coverage) | 27/08/2026 o v4.0.0 |

**v3.4 NO certificado** (código completo pero no bumpeado ni probado vivo — gate de regresión).
**SUPERSEDED:** PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 15 (auto-mejora del próximo Claude)

1. **Verifica la premisa de la deuda contra el archivo real (R2 otra vez).** e3-e6 estaba descrita como "4 cross-refs stale a arreglar". El grep contra ambos CHANGELOGs mostró que las refs históricas eran consistentes y correctas — tocarlas habría falseado historia. El único fix real era OTRA cosa: una asimetría (PA-agent emitió un cert que no logueó en su propio CHANGELOG). Lección: no ejecutes el label; diagnostica el archivo y arregla lo que de verdad está mal, aunque no coincida con la descripción heredada. No fabriques ediciones para llegar a un número.

2. **Append-only de un registro faltante NO es falsear historia — falsear es editar un bloque fechado existente.** Logear `PA-20260529-001` en el CHANGELOG del auditor es añadir un hecho verídico que faltaba. Distinto de cambiar un `Previous cert` histórico (eso sí mentiría). La política append-only del CHANGELOG lo respalda.

3. **Valida cualquier script/harness contra los módulos reales ANTES de entregarlo.** El smoke-test v2 se corrió en sandbox (clon DS + `requirements.txt`) hasta 9/9 verde. Reveló además que el import chain jala `sheets_logger`→`google.oauth2` (hay que instalar requirements completo, no solo pydantic/anthropic). Entregar sin probar habría hecho perder un ciclo a JARP.

4. **El stub de LLM de-riskea LÓGICA, no comportamiento vivo.** El harness offline ejecuta de verdad budget/handoff/synthesis-prompt/poisoning (R1/R3/R4/R5) con un cliente stub, pero NO valida (a) max_tokens real del prompt armado ni (b) parseo del JSON que devuelve el modelo. Offline GREEN reduce el pendiente a una sola corrida viva; no la elimina. No confundir "offline verde" con "gate cerrado".

5. **Secretos fuera del chat.** Nunca pedí la API key en la conversación. El test corre local en la máquina de JARP con `set` (sesión, no `setx`/registro). El sandbox de Claude no hace llamadas reales.

6. **TRADING: 12 SESIONES POSTERGADO (4-15).** Señalado 1 vez s15 (disonancia prioridad escrita vs comportamiento), sin acoso. NO re-confrontar. Si s16 vuelve a no elegir A: asumir prioridad real ≠ escrita y seguir.

7. **Artefactos de prueba NO entran al repo.** `smoke_contract.txt` tiene PII (4 DNI) — repo público, jamás commitear. `smoke_test_e2e.py` es helper fuera del surface certificado — no incluir en el bump. Ambos avisados a JARP en GitHub Desktop.
