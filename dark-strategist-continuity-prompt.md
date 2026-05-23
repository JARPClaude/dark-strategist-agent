# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 23/05/2026 (sesión 2) | **Para:** Próximo chat del proyecto Dark Strategist
**Reemplaza:** versión anterior del 23/05/2026 (sesión 1)

## Inicialización
Después del autorun de JARP_TOOLKIT.md, cargar este contexto.

---

## ESTADO ACTUAL VERIFICADO (23/05/2026 fin de sesión 2)

**Repo:** `JARPClaude/dark-strategist-agent`
**Versión live:** v3.2.0 (confirmada en GitHub con badges) — patch documental commit `DS-20260523-001` aplicado y pusheado.

**Inventario:**
- 20 dominios operativos (P01-P20): Trading, Legal (12 sub-áreas L01-L12), Code, Financial, Cloud, Cybersecurity, Agriculture, Real Estate, Science, Media, E-Commerce, Telecom, Public Sector, Medical, Marketing, Operations, HR, Strategy, Startup, General
- 5 skills: KAC, ACH, Deception Detection, Verdict Verification, Adaptive Autonomous Drive
- Arquitectura: AFO + Tribunal Transversal (2 capas Rol + Forense, ciegos entre sí) + SSM + GOAP A* + Sub-Agent Spawner + Budget Controller + Verdict Synthesizer + Transparency Report
- Backward compat: `tribunal.py` (v2.x) + `tribunal_transversal.py` (v3.0+) coexisten
- **Default model:** `claude-opus-4-7` (actualizado en sesión 2 desde claude-opus-4-6)

**JARP_TOOLKIT.md:** entrada #30 ya actualizada a v3.2.0 + TOP 7 to incorporate persistido + nota #16 sincronizada.

---

## CAMBIOS APLICADOS EN SESIÓN 2 (commit DS-20260523-001)

| Archivo | Cambio |
|---------|--------|
| `CHANGELOG.md` | Errata "21 domains" → "20 domains" + bloque Patch 2026-05-23 |
| `orchestrator/catalogs.py` | Mismo fix de errata en docstring |
| `orchestrator/main.py` | Default model `claude-opus-4-6` → `claude-opus-4-7` |
| `orchestrator/config.example.json` | Mismo upgrade de modelo |
| `JARP_TOOLKIT.md` (no versionado) | Entrada #30 reescrita a v3.2.0 + TOP 7 + BONUS + descartes |

---

## DEUDA TÉCNICA DETECTADA — NO RESUELTA AÚN

