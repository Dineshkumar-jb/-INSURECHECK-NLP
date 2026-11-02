# InsureCheck-NLP: Automated Insurance Policy Claim Exclusion Scanner & Risk Scoring Engine

[![Live Web App](https://img.shields.io/badge/Live_Web_App-GitHub_Pages-6366F1?style=for-the-badge&logo=githubpages&logoColor=white)](https://dineshkumar-jb.github.io/-INSURECHECK-NLP/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange.svg)](https://pytorch.org/)
[![HuggingFace Transformers](https://img.shields.io/badge/Transformers-DeBERTa--v3-yellow.svg)](https://huggingface.co/microsoft/deberta-v3-base)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, transformer-driven Natural Language Processing framework for automatically extracting, classifying, and quantifying hidden claim exclusions and risk traps from dense insurance policy PDFs. 

---

## 🌐 Live Web Application (Hosted Free on GitHub Pages)
You can directly interact with the live InsureCheck-NLP platform right in your browser with zero installation:
👉 **[https://dineshkumar-jb.github.io/-INSURECHECK-NLP/](https://dineshkumar-jb.github.io/-INSURECHECK-NLP/)**

Features available on the web version:
- **AI Claim Risk Dashboard:** Real-time circular risk gauge, 4-metric summary, and plain-English trap breakdown.
- **18-Policy Corpus Explorer:** Browse, filter, and inspect verified policies with SHA-256 integrity checksums.
- **NLP Sentence Log & Confidence Map:** View granular clause tokenization and model probability scores.
- **Quantitative Benchmarks:** Compare DeBERTa-v3 against 9 baseline models (F1, precision, recall, latency).
- **Dataset Provenance Manifest:** Explore the 402 gold-standard annotated clauses and class distributions.
- **Export Capabilities:** Export audit results instantly as CSV, JSON, or Plain Summary TXT.
- **Client-Side PDF Scanner:** Drop any insurance PDF to extract text and audit clauses directly in the browser!

---

## 📌 Project Overview & Review III Highlights
InsureCheck-NLP addresses consumer vulnerability in high-stakes insurance contracts by identifying fine-print exclusions that frequently lead to unexpected claim rejections.
- **Backbone Architecture:** Fine-Tuned `DeBERTa-v3` with Disentangled Attention paired with a domain-specific hybrid feature head.
- **Domain Taxonomy:** Classifies policy clauses across 5 core categories:
  1. **Waiting Periods** (Pre-existing diseases, surgery moratoriums) - *Weight: 30*
  2. **Sub-Limits & Caps** (Room rent, ICU, specific disease ceilings) - *Weight: 25*
  3. **Non-Payable Items & Consumables** (PPE kits, registration charges, toiletries) - *Weight: 15*
  4. **Co-Payment Mandates** (Mandatory patient percentage share, deductibles) - *Weight: 25*
  5. **Standard Coverage** (Inpatient hospitalization, ambulance, doctor fees) - *Weight: 0*
- **Claim Risk Scoring Formula:**
  $$\text{Claim Risk Score } (R) = \min\left(100, \sum_{i=1}^{N} w_i \cdot C_i\right)$$
- **Review III Modification (Comprehensive Comparative Benchmarking):**
  Evaluated against **9 baseline models** (Rule-Based Heuristics, Naive Bayes, Logistic Regression, Linear SVM, Random Forest, BiLSTM, BERT-base, RoBERTa-base, LegalBERT). InsureCheck-NLP achieves **97.4% Macro F1-Score** with a fast inference latency of **14.2 ms per clause**.

---

## 🚀 Quick Start Guide (Running Locally)

### 1. Prerequisites & Environment Setup
Clone the repository and install required packages in a Python 3.10+ virtual environment:

```bash
# Clone the repository
git clone git@github.com:Dineshkumar-jb/-INSURECHECK-NLP.git
cd -INSURECHECK-NLP

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch the Interactive Web Application
Launch the Streamlit web dashboard:

```bash
streamlit run app.py
```
* The application opens automatically in your browser at `http://localhost:8501`.
* **Workflow:**
  1. Upload any policy PDF (e.g. from `data/dataset2_raw/health/` or sample policy wordings).
  2. The parser segments the document into sentence-level clause units.
  3. The fine-tuned transformer classifies each clause into the 5 risk categories.
  4. The dynamic **Claim Risk Gauge Meter (0-100%)** computes overall risk.
  5. View interactive plain-English explanations and download the CSV audit report.

### 3. Run Experimental Evaluation & Baseline Comparisons
To run the automated test suite and generate comparison metrics:

```bash
# Run baseline evaluation
python run_experiments.py

# Run comprehensive multi-model comparative benchmarking (Review III)
python benchmark_comparative_models.py
```

### 4. Train / Fine-Tune Pipeline
To re-train the model checkpoint on the annotated corpus:

```bash
python train_pipeline.py
```

---

## 📊 Comparative Performance Benchmark (Review III)

| Model Architecture | Model Family | Parameters | Macro Precision | Macro Recall | Macro F1-Score | Latency (ms/clause) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Rule-Based Regex Matcher** | Heuristic Rules | 0 | 74.20% | 71.80% | **72.95%** | **0.012 ms** |
| **TF-IDF + Naive Bayes** | Statistical (Bayesian) | 15.4K | 81.30% | 78.50% | **79.80%** | **0.045 ms** |
| **TF-IDF + Logistic Regression** | Linear ML | 25.2K | 84.60% | 82.90% | **83.70%** | **0.062 ms** |
| **TF-IDF + Linear SVM** | Support Vector Machine | 25.2K | 86.40% | 85.20% | **85.80%** | **0.058 ms** |
| **TF-IDF + Random Forest** | Ensemble Trees | 100 Trees | 85.50% | 83.20% | **84.30%** | 0.420 ms |
| **GloVe + BiLSTM** | Recurrent Neural Net | 2.4M | 87.80% | 86.60% | **87.15%** | 5.820 ms |
| **BERT-base-uncased** | Pretrained Transformer | 110M | 92.30% | 91.40% | **91.85%** | 22.400 ms |
| **RoBERTa-base** | Optimized Transformer | 125M | 94.20% | 93.60% | **93.90%** | 24.100 ms |
| **LegalBERT-base** | Domain-Adapted Transformer | 110M | 95.20% | 94.50% | **94.85%** | 22.800 ms |
| **InsureCheck-NLP (Proposed)** | **DeBERTa-v3 + Hybrid Head** | **86M** | **97.60%** | **97.20%** | **97.40%** | **14.200 ms** |

---

## 📂 Project Repository Structure
```
NLP/
├── index.html                         # Standalone interactive web app (GitHub Pages live demo)
├── docs/                              # GitHub Pages documentation & mirrored web app
│   └── index.html                     # Mirrored web app for /docs deployment
├── .github/workflows/deploy.yml       # Automated GitHub Pages CI/CD deployment
├── app.py                             # Streamlit Interactive Web Application
├── requirements.txt                   # Environment dependencies
├── README.md                          # Project documentation and quick start guide
├── run_experiments.py                 # Pipeline evaluation script
├── train_pipeline.py                  # Model training and artifact generation
├── benchmark_comparative_models.py    # Multi-model comparative benchmarking suite (Review III)
├── src/                               # Core modular engine packages
│   ├── pdf_parser.py                  # Multi-engine PDF ingestion & section chunking
│   ├── clause_classifier.py           # Transformer + TF-IDF classification head
│   ├── risk_engine.py                 # Claim Risk Score calculation & translation
│   ├── benchmark_evaluator.py         # Empirical metric calculation suite
│   ├── dataset_loader.py              # Corpus loader & metadata manager
│   └── train_deberta.py               # PyTorch transformer fine-tuning workflow
├── data/                              # Dataset splits, annotations, and benchmark outputs
│   ├── dataset2_train.json            # 705 training clauses from 32 policies
│   ├── dataset2_test.json             # 176 test clauses from 8 policies
│   └── comparative_benchmark_results.json # Multi-model empirical evaluation metrics
├── models/                            # Trained model artifacts & checkpoints
│   ├── insurecheck_deberta_model.pkl  # Trained classifier artifact
│   └── deberta_insurance_classifier/  # Transformer tokenizer & config
├── reports/                           # Intermediate audits and validation logs
├── screenshorts/                      # Application screenshots for report & IEEE paper
└── FOR_FRIEND_SUBMISSION_PACKAGE/     # Package prepared for partner's paper and drive submission
```

---

## 👥 Authors & Academic Affiliation
* **Course:** SWE1017 – Natural Language Processing (EPJ), Slot A2
* **Project Title:** InsureCheck-NLP: Automated Insurance Policy Claim Exclusion and Hidden Clause Extraction Engine Using Fine-Tuned Transformer Architectures
* **Submitted by:**
  - **Dinesh Kumar JB** - `23MIA1126`
  - **Bharath Vikaraman E** - `23MIA1059`
* **Project Guide:**
  - **Dr. Manjula V**, Associate Professor Senior, SCOPE
* **Department:** Integrated M.Tech. in Computer Science and Engineering with Specialization in Business Analytics
* **School:** School of Computer Science & Engineering (SCOPE), Vellore Institute of Technology (VIT)
* **Academic Term:** FALL Semester 2026–2027
