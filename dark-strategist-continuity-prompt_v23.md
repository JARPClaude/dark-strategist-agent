# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 03/06/2026 (sesión 24 — DS v3.10.0 BYO corpus per-case + R2 overlap floor + pydantic, shipped & JARP_CERTIFIED) | **Para:** Sesión 25
**Reemplaza:** v22 del 03/06/2026 (sesión 23)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v23.md`
**⚠️ BORRAR en este cierre:** v22 (`git rm` en el commit de cierre). v23 = único continuity vigente. Subir v23 al PROYECTO claude.ai + quitar v22.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 24 (resumen ejecutivo)

Track (B) elegido: **roadmap restante**. El último ítem (corpus R2) se **re-scopeó** tras confrontación de JARP: de "pre-cargar leyes por jurisdicción" (no escala) → **mecanismo BYO per-case**. Resultado: **DS v3.10.0 shipped y CERTIFICADO** (`PA-20260603-006`). Bump **no-forense** (feed-layer). Trading (A) NO se eligió (21ª sesión postergada).

### 1. (B) DS v3.10.0 — BYO corpus per-case + R2 overlap floor + pydantic
Bump atómico §4.14.1. **8 archivos de código tocados, +134 líneas netas. CONTENIDO de prompts/skills, roster de 9 units y lógica de veredicto: byte-idénticos.**
- **Re-scopeo corpus R2 (decisión JARP):** el repo NO contiene leyes. Provee el **mecanismo**; el operador adjunta textos de referencia **de su caso** vía `--corpus`. Escala a cualquier jurisdicción, zero-infra. `JURISDICTION_CORPUS_MAP = {}` queda como gancho opcional dormido (NO poblar).
- **`orchestrator/retriever.py`** — `load_corpus_files(paths)` (BYO: `.jsonl/.txt/.md` directo; PDF/DOCX/PPTX/XLSX/HTML vía UNIT-INGEST/markitdown lazy + chunk). **R2 floor = overlap de tokens** (`query(..., drop_zero_overlap=True)`), NO score BM25. Docstring → v3.10.0 (content-based).
- **`orchestrator/main.py`** — flag `--corpus <path...>` (nargs) + `corpus_paths` en ambos case dicts. Stamps product-face → v3.10.0.
- **`orchestrator/wizard.py`** — paso 7 opcional "Attach reference texts?" → construye `--corpus` y delega al mismo parser (patrón s23). Stamps → v3.10.0.
- **`orchestrator/test_wizard.py`** — 5 → **7 tests** (BYO appended + empty omits). → v3.10.0.
- **`orchestrator/schema.py`** — `corpus_paths: list[str] | None` (additive; `corpus: str|None` map-gancho intacto).
- **`orchestrator/context_builder.py`** — passthrough `corpus_paths=case.get("corpus_paths")` (map lookup intacto).
- **`orchestrator/tribunal_transversal.py`** — rama BYO: `load_corpus_files(_byo) if _byo else load_corpus(ctx.corpus)`. Fallback map preservado (empty → no-op).
- **`orchestrator/requirements.txt`** — `pydantic>=2.0.0` declarado (cierra LATENT; era transitivo vía anthropic).

### 2. DECISIONES CLAVE
- **R2 = BYO per-case, NO pre-load.** El contenido jurisdiccional es input del operador, no responsabilidad del repo. Mata el enfoque "corpus por país" (no escala, mantenimiento eterno).
- **Floor R2 = overlap de tokens, NO score BM25.** Un floor por `score>0` da falsos negativos en corpus pequeños (BM25 IDF=0 para términos en ~mitad de un corpus diminuto). BYO trae corpus pequeños → overlap es robusto a tamaño. **Diagnosticado y corregido en máquina real durante s24** (el floor score-based había pasado en sandbox por azar de corpus mediano).
- **markitdown reutilizado** (ya era dep vía ingest.py) para corpus BYO binarios.
- **Bump no-forense (feed-layer) → re-cert CONFIRMATORY.**
- **mi-filesystem preserva escapes** (`\n` literal en strings) byte-exacto — verificado con probe; escritura directa de código segura.

### 3. RE-CERT DS v3.10.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). RULE 08 self-audit L0 (`PA-20260603-005`) PASS.
- **Evidencia funcional (máquina real, no sandbox):** `test_wizard.py` **7/7** + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (b_unified_output SKIP = key real, no-bloqueante) + `byo_check.py` GREEN (BYO loader + R2 inyecta + floor descarta ruido + legacy byte-idéntico, con BM25 vivo sin key).
- **CERT EMITIDO:** `PA-20260603-006` — DS **v3.10.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **03/09/2026 o v4.0.0**. **SUPERSEDES PA-20260603-004** (v3.9.0). Sin cascade (minor).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.10.0 = CERTIFICADO (`PA-20260603-006`).** Sin version-gap. PA-20260603-004 (v3.9.0) → SUPERSEDED.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s24)
1. Colocar los 8 archivos en `orchestrator/` (retriever.py + byo_check.py ya escritos directo por Claude en s24; byo_check NO se commitea).
2. **Stamps anclados:** `bump_stamps.ps1 -OldVersion 3.9.0 -NewVersion 3.10.0` (dry-run → -Apply). Sweep: 19 variants + base + router + README badge + CLAUDE + CATALOG_VERSION. (Los 8 .py de orchestrator ya traen sus stamps de módulo a 3.10.0, sin anclas → el script no los re-toca.)
3. **Edits de prosa no-anclados (revisar a mano — lección D-v39-01):** CHANGELOG `[3.10.0]`, fila roadmap README+CLAUDE, status final `ACTIVE → v3.10.0` en CLAUDE.
4. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 + Note #16 → v3.10.0/PA-006.
5. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.10.0/PA-006.
6. **Limpieza pre-commit:** borrar/gitignorar `orchestrator/byo_check.py` + `orchestrator/_byo_sample.jsonl` (temporales de validación).
7. Continuity v23 (este archivo) — commitear; `git rm` v22.

---

## DEUDA TÉCNICA — POST-SESIÓN 24

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.10.0** | ✅ CERRADA | v3.10.0 CERTIFICADO (PA-20260603-006) | 0/0/0/0. |
| **corpus R2** | ✅ CERRADA (re-scopeada) | Mecanismo BYO per-case shipped | Roadmap cerrado como MECANISMO, no data. Repo no contiene leyes. |
| **pydantic en requirements** | ✅ CERRADA | `pydantic>=2.0.0` declarado | — |
| **scripts helper en repo** | 🟢 DECIDIR | `bump_stamps.ps1` (+ futuros finalize) en raíz DS | Recomendado: `git mv` a `tools/` y commitear como tooling reutilizable. |
| **smoke desactualizado** | 🟢 WATCH | `smoke_test_e2e.py` aún rotulado "v3 (v3.4 pre-bump gate)" | Gate estable pero viejo; no ejercita R2 (doc cabe, sin corpus). Considerar añadir un caso BYO al smoke. |
| **clash n>0 live + gate b live** | 🟢 WATCH | `b_unified_output` necesita Opus real (key) | Pendiente validación con key. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

**CERRADAS s24:** corpus R2 (BYO), pydantic, re-cert v3.10.0. **El TOP-7 + el último ítem de la rama (B) están CERRADOS. DS roadmap = 100%.**

---

## ESTADO ACTUAL VERIFICADO (03/06/2026 fin de sesión 24)

### Repo dark-strategist-agent
- **v3.10.0 — CERTIFICADO (`PA-20260603-006`)**. Default `claude-opus-4-7`.
- **NEW:** `orchestrator/load_corpus_files` + `--corpus` + wizard paso 7 + `corpus_paths` (schema/context/tribunal). Floor R2 overlap-based.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}` (gancho dormido; BYO es la vía activa).
- **6 skills** (sin cambio). **9 sub-agentes N2 permanentes** (sin cambio).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s24. Sin cambios.

