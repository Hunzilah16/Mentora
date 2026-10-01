"""
Compile Hamna Cambridge AS Biology Topic 10 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic10_infectious_diseases_data import get_topic10_questions, get_topic10_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic10_Infectious_Diseases.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 10 — INFECTIOUS DISEASES"
TOPIC_SUBTITLE = "Pathogens, Transmission Dynamics, Global Prevention & Antibiotic Mechanisms"

# Exact subtopics from official syllabus
SUBTOPICS = [
    "10.1 Infectious diseases and pathogens: distinction between infectious communicable diseases and non-infectious conditions; taxonomy, biological features, life cycles, and transmission modes of four major worldwide pathogens: cholera (Vibrio cholerae, water-borne/food-borne faecal-oral route, small intestine enterocyte infection, choleragen enterotoxin, cAMP-mediated CFTR opening, massive Cl- and water secretion, watery diarrhoea, dehydration, Oral Rehydration Therapy / ORT via SGLT-1 Na+-glucose cotransporters); malaria (Plasmodium falciparum, vivax, ovale, malariae protoctists, female Anopheles mosquito vector, exo-erythrocytic hepatic schizogony, intra-erythrocytic cycle: trophozoite, schizont, haemozoin pyrogen release, cyclical chills and tertian/quartan fever, sexual reproduction in mosquito gut, vector control, ITNs, IRS, ACTs, antigenic variation); tuberculosis (Mycobacterium tuberculosis, M. bovis, airborne droplet inhalation, waxy mycolic acid evasion of phagosome-lysosome fusion, tubercle granuloma formation, caseous necrosis, latency, reactivation, cavitation, DOTS, BCG vaccine); HIV/AIDS (human immunodeficiency retrovirus, gp120/CD4 binding, reverse transcriptase, integrase, provirus latency, gradual destruction of CD4+ T-helper cells, opportunistic infections, AIDS definition, transmission routes, prevention, ART/HAART)",
    "10.2 Antibiotics and resistance mechanisms: definition of antibiotics as antimicrobial metabolites with selective toxicity against prokaryotes; mode of action of penicillin (β-lactam structural mimic of D-Ala-D-Ala, irreversible inhibition of peptidoglycan transpeptidase / glycoprotein peptidase, ongoing autolysin activity, weakening of cell wall lattice, osmotic entry of water, bacterial lysis; specificity for growing cells); why antibiotics do not affect viruses (viruses are acellular entities lacking peptidoglycan walls, cell surface membranes, 70S ribosomes, and independent metabolic pathways, replicating via host machinery); evolutionary mechanisms of bacterial antibiotic resistance: random spontaneous pre-existing mutations conferring resistance, antibiotic acting as environmental selective pressure, vertical clonal inheritance via binary fission vs horizontal gene transfer (conjugation via sex pilus, rolling-circle R-plasmid transfer, transformation, transduction); four molecular resistance mechanisms (β-lactamase enzymatic hydrolysis, mutated transpeptidase target sites, active multidrug efflux pumps, decreased outer membrane porin permeability); emergence of superbugs (MRSA, MDR-TB, XDR-TB); clinical strategies for antibiotic stewardship and control"
]

def main():
    print(f"Loading Topic 10 questions and FAQs...")
    qs = get_topic10_questions()
    faqs = get_topic10_faqs()
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
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic10_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
