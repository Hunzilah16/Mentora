"""
Run script to build Topic 21: Organic Synthesis.
"""
from topic21_data import TOPIC_21_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic21_Organic_Synthesis.pdf"
    topic_title = "Topic 21 — Organic Synthesis"
    topic_subtitle = "21.1 Organic Synthesis · Multi-Step Reaction Pathways · Functional Group Interconversions (FGI) · Carbon Chain Extension & Cleavage · Synthetic Strategy & Green Chemistry"
    
    subtopics_summary = [
        ("21.1 Functional Group Interconversions (FGI)", "Systematic conversion between alkanes, alkenes, halogenoalkanes, alcohols, aldehydes, ketones, carboxylic acids, esters, nitriles, and amines; identifying reagents and specific reaction conditions (temperature, catalysts, reflux vs distillation)."),
        ("21.1 Carbon Skeleton Modification", "Carbon chain extension via nucleophilic substitution of halogenoalkanes with cyanide (CN-) and nucleophilic addition of HCN to carbonyls; deducing synthetic routes that lengthen, maintain, or shorten carbon backbones."),
        ("21.1 Multi-Step Strategy & Green Chemistry", "Retrosynthetic analysis of target molecules; deducing structures of synthetic intermediates; calculating percentage yield and atom economy across multi-stage processes; hazard reduction and sustainable chemical synthesis.")
    ]
    
    subtopic_map = {
        "21.1": "SUBTOPIC 21.1 — ORGANIC SYNTHESIS (PATHWAYS, STRATEGIES & GREEN CHEMISTRY)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_21_QUESTIONS
    )

if __name__ == "__main__":
    main()
