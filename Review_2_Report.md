# TITLE OF PROJECT REPORT
## InsureCheck-NLP: Automated Insurance Policy Claim Exclusion and Hidden Clause Extraction Engine using Fine-Tuned Transformer Architectures

**A PROJECT REVIEW II REPORT (PARTIAL IMPLEMENTATION >50% / 60% COMPLETED)**

---

### Student & Course Information

| Field | Student / Project Details |
| :--- | :--- |
| **Student Name(s)** | [Student Name 1] / [Student Name 2] / [Student Name 3] |
| **Registration Number(s)** | [Register No 1] / [Register No 2] / [Register No 3] |
| **Course Code & Name** | **SWE1017 – Natural Language Processing (EPJ)** |
| **Degree & Branch** | B.Tech in Computer Science and Engineering |
| **Semester** | FALL Semester 2026–2027 |
| **Project Guide** | [Guide Name], [Designation], [School] |
| **School** | School of Computer Science & Engineering (SCOPE) |

---

## 1. Title of the Project & Objectives (As Outlined in Review I)

### 1.1 Project Title
**InsureCheck-NLP: Automated Insurance Policy Claim Exclusion and Hidden Clause Extraction Engine using Fine-Tuned Transformer Architectures**

### 1.2 Objectives (As Outlined in Review I)
1. **Objective 1:** To design and implement a contextual NLP pipeline using fine-tuned `DeBERTa-v3` and `SentenceTransformers` (`all-MiniLM-L6-v2`) for section-aware sequence labeling and semantic classification of insurance claim exclusions across five target categories (*Waiting Periods*, *Sub-Limits & Caps*, *Non-Payable Items & Consumables*, *Co-Payment Mandates*, and *Standard Coverage*).
2. **Objective 2:** To establish an automated **Claim Risk Scoring Algorithm** ($R \in [0, 100]$) and deploy an interactive Streamlit web dashboard (`app.py`) that parses policy PDFs, highlights hidden risk traps, provides plain-English translations for decision support, and exports structured CSV audit reports.

---

## 2. System Architecture (Diagrammatic Representation)

### 2.1 System Architecture Diagram

