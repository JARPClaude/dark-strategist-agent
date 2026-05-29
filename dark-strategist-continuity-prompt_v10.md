# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 28/05/2026 (sesión 11 — barrido de prompts CERRADO: B4a+B4b+B5) | **Para:** Sesión 12
**Reemplaza:** v9 del 28/05/2026 (sesión 10)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v10.md`

## Inicialización
- **Claude Desktop:** después del autorun de `JARP_TOOLKIT.md` (rutas en `jarp-toolkit\`), cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO DE LA SESIÓN 11 (resumen ejecutivo)

Sesión 11 **CERRÓ el barrido de prompts** (la forma accionable de la deuda n). Completó B4a (7 variants sweep) + B4b (legal deep) + B5 (5 skills). **26 artefactos revisados en total (21 prompts + 5 skills).** Resultado macro: **§4.14.1 validado como gobierno efectivo de punta a punta — 19/19 variants COMPLIANT, 0 violaciones de contrato.**

**Resultados principales:**

1. **PHASE 0 — todo verde.** Las 3 deudas de cierre de sesión 10 confirmadas cerradas: **u** (continuity v9 en remoto, SHA `7dccdf6`), **v** (backlog B3-DONE en remoto), **DSv33-08** (dedent router verificado por rotación de SHA: `36dac79`→`3c2d692`). Cert registry consistente.

2. **PHASE 1 — JARP eligió (B) continuar barrido v3.3.** **Trading (A) postergado 8ª sesión consecutiva (4-5-6-7-8-9-10-11).** Confronté sin filtro (2 veces: en PHASE 1 y al recibir GO). JARP eligió B con la confrontación completa leída. Su decisión, respetada.

3. **B4a — 7 variants (§4.14.1 sweep): 7/7 COMPLIANT.** publicsector, medical, marketing, operations, hr, strategy, startup. REPORT_ID `PA-20260528-002`.

4. **B4b — legal (DEEP pass): COMPLIANT, 0 findings reales, 12/12 catálogos completos.**
   - **Hallazgo importante:** los 6 catálogos legales históricamente señalados como faltantes (L05/L06/L09/L10/L11/L12) están **presentes y completos**. Una porción material de la "deuda 38 MODERATE fantasma" eran estos catálogos, **ya resueltos en remoto (sesión 9, SHA `0a04ea1`) pero nunca trackeados como cerrados.**
   - **LGv33-01 y LGv33-02 = NON-FINDINGS** (falsos positivos míos, descartados contra el texto literal de §4.14.1). LGv33-01: el BLOCK 7 de legal es el ejemplo canónico que el contrato cita como permitido. LGv33-02: el naming solo exige prefijo 2-letras.

5. **B5 — 5 skills (auditoría de metadata/formato): contenido sólido, 2 findings de metadata.**
   - **DSv33-S01 (A6, MODERATE):** 4 de 5 skills (kac/ach/deception/verdict-verification) sin version stamp; la base les asigna v2.6.0 sin confirmación in-situ. adaptive-autonomous-drive SÍ porta v3.2.0 (coincide). **Resuelve PI1.**
   - **DSv33-S02 (A5/A6, PENDING):** adaptive-autonomous-drive **carece de frontmatter YAML** (empieza con `#` markdown, sin `name`/`description` requeridos por auto-discovery de Agent Skills). Los otros 4 sí lo tienen. Severidad MODERATE↔SERIOUS según mecanismo de carga — **verificar `orchestrator/catalogs.py` SKILLS_CATALOG antes de fijar severidad.**
   - **Ironía estructural:** ningún skill está completo (el único con versión es el único sin frontmatter válido; los 4 con frontmatter válido no tienen versión).

6. **Cierres adicionales gratis (de leer la base completa en B4b):** DSv33-03 verificado en texto (monotonic aplicado); version-stamp router↔agente verificado COMPLIANT (3.2.x ↔ 3.2.x); **PI2 cerrable** (no es contradicción — §4.13 unit-cluster vs router domain-variant son capas distintas; skills ortogonales).

