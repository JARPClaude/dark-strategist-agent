# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 23/05/2026 (sesión 3) | **Para:** Próximo chat del proyecto Dark Strategist
**Reemplaza:** versión del 23/05/2026 (sesión 2)
**Ubicación nueva:** este archivo ahora vive en `dark-strategist-agent/dark-strategist-continuity-prompt_v2.md` — versionado dentro del repo (resuelve deuda b para este archivo específico)

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (estándar), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## ESTADO ACTUAL VERIFICADO (23/05/2026 fin de sesión 3)

**Repo:** `JARPClaude/dark-strategist-agent`
**Versión live:** v3.2.0 (confirmada en GitHub con badges)

**Patches documentales aplicados:**
- `DS-20260523-001` (sesión 2): CHANGELOG errata "21 domains" → "20 domains" + catalogs.py docstring + main.py default model `claude-opus-4-6` → `claude-opus-4-7` + config.example.json
- `DS-20260523-002` (sesión 3): main.py 3 referencias hardcoded `v3.0.0` → `v3.2.0` (docstring línea 2, argparse description, banner runtime)

**Inventario:**
- 20 dominios operativos (P01-P20): Trading, Legal (12 sub-áreas L01-L12), Code, Financial, Cloud, Cybersecurity, Agriculture, Real Estate, Science, Media, E-Commerce, Telecom, Public Sector, Medical, Marketing, Operations, HR, Strategy, Startup, General
- 5 skills: KAC, ACH, Deception Detection, Verdict Verification, Adaptive Autonomous Drive
- Arquitectura: AFO + Tribunal Transversal (2 capas Rol + Forense, ciegos entre sí) + SSM + GOAP A* + Sub-Agent Spawner + Budget Controller + Verdict Synthesizer + Transparency Report
- Backward compat: `tribunal.py` (v2.x) + `tribunal_transversal.py` (v3.0+) coexisten
- **Default model:** `claude-opus-4-7`
- **Estado de certificación:** v3.2.0 operacional sin re-cert formal. Última formal: v2.5.1 (PA-20260426-002). Reflejado en `.claude-init.md` línea 7 con redacción "pending formal re-cert".

**Archivos bootstrap (Claude Desktop):**
- `JARP_TOOLKIT.md`: entrada #30 sincronizada a v3.2.0 + TOP 7 to incorporate persistido + nota #16 (sin cambios en sesión 3).
- `.claude-init.md`: línea 7 actualizada en sesión 3 — refleja v3.2.0 + estado de cert pendiente.

---

## CAMBIOS APLICADOS EN SESIÓN 3

| Archivo | Cambio | Mecanismo |
|---------|--------|-----------|
| `orchestrator/main.py` | 3 referencias hardcoded `v3.0.0` → `v3.2.0` | Find & Replace local + commit DS-20260523-002 + push vía GitHub Desktop |
| `.claude-init.md` (no versionado) | Línea 7: `v2.5.1 (PA-20260426-002)` → `v3.2.0 (pending formal re-cert; last formal: v2.5.1 PA-20260426-002)` | Edit local directo + backup `.claude-init.md.bak` previo |
| `dark-strategist-continuity-prompt_v2.md` (este archivo) | Regenerado para sesión 4 + movido al repo DS | Escrito vía `mi-filesystem:write_file` |

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 3

