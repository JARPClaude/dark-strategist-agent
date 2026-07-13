# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 12/07/2026 (sesión 37 — DS v3.23.0 LW-7 fail-closed verdict on tribunal collapse, shipped & JARP_CERTIFIED PA-20260712-002) | **Para:** Sesión 38
**Reemplaza:** v35 del 11/07/2026 (sesión 36)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v36.md`
**⚠️ BORRAR en este cierre:** v35 (`git rm` en el commit de cierre). v36 = único continuity vigente. Subir v36 al PROYECTO claude.ai + quitar v35.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 37 (resumen ejecutivo)

Track elegido: **(B) valor-agregado**. Trading (A) NO elegido — **34ª sesión postergada (4–37)**. Nota una vez, sin re-confrontar. Toda corrida de la sesión fue NVIDIA/proxy o forced-collapse $0 (JARP fijó "todo NVIDIA"); el cert NO requirió Opus pago (ver §cert abajo).

Se arrancó por el candidato #1 (cerrar el WATCH live L07: ejercer LG08/LG09 → INVIABLE). **La investigación destapó DOS hallazgos, uno mucho mayor que el WATCH:**

### 1. HALLAZGO #1 (MAYOR, ABIERTO) — cert-surface ↔ runtime gap
Al preparar el fixture L07 se trazó el grafo de imports COMPLETO del runtime (`main.py` → `context_builder.py` → `tribunal_transversal.py` → `prompt_engine.py` → `sub_agent_spawner.py`). **Ningún componente del runtime carga `prompts/system_prompt_legal.md` ni ninguno de los 19 variant prompts.**
- `PromptEngine` arma TODOS los prompts N1 (Rol+Forense+AFO) desde un MASTER_TEMPLATE dinámico: inyecta solo `domain` label + `subscenario` + tool-name list + reglas conductuales genéricas + tabla de severidad. **NO inyecta el catálogo L07, LG08, LG09, GEOFENCE, taxonomía L01–L12, ni las signal-tables.**
- `SubAgentSpawner` guarda `self.prompts_dir` pero **jamás lo lee**; los 9 N2 permanentes usan `system_prompt` hardcodeados de ~5 líneas genéricas.
- `router.py::DomainRouter` (v2.7.0) SÍ tiene `load_domain_prompt` que lee los variants — pero **está huérfano**: no lo importa `main`, `TribunalTransversal`, ni `ContextBuilder`. Reliquia que v3.0.0 desconectó al meter el PromptEngine dinámico ("Replaces 15 static .md files"). `LEGAL_SUBAREA_MAP/ROLES` en catalogs.py también huérfanos (ContextBuilder no los usa).
- **Implicación:** desde v3.0.0, **ningún Failure Catalog de dominio (los 19 variants) se inyecta al runtime.** LG08/LG09 NO se aplican deterministamente — que un doc con gap minors/self-harm devuelva INVIABLE depende de que Opus lo tase FATAL por criterio genérico propio (no garantizado). `PA-20260711-002` certificó `system_prompt_legal.md` como "superficie SUSTANTIVA que vincula severidad" pero esa superficie es **inerte en runtime**. El motor de veredicto (≥1 FATAL→INVIABLE) es sólido y real; lo que NO está cableado es el **mapeo severidad** (que vive solo en el .md inerte).
- **Confirmado empíricamente:** corridas L07 en vivo colapsaron por proxy caído (nunca se llegó a un run sano que lo probara conductualmente), pero el trazado de código es definitivo (`search_code` de GitHub no indexa el repo → no me apoyé en él; solo lectura real de archivos).
- **DECISIÓN ARQUITECTÓNICA PENDIENTE (JARP delega, "confío en tu criterio" esperado):**
  - **(a) FIX injection** — recablear la carga del variant al pipeline (TribunalTransversal/PromptEngine anteponen `system_prompt_<domain>.md` al system de los N1). Restaura el determinismo intencional de LG08/LG09 y de los 19 catálogos. Máximo valor real; toca run-path → re-cert SUSTANTIVA.
  - **(b) ACCEPT + re-scope cert** — declarar los variants como spec/rúbrica, no prompts de runtime; degradar todo cambio variant-only de "SUSTANTIVA verdict-binding" a "doc/spec update". Cero código; cambia la semántica del cert-chain.
  - Recomendación de la sesión: (a) es el fix de fondo alineado al STANDING; pero es LLAMADA DE JARP. **Retomar en s38 como candidato #1 de valor real.**

### 2. HALLAZGO #2 (RESUELTO → v3.23.0) — fail-open verdict on tribunal collapse (LW-7)
El fallo de infra en las corridas L07 destapó que un **colapso total del tribunal** (todos los agentes erroran → `agents_consulted==0`, 0 findings) caía al `else` de la tabla y devolvía **`SOLID UNDER PRESSURE`** (el all-clear) sobre CERO análisis. Fail-OPEN en el verdict-path — dirección de fallo equivocada para un forense. LW-5/LW-6 ya habían hecho honesta la CONFIDENCE (LOW) y la razón de escalation ("tribunal collapse") en colapso, pero el `final_verdict` seguía fail-open.
- **Fix LW-7:** `_apply_collapse_guard(unified)` + `COLLAPSE_VERDICT = "INDETERMINATE — TRIBUNAL COLLAPSE"`, llamado en `run()` tras `_maybe_escalate`. Si `agents_consulted==0` → veredicto retenido (INDETERMINATE + reasoning fail-closed). **BINDING** verdict-path gate, SEPARADO de la capa confidence/escalation NON-BINDING (que nunca toca final_verdict). **No puede enmascarar un INVIABLE real** (≥1 FATAL exige ≥1 agente que contribuya). Idempotente.
- `schema.py`: doc de `final_verdict` +estado colapso. `smoke_test_e2e.py`: test `f_collapse_fail_closed` (colapso→INDETERMINATE + inverso INVIABLE intacto) + `b_unified_output` collapse-aware SKIP (el harness tampoco debe fail-open).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️
**DS repo v3.23.0 = CERTIFICADO (`PA-20260712-002`).** Sin version-gap. PA-20260711-002 (v3.22.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

### RE-CERT SUSTANTIVA 7-EJES — COMPLETA ✅
- **Por qué SUSTANTIVA (no CONFIRMATORY):** LW-7 es el **primer cambio orchestrator VERDICT-BINDING** (cambia `final_verdict` en colapso). Los previos collapse-path LW-5/LW-6 fueron CONFIRMATORY *porque* eran NON-BINDING.
- **Grade de evidencia = $0 forced-collapse** (idéntico a LW-5/LW-6): un colapso no tiene llamadas exitosas → 0/40 calls → $0, sin Opus pago. La excepción #34 (1 Opus pago) NO aplicó a este cert (solo aplica a deltas del *healthy synthesis path*, como LW-2 v3.19.0).
- **7-ejes:** A1–A7 todos PASS. A6 coherence MEJORÓ una incoherencia pre-existente (antes verdict=SOLID contradecía confidence=LOW en colapso; ahora verdict/reasoning/confidence/escalation/SSM concuerdan en "collapse").
- **Evidencia (máquina real):** smoke 13/13 offline (0 FAIL, 1 SKIP=b) con `f_collapse_fail_closed` + `e_monotonic_verdict` + `c_fallback_intact` + `inverse_INVIABLE_kept` PASS; **LIVE forced-collapse `DS-8C9732B9` $0** (0/40 calls, puerto muerto 9999) → `VEREDICTO: INDETERMINATE — TRIBUNAL COLLAPSE` + Confidence LOW + Escalation NO "zero agent coverage" + **SSM safely inert** ("verdict not recognized as qualifying") + banner v3.23.0. `compute_confidence`/`Finding`/`_apply_confidence`/motor-veredicto byte-idénticos.
- **CERT:** `PA-20260712-002` — DS **v3.23.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **10/10/2026 o v4.0.0**. **SUPERSEDES PA-20260711-002** (v3.22.0). `JARP_BENCHMARK_LIVE = v3.23.0`.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s37)
1. Código LW-7 (2 files committed): `tribunal_transversal.py` (`_apply_collapse_guard` + `COLLAPSE_VERDICT` + call en `run()`), `schema.py` (doc final_verdict). Local/gitignored: `smoke_test_e2e.py` (`f_collapse_fail_closed` + `b` collapse-aware SKIP). **Read-back byte-exacto confirmado pre-cert** (nunca rubber-stamp).
2. Bump atómico §4.14.1: `bump_stamps.ps1 -Apply` (23 files/69 stamps, `-OldVersion 3.22.0 -NewVersion 3.23.0`) + banners orchestrator (main×2/wizard/transparency v3.22.0→v3.23.0 vía one-shot) + CHANGELOG `[3.23.0]` + cert block + fila roadmap README×2 + CLAUDE×2 (incl. `**ACTIVE — v3.23.0**`).
3. **Doc-consistency (eje A2):** README Feature Set + Roadmap y CLAUDE Roadmap + bottom ACTIVE necesitaban fila v3.23.0 (drift recurrente — bump_stamps no cubre roadmap ROWS ni ACTIVE) → añadidas pre-commit. **Lección: cada bump, verificar roadmap rows + ACTIVE en README/CLAUDE explícitamente.**
4. Canónicos vía `sync_canonicals_v3_23_0.py` (9 ediciones anchored, EOL-aware): init header+#7+SUPERSEDED-prepend; toolkit header+#30(Version/CERT STATUS/supersede-tail/Previous-certs)+#16 → v3.23.0/PA-20260712-002. **AMBOS concuerdan posicionalmente.**
5. **5 one-shots en `_livewatch/` (gitignored, NO entran al árbol):** `apply_lw7_collapse_guard`, `harden_b_collapse_aware`, `bump_banners_v3_23_0`, `apply_docs_v3_23_0`, `sync_canonicals_v3_23_0`. Fixture `_livewatch/legal_ai_companion_tos.txt` también gitignored. Borrar para limpieza (opcional; el commit es limpio igual por gitignore).
6. `git rm dark-strategist-continuity-prompt_v35.md`. v36 = único continuity.
7. **Commits de cierre** (registrar SHAs tras push): DS cert commit (parent `d954736`) + jarp-toolkit sync commit (parent `7e29023`).

---

## DEUDA TÉCNICA — POST-SESIÓN 37

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **LW-7 fail-closed collapse** | ✅ CERRADA | verdict-BINDING guard; colapso→INDETERMINATE | 0/0/0/0, SUSTANTIVA, PA-20260712-002. |
| **#1 cert-surface↔runtime gap** | 🔴 **ABIERTO (MAYOR)** | 19 variants nunca inyectados al runtime N1 | Decisión (a) fix injection / (b) re-scope cert. **Candidato #1 s38.** |
| **WATCH live L07 (LG08/LG09)** | 🟡 ABIERTO (entangled con #1) | nunca ejercido conductualmente | Sin sentido ejercerlo hasta resolver #1 (las reglas no se inyectan → el "live L07" mediría criterio de modelo, no enforcement). |
| **Drift roadmap rows / ACTIVE** | ✅ CERRADA (s37) | README/CLAUDE fila v3.23 + ACTIVE | Vigilar en cada bump. |
| **LW-1..6 / earlier** | ✅ CERRADAS | stack confidence/escalation/lenses/signals/provenance/collapse | NON-BINDING (salvo LW-7 BINDING). |

### BACKLOG VALOR-AGREGADO — pendiente
- **🔴 #1 (cert-surface↔runtime gap)** — candidato #1 de valor REAL inmediato. Es la decisión más importante en el horizonte: o se cablea la superficie forense al runtime (a), o se re-escopea el cert-chain (b). Todo cambio variant-only futuro (incl. el propio L07 de v3.22.0) depende de esto.
- **🟡 WATCH live L07** — sólo tiene sentido DESPUÉS de resolver #1 (si se elige (a), ejercer LG08/LG09 en vivo prueba el enforcement real).
- **🟢 LW-4** (desempate dominio posicional) — opcional/DESCARTABLE.
- **STANDING:** cada sesión, velar que el sistema sea mejor. LW-7 cerró un fail-open de seguridad real. #1 es la próxima fuente de valor de fondo.

---

## ESTADO ACTUAL VERIFICADO (12/07/2026 — fin s37)

### Repo dark-strategist-agent
- **v3.23.0 — CERTIFICADO (`PA-20260712-002`)**. Default `claude-opus-4-7`. Commit de cierre s37 (**registrar SHA**; parent `d954736`).
- **MODIFICADO:** `orchestrator/tribunal_transversal.py` (LW-7 guard + call + banner v3.23.0); `orchestrator/schema.py` (doc final_verdict); `orchestrator/{main,wizard}.py` (banners v3.23.0); 23 product-face stamps (base+router+19 variants+README+CLAUDE); `CHANGELOG.md` ([3.23.0]+cert); `README.md`+`CLAUDE.md` (roadmap rows + ACTIVE); `dark-strategist-continuity-prompt_v36.md`. **git rm:** v35.
- **Verdict path hoy:** `_synthesize`→`_maybe_escalate`→**`_apply_collapse_guard`** (nuevo, BINDING)→provenance→SSM. `final_verdict` states: INVIABLE / VIABLE W/ CRITICAL / VIABLE W/ ADJUSTMENTS / SOLID UNDER PRESSURE / **INDETERMINATE — TRIBUNAL COLLAPSE** (nuevo). Motor ≥1 FATAL→INVIABLE INTACTO.
- **Runtime prompt surface (crítico, ver #1):** N1 = MASTER_TEMPLATE dinámico (prompt_engine.py); N2 permanentes = hardcoded en sub_agent_spawner.py. **Los 19 variant .md NO se cargan.** `router.py`/`DomainRouter.load_domain_prompt` = huérfano.
- `tools/bump_stamps.ps1` (params `-OldVersion -NewVersion -Apply`; 23/69). `gc.auto 0`. **7 skills, 9 N2, 20 dominios.**
- `_livewatch/` gitignorado + destrackeado (verificar por read-back del árbol → 404).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s37. Sin cambios.

### Repo jarp-toolkit
- Sincronizado a v3.23.0/PA-20260712-002. PRIVADO. HEAD = sync commit s37 (**registrar SHA**; parent `7e29023`). **AMBOS canónicos concuerdan posicionalmente.** `.claude-init.md`=LF, `JARP_TOOLKIT.md`=CRLF.

### free-claude-code
- Proxy $0. JARP fijó **"todo NVIDIA"** en s37 (todas las corridas non-cert vía NVIDIA/proxy). `fcc-server` NO en PATH — instalar/arrancar antes de usar. **Gotcha:** el SDK Anthropic exige `api_key` no-vacío aun con proxy → usar dummy (`sk-local`); key vacía = auth-fail antes de la 1ª llamada. Cert collapse-grade = puerto muerto 9999 → $0 (no necesita proxy ni Opus).

---

## PROTOCOLO DE INICIO PARA SESIÓN 38
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v36).
2. **PHASE 0 — Verificación:**
   - v35 borrado, v36 único continuity.
   - Repo en v3.23.0. **Cert: DS v3.23.0 `PA-20260712-002` ACTIVE.** PA-agent v1.3.0 ACTIVE. `PA-20260711-002` SUPERSEDED.
   - **AMBOS canónicos concuerdan POSICIONALMENTE** en v3.23.0/PA-20260712-002 (NO Select-String — leer campos reales, lección drift s33/s34).
   - **`orchestrator/_livewatch` NO trackeado — verificar por READ-BACK DEL ÁRBOL** (`get_file_contents orchestrator/`→ sin `_livewatch` en el listado / 404 al path directo), NUNCA por commit msg (lección s35).
   - HEAD remoto vía `list_commits` (perPage=3): DS = cert commit s37 (parent `d954736`); jarp-toolkit = sync commit s37 (parent `7e29023`).
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 34 SESIONES (4–37).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s38 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Valor-agregado** — **candidato #1: resolver el gap #1 (cert-surface↔runtime).** Es LA decisión arquitectónica de fondo: (a) cablear la carga del variant al pipeline N1 (fix injection) vs (b) re-escopear el cert-chain (variants = spec). Recomendación: (a). JARP delega criterio.
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | **veredicto determinista (≥1 FATAL→INVIABLE)** | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings+catálogo+comments feature-landing = content-based/congelados) | bump_stamps NO cubre orchestrator/*.py ni CHANGELOG ni roadmap-rows ni ACTIVE → bump manual aparte | Sintetizador VIVO, fallback determinista = producción | free-claude-code: free/NVIDIA para no-cert, forced-collapse $0 o Opus real para cert | Sev×Likelihood NON-BINDING | orden monotónico FATAL→LATENT al insertar filas | **leer el módulo/archivo real antes de incorporar/diseñar/anclar** | mi-filesystem preserva escapes byte-exacto | confianza/escalación/lentes/señales/provenance/corroboración = metadata NON-BINDING post-hoc; NUNCA tocan `final_verdict`/`Finding`/`compute_confidence`.

**De s25–s36:** ver v35 (stack LW-1..6/confidence/escalation/L07 AIPL/EOL per-file/Select-String prohibido/canónicos por one-shot anclado/live-fallo puerto 9999/read-back del árbol para untrack/§4.14.1). Todo vigente.

**De s37 (nuevas):**
- **Fail-closed en el verdict-path (LW-7):** un colapso total (`agents_consulted==0`) DEBE retener el veredicto (INDETERMINATE — TRIBUNAL COLLAPSE), nunca fail-open al all-clear. El guard es BINDING pero SEPARADO de la capa confidence NON-BINDING; reusa `agents_consulted` (aterrizado por LW-5); no puede enmascarar un INVIABLE real. **No re-introducir el fail-open (colapso→SOLID).**
- **Grade de evidencia por tipo de delta:** collapse-path = forced-collapse $0 (no Opus); healthy-synthesis-path = Opus real cert-grade (#34). Clasificación SUSTANTIVA/CONFIRMATORY es ORTOGONAL a la grade: SUSTANTIVA si el delta es verdict-BINDING (toca final_verdict), CONFIRMATORY si NON-BINDING.
- **El harness de test tampoco debe fail-open:** `b_unified_output` ahora SKIPea en colapso (0 agents no ejercita síntesis viva) en vez de PASS/FAIL falso.
- **cert-surface↔runtime:** ANTES de tratar un variant .md como verdict-binding, confirmar que el runtime LO CARGA. Hoy NO los carga (#1 abierto). El cert de una superficie inerte certifica spec, no comportamiento — resolver #1 antes de futuros cambios variant-only "sustantivos".
- **`--document` mode:** `type="general"` (hardcoded) + subscenario=filename-stem; `_resolve_domain` rutea por stem (DOMAIN_MAP no tiene "general" → cae al stem). Contenido del doc NO afecta ruteo. Aun ruteando a "Legal", solo cargan roles+tools genéricos legales, nunca el catálogo L07.

---

## DESCARTES — NO REINTRODUCIR
(Todos los de v35 siguen vigentes.) **Añadidos s37:** re-introducir el fail-open colapso→SOLID UNDER PRESSURE | hacer que la capa confidence/escalation toque `final_verdict` | gastar Opus pago en un cert de collapse-path (es $0 por definición) | tratar un variant .md como verdict-binding sin confirmar que el runtime lo carga | ejercer el WATCH live L07 antes de resolver #1 (mediría criterio de modelo, no enforcement).

---

## REFERENCIAS RÁPIDAS
- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v36.md` (v35 borrado s37)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). init=LF, toolkit=CRLF. **Verificar concordancia POSICIONAL al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. `list_commits` (perPage=3) + `get_file_contents` para verificación remota. GitHub `search_code` NO indexa el repo (0 hits en símbolos existentes) — usar SOLO lectura real de archivos para trazar código.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. `cd` antes de scripts. `bump_stamps.ps1` params NOMBRADOS `-OldVersion -NewVersion` + `-Apply`. **NO hay `pytest` — los test_*.py auto-ejecutables: `python test_X.py` / `python smoke_test_e2e.py <doc> <size>`.**
- **Método de edición:** stamps product-face = `bump_stamps.ps1 -Apply`. Multi-archivo/multi-edit + canónicos = one-shot Python anclado all-or-nothing + EOL-AWARE per-file (detecta CRLF/LF, normaliza a \n, match, restaura EOL), dry-run→--apply, en `_livewatch/` (gitignored). **Anclas SIN em-dash/box cuando se pueda → count==1 robusto; si inevitable, copiar byte-exacto del read (dry-run aborta seguro si falla).** Archivo nuevo/full-overwrite pequeño = mi-filesystem directo + read-back. **NO ejecuto Python/PS en la máquina de JARP → JARP corre.**
- **Live e2e:** sano = NVIDIA/proxy (no-cert) o Opus real (cert healthy-path). Colapso = puerto muerto 9999 → $0. Key dummy no-vacía obligatoria con proxy.

