# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 04/06/2026 (sesión 26 — DS v3.12.0 gate de escalamiento por confianza, shipped & JARP_CERTIFIED) | **Para:** Sesión 27
**Reemplaza:** v24 del 04/06/2026 (sesión 25)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v25.md`
**⚠️ BORRAR en este cierre:** v24 (`git rm` en el commit de cierre). v25 = único continuity vigente. Subir v25 al PROYECTO claude.ai + quitar v24.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 26 (resumen ejecutivo)

Continuación de s25 en el mismo chat (no se abrió chat nuevo). Track elegido: **P1 — gate de escalamiento por confianza** (siguiente lógico del backlog; depende de P3, ya hecho en s25). Trading (A) NO se eligió (**23ª sesión postergada, 4–26**).

**Resultado: DS v3.12.0 shipped y CERTIFICADO** (`PA-20260604-004`). Bump **no-forense confirmatorio**.

### 1. (P1) DS v3.12.0 — gate de escalamiento por confianza, NO-VINCULANTE
- **`orchestrator/schema.py`** — `+ should_escalate(confidence, rounds_done, max_rounds, remaining_agents, enabled)`. Gate puro/determinista/testeable. Escala SII: `enabled` Y `confidence=="LOW"` Y `rounds_done<max_rounds` Y `remaining_agents>0`.
- **`orchestrator/tribunal_transversal.py`** — `_maybe_escalate(...)` enganchado **justo tras `_synthesize`** en `run()` (antes de SSM). Si gate abre → `_run_escalation_round`: pasada Forense **acotada** sobre los hallazgos que dictan el veredicto, con **ids distintos `FOR-ESC-*`** (para que la corroboración cross-agent los cuente como independientes) → anexa outputs → **re-`_synthesize`** → recomputa `confidence`. Cap por `max_escalation_rounds`. **Degrada con gracia** (errores capturados) → corridas offline/sin-API no crashean. + bloque CONFIDENCE/Escalation en transparency report.
- **`orchestrator/main.py` + `config.example.json`** — llaves nuevas: `escalation_enabled` (true), `max_escalation_rounds` (1), `max_escalation_agents` (2). Leídas vía `.get(...)` con defaults (funciona aunque falten).
- **`orchestrator/test_escalation.py`** (NUEVO, commiteado) — truth-table 10 casos offline, $0.

**GARANTÍA INVIOLABLE verificada:** la escalación es decisión de **presupuesto de deliberación**, NO input del veredicto. `final_verdict` sigue severidad pura (FATAL→INVIABLE). Test integración: los 3 paths no-op del gate (HIGH / LOW-sin-budget / LOW-disabled) **no invocan `_synthesize` ni `_run_escalation_round`** y dejan `final_verdict` intacto. `confidence` puede quedarse LOW tras escalar (honesto, nunca se infla).

### 2. DECISIONES CLAVE (s26)
- **Gate de escalamiento = no-vinculante** (consistente con P3 + RULE LG07/F08). Solo decide *si vale gastar más deliberación*; jamás toca el veredicto.
- **Ronda de escalamiento = Opción 1 (acotada):** re-profundiza la capa Forense existente con ids `FOR-ESC-*` y una directiva de escrutinio sobre los hallazgos contestados. **Reusa prompts/agentes existentes, sin tipo de agente nuevo.** P2 (lentes-arquetipo) se enchufa después como mejora de esta ronda.
- **ids distintos obligatorios:** re-usar `FOR-01..` rompería la corroboración (se dedupea por `agent_id`). `FOR-ESC-*` garantiza que cuenten como agentes nuevos → suben `n`/corroboración → `compute_confidence` puede subir (o quedarse LOW si sigue sin corroborar).
- **Cap=1 ronda + budget-gated** por `remaining_agents()`. Sin loops.
- **Scripts de edición ahora NEWLINE-AWARE.** `config.example.json` está en **CRLF** mientras los `.py`/`.md` están en LF → un anchor con `\n` falla en CRLF. Todo script de edición detecta el fin de línea del archivo y traduce el anchor (`old.replace("\n", nl)`). Sin esto, el apply aborta (correctamente, all-or-nothing) en archivos CRLF.

### 3. RE-CERT DS v3.12.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 RULE 08 (`PA-20260604-003`) PASS (PA-agent sin cambios). Auditoría 7-ejes confirmatoria sobre delta v3.11.0 (19/19 byte-idénticas salvo stamp).
- **Evidencia funcional (máquina real, POST-bump):** `test_escalation.py` **10/10** + `test_confidence.py` **10/10** + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (`b_unified_output` SKIP = DNS/key, no-bloqueante), `c_fallback_intact` + `e_monotonic_verdict` PASS.
- **CERT EMITIDO:** `PA-20260604-004` — DS **v3.12.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **04/09/2026 o v4.0.0**. **SUPERSEDES PA-20260604-002** (v3.11.0). Sin cascade (minor).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.12.0 = CERTIFICADO (`PA-20260604-004`).** Sin version-gap. PA-20260604-002 (v3.11.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s26) ✅
1. P1 código: `apply_p1_escalation.py --apply` → `schema.py` + `tribunal_transversal.py` + `main.py` + `config.example.json` + `test_escalation.py`. Regresión verde.
2. Bump anclado: `bump_stamps.ps1 3.11.0→3.12.0 -Apply` → ~23 files / ~69 stamp lines (prompts + README + CLAUDE).
3. Bump manual: `bump_manual_v3_12_0.py --apply` → CHANGELOG [3.12.0] + 4 banners orchestrator + CLAUDE status + filas tabla.
4. Cert: `finalize_cert_v3_12_0.py --apply` → bloque JARP_CERTIFIED PA-20260604-004 en CHANGELOG.
5. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.12.0/PA-004 (vía mi-filesystem).
6. `jarp-toolkit/JARP_TOOLKIT.md` — `sync_toolkit_v3_12_0.py --apply` → header + #30 + Note #16.
7. Continuity v25 commiteado; `git rm` v24.
8. **One-shots BORRADOS** (no commiteados): `apply_p1_escalation.py`, `bump_manual_v3_12_0.py`, `finalize_cert_v3_12_0.py` (DS), `sync_toolkit_v3_12_0.py` (toolkit). **Recordatorio: `del` de PowerShell usa COMAS para varios archivos** (`del a.py, b.py, c.py`).

---

## DEUDA TÉCNICA — POST-SESIÓN 26

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.12.0** | ✅ CERRADA | v3.12.0 CERTIFICADO (PA-20260604-004) | 0/0/0/0. |
| **P1 escalación** | ✅ CERRADA | Gate de escalamiento por confianza shipped | Acotado, budget-gated, no-vinculante; test_escalation.py. |
| **clash n>0 live + gate b live** | 🟢 WATCH | `b_unified_output` SKIP | Causa = DNS INTERMITENTE (`getaddrinfo failed` a api.anthropic.com). Ambiental. No-bloqueante. La escalación LIVE tampoco se ejercita offline (degrada con gracia). |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO (del análisis forense s25) — pendiente
- **P2 — lentes-arquetipo (SIGUIENTE).** Perspectivas estructuradas que enriquecen la ronda de escalamiento P1. **NO impersonar personas reales** (fabricación de autoridad, descartado). Se enchufa en `_run_escalation_round`.
- **P4 — señales externas vía BYO/RAG existente** (`--corpus`; sin infra nueva).
- **P5 — lente de riesgo reputacional** (posible skill #7).
- **Caso-test dorado INVIABLE:** "consenso 95% → eficiencia 95%" (causalidad inventada). Fixture de lo que DS debe DESTRUIR. Útil para validar P1/P2 end-to-end con un caso LOW que dispare escalación.

---

## ESTADO ACTUAL VERIFICADO (04/06/2026 — fin s26)

### Repo dark-strategist-agent
- **v3.12.0 — CERTIFICADO (`PA-20260604-004`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.12.0 (registrar SHA tras push).
- **NEW:** `schema.should_escalate` + `tribunal._maybe_escalate`/`_run_escalation_round` + config keys + `test_escalation.py`. Gate de escalamiento determinista/no-vinculante.
- **De s25 vigente:** `schema.compute_confidence` + `tribunal._apply_confidence` (ambos caminos) + `test_confidence.py`.
- `tools/bump_stamps.ps1` (NO toca orchestrator/*.py ni CHANGELOG). `gc.auto 0` activo.
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` activo.
- **6 skills**, **9 sub-agentes N2 permanentes** (sin cambio).
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s26. Sin cambios.

