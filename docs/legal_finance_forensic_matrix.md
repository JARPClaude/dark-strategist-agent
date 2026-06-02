# Legal & Finance Forensic Matrix (v3.6.0)
# Source: knowledge-work-plugins (legal + finance plugins)
# Scope: P03 Legal + P05 Financial domain variants
# Status: content-based reference (not version-stamped per dual-versioning rule)

This catalog documents the 25 forensic incorporations from `knowledge-work-plugins`
into the Legal (P03) and Financial (P05) variants in v3.6.0. Operational rows live
in the variants themselves; this file is the annotated provenance reference.

## Design invariant (NON-NEGOTIABLE)

The deterministic verdict (>=1 FATAL -> INVIABLE) is **unchanged**. Severity x Likelihood
is **non-binding prioritization metadata only** — it orders findings *within* a tier
and never escalates/de-escalates the binding 4-tier scale (FATAL / SERIOUS /
MODERATE / LATENT) nor the verdict. Only the Failure Catalog sets the binding tier.

## The 25 incorporations

| # | Area | Incorporation | DS landing | Binding? |
|---|------|---------------|-----------|----------|
| 1 | Legal | Severity x Likelihood metadata field | finding field + LG07 | No |
| 2 | Legal | Risk Score 1-25 -> intra-tier order (G/Y/O/R) | BLOCK 1 header | No |
| 3 | L01 | NDA embedded non-solicit not flagged | Catalog SERIOUS | Yes |
| 4 | L01/L03 | Non-compete without jurisdiction carveout | Catalog SERIOUS | Yes |
| 5 | L01 | Missing standard NDA carveouts | Catalog MODERATE | Yes |
| 6 | L01 | Material deviation vs playbook unjustified | Catalog SERIOUS | Yes |
| 7 | L06 | Mandatory regulatory approval absent | Catalog FATAL | Yes |
| 8 | L06 | Jurisdictional requirement unmapped to action | Catalog SERIOUS | Yes |
| 9 | L01 | Active vendor relationship without MSA | Catalog SERIOUS | Yes |
| 10 | L04 | Vendor processing PII without executed DPA | Catalog FATAL | Yes |
| 11 | L01 | Surviving obligation / expiration untracked | Catalog MODERATE | Yes |
| 12 | Finance | Price/Volume decomposition lens | FORENSIC lens + F05 | Yes |
| 13 | Finance | Rate/Mix decomposition lens | FORENSIC lens + F05 | Yes |
| 14 | Finance | Headcount/Compensation decomposition lens | FORENSIC lens + F05 | Yes |
| 15 | Finance | Spend Category decomposition lens | FORENSIC lens + F05 | Yes |
| 16 | Finance | Material variance without decomposition | RULE F05 / Catalog SERIOUS | Yes |
| 17 | Finance | Materiality threshold undeclared | RULE F06 / Catalog MODERATE | Yes |
| 18 | Finance | SOX material weakness in ICFR | RULE F07 / Catalog FATAL | Yes |
| 19 | Finance | SOX significant deficiency | RULE F07 / Catalog SERIOUS | Yes |
| 20 | Finance | SOX control deficiency | RULE F07 / Catalog MODERATE | Yes |
| 21 | Finance | Significant account without identified control | Catalog SERIOUS | Yes |
| 22 | Finance | GL-to-subledger account unreconciled | Catalog SERIOUS | Yes |
| 23 | Finance | Reconciling items without aging/categorization | Catalog MODERATE | Yes |
| 24 | Finance | GAAP presentation non-conformity (ASC 220/210/230) | Catalog SERIOUS | Yes |
| 25 | Finance | Severity x Likelihood metadata (cross-domain) | F08 + finding field | No |

## The 4 financial decompositions (RULE F05)

1. **Price / Volume** — Volume Effect = (Actual Vol - Budget Vol) x Budget Price;
   Price Effect = (Actual Price - Budget Price) x Actual Vol. Verify: Volume + Price = Total.
2. **Rate / Mix** — Rate = sum(Actual Vol_i x (Actual Rate_i - Budget Rate_i));
   Mix = sum(Budget Rate_i x (Actual Vol_i - Expected Vol_i at Budget Mix)).
3. **Headcount / Compensation** — Volume (HC) + Rate (avg comp) + Mix (level/dept shift).
4. **Spend Category** — fixed vs volume-driven cost split.

## SOX deficiency -> binding tier (RULE F07)

| SOX classification | DS tier |
|--------------------|---------|
| Material weakness | FATAL |
| Significant deficiency | SERIOUS |
| Control deficiency | MODERATE |

## Severity x Likelihood scoring (non-binding, RULE LG07 / F08)

Likelihood: 1 Remote / 2 Unlikely / 3 Possible / 4 Likely / 5 Almost Certain.
Risk Score = Severity(1-5) x Likelihood(1-5): 1-4 GREEN / 5-9 YELLOW / 10-15 ORANGE / 16-25 RED.
Used ONLY to order findings within a tier. The binding 4-tier scale and the deterministic verdict are unaffected.

## Discarded source skills (no forensic contact)

Legal: legal-response, signature-request, brief, meeting-briefing (operational/generative).
Finance: journal-entry, journal-entry-prep, close-management (operational).
