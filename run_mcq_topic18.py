"""
Run script to build Paper 1 (Multiple Choice) Topic 18: Carboxylic Acids and Derivatives (Acids & Esters).
"""
from mcq_topic18_data import TOPIC_18_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic18_Carboxylic_Acids_Esters.pdf"
    topic_title = "Topic 18 — Carboxylic Acids and Derivatives (Paper 1 Multiple Choice)"
    topic_subtitle = "18.1 Carboxylic Acids: Structure, Acidity, Inductive Effects & Reactions · 18.2 Esters: Formation, IUPAC Nomenclature & Acid/Alkaline Hydrolysis · High-Frequency Repeats"
    
    subtopics_summary = [
        ("18.1 Carboxylic Acids: Structure, Acidity & Reactions", "Cyclic hydrogen-bonded dimers, high boiling points; weak acidity (Ka/pKa) and resonance delocalization in the carboxylate anion (two equal 0.127 nm C-O bonds); inductive effects of halogen (-I) and alkyl (+I) substituents; reactions with reactive metals (H2), metal oxides, alkalis, and carbonates/hydrogencarbonates (CO2 effervescence test); reduction by LiAlH4 to primary alcohols; acyl chloride synthesis with PCl5, PCl3, and SOCl2."),
        ("18.2 Esters: Formation, Naming & Hydrolysis", "Esterification of carboxylic acids with alcohols catalyzed by concentrated H2SO4; rapid irreversible ester synthesis using acyl chlorides; systematic IUPAC nomenclature; reversible acid-catalyzed hydrolysis vs irreversible alkaline hydrolysis (saponification to carboxylate salts and alcohols); commercial uses (flavorings, fragrances, low-toxicity solvents, plasticizers); transesterification of triglycerides into biodiesel."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Carboxylic Acids and Esters (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "18.1": "SUBTOPIC 18.1 — CARBOXYLIC ACIDS: STRUCTURE, ACIDITY & REACTIONS (Q1 – Q55)",
        "18.2": "SUBTOPIC 18.2 — ESTERS: FORMATION, NAMING & HYDROLYSIS (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_18_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
