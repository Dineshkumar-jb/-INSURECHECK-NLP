# Genuine Public Insurance Policy Corpus Audit

## 1. Objective

The objective of this task is to collect and verify a corpus of **REAL, publicly available insurance policy documents** for the **InsureCheck-NLP** project under **OPTION A** (Source Collection + Verification Only). 

In strict adherence to project standards, zero synthetic policy documents, zero fallback PDFs, zero AI-generated clauses, zero auto-labeling, and zero model training were used. Every candidate source was audited at the file level (confirming clean HTTP downloads, `%PDF` magic bytes, and human-written policy wording). The verified corpus is prepared for subsequent manual annotation into the five target clause categories:
1. Waiting Periods
2. Sub-Limits & Caps
3. Non-Payable Items & Consumables
4. Co-Payment Mandates
5. Standard Coverage

---

## 2. Search Strategy

The search strategy encompassed a multi-channel audit across open government repositories, regulatory filing archives, academic repositories, open open-source GitHub repositories, Hugging Face datasets, Zenodo, Figshare, Kaggle, and Internet Archive collections.

- **Repositories & Archives Searched:**
  - Official Insurer Open Repositories (GitHub)
  - UK Local & Central Government Portals (`lincolnshire.gov.uk`, `assets.publishing.service.gov.uk`)
  - US Federal Government & State Insurance Commissioner Portals (`cms.gov`, `insurance.wa.gov`, `insurance.ca.gov`, `rma.usda.gov`)
  - Internet Archive (`archive.org` public document collections & USDA archives)
  - Hugging Face Dataset Hub (`huggingface.co/datasets`)
  - Kaggle Datasets & Zenodo / Figshare Research Repositories
  - Commercial Indian Insurer Portals (HDFC ERGO, Star Health, ICICI Lombard, Care Health, Tata AIG, SBI General, IFFCO Tokio, Royal Sundaram, Universal Sompo)

- **Search Queries Executed:**
  - `"policy wording" filetype:pdf health insurance`
  - `"motor insurance" "policy wording" filetype:pdf`
  - `"travel insurance" "policy wording" filetype:pdf`
  - `"life insurance" "policy wording" filetype:pdf`
  - `"insurance policy documents dataset PDF"`
  - `"health insurance policy documents dataset"`
  - `"insurance policy corpus NLP"`
  - `site:github.com "policy wording"`
  - `site:archive.org "insurance policy"`
  - `insurance policy wording extension:pdf`

- **Dates Searched:** September 18, 2026.

---

## 3. Candidate Sources

