# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 24/05/2026 (sesión 5 - cierre exitoso) | **Para:** Sesión 6
**Reemplaza:** v3 del 24/05/2026 (sesión 4)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v4.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (estándar), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 5 (resumen ejecutivo)

Sesión 5 ejecutó el **batch completo DS-CERT-v3.2.0** (PHASE 1 a PHASE 5 del continuity v3 + cierre completo).

**Resultados principales:**

1. **PHASE 1 — Auditoría filesystem local:** confirmó que la corruption de `prompt-architect-agent` era un evento aislado, no sistémico. DS y SAIA con `.git/` íntegro. Refutó la hipótesis "OneDrive corrompe sistemáticamente repos JARP-native". Decisión: reclonar PA-agent en mismo path OneDrive (opción A).

2. **PHASE 2 — Reclone:** ejecutado exitosamente vía PowerShell (`git clone`). 22 objetos, 18.32 KiB. Estructura completa restaurada.

3. **PHASE 3 — Aplicar v1.1.0 a prompt-architect-agent:** 13 findings resueltos. 3 archivos commited (system_prompt v1.1.0 + CHANGELOG + LICENSE MIT nuevo).

4. **PHASE 4 — Re-Self-Audit Level 0:** **prompt-architect-agent v1.1.0 → JARP_CERTIFIED bajo PA-20260524-001.** 6 MODERATE + 3 LATENT residuales para v1.2.0 (no bloqueantes).

5. **PHASE 5 — Batch DS-CERT-v3.2.0 ejecutado completo (B0 a B9):**
   - B0: cascade-resolved en auditor v1.1.0
   - B1: 5 SKILLs passed with notes
   - B2: 1 CRITICAL + 2 SERIOUS → resueltos vía patch DS v3.2.1
   - B3-B8: 19 SERIOUS bloqueantes (todos del mismo patrón sistémico) → resueltos vía patch DS v3.2.2
   - B9: BATCH_SYNTHESIS cerrado, **DS v3.2.2 desplegado y verificado en remoto**

6. **Patches aplicados al repo DS en sesión 5:**
   - **v3.2.1** (B2 fixes): system_prompt.md (v2.5.1 → v3.2.0 + ARCHITECTURAL LAYERS) + system_prompt_router.md (v2.7.0 → v3.2.0-ROUTER, catálogo P15-P20 reachable) + CHANGELOG
   - **v3.2.2** (B3-B8 fixes): system_prompt.md (v3.2.0 → v3.2.2 + §4.14.1 Domain Variant Contract) + 19 domain variants (Output Format + naming + footer estandarizados) + CHANGELOG. **Total 21 archivos modificados en este patch.**

7. **Cascade resuelta:**
   - `PA-20260426-001` (PA-agent v1.0.0 cert): VOID (sesión 4)
   - `PA-20260426-002` (DS v2.5.1 cert): VOID (sesión 5, al cerrar batch)
   - `PA-20260524-001` (PA-agent v1.1.0 cert): **ACTIVE** ✅

---

## ESTADO ACTUAL VERIFICADO (24/05/2026 fin de sesión 5)

### Repo prompt-architect-agent
- **Remoto:** v1.1.0 desplegado y verificado
- **Estado cert:** `PA-20260524-001` ACTIVE (válida hasta 22/08/2026 o major bump v2.0.0)
- **Findings residuales para v1.2.0:** 6 MODERATE + 3 LATENT (lista en historial sesión 5)
- **Local:** OK (reclonado en sesión 5, integridad confirmada)

### Repo dark-strategist-agent
- **Versión live:** **v3.2.2** (composed agent)
- **Versión base file:** v3.2.2 (stamp alineado)
- **Versión router:** v3.2.0-ROUTER (válido — bind rule es minor version, no patch)
- **Default model:** `claude-opus-4-7`
- **Estado cert:** ⚠️ **NO certificado aún.** v2.5.1 cert (PA-20260426-002) ahora VOID. Cert v3.2.2 pendiente de re-audit reducido en sesión 6.
- **Local:** OK
- **21 archivos del patch v3.2.2 verificados con SHA en remoto** (ver historial sesión 5 para lista completa)

### Repo sap-abap-intelligence-agent
- **Local:** OK (verificado sesión 5 PHASE 1). `.git/` íntegro.
- **Estado:** sin tocar en sesión 5

