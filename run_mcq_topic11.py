"""
Run script to build Paper 1 (Multiple Choice) Topic 11: Group 17.
"""
from mcq_topic11_data import TOPIC_11_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic11_Group_17.pdf"
    topic_title = "Topic 11 — Group 17: The Halogens (Paper 1 Multiple Choice)"
    topic_subtitle = "11.1 Physical Properties: Colors, Volatility, Bond Energies · 11.2 Chemical Properties: Redox, Displacement, H2SO4 Reactions, Silver Halides · High-Frequency Repeats"
    
    subtopics_summary = [
        ("11.1 Physical Properties of Group 17", "Colors and physical states at 298 K (Cl2, Br2, I2), volatility and boiling point trends (London dispersion forces), electronegativity decrease, and the F-F bond energy anomaly (inter-lone pair repulsion)."),
        ("11.2 Chemical Properties of Halogens & Hydrides", "Oxidizing power decrease down Group 17, aqueous displacement reactions, halide reducing power trend (F- < Cl- < Br- < I-), solid sodium halides with concentrated H2SO4 (acid-base vs redox products), silver halide precipitation and NH3 solubility tests, disproportionation reactions (cold vs hot alkali), and hydrogen halide thermal stability."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Group 17 Halogen Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "11.1": "SUBTOPIC 11.1 — PHYSICAL PROPERTIES OF GROUP 17 (Q1 – Q40)",
        "11.2": "SUBTOPIC 11.2 — CHEMICAL PROPERTIES OF HALOGENS & HYDRIDES (Q41 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_11_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
