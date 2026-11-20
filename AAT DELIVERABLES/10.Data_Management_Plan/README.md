# 10 · Data Management Plan and Legal Compliance Checklist

**Course:** Research Methods & Scientific Integrity in AI (Session 11, Responsible Data Management) · **Instructor:** Dr. Loveleen Gaur  
**Student:** Angela Milén Acosta Ticona · **Date:** 19 November 2026

Plan for the data of the Design Science study *Design of a Sustainable Sourcing Assistant from Customs Import Records*, built on **real customs records and a real company**. The completed course template is in [Session11_DMP_and_Compliance_Checklist_Angela_Acosta.docx](Session11_DMP_and_Compliance_Checklist_Angela_Acosta.docx).

## Part A · Data Management Plan

### 1. Data description

Secondary data: Peruvian customs import declarations (SUNAT) for HS 4803.00.90, 4818.20 and 4818.90, 2020–2025, licensed from Veritrade as Excel exports (20,303 rows; fields such as date, customs office, importer name and tax ID (RUC), supplier, origin, net kg, FOB/CIF value and commercial description). Written cleaning rules reduce them to 2,994 parent-roll declarations (dataset v1, MD5 f2d7e5e5…, frozen; v2 = 3,003 after expert correction), from which I derive a 15-variable model dataset (CSV), aggregated tables, code and model outputs. For the 2026 evaluation of the sourcing assistant I will also generate at least 8 weekly export–summary pairs, two-rater labels on 200 descriptions, and a SUS questionnaire plus interview notes from one purchasing manager at the case company (Empresa A).

### 2. FAIR compliance

Code, documents and aggregated results will be deposited in Zenodo through its GitHub integration, which assigns a DOI to each release; the GitHub repository (angelaacosta-byte/ANGELA-ACOSTA) stays as the working copy. Metadata follow DataCite/Dublin Core, and the existing Datasheet (Deliverable 7) serves as codebook; files are UTF-8 CSV/JSON, with Harmonized System codes and ISO 3166 country codes as shared vocabularies. Documents, code and aggregated results are released under CC BY 4.0; the real records cannot be redistributed (Veritrade license), so the metadata state exactly how to obtain them: HS codes, date range, the Veritrade query and the MD5 hash of each export.

### 3. Anonymization approach

Replacing importer names and RUCs with codes is pseudonymization, not anonymization: 95% of the records are unique on year + month + net kg, so anyone with Veritrade access could re-identify an importer. Because Veritrade's terms of use also forbid publishing individual transactions, no record-level file is released at all, not even a generalized one; only aggregated tables are published, and every cell must hold at least 5 records from at least 3 distinct importers (k = 5, with l = 3 on importer identity), otherwise it is suppressed. I prefer this threshold rule to differential privacy because the counts are already coarse; a per-importer table, if ever needed, would get Laplace noise with ε = 1. Utility cost: all analyses are run on the real records, but readers cannot rerun them from the public files; exact reproduction requires their own licensed Veritrade access, using the documented query and MD5 hashes.

### 4. Storage and backup

Raw Veritrade exports, Empresa A's internal data and participant forms live only in an encrypted VeraCrypt container (AES-256) on my password-protected laptop; Google Colab processes only pseudonymized files, and GitHub holds only code and aggregated results. Only I hold the key; my supervisor sees aggregated results on request. Backups follow the 3-2-1 rule: the laptop container, an encrypted external drive kept at home, and an encrypted copy in my institutional UNMSM Google Drive, refreshed weekly and at every data version (MD5 recorded).

### 5. Legal compliance

Ley 29733 and its Regulation DS 016-2024-JUS apply: most records concern companies, but one importer is a natural person (RUC beginning with 10, 4 records) and the two evaluation participants are individuals, so those are personal data; no sensitive data are processed. GDPR does not apply because no data subject is in the EU; European suppliers are legal entities and are not analysed as individuals. Processing pseudonymized files in Google Colab (US servers) is a cross-border transfer covered by the providers' data-processing terms and standard contractual clauses, and participants consent to it explicitly. Veritrade's terms of use (checked on 19 November 2026) forbid publishing individual transactions and allow aggregated analyses that cite Veritrade, so only aggregates are published; Empresa A authorized its use under that alias.