### Commits de cierre sesión 37
**DS — commit de cierre (cert):**
```
feat: DS v3.23.0 — LW-7 fail-closed verdict on tribunal collapse (a 100% collapse [agents_consulted==0] now withholds the verdict as INDETERMINATE — TRIBUNAL COLLAPSE instead of the all-clear SOLID UNDER PRESSURE; _apply_collapse_guard in run() after escalation; BINDING verdict-path gate distinct from the NON-BINDING confidence/escalation layers; cannot mask a real INVIABLE) — SUBSTANTIVE re-cert JARP_CERTIFIED PA-20260712-002 (0/0/0/0); smoke 13/1 GREEN incl f_collapse_fail_closed + e_monotonic + inverse INVIABLE kept; LIVE forced-collapse DS-8C9732B9 $0 -> INDETERMINATE
```
Incluye: `orchestrator/{tribunal_transversal,schema,main,wizard}.py`, product-face stamps (23), `CHANGELOG.md` (+cert), `README.md`, `CLAUDE.md`, `dark-strategist-continuity-prompt_v36.md`; `git rm dark-strategist-continuity-prompt_v35.md`. NO incluye one-shots ni fixture (en `_livewatch/` gitignored). `_livewatch/` gitignorado + destrackeado.
**jarp-toolkit — sync:**
```
docs: sync DS v3.23.0 / PA-20260712-002 (LW-7 fail-closed verdict on tribunal collapse) — header + entry #30 (Version/CERT STATUS/supersede-tail/Previous certs) + note #16 + .claude-init header + #7 + SUPERSEDED
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 37

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.23.0** | **PA-20260712-002** | **v3.23.0** | ✅ ACTIVE | 10/10/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260711-002 (v3.22.0), PA-20260613-004 (v3.21.0), PA-20260613-002 (v3.20.0), PA-20260612-002 (v3.19.0), PA-20260611-002 (v3.18.0), PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 37 (auto-mejora del próximo Claude)

1. **Una investigación de "cerrar un WATCH barato" destapó el hallazgo mayor de la sesión (#1).** Preparar el fixture L07 obligó a trazar el runtime real → se descubrió que los 19 variants nunca se cargan. STANDING en acción: no se cerró barato; se encontró valor de fondo. **Trazar el grafo de imports COMPLETO antes de asumir que una superficie certificada está cableada.**
2. **El auditor NO rubber-stampea: el fail-open del colapso (LW-7) estuvo latente a través de LW-5/LW-6.** Esos fixes hicieron honesta la confidence pero dejaron el `final_verdict` fail-open. El fallo de infra en vivo lo expuso. Fail-closed = dirección de seguridad correcta para un forense.
3. **Grade de evidencia ≠ clasificación de cert.** collapse-path = $0 forced-collapse (no Opus, como LW-5/6); SUSTANTIVA/CONFIRMATORY depende de si el delta es verdict-BINDING. LW-7 = $0 grade PERO SUSTANTIVA (primer binding collapse-path). No confundir las dos cosas (evité gastar Opus innecesario).
4. **Drift de roadmap rows + ACTIVE en README/CLAUDE:** bump_stamps NO los cubre. Verificar explícitamente en cada bump (eje A2). Cerrado pre-commit en s37.
5. **Gotcha proxy:** el SDK Anthropic exige api_key no-vacío aun apuntando al proxy. Key vacía = auth-fail antes de la 1ª llamada (2 runs quemados en s37 por esto). Dummy `sk-local` obligatorio.
6. **GitHub `search_code` no indexa este repo** (0 hits en símbolos que existen). No apoyarse en él; lectura real de archivo es la única verificación de código válida.
7. **TRADING: 34 SESIONES POSTERGADO (4–37). NO re-confrontar.** Si s38 tampoco elige A, tratar backlog DS como prioridad de facto — priorizar #1 (cert-surface↔runtime) sobre relleno.
8. **#1 es la decisión arquitectónica en el horizonte.** No es opcional-descartable como LW-4; toca la identidad del producto (¿los variants forenses son runtime o spec?). Retomar en s38.
