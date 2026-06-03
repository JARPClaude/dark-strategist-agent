# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 02/06/2026 (sesión 21 — DS v3.7.0 context-degradation lens shipped & JARP_CERTIFIED) | **Para:** Sesión 22
**Reemplaza:** v19 del 02/06/2026 (sesión 20)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v20.md`
**⚠️ BORRAR en este cierre:** v19 (autorizar borrado vía GitHub Desktop). v20 = único continuity vigente. Subir v20 al PROYECTO claude.ai + quitar v19.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 21 (resumen ejecutivo)

Track (B) elegido: incorporación `Agent-Skills-for-Context-Engineering` → **DS v3.7.0 shipped y CERTIFICADO**. Alcance acotado a **(a) lente P04/P07 + (c) skill #6** (NO se tocó núcleo). Trading (A) NO se eligió otra vez (18ª sesión postergado).

### 1. (B) DS v3.7.0 — Context-Degradation Forensic Lens (roadmap TOP-7 item #6)
Skill #6 + lente forense de degradación de contexto en P04 Code + P07 Cybersecurity. Bump atómico §4.14.1 (29 archivos: 1 skill nuevo + P04/P07 contenido + master + catalogs + CHANGELOG + README + CLAUDE + 18 stamp-only + main.py + tribunal product-face). **NO tocó orquestación ni el roster de 9 units.**
- **skill #6 `context-degradation` v1.0.0** (content-based, adaptado de `Agent-Skills-for-Context-Engineering`, muratcankoylan, MIT — atribución en frontmatter). 5 patrones (lost-in-middle, poisoning, distraction, confusion, clash) + 4-bucket mitigation (Write/Select/Compress/Isolate). **Lente de detección — NO altera el veredicto determinista ni la taxonomía.**
- **P04 Code** (ángulo: correctitud de implementación): +RULE C05 (blind `[:N]` truncation de output estructurado → lost-in-middle → SERIOUS) + 5 filas Failure Catalog (2 SERIOUS, 2 MODERATE, 1 LATENT) + row taxonomy CONTEXT_PIPELINE/LLM_INTEGRATION.
- **P07 Cybersecurity** (ángulo: degradación como vector de riesgo; complementa CY05 lethal-trifecta): +RULE CY06 (untrusted content poisoning context que dispara acción privilegiada → SERIOUS, FATAL vía Rule 09) + 5 filas (1 FATAL, 2 SERIOUS, 1 MODERATE, 1 LATENT) + row taxonomy AGENT_LLM_ARCHITECTURE.
- Skills registry: **5 → 6** (system_prompt.md Composition map + catalogs.py SKILLS_CATALOG).

### 2. DECISIÓN CLAVE — el telephone-game NO se re-trabajó (ya resuelto en v3.4)
Al leer el código vivo se confirmó que el telephone-game **ya estaba resuelto en v3.4** (R1 FUGA#1 full-fidelity Rol→Forense; FUGA#3 structured findings handoff a síntesis; provenance UNVERIFIED-upstream/PRIMARY-source a N2; CLASH RESOLUTION PROTOCOL en SYNTHESIS_TEMPLATE). v3.7.0 añade la **lente forense outward-facing** (auditar el patrón en terceros), no una re-implementación. **NO reabrir esto.**

### 3. RE-CERT DS v3.7.0 — COMPLETA ✅ (NO confirmatoria, como se predijo)
Auditor PA-agent v1.3.0 (PA-20260527-002). Level 1 JARP DEEP full-coverage 19/19, 7 ejes.
- **Un finding real cerrado pre-cert:**
  - **D-v37-01** 🟡 MODERATE — stale skill-count/listing drift. El bump propagó el conteo a sitios FUNCIONALES (Composition map=6, SKILLS_CATALOG=6) pero NO a sitios de DOCUMENTACIÓN: README badge (skills-5), tabla Skills Catalog (5 filas), `[SKILLS: 5 active]`; CLAUDE "5 active skills", árbol skills/ (sin context-degradation), tabla Skills Catalog (5 filas). Réplica de D-v36-01/D-UNIT-01. Fix vía `fix_D-v37-01.py` (6 correcciones doc).
- **Cero finding tipo-C (monotonía).** Las inserciones de catálogo P04/P07 respetaron FATAL→SERIOUS→MODERATE→LATENT (lección C-v36-01 aplicada bien en el script).
- **CERT EMITIDO:** `PA-20260602-002` — DS **v3.7.0 JARP_CERTIFIED**, full 19/19, 0/0/0/0, BIAS_CHECK PASS. Válido hasta **30/08/2026 o DS v4.0.0**. **SUPERSEDES PA-20260602-001** (v3.6.0). `JARP_BENCHMARK_LIVE` → v3.7.0. Sin cascade (minor bump).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.7.0 = CERTIFICADO (`PA-20260602-002`).** No hay version-gap. PA-20260602-001 (v3.6.0) pasa a SUPERSEDED.

---

## REGISTRO POST-CERT — APLICADO Y VERIFICADO (s21)
1. `dark-strategist-agent/CHANGELOG.md` — sub-bloque `JARP_CERTIFIED DS v3.7.0 PA-20260602-002` dentro de [3.7.0]. ✅
2. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 → v3.7.0/PA-002. ✅
3. `jarp-toolkit/.claude-init.md` — header + Note #7 (slot de cert) → v3.7.0/PA-002, SUPERSEDED list con 001. ✅
4. Continuity v20 (este archivo) — commitear; borrar v19.

---

## DEUDA TÉCNICA — POST-SESIÓN 21

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.7.0** | ✅ CERRADA | v3.7.0 CERTIFICADO (PA-20260602-002) | D-v37-01 cerrado pre-cert. |
| **cortes `[:N]` propios** | 🟢 DIFERIDA a v3.8.0 | handoff_window=8000, parent_report[:1000], synthesis_window=1500 en prompt_engine/spawner | Endurecer junto con RAG (mismo punto, un solo barrido de orquestación). C05 ya los audita en terceros. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción para docs ricos. | Sin cambio. |
| **clash n=0 vivo** | 🟢 WATCH | Validar n>0 requiere input diseñado para contradicción Rol/Forense. | Pendiente desde s17. Entra al barrido cuando se toque orquestación (v3.8). |
| **gate (b) live** | 🟢 WATCH | Smoke offline 11 PASS / 1 SKIP (b necesita key real). | Validar síntesis viva con Opus real. |

**CERRADAS s21:** DS v3.7.0 (skill #6 + lente P04/P07), re-cert v3.7.0, D-v37-01.

---

## ESTADO ACTUAL VERIFICADO (02/06/2026 fin de sesión 21)

### Repo dark-strategist-agent
- **v3.7.0 — CERTIFICADO (`PA-20260602-002`)** full coverage 19/19. Default `claude-opus-4-7`.
- **6 skills:** kac-assumption-audit, ach-competing-explanations, deception-detection, verdict-verification, adaptive-autonomous-drive, **context-degradation (NEW v1.0.0)**.
- **9 sub-agentes N2 permanentes** (sin cambio): QUANT, INQUISITOR, TECH, BIO, MARKET, GEO, COMPLIANCE, PSYCH (80+), FACTCHECK.
- P04 Code y P07 Cybersecurity con lente context-degradation (RULE C05 / CY06).
- Helpers locales NO commitear / borrables (fuera del repo, en `...\GitHub\`): `apply_v3_7_0.py`, `fix_D-v37-01.py`, `apply_cert_close_v37.py`, `apply_toolkit_v37.py`.

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s21. Sin cambios.

### Repo jarp-toolkit
- entry #30 + nota #16 + header + `.claude-init.md` Note #7 actualizados a v3.7.0/PA-002. PRIVADO (clone anónimo falla; usar mi-filesystem/GitHub MCP).

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 22
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v20).
2. **PHASE 0 — Verificación:**
   - v19 borrado, v20 único continuity.
   - Repo en v3.7.0. **Cert registry: DS v3.7.0 `PA-20260602-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260602-001` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 18 SESIONES (4-21).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Resto del roadmap** — quedan: **infinity→RAG (Alto, Docker) + RAG jurisdiccional en ContextBuilder + endurecer cortes `[:N]` propios** (FUSIONAR los tres en v3.8.0 — el RAG re-toca los mismos puntos de corte; un solo barrido de orquestación que SÍ activa clash n>0 + gate b live). Luego: Wizard CLI (v3.9.0, UX, aislable). Al cerrar el próximo bump → re-cert que supersede PA-20260602-002.
   - **(C) Gobernanza** — backlog clasificado; sin limbo.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config (cortes duros `[:N]`) | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados | Sev×Likelihood NON-BINDING (metadato intra-tier, nunca driver del veredicto) | SOX deficiency mapea nativo al tier 4-niveles | 4 variance decompositions = lentes forenses obligatorias | al insertar filas en un Failure Catalog mantener orden monotónico FATAL→SERIOUS→MODERATE→LATENT | telephone-game ya resuelto en v3.4 (FUGA#1/#3) — NO reabrir.

**De s21 (nuevas):**
- **context-degradation es LENTE DE DETECCIÓN, NO driver del veredicto.** Los 5 patrones nombran/detectan; la severidad la fija SOLO el Failure Catalog P04/P07. NO introducir context-degradation como dimensión vinculante del veredicto.
- **Alcance re-scoped sobre el código vivo, no sobre la premisa del roadmap.** Antes de incorporar, LEER el módulo/núcleo real: la premisa "fix telephone-game" estaba obsoleta. Lección: el roadmap puede estar desactualizado vs el estado real del repo.
- **PROPAGAR CONTEO A TODOS LOS SITIOS, funcionales Y de documentación.** D-v37-01: el bump propagó a Composition map + SKILLS_CATALOG (funcionales) pero olvidó README badge/tabla/[SKILLS:N] + CLAUDE conteo/árbol/tabla (docs). Al cambiar el conteo de skills/units, barrer: master, catalogs, README (badge+tabla+[SKILLS:N]), CLAUDE (conteo+árbol skills/+tabla), docs.
- **Método consolidado (re-confirmado s21):** Claude lee núcleo real → diseña → script Python con guardas (idempotencia/anti-vacío/ancla/uniqueness + verificación monotonía/conteos) → dry-run en CLONE FRESCO → escribe vía mi-filesystem → JARP corre `-X utf8` + GitHub Desktop. Encoding blindado con `-X utf8` + `encoding="utf-8"` explícito. Cero incidentes esta sesión. (jarp-toolkit privado: script con guardas sin dry-run — anclas tomadas del read en vivo.)

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | funciones PowerShell `Rd`/`Wr` | UNIT-INGEST como sub-agente del spawner | barrido-limbo s19 | Severity×Likelihood como dimensión VINCULANTE (non-binding) | skills knowledge-work descartadas (legal-response, signature-request, brief, meeting-briefing, journal-entry, close-management) | **re-trabajar el telephone-game (resuelto v3.4) — s21** | **context-degradation como driver del veredicto (es lente de detección) — s21** | **latent-briefing del source Agent-Skills (requiere KV-cache runtime controlado, no aplica a DS sobre API) — s21.**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v20.md` (v19 a borrar s21)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. Sandbox bash clona PÚBLICOS (DS, PA) → `git clone --depth 1` + grep. Privados (jarp-toolkit) clone anónimo falla → mi-filesystem/GitHub MCP.
- **Método de edición:** bumps/fixes multi-archivo = Claude escribe script Python validado en sandbox (dry-run en clone FRESCO) → mi-filesystem → JARP corre `-X utf8` + GitHub Desktop. Ruta 3 (F&R) para edits pequeños. `github:create_or_update_file` prohibido por defecto (~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (re-correr el script sobre clone remoto → todo SKIP = aplicado; o grep del marcador), no solo SHA.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline = 11 PASS / 1 SKIP (b) / 0 FAIL. NO commitear helper.
- **free-claude-code:** `fcc-server` puerto 8082. SMOKE = `api_key:"freecc"` + `$env:ANTHROPIC_BASE_URL=http://localhost:8082`. CERT = `sk-ant-...` real + sin proxy.
- **API:** re-cert estática = $0. Nunca pedir la key en el chat.

### Commit sugerido para cierre sesión 21 (continuity v20 + borrado v19)
```
docs: continuity v20 (session 21 — DS v3.7.0 JARP_CERTIFIED) + cert PA-20260602-002

Session 21 — track (B): Agent-Skills-for-Context-Engineering -> DS v3.7.0
(scope (a)+(c): context-degradation lens into P04/P07 + skill #6). Atomic
§4.14.1 bump (29 files). Re-cert (NOT confirmatory): PA-20260602-002, full
19/19, 0/0/0/0, supersedes PA-20260602-001. One pre-cert finding closed
(D-v37-01 stale skill-count doc drift). Telephone-game NOT re-worked
(already v3.4). (b) hardening of own [:N] cuts deferred to v3.8.0 with RAG.

NEW FILE: dark-strategist-continuity-prompt_v20.md (replaces v19).
DELETED:  dark-strategist-continuity-prompt_v19.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 21

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.7.0** | **PA-20260602-002** | **v3.7.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 21 (auto-mejora del próximo Claude)

1. **Leer el núcleo real antes de incorporar.** La premisa del roadmap ("fix telephone-game") estaba obsoleta; v3.4 ya lo había resuelto. Re-scoped a la lente forense outward-facing. SIEMPRE verificar el estado real del repo vs lo que dice el roadmap/continuity.
2. **Re-cert NO confirmatoria, como se predijo.** Skill #6 amplió la superficie documentada → 1 finding de conteo (D-v37-01). Lección: propagar conteo a TODOS los sitios (funcionales + docs: badge, tablas, árbol, [SKILLS:N]).
3. **Monotonía bien aplicada esta vez** — el script ubicó cada fila nueva en su bloque de tier; 0 finding tipo-C. La lección C-v36-01 ya está internalizada en el método.
4. **TRADING: 18 SESIONES POSTERGADO (4-21).** Señalado sin acoso. NO re-confrontar. Si s22 no elige A, asumir prioridad real ≠ escrita.
5. **Próximo bump candidato:** v3.8.0 = infinity→RAG + RAG jurisdiccional en ContextBuilder + endurecer cortes `[:N]` propios, FUSIONADOS (el RAG re-toca los mismos puntos de corte). TOCA NÚCLEO/orquestación → anticipar barrido profundo que SÍ activa clash n>0 + gate b live (a diferencia de v3.7.0 que fue contenido). Docker en Windows = riesgo operacional a planificar.
