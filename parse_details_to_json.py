import os, json
from pypdf import PdfReader

paper_dir = "/home/nullframe/Desktop/NLP/REFERENCE PAPER"
pdf_files = sorted([f for f in os.listdir(paper_dir) if f.endswith(".pdf")], key=lambda x: int(x.split('.')[0]))

paper_info = []

for f in pdf_files:
    path = os.path.join(paper_dir, f)
    reader = PdfReader(path)
    full_text = ""
    for p in reader.pages:
        full_text += p.extract_text() or ""
    
    # Store key segments
    first_2_pages = ""
    for p in reader.pages[:2]:
        first_2_pages += (p.extract_text() or "") + "\n"
        
    last_page = reader.pages[-1].extract_text() or "" if len(reader.pages) > 0 else ""

    paper_info.append({
        "file": f,
        "num_pages": len(reader.pages),
        "first_pages": first_2_pages[:3000],
        "last_page": last_page[-2000:]
    })

with open("/home/nullframe/Desktop/NLP/papers_parsed.json", "w") as out:
    json.dump(paper_info, out, indent=2)

print("Parsed metadata saved to papers_parsed.json")
