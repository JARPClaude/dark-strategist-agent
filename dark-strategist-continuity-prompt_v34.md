# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 13/06/2026 (sesión 35 — DS v3.21.0 LW-6 escalation short-circuit on zero agent coverage, shipped & JARP_CERTIFIED) | **Para:** Sesión 36
**Reemplaza:** v33 del 13/06/2026 (sesión 34)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v34.md`
**⚠️ BORRAR en este cierre:** v33 (`git rm` en el commit de cierre). v34 = único continuity vigente. Subir v34 al PROYECTO claude.ai + quitar v33.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 35 (resumen ejecutivo)

Track elegido: **B — Backlog valor-agregado → LW-6** (escalation short-circuit sobre cobertura cero, candidato #1). Trading (A) NO se eligió (**32ª sesión postergada, 4–35**). Recordatorio una vez, sin re-confrontar.

**Resultado: DS v3.21.0 shipped y CERTIFICADO** (`PA-20260613-004`).

### 0. DISCREPANCIA HIGIÉNICA CORREGIDA (detectada en PHASE 0 de s35)
PHASE 0 verificó `_livewatch` **por contenido del árbol remoto** (no por mensaje de commit) y halló que `orchestrator/_livewatch/lw2_contract.txt` (fixture s33, 1961 B) **seguía trackeado** en el repo público, pese a que el `.gitignore` contiene `_livewatch/` y el chore s34 (`8943efe`) decía haberlo destrackeado. Causa: el `.gitignore` NO destrackea archivos ya commiteados, y el `git rm --cached` del chore usó una ruta raíz que no alcanzó `orchestrator/_livewatch/`. Corregido en s35: `git rm -r --cached orchestrator/_livewatch` (commit chore `857c6c7`, parent del cert s35). Cert no afectado (fixture = NOT certified surface). **Lección dura:** verificar `_livewatch` por **read-back del árbol** (`get_file_contents orchestrator/_livewatch` → 404 / `git ls-files` vacío), NUNCA por el mensaje del commit de untrack — mismo anti-patrón que Select-String (s33/s34). Mi reporte inicial de PHASE 0 confirmó "_livewatch no trackeado" por el commit; era falso-positivo, corregido por contenido.

### 1. DS v3.21.0 — LW-6 ESCALATION SHORT-CIRCUIT ON ZERO AGENT COVERAGE (NON-BINDING)
En un colapso 100% del tribunal (todos los agentes erroran → `agents_consulted==0` vía LW-5), la confianza es LOW (correcto) pero `should_escalate` disparaba una ronda de escalación contra el MISMO backend caído — acotada (`rounds<max_rounds` + caps) pero inútil (los `FOR-ESC-*` erroran igual). Observado en vivo en s34 (DS-36E093BE escaló 1 ronda).

**Fix (en `schema.py` + `tribunal_transversal.py`):**
- `should_escalate(..., agent_coverage=None)`: nuevo gate `if agent_coverage is not None and agent_coverage <= 0: return False`. **Discriminador = COBERTURA==0, NO confidence y NO umbral `<2`** — cobertura 1 (un agente sano con hallazgo sin corroborar) DEBE seguir escalando para buscar un 2º agente corroborante (intención v3.12.0). `agent_coverage=None` = cobertura desconocida → sin gate (backward-compat).
- `_maybe_escalate`: pasa `agent_coverage=unified.agents_consulted` al gate; el bloque `reason` distingue colapso-cobertura-cero (`"zero agent coverage -- escalation cannot help (tribunal collapse)"`) de disabled/no-budget → transparencia honesta de POR QUÉ no escaló.
- **Veredicto INTACTO:** `final_verdict`, `Finding`, `compute_confidence`, `_apply_confidence` SIN tocar. Determinista, NON-BINDING.
- **`test_escalation.py`** 10→**14**: las 10 tuplas 5-arg legacy intactas (default `None` → sin gate, backward-compat); +4 cobertura: `0`→False (el caso LW-6), `1`→True (escalate-to-corroborate preservado), `2`→True, `None`→True.

### 2. RE-CERT DS v3.21.0 — COMPLETA ✅ (CONFIRMATORY)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260613-003`) PASS. 7-ejes Level 1 JARP DEEP sobre delta v3.20.0→v3.21.0.
- **Por qué CONFIRMATORY:** el fix vive 100% en el gate de escalación (`should_escalate`) + el reason de su caller. Superficie forense (19 variants + 7 skills + base + router CONTENT) byte-idéntica salvo stamps. Veredicto intacto. NON-BINDING.
- **Evidencia (máquina real, post-apply + post-bump):** `test_escalation` **14/14** + `test_apply_confidence` **24/24** + `test_confidence` 10/10 + **LIVE collapse e2e**:
  - **`DS-66E01BF0`, $0 (0/40 calls):** backend muerto (`ANTHROPIC_BASE_URL=http://localhost:9999` + dummy key) → 10 agentes (5 ROL + 5 FOR) `Connection error` → fallback; tribunal (0 agents), 0 findings → **`Confidence: LOW`** → **`Escalation: NO | rounds: 0 | reason "zero agent coverage -- escalation cannot help (tribunal collapse)"`** (el delta LW-6; baseline s34 DS-36E093BE escaló 1 ronda). Veredicto `SOLID UNDER PRESSURE` (fallback determinista).
  - **Patrón reutilizable:** paths de fallo en vivo = puerto muerto 9999 → $0 (agentes fallan antes de llamar).
