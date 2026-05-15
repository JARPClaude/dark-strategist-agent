"""
Dark Strategist — SSM Persona Factory
Generates simulation personas based on document domain.
Version: 2.9.0

Each persona has:
  - role: who they are
  - profile: how they think
  - bias: their default inclination
  - objective: what they want
  - question: what they need answered before acting
  - stance: initial position (set after Round 1)
"""

from datetime import datetime


# ─── DOMAIN PERSONA SETS ──────────────────────────────────────────────────────

PERSONA_SETS = {

    "Trading": [
        {"role": "Institutional Investor", "profile": "Risk-averse, long horizon, regulated",
         "bias": "Skeptical of >3yr projections", "objective": "Preserve capital",
         "question": "Can I justify this to my investment committee?"},
        {"role": "Retail Trader", "profile": "Trend-follower, short horizon, emotional",
         "bias": "FOMO when trend is up, panic when down", "objective": "Quick returns",
         "question": "Is this better than what I'm already doing?"},
        {"role": "Financial Regulator", "profile": "Conservative, rule-bound, hostile to opacity",
         "bias": "Sees systemic risk in leverage", "objective": "Market stability",
         "question": "Does this comply with margin and reporting requirements?"},
        {"role": "Competing Fund Manager", "profile": "Analytical, competitive, protective of AUM",
         "bias": "Dismisses strategies that threaten his positioning",
         "objective": "Maintain competitive edge", "question": "Is this a real edge or curve fitting?"},
        {"role": "Risk Manager", "profile": "Quantitative, worst-case focused",
         "bias": "Always finds the tail risk", "objective": "Avoid blowup",
         "question": "What is the maximum drawdown scenario?"},
    ],

    "Legal": [
        {"role": "Opposing Counsel", "profile": "Adversarial, detail-oriented",
         "bias": "Every clause is a weapon for the other side", "objective": "Find exploitable gaps",
         "question": "Which clause do I attack first?"},
        {"role": "Judge", "profile": "Neutral, precedent-bound, impatient with ambiguity",
         "bias": "Disfavors poorly drafted agreements", "objective": "Apply the law clearly",
         "question": "Is this enforceable as written?"},
        {"role": "Regulator", "profile": "Rule-enforcer, conservative, hostile to gray areas",
         "bias": "Interprets ambiguity against the regulated party",
         "objective": "Compliance, not convenience", "question": "Does this meet the letter of the law?"},
        {"role": "Affected Third Party", "profile": "Aggrieved, motivated, seeks remedy",
         "bias": "Sees harm in everything that affects them",
         "objective": "Compensation or blocking", "question": "How does this hurt me?"},
        {"role": "In-house Legal Counsel", "profile": "Pragmatic, risk-conscious, cost-aware",
         "bias": "Prefers settlement over litigation", "objective": "Protect the company",
         "question": "What is our exposure if this fails?"},
    ],

    "Financial": [
        {"role": "Venture Capitalist", "profile": "Growth-focused, pattern-matcher, portfolio thinker",
         "bias": "Discounts capital-intensive models", "objective": "10x return",
         "question": "What is the path to exit?"},
        {"role": "Credit Analyst", "profile": "Conservative, cash flow focused",
         "bias": "Revenue is vanity, cash flow is sanity", "objective": "Loan repayment",
         "question": "Can they service the debt under stress?"},
        {"role": "CFO of potential acquirer", "profile": "Synergy-focused, integration-cost aware",
         "bias": "Skeptical of standalone projections", "objective": "Accretive deal",
         "question": "Does this improve our EBITDA post-integration?"},
        {"role": "Minority Shareholder", "profile": "Rights-conscious, dilution-sensitive",
         "bias": "Management always benefits at minority expense",
         "objective": "Protect economic rights", "question": "Am I getting diluted unfairly?"},
        {"role": "Financial Press", "profile": "Skeptical, narrative-seeking, public-interest oriented",
         "bias": "Scandal sells more than success", "objective": "Compelling story",
         "question": "What is the angle if this fails publicly?"},
    ],

    "Cloud": [
        {"role": "CTO", "profile": "Technical, architecture-focused, scalability obsessed",
         "bias": "Vendor lock-in is the enemy", "objective": "Technical excellence",
         "question": "Can we migrate off this if needed?"},
        {"role": "Security Team Lead", "profile": "Threat-modeling, compliance-aware",
         "bias": "Everything is a vulnerability until proven otherwise",
         "objective": "Zero breaches", "question": "Where is the attack surface?"},
        {"role": "Enterprise Customer", "profile": "Risk-averse, SLA-dependent, procurement-bound",
         "bias": "New vendors are a risk until proven otherwise",
         "objective": "Reliability and support", "question": "What is the SLA and who do I call at 3am?"},
        {"role": "Data Privacy Regulator", "profile": "GDPR/CCPA enforcer, data residency focused",
         "bias": "Data processing agreements are never complete enough",
         "objective": "Citizen data protection", "question": "Where is the data stored and who can access it?"},
        {"role": "Competing SaaS CEO", "profile": "Market share defensive, pricing aggressive",
         "bias": "Undercuts on price and over-promises on features",
         "objective": "Maintain market position", "question": "Can I match this feature set in 6 months?"},
    ],

    "E-Commerce": [
        {"role": "Marketplace Platform", "profile": "Fee-maximizing, rule-enforcing",
         "bias": "Suspends accounts that threaten their margins",
         "objective": "Platform health and revenue", "question": "Does this seller comply with our ToS?"},
        {"role": "End Consumer", "profile": "Price-sensitive, trust-dependent, review-driven",
         "bias": "One bad review kills the sale", "objective": "Value and reliability",
         "question": "Can I trust this brand I've never heard of?"},
        {"role": "Logistics Provider", "profile": "Capacity-constrained, margin-focused",
         "bias": "Overestimates its own capacity in peak season",
         "objective": "Profitable volumes", "question": "Can they sustain this volume without chargebacks?"},
        {"role": "Social Media Algorithm", "profile": "Engagement-maximizing, trend-sensitive",
         "bias": "Deprioritizes non-native content", "objective": "User retention on platform",
         "question": "Does this content keep users on my platform?"},
        {"role": "Competitor Brand", "profile": "Market-share defensive, aggressive on pricing",
         "bias": "Will undercut immediately if this gains traction",
         "objective": "Suppress new entrant", "question": "How fast can I respond to this threat?"},
    ],

    "Agriculture": [
        {"role": "Local Community Leader", "profile": "Land-protective, employment-focused",
         "bias": "Distrusts large external investors", "objective": "Community benefit",
         "question": "What happens to local jobs and land rights?"},
        {"role": "Environmental Regulator", "profile": "Permit-enforcing, impact-assessment focused",
         "bias": "Production plans underestimate environmental damage",
         "objective": "Environmental compliance", "question": "Has an EIA been completed and approved?"},
        {"role": "Commodity Buyer", "profile": "Quality-demanding, volume-reliability focused",
         "bias": "New suppliers always overpromise on yield",
         "objective": "Supply chain reliability", "question": "Can you guarantee volume and quality consistently?"},
        {"role": "Seasonal Agricultural Worker", "profile": "Employment-dependent, migrant, informal",
         "bias": "Large operations replace workers with machines",
         "objective": "Employment and fair wages", "question": "Will there still be work for me next season?"},
        {"role": "NGO / Environmental Watchdog", "profile": "Activist, media-connected, litigation-ready",
         "bias": "Any extraction project damages biodiversity",
         "objective": "Block or constrain the operation", "question": "What is the ecosystem damage?"},
    ],

    "Public Sector": [
        {"role": "Political Opposition", "profile": "Adversarial, media-savvy, vote-seeking",
         "bias": "Every government initiative is a scandal waiting to happen",
         "objective": "Political damage to governing party", "question": "Where is the corruption angle?"},
        {"role": "Citizen Taxpayer", "profile": "Value-for-money focused, cynical of government",
         "bias": "Public money is always wasted", "objective": "Lower taxes, better services",
         "question": "Is this worth my taxes?"},
        {"role": "State Auditor", "profile": "Process-focused, compliance-bound, public-interest",
         "bias": "Procurement irregularities are everywhere", "objective": "Accountability",
         "question": "Was this procured correctly and at fair market value?"},
        {"role": "International Monitoring Body", "profile": "Standards-enforcing, transparency-demanding",
         "bias": "Developing country governments hide cost overruns",
         "objective": "Good governance", "question": "Does this meet international transparency standards?"},
        {"role": "Investigative Journalist", "profile": "Source-cultivating, scandal-seeking",
         "bias": "Public projects always have a beneficiary who shouldn't benefit",
         "objective": "Front page story", "question": "Who personally benefits from this contract?"},
    ],

    "General": [
        {"role": "Skeptical Investor", "profile": "Pattern-matching, loss-averse",
         "bias": "Has seen this pitch before and it failed", "objective": "Capital preservation",
         "question": "Why will this work when similar attempts failed?"},
        {"role": "Hostile Regulator", "profile": "Rule-enforcing, conservative",
         "bias": "New = risky until proven otherwise", "objective": "Compliance",
         "question": "What rule does this break that hasn't been written yet?"},
        {"role": "Cynical Employee", "profile": "Change-resistant, job-protective",
         "bias": "Every new initiative means more work and no benefit",
         "objective": "Job security and routine", "question": "How does this make my life worse?"},
        {"role": "Aggressive Competitor", "profile": "Market-share defensive, fast-moving",
         "bias": "Will copy and undercut any successful feature",
         "objective": "Maintain dominance", "question": "How fast can I neutralize this?"},
        {"role": "Critical Press", "profile": "Narrative-seeking, public-interest claimed",
         "bias": "Success stories are boring; failure stories sell",
         "objective": "Compelling negative coverage", "question": "What is the failure scenario headline?"},
    ],
}

