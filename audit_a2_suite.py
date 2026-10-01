"""
Comprehensive Audit Script for Cambridge A Level Chemistry (9701) A2 Suite
Root: Urwah_Chem_Papers_A2/
Candidate: Urwah | Mentora Academy
"""
import os
import glob
import pypdf

def audit_a2():
    root = r"Urwah_Chem_Papers_A2"
    all_pdfs = glob.glob(os.path.join(root, "**", "*.pdf"), recursive=True)
    
    print("=" * 80)
    print("CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701) — A2 SUITE AUDIT")
    print("CANDIDATE: URWAH | MENTORA ACADEMY")
    print(f"DIRECTORY: {root}/")
    print("=" * 80)
    
    divisions = ["Physical Chemistry", "Inorganic Chemistry", "Organic Chemistry", "Analysis"]
    components = ["Paper 4 (Theory)", "MCQs", "Paper 5 (Planning & Analysis)"]
    
    total_pages = 0
    total_files = len(all_pdfs)
    
    div_stats = {d: {"count": 0, "pages": 0, "p4": 0, "mcq": 0, "p5": 0} for d in divisions}
    
    for pdf_path in sorted(all_pdfs):
        reader = pypdf.PdfReader(pdf_path)
        pages = len(reader.pages)
        size_kb = os.path.getsize(pdf_path) / 1024
        total_pages += pages
        
        # Determine division
        found_div = "Other"
        for d in divisions:
            if d in pdf_path:
                found_div = d
                break
        
        if found_div in div_stats:
            div_stats[found_div]["count"] += 1
            div_stats[found_div]["pages"] += pages
            if "Paper 4" in pdf_path:
                div_stats[found_div]["p4"] += 1
            elif "MCQ" in pdf_path:
                div_stats[found_div]["mcq"] += 1
            elif "Paper 5" in pdf_path:
                div_stats[found_div]["p5"] += 1
                
        rel_path = os.path.relpath(pdf_path, root)
        print(f"  • {rel_path:<70} | {pages:>3} pages | {size_kb:>6.1f} KB")

    print("\n" + "=" * 80)
    print("SUMMARY BY DIVISION:")
    print("=" * 80)
    for d, st in div_stats.items():
        print(f"  {d:<22}: {st['count']:>2} PDFs ({st['pages']:>4} pages) -> {st['p4']} Theory (P4), {st['mcq']} MCQs, {st['p5']} Practical (P5)")
        
    print("-" * 80)
    print(f"GRAND TOTAL: {total_files} PDFs across {total_pages} Pages")
    print("=" * 80)

if __name__ == "__main__":
    audit_a2()
