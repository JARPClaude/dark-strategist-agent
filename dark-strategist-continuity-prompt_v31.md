# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 11/06/2026 (sesión 32 — DS v3.18.0 LW-3 signal-provenance granularity, shipped & JARP_CERTIFIED) | **Para:** Sesión 33
**Reemplaza:** v30 del 07/06/2026 (sesión 31)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v31.md`
**⚠️ BORRAR en este cierre:** v30 (`git rm` en el commit de cierre). v31 = único continuity vigente. Subir v31 al PROYECTO claude.ai + quitar v30.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 32 (resumen ejecutivo)

Track elegido: **B — Backlog valor-agregado → LW-3** (signal-provenance granularity). Trading (A) NO se eligió (**29ª sesión postergada, 4–32**).

**Resultado: DS v3.18.0 shipped y CERTIFICADO** (`PA-20260611-002`).

### 1. DS v3.18.0 — LW-3 SIGNAL-PROVENANCE GRANULARITY (UX)
`retriever.load_corpus_files` spliteaba `.txt` por `\n\n` (párrafo) para AMBOS canales. Señales en líneas consecutivas (single `\n`) colapsaban en 1 passage → `_attribute_signal_provenance` mandaba todo finding a un solo `signal #N`. Repro: `_livewatch/signals_acme.txt` (header + 4 señales consecutivas → default 2 passages, las 4 mascadas en 1).

**Restricción crítica descubierta leyendo el código vivo (no anotada en el backlog):** `load_corpus_files` es **compartida por dos canales** — señales (`_active_signals`) Y corpus (`_active_corpus`). El corpus NECESITA el split `\n\n` (una cláusula/ley multi-línea debe seguir siendo UN passage para grounding BM25). Cambiar el split global a per-línea rompería R2. → El fix **debe ser per-canal**.

**Fix (contrato per-canal, byte-idéntico para corpus):**
- `retriever.load_corpus_files` gana param `txt_atomic_lines=False`. Rama `.txt`: `txt.split("\n")` si True (una señal por línea), `txt.split("\n\n")` si False (default = legacy, corpus byte-idéntico). `.jsonl` ya per-línea (sin cambio). Binarios/markup siguen por `chunk()` (fuera de scope).
- `tribunal_transversal.run`: el loop de señales llama `load_corpus_files(_p, txt_atomic_lines=True)`; la llamada de corpus `load_corpus_files(_byo)` SIN tocar (default) → grounding byte-idéntico (garantía estructural; `r2_byo_corpus legacy_byte_identical=True`).
- **`orchestrator/test_signals_granularity.py`** (NUEVO): 6 checks offline $0 — default colapsa líneas consecutivas (legacy), atomic = una por línea, atomic dropea blancos, **CORPUS guard** (default `\n\n` mantiene cláusula multi-línea en 1 passage), repro shape (default 2 / atomic 6), **e2e distinct-index** (dos findings sobre dos señales distintas → `signal_index` `[0,1]`; corre de verdad, no SKIP).

### 2. DEFECTO LATENTE QUE YO INTRODUJE (caught pre-cert)
El bloque que entregué para `retriever.py` reusaba `raw = f.read()` DENTRO de `for raw in paths:` → **shadowing de la variable de loop**. Funcionalmente inerte hoy (path ya capturado en `path`; `raw` no se reusa después en la iteración; el `for` rebindea en la siguiente vuelta), pero footgun latente. El **read-back de mi propio bloque aplicado** lo destapó → renombrado a `txt` antes de cualquier test/commit. Lección: leer de vuelta lo que UNO mismo entregó paga; no shippear shadowing en un release certificado (directiva robustez s28).

