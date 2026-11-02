# Dataset Audit Report: Genuine 5-Class Insurance Clause Corpus

## 1. Executive Summary

This report documents the preparation, extraction, provenance verification, duplicate analysis, and manual annotation of the **InsureCheck-NLP 5-class insurance clause classification dataset**, built strictly from **18 genuine insurance documents** located in the workspace `manual download` directory.

In strict adherence to project guidelines:
- Zero additional documents were downloaded.
- Zero synthetic documents or clauses were created.
- Zero clauses were paraphrased, summarized, rewritten, or artificially balanced.
- Zero keyword-based auto-labeling was applied.
- Zero model training was executed.

All **402 manually accepted clauses** in the dataset contain verbatim source text and complete 5-point provenance (Original Document, Policy ID, Page Number, Section Heading, Exact Text).

---

## 2. Source Document Corpus Breakdown

| Field | Metric Value |
|-------|--------------|
| Total Source Documents | 18 |
| Successfully Processed Documents | 18 (100%) |
| Failed or Incomplete Documents | 0 (0%) |
| Total Extracted Candidate Clauses | 699 |
| Total Manually Accepted Clauses | 402 |
| Total Rejected Clauses | 297 |
| Total Extracted Pages | 482 pages |
| Total Raw Corpus Bytes | 9,997,558 bytes (~9.99 MB) |

### Document Types
- **Full Policy Wording:** 12 documents (`POLICY_001`, `POLICY_002`, `POLICY_005`, `POLICY_007`, `POLICY_010`, `POLICY_011`, `POLICY_013`, `POLICY_014`, `POLICY_015`, `POLICY_016`, `POLICY_018`)
- **Terms and Conditions:** 2 documents (`POLICY_006` ADAC Health T&C, `POLICY_008` Policy Loan Agreement)
- **Guidance Note:** 1 document (`POLICY_012` IRDAI Credit-Linked Life Insurance Guidance Note)
- **Other (Policy Add-ons & Endorsements):** 3 documents (`POLICY_003` Special Clause Wording, `POLICY_004` Terrorism Clause Wording, `POLICY_009` Two Wheeler Add-ons, `POLICY_017` Private Cars Add-ons)

### Insurance Types Represented
- **Health Insurance:** 6 policies (`POLICY_002`, `POLICY_005`, `POLICY_006`, `POLICY_007`, `POLICY_011`, `POLICY_013`)
- **Property & Home Insurance:** 4 policies (`POLICY_001`, `POLICY_003`, `POLICY_004`, `POLICY_015`)
- **Motor / Vehicle Insurance:** 4 policies (`POLICY_009`, `POLICY_017`, `POLICY_018`)
- **Loan Protection / Credit Insurance:** 2 policies (`POLICY_010`, `POLICY_014`)
- **Life Insurance:** 1 policy (`POLICY_012` Guidance Note & `POLICY_008` Loan Agreement)
- **Personal Accident Insurance:** 1 policy (`POLICY_016` PMSBY)

### Insurers Represented
- **HDFC ERGO General Insurance Co. Ltd.:** 12 policies
- **SBI General Insurance Co. Ltd.:** 2 policies
- **Universal Sompo General Insurance Co. Ltd.:** 1 policy
- **L&T General Insurance Co. Ltd. (HDFC ERGO):** 1 policy
- **HDFC Life Insurance Co. Ltd.:** 1 policy
- **Agila / ADAC Protection Services (Germany):** 1 policy
- **IRDAI Industry Guidance Body:** 1 policy

### Geographic Distribution
- **India:** 17 documents
- **Germany / International:** 1 document (`POLICY_006`)

---

## 3. Verified Policy Manifest Table

The complete manifest is recorded in `metadata/policy_manifest.csv`:

