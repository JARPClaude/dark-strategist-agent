# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 29/05/2026 (sesión 13 — REBANADA Reliability core v3.4 CÓDIGO-COMPLETA, sin cerrar) | **Para:** Sesión 14
**Reemplaza:** v11 del 29/05/2026 (sesión 12)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v12.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 13 (resumen ejecutivo)

Sesión 13 **abrió el sprint v3.4** (JARP eligió B sobre A-trading → **10ª postergación de trading consecutiva, sesiones 4-13**) y ejecutó la **rebanada 1: Reliability core** — fix del telephone-game / context-degradation en el pipeline AFO→Tribunal→N2. Anclado en `Agent-Skills-for-Context-Engineering/skills/context-degradation` v2.1.0.

**Resultado: rebanada CÓDIGO-COMPLETA (R1-R5), 6 commits, SHA-verificados. NO cerrada — falta regresión E2E (bloqueante) + bump + re-cert.**

### Lo ejecutado (7 commits incl. backlog open + docs)
| ID | Patrón | Commit | Fix |
|----|--------|--------|-----|
| R1·#2 | clash (doc) | `fe007a7` | Ventana doc unificada N1=N2 → `doc_window` (4000). SSM excluida. |
| R1·#1 | telephone-game | `f808cda` | Handoff Rol→Forense full-fidelity. `concerns[:2]` eliminado; pasa assumptions/info_demanded/stance_reasoning/perspective con provenance → `handoff_window` (8000). |
| R1·#3 | compress | `c35b4db` | Findings ESTRUCTURADOS al sintetizador vivo → `synthesis_window` (1500) fallback. |
| R2 | lost-in-middle | — | **NO-OP VERIFICADO.** 21 prompts YA cumplen curva-U. No reordenar. |
| R3 | clash | `d27ef18` | Clash annotation protocol (precedencia FORENSE>ROL + records estructurados, prohibido silent pick). |
| R4 | poisoning | `5d7d0b0` | Circuit-breaker N2: parent_report=UNVERIFIED, document=PRIMARY. |
| R5 | non-linear cliff | `86b87e4` | `check_context_budget()` 70% alert + fix default 30→40 (DSv34-BUDGET resuelta). |

Backlog v3.4 canónico actualizado en `docs/v34_backlog.md` (estado completo + operación de cierre + deuda).

---

## ⚠️⚠️ GATE DURO — NO BUMPEAR SIN REGRESIÓN ⚠️⚠️

**El bump v3.3.0→v3.4.0 y la re-cert NO deben ejecutarse hasta que la regresión E2E pase.** Certificar full-coverage sobre código nunca ejecutado = validación vacía, exactamente lo que el sistema existe para detectar. 6 commits del core sin una sola ejecución real contra documento. Esto es la opción E (>1 mes certificado sin uso real) vuelta cuello de botella.

**Regresión E2E requiere (JARP, sesión 14 o más adelante):**
- API key de Anthropic (Claude no la tiene; el sandbox no hace llamadas reales). **JARP declaró s13: aún no tiene key ni doc de prueba — verlo más adelante.**
- Documento de prueba (>4000 chars, varios stakeholders para activar varios Rol agents).
- Confirmar: (a) prompt Forense no revienta max_tokens con handoff 8000 + N Rol agents; (b) síntesis produce `UnifiedVerdictOutput` válido + clash records con formato pedido; (c) `_deterministic_synthesis` fallback intacto; (d) `check_context_budget` dispara; provenance R4 presente; (e) veredicto determinista coherente (≥1 FATAL→INVIABLE).
- Claude puede entregar un **script de smoke-test E2E** listo para que JARP lo corra con su key.

---

## OPERACIÓN DE CIERRE v3.4 (tras regresión, requiere GO por fase)

1. **Regresión E2E** ← bloqueante, arriba.
2. **Bump atómico v3.3.0 → v3.4.0** (método s12): cara-de-producto (main.py print/--help, tribunal L381 Transparency Report header v3.3.0→v3.4.0) + 19 variants (vX.3.0→vX.4.0) + router (3.3.0→3.4.0) + base (3.3.0→3.4.0) + skills si su contenido cambió. **Módulos con content-version a subir** (su contenido SÍ cambió en v3.4): `budget_controller.py` (2.8.0→), `sub_agent_spawner.py` (2.8.0→), `prompt_engine.py`, `schema.py`, `tribunal_transversal.py`. Docstrings de módulo NO-tocados conservan su versión (content-based, regla dual s12).
3. **Borrado código muerto (DSv34-DEAD):** `orchestrator/tribunal.py` + `orchestrator/verdict_synthesizer.py`.
4. **Self-audit §4.14** + checks A-series nuevos, incluido el **invariante curva-U** (R2): MISSION en primer tercio, VERDICT en último tercio.
5. **Re-cert 7-axis Level 1 JARP DEEP full-coverage** post-bump (supersedes PA-20260529-001).
6. **Doc cleanup:** CHANGELOG [3.4.0], jarp-toolkit entry #30 (+ TK-COSMETIC pendiente de v3.2.2), README/CLAUDE, continuity v13.