### 3. RE-CERT DS v3.18.0 — COMPLETA ✅ (CONFIRMATORY)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260611-001`) PASS. 7-ejes Level 1 JARP DEEP sobre delta v3.17.0→v3.18.0.
- **Por qué CONFIRMATORY:** el fix vive 100% en la **capa de carga de señales + reporte post-veredicto** del orchestrator. NO toca la superficie prompt/skill forense (19 variants + 7 skills + base + router CONTENT byte-idéntico salvo stamps). Corpus grounding byte-idéntico (`r2_byo_corpus`). Provenance es determinista, POST-veredicto, report-only.
- **Evidencia funcional (máquina real, post-apply + post-bump):** `test_signals_granularity` 6/6 + `test_provenance` 12/12 + `smoke_test_e2e` **ALL PASS** (`c_fallback_intact` + `e_monotonic_verdict` INVIABLE + `r2_byo_corpus legacy_byte_identical=True`). Confirmación live load-level: corrida real `--signals` reportó `Ext.signals: ACTIVE — 6 evidence passage(s)` (split atómico activo end-to-end; pre-fix serían 2). + ruteo LW-1 re-confirmado en vivo (`strategy_acme_board_proposal` → Strategy).
- **CERT EMITIDO:** `PA-20260611-002` — DS **v3.18.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **11/09/2026 o v4.0.0**. **SUPERSEDES PA-20260607-002** (v3.17.0).
- **WATCH (registrado en CHANGELOG):** `b_unified_output` SKIPea en shell offline limpio (sin key) y, con dummy key + proxy caído, PASA vía la forma del fallback determinista (agentes connection-error → fallback → UnifiedVerdictOutput válido); el **JSON shape de modelo vivo sigue sin ejercerse** — mismo gap ambiental que v3.16/v3.17, no-bloqueante.
- **Bump:** `bump_stamps.ps1 -OldVersion 3.17.0 -NewVersion 3.18.0 -Apply` (23 files/69 stamps) + `bump_manual_v3_18_0.py` (4 banners operator-visible: main×2 / wizard / transparency + bloque CHANGELOG [3.18.0]; newline-aware, all-or-nothing, dry-run→apply). Banners frozen NO tocados (docstrings de módulo retriever v3.10.0 / main+wizard v3.10.0 / context_builder+tribunal v3.0.0; tribunal provenance feature-landing v3.15.0). One-shot BORRADO antes del commit.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.18.0 = CERTIFICADO (`PA-20260611-002`).** Sin version-gap. PA-20260607-002 (v3.17.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s32)
1. Archivos en disco (PHASE 2): `orchestrator/retriever.py` (param `txt_atomic_lines` + rama `.txt` per-canal, `txt` sin shadow), `orchestrator/tribunal_transversal.py` (señales con `txt_atomic_lines=True`), `orchestrator/test_signals_granularity.py` (NUEVO).
2. Bump aplicado (PHASE 3): `bump_stamps.ps1 -Apply` (prompts/README/CLAUDE) + `bump_manual_v3_18_0.py --apply` (banners main×2/wizard/transparency + CHANGELOG [3.18.0] con WATCH).
3. CHANGELOG: bloque `[3.18.0]` con cert `PA-20260611-002` + WATCH insertado sobre `[3.17.0]`.
4. `git rm dark-strategist-continuity-prompt_v30.md`.
5. `jarp-toolkit` + `.claude-init.md` → v3.18.0/PA-20260611-002 vía one-shot anclado `sync_canonicals_v3_18_0.py` (8 edits, all-or-nothing; header + #30 Version/CERT STATUS/Previous-certs + #16×2; init header + #7; superseded += PA-20260607-002). Verificado: re-corrida dry-run ABORTA con 8/8 anchors count 0 + grep `PA-20260611-002` hits en ambos. Commit separado en repo jarp-toolkit.
6. **One-shots BORRADOS** antes de cada commit: `bump_manual_v3_18_0.py` (DS) + `sync_canonicals_v3_18_0.py` (jarp-toolkit).
7. **Verificación post-push:** AMBOS canónicos concuerdan en v3.18.0/PA-20260611-002 (drift-check s29 OK). HEAD remoto confirmado vía `list_commits`.

---

## DEUDA TÉCNICA — POST-SESIÓN 32

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.18.0** | ✅ CERRADA | v3.18.0 CERTIFICADO (PA-20260611-002) | 0/0/0/0, CONFIRMATORY. |
| **LW-3 provenance granularity** | ✅ CERRADA | `txt_atomic_lines` per-canal; señales per-línea, corpus byte-idéntico | test 6/6 incl. e2e distinct-index; live 6 passages. |
| **LW-1 domain resolver** | ✅ CERRADA (s31) | boundary-aware + most-specific-first + order-invariant | Sin cambio. Re-confirmado en vivo s32. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟠 LW-2 (mejora):** confidence corroboración frágil. `_apply_confidence` arma `multi_agent_confirmed` por `(severity, _norm_title)` sobre findings crudos; los títulos divergen entre agentes Y el sintetizador reescribe los unificados → consenso unánime registra `Confirmed by 2+: 0` → `driver_corroborated=False` → confianza sesgada a la baja. NON-BINDING (veredicto intacto). Mejora: corroborar por acuerdo de veredicto / similitud semántica, o propagar source-agent por finding. **Slice propio, mayor sustancia del backlog — candidato #1 para s33.**
- **🟢 LW-4 (refinamiento opcional):** desempate de dominio **posicional** ("gana el primer token de dominio del filename") como alternativa al most-specific/longest-first actual. LW-1 ya cierra el defecto; esto es pulido de intuición. Evaluar valor real antes de invertir — candidato a descartar.
- **P5 extensión P14/P20** (candidato): extender reputational-risk a Public Sector (P14) + Startup (P20) — Activation v1.1.0 + Failure Catalog rows (prefijos PS/SU). El "3+2" diferido; cobertura ya lograda con P11/P16/P19 es razonable; valor incremental dudoso.
- **WATCH live-model JSON shape:** `b_unified_output` aún no ejercido contra modelo real (solo fallback shape). Para cerrarlo de verdad: levantar `fcc-server` en :8082 con `MODEL_OPUS` mapeado a backend free, correr smoke con tráfico real. Gap ambiental, no de código.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real.

---

## ESTADO ACTUAL VERIFICADO (11/06/2026 — fin s32)

### Repo dark-strategist-agent
- **v3.18.0 — CERTIFICADO (`PA-20260611-002`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.18.0 (**registrar SHA tras push**). HEAD previo (inicio s32) = `30ead2f`.
- **MODIFICADO:** `orchestrator/retriever.py` (`load_corpus_files` + `txt_atomic_lines` per-canal); `orchestrator/tribunal_transversal.py` (señales `txt_atomic_lines=True`). **NEW:** `orchestrator/test_signals_granularity.py` (6 checks).
- **De s31 vigente:** `_resolve_domain` boundary-aware + most-specific-first + order-invariant (+`import re`/`_SEP`) en `context_builder.py`; `test_domain_resolver.py` (23 checks).
- **De s30 vigente:** `skills/reputational-risk/SKILL.md` (v1.0.0) + `SKILLS_CATALOG` + bullet base #7 + RULES/rows P11/P16/P19 + `test_reputational_risk.py`.
- **De s29 vigente:** `overlap_score` + `_active_signals_tagged` + `_attribute_signal_provenance` post-veredicto + bloque `SIGNAL PROVENANCE` + `rag.provenance_min_overlap` + `test_provenance.py`.
- **De s28 vigente:** canal `--signals` + `RuntimeContext.signals_paths` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26/s25 vigente:** `schema.should_escalate`/`_maybe_escalate` + `test_escalation.py`; `schema.compute_confidence`/`_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (NO cubre orchestrator/*.py ni CHANGELOG; **dry-run por defecto — requiere `-Apply` para escribir**). `gc.auto 0` activo. `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus`/`--signals` activos.
- **7 skills**, **9 sub-agentes N2 permanentes**, **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only). `_livewatch/` throwaway no-commiteado (`signals_acme.txt` + `strategy_acme_board_proposal.txt`).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s32. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/CERT STATUS/Previous certs) + #16 + `.claude-init.md` #7 → v3.18.0/PA-20260611-002. PRIVADO. **AMBOS canónicos concuerdan (verificado al cierre).**

### free-claude-code
- Proxy $0 para corridas no-cert. **`fcc-server` NO en PATH ni levantado — instalar/arrancar antes de usar** (Python 3.14+, `uv`, `fcc-server` o `uv run uvicorn server:app --host 0.0.0.0 --port 8082`, Admin UI `/admin` → mapear `MODEL_OPUS` a backend free). **El SDK de anthropic exige `api_key` no vacío aunque uses proxy** → setear `ANTHROPIC_API_KEY="sk-local-dummy"` (gate del SDK, NO se factura) + `ANTHROPIC_BASE_URL=http://localhost:8082`. Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 33
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v31).
2. **PHASE 0 — Verificación:**
   - v30 borrado, v31 único continuity.
   - Repo en v3.18.0. **Cert: DS v3.18.0 `PA-20260611-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260607-002` SUPERSEDED.
   - **Verificar AMBOS canónicos concuerdan** (toolkit + init en v3.18.0/PA-20260611-002) — lección drift s29.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 29 SESIONES (4–32).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s33 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — LW-2 (confidence corroboración, candidato #1); LW-4 (desempate posicional, opcional); P5 extensión P14/P20; WATCH live-model (ambiental, requiere fcc-server arriba).
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes+comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE | RAG = MECANISMO | ContextBuilder document-free | infinity/Docker RECHAZADO | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case | Floor R2/señales/provenance = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25–s31:** Confianza/escalación/lentes/señales/provenance = metadata NO-VINCULANTE, determinista, post-hoc donde aplica; NUNCA tocan `final_verdict`/`Finding`. Docstrings de módulo congelados. Scripts de edición newline-aware + encadenados por archivo + all-or-nothing + dry-run. Riesgo reputacional = SKILL markdown (#7), NO lente-arquetipo; Failure Catalog VINCULA severidad; `VERDICT_IMPACT: NONE` = no computa/override, NO sin-severidad; activación⊆binding. Domain routing = boundary-aware + MOST-SPECIFIC-FIRST + ORDER-INVARIANT (claves ≤3 whole-token; compuestas = frase; largas = token-equal/prefix); `_resolve_domain` upstream de synthesis, no toca verdict path.

**De s32 (nuevas):**
- **Segmentación `.txt` per-canal:** señales = una por línea (`txt_atomic_lines=True`, ítems atómicos time-sensitive direccionables por provenance); corpus = párrafo `\n\n` (cláusula multi-línea = UN passage para BM25). `load_corpus_files` compartida → el flag selecciona por canal; corpus load byte-idéntico (default False). **NO cambiar el split `.txt` globalmente** (rompería grounding de corpus).
- **Provenance granularity es POST-veredicto y determinista** → su corrección se prueba 100% offline (el e2e `t_e2e_distinct_index` ejerce el código real de atribución); el modelo no interviene.
- **Leer de vuelta lo que UNO mismo entregó** — el read-back de mi propio bloque destapó un shadowing de loop-var (`raw`) que yo introduje; renombrado a `txt` pre-cert. No shippear footguns autoría-propia en un release certificado.
- **`bump_stamps.ps1` es dry-run por defecto** → SIEMPRE re-correr con `-Apply` para escribir (near-miss s32: el dry-run sin `-Apply` deja product-face en la versión vieja → drift si se commitea). Verificar con `Select-String prompts\*.md,README.md,CLAUDE.md -Pattern "<old-version>"` → 0.
- **free-claude-code gate del SDK:** `ANTHROPIC_API_KEY` no vacío es obligatorio aunque uses `ANTHROPIC_BASE_URL` (proxy) — usar dummy `sk-local-dummy` (NO se factura, el proxy enruta a free). Si el agente da `Connection error` → fcc-server caído (no auth). Costo Anthropic en no-cert = $0 garantizado por el base_url local.
- **One-shot para canónicos (jarp-toolkit) validado** como método seguro en edits grandes: anclado all-or-nothing aborta limpio si una ancla falla; la re-corrida post-apply que ABORTA con todos los anchors en count 0 es prueba de completitud por idempotencia. (Desviación de Ruta-3 aprobada explícitamente por JARP en s32; usar con OK explícito.)

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica | bumpear docstrings/catálogo/comments-feature-landing congelados | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts que escriben cada edit desde el snapshot original | activación dormida sobre activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` | riesgo reputacional como lente-arquetipo (usar SKILL) | duplicar Failure-Catalog rows (REUSAR) | activar skill en dominios sin Failure Catalog rows | transcribir líneas largas como anclas (usar line-based) | domain routing por substring crudo / acoplado al orden de inserción del dict (usar boundary-aware + most-specific-first + order-invariant — s31) | borrar claves cortas del DOMAIN_MAP para arreglar el bleed (whole-token las preserva — s31) | **cambiar el split `.txt` de `load_corpus_files` globalmente a per-línea — rompe el grounding de corpus; usar el flag per-canal `txt_atomic_lines` — s32** | **reusar la variable de loop (`for raw in paths`) como buffer de lectura — shadowing; usar nombre local distinto — s32** | **correr `bump_stamps.ps1` sin `-Apply` y asumir que escribió — s32**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v31.md` (v30 borrado s32)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. env var = `$env:VAR="..."`. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). `bump_stamps.ps1` con params NOMBRADOS + **`-Apply` para escribir** (`-OldVersion X -NewVersion Y -Apply`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1 -Apply`. Banners orchestrator + CHANGELOG = script Python anclado all-or-nothing + NEWLINE-AWARE (dry-run → --apply), a la RAÍZ. Edits prosa/código pequeños/archivo nuevo = mi-filesystem directo (full-overwrite; verificar read-back). Canónicos (archivos grandes) = **Ruta-3** por defecto, o **one-shot anclado** con OK explícito (s32). `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Domain routing (`--document` mode):** dominio del STEM del filename, boundary-aware + most-specific-first. Pinear con `--type X`.
- **Signals (`--signals` mode):** `.txt` se carga **una señal por línea** (LW-3). Corpus (`--corpus`) sigue por párrafo. Provenance atribuye cada finding a su señal específica.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **13 PASS / 0 FAIL** si hay key+proxy (b vía fallback), o **12 PASS / 1 SKIP** offline limpio. Tests s32: `test_signals_granularity` 6/0. `pip install rank_bm25 pydantic` antes.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 32
**Repo dark-strategist-agent (v3.18.0 cert) — commit atómico:**
```
fix: DS v3.18.0 — signal-provenance granularity LW-3 (txt_atomic_lines per-channel .txt split; signals per-line, corpus byte-identical) — test_signals_granularity 6/6 incl. e2e distinct-index + JARP_CERTIFIED PA-20260611-002
```
Incluye: `orchestrator/retriever.py`, `orchestrator/tribunal_transversal.py`, `orchestrator/test_signals_granularity.py`, banners (`orchestrator/{main,wizard,tribunal_transversal}.py`) + prompts/README/CLAUDE stamps (bump_stamps), `CHANGELOG.md`, `dark-strategist-continuity-prompt_v31.md`; `git rm dark-strategist-continuity-prompt_v30.md`. NO incluye el one-shot (`bump_manual_v3_18_0.py`, borrado).
**Repo jarp-toolkit:**
```
docs: sync DS v3.18.0 / PA-20260611-002 (LW-3 signal-provenance granularity) — header + entry #30 (Version/cert/superseded) + note #16 + .claude-init #7
```
NO incluye el one-shot (`sync_canonicals_v3_18_0.py`, borrado).

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 32

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.18.0** | **PA-20260611-002** | **v3.18.0** | ✅ ACTIVE | 11/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 32 (auto-mejora del próximo Claude)

1. **El backlog no veía la restricción per-canal.** LW-3 parecía "splitear señales por línea"; leer el código vivo reveló que `load_corpus_files` es compartida con el corpus, que NECESITA `\n\n`. El fix correcto es per-canal, no global. Leer el módulo real antes de diseñar paga (otra vez).
2. **Read-back de lo propio.** El shadowing `raw` lo introduje YO en el bloque entregado; el read-back tras aplicar lo destapó. Verificar lo que uno mismo escribe, no solo lo que escribe el usuario.
3. **`bump_stamps` dry-run por defecto.** Casi se commitea con product-face en 3.17.0 porque la primera corrida fue sin `-Apply`. Checklist: tras bump_stamps, grep `<old-version>` en product-face → 0 ANTES de seguir.
4. **free-claude-code: dummy key + proxy.** El SDK exige key no vacío; dummy `sk-local-dummy` pasa el gate sin facturar; el tráfico va al proxy local → backend free. `Connection error` = proxy caído (no auth). Regla permanente reforzada por JARP: free para no-cert, Opus real solo cert-grade.
5. **One-shot anclado para canónicos** (con OK explícito de JARP) = método robusto para edits grandes: all-or-nothing + la re-corrida post-apply que ABORTA con todos los anchors en 0 prueba completitud por idempotencia. Mejor que Ruta-3 manual cuando el volumen/densidad de chars especiales es alto.
6. **Honestidad en el cert:** `b_unified_output` pasó vía fallback (no modelo vivo) → se registró WATCH en CHANGELOG en vez de sobre-afirmar "live JSON validado". El JSON de modelo vivo sigue sin ejercerse.
7. **TRADING: 29 SESIONES POSTERGADO (4–32). NO re-confrontar.**
8. **Próximo candidato #1: LW-2** (confidence corroboración) — la mejora de mayor sustancia que queda. LW-4 y P5 huelen a barato-dormido; evaluar valor real antes de invertir.
