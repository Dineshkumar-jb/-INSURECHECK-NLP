# FINAL_INSURANCE_POLICY_SOURCE_AUDIT.md
## InsureCheck-NLP: Final Public Data Source Search & Provenance Audit Report

**Project Name:** InsureCheck-NLP  
**Course & Task:** Natural Language Processing (SWE1017) — Final Data Source Investigation  
**Audit Date:** September 18, 2026  

---

## 1. Objective

The objective of this final investigation is to conduct a broad, multi-platform search across open data repositories (**Hugging Face, GitHub, Kaggle, Zenodo, Figshare, UCI, university archives, and academic publications**) to determine whether an independently verifiable collection of **ACTUAL insurance policy documents / PDFs** exists that:
1. Contains genuine (non-synthetic) insurance policy text.
2. Is publicly accessible and downloadable.
3. Provides or can defensibly support our 5 target risk classification categories:
   - `Waiting Periods` (`LABEL2ID = 0`)
   - `Sub-Limits & Caps` (`LABEL2ID = 1`)
   - `Non-Payable Items & Consumables` (`LABEL2ID = 2`)
   - `Co-Payment Mandates` (`LABEL2ID = 3`)
   - `Standard Coverage` (`LABEL2ID = 4`)

### Strict Constraints Enforced:
- Zero data fabrication, paraphrasing, synthesis, or fallback PDF creation.
- Zero auto-annotation or class balancing.
- Zero model training executed (DistilBERT / DeBERTa).
- Preservation of all workspace files untouched.
- Direct file-level verification of candidate repositories.

---

## 2. Search Repositories & Search Queries

The search was executed across the following databases and search queries:

1. **Hugging Face Hub:** `site:huggingface.co/datasets "insurance policy" OR "insurance clause"`
2. **GitHub Repositories:** `site:github.com "insurance policy" "pdf" OR "txt" OR "json" corpus OR dataset`
3. **Zenodo & Figshare:** `site:zenodo.org OR site:figshare.com "insurance policy" OR "insurance contract"`
4. **Kaggle & UCI Machine Learning Repository:** `site:kaggle.com OR site:archive.ics.uci.edu "insurance policy"`
5. **15 Workspace Reference Papers (`REFERENCE PAPER/`):** Full-text scan of data availability statements and citations.

---

## 3. Candidate Datasets Classification Table

Every candidate dataset identified during the search was verified at the file level and classified into one of the 5 required categories:

- **Category A:** Genuine downloadable insurance-policy corpus (Real policy docs + public download + ground truth)
- **Category B:** Genuine insurance-policy corpus but not publicly downloadable (Author request / restricted)
- **Category C:** Insurance-related but not policy documents (Tabular claim, pricing, customer, fraud data)
- **Category D:** Legal contract dataset but not insurance-specific (CUAD, LexGLUE, LEDGAR)
- **Category E:** Synthetic / generated / reconstructed dataset

| Candidate Dataset | Actual Files Exist? | Real Insurance Docs? | Synthetic? | Provenance Verified? | License / Access | Downloadable? | Assigned Category |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **dhanushmekaka/insurance-policy-docs-dataset** | **No** *(0 data files on HF)* | **No** | **Yes** *(README states synthetic)* | **Not Verified** | MIT License | **No Data Files** | **E — Synthetic / Empty Repo** |
| **InsuranceRAG (`SIMPAC-2026-9`)** | **Yes** *(JSON / FAISS)* | **No** | **Yes** *(Synthetic JSON & QA)* | Verified Repo | MIT License | **Yes** | **E — Synthetic / QA Data** |
| **AWS Sample Policy Docs (`aws-samples`)** | **Yes** *(PDFs / TXT)* | **Partial** | **Partial** *(Sample UK booklets)* | Official AWS Repo | Apache 2.0 | **Yes** | **B — Corpus without 5-class labels** |
| **danielbeach/AiAgentPDFtoJSON** | **Yes** *(PDFs / JSON)* | **No** | **Yes** *(Fictional PDFs for LLM)* | Verified Repo | MIT License | **Yes** | **E — Fictional / Synthetic PDFs** |
| **CUAD (Contract Understanding Atticus Dataset)** | **Yes** *(510 PDFs)* | **No** *(Commercial)* | **No** | Verified Benchmark | CC BY 4.0 | **Yes** | **D — Legal Contract Dataset** |
| **LexGLUE (LEDGAR, EUR-Lex, CaseHOLD)** | **Yes** *(Parquet)* | **No** *(Legislation)*| **No** | Verified Benchmark | Open Access | **Yes** | **D — Legal NLP Dataset** |
| **Authors' Private 200-Contract Corpus (Frontiers 2026)** | **Yes** *(In research lab)*| **Partial** | **No** | Verified Paper Citation | Author Request Only | **No** | **B — Not Publicly Downloadable** |
| **Kaggle / UCI COIL 2000 Insurance Datasets** | **Yes** *(CSVs)* | **No** *(Tabular)* | **No** | Verified Benchmark | Open Access | **Yes** | **C — Insurance-Related (Tabular)** |

---

## 4. Detailed File-Level Verification Findings

