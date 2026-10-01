"""
Run script to build Topic 6: Electrochemistry.
"""
from topic6_data import TOPIC_6_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic6_Electrochemistry.pdf"
    topic_title = "Topic 6 — Electrochemistry"
    topic_subtitle = "6.1 Redox Processes · Oxidation Numbers · Disproportionation · Titrations · 6.2 Electrolysis & Faraday's Laws"
    
    subtopics_summary = [
        ("6.1 Redox processes", "Rules for oxidation states, balancing complex ionic half-equations, disproportionation reactions, self-indicating manganate(VII) and iodine-thiosulfate redox titrations, reducing power of halide ions"),
        ("6.2 Electrolysis", "Electrolysis of molten salts (PbBr2, Al2O3) and aqueous solutions (brine, CuSO4, H2SO4), preferential discharge of cations and anions, Faraday's laws (Q = It, F = 96500 C/mol), industrial copper refining and electroplating")
    ]
    
    subtopic_map = {
        "6.1": "SUBTOPIC 6.1 — REDOX PROCESSES, OXIDATION NUMBERS & TITRATIONS",
        "6.2": "SUBTOPIC 6.2 — ELECTROLYSIS & QUANTITATIVE FARADAY CALCULATIONS"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_6_QUESTIONS
    )

if __name__ == "__main__":
    main()
