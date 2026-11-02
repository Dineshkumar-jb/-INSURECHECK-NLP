import os
from pypdf import PdfReader

paper_dir = "/home/nullframe/Desktop/NLP/REFERENCE PAPER"
pdf_files = sorted([f for f in os.listdir(paper_dir) if f.endswith(".pdf")], key=lambda x: int(x.split('.')[0]))

print(f"Found {len(pdf_files)} PDF files.")

for f in pdf_files:
    path = os.path.join(paper_dir, f)
    print(f"\n==========================================")
    print(f"FILE: {f}")
    print(f"==========================================")
    try:
        reader = PdfReader(path)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        text = ""
        # Read first 2 pages and last page for references/future work
        for page_num in [0, 1, min(2, num_pages-1), num_pages-1]:
            if page_num < num_pages:
                text += f"\n--- Page {page_num+1} ---\n" + (reader.pages[page_num].extract_text() or "")
        print(text[:2000]) # Print first 2000 chars
    except Exception as e:
        print(f"Error reading {f}: {e}")
