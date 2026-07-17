# Dark Strategist — Continuity Prompt v40

**Sesión origen:** 41 (Claude for Windows) · **Fecha:** 16/07/2026
**Reemplaza:** v39 (borrar — v40 único continuity vigente)

---

## ESTADO DEL SISTEMA

- **DS versión en repo:** v3.23.0 (cert PA-20260712-002 ACTIVE). **NO bumpeado, NO certificado.**
- **HEAD remoto DS al abrir s41:** `e02963d5` (parent `c05f0a74`) — **medido**, v39 se declaraba en `c05f0a74` y envejeció en el commit que la rotó. **s41 commitea el delta de código de v3.24.0 + rotación a v40.**
- **HEAD remoto jarp-toolkit:** `514fa026` — sin cambios desde s37. Notas #34/#43 DESACTUALIZADAS.
- **PA-agent:** v1.3.0 (PA-20260527-002 ACTIVE) — ⚠️ **vence 25/08/2026** (40 días). El auditor caduca antes que el auditado.
- **Working tree al abrir s41:** limpio en ambos repos por `git status --short` ✅ (local == remoto en jarp-toolkit → la concordancia posicional leída en los locales es válida sobre el remoto).
- **Candidato v3.24.0: DELTA DE CÓDIGO COMPLETO Y SANO. Falta e2e sano → cert → bump.**

**PHASE 0 verificada en s41:** HEADs reales por `list_commits perPage=3` ✅ · concordancia POSICIONAL **8/8** en ambos canónicos a v3.23.0/PA-20260712-002 ✅ · `orchestrator/_livewatch` NO trackeado por read-back del árbol (29 entradas, único `type:dir` = `ssm`) **y** por `git status --short` ✅ · bytes remotos = tabla v39 (`router.py` 5199, `context_builder.py` 8607, `catalogs.py` 31298) ✅.

---

## ✅ LW-8 — RESUELTO. El diseño congelado de v39 NO COMPILABA.

### El GO no exime de auditar (3ª vez: s36 GEOFENCE, s40 LW-8, s41 esto)

