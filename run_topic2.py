"""
Run script to build Topic 2: Atoms, Molecules and Stoichiometry.
"""
from topic2_data import TOPIC_2_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic2_Stoichiometry.pdf"
    topic_title = "Topic 2 — Atoms, Molecules & Stoichiometry"
    topic_subtitle = "2.1 Relative Masses · 2.2 The Mole & L · 2.3 Empirical/Molecular Formulas · 2.4 Reacting Volumes"
    
    subtopics_summary = [
        ("2.1 Relative masses of atoms and molecules", "Ar and Mr definitions, unified atomic mass unit, carbon-12 standard, isotopic mass"),
        ("2.2 The mole and the Avogadro constant", "n = m/M, N = n × L calculations, moles of atoms, ions, subatomic particles, and Faraday constant"),
        ("2.3 Formulas (empirical, molecular, structural)", "Combustion analysis (CxHyOz), percentage composition by mass, hydrated salts (CuSO4·xH2O)"),
        ("2.4 Reacting masses and volumes", "Acid-base & back titrations, gas molar volume, ideal gas pV = nRT, % yield and % atom economy")
    ]
    
    subtopic_map = {
        "2.1": "SUBTOPIC 2.1 — RELATIVE MASSES OF ATOMS & MOLECULES",
        "2.2": "SUBTOPIC 2.2 — THE MOLE & THE AVOGADRO CONSTANT",
        "2.3": "SUBTOPIC 2.3 — EMPIRICAL & MOLECULAR FORMULAS",
        "2.4": "SUBTOPIC 2.4 — REACTING MASSES & GAS VOLUMES"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_2_QUESTIONS
    )

if __name__ == "__main__":
    main()
