"""
Run script to build Paper 1 (Multiple Choice) Topic 15: Halogenoalkanes.
"""
from mcq_topic15_data import TOPIC_15_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic15_Halogenoalkanes.pdf"
    topic_title = "Topic 15 — Halogenoalkanes (Paper 1 Multiple Choice)"
    topic_subtitle = "15.1 Nucleophilic Substitution: Mechanisms (SN1 vs SN2), Reagents & Reactivity Trends · 15.2 Elimination Reactions & Environmental Impact: CFCs and Ozone Depletion · High-Frequency Repeats"
    
    subtopics_summary = [
        ("15.1 Nucleophilic Substitution & Mechanisms", "Nucleophilic substitution by :OH- (hydrolysis to alcohols), :CN- (chain extension to nitriles), and :NH3 (excess ethanolic ammonia to primary amines); SN1 mechanism (two steps, planar carbocation intermediate, racemisation, 3° substrates) vs SN2 mechanism (one step, backside attack, Walden inversion, 1° substrates); reactivity trend C-F < C-Cl < C-Br < C-I determined by bond enthalpy; silver nitrate hydrolysis testing."),
        ("15.2 Elimination Reactions & Environmental Impact", "Elimination of hydrogen halides by heating with ethanolic KOH (base-promoted proton abstraction from beta-carbon yielding alkenes); Zaitsev's rule and major alkene isomer formation; chlorofluorocarbons (CFCs), atmospheric persistence, photolytic cleavage of C-Cl bonds in stratosphere forming .Cl radicals, catalytic ozone depletion cycle, Montreal Protocol, and hydrofluoroalkane (HFA) alternatives."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Halogenoalkanes (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "15.1": "SUBTOPIC 15.1 — NUCLEOPHILIC SUBSTITUTION & MECHANISMS (Q1 – Q55)",
        "15.2": "SUBTOPIC 15.2 — ELIMINATION REACTIONS & ENVIRONMENTAL IMPACT (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_15_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