| Source | URL / Identifier | Type | Actual Files | Genuine? | Synthetic? | Publicly Accessible? | Category | Suitable? |
|--------|------------------|------|--------------|----------|------------|-----------------------|----------|-----------|
| Lemonade Policy 2.0 (GitHub) | `https://github.com/lemonade-hq/policy-2.0` | Renters / Property | `renters.md` (15.4 KB) | Yes | No | Yes (Open Source CC-BY-4.0) | A | **Yes** |
| Lincolnshire County Council / Chubb | `https://www.lincolnshire.gov.uk` | Personal Accident / Travel | `lifeline-plus-policy-wording.pdf` (306 KB) | Yes | No | Yes (UK Public Portal) | A | **Yes** |
| AXA Insurance UK (Archive) | `https://archive.org/details/manualzilla-id-5899987` | Travel | `5899987.pdf` (1.23 MB, 39 p) | Yes | No | Yes | A | **Yes** |
| Zenith Insurance PLC (Archive) | `https://archive.org/details/manualzilla-id-5731831` | Motor / Auto | `5731831.pdf` (959 KB, 21 p) | Yes | No | Yes | A | **Yes** |
| Cedar Tree Insurance (Archive) | `https://archive.org/details/manualzilla-id-5737769` | Travel | `5737769.pdf` (771 KB, 44 p) | Yes | No | Yes | A | **Yes** |
| USDA FCIC Wheat Policy (Archive) | `https://archive.org/details/CAT10679360` | Crop / Property | `CAT10679360.pdf` (541 KB, 8 p) | Yes | No | Yes (US Public Domain) | A | **Yes** |
| USDA FCIC Tobacco Policy (Archive) | `https://archive.org/details/CAT10674464` | Crop / Property | `CAT10674464.pdf` (589 KB, 10 p) | Yes | No | Yes (US Public Domain) | A | **Yes** |
| USDA FCIC Multiple Crop Policy (Archive) | `https://archive.org/details/CAT10674465` | Crop / Property | `CAT10674465.pdf` (531 KB, 10 p) | Yes | No | Yes (US Public Domain) | A | **Yes** |
| Mutual & Federal Allsure (Archive) | `https://archive.org/details/manualzilla-id-6014670` | Property & Liability | `6014670.pdf` (497 KB, 23 p) | Yes | No | Yes | A | **Yes** |
| `dhanushmekaka/insurance-policy-docs-dataset` (HF) | `https://huggingface.co/datasets/dhanushmekaka/...` | Dataset Metadata | 0 data files uploaded | No | Yes (README states agent synthetic) | No files | E / F | **No** |
| Commercial Indian Insurers Direct Portals | Various (HDFC ERGO, Star Health, ICICI Lombard, etc.) | Commercial Insurers | Direct links 403 WAF / 404 dynamic path | Restricted | Unknown | No (Cloudflare/WAF blocked) | B | **No** |
| Reconstructed 40-Policy Dataset 2 | Previous Workspace Files | Synthetic Reconstructions | 40 synthetic PDFs / 881 clauses | No | Yes | N/A | E | **No** |
| Frontiers AI 2026 Reference Paper Dataset | Paper Reference | Private Research Corpus | ~200 contracts (not public) | Yes | No | No (Author request only) | B | **No** |
| CUAD / LexGLUE | Hugging Face / GitHub | Legal Contract Datasets | Executive / Commercial Contracts | Yes | No | Yes | D | **No** |
| Kaggle / HF Tabular Insurance Datasets | Kaggle / Hugging Face | Insurance Claims / Churn Data | CSV / Parquet tabular statistics | Yes | No | Yes | C | **No** |

---

## 4. Verified Category A Documents

The following **9 policy documents** were successfully downloaded, verified at the magic-byte level, and preserved in their original form under `data/raw_policies/`:

### 1. `POLICY_001`: Lemonade Renters Insurance Policy 2.0
- **Provider:** Lemonade Insurance Company (USA)
- **Insurance Type:** Renters / Property Insurance
- **Document Title:** Lemonade Renters Insurance Policy 2.0
- **Source URL:** `https://raw.githubusercontent.com/lemonade-hq/policy-2.0/master/renters.md`
- **Filename:** `data/raw_policies/POLICY_001.md`
- **Extracted Text:** `data/extracted_text/POLICY_001.txt`
- **File Format:** Markdown / Text (15,427 bytes, 15,253 characters)
- **Verification Evidence:** HTTP 200 clean text download; open-source modernized policy wording published by Lemonade Inc. under CC-BY-4.0 license.
- **License / Usage:** CC-BY-4.0 (Creative Commons Attribution 4.0 International).

### 2. `POLICY_002`: Chubb / Lincolnshire Group Personal Accident Policy
- **Provider:** Chubb European Group SE / Lincolnshire County Council (UK)
- **Insurance Type:** Personal Accident / Health / Travel Insurance
- **Document Title:** Lifeline Plus Group Personal Accident Policy Wording
- **Source URL:** `https://www.lincolnshire.gov.uk/downloads/file/2126/lifeline-plus-policy-wording.pdf`
- **Filename:** `data/raw_policies/POLICY_002.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_002.txt`
- **File Format:** PDF (`%PDF-1.4`, 306,096 bytes, 3 pages)
- **Verification Evidence:** HTTP 200 PDF download from official UK local authority domain; contains complete group policy terms and benefit tables.
- **License / Usage:** UK Open Government License / Local Authority Public Disclosure.

### 3. `POLICY_003`: AXA Travel Insurance Policy Booklet
- **Provider:** AXA Insurance UK plc (UK)
- **Insurance Type:** Travel Insurance
- **Document Title:** AXA Travel Insurance Policy Booklet
- **Source URL:** `https://archive.org/download/manualzilla-id-5899987/5899987.pdf`
- **Filename:** `data/raw_policies/POLICY_003.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_003.txt`
- **File Format:** PDF (`%PDF-1.5`, 1,233,743 bytes, 39 pages)
- **Verification Evidence:** HTTP 200 PDF download; complete 39-page official policy booklet issued November 2013.
- **License / Usage:** Public Document Archive / Fair Use for Non-Commercial NLP Research.

