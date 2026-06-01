# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 01/06/2026 (sesión 18 — re-cert v3.4.0 COMPLETA + free-claude-code cableado) | **Para:** Sesión 19
**Reemplaza:** v16 del 31/05/2026 (sesión 17)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v17.md`
**⚠️ BORRAR en este cierre:** v16 (autorizar borrado vía GitHub Desktop). v17 = único continuity vigente. Subir v17 al PROYECTO claude.ai + quitar v16.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 18 (resumen ejecutivo)

Tres bloques: (1) `free-claude-code` cableado como proxy de inferencia, (2) evaluación del documento "Barrido sistemático" que JARP no recordaba, (3) **re-cert full-coverage de DS v3.4.0 — COMPLETA**. DS pasa a **JARP_CERTIFIED**.

### 1. free-claude-code — CABLEADO (capacidad nueva)
- Proxy Anthropic-compatible (entry #43 toolkit). **Integración DS = zero-code:** DS instancia `anthropic.Anthropic(api_key=...)` SIN `base_url` (5 puntos: tribunal_transversal, router, sub_agent_spawner, ssm/interaction_engine, cloud_function) → exportar `ANTHROPIC_BASE_URL=http://localhost:8082` redirige todo. En Admin UI fijar `MODEL_OPUS` al backend elegido; DS sigue "pidiendo opus", el proxy resuelve por tier.
- **11 backends** (NO 17 — corregido s18): NVIDIA NIM, Kimi, Wafer, OpenRouter, DeepSeek, LM Studio, llama.cpp, Ollama, OpenCode Zen, OpenCode Go, Z.ai. Free: OpenRouter `:free`, OpenCode `*-free`, NIM créditos, 3 locales (Ollama/LM Studio/llama.cpp, sin tope externo, bound por hardware).
- **REGLA DE GOBERNANZA (registrada en toolkit nota #34):** backend free para TODA corrida DS no-cert (smoke/regresión/N-sims); **Opus real (`claude-opus-4-7`, sk-ant, sin proxy) solo para evidencia grado-cert.** Nunca certificar comportamiento de backend no auditado. Fijar UN backend por campaña (comparabilidad apples-to-apples). El fallback determinista carga docs ricos pase lo que pase → corridas free hacen stress de orquestación, NO validan calidad de síntesis.
- Arranque: `fcc-server` (o `uv run uvicorn server:app --port 8082`); `config.json` perfil SMOKE (`api_key:"freecc"`) vs CERT (`api_key:"sk-ant-..."`); `$env:ANTHROPIC_BASE_URL` solo en la ventana PowerShell (NO `setx`).
- Toolkit: entry #43 + nota #34 + header corregidos y pusheados (commit s18, verificado por contenido).

### 2. Evaluación documento "Barrido sistemático" (15 repos, era v3.1.0)
- **Hallazgo:** ese documento ES la fuente que generó el v3.3 ROADMAP de entry #30. Sus 🔴 INCORPORAR → TOP 7 actual, EXCEPTO `superpowers` (cayó del TOP 7).
- Estado real verificado por grep: **casi nada implementado** (todo el TOP 7 sigue pendiente, correctamente bloqueado hasta cerrar re-cert). GOAP A* (de ruflo) ya extraído v3.1 (`goap_planner.py`). Domain prompts P03/P05/P07/P16 existen pero SIN el contenido específico que el doc sugiere (matriz Severity×Likelihood 1-25, decomposiciones variance, security-guide lethal-trifecta, UNIT-PSYCH 80+).
- **Limbo de gobernanza (DECIDIR s19):** 7 conceptos sin clasificar (ni roadmap ni descarte): superpowers (2-stage FORENSE-SPEC/QUALITY review), agency-agents (NEXUS/Quality Gates/Reality-Checker), prompt-master (Memory Block/Diagnostic Checklist), ruflo (Trust ladder/Circuit breaker), spacex (Bull/Bear/Judge + Brier), everything-claude-code (the-security-guide), mempalace/claude-certified-architect. Clasificar explícitamente para no re-evaluar el doc desde cero en cada barrido.

### 3. RE-CERT DS v3.4.0 — COMPLETA ✅
Auditor: PA-agent v1.3.0 (PA-20260527-002 ACTIVE). Level 1 JARP DEEP full-coverage, 5 fases:
- **Fase A** — Self-audit L0 del PA-agent (`PA-20260601-001`): 0/0/0/0, BIAS_CHECK PASS. CERT_REGISTRY_REVIEW coherente. Auditor sano.
- **Fase B** — Base (`system_prompt.md` + `system_prompt_router.md`): 7/7 ejes verdes, 0 findings. Version stamp base↔router↔footer = 3.4.0 coherente.
- **Fase C** — 19/19 variants (P02-P20), §4.14.1 conforme: stamps v3.4.0-DOMAIN, footers 3-line, herencia explícita BLOCK 0-6, severidad monotónica gated, prefijos 2-letras inmutables, BASE→v3.4.0. 0 findings. (Confirma que el bump atómico s17 SÍ alcanzó los 19 variants.)
- **Fase D** — 5 skills (kac/ach/deception/verdict-verification v2.6.0 + adaptive-autonomous-drive v3.2.0, content-based versioning correcto) + product-face `main.py` (3 caras v3.4.0) + 5 docs (CLAUDE/CHANGELOG/industry_taxonomy/micro_agents/severity). 0 findings.
- **Fase E** — Síntesis: 31 targets, 31 PASS, **0 CRITICAL / 0 SERIOUS / 0 MODERATE / 0 LATENT**, conformance 100%, BIAS_CHECK PASS.

**CERT EMITIDO:** `PA-20260601-002` — DS **v3.4.0 JARP_CERTIFIED**, full coverage 19/19, válido hasta **30/08/2026 (90d) o DS v4.0.0**. **SUPERSEDES PA-20260529-001** (v3.3.0). `JARP_BENCHMARK_LIVE` avanza → v3.4.0. Sin cascade (era minor bump).
- **Disciplina de ID:** self-audit `-001` y cert maestro `-002` son IDs diarios separados; el batch usa un solo maestro (-002) con sub-IDs B1/31..B31/31, NO incrementa el contador diario por target.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN — ACTUALIZADO ⚠️⚠️

**DS repo v3.4.0 = CERTIFICADO (`PA-20260601-002`).** El version-gap de s17 (repo v3.4.0 / cert v3.3.0) quedó CERRADO. La cert previa `PA-20260529-001` (v3.3.0) pasa a SUPERSEDED. Afirmar "v3.4.0 está certificado" es ahora correcto.

---

## REGISTRO POST-CERT — PENDIENTE DE APLICAR POR JARP (s18, Ruta-3 + GitHub Desktop)
Emitidos como diffs F&R en s18. **PHASE 0 de s19 debe VERIFICAR que aterrizaron por contenido:**
1. `dark-strategist-agent/CHANGELOG.md` — bloque `[Certification] — 2026-06-01` (PA-20260601-002, full 19/19, supersedes PA-20260529-001).
2. `jarp-toolkit/JARP_TOOLKIT.md` — entry #30 CERT STATUS → CERTIFIED + nota #16 + PA-20260529-001→SUPERSEDED + header.
3. `jarp-toolkit/.claude-init.md` — Nota#7 + header → v3.4.0 CERTIFIED.
4. Continuity v17 (este archivo) — commitear; borrar v16.

---

## OPERACIÓN DE CIERRE v3.4 — ESTADO FINAL
Ítems 1-7 (s17) ✅ + **Fase 4 Re-cert ✅ COMPLETA (s18)**. La operación de cierre v3.4 está **CERRADA**. v3.4.0 shipped + certified.

---

## DEUDA TÉCNICA — POST-SESIÓN 18

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.4.0** | ✅ CERRADA | v3.4.0 CERTIFICADO (PA-20260601-002) | Era el 🔴 GOBERNANZA de s17. Resuelto s18. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Síntesis-LLM viva limpia solo en docs baja densidad; fallback determinista (diseñado) = sintetizador de producción para docs ricos. | No defecto. |
| **DSv34-SHAPE-followup** | 🟢 ACEPTADA (watch) | El fix movió el fallo vivo de Pydantic-shape a JSON-truncation. | Bajo valor (fallback ya es correcto). |
| **clash n=0 vivo** | 🟢 WATCH | Cero clash en inputs sin contradicción Rol/Forense — correcto. | Validar n>0 requiere input diseñado para provocar contradicción fáctica. |
| **BACKLOG-LIMBO** | 🟡 GOBERNANZA | 7 conceptos del barrido sin clasificar (ver §2). | Clasificar en s19 ANTES de tocar integraciones. |

**CERRADAS s18:** re-cert v3.4.0, free-claude-code cableado, evaluación barrido.
**CERRADAS s17:** gate (b) vivo, DSv34-SHAPE/PROV/DEAD, bump v3.4.0, doc cleanup.

---

## ESTADO ACTUAL VERIFICADO (01/06/2026 fin de sesión 18)

### Repo dark-strategist-agent
- **v3.4.0 — CERTIFICADO (`PA-20260601-002`)** full coverage 19/19. Default `claude-opus-4-7`. Código muerto eliminado (s17, 404 confirmado). Helpers locales NO commitear: `orchestrator/smoke_test_e2e.py` v3, `smoke_contract.txt` (Downloads).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. **Fue el auditor de la re-cert s18.** Sin cambios de versión.

### Repo jarp-toolkit
- entry #43 + nota #34 + header actualizados s18 (free-claude-code: 11 backends, zero-code routing, regla free-para-no-cert). Edits post-cert pendientes (ver arriba). PRIVADO (clone anónimo falla; usar mi-filesystem/GitHub MCP).

### free-claude-code
- Disponible como proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

### devil-advocate-agent
- Privado, íntegro, sin cambios.

---

## PROTOCOLO DE INICIO PARA SESIÓN 19
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v17).
2. **PHASE 0 — Verificación:**
   - v16 borrado, v17 único continuity.
   - Repo en v3.4.0. **Cert registry: DS v3.4.0 `PA-20260601-002` ACTIVE** (= certifica v3.4.0). Verificar que los 4 registros post-cert aterrizaron. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260529-001` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 15 SESIONES (4-18).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Integraciones roadmap v3.3/v3.4** — **DESBLOQUEADO** (re-cert hecha). TOP 7: markitdown→UNIT-INGEST, fact-checker→UNIT-FACTCHECK, stop-slop→post-proc AFO, knowledge-work-plugins→matrices, marketingskills→UNIT-PSYCH 80+, Agent-Skills-for-Context-Engineering, infinity→RAG (v4.0). Empezar por los 4× esfuerzo-Bajo (UNIT permanentes). Probar vía free-claude-code a $0. Al cerrar el bump → nueva re-cert que supersede PA-20260601-002.
   - **(C) Gobernanza backlog** — clasificar los 7 ítems en limbo ANTES de (B).
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config (cortes duros `[:N]`) | distinguir clash de severity-escalation.

**De s13-s17:** Sintetizador VIVO = `TribunalTransversal._synthesize`; el fallback determinista es el sintetizador de producción sancionado para docs ricos — NO debilitar el schema `Finding` para forzar parse (el schema estricto es correcto; se ajusta el prompt). | gate `b_unified_output` certifica robustez end-to-end (cualquier vía), NO parse limpio de Opus. | Editor folder-replace NO confiable para barridos multi-archivo → script PowerShell determinista (`UTF8Encoding($false)`, JARP corre + commitea). | Grep de verificación: distinguir stamp-stale de historia-correcta (filas roadmap/cert históricas matchean el patrón y son CORRECTAS). | Pago Anthropic: "Contact sales" ≠ fondear; fondeo self-serve = Console → Plans & Billing → Add funds. | Borrar código muerto NO es aislado si la doc viva lo declara intencional (va en el bump).

**De s18 (nuevas):**
- **free-claude-code: free para no-cert, Opus real para cert.** Integración DS zero-code vía `ANTHROPIC_BASE_URL` (DS no pasa `base_url` → respeta env var). 11 backends. Fijar UN backend por campaña.
- **Re-cert ID discipline:** self-audit L0 y cert maestro = IDs diarios separados; el batch usa UN maestro con sub-IDs por target, no infla el contador diario.
- **Re-cert confirmatoria cuando el bump no toca la superficie auditada:** v3.4.0 tocó síntesis/provenance/dead-code (orquestación), no la capa prompts/skills → 0 findings esperados y obtenidos. La re-cert valida coherencia de stamps + contrato §4.14.1, no corrige.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (taxonomía L01-L12 ya rescatada v3.1) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` para forzar parse (rechazado s17) | "17 backends" en free-claude-code (son 11 — corregido s18).