### 1. `dhanushmekaka/insurance-policy-docs-dataset` (Hugging Face)
- **Direct File Check:** The Hugging Face repository contains `.gitattributes` and `README.md` only. **0 data files** (0 Parquet, 0 JSON, 0 CSV) are uploaded to the Hugging Face Hub.
- **Provenance Evidence:** The README explicitly documents: *"Methodology: Synthetic policy documents based on real insurance structures built using BDR Agent Factory v1."*
- **Category:** **E — Synthetic / Empty Repo**.

### 2. `InsuranceRAG` Codebase (`SIMPAC-2026-9` on GitHub)
- **Direct File Check:** Contains `decoded_questions.json` (question-answer pairs) and `synthetic policy dataset` indexed in FAISS.
- **Provenance Evidence:** Software publication (*Software Impacts* 2026) for QA/RAG assistance.
- **Category:** **E — Synthetic / QA Data**.

### 3. CUAD (Contract Understanding Atticus Dataset)
- **Direct File Check:** 510 commercial contracts, 13,682 human-annotated clauses across 41 commercial categories.
- **Provenance Evidence:** Hendrycks et al., *NeurIPS 2021*.
- **Category:** **D — Legal Contract Dataset (Not Insurance Specific)**.
- **5-Class Mapping Audit:** Commercial contracts contain no medical waiting periods, hospital consumable exclusions, or patient percentage co-payments.

### 4. Authors' Private 200-Contract Corpus (*Frontiers in AI 2026 Paper #14*)
- **Direct File Check:** Govea et al., *Frontiers in Artificial Intelligence*, Vol. 9, Art. 1782405 (March 2026).
- **Data Availability Statement (Page 19):**
  > *"Access to the curated private contract dataset (approx. 200 contracts) may be granted upon reasonable request to the corresponding author (`william.villegas@udla.edu.ec`), subject to legal and ethical constraints."*
- **Category:** **B — Genuine insurance/legal-policy corpus but not publicly downloadable**.

### 5. Kaggle / UCI COIL 2000 Insurance Datasets
- **Direct File Check:** CSV files containing customer age, BMI, smokers, charges, and caravan insurance ownership indicators.
- **Category:** **C — Insurance-related but not policy documents (Tabular Data)**.

---

## 5. Reference Paper Dataset Findings

Inspection of the 15 reference papers in `REFERENCE PAPER/` confirms:
- **No paper provides a direct, publicly downloadable 5-class consumer insurance clause dataset.**
- Reference papers either rely on public legal benchmarks (CUAD, LexGLUE, LEDGAR) or utilize private contract corpora restricted behind author access requests.

---

## 6. CUAD Compatibility Final Determination

| Target Insurance Category | CUAD Category Candidate | Compatibility Status | Evidence & Rationale |
| :--- | :--- | :--- | :--- |
| **1. Waiting Periods** | *None* | **NO VALID MAPPING** | Zero medical waiting period clauses exist in CUAD. |
| **2. Sub-Limits & Caps** | `Limitation of Liability` | **PARTIAL / INDIRECT ONLY** | Commercial liability caps $\neq$ 1% room rent daily caps or cataract caps. |
| **3. Non-Payable Consumables** | *None* | **NO VALID MAPPING** | Zero hospital consumable exclusion clauses exist in CUAD. |
| **4. Co-Payment Mandates** | *None* | **NO VALID MAPPING** | Zero patient percentage cost-sharing mandates exist in CUAD. |
| **5. Standard Coverage** | `Insurance Requirements` | **PARTIAL / INDIRECT ONLY** | Commercial insurance requirements $\neq$ inpatient hospitalisation coverage. |

**Conclusion:** CUAD **cannot** be used as a direct supervised training dataset for our 5-class insurance classification task.

---

## 7. Authenticity Verification of Workspace Dataset 2

- **Previous Audit Result:** Confirmed as `C. SYNTHETIC/PARTIALLY SYNTHETIC DATA` (881 clauses generated from 23 unique template text strings across 40 policy IDs due to network download timeouts in the builder script).
- **Current Action:** Retained as a synthetic baseline reference only. **Not used for ground-truth training.**

---

## 8. Final Finding Statement & Decision

$$\mathbf{B\ \text{—}\ No\ suitable\ public\ insurance-policy\ corpus\ found}$$

### Final Determination:
While public insurance text corpora (such as AWS sample booklets), public QA datasets (such as `InsuranceRAG`), and public legal benchmarks (such as `CUAD`) exist online, **no publicly accessible, independently verified dataset currently provides ground-truth annotations matching all 5 of our target insurance risk categories** (*Waiting Periods, Sub-Limits & Caps, Non-Payable Items & Consumables, Co-Payment Mandates, Standard Coverage*).

---

## 9. Stop Condition Status

- **Model Training Executed:** **0** (No DistilBERT or DeBERTa training performed).
- **Files Modified/Overwritten:** **0** (All workspace files preserved untouched).
- **Final Report Location:** [`FINAL_INSURANCE_POLICY_SOURCE_AUDIT.md`](file:///home/nullframe/Desktop/NLP/FINAL_INSURANCE_POLICY_SOURCE_AUDIT.md)

Execution is stopped and awaiting user direction.
