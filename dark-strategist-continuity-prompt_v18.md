# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 01/06/2026 (sesión 19 — gobernanza barrido + v3.5.0 shipped & JARP_CERTIFIED) | **Para:** Sesión 20
**Reemplaza:** v17 del 01/06/2026 (sesión 18)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v18.md`
**⚠️ BORRAR en este cierre:** v17 (autorizar borrado vía GitHub Desktop). v18 = único continuity vigente. Subir v18 al PROYECTO claude.ai + quitar v17.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 19 (resumen ejecutivo)

Dos bloques cerrados: **(C) Gobernanza del backlog del barrido** + **(B) primer lote de integraciones → DS v3.5.0 shipped y CERTIFICADO**. Trading (A) NO se eligió otra vez (16ª sesión postergado).

### 1. (C) Gobernanza — barrido-limbo RESUELTO
Los 7 conceptos huérfanos del documento "Barrido sistemático" quedaron clasificados explícitamente en `JARP_TOOLKIT.md` entry #30 (1 ROADMAP / 6 DESCARTE). **No re-evaluar nunca más:**
- **ROADMAP:** lethal-trifecta (everything-claude-code/the-security-guide) → contenido P07 Cybersecurity. (YA implementado en v3.5.0.)
- **DESCARTE (6):** superpowers (redundante con Tribunal+verdict-verification+AAD); agency-agents (NEXUS/Quality-Gates/Reality-Checker → AFO/veredicto determinista/deception-detection+kac); prompt-master (tooling prompt-eng; checklist ya en PA-agent); ruflo (circuit-breaker ya en SafetyGuard+caps; trust-ladder choca con hard-caps); spacex Bull/Bear/Judge (redundante) + Brier (inaplicable sin outcomes realizados; reconsiderar solo ≥v4.0); mempalace + claude-certified-architect (memory-tooling/cert-prep, sin contacto forense).

### 2. (B) Integraciones — DS v3.5.0 (5 capacidades, lote esfuerzo-Bajo del TOP 7 + lethal-trifecta)
Construido en 3 grupos (G1 código nuevo, G2 contenido+post-proc, G3 bump atómico):
- **UNIT-INGEST** (`orchestrator/ingest.py`) — preprocesador markitdown (PDF/DOCX/PPTX/XLSX/HTML→Markdown). **NO es un finding-emitter** (decisión D1: va en el punto de carga de `main.py`, NO en el spawner — markitdown convierte, no audita). Degrada con gracia sin markitdown instalado (ImportError→raw read). Hook: `main.py` document load.
- **UNIT-FACTCHECK** (`sub_agent_spawner.py`) — 9º sub-agente N2 permanente. Valida claims/estadísticas/fuentes. Anti-fabricación (marca UNVERIFIED). Trigger: claim/study/statistic/source.
- **UNIT-PSYCH 80+** — catálogo de sesgos ~15→80+ en 8 familias. Prompt operativo en spawner + referencia anotada `docs/psych_bias_catalog.md`.
- **stop-slop** (`orchestrator/slop_filter.py`) — scorer de prosa 5-dim, stdlib-only (sin LLM/red), **score-only** (nunca muta findings/veredicto). Threshold 35/50; **cualquier dimensión saturada (==0) fuerza REVIEW** (calibración añadida tras smoke). Hook: cola de `_build_transparency_report` → bloque PROSE QUALITY advisory.
- **lethal-trifecta → P07** — `system_prompt_cybersecurity.md`: RULE CY05 (FATAL) + 2 filas Failure Catalog (trifecta completa=FATAL, 2-patas=SERIOUS), monotónicas.
- **Fix colateral:** `cloud_function/main.py` DS_MODEL default `claude-opus-4-6`→`claude-opus-4-7` (coherencia A6).

### 3. RE-CERT DS v3.5.0 — COMPLETA ✅ (NO confirmatoria, como se predijo)
Auditor PA-agent v1.3.0 (PA-20260527-002). Level 1 JARP DEEP full-coverage. 5 fases A–E, 31 targets, 31 PASS.
- **Dos findings reales hallados y cerrados pre-cert** (la superficie ampliada generó drift):
  - **C-P07-01** 🔵 LATENT — el Failure Catalog de P07 perdió el orden monotónico (fila FATAL bajo bloque SERIOUS). Fix: reorden a bloques FATAL(4)→SERIOUS(5)→MODERATE(3) (commit `0a234ff`).
  - **D-UNIT-01** 🟡 MODERATE — añadir UNIT-FACTCHECK dejó 5 refs stale al conteo "8 units" (3 en `system_prompt.md`, 2 en `micro_agents_catalog.md`); el doc tampoco listaba FACTCHECK ni el PSYCH 80+. Fix: 8→9 en todos + bloque FACTCHECK + PSYCH actualizado en el doc (commit `3d1c29e`).
- **CERT EMITIDO:** `PA-20260601-004` — DS **v3.5.0 JARP_CERTIFIED**, full coverage 19/19, 0/0/0/0, BIAS_CHECK PASS. Válido hasta **30/08/2026 o DS v4.0.0**. **SUPERSEDES PA-20260601-002** (v3.4.0). `JARP_BENCHMARK_LIVE` → v3.5.0. Sin cascade (minor bump).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.5.0 = CERTIFICADO (`PA-20260601-004`).** No hay version-gap. Afirmar "v3.5.0 está certificado" es correcto. PA-20260601-002 (v3.4.0) pasa a SUPERSEDED.

---

## REGISTRO POST-CERT — APLICADO Y VERIFICADO (s19)
Los 3 sitios verificados por contenido en remoto:
1. `dark-strategist-agent/CHANGELOG.md` (`4d4a338`) — bloque `[Certification]` PA-20260601-004 + status line `v3.5.0 CERTIFIED`. ✅
2. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 (Version/CERT STATUS/Previous certs) + Note #16 → v3.5.0/PA-004. ✅
3. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.5.0/PA-004, SUPERSEDED list con 002. ✅
4. Continuity v18 (este archivo) — commitear; borrar v17.

---

## DEUDA TÉCNICA — POST-SESIÓN 19

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.5.0** | ✅ CERRADA | v3.5.0 CERTIFICADO (PA-20260601-004) | C-P07-01 + D-UNIT-01 cerrados pre-cert. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción para docs ricos. | Sin cambio en v3.5.0. |
| **clash n=0 vivo** | 🟢 WATCH | Validar n>0 requiere input diseñado para provocar contradicción Rol/Forense. | Pendiente desde s17. |
| **gate (b) live** | 🟢 WATCH | Smoke offline 11 PASS / 1 SKIP (b necesita key real). El SKIP es estado aceptado (DSv34-SYNTH). | Para validar síntesis viva con doc rico: correr con Opus real (no free). |
| **UNIT-PSYCH doc legacy** | 🟢 RESUELTA | El doc `micro_agents_catalog.md` ya refleja 80+ (cerrado en D-UNIT-01). | — |

**CERRADAS s19:** gobernanza barrido (1 roadmap/6 descarte), DS v3.5.0 (5 capacidades), re-cert v3.5.0, C-P07-01, D-UNIT-01.

---

## ESTADO ACTUAL VERIFICADO (01/06/2026 fin de sesión 19)

### Repo dark-strategist-agent
- **v3.5.0 — CERTIFICADO (`PA-20260601-004`)** full coverage 19/19. Default `claude-opus-4-7`.
- **9 sub-agentes N2 permanentes** (era 8): QUANT, INQUISITOR, TECH, BIO, MARKET, GEO, COMPLIANCE, PSYCH (80+), **FACTCHECK (nuevo)**.
- Nuevos módulos: `orchestrator/ingest.py` (UNIT-INGEST preproc), `orchestrator/slop_filter.py` (stop-slop score-only), `docs/psych_bias_catalog.md` (80+ sesgos).
- Helpers locales NO commitear: `orchestrator/smoke_test_e2e.py` v3, `smoke_contract.txt` (Downloads). Helper `bump_3_5_0.ps1` quedó en `...\GitHub\` (FUERA del repo) — borrable.

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Fue el auditor de la re-cert s19. Sin cambios.

### Repo jarp-toolkit
- entry #30 + Note #16 + header + `.claude-init.md` actualizados a v3.5.0/PA-004. barrido-limbo resuelto en entry #30. PRIVADO (clone anónimo falla; usar mi-filesystem/GitHub MCP).

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 20
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v18).
2. **PHASE 0 — Verificación:**
   - v17 borrado, v18 único continuity.
   - Repo en v3.5.0. **Cert registry: DS v3.5.0 `PA-20260601-004` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260601-002` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 16 SESIONES (4-19).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Resto del roadmap v3.3/v3.4** — los 5 esfuerzo-Bajo YA están en v3.5.0. Quedan: knowledge-work-plugins (matriz 1-25 + 4 decomp. financieras, Medio), Agent-Skills-for-Context-Engineering (context degradation + fix telephone-game AFO, Medio), infinity→RAG (Alto, Docker), Wizard CLI, RAG jurisdiccional en ContextBuilder. Al cerrar el próximo bump → re-cert que supersede PA-20260601-004.
   - **(C) Gobernanza** — backlog ya clasificado; no hay limbo pendiente.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config (cortes duros `[:N]`) | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end (cualquier vía), NO parse limpio de Opus | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados.

