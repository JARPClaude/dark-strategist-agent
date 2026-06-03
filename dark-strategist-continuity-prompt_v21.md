# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 03/06/2026 (sesión 22 — DS v3.8.0 RAG document-feed retrieval shipped & JARP_CERTIFIED) | **Para:** Sesión 23
**Reemplaza:** v20 del 02/06/2026 (sesión 21)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v21.md`
**⚠️ BORRAR en este cierre:** v20 (autorizar borrado vía GitHub Desktop). v21 = único continuity vigente. Subir v21 al PROYECTO claude.ai + quitar v20.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 22 (resumen ejecutivo)

Track (B) elegido: ítem TOP-7 restante `infinity→RAG` → **DS v3.8.0 shipped y CERTIFICADO**. Re-scopeado sobre el código vivo. Trading (A) NO se eligió (19ª sesión postergada).

### 1. (B) DS v3.8.0 — RAG retrieval en la capa document-feed (BM25)
Bump atómico §4.14.1: **34 archivos** (2 nuevos + 6 core + product-face + base + router + 19 variants + 4 docs/config). **NO tocó orquestación ni el roster de 9 units.**
- **`orchestrator/retriever.py` (NEW)** — retriever léxico **BM25** (`rank_bm25`, Python puro + numpy; **sin modelo, sin API, sin daemon, sin Docker — zero-infra**). Dos trabajos, ambos en la capa doc-feed:
  - **R1 intra-documento**: reemplaza el `document[:doc_window]` ciego en `tribunal._call_agent` + `sub_agent_spawner` por recuperación de chunks relevantes al rol. Docs largos ya no pierden todo lo posterior a la ventana.
  - **R2 corpus jurisdiccional**: inyección opcional de pasajes de corpus local, seleccionado por domain vía `JURISDICTION_CORPUS_MAP` (`catalogs.py`), cargado de `corpus/<id>.txt|.jsonl`. **Ships VACÍO** (mecanismo ahora, contenido después).
- **`corpus/` (NEW)** — dir para corpora jurisdiccionales (README + .gitkeep).
- **`RuntimeContext.corpus`** — selector resuelto por ContextBuilder.
- **Config**: bloque `rag` + `tribunal.parent_report_window` en `config.example.json` y default de `main.py`. **Config-iza el `parent_report[:1000]` hardcodeado** (cierra la inconsistencia "windows-by-config").
- **Versión**: barrido dual — base + router + 19 variants + product-face → v3.8.0. Module docstrings + skills = content-based (sin cambio). Conteo de skills sin cambio (6).
- **+`rank_bm25>=0.2.2`** en `orchestrator/requirements.txt`.

### 2. DECISIONES CLAVE
- **`infinity`/Docker RECHAZADO** — sobredimensionado para auditoría forense de un documento; importaría dependencia Docker-en-Windows a un agente zero-infra. BM25 embebido lo evita. infinity queda como swap de backend v4.x SOLO si el corpus escala a millones (no lo hará).
- **RAG re-scopeado sobre el código vivo (lección s21 re-disparada):** la premisa del roadmap "RAG jurisdiccional en ContextBuilder" era **geométricamente incorrecta** — ContextBuilder es document-free (solo metadata), así que **solo SELECCIONA el corpus**; la recuperación+inyección viven en la capa doc-feed. SIEMPRE leer el núcleo real antes de incorporar.
- **BM25 léxico** elegido sobre densos para texto legal (término-preciso). Densos/Voyage reservados a v4.x si el recall léxico falla.
- **Fallback byte-idéntico** (doc corto / corpus vacío / sin `rank_bm25`) — probado en unit (12/12) + integración runtime. No-ruptura innegociable.

### 3. RE-CERT DS v3.8.0 — COMPLETA ✅
Auditor PA-agent v1.3.0 (`PA-20260527-002`). RULE 08 self-audit L0 (`PA-20260603-001`) PASS primero. Audit del delta v3.8.0 sobre baseline v3.7.0 (19/19 dominios sin cambio).
- **Evidencia funcional:** retriever 12/12 + **test de integración runtime** (grafo de módulos importa, `ctx.corpus` resuelve, helpers RAG ejecutan sin API, fallback byte-idéntico a nivel integración, RAG recupera cláusula en doc largo).
- **1 finding LATENT aceptado:**
  - **D-v38-01** 🟢 LATENT — skew de default `doc_top_k`: `retriever.build_agent_context` firma `doc_top_k=5`, orquestador+config usan `6`. No-funcional (config es autoritativo; el 5 solo se alcanza en llamada directa sin param, donde es un default conservador razonable). Default por capas. **Aceptado; alinear a 6 en el próximo touch de retriever.**
- **CERT EMITIDO:** `PA-20260603-002` — DS **v3.8.0 JARP_CERTIFIED**, **0 CRITICAL / 0 SERIOUS / 0 MODERATE / 1 LATENT (aceptado)**, BIAS_CHECK PASS. Válido hasta **30/08/2026 o DS v4.0.0**. **SUPERSEDES PA-20260602-002** (v3.7.0). `JARP_BENCHMARK_LIVE` → v3.8.0. Sin cascade (minor bump).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.8.0 = CERTIFICADO (`PA-20260603-002`).** No hay version-gap. PA-20260602-002 (v3.7.0) pasa a SUPERSEDED.

---

## REGISTRO POST-CERT — APLICADO (s22)
1. `dark-strategist-agent/CHANGELOG.md` — sub-bloque `JARP_CERTIFIED DS v3.8.0 PA-20260603-002` dentro de [3.8.0]. ✅
2. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 → v3.8.0/PA-20260603-002. ✅
3. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.8.0/PA-002, SUPERSEDED list con 002. ✅
4. Continuity v21 (este archivo) — commitear; borrar v20.

---

## DEUDA TÉCNICA — POST-SESIÓN 22

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.8.0** | ✅ CERRADA | v3.8.0 CERTIFICADO (PA-20260603-002) | 1 LATENT (D-v38-01) aceptado. |
| **D-v38-01** | 🟢 LATENT aceptada | `doc_top_k` default 5 (firma) vs 6 (config/orquestador) | Alinear a 6 en próximo touch de retriever. No-funcional. |
| **pydantic en requirements** | 🟢 LATENT pre-existente | `orchestrator/requirements.txt` no lista `pydantic` (dep dura vía schema.py); pre-existe desde antes de v3.7.0 | Higiene: agregar `pydantic>=2` en follow-up. Fuera de scope del audit histórico. |
| **cortes `[:N]` propios** | 🟢 MAYORMENTE CERRADA | doc_window → RAG (R1); parent_report → config | `handoff_window`/`synthesis_window` son ventanas de OUTPUT de agente (no documento) → quedan como config; prioridad baja. |
| **clash n>0 live + gate b live** | 🟢 WATCH | El bump las habilita; validación = smoke local con Opus real (entorno JARP) | Pendiente desde s17. Correr `smoke_test_e2e.py` con key real. |
| **corpus R2 contenido** | 🟢 DIFERIDA | Mecanismo shipped vacío; poblar corpus jurisdiccional (p.ej. Perú: Código Civil / Ley 29733) | Tarea de curación de contenido, sesión propia. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción para docs ricos | Sin cambio. |

**CERRADAS s22:** DS v3.8.0 (retriever BM25 R1+R2), re-cert v3.8.0, doc_window blind cut (→RAG), parent_report hardcode (→config).

---

## ESTADO ACTUAL VERIFICADO (03/06/2026 fin de sesión 22)

### Repo dark-strategist-agent
- **v3.8.0 — CERTIFICADO (`PA-20260603-002`)**. Verificado por CONTENIDO en remoto (re-run apply → all SKIP). Default `claude-opus-4-7`.
- **NEW:** `orchestrator/retriever.py` (BM25), `corpus/` (vacío). `JURISDICTION_CORPUS_MAP = {}`.
- **6 skills** (sin cambio): kac, ach, deception-detection, verdict-verification, adaptive-autonomous-drive, context-degradation.
- **9 sub-agentes N2 permanentes** (sin cambio): QUANT, INQUISITOR, TECH, BIO, MARKET, GEO, COMPLIANCE, PSYCH (80+), FACTCHECK.
- RAG en doc-feed layer: tribunal `_call_agent` + spawner usan `build_agent_context` (fallback `[:N]` interno).
- Helpers locales NO commitear / borrables (fuera del repo, en `...\GitHub\`): `apply_v3_8_0.py` (+ los de s21 si quedan).

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s22. Sin cambios.

### Repo jarp-toolkit
- entry #30 + header + `.claude-init.md` Note #7 actualizados a v3.8.0/PA-002. PRIVADO (clone anónimo falla; usar mi-filesystem/GitHub MCP).

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 23
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v21).
2. **PHASE 0 — Verificación:**
   - v20 borrado, v21 único continuity.
   - Repo en v3.8.0. **Cert registry: DS v3.8.0 `PA-20260603-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260602-002` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 19 SESIONES (4-22).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Resto del roadmap** — quedan: **corpus R2 contenido** (curación jurisdiccional, p.ej. Perú; activa R2 que ya está cableado) | **Wizard CLI** (v3.9.0, UX, aislable) | **alinear doc_top_k** (trivial, junto a otro touch). RAG jurisdiccional YA cableado (solo falta contenido). Al cerrar el próximo bump → re-cert que supersede PA-20260603-002.
   - **(C) Gobernanza** — backlog clasificado; sin limbo.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados | Sev×Likelihood NON-BINDING | SOX deficiency mapea nativo al tier 4-niveles | 4 variance decompositions obligatorias | orden monotónico FATAL→SERIOUS→MODERATE→LATENT al insertar filas | telephone-game resuelto v3.4 — NO reabrir | context-degradation es LENTE DE DETECCIÓN, NO driver del veredicto.

**De s22 (nuevas):**
- **RAG es un MECANISMO DE ALIMENTACIÓN en la capa doc-feed, NO un driver del veredicto.** Recupera/inyecta contexto; la severidad la fija SOLO el Failure Catalog. NO convertir RAG en dimensión vinculante.
- **ContextBuilder es document-free → solo SELECCIONA el corpus.** La recuperación+inyección viven en la capa doc-feed (tribunal `_call_agent` + spawner). NO mover retrieval de contenido a ContextBuilder.
- **`infinity`/Docker RECHAZADO para RAG — DS permanece zero-infra.** Retriever embebido (BM25). Densos/Voyage solo v4.x si el recall léxico falla. NO reintroducir infinity/Docker como baseline.
- **Fallback byte-idéntico OBLIGATORIO** ante cualquier cambio de feed: doc corto / corpus vacío / retriever no disponible → comportamiento `[:N]` legacy idéntico.
- **Lección re-confirmada (s21+s22): el roadmap puede estar geométricamente desalineado con la arquitectura viva.** SIEMPRE leer el módulo real antes de incorporar; re-scopear sobre el código, no sobre la etiqueta del roadmap.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` | "17 backends" free-claude-code (son 11) | UNIT-INGEST como sub-agente del spawner | Severity×Likelihood como dimensión VINCULANTE | skills knowledge-work descartadas | re-trabajar el telephone-game (resuelto v3.4) | context-degradation como driver del veredicto | latent-briefing de Agent-Skills (requiere KV-cache runtime) | **`infinity`/Docker como backend RAG baseline (zero-infra; BM25 embebido) — s22** | **embeddings densos como baseline RAG (BM25 suficiente para legal) — s22** | **RAG de contenido en ContextBuilder (document-free) — s22.**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v21.md` (v20 a borrar s22)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. Sandbox bash clona PÚBLICOS (DS, PA) → `git clone --depth 1` + grep. Privados (jarp-toolkit) clone anónimo falla → mi-filesystem/GitHub MCP. **Si mi-filesystem timeoutea: `node C:\Users\jrodr\filesystem-mcp\build\index.js` + reiniciar Claude Desktop.**
- **Método de edición:** bumps multi-archivo = Claude escribe script Python validado (dry-run en clone FRESCO) → mi-filesystem → JARP corre `-X utf8` + GitHub Desktop. Edits pequeños de docs = mi-filesystem directo (read→edit→write). `github:create_or_update_file` prohibido por defecto.
- **Verificar SIEMPRE por CONTENIDO** post-push (re-run script sobre clone remoto → all SKIP), no solo SHA.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` (helper local, NO commitear). Offline esperado 11 PASS / 1 SKIP (b necesita key real). **Instalar `pip install rank_bm25` antes de correr el agente.**
- **free-claude-code:** `fcc-server` puerto 8082. CERT = `sk-ant-...` real + sin proxy. re-cert estática = $0. Nunca pedir la key en el chat.
- **Deps runtime DS:** anthropic, pydantic (NO listado — deuda), google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, **rank_bm25 (NEW)**.

