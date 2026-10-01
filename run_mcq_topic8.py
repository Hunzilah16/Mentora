"""
Run script to build Paper 1 (Multiple Choice) Topic 8: Reaction Kinetics.
"""
from mcq_topic8_data import TOPIC_8_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic8_Reaction_Kinetics.pdf"
    topic_title = "Topic 8 — Reaction Kinetics (Paper 1 Multiple Choice)"
    topic_subtitle = "8.1 Collision Theory & Monitoring Rates · 8.2 Temperature & Maxwell-Boltzmann Distributions · 8.3 Catalysis · High-Frequency Repeats"
    
    subtopics_summary = [
        ("8.1 Collision Theory & Monitoring", "Collision theory criteria (E >= Ea and steric orientation), concentration, pressure, and surface area effects, experimental monitoring techniques (gas syringe, mass loss, colorimetry, turbidity, quenching), and initial rates."),
        ("8.2 Temperature & Maxwell-Boltzmann", "Features of Maxwell-Boltzmann energy distribution curves, temperature shifts (peak rightward and downward), area conservation, and exponential increase in fruitful collisions (why 10 K roughly doubles reaction rate)."),
        ("8.3 Homogeneous & Heterogeneous Catalysis", "Catalyst definitions, lowering Ea on Maxwell-Boltzmann and energy profile diagrams, homogeneous transition-metal mechanisms (Fe2+/Fe3+), heterogeneous surface catalysis steps (adsorption, bond weakening, reaction, desorption), and catalyst poisoning."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Reaction Kinetics (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "8.1": "SUBTOPIC 8.1 — COLLISION THEORY & MONITORING METHODS (Q1 – Q40)",
        "8.2": "SUBTOPIC 8.2 — TEMPERATURE & MAXWELL-BOLTZMANN DISTRIBUTIONS (Q41 – Q75)",
        "8.3": "SUBTOPIC 8.3 — HOMOGENEOUS & HETEROGENEOUS CATALYSIS (Q76 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_8_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
