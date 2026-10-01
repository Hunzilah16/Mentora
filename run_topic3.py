"""
Run script to build Topic 3: Chemical Bonding.
"""
from topic3_data import TOPIC_3_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic3_Chemical_Bonding.pdf"
    topic_title = "Topic 3 — Chemical Bonding"
    topic_subtitle = "3.1 Electronegativity · 3.2 Ionic · 3.3 Metallic · 3.4 Covalent & Dative · 3.5 VSEPR · 3.6 IMF · 3.7 Dot-and-Cross"
    
    subtopics_summary = [
        ("3.1 Electronegativity and bonding", "Pauling scale, periodic trends across periods and groups, non-polar vs polar bonds, dipole moments"),
        ("3.2 Ionic bonding", "Electrostatic attraction between oppositely charged ions, giant ionic lattices, physical properties (mp, conductivity, solubility)"),
        ("3.3 Metallic bonding", "Lattice of positive metal ions in a sea of delocalised electrons, electrical/thermal conductivity, malleability"),
        ("3.4 Covalent & coordinate bonding", "Shared electron pairs, orbital overlap (sigma and pi bonds), dative covalent bonds (NH4+, Al2Cl6, CO, H3O+)"),
        ("3.5 Shapes of molecules (VSEPR)", "Bond pair/lone pair repulsion (2 to 6 electron pairs), bond angles (180°, 120°, 109.5°, 107°, 104.5°, 90°)"),
        ("3.6 Intermolecular forces", "London dispersion (induced dipole), permanent dipole-dipole, and hydrogen bonding (N, O, F); boiling point anomalies"),
        ("3.7 Dot-and-cross diagrams", "Outer shell representations of ionic, covalent, and coordinate bonded species; octet expansion")
    ]
    
    subtopic_map = {
        "3.1": "SUBTOPIC 3.1 — ELECTRONEGATIVITY & BOND POLARITY",
        "3.2": "SUBTOPIC 3.2 — IONIC BONDING & LATTICE PROPERTIES",
        "3.3": "SUBTOPIC 3.3 — METALLIC BONDING & PROPERTIES",
        "3.4": "SUBTOPIC 3.4 — COVALENT & COORDINATE (DATIVE) BONDING",
        "3.5": "SUBTOPIC 3.5 — VSEPR THEORY & MOLECULAR GEOMETRY",
        "3.6": "SUBTOPIC 3.6 — INTERMOLECULAR FORCES & PHYSICAL PROPERTIES",
        "3.7": "SUBTOPIC 3.7 — DOT-AND-CROSS REPRESENTATIONS"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_3_QUESTIONS
    )

if __name__ == "__main__":
    main()
