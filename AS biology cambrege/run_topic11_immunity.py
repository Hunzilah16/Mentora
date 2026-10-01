"""
Compile Hamna Cambridge AS Biology Topic 11 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic11_immunity_data import get_topic11_questions, get_topic11_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic11_Immunity.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 11 — IMMUNITY"
TOPIC_SUBTITLE = "Cellular Defences, Humoral & Cell-Mediated Immunity, Antibodies, Vaccines & Monoclonals"

# Exact subtopics from official syllabus
SUBTOPICS = [
    "11.1 The immune system and cellular defences: distinction between self and non-self antigens; non-specific innate barriers (epithelial, chemical, cellular); origin of leukocytes in bone marrow (pluripotent hematopoietic stem cell -> myeloid and lymphoid progenitors); phagocytes: structure and functional comparison of short-lived neutrophils vs long-lived macrophages (APCs); sequential cytological stages of phagocytosis: chemotaxis, opsonisation (Fc receptors, C3b), pseudopodia engulfment, phagosome formation, lysosome fusion (phagolysosome), hydrolytic degradation (lysozyme, proteases, reactive oxygen species), exocytosis and peptide epitope loading onto MHC Class II molecules; adaptive lymphocytes: B-lymphocyte maturation in bone marrow vs T-lymphocyte maturation in thymus; clonal selection and clonal expansion (Burnet's theory); differentiation of selected B-cells into short-lived antibody-secreting plasma cells (ultrastructural adaptations: extensive RER, prominent Golgi, clock-face eccentric nucleus) and long-lived circulating memory B-cells; functional dichotomy of T-lymphocytes: CD4+ T-helper cells (TCR/CD4 binding to MHC II on APCs, interleukin cytokine secretion coordinating B-cell expansion and macrophage activation) vs CD8+ Cytotoxic T-killer cells (TCR/CD8 recognition of foreign viral peptides on MHC Class I, release of perforin transmembrane pores and granzyme apoptotic caspases)",
    "11.2 Antibodies, vaccination, and applied immunology: quaternary globular glycoprotein structure of IgG antibodies (two identical heavy chains, two identical light chains joined by interchain disulfide bonds -S-S-, flexible proline-rich hinge region, N-terminal hypervariable VH/VL domains forming two identical antigen-binding Fab sites, conserved C-terminal Fc stem determining effector activity); four primary antibody effector mechanisms: neutralisation of exotoxins and viral ligands, bivalent agglutination of bacterial lattices, opsonisation anchoring to phagocyte Fcγ receptors, and classical complement cascade activation leading to Membrane Attack Complex (MAC) osmotic lysis; quantitative kinetics of primary vs secondary immune responses (lag phase, rate of synthesis, peak titre, IgM vs IgG isotypes, persistence of immunological memory); hybridoma technology (Köhler and Milstein): fusion of immunized murine spleen B-cells with HGPRT-deficient immortal myeloma cells using PEG, selection on HAT medium, limiting dilution single-cell cloning, and bioreactor culture to generate pure monospecific monoclonal antibodies (mAbs); diagnostic applications (lateral flow pregnancy dipsticks detecting hCG, ELISA assays, flow cytometry) and targeted therapeutic applications (Trastuzumab / Herceptin blocking HER2 receptor dimerisation and inducing ADCC in breast carcinoma, Rituximab, antivenoms); systematic classification of acquired immunity (Natural vs Artificial, Active vs Passive matrix); vaccinology: antigenic preparations (live-attenuated, inactivated/killed, toxoids, recombinant subunits), role of adjuvants and booster doses; epidemiological dynamics of herd immunity (Herd Immunity Threshold HIT = 1 - 1/R0, breaking transmission chains, cocoon protection); eradication criteria (smallpox success vs measles/polio challenges); autoimmune breakdown of self-tolerance in Myasthenia Gravis (anti-AChR autoantibodies, receptor blockade, complement-mediated destruction of motor end-plate junctional folds, progressive muscle weakness)"
]

def main():
    print(f"Loading Topic 11 questions and FAQs...")
    qs = get_topic11_questions()
    faqs = get_topic11_faqs()
    total_marks = sum(sum(p.marks for p in q.parts) for q in qs)
    print(f"Loaded {len(qs)} questions. Total marks = {total_marks}")
    print(f"Loaded {len(faqs)} high-frequency examiner FAQs.")

    print(f"Building PDF: {PDF_PATH}...")
    build_topic_pdf(PDF_PATH, TOPIC_TITLE, TOPIC_SUBTITLE, SUBTOPICS, qs, faqs=faqs)

    doc = fitz.open(PDF_PATH)
    page_count = len(doc)
    print(f"Successfully generated {PDF_NAME} with {page_count} pages.")

    # Save preview of key pages with figures and mark schemes
    preview_pages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, page_count - 5, page_count - 4, page_count - 3, page_count - 2, page_count - 1]
    for p_idx in preview_pages:
        if p_idx < page_count:
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic11_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
