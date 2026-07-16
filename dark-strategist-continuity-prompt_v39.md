# Dark Strategist — Continuity Prompt v39

**Sesión origen:** 40 (Claude for Windows) · **Fecha:** 16/07/2026
**Reemplaza:** v38 rev 2 (borrar — v39 único continuity vigente)

---

## ESTADO DEL SISTEMA

- **DS versión en repo:** v3.23.0 (cert PA-20260712-002 ACTIVE). **NO bumpeado, NO certificado.**
- **HEAD remoto DS:** `c05f0a74` (parent `1b4c669c`). Fix GAP #1 en `639e06f5`. **s40 no commiteó nada.**
- **HEAD remoto jarp-toolkit:** `514fa026` — sin cambios desde s37. Notas #34/#43 DESACTUALIZADAS.
- **PA-agent:** v1.3.0 (PA-20260527-002 ACTIVE) — ⚠️ **vence 25/08/2026**: el auditor caduca antes que el auditado.
- **Working tree:** coherente por inspección de árbol (todo lo local extra está cubierto por `.gitignore`). **No verificado con `git status --short`** — Claude no tiene shell en Windows. Correr en PHASE 0.
- **Candidato:** v3.24.0 — **BLOQUEADO por LW-8** (ver abajo). Falta: LW-8 + fix #5 → cert → bump.

**PHASE 0 verificada en s40:** HEADs reales por `list_commits perPage=3` ✅ · concordancia POSICIONAL 8/8 en ambos canónicos a v3.23.0/PA-20260712-002 ✅ · `orchestrator/_livewatch` NO trackeado **por read-back del árbol** ✅ · bytes remotos = tabla v38 ✅.

---

## 🔴 LW-8 — EL HALLAZGO CENTRAL DE s40. Bloquea el cert.

**El dominio se resuelve por el NOMBRE DEL ARCHIVO, nunca por el contenido. Y el fallo es silencioso.**

### Cadena medida (fuente leída, no inferida)

`orchestrator/context_builder.py::_resolve_domain` (líneas 111-159), textual:

```python
domain = DOMAIN_MAP.get(doc_type.lower())
if domain:
    return domain
# ...normaliza separadores y tokeniza el STEM del archivo, busca keywords...
return "General"        # ← fallback final
```

`catalogs.py`:
- `DOMAIN_MAP` — 83 claves. **Las 12 que resuelven Legal:** `contract · alquiler · legal · compliance · nda · msa · gdpr · dsar · trademark · employment · litigation · ai governance`
- `DOMAIN_PROMPT_FILE` — 19 dominios con catálogo. Comentario final textual: `# "General": no dedicated catalog file (system_prompt.md not migrated).`

**Por qué la corrida DS-CF1CEFD1 resolvió Legal:** el stem `ai_governance_companion_minors` normaliza a `"ai governance companion minors"`; la clave compuesta `"ai governance"` matchea como frase → Legal. **Por el nombre del archivo. Nada más.**

### El vector fail-open

| Paso | `mindmate_tos.txt` (mismo documento) |
|---|---|
| tokens del stem | `{mindmate, tos}` |
| match en las 12 claves Legal | **ninguno** |
| `_resolve_domain` | **`return "General"`** |
| `DOMAIN_PROMPT_FILE["General"]` | no existe |
| `load_domain_catalog` | **`""` — SILENCIOSO** (diseñado así en s39: General no declara catálogo → `""` "esperado", el warning NO dispara) |
| LG08 / LG09 / L07 | **nunca se inyectan** |

El mismo ToS —menores sin verificación de edad, crisis de autolesión con ruteo externo evitado por retención— auditado **sin las compuertas auto-FATAL jurisdiction-independent**. La aplicación cae a "el juicio genérico del modelo base" — **exactamente el defecto que v3.24.0 existía para eliminar**.

### Clasificación

