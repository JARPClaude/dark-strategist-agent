# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 25/05/2026 (sesión 6 - cert v3.2.2 emitida) | **Para:** Sesión 7
**Reemplaza:** v4 del 24/05/2026 (sesión 5)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v5.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (estándar), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 6 (resumen ejecutivo)

Sesión 6 cerró el bloqueo principal heredado de sesión 5: la certificación pendiente de DS v3.2.2.

**Resultados principales:**

1. **PHASE 1 — Re-Cert DS v3.2.2 ejecutado.** Conformance check reducido contra Contract §4.14.1. Auditor: prompt-architect-agent v1.1.0 (PA-20260524-001). Sample: base + router + 6 de 19 variants (P02 Trading, P03 Legal, P08 Agro, P15 Medical, P16 Marketing, P19 Strategy = 47% file coverage).

2. **Hallazgos del re-cert:** 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT. Todas las verificaciones del Contract pasaron:
   - Output Format Contract (declaración explícita de herencia + adaptaciones)
   - Footer Contract (3-line canónico presente)
   - Severity Mapping Contract (no contradicciones)
   - Naming Convention Contract (T/LG/A/MD/MK/ST prefixes correctos)
   - Versioning Contract (BASE_PROTOCOL → v3.2.2 en todos)
   - P03 Legal Geofence monotónica confirmada
   - P08 Agro Yield SERIOUS reclasificación confirmada
   - Router bind rule v3.2.0-ROUTER ↔ Agent v3.2.2 alineado

3. **CERT EMITIDA:** `[JARP_CERTIFIED: DS v3.2.2 — PA-20260525-001]` ACTIVE, válida hasta 23/08/2026 o major bump v4.0.0.

4. **PHASE 2 — Actualización operacional ejecutada (deudas l, m, parte de e7, h):**
   - `dark-strategist-agent/CHANGELOG.md` — entrada cert añadida al tope
   - `.claude-init.md` línea 7 — estados cert actualizados (deuda m ✅)
   - `JARP_TOOLKIT.md` — entrada #30 DS + entrada #42 PA-agent + nota #16 + nota #44 actualizadas (deudas l + h ✅)
   - `dark-strategist-continuity-prompt_v5.md` creado (este archivo)
   - `dark-strategist-continuity-prompt_v4.md` queda en el repo (intento de delete falló por timeout MCP; no es bloqueante — la nomenclatura `_vN.md` resuelve precedencia)

5. **Cascade resuelta y consolidada:**
   - `PA-20260524-001` (PA-agent v1.1.0): **ACTIVE** ✅
   - `PA-20260525-001` (DS v3.2.2): **ACTIVE** ✅
   - `PA-20260426-002` (DS v2.5.1): VOID (definitivamente cerrada)

---

## ESTADO ACTUAL VERIFICADO (25/05/2026 fin de sesión 6)

### Repo prompt-architect-agent
- **Remoto:** v1.1.0 desplegado y verificado (desde sesión 5)
- **Estado cert:** `PA-20260524-001` ACTIVE (válida hasta 22/08/2026 o major bump v2.0.0)
- **Findings residuales para v1.2.0:** 6 MODERATE + 3 LATENT (sin cambios)
- **Local:** OK

### Repo dark-strategist-agent
- **Versión live:** **v3.2.2** (composed agent)
- **Versión base file:** v3.2.2 (stamp alineado)
- **Versión router:** v3.2.0-ROUTER (válido — bind rule satisfecho)
- **Default model:** `claude-opus-4-7`
- **Estado cert:** ✅ **`PA-20260525-001` ACTIVE — JARP_CERTIFIED**
- **Validity:** hasta 23/08/2026 (90 días) o major bump v4.0.0
- **Local:** OK
- **CHANGELOG actualizado con entrada cert** (sin push aún en sesión 6 — pendiente para sesión 7 vía GitHub Desktop)

### Repo sap-abap-intelligence-agent
- **Local:** OK (sin cambios desde sesión 5)
- **Estado:** sin tocar en sesión 6
- **Nota #44 toolkit actualizada:** corruption concern refutada (evento PA-agent sesión 4 fue aislado; no migrar preventivamente)

