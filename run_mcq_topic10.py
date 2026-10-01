"""
Run script to build Paper 1 (Multiple Choice) Topic 10: Group 2.
"""
from mcq_topic10_data import TOPIC_10_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic10_Group_2.pdf"
    topic_title = "Topic 10 — Group 2: The Alkaline Earth Metals (Paper 1 Multiple Choice)"
    topic_subtitle = "10.1 Physical Trends, Reactivity with Water & Steam, Solubility of Hydroxides & Sulfates, Thermal Stability of Carbonates & Nitrates, Applications · High-Frequency Repeats"
    
    subtopics_summary = [
        ("10.1 Group 2 Trends & Reactions", "Atomic radii and ionisation energy trends, reactions with oxygen and water (magnesium with steam vs liquid water), hydroxide solubility increase vs sulfate solubility decrease (thermodynamic lattice vs hydration enthalpies), thermal stability of carbonates and nitrates (polarising power of cations), Bunsen flame test colors, and industrial/medical applications (liming, antacids, barium meal)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Group 2 Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "10.1": "SUBTOPIC 10.1 — SIMILARITIES & TRENDS DOWN GROUP 2 (Q1 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_10_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
