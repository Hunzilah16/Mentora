"""
Compile Hamna Cambridge AS Biology Topic 1 Examination Pack with Updated Syllabus Subtopics and 12 Embedded Diagrams
"""
import os
import fitz
from topic1_cell_structure_data import get_topic1_questions, get_topic1_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic1_Cell_Structure.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 1 — CELL STRUCTURE"
TOPIC_SUBTITLE = "Microscopy, Cell Ultrastructure, Organelle Specialisation & Viruses"

# Exact subtopics from official syllabus provided by user
SUBTOPICS = [
    "1.1 The microscope in cell studies: temporary mounts, biological drawings, magnification calculations (M = I/A), eyepiece graticule and stage micrometer calibration (mm, µm, nm), resolution vs magnification (light vs electron microscopy)",
    "1.2 Cells as the basic units of living organisms: eukaryotic organelles (cell surface membrane, nucleus/nucleolus, RER/SER, Golgi body, mitochondria with circular DNA, 80S/70S ribosomes, lysosomes, centrioles, cilia, microvilli, chloroplasts with circular DNA, cell wall, plasmodesmata, vacuole & tonoplast), plant vs animal cells, ATP usage, prokaryotic cell (bacterium, peptidoglycan wall, circular DNA, 70S ribosomes), viruses (non-cellular, nucleic acid core, protein capsid, phospholipid envelope)"
]

def main():
    print(f"Loading Topic 1 questions and FAQs...")
    qs = get_topic1_questions()
    faqs = get_topic1_faqs()
    print(f"Loaded {len(qs)} questions and {len(faqs)} FAQs. Total marks = {sum(sum(p.marks for p in q.parts) for q in qs)}")

    print(f"Building PDF: {PDF_PATH}...")
    build_topic_pdf(PDF_PATH, TOPIC_TITLE, TOPIC_SUBTITLE, SUBTOPICS, qs, faqs=faqs)

    doc = fitz.open(PDF_PATH)
    page_count = len(doc)
    print(f"Successfully generated {PDF_NAME} with {page_count} pages.")

    # Save preview of pages with newly added figures
    preview_pages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, page_count - 1]
    for p_idx in preview_pages:
        if p_idx < page_count:
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic1_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
