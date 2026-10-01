"""
Run script to build Topic 13: Introduction to AS Organic Chemistry.
"""
from topic13_data import TOPIC_13_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic13_Intro_Organic.pdf"
    topic_title = "Topic 13 — An Introduction to AS Level Organic Chemistry"
    topic_subtitle = "13.1 Formulae & Nomenclature · 13.2 Reaction Types & Fission · 13.3 Hybridisation & Shapes · 13.4 Isomerism"
    
    subtopics_summary = [
        ("13.1 Formulae & Nomenclature", "Empirical, molecular, structural, displayed, and skeletal formulae; functional groups and systematic IUPAC nomenclature."),
        ("13.2 Organic Reactions & Mechanisms", "Homolytic/heterolytic fission, free radicals, carbocation stability (positive inductive effect), electrophiles, and nucleophiles."),
        ("13.3 Molecular Shapes & Hybridisation", "sp³, sp², and sp hybridisation, bond angles (109.5°, 120°, 180°), sigma bonds (coaxial overlap), and pi bonds (sideways p overlap)."),
        ("13.4 Structural & Stereoisomerism", "Structural isomerism (chain, positional, functional group) and stereoisomerism (geometric E/Z with CIP priority rules and chiral optical isomerism).")
    ]
    
    subtopic_map = {
        "13.1": "SUBTOPIC 13.1 — FORMULAE, FUNCTIONAL GROUPS & IUPAC NOMENCLATURE",
        "13.2": "SUBTOPIC 13.2 — CHARACTERISTIC ORGANIC REACTIONS & MECHANISMS",
        "13.3": "SUBTOPIC 13.3 — SHAPES OF ORGANIC MOLECULES, HYBRIDISATION & BONDING",
        "13.4": "SUBTOPIC 13.4 — STRUCTURAL ISOMERISM & STEREOISOMERISM (E/Z & OPTICAL)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_13_QUESTIONS
    )

if __name__ == "__main__":
    main()
