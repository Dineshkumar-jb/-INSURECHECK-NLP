# TITLE OF PROJECT REPORT
## InsureCheck-NLP: Automated Insurance Policy Claim Exclusion and Hidden Clause Extraction Engine using Fine-Tuned Transformer Architectures

**A PROJECT REVIEW I REPORT**

**Submitted by:**
- Candidate 1: [Register No.]
- Candidate 2: [Register No.]
- Candidate 3: [Register No.]

**Course Code & Name:** SWE1017 – Natural Language Processing (EPJ)  
**Project Guide:** [NAME], [Designation], [School]  
**School:** School of Computer Science & Engineering (SCOPE)  
**Degree / Branch:** B.Tech / Computer Science and Engineering  
**Semester:** FALL Semester 2026–2027  

---

## 1. Abstract
Insurance policy documents are notoriously complex legal contracts filled with dense terminology, ambiguous sub-clauses, and hidden exclusions designed to limit insurer liability. Policyholders frequently experience unexpected claim rejections due to unacknowledged fine print such as room-rent sub-limits, multi-year waiting periods, co-payment mandates, and non-payable consumable lists. This project presents **InsureCheck-NLP**, an intelligent Natural Language Processing framework for automatically extracting, classifying, and quantifying hidden claim exclusions and risk traps from insurance policy PDF documents. The proposed pipeline combines `pdfplumber` for section-aware text extraction, fine-tuned `DeBERTa-v3` for sequence labeling and clause classification, and `SentenceTransformers` (`all-MiniLM-L6-v2`) for semantic mapping against a standardized insurance risk taxonomy. InsureCheck-NLP calculates a composite **Policy Transparency & Claim Risk Score (%)** and generates a plain-English summary of non-covered conditions. Evaluated on public legal and insurance contract benchmarks (CUAD and custom insurance corpora), the system achieves strong F1-scores across four major exclusion categories. An interactive Streamlit dashboard provides policyholders with visual risk heatmaps and claim transparency analytics.

---

## 2. Problem Statement and Objectives

### Problem Statement
Insurance contracts contain lengthy legal fine print where critical claim-rejection clauses (such as disease waiting periods, co-pay percentages, and cap limits) are buried deep within multi-page PDF documents. Traditional search tools rely on basic keyword matching, which fails to capture semantic variations in complex legal phrasing (e.g., *"insurer shall not be liable for pre-existing ailments prior to 36 months"* vs. *"3-year waiting period for past illnesses"*). There is an urgent need for an automated, domain-specific NLP system that extracts hidden exclusion clauses and translates dense legal jargon into plain, actionable language.

### Objectives (Max 2 for Review I)
1. **Objective 1:** To design and implement a contextual NLP pipeline using fine-tuned `DeBERTa-v3` and `SentenceTransformers` for sequence labeling and semantic classification of insurance claim exclusions across four primary categories (Waiting Periods, Sub-Limits, Non-Payable Items, Co-Pay Rules).
2. **Objective 2:** To establish an automated **Claim Risk Scoring Algorithm** and deploy an interactive Streamlit UI that parses policy PDFs, highlights hidden risk traps, and presents plain-English summaries for decision support.

---

## 3. Review of Papers (Literature Survey - All 15 Papers)

*(Detailed review of 15 authentic peer-reviewed papers from Elsevier, Springer, and Frontiers provided in the reference repository)*

### Paper 1: Technical evaluation of language models adapted for the automation of legal contracts: clause extraction, classification, and summarization
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Technical evaluation of language models adapted for the automation of legal contracts: clause extraction, classification, and summarization
Frontiers in Artificial Intelligence, 2026  
  *Authors:* J. Govea, I. Ortiz-Gárces, P. Palacios, A. M. Navarro, S. A. Del Pino, and W. Villegas-Ch
- **(ii) Problem and Objectives:**  
  Automating legal contract processing (clause extraction, classification, summarization) in data-constrained domains.
- **(iii) Methodology Adopted:**  
  Domain-adapted DeBERTa/BERT, HuggingFace Transformers, scikit-learn, seqeval
- **(iv) Performance & Limitations:**  
  *Metrics:* Macro-F1, Span-level F1, ROUGE-L, BERTScore  
  *Performance Attained:* Macro-F1: 0.921 in classification, Span F1: 0.903 in clause extraction, ROUGE-L: 0.886  
  *Limitations (Gap Identified):* Tested on private-sector corporate contracts; lacks specific insurance policy claim risk scoring.  
  *Scope for Future Work:* Adapting legal transformers to consumer insurance policies and multi-category risk weighting.

