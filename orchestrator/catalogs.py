"""
Dark Strategist v3.0.0 — Catalogs
ROLE_CATALOG:  domain → agentes de rol (simulan el entorno)
               domain → agentes forenses (auditan la simulación)
SSM_CATALOG:   domain → personas para Simulación Social Masiva
DOMAIN_MAP:    keywords → domain name (for runtime detection)
REGIME_MAP:    regime name → calibration adjustments
"""

# ─── ROLE CATALOG ─────────────────────────────────────────────────────────────
# Each domain has two lists:
#   "rol":    Agentes de Rol — simulate the domain environment
#   "forense": Agentes Forenses — audit what the rol agents produce

ROLE_CATALOG = {

    "Trading": {
        "rol": [
            "Institutional Market Participant — executes large orders, moves price",
            "Retail Trader — follows trends, adds noise and momentum",
            "Market Maker — provides liquidity, exploits spreads",
            "Algorithmic System — rule-based, reacts to signals",
            "Risk Manager — monitors exposure and drawdown limits",
        ],
        "forense": [
            "Quantitative Forense — audits statistical validity, detects overfitting",
            "Execution Forense — detects slippage assumptions and fill model errors",
            "Regime Forense — challenges whether strategy survives across market regimes",
        ]
    },

    "Legal": {
        "rol": [
            "Contracting Party A — seeks favorable terms",
            "Contracting Party B — seeks protection and clarity",
            "Regulatory Observer — monitors compliance with applicable law",
            "Third Party Affected — not a signatory but impacted by the document",
        ],
        "forense": [
            "Clause Forense — identifies unenforceable, ambiguous, or missing clauses",
            "Jurisdiction Forense — challenges choice of law and enforceability by jurisdiction",
            "Liability Forense — maps unlimited exposure and missing limitation clauses",
        ]
    },

    "Financial": {
        "rol": [
            "Optimistic Founder — presents best-case projections",
            "Conservative Analyst — stress-tests assumptions",
            "Debt Investor — prioritizes cash flow and covenants",
            "Equity Investor — prioritizes growth and exit multiples",
        ],
        "forense": [
            "Model Forense — detects circular references, hardcoded assumptions, terminal value dominance",
            "Assumption Forense — challenges revenue growth, margin, and CAC assumptions",
            "Sensitivity Forense — tests what happens when key variables move adversarially",
        ]
    },

    "Cloud": {
        "rol": [
            "SaaS Founder — pitches growth and retention metrics",
            "Enterprise Buyer — evaluates reliability, SLA, and lock-in risk",
            "DevOps Engineer — assesses operational feasibility",
            "Data Privacy Officer — evaluates residency and compliance posture",
        ],
        "forense": [
            "Architecture Forense — identifies SPOF, missing DR, single-AZ risks",
            "Unit Economics Forense — challenges CAC/LTV ratio and churn model",
            "Vendor Lock-in Forense — evaluates exit strategy and portability",
        ]
    },

    "Code": {
        "rol": [
            "Developer Author — explains design choices and trade-offs",
            "Peer Reviewer — reads code critically from a maintainability lens",
            "Security Auditor — looks for exploitable vulnerabilities",
            "Operations Engineer — evaluates deployability and observability",
        ],
        "forense": [
            "Security Forense — detects injection, auth gaps, hardcoded secrets",
            "Quality Forense — identifies god classes, dead code, missing tests",
            "Performance Forense — finds N+1 queries, blocking I/O, memory leaks",
        ]
    },

    "Cybersecurity": {
        "rol": [
            "Penetration Tester — actively probes for weaknesses",
            "System Owner — defends current architecture",
            "Compliance Officer — checks regulatory requirements",
            "Incident Responder — evaluates response readiness",
        ],
        "forense": [
            "Privilege Forense — maps escalation paths and excessive access",
            "Control Forense — identifies SoD violations and missing compensating controls",
            "Observability Forense — detects absent logging and audit trail gaps",
        ]
    },

    "Agriculture": {
        "rol": [
            "Agricultural Producer — presents production plan and yield assumptions",
            "Environmental Authority — evaluates permits and ecological impact",
            "Local Community Representative — assesses social license",
            "Commodity Buyer — evaluates supply reliability and quality",
        ],
        "forense": [
            "Biological Forense — challenges yield assumptions against regional benchmarks",
            "Climate Forense — tests plan against El Niño/La Niña scenarios",
            "Biosecurity Forense — identifies missing protocols and outbreak risk",
        ]
    },

    "Real Estate": {
        "rol": [
            "Developer — presents project economics and timeline",
            "Institutional Investor — evaluates returns and liquidity",
            "Regulatory Authority — reviews zoning and permits",
            "End Buyer / Tenant — evaluates value and risk",
        ],
        "forense": [
            "Valuation Forense — challenges cap rate, NOI, and comparable selection",
            "Construction Forense — tests cost assumptions against regional benchmarks",
            "Rate Sensitivity Forense — models what happens at +200bps interest rates",
        ]
    },

    "Science": {
        "rol": [
            "Principal Investigator — presents methodology and findings",
            "Peer Reviewer — evaluates scientific rigor",
            "Statistical Auditor — tests data and analysis validity",
            "Replication Skeptic — challenges reproducibility",
        ],
        "forense": [
            "Methodology Forense — identifies design flaws, underpowered studies, HARKing",
            "Statistical Forense — detects p-hacking, missing effect sizes, Type I/II errors",
            "Conflict of Interest Forense — evaluates undisclosed incentives and funding bias",
        ]
    },

    "Medical": {
        "rol": [
            "Clinician Author — presents clinical protocol or medical document",
            "Peer Clinician — reviews from clinical practice perspective",
            "Regulatory Reviewer — evaluates FDA/EMA/COFEPRIS compliance",
            "Patient Advocate — assesses safety and informed consent clarity",
        ],
        "forense": [
            "Clinical Forense — identifies protocol deviations and adverse event gaps",
            "Regulatory Forense — challenges compliance with applicable health regulation",
            "Liability Forense — maps medical liability exposure and consent validity",
        ]
    },

    "Media": {
        "rol": [
            "Content Creator — presents strategy and monetization model",
            "Platform Algorithm — evaluates engagement and distribution potential",
            "Brand Advertiser — assesses brand safety and audience fit",
            "Competing Creator — identifies replication and substitution risk",
        ],
        "forense": [
            "Platform Dependency Forense — detects single-platform revenue concentration",
            "IP Forense — identifies ownership gaps and licensing risks",
            "Audience Forense — challenges audience ownership and portability assumptions",
        ]
    },

    "E-Commerce": {
        "rol": [
            "Merchant — presents business model and unit economics",
            "Marketplace Platform — evaluates compliance and fee model",
            "End Consumer — assesses value, trust, and purchase intent",
            "Logistics Provider — evaluates fulfillment feasibility",
        ],
        "forense": [
            "Unit Economics Forense — challenges CAC > LTV and margin assumptions",
            "Platform Risk Forense — evaluates account suspension and ToS exposure",
            "Return Rate Forense — models impact of realistic return and chargeback rates",
        ]
    },

    "Telecom": {
        "rol": [
            "Operator — presents network rollout and business case",
            "Spectrum Regulator — evaluates license and compliance",
            "Enterprise Customer — assesses SLA and reliability",
            "Infrastructure Sharer — evaluates tower economics and competition",
        ],
        "forense": [
            "Spectrum Forense — challenges unconfirmed spectrum assumptions",
            "CapEx Forense — tests cost assumptions against engineering benchmarks",
            "Churn Forense — challenges ARPU and retention model realism",
        ]
    },

    "Public Sector": {
        "rol": [
            "Government Proponent — presents policy or budget proposal",
            "Political Opposition — challenges feasibility and intent",
            "Civil Society Observer — evaluates transparency and impact",
            "State Auditor — reviews procurement and budget compliance",
        ],
        "forense": [
            "Budget Forense — challenges revenue assumptions against historical trend",
            "Procurement Forense — identifies compliance gaps and conflict of interest",
            "Implementation Forense — tests operational feasibility against institutional capacity",
        ]
    },

    "General": {
        "rol": [
            "Proponent — presents the case favorably",
            "Skeptic — challenges assumptions and claims",
            "Neutral Observer — evaluates from an impartial perspective",
            "Affected Stakeholder — assesses impact from a third-party view",
        ],
        "forense": [
            "Logic Forense — detects circular reasoning, fallacies, and contradictions",
            "Evidence Forense — challenges unsupported claims and missing data",
            "Risk Forense — identifies unmodeled risks and unintended consequences",
        ]
    },
}


