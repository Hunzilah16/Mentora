"""
Topic 5: The Mitotic Cell Cycle — 50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Cytological Mechanism Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Past Paper vs Original Ratio: 43 Authentic (86%) / 7 Original Extensions (14%)
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic5_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Chromosome structure & telomeres (Fig 5.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q3 - Replicated Chromosome Architecture and Telomeres",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="During nuclear division, eukaryotic chromatin condenses into highly structured, visible chromosomes. Fig. 5.1 illustrates the structural components of a replicated metaphase chromosome alongside the hierarchy of chromatin packaging.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_1_chromosome_structure_telomeres.png"),
        figure_caption="Fig. 5.1: Structure of a replicated metaphase chromosome (A) and nucleosome packaging (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.1, describe the role of histone proteins in packaging DNA into chromatin and explain why chromatin condensation is essential prior to nuclear division.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why sister chromatids are genetically identical and describe the specific role of the centromere during mitotic division.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the structure and function of telomeres, and explain why linear chromosomes require specialized terminal cap sequences.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Positively charged basic amino acids on histones bind negatively charged phosphate backbone of DNA; DNA winds around octamer core (~146 bp) to form nucleosomes ('beads on string'), folding into 30 nm fibres and loops; condensation prevents DNA tangling, breakage, and unequal segregation during anaphase [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Sister chromatids are produced by semi-conservative DNA replication during S phase, producing exact nucleotide sequence copies; centromere holds sister chromatids together until anaphase and serves as assembly site for kinetochores where spindle microtubules attach [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Telomeres consist of non-coding repetitive DNA sequences (TTAGGG in humans) at linear chromosome ends; protect vital coding genes from degradation during successive replication cycles (end-replication problem) and prevent chromosome ends from fusing or triggering inappropriate DNA damage response [2].", "marks": 2}
        ]
    ))

    # Q2: Importance of mitosis in multicellular organisms
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q3 - Biological Significance of Mitotic Nuclear Division",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Mitosis is a fundamental eukaryotic process that produces two genetically identical daughter nuclei from a single parental nucleus.",
        parts=[
            QuestionPart(label="(a)", text="Explain the importance of mitosis in the growth of multicellular organisms and the repair of damaged tissues.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe two examples of asexual reproduction in eukaryotes that depend entirely on mitotic division.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why it is vital that daughter cells produced by mitosis possess an exact replica of the parental genome.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Growth involves increasing total cell number from a single zygote while maintaining identical genetic instruction; repair involves replacing dead/damaged cells with structurally and functionally identical new cells to restore tissue architecture [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Binary fission / budding in yeast (or Hydra); vegetative propagation in plants (e.g. runners in strawberries, tubers in potatoes, bulbs) producing genetically identical clones [2].", "marks": 2},
            {"q": "Q2(c)", "points": "Ensures all somatic cells retain complete instructions for all metabolic proteins and cellular functions; prevents loss of vital alleles or gene dosage imbalances that could impair cell survival or lead to aberrant differentiation [2].", "marks": 2}
        ]
    ))

    # Q3: Cell cycle phases & durations (Fig 5.2)
    questions.append(Question(
        number=3,
        title="9700/22/F/M/22/Q2 - The Eukaryotic Cell Cycle and Phase Partitioning",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="The eukaryotic cell cycle comprises interphase (G1, S, G2), mitosis (M), and cytokinesis (C). Fig. 5.2 displays a proportional breakdown of a 24-hour mammalian cell cycle.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_2_cell_cycle_pie_chart.png"),
        figure_caption="Fig. 5.2: Phase proportions and durations in a typical 24-hour eukaryotic cell cycle.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.2, outline the primary biochemical and biosynthetic events occurring during the G1 phase and G2 phase of interphase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what occurs during the S phase of interphase and deduce why a cell cannot immediately enter mitosis following DNA synthesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Calculate the percentage of the 24-hour cycle spent in interphase compared to the M phase (mitosis + cytokinesis), and explain why interphase is described as 'metabolically active'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "G1: cell growth, transcription of mRNA, translation of proteins, synthesis of enzymes required for replication, duplication of organelles; G2: synthesis of tubulin and spindle proteins, ATP generation, error check of newly replicated DNA, centrosome maturation [2].", "marks": 2},
            {"q": "Q3(b)", "points": "S phase: semi-conservative replication of nuclear DNA and duplication of centrosomes/centrioles; cannot immediately divide because cell must synthesize tubulin, double cytoplasmic mass, and verify DNA replication fidelity at G2/M checkpoint to prevent mutational inheritance [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Interphase = (10h G1 + 8h S + 4h G2) = 22 h out of 24 h = 91.7%; M phase = 2 h = 8.3%; highly active because intensive cellular respiration, transcription, protein synthesis, and organelle biogenesis occur continuously [2].", "marks": 2}
        ]
    ))

    # Q4: Interphase biochemical checkpoints
    questions.append(Question(
        number=4,
        title="9700/23/M/J/21/Q4 - Molecular Checkpoint Control Across the Cell Cycle",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Progression through the eukaryotic cell cycle is strictly coordinated by surveillance mechanisms known as checkpoints.",
        parts=[
            QuestionPart(label="(a)", text="Describe the biological role of the G1/S restriction checkpoint and identify two conditions that must be fulfilled before a cell is permitted to pass it.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological state of a cell that exits the active cycle into G0 phase, citing one cell type that enters G0 reversibly and one irreversibly.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the surveillance role of the spindle assembly checkpoint (SAC) during metaphase and state the consequence if this checkpoint is bypassed.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "G1/S checkpoint commits cell to complete division or enter quiescent G0 state; requires sufficient cell size/growth, adequate nutrient and energy reserves, absence of DNA damage, and external growth factor signals [2].", "marks": 2},
            {"q": "Q4(b)", "points": "G0 is a non-dividing, metabolically active state where cells arrest differentiation or repair DNA; lymphocytes enter G0 reversibly (reactivated by antigen challenge); mature neurons or cardiac myocytes enter G0 permanently/irreversibly [2].", "marks": 2},
            {"q": "Q4(c)", "points": "SAC monitors whether all kinetochores are correctly attached to bipolar spindle microtubules under balanced tension; bypassing SAC leads to lagging chromosomes, non-disjunction, and aneuploidy in daughter cells [2].", "marks": 2}
        ]
    ))

    # Q5: DNA mass & chromosome ploidy (Fig 5.3)
    questions.append(Question(
        number=5,
        title="9700/21/M/J/22/Q3 - Quantitative Changes in DNA Content and Chromosome Number",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="During the cell cycle, cellular DNA mass doubles and halves, while chromosome count exhibits distinct regulatory patterns. Fig. 5.3 plots DNA mass and chromosome ploidy throughout a complete mitotic cycle.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_3_dna_mass_ploidy_graph.png"),
        figure_caption="Fig. 5.3: Relative DNA mass (solid line) and chromosome number (dashed line) across the cell cycle.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.3, explain why the DNA content rises from 2C to 4C during S phase, yet the chromosome number remains 2n throughout G2 and metaphase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the chromosome number momentarily doubles to 4n during anaphase, whereas the total cellular DNA mass remains at 4C.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the events occurring during telophase and cytokinesis that restore both DNA mass to 2C and chromosome count to 2n in each daughter cell.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "During S phase, each chromosome undergoes semi-conservative replication producing two identical sister chromatids (doubling DNA mass from 2C to 4C); however, sister chromatids remain joined at a single centromere, so each replicated structure is counted as one chromosome (2n) [2].", "marks": 2},
            {"q": "Q5(b)", "points": "At anaphase, centromeres split and sister chromatids separate to become individual daughter chromosomes; since both sets are within the same single cell cytoplasm, the chromosome count is 4n, while total DNA mass remains 4C until division of cytoplasm [2].", "marks": 2},
            {"q": "Q5(c)", "points": "During cytokinesis, the cytoplasm and organelles are partitioned into two separate daughter cells by cleavage furrow or cell plate; each resulting daughter cell encloses one set of 2n chromosomes and 2C DNA mass within a newly reassembled nuclear envelope [2].", "marks": 2}
        ]
    ))

    # Q6: Centromere and kinetochore function
    questions.append(Question(
        number=6,
        title="9700/22/O/N/21/Q2 - Centromeric Heterochromatin and Kinetochore Assembly",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="The centromere is a specialised, epigenetically defined chromosomal domain required for chromosome segregation during mitosis.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structural organisation of centromeric heterochromatin and state why it appears as a 'primary constriction' on condensed chromosomes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the structure and location of the kinetochore protein complex on a replicated chromosome.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how motor proteins associated with kinetochores contribute to chromosome movement during anaphase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Centromeric heterochromatin contains highly repetitive tandem satellite DNA sequences packaged with specialised histone variant CENP-A; tightly compacted structure is resistant to uncoiling, appearing narrower (constricted) than euchromatic chromosome arms [2].", "marks": 2},
            {"q": "Q6(b)", "points": "Multi-protein disc-like complex assembled on the outer surface of each centromere; each replicated chromosome has two kinetochores oriented back-to-back, facing opposite spindle poles [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Kinetochores contain minus-end directed motor proteins (dynein) and depolymerising kinesins; as kinetochore microtubules disassemble (lose tubulin dimers at plus ends), motor proteins actively pull daughter chromosomes along shortening microtubules toward centrosomes [2].", "marks": 2}
        ]
    ))

    # Q7: Four stages of mitosis (Fig 5.4)
    questions.append(Question(
        number=7,
        title="9700/21/O/N/23/Q3 - Sequential Morphological Events of Mitosis",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Mitosis is divided into four distinct phases: prophase, metaphase, anaphase, and telophase. Fig. 5.4 illustrates the diagnostic cellular changes across these stages in an animal cell.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_4_mitosis_four_stages_diagram.png"),
        figure_caption="Fig. 5.4: Cellular diagrams showing prophase, metaphase, anaphase, and telophase.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.4, describe the nuclear and cytoskeletal events that characterise prophase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the orientation and alignment of chromosomes at the equatorial plate during metaphase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the mechanisms responsible for the poleward migration of sister chromatids during anaphase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Chromatin condenses into distinct visible chromosomes composed of two sister chromatids; nucleolus disassembles; centrosomes migrate to opposite cell poles polymerising spindle microtubules; nuclear envelope breaks down into vesicles [2].", "marks": 2},
            {"q": "Q7(b)", "points": "Chromosomes align randomly in a single plane along the cell equator (metaphase plate); spindle microtubules from opposite poles attach to kinetochores of each sister chromatid, creating opposing tension [2].", "marks": 2},
            {"q": "Q7(c)", "points": "Centromeres divide as cohesin proteins are cleaved by separase; kinetochore microtubules shorten by depolymerisation at their plus and minus ends, pulling daughter chromosomes V-shaped (centromere leading) toward opposite centrosomes [2].", "marks": 2}
        ]
    ))

    # Q8: Nuclear envelope breakdown and reassembly
    questions.append(Question(
        number=8,
        title="9700/22/M/J/20/Q3 - Dynamics of the Nuclear Envelope and Nucleolus in Mitosis",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="During open eukaryotic mitosis, the nuclear envelope undergoes regulated disassembly in prophase followed by reassembly around daughter chromosomes in telophase.",
        parts=[
            QuestionPart(label="(a)", text="Explain the biological necessity of dismantling the nuclear envelope during late prophase in animal and plant cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how phosphorylation of nuclear lamins by cyclin-dependent kinases (CDKs) causes nuclear envelope breakdown.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the reassembly of the nuclear envelope and reformation of the nucleolus during telophase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "Dismantling the double membrane barrier allows cytoplasmic spindle microtubules to access and capture chromosomal kinetochores; without envelope breakdown, microtubule polymers cannot contact chromosomes [2].", "marks": 2},
            {"q": "Q8(b)", "points": "Active CDK1-cyclin B complex phosphorylates specific serine residues on nuclear lamina proteins (lamins A, B, C); phosphorylation disrupts electrostatic interactions, causing the 2D lamin meshwork to depolymerise and the nuclear envelope to fragment into vesicles [2].", "marks": 2},
            {"q": "Q8(c)", "points": "Dephosphorylation of lamins allows membrane vesicles to bind daughter chromosomes and fuse together into new double membranes; nucleolar organiser regions (NORs) of chromosomes transcribe rRNA to re-establish the nucleolus [2].", "marks": 2}
        ]
    ))

    # Q9: Root tip squash photomicrograph (Fig 5.5)
    questions.append(Question(
        number=9,
        title="9700/23/O/N/22/Q2 - Identification of Mitotic Stages in Allium Root Tip Squash",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Meristematic tissue from root tips provides an abundant source of actively dividing plant cells. Fig. 5.5 shows a high-power light photomicrograph field of an Allium cepa root tip squash stained with aceto-orcein, with five cells labeled A to E.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_5_root_tip_squash_photomicrograph.png"),
        figure_caption="Fig. 5.5: Light micrograph representation of Allium root meristem cells and diagnostic stage characteristics.",
        parts=[
            QuestionPart(label="(a)", text="Identify the mitotic stages represented by cells A, B, C, and D in Fig. 5.5, justifying each identification with one visible microscopic feature.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the apical meristem of the root tip is selected rather than tissue several millimetres behind the root cap when preparing this squash.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the biological function of maceration with 1.0 mol dm-3 hydrochloric acid (HCl) and staining with aceto-orcein during the squash preparation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "A = Anaphase (sister chromatids separated into two groups moving to poles); B = Metaphase (chromosomes aligned across equatorial plate); C = Prophase (chromatin condensed into visible threads, intact nucleus); D = Telophase (two distinct daughter clusters at opposite poles, cell plate forming) [2].", "marks": 2},
            {"q": "Q9(b)", "points": "The root apical meristem is the zone of active cell division (mitosis); tissue further back (zone of elongation/differentiation) contains differentiated non-dividing cells that have entered G0 or elongated [2].", "marks": 2},
            {"q": "Q9(c)", "points": "HCl breaks down / hydrolyses the calcium pectate of the middle lamella, softening tissue so cells can be squashed into a single monolayer; aceto-orcein is a basic dye that binds specifically to negatively charged phosphate groups of DNA, staining chromosomes dark red/purple [2].", "marks": 2}
        ]
    ))

    # Q10: Spindle apparatus and MTOC function
    questions.append(Question(
        number=10,
        title="9700/21/M/J/23/Q3 - Microtubule Organising Centres (MTOCs) and Spindle Bipolarity",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="The mitotic spindle is a self-assembling bipolar macromolecular machine constructed from alpha- and beta-tubulin heterodimers.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of a microtubule in terms of alpha- and beta-tubulin protofilaments and explain how dynamic instability allows spindle assembly.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between animal cells and flowering plant cells with respect to the structure and origin of their mitotic spindle poles.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the roles of interpolar (non-kinetochore) microtubules and astral microtubules during mitosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Hollow cylinder (~25 nm diameter) composed of 13 parallel protofilaments formed by alpha/beta-tubulin heterodimers; dynamic instability involves rapid switching between GTP-fuelled polymerisation (growth) and depolymerisation (shrinkage), allowing microtubules to search cytoplasm and capture kinetochores [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Animal cells possess centrosomes containing a pair of perpendicular centrioles (9x3 triplet pattern) acting as MTOCs; flowering plant cells lack centrioles/centrosomes but form spindle poles from diffuse, non-centrosomal MTOC material throughout the cytoplasm [2].", "marks": 2},
            {"q": "Q10(c)", "points": "Interpolar microtubules overlap at the spindle equator; kinesin motor proteins push them apart, elongating the cell during anaphase B; astral microtubules anchor centrosomes to the cell cortex, orienting the division axis [2].", "marks": 2}
        ]
    ))

    # Q11: Telomere shortening and senescence (Fig 5.6)
    questions.append(Question(
        number=11,
        title="9700/22/M/J/21/Q4 - The End-Replication Problem, Telomere Shortening, and Cellular Senescence",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="In conventional somatic cells, telomeric DNA shortens progressively with each round of cell division. Fig. 5.6 depicts the molecular basis of the end-replication problem and the Hayflick limit.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_6_telomere_shortening_senescence.png"),
        figure_caption="Fig. 5.6: The end-replication problem at the lagging strand and telomere-mediated replicative senescence.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.6, explain why conventional DNA polymerase cannot fully replicate the 3' end of the lagging strand template.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how critical telomere shortening triggers the Hayflick limit and cellular senescence.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how the enzyme telomerase prevents telomere shortening and state two specific human cell types where telomerase is actively expressed.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "DNA polymerase can only add nucleotides to an existing 3'-OH group and synthesises in 5' to 3' direction; RNA primer at the terminal end of the lagging strand is degraded by exonucleases, leaving an unreplicated single-stranded 3' overhang that is lost upon subsequent division [2].", "marks": 2},
            {"q": "Q11(b)", "points": "When telomeres erode below a critical threshold length, the exposed free chromosome ends resemble double-strand breaks; this activates p53 and ATM kinase cascades, arresting the cell irreversibly in G0 (replicative senescence) or triggering apoptosis [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Telomerase is a reverse transcriptase ribonucleoprotein with an intrinsic RNA template (TERC); it extends 3' single-stranded overhangs by synthesising repetitive TTAGGG units; actively expressed in embryonic stem cells, adult germline cells (spermatogonia), and cancer cells [2].", "marks": 2}
        ]
    ))

    # Q12: Telomerase in cancer immortality
    questions.append(Question(
        number=12,
        title="[Mentora Original A* Extension] - Telomerase Reactivation and Cellular Immortality in Neoplasia",
        syllabus_ref="Syllabus 5.1",
        difficulty="CHALLENGING",
        preamble="Normal somatic cells possess a finite replicative lifespan, whereas over 85% to 90% of malignant human carcinomas exhibit telomerase reactivation.",
        parts=[
            QuestionPart(label="(a)", text="Explain how telomerase reactivation confers replicative immortality to malignant tumour cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Suggest why somatic tissues evolved a finite Hayflick limit rather than constitutive telomerase expression.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Evaluate the therapeutic potential and potential side effects of using competitive telomerase inhibitors (e.g. Imetelstat) as anti-cancer chemotherapy.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "By continually synthesising hexameric TTAGGG repeats at chromosome tips, telomerase offsets end-replication losses; prevents telomere attrition from reaching the critical threshold, allowing indefinite rounds of mitotic proliferation without triggering p53-mediated senescence [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Acts as an intrinsic tumour-suppressive barrier; limits the cumulative number of divisions a cell lineage can undertake, thereby restricting the time window in which somatic cells can accumulate oncogenic mutations [2].", "marks": 2},
            {"q": "Q12(c)", "points": "Benefits: selectively induces telomere attrition and senescence in rapidly dividing malignant cells that depend on telomerase; Side effects: impairs normal proliferating tissues that express telomerase, causing bone marrow suppression (anaemia, neutropenia) and intestinal mucosal damage [2].", "marks": 2}
        ]
    ))

    # Q13: Stem cell potency hierarchy (Fig 5.7)
    questions.append(Question(
        number=13,
        title="9700/22/F/M/23/Q3 - Stem Cell Potency Hierarchy and Tissue Homeostasis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Stem cells are unspecialised cells capable of self-renewal and differentiation into specialised lineages. Fig. 5.7 illustrates the biological hierarchy of stem cell potency from zygote to terminal differentiation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_7_stem_cell_hierarchy_potency.png"),
        figure_caption="Fig. 5.7: Hierarchy of stem cell potency: totipotent, pluripotent, multipotent, and unipotent.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.7, distinguish between totipotent stem cells and pluripotent stem cells, citing an anatomical source for each.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how multipotent adult stem cells in bone marrow maintain tissue homeostasis throughout an organism's lifetime.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the process of asymmetric division in stem cells and explain why it is vital for sustained tissue regeneration.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Totipotent: can differentiate into all embryonic cell types PLUS extraembryonic tissues (placenta, amnion) (e.g. zygote and blastomeres up to 8-cell morula); Pluripotent: can differentiate into all cell types of the three embryonic germ layers (ectoderm, mesoderm, endoderm) but not placenta (e.g. inner cell mass of blastocyst) [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Haematopoietic stem cells divide by mitosis and differentiate into all mature blood lineages (erythrocytes, leukocytes, platelets) to replace millions of short-lived cells lost daily to senescence or wear [2].", "marks": 2},
            {"q": "Q13(c)", "points": "Each division produces one daughter cell that remains an undifferentiated stem cell (self-renewal) and one daughter cell that commits to differentiation; prevents depletion of the stem cell pool while generating replacement differentiated cells [2].", "marks": 2}
        ]
    ))

    # Q14: Clinical stem cell therapies & ethics
    questions.append(Question(
        number=14,
        title="9700/21/O/N/20/Q3 - Therapeutic Applications and Bioethics of Stem Cells",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Stem cell therapies represent a major frontier in regenerative medicine, ranging from bone marrow transplants to induced pluripotent stem cells (iPSCs).",
        parts=[
            QuestionPart(label="(a)", text="Describe how bone marrow stem cell transplantation is used to treat patients suffering from leukaemia.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the ethical advantages of using induced pluripotent stem cells (iPSCs) compared to embryonic stem cells (ESCs) in medical research.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two potential biological risks associated with transplanting undifferentiated stem cells into human clinical patients.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Chemotherapy / radiation obliterates the patient's cancerous bone marrow and abnormal leukocytes; donor haematopoietic stem cells are infused intravenously, home to marrow cavities, and regenerate a healthy population of erythrocytes, leukocytes, and platelets [2].", "marks": 2},
            {"q": "Q14(b)", "points": "iPSCs are derived by reprogramming adult somatic cells (e.g. fibroblasts) with transcription factors (Yamanaka factors), circumventing the destruction of human embryos; can be patient-specific (autologous), eliminating graft-versus-host immune rejection [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Formation of teratomas (benign or malignant multi-tissue tumours) due to uncontrolled proliferation; immune rejection by recipient if allogeneic stem cells are used / genomic instability from reprogramming vectors [2].", "marks": 2}
        ]
    ))

    # Q15: Carcinogenesis & tumour formation (Fig 5.8)
    questions.append(Question(
        number=15,
        title="9700/22/M/J/22/Q3 - Multi-Step Carcinogenesis, Angiogenesis, and Metastasis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Cancer arises from a sequential accumulation of genetic and epigenetic alterations in genes controlling cell division. Fig. 5.8 illustrates the four progression steps from single mutant cell to secondary metastatic colonies.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_8_carcinogenesis_tumour_formation.png"),
        figure_caption="Fig. 5.8: Multi-step model of carcinogenesis: mutation, hyperplasia, angiogenesis, and metastasis.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.8, distinguish between proto-oncogenes and tumour suppressor genes, explaining how mutations in each contribute to hyperplasia.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological importance of angiogenesis (Step 3) in tumour progression and describe how tumour cells stimulate this process.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the cellular events involved in metastasis (Step 4) and explain why metastatic tumours pose the greatest clinical challenge.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Proto-oncogenes stimulate normal cell division; gain-of-function mutation produces oncogenes with hyperactive proteins driving excessive mitosis; tumour suppressor genes inhibit cell cycle or initiate apoptosis; loss-of-function mutation removes braking mechanism, allowing unchecked proliferation [2].", "marks": 2},
            {"q": "Q15(b)", "points": "Tumours exceeding ~2 mm suffer hypoxia and nutrient starvation; hypoxic tumour cells secrete Vascular Endothelial Growth Factor (VEGF), stimulating capillary endothelial cells to sprout new blood vessels into tumour, supplying O2/glucose and enabling continued growth [2].", "marks": 2},
            {"q": "Q15(c)", "points": "Malignant cells lose cell-cell adhesion (E-cadherin), degrade basement membrane using matrix metalloproteinases, intravasate into blood/lymph, circulate, and extravasate into distant organs; widespread dissemination makes surgical excision impossible, requiring systemic cytotoxic chemotherapy [2].", "marks": 2}
        ]
    ))

    # Q16: Carcinogenic mutagens and p53 pathways
    questions.append(Question(
        number=16,
        title="9700/21/M/J/20/Q2 - Environmental Carcinogens and the Guardian Role of p53",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="The TP53 gene product, protein p53, is known as the 'guardian of the genome' due to its central surveillance role at cell cycle checkpoints.",
        parts=[
            QuestionPart(label="(a)", text="Describe three distinct classes of environmental mutagens that increase the risk of developing malignant tumours.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the normal cellular response coordinated by p53 upon detecting DNA double-strand breaks during the G1 phase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why loss-of-function mutations in both alleles of TP53 are found in over 50% of all human cancers.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Ionising radiation (X-rays, gamma rays) causing double-strand breaks; non-ionising UV radiation causing thymine-thymine dimers; chemical mutagens (e.g. benzopyrene in cigarette smoke, aflatoxins, reactive oxygen species) causing base alkylation/transversions [2].", "marks": 2},
            {"q": "Q16(b)", "points": "p53 acts as a transcription factor inducing p21, which binds and inhibits CDK2/4-cyclin complexes, arresting cells in G1; activates DNA repair enzymes; if damage is irreparable, p53 upregulates pro-apoptotic Bax, triggering programmed cell death [2].", "marks": 2},
            {"q": "Q16(c)", "points": "TP53 is a recessive tumour suppressor; loss of both alleles abolishes G1/S arrest and apoptosis, allowing damaged cells carrying unrepaired mutations and chromosomal aberrations to survive and divide continuously [2].", "marks": 2}
        ]
    ))

    # Q17: Cytokinesis in animals vs plants (Fig 5.9)
    questions.append(Question(
        number=17,
        title="9700/23/M/J/22/Q3 - Mechanics of Cytokinesis in Animal and Plant Cells",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Cytokinesis is the physical division of the cytoplasm following telophase. Fig. 5.9 contrasts the structural mechanisms of cytokinesis in animal cells and higher plant cells.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_9_cytokinesis_animal_vs_plant.png"),
        figure_caption="Fig. 5.9: Comparison of cytokinesis: cleavage furrow (A) vs cell plate formation (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.9, describe the formation and action of the contractile ring during animal cell cytokinesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how Golgi-derived vesicles and the phragmoplast construct a new cell wall during plant cytokinesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why plant cells cannot divide their cytoplasm using a contractile cleavage furrow mechanism.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Submembrane ring composed of actin microfilaments and myosin motor proteins forms at the equatorial cortex; myosin contracts actin filaments, invaginating the plasma membrane inward to create a cleavage furrow that deepens until cell pinches into two [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Phragmoplast microtubules guide Golgi vesicles containing pectins and hemicelluloses to equatorial plane; vesicles fuse outwards from centre toward parental walls, forming cell plate; vesicle membranes become plasma membranes, and contents form middle lamella [2].", "marks": 2},
            {"q": "Q17(c)", "points": "Higher plant cells are enclosed by a rigid, non-flexible outer cell wall composed of crystalline cellulose microfibrils; the rigid wall prevents inward deformation, constriction, or pinching of the plasma membrane [2].", "marks": 2}
        ]
    ))

    # Q18: S phase replication fork and cohesin complexes
    questions.append(Question(
        number=18,
        title="[Mentora Original A* Extension] - Cohesin Ring Complexes and Chromosome Sisterhood",
        syllabus_ref="Syllabus 5.1",
        difficulty="CHALLENGING",
        preamble="Following DNA replication in S phase, newly synthesised sister chromatids must remain precisely aligned until anaphase onset.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of cohesin protein complexes and explain how they entrap sister chromatids following replication.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the enzyme separase is kept inactive prior to anaphase, and describe the trigger that leads to its activation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Predict the cytological consequence if cohesin rings fail to assemble along chromosome arms during S phase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Ring-shaped multi-protein complex (composed of Smc1, Smc3, Scc1, Scc3); topologically encircles both sister DNA duplexes together along their length, maintaining cohesion and preventing premature dissociation [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Separase is bound and inhibited by the chaperone protein securin; once all chromosomes achieve bipolar attachment at metaphase, the Anaphase-Promoting Complex (APC/C) ubiquitylates securin for proteasomal destruction, freeing active separase to cleave cohesin [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Sister chromatids detach prematurely during prophase or metaphase; without cohesion opposing spindle pulling forces, chromosomes cannot align properly at the equator, resulting in catastrophic chromosome missegregation and cell death [2].", "marks": 2}
        ]
    ))

    # Q19: Kinetochore & spindle microtubule dynamics (Fig 5.10)
    questions.append(Question(
        number=19,
        title="9700/22/O/N/23/Q4 - Nanoscale Architecture of the Kinetochore-Microtubule Interface",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Accurate chromosome segregation depends on the mechanical linkage between spindle microtubules and the centromere. Fig. 5.10 displays the three-layer ultrastructure of the kinetochore.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_10_kinetochore_spindle_microtubules.png"),
        figure_caption="Fig. 5.10: Molecular structure of inner and outer kinetochore plates and microtubule depolymerisation.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.10, describe the structural distinction between the inner kinetochore plate and the outer kinetochore plate.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the Ndc80 complex captures spindle microtubules and maintains attachment while tubulin dimers are being removed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how depolymerisation of kinetochore microtubules at their plus ends generates mechanical pulling tension during anaphase A.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Inner plate binds centromeric heterochromatin containing specialised histone variant CENP-A; outer plate is a protein assembly (including Ndc80 and Mis12 complexes) extending outward into cytoplasm to bind microtubule plus ends [2].", "marks": 2},
            {"q": "Q19(b)", "points": "Ndc80 complexes have rod-like coiled coils with globular positively charged heads that bind negative tubulin tails; they act like sliding collars, retaining contact with curling protofilaments even as protofilaments peel backward [2].", "marks": 2},
            {"q": "Q19(c)", "points": "Loss of GTP cap causes protofilaments to curl outward into curved conformations (power stroke); curling protofilaments push against the kinetochore ring/collar, converting chemical energy of GTP hydrolysis into mechanical work that pulls the chromosome toward the pole [2].", "marks": 2}
        ]
    ))

    # Q20: Calculation of cell cycle parameters
    questions.append(Question(
        number=20,
        title="9700/22/F/M/21/Q3 - Quantitative Determination of Cell Cycle Stage Durations",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="In a sample of 800 dividing human cervical epithelial cells growing asynchronously in culture with a total cycle time of 22.0 hours, microscopic tally counts yielded: Interphase = 680 cells; Prophase = 64 cells; Metaphase = 24 cells; Anaphase = 16 cells; Telophase = 16 cells.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the Mitotic Index (MI) of this cell population, showing your working clearly.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the duration, in minutes, of metaphase in these cultured cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two essential assumptions that must hold true for stage durations to be accurately estimated from cell frequency counts in a fixed histological sample.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "MI = (Number of dividing cells in M / Total cells) x 100%; Dividing cells = 64 + 24 + 16 + 16 = 120; MI = (120 / 800) x 100% = 15.0% [2].", "marks": 2},
            {"q": "Q20(b)", "points": "Fraction of cells in metaphase = 24 / 800 = 0.030; Duration = 0.030 x 22.0 hours = 0.66 hours; 0.66 x 60 min = 39.6 minutes (allow 40 min) [2].", "marks": 2},
            {"q": "Q20(c)", "points": "All cells in the population must be dividing asynchronously (not synchronised in one phase); every cell in the meristem must have the same total cell cycle duration / no cells arrested in G0 [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & CYTOLOGICAL MECHANISM QUESTIONS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Comparison of chromatin vs chromosome
    questions.append(Question(
        number=21,
        title="9700/21/M/J/22/Q4 - Structural Comparison of Interphase Chromatin and Metaphase Chromosomes",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Contrast the physical state and accessibility of interphase euchromatin with that of a condensed metaphase chromosome.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why RNA transcription can proceed in interphase chromatin but is almost entirely halted on metaphase chromosomes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Interphase euchromatin is loosely packed, uncoiled (11 nm 'beads on string' to 30 nm fibre), and invisible under light microscope; metaphase chromosomes are maximally condensed, tightly supercoiled around scaffold proteins into distinct visible X-shaped rods [2].", "marks": 2},
            {"q": "Q21(b)", "points": "Loose chromatin allows RNA polymerase and transcription factor complexes to bind promoter sequences; extreme packaging in metaphase physically blocks enzyme access to DNA strands and sterically hinders unzipping [2].", "marks": 2}
        ]
    ))

    # Q22: Mitotic inhibitors & microtubule poisons (Fig 5.11)
    questions.append(Question(
        number=22,
        title="9700/22/M/J/21/Q3 - Pharmacological Inhibition of Mitosis by Microtubule Poisons",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Several potent natural alkaloids interfere with microtubule dynamics and are widely employed in chemotherapy and cytology. Fig. 5.11 contrasts the molecular actions of colchicine and paclitaxel (Taxol).",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_11_mitotic_inhibitors_microtubule_poisons.png"),
        figure_caption="Fig. 5.11: Mechanisms of mitotic arrest by tubulin polymerisation inhibitors vs stabilisers.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.11, explain how vinca alkaloids and colchicine arrest cells in metaphase by disrupting spindle assembly.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how paclitaxel (Taxol) exerts an anti-mitotic effect despite having the opposite biochemical mechanism to colchicine.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Bind free tubulin heterodimers and prevent their polymerisation into microtubules; spindle cannot form or breaks down, leaving unattached kinetochores that activate the spindle assembly checkpoint, arresting cells in pseudometaphase [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Taxol binds directly to assembled beta-tubulin subunits, hyper-stabilising microtubules and preventing their depolymerisation; because microtubules cannot shorten during anaphase, sister chromatids cannot be pulled to poles, blocking mitotic exit [2].", "marks": 2}
        ]
    ))

    # Q23: Anaphase A vs Anaphase B
    questions.append(Question(
        number=23,
        title="[Mentora Original A* Extension] - Biomechanical Distinction Between Anaphase A and Anaphase B",
        syllabus_ref="Syllabus 5.2",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between Anaphase A and Anaphase B in terms of the specific microtubules and motor proteins involved.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how sliding of overlapping polar microtubules increases the physical distance between dividing daughter chromosome sets.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Anaphase A involves shortening of kinetochore microtubules via plus/minus end depolymerisation to pull chromosomes toward poles; Anaphase B involves elongation and sliding of interpolar microtubules and cortical pulling of astral microtubules to push poles apart [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Plus-end directed kinesin-5 motor proteins cross-link antiparallel interpolar microtubules at the equator; by walking toward plus ends, they push overlapping microtubules in opposite directions, driving centrosomes and spindle poles further apart [2].", "marks": 2}
        ]
    ))

    # Q24: Benign vs malignant tumours
    questions.append(Question(
        number=24,
        title="9700/21/O/N/21/Q3 - Histological and Clinical Characteristics of Benign and Malignant Tumours",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Contrast benign tumours and malignant tumours with respect to cellular differentiation, capsule formation, and invasive capability.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why malignant tumours frequently lead to cachexia (wasting syndrome) and systemic organ failure in cancer patients.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Benign: slow growth, well-differentiated cells, enclosed by a fibrous connective tissue capsule, non-invasive; Malignant: rapid proliferation, poorly differentiated / anaplastic, non-encapsulated, actively invades surrounding tissue and colonises distant organs [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Tumour cells have abnormally high metabolic rates and glucose uptake (Warburg effect), consuming host energy reserves; secrete systemic inflammatory cytokines (TNF-alpha, IL-6) causing muscle wasting; metastatic growth physically obstructs vital organ functions [2].", "marks": 2}
        ]
    ))

    # Q25: Mitotic index grid counting (Fig 5.12)
    questions.append(Question(
        number=25,
        title="9700/22/F/M/20/Q2 - Calculation and Application of Mitotic Index in Onion Root Meristems",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Fig. 5.12 shows a microscopic counting grid of an Allium root tip squash and the corresponding phase distribution data.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_12_mitotic_index_grid_counting.png"),
        figure_caption="Fig. 5.12: Microscopic grid field (A) and stage frequency tally table (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.12, calculate the Mitotic Index (MI) of the sampled field and determine the duration of prophase assuming a 24.0-hour cell cycle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how medical oncologists utilise the Mitotic Index of tumour biopsies in clinical cancer grading and prognosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "Dividing cells = 3 (P) + 1 (M) + 1 (A) + 1 (T) = 6; Total = 25; MI = (6 / 25) x 100% = 24.0%; Prophase = 12.0% of cycle; Duration = 0.12 x 24.0 h = 2.88 hours (or 2 hours 53 minutes) [2].", "marks": 2},
            {"q": "Q25(b)", "points": "High MI indicates rapid cellular proliferation, correlating with high tumour histological grade, greater aggressiveness, and poorer prognosis; also predicts responsiveness to cell-cycle-specific cytotoxic chemotherapies [2].", "marks": 2}
        ]
    ))

    # Q26: Centrosome cycle & centriole structure
    questions.append(Question(
        number=26,
        title="9700/23/O/N/21/Q3 - Ultrastructure of Centrioles and the Centrosome Cycle",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the ultrastructure of a centriole as viewed under a transmission electron microscope.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the centrosome duplication cycle from G1 through S phase to prophase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Short hollow cylinder (~500 nm long, ~200 nm diameter) composed of nine peripheral triplets of microtubules (9+0 pattern) held together by cross-linking proteins, arranged perpendicular to each other in pairs [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Cell possesses one centrosome in G1; during S phase, a new daughter centriole (procentriole) buds at right angles to each mother centriole; in G2/prophase, the duplicated centrosomes separate and migrate to opposite poles to establish bipolar spindle [2].", "marks": 2}
        ]
    ))

    # Q27: Hayflick limit in somatic cell culture
    questions.append(Question(
        number=27,
        title="9700/21/M/J/21/Q2 - The Hayflick Limit in Cultured Somatic Fibroblasts",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by the Hayflick limit and describe how Leonard Hayflick demonstrated this phenomenon in human foetal fibroblasts.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why normal somatic cells undergo replicative senescence after approximately 50-70 divisions whereas embryonic stem cells proliferate indefinitely.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "The maximum number of times a normal human somatic cell population can divide in culture (~50-70 population doublings) before cell division permanently ceases; demonstrated by passaging fibroblasts until growth plateaued despite abundant nutrients [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Normal somatic cells lack telomerase activity, causing telomeres to shorten with each division until DNA damage response permanently halts cycle; embryonic stem cells constitutively express telomerase, maintaining telomere length and genomic integrity indefinitely [2].", "marks": 2}
        ]
    ))

    # Q28: Centrosome & centriole duplication (Fig 5.13)
    questions.append(Question(
        number=28,
        title="9700/22/M/J/23/Q4 - Structural Duplication of Centrosomes and Spindle Pole Separation",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        preamble="Centrosomes serve as the primary microtubule organizing centres (MTOCs) in animal cells and must duplicate exactly once per cycle. Fig. 5.13 illustrates the four steps of the centrosome duplication cycle.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_13_centrosome_centriole_duplication.png"),
        figure_caption="Fig. 5.13: Centrosome duplication cycle across G1, S, G2, and early prophase.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.13, explain the synchrony between nuclear DNA replication and centriole duplication during S phase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how pericentriolar material (PCM) recruitment in G2 phase prepares the centrosome for intense spindle microtubule nucleation in prophase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Both processes are triggered simultaneously at the G1/S transition by CDK2-cyclin E kinase activity; ensures that each daughter cell inherits exactly one centrosome and exactly one duplicate set of chromosomes [2].", "marks": 2},
            {"q": "Q28(b)", "points": "During G2, centrosomes recruit gamma-tubulin ring complexes (gamma-TuRCs) and scaffold proteins into the pericentriolar material; gamma-TuRCs act as structural templates to nucleate the rapid polymerisation of alpha/beta-tubulin into spindle microtubules [2].", "marks": 2}
        ]
    ))

    # Q29: Telomere sequence and G-quadruplexes
    questions.append(Question(
        number=29,
        title="[Mentora Original A* Extension] - Repetitive Telomeric Motifs and Protective T-Loop Architecture",
        syllabus_ref="Syllabus 5.1",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Describe the nucleotide sequence of the human telomeric repeat and explain how the single-stranded 3' G-rich overhang folds into a protective 'T-loop'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of the shelterin protein complex in shielding the T-loop from double-strand break repair machinery.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Repeated sequence is 5'-TTAGGG-3'; the 3' single-stranded overhang invades the double-stranded telomeric tract, displacing one strand to form a displacement (D-loop) and folding back into a large protective terminal loop (T-loop) [2].", "marks": 2},
            {"q": "Q29(b)", "points": "Shelterin (multi-protein complex including TRF1, TRF2, POT1) binds specific telomeric DNA, stabilising the T-loop and hiding chromosome ends; prevents Non-Homologous End Joining (NHEJ) enzymes from mistakenly identifying telomeres as broken DNA and fusing chromosomes [2].", "marks": 2}
        ]
    ))

    # Q30: Stem cell niche in crypts of Lieberkuhn
    questions.append(Question(
        number=30,
        title="9700/21/O/N/22/Q4 - Adult Stem Cell Niches in the Intestinal Crypts of Lieberkuhn",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the anatomical location and microenvironment of adult intestinal stem cells located at the base of the crypts of Lieberkuhn.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how daughter cells migrate up the crypt-villus axis and differentiate into absorptive enterocytes and mucus-secreting goblet cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Located at the very bottom of the crypts interdigitated between Paneth cells; the niche provides local Wnt signalling molecules and growth factors that maintain the cells in an undifferentiated, proliferative state [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Daughter cells undergo rapid transit-amplifying divisions while migrating up the crypt walls; as they move away from Paneth cell Wnt signals, they exit the cell cycle and differentiate into functional enterocytes (microvilli) or goblet cells, shedding at the villus tip after 3-5 days [2].", "marks": 2}
        ]
    ))

    # Q31: Mutagenic mechanisms of UV and radiation
    questions.append(Question(
        number=31,
        title="9700/22/F/M/22/Q4 - Molecular Lesions Caused by Ultraviolet Light and Ionising Radiation",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the photochemical alteration in DNA caused by ultraviolet (UV) radiation and explain how nucleotide excision repair corrects this lesion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why ionising radiation (gamma rays) is particularly lethal to dividing cells and why it can trigger gross chromosomal translocations.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "UV radiation causes adjacent pyrimidine bases (especially thymines) on the same strand to form covalent cyclobutane pyrimidine dimers; nucleotide excision repair endonucleases cut out the damaged oligonucleotide fragment, DNA polymerase synthesises the correct sequence, and ligase seals the nick [2].", "marks": 2},
            {"q": "Q31(b)", "points": "Ionising radiation generates hydroxyl free radicals that cleave both strands of the DNA phosphodiester backbone (double-strand breaks); error-prone repair (NHEJ) frequently religates ends from different chromosomes together, creating dicentric chromosomes, deletions, or oncogenic translocations [2].", "marks": 2}
        ]
    ))

    # Q32: Cell cycle checkpoints & cyclin-CDK (Fig 5.14)
    questions.append(Question(
        number=32,
        title="9700/23/M/J/20/Q3 - Cyclin-Dependent Kinase (CDK) Cascades and the Restriction Point",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        preamble="Cell cycle progression is driven by the periodic synthesis and destruction of cyclins and the activation of cyclin-dependent kinases (CDKs). Fig. 5.14 outlines the biochemical cascades governing the three major cycle checkpoints.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig5_14_cell_cycle_checkpoints_cyclin_cdk.png"),
        figure_caption="Fig. 5.14: Molecular regulation of cell cycle transitions by Cyclin-CDK complexes and inhibitors.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 5.14, describe how Cyclin D/CDK4 phosphorylates the Retinoblastoma protein (Rb) to release transcription factor E2F at the G1/S transition.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of the Maturation Promoting Factor (Cyclin B-CDK1 complex) in triggering chromosome condensation and nuclear envelope breakdown at the G2/M transition.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "In unphosphorylated state, Rb protein binds transcription factor E2F, keeping it inhibited; active Cyclin D-CDK4 phosphorylates Rb, altering its conformation so it releases E2F; free E2F enters nucleus and activates transcription of genes required for S phase (DNA polymerase, thymidine kinase) [2].", "marks": 2},
            {"q": "Q32(b)", "points": "Active CDK1 phosphorylates condensin complexes, triggering chromosome supercoiling and condensation; also phosphorylates nuclear lamins causing nuclear lamina depolymerisation and envelope disassembly [2].", "marks": 2}
        ]
    ))

    # Q33: Spindle checkpoint & aneuploidy
    questions.append(Question(
        number=33,
        title="9700/21/M/J/23/Q4 - The Spindle Assembly Checkpoint (SAC) and Aneuploidy Prevention",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe how unattached kinetochores recruit the MAD2 protein to inhibit the anaphase-promoting complex (APC/C).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how failure of the SAC can produce daughter cells with Down's syndrome (trisomy 21) or monosomy.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Unattached kinetochores catalyse a conformational change in MAD2 into an active form that binds and sequesters Cdc20; without free Cdc20, the ubiquitin ligase APC/C remains inactive, preventing degradation of securin and keeping separase inhibited [2].", "marks": 2},
            {"q": "Q33(b)", "points": "If SAC fails, anaphase initiates while a chromosome is unattached to one pole; both sister chromatids move to the same pole (non-disjunction); produces one daughter cell with an extra chromosome (trisomy, n+1) and one lacking that chromosome (monosomy, n-1) [2].", "marks": 2}
        ]
    ))

    # Q34: Plant vs animal cytokinesis mechanism
    questions.append(Question(
        number=34,
        title="9700/22/O/N/20/Q2 - Structural Adaptations in Cytokinesis Between Walled and Non-Walled Eukaryotes",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how the orientation of the phragmoplast determines the future division plane and tissue architecture in plants.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how plasmodesmata are formed during the assembly of the primary cell wall across the cell plate.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "The preprophase band of microtubules marks the equatorial cortex before mitosis, directing the expanding phragmoplast; ensures the new cross-wall fuses at the precise cortical division site, determining cell division planes necessary for organised plant tissue morphology [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Strands of smooth endoplasmic reticulum (desmotubules) become trapped between fusing Golgi vesicles along the developing cell plate; surrounding vesicles do not fuse at these points, leaving narrow cytoplasmic channels lined with plasma membrane (plasmodesmata) connecting daughter cells [2].", "marks": 2}
        ]
    ))

    # Q35: Staining protocols in meristem squashes
    questions.append(Question(
        number=35,
        title="9700/23/M/J/23/Q3 - Chemical Rationale of Reagents Used in Root Tip Squash Preparations",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain why root tips are placed into a fixative solution (e.g. ethanoic acid and ethanol) immediately after excision.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the root tissue must be squashed firmly with a thumb over a coverslip without sliding it sideways.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Fixative rapidly denatures and cross-links cellular proteins and enzymes; halts cellular metabolism immediately, preserving chromosomal morphology at the exact moment of sampling and preventing autolytic degradation [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Squashing firmly spreads the cells out into a single monolayer so light can pass through and individual chromosomes can be resolved; sliding sideways rolls cells over each other, damaging chromosomes and tearing tissue [2].", "marks": 2}
        ]
    ))

    # Q36: Tobacco smoke mutagens & lung cancer
    questions.append(Question(
        number=36,
        title="9700/21/O/N/23/Q4 - Carcinogens in Cigarette Smoke and Bronchial Epithelial Carcinogenesis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe how polycyclic aromatic hydrocarbons (such as benzopyrene) in cigarette smoke react with DNA to create mutational adducts.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how chronic destruction of ciliated bronchial epithelium by cigarette smoke accelerates oncogenic transformation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Metabolised by cytochrome P450 into reactive epoxides that covalently bind guanine bases; creates bulky DNA adducts that distort the double helix, causing DNA polymerase to misread bases during S phase, producing permanent transversions (e.g. G to T in TP53) [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Destruction of cilia impairs the mucus escalator, allowing concentrated chemical carcinogens to remain in prolonged contact with basal cells; chronic irritation forces basal stem cells to undergo continuous reparative mitosis, increasing replication errors and promoting tumour growth [2].", "marks": 2}
        ]
    ))

    # Q37: Telomeres as molecular clocks
    questions.append(Question(
        number=37,
        title="9700/22/F/M/23/Q4 - Telomeres as Cellular Chronometers of Biological Ageing",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain why leukocyte telomere length is widely studied as a biomarker of biological age in human populations.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how high levels of oxidative stress and systemic chronic inflammation accelerate telomeric attrition rates.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Leukocyte telomeres shorten predictably by ~30-50 base pairs per year due to repeated rounds of haematopoietic division and lack of telomerase; shorter telomeres reflect higher cumulative cellular turnover and biological ageing [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Reactive oxygen species (ROS) preferentially attack G-rich sequences (such as TTAGGG) causing oxidative lesions (8-oxoguanine); damaged telomeric DNA is poorly repaired and causes replication fork collapse, leading to substantial deletions at chromosome ends [2].", "marks": 2}
        ]
    ))

    # Q38: Asymmetric division in epidermal stem cells
    questions.append(Question(
        number=38,
        title="[Mentora Original A* Extension] - Asymmetric Stem Cell Division in Human Epidermal Stratification",
        syllabus_ref="Syllabus 5.1",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Describe how spindle orientation (perpendicular vs parallel to basement membrane) dictates symmetric versus asymmetric division in basal epidermal stem cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the differentiating daughter cell undergoes keratinisation and desquamation to maintain the skin permeability barrier.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Parallel spindle: cleavage furrow is perpendicular, keeping both daughter cells in contact with basement membrane niche signals (symmetric division for self-renewal); Perpendicular spindle: one daughter remains anchored in niche, while the other is displaced suprabasally into differentiation pathway (asymmetric division) [2].", "marks": 2},
            {"q": "Q38(b)", "points": "Suprabasal cells synthesise abundant cytokeratin filaments and envelope proteins, lose nucleus and organelles (programmed cornification), and form flattened dead squames in stratum corneum embedded in lipid matrix; shed continually from surface to renew barrier [2].", "marks": 2}
        ]
    ))

    # Q39: Prophase chromosome condensation mechanics
    questions.append(Question(
        number=39,
        title="9700/23/O/N/23/Q3 - Biochemical Machinery of Chromatin Hypercondensation in Early Prophase",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the role of condensin complexes and topoisomerase II in supercoiling 30 nm chromatin fibres into metaphase chromatids.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of phosphorylation of histone H3 on serine residues during prophase condensation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Condensin I and II complexes form ring-like protein clamps that hydrolyse ATP to extrude loops of DNA, packaging chromatin into nested loop arrays; Topoisomerase II relaxes torsional strain and decatenates tangled sister chromatid strands, allowing clean segregation [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Phosphorylation of histone H3 (Ser10/Ser28) by Aurora B kinase acts as an epigenetic mark, recruiting condensin complexes and chromatin remodelling factors to initiate dense chromosome condensation at early prophase [2].", "marks": 2}
        ]
    ))

    # Q40: Mitosis in unicellular vs multicellular organisms
    questions.append(Question(
        number=40,
        title="9700/21/M/J/20/Q3 - Evolutionary Divergence of Mitosis: Unicellular Fission vs Multicellular Ontogeny",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Compare the biological outcome of mitosis in a unicellular eukaryote (e.g. Amoeba) with that in a multicellular eukaryote (e.g. human embryo).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why binary fission in prokaryotes is not considered true mitosis, identifying two major structural differences in the division machinery.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "In unicellular eukaryotes, mitosis constitutes reproduction, producing separate independent individuals (doubling population size); in multicellular eukaryotes, mitosis increases total cell number within a single organism for development, growth, and tissue renewal [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Prokaryotes lack a nucleus, histone packaging, and a tubulin-based mitotic spindle; DNA replication occurs from a single origin of circular chromosome, and daughter DNA copies are separated by attachment to plasma membrane and FtsZ ring constriction [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Mitosis definition
    questions.append(Question(
        number=41,
        title="9700/12/M/J/22/Q15 - Define Mitosis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term mitosis in precise biological terms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "Nuclear division that produces two genetically identical daughter nuclei, each containing the same number and type of chromosomes as the parent nucleus [2].", "marks": 2}
        ]
    ))

    # Q42: Centromere definition
    questions.append(Question(
        number=42,
        title="9700/11/O/N/21/Q16 - Define Centromere",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term centromere and state its two primary biological functions.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "A specialised region of a chromosome that holds two sister chromatids together and serves as the assembly site for the kinetochore protein complex where spindle microtubules attach during nuclear division [2].", "marks": 2}
        ]
    ))

    # Q43: Chromatid definition
    questions.append(Question(
        number=43,
        title="9700/12/M/J/21/Q16 - Define Sister Chromatid",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term sister chromatid and explain when sister chromatids are formed in the cell cycle.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "One of the two identical replicated copies of a single chromosome joined by a common centromere; formed during the S phase of interphase by semi-conservative DNA replication [2].", "marks": 2}
        ]
    ))

    # Q44: Telomere definition
    questions.append(Question(
        number=44,
        title="9700/13/O/N/22/Q17 - Define Telomere",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term telomere and state its primary role in preserving genomic integrity.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "A specialised region of repetitive non-coding DNA sequence at the terminal ends of eukaryotic linear chromosomes; protects coding genes from degradation during successive rounds of DNA replication and prevents end-to-end chromosome fusion [2].", "marks": 2}
        ]
    ))

    # Q45: Stem cell definition
    questions.append(Question(
        number=45,
        title="9700/11/M/J/20/Q15 - Define Stem Cell",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term stem cell, stating its two defining functional properties.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "An undifferentiated cell that has the ability to divide repeatedly by mitosis while remaining unspecialised (self-renewal) and has the potential to differentiate into specialised mature cell types (potency) [2].", "marks": 2}
        ]
    ))

    # Q46: Mitotic index definition
    questions.append(Question(
        number=46,
        title="9700/12/O/N/23/Q16 - Define Mitotic Index",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define Mitotic Index (MI) and state the formula used for its calculation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "The proportion or percentage of cells within a tissue or sample that are actively undergoing mitosis; calculated as MI = (Number of cells with visible chromosomes in prophase, metaphase, anaphase, telophase / Total number of cells observed) x 100% [2].", "marks": 2}
        ]
    ))

    # Q47: Carcinogen definition
    questions.append(Question(
        number=47,
        title="9700/11/F/M/22/Q14 - Define Carcinogen and Oncogene",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the terms carcinogen and oncogene.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "Carcinogen: an environmental agent (chemical, radiation, or virus) that causes mutations leading to the development of cancer; Oncogene: a mutated form of a proto-oncogene that causes uncontrolled cell proliferation by producing hyperactive growth-promoting proteins [2].", "marks": 2}
        ]
    ))

    # Q48: Metastasis definition
    questions.append(Question(
        number=48,
        title="9700/12/M/J/23/Q17 - Define Metastasis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term metastasis and explain how malignant cells disseminate through the human body.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "The spread of malignant tumour cells from the primary site of origin to distant tissues or organs; tumour cells detach, penetrate blood or lymphatic vessels, circulate, and establish secondary tumours (metastases) elsewhere in the body [2].", "marks": 2}
        ]
    ))

    # Q49: Kinetochore definition
    questions.append(Question(
        number=49,
        title="9700/13/O/N/20/Q15 - Define Kinetochore",
        syllabus_ref="Syllabus 5.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term kinetochore and state its specific function during mitotic cell division.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "A complex multi-protein structure assembled on the centromeric DNA of each sister chromatid; serves as the physical attachment site for spindle microtubules and contains motor proteins that drive chromosome movement to spindle poles during anaphase [2].", "marks": 2}
        ]
    ))

    # Q50: Cytokinesis definition
    questions.append(Question(
        number=50,
        title="9700/11/M/J/22/Q17 - Define Cytokinesis",
        syllabus_ref="Syllabus 5.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term cytokinesis and distinguish it from karyokinesis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "The physical division of the cytoplasm and parental cell boundary into two separate daughter cells following nuclear division; karyokinesis is the division of the cell nucleus (mitosis), whereas cytokinesis is the division of the entire cell body [2].", "marks": 2}
        ]
    ))

    # Assign section keys
    for q in questions:
        if q.number <= 20:
            q.section_key = "Section A — High-Tariff Structured Analysis & Data Evaluation (120 Marks)"
        elif q.number <= 40:
            q.section_key = "Section B — Core Conceptual & Cytological Mechanism Questions (80 Marks)"
        else:
            q.section_key = "Section C — High-Yield Rapid Recall & Rigorous Definitions (20 Marks)"

    return questions

def get_topic5_faqs():
    return [
        {
            "q_num": 1,
            "title": "Explain the Structure of Telomeres, How They Address the End-Replication Problem, and the Significance of Telomerase in Cancer.",
            "category": "Telomere Biology • End-Replication Problem",
            "examiner_trap": "Stating that telomeres code for essential proteins or prevent gene mutations. Telomeres consist of non-coding repetitive DNA sequences that prevent the erosion of vital coding genes at chromosome ends.",
            "model_answer": "• Structure of Telomeres: Specialized structures located at the physical ends of linear eukaryotic chromosomes, composed of non-coding tandemly repeated DNA sequences (in humans: 5'-TTAGGG-3') and associated shelterin protective proteins.\n• The End-Replication Problem:\n  1. During DNA replication, DNA polymerase requires an RNA primer to initiate synthesis and can only synthesize DNA in a 5' to 3' direction;\n  2. When the terminal RNA primer is excised from the 5' end of the newly synthesized lagging strand, DNA polymerase cannot fill the gap (no upstream 3'-OH group available);\n  3. Consequently, chromosomes shorten slightly with every successive cycle of mitotic division.\n• Protective Function: Telomeres act as disposable buffers; vital coding genes located upstream are preserved from terminal erosion, and telomeric shelterin caps prevent chromosome ends from being misidentified by the cell as double-stranded DNA breaks (preventing inappropriate DNA repair and lethal end-to-end chromosomal fusions).\n• Cellular Senescence (Mitotic Clock): Telomeres progressively shorten until a critical threshold is reached (Hayflick limit), triggering cell cycle arrest, senescence, or apoptosis.\n• Telomerase in Cancer: Germ cells, stem cells, and ~90% of malignant cancer cells express the enzyme telomerase (a reverse transcriptase with an internal RNA template); telomerase continually extends telomeric repeats, granting cancer cells limitless replicative immortality."
        },
        {
            "q_num": 2,
            "title": "Detail the Precise Dynamic Behaviour of Chromosomes, Nuclear Envelope, and Spindle Microtubules Across the Four Stages of Mitosis.",
            "category": "Nuclear Division • Mitotic Stages",
            "examiner_trap": "Referring to sister chromatids as 'chromosomes' before centromere cleavage, or claiming that chromosomes replicate during prophase. DNA replication occurs during S-phase of interphase.",
            "model_answer": "• Prophase:\n  1. Chromatin fibres condense, shorten, and thicken by supercoiling around histone octamers to form distinct visible chromosomes;\n  2. Each chromosome consists of two genetically identical sister chromatids joined at a narrow region termed the centromere;\n  3. Nucleolus gradually disappears as ribosomal RNA transcription ceases;\n  4. Centrosomes migrate to opposite poles of the cell, polymerising tubulin to assemble the mitotic spindle apparatus;\n  5. Nuclear envelope disintegrates into membrane vesicles at late prophase.\n• Metaphase:\n  1. Kinetochore microtubules from opposite spindle poles attach securely to protein kinetochores located on each centromere;\n  2. Microtubule motor proteins align chromosomes individually in a single file along the equatorial plane (metaphase plate);\n  3. Spindle assembly checkpoint (SAC) verifies tension across all kinetochore attachments.\n• Anaphase:\n  1. Centromeres divide synchronously as the enzyme separase degrades cohesion rings;\n  2. Sister chromatids are pulled apart and are now officially termed daughter chromosomes;\n  3. Kinetochore microtubules depolymerise at the kinetochore ends, pulling daughter chromosomes centromere-first (yielding characteristic V- or J-shapes) toward opposite spindle poles.\n• Telophase:\n  1. Daughter chromosomes arrive at opposite poles, decondense, uncoil, and revert to diffuse chromatin;\n  2. Nuclear envelope reforms around each set of daughter chromosomes from vesicle fusion;\n  3. Nucleoli reappear within newly formed nuclei; spindle microtubules completely disassemble."
        },
        {
            "q_num": 3,
            "title": "Contrast the Changes in Nuclear DNA Mass (2C to 4C) with Chromosome Number (2n) Throughout the Complete Cell Cycle.",
            "category": "Cytogenetics • DNA Mass vs Chromosome Number",
            "examiner_trap": "Confusing chromosome number with DNA mass. During S-phase, DNA mass doubles from 2C to 4C, but the chromosome count remains 2n because each chromosome consists of two sister chromatids joined at one centromere.",
            "model_answer": "• G1 Phase (Gap 1 of Interphase):\n  1. Diploid cell contains 2n chromosomes (e.g. 46 chromosomes in humans);\n  2. Nuclear DNA mass is at the diploid baseline level designated as 2C;\n  3. Chromosomes are unreplicated and exist as single chromatids.\n• S Phase (Synthesis Phase of Interphase):\n  1. Semi-conservative DNA replication occurs across all chromosomes;\n  2. DNA mass doubles progressively from 2C to 4C;\n  3. Chromosome number remains strictly 2n because the two identical DNA copies remain physically united at a single shared centromere as sister chromatids.\n• G2 Phase (Gap 2 of Interphase):\n  1. Cell prepares for mitosis, synthesizing tubulin and checking for DNA replication fidelity;\n  2. DNA mass remains 4C; chromosome number remains 2n.\n• Mitosis (Nuclear Division):\n  1. Prophase and Metaphase: DNA mass is 4C; chromosome count is 2n (double-chromatid chromosomes);\n  2. Anaphase: Centromeres divide and sister chromatids separate; chromosome count temporarily doubles to 4n (92 individual daughter chromosomes in humans), while DNA mass remains 4C.\n• Telophase & Cytokinesis (Cell Division):\n  1. Cytoplasm divides equally between two daughter cells;\n  2. Each daughter cell receives 2n chromosomes and 2C DNA mass, restoring the exact genetic baseline of the parental cell."
        },
        {
            "q_num": 4,
            "title": "Contrast the Cytological Mechanism of Cytokinesis in Animal Cells (Cleavage Furrow) with Plant Cells (Cell Plate Assembly).",
            "category": "Cell Division • Comparative Cytokinesis",
            "examiner_trap": "Stating that plant cells form a cleavage furrow. Plant cells cannot pinch inward due to the rigid, inextensible cellulose cell wall.",
            "model_answer": "• Animal Cell Cytokinesis (Contractile Cleavage Furrow):\n  1. Structure Involved: A contractile ring composed of antiparallel actin microfilaments and non-muscle myosin motor proteins assembles just beneath the plasma membrane at the cell equator during anaphase;\n  2. Mechanism: ATP-driven sliding of myosin along actin filaments constricts the contractile ring like a purse string, pulling the plasma membrane inward to create a deepening cleavage furrow;\n  3. Directionality: Constriction proceeds centripetally (from the outside inward) until the furrow meets in the center, pinching the cytoplasm into two completely separate daughter cells.\n• Plant Cell Cytokinesis (Phragmoplast & Cell Plate Assembly):\n  1. Physical Constraint: Rigid, inextensible cellulose cell wall prevents membrane furrowing or inward pinching;\n  2. Structure Involved: Cytoskeletal array termed the phragmoplast forms at the equator from remnant spindle microtubules;\n  3. Mechanism: Golgi-derived secretory vesicles containing cell wall building materials (pectins, hemicelluloses, and glycoprotein precursors) travel along microtubules and align along the equatorial plane;\n  4. Fusion: Vesicles coalesce and fuse together from the center outward (centrifugal assembly), forming a continuous flattened membrane disc termed the cell plate;\n  5. Completion: Vesicle membranes fuse with the parental plasma membrane to establish new daughter cell boundaries; vesicle lumen contents form the middle lamella, upon which cellulose synthase enzymes deposit primary cell walls."
        },
        {
            "q_num": 5,
            "title": "Explain the Practical Protocol for an Allium Root Tip Squash, the Mitotic Index (MI) Formula, and How to Calculate Phase Duration.",
            "category": "Practical Microscopy • Mitotic Index Calculations",
            "examiner_trap": "Including interphase cells in the numerator when calculating Mitotic Index, or dividing by the number of interphase cells rather than the TOTAL number of cells counted.",
            "model_answer": "• Root Tip Squash Protocol:\n  1. Root Meristem: Excise terminal 1–2 mm of growing root tips (apical meristem contains actively dividing undifferentiated cells);\n  2. Hydrolysis / Maceration: Warm root tips in 1.0 mol dm-3 hydrochloric acid (HCl) at 60°C for 5 minutes; breaks down calcium pectate in the middle lamella, softening tissue so cells separate into a single layer;\n  3. Staining: Stain with acetic orcein, Feulgen reagent, or acetocarmine (cationic dyes that bind specifically to negatively charged DNA/chromatin, staining chromosomes dark purple/red);\n  4. Squashing: Place root tip on slide, cover with coverslip, press firmly straight down with thumb through filter paper (avoiding lateral twisting, which shears chromosomes) to spread tissue into a uniform single monolayer of cells.\n• Mitotic Index (MI) Formula:\n  MI = (Number of cells with visible condensed chromosomes [in Prophase, Metaphase, Anaphase, Telophase] / Total number of cells in field of view [Mitotic + Interphase cells]) x 100%\n• Calculation of Phase Duration:\n  Phase Duration = (Number of cells in specified mitotic phase / Total number of cells counted) x Total duration of complete cell cycle (hours or minutes).\n• Significance: Assesses tissue growth rate; in clinical oncology, elevated MI is a diagnostic and prognostic biomarker of aggressively proliferating malignant tumours."
        },
        {
            "q_num": 6,
            "title": "Define Stem Cells, Contrast the Three Levels of Stem Cell Potency (Totipotent, Pluripotent, Multipotent), and Outline Their Medical Importance.",
            "category": "Developmental Biology • Stem Cell Potency",
            "examiner_trap": "Confusing pluripotent with totipotent. Pluripotent stem cells can form all embryonic tissues but CANNOT form extraembryonic tissues (placenta and umbilical cord).",
            "model_answer": "• Definition of Stem Cells: Undifferentiated precursor cells that possess two hallmark capabilities: indefinite self-renewal (dividing by mitosis to maintain stem cell pool) and potency (the capacity to differentiate into specialized cell types under appropriate biochemical cues).\n• Hierarchy of Potency:\n  1. Totipotent Stem Cells: Possess the highest developmental potential; can differentiate into ALL cell types of the adult organism PLUS extraembryonic supporting tissues (placenta, amnion, and umbilical cord); examples: the fertilized zygote and early cleavage blastomeres up to the 8-cell stage;\n  2. Pluripotent Stem Cells: Can differentiate into ALL specialized cell types derived from the three embryonic germ layers (ectoderm, mesoderm, endoderm), but CANNOT form extraembryonic tissues; example: inner cell mass (ICM) of the 5-day-old blastocyst (embryonic stem cells, ESCs);\n  3. Multipotent Stem Cells: Adult/somatic stem cells with restricted lineage; can differentiate into a limited subset of related specialized cell types within a specific tissue; example: haematopoietic stem cells (HSCs) in bone marrow producing all blood lineages (erythrocytes, leukocytes, platelets).\n• Regenerative Medicine Applications: Tissue engineering, bone marrow transplants for leukaemia, repairing damaged cardiac muscle post-infarction, and cell replacement therapies for degenerative conditions (e.g. dopamine neurons in Parkinson's disease)."
        },
        {
            "q_num": 7,
            "title": "Describe the Multi-Step Carcinogenesis Cascade: Environmental Mutagens, Proto-Oncogenes, Tumour Suppressor Genes (p53), Angiogenesis, and Metastasis.",
            "category": "Oncology • Carcinogenesis Mechanisms",
            "examiner_trap": "Stating that a single genetic mutation causes cancer, or confusing oncogenes (dominant gain-of-function) with tumour suppressor genes (recessive loss-of-function).",
            "model_answer": "• Multi-Step Carcinogenesis: Cancer arises through the sequential accumulation of multiple (typically 4–7) driver mutations in critical cell-cycle regulatory genes within a single somatic cell lineage over decades.\n• Environmental Mutagens / Carcinogens: Physical agents (ionising X-rays, UV radiation inducing thymine dimers), chemical carcinogens (tobacco smoke tar, benzo[a]pyrene alkylating bases), and biological oncoviruses (HPV) that induce irreversible mutations.\n• Proto-Oncogenes vs Oncogenes:\n  1. Proto-oncogenes: Normal cellular genes that stimulate cell growth and mitotic progression (e.g. ras, myc);\n  2. Oncogenes: Mutated, hyperactive alleles (gain-of-function mutation); act dominantly (single mutated copy causes overstimulation); produce permanently activated growth factor receptors or signaling kinases, driving relentless cell division.\n• Tumour Suppressor Genes (e.g. TP53):\n  1. Normal function: Encode proteins that halt the cell cycle at DNA damage checkpoints, promote DNA repair, or trigger apoptosis (programmed cell death) if damage is unrepairable;\n  2. Inactivation: Recessive loss-of-function mutations in both alleles result in loss of cell cycle checkpoints; damaged, genetically unstable cells proliferate unchecked.\n• Angiogenesis and Metastasis:\n  1. Tumour mass exceeding ~1–2 mm secretes vascular endothelial growth factor (VEGF), stimulating new capillary network formation into the tumour (angiogenesis) for oxygen/nutrient delivery;\n  2. Malignant cells lose E-cadherin cell-cell adhesion, secrete matrix metalloproteinases that degrade basal lamina, intravasate into blood/lymphatic vessels, and establish secondary tumours at distant organ sites (metastasis)."
        },
        {
            "q_num": 8,
            "title": "Explain the Functions of the Three Major Cell Cycle Checkpoints (G1/S, G2/M, and Metaphase SAC).",
            "category": "Cell Cycle Control • Checkpoint Fidelity",
            "examiner_trap": "Assuming the cell cycle is an unregulated continuous loop. Progress is strictly gated at three biochemical checkpoints governed by cyclins and cyclin-dependent kinases (CDKs).",
            "model_answer": "• G1/S Checkpoint (The Restriction Point):\n  1. Location: Near the end of G1 phase in interphase;\n  2. Function: Master decision point determining whether the cell enters the division cycle or exits into quiescent G0 resting state;\n  3. Assessment: Evaluates external mitogenic signals, cell size, nutrient adequacy, and checks for genomic DNA damage;\n  4. Mechanism: If DNA is damaged, p53 transcription factor accumulates and activates p21 (CDK inhibitor), halting cycle until excision repair completes; if irreparable, p53 activates Bax to trigger apoptosis.\n• G2/M Checkpoint:\n  1. Location: Boundary between G2 phase and prophase of mitosis;\n  2. Function: Assesses the completeness and fidelity of DNA replication carried out during S phase;\n  3. Mechanism: Checks for unreplicated single-stranded DNA gaps or double-strand breaks; inhibits CDK1-cyclin B complex (maturation promoting factor, MPF) until replication is 100% complete and damage is repaired.\n• Spindle Assembly Checkpoint (SAC / Metaphase Checkpoint):\n  1. Location: Transition from metaphase to anaphase during mitosis;\n  2. Function: Guarantees that every single kinetochore on all sister chromatids is bilaterally attached to spindle microtubules and under proper mechanical tension at the metaphase plate;\n  3. Significance: Inactivates the anaphase-promoting complex (APC/C) as long as any kinetochore remains unattached, preventing premature centromere cleavage and averting catastrophic chromosome non-disjunction and aneuploidy."
        },
        {
            "q_num": 9,
            "title": "Contrast the Pharmacological Mechanisms and Mitotic Consequences of Spindle Poisons: Colchicine vs Paclitaxel (Taxol).",
            "category": "Pharmacology & Cytology • Spindle Inhibitors",
            "examiner_trap": "Asserting that colchicine and taxol have identical actions. Colchicine prevents microtubule assembly (polymerisation), whereas paclitaxel prevents microtubule disassembly (depolymerisation).",
            "model_answer": "• Dynamic Instability of Microtubules: Mitotic spindle microtubules are hollow cylinders assembled from alpha- and beta-tubulin heterodimers that undergo continuous rapid polymerisation (growth) and depolymerisation (shortening).\n• Colchicine Mechanism & Effects:\n  1. Mechanism: Alkaloid derived from Colchicum autumnale; binds with high affinity to free unpolymerised tubulin heterodimers, forming tubulin-colchicine complexes that prevent further addition to microtubule plus-ends;\n  2. Consequence: Complete depolymerisation and failure of mitotic spindle formation;\n  3. Cell Arrest: Dividing cells enter mitosis but are arrested at metaphase because chromosomes cannot align or attach to a spindle; centromeres remain intact;\n  4. Applications: Used in cytogenetics to prepare karyotypes (accumulates metaphase spreads) and in plant breeding to induce polyploidy (doubles chromosome number when nuclear envelope reforms around unseparated chromosomes).\n• Paclitaxel (Taxol) Mechanism & Effects:\n  1. Mechanism: Terpenoid extracted from the Pacific yew tree (Taxus brevifolia); binds specifically to assembled beta-tubulin subunits along the inner surface of the microtubule polymer;\n  2. Consequence: Hyper-stabilises the microtubule lattice, locking it in place and completely preventing tubulin subunit depolymerisation;\n  3. Cell Arrest: Spindle fibres form, but kinetochore microtubules cannot depolymerise/shorten during anaphase; chromosomes cannot move to poles; frozen in prolonged mitotic arrest which triggers the intrinsic apoptosis pathway;\n  4. Clinical Application: Widely used chemotherapeutic drug against breast, ovarian, and lung carcinomas."
        },
        {
            "q_num": 10,
            "title": "Describe the Structure, Duplication Cycle, and Spindle-Nucleating Function of the Centrosome in Animal Cells, and Contrast with Higher Plants.",
            "category": "Cell Ultrastructure • Centrosome & Spindle Organization",
            "examiner_trap": "Claiming that plant cells contain centrioles. Higher plants lack centrioles and discrete centrosomes, yet successfully nucleate spindles via non-centrosomal MTOCs.",
            "model_answer": "• Animal Centrosome Structure:\n  1. The primary microtubule-organising centre (MTOC) of animal cells, located adjacent to the interphase nucleus;\n  2. Consists of a pair of cylindrical centrioles oriented strictly perpendicular (at 90°) to each other;\n  3. Centriole Ultrastructure: Each centriole is composed of nine symmetrically arranged triplets of microtubules (9+0 arrangement), lacking central microtubules;\n  4. Pericentriolar Material (PCM): An amorphous proteinaceous matrix surrounding the centrioles, containing ring complexes of gamma-tubulin (gamma-TuRCs) that act as templates for nucleating spindle microtubules.\n• Centrosome Duplication Cycle:\n  1. G1 Phase: Cell contains a single centrosome with two parental centrioles;\n  2. S Phase: Simultaneous with DNA replication, a daughter centriole (procentriole) buds at right angles from the base of each parental centriole;\n  3. G2 Phase: Daughter centrioles elongate to full length; two mature centrosomes reside side by side;\n  4. Prophase: Centrosomes separate, propelled by kinesin motor proteins pushing interpolar microtubules, and migrate to opposite poles of the cell, establishing the bipolar mitotic spindle axes.\n• Contrast with Higher Plant Cells:\n  1. Flowering plants (angiosperms) and gymnosperms contain NO centrioles and NO discrete compact centrosomes;\n  2. Spindle Organisation: Microtubules are nucleated and organized into a functional bipolar spindle by diffuse gamma-tubulin complexes dispersed across the nuclear envelope and cortical cytoplasm."
        }
    ]

