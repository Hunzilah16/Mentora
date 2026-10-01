"""
Run script to build Topic 9: Chemical Periodicity.
"""
from topic9_data import TOPIC_9_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic9_Periodicity.pdf"
    topic_title = "Topic 9 — The Periodic Table: Chemical Periodicity"
    topic_subtitle = "9.1 Periodicity of Physical Properties (Period 3) · 9.2 Periodicity of Chemical Properties (Oxides & Chlorides)"
    
    subtopics_summary = [
        ("9.1 Physical Periodicity (Period 3)", "Trends across Period 3: atomic radius, ionic radius, melting points, electrical conductivity, and successive & first ionisation energies."),
        ("9.2 Chemical Periodicity (Oxides & Chlorides)", "Reactions of Period 3 elements with O2, Cl2, and H2O; structure, bonding, acid-base character of oxides; structure, bonding, and hydrolysis of chlorides.")
    ]
    
    subtopic_map = {
        "9.1": "SUBTOPIC 9.1 — PHYSICAL PERIODICITY ACROSS PERIOD 3",
        "9.2": "SUBTOPIC 9.2 — CHEMICAL PERIODICITY: OXIDES & CHLORIDES"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_9_QUESTIONS
    )

if __name__ == "__main__":
    main()