- **CERT EMITIDO:** `PA-20260613-004` — DS **v3.21.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **13/09/2026 o v4.0.0**. **SUPERSEDES PA-20260613-002** (v3.20.0).
- **Bump:** `bump_lw6_v3_21_0.py` (banners operator-visible: main×2 / wizard / tribunal_transversal + CHANGELOG `[3.21.0]`; **NO config knob** — LW-6 reusa `agents_consulted`) + `bump_stamps.ps1 -OldVersion 3.20.0 -NewVersion 3.21.0 -Apply` (23 files / 69 stamps). Ambos EOL-aware, all-or-nothing, dry-run→apply. One-shots BORRADOS antes del commit.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.21.0 = CERTIFICADO (`PA-20260613-004`).** Sin version-gap. PA-20260613-002 (v3.20.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s35)
1. Archivos en disco (PHASE 3/4): `orchestrator/schema.py` (`should_escalate` + `agent_coverage` gate + docstring LW-6), `orchestrator/tribunal_transversal.py` (caller pasa `agent_coverage` + reason honesto + banner v3.21.0), `orchestrator/test_escalation.py` (10→14), banners (`main.py`×2 / `wizard.py`), product-face stamps (23 files), `CHANGELOG.md` (bloque `[3.21.0]` + cert `PA-20260613-004`).
2. Canónicos vía one-shot anclado `sync_canonicals_v3_21_0.py` (NO Ruta-3 manual): `.claude-init.md` (header + Note #7 + SUPERSEDED list) + `JARP_TOOLKIT.md` (header + #30 Version + CERT STATUS + supersede-tail + Previous-certs prepend + Note #16 ×2) → v3.21.0/PA-20260613-004. Replace-de-anchor-único in-place (sin huérfana). **AMBOS canónicos concuerdan (verificado posicionalmente).**
3. **EOL per-file confirmado:** `.claude-init.md`=**LF**; `JARP_TOOLKIT.md`=**CRLF**; `.py`=**CRLF EXCEPTO** `test_escalation.py`=**LF** (descubierto en s35 — el descarte "asumir .py=CRLF" se valida; detectar per-file SIEMPRE). El one-shot detectó cada uno.
4. One-shots BORRADOS antes de los commits: `apply_lw6_fix.py`, `bump_lw6_v3_21_0.py`, `finalize_cert_v3_21_0.py` (DS), `sync_canonicals_v3_21_0.py` (raíz DS, edita jarp-toolkit por ruta absoluta).
5. `git rm dark-strategist-continuity-prompt_v33.md`. v34 = único continuity.
6. **Commits de cierre** (registrar SHAs tras push vía GitHub Desktop): DS cert commit (parent `857c6c7` = chore untrack `_livewatch`) + jarp-toolkit sync commit (parent `6abf331` = sync s34).
7. **`_livewatch/`** gitignorado y AHORA realmente destrackeado (s35). El fixture `lw5_collapse.txt` (s34) sigue local-only. Sanity de untracked ANTES de pushear.

---

## DEUDA TÉCNICA — POST-SESIÓN 35

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.21.0** | ✅ CERRADA | v3.21.0 CERTIFICADO (PA-20260613-004) | 0/0/0/0, CONFIRMATORY. |
| **LW-6 escalation short-circuit** | ✅ CERRADA | should_escalate corta si agent_coverage==0 | test 14/14; live DS-66E01BF0 Escalation NO/0 rounds $0. NON-BINDING. |
| **`_livewatch` leak (s33→s35)** | ✅ CERRADA (s35) | `lw2_contract.txt` destrackeado (`git rm -r --cached orchestrator/_livewatch`) | Verificar por read-back del árbol, no por commit msg. |
| **LW-5 / LW-2 / LW-3 / LW-1** | ✅ CERRADAS (s34/s33/s32/s31) | confidence-collapse floor / corroboration / provenance granularity / domain resolver | Sin cambio. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟢 LW-4 (refinamiento opcional/DESCARTABLE):** desempate de dominio posicional ("primer token de dominio del filename"). LW-1 ya cerró el defecto; pulido de intuición. Evaluar valor antes de invertir — fuerte candidato a descartar.
- **P5 extensión P14/P20** (candidato): reputational-risk a Public Sector (P14) + Startup (P20). Valor incremental dudoso.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real. **Nota s35:** el backlog LW se está agotando (LW-1/2/3/5/6 cerrados; solo LW-4 descartable). Para s36+, considerar fuentes nuevas de valor real (no rellenar con LW-4/P5 si no aportan) — o re-evaluar prioridad de facto vs trading.

---

## ESTADO ACTUAL VERIFICADO (13/06/2026 — fin s35)

### Repo dark-strategist-agent
- **v3.21.0 — CERTIFICADO (`PA-20260613-004`)**. Default `claude-opus-4-7`. Commit de cierre = cert commit s35 (**registrar SHA tras push**; parent `857c6c7`).
- **MODIFICADO:** `orchestrator/schema.py` (`should_escalate` + `agent_coverage` gate); `orchestrator/tribunal_transversal.py` (caller + reason honesto + banner v3.21.0); `orchestrator/test_escalation.py` (14 casos); `orchestrator/{main,wizard}.py` (banners); 23 product-face stamps; `CHANGELOG.md`; `dark-strategist-continuity-prompt_v34.md`. **git rm:** v33.
- **De s34 vigente:** `_apply_confidence` LW-5 (`agents_consulted` cuenta solo contribuyentes sin `"error"`); `test_apply_confidence.py` (24 checks). De s33: corroboración por overlap title+evidence same-sev + floor exacto legacy; `config.example.json` `corroboration_min_overlap:4`.
- **De s32/s31/s30 vigente:** `txt_atomic_lines` per-canal + `test_signals_granularity`; `_resolve_domain` boundary-aware + most-specific-first + order-invariant + `test_domain_resolver`; `skills/reputational-risk/` + `test_reputational_risk`.
- **De s29–s25 vigente:** `overlap_score` + provenance post-veredicto + `test_provenance`; canal `--signals` + `test_signals`; `archetype_lenses.py` + `test_archetype_lenses`; `schema.should_escalate`/`compute_confidence` + `test_escalation`/`test_confidence`.
- `tools/bump_stamps.ps1` (cubre prompts/*.md + README + CLAUDE = 23 files / 69 stamps; NO orchestrator/*.py ni CHANGELOG ni config; **dry-run por defecto — requiere `-Apply`**; params NOMBRADOS). `gc.auto 0` activo. `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus`/`--signals` activos.
- **7 skills**, **9 sub-agentes N2 permanentes**, **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` + `_livewatch/` GITIGNORADOS (local-only). `_livewatch/lw5_collapse.txt` = fixture throwaway s34 (local).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s35. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/CERT STATUS/supersede-tail/Previous certs) + #16 + `.claude-init.md` header + #7 → v3.21.0/PA-20260613-004. PRIVADO. HEAD = sync commit s35 (**registrar SHA tras push**; parent `6abf331`). **AMBOS canónicos concuerdan (verificado posicionalmente).** `.claude-init.md`=LF, `JARP_TOOLKIT.md`=CRLF.

### free-claude-code
- Proxy $0 para no-cert. **`fcc-server` NO en PATH ni levantado — instalar/arrancar antes de usar** (Python 3.14+, `uv`, `fcc-server`, Admin UI `/admin`). SDK exige `api_key` no vacío aunque uses proxy → dummy + `ANTHROPIC_BASE_URL`. **Cert = Opus real (sk-ant, sin proxy).** **Para ejercer paths de FALLO en vivo: apuntar a puerto muerto (`http://localhost:9999`) → $0** (agentes erroran antes de llamar; no consume Opus; no requiere fcc-server levantado).

---

## PROTOCOLO DE INICIO PARA SESIÓN 36
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v34).
2. **PHASE 0 — Verificación:**
   - v33 borrado, v34 único continuity.
   - Repo en v3.21.0. **Cert: DS v3.21.0 `PA-20260613-004` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260613-002` SUPERSEDED.
   - **Verificar AMBOS canónicos concuerdan POSICIONALMENTE** (toolkit #30 Version + CERT STATUS + nota #16 + init #7 en v3.21.0/PA-20260613-004) — lección drift s33/s34. NO confiar en Select-String a secas.
   - **`orchestrator/_livewatch` NO trackeado — verificar por READ-BACK DEL ÁRBOL** (`get_file_contents orchestrator/_livewatch` → 404, o `git ls-files orchestrator/_livewatch` vacío), NUNCA por mensaje de commit (lección s35). Si reaparece: `git rm -r --cached orchestrator/_livewatch`.
   - Confirmar HEAD remoto vía `list_commits` (perPage=3): DS = cert commit s35; jarp-toolkit = sync commit s35.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 32 SESIONES (4–35).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s36 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — agotándose: solo **LW-4 (opcional/DESCARTABLE)** + **P5 ext P14/P20 (dudoso)**. Si ninguno aporta valor real, NO rellenar — buscar fuente nueva de valor o reconsiderar prioridad.
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes+comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG ni config → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE | RAG = MECANISMO | ContextBuilder document-free | infinity/Docker RECHAZADO | **leer el módulo real antes de incorporar/diseñar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case | Floor R2/señales/provenance/corroboración = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25–s34:** Confianza/escalación/lentes/señales/provenance/corroboración = metadata NO-VINCULANTE, determinista, post-hoc; NUNCA tocan `final_verdict`/`Finding`/`compute_confidence`. Docstrings de módulo congelados. Scripts de edición newline-aware + encadenados por archivo + all-or-nothing + dry-run. Riesgo reputacional = SKILL markdown (#7); Failure Catalog VINCULA severidad; activación⊆binding. Domain routing = boundary-aware + MOST-SPECIFIC-FIRST + ORDER-INVARIANT. Segmentación `.txt` per-canal (`txt_atomic_lines`). Provenance/corroboración POST-veredicto. Leer de vuelta lo que UNO entregó. `bump_stamps.ps1` dry-run por defecto → SIEMPRE `-Apply`. Corroboración = OVERLAP sobre `title+evidence` same-sev + floor exacto legacy. NO propagar source-agent por finding. Validar la propia heurística contra su peor modo de falla. **LW-5 (s34):** `agents_consulted` cuenta SOLO contribuyentes (`isinstance(o,dict) and "error" not in o`); colapso 100% → LOW; el discriminador es COBERTURA (clave `"error"`), NO el conteo de findings; NO colapsar todo "0 findings" a LOW (rompe el HIGH limpio-legítimo). Verificación canónica POSICIONAL, no Select-String. EOL per-file real. Live e2e de FALLO = puerto muerto 9999 → $0. Canónicos vía one-shot anclado, NO Ruta-3 manual.

**De s35 (nuevas):**
- **LW-6 / escalation short-circuit on zero coverage:** `should_escalate(..., agent_coverage=None)` corta a False si `agent_coverage is not None and agent_coverage <= 0`. **El discriminador es COBERTURA==0, NO confidence y NO un umbral `<2`** — cobertura 1 DEBE seguir escalando para corroborar (intención v3.12.0). `_maybe_escalate` pasa `unified.agents_consulted` y emite reason honesto de cobertura-cero. NON-BINDING; `final_verdict`/`Finding`/`compute_confidence`/`_apply_confidence` intactos.
- **Verificar `_livewatch` (y cualquier untrack) por READ-BACK DEL ÁRBOL, no por mensaje de commit:** el `.gitignore` no destrackea lo ya commiteado; un `git rm --cached` con ruta equivocada deja el archivo trackeado aunque el mensaje diga lo contrario. El árbol manda (mismo principio que Select-String: el grep/mensaje confirma intención, no resultado).
- **EOL NO es uniforme ni dentro de `.py`:** `test_escalation.py`=LF mientras `schema.py`/`tribunal_transversal.py`/`main.py`/`wizard.py`=CRLF. Detectar per-file SIEMPRE; el descarte "asumir .py=CRLF" se reconfirma.
- **One-shot con rutas absolutas para editar otro repo:** `sync_canonicals_v3_21_0.py` vivió en la raíz DS pero editó jarp-toolkit por ruta absoluta → se borra como throwaway DS, nunca entra a jarp-toolkit.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance/corroboración como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica | bumpear docstrings/catálogo/comments-feature-landing congelados | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts que escriben cada edit desde el snapshot original | activación dormida sobre activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` | riesgo reputacional como lente-arquetipo (usar SKILL) | duplicar Failure-Catalog rows | activar skill en dominios sin Failure Catalog rows | transcribir líneas largas como anclas (usar line-based / re-leer) | domain routing por substring crudo / acoplado al orden | borrar claves cortas del DOMAIN_MAP | correr `bump_stamps.ps1` sin `-Apply` | corroborar confianza por TÍTULO SOLO | propagar source-agent por finding | colapsar todo "0 findings" a LOW (el discriminador de cobertura es la clave `"error"`, NO el conteo de findings — s34) | verificar campos canónicos por Select-String a secas (usar re-lectura/replace-de-anchor-único in-place — s34) | Ruta-3 manual para canónicos con riesgo de mis-paste (usar one-shot anclado — s34) | asumir EOL uniforme (.claude-init=LF, JARP_TOOLKIT=CRLF, .py=CRLF EXCEPTO test_escalation.py=LF; detectar per-file — s34/s35) | **gatear escalación por `<2` o por confidence en vez de COBERTURA==0 (rompe escalate-to-corroborate en cobertura 1) — s35** | **verificar `_livewatch`/untrack por mensaje de commit en vez de read-back del árbol (el .gitignore no destrackea lo ya commiteado) — s35**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v34.md` (v33 borrado s35)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan POSICIONALMENTE al cierre.** init=LF, toolkit=CRLF.
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. `github:list_commits` (perPage=3) + `get_file_contents` para verificación remota; `get_file_contents` sobre dir = listar (404 si no existe = read-back de borrado).
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. env var = `$env:VAR="..."`; limpiar con `Remove-Item Env:\VAR`. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). `bump_stamps.ps1` con params NOMBRADOS + **`-Apply`**.
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1 -Apply`. Banners orchestrator + CHANGELOG = script Python anclado all-or-nothing + EOL-AWARE per-file (dry-run → --apply), a la RAÍZ. Edits código pequeños/archivo nuevo = mi-filesystem directo (full-overwrite; verificar read-back). Canónicos (archivos grandes) = **one-shot anclado** (replace de anchor único in-place, rutas absolutas; preferido sobre Ruta-3 manual). `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Higiene de fixtures/one-shots:** throwaways (`_livewatch/`, smoke) en `.gitignore` ANTES de cualquier commit; one-shots BORRADOS antes del commit de cert; sanity de untracked en GitHub Desktop antes de pushear; **verificar `_livewatch` destrackeado por read-back del árbol**.
- **Escalación (`should_escalate`):** gate determinista; corta a False si `agent_coverage<=0` (cobertura cero); NON-BINDING. **Confidence (`_apply_confidence`):** corroboración overlap title+evidence same-sev + floor legacy; `agents_consulted` solo contribuyentes. `compute_confidence`/`final_verdict` intactos.
- **Live e2e:** sano = Opus real (cert) o free proxy (no-cert). **Fallo/colapso = backend muerto puerto 9999 → $0.**
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → 13 PASS / 0 FAIL con key+proxy, o 12 PASS / 1 SKIP offline. Tests s35: `test_escalation` 14/0; `test_apply_confidence` 24/0. `pip install rank_bm25 pydantic` antes.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 35
**Repo dark-strategist-agent — commit de cierre (cert):**
```
fix: DS v3.21.0 — escalation short-circuit on zero agent coverage LW-6 (should_escalate gains agent_coverage gate; a 100% tribunal collapse agents_consulted==0 no longer escalates into the same failed path — short-circuits to False, COVERAGE==0 discriminator preserves escalate-to-corroborate at coverage 1; _maybe_escalate honest zero-coverage reason; NON-BINDING, verdict path untouched) — test_escalation 14/14 + live collapse e2e DS-66E01BF0 Escalation NO/0 rounds $0 + JARP_CERTIFIED PA-20260613-004
```
Incluye: `orchestrator/schema.py`, `orchestrator/tribunal_transversal.py`, `orchestrator/test_escalation.py`, `orchestrator/{main,wizard}.py` (banners), product-face stamps (23), `CHANGELOG.md`, `dark-strategist-continuity-prompt_v34.md`; `git rm dark-strategist-continuity-prompt_v33.md`. NO incluye one-shots (borrados). `_livewatch/` gitignorado + destrackeado.
**Repo jarp-toolkit — sync:**
```
docs: sync DS v3.21.0 / PA-20260613-004 (LW-6 escalation short-circuit on zero agent coverage) — header + entry #30 (Version/CERT STATUS/supersede-tail/Previous certs) + note #16 + .claude-init header + #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 35

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.21.0** | **PA-20260613-004** | **v3.21.0** | ✅ ACTIVE | 13/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260613-002 (v3.20.0), PA-20260612-002 (v3.19.0), PA-20260611-002 (v3.18.0), PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 35 (auto-mejora del próximo Claude)

1. **PHASE 0 atrapó un leak real por verificación de CONTENIDO.** `orchestrator/_livewatch/lw2_contract.txt` seguía trackeado pese al `.gitignore` y al chore s34 que decía haberlo quitado. Mi reporte inicial lo dio por destrackeado confiando en el mensaje del commit — falso-positivo, mismo anti-patrón que Select-String. El árbol (no el mensaje) manda. Verificar untrack por `git ls-files`/`get_file_contents`→404.
2. **LW-6: el discriminador correcto era COBERTURA, no confidence ni `<2`.** Cobertura 0 (colapso) = escalación fútil → cortar; cobertura 1 (baja corroboración con agente sano) = escalar para corroborar (intención v3.12.0). Gatear por `<2` habría roto el caso legítimo. Leer `should_escalate` + `_maybe_escalate` reales reveló dónde inyectar el gate sin tocar `compute_confidence`.
3. **Offline prueba la corrección; live prueba que el path se ejerce.** Los 14 checks prueban `should_escalate`; el live (DS-66E01BF0, puerto muerto, $0) ejerció el short-circuit end-to-end: `Escalation: NO | rounds 0 | reason zero agent coverage`, vs baseline s34 que escaló 1 ronda.
4. **EOL no es uniforme ni entre `.py`:** `test_escalation.py`=LF, el resto CRLF. El one-shot EOL-aware per-file lo manejó. Nunca asumir.
5. **Canónicos vía one-shot anclado con rutas absolutas** (vivió en raíz DS, editó jarp-toolkit). Replace-de-anchor-único in-place → sin huérfana (la falla s33 fue mis-paste manual).
6. **TRADING: 32 SESIONES POSTERGADO (4–35). NO re-confrontar.** Si s36 tampoco elige A, tratar el backlog DS como prioridad de facto — pero el backlog LW se agota (solo LW-4 descartable + P5 dudoso). Para valor real futuro, buscar fuente nueva, no rellenar con cheap-dormido.
7. **El backlog de alto valor casi se agotó.** LW-1/2/3/5/6 cerrados. s36 debería evaluar honestamente si LW-4/P5 aportan o si conviene una fuente nueva de valor (o re-discutir prioridades con JARP).