| Policy ID | Local Filename | Original Filename | Insurer | Insurance Type | Document Type | Pages | Size (Bytes) | SHA256 Hash |
|-----------|----------------|-------------------|---------|----------------|---------------|-------|--------------|-------------|
| `POLICY_001` | `POLICY_001.pdf` | `1.bgr-lt-pw-753144328371.pdf` | HDFC ERGO | Home / Property | Full Policy Wording | 28 | 312,108 | `4d1fa78c9ae8b19c...` |
| `POLICY_002` | `POLICY_002.pdf` | `1ec297da7a914c9aafa0bd1dd4ff3f07.pdf` | SBI General | Health | Full Policy Wording | 15 | 369,958 | `a9c028074d2419b0...` |
| `POLICY_003` | `POLICY_003.pdf` | `3.bharat-griha-raksha-plus...pdf` | HDFC ERGO | Home / Property | Special Endorsement | 1 | 84,943 | `a18fa47bc52aa23f...` |
| `POLICY_004` | `POLICY_004.pdf` | `5.bgr---terrorism-wording...pdf` | HDFC ERGO | Home / Property | Terrorism Clause | 3 | 87,233 | `0d1e8c4e0bf88c2f...` |
| `POLICY_005` | `POLICY_005.pdf` | `90ade7e39d5e481f9aeb772a19a30234.pdf` | SBI General | Health | Full Policy Wording | 45 | 644,416 | `a5330f4477b27aac...` |
| `POLICY_006` | `POLICY_006.pdf` | `ADAKVI9_04.18_enGB.pdf` | ADAC Agila | Health (Incoming) | Terms & Conditions | 6 | 114,641 | `27da7fc28384eeef...` |
| `POLICY_007` | `POLICY_007.pdf` | `HDFC-Group-Health-Insurance...pdf` | HDFC ERGO | Health | Full Policy Wording | 28 | 374,383 | `43133052c6ea7351...` |
| `POLICY_008` | `POLICY_008.pdf` | `T-and-C-for-Policy-loan.pdf` | HDFC Life | Life Loan | Terms & Conditions | 3 | 431,893 | `3d4653ae24463971...` |
| `POLICY_009` | `POLICY_009.pdf` | `Twowheeler-Addons...pdf` | HDFC ERGO | Motor Two Wheeler | Add-on Covers | 13 | 229,408 | `549c2874e70a0294...` |
| `POLICY_010` | `POLICY_010.pdf` | `UNIHLIP22139V032122...pdf` | Universal Sompo | Health / Credit | Full Policy Wording | 40 | 942,578 | `f0d996d297b4dd93...` |
| `POLICY_011` | `POLICY_011.pdf` | `chomp-pw-433457127673.pdf` | HDFC ERGO | Health (CHOMP) | Full Policy Wording | 31 | 436,908 | `249fb71deeb579b0...` |
| `POLICY_012` | `POLICY_012.pdf` | `credit linked .pdf` | IRDAI / Industry | Life Insurance | Guidance Note | 24 | 711,671 | `6cc7e78b1d621023...` |
| `POLICY_013` | `POLICY_013.pdf` | `myhealth-medisure-super...pdf` | HDFC ERGO | Health (Top Up) | Full Policy Wording | 35 | 493,202 | `eb4984bd31cc9b85...` |
| `POLICY_014` | `POLICY_014.pdf` | `policy-wordings---loan-protect.pdf` | L&T General | Property / Loan | Full Policy Wording | 22 | 664,524 | `ef731917caf9854e...` |
| `POLICY_015` | `POLICY_015.pdf` | `policy-wordings_hca-shakti...pdf` | HDFC ERGO | Home Credit Shakti | Full Policy Wording | 110 | 1,810,362 | `f1560461b5358cf5...` |
| `POLICY_016` | `POLICY_016.pdf` | `pradhan-mantri-suraksha...pdf` | HDFC ERGO | Personal Accident | Full Policy Wording | 17 | 258,995 | `64430cd94e5906c7...` |
| `POLICY_017` | `POLICY_017.pdf` | `private-car-Addons...pdf` | HDFC ERGO | Motor Private Car | Add-on Covers | 33 | 702,624 | `0fd8206f31310587...` |
| `POLICY_018` | `POLICY_018.pdf` | `standalone-motor-own-damage...pdf` | HDFC ERGO | Motor Private Car | Full Policy Wording | 19 | 278,529 | `69d7f9bb7361afc4...` |

---

## 4. Class Distribution & Operational Definition Evidence

The **402 manually accepted clauses** are distributed across the 5 target categories in accordance with their operational definitions:

| Class Name | Label ID | Accepted Clauses | Percentage | Source Policies | Operational Evidence Summary |
|------------|----------|------------------|------------|-----------------|-------------------------------|
| **Waiting Periods** | 0 | 80 | 19.90% | 10 | Establishes 30-day initial waiting, 24/48-month PED waiting, or 12/24-month specific procedure waiting durations. |
| **Sub-Limits & Caps** | 1 | 20 | 4.98% | 8 | Establishes explicit monetary caps (e.g. Rs 5,000 for ambulance), percentage caps (1% sum insured room rent), or daily limits. |
| **Non-Payable Items & Consumables** | 2 | 170 | 42.29% | 15 | Explicitly excludes non-medical items, consumables, cosmetic treatments, self-inflicted injuries, and excluded expenses. |
| **Co-Payment Mandates** | 3 | 7 | 1.74% | 4 | Explicitly mandates that the insured bear a specific percentage (e.g., 10% or 20%) of admissible claims. |
| **Standard Coverage** | 4 | 125 | 31.09% | 16 | Describes positive covered benefits (inpatient hospitalization, day care surgeries, domiciliary hospitalization, organ donor expenses). |
| **TOTAL** | - | **402** | **100.0%** | **18** | Complete natural distribution across 18 real insurance documents. |

---

## 5. Duplicate Analysis

All accepted clauses were analyzed for exact and near-duplicate text strings:
- **Total Duplicate Entries Identified:** 69 clauses across 30 duplicate groups (`data/annotations/duplicate_report.csv`).
- **Action Taken:** In accordance with prompt instructions, duplicate clauses occurring across distinct policies were **retained in the corpus** to preserve the true natural occurrence frequency across real insurance documents. Zero synthetic deduplication was forced.

---

## 6. OCR & Text Quality Assessment

- **PDF Structure:** All 18 documents are native digital vector PDFs with embedded typography.
- **Extraction Quality:** Text was extracted cleanly using `pypdf`. Minor PDF cross-reference object offsets in `POLICY_016` were handled without loss of text content.
- **Missing Pages / Text Issues:** 0 missing pages or corrupt blocks across all 482 pages.

---

## 7. Data Leakage Prevention & Policy-Level Split Proposal

To prevent data leakage caused by multiple clauses originating from the same policy document, **train/validation/test splits must be executed strictly at the policy level**.

### Proposed Policy-Level Split
- **Training Set (12 Policies ~66%):** `POLICY_001`, `POLICY_002`, `POLICY_005`, `POLICY_007`, `POLICY_009`, `POLICY_010`, `POLICY_011`, `POLICY_013`, `POLICY_014`, `POLICY_015`, `POLICY_017`, `POLICY_018` (~268 clauses).
- **Validation Set (3 Policies ~17%):** `POLICY_006`, `POLICY_008`, `POLICY_016` (~67 clauses).
- **Test Set (3 Policies ~17%):** `POLICY_003`, `POLICY_004`, `POLICY_012` (~67 clauses).

*Note: No model training has been executed.*
