# Google Drive Submission & Demo Video Checklist
## Guide for Final EPJ Evaluation (Review III Submission)

---

### 🚨 Critical Instructions Before You Submit
1. **Sharing Permission:**
   - Right-click the root folder on Google Drive $\rightarrow$ Click **Share** $\rightarrow$ Under "General access", change from **"Restricted"** to **"Anyone with the link"** with role set to **"Viewer"**.
   - **Test this link in an Incognito / Private Browser Window** before submitting to ensure it opens without prompting for a login or access request!
2. **Consistency Guarantee:**
   - Ensure the **Project Report**, **Demo Video**, **Source Code**, and **IEEE Research Paper** all describe the **same, updated version** of the project (incorporating the Review III Model Comparison).

---

## 📁 Prescribed Google Drive Folder Structure

Create a main folder named:  
`SWE1017_InsureCheck-NLP_Final_Submission/`

Organize its contents into the following subfolders:

```
SWE1017_InsureCheck-NLP_Final_Submission/
│
├── 01_Demo_Video/
│   └── InsureCheck_NLP_Complete_System_Demo.mp4  (1080p, 5-8 minutes)
│
├── 02_Source_Code/
│   ├── src/
│   │   ├── pdf_parser.py
│   │   ├── clause_classifier.py
│   │   ├── risk_engine.py
│   │   ├── benchmark_evaluator.py
│   │   ├── dataset_loader.py
│   │   └── train_deberta.py
│   ├── data/
│   │   ├── dataset2_train.json
│   │   ├── dataset2_test.json
│   │   └── comparative_benchmark_results.json
│   ├── models/
│   │   ├── insurecheck_deberta_model.pkl
│   │   └── deberta_insurance_classifier/
│   ├── app.py
│   ├── benchmark_comparative_models.py
│   ├── run_experiments.py
│   ├── train_pipeline.py
│   ├── requirements.txt
│   └── README.md
│
├── 03_Project_Report/
│   ├── Final_Project_Report_Submission.pdf  (Primary Submission)
│   └── Final_Project_Report_Submission.docx (Editable Source)
│
├── 04_IEEE_Research_Paper/
│   ├── InsureCheck_NLP_IEEE_Research_Paper.pdf  (IEEE 2-Column Template)
│   └── InsureCheck_NLP_IEEE_Research_Paper.docx (or Overleaf ZIP source)
│
└── 05_Plagiarism_Report/
    └── Turnitin_Plagiarism_Report_InsureCheck.pdf (Showing <15% similarity)
```

---

## 🎥 Demo Video: Step-by-Step Recording Script & Flow

The university guidelines state:
> *"The video must include a full implementation demo of the working system, showing the complete working flow from input to output."*

### Suggested Video Duration: 5 to 7 Minutes
### Screen Recording Tool: OBS Studio, SimpleScreenRecorder, or Loom (Full HD 1080p)

| Time | Segment | What to Show on Screen | What to Say / Highlight |
| :---: | :--- | :--- | :--- |
| **0:00 - 0:45** | **Title & Problem Intro** | Title slide / Slide 1 & 2 from PPT | Introduce project title: *InsureCheck-NLP*, team members, register numbers, and course SWE1017. Explain the problem: over 25% of health claims suffer deductions due to hidden fine print in 40+ page policy PDFs. |
| **0:45 - 1:30** | **System Architecture & Review 3 Update** | Architecture diagram & benchmark table | Explain the 4 pipeline stages: PDF Ingestion $\rightarrow$ Fine-tuned DeBERTa-v3 Classifier $\rightarrow$ Risk Engine $\rightarrow$ Streamlit Dashboard. State that for Review III, the model was rigorously benchmarked against 9 baselines (achieving 97.4% F1 and 14.2ms latency). |
| **1:30 - 2:00** | **Terminal & Launch** | Terminal running `streamlit run app.py` | Show running `pip install -r requirements.txt` and starting the app with `streamlit run app.py`. Browser automatically loads `http://localhost:8501`. |
| **2:00 - 3:30** | **Live Document Ingestion & Real-Time Scanning** | Streamlit UI in Browser | 1. Drag and drop a sample policy PDF (e.g. `Health Suraksha Policy Wording.pdf`).<br>2. Watch the progress bar as `pdfplumber` extracts sections and DeBERTa-v3 classifies clauses in real time.<br>3. Point out the animated **Claim Risk Gauge Meter** showing the composite risk score (e.g., 85% - HIGH RISK). |
| **3:30 - 4:45** | **Interactive Inspection & Plain-English Translation** | Dashboard table, filters, and cards | 1. Filter clauses by category (Waiting Periods, Sub-Limits, Non-Payables, Co-Pay).<br>2. Highlight how dense legal clauses are translated into plain 5th-grade English (e.g., *"Insurer will not pay for any pre-existing ailment until after 36 months"* translated to *"You cannot claim for any past disease for the first 3 years"*).<br>3. Click the **"Export CSV Audit Report"** button to download the structured audit file. |
| **4:45 - 5:30** | **Benchmark Script Execution** | Terminal running `python benchmark_comparative_models.py` | Run `python benchmark_comparative_models.py` live in terminal to show execution of the 9 baseline comparisons, verifying the empirical metrics reported in the paper and report. |
| **5:30 - 6:00** | **Conclusion & Wrap-Up** | Final summary slide / Streamlit UI | Summarize practical impact: empowers policyholders with pre-claim transparency; adheres to IRDAI consumer disclosure standards; thank the evaluator. |

---

## ✅ Pre-Submission Verification Checklist

Before sending the final Drive link to the professor:
- [ ] **Drive Access:** Opened the link in an incognito window without signing into Google; folder opened immediately.
- [ ] **Complete Working Flow:** Video starts from terminal launch/PDF upload and ends with CSV audit download.
- [ ] **README Included:** `README.md` is present in the `02_Source_Code/` folder and explains how to run the code.
- [ ] **All Files Consistent:** Report, Paper, Code, and Video all cite the **97.4% Macro F1** and **14.2 ms latency** on the 5-class taxonomy with 9 baseline model comparisons.
- [ ] **Paper Template:** Paper is strictly formatted in IEEE 2-column format.
- [ ] **Plagiarism Report Attached:** Turnitin similarity index is below university threshold (<15%).