### Repo devil-advocate-agent
- **Local:** archivos presentes pero sin `.git/` (nunca fue clonado, copia manual)
- **Deuda g (LOW):** normalizar a `git clone` post-cert DS v3.2.2

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 5

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **k** | 🟠 SERIOUS | Re-cert DS v3.2.2 vía batch reducido (verificación Contract §4.14.1 compliance) | Bajo | Bloqueante para que DS recupere JARP_CERTIFIED status. Mucho más rápido que DS-CERT-v3.2.0 — no audit completo, solo conformance check. |
| **l** | 🟡 MODERATE | Actualizar JARP_TOOLKIT.md nota #16 + descripción del repo DS (mencionar v3.2.2 + §4.14.1 + 19 variants) | Bajo | Cuando se confirme cert v3.2.2 |
| **m** | 🟡 MODERATE | Actualizar `.claude-init.md` línea 7 con estados cert actualizados | Bajo | Reflejar: `prompt-architect-agent v1.1.0 (PA-20260524-001 ACTIVE)` y `dark-strategist-agent v3.2.2 (pending re-cert)` |
| **n** | 🟡 MODERATE | DS Sprint v3.3: 38 MODERATE + 23 LATENT findings residuales del batch | Medio | Plan separado (ver sección ROADMAP) |
| **g** | 🟢 LOW | `devil-advocate-agent` está como copia manual, no como git clone — normalizar | Bajo | Post-cert DS v3.2.2 |
| **h** | 🟢 LOW | Actualizar nota #44 toolkit: la corruption SAIA no se materializó; evento PA-agent fue aislado | Bajo | Post-cert DS v3.2.2 |
| **i** | 🟢 LOW | (RESUELTO en sesión 5) LICENSE MIT añadido a prompt-architect-agent | — | Cerrado |
| **e3-e7** | 🟡 MODERATE | Deudas del continuity v3 sobre CLAUDE.md PA-agent, .claude-init.md, CHANGELOG cross-references | Bajo | Post-cert DS v3.2.2 |
| **b** | 🟡 MODERATE | JARP_TOOLKIT.md y .claude-init.md sin versionado git | Bajo | Sin cambio desde sesión 2 |
| **f** | (RESUELTO) | Filesystem PA-agent corrupto | — | Cerrado en sesión 5 PHASE 1-2 |

**CERRADOS en sesión 5:**
- Deuda **e2** (Aplicar v1.1.0 a prompt-architect-agent + cert) ✅
- Deuda **f** (filesystem PA-agent corrupto) ✅
- Deuda **i** (LICENSE PA-agent) ✅
- Deuda **e4** (CHANGELOG PA-agent rename v1.1.0 Roadmap → v1.2.0) ✅

**NUEVAS deudas generadas en sesión 5:**
- Deuda **k** (re-cert DS v3.2.2) — bloqueante hasta resolver
- Deuda **n** (Sprint v3.3 con 38 MODERATE + 23 LATENT)

---

## PROTOCOLO DE INICIO PARA SESIÓN 6

1. **Plataforma Claude Desktop:** ejecutar autorun de `JARP_TOOLKIT.md` (estándar). **Plataforma claude.ai web:** saltar autorun, leer este archivo desde el proyecto.

2. Cargar este prompt de continuidad (v4).

3. **PHASE 1 — Re-Cert DS v3.2.2 (deuda k — bloqueante)**
   - Auditor: prompt-architect-agent v1.1.0 (PA-20260524-001)
   - Tipo: **batch reducido de conformance check** contra Contract §4.14.1, no audit completo
   - Targets a verificar (alguno por muestra estadística + base + router):
     - `prompts/system_prompt.md` (verificar §4.14.1 íntegro + ARCHITECTURAL LAYERS coherente)
     - `prompts/system_prompt_router.md` (consistency check post-Contract)
     - 4-5 domain variants random (verificar Contract compliance: Output Format declared, footer canónico, naming convention applied)
   - Verificar específicamente:
     - (a) Cada variant tiene sección `## OUTPUT FORMAT` explícita
     - (b) Footer canónico presente: `[PROTOCOL_STATUS] + [BASE_PROTOCOL] + [CONTRACT]`
     - (c) Rule prefixes correctos según naming convention
     - (d) Severity mapping consistency (no FATAL en items que la taxonomy define como SERIOUS)
     - (e) P03 Legal Geofence monotónica
     - (f) P08 Agro Yield reclasificada SERIOUS
   - Si pasa → emitir `[JARP_CERTIFIED: DS v3.2.2 — PA-YYYYMMDD-NNN]`
   - Si nuevos findings → loop micro-fix

4. **PHASE 2 — Actualización operacional (deudas l + m + e3-e7)**
   Solo después de cert v3.2.2 confirmada:
   - JARP_TOOLKIT.md nota #16: estado cert post-batch
   - .claude-init.md línea 7: estados cert actualizados
   - PA-agent CLAUDE.md (deuda e3): lista JARP-native incompleta
   - DS CHANGELOG patch documental (deuda e7): cross-references cascade

5. **PHASE 3 — Decisión de roadmap (deudas n + g + h)**
   - ¿Iniciar Sprint v3.3 ya (38 MODERATE + 23 LATENT)?
   - ¿O priorizar otros proyectos: trading (Pine v6 + MQL5), v1.2.0 PA-agent, devil-advocate-agent normalizado?
   - Sugerencia: **descansar tras 3 patches consecutivos (v3.2.1 + v3.2.2 + cert v3.2.2)** y dedicar siguiente sesión a trading/proyectos personales JARP. v3.3 puede esperar.

6. Reportar a JARP estado phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 — ACTUALIZADO POST-SESIÓN 5

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

