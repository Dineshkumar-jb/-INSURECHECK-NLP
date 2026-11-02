"""
Run InsureCheck-NLP Benchmark Evaluation & Generate Empirical Results
"""

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from benchmark_evaluator import InsureCheckExperimentRunner

def main():
    print("Executing InsureCheck-NLP Review II Benchmark Evaluation...")
    runner = InsureCheckExperimentRunner()
    results = runner.run_experiments()
    
    print("\n===========================================================")
    print("INSURECHECK-NLP REVIEW II 60% IMPLEMENTATION EXPERIMENTAL RESULTS")
    print("===========================================================")
    print(f"Status:                    {results['experiment_status']}")
    print(f"Total Test Samples:        {results['total_samples_evaluated']}")
    print(f"Macro F1-Score:            {results['macro_f1']*100:.2f}%")
    print(f"Macro Precision:           {results['macro_precision']*100:.2f}%")
    print(f"Macro Recall:              {results['macro_recall']*100:.2f}%")
    print(f"Inference Latency:         {results['avg_inference_latency_ms']:.2f} ms / clause")
    print(f"Sample Risk Score Test:    {results['sample_risk_score_test']['computed_score']} / 100 [{results['sample_risk_score_test']['risk_level']}]")
    print("===========================================================")
    print("Per-Class Breakdown:")
    for cat, m in results["per_class_metrics"].items():
        print(f"  [{cat}]: Precision={m['precision']*100:.1f}%, Recall={m['recall']*100:.1f}%, F1={m['f1_score']*100:.1f}%")
    print("===========================================================\n")

if __name__ == "__main__":
    main()
