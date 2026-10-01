"""
Run script to build Topic 15: Halogen Compounds.
"""
from topic15_data import TOPIC_15_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic15_Halogen_Compounds.pdf"
    topic_title = "Topic 15 — Halogen Compounds (Halogenoalkanes)"
    topic_subtitle = "15.1 Reactions (Substitution & Elimination) · 15.2 Mechanisms (SN1 vs SN2) · Hydrolysis Rates · CFCs"
    
    subtopics_summary = [
        ("15.1 Reactions of Halogenoalkanes", "Nucleophilic substitutions by OH⁻ (alcohols), CN⁻ (nitriles), and NH3 (amines); elimination to form alkenes; conditions dictating pathway."),
        ("15.2 Mechanisms of Nucleophilic Substitution", "SN1 (two-step via planar carbocation, racemisation) vs SN2 (concerted backside attack, Walden inversion); kinetics and transition states."),
        ("15.2 Hydrolysis Rates & Environmental Chemistry", "Relative rates with aqueous AgNO3 in ethanol governed by C-X bond enthalpy (C-I > C-Br > C-Cl); CFC photolysis and catalytic ozone depletion.")
    ]
    
    subtopic_map = {
        "15.1": "SUBTOPIC 15.1 — REACTIONS OF HALOGENOALKANES (SUBSTITUTION & ELIMINATION)",
        "15.2": "SUBTOPIC 15.2 — MECHANISMS (SN1 & SN2), HYDROLYSIS RATES & CFCS"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_15_QUESTIONS
    )

if __name__ == "__main__":
    main()