7. **Corrección honesta (OBS-1):** dije "18 de 19 variants slim" en B4a asumiendo legal slim sin leerlo. **Real: 17 slim** — base + trading + legal traen provenance completo. Corregido en backlog.

---

## ESTADO ACTUAL VERIFICADO (28/05/2026 fin de sesión 11)

### Repo dark-strategist-agent
- **base `system_prompt.md`:** SHA `f7c6098`, 23.529 bytes. Stamp v3.2.2 INTACTO.
- **router `system_prompt_router.md`:** SHA `3c2d692`, 7.770 bytes (DSv33-08 dedent aplicado). Stamp v3.2.0-ROUTER INTACTO.
- **legal `system_prompt_legal.md`:** SHA `0a04ea1`, 15.208 bytes. 12/12 catálogos completos.
- **`docs/v33_backlog.md`:** ACTUALIZADO sesión 11 (B4+B5 + findings + PI status). **Local sin push (deuda w).**
- **NUEVO `dark-strategist-continuity-prompt_v10.md`:** este archivo. **Local sin push (deuda w).**
- **Estado cert:** **`PA-20260525-001` ACTIVE — JARP_CERTIFIED** (válida hasta 23/08/2026 o v4.0.0). **Sin impacto en sesión 11.**
- **Sprint v3.3 EN PROGRESO:** barrido CERRADO; bump atómico v3.3.0 NO aplicado (operación de cierre, sesión 12+).
- **Default model:** `claude-opus-4-7`

### Repo prompt-architect-agent
- v1.3.0, cert `PA-20260527-002` ACTIVE. Sin cambios sesión 11. (Auditor; Level 0 satisfecho por cert vigente.)

### Repo jarp-toolkit
- Cert registry consistente. Sin cambios sesión 11.

---

## DEUDA TÉCNICA — ESTADO POST-SESIÓN 11

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **w** | 🟡 MODERATE (op) | Push de continuity v10 + `docs/v33_backlog.md` actualizado | JARP vía GitHub Desktop al cierre |
| **DSv33-06** | 🔵 LATENT | identity-lock + refuerzo reglas críticas en base | Diseñar bloque con GO. Folding en bump. |
| **DSv33-S01** | 🟡 MODERATE | version stamp ausente en 4 skills | Añadir `version: 2.6.0` a frontmatter en bump |
| **DSv33-S02** | 🟡→🟠 PENDING | adaptive-autonomous-drive sin frontmatter YAML | Verificar `catalogs.py` SKILLS_CATALOG; normalizar a YAML (name+description+version) |
| **t** | 🟢 LOW | CHANGELOG `[3.2.2]` ítems stale "deferred to v3.3" | Limpiar en entry v3.3.0 |
| **e3-e6** | 🟡 MODERATE | Cross-refs CHANGELOG DS↔PA-agent | Residuales menores |
| **g** | 🟢 LOW | `devil-advocate-agent` copia manual → git clone | Sin urgencia |
| **OBS-1** | 🟢 LOW (cosmético) | 17 variants header slim (solo base+trading+legal completos) | Normalizar en bump |

**CERRADAS en sesión 11:**
- **Barrido de prompts (deuda n forma "completar barrido")** ✅ — B4a+B4b+B5 hechos. 26 artefactos. Residual = cerrar DSv33-06 + S01/S02 en bump.
- **u** (push v9) ✅, **v** (backlog B3-DONE) ✅, **DSv33-08** (dedent) ✅ — verificadas en PHASE 0.
- **PI1** ✅ resuelto (→ S01). **PI2** ✅ cerrable (documentar, no fix).
- **LGv33-01/02** ✅ non-findings verificados contra contrato.
- **DSv33-03** ✅ verificado en texto de base. **Version-stamp router↔agente** ✅ COMPLIANT.

**NUEVA deuda sesión 11:** w (push), DSv33-S01, DSv33-S02 (pending).

---

## ⚠️ ESTADO DEL SPRINT v3.3 (LEER ANTES DE CONTINUAR)

Sprint **abierto**. Barrido CERRADO. Contenido commiteado mid-sprint bajo stamp 3.2.2 (correcto — bump atómico al cierre). NO "arreglar" stamps.