### Repo jarp-toolkit
- header + entry #30 + Note #16 + `.claude-init.md` Note #7 → v3.10.0/PA-006. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 25
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v23).
2. **PHASE 0 — Verificación:**
   - v22 borrado, v23 único continuity.
   - Repo en v3.10.0. **Cert registry: DS v3.10.0 `PA-20260603-006` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260603-004` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados (sin ellos R1/R2 corren degradados a legacy).
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 21 SESIONES (4-24).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) DS roadmap** — **CERRADO 100%.** Solo quedan WATCH/DECIDIR menores (scripts→tools/, smoke BYO-case). No hay roadmap mayor pendiente.
   - **(C) Gobernanza** — backlog clasificado; sin limbo.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados | Sev×Likelihood NON-BINDING | SOX deficiency mapea nativo al tier 4-niveles | 4 variance decompositions obligatorias | orden monotónico FATAL→SERIOUS→MODERATE→LATENT al insertar filas | telephone-game resuelto v3.4 — NO reabrir | context-degradation es LENTE DE DETECCIÓN, NO driver del veredicto | RAG es MECANISMO DE ALIMENTACIÓN doc-feed, NO driver del veredicto | ContextBuilder document-free → solo SELECCIONA corpus; retrieval en doc-feed layer | infinity/Docker RECHAZADO — DS zero-infra (BM25 embebido) | fallback byte-idéntico OBLIGATORIO ante cualquier cambio de feed | leer el módulo real antes de incorporar (roadmap puede estar geométricamente desalineado) | el wizard SINTETIZA argv → mismo parser argparse (NO re-implementar lógica) | bump no-forense (product-face) → re-cert CONFIRMATORY | barrido de stamps anclado por línea; líneas de status sin ancla revisar a mano | verificar README+CLAUDE post-bump por contenido.

**De s24 (nuevas):**
- **R2 = corpus BYO per-case, NO pre-cargado.** El operador adjunta los textos de su caso vía `--corpus` (cualquier jurisdicción). El repo NO contiene leyes. `JURISDICTION_CORPUS_MAP` queda `{}` como gancho opcional. NO poblar corpus en el repo.
- **Floor R2 = OVERLAP DE TOKENS, no score BM25.** Un floor por score da falsos negativos en corpus pequeños (IDF=0). `drop_zero_overlap` descarta solo pasajes sin token compartido (ruido puro). Robusto a tamaño de corpus.
- **Cualquier nuevo modo de ingesta de corpus reutiliza UNIT-INGEST (markitdown)** para binarios → chunk → BM25. No reinventar conversión.
- **mi-filesystem preserva escapes byte-exacto** (verificado): se puede escribir código con `\n` literales directo. Para reemplazos masivos seguir Ruta 3 si el archivo es grande/sensible.
- **Validar features de retrieval con un corpus PEQUEÑO** (2-3 pasajes), no solo mediano — los edge cases de BM25 (IDF=0) solo aparecen con corpus diminutos, que son el caso realista de BYO.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | UNIT-INGEST como sub-agente del spawner | Severity×Likelihood como dimensión VINCULANTE | skills knowledge-work descartadas | re-trabajar el telephone-game (resuelto v3.4) | context-degradation como driver del veredicto | latent-briefing de Agent-Skills (requiere KV-cache runtime) | infinity/Docker como backend RAG baseline | embeddings densos como baseline RAG (BM25 suficiente) | RAG de contenido en ContextBuilder (document-free) | re-implementar lógica de pipeline en el wizard | **pre-cargar corpus jurisdiccional por país en el repo (no escala) — s24** | **floor R2 por score BM25 (frágil en corpus pequeños; usar overlap) — s24.**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v23.md` (v22 a borrar s24)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. **Si mi-filesystem timeoutea: `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop.**
- **Método de edición:** stamps multi-archivo = `bump_stamps.ps1` (anclado, dry-run → -Apply). Edits de prosa multi-archivo = script `.Replace` all-or-nothing. Edits pequeños/archivo nuevo = mi-filesystem directo (preserva escapes byte-exacto). Edits quirúrgicos en archivos grandes = Ruta 3. `github:create_or_update_file` prohibido por defecto. NO puedo ejecutar Python/PowerShell en la máquina de JARP → JARP corre regresión y scripts.
- **BYO corpus runtime:** `python main.py --type legal --subscenario lease --objective "..." --tribunal --corpus laws/x.pdf laws/y.txt` (cualquier jurisdicción). Sin `--corpus` → R2 no-op, legacy preservado.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py`. Offline esperado 11 PASS / 1 SKIP. **`pip install rank_bm25` + `pydantic` antes de correr el agente** (si faltan, R1/R2 degradan a legacy).
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real + sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commit sugerido para cierre sesión 24
**Repo dark-strategist-agent:**
```
feat: DS v3.10.0 — BYO per-case corpus + R2 overlap floor + pydantic + JARP_CERTIFIED PA-20260603-006

Session 24 — track (B): re-scoped corpus R2 from "pre-load laws per jurisdiction"
(does not scale) to BYO per-case mechanism. --corpus flag (main.py) + wizard step 7
+ retriever.load_corpus_files (.jsonl/.txt/.md + PDF/DOCX via markitdown) +
corpus_paths (schema/context_builder/tribunal). R2 relevance floor switched from
BM25-score to token-overlap (score floor false-negatives on tiny corpora, IDF=0).
pydantic>=2.0.0 declared. Atomic §4.14.1 stamp bump. Non-forensic (feed-layer;
prompt/skill/verdict surface byte-identical except stamps). Repo contains no laws;
JURISDICTION_CORPUS_MAP stays {} (optional hook). Roadmap item "corpus R2" CLOSED
as mechanism, not data. Re-cert PA-20260603-006, 0/0/0/0, BIAS PASS, supersedes
PA-20260603-004.

NEW: dark-strategist-continuity-prompt_v23.md (replaces v22)
DELETED: dark-strategist-continuity-prompt_v22.md
```
**Repo jarp-toolkit:**
```
docs: sync DS v3.10.0 / PA-20260603-006 (BYO corpus + overlap floor) — header + #16 + #30 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 24

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.10.0** | **PA-20260603-006** | **v3.10.0** | ✅ ACTIVE | 03/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 24 (auto-mejora del próximo Claude)

1. **Confronta el roadmap contra el código real ANTES de ejecutar.** s24 encontró DOS desalineamientos: (a) el map es por DOMINIO, no jurisdicción; (b) pre-cargar leyes no escala. JARP confrontó (b); el resultado fue un re-scopeo a BYO que es la arquitectura correcta. Cuando el roadmap pide "poblar X", preguntar primero si "poblar" es siquiera la jugada correcta vs "habilitar mecanismo".
2. **Valida retrieval con corpus PEQUEÑO.** El floor score-based pasó en sandbox (corpus de 5) y falló en máquina real (corpus de 2, IDF=0). El edge case de BYO es corpus diminuto. Probar siempre 2-3 pasajes.
3. **Baseline regresión PRE-cambio + deps check** atrapó que `rank_bm25` no estaba instalado en el Python de JARP → R1/R2 corrían degradados a legacy. Sin ese check, todo "verde" habría sido un espejismo.
4. **Para entregar archivos a JARP:** escritura directa vía mi-filesystem garantiza ubicación (JARP a veces descarga a Downloads y no mueve). Preferir mi-filesystem sobre present_files para archivos que DEBEN quedar en una ruta exacta. mi-filesystem preserva escapes `\n` byte-exacto (verificado con probe).
5. **No puedo ejecutar en la máquina de JARP.** JARP corre regresión (`test_wizard.py`, `smoke_test_e2e.py`, `byo_check.py`) y los scripts. Gate regresión-verde ANTES de mover versión/cert.
6. **TRADING: 21 SESIONES POSTERGADO (4-24).** NO re-confrontar. Si s25 no elige A, asumir prioridad real ≠ escrita.
7. **DS roadmap = 100% cerrado.** Próximas sesiones: o trading (A), o WATCH menores (scripts→tools/, smoke BYO-case), o nuevas ideas del pipeline.
