"""
Run script to build Paper 1 (Multiple Choice) Topic 20: Polymerisation (Addition Polymers).
"""
from mcq_topic20_data import TOPIC_20_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic20_Polymerisation.pdf"
    topic_title = "Topic 20 — Polymerisation: Addition Polymers (Paper 1 Multiple Choice)"
    topic_subtitle = "20.1 Addition Polymerisation: Monomers, Repeat Units & Properties · 20.2 Disposal, Recycling & Environmental Impact · High-Frequency Repeats"
    
    subtopics_summary = [
        ("20.1 Addition Polymerisation: Monomers, Repeat Units & Properties", "Addition polymerisation characteristics (C=C double bond cleavage, all-carbon backbone, 100% atom economy); deducing repeat unit from monomer and monomer from polymer chain; poly(ethene), poly(propene), poly(chloroethene) (PVC), poly(phenylethene) (polystyrene), poly(tetrafluoroethene) (PTFE / Teflon), poly(methyl methacrylate) (PMMA / Perspex), poly(acrylonitrile) (acrylic); structural property relationships: LDPE vs HDPE (chain branching, density, crystallinity, intermolecular dispersion forces), dipole-dipole attractions in PVC, plasticizer function in flexible PVC."),
        ("20.2 Disposal, Recycling & Environmental Impact", "Environmental persistence of polyalkenes due to inert, non-polar C-C and C-H sigma bonds (impervious to hydrolysis and bacterial enzymes); landfill accumulation, leaching of additives, marine microplastics; waste incineration for energy recovery vs greenhouse gas emissions (CO2) and toxic emissions (HCl from PVC) requiring flue gas neutralization (CaCO3 / CaO scrubbers); mechanical recycling, sorting technologies (Resin Identification Codes, sink-float density separation, NIR optical sorting) vs chemical feedstock recycling (pyrolysis cracking to virgin-grade monomers); photodegradable addition polymers (carbonyl group UV absorption) and biodegradable polyesters (PLA)."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Addition Polymerisation and Polymer Disposal (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "20.1": "SUBTOPIC 20.1 — ADDITION POLYMERISATION: MONOMERS, REPEAT UNITS & PROPERTIES (Q1 – Q55)",
        "20.2": "SUBTOPIC 20.2 — DISPOSAL, RECYCLING & ENVIRONMENTAL IMPACT (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_20_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
