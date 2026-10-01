"""
Run script to build Paper 1 (Multiple Choice) Topic 9: The Periodic Table: Chemical Periodicity.
"""
from mcq_topic9_data import TOPIC_9_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic9_Periodicity.pdf"
    topic_title = "Topic 9 — Periodic Table: Chemical Periodicity (Paper 1 Multiple Choice)"
    topic_subtitle = "9.1 Physical Periodicity: Radii, Melting Points, Conductivity, Ionisation Energies · 9.2 Chemical Periodicity: Reactions, Oxides & Chlorides · High-Frequency Repeats"
    
    subtopics_summary = [
        ("9.1 Physical Periodicity", "Trends across Period 3: atomic radius decrease, ionic radius discontinuity (Si4+ to P3-), melting point patterns (metals, giant covalent Si, S8 > P4 > Cl2 > Ar), electrical conductivity transitions, and first ionisation energy discontinuities (Al vs Mg, S vs P)."),
        ("9.2 Chemical Periodicity", "Reactions of Period 3 elements with oxygen, chlorine, and water (magnesium with steam vs liquid water), acid-base character of oxides (basic Na2O/MgO, amphoteric Al2O3, acidic SiO2/P4O10/SO2/SO3), and chloride hydrolysis (NaCl, MgCl2, AlCl3, SiCl4, PCl5)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Periodicity (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "9.1": "SUBTOPIC 9.1 — PHYSICAL PERIODICITY OF PERIOD 3 (Q1 – Q50)",
        "9.2": "SUBTOPIC 9.2 — CHEMICAL PERIODICITY OF PERIOD 3 (Q51 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_9_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