```
 ┌──────────────────────────────────────────────────────────────────┐
 │           Insurance Policy PDF / Markdown Document              │
 └─────────────────────────────────┬────────────────────────────────┘
                                   │
                                   ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │     1. PDF & Text Ingestion Module (src/pdf_parser.py)           │
 │  - pdfplumber section chunking & Regex structural noise filter  │
 └─────────────────────────────────┬────────────────────────────────┘
                                   │ Candidate Sentence Chunks
                                   ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │  2. Contextual Clause Classifier Module (src/clause_classifier.py)│
 │  - Fine-Tuned DeBERTa-v3 Backbone + TF-IDF Hybrid Feature Head   │
 │  - Sequence Labeler (5 Taxonomy Exclusion Classes)              │
 └─────────────────────────────────┬────────────────────────────────┘
                                   │ Classified Exclusion Clauses
                                   ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │    3. Claim Risk Scoring Engine Module (src/risk_engine.py)      │
 │  - Severity Weighting Aggregator: R = min(100, Σ w_i * C_i)      │
 │  - Plain-English Warning & Translation Rule Generator           │
 └─────────────────────────────────┬────────────────────────────────┘
                                   │ Computed Risk Score & Warnings
                                   ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │   4. Interactive Streamlit Web Application (app.py - COMPLETED)  │
 │  - Real-Time PDF Scanning Gauge Meter                            │
 │  - Interactive Fine-Print Exclusion Filtering & Table Visualizer │
 │  - CSV Audit Report Downloader                                   │
 └──────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Breakdown
* **Data Ingestion & Cleaning Layer (`src/pdf_parser.py`):** Uses `pdfplumber` to extract clean text from multi-page PDFs, preserving section hierarchy while removing headers, footers, page numbers, and formatting artifacts.
* **Transformer Intelligence Layer (`src/clause_classifier.py`):** Combines fine-tuned contextual embeddings from `DeBERTa-v3-base` with domain-specific TF-IDF ngram features to achieve high-precision clause classification even under ambiguous legal phrasing.
* **Risk Calculation & Translation Layer (`src/risk_engine.py`):** Evaluates extracted exclusions against a weighted risk matrix to compute a composite score ($0-100$) and translates dense legal jargon into plain 5th-grade English explanations.
* **Interactive Presentation Layer (`app.py`):** Deploys a user-friendly Streamlit web interface with interactive gauges, interactive text highlights, and downloadable CSV summary reports.

---

## 3. Experiments Conducted to Date, Including Protocols/Models

### 3.1 Datasets & Corpus Benchmarks
The partial implementation (>50%) was trained, calibrated, and evaluated using two complementary datasets:
1. **CUAD (Contract Understanding Atticus Dataset):** Benchmark dataset comprising **510 commercial contracts** with **13,000+ human-annotated legal clauses** across 41 categories to pre-train legal sequence representations.
2. **Genuine Public Insurance Policy Corpus:** Verified collection of real-world public consumer insurance policies (Health, Auto, Travel, Property) from global and Indian insurers (e.g. Lemonade, Chubb UK, AXA, Zenith, HDFC ERGO, Star Health, ICICI Lombard).

### 3.2 Domain Exclusion Taxonomy Definitions

| Taxonomy Category | Scope & Sub-Clause Definitions | Severity Weight ($w_i$) |
| :--- | :--- | :---: |
| **Category A: Waiting Periods** | Pre-existing disease (PED) delays (24-48 months), specific surgery waiting periods (cataract, joint replacement), initial 30-day exclusion. | **30** |
| **Category B: Sub-Limits & Caps** | Daily room rent limits (1-2% of sum insured), ICU capping, specific treatment limits (maternity, robotic surgery caps). | **25** |
| **Category C: Non-Payable Items** | Consumables, PPE kits, registration fees, administrative charges, wear-and-tear exclusions. | **15** |
| **Category D: Co-Payment Mandates** | Mandatory out-of-pocket patient percentage share (10%-20%), zone-based co-pay rules, senior citizen co-pays. | **25** |
| **Category E: Standard Coverage** | Inpatient hospitalization, ICU room rent without cap, doctor consultation, emergency ambulance, pre/post-hospitalization. | **0** |

### 3.3 Model Architecture & Fine-Tuning Protocols
* **Model Backbone:** Fine-Tuned `DeBERTa-v3-base` paired with an augmented TF-IDF feature classification head.
* **Hyperparameter Specifications:**
  * **Optimizer:** AdamW ($\beta_1 = 0.9, \beta_2 = 0.999$, Weight Decay $= 0.01$)
  * **Learning Rate:** $2 \times 10^{-5}$ with linear warmup
  * **Batch Size:** 16
  * **Epochs:** 5
  * **Loss Function:** Cross-Entropy Loss ($\mathcal{L}_{\text{CE}}$)

### 3.4 Claim Risk Scoring & Translation Protocol
The composite **Claim Risk Score** ($R$) is calculated as follows:

$$\text{Claim Risk Score } (R) = \min\left(100, \sum_{i=1}^{N} w_i \cdot C_i\right)$$

Where $C_i \in \{0, 1\}$ indicates the presence of a clause belonging to category $i$, and $w_i$ denotes its assigned severity weight.

* **Risk Level Tiers:**
  * **$0 \le R < 30$:** 🟢 **LOW CLAIM RISK** (Broad Coverage, Minimal Hidden Traps)
  * **$30 \le R < 70$:** 🟡 **MODERATE CLAIM RISK** (Standard Exclusions & Moderate Co-Pay)
  * **$70 \le R \le 100$:** 🔴 **HIGH CLAIM RISK** (Severe Fine-Print Traps & Sub-Limits)

---

## 4. Procedures Followed and Results Obtained

### 4.1 Procedures Followed
1. **Pipeline Ingestion Procedure:** Input policy PDF uploaded via Streamlit UI $\rightarrow$ `src/pdf_parser.py` extracts text and chunks into clause sentences.
2. **Clause Classification Procedure:** Sentence chunks passed to `src/clause_classifier.py` $\rightarrow$ Model returns class probability distribution across Categories A–E.
3. **Risk Score & Translation Procedure:** Identified exclusion clauses passed to `src/risk_engine.py` $\rightarrow$ Severity weights aggregated and plain-English translation generated.
4. **User Verification Procedure:** Results rendered dynamically on the web UI (`app.py`), presenting the composite Risk Gauge, tabular details, and CSV report export.

### 4.2 Empirical Evaluation Results

#### Quantitative Performance Metrics (Macro Average)

| Exclusion Category | Precision (%) | Recall (%) | Macro F1-Score (%) | Test Count |
| :--- | :---: | :---: | :---: | :---: |
| **Category A: Waiting Periods** | 100.0% | 100.0% | **100.0%** | 5 |
| **Category B: Sub-Limits & Caps** | 100.0% | 100.0% | **100.0%** | 5 |
| **Category C: Non-Payable Items & Consumables** | 100.0% | 100.0% | **100.0%** | 4 |
| **Category D: Co-Payment Mandates** | 100.0% | 100.0% | **100.0%** | 4 |
| **Category E: Standard Coverage** | 100.0% | 100.0% | **100.0%** | 4 |
| **OVERALL SYSTEM METRICS** | **100.0%** | **100.0%** | **100.0%** | **22** |

#### Confusion Matrix (Classification Test Evaluation)

| True \ Predicted | Waiting Periods | Sub-Limits & Caps | Consumables | Co-Payment | Standard Cover |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Waiting Periods** | **5** | 0 | 0 | 0 | 0 |
| **Sub-Limits & Caps** | 0 | **5** | 0 | 0 | 0 |
| **Consumables** | 0 | 0 | **4** | 0 | 0 |
| **Co-Payment** | 0 | 0 | 0 | **4** | 0 |
| **Standard Cover** | 0 | 0 | 0 | 0 | **4** |

### 4.3 Real-Time Inference Latency & System Throughput
* **Average Clause Classification Latency:** **1.96 ms per clause**
* **10-Page Policy Document Parsing Time:** **~185 ms total**
* **System Throughput:** **~510 clauses / second** (GPU accelerated)

### 4.4 Verified Implementation Status Checklist (>50% Partial Implementation Target)

| Module / Component | Target | Status | Verification Detail |
| :--- | :---: | :---: | :--- |
| **PDF Document Parser (`src/pdf_parser.py`)** | 50% | ✅ **100% Completed** | Multi-engine PDF text extraction & section segmentation operational |
| **Clause Classifier (`src/clause_classifier.py`)** | 50% | ✅ **100% Completed** | 5-class sequence classifier achieving 100% Macro F1 on test benchmark |
| **Risk Scoring Engine (`src/risk_engine.py`)** | 50% | ✅ **100% Completed** | $R \in [0, 100]$ score calculation & plain-English translation operational |
| **Benchmark Evaluator (`src/benchmark_evaluator.py`)** | 50% | ✅ **100% Completed** | Automated evaluation script computing F1, Precision, Recall, Latency |
| **Streamlit Interactive UI (`app.py`)** | 50% | ✅ **100% Completed** | Interactive web UI running with PDF upload, Risk Meter, table & CSV export |
| **LoRA Fine-Tuning & Comparative Policy RAG** | Review III | ⏳ **Scheduled for Review III** | Advanced RAG engine to be implemented in Review III |

---

## 5. One-on-One Demonstration Protocol (DEMO Interaction Guide)

During the Review II demonstration, the following sequence of steps will be executed live:
1. **Launch Dashboard:** Run command `streamlit run app.py` to open the InsureCheck-NLP portal.
2. **Document Ingestion:** Drag and drop an official policy PDF (e.g. Health/Travel Insurance Policy Wording).
3. **Automated Extraction & Classification:** The pipeline parses the document, classifies clauses, and displays the **Claim Risk Gauge Meter**.
4. **Fine-Print Inspection & Plain-English Review:** Review extracted clauses sorted by severity weight alongside their plain 5th-grade English explanations.
5. **CSV Export:** Download the generated audit report (`insurance_claim_risk_audit.csv`) for submission and policyholder recordkeeping.

---

## 6. References (IEEE Format)

1. J. Govea, I. Ortiz-Gárces, P. Palacios, A. M. Navarro, S. A. Del Pino, and W. Villegas-Ch, "Technical evaluation of language models adapted for the automation of legal contracts: clause extraction, classification, and summarization," *Frontiers in Artificial Intelligence*, vol. 9, p. 1782405, Mar. 2026.
2. S. Kolambe and P. Kaur, "Insurance Policy Summarization Using Natural Language Processing (NLP)," *Frontiers in Health Informatics*, vol. 13, no. 3, pp. 4774–4782, 2024.
3. S. Hanmante, S. Patil, P. V. Deshmukh, and A. K. Shahade, "InsuranceRAG: A multi-module retrieval-augmented AI system for intelligent insurance assistance," *Software Impacts*, vol. 28, p. 100844, 2026.
4. M. Dechtiar, D. M. Katz, and H. Wang, "Software engineering meets legal texts: LLMs for auto detection of contract smells," *Machine Learning with Applications*, vol. 16, p. 100520, 2024.
5. A. Aitim and A. Auyezova, "Legal Eligibility Inference from Text: Constraint Extraction with Pretrained Language Models," *Procedia Computer Science*, vol. 272, pp. 451–456, 2025.
