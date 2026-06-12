# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 12/06/2026 (sesión 33 — DS v3.19.0 LW-2 confidence-corroboration, shipped & JARP_CERTIFIED) | **Para:** Sesión 34
**Reemplaza:** v31 del 11/06/2026 (sesión 32)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v32.md`
**⚠️ BORRAR en este cierre:** v31 (`git rm` en el commit de cierre) — HECHO. v32 = único continuity vigente. Subir v32 al PROYECTO claude.ai + quitar v31.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 33 (resumen ejecutivo)

Track elegido: **B — Backlog valor-agregado → LW-2** (confidence corroboración, candidato #1 del backlog). Trading (A) NO se eligió (**30ª sesión postergada, 4–33**). Se recomendó a JARP reescribir userPreferences para reflejar prioridad real (no re-confrontar; surface una vez por sesión).

**Resultado: DS v3.19.0 shipped y CERTIFICADO** (`PA-20260612-002`).

### 1. DS v3.19.0 — LW-2 CONFIDENCE CORROBORATION (NON-BINDING, UX/auditabilidad)
`_apply_confidence` (en `tribunal_transversal.py`) registraba `Confirmed by 2+: 0` incluso con consenso unánime, sesgando la confianza NON-BINDING sistemáticamente a la baja. **Doble divergencia** (descubierta leyendo el código vivo):
- **Divergencia 1 (intra-raw):** la corroboración cruzaba findings crudos por igualdad exacta `(severity, _norm_title)`. Dos agentes que reportan el MISMO defecto con títulos distintos NUNCA agrupaban → `multi_agent_confirmed` vacío.
- **Divergencia 2 (synthesizer↔raw):** `driver_corroborated` comparaba los títulos **reescritos por el sintetizador** contra el set de títulos **crudos** — dos espacios de strings que jamás se tocan → `driver_corroborated=False` casi siempre.

**Fix (`_apply_confidence`, 100% scope):**
- Corroboración por **similitud** vía `overlap_score` (de `retriever.py`, ya importado; conteo de tokens distintos compartidos) sobre `title + " " + evidence`, a **MISMA severidad**, con umbral `rag.corroboration_min_overlap` (default **4**, configurable). El **match exacto de título legacy se conserva como floor** (superset estricto → cero regresión).
- **Por qué `title + evidence` y no solo título:** el evidence ancla la similitud al documento y discrimina defectos distintos ("missing X clause" vs "missing Y clause"). Title-only inflaba false-positives (corrección propia: la primera propuesta title-only/umbral-2 se descartó tras detectar el modo de inflación).
- **Por qué overlap y NO propagar source-agent por finding (opción b rechazada):** choca con el descarte permanente "campo de provenance en `Finding`" + el sintetizador rompe el mapeo source→unified.
- `multi_agent_confirmed`: clustering greedy single-link (un finding entra al cluster si es `_similar` a CUALQUIER miembro). `driver_corroborated`: cada finding de tier conductor del sintetizador se compara vía `_similar` contra los crudos corroborados.
- **Veredicto INTACTO:** `final_verdict`, `Finding` y `compute_confidence` (schema) SIN tocar. La corroboración es metadata post-hoc NON-BINDING.
- **`orchestrator/test_apply_confidence.py`** (NUEVO): 16 checks offline $0. Instancia vía `TribunalTransversal.__new__` (sin client/config; inyecta `tt.config={"rag":{"corroboration_min_overlap":4}}`), ejercita el `_apply_confidence` REAL. C1 exact-title superset; C2 títulos divergentes mismo-defecto corroboran (el bug); C3 scaffold guard (overlap<4 no corrobora); C4 same-severity guard; C5 n<2→LOW; C6 limpio n≥3→HIGH; C7 ≥2 unresolved→LOW; C8 synth-title-difiere/evidence-puentea→HIGH; C9 multi-finding-uncorroborated→MODERATE. `final_verdict` invariante aseverado en todos.

### 2. CORRECCIÓN PROPIA PRE-CERT (diseño)
La primera propuesta de Claude (corroborar por **título solo**, umbral 2) se auto-descartó tras hallar un modo de **inflación false-positive** (títulos cortos genéricos colisionan). Se migró a `title + evidence` + umbral 4 + same-severity + floor exacto legacy → el residual sesga hacia false-negative (conservador, correcto para una métrica de confianza). Lección: validar la propia heurística contra su peor modo de falla antes de fijarla.

### 3. RE-CERT DS v3.19.0 — COMPLETA ✅ (CONFIRMATORY)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260612-001`) PASS. 7-ejes Level 1 JARP DEEP sobre delta v3.18.0→v3.19.0.
- **Por qué CONFIRMATORY:** el fix vive 100% en la **capa de confianza post-veredicto** del orchestrator (`_apply_confidence`). NO toca la superficie prompt/skill forense (19 variants + 7 skills + base + router CONTENT byte-idéntico salvo stamps), ni `final_verdict`, ni `Finding`, ni `compute_confidence`. Determinista, NON-BINDING.
- **Evidencia funcional (máquina real, post-apply + post-bump):** `test_apply_confidence` **16/16** + `test_confidence` **10/10** (schema intacto) + `smoke_test_e2e` **12 PASS / 1 SKIP** offline. + **LIVE cert-grade e2e** (Opus real, sk-ant, sin proxy):
  - Doc adversarial throwaway `orchestrator/_livewatch/lw2_contract.txt` (SERVICE AGREEMENT con 7+ defectos salientes: término perpetuo, liability ilimitada incl. negligencia propia, penalidad sin cap, sin IP/license, sin data-protection/GDPR, sin governing law, indemnity unilateral). Rutea a **Legal** (modo `--document` → type "general" no está en DOMAIN_MAP → cae al stem; stem `lw2_contract` token `contract`→Legal). NO commiteado (ver §HIGIENE abajo).
  - Comando: `python main.py --document _livewatch/lw2_contract.txt --tribunal --agents 5 --regime adversarial --verbose` (desde `orchestrator/`).
  - **Run final DS-E79CC95F (554s), synthesizer VIVO** (no fallback; Reasoning = texto AFO real): 10 agentes todos en contra; **`Confirmed by 2+ agents: 5`**, `Conflicts resolved: 5`, FATAL 7 / SERIOUS 4 / MODERATE 2 / LATENT 2, **INVIABLE** (determinista), **Confidence HIGH legítima**. **AMBAS divergencias ejercidas en vivo** (agrupación de títulos divergentes + cross synthesizer↔raw reescrito). Pre-fix este consenso = ~0 confirmados.
