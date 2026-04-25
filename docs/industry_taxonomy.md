# Industry & Business Taxonomy — Dark Strategist v2.5.1
# Section §4.22

This document provides the agent with a complete, professional taxonomy of industries and business lines for precise domain classification in Phase 0. It eliminates ambiguity when the user declares their sector and enables more accurate calibration of the forensic analysis framework.

Source: Unified architecture integrating modern sectors including e-commerce, content creators, R&D, and public sector.

---

## How the Agent Uses This Taxonomy

**In Phase 0 — Domain Identification:**
When the user declares their industry or business line, the agent cross-references this taxonomy to:
1. Confirm or suggest the precise classification
2. Identify if the entity is multi-industry (triggers War Room consideration)
3. Map to the corresponding calibration framework in §4.6
4. Determine micro-agent activation via §4.13 matrix

**Cross-Industry Note:**
Some solutions apply to any industry and giro (e.g., accounting software, talent management platforms). These are classified as `[CROSS-INDUSTRY]` and use the domain declared in Phase 0 for calibration, not the solution's own nature.

**Giro de Negocio as secondary classifier:**
The giro complements the industry declaration. It defines HOW the entity operates, not WHERE. A company in the Retail industry with a SaaS giro (e.g., e-commerce platform) activates both UNIT-TECH and UNIT-MARKET.

---

## §4.22.A — Unified Industry List (22 Industries)

Defines the sector or economic ecosystem where the entity operates.

### Energía y Recursos Naturales

| Industry | Description |
|---|---|
| **Agricultura, Ganadería y Pesca** | Primary production and biological raw materials |
| **Minería y Metales** | Mineral extraction and basic metallurgical processing |
| **Petróleo, Gas y Energía** | Hydrocarbons and fossil fuels |
| **Química** | Production of industrial substances, fertilizers, and polymers |
| **Servicios Públicos (Utilities)** | Electricity, water, gas, and waste management |

### Manufactura y Construcción

| Industry | Description |
|---|---|
| **Aeroespacial y Defensa** | Aeronautical, space technology, and security |
| **Automotriz** | Vehicle and auto parts design and manufacturing |
| **Productos de Consumo** | Fast-moving consumer goods (food, personal care, home) |
| **Ingeniería, Construcción y Operaciones** | Infrastructure, civil works, and buildings |
| **Alta Tecnología (High Tech)** | Semiconductors, hardware, and electronics |
| **Manufactura Industrial** | Heavy machinery and production equipment |
| **Productos Derivados (Mill Products)** | Processing of wood, paper, steel, and textiles |

### Servicios y Conocimiento

| Industry | Description |
|---|---|
| **Servicios Financieros y Seguros** | Banking, investments, and risk management |
| **Ciencias de la Vida y Biotecnología** | Pharmaceuticals and medical devices |
| **Salud** | Clinical, hospital, and medical assistance services |
| **Medios y Entretenimiento** | Film, TV, music, video games, and Content Creators |
| **Servicios Profesionales, Científicos y Técnicos** | Consulting, legal (law firms), and R&D |
| **Sector Público y Gobierno** | State administration and international organizations |
| **Retail y Comercio** | Physical retail and E-commerce |
| **Telecomunicaciones** | Data networks, connectivity, and internet |
| **Viajes, Transporte y Logística** | Airlines, hotels, cargo, and warehousing |
| **Distribución Mayorista** | Large-scale supply |
| **Educación** | Academic institutions and training platforms |
| **Inmobiliaria (Real Estate)** | Real estate management and development |

---

## §4.22.B — Unified Business Line List (23 Giros)

Defines the specific activity and operating model of the entity.

### Giro Comercial (Intermediación)

| Giro | Description |
|---|---|
| **Mayorista** | Large-scale buying and selling |
| **Minorista (Retail / E-commerce)** | Direct sale to end user (physical or digital) |
| **Comisionista / Marketplace** | Intermediation between third parties for commission |
| **Distribución** | Logistical placement of products |

### Giro Industrial (Transformación)

| Giro | Description |
|---|---|
| **Extractivo** | Direct capture of natural resources |
| **Manufactura de Consumo** | Production of finished goods |
| **Manufactura de Capital** | Production of machinery for other industries |
| **Maquila y Ensamblaje** | Partial processing or assembly for third parties |

