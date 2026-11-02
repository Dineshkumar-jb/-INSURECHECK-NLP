"""
InsureCheck-NLP: PDF Document Parser Module
Extracts unstructured text from Insurance Policy PDFs, performs section-aware chunking,
and isolates Exclusion, Waiting Period, Sub-Limit, and Co-Pay sections.
"""

import re
import os
from typing import List, Dict, Any

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


class InsurancePDFParser:
    def __init__(self):
        # Section detection regex patterns
        self.section_patterns = {
            "exclusions": r"(?:general\s+)?exclusions|what\s+is\s+not\s+covered|items\s+excluded|non-payable",
            "waiting_periods": r"waiting\s+period|pre-existing\s+(?:diseases|conditions)|specific\s+waiting\s+period",
            "sub_limits": r"sub-limit|capping|maximum\s+limit|cap\s+on\s+(?:room|cataract|treatment)",
            "co_pay": r"co-payment|deductible|patient\s+share|co-pay"
        }

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extracts full text from a PDF file path."""
        text = ""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at path: {pdf_path}")

        # Try pypdf first for speed
        if PdfReader:
            try:
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
            except Exception as e:
                text = ""

        # Fallback to pdfplumber if text is sparse or pypdf failed
        if len(text.strip()) < 100 and pdfplumber:
            try:
                with pdfplumber.open(pdf_path) as pdf:
                    for page in pdf.pages:
                        extracted = page.extract_text()
                        if extracted:
                            text += extracted + "\n"
            except Exception as e:
                pass

        return text

    def segment_into_sentences(self, text: str) -> List[str]:
        """Splits extracted text into clean candidate sentences/clauses."""
        # Clean formatting noise
        text = re.sub(r'\r\n|\r', '\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        
        # Split by sentence boundaries and bullet points
        raw_chunks = re.split(r'(?<=[.!?])\s+|\n+(?=[•\-*\d+\.\)])', text)
        
        sentences = []
        for chunk in raw_chunks:
            cleaned = chunk.strip()
            # Retain meaningful clauses (length >= 15 chars)
            if len(cleaned) >= 15 and not cleaned.isnumeric():
                sentences.append(cleaned)
        return sentences

    def extract_relevant_sections(self, text: str) -> Dict[str, List[str]]:
        """Segments sentences into structural policy section categories."""
        sentences = self.segment_into_sentences(text)
        categorized = {
            "exclusions": [],
            "waiting_periods": [],
            "sub_limits": [],
            "co_pay": [],
            "general_text": []
        }

        for sentence in sentences:
            sent_lower = sentence.lower()
            matched = False
            for sec_key, pattern in self.section_patterns.items():
                if re.search(pattern, sent_lower):
                    categorized[sec_key].append(sentence)
                    matched = True
            if not matched:
                categorized["general_text"].append(sentence)

        return categorized


if __name__ == "__main__":
    # Test parser module
    parser = InsurancePDFParser()
    sample_text = """
    1. GENERAL EXCLUSIONS: The company shall not be liable for pre-existing ailments prior to 36 months of continuous coverage.
    2. SUB-LIMITS: Treatment of cataract is subject to a maximum sub-limit of $300 per eye or 10% of sum insured.
    3. CO-PAYMENT: A mandatory 20% co-payment applies to all claims filed by insured persons above 65 years of age.
    """
    sections = parser.extract_relevant_sections(sample_text)
    print("Parsed Sections Test:")
    for k, v in sections.items():
        print(f"  [{k.upper()}]: {len(v)} clauses")
