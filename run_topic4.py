"""
Run script to build Topic 4: States of Matter.
"""
from topic4_data import TOPIC_4_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic4_States_of_Matter.pdf"
    topic_title = "Topic 4 — States of Matter"
    topic_subtitle = "4.1 The Gaseous State · pV = nRT · Real Gas Deviations · 4.2 Solid Lattices & Allotropes"
    
    subtopics_summary = [
        ("4.1 The gaseous state", "Kinetic theory assumptions, ideal gas equation pV = nRT, deviations from ideality (compressibility factor), Mr of volatile liquids, gas density & stoichiometry"),
        ("4.2 Bonding and structure", "Solid lattices (giant ionic, giant covalent, giant metallic, simple molecular), carbon allotropes (diamond, graphite, graphene, C60), open lattice of ice, liquids & vapour pressure")
    ]
    
    subtopic_map = {
        "4.1": "SUBTOPIC 4.1 — THE GASEOUS STATE: IDEAL & REAL GASES, pV = nRT",
        "4.2": "SUBTOPIC 4.2 — BONDING & STRUCTURE: LATTICES & ALLOTROPES"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_4_QUESTIONS
    )

if __name__ == "__main__":
    main()
