# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 03/06/2026 (sesión 23 — DS v3.9.0 Interactive Wizard CLI + doc_top_k fix shipped & JARP_CERTIFIED) | **Para:** Sesión 24
**Reemplaza:** v21 del 03/06/2026 (sesión 22)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v22.md`
**⚠️ BORRAR en este cierre:** v21 (`git rm` en el commit de cierre). v22 = único continuity vigente. Subir v22 al PROYECTO claude.ai + quitar v21.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 23 (resumen ejecutivo)

Track (B) elegido: **Wizard CLI v3.9.0 + alineación doc_top_k (D-v38-01)** → **DS v3.9.0 shipped y CERTIFICADO**. Bump **no-forense** (solo product-face del orquestador). Trading (A) NO se eligió (20ª sesión postergada).

### 1. (B) DS v3.9.0 — Interactive Wizard CLI + fix D-v38-01
Bump atómico §4.14.1: **2 nuevos + main.py + retriever.py + barrido de stamps (base + router + 19 variants + README + CLAUDE = 23 archivos, 69 líneas)**. **NO tocó CONTENIDO de prompts/skills, ni roster de 9 units, ni lógica de veredicto.**
- **`orchestrator/wizard.py` (NEW)** — wizard interactivo guiado para operadores no-técnicos (cierra gap KIMI/Copilot). `build_command(answers)` PURO + unit-testeado; `run_wizard()` = única I/O. Flujo: dominio (20 → token `--type` canónico) → drill-down Legal L01–L12 → subscenario → objective → regime (7) → Tribunal (auto/1/3/5/7) → SSM (MICRO/MESO/MACRO). Imprime el comando `python main.py ...` equivalente y ofrece ejecutarlo.
- **`main.py`** — flag `--wizard`. **El wizard SINTETIZA argv y lo re-parsea con el MISMO parser argparse** → la vía guiada es byte-idéntica a los flags manuales. Ninguna ruta existente alterada.
- **`orchestrator/test_wizard.py` (NEW)** — 5 casos sobre `build_command`.
- **`orchestrator/retriever.py`** — **D-v38-01 CERRADA**: default `doc_top_k` de `build_agent_context` alineado **5 → 6** (config era autoritativo; era "el próximo touch de retriever" que la cert v3.8.0 señaló). `query(top_k=5)` NO tocado (fuera de scope). Docstring del módulo queda en v3.8.0 (content-based).
- **Versión**: barrido §4.14.1 vía `bump_stamps.ps1` (reemplazo anclado por línea, dry-run obligatorio). Skills/dominios sin cambio (6/20).

### 2. DECISIONES CLAVE
- **Bump no-forense = re-cert confirmatory.** El Wizard + doc_top_k tocan SOLO el product-face del orquestador; la superficie forense (19 variants + 6 skills + base + router CONTENIDO) es byte-idéntica salvo stamps. La cert valida consistencia, no nuevo contenido.
- **El wizard NO re-implementa lógica:** construye argv y lo re-parsea por el mismo parser → cero divergencia. Patrón a preservar.
- **Método de bump mecánico:** `bump_stamps.ps1` (anclado a PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/Version:/badge; excluye CHANGELOG; dry-run → -Apply). Reutilizable en bumps futuros vía `-OldVersion/-NewVersion`. Edits de prosa = `finalize_v3_9_0.ps1` (reemplazos literales `.Replace`, all-or-nothing).

### 3. RE-CERT DS v3.9.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). RULE 08 self-audit L0 (`PA-20260603-003`) PASS primero. Audit del delta v3.9.0 sobre baseline v3.8.0 (19/19 sin cambio).
- **Evidencia funcional:** `test_wizard.py` 5/5 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, necesita key real, no-bloqueante) + flujo wizard validado en vivo (argv correcto emitido, paridad con flags manuales).
- **3 findings de consistencia documental atrapados y resueltos PRE-cert:**
  - **D-v39-01** 🟡 MODERATE — `CLAUDE.md` status final `**ACTIVE — v3.8.0**` no capturado por el barrido anclado (línea sin ancla de stamp). → corregido a v3.9.0.
  - **D-v39-02** 🟡 MODERATE — árbol de repo en `CLAUDE.md` sin `wizard.py`/`test_wizard.py`. → añadidos.
  - **D-v39-03** 🔵 LATENT — tablas roadmap de README+CLAUDE sin fila v3.9.0. → añadida.
- **D-v38-01 (LATENT de v3.8.0) → CERRADA** (doc_top_k alineado a 6).
- **CERT EMITIDO:** `PA-20260603-004` — DS **v3.9.0 JARP_CERTIFIED**, **0 CRITICAL / 0 SERIOUS / 0 MODERATE / 0 LATENT**, BIAS_CHECK PASS. Válido hasta **30/08/2026 o DS v4.0.0**. **SUPERSEDES PA-20260603-002** (v3.8.0). `JARP_BENCHMARK_LIVE` → v3.9.0. Sin cascade (minor bump).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.9.0 = CERTIFICADO (`PA-20260603-004`).** No hay version-gap. PA-20260603-002 (v3.8.0) pasa a SUPERSEDED.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s23)
1. `dark-strategist-agent/CHANGELOG.md` — entrada `[3.9.0]` + sub-bloque `JARP_CERTIFIED DS v3.9.0 PA-20260603-004`. (vía `finalize_v3_9_0.ps1`)
2. `dark-strategist-agent/CLAUDE.md` — fix `ACTIVE` + árbol + fila roadmap. (vía script)
3. `dark-strategist-agent/README.md` — fila roadmap v3.9.0. (vía script)
4. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 + Note #16 → v3.9.0/PA-004. (vía script)
5. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.9.0/PA-004. ✅ (escrito directo)
6. Continuity v22 (este archivo) — commitear; `git rm` v21.

---

## DEUDA TÉCNICA — POST-SESIÓN 23

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.9.0** | ✅ CERRADA | v3.9.0 CERTIFICADO (PA-20260603-004) | 0/0/0/0. |
| **D-v38-01** | ✅ CERRADA | `doc_top_k` alineado 5 → 6 | Cerrada en v3.9.0. |
| **Wizard CLI** | ✅ CERRADA | v3.9.0 shipped | Gap KIMI/Copilot cerrado. |
| **corpus R2 contenido** | 🟢 DIFERIDA (único roadmap restante) | Mecanismo shipped vacío; poblar corpus jurisdiccional (p.ej. Perú: Código Civil / Ley 29733) | Curación de contenido. Activa R2 ya cableado. **NO es código → evaluar si requiere re-cert o solo data.** |
| **pydantic en requirements** | 🟢 LATENT pre-existente | `orchestrator/requirements.txt` no lista `pydantic` (dep dura vía schema.py) | Higiene: agregar `pydantic>=2`. |
| **scripts helper en repo** | 🟢 DECIDIR | `bump_stamps.ps1` + `finalize_v3_9_0.ps1` en raíz DS | Decidir: commitear como tooling reutilizable o `.gitignore`. |
| **clash n>0 live + gate b live** | 🟢 WATCH | smoke offline GREEN; `b_unified_output` sigue necesitando Opus real | Pendiente validación con key real. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción para docs ricos | Sin cambio. |

**CERRADAS s23:** DS v3.9.0 (Wizard CLI), D-v38-01 (doc_top_k), 3 findings doc pre-cert, re-cert v3.9.0.

**TOP-7 roadmap: COMPLETO. Único pendiente de la rama (B): corpus R2 contenido (data, no código).**

---

## ESTADO ACTUAL VERIFICADO (03/06/2026 fin de sesión 23)

### Repo dark-strategist-agent
- **v3.9.0 — CERTIFICADO (`PA-20260603-004`)**. Default `claude-opus-4-7`.
- **NEW:** `orchestrator/wizard.py`, `orchestrator/test_wizard.py`. `main.py --wizard`. `retriever.py` doc_top_k=6.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`.
- **6 skills** (sin cambio). **9 sub-agentes N2 permanentes** (sin cambio).
- Helper scripts en raíz: `bump_stamps.ps1`, `finalize_v3_9_0.ps1` (decidir commit/gitignore).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s23. Sin cambios.

