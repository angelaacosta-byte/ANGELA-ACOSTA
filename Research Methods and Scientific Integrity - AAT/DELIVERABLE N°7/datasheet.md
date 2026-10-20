# Datasheet — Peruvian Paper Imports, HS Chapter 48, 2022–2026 (SUNAT / Veritrade)

## Motivation
- **Purpose:** Assembled for my doctoral thesis to study sustainable import patterns in Peru's paper sector. The source records were created by SUNAT for customs control and tax collection, not for research, which is why they contain no environmental variables.
- **Created by / funded by:** Extract assembled by Angela Milén Acosta Ticona (UNMSM) from SUNAT customs declarations, accessed through Veritrade. Self-funded doctoral research; Veritrade subscription budgeted at S/ 6,000 in the protocol.

## Composition
- **What instances represent:** One product line of an import customs declaration (DAM) under HS Chapter 48, 2022–2026.
- **Fields:** Date, HS subheading, commercial description (free text), country of origin, supplier, importer, FOB and CIF value (USD), net weight (kg), quantity and unit.
- **Number of instances:** UNKNOWN — to investigate: will be reported after de-duplication and cleaning, with the MD5 of each extract.
- **Labels:** None in the source. A proxy label ('proxy-indicated sustainable' vs 'no sustainability wording found') is constructed from the descriptions.
- **Sample vs population:** Intended to cover all Chapter 48 import lines in the period; Veritrade's coverage of SUNAT records is UNKNOWN — to investigate.
- **Missing data / gaps:** No environmental fields at all; inconsistent free text (Spanish/English, abbreviations); supplier names not standardized; year 2026 incomplete until early 2027.
- **Sensitive information:** Importer and supplier identities are commercially sensitive. Importers that are natural persons may be personal data under Peru's Law 29733 on personal data protection.

## Collection process
- **How collected:** Customs agents file the import declaration at clearance and SUNAT records it; I export the lines from Veritrade with HS Chapter 48 and date filters. Each export is logged with date, query parameters and MD5 hash.
- **Who wrote the descriptions:** Importers and customs agents, in free text, so wording quality varies by firm and agent.
- **Timeframe:** January 2022 – December 2026 (2026 added in protocol month 7).
- **Consent / ethics:** Administrative records, no human subjects. Reuse rights under Veritrade's terms: UNKNOWN — to investigate. Protocol submitted to the UNMSM ethics committee before fieldwork.

## Preprocessing / cleaning / labeling
- **Current status:** Raw extract on hand; cleaning in progress (October 2026).
- **Planned steps:** Harmonize HS codes to 10 digits; convert currency to USD and weight to kg; compute unit value (USD/kg); remove duplicates; normalize text (lowercase, accents, abbreviations); standardize supplier names; keyword dictionaries for FSC / PEFC / ISO 14001 / reciclado / recycled, validated on a manual sample with Cohen's kappa.
- **Anomalies:** Isolation Forest flags are reviewed and logged, never deleted silently; the filter is fit on training data only.
- **Raw data available:** The raw extract is kept read-only with its MD5; every cleaning step is code, so it can be re-run.

## Uses
- **Appropriate uses:** Research on AGGREGATED import patterns; replication of the method in other sectors or Latin American countries.
- **Should NOT be used for:** Identifying, ranking or sanctioning individual firms; customs risk targeting; sustainability certification claims; commercial intelligence on competitors.

## Distribution
- **How distributed:** Raw data will NOT be redistributed. I will share code, codebook, aggregated tables and a synthetic sample.
- **License / restrictions:** Veritrade terms of use apply — UNKNOWN — to investigate. Code under MIT.

## Maintenance
- **Maintainer:** Angela Milén Acosta Ticona (angela.acosta@unmsm.edu.pe).
- **Versioning:** Every extract is dated and fingerprinted (MD5), as in my repro-lab repository.
- **Update plan:** SUNAT rectifies declarations over time: re-extract, log the change, and update this datasheet at each version.