### Commit sugerido para cierre sesión 22 (cert close + continuity v21 + borrado v20)
```
docs: continuity v21 (session 22 — DS v3.8.0 JARP_CERTIFIED) + cert PA-20260603-002

Session 22 — track (B): infinity->RAG re-scoped -> DS v3.8.0 (BM25 retriever at
document-feed layer, R1 intra-document + R2 jurisdictional corpus empty). Re-cert:
PA-20260603-002, 0/0/0/1-LATENT (D-v38-01 doc_top_k skew accepted), BIAS PASS,
supersedes PA-20260602-002. infinity/Docker rejected (zero-infra). RAG re-scoped
(ContextBuilder document-free -> selects corpus only).

CHANGELOG: JARP_CERTIFIED sub-block in [3.8.0].
NEW FILE: dark-strategist-continuity-prompt_v21.md (replaces v20).
DELETED:  dark-strategist-continuity-prompt_v20.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 22

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.8.0** | **PA-20260603-002** | **v3.8.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 22 (auto-mejora del próximo Claude)

1. **El roadmap volvió a estar desalineado con el código vivo (lección s21 re-disparada).** "RAG jurisdiccional en ContextBuilder" era geométricamente imposible — ContextBuilder no toca el documento. Re-scopeado a la capa doc-feed. SIEMPRE leer el núcleo real antes de diseñar.
2. **El dry-run en clone pristino atrapó 2 defectos pre-write:** (a) marcador de idempotencia falso-positivo (corpus-thread al spawner saltado porque el substring aparecía en un helper insertado antes); (b) auto-generación de requirements.txt inexacta (stdlib + nombres-import≠paquete) — además `orchestrator/requirements.txt` y `config.example.json` SÍ existían (grep inicial estaba scopeado a root). Reconciliado. **El dry-run no es opcional.**
3. **Test de integración runtime añadido a la evidencia de cert** (no solo py_compile): instalar deps + importar el grafo + ejecutar los helpers RAG sin API. Atrapa breaks de import-time que py_compile no ve.
4. **Versionado dual aplicado limpio:** product-face (main.py, tribunal transparency) + base + router + 19 variants → v3.8.0; module docstrings (catalogs 3.2.0, tribunal/schema/cb 3.0.0, spawner 2.9.0) + skills NO tocados; históricos (CHANGELOG [3.7.0], filas roadmap, `# NEW v3.7.0`) preservados. Clasificar SIEMPRE antes de un replace de versión.
5. **mi-filesystem timeouteó** a mitad de escritura de v21 (4 min, sin confirmación). Reinicio (`node ...filesystem-mcp\build\index.js` + restart Desktop) lo recuperó. Tras timeout: verificar por LECTURA si el write quedó antes de reintentar.
6. **TRADING: 19 SESIONES POSTERGADO (4-22).** Señalado sin acoso. NO re-confrontar. Si s23 no elige A, asumir prioridad real ≠ escrita.
7. **Próximo bump candidato:** corpus R2 contenido (activa lo ya cableado) o Wizard CLI v3.9.0 (UX, aislable). doc_top_k align trivial junto a cualquier touch de retriever.