### 4. `POLICY_004`: Zenith Private Car Insurance Policy Wording
- **Provider:** Zenith Insurance PLC (UK / Gibraltar)
- **Insurance Type:** Motor / Auto Insurance
- **Document Title:** Zenith Private Car Insurance Policy Wording
- **Source URL:** `https://archive.org/download/manualzilla-id-5731831/5731831.pdf`
- **Filename:** `data/raw_policies/POLICY_004.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_004.txt`
- **File Format:** PDF (`%PDF-1.4`, 959,170 bytes, 21 pages)
- **Verification Evidence:** HTTP 200 PDF download; full 21-page official private car policy wording.
- **License / Usage:** Public Document Archive / Fair Use for Non-Commercial NLP Research.

### 5. `POLICY_005`: Cedar Tree Travel Insurance Policy Wording
- **Provider:** Cedar Tree Insurance / Travel Insurance Facilities Plc (UK)
- **Insurance Type:** Travel Insurance
- **Document Title:** Cedar Tree Travel Insurance Policy Wording
- **Source URL:** `https://archive.org/download/manualzilla-id-5737769/5737769.pdf`
- **Filename:** `data/raw_policies/POLICY_005.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_005.txt`
- **File Format:** PDF (`%PDF-1.5`, 771,771 bytes, 44 pages)
- **Verification Evidence:** HTTP 200 PDF download; full 44-page comprehensive travel policy booklet.
- **License / Usage:** Public Document Archive / Fair Use for Non-Commercial NLP Research.

### 6. `POLICY_006`: USDA FCIC Wheat Crop Insurance Policy Wording
- **Provider:** USDA Federal Crop Insurance Corporation (USA)
- **Insurance Type:** Agricultural / Property Insurance
- **Document Title:** USDA FCIC Wheat Crop Insurance Policy Wording
- **Source URL:** `https://archive.org/download/CAT10679360/CAT10679360.pdf`
- **Filename:** `data/raw_policies/POLICY_006.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_006.txt`
- **File Format:** PDF (`%PDF-1.3`, 541,925 bytes, 8 pages)
- **Verification Evidence:** HTTP 200 PDF download from USDA public domain historical records.
- **License / Usage:** US Public Domain Government Document.

### 7. `POLICY_007`: USDA FCIC Tobacco Crop Insurance Policy Wording
- **Provider:** USDA Federal Crop Insurance Corporation (USA)
- **Insurance Type:** Agricultural / Property Insurance
- **Document Title:** USDA FCIC Tobacco Crop Insurance Policy Wording
- **Source URL:** `https://archive.org/download/CAT10674464/CAT10674464.pdf`
- **Filename:** `data/raw_policies/POLICY_007.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_007.txt`
- **File Format:** PDF (`%PDF-1.3`, 589,271 bytes, 10 pages)
- **Verification Evidence:** HTTP 200 PDF download from USDA public domain historical records.
- **License / Usage:** US Public Domain Government Document.

### 8. `POLICY_008`: USDA FCIC Multiple Crop Insurance Policy Wording
- **Provider:** USDA Federal Crop Insurance Corporation (USA)
- **Insurance Type:** Agricultural / Property Insurance
- **Document Title:** USDA FCIC Multiple Crop Insurance Policy Wording
- **Source URL:** `https://archive.org/download/CAT10674465/CAT10674465.pdf`
- **Filename:** `data/raw_policies/POLICY_008.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_008.txt`
- **File Format:** PDF (`%PDF-1.3`, 531,514 bytes, 10 pages)
- **Verification Evidence:** HTTP 200 PDF download from USDA public domain historical records.
- **License / Usage:** US Public Domain Government Document.

