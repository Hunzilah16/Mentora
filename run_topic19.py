"""
Run script to build Topic 19: Nitrogen Compounds (Amines and Nitriles).
"""
from topic19_data import TOPIC_19_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic19_Nitrogen_Compounds.pdf"
    topic_title = "Topic 19 — Nitrogen Compounds (Amines & Nitriles)"
    topic_subtitle = "19.1 Primary Amines · Basicity & Inductive Effects · Salt Formation & Acylation · 19.2 Nitriles · Hydrolysis & Reduction Pathways"
    
    subtopics_summary = [
        ("19.1 Primary Amines & Basicity Trends", "Preparation from halogenoalkanes and excess ammonia; relative basicity (aliphatic primary amines > ammonia > phenylamine) governed by +I alkyl groups and aromatic pi delocalisation; physical properties and hydrogen bonding."),
        ("19.1 Reactions of Primary Amines", "Salt formation with mineral acids (RNH3+Cl-) and liberation by strong base; acylation with acyl chlorides to form substituted amides (peptide link); complexation and ligand exchange with aqueous copper(II) ions."),
        ("19.2 Nitriles & Hydroxynitriles", "Nucleophilic substitution (KCN) for +1 carbon chain extension; nucleophilic addition of HCN to carbonyls; acid hydrolysis (carboxylic acids) vs alkaline hydrolysis (carboxylates + NH3); reduction to pure primary amines via LiAlH4 or H2/Ni.")
    ]
    
    subtopic_map = {
        "19.1": "SUBTOPIC 19.1 — PRIMARY AMINES (STRUCTURE, BASICITY & REACTIONS)",
        "19.2": "SUBTOPIC 19.2 — NITRILES & HYDROXYNITRILES (SYNTHESIS, HYDROLYSIS & REDUCTION)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_19_QUESTIONS
    )

if __name__ == "__main__":
    main()
