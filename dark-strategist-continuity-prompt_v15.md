# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 30/05/2026 (sesión 16 — gate encogido a (b) + ítem g cerrado) | **Para:** Sesión 17
**Reemplaza:** v14 del 30/05/2026 (sesión 15)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v15.md`
**⚠️ BORRADO en este cierre:** `dark-strategist-continuity-prompt_v14.md` eliminado del repo (autorizado por JARP s16). v15 es el ÚNICO continuity vigente. Actualizar también el archivo del PROYECTO claude.ai (subir v15, quitar v14).

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 16 (resumen ejecutivo)

Sesión sin tocar código del core. Tres frentes: intento de obtener API key (fallido, diferido), encogimiento del gate de regresión, y cierre del ítem g.

### 1. API key — INTENTADA, DIFERIDA por JARP
JARP creó cuenta en Anthropic Console. Hallazgos:
- **Sin crédito gratis $5** para esta cuenta — **Perú no elegible** (saldo USD 0.00, no aparece "Claim"). El trial gratis es geo-restringido.
- El **formulario de pago (Stripe)** del modal "Agregar fondos" **no cargó** (spinner colgado). Descartado: extensiones/cookies (falló también en incógnito). Sospecha: **bloqueo a nivel red/DNS/VPN** (Pi-hole/NextDNS/hosts/firewall) — no se resolvió en sesión.
- **JARP decidió dejar la key de lado por el momento.** El blocker (b) persiste.
- Para retomar: destrabar el form de Stripe (probar `js.stripe.com/v3/` directo, hotspot móvil, DNS 1.1.1.1) → fondear $5 (cap a ~$10) → `set ANTHROPIC_API_KEY` (NO setx). Costo real de una corrida acotada ~$1–4. Nunca pedir la key en el chat.

### 2. Gate de regresión — ENCOGIDO de 3 a 1 (sin gastar token)
Diagnóstico read-only contra el clon (lección R2). Las premisas del gate eran más flojas que el código real:
- **(a) max_tokens — CERRADO offline POR CONSTRUCCIÓN.** El prompt Forense = MASTER_TEMPLATE (1972 chars) + UN `rol_simulation[:8000]` (no ×N) + user `document[:4000]`. Todas las ventanas son cortes duros `[:N]` → prompt acotado sin importar input. Bound proof: forense_in≈4776 tok, synth_in≈8137 tok, +max_tokens 8192 ≪ 200k (margen ≈183.670 tok). Imposible reventar max_tokens con la config actual. Un bound proof cubre TODOS los inputs > observar una corrida.
- **(d) — PARTIDO. budget = CERRADO offline; provenance = deuda nueva.** Orquestador VIVO = `tribunal_transversal.py` (tiene su propio `_build_transparency_report` L382, retorna `transparency_report`). El bloque `BUDGET CONSUMED` SÍ se renderiza → cerrado vía **stub-run completo de `tt.run()`** (stub shape-aware del cliente LLM). **Provenance markers NO se renderizan en el reporte vivo** (ver DSv34-PROV).
- **(b) — ÚNICO PENDIENTE.** Parseo del JSON real de Opus → `UnifiedVerdictOutput` válido + clash records. Irreductible: necesita key. Ningún stub lo sustituye.

`smoke_test_e2e.py` actualizado a **v3** (helper local, **NO commitear**): añade `a_max_tokens_bound` + `d_budget_in_report` offline + `_FullRunStub` shape-aware; bloque ONLINE reducido a solo `b`. **Validado en sandbox Y en entorno JARP: 11 PASS / 1 SKIP (b) / 0 FAIL.** Escrito a disco vía mi-filesystem, verificado por contenido.

### 3. Ítem g — CERRADO (devil-advocate-agent → git)
`devil-advocate-agent` era copia manual (sin `.git/`). Adjuntado a git NO-destructivo:
```
git init -b main
git remote add origin https://github.com/JARPClaude/devil-advocate-agent.git
git fetch origin
git reset --mixed origin/main
git config core.autocrlf true
git checkout -- .
```
- El "drift" que reportó git (5 files, 348 ins/112 del) era **EOL/whitespace**, NO contenido. **Los 5 archivos verificados content-idénticos** (CHANGELOG, CLAUDE, README, example_01, example_02) entre la copia OneDrive y el remoto → **CERO pérdida.**
- **Patrón OneDrive+git confirmado concreto:** el `.git/` local fue destruido por OneDrive; la **nube conservó el repo completo del 18 abril** (con `.git/`). Recuperado descargando la carpeta de onedrive.com → ZIP backup en `C:\Users\jrodr\Downloads\devil-advocate-agent.zip`.
- **Repo es privado** (clon anónimo en sandbox falla — como jarp-toolkit; usar GitHub MCP).

---

## ⚠️⚠️ GATE DURO — REDUCIDO A SOLO (b) ⚠️⚠️

**(a) cerrado por construcción. (d-budget) cerrado vía stub-run. Offline GREEN (incl. R1/R3/R4/R5 + a + d-budget).** Lo único irreductible que SOLO se valida con key (corrida viva):
- **(b)** ¿la salida REAL de `claude-opus-4-7` parsea a `UnifiedVerdictOutput` válido con clash records? Comportamiento del modelo, no del código. El stub prueba el parser con input bien formado, NO que Opus produzca ese shape.

**Único blocker restante: API key.** JARP la dejó de lado s16 (Console sin crédito gratis para Perú + form de pago Stripe no cargó). Bump v3.4 bloqueado hasta cerrar (b).

**Correr la parte ONLINE cuando JARP tenga key:**
```
cd /d "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\orchestrator"
set ANTHROPIC_API_KEY=sk-ant-...   (NO setx)
python smoke_test_e2e.py "C:\Users\jrodr\Downloads\smoke_contract.txt" 5
```
Esperado: 12 PASS / 0 SKIP / 0 FAIL → gate cleared → bump v3.4 desbloqueado.

---

## OPERACIÓN DE CIERRE v3.4 (tras (b) vivo, requiere GO por fase)

1. **Regresión E2E VIVA = solo (b)** ← bloqueante (key). (a)+(d-budget) ya verdes offline (v3).
2. **Bump atómico v3.3.0 → v3.4.0** (método s12): cara-de-producto (main.py print/--help, header Transparency Report) + 19 variants + router + base + skills (si su contenido cambió) + módulos content-version: `budget_controller.py`, `sub_agent_spawner.py`, `prompt_engine.py`, `schema.py`, `tribunal_transversal.py`. `budget_controller.py` y `sub_agent_spawner.py` aún declaran `Version: 2.8.0` en docstring (subir solo si su contenido cambia).
3. **Borrado código muerto `DSv34-DEAD`:** `orchestrator/tribunal.py` + `orchestrator/verdict_synthesizer.py` + sincronizar narrativa "v2.x preserved" en `CLAUDE.md` L84/L87 y `prompts/system_prompt.md` L38.
4. **Cableado `DSv34-PROV`** (deuda nueva): devolver el bloque sub-agents/provenance al reporte vivo (`tribunal_transversal._build_transparency_report` + `_init_transparency` no tiene key `sub_agents`). Va junto a #3.
5. **Self-audit §4.14** + checks A-series + invariante curva-U (MISSION primer tercio, VERDICT último tercio).
6. **Re-cert 7-axis Level 1 JARP DEEP full-coverage** post-bump (supersedes PA-20260529-001).
7. **Doc cleanup:** CHANGELOG [3.4.0], jarp-toolkit entry #30 (sigue v3.3.0), README/CLAUDE, continuity v16.

Ninguno de #2-#7 arranca sin cerrar #1 (anti-apilamiento + no certificar lo no ejecutado).

---

## DEUDA TÉCNICA — POST-SESIÓN 16

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **REGRESIÓN-ONLINE** | 🔴 BLOQUEANTE | Reducida a **SOLO (b)**. (a)+(d-budget) verdes offline (v3). | Único blocker del bump. JARP dejó la key de lado s16 (Console sin crédito gratis Perú + form Stripe no cargó). Script listo. |
| **DSv34-DEAD** | 🟡 MODERATE | `tribunal.py` + `verdict_synthesizer.py` huérfanos + narrativa en CLAUDE.md/system_prompt.md. | BORRAR en bump de cierre v3.4 (doble re-cert). |
| **DSv34-PROV** | 🟡 MODERATE (NUEVA s16) | El reporte vivo `tribunal_transversal._build_transparency_report` NO renderiza bloque sub-agents/provenance (el `tribunal.py` muerto sí). Provenance *creation* verificado por r4 a nivel spawner. | Cablear en bump v3.4 junto a DSv34-DEAD (al borrar tribunal.py, portar su bloque al reporte vivo). |
| **DSv34-HISTORY** | 🟢 ACEPTADA | Remoto = historial de UN commit raíz. Patrón OneDrive+git re-bootstrap. | Registro permanente. NO investigar salvo pedido. |

**CERRADAS s16:** ítem **g** (devil-advocate-agent adjuntado a git, contenido verificado íntegro), gate-shrink (a + d-budget offline GREEN).
**CERRADAS s15:** e3-e6. **CERRADAS s14:** `.claude-init Nota#7`, `TK-COSMETIC`. **CERRADAS s13:** R1-R5, DSv34-BUDGET, DSv34-FUGA#4.