| # | Severidad | Item | Esfuerzo | Notas |
|---|-----------|------|----------|-------|
| **e** | 🟡 MODERATE | **Re-certificación formal v3.2.0 por prompt-architect-agent** | Medio | **Deuda nueva** derivada de redacción honesta-pendiente en `.claude-init.md`. Decisión arquitectónica para sesión 4: ¿cert v3.2.0 antes de Sprint 2, o saltar directo a re-cert v3.3 (ya en Sprint 3 del roadmap)? |
| b | 🟡 MODERATE | `JARP_TOOLKIT.md` y `.claude-init.md` viven sin versionado git en `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\`. Considerar repo privado `jarp-toolkit`. | Bajo | Sin cambio respecto a sesión 2. Este continuity prompt ya NO forma parte de la deuda — está versionado en repo DS desde sesión 3. |

**CERRADOS en sesión 3:**
- ~~Fix 3 referencias hardcoded `v3.0.0` en main.py~~ → commit `DS-20260523-002`
- ~~`.claude-init.md` cita certificación obsoleta v2.5.1~~ → edit local con redacción honesta-pendiente

---

## ROADMAP v3.3 — APROBADO POR JARP (sin cambios desde sesión 2)

### Pre-sprint (sesión 4 — decisiones arquitectónicas)
- **Decisión sobre deuda (e):** ¿re-cert formal v3.2.0 ahora, o directo a v3.3?
- (Opcional) Setup repo `jarp-toolkit` para versionar master files (deuda b)

### Sprint 2 — Skills bajo esfuerzo (alto valor)
- **markitdown** → sub-agente UNIT-INGEST permanente (PDF/DOCX/PPTX/XLSX/HTML)
- **fact-checker** → sub-agente UNIT-FACTCHECK permanente
- **stop-slop** → post-procesador AFO con scoring 5-dim, threshold 35/50
- **marketingskills** → ampliar UNIT-PSYCH (~15 → 80+ sesgos)
- **Cookbook (Anthropic)** → context-caching pattern (ahorro 90% prompts dominio)

### Sprint 3 — Estructural
- **Agent-Skills-for-Context-Engineering** → fix telephone game AFO + mitigar context degradation
- **knowledge-work-plugins** legal+finance → matriz 1-25 + 4 decomposiciones financieras
- **prompt-architect-agent** Level 1 JARP DEEP audit sobre 20 system_prompts → re-certificación v3.3 (resuelve también deuda **e** si se difirió)
- Auto-detector de regime en ContextBuilder (señales lexicales del doc)
- **infinity** → RAG layer con corpus jurisdiccional (Docker + corpus)
- **Wizard interactivo CLI** (cierra gap KIMI + Copilot — usuarios no-técnicos)

### Sprint 4 — Plataforma
- **claude-code-security-review** como N2 permanente UNIT-SAST (Code + Cybersecurity)
- Smart model routing Opus/Sonnet/Haiku según tipo de N1 (patrón awesome-claude-code-subagents)
- **spec-kit** para planificar v3.4 con SDD desde inicio

---

## REPOS PARA RENDIMIENTO DE CLAUDE EN SESIONES DS (sin cambios)

- **caveman** — `/caveman` activa ~75% reducción de tokens manteniendo sustancia técnica. Crítico para sesiones largas.
- **token-ninja** — Intercepta comandos deterministas localmente.
- **omega-memory** — Cross-model MCP local-first para continuidad v3.2 → v3.3 → v3.4.
- **visual-explainer** — Auto-renderiza HTML para diagramas de arquitectura.
- **prompt-architect-agent** (TUYO) — 7-axis forensic framework para auditar los 20 system_prompts.
- **the-architect** — Blueprint 16-section antes de escribir v3.3.
- **spec-kit** — Workflow SDD `/specify → /clarify → /plan → /tasks → /implement`.
- **gstack** — `/office-hours → /plan-eng-review → /qa → /ship` cuando v3.3 vaya a producción real.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

- **Jerarquía:** AFO (N0) → Agentes Forenses N1 (ciegos entre sí, paralelos) → Sub-agentes N2 (permanentes + temporales)
- **Tribunal_MAX = 7** agentes paralelos | max_calls_total = 40 | max_n2_per_n1 = 3
- **SSM activation logic:**
  - INVIABLE → bloqueada
  - VIABLE WITH CRITICAL CORRECTIONS → automática
  - VIABLE WITH ADJUSTMENTS → automática
  - SOLID UNDER PRESSURE → opcional con flag `--ssm`
- **Veredicto determinista:** ≥1 FATAL → INVIABLE (tabla monotónica, no negociable)
- **Todo skill y dominio nuevo en inglés estricto**
- **Stack:** Python + Claude API + GCP Cloud Functions + Google Sheets + Slack webhook + GitHub Issues
- **Default model:** `claude-opus-4-7`
- **Backward compatibility obligatoria entre versiones**
- **Notificaciones automáticas:** Slack `#dark-strategist-alerts` + GitHub Issues + Google Sheets log
- **Repo name `dark-strategist-agent` NO CAMBIA bajo ninguna circunstancia**