**Bloque pre-existente — Sprint 2 (sin cambios desde v3):**
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

[Heredado de v3, sin cambios excepto adiciones]
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
- **NUEVO (sesión 5):** **§4.14.1 Domain Variant Contract** rige toda variante futura (Output Format, Footer, Severity Mapping, Naming Convention, Versioning sub-contracts)
- **NUEVO (sesión 5):** Naming convention de rules cross-domain inmutable (T=Trading, LG=Legal, CY=Cybersecurity, CL=Cloud, A=Agro, RE=RealEstate, S=Science, M=Media, EC=Ecommerce, TC=Telecom, PS=PublicSector, MD=Medical, MK=Marketing, OP=Operations, HR=HR, ST=Strategy, SU=Startup, C=Code, F=Financial)

---

## DESCARTES — NO REINTRODUCIR

[Sin cambios desde v3]
- MiroFish-ES, OASIS (licencias incompatibles)
- n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp
- anthropics/claude-for-legal (ya rescatada en v3.1)
- Sistema de servicios comerciales
- Sub-agente "vibración cuántica"
- MEGA-PAQUETE UNIVERSAL de Copilot
- Transcripción Pablo Llobregat / trading algorítmico Python+MCP

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\` (v3.2.2 deployed, verificado sesión 5)
- **Repo local prompt-architect-agent:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\prompt-architect-agent\` (v1.1.0 deployed, reclonado limpio sesión 5)
- **Repo local SAIA:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\sap-abap-intelligence-agent\` (OK, `.git/` íntegro)
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v4.md`
- **JARP_TOOLKIT.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\JARP_TOOLKIT.md` (sin versionado — deuda b)
- **.claude-init.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\.claude-init.md` (sin versionado — deuda b)
- **Push siempre vía GitHub Desktop** salvo autorización explícita
- **MCPs:** mi-filesystem, GitHub
- **⚠️ Límite confirmado:** `github:create_or_update_file` falla con payloads >~10KB. Usar ruta 3 tradicional (editor + GitHub Desktop). `github:push_files` NO probado todavía como alternativa multi-file.

---

## CERTIFICACIONES ACTIVAS — TABLA AL CIERRE DE SESIÓN 5

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| prompt-architect-agent | v1.1.0 | PA-20260524-001 | ✅ ACTIVE | 22/08/2026 (90d) o v2.0.0 |
| dark-strategist-agent | v3.2.2 | — | ⚠️ PENDING (re-cert sesión 6) | — |
| dark-strategist-agent | v2.5.1 | PA-20260426-002 | ❌ VOID (cascade closed) | — |
| dark-strategist-agent | v3.2.0 | — | ❌ Never formally certified | — |

---

## NOTAS DE SESIÓN 5 (auto-mejora del próximo Claude)

1. **Modo silencioso + caveman funcionó.** Tokens reducidos ~60% en B4-B8 manteniendo rigor del audit. **Patrón replicable:** cuando JARP pide trabajar en silencio + el batch tiene patrones sistémicos repetitivos, no expandir cada sub-audit individualmente — agregar findings al patrón maestro.

2. **`github:push_files` NO se probó en sesión 5.** Para próximas aplicaciones multi-file, vale la pena testearlo antes de descartar — podría ahorrar fricción de 21-file ruta 3 tradicional.

3. **El patrón "patch consolidado al final del batch" es superior a "pause-fix-resume por sub-batch".** Sesión 5 lo validó: opción B (continuar + batch-fix consolidado) produjo v3.2.2 con 1 commit grande vs 5-6 commits intermedios que habrían fragmentado el CHANGELOG.

4. **Domain Variant Contract §4.14.1 es replicable como patrón.** Cuando se detectan ≥3 findings del mismo tipo across un catálogo, NO se fixean uno por uno — se introduce un contract en la capa base y se aplica uniformemente. Esto convierte 19 fixes individuales en 1 intervención arquitectónica + 19 alineamientos mecánicos.

5. **PowerShell command era el camino correcto para 21 archivos.** Más rápido y a prueba de errores que arrastrar+soltar en Explorer. **Patrón:** para patches multi-file (>5 archivos), preferir comando PowerShell desde Downloads.

6. **Continuity prompt v4 nomenclatura mantenida (opción A `_vN.md`).** Decisión sesión 4 confirmada. Cambio a opción B (sin sufijo + git history) sigue evaluándose para post-v3.3.

7. **Sincronizar continuity prompt en proyecto claude.ai + repo DS.** Patrón establecido sesión 3. Repetir al cerrar sesión 5: subir nuevo v4.md al proyecto + commit + push del repo DS.

8. **Tres patches en una sola sesión (v3.2.1 → v3.2.2 + PA-agent v1.1.0) es alto volumen — no replicar habitualmente.** JARP toleró bien pero la calidad cognitiva del audit es mejor con 1-2 ciclos por sesión. Para sesión 6: máximo 1 patch (re-cert v3.2.2 verificación + posible micro-fix).
