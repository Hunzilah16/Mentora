"""
Run script to build Paper 1 (Multiple Choice) Topic 12: Nitrogen and Sulfur.
"""
from mcq_topic12_data import TOPIC_12_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic12_Nitrogen_Sulfur.pdf"
    topic_title = "Topic 12 — Nitrogen and Sulfur (Paper 1 Multiple Choice)"
    topic_subtitle = "12.1 Nitrogen Chemistry: Chemical Inertness, Ammonia, Ammonium Salts, Oxides of Nitrogen, Catalytic Cycles · 12.2 Sulfur Chemistry: SO2, Acid Rain, Flue Gas Desulfurisation, Contact Process · High-Frequency Repeats"
    
    subtopics_summary = [
        ("12.1 Nitrogen, Ammonia & Nitrogen Oxides", "Lack of reactivity of N2 due to high triple bond enthalpy (945 kJ mol^-1) and non-polarity; basicity of ammonia (lone pair donor) and formation of ammonium salts; displacement of NH3 by warming with strong base; formation of NO/NO2 in car engines and lightning; catalytic role of NO2 in atmospheric SO2 oxidation; removal of exhaust gases by catalytic converters."),
        ("12.2 Sulfur Chemistry & Environmental Impact", "Combustion of sulfur-containing fossil fuels forming SO2; role of SO2 and NO2 in acid rain formation; environmental consequences of acid rain on limestone, aquatic life, and soil leaching; industrial prevention via flue gas desulfurisation (FGD with CaO/CaCO3); conversion of SO2 to SO3 in the Contact Process using V2O5 catalyst."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Nitrogen and Sulfur Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "12.1": "SUBTOPIC 12.1 — NITROGEN, AMMONIA & NITROGEN OXIDES (Q1 – Q55)",
        "12.2": "SUBTOPIC 12.2 — SULFUR CHEMISTRY, ACID RAIN & CONTACT PROCESS (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_12_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
