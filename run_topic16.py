"""
Run script to build Topic 16: Hydroxy Compounds (Alcohols).
"""
from topic16_data import TOPIC_16_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic16_Alcohols.pdf"
    topic_title = "Topic 16 — Hydroxy Compounds (Alcohols)"
    topic_subtitle = "16.1 Alcohols · Physical Properties · Reactions with Na · Halogenation · Oxidation · Dehydration · Esterification · Iodoform Test"
    
    subtopics_summary = [
        ("16.1 Classification & Physical Properties", "Primary, secondary, and tertiary alcohols; boiling point trends, volatility, and solubility governed by extensive intermolecular hydrogen bonding; combustion as bioethanol."),
        ("16.1 Substitution & Oxidation Pathways", "Halogenation using PCl5, PCl3, SOCl2, NaBr/H2SO4, and red P/I2; reaction with sodium metal; differential oxidation with acidified K2Cr2O7 (distillation vs reflux)."),
        ("16.1 Dehydration, Esterification & Tri-iodomethane Test", "Elimination over hot Al2O3 or conc. H2SO4 to form alkenes (regioselectivity & stereoisomers); reversible acid-catalysed esterification; tri-iodomethane (iodoform) diagnostic test.")
    ]
    
    subtopic_map = {
        "16.1": "SUBTOPIC 16.1 — HYDROXY COMPOUNDS (ALCOHOLS)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_16_QUESTIONS
    )

if __name__ == "__main__":
    main()
