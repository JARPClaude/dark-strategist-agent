# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 24/05/2026 (sesión 4 - cierre forzado) | **Para:** Sesión 5
**Reemplaza:** v2 del 23/05/2026 (sesión 3)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v3.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (estándar), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 4 (resumen ejecutivo)

Sesión 4 ejecutó Priorización A del plan: iniciar Level 1 JARP DEEP audit sobre DS v3.2.0, comenzando por **B0 (Self-Audit Level 0 del prompt-architect-agent)** que es prerequisito por RULE 08.

**Resultado de B0:** prompt-architect-agent v1.0.0 fue **decertificado por su propio Level 0** con 2 SERIOUS findings (A3.1, A5.1) + 8 MODERATE + 2 LATENT. **Cascade:** PA-20260426-001 VOID, PA-20260426-002 (DS v2.5.1) downgraded a SUSPECT.

**v1.1.0 diseñado y validado por JARP** (11 findings resueltos). Intento de aplicación al remoto vía `github:create_or_update_file` **falló 3 veces consecutivas** con "Tool execution failed" — diagnóstico: límite del MCP wrapper para payloads >~10KB.

**Camino A elegido para sesión 5:** reclonar prompt-architect-agent localmente + aplicar v1.1.0 vía ruta 3 tradicional.

