# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"No tienes lealtad hacia ninguna solución. Tu único estándar es la verdad bajo presión máxima."*

---

## ¿Qué es esto?

El **Dark Strategist** es un agente IA de auditoría forense y orquestación adversarial. No valida propuestas — las **destruye sistemáticamente** para exponer lo que puede fallar antes de que la realidad lo haga.

Opera bajo una lógica de **"destrucción constructiva"**: la validez de una propuesta no se asume — debe sobrevivir a una inspección de 7 niveles, ejecutada por micro-agentes especializados coordinados por un Director de Auditoría.

---

## Capacidades v2.3.0

| Capacidad | Descripción |
|-----------|-------------|
| **7 niveles de análisis forense** | Estructural → Lógico → Supuestos → Riesgos → Omisiones → Implementación → Consecuencias |
| **Severidad dinámica (Regla 09)** | LATENTE que genera colapso en Nivel 7 escala automáticamente a FATAL |
| **War Room con umbral determinista** | 4 criterios de activación — no intuición |
| **Geofence Audit** | Geografía como multiplicador de severidad (4 variables) |
| **7 micro-agentes estándar** | UNIT-QUANT, UNIT-INQUISITOR, UNIT-TECH, UNIT-BIO, UNIT-MARKET, UNIT-GEO, UNIT-COMPLIANCE |
| **Matriz de activación por dominio** | Determinista — dado un dominio, los agentes se asignan sin ambigüedad |
| **NEGLECT_DETECTED** | Bloquea análisis si revisión ignora un FATAL previo (3 criterios de desbloqueo, límite 3 intentos) |
| **VERSION_TRACK** | Detecta maquillaje vs. corrección real entre versiones |
| **Tabla de veredicto determinista** | Lógica cascada: FATAL → INVIABLE, sin ambigüedad |
| **Dual-Language Protocol** | Reportes en español, SYSTEM_LOGS en inglés, mapa ES/EN explícito |
| **REPORT_ID convention** | Formato `DS-AAAAMMDD-NNN` para trazabilidad entre sesiones |
| **Agnosticismo sectorial** | Audita lógica, no industrias |

---

## Estructura del Repositorio

```
dark-strategist-agent/
├── README.md                              ← Este archivo
├── CLAUDE.md                              ← Instrucciones para Claude
├── CHANGELOG.md                           ← Historial de versiones
├── prompts/
│   └── system_prompt.md                   ← System prompt production-ready (EN)
├── examples/
│   ├── example_01_business_plan.md        ← Ejemplo: plan de negocio e-commerce
│   ├── example_02_tech_architecture.md    ← Ejemplo: migración a microservicios
│   └── example_03_war_room.md             ← Ejemplo: análisis multi-dominio con War Room
└── docs/
    └── report_template.md                 ← Plantilla de reporte vacía (para uso inmediato)
```

---

## Instalación Rápida

### Claude.ai Projects (recomendado)
1. Copia el contenido de `prompts/system_prompt.md`
2. Ve a Claude.ai → Projects → New Project → Project Instructions
3. Pega el prompt completo
4. Presenta tu propuesta al agente

### Claude API (Python)
```python
import anthropic

with open("prompts/system_prompt.md", "r", encoding="utf-8") as f:
    system = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8192,
    system=system,
    messages=[{"role": "user", "content": "Mi propuesta: [TEXTO]"}]
)
print(response.content[0].text)
```

### Activación por identificador
```
@SOVEREIGN_ADVERSARY → activa el agente
[INVOKE: ADVERSARY]  → activación alternativa
[ORCHESTRATOR: DARK_STRATEGIST] → modo orquestador
```

---

## Flujo de Análisis

```
Usuario presenta propuesta
         ↓
    PHASE 0 — INTAKE
  (Dominio, Escala, Restricciones,
   Objetivo, Versión, Geofence Audit)
         ↓
  ¿Umbral War Room cumplido?
    ↙ NO          ↘ SÍ
Análisis      War Room activa
 lineal      micro-agentes
    ↘            ↙
   7 NIVELES FORENSES
  (por cada nivel o agente)
         ↓
    SEVERIDAD DINÁMICA
   (Regla 09 — escalada)
         ↓
   BLOQUE 6 — VEREDICTO
  (tabla determinista cascada)
         ↓
  ¿Usuario pide correcciones?
         ↓ SÍ
   PLAN DE CORRECCIÓN §4.9
```

---

## Taxonomía de Severidad

| Nivel | Descripción | Acción |
|-------|-------------|--------|
| 🔴 **FATAL** | Invalida la solución. Fracaso con certeza si no se resuelve. | Aparece en veredicto obligatoriamente |
| 🟠 **GRAVE** | Compromete significativamente el éxito. | Corregir antes de cualquier ejecución |
| 🟡 **MODERADO** | Debilita materialmente sin matar la solución. | Abordar en refinamiento |
| 🔵 **LATENTE** | Riesgo de 2.° o 3.° orden. Sujeto a escalada por Regla 09. | Monitoreo activo |

**Regla 09 — Escalada Transversal:** 🔵 LATENTE que dispara colapso en Nivel 7 → escala a 🔴 FATAL automáticamente.

---

## Veredicto — Tabla Determinista

| Condición | Veredicto |
|-----------|-----------|
| ≥ 1 🔴 FATAL | 🔴 INVIABLE |
| 0 FATAL + ≥ 1 🟠 GRAVE | 🟠 VIABLE CON CORRECCIONES CRÍTICAS |
| 0 FATAL + 0 GRAVE + ≥ 1 🟡 MODERADO | 🟡 VIABLE CON AJUSTES |
| Solo 🔵 LATENTE o sin hallazgos | 🟢 SÓLIDA BAJO PRESIÓN |

---

## Cuándo usarlo

✅ Antes de ejecutar un plan de negocio
✅ Antes de presentar a inversores o stakeholders
✅ Antes de lanzar una arquitectura a producción
✅ Antes de firmar un contrato o acuerdo significativo
✅ Antes de defender una estrategia en reunión de alto nivel
✅ Para cualquier propuesta en cualquier industria o país

❌ Para recibir retroalimentación amable
❌ Para validar algo que ya no puede cambiarse

---

## Dominios Soportados

El protocolo es agnóstico a la industria. Cubre explícitamente:

`Negocio / Comercial` · `Tecnológico / Sistemas / IA` · `Financiero / Mercados` · `Mercados de Capitales` · `Legal / Regulatorio` · `Auditoría de Sistemas / Ciberseguridad` · `Agro / Pesca / Minería / Ganadería / Extractivo` · `Sector Público / Gobierno` · `Científico / I+D` · `Dominio desconocido (Sub-Protocolo §4.3)`

---

## Versión

`v2.3.0` — Ver [CHANGELOG.md](./CHANGELOG.md) para historial completo.

**Evolución del protocolo:**
- v1.0 → Prompt adversarial base
- v2.0 → Intake estructurado, taxonomía de severidad, 7 niveles, 8 reglas
- v2.1 → War Room, Geofence Audit, Reglas 09-10, NEGLECT_DETECTED, Red Line Rule
- v2.2 → Lógica de veredicto determinista, estándar de evidencia Regla 10, NEGLECT unlock, matriz §4.13
- v2.3 → Mapa ES/EN, umbral War Room, Geofence expandido en reporte, VERSION_TRACK degradation, UNIT-BIO ganadería, REPORT_ID convention

---

## Autor

JARP — parte del ecosistema de agentes IA personales.
