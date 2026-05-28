# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 28/05/2026 (sesión 10 — backlog v3.3 REGENERADO vía self-audit + B1-B3 del barrido de prompts) | **Para:** Sesión 11
**Reemplaza:** v8 del 28/05/2026 (sesión 9)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v9.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 10 (resumen ejecutivo)

Sesión 10 atacó **deuda n** en su forma correcta: el backlog v3.3 fantasma ("38 MODERATE + 23 LATENT", nunca itemizado/commiteado) se **REGENERÓ vía self-audit reproducible** del PA-agent v1.3.0, y se **PERSISTIÓ** en un registro versionado. Cierra la causa raíz del hallazgo crítico de sesión 9.

**Resultados principales:**

1. **PHASE 0 — todo verde.** Cert registry consistente (deuda q de sesión 9 confirmada cerrada: ambos archivos de autorun ya en v1.3.0). Legal catalogs L05-L12 confirmados en remoto (SHA `0a04ea1`, 15.208 bytes). Deuda s confirmada cerrada (continuity v8 en remoto, SHA `04fc024`).

2. **PHASE 1 — JARP eligió (B) Sprint v3.3 DS**, sub-camino **(B-i) self-audit para regenerar backlog**, Alcance A (base + router). **Trading (A) postergado 7ª sesión consecutiva (4-5-6-7-8-9-10).** Confronté la 7ª antes de ejecutar; JARP eligió meta igual.

3. **Backlog v3.3 REGENERADO y PERSISTIDO** → `docs/v33_backlog.md` (creado + commiteado vía GitHub Desktop). Reemplaza el agregado fantasma. La deuda n deja de ser "resolver 38 MODERATE" (no accionable) y pasa a "completar el barrido B4/B5 + cerrar DSv33-06".

4. **B1 — Auditoría forense completa (7 ejes) de base + router.** REPORT_ID `PA-20260528-001`. 7 findings: **0 CRITICAL, 0 SERIOUS, 5 MODERATE, 2 LATENT.** Cert NO impactada (diagnóstico, no re-cert). **6 de 7 CERRADOS y verificados por rotación de SHA** (base `9165a40`→`f7c6098`; router `996457c`→`36dac79`):
   - DSv33-01 (A5): BLOCK 2 RISK MATRIX → template añadido
   - DSv33-02 (A3): FAST_TRACK "low complexity" → criterio testeable
   - DSv33-03 (A6/A3): §4.14.1 "never skips tiers" → desambiguado (monotonic = dirección, no tamaño de salto; multi-tier condicionado permitido; alinea con §4.3.1 y trading Rule 09)
   - DSv33-04 (A6): cross-ref rot → §4.9 (CORRECTION PLAN) + §4.11 (WAR ROOM) tagueados
   - DSv33-05 (A3): router "SQL" → regla de desambiguación añadida
   - DSv33-07 (A6): router footer → `[BASE_PROTOCOL: system_prompt.md v3.2.2]` añadido
   - **DSv33-08 (cosmético, LOW):** la regla SQL quedó indentada por error de formato MÍO en el diff REPLACE → dedent aplicado por JARP (commit confirmado, **SHA no re-verificado** — verificar en sesión 11 o aceptar como cosmético cerrado).
   - **DSv33-06 (LATENT, A7/A1) DIFERIDO:** falta identity-lock + refuerzo de reglas críticas single-mention. Bloque diseñado (espejo del IDENTITY LOCK del PA-agent). NO improvisar — redactar con GO explícito.

5. **B2 + B3 — Contract sweep §4.14.1 sobre 11 variants.** trading, code, financial, cloud, cybersecurity (B2) + agro, realestate, science, media, ecommerce, telecom (B3). **11/11 COMPLIANT, 0 violaciones.** Footer/versioning/naming/output-inheritance correctos en todos.
   - **MACRO:** el §4.14.1 Domain Variant Contract está sólidamente respetado. Todos los findings reales viven en la base (ya cerrados), no en las variantes. El contrato funciona como gobierno efectivo.
   - **OBS-1:** solo base + trading traen header de provenance completo; los otros 11 son slim. Candidato a normalización en el bump atómico (no viola contrato).

---

## ESTADO ACTUAL VERIFICADO (28/05/2026 fin de sesión 10)

