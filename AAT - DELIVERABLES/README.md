# Reproducibility Audit · Part 2: My Own Data

**Thesis:** Sustainable Import Patterns of Tissue Parent Rolls in Peru (2020–2025): A Machine Learning Analysis of Customs Import Records
**Author:** Angela Milén Acosta Ticona · Doctoral Program in Deep Tech, AI & Emerging Technologies, UNMSM · Course: Research Methods & Scientific Integrity in AI (Dr. Loveleen Gaur)

**EN:** In Part 1 I audited a published paper (DATE, Kim et al., KDD 2020: https://github.com/angelaacosta-byte/date-repro-audit). Here I apply the same audit to **my own data and pipeline**: data versions, data quality, reproducible cleaning, anomaly stability, 20-seed stability, and the seeded vs unseeded test.
**ES:** En la Parte 1 audité un artículo publicado (DATE). Aquí aplico la misma auditoría a **mis propios datos**.

## Main findings · Hallazgos principales

| Check | Result |
|---|---|
| Data versions fingerprinted (MD5) | raw 11,586 → prefiltered 3,748 → final 2,994 records; all three hashes verified |
| Data quality (raw → final) | no duplicates, no invalid dates or HS codes; supplier missing in 27% (raw) and 48% (final) of records → supplier identity is not used as a predictor |
| Cleaning re-run from code | reproduces the final file **record by record** (2,968 kept by rules + 26 by documented expert decision) |
| Anomaly screen, 20 seeds | 59–60 records flagged per seed; mean Jaccard 0.76 → only the **39 records flagged by all 20 seeds** are treated as anomalies |
| Main model, 20 seeds | PR-AUC **0.4686 ± 0.0212** (base rate 0.0444), identical to the public repository `repro-lab-roll-paper` |
| Import profiles, 20 seeds | K-Means k = 6, adjusted Rand index 0.98 → very stable |
| Seeded vs unseeded (DATE lesson) | seed 42 run 5 times → identical; no seed → PR-AUC varies between runs |

![Result stability](figures/fig2_seed_stability.png)

## Files
| File | Content |
|---|---|
| `D6_Data_Quality_and_Reproducibility_Audit.ipynb` / `.html` | The audit, executed |
| `limpieza_reglas.py`, `decisiones_manuales.csv` | Cleaning rules and documented expert decisions (no firm names) |
| `figures/`, `outputs/` | Figures and tables produced by the notebook |

## Data
The three Veritrade files are commercially sensitive and are **not** published here. Their MD5 fingerprints are listed in Section 1 of the notebook; the anonymised feature table is public in https://github.com/angelaacosta-byte/repro-lab-roll-paper.

## Reproduce
Put `01_raw_veritrade.xlsx`, `02_prefiltered.xlsx` and `03_final_bobinas.xlsx` in `data/`, then `pip install -r requirements.txt` and *Run All*. Section 6 gives different numbers on every run **on purpose** (it shows what happens without a seed).
