# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 02/06/2026 (sesión 20 — DS v3.6.0 legal+finance forensic matrix shipped & JARP_CERTIFIED) | **Para:** Sesión 21
**Reemplaza:** v18 del 01/06/2026 (sesión 19)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v19.md`
**⚠️ BORRAR en este cierre:** v18 (autorizar borrado vía GitHub Desktop). v19 = único continuity vigente. Subir v19 al PROYECTO claude.ai + quitar v18.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 20 (resumen ejecutivo)

Track (B) elegido: incorporación `knowledge-work-plugins` (legal+finance) → **DS v3.6.0 shipped y CERTIFICADO**. Trading (A) NO se eligió otra vez (17ª sesión postergado).

### 1. (B) DS v3.6.0 — Legal & Finance Forensic Matrix (roadmap TOP-7 item #4)
25 incorporaciones forenses de `knowledge-work-plugins` a P03 Legal + P05 Financial. Bump atómico §4.14.1 (26 archivos stamp + 1 doc nuevo). **NO tocó el roster de 9 units** (contenido de dominio, no sub-agentes).
- **P03 Legal:** +Severity×Likelihood metadata NON-BINDING (RULE LG07) + Risk Score 1-25 en BLOCK 1; +9 filas Failure Catalog (L01: non-solicit/non-compete-carveout/NDA-carveouts/playbook-deviation/MSA-gap/surviving-obligation; L04: vendor-PII-without-DPA 🔴; L06: missing-approval 🔴/unmapped-jurisdiction).
- **P05 Financial:** +4 lentes de variance decomposition (Price/Volume, Rate/Mix, Headcount/Comp, Spend Category) como RULE F05; +RULE F06 (materiality threshold), F07 (SOX deficiency→tier nativo), F08 (Sev×Lik non-binding); +9 filas Catalog (SOX material-weakness 🔴/significant-deficiency 🟠/control-deficiency 🟡, significant-account-sin-control, GL-subledger-unreconciled, variance-undecomposed, GAAP-nonconformity, reconciling-no-aging, variance-no-threshold).
- **Doc nuevo:** `docs/legal_finance_forensic_matrix.md` (matriz 1-25 anotada + 4 decomposiciones + mapa SOX→tier + scoring Sev×Lik). Content-based (no version-stamped).
- **Descartadas (sin contacto forense):** legal-response, signature-request, brief, meeting-briefing; journal-entry×2, close-management.

### 2. DECISIÓN ARQUITECTÓNICA CLAVE — Sev×Likelihood es NON-BINDING
La matriz Severity×Likelihood (1-25) de `legal-risk-assessment` se incorporó como **metadato de priorización intra-tier, NUNCA vinculante al veredicto**. El veredicto determinista (≥1 FATAL → INVIABLE) queda intacto. El tier binding lo fija SOLO el Failure Catalog (4 niveles 🔴🟠🟡🔵). Likelihood/Risk Score ordenan findings DENTRO de su tier. RULE LG07 (legal) + F08 (financial) lo blindan. **NO introducir probabilismo en el veredicto** (opción rechazada en diseño).

### 3. RE-CERT DS v3.6.0 — COMPLETA ✅ (NO confirmatoria, como se predijo)
Auditor PA-agent v1.3.0 (PA-20260527-002). Level 1 JARP DEEP full-coverage 19/19, 7 ejes.
- **Dos findings reales hallados y cerrados pre-cert** (la superficie ampliada P03/P05 generó drift):
  - **C-v36-01** 🔵 LATENT — orden monotónico de Failure Catalog roto en 4 catálogos (L01, L04, L06 legal + financial): la inserción de filas metió FATAL/SERIOUS bajo bloques MODERATE. Fix: reorden a FATAL→SERIOUS→MODERATE (contenido idéntico, solo orden). Réplica de C-P07-01 (s19). Commit `73e3de2`.
  - **D-v36-01** 🟡 MODERATE — conteos stale: se añadieron 18 filas reales (9+9), pero `system_prompt.md` decía "+12" y CHANGELOG "+10" (financial). Fix: +12→+18, +10→+9. Réplica de D-UNIT-01 (s19). Commit `73e3de2`.
- **CERT EMITIDO:** `PA-20260602-001` — DS **v3.6.0 JARP_CERTIFIED**, full coverage 19/19, 0/0/0/0, BIAS_CHECK PASS. Válido hasta **30/08/2026 o DS v4.0.0**. **SUPERSEDES PA-20260601-004** (v3.5.0). `JARP_BENCHMARK_LIVE` → v3.6.0. Sin cascade (minor bump).

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.6.0 = CERTIFICADO (`PA-20260602-001`).** No hay version-gap. Afirmar "v3.6.0 está certificado" es correcto. PA-20260601-004 (v3.5.0) pasa a SUPERSEDED.

---

## REGISTRO POST-CERT — APLICADO Y VERIFICADO (s20)
Sitios verificados por contenido en remoto:
1. `dark-strategist-agent/CHANGELOG.md` — bloque `[Certification]` PA-20260602-001. ✅
2. `jarp-toolkit/JARP_TOOLKIT.md` — header + entry #30 (Version/CERT STATUS/Previous certs) + nota → v3.6.0/PA-001. ✅
3. `jarp-toolkit/.claude-init.md` — header + Note #7 → v3.6.0/PA-001, SUPERSEDED list con 004. ✅
4. Continuity v19 (este archivo) — commitear; borrar v18.

---

## DEUDA TÉCNICA — POST-SESIÓN 20

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.6.0** | ✅ CERRADA | v3.6.0 CERTIFICADO (PA-20260602-001) | C-v36-01 + D-v36-01 cerrados pre-cert. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción para docs ricos. | Sin cambio. |
| **clash n=0 vivo** | 🟢 WATCH | Validar n>0 requiere input diseñado para contradicción Rol/Forense. | Pendiente desde s17. |
| **gate (b) live** | 🟢 WATCH | Smoke offline 11 PASS / 1 SKIP (b necesita key real). SKIP = estado aceptado (DSv34-SYNTH). | Validar síntesis viva con Opus real. |

**CERRADAS s20:** DS v3.6.0 (25 incorporaciones legal+finance), re-cert v3.6.0, C-v36-01, D-v36-01.

---

## ESTADO ACTUAL VERIFICADO (02/06/2026 fin de sesión 20)

### Repo dark-strategist-agent
- **v3.6.0 — CERTIFICADO (`PA-20260602-001`)** full coverage 19/19. Default `claude-opus-4-7`.
- **9 sub-agentes N2 permanentes** (sin cambio): QUANT, INQUISITOR, TECH, BIO, MARKET, GEO, COMPLIANCE, PSYCH (80+), FACTCHECK.
- P03 Legal y P05 Financial ampliados (matriz forense 25). Nuevo doc `docs/legal_finance_forensic_matrix.md`.
- Helpers locales NO commitear / borrables (fuera del repo): `apply_v3_6_0.py`, `fix_C-v36-01.py`, `apply_cert_close_v36.py` en `...\GitHub\`.

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s20. Sin cambios.

### Repo jarp-toolkit
- entry #30 + nota + header + `.claude-init.md` actualizados a v3.6.0/PA-001. PRIVADO (clone anónimo falla; usar mi-filesystem/GitHub MCP).

### free-claude-code
- Proxy de inferencia para corridas DS no-cert ($0). Reglas en toolkit nota #34.

---

## PROTOCOLO DE INICIO PARA SESIÓN 21
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v19).
2. **PHASE 0 — Verificación:**
   - v18 borrado, v19 único continuity.
   - Repo en v3.6.0. **Cert registry: DS v3.6.0 `PA-20260602-001` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260601-004` SUPERSEDED.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 17 SESIONES (4-20).** Prioridad #1 en userPreferences. NO re-confrontar; si vuelve a no elegir A, asumir prioridad real ≠ escrita y seguir sin fricción.
   - **(B) Resto del roadmap** — quedan: Agent-Skills-for-Context-Engineering (context degradation + fix telephone-game AFO, Medio — TOCA NÚCLEO), infinity→RAG (Alto, Docker), Wizard CLI, RAG jurisdiccional en ContextBuilder. Al cerrar el próximo bump → re-cert que supersede PA-20260602-001.
   - **(C) Gobernanza** — backlog ya clasificado; sin limbo pendiente.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo = content-based) | ventanas por config (cortes duros `[:N]`) | distinguir clash de severity-escalation | Sintetizador VIVO = `_synthesize`, fallback determinista = sintetizador de producción para docs ricos; NO debilitar el schema `Finding` | gate `b_unified_output` certifica robustez end-to-end | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 (-NNN) y cert maestro (-NNN) son IDs diarios separados.