---

## ESTADO ACTUAL VERIFICADO (30/05/2026 fin de sesión 16)

### Repo dark-strategist-agent
- **Versión declarada:** **v3.3.0** (bump a v3.4.0 PENDIENTE — gate (b) vivo).
- **Cert vigente:** `PA-20260529-001` ACTIVE (full coverage v3.3.0). v3.4 NO certificado (correcto).
- **5 config keys v3.4 presentes.** Default model `claude-opus-4-7`. `max_tokens` default 8192 (output). Context window 200k.
- **Código muerto presente** (a borrar en bump): `orchestrator/tribunal.py`, `orchestrator/verdict_synthesizer.py`.
- **Helper local (NO commitear):** `orchestrator/smoke_test_e2e.py` v3. Si aparece en GitHub Desktop, descartar.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios s16.

### Repo devil-advocate-agent (NUEVO en contexto)
- **Ahora repo git** (era copia manual sin `.git/`). Rama `main` tracking `origin/main`, working tree limpio, contenido íntegro verificado. `core.autocrlf true`. **Privado.** Backup ZIP en Downloads.

### Repo jarp-toolkit
- Sin cambios s16. (.claude-init Nota#7 = DS v3.3.0 / PA-20260529-001; entry #30 = v3.3.0 desde s14.)

### Artefactos de prueba (locales, fuera de repos)
- `C:\Users\jrodr\Downloads\smoke_contract.txt` — contrato (PII, NUNCA al repo).
- `smoke_test_e2e.py` v3 — en `orchestrator/` local (helper, no commitear).

---

## PROTOCOLO DE INICIO PARA SESIÓN 17

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo (v15).
2. Cargar este prompt (v15) + `docs/v34_backlog.md`.
3. **PHASE 0 — Verificación rápida:**
   - Confirmar v14 ya NO existe en el repo (borrado s16); v15 es el único continuity.
   - 5 config keys v3.4 presentes. Cert registry: DS v3.3.0 (PA-20260529-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
4. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 13 SESIONES (4-16).** Prioridad #1 en userPreferences. Señalado sin acoso. Si JARP vuelve a no elegir A: asumir prioridad real ≠ escrita; NO re-confrontar.
   - **(C) Regresión E2E VIVA (b) + cierre v3.4** — bloqueante = API key. Si JARP ya tiene key: correr online smoke-test → si 12/0/0, proceder al bump por fases. Si no: no se avanza el bump.
   - **(B) Otra rebanada v3.4** — NO empezar sin cerrar la 1. DSv34-DEAD + DSv34-PROV pertenecen al bump.
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual.

**De s13:** Sintetizador VIVO = `TribunalTransversal._synthesize()` → `build_synthesis_prompt`; `verdict_synthesizer.py`+`tribunal.py` MUERTOS (borrar en cierre) | ventanas por config, nunca hardcoded ni eliminar (hacer configurable) | distinguir clash de severity-escalation | poisoning = marcar frontera (claim UNVERIFIED, doc PRIMARY) | verificar premisas del backlog contra el archivo ANTES de codificar | NO bumpear ni certificar sobre código no ejecutado.

**De s14:** No falsear registro histórico al "limpiar" versiones | borrar código muerto NO es aislado si la doc viva lo declara intencional (va en el bump) | diagnóstico read-only antes de cerrar deuda.

**De s15:** Verificar la premisa de la deuda contra el archivo ANTES de arreglarla (R2) | validar harness/script contra módulos reales ANTES de entregar | el stub cubre LÓGICA, no comportamiento vivo (max_tokens real, parseo JSON real) | secretos fuera del chat (`set`, no `setx`).

**De s16 (nuevas):**
- **Verificar CONTENIDO contra el archivo antes de concluir.** EOL/whitespace ≠ pérdida de datos. El conteo de líneas de `git diff` NO distingue contenido de fin-de-línea. (Error s16: escalé alarma de "pérdida de contenido" desde el stat de git sin leer el archivo; los 5 files eran content-idénticos.)
- **(a) es cerrable POR CONSTRUCCIÓN** cuando las ventanas son cortes duros `[:N]`: un bound proof (ensamblar prompt real worst-case y asertar ≪ límites) cubre TODOS los inputs > observar una corrida viva.
- **Stub shape-aware** permite full-run offline de `tt.run()` para validar render del reporte (budget/provenance) sin key. De-riskea (d-render), no cierra (b).
- **OneDrive+git:** el `.git/` local puede ser destruido; la NUBE puede conservarlo. Recuperación = descargar carpeta de onedrive.com (pausar sync antes de operar git en la carpeta; verificar `.git` íntegro; reanudar después).

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido).

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.4 (CANÓNICO):** `dark-strategist-agent/docs/v34_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v15.md` (v14 borrado s16)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — clone anónimo falla; usar GitHub MCP).
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = read/verify estándar.
- **Sandbox bash:** clonar repos PÚBLICOS (DS, PA) para grep/sed/patch es más barato que API reads. devil-advocate-agent y jarp-toolkit son PRIVADOS (clon anónimo falla).
- **Método de edición = Ruta 3 (F&R explícito).** `github:create_or_update_file` prohibido (límite ~10KB + autorización per-session). Para archivos LOCALES no-commiteados (helpers, continuity), `mi-filesystem:write_file` (overwrite completo) es válido.
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep del marcador esperado), no solo SHA/mensaje.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline = 11 checks (incl. a + d-budget). Online = +b (1 check, key). NO commitear el helper. NO mover `smoke_contract.txt` (PII) al repo.