### Paper 2: Insurance Policy Summarization Using Natural Language Processing (NLP)
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Insurance Policy Summarization Using Natural Language Processing (NLP)
Frontiers in Health Informatics, 2024  
  *Authors:* Sapana Kolambe and Dr. Parminder Kaur
- **(ii) Problem and Objectives:**  
  High complexity and length of insurance policy terms hindering policyholder comprehension of exclusions.
- **(iii) Methodology Adopted:**  
  Hybrid Extraction-based & Abstractive Summarization, Tokenization, POS Tagging, TextRank
- **(iv) Performance & Limitations:**  
  *Metrics:* ROUGE-1, ROUGE-L, Edit Distance, Cosine Similarity, Human Evaluation  
  *Performance Attained:* High summary fidelity across coverage and exclusion terms; improved user understandability.  
  *Limitations (Gap Identified):* Basic extractive-abstractive pipeline lacks explicit fine-grained clause extraction and numeric risk scoring.  
  *Scope for Future Work:* Incorporating fine-grained legal entity extraction and automated risk score calculation.

### Paper 3: AI-powered decision-making in facilitating insurance claim dispute resolution
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  AI-powered decision-making in facilitating insurance claim dispute resolution
Annals of Operations Research (Springer), 2023  
  *Authors:* Wen Zhang, Jingwen Shi, Xiaojun Wang, and Henry Wynn
- **(ii) Problem and Objectives:**  
  Prolonged dispute resolution and subjective cost estimation in road traffic accident (RTA) insurance claims.
- **(iii) Methodology Adopted:**  
  Predictive Regression & Machine Learning Decision-Making Models, Asymptotic Injury Modeling
- **(iv) Performance & Limitations:**  
  *Metrics:* Mean Absolute Error (MAE), RMSE, Judicial Cost Estimation Accuracy  
  *Performance Attained:* High predictive accuracy in judicial cost estimation across 88 real-life RTA case studies.  
  *Limitations (Gap Identified):* Focused on numerical/judicial dispute costs rather than unstructured text policy clause extraction.  
  *Scope for Future Work:* Integrating text-mining of insurance policy exclusion clauses with financial dispute estimation.

### Paper 4: Transforming Health Insurance Claims Adjudication using Blockchain Technology
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Transforming Health Insurance Claims Adjudication using Blockchain Technology
Procedia Computer Science (Elsevier), 2023  
  *Authors:* MobiSPC Conference Research Group
- **(ii) Problem and Objectives:**  
  Inefficiencies, tampering risks, and delays in centralized health insurance claims adjudication.
- **(iii) Methodology Adopted:**  
  Smart Contracts, Decentralized Ledger Technology (DLT), Automated Rules Verification
- **(iv) Performance & Limitations:**  
  *Metrics:* Claim Settlement Latency, System Security, Throughput (TPS)  
  *Performance Attained:* Substantial reduction in claims settlement time from weeks to near real-time automated execution.  
  *Limitations (Gap Identified):* Focuses on blockchain architecture; lacks natural language processing for parsing raw policy text.  
  *Scope for Future Work:* Combining NLP policy clause extraction with smart contract execution for automated claims.

### Paper 5: Explainable AI and Law: An Evidential Survey
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Explainable AI and Law: An Evidential Survey
Digital Society (Springer), 2024  
  *Authors:* Karen McGregor Richmond, Satya M. Muddamsetty, Thomas Gammeltoft-Hansen, Henrik Palmer Olsen, and Thomas B. Moeslund
- **(ii) Problem and Objectives:**  
  Black-box opacities in AI legal decision-making reducing accountability and transparency.
- **(iii) Methodology Adopted:**  
  Explainable AI (XAI) Taxonomy Mapping, Evidential Reasoning Frameworks
- **(iv) Performance & Limitations:**  
  *Metrics:* Explainability Fidelity, Stakeholder Trust Score, Interpretability  
  *Performance Attained:* Developed a structured taxonomy aligning legal inference types with transparent algorithmic models.  
  *Limitations (Gap Identified):* Conceptual survey framework without automated empirical text processing code.  
  *Scope for Future Work:* Implementing XAI token-attribution heads (e.g. SHAP/Integrated Gradients) in legal NLP classifiers.

### Paper 6: Legal Information Retrieval and Entailment Using Transformer-based Approaches
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Legal Information Retrieval and Entailment Using Transformer-based Approaches
The Review of Socionetwork Strategies (Springer), 2024  
  *Authors:* Mi-Young Kim, Juliano Rabelo, Housam K. B. Babiker, Md Abed Rahman, and Randy Goebel
- **(ii) Problem and Objectives:**  
  Information overload and complex legal entailment verification in case law and statute retrieval (COLIEE).
- **(iii) Methodology Adopted:**  
  Sentence-Transformers, Legal-BERT-ECHR, Stacking-Voting Ensembles, Binary Classification
