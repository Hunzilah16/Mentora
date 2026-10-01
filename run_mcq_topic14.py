"""
Run script to build Paper 1 (Multiple Choice) Topic 14: Hydrocarbons (Alkanes & Alkenes).
"""
from mcq_topic14_data import TOPIC_14_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic14_Hydrocarbons.pdf"
    topic_title = "Topic 14 — Hydrocarbons: Alkanes & Alkenes (Paper 1 Multiple Choice)"
    topic_subtitle = "14.1 Alkanes: Combustion, Free Radical Substitution, Catalytic Cracking · 14.2 Alkenes: Electrophilic Addition, Markovnikov Rule, KMnO4 Oxidation · High-Frequency Repeats"
    
    subtopics_summary = [
        ("14.1 Alkanes: Combustion, Substitution & Cracking", "Complete vs incomplete combustion (CO toxicity, unburnt hydrocarbons, greenhouse warming); mechanism of free radical substitution (initiation via UV homolytic fission, propagation cycles, termination pairings); thermal vs catalytic cracking of long-chain petroleum fractions over zeolite catalysts."),
        ("14.2 Alkenes: Electrophilic Addition & Oxidation", "Electrophilic addition of halogens, hydrogen halides, and steam (industrial hydration with H3PO4); Markovnikov's rule and inductive stabilization of carbocation intermediates (3° > 2° > 1°); mild oxidation with cold dilute KMnO4 (forming vicinal diols); oxidative cleavage with hot concentrated acidified KMnO4 (yielding CO2, carboxylic acids, and ketones); addition polymerisation."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Hydrocarbon Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "14.1": "SUBTOPIC 14.1 — ALKANES: COMBUSTION, SUBSTITUTION & CRACKING (Q1 – Q40)",
        "14.2": "SUBTOPIC 14.2 — ALKENES: ELECTROPHILIC ADDITION & OXIDATION (Q41 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_14_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
