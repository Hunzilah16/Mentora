"""
Run script to build Paper 1 (Multiple Choice) Topic 1: Atomic Structure.
"""
from mcq_topic1_data import TOPIC_1_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic1_Atomic_Structure.pdf"
    topic_title = "Topic 1 — Atomic Structure (Paper 1 Multiple Choice)"
    topic_subtitle = "1.1 Particles & Radii · 1.2 Isotopes · 1.3 Orbitals & Configurations · 1.4 Ionisation Energies · High-Frequency Repeats"
    
    subtopics_summary = [
        ("1.1 Particles & Atomic Radii", "Fundamental particles, charges, masses, deflection in electric fields, nuclear charge, shielding, and periodic trends in atomic and ionic radii."),
        ("1.2 Isotopes & Relative Masses", "Definition of isotopes, mass spectrometry principles, calculating relative atomic mass Ar, and polyatomic isotopic peak ratios (Cl2, Br2)."),
        ("1.3 Electrons & Orbitals", "Principal shells (n), subshells (s, p, d), orbital shapes, Aufbau principle, Hund's rule, Pauli exclusion, transition metal configurations (Cr, Cu), and cation formation."),
        ("1.4 Ionisation Energies", "First and successive ionisation energies, periodic trends across Period 3, Group 13/16 anomalies (Al vs Mg, S vs P), shell jumps, and evidence for electronic structure."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Atomic Structure (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "1.1": "SUBTOPIC 1.1 — PARTICLES IN THE ATOM & ATOMIC RADIUS (Q1 – Q25)",
        "1.2": "SUBTOPIC 1.2 — ISOTOPES & RELATIVE ATOMIC MASS (Q26 – Q50)",
        "1.3": "SUBTOPIC 1.3 — ELECTRONS, ENERGY LEVELS & ATOMIC ORBITALS (Q51 – Q75)",
        "1.4": "SUBTOPIC 1.4 — FIRST & SUCCESSIVE IONISATION ENERGIES (Q76 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_1_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
