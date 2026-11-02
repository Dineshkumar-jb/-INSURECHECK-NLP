import json, os
from pypdf import PdfReader

paper_dir = "/home/nullframe/Desktop/NLP/REFERENCE PAPER"
pdf_files = sorted([f for f in os.listdir(paper_dir) if f.endswith(".pdf")], key=lambda x: int(x.split('.')[0]))

for f in pdf_files:
    path = os.path.join(paper_dir, f)
    reader = PdfReader(path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    
    print(f"\n=======================================================")
    print(f"PAPER FILE: {f}")
    print(f"=======================================================")
    print("--- FIRST 1000 CHARS ---")
    print(full_text[:1000])
    print("\n--- ABSTRACT / METHODOLOGY / RESULTS LOOKUP ---")
    # Search for Abstract, Conclusion, Results, Performance in text
    lower = full_text.lower()
    abs_idx = lower.find("abstract")
    if abs_idx != -1:
        print("\n[ABSTRACT]:\n", full_text[abs_idx:abs_idx+800])
    
    res_idx = lower.find("result")
    if res_idx != -1:
        print("\n[RESULTS]:\n", full_text[res_idx:res_idx+600])
        
    concl_idx = lower.find("conclusion")
    if concl_idx != -1:
        print("\n[CONCLUSION]:\n", full_text[concl_idx:concl_idx+600])