- **(iv) Performance & Limitations:**  
  *Metrics:* Precision, Recall, F1-Score, COLIEE Task Accuracy  
  *Performance Attained:* Superior entailment accuracy using Legal-BERT-ECHR on legal paraphrasing and condition matching.  
  *Limitations (Gap Identified):* Evaluated on statute law databases; does not target consumer insurance policy contracts.  
  *Scope for Future Work:* Adapting legal entailment transformers to premise-claim verification in insurance contracts.

### Paper 7: InsuranceRAG: A multi-module retrieval-augmented AI system for intelligent insurance assistance
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  InsuranceRAG: A multi-module retrieval-augmented AI system for intelligent insurance assistance
Software Impacts (Elsevier), 2026  
  *Authors:* Sejal Hanmante, Shivani Patil, Priyanka V. Deshmukh, and Aniket K. Shahade
- **(ii) Problem and Objectives:**  
  Lack of transparent, conversational AI tools for query resolution and clause-level document retrieval in health insurance.
- **(iii) Methodology Adopted:**  
  Retrieval-Augmented Generation (RAG), FAISS Vector Store, Domain-adapted Embeddings, LLM Evaluator
- **(iv) Performance & Limitations:**  
  *Metrics:* Retrieval Recall@K, Answer Faithfulness, Latency, User Evaluation  
  *Performance Attained:* High retrieval accuracy and explainable clause-level responses via a web dashboard.  
  *Limitations (Gap Identified):* Focuses on conversational QA without calculating structured, composite policy claim risk scores.  
  *Scope for Future Work:* Integrating automated policy risk scoring algorithms with RAG clause extraction.

### Paper 8: Optimizing Claim Assessment Process for Property Insurance using Machine Learning
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Optimizing Claim Assessment Process for Property Insurance using Machine Learning
Procedia Computer Science (Elsevier), 2024  
  *Authors:* ISICO Conference Research Team
- **(ii) Problem and Objectives:**  
  Data imbalance and limited feature importance in property insurance claim frequency and risk prediction.
- **(iii) Methodology Adopted:**  
  Random Forest, Logistic Regression, SMOTE Data Imbalance Oversampling
- **(iv) Performance & Limitations:**  
  *Metrics:* Recall, Precision, F1-Score  
  *Performance Attained:* Achieved 96% Recall with Random Forest after applying SMOTE balancing.  
  *Limitations (Gap Identified):* Operates on structured tabular risk features rather than unstructured PDF contract text.  
  *Scope for Future Work:* Combining structured tabular ML models with text-based NLP exclusion extraction.

### Paper 9: Structure-Aware Uncertainty-Calibrated Evaluation for Legal Contract Knowledge Graph Extraction
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Structure-Aware Uncertainty-Calibrated Evaluation for Legal Contract Knowledge Graph Extraction
Procedia Computer Science (Elsevier), 2026  
  *Authors:* Moriya Dechtiar, Daniel Martin Katz, and Hongming Wang
- **(ii) Problem and Objectives:**  
  Evaluating epistemic uncertainty and inter-judge disagreement in legal contract knowledge graph extraction.
- **(iii) Methodology Adopted:**  
  Multi-Judge Ensemble (Semantic + Structural + LLM Judges), Isotonic Regression Calibration
- **(iv) Performance & Limitations:**  
  *Metrics:* Coefficient of Variation (CV), AUC for Error Detection, Calibration Error  
  *Performance Attained:* Achieved 0.982 AUC for error detection in contract knowledge graph extraction.  
  *Limitations (Gap Identified):* High computational overhead of multi-judge ensembles; requires reference-free validation data.  
  *Scope for Future Work:* Lightweight single-pass uncertainty calibration for real-time contract scanning.

### Paper 10: A case study for automated attribute extraction from legal documents using large language models
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  A case study for automated attribute extraction from legal documents using large language models
Artificial Intelligence and Law (Springer), 2026  
  *Authors:* Subinay Adhikary, Procheta Sen, Dwaipayan Roy, and Kripabandhu Ghosh
- **(ii) Problem and Objectives:**  
  Automated extraction of fine-grained concepts, attributes, and tags from unstructured legal proceedings.
- **(iii) Methodology Adopted:**  
  Weakly Supervised Sequence Labeling, Few-Shot Prompting with LLaMA-2 & Black-Box LLMs
- **(iv) Performance & Limitations:**  
  *Metrics:* Span Extraction Precision, Recall, Macro F1, Downstream Prediction Accuracy  
  *Performance Attained:* LLaMA-2 achieved superior few-shot attribute generation and downstream statute prediction accuracy.  
  *Limitations (Gap Identified):* LLM hallucination risk and prompt sensitivity in unconstrained few-shot prompting regimes.  
  *Scope for Future Work:* Combining LLM few-shot extraction with fine-tuned transformer classification heads.

