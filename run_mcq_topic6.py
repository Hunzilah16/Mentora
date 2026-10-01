"""
Run script to build Paper 1 (Multiple Choice) Topic 6: Electrochemistry.
"""
from mcq_topic6_data import TOPIC_6_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic6_Electrochemistry.pdf"
    topic_title = "Topic 6 — Electrochemistry (Paper 1 Multiple Choice)"
    topic_subtitle = "6.1 Redox Processes: Oxidation Numbers, Disproportionation, Half-Equations · 6.2 Electrolysis & Quantitative Laws · High-Frequency Repeats"
    
    subtopics_summary = [
        ("6.1 Redox Processes", "Rules for assigning oxidation numbers, oxidation states in complex ions and organic compounds, identifying oxidizing and reducing agents, balancing redox half-equations in acidic media, and disproportionation reactions (chlorine in cold vs hot alkali)."),
        ("6.2 Electrolysis & Quantitative Laws", "Electrolysis of molten vs aqueous electrolytes (brine, dilute sulfuric acid, aqueous CuSO4), selective discharge at electrodes, quantitative Faraday calculations (Q = It, moles of electrons, mass and gas volume discharged), and copper refining."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Electrochemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "6.1": "SUBTOPIC 6.1 — REDOX PROCESSES & OXIDATION NUMBERS (Q1 – Q55)",
        "6.2": "SUBTOPIC 6.2 — ELECTROLYSIS & FARADAY'S LAWS (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_6_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
