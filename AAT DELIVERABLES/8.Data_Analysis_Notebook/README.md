# Sustainable Import Patterns of Tissue Parent Rolls in Peru (2020–2025)

**Author:** Angela Milén Acosta Ticona — Doctoral program, UNMSM
**Paradigm:** Positivist (quantitative, retrospective, observational)
**Data source:** Veritrade (SUNAT customs import declarations), HS 4803.00.90, 4818.20, 4818.90, Jan 2020 – Dec 2025

## Problem
Peru's tissue converters import parent rolls (*bobinas*) and convert them locally into toilet paper, towels and napkins.
Customs records contain no environmental field, so it is unknown how much of this imported fibre is recycled or certified.
This project measures it with explicit, validated text proxies (FSC/PEFC/ISO 14001/Ecolabel, recycled fibre).

## Folder structure
| Path | Content |
|---|---|
| `Bobinas_Sustainability_Analysis.ipynb` | Full analysis (RQ1–RQ3, price test, validation sample, sensitivity) |
| `cleaning/limpieza_reglas.py` | Rule-based screening of parent rolls vs. finished products |
| `cleaning/build_clean.py` | Applies the rules + expert decisions and writes the audited workbook |
| `cleaning/decisiones_manuales.csv` | Documented expert decisions for ambiguous records |
| `data/` (not published) | Cleaned Veritrade file, commercially sensitive; MD5 listed below |
| `figures/`, `outputs/` | Figures and tables produced by the notebook |

## Reproduce
```bash
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute Bobinas_Sustainability_Analysis.ipynb
```
Expected MD5 of `data/bobinas_limpio.xlsx`: `f2d7e5e54cc455749e50e57bb96dbfea`. Seed = 42.
Two consecutive runs produce byte-identical tables in `outputs/`.

## Main results
* 2,994 parent-roll imports, 123.1 thousand tonnes, US$ 138.0 million FOB.
* Only 4.4% of records (2.2% of tonnage) carry a sustainability signal; no significant trend 2020–2025 (H5 not supported).
* Recycled-fibre parent rolls cost 12.9% less per kg than virgin ones, controlling for year, product and HS code.
* Six import profiles (K-Means); the sustainability signal differs strongly across them.
* XGBoost predicts the signal on 2025 data (PR-AUC 0.42 vs 0.04 baseline) but does not significantly beat logistic regression.

## Ethics
No human participants. Importer and supplier names are replaced by codes in all outputs. A proxy label is not proof that a firm is or is not sustainable.