**NO son descarte (PENDIENTE clasificación s19):** superpowers, agency-agents, prompt-master, ruflo (trust/circuit), spacex (Bull/Bear/Judge/Brier), everything-claude-code (security-guide), mempalace, claude-certified-architect.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v17.md` (v16 a borrar s18)
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md`
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. Sandbox bash clona PÚBLICOS (DS, PA) → `git clone --depth 1` + grep, preferido por eficiencia de tokens. Privados (jarp-toolkit, devil-advocate) clone anónimo falla → mi-filesystem/GitHub MCP.
- **Método de edición = Ruta 3 (F&R explícito)** para archivos committed. Barridos multi-archivo = script PowerShell. Archivos LOCALES/continuity = `mi-filesystem:write_file` (overwrite). `github:create_or_update_file` prohibido por defecto (límite ~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep/get_file_contents del marcador), no solo SHA.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline (sin key) = 11 PASS / 1 SKIP (b) / 0 FAIL. NO commitear el helper ni `smoke_contract.txt`.
- **free-claude-code:** `fcc-server` puerto 8082, Admin UI `/admin`. SMOKE = `api_key:"freecc"` + `$env:ANTHROPIC_BASE_URL=http://localhost:8082`. CERT = `sk-ant-...` real + sin proxy.
- **API:** saldo ≈$1.66 (la re-cert fue $0 — estática). free-claude-code para corridas no-cert a $0. `$env:ANTHROPIC_API_KEY="sk-ant-..."` en PowerShell (NO `setx`). Nunca pedir la key en el chat.