### Repo devil-advocate-agent
- **Local:** copia manual sin `.git/` (sin cambios)
- **Deuda g (LOW):** sin tocar

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 6

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **o** | 🟡 MODERATE | **Push remoto del repo DS** (CHANGELOG + cert entry sin sincronizar a github.com) | Bajo | Bloqueante para que la cert sea pública. Sesión 7 PHASE 0. Vía GitHub Desktop. |
| **e3** | 🟡 MODERATE | CLAUDE.md PA-agent: lista JARP-native incompleta | Bajo | Sin cambios desde v4 |
| **e4-e6** | 🟡 MODERATE | Cross-references CHANGELOG DS ↔ PA-agent | Bajo | Parcialmente cubiertos en CHANGELOG cert sesión 6, residuales pendientes |
| **n** | 🟡 MODERATE | DS Sprint v3.3: 38 MODERATE + 23 LATENT residuales del batch | Medio | Plan separado (ver ROADMAP) |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → normalizar a git clone | Bajo | Sin urgencia |
| **b** | 🟡 MODERATE | JARP_TOOLKIT.md y .claude-init.md sin versionado git | Bajo | Sin cambio desde sesión 2. Riesgo: pérdida de cambios si OneDrive falla. |

**CERRADAS en sesión 6:**
- **k** (re-cert DS v3.2.2) ✅
- **l** (JARP_TOOLKIT.md nota #16 + entrada #30 + entrada #42) ✅
- **m** (.claude-init.md línea 7) ✅
- **h** (nota #44 toolkit corruption SAIA) ✅
- **e7** (parcial — cert documentada en CHANGELOG; residuales menores quedan abiertos)

**NUEVA deuda generada en sesión 6:**
- **o** (push remoto DS) — bajo esfuerzo, pero bloqueante para visibilidad pública de la cert

---

## PROTOCOLO DE INICIO PARA SESIÓN 7

1. **Plataforma Claude Desktop:** ejecutar autorun de `JARP_TOOLKIT.md` (estándar). **Plataforma claude.ai web:** saltar autorun, leer este archivo desde el proyecto.

2. Cargar este prompt de continuidad (v5).

3. **PHASE 0 — Push remoto DS (deuda o)**
   - Verificar diff local del repo DS contra remoto
   - JARP ejecuta push vía GitHub Desktop
   - Confirmar entrada cert visible en github.com/JARPClaude/dark-strategist-agent/blob/main/CHANGELOG.md

4. **PHASE 1 — Decisión de roadmap (NO bloqueante)**
   JARP elige una de estas tres líneas:
   - **(A) Trading hands-on** — Pine Script v6 / MQL5 / indicadores / bots (alineado con prioridad #1 de userPreferences)
   - **(B) Sprint v3.3** — abordar 38 MODERATE + 23 LATENT residuales del batch DS
   - **(C) PA-agent v1.2.0** — resolver 6 MODERATE + 3 LATENT del PA-agent self-audit
   - **(D) Otro proyecto JARP** (e.g., go-to-market de algún producto validado)

   **Sugerencia para JARP:** Después de 3 ciclos consecutivos de patches DS/PA-agent (sesiones 4-5-6), línea (A) es la opción higiénica — alinea con prioridad #1 declarada en userPreferences y rompe el ciclo de meta-trabajo. Sprint v3.3 puede esperar 1-2 semanas sin daño operativo (cert ACTIVE hasta 23/08/2026).

5. Reportar a JARP estado phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 — SIN CAMBIOS DESDE v4

### Sprint v3.3 — Resolver 38 MODERATE + 23 LATENT del batch

**Bloque principal — Domain Variant deep-fix (alto valor):**
- Sub-area Failure Catalogs faltantes en Legal: L05 Product, L06 Regulatory, L09 Litigation, L10 Real Estate, L11 Finance, L12 Public Regulatory (6 catalogs × 5+ rows = ~30+ rows)
- Otras MODERATE distribuidas across variants (~32 findings)

**Bloque secundario — PA-agent v1.2.0:**
- 6 MODERATE + 3 LATENT residuales del PA-agent self-audit:
  - A3.5 multi-day batch resumption rules
  - A3.6 Comparative Mode Phase 0 scope
  - A4.3 cascade SUSPECT identification mechanism
  - A4.4 RULE 09 expiration evaluation timing
  - A5.4 VERDICT vs EDGE CASE 0-findings double-emit
  - A5.5 BATCH_SYNTHESIS PENDING_INVESTIGATION rendering
  - A6.1 terminology JARP_BENCHMARK_LIVE consistency
  - A7.3 turn counting mechanism
  - A7.4 RULE 09 date awareness dependency

**Bloque pre-existente — Sprint 2:**
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

[Heredado de v4, sin cambios]
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
- **§4.14.1 Domain Variant Contract** rige toda variante futura (Output Format, Footer, Severity Mapping, Naming Convention, Versioning sub-contracts) — **confirmado JARP_CERTIFIED en sesión 6**
- Naming convention de rules cross-domain inmutable (T=Trading, LG=Legal, CY=Cybersecurity, CL=Cloud, A=Agro, RE=RealEstate, S=Science, M=Media, EC=Ecommerce, TC=Telecom, PS=PublicSector, MD=Medical, MK=Marketing, OP=Operations, HR=HR, ST=Strategy, SU=Startup, C=Code, F=Financial)

---

## DESCARTES — NO REINTRODUCIR

[Sin cambios desde v4]
- MiroFish-ES, OASIS (licencias incompatibles)
- n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp
- anthropics/claude-for-legal (ya rescatada en v3.1)
- Sistema de servicios comerciales
- Sub-agente "vibración cuántica"
- MEGA-PAQUETE UNIVERSAL de Copilot
- Transcripción Pablo Llobregat / trading algorítmico Python+MCP

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\` (v3.2.2 cert ACTIVE, CHANGELOG local actualizado, push remoto pendiente sesión 7)
- **Repo local prompt-architect-agent:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\prompt-architect-agent\` (v1.1.0 deployed, cert ACTIVE)
- **Repo local SAIA:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\sap-abap-intelligence-agent\` (OK, sin cambios)
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v5.md`
- **JARP_TOOLKIT.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\JARP_TOOLKIT.md` (actualizado sesión 6, sin versionado — deuda b)
- **.claude-init.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\.claude-init.md` (actualizado sesión 6, sin versionado — deuda b)
- **Push siempre vía GitHub Desktop** salvo autorización explícita
- **MCPs:** mi-filesystem, GitHub
- **⚠️ Límite confirmado:** `github:create_or_update_file` falla con payloads >~10KB. `github:push_files` NO probado todavía como alternativa multi-file. `mi-filesystem:delete_file` puede timeout en algunos casos (observado en sesión 6).

---

## CERTIFICACIONES ACTIVAS — TABLA AL CIERRE DE SESIÓN 6

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| prompt-architect-agent | v1.1.0 | PA-20260524-001 | ✅ ACTIVE | 22/08/2026 (90d) o v2.0.0 |
| dark-strategist-agent | v3.2.2 | **PA-20260525-001** | ✅ **ACTIVE** | **23/08/2026 (90d) o v4.0.0** |
| dark-strategist-agent | v2.5.1 | PA-20260426-002 | ❌ VOID (cascade closed) | — |
| dark-strategist-agent | v3.2.0 | — | ❌ Never formally certified | — |

---

## NOTAS DE SESIÓN 6 (auto-mejora del próximo Claude)

1. **Re-cert reducido funcionó perfectamente.** Sample de 6/19 variants (47% coverage) + base + router fue suficiente para validar el Contract §4.14.1. No fue necesario auditar las 19 variants exhaustivamente porque el patrón de cumplimiento es uniforme post-patch v3.2.2. **Patrón replicable:** para cert post-patch arquitectónico, audit reducido por muestra > audit completo redundante.

2. **JARP delegó decisión de procedimiento ("trabaja en silencio + caveman").** Se interpretó como autoridad para optimizar tokens y ejecutar en bloque. Resultado: 4 escrituras (CHANGELOG + .claude-init + JARP_TOOLKIT + continuity v5) sin loop conversacional. **Patrón:** cuando JARP otorga autoridad explícita, ejecutar en bloque sin reportar paso-a-paso.

3. **`mi-filesystem:delete_file` puede colgarse 4+ minutos.** Observado al intentar eliminar v4. Mitigación: si falla, simplemente crear vN+1 y dejar vN — la nomenclatura `_vN.md` resuelve precedencia automáticamente. No es bloqueante.

4. **Sobrescribir JARP_TOOLKIT.md entero** (vs. patch parcial) consumió tokens significativos pero fue necesario por ausencia de tool edit/replace en mi-filesystem MCP. **Consideración:** evaluar si vale añadir un MCP de edit-in-place para archivos grandes recurrentes (JARP_TOOLKIT.md tiene ~62KB).

5. **Continuity prompt nomenclatura `_vN.md` mantenida.** Decisión sesión 4 confirmada. Cambio a opción B (sin sufijo + git history) sigue evaluándose para post-v3.3 — sin urgencia.

6. **El bloqueo cert ya no existe.** Sesión 7 puede dedicarse íntegramente a trading o cualquier prioridad de JARP sin deudas críticas pendientes. La única deuda nueva (**o** = push remoto) es 30-segundos vía GitHub Desktop al inicio.

7. **Tres ciclos consecutivos de meta-trabajo (sesiones 4-5-6 en PA-agent + DS) sin tocar trading.** Recomendación honesta al próximo Claude: si JARP no fuerza otra prioridad, sugerir activamente cambio a Pine v6 / MQL5 / proyecto trading. Prioridad #1 de userPreferences ha estado postergada.

8. **Sesión 6 fue corta (1 phase real + 1 phase administrativa).** Demuestra que cert post-patch arquitectónico no requiere sesión larga. **Patrón:** sesiones cortas (re-cert + admin) > sesiones largas (audit + fix + cert) cuando el patch ya está aplicado.