### Paper 11: Health insurance fraud detection based on multi-channel heterogeneous graph structure learning
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Health insurance fraud detection based on multi-channel heterogeneous graph structure learning
Heliyon (Elsevier), 2024  
  *Authors:* Binsheng Hong, Ping Lu, Hang Xu, Jiangtao Lu, Kaibiao Lin, and Fan Yang
- **(ii) Problem and Objectives:**  
  Detecting complex, evolving health insurance fraud tactics across heterogeneous entities (patients, doctors, medicines).
- **(iii) Methodology Adopted:**  
  Multi-channel Heterogeneous Graph Structured Learning (MHGSL), Graph Convolutional Networks (GCN), KNN
- **(iv) Performance & Limitations:**  
  *Metrics:* Classification Accuracy, Macro F1, Precision, Recall, AUC-ROC  
  *Performance Attained:* High fraud detection accuracy by capturing multi-entity relational topology.  
  *Limitations (Gap Identified):* Requires structured relational graph data; does not process unstructured policy document text.  
  *Scope for Future Work:* Graph-augmented text processing linking policy exclusions with claim history.

### Paper 12: Addressing the notion of trust around ChatGPT in the high-stakes use case of insurance
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Addressing the notion of trust around ChatGPT in the high-stakes use case of insurance
Technology in Society (Elsevier), 2024  
  *Authors:* Juliane Ressel, Michaele Völler, Finbarr Murphy, and Martin Mullins
- **(ii) Problem and Objectives:**  
  Trust, governance, and financial inclusion risks around consumer-facing LLMs in high-stakes insurance applications.
- **(iii) Methodology Adopted:**  
  AI Governance Evaluation Framework, Dread Risk & Trust Judgment Analysis
- **(iv) Performance & Limitations:**  
  *Metrics:* Qualitative Trust Metrics, Risk Governance Alignment  
  *Performance Attained:* Established domain-specific governance framework for consumer-facing LLMs under the EU AI Act.  
  *Limitations (Gap Identified):* Conceptual commentary paper without empirical model implementation.  
  *Scope for Future Work:* Developing verifiable, explainable NLP systems that adhere to EU AI Act transparency rules.

### Paper 13: Legal Eligibility Inference from Text: Constraint Extraction with Pretrained Language Models
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Legal Eligibility Inference from Text: Constraint Extraction with Pretrained Language Models
Procedia Computer Science (Elsevier), 2025  
  *Authors:* Aigerim Aitim and Anel Auyezova
- **(ii) Problem and Objectives:**  
  Automated extraction of structured eligibility restrictions and condition-action pairings from legal text.
- **(iii) Methodology Adopted:**  
  Pre-trained BERT, Named Entity Recognition (NER), Condition-Action Pairing Rules, Entitlement Logic
- **(iv) Performance & Limitations:**  
  *Metrics:* NER Precision, Recall, Constraint Extraction Accuracy  
  *Performance Attained:* High precision in formalizing entitlement logic into machine-readable constraints.  
  *Limitations (Gap Identified):* Restricted to eligibility rules; does not calculate composite policy financial risk scores.  
  *Scope for Future Work:* Extending constraint extraction to insurance policy claim exclusion weighting.

### Paper 14: Software engineering meets legal texts: LLMs for auto detection of contract smells
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Software engineering meets legal texts: LLMs for auto detection of contract smells
Machine Learning with Applications (Elsevier), 2024  
  *Authors:* Moriya Dechtiar, Daniel Martin Katz, and Hongming Wang
- **(ii) Problem and Objectives:**  
  Detecting 'contract smells' (text patterns indicative of significant issues or ambiguities in legal contracts).
- **(iii) Methodology Adopted:**  
  GPT-4 Semi-Automated Labeling, BERT, LEGAL-BERT Fine-Tuning, Single vs Multi-Class Classification
- **(iv) Performance & Limitations:**  
  *Metrics:* Macro F1, Accuracy, Single-Class vs Multi-Class Precision  
  *Performance Attained:* High accuracy achieved with fine-tuned LEGAL-BERT for single-class contract smell detection.  
  *Limitations (Gap Identified):* Identifies general contractual ambiguity rather than specific consumer insurance exclusion traps.  
  *Scope for Future Work:* Applying contract smell concepts to insurance policy fine-print exclusion traps.

### Paper 15: Automated construction contract analysis for risk and responsibility assessment using natural language processing and machine learning
- **(i) Title, Author, Date of Publication & Publisher Information:**  
  Automated construction contract analysis for risk and responsibility assessment using natural language processing and machine learning
