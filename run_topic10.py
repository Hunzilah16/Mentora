"""
Run script to build Topic 10: Group 2.
"""
from topic10_data import TOPIC_10_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic10_Group2.pdf"
    topic_title = "Topic 10 — Group 2: The Alkaline Earth Metals"
    topic_subtitle = "10.1 Similarities & Trends in Properties of Mg to Ba and Their Compounds · Thermal Stability · Solubility"
    
    subtopics_summary = [
        ("10.1 Physical & Chemical Trends", "Reactions of Mg to Ba with oxygen, water, steam, and dilute acids; trends in atomic/ionic radii and first two ionisation energies."),
        ("10.1 Thermal Stability of Compounds", "Thermal decomposition of carbonates and nitrates; explanation using cation radius, charge density, and polarising power on oxoanions."),
        ("10.1 Solubility Trends & Qualitative Analysis", "Opposing solubility trends of hydroxides (increasing) and sulfates (decreasing); sulfate test with BaCl2; lime in agriculture and flue-gas desulfurisation.")
    ]
    
    subtopic_map = {
        "10.1": "SUBTOPIC 10.1 — GROUP 2: TRENDS, REACTIONS & COMPOUNDS"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_10_QUESTIONS
    )

if __name__ == "__main__":
    main()
