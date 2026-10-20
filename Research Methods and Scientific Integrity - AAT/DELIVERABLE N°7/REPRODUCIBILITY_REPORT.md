# Reproducibility Report - Session 7
_Generated 2026-10-20 23:01 UTC_

## Environment
- Python: 3.13.16
- numpy: 2.5.3 | pandas: 3.0.5 | scikit-learn: 1.9.1 | scipy: 1.18.1
- Global RANDOM_STATE: 42
- Lab dataset (Exercises 1-3, 7-10): Wisconsin Breast Cancer (569 samples, 30 features)
- Model Card and Datasheet: MY THESIS (planned XGBoost classifier; SUNAT/Veritrade HS Chapter 48 imports, 2022-2026).
  The Model Card is prospective: the customs data are still being cleaned, so it reports no thesis results yet.

## Lab headline results (class dataset, measured in this run)
- Fancy model, test accuracy: 0.9580
- Tuned baseline, test accuracy: 0.9790
- Paired t-test over 10 seeds (fancy vs tuned baseline): p = 0.5414
- McNemar exact p (single test set): 0.3750
- Fancy bootstrap 95% CI: [0.9231, 0.9860]

## Artifacts in this bundle
- model_card.md - 9-section Model Card of my thesis model (Mitchell et al., 2019)
- datasheet.md - 7-section Datasheet of my customs dataset (Gebru et al., 2021)
- annex_iv_crosswalk.md - EU AI Act Annex IV gap analysis
- fig_compute_matched.png, fig_ablation_errorbars.png - figures

## Documentation scorecard
- Score: 8/8