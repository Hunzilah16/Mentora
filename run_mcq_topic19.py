"""
Run script to build Paper 1 (Multiple Choice) Topic 19: Nitrogen Compounds (Primary Amines, Amides & Nitriles).
"""
from mcq_topic19_data import TOPIC_19_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic19_Nitrogen_Compounds.pdf"
    topic_title = "Topic 19 — Nitrogen Compounds: Primary Amines, Amides & Nitriles (Paper 1 Multiple Choice)"
    topic_subtitle = "19.1 Primary Aliphatic Amines: Basicity, Synthesis & Reactions · 19.2 Nitriles & Amides: Formation, Hydrolysis & Neutrality · High-Frequency Repeats"
    
    subtopics_summary = [
        ("19.1 Primary Aliphatic Amines: Basicity, Synthesis & Reactions", "Structure and pyramidal geometry (~107°); intermolecular hydrogen bonding and volatility trends; Bronsted-Lowry basicity and relative base strengths (ethylamine > ammonia > phenylamine); +I inductive electron donation vs resonance delocalization; reactions with mineral acids (alkylammonium salts); synthesis from halogenoalkanes and haloalkane polyalkylation suppression; reduction of nitriles with LiAlH4 or H2/Ni; nucleophilic substitution with haloalkanes and acyl chlorides; copper(II) and silver(I) complex formation."),
        ("19.2 Nitriles & Amides: Formation, Hydrolysis & Neutrality", "Amide group structure, coplanarity, and neutrality in water due to carbonyl pi resonance delocalization; preparation of primary and substituted amides from acyl chlorides; acid and alkaline hydrolysis of amides (releasing carboxylic acids/salts and NH3); preparation of nitriles from halogenoalkanes (chain lengthening) and aldehydes/ketones (cyanohydrins); acid/alkaline hydrolysis of nitriles; catalytic and chemical reduction to primary amines; dehydration of amides to nitriles with P4O10; commercial polyamides (Nylon-6,6, Kevlar) and biodegradability."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Nitrogen Compounds (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "19.1": "SUBTOPIC 19.1 — PRIMARY ALIPHATIC AMINES: BASICITY, SYNTHESIS & REACTIONS (Q1 – Q55)",
        "19.2": "SUBTOPIC 19.2 — NITRILES & AMIDES: FORMATION, HYDROLYSIS & NEUTRALITY (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_19_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
