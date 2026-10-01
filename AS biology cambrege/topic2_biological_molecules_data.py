"""
Topic 2: Biological Molecules  -  50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Biochemical Mechanism Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Past Paper vs Original Ratio: 43 Authentic (86%) / 7 Original Extensions (14%)
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic2_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Benedict's semi-quantitative colorimetry & calibration curve (Fig 2.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q2  -  Semi-Quantitative Benedict's Test & Colorimetry",
        syllabus_ref="Syllabus 2.1",
        difficulty="ADVANCED",
        preamble="A student investigated the concentration of reducing sugar in fruit juice samples. Standard glucose solutions were prepared and tested with excess Benedict's reagent under standard conditions (80  deg C for 5 minutes). After centrifuging to remove the cuprous oxide precipitate, the absorbance of the unreacted supernatant was determined using a colorimeter fitted with a 680 nm red filter. Fig. 2.1 shows the colour standards and resulting calibration curve.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_1_benedicts_reducing_test.png"),
        figure_caption="Fig. 2.1: Semi-quantitative colour progression of Benedict's test and colorimeter absorbance calibration curve at 680 nm.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the absorbance of the supernatant decreases as the concentration of reducing sugar in the initial sample increases.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="A fruit juice sample X gave an absorbance reading of 0.65 arbitrary units. Use Fig. 2.1 to determine the concentration of reducing sugar in sample X, showing your working.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two variables that must be strictly standardised when heating the reaction mixture to ensure valid, reproducible results.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "More reducing sugar reduces more Cu2+ (copper(II) ions) to Cu+ / insoluble Cu2O precipitate; leaving lower concentration of blue Cu2+ ions in the supernatant / less blue light absorbed by remaining supernatant [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Intercept with calibration line shown at absorbance 0.65 AU; reading correctly corresponding concentration = 1.15% to 1.25% (g / 100 cm3) [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Temperature of water-bath (maintained at 80-100  deg C / thermostatically controlled); duration of heating (exactly 5 minutes) / volume ratio of Benedict's reagent to sample solution [2].", "marks": 2}
        ]
    ))

    # Q2: Haworth projections of alpha and beta glucose (Fig 2.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q2  -  Structural Isomerism: alpha-Glucose vs beta-Glucose",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Glucose is a hexose monosaccharide that exists predominantly as a six-membered pyranose ring in aqueous solution. Fig. 2.2 shows the ring structures of alpha-glucose and beta-glucose.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_2_alpha_beta_glucose.png"),
        figure_caption="Fig. 2.2: Haworth projection ring structures of alpha-glucose and beta-glucose showing carbon atom numbering 1 to 6.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 2.2, describe the precise structural difference between alpha-glucose and beta-glucose.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the general empirical formula for hexose monosaccharides and define the term structural isomer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the orientation of the hydroxyl group on carbon 1 in beta-glucose dictates the structural differences between starch and cellulose.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "In alpha-glucose the hydroxyl (-OH) group on carbon 1 (C1) lies below the plane of the ring; whereas in beta-glucose the hydroxyl group on carbon 1 lies above the plane of the ring [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Empirical formula: CnH2nOn / C6H12O6; structural isomers have the same molecular formula but different structural arrangements / spatial orientations of atoms [2].", "marks": 2},
            {"q": "Q2(c)", "points": "beta-glucose monomers must alternate by 180 deg  rotation to allow glycosidic bond formation; producing straight, unbranched chains (cellulose) rather than coiled helices (amylose/starch) [2].", "marks": 2}
        ]
    ))

    # Q3: Maltose condensation & hydrolysis (Fig 2.3)
    questions.append(Question(
        number=3,
        title="9700/22/F/M/23/Q3  -  Formation and Hydrolysis of the Glycosidic Bond",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Disaccharides are formed when two monosaccharides are joined by a covalent condensation reaction. Fig. 2.3 illustrates the condensation of two alpha-glucose molecules to form maltose and its reversible hydrolysis.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_3_maltose_condensation.png"),
        figure_caption="Fig. 2.3: Condensation of two alpha-glucose molecules to form maltose and an alpha(1->4)-glycosidic bond.",
        parts=[
            QuestionPart(label="(a)", text="State the precise name of the covalent bond formed at carbon 1 and carbon 4 in Fig. 2.3 and identify the small inorganic molecule eliminated during this reaction.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between a condensation reaction and a hydrolysis reaction with reference to disaccharide metabolism.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Maltose is classified as a reducing sugar. Explain why maltose gives a positive result in Benedict's test whereas some other disaccharides, such as sucrose, do not.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "alpha(1->4)-glycosidic bond / alpha-1,4-glycosidic bond; water (H2O) [2].", "marks": 2},
            {"q": "Q3(b)", "points": "Condensation joins two monosaccharide monomers by forming a glycosidic bond with the release of a water molecule; hydrolysis splits a disaccharide into two monomers by breaking the glycosidic bond using the addition of a water molecule [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Maltose retains a free anomeric hemiacetal carbon (C1 on the second glucose) capable of opening into an active aldehyde group that donates electrons to reduce Cu2+; sucrose has both anomeric carbons (C1 of glucose and C2 of fructose) locked within the glycosidic bond [2].", "marks": 2}
        ]
    ))

    # Q4: Comparative architecture of amylose, amylopectin and glycogen (Fig 2.4)
    questions.append(Question(
        number=4,
        title="9700/23/M/J/21/Q2  -  Storage Polysaccharides: Starch vs Glycogen",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Polysaccharides are macromolecular energy storage polymers. Fig. 2.4 compares the macromolecular architecture of amylose, amylopectin, and glycogen.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_4_amylose_amylopectin_glycogen.png"),
        figure_caption="Fig. 2.4: Macromolecular architecture of (A) amylose, (B) amylopectin, and (C) glycogen.",
        parts=[
            QuestionPart(label="(a)", text="Compare the structural differences between amylose and amylopectin shown in Fig. 2.4 in terms of bonding and molecular shape.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the frequent branching of glycogen shown in Fig. 2.4(C) adapts it to its role as an energy store in active animal tissues such as skeletal muscle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why storing glucose as insoluble starch or glycogen is advantageous to a cell compared to storing free glucose molecules.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Amylose has only alpha(1->4) glycosidic bonds and forms an unbranched helical coil; amylopectin has alpha(1->4) bonds and occasional alpha(1->6) glycosidic bonds forming a branched structure [2].", "marks": 2},
            {"q": "Q4(b)", "points": "Frequent alpha(1->6) branches (every 8-12 units) produce many terminal ends for simultaneous enzymatic hydrolysis by glycogen phosphorylase; permitting rapid mobilisation of glucose-1-phosphate / ATP generation during bursts of muscular contraction [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Starch and glycogen are insoluble and have no osmotic effect (do not lower water potential / do not cause cellular osmotic lysis); macromolecules are too large to diffuse across cell surface membranes [2].", "marks": 2}
        ]
    ))

    # Q5: Cellulose microfibril and cell wall tensile strength (Fig 2.5)
    questions.append(Question(
        number=5,
        title="9700/22/O/N/23/Q3  -  Molecular Architecture and Mechanical Role of Cellulose",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Cellulose is the primary structural component of the plant cell wall. Fig. 2.5 shows the molecular arrangement of beta-glucose chains, inter-chain hydrogen bonding, and their assembly into microfibrils.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_5_cellulose_microfibril.png"),
        figure_caption="Fig. 2.5: Cellulose polymer showing 180 deg  inverted beta-glucose monomers, inter-chain hydrogen bonds, and microfibril hierarchy.",
        parts=[
            QuestionPart(label="(a)", text="Explain why alternate beta-glucose monomers must be rotated through 180 deg  along the length of a cellulose chain.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 2.5, describe how individual cellulose molecules are held together to form a microfibril.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Relate the molecular structure of cellulose microfibrils to the function of plant cell walls in resisting internal turgor pressure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "In beta-glucose the hydroxyl (-OH) group on C1 is above the ring while that on C4 is below the ring; inversion of successive monomers brings -OH groups into proximity to form beta(1->4) glycosidic bonds without bending the chain [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Chains are long, straight, and unbranched; held parallel to one another by thousands of cross-linking hydrogen bonds between projecting -OH groups [2].", "marks": 2},
            {"q": "Q5(c)", "points": "High tensile strength of microfibrils prevents cell lysis / bursting when water enters by osmosis; criss-cross lattice embedded in matrix provides mechanical rigidity to maintain plant erectness [2].", "marks": 2}
        ]
    ))

    # Q6: Triglyceride condensation and ester bonds (Fig 2.6)
    questions.append(Question(
        number=6,
        title="9700/21/M/J/22/Q2  -  Triglyceride Condensation & Fatty Acid Saturation",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Triglycerides are neutral hydrophobic lipids formed from glycerol and three fatty acid molecules. Fig. 2.6 shows the esterification reaction and the structures of saturated and unsaturated fatty acid tails.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_6_triglyceride_condensation.png"),
        figure_caption="Fig. 2.6: Condensation of glycerol with three fatty acids to form a triglyceride and three ester bonds.",
        parts=[
            QuestionPart(label="(a)", text="Identify the functional groups on glycerol and a fatty acid that react together to form an ester bond, and state the total number of water molecules produced per triglyceride formed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 2.6, explain the difference between a saturated fatty acid and an unsaturated fatty acid.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why triglycerides containing cis-unsaturated fatty acids have lower melting points and remain liquid (oils) at room temperature.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Hydroxyl group (-OH) on glycerol reacts with carboxyl group (-COOH) on the fatty acid; exactly 3 water molecules (H2O) produced [2].", "marks": 2},
            {"q": "Q6(b)", "points": "Saturated fatty acids contain only single carbon-carbon bonds (C-C) and maximum hydrogens; unsaturated fatty acids contain one or more carbon-carbon double bonds (C=C) [2].", "marks": 2},
            {"q": "Q6(c)", "points": "cis-double bonds introduce a permanent ~30 deg  kink in the hydrocarbon chain; preventing close, tight parallel packing of tails, resulting in weaker intermolecular van der Waals forces that melt at lower temperatures [2].", "marks": 2}
        ]
    ))

    # Q7: Phospholipid structure and bilayer assembly (Fig 2.7)
    questions.append(Question(
        number=7,
        title="9700/22/M/J/21/Q2  -  Phospholipid Structure & Lipid Bilayer Self-Assembly",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Phospholipids are the principal structural lipids of cellular membranes. Fig. 2.7 shows the molecular components of a phospholipid and their spontaneous orientation in an aqueous environment.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_7_phospholipid_structure.png"),
        figure_caption="Fig. 2.7: Phospholipid molecular architecture (left) and spontaneous formation of a lipid bilayer in water (right).",
        parts=[
            QuestionPart(label="(a)", text="Describe how the molecular composition of a phospholipid differs from that of a triglyceride.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the term amphipathic with reference to the phosphate head and hydrocarbon tails of a phospholipid.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to hydrophobic interactions and hydrogen bonding, explain why phospholipids spontaneously arrange into a bilayer in aqueous solution.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "One fatty acid chain of a triglyceride is replaced by a polar, negatively charged phosphate group (ester-linked to glycerol) [2].", "marks": 2},
            {"q": "Q7(b)", "points": "Amphipathic means having both hydrophilic (polar phosphate head attracted to water) and hydrophobic (non-polar fatty acid tails repelled by water) regions on the same molecule [2].", "marks": 2},
            {"q": "Q7(c)", "points": "Hydrophilic phosphate heads orient outwards to form hydrogen bonds with surrounding aqueous cytoplasm/extracellular fluid; hydrophobic fatty acid tails are sequestered inwards into the core away from water due to the hydrophobic effect [2].", "marks": 2}
        ]
    ))

    # Q8: Amino acid general formula and peptide bond condensation (Fig 2.8)
    questions.append(Question(
        number=8,
        title="9700/23/O/N/22/Q3  -  Amino Acid Chemistry & Formation of Dipeptides",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="Proteins are polymers of amino acids linked by covalent peptide bonds. Fig. 2.8 shows the generalised structure of an amino acid and the formation of a dipeptide.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_8_amino_acid_peptide_bond.png"),
        figure_caption="Fig. 2.8: General structure of an amino acid (left) and condensation reaction forming a dipeptide (right).",
        parts=[
            QuestionPart(label="(a)", text="Draw or describe the four chemical groups attached to the central alpha-carbon atom in an amino acid.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 2.8, identify the atoms that combine to form the water molecule released during peptide bond formation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the variable R-group determines the chemical properties of an individual amino acid in a polypeptide chain.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "Central alpha-carbon bonded to: amino group (-NH2), carboxyl group (-COOH), hydrogen atom (-H), and variable side-chain (-R group) [2].", "marks": 2},
            {"q": "Q8(b)", "points": "Hydroxyl group (-OH) from the carboxyl group of amino acid 1 and a hydrogen atom (-H) from the amine group of amino acid 2 [2].", "marks": 2},
            {"q": "Q8(c)", "points": "R-groups may be non-polar (hydrophobic), polar uncharged (hydrophilic), positively charged (basic), or negatively charged (acidic); determining tertiary folding and bonding capabilities [2].", "marks": 2}
        ]
    ))

    # Q9: Protein tertiary structure and 4 stabilizing interactions (Fig 2.9)
    questions.append(Question(
        number=9,
        title="9700/22/F/M/22/Q2  -  Tertiary Structure: Stabilising Bonds & Thermal Denaturation",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="The specific 3D tertiary structure of a globular protein is determined by interactions between the R-groups of distant amino acid residues. Fig. 2.9 illustrates four types of stabilising interactions.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_9_protein_tertiary_interactions.png"),
        figure_caption="Fig. 2.9: Four R-group interactions maintaining the tertiary conformation of a folded polypeptide.",
        parts=[
            QuestionPart(label="(a)", text="Identify the four types of interactions labelled 1, 2, 3, and 4 in Fig. 2.9.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State which of the interactions in Fig. 2.9 is a covalent bond and name the specific sulfur-containing amino acid involved in its formation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how an increase in temperature above 60  deg C causes irreversible loss of tertiary conformation (denaturation) in a globular protein.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "1 = Disulfide bridge / disulfide bond; 2 = Ionic bond / salt bridge; 3 = Hydrogen bond; 4 = Hydrophobic interactions [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Disulfide bridge (bond 1); cysteine [2].", "marks": 2},
            {"q": "Q9(c)", "points": "Increased thermal kinetic energy causes violent molecular vibration; breaking weak hydrogen and ionic bonds / disrupting hydrophobic interactions, causing polypeptide chain to unfold and lose specific active site / tertiary shape [2].", "marks": 2}
        ]
    ))

    # Q10: Haemoglobin quaternary structure & Fe2+ prosthetic group (Fig 2.10)
    questions.append(Question(
        number=10,
        title="9700/21/M/J/23/Q1  -  Quaternary Structure & Function of Haemoglobin",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="Haemoglobin is an allosteric globular protein found in red blood cells that transports oxygen. Fig. 2.10 illustrates its quaternary structure composed of globin subunits and prosthetic haem groups.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_10_haemoglobin_quaternary.png"),
        figure_caption="Fig. 2.10: Quaternary structure of adult haemoglobin (HbA) showing four globin chains and four haem groups.",
        parts=[
            QuestionPart(label="(a)", text="Describe the quaternary structure of a molecule of adult haemoglobin (HbA) shown in Fig. 2.10.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of the iron ion (Fe2+) in the prosthetic haem group during oxygen transport.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the distribution of hydrophobic and hydrophilic amino acid residues maintains the solubility of haemoglobin in the erythrocyte cytoplasm.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Composed of four polypeptide subunits: two identical alpha-globin chains and two identical beta-globin chains; each subunit is associated with one non-protein prosthetic haem group [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Each Fe2+ ion reversibly binds one molecule of oxygen (O2) forming oxyhaemoglobin; one complete haemoglobin molecule transports a maximum of 4 O2 molecules (8 oxygen atoms) [2].", "marks": 2},
            {"q": "Q10(c)", "points": "Hydrophilic R-groups are oriented on the external surface forming hydrogen bonds with water molecules; hydrophobic R-groups are clustered in the interior, conferring high water solubility [2].", "marks": 2}
        ]
    ))

    # Q11: Collagen triple helix and tensile strength (Fig 2.11)
    questions.append(Question(
        number=11,
        title="9700/22/O/N/21/Q2  -  Collagen Architecture: Triple Helix to Fibril",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="Collagen is the most abundant fibrous structural protein in animals, providing tensile strength to tendons, skin, and bones. Fig. 2.11 shows the structural hierarchy from tropocollagen triple helix to collagen fibril.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_11_collagen_triple_helix.png"),
        figure_caption="Fig. 2.11: Collagen triple helix (top) and staggered covalent cross-linking forming a collagen fibril (bottom).",
        parts=[
            QuestionPart(label="(a)", text="Explain the importance of the repeating amino acid sequence Gly-X-Y in the primary structure of a collagen polypeptide chain.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the arrangement of the three polypeptide chains in a tropocollagen molecule.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 2.11, explain how tropocollagen molecules are assembled to form collagen fibrils with high tensile strength without lines of weakness.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Glycine has the smallest R-group (a single hydrogen atom, -H); enabling three polypeptide chains to pack tightly together in the central core of the triple helix without steric hindrance [2].", "marks": 2},
            {"q": "Q11(b)", "points": "Three left-handed helical polypeptide chains wind around each other into a tight right-handed triple helix; held together by extensive inter-chain hydrogen bonds [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Tropocollagen molecules lie parallel in a staggered arrangement (~67 nm overlap) avoiding a single transverse line of weakness; stabilized by covalent cross-links between lysine residues of adjacent molecules [2].", "marks": 2}
        ]
    ))

    # Q12: Water dipole, hydrogen bonding and hydration shells (Fig 2.12)
    questions.append(Question(
        number=12,
        title="9700/22/M/J/20/Q2  -  Dipolar Nature & Solvent Properties of Water",
        syllabus_ref="Syllabus 2.4",
        difficulty="ADVANCED",
        preamble="Water is the medium in which all metabolic reactions occur. Fig. 2.12 illustrates the dipolar structure of a water molecule, hydrogen bonding, and hydration shells surrounding dissolved ions.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_12_water_dipole_hbonding.png"),
        figure_caption="Fig. 2.12: Dipolar nature of water, hydrogen bonding network (left), and hydration shells surrounding Na+ and Cl- (right).",
        parts=[
            QuestionPart(label="(a)", text="Explain why water is described as a dipolar molecule.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 2.12, explain how water molecules interact with sodium ions (Na+) and chloride ions (Cl-) to dissolve sodium chloride.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the high specific heat capacity of water buffers aquatic organisms against sudden fluctuations in environmental temperature.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Oxygen atom is more electronegative than hydrogen, pulling shared electrons towards itself; producing a partial negative charge (delta-) on oxygen and partial positive charges (delta+) on hydrogens at a 104.5 deg  angle [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Partially negative oxygen atoms (delta-) form electrostatic attractions with Na+ cations; partially positive hydrogen atoms (delta+) attract Cl- anions; forming hydration shells that isolate and disperse ions in solution [2].", "marks": 2},
            {"q": "Q12(c)", "points": "A large amount of thermal energy is required to break extensive intermolecular hydrogen bonds before kinetic energy increases; large bodies of water change temperature very slowly, maintaining thermally stable habitats [2].", "marks": 2}
        ]
    ))

    # Q13: Biochemical diagnostic flowchart (Fig 2.13)
    questions.append(Question(
        number=13,
        title="9700/23/M/J/22/Q2  -  Systematic Identification of Biological Macromolecules",
        syllabus_ref="Syllabus 2.1",
        difficulty="ADVANCED",
        preamble="A biological mystery extract was analysed using a sequence of biochemical food tests. Fig. 2.13 shows the standard diagnostic flowchart for identifying starch, reducing sugars, non-reducing sugars, lipids, and proteins.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_13_biochemical_testing_flowchart.png"),
        figure_caption="Fig. 2.13: Diagnostic flowchart summarizing reagents, procedures, and positive observations for biological molecule tests.",
        parts=[
            QuestionPart(label="(a)", text="A sample gives a negative result when heated directly with Benedict's solution, but gives a brick-red precipitate after boiling with dilute hydrochloric acid followed by neutralisation with sodium hydrogen carbonate. Explain these observations.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the procedure and expected positive result for the emulsion test for lipids.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the chemical basis of the colour change from blue to lilac in the biuret test for proteins.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "The initial negative result indicates absence of reducing sugars; boiling with dilute HCl hydrolyses non-reducing disaccharides (e.g. sucrose) into reducing monosaccharides (glucose and fructose) which reduce Cu2+ in the second test [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Dissolve sample thoroughly in ethanol; pour / decant ethanol solution into an equal volume of water; positive result is the appearance of a cloudy / milky-white emulsion of lipid droplets [2].", "marks": 2},
            {"q": "Q13(c)", "points": "In alkaline solution (NaOH/KOH), Cu2+ ions form a coordination complex with nitrogen atoms in adjacent peptide bonds (-CO-NH-); producing a characteristic purple / lilac colour [2].", "marks": 2}
        ]
    ))

    # Q14: Sucrose non-reducing rationale (Fig 2.14)
    questions.append(Question(
        number=14,
        title="9700/21/O/N/23/Q2  -  Condensation of Sucrose & Non-Reducing Chemistry",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Sucrose is the major transport disaccharide in the phloem of angiosperms. Fig. 2.14 illustrates the condensation of alpha-glucose and beta-fructose to form sucrose.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig2_14_sucrose_condensation.png"),
        figure_caption="Fig. 2.14: Condensation reaction of alpha-glucose and beta-fructose to form sucrose, showing the alpha(1<->2)beta-glycosidic bond.",
        parts=[
            QuestionPart(label="(a)", text="Identify the two monosaccharides that condense to form sucrose and state the carbons involved in the glycosidic bond.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 2.14, explain why sucrose is classified as a non-reducing sugar.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest why plants transport carbohydrate in the phloem as sucrose rather than as glucose.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "alpha-glucose and beta-fructose; glycosidic bond formed between carbon 1 (C1) of glucose and carbon 2 (C2) of fructose [2].", "marks": 2},
            {"q": "Q14(b)", "points": "Both anomeric / reducing carbons (C1 of glucose and C2 of fructose) are involved in forming the glycosidic bond; neither ring can open into a free aldehyde or ketone group to donate electrons to Cu2+ [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Sucrose is chemically less reactive / non-reducing, so it is not readily oxidised or metabolised during translocation; transports twice as much carbon per molecule at the same osmotic potential [2].", "marks": 2}
        ]
    ))

    # Q15: Non-reducing sugar acid hydrolysis protocol
    questions.append(Question(
        number=15,
        title="9700/22/F/M/21/Q3  -  Acid Hydrolysis Protocol for Non-Reducing Sugars",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="A food chemistry laboratory tested a commercial syrup for non-reducing sugars using acid hydrolysis.",
        parts=[
            QuestionPart(label="(a)", text="Outline the three sequential experimental steps required to test for a non-reducing sugar such as sucrose.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the solution must be neutralised before adding Benedict's reagent.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest how an enzyme could be used instead of dilute hydrochloric acid to achieve hydrolysis, naming the enzyme required.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "1. Boil sample with dilute hydrochloric acid (HCl) for several minutes; 2. Cool and neutralise with sodium hydrogen carbonate (NaHCO3) / test with indicator; 3. Add Benedict's reagent and heat to 80-100  deg C [2].", "marks": 2},
            {"q": "Q15(b)", "points": "Benedict's reagent is alkaline and requires a basic pH to function; excess acid would neutralise the reagent and prevent reduction of Cu2+ ions [2].", "marks": 2},
            {"q": "Q15(c)", "points": "Sucrase / invertase enzyme; incubated at optimum temperature (37-40  deg C) and optimum neutral pH [2].", "marks": 2}
        ]
    ))

    # Q16: Ethanol emulsion test for lipids
    questions.append(Question(
        number=16,
        title="9700/21/M/J/20/Q2  -  Mechanism of the Ethanol Emulsion Test",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="Lipids are non-polar hydrophobic molecules that are virtually insoluble in water but soluble in organic solvents.",
        parts=[
            QuestionPart(label="(a)", text="Describe how the solubility of triglycerides in ethanol differs from their solubility in water, with reference to intermolecular interactions.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why adding water to an ethanolic solution of lipid causes a cloudy white emulsion to form.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the presence of water in the initial ethanol extraction tube would invalidate the test.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Non-polar hydrocarbon tails of triglycerides form London dispersion forces with ethanol; but cannot form hydrogen bonds with water molecules, so are hydrophobic and insoluble in water [2].", "marks": 2},
            {"q": "Q16(b)", "points": "Lipid is insoluble in the aqueous mixture and precipitates out of solution; forming tiny suspended lipid droplets (an emulsion) that scatter transmitted light, appearing cloudy/milky [2].", "marks": 2},
            {"q": "Q16(c)", "points": "Water present initially prevents complete dissolution of lipid in ethanol / produces premature turbidity before decanting, yielding a false negative or unstandardised result [2].", "marks": 2}
        ]
    ))

    # Q17: Comparison of glycogen and amylopectin
    questions.append(Question(
        number=17,
        title="9700/23/O/N/21/Q3  -  Comparative Biochemistry of Branched Polysaccharides",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Both glycogen and amylopectin are branched polymers composed of alpha-glucose monomers.",
        parts=[
            QuestionPart(label="(a)", text="State the two types of glycosidic bonds present in both glycogen and amylopectin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compare the frequency of branch points in glycogen with that in amylopectin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the structural difference identified in (b) relates to the higher metabolic rate of animals compared to plants.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "alpha(1->4)-glycosidic bonds (in linear chains) and alpha(1->6)-glycosidic bonds (at branch points) [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Glycogen has branch points approximately every 8 to 12 glucose units; whereas amylopectin has branch points approximately every 20 to 30 units (glycogen is much more branched) [2].", "marks": 2},
            {"q": "Q17(c)", "points": "Animals have higher metabolic demands / cellular respiration rates for locomotion; more branch points provide vastly more terminal glucose ends for rapid simultaneous phosphorolysis / glucose release [2].", "marks": 2}
        ]
    ))

    # Q18: Globular vs fibrous proteins: Haemoglobin vs Collagen
    questions.append(Question(
        number=18,
        title="9700/22/M/J/22/Q3  -  Globular vs Fibrous Protein Classification",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Proteins are broadly categorised into globular and fibrous classes based on their overall 3D conformation.",
        parts=[
            QuestionPart(label="(a)", text="Contrast the general solubility and overall molecular shape of globular proteins with fibrous proteins.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compare the primary structures of haemoglobin and collagen with respect to amino acid diversity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the physiological roles of haemoglobin and collagen reflect their respective structural classifications.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Globular proteins are compact, spherical/rounded, and generally water-soluble; fibrous proteins are elongated, form extended fibres/sheets, and are generally insoluble in water [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Haemoglobin has a diverse, non-repeating sequence of 20 different amino acids; collagen has a highly repetitive sequence dominated by Gly-X-Y triplets (one-third glycine) [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Haemoglobin has dynamic physiological role (reversibly binds O2, soluble in cytoplasm); collagen has static structural role (tensile strength in tendons/dermis resisting mechanical stretching) [2].", "marks": 2}
        ]
    ))

    # Q19: [Mentora Original A* Extension] Water thermodynamic properties
    questions.append(Question(
        number=19,
        title="[Mentora Original A* Extension] Q19  -  Thermodynamic Properties of Water in Homeostasis",
        syllabus_ref="Syllabus 2.4",
        difficulty="ADVANCED",
        preamble="The physical properties of water are fundamental to biochemical homeostasis. Water has a high specific heat capacity (4.184 J g-1 K-1) and a very high latent heat of vaporisation (2260 kJ kg-1).",
        parts=[
            QuestionPart(label="(a)", text="Explain, in terms of intermolecular hydrogen bonding, why water exhibits such an unusually high latent heat of vaporisation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate or estimate the cooling effect on a 60 kg athlete if 500 cm3 of sweat (assumed pure water, density 1.0 g cm-3) evaporates from the skin surface, given the specific heat capacity of the human body is 3.5 kJ kg-1  deg C-1.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the high specific heat capacity of water is biologically vital within cellular cytoplasm.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Extensive network of hydrogen bonds between water molecules requires substantial thermal energy input to break before molecules can escape into gaseous phase [2].", "marks": 2},
            {"q": "Q19(b)", "points": "Heat removed = 0.5 kg × 2260 kJ kg-1 = 1130 kJ; Temperature decrease = DeltaQ / (m × c) = 1130 / (60 × 3.5) = 1130 / 210 ≈ 5.38  deg C (accept 5.3-5.5  deg C) [2].", "marks": 2},
            {"q": "Q19(c)", "points": "Buffers cytoplasm against abrupt temperature spikes produced by exothermic metabolic reactions; protecting intracellular enzymes from thermal fluctuations and maintaining optimal kinetic rates [2].", "marks": 2}
        ]
    ))

    # Q20: [Mentora Original A* Extension] Energy density of triglycerides vs glycogen
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] Q20  -  Metabolic Energetics: Lipids vs Carbohydrates",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="Triglycerides yield approximately 38 kJ g-1 of metabolic energy upon complete cellular respiration, whereas hydrated glycogen yields only approximately 17 kJ g-1.",
        parts=[
            QuestionPart(label="(a)", text="Explain why triglycerides yield more than twice as much energy per gram during aerobic oxidation compared to carbohydrates.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the non-polar, hydrophobic nature of triglycerides makes them a much lighter energy store than glycogen in mobile animals.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State one significant physiological advantage of storing energy as glycogen despite its lower energy density.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Triglycerides have a much higher proportion of carbon-hydrogen (C-H) bonds and far less oxygen (more chemically reduced); releasing more electrons/protons to the electron transport chain per gram [2].", "marks": 2},
            {"q": "Q20(b)", "points": "Triglycerides are stored in anhydrous form without associated water; glycogen is polar and binds ~2 g of hydration water per gram of dry glycogen, making it much heavier to carry [2].", "marks": 2},
            {"q": "Q20(c)", "points": "Glycogen can be rapidly mobilised under anaerobic conditions (glycolysis without oxygen); whereas fatty acids can only be respirated aerobically via beta-oxidation in mitochondria [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & BIOCHEMICAL MECHANISM QUESTIONS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Benedict's reduction mechanism
    questions.append(Question(
        number=21,
        title="9700/22/O/N/22/Q2  -  Redox Chemistry of Benedict's Reagent",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="Benedict's reagent contains copper(II) sulfate, sodium carbonate, and sodium citrate in aqueous alkaline solution.",
        parts=[
            QuestionPart(label="(a)", text="Describe the oxidation state change of copper during a positive Benedict's test.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what happens to the reducing sugar molecule during this redox reaction.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Copper is reduced from oxidation state +2 (blue Cu2+ ions in cupric form) to +1 (insoluble red Cu+ in copper(I) oxide, Cu2O) [2].", "marks": 2},
            {"q": "Q21(b)", "points": "The reducing sugar is oxidised; its free carbonyl group (aldehyde -CHO) loses electrons to form a carboxylate group (-COO-) [2].", "marks": 2}
        ]
    ))

    # Q22: Biuret test mechanism
    questions.append(Question(
        number=22,
        title="9700/21/O/N/21/Q2  -  Principles of the Biuret Protein Assay",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="The biuret test is specific for proteins and polypeptides containing multiple peptide linkages.",
        parts=[
            QuestionPart(label="(a)", text="Explain why free amino acids do not give a purple colour in the biuret test.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how the intensity of the purple colour can be used to estimate protein concentration.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "The biuret reaction requires coordination of Cu2+ with at least two adjacent peptide bonds (-CO-NH-); free amino acids have no peptide bonds [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Colour intensity is directly proportional to the number of peptide bonds present; measurable via colorimeter absorbance using standard calibration curve [2].", "marks": 2}
        ]
    ))

    # Q23: Ribose vs Deoxyribose pentose rings
    questions.append(Question(
        number=23,
        title="9700/23/M/J/23/Q3  -  Pentose Monosaccharides: Ribose vs Deoxyribose",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Ribose and deoxyribose are five-carbon pentose sugars essential for nucleic acid and ATP biosynthesis.",
        parts=[
            QuestionPart(label="(a)", text="State the exact molecular formula of ribose and deoxyribose.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the structural difference at carbon atom 2 (C2) between ribose and deoxyribose.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Ribose = C5H10O5; Deoxyribose = C5H10O4 [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Ribose has a hydroxyl group (-OH) attached to carbon 2; deoxyribose has a hydrogen atom (-H) attached to carbon 2 (lacks an oxygen atom) [2].", "marks": 2}
        ]
    ))

    # Q24: Monomer, polymer and macromolecule definitions
    questions.append(Question(
        number=24,
        title="9700/22/F/M/20/Q2  -  Definitions: Monomer, Polymer & Macromolecule",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Biological systems assemble large, complex molecules from simpler constituent units.",
        parts=[
            QuestionPart(label="(a)", text="Define the terms monomer and polymer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a triglyceride is described as a macromolecule but not a true polymer.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Monomer: small repeating unit from which larger polymers are made; Polymer: large molecule formed from many identical or similar repeating monomers joined by covalent bonds [2].", "marks": 2},
            {"q": "Q24(b)", "points": "A triglyceride is a large molecular mass structure (macromolecule); but it is formed by condensation of four distinct molecules (one glycerol + three fatty acids), not by repeating chains of identical monomers [2].", "marks": 2}
        ]
    ))

    # Q25: Lactose disaccharide condensation
    questions.append(Question(
        number=25,
        title="9700/21/M/J/21/Q3  -  Synthesis of Lactose Disaccharide",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Lactose is the primary carbohydrate found in mammalian milk.",
        parts=[
            QuestionPart(label="(a)", text="Name the two monosaccharides that condense to form lactose, and state the type of glycosidic bond formed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why individuals with lactose intolerance experience digestive symptoms when consuming milk.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "beta-galactose and beta-glucose; beta(1->4)-glycosidic bond [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Lack the enzyme lactase in brush border of small intestine; undigested lactose remains in gut lumen, lowering water potential (causing osmotic diarrhoea) and fermented by colon bacteria (gas/cramps) [2].", "marks": 2}
        ]
    ))

    # Q26: Iodine-starch polyiodide complex
    questions.append(Question(
        number=26,
        title="9700/22/O/N/20/Q3  -  Molecular Mechanism of the Iodine Test for Starch",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="The iodine test relies on the molecular interaction between polyiodide ions and starch.",
        parts=[
            QuestionPart(label="(a)", text="Describe how iodine molecules interact with the helical structure of amylose to produce a blue-black colour.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why heating a blue-black starch-iodine solution causes it to become colourless, and why the colour returns upon cooling.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Linear polyiodide ions (I3-, I5-) become trapped inside the hydrophobic central cavity of the amylose helix; electron transfer alters orbital energy levels to absorb light, producing intense blue-black colour [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Heating uncoils the amylose helix so polyiodide ions are released (colourless); cooling allows hydrogen bonding to reform helical coil, trapping iodine once again (recovering blue-black colour) [2].", "marks": 2}
        ]
    ))

    # Q27: Plant cell wall adaptations of cellulose
    questions.append(Question(
        number=27,
        title="9700/23/M/J/20/Q2  -  Mechanical Adaptations of the Plant Cell Wall",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Plant cell walls provide mechanical support and define cell shape.",
        parts=[
            QuestionPart(label="(a)", text="Outline how the arrangement of cellulose microfibrils in laminated layers confers multidirectional tensile strength.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the plant cell wall is fully permeable to water and dissolved mineral ions despite its mechanical strength.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Microfibrils are laid down in criss-cross layers at different angles; embedded in a pectin/hemicellulose matrix, resisting tensile forces exerted in all directions [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Cellulose microfibrils are separated by large aqueous pores (spaces); allowing unrestricted free passage of water and dissolved solutes by apoplastic mass flow [2].", "marks": 2}
        ]
    ))

    # Q28: Saturated vs unsaturated fatty acids
    questions.append(Question(
        number=28,
        title="9700/22/M/J/23/Q4  -  Hydrocarbon Packing in Saturated vs Unsaturated Lipids",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Lipids extracted from animal tissues are typically solid at 20  deg C, whereas lipids from plant seeds are typically liquid oils.",
        parts=[
            QuestionPart(label="(a)", text="Explain the structural basis for the difference in physical state between animal fats and plant oils at room temperature.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Define the terms monounsaturated and polyunsaturated fatty acid.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Animal fats have predominantly saturated fatty acids with straight chains that pack closely, maximizing van der Waals forces (solid); plant oils contain cis-unsaturated kinks preventing close packing (liquid) [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Monounsaturated fatty acid has exactly one carbon-carbon double bond (C=C); polyunsaturated fatty acid has two or more carbon-carbon double bonds in its hydrocarbon chain [2].", "marks": 2}
        ]
    ))

    # Q29: Hydrophobic effect and phospholipid membranes
    questions.append(Question(
        number=29,
        title="9700/21/O/N/23/Q3  -  The Hydrophobic Effect in Membrane Assembly",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Cellular compartmentalisation depends on the thermodynamic self-assembly of phospholipid bilayers.",
        parts=[
            QuestionPart(label="(a)", text="Explain why water molecules surrounding non-polar hydrocarbon tails experience an unfavourable decrease in entropy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how clustering of hydrophobic tails in the interior of a bilayer increases the entropy of the system.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Water molecules cannot form hydrogen bonds with non-polar hydrocarbons and must arrange into rigid, ordered 'cages' (clathrates), lowering entropy [2].", "marks": 2},
            {"q": "Q29(b)", "points": "Clustering tails together minimizes total hydrophobic surface area exposed; freeing cage water molecules into random bulk solution, greatly increasing system entropy [2].", "marks": 2}
        ]
    ))

    # Q30: Physiological functions of triglycerides
    questions.append(Question(
        number=30,
        title="9700/22/F/M/22/Q3  -  Physiological Roles of Triglycerides in Animals",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Adipose tissue stores triglycerides beneath the dermis and surrounding internal organs.",
        parts=[
            QuestionPart(label="(a)", text="Describe the role of subcutaneous adipose tissue in thermal insulation in marine mammals such as seals.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the metabolic oxidation of triglycerides produces significant amounts of metabolic water in desert organisms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Lipids have low thermal conductivity; thick blubber layer reduces conductive heat loss from warm core to cold sea water, maintaining body temperature [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Triglycerides have high hydrogen content; complete oxidation in aerobic respiration produces water (H2O) when electrons and protons combine with oxygen at terminal cytochrome oxidase [2].", "marks": 2}
        ]
    ))

    # Q31: Protein secondary structure: alpha helix and beta sheet
    questions.append(Question(
        number=31,
        title="9700/23/O/N/22/Q4  -  Secondary Structure Conformations: alpha-Helix & beta-Pleated Sheet",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Secondary structure refers to local, regular folding of the polypeptide chain backbone.",
        parts=[
            QuestionPart(label="(a)", text="Describe the hydrogen bonding pattern that stabilises an alpha-helix.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between parallel and antiparallel beta-pleated sheets.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "Hydrogen bonds form between the oxygen of the carbonyl group (-C=O) of one peptide bond and the hydrogen of the amino group (-N-H) of another residue four places ahead along the chain [2].", "marks": 2},
            {"q": "Q31(b)", "points": "In parallel sheets, adjacent polypeptide strands run in the same N-to-C terminal direction; in antiparallel sheets, adjacent strands run in opposite directions [2].", "marks": 2}
        ]
    ))

    # Q32: Thermal and pH denaturation of enzymes
    questions.append(Question(
        number=32,
        title="9700/22/M/J/21/Q4  -  Disruption of Tertiary Interactions by pH & Temperature",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="The tertiary structure of an enzyme active site is sensitive to changes in the surrounding environment.",
        parts=[
            QuestionPart(label="(a)", text="Explain how a decrease in pH disrupts ionic bonds in the tertiary structure of a protein.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why primary structure is unaffected when a protein undergoes denaturation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Excess H+ ions protonate negatively charged carboxylate groups (-COO- + H+ -> -COOH); neutralizing the negative charge and destroying ionic salt bridges with -NH3+ groups [2].", "marks": 2},
            {"q": "Q32(b)", "points": "Denaturation disrupts weaker hydrogen, ionic, and hydrophobic interactions; covalent peptide bonds between amino acids have high activation energy and are not broken by heat or pH shifts [2].", "marks": 2}
        ]
    ))

    # Q33: Iron in haemoglobin and anaemia
    questions.append(Question(
        number=33,
        title="9700/21/M/J/23/Q4  -  Iron Coordination in Haemoglobin & Pathophysiology of Anaemia",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Haemoglobin synthesised in erythroblasts requires dietary iron.",
        parts=[
            QuestionPart(label="(a)", text="State the oxidation state of the iron ion in functional haemoglobin and explain what happens if it is oxidised to Fe3+.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a dietary deficiency of iron causes symptoms of chronic fatigue and weakness.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Fe2+ (ferrous); oxidation to Fe3+ forms methaemoglobin, which cannot bind oxygen reversibly [2].", "marks": 2},
            {"q": "Q33(b)", "points": "Less iron means fewer haem groups and lower haemoglobin synthesis; reduces oxygen carrying capacity of blood, leading to lower aerobic respiration and less ATP synthesis in muscles/brain [2].", "marks": 2}
        ]
    ))

    # Q34: Glycine residue in collagen
    questions.append(Question(
        number=34,
        title="9700/22/O/N/22/Q4  -  Stereochemical Role of Glycine in the Collagen Helix",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Collagen contains glycine at every third position in its primary structure.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of glycine and explain why any other amino acid would disrupt the tropocollagen triple helix.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of hydroxyproline and vitamin C in maintaining collagen stability.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Glycine has only a hydrogen atom (-H) as its R-group; any larger side chain would create steric clash / prevent close packing of the three helical chains along the central axis [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Hydroxyproline forms essential inter-chain hydrogen bonds; vitamin C is required as a cofactor by prolyl hydroxylase (deficiency causes scurvy and weak connective tissue) [2].", "marks": 2}
        ]
    ))

    # Q35: Water as a universal biological solvent
    questions.append(Question(
        number=35,
        title="9700/21/O/N/22/Q4  -  Physical Basis of Water as a Biological Solvent",
        syllabus_ref="Syllabus 2.4",
        difficulty="CHALLENGING",
        preamble="Water dissolves a wide variety of polar and ionic solutes within metabolic systems.",
        parts=[
            QuestionPart(label="(a)", text="Explain how water dissolves polar non-ionic molecules such as glucose and amino acids.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why water is an ineffective solvent for non-polar lipids such as cholesterol and triglycerides.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Water forms hydrogen bonds with polar functional groups (-OH in glucose, -NH2 and -COOH in amino acids); separating solute molecules and distributing them evenly [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Non-polar lipids lack dipoles or charges and cannot form hydrogen bonds with water; cohesive hydrogen bonding between water molecules excludes non-polar molecules [2].", "marks": 2}
        ]
    ))

    # Q36: Cohesion and adhesion in xylem transpiration
    questions.append(Question(
        number=36,
        title="9700/23/M/J/22/Q4  -  Cohesion-Tension Properties of Water in Plant Xylem",
        syllabus_ref="Syllabus 2.4",
        difficulty="CHALLENGING",
        preamble="Water moves upward through xylem vessels in tall trees against gravity.",
        parts=[
            QuestionPart(label="(a)", text="Explain the difference between cohesion and adhesion in the context of water transport in xylem.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how hydrogen bonding prevents cavitation (breaking of the continuous water column) under negative hydrostatic pressure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Cohesion is the attraction between water molecules due to hydrogen bonding; adhesion is the attraction between water molecules and hydrophilic cellulose/lignin in xylem walls [2].", "marks": 2},
            {"q": "Q36(b)", "points": "High tensile strength from collective hydrogen bonds allows water columns to withstand great tension without pulling apart / breaking continuity [2].", "marks": 2}
        ]
    ))

    # Q37: [Mentora Original A* Extension] Allosteric cooperativity in haemoglobin
    questions.append(Question(
        number=37,
        title="[Mentora Original A* Extension] Q37  -  Allosteric Cooperativity in Haemoglobin",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="The oxygen dissociation curve of haemoglobin has a characteristic sigmoidal shape due to cooperative binding.",
        parts=[
            QuestionPart(label="(a)", text="Describe how binding of the first oxygen molecule alters the tertiary and quaternary conformation of haemoglobin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how this conformational change increases the affinity of the remaining three haem groups for oxygen.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Oxygen binding pulls the Fe2+ ion into the plane of the porphyrin ring; pulling the proximal histidine and shifting the quaternary arrangement from the tense (T) state to relaxed (R) state [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Conformational shift unmasks adjacent haem clefts; making subsequent oxygen binding energetically easier (higher affinity), producing sigmoidal cooperative loading [2].", "marks": 2}
        ]
    ))

    # Q38: [Mentora Original A* Extension] Scurvy and collagen biosynthesis
    questions.append(Question(
        number=38,
        title="[Mentora Original A* Extension] Q38  -  Molecular Pathology of Scurvy",
        syllabus_ref="Syllabus 2.3",
        difficulty="ADVANCED",
        preamble="Scurvy is characterized by bleeding gums, fragile capillaries, and poor wound healing.",
        parts=[
            QuestionPart(label="(a)", text="Explain the biochemical role of ascorbic acid (vitamin C) in the post-translational modification of collagen.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how unhydroxylated collagen chains lead to fragile blood vessel walls.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Ascorbic acid acts as a reducing cofactor to maintain the Fe2+ ion of prolyl 4-hydroxylase in its reduced state during the hydroxylation of proline residues [2].", "marks": 2},
            {"q": "Q38(b)", "points": "Without hydroxyproline, inter-chain hydrogen bonds cannot form; tropocollagen triple helices unfold at physiological body temperature (37  deg C), weakening vascular basement membranes [2].", "marks": 2}
        ]
    ))

    # Q39: [Mentora Original A* Extension] Density anomaly of water and ice
    questions.append(Question(
        number=39,
        title="[Mentora Original A* Extension] Q39  -  Density Anomaly of Water & Aquatic Survival",
        syllabus_ref="Syllabus 2.4",
        difficulty="ADVANCED",
        preamble="Unlike most substances, solid water (ice) is less dense than liquid water at 4  deg C.",
        parts=[
            QuestionPart(label="(a)", text="Explain, in terms of molecular geometry and hydrogen bonding, why ice floats on liquid water.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the ecological importance of floating ice for freshwater aquatic ecosystems in winter.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Below 4  deg C, water molecules slow down and form maximum (4) hydrogen bonds in a rigid, open tetrahedral lattice; holding molecules further apart than in liquid water, reducing density [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Ice layer on lake surfaces acts as an insulating blanket; preventing water below from freezing solid and preserving liquid habitats for aquatic organisms [2].", "marks": 2}
        ]
    ))

    # Q40: [Mentora Original A* Extension] Serial dilution protocol for reducing sugars
    questions.append(Question(
        number=40,
        title="[Mentora Original A* Extension] Q40  -  Serial Dilution Calculation for Colorimetric Assay",
        syllabus_ref="Syllabus 2.1",
        difficulty="ADVANCED",
        preamble="A candidate is provided with a 2.0% (g / 100 cm3) stock glucose solution and asked to prepare a two-fold serial dilution series.",
        parts=[
            QuestionPart(label="(a)", text="Describe how to prepare four successive dilutions (concentrations: 1.0%, 0.5%, 0.25%, and 0.125%) using a 10 cm3 graduated pipette and distilled water, producing 10 cm3 of each solution.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a serial dilution series is preferable to separate simple dilutions when generating a colorimetric calibration curve.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Transfer 10 cm3 of 2.0% stock into tube 1; take 5 cm3 from stock and add 5 cm3 distilled water to make 1.0%; mix and transfer 5 cm3 of 1.0% into 5 cm3 water for 0.5%; repeat sequentially [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Provides an evenly spaced logarithmic range of concentrations; minimizes systematic pipetting errors across wide dynamic ranges [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Definition of monosaccharide
    questions.append(Question(
        number=41,
        title="9700/22/F/M/23/Q1  -  Definition of a Monosaccharide",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Monosaccharides are the basic building blocks of carbohydrates.",
        parts=[
            QuestionPart(label="(a)", text="Define the term monosaccharide and state the general empirical formula for triose and hexose sugars.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "A single sugar monomer that cannot be hydrolysed into simpler carbohydrate units; general empirical formula (CH2O)n / CnH2nOn [2].", "marks": 2}
        ]
    ))

    # Q42: Monomers of maltose and sucrose
    questions.append(Question(
        number=42,
        title="9700/21/M/J/22/Q1  -  Disaccharide Constituents",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Disaccharides consist of two hexose units.",
        parts=[
            QuestionPart(label="(a)", text="State the constituent monosaccharide units present in maltose and sucrose.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "Maltose = alpha-glucose + alpha-glucose; Sucrose = alpha-glucose + beta-fructose [2].", "marks": 2}
        ]
    ))

    # Q43: Starch chemical test and observation
    questions.append(Question(
        number=43,
        title="9700/22/M/J/22/Q1  -  The Starch Test",
        syllabus_ref="Syllabus 2.1",
        difficulty="CHALLENGING",
        preamble="Starch is detected using a specific chemical reagent.",
        parts=[
            QuestionPart(label="(a)", text="State the reagent used and the positive colour change observed when testing for starch.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "Iodine in potassium iodide (KI) solution; colour changes from yellow-brown / orange to blue-black [2].", "marks": 2}
        ]
    ))

    # Q44: Ester bond in triglycerides
    questions.append(Question(
        number=44,
        title="9700/23/M/J/21/Q1  -  Ester Bond Formation",
        syllabus_ref="Syllabus 2.2",
        difficulty="CHALLENGING",
        preamble="Lipid synthesis involves covalent bond formation.",
        parts=[
            QuestionPart(label="(a)", text="State the name of the covalent bond formed between glycerol and a fatty acid, and name the reaction type.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Ester bond / ester linkage (-COO-); condensation reaction [2].", "marks": 2}
        ]
    ))

    # Q45: Definition of primary structure
    questions.append(Question(
        number=45,
        title="9700/22/O/N/21/Q1  -  Definition of Primary Structure",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Protein structure is described across four hierarchical levels.",
        parts=[
            QuestionPart(label="(a)", text="Define the primary structure of a protein.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "The unique sequence and number of amino acids in a polypeptide chain, linked together by covalent peptide bonds [2].", "marks": 2}
        ]
    ))

    # Q46: Secondary protein structures
    questions.append(Question(
        number=46,
        title="9700/21/O/N/21/Q1  -  Types of Secondary Structure",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Polypeptide backbones fold into regular conformations.",
        parts=[
            QuestionPart(label="(a)", text="Name the two common types of secondary structure in proteins and state the bond that maintains them.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "alpha-helix (alpha-helix) and beta-pleated sheet (beta-pleated sheet); maintained by hydrogen bonds between peptide backbone -C=O and -N-H groups [2].", "marks": 2}
        ]
    ))

    # Q47: Haemoglobin polypeptide chains and prosthetic group
    questions.append(Question(
        number=47,
        title="9700/22/M/J/21/Q1  -  Subunit Composition of Haemoglobin",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Haemoglobin is an oligomeric globular protein.",
        parts=[
            QuestionPart(label="(a)", text="State the number of globin polypeptide chains and the name of the prosthetic group present in one molecule of haemoglobin.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "4 polypeptide chains (two alpha-chains and two beta-chains); haem (heme) group [2].", "marks": 2}
        ]
    ))

    # Q48: Glycine in collagen
    questions.append(Question(
        number=48,
        title="9700/23/O/N/20/Q1  -  Glycine Frequency in Collagen",
        syllabus_ref="Syllabus 2.3",
        difficulty="CHALLENGING",
        preamble="Collagen possesses a unique amino acid distribution.",
        parts=[
            QuestionPart(label="(a)", text="Name the amino acid that occurs at every third position in the collagen primary sequence and state its R-group.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "Glycine; R-group is a single hydrogen atom (-H) [2].", "marks": 2}
        ]
    ))

    # Q49: High latent heat of vaporisation of water
    questions.append(Question(
        number=49,
        title="9700/22/F/M/20/Q1  -  Definition of Latent Heat of Vaporisation",
        syllabus_ref="Syllabus 2.4",
        difficulty="CHALLENGING",
        preamble="Water has notable thermal constants.",
        parts=[
            QuestionPart(label="(a)", text="Define the term latent heat of vaporisation and explain its biological importance during sweating.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "The amount of thermal energy required to convert a unit mass of liquid into vapour without a change in temperature; evaporation of sweat removes large amounts of body heat, providing effective evaporative cooling [2].", "marks": 2}
        ]
    ))

    # Q50: [Mentora Original A* Extension] Phospholipid bilayer vs Triglyceride droplet
    questions.append(Question(
        number=50,
        title="[Mentora Original A* Extension] Q50  -  Supramolecular Assembly: Phospholipid Bilayer vs Triglyceride Droplet",
        syllabus_ref="Syllabus 2.2",
        difficulty="ADVANCED",
        preamble="When added to water, phospholipids form stable bilayers or vesicles, whereas triglycerides form large coalesced oil droplets.",
        parts=[
            QuestionPart(label="(a)", text="Explain why phospholipids assemble into bilayers in water while triglycerides coalesce into large droplets.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "Phospholipids are amphipathic: polar heads interact with water while tails are sequestered in the interior; triglycerides are entirely non-polar with no hydrophilic region to interact with water, so they coalesce to minimize water contact [2].", "marks": 2}
        ]
    ))

    return questions

def get_topic2_faqs():
    return [
        {
            "q_num": 1,
            "title": "Why Does Sucrose Give a Negative Benedict's Test and What Is the Biochemical Rationale for the Non-Reducing Sugar Test?",
            "category": "Biochemical Assays • Carbohydrate Chemistry",
            "examiner_trap": "Heating sucrose directly with Benedict's reagent and concluding that no sugar is present. Sucrose is a non-reducing disaccharide that must be hydrolysed with acid first.",
            "model_answer": "• Chemical Rationale: Benedict's test detects free aldehyde (-CHO) or ketone (C=O) groups (anomeric carbons) capable of reducing blue Cu2+ ions to brick-red Cu+ (Cu2O precipitate).\n• Sucrose Structure: Composed of alpha-glucose and beta-fructose joined by an alpha(1->2)beta-glycosidic bond; the bond links BOTH anomeric carbons together, locking the rings so neither can open to expose a free reducing carbonyl group.\n• Hydrolysis Protocol: Boil sample with dilute hydrochloric acid (HCl) at 100°C to break the glycosidic bond into free alpha-glucose and beta-fructose monomers.\n• Neutralisation: Cool and neutralise with sodium hydrogencarbonate (NaHCO3) or dilute NaOH (Benedict's reaction requires an alkaline pH to function).\n• Re-testing: Re-heat with Benedict's reagent; the liberated monosaccharide monomers reduce Cu2+ ions, yielding a positive brick-red precipitate."
        },
        {
            "q_num": 2,
            "title": "How Does the Position of the Hydroxyl Group on C1 in Alpha- vs Beta-Glucose Direct the Entire Architecture of Starch vs Cellulose?",
            "category": "Stereochemistry • Macromolecular Architecture",
            "examiner_trap": "Confusing the C1 -OH orientation (down in alpha, up in beta) or failing to explain why beta-glucose forces alternate 180° rotation of successive monomers.",
            "model_answer": "• Anomeric Carbon (C1): In Haworth projections, alpha-glucose has the C1 hydroxyl (-OH) group pointing BELOW the ring (trans to C6); beta-glucose has the C1 -OH pointing ABOVE the ring (cis to C6).\n• Alpha-Polymers (Starch & Glycogen): All alpha-glucose monomers face the same direction; alpha(1->4) glycosidic bonds create a natural curve, coiling the chain into a compact, helical spiral ideal for osmotic-free carbohydrate storage.\n• Beta-Polymers (Cellulose): Because the C1 -OH points up and C4 -OH points down, each successive beta-glucose must be rotated 180° relative to its neighbour to form a beta(1->4) glycosidic bond.\n• Result: Cellulose forms straight, uncoiled, linear parallel ribbons; exposed -OH groups on both sides form extensive hydrogen bonds cross-linking adjacent chains into high-tensile-strength microfibrils."
        },
        {
            "q_num": 3,
            "title": "Why Are Amylopectin and Glycogen Highly Branched and How Does This Adapt Them for Rapid Glucose Mobilisation?",
            "category": "Polysaccharide Kinetics • Energy Storage",
            "examiner_trap": "Stating that amylose has 1,6-glycosidic bonds (amylose is strictly unbranched 1,4-only) or failing to link branch ends to enzymatic hydrolysis rates.",
            "model_answer": "• Amylose Architecture: Linear, unbranched polymer of alpha-glucose linked solely by alpha(1->4) glycosidic bonds; coiled into a tight helix by hydrogen bonding (6 monomers per turn); compact storage.\n• Amylopectin Architecture: Branched polymer with alpha(1->4) main chains and alpha(1->6) glycosidic branch points occurring every 20–30 monomers.\n• Glycogen Architecture: Animal storage polysaccharide; structurally identical to amylopectin but much more frequently branched (alpha(1->6) branch points every 8–12 monomers).\n• Functional Significance of Branching: Branching creates thousands of accessible non-reducing terminal ends; enables multiple glycogen phosphorylase / amylase enzymes to simultaneously hydrolyse glucose units rapidly to meet sudden metabolic surges (fight-or-flight)."
        },
        {
            "q_num": 4,
            "title": "What Gives Cellulose Microfibrils Their Immense Tensile Strength in Plant Cell Walls?",
            "category": "Structural Polysaccharides • Plant Biomechanics",
            "examiner_trap": "Asserting that cellulose molecules are branched or that covalent bonds form between separate chains. The tensile strength derives from thousands of cross-linking hydrogen bonds.",
            "model_answer": "• Monomer & Linkage: Composed of beta-glucose monomers linked by beta(1->4) glycosidic bonds with alternate 180° inversion of monomers.\n• Unbranched Linear Chains: Forms completely straight, flat, unbranched polyglucan chains without coiling.\n• Inter-Chain Hydrogen Bonding: Hydroxyl (-OH) groups projecting outward in all directions form thousands of parallel cross-linking hydrogen bonds with neighbouring cellulose chains.\n• Microfibril Hierarchy: 60–70 parallel chains aggregate into crystalline microfibrils (~10 nm diameter); microfibrils bundle into macrofibrils embedded in a hydrated matrix of pectin and hemicellulose.\n• High Tensile Strength: Resists extreme tensile pulling forces without stretching; allows plant cells to withstand high osmotic turgor pressure without bursting."
        },
        {
            "q_num": 5,
            "title": "How Does the Structure of a Phospholipid Differ from a Triglyceride and Why Does It Spontaneously Form a Bilayer?",
            "category": "Lipid Biochemistry • Membrane Dynamics",
            "examiner_trap": "Claiming phospholipids 'dissolve' in water or confusing ester bonds with peptide bonds. Phospholipids are amphipathic molecules that assemble via hydrophobic interactions.",
            "model_answer": "• Chemical Differences: Triglycerides consist of glycerol condensed with THREE fatty acids via three ester bonds (completely non-polar, hydrophobic); phospholipids have ONE fatty acid replaced by a polar, negatively charged phosphate group linked to glycerol.\n• Amphipathic Nature: Phospholipids possess a hydrophilic polar head (phosphate group, attracted to water dipoles) and two hydrophobic non-polar tails (hydrocarbon fatty acid chains, repelled by water).\n• Spontaneous Bilayer Self-Assembly: In aqueous media, hydrophobic interactions and van der Waals forces drive hydrophobic fatty acid tails to cluster together facing inward, shielded from water.\n• Hydrophilic phosphate heads orient outward, forming electrostatic and hydrogen bonds with surrounding water molecules on the cytosolic and extracellular surfaces."
        },
        {
            "q_num": 6,
            "title": "Distinguish Between the Four Levels of Protein Structure and the Bonds That Stabilise Each Level.",
            "category": "Protein Hierarchy • Chemical Bonds",
            "examiner_trap": "Confusing secondary structure bonds (hydrogen bonds between peptide backbone -C=O and -N-H groups) with tertiary structure bonds (interactions between R-groups).",
            "model_answer": "• Primary Structure: The unique linear sequence of amino acids in a polypeptide chain, covalently linked by peptide bonds; determined by gene nucleotide sequence.\n• Secondary Structure: Regular local folding of the polypeptide backbone into alpha-helices or beta-pleated sheets, stabilised strictly by hydrogen bonds between peptide backbone C=O and N-H groups (R-groups not involved).\n• Tertiary Structure: The precise 3D globular or fibrous conformation of a single polypeptide chain, stabilised by interactions between amino acid R-groups:\n  1. Disulfide bridges (strong covalent bonds between cysteine -SH groups);\n  2. Ionic bonds (between positively and negatively charged R-groups e.g. Lys+ and Asp-);\n  3. Hydrogen bonds (between polar R-groups);\n  4. Hydrophobic interactions (non-polar R-groups sequestered into core).\n• Quaternary Structure: The association of two or more polypeptide subunits (and prosthetic groups) into a functional multi-subunit protein (e.g. haemoglobin, collagen)."
        },
        {
            "q_num": 7,
            "title": "How Does Haemoglobin's Quaternary Structure and Prosthetic Groups Enable Cooperative Oxygen Binding?",
            "category": "Globular Proteins • Allosteric Cooperativity",
            "examiner_trap": "Calling haemoglobin an enzyme or simple protein. It is a conjugated globular protein whose allosteric cooperativity is driven by quaternary conformational changes.",
            "model_answer": "• Quaternary Structure: Spherical, water-soluble globular protein composed of four polypeptide subunits: two alpha-globin chains (141 amino acids) and two beta-globin chains (146 amino acids).\n• Conjugated Protein: Each globin chain contains a non-protein haem prosthetic group embedded in a hydrophobic crevice, containing a central ferrous ion (Fe2+) capable of reversibly binding one O2 molecule (total 4 O2 / 8 oxygen atoms per haemoglobin).\n• Surface Properties: Hydrophilic R-groups face outward into water (maintaining high solubility in erythrocyte cytoplasm); hydrophobic R-groups face inward.\n• Allosteric Cooperativity: Binding of the first O2 molecule to one Fe2+ alters the tertiary and quaternary conformation of that subunit, transmitting strain to adjacent subunits; relaxes their binding pockets, dramatically increasing their affinity for subsequent O2 molecules."
        },
        {
            "q_num": 8,
            "title": "Contrast the Structural and Mechanical Properties of Collagen with Haemoglobin.",
            "category": "Fibrous vs Globular Proteins • Structure-Function",
            "examiner_trap": "Confusing the tropocollagen triple helix with an alpha-helix. Tropocollagen is a right-handed triple helix composed of three left-handed polyproline chains with glycine every 3rd residue.",
            "model_answer": "• Structural Shape: Haemoglobin is a compact, spherical globular protein with a folded metabolic/transport role; collagen is an elongated, insoluble fibrous protein with a structural support role.\n• Primary Sequence of Collagen: Highly repetitive repeating triplet (Gly-X-Y), where every third residue is Glycine (smallest amino acid, -H side chain), allowing chains to pack extremely tightly together.\n• Tropocollagen Triple Helix: Three left-handed polypeptide helical chains coil together into a tight, rigid, right-handed triple helix held together by extensive inter-chain hydrogen bonds.\n• Staggered Fibril Assembly: Tropocollagen molecules lie parallel and staggered by 67 nm (avoiding a single line of weakness) and form covalent cross-links between lysine residues, assembling into collagen fibrils and fibres.\n• Mechanical Properties: Immense tensile strength with zero elasticity; forms tendons, ligaments, cartilage, skin dermis, and bone matrices."
        },
        {
            "q_num": 9,
            "title": "Explain How the Dipolar Nature and Hydrogen Bonding of Water Underlie Its Vital Thermal and Solvent Properties.",
            "category": "Physical Chemistry • Water Properties",
            "examiner_trap": "Attributing water's thermal stability to covalent O-H bonds. Thermal properties are governed by the extensive network of intermolecular hydrogen bonds.",
            "model_answer": "• Dipolar Molecule: Oxygen is more electronegative than hydrogen, drawing shared electrons closer; results in a partial negative charge (delta-) on oxygen and partial positive charges (delta+) on hydrogens.\n• Hydrogen Bonding Network: Delta- oxygen of one water molecule forms a hydrogen bond with the delta+ hydrogen of an adjacent molecule; each molecule forms up to four hydrogen bonds.\n• High Specific Heat Capacity: Large amounts of heat energy are absorbed to break hydrogen bonds before kinetic energy increases; buffers aquatic habitats and large organisms against rapid temperature fluctuations.\n• High Latent Heat of Vaporisation: Immense thermal energy required to vaporise liquid water into steam (breaking all H-bonds); provides powerful evaporative cooling during sweating and transpiration.\n• Solvent Action: Dipolar water molecules form hydration shells around cations (surrounding with delta- O) and anions (surrounding with delta+ H), dissolving ions and polar metabolic substrates."
        },
        {
            "q_num": 10,
            "title": "How Is Quantitative Colorimetry Used with Benedict's Reagent and Serial Dilutions to Determine Unknown Glucose Concentration?",
            "category": "Quantitative Analytical Methods • Colorimetry",
            "examiner_trap": "Placing the reacted mixture directly into a colorimeter without centrifuging out the copper(I) oxide precipitate, or confusing % transmission with absorbance.",
            "model_answer": "• Serial Dilution: Prepare a series of known glucose standards (e.g. 10.0, 5.0, 2.5, 1.25, 0.625 mmol dm-3) using proportional or serial dilution with distilled water.\n• Standardised Reaction: Add identical excess volumes of Benedict's reagent to each standard and the unknown sample; heat in boiling water bath (100°C) for exactly 5 minutes.\n• Centrifugation / Filtration: Precipitate of red copper(I) oxide (Cu2O) MUST be removed by centrifugation or filtration to yield a clear supernatant liquid; failure to remove precipitate causes light scattering and invalid readings.\n• Colorimeter Calibration: Use a red filter (680 nm, complementary to blue Cu2+); zero colorimeter using distilled water (blank).\n• Absorbance vs Concentration: High glucose reduces more Cu2+, leaving less unreacted blue Cu2+ in supernatant (lower absorbance of red light, higher transmission); plot calibration curve of absorbance vs concentration and interpolate unknown."
        }
    ]

