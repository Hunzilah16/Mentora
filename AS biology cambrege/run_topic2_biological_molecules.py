"""
Compile Hamna Cambridge AS Biology Topic 2 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic2_biological_molecules_data import get_topic2_questions, get_topic2_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic2_Biological_Molecules.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 2 — BIOLOGICAL MOLECULES"
TOPIC_SUBTITLE = "Carbohydrates, Lipids, Proteins, Water & Biochemical Testing"

# Exact subtopics from official syllabus provided by user
SUBTOPICS = [
    "2.1 Testing for biological molecules: Benedict's test for reducing sugars (semi-quantitative estimation & colorimetry), non-reducing sugars (acid hydrolysis & neutralisation), iodine test for starch, emulsion test for lipids, biuret test for proteins",
    "2.2 Carbohydrates and lipids: ring forms of alpha-glucose and beta-glucose, monomers, polymers, macromolecules, condensation & hydrolysis of glycosidic bonds (maltose, sucrose), polysaccharides (starch amylose & amylopectin, glycogen, cellulose microfibrils & plant cell walls), triglycerides (glycerol, saturated & unsaturated fatty acids, ester bonds, energy storage & metabolic functions), phospholipids (hydrophilic polar head, hydrophobic fatty acid tails, membrane bilayer)",
    "2.3 Proteins: general structure of an amino acid, peptide bond condensation & hydrolysis, primary, secondary (alpha-helix, beta-pleated sheet), tertiary & quaternary structures, bonding types (hydrophobic, hydrogen, ionic, covalent disulfide bonds), globular vs fibrous proteins, haemoglobin (4 globin chains, 4 haem groups, Fe2+, oxygen transport) vs collagen (Gly-X-Y repeating sequence, triple helix, covalent cross-links, tensile strength)",
    "2.4 Water: hydrogen bonding between dipolar water molecules, solvent action (solvation shells), high specific heat capacity (thermal stability), high latent heat of vaporisation (evaporative cooling), cohesion and surface tension"
]

def main():
    print(f"Loading Topic 2 questions and FAQs...")
    qs = get_topic2_questions()
    faqs = get_topic2_faqs()
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
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic2_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
