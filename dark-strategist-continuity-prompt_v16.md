# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 31/05/2026 (sesión 17 — bump v3.4.0 completo, pusheado y verificado) | **Para:** Sesión 18
**Reemplaza:** v15 del 30/05/2026 (sesión 16)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v16.md`
**⚠️ BORRADO en este cierre:** `dark-strategist-continuity-prompt_v15.md` eliminado del repo (autorizado por JARP s17). v16 es el ÚNICO continuity vigente. Actualizar también el archivo del PROYECTO claude.ai (subir v16, quitar v15).

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 17 (resumen ejecutivo)

Sesión de cierre completo del bump v3.4.0. Se destrabó la API key, se cerró el gate vivo (b), y se ejecutó el bump atómico entero (contenido + versión + commit + push + verificación por contenido). El repo quedó en **v3.4.0**, **NOT YET CERTIFIED**.

### 1. API key — DESTRABADA y FONDEADA
- El blocker de s16 era pago Stripe, NO la cuenta. Hallazgos de la sesión:
  - El form "Contact sales" rechaza dominios personales (hotmail) — **es la puerta equivocada**, no tiene relación con fondear. El fondeo va por **Console → Plans & Billing → Add funds**, no por ventas.
  - `js.stripe.com/v3/` SÍ cargaba → el bloqueo no era de todo Stripe, solo de subdominios de telemetría (`m.stripe.com`). El modal de pago colgaba esperando esa telemetría.
  - **JARP fondeó $5 exitosamente** (saldo confirmado USD 5.00). Recarga automática OFF.
- **Gasto de la sesión:** 2 corridas vivas de ~$1.67 c/u → **saldo restante ≈ $1.66.** NO alcanza para otra corrida viva completa sin re-fondear.
- Patrón para fondeo futuro: si el modal cuelga, hotspot móvil / DNS 1.1.1.1 / allowlist `m.stripe.com`+`api.stripe.com` en bloqueadores de privacidad.

### 2. Gate vivo (b) — CERRADO (vía fallback, aceptado por diseño)
- Corrida viva real contra `claude-opus-4-7` (379s): `12 PASS / 0 SKIP / 0 FAIL` → gate cleared.
- **PERO (b) NO demostró parse limpio de Opus.** Dos corridas revelaron que la salida viva del modelo NO parsea directo a `UnifiedVerdictOutput`:
  - 1ª corrida: `moderate_findings` sin `severity/evidence/root_cause` → Pydantic rechaza → fallback determinista.
  - 2ª corrida (post-fix SHAPE): `Synthesis failed: Unterminated string` (JSON truncado/malformado) → fallback determinista.
- **El check `b_unified_output` pasa porque su criterio es laxo** (final_verdict + conflicts_detected lista + budget en reporte), NO que Opus produzca el shape. El **fallback determinista es el sintetizador de producción real para docs ricos** — es componente diseñado y validado (`c_fallback_intact`), produce veredictos correctos de alta calidad (18 FATAL bien fundados sobre el contrato de prueba). Aceptado como degradación elegante por diseño → **DSv34-SYNTH**.
- **clash n=0 vivo** = correcto para el input (ROL neutrales → sin contradicción fáctica Rol/Forense). No defecto. Watch de baja prioridad.

### 3. Bump v3.4.0 — COMPLETO, COMMITEADO, PUSHEADO, VERIFICADO
Cuatro cambios de contenido + alineación atómica de versión, en un solo commit de 29 archivos (27 M + 2 D).

- **DSv34-SHAPE — RESUELTA.** `prompt_engine.py` `SYNTHESIS_TEMPLATE`: se fijó el shape completo del objeto finding (6 campos) en las 4 arrays + instrucción de no abreviar moderate/latent ni mezclar con `multi_agent_confirmed`. Schema `Finding` (estricto, 5 requeridos) NO se tocó — el prompt sub-especificaba, no el validador. Eliminó el error Pydantic. (Trade: ahora el fallo viво es por longitud/JSON, ver DSv34-SYNTH.)
- **DSv34-PROV — RESUELTA + ejecución-verificada.** `tribunal_transversal.py`: `_init_transparency` gana key `sub_agents`; `run()` recolecta `sub_agents_used` del layer Forense (defensivo `.get()`/`isinstance`); el reporte vivo renderiza bloque `SUB-AGENTES FORENSES (N2)` (permanent+temporary). Verificado vía stub full-run offline (`d_budget_in_report` PASS).
- **DSv34-DEAD — RESUELTA.** Borrados `orchestrator/tribunal.py` + `orchestrator/verdict_synthesizer.py` (cero importadores confirmado por grep). Narrativa "v2.x preserved/coexisten" sincronizada en `CLAUDE.md` (árbol) y `prompts/system_prompt.md` (L36 pipeline + L38 composition map). Confirmado en remoto: ambos dan 404.
- **DSv34-SYNTH — ACEPTADA** (característica, no defecto; documentada en CHANGELOG + entry #30).
- **Version bump atómico 3.3.0 → 3.4.0** (§4.14.1): base + router (3.4.0-ROUTER) + 19 variants (header `# Version: 3.4.0-DOMAIN` + `# Base: ...v3.4.0` + `(composed agent v3.4.0)` + footer `ACTIVE — v3.4.0-DOMAIN` + `BASE_PROTOCOL v3.4.0`) + main.py (3 product-face) + tribunal_transversal.py (header Transparency Report) + README + CLAUDE.md + CHANGELOG `[3.4.0]`. Docstrings de módulo dejados en su versión de introducción (content-based versioning, convención CHANGELOG). Ejemplos de regla §4.14/§4.14.1 refrescados a `v3.4.x`.
- **Verificación post-push por CONTENIDO** (no solo SHA) vía GitHub MCP: base + router en 3.4.0 confirmados; los 2 muertos dan 404; SHA rotados.

