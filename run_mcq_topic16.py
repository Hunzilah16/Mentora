"""
Run script to build Paper 1 (Multiple Choice) Topic 16: Hydroxy Compounds (Alcohols).
"""
from mcq_topic16_data import TOPIC_16_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic16_Hydroxy_Compounds.pdf"
    topic_title = "Topic 16 — Hydroxy Compounds: Alcohols (Paper 1 Multiple Choice)"
    topic_subtitle = "16.1 Classification, Physical Properties & Substitution Reactions · 16.2 Oxidation, Dehydration, Esterification & Tri-iodomethane Test · High-Frequency Repeats"
    
    subtopics_summary = [
        ("16.1 Classification, Physical Properties & Substitutions", "Classification into primary, secondary, and tertiary alcohols; physical properties (intermolecular hydrogen bonding, volatility, water solubility); industrial hydration of ethene vs carbohydrate fermentation; reaction with sodium metal (alkoxide salts and H2); halogenation with HX, PCl3, PCl5 (steamy HCl test), and SOCl2 (clean gaseous byproducts); Lucas test for classification."),
        ("16.2 Oxidation, Dehydration, Esters & Iodoform Test", "Oxidation with acidified potassium dichromate(VI) (distillation of aldehydes vs reflux of carboxylic acids from 1° alcohols, ketones from 2° alcohols, inertness of 3° alcohols); acid-catalyzed dehydration to alkenes (Zaitsev's rule and cis-trans stereoisomers); condensation with carboxylic acids forming esters; alkaline hydrolysis of esters (saponification); the tri-iodomethane (iodoform) reaction identifying CH3-CH(OH)- groupings."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Alcohol Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "16.1": "SUBTOPIC 16.1 — CLASSIFICATION, PHYSICAL PROPERTIES & SUBSTITUTION (Q1 – Q55)",
        "16.2": "SUBTOPIC 16.2 — OXIDATION, DEHYDRATION, ESTERS & IODOFORM (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_16_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