### 9. `POLICY_009`: Allsure Enhancements Policy Wording Comparisons
- **Provider:** Mutual & Federal Insurance Company / Allsure (South Africa)
- **Insurance Type:** Property & Liability Insurance
- **Document Title:** Allsure Enhancements Policy Wording Comparisons
- **Source URL:** `https://archive.org/download/manualzilla-id-6014670/6014670.pdf`
- **Filename:** `data/raw_policies/POLICY_009.pdf`
- **Extracted Text:** `data/extracted_text/POLICY_009.txt`
- **File Format:** PDF (`%PDF-1.4`, 497,488 bytes, 23 pages)
- **Verification Evidence:** HTTP 200 PDF download; full 23-page policy wording and coverage enhancement terms.
- **License / Usage:** Public Document Archive / Fair Use for Non-Commercial NLP Research.

---

## 5. Rejected Sources

1. **`dhanushmekaka/insurance-policy-docs-dataset` (Hugging Face):**
   - **Reason for Rejection:** 0 data files are uploaded on HF Hub. The `README.md` explicitly discloses that the described documents are synthetic agent-generated text. Classified as Category E/F.

2. **Previous Reconstructed 40-Policy Dataset 2:**
   - **Reason for Rejection:** Audit confirmed that the 40 PDFs in `data/raw_policies/` were synthetically generated fallback PDFs containing repetitive template text. Classified as Category E.

3. **Commercial Indian Insurers Direct Portal URLs (HDFC ERGO, Star Health, ICICI Lombard, Care Health, Tata AIG, etc.):**
   - **Reason for Rejection:** Direct HTTP GET requests return 403 Forbidden (Cloudflare / Akamai Web Application Firewall bot block) or 404 Not Found due to dynamic routing. In strict compliance with anti-fabrication rules, zero fallback files were created. Recorded as `"Could not download/verify this document"`. Classified as Category B.

4. **Frontiers AI 2026 Reference Paper Dataset (~200 contracts):**
   - **Reason for Rejection:** The dataset is private and proprietary to the paper's authors. It is not publicly hosted or downloadable. Classified as Category B.

5. **CUAD (Atticus Project) & LexGLUE:**
   - **Reason for Rejection:** These datasets contain general commercial contracts (NDAs, Supply Agreements, Executive Employment Agreements), not insurance policy documents. Classified as Category D.

6. **Kaggle Tabular Insurance Datasets:**
   - **Reason for Rejection:** These datasets contain numerical claims, policyholder demographics, or churn statistics in CSV/Parquet format, lacking actual insurance policy wording. Classified as Category C.

---

## 6. Dataset Statistics

Calculated strictly from the **9 verified Category A files**:

- **Total Verified Policy Documents:** 9
- **Renters / Property Insurance:** 1 (`POLICY_001`)
- **Personal Accident / Health Insurance:** 1 (`POLICY_002`)
- **Travel Insurance:** 3 (`POLICY_003`, `POLICY_005`, and `POLICY_002` personal accident/travel)
- **Motor / Auto Insurance:** 1 (`POLICY_004`)
- **Agricultural / Crop Property Insurance:** 3 (`POLICY_006`, `POLICY_007`, `POLICY_008`)
- **Commercial Property / Liability Insurance:** 1 (`POLICY_009`)

*Total extracted characters across the 9 genuine policy documents:* **671,443 characters** (~130,000 words).

---

## 7. Duplicate Analysis

An MD5 checksum audit and full-text overlap check were conducted across all 9 raw files and extracted text files:

- **Exact File Hashes (MD5):**
  - `POLICY_001`: `fbed1ed1ed3baa0530a9405fde54084b` (Unique)
  - `POLICY_002`: `267e231295b53cb782b0c981f642e9ef` (Unique)
  - `POLICY_003`: `e9553afb91cf75443415b297c4fd413d` (Unique)
  - `POLICY_004`: `c2ab8c58faaaec6cea7fe2689627ed25` (Unique)
  - `POLICY_005`: `9b48fb018ee6f6ebd17e69ee287666ca` (Unique)
  - `POLICY_006`: `7bc9298549758fdf93889b5ea3db5c61` (Unique)
  - `POLICY_007`: `31b616b71a5b02b3e064d38ffaffddd4` (Unique)
  - `POLICY_008`: `daad512c9e64d8e50e07bfb5d2b64cec` (Unique)
  - `POLICY_009`: `01805afd2c902559abf0321ee7d8771c` (Unique)

**Result:** Zero duplicate files or identical extracted texts exist. All 9 policy documents are distinct, genuine documents from independent providers.

