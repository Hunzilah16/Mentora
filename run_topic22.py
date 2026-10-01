"""
Run script to build Topic 22: Analytical Techniques.
"""
from topic22_data import TOPIC_22_QUESTIONS
from build_topic_pdf import build_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Topic22_Analytical_Techniques.pdf"
    topic_title = "Topic 22 — Analytical Techniques"
    topic_subtitle = "22.1 Infrared Spectroscopy · 22.2 Mass Spectrometry · Characteristic IR Absorption Ranges · Molecular Ion [M]+ & [M+1]+ Carbon Ratios · Isotopic Multiplicity (35Cl/37Cl & 79Br/81Br) · Fragmentation & Structural Elucidation"
    
    subtopics_summary = [
        ("22.1 Infrared Spectroscopy", "Covalent bond vibrations (stretching and bending modes) and dipole moment change requirement; characteristic absorption ranges from Data Booklet (O-H, C=O, C-H, C=C, C=N, C-O, N-H); distinguishing functional group isomers; monitoring reaction progress; fingerprint region (< 1500 cm-1); atmospheric greenhouse gases."),
        ("22.2 Mass Spectrometry: Molecular Ion & Carbon Count", "Electron-impact ionisation to radical cations [M]+.; relative molecular mass Mr determination; [M+1]+ carbon-13 abundance calculation: n = (100 x [M+1]+) / (1.1 x [M]+)."),
        ("22.2 Mass Spectrometry: Isotope Patterns & Fragmentation", "Chlorine (35Cl:37Cl approx 3:1) and bromine (79Br:81Br approx 1:1) isotopic signatures in mono- and di-haloalkanes; alpha-cleavage and carbocation stability (acylium [RCO]+, oxonium [RCH=OH]+, tropylium [C7H7]+, alkyl carbocations); diagnostic neutral losses (M-15, M-17, M-18, M-28, M-31, M-45); comprehensive multi-technique structural elucidation.")
    ]
    
    subtopic_map = {
        "22.1": "SUBTOPIC 22.1 — INFRARED SPECTROSCOPY (PRINCIPLES, ABSORPTIONS & DIAGNOSTICS)",
        "22.2": "SUBTOPIC 22.2 — MASS SPECTROMETRY (MOLECULAR ION, ISOTOPIC RATIOS & FRAGMENTATION)"
    }
    
    build_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_22_QUESTIONS
    )

if __name__ == "__main__":
    main()
