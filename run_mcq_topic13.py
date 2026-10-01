"""
Run script to build Paper 1 (Multiple Choice) Topic 13: Introduction to AS Level Organic Chemistry.
"""
from mcq_topic13_data import TOPIC_13_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic13_Intro_Organic.pdf"
    topic_title = "Topic 13 — Introduction to AS Organic Chemistry (Paper 1 Multiple Choice)"
    topic_subtitle = "13.1 Formulas, IUPAC Nomenclature & Functional Groups · 13.2 Organic Reaction Terminology & Mechanisms · 13.3 Shapes of Molecules, Hybridisation & Bonding · 13.4 Structural & Stereoisomerism · High-Frequency Repeats"
    
    subtopics_summary = [
        ("13.1 Formulas, Nomenclature & Functional Groups", "Types of chemical formulae (empirical, molecular, general, structural, displayed, skeletal); systematic IUPAC naming of alkanes, alkenes, halogenoalkanes, alcohols, aldehydes, ketones, carboxylic acids, esters, amines, and nitriles; functional group recognition in polyfunctional molecules."),
        ("13.2 Reaction Terminology & Mechanisms", "Homolytic vs heterolytic fission, free radicals, electrophiles, nucleophiles; classification of reaction types: addition, substitution, elimination, hydrolysis, condensation, oxidation, and reduction; curly arrow electron movement conventions; carbocation stability (+I inductive effect)."),
        ("13.3 Shapes of Molecules, Hybridisation & Bonding", "Orbital hybridisation (sp3 tetrahedral 109.5°, sp2 trigonal planar 120°, sp linear 180°); end-on sigma bond overlap vs sideways pi bond overlap; bond lengths and bond enthalpies; planar geometry of double bonds and carbonyl groups; restricted rotation around pi bonds."),
        ("13.4 Isomerism: Structural & Stereoisomerism", "Chain, positional, and functional group isomerism; stereoisomerism: cis-trans / E-Z isomerism in alkenes (restricted rotation and two different groups on each double-bond carbon); chirality and optical isomerism (asymmetric carbons, non-superimposable enantiomers, polarimetry, racemic mixtures)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Introductory Organic Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "13.1": "SUBTOPIC 13.1 — FORMULAS, NOMENCLATURE & FUNCTIONAL GROUPS (Q1 – Q30)",
        "13.2": "SUBTOPIC 13.2 — REACTION TERMINOLOGY & MECHANISMS (Q31 – Q55)",
        "13.3": "SUBTOPIC 13.3 — SHAPES OF MOLECULES, HYBRIDISATION & BONDING (Q56 – Q75)",
        "13.4": "SUBTOPIC 13.4 — STRUCTURAL & STEREOISOMERISM (Q76 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_13_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
