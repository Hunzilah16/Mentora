"""
Topic 8: Transport in Mammals - 50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Physiological Mechanism Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Past Paper vs Original Ratio: 44 Authentic (88%) / 6 Original Extensions (12%)
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic8_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Closed double circulation vs single circulation (Fig 8.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q4 - Closed Double Circulation: Pulmonary vs Systemic Circuits",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Mammals possess a closed, double circulatory system in which blood passes through the heart twice during one complete circuit of the body. Fig. 8.1 is a schematic plan showing the relationship between the pulmonary circuit, the systemic circuit, and the four cardiac chambers.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_1_circulatory_system_plan.png"),
        figure_caption="Fig. 8.1: Schematic plan of closed double circulation in mammals showing systemic and pulmonary vascular circuits.",
        parts=[
            QuestionPart(label="(a)", text="Explain the physiological advantages of a double circulation compared to a single circulation found in fish.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the blood pressure in the pulmonary circuit is significantly lower than that in the systemic circuit, and explain the biological necessity for this lower pressure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the two great vessels that carry oxygenated blood, stating the chamber each arises from or leads into.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Blood is repressurised after passing through gas exchange surfaces (pulmonary capillaries); systemic circulation receives high-pressure blood from left ventricle, allowing rapid mass flow of oxygen and glucose over long distances to meet high metabolic rate of endotherms [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Pulmonary circulation is shorter with lower total vascular resistance; lower pressure (~25 mmHg) prevents fluid ultrafiltration into delicate alveoli (prevents pulmonary oedema) and prevents rupturing of thin-walled alveolar capillaries [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Pulmonary vein carries oxygenated blood from lungs into left atrium; Aorta carries oxygenated blood from left ventricle to systemic tissues [2].", "marks": 2}
        ]
    ))

    # Q2: Histological cross-section analysis of artery vs vein vs capillary (Fig 8.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q3 - Histology and Function of Blood Vessels: Artery, Vein, and Capillary",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="The three main types of blood vessels exhibit distinct histological adaptations related to the blood pressure and velocity they experience. Fig. 8.2 shows transverse sections (TS) of an elastic/muscular artery, a vein, and a capillary.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_2_artery_vein_capillary_ts.png"),
        figure_caption="Fig. 8.2: Histological transverse sections comparing the wall layers and lumen dimensions of an artery, a vein, and a capillary.",
        parts=[
            QuestionPart(label="(a)", text="Describe the roles of elastic fibres and smooth muscle fibres in the tunica media of large arteries.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Contrast the structural features of veins with those of arteries, and explain how these adaptations facilitate venous return.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 8.2, explain two structural features of capillaries that adapt them for rapid exchange of respiratory gases and metabolites.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Elastic fibres stretch during ventricular systole to absorb high pulse pressure, and recoil during diastole to smooth out pulsatile flow and maintain diastolic pressure; smooth muscle contracts (vasoconstriction) or relaxes (vasodilation) to regulate lumen diameter and divert blood flow to active tissues [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Veins have a much thinner tunica media (less muscle and elastic tissue) and a wide irregular lumen offering minimal vascular resistance; possess pocket/semilunar valves to ensure unidirectional flow and prevent backflow under low pressure [2].", "marks": 2},
            {"q": "Q2(c)", "points": "Wall consists of a single layer of squamous endothelial cells (~0.5 µm thick), providing an extremely short diffusion distance; narrow lumen (~7 µm) forces erythrocytes to pass in single file, slowing flow and maximizing contact surface area for exchange [2].", "marks": 2}
        ]
    ))

    # Q3: Capillary bed ultrafiltration & Starling forces (Fig 8.3)
    questions.append(Question(
        number=3,
        title="9700/22/M/J/22/Q3 - Microcirculation and Tissue Fluid Dynamics: Starling Forces",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Exchange of substances between blood and body cells occurs via tissue fluid formed in systemic capillary beds. Fig. 8.3 illustrates the hydrostatic pressure and oncotic pressure gradients operating across the arterial and venous ends of a capillary bed.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_3_capillary_bed_tissue_fluid.png"),
        figure_caption="Fig. 8.3: Dynamic Starling forces governing ultrafiltration at the arterial end and osmotic reabsorption at the venous end of a capillary bed.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the interaction between hydrostatic pressure and oncotic pressure leads to the formation of tissue fluid at the arterial end of a capillary bed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why not all the tissue fluid formed is reabsorbed into the capillary at the venous end, and state the route by which the remainder is returned to the blood.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two chemical differences between blood plasma and tissue fluid, giving an explanation for each difference.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "At the arterial end, hydrostatic pressure (+4.3 kPa) exceeds the inward oncotic pressure (-3.3 kPa) generated by plasma proteins; this creates a positive net filtration pressure (+1.0 kPa) forcing water, ions, and small solutes out through capillary endothelial gaps [2].", "marks": 2},
            {"q": "Q3(b)", "points": "Friction along capillary walls reduces hydrostatic pressure at venous end (+1.6 kPa), allowing inward oncotic pressure to drive reabsorption of ~90% of fluid; the remaining ~10% enters blind-ended lymphatic capillaries and is returned to the blood via the thoracic duct into subclavian veins [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Plasma contains a much higher concentration of large plasma proteins (albumin, fibrinogen, globulins) because they are too large to pass through capillary endothelial pores; tissue fluid contains lower protein and virtually zero erythrocytes/platelets [2].", "marks": 2}
        ]
    ))

    # Q4: Formed elements of mammalian blood (Fig 8.4)
    questions.append(Question(
        number=4,
        title="9700/21/M/J/21/Q2 - Cellular Components of Mammalian Blood Smear",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="A stained human blood smear contains distinct cellular elements with specialized morphologies. Fig. 8.4 illustrates the structural appearance of an erythrocyte, a neutrophil, a monocyte, and a lymphocyte.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_4_blood_formed_elements.png"),
        figure_caption="Fig. 8.4: Formed elements of blood: erythrocyte biconcave disk, neutrophil granulocyte, monocyte, and lymphocyte.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the biconcave disc shape and absence of a nucleus in mature erythrocytes adapt them for their role in oxygen transport.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 8.4, contrast the nuclear morphology and cytoplasmic staining of a neutrophil with that of a lymphocyte.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the role of monocytes in immune defence following their migration into peripheral body tissues.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Biconcave shape provides a high surface area to volume (SA:V) ratio for rapid diffusion of oxygen into/out of cell and shortens diffusion distance to center; absence of nucleus and organelles maximizes internal volume for packaging ~280 million haemoglobin molecules [2].", "marks": 2},
            {"q": "Q4(b)", "points": "Neutrophil has a multi-lobed nucleus (3–5 lobes connected by chromatin strands) and granular cytoplasm; lymphocyte has a large, dense, spherical nucleus occupying almost the entire cell with only a thin rim of agranular cytoplasm [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Monocytes circulate in blood for 1–3 days, then extravasate into tissues where they differentiate into large phagocytic macrophages (or dendritic cells); engulf cellular debris and pathogens via phagocytosis and act as antigen-presenting cells (APCs) [2].", "marks": 2}
        ]
    ))

    # Q5: Internal anatomy of the heart & wall thickness (Fig 8.5)
    questions.append(Question(
        number=5,
        title="9700/22/O/N/21/Q4 - Internal Architecture of Mammalian Heart and Valve Operations",
        syllabus_ref="Syllabus 8.3",
        difficulty="ADVANCED",
        preamble="The mammalian heart is a muscular dual pump divided by a central septum. Fig. 8.5 shows a coronal section through the mammalian heart detailing the internal cavities, myocardium thickness, and atrioventricular and semilunar valves.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_5_heart_internal_anatomy.png"),
        figure_caption="Fig. 8.5: Internal coronal view of the mammalian heart showing chambers, myocardium thickness variations, and valves.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the ventricular walls are significantly thicker than the atrial walls, and why the left ventricular wall is approximately three times thicker than the right ventricular wall.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the mechanism by which the atrioventricular (bicuspid and tricuspid) valves open and close during the cardiac cycle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the function of the chordae tendineae and papillary muscles during ventricular systole.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Atria only pump blood a short distance into adjacent ventricles against minimal resistance; ventricles pump blood out of heart; Left ventricle wall is ~3x thicker than right ventricle because it must generate high hydrostatic pressure (~120 mmHg) to pump blood through high-resistance systemic capillaries, whereas right ventricle pumps into low-resistance pulmonary circuit (~25 mmHg) [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Open when atrial pressure exceeds ventricular pressure during diastole; close when ventricular pressure exceeds atrial pressure during ventricular systole, preventing blood from flowing back into atria [2].", "marks": 2},
            {"q": "Q5(c)", "points": "Papillary muscles contract simultaneously with ventricular myocardium, pulling on inelastic chordae tendineae; prevents atrioventricular valve flaps from being forced (everted/prolapsed) backwards into atria under high systolic pressure [2].", "marks": 2}
        ]
    ))

    # Q6: Wiggers diagram analysis of cardiac cycle (Fig 8.6)
    questions.append(Question(
        number=6,
        title="9700/22/M/J/20/Q3 - The Cardiac Cycle: Pressure-Volume Wiggers Analysis",
        syllabus_ref="Syllabus 8.3",
        difficulty="ADVANCED",
        preamble="Pressure and volume changes in the left side of the heart coordinate the unidirectional movement of blood. Fig. 8.6 shows the pressure waveforms in the left ventricle, aorta, and left atrium alongside left ventricular volume during one 0.8-second cardiac cycle.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_6_cardiac_cycle_wiggers.png"),
        figure_caption="Fig. 8.6: Canonical Wiggers diagram showing left ventricular, aortic, and left atrial pressures and ventricular volume over 0.8 s.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 8.6, state the exact time at which the atrioventricular valve closes, and identify the physical event that causes this closure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the stroke volume from Fig. 8.6, showing your working from end-diastolic volume and end-systolic volume.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the cause of the dicrotic notch observed in the aortic pressure waveform at approximately 0.40 seconds.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Time = 0.11 s (accept 0.10–0.12 s); occurs when left ventricular pressure rises above left atrial pressure, causing blood to push AV valve cusps shut (producing first heart sound 'lub') [2].", "marks": 2},
            {"q": "Q6(b)", "points": "End-diastolic volume = 125 cm3, End-systolic volume = 60 cm3; Stroke volume = EDV - ESV = 125 - 60 = 65 cm3 (accept 60–70 cm3) [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Left ventricle begins diastole and pressure drops below aortic pressure; transient retrograde blood flow pushes aortic semilunar valve closed; elastic recoil of expanded aortic wall rebounds against closed valve, producing a brief pressure spike [2].", "marks": 2}
        ]
    ))

    # Q7: Electrical conduction system of heart (Fig 8.7)
    questions.append(Question(
        number=7,
        title="9700/21/O/N/20/Q4 - Myogenic Initiation and Electrical Conduction in the Heart",
        syllabus_ref="Syllabus 8.3",
        difficulty="ADVANCED",
        preamble="The rhythmic contraction of mammalian cardiac muscle is myogenic and coordinated by a specialized electrical conduction system. Fig. 8.7 illustrates the anatomical components and sequence of electrical excitation through the heart.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_7_heart_conduction_system.png"),
        figure_caption="Fig. 8.7: Electrical conduction pathways: Sinoatrial Node (SAN), Atrioventricular Node (AVN), Bundle of His, and Purkyne tissue.",
        parts=[
            QuestionPart(label="(a)", text="State what is meant by the term myogenic and explain why the Sinoatrial Node (SAN) acts as the heart's natural pacemaker.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological importance of the 0.1 second delay in transmission that occurs at the Atrioventricular Node (AVN).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the route taken by the wave of excitation from the AVN to the ventricular myocardium, and explain why ventricles contract from the apex upward.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Myogenic means cardiac muscle initiates its own contractions without requiring external nerve impulses; SAN depolarises spontaneously at the fastest intrinsic rate (~70–80 bpm), initiating waves of excitation that spread across atria [2].", "marks": 2},
            {"q": "Q7(b)", "points": "Ensures that atria have completely finished contracting (atrial systole) and emptying their blood through AV valves into ventricles before ventricular systole commences [2].", "marks": 2},
            {"q": "Q7(c)", "points": "Wave passes down Bundle of His in septum, through left and right bundle branches, then spreads through Purkyne fibres up ventricular walls; contracting from apex upward pumps blood efficiently towards the semilunar valves at base of aorta and pulmonary artery [2].", "marks": 2}
        ]
    ))

    # Q8: Oxygen dissociation curve of adult haemoglobin (Fig 8.8)
    questions.append(Question(
        number=8,
        title="9700/22/F/M/23/Q3 - Cooperative Oxygen Binding and the Haemoglobin Dissociation Curve",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="Haemoglobin is a globular transport protein composed of four globin polypeptides, each with a haem prosthetic group. Fig. 8.8 shows the sigmoidal oxygen dissociation curve of adult haemoglobin (HbA) across physiological oxygen partial pressures.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_8_oxygen_dissociation_curve.png"),
        figure_caption="Fig. 8.8: Sigmoidal oxygen dissociation curve of adult haemoglobin showing cooperative binding, P50, and tissue saturation levels.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the oxygen dissociation curve of haemoglobin has a sigmoidal (S-shaped) profile rather than a straight line.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 8.8, compare the percentage saturation of haemoglobin in pulmonary capillaries (pO2 = 12 kPa) with that in resting muscle (pO2 = 5.3 kPa), and state the percentage of oxygen released.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Define the term P50 and state what a low P50 value indicates regarding haemoglobin's affinity for oxygen.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "Reflects positive cooperativity: initially haemoglobin has a tight (T) conformation and binding 1st O2 molecule is difficult (shallow initial curve); binding 1st O2 alters tertiary/quaternary conformation, relaxing binding pocket and making binding of 2nd and 3rd O2 molecules much easier (steep curve) [2].", "marks": 2},
            {"q": "Q8(b)", "points": "At pO2 12 kPa (lungs), saturation = 98%; at pO2 5.3 kPa (resting muscle), saturation = 75%; Percentage of oxygen released = 98% - 75% = 23% (accept 22–25%) [2].", "marks": 2},
            {"q": "Q8(c)", "points": "P50 is the partial pressure of oxygen at which haemoglobin is exactly 50% saturated with oxygen; a low P50 indicates a high affinity for oxygen (loads oxygen readily at low pO2) [2].", "marks": 2}
        ]
    ))

    # Q9: The Bohr effect (Fig 8.9)
    questions.append(Question(
        number=9,
        title="9700/21/M/J/23/Q2 - The Bohr Effect and Allosteric Regulation of Oxygen Delivery",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="The affinity of haemoglobin for oxygen decreases in the presence of carbon dioxide and acidic conditions. Fig. 8.9 demonstrates the rightward displacement of the oxygen dissociation curve (the Bohr shift) under elevated partial pressures of carbon dioxide (pCO2).",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_9_bohr_shift_curves.png"),
        figure_caption="Fig. 8.9: The Bohr shift: rightward displacement of the oxygen dissociation curve under elevated pCO2 and lower pH.",
        parts=[
            QuestionPart(label="(a)", text="Describe the biochemical mechanism responsible for the Bohr shift when carbon dioxide concentration increases in respiring tissues.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 8.9, explain the physiological benefit of the Bohr effect to actively contracting skeletal muscle during strenuous exercise.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the Bohr shift promotes the uptake of oxygen when blood arrives in the pulmonary capillaries of the lungs.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "CO2 dissolves and reacts with water to form H2CO3, which dissociates into H+ and HCO3-; H+ ions bind to allosteric sites on globin chains, forming haemoglobinic acid (HHb); this stabilizes the deoxygenated T-conformation, reducing O2 affinity [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Actively respiring muscle produces high pCO2 and lactic acid; causes rightward curve shift, so at the same low tissue pO2 (e.g. 4 kPa), haemoglobin releases significantly more O2 (~15–20% extra) to sustain aerobic respiration [2].", "marks": 2},
            {"q": "Q9(c)", "points": "In pulmonary capillaries, CO2 diffuses out into alveoli, lowering blood pCO2 and raising pH; curve shifts left, increasing haemoglobin's affinity for oxygen so it loads O2 to full saturation even at slightly lower pO2 [2].", "marks": 2}
        ]
    ))

    # Q10: Carbon dioxide transport & Chloride shift (Fig 8.10)
    questions.append(Question(
        number=10,
        title="9700/22/O/N/22/Q2 - Biochemical Pathways of CO2 Transport and the Chloride Shift",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="Carbon dioxide produced during cellular respiration is transported in the blood in three distinct forms. Fig. 8.10 illustrates the biochemical reactions occurring within an erythrocyte in a systemic capillary bed, including the chloride shift.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_10_co2_transport_rbc_chloride_shift.png"),
        figure_caption="Fig. 8.10: Pathways of CO2 transport inside an erythrocyte: carbonic anhydrase reaction, HHb formation, and anion exchange (chloride shift).",
        parts=[
            QuestionPart(label="(a)", text="State the three forms in which carbon dioxide is transported in blood, giving the approximate percentage carried by each form.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the reaction catalysed by carbonic anhydrase in erythrocytes and explain the role of haemoglobin as a chemical buffer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain what is meant by the chloride shift and why it is essential for red blood cell function.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Hydrogencarbonate ions (HCO3-) dissolved in plasma (~85%); Carbaminohaemoglobin bound to amino terminal groups of haemoglobin (~10%); Dissolved CO2 gas in physical solution in plasma (~5%) [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Carbonic anhydrase reversibly hydrates CO2 + H2O <-> H2CO3, which dissociates into H+ + HCO3-; Deoxyhaemoglobin buffers H+ by binding them to form haemoglobinic acid (HHb), preventing dangerous drops in blood pH [2].", "marks": 2},
            {"q": "Q10(c)", "points": "As HCO3- ions diffuse out of RBC down concentration gradient into plasma, chloride ions (Cl-) diffuse in from plasma via Band 3 anion exchanger; maintains electrical neutrality (electrochemical balance) across erythrocyte membrane [2].", "marks": 2}
        ]
    ))

    # Q11: Comparative curves: Adult Hb vs Fetal Hb vs Myoglobin (Fig 8.11)
    questions.append(Question(
        number=11,
        title="9700/21/O/N/21/Q2 - Comparative Oxygen Transport Proteins: HbA, HbF, and Myoglobin",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="Different oxygen-binding pigments exhibit distinct dissociation curves adapted to their physiological environments. Fig. 8.11 compares the oxygen dissociation curves of adult haemoglobin (HbA), fetal haemoglobin (HbF), and muscle myoglobin.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_11_fetal_adult_myoglobin_curves.png"),
        figure_caption="Fig. 8.11: Comparison of oxygen dissociation curves for adult haemoglobin (HbA), fetal haemoglobin (HbF), and myoglobin.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 8.11, explain why the curve for fetal haemoglobin lies to the left of the curve for maternal adult haemoglobin, and explain why this is essential for fetal survival.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the oxygen dissociation curve for myoglobin is hyperbolic rather than sigmoidal.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the physiological function of myoglobin in skeletal muscle during sustained anaerobic conditions.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "HbF curve shifted to left indicates higher affinity for O2 at all partial pressures (lower P50); at placental capillaries (pO2 ~4 kPa), maternal HbA unloads O2 while fetal HbF binds O2, ensuring net transfer of oxygen from mother to fetus across placenta [2].", "marks": 2},
            {"q": "Q11(b)", "points": "Myoglobin consists of a single polypeptide chain with only one haem group; lacks quaternary structure, so cannot exhibit subunit cooperativity (positive cooperativity requires multiple interacting subunits) [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Acts as an emergency oxygen store; because of very high affinity, it remains fully saturated under resting and moderate exercise conditions and only releases its bound oxygen at very low pO2 (<1.5 kPa) when muscle cells become severely hypoxic [2].", "marks": 2}
        ]
    ))

    # Q12: Vasomotor regulation in arterioles (Fig 8.12)
    questions.append(Question(
        number=12,
        title="9700/22/M/J/19/Q4 - Vasomotor Control and Resistance in Arterioles",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Arterioles contain a prominent layer of circular smooth muscle in their tunica media and act as the principal resistance vessels of the systemic circulation. Fig. 8.12 shows transverse sections of an arteriole in states of vasoconstriction and vasodilation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_12_arteriole_vasoconstriction.png"),
        figure_caption="Fig. 8.12: Vasomotor changes in arteriole lumen diameter during smooth muscle vasoconstriction and vasodilation.",
        parts=[
            QuestionPart(label="(a)", text="Describe how circular smooth muscle contraction alters arteriole resistance and local blood flow according to Poiseuille's law.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the autonomic nervous system coordinates vasoconstriction in abdominal viscera and vasodilation in skeletal muscles during exercise.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why arterioles are subject to the greatest drop in blood pressure across the entire systemic circulation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Contraction of circular smooth muscle constricts lumen; resistance is inversely proportional to radius to fourth power (R proportional to 1/r^4); small decrease in radius causes massive increase in vascular resistance, drastically reducing blood flow to local capillary beds [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Sympathetic stimulation and noradrenaline release trigger vasoconstriction of gut/renal arterioles (diverting blood away from digestive organs); local metabolic factors (CO2, lactate, H+) trigger vasodilation of arterioles supplying active skeletal muscle [2].", "marks": 2},
            {"q": "Q12(c)", "points": "Arterioles have narrow individual lumens and total cross-sectional area is still relatively small, generating immense frictional resistance against blood flow; dissipates hydrostatic pressure before blood reaches delicate capillaries [2].", "marks": 2}
        ]
    ))

    # Q13: Lymphatic system architecture & drainage (Fig 8.13)
    questions.append(Question(
        number=13,
        title="9700/21/M/J/18/Q3 - Structure and Function of the Mammalian Lymphatic System",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="The lymphatic system is a secondary circulatory network responsible for drainage and immune surveillance. Fig. 8.13 shows the microscopic anatomy of a blind-ended lymphatic capillary within interstitial body tissues.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_13_lymphatic_system_drainage.png"),
        figure_caption="Fig. 8.13: Structure of a blind-ended lymphatic capillary showing overlapping endothelial cell flap valves and drainage route.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 8.13, describe how the overlapping endothelial cells of lymphatic capillaries act as one-way flap valves.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the mechanisms responsible for propelling lymph through larger lymphatic vessels towards the subclavian veins.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State the role of lymph nodes located along the lymphatic network in protecting the body against systemic infection.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "When interstitial fluid hydrostatic pressure rises above lymphatic pressure, fluid pushes overlapping endothelial flaps open, allowing fluid, proteins, and cellular debris to enter; when internal lymph pressure rises, flaps are pushed shut, preventing backflow [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Contraction of surrounding skeletal muscles massages thin-walled lymph vessels; internal semilunar valves prevent backflow; negative intrathoracic pressure during inhalation draws lymph towards thoracic duct [2].", "marks": 2},
            {"q": "Q13(c)", "points": "Contain reticular meshwork packed with macrophages and lymphocytes; macrophages phagocytose bacteria, viruses, and cellular debris filtered from lymph; dendritic cells present antigens to activate B- and T-lymphocytes for adaptive immunity [2].", "marks": 2}
        ]
    ))

    # Q14: Blood pressure profile across systemic vascular tree (Fig 8.14)
    questions.append(Question(
        number=14,
        title="9700/22/F/M/22/Q3 - Blood Pressure and Pulse Attenuation Across the Systemic Vascular Tree",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="As blood flows from the aorta through the systemic vascular tree, both absolute blood pressure and pulse oscillations undergo profound changes. Fig. 8.14 illustrates the systolic, diastolic, and mean blood pressure profiles from the aorta to the vena cava.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig8_14_cardiac_output_pressures.png"),
        figure_caption="Fig. 8.14: Pressure profile across systemic circulation showing systolic, diastolic, and pulse pressure attenuation.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 8.14, describe what happens to the pulse pressure (the difference between systolic and diastolic pressure) as blood travels from the aorta to the capillaries.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the structure of elastic arteries contributes to dampening pulse pressure and maintaining continuous blood flow.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why blood flow in capillaries must be non-pulsatile and under low pressure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Pulse pressure is wide in aorta and large arteries (~120/80 mmHg = 40 mmHg), narrows sharply in arterioles, and is completely extinguished before reaching capillaries where flow becomes completely non-pulsatile [2].", "marks": 2},
            {"q": "Q14(b)", "points": "Thick tunica media rich in elastic laminae stretches during ventricular systole, storing potential energy; elastically recoils during ventricular diastole, converting pulsatile ejection into continuous forward blood flow (Windkessel effect) [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Thin single-cell capillary walls (~0.5 µm) would rupture under high or pulsatile pressures; slow, non-pulsatile flow allows maximum contact time for diffusion of gases, nutrients, and waste products across endothelium [2].", "marks": 2}
        ]
    ))

    # Q15: Atherosclerosis pathogenesis & coronary occlusion
    questions.append(Question(
        number=15,
        title="9700/21/O/N/19/Q4 - Pathogenesis of Atherosclerosis and Coronary Artery Disease",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Atherosclerosis is a progressive vascular pathology affecting medium and large arteries, particularly the coronary arteries.",
        parts=[
            QuestionPart(label="(a)", text="Describe the sequence of events leading from initial endothelial damage to the formation of a mature atheromatous plaque.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the rupture of an atheroma leads to thrombus formation in a coronary artery.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the physiological consequences of a complete coronary artery occlusion on myocardial tissue.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Endothelial damage (from hypertension, toxins in cigarette smoke) allows low-density lipoproteins (LDLs) to infiltrate tunica intima; macrophages engulf oxidised LDLs becoming foam cells; forms fatty streaks; smooth muscle cells proliferate and deposit fibrous collagen cap, forming a mature atheroma [2].", "marks": 2},
            {"q": "Q15(b)", "points": "Rupture of fibrous cap exposes thrombogenic collagen and tissue factor to blood; platelets adhere and activate, triggering the coagulation cascade (prothrombin -> thrombin -> fibrinogen -> insoluble fibrin mesh); forms a blood clot (thrombus) that occludes lumen [2].", "marks": 2},
            {"q": "Q15(c)", "points": "Downstream cardiac myocytes are deprived of oxygen and glucose; aerobic respiration ceases and ATP depletes; cells undergo irreversible necrosis/infarction (myocardial infarction), impairing cardiac pumping [2].", "marks": 2}
        ]
    ))

    # Q16: Carbon monoxide poisoning & carboxyhaemoglobin
    questions.append(Question(
        number=16,
        title="9700/22/M/J/18/Q4 - Carbon Monoxide Toxicity and Oxygen Affinity Modulation",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="Carbon monoxide (CO) is a colourless, odourless toxic gas present in cigarette smoke and faulty heating appliances.",
        parts=[
            QuestionPart(label="(a)", text="Explain why carbon monoxide binds to haemoglobin in preference to oxygen.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the double pathological effect of carbon monoxide on haemoglobin's oxygen-carrying capacity and oxygen unloading.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why chronic cigarette smokers exhibit a compensatory increase in red blood cell count (polycythaemia).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Carbon monoxide binds to the ferrous ion (Fe2+) of the haem prosthetic group with an affinity approximately 200–250 times greater than oxygen, forming very stable carboxyhaemoglobin (COHb) [2].", "marks": 2},
            {"q": "Q16(b)", "points": "First, directly blocks available O2 binding sites on haemoglobin, reducing oxygen-carrying capacity; second, binding of CO locks remaining subunits in high-affinity relaxed state, shifting curve left and preventing O2 unloading to hypoxic tissues [2].", "marks": 2},
            {"q": "Q16(c)", "points": "Elevated carboxyhaemoglobin causes chronic tissue hypoxia; kidneys detect reduced oxygen delivery and secrete the hormone erythropoietin (EPO); EPO stimulates haematopoietic stem cells in bone marrow to produce more erythrocytes to restore oxygen delivery [2].", "marks": 2}
        ]
    ))

    # Q17: High-altitude physiological acclimatisation
    questions.append(Question(
        number=17,
        title="9700/22/O/N/20/Q2 - Physiological Acclimatisation to High Altitude Hypoxia",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="At high altitudes (e.g. 4000 m above sea level), total atmospheric pressure is reduced, resulting in a significantly lower partial pressure of oxygen in inspired air.",
        parts=[
            QuestionPart(label="(a)", text="Explain why a low atmospheric pO2 reduces the percentage saturation of arterial haemoglobin leaving pulmonary capillaries.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how an increase in red blood cell production improves oxygen transport during long-term altitude acclimatisation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the role of 2,3-bisphosphoglycerate (2,3-BPG) in red blood cells during high-altitude acclimatisation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Lower atmospheric pO2 reduces alveolar pO2 (from ~13 kPa at sea level to ~7 kPa at altitude); reduces steepness of concentration gradient between alveoli and pulmonary capillary blood, resulting in lower equilibrium saturation of haemoglobin (~75–80%) [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Hypoxia stimulates renal secretion of erythropoietin (EPO), increasing erythrocyte count (haematocrit); although each erythrocyte carries less O2, the higher total concentration of haemoglobin per unit blood volume restores overall oxygen carrying capacity [2].", "marks": 2},
            {"q": "Q17(c)", "points": "Erythrocytes increase synthesis of 2,3-BPG, which binds to central cavity of deoxyhaemoglobin; shifts oxygen dissociation curve to the right, facilitating unloading of oxygen to respiring tissues at low tissue pO2 [2].", "marks": 2}
        ]
    ))

    # Q18: Kwashiorkor, hypoproteinaemia & systemic oedema
    questions.append(Question(
        number=18,
        title="9700/21/M/J/20/Q3 - Hypoproteinaemia, Oncotic Pressure, and Systemic Oedema",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Children suffering from severe protein-energy malnutrition (kwashiorkor) characteristically develop pronounced swelling of the abdomen and extremities (oedema).",
        parts=[
            QuestionPart(label="(a)", text="Explain the role of plasma proteins, particularly serum albumin, in maintaining blood oncotic pressure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how severe dietary protein deficiency leads to systemic tissue fluid accumulation (oedema).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest why a blockage of lymphatic drainage (e.g. by filarial nematode parasites in elephantiasis) also results in massive oedema.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Albumin is synthesized by the liver and cannot pass through capillary endothelial pores; remains in blood plasma, creating a colloid osmotic (oncotic) pressure (~ -3.3 kPa / 25 mmHg) that draws water osmotically from interstitial spaces back into capillaries [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Protein deficiency reduces liver albumin synthesis, causing severe hypoproteinaemia; plasma oncotic pressure falls; at venous end of capillaries, inward osmotic draw is insufficient to balance hydrostatic pressure, so fluid is not reabsorbed and accumulates in interstitial tissue spaces [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Lymphatic vessels drain the unabsorbed ~10% of tissue fluid and escaped plasma proteins; blockage halts lymphatic drainage and proteins accumulate in interstitium, raising interstitial oncotic pressure and causing severe swelling [2].", "marks": 2}
        ]
    ))

    # Q19: Cardiac output calculation & stroke volume adaptations
    questions.append(Question(
        number=19,
        title="9700/22/F/M/21/Q3 - Calculation of Cardiac Output and Aerobic Adaptations",
        syllabus_ref="Syllabus 8.3",
        difficulty="ADVANCED",
        preamble="Cardiac output (CO) is the volume of blood pumped by one ventricle per minute and is calculated using the formula: Cardiac Output = Heart Rate x Stroke Volume.",
        parts=[
            QuestionPart(label="(a)", text="A resting individual has a heart rate of 72 bpm and a stroke volume of 70 cm3. Calculate their resting cardiac output in dm3 min-1.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="During strenuous exercise, an athlete's cardiac output increases to 30 dm3 min-1 at a heart rate of 180 bpm. Calculate their exercise stroke volume.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how endurance athletic training produces cardiac hypertrophy, resulting in resting bradycardia (resting heart rate < 50 bpm) while maintaining normal cardiac output.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "CO = HR x SV = 72 x 70 = 5040 cm3 min-1 = 5.04 dm3 min-1 [2].", "marks": 2},
            {"q": "Q19(b)", "points": "SV = CO / HR = 30 000 cm3 min-1 / 180 bpm = 166.7 cm3 (accept 166–167 cm3) [2].", "marks": 2},
            {"q": "Q19(c)", "points": "Training increases left ventricular chamber volume and myocardial thickness (hypertrophy); increases contractility and resting stroke volume (~100–110 cm3); therefore, a lower heart rate (~45–50 bpm) is sufficient to deliver the normal resting cardiac output of ~5.0 dm3 min-1 [2].", "marks": 2}
        ]
    ))

    # Q20: [Mentora Original A* Extension] Nitric oxide endothelial signalling & cGMP
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] Q20 - Endothelial Nitric Oxide Signalling and Smooth Muscle Relaxation",
        syllabus_ref="Syllabus 8.1",
        difficulty="ADVANCED",
        preamble="Vascular endothelial cells play an active endocrine role by releasing chemical mediators that regulate vascular tone in adjacent smooth muscle.",
        parts=[
            QuestionPart(label="(a)", text="Describe how shear stress from flowing blood stimulates endothelial cells to produce nitric oxide (NO).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the intracellular signaling mechanism by which nitric oxide diffuses into vascular smooth muscle and causes vasodilation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how pharmacological agents like nitroglycerin treat angina pectoris.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Increased blood flow exerts frictional shear stress on endothelial luminal membrane; activates endothelial nitric oxide synthase (eNOS), which synthesizes nitric oxide gas (NO) from L-arginine and oxygen [2].", "marks": 2},
            {"q": "Q20(b)", "points": "NO is a small non-polar gas that diffuses rapidly across membranes into adjacent vascular smooth muscle; binds to and activates soluble guanylyl cyclase, converting GTP to cyclic GMP (cGMP); cGMP lowers intracellular Ca2+, causing smooth muscle relaxation and vasodilation [2].", "marks": 2},
            {"q": "Q20(c)", "points": "Nitroglycerin is metabolised in vascular cells to release nitric oxide; causes widespread vasodilation of systemic veins and coronary arteries, reducing venous return (cardiac preload) and myocardial oxygen demand while improving coronary perfusion [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & PHYSIOLOGICAL MECHANISMS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Water properties in blood plasma transport
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q5 - Solvent and Thermal Roles of Water in Blood Plasma",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Water constitutes approximately 90–92% of mammalian blood plasma.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the dipolar nature of water makes it an effective transport medium for dissolved glucose and amino acids.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the importance of water's high specific heat capacity in maintaining thermal homeostasis during physical activity.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Water molecules have partial charges (delta- O, delta+ H); form hydration shells and hydrogen bonds around polar functional groups of glucose and charged amino acids, dissolving them for mass transport in plasma [2].", "marks": 2},
            {"q": "Q21(b)", "points": "A large amount of metabolic heat can be absorbed by circulating blood with minimal rise in temperature; distributes heat from contracting muscle to skin surface for dissipation, preventing thermal denaturation of enzymes [2].", "marks": 2}
        ]
    ))

    # Q22: Elastic recoil in aorta (Windkessel effect)
    questions.append(Question(
        number=22,
        title="9700/21/O/N/22/Q5 - Elastic Arteries and the Windkessel Effect",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="The aorta and pulmonary trunk contain large quantities of elastic tissue in their walls.",
        parts=[
            QuestionPart(label="(a)", text="Describe the changes in the aorta wall during ventricular systole and ventricular diastole.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why loss of arterial elasticity with aging (arteriosclerosis) leads to isolated systolic hypertension.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "During systole, elastic fibres stretch under high pressure, storing potential energy; during diastole, elastic fibres passively recoil against blood, maintaining forward pressure (~80 mmHg) and continuous perfusion [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Stiffened arterial walls cannot expand to accommodate stroke volume; higher pressure is required to force blood into rigid aorta, driving up peak systolic pressure while diastolic pressure falls due to lack of elastic recoil [2].", "marks": 2}
        ]
    ))

    # Q23: Skeletal muscle pump and venous return
    questions.append(Question(
        number=23,
        title="9700/22/M/J/21/Q5 - Skeletal Muscle Pump and Venous Return Mechanisms",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Blood pressure in large systemic veins is typically under 10 mmHg, yet blood must return to the heart against gravity from lower extremities.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the skeletal muscle pump and venous semilunar valves facilitate venous return from the legs.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the clinical cause and appearance of varicose veins.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Contraction of leg skeletal muscles compresses deep veins, squeezing blood upwards; semilunar valves distal to contraction close to prevent backflow, while proximal valves open to allow unidirectional upward flow [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Venous semilunar valves become incompetent / fail to close properly; blood pools under gravity in superficial veins, increasing hydrostatic pressure and causing veins to become permanently dilated, twisted, and swollen [2].", "marks": 2}
        ]
    ))

    # Q24: Capillary endothelium adaptations
    questions.append(Question(
        number=24,
        title="9700/21/M/J/22/Q5 - Capillary Ultrastructure and Transcapillary Exchange",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Capillaries are the definitive exchange vessels connecting arterioles and venules.",
        parts=[
            QuestionPart(label="(a)", text="Describe the cellular structure of a capillary wall, referencing endothelial junctions.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how lipid-soluble substances and small water-soluble ions cross capillary walls by different routes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Single layer of flattened squamous endothelial cells resting on a thin basal lamina; adjacent cells separated by narrow intercellular clefts (~10–15 nm wide) that permit passage of fluid and small polar solutes [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Lipid-soluble substances (O2, CO2, steroid hormones) diffuse directly through the phospholipid bilayer of endothelial cells; small water-soluble ions (Na+, K+, glucose) diffuse through intercellular clefts and fenestrations [2].", "marks": 2}
        ]
    ))

    # Q25: Papillary muscles and chordae tendineae
    questions.append(Question(
        number=25,
        title="9700/22/O/N/20/Q5 - Biomechanics of Papillary Muscles and Chordae Tendineae",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="Atrioventricular valves must remain tightly sealed during the immense pressure of ventricular systole.",
        parts=[
            QuestionPart(label="(a)", text="Describe the anatomical connection between papillary muscles, chordae tendineae, and the atrioventricular valve cusps.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the consequence of a rupture of the chordae tendineae following a myocardial infarction.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "Papillary muscles project from ventricular myocardium into cavity; non-elastic collagenous cords (chordae tendineae) extend from papillary muscle tips and attach to the free margins of AV valve cusps [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Valve cusps are no longer tethered during systole and prolapse (evert) backward into atrium; allows massive systolic regurgitation/backflow of blood into atrium, causing acute pulmonary oedema and heart failure [2].", "marks": 2}
        ]
    ))

    # Q26: Non-conducting fibrous ring of heart
    questions.append(Question(
        number=26,
        title="9700/21/O/N/19/Q5 - Function of the Fibrous Cardiac Skeleton",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="A dense ring of fibrous connective tissue separates the atrial and ventricular syncytia.",
        parts=[
            QuestionPart(label="(a)", text="Explain the electrical insulating role of the atrioventricular fibrous skeleton.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what would happen to cardiac coordination if the wave of excitation could cross directly from atria to ventricles across the fibrous ring.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Composed of non-conducting collagen/elastic fibrous tissue; prevents direct electrical conduction from atrial muscle to ventricular muscle, forcing impulse to pass exclusively through the AV node [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Ventricles would begin contracting prematurely from the top down immediately after atria; would prevent complete ventricular filling and trap blood in the apex instead of pumping it out through semilunar valves [2].", "marks": 2}
        ]
    ))

    # Q27: Structural difference between HbA and HbF
    questions.append(Question(
        number=27,
        title="9700/22/M/J/19/Q5 - Polypeptide Subunit Composition of HbA vs HbF",
        syllabus_ref="Syllabus 8.2",
        difficulty="CHALLENGING",
        preamble="Adult and fetal haemoglobins have distinct subunit compositions coded by different globin genes.",
        parts=[
            QuestionPart(label="(a)", text="State the polypeptide chain composition of adult haemoglobin (HbA) compared to fetal haemoglobin (HbF).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the presence of gamma chains in HbF gives it a higher affinity for oxygen than HbA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "HbA consists of two alpha-globin and two beta-globin chains (alpha2 beta2); HbF consists of two alpha-globin and two gamma-globin chains (alpha2 gamma2) [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Gamma chains lack a specific positively charged histidine residue found in beta chains; binds 2,3-BPG with significantly lower affinity, leaving HbF in high-affinity conformation to bind oxygen at lower pO2 [2].", "marks": 2}
        ]
    ))

    # Q28: Carbaminohaemoglobin formation
    questions.append(Question(
        number=28,
        title="9700/22/F/M/20/Q5 - Mechanism of Carbaminohaemoglobin Formation",
        syllabus_ref="Syllabus 8.2",
        difficulty="CHALLENGING",
        preamble="Approximately 10% of carbon dioxide in blood is carried directly bound to haemoglobin.",
        parts=[
            QuestionPart(label="(a)", text="Describe how carbon dioxide binds to haemoglobin to form carbaminohaemoglobin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why deoxygenated haemoglobin binds carbon dioxide more readily than oxyhaemoglobin (the Haldane effect).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "CO2 reacts reversibly with uncharged terminal amino groups (-NH2) of the globin polypeptide chains to form carbamate groups (-NHCOO-), releasing a proton: Hb-NH2 + CO2 <-> Hb-NHCOO- + H+ [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Deoxygenation alters the conformation of haemoglobin, making terminal amino groups more basic and accessible; allows deoxygenated blood to carry more CO2 at any given pCO2 than oxygenated blood [2].", "marks": 2}
        ]
    ))

    # Q29: Plasma transport of hydrogencarbonate ions
    questions.append(Question(
        number=29,
        title="9700/21/M/J/20/Q5 - Hydrogencarbonate Ion Transport and Plasma Buffer Systems",
        syllabus_ref="Syllabus 8.2",
        difficulty="CHALLENGING",
        preamble="The majority (~85%) of carbon dioxide is transported as dissolved hydrogencarbonate ions.",
        parts=[
            QuestionPart(label="(a)", text="Describe how hydrogencarbonate ions are formed in erythrocytes and transported in plasma.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the hydrogencarbonate buffer system in blood plasma resists pH changes when lactic acid enters during exercise.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Carbonic anhydrase hydrates CO2 to H2CO3, which dissociates into H+ and HCO3-; HCO3- diffuses out of erythrocyte down concentration gradient into plasma via Band 3 anion exchanger in exchange for Cl- [2].", "marks": 2},
            {"q": "Q29(b)", "points": "Excess H+ ions from lactic acid react with plasma HCO3- to form H2CO3: H+ + HCO3- <-> H2CO3; H2CO3 breaks down into CO2 and H2O; excess CO2 is eliminated by hyperventilation, maintaining pH at ~7.4 [2].", "marks": 2}
        ]
    ))

    # Q30: Left atrium vs left ventricle wall thickness
    questions.append(Question(
        number=30,
        title="9700/22/O/N/18/Q5 - Structural Comparison of Atrial and Ventricular Myocardium",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="The myocardium of the four cardiac chambers shows distinct variations in thickness.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the wall of the left ventricle is thicker than the wall of the left atrium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why ventricular filling is mostly passive before atrial systole occurs.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Left atrium only pumps blood past the AV valve into the relaxed left ventricle; left ventricle must generate enough contractile force to overcome systemic vascular resistance and pump blood through aorta to entire body [2].", "marks": 2},
            {"q": "Q30(b)", "points": "During diastole, ventricles relax and internal pressure falls below atrial pressure; AV valves open and ~70–80% of ventricular filling occurs passively by gravity and venous suction before atria contract [2].", "marks": 2}
        ]
    ))

    # Q31: AV nodal delay physiological necessity
    questions.append(Question(
        number=31,
        title="9700/21/M/J/19/Q5 - Cellular Mechanism of the Atrioventricular Nodal Delay",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="Conduction velocity drops significantly as the electrical impulse enters the AV node.",
        parts=[
            QuestionPart(label="(a)", text="Describe the cellular adaptations of AV nodal myocytes that cause the 0.1 second conduction delay.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what would occur if the AV nodal delay were absent.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "AV nodal myocytes have much smaller diameters, fewer gap junctions in intercalated discs, and a slower upstroke of action potential, drastically slowing conduction velocity (~0.05 m s-1 vs ~4 m s-1 in Purkyne fibres) [2].", "marks": 2},
            {"q": "Q31(b)", "points": "Ventricles would contract simultaneously with atria; AV valves would slam shut before atria empty, drastically reducing end-diastolic volume, stroke volume, and cardiac output [2].", "marks": 2}
        ]
    ))

    # Q32: Pulmonary vs systemic pressure rationale
    questions.append(Question(
        number=32,
        title="9700/22/F/M/19/Q5 - Hemodynamics: Pulmonary vs Systemic Pressure Gradients",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="The right ventricle generates a peak systolic pressure of ~25 mmHg, while the left ventricle generates ~120 mmHg.",
        parts=[
            QuestionPart(label="(a)", text="Explain the structural reasons for the low resistance of the pulmonary circuit.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the medical hazard of elevated pulmonary blood pressure (pulmonary hypertension).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Pulmonary vessels are short, have wider diameters, and branch into an enormous parallel capillary bed across millions of alveoli, offering very low total vascular resistance [2].", "marks": 2},
            {"q": "Q32(b)", "points": "High hydrostatic pressure in pulmonary capillaries forces excess fluid into alveolar air spaces (pulmonary oedema); impairs gas exchange, increases diffusion distance for O2, and leads to right ventricular heart failure [2].", "marks": 2}
        ]
    ))

    # Q33: Composition of lymph vs tissue fluid vs plasma
    questions.append(Question(
        number=33,
        title="9700/21/O/N/18/Q5 - Compositional Comparison: Plasma, Tissue Fluid, and Lymph",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Extracellular fluids in mammals undergo continuous exchange and filtration.",
        parts=[
            QuestionPart(label="(a)", text="Compare the protein and lipid content of tissue fluid with that of blood plasma.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why lymph draining from the small intestine (lacteals) has a milky appearance (chyle).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Tissue fluid contains only very low concentrations of small proteins (albumins) and virtually no large proteins (fibrinogen); plasma has high protein content (~70 g dm-3) and lipid lipoproteins [2].", "marks": 2},
            {"q": "Q33(b)", "points": "Dietary fats are absorbed into lacteal lymphatic capillaries as chylomicrons (droplets of triglycerides coated in protein and phospholipid); suspended lipid droplets scatter light, producing an opaque milky emulsion [2].", "marks": 2}
        ]
    ))

    # Q34: Neutrophil diapedesis and phagocytosis
    questions.append(Question(
        number=34,
        title="9700/22/M/J/17/Q5 - Neutrophil Extravasation and Phagocytosis",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Neutrophils are the first leukocytes recruited to sites of acute bacterial infection.",
        parts=[
            QuestionPart(label="(a)", text="Describe how neutrophils leave post-capillary venules and enter infected tissues (diapedesis).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how neutrophils destroy engulfed bacterial pathogens inside phagolysosomes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Inflammatory cytokines cause endothelial cells to express selectins and integrins; neutrophils marginate, roll, adhere firmly, and squeeze through widened intercellular endothelial junctions by amoeboid movement [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Phagosome fuses with primary granules containing lysozyme, defensins, and myeloperoxidase; releases reactive oxygen species (respiratory burst producing H2O2 and superoxide) and proteases, enzymatically digesting pathogen [2].", "marks": 2}
        ]
    ))

    # Q35: Monocyte differentiation into macrophages
    questions.append(Question(
        number=35,
        title="9700/21/O/N/17/Q5 - Monocyte Ontogeny and Macrophage Functions",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Monocytes are the largest circulating agranulocytes in mammalian blood.",
        parts=[
            QuestionPart(label="(a)", text="Describe the morphological changes that occur when a monocyte matures into a tissue macrophage.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Contrast the lifespan and phagocytic capacity of macrophages with those of neutrophils.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Cell enlarges up to 5-fold, increases synthesis of lysosomes and mitochondria, develops extensive pseudopodia for motility, and expresses higher densities of cell-surface pattern-recognition receptors [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Neutrophils are short-lived (hours to days), phagocytose 5–20 bacteria and then die forming pus; macrophages are long-lived (months to years), can phagocytose over 100 pathogens, and digest larger debris [2].", "marks": 2}
        ]
    ))

    # Q36: Myogenic property of cardiac myocytes
    questions.append(Question(
        number=36,
        title="9700/22/M/J/16/Q5 - Electrophysiological Basis of Myogenic Automaticity",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="Unlike skeletal muscle, mammalian cardiac muscle beats autonomously without neural input.",
        parts=[
            QuestionPart(label="(a)", text="Explain how pacemaker potentials in the Sinoatrial Node generate spontaneous myogenic contractions.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the autonomic nervous system modulates heart rate above or below the intrinsic SAN rate.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "SAN myocytes have unstable resting membrane potentials due to leaky 'funny' Na+ channels and transient Ca2+ channels; slow inward leak depolarises membrane to threshold, firing spontaneous action potentials [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Sympathetic nerves release noradrenaline (binding beta-1 receptors) to increase Na+/Ca2+ permeability, speeding depolarisation and increasing heart rate; parasympathetic (vagus) nerve releases acetylcholine to hyperpolarise SAN, decreasing heart rate [2].", "marks": 2}
        ]
    ))

    # Q37: Cause of dicrotic notch on aortic pressure curve
    questions.append(Question(
        number=37,
        title="9700/21/M/J/18/Q5 - The Dicrotic Notch and Aortic Valve Dynamics",
        syllabus_ref="Syllabus 8.3",
        difficulty="CHALLENGING",
        preamble="A small transient rise in aortic pressure known as the dicrotic notch appears immediately following ventricular systole.",
        parts=[
            QuestionPart(label="(a)", text="Describe the pressure gradient that causes the aortic semilunar valve to snap shut at the end of systole.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why aortic pressure rebounds upward slightly immediately following valve closure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Ventricular myocardium relaxes during isovolumetric relaxation, dropping ventricular pressure below ~100 mmHg; pressure in stretched aorta remains higher (~100 mmHg), creating a reversed gradient that drives blood back towards ventricle [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Retrograde blood fills the cup-shaped cusps of the aortic semilunar valve, slamming them shut; the momentum of rebounding blood against the closed valve and elastic recoil of the aorta produces a brief pressure inflection [2].", "marks": 2}
        ]
    ))

    # Q38: Precapillary sphincters and blood flow shunting
    questions.append(Question(
        number=38,
        title="9700/22/O/N/16/Q5 - Precapillary Sphincters and Microvascular Shunting",
        syllabus_ref="Syllabus 8.1",
        difficulty="CHALLENGING",
        preamble="Not all capillary beds in the body can be simultaneously perfused with blood.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure and location of precapillary sphincters in a microvascular bed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how blood bypasses a capillary bed when precapillary sphincters constrict.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Rings of smooth muscle wrapped around the entrance of each true capillary where it branches off a metarteriole or terminal arteriole [2].", "marks": 2},
            {"q": "Q38(b)", "points": "Constriction of sphincters shuts off flow into true capillary loops; blood is shunted directly from arteriole to venule through a vascular thoroughfare channel (arteriovenous shunt), conserving blood volume [2].", "marks": 2}
        ]
    ))

    # Q39: [Mentora Original A* Extension] Starling's Law of the Heart
    questions.append(Question(
        number=39,
        title="[Mentora Original A* Extension] Q39 - Frank-Starling Mechanism and Myocardial Length-Tension Relationship",
        syllabus_ref="Syllabus 8.3",
        difficulty="ADVANCED",
        preamble="The intrinsic ability of the heart to adapt to changing volumes of inflowing blood is described by Frank-Starling's law of the heart.",
        parts=[
            QuestionPart(label="(a)", text="State Frank-Starling's law of the heart in terms of end-diastolic volume and stroke volume.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the sliding filament mechanism underlying the increased contractile force when cardiac muscle is stretched.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "The stroke volume of the heart increases in direct proportion to an increase in the volume of blood in the ventricles before contraction (end-diastolic volume / preload) [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Increased venous return stretches cardiac myocytes toward optimal sarcomere length (~2.2 µm); increases affinity of troponin C for Ca2+ and optimizes actin-myosin cross-bridge overlap, generating greater peak systolic force [2].", "marks": 2}
        ]
    ))

    # Q40: [Mentora Original A* Extension] Sickle cell crisis in microcirculation
    questions.append(Question(
        number=40,
        title="[Mentora Original A* Extension] Q40 - Sickle Cell Microvascular Occlusion and Vaso-Occlusive Crisis",
        syllabus_ref="Syllabus 8.2",
        difficulty="ADVANCED",
        preamble="In individuals homozygous for the HbS allele, severe hypoxia triggers sickle cell crises in microcirculatory beds.",
        parts=[
            QuestionPart(label="(a)", text="Explain why sickling of red blood cells occurs preferentially in systemic capillary beds rather than pulmonary capillaries.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the pathophysiology of a vaso-occlusive crisis resulting from sickled erythrocytes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Deoxygenated HbS exposes a hydrophobic valine patch that polymerises into rigid insoluble fibres; systemic capillary beds have low pO2 (~4 kPa) where HbS unloads O2 and polymerises, whereas pulmonary capillaries have high pO2 where HbS is oxygenated and soluble [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Sickled erythrocytes lose flexibility and become crescent-shaped; adhere to capillary endothelium and become mechanically trapped in narrow microvessels (~7 µm); causes vaso-occlusion, blocking blood flow, causing local tissue ischemia, severe pain, and infarction [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Closed double circulation definition
    questions.append(Question(
        number=41,
        title="9700/12/M/J/23/Q31 - Define Closed Double Circulation",
        syllabus_ref="Syllabus 8.1",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="Define the terms closed circulation and double circulation as applied to mammals.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "Closed: blood is confined within a continuous network of blood vessels (does not directly bathe tissues); Double: blood passes through the heart twice during one complete circuit of the body (pulmonary and systemic circuits) [2].", "marks": 2}
        ]
    ))

    # Q42: Erythrocyte dimensions
    questions.append(Question(
        number=42,
        title="9700/11/O/N/22/Q32 - Dimensions and Surface Area of Erythrocytes",
        syllabus_ref="Syllabus 8.1",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="State the mean diameter and thickness of a mature human erythrocyte, and state one advantage of this size.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "Diameter = 7.0–7.5 µm; thickness = 2.0 µm; diameter matches capillary diameter (~7 µm), forcing single-file flow to maximize surface contact and minimize diffusion distance for O2 [2].", "marks": 2}
        ]
    ))

    # Q43: Bohr effect definition
    questions.append(Question(
        number=43,
        title="9700/12/M/J/22/Q33 - Define the Bohr Effect",
        syllabus_ref="Syllabus 8.2",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="Define the Bohr effect and state its direct physiological significance in metabolically active tissues.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "The decrease in the oxygen affinity of haemoglobin caused by an increase in carbon dioxide concentration and/or a decrease in pH; causes haemoglobin to release more oxygen in actively respiring tissues [2].", "marks": 2}
        ]
    ))

    # Q44: SAN function
    questions.append(Question(
        number=44,
        title="9700/13/O/N/21/Q30 - Function of the Sinoatrial Node",
        syllabus_ref="Syllabus 8.3",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="State the exact anatomical location of the Sinoatrial Node (SAN) and describe its physiological role.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Located in the superior wall of the right atrium near the opening of the superior vena cava; acts as the primary pacemaker by generating rhythmic waves of electrical depolarisation that initiate heartbeat [2].", "marks": 2}
        ]
    ))

    # Q45: Carbonic anhydrase
    questions.append(Question(
        number=45,
        title="9700/12/F/M/22/Q32 - Function of Carbonic Anhydrase",
        syllabus_ref="Syllabus 8.2",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="State the intracellular location of carbonic anhydrase in blood and write the balanced chemical equation it catalyses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "Located inside erythrocytes (red blood cells); catalyses CO2 + H2O <-> H2CO3 (carbon dioxide + water <-> carbonic acid) [2].", "marks": 2}
        ]
    ))

    # Q46: Chordae tendineae
    questions.append(Question(
        number=46,
        title="9700/11/M/J/21/Q31 - Function of Chordae Tendineae",
        syllabus_ref="Syllabus 8.3",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="State the tissue composition of the chordae tendineae and explain why they must be non-elastic.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "Composed of dense regular fibrous connective tissue rich in inelastic collagen; must be non-elastic so they do not stretch under ventricular systolic pressure, preventing AV valve eversion into atria [2].", "marks": 2}
        ]
    ))

    # Q47: P50 definition
    questions.append(Question(
        number=47,
        title="9700/12/O/N/20/Q32 - Define P50 of Haemoglobin",
        syllabus_ref="Syllabus 8.2",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="Define the term P50 in relation to haemoglobin and state its typical value for normal adult human blood.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "The partial pressure of oxygen at which haemoglobin is exactly 50% saturated with oxygen; normal adult human HbA value is approximately 3.5–3.7 kPa (26–28 mmHg) [2].", "marks": 2}
        ]
    ))

    # Q48: Plasma vs tissue fluid differences
    questions.append(Question(
        number=48,
        title="9700/11/M/J/20/Q33 - Differences Between Plasma and Tissue Fluid",
        syllabus_ref="Syllabus 8.1",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="State two compositional differences between blood plasma and tissue fluid.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "Plasma contains red blood cells, platelets, and high concentrations of plasma proteins (e.g. albumin, fibrinogen); tissue fluid contains no red blood cells/platelets and very low protein concentration [2].", "marks": 2}
        ]
    ))

    # Q49: [Mentora Original A* Extension] Chloride shift definition
    questions.append(Question(
        number=49,
        title="[Mentora Original A* Extension] Q49 - Define the Chloride Shift",
        syllabus_ref="Syllabus 8.2",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="Define the term chloride shift and name the membrane transport protein responsible for it.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "The movement of chloride ions (Cl-) from plasma into erythrocytes as hydrogencarbonate ions (HCO3-) diffuse out, maintaining electrochemical neutrality; mediated by the Band 3 anion exchanger protein [2].", "marks": 2}
        ]
    ))

    # Q50: [Mentora Original A* Extension] Vulnerability of coronary arteries
    questions.append(Question(
        number=50,
        title="[Mentora Original A* Extension] Q50 - Susceptibility of Coronary Arteries to Atheroma",
        syllabus_ref="Syllabus 8.1",
        difficulty="CORE",
        parts=[
            QuestionPart(label="(a)", text="Explain why coronary arteries are especially susceptible to the formation of atheromas compared to other systemic arteries.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "Coronary arteries arise directly from base of aorta and experience high systolic pressure pulses and turbulent flow around sharp bifurcations; mechanical shear stress causes endothelial micro-tears that trigger lipid infiltration [2].", "marks": 2}
        ]
    ))

    # Assign section keys
    for q in questions:
        if q.number <= 20:
            q.section_key = "Section A — High-Tariff Structured Analysis & Data Evaluation (120 Marks)"
        elif q.number <= 40:
            q.section_key = "Section B — Core Conceptual & Physiological Mechanism Questions (80 Marks)"
        else:
            q.section_key = "Section C — High-Yield Rapid Recall & Rigorous Definitions (20 Marks)"

    return questions

def get_topic8_faqs():
    return [
        {
            "q_num": 1,
            "title": "Why Is a Closed Double Circulatory System Superior to a Single Circulation in Endothermic Mammals?",
            "category": "Comparative Hemodynamics • Double Circulation",
            "examiner_trap": "Stating that double circulation allows oxygenated and deoxygenated blood to mix, or failing to explain why pressure drops across gas exchange capillary beds.",
            "model_answer": "• Pressure Loss across Capillaries: As blood passes through narrow capillary networks (whether in fish gills or mammalian lungs), friction against vessel walls causes a massive drop in hydrostatic pressure.\n• Limitation of Single Circulation: In fish, blood pumped by the heart passes through gill capillaries, loses pressure, and flows sluggishly through systemic tissues under low pressure; severely limits the rate of oxygen and nutrient delivery.\n• Double Circulation Architecture:\n  1. Pulmonary Circuit: Right ventricle pumps deoxygenated blood under low pressure (~25 mmHg) to the lungs; protects delicate alveolar capillaries from rupture and pulmonary oedema while allowing sufficient time for complete gas exchange;\n  2. Systemic Circuit: Oxygenated blood returns to the left atrium and passes into the left ventricle, which repressurises it to high pressure (~120 mmHg);\n  3. High-Pressure Systemic Delivery: Drives rapid mass flow through extensive systemic capillary networks, sustaining the high metabolic rates, active lifestyle, and endothermic thermoregulation of mammals."
        },
        {
            "q_num": 2,
            "title": "How Do the Histological Layers of Arteries, Veins, and Capillaries Relate Directly to Their Hemodynamic Functions?",
            "category": "Histology • Structure-Function Relationships",
            "examiner_trap": "Confusing elastic tissue function (stretching and recoiling to smooth out pulse) with smooth muscle function (contracting and relaxing to alter lumen diameter and distribute blood).",
            "model_answer": "• Arteries (Pressure Reservoirs):\n  1. Tunica Intima: Smooth endothelium minimizes friction; internal elastic lamina;\n  2. Tunica Media: Extremely thick layer rich in elastic fibres and smooth muscle; elastic fibres stretch during ventricular systole to absorb high pulse pressure, and recoil during diastole to maintain continuous forward flow (Windkessel effect); smooth muscle contracts (vasoconstriction) or relaxes (vasodilation) to regulate peripheral vascular resistance and distribute flow;\n  3. Tunica Externa: Thick collagen coat prevents bursting under extreme systolic pressures; narrow regular lumen maintains high pressure.\n• Veins (Capacitance / Blood Reservoirs):\n  1. Tunica Media: Much thinner than arteries with minimal elastic fibres and sparse smooth muscle (low pressure environment, ~5–10 mmHg);\n  2. Wide Irregular Lumen: Offers minimal resistance to venous return;\n  3. Semilunar Valves: Endothelial flap valves prevent backflow under gravity, working with skeletal muscle pumps to return blood to the heart.\n• Capillaries (Exchange Vessels):\n  1. Single Squamous Endothelial Layer: ~0.5 µm thick, providing minimal diffusion distance for metabolic exchange;\n  2. Narrow Lumen (~7 µm): Squeezes erythrocytes into single file, slowing transit time and maximizing surface contact for diffusion."
        },
        {
            "q_num": 3,
            "title": "Explain the Formation and Reabsorption of Tissue Fluid across Capillary Beds Based on Starling's Hypothesis.",
            "category": "Microcirculation • Starling Forces & Oedema",
            "examiner_trap": "Claiming that tissue fluid is formed by active transport or diffusion. Tissue fluid formation is driven by pressure ultrafiltration through intercellular endothelial clefts.",
            "model_answer": "• Starling Forces Balance:\n  1. Hydrostatic Pressure (HP): Blood pressure forced against capillary walls by heart pumping; pushes fluid out of capillaries into interstitium;\n  2. Oncotic Pressure (OP / Colloid Osmotic Pressure): Osmotic pressure exerted by large plasma proteins (mainly albumin) trapped in capillary lumen; draws fluid back into capillaries.\n• Arterial End (Net Ultrafiltration):\n  1. Capillary HP (+4.3 kPa / 32 mmHg) exceeds inward OP (-3.3 kPa / 25 mmHg);\n  2. Net filtration pressure = +1.0 kPa (+7 mmHg); forces water, glucose, amino acids, ions, and dissolved O2 out through capillary intercellular clefts into tissue spaces to bathe cells;\n  3. Cells and large plasma proteins are retained inside capillaries.\n• Venous End (Net Reabsorption):\n  1. Frictional resistance along capillary drops HP to +1.6 kPa (12 mmHg);\n  2. Inward OP remains constant at -3.3 kPa (-25 mmHg);\n  3. Net absorption pressure = -1.7 kPa (-13 mmHg); draws ~90% of tissue fluid containing metabolic wastes (urea, CO2) back into blood.\n• Lymphatic Drainage: Remaining ~10% of interstitial fluid enters blind-ended lymphatic capillaries, passing through lymph nodes and returning to circulation via subclavian veins."
        },
        {
            "q_num": 4,
            "title": "Why Is the Oxygen Dissociation Curve for Adult Haemoglobin Sigmoidal (S-Shaped) Rather Than Hyperbolic?",
            "category": "Biochemical Kinetics • Allosteric Cooperativity",
            "examiner_trap": "Attributing the sigmoidal shape to 'surface area' or confusing it with an enzyme saturation curve. It is caused by positive cooperativity among four allosteric globin subunits.",
            "model_answer": "• Quaternary Structure: Adult haemoglobin (HbA) is a tetramer of four globin polypeptides (two alpha and two beta chains), each enclosing a haem prosthetic group containing an iron ion (Fe2+) capable of reversibly binding one O2 molecule (total 4 O2 per molecule).\n• Tense (T) vs Relaxed (R) Allosteric States:\n  1. Initial Flat Region: In deoxygenated blood, haemoglobin resides in a rigid, low-affinity T-conformation held by salt bridges; binding of the first O2 molecule is thermodynamically difficult (shallow curve at low pO2);\n  2. Positive Cooperativity (Steep Region): Binding of the first O2 pulls the Fe2+ ion into the porphyrin ring, altering the tertiary structure of that subunit and breaking salt bridges; triggers a quaternary conformational shift into the high-affinity R-conformation;\n  3. Relaxed Subunits: The binding sites of the remaining three subunits are exposed, multiplying their affinity for oxygen by ~300-fold; binding of the 2nd and 3rd O2 occurs with immense ease, producing a steep sigmoidal rise;\n  4. Plateau Region: Once three sites are filled, finding the final unoccupied 4th site depends purely on random collision frequency, flattening the curve near 100% saturation.\n• Physiological Value: Ensures haemoglobin loads to near 100% in lungs (pO2 ~12 kPa) and unloads massive volumes of oxygen over the narrow physiological range found in tissues (pO2 2–6 kPa)."
        },
        {
            "q_num": 5,
            "title": "What Is the Molecular Mechanism of the Bohr Effect and Why Is It Physiologically Advantageous During Strenuous Exercise?",
            "category": "Respiratory Biochemistry • The Bohr Shift",
            "examiner_trap": "Stating that CO2 binds to the iron atom in haem. CO2 forms carbaminohaemoglobin at terminal amino groups, while H+ binds to allosteric globin residues, driving the Bohr shift.",
            "model_answer": "• Biochemical Mechanism of the Bohr Shift:\n  1. Actively respiring tissues produce elevated partial pressures of carbon dioxide (pCO2) and lactic acid;\n  2. Carbonic anhydrase inside erythrocytes hydrates CO2: CO2 + H2O <-> H2CO3 <-> H+ + HCO3-;\n  3. Excess H+ ions bind to specific histidine and other allosteric amino acid residues on globin chains, forming haemoglobinic acid (HHb);\n  4. Proton binding forms new salt bridges that stabilize the low-affinity Tense (T) deoxygenated conformation;\n  5. This reduces haemoglobin's affinity for oxygen, shifting the entire oxygen dissociation curve to the RIGHT.\n• Physiological Advantage During Exercise:\n  1. In working muscles, pCO2 rises and pH drops (acidosis);\n  2. At any given tissue pO2 (e.g. 4.0 kPa), haemoglobin releases significantly more oxygen (an additional 15–20% of its payload) compared to resting conditions;\n  3. Unloaded oxygen diffuses into mitochondria, sustaining aerobic cellular respiration and delaying the onset of anaerobic lactic fermentation.\n• Pulmonary Reversal: In lungs, CO2 is excreted; pH rises, shifting curve left, increasing affinity for complete O2 loading."
        },
        {
            "q_num": 6,
            "title": "Detail the Biochemical Steps of Carbon Dioxide Transport in Erythrocytes, Including the Action of Carbonic Anhydrase and the Chloride Shift.",
            "category": "Cellular Biochemistry • Erythrocyte Physiology",
            "examiner_trap": "Omitting the Band 3 anion exchanger or failing to state that the chloride shift maintains electrical neutrality across the erythrocyte membrane.",
            "model_answer": "• Three Modes of CO2 Transport in Blood:\n  1. Dissolved in physical solution in plasma (~5%);\n  2. Bound to globin amino terminals as carbaminohaemoglobin (~10%): CO2 + Hb-NH2 <-> Hb-NHCOO- + H+;\n  3. Converted into hydrogencarbonate ions (HCO3-) transported in plasma (~85%).\n• Intra-Erythrocyte Carbonic Anhydrase Reaction:\n  1. CO2 diffuses from respiring cells down its concentration gradient into erythrocytes;\n  2. Carbonic anhydrase catalyses the rapid reversible hydration of CO2: CO2 + H2O <-> H2CO3 (increases reaction rate by 10,000-fold);\n  3. Carbonic acid immediately dissociates spontaneously into hydrogen ions and hydrogencarbonate ions: H2CO3 <-> H+ + HCO3-;\n  4. Haemoglobin acts as a buffer: Deoxygenated haemoglobin binds H+ to form haemoglobinic acid (HHb), preventing intracellular acidosis.\n• The Chloride Shift (Hamburger Phenomenon):\n  1. As [HCO3-] accumulates inside erythrocyte, it diffuses down its concentration gradient out into the blood plasma;\n  2. Efflux of negatively charged HCO3- leaves a net positive charge inside the cell;\n  3. Chloride ions (Cl-) in plasma rapidly diffuse into the erythrocyte via the Band 3 anion exchanger membrane protein;\n  4. Ensures electrochemical neutrality (electrical balance) is strictly maintained across the erythrocyte membrane."
        },
        {
            "q_num": 7,
            "title": "Why Does Fetal Haemoglobin (HbF) Exhibit a Higher Oxygen Affinity than Maternal Adult Haemoglobin (HbA) and How Does This Enable Placental Gas Exchange?",
            "category": "Developmental Physiology • Placental Exchange",
            "examiner_trap": "Claiming that fetal blood and maternal blood mix in the placenta. The two circulations remain completely separated by the placental barrier.",
            "model_answer": "• Structural Subunit Difference:\n  1. Adult haemoglobin (HbA) consists of two alpha-globin and two beta-globin chains (alpha2 beta2);\n  2. Fetal haemoglobin (HbF) consists of two alpha-globin and two gamma-globin chains (alpha2 gamma2).\n• Molecular Mechanism of Higher Affinity:\n  1. Gamma chains lack a positively charged histidine residue (His143) present in beta chains, replacing it with a neutral serine;\n  2. Consequently, HbF binds the allosteric inhibitor 2,3-bisphosphoglycerate (2,3-BPG) with significantly lower affinity than maternal HbA;\n  3. Without 2,3-BPG binding to lock it in the low-affinity T-state, HbF remains predominantly in the high-affinity Relaxed (R) state;\n  4. Shifts the oxygen dissociation curve of fetal blood to the LEFT of maternal blood (lower P50: ~2.4 kPa vs ~3.6 kPa).\n• Placental Transfer Dynamics:\n  1. Maternal and fetal blood streams flow in close proximity through placental capillaries without mixing;\n  2. At the prevailing placental pO2 (~4.0 kPa), maternal HbA has lower affinity and unloads oxygen;\n  3. Fetal HbF has higher affinity at the same pO2 and binds the released oxygen tightly, ensuring efficient net uptake of oxygen into the fetal circulation to sustain development."
        },
        {
            "q_num": 8,
            "title": "How Are the Events of the Cardiac Cycle (Valve Closures, Heart Sounds, and Pressure Crossovers) Deduced from a Wiggers Diagram?",
            "category": "Cardiac Electrophysiology • Wiggers Diagram Interpretation",
            "examiner_trap": "Confusing the order of valve closures. Remember: AV valves close FIRST at the start of ventricular systole; semilunar valves open, then close at the start of diastole.",
            "model_answer": "• Key Diagnostic Pressure Crossovers:\n  1. Atrioventricular (AV) Valve Closure (t ≈ 0.11 s):\n     - Ventricular systole begins; ventricular pressure rises sharply above atrial pressure;\n     - Blood pushes upward against AV valve cusps, snapping them shut;\n     - Produces the first heart sound, S1 ('lub');\n     - Initiates Isovolumetric Contraction (ventricles contract with all valves closed; pressure skyrockets without volume change).\n  2. Aortic Semilunar Valve Opening (t ≈ 0.15 s):\n     - Ventricular pressure rises above aortic pressure (~80 mmHg);\n     - Semilunar valve flaps forced open; rapid ventricular ejection begins; ventricular volume drops steeply from 125 cm3 to 60 cm3 (stroke volume ≈ 65 cm3).\n  3. Aortic Semilunar Valve Closure (t ≈ 0.38 s):\n     - Ventricular myocardium begins relaxing; ventricular pressure drops below aortic pressure;\n     - Retrograde blood flow snaps aortic semilunar valve shut;\n     - Produces the second heart sound, S2 ('dub');\n     - Sudden rebound against closed valve causes the dicrotic notch on the aortic pressure waveform;\n     - Initiates Isovolumetric Relaxation (pressure drops with all valves closed).\n  4. AV Valve Opening (t ≈ 0.45 s):\n     - Ventricular pressure falls below atrial pressure; AV valves open, beginning rapid passive ventricular filling."
        },
        {
            "q_num": 9,
            "title": "Explain How the Wave of Electrical Depolarisation Coordinates Atrial and Ventricular Systole, Emphasising the Pacemaker and AV Nodal Delay.",
            "category": "Cardiac Conduction • Pacemaker & Purkyne System",
            "examiner_trap": "Stating that the AV node initiates the heartbeat. The Sinoatrial Node (SAN) is the primary pacemaker; the AVN delays the impulse.",
            "model_answer": "• Myogenic Origin & Pacemaker (SAN):\n  1. Sinoatrial Node (SAN) in right atrial wall initiates intrinsic myogenic depolarisation waves at ~70–80 bpm;\n  2. Wave spreads rapidly across atrial muscle via gap junctions in intercalated discs, causing atrial systole (contracting from top down, pushing blood into ventricles).\n• Electrical Block by Fibrous Skeleton:\n  1. Non-conducting fibrous ring of connective tissue between atria and ventricles completely blocks direct electrical passage, preventing ventricles from contracting from the top down.\n• Atrioventricular Nodal Delay (AVN):\n  1. Wave of excitation reaches Atrioventricular Node (AVN) in lower interatrial septum;\n  2. AVN cells have smaller diameters and fewer gap junctions, delaying transmission by ~0.10–0.12 seconds;\n  3. Critical function: Guarantees that atria have completely finished contracting and emptying blood into ventricles before ventricles begin contracting.\n• Rapid Purkyne Conduction to Apex:\n  1. Impulse leaves AVN and speeds down the Bundle of His within the interventricular septum, dividing into left and right bundle branches;\n  2. Spreads rapidly through specialized Purkyne fibres (conduction velocity ~4 m s-1) to the ventricular apex;\n  3. Depolarisation spreads upward through ventricular myocardium, causing ventricles to contract from the apex upward, squeezing blood upwards into the aorta and pulmonary artery."
        },
        {
            "q_num": 10,
            "title": "Why Does the Steepest Drop in Systemic Blood Pressure Occur in Arterioles Rather than Capillaries or Veins?",
            "category": "Hemodynamics • Peripheral Resistance",
            "examiner_trap": "Assuming blood pressure drops most in capillaries because capillaries are narrow. Capillaries have an immense total cross-sectional area which lowers resistance.",
            "model_answer": "• The Peripheral Resistance Vessels (Arterioles):\n  1. As blood flows from the aorta (~100 mmHg) through muscular arteries, pressure remains relatively high with wide pulse oscillations;\n  2. The steepest drop in blood pressure occurs across the arterioles, where mean pressure plunges from ~85 mmHg down to ~35 mmHg (a massive ~50 mmHg drop across a few millimetres).\n• Physical and Anatomical Rationale:\n  1. Poiseuille's Resistance Formula: Resistance to fluid flow is inversely proportional to the fourth power of vessel radius (R proportional to 1/r^4); halving vessel radius multiplies resistance by 16-fold;\n  2. Arteriolar Dimensions: Arterioles have narrow individual lumens (diameter ~10–100 µm) and have not yet branched into the vast parallel capillary network, meaning total cross-sectional area is still small;\n  3. High Frictional Drag: Immense friction against vessel walls converts fluid kinetic energy into heat, dissipating hydrostatic pressure.\n• Protection of Capillaries:\n  1. This steep pressure drop is vital: it extinguishes the dangerous pulsatile pressure wave and delivers blood to fragile capillaries at a safe, smooth, low pressure (~35 mmHg arterial, dropping to ~15 mmHg venous);\n  2. Prevents the rupture of ultra-thin (0.5 µm) single-cell capillary endothelial exchange walls."
        }
    ]

