# DARK STRATEGIST — PROMPT DE CONTINUIDAD
**Generado:** 07/06/2026 (sesión 31 — DS v3.17.0 LW-1 domain-resolver fix, shipped & JARP_CERTIFIED) | **Para:** Sesión 32
**Reemplaza:** v29 del 06/06/2026 (sesión 30)
**Ubicación:** `dark-strategist-agent/dark-strategist-continuity-prompt_v30.md`
**⚠️ BORRAR en este cierre:** v29 (`git rm` en el commit de cierre). v30 = único continuity vigente. Subir v30 al PROYECTO claude.ai + quitar v29.

## Inicialización
- **Claude Desktop:** autorun `JARP_TOOLKIT.md` → cargar este contexto.
- **claude.ai web:** leer este archivo desde el proyecto Dark Strategist.

---

## CONTEXTO SESIÓN 31 (resumen ejecutivo)

Track elegido: **B — Backlog valor-agregado → LW-1** (domain-resolver correctness fix). Trading (A) NO se eligió (**28ª sesión postergada, 4–31**).

**Resultado: DS v3.17.0 shipped y CERTIFICADO** (`PA-20260607-002`).

### 1. DS v3.17.0 — LW-1 DOMAIN-RESOLVER FIX (correctness)
`context_builder._resolve_domain` tenía **dos** defectos compuestos:
- **(1) substring bleed:** matcheaba claves de `DOMAIN_MAP` como substring crudo del subscenario → claves cortas (`"ma":"Financial"`, `"ops"`, `"hr":"Human Resources"`, `"sop"`) pegaban en cualquier stem que las contuviera (`transformation`→Financial vía "ma"; `threshold`→HR vía "hr"; `management`/`summary`/`marketing`/`devops`). En `--document` mode el subscenario = STEM del filename → mis-ruteaba documentos reales al **variant + Failure Catalog + lentes forenses equivocados**.
- **(2) order-dependence (latente, descubierto en s31):** devolvía el **primer** substring-match en orden de inserción del dict → el ruteo multi-token quedaba acoplado silenciosamente al layout del `DOMAIN_MAP`.

**Fix (contrato nuevo, determinista, order-invariant):**
- Separadores (`_ - . ` espacios) normalizados; el stem se tokeniza limpio.
- Claves evaluadas **MOST-SPECIFIC FIRST** (keyword más largo, tie-break alfabético) — **independiente del orden de inserción**.
- Claves cortas (≤3 chars: `ma`/`ops`/`hr`/`sop`/`gtm`/`pmf`/`nda`/`msa`) → **whole-token only** (mata el bleed).
- Claves compuestas/multi-word (`real_estate`, `human_resources`, `market_entry`, `series_a`, `unit_economics`, `ai governance`) → match de **frase normalizada**.
- Claves largas single-word → token-equal **o token-prefix** (`cyber` sigue resolviendo `cybersecurity`).
- **Exact-type fast path intacto.** **Ninguna clave borrada.** Docstring de módulo congelado en `v3.0.0` (content-based; sólo banners runtime rastrean el minor).
- `import re` + `_SEP = re.compile(r'[^a-z0-9]+')` añadidos al módulo.

**`orchestrator/test_domain_resolver.py`** (NUEVO): 23 checks offline $0 — repro LW-1 (`transformation`→Strategy vs `board_proposal`→Strategy), bleed muerto (`management`/`summary`/`threshold`/`devops`→General), tokens válidos (`project_ma_dd`→Financial, `ops`/`hr`/`nda`), prefijo largo (`cybersecurity`→Cybersecurity, `data_processing`→Operations), compuestas (`real_estate`/`series_a`/`market_entry`), exact-type, colisiones multi-token (most-specific wins: `social_media_strategy`→Strategy, `saas_unit_economics`→Startup, `cloud_security_review`→Cybersecurity), no-match→General.

