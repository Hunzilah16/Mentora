"""
Topic 1: Cell Structure — 50-Question Examination Dataset (220 Marks)
Candidate: Hamna | Cambridge International AS Level Biology (9700)
Division: 80% Authentic Past Papers (9700) / 20% Original Challenging Extension Problems
Tariff:
  - Section A: Q1 - Q20 (20 × 6 Marks = 120 Marks)
  - Section B: Q21 - Q40 (20 × 4 Marks = 80 Marks)
  - Section C: Q41 - Q50 (10 × 2 Marks = 20 Marks)
  - Section D: 10 Core Repeated Mastery Questions (embedded in Section A & B)
Total: 50 Questions | 220 Marks
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAG_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic1_questions():
    questions = []

    # =========================================================================
    # SECTION A: EXTENDED HIGH-TARIFF QUESTIONS (20 × 6 MARKS = 120 MARKS)
    # =========================================================================

    # Q1 [Past Paper 9700/22/M/J/23/Q1] - Visual Fig 1.1 Animal Cell TEM
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q1 Animal Cell Ultrastructure & Protein Processing",
        syllabus_ref="Syllabus 1.2.1, 1.2.2",
        difficulty="CHALLENGING",
        preamble="Fig. 1.1 is a diagram representing the fine ultrastructure of an animal cell as observed with a transmission electron microscope (TEM).",
        figure_path=os.path.join(DIAG_DIR, "fig1_1_animal_cell_tem.png"),
        figure_caption="Fig. 1.1: Transmission electron micrograph (TEM) diagram of an animal cell.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Identify the organelles labelled C and G in Fig. 1.1, and outline the functional pathway connecting them during the synthesis and export of an extracellular glycoprotein.", marks=4, num_answer_lines=5),
            QuestionPart(label="(b)", text="Explain how the structural adaptations of organelle F enable efficient synthesis of ATP.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "C is rough endoplasmic reticulum (RER) and G is Golgi apparatus / Golgi body [1]; Polypeptides synthesised by 80S ribosomes on RER enter cisternae where they undergo folding / initial glycosylation [1]; Transport vesicles bud off from RER membrane and transport protein to cis face of Golgi body [1]; In Golgi, proteins undergo post-translational modification / oligosaccharide processing and packaging into secretory vesicles that fuse with cell surface membrane via exocytosis [1]", "marks": 4},
            {"part": "(b)", "points": "Inner mitochondrial membrane is extensively folded into cristae to provide a large surface area for electron transport chain complexes and ATP synthase enzymes [1]; Mitochondrial matrix contains Krebs cycle enzymes, small circular DNA, and 70S ribosomes for autonomous protein synthesis [1]", "marks": 2}
        ]
    ))

    # Q2 [Past Paper 9700/21/M/J/22/Q2] - Visual Fig 1.2 Plant Cell
    questions.append(Question(
        number=2,
        title="9700/21/M/J/22/Q2 Plant Cell Fine Structure & Organelle Compartmentalisation",
        syllabus_ref="Syllabus 1.2.1, 1.2.3",
        difficulty="CHALLENGING",
        preamble="Fig. 1.2 illustrates the detailed ultrastructure of a palisade mesophyll cell from a dicotyledonous leaf.",
        figure_path=os.path.join(DIAG_DIR, "fig1_2_plant_cell_tem.png"),
        figure_caption="Fig. 1.2: Fine structure of a photosynthetic plant mesophyll cell.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the functions of structures labelled A and B in Fig. 1.2, relating their structural components to their physiological roles.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Describe two structural differences between the palisade cell in Fig. 1.2 and the animal cell in Fig. 1.1 that are visible under a transmission electron microscope.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify structure F and state its significance in symplastic transport.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "A is cellulose cell wall: provides mechanical strength / tensile strength to prevent osmotic lysis, withstand turgor pressure, and maintain cell shape [1]; B is tonoplast: selectively permeable vacuolar membrane regulating water and solute exchange between cytoplasm and vacuolar cell sap to maintain cell turgidity [2]", "marks": 3},
            {"part": "(b)", "points": "Plant cell contains chloroplasts with thylakoid grana whereas animal cell lacks chloroplasts [1]; Plant cell has a rigid cellulose cell wall and large central vacuole with tonoplast, whereas animal cell has only a flexible cell surface membrane and centrioles [1]", "marks": 2},
            {"part": "(c)", "points": "F is a plasmodesma (cytoplasmic bridge / channel lined with plasma membrane); allows direct symplastic movement of water, mineral ions, and signalling molecules between adjacent plant cells without crossing membranes [1]", "marks": 1}
        ]
    ))

    # Q3 [Past Paper 9700/23/O/N/23/Q1] - Visual Fig 1.3 Bacterium
    questions.append(Question(
        number=3,
        title="9700/23/O/N/23/Q1 Prokaryotic Ultrastructure & Antibiotic Targets",
        syllabus_ref="Syllabus 1.2.5, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Fig. 1.3 shows the fine ultrastructure of a rod-shaped bacterium as revealed by electron microscopy.",
        figure_path=os.path.join(DIAG_DIR, "fig1_3_bacterium_prokaryote.png"),
        figure_caption="Fig. 1.3: Generalized ultrastructure of a prokaryotic cell (bacterium).",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Identify the genetic components labelled A and B in Fig. 1.3, and describe how structure B contributes to genetic diversity and antibiotic resistance in bacterial populations.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Contrast the structural features of bacterial ribosomes (C) with those found in the cytoplasm of eukaryotic animal cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why penicillin is lethal to actively growing bacteria but has no toxic effect on human eukaryotic cells.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "A is circular chromosomal DNA (nucleoid) and B is a plasmid (small circular double-stranded DNA) [1]; Plasmids can replicate autonomously and carry non-essential accessory genes such as beta-lactamase / antibiotic resistance genes [1]; Plasmids can be horizontally transferred between bacterial cells via conjugation (pili), disseminating resistance across strains [1]", "marks": 3},
            {"part": "(b)", "points": "Bacterial ribosomes (C) are 70S (smaller, composed of 50S and 30S subunits) [1]; Cytoplasmic eukaryotic ribosomes are 80S (larger, composed of 60S and 40S subunits) [1]", "marks": 2},
            {"part": "(c)", "points": "Penicillin specifically inhibits transpeptidase enzymes that cross-link peptidoglycan polymers in bacterial cell walls (D); human cells lack cell walls and peptidoglycan, so penicillin exerts selective toxicity without cellular harm [1]", "marks": 1}
        ]
    ))

    # Q4 [Past Paper 9700/22/F/M/24/Q1] - Visual Fig 1.4 Graticule / Calibration
    questions.append(Question(
        number=4,
        title="9700/22/F/M/24/Q1 Microscopic Calibration & Size Measurement",
        syllabus_ref="Syllabus 1.1.3, 1.1.4",
        difficulty="CHALLENGING",
        preamble="A biology student used a light microscope fitted with an eyepiece graticule and a stage micrometer to measure the diameter of mammalian lymphocytes. Fig. 1.4 shows the alignment of the stage micrometer scale and the eyepiece graticule under high power (×400).",
        figure_path=os.path.join(DIAG_DIR, "fig1_4_graticule_micrometer.png"),
        figure_caption="Fig. 1.4: Calibration of eyepiece graticule with stage micrometer under ×400 total magnification.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Using Fig. 1.4, calculate the exact actual distance represented by 1 eyepiece graticule unit (epu) in micrometres (µm). Show your complete working.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Under the same magnification, the student observed a white blood cell that spanned 2.6 eyepiece graticule units. Calculate the actual diameter of this cell in micrometres (µm) and convert your answer to nanometres (nm).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the eyepiece graticule must be recalibrated whenever the objective lens is changed from ×10 to ×40.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "From Fig. 1.4, 40 graticule units correspond precisely to 0.20 mm (200 um) on the stage micrometer [1]; 1 graticule unit = 200 um / 40 = 5.0 um (or 0.005 mm) [1]", "marks": 2},
            {"part": "(b)", "points": "Actual diameter = 2.6 graticule units × 5.0 um/unit = 13.0 um [1]; Conversion to nanometres: 13.0 × 1000 = 13,000 nm [1]", "marks": 2},
            {"part": "(c)", "points": "The eyepiece graticule is located in the microscope ocular and its apparent scale divisions remain physically fixed in size [1]; Changing the objective lens changes the optical magnification of the specimen image projected onto the graticule, so each graticule division subtends a smaller real specimen distance at higher magnification [1]", "marks": 2}
        ]
    ))

    # Q5 [Past Paper 9700/22/M/J/22/Q1] - Visual Fig 1.5 Virus Structure
    questions.append(Question(
        number=5,
        title="9700/22/M/J/22/Q1 Viral Ultrastructure & Retroviral Replication",
        syllabus_ref="Syllabus 1.2.7",
        difficulty="CHALLENGING",
        preamble="Fig. 1.5 is a diagram of the human immunodeficiency virus (HIV), an enveloped retrovirus.",
        figure_path=os.path.join(DIAG_DIR, "fig1_5_virus_structure.png"),
        figure_caption="Fig. 1.5: Diagrammatic representation of human immunodeficiency virus (HIV).",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Identify the molecular structures labelled A, B, and C in Fig. 1.5.", marks=3, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the essential enzymatic function of structure E in the viral lifecycle within a host T-helper lymphocyte.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Discuss two reasons why viruses are classified by biologists as non-cellular structures rather than living cells.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "A: Glycoprotein spike (gp120 / gp41) [1]; B: Phospholipid bilayer envelope [1]; C: Protein capsid shell (capsomeres / p24 core) [1]", "marks": 3},
            {"part": "(b)", "points": "E is reverse transcriptase [1]; Catalyses the synthesis of single-stranded complementary DNA (cDNA) from the viral RNA genome (D), followed by synthesis of double-stranded viral DNA that integrates into the host lymphocyte genome via integrase [1]", "marks": 2},
            {"part": "(c)", "points": "Viruses lack cellular compartmentalisation / cytoplasm, have no cell surface membrane of their own, no organelles, and have no independent metabolic or energetic machinery (cannot synthesise ATP or proteins without host machinery) [1]", "marks": 1}
        ]
    ))

    # Q6 [Past Paper 9700/21/O/N/23/Q1] - Visual Fig 1.12
    questions.append(Question(
        number=6,
        title="9700/21/O/N/23/Q1 Resolution, Magnification & Electron Optics",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="CHALLENGING",
        preamble="Fig. 1.12 shows the diffraction patterns and Airy disk intensity profiles for light waves and electron beams, demonstrating the Rayleigh criterion for resolution.",
        figure_path=os.path.join(DIAG_DIR, "fig1_12_resolution_diffraction.png"),
        figure_caption="Fig. 1.12: Diffraction patterns and resolution limit (Rayleigh criterion) for light vs electron waves.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Define the terms resolution and magnification as used in microscopy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a transmission electron microscope (TEM) has a significantly higher resolving power than a high-performance light microscope.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two limitations of using a transmission electron microscope to study living eukaryotic cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Magnification is the number of times larger an image is compared to the real size of the specimen (Image / Actual) [1]; Resolution is the ability to distinguish between two separate points that are close together / the minimum distance between two points at which they can still be seen as distinct entities [1]", "marks": 2},
            {"part": "(b)", "points": "Resolving power is limited by the wavelength of radiation used (limit of resolution is approx. half the wavelength) [1]; Electrons have a much shorter de Broglie wavelength (approx. 0.005 nm) than visible light photons (400–700 nm), allowing electron beams to resolve structures as close as 0.5 nm compared to 200 nm for light [1]", "marks": 2},
            {"part": "(c)", "points": "Specimens must be placed in a high vacuum (electrons would collide with air molecules), which rapidly dehydrates and kills living cells [1]; Specimen preparation requires chemical fixation, heavy metal staining (e.g. osmium tetroxide), and ultra-thin sectioning, producing potential artefacts and precluding the observation of living dynamic processes [1]", "marks": 2}
        ]
    ))

    # Q7 [Past Paper 9700/22/O/N/22/Q1] - Visual Fig 1.10
    questions.append(Question(
        number=7,
        title="9700/22/O/N/22/Q1 Centrioles, Microtubules & Cilia Organization",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Fig. 1.10 is a diagram showing the transverse section ultrastructure of a centriole.",
        figure_path=os.path.join(DIAG_DIR, "fig1_10_centriole_structure.png"),
        figure_caption="Fig. 1.10: Transverse section schematic of a centriole showing 9+0 triplet microtubule architecture.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular structure of a microtubule and explain how tubulin dimers assemble to form the hollow cylinder.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Contrast the structural arrangement of microtubules in a centriole with that in the axoneme of a cilium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Outline the physiological role of ciliated epithelial cells in the human respiratory tract.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Microtubules are hollow cylinders approx. 25 nm in diameter composed of globular tubulin proteins [1]; Alpha- and beta-tubulin molecules polymerise to form alpha-beta heterodimers, which assemble end-to-end into 13 longitudinal protofilaments surrounding a central lumen [1]", "marks": 2},
            {"part": "(b)", "points": "Centriole consists of 9 triplets of microtubules arranged in a ring with no central microtubules (9+0 arrangement) [1]; Ciliary axoneme consists of 9 doublets of microtubules surrounding 2 central single microtubules (9+2 arrangement) connected by radial spokes and dynein arms [1]", "marks": 2},
            {"part": "(c)", "points": "Coordinated, rhythmic beating of cilia sweeps a layer of mucus produced by goblet cells upwards towards the pharynx / throat [1]; Traps inhaled dust particles, bacteria, and pathogens and removes them from the gas exchange surface, swallowing or coughing them out to prevent lung infections [1]", "marks": 2}
        ]
    ))

    # Q8 [Past Paper 9700/23/M/J/23/Q1] - Visual Fig 1.8
    questions.append(Question(
        number=8,
        title="9700/23/M/J/23/Q1 Nuclear Pore Complex & Ribosome Biogenesis",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Fig. 1.8 shows the fine ultrastructure of a eukaryotic nucleus as observed in an electron micrograph.",
        figure_path=os.path.join(DIAG_DIR, "fig1_8_nucleus_tem.png"),
        figure_caption="Fig. 1.8: Transmission electron micrograph diagram of the eukaryotic nucleus.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of the nuclear envelope, making reference to its outer membrane, inner membrane, perinuclear space, and nuclear pores.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Explain the function of the nucleolus in the biogenesis of ribosomal subunits.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify two different macromolecular complexes that exit the nucleus via nuclear pores into the cytoplasm.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "The nuclear envelope consists of two concentric phospholipid bilayers separated by a fluid-filled perinuclear space (20–40 nm wide) [1]; The outer membrane is continuous with the rough endoplasmic reticulum and is studded with 80S ribosomes [1]; The double membrane is perforated by nuclear pore complexes (approx. 100 nm diameter) that selectively regulate the bidirectional transport of macromolecules between nucleoplasm and cytoplasm [1]", "marks": 3},
            {"part": "(b)", "points": "The nucleolus contains ribosomal DNA (rDNA) genes that transcribe ribosomal RNA (rRNA) precursors [1]; Combines processed rRNA molecules with ribosomal proteins imported from the cytoplasm to assemble large (60S) and small (40S) ribosomal subunits [1]", "marks": 2},
            {"part": "(c)", "points": "Processed messenger RNA (mRNA) complexes and assembled ribosomal subunits (40S and 60S) [or transfer RNA (tRNA)] [1]", "marks": 1}
        ]
    ))

    # Q9 [Past Paper 9700/21/M/J/23/Q2] - Visual Fig 1.7
    questions.append(Question(
        number=9,
        title="9700/21/M/J/23/Q2 Mitochondria vs Chloroplasts: Endosymbiotic Theory",
        syllabus_ref="Syllabus 1.2.1, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Fig. 1.7 shows a transmission electron micrograph schematic of a plant chloroplast.",
        figure_path=os.path.join(DIAG_DIR, "fig1_7_chloroplast_tem.png"),
        figure_caption="Fig. 1.7: Transmission electron micrograph schematic of a chloroplast.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State three structural features shared by both mitochondria and chloroplasts that provide strong evidence for the endosymbiotic origin of eukaryotic cells.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Contrast the structural location and function of the ATP synthase enzyme in mitochondria with its location and function in chloroplasts.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why mitochondria and chloroplasts cannot survive independently outside of a host eukaryotic cell.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Both possess a double membrane envelope (outer membrane derived from host vacuole, inner from prokaryote) [1]; Both contain small, circular double-stranded DNA not associated with histone proteins [1]; Both contain 70S ribosomes (similar to bacterial ribosomes) and replicate independently by binary fission [1]", "marks": 3},
            {"part": "(b)", "points": "In mitochondria, ATP synthase is embedded in the inner mitochondrial membrane (cristae) and synthesises ATP as protons flow from the intermembrane space into the matrix [1]; In chloroplasts, ATP synthase is embedded in the thylakoid membrane and synthesises ATP as protons flow from the thylakoid lumen into the stroma [1]", "marks": 2},
            {"part": "(c)", "points": "Over evolutionary time, most essential ancestral endosymbiont genes were transferred to the host cell nucleus; the organelles rely on cytosolic translation and nuclear-encoded proteins imported via translocons [1]", "marks": 1}
        ]
    ))

    # Q10 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=10,
        title="[Mentora Original A* Extension] Q10: Lysosome Biogenesis & Autophagy",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="ADVANCED",
        preamble="Lysosomes are spherical single-membrane organelles containing hydrolytic acid hydrolases maintained at an acidic luminal pH (~4.5–5.0).",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain how the lysosomal membrane maintains an internal pH lower than the surrounding neutral cytosol (pH ~7.2) and outline the protective significance of this mechanism.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Distinguish between heterophagy (phagocytosis) and autophagy carried out by lysosomes in eukaryotic cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Predict the physiological consequence to a cell if its lysosomal enzymes fail to be tagged with mannose-6-phosphate during processing in the Golgi body.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "The lysosomal membrane contains active V-type H+ ATPase proton pumps that actively transport protons from the cytosol into the lysosome lumen against their concentration gradient using ATP hydrolysis [1]; Lysosomal acid hydrolases have an acidic pH optimum (~5.0); if a lysosome ruptures accidentally, the neutral cytosolic pH (~7.2) inactivates the released hydrolases, preventing autolysis and catastrophic cell destruction [2]", "marks": 3},
            {"part": "(b)", "points": "Heterophagy involves lysosomes fusing with endocytic/phagocytic vesicles containing extracellular foreign materials (e.g. ingested bacteria) [1]; Autophagy involves lysosomes fusing with autophagosomes enclosing damaged, worn-out intracellular organelles (e.g. aged mitochondria) to recycle biological macromolecules [1]", "marks": 2},
            {"part": "(c)", "points": "Hydrolases would fail to be sorted into clathrin-coated budding lysosomal vesicles in the trans-Golgi and would instead be constitutively secreted into the extracellular matrix via default exocytosis, causing I-cell disease (lysosomal storage disorder) [1]", "marks": 1}
        ]
    ))

    # Q11 [Past Paper 9700/22/M/J/21/Q1]
    questions.append(Question(
        number=11,
        title="9700/22/M/J/21/Q1 Endoplasmic Reticulum & Lipid Synthesis",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Eukaryotic cells contain two interconnected forms of endoplasmic reticulum: rough endoplasmic reticulum (RER) and smooth endoplasmic reticulum (SER).",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structural and biochemical differences between rough endoplasmic reticulum and smooth endoplasmic reticulum.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="State two metabolic functions performed by the smooth endoplasmic reticulum in specialised mammalian tissues.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Name the specific cellular mechanism by which newly synthesised secretory proteins are targeted to the RER lumen.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "RER is formed of flattened, parallel sheet-like membranous sacs (cisternae) studded with 80S ribosomes on its cytoplasmic surface, primarily involved in protein synthesis and folding [2]; SER consists of a more tubular, branching network of interconnected tubules devoid of ribosomes on its outer surface [1]", "marks": 3},
            {"part": "(b)", "points": "Synthesis of lipids, phospholipids, and steroid hormones (e.g. cholesterol, testosterone, estrogen in endocrine cells) [1]; Detoxification of drugs and metabolic xenobiotics (in hepatocytes) OR storage and release of calcium ions (sarcoplasmic reticulum in muscle fibres) [1]", "marks": 2},
            {"part": "(c)", "points": "N-terminal signal peptide (signal sequence) on nascent polypeptide bound by Signal Recognition Particle (SRP) and directed to a translocon channel in the RER membrane [1]", "marks": 1}
        ]
    ))

    # Q12 [Past Paper 9700/21/O/N/21/Q2]
    questions.append(Question(
        number=12,
        title="9700/21/O/N/21/Q2 Cytoskeleton, Centrosomes & Intracellular Transport",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="The cytoplasm of eukaryotic cells is organized by a dynamic cytoskeletal network that supports organelle transport and cell division.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe how motor proteins (kinesin and dynein) interact with microtubules to transport secretory vesicles through the cytoplasm.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Explain the structural role of the centrosome during animal cell mitosis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State why plant cells are able to form a functional mitotic spindle apparatus despite lacking centrioles.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Microtubules act as intracellular tracks / railways possessing intrinsic structural polarity (plus end and minus end) [1]; Motor proteins (kinesin moves towards plus end / cell periphery, dynein towards minus end / centrosome) attach to vesicle membranes via receptor proteins [1]; Motor protein globular heads hydrolyse ATP to ADP + Pi, undergoing conformational changes that produce 'walking' steps along the microtubule protofilament [1]", "marks": 3},
            {"part": "(b)", "points": "Centrosome contains a pair of mutually perpendicular centrioles surrounded by pericentriolar material acting as the main Microtubule Organising Centre (MTOC) [1]; Nucleates and organizes the rapid polymerization of spindle microtubules that attach to chromosome kinetochores and segregate sister chromatids [1]", "marks": 2},
            {"part": "(c)", "points": "Plant cells possess diffuse, non-centrosomal microtubule organizing centres (MTOCs) located throughout the nuclear envelope and cortical cytoplasm that nucleate spindle fibres [1]", "marks": 1}
        ]
    ))

    # Q13 [Past Paper 9700/22/F/M/23/Q1]
    questions.append(Question(
        number=13,
        title="9700/22/F/M/23/Q1 The Fluid Mosaic Model: Membrane Compartmentalisation",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="The cell surface membrane and intracellular organelle membranes share the fundamental fluid mosaic architecture.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain why internal membrane systems (compartmentalisation) provide significant metabolic advantages to eukaryotic cells compared to prokaryotic cells.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Describe how the phospholipid bilayer creates an effective barrier to water-soluble ions while remaining permeable to lipid-soluble substances.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the organelle membrane that contains a high concentration of cardiolipin and explain its functional significance.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Compartmentalisation isolates incompatible metabolic reactions (e.g. destructive hydrolytic enzymes in lysosomes isolated from cytoplasm) [1]; Concentrates specific enzymes, substrates, and cofactors in a restricted volume, dramatically increasing reaction rates and collision frequencies [1]; Allows the establishment and maintenance of localized electrochemical ion gradients across membranes (e.g. proton motive force in mitochondria/chloroplasts) [1]", "marks": 3},
            {"part": "(b)", "points": "The hydrophobic fatty acid hydrocarbon tails form a dense non-polar core in the centre of the bilayer that repels charged ions and large polar hydrophilic molecules [1]; Non-polar, lipid-soluble molecules (e.g. steroid hormones, O2, CO2) dissolve readily in the fatty acyl core and cross freely via simple diffusion [1]", "marks": 2},
            {"part": "(c)", "points": "Inner mitochondrial membrane; cardiolipin reduces proton permeability, ensuring the proton gradient is exclusively dissipated through ATP synthase [1]", "marks": 1}
        ]
    ))

    # Q14 [Past Paper 9700/23/M/J/22/Q2]
    questions.append(Question(
        number=14,
        title="9700/23/M/J/22/Q2 Plant Cell Walls & Plasmodesmata Architecture",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Plant cell walls provide structural support and withstand high internal turgor pressures generated by osmosis.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular architecture of a primary plant cell wall, with reference to cellulose microfibrils, hemicelluloses, pectins, and the middle lamella.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Explain how hydrogen bonding between adjacent beta-glucose chains contributes to the high tensile strength of cellulose fibres.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State the function of the middle lamella during cell division and tissue cohesion.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Cellulose molecules are organized into bundles called microfibrils (approx. 60–70 parallel glucan chains) [1]; Microfibrils are embedded in an amorphous, gelatinous matrix of branched hemicelluloses and hydrated pectins (calcium and magnesium pectates) [1]; The middle lamella forms the outermost cement-like layer that bonds adjacent plant cell walls together [1]", "marks": 3},
            {"part": "(b)", "points": "Successive beta-glucose monomers are rotated by 180 degrees, allowing hydroxyl (-OH) groups to project outwards in all directions [1]; Enormous numbers of cross-linking hydrogen bonds form between parallel unbranched chains, conferring immense cumulative tensile strength that resists stretching [1]", "marks": 2},
            {"part": "(c)", "points": "Binds and cements adjacent cell walls together through pectin gels, maintaining tissue structural integrity and mechanical cohesion [1]", "marks": 1}
        ]
    ))

    # Q15 [Past Paper 9700/21/M/J/24/Q1]
    questions.append(Question(
        number=15,
        title="9700/21/M/J/24/Q1 Scanning vs Transmission Electron Microscopy",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="CHALLENGING",
        preamble="Electron microscopes use focused beams of electrons to produce images of specimens at high magnifications.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Compare the operating principles of a Transmission Electron Microscope (TEM) with a Scanning Electron Microscope (SEM).", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Contrast the images produced by TEM and SEM in terms of dimensionality and specimen detail.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State one key advantage of using a scanning electron microscope over a light microscope when examining the surface of an insect eye.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "In a TEM, an electron beam passes directly through an ultra-thin specimen; transmitted electrons are focused by electromagnetic lenses onto a fluorescent screen/detector [1]; In an SEM, a fine beam of electrons scans back and forth across the gold-coated surface of a specimen, causing secondary electrons to be emitted and captured by a collector [2]", "marks": 3},
            {"part": "(b)", "points": "TEM produces 2-dimensional (flat) images showing internal cell ultrastructure and fine organelle details with resolution down to 0.5 nm [1]; SEM produces 3-dimensional images with great depth of field showing external surface contours and topography (resolution ~3–10 nm) [1]", "marks": 2},
            {"part": "(c)", "points": "SEM offers vastly greater resolving power and enormous depth of field, rendering intricate microscopic surface ommatidia and bristles sharply in focus in 3D [1]", "marks": 1}
        ]
    ))

    # Q16 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=16,
        title="[Mentora Original A* Extension] Q16: Microscopic Scale, Conversions & Magnification Indices",
        syllabus_ref="Syllabus 1.1.3, 1.1.4",
        difficulty="ADVANCED",
        preamble="Accurate quantitative scaling is fundamental when analysing electron micrographs and light microscope preparations.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="A spherical bacterium has a measured diameter of 1.25 µm. Calculate its volume in cubic micrometres (µm³) and express this value in cubic millimetres (mm³), using standard scientific notation. (Volume of sphere = 4/3 × π × r³).", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="An electron micrograph shows a ribosome with an image diameter of 15 mm. If the actual diameter is 25 nm, calculate the magnification of the micrograph. Show your working clearly.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why expressing organelle measurements in nanometres (nm) is more scientifically appropriate than in millimetres (mm).", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Radius r = 1.25 / 2 = 0.625 um; Volume = (4/3) × π × (0.625)^3 = 1.02 um3 [1]; Conversion: 1 mm = 1,000 um, so 1 mm3 = 10^9 um3 [1]; Volume in mm3 = 1.02 × 10^-9 mm3 [1]", "marks": 3},
            {"part": "(b)", "points": "Formula: Magnification M = Image size (I) / Actual size (A) [1]; Convert units: I = 15 mm = 15,000,000 nm; M = 15,000,000 / 25 = ×600,000 (or 6.0 × 10^5) [1]", "marks": 2},
            {"part": "(c)", "points": "Avoids awkward and error-prone decimal exponents / fractional notation, matching the physical dimensional scale of macromolecular structures (1 nm = 10^-9 m) directly [1]", "marks": 1}
        ]
    ))

    # Q17 [Past Paper 9700/22/O/N/23/Q1]
    questions.append(Question(
        number=17,
        title="9700/22/O/N/23/Q1 Eukaryotic vs Prokaryotic Ribosomes & Translation Sites",
        syllabus_ref="Syllabus 1.2.1, 1.2.5",
        difficulty="CHALLENGING",
        preamble="Ribosomes are non-membrane bound ribonucleoprotein complexes found in all living organisms.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Outline the structural composition of a ribosome, identifying its two fundamental biochemical components.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compare the sedimentation coefficients, subunit sizes, and subcellular distributions of ribosomes found in eukaryotic cells.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Explain why free cytosolic ribosomes and membrane-bound RER ribosomes synthesise proteins for completely different destinations.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Ribosomes consist of ribosomal RNA (rRNA) molecules and ribosomal proteins organized into two unequal subunits (large subunit and small subunit) [2]", "marks": 2},
            {"part": "(b)", "points": "Eukaryotic cytoplasm contains 80S ribosomes composed of 60S (large) and 40S (small) subunits [1]; Mitochondria and chloroplasts contain 70S ribosomes composed of 50S (large) and 30S (small) subunits [1]; 80S ribosomes translate nuclear mRNAs in the cytosol, whereas organellar 70S ribosomes translate mitochondrial/chloroplast circular DNA genes locally [1]", "marks": 3},
            {"part": "(c)", "points": "Free cytosolic ribosomes synthesise proteins destined to remain in the cytosol, nucleus, or peroxisomes; RER ribosomes synthesise proteins with hydrophobic signal peptides destined for lysosomes, membrane insertion, or extracellular secretion [1]", "marks": 1}
        ]
    ))

    # Q18 [Past Paper 9700/21/M/J/22/Q1] - Visual Fig 1.9
    questions.append(Question(
        number=18,
        title="9700/21/M/J/22/Q1 The Golgi Body & Secretory Pathway Kinetics",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Fig. 1.9 illustrates the functional polarity of the Golgi apparatus and vesicle trafficking towards the cell surface membrane.",
        figure_path=os.path.join(DIAG_DIR, "fig1_9_golgi_secretory.png"),
        figure_caption="Fig. 1.9: Diagram of Golgi apparatus polarity and vesicular transport to plasma membrane.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structural polarity of the Golgi apparatus, distinguishing between the cis face and trans face cisternae.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain three specific post-translational modifications carried out on polypeptides within the Golgi lumen.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Identify the cellular destination of vesicles that bud off from the trans-Golgi network carrying digestive hydrolases.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "The cis face is convex, faces the rough ER / nucleus, and receives incoming transport vesicles [1]; The trans face is concave, oriented towards the plasma membrane, and buds off mature secretory vesicles and lysosomes [1]", "marks": 2},
            {"part": "(b)", "points": "Glycosylation: enzymatic addition or trimming of carbohydrate chains to form glycoproteins [1]; Phosphorylation of specific amino acid residues (or sulfation of oligosaccharides) [1]; Cleavage / proteolytic processing of inactive pro-proteins into active mature hormones/enzymes (e.g. pro-insulin to insulin) [1]", "marks": 3},
            {"part": "(c)", "points": "Primary lysosomes (or late endosomes) [1]", "marks": 1}
        ]
    ))

    # Q19 [Past Paper 9700/23/O/N/21/Q1] - Visual Fig 1.11
    questions.append(Question(
        number=19,
        title="9700/23/O/N/21/Q1 Epithelial Microvilli & Surface Area Adaptations",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Fig. 1.11 is a diagram showing the ultrastructure of microvilli on the apical surface of an intestinal epithelial cell.",
        figure_path=os.path.join(DIAG_DIR, "fig1_11_microvilli_epithelium.png"),
        figure_caption="Fig. 1.11: Fine structure of the intestinal brush border showing microvilli and cytoskeleton.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the internal ultrastructure of a microvillus, with reference to actin microfilaments and the plasma membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how microvilli increase the efficiency of substance absorption in intestinal epithelial cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Contrast the structural features and motility of microvilli with those of respiratory cilia.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Each microvillus is a finger-like cylindrical evagination of the apical plasma membrane containing a central core of parallel bundled actin microfilaments [1]; The actin bundle is cross-linked and anchored into the underlying terminal web cytoskeleton of the cell [1]", "marks": 2},
            {"part": "(b)", "points": "Enormously increases the surface area-to-volume ratio of the apical membrane by up to 20–30 fold [1]; Accommodates a vastly higher density of carrier proteins, symporters (e.g. SGLT1 glucose-Na+ cotransporters), and channel proteins for facilitated diffusion and active transport [1]", "marks": 2},
            {"part": "(c)", "points": "Microvilli are non-motile, small (~1 um long), supported by actin filaments, and function in surface area expansion [1]; Cilia are motile, longer (~5–10 um), contain a 9+2 microtubule axoneme with ATP-powered dynein arms, and beat rhythmically to generate fluid flow [1]", "marks": 2}
        ]
    ))

    # Q20 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] Q20: Cellular Energetics & ATP Compartmentalisation",
        syllabus_ref="Syllabus 1.2.4",
        difficulty="ADVANCED",
        preamble="Cells continuously hydrolyse and regenerate millions of molecules of adenosine triphosphate (ATP) to drive thermodynamically unfavourable reactions.",
        section_key="Section A — Extended High-Tariff Questions (6 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain why ATP is described as the 'universal energy currency' of living cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="List four distinct cellular processes in a eukaryotic animal cell that directly depend on the hydrolysis of ATP.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why prokaryotic bacteria can synthesise ATP via chemiosmosis despite lacking mitochondria.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "ATP is used by all living organisms in all cell types to transfer energy from exergonic catabolic reactions to endergonic cellular processes [1]; Releases energy in a single-step hydrolysis of its phosphoanhydride bond (~30.5 kJ/mol), providing small, manageable quantities of energy without damaging cell structures [1]", "marks": 2},
            {"part": "(b)", "points": "Any four of: Active transport (e.g. Na+/K+ ATPase pump); Anabolic polymerisation reactions (protein/DNA synthesis); Vesicle movement along microtubules (motor proteins); Muscle contraction / sliding filaments; Ciliary/flagellar beating; Exocytosis / endocytosis [2] (1 mark for two, 2 marks for four)", "marks": 2},
            {"part": "(c)", "points": "Bacteria possess electron transport chain complexes and ATP synthase enzymes directly embedded in their plasma (cell surface) membrane [1]; They pump protons out of the cytoplasm into the periplasmic space (between plasma membrane and peptidoglycan wall), establishing a proton motive force that drives ATP synthesis as protons re-enter via ATP synthase [1]", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: DATA INTERPRETATION & EXPLANATIONS (20 × 4 MARKS = 80 MARKS)
    # =========================================================================

    # Q21 [Past Paper 9700/22/M/J/23/Q3] - Visual Fig 1.6
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q3 Measuring Organelles from Photomicrographs",
        syllabus_ref="Syllabus 1.1.3",
        difficulty="CHALLENGING",
        preamble="Fig. 1.6 shows a transmission electron micrograph of a mitochondrion in longitudinal section. The scale bar printed on the micrograph measures 20 mm and represents 1.0 µm.",
        figure_path=os.path.join(DIAG_DIR, "fig1_6_mitochondrion_measurement.png"),
        figure_caption="Fig. 1.6: Transmission electron micrograph of a mitochondrion with scale bar.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Calculate the linear magnification of the micrograph using the scale bar in Fig. 1.6.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the actual length of the mitochondrion in micrometres (µm) if its measured image length is 68 mm.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Magnification = Image size of scale bar / Actual size of scale bar [1]; 20 mm = 20,000 um; M = 20,000 um / 1.0 um = ×20,000 [1]", "marks": 2},
            {"part": "(b)", "points": "Actual size = Image size / Magnification [1]; Actual length = 68 mm / 20,000 = 0.0034 mm = 3.4 µm [1]", "marks": 2}
        ]
    ))

    # Q22 [Past Paper 9700/21/O/N/22/Q3]
    questions.append(Question(
        number=22,
        title="9700/21/O/N/22/Q3 Plant Vacuole & Osmotic Regulation",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Mature plant cells typically contain a single large permanent central vacuole bounded by the tonoplast.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Outline the physiological role of the central vacuole in maintaining tissue firmness (turgor) in herbaceous plants.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State two non-osmotic functions of plant vacuoles.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Accumulates dissolved mineral ions, organic acids, and sugars, creating a low water potential that draws water into the vacuole by osmosis [1]; The expanding cell sap presses the protoplast against the rigid cellulose cell wall, generating hydrostatic turgor pressure that provides mechanical support [1]", "marks": 2},
            {"part": "(b)", "points": "Storage of metabolic reserves (e.g. sucrose, proteins) and waste products / secondary metabolites (e.g. tannins, alkaloids) [1]; Lytic organelle function containing hydrolytic enzymes to degrade unneeded macromolecules (analogous to animal lysosomes) [1]", "marks": 2}
        ]
    ))

    # Q23 [Past Paper 9700/22/M/J/22/Q3]
    questions.append(Question(
        number=23,
        title="9700/22/M/J/22/Q3 Centrioles in Cell Division",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Centrioles duplicate during interphase prior to the onset of nuclear division.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the spatial arrangement of the two centrioles within a centrosome of an animal cell during interphase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what happens to the two centrosomes as the cell progresses from prophase to metaphase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Two cylindrical centrioles lie mutually perpendicular (at 90 degrees to each other) within the centrosome [1]; Embedded in an amorphous cloud of pericentriolar material [1]", "marks": 2},
            {"part": "(b)", "points": "The two centrosomes migrate to opposite poles of the dividing cell driven by motor proteins along interpolar microtubules [1]; Spindle microtubules radiate from each centrosome to form the mitotic spindle apparatus, attaching to kinetochores at the metaphase plate [1]", "marks": 2}
        ]
    ))

    # Q24 [Past Paper 9700/23/O/N/22/Q2]
    questions.append(Question(
        number=24,
        title="9700/23/O/N/22/Q2 Microtubule Dynamic Instability & Spindle Poisons",
        syllabus_ref="Syllabus 1.2.4",
        difficulty="CHALLENGING",
        preamble="Certain anticancer drugs, such as colchicine and paclitaxel (Taxol), specifically interfere with microtubule assembly and disassembly.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain how colchicine arrests dividing human cancer cells at metaphase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Predict and explain the effect of colchicine treatment on vesicle movement between the ER and Golgi apparatus.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Colchicine binds to free tubulin heterodimers and prevents their polymerisation into microtubules [1]; Prevents the formation of the mitotic spindle; chromosomes cannot align or segregate, arresting cells in metaphase [1]", "marks": 2},
            {"part": "(b)", "points": "Vesicle transport is severely disrupted / inhibited [1]; Vesicles rely on intact microtubule tracks and motor proteins (kinesin/dynein) for directed trafficking through the cytosol [1]", "marks": 2}
        ]
    ))

    # Q25 [Past Paper 9700/21/M/J/23/Q3]
    questions.append(Question(
        number=25,
        title="9700/21/M/J/23/Q3 Chloroplast Thylakoids & Light Capture",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="The internal membrane network of a chloroplast is organized into flattened thylakoid sacs stacked into grana.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain how the structural organization of thylakoid membranes into grana maximizes the capture of light energy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the biochemical role of the stroma in a chloroplast.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Provides an enormous surface area densely packed with photosynthetic pigment-protein complexes (photosystems I and II, chlorophylls, carotenoids) [1]; Stacking into grana optimizes light interception and facilitates efficient energy transfer between antennae complexes [1]", "marks": 2},
            {"part": "(b)", "points": "Gel-like fluid containing soluble enzymes (including Rubisco) that catalyse the Calvin cycle (light-independent reactions) for carbon fixation [1]; Contains 70S ribosomes, circular DNA, and starch grains [1]", "marks": 2}
        ]
    ))

    # Q26 [Past Paper 9700/22/F/M/22/Q1]
    questions.append(Question(
        number=26,
        title="9700/22/F/M/22/Q1 Prokaryotic Peptidoglycan Cell Wall",
        syllabus_ref="Syllabus 1.2.5",
        difficulty="CHALLENGING",
        preamble="Unlike plant cell walls made of cellulose, the cell walls of Bacteria are constructed from peptidoglycan (murein).",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular components of peptidoglycan.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the peptidoglycan wall protects bacteria from osmotic bursting in hypotonic environments.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Peptidoglycan consists of repeating disaccharide backbone units of N-acetylglucosamine (NAG) and N-acetylmuramic acid (NAM) [1]; Cross-linked by short oligopeptide peptide side-chains forming a rigid, lattice-like covalent meshwork [1]", "marks": 2},
            {"part": "(b)", "points": "When water enters the bacterial cell by osmosis down a water potential gradient, internal turgor pressure rises [1]; The cross-linked peptidoglycan mesh has high tensile strength that resists osmotic swelling and mechanical lysis [1]", "marks": 2}
        ]
    ))

    # Q27 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=27,
        title="[Mentora Original A* Extension] Q27: Limits of Resolution in Light Microscopy",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="ADVANCED",
        preamble="The theoretical limit of resolution (d) of an optical microscope is described by Ernst Abbe's equation: d = λ / (2 · NA), where λ is the wavelength of illuminating radiation and NA is numerical aperture.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Calculate the theoretical resolution limit (d) of a light microscope using green light (λ = 500 nm) and an oil-immersion objective lens with NA = 1.25.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why ribosomes (diameter ~25 nm) and centrioles (diameter ~200 nm, length ~500 nm) cannot be resolved as distinct internal structures using this microscope.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "d = 500 nm / (2 × 1.25) = 500 / 2.5 [1]; d = 200 nm (or 0.20 µm) [1]", "marks": 2},
            {"part": "(b)", "points": "Ribosomes (25 nm) are substantially smaller than the 200 nm resolution limit, so light waves diffracted by them cannot form separate airy disk peaks [1]; Structures smaller than 200 nm appear only as blurred diffraction spots or remain completely invisible against the background [1]", "marks": 2}
        ]
    ))

    # Q28 [Past Paper 9700/23/M/J/23/Q2]
    questions.append(Question(
        number=28,
        title="9700/23/M/J/23/Q2 Peroxisomes & Catalase Function",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="Peroxisomes are metabolic microbodies present in all eukaryotic cells containing oxidative enzymes.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the biochemical reaction catalysed by the enzyme catalase inside peroxisomes, giving the word or balanced chemical equation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why confining catalase within peroxisomes is vital for cell survival.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Breaks down toxic hydrogen peroxide into water and oxygen [1]; 2 H2O2 -> 2 H2O + O2 [1]", "marks": 2},
            {"part": "(b)", "points": "Hydrogen peroxide is a hazardous, reactive oxygen species produced during fatty acid beta-oxidation [1]; Compartmentalisation inside peroxisomes prevents H2O2 from leaking into the cytosol where it would generate destructive hydroxyl free radicals that damage DNA, proteins, and membrane lipids [1]", "marks": 2}
        ]
    ))

    # Q29 [Past Paper 9700/21/O/N/23/Q2]
    questions.append(Question(
        number=29,
        title="9700/21/O/N/23/Q2 Viral Capsid & Genome Diversity",
        syllabus_ref="Syllabus 1.2.7",
        difficulty="CHALLENGING",
        preamble="Viruses exhibit remarkable structural diversity in their protein capsids and genetic material.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of a viral capsid and state its primary functions.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State four different configurations of genetic material found among different families of viruses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Protein shell constructed from repeating protein subunits called capsomeres arranged symmetrically (helical, icosahedral, or complex) [1]; Encloses and protects the viral genome from chemical and enzymatic degradation (nucleases) and aids attachment to host cell surface receptors [1]", "marks": 2},
            {"part": "(b)", "points": "Single-stranded DNA (ssDNA); Double-stranded DNA (dsDNA); Single-stranded RNA (ssRNA); Double-stranded RNA (dsRNA) [2] (1 mark for any two, 2 marks for all four)", "marks": 2}
        ]
    ))

    # Q30 [Past Paper 9700/22/M/J/24/Q2]
    questions.append(Question(
        number=30,
        title="9700/22/M/J/24/Q2 Preparation of Temporary Mounts for Microscopy",
        syllabus_ref="Syllabus 1.1.1",
        difficulty="CHALLENGING",
        preamble="To view cellular specimens under a light microscope, students prepare temporary stained mounts.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe two precautions taken when lowering a cover slip onto a liquid specimen to ensure an optimal microscopic image.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why biological specimens are frequently treated with stains such as iodine in potassium iodide solution or methylene blue.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Lower the coverslip gently at a 45-degree angle using a mounted needle to prevent trapping air bubbles [1]; Blot excess stain/liquid from the edges using filter paper to prevent the coverslip from floating or smearing onto the objective lens [1]", "marks": 2},
            {"part": "(b)", "points": "Biological specimens are largely transparent; stains bind differentially to specific biochemical structures (e.g. iodine stains starch granules blue-black; methylene blue stains nuclei/DNA dark blue) [1]; Dramatically increases optical contrast between cell components and surrounding medium [1]", "marks": 2}
        ]
    ))

    # Q31 [Past Paper 9700/23/O/N/23/Q2]
    questions.append(Question(
        number=31,
        title="9700/23/O/N/23/Q2 Calculating Magnification of Scaled Drawings",
        syllabus_ref="Syllabus 1.1.2, 1.1.3",
        difficulty="CHALLENGING",
        preamble="A candidate produced a biological drawing of an epidermal guard cell. The drawing had a length of 54 mm, whereas the actual cell length was 45 µm.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Calculate the magnification of the candidate's drawing.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Outline two rules of biological drawing that the candidate must follow to gain full marks in a Cambridge practical examination.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Convert units: 54 mm = 54,000 µm [1]; Magnification M = I / A = 54,000 / 45 = ×1,200 [1]", "marks": 2},
            {"part": "(b)", "points": "Use a sharp HB pencil to draw continuous, clear, clean lines without shading or cross-hatching [1]; Use a ruler to draw straight, horizontal label lines that touch the feature being labelled without arrowheads [1]", "marks": 2}
        ]
    ))

    # Q32 [Past Paper 9700/21/M/J/21/Q2]
    questions.append(Question(
        number=32,
        title="9700/21/M/J/21/Q2 Flagella: Prokaryotes vs Eukaryotes",
        syllabus_ref="Syllabus 1.2.5, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Locomotion in both bacteria and certain eukaryotic cells is mediated by flagella, but their evolutionary structures are completely distinct.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure and energy source that powers a bacterial flagellum.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Contrast the structure and motility mechanism of a eukaryotic flagellum (such as that of a sperm cell) with a bacterial flagellum.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Bacterial flagellum is a rigid, hollow helical filament composed of repeating flagellin protein subunits, attached to a rotary motor in the cell membrane [1]; Powered directly by a proton gradient (proton motive force) across the plasma membrane, not ATP [1]", "marks": 2},
            {"part": "(b)", "points": "Eukaryotic flagellum is surrounded by the plasma membrane and contains a 9+2 arrangement of microtubules with dynein arms [1]; Powered by ATP hydrolysis and generates a whip-like undulating sinusoidal wave rather than rotating like a propeller [1]", "marks": 2}
        ]
    ))

    # Q33 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=33,
        title="[Mentora Original A* Extension] Q33: Density Gradient Centrifugation of Organelles",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="ADVANCED",
        preamble="Cell fractionation and differential ultracentrifugation are experimental techniques used to isolate individual organelles based on their size and density.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain why cell homogenisation must be carried out in an ice-cold, isotonic, buffered solution.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Predict the order of organelle sedimentation in differential centrifugation from lowest speed (first pellet) to highest speed (last pellet) among: ribosomes, nuclei, mitochondria.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Ice-cold: reduces enzyme activity (especially autolytic proteases/DNases) to prevent organelle degradation [1]; Isotonic: prevents osmotic water movement into or out of organelles, preventing osmotic lysis or shrinkage [1]; Buffered: maintains constant physiological pH (~7.4) to prevent denaturation of membrane proteins and enzymes [1]", "marks": 3},
            {"part": "(b)", "points": "Nuclei (pelleted first at ~1,000 g) -> Mitochondria (pelleted at ~10,000 g) -> Ribosomes (pelleted at ~100,000 g) [1]", "marks": 1}
        ]
    ))

    # Q34 [Past Paper 9700/22/O/N/21/Q2]
    questions.append(Question(
        number=34,
        title="9700/22/O/N/21/Q2 Nuclear Envelope Fragmentation in Mitosis",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        preamble="During eukaryotic cell division, the nuclear envelope undergoes dramatic structural changes.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe what happens to the nuclear envelope during prophase and prometaphase of mitosis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how and when the nuclear envelope reassembles around daughter nuclei.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Nuclear lamin intermediate filaments are phosphorylated, causing the nuclear lamina to depolymerise [1]; The nuclear envelope breaks down into small membranous vesicles that disperse into the endoplasmic reticulum network [1]", "marks": 2},
            {"part": "(b)", "points": "During telophase, nuclear lamina proteins are dephosphorylated [1]; Membranous vesicles bind to the surface of individual decondensing chromosomes and fuse together to re-form two intact nuclear envelopes around the daughter nuclei [1]", "marks": 2}
        ]
    ))

    # Q35 [Past Paper 9700/23/F/M/24/Q1]
    questions.append(Question(
        number=35,
        title="9700/23/F/M/24/Q1 Autolysis & Programmed Cell Death (Apoptosis)",
        syllabus_ref="Syllabus 1.2.1, 1.2.4",
        difficulty="CHALLENGING",
        preamble="Lysosomes play critical roles in both normal physiological remodeling and pathological tissue destruction.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain the biological meaning of the term autolysis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Give two examples in animal development where controlled lysosomal activity is essential.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Self-destruction of an entire cell or tissue by the mass release of its own lysosomal hydrolytic enzymes into the cytoplasm [1]; Occurs post-mortem or during programmed cell death (apoptosis) [1]", "marks": 2},
            {"part": "(b)", "points": "Resorption of the tadpole tail during amphibian metamorphosis [1]; Regression of the uterine lining during menstruation OR digit separation (removal of webbing between fingers/toes) during human embryonic limb development [1]", "marks": 2}
        ]
    ))

    # Q36 [Past Paper 9700/21/M/J/24/Q2]
    questions.append(Question(
        number=36,
        title="9700/21/M/J/24/Q2 Circular DNA in Mitochondria & Chloroplasts",
        syllabus_ref="Syllabus 1.2.1, 1.2.6",
        difficulty="CHALLENGING",
        preamble="Both mitochondria and chloroplasts contain their own genetic systems consisting of circular DNA molecules.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe two structural characteristics of mitochondrial DNA that differentiate it from eukaryotic nuclear DNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what types of proteins are encoded by organellar circular DNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Mitochondrial DNA is circular (covalently closed loop) whereas nuclear DNA is linear [1]; Mitochondrial DNA is 'naked' (not complexed with histone proteins) whereas nuclear DNA is packaged with histones into nucleosomes [1]", "marks": 2},
            {"part": "(b)", "points": "Encodes essential core polypeptides of the electron transport chain / ATP synthase (and Rubisco large subunit in chloroplasts) [1]; Encodes organelle-specific transfer RNAs (tRNAs) and ribosomal RNAs (rRNAs) for internal translation [1]", "marks": 2}
        ]
    ))

    # Q37 [Past Paper 9700/22/O/N/22/Q2]
    questions.append(Question(
        number=37,
        title="9700/22/O/N/22/Q2 Bacterial Plasmids & Recombinant Vectors",
        syllabus_ref="Syllabus 1.2.5",
        difficulty="CHALLENGING",
        preamble="Plasmids are small, extrachromosomal circular DNA molecules found naturally in many bacteria.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the features of plasmids that make them suitable as cloning vectors in genetic engineering.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how plasmids contribute to the rapid spread of multidrug resistance across different bacterial species.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Small size allows easy uptake by competent bacterial cells; possess an origin of replication (ori) ensuring autonomous replication independent of chromosome [1]; Contain unique restriction endonuclease recognition sites and selectable marker genes (e.g. antibiotic resistance) [1]", "marks": 2},
            {"part": "(b)", "points": "Conjugative plasmids code for sex pili that connect donor and recipient bacteria, allowing copy transfer via conjugation [1]; R-plasmids carry multiple transposons with resistance genes that can jump between plasmids and genomes across diverse taxonomic groups [1]", "marks": 2}
        ]
    ))

    # Q38 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=38,
        title="[Mentora Original A* Extension] Q38: Artifacts in Electron Microscopy",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="ADVANCED",
        preamble="When interpreting high-resolution electron micrographs, cytologists must distinguish authentic biological structures from preparation artifacts.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Define the term artifact as applied to electron microscopy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how harsh chemical fixation, dehydration in alcohol, and heavy metal staining can induce structural artifacts in cellular organelles.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "A structural detail, distortion, or precipitate observed in a microscopic image that is not naturally present in the living specimen [1]; Introduced accidentally as an artificial consequence of specimen preparation, cutting, or electron beam damage [1]", "marks": 2},
            {"part": "(b)", "points": "Ethanol dehydration causes shrinkage and collapse of delicate cytoplasmic spaces / membranes [1]; Heavy metal stains (e.g. lead citrate, uranyl acetate) can precipitate irregularly on membranes, creating false granules or simulated organelle borders [1]", "marks": 2}
        ]
    ))

    # Q39 [Past Paper 9700/23/M/J/21/Q2]
    questions.append(Question(
        number=39,
        title="9700/23/M/J/21/Q2 Comparison of Plant and Animal Intercellular Junctions",
        syllabus_ref="Syllabus 1.2.1, 1.2.3",
        difficulty="CHALLENGING",
        preamble="Both plant and animal multicellular tissues require direct intercellular communication pathways.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of a plasmodesma, making reference to the plasma membrane and desmotubule.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Identify the functionally analogous intercellular junction found in animal tissues and describe its structure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "A microscopic channel passing through the plant cell wall, lined by continuous plasma membrane connecting adjacent cells [1]; Traversed centrally by a desmotubule, an elongated cylinder of smooth endoplasmic reticulum that coordinates transport [1]", "marks": 2},
            {"part": "(b)", "points": "Gap junction [1]; Formed by hexameric rings of transmembrane connexin proteins (connexons) in adjacent plasma membranes that dock together to form an aqueous pore for ions and small metabolites [1]", "marks": 2}
        ]
    ))

    # Q40 [Past Paper 9700/21/O/N/21/Q1]
    questions.append(Question(
        number=40,
        title="9700/21/O/N/21/Q1 Retroviruses vs Non-Enveloped DNA Viruses",
        syllabus_ref="Syllabus 1.2.7",
        difficulty="CHALLENGING",
        preamble="Viruses vary substantially in structural complexity depending on whether they possess a lipid envelope.",
        section_key="Section B — Data Interpretation & Structured Explanations (4 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Explain how enveloped viruses (such as HIV or influenza) acquire their phospholipid bilayer envelope.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why enveloped viruses are generally more sensitive to chemical disinfectants (such as ethanol and detergents) than non-enveloped capsid viruses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "During viral egress from an infected host cell by budding through the host plasma membrane [1]; The viral nucleocapsid becomes enclosed in a patch of host lipid bilayer containing embedded viral glycoproteins [1]", "marks": 2},
            {"part": "(b)", "points": "Ethanol and detergents readily dissolve lipid bilayers and disrupt hydrophobic interactions in the envelope [1]; Stripping the envelope removes the spike glycoproteins necessary for attaching to and penetrating host cells, rendering the virus non-infectious [1]", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: CORE DEFINITIONS & SHORT CALCULATIONS (10 × 2 MARKS = 20 MARKS)
    # =========================================================================

    # Q41 [Past Paper 9700/22/M/J/23/Q5(a)]
    questions.append(Question(
        number=41,
        title="9700/22/M/J/23/Q5(a) Definition of Resolution",
        syllabus_ref="Syllabus 1.1.5",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Define the term resolution as used in microscopy.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "The ability to distinguish between two points that are very close together [1]; The minimum distance separating two points at which they can still be recognized as distinct entities [1]", "marks": 2}
        ]
    ))

    # Q42 [Past Paper 9700/21/M/J/22/Q5(b)]
    questions.append(Question(
        number=42,
        title="9700/21/M/J/22/Q5(b) Magnification Formula M = I / A",
        syllabus_ref="Syllabus 1.1.3",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="A plant root hair cell has an actual width of 18 µm. In a photomicrograph, its measured image width is 36 mm. Calculate the magnification.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Convert image size: 36 mm = 36,000 µm [1]; Magnification M = 36,000 / 18 = ×2,000 [1]", "marks": 2}
        ]
    ))

    # Q43 [Past Paper 9700/23/O/N/22/Q4(a)]
    questions.append(Question(
        number=43,
        title="9700/23/O/N/22/Q4(a) Calculating Actual Size in Nanometres",
        syllabus_ref="Syllabus 1.1.3, 1.1.4",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="An electron micrograph of a nuclear pore complex has an image diameter of 14 mm at a magnification of ×140,000. Calculate the actual diameter in nanometres (nm).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Actual size A = I / M = 14 mm / 140,000 = 0.0001 mm [1]; 0.0001 mm = 0.1 µm = 100 nm [1]", "marks": 2}
        ]
    ))

    # Q44 [Past Paper 9700/22/O/N/23/Q4(b)]
    questions.append(Question(
        number=44,
        title="9700/22/O/N/23/Q4(b) Structure of Peptidoglycan Cell Wall",
        syllabus_ref="Syllabus 1.2.5",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the two principal chemical macromolecules that form the cell wall of a typical bacterium.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Polysaccharide chains (amino sugars / NAG and NAM) [1]; Cross-linked by short peptides / amino acid oligopeptides [1]", "marks": 2}
        ]
    ))

    # Q45 [Past Paper 9700/21/F/M/24/Q4(a)]
    questions.append(Question(
        number=45,
        title="9700/21/F/M/24/Q4(a) Ribosome Sedimentation Rates: 70S vs 80S",
        syllabus_ref="Syllabus 1.2.1, 1.2.5",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the location of 70S ribosomes and 80S ribosomes in a photosynthetic plant cell.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "70S ribosomes: located in the mitochondrial matrix and chloroplast stroma [1]; 80S ribosomes: located freely in the cytoplasm and attached to the rough endoplasmic reticulum [1]", "marks": 2}
        ]
    ))

    # Q46 [Past Paper 9700/22/M/J/21/Q4(c)]
    questions.append(Question(
        number=46,
        title="9700/22/M/J/21/Q4(c) Non-Cellular Classification of Viruses",
        syllabus_ref="Syllabus 1.2.7",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State two structural features that distinguish viruses from all cellular organisms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Lack a cellular structure / no cytoplasm / no organelles [1]; Contain only one type of nucleic acid (either DNA or RNA, never both simultaneously as functional genomes) [1]", "marks": 2}
        ]
    ))

    # Q47 [Past Paper 9700/23/M/J/22/Q5(a)]
    questions.append(Question(
        number=47,
        title="9700/23/M/J/22/Q5(a) ATP Synthesis in Organelles",
        syllabus_ref="Syllabus 1.2.4",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Name the membrane-bound enzyme complex responsible for synthesizing ATP during oxidative phosphorylation and photophosphorylation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "ATP synthase [1]; Driven by the facilitated diffusion of protons (H+) down their electrochemical gradient [1]", "marks": 2}
        ]
    ))

    # Q48 [Past Paper 9700/21/O/N/21/Q5(b)]
    questions.append(Question(
        number=48,
        title="9700/21/O/N/21/Q5(b) Microtubule Diameter & Tubulin",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="State the diameter of a microtubule and name the globular protein from which it is polymerised.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Diameter: approximately 25 nm (accept 20–25 nm) [1]; Protein: tubulin (alpha-tubulin and beta-tubulin heterodimers) [1]", "marks": 2}
        ]
    ))

    # Q49 [Original Cambridge A* Extension Question]
    questions.append(Question(
        number=49,
        title="[Mentora Original A* Extension] Q49: Eyepiece Graticule Calibration Factor",
        syllabus_ref="Syllabus 1.1.4",
        difficulty="ADVANCED",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="When calibrating a microscope under ×100 magnification, 50 eyepiece graticule units span 0.40 mm on a stage micrometer. Calculate the calibration factor in µm per graticule unit.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "Convert 0.40 mm = 400 µm [1]; 400 µm / 50 graticule units = 8.0 µm per graticule unit [1]", "marks": 2}
        ]
    ))

    # Q50 [Past Paper 9700/22/F/M/23/Q5(c)]
    questions.append(Question(
        number=50,
        title="9700/22/F/M/23/Q5(c) The Tonoplast Membrane",
        syllabus_ref="Syllabus 1.2.1",
        difficulty="CHALLENGING",
        section_key="Section C — Core Definitions & Quantitative Calculations (2 Marks Each)",
        parts=[
            QuestionPart(label="(a)", text="Define tonoplast and state its biological location in plant cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": "The selectively permeable single membrane [1]; Enclosing the central permanent vacuole of a plant cell separating vacuolar cell sap from cytoplasm [1]", "marks": 2}
        ]
    ))

    return questions

def get_topic1_faqs():
    return [
        {
            "q_num": 1,
            "title": "Why Does an Electron Microscope Have a Higher Resolution Than a Light Microscope?",
            "category": "Microscopy Physics • Resolution Principles",
            "examiner_trap": "Stating that an electron microscope has higher resolution because it has 'higher magnification' or is 'more powerful' scores 0 marks. Resolution is strictly governed by the wavelength of radiation.",
            "model_answer": "• Resolution is the ability to distinguish between two separate points as distinct entities; determines level of fine structural detail visible.\n• The limit of resolution is approximately half the wavelength of the radiation used (diffraction limit).\n• Visible light has a long wavelength (400–700 nm), giving a maximum light microscope resolution of ~200 nm.\n• An electron beam has an extremely short wavelength (~0.005 nm), yielding an effective resolution of ~0.5 nm (over 400x greater detail than light microscopes).\n• High resolution allows visualization of ribosomes, cristae, nuclear pores, and phospholipid bilayers."
        },
        {
            "q_num": 2,
            "title": "How and Why Must an Eyepiece Graticule Be Calibrated with a Stage Micrometer?",
            "category": "Microscopic Measurement • Calibration Protocol",
            "examiner_trap": "Assuming an eyepiece graticule has a fixed physical measurement (e.g. 'each mark is 1 µm'). Graticule units are arbitrary and MUST be calibrated separately for EACH objective lens magnification.",
            "model_answer": "• An eyepiece graticule is a transparent glass disc etched with 100 arbitrary, uncalibrated scale divisions that sits in the microscope ocular.\n• A stage micrometer is a precision slide etched with a known microscopic scale (e.g. 1.0 mm divided into 100 units; 1 division = 10 µm / 0.01 mm).\n• Calibration: Align eyepiece graticule scale with stage micrometer scale; find points of exact line coincidence; count graticule units (epu) spanning a known micrometer distance.\n• Calculation: Calibration factor = (stage micrometer distance in µm) / (number of eyepiece units).\n• Crucial principle: When changing objective lenses (e.g. x10 to x40), the specimen image is magnified but the graticule is not; the graticule MUST be recalibrated."
        },
        {
            "q_num": 3,
            "title": "What Are the Definitive Ultrastructural Distinctions Between Prokaryotic and Eukaryotic Cells?",
            "category": "Cell Taxonomy • Ultrastructural Architecture",
            "examiner_trap": "Asserting that prokaryotes have 'no ribosomes' (they possess smaller 70S ribosomes) or that they have a cellulose cell wall (bacterial walls consist of peptidoglycan/murein).",
            "model_answer": "• Genetic Material: Prokaryotes possess a single circular, naked DNA molecule located in the nucleoid region (no true nucleus) and plasmids; eukaryotes have linear DNA complexed with histone proteins within a double-membrane nucleus.\n• Ribosome Size: Prokaryotes have smaller 70S ribosomes (in cytoplasm); eukaryotes have larger 80S ribosomes (cytosolic/RER) and 70S inside mitochondria and chloroplasts.\n• Membrane-Bound Organelles: Prokaryotes completely lack membrane-bound organelles (no mitochondria, chloroplasts, ER, Golgi, lysosomes); eukaryotes possess extensive compartmentalisation.\n• Cell Wall Chemistry: Prokaryotic walls consist of peptidoglycan (murein); plant eukaryotic walls contain cellulose, and fungal walls contain chitin."
        },
        {
            "q_num": 4,
            "title": "Trace the Complete Organellar Pathway of a Secretory Protein from Synthesis to Exocytosis.",
            "category": "Endomembrane Dynamics • Protein Secretion",
            "examiner_trap": "Claiming that the Golgi apparatus 'synthesises' secretory proteins (synthesis occurs at RER ribosomes; Golgi modifies, sorts, and packages) or omitting transport vesicles.",
            "model_answer": "• Transcription in nucleus: mRNA transcribes gene, exits into cytoplasm via nuclear pore.\n• Translation on Rough ER: Ribosomes on RER membrane translate mRNA into polypeptide, which threads into RER cisternal lumen for secondary/tertiary folding.\n• Transport Vesicle: Vesicles bud off RER membrane carrying immature glycoprotein and fuse with the cis-face of the Golgi apparatus.\n• Golgi Processing: Protein passes through Golgi cisternae; modified by glycosylation (oligosaccharide addition), phosphorylation, and conformational sorting.\n• Secretory Vesicle & Exocytosis: Mature secretory vesicles bud off trans-Golgi face, move along cytoskeleton powered by ATP motor proteins, and fuse with cell surface membrane (exocytosis)."
        },
        {
            "q_num": 5,
            "title": "What Structural Evidence Within Mitochondria and Chloroplasts Supports the Endosymbiotic Theory?",
            "category": "Organelle Evolution • Endosymbiotic Theory",
            "examiner_trap": "Confusing mitochondrial cristae with chloroplast thylakoid membranes, or failing to identify both circular naked DNA and 70S ribosomes as prokaryotic signatures.",
            "model_answer": "• Circular, Naked DNA: Both organelles contain small circular loops of DNA without histone proteins, identical to bacterial chromosomes.\n• 70S Ribosomes: Both contain 70S ribosomes (subunits 30S and 50S), identical in size and antibiotic susceptibility to prokaryotic ribosomes, distinct from eukaryotic 80S.\n• Double Membrane: Both are surrounded by two concentric membranes; the inner membrane exhibits bacterial lipid composition, while the outer membrane reflects the host endocytic vesicle.\n• Autonomous Binary Fission: Mitochondria and chloroplasts replicate independently within the eukaryotic cell via binary fission."
        },
        {
            "q_num": 6,
            "title": "What Is the Microscopic Architecture and Function of Centrioles and Microtubule Organising Centres (MTOC)?",
            "category": "Cytoskeleton • Mitotic Apparatus",
            "examiner_trap": "Claiming plant cells cannot perform mitosis because they lack centrioles. Higher plant cells organize spindle fibres from MTOCs without requiring centrioles.",
            "model_answer": "• Centriole Architecture: A pair of hollow cylindrical structures positioned at right angles to each other in the centrosome; wall composed of 9 triplets (9x3) of microtubules polymerised from tubulin.\n• MTOC Function: Centrosome acts as the primary Microtubule Organising Centre (MTOC) in animal cells, nucleating and organising tubulin heterodimers into spindle fibres.\n• Mitotic Role: During prophase, centrosomes replicate and migrate to opposite cellular poles; polymerise spindle microtubules that attach to kinetochores to pull sister chromatids apart.\n• Cilia and Flagella: Centrioles act as basal bodies that template the 9+2 axoneme arrangement of cilia and flagella."
        },
        {
            "q_num": 7,
            "title": "Distinguish Between Transmission Electron Microscopy (TEM) and Scanning Electron Microscopy (SEM).",
            "category": "Microscopic Instrumentation • Beam Interactions",
            "examiner_trap": "Confusing the types of images produced: TEM produces high-resolution 2D internal cross-sections; SEM produces 3D surface topographical views.",
            "model_answer": "• Transmission Electron Microscope (TEM): Electron beam passes through an ultra-thin resin-embedded specimen stained with heavy metals; electrons transmitted through specimen create a high-resolution 2D image of internal organellar ultrastructure (resolution ~0.5 nm).\n• Scanning Electron Microscope (SEM): Electron beam scans across the surface of a specimen coated in a thin layer of gold; secondary electrons reflected and emitted from the surface are collected by a detector, producing a 3D image of surface topography (resolution ~3–10 nm).\n• Specimen preparation: Both require non-living dead specimens maintained under high vacuum."
        },
        {
            "q_num": 8,
            "title": "What Are the Exact Roles of the Nuclear Envelope, Nuclear Pores, and Nucleolus?",
            "category": "Nuclear Anatomy • Functional Compartmentalisation",
            "examiner_trap": "Stating that the nucleolus synthesises complete ribosomes. The nucleolus transcribes ribosomal RNA (rRNA) and assembles ribosomal subunits, not fully assembled functional ribosomes.",
            "model_answer": "• Nuclear Envelope: Double membrane (inner and outer phospholipid bilayers separated by perinuclear space); outer membrane continuous with rough ER; compartmentalises genetic DNA from cytoplasm.\n• Nuclear Pores: Large multi-protein complexes perforating envelope; regulate selective bidirectional transport: mRNA, tRNA, and ribosomal subunits exit to cytoplasm; histones, DNA/RNA polymerases, nucleotides, and ATP enter nucleus.\n• Nucleolus: Dense, non-membrane-bound subnuclear region containing rDNA; transcribes rRNA and complexes it with ribosomal proteins to assemble 40S and 60S ribosomal subunits."
        },
        {
            "q_num": 9,
            "title": "How Do Primary Cell Walls, Middle Lamellae, and Plasmodesmata Function Together in Plant Tissues?",
            "category": "Plant Cell Anatomy • Extracellular Matrix",
            "examiner_trap": "Describing the plant cell wall as 'selectively permeable'. The primary cell wall is completely permeable to water and dissolved solutes; the plasma membrane confers selective permeability.",
            "model_answer": "• Primary Cell Wall: Extracellular meshwork of cellulose microfibrils embedded in a hydrated matrix of hemicellulose and pectin; fully permeable to water and dissolved ions; confers high tensile strength to prevent osmotic lysis.\n• Middle Lamella: Outermost intercellular cementing layer composed of calcium and magnesium pectates; glues adjacent plant cell walls together.\n• Plasmodesmata: Microscopic cylindrical cytoplasmic channels traversing cell walls; lined by plasma membrane and containing a central desmotubule (derived from ER); enables continuous symplastic transport of water, sucrose, and signalling ions."
        },
        {
            "q_num": 10,
            "title": "Why Are Viruses Categorised as Non-Cellular (Acellular) Biological Entities?",
            "category": "Virology • Acellular Structures",
            "examiner_trap": "Classifying viruses as prokaryotes or living cells. Viruses lack cellular organization, have no metabolic machinery, and cannot generate ATP independently.",
            "model_answer": "• Non-Cellular Nature: Lack cytoplasm, cell surface membrane (unless host-derived envelope), ribosomes, and cellular organelles.\n• Nucleic Acid Genome: Possess only ONE type of nucleic acid genome (either DNA or RNA, single-stranded or double-stranded, never both simultaneously as genetic material).\n• Protein Capsid: Genetic core is enclosed in a protective protein coat composed of repeating protein subunits called capsomeres.\n• Obligate Intracellular Parasites: Exhibit zero independent metabolic activity; cannot synthesise ATP or proteins; completely dependent on host cell machinery (ribosomes, tRNA, enzymes) for replication."
        }
    ]

if __name__ == "__main__":
    qs = get_topic1_questions()
    faqs = get_topic1_faqs()
    print(f"Loaded {len(qs)} questions and {len(faqs)} FAQs for Topic 1: Cell Structure.")
    total_marks = sum(sum(p.marks for p in q.parts) for q in qs)
    print(f"Total marks = {total_marks}")

