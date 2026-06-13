# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 13/06/2026 (sesión 34 — DS v3.20.0 LW-5 confidence-collapse floor, shipped & JARP_CERTIFIED) | **Para:** Sesión 35
**Reemplaza:** v32 del 12/06/2026 (sesión 33)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v33.md`
**⚠️ BORRAR en este cierre:** v32 (`git rm` en el commit de cierre). v33 = único continuity vigente. Subir v33 al PROYECTO claude.ai + quitar v32.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 34 (resumen ejecutivo)

Track elegido: **B — Backlog valor-agregado → LW-5** (confidence false-positive sobre colapso del tribunal, candidato #1). Trading (A) NO se eligió (**31ª sesión postergada, 4–34**). Recordatorio una vez, sin re-confrontar (ya recomendado reescribir userPreferences en s33).

**Resultado: DS v3.20.0 shipped y CERTIFICADO** (`PA-20260613-002`).

### 0. CORRECCIÓN DE DRIFT s33 (detectada en PHASE 0 de s34)
El cierre s33 afirmó haber bumpeado el campo `**Version:**` de la entrada **#30** de `JARP_TOOLKIT.md` a v3.19.0 y lo "verificó" por `Select-String`. **El bump al #30 nunca se aplicó:** el bloque Ruta-3 de v3.19.0 aterrizó en el lugar equivocado (línea huérfana entre repo #26 y `### 27`), y `Select-String` matcheó ESE string huérfano → falso-positivo. El campo #30 quedó en `3.18.0 / PA-20260611-002`. Corregido en s34 con commit `docs:` separado en jarp-toolkit (`b6a7ab8`): bump del #30 Version + eliminación de la huérfana. **Lección dura:** verificar campos canónicos POSICIONALMENTE (re-leer el bloque/entrada o anclar por contexto), nunca por presencia de string a secas. Cert no afectado (el repo SÍ estaba en v3.19.0; era drift de marcador documental).

### 1. DS v3.20.0 — LW-5 CONFIDENCE FALSE-POSITIVE ON TRIBUNAL COLLAPSE (NON-BINDING)
`_apply_confidence` (en `tribunal_transversal.py`) hacía `unified.agents_consulted = len(all_outputs)`, **contando agentes que fallaron** (connection-error / BUDGET_EXCEEDED / parse-fail — se appendean a `all_outputs` con clave `"error"` y SIN `findings`; ver `_run_rol_layer`/`_run_forense_layer`/`_call_agent`). En un colapso 100% del tribunal (0 findings), la rama HIGH de `compute_confidence` (`driver_finding_count==0`, "veredicto limpio") reportaba **HIGH sobre cero análisis** — señal de auditabilidad engañosa.

**Fix (100% en `_apply_confidence`, 1 línea):**
```
contributing = [o for o in all_outputs if isinstance(o, dict) and "error" not in o]
unified.agents_consulted = len(contributing)
```
- Colapso 100% (todos errored) → `agents_consulted=0` → `n<2` → **LOW**. Cobertura parcial (p.ej. 2 sanos + 3 errored) → `agents_consulted=2` → `n<3` → MODERATE (honesto). Doc genuinamente limpio (agentes sanos, 0 findings) → HIGH **preservado** (la rama clean-legítima del schema sigue viva).
- **Discriminador = COBERTURA de agentes (clave `"error"`), NO conteo de findings.** NO colapsar todo "0 findings" a LOW: rompería el HIGH limpio-legítimo (intención v3.11.0). El test `test_confidence.py` línea `(4, False, 0, 0) -> HIGH` confirma que el branch clean del schema queda intacto — el fix opera aguas arriba (en el conteo), no toca `compute_confidence`.
- **Veredicto INTACTO:** `final_verdict`, `Finding`, `compute_confidence` (schema) SIN tocar. Determinista, NON-BINDING.
- **`orchestrator/test_apply_confidence.py`** 16→**24 checks**: C10 colapso (5 errored, clean)→LOW + `agents_consulted==0` + verdict intact; C11 cobertura parcial (2 sanos + 3 errored)→MODERATE + `agents_consulted==2`; C12 no-regresión (3 sanos corroborando + 2 errored)→`agents_consulted==3`, corroboración intacta, HIGH. `final_verdict` invariante en todos.

