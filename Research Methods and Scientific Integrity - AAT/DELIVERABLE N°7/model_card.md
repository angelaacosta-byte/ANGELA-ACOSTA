# Model Card — Sustainable-Import Proxy Classifier (prospective, v0.1)

## Model details
- **Name / version:** Sustainable-Import Proxy Classifier (XGBoost), v0.1 — PROSPECTIVE, not yet trained
- **Owner / contact:** Angela Milén Acosta Ticona <angela.acosta@unmsm.edu.pe>, Doctoral Program in Deep Tech, AI & Emerging Technologies, UNMSM
- **Date:** 2026-10 (card written before modeling; will be updated when results exist)
- **Architecture:** XGBoost gradient-boosted trees on structured customs fields, explained with SHAP. Part of a pipeline: Isolation Forest (data-quality filter) -> K-Means (import profiles) -> XGBoost + SHAP (RQ2).
- **Thesis:** Sustainable Import Patterns in Peru's Paper Products Sector (2022–2026): explanatory sequential mixed methods
- **License:** Code: MIT (planned, as in my repro-lab repository). Data: restricted by Veritrade terms — UNKNOWN — to investigate.

## Intended use
- **Primary intended uses:** Research only: find which structured customs variables (HS subheading, origin, supplier, unit value, volume, frequency) are associated with a proxy-based sustainability label (RQ2, H2–H3).
- **Intended users:** The researcher, thesis advisor and committee; policy analysts reading AGGREGATED results (MINAM, SUNAT, MINCETUR, PRODUCE).
- **Out-of-scope / misuse:** NOT for accusing or sanctioning individual firms of greenwashing; NOT for customs risk selection or inspection decisions; NOT a sustainability certification; NOT transferable to other sectors or countries without re-validation.

## Factors
- **Relevant groups / conditions:** HS heading (4803, 4818, rest of Chapter 48); country of origin; supplier seen vs NEW in training; importer size; year (2022–2026); description language (Spanish vs English); free-text quality.
- **Evaluation factors:** Results will be disaggregated per class and per group above, never reported only as an overall average.
- **Known blind spot:** No environmental field exists in customs records, so true sustainability cannot be observed — only proxies.

## Metrics
- **Performance measures:** Primary: PR-AUC (sustainable class is expected to be a minority). Also F1, precision, recall and per-class recall. Accuracy is NOT used as a headline metric.
- **Decision thresholds:** Chosen on validation folds only, fixed before touching the 2026 test year.
- **Variation approach:** Mean ± std over 5 folds x 5 seeds; bootstrap 95% CI on the 2026 hold-out; paired corrected resampled t-test (Nadeau & Bengio, 2003) against each baseline.
- **Baselines (fair benchmark):** Majority class, logistic regression and random forest, each given the SAME tuning budget (same number of search trials) and the same features and splits as XGBoost.
- **Pre-registration:** H1–H4, the primary comparison (XGBoost vs logistic regression on PR-AUC) and numeric thresholds to be registered on OSF before modeling (protocol month 7).

## Evaluation data
- **Datasets:** Temporal hold-out: all 2026 declaration lines (full year available early 2027). Internal validation on 2022–2025 with StratifiedGroupKFold, grouped by supplier.
- **Why this split:** Random k-fold would put the same supplier in train and test: a supplier that always writes 'FSC' would be memorized (leakage).
- **Preprocessing:** Every step that learns from data (encoding, scaling, imputation, Isolation Forest) is fit on training folds only, inside a Pipeline.

## Training data
- **Datasets:** SUNAT / Veritrade import declaration lines, HS Chapter 48, 2022–2025 (see my Datasheet).
- **Label:** Binary: 'proxy-indicated sustainable' vs 'no sustainability wording found', built from certification (FSC, PEFC, ISO 14001) and recycled-content wording for a labeled subset; manual audit of a random sample with Cohen's kappa.
- **Features EXCLUDED (leakage control):** The description text and anything derived from it (it is the label's source); any value rectified after inspection; any HS rule used to build the label.
- **Known limitations:** One-directional label noise: certified paper without wording is labeled 'conventional'. Size of the labeled subset: UNKNOWN — to investigate (data cleaning in progress).

## Quantitative analyses
- **Overall results:** UNKNOWN — to investigate: no thesis model trained yet; raw customs data are being cleaned (October 2026).
- **Disaggregated results:** UNKNOWN — planned per-class and per-group tables (HS heading, origin, new vs seen supplier, year, language).
- **Planned ablation:** Remove one feature group at a time (HS subheading, origin, supplier, unit value, volume/frequency); run without the Isolation Forest filter; rebuild the label from certification-only and recycled-only wording. Report mean ± std and say which components do NOT help.
- **Planned stability check:** K-Means re-run with >= 10 seeds; only profiles that stay stable (adjusted Rand index) go to the interviews.

## Ethical considerations
- **Risks:** Reputational harm if a proxy label is read as proof of greenwashing; disclosure of commercially sensitive firm data; ecological fallacy when country-level regulation stands in for a shipment; automation bias in policy use.
- **Mitigations:** Aggregated or anonymized reporting only; no firm-level scores published; UNMSM ethics committee review; expert interviews (QUAL phase) judge each proxy; results presented as associations, not verdicts.

## Caveats and recommendations
- **Caveats:** A proxy is not sustainability; absence of wording is not evidence of conventional paper. Results apply only to Peru, HS Chapter 48, 2022–2026.
- **Recommendations:** Update this card with measured results, CIs and subgroup tables before any use; re-validate if SUNAT adds environmental fields to the import declaration; external validation before any transfer to other sectors.
