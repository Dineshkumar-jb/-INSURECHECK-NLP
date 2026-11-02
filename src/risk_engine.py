"""
InsureCheck-NLP: Claim Risk Scoring Engine & Plain-English Simplifier
Calculates the Policy Transparency & Claim Risk Score (0 - 100%) and generates
plain-English explanations for identified non-coverage exclusions.
"""

from typing import List, Dict, Any, Tuple


class InsureCheckRiskEngine:
    def __init__(self):
        # Severity weights per exclusion category
        self.severity_weights = {
            "Waiting Periods": 30,
            "Sub-Limits & Caps": 25,
            "Co-Payment Mandates": 25,
            "Non-Payable Items & Consumables": 15,
            "Standard Coverage": 0
        }
        
        # Plain-English translation patterns
        self.translation_templates = {
            "Waiting Periods": "⚠️ PRE-EXISTING & SPECIFIC DISEASE WAIT: Any illness or condition mentioned here will NOT be covered for the initial specified months. You must pay out-of-pocket during this period.",
            "Sub-Limits & Caps": "⚠️ PAYOUT CAP LIMIT: The insurance company will only pay up to the specified dollar/percentage limit. Any excess medical bill amount must be paid out-of-pocket by the policyholder.",
            "Co-Payment Mandates": "⚠️ MANDATORY CO-PAYMENT: You must pay the specified percentage share of every hospital bill out of your own pocket, regardless of your total sum insured.",
            "Non-Payable Items & Consumables": "⚠️ EXCLUDED CONSUMABLES: Listed administrative, diagnostic, and consumable items (like gloves, masks, PPE) are not reimbursable and will be deducted from your final claim payout."
        }

    def compute_claim_risk_score(self, classified_clauses: List[Dict[str, Any]]) -> Tuple[float, str, List[Dict[str, Any]]]:
        """
        Computes Claim Risk Score (0-100) using equation: R = min(100, sum(w_i * C_i))
        Returns (Score, Risk Level, Enriched Exclusion List)
        """
        total_risk = 0.0
        enriched_exclusions = []

        for item in classified_clauses:
            cat = item["category"]
            if cat in self.severity_weights and cat != "Standard Coverage":
                weight = self.severity_weights[cat]
                total_risk += weight
                
                # Generate plain English summary
                plain_summary = self.translate_to_plain_english(item["clause_text"], cat)
                
                enriched_exclusions.append({
                    "clause_text": item["clause_text"],
                    "category": cat,
                    "confidence": item["confidence"],
                    "severity_weight": weight,
                    "plain_english_summary": plain_summary,
                    "risk_badge": "🔴 High Risk" if weight >= 25 else "🟡 Medium Risk"
                })

        # Cap score at 100
        final_score = min(100.0, total_risk)
        
        # Risk Level Categorization
        if final_score <= 30:
            risk_level = "🟢 LOW CLAIM RISK (Transparent Policy)"
        elif final_score <= 60:
            risk_level = "🟡 MODERATE CLAIM RISK (Moderate Exclusions)"
        else:
            risk_level = "🔴 HIGH CLAIM RISK (Severe Fine Print Traps)"

        return final_score, risk_level, enriched_exclusions

    def translate_to_plain_english(self, clause_text: str, category: str) -> str:
        """Translates dense legal policy text into plain-English explanation."""
        template = self.translation_templates.get(category, "⚠️ Policy exclusion applies to this term.")
        
        # Customized text simplifications
        text_lower = clause_text.lower()
        if "cataract" in text_lower:
            return "⚠️ CATARACT SURGERY CAP: Insurance pays maximum capped limit for cataract treatment. Any extra bill must be paid out-of-pocket."
        elif "room rent" in text_lower:
            return "⚠️ ROOM RENT CAP: Room charges are capped per day. If you choose a higher room, all associated hospital charges (doctors, ICU) will also be proportionately deducted."
        elif "pre-existing" in text_lower:
            return "⚠️ PRE-EXISTING DISEASE WAIT: Any illness you had prior to buying this policy will not be covered until the waiting period completes."
        elif "co-pay" in text_lower or "co-payment" in text_lower:
            return "⚠️ MANDATORY PATIENT CO-PAY: You are required to pay a fixed percentage of every hospital bill out-of-pocket."

        return template


if __name__ == "__main__":
    engine = InsureCheckRiskEngine()
    test_clauses = [
        {"clause_text": "Room rent is capped at 1% per day.", "category": "Sub-Limits & Caps", "confidence": 0.95},
        {"clause_text": "36 months waiting period for pre-existing disease.", "category": "Waiting Periods", "confidence": 0.98},
        {"clause_text": "20% co-payment for senior citizens.", "category": "Co-Payment Mandates", "confidence": 0.92}
    ]
    score, level, ex_list = engine.compute_claim_risk_score(test_clauses)
    print(f"Risk Score: {score}/100 [{level}]")
    for ex in ex_list:
        print(f" - {ex['risk_badge']}: {ex['plain_english_summary']}")
