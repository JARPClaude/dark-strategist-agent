# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 28/05/2026 (sesión 9 — deuda q cerrada + Bloque 1 v3.3 parcial: 6 Legal catalogs) | **Para:** Sesión 10
**Reemplaza:** v7 del 27/05/2026 (sesión 8)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v8.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 9 (resumen ejecutivo)

Sesión 9 cerró **deuda q** (higiene de cert registry) y ejecutó la **sub-fase L-catalogs del Bloque 1 del Sprint v3.3**. Además produjo un **hallazgo crítico sobre la deuda n** que reformula cómo se ataca el resto del sprint.

**Resultados principales:**

1. **PHASE 0 detectó cert registry stale.** Los archivos de autorun (`JARP_TOOLKIT.md` entry #42 + `.claude-init.md` nota #7) seguían referenciando PA-agent **v1.2.0 / PA-20260525-002** como ACTIVE — congelados al 26/05, un día antes del cierre de sesión 8. El estado real (verificado contra el CHANGELOG remoto del PA-agent, tiebreaker canónico) era **v1.3.0 / PA-20260527-002**. La deuda **q** se reclasificó de cosmética (🟢 LOW "considerar añadir entry") a higiene real de cert registry (🟡 MODERATE), porque alimentaba el `CERT_REGISTRY_REVIEW` del PA-agent con datos incorrectos en cada arranque. **Corrección de auto-auditoría:** la nota #7 de sesión 8 que afirmaba "JARP_TOOLKIT.md NO tiene entry para PA-agent" era falsa — el entry #42 sí existía, solo estaba obsoleto en versión.

2. **PHASE 1 — Decisión de roadmap.** JARP consideró (E) audit real y eligió **(B) Sprint v3.3 DS**. Trading (A) postergado **6ª sesión consecutiva (4-5-6-7-8-9)**.

3. **Deuda q CERRADA (cert registry consistente).** Vía Ruta 3, 3 commits en repo `jarp-toolkit`:
   - `JARP_TOOLKIT.md` entry #42: v1.2.0 → v1.3.0, cert PA-20260527-002, v1.3.0 additions, ambos certs previos SUPERSEDED. Headers bumpeados.
   - `.claude-init.md` nota #7: cert registry → v1.3.0 / PA-20260527-002. Header bumpeado.
   - Fix cosmético: blank line restaurada antes del `---` de cierre del entry #42 (evitaba render setext H2). SHA final `2905933`.
   - Notas #31/#32 NO tocadas (enunciados de procedencia histórica "added in v1.2.0", correctos — no stale).

4. **Bloque 1 Sprint v3.3 (PARCIAL) — 6 Legal Failure Catalogs entregados.** `prompts/system_prompt_legal.md`: insertados L05 Product, L06 Regulatory, L09 Litigation, L10 Real Estate, L11 Finance, L12 Public Regulatory en orden numérico (L05+L06 entre L04 y L07; L09-L12 entre L08 y WAR ROOM). ~30 rows. Calibración espejo de catalogs vivos (FATAL = unenforceable / regulatory violation / catastrophic). 2 ediciones colaterales: nota de taxonomía + línea OUTPUT FORMAT (forward-references a v3.3 eliminadas). **Severity Mapping Contract satisfecho** — "No warranty disclaimer" se calibró SERIOUS (no FATAL) por consistencia con L01 "No limitation of liability". Verificado: SHA `e7e4472` → `0a04ea1`, 12.402 → 15.208 bytes. **Version strings INTACTOS (3.2.2-LEGAL)** por §4.14.1 Versioning Contract — ver decisión arquitectónica abajo.

5. **🔴 HALLAZGO CRÍTICO — el backlog "38 MODERATE + 23 LATENT" NO existe itemizado.** Se buscó en `dark-strategist-agent/docs/` (8 docs de arquitectura), CHANGELOG de DS (canónico per governance), y raíz de `prompt-architect-agent` (el auditor). El registro enumerado B1–B9 de sesión 5 nunca se commiteó. Solo existe el resumen en prosa del CHANGELOG `[3.2.2]` → "Findings deferred to v3.3", con ejemplos + "etc." Y ese agregado está **stale/parcialmente resuelto**:
   - Los Legal catalogs L05-L12 cerrados HOY estaban listados ahí como MODERATE diferido → el contador ya no es 38.
   - Un ítem listado es del PA-agent y ya está resuelto: *"multi-day batch resumption rules in prompt-architect-agent"* → cerrado en PA-agent v1.2.0 (sesión 7). Mal ubicado Y obsoleto.
   - Un LATENT listado ya está resuelto: B2-RE.1 (*"'v2.5.1 forensic base' wording"*) → `system_prompt.md` hoy dice v3.2.2.
   - **Conclusión:** "atacar las 32 MODERATE restantes" no es accionable como está formulada. Perseguir un registro perdido o completarlo de memoria viola RULE 06 (NO CRITICAL HALLUCINATIONS) y la userPref "no inventes datos". El backlog residual real debe **regenerarse vía self-audit** (PA-agent v1.3.0 Level 1 sobre DS), no recuperarse.

---

## ESTADO ACTUAL VERIFICADO (28/05/2026 fin de sesión 9)

### Repo dark-strategist-agent
- **Local:** v3.2.2 ✅ + 6 Legal catalogs nuevos
- **Remoto:** v3.2.2 + Legal catalogs L05-L12 pusheados ✅ (commit del 28/05, SHA legal `0a04ea1`)
- **Local sin push (al generar este v8):** este propio archivo `dark-strategist-continuity-prompt_v8.md` (deuda **s** — JARP commitea vía GitHub Desktop)
- **Estado cert:** **`PA-20260525-001` ACTIVE — JARP_CERTIFIED** (válida hasta 23/08/2026 o v4.0.0)
- **Sprint v3.3 EN PROGRESO:** Legal catalogs commiteados mid-sprint bajo stamp `3.2.2-LEGAL`. Version bump a v3.3.0 NO aplicado todavía (operación atómica de cierre — ver decisiones arquitectónicas).
- **Default model:** `claude-opus-4-7`

### Repo prompt-architect-agent
- **Local/Remoto:** v1.3.0 ✅
- **Estado cert:** **`PA-20260527-002` ACTIVE — JARP_CERTIFIED** (válida hasta 25/08/2026 o v2.0.0)
- **Sin cambios en sesión 9.**

### Repo jarp-toolkit ⭐ ACTUALIZADO SESIÓN 9
- **Local/Remoto:** ✅ cert registry consistente (deuda q cerrada)
- `JARP_TOOLKIT.md` SHA `2905933`. `.claude-init.md` SHA `9a05362`.
- Entry #42 PA-agent ahora en v1.3.0 / PA-20260527-002.

### Repo sap-abap-intelligence-agent
- Sin cambios desde sesión 5.

### Repo devil-advocate-agent
- Copia manual sin `.git/` (deuda g LOW, sin tocar).

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 9

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **s** | 🟡 MODERATE (operativo) | Push del continuity v8 en repo DS | Bajo | JARP vía GitHub Desktop al cierre sesión 9 |
| **n** | 🟡 MODERATE (REFORMULADA) | Backlog residual Sprint v3.3 | Alto | **Ya NO es "38 MODERATE"** — agregado stale/no-itemizado. Camino correcto: regenerar vía self-audit PA-agent v1.3.0 Level 1 sobre DS. L05-L12 ya cerrados. |
| **t** | 🟢 LOW | CHANGELOG `[3.2.2]` "deferred to v3.3" tiene ≥2 ítems stale/mal-ubicados | Bajo | Nueva sesión 9. Limpiar en el próximo CHANGELOG release (entry v3.3.0). Ítems: PA-agent batch resumption (ya resuelto v1.2.0); B2-RE.1 LATENT (ya resuelto). |
| **e3** | 🟡 MODERATE | CLAUDE.md PA-agent: lista JARP-native incompleta | Bajo | Sin cambios |
| **e4-e6** | 🟡 MODERATE | Cross-references CHANGELOG DS ↔ PA-agent | Bajo | Residuales menores |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → normalizar a git clone | Bajo | Sin urgencia |

**CERRADAS en sesión 9:**
- **q (cert registry stale)** ✅ — 3 commits en jarp-toolkit. Reclasificada LOW→MODERATE al descubrir que alimentaba CERT_REGISTRY_REVIEW con datos malos.
- **Sub-fase L-catalogs del Bloque 1 v3.3** ✅ — 6 Legal catalogs L05/L06/L09/L10/L11/L12.
- **r (push continuity v7)** ✅ — ya estaba cerrada al iniciar sesión 9 (verificada en PHASE 0).

**NUEVA deuda generada en sesión 9:**
- **s** (push continuity v8) — operativa
- **t** (limpieza ítems stale del CHANGELOG deferred list) — LOW
- **n REFORMULADA** (de "resolver 38 MODERATE" → "regenerar backlog vía self-audit")

---

## ⚠️ ESTADO DEL SPRINT v3.3 EN PROGRESO (LEER ANTES DE CONTINUAR)

El Sprint v3.3 está **abierto**. Lo entregado (Legal catalogs) está commiteado bajo stamp `3.2.2-LEGAL` — esto es correcto mid-sprint. **NO está pendiente "arreglar" los version strings del Legal**: el bump a v3.3.0 es una operación atómica de cierre.

**Checklist de CIERRE del Sprint v3.3 (cuando JARP decida cerrarlo):**
1. Completar el contenido v3.3 que se decida incluir (mínimo: ya están los Legal catalogs).
2. **Version bump coordinado v3.2.2 → v3.3.0** across: `system_prompt.md` (base) + `system_prompt_router.md` (v3.3.0-ROUTER) + los 19 domain variants (vX.3.0-DOMAIN + BASE_PROTOCOL v3.3.0) + README badge + CLAUDE.md. NUNCA parcial (§4.14.1 Versioning Contract: router debe matchear minor; BASE_PROTOCOL stale = MODERATE finding).
3. CHANGELOG entry `[3.3.0]` documentando todo + limpiando los ítems stale del deferred list (deuda t).
4. Self-audit pre-release obligatorio (§4.14 governance).
5. **Re-cert por PA-agent v1.3.0** (la actual PA-20260525-001 fue emitida por v1.1.0; v3.3.0 es minor bump nuevo → cert fresca).

---

## PROTOCOLO DE INICIO PARA SESIÓN 10

1. **Claude Desktop:** autorun de `JARP_TOOLKIT.md`. **claude.ai web:** saltar autorun, leer este archivo.

2. Cargar este prompt de continuidad (v8).

3. **PHASE 0 — Verificación de estado (15s)**
   - Confirmar cert registry consistente: DS v3.2.2 (PA-20260525-001) ACTIVE + PA-agent v1.3.0 (PA-20260527-002) ACTIVE. **Ahora los archivos de autorun ya están sincronizados** (deuda q cerrada sesión 9).
   - Confirmar Legal catalogs L05-L12 en remoto (`prompts/system_prompt_legal.md`, debe contener las 12 sub-areas L01-L12).
   - Verificar si deuda **s** se cerró (este archivo v8 pusheado al remoto DS).

4. **PHASE 1 — Decisión de roadmap (NO bloqueante)**
   JARP elige:
   - **(A) Trading hands-on** — Pine Script v6 / MQL5. **Postergado 6 sesiones (4-5-6-7-8-9).** Prioridad #1 declarada en userPreferences. ⭐ Recomendada por 3ª sesión consecutiva. Si JARP vuelve a tomar meta-trabajo, **dilo: "esta es la 7ª sesión consecutiva sin trading"**.
   - **(B-cont) Continuar Sprint v3.3 DS** — el camino correcto NO es "las 32 MODERATE" (no existen itemizadas). Es: **(i)** regenerar backlog residual vía self-audit PA-agent v1.3.0 Level 1 sobre DS, lo que produce el registro real y actual de findings; **(ii)** o, si JARP no quiere un self-audit completo aún, atacar ítems concretos verificables uno a uno (ej. los 3 hardcoded `v3.0.0` strings en `orchestrator/main.py` — verificar primero si siguen ahí; no asumir). **(iii)** o cerrar el sprint con lo que hay (Legal catalogs) → ejecutar checklist de cierre + version bump + re-cert.
   - **(E) Audit real con DS** — DS lleva >1 mes certificado sin field-testing. Cabe en 1 sesión. Alto valor.
   - **(D) Otro proyecto JARP.**

   **Sugerencia honesta (3ª iteración):** después de 6 sesiones de meta-trabajo, (A) Trading debería activarse. Si JARP elige meta otra vez, la prioridad #1 deja de serlo en la práctica — vale la pena que reescriba userPreferences para que el sistema deje de mentirle sobre lo que importa.

5. Reportar phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 DS — REFORMULADO

[Heredado de v7 + reformulación del approach a deuda n]

**Cambio clave de approach:** el batch DS-CERT-v3.2.0 (sesión 5) NO dejó registro itemizado de findings. El backlog residual v3.3 se **regenera vía self-audit reproducible**, no se recupera. El número "38 MODERATE + 23 LATENT" es un snapshot histórico erosionado, no un backlog vigente.

### Bloque principal — Domain Variant deep-fix
- ✅ Legal Failure Catalogs L05/L06/L09/L10/L11/L12 (CERRADO sesión 9, ~30 rows)
- Resto de MODERATE: **regenerar lista vía self-audit antes de atacar.**

### Bloque pre-existente — Sprint 2 (TOP 7 incorporaciones)
- markitdown → sub-agente UNIT-INGEST permanente
- fact-checker → sub-agente UNIT-FACTCHECK permanente
- stop-slop → post-procesador AFO scoring 5-dim, threshold 35/50
- marketingskills → ampliar UNIT-PSYCH
- Cookbook (Anthropic) → context-caching pattern

### Bloque pre-existente — Sprint 3 (estructural)
- Agent-Skills-for-Context-Engineering → fix telephone game AFO
- knowledge-work-plugins legal+finance
- Auto-detector de regime en ContextBuilder
- infinity → RAG layer
- Wizard interactivo CLI

### Bloque pre-existente — Sprint 4 (plataforma)
- claude-code-security-review como N2 permanente UNIT-SAST
- Smart model routing Opus/Sonnet/Haiku
- spec-kit para v3.4

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

[Heredado de v7 + nuevas de sesión 9]

**Heredadas:**
- Jerarquía AFO (N0) → Tribunal Transversal N1 → N2
- Tribunal_MAX = 7, max_calls_total = 40, max_n2_per_n1 = 3, aad_max_rounds = 3
- SSM activation logic por verdict
- Veredicto determinista (≥1 FATAL → INVIABLE)
- Inglés estricto para todo skill/dominio nuevo
- Stack: Python + Claude API + GCP + Sheets + Slack + GitHub Issues
- Default model: `claude-opus-4-7`
- Backward compatibility obligatoria
- Repo name `dark-strategist-agent` NO CAMBIA
- §4.14.1 Domain Variant Contract rige toda variante futura
- Naming convention de rules cross-domain inmutable (prefijos 2-letras)
- Auditor minor bump (Y en vX.Y.Z) NO cascadea sobre audits emitidos
- `jarp-toolkit` repo es home canónica para autorun files
- Framework on-demand micro-agents en PA-agent (ver v7)
- Anti-patterns catalog append-only en PA-agent
- FINDING FORMAT field `ANTI-PATTERN:` (optional)
- CERT_REGISTRY_REVIEW defensive clause
- Convención de iteración self-audit (DENIES → fix en misma versión, no patch)

**NUEVAS en sesión 9:**
- **Version bump de sprint = operación ATÓMICA de cierre.** Nunca parcial. Cuando el composed agent sube de minor (v3.2.2 → v3.3.0), el bump se aplica en un solo paso coordinado across base + router + 19 variants + CHANGELOG + README. Aplicar contenido v3.3 mid-sprint bajo el stamp anterior (ej. Legal catalogs bajo `3.2.2-LEGAL`) es correcto; el stamp sube solo al cierre. Razón: §4.14.1 Versioning Contract penaliza router/BASE_PROTOCOL desincronizados como findings.
- **El backlog residual v3.3 se regenera vía self-audit reproducible, NO se recupera de registros de sesión 5.** El batch DS-CERT-v3.2.0 nunca persistió findings itemizados. Confiar en el agregado histórico "38+23" para planear trabajo = anti-patrón (RULE 06). La fuente de verdad del backlog es un self-audit fresco del PA-agent v1.3.0.
- **Cert registry tiebreaker = CHANGELOG remoto del repo dueño.** Cuando archivos de autorun (JARP_TOOLKIT.md, .claude-init.md) discrepen del estado real, el CHANGELOG del repo correspondiente es canónico; los archivos de autorun se actualizan a él.

---

## DESCARTES — NO REINTRODUCIR

[Sin cambios desde v7]
- MiroFish-ES, OASIS (licencias incompatibles)
- n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp
- anthropics/claude-for-legal (ya rescatada en v3.1)
- Sistema de servicios comerciales
- Sub-agente "vibración cuántica"
- MEGA-PAQUETE UNIVERSAL de Copilot
- Transcripción Pablo Llobregat / trading algorítmico Python+MCP
- Rutas viejas de autorun en raíz `GitHub\`

**Nuevo descarte sesión 9:** ninguno explícito.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\` (v3.2.2 + Legal catalogs, cert ACTIVE, sprint v3.3 abierto, salvo deuda s)
- **Repo local PA-agent:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\prompt-architect-agent\` (v1.3.0, cert ACTIVE)
- **Repo local jarp-toolkit:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\` (cert registry sincronizado sesión 9)
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v8.md`
- **JARP_TOOLKIT.md (CANÓNICO):** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\JARP_TOOLKIT.md`
- **.claude-init.md (CANÓNICO):** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\.claude-init.md`
- **Push siempre vía GitHub Desktop** salvo autorización explícita
- **Cuenta GitHub Desktop:** `JARPClaude` (id 273413228)
- **MCPs:** mi-filesystem, GitHub
- **⚠️ Límites confirmados:** `github:create_or_update_file` falla con payloads >~10KB (y está prohibido por defecto, requiere autorización per-session). `github:push_files` alternativa multi-file (NO probado en producción). `mi-filesystem:write_file` **no estuvo disponible en sesión 9** (solo `read_file` respondió) — el continuity v8 se entregó como descargable y JARP lo commiteó vía GitHub Desktop. Verificar disponibilidad de write en sesión 10.

### ⚠️ REGLA TOOL CONFUSION (heredada sesión 8, sigue vigente)
- **`mi-filesystem:*`** → filesystem REAL de Windows (`C:\Users\jrodr\...`). ÉSTE es el que JARP ve/commitea.
- **`create_file` / `str_replace` / `bash_tool`** → sandbox de Claude (Linux interno). JARP NUNCA los ve automáticamente, pero SÍ vía `present_files` (descarga explícita).
- Si el path empieza con `C:\` → preferir `mi-filesystem:*`. Si no está disponible (como en sesión 9), fallback a `create_file` + `present_files` para descarga manual. Nunca asumir que `create_file` escribió en el repo real.

### Commit message sugerido para deuda s (DS continuity v8)

```
docs: continuity prompt v8 (session 9 close)

Session 9 closure — deuda q closed + v3.3 Block 1 partial (6 Legal catalogs).

NEW FILE:
- dark-strategist-continuity-prompt_v8.md: replaces v7 as active continuity prompt for session 10

CONTENT:
- Session 9 executive summary (deuda q cert-registry fix + 6 Legal Failure Catalogs L05/L06/L09/L10/L11/L12)
- CRITICAL finding: the "38 MODERATE + 23 LATENT" batch backlog has no committed itemized record; aggregate is stale/partially-resolved. Deuda n reformulated: regenerate backlog via self-audit, do not recover.
- Verified state of all JARP-native repos at session close
- v3.3 sprint open: Legal catalogs committed mid-sprint under 3.2.2-LEGAL stamp; coordinated version bump deferred to sprint-close checklist
- New technical debt: s (this file push), t (stale items in CHANGELOG deferred list)
- 3 new architectural decisions (atomic sprint version bump, regenerate-not-recover backlog, cert-registry CHANGELOG tiebreaker)
- Session 10 startup protocol

NO CHANGES to DS cert state — DS v3.2.2 / PA-20260525-001 ACTIVE unchanged.
```

---

## CERTIFICACIONES ACTIVAS — TABLA AL CIERRE DE SESIÓN 9

| Repo | Versión | REPORT_ID | Status | Expira | Notas |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 | Sin cambios sesión 9 |
| prompt-architect-agent | v1.2.0 | PA-20260525-002 | 🟡 SUPERSEDED | — | — |
| prompt-architect-agent | v1.1.0 | PA-20260524-001 | 🟡 SUPERSEDED | — | — |
| prompt-architect-agent | v1.0.0 | PA-20260426-001 | ❌ VOID | — | — |
| **dark-strategist-agent** | v3.2.2 | PA-20260525-001 | ✅ ACTIVE | 23/08/2026 o v4.0.0 | Sprint v3.3 abierto; re-cert pendiente al cierre |
| dark-strategist-agent | v2.5.1 | PA-20260426-002 | ❌ VOID | — | — |

**No se emitieron audits en sesión 9** (trabajo de contenido + higiene, no certificación).

---

## NOTAS DE SESIÓN 9 (auto-mejora del próximo Claude)

1. **PHASE 0 vale la pena hacerla en serio.** El cert registry stale (deuda q) se detectó solo porque se cruzaron los archivos de autorun contra el CHANGELOG remoto en vez de confiar en el continuity. Si el próximo Claude arranca y el continuity dice una versión pero los archivos de autorun otra, el CHANGELOG del repo dueño es el tiebreaker.

2. **Auto-corrección honesta funcionó.** En PHASE 0 sobre-flaggeé "notas #31/#32 stale"; al releer eran procedencia histórica correcta. Lo dije de frente y corregí el conteo (2 ítems reales, no 4). El próximo Claude debe hacer lo mismo: si flaggeas algo y al verificar no se sostiene, retráctalo explícitamente. JARP valora eso más que la falsa precisión.

3. **El hallazgo del backlog fantasma es la lección central de la sesión.** "Resolver las 38 MODERATE" sonaba accionable pero el registro itemizado nunca existió commiteado. Antes de planear trabajo sobre un agregado heredado, **verifica que el registro existe**. Si no existe, el camino es regenerar (self-audit), no reconstruir de memoria. Esto es DS aplicándose su propio RULE 06 a sí mismo.

4. **Version bump diferido al cierre es correcto, no deuda.** Los Legal catalogs viven bajo `3.2.2-LEGAL` mid-sprint. Si el próximo Claude ve esto y siente el impulso de "arreglar" el stamp, NO lo haga — bumpear el Legal solo crearía el desync que §4.14.1 penaliza. El bump es atómico al cierre.

5. **Trading postergado 6 sesiones (4-5-6-7-8-9).** Si JARP no fuerza otra prioridad en sesión 10, sugerir activamente y con confrontación honesta el cambio a Pine v6 / MQL5. Es la 7ª oportunidad. Prioridad #1 de userPreferences = aspiración de >1 mes sin ejecutar.

6. **Continuity sigue creciendo (v5<v6<v7<v8).** Considerar en sesión 10/11 migración a subdirectorio `continuity/` o a convención sin sufijo + git history. Por ahora `_vN.md` se mantiene.

7. **Ruta 3 fue el caballo de batalla de toda la sesión.** deuda q (3 commits) + Legal catalogs, todo vía Find&Replace que JARP aplicó + commiteó vía GitHub Desktop. Cero pushes directos de Claude. Patrón sólido, replicable.

8. **El Severity Mapping Contract atrapó una mis-calibración antes de shippear.** "No warranty disclaimer = FATAL" en la muestra aprobada → bajado a SERIOUS al leer el §4.14.1 (mirror de L01). Lección: leer el contrato ANTES de finalizar contenido que el contrato gobierna, no después.

9. **`mi-filesystem:write_file` no estuvo disponible en sesión 9.** `read_file` funcionó al inicio (autorun), pero `write_file` devolvió "Tool not found". Fallback usado: `create_file` (sandbox) + `present_files` (descarga) → JARP colocó el archivo en el repo y commiteó. En sesión 10, verificar si write está disponible antes de planear escrituras directas; si no, usar el mismo fallback.