**Checklist de CIERRE:**
1. ✅ Completar barrido de findings (B1-B5) — HECHO sesión 11.
2. **Version bump atómico v3.2.2 → v3.3.0** across base + router (→v3.3.0-ROUTER) + 19 variants (vX.3.0-DOMAIN + BASE_PROTOCOL v3.3.0) + **5 skills** + README + CLAUDE.md. NUNCA parcial (§4.14.1).
   - Fold: OBS-1 (17 headers slim), DSv33-S01 (version a 4 skills), DSv33-S02 (frontmatter adaptive — verificar carga antes), DSv33-06 (si se aprobó).
3. Verificar 3 strings `v3.0.0` en `orchestrator/main.py` (confirmar presencia antes de tocar).
4. CHANGELOG `[3.3.0]` + limpieza ítems stale (deuda t).
5. Self-audit pre-release (§4.14).
6. Re-cert por PA-agent v1.3.0 (minor bump nuevo → cert fresca).

---

## PROTOCOLO DE INICIO PARA SESIÓN 12

1. **Claude Desktop:** autorun `JARP_TOOLKIT.md`. **claude.ai web:** leer este archivo.
2. Cargar este prompt (v10).
3. **PHASE 0 — Verificación (rápida):**
   - Cert registry: DS v3.2.2 (PA-20260525-001) + PA-agent v1.3.0 (PA-20260527-002) ACTIVE.
   - Confirmar deuda w (continuity v10 + backlog actualizado) pusheada.
4. **PHASE 1 — Decisión de roadmap:**
   - **(A) Trading hands-on** — Pine v6 / MQL5. **POSTERGADO 8 SESIONES (4-5-6-7-8-9-10-11).** Prioridad #1 declarada en userPreferences. ⭐ **Máxima urgencia.** Sesión 12 = 9ª. Ya lo confronté 2 sesiones seguidas. Si JARP vuelve a tomar otra cosa: la prioridad #1 escrita es ficción operativa. Decírselo sin filtro UNA vez y sugerir reescribir userPreferences si trading ya no es #1. No repetir como nag — dicho, su decisión.
   - **(B) Cierre de sprint v3.3 — bump atómico v3.3.0** — el barrido ya cerró; este es el siguiente paso lógico de la rama DS. Operación grande (26 artefactos + docs + cert). Requiere plan + GO + contexto fresco. Antes del bump: decidir DSv33-06 (diseñar identity-lock) y verificar carga de skills (DSv33-S02).
   - **(E) Audit real con DS** — field-testing; >1 mes certificado sin uso real.
   - **(D) Otro proyecto JARP** (SAIA Sprint 1, etc.).
5. Reportar phase por phase, esperar GO entre fases.

---

## ROADMAP v3.3 DS

[Heredado de v8/v9. Backlog residual itemizado vive en `docs/v33_backlog.md`.]

### Barrido de prompts (deuda n) — ✅ CERRADO sesión 11
- ✅ B1 base+router (6 findings cerrados, DSv33-06 diferido)
- ✅ B2+B3 11 variants (compliant)
- ✅ B4a 7 variants (compliant)
- ✅ B4b legal (compliant, 12/12 catálogos)
- ✅ B5 5 skills (DSv33-S01/S02 para bump)

### Bloques pre-existentes (Sprint 2-4): TOP 7 + estructural + plataforma
[Sin cambios — ver v8/v9: markitdown, fact-checker, stop-slop, marketingskills, Cookbook, Agent-Skills-for-Context-Engineering, knowledge-work-plugins, infinity, Wizard CLI, claude-code-security-review, smart model routing, spec-kit.]

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas clave:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | repo name fijo | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor bump no cascadea | jarp-toolkit home de autorun | **version bump = operación ATÓMICA de cierre** | **backlog se regenera vía self-audit, NO se recupera** | **backlog regenerado se PERSISTE en `docs/v33_backlog.md`** | cert tiebreaker = CHANGELOG remoto del repo dueño | §4.14.1 validado como gobierno efectivo.

