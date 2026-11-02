import os
from pypdf import PdfReader

paper_dir = "/home/nullframe/Desktop/NLP/REFERENCE PAPER"
pdf_files = sorted([f for f in os.listdir(paper_dir) if f.endswith(".pdf")], key=lambda x: int(x.split('.')[0]))

for f in pdf_files:
    path = os.path.join(paper_dir, f)
    reader = PdfReader(path)
    text = ""
    for page in reader.pages[:2]: # first 2 pages
        text += page.extract_text() or ""
    
    print(f"=== {f} ===")
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines[:30]:
        print("  ", line)
    print("\n")
