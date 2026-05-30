# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 29/05/2026 (sesión 14 — limpieza de deuda barata + diagnóstico recuadro 4-ítems) | **Para:** Sesión 15
**Reemplaza:** v12 del 29/05/2026 (sesión 13)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v13.md`
**⚠️ BORRADO en este cierre:** `dark-strategist-continuity-prompt_v11.md` + `_v12.md` eliminados del repo (autorizado por JARP s14). v13 es el ÚNICO continuity vigente. Actualizar también el archivo del PROYECTO claude.ai (subir v13, quitar v12).

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 14 (resumen ejecutivo)

Sesión corta de mantenimiento. Sin tocar código de orchestrator ni el gate de regresión. Dos frentes:

### 1. Limpieza de deuda barata 🟢 — CERRADA y verificada por contenido en remoto
Repo `jarp-toolkit`, vía Ruta 3 (F&R → JARP commit por GitHub Desktop), 1 commit:
| Ítem | Fix | Verificado |
|------|-----|-----------|
| `.claude-init Nota#7` | DS `v3.2.2/PA-20260525-001` → `v3.3.0/PA-20260529-001` (+ valid-until 2026-08-27, + record DS v3.2.2 SUPERSEDED). Header `Last updated` → 29/05/2026. | ✅ contenido en remoto |
| `TK-COSMETIC` | `JARP_TOOLKIT.md` entry #30: `**Architecture v3.2.2:**` → `**Architecture v3.3.0:**` | ✅ contenido en remoto |

**Preservados intencionalmente** (registro histórico verídico, NO tocar): `NEW (v3.2.2): §4.14.1` y `Previous cert (SUPERSEDED): v3.2.2 — PA-20260525-001`. Cambiarlos falsearía cuándo nació cada cosa.

### 2. Diagnóstico read-only del recuadro 4-ítems (clon público DS, grep barato)
JARP preguntó por cerrar los 4 ítems abiertos. Verificado contra archivos reales — NO son equivalentes:

