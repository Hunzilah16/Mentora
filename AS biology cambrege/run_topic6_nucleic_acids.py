"""
Compile Hamna Cambridge AS Biology Topic 6 Examination Pack with Official Syllabus Subtopics,
14 Embedded High-Legibility Diagrams, and Section D: 10 High-Frequency Examiner FAQs
"""
import os
import fitz
from topic6_nucleic_acids_data import get_topic6_questions, get_topic6_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic6_Nucleic_Acids.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 6 — NUCLEIC ACIDS AND PROTEIN SYNTHESIS"
TOPIC_SUBTITLE = "DNA Duplex Architecture, Semiconservative Replication, Transcription, Translation & Gene Mutations"

# Exact subtopics from official Cambridge 9700 syllabus
SUBTOPICS = [
    "6.1 Structure of nucleic acids and replication of DNA: structure of mononucleotides including ATP as a phosphorylated nucleotide; purines (adenine, guanine) and pyrimidines (cytosine, thymine, uracil); double-helical architecture of DNA, antiparallel strand orientation (5' to 3' vs 3' to 5'), 3'-5' covalent phosphodiester bonds, and complementary base pairing (A-T with 2 hydrogen bonds, G-C with 3 hydrogen bonds); semi-conservative replication mechanism (helicase, single-stranded binding proteins, DNA polymerase, leading and lagging strand synthesis, Okazaki fragments, and DNA ligase); experimental validation by Meselson and Stahl using 15N and 14N density gradient centrifugation; comparative biochemistry and structures of RNA species (mRNA, tRNA, rRNA).",
    "6.2 Protein synthesis: the gene as a sequence of nucleotides encoding a polypeptide; triplet nature, degeneracy, non-overlapping, and universality of the genetic code; transcription mechanism (RNA polymerase binding promoter, unwinding duplex, reading template strand 3'->5', condensing rNTPs 5'->3', displacement of pre-mRNA); translation mechanism (ribosomal A, P, and E sites, peptidyl transferase ribozyme activity, initiator Met-tRNA, stop codons, and release factors); polyribosomes (polysomes); post-transcriptional processing in eukaryotes (intron excision, exon splicing); gene mutations (silent, missense, and nonsense base substitutions vs insertion/deletion frameshifts); molecular genetic basis and clinical pathology of sickle cell anaemia (HbA vs HbS, Glu6Val, deoxyhaemoglobin polymerisation)."
]

def main():
    print(f"Loading Topic 6 questions and FAQs...")
    qs = get_topic6_questions()
    faqs = get_topic6_faqs()
    total_marks = sum(sum(p.marks for p in q.parts) for q in qs)
    print(f"Loaded {len(qs)} questions ({total_marks} marks) and {len(faqs)} examiner FAQs.")

    print(f"Building PDF: {PDF_PATH}...")
    build_topic_pdf(PDF_PATH, TOPIC_TITLE, TOPIC_SUBTITLE, SUBTOPICS, qs, faqs=faqs)

    doc = fitz.open(PDF_PATH)
    page_count = len(doc)
    print(f"Successfully generated {PDF_NAME} with {page_count} pages.")

    # Render previews of key pages: cover, diagram pages, FAQ pages, and mark scheme
    # Let's save previews across key regions
    preview_pages = [0, 1, 3, 5, 7, 9, 11, 13, 15, page_count - 5, page_count - 4, page_count - 3, page_count - 2, page_count - 1]
    for p_idx in preview_pages:
        if 0 <= p_idx < page_count:
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic6_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
