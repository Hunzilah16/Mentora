"""
Run script to build Paper 1 (Multiple Choice) Topic 4: States of Matter.
"""
from mcq_topic4_data import TOPIC_4_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic4_States_of_Matter.pdf"
    topic_title = "Topic 4 — States of Matter (Paper 1 Multiple Choice)"
    topic_subtitle = "4.1 Gaseous State: Kinetic Theory, Ideal & Real Gases, pV = nRT · 4.2 Liquid & Solid States: Giant & Molecular Lattices · High-Frequency Repeats"
    
    subtopics_summary = [
        ("4.1 The Gaseous State", "Kinetic-molecular theory, ideal gas equation pV = nRT, molar mass determination, non-ideal gas deviations (intermolecular forces and molecular volume), compressibility factor Z, Dalton's law of partial pressures, and Graham's law."),
        ("4.2 Liquid & Solid States", "Dynamic liquid-vapor equilibrium, boiling point vs external pressure, four crystal lattice types (giant ionic, giant covalent, giant metallic, simple molecular), allotropes of carbon (diamond, graphite, graphene, C60), and quartz SiO2."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on States of Matter (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "4.1": "SUBTOPIC 4.1 — THE GASEOUS STATE: IDEAL & REAL GASES (Q1 – Q50)",
        "4.2": "SUBTOPIC 4.2 — THE LIQUID & SOLID STATES (Q51 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_4_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