---

## DESCARTES — NO REINTRODUCIR

- **MiroFish-ES, OASIS** (licencias AGPL/Apache incompatibles + LLM externo + stack Node.js+Neo4j)
- **n8n-mcp, claude-mem, ui-ux-pro-max-skill, agent-view, AI-Driven-Swift-Architecture, claude-code-game-studios, tradingview-mcp** (sin punto de contacto con auditoría forense)
- **anthropics/claude-for-legal** (taxonomía 12 sub-áreas YA rescatada en v3.1)
- **Sistema de servicios comerciales** (landing + cobro): infraestructura de producto, no de agente
- **Sub-agente desde post LinkedIn "vibración cuántica"** (pseudociencia)
- **MEGA-PAQUETE UNIVERSAL de Copilot** (esqueleto sin contenido — FATAL por promesa sin entregable)
- **Transcripción Pablo Llobregat / trading algorítmico Python+MCP** — pertenece a pipeline de trading personal (Pine Script v6 / MQL5 / agentic-trading), NO a Dark Strategist. Idea marginal rescatada: auto-detector de regime (Sprint 3).

---

## CONVERSACIONES EXTERNAS PROCESADAS

- **KIMI:** Puntaje 6.0/10. Rescatado: wizard, RAG, validación SSM.
- **Perplexity:** Aportó Tribunal Transversal 2-capas + VerdictOutput Pydantic + catálogos dinámicos + `regime` (integrados v3.0).
- **Copilot:** Aportó skill `adaptive-autonomous-drive` + 5 dominios v3.2 (Marketing, Operations, HR, Strategy, Startup).
- **Pablo Llobregat (sesión 2):** Descartado para DS. Aplica a trading personal.

---

## ANÁLISIS DE MERCADO REGISTRADO

Sin equivalente directo. Lo más cercano: ARCADE (paper académico), Harvey/Luminance (legal-only), FEAT (forense médica single-domain), Archer/Centraleyes (GRC continuo). Ninguno combina las 5 capas + MIT open source + Tribunal Transversal + AAD.

---

## PROTOCOLO DE INICIO PARA EL PRÓXIMO CHAT (sesión 4)

1. **Plataforma Claude Desktop:** ejecutar autorun de `JARP_TOOLKIT.md` (estándar). **Plataforma claude.ai web:** saltar autorun, leer este archivo desde el proyecto.
2. Cargar este prompt de continuidad
3. Verificar estado del repo con `github:get_file_contents` sobre:
   - `JARPClaude/dark-strategist-agent/README.md` → confirmar badge v3.2.0
   - `JARPClaude/dark-strategist-agent/CHANGELOG.md` → confirmar bloques Patch 2026-05-23 (ambos: -001 y -002)
   - `JARPClaude/dark-strategist-agent/orchestrator/main.py` → confirmar v3.2.0 en docstring + argparse + banner
4. **(Solo Claude Desktop)** verificar `.claude-init.md` línea 7 vía `mi-filesystem:read_file`
5. Reportar a JARP: "Continuidad Dark Strategist cargada (sesión 4). v3.2.0 verificada + patches DS-20260523-001 y -002 confirmados. Deuda abierta: (b) versionado master files, (e) decisión sobre re-cert formal v3.2.0. Roadmap v3.3 listo para Sprint 2."
6. Preguntar a JARP cuál pendiente prioriza — recomendar primero resolver (e) por ser bloqueante conceptual del Sprint 2 (no se puede certificar v3.3 sobre una v3.2.0 nunca certificada formalmente sin auditar el salto).

---

## REFERENCIAS RÁPIDAS

