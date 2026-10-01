"""
Run script to build Paper 1 (Multiple Choice) Topic 21: Organic Synthesis.
"""
from mcq_topic21_data import TOPIC_21_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic21_Organic_Synthesis.pdf"
    topic_title = "Topic 21 — Organic Synthesis (Paper 1 Multiple Choice)"
    topic_subtitle = "21.1 Multi-Step Synthetic Routes & Functional Group Interconversions · 21.2 Synthetic Strategies, Yields, Reagents & Regiochemistry · High-Frequency Repeats"
    
    subtopics_summary = [
        ("21.1 Multi-Step Synthetic Routes & Functional Group Interconversions", "Devising 2-, 3-, and 4-step synthetic pathways connecting all AS functional groups: alkanes, halogenoalkanes, alkenes, alcohols (1°, 2°, 3°), aldehydes, ketones, carboxylic acids, esters, acyl chlorides, amides, and nitriles; reagent and condition selection; selective oxidation (distillation vs reflux with acidified K2Cr2O7); selective reduction (NaBH4 for carbonyls vs LiAlH4 for nitriles/acids); nucleophilic substitutions and eliminations; strategic carbon chain extension via nitriles and cyanohydrins."),
        ("21.2 Synthetic Strategies, Yields, Reagents & Regiochemistry", "Retrosynthetic analysis and strategic disconnections; overall multi-step percentage yield calculations; atom economy and E-factor comparisons; regioselectivity (Markovnikov's rule in HX addition, Zaitsev's rule in base-induced elimination); stereochemical outcomes (Walden inversion in SN2, racemization in SN1, optical activity); practical synthetic methods (reflux vs distillation, solvent effects, separating funnel extraction, drying agents, recrystallisation criteria)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Organic Synthesis (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "21.1": "SUBTOPIC 21.1 — MULTI-STEP SYNTHETIC ROUTES & FUNCTIONAL GROUP INTERCONVERSIONS (Q1 – Q55)",
        "21.2": "SUBTOPIC 21.2 — SYNTHETIC STRATEGIES, YIELDS, REAGENTS & REGIOCHEMISTRY (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_21_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
