"""
Run script to build Topic 8: Reaction Kinetics.
"""
from topic8_data import TOPIC_8_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic8_Reaction_Kinetics.pdf"
    topic_title = "Topic 8 — Reaction Kinetics"
    topic_subtitle = "8.1 Rate of Reaction · Collision Theory · Tangents · 8.2 Temperature & Boltzmann · 8.3 Catalysis"
    
    subtopics_summary = [
        ("8.1 Rate of reaction", "Rate definitions, collision theory (fruitful collisions, Ea, orientation), experimental monitoring (gas syringe, mass loss, colorimetry, conductivity, titrations), initial rates & tangents"),
        ("8.2 Temperature & Boltzmann", "Maxwell-Boltzmann distribution of molecular kinetic energies, temperature shifts, activation energy, why a 10 °C rise doubles rate"),
        ("8.3 Catalysis", "Homogeneous vs heterogeneous catalysts, adsorption-reaction-desorption mechanism, catalyst poisoning, enzymes, automotive catalytic converters, shift in activation energy")
    ]
    
    subtopic_map = {
        "8.1": "SUBTOPIC 8.1 — RATE OF REACTION & EXPERIMENTAL METHODS",
        "8.2": "SUBTOPIC 8.2 — TEMPERATURE & MAXWELL-BOLTZMANN DISTRIBUTIONS",
        "8.3": "SUBTOPIC 8.3 — HOMOGENEOUS & HETEROGENEOUS CATALYSIS"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_8_QUESTIONS
    )

if __name__ == "__main__":
    main()