### Giro de Servicios (Intangibles)

| Giro | Description |
|---|---|
| **Servicios Profesionales** | Specialized advisory (Legal, Accounting, Consulting) |
| **Servicios Financieros** | Capital management, loans, and insurance |
| **Salud y Bienestar** | Medical care and personal wellness |
| **Educación y Capacitación** | Teaching and technical training |
| **Logística y Transporte** | Mobility of goods or people |
| **Hospitalidad y Gastronomía** | Accommodation and food services |
| **Mantenimiento y Soporte** | Technical, IT, and cleaning services |

### Giro Tecnológico y Digital

| Giro | Description |
|---|---|
| **SaaS (Software as a Service)** | Cloud-based subscription software |
| **Desarrollo e Innovación (R&D)** | Software, AI creation, and Intellectual Property |
| **Contenido Digital y Medios** | Streaming, Podcasting, YouTube, and Influencer Marketing |
| **Ciberseguridad y Datos** | Information protection and administration |

### Giro Gubernamental y Público

| Giro | Description |
|---|---|
| **Administración y Gobernanza** | Policy management and citizen services |
| **Regulación y Supervisión** | Market and regulatory oversight |
| **Justicia y Seguridad** | Judiciary and law enforcement |
| **Empresas Estatales** | State-owned productive entities |

---

## §4.22.C — Giro → Micro-Agent Mapping (Supplementary)

The giro de negocio complements the industry-based micro-agent activation matrix in §4.13. When the giro provides additional signal, the Director applies this supplementary mapping:

| Giro Category | Additional Micro-Agent Signal |
|---|---|
| Giro Comercial (Mayorista, Retail, E-commerce, Marketplace) | UNIT-MARKET + UNIT-INQUISITOR |
| Giro Industrial (Extractivo, Manufactura, Maquila) | UNIT-BIO (extractivo) / UNIT-TECH (manufactura) |
| Giro de Servicios Profesionales | UNIT-INQUISITOR + UNIT-COMPLIANCE |
| Giro de Servicios Financieros | UNIT-QUANT + UNIT-GEO |
| Giro Tecnológico (SaaS, R&D, Ciberseguridad) | UNIT-TECH + UNIT-COMPLIANCE |
| Giro Tecnológico (Contenido Digital y Medios) | UNIT-MARKET + UNIT-INQUISITOR |
| Giro Gubernamental | UNIT-COMPLIANCE + UNIT-INQUISITOR + UNIT-GEO |

**Rule:** The §4.13 industry matrix is the primary activation mechanism. The §4.22.C giro mapping is a secondary signal used when the giro provides specificity the industry declaration does not (e.g., a company in Retail industry with a SaaS giro activates both UNIT-MARKET and UNIT-TECH).

---

## §4.22.D — Phase 0 Classification Examples

| User Statement | Industry | Giro | Notes |
|---|---|---|---|
| "Somos una plataforma de e-commerce de moda" | Retail y Comercio | Minorista / E-commerce | May also trigger UNIT-TECH if platform is proprietary |
| "Tenemos un canal de YouTube de finanzas" | Medios y Entretenimiento | Contenido Digital y Medios | UNIT-MARKET + UNIT-INQUISITOR active |
| "Desarrollamos software de IA para hospitales" | Ciencias de la Vida / Alta Tecnología | SaaS / Desarrollo e Innovación (R&D) | Multi-industry → War Room consideration |
| "Somos un estudio de abogados corporativos" | Servicios Profesionales | Servicios Profesionales | UNIT-INQUISITOR + UNIT-COMPLIANCE |
| "Empresa minera de cobre en Perú" | Minería y Metales | Extractivo | UNIT-BIO + UNIT-GEO + UNIT-INQUISITOR + Geofence Audit critical |
| "Startup de ciberseguridad B2B" | Alta Tecnología | Ciberseguridad y Datos | UNIT-TECH + UNIT-COMPLIANCE + UNIT-GEO |
| "ONG de educación en zonas rurales" | Educación / Sector Público | Administración y Gobernanza | UNIT-COMPLIANCE + UNIT-INQUISITOR + UNIT-GEO |
