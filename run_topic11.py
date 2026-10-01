"""
Run script to build Topic 11: Group 17 (The Halogens).
"""
from topic11_data import TOPIC_11_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic11_Group17.pdf"
    topic_title = "Topic 11 — Group 17: The Halogens"
    topic_subtitle = "11.1 Physical Properties & Enthalpies · 11.2 Chemical Properties & Displacement · 11.3 Halide Reactions · 11.4 Chlorine Chemistry"
    
    subtopics_summary = [
        ("11.1 Physical Properties & Enthalpies", "Colors and physical states at r.t.p., volatility, London dispersion forces, F-F bond enthalpy anomaly, and H-X thermal stability."),
        ("11.2 Chemical Properties & Displacement", "Halogen oxidising strength, aqueous displacement reactions, cyclohexane solvent extraction, and thermal stability of HX."),
        ("11.3 Halide Reactions: H2SO4 & AgNO3", "Relative reducing power of halide ions with concentrated H2SO4; qualitative identification with acidified AgNO3 and aqueous NH3."),
        ("11.4 Chlorine Chemistry & Disproportionation", "Disproportionation of Cl2 with cold dilute NaOH (bleach) and hot conc NaOH (chlorate(V)); water treatment and redox titrations.")
    ]
    
    subtopic_map = {
        "11.1": "SUBTOPIC 11.1 — PHYSICAL PROPERTIES & BOND ENTHALPIES",
        "11.2": "SUBTOPIC 11.2 — CHEMICAL PROPERTIES & DISPLACEMENT REACTIONS",
        "11.3": "SUBTOPIC 11.3 — REACTIONS OF HALIDE IONS: H2SO4 & SILVER NITRATE",
        "11.4": "SUBTOPIC 11.4 — REACTIONS OF CHLORINE & DISPROPORTIONATION"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_11_QUESTIONS
    )

if __name__ == "__main__":
    main()
