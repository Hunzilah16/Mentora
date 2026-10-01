"""
Run script to build Topic 18: Carboxylic Acids and Derivatives.
"""
from topic18_data import TOPIC_18_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic18_Carboxylic_Acids.pdf"
    topic_title = "Topic 18 — Carboxylic Acids and Derivatives"
    topic_subtitle = "18.1 Carboxylic Acids · Acidity & Inductive Effects · Reactions (Metals, Bases, Carbonates, LiAlH4) · 18.2 Esters & Hydrolysis"
    
    subtopics_summary = [
        ("18.1 Physical Properties & Carboxylate Resonance", "Hydrogen-bonded cyclic dimers in pure state; weak acid dissociation and resonance stabilisation of carboxylate anion; relative acidity compared to alcohols and phenols."),
        ("18.1 Substituent Effects & Chemical Reactions", "Negative inductive (-I) effect of halogen substituents on acid strength (pKa); effervescence with carbonates (CO2 test); reduction by LiAlH4 in dry ether; chlorination to acyl chlorides (SOCl2/PCl5)."),
        ("18.2 Esters & Hydrolysis Pathways", "Acid-catalysed condensation esterification (Le Chatelier's equilibrium) vs acyl chloride routes; reversible acid hydrolysis vs irreversible alkaline saponification (soap making and biodiesel).")
    ]
    
    subtopic_map = {
        "18.1": "SUBTOPIC 18.1 — CARBOXYLIC ACIDS (STRUCTURE, ACIDITY & REACTIONS)",
        "18.2": "SUBTOPIC 18.2 — ESTERS (FORMATION, PROPERTIES & HYDROLYSIS)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_18_QUESTIONS
    )

if __name__ == "__main__":
    main()