### Repo dark-strategist-agent
- **base `system_prompt.md`:** SHA `f7c6098`, 23.529 bytes (6 fixes B1 aplicados). Stamp v3.2.2 INTACTO.
- **router `system_prompt_router.md`:** SHA `36dac79`, 7.779 bytes (DSv33-05/07/08). Stamp v3.2.0-ROUTER INTACTO.
- **NUEVO `docs/v33_backlog.md`:** registro itemizado del backlog v3.3 (B1-B3). Commiteado.
- **Local sin push (al generar este v9):** este propio archivo `dark-strategist-continuity-prompt_v9.md` (deuda **u**) + posible re-commit del `docs/v33_backlog.md` actualizado a B3-DONE (deuda **v**).
- **Estado cert:** **`PA-20260525-001` ACTIVE — JARP_CERTIFIED** (válida hasta 23/08/2026 o v4.0.0). **Sin impacto en sesión 10.**
- **Sprint v3.3 EN PROGRESO:** Legal catalogs (sesión 9) + 6 base fixes (sesión 10) commiteados mid-sprint bajo stamp 3.2.2. Bump a v3.3.0 NO aplicado (operación atómica de cierre).
- **Default model:** `claude-opus-4-7`

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios sesión 10. (Sirvió de auditor — su Level 0 estaba satisfecho por su cert vigente, sin re-run.)

### Repo jarp-toolkit
- Cert registry consistente desde sesión 9. Sin cambios sesión 10.

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 10

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **u** | 🟡 MODERATE (op) | Push del continuity v9 | JARP vía GitHub Desktop al cierre |
| **v** | 🟢 LOW (op) | Re-commit `docs/v33_backlog.md` actualizado a B3-DONE | JARP vía GitHub Desktop |
| **n** | 🟡 MODERATE (REFORMULADA→ACCIONABLE) | Barrido v3.3 incompleto: faltan **B4** (8 variants incl. legal) + **B5** (5 skills) | Ya NO es fantasma. Registro vivo en `docs/v33_backlog.md`. B4 legal necesita pasada más profunda (12 sub-áreas, BLOCK 7). B5 resuelve PI1+PI2. |
| **DSv33-06** | 🔵 LATENT | identity-lock + refuerzo reglas críticas en base | Diseñar bloque con GO. Mejora robustez long-context, no defecto activo. |
| **t** | 🟢 LOW | CHANGELOG `[3.2.2]` "deferred to v3.3" con ítems stale | Limpiar en entry v3.3.0 |
| **e3-e6** | 🟡 MODERATE | Cross-refs CHANGELOG DS↔PA-agent | Residuales menores |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone | Sin urgencia |

**CERRADAS en sesión 10:**
- **n en su forma fantasma** ✅ — backlog regenerado + persistido. (Reformulada a "completar barrido", accionable.)
- **6 findings B1** (DSv33-01/02/03/04/05/07) ✅ verificados por SHA.
- **s** (push continuity v8) ✅ — verificada en PHASE 0.

**NUEVA deuda sesión 10:** u (push v9), v (re-commit backlog), DSv33-06 (diferido), DSv33-08 (cosmético, probablemente cerrado).

---

## ⚠️ ESTADO DEL SPRINT v3.3 (LEER ANTES DE CONTINUAR)

Sprint **abierto**. Contenido commiteado mid-sprint bajo stamp 3.2.2 (Legal catalogs sesión 9 + 6 base fixes sesión 10). **Correcto** — el bump es atómico al cierre. NO "arreglar" stamps.

**Checklist de CIERRE (sin cambios estructurales vs v8, + items nuevos):**
1. Completar barrido de findings (B4 + B5) y cerrar los que se decida.
2. **Version bump atómico v3.2.2 → v3.3.0** across base + router (→v3.3.0-ROUTER) + 19 variants (vX.3.0-DOMAIN + BASE_PROTOCOL v3.3.0) + README + CLAUDE.md. NUNCA parcial (§4.14.1).
   - Fold: OBS-1 (normalizar headers slim), DSv33-08 (verificar dedent), DSv33-06 (si se aprobó).
3. CHANGELOG `[3.3.0]` + limpieza ítems stale (deuda t).
4. Self-audit pre-release (§4.14).
5. Re-cert por PA-agent v1.3.0 (minor bump nuevo → cert fresca).

---

