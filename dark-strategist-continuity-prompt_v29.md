# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 06/06/2026 (sesión 30 — DS v3.16.0 reputational-risk skill #7, shipped & JARP_CERTIFIED) | **Para:** Sesión 31
**Reemplaza:** v28 del 06/06/2026 (sesión 29)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v29.md`
**⚠️ BORRAR en este cierre:** v28 (`git rm` en el commit de cierre). v29 = único continuity vigente. Subir v29 al PROYECTO claude.ai + quitar v28.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 30 (resumen ejecutivo)

Track elegido: **P5 — riesgo reputacional** (Backlog valor-agregado). Trading (A) NO se eligió (**27ª sesión postergada, 4–30**).

**Resultado: DS v3.16.0 shipped y CERTIFICADO** (`PA-20260606-006`).

### 0. DRIFT FIX al arranque (PHASE 0)
`JARP_TOOLKIT.md` quedó **un minor atrás** del cierre s29 (mostraba v3.14.0/PA-20260606-002 en header + #30 + #16), mientras `.claude-init.md` #7 sí estaba en v3.15.0/PA-20260606-004. Sync parcial detectado en PHASE 0 y corregido (GO-A) ANTES de P5: 6 bloques Ruta 3 → toolkit a v3.15.0/PA-20260606-004. Commit `jarp-toolkit` `0a5afc4`. **Lección: verificar AMBOS canónicos concuerdan al cierre, no solo init.**

### 1. DS v3.16.0 — REPUTATIONAL-RISK FORENSIC LENS (skill #7)
Lente de detección **markdown** para riesgo reputacional. Gate skill-vs-lens resuelto a favor de **skill** (activación amplia) sobre lente-arquetipo (dormant, cap=2 → DESCARTE) y sobre bump-cap (band-aid escalation-gated + costo).
- **`skills/reputational-risk/SKILL.md`** (NUEVO, v1.0.0): 5 patrones — misrepresentation/over-claim, broken-promise, stakeholder-betrayal, association-contamination, silence-in-crisis — c/u con Detection + Audit signal. Clon del template `context-degradation`. `VERDICT_IMPACT: NONE`.
- **`orchestrator/catalogs.py`**: `SKILLS_CATALOG += "reputational-risk"` (registry path-only; docstring v3.2.0 congelado, NO tocado).
- **`prompts/system_prompt.md`** (base): +1 bullet skill #7 en composition map.
- **Variants (fásico 3+2):** P11 Media (RULE M05 silence-in-crisis / M06 association-contamination / M07 over-claim + 3 catalog rows), P16 Marketing (RULE MK05 broken-promise + 1 row; **over-claim REUSA MK04 existente — sin duplicar**), P19 Strategy (RULE ST05 stakeholder-betrayal / ST06 association-contamination / ST07 silence-in-crisis + 3 rows). Orden monotónico FATAL→LATENT verificado en los 3.
- **`orchestrator/test_reputational_risk.py`** (NUEVO): 14 checks offline $0 — estructura SKILL.md + 5 patrones + `VERDICT_IMPACT:NONE`; registro `SKILLS_CATALOG`+path; activación⊆binding (P11/P16/P19 tienen tag `[reputational-risk:]`); disciplina de scope (P14/P20 NO bound); no-impacto estructural (`reputational` en orchestrator/*.py solo en catalogs.py).

**GARANTÍA verificada:** skill markdown = **no computa ni referencia el verdict-path** (check #14). Findings reputacionales portan severidad **catalog-bound** y alimentan la tabla monotónica como cualquier finding → **pueden hundir el veredicto (correcto)**. Distinto de la familia metadata P1-P4/provenance (que NUNCA toca el veredicto). `VERDICT_IMPACT: NONE` = la skill no computa/override, NO que sus findings sean sin-severidad.

### 2. DECISIONES CLAVE (s30)
- **Reputational = SKILL markdown, NO lente-arquetipo.** Lente = escalation-gated + capped = dormida (DESCARTE). Skill = activación amplia + forense-nativa (riesgo reputacional es dimensión de severidad de un Finding, no palanca de calidad deliberativa).
- **Severidad la vincula el Failure Catalog del variant** (patrón SOX-tier): la skill nombra y detecta; el catálogo vincula; la tabla determinista computa.
- **Activación⊆binding (regla nueva):** una skill activa SOLO en dominios con Failure Catalog rows. Declarar activación sin rows = findings sin hogar de severidad (prohibido).
- **No-duplicación:** donde un patrón ya está cubierto (over-claim ↔ MK04 en Marketing), se REUSA la row existente; no se duplica.
- **Fásico 3+2** (P11/P16/P19 ahora; P14/P20 → candidato v3.17.0) para acotar superficie de cert.
- **No-impacto estructural (markdown) vs golden runtime (Python):** una skill markdown no tiene code-path de veredicto → el test asserta no-impacto **estructuralmente** (registro + activación⊆binding + ausencia en orchestrator verdict modules), honesto sobre la diferencia con provenance (que era Python y tuvo golden runtime).

### 3. RE-CERT DS v3.16.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260606-005`) PASS (PA-agent sin cambios). 7-ejes Level 1 JARP DEEP sobre delta v3.15.0→v3.16.0.
- **Evidencia funcional (máquina real, post-apply + post-bump):** `test_reputational_risk` 14/14 + `test_provenance` 12/12 + `test_signals` 11/11 + `test_archetype_lenses/escalation/confidence` 10/10 c/u + `test_wizard` 7/7 + `smoke_test_e2e` **0 FAIL / 1 SKIP** (`b_unified_output` = sin ANTHROPIC_API_KEY) con `run()` construyendo el transparency report limpio (banner bump tribunal:649 verificado no-breaking), `e_monotonic_verdict` INVIABLE, `c_fallback_intact` + `r2_byo_corpus` PASS.
- **CERT EMITIDO:** `PA-20260606-006` — DS **v3.16.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **06/09/2026 o v4.0.0**. **SUPERSEDES PA-20260606-004** (v3.15.0). Bump no-forense detección/feed-layer → CONFIRMATORY.
- **Bump:** `bump_stamps.ps1` (23 files / 69 stamps) + `bump_manual_v3_16_0.py` (6 files, newline-aware CRLF, all-or-nothing, line-based roadmap inserts). Dry-run en clon pristino (sandbox) antes del apply. Disjunción/order-independence probada en vivo (README PROTOCOL_STATUS re-ancló 216→217 tras el insert del manual). One-shot BORRADO antes del commit de cert.