# Fallback for domains not explicitly mapped
DEFAULT_DOMAIN_MAPPING = {
    "Code": "General",
    "Cybersecurity": "General",
    "Real Estate": "Financial",
    "Science": "General",
    "Media": "E-Commerce",
    "Telecom": "Cloud",
    "Unknown": "General",
}


class PersonaFactory:
    """
    Generates simulation personas based on document domain.
    """

    def generate(self, domain: str, scale: str = "MESO") -> list:
        """
        Returns a list of persona dicts for the given domain and scale.
        Scale: MICRO (5-10), MESO (20), MACRO (50)
        """
        scale_counts = {"MICRO": 5, "MESO": 10, "MACRO": 20}
        target_count = scale_counts.get(scale, 10)

        # Get base personas for domain
        mapped_domain = DEFAULT_DOMAIN_MAPPING.get(domain, domain)
        base_personas = PERSONA_SETS.get(mapped_domain,
                        PERSONA_SETS.get(domain, PERSONA_SETS["General"]))

        # Expand to target count by cycling through base personas with variations
        personas = []
        for i in range(target_count):
            base = base_personas[i % len(base_personas)].copy()
            base["id"] = f"P{str(i+1).zfill(2)}"
            base["stance"] = "NEUTRAL"           # Set after Round 1
            base["coalition"] = None              # Set after Round 3
            base["action"] = None                 # Set after Round 4
            base["domain"] = domain
            personas.append(base)

        return personas

    def describe(self, personas: list) -> str:
        """Returns a readable summary of generated personas."""
        lines = [f"  P{p['id']}: {p['role']} — {p['objective']}" for p in personas]
        return "\n".join(lines)