### 2. DECISIÓN CLAVE (s31): A (order-invariant) sobre B (mínimo)
Se planteó A (longest-first/order-invariant) vs B (boundary-aware preservando orden de inserción). Ambas pasaban el core LW-1 19/19; diferían sólo en 3 colisiones multi-token. **Se eligió A** porque B sólo mata el síntoma visible (bleed) y deja vivo el Defecto 2 (acoplamiento al orden del dict); A mata ambos y vuelve el ruteo un contrato determinista documentable. Los 3 desempates que B "preservaba" eran **accidentes del orden de inserción**, no decisiones de diseño; los de A son discutiblemente más correctos (`cloud_security_review`→Cybersecurity). Alineado con la directiva permanente (s28): eliminar defectos latentes, valor real sobre barato-dormido.
> **Lección de proceso:** la recomendación inicial fue B (scope mínimo); cambió a A cuando JARP pidió la lectura estratégica/táctica/operativa. Cambiar de recomendación bajo un lente distinto, con razón explícita, es buena epistemología, no vacilación — pero NO declarar una decisión del usuario como confirmada sin que la diga (se cometió y corrigió en s31).

### 3. RE-CERT DS v3.17.0 — COMPLETA ✅ (CONFIRMATORY)
Auditor PA-agent v1.3.0 (`PA-20260527-002`). Self-audit L0 (`PA-20260607-001`) PASS. 7-ejes Level 1 JARP DEEP sobre delta v3.16.0→v3.17.0.
- **Por qué CONFIRMATORY:** el fix vive 100% en la **capa de routing del orchestrator** (pre-veredicto, upstream de synthesis). NO toca la superficie prompt/skill que audita PA-agent. Superficie forense (19 variants + 7 skills + base + router CONTENT) byte-idéntica salvo stamps.
- **Evidencia funcional (máquina real, post-apply + post-bump):** `test_domain_resolver` 23/23 + `smoke_test_e2e` **0 FAIL / 1 SKIP** (`b_unified_output` sin API key, no-bloqueante) con `c_fallback_intact` + `e_monotonic_verdict` INVIABLE + `r2_byo_corpus` PASS.
- **CERT EMITIDO:** `PA-20260607-002` — DS **v3.17.0 JARP_CERTIFIED**, **0/0/0/0**, BIAS_CHECK PASS. Válido hasta **07/09/2026 o v4.0.0**. **SUPERSEDES PA-20260606-006** (v3.16.0). Fix orchestrator no-forense → CONFIRMATORY.
- **Bump:** `bump_stamps.ps1 -OldVersion 3.16.0 -NewVersion 3.17.0` (23 files/69 stamps) + `bump_manual_v3_17_0.py` (4 banners operator-visible: main×2 / wizard / transparency report + bloque CHANGELOG; newline-aware, all-or-nothing, dry-run→apply). Banners frozen NO tocados (main/wizard docstring v3.10.0; tribunal provenance v3.15.0). One-shot BORRADO antes del commit.

---

## ⚠️⚠️ ESTADO DE CERTIFICACIÓN ⚠️⚠️

**DS repo v3.17.0 = CERTIFICADO (`PA-20260607-002`).** Sin version-gap. PA-20260606-006 (v3.16.0) → SUPERSEDED. PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE.

---