### 4. Self-audit ligero (Fase 3) — 4/4 frentes verdes
- F1 refs colgantes a módulos muertos: cero (README/DEPLOY usan el concepto, no el módulo).
- F2 render PROV: ejecución-verificado (smoke offline 11 PASS / 1 SKIP / 0 FAIL, `d_budget_in_report` PASS con stub-run).
- F3 coherencia de version-stamps: confirmada por greps.
- F4 curva-U base: MISSION primer tercio / VERDICT (BLOCK 6) último tercio, intacta.

### 5. Doc cleanup (Fase 5) — COMPLETO
- `.claude-init.md` Nota#7 + header: reflejan repo v3.4.0 / v3.4.0 NOT YET CERTIFIED / cert cubre v3.3.0.
- `JARP_TOOLKIT.md` entry #30 + Nota#16 + header: idem; narrativa muerta eliminada; roadmap v3.3 (markitdown/fact-checker/etc.) dejado intacto (pendiente, no incorporado).
- Continuity v16 generada (este archivo); v15 borrado.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN — CRÍTICO ⚠️⚠️

**El repo está en v3.4.0 pero la cert vigente `PA-20260529-001` certifica v3.3.0.** Por tanto **v3.4.0 NO ESTÁ CERTIFICADO**. Esto es correcto y esperado — la re-cert es la próxima acción de gobernanza (Fase 4). NO afirmar que v3.4.0 está certificado en ningún artefacto.

---

## OPERACIÓN DE CIERRE v3.4 — ESTADO