**NUEVAS en sesión 11:**
- **§4.14.1 Output Format Contract permite explícitamente BLOCKs ≥7** para secciones domain-mandatory (ej: legal BLOCK 7 AI_DISCLAIMER es el ejemplo canónico). NO confundir la frase "No additional BLOCKs ≥7" de otros variants (declaración de hecho) con prohibición.
- **§4.13 (activation matrix) y router (19 domains) son CAPAS DISTINTAS** — unit-cluster vs domain-variant — reconciliadas vía Primary Unit de cada variant. NO es contradicción (cierra PI2).
- **Los skills son ORTOGONALES al routing de dominio** — se activan por trigger (pre-FATAL, ambigüedad, stakes altos), no por dominio. No participan del mapeo §4.13↔router.
- **Convención canónica de skill (a unificar en bump):** frontmatter YAML con `name` + `description` + `version`. Hoy 4 skills tienen name/description sin version; 1 (adaptive) tiene version sin frontmatter YAML. Ninguno está completo.
- **Contract sweep ≠ deep pass** (reforzado): B2/B3/B4a son sweeps de contrato; B1/B4b son deep. Un sweep COMPLIANT NO certifica ausencia de findings A3/A5 internos.
- **Disciplina de batch confirmada otra vez:** B4 partido en B4a (sweep 7) + B4b (legal deep, solo) + B5 (skills). No encadenar deep passes con sweeps en un turno.
- **Verificar antes de asumir:** el error OBS-1 (asumir legal slim) refuerza RULE 06. Leer el archivo, no inferir su estado.

---

## DESCARTES — NO REINTRODUCIR
[Sin cambios desde v8/v9.] MiroFish-ES, OASIS | n8n-mcp, claude-mem, etc. | claude-for-legal (ya rescatada) | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | rutas viejas de autorun.
**Nuevo descarte sesión 11:** ninguno.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Backlog v3.3 (canónico):** `dark-strategist-agent/docs/v33_backlog.md`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v10.md`
- **JARP_TOOLKIT.md / .claude-init.md (CANÓNICOS):** `...\jarp-toolkit\`
- **Push siempre vía GitHub Desktop** salvo autorización explícita. Cuenta: `JARPClaude`.
- **MCPs:** mi-filesystem, GitHub. **`mi-filesystem:write_file` disponible sesión 11** — usado para backlog + este continuity. **Solo full overwrite** (sin edición parcial).
- **`github:get_file_contents`** con `owner: JARPClaude` = patrón estándar read/verify. Funcionó perfecto toda la sesión. **Listar directorio (path=dir) es más barato en tokens que leer cada archivo** — usado en PHASE 0.
- **`github:create_or_update_file`** prohibido por defecto (límite ~10KB + autorización per-session). Ediciones quirúrgicas = Ruta 3.

### ⚠️ REGLA TOOL CONFUSION (heredada, vigente)
- `mi-filesystem:*` → filesystem REAL Windows (`C:\`). JARP lo ve/commitea.
- `create_file`/`str_replace`/`bash_tool` → sandbox Claude (Linux). JARP no lo ve salvo `present_files`.
- Path `C:\` → preferir `mi-filesystem:*`.

### Commits sugeridos para cierre sesión 11 (deuda w)

**Backlog:**
```
docs: update v3.3 backlog — B4+B5 complete, prompt sweep CLOSED

- B4a: 7 variants §4.14.1 sweep, all COMPLIANT
- B4b: legal deep pass, COMPLIANT, 12/12 sub-area catalogs verified
- B5: 5 skills metadata audit — DSv33-S01 (version gap) + DSv33-S02 (frontmatter)
- PI1 resolved, PI2 closable, LGv33-01/02 non-findings
- §4.14.1 validated end-to-end: 19/19 variants compliant, 0 violations
- REPORT_ID PA-20260528-002 (diagnostic, no cert impact)
```

**Continuity:**
```
docs: continuity prompt v10 (session 11 close)

Session 11 — prompt sweep CLOSED (B4a+B4b+B5). 26 artifacts reviewed.

