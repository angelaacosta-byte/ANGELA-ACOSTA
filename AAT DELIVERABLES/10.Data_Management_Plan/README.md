# 10 · Data Management Plan and Legal Compliance Checklist

**Course:** Research Methods & Scientific Integrity in AI (Session 11, Responsible Data Management) · **Instructor:** Dr. Loveleen Gaur  
**Student:** Angela Milén Acosta Ticona · **Date:** 19 November 2026

Plan for the data of the Design Science study *Design of a Sustainable Sourcing Assistant from Customs Import Records*. The completed course template is in [Session11_DMP_and_Compliance_Checklist_Angela_Acosta.docx](Session11_DMP_and_Compliance_Checklist_Angela_Acosta.docx).

## Part A · Data Management Plan

### 1. Data description

Secondary data: Peruvian customs import declarations (SUNAT) for HS 4803.00.90, 4818.20 and 4818.90, 2020–2025, licensed from Veritrade as Excel exports (20,303 rows; fields such as date, customs office, importer name and tax ID (RUC), supplier, origin, net kg, FOB/CIF value and commercial description). Written cleaning rules reduce them to 2,994 parent-roll declarations (dataset v1, MD5 f2d7e5e5…, frozen; v2 = 3,003 after expert correction), from which I derive a 15-variable model dataset (CSV), aggregated tables, code and model outputs. For the 2026 evaluation of the sourcing assistant I will also generate at least 8 weekly export–summary pairs, two-rater labels on 200 descriptions, and a SUS questionnaire plus interview notes from one purchasing manager at the case company (Empresa A).

### 2. FAIR compliance

Code and shareable data will be deposited in Zenodo through its GitHub integration, which assigns a DOI to each release; the GitHub repository (angelaacosta-byte/ANGELA-ACOSTA) stays as the working copy. Metadata follow DataCite/Dublin Core, and the existing Datasheet (Deliverable 7) serves as codebook; files are UTF-8 CSV/JSON, with Harmonized System codes and ISO 3166 country codes as shared vocabularies. Data are released under CC BY 4.0 and code under MIT, each with a README and the cleaning rules, so anyone can reuse them without contacting me.

### 3. Anonymization approach

Replacing importer names and RUCs with codes is pseudonymization, not anonymization: in the current public model file 95% of records are unique on year + month + net kg, and anyone who buys the same Veritrade data could re-identify the importer. The public release will therefore keep only year, origin and product type as quasi-identifiers (unit price rounded to US$ 0.05/kg, grammage in bands) and suppress every record whose group has fewer than k = 5 records or fewer than 3 distinct importers (l = 3 on importer identity, so no group exposes a single firm); this keeps 2,163 of 2,994 records (72%) and 78 of 133 sustainable ones. Published statistics follow the same rule (≥ 5 records and ≥ 3 importers per cell); I prefer this to differential privacy because the counts are already coarse, but a per-importer table would get Laplace noise with ε = 1. Utility cost: month, exact kg and FOB, customs office and importer codes disappear, so the PR-AUC of 0.47 can only be reproduced exactly with the restricted file (Section 6).

### 4. Storage and backup

Raw Veritrade exports, Empresa A's internal data and participant forms live only in an encrypted VeraCrypt container (AES-256) on my password-protected laptop; GitHub and Google Colab receive only pseudonymized or aggregated files. Only I hold the key; my supervisor sees aggregated results on request. Backups follow the 3-2-1 rule: the laptop container, an encrypted external drive kept at home, and an encrypted copy in my institutional UNMSM Google Drive, refreshed weekly and at every data version (MD5 recorded).

### 5. Legal compliance

Ley 29733 and its Regulation DS 016-2024-JUS apply: most records concern companies, but one importer is a natural person (RUC beginning with 10, 4 records) and the two evaluation participants are individuals, so those are personal data; no sensitive data are processed. GDPR does not apply because no data subject is in the EU; European suppliers are legal entities and are not analysed as individuals. Processing pseudonymized files in Google Colab and GitHub (US servers) is a cross-border transfer covered by the providers' data-processing terms and standard contractual clauses, and participants consent to it explicitly; Veritrade data are used within its license (no redistribution of raw exports), and Empresa A authorized its use under that alias.

### 6. Sharing plan

Open (CC BY 4.0, Zenodo DOI): code, cleaning rules, the generalized record-level file from Section 3, aggregated tables, synthetic demo data for the assistant, and the model card and datasheet. Restricted: the pseudonymized record-level file with exact values, shared only with reviewers or examiners for reproducibility under a signed data-use agreement (no re-identification, no redistribution) through Zenodo restricted access. Never shared: raw Veritrade exports, importer names and RUCs, Empresa A's internal data, and identifiable participant data.

### 7. Retention and disposal

Raw Veritrade exports, the code-to-importer key, Empresa A's data and signed consent forms are kept until five years after the thesis defense (planned for 2028) and deleted on 31 December 2033. Deletion means destroying the VeraCrypt containers and overwriting the drives (for example, cipher /w or DBAN), with the deletion logged; interview audio, if any, is deleted right after transcription. The anonymized public release and the code stay on Zenodo indefinitely.

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
| 7 | Cross-border transfer mechanism is in place if data leaves Peru. | **Yes** | Only pseudonymized or aggregated files leave Peru (Colab, GitHub, Zenodo), under the providers' contractual clauses and participant consent. |
| 8 | Storage location, encryption, and access controls are defined. | **Yes** | VeraCrypt AES-256, single key holder, 3-2-1 backups (DMP §4). |
| 9 | Breach-response plan exists (notify the ANPD within 48 hours). | **Yes** | If personal data are exposed: contain, notify the ANPD within 48 hours, inform the persons affected and Empresa A, log the incident. |
| 10 | Retention period and secure-deletion date are defined. | **Yes** | Secure deletion on 31 December 2033 (DMP §7). |
| 11 | Data Protection Officer consulted if required. | **N/A** | Small-scale research with no sensitive or large-scale processing, so no DPO is required; ethics questions go to the UNMSM research ethics committee. |
| 12 | CARE principles applied for Indigenous-community data. | **N/A** | No Indigenous-community data: only customs records of companies and two adult professionals. |

## Key decision

Removing importer names is **pseudonymization, not anonymization**: 95% of the records in the earlier public model file were unique on year + month + net kg, and the source data can be bought from Veritrade. The public release is therefore generalized and filtered to k = 5 records and at least 3 distinct importers per group (Part A, §3), and the exact pseudonymized file moves to restricted access (§6).