## REGISTRO POST-CERT — A APLICAR EN CIERRE (s31)
1. Archivos ya en disco (PHASE 2, untracked/modificados): `orchestrator/context_builder.py` (resolver A), `orchestrator/test_domain_resolver.py` (NUEVO).
2. Bump aplicado (PHASE 3): `bump_stamps.ps1` (prompts/README/CLAUDE) + `bump_manual_v3_17_0.py --apply` (banners main×2/wizard/transparency + CHANGELOG [3.17.0]).
3. CHANGELOG: bloque `[3.17.0]` con cert `PA-20260607-002` insertado sobre `[3.16.0]`.
4. `git rm dark-strategist-continuity-prompt_v29.md`.
5. `jarp-toolkit` + `.claude-init.md` → v3.17.0/PA-20260607-002 (Ruta 3: header + #30 [Version + CERT STATUS + Previous certs] + #16 + init #8; superseded += PA-20260606-006). Commit separado en repo jarp-toolkit.
6. **One-shot `bump_manual_v3_17_0.py` BORRAR** (mi-filesystem) antes del commit.
7. **Verificación post-push:** grep `3\.16\.0` repo-wide → 0 banners residuales (sólo refs históricas en CHANGELOG son legítimas). Verificar AMBOS canónicos concuerdan en v3.17.0/PA-20260607-002 (lección drift s29).

---

## DEUDA TÉCNICA — POST-SESIÓN 31

| # | Severidad | Item | Notas |
|---|-----------|------|-------|
| **RE-CERT v3.17.0** | ✅ CERRADA | v3.17.0 CERTIFICADO (PA-20260607-002) | 0/0/0/0, CONFIRMATORY. |
| **LW-1 domain resolver** | ✅ CERRADA | boundary-aware + most-specific-first + order-invariant | test 23/0; 2 defectos cerrados (bleed + orden). |
| **clash/gate/señales/provenance/reputational LIVE** | ✅ CERRADA (s30) | `b_unified_output` cerrado vía corrida live real s30 | Sin cambio. |
| **DSv34-SYNTH** | 🟢 ACEPTADA | Fallback determinista = sintetizador de producción | Sin cambio. |

### BACKLOG VALOR-AGREGADO — pendiente
- **🟠 LW-2 (mejora):** confidence corroboración frágil. `_apply_confidence` arma `multi_agent_confirmed` por `(severity, _norm_title)` sobre findings crudos; los títulos divergen entre agentes Y el sintetizador reescribe los unificados → consenso unánime registra `Confirmed by 2+: 0` → `driver_corroborated=False` → confianza sesgada a la baja. NON-BINDING (veredicto intacto). Mejora: corroborar por acuerdo de veredicto / similitud semántica, o propagar source-agent por finding. Slice propio.
- **🟡 LW-3 (UX — quick):** provenance granularidad por formato de señales. `retriever.load_corpus_files` splitea `.txt` por línea en blanco; señales en líneas consecutivas colapsan en 1 passage → atribución manda todo a "signal #1". Fix: documentar "una señal por párrafo" o splitear señales `.txt` por línea. Zero/low-code. Repro: `_livewatch/signals_acme.txt`.
- **🟢 LW-4 (NUEVO, s31 — refinamiento opcional):** desempate de dominio **posicional** ("gana el primer token de dominio del filename") como alternativa aún más intuitiva al actual most-specific/longest-first. Order-invariant respecto al dict pero respeta la convención de nombrar liderando con el dominio. Evaluar valor real vs el contrato actual (que ya cierra LW-1); slice aparte si aporta.
- **P5 extensión P14/P20** (candidato): extender reputational-risk a Public Sector (P14) + Startup (P20) — Activation v1.1.0 + Failure Catalog rows (prefijos PS/SU). El "3+2" diferido; evaluar valor real vs cobertura ya lograda con P11/P16/P19.
- **STANDING:** cada sesión, velar que el sistema sea mejor (más robusto/valioso/eficiente/valor agregado). Proponer mejoras proactivamente; nunca barato-dormido sobre valor real.

---

## ESTADO ACTUAL VERIFICADO (07/06/2026 — fin s31)

### Repo dark-strategist-agent
- **v3.17.0 — CERTIFICADO (`PA-20260607-002`)**. Default `claude-opus-4-7`. HEAD = commit de cierre v3.17.0 (**registrar SHA tras push**). HEAD previo (inicio s31) = `485e8fa`.
- **MODIFICADO:** `orchestrator/context_builder.py` — `_resolve_domain` boundary-aware + most-specific-first + order-invariant (+`import re`/`_SEP`). **NEW:** `orchestrator/test_domain_resolver.py` (23 checks).
- **De s30 vigente:** `skills/reputational-risk/SKILL.md` (v1.0.0) + `SKILLS_CATALOG` + bullet base #7 + RULES/rows P11/P16/P19 + `test_reputational_risk.py`.
- **De s29 vigente:** `overlap_score` + `_active_signals_tagged` + `_attribute_signal_provenance` post-veredicto + bloque `SIGNAL PROVENANCE` + `rag.provenance_min_overlap` + `test_provenance.py`.
- **De s28 vigente:** canal `--signals` + `RuntimeContext.signals_paths` + `test_signals.py`.
- **De s27 vigente:** `archetype_lenses.py` (5 lentes) + `_run_escalation_round` lens-driven + `test_archetype_lenses.py`.
- **De s26/s25 vigente:** `schema.should_escalate`/`_maybe_escalate` + `test_escalation.py`; `schema.compute_confidence`/`_apply_confidence` + `test_confidence.py`.
- `tools/bump_stamps.ps1` (NO cubre orchestrator/*.py ni CHANGELOG). `gc.auto 0` activo. `corpus/` vacío. `JURISDICTION_CORPUS_MAP = {}`. BYO `--corpus`/`--signals` activos.
- **7 skills**, **9 sub-agentes N2 permanentes**, **20 dominios P01–P20.**
- `smoke_test_e2e.py` + `smoke_contract.txt` GITIGNORADOS (local-only). `_livewatch/` throwaway no-commiteado.

### Repo prompt-architect-agent
- v1.3.0 (`PA-20260527-002`) ACTIVE. Auditor de la re-cert s31. Sin cambios.

### Repo jarp-toolkit
- header + #30 (Version/CERT STATUS/Previous certs) + #16 + `.claude-init.md` #8 → v3.17.0/PA-20260607-002. PRIVADO. **Verificar AMBOS canónicos concuerdan al cierre.**

### free-claude-code
- Proxy $0 para corridas no-cert. **`fcc-server` NO en PATH — instalar antes de usar.** Cert = Opus real sin proxy.

---

## PROTOCOLO DE INICIO PARA SESIÓN 32
1. **Desktop:** autorun `JARP_TOOLKIT.md`. **Web:** leer este archivo (v30).
2. **PHASE 0 — Verificación:**
   - v29 borrado, v30 único continuity.
   - Repo en v3.17.0. **Cert: DS v3.17.0 `PA-20260607-002` ACTIVE.** PA-agent v1.3.0 (`PA-20260527-002`) ACTIVE. `PA-20260606-006` SUPERSEDED.
   - **Verificar AMBOS canónicos concuerdan** (toolkit + init en v3.17.0/PA-20260607-002) — lección drift s29.
   - `rank_bm25` + `pydantic` instalados. `gc.auto 0` activo.
3. **PHASE 1 — Decisión:**
   - **(A) Trading hands-on** — **POSTERGADO 28 SESIONES (4–31).** Prioridad #1 en userPreferences. **NO re-confrontar.** Si s32 no elige A, asumir prioridad real ≠ escrita.
   - **(B) Backlog valor-agregado** — LW-2 (confidence corroboración); LW-3 (provenance granularidad, quick); LW-4 (desempate posicional, opcional); P5 extensión P14/P20.
   - **STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real.
4. Reportar phase por phase, esperar GO entre fases.

---

## DECISIONES ARQUITECTÓNICAS VIGENTES (NO REVERTIR)

**Heredadas:** Jerarquía AFO→Tribunal→N2 | límites (Tribunal_MAX 7, calls 40, n2 3, aad 3) | veredicto determinista (≥1 FATAL→INVIABLE) | inglés estricto skills/dominios | default `claude-opus-4-7` | §4.14.1 rige toda variante | prefijos 2-letras inmutables | auditor minor no cascadea | version bump = operación ATÓMICA de cierre | cert tiebreaker = CHANGELOG remoto | versionado dual (variants+product-face rastrean minor; skills+docstrings de módulo+catálogo de lentes+comments feature-landing = content-based/congelados) | bump_stamps.ps1 NO cubre orchestrator/*.py ni CHANGELOG → bump manual aparte | Sintetizador VIVO `_synthesize`, fallback determinista = sintetizador de producción; NO debilitar schema `Finding` | free-claude-code: free para no-cert, Opus real para cert | re-cert ID discipline: self-audit L0 y cert maestro IDs diarios separados | Sev×Likelihood NON-BINDING | SOX→tier 4-niveles | orden monotónico FATAL→LATENT al insertar filas | telephone-game resuelto v3.4 | context-degradation = LENTE | RAG = MECANISMO | ContextBuilder document-free | infinity/Docker RECHAZADO | **leer el módulo real antes de incorporar** | wizard SINTETIZA argv → mismo parser | bump no-forense → re-cert CONFIRMATORY | R2 = corpus BYO per-case | Floor R2/señales/provenance = OVERLAP DE TOKENS | mi-filesystem preserva escapes byte-exacto.

**De s25–s29:** Confianza/escalación/lentes/señales/provenance = metadata NO-VINCULANTE, determinista, post-hoc donde aplica; NUNCA tocan `final_verdict`/`Finding`. Docstrings de módulo congelados. Scripts de edición newline-aware + encadenados por archivo + all-or-nothing + dry-run.

**De s30:** Riesgo reputacional = SKILL markdown (#7), NO lente-arquetipo. Skill NOMBRA/DETECTA; Failure Catalog VINCULA severidad; tabla determinista COMPUTA. `VERDICT_IMPACT: NONE` = no computa/override, NO sin-severidad. Activación⊆binding. No-duplicación de rows. No-impacto de skill markdown = garantía ESTRUCTURAL. bump_manual inserts LINE-BASED. El live e2e destapa lo que el offline no puede.

**De s31 (nuevas):**
- **Domain routing = boundary-aware + MOST-SPECIFIC-FIRST (longest keyword, tie-break alfabético) + ORDER-INVARIANT.** Claves cortas (≤3) whole-token only; compuestas = frase; largas = token-equal/prefix. Mata substring-bleed Y la orden-dependencia. Ninguna clave borrada. Exact-type fast path intacto. `_resolve_domain` es upstream de synthesis → no toca el verdict path.
- **Al arreglar un defecto, preferir el contrato order-invariant/most-specific sobre preservar comportamiento incidental** — eliminar el defecto latente, no sólo el síntoma visible (directiva robustez s28).
- **NO declarar una decisión del usuario como confirmada sin que la diga explícitamente** (el "regresión verde" no es elección de A/B; el test que pasa lo escribió Claude → evidencia circular).
- **El bump_manual cubre 4 banners operator-visible:** main×2 (argparse desc + print header) / wizard (run_wizard print) / transparency report (tribunal). Los docstrings de módulo (main/wizard v3.10.0) y refs feature-landing (tribunal provenance v3.15.0) son FROZEN.

---

## DESCARTES — NO REINTRODUCIR
MiroFish-ES, OASIS | n8n-mcp, claude-mem | claude-for-legal | servicios comerciales | "vibración cuántica" | MEGA-PAQUETE Copilot | `HandoffPacket` Pydantic full | debilitar schema `Finding` | Severity×Likelihood VINCULANTE | telephone-game (resuelto v3.4) | context-degradation como driver | infinity/Docker baseline RAG | embeddings densos baseline | pre-cargar corpus jurisdiccional en el repo | floor por score BM25 | confianza/escalación/lentes/señales/provenance como driver del veredicto | impersonar personas reales en lentes | "consenso → eficiencia" como métrica | bumpear docstrings/catálogo/comments-feature-landing congelados | re-usar ids `FOR-*` en escalamiento | anchors `\n` literal en CRLF | doblar manual lo que bump_stamps ya cubre | conflacionar corpus (grounding) con señales (evidencia) | scripts que escriben cada edit desde el snapshot original | activación dormida sobre activación amplia | auto-reporte del agente para provenance | campo de provenance en `Finding` | riesgo reputacional como lente-arquetipo (usar SKILL) | duplicar Failure-Catalog rows (REUSAR) | activar skill en dominios sin Failure Catalog rows | transcribir líneas largas como anclas (usar line-based) | **domain routing por substring crudo / acoplado al orden de inserción del dict — usar boundary-aware + most-specific-first + order-invariant — s31** | **borrar claves cortas del DOMAIN_MAP para arreglar el bleed (whole-token match las preserva) — s31**.

---

## REFERENCIAS RÁPIDAS

- **Repo local DS:** `C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent\`
- **Este archivo:** `dark-strategist-agent/dark-strategist-continuity-prompt_v30.md` (v29 borrado s31)
- **jarp-toolkit / .claude-init (CANÓNICOS):** `...\jarp-toolkit\` (PRIVADO). **Verificar AMBOS concuerdan al cierre.**
- **Push siempre vía GitHub Desktop / CLI.** Cuenta `JARPClaude`. **OneDrive en PAUSA para git pesado; `gc.auto 0` activo.**
- **MCPs:** mi-filesystem, GitHub. Si mi-filesystem timeoutea: reiniciar Claude Desktop.
- **PowerShell de JARP:** NO acepta `&&` (por separado o `;`). `del` de varios usa COMAS. env var = `$env:VAR="..."`. `cd` antes de scripts (bump/one-shots desde RAÍZ; tests desde `orchestrator/`). bump_stamps.ps1 con params NOMBRADOS (`-OldVersion X -NewVersion Y [-Apply]`).
- **Método de edición:** stamps multi-archivo = `tools/bump_stamps.ps1`. Banners orchestrator + CHANGELOG = script Python anclado all-or-nothing + NEWLINE-AWARE (dry-run → --apply), a la RAÍZ. Edits prosa/código pequeños/archivo nuevo = mi-filesystem directo (full-overwrite; verificar read-back). Canónicos (archivos grandes) = **Ruta 3** (bloques find-replace que JARP aplica en editor) — NO full-overwrite (riesgo al re-emitir archivos grandes). `github:create_or_update_file` prohibido por defecto. NO ejecuto Python/PS en la máquina de JARP → JARP corre regresión y scripts.
- **Domain routing (`--document` mode):** dominio se infiere del STEM del filename, ahora boundary-aware + most-specific-first. Para pinear dominio sin ambigüedad usar `--type X`. Colisiones multi-token → gana el keyword más largo (determinista).
- **Smoke-test E2E (LOCAL, gitignorado):** `python smoke_test_e2e.py` → **12 PASS / 1 SKIP** offline. Tests nuevos s31: `test_domain_resolver` 23/0. `pip install rank_bm25 pydantic` antes.
- **Deps runtime DS:** anthropic, pydantic, requests, google-auth/-oauthlib/-api-python-client, python-dotenv, markitdown, rank_bm25.

### Commits de cierre sesión 31
**Repo dark-strategist-agent (v3.17.0 cert) — commit atómico:**
```
fix: DS v3.17.0 — domain resolver LW-1 (boundary-aware + most-specific-first + order-invariant) — kills substring-bleed + order-dependence, test_domain_resolver 23/23 + JARP_CERTIFIED PA-20260607-002
```
Incluye: `orchestrator/context_builder.py`, `orchestrator/test_domain_resolver.py`, banners (`orchestrator/{main,wizard,tribunal_transversal}.py`) + prompts/README/CLAUDE stamps (bump_stamps), `CHANGELOG.md`, `dark-strategist-continuity-prompt_v30.md`; `git rm dark-strategist-continuity-prompt_v29.md`. NO incluye el one-shot (`bump_manual_v3_17_0.py`, borrado).
**Repo jarp-toolkit:**
```
docs: sync DS v3.17.0 / PA-20260607-002 (LW-1 domain resolver fix) — header + entry #30 (Version/cert/superseded) + note #16 + .claude-init #8
```

---

## CERTIFICACIONES ACTIVAS — AL CIERRE DE SESIÓN 31

| Repo | Versión repo | REPORT_ID | Certifica | Status | Expira |
|---|---|---|---|---|---|
| **prompt-architect-agent** | v1.3.0 | PA-20260527-002 | v1.3.0 | ✅ ACTIVE | 25/08/2026 o v2.0.0 |
| **dark-strategist-agent** | **v3.17.0** | **PA-20260607-002** | **v3.17.0** | ✅ ACTIVE | 07/09/2026 o v4.0.0 |

**SUPERSEDED:** PA-20260606-006 (v3.16.0), PA-20260606-004 (v3.15.0), PA-20260606-002 (v3.14.0), PA-20260605-002 (v3.13.0), PA-20260604-004 (v3.12.0), PA-20260604-002 (v3.11.0), PA-20260603-006 (v3.10.0), PA-20260603-004 (v3.9.0), PA-20260603-002 (v3.8.0), PA-20260602-002 (v3.7.0), PA-20260602-001 (v3.6.0), PA-20260601-004 (v3.5.0), PA-20260601-002 (v3.4.0), PA-20260529-001 (v3.3.0), PA-20260525-001 (v3.2.2). **VOID:** PA-20260426-002 (v2.5.1).

---

## NOTAS DE SESIÓN 31 (auto-mejora del próximo Claude)

1. **LW-1 tenía DOS defectos, no uno.** El backlog documentaba el substring-bleed; leer el código vivo reveló la orden-dependencia latente debajo. Leer el módulo real antes de fixear paga.
2. **A vs B: elegir el contrato robusto sobre el mínimo cuando el costo es trivial.** B fijaba el síntoma; A fija la causa (order-invariance). Costo de A: 1 línea + 3 expectativas de test. Directiva s28 (robustez) lo justifica.
3. **Honestidad sobre la decisión del usuario.** Se declaró "B confirmado" tras un screenshot de regresión verde que NO era elección de B (el test lo escribió Claude → circular). Corregido: NO asumir decisiones; pedir confirmación explícita en bifurcaciones.
4. **Dry-run en MI sandbox antes de escribir en el repo de JARP.** El resolver y el bump_manual se validaron contra DOMAIN_MAP real / mock files (idempotencia + frozen-refs intactos + cero banner residual) ANTES de tocar disco. Disciplina dry-run honrada sin ejecutar en la máquina de JARP.
5. **Verificación content-based + grep de completitud.** Tras el bump: grep `3\.16\.0` repo-wide → 0 banners residuales (refs históricas en CHANGELOG son legítimas). Read-back de archivos editados.
6. **Banners operator-visible = 4** (main×2/wizard/transparency). Documentado en cada entry "Versioning" del CHANGELOG; usarlo como checklist en cada bump. Frozen: docstrings de módulo + refs feature-landing.
7. **bump granularidad:** se eligió minor (v3.17.0) sobre patch (v3.16.1) — el histórico de certs es 100% `.0`; un slice = un minor. Consistencia sobre tecnicismo.
8. **TRADING: 28 SESIONES POSTERGADO (4–31). NO re-confrontar.**
9. **LW-4 nace de LW-1:** el desempate posicional ("primer token de dominio gana") es candidato a refinamiento aún más intuitivo; evaluar valor real vs el contrato most-specific actual antes de invertir.