# ─── SSM CATALOG ──────────────────────────────────────────────────────────────
# Personas for Simulación Social Masiva — indexed by domain

SSM_CATALOG = {
    "Trading":      ["institutional_investor", "retail_trader", "financial_regulator",
                     "competing_fund_manager", "risk_manager"],
    "Legal":        ["opposing_counsel", "judge", "regulator",
                     "affected_third_party", "in_house_counsel"],
    "Financial":    ["venture_capitalist", "credit_analyst", "acquiring_cfo",
                     "minority_shareholder", "financial_press"],
    "Cloud":        ["cto", "security_lead", "enterprise_customer",
                     "data_privacy_regulator", "competing_saas_ceo"],
    "Code":         ["senior_engineer", "security_auditor", "product_manager",
                     "devops_lead", "junior_developer"],
    "Cybersecurity":["ciso", "compliance_officer", "penetration_tester",
                     "incident_responder", "regulator"],
    "Agriculture":  ["community_leader", "environmental_regulator", "commodity_buyer",
                     "seasonal_worker", "ngo_watchdog"],
    "Real Estate":  ["institutional_investor", "retail_buyer", "regulator",
                     "tenant", "competing_developer"],
    "Science":      ["peer_reviewer", "journal_editor", "funding_agency",
                     "replication_researcher", "science_journalist"],
    "Medical":      ["senior_clinician", "hospital_administrator", "patient_advocate",
                     "health_regulator", "medical_insurer"],
    "Media":        ["content_creator", "brand_advertiser", "platform_algorithm",
                     "competing_creator", "media_regulator"],
    "E-Commerce":   ["marketplace_platform", "end_consumer", "logistics_provider",
                     "competing_brand", "payment_processor"],
    "Telecom":      ["enterprise_customer", "spectrum_regulator", "infrastructure_sharer",
                     "competing_operator", "consumer_advocate"],
    "Public Sector":["political_opposition", "taxpayer", "state_auditor",
                     "international_monitor", "investigative_journalist"],
    "General":      ["skeptical_investor", "hostile_regulator", "cynical_employee",
                     "aggressive_competitor", "critical_press"],
}