- **Repo local:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v2.md` (versionado en repo desde sesión 3)
- **JARP_TOOLKIT.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\JARP_TOOLKIT.md` (sin versionado — deuda b)
- **.claude-init.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\.claude-init.md` (sin versionado — deuda b, backup .bak existe)
- **Push siempre vía GitHub Desktop** salvo autorización explícita de JARP para `github:create_or_update_file`
- **MCPs disponibles en Claude Desktop:** mi-filesystem, GitHub
- **Reinicio MCP si falla:** `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop
- **`mi-filesystem` limitación:** solo `write_file` (sobreescritura completa), no `str_replace` ni `patch`. Para edits quirúrgicos en archivos grandes → ruta 3 (diff puro + JARP aplica) es el patrón establecido.

---

## NOTAS DE SESIÓN 3 (auto-mejora del próximo Claude)

1. **Detección de plataforma:** El system prompt genérico ("web or mobile chat interface") engañó al Claude inicial de sesión 3 a asumir claude.ai web. La señal CONFIABLE de Claude Desktop es la presencia de `mi-filesystem` con paths `C:\...`. NO confiar solo en el system prompt; verificar tools disponibles antes de descartar el autorun de `JARP_TOOLKIT.md`.

2. **Patrón de edit confirmado (Ruta 3):** Para edits quirúrgicos en archivos versionados grandes, entregar diff puro y dejar que JARP aplique vía Find & Replace + GitHub Desktop. Razones: (a) `mi-filesystem:write_file` exige reproducir 100% del archivo sin alucinación — riesgo de corrupción colateral; (b) preserva filtro humano pre-commit; (c) respeta workflow establecido. Aplicado exitosamente en `orchestrator/main.py` (8211 bytes, 3 cambios de 5 caracteres).

3. **Backup manual antes de editar archivos no-versionados:** Patrón establecido en sesión 3 sobre `.claude-init.md` → `.claude-init.md.bak`. Replicable para cualquier archivo sin git tracking antes de modificación.

4. **Redacción honesta-pendiente como patrón documental:** Cuando una métrica cambia (versión, estado, certificación) pero su validación formal no ha ocurrido, NO bumpear ciegamente. Usar formato `<nuevo_estado> (pending <validación>; last formal: <estado_previo>)`. Preserva trazabilidad + comunica honestamente la deuda. Aplicado en `.claude-init.md` línea 7. Genera deuda explícita rastreable (en este caso, deuda **e**).

5. **No extender scope silenciosamente:** En sesión 3, al observar archivos sueltos en captura de Windows Explorer, intenté agregar inventario adicional como deuda. JARP confirmó que eran archivos de prueba a eliminar. **Confrontar y preguntar antes de extender análisis** — extender scope viola user preferences explícitas.

6. **Patrón conversacional confirmado:** JARP usa "Cuál es tu mejor recomendación estratégica, táctica y operativa para poder decidir?" como ritual de validación antes de aprobar planes. Responder con framework de 3 ejes explícito + recomendación clara al frente + plan/diff concreto al final. NO validación vacía ni "depende".

7. **Movimiento del continuity prompt al repo DS:** Este archivo (`_v2.md`) ahora vive versionado en el repo. Próximas sesiones tienen dos opciones de nomenclatura — decisión pendiente para sesión 4:
   - **(A)** Crear `_v3.md` por cada sesión que actualice (historial explícito en filesystem)
   - **(B)** Renombrar a `dark-strategist-continuity-prompt.md` (sin sufijo) y delegar versionado completo a git history
   - Recomendación: opción (B) cuando estabilice el contenido. Por ahora (A) facilita revisión visual entre versiones.

8. **Confusión potencial archivo de proyecto claude.ai vs archivo de repo:** El continuity prompt vive en DOS lugares: (i) proyecto Dark Strategist en claude.ai (subido manualmente por JARP), (ii) repo DS desde sesión 3. Cuando se actualice este archivo, JARP debe sincronizar ambos: commit + push del repo + reemplazo del archivo en el proyecto claude.ai. Si solo se actualiza uno, las sesiones siguientes verán versiones inconsistentes según plataforma.
