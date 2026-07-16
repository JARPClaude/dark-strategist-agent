# Dark Strategist — Continuity Prompt v38

**Sesión origen:** 39 (Cowork / Claude for Windows) · **Fecha:** 15/07/2026
**Reemplaza:** v37 (borrado — v38 único continuity vigente)
**Rev:** 2 (cierre de s39 — infraestructura del smoke desbloqueada parcialmente)

---

## ESTADO DEL SISTEMA

- **DS versión en repo:** v3.23.0 (cert PA-20260712-002 ACTIVE). **NO bumpeado, NO certificado.**
- **HEAD remoto DS:** `1b4c669c` (parent `639e06f5`) — commit del continuity v38. **El fix GAP #1 está en `639e06f5`**, ambos pusheados y verificados por read-back del árbol.
- **HEAD remoto jarp-toolkit:** `514fa026` (parent `7e29023`) — **sin cambios en s39** (notas #34/#43 quedaron desactualizadas, ver BACKLOG).
- **PA-agent:** v1.3.0 (PA-20260527-002 ACTIVE).
- **Working tree:** LIMPIO. Todo s38+s39 commiteado y pusheado.
- **Candidato:** v3.24.0 — falta smoke + cert + bump.

---

## QUÉ SE HIZO EN s39

s38 dejó el GAP #1 fix en working tree sin commit. s39 lo **auditó, corrigió, commiteó y pusheó**.

### Hallazgos de la auditoría (6)

| # | Sev | Hallazgo | Estado |
|---|-----|----------|--------|
| 1 | SERIO | El catálogo forense se inyectaba también en `build_rol_prompt` / `ROLE_AGENT_TEMPLATE` | ✅ FIXED |
| 2 | MOD | `"findings you report above"` — puntero deíctico roto (van abajo) | ✅ FIXED |
| 3 | MOD | Docstrings afirmando "Legal pilot ships alone / 18 not migrated" — FALSO, los 19 están migrados. Idem residuo `pilot` | ✅ FIXED |
| 4 | SERIO | El dominio (y por tanto la inyección) depende del **stem del archivo** | ⚠️ LIMITACIÓN DECLARADA → v3.25.0 |
| 5 | SERIO | `prompts_dir` relativo al CWD + fallback mudo | ✅ OBSERVABLE (warning) — anclaje → v3.25.0 |
| 6 | REG | El fixture que v37 mandaba usar **no existe** | ⚠️ corregido en este doc |

**Hallazgo #1 en detalle (el importante):** el Agente de Rol NO tiene campos `severity`/`findings` en su contrato de salida — un rulebook de severidad es inaplicable ahí. Peor: los dos N1 son **blind peers por diseño**; cebar la capa Rol con la taxonomía del Forense hace que actores simulados razonen como auditores, suprime clashes ROL↔FORENSE reales, y **infla confidence** (misma familia que LW-2 / LW-5, ya arreglados dos veces). Los 212 checks de s38 no lo cazaban: medían extracción, no destino. **La inyección es FORENSE-only, con guard en test.**

**(b) ANOMALY WARNING — añadido en s39:** `load_domain_catalog` ahora separa dos condiciones que colapsaban en el mismo `""` mudo:
- dominio sin entrada en `DOMAIN_PROMPT_FILE` (P01 General) → `""` **silencioso, esperado**;
- dominio que **declara** catálogo pero no lo puede leer / sin contenido en marcadores → `""` + **warning a stderr** nombrando dominio, archivo y qué se perdió.

Razón: el cert de v3.24.0 afirma *"la inyección ocurre"*. Un `""` indistinguible del éxito hace ese claim **inverificable en toda corrida posterior a la certificante** — misma clase de defecto que GAP #1. El fallback se mantiene (el tribunal nunca crashea).

### Estado del código (bytes verificados contra remoto)

| Archivo | Bytes | |
|---|---|---|
| `orchestrator/domain_catalog.py` | 9427 | NUEVO |
| `orchestrator/test_domain_catalog_all19.py` | 6641 | NUEVO — **224 checks** |
| `orchestrator/prompt_engine.py` | 14382 | M |
| `orchestrator/catalogs.py` | 31298 | M (`DOMAIN_PROMPT_FILE`, 19 entradas) |
| `orchestrator/tribunal_transversal.py` | 42323 | M (1 línea `prompts_dir`) |
| `prompts/system_prompt_*.md` | ×19 | M (solo marcadores + header) |
| `dark-strategist-continuity-prompt_v38.md` | 12814 | A (v37 rotado) |

`router.py` (5199) intacto y huérfano. `orchestrator/_livewatch` **NO trackeado** (verificado por árbol).

### Evidencia acumulada (toda medida, ninguna inferida)

- **224/224 offline**: extracción ×19, leak guards 7×19, superficie de inyección ×6, anomaly warning ×6.
- **3 corridas live $0** — LW-5/6/7 intactas bajo el código nuevo, por **tres vectores de colapso independientes**:
  - `DS-5F6CD814` — auth error (sin key) → `INDETERMINATE — TRIBUNAL COLLAPSE`, 0/40, 0.3s.
  - `DS-C7F42901` — connection error (proxy caído) → idem, 0/40, 41s.
  - `DS-EEB1F05B` — **503 upstream** (`NVIDIA_NIM_API_KEY is not set`, con `request_id`) → idem, 0/40, 6.5s.
- **`Domain: Legal` confirmado en runtime real** vía `--document` (`--verbose`), en las 3 corridas.
- **El catálogo Legal SÍ entra en los 5 prompts Forenses**: en `DS-C7F42901` y `DS-EEB1F05B` los prompts se construyeron completos antes del fallo HTTP y **no hubo `[DOMAIN_CATALOG] WARNING`**. Con (b) activo, ese silencio es dato, no suposición.
- Prompt Forense Legal = **11.847 chars** (con LG08/LG09/GEOFENCE **y** `OUTPUT FORMAT (JSON)` coexistiendo). Rol = 1.527 chars, limpio.

---

## LO QUE FALTA — para cerrar v3.24.0

1. **Smoke NVIDIA ($0, NO es evidencia de cert).** Única pregunta técnica abierta del fix: ¿el prompt Forense de 11.847 chars **parsea limpio**, o el bloque compite con el contrato JSON y `_call_agent` cae a `{"raw_output":…, "UNKNOWN"}`? Mirar SOLO: `agents_consulted > 0` y FOR con `verdict != UNKNOWN`. El veredicto de NVIDIA es irrelevante (#34: las corridas libres estresan orquestación, no síntesis).

   **INFRAESTRUCTURA YA RESUELTA en s39 (no rehacer):**
   - `uv 0.11.29` **instalado** en `C:\Users\jrodr\.local\bin` — **NO está en el PATH por defecto**:
     `$env:Path = "C:\Users\jrodr\.local\bin;$env:Path"`
   - Proxy **arranca OK**: `cd free-claude-code` → `uv run fcc-server` (81 packages, ~4s). Uvicorn en `0.0.0.0:8082`, Admin UI `http://127.0.0.1:8082/admin`, `/health` 200.
   - **`MODEL_OPUS` está bien mapeado**: el 503 de `DS-EEB1F05B` lo prueba — el proxy resolvió `claude-opus-4-7` → backend NVIDIA NIM y falló por credencial, no por ruteo.

   **ÚNICO BLOQUEO RESTANTE: `NVIDIA_NIM_API_KEY`.** Sacar key en `https://build.nvidia.com/settings/api-keys` → en `free-claude-code`: `Copy-Item .env.example .env`, poner `NVIDIA_NIM_API_KEY=nvapi-...`, **relanzar el server** (el `.env` se lee al arranque), re-correr DS.

   **Riesgo bajo**: los 133 leak-guards prueban que ningún contrato competidor entró en los bloques; el bloque lleva instrucción explícita de no redefinir formato; el `OUTPUT FORMAT (JSON)` va al final. Y si revienta, `_call_agent` degrada sin crashear.

2. **Cert SUSTANTIVO re-scopeado — CAMINO 3 (decisión de JARP en s39).**

   **PODRÁ afirmar:** 19/19 migrados y extracción correcta · sin fuga de contrato competidor · inyección **Forense-only**, Rol limpio · `--document` resuelve `Legal` en runtime · LG08/LG09/GEOFENCE presentes en el prompt Forense junto al JSON · guardas LW-5/6/7 sobreviven al cambio (3 vectores) · la falla de inyección es **observable**.

   **DEBERÁ declarar como NO evidenciado:**
   - **WATCH live L07 ABIERTO — 4ª sesión (s36→s39).** Que el N1 aplique LG08/LG09 como base-FATAL bajo Opus **no está medido**. Que el fixture salga INVIABLE, tampoco.
   - **Hallazgo #4 como condición del alcance**, no nota al pie: los 19 variants son verdict-binding **condicionado a que el resolver acierte el dominio**, que depende del stem.
   - **Hallazgo #5** como limitación conocida.

3. **Bump v3.24.0:** `bump_stamps.ps1 -OldVersion 3.23.0 -NewVersion 3.24.0 -Apply` + one-shot Python (banners orquestador, CHANGELOG, roadmap rows) + ACTIVE en README/CLAUDE.
4. **Sync canónicos** (posicional, ambos) + **continuity v39** + push.

**Por qué no hubo `sk-ant`:** no hay `.env` en DS, `ANTHROPIC_API_KEY` NOT SET, no hay `config.json`. JARP declaró en s39 que ya no usa `ANTHROPIC_API_KEY` y que usará NVIDIA — **esto contradice la nota #34 vigente y el propio v37**; ver BACKLOG.

---

## BACKLOG ABIERTO

**Gobernanza (resolver antes o durante el cert):**
- **Nota #34 vs. realidad — DECISIÓN PENDIENTE DE JARP.** #34 exige *"real Opus (sk-ant, no proxy) for cert-grade live evidence only"* y dice que las corridas libres **no** evidencian calidad de síntesis. JARP declaró en s39 que usará NVIDIA por costo cero. **Camino 3 evita el choque** (no certifica juicio del N1), pero si en el futuro se quiere certificar comportamiento forense con NVIDIA, **#34 debe editarse formalmente en ambos canónicos** — con la consecuencia de que DS nunca tendría evidencia cert-grade sobre `claude-opus-4-7`, su modelo de producción declarado. Volverá en el próximo cert de superficie forense.
- **Nota #34 / entrada #43 DESACTUALIZADAS — corregir en jarp-toolkit (no se hizo en s39):**
  - Documentan `uv run uvicorn server:app` y `server.py`. **NO EXISTE** — repo real `free-claude-code` **v4.6.4**, layout `src/free_claude_code`, sin `server.py` en la raíz.
  - Entry point real: `fcc-server = free_claude_code.cli.entrypoints:serve`. **Arranque correcto: `uv run fcc-server`.**
  - `requires-python = ">=3.14.0"`, `uv >= 0.11.0`. Instalar uv: `irm https://astral.sh/uv/install.ps1 | iex` → queda en `C:\Users\jrodr\.local\bin` (agregar al PATH manualmente).
  - Requiere `NVIDIA_NIM_API_KEY` en el `.env` del **proxy** (plantilla: `.env.example`).
- **Reglas operativas nuevas para añadir al toolkit:** ver LECCIÓN TRANSVERSAL.

**v3.25.0 (candidatos):**
- **(a) `--document` + `--type`:** hoy el `if/elif` de `main.py` **descarta el documento en silencio** si vienen los 3 flags. No existe la vía documento-real + dominio-pinneado. Bug por derecho propio.
- **(c) `prompts_dir` anclado al repo** (`Path(__file__).parent.parent`), respetando `DS_PROMPTS_DIR`. Una línea. Mata #5 en la raíz.
- **`SubAgentSpawner`:** MISMO bug `prompts_dir` (guardado, nunca leído). 9 N2 permanentes hardcoded en `PERMANENT_SUBAGENTS`.
- **Reporte de colapso parcial:** el transparency report lista `stance=NEUTRAL` / `verdict=UNKNOWN` para agentes que **errorearon**. El veredicto global es honesto (LW-7), pero la capa de reporte sugiere participación inexistente. En un colapso *parcial* podría engañar.
- **`router.py` cleanup:** huérfano + desactualizado (14/20). `DOMAIN_PROMPT_FILE` lo reemplaza (19/20). **No borrar antes** de que v3.24.0 esté certificado.
- **AI Disclaimer BLOCK 7 (RULE LG03):** sin cablear a síntesis/AFO.

**Trading hands-on:** POSTERGADO desde s4 (prioridad #1 en userPreferences). No re-confrontar salvo activación explícita.

---

## FIXTURES REALES (verificado — `orchestrator/_livewatch/`, NO trackeado)

| Archivo | Bytes | Resuelve a |
|---|---|---|
| `ai_governance_companion_minors.txt` | 3539 | **Legal** ✅ |
| `lw2_contract.txt` | 2000 | **Legal** ✅ |
| `cert_brief_v3_22_0.md` | 5436 | — |

⚠️ **v37 mandaba usar `legal_ai_companion_tos.txt` — NO EXISTE.**
El fixture bueno es `ai_governance_companion_minors.txt`: ToS de companion AI con cohorte declarada 13-17 sin verificación de edad ("growth strength"), crisis de autolesión respondida alentando a seguir en la app con ruteo externo **explícitamente evitado por retención**, sin disclosure de IA, positioning "therapy-grade" sin supervisión clínica, sin audit trail, cierra con *"no hay regulación, no adoptamos controles"* — exactamente lo que LG08/LG09 anulan por jurisdiction-independent. **INVIABLE de manual.** Dispara LG08 + LG09.

**Secuencia completa del smoke/e2e (verificada en s39 hasta el 503):**
```powershell
# Ventana 1 — proxy
$env:Path = "C:\Users\jrodr\.local\bin;$env:Path"
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\free-claude-code"
uv run fcc-server          # requiere .env con NVIDIA_NIM_API_KEY

# Ventana 2 — DS, desde la RAÍZ del repo (NO desde orchestrator/)
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent"
$env:ANTHROPIC_API_KEY = "dummy-for-proxy"
$env:ANTHROPIC_BASE_URL = "http://localhost:8082"
python orchestrator\main.py --document orchestrator\_livewatch\ai_governance_companion_minors.txt --tribunal --regime adversarial --verbose
```
`--verbose` imprime el ctx **antes** de la 1ª llamada: si no dice `Domain: Legal`, Ctrl-C y $0 gastados.
⚠️ **Para cualquier e2e cert-grade con `sk-ant`: `Remove-Item Env:ANTHROPIC_BASE_URL` primero** o la evidencia se contamina (#34).

---

## LECCIÓN TRANSVERSAL DE s39 (la más importante)

**Ni el texto canónico ni Claude son fuente. La fuente es el sistema respondiendo.**

Cuatro alucinaciones cazadas en s38/s39, todas del mismo mecanismo — texto escrito de memoria describiendo un estado que nadie verificó:
1. `system_prompt_startup.md` inventado (s38).
2. Docstrings afirmando "18 variants not migrated" (eran 19).
3. Fixture `legal_ai_companion_tos.txt` inexistente (v37).
4. Nota #34 documentando un arranque que `free-claude-code` abandonó hace versiones.

Y **tres predicciones falladas de Claude** en s39: "3 files changed" (eran 23), "el fixture resolverá a General" (resolvió Legal), "el `.env` en `orchestrator/` explica la falla" (no hay `.env`).

**Ninguna la cazó el criterio. Todas las cazó medir**: script anclado con abort, pre-flight $0, `Test-Path`, `Get-ChildItem`, read-back del árbol.

**Reglas operativas nuevas:**
- **`git status --short` SIEMPRE, nunca `git diff --stat`** para verificar pre-commit: `diff` **no muestra untracked** — por ahí pasan one-shots sin borrar y basura de tooling. Misma familia que la lección `Select-String` (s35) y "los commit messages no prueban nada" (s36).
- **`mi-filesystem` puede dejar archivos con el path colapsado como nombre** en la raíz del repo (visto en s39: `ersjrodrOneDrive…`, 3900 bytes, PUA U+F022). Solo visible por `git status --short`.
- **Al investigar basura, leer el contenido ANTES de borrar** (en s39 se borró sin diagnosticar — error).
- **Releer el archivo target inmediatamente antes de construir cualquier ancla**, aun si lo editaste hace 3 turnos (así se cazó el residuo `pilot` de la línea 3).
- **Todo doc canónico envejece en la misma sesión que se escribe.** Este v38 se desactualizó 20 min después de crearse (`uv` pasó de ausente a instalado). Releer y corregir antes de cerrar, no confiar en lo escrito hace un rato.

---

## PROTOCOLO DE INICIO (s40)

**PHASE 0:**
- HEADs remotos reales (`list_commits perPage=3`): DS debería estar en `1b4c669c` si nadie tocó nada; jarp-toolkit en `514fa026`.
- Cert registry: ambos canónicos concuerdan **POSICIONALMENTE** en v3.23.0 / PA-20260712-002 (8 posiciones; lección drift s33/s34 — **NO `Select-String`**).
- `orchestrator/_livewatch` NO trackeado — **por read-back del árbol** (`get_file_contents orchestrator/` → sin `_livewatch`), no por commit msg.
- Working tree: `git status --short`.

**PHASE 1 — decisión, esperar GO.** Candidatos:
- **(b1) cerrar v3.24.0** — key NVIDIA en el `.env` del proxy → smoke → cert camino 3 → bump → sync canónicos → continuity v39 → push. *(`uv` y el proxy ya están listos; ver LO QUE FALTA #1.)*
- **(b2) sync jarp-toolkit** — corregir notas #34/#43 + añadir las reglas operativas nuevas. No depende de ninguna key.
- **(b3) SubAgentSpawner** (mismo bug `prompts_dir`, v3.25.0).
- **(b4) (a) + (c)** — CLI y `prompts_dir` anclado.
- **(b5) `router.py` cleanup** (solo post-cert de v3.24.0).

**STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real. **Verificar contra fuente real antes de dar por bueno — medir, no inferir.** Trabajar en silencio, priorizar tokens. Español para conversación, inglés estricto para código/comentarios (prefijo `//--- `).