**s39 lo etiquetó SERIOUS ("limitación declarada"). Con la cadena medida es CRITICAL.**
Familia **LW-5 / LW-6 / LW-7** — fail-open en el camino del veredicto. Las tres se arreglaron; **ninguna se declaró**. LW-7 fue *"un tribunal colapsado nunca emite all-clear"*. LW-8 es su gemelo: **un documento Legal mal nombrado nunca debe auditarse sin LG08/LG09.**

### Por qué el cert NO pudo emitirse (decisión de s40)

`prompt-architect-agent/docs/certification_protocol.md`, textual:
> | CRITICAL findings | **0 — absolute** |
> | SERIOUS findings | **0 — absolute** |
> *"No exceptions. No partial certifications. **No 'certified with conditions.'**"*

Camino 3 proponía declarar #4 como *"condición del alcance"* y #5 como *"limitación conocida"*. **Eso es certified-with-conditions**, prohibido por el protocolo palabra por palabra. Peor: el cert afirmaría *"los 19 variants son verdict-binding"* mientras su inyección **depende de cómo el usuario nombre el archivo** — la misma clase de fallo (certificar como verdict-binding lo que el runtime no garantiza) que motivó todo v3.24.0.

**JARP eligió (A): subir LW-8 + fix #5 a v3.24.0 y certificar limpio.** Camino 3 queda MUERTO.

---

## DISEÑO LW-8 — CONGELADO, CON GO DE JARP. Implementar en s41.

### Fix #5 — una línea

`orchestrator/main.py` línea 55:
```python
"prompts_dir": os.getenv("DS_PROMPTS_DIR", "./prompts"),                      # ANTES
"prompts_dir": os.getenv("DS_PROMPTS_DIR",
                str(Path(__file__).resolve().parent.parent / "prompts")),     # DESPUÉS
```
Mata #5 en la raíz. El CWD deja de importar. `DS_PROMPTS_DIR` sigue mandando si está.

### Fix #4 = LW-8 — escalón de contenido, monotónico

**NO rehacer `_resolve_domain`.** LW-1 ya lo certificó (anti substring-bleed, order-invariant, most-specific-first). Tocarlo revienta esa garantía y agranda el delta.

```python
#--- Stem resolution first (LW-1 contract, unchanged, certified).
domain = self._resolve_domain(doc_type, subscenario)

#--- LW-8 fail-closed: the stem is weaker evidence than the document itself.
#--- A catalog-bearing domain reached only via filename means a Legal document
#--- named `mindmate_tos.txt` is audited WITHOUT LG08/LG09 -- silently.
#--- Content fallback fires ONLY on the General sink: never overrides a
#--- successful stem match, so existing routing is byte-identical.
if domain == "General":
    domain = self._resolve_domain_from_content(document_text) or "General"

#--- Last line: still General but the document carries catalog-domain signals
#--- -> the omission is NOT silent. Recorded in RuntimeContext + transparency.
```

**Tres propiedades que lo hacen certificable:**
1. **Monotónico.** Solo actúa sobre el sumidero `General`. Ninguna resolución existente cambia → LW-1 byte-identical → cero regresión posible.
2. **Fail-closed observable.** Si tras el contenido sigue `General` **y** el documento lleva señales L07 (`minor`, `age verification`, `parental consent`, `mental health`, `emotional dependency`, `crisis protocol`, `self-harm`, `companion AI`, `chatbot safety`), la omisión se registra en el transparency report. Deja de ser invisible.
3. **Evidencia mejor, no adivinanza.** No infiere el veredicto: usa el documento para resolver el dominio. Estrictamente superior al stem.

**NO forzar INDETERMINATE.** LW-7 podía: su disparador era binario (`agents_consulted==0`). LW-8 es heurístico — retener el veredicto porque un ToS de café menciona "minor" sería fail-closed mal aplicado. La compuerta correcta es **observabilidad + ruteo por contenido**, no bloqueo.

