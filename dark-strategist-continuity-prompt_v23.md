# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 03/06/2026 (sesión 24 — DS v3.10.0 BYO corpus per-case + R2 overlap floor + pydantic, shipped & JARP_CERTIFIED) | **Enmendado:** 04/06/2026 (rama B housekeeping cerrada) | **Para:** Sesión 25
**Reemplaza:** v22 del 03/06/2026 (sesión 23)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v23.md`
**⚠️ BORRAR en este cierre:** v22 (`git rm` en el commit de cierre). v23 = único continuity vigente. Subir v23 al PROYECTO claude.ai + quitar v22.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 24 (resumen ejecutivo)

Track (B) elegido: **roadmap restante**. El último ítem (corpus R2) se **re-scopeó** tras confrontación de JARP: de "pre-cargar leyes por jurisdicción" (no escala) → **mecanismo BYO per-case**. Resultado: **DS v3.10.0 shipped y CERTIFICADO** (`PA-20260603-006`). Bump **no-forense** (feed-layer). Trading (A) NO se eligió (21ª sesión postergada).

**ADENDA 04/06 — rama (B) WATCH menores CERRADOS** (housekeeping, sin bump ni re-cert; `PA-006` intacto): scripts→`tools/` + caso BYO en el smoke. Incidente OneDrive/git resuelto sin daño. Detalle en tabla de deuda + decisiones + lecciones. Repo HEAD ahora `feb93be`.

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

### 4. (B) RAMA WATCH MENORES — CERRADA 04/06 (housekeeping, sin re-cert)
- **scripts→tools/:** `bump_stamps.ps1` movido a `tools/` (tooling reutilizable). `git mv` falló (dir destino inexistente + posible untracked) → patrón robusto `New-Item -Force tools` + `Move-Item -Force` + `git add -A`.
- **smoke BYO-case:** check **`r2_byo_corpus`** añadido a `smoke_test_e2e.py` (offline; `load_corpus_files` → R2 token-overlap floor: inyecta relevante, descarta ruido zero-overlap, legacy byte-idéntico). Smoke local **12 PASS / 1 SKIP**, `r2_byo_corpus` PASS. **`smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS** (paths locales hardcoded) → la mejora vive en la máquina local, NO en el repo (por diseño). El commit inicial prometía el caso BYO en el repo (inexacto) → **enmendado** a `chore: move bump_stamps.ps1 to tools/` (`git commit --amend` + `git push --force-with-lease`, HEAD `feb93be`).
- **Incidente OneDrive/git:** `git gc --auto` post-commit disparó bucle `Deletion of directory '.git/objects/XX' failed (y/n)`. **`n` a todos = SEGURO** (commit intacto, solo omite poda de sueltos). `git fsck --full` LIMPIO (2 dangling trees = normal). `git config gc.auto 0` aplicado en DS como guarda permanente.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.10.0 = CERTIFICADO (`PA-20260603-006`).** Sin version-gap. PA-20260603-004 (v3.9.0) → SUPERSEDED. La rama (B) housekeeping NO tocó el agente → cert intacto.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s24) ✅
1. Los 8 archivos en `orchestrator/` colocados (byo_check NO commiteado).
2. **Stamps anclados:** `bump_stamps.ps1 3.9.0→3.10.0 -Apply` → 23 files / 69 stamp lines.
3. **Edits de prosa no-anclados:** CHANGELOG `[3.10.0]`, filas roadmap README+CLAUDE, status `ACTIVE → v3.10.0` en CLAUDE — aplicados.
4. `jarp-toolkit/JARP_TOOLKIT.md` — header + #16 + #30 + Note ajustados → v3.10.0/PA-006.
5. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.10.0/PA-006.
6. Temporales `byo_check.py` + `_byo_sample.jsonl` borrados.
7. Continuity v23 commiteado; `git rm` v22.
8. **(rama B, 04/06):** `tools/bump_stamps.ps1` versionado; caso BYO en smoke local; `gc.auto 0`.

---

## DEUDA TÉCNICA — POST-SESIÓN 24

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.10.0** | ✅ CERRADA | v3.10.0 CERTIFICADO (PA-20260603-006) | 0/0/0/0. |
| **corpus R2** | ✅ CERRADA (re-scopeada) | Mecanismo BYO per-case shipped | Roadmap cerrado como MECANISMO, no data. Repo no contiene leyes. |
| **pydantic en requirements** | ✅ CERRADA | `pydantic>=2.0.0` declarado | — |
| **scripts helper en repo** | ✅ CERRADA (04/06) | `bump_stamps.ps1` → `tools/` | Tooling reutilizable versionado. HEAD `feb93be`. |
| **smoke desactualizado** | ✅ CERRADA-funcional (04/06) | caso `r2_byo_corpus` añadido | Ejercita R2 BYO offline (12 PASS/1 SKIP local). **Smoke GITIGNORADO** (paths locales) → vive local, fuera del repo por diseño. |
| **clash n>0 live + gate b live** | 🟢 WATCH | `b_unified_output` necesita Opus real (key) | Pendiente validación con key. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

**El TOP-7 + corpus R2 + los WATCH menores (scripts, smoke BYO) están CERRADOS. DS roadmap = 100%.** Solo queda WATCH de validación live con key (no-bloqueante).

---

## ESTADO ACTUAL VERIFICADO (04/06/2026 — fin rama B)