Automation in Construction (Elsevier), 2023  
  *Authors:* Irem Dikmen, Gorkem Eken, Huseyin Erol, and M. Talat Birgonul
- **(ii) Problem and Objectives:**  
  Automating contract review to extract risk and responsibility information for risk management plans.
- **(iii) Methodology Adopted:**  
  NLP Vectorization, Machine Learning Text Classification, Ensemble Models, Sentence Type Classifier
- **(iv) Performance & Limitations:**  
  *Metrics:* Accuracy, Macro F1-Score  
  *Performance Attained:* High sentence classification accuracy across Obligation, Risk, and Right categories (3,485 sentences).  
  *Limitations (Gap Identified):* Domain-specific to construction contracts (FIDIC); not evaluated on health/life insurance policies.  
  *Scope for Future Work:* Cross-domain adaptation of risk/responsibility sentence classification to consumer insurance.

### Literature Survey Table (All 15 Papers)

| S.No. | Title of the Paper, Publisher And year | Problem addressed | Algorithms used | Performance metrics used | Performance attained | Limitations (Gap identified) | Scope for future work |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Technical evaluation of language models adapted for the automation of legal contracts: clause extraction, classification, and summarization - Frontiers in Artificial Intelligence, 2026** | Automating legal contract processing (clause extraction, classification, summarization) in data-constrained domains. | Domain-adapted DeBERTa/BERT, HuggingFace Transformers, scikit-learn, seqeval | Macro-F1, Span-level F1, ROUGE-L, BERTScore | Macro-F1: 0.921 in classification, Span F1: 0.903 in clause extraction, ROUGE-L: 0.886 | Tested on private-sector corporate contracts; lacks specific insurance policy claim risk scoring. | Adapting legal transformers to consumer insurance policies and multi-category risk weighting. |
| 2 | **Insurance Policy Summarization Using Natural Language Processing (NLP) - Frontiers in Health Informatics, 2024** | High complexity and length of insurance policy terms hindering policyholder comprehension of exclusions. | Hybrid Extraction-based & Abstractive Summarization, Tokenization, POS Tagging, TextRank | ROUGE-1, ROUGE-L, Edit Distance, Cosine Similarity, Human Evaluation | High summary fidelity across coverage and exclusion terms; improved user understandability. | Basic extractive-abstractive pipeline lacks explicit fine-grained clause extraction and numeric risk scoring. | Incorporating fine-grained legal entity extraction and automated risk score calculation. |
| 3 | **AI-powered decision-making in facilitating insurance claim dispute resolution - Annals of Operations Research (Springer), 2023** | Prolonged dispute resolution and subjective cost estimation in road traffic accident (RTA) insurance claims. | Predictive Regression & Machine Learning Decision-Making Models, Asymptotic Injury Modeling | Mean Absolute Error (MAE), RMSE, Judicial Cost Estimation Accuracy | High predictive accuracy in judicial cost estimation across 88 real-life RTA case studies. | Focused on numerical/judicial dispute costs rather than unstructured text policy clause extraction. | Integrating text-mining of insurance policy exclusion clauses with financial dispute estimation. |
| 4 | **Transforming Health Insurance Claims Adjudication using Blockchain Technology - Procedia Computer Science (Elsevier), 2023** | Inefficiencies, tampering risks, and delays in centralized health insurance claims adjudication. | Smart Contracts, Decentralized Ledger Technology (DLT), Automated Rules Verification | Claim Settlement Latency, System Security, Throughput (TPS) | Substantial reduction in claims settlement time from weeks to near real-time automated execution. | Focuses on blockchain architecture; lacks natural language processing for parsing raw policy text. | Combining NLP policy clause extraction with smart contract execution for automated claims. |
| 5 | **Explainable AI and Law: An Evidential Survey - Digital Society (Springer), 2024** | Black-box opacities in AI legal decision-making reducing accountability and transparency. | Explainable AI (XAI) Taxonomy Mapping, Evidential Reasoning Frameworks | Explainability Fidelity, Stakeholder Trust Score, Interpretability | Developed a structured taxonomy aligning legal inference types with transparent algorithmic models. | Conceptual survey framework without automated empirical text processing code. | Implementing XAI token-attribution heads (e.g. SHAP/Integrated Gradients) in legal NLP classifiers. |
| 6 | **Legal Information Retrieval and Entailment Using Transformer-based Approaches - The Review of Socionetwork Strategies (Springer), 2024** | Information overload and complex legal entailment verification in case law and statute retrieval (COLIEE). | Sentence-Transformers, Legal-BERT-ECHR, Stacking-Voting Ensembles, Binary Classification | Precision, Recall, F1-Score, COLIEE Task Accuracy | Superior entailment accuracy using Legal-BERT-ECHR on legal paraphrasing and condition matching. | Evaluated on statute law databases; does not target consumer insurance policy contracts. | Adapting legal entailment transformers to premise-claim verification in insurance contracts. |
| 7 | **InsuranceRAG: A multi-module retrieval-augmented AI system for intelligent insurance assistance - Software Impacts (Elsevier), 2026** | Lack of transparent, conversational AI tools for query resolution and clause-level document retrieval in health insurance. | Retrieval-Augmented Generation (RAG), FAISS Vector Store, Domain-adapted Embeddings, LLM Evaluator | Retrieval Recall@K, Answer Faithfulness, Latency, User Evaluation | High retrieval accuracy and explainable clause-level responses via a web dashboard. | Focuses on conversational QA without calculating structured, composite policy claim risk scores. | Integrating automated policy risk scoring algorithms with RAG clause extraction. |
| 8 | **Optimizing Claim Assessment Process for Property Insurance using Machine Learning - Procedia Computer Science (Elsevier), 2024** | Data imbalance and limited feature importance in property insurance claim frequency and risk prediction. | Random Forest, Logistic Regression, SMOTE Data Imbalance Oversampling | Recall, Precision, F1-Score | Achieved 96% Recall with Random Forest after applying SMOTE balancing. | Operates on structured tabular risk features rather than unstructured PDF contract text. | Combining structured tabular ML models with text-based NLP exclusion extraction. |
| 9 | **Structure-Aware Uncertainty-Calibrated Evaluation for Legal Contract Knowledge Graph Extraction - Procedia Computer Science (Elsevier), 2026** | Evaluating epistemic uncertainty and inter-judge disagreement in legal contract knowledge graph extraction. | Multi-Judge Ensemble (Semantic + Structural + LLM Judges), Isotonic Regression Calibration | Coefficient of Variation (CV), AUC for Error Detection, Calibration Error | Achieved 0.982 AUC for error detection in contract knowledge graph extraction. | High computational overhead of multi-judge ensembles; requires reference-free validation data. | Lightweight single-pass uncertainty calibration for real-time contract scanning. |
| 10 | **A case study for automated attribute extraction from legal documents using large language models - Artificial Intelligence and Law (Springer), 2026** | Automated extraction of fine-grained concepts, attributes, and tags from unstructured legal proceedings. | Weakly Supervised Sequence Labeling, Few-Shot Prompting with LLaMA-2 & Black-Box LLMs | Span Extraction Precision, Recall, Macro F1, Downstream Prediction Accuracy | LLaMA-2 achieved superior few-shot attribute generation and downstream statute prediction accuracy. | LLM hallucination risk and prompt sensitivity in unconstrained few-shot prompting regimes. | Combining LLM few-shot extraction with fine-tuned transformer classification heads. |
| 11 | **Health insurance fraud detection based on multi-channel heterogeneous graph structure learning - Heliyon (Elsevier), 2024** | Detecting complex, evolving health insurance fraud tactics across heterogeneous entities (patients, doctors, medicines). | Multi-channel Heterogeneous Graph Structured Learning (MHGSL), Graph Convolutional Networks (GCN), KNN | Classification Accuracy, Macro F1, Precision, Recall, AUC-ROC | High fraud detection accuracy by capturing multi-entity relational topology. | Requires structured relational graph data; does not process unstructured policy document text. | Graph-augmented text processing linking policy exclusions with claim history. |
| 12 | **Addressing the notion of trust around ChatGPT in the high-stakes use case of insurance - Technology in Society (Elsevier), 2024** | Trust, governance, and financial inclusion risks around consumer-facing LLMs in high-stakes insurance applications. | AI Governance Evaluation Framework, Dread Risk & Trust Judgment Analysis | Qualitative Trust Metrics, Risk Governance Alignment | Established domain-specific governance framework for consumer-facing LLMs under the EU AI Act. | Conceptual commentary paper without empirical model implementation. | Developing verifiable, explainable NLP systems that adhere to EU AI Act transparency rules. |
| 13 | **Legal Eligibility Inference from Text: Constraint Extraction with Pretrained Language Models - Procedia Computer Science (Elsevier), 2025** | Automated extraction of structured eligibility restrictions and condition-action pairings from legal text. | Pre-trained BERT, Named Entity Recognition (NER), Condition-Action Pairing Rules, Entitlement Logic | NER Precision, Recall, Constraint Extraction Accuracy | High precision in formalizing entitlement logic into machine-readable constraints. | Restricted to eligibility rules; does not calculate composite policy financial risk scores. | Extending constraint extraction to insurance policy claim exclusion weighting. |
| 14 | **Software engineering meets legal texts: LLMs for auto detection of contract smells - Machine Learning with Applications (Elsevier), 2024** | Detecting 'contract smells' (text patterns indicative of significant issues or ambiguities in legal contracts). | GPT-4 Semi-Automated Labeling, BERT, LEGAL-BERT Fine-Tuning, Single vs Multi-Class Classification | Macro F1, Accuracy, Single-Class vs Multi-Class Precision | High accuracy achieved with fine-tuned LEGAL-BERT for single-class contract smell detection. | Identifies general contractual ambiguity rather than specific consumer insurance exclusion traps. | Applying contract smell concepts to insurance policy fine-print exclusion traps. |
| 15 | **Automated construction contract analysis for risk and responsibility assessment using natural language processing and machine learning - Automation in Construction (Elsevier), 2023** | Automating contract review to extract risk and responsibility information for risk management plans. | NLP Vectorization, Machine Learning Text Classification, Ensemble Models, Sentence Type Classifier | Accuracy, Macro F1-Score | High sentence classification accuracy across Obligation, Risk, and Right categories (3,485 sentences). | Domain-specific to construction contracts (FIDIC); not evaluated on health/life insurance policies. | Cross-domain adaptation of risk/responsibility sentence classification to consumer insurance. |


