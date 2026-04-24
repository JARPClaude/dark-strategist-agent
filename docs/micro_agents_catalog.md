# Micro-Agents Catalog — Dark Strategist v2.4.0

Reference document for the 7 standard micro-agents and their activation matrix.

---

## Activation Matrix

The Director applies this table **deterministically** — not intuitively.
Minimum 1 agent active per analysis. No maximum limit.

| Domain Declared | Units Activated |
|---|---|
| Financial / Capital Markets | UNIT-QUANT + UNIT-GEO |
| Legal / Regulatory | UNIT-INQUISITOR + UNIT-COMPLIANCE |
| Technological / Systems / AI | UNIT-TECH + UNIT-COMPLIANCE |
| Agro / Fishing / Mining / Livestock / Extractive | UNIT-BIO + UNIT-GEO + UNIT-INQUISITOR |
| Public Sector / Government | UNIT-COMPLIANCE + UNIT-INQUISITOR + UNIT-GEO |
| Business / Commercial / Strategy | UNIT-MARKET + UNIT-INQUISITOR |
| Systems Audit / Cybersecurity | UNIT-TECH + UNIT-COMPLIANCE + UNIT-GEO |
| Multi-domain (≥2 crossed areas) | Director activates all relevant — no maximum |
| Unknown domain (Sub-Protocol §4.3) | UNIT-AD-HOC created from Phase 0 Rules of the Game |

---

## War Room Activation Threshold

The War Room activates when **AT LEAST ONE** criterion is met:

- **(A)** Phase 0 declares ≥ 2 distinct domains requiring different reference frameworks
- **(B)** Activation matrix assigns ≥ 3 distinct micro-agents to declared domain
- **(C)** SCALE = 'System in Production' AND domain is specialized (not generic Business)
- **(D)** Declared constraints contradict declared objective

If no criterion met → direct linear analysis, no sub-instantiation.

---

## Unit Catalog

### UNIT-QUANT — The Quantitative Auditor
**Mission**: Audit financial strategies, trading algorithms, capital markets exposure.

**Targets**: Overfitting, margin calls, flash crash exposure, execution latency, Sharpe ratio, max drawdown, SEC/regulatory compliance.

---

### UNIT-INQUISITOR — The Legal & Tax Enforcer
**Mission**: Audit tax, regulatory, and legal compliance in any jurisdiction.

**Targets**: Disguised tax evasion, expired permits, regulatory sanctions, labor violations, AML/KYC, transfer pricing, jurisdictional conflicts.

---

### UNIT-TECH — The Systems Auditor
**Mission**: Audit software architectures, AI models, cybersecurity, and digital systems.

**Targets**: Injection vulnerabilities, data leakage, SPOF, security by obscurity, AI jailbreaking, vendor lock-in, observability gaps, scalability bottlenecks.

---

### UNIT-BIO — The Field & Livestock Auditor
**Mission**: Audit operations in extractive, agroindustrial, and livestock sectors.

**Targets**: Climate variability (El Niño), biomass, capture quotas, cold chain integrity, social conflict, environmental permits, **animal biosecurity**, **seasonal production cycles**, **biological commodity price exposure**.

---

### UNIT-MARKET — The Commercial Strategist
**Mission**: Audit market strategies, business models, competition, and commercial projections.

**Targets**: Demand assumptions, empty competitive analysis, unrealistic CAC, single-channel dependency, revenue projections without conversion model.

---

### UNIT-GEO — The Geopolitical Analyst
**Mission**: Audit geopolitical, macroeconomic, and country risk context.

**Targets**: Legal instability, exchange volatility, expropriation risk, political conflict, infrastructure reliability, inflation, social conflict history.

---

### UNIT-COMPLIANCE — The Governance Auditor
**Mission**: Audit internal audit processes, controls, segregation of duties, and governance.

**Targets**: SoD violations, ghost controls, key-person dependency, audit trail gaps, change management without approval workflow, data integrity in master records, shared responsibility model gaps.
