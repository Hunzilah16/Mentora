"""
Compile Hamna Cambridge AS Biology Topic 9 Examination Pack with Official Syllabus Subtopics and 14 Embedded Diagrams
"""
import os
import fitz
from topic9_gas_exchange_data import get_topic9_questions, get_topic9_faqs
from build_as_biology_pdf import build_topic_pdf

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"
PDF_NAME = "Hamna_Bio_Topic9_Gas_Exchange.pdf"
PDF_PATH = os.path.join(OUTPUT_DIR, PDF_NAME)

TOPIC_TITLE = "TOPIC 9 — GAS EXCHANGE"
TOPIC_SUBTITLE = "Respiratory Anatomy, Alveolar Gas Exchange & Effects of Tobacco Smoking"

# Exact subtopics from official syllabus
SUBTOPICS = [
    "9.1 The gas exchange system: gross anatomy of the respiratory tract (larynx, trachea, bronchi, bronchioles, terminal and respiratory bronchioles, alveoli, capillary network); histological tissue distribution (hyaline cartilage C-rings in trachea, irregular plates in bronchi, absent in bronchioles; pseudostratified ciliated columnar epithelium, goblet cells, seromucous glands, smooth muscle, elastic fibres, squamous epithelium); recognition in light photomicrographs, electron micrographs, and plan diagrams; functional adaptations of ciliated cells and goblet cells (mucociliary escalator), cartilage (airway patency), smooth muscle (bronchomotor tone), elastic fibres (alveolar expansion and passive recoil), and squamous epithelium (ultrathin diffusion barrier)",
    "9.2 Gas exchange at the alveolar surface: quantitative application of Fick's first law of diffusion (Rate ∝ A × ΔP / x); physiological adaptations maximising surface area (~100 m² across 500–700 million alveoli, extensive branching capillary meshwork); maintaining steep partial pressure gradients (alveolar pO2 = 104 mmHg, capillary pO2 = 40 mmHg; alveolar pCO2 = 40 mmHg, capillary pCO2 = 45 mmHg) via continuous ventilation and continuous pulmonary capillary perfusion; ultrathin diffusion barrier (< 0.5 µm: Type I pneumocyte cytoplasm, shared fused basement membrane, endothelial cell cytoplasm); single-file RBC transit; pulmonary surfactant biophysics (Type II pneumocytes, DPPC, surface tension reduction, prevention of alveolar collapse / atelectasis and IRDS)",
    "9.3 Tobacco smoking impacts and pathology: triad of tobacco toxins (nicotine, carbon monoxide, tar); nicotine mode of action (sympathetic stimulation, adrenaline release, arteriolar vasoconstriction, hypertension, platelet activation, atheroma and thrombosis); carbon monoxide toxicity (irreversible binding to haemoglobin with 250x higher affinity forming carboxyhaemoglobin HbCO, leftward shift of dissociation curve, tissue hypoxia, fetal growth restriction); tar actions (ciliostasis, goblet cell hyperplasia, mucus hypersecretion); pathogenesis of respiratory diseases: chronic bronchitis (chronic inflammation, productive smoker's cough, bacterial superinfections), pulmonary emphysema (macrophage/neutrophil elastase secretion, oxidative inactivation of α1-antitrypsin, proteolytic destruction of alveolar septa, loss of elastic recoil, air trapping, bullae formation), COPD, and multi-step bronchogenic carcinoma (benzo[a]pyrene DNA adducts, TP53 and KRAS mutations, dysplasia, invasive carcinoma, metastasis)"
]

def main():
    print(f"Loading Topic 9 questions and FAQs...")
    qs = get_topic9_questions()
    faqs = get_topic9_faqs()
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
            preview_path = os.path.join(OUTPUT_DIR, f"preview_topic9_p{p_idx+1}.png")
            pix.save(preview_path)
            print(f"Saved preview: {preview_path}")

if __name__ == "__main__":
    main()