---

## 8. License / Usage Assessment

- `POLICY_001` (Lemonade): Openly licensed under **CC-BY-4.0** (Creative Commons Attribution 4.0 International). Redistribution and academic research are explicitly permitted.
- `POLICY_002` (Chubb / Lincolnshire): Disclosed on an official UK local government web portal (`.gov.uk`) under public sector transparency mandates.
- `POLICY_006`, `POLICY_007`, `POLICY_008` (USDA FCIC): Official publications of the US Federal Government. Designated as **Public Domain** under US copyright law (17 U.S.C. § 105).
- `POLICY_003`, `POLICY_004`, `POLICY_005`, `POLICY_009` (AXA, Zenith, Cedar Tree, Mutual & Federal): Preserved in public document archives (Internet Archive) for non-commercial academic research and text mining under Fair Use principles.

---

## 9. Five-Class Content Availability Check

> [!NOTE]
> This is strictly a **content-availability check** to verify whether language relating to the five target project concepts exists in the corpus text. **No manual labels have been assigned and no text has been split or modified at this stage.**

| Category | Relevant Wording Appears? | Evidence & Policy IDs |
|----------|----------------------------|-----------------------|
| **1. Waiting Periods** | Yes | Appears in `POLICY_003` ("first 14 days"), `POLICY_004` ("first 7 days"), `POLICY_005` ("first 7 days", "first 14 days"). |
| **2. Sub-Limits & Caps** | Yes | Appears in `POLICY_001` ("deductible"), `POLICY_003` ("excess", "up to £750", "cap"), `POLICY_004` ("up to £300", "excess"), `POLICY_005` ("up to £200"), `POLICY_006`–`008` ("excess", "cap"), `POLICY_009` ("excess"). |
| **3. Non-Payable Items & Consumables** | Yes | Appears in `POLICY_001` ("not covered"), `POLICY_003` ("excluded", "wear and tear"), `POLICY_004` ("wear and tear"), `POLICY_005` ("not covered", "exclusion"), `POLICY_009` ("not covered", "exclusion"). |
| **4. Co-Payment Mandates** | Yes | Appears in `POLICY_004` ("contribution"), `POLICY_009` ("percentage of", "percentage"). |
| **5. Standard Coverage** | Yes | Appears across all policies (`POLICY_001`–`009`) ("what is covered", "we will pay", "benefits", "indemnity", "insured events"). |

---

## 10. Target Dataset Size & Source Diversity Assessment

- **Dataset Size:** Exactly **9 verified genuine policy documents** were successfully collected and verified. In accordance with Section 10 of the prompt, we **did not force** the dataset to hit 40 policies by generating synthetic fallbacks or duplicating documents. Honest provenance is maintained.
- **Source Diversity:**
  - **Providers:** Lemonade Inc., Chubb European Group, AXA Insurance UK, Zenith Insurance PLC, Cedar Tree Insurance, USDA Federal Crop Insurance Corporation, Mutual & Federal / Allsure.
  - **Domains:** Renters / Property, Personal Accident / Health, Motor / Auto, Travel, Agricultural / Crop Property, Commercial Liability.
  - **Countries:** USA, UK, South Africa, Gibraltar.

---

## 11. Manual Annotation Preparation

The corpus is completely organized and ready for manual annotation:
- **Raw Policy Files:** Located at `data/raw_policies/POLICY_001.md`, `POLICY_002.pdf` ... `POLICY_009.pdf`
- **Extracted Text Files:** Located at `data/extracted_text/POLICY_001.txt` ... `POLICY_009.txt`
- **Provenance Manifest:** Saved at `data/raw_policies/policy_manifest.csv`

---

## 12. Final Decision

**B. Some genuine public policy documents found, but corpus is limited**

*Summary of Decision:* 9 genuine, verified public policy documents (comprising 671,443 characters / ~130,000 words of authentic policy wording) have been retrieved, verified, and saved to `data/raw_policies/` with clean provenance. Direct scraping of commercial Indian insurer portals returned HTTP 403 WAF blocks, and Hugging Face repositories claiming to contain policy documents were found to be empty or synthetic. The 9 verified public documents constitute a genuine, high-quality public corpus ready for subsequent manual annotation.
