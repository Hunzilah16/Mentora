"""
Run script to build Topic 7: Equilibria.
"""
from topic7_data import TOPIC_7_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic7_Equilibria.pdf"
    topic_title = "Topic 7 — Equilibria"
    topic_subtitle = "7.1 Chemical Equilibria · Le Chatelier · Kc & Kp · Industrial Processes · 7.2 Brønsted-Lowry Acids & Bases"
    
    subtopics_summary = [
        ("7.1 Chemical equilibria", "Dynamic equilibrium features, Le Chatelier's principle (concentration, pressure, temperature, catalysts), Kc and Kp calculations, Haber and Contact processes compromise conditions"),
        ("7.2 Brønsted-Lowry acids & bases", "Proton donors and acceptors, conjugate acid-base pairs, strong vs weak acids/bases, experimental distinctions (pH, conductivity, reaction rates), autoionisation of water Kw")
    ]
    
    subtopic_map = {
        "7.1": "SUBTOPIC 7.1 — CHEMICAL EQUILIBRIA, LE CHATELIER, Kc & Kp",
        "7.2": "SUBTOPIC 7.2 — BRØNSTED-LOWRY ACIDS & BASES"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_7_QUESTIONS
    )

if __name__ == "__main__":
    main()