### Repo dark-strategist-agent
- **v3.10.0 — CERTIFICADO (`PA-20260603-006`)**. Default `claude-opus-4-7`. HEAD `feb93be`.
- **NEW:** `orchestrator/load_corpus_files` + `--corpus` + wizard paso 7 + `corpus_paths` (schema/context/tribunal). Floor R2 overlap-based.
- **`tools/bump_stamps.ps1`** (tooling). **`gc.auto 0`** (guarda OneDrive, config local).
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}` (gancho dormido; BYO es la vía activa).
- **6 skills** (sin cambio). **9 sub-agentes N2 permanentes** (sin cambio).
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only, paths personales) — contienen el caso `r2_byo_corpus`.

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
   - Repo en v3.10.0, HEAD `feb93be`. **Cert registry: DS v3.10.0 `PA-20260603-006` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260603-004` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados (sin ellos R1/R2 corren degradados a legacy).
   - `gc.auto 0` activo (no esperar el bucle OneDrive en commits).
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 21 SESIONES (4-24).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) DS roadmap** — **CERRADO 100%** incl. WATCH menores. Solo queda WATCH live-key (no-bloqueante).
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

**De rama B (04/06):**
- **`smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS** (paths locales hardcoded → `C:\...\Downloads\`). Las mejoras al smoke (p.ej. `r2_byo_corpus`) viven en la máquina local y corren en cada regresión, pero NO se versionan. NO forzar al repo (`git add -f`) sin parametrizar primero los paths personales.
- **OneDrive + git gc:** `git gc --auto` post-commit dispara el bucle `Deletion of directory '.git/objects/XX' failed (y/n)` porque OneDrive lockea `.git/objects/`. Responder **`n` a todos es SEGURO** (commit ya escrito; solo se omite la poda de objetos sueltos, redundantes con el packfile). `git config gc.auto 0` aplicado como guarda. Mantener **OneDrive en PAUSA** durante operaciones git pesadas (gc, push grande, amend).
- **Higiene de mensaje de commit:** verificar QUÉ entró realmente (`git log -1` / clone fresco) antes de dar por bueno un mensaje — un archivo gitignorado se omite en silencio y el mensaje puede sobre-prometer. Enmendar con `--amend` + `--force-with-lease` si el historial quedó inexacto (repo personal, sin colaboradores).

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | UNIT-INGEST como sub-agente del spawner | Severity×Likelihood como dimensión VINCULANTE | skills knowledge-work descartadas | re-trabajar el telephone-game (resuelto v3.4) | context-degradation como driver del veredicto | latent-briefing de Agent-Skills (requiere KV-cache runtime) | infinity/Docker como backend RAG baseline | embeddings densos como baseline RAG (BM25 suficiente) | RAG de contenido en ContextBuilder (document-free) | re-implementar lógica de pipeline en el wizard | **pre-cargar corpus jurisdiccional por país en el repo (no escala) — s24** | **floor R2 por score BM25 (frágil en corpus pequeños; usar overlap) — s24** | **forzar el smoke al repo sin parametrizar paths locales — s24/B.**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v23.md` (v22 borrado s24)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para operaciones git pesadas; `gc.auto 0` ya activo en DS.**
- **MCPs:** mi-filesystem, GitHub. **Si mi-filesystem timeoutea: `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop.**
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1` (anclado, dry-run → -Apply). Edits de prosa multi-archivo = script `.Replace` all-or-nothing. Edits pequeños/archivo nuevo = mi-filesystem directo (preserva escapes byte-exacto). Edits quirúrgicos en archivos grandes = Ruta 3. `github:create_or_update_file` prohibido por defecto. NO puedo ejecutar Python/PowerShell en la máquina de JARP → JARP corre regresión y scripts.
- **BYO corpus runtime:** `python main.py --type legal --subscenario lease --objective "..." --tribunal --corpus laws/x.pdf laws/y.txt` (cualquier jurisdicción). Sin `--corpus` → R2 no-op, legacy preservado.
- **Smoke-test E2E (LOCAL, gitignorado):** `orchestrator/smoke_test_e2e.py`. Offline esperado **12 PASS / 1 SKIP** (incl. `r2_byo_corpus`). **`pip install rank_bm25` + `pydantic` antes de correr el agente** (si faltan, R1/R2 degradan a legacy).
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real + sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 24
**Repo dark-strategist-agent (v3.10.0 cert) — pusheado.**
```
feat: DS v3.10.0 — BYO per-case corpus + R2 overlap floor + pydantic + JARP_CERTIFIED PA-20260603-006
```
**Repo dark-strategist-agent (rama B housekeeping) — HEAD feb93be.**
```
chore: move bump_stamps.ps1 to tools/
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
4. **Para entregar archivos a JARP:** escritura directa vía mi-filesystem garantiza ubicación. mi-filesystem preserva escapes `\n` byte-exacto (verificado con probe).
5. **No puedo ejecutar en la máquina de JARP.** JARP corre regresión y scripts. Gate regresión-verde ANTES de mover versión/cert.
6. **TRADING: 21 SESIONES POSTERGADO (4-24).** NO re-confrontar. Si s25 no elige A, asumir prioridad real ≠ escrita.
7. **DS roadmap = 100% cerrado** (incl. WATCH menores rama B). Próximas sesiones: trading (A), WATCH live-key, o nuevas ideas del pipeline.
8. **Verifica el push por CONTENIDO, no por mensaje** (rama B): un archivo gitignorado se omite en silencio; el mensaje del commit puede sobre-prometer. Clone fresco / `git log -1` antes de cerrar. Enmendar con `--amend`+`--force-with-lease` si el historial quedó inexacto.
9. **OneDrive + git:** `gc.auto 0` ya aplicado; OneDrive en PAUSA para git pesado. Bucle de borrado `.git/objects` → `n` a todo es seguro.
