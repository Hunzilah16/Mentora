"""
Run script to build Topic 5: Chemical Energetics.
"""
from topic5_data import TOPIC_5_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic5_Chemical_Energetics.pdf"
    topic_title = "Topic 5 — Chemical Energetics"
    topic_subtitle = "5.1 Enthalpy Change · Standard Conditions · Calorimetry · 5.2 Hess's Law · Bond Energies"
    
    subtopics_summary = [
        ("5.1 Enthalpy change, delta-H", "Standard conditions (298 K, 100 kPa), definitions of formation, combustion, neutralisation, and atomisation, enthalpy profile diagrams, solution and flame calorimetry q = mc*delta-T, cooling curve extrapolation"),
        ("5.2 Hess's law", "Conservation of energy in cycles, calculations using standard enthalpies of formation and combustion, mean bond enthalpies, bond breaking vs bond forming, differences between bond energy and standard enthalpy calculations")
    ]
    
    subtopic_map = {
        "5.1": "SUBTOPIC 5.1 — ENTHALPY CHANGE, DELTA-H & CALORIMETRY",
        "5.2": "SUBTOPIC 5.2 — HESS'S LAW & BOND ENERGIES"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_5_QUESTIONS
    )

if __name__ == "__main__":
    main()