1. ✅ Regresión E2E viva (b) — cerrada (vía fallback determinista, aceptado).
2. ✅ Bump atómico v3.3.0 → v3.4.0 — commiteado + pusheado + verificado por contenido.
3. ✅ Borrado DSv34-DEAD — `tribunal.py` + `verdict_synthesizer.py` eliminados (404 en remoto).
4. ✅ Cableado DSv34-PROV — bloque sub-agents restaurado al reporte vivo.
5. ✅ Self-audit ligero §4.14 + A-series + curva-U.
6. ⏳ **Re-cert 7-axis Level 1 JARP DEEP full-coverage** (supersedes PA-20260529-001) — **PENDIENTE, cabeza de sesión 18.**
7. ✅ Doc cleanup (CHANGELOG, jarp-toolkit #30, .claude-init, README/CLAUDE, continuity v16).

---

## DEUDA TÉCNICA — POST-SESIÓN 17

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.4.0** | 🔴 GOBERNANZA | v3.4.0 NOT YET CERTIFIED. Re-cert 7-axis Level 1 JARP DEEP pendiente. | Cabeza de s18. Supersedes PA-20260529-001. **Confirmar si la re-cert consume API** (saldo ≈$1.66, podría no alcanzar full-coverage). |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Síntesis-LLM viva parsea limpio solo en docs de baja densidad de findings; fallback determinista (diseñado) maneja docs ricos. | NO es defecto. Documentada. Hardening futuro solo si surge requisito de "pureza de síntesis". |
| **DSv34-SHAPE-followup** | 🟢 ACEPTADA (watch) | El fix de shape movió el fallo vivo de Pydantic-shape a JSON-truncation (unterminated string). Para docs ricos sigue cayendo al fallback. | Si en el futuro se quiere parse limpio: subir max_tokens de la llamada de síntesis (tiene techo) o parseo más tolerante. Bajo valor (fallback ya es correcto). |
| **clash n=0 vivo** | 🟢 WATCH | Cero clash records en corridas vivas — correcto para inputs sin contradicción Rol/Forense. | Para validar n>0 vivo haría falta un input diseñado para provocar contradicción fáctica. Baja prioridad. |

**CERRADAS s17:** gate (b) vivo, DSv34-SHAPE, DSv34-PROV, DSv34-DEAD, bump v3.4.0, doc cleanup.
**CERRADAS s16:** ítem g, gate-shrink (a + d-budget). **CERRADAS s15:** e3-e6. **CERRADAS s14:** `.claude-init Nota#7`, `TK-COSMETIC`. **CERRADAS s13:** R1-R5, DSv34-BUDGET, DSv34-FUGA#4.

---

## ESTADO ACTUAL VERIFICADO (31/05/2026 fin de sesión 17)

### Repo dark-strategist-agent
- **Versión declarada:** **v3.4.0** (commiteada + pusheada + verificada por contenido en remoto).
- **Cert vigente:** `PA-20260529-001` ACTIVE certifica **v3.3.0**. **v3.4.0 NO certificado** (correcto — re-cert pendiente).
- **5 config keys v3.4 presentes.** Default model `claude-opus-4-7`. `max_tokens` default 8192 (output). Context window 200k.
- **Código muerto:** ELIMINADO (`tribunal.py` + `verdict_synthesizer.py` ya no existen; 404 en remoto).
- **Helper local (NO commitear):** `orchestrator/smoke_test_e2e.py` v3. Confirmado NO staged en el commit v3.4.0. Si aparece en GitHub Desktop, descartar.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios s17. **Es el auditor de la re-cert de s18.**

### Repo devil-advocate-agent
- Repo git, privado, contenido íntegro. Sin cambios s17.

### Repo jarp-toolkit
- Actualizado s17: `.claude-init.md` Nota#7 + header; `JARP_TOOLKIT.md` entry #30 + Nota#16 + header → todos reflejan v3.4.0 NOT YET CERTIFIED. PRIVADO (clone anónimo falla; usar mi-filesystem o GitHub MCP).

### Artefactos de prueba (locales, fuera de repos)
- `C:\Users\jrodr\Downloads\smoke_contract.txt` — **regenerado en s17** (contrato sintético SIN PII, ~10 red flags deliberados). Reemplazó al original que se había perdido. Es helper, NO va al repo.
- `smoke_test_e2e.py` v3 — en `orchestrator/` local (helper, no commitear).

---

## PROTOCOLO DE INICIO PARA SESIÓN 18

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo (v16).
2. Cargar este prompt (v16).
3. **PHASE 0 — Verificación rápida:**
   - Confirmar v15 ya NO existe en el repo (borrado s17); v16 es el único continuity.
   - Confirmar repo en v3.4.0 (header `system_prompt.md` + router + footer). Cert registry: DS **v3.3.0** (PA-20260529-001) ACTIVE = certifica v3.3.0, **v3.4.0 NO certificado**. PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
4. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 14 SESIONES (4-17).** Prioridad #1 en userPreferences. Señalado sin acoso. Si JARP vuelve a no elegir A: asumir prioridad real ≠ escrita; NO re-confrontar.
   - **(C) Re-cert v3.4.0** — Fase 4 pendiente. 7-axis Level 1 JARP DEEP full-coverage con el prompt-architect-agent v1.3.0, supersedes PA-20260529-001. **ANTES de arrancar: confirmar si la re-cert consume API y si el saldo (~$1.66) alcanza.** Si no alcanza → fondear primero o hacer la parte no-API.
   - **(B) Integraciones del roadmap v3.3/v3.4** (markitdown, fact-checker, stop-slop, etc.) — NO empezar sin cerrar la re-cert. Pertenecen a un bump futuro.
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; docstrings de módulo = content-based) | ventanas por config (cortes duros `[:N]`, nunca hardcoded ni eliminar) | distinguir clash de severity-escalation.

