"""
Dark Strategist v3.2.0 — Catalogs
ROLE_CATALOG:      domain → agentes de rol + agentes forenses
SSM_CATALOG:       domain → personas para SSM
DOMAIN_MAP:        keywords → domain name
LEGAL_SUBAREA_MAP: keywords → legal sub-area (L01-L12)
LEGAL_SUBAREA_ROLES: legal sub-area → specialized rol + forense agents
REGIME_MAP:        regime → calibration
DOMAIN_TOOLS:      domain → available tools

v3.2.0: Added 5 new domains — Marketing, Operations, Human Resources,
        Strategy, Startup. Total: 20 domains (P01 General + P02-P15 + Medical + 5 new).
"""

# ─── ROLE CATALOG ─────────────────────────────────────────────────────────────

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
            "Opposing Counsel — reads document adversarially seeking exploitable gaps",
        ],
        "forense": [
            "Clause Forense — identifies unenforceable, ambiguous, or missing clauses",
            "Jurisdiction Forense — challenges choice of law and enforceability by jurisdiction",
            "Liability Forense — maps unlimited exposure and missing limitation clauses",
            "IP Forense — identifies ownership gaps, chain of title, and licensing risks",
            "Compliance Forense — audits regulatory framework adherence and reporting gaps",
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

    # ── NEW v3.2.0 ─────────────────────────────────────────────────────────────

    "Marketing": {
        "rol": [
            "Growth Marketer — presents CAC, ROAS and funnel assumptions",
            "Brand Manager — defends brand positioning and claim validity",
            "Paid Media Buyer — evaluates channel mix and budget allocation",
            "Target Customer — assesses relevance, trust and purchase intent",
        ],
        "forense": [
            "CAC Forense — validates attribution methodology and payback period",
            "Claim Forense — challenges unverifiable brand claims at scale",
            "Channel Forense — detects dangerous channel concentration and saturation risk",
        ]
    },

    "Operations": {
        "rol": [
            "Operations Director — presents process design and capacity plan",
            "Frontline Operator — assesses SOP executability in practice",
            "Supplier / Vendor — evaluates contract feasibility and SLA realism",
            "Logistics Partner — assesses last-mile and fulfillment assumptions",
        ],
        "forense": [
            "Bottleneck Forense — identifies hidden throughput constraints at scale",
            "SoD Forense — detects segregation of duties violations in critical processes",
            "Supplier Concentration Forense — challenges single-supplier dependency assumptions",
        ]
    },

    "Human Resources": {
        "rol": [
            "HR Director — presents talent strategy and compensation framework",
            "Employee Representative — assesses equity, fairness and policy clarity",
            "Line Manager — evaluates implementation realism and performance framework",
            "Labor Regulator — monitors legal compliance and protected class exposure",
        ],
        "forense": [
            "Pay Equity Forense — detects compensation gaps and discrimination exposure",
            "Culture Claim Forense — challenges unverifiable culture and value statements",
            "Policy Compliance Forense — audits HR policies against applicable labor law",
        ]
    },

    "Strategy": {
        "rol": [
            "Executive Proponent — presents strategic plan with optimistic framing",
            "Board Challenger — stress-tests assumptions and resource commitments",
            "Competitor — models likely response to strategic moves",
            "External Analyst — evaluates market positioning and moat durability",
        ],
        "forense": [
            "Assumption Forense — identifies the single assumption that invalidates the plan",
            "Mirror Imaging Forense — detects competitor analysis that models only current state",
            "Execution Gap Forense — challenges organizational capacity to deliver the strategy",
        ]
    },

    "Startup": {
        "rol": [
            "Founder — presents pitch with maximum optimism and vision",
            "VC Investor — evaluates return potential and exit path",
            "Customer — assesses real product-market fit signal",
            "Competing Startup — models aggressive market response",
        ],
        "forense": [
            "Unit Economics Forense — validates CAC, LTV, payback period methodology",
            "PMF Forense — challenges product-market fit claims against retention data",
            "Runway Forense — models burn rate against realistic revenue ramp scenarios",
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


# ─── LEGAL SUB-AREA MAP ───────────────────────────────────────────────────────

LEGAL_SUBAREA_MAP = {
    "vendor": "L01", "nda": "L01", "msa": "L01",
    "sow": "L01", "saas": "L01", "subscription": "L01",
    "merger": "L02", "acquisition": "L02", "due diligence": "L02",
    "board": "L02", "shareholder": "L02", "cap table": "L02",
    "employment": "L03", "termination": "L03", "severance": "L03",
    "non-compete": "L03", "worker": "L03", "classification": "L03",
    "gdpr": "L04", "dsar": "L04", "dpa": "L04",
    "pia": "L04", "ccpa": "L04", "data processing": "L04",
    "product launch": "L05", "marketing claim": "L05", "terms of service": "L05",
    "eula": "L05", "warranty": "L05",
    "regulatory filing": "L06", "gap analysis": "L06", "compliance framework": "L06",
    "ai governance": "L07", "ai assessment": "L07", "algorithmic": "L07",
    "ai vendor": "L07",
    "trademark": "L08", "patent": "L08", "fto": "L08",
    "dmca": "L08", "copyright": "L08", "oss": "L08",
    "demand letter": "L09", "claim chart": "L09", "deposition": "L09",
    "settlement": "L09", "litigation": "L09",
    "lease": "L10", "purchase agreement": "L10", "title": "L10", "zoning": "L10",
    "loan agreement": "L11", "covenant": "L11", "security instrument": "L11",
    "intercreditor": "L11",
    "government contract": "L12", "public tender": "L12", "rfp": "L12",
}

LEGAL_SUBAREA_LABELS = {
    "L01": "Commercial Legal", "L02": "Corporate / M&A Legal",
    "L03": "Employment Legal", "L04": "Privacy Legal",
    "L05": "Product Legal", "L06": "Regulatory Legal",
    "L07": "AI Governance Legal", "L08": "IP Legal",
    "L09": "Litigation Legal", "L10": "Real Estate Legal",
    "L11": "Finance Legal", "L12": "Public Regulatory Legal",
}

LEGAL_SUBAREA_ROLES = {
    "L01": {"rol": ["Vendor Party", "Buyer Party", "Procurement Officer"],
            "forense": ["Clause Forense", "Liability Forense", "IP Forense"]},
    "L02": {"rol": ["Acquiring Party", "Target Company", "Investment Banker"],
            "forense": ["Diligence Forense", "Liability Forense", "Valuation Forense"]},
    "L03": {"rol": ["Employer", "Employee / Worker", "Labor Regulator"],
            "forense": ["Classification Forense", "IP Forense", "Clause Forense"]},
    "L04": {"rol": ["Data Controller", "Data Subject", "Data Protection Authority"],
            "forense": ["Consent Forense", "Residency Forense", "Compliance Forense"]},
    "L05": {"rol": ["Product Team", "Consumer", "Regulatory Body"],
            "forense": ["Claims Forense", "Liability Forense", "ToS Forense"]},
    "L06": {"rol": ["Regulated Entity", "Regulator", "Compliance Officer"],
            "forense": ["Gap Forense", "Reporting Forense", "Jurisdiction Forense"]},
    "L07": {"rol": ["AI Developer", "AI User", "AI Regulator"],
            "forense": ["Bias Forense", "IP Forense", "Liability Forense"]},
    "L08": {"rol": ["IP Owner", "Licensee", "Competitor"],
            "forense": ["Title Forense", "Scope Forense", "Territory Forense"]},
    "L09": {"rol": ["Claimant", "Defendant", "Judge"],
            "forense": ["Jurisdiction Forense", "Evidence Forense", "Damages Forense"]},
    "L10": {"rol": ["Buyer", "Seller", "Regulatory Authority"],
            "forense": ["Title Forense", "Zoning Forense", "Liability Forense"]},
    "L11": {"rol": ["Lender", "Borrower", "Intercreditor Party"],
            "forense": ["Covenant Forense", "Priority Forense", "Default Forense"]},
    "L12": {"rol": ["Government Entity", "Bidder", "Oversight Body"],
            "forense": ["Procurement Forense", "Compliance Forense", "Integrity Forense"]},
}


# ─── SSM CATALOG ──────────────────────────────────────────────────────────────

SSM_CATALOG = {
    "Trading":          ["institutional_investor", "retail_trader", "financial_regulator",
                         "competing_fund_manager", "risk_manager"],
    "Legal":            ["opposing_counsel", "judge", "regulator",
                         "affected_third_party", "in_house_counsel"],
    "Financial":        ["venture_capitalist", "credit_analyst", "acquiring_cfo",
                         "minority_shareholder", "financial_press"],
    "Cloud":            ["cto", "security_lead", "enterprise_customer",
                         "data_privacy_regulator", "competing_saas_ceo"],
    "Code":             ["senior_engineer", "security_auditor", "product_manager",
                         "devops_lead", "junior_developer"],
    "Cybersecurity":    ["ciso", "compliance_officer", "penetration_tester",
                         "incident_responder", "regulator"],
    "Agriculture":      ["community_leader", "environmental_regulator", "commodity_buyer",
                         "seasonal_worker", "ngo_watchdog"],
    "Real Estate":      ["institutional_investor", "retail_buyer", "regulator",
                         "tenant", "competing_developer"],
    "Science":          ["peer_reviewer", "journal_editor", "funding_agency",
                         "replication_researcher", "science_journalist"],
    "Medical":          ["senior_clinician", "hospital_administrator", "patient_advocate",
                         "health_regulator", "medical_insurer"],
    "Media":            ["content_creator", "brand_advertiser", "platform_algorithm",
                         "competing_creator", "media_regulator"],
    "E-Commerce":       ["marketplace_platform", "end_consumer", "logistics_provider",
                         "competing_brand", "payment_processor"],
    "Telecom":          ["enterprise_customer", "spectrum_regulator", "infrastructure_sharer",
                         "competing_operator", "consumer_advocate"],
    "Public Sector":    ["political_opposition", "taxpayer", "state_auditor",
                         "international_monitor", "investigative_journalist"],
    # NEW v3.2.0
    "Marketing":        ["target_customer", "competing_brand", "platform_algorithm",
                         "media_buyer", "brand_safety_auditor"],
    "Operations":       ["frontline_operator", "supplier", "logistics_partner",
                         "regulatory_inspector", "competing_operator"],
    "Human Resources":  ["employee_representative", "labor_regulator", "job_candidate",
                         "line_manager", "competing_employer"],
    "Strategy":         ["board_member", "activist_shareholder", "competing_ceo",
                         "industry_analyst", "disruptive_entrant"],
    "Startup":          ["lead_investor", "enterprise_customer", "competing_startup",
                         "talent_candidate", "press_journalist"],
    "General":          ["skeptical_investor", "hostile_regulator", "cynical_employee",
                         "aggressive_competitor", "critical_press"],
}


# ─── DOMAIN MAP ───────────────────────────────────────────────────────────────

DOMAIN_MAP = {
    # Existing domains
    "chart": "Trading", "trading": "Trading", "xauusd": "Trading",
    "eurusd": "Trading", "backtest": "Trading",
    "contract": "Legal", "alquiler": "Legal", "legal": "Legal",
    "compliance": "Legal", "nda": "Legal", "msa": "Legal",
    "gdpr": "Legal", "dsar": "Legal", "trademark": "Legal",
    "employment": "Legal", "litigation": "Legal", "ai governance": "Legal",
    "finance": "Financial", "investment": "Financial",
    "valuation": "Financial", "ma": "Financial",
    "cloud": "Cloud", "saas": "Cloud", "paas": "Cloud", "iaas": "Cloud",
    "code": "Code", "architecture": "Code", "abap": "Code",
    "cyber": "Cybersecurity", "security": "Cybersecurity", "pentest": "Cybersecurity",
    "agro": "Agriculture", "livestock": "Agriculture", "harvest": "Agriculture",
    "real_estate": "Real Estate", "property": "Real Estate",
    "science": "Science", "research": "Science",
    "medical": "Medical", "clinical": "Medical", "health": "Medical",
    "media": "Media", "content": "Media",
    "ecommerce": "E-Commerce", "marketplace": "E-Commerce",
    "telecom": "Telecom", "spectrum": "Telecom",
    "public": "Public Sector", "government": "Public Sector",
    "procurement": "Public Sector",
    # NEW v3.2.0
    "marketing": "Marketing", "growth": "Marketing", "brand": "Marketing",
    "funnel": "Marketing", "advertising": "Marketing", "gtm": "Marketing",
    "operations": "Operations", "ops": "Operations", "supply_chain": "Operations",
    "logistics": "Operations", "sop": "Operations", "process": "Operations",
    "hr": "Human Resources", "human_resources": "Human Resources",
    "talent": "Human Resources", "compensation": "Human Resources",
    "culture": "Human Resources", "people": "Human Resources",
    "strategy": "Strategy", "strategic": "Strategy", "transformation": "Strategy",
    "competitive": "Strategy", "market_entry": "Strategy", "portfolio": "Strategy",
    "startup": "Startup", "pitch": "Startup", "deck": "Startup",
    "unit_economics": "Startup", "pmf": "Startup", "fundraising": "Startup",
    "seed": "Startup", "series_a": "Startup", "runway": "Startup",
}


# ─── REGIME MAP ───────────────────────────────────────────────────────────────

REGIME_MAP = {
    "standard":    {"depth": "full", "bias": "neutral",
                    "description": "Standard analysis — balanced perspective"},
    "adversarial": {"depth": "full", "bias": "hostile",
                    "description": "Maximum adversarial pressure — assume worst case"},
    "breakout":    {"depth": "full", "bias": "momentum",
                    "description": "High volatility / trend breakout — fast conditions"},
    "crisis":      {"depth": "full", "bias": "defensive",
                    "description": "Crisis conditions — capital preservation priority"},
    "regulatory":  {"depth": "full", "bias": "compliance",
                    "description": "Regulatory scrutiny — compliance-first lens"},
    "fast_track":  {"depth": "light", "bias": "neutral",
                    "description": "Rapid assessment — 4 levels, reduced scope"},
    "comparative": {"depth": "full", "bias": "comparative",
                    "description": "N≥2 solutions — cross-evaluation mode"},
}

DEFAULT_REGIME = REGIME_MAP["standard"]


# JURISDICTION CORPUS MAP (v3.8.0): domain -> corpus id under corpus/<id>.txt|.jsonl.
# Empty by default: RAG MECHANISM ships now; CONTENT populated later.
# Missing/None => retriever falls back to legacy [:N] feed (non-breaking).
JURISDICTION_CORPUS_MAP = {}


# ─── DOMAIN TOOLS ─────────────────────────────────────────────────────────────

DOMAIN_TOOLS = {
    "Trading":          ["price_action", "volume_profile", "order_flow",
                         "sharpe_ratio", "drawdown_analysis", "regime_detection"],
    "Legal":            ["clause_extraction", "jurisdiction_check", "sub_area_detection",
                         "liability_mapping", "enforceability_analysis", "ip_chain_audit"],
    "Financial":        ["dcf_analysis", "sensitivity_testing", "cac_ltv_ratio",
                         "burn_rate_analysis", "comparable_selection"],
    "Cloud":            ["architecture_review", "sla_analysis", "cac_ltv_ratio",
                         "vendor_lock_in_assessment", "dr_plan_check"],
    "Code":             ["static_analysis", "security_scanning", "complexity_check",
                         "test_coverage_review", "dependency_audit"],
    "Cybersecurity":    ["threat_modeling", "privilege_mapping", "sod_analysis",
                         "owasp_check", "audit_trail_review"],
    "Agriculture":      ["yield_benchmarking", "biosecurity_audit", "climate_modeling",
                         "cold_chain_review", "environmental_impact"],
    "Real Estate":      ["cap_rate_analysis", "dcf_real_estate", "zoning_verification",
                         "construction_cost_benchmark", "rate_sensitivity"],
    "Science":          ["power_analysis", "statistical_validity", "reproducibility_check",
                         "conflict_of_interest_audit", "methodology_review"],
    "Medical":          ["protocol_compliance", "adverse_event_review",
                         "regulatory_compliance", "consent_analysis", "liability_mapping"],
    "Media":            ["platform_dependency_analysis", "ip_ownership_check",
                         "cpm_modeling", "audience_ownership_review"],
    "E-Commerce":       ["unit_economics", "cac_ltv_ratio", "return_rate_modeling",
                         "marketplace_risk", "ad_spend_analysis"],
    "Telecom":          ["spectrum_verification", "capex_benchmarking",
                         "churn_modeling", "arpu_analysis", "vendor_concentration"],
    "Public Sector":    ["procurement_compliance", "budget_benchmarking",
                         "enforcement_mechanism_check", "stakeholder_mapping"],
    # NEW v3.2.0
    "Marketing":        ["cac_attribution_audit", "roas_validation", "funnel_math",
                         "channel_concentration_check", "claim_verifiability",
                         "ltv_cohort_analysis", "brand_differentiation_audit"],
    "Operations":       ["bottleneck_detection", "supplier_concentration_check",
                         "sop_executability_audit", "capacity_stress_test",
                         "sod_compliance", "lead_time_benchmarking"],
    "Human Resources":  ["pay_equity_analysis", "labor_law_compliance",
                         "culture_claim_validation", "performance_bias_detection",
                         "attrition_benchmarking", "sod_hr_audit"],
    "Strategy":         ["assumption_single_point_check", "mirror_imaging_detection",
                         "competitive_response_modeling", "scenario_planning",
                         "synergy_claim_validation", "execution_gap_analysis"],
    "Startup":          ["cac_ltv_payback", "pmf_retention_check",
                         "tam_methodology_audit", "runway_modeling",
                         "burn_rate_stress_test", "unit_economics_cohort"],
    "General":          ["logic_validation", "evidence_mapping",
                         "assumption_audit", "risk_identification"],
}


# ─── SKILLS CATALOG ───────────────────────────────────────────────────────────
# Active skills registered in the system

SKILLS_CATALOG = {
    "kac-assumption-audit":       "skills/kac-assumption-audit/SKILL.md",
    "ach-competing-explanations": "skills/ach-competing-explanations/SKILL.md",
    "deception-detection":        "skills/deception-detection/SKILL.md",
    "verdict-verification":       "skills/verdict-verification/SKILL.md",
    "adaptive-autonomous-drive":  "skills/adaptive-autonomous-drive/SKILL.md",  # NEW v3.2.0
    "context-degradation":        "skills/context-degradation/SKILL.md",  # NEW v3.7.0
}
