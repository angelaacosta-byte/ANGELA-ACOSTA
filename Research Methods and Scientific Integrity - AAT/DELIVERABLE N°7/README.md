# Deliverable N° 7 · Model Card + Datasheet (Session 7)

**Course:** Research Methods & Scientific Integrity in AI · Dr. Loveleen Gaur · UNMSM
**Student:** Angela Milén Acosta Ticona · COD. 26207270 · October 2026

**EN:** A Model Card (Mitchell et al., 2019) and a Datasheet (Gebru et al., 2021) for my doctoral thesis, *Sustainable Import Patterns in Peru's Paper Products Sector (2022–2026)*, plus the Session 7 benchmarking lab.
**ES:** Una Model Card y una Datasheet para mi tesis doctoral, más el laboratorio de benchmarking de la Sesión 7.

## Files · Archivos

| File | What it is |
|---|---|
| `Session7_HandsOn_Deliverable7_Angela_Acosta.ipynb` | The Session 7 notebook, executed. Lab exercises 1–3 and 7–10 on the class dataset, with my "Your turn" cells and answers at the end. Exercises 4–5 describe **my thesis**. |
| `model_card.md` | 9-section Model Card of my planned XGBoost classifier (**prospective**: no thesis model trained yet) |
| `datasheet.md` | 7-section Datasheet of my SUNAT / Veritrade import data, HS Chapter 48, 2022–2026 |
| `annex_iv_crosswalk.md` | EU AI Act Annex IV gap analysis of my Model Card (educational, not a conformity assessment) |
| `REPRODUCIBILITY_REPORT.md` | Environment, lab headline results and scorecard |
| `fig_compute_matched.png`, `fig_ablation_errorbars.png` | Lab figures |
| `session7_deliverable.zip` | Everything above in one file (Exercise 12) |

## Results in one table · Resultados en una tabla

| Check | Result |
|---|---|
| Documentation scorecard (Exercise 6) | **8/8** |
| Annex IV crosswalk (Exercise 11) | 2/6 covered; 4 gaps: data licence, labeled subset size, and no results yet (×2) |
| Lab: fancy model vs tuned baseline | −0.2 pts, paired t-test p = 0.54: no detectable difference |
| Lab: leakage on pure noise | +17.6 phantom accuracy points |

## Why the Model Card is prospective · Por qué la Model Card es prospectiva

**EN:** My customs data are downloaded but still being cleaned, so no thesis model exists yet. The card fixes the evaluation protocol in advance (PR-AUC, folds grouped by supplier, 2026 hold-out, equal tuning for all baselines, ablation plan) and marks every gap as `UNKNOWN — to investigate`. It reports **no invented results**. It will be updated when the model is trained.

**ES:** Mis datos aduaneros están descargados, pero aún se están limpiando, así que todavía no existe un modelo de la tesis. La tarjeta fija de antemano el protocolo de evaluación y marca cada vacío como `UNKNOWN — to investigate`. No reporta resultados inventados y se actualizará cuando el modelo esté entrenado.

## How to reproduce · Cómo reproducir

Open the notebook in Google Colab and run all cells (CPU, about 2 minutes). It writes every file listed above.
Abre el notebook en Google Colab y ejecuta todas las celdas; genera todos los archivos de arriba.

## References

- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92.
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. *Proceedings of FAT\* '19*, 220–229.
- Nadeau, C., & Bengio, Y. (2003). Inference for the generalization error. *Machine Learning, 52*, 239–281.
- Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex IV.