### 4. LIVE-WATCH CERRADO (s30 post-cert) — y 3 hallazgos
Corrida live real (key real; Strategy/P19; doc reputacional `_livewatch/strategy_acme_board_proposal.txt` + `_livewatch/signals_acme.txt`; `--tribunal --agents 5 --regime adversarial`). Resultado: 8 calls reales, **síntesis live SIN fallback → `b_unified_output` cerrado** (el único SKIP de cada cert), 4 ROL + 3 FOR live, N2 spawn (UNIT-INQUISITOR + UNIT-COMPLIANCE), **6 FATAL → INVIABLE** determinista, los 5 patrones reputacionales afloraron como findings con severidad catalog-bound, provenance atribuyó post-veredicto, escalación-gate corrió (MODERATE → no disparó), render limpio. **Las 6 capas no-vinculantes (confidence/escalación/lentes/señales/provenance/reputational) quedan saldadas live.** El live destapó 3 hallazgos que el offline/estructural NUNCA habría mostrado (ver backlog LW-1/2/3). Ninguno invalida el cert: veredicto determinista correcto; LW-2/LW-3 son metadata NON-BINDING.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.16.0 = CERTIFICADO (`PA-20260606-006`).** Sin version-gap. PA-20260606-004 (v3.15.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s30)
1. Archivos nuevos (untracked, stagear en GitHub Desktop): `skills/reputational-risk/SKILL.md`, `orchestrator/test_reputational_risk.py`, `dark-strategist-continuity-prompt_v29.md`.
2. Edits Ruta 3 ya aplicados por JARP en editor (Phase 2): catalogs.py (+1 SKILLS_CATALOG), base (bullet), media/marketing/strategy (RULES + rows). Regresión verde 14/14.
3. Bump ya aplicado (Phase 3): bump_stamps 23/69 + bump_manual 6 files. Banners orchestrator v3.16.0; refs frozen v3.15.0 (retriever:38 + tribunal:63/115/575/682) INTACTOS.
4. CHANGELOG: reemplazar la línea `PENDING` por el bloque cert `PA-20260606-006` (Ruta 3, aplicado en cierre).
5. `git rm dark-strategist-continuity-prompt_v28.md`.
6. `jarp-toolkit` + `.claude-init.md` → v3.16.0/PA-20260606-006 (header + #30 [Version + skills 6→7 + CERT STATUS + Previous certs] + #16 + init #7; superseded += PA-20260606-004). Commit separado en repo jarp-toolkit.
7. **One-shot `bump_manual_v3_16_0.py` YA BORRADO** (mi-filesystem) antes del commit.

---

## DEUDA TÉCNICA — POST-SESIÓN 30

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.16.0** | ✅ CERRADA | v3.16.0 CERTIFICADO (PA-20260606-006) | 0/0/0/0. |
| **P5 reputational-risk** | ✅ CERRADA (fásico 3+2) | Skill #7 markdown, P11/P16/P19 | 7 RULES + 7 rows; test 14/0/0. P14/P20 diferidos. |
| **Drift toolkit (s29)** | ✅ CERRADA | JARP_TOOLKIT.md sincronizado en PHASE 0 s30 | Ambos canónicos ahora concuerdan. |
| **clash/gate/señales/provenance/reputational LIVE** | ✅ CERRADA (s30 post-cert) | `b_unified_output` cerrado vía corrida live real | Strategy/P19, 8 calls, síntesis live (no fallback), 6 FATAL→INVIABLE, reputational 5/5, provenance atribuyó, escalación-gate corrió. Destapó 3 follow-ups → backlog LW-1/2/3. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🔴 LW-1 (DEFECTO — prioridad alta, correctness):** domain resolver false-match por substring. `context_builder._resolve_domain` hace `keyword in subscenario`; la clave de 2 letras `"ma":"Financial"` (y `"ops"`, `"hr"`, `"sop"`) matchea cualquier stem que las contenga → docs con "transformation/marketing/management/summary" mis-rutean a **Financial** → carga el **variant equivocado** en auditorías reales (Failure Catalog + lentes forenses erróneos). Fix quirúrgico: match por **token/word-boundary**, u ordenar claves largas primero, o eliminar claves de 2 letras. Slice propio + re-cert CONFIRMATORY. Repro: `strategy_acme_transformation.txt`→Financial vs `strategy_acme_board_proposal.txt`→Strategy. **Supera en valor a P5-ext (correctness > cobertura).**
- **🟠 LW-2 (mejora):** confidence corroboración frágil. `_apply_confidence` arma `multi_agent_confirmed` por `(severity, _norm_title)` sobre findings crudos de cada agente; los títulos divergen entre agentes Y el sintetizador reescribe los títulos unificados → consenso unánime registra `Confirmed by 2+: 0` → `driver_corroborated=False` → confianza sesgada a la baja (MODERATE pese a 3/3 FOR=INVIABLE). NON-BINDING (veredicto intacto). Mejora: corroborar por acuerdo de veredicto o similitud semántica, o que el sintetizador propague source-agent por finding. Slice propio.
- **🟡 LW-3 (UX — quick):** provenance granularidad por formato de señales. `retriever.load_corpus_files` splitea `.txt` por línea en blanco (`\n\n`); señales en líneas consecutivas colapsan en 1 passage → atribución manda todo a "signal #1" (mecanismo correcto, input mal formateado). Fix: documentar "una señal por párrafo (línea en blanco entre entradas)" o splitear señales `.txt` por línea. Zero/low-code. Repro: `_livewatch/signals_acme.txt`.
- **P5 extensión P14/P20** (candidato v3.17.0): extender reputational-risk a Public Sector (P14) + Startup (P20) — Activation v1.1.0 + Failure Catalog rows (prefijos PS/SU). Es el "3+2" diferido; evaluar si aporta valor real o si P11/P16/P19 ya cubre el grueso.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real.

> Nota inputs live-WATCH: `_livewatch/` (doc Strategy + señales) es **throwaway no-commiteado**. Borrable, o reutilizable para validar LW-3 (re-formatear señales con línea en blanco entre entradas → la atribución discrimina).

---

## ESTADO ACTUAL VERIFICADO (06/06/2026 — fin s30)

### Repo dark-strategist-agent
- **v3.16.0 — CERTIFICADO (`PA-20260606-006`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.16.0 (**registrar SHA tras push**). HEAD previo (inicio s30) = `dea9bc7`.
- **NEW:** `skills/reputational-risk/SKILL.md` (v1.0.0) + `SKILLS_CATALOG` entry + bullet skill #7 en base + RULES/rows en P11/P16/P19 + `test_reputational_risk.py`.
- **De s29 vigente:** `overlap_score` + `_active_signals_tagged` + `_attribute_signal_provenance` post-veredicto + bloque `SIGNAL PROVENANCE` + `rag.provenance_min_overlap` + `test_provenance.py`.
- **De s28 vigente:** canal de señales `--signals` + `RuntimeContext.signals_paths` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26 vigente:** `schema.should_escalate` + `_maybe_escalate`/`_run_escalation_round` + `test_escalation.py`.
- **De s25 vigente:** `schema.compute_confidence` + `_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (anchors PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/-ROUTER/ARCHITECTURAL LAYERS/Version:/version:/VERSION; scope prompts+README+CLAUDE; NO CHANGELOG ni orchestrator/*.py). `gc.auto 0` activo.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` + `--signals` activos.
- **7 skills** (kac, ach, deception, verdict-verification, AAD, context-degradation, **reputational-risk**), **9 sub-agentes N2 permanentes**. **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only). `_livewatch/` throwaway no-commiteado (inputs live-WATCH).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s30. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/skills 7/CERT STATUS/Previous certs) + #16 + `.claude-init.md` #7 → v3.16.0/PA-20260606-006. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). **`fcc-server` NO en PATH — instalar/configurar antes de usarlo.** Cert = Opus real sin proxy. (live-WATCH s30 se cerró con key real, no fcc.)