# ─── DOMAIN MAP ───────────────────────────────────────────────────────────────
# Maps document type / subscenario keywords to canonical domain name

DOMAIN_MAP = {
    "chart":        "Trading",
    "trading":      "Trading",
    "xauusd":       "Trading",
    "eurusd":       "Trading",
    "backtest":     "Trading",
    "contract":     "Legal",
    "alquiler":     "Legal",
    "legal":        "Legal",
    "compliance":   "Legal",
    "finance":      "Financial",
    "investment":   "Financial",
    "valuation":    "Financial",
    "ma":           "Financial",
    "cloud":        "Cloud",
    "saas":         "Cloud",
    "paas":         "Cloud",
    "iaas":         "Cloud",
    "code":         "Code",
    "architecture": "Code",
    "abap":         "Code",
    "cyber":        "Cybersecurity",
    "security":     "Cybersecurity",
    "pentest":      "Cybersecurity",
    "agro":         "Agriculture",
    "livestock":    "Agriculture",
    "harvest":      "Agriculture",
    "real_estate":  "Real Estate",
    "property":     "Real Estate",
    "science":      "Science",
    "research":     "Science",
    "medical":      "Medical",
    "clinical":     "Medical",
    "health":       "Medical",
    "media":        "Media",
    "content":      "Media",
    "ecommerce":    "E-Commerce",
    "marketplace":  "E-Commerce",
    "telecom":      "Telecom",
    "spectrum":     "Telecom",
    "public":       "Public Sector",
    "government":   "Public Sector",
    "procurement":  "Public Sector",
}


# ─── REGIME MAP ───────────────────────────────────────────────────────────────
# Regime calibrates analysis intensity and framing

REGIME_MAP = {
    "standard":     {"depth": "full", "bias": "neutral",
                     "description": "Standard analysis — balanced perspective"},
    "adversarial":  {"depth": "full", "bias": "hostile",
                     "description": "Maximum adversarial pressure — assume worst case"},
    "breakout":     {"depth": "full", "bias": "momentum",
                     "description": "High volatility / trend breakout — fast conditions"},
    "crisis":       {"depth": "full", "bias": "defensive",
                     "description": "Crisis conditions — capital preservation priority"},
    "regulatory":   {"depth": "full", "bias": "compliance",
                     "description": "Regulatory scrutiny — compliance-first lens"},
    "fast_track":   {"depth": "light", "bias": "neutral",
                     "description": "Rapid assessment — 4 levels, reduced scope"},
    "comparative":  {"depth": "full", "bias": "comparative",
                     "description": "N≥2 solutions — cross-evaluation mode"},
}

DEFAULT_REGIME = REGIME_MAP["standard"]