### Repo jarp-toolkit
- header + #30 + Note #16 + `.claude-init.md` Note #7 → v3.12.0/PA-004. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 27
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v25).
2. **PHASE 0 — Verificación:**
   - v24 borrado, v25 único continuity.
   - Repo en v3.12.0. **Cert registry: DS v3.12.0 `PA-20260604-004` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260604-002` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados.
   - `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 23 SESIONES (4–26).** Prioridad #1 en userPreferences. **NO re-confrontar.**
   - **(B) Backlog valor-agregado** — **P2 (lentes-arquetipo) es el siguiente lógico** (enriquece la ronda de escalamiento P1). Luego P4/P5. Caso-test dorado disponible.
   - **(C) WATCH live-key/DNS** — no-bloqueante (ambiental).
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based/congelados, p.ej. catalogs.py @3.2.0) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | 4 variance decompositions | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE, NO driver | RAG = MECANISMO, NO driver | ContextBuilder document-free | infinity/Docker RECHAZADO | fallback byte-idéntico ante cambio de feed | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2 = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25:** Confianza = metadata NO-VINCULANTE, determinista, ambos caminos (`compute_confidence` nunca toca `final_verdict`). `multi_agent_confirmed` + `agents_consulted` derivados determinísticamente. Docstrings de módulo congelados (no bumpean cada minor).