### Commit sugerido para cierre sesión 16 (continuity v15 + borrado v14)
```
docs: continuity v15 (session 16 close — gate shrunk to (b) + item g closed)

Session 16 — shrank the v3.4 regression gate from 3 unknowns (a/b/d) to 1.
(a) max_tokens: closed offline BY CONSTRUCTION (bound proof, ~183k tok margin).
(d) budget markers: closed offline via full stub run of tt.run().
(b) live UnifiedVerdictOutput from Opus: STILL the only blocker, needs API key
    (deferred by JARP — Console no free $5 for Peru + Stripe form failed to load).
smoke_test_e2e.py -> v3 (local helper, NOT committed): 11 PASS / 1 SKIP / 0 FAIL,
    validated in sandbox AND JARP env.

NEW DEBT DSv34-PROV: live transparency report dropped the sub-agents/provenance
block that dead tribunal.py had; wire it in the v3.4 bump (r4 still verifies
provenance creation at spawner level).

ITEM g CLOSED: devil-advocate-agent was a manual copy (no .git — OneDrive had
destroyed it; cloud retained the April-18 repo). Re-attached via git init +
remote + reset --mixed; core.autocrlf true. Reported drift (348/112) was
EOL/whitespace only — all 5 files verified content-identical, zero loss.

NEW FILE:
- dark-strategist-continuity-prompt_v15.md: replaces v14 for session 17.

DELETED:
- dark-strategist-continuity-prompt_v14.md

STATE:
- DS still v3.3.0, still PA-20260529-001 ACTIVE.
- Gate reduced to only (b); bump v3.4 still blocked on API key.
- Trading deferred 13 sessions (4-16).
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 16

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.3.0 | PA-20260529-001 | ✅ ACTIVE (full coverage) | 27/08/2026 o v4.0.0 |

**v3.4 NO certificado** (código completo pero no bumpeado ni probado vivo — gate (b)).
**SUPERSEDED:** PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 16 (auto-mejora del próximo Claude)

1. **Verifica CONTENIDO antes de concluir — no leas el conteo de líneas de git como pérdida de datos.** El `git diff --stat` mostró 348/112 cambios en 5 archivos; escalé eso a "se destruyó tu contenido bueno" y monté una recuperación de OneDrive. Al leer los archivos reales, los 5 eran **content-idénticos**: era EOL/whitespace. Lección: el stat de git no distingue contenido de fin-de-línea; lee el archivo antes de afirmar pérdida o drift. (Mismo error de raíz que la suposición de EOL minutos antes.)
2. **(a) se cierra por construcción, no fabricando un check de riesgo inexistente.** El backlog decía "MASTER_TEMPLATE + handoff 8000 × N revienta max_tokens"; el código muestra UN handoff `[:8000]` por call, cortes duros, margen ≈183k tok. El cierre honesto fue un bound proof determinista, no simular un riesgo que no existe (R2 otra vez).
3. **El stub shape-aware permite full-run offline.** Un cliente LLM stub que devuelve JSON parseable por tipo de call (síntesis vs agente vs sub-agente vs SSM) deja correr `tt.run()` entero sin key → valida el render del reporte (budget). NO valida (b) (shape real de Opus).
4. **OneDrive+git: la nube es la red de seguridad.** El `.git/` local de devil-advocate-agent estaba destruido; la nube conservó el repo del 18 abril. Pausar OneDrive antes de operar git en la carpeta; verificar `.git` íntegro; reanudar después. Recuperación de contenido = onedrive.com historial/descarga.
5. **API key: bloqueo geográfico + de red.** Perú no elegible para el crédito gratis $5; el form de Stripe del Console no cargó (sospecha DNS/firewall/VPN local). JARP lo dejó de lado. Para retomar: `js.stripe.com/v3/` directo, hotspot móvil, DNS 1.1.1.1.
6. **TRADING: 13 SESIONES POSTERGADO (4-16).** Señalado sin acoso. NO re-confrontar. Si s17 vuelve a no elegir A: asumir prioridad real ≠ escrita y seguir.
7. **Artefactos de prueba NO entran al repo.** `smoke_contract.txt` (PII), `smoke_test_e2e.py` v3 (helper). Avisar a JARP en GitHub Desktop si aparecen.
