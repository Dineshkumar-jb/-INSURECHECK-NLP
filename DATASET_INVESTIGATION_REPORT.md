# DATASET_INVESTIGATION_REPORT.md
## InsureCheck-NLP: Investigation & Verification Report for Public Insurance-Policy Datasets

**Project Name:** InsureCheck-NLP  
**Course & Assessment:** Natural Language Processing (SWE1017)  
**Investigation Date:** September 18, 2026  

---

## 1. Objective

The objective of this investigation is to conduct an extensive, evidence-based search across public dataset repositories, academic databases, research paper supplements, and open-source codebases to locate an independently verifiable, publicly accessible dataset of **real insurance policy documents/clauses** that natively supports or can defensibly map to our 5 target risk classification categories:

1. **Waiting Periods** (`LABEL2ID = 0`)
2. **Sub-Limits & Caps** (`LABEL2ID = 1`)
3. **Non-Payable Items & Consumables** (`LABEL2ID = 2`)
4. **Co-Payment Mandates** (`LABEL2ID = 3`)
5. **Standard Coverage** (`LABEL2ID = 4`)

### Strict Constraints Enforced During Investigation:
- Zero data fabrication, paraphrasing, synthesis, or class auto-balancing.
- Zero model training executed (DistilBERT / DeBERTa).
- Preservation of all existing workspace files untouched.
- Strict empirical verification of every candidate URL and metadata claim.

---

## 2. Search Sources & Methodology

The following primary platforms, repositories, and academic archives were systematically queried:

1. **Hugging Face Hub:** Datasets under tags `insurance-policy`, `insurance-clause`, `health-insurance`, `legal-contracts`.
2. **GitHub Repositories:** Codebases and dataset releases associated with legal NLP and InsurTech publications.
3. **Kaggle Datasets:** Open datasets tagged with `insurance`, `policy`, `claims`, `contracts`.
4. **Zenodo & Figshare Archives:** Academic data repositories for legal/financial NLP benchmarks.
5. **15 Workspace Reference Papers (`REFERENCE PAPER/`):** Full-text inspection of data availability statements, citations, and supplementary material links.

---

## 3. Candidate Datasets Comparison Table

| Dataset Name | Candidate Category | Real Docs? | Public? | Pre-Annotated Labels? | Insurance Specific? | Downloadable? | 5-Class Compatibility |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **dhanushmekaka/insurance-policy-docs-dataset** | B. Insurance Corpus without Labels | **Yes** | **Yes** | **No** | **Yes** | **Yes** | **Not Directly Compatible** *(No 5-class labels)* |
| **InsuranceRAG Repo Data (`SIMPAC-2026-9`)** | D. Synthetic / QA Interaction Data | **No** | **Yes** | **No** | **Yes** | **Yes** | **Not Suitable** *(QA pairs / Synthetic JSON)* |
| **CUAD (Contract Understanding Atticus Dataset)** | C. Legal NLP (Not Insurance Specific) | **Yes** | **Yes** | **Yes** *(41 Legal Cats)* | **No** *(Commercial Contracts)* | **Yes** | **No Direct Mapping** *(Missing 3/5 insurance classes)* |
| **LexGLUE (LEDGAR, EUR-Lex, CaseHOLD)** | C. Legal NLP (Not Insurance Specific) | **Yes** | **Yes** | **Yes** *(Statutory/Provisions)*| **No** *(EU Legislation/Caselaw)* | **Yes** | **No Valid Mapping** |
| **Authors' Private 200-Contract Corpus (Frontiers AI 2026)** | B. Insurance/Legal Corpus | **Yes** | **No** | **Yes** | **Partial** *(Private Contracts)* | **No** *(Author Request Required)* | **Not Currently Accessible** |
| **Kaggle / Medical Insurance Datasets** | Rejected False Positive | **No** | **Yes** | **N/A** *(Tabular)* | **Yes** | **Yes** | **Not Suitable** *(Tabular Cost Data)* |

---

## 4. Detailed Candidate Verification & Evidence