**De s13-s16:** Sintetizador VIVO = `TribunalTransversal._synthesize` | NO bumpear ni certificar sobre código no ejecutado | verificar premisa de la deuda contra el archivo ANTES de arreglarla | el stub cubre LÓGICA, no comportamiento vivo | secretos fuera del chat (`set`/`$env:`, no `setx`) | verificar CONTENIDO contra el archivo antes de concluir (EOL/whitespace ≠ pérdida) | (a) cerrable por construcción con bound proof | borrar código muerto NO es aislado si la doc viva lo declara intencional (va en el bump) | no falsear registro histórico al limpiar versiones.

**De s17 (nuevas):**
- **El fallback determinista es el sintetizador de producción sancionado para docs ricos.** La síntesis-LLM viva es best-effort (parsea limpio solo en docs de baja densidad de findings). Es degradación elegante por diseño, no defecto. NO debilitar el schema `Finding` para forzar parse — el schema estricto es correcto; el prompt es lo que se ajusta.
- **El gate `b_unified_output` certifica robustez end-to-end (cualquier vía), NO parse limpio de Opus.** Certificar (b) honestamente como "cleared vía fallback", nunca como "Opus parsea limpio".
- **Editor folder-replace NO es confiable para barridos multi-archivo.** En s17 el "reemplazar en archivos" del editor solo tocó el archivo abierto; los 19 variants quedaron sin tocar. Para barridos de stamps usar **script PowerShell determinista** (`[System.IO.File]::ReadAllText/WriteAllText` con `UTF8Encoding($false)` para no corromper em-dash) — JARP lo corre, revisa `git diff`, commitea por GitHub Desktop (filtro humano preservado).
- **Grep de verificación: cuidado con falsos positivos legítimos.** Filas históricas de roadmap (`| v3.3.0 | ...`), cert histórica (`certifies v3.3.0`), y prosa factual (`tracked at v3.3.x is updated to v3.4.x`) DEBEN matchear `3.3.x` y son correctas. No "corregirlas". Distinguir stamp-stale de historia-correcta antes de actuar.
- **Pago Anthropic: "Contact sales" ≠ fondear.** El fondeo self-serve va por Console → Plans & Billing → Add funds. El form de sales rechaza dominios personales y es irrelevante para fondear pay-as-you-go.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` para forzar parse de síntesis (rechazado s17).

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md` (verificar contra archivo antes de codear).
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v16.md` (v15 borrado s17)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — clone anónimo falla; usar GitHub MCP o mi-filesystem).
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = read/verify estándar.
- **Sandbox bash:** NO ve el disco local (rutas Windows). Sirve para clonar repos PÚBLICOS (DS, PA) y grep/sed. devil-advocate y jarp-toolkit son PRIVADOS (clon anónimo falla). Para verificar el LOCAL post-edición, usar mi-filesystem o pedir a JARP un grep PowerShell (`Select-String`).
- **Método de edición = Ruta 3 (F&R explícito)** para archivos committed. `github:create_or_update_file` prohibido (límite ~10KB + autorización per-session). Para barridos multi-archivo: script PowerShell determinista (JARP corre + commitea). Para archivos LOCALES no-commiteados (helpers, continuity), `mi-filesystem:write_file` (overwrite completo) es válido.
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep/get_file_contents del marcador esperado), no solo SHA/mensaje.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline (sin key) = 11 PASS / 1 SKIP (b) / 0 FAIL. Online (con `$env:ANTHROPIC_API_KEY`) = +b. NO commitear el helper. NO mover `smoke_contract.txt` (helper) al repo.
- **API:** saldo ≈$1.66. Recarga automática OFF. Una corrida viva ≈$1.67 (NO alcanza otra sin re-fondear). `$env:ANTHROPIC_API_KEY="sk-ant-..."` en PowerShell (sesión actual; NO `setx`, NO `set` estilo CMD). Nunca pedir la key en el chat.

### Commit sugerido para cierre sesión 17 (continuity v16 + borrado v15)
```
docs: continuity v16 (session 17 close — v3.4.0 shipped, NOT YET CERTIFIED)