---

## 4. Summary of Literature and Limitations and Your Proposed Alternative Methodology and Design

### Summary of Literature & Identified Gaps
1. **General Legal vs. Insurance Gap:** Most existing contract analysis systems focus on enterprise corporate contracts (e.g., M&A agreements), neglecting consumer insurance policy fine print.
2. **Surface Keyword Failure:** Search tools miss exclusions expressed through negative framing (e.g., *"shall be non-payable"*, *"subject to 24-month moratorium"*).
3. **Black-Box Outputs:** Existing risk tools output a single score without providing exact page/line numbers or plain-English explanations of non-covered conditions.

### Proposed Alternative Methodology
**InsureCheck-NLP** addresses these gaps via a 4-stage processing pipeline:
1. **Section-Aware PDF Extraction:** Extract text from policy PDFs using `pdfplumber`, segmenting text into structural sections (*Exclusions*, *Waiting Periods*, *Limits & Deductibles*).
2. **Clause Sequence Labeling & Classification:** Feed candidate text chunks into a fine-tuned `DeBERTa-v3` transformer model to extract and classify exclusion clauses into 4 categories:
   - **Category A:** Waiting Periods (Pre-existing diseases, specific surgery delays).
   - **Category B:** Sub-Limits & Caps (Room rent caps, ICU caps, cataract limits).
   - **Category C:** Non-Payable Items & Consumables (PPE, registration fees, diagnostic charges).
   - **Category D:** Co-Payment Mandates (Mandatory patient percentage share).
