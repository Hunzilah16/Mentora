"""
Compile Hamna Cambridge AS Biology Topic 5 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic5_mitotic_cell_cycle_data import get_topic5_questions, get_topic5_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic5_Mitotic_Cell_Cycle.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 5 - THE MITOTIC CELL CYCLE"
TOPIC_SUBTITLE = "Chromosome Structure, Mitosis Stages, Telomeres, Stem Cells & Carcinogenesis"

# Exact subtopics from official syllabus
SUBTOPICS = [
    "5.1 Replication and division of nuclei and cells: structure of a chromosome including DNA, histone proteins (nucleosomes, chromatin packaging), sister chromatids, centromere, and telomeres; biological importance of mitosis (growth, replacement of worn-out cells, tissue repair, asexual reproduction); mitotic cell cycle comprising interphase (G1, S, G2 phases), nuclear division (mitosis), and cell division (cytokinesis); role of telomeres in preventing loss of vital genetic information and end-to-end chromosomal fusion; role of stem cells (totipotent, pluripotent, multipotent) in cell replacement and tissue repair; uncontrolled cell division, environmental mutagens, proto-oncogenes, tumour suppressor genes (p53), and multi-step tumour formation",
    "5.2 Chromosome behaviour in mitosis: dynamic behaviour of chromosomes, nuclear envelope, cell surface membrane, and spindle apparatus during prophase, metaphase, anaphase, and telophase; comparison of cytokinesis in animal cells (contractile cleavage furrow) and plant cells (phragmoplast and cell plate assembly); interpret light photomicrographs and electron micrographs to identify stages of mitosis; quantitative determination and clinical applications of the Mitotic Index (MI) and stage durations in meristematic tissues"
]

def main():
    print(f"Loading Topic 5 questions and FAQs...")
    qs = get_topic5_questions()
    faqs = get_topic5_faqs()
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
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic5_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