NEW FILE:
- dark-strategist-continuity-prompt_v10.md: replaces v9 for session 12.

CONTENT:
- §4.14.1 validated as effective governance: 19/19 variants compliant.
- legal deep pass: 12/12 catalogs complete (6 historically-flagged now confirmed).
- skills: DSv33-S01 (version traceability) + DSv33-S02 (adaptive frontmatter, pending load-mechanism check).
- DSv33-03 text-verified; router↔agent version-stamp COMPLIANT; PI2 closable.
- Pending for bump: DSv33-06 + DSv33-S01/S02 + OBS-1 (17 slim headers).
- Trading deferred 8 consecutive sessions (4-11) — flagged for session 12 (9th).

NO CHANGES to DS cert state — DS v3.2.2 / PA-20260525-001 ACTIVE unchanged.
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 11

| Repo | Versión | REPORT_ID | Status | Expira |
|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | v3.2.2 | PA-20260525-001 | ✅ ACTIVE | 23/08/2026 o v4.0.0 |

**PA-20260528-001** (B1) y **PA-20260528-002** (B4+B5) = audits DIAGNÓSTICOS (barrido de findings), NO certificaciones. No alteran estado de cert. Cert previas SUPERSEDED/VOID sin cambios.

---

## NOTAS DE SESIÓN 11 (auto-mejora del próximo Claude)

1. **El barrido cerró revelando que parte de la "deuda fantasma" ya estaba resuelta.** Los 6 catálogos legales L05/L06/L09/L10/L11/L12, núcleo de los "38 MODERATE", estaban completos en remoto desde sesión 9 — solo nunca se trackeó su cierre. Lección: deuda no-trackeada ≠ deuda no-resuelta. Verificar el estado real antes de asumir que algo falta.

2. **Levantar findings con cautela y verificarlos contra la fuente funciona.** LGv33-01/02 los marqué PENDING_INVESTIGATION sin afirmar violación; la lectura del contrato los descartó como non-findings. Mejor un falso positivo verificado que una violación afirmada en falso. Pero costó un read de 23KB — el trade-off valió porque la base dio cierres extra (DSv33-03, version-stamp, PI2).

3. **Verificar antes de asumir (RULE 06, otra vez).** Dije "18 variants slim" asumiendo legal slim sin leerlo. Real: 17. Error detectado y corregido en el mismo turno al leer legal. El próximo Claude: NO inferir el estado de un archivo que no leíste.

4. **Disciplina de batch sostenida toda la sesión.** B4 partido en B4a (7 sweep) + B4b (legal deep solo) + B5 (skills). Cada uno su turno, GO entre fases. No se encadenó deep + sweep. Resultado: calidad sin hallucination ni budget blowout.

5. **Contract sweep ≠ deep pass (persistente).** El próximo Claude que vuelva sobre variants sweepeados (B2/B3/B4a) debe recordar: COMPLIANT de contrato NO = auditado a fondo. Si se quiere profundidad por variant, es 7-axis deep, no sweep.

6. **TRADING: 8 SESIONES POSTERGADO (4-11).** Confrontado 2 veces esta sesión; JARP eligió B con la confrontación leída. Es su decisión, respetada. Sesión 12 = 9ª. Decirlo UNA vez sin filtro y sugerir reescribir userPreferences si trading ya no es #1 real. No convertirlo en nag recurrente — es honestidad sobre disonancia declarado-vs-ejecutado, no acoso.

7. **`mi-filesystem:write_file` disponible** (como sesión 10). Solo full overwrite. Verificar al inicio igual.

8. **Continuity sigue creciendo (v9<v10).** Pendiente histórico: migrar a subdir `continuity/` o convención sin sufijo + git history. Por ahora `_vN.md`.

9. **El bump atómico v3.3.0 es la próxima operación grande de la rama DS.** No improvisar. Requiere plan explícito, GO, contexto fresco, y resolver antes DSv33-06 (diseño) + DSv33-S02 (verificar carga). 26 artefactos + docs + re-cert. Es trabajo de ≥1 sesión dedicada.