### Delta estimado

| Archivo | Cambio |
|---|---|
| `main.py` | 1 línea (#5) |
| `context_builder.py` | `_resolve_domain_from_content` + 3 líneas de gate |
| `catalogs.py` | tabla de señales por dominio-con-catálogo |
| `schema.py` / transparency | campo de omisión declarada |
| tests | resolución por contenido ×19 · **guard de monotonía (el stem SIEMPRE gana)** · gate de señales |

**SUSTANTIVO, no confirmatorio.** Cambia qué catálogo se inyecta → toca el veredicto. 7-axis JARP DEEP.

### ⚠️ Medición pendiente antes de anclar
Las señales auto-detect L07 **hay que releerlas de `prompts/system_prompt_legal.md`**, no del CHANGELOG v3.22.0 ni de este doc. Lección del residuo `pilot` (s39): releer el target inmediatamente antes de construir cualquier ancla.

---

## ✅ SMOKE PASS — DS-CF1CEFD1. La pregunta de 4 sesiones, contestada.

```
Tribunal: AUTO (10 agents) | Budget: 11/40 (27.5%) | n1: 5, rol: 5, synthesis: 1
FOR-01..05 → verdict = INVIABLE      ← NO UNKNOWN
Duration: 324.8s | Domain: Legal | Backend: nvidia/nemotron-3-super-120b-a12b
```

**El prompt Forense de 11.847 chars parsea limpio.** El bloque del catálogo **no compite** con `OUTPUT FORMAT (JSON)`. El riesgo declarado en v38 era **infundado** — ahora medido.

**Y las reglas no solo entran: se aplican.** Los agentes las citan por ID:
- *"Under **RULE LG08**, consumer-facing AI reachable by minors without documented age-gating/parental consent is automatic FATAL"*
- *"**RULE LG09** mandates automatic FATAL for user-facing AI lacking a crisis-escalation protocol for self-harm/suicide signals"*
- También `RULE L07` y `RULE L04` por nombre.

Fixture salió **INVIABLE**, como estaba previsto. 19 FATAL / 24 SERIOUS / MULTI-AGENT CONFIRMED 3.

⚠️ **WATCH live L07 NO se cierra — 5ª sesión abierto.** Fue **Nemotron, no Opus**. #34: las corridas libres estresan orquestación, no síntesis. Guardar la salida completa de DS-CF1CEFD1: es la evidencia del cert.

---

## 3 HALLAZGOS DEL E2E — solo visibles con una corrida sana

**(1) 🔴 SubAgentSpawner decorativo.** `[SPAWNER] FOR-0x → spawning UNIT-INQUISITOR/UNIT-COMPLIANCE` ×10, pero `Breakdown: {'n2': 0}` — **cero llamadas**. El transparency report **lista UNIT-COMPLIANCE y UNIT-INQUISITOR como si hubieran auditado**. Un lector concluye que hubo capa N2. No la hubo. Misma familia que LW-7 y que "reporte de colapso parcial": **la capa de reporte afirma participación inexistente.** Esto es (b3), ahora con evidencia viva.

**(2) 🔴 La síntesis determinista no deduplica.** 19 FATAL reportados, **7 únicos**: IP ownership ×5, LG08 age-verification ×4, LG09 crisis ×4, unlimited liability ×2, therapy-grade ×2, DPA/GDPR ×1, invalid consent ×1. Y `Confirmed by 2+ agents: 3` **debería ser 5** — el matcher de corroboración falla con variantes de redacción (*"Missing IP ownership clause"* vs *"No IP ownership clause"*). **Subcuenta corroboración e infla el conteo FATAL**; ambos son números de cara al producto. Verdict-safe (`>=1 FATAL → INVIABLE` igual), pero solo ocurre en el camino de fallback — y LW-5/6/7 enseñaron que **los caminos de fallback importan**.

**(3) 🟠 La síntesis truncó el JSON.** `Synthesis failed: Unterminated string starting at: line 102 column 22 (char 8245)` → cayó al fallback determinista sin crashear, y el veredicto lo declara honestamente. Degradación correcta. **Pero no hay reparación ni reintento** en el camino de síntesis. Con Opus y 43 findings el mismo truncamiento es plausible. Culpa de Nemotron (síntesis, fuera de #34), pero el **hueco de robustez es de DS**.

---

## 🔴 HALLAZGO DS PARA v3.25.0 — `content[0].text` sin filtro de tipo

`tribunal_transversal.py`:
```
L601  _call_agent   →  text = response.content[0].text.strip()   ← FUERA del try
L261  _synthesize   →  text = response.content[0].text.strip()   ← dentro del try
```
Cero filtrado por tipo de bloque. **Contra `sk-ant` Opus real no hay bug**: la API de Anthropic nunca devuelve bloques `thinking` salvo que los pidas, y DS no los pide (manda solo `model`/`max_tokens`/`system`/`messages`).

**Contra backends proxeados — que es lo que la #34 ordena para TODAS las corridas no-cert — es un vector de colapso total latente.** La premisa de #34 ("rutea DS por el backend que sea") solo se sostiene si DS tolera las formas que esos backends producen. Hoy no las tolera. Fix: iterar bloques y tomar el primero con `type == "text"`. ~3 líneas, 2 sitios. **NO antes del cert de v3.24.0** — es superficie bajo auditoría.

---

## 🔧 INFRAESTRUCTURA — 8 HALLAZGOS. Todo esto va a jarp-toolkit (b2).

**El proxy y `uv` funcionan. La configuración de v38 estaba mal en 4 puntos.**

| # | Hallazgo | Estado |
|---|---|---|
| 1 | **`MODEL_OPUS` está VACÍO.** v38 dice *"está bien mapeado, el 503 lo prueba"* — **FALSO**. El ruteo va por el fallback `MODEL`. **4 confirmaciones independientes:** `.env` del repo · `config/admin/manifest.py` · `~/.fcc/.env` · la propia UI (*"Select None to use the Default Model for Opus requests"*) | v38 corregido |
| 2 | **`ANTHROPIC_AUTH_TOKEN` default = `freecc`**, no `dummy-for-proxy` | v38 corregido |
| 3 | **Precedencia `.env`:** `config/env_files.py::settings_env_files()` devuelve `[repo_env_path(), managed_env_path()]` low→high + `FCC_ENV_FILE` (máxima). **`~/.fcc/.env` PISA al `.env` del repo.** La Admin UI escribe en `~/.fcc/.env`. **El `.env` del repo está muerto** (sombreado por completo: `env_file_value` trata `KEY=` como *definida*, devuelve `""`, no `None`) | NUEVO |
| 4 | **`repo_env_path()` devuelve `Path(".env")` — relativo al CWD.** Misma familia que el hallazgo #5 de DS. Otro repo, mismo defecto | NUEVO |
| 5 | **`uv run` exige CWD = raíz del proyecto.** Mordió 2 veces. No está en #43 | NUEVO |
| 6 | **`uv` + OneDrive falla DESTRUCTIVAMENTE e INTERMITENTE.** `Acceso denegado (os error 5)` al borrar `.dist-info\licenses` → deja el venv a medio desinstalar → `package_version()` vacío → `AssertionError: A version must be provided for OpenAPI`. **Parece un crash de FCC y no lo es.** Peor: `uv run` solo reconstruye a veces → funcionó 2 veces y a la 3ª rompió | NUEVO |
| 7 | **Los campos secretos de la Admin UI son write-only / replace-only. NO se pueden vaciar desde la UI.** Placeholder *"Configured - enter a new value to replace"*. Para poner cualquier secreto en blanco hay que **editar `~/.fcc/.env` a mano** — el *"Edit in the server UI when possible"* del propio archivo tiene ese agujero | NUEVO |
| 8 | **La sección `Runtime` de la Admin UI está en una tarjeta aparte al FONDO de Providers** — no detrás de `Show advanced` (eso solo despliega los `*_PROXY`) | NUEVO |

### ✅ CONFIGURACIÓN QUE FUNCIONA — verificada en `~/.fcc/.env`

| Clave | Valor |
|---|---|
| `NVIDIA_NIM_API_KEY` | **SET** (cuenta NVIDIA Cloud org `JARP`, key `dark-strategist`, 12 meses) |
| `ENABLE_MODEL_THINKING` | **`false`** ← confound eliminado, ver abajo |
| `ANTHROPIC_AUTH_TOKEN` | **vacío** ← indispensable, ver abajo |
| `MODEL` | `nvidia_nim/nvidia/nemotron-3-super-120b-a12b` 📌 **pin de backend del cert** |
| `MODEL_OPUS` | vacío → fallback |

🔴 **`ANTHROPIC_AUTH_TOKEN` DEBE quedar vacío** o DS recibe `401 {'detail': 'Missing proxy authentication token'}` en los 10 agentes.
**Mecanismo trazado y probado:** el proxy valida `Authorization: Bearer`, **ignora `x-api-key`** (que es lo que manda el SDK). Y **no se puede arreglar desde el cliente**: SDK `anthropic` 0.116.0 —
```python
has_explicit_credential = (api_key is not None or auth_token is not None or ...)
if not has_explicit_credential:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    auth_token = os.environ.get("ANTHROPIC_AUTH_TOKEN")
```
`main.py:51` hace `os.getenv("ANTHROPIC_API_KEY", "")` → default **`""`**, y `"" is not None` → `has_explicit_credential=True` → **el SDK jamás lee `ANTHROPIC_AUTH_TOKEN` del entorno**. Probado empíricamente: `Anthropic(api_key='')` + env var puesta → `auth_headers: {'X-Api-Key': ''}`, sin `Authorization`. (`base_url` **sí** se lee siempre — rama aparte, sin condición. Por eso `ANTHROPIC_BASE_URL` funciona.)
⚠️ **Seguridad:** `HOST=0.0.0.0` → `/v1/messages` escucha en toda la LAN. El token vacío deja la key de NVIDIA usable por cualquiera en la red. **Restaurar `freecc` al cerrar sesión de trabajo.**

🔴 **`ENABLE_MODEL_THINKING=false` es obligatorio.** El proxy tiene `ThinkTagParser` (`core/anthropic/thinking.py`) que parte `<think>…</think>` en chunks `ContentType.THINKING`; Nemotron es un modelo de razonamiento; el `.env` documenta la flag como *"provider reasoning requests **and Claude thinking blocks**"*. Combinado con `content[0].text` sin filtro → **colapso total disfrazado de infraestructura**. Con `false` el confound desaparece. *(El eslabón "el bloque thinking sale en posición 0" quedó SIN medir — pero el toggle es gratis y reversible, e higiene experimental exige eliminar el confound.)*

### 🚀 SECUENCIA COMPLETA VERIFICADA — copiar tal cual

```powershell
# ── Ventana A — proxy. Queda ocupada. NO tocar.
$env:UV_PROJECT_ENVIRONMENT = "C:\Users\jrodr\.venvs\free-claude-code"   # OBLIGATORIO: fuera de OneDrive
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\free-claude-code"        # OBLIGATORIO: uv run resuelve contra el CWD
uv run fcc-server
# esperar: Uvicorn running on http://0.0.0.0:8082

# ── Ventana B — DS
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent"
$env:ANTHROPIC_API_KEY  = "freecc"
$env:ANTHROPIC_BASE_URL = "http://127.0.0.1:8082"      # 127.0.0.1, NO localhost
curl.exe -s -o NUL -w "health -> %{http_code}`n" http://127.0.0.1:8082/health
#  ⚠️ si NO dice 200 → PARAR. No correr DS.
python orchestrator\main.py --document orchestrator\_livewatch\ai_governance_companion_minors.txt --tribunal --regime adversarial --verbose
```

- **`uv` ya está en el PATH permanente.** v38 decía agregarlo a mano cada ventana — envejecido.
- **`UV_PROJECT_ENVIRONMENT` vive solo en su ventana.** Reiniciar el server en OTRA ventana reconstruye el venv dentro de OneDrive → vuelve el hallazgo #6. **Hacerlo permanente en s41.**
- **`127.0.0.1` en vez de `localhost`:** no era la causa de nada, pero medido ahorra la mitad del tiempo por el doble round-trip IPv6 (40.9s → 22.6s en fallo). Dato gratis.
- **`Ctrl+C` es una COMBINACIÓN DE TECLAS.** No se escribe. (Claude la puso dentro de un bloque de comandos en s40 → una hora perdida.)
- **Para e2e cert-grade con `sk-ant`: `Remove-Item Env:ANTHROPIC_BASE_URL` primero** o la evidencia se contamina (#34).

---

## LO QUE FALTA — para cerrar v3.24.0

1. **Implementar LW-8 + fix #5** (diseño arriba, GO dado). Releer `system_prompt_legal.md` para las señales L07 antes de anclar.
2. **Tests:** resolución por contenido ×19 · **guard de monotonía** (el stem siempre gana — prueba de no-regresión de LW-1) · gate de señales. Sumar a los 224 offline existentes.
3. **Re-correr el e2e** con el fixture renombrado (`mindmate_tos.txt`) → debe resolver Legal **por contenido** y salir INVIABLE. **Esa es la prueba de LW-8.** $0 con NVIDIA.
4. **Cert SUSTANTIVO 7-axis JARP DEEP** — RULE 08 self-audit L0 primero (PA-20260716-001 o el correlativo del día), luego el cert (PA-YYYYMMDD-002). **0 CRITICAL + 0 SERIOUS absoluto, sin condiciones.**
5. **Bump v3.24.0:** `bump_stamps.ps1 -OldVersion 3.23.0 -NewVersion 3.24.0 -Apply` + one-shot Python (banners orquestador, CHANGELOG, roadmap rows) + ACTIVE en README/CLAUDE.
6. **Sync canónicos** (posicional, ambos) + **continuity v40** + push.

### Lo que el cert PODRÁ afirmar (ya medido)
19/19 migrados y extracción correcta · sin fuga de contrato competidor · inyección **Forense-only**, Rol limpio · `Domain: Legal` en runtime (**5 corridas**) · LG08/LG09/GEOFENCE coexisten con el JSON en el prompt Forense · **el prompt de 11.847 chars parsea limpio (5/5 FOR, JSON válido, DS-CF1CEFD1)** · **las reglas se aplican como base-FATAL, citadas por ID** · guardas LW-5/6/7 sobreviven (**3 vectores de colapso + 1 corrida sana**) · la falla de inyección es observable · **+ LW-8: el dominio resuelve por contenido cuando el stem falla, y la omisión nunca es silenciosa**.

### Lo que DEBERÁ declarar como NO evidenciado
- **WATCH live L07 ABIERTO — 5ª sesión (s36→s40).** Que el N1 aplique LG08/LG09 como base-FATAL **bajo Opus** no está medido. Nemotron ≠ Opus (#34).
- **N2 decorativo** (`n2: 0`) y **fallback sin dedup** — fuera del delta, declarados, → v3.25.0.

---

## BACKLOG ABIERTO

**Gobernanza:**
- **Nota #34 vs. realidad — DECISIÓN PENDIENTE DE JARP.** #34 exige *"real Opus (sk-ant, no proxy) for cert-grade live evidence only"*. JARP declaró en s39 que usará NVIDIA por costo cero. **s40 no forzó el choque** (el cert no certifica juicio del N1), pero si se quiere certificar comportamiento forense con NVIDIA, **#34 debe editarse formalmente en ambos canónicos** — con la consecuencia de que DS nunca tendría evidencia cert-grade sobre `claude-opus-4-7`, su modelo de producción declarado.
- **Notas #34/#43 DESACTUALIZADAS — corregir en jarp-toolkit (b2):** documentan `uv run uvicorn server:app` y `server.py`, que **NO EXISTEN**. Repo real `free-claude-code` **v4.6.4**, layout `src/free_claude_code`, entry point `fcc-server = free_claude_code.cli.entrypoints:serve`, arranque correcto `uv run fcc-server`. `requires-python >=3.14.0`, `uv >= 0.11.0` (instalado: 0.11.29). **Ya no son 11 backends: ~25.** Config vía Admin UI → `~/.fcc/.env`. **+ los 8 hallazgos de infra de arriba + las reglas operativas nuevas.**
- **PA-agent PA-20260527-002 vence 25/08/2026** — el auditor caduca antes que el auditado.

**v3.25.0 (candidatos):**
- **`content[0].text` sin filtro de tipo** ×2 sitios — vector de colapso latente contra backends proxeados. ~3 líneas.
- **SubAgentSpawner:** N2 decorativo (10 spawns, 0 llamadas) + el reporte afirma participación inexistente. Mismo bug `prompts_dir`. 9 N2 hardcoded en `PERMANENT_SUBAGENTS`.
- **Dedup en `_deterministic_synthesis`** + matcher de corroboración tolerante a variantes de redacción.
- **Reparación/reintento en el camino de síntesis** (truncamiento JSON).
- **`--document` + `--type`:** el `if/elif` de `main.py` **descarta el documento en silencio** si vienen los 3 flags.
- **Reporte de colapso parcial:** lista `stance=NEUTRAL`/`verdict=UNKNOWN` para agentes que errorearon.
- **`router.py` cleanup:** huérfano (5199 bytes) + desactualizado (14/20). **No borrar antes** de que v3.24.0 esté certificado.
- **AI Disclaimer BLOCK 7 (RULE LG03):** sin cablear a síntesis/AFO.
- **`UV_PROJECT_ENVIRONMENT` permanente** (setx o perfil de PowerShell).

**Trading hands-on:** POSTERGADO desde s4 — **37 sesiones (4–40)**, prioridad #1 en userPreferences. **No re-confrontar** salvo activación explícita. s40 no lo eligió → prioridad real ≠ escrita.

---

## FIXTURES REALES (`orchestrator/_livewatch/`, NO trackeado, cubierto por `.gitignore`)

| Archivo | Bytes | Resuelve a |
|---|---|---|
| `ai_governance_companion_minors.txt` | 3539 | **Legal** ✅ — **pero por el stem `ai_governance`, no por el contenido** |
| `lw2_contract.txt` | 2000 | **Legal** ✅ (stem `contract`) |
| `cert_brief_v3_22_0.md` | 5436 | — |

⚠️ **Existe además `_livewatch/` en la RAÍZ del repo** (`lw5_collapse.txt`, `signals_acme.txt`, `strategy_acme_board_proposal.txt`) — v38 no lo menciona. Ambos ignorados por `.gitignore` (`_livewatch/` matchea a cualquier nivel). Inocuo, pero documentado.

**Para probar LW-8 en s41:** copiar `ai_governance_companion_minors.txt` → **`mindmate_tos.txt`**. Pre-LW-8 debe resolver `General`; post-LW-8 debe resolver `Legal` **por contenido** y salir INVIABLE.

---

## LECCIÓN TRANSVERSAL DE s40

**La verificación de infraestructura viva CADUCA EN MINUTOS.**

s40 midió `Uvicorn running` + Admin UI `CONFIGURED` y actuó sobre el **recuerdo** de esa medición cinco minutos después. El server ya estaba muerto. Dos corridas vacías.

Es la hermana de *"todo doc canónico envejece en la misma sesión que se escribe"* (s39) — solo que aquí lo que envejeció fue **un dato propio, medido, correcto en su momento**.

**Regla nueva: la verificación de infra viva se hace INMEDIATAMENTE ANTES de la operación que la consume.** De ahí el `curl /health` pegado al comando de DS, sin pausa entre medio, y el **PARAR si no da 200**.

**Otras reglas nuevas de s40:**
- **Nunca escribir combinaciones de teclas dentro de bloques de comandos.** `Ctrl+C` en un bloque ` ```powershell ` se escribe como texto y PowerShell lo rechaza. Costó una hora y dos corridas.
- **Los `000` de curl no son "el servidor responde mal": son "no hay servidor".** Distinguir `000` (sin conexión) de `401`/`503` (hay alguien al otro lado) ahorra horas de diagnóstico en la capa equivocada.
- **Medir mata hipótesis elegantes.** La hipótesis IPv6 era coherente, encajaba con los tiempos, y era **falsa** (`127.0.0.1 -> 000` también). El diagnóstico $0 la mató en 30 segundos. Sin él, "cambia a 127.0.0.1 y listo" habría fallado igual y el fallo se habría atribuido al prompt.
- **Anti-rubber-stamping funcionó.** s40 llegó al cert con GO y **lo bloqueó** al medir #4 contra la fuente y encontrar que camino 3 violaba el propio `certification_protocol.md`. Mismo patrón que s36 (GEOFENCE). **El GO de JARP no exime de auditar.**
- **La cadena de escalones de infra es real y hay que subirla en orden:** conexión → auth → parseo. Cada una enmascara a la siguiente. Saltarse una produce diagnósticos que culpan a la capa equivocada.

---

## PROTOCOLO DE INICIO (s41)

**PHASE 0:**
- HEADs remotos reales (`list_commits perPage=3`): DS debería estar en `c05f0a74`, jarp-toolkit en `514fa026` (s40 no commiteó nada).
- Cert registry: ambos canónicos concuerdan **POSICIONALMENTE** en v3.23.0 / PA-20260712-002 (8 posiciones — **NO `Select-String`**, lección drift s33/s34).
- `orchestrator/_livewatch` NO trackeado — **por read-back del árbol** (`get_file_contents orchestrator/` → sin `_livewatch`), no por commit msg.
- Working tree: **`git status --short`** (NUNCA `git diff --stat` — no muestra untracked, lección s39). **Claude no tiene shell en Windows: pedírselo a JARP.**

**PHASE 1 — decisión, esperar GO.** Candidatos:
- **(b1) LW-8 + fix #5 → tests → e2e con `mindmate_tos.txt` → cert 7-axis → bump v3.24.0 → sync canónicos → continuity v40 → push.** ← **el camino elegido por JARP en s40. Diseño congelado arriba.**
- **(b2) sync jarp-toolkit** — notas #34/#43 + los 8 hallazgos de infra + las reglas operativas nuevas. **No depende de ninguna key ni server.** Es el pendiente más grande y más barato.
- **(b3) SubAgentSpawner** (N2 decorativo, evidencia viva en DS-CF1CEFD1).
- **(b4) `content[0].text` sin filtro de tipo** (v3.25.0, post-cert).
- **(b5) `router.py` cleanup** (solo post-cert de v3.24.0).

**STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real. **VERIFICAR CONTRA FUENTE REAL ANTES DE DAR POR BUENO — MEDIR, NO INFERIR.** Ni el texto canónico ni Claude son fuente: la fuente es el sistema respondiendo. Trabajar en silencio, priorizar tokens. Español para conversación, inglés estricto para código/comentarios (prefijo `//--- `).
