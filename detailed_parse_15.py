import os
from pypdf import PdfReader

paper_dir = "/home/nullframe/Desktop/NLP/REFERENCE PAPER"
pdf_files = sorted([f for f in os.listdir(paper_dir) if f.endswith(".pdf")], key=lambda x: int(x.split('.')[0]))

for f in pdf_files:
    path = os.path.join(paper_dir, f)
    reader = PdfReader(path)
    text = ""
    for p in reader.pages:
        text += p.extract_text() or ""
    
    print(f"==========================================")
    print(f"FILE: {f} (Pages: {len(reader.pages)})")
    print(f"==========================================")
    # Print first 1500 chars and last 500 chars
    print("--- HEAD ---")
    print(text[:1200])
    print("\n--- TAIL ---")
    print(text[-800:])
    print("\n")
