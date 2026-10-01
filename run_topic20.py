"""
Run script to build Topic 20: Polymerisation (Addition Polymerisation).
"""
from topic20_data import TOPIC_20_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic20_Polymerisation.pdf"
    topic_title = "Topic 20 — Polymerisation (Addition Polymerisation)"
    topic_subtitle = "20.1 Addition Polymerisation · Monomers & Repeat Units · LDPE vs HDPE Architecture · PVC & Plasticisers · Environmental Disposal & Recycling"
    
    subtopics_summary = [
        ("20.1 Addition Polymerisation & Repeat Units", "Opening of carbon-carbon double bonds (pi-bond cleavage); drawing repeat units from given alkene monomers and deducing monomers from polymer backbones; 100% atom economy."),
        ("20.1 Structure-Property Relationships", "Chain branching vs linearity: comparison of LDPE (high pressure, branched, flexible) and HDPE (Ziegler-Natta, linear, dense, rigid); effect of chain length on dispersion forces and tensile strength."),
        ("20.1 Polar Polymers & Environmental Fate", "Permanent dipole attractions in poly(chloroethene) (PVC) and internal lubrication by plasticisers; non-biodegradability in landfill; toxic combustion emissions (HCl gas and flue gas scrubbing with CaO); mechanical vs chemical feedstock recycling (pyrolysis).")
    ]
    
    subtopic_map = {
        "20.1": "SUBTOPIC 20.1 — ADDITION POLYMERISATION (STRUCTURE, PROPERTIES & DISPOSAL)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_20_QUESTIONS
    )

if __name__ == "__main__":
    main()