**De s19:** UNIT-INGEST NO es finding-emitter (preproceso markitdown en main.py) | stop-slop score-only stdlib-only | 9 sub-agentes N2 (spawner autoritativo del roster; propagar conteo a system_prompt.md + micro_agents_catalog.md) | re-cert NO confirmatoria cuando el bump amplía superficie | PowerShell: nunca nombrar funciones `Rd`/`Wr` (alias), guarda anti-vacío, correr como `-File`, **método preferido = Claude escribe vía mi-filesystem/script Python validado en sandbox**.

**De s20 (nuevas):**
- **Severity×Likelihood es NON-BINDING.** Metadato de priorización intra-tier (RULE LG07 legal / F08 financial). NUNCA altera el tier binding ni el veredicto determinista. El tier lo fija SOLO el Failure Catalog. NO introducir probabilismo en el veredicto.
- **SOX deficiency mapea NATIVAMENTE al tier 4-niveles** (RULE F07): material weakness→🔴, significant deficiency→🟠, control deficiency→🟡. Es escala de severidad nativa, sin fricción con el determinismo.
- **Las 4 variance decompositions son lentes forenses obligatorias** (RULE F05): variance material sin descomposición Price/Volume·Rate/Mix·Headcount/Comp·Spend = omisión analítica (default SERIOUS).
- **AL INSERTAR FILAS EN UN FAILURE CATALOG, MANTENER EL ORDEN MONOTÓNICO** FATAL→SERIOUS→MODERATE→LATENT dentro de cada catálogo/sub-area. Insertar al final rompe la monotonía (C-v36-01). Ubicar cada fila nueva en su bloque de tier. Barrer monotonía de TODOS los catálogos tocados ANTES de la cert.
- **AL AÑADIR FILAS, PROPAGAR EL CONTEO** a la changelog-line de `system_prompt.md` + al bloque CHANGELOG (D-v36-01). Contar las filas reales, no estimar.
- **Método consolidado (validado s20):** Claude construye script Python de aplicación, dry-run contra CLONE FRESCO (no árbol modificado), escribe el script vía mi-filesystem, JARP corre + revisa en GitHub Desktop + commitea. Guardas: idempotencia + anti-vacío + ancla + uniqueness. Helpers fuera del repo, borrables.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal (taxonomía ya rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun | `HandoffPacket` Pydantic full | compactador real de tokens (diferido) | debilitar schema `Finding` para forzar parse | "17 backends" free-claude-code (son 11) | funciones PowerShell `Rd`/`Wr` (colisión alias) | UNIT-INGEST como sub-agente del spawner | barrido-limbo: superpowers, agency-agents, prompt-master, ruflo, spacex, mempalace, claude-certified-architect (DESCARTE s19) | **Severity×Likelihood como dimensión VINCULANTE del veredicto (es non-binding, s20)** | **skills knowledge-work descartadas: legal-response, signature-request, brief, meeting-briefing, journal-entry, close-management (operativas, sin contacto forense — s20).**

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v19.md` (v18 a borrar s20)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO — GitHub MCP o mi-filesystem)
- **Push siempre vía GitHub Desktop.** Cuenta `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. Sandbox bash clona PÚBLICOS (DS, PA) → `git clone --depth 1` + grep. Privados (jarp-toolkit) clone anónimo falla → mi-filesystem/GitHub MCP.
- **Método de edición:** bumps/fixes multi-archivo = Claude escribe script Python validado en sandbox (dry-run en clone FRESCO) → mi-filesystem → JARP corre + GitHub Desktop. Ruta 3 (F&R) para edits pequeños puntuales. `github:create_or_update_file` prohibido por defecto (~10KB + autorización per-session).
- **Post-push: verificar SIEMPRE por CONTENIDO** (grep del marcador), no solo SHA.
- **Smoke-test E2E:** `orchestrator/smoke_test_e2e.py` v3. Offline = 11 PASS / 1 SKIP (b) / 0 FAIL. NO commitear helper.
- **free-claude-code:** `fcc-server` puerto 8082. SMOKE = `api_key:"freecc"` + `$env:ANTHROPIC_BASE_URL=http://localhost:8082`. CERT = `sk-ant-...` real + sin proxy.
- **API:** re-cert estática = $0. Nunca pedir la key en el chat.

### Commit sugerido para cierre sesión 20 (continuity v19 + borrado v18)
```
docs: continuity v19 (session 20 — DS v3.6.0 JARP_CERTIFIED) + cert PA-20260602-001

Session 20 — track (B): knowledge-work-plugins legal+finance -> DS v3.6.0.
25 forensic incorporations into P03/P05 (Sev×Lik non-binding, 4 variance
decompositions, SOX tier map, 18 catalog rows). Atomic §4.14.1 bump (27 files).
Re-cert (NOT confirmatory): PA-20260602-001, full 19/19, 0/0/0/0, supersedes
PA-20260601-004. Two pre-cert findings closed (C-v36-01 monotonic order,
D-v36-01 stale counts) in 73e3de2.

NEW FILE: dark-strategist-continuity-prompt_v19.md (replaces v18).
DELETED:  dark-strategist-continuity-prompt_v18.md
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 20

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.6.0** | **PA-20260602-001** | **v3.6.0** | ✅ ACTIVE | 30/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 20 (auto-mejora del próximo Claude)

1. **Re-cert NO confirmatoria, como se predijo.** Ampliar P03/P05 generó 2 findings de coherencia (orden monotónico + conteos). Lección reforzada: al insertar filas en catálogos, (a) ubicarlas en su bloque de tier para no romper monotonía, (b) contar filas reales y propagar a changelog-line + CHANGELOG. Barrer AMBOS ejes antes de la cert.
2. **Sev×Likelihood se diseñó NON-BINDING desde el inicio** — preservó el veredicto determinista. Si un futuro source trae una dimensión probabilística, incorporarla como metadato, nunca como driver del tier.
3. **Método script-Python-vía-mi-filesystem confirmado como superior a PowerShell.** Dry-run en clone fresco + guardas (idempotencia/anti-vacío/ancla/uniqueness) + JARP corre como `-File`. Cero incidentes de encoding/alias esta sesión.
4. **TRADING: 17 SESIONES POSTERGADO (4-20).** Señalado sin acoso. NO re-confrontar. Si s21 no elige A, asumir prioridad real ≠ escrita.
5. **Próximo bump candidato:** Agent-Skills-for-Context-Engineering (Medio, TOCA NÚCLEO AFO — telephone-game) o infinity→RAG (Alto, Docker). El de context-engineering toca orquestación → anticipar barrido más profundo (clash, gate b) que el de contenido P03/P05.