**De s26 (nuevas):**
- **Gate de escalamiento (`should_escalate`) = NO-VINCULANTE, determinista.** Solo decide gastar deliberación; jamás toca el veredicto. Ronda acotada, ids `FOR-ESC-*` distintos, cap por config, budget-gated, degrada con gracia offline.
- **Ronda de escalamiento reusa la capa Forense existente (Opción 1), sin tipo de agente nuevo.** P2 se enchufa aquí.
- **Scripts de edición DEBEN ser newline-aware** (detectar `\r\n` vs `\n` del archivo). `config.example.json` está en CRLF; los `.py`/`.md` en LF. Anchor con `\n` literal falla en CRLF.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | skills knowledge-work descartadas | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor R2 por score BM25 | **confianza como driver del veredicto (es metadata) — s25** | **impersonar personas reales en lentes-arquetipo — s25** | **"consenso → eficiencia" como métrica válida (caso-test INVIABLE) — s25** | **bumpear docstrings de módulo congelados cada minor — s25** | **escalación como input del veredicto (es decisión de presupuesto de deliberación) — s26** | **re-usar ids `FOR-*` en la ronda de escalamiento (rompe corroboración; usar `FOR-ESC-*`) — s26** | **anchors de edición con `\n` literal en archivos CRLF — s26**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v25.md` (v24 borrado s26)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (comandos por separado o `;`). `del` de varios archivos usa **COMAS** (`del a, b, c`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1` (NO orchestrator/*.py ni CHANGELOG). Edits prosa/código multi-archivo = **script Python anclado all-or-nothing + NEWLINE-AWARE** (dry-run → --apply), **entregado a la RAÍZ del repo** donde JARP lo corre. Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Confianza + escalación runtime:** `confidence` determinista (P3); `_maybe_escalate` re-delibera si LOW+budget (P1). Ambos NO-VINCULANTES, etiquetados en el transparency report.
- **Smoke-test E2E (LOCAL, gitignorado):** `orchestrator/smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. `python test_escalation.py` → **0 FAIL / 10**. `python test_confidence.py` → **0 FAIL / 10**. `pip install rank_bm25` + `pydantic` antes.
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 26
**Repo dark-strategist-agent (v3.12.0 cert) — commit atómico:**
```
feat: DS v3.12.0 — confidence-gated escalation (NON-BINDING, bounded, budget-gated) + JARP_CERTIFIED PA-20260604-004
```
Incluye: `orchestrator/{schema,tribunal_transversal,main,test_escalation}.py`, `orchestrator/config.example.json`, 21 prompts, README, CLAUDE, CHANGELOG, `orchestrator/wizard.py`, `dark-strategist-continuity-prompt_v25.md`; `git rm dark-strategist-continuity-prompt_v24.md`. NO incluye los one-shots.
**Repo jarp-toolkit:**
```
docs: sync DS v3.12.0 / PA-20260604-004 (confidence-gated escalation) — header + #16 + #30 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 26

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.12.0** | **PA-20260604-004** | **v3.12.0** | ✅ ACTIVE | 04/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 26 (auto-mejora del próximo Claude)

1. **Lee el módulo real ANTES de implementar.** P1 se enchufó en `run()` tras `_synthesize`; el spawner produce metadata (`sub_agents_used`), NO findings → la ronda de escalamiento debe generar outputs con findings (ids `FOR-ESC-*`) para mover la corroboración. Confírmalo contra el código, no asumas.
2. **Scripts de edición = NEWLINE-AWARE.** `config.example.json` está en CRLF; el anchor con `\n` falló y el apply abortó (correcto, all-or-nothing). Fix: detectar `\r\n` vs `\n` y traducir el anchor. Aplícalo a TODOS los scripts de edición de aquí en adelante.
3. **PowerShell `del` de varios archivos = COMAS** (`del a.py, b.py, c.py`), no espacios. Y nada de `&&`.
4. **Garantía inviolable:** escalación = decisión de presupuesto, no input del veredicto. Verifícalo con los paths no-op del gate (no deben invocar `_synthesize`/`_run_escalation_round`; `final_verdict` intacto).
5. **Gate regresión-verde ANTES de bump/cert** (test_escalation 10/10 + test_confidence 10/10 + smoke 12 PASS/1 SKIP). Re-correr POST-bump.
6. **TRADING: 23 SESIONES POSTERGADO (4–26). NO re-confrontar.** Si s27 no elige A, asumir prioridad real ≠ escrita.
7. **Backlog:** P2 (lentes-arquetipo, NO personas reales) enriquece la ronda de escalamiento P1 → siguiente lógico. Luego P4 (señales vía BYO) / P5 (skill riesgo reputacional). Caso-test dorado INVIABLE: "consenso → eficiencia".
8. **WATCH b = DNS intermitente** (`getaddrinfo failed`). Ambiental, no-bloqueante. La escalación live tampoco se ejercita offline (degrada con gracia). No quemar sesión debuggeándolo.
9. **Entrega one-shots a la RAÍZ del repo** donde JARP los corre (no a home). Mismo error costó un round-trip en s25.
