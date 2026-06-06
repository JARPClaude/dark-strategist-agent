# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 05/06/2026 (sesión 27 — DS v3.13.0 lentes-arquetipo P2, shipped & JARP_CERTIFIED) | **Para:** Sesión 28
**Reemplaza:** v25 del 04/06/2026 (sesión 26)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v26.md`
**⚠️ BORRAR en este cierre:** v25 (`git rm` en el commit de cierre). v26 = único continuity vigente. Subir v26 al PROYECTO claude.ai + quitar v25.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 27 (resumen ejecutivo)

Track elegido: **P2 — lentes-arquetipo** (siguiente lógico del backlog; enriquece la ronda de escalamiento P1 de s26). Trading (A) NO se eligió (**24ª sesión postergada, 4–27**).

**Resultado: DS v3.13.0 shipped y CERTIFICADO** (`PA-20260605-002`).

### 1. (P2) DS v3.13.0 — lentes-arquetipo en la ronda de escalamiento, NO-VINCULANTE
- **`orchestrator/archetype_lenses.py`** (NUEVO) — catálogo congelado de **5 lentes abstractas** (`FALSIFIER`, `FAILURE_MODE_HUNTER`, `EVIDENCE_AUDITOR`, `INCENTIVE_AUDITOR`, `SYSTEMIC_LENS`) + helpers puros `select_lenses(n)` (determinista, devuelve **copias** de dict → no corrompe el catálogo) y `build_lens_directive(lens, round_no, focus)`. Sin API, sin I/O, full testeable. **Roles ABSTRACTOS — jamás impersonación de personas reales** (autoridad fabricada, descartado).
- **`orchestrator/tribunal_transversal.py`** — `_run_escalation_round` ahora asigna **una lente por agente `FOR-ESC-*`** (orden determinista; el par complementario inicial — refute-first + extend-first — corre bajo `max_escalation_agents=2`). La lente moldea *cómo* re-examina los hallazgos que mueven el veredicto. ids `FOR-ESC-*` intactos (corroboración los cuenta independientes). `result["lens"]` etiquetado; `_maybe_escalate` registra `esc["lenses"]`; transparency report los muestra. `build_lens_directive(None,…)` → directiva neutral si hay más agentes que lentes → offline nunca crashea.
- Catálogo + docstring de módulo **content-based/congelados** (no bumpean cada minor).
- **`orchestrator/test_archetype_lenses.py`** (NUEVO, commiteado) — 10 checks offline, $0 (integridad de catálogo, contrato de orden, cap/degenerados/coerción/determinismo/aislamiento de `select_lenses`, embedding + degradación de `build_lens_directive`).

**GARANTÍA INVIOLABLE verificada:** las lentes cambian **calidad de deliberación**, NUNCA el veredicto. `final_verdict` sigue severidad pura (FATAL→INVIABLE). Los paths no-op del gate siguen sin invocar `_synthesize`/`_run_escalation_round`. La escalación sigue siendo decisión de presupuesto de deliberación.

### 2. DECISIONES CLAVE (s27)
- **Lentes = enriquecimiento NO-VINCULANTE de la ronda de escalamiento.** Solo moldean la directiva del agente `FOR-ESC-*`; no tocan el veredicto ni el schema `Finding`.
- **Opción 1 confirmada (acotada):** reusa la capa Forense existente, **sin tipo de agente nuevo**. Las lentes se enchufan vía `build_forense_prompt(directive=…)`.
- **Orden del catálogo es significativo:** las 2 primeras (FALSIFIER + FAILURE_MODE_HUNTER) son el par de mayor valor porque `max_escalation_agents` default = 2.
- **Edición vía Ruta 3** (script anclado all-or-nothing + newline-aware, entregado a la RAÍZ): `apply_p2_lenses.py` aplicó las 4 anclas (import + `_run_escalation_round` + esc-dict + línea transparency). Archivos nuevos vía mi-filesystem directo.

### 3. RE-CERT DS v3.13.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260605-001`) PASS (PA-agent sin cambios). Auditoría 7-ejes Level 1 JARP DEEP sobre delta v3.12.0.
- **Evidencia funcional (máquina real, post-apply):** `test_archetype_lenses.py` **10/10** + `test_escalation.py` **10/10** + `test_confidence.py` **10/10** + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (`b_unified_output` SKIP = ANTHROPIC_API_KEY/DNS, no-bloqueante), `c_fallback_intact` + `e_monotonic_verdict` PASS. El pipeline importa `tribunal`→`archetype_lenses` limpio.
- **CERT EMITIDO:** `PA-20260605-002` — DS **v3.13.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **05/09/2026 o v4.0.0**. **SUPERSEDES PA-20260604-004** (v3.12.0). Sin cascade (minor).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.13.0 = CERTIFICADO (`PA-20260605-002`).** Sin version-gap. PA-20260604-004 (v3.12.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s27) ✅
1. P2 archivos nuevos: `orchestrator/archetype_lenses.py` + `orchestrator/test_archetype_lenses.py` (mi-filesystem).
2. P2 código: `apply_p2_lenses.py --apply` → 4 anclas en `tribunal_transversal.py`. Regresión verde.
3. Bump anclado: `bump_stamps.ps1 3.12.0 3.13.0 -Apply` → stamps prompts(21)+README+CLAUDE (anchors PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/-ROUTER/Version:/VERSION). NO toca CHANGELOG ni orchestrator/*.py.
4. Bump manual: `bump_manual_v3_13_0.py --apply` → CHANGELOG `[3.13.0]` + cert block + 4 banners orchestrator (main×2, wizard, transparency) + CLAUDE (status bottom + fila roadmap + árbol) + README (fila roadmap). Disjunto de bump_stamps (sin conflicto de orden).
5. `jarp-toolkit` + `.claude-init.md`: `sync_toolkit_v3_13_0.py --apply` → header + #16 + #30 + init #7 → v3.13.0/PA-002.
6. Continuity v26 commiteado; `git rm` v25.
7. **One-shots BORRADOS** (no commiteados): `apply_p2_lenses.py`, `bump_manual_v3_13_0.py` (DS), `sync_toolkit_v3_13_0.py` (toolkit). **`del` de PowerShell usa COMAS** (`del a.py, b.py`).

---

## DEUDA TÉCNICA — POST-SESIÓN 27

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.13.0** | ✅ CERRADA | v3.13.0 CERTIFICADO (PA-20260605-002) | 0/0/0/0. |
| **P2 lentes-arquetipo** | ✅ CERRADA | Lentes en la ronda de escalamiento shipped | Abstractas, no-vinculantes, sin agente nuevo; test_archetype_lenses.py. |
| **clash n>0 live + gate b live** | 🟢 WATCH | `b_unified_output` SKIP | DNS/key ambiental (`getaddrinfo failed` / ANTHROPIC_API_KEY). No-bloqueante. La escalación+lentes live tampoco se ejercitan offline (degradan con gracia). |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO (del análisis forense s25) — pendiente
- **P4 — señales externas vía BYO/RAG existente (SIGUIENTE).** `--corpus`; sin infra nueva. Aprovecha el retriever BM25 (R2) ya presente.
- **P5 — lente de riesgo reputacional** (posible skill #7). Nota: P5 podría modelarse como una lente-arquetipo adicional (`REPUTATIONAL_LENS`) en `archetype_lenses.py` — evaluar reuso vs skill.
- **Caso-test dorado INVIABLE:** "consenso 95% → eficiencia 95%" (causalidad inventada). Fixture LOW para validar P1/P2 end-to-end con escalación+lentes (la lente `EVIDENCE_AUDITOR` está diseñada para matar exactamente este patrón).

---

## ESTADO ACTUAL VERIFICADO (05/06/2026 — fin s27)

### Repo dark-strategist-agent
- **v3.13.0 — CERTIFICADO (`PA-20260605-002`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.13.0 (registrar SHA tras push).
- **NEW:** `archetype_lenses.py` (5 lentes + `select_lenses`/`build_lens_directive`) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26 vigente:** `schema.should_escalate` + `tribunal._maybe_escalate`/`_run_escalation_round` (ahora con lentes) + config keys + `test_escalation.py`.
- **De s25 vigente:** `schema.compute_confidence` + `tribunal._apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (anchors PROTOCOL_STATUS/BASE_PROTOCOL/CATALOG_VERSION/-ROUTER/Version:/VERSION; scope prompts+README+CLAUDE; NO CHANGELOG ni orchestrator/*.py). `gc.auto 0` activo.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` activo.
- **6 skills**, **9 sub-agentes N2 permanentes** (sin cambio). **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s27. Sin cambios.

### Repo jarp-toolkit
- header + #16 + #30 + `.claude-init.md` #7 → v3.13.0/PA-002. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 28
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v26).
2. **PHASE 0 — Verificación:**
   - v25 borrado, v26 único continuity.
   - Repo en v3.13.0. **Cert registry: DS v3.13.0 `PA-20260605-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260604-004` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados.
   - `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 24 SESIONES (4–27).** Prioridad #1 en userPreferences. **NO re-confrontar.**
   - **(B) Backlog valor-agregado** — **P4 (señales externas vía BYO) es el siguiente lógico.** Luego P5 (riesgo reputacional, posible lente o skill). Caso-test dorado disponible.
   - **(C) WATCH live-key/DNS** — no-bloqueante (ambiental).
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo + catálogo de lentes = content-based/congelados, p.ej. catalogs.py @3.2.0) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | 4 variance decompositions | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE, NO driver | RAG = MECANISMO, NO driver | ContextBuilder document-free | infinity/Docker RECHAZADO | fallback byte-idéntico ante cambio de feed | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2 = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25:** Confianza = metadata NO-VINCULANTE, determinista, ambos caminos (`compute_confidence` nunca toca `final_verdict`). `multi_agent_confirmed` + `agents_consulted` derivados determinísticamente. Docstrings de módulo congelados.

**De s26:** Gate de escalamiento (`should_escalate`) = NO-VINCULANTE, determinista (solo decide gastar deliberación). Ronda acotada, ids `FOR-ESC-*` distintos, cap por config, budget-gated, degrada offline. Reusa capa Forense (Opción 1), sin agente nuevo. Scripts de edición DEBEN ser newline-aware (`\r\n` vs `\n`; `config.example.json` está en CRLF, .py/.md en LF).

**De s27 (nuevas):**
- **Lentes-arquetipo (`archetype_lenses.py`) = enriquecimiento NO-VINCULANTE de la ronda de escalamiento.** Moldean *cómo* el agente `FOR-ESC-*` re-examina; jamás tocan el veredicto ni el schema `Finding`.
- **Roles ABSTRACTOS obligatorio — NUNCA impersonar personas reales** (autoridad fabricada). El catálogo es la frontera ética.
- **Catálogo de lentes content-based/congelado** (no bumpea cada minor; igual que docstrings de módulo).
- **`bump_stamps.ps1` y el bump manual son DISJUNTOS** → order-independent. bump_stamps = stamps con anchor (PROTOCOL_STATUS/BASE_PROTOCOL/Version:/VERSION/-ROUTER/CATALOG_VERSION) en prompts+README+CLAUDE. Manual = CHANGELOG + banners orchestrator + CLAUDE bottom-status/roadmap/árbol + README roadmap (líneas SIN anchor de stamp). Verificado leyendo `bump_stamps.ps1`.
- **`-like` de PowerShell es case-insensitive** → el anchor `VERSION` captura `version-3.12.0` del badge README. Tenerlo en cuenta para no doblar manualmente lo que ya hace bump_stamps.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | skills knowledge-work descartadas | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor R2 por score BM25 | **confianza como driver del veredicto (es metadata) — s25** | **impersonar personas reales en lentes-arquetipo — s25/s27 (reafirmado: el catálogo es 100% roles abstractos)** | **"consenso → eficiencia" como métrica válida (caso-test INVIABLE) — s25** | **bumpear docstrings de módulo congelados / catálogo de lentes cada minor — s25/s27** | **escalación/lentes como input del veredicto (es decisión de presupuesto/calidad de deliberación) — s26/s27** | **re-usar ids `FOR-*` en la ronda de escalamiento (rompe corroboración; usar `FOR-ESC-*`) — s26** | **anchors de edición con `\n` literal en archivos CRLF — s26** | **doblar manualmente stamps que `bump_stamps.ps1` ya cubre vía anchor — s27**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v26.md` (v25 borrado s27)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (comandos por separado o `;`). `del` de varios archivos usa **COMAS** (`del a, b`). `cd` antes de correr scripts (bump manual desde RAÍZ; tests desde `orchestrator/`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1`. Edits prosa/código/banner multi-archivo = **script Python anclado all-or-nothing + NEWLINE-AWARE per-file** (dry-run → --apply), **a la RAÍZ del repo**. Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Confianza + escalación + lentes runtime:** `confidence` determinista (P3); `_maybe_escalate` re-delibera si LOW+budget (P1); `_run_escalation_round` asigna una lente abstracta por `FOR-ESC-*` (P2). Todos NO-VINCULANTES, etiquetados en el transparency report.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. `python test_archetype_lenses.py` → **0 FAIL / 10**. `python test_escalation.py` → **0 FAIL / 10**. `python test_confidence.py` → **0 FAIL / 10**. `pip install rank_bm25 pydantic` antes.
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 27
**Repo dark-strategist-agent (v3.13.0 cert) — commit atómico:**
```
feat: DS v3.13.0 — archetype lenses for the escalation round (abstract, NON-BINDING) + JARP_CERTIFIED PA-20260605-002
```
Incluye: `orchestrator/{archetype_lenses,tribunal_transversal,test_archetype_lenses}.py`, 21 prompts (stamps), README, CLAUDE, CHANGELOG, `orchestrator/{main,wizard}.py` (banners), `dark-strategist-continuity-prompt_v26.md`; `git rm dark-strategist-continuity-prompt_v25.md`. NO incluye los one-shots.
**Repo jarp-toolkit:**
```
docs: sync DS v3.13.0 / PA-20260605-002 (archetype lenses) — header + #16 + #30 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 27

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.13.0** | **PA-20260605-002** | **v3.13.0** | ✅ ACTIVE | 05/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 27 (auto-mejora del próximo Claude)

1. **Lee el módulo real ANTES de implementar.** Confirmé `_run_escalation_round` contra el código antes de enchufar las lentes; la directiva entra como el arg `rol_simulation` de `build_forense_prompt`. No asumas la firma.
2. **`bump_stamps.ps1` lee con `ReadAllLines` y escribe con `WriteAllLines` (UTF8 sin BOM) → puede normalizar a CRLF en Windows.** Por eso el bump manual que corre después debe ser **newline-aware per-file** (CLAUDE/README pueden quedar CRLF; CHANGELOG/orchestrator quedan LF). Verificado: manual y bump_stamps son disjuntos → orden indiferente.
3. **`-like` de PowerShell es case-insensitive.** El anchor `VERSION` de bump_stamps captura `version-3.12.0` del badge README. No dupliques ese stamp en el manual.
4. **Banners product-face orchestrator = 4:** `main.py` ×2 (`description=` argparse + `print` header), `wizard.py` ×1 (`run_wizard` header), `tribunal_transversal.py` ×1 (transparency report). Los docstrings de tope (main 3.10.0, wizard 3.10.0, tribunal 3.0.0) son **frozen — NO tocar**. Los marcadores históricos (`P1 (v3.12.0)`, `v3.11.0 --`) **NO tocar**.
5. **CLAUDE/README tienen DOS tablas roadmap** que el bump manual debe ampliar con la fila nueva (no las toca bump_stamps). Histórico de findings D-v39-03 = fila roadmap faltante. Añade fila, no bumpees filas históricas.
6. **Árbol de repo en CLAUDE.md:** lista módulos sustantivos (retriever, wizard) con `← NEW vX`; añadí `archetype_lenses.py`. Los tests menores (test_confidence/test_escalation) NO están listados → mantuve esa asimetría (no listé test_archetype_lenses.py para no crear inconsistencia nueva).
7. **Garantía inviolable:** lentes = calidad de deliberación, no input del veredicto. `final_verdict` severidad pura intacto; gate no-op sin tocar synthesis.
8. **Gate regresión-verde ANTES de bump/cert** (archetype 10/10 + escalation 10/10 + confidence 10/10 + smoke 12/1). Se corrió post-apply.
9. **TRADING: 24 SESIONES POSTERGADO (4–27). NO re-confrontar.** Si s28 no elige A, asumir prioridad real ≠ escrita.
10. **Backlog:** P4 (señales externas vía BYO) siguiente. P5 (riesgo reputacional) — evaluar modelarlo como lente `REPUTATIONAL_LENS` en `archetype_lenses.py` (reuso) vs skill #7. Caso-test dorado INVIABLE: "consenso → eficiencia" (la lente EVIDENCE_AUDITOR lo ataca).
11. **Entrega one-shots a la RAÍZ del repo** donde JARP los corre.
