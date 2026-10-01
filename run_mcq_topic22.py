"""
Run script to build Paper 1 (Multiple Choice) Topic 22: Analytical Chemistry (IR & Mass Spectrometry).
"""
from mcq_topic22_data import TOPIC_22_MCQ_QUESTIONS
from build_mcq_topic_pdf import build_mcq_pdf_document

def main():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Paper1_Topic22_Analytical_Chemistry.pdf"
    topic_title = "Topic 22 — Analytical Chemistry: IR & Mass Spectrometry (Paper 1 Multiple Choice)"
    topic_subtitle = "22.1 Infrared Spectroscopy: Principles, Absorption Bands & Greenhouse Effect · 22.2 Mass Spectrometry: Molecular Ions, [M+1], [M+2] & Fragmentation · High-Frequency Repeats"
    
    subtopics_summary = [
        ("22.1 Infrared Spectroscopy: Principles, Bands & Greenhouse Effect", "Principles of infrared spectroscopy (molecular vibrations, stretching and bending, requirement for changing dipole moment); diagnostic absorption wavenumbers for O-H (alcohols 3200-3600 cm^-1 vs carboxylic acids broad 2500-3300 cm^-1), C=O (aldehydes, ketones, carboxylic acids, esters, amides), C-O, C-H (sp3 vs sp2 vs sp), C=C, C#C, C#N (2220-2260 cm^-1), N-H (primary amine doublet vs secondary amine singlet); fingerprint region (< 1500 cm^-1) for computer matching; molecular basis of the greenhouse effect (IR absorption by H2O, CO2, CH4 vs IR transparency of homonuclear N2 and O2)."),
        ("22.2 Mass Spectrometry: Molecular Ions, [M+1], [M+2] & Fragmentation", "Mass spectrometry instrumentation (electron impact ionization, acceleration, magnetic sector deflection by m/z, detection); molecular ion peak (M) and relative molecular mass (Mr); [M+1] peak and carbon counting formula; [M+2] isotope peaks for chlorine (3:1) and bromine (1:1); two-halogen clusters (two chlorines 9:6:1, two bromines 1:2:1, one Cl + one Br 3:4:1); fragmentation mechanics (homolytic/heterolytic cleavage, stability of carbocations, unobserved neutral radicals); diagnostic fragment ions (m/z 15 [CH3]+, 29 [C2H5]+/[CHO]+, 31 [CH2OH]+, 43 [CH3CO]+/[C3H7]+, 45 [COOH]+, 57 [C4H9]+, 77 [C6H5]+, 91 [C7H7]+ tropylium); combined IR and MS structural deduction."),
        ("High-Frequency Core Repeats", "The 10 most frequently examined Cambridge Paper 1 questions on Analytical Chemistry (Q101 – Q110).")
    ]
    
    subtopic_map = {
        "22.1": "SUBTOPIC 22.1 — INFRARED SPECTROSCOPY: PRINCIPLES, BANDS & GREENHOUSE EFFECT (Q1 – Q55)",
        "22.2": "SUBTOPIC 22.2 — MASS SPECTROMETRY: MOLECULAR IONS, [M+1], [M+2] & FRAGMENTATION (Q56 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    
    build_mcq_pdf_document(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=TOPIC_22_MCQ_QUESTIONS
    )

if __name__ == "__main__":
    main()
