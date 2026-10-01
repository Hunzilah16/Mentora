"""
Run script to build Paper 1 (Multiple Choice) Topic 5: Chemical Energetics.
"""
from mcq_topic5_data import TOPIC_5_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic5_Chemical_Energetics.pdf"
    topic_title = "Topic 5 — Chemical Energetics (Paper 1 Multiple Choice)"
    topic_subtitle = "5.1 Enthalpy Change Delta H: Definitions, Calorimetry, Bond Energies · 5.2 Hess's Law & Enthalpy Cycles · High-Frequency Repeats"
    
    subtopics_summary = [
        ("5.1 Enthalpy Change, Delta H", "Standard enthalpy changes (formation, combustion, neutralisation, atomisation), thermochemical energy profiles, activation energy, experimental calorimetry (q = mc Delta T), and average bond enthalpies."),
        ("5.2 Hess's Law & Cycles", "Hess's Law principle, thermochemical cycles utilizing standard enthalpies of formation and combustion, bond enthalpy reaction calculations, and discrepancies between gaseous bond models and standard state experiments."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Chemical Energetics (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "5.1": "SUBTOPIC 5.1 — ENTHALPY CHANGE, DELTA H & CALORIMETRY (Q1 – Q55)",
        "5.2": "SUBTOPIC 5.2 — HESS'S LAW & THERMOCHEMICAL CYCLES (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_5_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
