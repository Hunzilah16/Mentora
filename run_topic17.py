"""
Run script to build Topic 17: Carbonyl Compounds (Aldehydes and Ketones).
"""
from topic17_data import TOPIC_17_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic17_Carbonyl_Compounds.pdf"
    topic_title = "Topic 17 — Carbonyl Compounds (Aldehydes & Ketones)"
    topic_subtitle = "17.1 Aldehydes & Ketones · Nucleophilic Addition (HCN) · Reduction (NaBH4) · Diagnostic Tests (2,4-DNPH, Tollens', Fehling's) · Iodoform Reaction"
    
    subtopics_summary = [
        ("17.1 Structure & Nucleophilic Addition", "Polarity of carbonyl C=O, nucleophilic addition of HCN via planar trigonal carbonyl carbon; stereochemical racemisation; synthetic transformations of 2-hydroxynitriles to carboxylic acids and amines."),
        ("17.1 Reduction & Interconversions", "Hydride transfer mechanism using NaBH4 (in aqueous ethanol) reducing aldehydes to 1° alcohols and ketones to 2° alcohols; comparison with LiAlH4 in dry ether."),
        ("17.1 Diagnostic Chemical Tests & Iodoform Reaction", "Condensation with 2,4-DNPH (Brady's reagent) and derivative melting points; distinction between aldehydes and ketones using Tollens' silver mirror and Fehling's brick-red Cu2O; alkaline tri-iodomethane (iodoform) test for CH3-CO- group.")
    ]
    
    subtopic_map = {
        "17.1": "SUBTOPIC 17.1 — CARBONYL COMPOUNDS (ALDEHYDES & KETONES)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_17_QUESTIONS
    )

if __name__ == "__main__":
    main()