---

## DEUDA TÉCNICA — POST-SESIÓN 13

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` (v2.9.0) + `verdict_synthesizer.py` (v2.8.0) huérfanos. main solo cablea TribunalTransversal. | BORRAR en bump de cierre. |
| **DSv34-HISTORY** | 🟢 LOW (registro) | **Remoto = historial git de UN solo commit raíz** (`03821d1`, bootstrap masivo con mensaje de FUGA#2 pegado encima). NO contiene la historia de 13 sesiones que las continuities asumen. Compatible con patrón OneDrive+git re-bootstrap documentado. | Anotado. NO investigar salvo que JARP lo pida. **No bloquea** — base de código correcta y verificada por SHA toda la sesión. JARP puede querer confirmar si hubo reclonado/reinit reciente. |
| **TK-COSMETIC** | 🟢 LOW | jarp-toolkit entry #30 descripciones arquitectónicas `v3.2.2` sin actualizar. | Limpiar en próxima edición toolkit. |
| **.claude-init Nota#7** | 🟢 LOW (s13) | `.claude-init.md` Nota #7 declara DS v3.2.2 / PA-20260525-001 (stale; debería v3.3.0 / PA-20260529-001). Drift en archivo de init, no afecta runtime. | F&R en próxima edición de docs. |
| **e3-e6** | 🟡 MODERATE | Cross-refs CHANGELOG DS↔PA-agent | Residuales menores |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone | Sin urgencia |

**CERRADAS s13:** R1-R5 (código), DSv34-BUDGET (R5), DSv34-FUGA#4 (lectura: código muerto identificado).

---

## ESTADO ACTUAL VERIFICADO (29/05/2026 fin de sesión 13)

### Repo dark-strategist-agent
- **HEAD remoto:** `86b87e4` (tras R5). Todo el orchestrator compila; config.example.json válido.
- **Versión declarada:** sigue **v3.3.0** (el bump a v3.4.0 es operación de cierre PENDIENTE — gate de regresión).
- **Cert vigente:** `PA-20260529-001` ACTIVE (full coverage v3.3.0). NO re-certificado para v3.4 (correcto: código no bumpeado ni probado).
- **config["tribunal"] nuevas keys:** `doc_window`(4000), `handoff_window`(8000), `synthesis_window`(1500), `context_budget_chars`(32000), `context_alert_percent`(70). default `max_calls_total`=40.
- **Default model:** `claude-opus-4-7`.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios s13.

### Repo jarp-toolkit
- Sin cambios s13. Entry #30 DS → v3.3.0 / PA-20260529-001 (sigue correcto; v3.4 aún no publicado).

---

## PROTOCOLO DE INICIO PARA SESIÓN 14

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo.
2. Cargar este prompt (v12) + `docs/v34_backlog.md`.
3. **PHASE 0 — Verificación rápida:**
   - HEAD remoto = `86b87e4` (o posterior si JARP siguió). Las 5 config keys de v3.4 presentes.
   - Cert registry: DS v3.3.0 (PA-20260529-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
4. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 10 SESIONES (4-13).** Prioridad #1 en userPreferences. Ya confrontado s12 + s13. Si JARP vuelve a no elegir A en s14 (11ª): NO re-confrontar (ya dicho sin filtro 2 veces). Asumir que la prioridad real ≠ la escrita; sugerir UNA vez reescribir userPreferences y seguir.
   - **(C) Regresión E2E + cierre v3.4** — la continuación natural. Bloqueante para el bump. Requiere API key de JARP. Si JARP tiene key → script smoke-test → regresión → bump → re-cert.
   - **(B) Otra rebanada v3.4** — 4× Bajo / Wizard CLI / knowledge-work matrices. NO empezar otra rebanada sin cerrar la 1 (regla anti-apilamiento; ya se apilaron R1-R5 sin probar).
   - **(E) Field-test real DS** — coincide con la regresión; matar dos pájaros.
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+cara-de-producto siguen minor del agente; skills+docstrings de módulo = content-based).

**NUEVAS / REFORZADAS s13:**
- **Sintetizador VIVO = `TribunalTransversal._synthesize()` → `build_synthesis_prompt`.** `verdict_synthesizer.py` + `tribunal.py` están MUERTOS (main no los cablea). NO editarlos creyéndolos vivos — borrar en cierre.
- **Ventanas de contexto gobernadas por config, NO hardcoded.** Patrón `config["tribunal"].get("X_window", default)`. Nunca eliminar un límite — hacerlo configurable.
- **Distinguir clash de severity-escalation.** Clash = contradicción factual entre fuentes → precedencia + record. Severity disagreement → escalado. NO colapsar ambos.
- **Poisoning: marcar frontera de confianza.** Claim upstream = UNVERIFIED; document = PRIMARY SOURCE. Recovery = verificar contra fuente, no corregir encima.
- **Verificar premisas del backlog contra el archivo real ANTES de codificar.** R2 (curva-U) resultó no-op: los prompts ya cumplían. No fabricar trabajo.
- **NO bumpear ni certificar sobre código no ejecutado** (gate de regresión).

---

## DESCARTES — NO REINTRODUCIR
[Sin cambios desde v8-v11.] MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun.
**Nuevo descarte s13:** `HandoffPacket` Pydantic full (over-engineering — los handoffs se serializan a string en prompts; las ventanas gobernadas + emisión estructurada lo cubren mejor). Compactador real de tokens (sprint propio, no minor — diferido).

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v12.md`
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — clone anónimo falla; usar GitHub MCP o download_url autenticado).
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = read/verify estándar.
- **Sandbox bash:** clonar repos públicos (DS) para grep/sed/patch es MÁS barato que API reads. Patrón validado s12-s13.
- **Método de edición = Ruta 3 (F&R explícito a JARP).** El patch vive en sandbox de Claude, NO en disco de JARP. `github:create_or_update_file` prohibido (límite ~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por SHA en clon nuevo.** Un commit puede subir con mensaje correcto + contenido equivocado (capturado s13).

### Commit sugerido para cierre sesión 13 (continuity v12)
```
docs: continuity prompt v12 (session 13 close — v3.4 Reliability core code-complete)

Session 13 — opened sprint v3.4, executed Reliability core slice (R1-R5),
6 commits SHA-verified. Slice CODE-COMPLETE, NOT closed.

NEW FILE:
- dark-strategist-continuity-prompt_v12.md: replaces v11 for session 14.

STATE:
- v3.4 Reliability core code-complete: R1 (handoff fidelity, 3 leaks),
  R2 (U-curve no-op verified), R3 (clash annotation), R4 (poisoning
  circuit-breaker), R5 (context-budget alert + default fix).
- HARD GATE: no bump/re-cert until E2E regression passes (needs API key, deferred).
- DS still v3.4 NOT bumped, still PA-20260529-001 (v3.3.0). Correct.
- Trading deferred 10 consecutive sessions (4-13).
- DSv34-HISTORY: remote has single-commit root history (OneDrive+git re-bootstrap pattern).
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 13

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.3.0 | PA-20260529-001 | ✅ ACTIVE (full coverage) | 27/08/2026 o v4.0.0 |

**v3.4 NO certificado** (código completo pero no bumpeado ni probado — gate de regresión).
**SUPERSEDED:** PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 13 (auto-mejora del próximo Claude)

1. **El commit `03821d1` reveló que el remoto NO tiene la historia que la continuity asume.** Es un único commit raíz (bootstrap) con el mensaje de FUGA#2 pegado. Las verificaciones por SHA en clon nuevo lo capturaron — un commit subió con mensaje correcto pero contenido equivocado (creó archivos en vez de aplicar el patch). LECCIÓN: SIEMPRE verificar post-push por contenido real (grep del marcador esperado), no solo por rotación de SHA o por el mensaje del commit.

2. **El patch vive en el sandbox de Claude, NO en el disco de JARP.** El primer intento de FUGA#2 falló porque entregué "aplica /tmp/fuga2.patch" — JARP no tiene ese archivo. GitHub Desktop commiteó lo que estaba staged (otra cosa). LECCIÓN: entregar SIEMPRE F&R explícito línea por línea. Nunca asumir que JARP puede correr `git apply` sobre un patch del sandbox.

3. **Verificar premisas del backlog contra el archivo real.** R2 (curva-U) se asumía pendiente; el archivo real mostró que los 21 prompts YA cumplen. Declararlo no-op verificado en vez de fabricar un reordenamiento riesgoso. No inflar trabajo.

4. **Distinguir over-engineering de fix proporcional.** R1 NO necesitó un `HandoffPacket` Pydantic (los handoffs se serializan a string). Ventanas gobernadas + emisión estructurada lo cubren con menos riesgo. R5 NO necesitó un compactador real (sprint propio) — un alert observable basta para el minor.

5. **No eliminar límites al "mejorar".** En FUGA#1 mi primer intento quitó `[:2000]` por completo → habría desbordado max_tokens. Lo corregí a ventana gobernada. La regla de JARP (no romper edge-case coverage) capturó el error antes del commit.

6. **TRADING: 10 SESIONES POSTERGADO (4-13).** Confrontado UNA vez s13 (JARP eligió B con la confrontación leída). NO re-confrontar en s14 si vuelve a no elegir A — ya dicho sin filtro 2 veces (s12, s13). Sugerir UNA vez reescribir userPreferences y seguir. Honestidad sobre disonancia, no acoso.

7. **JARP apiló R1-R5 sin regresión intermedia (decisión propia, confrontada).** Riesgo: si la regresión falla, 6 commits que desenredar. El próximo Claude: la regresión E2E es el PRIMER trabajo real de cierre, bloqueante, antes de cualquier bump.

8. **Continuity sigue creciendo (v11<v12).** Pendiente histórico: migrar a subdir `continuity/`. Por ahora `_vN.md`.
