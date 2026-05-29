# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 29/05/2026 (sesión 12 — SPRINT v3.3 CERRADO: bump atómico v3.3.0 + cert full-coverage) | **Para:** Sesión 13
**Reemplaza:** v10 del 28/05/2026 (sesión 11)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v11.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 12 (resumen ejecutivo)

Sesión 12 **CERRÓ el sprint v3.3** ejecutando el **bump atómico v3.2.2 → v3.3.0** (la operación grande de cierre que el continuity v10 dejó planificada) + self-audit §4.14 + **re-certificación 7-axis full-coverage**. JARP eligió (B) cierre de sprint sobre (A) trading — **9ª postergación de trading consecutiva (sesiones 4-12)**.

**Resultados principales:**

1. **PHASE 0 — verde.** Deuda w (continuity v10 + backlog s11) confirmada en remoto. Cert registry consistente (DS v3.2.2 / PA-agent v1.3.0).

2. **PHASE 1 — JARP eligió (B) bump v3.3.0.** Trading confrontado UNA vez sin filtro (disonancia declarado-vs-ejecutado: userPreferences dice trading #1, 8 sesiones sin tocarlo). JARP eligió B con la confrontación leída. Respetado. **Sesión 13 = 10ª postergación si vuelve a no elegir A.**

3. **Bump atómico v3.3.0 — 31 archivos, COMPLETADO + verificado por SHA.**
   - 21 prompts (base + router→v3.3.0-ROUTER + 19 variants vX.3.0-DOMAIN) + 5 skills + main.py + tribunal_transversal.py + README + CLAUDE + CHANGELOG.
   - Método: clon en sandbox → script sed (grupos automatizables) + ediciones Python con asserts de unicidad (contenido) → patch único `git apply` → JARP commit/push vía GitHub Desktop.
   - **diffstat: 31 files, 159 insertions, 119 deletions.** Atomicidad §4.14.1 triple-verificada pre-push.

4. **Self-audit §4.14 pre-release — PASS (4/4).** A1 atomicidad (0 stamps activos stale), A2 skills content-version, A3 router↔agent minor match, A4 21/21 prompts stamped. Auto-corrección: A3 dio falso negativo de grep, verificado contra fuente (RULE 06) antes de declarar.

5. **Re-cert 7-axis Level 1 JARP DEEP — full coverage — PA-20260529-001.**
   - Ejecutado el protocolo real del PA-agent (leído `docs/certification_protocol.md` + `docs/audit_dimensions.md` + `docs/operational_levels.md`).
   - **0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT.** A6 coherence verificada end-to-end (19/19 footers BASE_PROTOCOL v3.3.0; router L117 versionless = placeholder dinámico non-finding verificado).
   - **SUPERSEDES PA-20260525-001** (v3.2.2, reduced 47% → ahora full 19/19). Cert registrada en DS CHANGELOG + jarp-toolkit (4 F&R).

---

## HALLAZGOS DE LA SESIÓN 12 (correcciones de registro)

- **"3 strings v3.0.0 en main.py" = MAL CARACTERIZADO.** Eran **3× v3.2.0** (product-face). No existe ningún v3.0.0 en main.py. Bumpeados a v3.3.0. Corregido.
- **orchestrator NO es stale uniforme** — es **versionado-por-módulo** (content-based): context_builder/prompt_engine/schema/tribunal = v3.0.0; goap_planner = v3.1.0; catalogs/main = v3.2.0. Cada docstring = versión de introducción del módulo. **Solo cara-de-producto bumpea** (main.py 3× + tribunal L381 Transparency Report, que estaba stale en v3.0.0 visible al usuario). `catalogs.py` NO entró (todos sus stamps son módulo/históricos correctos).
- **README + CLAUDE.md estaban stale en v3.2.0** (nunca subieron a v3.2.2). Sincronizados a v3.3.0.
- **Filosofía de versionado consolidada:** skills + docstrings de módulo = content-based (NO acoplados al release del agente). Solo variants + cara-de-producto siguen el minor del agente. El inventario de skills en base L30-34 confirmó independientemente: kac/ach/deception/verdict v2.6.0, adaptive v3.2.0 (validado por git log: 4 skills añadidos 05/05/2026 = CHANGELOG [2.6.x]).

---

## ESTADO ACTUAL VERIFICADO (29/05/2026 fin de sesión 12)

### Repo dark-strategist-agent
- **base `system_prompt.md`:** SHA `8ed2ac0`, 23.563 bytes. **Version: 3.3.0.** §4.14.1 norma router↔agent → v3.3.x.
- **CHANGELOG.md:** SHA `7d8e89f`, 17.836 bytes. Entry `[3.3.0]` + `[Certification] PA-20260529-001`.
- **router:** v3.3.0-ROUTER (L2/L17/L156/L157/L158 todos 3.3.0).
- **19 variants:** todos vX.3.0-DOMAIN + BASE_PROTOCOL v3.3.0.
- **5 skills:** frontmatter YAML completo. kac/ach/deception/verdict version 2.6.0; adaptive version 3.2.0 (ahora con frontmatter YAML válido).
- **orchestrator:** main.py + tribunal product-face en v3.3.0; resto módulos en su content-version (NO tocar).
- **Estado cert:** **`PA-20260529-001` ACTIVE — JARP_CERTIFIED full coverage** (válida hasta 27/08/2026 o v4.0.0).
- **Default model:** `claude-opus-4-7`
- **Sprint v3.3:** **CERRADO.** Bump aplicado, certificado, registrado.

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios sesión 12 (auditor; Level 0 satisfecho).

### Repo jarp-toolkit
- SHA `58c01a9`. Entry #30 DS → v3.3.0 / PA-20260529-001. Nota #16 + L7 last-updated actualizadas. Cert registry consistente.

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 12

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **DSv33-06** | 🔵 LATENT | identity-lock + refuerzo reglas críticas en base | Diferido formalmente en cert. Diseño + §4.14 self-audit propios. Su propio ciclo (v3.3.1 o v3.4). |
| **TK-COSMETIC** | 🟢 LOW (nuevo s12) | jarp-toolkit entry #30: `**Architecture v3.2.2:**` + `**NEW (v3.2.2):**` sin actualizar a v3.3.0 | Descripciones arquitectónicas, no stamps. Limpiar en próxima edición del toolkit. No vale commit propio. |
| **e3-e6** | 🟡 MODERATE | Cross-refs CHANGELOG DS↔PA-agent | Residuales menores |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone | Sin urgencia |

**CERRADAS en sesión 12:**
- **Bump atómico v3.3.0** ✅ — 31 archivos, verificado por SHA.
- **DSv33-S01** ✅ (version a 4 skills), **DSv33-S02** ✅ (frontmatter adaptive; MODERATE confirmado — carga por path explícito en SKILLS_CATALOG, no auto-discovery), **OBS-1** ✅ (headers slim), **t** ✅ (CHANGELOG stale items re-etiquetados RESOLVED).
- **Corrección main.py** ✅ (era v3.2.0 no v3.0.0).
- **README/CLAUDE stale v3.2.0** ✅, **tribunal Transparency Report stale v3.0.0** ✅.
- **Self-audit §4.14** ✅ PASS. **Re-cert full-coverage PA-20260529-001** ✅ registrada en DS CHANGELOG + toolkit.

**NUEVA deuda sesión 12:** TK-COSMETIC (low).

---

## ⚠️ ESTADO DEL SPRINT v3.3 — CERRADO

El sprint v3.3 (abierto desde sesión ~7, barrido cerrado sesión 11, bump cerrado sesión 12) está **COMPLETO**. v3.3.0 publicado, certificado full-coverage, registrado en los 3 repos. **No quedan operaciones de cierre pendientes.**

Los items del **ROADMAP v3.3 — TO INCORPORATE** (entry #30 del toolkit) son **features nuevos, no deuda de cierre**: Wizard CLI, RAG jurisdiccional, TOP 7 (markitdown/fact-checker/stop-slop/knowledge-work-plugins/marketingskills/Agent-Skills-for-Context-Engineering/infinity), bonus. Estos abren un **sprint v3.4 / v4.0**, son trabajo de feature, requieren su propio planning + GO. NO son continuación automática del v3.3.

---

## PROTOCOLO DE INICIO PARA SESIÓN 13

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo.
2. Cargar este prompt (v11).
3. **PHASE 0 — Verificación (rápida):**
   - Cert registry: DS v3.3.0 (PA-20260529-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
   - Confirmar push de continuity v11 (deuda de cierre s12, ver abajo).
4. **PHASE 1 — Decisión de roadmap:**
   - **(A) Trading hands-on** — Pine v6 / MQL5. **POSTERGADO 9 SESIONES (4-12).** Prioridad #1 declarada en userPreferences. ⭐ **Sesión 13 = 10ª.** Ya confrontado múltiples sesiones. Si JARP vuelve a no elegir A: la prioridad #1 escrita es ficción operativa — decirlo UNA vez sin filtro y sugerir reescribir userPreferences si trading ya no es #1 real. NO nag recurrente.
   - **(B) Sprint v3.4 / features DS** — el sprint v3.3 cerró; los items del roadmap (Wizard CLI, RAG jurisdiccional, TOP 7) son features nuevos. Requieren planning + GO propios. NO es continuación automática.
   - **(E) Audit real con DS** — field-testing; >1 mes certificado sin uso real. Sigue pendiente.
   - **(D) Otro proyecto JARP** (SAIA Sprint 1, etc.).
5. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas clave:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | repo name fijo | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor bump no cascadea | jarp-toolkit home de autorun | **version bump = operación ATÓMICA de cierre** | backlog se regenera vía self-audit | cert tiebreaker = CHANGELOG remoto del repo dueño | §4.14.1 validado como gobierno efectivo.

**NUEVAS / REFORZADAS en sesión 12:**
- **Versionado dual confirmado:** (a) variants + cara-de-producto (main.py, tribunal Transparency Report) siguen el minor del agente; (b) skills + docstrings de módulo del orchestrator = content-based (versión de introducción, NO acoplada al release). NO bumpear docstrings de módulo en un release del agente.
- **Cara-de-producto vs docstring-de-módulo:** product-face = lo que el usuario ve (--help, runtime print, Transparency Report header). Module docstring = interno. Solo product-face bumpea con el agente.
- **Método de bump validado:** clon sandbox → sed (grupos uniformes) + Python con asserts unicidad (contenido) → patch único `git apply` → dry-run en clon fresco contra remote HEAD → JARP commit/push. Genera patch SIEMPRE contra clon limpio del remote, NO contra árbol ya modificado (error capturado y corregido en s12).
- **Cert full-coverage > reduced conformance:** PA-20260529-001 elevó el registro de 47% (6/19) a 19/19. El barrido B1-B5 ES el trabajo de conformidad full-coverage; la cert lo consolida.
- **`git apply` en Windows CMD:** los comentarios `# texto` NO funcionan en CMD (solo Git Bash). Omitir todo tras `#` al dar comandos a JARP en CMD.
- **Borrar el .patch antes del commit** (`del archivo.patch`) para no subirlo al repo.

---

## DESCARTES — NO REINTRODUCIR
[Sin cambios desde v8/v9/v10.] MiroFish-ES, OASIS | n8n-mcp, claude-mem, etc. | claude-for-legal (ya rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun.
**Nuevo descarte sesión 12:** ninguno.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.3 (canónico):** `dark-strategist-agent/docs/v33_backlog.md` (sprint cerrado — al cierre debería marcar v3.3 DONE)
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v11.md`
- **JARP_TOOLKIT.md / .claude-init.md (CANÓNICOS):** `...\jarp-toolkit\`
- **Push siempre vía GitHub Desktop** salvo autorización explícita. Cuenta: `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. `github:get_file_contents` con `owner: JARPClaude` = patrón estándar read/verify. **jarp-toolkit es PRIVADO** — clone anónimo en sandbox falla; usar GitHub MCP o download_url autenticado.
- **Sandbox bash disponible:** clonar repos públicos (DS, PA-agent) al sandbox para grep/sed/patch es MÁS barato en tokens que leer archivos vía API. Patrón usado toda la sesión 12.
- **`github:create_or_update_file`** prohibido por defecto (límite ~10KB + autorización per-session). Ediciones = Ruta 3 (patch `git apply` o F&R manual).

### Commits sugeridos para cierre sesión 12 (continuity v11)
```
docs: continuity prompt v11 (session 12 close — sprint v3.3 CLOSED)

Session 12 — atomic bump v3.2.2 → v3.3.0 (31 files) + self-audit §4.14 + full-coverage re-cert PA-20260529-001.

NEW FILE:
- dark-strategist-continuity-prompt_v11.md: replaces v10 for session 13.

STATE:
- DS v3.3.0 — JARP_CERTIFIED PA-20260529-001 (full coverage 19/19, 0/0/0/0). Supersedes PA-20260525-001.
- Sprint v3.3 CLOSED. Roadmap items (Wizard CLI, RAG, TOP 7) = new features for v3.4, not closure debt.
- Dual versioning confirmed: variants + product-face track agent minor; skills + module docstrings content-based.
- Trading deferred 9 consecutive sessions (4-12) — flagged for session 13 (10th).

NO further v3.3 closure operations pending.
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 12

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.3.0 | PA-20260529-001 | ✅ ACTIVE (full coverage) | 27/08/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260525-001 (DS v3.2.2, reduced 47%). **VOID:** PA-20260426-002 (DS v2.5.1).
**PA-20260528-001/002** = audits DIAGNÓSTICOS (barrido), NO certificaciones.

---

## NOTAS DE SESIÓN 12 (auto-mejora del próximo Claude)

1. **El bump grande se ejecutó en una sesión.** Pre-bump (verificar carga de skills + strings reales) reveló deuda mal caracterizada (main.py v3.2.0 no v3.0.0). Lección: verificar el estado REAL de cada string antes de bumpear; no confiar en la caracterización del backlog.

2. **Versionado-por-módulo vs cara-de-producto.** El error inicial fue asumir "orchestrator stale en v3.2.0". Falso: cada módulo lleva su versión de introducción. Solo product-face bumpea. El próximo Claude: NO aplicar "todo → vX.Y.Z" a docstrings de módulo; distinguir qué es cara-de-producto (usuario lo ve) de qué es docstring interno.

3. **Patch contra clon limpio, SIEMPRE.** Generé el patch de cert sobre un árbol que ya tenía el bump → falló el dry-run (hunk de un cambio ya pusheado). Corregido regenerando contra clon fresco del remote. El dry-run en clon fresco es obligatorio antes de entregar cualquier patch.

4. **Verificar findings contra la fuente (RULE 06, otra vez).** A3 del self-audit y A6 de la cert dieron "anomalías" que resultaron falsos positivos de grep (router con espacio en stamp; router L117 placeholder dinámico). Ambos verificados contra el texto antes de clasificar. Mejor un falso positivo verificado que un finding afirmado en falso.

5. **Cert full-coverage es honestidad de registro.** La cert previa era reduced 47%; el barrido ya había cubierto 19/19. Subir el registro a full-coverage refleja el rigor real. No inflar, pero tampoco subdeclarar lo verificado.

6. **TRADING: 9 SESIONES POSTERGADO (4-12).** Confrontado UNA vez esta sesión; JARP eligió B con la confrontación leída. Su decisión, respetada. Sesión 13 = 10ª. Decirlo UNA vez sin filtro y sugerir reescribir userPreferences si trading ya no es #1 real. NO nag recurrente — honestidad sobre disonancia, no acoso.

7. **Sandbox bash >> API reads para operaciones masivas.** Clonar repo público + grep/sed/patch local es mucho más barato en tokens que leer 31 archivos vía `github:get_file_contents`. Patrón validado toda la sesión. (jarp-toolkit es privado → ahí sí GitHub MCP o download_url.)

8. **Continuity sigue creciendo (v10<v11).** Pendiente histórico: migrar a subdir `continuity/` o convención sin sufijo + git history. Por ahora `_vN.md`.

9. **El sprint v3.3 CERRÓ.** No hay más operación grande pendiente en la rama DS salvo (E) field-testing y los features del roadmap v3.4. El próximo Claude NO debe asumir que "queda trabajo de v3.3" — quedan features nuevos (otro sprint) y deuda residual menor (e3-e6, g, TK-COSMETIC, DSv33-06 diferido).
