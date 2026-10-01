"""
Run script to build Paper 1 (Multiple Choice) Topic 3: Chemical Bonding.
"""
from mcq_topic3_data import TOPIC_3_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic3_Chemical_Bonding.pdf"
    topic_title = "Topic 3 — Chemical Bonding (Paper 1 Multiple Choice)"
    topic_subtitle = "3.1 Electronegativity · 3.2 Ionic Lattices · 3.3 Metallic Bonding · 3.4 Covalent & Dative · 3.5 Shapes & VSEPR · 3.6 Intermolecular Forces · 3.7 Lewis Structures · High-Frequency Repeats"
    
    subtopics_summary = [
        ("3.1 Electronegativity & Bonding", "Pauling scale, periodic trends across periods and down groups, bond dipole moments, symmetrical cancellation, and the covalent-ionic continuum."),
        ("3.2 Ionic Bonding & Giant Lattices", "Non-directional electrostatic attractions, lattice energy factors (charge and radius), NaCl 6:6 and CsCl 8:8 lattices, physical properties, electrical conductivity, and brittleness."),
        ("3.3 Metallic Bonding & Properties", "Electrostatic attraction to delocalised sea of electrons, Period 3 strength trends (Na < Mg < Al), thermal and electrical conductivity mechanisms, malleability, and alloys."),
        ("3.4 Covalent & Coordinate (Dative) Bonding", "Shared electron pairs, orbital overlap (sigma vs pi), bond enthalpy vs length, coordinate bonds in NH4+, H3O+, Al2Cl6, CO, and adducts, equivalence of bonds once formed."),
        ("3.5 Shapes of Molecules & VSEPR Theory", "Electron pair repulsion hierarchy, bond angle compression (~2.5° per lone pair), linear (180°), trigonal planar (120°), tetrahedral (109.5°), pyramidal (107°), bent (104.5°), trigonal bipyramidal (90°/120°), octahedral (90°)."),
        ("3.6 Intermolecular Forces & Hydrogen Bonding", "London dispersion forces (instantaneous-induced dipoles, polarisability, surface area), permanent dipole-dipole forces, hydrogen bonding criteria, anomalous properties of water and ice, and DNA base pairing."),
        ("3.7 Dot-and-Cross Diagrams & Lewis Structures", "Octet rule, electron-deficient molecules (BF3), expanded octet hypervalent species (PCl5, SF6), polyatomic ions, and non-bonding lone pairs."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Chemical Bonding (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "3.1": "SUBTOPIC 3.1 — ELECTRONEGATIVITY & BOND POLARITY (Q1 – Q14)",
        "3.2": "SUBTOPIC 3.2 — IONIC BONDING & GIANT LATTICES (Q15 – Q28)",
        "3.3": "SUBTOPIC 3.3 — METALLIC BONDING & PHYSICAL PROPERTIES (Q29 – Q42)",
        "3.4": "SUBTOPIC 3.4 — COVALENT & COORDINATE (DATIVE) BONDING (Q43 – Q64)",
        "3.5": "SUBTOPIC 3.5 — SHAPES OF MOLECULES & VSEPR THEORY (Q65 – Q80)",
        "3.6": "SUBTOPIC 3.6 — INTERMOLECULAR FORCES & HYDROGEN BONDING (Q81 – Q95)",
        "3.7": "SUBTOPIC 3.7 — DOT-AND-CROSS DIAGRAMS & LEWIS STRUCTURES (Q96 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_3_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