Session 17 — full v3.4.0 bump executed, committed, pushed, content-verified.
API key funded ($5; ~$1.66 left). Live gate (b) cleared on claude-opus-4-7
(via deterministic fallback — accepted by design, DSv34-SYNTH).

DSv34-SHAPE: synthesis finding-object shape pinned in prompt_engine.py.
DSv34-PROV: sub-agent provenance restored to live transparency report.
DSv34-DEAD: tribunal.py + verdict_synthesizer.py removed (404 confirmed remote).
Atomic stamp bump 3.3.0 -> 3.4.0 across 27 files; 2 deletions.

STATE: repo v3.4.0, NOT YET CERTIFIED (PA-20260529-001 certifies v3.3.0).
NEXT (s18): re-cert 7-axis Level 1 JARP DEEP -> supersedes PA-20260529-001.
Trading deferred 14 sessions (4-17).

NEW FILE:
- dark-strategist-continuity-prompt_v16.md: replaces v15 for session 18.

DELETED:
- dark-strategist-continuity-prompt_v15.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 17

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.4.0** | PA-20260529-001 | **v3.3.0** | ✅ ACTIVE | 27/08/2026 o v4.0.0 |

**⚠️ v3.4.0 NO certificado** — el repo avanzó a v3.4.0 pero la cert vigente cubre v3.3.0. Re-cert pendiente (s18).
**SUPERSEDED:** PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 17 (auto-mejora del próximo Claude)

1. **El gate vivo destapó lo que el stub no podía: Opus NO produce el shape limpio para docs ricos.** Primero por shape (moderate_findings sin campos), luego por longitud (JSON truncado). El fallback determinista salva en ambos casos y es el sintetizador real de producción. Certifica honesto: "(b) cleared vía fallback", no "Opus parsea limpio". No debilitaste el schema para forzarlo — correcto.
2. **El editor folder-replace mintió dos veces.** JARP dijo "aplicado" y los 19 variants seguían en 3.3.0 — su editor solo tocó el archivo abierto. Solución: script PowerShell determinista. Lección: para barridos multi-archivo NO confíes en el "reemplazar en carpeta" del editor; verifica SIEMPRE con grep antes de concluir, y si falla, script.
3. **Grep de verificación tiene falsos positivos legítimos.** Filas de roadmap históricas, certs históricas y prosa factual ("tracked at v3.3.x is updated to v3.4.x") matchean el patrón y son CORRECTAS. Clasifica cada hit como stamp-stale (corregir) vs historia (dejar) antes de actuar. Casi escalas un falso positivo dos veces.
4. **Verifica CONTENIDO post-push, no solo SHA.** Se confirmó base+router en 3.4.0 vía get_file_contents y los 2 muertos vía 404. El sandbox bash NO ve el disco local Windows — para verificar local usa mi-filesystem o pide grep PowerShell a JARP.
5. **Costo real de una corrida viva ≈ $1.67.** Dos corridas consumieron ~$3.34 de los $5. Queda ~$1.66 — NO alcanza otra. Si s18 (re-cert) consume API, fondear primero. Confirmar SIEMPRE si una operación gasta antes de prometerla.
6. **TRADING: 14 SESIONES POSTERGADO (4-17).** Señalado sin acoso. NO re-confrontar. Si s18 vuelve a no elegir A: asumir prioridad real ≠ escrita y seguir.
7. **Artefactos de prueba NO entran al repo.** `smoke_contract.txt` (helper, regenerado s17 sin PII), `smoke_test_e2e.py` v3 (helper). Confirmado NO staged. Avisar a JARP en GitHub Desktop si aparecen.
8. **Pago Anthropic — la trampa de "Contact sales".** No es el camino de fondeo; rechaza dominios personales. El fondeo self-serve es Console → Plans & Billing → Add funds. Si el modal Stripe cuelga, es bloqueo de telemetría (`m.stripe.com`): hotspot móvil lo resuelve.
