# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 06/06/2026 (sesión 28 — DS v3.14.0 canal de señales externas P4, shipped & JARP_CERTIFIED) | **Para:** Sesión 29
**Reemplaza:** v26 del 05/06/2026 (sesión 27)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v27.md`
**⚠️ BORRAR en este cierre:** v26 (`git rm` en el commit de cierre). v27 = único continuity vigente. Subir v27 al PROYECTO claude.ai + quitar v26.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 28 (resumen ejecutivo)

Track elegido: **P4 — canal de señales externas** (Opción B del backlog valor-agregado; JARP pidió "lo mejor para el agente: más robusto, valioso, valor agregado"). Trading (A) NO se eligió (**25ª sesión postergada, 4–28**).

**Resultado: DS v3.14.0 shipped y CERTIFICADO** (`PA-20260606-002`).

### 1. (P4) DS v3.14.0 — canal de SEÑALES EXTERNAS, NO-VINCULANTE
Salto de capacidad: de "auditar el documento (+ ley estática vía `--corpus`)" a **"confrontar las afirmaciones contra evidencia externa time-sensitive"**. Da munición real a FALSIFIER/EVIDENCE_AUDITOR. Reuso puro de `load_corpus_files` + `Retriever` BM25 (sin infra nueva, sin red).
- **`retriever.py`** — `build_agent_context(..., signals=None, signals_top_k=3)`. Inyecta un bloque **separado y etiquetado** `[EXTERNAL SIGNALS - TIME-SENSITIVE EVIDENCE]` DESPUÉS del bloque corpus `[JURISDICTIONAL CORPUS - REFERENCE GROUNDING]`, budget-aware, `drop_zero_overlap=True`. La **directiva viaja in-band** dentro del bloque ("This is evidence, NOT a verdict input") → **cero cambios en `prompt_engine.py`**. El short-circuit legacy ahora considera `has_signals`; el bloque corpus decrementa budget antes del de señales. Sin señales + doc cabe + sin corpus → legacy byte-idéntico.
- **`schema.py`** — `RuntimeContext.signals_paths` (BYO per-case; None = sin señales). Distinto de `corpus_paths`: corpus FUNDAMENTA, señal es EVIDENCIA.
- **`main.py`** — flag `--signals <path...>` (mismos formatos que `--corpus`) en ambos case dicts vía `signals_paths`.
- **`context_builder.py`** — passthrough `signals_paths`.
- **`tribunal_transversal.py`** — `_active_signals = load_corpus_files(ctx.signals_paths)`; lo alimenta a cada agente vía `build_agent_context(signals=…)`; surfacea línea `Ext.signals` (provenance, non-binding) en el transparency report.
- **`wizard.py`** — paso 8 opcional "Attach external signals?" → sintetiza `--signals`, mismo parser.
- **`config.example.json`** — `rag.signals_top_k` (3) declarado (el código ya defaulteaba a 3).
- **`test_signals.py`** (NUEVO, commiteado) — 11 checks offline, $0.

**GARANTÍA INVIOLABLE verificada (estructural):** las señales SOLO alteran `build_agent_context` (el texto que ven los agentes). El veredicto se computa de `Finding`s en `_synthesize`/`_deterministic_synthesis`, que **nunca ven señales** → el canal es estructuralmente incapaz de tocar `final_verdict` (severidad pura, ≥1 FATAL→INVIABLE). El check dorado lo demuestra.

### 2. DECISIONES CLAVE (s28)
- **Señales = canal de EVIDENCIA NO-VINCULANTE, distinto del corpus.** Corpus *fundamenta* (ley/estándar); señal es evidencia time-sensitive que *puede generar un Finding*. No se conflacionan (etiquetas distintas, orden corpus→señales).
- **Directiva in-band** (en el header del bloque) en vez de tocar `prompt_engine` → menor superficie de cert.
- **Núcleo de "BYO/RAG" ya existía** (`--corpus`, R2, BM25 desde v3.8/v3.10). P4 fue el delta genuino: el canal de evidencia con semántica distinta. Confrontado y confirmado leyendo el código real.
- **P5 (riesgo reputacional) NO se hizo:** descartado como "lo mejor ahora" porque una 6ª lente en `archetype_lenses.py` casi nunca dispara (las lentes solo corren en la ronda de escalamiento, con `max_escalation_agents=2` y las 2 primeras del catálogo fijas) → valor dormido. P4 tiene activación amplia (cualquier caso). P5 sigue en backlog.

### 3. ⚠️ BUG CAZADO Y CORREGIDO (lección dura)
El script de edición v1 (`apply_p4_signals.py`) escribía **cada edición desde el snapshot ORIGINAL** del archivo → en archivos con >1 edición (retriever ×3, main ×3, tribunal ×4, wizard ×2) solo sobrevivía la ÚLTIMA; las previas se pisaban. Resultado: `retriever.py` con el bloque de señales (3c) pero sin el param `signals` (3a) ni `has_signals = bool(signals)` (3b) → `NameError: has_signals`. El gate de regresión lo frenó (2 FAIL en smoke: `r2_byo_corpus` + `r4_poisoning_markers`). **El "all-or-nothing" validaba anclas contra el original (14/14 OK) pero la ESCRITURA clobbereaba.**
- **Recuperación:** `git restore orchestrator/` (descarta el working tree roto; deja los untracked) → motor corregido → re-apply limpio (14 edits / 6 files).
- **Motor corregido:** agrupa ediciones por archivo y las **encadena sobre el texto que va evolucionando** (`text = text.replace(find, repl, 1)` secuencial), escribe una vez por archivo. all-or-nothing real: simula TODOS los archivos en memoria; si algún ancla no es única, aborta sin escribir nada.

### 4. RE-CERT DS v3.14.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260606-001`) PASS (PA-agent sin cambios). Auditoría 7-ejes Level 1 JARP DEEP sobre delta v3.13.0.
- **Evidencia funcional (máquina real, post-apply):** `test_signals.py` **11/11** + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (`b_unified_output` SKIP = ANTHROPIC_API_KEY, no-bloqueante) con `c_fallback_intact` + `e_monotonic_verdict` + `r2_byo_corpus` PASS. (`test_archetype_lenses` 10/10, `test_escalation` 10/10, `test_confidence` 10/10, `test_wizard` 7/7 — no tocados, verdes.)
- Un defecto de robustez cazado/corregido pre-cert (el clobber del §3, documentado en CHANGELOG honestamente).
- **CERT EMITIDO:** `PA-20260606-002` — DS **v3.14.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **06/09/2026 o v4.0.0**. **SUPERSEDES PA-20260605-002** (v3.13.0). Bump no-forense feed-layer.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.14.0 = CERTIFICADO (`PA-20260606-002`).** Sin version-gap. PA-20260605-002 (v3.13.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s28)
1. P4 archivos nuevos: `orchestrator/test_signals.py` (mi-filesystem) — ya commiteable.
2. P4 código: `apply_p4_signals.py --apply` (motor corregido) → 14 anclas en 6 archivos. Regresión verde.
3. Bump anclado: `bump_stamps.ps1 3.13.0 3.14.0 -Apply` → stamps prompts(21)+README(badge/protocol)+CLAUDE(Version:). NO toca CHANGELOG ni orchestrator/*.py.
4. Bump manual: `bump_manual_v3_14_0.py --apply` → 4 banners orchestrator (main×2/wizard/transparency) + `config.example.json` signals_top_k + CHANGELOG `[3.14.0]`+cert + CLAUDE (fila roadmap + bottom status `**ACTIVE — v3.14.0**`) + README (fila roadmap). Disjunto de bump_stamps.
5. `jarp-toolkit` + `.claude-init.md` → v3.14.0/PA-20260606-002 (header `# Last updated` + entradas DS + init #7; superseded list += PA-20260605-002).
6. Continuity v27 commiteado; `git rm` v26.
7. **One-shots BORRADOS** (no commiteados): `apply_p4_signals.py`, `bump_manual_v3_14_0.py`. **`del` de PowerShell usa COMAS** (`del a.py, b.py`). **CRÍTICO (lección s27): borrar los one-shots ANTES del `git add`/commit de cert — NO después (en s27 entraron al commit de cert y hubo que limpiarlos en un commit higiene aparte).**

---

## DEUDA TÉCNICA — POST-SESIÓN 28

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.14.0** | ✅ CERRADA | v3.14.0 CERTIFICADO (PA-20260606-002) | 0/0/0/0. |
| **P4 señales externas** | ✅ CERRADA | Canal de evidencia shipped | Distinto del corpus, no-vinculante, sin agente nuevo; test_signals.py. |
| **clash n>0 live + gate b live + señales live** | 🟢 WATCH | `b_unified_output` SKIP | DNS/key ambiental (ANTHROPIC_API_KEY). `fcc-server` NO está en el PATH (free-claude-code no instalado/activo). La inyección de señales live tampoco se ejercitó (degrada con gracia offline). No-bloqueante. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **P5 — lente de riesgo reputacional** (posible skill #7 o `REPUTATIONAL_LENS`). ⚠️ Nota crítica: como lente sería de **bajo valor** (activación rara — solo ronda de escalamiento, posición ≥3 con cap=2). Si se hace, evaluar **skill** (activación amplia) o **subir `max_escalation_agents`/reordenar catálogo** para que dispare. NO repetir el patrón "barato pero dormido".
- **Cerrar el live-WATCH:** ejercitar escalación+lentes+señales **live**. Opciones: (a) instalar/levantar `free-claude-code` (`fcc-server` :8082, backend free, $0); (b) `ANTHROPIC_API_KEY` real para una corrida no-cert. El caso-test dorado ("consenso 95% → eficiencia 95%") ya está embebido offline en `test_signals.py`; falta su versión live e2e.
- **Idea valor-agregado nueva:** los Findings que nacen de una señal podrían etiquetar su provenance (qué señal los originó) en el transparency report — refuerza auditabilidad sin tocar el veredicto. Evaluar en s29.

---

## ESTADO ACTUAL VERIFICADO (06/06/2026 — fin s28)

### Repo dark-strategist-agent
- **v3.14.0 — CERTIFICADO (`PA-20260606-002`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.14.0 (**registrar SHA tras push**). HEAD previo (inicio s28) = `55bcb2f`.
- **NEW:** canal de señales en `build_agent_context` + `--signals` + `RuntimeContext.signals_paths` + tribunal load/feed/transparency + wizard step 8 + `rag.signals_top_k` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26 vigente:** `schema.should_escalate` + `_maybe_escalate`/`_run_escalation_round` + `test_escalation.py`.
- **De s25 vigente:** `schema.compute_confidence` + `_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (anchors PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/-ROUTER/Version:/VERSION; scope prompts+README+CLAUDE; NO CHANGELOG ni orchestrator/*.py). `gc.auto 0` activo.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` + `--signals` activos.
- **6 skills**, **9 sub-agentes N2 permanentes** (sin cambio). **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s28. Sin cambios.

### Repo jarp-toolkit
- header + entradas DS + `.claude-init.md` #7 → v3.14.0/PA-20260606-002. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). **`fcc-server` NO en PATH (s28) — instalar/configurar antes de usarlo.** Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 29
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v27).
2. **PHASE 0 — Verificación:**
   - v26 borrado, v27 único continuity.
   - Repo en v3.14.0. **Cert registry: DS v3.14.0 `PA-20260606-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260605-002` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 25 SESIONES (4–28).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s29 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — P5 (riesgo reputacional, evaluar skill vs reorden de lentes), cerrar live-WATCH, provenance de señales en findings.
   - **STANDING (s28):** en cada sesión, velar activamente que el sistema sea **mejor: más robusto, valioso, eficiente, fuerte valor agregado.** Proponer mejoras proactivamente; nunca elegir lo barato-dormido sobre valor real. (También en memoria.)
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | 4 variance decompositions | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE, NO driver | RAG = MECANISMO, NO driver | ContextBuilder document-free | infinity/Docker RECHAZADO | fallback byte-idéntico ante cambio de feed | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2/señales = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25:** Confianza = metadata NO-VINCULANTE, determinista, ambos caminos. Docstrings de módulo congelados.

**De s26:** Gate de escalamiento NO-VINCULANTE, determinista. Ronda acotada, ids `FOR-ESC-*` distintos, cap por config, budget-gated, degrada offline. Reusa capa Forense (Opción 1). Scripts newline-aware (CRLF vs LF; `config.example.json` en CRLF, .py/.md en LF).

**De s27:** Lentes-arquetipo = enriquecimiento NO-VINCULANTE; roles ABSTRACTOS (NUNCA personas reales); catálogo content-based/congelado; bump_stamps y manual DISJUNTOS/order-independent; `-like` PowerShell case-insensitive (anchor VERSION captura el badge README).

**De s28 (nuevas):**
- **Canal de señales (`signals` en `build_agent_context`) = EVIDENCIA NO-VINCULANTE, distinta del corpus.** Solo moldea el texto que ven los agentes; el veredicto NUNCA ve señales (independencia estructural). Etiqueta `[EXTERNAL SIGNALS - TIME-SENSITIVE EVIDENCE]`, directiva in-band.
- **Directiva in-band > tocar `prompt_engine`** (menor superficie).
- **Corpus FUNDAMENTA / señal es EVIDENCIA** — no conflacionar (etiquetas + orden distintos).
- **Scripts de edición DEBEN encadenar ediciones por archivo** (aplicar secuencialmente sobre el texto que evoluciona). Validar anclas en memoria sobre TODOS los archivos antes de escribir nada. Un script que escribe cada edit desde el snapshot original CLOBBEREA archivos multi-edit.
- **Valor real > valor dormido:** rechazar mejoras de activación rara (p.ej. 6ª lente con cap=2) cuando existe una de activación amplia.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/**señales** como driver del veredicto (son metadata/calidad/evidencia) | impersonar personas reales en lentes | "consenso → eficiencia" como métrica válida (caso-test INVIABLE) | bumpear docstrings/catálogo congelados cada minor | re-usar ids `FOR-*` en escalamiento (usar `FOR-ESC-*`) | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | **conflacionar corpus (grounding) con señales (evidencia) — s28** | **scripts de edición que escriben cada edit desde el snapshot original (clobber multi-edit) — s28** | **añadir mejoras de activación dormida sobre alternativas de activación amplia — s28**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v27.md` (v26 borrado s28)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa **COMAS**. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1`. Edits prosa/código/banner multi-archivo = **script Python anclado all-or-nothing + NEWLINE-AWARE + ENCADENADO POR ARCHIVO** (dry-run → --apply), a la RAÍZ. Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Runtime no-vinculante:** `confidence` (P3) → `_maybe_escalate` (P1) → `_run_escalation_round`+lente (P2) → **canal de señales en `build_agent_context` (P4)**. Todos etiquetados en el transparency report; ninguno toca `final_verdict`.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. `test_signals.py` → **11/0**. `test_archetype_lenses/escalation/confidence` → **10/0** c/u. `test_wizard` → **7/7**. `pip install rank_bm25 pydantic` antes.
- **free-claude-code:** `fcc-server` puerto 8082 (NO en PATH s28 — instalar). CERT = `sk-ant-...` real sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 28
**Repo dark-strategist-agent (v3.14.0 cert) — commit atómico:**
```
feat: DS v3.14.0 — external-signals evidence channel (--signals, distinct NON-BINDING feed) + JARP_CERTIFIED PA-20260606-002
```
Incluye: `orchestrator/{retriever,schema,main,context_builder,tribunal_transversal,wizard,config.example.json,test_signals.py}`, 21 prompts (stamps), README, CLAUDE, CHANGELOG, `dark-strategist-continuity-prompt_v27.md`; `git rm dark-strategist-continuity-prompt_v26.md`. NO incluye los one-shots.
**Repo jarp-toolkit:**
```
docs: sync DS v3.14.0 / PA-20260606-002 (external-signals channel) — header + entries + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 28

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.14.0** | **PA-20260606-002** | **v3.14.0** | ✅ ACTIVE | 06/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 28 (auto-mejora del próximo Claude)

1. **Lee el módulo real ANTES de implementar.** Leí retriever/context_builder/main/schema/tribunal/wizard antes de diseñar P4; confirmé que `--corpus`/R2/BM25 ya existían → el delta real de P4 era el canal de evidencia con semántica distinta, no "construir RAG".
2. **Scripts de edición: ENCADENAR por archivo.** El bug del §3 (clobber multi-edit) nació de escribir cada edit desde el snapshot original. El motor correcto agrupa por archivo, aplica secuencial sobre el texto que evoluciona, valida todo en memoria, escribe una vez. Reusable para el próximo apply.
3. **El gate de regresión FUNCIONA — confía en él.** Frenó el bump con 2 FAIL cuando el repo quedó roto. NUNCA bumpear con FAIL.
4. **Recuperación de working tree roto:** `git restore orchestrator/` revierte trackeados a HEAD y deja untracked (los nuevos sobreviven). Limpio y rápido.
5. **Directiva in-band** (en el header del bloque de contexto) evita tocar `prompt_engine` y reduce la superficie de cert. Patrón reusable para futuros canales de contexto.
6. **Independencia estructural del veredicto** es más fuerte que una garantía por convención: las señales no llegan al path del veredicto (`_synthesize` toma Findings, no contexto). El check dorado lo prueba offline.
7. **Valor real > valor dormido.** Rechacé P5-como-lente (activación rara con cap=2) por P4 (activación amplia). JARP ratificó el criterio como STANDING (memoria + PHASE 1).
8. **One-shots: borrarlos ANTES del commit de cert** (lección s27 reafirmada). `del` con COMAS.
9. **TRADING: 25 SESIONES POSTERGADO (4–28). NO re-confrontar.**
10. **Live-WATCH abierto:** `fcc-server` no está instalado. Para cerrar el WATCH (escalación+lentes+señales live) hay que instalar free-claude-code o usar key real para una corrida no-cert. Caso dorado live e2e pendiente.