### Repo jarp-toolkit
- header + entry #30 + Note #16 + `.claude-init.md` Note #7 → v3.9.0/PA-004. PRIVADO (mi-filesystem/GitHub MCP).

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 24
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v22).
2. **PHASE 0 — Verificación:**
   - v21 borrado, v22 único continuity.
   - Repo en v3.9.0. **Cert registry: DS v3.9.0 `PA-20260603-004` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260603-002` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 20 SESIONES (4-23).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Roadmap restante** — queda SOLO **corpus R2 contenido** (curación jurisdiccional, p.ej. Perú; activa R2 ya cableado — es DATA, evaluar si re-cert aplica) + **pydantic en requirements** (higiene trivial). Wizard + doc_top_k YA cerrados.
   - **(C) Gobernanza** — backlog clasificado; sin limbo.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados | Sev×Likelihood NON-BINDING | SOX deficiency mapea nativo al tier 4-niveles | 4 variance decompositions obligatorias | orden monotónico FATAL→SERIOUS→MODERATE→LATENT al insertar filas | telephone-game resuelto v3.4 — NO reabrir | context-degradation es LENTE DE DETECCIÓN, NO driver del veredicto | RAG es MECANISMO DE ALIMENTACIÓN doc-feed, NO driver del veredicto | ContextBuilder document-free → solo SELECCIONA corpus; retrieval en doc-feed layer | infinity/Docker RECHAZADO — DS zero-infra (BM25 embebido) | fallback byte-idéntico OBLIGATORIO ante cualquier cambio de feed | leer el módulo real antes de incorporar (roadmap puede estar geométricamente desalineado).

**De s23 (nuevas):**
- **El wizard SINTETIZA argv → mismo parser argparse.** NO re-implementar lógica de pipeline en el wizard. Cualquier nuevo modo de invocación debe construir flags y delegar al parser existente.
- **Bump no-forense (solo product-face del orquestador) → re-cert CONFIRMATORY.** No expande la superficie de prompts/skills. Clasificar SIEMPRE forense vs no-forense antes de certificar el alcance.
- **Barrido de stamps anclado por línea (no global).** Anclas: PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/Version:/badge. Excluir CHANGELOG (historia inmutable). Las líneas de status SIN ancla (p.ej. `**ACTIVE — vX**` al pie) NO las captura el barrido → revisar a mano post-bump (lección D-v39-01).
- **Verificar README+CLAUDE post-bump por contenido:** filas roadmap, árbol de repo y status final son superficies de drift que el barrido anclado no toca.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | UNIT-INGEST como sub-agente del spawner | Severity×Likelihood como dimensión VINCULANTE | skills knowledge-work descartadas | re-trabajar el telephone-game (resuelto v3.4) | context-degradation como driver del veredicto | latent-briefing de Agent-Skills (requiere KV-cache runtime) | infinity/Docker como backend RAG baseline (zero-infra; BM25 embebido) | embeddings densos como baseline RAG (BM25 suficiente para legal) | RAG de contenido en ContextBuilder (document-free) | **re-implementar lógica de pipeline en el wizard (debe delegar al parser) — s23.**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v22.md` (v21 a borrar s23)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. **Si mi-filesystem timeoutea: `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop.**
- **Método de edición:** stamps multi-archivo = `bump_stamps.ps1` (anclado, dry-run → -Apply). Edits de prosa multi-archivo = script de reemplazos literales `.Replace` all-or-nothing (`finalize_v3_9_0.ps1`). Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO puedo ejecutar Python/PowerShell en la máquina de JARP → JARP corre regresión y scripts.
- **Verificar SIEMPRE por CONTENIDO** post-bump (README/CLAUDE: roadmap, árbol, status final).
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py`. Offline esperado 11 PASS / 1 SKIP (b necesita key real). `pip install rank_bm25` antes de correr el agente.
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real + sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic (NO listado — deuda), google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commit sugerido para cierre sesión 23
**Repo dark-strategist-agent:**
```
feat: DS v3.9.0 — Interactive Wizard CLI + doc_top_k align (D-v38-01) + JARP_CERTIFIED PA-20260603-004

Session 23 — track (B): Wizard CLI (orchestrator/wizard.py + main.py --wizard,
synthesizes argv into the same parser) + retriever.py doc_top_k 5->6 (closes
D-v38-01). Atomic §4.14.1 stamp bump (23 files). Non-forensic (orchestrator
product-face only; prompt/skill surface byte-identical except stamps).
Re-cert PA-20260603-004, 0/0/0/0, BIAS PASS, supersedes PA-20260603-002.
3 doc-consistency findings resolved pre-cert (D-v39-01/02/03).

NEW: orchestrator/wizard.py, orchestrator/test_wizard.py
NEW: dark-strategist-continuity-prompt_v22.md (replaces v21)
DELETED: dark-strategist-continuity-prompt_v21.md
```
**Repo jarp-toolkit:**
```
docs: sync DS v3.9.0 / PA-20260603-004 (Wizard CLI + doc_top_k) — header + #16 + #30 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 23

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.9.0** | **PA-20260603-004** | **v3.9.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 23 (auto-mejora del próximo Claude)

1. **Bump no-forense ≠ bump forense.** El Wizard toca product-face, no contenido de prompts. La re-cert es confirmatory: validar consistencia (stamps, árbol, roadmap, status), no re-auditar la superficie forense byte-idéntica.
2. **El barrido anclado NO captura líneas de status sin ancla** (D-v39-01: `**ACTIVE — v3.8.0**` al pie de CLAUDE.md). Tras cualquier `bump_stamps.ps1`, revisar a mano README/CLAUDE: status final, árbol de repo, filas roadmap.
3. **Patrón wizard: sintetizar argv y re-parsear con el mismo parser** garantiza paridad total con flags manuales y cero deuda de divergencia. Reusar si se añaden más modos de entrada.
4. **No puedo ejecutar en la máquina de JARP.** mi-filesystem es solo archivos. JARP corre regresión (`test_wizard.py`, `smoke_test_e2e.py`) y los scripts (`bump_stamps.ps1`, `finalize_v3_9_0.ps1`). Gate regresión-verde ANTES de mover versión/cert.
5. **TRADING: 20 SESIONES POSTERGADO (4-23).** Señalado sin acoso (s23 reiteró recomendación una vez). NO re-confrontar. Si s24 no elige A, asumir prioridad real ≠ escrita.
6. **Único roadmap restante (B): corpus R2 contenido** — es DATA (curación jurisdiccional), no código. Evaluar si poblar el corpus requiere re-cert (cambia output de retrieval) o se trata como data deferida.
