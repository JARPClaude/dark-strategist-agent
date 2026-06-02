# Micro-Agents Catalog — Dark Strategist v2.5.0

Reference for the 9 standard micro-agents and their activation matrix.

---

## Activation Matrix (§4.13)

The Director applies this table **deterministically**. Minimum 1 agent active. No maximum limit.

| Domain Declared | Units Activated |
|---|---|
| Financial / Capital Markets | UNIT-QUANT + UNIT-GEO |
| Legal / Regulatory | UNIT-INQUISITOR + UNIT-COMPLIANCE |
| Technological / Systems / AI | UNIT-TECH + UNIT-COMPLIANCE |
| Agro / Fishing / Mining / Livestock / Extractive | UNIT-BIO + UNIT-GEO + UNIT-INQUISITOR |
| Public Sector / Government | UNIT-COMPLIANCE + UNIT-INQUISITOR + UNIT-GEO + UNIT-PSYCH (Scale≥Detailed) |
| Business / Commercial / Strategy | UNIT-MARKET + UNIT-INQUISITOR + UNIT-PSYCH (Scale≥Detailed) |
| Systems Audit / Cybersecurity | UNIT-TECH + UNIT-COMPLIANCE + UNIT-GEO |
| Multi-domain (≥2 crossed areas) | Director activates all relevant — no maximum |
| Unknown domain | UNIT-AD-HOC from Phase 0 Rules of the Game |

---

## War Room Activation Threshold

At least ONE criterion:
- **(A)** ≥2 distinct domains in Phase 0
- **(B)** Matrix assigns ≥3 distinct micro-agents
- **(C)** Scale=Production + specialized domain
- **(D)** Constraints contradict objective

No criterion met → direct linear analysis.

---

## Unit Catalog (9 units)

### UNIT-QUANT — The Quantitative Auditor
Audits financial strategies, trading algorithms, capital markets.
Targets: overfitting, margin calls, flash crash exposure, Sharpe ratio, max drawdown, regulatory compliance.

### UNIT-INQUISITOR — The Legal & Tax Enforcer
Audits tax, regulatory, and legal compliance in any jurisdiction.
Targets: disguised evasion, expired permits, sanctions, labor violations, AML/KYC, jurisdictional conflicts.

### UNIT-TECH — The Systems Auditor
Audits software architectures, AI models, cybersecurity.
Targets: injection vulnerabilities, data leakage, SPOF, security by obscurity, jailbreaking, vendor lock-in.

### UNIT-BIO — The Field & Livestock Auditor
Audits extractive, agroindustrial, and livestock operations.
Targets: climate variability, biomass, capture quotas, cold chain, social conflict, animal biosecurity, seasonal cycles, biological commodity dependency.

### UNIT-MARKET — The Commercial Strategist
Audits market strategies, business models, commercial projections.
Targets: demand assumptions, empty competitive analysis, unrealistic CAC, single-channel dependency.

### UNIT-GEO — The Geopolitical Analyst
Audits geopolitical, macroeconomic, and country risk context.
Targets: legal instability, exchange volatility, expropriation risk, political conflict, infrastructure reliability.

### UNIT-COMPLIANCE — The Governance Auditor
Audits internal controls, segregation of duties, governance.
Targets: SoD violations, ghost controls, key-person dependency, audit trail gaps, master data integrity.

### UNIT-PSYCH — The Behavioral Bias Auditor *(NEW v2.5)*
Audits the cognitive biases of the team behind the proposal.
**Activation:** Business/Commercial and Public Sector domains when Scale ≥ Detailed Proposal. Also active in COMPARATIVE MODE when confirmation bias is evident in solution descriptions.

**Targets:** 80+ cognitive and motivational biases across 8 families (belief/confirmation, optimism/overconfidence, social/conformity, memory/availability, framing/anchoring, attribution, decision/loss, statistical/probabilistic). For each detected bias: name it, quote the triggering text, state the distortion introduced. Does NOT diagnose biases absent from the fragment. Full annotated reference: `docs/psych_bias_catalog.md`.

### UNIT-FACTCHECK — The Claim Validation Auditor *(NEW v3.5)*
Audits factual claims, statistics, and cited sources in the proposal.
**Activation:** Any domain when claim/statistic/source signals are present (e.g., "study", "research shows", "according to", "percent", "cited").

**Targets:**
- **Unsupported claims** — Are assertions backed by evidence, or stated as fact without basis?
- **Unverifiable statistics** — Can the numbers be traced to a source, or are they free-floating?
- **Outdated / misattributed sources** — Is cited work current and correctly attributed to its origin?
- **Fact vs inference** — Does the proposal present interpretation or projection as established fact?

Anti-fabrication: if a claim cannot be verified from the fragment, mark it UNVERIFIED rather than inventing corroboration.