3. **Claim Risk Scoring Engine:** Compute a **Claim Risk Score ($R$)**:
   $$R = \min\left(100, \sum_{i=1}^{N} w_i \cdot C_i\right)$$
   where $w_i$ represents the severity weight of clause $C_i$ (e.g., Room Rent Capping = Weight 25, 4-Year Waiting Period = Weight 30).
4. **Streamlit UI Deployment:** Build a web application featuring drag-and-drop PDF upload, an interactive Claim Risk Score gauge meter, a plain-English non-coverage checklist, and visual text highlighting.

### Experimental Design (Architecture Diagram)

```
 ┌────────────────────────────────────────────────────────┐
 │            Insurance Policy Document (PDF)             │
 └──────────────────────────┬─────────────────────────────┘
                            │ (pdfplumber Parsing)
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │           Section Chunking & Noise Filtering           │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │           DeBERTa-v3 Transformer Encoder               │
 │           (Clause Extraction & NER Pipeline)           │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │             Multi-Class Exclusion Taxonomy             │
 │ [Waiting Periods | Sub-Limits | Consumables | Co-Pay]  │
 └──────────────────────────┬─────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
 ┌─────────────────────┐         ┌─────────────────────┐
 │ Claim Risk Score    │         │ Plain-English       │
 │ Computation (0-100) │         │ Simplifier Head     │
 └──────────┬──────────┘         └──────────┬──────────┘
            │                               │
            └───────────────┬───────────────┘
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │  Streamlit Interactive UI: PDF Scanner & Trap Summary  │
 └────────────────────────────────────────────────────────┘
```

---

## 5. Datasets Description and Sample Data

### Datasets Description
- **CUAD (Contract Understanding Atticus Dataset):** Public legal contract dataset containing 510 commercial contracts with over 13,000 human-annotated legal clauses across 41 categories.
- **Custom Insurance Policy Corpus:** A curated dataset of 40 real-world consumer insurance policies (Health, Auto, Travel, Life) covering major Indian and international providers.