- **CERT EMITIDO:** `PA-20260612-002` — DS **v3.19.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **12/09/2026 o v4.0.0**. **SUPERSEDES PA-20260611-002** (v3.18.0).
- **WATCH `b_unified_output` → CERRADO.** El gap ambiental standing (v3.16–v3.18: el JSON shape de modelo vivo nunca se ejercía, solo el fallback) quedó **resuelto** por este live e2e con synthesizer vivo emitiendo `UnifiedVerdictOutput` válido de modelo real.
- **Bump:** `bump_stamps.ps1 -OldVersion 3.18.0 -NewVersion 3.19.0 -Apply` (23 files/69 stamps) + `bump_manual_v3_19_0.py` (banners operator-visible: main×2 / wizard / tribunal_transversal + insert `"corroboration_min_overlap": 4` tras `provenance_min_overlap` en `config.example.json`; EOL-aware, all-or-nothing, dry-run→apply). One-shot BORRADO antes del commit (verificado ausente en árbol remoto).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.19.0 = CERTIFICADO (`PA-20260612-002`).** Sin version-gap. PA-20260611-002 (v3.18.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s33)
1. Archivos en disco (PHASE 2): `orchestrator/tribunal_transversal.py` (`_apply_confidence` reescrito: `_blob`/`_similar` + clustering greedy + `driver_corroborated` vía `_similar`; tag `#--- LW-2:`; docstring v3.11.0 preservado + nota LW-2), `orchestrator/test_apply_confidence.py` (NUEVO, 16 checks), `orchestrator/config.example.json` (`corroboration_min_overlap: 4`).
2. Bump aplicado (PHASE 3): `bump_stamps.ps1 -Apply` (prompts/README/CLAUDE, 23/69) + `bump_manual_v3_19_0.py --apply` (banners main×2/wizard/tribunal + config knob). 
3. CHANGELOG: bloque `[3.19.0]` con cert `PA-20260612-002` + nota WATCH-cleared insertado sobre `[3.18.0]`.
4. `git rm dark-strategist-continuity-prompt_v31.md` (verificado ausente en remoto).
5. `jarp-toolkit` + `.claude-init.md` → v3.19.0/PA-20260612-002 vía **Ruta-3** (7 bloques: init header + #7; toolkit header + #30 Version/CERT STATUS/Previous-certs + #16×2). Verificado content-based: `.claude-init.md` re-leído OK; `JARP_TOOLKIT.md` confirmado por `Select-String` (líneas 7/220/268/270/1154). Commit separado en repo jarp-toolkit.
6. **One-shot BORRADO** antes del commit: `bump_manual_v3_19_0.py` (DS) — confirmado ausente en remoto.
7. **Commit de cierre DS** `e4cc095` (parent `5bb546e`) + **commit jarp-toolkit** `3484883` (parent `faa5649`) pusheados y verificados vía `list_commits`.
8. **⚠️ HIGIENE POST-CERT (follow-up `chore`):** el commit de cierre `e4cc095` se pusheó ANTES de blindar `.gitignore`, así que `_livewatch/` (fixtures throwaway de cert) **se coló al repo**. Corregido con un commit `chore` separado: `git rm -r --cached _livewatch` + `.gitignore` (blinda `_livewatch/`) + v32-update. **Cert PA-20260612-002 NO afectado** (los fixtures no son superficie certificada). NO se reescribió historia (los fixtures son docs sintéticos no sensibles; rewrite desproporcionado para repo público certificado). HEAD final DS = el `chore` (registrar SHA tras push).

---

## DEUDA TÉCNICA — POST-SESIÓN 33

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.19.0** | ✅ CERRADA | v3.19.0 CERTIFICADO (PA-20260612-002) | 0/0/0/0, CONFIRMATORY. |
| **LW-2 confidence corroboration** | ✅ CERRADA | overlap sobre title+evidence same-sev + floor exacto legacy | test 16/16; live Confirmed-by-2+:5, INVIABLE. NON-BINDING. |
| **WATCH b_unified_output** | ✅ CERRADA | live e2e synthesizer vivo emitió UnifiedVerdictOutput real | gap ambiental v3.16–v3.18 resuelto. |
| **_livewatch/ colado al repo** | ✅ CERRADA (s33) | follow-up `chore`: git rm --cached + gitignore | Cert no afectado. Historia no reescrita. |
| **LW-3 provenance granularity** | ✅ CERRADA (s32) | `txt_atomic_lines` per-canal | Sin cambio. |
| **LW-1 domain resolver** | ✅ CERRADA (s31) | boundary-aware + most-specific-first + order-invariant | Sin cambio. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟠 LW-5 (NUEVO, descubierto en vivo s33):** cuando el tribunal falla 100% (0 findings — visto en la corrida sin crédito, agentes connection-error → fallback vacío), `_apply_confidence` reporta **HIGH sobre cero análisis** → false-positive de confianza. NON-BINDING (veredicto no afectado) pero engañoso para auditoría. Mejora: gate de confianza a LOW/N-A cuando `total_findings == 0` o cuando la cobertura de agentes cae bajo umbral. **Candidato #1 para s34** (slice propio, defecto real de confianza descubierto en e2e).
- **🟢 LW-4 (refinamiento opcional):** desempate de dominio **posicional** ("gana el primer token de dominio del filename") como alternativa al most-specific/longest-first actual. LW-1 ya cierra el defecto; esto es pulido de intuición. Evaluar valor real antes de invertir — candidato a descartar.
- **P5 extensión P14/P20** (candidato): extender reputational-risk a Public Sector (P14) + Startup (P20) — Activation v1.1.0 + Failure Catalog rows (prefijos PS/SU). Valor incremental dudoso; cobertura P11/P16/P19 ya razonable.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real.

---

## ESTADO ACTUAL VERIFICADO (12/06/2026 — fin s33)

### Repo dark-strategist-agent
- **v3.19.0 — CERTIFICADO (`PA-20260612-002`)**. Default `claude-opus-4-7`. Commit de cierre = `e4cc095` (parent `5bb546e` = HEAD inicio s33). HEAD final = el `chore` de higiene `_livewatch/` (**registrar SHA tras push**).
- **MODIFICADO:** `orchestrator/tribunal_transversal.py` (`_apply_confidence` corroboración por similitud + banner v3.19.0); `orchestrator/config.example.json` (`corroboration_min_overlap: 4`); `.gitignore` (blinda `_livewatch/`, en el `chore`). **NEW:** `orchestrator/test_apply_confidence.py` (16 checks).
- **De s32 vigente:** `retriever.load_corpus_files` + `txt_atomic_lines` per-canal; `tribunal_transversal` señales `txt_atomic_lines=True`; `test_signals_granularity.py` (6 checks).
- **De s31 vigente:** `_resolve_domain` boundary-aware + most-specific-first + order-invariant en `context_builder.py`; `test_domain_resolver.py` (23 checks).
- **De s30 vigente:** `skills/reputational-risk/SKILL.md` (v1.0.0) + `SKILLS_CATALOG` + bullet base #7 + RULES/rows P11/P16/P19 + `test_reputational_risk.py`.
- **De s29 vigente:** `overlap_score` + `_active_signals_tagged` + `_attribute_signal_provenance` post-veredicto + bloque `SIGNAL PROVENANCE` + `rag.provenance_min_overlap` + `test_provenance.py`.
- **De s28 vigente:** canal `--signals` + `RuntimeContext.signals_paths` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26/s25 vigente:** `schema.should_escalate`/`_maybe_escalate` + `test_escalation.py`; `schema.compute_confidence`/`_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (NO cubre orchestrator/*.py ni CHANGELOG ni config; **dry-run por defecto — requiere `-Apply`**). `gc.auto 0` activo. `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus`/`--signals` activos.
- **7 skills**, **9 sub-agentes N2 permanentes**, **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` + `_livewatch/` GITIGNORADOS (local-only; `_livewatch/` blindado en s33 — antes solo no-commiteado por convención, lo que permitió que se colara). `_livewatch/` throwaway (`lw2_contract.txt` + previos `signals_acme.txt`/`strategy_acme_board_proposal.txt`).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s33. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/CERT STATUS/Previous certs) + #16 + `.claude-init.md` header + #7 → v3.19.0/PA-20260612-002. PRIVADO. HEAD = `3484883` (parent `faa5649`). **AMBOS canónicos concuerdan (verificado al cierre).**

