"""
Compile Hamna Cambridge AS Biology Topic 8 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic8_transport_mammals_data import get_topic8_questions, get_topic8_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic8_Transport_Mammals.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 8 — TRANSPORT IN MAMMALS"
TOPIC_SUBTITLE = "Circulatory System, Microcirculation, Gas Transport & Cardiac Physiology"

# Exact subtopics from official syllabus
SUBTOPICS = [
    "8.1 The circulatory system: closed double circulation in mammals (pulmonary and systemic circuits); major blood vessels (pulmonary artery, pulmonary vein, aorta, vena cava, coronary vessels); structural relationship to function of arteries, veins, and capillaries (tunica intima, media, externa, lumen dimensions, elastic and collagen fibres); cellular formed elements of mammalian blood (erythrocytes, monocytes, neutrophils, lymphocytes); water roles in transport (dipolar solvent action, thermal capacity); tissue fluid formation across capillary beds (Starling forces: hydrostatic pressure vs oncotic pressure) and lymphatic drainage",
    "8.2 Transport of oxygen and carbon dioxide: structure of haemoglobin (4 globin chains, 4 haem groups, Fe2+); cooperative oxygen binding and sigmoidal dissociation curve (T vs R allosteric states); physiological significance of curve at pulmonary and systemic capillary beds; the Bohr shift (effect of elevated pCO2 and acidic pH on oxygen unloading); transport of carbon dioxide (dissolved gas, carbaminohaemoglobin, hydrogencarbonate ions in plasma); intra-erythrocyte reactions (carbonic anhydrase, buffering by haemoglobinic acid HHb, the chloride shift via Band 3 exchanger); comparative dissociation curves of adult haemoglobin, fetal haemoglobin (higher affinity for placental transfer), and myoglobin",
    "8.3 The heart: external and internal gross anatomy of the mammalian heart (chambers, septum, cardiac valves: bicuspid/mitral, tricuspid, aortic and pulmonary semilunar); structural variations in myocardium wall thickness (atria vs ventricles; left ventricle 3x thicker than right ventricle); mechanical events and pressure-volume dynamics of the cardiac cycle (Wiggers diagram: atrial systole, ventricular systole, diastole, valve operations, heart sounds S1 and S2); myogenic initiation and electrical conduction system (Sinoatrial Node pacemaker, internodal pathways, 0.1s Atrioventricular Node delay, Bundle of His, Purkyne tissue)"
]

def main():
    print(f"Loading Topic 8 questions and FAQs...")
    qs = get_topic8_questions()
    faqs = get_topic8_faqs()
    total_marks = sum(sum(p.marks for p in q.parts) for q in qs)
    print(f"Loaded {len(qs)} questions. Total marks = {total_marks}")
    print(f"Loaded {len(faqs)} high-frequency examiner FAQs.")

    print(f"Building PDF: {PDF_PATH}...")
    build_topic_pdf(PDF_PATH, TOPIC_TITLE, TOPIC_SUBTITLE, SUBTOPICS, qs, faqs=faqs)

    doc = fitz.open(PDF_PATH)
    page_count = len(doc)
    print(f"Successfully generated {PDF_NAME} with {page_count} pages.")

    # Save preview of key pages with figures and mark schemes
    preview_pages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, page_count - 4, page_count - 3, page_count - 2, page_count - 1]
    for p_idx in preview_pages:
        if p_idx < page_count:
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic8_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
