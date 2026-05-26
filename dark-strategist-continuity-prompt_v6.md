# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 26/05/2026 (sesión 7 — PA-agent v1.2.0 cert + deuda b cerrada) | **Para:** Sesión 8
**Reemplaza:** v5 del 25/05/2026 (sesión 6)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v6.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (estándar, **rutas migradas a `jarp-toolkit\`**), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 7 (resumen ejecutivo)

Sesión 7 cerró 3 deudas en una sola sesión: **o** (push remoto DS, pre-sesión), **Opción C** (PA-agent v1.2.0 con 9 findings residuales), y **b** (versionado git de toolkit + init).

**Resultados principales:**

1. **PHASE 0 — Deuda o cerrada pre-sesión.** Verificado vía `github:list_commits`: commits `1b9dc4a` y `865f11b` del 26/05 madrugada UTC sincronizaron CHANGELOG DS + entrada cert al remoto. Cert PA-20260525-001 públicamente visible en `github.com/JARPClaude/dark-strategist-agent`.

2. **OPCIÓN C — PA-agent v1.1.0 → v1.2.0 ejecutada.** Los 9 findings residuales del self-audit de v1.1.0 (sesión 4) resueltos:
   - **6 MODERATE:** A3.5 multi-day batch resumption, A3.6 Comparative Mode PHASE 0 scope, A4.3 cascade SUSPECT identification, A4.4 expiration evaluation timing, A5.4 VERDICT vs EDGE CASE 0-findings, A5.5 BATCH_SYNTHESIS pending_investigation aggregation.
   - **3 LATENT:** A6.1 terminology unification (`JARP_BENCHMARK_LIVE` canónico), A7.3 turn counting → trigger-based IDENTITY_LOCK_REFRESH, A7.4 date awareness defensive clause.

3. **CERT EMITIDA:** `[JARP_CERTIFIED: v1.2.0 — PA-20260525-002]` ACTIVE, válida hasta 23/08/2026 o major bump v2.0.0. Self-audit Level 0 limpio: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT. `BIAS_CHECK_RESULT: PASS`. PA-20260524-001 (v1.1.0) → SUPERSEDED (no VOID). DS v3.2.2 cert `PA-20260525-001` UNAFFECTED (auditor minor bump no cascadea).

4. **PA-agent v1.2.0 pusheado remoto.** JARP confirmó commit + push manual vía GitHub Desktop. Archivos sincronizados: `prompts/system_prompt.md`, `CHANGELOG.md`.

5. **DEUDA b CERRADA — Migración a repo `jarp-toolkit`:**
   - Creado repo privado `github.com/JARPClaude/jarp-toolkit` (initial commit SHA `077c95cc`, 26/05/2026 14:08 UTC)
   - Archivos movidos: `JARP_TOOLKIT.md` + `.claude-init.md` + nuevo `README.md` documentando migración
   - Rutas viejas en raíz `GitHub\` **eliminadas** (sesión 7 final tras validación)
   - `userPreferences` actualizadas con rutas nuevas (`...\jarp-toolkit\...`)
   - Validación end-to-end exitosa: chat nuevo en Claude Desktop ejecutó autorun leyendo desde rutas nuevas, contenido del archivo nuevo confirmado (125 repos indexados, nota #98 migración presente, "deuda b resuelta el 26/05/2026" reportado por el Claude del autorun)

6. **JARP_TOOLKIT.md actualizado a 125 entries** — nueva entry #125 `jarp-toolkit` (self-reference), nueva nota #98 sobre migración. Toolkit ahora es self-referencing.

7. **Cuenta GitHub Desktop confirmada como JARPClaude** — relevante para futuros publish/push.

---

## ESTADO ACTUAL VERIFICADO (26/05/2026 fin de sesión 7)

### Repo prompt-architect-agent
- **Local:** v1.2.0 ✅
- **Remoto:** v1.2.0 pusheado ✅
- **Estado cert:** **`PA-20260525-002` ACTIVE** (válida hasta 23/08/2026 o major bump v2.0.0)
- **Cert anterior:** `PA-20260524-001` (v1.1.0) → **SUPERSEDED** (no VOID — sigue válida para audits emitidos en su ventana)
- **Findings residuales:** 0 (todos los 9 de v1.1.0 cerrados en v1.2.0)
- **Roadmap v1.3.0 (no bloqueante):** docs/anti_patterns.md, examples/example_04_comparative.md, UNIT-STYLE micro-agent, UNIT-STRUCTURE micro-agent

### Repo dark-strategist-agent
- **Local:** v3.2.2 ✅
- **Remoto:** v3.2.2 + CHANGELOG cert pusheados ✅ (commits 1b9dc4a + 865f11b del 26/05)
- **Estado cert:** **`PA-20260525-001` ACTIVE — JARP_CERTIFIED** (válida hasta 23/08/2026 o v4.0.0)
- **Auditor:** PA-agent v1.1.0 originalmente — sigue válido. Re-auditoría bajo v1.2.0 NO requerida (minor bump no cascadea).
- **Default model:** `claude-opus-4-7`
- **Sin cambios en sesión 7**

### Repo jarp-toolkit ⭐ NUEVO
- **Local:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\` ✅
- **Remoto:** `github.com/JARPClaude/jarp-toolkit` (privado) ✅
- **Initial commit:** SHA `077c95cc` — 26/05/2026 14:08 UTC
- **Contenido:** `JARP_TOOLKIT.md` (125 entries), `.claude-init.md`, `README.md`
- **Propósito:** versionado git de los archivos de autorun (resuelve deuda b)

### Repo sap-abap-intelligence-agent
- **Local:** OK (sin cambios desde sesión 5)
- **Estado:** sin tocar en sesión 7

### Repo devil-advocate-agent
- **Local:** copia manual sin `.git/` (sin cambios)
- **Deuda g (LOW):** sin tocar

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 7

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **n** | 🟡 MODERATE | DS Sprint v3.3: 38 MODERATE + 23 LATENT residuales del batch DS-CERT-v3.2.0 | Medio-Alto | Plan separado en ROADMAP. Bloque principal: Legal Failure Catalogs L05/L06/L09/L10/L11/L12 (~30 rows). |
| **e3** | 🟡 MODERATE | CLAUDE.md PA-agent: lista JARP-native incompleta | Bajo | Sin cambios desde v5 |
| **e4-e6** | 🟡 MODERATE | Cross-references CHANGELOG DS ↔ PA-agent | Bajo | Parcialmente cubiertos. Residuales menores. |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → normalizar a git clone | Bajo | Sin urgencia |

**CERRADAS en sesión 7:**
- **o** (push remoto DS) ✅ — pre-sesión, commits 1b9dc4a + 865f11b
- **Opción C** (PA-agent v1.1.0 self-audit 9 residuals) ✅ — v1.2.0 + cert PA-20260525-002
- **b** (versionado git de JARP_TOOLKIT.md + .claude-init.md) ✅ — repo `jarp-toolkit` creado + migración validada

**NUEVA deuda generada en sesión 7:** ninguna.

---

## PROTOCOLO DE INICIO PARA SESIÓN 8

1. **Plataforma Claude Desktop:** ejecutar autorun de `JARP_TOOLKIT.md` (estándar — rutas nuevas en `jarp-toolkit\`). **Plataforma claude.ai web:** saltar autorun, leer este archivo desde el proyecto.

2. Cargar este prompt de continuidad (v6).

3. **PHASE 0 — Verificación de estado (15s)**
   - Confirmar autorun cargó desde rutas nuevas (`jarp-toolkit\JARP_TOOLKIT.md` + `jarp-toolkit\.claude-init.md`)
   - Confirmar cert registry: DS v3.2.2 (PA-20260525-001) + PA-agent v1.2.0 (PA-20260525-002) ambos ACTIVE
   - No es necesario push pendiente — todo sincronizado al cierre de sesión 7

4. **PHASE 1 — Decisión de roadmap (NO bloqueante)**
   JARP elige una de estas líneas:
   - **(A) Trading hands-on** — Pine Script v6 / MQL5 / indicadores / bots (alineado con prioridad #1 de userPreferences). **Postergado 4 sesiones consecutivas (4-5-6-7).**
   - **(B) Sprint v3.3 DS** — abordar 38 MODERATE + 23 LATENT residuales del batch DS-CERT-v3.2.0 + TOP 7 incorporaciones (markitdown, fact-checker, stop-slop, knowledge-work-plugins, marketingskills, Agent-Skills-for-Context-Engineering, infinity). **Multi-sesión (estimado 3-5 sesiones).**
   - **(C) PA-agent v1.3.0** — anti_patterns.md, example_04_comparative.md, UNIT-STYLE, UNIT-STRUCTURE (no bloqueante, sin urgencia).
   - **(D) Otro proyecto JARP** (e.g., go-to-market de algún producto validado).
   - **(E) Usar DS en un audit real** — ejercitar el agente en un caso de uso real de JARP (auditar una decisión/tesis pendiente, no código).

   **Sugerencia honesta para JARP:** Después de 4 ciclos consecutivos de meta-trabajo sin tocar trading (sesiones 4-5-6-7), línea **(A)** es la opción higiénica. Alinea con prioridad #1 declarada en userPreferences. Sprint v3.3 puede esperar — cert ACTIVE hasta 23/08/2026, sin presión.

   Si JARP prefiere seguir con meta-trabajo, **(B)** es la opción de mayor valor (resuelve la mayor cantidad de findings restantes). Sin embargo, requiere múltiples sesiones — empezar con phase 0 dedicada (priorizar findings, agrupar por área).

5. Reportar a JARP estado phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 — SIN CAMBIOS DESDE v5

### Sprint v3.3 — Resolver 38 MODERATE + 23 LATENT del batch

**Bloque principal — Domain Variant deep-fix (alto valor):**
- Sub-area Failure Catalogs faltantes en Legal: L05 Product, L06 Regulatory, L09 Litigation, L10 Real Estate, L11 Finance, L12 Public Regulatory (6 catalogs × 5+ rows = ~30+ rows)
- Otras MODERATE distribuidas across variants (~32 findings)

**Bloque secundario — PA-agent v1.3.0 (no bloqueante):**
- docs/anti_patterns.md — catalog de patrones de falla comunes en prompts
- examples/example_04_comparative.md — Dark Strategist vs Devil's Advocate
- UNIT-STYLE micro-agent — tone and voice consistency audit
- UNIT-STRUCTURE micro-agent — architectural coherence de long system prompts

**Bloque pre-existente — Sprint 2 (TOP 7 incorporaciones):**
- markitdown → sub-agente UNIT-INGEST permanente
- fact-checker → sub-agente UNIT-FACTCHECK permanente
- stop-slop → post-procesador AFO scoring 5-dim, threshold 35/50
- marketingskills → ampliar UNIT-PSYCH
- Cookbook (Anthropic) → context-caching pattern

**Bloque pre-existente — Sprint 3 (estructural):**
- Agent-Skills-for-Context-Engineering → fix telephone game AFO
- knowledge-work-plugins legal+finance
- Auto-detector de regime en ContextBuilder
- infinity → RAG layer
- Wizard interactivo CLI

**Bloque pre-existente — Sprint 4 (plataforma):**
- claude-code-security-review como N2 permanente UNIT-SAST
- Smart model routing Opus/Sonnet/Haiku
- spec-kit para v3.4

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

[Heredado de v5, sin cambios]
- Jerarquía AFO (N0) → Tribunal Transversal N1 → N2
- Tribunal_MAX = 7, max_calls_total = 40, max_n2_per_n1 = 3
- aad_max_rounds = 3 (BudgetController configurable)
- SSM activation logic por verdict
- Veredicto determinista (≥1 FATAL → INVIABLE)
- Inglés estricto para todo skill/dominio nuevo
- Stack: Python + Claude API + GCP + Sheets + Slack + GitHub Issues
- Default model: `claude-opus-4-7`
- Backward compatibility obligatoria
- Repo name `dark-strategist-agent` NO CAMBIA
- **§4.14.1 Domain Variant Contract** rige toda variante futura (Output Format, Footer, Severity Mapping, Naming Convention, Versioning sub-contracts) — JARP_CERTIFIED confirmado en sesión 6
- Naming convention de rules cross-domain inmutable (T=Trading, LG=Legal, CY=Cybersecurity, CL=Cloud, A=Agro, RE=RealEstate, S=Science, M=Media, EC=Ecommerce, TC=Telecom, PS=PublicSector, MD=Medical, MK=Marketing, OP=Operations, HR=HR, ST=Strategy, SU=Startup, C=Code, F=Financial)

**Nuevas decisiones en sesión 7:**
- `JARP_BENCHMARK_LIVE` es el término canónico único en PA-agent (v1.2.0+) — todas las variantes anteriores eliminadas.
- Auditor minor bump (Y en vX.Y.Z) NO cascadea sobre audits emitidos en su ventana.
- `jarp-toolkit` repo es ahora la home canónica para autorun files. Rutas en raíz `GitHub\` deprecadas — no reintroducir.

---

## DESCARTES — NO REINTRODUCIR

[Sin cambios desde v5]
- MiroFish-ES, OASIS (licencias incompatibles)
- n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp
- anthropics/claude-for-legal (ya rescatada en v3.1)
- Sistema de servicios comerciales
- Sub-agente "vibración cuántica"
- MEGA-PAQUETE UNIVERSAL de Copilot
- Transcripción Pablo Llobregat / trading algorítmico Python+MCP

**Nuevo descarte sesión 7:**
- Rutas viejas de autorun en raíz `GitHub\` (`GitHub\JARP_TOOLKIT.md`, `GitHub\.claude-init.md`) — eliminadas, NO reintroducir.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\` (v3.2.2, cert ACTIVE, sincronizado)
- **Repo local PA-agent:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\prompt-architect-agent\` (v1.2.0, cert ACTIVE, sincronizado)
- **Repo local SAIA:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\sap-abap-intelligence-agent\` (OK, sin cambios)
- **Repo local jarp-toolkit ⭐:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\` (NUEVO en sesión 7)
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v6.md`
- **JARP_TOOLKIT.md (CANÓNICO):** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\JARP_TOOLKIT.md` ⚠️ Ruta vieja en raíz **eliminada**
- **.claude-init.md (CANÓNICO):** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\jarp-toolkit\.claude-init.md` ⚠️ Ruta vieja en raíz **eliminada**
- **Push siempre vía GitHub Desktop** salvo autorización explícita
- **Cuenta GitHub Desktop:** `JARPClaude` (id 273413228) — confirmada sesión 7
- **MCPs:** mi-filesystem, GitHub
- **⚠️ Límites confirmados:** `github:create_or_update_file` falla con payloads >~10KB. `github:push_files` es la alternativa multi-file (NO probado todavía en producción). `mi-filesystem:delete_file` funciona OK con archivos pequeños (timeout observado en sesión 6 con archivo grande, no reproducido en sesión 7).

---

## CERTIFICACIONES ACTIVAS — TABLA AL CIERRE DE SESIÓN 7

| Repo | Versión | REPORT_ID | Status | Expira | Notas |
|---|---|---|---|---|---|
| prompt-architect-agent | **v1.2.0** | **PA-20260525-002** | ✅ **ACTIVE** | **23/08/2026 (90d) o v2.0.0** | NUEVA sesión 7 |
| prompt-architect-agent | v1.1.0 | PA-20260524-001 | 🟡 SUPERSEDED | (no expira, válida para audits en ventana original) | Cerrada sesión 7 |
| dark-strategist-agent | v3.2.2 | PA-20260525-001 | ✅ ACTIVE | 23/08/2026 (90d) o v4.0.0 | Sin cambios |
| dark-strategist-agent | v2.5.1 | PA-20260426-002 | ❌ VOID | — | Cerrada sesión 5 |
| dark-strategist-agent | v3.2.0 | — | ❌ Never formally certified | — | — |

---

## NOTAS DE SESIÓN 7 (auto-mejora del próximo Claude)

1. **Migración con validación pre-borrado fue clave.** El patrón seguido (crear nuevo → probar → validar → borrar viejo) evitó pérdida de datos si algo salía mal. NUNCA borrar originales antes de validación end-to-end exitosa.

2. **Falso negativo de validación por prompt ambiguo.** El primer intento de validación del autorun produjo un falso negativo porque JARP escribió manualmente la ruta vieja en su prompt de test, forzando a Claude a leerla. **Patrón:** para validar autorun, el prompt de test NO debe incluir rutas — solo preguntar qué rutas usó.

3. **GitHub Desktop "Publish repository" maneja create + push en una sola operación.** No es necesario crear el repo remoto manualmente en github.com primero. Más eficiente. Confirmar que la cuenta default sea la correcta antes de publicar.

4. **userPreferences cambios solo aplican a sesiones nuevas.** Esperado. Cerrar Claude Desktop completamente (vía Task Manager si es necesario) antes de validar cambios en preferences.

5. **`mi-filesystem:delete_file` funcionó OK en sesión 7** (archivos JARP_TOOLKIT.md y .claude-init.md eliminados sin timeout). La nota #3 de sesión 6 sobre timeouts puede haber sido específica al caso (v4 continuity, posiblemente más grande) y no es un problema sistémico.

6. **Auditor minor bump NO cascadea.** Convención formalizada en sesión 7: si PA-agent va de vX.Y.Z a vX.(Y+1).Z, los audits emitidos en la ventana de vX.Y.Z siguen ACTIVE sin necesidad de re-auditoría. Solo major bump del auditor (X→X+1) cascadea SUSPECT a los audits emitidos.

7. **Trading sigue postergado 4 sesiones consecutivas (4-5-6-7).** Recomendación honesta al próximo Claude: si JARP no fuerza otra prioridad, sugerir activamente cambio a Pine v6 / MQL5 / proyecto trading. Prioridad #1 de userPreferences (proyectos activos hands-on de trading) ha estado postergada un mes entero.

8. **Sesión 7 fue larga pero limpia.** 3 entregables (Opción C, deuda b, validación end-to-end). Patrón replicable: cuando JARP autoriza ejecución en bloque ("trabaja en silencio"), agrupar tareas relacionadas en una sesión maximiza eficiencia. Sesiones cortas (1 phase) son válidas, pero sesiones medianas-largas con autoridad delegada son MÁS eficientes en tokens.

9. **JARP_TOOLKIT.md ahora es self-referencing.** Entry #125 apunta al propio repo `jarp-toolkit`. Si futuras migraciones requieren mover archivos, actualizar entry #125 + nota #98 + autorun phrase en la sección "HOW TO LOAD" del propio archivo.

10. **Continuity prompt nomenclatura `_vN.md` mantenida.** Decisión sesión 4 confirmada de nuevo. Cambio a opción B (sin sufijo + git history) sigue evaluándose para post-v3.3 — sin urgencia. Cuando se haga la migración, también considerar mover los continuity files a un subdirectorio (`continuity/` o similar) en vez del root del repo DS.