### 2. RE-CERT DS v3.20.0 — COMPLETA ✅ (CONFIRMATORY)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260613-001`) PASS. 7-ejes Level 1 JARP DEEP sobre delta v3.19.0→v3.20.0.
- **Por qué CONFIRMATORY:** el fix vive 100% en la capa de confianza post-veredicto (`_apply_confidence`). Superficie forense (19 variants + 7 skills + base + router CONTENT) byte-idéntica salvo stamps. `final_verdict`/`Finding`/`compute_confidence` intactos. Determinista, NON-BINDING.
- **Evidencia (máquina real, post-apply + post-bump):** `test_apply_confidence` **24/24** + `test_confidence` **10/10** + **LIVE collapse e2e**:
  - **`DS-36E093BE`, $0 (0/40 calls):** backend muerto (`ANTHROPIC_BASE_URL=http://localhost:9999` + dummy key) → 7 agentes (4 ROL + 3 FOR) `Connection error` → fallback; tribunal **(0 agents)**, 0 findings → **`Confidence: LOW`** (pre-fix: HIGH). `agents_consulted=0`. Veredicto `SOLID UNDER PRESSURE` (fallback determinista). Escalación: LOW disparó 1 ronda (lenses FAILURE_MODE_HUNTER/FALSIFIER), también falló contra el backend muerto, **paró** (1 ronda, acotado, sin loop).
  - **Patrón reutilizable:** ejercer paths de fallo en vivo = apuntar a puerto muerto → $0 (agentes fallan antes de llamar). No requiere Opus.
