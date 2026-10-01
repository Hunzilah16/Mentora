"""
Compile Hamna Cambridge AS Biology Topic 4 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic4_membranes_transport_data import get_topic4_questions, get_topic4_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic4_Membranes_Transport.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 4 - CELL MEMBRANES AND TRANSPORT"
TOPIC_SUBTITLE = "Fluid Mosaic Membranes, Transport Mechanisms, Osmosis & Cell Signalling"

# Exact subtopics from official syllabus provided by user
SUBTOPICS = [
    "4.1 Fluid mosaic membranes: fluid mosaic model of membrane structure with reference to hydrophobic and hydrophilic interactions; arrangement of cholesterol, glycolipids and glycoproteins; roles of phospholipids, cholesterol, glycolipids, proteins and glycoproteins (membrane stability, fluidity, permeability, transport, cell signalling, cell recognition); main stages in cell signalling (secretion of ligands, transport, complementary binding to membrane receptors, G-protein transduction, second messengers, amplification cascade)",
    "4.2 Movement into and out of cells: simple diffusion, facilitated diffusion (hydrophilic channel proteins vs conformational carrier proteins), osmosis, active transport (primary ATP pumps, Na+/K+-ATPase, secondary co-transport), endocytosis (phagocytosis, pinocytosis, receptor-mediated) and exocytosis (secretory vesicle fusion); investigations using plant tissue (beetroot permeability, potato osmometry), dialysis (Visking) tubing and agar diffusion blocks; surface area to volume ratio calculations and physical limits on cell size; water potential (Psi = Psi_s + Psi_p) effects on plant cells (turgor, incipient and full plasmolysis) and animal cells (haemolysis, crenation)"
]

def main():
    print(f"Loading Topic 4 questions and FAQs...")
    qs = get_topic4_questions()
    faqs = get_topic4_faqs()
    total_marks = sum(sum(p.marks for p in q.parts) for q in qs)
    print(f"Loaded {len(qs)} questions. Total marks = {total_marks}")
    print(f"Loaded {len(faqs)} high-frequency examiner FAQs.")

    print(f"Building PDF: {PDF_PATH}...")
    build_topic_pdf(PDF_PATH, TOPIC_TITLE, TOPIC_SUBTITLE, SUBTOPICS, qs, faqs=faqs)

    doc = fitz.open(PDF_PATH)
    page_count = len(doc)
    print(f"Successfully generated {PDF_NAME} with {page_count} pages.")

    # Save preview of key pages with figures and mark schemes
    preview_pages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, page_count - 2, page_count - 1]
    for p_idx in preview_pages:
        if p_idx < page_count:
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic4_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
