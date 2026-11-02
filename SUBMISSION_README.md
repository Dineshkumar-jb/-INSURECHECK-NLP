# 🛡️ InsureCheck-NLP: Quick Start & Submission Guide

**Automated Insurance Policy Claim Exclusion and Hidden Clause Extraction Engine**  
*Course:* SWE1017 – Natural Language Processing (EPJ), Slot A2  
*School:* SCOPE, Vellore Institute of Technology (VIT)  
*Guide:* Dr. Manjula V, Associate Professor Senior, SCOPE  
*Authors:*  
- **Dinesh Kumar JB** (`23MIA1126`)  
- **Bharath Vikaraman E** (`23MIA1059`)  

---

## 🌐 1. Live Web Demo (Zero Installation Required)
You can test the fully interactive platform directly in any web browser without running code locally:  
👉 **[https://dineshkumar-jb.github.io/-INSURECHECK-NLP/](https://dineshkumar-jb.github.io/-INSURECHECK-NLP/)**

GitHub Repository:  
👉 **[https://github.com/Dineshkumar-jb/-INSURECHECK-NLP](https://github.com/Dineshkumar-jb/-INSURECHECK-NLP)**

---

## ⚡ 2. How to Run the Project Locally (2 Steps)

### Step 1: Install Dependencies
Open a terminal inside the unzipped project folder and install the required Python packages:

```bash
# Recommended: Create and activate a Python 3.10+ virtual environment
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 2: Launch the Web Application
Run the Streamlit interactive dashboard:

```bash
streamlit run app.py
```
* The application will immediately launch in your default web browser at **`http://localhost:8501`**.

---

## 🧪 3. How to Run Experimental Evaluation & Benchmarks

To reproduce our Review III comparative experimental results across all 9 baseline models:

```bash
# Run multi-model benchmark evaluation (DeBERTa-v3 vs RoBERTa, LegalBERT, BiLSTM, SVM, etc.)
python benchmark_comparative_models.py

# Run pipeline unit tests & latency validation
python run_experiments.py
```

---

## 📊 4. System Capabilities Demonstrated

1. **AI Claim Risk Dashboard:** Computes a normalized Claim Risk Index (0–100%) and provides live KPI metrics.
2. **Plain-English Translation:** Translates complex legal fine-print clauses (waiting periods, room rent caps, cataract limits) into plain consumer warnings.
3. **18-Policy IRDAI Corpus Explorer:** Includes 18 real-world policy wordings (HDFC ERGO, SBI General, Star Health, etc.) with SHA-256 audited checksums.
4. **Sentence-Level NLP Log:** Detailed tokenization and classification traces with model confidence scores.
5. **PDF Ingestion:** Upload any insurance policy PDF to extract text and audit exclusions end-to-end.
6. **Forensic Audit Export:** Download audit logs as CSV, JSON, or Plain Summary TXT.

---

## 📁 5. Folder Contents

```
INSURECHECK_NLP/
├── app.py                             # Main Streamlit web application
├── index.html                         # Standalone interactive web app (GitHub Pages)
├── requirements.txt                   # Python dependencies
├── README.md                          # Full repository documentation
├── SUBMISSION_README.md               # Quick start submission instructions
├── benchmark_comparative_models.py    # Multi-model benchmarking script (Review III)
├── run_experiments.py                 # Pipeline validation script
├── train_pipeline.py                  # PyTorch model fine-tuning pipeline
├── Final_Project_Report_Submission.docx # Complete 43-page final project report
├── Final_Project_Report.md            # Markdown version of the final project report
├── src/                               # Core Python engine modules
│   ├── clause_classifier.py           # 5-class NLP classification engine
│   ├── pdf_parser.py                  # Multi-engine PDF ingestion & sentence chunker
│   ├── risk_engine.py                 # Risk scoring & plain-English translation
│   ├── benchmark_evaluator.py         # Empirical metric calculation suite
│   ├── dataset_loader.py              # Corpus metadata loader
│   └── train_deberta.py               # PyTorch transformer training loop
├── data/                              # Gold-standard datasets & 18 policy texts
├── metadata/                          # Policy manifest & SHA-256 registry
├── assets/                            # Premium dark-mode CSS styling system
├── screenshorts/                      # High-resolution screenshots of the working UI
└── FOR_FRIEND_SUBMISSION_PACKAGE/     # IEEE Research Paper draft & review assets
```
