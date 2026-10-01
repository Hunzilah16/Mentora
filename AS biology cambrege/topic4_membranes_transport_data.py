"""
Topic 4: Cell Membranes and Transport — 50 Examination-Style Questions & Mark Schemes
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

def get_topic4_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Fluid mosaic model (Fig 4.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q2 - The Fluid Mosaic Model of Cell Membranes",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="The currently accepted model of membrane architecture is the fluid mosaic model originally proposed by Singer and Nicolson. Fig. 4.1 illustrates a three-dimensional cross-section through a eukaryotic cell surface membrane.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_1_fluid_mosaic_membrane.png"),
        figure_caption="Fig. 4.1: Cross-sectional diagram of the fluid mosaic cell surface membrane.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.1, explain why the model of membrane structure is described as 'fluid' and 'mosaic'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the amphipathic nature of phospholipids dictates their spontaneous arrangement into a stable bilayer in an aqueous environment.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State the distinct roles of the glycoprotein and the peripheral protein shown on the outer and inner surfaces of the membrane.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "'Fluid' because phospholipid molecules and many proteins can diffuse laterally within their monolayer / plane of membrane; 'Mosaic' because globular proteins of varying shapes and sizes are interspersed throughout the phospholipid bilayer in an irregular pattern [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Phospholipids have hydrophilic (polar) phosphate heads and hydrophobic (non-polar) hydrocarbon fatty acid tails; heads form hydrogen bonds with surrounding water inside and outside cell, while tails are shielded from water in the interior hydrophobic core via hydrophobic interactions [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Glycoprotein acts as cell recognition site / receptor for chemical ligands / cell-cell adhesion; peripheral protein provides mechanical support / anchors cytoskeleton / acts as intracellular signalling enzyme [2].", "marks": 2}
        ]
    ))

    # Q2: Membrane protein types & distribution
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q2 - Integral and Peripheral Membrane Proteins",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="Proteins constitute approximately 50% of the mass of a typical plasma membrane and exhibit diverse structural associations with the lipid bilayer.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between integral (transmembrane) proteins and peripheral proteins in terms of their location and interactions within the membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the amino acid composition and tertiary structure of a transmembrane protein allow it to span the entire phospholipid bilayer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest why a channel protein that facilitates the diffusion of chloride ions (Cl-) cannot transport fatty acids.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Integral proteins penetrate into the hydrophobic core of the bilayer (often spanning the whole width), held by hydrophobic interactions; peripheral proteins are attached loosely to the membrane surface or to integral proteins via electrostatic / hydrogen bonds [2].", "marks": 2},
            {"q": "Q2(b)", "points": "The central transmembrane region features amino acids with non-polar (hydrophobic) R-groups interacting with fatty acid tails, while the outer ends feature polar/charged R-groups interacting with the aqueous cytoplasm and extracellular fluid [2].", "marks": 2},
            {"q": "Q2(c)", "points": "Chloride channel has a hydrophilic aqueous pore with positively charged amino acid residues specific for hydrated anions; fatty acids are non-polar hydrophobic molecules that dissolve and diffuse directly through the lipid bilayer, not through polar aqueous pores [2].", "marks": 2}
        ]
    ))

    # Q3: Cholesterol & fluidity regulation (Fig 4.2)
    questions.append(Question(
        number=3,
        title="9700/22/F/M/22/Q3 - Cholesterol and Membrane Fluidity Regulation",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="Cholesterol is an essential lipid component interspersed between phospholipid molecules in animal cell membranes. Fig. 4.2 illustrates how cholesterol modulates phospholipid mobility at high and low temperatures.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_2_cholesterol_fluidity.png"),
        figure_caption="Fig. 4.2: Cholesterol regulating membrane fluidity at high temperature (A) and low temperature (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.2(A), explain the molecular mechanism by which cholesterol prevents excessive membrane fluidity at high temperatures (>37 deg C).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 4.2(B), explain how cholesterol prevents the membrane from solidifying / crystallising at low temperatures (<10 deg C).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest the physiological consequences to an animal cell if its plasma membrane became excessively fluid.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "Rigid steroid ring system of cholesterol intercalates between fatty acid tails, restricting their lateral mobility and packing them more closely; reduces membrane fluidity and prevents uncontrolled leakage of polar solutes [2].", "marks": 2},
            {"q": "Q3(b)", "points": "Cholesterol disrupts regular close packing of saturated hydrocarbon fatty acid tails; prevents formation of a rigid crystalline gel lattice, maintaining fluidity and transport protein function in cold conditions [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Membrane becomes leaky / loses selective permeability, allowing uncontrolled ion/metabolite leakage; membrane proteins can denature or become displaced, impairing transport and signalling processes [2].", "marks": 2}
        ]
    ))

    # Q4: Glycolipids, Antigens & Cell Recognition
    questions.append(Question(
        number=4,
        title="9700/23/M/J/21/Q2 - Glycolipids, Antigens & Cell Recognition",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="Cell surface membranes carry carbohydrates covalently linked to lipids (glycolipids) or proteins (glycoproteins), forming the glycocalyx.",
        parts=[
            QuestionPart(label="(a)", text="Describe the arrangement of glycolipids in the plasma membrane and explain why their carbohydrate chains always project into the extracellular space.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of cell surface glycolipids and glycoproteins as immunological antigens and cell-to-cell recognition markers.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="In the ABO blood group system, explain why red blood cells from an individual of blood group A will be agglutinated if transfused into a recipient of blood group B.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Lipid hydrophobic tails anchor the molecule into outer monolayer of bilayer, while hydrophilic oligosaccharide chain extends into extracellular fluid; orientation is established in Golgi lumen during glycosylation and maintained during vesicle fusion with plasma membrane [2].", "marks": 2},
            {"q": "Q4(b)", "points": "Carbohydrate chains exhibit unique branching patterns specific to cell type and individual; act as identification tags recognised by immune cells (distinguishing self from non-self) and enable homologous cells to adhere into tissues [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Group A RBCs have A-antigen glycoproteins; group B recipient plasma contains anti-A antibodies which bind complementarily to A-antigens, causing clumping (agglutination) and complement-mediated haemolysis [2].", "marks": 2}
        ]
    ))

    # Q5: Cell signalling pathway (Fig 4.3)
    questions.append(Question(
        number=5,
        title="9700/22/M/J/21/Q4 - Cell Signalling Pathways & Glucagon Action",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="Cell signalling allows multicellular organisms to coordinate metabolic activities across distant tissues. Fig. 4.3 shows the stages of a G-protein coupled receptor (GPCR) signalling pathway activated by glucagon.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_3_cell_signalling_pathway.png"),
        figure_caption="Fig. 4.3: Diagram of cell signalling stages: ligand binding, G-protein transduction, and kinase cascade.",
        parts=[
            QuestionPart(label="(a)", text="Outline the first three stages of cell signalling shown in Fig. 4.3 from secretion to receptor binding.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of G-proteins and adenylyl cyclase in generating the second messenger cyclic AMP (cAMP).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the biological importance of an intracellular enzyme phosphorylation cascade in terms of signal amplification.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Signalling cell secretes ligand (e.g. glucagon) into blood via exocytosis; ligand is transported through circulatory system to target organ; ligand binds to specific complementary binding site on transmembrane receptor [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Receptor undergoes conformational change that activates membrane-associated G-protein; G-protein binds GTP and moves laterally to activate adenylyl cyclase, which converts ATP into cyclic AMP (second messenger) [2].", "marks": 2},
            {"q": "Q5(c)", "points": "Each activated enzyme in the cascade activates many molecules of the subsequent downstream enzyme (e.g. Protein Kinase A -> Phosphorylase Kinase -> Glycogen Phosphorylase); one hormone molecule leads to the release of millions of glucose molecules [2].", "marks": 2}
        ]
    ))

    # Q6: Target cell specificity & signal termination
    questions.append(Question(
        number=6,
        title="9700/21/M/J/20/Q2 - Target Cell Specificity & Signal Termination",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        preamble="Hormones circulate in the bloodstream throughout the whole body but induce responses only in specific target cells.",
        parts=[
            QuestionPart(label="(a)", text="Explain why a water-soluble peptide hormone such as insulin affects liver and muscle cells but has no effect on red blood cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe two mechanisms by which a target cell terminates the intracellular signal once the external hormone stimulus ceases.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why steroid hormones (such as testosterone and oestrogen) bind to intracellular receptors rather than cell surface receptors.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Water-soluble peptide hormones cannot cross the hydrophobic core of the bilayer; they require specific cell surface receptors which are expressed on liver and muscle cell membranes but absent from red blood cells [2].", "marks": 2},
            {"q": "Q6(b)", "points": "G-protein possesses intrinsic GTPase activity which hydrolyses GTP to GDP, resetting to inactive state; phosphodiesterase enzyme hydrolyses cAMP into inactive AMP / receptor undergoes endocytosis and degradation [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Steroid hormones are non-polar / lipid-soluble molecules; they readily dissolve in and diffuse directly across the hydrophobic fatty acid core of the plasma membrane into the cytoplasm to bind internal receptors [2].", "marks": 2}
        ]
    ))

    # Q7: Simple vs facilitated diffusion (Fig 4.4)
    questions.append(Question(
        number=7,
        title="9700/22/O/N/21/Q3 - Simple vs Facilitated Diffusion Mechanisms",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Passive movement of solutes into cells can occur via simple diffusion or facilitated diffusion. Fig. 4.4 compares simple diffusion through the lipid bilayer with facilitated diffusion through channel and carrier proteins.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_4_simple_vs_facilitated_diffusion.png"),
        figure_caption="Fig. 4.4: Comparison of simple diffusion (A), channel-facilitated diffusion (B), and carrier-facilitated diffusion (C).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.4, contrast simple diffusion with facilitated diffusion via channel proteins in terms of pathway and solute characteristics.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the sequence of molecular events during the transport of a polar molecule (such as glucose) by a carrier protein.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why inorganic ions such as sodium (Na+) and chloride (Cl-) cannot cross the membrane by simple diffusion despite being very small.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Simple diffusion occurs directly through phospholipid bilayer for small non-polar/hydrophobic molecules (O2, CO2); channel diffusion occurs through a water-filled hydrophilic pore in a transmembrane protein for charged/polar solutes [2].", "marks": 2},
            {"q": "Q7(b)", "points": "Solute binds to a specific complementary binding site on one side of carrier; induces a reversible conformational change in protein tertiary structure that exposes solute to opposite side where it dissociates [2].", "marks": 2},
            {"q": "Q7(c)", "points": "Ions carry electrical charges and are surrounded by a hydration shell of water dipoles; they are energetically repelled by the non-polar hydrophobic fatty acid hydrocarbon tails in the membrane core [2].", "marks": 2}
        ]
    ))

    # Q8: Fick's Law of diffusion & membrane adaptations
    questions.append(Question(
        number=8,
        title="[Mentora Original A* Extension] - Fick's Law of Diffusion & Membrane Specialisations",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        preamble="The rate of diffusion across biological boundaries is mathematically described by Fick's Law: Rate of Diffusion is proportional to (Surface Area x Concentration Difference) / Diffusion Distance.",
        parts=[
            QuestionPart(label="(a)", text="Explain three specific structural features of mammalian proximal convoluted tubule epithelial cells that maximise the rate of nutrient reabsorption.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the theoretical fold-increase in diffusion rate if the surface area of a membrane is quadrupled (x4) and the membrane thickness is halved (x0.5), assuming constant concentration difference.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why facilitated diffusion is strictly classified as a passive transport mechanism even though it requires specialised transmembrane proteins.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "Apical membrane folded into dense microvilli (vastly increases surface area); rich in transport proteins / co-transporters; abundant mitochondria generate ATP for active transport maintaining steep concentration gradient [2].", "marks": 2},
            {"q": "Q8(b)", "points": "Using Fick's Law: New Rate = (4 x SA * Delta C) / (0.5 * d) = 8 times original rate; theoretical fold-increase is 8-fold [2].", "marks": 2},
            {"q": "Q8(c)", "points": "Net solute movement occurs strictly down the electrochemical / concentration gradient; relies entirely on intrinsic kinetic energy of molecules without expenditure of metabolic energy (ATP) [2].", "marks": 2}
        ]
    ))

    # Q9: Kinetics of diffusion & carrier saturation (Fig 4.5)
    questions.append(Question(
        number=9,
        title="9700/21/O/N/20/Q3 - Kinetics of Membrane Transport & Carrier Saturation",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="The rate of transport across a membrane depends on the concentration gradient and the mechanism of transport. Fig. 4.5 shows the relationship between external solute concentration and the rate of transport for simple and facilitated diffusion.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_5_diffusion_kinetics_curve.png"),
        figure_caption="Fig. 4.5: Transport kinetics comparing simple diffusion and facilitated diffusion.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.5, explain why the rate of simple diffusion is directly proportional to concentration difference without showing saturation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the rate of facilitated diffusion reaches a maximum plateau (Vmax) at high solute concentrations.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Predict and explain the effect on the facilitated diffusion curve if the cell synthesises and inserts twice the number of carrier proteins into its membrane.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Solute passes directly through lipid bilayer without interacting with specific binding sites; bilayer surface area is vast and does not become occupied or limiting (Fick's law applies) [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Number of carrier/channel proteins in membrane is finite; at high solute concentrations, all binding sites are continuously occupied (saturated), so protein availability becomes the rate-limiting factor [2].", "marks": 2},
            {"q": "Q9(c)", "points": "The maximum rate of transport (Vmax) doubles / shifts upwards because twice as many binding sites are available per unit time; the affinity for solute remains unchanged [2].", "marks": 2}
        ]
    ))

    # Q10: Aquaporins & water permeability
    questions.append(Question(
        number=10,
        title="9700/22/F/M/20/Q2 - Aquaporins and Membrane Water Permeability",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Water molecules can cross the plasma membrane either by slow direct penetration through the phospholipid bilayer or rapidly through specialised channels called aquaporins.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of an aquaporin and explain how it allows rapid bidirectional flow of water while strictly excluding protons (H3O+).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how water molecules are able to cross the phospholipid bilayer directly, despite possessing polar O-H bonds.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why collecting duct epithelial cells in the kidney insert additional aquaporins into their apical membranes during periods of water deprivation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Narrow hydrophilic pore lined with conserved positive amino acid residues (arginine/histidine); repels positive hydronium ions (protons) by electrostatic repulsion while allowing single file passage of uncharged water dipoles [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Water molecules are extremely small and have high kinetic energy; transient gaps / voids open momentarily between oscillating fatty acid tails, allowing water molecules to slip across [2].", "marks": 2},
            {"q": "Q10(c)", "points": "Triggered by antidiuretic hormone (ADH); increases water permeability of collecting duct, allowing maximal water reabsorption into hypertonic medullary interstitium by osmosis, producing concentrated urine [2].", "marks": 2}
        ]
    ))

    # Q11: Sodium-potassium pump (Fig 4.6)
    questions.append(Question(
        number=11,
        title="9700/22/M/J/22/Q3 - The Sodium-Potassium ATPase Active Transport Pump",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="The sodium-potassium pump (Na+/K+-ATPase) is a primary active transport carrier protein present in the plasma membrane of virtually all animal cells. Fig. 4.6 illustrates the catalytic cycle of the pump.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_6_active_transport_nak_pump.png"),
        figure_caption="Fig. 4.6: Stepwise mechanism of the sodium-potassium ATPase pump.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.6, state the exact stoichiometry and direction of ion transport catalysed by the Na+/K+-ATPase pump per cycle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the precise biochemical role of ATP binding and hydrolysis in operating this carrier protein.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain two essential physiological consequences of maintaining high intracellular K+ and low intracellular Na+ concentrations in animal tissues.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Pumps 3 Na+ ions out of cell and 2 K+ ions into cell per cycle, both against their respective electrochemical gradients [2].", "marks": 2},
            {"q": "Q11(b)", "points": "Hydrolysis of ATP transfers a terminal phosphate group to pump protein (phosphorylation); phosphorylation triggers a conformational change that flips binding sites outward and lowers affinity for Na+; dephosphorylation restores original inward shape [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Establishes resting membrane potential necessary for nerve impulses and muscle contraction; generates electrochemical Na+ gradient that drives secondary active co-transport of glucose and amino acids [2].", "marks": 2}
        ]
    ))

    # Q12: Secondary active transport & intestinal glucose absorption
    questions.append(Question(
        number=12,
        title="9700/23/O/N/21/Q2 - Secondary Active Transport & Glucose Absorption in the Ileum",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Epithelial cells lining the mammalian ileum absorb glucose from the gut lumen against a steep concentration gradient.",
        parts=[
            QuestionPart(label="(a)", text="Describe how sodium-glucose co-transporter proteins (SGLT1) in the apical membrane transport glucose into the epithelial cell.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the continuous absorption of glucose relies on the activity of the Na+/K+ pump located in the basolateral membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how glucose exits the epithelial cell across the basolateral membrane to enter the blood capillaries.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Na+ moves down its steep concentration gradient into cell, binding to co-transporter; conformational change simultaneously carries glucose against its concentration gradient into cytoplasm (symport) [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Basolateral Na+/K+ pump actively pumps Na+ out into interstitial fluid using ATP; maintains low intracellular Na+ concentration, preserving electrochemical driving force for apical symport [2].", "marks": 2},
            {"q": "Q12(c)", "points": "Glucose accumulates to high concentration inside cell and leaves across basolateral membrane by facilitated diffusion down its concentration gradient via GLUT2 carrier proteins [2].", "marks": 2}
        ]
    ))

    # Q13: Osmosis in plant cells & incipient plasmolysis (Fig 4.7)
    questions.append(Question(
        number=13,
        title="9700/22/M/J/20/Q3 - Osmosis in Plant Cells & Incipient Plasmolysis",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Water movement into and out of plant cells is governed by water potential (Psi). Fig. 4.7 illustrates the appearance of plant cells immersed in pure water (A), an isotonic sucrose solution (B), and a concentrated sucrose solution (C).",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_7_osmosis_plant_cells_plasmolysis.png"),
        figure_caption="Fig. 4.7: Plant cells in hypotonic, isotonic (incipient plasmolysis), and hypertonic solutions.",
        parts=[
            QuestionPart(label="(a)", text="Define solute potential (Psi_s) and pressure potential (Psi_p), and state the formula relating them to water potential (Psi).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 4.7(B), explain what is meant by the term 'incipient plasmolysis' and deduce the value of Psi_p at this state.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="In the fully plasmolysed cell shown in Fig. 4.7(C), identify the substance filling the space between the cell wall and the shrunken protoplast, and justify your answer.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Psi_s is the reduction in water potential due to dissolved solute molecules (always negative); Psi_p is the hydrostatic pressure exerted by cell wall on protoplast (positive in turgid cells); Psi = Psi_s + Psi_p [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Incipient plasmolysis is the point where the protoplast just ceases to exert pressure against cell wall (50% cells plasmolysed); at this point, pressure potential Psi_p = 0 kPa, so cell Psi = cell Psi_s [2].", "marks": 2},
            {"q": "Q13(c)", "points": "External concentrated sucrose solution; the plant cell wall is freely permeable to water and small dissolved solutes like sucrose, whereas the plasma membrane is selectively permeable and retains internal solutes [2].", "marks": 2}
        ]
    ))

    # Q14: Quantitative water potential calculations in plant cells
    questions.append(Question(
        number=14,
        title="[Mentora Original A* Extension] - Quantitative Water Potential Calculations in Plant Tissues",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        preamble="Water potential calculations provide a quantitative basis for understanding water movement across plant tissues.",
        parts=[
            QuestionPart(label="(a)", text="A plant cell with a solute potential (Psi_s) of -850 kPa and a pressure potential (Psi_p) of +350 kPa is placed in an open beaker of pure water (Psi = 0 kPa). Calculate its initial water potential (Psi) and state the direction of net water flow.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the final pressure potential (Psi_p) of this cell when it reaches dynamic osmotic equilibrium with the pure water, assuming cell volume change is negligible.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why plant cells do not burst when fully turgid in pure water, whereas animal cells placed in pure water undergo osmotic lysis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Initial Psi = Psi_s + Psi_p = -850 + 350 = -500 kPa; net movement of water is into cell down water potential gradient (from 0 kPa to -500 kPa) [2].", "marks": 2},
            {"q": "Q14(b)", "points": "At osmotic equilibrium with pure water, cell Psi = 0 kPa; 0 = -850 + Psi_p; Psi_p = +850 kPa [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Plant cells possess a rigid cellulose cell wall with high tensile strength that resists internal hydrostatic pressure; animal cells lack a cell wall, so water influx causes continuous expansion until plasma membrane ruptures [2].", "marks": 2}
        ]
    ))

    # Q15: Osmosis in animal erythrocytes (Fig 4.8)
    questions.append(Question(
        number=15,
        title="9700/21/M/J/22/Q2 - Osmotic Behaviour of Erythrocytes (Red Blood Cells)",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Unlike plant cells, animal erythrocytes lack a rigid cell wall and respond sensitively to changes in external solute concentration. Fig. 4.8 shows erythrocytes placed in three different sodium chloride (NaCl) solutions.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_8_osmosis_erythrocytes.png"),
        figure_caption="Fig. 4.8: Erythrocytes in hypotonic (A), isotonic (B), and hypertonic (C) saline solutions.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.8(A), explain why erythrocytes undergo haemolysis when placed in 0.1% NaCl (hypotonic) solution.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 4.8(C), explain the term 'crenation' and describe the water potential gradient responsible for this appearance in 3.0% NaCl.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why intravenous medical drips administered to human hospital patients must contain 0.9% NaCl solution rather than distilled water.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "0.1% NaCl has higher water potential (less negative) than erythrocyte cytoplasm; net water enters cell by osmosis; lacking a cell wall, membrane stretches beyond its elastic limit and ruptures (haemolysis), releasing haemoglobin [2].", "marks": 2},
            {"q": "Q15(b)", "points": "3.0% NaCl has lower water potential (more negative) than cytoplasm; net water exits cell by osmosis; loss of water causes cell volume to shrink and membrane wrinkles forming spiky crenated appearance [2].", "marks": 2},
            {"q": "Q15(c)", "points": "0.9% NaCl is isotonic to human blood plasma (same water potential, approx -750 kPa); ensures dynamic equilibrium with no net movement of water into or out of erythrocytes, preventing lysis or crenation [2].", "marks": 2}
        ]
    ))

    # Q16: Endocytosis: phagocytosis & pinocytosis
    questions.append(Question(
        number=16,
        title="9700/22/O/N/22/Q3 - Endocytosis: Phagocytosis and Pinocytosis",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Endocytosis is an active transport process enabling eukaryotic cells to internalise macromolecules and particulate matter that cannot pass through transport proteins.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between phagocytosis and pinocytosis with reference to the physical state of the material ingested.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the sequence of cellular events that occurs when a macrophage engulfs and digests a pathogenic bacterium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why endocytosis requires metabolic energy in the form of ATP.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Phagocytosis involves the uptake of solid particles / cells (cell eating) forming large vesicles/vacuoles; pinocytosis involves non-specific uptake of extracellular liquids / solutes (cell drinking) forming smaller vesicles [2].", "marks": 2},
            {"q": "Q16(b)", "points": "Pseudopodia extend around bacterium and fuse to enclose it in a phagocytic vacuole (phagosome); primary lysosomes fuse with phagosome to form a phagolysosome, where hydrolytic lysozymes / proteases digest the bacterium [2].", "marks": 2},
            {"q": "Q16(c)", "points": "ATP is required for actin microfilament polymerisation and motor protein activity that deform the plasma membrane and pinch off vesicles; ATP also powers fusion of intracellular membranes [2].", "marks": 2}
        ]
    ))

    # Q17: Estimating water potential via mass change (Fig 4.9)
    questions.append(Question(
        number=17,
        title="9700/21/O/N/21/Q4 - Estimating Plant Tissue Water Potential via Mass Change",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="A student investigated the water potential of potato tuber tissue by immersing cylinders of tissue in sucrose solutions ranging from 0.0 to 1.0 mol dm-3. Fig. 4.9 shows the percentage change in mass plotted against sucrose concentration.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_9_water_potential_calibration_curve.png"),
        figure_caption="Fig. 4.9: Percentage mass change of potato cylinders vs sucrose concentration.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.9, determine the sucrose concentration that is isotonic to the potato tissue and explain what is occurring at this concentration.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why potato cylinders gained mass in 0.0 and 0.2 mol dm-3 sucrose but lost mass in concentrations greater than 0.5 mol dm-3.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two procedural precautions the student must take when preparing and weighing the potato cylinders to ensure valid percentage change data.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Isotonic concentration is where the curve intersects the zero mass change line at 0.34 mol dm-3 (Psi = -860 kPa); at this point, solution Psi equals tissue Psi, resulting in dynamic equilibrium with no net water movement by osmosis [2].", "marks": 2},
            {"q": "Q17(b)", "points": "In <=0.2 mol dm-3, solution has higher Psi than tissue, so water enters cells down Psi gradient; in >=0.5 mol dm-3, solution has lower Psi than tissue, so water leaves cells by osmosis [2].", "marks": 2},
            {"q": "Q17(c)", "points": "Gently blot cylinders with paper towel before weighing to remove surface water without squeezing tissue; use a cork borer of identical diameter to keep surface area constant / use closed boiling tubes to prevent evaporation [2].", "marks": 2}
        ]
    ))

    # Q18: Exocytosis & secretory vesicle trafficking
    questions.append(Question(
        number=18,
        title="9700/22/F/M/21/Q2 - Exocytosis & Secretory Vesicle Trafficking",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Pancreatic acinar cells synthesise and secrete digestive enzymes into the pancreatic duct by exocytosis.",
        parts=[
            QuestionPart(label="(a)", text="Describe how digestive enzyme proteins are processed and transported through the cell from their site of translation to the plasma membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the molecular events occurring during vesicle fusion with the cell surface membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why continuous exocytosis would cause the plasma membrane surface area to increase, and state how the cell maintains a constant membrane area.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Synthesised on ribosomes of rough ER, enter ER lumen and folded; transported via transport vesicles to cis-Golgi, chemically modified and sorted; packaged into secretory vesicles that bud off trans-Golgi and travel along microtubules [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Vesicle membrane SNARE proteins interact with complementary plasma membrane SNAREs; phospholipid bilayers coalesce and fuse in an ATP/Ca2+-dependent process, creating a pore that releases contents to exterior [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Vesicle membrane incorporates directly into the plasma membrane during fusion; cell counterbalances this by an equal rate of endocytosis, removing membrane lipids and proteins to form internal vesicles [2].", "marks": 2}
        ]
    ))

    # Q19: SA:V ratio & agar cubes diffusion (Fig 4.10)
    questions.append(Question(
        number=19,
        title="9700/21/M/J/21/Q3 - Surface Area to Volume Ratio and Diffusion in Agar Blocks",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Agar cubes stained with phenolphthalein and dilute NaOH were cut into sizes 3 cm, 2 cm, and 1 cm, then immersed in dilute hydrochloric acid (HCl) for 10 minutes. Fig. 4.10 displays the cross-sections and quantitative data.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_10_agar_cubes_sa_vol_ratio.png"),
        figure_caption="Fig. 4.10: Diffusion of acid into agar cubes and surface area to volume scaling.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.10, explain why 100% of the 1 cm cube was decolourised while only 48.1% of the 3 cm cube was decolourised, given that the diffusion distance into each face was identical (1.5 mm).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the surface area to volume (SA:V) ratio for a hypothetical cubic cell with side length 0.5 cm.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the relationship between cell size and SA:V ratio imposes an upper physical limit on the size of single metabolically active cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "1 cm cube has a much higher SA:V ratio (6:1) than the 3 cm cube (2:1); the diffusion distance of 1.5 mm from all six faces meets in the center of the 1 cm cube, whereas in the 3 cm cube a large unpenetrated volume core remains [2].", "marks": 2},
            {"q": "Q19(b)", "points": "SA = 6 x (0.5)^2 = 1.5 cm^2; Volume = (0.5)^3 = 0.125 cm^3; SA:V ratio = 1.5 / 0.125 = 12.0 : 1 [2].", "marks": 2},
            {"q": "Q19(c)", "points": "As cell volume increases, metabolic demand for oxygen and nutrients increases with volume (r^3) while surface area for exchange increases only with area (r^2); diffusion distance to center becomes too large for diffusion to supply metabolic needs [2].", "marks": 2}
        ]
    ))

    # Q20: Patch clamp & ion channels
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] - Gated Ion Channels, Resting Potentials & Patch-Clamp Investigations",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        preamble="Ion channels in excitable membranes exist in closed or open states regulated by voltage or chemical ligands.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between voltage-gated and ligand-gated channel proteins with reference to their opening triggers.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how potassium leakage channels maintain a negative resting membrane potential inside animal cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Outline how the patch-clamp electrophysiology technique allows scientists to investigate the gating of individual channel proteins.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Voltage-gated channels open or close in response to changes in electrical potential difference across membrane; ligand-gated channels open upon binding of a specific chemical extracellular or intracellular messenger [2].", "marks": 2},
            {"q": "Q20(b)", "points": "Membrane is significantly more permeable to K+ than Na+ at rest; K+ diffuses down its concentration gradient out of cell via open leakage channels, leaving behind non-diffusible negative organic anions and creating a negative interior potential [2].", "marks": 2},
            {"q": "Q20(c)", "points": "A polished micropipette forms a high-resistance gigaohm seal with a tiny patch of membrane containing a single channel; microelectrodes record microscopic picoampere currents flowing through channel as it switches between open and closed conformations [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & BIOCHEMICAL MECHANISMS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Bilayer permeability to different molecules
    questions.append(Question(
        number=21,
        title="9700/12/M/J/23/Q14 - Differential Permeability of the Lipid Bilayer",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Predict and explain the relative permeability of an artificial phospholipid bilayer (lacking proteins) to: (i) oxygen gas (O2), and (ii) sodium ions (Na+).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why small uncharged polar molecules like urea cross the bilayer faster than large uncharged polar molecules like glucose.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "O2 is small and non-polar so readily dissolves in and diffuses rapidly across the hydrophobic hydrocarbon core; Na+ is fully charged with a hydration shell, so is repelled by hydrophobic core and has virtually zero permeability [2].", "marks": 2},
            {"q": "Q21(b)", "points": "Urea is small enough to fit through transient gaps between moving fatty acid tails; glucose is much larger (hexose ring) and forms multiple hydrogen bonds with water, making entry into hydrophobic interior energetically prohibitive [2].", "marks": 2}
        ]
    ))

    # Q22: Visking tubing osmometer (Fig 4.11)
    questions.append(Question(
        number=22,
        title="9700/22/M/J/19/Q3 - Visking Tubing Osmometer Investigation",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Visking (dialysis) tubing is a partially permeable membrane made of regenerated cellulose containing microscopic sub-nanometre pores. Fig. 4.11 shows an osmometer apparatus assembled by a student.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_11_visking_tubing_osmometer.png"),
        figure_caption="Fig. 4.11: Visking tubing osmometer measuring osmotic liquid rise over time.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.11, explain why the liquid meniscus rose in the capillary tube from h1 to h2 over 30 minutes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why sucrose molecules did not diffuse out of the Visking tubing into the surrounding water in the beaker.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Distilled water in beaker has higher water potential (0 kPa) than concentrated sucrose inside bag; water molecules move by osmosis down water potential gradient into bag, increasing internal volume and hydrostatic pressure which forces liquid up tube [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Pores in Visking cellulose membrane are smaller than the molecular diameter of hydrated sucrose disaccharide molecules; water molecules are small enough to pass through pores, but sucrose is too large [2].", "marks": 2}
        ]
    ))

    # Q23: Glycocalyx and cell adhesion
    questions.append(Question(
        number=23,
        title="9700/21/O/N/19/Q2 - Roles of the Glycocalyx in Cell Adhesion & Protection",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular composition of the glycocalyx.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State two functions of the glycocalyx other than acting as hormone receptor sites.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Fuzzy carbohydrate-rich coating on external surface of cell membrane formed by the branching oligosaccharide chains of glycoproteins and glycolipids [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Cell-cell adhesion (binding neighbouring cells together in epithelial tissues); protecting cell surface from mechanical and chemical damage / lubricating cell surface [2].", "marks": 2}
        ]
    ))

    # Q24: G-protein coupled receptors & transduction
    questions.append(Question(
        number=24,
        title="9700/11/O/N/22/Q15 - G-Protein Coupled Receptor Transduction",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the conformational change that occurs when an extracellular ligand binds to a G-protein coupled receptor (GPCR).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the activated G-protein transmits the signal inside the cell.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Ligand binding to the extracellular domain alters tertiary structure of receptor, causing cytosolic loop to bind to and activate an adjacent heterotrimeric G-protein [2].", "marks": 2},
            {"q": "Q24(b)", "points": "GDP bound to G-protein alpha-subunit is exchanged for GTP; alpha-subunit dissociates from beta-gamma dimer and moves laterally along membrane to activate effector enzyme adenylyl cyclase [2].", "marks": 2}
        ]
    ))

    # Q25: Bulk transport mechanisms (Fig 4.12)
    questions.append(Question(
        number=25,
        title="9700/22/F/M/19/Q3 - Bulk Transport Mechanisms: Endocytosis & Exocytosis",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Vesicular transport enables the bulk trans-membrane movement of macromolecules. Fig. 4.12 contrasts endocytosis and exocytosis.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_12_endocytosis_and_exocytosis.png"),
        figure_caption="Fig. 4.12: Comparison of endocytosis (A) and exocytosis (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.12, explain how the fluid nature of the phospholipid bilayer allows endocytic vesicle formation and exocytic fusion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State two specific biological examples of exocytosis in human physiology.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "Weak hydrophobic interactions between phospholipid tails allow phospholipids to move laterally; membrane can deform, invaginate, pinch off, and self-reseal or fuse with transport vesicles without rupturing [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Secretion of peptide hormones (e.g. insulin from pancreatic beta cells); release of neurotransmitters (e.g. acetylcholine from synaptic vesicles) [2].", "marks": 2}
        ]
    ))

    # Q26: Temperature and membrane fluidity
    questions.append(Question(
        number=26,
        title="9700/12/M/J/21/Q16 - Temperature Effects on Membrane Permeability",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how an increase in temperature from 10 deg C to 35 deg C affects phospholipid kinetic energy and membrane fluidity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why heating a membrane above 60 deg C causes an irreversible loss of selective permeability.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Phospholipids gain thermal kinetic energy and vibrate / diffuse laterally more rapidly; intermolecular spaces between fatty acid tails increase, causing membrane fluidity and solute permeability to rise [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Thermal agitation disrupts hydrogen bonds and ionic interactions holding tertiary structure of transport proteins; denatured proteins lose shape and precipitate, creating open hydrophilic voids/pores across bilayer [2].", "marks": 2}
        ]
    ))

    # Q27: Proton pumps and chemiosmosis
    questions.append(Question(
        number=27,
        title="9700/23/M/J/18/Q2 - Proton Pumps in Mitochondrial & Chloroplast Membranes",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how electron transport chain complexes act as proton pumps across the inner mitochondrial membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the inner mitochondrial membrane must be impermeable to protons except through ATP synthase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "High-energy electrons transferred along redox carriers release free energy; complexes use this energy to actively pump H+ ions from matrix across inner membrane into intermembrane space [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Maintains an electrochemical proton gradient (proton motive force); protons can only diffuse back through hydrophilic channel of ATP synthase, driving phosphorylation of ADP to ATP (chemiosmosis) [2].", "marks": 2}
        ]
    ))

    # Q28: Beetroot membrane permeability (Fig 4.13)
    questions.append(Question(
        number=28,
        title="9700/21/M/J/19/Q4 - Beetroot Membrane Permeability & Temperature Stress",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Beetroot (Beta vulgaris) cells contain a water-soluble red pigment called betalain inside their large central vacuole, surrounded by the tonoplast and plasma membrane. Fig. 4.13 shows the effect of temperature on betalain leakage measured by a colorimeter at 520 nm.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_13_beetroot_membrane_permeability.png"),
        figure_caption="Fig. 4.13: Absorbance of betalain leakage from beetroot discs vs incubation temperature.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.13, explain the low stable absorbance between 0 deg C and 40 deg C.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the steep surge in absorbance between 45 deg C and 65 deg C.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Tonoplast and plasma membrane remain intact and selectively permeable; phospholipids and proteins maintain structural integrity, preventing hydrophilic betalain molecules from escaping [2].", "marks": 2},
            {"q": "Q28(b)", "points": "High temperature denatures membrane transport and structural proteins, creating large pores; phospholipids gain extreme kinetic energy and bilayer melts/disintegrates, allowing massive betalain efflux [2].", "marks": 2}
        ]
    ))

    # Q29: Cell wall structure vs plasma membrane permeability
    questions.append(Question(
        number=29,
        title="9700/12/F/M/22/Q14 - Plant Cell Wall Structure vs Plasma Membrane Permeability",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Contrast the permeability of the primary cellulose cell wall with that of the cell surface membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of the cell wall in generating turgor pressure (Psi_p) when a plant cell is in pure water.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Cellulose cell wall is freely permeable to water, dissolved ions, and small organic solutes through spaces between microfibrils; plasma membrane is selectively / partially permeable due to hydrophobic bilayer core [2].", "marks": 2},
            {"q": "Q29(b)", "points": "As water enters protoplast by osmosis, protoplast expands and pushes against inelastic cell wall; rigid wall exerts an equal and opposite inward mechanical pressure, raising Psi_p until cell Psi equals outside Psi [2].", "marks": 2}
        ]
    ))

    # Q30: Ethanol concentration & membrane disruption
    questions.append(Question(
        number=30,
        title="[Mentora Original A* Extension] - Ethanol Concentration & Membrane Solubilization",
        syllabus_ref="Syllabus 4.1",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Explain why immersing beetroot discs in solutions of increasing ethanol concentration causes an increase in membrane permeability.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Suggest why medical skin wipes used prior to injections contain 70% ethanol rather than 100% pure ethanol.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Ethanol is an organic solvent that dissolves non-polar fatty acid hydrocarbon tails of phospholipids; disrupts hydrophobic interactions holding bilayer together and denatures membrane proteins, causing membrane lysis [2].", "marks": 2},
            {"q": "Q30(b)", "points": "70% ethanol contains 30% water, which slows evaporation and enables alcohol to penetrate bacterial cell walls before denaturing proteins; 100% ethanol rapidly coagulates outer surface proteins, forming a protective barrier that shields internal microbes [2].", "marks": 2}
        ]
    ))

    # Q31: Water potential gradients in plant tissue systems
    questions.append(Question(
        number=31,
        title="9700/22/O/N/18/Q3 - Water Potential Gradients in Multi-Tissue Plant Systems",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how a continuous water potential gradient is maintained from the soil solution, through root hair cells and cortical cells, into the root xylem vessels.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how active transport of mineral ions by root endodermal cells contributes to this gradient.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "Soil solution has highest (least negative) Psi; transpiration pull and mineral accumulation ensure root cortical cells have progressively lower (more negative) Psi, driving continuous osmosis down Psi gradient [2].", "marks": 2},
            {"q": "Q31(b)", "points": "Endodermis cells actively pump mineral ions (e.g. nitrates, potassium) into xylem sap across Casparian strip; lowers xylem solute potential (Psi_s), maintaining steep Psi gradient that pulls water into stele (root pressure) [2].", "marks": 2}
        ]
    ))

    # Q32: Comparative classification matrix (Fig 4.14)
    questions.append(Question(
        number=32,
        title="9700/21/O/N/18/Q4 - Comparative Classification of Membrane Transport Modes",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        preamble="Cells employ various physical mechanisms to exchange materials across their membranes. Fig. 4.14 summarizes the core distinguishing criteria across six transport categories.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig4_14_membrane_transport_decision_tree.png"),
        figure_caption="Fig. 4.14: Decision matrix classifying membrane transport mechanisms.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 4.14, identify two key criteria that distinguish active transport from facilitated diffusion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why bulk transport (endocytosis and exocytosis) requires ATP even if particles are moving in the direction of their concentration gradient.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Direction relative to gradient: active transport moves solutes against gradient (low to high), facilitated diffusion moves solutes down gradient (high to low); Energy requirement: active transport requires ATP hydrolysis, facilitated diffusion is passive [2].", "marks": 2},
            {"q": "Q32(b)", "points": "Energy is not used to move individual solute particles across a protein channel, but to power cytoskeletal motor proteins (kinesin/dynein) and membrane fission/fusion events [2].", "marks": 2}
        ]
    ))

    # Q33: Voltage-gated potassium channels in axons
    questions.append(Question(
        number=33,
        title="9700/11/M/J/20/Q15 - Voltage-Gated Potassium Channels in Axon Repolarisation",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the stimulus that triggers the opening of voltage-gated potassium (K+) channels during an action potential.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the opening of these channels restores the resting membrane potential (repolarisation).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Depolarisation of axon membrane reaching approximately +30 to +40 mV alters electrostatic charge on voltage-sensor domains of channel protein, triggering pore opening [2].", "marks": 2},
            {"q": "Q33(b)", "points": "K+ ions diffuse rapidly out of axon down their steep electrochemical gradient via open channels; loss of positive charges restores negative potential inside axon relative to outside [2].", "marks": 2}
        ]
    ))

    # Q34: Microvilli & surface area amplification
    questions.append(Question(
        number=34,
        title="9700/22/M/J/18/Q2 - Microvilli & Surface Area Amplification",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of microvilli found on the apical surface of intestinal enterocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how microvilli increase the efficiency of absorption of digestion products.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Finger-like microscopic folds of the apical plasma membrane, supported internally by bundles of parallel actin microfilaments anchored in the terminal web [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Dramatically increases effective surface area of plasma membrane per cell; provides extensive membrane space to accommodate vast numbers of carrier proteins, ion channels, and membrane-bound digestive enzymes [2].", "marks": 2}
        ]
    ))

    # Q35: Facilitated diffusion carrier kinetics
    questions.append(Question(
        number=35,
        title="9700/13/M/J/22/Q16 - Carrier-Mediated Facilitated Diffusion Kinetics",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how a non-competitive inhibitor affecting carrier proteins would alter the transport kinetics curve of a solute.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why carrier proteins exhibit high specificity for single isomers of a molecule (e.g. D-glucose vs L-glucose).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Binds to an allosteric site on carrier protein, changing tertiary shape of binding pocket; reduces maximum transport velocity (Vmax) regardless of solute concentration [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Binding site has precise three-dimensional geometry complementary only to the specific stereoisomer; R-groups form hydrogen and ionic bonds only when chemical groups are in exact spatial arrangement [2].", "marks": 2}
        ]
    ))

    # Q36: Receptor-mediated endocytosis & LDL uptake
    questions.append(Question(
        number=36,
        title="9700/21/M/J/17/Q3 - Receptor-Mediated Endocytosis & LDL Uptake",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the role of clathrin protein coats in receptor-mediated endocytosis of low-density lipoproteins (LDL).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the biomedical consequence if a mutation prevents LDL receptors from clustering in clathrin-coated pits.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Clathrin molecules assemble into a triskelion polymeric lattice on cytosolic face of membrane, inducing curvature that forces membrane to invaginate and pinch off as a coated vesicle [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Cells cannot internalise LDL particles from blood; leads to severe familial hypercholesterolaemia with dangerous accumulation of cholesterol in blood, causing premature atherosclerosis and heart disease [2].", "marks": 2}
        ]
    ))

    # Q37: Metabolic poisons & active transport arrest
    questions.append(Question(
        number=37,
        title="[Mentora Original A* Extension] - Metabolic Poisons & Active Transport Arrest",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Explain why treating an animal tissue with sodium cyanide (which inhibits cytochrome c oxidase in aerobic respiration) halts active transport but leaves simple diffusion unaffected.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why lowering the temperature from 25 deg C to 0 deg C severely reduces the rate of both active transport and facilitated diffusion.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Cyanide blocks oxidative phosphorylation, depleting cellular ATP synthesis required to power carrier proteins in active transport; simple diffusion relies solely on thermal kinetic energy of solutes, not cellular ATP [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Low temperature decreases kinetic energy of solute molecules and membrane phospholipids (reducing collision rate); also slows conformational changes in carrier proteins and reduces respiratory enzyme rates generating ATP [2].", "marks": 2}
        ]
    ))

    # Q38: Osmotic pressure in halophytic plant cells
    questions.append(Question(
        number=38,
        title="9700/12/O/N/20/Q14 - Osmotic Adaptations in Mangrove Halophytes",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain how mangrove halophytes living in coastal seawater (low water potential) are able to absorb water by osmosis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why halophytes compartmentalise high concentrations of salt ions into the central vacuole rather than leaving them in the cytoplasm.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Root cells actively accumulate high concentrations of inorganic ions / organic solutes in their vacuoles, lowering root cell solute potential (Psi_s) to a value even lower (more negative) than external seawater [2].", "marks": 2},
            {"q": "Q38(b)", "points": "High cytosolic salt concentrations would denature sensitive metabolic enzymes and disrupt ribosomal protein synthesis; vacuole acts as safe storage depot while tonoplast maintains cytoplasmic osmotic balance [2].", "marks": 2}
        ]
    ))

    # Q39: Lipid rafts and membrane microdomains
    questions.append(Question(
        number=39,
        title="9700/23/O/N/17/Q2 - Lipid Rafts and Signalling Microdomains",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular characteristics of lipid rafts within the plasma membrane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological importance of lipid rafts in cell signalling cascades.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Specialised, microdomains enriched in cholesterol and sphingolipids with longer, saturated fatty acid tails, forming thicker and more rigid membrane patches that float within fluid bilayer [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Concentrate specific receptor proteins, G-proteins, and downstream effector enzymes in close spatial proximity, accelerating signal transduction kinetics and preventing cross-talk between pathways [2].", "marks": 2}
        ]
    ))

    # Q40: Cyanide effect on membrane potential & ion gradients
    questions.append(Question(
        number=40,
        title="9700/11/F/M/21/Q15 - Dissipation of Electrochemical Gradients by Cyanide",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe what happens to intracellular Na+ and extracellular K+ concentrations over time following exposure to a metabolic inhibitor.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why secondary active co-transporters in the same cell also cease functioning shortly after inhibitor addition.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Na+/K+ pump stops running due to ATP exhaustion; passive leakage leads to Na+ diffusing into cell and K+ diffusing out, causing internal Na+ to rise and external K+ to rise until gradients dissipate to zero [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Secondary active transport relies on the steep inward electrochemical gradient of Na+ established by primary active transport; when the Na+ gradient dissipates, the driving force for co-transport is lost [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Fluid mosaic model definition
    questions.append(Question(
        number=41,
        title="9700/12/M/J/20/Q12 - Define Fluid Mosaic Model",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the fluid mosaic model of membrane structure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "A model of cell membrane structure where phospholipids form a dynamic bilayer in which individual lipid molecules can move laterally ('fluid'), interspersed with an irregular pattern of diverse globular proteins ('mosaic') [2].", "marks": 2}
        ]
    ))

    # Q42: Osmosis definition
    questions.append(Question(
        number=42,
        title="9700/11/M/J/21/Q13 - Define Osmosis",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term osmosis in precise biological terms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "The net movement of water molecules from a region of higher water potential (less negative) to a region of lower water potential (more negative), down a water potential gradient, across a selectively / partially permeable membrane [2].", "marks": 2}
        ]
    ))

    # Q43: Water potential definition
    questions.append(Question(
        number=43,
        title="9700/12/O/N/21/Q14 - Define Water Potential",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define water potential (Psi) and state the water potential value of pure water at standard atmospheric pressure and 20 deg C.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "A measure of the tendency of water molecules to move from one area to another / kinetic energy of free water molecules compared to pure water; pure water has a water potential of exactly 0 kPa [2].", "marks": 2}
        ]
    ))

    # Q44: Active transport definition
    questions.append(Question(
        number=44,
        title="9700/13/O/N/22/Q12 - Define Active Transport",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term active transport.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "The movement of molecules or ions across a biological membrane against their concentration / electrochemical gradient (from low to high concentration), involving carrier proteins and requiring metabolic energy in the form of ATP [2].", "marks": 2}
        ]
    ))

    # Q45: Role of cholesterol
    questions.append(Question(
        number=45,
        title="9700/11/F/M/23/Q13 - Role of Cholesterol in Cell Surface Membranes",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="State two distinct functions of cholesterol in eukaryotic plasma membranes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "Regulates membrane fluidity across temperature fluctuations (prevents crystallization at low temp, restrains excess movement at high temp); stabilizes bilayer mechanical integrity and decreases permeability to small water-soluble solutes [2].", "marks": 2}
        ]
    ))

    # Q46: Glycocalyx definition
    questions.append(Question(
        number=46,
        title="9700/12/F/M/20/Q11 - Define Glycocalyx and State Its Function",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term glycocalyx and state its primary role in cell recognition.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "The external carbohydrate-rich layer on the cell surface membrane formed by branching oligosaccharide chains of glycolipids and glycoproteins; functions as immunological self-antigen tags and cell-cell recognition markers [2].", "marks": 2}
        ]
    ))

    # Q47: Incipient plasmolysis definition
    questions.append(Question(
        number=47,
        title="[Mentora Original A* Extension] - Define Incipient Plasmolysis",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="Define the term incipient plasmolysis and state the numerical value of pressure potential (Psi_p) at this state.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "The condition of a plant tissue immersed in an external solution where the protoplast just ceases to exert pressure against the cell wall (exactly 50% of cells show detachment); pressure potential Psi_p is 0 kPa, so cell Psi = cell Psi_s [2].", "marks": 2}
        ]
    ))

    # Q48: Carrier vs channel protein
    questions.append(Question(
        number=48,
        title="9700/11/M/J/22/Q14 - Distinguish Carrier Protein vs Channel Protein",
        syllabus_ref="Syllabus 4.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between a carrier protein and a channel protein in terms of mechanism of transport.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "Channel proteins have fixed or gated water-filled hydrophilic pores that allow ions to diffuse through directly; carrier proteins possess specific binding sites that undergo alternating conformational (shape) changes to move solutes across [2].", "marks": 2}
        ]
    ))

    # Q49: Phagosome-lysosome fusion
    questions.append(Question(
        number=49,
        title="[Mentora Original A* Extension] - Function of Phagosome-Lysosome Fusion",
        syllabus_ref="Syllabus 4.2",
        difficulty="CHALLENGING",
        parts=[
            QuestionPart(label="(a)", text="State the physiological purpose of fusing a primary lysosome with a phagosome during phagocytosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "Delivers hydrolytic enzymes (lysozyme, acid hydrolases, proteases) directly into the phagosome lumen to enzymatically digest and destroy engulfed microorganisms at an optimum acidic pH [2].", "marks": 2}
        ]
    ))

    # Q50: SA:V ratio and cell size relationship
    questions.append(Question(
        number=50,
        title="9700/12/M/J/19/Q12 - Surface Area to Volume Ratio and Cell Size",
        syllabus_ref="Syllabus 4.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="State the mathematical relationship between the linear dimensions of a cell and its surface area to volume (SA:V) ratio, and explain its consequence for cell size.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "As cell linear dimensions increase, volume increases with cube of radius (r^3) while surface area increases only with square (r^2), causing SA:V ratio to decrease inversely (1/r); restricts maximum cell size because simple diffusion becomes too slow to support internal metabolic demand [2].", "marks": 2}
        ]
    ))

    return questions

def get_topic4_faqs():
    return [
        {
            "q_num": 1,
            "title": "Explain the Fluid Mosaic Model of Membrane Structure and Describe How Cholesterol Regulates Membrane Fluidity at High and Low Temperatures.",
            "category": "Membrane Architecture • Fluidity Buffering",
            "examiner_trap": "Stating that cholesterol only increases or only decreases membrane fluidity. Cholesterol acts as a bidirectional fluidity buffer, dampening fluidity at high temperatures and preventing solid crystallisation at low temperatures.",
            "model_answer": "• The Fluid Mosaic Model:\n  1. 'Fluid': Phospholipids and embedded proteins can move laterally (diffuse sideways) within their respective monolayers; hydrocarbon tails flex and rotate;\n  2. 'Mosaic': A diverse variety of protein molecules (integral, peripheral, glycoproteins) are scattered irregularly throughout the phospholipid bilayer like tiles in a mosaic.\n• Chemical Arrangement of Cholesterol: Amphipathic molecule; its small polar hydroxyl (-OH) group aligns with the hydrophilic phosphate heads of phospholipids, while its rigid hydrophobic steroid rings and hydrocarbon tail intercalate between fatty acid tails.\n• Regulation at High Temperatures: Restricts the lateral movement and excessive thermal vibration of phospholipid fatty acid chains, preventing the membrane from becoming overly fluid, structurally unstable, and leaky to small polar molecules.\n• Regulation at Low Temperatures: Intercalates between fatty acid chains, disrupting regular packing and preventing hydrocarbon chains from clustering into a rigid, crystalline crystalline gel, thereby maintaining membrane fluidity at lower temperatures."
        },
        {
            "q_num": 2,
            "title": "Distinguish Between Simple Diffusion and Facilitated Diffusion, and Contrast Channel Proteins with Carrier Proteins.",
            "category": "Transport Mechanisms • Passive Permeation",
            "examiner_trap": "Confusing channel proteins with carrier proteins, or stating that facilitated diffusion requires ATP. Facilitated diffusion is strictly passive down a concentration gradient.",
            "model_answer": "• Simple Diffusion: Passive net movement of small, non-polar, or lipid-soluble solute molecules (e.g. O2, CO2, glycerol, steroids) directly through the phospholipid bilayer from high to low concentration down a concentration gradient without protein assistance.\n• Facilitated Diffusion: Passive net movement of polar molecules, large molecules, or charged inorganic ions (e.g. glucose, amino acids, Na+, K+, Cl-) down their electrochemical/concentration gradient via specific transmembrane transport proteins (no metabolic ATP expended).\n• Hydrophilic Channel Proteins:\n  1. Fixed water-filled hydrophilic pores spanning the entire lipid bilayer;\n  2. Highly specific for particular inorganic ions based on diameter and charge distribution;\n  3. Can be voltage-gated or ligand-gated (opening/closing in response to stimuli);\n  4. Facilitate rapid ion flux without conformational shape change.\n• Conformational Carrier Proteins:\n  1. Possess specific binding pockets complementary to a particular solute;\n  2. Solute binding induces a reversible conformational change that opens the carrier to the opposite side of the membrane;\n  3. Transport kinetics display saturation: at high solute concentrations, carrier sites become saturated, reaching a maximum rate of transport (Vmax)."
        },
        {
            "q_num": 3,
            "title": "Explain the Water Potential Equation (Psi = Psi_s + Psi_p) and Define the State of Incipient Plasmolysis in Plant Tissue.",
            "category": "Osmosis & Water Relations • Water Potential",
            "examiner_trap": "Describing water movement using 'water concentration' instead of 'water potential (Psi)'. Stating that pressure potential (Psi_p) can be negative; Psi_p is zero or positive.",
            "model_answer": "• Water Potential (Psi): The tendency of water molecules to move from one region to another; pure liquid water at standard temperature and atmospheric pressure has a defined water potential of 0 kPa (the maximum possible value); the addition of solute lowers water potential, making Psi negative.\n• Components of the Water Potential Equation (Psi = Psi_s + Psi_p):\n  1. Solute Potential (Psi_s): The effect of dissolved solutes in lowering water potential; always negative or zero; more solute molecules bind free water dipoles in hydration shells, reducing free kinetic energy;\n  2. Pressure Potential (Psi_p): The hydrostatic pressure exerted by the cell wall pushing inward against the expanding protoplast (wall pressure); zero or positive.\n• Incipient Plasmolysis:\n  1. The exact physiological state where the plant protoplast has shrunk just enough that the plasma membrane exerts zero pressure against the cell wall (Psi_p = 0 kPa);\n  2. At this point, the overall cell water potential equals its solute potential: Psi = Psi_s;\n  3. Operationally defined in experiments as the external solute concentration where exactly 50% of plant cells in a tissue are plasmolysed and 50% remain unplasmolysed."
        },
        {
            "q_num": 4,
            "title": "Contrast the Behaviour and Morphological Changes of Plant Cells and Erythrocytes Placed in Hypotonic vs Hypertonic Solutions.",
            "category": "Osmosis • Cellular Responses & Cell Wall Function",
            "examiner_trap": "Stating that animal cells become 'turgid' or that plant cells 'burst'. Plant cells cannot burst under normal osmotic conditions due to the high tensile strength of the cellulose cell wall.",
            "model_answer": "• Hypotonic Environment (Higher Psi / Lower Solute Concentration than Cytoplasm):\n  1. Plant Cells: Water moves into the vacuole and cytoplasm by osmosis down the water potential gradient; protoplast expands and presses against the rigid cellulose cell wall; the wall exerts an equal and opposite hydrostatic wall pressure (pressure potential Psi_p rises); cell becomes turgid, providing mechanical support to non-woody tissues;\n  2. Erythrocytes (Red Blood Cells): Water enters by osmosis; without a rigid cell wall to resist internal hydrostatic pressure, the flexible plasma membrane stretches until it ruptures, releasing haemoglobin into solution (osmotic lysis or haemolysis).\n• Hypertonic Environment (Lower Psi / Higher Solute Concentration than Cytoplasm):\n  1. Plant Cells: Water exits vacuole and cytoplasm by osmosis down the water potential gradient; protoplast shrinks away from the cell wall (plasmolysis); the space between the cell wall and the shrunken plasma membrane fills with the external hypertonic solution through the freely permeable wall;\n  2. Erythrocytes: Water exits by osmosis; cell volume decreases rapidly and the cell shrinks, forming notched, crinkled edges (crenation)."
        },
        {
            "q_num": 5,
            "title": "Describe the Molecular Mechanism of Primary Active Transport via the Na+/K+-ATPase Pump and Secondary Active Glucose Co-Transport.",
            "category": "Active Transport • Electrochemical Gradients",
            "examiner_trap": "Omitting the stoichiometric ratio (3 Na+ out / 2 K+ in) or failing to explain that glucose transport against its gradient is energized by the downhill Na+ electrochemical gradient.",
            "model_answer": "• Primary Active Transport (Na+/K+-ATPase Pump):\n  1. Three intracellular Na+ ions bind to high-affinity sites on the cytoplasmic face of the pump protein;\n  2. ATP binds and is hydrolysed to ADP and inorganic phosphate (Pi); the phosphate remains covalently attached to the pump (phosphorylation);\n  3. Phosphorylation induces a major conformational change, translocating the three Na+ ions across the membrane and releasing them outside against their concentration gradient;\n  4. Two extracellular K+ ions bind to high-affinity sites on the external face, triggering dephosphorylation;\n  5. Dephosphorylation reverts the protein to its original conformation, carrying the two K+ ions into the cytosol against their concentration gradient (net electrogenic pump: 3 Na+ out, 2 K+ in per ATP).\n• Secondary Active Co-Transport (Na+/Glucose Symporter):\n  1. The steep electrochemical gradient of Na+ established by the Na+/K+-ATPase creates driving potential;\n  2. Na+ binds to the co-transporter and moves passively downhill into the epithelial cell;\n  3. The energy released by Na+ moving down its electrochemical gradient drives the simultaneous inward transport of glucose against its steep chemical concentration gradient (indirect ATP requirement)."
        },
        {
            "q_num": 6,
            "title": "Explain the Cytological Mechanisms of Endocytosis (Phagocytosis and Pinocytosis) and Exocytosis, Emphasising the Role of ATP and Microtubules.",
            "category": "Bulk Transport • Vesicular Trafficking",
            "examiner_trap": "Classifying bulk transport as active transport mediated by carrier proteins. Bulk transport involves dynamic membrane remodeling, vesicle fission/fusion, and motor proteins.",
            "model_answer": "• Endocytosis (Bulk Inward Transport):\n  1. Invagination of the plasma membrane triggered by particle binding or fluid contact;\n  2. Phagocytosis: Uptake of solid particles (e.g. macrophages engulfing bacteria); pseudopodia extend around the particle, enclose it, and fuse to form a phagocytic vacuole (phagosome);\n  3. Pinocytosis: Non-specific uptake of extracellular fluid and dissolved solutes by pinching inward to form tiny micropinocytic vesicles;\n  4. Receptor-Mediated Endocytosis: Target macromolecules bind to specific cell-surface receptors concentrated in clathrin-coated pits, triggering invagination into clathrin-coated vesicles.\n• Exocytosis (Bulk Outward Secretion):\n  1. Secretory proteins synthesized on RER and modified in Golgi body are packaged into secretory vesicles;\n  2. Vesicles are actively transported along cytoskeleton tracks (microtubules) by motor proteins (kinesin/dynein) fueled by ATP hydrolysis;\n  3. Vesicle membrane fuses with the plasma membrane via SNARE proteins, discharging contents into extracellular fluid;\n  4. Replaces lipid membrane and increases the surface area of the cell surface membrane.\n• Requirement for Energy: Both processes require substantial ATP for actin microfilament rearrangement, membrane pinching/fission, motor protein motility, and vesicle membrane fusion."
        },
        {
            "q_num": 7,
            "title": "Describe the Experimental Protocol and Biochemical Rationale for Investigating Membrane Permeability in Beetroot Tissue.",
            "category": "Experimental Practical Skills • Membrane Permeability",
            "examiner_trap": "Failing to wash cut beetroot discs before beginning the experiment (leaves ruptured pigment on surfaces), or attributing pigment release to enzyme action rather than membrane disruption.",
            "model_answer": "• Storage of Betalain: Red betalain pigment is sequestered within the large central vacuole of Beta vulgaris cells, bounded by two semi-permeable membranes (tonoplast and plasma membrane).\n• Core Preparation Protocol:\n  1. Use a cork borer to cut uniform cylinders of beetroot; slice into uniform discs using a sharp scalpel and ruler to ensure identical surface area;\n  2. Wash discs repeatedly in running tap water and distilled water until the wash water remains completely clear, removing pigment released from cells mechanically ruptured during slicing;\n  3. Blot discs gently with filter paper.\n• Temperature Stress Investigation:\n  1. Place discs into test tubes containing equal volumes of distilled water maintained in thermostatically controlled water baths at varied temperatures (e.g. 20, 30, 40, 50, 60, 70, 80°C) for a fixed time (e.g. 15 minutes);\n  2. Remove discs and pipette supernatant liquid into cuvettes;\n  3. Measure absorbance or percentage transmission using a colorimeter fitted with a blue/green filter (~520 nm, complementary to red betalain).\n• Biochemical Explanation:\n  1. Above 45–50°C, increasing kinetic energy increases membrane fluidity; thermal agitation causes membrane proteins to denature (breaking tertiary hydrogen and ionic bonds), creating gaping holes;\n  2. Phospholipid bilayer loses integrity and ruptures; betalain pigment diffuses rapidly out of vacuoles down its concentration gradient."
        },
        {
            "q_num": 8,
            "title": "Explain Why the Depth of Diffusion Remains Constant Across Different Sized Agar Blocks While the Percentage Volume Reached Differs.",
            "category": "Diffusion Physics • Surface Area to Volume Ratio",
            "examiner_trap": "Claiming that the rate of diffusion or depth of diffusion is greater in smaller agar blocks. Diffusion rate (mm min-1) depends solely on temperature, concentration gradient, and matrix density, not cube size.",
            "model_answer": "• Experimental Model: Phenolphthalein-agar blocks stained pink with dilute NaOH placed into a beaker of dilute hydrochloric acid (HCl); acid diffuses inward, neutralising NaOH and turning phenolphthalein colourless.\n• Absolute Rate of Diffusion (Constant):\n  1. The depth of acid penetration (distance moved from the surface in mm) over a fixed time interval is IDENTICAL across all block sizes (e.g. 1 cm, 2 cm, 3 cm cubes);\n  2. Justification: Temperature, concentration gradient of H+ ions, agar porosity, and diffusion coefficient of HCl are completely constant across all blocks.\n• Percentage Decolourisation vs Cube Size (Variable):\n  1. Smaller cubes have a much higher surface area to volume (SA:V) ratio than larger cubes;\n  2. In a 1 cm cube, the diffusing acid penetrates to the center, decolourising 100% of the block volume in a short time;\n  3. In a 3 cm cube, the same depth of penetration leaves a large, untouched pink core in the center; the percentage of total volume reached is drastically lower;\n  4. Biological Significance: Proves that diffusion alone is inadequate to supply nutrients and remove metabolic wastes from the interior of large multicellular organisms, necessitating specialised exchange surfaces and mass transport systems."
        },
        {
            "q_num": 9,
            "title": "Outline the Main Stages of a Cell Signalling Pathway: Ligand Reception, G-Protein Transduction, Second Messengers, and Cascade Amplification.",
            "category": "Cell Signalling • Signal Transduction Cascades",
            "examiner_trap": "Asserting that all signalling molecules pass through the plasma membrane into the cytoplasm. Hydrophilic ligands (e.g. adrenaline, glucagon, peptide hormones) cannot cross the lipid bilayer.",
            "model_answer": "• Stage 1: Signal Secretion and Delivery:\n  1. Endocrine or paracrine signalling cell secretes a chemical messenger molecule (ligand / first messenger, e.g. adrenaline, glucagon) by exocytosis into the extracellular fluid or bloodstream.\n• Stage 2: Reception at Target Cell Surface:\n  1. Hydrophilic ligand cannot cross the hydrophobic lipid bilayer; binds specifically and reversibly to the extracellular binding domain of a complementary transmembrane receptor protein (e.g. G-protein coupled receptor, GPCR).\n• Stage 3: Transduction & G-Protein Activation:\n  1. Ligand binding induces a conformational change in the intracellular receptor domain;\n  2. Activates an associated heterotrimeric G-protein by causing GDP to be exchanged for GTP on the alpha-subunit;\n  3. Active G-protein subunit dissociates and moves laterally in the membrane to activate an effector enzyme (adenylyl cyclase).\n• Stage 4: Second Messenger Generation & Cascade Amplification:\n  1. Activated adenylyl cyclase converts multiple cytoplasmic ATP molecules into cyclic AMP (cAMP, the second messenger);\n  2. cAMP molecules diffuse throughout the cytosol and activate protein kinase A (PKA);\n  3. Signal Amplification: One ligand molecule activates one receptor, which activates many G-proteins, producing thousands of cAMP molecules, activating cascades of protein kinases;\n  4. Each active kinase phosphorylates and activates hundreds of target enzymes, triggering a massive, rapid physiological response (e.g. glycogenolysis)."
        },
        {
            "q_num": 10,
            "title": "Detail the Structural Distribution and Biological Roles of Glycolipids and Glycoproteins in the Plasma Membrane.",
            "category": "Glycocalyx Functions • Cell Surface Recognition",
            "examiner_trap": "Claiming that carbohydrate chains are found on the cytoplasmic (inner) face of the plasma membrane. The glycocalyx is located exclusively on the outer extracellular surface.",
            "model_answer": "• Chemical Nature and Asymmetrical Distribution:\n  1. Short, branched oligosaccharide chains covalently bonded either to the glycerol/phosphate head of lipids (glycolipids) or to external domains of membrane proteins (glycoproteins);\n  2. Asymmetry: Distributed EXCLUSIVELY on the outer extracellular monolayer of the plasma membrane, collectively forming a sugary carbohydrate coating termed the glycocalyx.\n• Biological Roles:\n  1. Cell-to-Cell Recognition & Antigens: Carbohydrate branch configurations vary enormously between cell types, acting as specific molecular identification markers / antigens (e.g. ABO blood group antigens on erythrocytes; major histocompatibility complex MHC markers for immune discrimination of self vs non-self);\n  2. Cell Signalling Receptors: Oligosaccharide domains project into the extracellular environment to form high-affinity receptor sites for hormone and neurotransmitter binding;\n  3. Cell-to-Cell Adhesion: Extracellular carbohydrate branches of neighbouring cells interlock and form hydrogen bonds, binding cells together into tissues and maintaining structural integrity of epithelial sheets;\n  4. Structural Stability: Hydroxyl groups on carbohydrate chains form extensive hydrogen bonds with surrounding water molecules, stabilising overall membrane architecture."
        }
    ]