### free-claude-code
- Proxy $0 para corridas no-cert. **`fcc-server` NO en PATH ni levantado — instalar/arrancar antes de usar** (Python 3.14+, `uv`, `fcc-server` o `uv run uvicorn server:app --host 0.0.0.0 --port 8082`, Admin UI `/admin` → mapear `MODEL_OPUS` a backend free). **El SDK de anthropic exige `api_key` no vacío aunque uses proxy** → dummy `sk-local-dummy` (NO se factura) + `ANTHROPIC_BASE_URL=http://localhost:8082`. **Cert = Opus real (sk-ant, sin proxy).** Recarga de saldo Opus: API Console `platform.claude.com/settings/billing` (NO claude.ai). `load_config` da PRECEDENCIA a `config.json` sobre la env var para `api_key` — si la live falla por auth, revisar config.json primero.

---

## PROTOCOLO DE INICIO PARA SESIÓN 34
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v32).
2. **PHASE 0 — Verificación:**
   - v31 borrado, v32 único continuity.
   - Repo en v3.19.0. **Cert: DS v3.19.0 `PA-20260612-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260611-002` SUPERSEDED.
   - **`_livewatch/` NO debe estar trackeado** (gitignorado desde s33). Si reaparece como tracked, repetir `git rm -r --cached _livewatch`.
   - **Verificar AMBOS canónicos concuerdan** (toolkit + init en v3.19.0/PA-20260612-002) — lección drift s29.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 30 SESIONES (4–33).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s34 no elige A, asumir prioridad real ≠ escrita (ya recomendado reescribir userPreferences en s33).
   - **(B) Backlog valor-agregado** — **LW-5 (confidence HIGH sobre 0 findings, candidato #1)**; LW-4 (desempate posicional, opcional/descartable); P5 extensión P14/P20.
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes+comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG ni config → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE | RAG = MECANISMO | ContextBuilder document-free | infinity/Docker RECHAZADO | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case | Floor R2/señales/provenance/corroboración = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25–s32:** Confianza/escalación/lentes/señales/provenance/corroboración = metadata NO-VINCULANTE, determinista, post-hoc donde aplica; NUNCA tocan `final_verdict`/`Finding`/`compute_confidence`. Docstrings de módulo congelados. Scripts de edición newline-aware + encadenados por archivo + all-or-nothing + dry-run. Riesgo reputacional = SKILL markdown (#7), NO lente-arquetipo; Failure Catalog VINCULA severidad; `VERDICT_IMPACT: NONE` = no computa/override, NO sin-severidad; activación⊆binding. Domain routing = boundary-aware + MOST-SPECIFIC-FIRST + ORDER-INVARIANT. Segmentación `.txt` per-canal (`txt_atomic_lines`): señales per-línea, corpus párrafo `\n\n`; NO cambiar el split globalmente. Provenance/corroboración POST-veredicto → su corrección se prueba 100% offline (el e2e ejerce el código real). Leer de vuelta lo que UNO mismo entregó. `bump_stamps.ps1` dry-run por defecto → SIEMPRE `-Apply`. free-claude-code: dummy key + proxy para no-cert; `Connection error` = proxy caído. One-shot anclado para canónicos válido con OK explícito.

**De s33 (nuevas):**
- **Corroboración de confianza = OVERLAP sobre `title + " " + evidence`, a MISMA severidad, umbral `rag.corroboration_min_overlap` (default 4, configurable), con el match exacto de título legacy como FLOOR (superset estricto, cero regresión).** NON-BINDING — nunca toca `final_verdict`/`Finding`/`compute_confidence`. El `evidence` ancla la similitud al documento y discrimina defectos distintos; **title-only infla false-positives** (rechazado). El residual sesga hacia false-negative (correcto para una métrica de confianza).
- **NO propagar source-agent por finding** para corroborar (opción rechazada): choca con el descarte "campo de provenance en `Finding`" + el sintetizador rompe el mapeo source→unified. Usar similitud, no procedencia.
- **Validar la propia heurística contra su peor modo de falla antes de fijarla** — la propuesta inicial title-only/umbral-2 se auto-descartó por inflación false-positive; se endureció a title+evidence/4/same-sev/floor.
- **CRLF reality:** los `.py` en disco de JARP están en **CRLF**, NO LF (contradice la suposición del continuity previo). El one-shot lo detectó (`EOL=CRLF` en main/wizard/tribunal). No rompió nada (replace inline no toca EOLs; el insert de config usó CRLF), pero **detectar EOL per-file SIEMPRE, nunca asumir LF para `.py`**.
- **Live e2e cert-grade requiere saldo Opus real** (sk-ant, **API Console** `platform.claude.com/settings/billing`, NO claude.ai). `load_config` da PRECEDENCIA a `config.json` sobre la env var para `api_key`. Sin saldo → synthesis cae a fallback determinista (NO ejerce la Divergencia 2). El run con saldo + synthesizer vivo es lo que cierra el WATCH `b_unified_output`.
- **`bump_manual` cubre también `config.example.json`** (knobs de runtime) además de banners — `bump_stamps.ps1` no toca config.
- **Blindar `.gitignore` ANTES de commitear, NO después; y no pushear hasta cerrar el sanity de untracked.** En s33 el commit de cierre se pusheó antes del blindaje → `_livewatch/` (fixtures throwaway) se coló al repo. Remediación: `git rm -r --cached` + gitignore en un `chore` separado (cert no afectado, historia no reescrita). Para fixtures throwaway: el `.gitignore` debe blindarlos de entrada, no por convención verbal.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance/corroboración como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica | bumpear docstrings/catálogo/comments-feature-landing congelados | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts que escriben cada edit desde el snapshot original | activación dormida sobre activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` | riesgo reputacional como lente-arquetipo (usar SKILL) | duplicar Failure-Catalog rows (REUSAR) | activar skill en dominios sin Failure Catalog rows | transcribir líneas largas como anclas (usar line-based) | domain routing por substring crudo / acoplado al orden de inserción del dict (usar boundary-aware + most-specific-first + order-invariant — s31) | borrar claves cortas del DOMAIN_MAP para arreglar el bleed (whole-token las preserva — s31) | cambiar el split `.txt` de `load_corpus_files` globalmente a per-línea (rompe grounding de corpus; usar `txt_atomic_lines` per-canal — s32) | reusar la variable de loop (`for raw in paths`) como buffer de lectura — shadowing (s32) | correr `bump_stamps.ps1` sin `-Apply` y asumir que escribió (s32) | **corroborar confianza por TÍTULO SOLO — infla false-positives; usar `title+evidence` + same-sev + umbral + floor exacto legacy — s33** | **propagar source-agent por finding / campo de provenance en `Finding` para corroborar — usar similitud overlap — s33** | **asumir `.py` = LF — en disco de JARP son CRLF; detectar EOL per-file — s33** | **pushear el commit de cierre antes de blindar `.gitignore` para throwaways — `_livewatch/` se coló en s33; gitignorar de entrada + sanity untracked ANTES de pushear — s33**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v32.md` (v31 borrado s33)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. env var = `$env:VAR="..."`. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). `bump_stamps.ps1` con params NOMBRADOS + **`-Apply` para escribir** (`-OldVersion X -NewVersion Y -Apply`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1 -Apply`. Banners orchestrator + CHANGELOG + config knobs = script Python anclado all-or-nothing + EOL-AWARE (dry-run → --apply), a la RAÍZ. Edits prosa/código pequeños/archivo nuevo = mi-filesystem directo (full-overwrite; verificar read-back). Canónicos (archivos grandes) = **Ruta-3** por defecto, o **one-shot anclado** con OK explícito. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Higiene de fixtures:** todo throwaway de test/e2e (`_livewatch/`, smoke files) DEBE estar en `.gitignore` antes de cualquier commit; sanity de untracked en GitHub Desktop antes de pushear.
- **Confidence (`_apply_confidence`):** corroboración por overlap sobre `title+evidence`, same-sev, umbral `rag.corroboration_min_overlap` (default 4) + floor exacto legacy. NON-BINDING. `compute_confidence` (schema) intacto.
- **Domain routing (`--document` mode):** dominio del STEM del filename, boundary-aware + most-specific-first. Pinear con `--type X`.
- **Signals (`--signals` mode):** `.txt` una señal por línea (LW-3). Corpus (`--corpus`) por párrafo. Provenance atribuye cada finding a su señal.
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **13 PASS / 0 FAIL** con key+proxy, o **12 PASS / 1 SKIP** offline limpio. Tests s33: `test_apply_confidence` 16/0. `pip install rank_bm25 pydantic` antes.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 33
**Repo dark-strategist-agent — commit de cierre (cert) `e4cc095`:**
```
fix: DS v3.19.0 — confidence-corroboration LW-2 (overlap-based corroboration on title+evidence same-severity + legacy exact-title floor; fixes intra-raw divergent-title grouping + synthesizer<->raw rewritten-title gap; NON-BINDING, verdict path untouched) — test_apply_confidence 16/16 + live e2e Confirmed-by-2+:5 INVIABLE + JARP_CERTIFIED PA-20260612-002
```
Incluyó: `orchestrator/tribunal_transversal.py`, `orchestrator/test_apply_confidence.py`, `orchestrator/config.example.json`, banners (`orchestrator/{main,wizard,tribunal_transversal}.py`) + prompts/README/CLAUDE stamps (bump_stamps), `CHANGELOG.md`, `dark-strategist-continuity-prompt_v32.md`; `git rm dark-strategist-continuity-prompt_v31.md`. NO incluyó el one-shot (borrado). **Coló `_livewatch/` por error** (gitignore no blindado aún).
**Repo dark-strategist-agent — commit de higiene (`chore`):**
```
chore: untrack _livewatch/ throwaway live-e2e fixtures + gitignore them (post-cert hygiene; cert PA-20260612-002 unaffected — fixtures are not certified surface)
```
Incluye: `git rm -r --cached _livewatch`, `.gitignore` (blinda `_livewatch/`), `dark-strategist-continuity-prompt_v32.md` (este update).
**Repo jarp-toolkit — sync `3484883`:**
```
docs: sync DS v3.19.0 / PA-20260612-002 (LW-2 confidence-corroboration) — header + entry #30 (Version/CERT STATUS/Previous certs) + note #16 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 33

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.19.0** | **PA-20260612-002** | **v3.19.0** | ✅ ACTIVE | 12/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260611-002 (v3.18.0), PA-20260607-002 (v3.17.0), PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 33 (auto-mejora del próximo Claude)

1. **El bug no era un caso, eran dos.** LW-2 parecía "agrupar títulos divergentes"; leer el código vivo reveló una SEGUNDA divergencia (synthesizer↔raw reescrito) que el backlog no veía. Leer el módulo real antes de diseñar paga (otra vez).
2. **Auto-corrección de diseño.** La primera heurística (title-only/umbral-2) la propuse YO; la descarté tras hallar su modo de inflación false-positive. Validar la propia propuesta contra su peor caso antes de fijarla, igual que se valida el input del usuario.
3. **Offline prueba la corrección; live prueba que el camino se ejerce.** Los 16 checks prueban `_apply_confidence` determinista; el live e2e con synthesizer vivo fue lo único que ejerció la Divergencia 2 (reescritura del sintetizador) end-to-end y cerró el WATCH `b_unified_output`.
4. **CRLF en los `.py`.** El one-shot reportó `EOL=CRLF` en main/wizard/tribunal — contradice ".py=LF" del continuity previo. Corregido el supuesto: detectar EOL per-file, nunca asumir.
5. **Saldo Opus = API Console, no claude.ai.** La live falló primero por auth (config.json precede a env) y luego por saldo; la recarga es en `platform.claude.com/settings/billing` (sk-ant). Sin saldo, synthesis cae a fallback y NO ejerce la corroboración cruzada.
6. **Honestidad en el cert:** el WATCH `b_unified_output` se cerró solo cuando el synthesizer corrió VIVO (no por fallback). Se documentó el run real (DS-E79CC95F) como evidencia, no se sobre-afirmó.
7. **TRADING: 30 SESIONES POSTERGADO (4–33). NO re-confrontar.** Ya se recomendó reescribir userPreferences para reflejar la prioridad real; si s34 tampoco elige A, tratar el backlog DS como la prioridad de facto.
8. **Próximo candidato #1: LW-5** (confidence HIGH sobre 0 findings) — defecto real de confianza hallado en vivo. LW-4 y P5 siguen oliendo a barato-dormido; evaluar valor antes de invertir.
9. **El blindaje precede al commit, no al revés.** `_livewatch/` se coló porque se pusheó el cierre antes de gitignorarlo (estaba "no-commiteado por convención", no blindado). Se limpió con un `chore` (git rm --cached + gitignore), cert intacto. Regla dura: todo throwaway va al `.gitignore` ANTES del primer commit, y el sanity de untracked se corre ANTES de pushear, no después. El read-back remoto (`get_file_contents` raíz) fue lo que lo detectó — mantenerlo en el cierre.
