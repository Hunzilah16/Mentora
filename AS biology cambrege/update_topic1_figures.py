"""
Attach expanded figures to questions in topic1_cell_structure_data.py
"""
import os

data_path = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\topic1_cell_structure_data.py"

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (
        '''    # Q6 [Past Paper 9700/21/O/N/23/Q1]
    questions.append(Question(
        number=6,
        title="9700/21/O/N/23/Q1 Resolution, Magnification & Electron Optics",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="CHALLENGING",
        preamble="The development of electron microscopes revolutionized cell biology by revealing structures that were completely invisible under light microscopes.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q6 [Past Paper 9700/21/O/N/23/Q1] - Visual Fig 1.12
    questions.append(Question(
        number=6,
        title="9700/21/O/N/23/Q1 Resolution, Magnification & Electron Optics",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="CHALLENGING",
        preamble="Fig. 1.12 shows the diffraction patterns and Airy disk intensity profiles for light waves and electron beams, demonstrating the Rayleigh criterion for resolution.",
        figure_path=os.path.join(DIAG_DIR, "fig1_12_resolution_diffraction.png"),
        figure_caption="Fig. 1.12: Diffraction patterns and resolution limit (Rayleigh criterion) for light vs electron waves.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
    (
        '''    # Q7 [Past Paper 9700/22/O/N/22/Q1]
    questions.append(Question(
        number=7,
        title="9700/22/O/N/22/Q1 Centrioles, Microtubules & Cilia Organization",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Centrioles, cilia, and flagella are specialized eukaryotic structures constructed from protein microtubules.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q7 [Past Paper 9700/22/O/N/22/Q1] - Visual Fig 1.10
    questions.append(Question(
        number=7,
        title="9700/22/O/N/22/Q1 Centrioles, Microtubules & Cilia Organization",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Fig. 1.10 is a diagram showing the transverse section ultrastructure of a centriole.",
        figure_path=os.path.join(DIAG_DIR, "fig1_10_centriole_structure.png"),
        figure_caption="Fig. 1.10: Transverse section schematic of a centriole showing 9+0 triplet microtubule architecture.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
    (
        '''    # Q8 [Past Paper 9700/23/M/J/23/Q1]
    questions.append(Question(
        number=8,
        title="9700/23/M/J/23/Q1 Nuclear Pore Complex & Ribosome Biogenesis",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="The eukaryotic nucleus is enclosed by a complex double membrane that coordinates molecular traffic with the cytoplasm.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q8 [Past Paper 9700/23/M/J/23/Q1] - Visual Fig 1.8
    questions.append(Question(
        number=8,
        title="9700/23/M/J/23/Q1 Nuclear Pore Complex & Ribosome Biogenesis",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Fig. 1.8 shows the fine ultrastructure of a eukaryotic nucleus as observed in an electron micrograph.",
        figure_path=os.path.join(DIAG_DIR, "fig1_8_nucleus_tem.png"),
        figure_caption="Fig. 1.8: Transmission electron micrograph diagram of the eukaryotic nucleus.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
    (
        '''    # Q9 [Past Paper 9700/21/M/J/23/Q2]
    questions.append(Question(
        number=9,
        title="9700/21/M/J/23/Q2 Mitochondria vs Chloroplasts: Endosymbiotic Theory",
        syllabus_ref="Syllabus 1.2.1, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Mitochondria and chloroplasts are semi-autonomous organelles believed to have originated from free-living prokaryotic ancestors.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q9 [Past Paper 9700/21/M/J/23/Q2] - Visual Fig 1.7
    questions.append(Question(
        number=9,
        title="9700/21/M/J/23/Q2 Mitochondria vs Chloroplasts: Endosymbiotic Theory",
        syllabus_ref="Syllabus 1.2.1, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Fig. 1.7 shows a transmission electron micrograph schematic of a plant chloroplast.",
        figure_path=os.path.join(DIAG_DIR, "fig1_7_chloroplast_tem.png"),
        figure_caption="Fig. 1.7: Transmission electron micrograph schematic of a chloroplast.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
    (
        '''    # Q18 [Past Paper 9700/21/M/J/22/Q1]
    questions.append(Question(
        number=18,
        title="9700/21/M/J/22/Q1 The Golgi Body & Secretory Pathway Kinetics",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="The Golgi apparatus is a polarized organelle that processes, sorts, and packages macromolecular cargo.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q18 [Past Paper 9700/21/M/J/22/Q1] - Visual Fig 1.9
    questions.append(Question(
        number=18,
        title="9700/21/M/J/22/Q1 The Golgi Body & Secretory Pathway Kinetics",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Fig. 1.9 illustrates the functional polarity of the Golgi apparatus and vesicle trafficking towards the cell surface membrane.",
        figure_path=os.path.join(DIAG_DIR, "fig1_9_golgi_secretory.png"),
        figure_caption="Fig. 1.9: Diagram of Golgi apparatus polarity and vesicular transport to plasma membrane.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
    (
        '''    # Q19 [Past Paper 9700/23/O/N/21/Q1]
    questions.append(Question(
        number=19,
        title="9700/23/O/N/21/Q1 Epithelial Microvilli & Surface Area Adaptations",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Epithelial cells lining the mammalian small intestine (ileum) and proximal convoluted tubules of the kidney have specialized apical surfaces.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",''',
        '''    # Q19 [Past Paper 9700/23/O/N/21/Q1] - Visual Fig 1.11
    questions.append(Question(
        number=19,
        title="9700/23/O/N/21/Q1 Epithelial Microvilli & Surface Area Adaptations",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Fig. 1.11 is a diagram showing the ultrastructure of microvilli on the apical surface of an intestinal epithelial cell.",
        figure_path=os.path.join(DIAG_DIR, "fig1_11_microvilli_epithelium.png"),
        figure_caption="Fig. 1.11: Fine structure of the intestinal brush border showing microvilli and cytoskeleton.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",'''
    ),
]

for old_s, new_s in replacements:
    if old_s in text:
        text = text.replace(old_s, new_s)
        print("Replaced a block successfully.")
    else:
        print("Warning: block not found in text.")

with open(data_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated topic1_cell_structure_data.py successfully.")
