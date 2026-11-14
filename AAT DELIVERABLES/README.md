# Design of a Sustainable Sourcing Assistant from Customs Import Records
### A Design Science Study in a Peruvian Tissue-Paper Importer

**Author:** Angela Milén Acosta Ticona · Doctoral Program in Deep Tech, AI & Emerging Technologies, UNMSM
**Course:** Research Methods & Scientific Integrity in AI · Dr. Loveleen Gaur · 2026
**Paradigm:** Design Science Research (DSR), grounded in pragmatism · **Status:** in progress, Phases 1–2 complete

## Problem
Peruvian converters import tissue parent rolls (*bobinas*) and convert them into toilet paper, towels and napkins.
Importers buy customs data from commercial providers (Veritrade), but the exports mix parent rolls with other products, are cleaned by hand and give no price benchmark or sustainability information.
In the case company (**Empresa A**, one of the three largest importers out of 73), each summary takes at least one hour (about 65 per year), and none of its 185 import declarations in 2020–2025 carried a recycled-fibre or certification claim, against 4.7% in the rest of the market.

**Research question:** How can an artifact be designed that turns customs import records into decision support for an importer to buy tissue parent rolls at competitive prices and from more sustainable sources?

**The artifact:** a *sustainable sourcing assistant*. The user uploads a Veritrade export and downloads an Excel report that keeps only parent rolls for conversion, reads product type, grammage, recycled fibre and FSC/PEFC from the description, compares each price with similar imports and suggests origins with sustainable supply.

## Design Science phases (Peffers et al., 2007)
| Phase | Status | Where |
|---|---|---|
| 1. Problem identification | ✅ Done: diagnosis of 2,994 real declarations (2020–2025) and of the case company | [8.Data_Analysis_Notebook](8.Data_Analysis_Notebook), [3.Research_Protocol](3.Research_Protocol_Angela_Acosta.docx) |
| 2. Objectives | ✅ Done: requirements R0–R10 with thresholds fixed on 13 Nov 2026, before building | [3.Research_Protocol](3.Research_Protocol_Angela_Acosta.docx), Section 05 |
| 3. Design and development | ⏳ Next: artifact v1 in Google Colab | `9.Sourcing_Assistant` (to be added) |
| 4. Demonstration | ⏳ Pending | — |
| 5. Evaluation | ⏳ Technical evaluation of the engine done (topics 5–6); user evaluation pending | [5](5.Reproducible_ML_Pipeline), [6](6.Reproducibility_Audit_My_Data) |
| 6. Communication | ⏳ In progress | this repository |

## Contents by topic
| # | Topic | File / link |
|---|---|---|
| 1 | Research paradigm (Design Science Research) | [1.Research_Paradigm_Angela_Acosta.docx](1.Research_Paradigm_Angela_Acosta.docx) |
| 2 | Method selection (method-fit matrix: DSR 94/100) | [2.Method_Fit_Matrix_Angela_Acosta.docx](2.Method_Fit_Matrix_Angela_Acosta.docx) |
| 3 | Research protocol (Version 5, DSR; requirements R0–R10) | [3.Research_Protocol_Angela_Acosta.docx](3.Research_Protocol_Angela_Acosta.docx) |
| 4 | Systematic review and PRISMA 2020 (319 records → 37 studies) | [4.Systematic_Review_Angela_Acosta.docx](4.Systematic_Review_Angela_Acosta.docx) · every excluded record with its reason: [D4_Excluded_studies.xlsx](D4_Excluded_studies.xlsx) |
| 5 | Reproducible ML pipeline: the assistant's analytical engine (automated check, 20 seeds) | [5.Reproducible_ML_Pipeline](5.Reproducible_ML_Pipeline) · live check: https://github.com/angelaacosta-byte/repro-lab-roll-paper |
| 6 | Reproducibility audit: DATE paper and my own data | [6.Reproducibility_Audit_My_Data](6.Reproducibility_Audit_My_Data) · DATE audit: https://github.com/angelaacosta-byte/date-repro-audit |
| 7 | Model card and datasheet | [7.Model_card.md](7.Model_card.md) · [7.Datasheet.md](7.Datasheet.md) |

**Supporting material:** [8.Data_Analysis_Notebook](8.Data_Analysis_Notebook) — Phase 1 (problem diagnosis): the full positivist analysis of the market data, which also provides the assistant's components.

## Phase 1 results (diagnosis)
* Only **4.4%** of parent-roll declarations state recycled fibre or a certification; no significant trend 2020–2025.
* Recycled-fibre parent rolls cost about **13–15% less per kg** than virgin ones.
* Structured customs fields predict the sustainability label about 10 times better than chance: PR-AUC 0.47 ± 0.02 over 20 seeds (base rate 0.04); XGBoost does not beat logistic regression.
* None of the 37 studies in the systematic review uses the customs declaration as unit of analysis or offers a tool that turns customs records into sourcing decisions.

## Transparency note
The project started with a positivist design. After identifying a practical problem in the company where the researcher works as import assistant, it was reoriented to Design Science Research. The positivist study is kept as Phase 1, and the design requirements were fixed before the artifact was built. The researcher's dual role is declared as a conflict of interest and mitigated (Deliverable 3, Section 07). The company is called "Empresa A"; its own data and the raw Veritrade files are never published.

## Pending
* Build and evaluate artifact v1 (requirements R0–R10).
* Two-rater validation of the sustainability detector (Cohen's kappa) on 200 descriptions.
