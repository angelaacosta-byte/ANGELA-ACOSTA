# Sustainable Import Patterns of Tissue Parent Rolls in Peru (2020–2025)
### A Machine Learning Analysis of Customs Import Records

**Author:** Angela Milén Acosta Ticona · Doctoral Program in Deep Tech, AI & Emerging Technologies, UNMSM
**Course:** Research Methods & Scientific Integrity in AI · Dr. Loveleen Gaur · 2026

## Problem
Peruvian converters import tissue parent rolls (*bobinas*) and convert them into toilet paper, towels and napkins for the local market.
Customs records have **no environmental field**, so it is unknown how much of this imported fibre is recycled or certified.
This study measures it from the import declarations themselves.

**Research question:** Which sustainable import patterns characterize Peru's imports of tissue parent rolls for local conversion between 2020 and 2025, and which customs variables predict proxy-indicated sustainable imports?
**Paradigm:** Positivist (quantitative, retrospective, observational).

## Data
* **Source:** Veritrade (SUNAT customs import declarations), HS 4803.00.90, 4818.20 and 4818.90, January 2020 – December 2025.
* **Cleaning:** 11,586 raw lines → 3,748 → **2,994 parent-roll records**, with written rules and documented expert decisions; each version fingerprinted (MD5).
* **Privacy:** the Veritrade files contain firm names and are not published; public files are anonymised.

## Contents by topic
| # | Topic | File / link |
|---|---|---|
| 1 | Research paradigm | [1.Research_Paradigm_Angela_Acosta.docx](1.Research_Paradigm_Angela_Acosta.docx) |
| 2 | Method selection (method-fit matrix) | [2.Method_Fit_Matrix_Angela_Acosta.docx](2.Method_Fit_Matrix_Angela_Acosta.docx) |
| 3 | Research protocol | [3.Research_Protocol_Angela_Acosta.docx](3.Research_Protocol_Angela_Acosta.docx) |
| 4 | Systematic review and PRISMA 2020 | [4.Systematic_Review_Angela_Acosta.docx](4.Systematic_Review_Angela_Acosta.docx) |
| 5 | Reproducible ML pipeline on my data (automated check, 20 seeds) | https://github.com/angelaacosta-byte/repro-lab-roll-paper |
| 6 | Reproducibility audit: DATE paper and my own data | [6.Reproducibility_Audit_My_Data](6.Reproducibility_Audit_My_Data) · DATE audit: https://github.com/angelaacosta-byte/date-repro-audit |
| 7 | Model card and datasheet | [7.Model_card.md](7.Model_card.md) · [7.Datasheet.md](7.Datasheet.md) |

## Main results so far
* Only **4.4%** of parent-roll records (2.2% of tonnage) declare recycled fibre or a certification; no significant trend 2020–2025.
* Recycled-fibre parent rolls cost about **13% less per kg** than virgin ones (controlling for year, product and HS code).
* Predictive model: PR-AUC 0.47 ± 0.02 over 20 seeds (base rate 0.04); XGBoost does not beat logistic regression.

## Pending
* Systematic review: add Web of Science and document the reason for each title/abstract exclusion.
* Two-rater validation of the sustainability proxy (Cohen's kappa) on 200 records.