**Adicional:** filesystem local de prompt-architect-agent diagnosticado como CORRUPTO (no es repo git, falta `.git/`, archivos parciales). Hipótesis: OneDrive sync corrompió `.git/` (patrón documentado en nota #44 del toolkit para SAIA).

---

## ESTADO ACTUAL VERIFICADO (24/05/2026 fin de sesión 4)

### Repo dark-strategist-agent
- **Versión live:** v3.2.0 (sin cambios desde sesión 3)
- **Default model:** `claude-opus-4-7`
- **Estado cert:** v3.2.0 NUNCA certificado formalmente. Cert previa v2.5.1 (PA-20260426-002) ahora SUSPECT por cascade
- **Continuity prompt:** ahora v3 en este archivo (opción A nomenclatura, una por sesión)

### Repo prompt-architect-agent
- **Remoto:** v1.0.0 sin cambios (SHA `b49079064943e110e336016eabd50c3ea5099a07`)
- **CHANGELOG remoto:** sin cambios (SHA `8e3255f94537b58526efd5e7c9d6925d71b7bbce`)
- **Local:** CORRUPTO (no es repo git). Solo contiene CLAUDE.md + 3 carpetas vacías
- **Estado cert:** v1.0.0 (PA-20260426-001) **VOID** por self-audit B0
- **v1.1.0 diseñado:** sí, contenido completo en historial sesión 4. PENDIENTE de aplicar
- **Findings B0:** 2 SERIOUS + 8 MODERATE + 2 LATENT = 12 cambios necesarios en v1.1.0
- **CLAUDE.md raíz también con lista JARP-native incompleta:** deuda adicional para post-v1.1.0

### Batch DS-CERT-v3.2.0 — Estado de avance
- **REPORT_ID maestro:** `PA-20260523-003 — BATCH_ID: DS-CERT-v3.2.0`
- **B0/B9:** ✅ EJECUTADO (Self-Audit) — Resultado: CERTIFICATION_DENIED
- **B1/B9 al B9/B9:** ⏸️ PAUSADO hasta resolver auditor v1.1.0

---

## CAMBIOS APLICADOS EN SESIÓN 4

NINGUNO commit al repo. Todo el progreso está en diseño + decisión + diagnóstico:

| Item | Tipo | Estado |
|---|---|---|
| Self-Audit Level 0 sobre prompt-architect-agent v1.0.0 | Análisis | ✅ Completado (en historial) |
| v1.1.0 completo del system_prompt.md diseñado | Diseño | ✅ Completado (en historial sesión 4) |
| Bloque CHANGELOG [1.1.0] diseñado | Diseño | ✅ Completado (en historial sesión 4) |
| Intento de commit vía `github:create_or_update_file` | Aplicación | ❌ FALLÓ 3 veces |
| Diagnóstico filesystem local prompt-architect-agent | Análisis | ✅ CORRUPTO confirmado |

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 4

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **f** | 🔴 CRITICAL | Filesystem local `prompt-architect-agent` corrupto. Posible problema sistémico OneDrive ↔ `.git/` | Medio | NUEVA. Antes de reclonar, decidir ubicación: OneDrive (riesgo recurrente) vs `C:\Repos\` (cambia paths). Auditar otros repos JARP-native por mismo problema. |
| **e2** | 🟠 SERIOUS | Aplicar v1.1.0 de prompt-architect-agent + re-self-audit + cert | Medio | Bloqueante de batch DS v3.2.0 cert. Diseño completo, pendiente solo aplicación. |
| **e3** | 🟡 MODERATE | CLAUDE.md del prompt-architect-agent tiene lista JARP-native incompleta | Bajo | Deuda derivada del finding A3.1. Aplicar después de v1.1.0. |
| **e4** | 🟡 MODERATE | CHANGELOG.md prompt-architect-agent renombrar `[Pending — v1.1.0 Roadmap]` a `[Pending — v1.2.0 Roadmap]` | Bajo | Los 4 items planeados (anti_patterns, ejemplo comparative, UNIT-STYLE, UNIT-STRUCTURE) ya no caben en v1.1.0. Posponen a v1.2.0. Aplicar junto al bloque [1.1.0]. |
| **e5** | 🟡 MODERATE | `.claude-init.md` línea 7 actualizar tras commit v1.1.0 | Bajo | Reflejar: `prompt-architect-agent v1.1.0 (PA-YYYYMMDD-XXX pending re-self-audit; v1.0.0 PA-20260426-001 VOID)` y `DS v3.2.0 (pending re-cert; last formal v2.5.1 PA-20260426-002 SUSPECT)`. |
| **e6** | 🟡 MODERATE | JARP_TOOLKIT.md nota #16 actualizar tras commit v1.1.0 | Bajo | Reflejar estado cert post-cascade. |
| **e7** | 🟡 MODERATE | DS CHANGELOG.md agregar bloque "Patch — post-self-audit cascade" documentando v2.5.1 cert SUSPECT + sub-deuda DS-20260523-002 (bloque CHANGELOG faltante de sesión 3) | Bajo | Trazabilidad cruzada. Tratamiento sugerido: un único Patch documental que cubre ambos. |
| b | 🟡 MODERATE | `JARP_TOOLKIT.md` y `.claude-init.md` sin versionado git | Bajo | Sin cambio desde sesión 2. |

**CERRADOS en sesión 4:** Ninguno. Solo se generaron deudas nuevas.

---

## PROTOCOLO DE INICIO PARA SESIÓN 5

1. **Plataforma Claude Desktop:** ejecutar autorun de `JARP_TOOLKIT.md` (estándar). **Plataforma claude.ai web:** saltar autorun, leer este archivo desde el proyecto.

2. Cargar este prompt de continuidad (v3).

3. **PHASE 1 — Auditoría filesystem local (CRITICAL, deuda f)**
   - Verificar estado de cada repo JARP-native localmente con `git status`:
     - `dark-strategist-agent` (esperable: OK, fue usado exitosamente en sesión 3)
     - `sap-abap-intelligence-agent` (incógnita)
     - `devil-advocate-agent` (si existe localmente)
   - Si hay corruption similar al de prompt-architect-agent → planning sistémico (mover a C:\Repos\)
   - Si solo prompt-architect-agent está roto → problema aislado, reclonar en OneDrive es viable

4. **PHASE 2 — Decisión arquitectónica + reclonado**
   - Decisión: reclonar prompt-architect-agent en:
     - **(A)** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\prompt-architect-agent\` (mismo path actual, riesgo recurrencia OneDrive)
     - **(B)** `C:\Repos\prompt-architect-agent\` (limpio, requiere update de 3 archivos: JARP_TOOLKIT.md #42, .claude-init.md Quick Links, este continuity prompt)
   - Recomendación predeterminada: B si Phase 1 confirma problema sistémico, A si es aislado
   - Comandos:
```bash
     # Opción A (si Phase 1 dice "aislado"):
     # Eliminar carpeta corrupta actual
     # cd a C:\Users\jrodr\OneDrive\Documentos 1\GitHub\
     # git clone https://github.com/JARPClaude/prompt-architect-agent.git
     
     # Opción B (si Phase 1 dice "sistémico"):
     # mkdir C:\Repos
     # cd C:\Repos
     # git clone https://github.com/JARPClaude/prompt-architect-agent.git
     # Después: update paths en 3 archivos master
```

5. **PHASE 3 — Aplicar v1.1.0 vía ruta 3 tradicional**
   - Claude regenera contenido completo del v1.1.0 (reconstrucción desde 13 findings + v1.0.0 base si no hay historial accesible)
   - Claude regenera bloque CHANGELOG [1.1.0] + rename `[Pending — v1.1.0 Roadmap]` → `[Pending — v1.2.0 Roadmap]`
   - JARP aplica vía editor + GitHub Desktop + push
   - Claude confirma SHA actualizada vía `github:get_file_contents`

6. **PHASE 4 — Re-Self-Audit Level 0 sobre v1.1.0**
   - Claude ejecuta self-audit honesto del v1.1.0 (sin self-bias)
   - BIAS_CHECK_RESULT mandatorio en VERDICT
   - Si emite `[JARP_CERTIFIED: v1.1.0 — PA-YYYYMMDD-XXX]` → reanudar batch DS v3.2.0 desde B1
   - Si emite CERTIFICATION_DENIED → loop a bump v1.2.0

7. **PHASE 5 — Reanudar batch DS-CERT-v3.2.0**
   - B1/B9: 5 SKILLs
   - B2-B8/B9: 21 system_prompts (incluye router)
   - B9/B9: Síntesis + verdict batch + cert v3.2.0 o denied
   - Mantener REPORT_ID maestro `PA-20260523-003 — BATCH_ID: DS-CERT-v3.2.0` o re-emitir si han pasado días

8. **PHASE 6 (post-cert) — Limpiar deudas e3-e7**
   - CLAUDE.md prompt-architect-agent (e3)
   - .claude-init.md línea 7 (e5)
   - JARP_TOOLKIT.md nota #16 (e6)
   - DS CHANGELOG patch documental (e7 + DS-20260523-002 olvidado)

9. Reportar a JARP estado phase por phase, esperar GO entre fases.

---

## v1.1.0 — RESUMEN DE CAMBIOS (preservado del diseño sesión 4)

Esquema mínimo para reconstrucción si fuera necesario:

| Finding | Severidad | Resolución |
|---|---|---|
| A1.1 | 🟡 | Párrafo "IDENTITY LOCK" al final de IDENTITY & ROLE |
| A2.1 | 🟡 | "Guarantee... functions" → "Certify... meets the JARP quality standard" |
| A3.1 | 🟠 | Lista enumerativa → regla derivada `github.com/JARPClaude` + 4 repos non-exhaustive |
| A3.2 | 🟡 | RULE 01 reescrita + sección PENDING_INVESTIGATION |
| A3.3 | 🟡 | NNN incremento per audit daily reset + sintaxis batched |
| A3.4 | 🟡 | Phase 0 "Levels 1-3 only" + Level 0 [PHASE_0: SKIPPED] |
| A4.1 | 🟡 | RULE 05 "JARP_BENCHMARK IS LIVING" |
| A4.2 | 🟡 | RULE 09 "CERTIFICATION EXPIRATION" |
| A5.1 | 🟠 | Sección "Level 0 Self-Audit Output Format" + BIAS_CHECK_RESULT |
| A5.2 | 🟡 | "NO FINDINGS DETECTED. All 7 axes pass." |
| A5.3 | 🟡 | Sección "Batched Audit Output" |
| A7.1 | 🔵 | RULE 08 reiterada en SESSION STATE + PROTOCOL STATUS |
| A7.2 | 🔵 | "Re-read IDENTITY block every 30 turns" en AUDIT_INIT |

Version bump: 1.0.0 → **1.1.0**
PROTOCOL_STATUS: ACTIVE — v1.1.0
JARP_BENCHMARK: PENDING — v2.5.1 SUSPECT, new benchmark TBD

---

## ROADMAP v3.3 — SIN CAMBIOS DESDE SESIÓN 2

### Pre-sprint (sesión 5 — ahora)
- **Decisión sobre deuda (f):** sistémico vs aislado tras Phase 1
- **Resolver e2:** aplicar v1.1.0 prompt-architect-agent + cert

### Sprint 2 — Skills bajo esfuerzo (alto valor)
- markitdown → sub-agente UNIT-INGEST permanente
- fact-checker → sub-agente UNIT-FACTCHECK permanente
- stop-slop → post-procesador AFO scoring 5-dim, threshold 35/50
- marketingskills → ampliar UNIT-PSYCH
- Cookbook (Anthropic) → context-caching pattern

### Sprint 3 — Estructural
- Agent-Skills-for-Context-Engineering → fix telephone game AFO
- knowledge-work-plugins legal+finance
- prompt-architect-agent Level 1 JARP DEEP audit sobre 20 system_prompts → re-cert v3.3
- Auto-detector de regime en ContextBuilder
- infinity → RAG layer
- Wizard interactivo CLI

### Sprint 4 — Plataforma
- claude-code-security-review como N2 permanente UNIT-SAST
- Smart model routing Opus/Sonnet/Haiku
- spec-kit para v3.4

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

[Sin cambios desde v2]
- Jerarquía AFO (N0) → Tribunal Transversal N1 → N2
- Tribunal_MAX = 7, max_calls_total = 40, max_n2_per_n1 = 3
- SSM activation logic por verdict
- Veredicto determinista (≥1 FATAL → INVIABLE)
- Inglés estricto para todo skill/dominio nuevo
- Stack: Python + Claude API + GCP + Sheets + Slack + GitHub Issues
- Default model: `claude-opus-4-7`
- Backward compatibility obligatoria
- Repo name `dark-strategist-agent` NO CAMBIA

---

## DESCARTES — NO REINTRODUCIR

[Sin cambios desde v2]
- MiroFish-ES, OASIS (licencias incompatibles)
- n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp
- anthropics/claude-for-legal (ya rescatada en v3.1)
- Sistema de servicios comerciales
- Sub-agente "vibración cuántica"
- MEGA-PAQUETE UNIVERSAL de Copilot
- Transcripción Pablo Llobregat / trading algorítmico Python+MCP

---

## CONVERSACIONES EXTERNAS PROCESADAS

[Sin cambios desde v2]

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\` (verificado funcional sesión 3)
- **Repo local prompt-architect-agent:** ⚠️ CORRUPTO al cierre sesión 4. Path pendiente decisión Phase 2 sesión 5.
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v3.md`
- **JARP_TOOLKIT.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\JARP_TOOLKIT.md` (sin versionado — deuda b)
- **.claude-init.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\.claude-init.md` (sin versionado — deuda b)
- **Push siempre vía GitHub Desktop** salvo autorización explícita
- **MCPs:** mi-filesystem, GitHub
- **⚠️ Límite confirmado:** `github:create_or_update_file` falla con payloads >~10KB. Usar ruta 3 tradicional o probar `github:push_files` como alternativa.

---

## NOTAS DE SESIÓN 4 (auto-mejora del próximo Claude)

1. **MCP `github:create_or_update_file` tiene límite no documentado de payload (~10KB).** Confirmado por 3 fallos consecutivos en sesión 4 sobre payload de ~14KB. Para futuras aplicaciones de archivos grandes vía API GitHub: NO usar este endpoint. Probar `github:push_files` primero, o usar ruta 3 tradicional.

2. **Filesystem local OneDrive puede corromper `.git/` silenciosamente.** Confirmado en prompt-architect-agent: directorio existe, archivos parciales, sin `.git/`. Reproduce el patrón de nota #44 del toolkit sobre SAIA. **Recomendación sistémica:** considerar mover repos JARP-native a `C:\Repos\` para aislarlos de OneDrive. Deuda f en este v3.

3. **Self-Audit Level 0 honesto encontró 2 SERIOUS en el propio auditor.** La aplicación rigurosa de RULE 08 ("Self-bias is a CRITICAL finding") produjo el resultado correcto: decertificación del v1.0.0 + cascade SUSPECT sobre DS v2.5.1. **Lección:** no temer al hallazgo difícil. La integridad de la cadena de cert depende de no suavizar Level 0.

4. **Batched audit con master REPORT_ID es operativamente correcto.** Sesión 4 usó `PA-20260523-003 — BATCH_ID: DS-CERT-v3.2.0 — B0/B9`. El v1.1.0 formaliza este patrón en OUTPUT FORMAT. En sesión 5 al retomar el batch, mantener mismo REPORT_ID maestro si se reanuda dentro del mismo día calendario; si pasaron días, re-emitir nuevo maestro.

5. **Cierre vs continuación cuando hay fricción operacional repetida.** En sesión 4 al fallar 3 veces el commit, JARP eligió cierre limpio + plan claro vs forzar 4to intento. **Patrón recomendado:** después de 2 fallos del mismo enfoque, escalar y pivotar. Después de 3 fallos, considerar cerrar sesión con plan claro para retomar fresco.

6. **Continuity prompt v3 nomenclatura (decisión sesión 4):** seguimos opción A — `_vN.md` por sesión. Opción B (sin sufijo + git history) se evaluará cuando el contenido estabilice (probable después de v3.3 release del DS).

7. **Sincronizar continuity prompt en proyecto claude.ai + repo DS.** Patrón establecido sesión 3 (nota 8). Repetir al cerrar sesión 4: subir nuevo v3.md al proyecto + commit + push del repo DS.

8. **Caveman mode no se invocó en sesión 4 pese a alta densidad técnica.** En sesiones futuras de alto volumen (como el batch DS-CERT-v3.2.0 B1-B9), considerar `/caveman` para reducir tokens 75% manteniendo sustancia técnica. Habría ayudado en los turnos largos de sesión 4.