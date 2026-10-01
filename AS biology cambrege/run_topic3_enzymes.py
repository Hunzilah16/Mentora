"""
Compile Hamna Cambridge AS Biology Topic 3 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic3_enzymes_data import get_topic3_questions, get_topic3_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic3_Enzymes.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 3 - ENZYMES"
TOPIC_SUBTITLE = "Mode of Action, Enzyme Kinetics, Vmax, Km, Inhibition & Immobilisation"

# Exact subtopics from official syllabus provided by user
SUBTOPICS = [
    "3.1 Mode of action of enzymes: globular proteins, intracellular vs extracellular enzymes, active site, enzyme-substrate (ES) and enzyme-product (EP) complexes, lowering of activation energy (Ea), lock-and-key vs induced-fit hypotheses, enzyme specificity, monitoring reaction progress (measuring product formation with catalase, substrate disappearance with amylase, colorimetric assays)",
    "3.2 Factors that affect enzyme action: effects of temperature (kinetic energy, thermal denaturation), pH (buffers, charge alteration of R-groups), enzyme concentration (limiting factors), substrate concentration (saturation, Vmax), Michaelis-Menten constant (Km, substrate affinity), reversible inhibitors (competitive vs non-competitive, allosteric regulation), immobilised enzymes in alginate (thermal stability, reusability, continuous processing)"
]

def main():
    print(f"Loading Topic 3 questions and FAQs...")
    qs = get_topic3_questions()
    faqs = get_topic3_faqs()
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
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic3_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