- **CERT EMITIDO:** `PA-20260613-002` — DS **v3.20.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **13/09/2026 o v4.0.0**. **SUPERSEDES PA-20260612-002** (v3.19.0).
- **Bump:** `bump_manual_v3_20_0.py` (banners operator-visible: main×2 / wizard / tribunal_transversal + CHANGELOG `[3.20.0]`; **NO config knob** — LW-5 no agrega knob) + `bump_stamps.ps1 -OldVersion 3.19.0 -NewVersion 3.20.0 -Apply` (23 files / 69 stamps). Ambos EOL-aware, all-or-nothing, dry-run→apply. One-shots BORRADOS antes del commit.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.20.0 = CERTIFICADO (`PA-20260613-002`).** Sin version-gap. PA-20260612-002 (v3.19.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s34)
1. Archivos en disco (PHASE 2/3): `orchestrator/tribunal_transversal.py` (`_apply_confidence`: `agents_consulted` cuenta solo contribuyentes sin `"error"` + banner v3.20.0; tag `#--- LW-5:`), `orchestrator/test_apply_confidence.py` (16→24 checks), banners (`main.py`×2 / `wizard.py` / `tribunal_transversal.py`), product-face stamps (23 files), `CHANGELOG.md` (bloque `[3.20.0]` + cert).
2. Canónicos vía one-shot anclado `sync_canonicals_v3_20_0.py` (NO Ruta-3 manual — para evitar el drift s33): `.claude-init.md` (header + #7 + SUPERSEDED) + `JARP_TOOLKIT.md` (header + #30 Version + CERT STATUS + Previous-certs + Note #16) → v3.20.0/PA-20260613-002. Verificado: init re-leído OK posicionalmente; toolkit por replace-de-anchor-único in-place + read-back-assert (sin riesgo de huérfana — no hubo inserción). **AMBOS canónicos concuerdan.**
3. **EOL per-file confirmado:** `.claude-init.md` = **LF**; `JARP_TOOLKIT.md` = **CRLF**; los `.py` = **CRLF**. El one-shot detectó y preservó cada uno. Nunca asumir EOL.
4. One-shots BORRADOS antes de los commits: `apply_lw5_fix.py`, `bump_manual_v3_20_0.py` (DS), `sync_canonicals_v3_20_0.py` (jarp-toolkit).
5. `git rm dark-strategist-continuity-prompt_v32.md`. v33 = único continuity.
6. **Commits de cierre** (registrar SHAs tras push vía GitHub Desktop): DS cert commit + jarp-toolkit sync commit.
7. **`_livewatch/`** sigue gitignorado (blindado s33); el fixture `lw5_collapse.txt` es local-only, no se commitea. Sanity de untracked ANTES de pushear.

---

## DEUDA TÉCNICA — POST-SESIÓN 34

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.20.0** | ✅ CERRADA | v3.20.0 CERTIFICADO (PA-20260613-002) | 0/0/0/0, CONFIRMATORY. |
| **LW-5 confidence-collapse floor** | ✅ CERRADA | agents_consulted cuenta solo contribuyentes (sin `"error"`) | test 24/24; live DS-36E093BE Confidence LOW $0. NON-BINDING. |
| **Drift #30 Version (s33)** | ✅ CERRADA (s34) | bump real del #30 + borrado huérfana (jarp-toolkit b6a7ab8) | Verificar canónicos POSICIONALMENTE, no Select-String. |
| **LW-2 confidence corroboration** | ✅ CERRADA (s33) | overlap title+evidence same-sev + floor exacto | Sin cambio. |
| **WATCH b_unified_output** | ✅ CERRADA (s33) | live synthesizer vivo emitió UnifiedVerdictOutput real | Sin cambio. |
| **LW-3 / LW-1** | ✅ CERRADAS (s32/s31) | provenance granularity / domain resolver | Sin cambio. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟠 LW-6 (NUEVO, descubierto en vivo s34):** short-circuit de escalación cuando la cobertura de agentes es CERO. Observado en DS-36E093BE: el tribunal colapsado dio LOW → `should_escalate` disparó 1 ronda que también falló contra el backend muerto. Es **acotado** (`rounds_done<max_rounds` + budget caps, no loop) y honesto, pero desperdicia intentos escalando hacia un backend caído. Mejora: no escalar si `agents_consulted==0` (cobertura nula ≠ baja corroboración). Candidato de bajo esfuerzo (gate en `_maybe_escalate`/`should_escalate`). Slice propio.
- **🟢 LW-4 (refinamiento opcional):** desempate de dominio posicional ("primer token de dominio del filename"). LW-1 ya cierra el defecto; pulido de intuición. Evaluar valor antes de invertir — candidato a descartar.
- **P5 extensión P14/P20** (candidato): reputational-risk a Public Sector (P14) + Startup (P20). Valor incremental dudoso.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real.

---

## ESTADO ACTUAL VERIFICADO (13/06/2026 — fin s34)

### Repo dark-strategist-agent
- **v3.20.0 — CERTIFICADO (`PA-20260613-002`)**. Default `claude-opus-4-7`. Commit de cierre = el cert commit s34 (**registrar SHA tras push**; parent `8943efe` = HEAD inicio s34).
- **MODIFICADO:** `orchestrator/tribunal_transversal.py` (`_apply_confidence` LW-5 + banner v3.20.0); `orchestrator/test_apply_confidence.py` (24 checks); `orchestrator/{main,wizard}.py` (banners); 23 product-face stamps; `CHANGELOG.md`; `dark-strategist-continuity-prompt_v33.md`. **git rm:** v32.
- **De s33 vigente:** `_apply_confidence` corroboración por similitud (overlap title+evidence same-sev + floor exacto legacy); `test_apply_confidence.py`; `config.example.json` `corroboration_min_overlap:4`.
- **De s32/s31/s30 vigente:** `txt_atomic_lines` per-canal + `test_signals_granularity`; `_resolve_domain` boundary-aware + most-specific-first + order-invariant + `test_domain_resolver`; `skills/reputational-risk/` + `test_reputational_risk`.
- **De s29–s25 vigente:** `overlap_score` + provenance post-veredicto + `test_provenance`; canal `--signals` + `test_signals`; `archetype_lenses.py` + `test_archetype_lenses`; `schema.should_escalate`/`compute_confidence` + `test_escalation`/`test_confidence`.
- `tools/bump_stamps.ps1` (NO cubre orchestrator/*.py ni CHANGELOG ni config; **dry-run por defecto — requiere `-Apply`**; params NOMBRADOS). `gc.auto 0` activo. `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus`/`--signals` activos.
- **7 skills**, **9 sub-agentes N2 permanentes**, **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` + `_livewatch/` GITIGNORADOS (local-only). `_livewatch/lw5_collapse.txt` = fixture throwaway s34.

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s34. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/CERT STATUS/Previous certs) + #16 + `.claude-init.md` header + #7 → v3.20.0/PA-20260613-002. PRIVADO. HEAD = el sync commit s34 (**registrar SHA tras push**; parent `b6a7ab8` = fix drift s34). **AMBOS canónicos concuerdan (verificado posicionalmente).** `.claude-init.md`=LF, `JARP_TOOLKIT.md`=CRLF.

### free-claude-code
- Proxy $0 para no-cert. **`fcc-server` NO en PATH ni levantado — instalar/arrancar antes de usar** (Python 3.14+, `uv`, `fcc-server`, Admin UI `/admin`). SDK exige `api_key` no vacío aunque uses proxy → dummy `sk-local-dummy` + `ANTHROPIC_BASE_URL`. **Cert = Opus real (sk-ant, sin proxy).** `load_config` PRECEDE config.json sobre env var para `api_key`. Recarga Opus: `platform.claude.com/settings/billing` (NO claude.ai). **Para ejercer paths de FALLO en vivo: apuntar a puerto muerto (`http://localhost:9999`) → $0.**

---

## PROTOCOLO DE INICIO PARA SESIÓN 35
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v33).
2. **PHASE 0 — Verificación:**
   - v32 borrado, v33 único continuity.
   - Repo en v3.20.0. **Cert: DS v3.20.0 `PA-20260613-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260612-002` SUPERSEDED.
   - **Verificar AMBOS canónicos concuerdan POSICIONALMENTE** (toolkit #30 Version + CERT STATUS + nota #16 + init #7 en v3.20.0/PA-20260613-002) — lección drift s33/s34. NO confiar en Select-String a secas.
   - **`_livewatch/` NO trackeado** (gitignorado). Si reaparece, `git rm -r --cached _livewatch`.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 31 SESIONES (4–34).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s35 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — **LW-6 (escalation short-circuit sobre cobertura cero, candidato #1)**; LW-4 (opcional/descartable); P5 extensión P14/P20.
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes+comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG ni config → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE | RAG = MECANISMO | ContextBuilder document-free | infinity/Docker RECHAZADO | **leer el módulo real antes de incorporar/diseñar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case | Floor R2/señales/provenance/corroboración = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25–s33:** Confianza/escalación/lentes/señales/provenance/corroboración = metadata NO-VINCULANTE, determinista, post-hoc; NUNCA tocan `final_verdict`/`Finding`/`compute_confidence`. Docstrings de módulo congelados. Scripts de edición newline-aware + encadenados por archivo + all-or-nothing + dry-run. Riesgo reputacional = SKILL markdown (#7); Failure Catalog VINCULA severidad; activación⊆binding. Domain routing = boundary-aware + MOST-SPECIFIC-FIRST + ORDER-INVARIANT. Segmentación `.txt` per-canal (`txt_atomic_lines`). Provenance/corroboración POST-veredicto → corrección probable 100% offline (el e2e ejerce el código real). Leer de vuelta lo que UNO entregó. `bump_stamps.ps1` dry-run por defecto → SIEMPRE `-Apply`. Corroboración = OVERLAP sobre `title+evidence` same-sev + floor exacto legacy; title-only infla false-positives. NO propagar source-agent por finding. Validar la propia heurística contra su peor modo de falla.

**De s34 (nuevas):**
- **LW-5 / confidence-collapse floor:** `agents_consulted` cuenta SOLO agentes contribuyentes (`isinstance(o, dict) and "error" not in o`). Colapso 100% → LOW; NON-BINDING. **El discriminador es la COBERTURA de agentes (clave `"error"`), NO el conteo de findings.** NO colapsar todo "0 findings" a LOW — rompería el HIGH limpio-legítimo del schema (`compute_confidence` intacto, branch `driver_finding_count==0 → HIGH` deliberadamente vivo).
- **Verificación canónica POSICIONAL, NO Select-String:** el drift #30 de s33 nació de "verificar" por presencia de string, que matcheó una línea huérfana mal insertada. Verificar re-leyendo el bloque/entrada o por replace-de-anchor-único in-place (sin inserción → sin huérfana). El grep confirma existencia, no ubicación.
- **EOL per-file real:** `.claude-init.md`=LF, `JARP_TOOLKIT.md`=CRLF, `.py`=CRLF. Detectar per-file SIEMPRE; nunca asumir.
- **Live e2e de paths de FALLO = backend muerto (puerto 9999) → $0** (agentes fallan antes de llamar; no consume Opus). Patrón para ejercer colapso/timeout sin costo.
- **Canónicos vía one-shot anclado, NO Ruta-3 manual,** cuando hay riesgo de mis-paste (replace de anchor único in-place = sin huérfana; el manual fue lo que falló en s33).

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance/corroboración como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica | bumpear docstrings/catálogo/comments-feature-landing congelados | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts que escriben cada edit desde el snapshot original | activación dormida sobre activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` | riesgo reputacional como lente-arquetipo (usar SKILL) | duplicar Failure-Catalog rows | activar skill en dominios sin Failure Catalog rows | transcribir líneas largas como anclas (usar line-based / re-leer) | domain routing por substring crudo / acoplado al orden | borrar claves cortas del DOMAIN_MAP | cambiar el split `.txt` de `load_corpus_files` globalmente | reusar la variable de loop como buffer | correr `bump_stamps.ps1` sin `-Apply` | corroborar confianza por TÍTULO SOLO | propagar source-agent por finding para corroborar | asumir `.py`=LF (son CRLF) | pushear el commit de cierre antes de blindar `.gitignore` para throwaways | **colapsar todo "0 findings" a LOW (rompe el HIGH limpio-legítimo); el discriminador de cobertura es la clave `"error"`, NO el conteo de findings — s34** | **verificar campos canónicos por Select-String a secas (encuentra el string, no su ubicación; usar re-lectura del bloque o replace-de-anchor-único in-place) — s34** | **Ruta-3 manual para canónicos cuando hay riesgo de mis-paste (usar one-shot anclado) — s34** | **asumir EOL uniforme (.claude-init=LF, JARP_TOOLKIT=CRLF, .py=CRLF; detectar per-file) — s34**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v33.md` (v32 borrado s34)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan POSICIONALMENTE al cierre.** init=LF, toolkit=CRLF.
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. env var = `$env:VAR="..."`; limpiar con `Remove-Item Env:\VAR`. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). `bump_stamps.ps1` con params NOMBRADOS + **`-Apply`** (`-OldVersion X -NewVersion Y -Apply`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1 -Apply`. Banners orchestrator + CHANGELOG + config knobs = script Python anclado all-or-nothing + EOL-AWARE per-file (dry-run → --apply), a la RAÍZ. Edits prosa/código pequeños/archivo nuevo = mi-filesystem directo (full-overwrite; verificar read-back). Canónicos (archivos grandes) = **one-shot anclado** (preferido sobre Ruta-3 manual; replace de anchor único in-place evita huérfanas) o Ruta-3 con OK explícito. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Higiene de fixtures/one-shots:** throwaways (`_livewatch/`, smoke) en `.gitignore` ANTES de cualquier commit; one-shots BORRADOS antes del commit de cert; sanity de untracked en GitHub Desktop antes de pushear.
- **Confidence (`_apply_confidence`):** corroboración por overlap `title+evidence` same-sev + floor exacto legacy; `agents_consulted` cuenta solo contribuyentes (sin `"error"`). NON-BINDING. `compute_confidence` (schema) intacto.
- **Live e2e:** sano = Opus real (cert) o free proxy (no-cert). **Fallo/colapso = backend muerto puerto 9999 → $0.**
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → 13 PASS / 0 FAIL con key+proxy, o 12 PASS / 1 SKIP offline. Tests s34: `test_apply_confidence` 24/0. `pip install rank_bm25 pydantic` antes.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 34
**Repo dark-strategist-agent — commit de cierre (cert):**
```
fix: DS v3.20.0 — confidence-collapse floor LW-5 (_apply_confidence grounds agents_consulted on contributing/non-errored agents only; a 100% tribunal collapse now yields LOW instead of HIGH over zero analysis; NON-BINDING, verdict path untouched) — test_apply_confidence 24/24 + live collapse e2e DS-36E093BE Confidence LOW $0 + JARP_CERTIFIED PA-20260613-002
```
Incluye: `orchestrator/tribunal_transversal.py`, `orchestrator/test_apply_confidence.py`, `orchestrator/{main,wizard}.py` (banners), product-face stamps (23 files), `CHANGELOG.md`, `dark-strategist-continuity-prompt_v33.md`; `git rm dark-strategist-continuity-prompt_v32.md`. NO incluye one-shots (borrados). `_livewatch/` gitignorado (no se cuela).
**Repo jarp-toolkit — sync:**
```
docs: sync DS v3.20.0 / PA-20260613-002 (LW-5 confidence-collapse floor) — header + entry #30 (Version/CERT STATUS/Previous certs) + note #16 + .claude-init header + #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 34

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.20.0** | **PA-20260613-002** | **v3.20.0** | ✅ ACTIVE | 13/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260612-002 (v3.19.0), PA-20260611-002 (v3.18.0), PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 34 (auto-mejora del próximo Claude)

1. **PHASE 0 atrapó un drift real.** El #30 Version de `JARP_TOOLKIT.md` seguía en v3.18.0 pese a que s33 lo dio por bumpeado — `Select-String` matcheó una línea huérfana mal insertada y dio falso-positivo. Verificar canónicos POSICIONALMENTE (re-leer el bloque) o por replace-de-anchor-único in-place. El grep confirma existencia, no ubicación.
2. **LW-5: el discriminador correcto no era el conteo de findings.** "0 findings" puede ser limpio-legítimo (HIGH) o colapso (debe ser LOW). El discriminador es la COBERTURA de agentes (clave `"error"`). Tocar `compute_confidence` habría roto el HIGH limpio; el fix fue aguas arriba, en `agents_consulted`. Leer el flujo real (cómo se appendea un agente fallido) reveló el discriminador limpio.
3. **Offline prueba la corrección; live prueba que el path se ejerce.** Los 24 checks prueban `_apply_confidence`; el live de colapso (backend muerto, $0) ejerció el HIGH→LOW end-to-end y confirmó `agents_consulted=0` + escalación acotada.
4. **Paths de fallo en vivo a costo cero:** apuntar el SDK a un puerto muerto. Útil para LW-6 y futuros tests de resiliencia.
5. **EOL no es uniforme:** init=LF, toolkit=CRLF, .py=CRLF. El one-shot EOL-aware per-file lo manejó; nunca asumir.
6. **One-shot anclado > Ruta-3 manual para canónicos.** El drift s33 fue mis-paste manual; el replace-de-anchor-único in-place no puede crear huérfanas. La transcripción de anchors largos desde caché es frágil (un anchor de init falló por "cert-grade" omitido + cláusula Prior mal copiada) — el all-or-nothing dry-run lo atrapó sin escribir. Re-leer el archivo real para anchors largos.
7. **TRADING: 31 SESIONES POSTERGADO (4–34). NO re-confrontar.** Ya recomendado reescribir userPreferences; si s35 tampoco elige A, tratar el backlog DS como prioridad de facto.
8. **Próximo candidato #1: LW-6** (short-circuit de escalación sobre cobertura cero) — defecto real de eficiencia hallado en vivo. LW-4 y P5 siguen oliendo a barato-dormido; evaluar valor antes de invertir.