### Candidate 1: `dhanushmekaka/insurance-policy-docs-dataset` (Hugging Face)
- **Source URL:** [huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset](https://huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset)
- **Classification:** **Category B: Existing insurance-policy corpus without labels**
- **Document Count:** Real policy text chunks extracted from consumer policy manuals for RAG systems.
- **Domains Represented:** Health Insurance, Life Insurance.
- **Public Accessibility:** Publicly accessible on Hugging Face Hub under open access.
- **Verification Status:** **Genuine Document Text Verified**; however, it lacks pre-existing ground-truth annotations matching our 5 target categories (*Waiting Periods, Sub-Limits, Consumables, Co-Pay, Coverage*).

### Candidate 2: `InsuranceRAG` Codebase & Data (*Software Impacts 2026*)
- **Source URL:** [github.com/SoftwareImpacts/SIMPAC-2026-9](https://github.com/SoftwareImpacts/SIMPAC-2026-9)
- **Paper Citation:** Hanmante et al., *Software Impacts* 28 (2026) 100844.
- **Classification:** **Category D: Synthetic / QA Interaction Dataset**
- **Contents:** `decoded_questions.json` (question-answer pairs for Indian health insurance terms) and `synthetic policy dataset` (`faiss_policy.index`).
- **Verification Status:** **Not Suitable** for sequence classification. Contains question-answering pairs and synthetic recommendation metadata, not clause-level ground truth.

### Candidate 3: CUAD (Contract Understanding Atticus Dataset)
- **Source URL:** [huggingface.co/datasets/atticus/cuad](https://huggingface.co/datasets/atticus/cuad)
- **Paper Citation:** Hendrycks et al., *NeurIPS 2021*.
- **Classification:** **Category C: Legal NLP dataset that is NOT specifically insurance**
- **Contents:** 510 commercial legal contracts with 13,682 human-annotated clauses across 41 categories.
- **Verification Status:** Publicly downloadable under CC BY 4.0. Contains commercial contracts (e.g., employment, mergers, software licenses), not consumer insurance policies.

### Candidate 4: Authors' Private 200-Contract Corpus (*Frontiers in AI 2026*)
- **Source Paper:** Govea et al., *Frontiers in Artificial Intelligence*, Vol. 9, Art. 1782405 (March 2026).
- **Classification:** **Category B: Private Legal/Contract Corpus**
- **Data Availability Statement (Page 19):**
  > *"Access to the curated private contract dataset (approx. 200 contracts) may be granted upon reasonable request to the corresponding author (william.villegas@udla.edu.ec), subject to legal and ethical constraints."*
- **Verification Status:** **Not Currently Publicly Accessible — Author Request Required.**

---

## 5. Reference Paper Findings

An empirical audit of all 15 reference papers in `REFERENCE PAPER/` confirms:
1. **No paper releases a pre-packaged, publicly downloadable 5-class insurance clause dataset.**
2. **Public Legal Benchmarks (CUAD, LexGLUE, LEDGAR):** Widely cited for legal text pre-training, but focused on general commercial contracts or EU statutory provisions.
3. **Private Contract Corpora:** Evaluated in recent literature (e.g., Govea et al. 2026), but held under restricted access requiring author permissions.

---

## 6. CUAD Compatibility Mapping Analysis

We evaluated whether CUAD's 41 commercial contract labels can be mapped to our 5 target insurance categories:

| Target Insurance Category | CUAD Category Candidate | Mapping Compatibility | Evidence & Rationale |
| :--- | :--- | :--- | :--- |
| **1. Waiting Periods** | *None* | **NO VALID MAPPING** | Commercial contracts contain no medical waiting period clauses. |
| **2. Sub-Limits & Caps** | `Limitation of Liability` | **PARTIAL / INDIRECT ONLY** | Commercial liability caps $\neq$ 1% room rent daily caps or cataract caps. |
| **3. Non-Payable Consumables** | *None* | **NO VALID MAPPING** | Commercial contracts contain no excluded hospital consumable items. |
| **4. Co-Payment Mandates** | *None* | **NO VALID MAPPING** | Commercial contracts contain no patient percentage cost-sharing mandates. |
| **5. Standard Coverage** | `Insurance Requirements` | **PARTIAL / INDIRECT ONLY** | Commercial liability insurance requirements $\neq$ inpatient hospitalisation cover. |

**Conclusion:** CUAD **cannot** serve as a direct supervised training dataset for our 5-class insurance classifier without creating invalid label mappings.

---

## 7. Categorized Candidate Recommendations

- **Directly Compatible (5-Class Pre-Annotated):** **None Found** *(No pre-existing public dataset provides ground-truth labels for all 5 specific insurance categories).*
- **Potentially Usable After Annotation:** 
  - [`dhanushmekaka/insurance-policy-docs-dataset`](https://huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset) *(Contains real insurance policy text chunks; requires manual/verified clause annotation).*
- **Auxiliary Legal-Domain Dataset:** 
  - [`atticus/cuad`](https://huggingface.co/datasets/atticus/cuad) *(Useful for legal domain pre-training/embeddings, but not for direct 5-class evaluation).*
- **Not Suitable:** 
  - Kaggle tabular insurance cost datasets, InsuranceRAG synthetic QA datasets, LexGLUE statutory texts.

---

## 8. Provenance & Authenticity Check of Current Workspace Dataset 2

The previous audit of the local reconstructed Dataset 2 (`data/dataset2_policy_manifest.csv` and `data/dataset2_clauses_all.json`) revealed:
- **Total Clauses:** 881
- **Unique Text Strings:** 23
- **Repetition:** The 23 unique text strings were repeated 38–40 times across 40 policy IDs because live HTTP downloads timed out during script execution, invoking a fallback template function (`generate_authentic_policy_wording_text`).
- **Authenticity Determination:** Classified strictly as **`C. SYNTHETIC/PARTIALLY SYNTHETIC DATA`**. It will **not** be treated as real-world ground truth.

---

## 9. Final Finding

> **"No publicly accessible, independently verified dataset matching all five target classes was identified."**

While public insurance policy text corpora exist (such as Hugging Face's `insurance-policy-docs-dataset`) and public legal contract benchmarks exist (such as `CUAD`), **no pre-packaged public dataset currently provides verified ground-truth labels for all 5 of our target insurance risk categories** (*Waiting Periods, Sub-Limits & Caps, Non-Payable Items & Consumables, Co-Payment Mandates, Standard Coverage*).

---

## 10. Stop Condition & Summary

- **Model Training Executed:** **0** (No DistilBERT or DeBERTa training performed).
- **Files Modified/Overwritten:** **0** (All workspace files preserved untouched).
- **Current Status:** Stopped after dataset investigation and reporting, awaiting user review and direction.
