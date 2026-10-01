"""
Run script to build Paper 1 (Multiple Choice) Topic 7: Equilibria.
"""
from mcq_topic7_data import TOPIC_7_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic7_Equilibria.pdf"
    topic_title = "Topic 7 — Equilibria (Paper 1 Multiple Choice)"
    topic_subtitle = "7.1 Chemical Equilibria: Le Chatelier's Principle, Kc & Kp · 7.2 Brønsted-Lowry Acids & Bases · High-Frequency Repeats"
    
    subtopics_summary = [
        ("7.1 Chemical Equilibria, Kc & Kp", "Dynamic equilibrium characteristics, Le Chatelier's principle (temperature, pressure, concentration, catalysts), industrial compromise conditions (Haber and Contact processes), expressions and units for Kc and Kp, and ICE table calculations."),
        ("7.2 Brønsted-Lowry Theory of Acids & Bases", "Proton donor and acceptor definitions, conjugate acid-base pairs, amphiprotic substances, strong vs weak acids (pH, conductivity, and reaction rate distinctions), and non-aqueous proton transfers."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Chemical Equilibria (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "7.1": "SUBTOPIC 7.1 — CHEMICAL EQUILIBRIA, KC & KP (Q1 – Q55)",
        "7.2": "SUBTOPIC 7.2 — BRØNSTED-LOWRY ACIDS & BASES (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_7_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
