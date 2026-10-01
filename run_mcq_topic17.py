"""
Run script to build Paper 1 (Multiple Choice) Topic 17: Carbonyl Compounds (Aldehydes & Ketones).
"""
from mcq_topic17_data import TOPIC_17_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic17_Carbonyl_Compounds.pdf"
    topic_title = "Topic 17 — Carbonyl Compounds: Aldehydes & Ketones (Paper 1 Multiple Choice)"
    topic_subtitle = "17.1 Structure, Physical Properties & Nucleophilic Addition of HCN · 17.2 Diagnostic Testing: 2,4-DNPH, Tollens', Fehling's & Tri-iodomethane Reaction · High-Frequency Repeats"
    
    subtopics_summary = [
        ("17.1 Structure, Properties & Nucleophilic Addition", "Planar sp2 hybridised carbonyl group (>C=O), strong permanent dipole-dipole attractions, water solubility via hydrogen-bond acceptance; nucleophilic addition of HCN catalyzed by NaCN/OH- (cyanohydrin formation); optical inactivity of racemic cyanohydrin mixtures due to equal probability of top/bottom attack; reduction with NaBH4 to 1° and 2° alcohols; hydrolysis of cyanohydrins to alpha-hydroxy acids."),
        ("17.2 Diagnostic Testing & The Iodoform Reaction", "Condensation with 2,4-dinitrophenylhydrazine (Brady's reagent) forming yellow/orange/red crystalline precipitates with sharp melting points for identification; distinction between aldehydes and ketones using Tollens' reagent (silver mirror) and Fehling's solution (brick-red Cu2O precipitate); oxidation by acidified K2Cr2O7; the tri-iodomethane (iodoform) reaction identifying methyl carbonyls (CH3-CO-)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Carbonyl Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "17.1": "SUBTOPIC 17.1 — STRUCTURE, PROPERTIES & NUCLEOPHILIC ADDITION (Q1 – Q55)",
        "17.2": "SUBTOPIC 17.2 — DIAGNOSTIC TESTING & THE IODOFORM REACTION (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_17_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
