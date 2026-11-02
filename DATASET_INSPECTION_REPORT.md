# DATASET_INSPECTION_REPORT.md
## InsureCheck-NLP: Inspection & Provenance Verification Report for `dhanushmekaka/insurance-policy-docs-dataset`

**Dataset Name:** `dhanushmekaka/insurance-policy-docs-dataset`  
**Repository URL:** [huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset](https://huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset)  
**Publisher:** BDR AI Organization  
**Inspection Date:** September 18, 2026  
**Local Storage Path:** `data/external/insurance_policy_docs_original/`  

---

## 1. Dataset Identity

- **Dataset Identifier:** `dhanushmekaka/insurance-policy-docs-dataset`
- **Hugging Face Hub URL:** `https://huggingface.co/datasets/dhanushmekaka/insurance-policy-docs-dataset`
- **Original Citation / Publisher:** BDR AI Organization (*Insurance Policy Documents Dataset*, 2025)
- **Pretty Name:** Insurance Policy Documents Dataset
- **License:** MIT License
- **Intended Use Case:** RAG-based knowledge systems, policy QA, and clause retrieval evaluation

---

## 2. Source and Provenance Analysis

An empirical inspection of the Hugging Face repository revealed the following critical findings:

1. **Repository Files:** The Hugging Face repository contains **only two metadata files**:
   - `README.md` (4.2 KB)
   - `.gitattributes` (2.5 KB)
   - **Data Files Uploaded:** **0 data files** (No Parquet, JSON, CSV, or PDF data splits exist in the Hugging Face Hub commit history).
2. **Dataset Creation Methodology (from `README.md`):**
   > *"Methodology: Synthetic policy documents based on real insurance structures"*  
   > *"Built using BDR Agent Factory v1"*  
   > *"Limitations: Synthetic documents may not capture all legal nuances; simplified regulatory language"*
3. **Provenance Determination:** **"Provenance not independently verified."**  
   The repository does not host raw real-world policy PDFs from commercial insurers; its README describes a synthetic generation methodology for RAG testing.

---

## 3. File Structure & Local Preservation

The original repository files were downloaded unchanged and stored separately in:
📁 `data/external/insurance_policy_docs_original/`

```text
data/external/insurance_policy_docs_original/
├── .gitattributes   (2,460 bytes)
└── README.md        (4,200 bytes)
```

**Zero existing workspace files** (`train_clauses.json`, `test_clauses.json`, `build_dataset2.py`, or model training code) were modified or overwritten.

---

## 4. Actual Dataset Counts

- **Total Data Records Uploaded on HF Hub:** **0**
- **Available Splits:** None (`EmptyDatasetError`)
- **Total Parquet / JSON Files:** **0**
- **Document IDs:** Specified in README schema, but no data records exist in the repository.

---

## 5. Available Metadata & Schema (from `README.md`)

The README defines a target JSON schema for insurance documents:

```json
{
  "document_id": "string",
  "document_type": "policy | endorsement | exclusion | clause",
  "policy_category": "motor | medical | property | life",
  "document_metadata": {
    "version": "string",
    "effective_date": "date",
    "expiry_date": "date",
    "jurisdiction": "string",
    "policy_number": "string"
  },
  "content": {
    "full_text": "string",
    "sections": [
      {
        "section_id": "string",
        "title": "string",
        "content": "string",
        "clauses": ["string"]
      }
    ]
  }
}
```

---

## 6. Representative Original Text Samples

Excerpt from `README.md` outlining intended document coverage:

```text
# Use Cases:
1. Policy Question Answering: Answer questions about coverage, exclusions, and terms with cited clauses.
2. Clause Conflict Detection: Identify contradictions between policies, endorsements, and exclusions.
3. Version Management: Track policy changes across versions and effective dates.
```

---

## 7. Duplicate Analysis

- **Total Uploaded Records:** 0
- **Unique Records:** 0
- **Duplicate Records:** N/A (0 data files present in repository)

---

## 8. Five-Class Concept Coverage Feasibility

We evaluated how the README schema concepts align with our project's 5 target categories:

| Target Class | Evidence in README Schema? | Candidate Records | Actual Ground-Truth Label? | Manual Annotation Needed? |
| :--- | :---: | :---: | :---: | :---: |
| **1. Waiting Periods** | **Yes** *(Exclusions/Medical)* | 0 *(No files)* | **No** | **Yes** |
| **2. Sub-Limits & Caps** | **Yes** *(Policy Terms/Limits)* | 0 *(No files)* | **No** | **Yes** |
| **3. Non-Payable Items & Consumables** | **Yes** *(Exclusions)* | 0 *(No files)* | **No** | **Yes** |
| **4. Co-Payment Mandates** | **Yes** *(Policy Terms)* | 0 *(No files)* | **No** | **Yes** |
| **5. Standard Coverage** | **Yes** *(Policy Content)* | 0 *(No files)* | **No** | **Yes** |

**Note:**  
> **"Keyword/concept candidate counts — NOT annotations."**  
> Candidate concept counts are 0 because no data records were uploaded to the Hugging Face repository.

---

## 9. Candidate Counts

```text
Waiting Period candidate records: 0 (No data files uploaded)
Sub-Limit candidate records: 0 (No data files uploaded)
Consumables/Non-Payable candidate records: 0 (No data files uploaded)
Co-Payment candidate records: 0 (No data files uploaded)
Coverage candidate records: 0 (No data files uploaded)
```
*(Clearly labeled: Keyword/concept candidate counts — NOT annotations.)*

---

## 10. License Verification

- **License Name:** **MIT License** (specified in `README.md`).
- **Commercial/Research Permissibility:** Free for research and commercial use with attribution.
- **Attribution Citation:** `BDR AI Organization (2025), Insurance Policy Documents Dataset, Hugging Face`.

---

## 11. Limitations

1. **Empty Repository on HF Hub:** The repository contains only `README.md` and `.gitattributes` without uploaded data files.
2. **Synthetic Generation Methodology:** The README explicitly states that the dataset design is based on synthetic policy documents generated by *BDR Agent Factory v1*.
3. **No Pre-Annotated 5-Class Labels:** Does not contain pre-existing ground-truth labels for our 5 specific insurance risk categories.

---

## 12. Final Conclusion & Recommendation

Select one of the required formal conclusions:

### **OPTION B: POTENTIALLY USABLE, BUT PROVENANCE/LENGTH/METADATA LIMITATIONS EXIST**

#### Explanation:
While the Hugging Face repository `dhanushmekaka/insurance-policy-docs-dataset` provides a well-defined schema and MIT license in its `README.md`, no actual data files are currently uploaded to the Hugging Face Hub, and the described methodology relies on synthetic agent-generated policy text. 

Therefore, it **cannot** serve as a direct source of real-world ground-truth training data without uploading real policy documents.

---

## 🛑 Absolute Stop Condition Status

- **Model Training Executed:** **0** (No DistilBERT or DeBERTa training performed).
- **Dataset Modifications / Annotations:** **0** (No files altered or synthetic data created).
- **Current Workspace State:** Stopped after completing `DATASET_INSPECTION_REPORT.md`, awaiting user review.