---

## PROTOCOLO DE INICIO PARA SESIÓN 31
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v29).
2. **PHASE 0 — Verificación:**
   - v28 borrado, v29 único continuity.
   - Repo en v3.16.0. **Cert registry: DS v3.16.0 `PA-20260606-006` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260606-004` SUPERSEDED.
   - **Verificar AMBOS canónicos concuerdan** (toolkit + init en v3.16.0/PA-20260606-006) — lección drift s29.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 27 SESIONES (4–30).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s31 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — **LW-1 domain resolver fix (prioridad alta, correctness)**; LW-2 confidence corroboración; LW-3 provenance granularidad (quick); P5 extensión P14/P20 (cobertura). **live-WATCH ya CERRADO en s30.**
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes + comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | 4 variance decompositions | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE, NO driver | RAG = MECANISMO, NO driver | ContextBuilder document-free | infinity/Docker RECHAZADO | fallback byte-idéntico ante cambio de feed | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2/señales/provenance = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25:** Confianza = metadata NO-VINCULANTE, determinista, ambos caminos. Docstrings de módulo congelados.

**De s26:** Gate de escalamiento NO-VINCULANTE, determinista. Ronda acotada, ids `FOR-ESC-*` distintos, cap por config, budget-gated, degrada offline. Reusa capa Forense. Scripts newline-aware (CRLF en la máquina de JARP — el motor DEBE detectar/preservar el newline por archivo).

**De s27:** Lentes-arquetipo = enriquecimiento NO-VINCULANTE; roles ABSTRACTOS (NUNCA personas reales); catálogo content-based/congelado; bump_stamps y manual DISJUNTOS/order-independent; `-like` PowerShell case-insensitive.

**De s28:** Canal de señales = EVIDENCIA NO-VINCULANTE distinta del corpus; directiva in-band > tocar `prompt_engine`; corpus FUNDAMENTA / señal es EVIDENCIA; scripts de edición DEBEN encadenar ediciones por archivo (validar anclas en memoria sobre TODOS los archivos antes de escribir nada); valor real > valor dormido.

**De s29:** Provenance (`_attribute_signal_provenance`) = hint de auditabilidad HEURÍSTICO NO-VINCULANTE, post-veredicto, report-only, NUNCA toca `final_verdict`/`Finding` (independencia estructural; golden #11). Atribución determinista post-hoc (overlap) > auto-reporte del agente. Report-only, sin campo nuevo en `Finding`. Señales path-tagged con feed proyección byte-idéntica.

**De s30 (nuevas):**
- **Riesgo reputacional = SKILL markdown (#7), NO lente-arquetipo.** Lente escalation-gated/capped = dormida (DESCARTE). Skill = activación amplia + forense-nativa.
- **Una skill NOMBRA/DETECTA; el Failure Catalog del variant VINCULA severidad; la tabla determinista COMPUTA.** `VERDICT_IMPACT: NONE` = la skill no computa/override — NO que sus findings sean sin-severidad. Findings de skill portan severidad catalog-bound y PUEDEN hundir el veredicto (correcto; distinto de la familia metadata P1-P4/provenance).
- **Activación⊆binding:** una skill activa SOLO en dominios con Failure Catalog rows (no findings sin hogar de severidad).
- **No-duplicación de rows:** donde un patrón ya está cubierto (over-claim↔MK04), REUSAR la row existente.
- **No-impacto de skill markdown = garantía ESTRUCTURAL** (markdown no puede tocar `final_verdict`), no golden runtime; el test asserta registro + activación⊆binding + ausencia en orchestrator verdict modules.
- **bump_manual: inserts de roadmap LINE-BASED** (anclar por prefijo de línea único, no transcribir líneas largas) — evita fragilidad de anclas largas.
- **El live e2e destapa lo que el offline/estructural no puede** (LW-1/2/3 surgieron solo con modelo real). Ejercitar live tras shippear capas no-vinculantes.
- **Domain routing por substring es frágil** (LW-1): claves cortas (`ma`/`ops`/`hr`) producen false-matches; el ruteo correcto exige token/word-boundary. Para forzar dominio en `--document` mode, nombrar el archivo con un keyword inequívoco sin substring de clave corta.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica válida | bumpear docstrings/catálogo/comments-feature-landing congelados cada minor | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts de edición que escriben cada edit desde el snapshot original (clobber multi-edit) | añadir mejoras de activación dormida sobre alternativas de activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` por ahora | **riesgo reputacional como lente-arquetipo (dormant) — usar SKILL — s30** | **duplicar Failure-Catalog rows cuando el patrón ya está cubierto — REUSAR — s30** | **activar una skill en dominios sin Failure Catalog rows (findings sin hogar de severidad) — s30** | **transcribir líneas largas como anclas en scripts (usar inserts line-based por prefijo) — s30**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v29.md` (v28 borrado s30)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa **COMAS**. env var = `$env:VAR="..."` (NO `set`, que es cmd). `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). bump_stamps.ps1 con params NOMBRADOS (`-OldVersion X -NewVersion Y [-Apply]`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1`. Edits prosa/código/banner multi-archivo = **Ruta 3** o **script Python anclado all-or-nothing + NEWLINE-AWARE + ENCADENADO POR ARCHIVO + INSERTS LINE-BASED** (dry-run en clon pristino → --apply), a la RAÍZ. Edits pequeños/archivo nuevo = mi-filesystem directo (`create_directory` para subdirs nuevos; verificar con `list_directory`/read-back). `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Correr DS contra modelo real (no-cert):** desde `orchestrator/`, setear backend en la MISMA shell ANTES — key real `$env:ANTHROPIC_API_KEY="sk-ant-..."` (NUNCA pedirla/pegarla en el chat) o fcc `$env:ANTHROPIC_BASE_URL="http://localhost:8082"` + key placeholder (DS instancia `Anthropic(api_key=…)` SIN `base_url` → respeta el env var, routing zero-code). `--document <file>` ingiere archivo real; el **dominio se infiere del STEM del filename** (substring → ver LW-1). `--type X --subscenario Y --objective Z` pinea dominio pero el doc es un stub (sin contenido real).
- **Skill nueva = patrón:** `skills/<name>/SKILL.md` (frontmatter + patrones + Activación por dominio + binding al Failure Catalog + `[VERDICT_IMPACT: NONE]`) + `SKILLS_CATALOG` entry + bullet en base + RULES/rows en los variants activos + test estructural. Activación⊆binding. Severidad solo vía catálogo.
- **Runtime no-vinculante:** `confidence` (P3) → `_maybe_escalate` (P1) → `_run_escalation_round`+lente (P2) → señales (P4) → provenance post-veredicto (s29). **Reputational (s30) NO es de esta familia:** es skill de detección con findings de severidad real catalog-bound.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. Tests: `test_reputational_risk` 14/0 · `test_provenance` 12/0 · `test_signals` 11/0 · `test_archetype_lenses/escalation/confidence` 10/0 c/u · `test_wizard` 7/7. `pip install rank_bm25 pydantic` antes.
- **free-claude-code:** `fcc-server` puerto 8082 (NO en PATH — instalar). CERT = `sk-ant-...` real sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 30
**Repo dark-strategist-agent (v3.16.0 cert) — commit atómico:**
```
feat: DS v3.16.0 — reputational-risk forensic lens (skill #7) into P11/P16/P19 — 5 patterns, detection lens, severity bound by Failure Catalog, NON-BINDING + JARP_CERTIFIED PA-20260606-006
```
Incluye: `skills/reputational-risk/SKILL.md`, `orchestrator/{catalogs.py,test_reputational_risk.py,main.py,wizard.py,tribunal_transversal.py}`, `prompts/{system_prompt,system_prompt_media,system_prompt_marketing,system_prompt_strategy}.md` + 21 prompts (stamps), README, CLAUDE, CHANGELOG, `dark-strategist-continuity-prompt_v29.md`; `git rm dark-strategist-continuity-prompt_v28.md`. NO incluye el one-shot (borrado).
Commits posteriores s30: `42a24f2` (remove v28), `6bbfcc3` (README Full Feature Set tabla → v3.16), + este registro live-WATCH/LW-1/2/3.
**Repo jarp-toolkit:**
```
docs: sync DS v3.16.0 / PA-20260606-006 (reputational-risk skill #7) — header + entry #30 (Version/skills 7/cert/superseded) + note #16 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 30

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.16.0** | **PA-20260606-006** | **v3.16.0** | ✅ ACTIVE | 06/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 30 (auto-mejora del próximo Claude)

1. **Verificar AMBOS canónicos al cierre.** El drift s29 (toolkit un minor atrás del init) se atrapó en PHASE 0 s30 por leer ambos. Sincronizar init Y toolkit en cada cierre, no solo uno.
2. **Gate skill-vs-lens ANTES de codear, sobre código vivo.** Leí skills/catalogs/variants → confirmé que skill > lente (activación amplia vs dormida) y que la severidad la vincula el Failure Catalog. El gate se resolvió por evidencia en código, no por suposición.
3. **Una skill markdown NO tiene golden runtime de veredicto** — su no-impacto es estructural (markdown no toca `final_verdict`). No prometer golden runtime donde no aplica; el test asserta estructura + activación⊆binding + ausencia en orchestrator. Honestidad sobre la diferencia con provenance (Python).
4. **Activación⊆binding** — declarar activación de skill solo donde hay Failure Catalog rows. Fásico 3+2 respetó esto (P14/P20 NO en activación v1.0.0).
5. **No duplicar lo ya cubierto** — over-claim en Marketing reusa MK04. Leer el variant en vivo revela qué patrones ya están bound.
6. **bump_manual line-based para roadmap** — anclar por prefijo de línea único (`| v3.15.0 `), no transcribir la fila completa. Evita fragilidad de anclas largas. Banners orchestrator = REPLACE de substring único; refs feature-landing (v3.15.0 en comments/docstrings) = FROZEN, no se tocan.
7. **Dry-run en clon pristino (sandbox) + apply en máquina real** — el clon es LF, la máquina CRLF; el motor newline-aware detecta/preserva por archivo. La disjunción bump_stamps/manual se probó en vivo (re-anclaje README 216→217).
8. **One-shot borrado ANTES del commit** (mi-filesystem delete + list_directory verifica).
9. **TRADING: 27 SESIONES POSTERGADO (4–30). NO re-confrontar.**
10. **Live-WATCH CERRADO (s30 post-cert)** con key real (no fcc — fcc sigue sin instalar). Cerró `b_unified_output` + ejercitó las 6 capas live (Strategy/P19, 6 FATAL→INVIABLE). El live destapó 3 hallazgos → **LW-1** (domain resolver substring bug — prioridad), **LW-2** (confidence corroboración frágil), **LW-3** (provenance granularidad por formato). El offline/estructural NUNCA los habría mostrado — ese es el valor del e2e live.
11. **Para forzar dominio en `--document` mode:** el ruteo usa el STEM del filename por substring; nombrar el archivo con un keyword inequívoco SIN substrings de claves cortas (`ma`/`ops`/`hr`/`sop`). Ej.: `strategy_acme_board_proposal` → Strategy; `…transformation` → Financial (LW-1).
