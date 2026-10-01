"""
Run script to build Topic 12: Nitrogen and Sulfur.
"""
from topic12_data import TOPIC_12_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic12_Nitrogen_Sulfur.pdf"
    topic_title = "Topic 12 — Nitrogen and Sulfur"
    topic_subtitle = "12.1 Nitrogen & Ammonia · 12.2 Nitrogen Oxides in Atmosphere · 12.3 Sulfur & The Contact Process · Acid Rain"
    
    subtopics_summary = [
        ("12.1 Nitrogen, Ammonia & Fertilisers", "Unreactivity of N2 (triple bond), basicity of NH3, ammonium ion structure (dative bonding), fertilisers, and environmental eutrophication."),
        ("12.2 Nitrogen Oxides & Smog", "Formation of NO in car engines, catalytic converters (Pt/Rh/Pd honeycomb), tropospheric ozone and PAN in photochemical smog."),
        ("12.3 Sulfur & The Contact Process", "Manufacture of H2SO4 by the Contact process (V2O5 catalyst, 450 °C, 1-2 atm, oleum), acid rain corrosion, and flue-gas desulfurisation.")
    ]
    
    subtopic_map = {
        "12.1": "SUBTOPIC 12.1 — NITROGEN, AMMONIA, FERTILISERS & EUTROPHICATION",
        "12.2": "SUBTOPIC 12.2 — NITROGEN OXIDES IN THE ATMOSPHERE & CATALYTIC CONVERTERS",
        "12.3": "SUBTOPIC 12.3 — SULFUR, THE CONTACT PROCESS & ACID RAIN"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_12_QUESTIONS
    )

if __name__ == "__main__":
    main()
