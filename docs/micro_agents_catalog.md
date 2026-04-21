# Micro-Agents Catalog — Dark Strategist v2.3.0

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
**Mission**: Audit financial strategies, trading algorithms, capital markets exposure (NYSE, Forex).

**Targets**:
- Overfitting of strategies to historical data
- Margin call scenarios and leverage exposure
- Flash crash and liquidity gap vulnerability
- Execution latency and slippage
- Sharpe ratio and risk-adjusted returns
- Maximum drawdown under adverse scenarios
- SEC/regulatory compliance for traded instruments

---

### UNIT-INQUISITOR — The Legal & Tax Enforcer
**Mission**: Audit tax, regulatory, and legal compliance in any jurisdiction.

**Targets**:
- Disguised tax evasion structures
- Expired or incomplete permits and licenses
- Regulatory sanctions and pending infractions
- Labor law violations and social security gaps
- Money laundering risk vectors (AML/KYC)
- Transfer pricing manipulation
- Jurisdictional conflicts and applicable law gaps

---

### UNIT-TECH — The Systems Auditor
**Mission**: Audit software architectures, AI models, cybersecurity, and digital systems.

**Targets**:
- Injection vulnerabilities (SQL, command, prompt)
- Data leakage and training data exposure
- Single point of failure (SPOF) in critical paths
- Security by obscurity instead of real security
- AI jailbreaking and adversarial attack vectors
- Vendor lock-in and third-party dependency risk
- Observability gaps (distributed tracing, logging)
- Scalability bottlenecks under load

---

### UNIT-BIO — The Field & Livestock Auditor
**Mission**: Audit operations in extractive, agroindustrial, and livestock sectors.

**Targets**:
- Climate variability risk (El Niño, droughts, floods)
- Biomass availability and sustainability
- Capture quotas and regulatory fishing limits
- Cold chain integrity and logistics gaps
- Social conflict and community blockade history
- Environmental permits and compliance
- Animal biosecurity and disease outbreak protocols
- Seasonal production cycles and cash flow gaps
- Biological commodity price exposure

---

### UNIT-MARKET — The Commercial Strategist
**Mission**: Audit market strategies, business models, competition, and commercial projections.

**Targets**:
- Demand assumptions without empirical validation
- Empty or outdated competitive analysis
- Unrealistic Customer Acquisition Cost (CAC)
- Single-channel dependency (organic only, one platform)
- Revenue projections without conversion model
- Market timing assumptions
- Pricing strategy under competitive pressure

---

### UNIT-GEO — The Geopolitical Analyst
**Mission**: Audit geopolitical, macroeconomic, and country risk context.

**Targets**:
- Legal instability and regulatory arbitrariness
- Exchange rate volatility and currency risk
- Expropriation or nationalization risk
- Political conflict and electoral cycle impact
- Infrastructure reliability (ports, roads, energy)
- Inflation and purchasing power erosion
- Social conflict and strike history
- Country risk rating changes

---

### UNIT-COMPLIANCE — The Governance Auditor
**Mission**: Audit internal audit processes, controls, segregation of duties, and governance.

**Targets**:
- Segregation of Duties (SoD) violations
- Ghost controls (documented but not enforced)
- Key-person dependency (single person controls critical process)
- Lack of transaction traceability
- Audit trail gaps
- Change management without approval workflow
- Data integrity in master records
- Shared responsibility model gaps (cloud/partner)