| # | Severidad | Item | Esfuerzo |
|---|-----------|------|----------|
| 1 | 🟡 MODERATE | `orchestrator/main.py` tiene 3 referencias hardcoded a `v3.0.0` (docstring línea 1 + `argparse description` + banner `print`). Deben pasar a `v3.2.0`. | Trivial — 1 commit |
| 2 | 🟡 MODERATE | `JARP_TOOLKIT.md` vive sin versionado git en `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\`. Riesgo de corrupción/pérdida histórica. Considerar crear repo privado `jarp-toolkit`. | Bajo — decisión + setup |

---

## ROADMAP v3.3 — APROBADO POR JARP

### Sprint 1 — Quick wins restantes (próxima sesión)
- Fix las 3 referencias `v3.0.0` hardcoded en `main.py`
- (Opcional) Setup repo `jarp-toolkit` para versionar el master file

### Sprint 2 — Skills bajo esfuerzo (alto valor)
- **markitdown** → sub-agente UNIT-INGEST permanente (PDF/DOCX/PPTX/XLSX/HTML)
- **fact-checker** → sub-agente UNIT-FACTCHECK permanente
- **stop-slop** → post-procesador AFO con scoring 5-dim, threshold 35/50
- **marketingskills** → ampliar UNIT-PSYCH (~15 → 80+ sesgos)
- **Cookbook (Anthropic)** → context-caching pattern (ahorro 90% prompts dominio)

### Sprint 3 — Estructural
- **Agent-Skills-for-Context-Engineering** → fix telephone game AFO + mitigar context degradation
- **knowledge-work-plugins** legal+finance → matriz 1-25 + 4 decomposiciones financieras
- **prompt-architect-agent** Level 1 JARP DEEP audit sobre 20 system_prompts → re-certificación v3.3
- Auto-detector de regime en ContextBuilder (señales lexicales del doc)
- **infinity** → RAG layer con corpus jurisdiccional (Docker + corpus)
- **Wizard interactivo CLI** (cierra gap KIMI + Copilot — usuarios no-técnicos)

### Sprint 4 — Plataforma
- **claude-code-security-review** como N2 permanente UNIT-SAST (Code + Cybersecurity)
- Smart model routing Opus/Sonnet/Haiku según tipo de N1 (patrón awesome-claude-code-subagents)
- **spec-kit** para planificar v3.4 con SDD desde inicio

---

## REPOS PARA RENDIMIENTO DE CLAUDE EN SESIONES DS

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
- **Sub-agente desde post LinkedIn de "vibración cuántica"** (pseudociencia)
- **MEGA-PAQUETE UNIVERSAL de Copilot** (esqueleto sin contenido — FATAL por promesa sin entregable)
- **Transcripción Pablo Llobregat / trading algorítmico Python+MCP** (análisis Copilot/Perplexity en sesión 2) — pertenece a pipeline de trading personal (Pine Script v6 / MQL5 / agentic-trading), NO a Dark Strategist. Solo aporta validación arquitectónica indirecta (modelos especializados + filtrado por hipótesis = lo que DS ya hace). Idea marginal rescatada: auto-detector de regime (Sprint 3).

---

## CONVERSACIONES EXTERNAS PROCESADAS

- **KIMI:** Puntaje 6.0/10. Rescatado: wizard, RAG, validación SSM.
- **Perplexity:** Aportó Tribunal Transversal 2-capas + VerdictOutput Pydantic + catálogos dinámicos + `regime` (integrados v3.0).
- **Copilot:** Aportó skill `adaptive-autonomous-drive` + 5 dominios v3.2 (Marketing, Operations, HR, Strategy, Startup).
- **Pablo Llobregat (sesión 2, transcripción + análisis Copilot):** Descartado para DS. Aplica a trading personal.

---

## ANÁLISIS DE MERCADO REGISTRADO

Sin equivalente directo. Lo más cercano: ARCADE (paper académico), Harvey/Luminance (legal-only), FEAT (forense médica single-domain), Archer/Centraleyes (GRC continuo). Ninguno combina las 5 capas + MIT open source + Tribunal Transversal + AAD.

---

## PROTOCOLO DE INICIO PARA EL PRÓXIMO CHAT

1. Ejecutar autorun de `JARP_TOOLKIT.md` (estándar)
2. Cargar este prompt de continuidad (archivo del proyecto)
3. Verificar estado del repo con `github:get_file_contents` sobre `JARPClaude/dark-strategist-agent/README.md` y `CHANGELOG.md` (confirmar v3.2.0 + presencia del bloque Patch 2026-05-23)
4. Reportar a JARP: "Continuidad Dark Strategist cargada (sesión 3). v3.2.0 verificada + patch documental DS-20260523-001 aplicado. Pendientes: (a) fix 3 referencias hardcoded v3.0.0 en main.py, (b) decisión sobre versionar JARP_TOOLKIT.md, (c) planificación v3.3 (Sprint 2 skills bajo esfuerzo recomendado como punto de partida)."
5. Preguntar a JARP cuál pendiente prioriza

---

## REFERENCIAS RÁPIDAS

- **Repo local:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **JARP_TOOLKIT.md:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\JARP_TOOLKIT.md` (sin versionado — riesgo registrado)
- **Push siempre vía GitHub Desktop** (workflow establecido)
- **mi-filesystem MCP** y **GitHub MCP** disponibles en Claude Desktop
- **Reinicio MCP si falla:** `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop
- **Limitación operativa conocida:** `mi-filesystem` solo soporta `write_file` (sobrescritura completa), no `str_replace`. Para editar archivos grandes (como `JARP_TOOLKIT.md`) hay que reescribir todo el contenido — alta carga de tokens. Considerar usar `str_replace` vía GitHub MCP cuando el archivo esté en un repo.

---

## NOTA SOBRE LA SESIÓN 2 (para auto-mejora del próximo Claude)

- Tiempo invertido en mapeo completo del ecosistema (124 repos) generó diagnóstico de TOP 7 + BONUS. Mantener este barrido como baseline; no repetirlo a menos que JARP_TOOLKIT.md crezca >20%.
- Confrontaciones técnicas que valieron la pena: (a) errata 21→20 en CHANGELOG, (b) modelo desactualizado opus-4-6, (c) descarte de transcripción Llobregat por irrelevancia para DS, (d) advertencia sobre `JARP_TOOLKIT.md` sin versionado.
- Patrón de trabajo confirmado: ediciones locales + JARP hace push vía GitHub Desktop. NO usar `github:create_or_update_file` salvo que JARP lo autorice explícitamente.
- JARP prefiere autorización puntual por cambio. Extender scope silenciosamente (ej. "aprovecho y arreglo también X") viola sus user preferences. Confrontar y preguntar siempre.