v39 congeló: `domain = self._resolve_domain_from_content(document_text)` dentro de `context_builder`.
**Medido contra fuente:** `ContextBuilder.build(case: dict)` — el `case` contiene `type`, `subscenario`, `objective`, `regime`, `run_ssm`, `ssm_scale`, `corpus_paths`, `signals_paths`. **Cero texto de documento.** `document_text` no existe en ese scope → `NameError`. El toolkit (#30, v3.8.0: *«ContextBuilder es document-free»*) **no estaba envejecido: decía la verdad**.

### La causa raíz estaba en `main.py`, no en el resolver

```python
document = ingest_document(str(doc_path))    # ← el documento YA está en memoria
case = {"type": "general", "subscenario": doc_path.stem, ...}   # ← 🔴 el nombre, como "evidencia"
ctx = builder.build(case)                    # ← 3 líneas después
```
`_resolve_domain` **no tenía defecto**: hacía exactamente lo que LW-1 certificó. Se le entregaba basura. **LW-8 era un defecto de síntesis del caso en el entry point.** Arreglarlo en `context_builder` habría parcheado el síntoma aguas abajo Y roto el contrato document-free certificado.

### Diseño aprobado (A) — `domain_hint`

`main.py` (dueño de la ingesta) resuelve por contenido y pasa un **string ya resuelto**; `ContextBuilder` sigue sin ver texto jamás:
```python
if domain == "General":
    domain = case.get("domain_hint") or "General"
```
`_resolve_domain` **byte-identical**. Monotónico: solo el sumidero `General`.

### Alcance aprobado (1) — C1 y C2 separadas

| Claim | Alcance | Mecanismo |
|---|---|---|
| **C2 — la omisión NUNCA es silenciosa** | **universal, 20/20 dominios** | `RuntimeContext.domain_resolution` + `describe_domain_resolution()` → transparency report. Determinista, post-verdicto, report-only, NON-BINDING. **Precedente certificado limpio: v3.15.0 `_attribute_signal_provenance`** |
| **C1 — el dominio resuelve por contenido** | **Legal**, tabla extensible | `DOMAIN_CONTENT_SIGNALS` + scoring por frases distintas, umbral 3, margen 2 |

**Por qué el recorte NO es camino 3:** LW-8 es CRITICAL **porque** existen LG08/LG09 (auto-FATAL, jurisdiction-independent, daño irreversible). **Viven en Legal/L07.** Se arregla el ruteo donde está el daño; la procedencia se declara en todos lados. Ningún dominio queda peor que hoy, ninguno queda mudo. Agregar un dominio a la tabla es **cambio de contenido, sin cambio de código**.

### 🔴 Dos hipótesis elegantes que la medición mató

**(1) v39 tenía la lista L07 MAL.** Fuente textual (`system_prompt_legal.md`, fila L07): **13 señales** — `AI governance, AI assessment, algorithmic, AI vendor, minors, age verification, parental consent, mental health, emotional dependency, crisis protocol, self-harm, companion AI, chatbot safety`. v39 declaró 9 y escribió **`minor`** singular. `JARP_TOOLKIT` #16 registra *«signal minor->minors»* como cambio deliberado de v3.22.0. **v39 lo revirtió de memoria.** Anclar contra v39 metía una regresión sobre un cambio certificado. Test **F2** lo clava.

**(2) Reusar `DOMAIN_MAP` contra el documento: REFUTADO.** Era la opción de costo cero. `DOMAIN_MAP` matchea por token-o-prefijo e incluye `health`→Medical, `property`→Real Estate, `content`→Media, `security`→Cybersecurity, `process`→Operations, `people`→HR. Cualquier ToS de IA dice «mental **health**», «intellectual **property**», «user **content**», «data **security**». Resolvería **Medical/Media/Real Estate** — inyectando el catálogo **equivocado, en silencio, con cara de éxito**. **Peor que General.** `DOMAIN_MAP` es vocabulario de *stem* (una cadena = un tema), no de prosa. Tests **C1/C2** lo dejan clavado como regresión.

**(3) La tabla certificada NO es usable verbatim.** Sus 12 filas tienen `policy`, `security`, `title`, `board`, `consent`, `debt`, `vendor`, `subscription`, `saas`, `patent`, `termination`, `classification`. Adentro del prompt son válidas (Legal ya establecido, el modelo elige *sub-área*). Como ruteo de **dominio** reproducen el mismo falso-positivo. → `DOMAIN_CONTENT_SIGNALS["Legal"]` es **subconjunto estricto** de la fuente certificada, con las genéricas excluidas y la exclusión documentada en el código. **Quitar no inventa; agregar sí.** Test **C3** lo clava.

---

## 📐 DELTA DE CÓDIGO v3.24.0 — COMPLETO. 7 archivos.

| Archivo | Cambio | EOL |
|---|---|---|
| `catalogs.py` | `DOMAIN_CONTENT_SIGNALS` (subconjunto estricto + refutación de `DOMAIN_MAP` documentada) | **CRLF** |
| `context_builder.py` | `score_domain_signals` · `resolve_domain_from_content` · `describe_domain_resolution` (las 3 **puras, module-level**) · gate de 3 líneas sobre el sumidero · procedencia · `describe()` | **LF** |
| `main.py` | **fix #5** (`Path(__file__).parent.parent / "prompts"`) · import · hint en la rama `--document` | **CRLF** |
| `schema.py` | `domain_resolution` (default `"unknown"` — no puede mentir) + `domain_signals` en `RuntimeContext` | **CRLF** |
| `tribunal_transversal.py` | import + `Resolved by:` en el bloque AFO. **3 líneas. No toca `_synthesize`, `_apply_collapse_guard`, `_apply_confidence`, ni el camino del veredicto** | **CRLF** |
| `domain_catalog.py` | los 2 docstrings que **fix #5 volvió falsos** + sección `UPSTREAM OF THIS MODULE (LW-8)` | **LF** |
| `test_domain_content_resolution.py` | **nuevo**, 68 tests offline | **LF** |

**`_resolve_domain` NO se tocó.** LW-1 byte-identical.

### 🧪 315 tests offline VERDES
- `test_domain_content_resolution` **68/68** — A3: **las 83 claves de `DOMAIN_MAP` resuelven igual sin hint** · A1/A2: el stem gana **con hint contradictorio presente** · C1/C2/C3: hipótesis refutada clavada · D1-D3: `agenda`/`Rwanda`↛`nda`, `photos`↛`tos`, `sowing`↛`sow` · F2: `minor` prohibido · G1-G10: renderizado de la procedencia
- `test_domain_resolver` **23/23** → LW-1 intacto
- `test_domain_catalog_all19` **224/224** → inyección Forense-only intacta, `build_rol_prompt` sigue sin filtrar IDs Legal al layer de Rol

---

## 🎯 LA EVIDENCIA DEL CERT — `_probe_lw8.py`, offline, determinista, $0

**Los mismos 3537 bytes. Cuatro corridas. Este es LW-8 entero:**

| # | stem | contenido | dominio | catálogo | LG08 | LG09 |
|---|---|---|---|---|---|---|
| 1 | `mindmate_tos` | OFF | **General** | **0 chars** | **✗** | **✗** |
| 2 | `ai_governance_companion_minors` | OFF | Legal | **8976 chars** | ✓ | ✓ |
| 3 | `mindmate_tos` | **ON** | **Legal** (`document-content`) | **8976 chars** | ✓ | ✓ |
| 4 | `ai_governance_companion_minors` | ON | Legal (`subscenario-keyword`) | **8976 chars** | ✓ | ✓ |

**(1) vs (2): renombrar el archivo hacía aparecer o desaparecer 8976 caracteres de reglas vinculantes.** (3) lo arregla. **(4) es la no-regresión sobre bytes reales: el stem afortunado sigue ganando y produce 8976 idénticos a (2).**

Señales detectadas en el documento real: **8** — `age verification`, `ai governance`, `emotional dependency`, `mental health`, `minors`, `parental consent`, `self-harm`, `tos`. Umbral 3, margen 8 sobre el runner-up.

⚠️ **El probe fue BORRADO** (`orchestrator/_probe_lw8.py`). **Recrearlo en s42 si el cert lo necesita** — es reproducible desde esta tabla y los 4 casos están descritos arriba.

### LW-8 probado VIVO en el pipeline real (2 corridas, $0)
```
[RUNTIME CONTEXT]
  Domain:      Legal  (resolved by: document-content)
  Type:        general / mindmate_tos
```
Y en el transparency report:
```
  Resolved by: document-content — resolved from the document itself (stem carried no usable signal).
               Content signals — Legal: 8 [age verification, ai governance, emotional dependency, ...]
```
**El ruteo movió el tribunal entero, no un string:** los 5 Rol y 5 Forense son los del catálogo Legal (Clause/Jurisdiction/IP/Liability/Compliance Forense, Opposing Counsel…). Con `General` habrían sido Logic/Evidence/Risk genéricos.

**LW-8 resuelve ANTES de la primera llamada API** — por eso se midió incluso sin servidor.

### La línea que produce el sumidero (C2 en acción)
```
  Domain:      General / mindmate_tos
  Resolved by: general-sink — NO DOMAIN COULD BE RESOLVED. General declares no Failure
               Catalog, so NO binding severity rules were injected into the Forense N1
               prompts: any domain hard gate (e.g. Legal RULE LG08 minors / RULE LG09
               self-harm crisis) did NOT apply and severity fell back to generic model
               judgement. If this document belongs to a catalog-bearing domain, pin it
               with --type and re-run.
               Content signals found but undecided — Legal: 1 [mental health]
```
Y `subscenario-keyword` dice textualmente *«matched a keyword in the SUBSCENARIO STRING. In --document mode that string is the FILENAME STEM, not the document body»*. **DS-CF1CEFD1 de s40 habría declarado, en su propio reporte, que resolvió Legal por el nombre del archivo.**

---

## ⏳ LO ÚNICO QUE FALTA PARA v3.24.0

1. **e2e SANO** con `mindmate_tos.txt` → reglas LG08/LG09 **citadas por ID** + **INVIABLE**. **NO logrado en s41** (2 intentos, ambos colapso de infra). $0 con NVIDIA. *Prueba que las reglas inyectadas se APLICAN — el ruteo ya está probado por el probe, que es mejor evidencia.*
2. **RULE 08 self-audit L0** del PA-agent → después el cert.
3. **Cert SUSTANTIVO 7-axis JARP DEEP** — `PA-20260716-001` (self-audit) + `PA-2026MMDD-002` (cert). **0 CRITICAL + 0 SERIOUS absoluto, sin condiciones.**
4. **Bump v3.24.0** — `bump_stamps.ps1 -OldVersion 3.23.0 -NewVersion 3.24.0 -Apply` + one-shot Python (banners orquestador, CHANGELOG, roadmap rows) + ACTIVE en README/CLAUDE.
5. **Sync canónicos + b2 en el MISMO commit** (posicional, ambos archivos).
6. **Continuity v41** + push + read-back remoto.

### Lo que el cert PODRÁ afirmar (medido)
19/19 migrados · sin fuga de contrato competidor · inyección Forense-only, Rol limpio · **LW-8: el dominio resuelve por contenido cuando el stem falla (probe 4 casos, bytes reales)** · **la omisión nunca es silenciosa (procedencia universal, 20/20)** · **LW-1 byte-identical (83/83 claves + monotonía sobre el doc real)** · guardas LW-5/6/7 sobreviven al delta (**5 vectores de colapso**: auth, conexión, upstream 503, 401 de proxy, puerto muerto) · fix #5 mata la dependencia del CWD · 315 tests offline.

### Lo que DEBERÁ declarar como NO evidenciado
- **WATCH live L07 ABIERTO — 6ª sesión (s36→s41).** Que el N1 aplique LG08/LG09 como base-FATAL **bajo Opus** no está medido. Nemotron ≠ Opus (#34).
- **N2 decorativo** (`n2: 0`) y **fallback sin dedup** — fuera del delta, → v3.25.0.

---

## 🔴 ACCIÓN DE CIERRE PENDIENTE, SIN VERIFICAR

**`NVIDIA_NIM_API_KEY` COMPROMETIDA.** En s41 JARP pegó el `.env` completo de `~/.fcc/` en el chat, en texto plano. La key (`nvapi-wkEM…`, org `JARP`, key `dark-strategist`, 12 meses) quedó en el transcript de claude.ai. **Se pidió rotación dos veces; JARP no respondió. NO SE PUEDE DAR POR HECHA.**

Agravante: `HOST=0.0.0.0` → `/v1/messages` escucha en toda la LAN.

**Acción: revocar `dark-strategist` en build.nvidia.com, emitir nueva, cargar por la Admin UI** (que para *escribir* secretos sí sirve; el agujero del hallazgo #7 es solo para vaciarlos).

**Regla nueva: NUNCA volcar un `.env` completo a una conversación.**
```powershell
Get-Content "$env:USERPROFILE\.fcc\.env" | Where-Object { $_ -notmatch '(KEY|TOKEN|SECRET)=.+' }
```

---

## 🔧 INFRA — 6 HALLAZGOS NUEVOS DE s41 (van a b2, sumados a los 8 de s40)

| # | Hallazgo |
|---|---|
| 9 | **EOL MEZCLADO en `orchestrator/`.** LF: `context_builder.py`, `domain_catalog.py`, `test_*.py` nuevos · CRLF: `catalogs.py`, `main.py`, `schema.py`, `tribunal_transversal.py`. **La nota vigente («orchestrator .py files CRLF») es FALSA.** Un overwrite ingenuo habría metido ~200 líneas fantasma en el diff del cert. **Detección per-file OBLIGATORIA.** |
| 10 | **`ANTHROPIC_AUTH_TOKEN` vacío es estado de TRABAJO, no de reposo.** Restaurar `freecc` al cerrar (como ordena v39 por seguridad) **rompe la corrida siguiente** con 401 ×10. Documentar el CICLO, no solo la restauración. |
| 11 | **Nunca volcar un `.env` completo a una conversación.** Filtrar siempre (ver arriba). |
| 12 | **Existe un tier `MODEL_FABLE` / `ENABLE_FABLE_THINKING`** en `~/.fcc/.env`. La nota #43 habla de 11 backends y ni sabe que existe. |
| 13 | **`uv run fcc-server` reconstruye el venv en cada arranque** («Uninstalled 1 package / Installed 1 package») y avisa *«Failed to hardlink files; falling back to full copy»* — cache y target en filesystems distintos. Con `UV_PROJECT_ENVIRONMENT` fuera de OneDrive es inocuo pero lento. |
| 14 | **`LEGAL_SUBAREA_MAP` DIVERGIDO y probablemente HUÉRFANO.** El prompt declara **13** señales L07; `catalogs.py` tiene **4**. Las 9 de v3.22.0 aterrizaron en el prompt y **nunca en el código**. Y `context_builder.py` **no lo importa**. Familia `router.py`. → v3.25.0, **requiere trace de imports antes de tocarlo**. |

### Config que funciona (`~/.fcc/.env`) — verificada en s41
`MODEL=nvidia_nim/nvidia/nemotron-3-super-120b-a12b` 📌 pin del cert · `MODEL_OPUS=` vacío → fallback · `ENABLE_MODEL_THINKING=false` · `ANTHROPIC_AUTH_TOKEN=` **vacío para trabajar** · `NVIDIA_NIM_API_KEY` **A ROTAR**.

### Secuencia (v39 §SECUENCIA, sigue vigente)
```powershell
# ── Ventana A — proxy. Queda ocupada. NO tocar. Verificar el env var ANTES:
$env:UV_PROJECT_ENVIRONMENT        # debe imprimir C:\Users\jrodr\.venvs\free-claude-code
$env:UV_PROJECT_ENVIRONMENT = "C:\Users\jrodr\.venvs\free-claude-code"   # OBLIGATORIO: fuera de OneDrive
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\free-claude-code"        # OBLIGATORIO: uv run resuelve contra el CWD
uv run fcc-server
# esperar: Uvicorn running on http://0.0.0.0:8082

# ── Ventana B — health SOLO. Parar y leer el número.
cd "C:\Users\jrodr\OneDrive\Documentos 1\GitHub\dark-strategist-agent"
$env:ANTHROPIC_API_KEY  = "freecc"
$env:ANTHROPIC_BASE_URL = "http://127.0.0.1:8082"
curl.exe -s -o NUL -w "health -> %{http_code}`n" http://127.0.0.1:8082/health
#  200 -> seguir | 000 -> NO HAY SERVIDOR, no correr DS | 401/503 -> otra capa

# ── Ventana B — DS, SOLO si el health dio 200
python orchestrator\main.py --document orchestrator\_livewatch\mindmate_tos.txt --tribunal --regime adversarial --verbose
```
- **`UV_PROJECT_ENVIRONMENT` vive solo en su ventana.** Reiniciar el server en OTRA ventana reconstruye el venv dentro de OneDrive → vuelve el hallazgo #6 (borrado destructivo intermitente). **Hacerlo permanente (`setx`) en s42.**
- **`Ctrl+C` es una COMBINACIÓN DE TECLAS.** No se escribe en un bloque de comandos.
- **Para e2e cert-grade con `sk-ant`: `Remove-Item Env:ANTHROPIC_BASE_URL` primero** o la evidencia se contamina (#34).

---

## LECCIÓN TRANSVERSAL DE s41

**Medir mata hipótesis elegantes. Tres murieron en una sesión, ninguna por criterio.**

1. El diseño congelado **con GO explícito de JARP** no compilaba — lo dijo `context_builder.py`, no yo.
2. La lista L07 de v39 tenía `minor` por `minors` — lo dijo `system_prompt_legal.md`, contra un cambio que el propio toolkit registraba.
3. Reusar `DOMAIN_MAP` era elegante, gratis y **catastrófico** — lo dijo la tabla de claves, no la intuición.

Las tres estaban en documentos que decían ser fuente. **Ni el texto canónico ni Claude son fuente: la fuente es el archivo abierto y el sistema respondiendo.**

**Otras reglas nuevas de s41:**
- **El `curl /health` es una COMPUERTA, no un adorno.** s41 midió `health -> 000` y corrió DS igual. 23 segundos de timeout contra un puerto vacío. **La regla existía, escrita en v39, y se ignoró teniendo la medición fresca en la línea de arriba.** → **Separar el health de la corrida en DOS TURNOS.** Cuesta 10 segundos y elimina la posibilidad.
- **La evidencia offline determinista supera al live run** cuando lo que se prueba es lógica de ruteo. El probe midió LW-8 exacto, en 4 casos, a $0, sin Nemotron de intermediario. El live run prueba **otra cosa** (que las reglas se aplican), no lo mismo mejor.
- **Detectar EOL per-file antes de cualquier escritura.** Ver hallazgo #9.
- **Nunca pegar un `.env` completo en un chat.** Ver hallazgo #11.
- **Los fallos de infra siguen siendo evidencia gratis**: los 2 colapsos de s41 probaron LW-5/6/7 contra 2 vectores nuevos (401 de proxy, puerto muerto). 5 vectores acumulados.
- **Un doc que describe mal su propio runtime es el defecto que estamos cerrando.** `domain_catalog.py` decía *«deferred to v3.25.0»* de algo que fix #5 arregló 20 minutos después. Corregido en el mismo delta.

---

## BACKLOG ABIERTO

**Gobernanza:**
- 🔴 **ROTAR `NVIDIA_NIM_API_KEY`** — sin verificar (ver arriba).
- **Nota #34 vs. realidad — DECISIÓN PENDIENTE DE JARP.** #34 exige *«real Opus (sk-ant, no proxy) for cert-grade live evidence only»*. JARP declaró en s39 que usará NVIDIA por costo cero. Si se quiere certificar comportamiento forense con NVIDIA, **#34 debe editarse formalmente en ambos canónicos** — con la consecuencia de que DS nunca tendría evidencia cert-grade sobre `claude-opus-4-7`, su modelo de producción declarado.
- **Notas #34/#43 DESACTUALIZADAS (b2):** documentan `uv run uvicorn server:app` y `server.py`, **inexistentes**. Repo real `free-claude-code` **v4.6.4**, layout `src/free_claude_code`, entry point `fcc-server`, arranque `uv run fcc-server`. `requires-python >=3.14.0`, `uv >= 0.11.0` (instalado 0.11.29). **~25 backends, no 11. + tier Fable.** Config vía Admin UI → `~/.fcc/.env`. **+ los 8 hallazgos de s40 + los 6 de s41.**
- **PA-agent PA-20260527-002 vence 25/08/2026** — 40 días.

**v3.25.0 (candidatos):**
- **`content[0].text` sin filtro de tipo** ×2 sitios (`tribunal_transversal.py` L601 `_call_agent` fuera del try, L261 `_synthesize` dentro) — vector de colapso latente contra backends proxeados, que es lo que #34 ordena para TODAS las corridas no-cert. ~3 líneas.
- **`LEGAL_SUBAREA_MAP`** divergido + huérfano (hallazgo #14).
- **SubAgentSpawner:** N2 decorativo (10 spawns, 0 llamadas) + el reporte afirma participación inexistente. 9 N2 hardcoded en `PERMANENT_SUBAGENTS`.
- **Dedup en `_deterministic_synthesis`** + matcher de corroboración tolerante a variantes de redacción.
- **Reparación/reintento en el camino de síntesis** (truncamiento JSON).
- **`--document` + `--type`:** el `if/elif` de `main.py` **descarta el documento en silencio** si vienen los 3 flags — `document = f"[Document type: ...]"`, 60 chars. **Confirmado textual en s41.** Mismo fail-open silencioso que LW-8, otra rama.
- **Reporte de colapso parcial:** lista `stance=NEUTRAL`/`verdict=UNKNOWN` para agentes que errorearon.
- **`router.py` cleanup:** huérfano (5199 bytes) + desactualizado (14/20). **Solo post-cert de v3.24.0.**
- **AI Disclaimer BLOCK 7 (RULE LG03):** sin cablear a síntesis/AFO.
- **Extender `DOMAIN_CONTENT_SIGNALS` a los otros 18 dominios** — contenido puro, sin código. Fundarlas leyendo cada variant (~500KB); no inventarlas.
- **`UV_PROJECT_ENVIRONMENT` permanente** (`setx` o perfil de PowerShell).

**Trading hands-on:** POSTERGADO desde s4 — **38 sesiones (4–41)**, prioridad #1 en userPreferences. **No re-confrontar** salvo activación explícita. s41 no lo eligió → prioridad real ≠ escrita.

---

## FIXTURES (`orchestrator/_livewatch/`, NO trackeado — verificado por `git status --short`)

| Archivo | Bytes | Resuelve a |
|---|---|---|
| `ai_governance_companion_minors.txt` | 3537 | **Legal** por `subscenario-keyword` (el stem) |
| `mindmate_tos.txt` | 3537 | **Legal** por `document-content` ← **copia creada en s41. LA PRUEBA DE LW-8.** |
| `lw2_contract.txt` | 2000 | **Legal** (stem `contract`) |
| `cert_brief_v3_22_0.md` | 5436 | — |

⚠️ Existe además `_livewatch/` en la RAÍZ (`lw5_collapse.txt`, `signals_acme.txt`, `strategy_acme_board_proposal.txt`). Ambos ignorados (`_livewatch/` matchea a cualquier nivel). Inocuo, documentado.

---

## PROTOCOLO DE INICIO (s42)

**PHASE 0:**
- HEADs remotos reales (`list_commits perPage=3`): DS debería estar en el commit de s41 (delta v3.24.0 + rotación v40, parent `e02963d5`); jarp-toolkit en `514fa026`.
- Cert registry: ambos canónicos concuerdan **POSICIONALMENTE** en v3.23.0 / PA-20260712-002 (8 posiciones — **NO `Select-String`**, lección drift s33/s34).
- `orchestrator/_livewatch` NO trackeado — por read-back del árbol **y** `git status --short`.
- Working tree: **`git status --short`** (NUNCA `git diff --stat`, lección s39). **Claude no tiene shell en Windows: pedírselo a JARP.**
- **Verificar que los 3 one-shots de s41 NO están en el remoto** (`_oneshot_lw8.py`, `_oneshot_lw8_b.py`, `orchestrator/_probe_lw8.py`) → `get_file_contents` → **404**. Borrados localmente en s41 y ausentes del `git status`; **confirmar contra el remoto, no contra el commit msg.**

**PHASE 1 — decisión, esperar GO.** Candidatos:
- **(b1) CERRAR v3.24.0:** infra viva → e2e sano con `mindmate_tos.txt` → self-audit L0 → cert 7-axis SUSTANTIVO → bump → sync canónicos + b2 → continuity v41 → push. ← **el camino. Solo falta el e2e.**
- **(b2) sync jarp-toolkit** — notas #34/#43 + **14 hallazgos de infra** (8 de s40 + 6 de s41) + reglas operativas nuevas. **No depende de key ni server.** Plegarlo en el commit de sync de b1.
- **(b3) `content[0].text` sin filtro de tipo** (v3.25.0, post-cert).
- **(b4) SubAgentSpawner** (N2 decorativo).
- **(b5) `router.py` + `LEGAL_SUBAREA_MAP` cleanup** (solo post-cert).

**STANDING:** sistema más robusto/valioso/eficiente; nunca barato-dormido sobre valor real. **VERIFICAR CONTRA FUENTE REAL ANTES DE DAR POR BUENO — MEDIR, NO INFERIR.** Ni el texto canónico ni Claude son fuente: la fuente es el sistema respondiendo. **El GO no exime de auditar** (s36 GEOFENCE, s40 LW-8, s41 diseño congelado). Trabajar en silencio, priorizar tokens. Español para conversación, inglés estricto para código/comentarios (prefijo `//--- `).
