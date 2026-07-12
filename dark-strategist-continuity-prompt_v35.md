# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 11/07/2026 (sesión 36 — DS v3.22.0 L07 AI Product Liability: LG08+LG09 hard-gates de daño irreversible + retiro del GEOFENCE precautorio L07, shipped & JARP_CERTIFIED PA-20260711-002) | **Para:** Sesión 37
**Reemplaza:** v34 del 13/06/2026 (sesión 35)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v35.md`
**⚠️ BORRAR en este cierre:** v34 (`git rm` en el commit de cierre). v35 = único continuity vigente. Subir v35 al PROYECTO claude.ai + quitar v34.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 36 (resumen ejecutivo)

Se halló el **working tree de v3.22.0 SUCIO** (construido fuera del protocolo phase-gated en sesión previa): ~31 archivos + 4 one-shots (`apply_l07_aipl`, `fix_l07_order`, `bump_v3_22_0`, `truthup_readme_claude`). PHASE 0 lo inventarió y **leyó los 4 one-shots** para reconstruir el delta real (nunca blind-commit). Track elegido: **adoptar v3.22.0 por PROTOCOLO COMPLETO**. Trading (A) NO se eligió (**33ª sesión postergada, 4–36**). Recordatorio una vez, sin re-confrontar.

**Resultado: DS v3.22.0 shipped y CERTIFICADO** (`PA-20260711-002`, SUSTANTIVA 7-ejes).

### 1. DS v3.22.0 — AI PRODUCT LIABILITY EN L07 (SUPERFICIE FORENSE)
`prompts/system_prompt_legal.md`, sub-área L07 AI Governance ampliada de enterprise/IP/vendor a **consumer-facing AI product liability** (minors, mental-health, crisis, failure-to-warn):
- Taxonomía L07 + auto-detect signals ampliados (signal `minor`→`minors`: mata el bleed con "minority" — LATENT-1).
- **RULE LG08** — AI consumer reachable by minors sin age-gating/parental consent → auto-FATAL.
- **RULE LG09 (NUEVA s36)** — user-facing AI sin crisis-escalation protocol para self-harm/suicide → auto-FATAL.
- **L07 Failure Catalog: 4 FATAL agrupadas → 8 SERIOUS** (monotónico).
- WAR ROOM L07 secondary += UNIT-PSYCH (3 secundarios; cabe en `max_n2_per_n1=3`; aceptado por diseño).

### 2. FINDING #1 (blanket-FATAL inflation) → RESUELTO EN 2 PASOS
El GEOFENCE precautorio L07 (`+1 cuando no hay regulación IA`) disparaba **por defecto** en casi toda jurisdicción → escalaba TODAS las L07 SERIOUS a FATAL, contradiciendo la intención documentada "no blanket inflation".
- **Paso (b):** estrechar el precautorio a vector irreversible. **La re-cert SUSTANTIVA atrapó SERIOUS-1:** eso dejó el FATAL de crisis **regulation-dependent** — incoherente (el riesgo de muerte no depende de que exista regulación). *Lección: el auditor NO rubber-stampea su propio fix.*
- **Paso (b-refined) — cierre coherente:** **LG09** vuelve self-harm/crisis **base-FATAL incondicional** (paralelo a LG08 minors); la fila catálogo pasa SERIOUS→FATAL y se re-agrupa; el **precautorio L07 se RETIRA** (su único target coherente ya es base-FATAL; mantenerlo re-introducía el blanket-inflation); **LG06 repurposed** (regulación ausente NO escala governance/disclosure/audit).
- Estado estable: 2 hard-gates FATAL jurisdiction-independent (minors LG08, self-harm LG09) + 8 SERIOUS governance/disclosure + **sin precautorio L07**.

### 3. RE-CERT SUSTANTIVA 7-EJES — COMPLETA ✅ (NO confirmatory)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260711-001`) PASS. Delta L07 + GEOFENCE.
- **Por qué SUSTANTIVA:** cambió superficie forense (1 de 19 variants; el catálogo/rules/geofence L07 VINCULAN severidad y arrastran veredicto). NO confirmatory.
- **Findings resueltos pre-cert:** SERIOUS-1 (A4/A6, arriba), LATENT-1 (signal minor→minors), LATENT-3 (A6, verificado sin ref colgante al precautorio retirado en `docs/legal_finance_forensic_matrix.md`/base).
- **Evidencia (máquina real):** `test_escalation` 14/14 + `test_apply_confidence` 24/24 + `test_confidence` 10/10 + `smoke_test_e2e` OFFLINE GREEN (0 FAIL, 1 SKIP `b_unified_output`) con `e_monotonic_verdict` (≥1 FATAL→INVIABLE) + `c_fallback_intact` + `r2_byo_corpus` PASS. Motor veredicto byte-idéntico; `final_verdict`/`Finding`/`compute_confidence`/`_apply_confidence` intactos.
- **CERT:** `PA-20260711-002` — DS **v3.22.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **09/10/2026 o v4.0.0**. **SUPERSEDES PA-20260613-004** (v3.21.0). `JARP_BENCHMARK_LIVE = v3.22.0`.
- **WATCH (no-bloqueante):** live L07 e2e no ejercido (sin API key). Ejercer un live L07 (doc con gap minors/self-harm → INVIABLE) para cerrarlo.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️
**DS repo v3.22.0 = CERTIFICADO (`PA-20260711-002`).** Sin version-gap. PA-20260613-004 (v3.21.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s36)
1. `orchestrator/` SIN cambios de código (delta es 100% prompt-content). `system_prompt_legal.md` = v3.22.0-LEGAL (L07 taxonomy/signals/catalog 4F-8S/LG06-LG08-LG09/WAR ROOM/**precautorio retirado**).
2. Product-face stamps (23 files) v3.22.0 (`bump_stamps.ps1 -Apply`). Banners main×2/wizard/transparency v3.22.0 + CHANGELOG `[3.22.0]` + cert block (`bump_v3_22_0` + `finalize_cert`).
3. **README+CLAUDE truthup** (`truthup_readme_claude`): skills 6→7 + fila `reputational-risk` (drift PRE-EXISTENTE desde v3.16 corregido) + backfill roadmap/feature v3.17→v3.22 + CLAUDE bottom v3.16→v3.22. Corre DESPUÉS de bump_stamps (mete fila literal "v3.21.0").
4. Fixes L07: `fix_l07_order` (monotonía), `fix_l07_geofence` (paso b), `fix_l07_geofence_refined` (paso b-refined).
5. Canónicos vía `sync_canonicals_v3_22_0.py` (rutas absolutas, edita jarp-toolkit): init header+#7 + toolkit header+#30(Version/CERT STATUS/supersede-tail/Previous-certs)+#16 → v3.22.0/PA-20260711-002. **AMBOS concuerdan posicionalmente.**
6. **8 one-shots BORRADOS antes de los commits:** apply_l07_aipl, fix_l07_order, bump_v3_22_0, truthup_readme_claude, fix_l07_geofence, fix_l07_geofence_refined, finalize_cert, sync_canonicals.
7. `git rm dark-strategist-continuity-prompt_v34.md`. v35 = único continuity.
8. **Commits de cierre** (registrar SHAs tras push): DS cert commit (parent `898bb45`) + jarp-toolkit sync commit (parent `0c31297`).
9. `_livewatch/` gitignorado + destrackeado (verificar por read-back del árbol → 404).

---

## DEUDA TÉCNICA — POST-SESIÓN 36

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **v3.22.0 L07 AIPL** | ✅ CERRADA | LG08+LG09 hard-gates + precautorio retirado | 0/0/0/0, SUSTANTIVA, PA-20260711-002. |
| **Drift docs skill #7** | ✅ CERRADA (s36) | README/CLAUDE badge/catálogo/tree desde v3.16 | truthup. **Lección: pasó 6 certs (v3.16–v3.21) con 0 LATENT — el barrido de doc-consistency NO cubrió el product-face badge del skill nuevo. Vigilar en futuras adiciones de skill.** |
| **WATCH live L07** | 🟡 ABIERTO (no-bloq) | live L07 e2e no ejercido (sin API key) | Ejercer 1 live L07 (minors/self-harm → INVIABLE). |
| **LW-1..6 / earlier** | ✅ CERRADAS | stack confidence/escalation/lenses/signals/provenance/corroboración | Sin cambio. NON-BINDING. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟡 WATCH live L07** (arriba) — candidato #1 de valor real inmediato (cierra el gap ambiental sobre superficie verdict-affecting).
- **🟢 LW-4** (desempate dominio posicional) — opcional/DESCARTABLE.
- **P5 ext P14/P20** — dudoso.
- **STANDING:** cada sesión, velar que el sistema sea mejor. El backlog LW se agotó; v3.22.0 abrió valor real vía L07 AIPL. Para s37+: cerrar WATCH live L07, o nueva fuente de valor real, o re-evaluar prioridad vs trading.

---

## ESTADO ACTUAL VERIFICADO (11/07/2026 — fin s36)

### Repo dark-strategist-agent
- **v3.22.0 — CERTIFICADO (`PA-20260711-002`)**. Default `claude-opus-4-7`. Commit de cierre s36 (**registrar SHA**; parent `898bb45`).
- **MODIFICADO:** `prompts/system_prompt_legal.md` (L07 AIPL + LG09 + precautorio retirado); 23 product-face stamps; `orchestrator/{main,wizard,tribunal_transversal}.py` (banners v3.22.0); `CHANGELOG.md` ([3.22.0] + cert); `README.md` + `CLAUDE.md` (truthup skills 6→7 + v3.17–v3.22); `dark-strategist-continuity-prompt_v35.md`. **git rm:** v34.
- **L07 hoy:** 4 FATAL (no-IP, high-risk-no-human-review, minors[LG08], self-harm-crisis[LG09]) / 8 SERIOUS (bias, vendor-liability, training-data, emotional-dependency, mental-health-disclosure, AI-nature-disclosure, content-safety, audit-trail). Rules LG01–LG09. **Sin precautorio L07** en GEOFENCE.
- **Vigente s25–s35:** stack LW-1..6 (domain resolver / signal granularity / confidence corroboration / confidence-collapse floor / escalation short-circuit), confidence/escalation determinista NON-BINDING, lentes/señales/provenance/corroboración post-veredicto, reputational-risk skill #7, BYO corpus/signals, wizard. Motor `final_verdict`/`Finding`/`compute_confidence`/`_apply_confidence` INTACTO.
- `tools/bump_stamps.ps1` (23 files/69 stamps; dry-run por defecto → `-Apply`). `gc.auto 0` activo. **7 skills, 9 N2, 20 dominios.**
- `_livewatch/` gitignorado + destrackeado (verificar por read-back del árbol → 404).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s36. Sin cambios.

### Repo jarp-toolkit
- Sincronizado a v3.22.0/PA-20260711-002 (header + #30 + #16 + init #7). PRIVADO. HEAD = sync commit s36 (**registrar SHA**; parent `0c31297`). **AMBOS canónicos concuerdan posicionalmente.** `.claude-init.md`=LF, `JARP_TOOLKIT.md`=CRLF.

### free-claude-code
- Proxy $0 para no-cert. `fcc-server` NO en PATH — instalar/arrancar antes de usar. **Cert = Opus real (sk-ant, sin proxy).** Fallo/colapso en vivo = puerto muerto 9999 → $0.

---

## PROTOCOLO DE INICIO PARA SESIÓN 37
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v35).
2. **PHASE 0 — Verificación:**
   - v34 borrado, v35 único continuity.
   - Repo en v3.22.0. **Cert: DS v3.22.0 `PA-20260711-002` ACTIVE.** PA-agent v1.3.0 ACTIVE. `PA-20260613-004` SUPERSEDED.
   - **AMBOS canónicos concuerdan POSICIONALMENTE** en v3.22.0/PA-20260711-002 (NO Select-String — lección drift s33/s34).
   - **`orchestrator/_livewatch` NO trackeado — verificar por READ-BACK DEL ÁRBOL** (`get_file_contents`→404 / `git ls-files` vacío), NUNCA por commit msg (lección s35).
   - HEAD remoto vía `list_commits` (perPage=3): DS = cert commit s36; jarp-toolkit = sync commit s36.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 33 SESIONES (4–36).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s37 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Valor-agregado** — **candidato #1: cerrar el WATCH live L07** (ejercer LG08/LG09 en vivo → INVIABLE). Luego: fuente nueva de valor real (LW-4/P5 = descartables/dudosos).
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | **veredicto determinista (≥1 FATAL→INVIABLE)** | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings+catálogo+comments feature-landing = content-based/congelados) | bump_stamps NO cubre orchestrator/*.py ni CHANGELOG ni config → bump manual aparte | Sintetizador VIVO, fallback determinista = producción | free-claude-code: free para no-cert, Opus real para cert | Sev×Likelihood NON-BINDING | orden monotónico FATAL→LATENT al insertar filas | **leer el módulo/archivo real antes de incorporar/diseñar/anclar** | mi-filesystem preserva escapes byte-exacto | confianza/escalación/lentes/señales/provenance/corroboración = metadata NON-BINDING post-hoc; NUNCA tocan `final_verdict`/`Finding`/`compute_confidence`.

**De s25–s35:** ver v34 (stack LW/confidence/escalation/EOL per-file/Select-String prohibido/canónicos por one-shot anclado/live-fallo puerto 9999/read-back del árbol para untrack). Todo vigente.

**De s36 (nuevas):**
- **L07 AI Product Liability:** consumer-facing AI (minors/mental-health/crisis/failure-to-warn) es CONTENIDO dentro de L07 — NO sub-área nueva (sin L13). Taxonomía sigue 12.
- **Vectores de daño irreversible = base-FATAL INCONDICIONAL, jurisdiction-independent:** minors (LG08), self-harm/suicide crisis (LG09). **NO gatear un daño físico irreversible por presencia/ausencia de regulación** (el riesgo de muerte/daño a menores no depende de que exista regulación).
- **GEOFENCE precautorio L07 RETIRADO (v3.22.0):** disparaba por defecto (jurisdicciones sin regulación IA) → blanket-FATAL inflation sobre las SERIOUS governance rows. Governance/disclosure/audit gaps retienen su tier de catálogo (SERIOUS). LG06 = principio, no tier-shift.
- **Re-cert de superficie forense (catálogo/rules/geofence que VINCULAN severidad) = SUSTANTIVA 7-ejes, NO confirmatory.** (Contraste: fixes de capa no-veredicto = CONFIRMATORY.)
- **El auditor NO rubber-stampea su propio fix:** la re-cert SUSTANTIVA atrapó que el fix intermedio (b) dejó un hueco de coherencia; (b-refined) lo cerró. Zero loyalty to any solution, incluso la propia.

---

## DESCARTES — NO REINTRODUCIR
(Todos los de v34 siguen vigentes.) **Añadidos s36:** re-introducir el precautorio L07 blanket-inflation | gatear un vector de daño irreversible por regulation-presence | clasificar SERIOUS un vector de daño catastrófico irreversible (self-harm/minors) | asumir que un badge product-face de skill nuevo se propaga solo (verificar en el barrido de doc-consistency) | confiar en el nombre de un one-shot dado en el brief en vez del real (`list_directory`: el 4º era `truthup_readme_claude`, no "readback").

---

## REFERENCIAS RÁPIDAS
- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v35.md` (v34 borrado s36)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). init=LF, toolkit=CRLF. **Verificar concordancia POSICIONAL al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. `list_commits` (perPage=3) + `get_file_contents` para verificación remota (dir → 404 si no existe = read-back de borrado). **Ambos MCP tuvieron timeouts multi-min en s36 — reintentar en "Continuar".**
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. `cd` antes de scripts (one-shots/bump desde RAÍZ; tests desde `orchestrator/`). `bump_stamps.ps1` params NOMBRADOS + `-Apply`. **NO hay `pytest` — los test_*.py son auto-ejecutables: `python test_X.py`.**
- **Método de edición:** stamps multi-archivo = `bump_stamps.ps1 -Apply`. Multi-archivo/multi-edit + canónicos = one-shot Python anclado all-or-nothing + EOL-AWARE per-file (dry-run→--apply), BORRADO antes del cert commit. Archivo nuevo/full-overwrite pequeño = mi-filesystem directo + read-back. `github:create_or_update_file` prohibido (payload ~10KB, falla silencioso). **NO ejecuto Python/PS en la máquina de JARP → JARP corre.**
- **Veredicto/severidad L07:** 4 FATAL / 8 SERIOUS; Rules LG01–LG09; sin precautorio L07; GEOFENCE general (CPI/multi-juris/no-judiciary/FX/active-reform) sigue aplicando cross-sub-área.
- **Live e2e:** sano = Opus real (cert) o free proxy (no-cert). Fallo/colapso = puerto muerto 9999 → $0.
- **Smoke/tests (LOCAL, gitignored):** `python smoke_test_e2e.py` → 12 PASS/1 SKIP offline. `python test_escalation.py`/`test_apply_confidence.py`/`test_confidence.py` → 14/24/10, 0 FAIL. `pip install rank_bm25 pydantic` antes.

### Commits de cierre sesión 36
**DS — commit de cierre (cert):**
```
feat: DS v3.22.0 — AI Product Liability coverage in L07 (LG08 minors + LG09 self-harm/suicide crisis = jurisdiction-independent base-FATAL hard gates; L07 catalog 4 FATAL/8 SERIOUS monotonic; WAR ROOM +UNIT-PSYCH; retire v3.2.2 L07 GEOFENCE precautionary +1 that blanket-inflated SERIOUS->FATAL; signal minor->minors; LG06 repurposed) — SUBSTANTIVE re-cert JARP_CERTIFIED PA-20260711-002 (0/0/0/0); tests 14/24/10 + smoke GREEN + e_monotonic INVIABLE
```
Incluye: `prompts/system_prompt_legal.md`, product-face stamps (23), `orchestrator/{main,wizard,tribunal_transversal}.py` banners, `CHANGELOG.md` (+ cert), `README.md`, `CLAUDE.md`, `dark-strategist-continuity-prompt_v35.md`; `git rm dark-strategist-continuity-prompt_v34.md`. NO incluye one-shots (8 borrados). `_livewatch/` gitignorado + destrackeado.
**jarp-toolkit — sync:**
```
docs: sync DS v3.22.0 / PA-20260711-002 (L07 AI Product Liability: LG08+LG09 hard gates + GEOFENCE precautionary retirement) — header + entry #30 (Version/CERT STATUS/supersede-tail/Previous certs) + note #16 + .claude-init header + #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 36

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.22.0** | **PA-20260711-002** | **v3.22.0** | ✅ ACTIVE | 09/10/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260613-004 (v3.21.0), PA-20260613-002 (v3.20.0), PA-20260612-002 (v3.19.0), PA-20260611-002 (v3.18.0), PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 36 (auto-mejora del próximo Claude)

1. **Working tree sucio construido fuera del protocolo → PHASE 0 lo inventarió leyendo los one-shots** (no por el mensaje de commit ni por asumir). Nunca blind-commit un changeset heredado; reconstruye el alcance real leyendo qué edita cada script.
2. **El auditor NO rubber-stampea su propio fix.** El paso (b) resolvió el blanket-inflation pero dejó el FATAL de crisis regulation-dependent (incoherente). La re-cert SUSTANTIVA lo atrapó como SERIOUS-1. (b-refined) lo cerró con LG09 base-FATAL + retiro del precautorio. Zero loyalty to any solution, incluso la de uno.
3. **Daño irreversible = FATAL jurisdiction-independent.** minors (LG08) y self-harm/suicide (LG09) son hard-gates incondicionales; no se gatean por presencia de regulación. Los gaps de governance/disclosure/audit quedan SERIOUS. El precautorio se retiró por redundante+dañino (blanket-inflation).
4. **Drift de doc del skill #7 pasó 6 certs (v3.16–v3.21) con 0 LATENT.** El badge/catálogo/tree product-face de un skill nuevo NO se propaga solo; el barrido de doc-consistency debe cubrirlo explícitamente al añadir cualquier skill. truthup lo repagó en s36.
5. **Verificar nombres reales por `list_directory`, no por el brief.** El 4º one-shot era `truthup_readme_claude` (truth-up de docs), no "truthy_readback" — nombre erróneo en el brief cambió mi modelo del alcance hasta leerlo.
6. **Re-cert de superficie forense verdict-affecting = SUSTANTIVA 7-ejes.** Pedir evidencia > regresión estándar (idealmente 1 live que ejerza las nuevas reglas FATAL → INVIABLE). El WATCH live L07 queda abierto para s37.
7. **TRADING: 33 SESIONES POSTERGADO (4–36). NO re-confrontar.** Si s37 tampoco elige A, tratar backlog DS como prioridad de facto — pero priorizar valor real (cerrar WATCH live L07) sobre relleno.