### Commit sugerido para cierre sesión 18 (continuity v17 + borrado v16)
```
docs: continuity v17 (session 18 — DS v3.4.0 JARP_CERTIFIED) + cert registry

Session 18 — three blocks:
1. free-claude-code wired as inference proxy (zero-code DS routing via
   ANTHROPIC_BASE_URL; 11 backends; free-for-non-cert governance rule).
   Toolkit entry #43 + note #34 corrected and pushed.
2. "Barrido sistemático" doc evaluated = source of the v3.3 roadmap (TOP 7);
   superpowers fell off; 7 concepts in governance limbo (classify s19).
3. RE-CERT DS v3.4.0 COMPLETE — Level 1 JARP DEEP full coverage by
   prompt-architect-agent v1.3.0. 31 targets, 0/0/0/0, conformance 100%.

CERT: PA-20260601-002 — DS v3.4.0 JARP_CERTIFIED, valid until 2026-08-30
or v4.0.0. Supersedes PA-20260529-001 (v3.3.0). JARP_BENCHMARK_LIVE -> v3.4.0.

NEW FILE: dark-strategist-continuity-prompt_v17.md (replaces v16).
DELETED:  dark-strategist-continuity-prompt_v16.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 18

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.4.0** | **PA-20260601-002** | **v3.4.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 18 (auto-mejora del próximo Claude)

1. **La re-cert fue confirmatoria, como se predijo.** El bump v3.4.0 tocó síntesis/provenance/dead-code (orquestación), NO la capa de prompts/skills/docs → 0 findings esperados y obtenidos. Cuando un bump no toca la superficie auditada, la re-cert valida coherencia de stamps + contrato §4.14.1, no corrige.
2. **El bump atómico de s17 SÍ alcanzó los 19 variants** — confirmado uno por uno (stamps v3.4.0 + footers + BASE→v3.4.0). El riesgo latente del editor-folder-replace quedó descartado por evidencia. El script PowerShell funcionó.
3. **free-claude-code: integración zero-code confirmada contra el código** (DS no pasa `base_url` → respeta env var). Pero free ≠ apto para cert. Iterar gratis, sellar con Opus.
4. **El documento "Barrido sistemático" ya estaba procesado** — NO re-evaluar desde cero. Su resultado vive en el roadmap de entry #30. Lo único accionable nuevo: clasificar los 7 conceptos huérfanos.
5. **Disciplina de REPORT_ID en batch:** self-audit L0 = su propio ID diario (-001); re-cert = un maestro (-002) con sub-IDs por target.
6. **TRADING: 15 SESIONES POSTERGADO (4-18).** Señalado sin acoso. NO re-confrontar. Si s19 no elige A, asumir prioridad real ≠ escrita.
7. **Integraciones DESBLOQUEADAS** tras la re-cert. Próximo bump (¿v3.5?) arranca por los 4 UNIT permanentes esfuerzo-Bajo, probados vía free-claude-code a $0, y al cerrar → nueva re-cert que supersede PA-20260601-002.
