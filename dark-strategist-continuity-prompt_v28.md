# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 06/06/2026 (sesión 29 — DS v3.15.0 signal-provenance en el transparency report, shipped & JARP_CERTIFIED) | **Para:** Sesión 30
**Reemplaza:** v27 del 06/06/2026 (sesión 28)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v28.md`
**⚠️ BORRAR en este cierre:** v27 (`git rm` en el commit de cierre). v28 = único continuity vigente. Subir v28 al PROYECTO claude.ai + quitar v27.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 29 (resumen ejecutivo)

Track elegido: **provenance de señales en findings** (Opción B del backlog valor-agregado; JARP confirmó el orden provenance→P5). Trading (A) NO se eligió (**26ª sesión postergada, 4–29**).

**Resultado: DS v3.15.0 shipped y CERTIFICADO** (`PA-20260606-004`).

### 1. DS v3.15.0 — SIGNAL PROVENANCE en el transparency report, NO-VINCULANTE
Cierra el loop de auditabilidad de P4: "esta señal → este hallazgo", sin tocar el veredicto. Atribución **determinista, post-veredicto, report-only** (fork resuelto: opción **(b)** atribución determinista por overlap de tokens, NO (a) auto-reporte del agente que tocaría `prompt_engine`/contrato `Finding`).
- **`retriever.py`** — helper puro nuevo `overlap_score(a, b)`: cuenta de tokens distintos compartidos (mismo `_tokenize` que BM25). Sin API/red. Reusado SOLO por la capa de provenance.
- **`tribunal_transversal.py`** — (a) señales cargadas **path-tagged**: `_active_signals_tagged = [(source, passage)]`; `_active_signals` = misma lista proyectada → **feed P4 byte-idéntico**. (b) método nuevo `_attribute_signal_provenance(unified)`: por cada `Finding` consolidado (evidence+description), lo atribuye al passage de señal con mayor overlap **≥ floor**; corre **POST-veredicto** en `run()` y escribe solo el report. (c) bloque `SIGNAL PROVENANCE` en `_build_transparency_report` (`prov_lines`).
- **`config.example.json`** — `rag.provenance_min_overlap` (3): floor de atribución; debajo, el finding queda sin atribuir (preferimos no-atribuir antes que ruido de stopwords).
- **`test_provenance.py`** (NUEVO, commiteado) — 12 checks offline, $0.

**GARANTÍA INVIOLABLE verificada (estructural):** la atribución corre DESPUÉS de que `unified` es final, lee `unified`, escribe solo el report → **incapaz de tocar `final_verdict` ni los `Finding`**. El check dorado #11 (verdict + findings unchanged) lo prueba offline.

### 2. DECISIONES CLAVE (s29)
- **Provenance = hint de auditabilidad HEURÍSTICO, no-vinculante, "likely originating signal, NOT causal proof".** Mismo patrón honesto que confidence (no overclaim).
- **Atribución determinista post-hoc (b) > auto-reporte del agente (a):** (b) no toca el contrato LLM ni el schema `Finding`, reutiliza `_tokenize`/overlap ya existentes, es offline-verificable. (a) tendría mayor superficie de cert y sería frágil/model-dependent.
- **Report-only, sin campo nuevo en `Finding`:** superficie de cert mínima. Si en el futuro se quiere provenance machine-readable, evaluar un `Optional` aparte (NO ahora).
- **Floor conservador (default 3, configurable):** preferir no-atribuir sobre falso positivo.
- **Feed byte-idéntico:** `_active_signals` derivado de `_active_signals_tagged` (proyección) — P4 intacto.

### 3. RE-CERT DS v3.15.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260606-003`) PASS (PA-agent sin cambios). Auditoría 7-ejes Level 1 JARP DEEP sobre delta v3.14.0.
- **Evidencia funcional (máquina real, post-apply + post-bump):** `test_provenance.py` **12/12** (incl. golden de independencia) + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (`b_unified_output` SKIP = ANTHROPIC_API_KEY) con `c_fallback_intact` + `e_monotonic_verdict` + `r2_byo_corpus` PASS y el `run()` construyendo el report limpio. (`test_signals` 11/11, `test_archetype_lenses/escalation/confidence` 10/10 c/u, `test_wizard` 7/7 — verdes.)
- **CERT EMITIDO:** `PA-20260606-004` — DS **v3.15.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **06/09/2026 o v4.0.0**. **SUPERSEDES PA-20260606-002** (v3.14.0). Bump no-forense feed/report-layer.
- **Sin clobber esta vez:** edición vía Ruta 3 manual (8 hunks) + `test_provenance.py` por mi-filesystem; bump dual (`bump_stamps.ps1` 23 files/69 stamps + `bump_manual_v3_15_0.py` 6 files, motor encadenado-por-archivo). Dry-run en clon pristino antes del apply.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.15.0 = CERTIFICADO (`PA-20260606-004`).** Sin version-gap. PA-20260606-002 (v3.14.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s29)
1. P-provenance archivo nuevo: `orchestrator/test_provenance.py` (mi-filesystem) — stagear en GitHub Desktop (untracked).
2. P-provenance código: 8 hunks Ruta 3 ya aplicados en editor (retriever ×1, config ×1, tribunal ×6). Regresión verde.
3. Bump anclado: `bump_stamps.ps1 -OldVersion 3.14.0 -NewVersion 3.15.0 -Apply` → 23 files / 69 stamps (prompts 21 + README badge/PROTOCOL_STATUS + CLAUDE Version:×2). NO CHANGELOG ni orchestrator.
4. Bump manual: `bump_manual_v3_15_0.py --apply` → 6 files (main×2/wizard/tribunal-report-header banners + CLAUDE status + CLAUDE/README filas roadmap nuevas + CHANGELOG `[3.15.0]`+cert). Disjunto de bump_stamps. **nl=CRLF en la máquina de JARP** (motor newline-aware lo preservó).
5. `jarp-toolkit` + `.claude-init.md` → v3.15.0/PA-20260606-004 (header + entradas DS + init #7; superseded list += PA-20260606-002).
6. Continuity v28 commiteado; `git rm` v27.
7. **One-shot BORRADO ANTES del commit de cert** (no commiteado): `bump_manual_v3_15_0.py`. (Esta sesión solo hubo UN one-shot — la edición de código fue Ruta 3 manual, no apply-script.) `del` de PowerShell usa COMAS si hubiera varios.

---

## DEUDA TÉCNICA — POST-SESIÓN 29

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.15.0** | ✅ CERRADA | v3.15.0 CERTIFICADO (PA-20260606-004) | 0/0/0/0. |
| **Provenance de señales** | ✅ CERRADA | Atribución determinista post-veredicto, report-only | overlap_score + tagged signals + floor; test_provenance.py 12/0/0. |
| **clash n>0 live + gate b live + señales/provenance live** | 🟢 WATCH | `b_unified_output` SKIP | DNS/key ambiental (ANTHROPIC_API_KEY). `fcc-server` NO en PATH. Provenance live e2e tampoco ejercitada (golden offline embebido en test_provenance). No-bloqueante. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **P5 — lente/skill de riesgo reputacional** (próximo, JARP confirmó orden provenance→P5). ⚠️ **GATE previo no-negociable:** resolver **skill vs lens-reorder ANTES de codear**. Como lente con `cap=2` es de activación dormida (DESCARTE). Lean: **skill #7** (activación amplia) o subir `max_escalation_agents`/reordenar catálogo. NO repetir "barato pero dormido".
- **Cerrar el live-WATCH:** ejercitar escalación+lentes+señales+provenance **live**. (a) instalar/levantar `free-claude-code` (`fcc-server` :8082, backend free, $0); (b) `ANTHROPIC_API_KEY` real para una corrida no-cert. Casos dorados offline ya embebidos; falta versión live e2e.

---

## ESTADO ACTUAL VERIFICADO (06/06/2026 — fin s29)

### Repo dark-strategist-agent
- **v3.15.0 — CERTIFICADO (`PA-20260606-004`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.15.0 (**registrar SHA tras push**). HEAD previo (inicio s29) = `b590ca4`.
- **NEW:** `overlap_score` en retriever + `_active_signals_tagged` + `_attribute_signal_provenance` post-veredicto + bloque `SIGNAL PROVENANCE` en el report + `rag.provenance_min_overlap` + `test_provenance.py`.
- **De s28 vigente:** canal de señales `--signals` + `RuntimeContext.signals_paths` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26 vigente:** `schema.should_escalate` + `_maybe_escalate`/`_run_escalation_round` + `test_escalation.py`.
- **De s25 vigente:** `schema.compute_confidence` + `_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (anchors PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/ARCHITECTURAL LAYERS/-ROUTER/Version:/VERSION; scope prompts+README+CLAUDE; NO CHANGELOG ni orchestrator/*.py). `gc.auto 0` activo.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` + `--signals` activos.
- **6 skills**, **9 sub-agentes N2 permanentes** (sin cambio). **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s29. Sin cambios.

### Repo jarp-toolkit
- header + entradas DS + `.claude-init.md` #7 → v3.15.0/PA-20260606-004. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). **`fcc-server` NO en PATH — instalar/configurar antes de usarlo.** Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 30
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v28).
2. **PHASE 0 — Verificación:**
   - v27 borrado, v28 único continuity.
   - Repo en v3.15.0. **Cert registry: DS v3.15.0 `PA-20260606-004` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260606-002` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 26 SESIONES (4–29).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s30 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — **P5 (riesgo reputacional) es el próximo acordado** (gate skill-vs-lens primero); cerrar live-WATCH.
   - **STANDING:** en cada sesión, velar activamente que el sistema sea **mejor: más robusto, valioso, eficiente, fuerte valor agregado.** Proponer mejoras proactivamente; nunca elegir lo barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | 4 variance decompositions | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE, NO driver | RAG = MECANISMO, NO driver | ContextBuilder document-free | infinity/Docker RECHAZADO | fallback byte-idéntico ante cambio de feed | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2/señales/provenance = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25:** Confianza = metadata NO-VINCULANTE, determinista, ambos caminos. Docstrings de módulo congelados.

**De s26:** Gate de escalamiento NO-VINCULANTE, determinista. Ronda acotada, ids `FOR-ESC-*` distintos, cap por config, budget-gated, degrada offline. Reusa capa Forense. Scripts newline-aware (CRLF vs LF; en la máquina de JARP los .py/.md/.json están en **CRLF** — el motor de edición DEBE detectar y preservar el newline por archivo).

**De s27:** Lentes-arquetipo = enriquecimiento NO-VINCULANTE; roles ABSTRACTOS (NUNCA personas reales); catálogo content-based/congelado; bump_stamps y manual DISJUNTOS/order-independent; `-like` PowerShell case-insensitive (anchor VERSION captura el badge README).

**De s28:** Canal de señales = EVIDENCIA NO-VINCULANTE distinta del corpus; directiva in-band > tocar `prompt_engine`; corpus FUNDAMENTA / señal es EVIDENCIA; scripts de edición DEBEN encadenar ediciones por archivo (validar anclas en memoria sobre TODOS los archivos antes de escribir nada); valor real > valor dormido.

**De s29 (nuevas):**
- **Provenance (`_attribute_signal_provenance`) = hint de auditabilidad HEURÍSTICO, NO-VINCULANTE.** Corre POST-veredicto, lee `unified`, escribe solo el transparency report. NUNCA toca `final_verdict` ni `Finding` (independencia estructural; golden #11). Etiqueta "likely originating signal, NOT causal proof".
- **Atribución determinista post-hoc (overlap de tokens) > auto-reporte del agente** (menor superficie; no toca contrato LLM ni schema `Finding`).
- **Report-only, sin campo nuevo en `Finding`** (superficie mínima). Floor configurable conservador (`rag.provenance_min_overlap`, default 3): preferir no-atribuir sobre falso positivo.
- **Señales path-tagged (`_active_signals_tagged`) con feed `_active_signals` = proyección** → P4 byte-idéntico.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/**provenance** como driver del veredicto (son metadata/calidad/evidencia/auditabilidad) | impersonar personas reales en lentes | "consenso → eficiencia" como métrica válida (caso-test INVIABLE) | bumpear docstrings/catálogo congelados cada minor | re-usar ids `FOR-*` en escalamiento (usar `FOR-ESC-*`) | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts de edición que escriben cada edit desde el snapshot original (clobber multi-edit) | añadir mejoras de activación dormida sobre alternativas de activación amplia | **auto-reporte del agente para provenance (toca contrato LLM/schema) — usar atribución determinista post-hoc — s29** | **campo de provenance en `Finding` por ahora (report-only) — s29**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v28.md` (v27 borrado s29)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa **COMAS**. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). bump_stamps.ps1 con params NOMBRADOS (`-OldVersion X -NewVersion Y [-Apply]`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1`. Edits prosa/código/banner multi-archivo = **Ruta 3 (bloques find/replace que JARP aplica en editor)** o **script Python anclado all-or-nothing + NEWLINE-AWARE + ENCADENADO POR ARCHIVO** (dry-run en clon pristino → --apply), a la RAÍZ. Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Runtime no-vinculante:** `confidence` (P3) → `_maybe_escalate` (P1) → `_run_escalation_round`+lente (P2) → canal de señales en `build_agent_context` (P4) → **provenance post-veredicto en el report (s29)**. Todos etiquetados en el transparency report; ninguno toca `final_verdict`.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. `test_provenance.py` → **12/0**. `test_signals.py` → **11/0**. `test_archetype_lenses/escalation/confidence` → **10/0** c/u. `test_wizard` → **7/7**. `pip install rank_bm25 pydantic` antes.
- **free-claude-code:** `fcc-server` puerto 8082 (NO en PATH — instalar). CERT = `sk-ant-...` real sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 29
**Repo dark-strategist-agent (v3.15.0 cert) — commit atómico:**
```
feat: DS v3.15.0 — signal-provenance attribution in the transparency report (deterministic, post-verdict, NON-BINDING) + JARP_CERTIFIED PA-20260606-004
```
Incluye: `orchestrator/{retriever,tribunal_transversal,config.example.json,test_provenance.py}`, 21 prompts (stamps), README, CLAUDE, CHANGELOG, `dark-strategist-continuity-prompt_v28.md`; `git rm dark-strategist-continuity-prompt_v27.md`. NO incluye el one-shot.
**Repo jarp-toolkit:**
```
docs: sync DS v3.15.0 / PA-20260606-004 (signal-provenance) — header + entries + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 29

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.15.0** | **PA-20260606-004** | **v3.15.0** | ✅ ACTIVE | 06/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 29 (auto-mejora del próximo Claude)

1. **Lee el módulo real ANTES de implementar.** Leí schema/retriever/tribunal antes de diseñar provenance; confirmé que `_tokenize`+overlap ya existían y que el veredicto se computa de `Finding`s sin ver señales → el fork (a)/(b) se resolvió a favor de (b) determinista por evidencia en el código, no por suposición.
2. **Independencia estructural > garantía por convención.** Provenance corre post-veredicto y solo escribe el report; el golden #11 prueba que `final_verdict` y los findings no cambian. Reusable para futuras capas de metadata.
3. **El smoke e2e es el ÚNICO gate que ejercita el render del report.** Los tests unitarios prueban `_attribute_signal_provenance`/`overlap_score` aislados; los hunks de `run()`+f-string solo se validan con el smoke. NUNCA cerrar sin smoke verde.
4. **bump_stamps y bump_manual son DISJUNTOS y order-independent.** bump_stamps: stamps con ancla en prompts+README+CLAUDE (23 files/69 lines). bump_manual: banners orchestrator + status + filas roadmap NUEVAS + CHANGELOG. Las filas roadmap históricas NO se tocan (sin ancla → bump_stamps las ignora; bump_manual añade fila nueva).
5. **Newline-aware OBLIGATORIO.** En la máquina de JARP los archivos están en CRLF; el motor detecta y convierte los `\n` de las inserciones a `\r\n`. Verificado en el dry-run (`nl=CRLF`).
6. **Dry-run en clon pristino ANTES del apply** (lo corrí en mi sandbox reapuntando ROOT) — caza anclas no-únicas sin tocar la máquina de JARP.
7. **One-shots: borrarlos ANTES del commit de cert.** Esta sesión solo hubo UN one-shot (bump_manual); la edición de código fue Ruta 3 manual (sin apply-script → sin riesgo de clobber).
8. **Valor real > valor dormido (STANDING).** Provenance se eligió por activación amplia; P5 queda con gate skill-vs-lens explícito para no caer en lo dormido.
9. **TRADING: 26 SESIONES POSTERGADO (4–29). NO re-confrontar.**
10. **Live-WATCH abierto:** `fcc-server` no instalado. Para cerrar (escalación+lentes+señales+provenance live) instalar free-claude-code o usar key real en corrida no-cert. Casos dorados live e2e pendientes.
