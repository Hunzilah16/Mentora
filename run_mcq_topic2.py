"""
Run script to build Paper 1 (Multiple Choice) Topic 2: Atoms, Molecules & Stoichiometry.
"""
from mcq_topic2_data import TOPIC_2_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic2_Stoichiometry.pdf"
    topic_title = "Topic 2 — Atoms, Molecules & Stoichiometry (Paper 1 Multiple Choice)"
    topic_subtitle = "2.1 Relative Masses · 2.2 Mole Concept · 2.3 Formulas & Hydrates · 2.4 Titrations & Reacting Masses · High-Frequency Repeats"
    
    subtopics_summary = [
        ("2.1 Relative Masses of Atoms & Molecules", "Carbon-12 standard, relative isotopic mass, relative atomic mass Ar, relative molecular mass Mr, relative formula mass of giant lattices and hydrated salts."),
        ("2.2 The Mole & Avogadro Constant", "The mole as amount of substance, Avogadro constant L = 6.02 x 10^23 mol^-1, mass of single atoms, molar volume of gases at r.t.p. (24.0 dm^3 mol^-1), calculating numbers of atoms, molecules, ions, and electrons."),
        ("2.3 Formulas (Empirical, Molecular, Hydrated)", "Determining empirical and molecular formulas from percentage compositions, combustion analysis masses (CO2, H2O), gravimetric water of crystallization loss, and gaseous combustion eudiometry."),
        ("2.4 Reacting Masses, Titrations & Atom Economy", "Stoichiometric calculations, limiting reagents, theoretical vs actual yields, percentage atom economy (addition vs substitution), acid-base & redox titrations, concordant titres, and back titrations."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Stoichiometry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "2.1": "SUBTOPIC 2.1 — RELATIVE MASSES OF ATOMS AND MOLECULES (Q1 – Q25)",
        "2.2": "SUBTOPIC 2.2 — THE MOLE AND THE AVOGADRO CONSTANT (Q26 – Q50)",
        "2.3": "SUBTOPIC 2.3 — FORMULAS: EMPIRICAL, MOLECULAR & HYDRATED (Q51 – Q75)",
        "2.4": "SUBTOPIC 2.4 — REACTING MASSES, VOLUMES, TITRATIONS & ATOM ECONOMY (Q76 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_2_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