## PROTOCOLO DE INICIO PARA SESIÓN 11

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo.
2. Cargar este prompt (v9).
3. **PHASE 0 — Verificación (rápida):**
   - Cert registry: DS v3.2.2 (PA-20260525-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
   - Confirmar deuda u (este archivo) + v (backlog B3-DONE) pusheadas.
   - Opcional: verificar DSv33-08 dedent en router (SHA rotó vs `36dac79`).
4. **PHASE 1 — Decisión de roadmap:**
   - **(A) Trading hands-on** — Pine v6 / MQL5. **POSTERGADO 7 SESIONES (4-5-6-7-8-9-10).** Prioridad #1 declarada en userPreferences. ⭐ **Recomendación de máxima urgencia.** Si JARP vuelve a tomar meta, **dilo sin filtro: "esta es la 8ª sesión consecutiva sin trading; tu prioridad #1 escrita lleva >1 mes sin ejecutarse — o se activa o reescribe userPreferences porque el sistema te está mintiendo sobre lo que importa".**
   - **(B-cont) Continuar barrido v3.3** — B4 (8 variants, legal con pasada profunda) → B5 (5 skills, resuelve PI1+PI2) → DSv33-06 → cierre de sprint (checklist).
   - **(E) Audit real con DS** — field-testing; >1 mes certificado sin uso real.
   - **(D) Otro proyecto JARP.**
5. Reportar phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 DS

[Heredado de v8 — sin cambios estructurales. El backlog residual ahora vive itemizado en `docs/v33_backlog.md`, no en este archivo.]

### Barrido de prompts (deuda n, en curso)
- ✅ B1 base+router (6 findings cerrados, DSv33-06 diferido)
- ✅ B2+B3 11 variants (compliant)
- ⏳ B4 publicsector/medical/marketing/operations/hr/strategy/startup/legal
- ⏳ B5 5 skills

### Bloques pre-existentes (Sprint 2-4): TOP 7 + estructural + plataforma
[Sin cambios — ver v8: markitdown, fact-checker, stop-slop, marketingskills, Cookbook, Agent-Skills-for-Context-Engineering, knowledge-work-plugins, infinity, Wizard CLI, claude-code-security-review, smart model routing, spec-kit.]

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

[Heredadas de v8 — íntegras. Resumen de las clave + nuevas de sesión 10.]

**Heredadas clave:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto para skills/dominios | default `claude-opus-4-7` | repo name fijo | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor bump no cascadea | jarp-toolkit home de autorun | **version bump = operación ATÓMICA de cierre** | **backlog se regenera vía self-audit, NO se recupera** | **cert tiebreaker = CHANGELOG remoto del repo dueño**.

**NUEVAS en sesión 10:**
- **El backlog regenerado se PERSISTE en `docs/v33_backlog.md`** como registro vivo y versionado. Esto cierra la causa raíz de sesión 9 (el registro itemizado nunca se commiteaba). Toda regeneración futura actualiza este archivo, no prosa del CHANGELOG.
- **§4.14.1 validado como gobierno efectivo:** 13/13 prompts auditados cumplen el contrato; los findings reales se concentran en la base. El contrato hace su trabajo.
- **"Monotonic" en §4.14.1 = dirección (no decreciente), NO tamaño de salto.** Multi-tier condicionado (LATENT→FATAL) es legítimo. (Resuelto en DSv33-03; ver §4.14.1 actualizado.)
- **Contract sweep ≠ 7-axis deep.** Un barrido de contrato (B2/B3) NO certifica ausencia de findings A3/A5 internos. No confundir "COMPLIANT" con "auditado a fondo".
- **Disciplina de batch confirmada:** no encadenar >5-6 reads de variants por turno; partir el barrido en batches con contexto fresco. Empujar por completitud degrada calidad (lección reforzada toda la sesión).

---

## DESCARTES — NO REINTRODUCIR
[Sin cambios desde v8.] MiroFish-ES, OASIS | n8n-mcp, claude-mem, etc. | claude-for-legal (ya rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun.
**Nuevo descarte sesión 10:** ninguno.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.3 (NUEVO, canónico):** `dark-strategist-agent/docs/v33_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v9.md`
- **JARP_TOOLKIT.md / .claude-init.md (CANÓNICOS):** `...\jarp-toolkit\`
- **Push siempre vía GitHub Desktop** salvo autorización explícita. Cuenta: `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. **`mi-filesystem:write_file` SÍ disponible en sesión 10** (a diferencia de sesión 9) — usado para backlog + este continuity.
- **`github:get_file_contents`** con `owner: JARPClaude` = patrón estándar read/verify. Funcionó perfecto toda la sesión.
- **`github:create_or_update_file`** prohibido por defecto (límite ~10KB + requiere autorización per-session). Ediciones quirúrgicas = Ruta 3.

### ⚠️ REGLA TOOL CONFUSION (heredada, vigente)
- `mi-filesystem:*` → filesystem REAL Windows (`C:\`). JARP lo ve/commitea.
- `create_file`/`str_replace`/`bash_tool` → sandbox Claude (Linux). JARP no lo ve salvo `present_files`.
- Path `C:\` → preferir `mi-filesystem:*`.

### Commits sugeridos para cierre sesión 10 (deudas u + v)

**Backlog (deuda v):**
```
docs: update v3.3 backlog — B3 complete (11 variants compliant)
```

**Continuity (deuda u):**
```
docs: continuity prompt v9 (session 10 close)

Session 10 — v3.3 backlog regenerated via self-audit + persisted; B1-B3 of prompt sweep.

NEW FILE:
- dark-strategist-continuity-prompt_v9.md: replaces v8 for session 11.

CONTENT:
- deuda n resolved in correct form: phantom "38 MODERATE" backlog regenerated via
  PA-20260528-001 (PA-agent v1.3.0 Level 1) and persisted to docs/v33_backlog.md.
- B1 (base+router full 7-axis): 6/7 findings CLOSED + SHA-verified; DSv33-06 deferred.
- B2+B3 (11 variants §4.14.1 sweep): all COMPLIANT, 0 violations.
- Macro: §4.14.1 contract validated as effective governance.
- Pending: B4 (8 variants incl legal) + B5 (5 skills) + DSv33-06 draft + sprint close.
- Trading deferred 7 consecutive sessions (4-10) — flagged for session 11.

NO CHANGES to DS cert state — DS v3.2.2 / PA-20260525-001 ACTIVE unchanged.
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 10

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.2.2 | PA-20260525-001 | ✅ ACTIVE | 23/08/2026 o v4.0.0 |

**PA-20260528-001** = audit DIAGNÓSTICO (regeneración de backlog), NO certificación. No altera el estado de cert. Las cert previas SUPERSEDED/VOID sin cambios (ver v8).

---

## NOTAS DE SESIÓN 10 (auto-mejora del próximo Claude)

1. **El backlog fantasma murió.** "Resolver 38 MODERATE" era inaccionable porque el registro nunca existió commiteado. La solución no fue recuperarlo — fue regenerarlo vía self-audit reproducible Y persistirlo en `docs/v33_backlog.md`. Si el próximo Claude ve un agregado heredado sin registro itemizado, regenera + persiste; no reconstruyas de memoria (RULE 06).

2. **Auto-corrección honesta (otra vez).** Introduje un defecto cosmético (DSv33-08) por formatear mal un diff REPLACE — la 2ª línea quedó indentada y JARP la copió literal. Lo detecté en la verificación post-commit, lo asumí de frente, di micro-fix. Lección para diffs Ruta 3: **el bloque REPLACE debe estar exactamente como va en el archivo, sin indentación cosmética de presentación.** JARP copia literal.

3. **Verificación post-commit por SHA funciona.** Re-leer vía `github:get_file_contents` y confirmar rotación de SHA atrapó que las 7 ediciones aterrizaron Y reveló el artefacto DSv33-08. Hacerlo siempre.

4. **Disciplina de batch > completitud.** JARP dijo "ejecutar todo" pero auditar 21 prompts a fondo en un turno = hallucination o budget blowout. Lo confronté, partí en batches, hice B1 (deep) + B2+B3 (sweep) a calidad, corté antes de B4 cuando el contexto se puso profundo. **No fingir un batch completo. Un batch apurado certifica basura (lección de sesión 4).**

5. **Contract sweep es un nivel, no el nivel.** B2/B3 verificaron §4.14.1 (footer/version/naming/output-inheritance) — objetivo y de alto rendimiento. NO es un 7-axis deep. No vender "COMPLIANT" como "auditado a fondo". El próximo Claude que haga B4/B5 debe mantener la distinción.

6. **TRADING: 7 SESIONES POSTERGADO (4-5-6-7-8-9-10).** Lo confronté en PHASE 1; JARP eligió meta igual. Es su decisión y la respeto — PERO en sesión 11 es la 8ª. Si vuelve a tomar meta, la prioridad #1 de userPreferences es ficción operativa. Decírselo sin filtro y sugerir que reescriba userPreferences si trading ya no es realmente #1. No es nag — es honestidad sobre la disonancia entre lo declarado y lo ejecutado.

7. **`mi-filesystem:write_file` volvió** (no estaba en sesión 9). Usado para backlog + continuity. Verificar disponibilidad al inicio igual.

8. **Continuity sigue creciendo (v8<v9).** Heredé de v8 la sugerencia de migrar a subdir `continuity/` o convención sin sufijo + git history. Sigue pendiente. Por ahora `_vN.md`.