**De s19 (nuevas):**
- **UNIT-INGEST NO es un finding-emitter.** Es preproceso de documento (markitdown) en el punto de carga (`main.py`), NO un sub-agente del spawner. Convertir ≠ auditar — meterlo en `PERMANENT_SUBAGENTS` rompería el contrato de unit. Degrada con gracia (sin markitdown → raw read; nunca crashea el pipeline).
- **stop-slop es score-only, stdlib-only.** Anota score 5-dim + flag en el Transparency Report; **nunca** reescribe findings ni veredicto. Sin LLM/red → corre igual en free u Opus, cero superficie de síntesis añadida. Calibración: cualquier dimensión saturada (==0) fuerza REVIEW (no basta el threshold agregado).
- **9 sub-agentes N2 permanentes** (FACTCHECK añadido). Conteo coherente en spawner (autoritativo) ↔ `system_prompt.md` roster ↔ `micro_agents_catalog.md`. Al añadir/quitar un unit, propagar el conteo a los 3 sitios (lección D-UNIT-01).
- **El spawner es la fuente autoritativa del roster.** Los docs (`system_prompt.md`, `micro_agents_catalog.md`) deben sincronizarse a él, no al revés.
- **Re-cert NO confirmatoria cuando el bump amplía superficie auditada** (nuevos units/contenido) → esperar findings reales de coherencia (orden de catálogo, conteos). Distinto de v3.4.0 (orquestación, no tocó prompts → confirmatoria).
- **PowerShell aprende de s19:** (1) `Rd`/`rd` es ALIAS nativo de `Remove-Item` y los alias ganan a las funciones → NUNCA nombrar funciones helper `Rd`/`Wr`/etc.; usar `Read-RepoFile`/`Write-RepoFile`. (2) Guarda anti-vacío obligatoria (rehúsa escribir string vacío) → imposible blanquear archivos. (3) Correr como ARCHIVO (`-File`), no pegar línea por línea (el paste interactivo ignora `$ErrorActionPreference='Stop'` y cascadea). (4) El `.ps1` debe EXISTIR en disco antes de `-File`. (5) **Método preferido para bumps multi-archivo ahora: Claude escribe los archivos vía mi-filesystem tras validar en sandbox Python** — más verificable que PowerShell, inmune a encoding/alias. PS queda como fallback. (6) Verificar SIEMPRE anclas con backticks/emoji incluidos (el router-ref `\`...\`` casi queda stale).

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (taxonomía ya rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` para forzar parse | "17 backends" free-claude-code (son 11) | **funciones PowerShell nombradas `Rd`/`Wr` (colisión con alias Remove-Item)** | **UNIT-INGEST como sub-agente del spawner (es preproceso, no auditor)** | **barrido-limbo: superpowers, agency-agents, prompt-master, ruflo, spacex, mempalace, claude-certified-architect (clasificados DESCARTE en s19 — NO re-evaluar).**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v18.md` (v17 a borrar s19)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. Sandbox bash clona PÚBLICOS (DS, PA) → `git clone --depth 1` + grep, preferido por eficiencia de tokens. Privados (jarp-toolkit, devil-advocate) clone anónimo falla → mi-filesystem/GitHub MCP.
- **Método de edición:** Ruta 3 (F&R explícito) para archivos committed pequeños. **Bumps multi-archivo: Claude escribe vía mi-filesystem tras validar en sandbox Python** (preferido sobre PowerShell desde s19). `github:create_or_update_file` prohibido por defecto (límite ~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep/get_file_contents del marcador), no solo SHA.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline (sin key) = 11 PASS / 1 SKIP (b) / 0 FAIL. NO commitear el helper ni `smoke_contract.txt`.
- **free-claude-code:** `fcc-server` puerto 8082, Admin UI `/admin`. SMOKE = `api_key:"freecc"` + `$env:ANTHROPIC_BASE_URL=http://localhost:8082`. CERT = `sk-ant-...` real + sin proxy.
- **API:** la re-cert fue $0 (estática). free-claude-code para corridas no-cert a $0. `$env:ANTHROPIC_API_KEY="sk-ant-..."` en PowerShell (NO `setx`). Nunca pedir la key en el chat.

### Commit sugerido para cierre sesión 19 (continuity v18 + borrado v17)
```
docs: continuity v18 (session 19 — DS v3.5.0 JARP_CERTIFIED) + close governance + integrations

Session 19 — two blocks:
1. (C) Governance: barrido-limbo resolved in toolkit entry #30 — 1 ROADMAP
   (lethal-trifecta -> P07, implemented) / 6 DISCARD. No more re-evaluation.
2. (B) Integrations: DS v3.5.0 shipped — 5 low-effort roadmap items
   (UNIT-INGEST, UNIT-FACTCHECK, UNIT-PSYCH 80+, stop-slop, lethal-trifecta P07)
   + cloud DS_MODEL fix. Atomic §4.14.1 bump 3.4.0 -> 3.5.0 (27 files).
   Re-cert (NOT confirmatory): PA-20260601-004, full 19/19, 0/0/0/0, supersedes
   PA-20260601-002. Two pre-cert findings closed (C-P07-01, D-UNIT-01).

NEW FILE: dark-strategist-continuity-prompt_v18.md (replaces v17).
DELETED:  dark-strategist-continuity-prompt_v17.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 19

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.5.0** | **PA-20260601-004** | **v3.5.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 19 (auto-mejora del próximo Claude)

1. **PowerShell falló dos veces por un error de naming mío** (`Rd`→alias `Remove-Item`). Lección sistémica: para bumps multi-archivo, **escribir vía mi-filesystem tras validar en sandbox Python** es más confiable y verificable que generar `.ps1`. PS quedó como fallback con guarda anti-vacío + nombres no-alias + correr como archivo.
2. **La re-cert fue NO confirmatoria, como se predijo** — la superficie ampliada (9º unit, P07, slop) generó 2 findings reales de coherencia (orden de catálogo, conteo de units). Cuando un bump añade units/contenido, anticipar drift de conteo/orden y barrerlo ANTES de la cert.
3. **El spawner es autoritativo para el roster de units.** Al añadir/quitar uno, propagar el conteo a `system_prompt.md` (3 refs) + `micro_agents_catalog.md` (2 refs + bloque). D-UNIT-01 fue exactamente esto.
4. **UNIT-INGEST no es del spawner** — es preproceso (markitdown) en `main.py`. Convertir ≠ auditar. No moverlo al spawner "para que sea un UNIT como los demás".
5. **stop-slop score-only** — nunca dejar que mute findings/veredicto; stdlib-only para no añadir superficie de síntesis. Calibración: dimensión saturada fuerza REVIEW.
6. **TRADING: 16 SESIONES POSTERGADO (4-19).** Señalado sin acoso. NO re-confrontar. Si s20 no elige A, asumir prioridad real ≠ escrita.
7. **Próximo bump** (¿v3.6?): los esfuerzo-Medio del TOP 7 (knowledge-work-plugins, Agent-Skills-for-Context-Engineering) o el Alto (infinity→RAG). Probar vía free-claude-code a $0; sellar con Opus; re-cert que supersede PA-20260601-004.
