"""
Run script to build Topic 14: Hydrocarbons.
"""
from topic14_data import TOPIC_14_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic14_Hydrocarbons.pdf"
    topic_title = "Topic 14 — Hydrocarbons"
    topic_subtitle = "14.1 Alkanes (Cracking, Combustion, Free Radicals) · 14.2 Alkenes (Electrophilic Addition, Oxidation, Polymers)"
    
    subtopics_summary = [
        ("14.1 Alkanes", "Crude oil refining, catalytic cracking (zeolite), complete/incomplete combustion (CO hazard), and free-radical substitution mechanisms."),
        ("14.2 Alkenes", "Electrophilic addition reactions (H2, Br2, HX, steam), Markovnikov's rule and carbocation stability, oxidative cleavage with KMnO4, and addition polymerisation.")
    ]
    
    subtopic_map = {
        "14.1": "SUBTOPIC 14.1 — ALKANES: CRACKING, COMBUSTION & FREE-RADICAL SUBSTITUTION",
        "14.2": "SUBTOPIC 14.2 — ALKENES: ELECTROPHILIC ADDITION, OXIDATION & POLYMERISATION"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_14_QUESTIONS
    )

if __name__ == "__main__":
    main()