- **DSv34-DEAD** 🟡 — `tribunal.py` (379 L) + `verdict_synthesizer.py` (140 L). ✅ Confirmado **código muerto** (nada los importa; `main.py` solo cablea `ContextBuilder` + `TribunalTransversal`; sin tests; `tribunal.py` solo se auto-importa). **PERO** la doc viva los declara diseño intencional en `CLAUDE.md` L84/L87 (árbol) y `prompts/system_prompt.md` L38 ("coexisting for backward compatibility"). El system_prompt está CERTIFICADO → borrarlos dispara re-cert. **Por eso pertenece al bump de cierre v3.4** (donde la re-cert ya está prevista). Adelantarlo = doble re-cert = cuesta MÁS. **NO adelantar.**
- **DSv34-HISTORY** 🟢 — no accionable como fix. "Cerrarlo" = reconstruir historia git = invasivo + re-expone al patrón OneDrive+git que corrompió repos. **Reclasificado a ACEPTADA (registro permanente).** Cero código.
- **e3-e6** 🟡 — **mejor candidato accionable.** Solo cross-refs CHANGELOG DS↔PA-agent. Sin código, sin system prompt, **sin re-cert, sin gate**. Requiere diagnóstico: leer ambos CHANGELOGs e identificar las 4 cross-refs. **AGENDADO como primer trabajo de s15.**
- **g** 🟢 — `devil-advocate-agent` local = copia manual sin `.git/`; remoto existe. Cierre = reclonar (lo hace JARP). Caveat: reclonar dentro de `OneDrive\...\GitHub\` re-expone al patrón de corrupción. Bajo valor, sin urgencia.

---

## ⚠️⚠️ GATE DURO — NO BUMPEAR SIN REGRESIÓN ⚠️⚠️

**INTACTO desde s13. No se tocó en s14.** El bump v3.3.0→v3.4.0 y la re-cert NO deben ejecutarse hasta que la regresión E2E pase. Certificar full-coverage sobre código nunca ejecutado = validación vacía. 6 commits del core (R1-R5) sin una sola ejecución real contra documento.

**Regresión E2E requiere (JARP):**
- API key de Anthropic (Claude no la tiene; el sandbox no hace llamadas reales). **JARP declaró s13: aún no tiene key ni doc de prueba.** No reconfirmado en s14.
- Documento de prueba (>4000 chars, varios stakeholders para activar varios Rol agents).
- Confirmar: (a) prompt Forense no revienta max_tokens con handoff 8000 + N Rol agents; (b) síntesis produce `UnifiedVerdictOutput` válido + clash records; (c) `_deterministic_synthesis` fallback intacto; (d) `check_context_budget` dispara; provenance R4 presente; (e) veredicto determinista coherente (≥1 FATAL→INVIABLE).
- Claude puede entregar un **script de smoke-test E2E** listo para que JARP lo corra con su key (ofrecido s14, no solicitado aún).

---

## OPERACIÓN DE CIERRE v3.4 (tras regresión, requiere GO por fase)

1. **Regresión E2E** ← bloqueante, arriba.
2. **Bump atómico v3.3.0 → v3.4.0** (método s12): cara-de-producto (main.py print/--help, tribunal_transversal Transparency Report header v3.3.0→v3.4.0) + 19 variants (vX.3.0→vX.4.0) + router (3.3.0→3.4.0) + base (3.3.0→3.4.0) + skills si su contenido cambió. **Módulos con content-version a subir:** `budget_controller.py`, `sub_agent_spawner.py`, `prompt_engine.py`, `schema.py`, `tribunal_transversal.py`. Docstrings NO-tocados conservan versión (content-based, regla dual s12).
3. **Borrado código muerto (DSv34-DEAD):** `orchestrator/tribunal.py` + `orchestrator/verdict_synthesizer.py` + sincronizar `CLAUDE.md` L84/L87 y `prompts/system_prompt.md` L38 (quitar narrativa "v2.x preserved / coexisting"). Esto es lo que justifica meterlo en el bump (re-cert ya prevista aquí).
4. **Self-audit §4.14** + checks A-series nuevos, incluido el **invariante curva-U** (R2): MISSION en primer tercio, VERDICT en último tercio.
5. **Re-cert 7-axis Level 1 JARP DEEP full-coverage** post-bump (supersedes PA-20260529-001).
6. **Doc cleanup:** CHANGELOG [3.4.0], jarp-toolkit entry #30, README/CLAUDE, continuity v14.

---

## DEUDA TÉCNICA — POST-SESIÓN 14

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **e3-e6** | 🟡 MODERATE | Cross-refs CHANGELOG DS↔PA-agent. | **PRIMER accionable s15.** Barato, sin gate, sin re-cert. Diagnóstico: leer ambos CHANGELOGs, aislar las 4 refs, F&R Ruta 3. |
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` + `verdict_synthesizer.py` huérfanos (confirmado muerto s14) + narrativa en CLAUDE.md/system_prompt.md. | BORRAR en bump de cierre v3.4 (NO antes — doble re-cert). |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone. | Sin urgencia. Caveat OneDrive al reclonar. |
| **DSv34-HISTORY** | 🟢 ACEPTADA | Remoto = historial de UN commit raíz (`03821d1`, bootstrap, mensaje FUGA#2 pegado). Patrón OneDrive+git re-bootstrap. | Reclasificada s14 de "abierta" a registro permanente. NO investigar salvo pedido. No bloquea. |

**CERRADAS s14:** `.claude-init Nota#7`, `TK-COSMETIC`.
**CERRADAS s13:** R1-R5 (código), DSv34-BUDGET (R5), DSv34-FUGA#4.

---

## ESTADO ACTUAL VERIFICADO (29/05/2026 fin de sesión 14)

### Repo dark-strategist-agent
- **HEAD remoto (clon público s14):** `3dcf967` (docs: continuity v12 + v3.4 backlog final, cierre s13). El core R1-R5 (hasta `86b87e4`) está incorporado; doc commit encima.
- **Versión declarada:** **v3.3.0** (bump a v3.4.0 = operación de cierre PENDIENTE — gate de regresión).
- **Cert vigente:** `PA-20260529-001` ACTIVE (full coverage v3.3.0). v3.4 NO certificado (código no bumpeado ni probado — correcto).
- **config["tribunal"] keys v3.4 presentes:** `doc_window`(4000), `handoff_window`(8000), `synthesis_window`(1500), `context_budget_chars`(32000), `context_alert_percent`(70). default `max_calls_total`=40.
- **Default model:** `claude-opus-4-7`.
- **Código muerto presente** (a borrar en bump): `orchestrator/tribunal.py`, `orchestrator/verdict_synthesizer.py`.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios s13/s14.

### Repo jarp-toolkit
- **Editado s14** (cierre de 2 deudas, verificado por contenido):
  - `.claude-init.md`: Nota #7 → DS v3.3.0 / PA-20260529-001; header Last updated 29/05/2026.
  - `JARP_TOOLKIT.md`: entry #30 `Architecture v3.3.0`. Header sigue "session 12" (cosmético, no crítico).

---

## PROTOCOLO DE INICIO PARA SESIÓN 15

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo (v13).
2. Cargar este prompt (v13) + `docs/v34_backlog.md`.
3. **PHASE 0 — Verificación rápida:**
   - Confirmar v11 + v12 ya NO existen en el repo (borrados s14); v13 es el único continuity.
   - 5 config keys de v3.4 presentes. Cert registry: DS v3.3.0 (PA-20260529-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
4. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 11 SESIONES (4-14).** Prioridad #1 en userPreferences. Ya confrontado sin filtro s12+s13. **NO re-confrontar.** Si JARP vuelve a no elegir A (12ª): asumir prioridad real ≠ escrita; sugerir UNA vez reescribir userPreferences y seguir. Honestidad sobre disonancia, no acoso.
   - **(e3-e6) Cross-refs CHANGELOG** — primer accionable barato, sin gate. Leer ambos CHANGELOGs → F&R Ruta 3.
   - **(C) Regresión E2E + cierre v3.4** — continuación natural. Bloqueante para el bump. Requiere API key + doc de prueba de JARP.
   - **(B) Otra rebanada v3.4** — NO empezar sin cerrar la 1 (regla anti-apilamiento).
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+cara-de-producto siguen minor del agente; skills+docstrings de módulo = content-based).

**De s13 (vigentes):**
- **Sintetizador VIVO = `TribunalTransversal._synthesize()` → `build_synthesis_prompt`.** `verdict_synthesizer.py` + `tribunal.py` MUERTOS (main no los cablea). NO editarlos creyéndolos vivos — borrar en cierre.
- **Ventanas de contexto gobernadas por config, NO hardcoded.** Patrón `config["tribunal"].get("X_window", default)`. Nunca eliminar un límite — hacerlo configurable.
- **Distinguir clash de severity-escalation.** Clash = contradicción factual → precedencia + record. Severity disagreement → escalado. NO colapsar.
- **Poisoning: marcar frontera de confianza.** Claim upstream = UNVERIFIED; document = PRIMARY. Recovery = verificar contra fuente, no corregir encima.
- **Verificar premisas del backlog contra el archivo real ANTES de codificar.** No fabricar trabajo.
- **NO bumpear ni certificar sobre código no ejecutado** (gate de regresión).

**Reforzadas s14:**
- **No falsear registro histórico al "limpiar" versiones.** Distinguir label de estado actual (actualizable) de marcador "NEW (vX)"/"Previous cert" (histórico, intocable).
- **Borrar código muerto NO es aislado si la doc viva lo declara intencional.** Verificar refs en CLAUDE.md/system_prompt antes de borrar; si toca system prompt certificado, va en el bump (no suelto).
- **Diagnóstico read-only antes de cerrar deuda.** Clon público + grep es más barato que API reads y revela dependencias ocultas.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full (over-engineering — ventanas gobernadas lo cubren) | compactador real de tokens (sprint propio, diferido).

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v13.md` (v11+v12 borrados s14)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — clone anónimo falla; usar GitHub MCP o download_url autenticado).
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = read/verify estándar.
- **Sandbox bash:** clonar repos públicos (DS) para grep/sed/patch es MÁS barato que API reads. Patrón validado s12-s14.
- **Método de edición = Ruta 3 (F&R explícito a JARP).** El patch vive en sandbox de Claude, NO en disco de JARP. `github:create_or_update_file` prohibido (límite ~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep del marcador esperado), no solo por rotación de SHA o mensaje del commit.

### Commit sugerido para cierre sesión 14 (continuity v13 + borrado v11/v12)
```
docs: continuity v13 (session 14 close — cheap-debt cleanup + 4-item triage)

Session 14 — maintenance. Closed cheap debt (.claude-init Note#7 + TK-COSMETIC)
in jarp-toolkit, content-verified on remote. Triaged the 4 open debt items.

NEW FILE:
- dark-strategist-continuity-prompt_v13.md: replaces v12 for session 15.

DELETED:
- dark-strategist-continuity-prompt_v11.md
- dark-strategist-continuity-prompt_v12.md

STATE:
- Cheap debt CLOSED: init/toolkit cert registry synced to DS v3.3.0.
- DSv34-DEAD confirmed dead BUT deferred to v3.4 close bump (touches certified
  system_prompt -> avoid double re-cert).
- DSv34-HISTORY reclassified to ACCEPTED (registro permanente).
- e3-e6 (CHANGELOG cross-refs) = first actionable for session 15.
- HARD GATE intact: no bump/re-cert until E2E regression (needs API key, deferred).
- DS still v3.3.0, still PA-20260529-001. Trading deferred 11 sessions (4-14).
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 14

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.3.0 | PA-20260529-001 | ✅ ACTIVE (full coverage) | 27/08/2026 o v4.0.0 |

**v3.4 NO certificado** (código completo pero no bumpeado ni probado — gate de regresión).
**SUPERSEDED:** PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 14 (auto-mejora del próximo Claude)

1. **No falsear historia al sincronizar versiones.** En la limpieza TK, `Architecture v3.2.2` → `v3.3.0` (label de estado, correcto), pero `NEW (v3.2.2): §4.14.1` y `Previous cert v3.2.2` se PRESERVARON: son registro histórico verídico. Cambiarlos mentiría sobre cuándo nació cada cosa. La regla JARP "no inventes datos" aplica también a metadatos de versión.

2. **Verificar dependencias ocultas antes de cerrar una deuda que parece trivial.** DSv34-DEAD parecía "borra 2 archivos huérfanos". El grep confirmó que son muertos, PERO `CLAUDE.md` y el `system_prompt.md` CERTIFICADO los narran como diseño intencional. Borrarlos suelto dispararía una re-cert extra → doble costo. Pertenecen al bump donde la re-cert ya está prevista. Lección: una deuda barata en superficie puede arrastrar re-cert.

3. **No todos los ítems abiertos son "trabajo a hacer".** DSv34-HISTORY no es un fix — "cerrarlo" sería invasivo y re-expondría al patrón OneDrive+git. Reclasificado a ACEPTADA. A veces cerrar deuda = reconocer que no se acciona, no ejecutarla.

4. **Cierre limpio > medio-resolver.** JARP ofreció continuar con e3-e6 o cerrar. Elegí cerrar: mezclar e3-e6 (trabajo nuevo de F&R sin diagnosticar) con el borrado de v11/v12 + continuity apila trabajo. e3-e6 queda como primer accionable de s15, ya diagnosticado el camino (leer ambos CHANGELOGs).

5. **TRADING: 11 SESIONES POSTERGADO (4-14).** Ya confrontado sin filtro s12+s13. NO re-confrontar. Si en s15 vuelve a no elegir A: sugerir UNA vez reescribir userPreferences y seguir.

6. **Borrado de archivos del repo:** v11+v12 borrados del disco local s14 (autorizado). JARP commitea el borrado vía GitHub Desktop. El archivo del PROYECTO claude.ai se gestiona aparte (subir v13, quitar v12) — Claude no tiene escritura al proyecto.

7. **Continuity: migrar a subdir `continuity/` sigue pendiente.** Con el borrado de v11/v12 el directorio queda más limpio (solo v13). Reconsiderar el subdir cuando haya 3+ continuities de nuevo.
