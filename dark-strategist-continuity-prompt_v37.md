# Dark Strategist — Continuity Prompt v37

**Sesión origen:** 38 (Cowork / Claude for Windows) · **Fecha:** 15/07/2026
**Reemplaza:** v36 (borrar v36 — v37 único continuity vigente)

---

## ESTADO DEL SISTEMA

- **DS versión en repo:** v3.23.0 (cert PA-20260712-002 ACTIVE).
- **Trabajo de s38 aplicado al working tree local, NO commiteado, NO certificado, NO pusheado.** Candidato a **v3.24.0**.
- **PA-agent:** v1.3.0 (PA-20260527-002 ACTIVE).
- **Working tree:** SUCIO — 22 archivos modificados (GAP #1 fix, ver abajo). Sin commit todavía.
- **Repos:** `JARPClaude/dark-strategist-agent` (público), `JARPClaude/jarp-toolkit` (privado).

---

## QUÉ SE HIZO EN s38 — GAP #1 fix (cert-surface ↔ runtime)

**Problema resuelto:** los 19 variant `.md` (`prompts/system_prompt_<domain>.md`) NUNCA se inyectaban al runtime N1. El único lector era `router.py::DomainRouter` — huérfano (jamás importado por `main.py`/`context_builder.py`/`tribunal_transversal.py`) y desactualizado (14/20 dominios). Los N1 corrían solo con templates genéricos de `prompt_engine.py`, así que reglas como Legal LG08/LG09 nunca llegaban al modelo.

**Decisión tomada:** (a) fix injection — cablear los variants al pipeline. Elegida sobre (b) re-scope cert.

**Diseño (por qué no concatenación directa):** los variants NO son fragmentos inyectables — son prompts alternos con su propio contrato `BLOCK 0-7`. Inyectar el archivo completo competiría con el JSON real (`schema.Finding` / `json.loads` en `_call_agent`). Solución: **extracción por marcadores** `<!-- CATALOG:START -->` / `<!-- CATALOG:END -->` (soporta pares múltiples, se concatenan en orden). Se extrae SOLO: Severity Taxonomy + Domain Rules + Failure Catalog (Legal: +GEOFENCE y 12 sub-catálogos L01-L12; Financial: +Variance Decomposition Lenses). Se excluye: Phase 0, Forensic 7-Levels, WAR ROOM, BLOCK/OUTPUT FORMAT, Severity×Likelihood.

**Archivos modificados/creados (22 total en el diff):**
- `orchestrator/domain_catalog.py` — NUEVO. Loader con regex `findall`, cache por (domain, prompts_dir), fallback `""` para dominio no migrado/sin archivo/sin marcadores (cero regresión).
- `orchestrator/catalogs.py` — `DOMAIN_PROMPT_FILE` dict agregado (19 dominios; General sin entrada). `router.py::PROMPT_CATALOG` intacto, sin tocar.
- `orchestrator/prompt_engine.py` — `PromptEngine.__init__(prompts_dir)`; placeholder `{domain_catalog_block}` en `MASTER_TEMPLATE`/`ROLE_AGENT_TEMPLATE`; inyección en `build_rol_prompt`/`build_forense_prompt`. `build_synthesis_prompt` sin cambios.
- `orchestrator/tribunal_transversal.py` — 1 línea: `self.engine = PromptEngine(prompts_dir=config.get("prompts_dir", "./prompts"))`.
- `prompts/system_prompt_*.md` — 19 archivos, 2 pares de marcador c/u (Financial 3) + línea de header v3.24.0. Diff = solo esas líneas.
- `orchestrator/test_domain_catalog_all19.py` — NUEVO, 212 checks.

**Verificación completada (VÁLIDA):**
- Test offline `test_domain_catalog_all19.py`: **212 passed, 0 failed** — corrido en máquina de JARP, confirmado.
- `git diff --stat`: 22 files, 206 insertions(+), 5 deletions(-). Cada `.md` muestra ~8 líneas (Financial 10, Legal 9). Todo en rango esperado.
- **Auditoría byte-a-byte de los 19 `.md` contra GitHub main: 19/19 idénticos al original** (fuera de marcadores + header).

**⚠️ INCIDENTE s38 (lección crítica):** `system_prompt_startup.md` se escribió inicialmente con contenido ALUCINADO (dominio, taxonomía y RULES SU01-05 inventados, no los reales del repo). Se detectó porque el `git diff --stat` mostró 106 líneas en vez de ~8. Se corrigió re-fetcheando el original de GitHub y reescribiendo con marcadores. **Regla reforzada: al migrar/editar archivos existentes, verificar SIEMPRE contra la fuente real (git diff o fetch del original) antes de dar por bueno — no confiar en escritura "de memoria".**

---

## LO QUE FALTA (tuyo, no del agente) — antes de certificar v3.24.0

1. **E2E LIVE** contra el pipeline real con API key. Mínimo: fixture Legal `_livewatch/legal_ai_companion_tos.txt` (dispara LG08/LG09) — confirmar que el N1 aplica las reglas inyectadas y no solo criterio genérico. Recomendado sumar Startup (por el incidente) + 1-2 dominios más de control.
2. **Clasificación cert:** SUSTANTIVA (toca contenido de prompt que alimenta asignación de severidad en 19 dominios — NO es NON-BINDING como LW-1..7). Calibración axis A1-A7 la hace PA-agent.
3. **Bump v3.24.0:** `bump_stamps.ps1 -OldVersion 3.23.0 -NewVersion 3.24.0 -Apply` + CHANGELOG + roadmap rows + ACTIVE en README/CLAUDE.
4. **Push** vía GitHub Desktop/CLI (convención JARP).

---

## BACKLOG ABIERTO (NO resuelto en s38)

- **`SubAgentSpawner`:** MISMO bug — `self.prompts_dir` guardado, nunca leído. Los 9 N2 permanentes siguen 100% hardcoded en `PERMANENT_SUBAGENTS`. Fuera de scope de s38 (hallazgo original fue "runtime N1", no N2). Candidato natural para v3.25.0.
- **AI Disclaimer BLOCK 7 (RULE LG03):** no cableado a la síntesis/AFO todavía.
- **`router.py`:** huérfano + desactualizado. Candidato a borrar en cleanup — `DOMAIN_PROMPT_FILE` lo reemplaza funcionalmente (19/20 vs sus 14/20).
- **Trading hands-on:** POSTERGADO desde s4 (prioridad #1 en userPreferences, no re-confrontar salvo que JARP lo active explícitamente).

---

## PROTOCOLO DE INICIO (nueva sesión)

**PHASE 0 — verificación de estado:**
- Confirmar HEADs remotos reales (`list_commits perPage=3`) para DS y jarp-toolkit — determinar si el fix de s38 ya fue commiteado/pusheado o sigue en working tree local.
- Si YA está pusheado: DS debería estar en v3.24.0, cert nuevo. Verificar registro de cert (ambos canónicos concuerdan POSICIONALMENTE, lección drift s33/s34, NO Select-String).
- Si NO está pusheado: el fix sigue en working tree de JARP, esperando e2e LIVE + bump. Retomar desde "LO QUE FALTA".
- `orchestrator/_livewatch` NO trackeado (read-back del árbol, lección s35).

**PHASE 1 — decisión:** esperar GO de JARP. Candidatos: (a) cerrar v3.24.0 si falta e2e/bump, (b) atacar SubAgentSpawner (mismo patrón, v3.25.0), (c) AI Disclaimer BLOCK 7, (d) router.py cleanup.

**STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real. Verificar contra fuente real antes de dar por bueno. Trabajar en silencio, priorizar tokens. Español para conversación, inglés estricto para código/comentarios (prefijo `//--- `).