### 6. Sharing plan

Open (CC BY 4.0, Zenodo DOI): code, cleaning rules, aggregated tables that meet the 5-records / 3-importers rule, the model card and the datasheet, always citing Veritrade (based on SUNAT records) as the source. Not shared, not even on request: any record-level file, raw or pseudonymized, because Veritrade's license forbids redistributing individual transactions; importer names and RUCs; Empresa A's internal data; and identifiable participant data. Reviewers who need to reproduce exact results can obtain the same records with their own Veritrade access using the documented query, and check them against the published MD5 hashes.

### 7. Retention and disposal

Raw Veritrade exports, the code-to-importer key, Empresa A's data and signed consent forms are kept until five years after the thesis defense (planned for 2028) and deleted on 31 December 2033. Deletion means destroying the VeraCrypt containers and overwriting the drives (for example, cipher /w or DBAN), with the deletion logged; interview audio, if any, is deleted right after transcription. The aggregated public release and the code stay on Zenodo indefinitely.

## Part B · Legal compliance checklist

Derived from Ley 29733 and its Regulation DS 016-2024-JUS, GDPR and the CARE principles. Every item is a Yes or a justified N/A before new data are collected.

| # | Requirement | Answer | Evidence or justification |
|---|---|---|---|
| 1 | Lawful basis for processing is recorded (consent or legitimate interest). | **Yes** | Legitimate interest (scientific research) for licensed customs records; informed consent for the two evaluation participants. |
| 2 | Consent is specific, informed, and documented. | **Yes** | Written consent form (purpose, cloud processing, right to withdraw) signed by the purchasing manager and the second rater before the 2026 evaluation. |
| 3 | Sensitive data is identified (health, biometric, racial or ethnic origin). | **Yes** | Checked: no health, biometric or ethnic data; only firm-level trade records and work opinions. |
| 4 | Data minimization applied: only what the study needs is collected. | **Yes** | Only 3 HS codes and the fields the design requirements need; participants give SUS scores, task times and interview notes, no demographics. |
| 5 | Ley 29733 obligations are mapped to this project. | **Yes** | Mapped in DMP §5: one natural-person importer and the participants are personal data; ARCO rights honored on request. |
| 6 | GDPR applicability checked: are any data subjects in the EU? | **Yes** | No data subject is in the EU, so GDPR does not apply. |
| 7 | Cross-border transfer mechanism is in place if data leaves Peru. | **Yes** | Pseudonymized files are processed in Colab (US) under the provider's contractual clauses and participant consent; only aggregated results are published (GitHub, Zenodo). |
| 8 | Storage location, encryption, and access controls are defined. | **Yes** | VeraCrypt AES-256, single key holder, 3-2-1 backups (DMP §4). |
| 9 | Breach-response plan exists (notify the ANPD within 48 hours). | **Yes** | If personal data are exposed: contain, notify the ANPD within 48 hours, inform the persons affected and Empresa A, log the incident. |
| 10 | Retention period and secure-deletion date are defined. | **Yes** | Secure deletion on 31 December 2033 (DMP §7). |
| 11 | Data Protection Officer consulted if required. | **N/A** | Small-scale research with no sensitive or large-scale processing, so no DPO is required; ethics questions go to the UNMSM research ethics committee. |
| 12 | CARE principles applied for Indigenous-community data. | **N/A** | No Indigenous-community data: only customs records of companies and two adult professionals. |

## Key decisions

1. All analyses use the **real** Veritrade/SUNAT records; no synthetic data are used.
2. Removing importer names is **pseudonymization, not anonymization**: 95% of the records are unique on year + month + net kg, and the source data can be bought from Veritrade.
3. Veritrade's terms of use forbid publishing individual transactions, so **no record-level file is published**. Only aggregated results (at least 5 records from at least 3 importers per cell) are shared, citing Veritrade as the source.
