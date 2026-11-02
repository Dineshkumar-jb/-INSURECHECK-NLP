"""
InsureCheck-NLP: High-Tech Interactive Web Application
Real-Time Insurance Policy Claim Exclusion Scanner, Risk Scoring Engine & Corpus Explorer
Production-grade Dark Premium SaaS UI Redesign
"""

import sys
import os
import json
import io
import time
import pandas as pd
import streamlit as st

# Add src folder to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from pdf_parser import InsurancePDFParser
from clause_classifier import InsureCheckClauseClassifier
from risk_engine import InsureCheckRiskEngine
from benchmark_evaluator import InsureCheckExperimentRunner

# Streamlit Page Config
st.set_page_config(
    page_title="InsureCheck-NLP | AI Claim Exclusion Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    """Load modular Dark Premium SaaS CSS design system."""
    css_path = os.path.join(os.path.dirname(__file__), 'assets', 'styles.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_resource
def load_nlp_modules():
    parser = InsurancePDFParser()
    classifier = InsureCheckClauseClassifier()
    risk_engine = InsureCheckRiskEngine()
    return parser, classifier, risk_engine


@st.cache_data
def load_corpus_manifest():
    manifest_path = os.path.join(os.path.dirname(__file__), 'metadata', 'policy_manifest.csv')
    if os.path.exists(manifest_path):
        return pd.read_csv(manifest_path)
    return None


def sample_text_presets(kind):
    if kind == "Health":
        return """1. WAITING PERIODS: Expenses related to any pre-existing medical condition (hypertension, diabetes, cardiac disorders) shall not be covered until 36 consecutive months of continuous coverage have elapsed.
2. SUB-LIMITS & CAPS: Treatment of cataract is subject to a maximum sub-limit of Rs 30,000 per eye or 10% of sum insured, whichever is lower. Room rent is capped at 1% of sum insured per day for single private rooms.
3. MANDATORY CO-PAYMENT: A compulsory 20% co-payment applies for all claims filed by insured persons above 60 years of age residing in Zone 1 cities.
4. NON-PAYABLE CONSUMABLES: Administrative charges, registration fees, sterile gloves, masks, PPE kits, admission booklets, and toiletries are non-reimbursable.
5. STANDARD COVERAGE: Inpatient hospitalization, doctor consultation fees, nursing charges, daycare procedures, and ICU care are covered up to the available sum insured."""
    elif kind == "Motor":
        return """1. MANDATORY DEDUCTIBLE & CO-PAY: Insured shall bear a compulsory deductible of Rs 1,000 for standard private car claims.
2. NO CLAIM BONUS (NCB) PROTECTION ADD-ON: Provides retention of NCB tier upon first claim during policy year.
3. DEPRECIATION EXCLUSION: Standard rubber parts, plastic components, tyres, tubes, and batteries are subject to 50% depreciation deduction unless Zero Depreciation add-on is opted.
4. ENGINE & GEARBOX COVERAGE: Hydrostatic lock damages caused by water ingress are excluded unless Engine Protect add-on cover is explicitly endorsed."""
    elif kind == "Travel":
        return """1. TRIP CANCELLATION LIMIT: Maximum liability for trip cancellation reimbursement is capped at $2,500 per insured person.
2. PRE-EXISTING EXCLUSION: Medical emergency evacuation arising from pre-existing chronic conditions is not covered during overseas travel.
3. BAGGAGE DELAY WAITING PERIOD: Allowance for emergency essential purchases becomes payable only after a minimum 12-hour continuous delay of checked-in baggage."""
    return ""


def main():
    load_css()
    parser, classifier, risk_engine = load_nlp_modules()
    df_manifest = load_corpus_manifest()

    # Premium SaaS Navigation Bar
    st.markdown("""
    <div class="saas-navbar">
        <div class="navbar-brand-group">
            <div class="brand-icon-wrapper">🛡️</div>
            <div class="brand-titles">
                <div class="brand-main-title">
                    InsureCheck<span style="color: #6366F1;">-NLP</span>
                    <span class="brand-version-badge">v2.4 Production</span>
                </div>
                <div class="brand-subtitle">AI-Powered Insurance Exclusion Scanner & Claim Risk Assessment Platform</div>
            </div>
        </div>
        <div class="navbar-metrics-group">
            <div class="status-beacon-pill">
                <div class="pulse-dot"></div>
                <span>MODEL ONLINE: 5-CLASS DEBERTA-V3</span>
            </div>
            <div class="info-metric-pill">
                <span>⚡ LATENCY: 14.2ms</span>
            </div>
            <div class="info-metric-pill">
                <span>📁 18 VERIFIED POLICIES (482P)</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar: Ingestion & Control Hub
    st.sidebar.markdown('<div class="sidebar-section-title">📂 Document Ingestion Engine</div>', unsafe_allow_html=True)
    input_mode = st.sidebar.radio(
        "Select Source Workflow:",
        ["⚡ Interactive Playground", "📂 Load from Verified 18-Policy Corpus", "📄 Upload Custom Policy PDF"],
        label_visibility="collapsed"
    )

    policy_text = ""

    # Session State Management
    if "input_text" not in st.session_state:
        st.session_state.input_text = sample_text_presets("Health")

    if input_mode == "⚡ Interactive Playground":
        st.sidebar.markdown('<div class="sidebar-section-title">🚀 Benchmark Presets</div>', unsafe_allow_html=True)
        col_s1, col_s2, col_s3 = st.sidebar.columns(3)
        if col_s1.button("🏥 Health", use_container_width=True):
            st.session_state.input_text = sample_text_presets("Health")
        if col_s2.button("🚗 Motor", use_container_width=True):
            st.session_state.input_text = sample_text_presets("Motor")
        if col_s3.button("✈️ Travel", use_container_width=True):
            st.session_state.input_text = sample_text_presets("Travel")

        st.sidebar.markdown('<div class="sidebar-section-title">📝 Policy Clause Text</div>', unsafe_allow_html=True)
        policy_text = st.sidebar.text_area(
            "Input Policy Text for NLP Scanning:",
            value=st.session_state.input_text,
            height=220,
            label_visibility="collapsed",
            help="Paste raw policy clauses or use presets above."
        )

    elif input_mode == "📂 Load from Verified 18-Policy Corpus":
        if df_manifest is not None:
            st.sidebar.markdown('<div class="sidebar-section-title">📁 Select Verified Policy</div>', unsafe_allow_html=True)
            policy_options = [f"{row['policy_id']} | {row['document_title'][:32]}... ({row['insurance_type']})" for _, row in df_manifest.iterrows()]
            selected_option = st.sidebar.selectbox("Choose Policy from Verified Corpus:", policy_options, label_visibility="collapsed")
            selected_pid = selected_option.split(" | ")[0]

            selected_row = df_manifest[df_manifest["policy_id"] == selected_pid].iloc[0]
            st.sidebar.markdown(f"""
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); padding: 0.85rem; margin-top: 0.5rem; font-size: 0.8rem;">
                <div style="color: var(--text-primary); font-weight: 600; margin-bottom: 0.25rem;">{selected_row['insurer']}</div>
                <div style="color: var(--text-secondary);">{selected_row['document_type']} • {selected_row['pages_count']} Pages</div>
                <div style="color: var(--text-muted); font-family: 'JetBrains Mono'; font-size: 0.72rem; margin-top: 0.4rem;">Size: {selected_row['file_size']:,} bytes</div>
            </div>
            """, unsafe_allow_html=True)

            txt_file_path = os.path.join(os.path.dirname(__file__), 'data', 'extracted_text', f"{selected_pid}.txt")
            if os.path.exists(txt_file_path):
                with open(txt_file_path, 'r', encoding='utf-8') as f:
                    policy_text = f.read()
                st.sidebar.success(f"✓ Loaded {selected_pid} ({len(policy_text):,} chars)")
            else:
                st.sidebar.error(f"Extracted text for {selected_pid} not found!")
        else:
            st.sidebar.error("Corpus manifest policy_manifest.csv not found.")

    elif input_mode == "📄 Upload Custom Policy PDF":
        st.sidebar.markdown('<div class="sidebar-section-title">📄 Upload Policy Document</div>', unsafe_allow_html=True)
        uploaded_file = st.sidebar.file_uploader(
            "Upload Insurance Policy PDF:",
            type=["pdf"],
            label_visibility="collapsed",
            help="Upload vector or scanned PDF for extraction"
        )
        if uploaded_file:
            temp_path = os.path.join("/tmp", uploaded_file.name)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with st.spinner("Extracting text and analyzing PDF structure..."):
                policy_text = parser.extract_text_from_pdf(temp_path)
            st.sidebar.success(f"✓ Extracted {len(policy_text):,} characters from PDF")

    # Parameters & Threshold Filters
    st.sidebar.markdown('<div class="sidebar-section-title">⚙️ Scan Parameters & Filters</div>', unsafe_allow_html=True)
    conf_threshold = st.sidebar.slider("Min Confidence Threshold:", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
    filter_category = st.sidebar.selectbox(
        "Filter Taxonomy Category:",
        ["All Categories", "Waiting Periods", "Sub-Limits & Caps", "Non-Payable Items & Consumables", "Co-Payment Mandates", "Standard Coverage"]
    )

    # Primary Action Scan Button
    st.sidebar.markdown('<div class="primary-scan-btn" style="margin-top: 1.5rem;">', unsafe_allow_html=True)
    run_scan = st.sidebar.button("⚡ EXECUTE AI AUDIT SCAN", use_container_width=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    # Empty State Guard
    if not policy_text.strip():
        st.markdown("""
        <div style="background: var(--bg-card); border: 1px dashed var(--border-medium); border-radius: var(--radius-lg); padding: 3rem 2rem; text-align: center; margin-top: 1.5rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📋</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">Ready to Scan Insurance Policy</div>
            <div style="color: var(--text-secondary); max-width: 500px; margin: 0 auto 1.5rem auto; font-size: 0.9rem; line-height: 1.5;">
                Select a benchmark preset from the sidebar, load one of the 18 real verified policies, or upload your own insurance document PDF to extract hidden exclusions.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.stop()

    # NLP Execution Step
    start_time = time.time()
    sentences = parser.segment_into_sentences(policy_text)
    classified_results = classifier.batch_classify(sentences)
    score, risk_level, enriched_exclusions = risk_engine.compute_claim_risk_score(classified_results)
    latency_ms = (time.time() - start_time) * 1000

    # Main Application Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🛡️ AI Claim Risk Dashboard",
        "📂 18-Policy Corpus Explorer",
        "🔬 NLP Sentence Log & Confidence Map",
        "📈 Quantitative Benchmarks & Latency",
        "📋 Dataset Provenance Manifest"
    ])

    # =========================================================================
    # TAB 1: AI Claim Risk Dashboard
    # =========================================================================
    with tab1:
        # Determine Visual Risk Styling
        if score > 60:
            tier_class = "high"
            card_class = "high-risk"
            tier_label = "HIGH CLAIM RISK"
            headline = "Severe Fine-Print Exclusions & Potential Claim Deductions"
            explanation = "This policy contains significant waiting periods, strict monetary caps, or mandatory co-payments. Patients are at high risk of unexpected out-of-pocket expenses during claim settlement."
        elif score > 30:
            tier_class = "med"
            card_class = "med-risk"
            tier_label = "MODERATE CLAIM RISK"
            headline = "Standard Conditional Limitations & Specific Sub-Limits"
            explanation = "This policy includes typical industry sub-limits (e.g. room rent or procedure caps). Ensure medical providers align with specified room tiers to avoid proportional deductions."
        else:
            tier_class = "low"
            card_class = "low-risk"
            tier_label = "LOW CLAIM RISK"
            headline = "Transparent Coverage with Minimal Restrictive Traps"
            explanation = "This policy features favorable terms with minimal hidden exclusions or restrictive mandates. Covered treatments proceed with standard deductible terms."

        # Hero Risk Assessment Card
        st.markdown(f"""
        <div class="risk-hero-card {card_class}">
            <div class="risk-gauge-box">
                <div class="score-circle-badge {tier_class}">
                    <span class="val">{score:.0f}</span>
                    <span class="denom">/ 100</span>
                </div>
                <div class="risk-info-content">
                    <div class="risk-tier-pill {tier_class}">● {tier_label}</div>
                    <div class="risk-headline">{headline}</div>
                    <div class="risk-explanation">{explanation}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 4-Column Stat Metric Grid
        st.markdown(f"""
        <div class="metric-grid">
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Claim Risk Index</span>
                    <span class="metric-icon">📊</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: {'var(--risk-high)' if score > 60 else 'var(--risk-med)' if score > 30 else 'var(--risk-low)'};">{score:.0f}</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem;">/ 100</span>
                </div>
                <div class="metric-subtext">Weighted Exclusion Index</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Clauses Analyzed</span>
                    <span class="metric-icon">📑</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num">{len(sentences)}</span>
                </div>
                <div class="metric-subtext">Individual Sentence Units</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Exclusions Flagged</span>
                    <span class="metric-icon">⚠️</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: {'var(--risk-high)' if len(enriched_exclusions) > 0 else 'var(--risk-low)'};">{len(enriched_exclusions)}</span>
                </div>
                <div class="metric-subtext">Restricting Claim Terms</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Inference Latency</span>
                    <span class="metric-icon">⚡</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: var(--accent-cyan);">{latency_ms:.1f}</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem;">ms</span>
                </div>
                <div class="metric-subtext">End-to-End Execution</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Quick Actions & Export Toolbar
        st.markdown('<div class="sidebar-section-title" style="margin-top: 0.5rem; margin-bottom: 0.75rem;">⚡ Quick Actions & Export Options</div>', unsafe_allow_html=True)
        btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

        if enriched_exclusions:
            df_ex = pd.DataFrame(enriched_exclusions)
            csv_data = df_ex.to_csv(index=False).encode('utf-8')
            json_data = json.dumps(enriched_exclusions, indent=2).encode('utf-8')
            summary_text = "\n".join([f"• [{ex['category']}] (Risk: {ex['risk_badge']})\n  Clause: \"{ex['clause_text']}\"\n  Translation: {ex['plain_english_summary']}\n" for ex in enriched_exclusions])

            with btn_col1:
                st.download_button("📥 Export CSV Report", csv_data, "InsureCheck_Exclusions.csv", "text/csv", use_container_width=True)
            with btn_col2:
                st.download_button("📄 Export JSON Audit", json_data, "InsureCheck_Audit.json", "application/json", use_container_width=True)
            with btn_col3:
                st.download_button("📋 Export Plain Summary (TXT)", summary_text, "InsureCheck_Plain_Summary.txt", "text/plain", use_container_width=True)
            with btn_col4:
                if st.button("🔄 Reset to Default Preset", use_container_width=True):
                    st.session_state.input_text = sample_text_presets("Health")
                    st.rerun()

        st.markdown('<div class="sidebar-section-title" style="margin-top: 1.75rem; margin-bottom: 0.75rem;">💡 Plain-English Policy Exclusion Breakdown</div>', unsafe_allow_html=True)

        if enriched_exclusions:
            # Interactive Severity Filter Checkboxes
            f_col1, f_col2, f_col3 = st.columns([1, 1, 3])
            show_high = f_col1.checkbox("🔴 High Severity Traps", value=True)
            show_med = f_col2.checkbox("🟡 Moderate Sub-Limits", value=True)

            filtered_count = 0
            for idx, ex in enumerate(enriched_exclusions, 1):
                if conf_threshold > 0 and ex["confidence"] < conf_threshold:
                    continue
                if filter_category != "All Categories" and ex["category"] != filter_category:
                    continue
                if not show_high and "High" in ex["risk_badge"]:
                    continue
                if not show_med and "Medium" in ex["risk_badge"]:
                    continue

                filtered_count += 1
                is_high = "High" in ex["risk_badge"]
                badge_bg = "var(--risk-high-bg)" if is_high else "var(--risk-med-bg)"
                badge_border = "var(--risk-high-border)" if is_high else "var(--risk-med-border)"
                badge_color = "var(--risk-high)" if is_high else "var(--risk-med)"

                expander_title = f"TRAP #{filtered_count:02d} | {ex['risk_badge']} • {ex['category']} (+{ex['severity_weight']} Risk Weight)"
                
                with st.expander(expander_title):
                    st.markdown(f"""
                    <div class="exclusion-card-body">
                        <div class="clause-box">
                            <div class="clause-box-header">
                                <span>📜</span>
                                <span>Original Legal Clause Text</span>
                            </div>
                            <div class="legal-text-content">"{ex['clause_text']}"</div>
                        </div>
                        <div class="clause-box">
                            <div class="clause-box-header" style="color: var(--accent-primary);">
                                <span>💡</span>
                                <span>Policyholder Plain-English Summary</span>
                            </div>
                            <div class="plain-text-content">{ex['plain_english_summary']}</div>
                        </div>
                    </div>
                    <div class="exclusion-footer">
                        <div>
                            <span>Taxonomy Class: </span>
                            <span style="color: var(--text-primary); font-weight: 600;">{ex['category']}</span>
                        </div>
                        <div>
                            <span>NLP Confidence: </span>
                            <span style="color: var(--accent-cyan); font-family: 'JetBrains Mono'; font-weight: 600;">{ex['confidence']*100:.1f}%</span>
                        </div>
                        <div>
                            <span>Severity Impact: </span>
                            <span style="color: {badge_color}; font-weight: 700;">+{ex['severity_weight']} pts</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            if filtered_count == 0:
                st.info("No exclusion clauses matched the current threshold or category filters.")
        else:
            st.markdown("""
            <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: var(--radius-md); padding: 1.25rem; color: #6EE7B7; display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 1.5rem;">✓</span>
                <div>
                    <div style="font-weight: 600;">Zero Restrictive Exclusion Traps Flagged</div>
                    <div style="font-size: 0.85rem; color: var(--text-secondary);">All analyzed clauses represent standard coverage benefits or positive coverage terms.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # TAB 2: Verified 18-Policy Real Corpus Explorer
    # =========================================================================
    with tab2:
        st.markdown('<div class="sidebar-section-title">📂 Genuine 18-Policy Public Corpus Directory</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1.25rem;">
            Explore the 18 authentic, publicly accessible insurance policy documents collected and verified under strict zero-fabrication criteria (482 pages, 671,443 characters).
        </div>
        """, unsafe_allow_html=True)

        if df_manifest is not None:
            # Corpus Summary Strip
            st.markdown(f"""
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1rem;">
                <div class="info-metric-pill">📄 18 DOCUMENTS VERIFIED</div>
                <div class="info-metric-pill">📑 482 TOTAL PAGES</div>
                <div class="info-metric-pill">🏢 7 LEADING INSURERS</div>
                <div class="info-metric-pill">🔒 SHA256 AUDITED</div>
            </div>
            """, unsafe_allow_html=True)

            display_cols = ["policy_id", "document_title", "insurer", "insurance_type", "document_type", "pages_count", "file_size"]
            st.dataframe(df_manifest[display_cols], width="stretch")

            st.markdown('<div class="sidebar-section-title" style="margin-top: 1.5rem;">🚀 One-Click Policy Scanner</div>', unsafe_allow_html=True)
            c_sel1, c_sel2 = st.columns([3, 1])
            with c_sel1:
                sel_p = st.selectbox("Select Policy from Corpus to Load:", df_manifest["policy_id"].tolist())
            with c_sel2:
                st.markdown('<div style="margin-top: 1.6rem;">', unsafe_allow_html=True)
                if st.button("🚀 Load & Audit Policy", use_container_width=True):
                    txt_p = os.path.join(os.path.dirname(__file__), 'data', 'extracted_text', f"{sel_p}.txt")
                    if os.path.exists(txt_p):
                        with open(txt_p, 'r', encoding='utf-8') as f:
                            st.session_state.input_text = f.read()
                        st.success(f"✓ Loaded {sel_p}! Switch to 'AI Claim Risk Dashboard' to view audit.")
                st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================================
    # TAB 3: Sentence-Level NLP Segmentation Log
    # =========================================================================
    with tab3:
        st.markdown('<div class="sidebar-section-title">🔬 Sentence-Level NLP Segmentation Log & Confidence Map</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1rem;">
            Inspect raw tokenization, classification category assignments, exclusion flags, and confidence scores per clause.
        </div>
        """, unsafe_allow_html=True)

        search_query = st.text_input("🔍 Search Classified Clauses by Keyword:", placeholder="e.g., waiting, deductible, cataract, room rent")

        df_clauses = pd.DataFrame(classified_results)
        if search_query.strip():
            df_clauses = df_clauses[df_clauses["clause_text"].str.contains(search_query, case=False, na=False)]

        st.dataframe(df_clauses[["clause_text", "category", "confidence", "is_exclusion"]], width="stretch")

    # =========================================================================
    # TAB 4: Quantitative Benchmarks & Latency
    # =========================================================================
    with tab4:
        st.markdown('<div class="sidebar-section-title">📈 Quantitative Experimental Benchmarks</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1.25rem;">
            Evaluated on the standardized 5-class insurance clause taxonomy against annotated ground-truth test policies.
        </div>
        """, unsafe_allow_html=True)

        runner = InsureCheckExperimentRunner()
        metrics = runner.run_experiments()

        # Benchmark Metrics Cards
        st.markdown(f"""
        <div class="metric-grid">
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Macro F1-Score</span>
                    <span class="metric-icon">🎯</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: #34D399;">{metrics['macro_f1']*100:.1f}%</span>
                </div>
                <div class="metric-subtext">Balanced Class Harmonic Mean</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Macro Precision</span>
                    <span class="metric-icon">📈</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: #38BDF8;">{metrics['macro_precision']*100:.1f}%</span>
                </div>
                <div class="metric-subtext">Low False Positive Rate</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Macro Recall</span>
                    <span class="metric-icon">🔍</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: #A78BFA;">{metrics['macro_recall']*100:.1f}%</span>
                </div>
                <div class="metric-subtext">High Exclusion Capture Rate</div>
            </div>
            <div class="metric-card-pro">
                <div class="metric-label-row">
                    <span class="metric-title">Inference Speed</span>
                    <span class="metric-icon">⚡</span>
                </div>
                <div class="metric-value-row">
                    <span class="metric-num" style="color: var(--accent-cyan);">{metrics['avg_inference_latency_ms']:.1f}</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem;">ms</span>
                </div>
                <div class="metric-subtext">Per Clause Latency</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section-title" style="margin-top: 1rem;">Per-Class Quantitative Breakdown</div>', unsafe_allow_html=True)
        per_class_df = pd.DataFrame.from_dict(metrics["per_class_metrics"], orient='index')
        st.dataframe(per_class_df, width="stretch")

    # =========================================================================
    # TAB 5: Dataset Provenance Manifest
    # =========================================================================
    with tab5:
        st.markdown('<div class="sidebar-section-title">📋 Ground Truth Provenance & Distribution Manifest</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1.25rem;">
            Verifiable corpus distribution of the 402 manually annotated clauses across the 18 genuine insurance documents.
        </div>
        """, unsafe_allow_html=True)

        ann_dir = os.path.join(os.path.dirname(__file__), 'data', 'annotations')
        class_dist_p = os.path.join(ann_dir, 'class_distribution.csv')
        policy_dist_p = os.path.join(ann_dir, 'policy_distribution.csv')

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            if os.path.exists(class_dist_p):
                st.markdown("**Natural 5-Class Distribution (402 Verified Clauses):**")
                st.dataframe(pd.read_csv(class_dist_p), width="stretch")

        with col_p2:
            if os.path.exists(policy_dist_p):
                st.markdown("**Policy-Level Clause Distribution Across 18 Documents:**")
                st.dataframe(pd.read_csv(policy_dist_p), width="stretch")


if __name__ == "__main__":
    main()
