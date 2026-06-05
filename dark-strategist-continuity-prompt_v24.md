# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 04/06/2026 (sesión 25 — DS v3.11.0 confianza determinista auditable, shipped & JARP_CERTIFIED) | **Para:** Sesión 26
**Reemplaza:** v23 del 03/06/2026 (sesión 24)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v24.md`
**⚠️ BORRAR en este cierre:** v23 (`git rm` en el commit de cierre). v24 = único continuity vigente. Subir v24 al PROYECTO claude.ai + quitar v23.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 25 (resumen ejecutivo)

Sesión de **implementación de valor agregado**. Origen: en s25 (antes de este trabajo) se hizo análisis forense de 3 copias Copilot/Perplexity → backlog priorizado P1–P5 + un caso-test dorado. Trading (A) NO se eligió (**22ª sesión postergada, 4–25**). Track elegido: **P3 — confianza determinista auditable**.

**Resultado: DS v3.11.0 shipped y CERTIFICADO** (`PA-20260604-002`). Bump **no-forense confirmatorio**.

### 1. (P3) DS v3.11.0 — confianza determinista auditable, NO-VINCULANTE
**Hallazgo de arranque (regla "leer el módulo real"):** `confidence` YA EXISTÍA en `schema.py` (`AgentVerdictOutput` + `UnifiedVerdictOutput`, `HIGH|MODERATE|LOW`) pero era **deshonesta**: en `_synthesize` = lo que adivinara el LLM; en `_deterministic_synthesis` = constante `"MODERATE"` hardcodeada. P3 NO agregó confianza — la volvió **determinista, auditable, computada en ambos caminos, y explícitamente no-vinculante**.

- **`orchestrator/schema.py`** — `+ compute_confidence(agents_consulted, driver_corroborated, driver_finding_count, unresolved_conflicts)`. Función pura, testeable. Regla: **LOW** si <2 agentes O el veredicto descansa en 1 hallazgo no-corroborado O ≥2 clashes UNRESOLVED; **HIGH** si ≥3 agentes Y 0 clashes UNRESOLVED Y (tier que dicta veredicto vacío/clean O multi-agent-confirmed); **MODERATE** resto. (Edge: tier vacío con ≥3 agentes y 0 clashes → HIGH, no LOW.)
- **`orchestrator/tribunal_transversal.py`** — import + `_apply_confidence(unified, all_outputs)` cableado en AMBOS caminos de síntesis. Computa corroboración cross-agent (`(severity, título-normalizado)` reportado por ≥2 agentes distintos), **puebla `multi_agent_confirmed` determinísticamente** (el fallback antes NO lo poblaba), fija `agents_consulted = len(all_outputs)` (ground truth), deriva `confidence`. 2 etiquetas NO-VINCULANTES añadidas (`_format_verdict` + transparency report).
- **`orchestrator/test_confidence.py`** (NUEVO, commiteado) — truth-table 10 casos offline, $0.

**GARANTÍA INVIOLABLE verificada:** `compute_confidence` solo se asigna a `.confidence`. `final_verdict` se computa SOLO por severidad (FATAL→INVIABLE), en rama separada. Test de integración: en 4 casos con `confidence` variando, `final_verdict` quedó INTACTO.

### 2. DECISIONES CLAVE (s25)
- **Confianza = metadata NO-VINCULANTE** (consistente con RULE LG07/F08). NUNCA toca `final_verdict`. Es señal de auditabilidad (cuán corroborado/disputado está el veredicto), NO probabilidad de éxito real NI garantía de eficiencia. Las etiquetas en los reportes lo dicen explícitamente — **inocula contra la falacia "consenso 95% → eficiencia 95%"** que el análisis forense detectó como FATAL.
- **`multi_agent_confirmed` se sobrescribe determinísticamente en AMBOS caminos** (incl. LLM), no solo el fallback. "Auditable" exige que lo mostrado coincida con lo computado, no con la corazonada del modelo. Decisión confrontada y aprobada por JARP.
- **`bump_stamps.ps1` EXCLUYE `orchestrator/*.py` Y CHANGELOG** (scope = prompts/*.md + README + CLAUDE anchored). → los banners product-face en orchestrator (main:126/242, wizard:149, tribunal:440), el CHANGELOG, y la prosa no-anclada (CLAUDE status, filas de tabla) requieren **script manual aparte**. NO asumir que el .ps1 cubre todo el bump.
- **Dual-versioning afinado:** docstrings de cabecera de módulo = CONTENT-BASED/congelados (schema/tribunal @v3.0.0 de origen; main/wizard @su-último-cambio). NO bumpean cada minor — solo cuando ESE módulo cambia. Precedente: `catalogs.py` congelado en 3.2.0. **Solo los banners visibles al operador en runtime** (prints, argparse `--help`, título del transparency report) trackean el minor del PRODUCTO → 3.11.0. JARP aceptó dejar main:2/wizard:2 en 3.10.0 (divergencia intra-archivo defendible).

### 3. RE-CERT DS v3.11.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 RULE 08 (`PA-20260604-001`) PASS (PA-agent sin cambios). Auditoría 7-ejes confirmatoria sobre delta v3.10.0 (19/19 byte-idénticas salvo stamp).
- **Evidencia funcional (máquina real, POST-bump):** `test_confidence.py` **10/10** + `smoke_test_e2e.py` **0 FAIL / 1 SKIP** (`b_unified_output` SKIP = DNS/key, no-bloqueante), con `c_fallback_intact` + `e_monotonic_verdict` PASS.
- **CERT EMITIDO:** `PA-20260604-002` — DS **v3.11.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **04/09/2026 o v4.0.0**. **SUPERSEDES PA-20260603-006** (v3.10.0). Sin cascade (minor).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.11.0 = CERTIFICADO (`PA-20260604-002`).** Sin version-gap. PA-20260603-006 (v3.10.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — APLICADO EN CIERRE (s25) ✅
1. P3 código: `apply_p3_confidence.py --apply` → `schema.py` + `tribunal_transversal.py` + `test_confidence.py`. Regresión verde.
2. Bump anclado: `bump_stamps.ps1 3.10.0→3.11.0 -Apply` → ~23 files / ~69 stamp lines (prompts + README + CLAUDE).
3. Bump manual: `bump_manual_v3_11_0.py --apply` → CHANGELOG [3.11.0] + 4 banners orchestrator + CLAUDE status + filas tabla README/CLAUDE.
4. Cert: `finalize_cert_v3_11_0.py --apply` → bloque JARP_CERTIFIED PA-20260604-002 en CHANGELOG.
5. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.11.0/PA-002 (vía mi-filesystem).
6. `jarp-toolkit/JARP_TOOLKIT.md` — `sync_toolkit_v3_11_0.py --apply` → header + #30 (Version/CERT/Previous) + Note #16.
7. Continuity v24 commiteado; `git rm` v23.
8. **One-shots BORRADOS** (no commiteados): `apply_p3_confidence.py`, `bump_manual_v3_11_0.py`, `finalize_cert_v3_11_0.py` (DS), `sync_toolkit_v3_11_0.py` (toolkit). Copia huérfana `C:\Users\jrodr\apply_p3_confidence.py` también borrable.

---

## DEUDA TÉCNICA — POST-SESIÓN 25

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.11.0** | ✅ CERRADA | v3.11.0 CERTIFICADO (PA-20260604-002) | 0/0/0/0. |
| **P3 confianza** | ✅ CERRADA | Confianza determinista auditable no-vinculante shipped | Ambos caminos; test_confidence.py. |
| **clash n>0 live + gate b live** | 🟢 WATCH | `b_unified_output` SKIP | **Causa real = DNS INTERMITENTE** (`getaddrinfo failed` a api.anthropic.com en la máquina de JARP), no solo "no key". Ambiental (VPN/DNS/firewall). No-bloqueante. free-claude-code (localhost:8082) podría esquivarlo para dogfood no-cert, NO para cert. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO (del análisis forense s25) — pendiente
- **P1 — gate de escalamiento por confianza (SIGUIENTE).** Si `confidence == LOW` y hay presupuesto → ronda de escalamiento (N2 + lentes-arquetipo) → re-sintetiza → recomputa. **Depende de P3 (ya hecho).** Veredicto sigue severidad.
- **P2 — lentes-arquetipo** (perspectivas estructuradas; **NO impersonar personas reales** = fabricación de autoridad, descartado).
- **P4 — señales externas vía BYO/RAG existente** (`--corpus`; no requiere infra nueva).
- **P5 — lente de riesgo reputacional** (posible skill #7).
- **Caso-test dorado INVIABLE:** la afirmación "consenso 95% → eficiencia 95% del bot" (causalidad inventada + métrica fabricada) — usar como fixture de lo que DS debe DESTRUIR. Útil para validar P1/P3 end-to-end.

---

## ESTADO ACTUAL VERIFICADO (04/06/2026 — fin s25)

### Repo dark-strategist-agent
- **v3.11.0 — CERTIFICADO (`PA-20260604-002`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.11.0 (registrar SHA tras push).
- **NEW:** `schema.compute_confidence` + `tribunal._apply_confidence` (ambos caminos) + `test_confidence.py`. Confianza determinista/auditable/no-vinculante.
- `tools/bump_stamps.ps1` (NO toca orchestrator/*.py ni CHANGELOG). `gc.auto 0` activo (guarda OneDrive).
- `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus` activo (v3.10.0).
- **6 skills**, **9 sub-agentes N2 permanentes** (sin cambio).
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only). El smoke local incluye `r2_byo_corpus`. (`smoke_contract.txt` se creó en s25 — contrato Lima de prueba; sigue local.)

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s25. Sin cambios.

### Repo jarp-toolkit
- header + #30 + Note #16 + `.claude-init.md` Note #7 → v3.11.0/PA-002. PRIVADO.

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34. (Cert = Opus real sin proxy.)

---

## PROTOCOLO DE INICIO PARA SESIÓN 26
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v24).
2. **PHASE 0 — Verificación:**
   - v23 borrado, v24 único continuity.
   - Repo en v3.11.0. **Cert registry: DS v3.11.0 `PA-20260604-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260603-006` SUPERSEDED.
   - `rank_bm25` + `pydantic` instalados (sin ellos R1/R2 corren degradados a legacy).
   - `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 22 SESIONES (4–25).** Prioridad #1 en userPreferences. **NO re-confrontar** (regla heredada): si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Backlog valor-agregado** — **P1 (gate escalamiento) es el siguiente lógico** (depende de P3, ya hecho). Luego P2/P4/P5. Caso-test dorado disponible.
   - **(C) WATCH live-key/DNS** — no-bloqueante (ambiental).
   - **(D) Gobernanza** — sin limbo.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config | distinguir clash de severity-escalation | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) IDs diarios separados | Sev×Likelihood NON-BINDING | SOX deficiency mapea nativo al tier 4-niveles | 4 variance decompositions obligatorias | orden monotónico FATAL→SERIOUS→MODERATE→LATENT al insertar filas | telephone-game resuelto v3.4 — NO reabrir | context-degradation es LENTE DE DETECCIÓN, NO driver del veredicto | RAG es MECANISMO DE ALIMENTACIÓN, NO driver del veredicto | ContextBuilder document-free → solo SELECCIONA corpus | infinity/Docker RECHAZADO (zero-infra, BM25 embebido) | fallback byte-idéntico OBLIGATORIO ante cambio de feed | leer el módulo real antes de incorporar | el wizard SINTETIZA argv → mismo parser (NO re-implementar) | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case, NO pre-cargado (`JURISDICTION_CORPUS_MAP` `{}`) | Floor R2 = OVERLAP DE TOKENS, no score BM25 | ingesta de corpus reutiliza UNIT-INGEST/markitdown | mi-filesystem preserva escapes byte-exacto | validar retrieval con corpus PEQUEÑO.

**De s25 (nuevas):**
- **Confianza = metadata NO-VINCULANTE, determinista, computada en ambos caminos de síntesis.** `compute_confidence` (regla por nº agentes + corroboración cross-agent + clashes UNRESOLVED) NUNCA toca `final_verdict`. Es señal de auditabilidad, NO probabilidad de éxito ni eficiencia. Las etiquetas en los reportes lo declaran (anti-falacia consenso=eficiencia).
- **`multi_agent_confirmed` + `agents_consulted` se derivan determinísticamente en AMBOS caminos** (no se confía en la corazonada del LLM para un campo de auditabilidad). El fallback antes ni los poblaba — ahora sí.
- **`bump_stamps.ps1` NO cubre `orchestrator/*.py` ni CHANGELOG.** Todo bump futuro necesita: (1) .ps1 para prompts+README+CLAUDE anclados; (2) script manual para CHANGELOG + banners product-face en orchestrator (main/wizard/tribunal runtime) + prosa no-anclada (CLAUDE status, filas tabla).
- **Docstrings de cabecera de módulo = content-based/congelados** (schema/tribunal @3.0.0; main/wizard @último-cambio; `catalogs.py` @3.2.0 de precedente). NO bumpean cada minor — solo cuando ESE módulo cambia. Banners runtime visibles al operador SÍ trackean el minor del producto.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | UNIT-INGEST como sub-agente del spawner | Severity×Likelihood como dimensión VINCULANTE | skills knowledge-work descartadas | re-trabajar telephone-game (resuelto v3.4) | context-degradation como driver del veredicto | latent-briefing de Agent-Skills | infinity/Docker baseline RAG | embeddings densos baseline (BM25 suficiente) | RAG de contenido en ContextBuilder | re-implementar lógica de pipeline en el wizard | pre-cargar corpus jurisdiccional por país en el repo | floor R2 por score BM25 (usar overlap) | forzar el smoke al repo sin parametrizar paths locales | **confianza como driver del veredicto (es metadata) — s25** | **impersonar personas reales en lentes-arquetipo (fabricación de autoridad) — s25** | **"consenso → eficiencia" como métrica válida (falacia; es caso-test INVIABLE) — s25** | **bumpear docstrings de módulo congelados cada minor — s25**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v24.md` (v23 borrado s25)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` ya activo en DS.**
- **MCPs:** mi-filesystem, GitHub. **Si mi-filesystem timeoutea: `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop.** (En s25 mi-filesystem se colgó una vez ~4min y se recuperó al reintentar.)
- **PowerShell de JARP NO acepta `&&`** — dar comandos por separado o con `;`.
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1` (NO toca orchestrator/*.py ni CHANGELOG). Edits de prosa/código multi-archivo = **script Python anclado all-or-nothing** (dry-run → --apply), **entregado a la RAÍZ del repo donde JARP lo corre** (no a home). Edits pequeños/archivo nuevo = mi-filesystem directo. `github:create_or_update_file` prohibido por defecto. NO puedo ejecutar Python/PowerShell en la máquina de JARP → JARP corre regresión y scripts.
- **Confianza runtime:** `confidence` (HIGH/MODERATE/LOW) ahora determinista; impresa en veredicto + transparency report, etiquetada NO-VINCULANTE.
- **Smoke-test E2E (LOCAL, gitignorado):** `orchestrator/smoke_test_e2e.py`. Offline esperado **12 PASS / 1 SKIP**. `python test_confidence.py` → **0 FAIL / 10**. **`pip install rank_bm25` + `pydantic` antes de correr el agente.**
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real + sin proxy. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 25
**Repo dark-strategist-agent (v3.11.0 cert) — commit atómico:**
```
feat: DS v3.11.0 — deterministic auditable confidence (NON-BINDING, both synthesis paths) + JARP_CERTIFIED PA-20260604-002
```
Incluye: `orchestrator/{schema,tribunal_transversal,test_confidence}.py`, 21 prompts, README, CLAUDE, CHANGELOG, `orchestrator/{main,wizard}.py`, `dark-strategist-continuity-prompt_v24.md`; `git rm dark-strategist-continuity-prompt_v23.md`. NO incluye los one-shots.
**Repo jarp-toolkit:**
```
docs: sync DS v3.11.0 / PA-20260604-002 (deterministic auditable confidence) — header + #16 + #30 + .claude-init #7
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 25

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.11.0** | **PA-20260604-002** | **v3.11.0** | ✅ ACTIVE | 04/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 25 (auto-mejora del próximo Claude)

1. **Lee el módulo real ANTES de implementar.** P3 parecía "agregar confianza" — pero `confidence` ya existía (deshonesta). El trabajo real era volverla determinista, no crearla. Tanto el informe propio como Copilot/Perplexity asumieron mal. Confirma siempre contra el código.
2. **`bump_stamps.ps1` NO cubre `orchestrator/*.py` ni CHANGELOG.** Todo bump futuro = .ps1 (prompts+README+CLAUDE) + script manual (CHANGELOG + banners runtime orchestrator + prosa no-anclada). No confíes en que el .ps1 hizo todo — barre `findstr /S "OLD.VER"` para confirmar cero drift product-face.
3. **Docstrings de módulo son content-based/congelados.** No los bumpees cada minor (catalogs.py @3.2.0 de precedente). Solo banners runtime visibles al operador trackean el producto. Distinción confirmada y aceptada por JARP.
4. **Entrega los one-shots a la RAÍZ del repo donde JARP los corre.** En s25 se escribió un script a home → `No such file or directory`. Reubicar costó un round-trip.
5. **PowerShell de JARP no acepta `&&`.** Comandos por separado o `;`.
6. **Garantía inviolable:** confianza/Sev×Lik son metadata. `compute_confidence` solo se asigna a `.confidence`; el veredicto es severidad pura. Verifícalo con test de integración (final_verdict intacto bajo confidence variable).
7. **Gate regresión-verde ANTES de bump/cert** (test_confidence 10/10 + smoke 12 PASS/1 SKIP). El bump es texto+banners → re-correr regresión post-bump para cerrar el cert con evidencia post-bump.
8. **TRADING: 22 SESIONES POSTERGADO (4–25). NO re-confrontar.** Si s26 no elige A, asumir prioridad real ≠ escrita.
9. **Backlog valor-agregado:** P1 (gate escalamiento por `confidence==LOW`) es el siguiente lógico (depende de P3). Luego P2 (lentes-arquetipo, NO personas reales) / P4 (señales vía BYO) / P5 (skill riesgo reputacional). Caso-test dorado INVIABLE: "consenso → eficiencia".
10. **WATCH b = DNS intermitente** (`getaddrinfo failed` a api.anthropic.com), no solo "no key". Ambiental. No-bloqueante. No quemar sesión debuggeándolo.