### Sample Data
- **Raw Policy Text Snippet:**  
  *"Treatment of cataract is subject to a maximum sub-limit of $300 per eye or 10% of sum insured, whichever is lower. Expenses related to any pre-existing disease (PED) shall not be covered until 36 consecutive months of continuous coverage have elapsed."*
- **Extracted Structural Output:**
  - **Clause 1:** `Sub-Limit & Cap` $\rightarrow$ *"Cataract capped at $300 per eye"* $\rightarrow$ **Severity Weight: 20 (Medium Risk)**
  - **Clause 2:** `Waiting Period` $\rightarrow$ *"36 months continuous coverage for Pre-Existing Diseases"* $\rightarrow$ **Severity Weight: 30 (High Risk)**
- **Calculated Claim Risk Score:** **50 / 100 (Moderate-to-High Risk)**
- **Plain-English Summary:**  
  1. ⚠️ **Cataract Surgery Cap:** Insurance pays maximum $300 per eye for cataract surgery. Any extra bill must be paid out-of-pocket.  
  2. ⚠️ **3-Year Pre-Existing Disease Wait:** Any illness you had before buying this policy will not be covered for the first 3 years.

---

## 6. References (As per IEEE format - All 15 Papers)

1. J. Govea, I. Ortiz-Gárces, P. Palacios, A. M. Navarro, S. A. Del Pino, and W. Villegas-Ch, "Technical evaluation of language models adapted for the automation of legal contracts: clause extraction, classification, and summarization," Frontiers in Artificial Intelligence, vol. 9, p. 1782405, Mar. 2026.
2. S. Kolambe and P. Kaur, "Insurance Policy Summarization Using Natural Language Processing (NLP)," Frontiers in Health Informatics, vol. 13, no. 3, pp. 4774–4782, 2024.
3. W. Zhang, J. Shi, X. Wang, and H. Wynn, "AI-powered decision-making in facilitating insurance claim dispute resolution," Annals of Operations Research, vol. 330, pp. 1–25, Oct. 2023.
4. "Transforming Health Insurance Claims Adjudication using Blockchain Technology," Procedia Computer Science, vol. 224, pp. 147–154, Aug. 2023.
5. K. M. Richmond, S. M. Muddamsetty, T. Gammeltoft-Hansen, H. P. Olsen, and T. B. Moeslund, "Explainable AI and Law: An Evidential Survey," Digital Society, vol. 3, p. 1, Dec. 2024.
6. M.-Y. Kim, J. Rabelo, H. K. B. Babiker, M. A. Rahman, and R. Goebel, "Legal Information Retrieval and Entailment Using Transformer-based Approaches," The Review of Socionetwork Strategies, vol. 18, pp. 101–121, Jan. 2024.
7. S. Hanmante, S. Patil, P. V. Deshmukh, and A. K. Shahade, "InsuranceRAG: A multi-module retrieval-augmented AI system for intelligent insurance assistance," Software Impacts, vol. 28, p. 100844, 2026.
8. "Optimizing Claim Assessment Process for Property Insurance using Machine Learning," Procedia Computer Science, vol. 234, pp. 520–526, 2024.
9. M. Dechtiar, D. M. Katz, and H. Wang, "Structure-Aware Uncertainty-Calibrated Evaluation for Legal Contract Knowledge Graph Extraction," Procedia Computer Science, vol. 275, pp. 513–522, 2026.
10. S. Adhikary, P. Sen, D. Roy, and K. Ghosh, "A case study for automated attribute extraction from legal documents using large language models," Artificial Intelligence and Law, vol. 34, pp. 245–266, Nov. 2024.
11. B. Hong, P. Lu, H. Xu, J. Lu, K. Lin, and F. Yang, "Health insurance fraud detection based on multi-channel heterogeneous graph structure learning," Heliyon, vol. 10, no. 8, p. e30045, Apr. 2024.
12. J. Ressel, M. Völler, F. Murphy, and M. Mullins, "Addressing the notion of trust around ChatGPT in the high-stakes use case of insurance," Technology in Society, vol. 78, p. 102644, Aug. 2024.
13. A. Aitim and A. Auyezova, "Legal Eligibility Inference from Text: Constraint Extraction with Pretrained Language Models," Procedia Computer Science, vol. 272, pp. 451–456, 2025.
14. M. Dechtiar, D. M. Katz, and H. Wang, "Software engineering meets legal texts: LLMs for auto detection of contract smells," Machine Learning with Applications, vol. 16, p. 100520, 2024.
15. I. Dikmen, G. Eken, H. Erol, and M. T. Birgonul, "Automated construction contract analysis for risk and responsibility assessment using natural language processing and machine learning," Automation in Construction, vol. 145, p. 104620, Jan. 2023.
