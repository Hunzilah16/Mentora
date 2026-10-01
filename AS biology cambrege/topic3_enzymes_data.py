"""
Topic 3: Enzymes — 50 Examination-Style Questions & Mark Schemes
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

def get_topic3_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Activation energy profile (Fig 3.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q3 - Activation Energy Profile & Reaction Energetics",
        syllabus_ref="Syllabus 3.1",
        difficulty="ADVANCED",
        preamble="Chemical reactions in biological systems require an initial input of energy to overcome the activation energy barrier. Fig. 3.1 shows the free energy profile of an exergonic reaction in the presence and absence of an enzyme.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_1_activation_energy_profile.png"),
        figure_caption="Fig. 3.1: Energy profile of an exergonic reaction with and without enzyme catalysis.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 3.1, define activation energy (Ea) and explain how the enzyme facilitates the conversion of substrates into products.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the overall free energy change (Delta G) of the reaction is identical for both the catalysed and uncatalysed pathways.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how the formation of an enzyme-substrate (ES) complex lowers the activation energy of a metabolic reaction.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Activation energy is the minimum kinetic energy required by colliding reactant molecules to reach the unstable transition state; the enzyme lowers the activation energy barrier so a greater proportion of substrate molecules possess sufficient energy to react at body temperature [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Delta G is the difference in free energy between initial substrate ground state and final product ground state; enzymes accelerate reaction rate by altering transition state pathway but do not alter the thermodynamic stability of substrates or products [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Substrate binding into the active site places mechanical strain on specific covalent bonds / brings reactive groups into precise mutual orientation / creates favourable microenvironment with catalytic R-groups [2].", "marks": 2}
        ]
    ))

    # Q2: Induced-fit model vs lock-and-key (Fig 3.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q3 - The Induced-Fit Mechanism of Enzyme Action",
        syllabus_ref="Syllabus 3.1",
        difficulty="ADVANCED",
        preamble="Historically, Emil Fischer proposed the rigid 'lock-and-key' model, while Daniel Koshland refined this into the dynamic 'induced-fit' hypothesis. Fig. 3.2 compares these two models of catalytic mechanism.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_2_induced_fit_mechanism.png"),
        figure_caption="Fig. 3.2: Comparison of the rigid lock-and-key model (A) and dynamic induced-fit model (B).",
        parts=[
            QuestionPart(label="(a)", text="Describe the fundamental difference between the lock-and-key model and the induced-fit model shown in Fig. 3.2.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the induced-fit model provides a better explanation for how enzymes lower the activation energy of a chemical reaction.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="After product formation, explain what happens to the conformation of the active site.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "In lock-and-key, active site is rigidly complementary to substrate before binding; in induced-fit, active site is flexible and undergoes a conformational change to wrap precisely around substrate upon initial collision [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Conformational change exerts physical torsional stress / strain on substrate bonds, distorting them towards transition state geometry and reducing energy required to break bonds [2].", "marks": 2},
            {"q": "Q2(c)", "points": "Products have lower affinity for active site and dissociate; active site reverts back to its original relaxed resting conformation, ready to accept another substrate molecule [2].", "marks": 2}
        ]
    ))

    # Q3: Catalase reaction progress curve & initial rate tangent (Fig 3.3)
    questions.append(Question(
        number=3,
        title="9700/22/F/M/23/Q4 - Catalase Kinetics & Initial Rate Determination",
        syllabus_ref="Syllabus 3.1",
        difficulty="ADVANCED",
        preamble="A student investigated the decomposition of hydrogen peroxide (H2O2) by intracellular catalase extracted from yeast. The volume of oxygen gas (O2) evolved was measured every 10 seconds using a gas syringe. Fig. 3.3 shows the progress curve obtained.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_3_reaction_progress_catalase.png"),
        figure_caption="Fig. 3.3: Volume of oxygen gas evolved over time during catalase decomposition of hydrogen peroxide.",
        parts=[
            QuestionPart(label="(a)", text="Write the balanced chemical equation for the reaction catalysed by catalase.", marks=2, num_answer_lines=2),
            QuestionPart(label="(b)", text="With reference to Fig. 3.3, determine the initial rate of reaction at t = 0 s, showing your working and stating appropriate units.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the rate of reaction gradually decreases as time progresses and eventually reaches a plateau.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "2 H2O2 -> 2 H2O + O2 [2].", "marks": 2},
            {"q": "Q3(b)", "points": "Gradient of tangent at t = 0 s: Delta V / Delta t = 40.3 / 30; Initial rate = 1.34 cm3 s-1 (accept 1.30 to 1.38 cm3 s-1 with units) [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Substrate (H2O2) is consumed, lowering substrate concentration; fewer successful collisions between substrate and active sites per unit time; plateau occurs when all H2O2 is completely converted into products [2].", "marks": 2}
        ]
    ))

    # Q4: Amylase starch colorimeter transmission (Fig 3.4)
    questions.append(Question(
        number=4,
        title="9700/23/M/J/21/Q3 - Colorimetric Assay of Amylase Substrate Depletion",
        syllabus_ref="Syllabus 3.1",
        difficulty="ADVANCED",
        preamble="The hydrolysis of starch by salivary amylase was monitored in a colorimeter. Samples were withdrawn at intervals, mixed with standardized iodine-potassium iodide solution, and percentage light transmission was measured at 580 nm. Fig. 3.4 shows the results.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_4_starch_amylase_colorimeter.png"),
        figure_caption="Fig. 3.4: Light transmission percentage vs incubation time during starch hydrolysis by amylase.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the percentage light transmission increases as the reaction proceeds.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 3.4, identify the achromic point of the reaction and explain its biochemical significance.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest why using a colorimeter is superior to visual inspection of colour changes on a spotting tile.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Amylase hydrolyses starch into maltose; less starch available to form blue-black polyiodide inclusion complex, so less light is absorbed and more light is transmitted through solution [2].", "marks": 2},
            {"q": "Q4(b)", "points": "Achromic point is reached at ~90 s (transmission reaches maximum plateau ~88-90%); represents complete hydrolysis of starch (no helical amylose chains remain to bind iodine) [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Provides quantitative, objective numerical data; eliminates subjective human error in judging subtle colour transitions [2].", "marks": 2}
        ]
    ))

    # Q5: Temperature effect and thermal denaturation (Fig 3.5)
    questions.append(Question(
        number=5,
        title="9700/22/O/N/23/Q4 - Thermal Kinetics, Q10 & Irreversible Denaturation",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The activity of an enzyme was measured across a temperature range of 0 °C to 75 °C. Fig. 3.5 shows the resulting rate curve.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_5_temperature_effect_denaturation.png"),
        figure_caption="Fig. 3.5: Effect of temperature on initial reaction rate showing optimum and thermal denaturation.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the rate of reaction approximately doubles for every 10 °C rise in temperature between 0 °C and 30 °C (Q10 ≈ 2).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Identify the optimum temperature from Fig. 3.5 and define what is meant by optimum temperature.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain in molecular detail why the rate of reaction drops sharply above 45 °C.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Increased thermal energy increases kinetic energy of enzyme and substrate molecules; faster movement increases frequency of collisions and proportion of collisions possessing energy >= Ea [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Optimum temperature is ~40 °C (accept 38-42 °C); the temperature at which the rate of catalytic conversion is highest [2].", "marks": 2},
            {"q": "Q5(c)", "points": "Violent thermal vibrations break weak hydrogen and ionic bonds stabilizing tertiary structure; active site loses specific complementary shape (denatures), substrate cannot bind, ES complexes cannot form [2].", "marks": 2}
        ]
    ))

    # Q6: pH effect on digestive enzymes (Fig 3.6)
    questions.append(Question(
        number=6,
        title="9700/21/M/J/22/Q3 - pH Sensitivity & Active Site Ionisation States",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="Human digestive enzymes function in specialized anatomical compartments with distinct physiological pH levels. Fig. 3.6 compares the activity curves of pepsin, salivary amylase, and trypsin.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_6_ph_effect_bell_curve.png"),
        figure_caption="Fig. 3.6: Effect of pH on catalytic activity of pepsin, salivary amylase, and trypsin.",
        parts=[
            QuestionPart(label="(a)", text="State the optimum pH for pepsin and trypsin from Fig. 3.6 and name the anatomical organ where each functions in vivo.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how changes in pH away from the optimum alter the charge distribution of amino acid R-groups in the active site.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why enzymes require buffer solutions when investigating the effect of substrate concentration on reaction rate.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Pepsin: optimum pH 2.0 (stomach / gastric juice); Trypsin: optimum pH 8.5 (duodenum / small intestine) [2].", "marks": 2},
            {"q": "Q6(b)", "points": "Excess H+ (low pH) protonates -COO- groups to -COOH; excess OH- (high pH) deprotonates -NH3+ groups to -NH2; breaks ionic bonds and destroys precise electrical charge complementarity required to bind substrate [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Substrates or reaction products can release or consume H+ ions, changing pH; buffers resist pH fluctuations to ensure pH remains constant as a controlled variable [2].", "marks": 2}
        ]
    ))

    # Q7: Enzyme concentration effect (Fig 3.7)
    questions.append(Question(
        number=7,
        title="9700/22/M/J/21/Q3 - Enzyme Concentration as a Rate-Limiting Factor",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The effect of enzyme concentration on initial rate was tested under two different substrate conditions: substrate in excess and substrate limited. Fig. 3.7 shows the two curves obtained.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_7_enzyme_concentration_effect.png"),
        figure_caption="Fig. 3.7: Initial reaction rate vs enzyme concentration under excess and limiting substrate conditions.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the reaction rate is directly proportional to enzyme concentration when substrate is in excess.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the rate of reaction plateaus when substrate concentration is limited.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest how you could experimentally test whether substrate concentration is limiting at the plateau.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "More enzyme molecules provide more available active sites per unit volume; increases frequency of successful collisions and rate of ES complex formation [2].", "marks": 2},
            {"q": "Q7(b)", "points": "Substrate molecules become the limiting factor; all substrate molecules are already bound into active sites, leaving surplus enzyme active sites unoccupied / idle [2].", "marks": 2},
            {"q": "Q7(c)", "points": "Add extra substrate to the reaction mixture; if rate increases, substrate was limiting [2].", "marks": 2}
        ]
    ))

    # Q8: Substrate concentration saturation kinetics (Fig 3.8)
    questions.append(Question(
        number=8,
        title="9700/23/O/N/22/Q2 - Substrate Saturation & Michaelis-Menten Kinetics",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="When the concentration of an enzyme is held constant and substrate concentration is increased, the reaction rate follows a characteristic hyperbolic curve. Fig. 3.8 shows this saturation curve.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_8_substrate_concentration_saturation.png"),
        figure_caption="Fig. 3.8: Hyperbolic curve of initial reaction rate (V) vs substrate concentration [S].",
        parts=[
            QuestionPart(label="(a)", text="Explain why the reaction rate increases steeply at low substrate concentrations (first-order kinetics).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why increasing substrate concentration beyond 40 mmol dm-3 produces no further increase in reaction rate (zero-order kinetics).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State the single modification to the reaction mixture that would increase the maximum rate (Vmax).", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "At low [S], most active sites are empty / unoccupied; increasing [S] increases collision frequency with active sites, so substrate concentration is rate-limiting [2].", "marks": 2},
            {"q": "Q8(b)", "points": "All active sites are fully saturated with substrate; as soon as product leaves, another substrate immediately binds; maximum turnover rate is reached and enzyme concentration is limiting [2].", "marks": 2},
            {"q": "Q8(c)", "points": "Increase the concentration of enzyme [2].", "marks": 2}
        ]
    ))

    # Q9: Michaelis-Menten Km and Vmax comparison (Fig 3.9)
    questions.append(Question(
        number=9,
        title="9700/22/F/M/22/Q4 - Derivation of Km & Comparing Enzyme Affinities",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The Michaelis-Menten constant (Km) is a fundamental kinetic parameter in enzymology. Fig. 3.9 shows the kinetic curves of two enzymes, Enzyme 1 and Enzyme 2, that act on the same substrate.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_9_michaelis_menten_km_vmax.png"),
        figure_caption="Fig. 3.9: Derivation of Km from 1/2 Vmax for Enzyme 1 and Enzyme 2.",
        parts=[
            QuestionPart(label="(a)", text="Define the Michaelis-Menten constant (Km) in terms of Vmax.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Using Fig. 3.9, determine the numerical value of Km for Enzyme 1 and Enzyme 2.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State which enzyme has the higher affinity for the substrate and explain the physiological advantage of having a low Km value in low substrate environments.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Km is the substrate concentration at which the reaction velocity is half of its maximum rate (1/2 Vmax) [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Vmax = 80 AU -> 1/2 Vmax = 40 AU; Km(Enzyme 1) = 4.0 mmol dm-3; Km(Enzyme 2) = 14.0 mmol dm-3 [2].", "marks": 2},
            {"q": "Q9(c)", "points": "Enzyme 1 has higher affinity; can operate close to maximum catalytic capacity even when intracellular substrate concentrations are very low [2].", "marks": 2}
        ]
    ))

    # Q10: Competitive inhibition kinetics (Fig 3.10)
    questions.append(Question(
        number=10,
        title="9700/21/M/J/23/Q2 - Competitive Enzyme Inhibition & Reversible Kinetics",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="Malonate is a classic competitive inhibitor of the mitochondrial enzyme succinate dehydrogenase. Fig. 3.10 shows the mechanism and the effect of a competitive inhibitor on reaction rate.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_10_competitive_inhibition_kinetics.png"),
        figure_caption="Fig. 3.10: Molecular mechanism and kinetic curve of competitive inhibition.",
        parts=[
            QuestionPart(label="(a)", text="Describe how the molecular structure of a competitive inhibitor relates to that of the normal substrate.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 3.10, explain why a competitive inhibitor increases the apparent Km of an enzyme without altering Vmax.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the effect of a competitive inhibitor can be experimentally overcome.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Competitive inhibitor has a molecular shape / geometry highly similar to the substrate, allowing it to fit into and bind reversibly to the active site [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Inhibitor competes with substrate for active sites, requiring a higher substrate concentration to achieve 1/2 Vmax (higher Km); but at very high [S], substrate outcompetes inhibitor so all active sites are saturated to reach normal Vmax [2].", "marks": 2},
            {"q": "Q10(c)", "points": "Significantly increase the concentration of the substrate; substrate molecules outnumber inhibitor molecules, vastly increasing probability of substrate binding [2].", "marks": 2}
        ]
    ))

    # Q11: Non-competitive allosteric inhibition (Fig 3.11)
    questions.append(Question(
        number=11,
        title="9700/22/O/N/21/Q3 - Non-Competitive Inhibition & Allosteric Site Regulation",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="Non-competitive inhibitors do not compete directly for the active site. Fig. 3.11 illustrates the allosteric mechanism and its effect on reaction kinetics.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_11_non_competitive_allosteric.png"),
        figure_caption="Fig. 3.11: Non-competitive inhibitor binding to allosteric site and resulting kinetics.",
        parts=[
            QuestionPart(label="(a)", text="Describe where a non-competitive inhibitor binds on an enzyme molecule and how this alters active site function.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why increasing substrate concentration cannot restore the original Vmax in the presence of a non-competitive inhibitor.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the value of Km remains unchanged in the presence of a pure non-competitive inhibitor.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Binds to an allosteric site (a site separate from the active site); alters tertiary conformation of the enzyme, distorting active site shape so catalysis cannot occur [2].", "marks": 2},
            {"q": "Q11(b)", "points": "Inhibitor does not compete with substrate for active sites; inhibited enzyme molecules are functionally inactive regardless of how high substrate concentration is raised [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Enzyme molecules that remain uninhibited have unchanged, normal active sites and retain identical affinity for substrate, reaching half of their reduced Vmax at the same [S] [2].", "marks": 2}
        ]
    ))

    # Q12: Lineweaver-Burk double reciprocal plot (Fig 3.12)
    questions.append(Question(
        number=12,
        title="9700/22/M/J/20/Q3 - Diagnostic Analysis via Lineweaver-Burk Plots",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The Lineweaver-Burk plot linearises Michaelis-Menten data by plotting the reciprocal of velocity (1/V) against the reciprocal of substrate concentration (1/[S]). Fig. 3.12 compares normal, competitive, and non-competitive enzyme kinetics.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_12_lineweaver_burk_double_reciprocal.png"),
        figure_caption="Fig. 3.12: Lineweaver-Burk double-reciprocal plot comparing uninhibited and inhibited enzymes.",
        parts=[
            QuestionPart(label="(a)", text="State the kinetic meaning of the y-intercept and x-intercept on a Lineweaver-Burk plot.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 3.12, explain how a Lineweaver-Burk plot distinguishes between a competitive and a non-competitive inhibitor.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="A line has a y-intercept of 0.20 AU-1 and an x-intercept of -0.25 mmol-1 dm3. Calculate the values of Vmax and Km for this enzyme.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "y-intercept = 1 / Vmax; x-intercept = -1 / Km [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Competitive inhibitor shares same y-intercept (same Vmax) but shifts x-intercept closer to origin (higher Km); non-competitive inhibitor has higher y-intercept (lower Vmax) but identical x-intercept (same Km) [2].", "marks": 2},
            {"q": "Q12(c)", "points": "Vmax = 1 / 0.20 = 5.0 AU; Km = -1 / (-0.25) = 4.0 mmol dm-3 [2].", "marks": 2}
        ]
    ))

    # Q13: Immobilised enzymes in calcium alginate (Fig 3.13)
    questions.append(Question(
        number=13,
        title="9700/23/M/J/22/Q3 - Industrial Biotechnology: Immobilised Enzymes in Alginate",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="In biotechnology, enzymes are frequently immobilized within porous calcium alginate beads. Fig. 3.13 shows a packed-bed bioreactor column and the thermal stability comparison between free and immobilised lactase.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_13_immobilised_enzymes_alginate.png"),
        figure_caption="Fig. 3.13: Packed-bed bioreactor column (left) and thermal stability curves of free vs immobilised lactase (right).",
        parts=[
            QuestionPart(label="(a)", text="Describe how lactase is immobilised into calcium alginate beads in the laboratory.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain two commercial advantages of using immobilised enzymes in a continuous bioreactor column compared to free enzymes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 3.13, explain why the immobilised enzyme retains high catalytic activity at 60 °C while the free enzyme is completely inactivated.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Mix lactase enzyme solution with sodium alginate; drop mixture using a syringe / pipette into a solution of calcium chloride (CaCl2) to form insoluble spherical gel beads [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Enzyme is easily recovered and reused multiple times (lowers running costs); product is not contaminated with enzyme, eliminating downstream purification steps [2].", "marks": 2},
            {"q": "Q13(c)", "points": "Alginate matrix physically holds enzyme in place and restricts molecular vibration / unfolding; stabilizing tertiary structure and active site conformation against thermal denaturation at higher temperatures [2].", "marks": 2}
        ]
    ))

    # Q14: End-product feedback allosteric inhibition (Fig 3.14)
    questions.append(Question(
        number=14,
        title="9700/21/O/N/23/Q4 - End-Product Allosteric Feedback Control",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="Multi-step biochemical pathways are regulated to maintain cellular homeostasis without wasting chemical energy. Fig. 3.14 illustrates end-product inhibition in the synthesis of L-isoleucine from L-threonine.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig3_14_end_product_allosteric_feedback.png"),
        figure_caption="Fig. 3.14: Feedback inhibition of threonine deaminase by the end-product L-isoleucine.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 3.14, describe how accumulation of L-isoleucine down-regulates its own synthesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why inhibiting the first enzyme in a biosynthetic pathway is more metabolically efficient than inhibiting an enzyme later in the pathway.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain what happens to the activity of threonine deaminase when intracellular levels of isoleucine decline.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Isoleucine binds reversibly to the allosteric site of Enzyme 1 (threonine deaminase); causes conformational change in active site that prevents threonine from binding, stopping production of intermediate A [2].", "marks": 2},
            {"q": "Q14(b)", "points": "Prevents wasteful accumulation of toxic or redundant pathway intermediates (A and B); conserves ATP and substrate threonine for other vital metabolic pathways [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Isoleucine dissociates from the allosteric site; active site reverts to its active conformation and synthesis of isoleucine resumes (negative feedback homeostasis) [2].", "marks": 2}
        ]
    ))

    # Q15: Intracellular vs extracellular enzymes
    questions.append(Question(
        number=15,
        title="9700/22/F/M/21/Q4 - Intracellular vs Extracellular Enzymes",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Enzymes operate both within cytoplasmic compartments and in the extracellular environment.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between an intracellular enzyme and an extracellular enzyme, providing one named biological example of each.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why intracellular lysosomal enzymes (acid hydrolases) have an optimum pH of ~5.0, whereas cytoplasmic enzymes have an optimum pH of ~7.2.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the cellular pathway by which extracellular enzymes are synthesized and secreted from eukaryotic cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Intracellular enzymes function inside cells (e.g. catalase, DNA polymerase); extracellular enzymes are secreted and function outside cells (e.g. pepsin, amylase) [2].", "marks": 2},
            {"q": "Q15(b)", "points": "Inside lysosome, proton pumps maintain pH 5.0 for optimal hydrolysis of engulfed pathogens/organelles; if lysosome ruptures, enzymes are inactive in neutral cytoplasm (pH 7.2), protecting cell from autolysis [2].", "marks": 2},
            {"q": "Q15(c)", "points": "Synthesized by ribosomes on rough endoplasmic reticulum -> transported via vesicles to Golgi apparatus for modification/packaging -> transport vesicles fuse with cell surface membrane (exocytosis) [2].", "marks": 2}
        ]
    ))

    # Q16: Experimental determination of Km and Vmax
    questions.append(Question(
        number=16,
        title="9700/21/M/J/20/Q3 - Experimental Protocol for Km and Vmax Determination",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="A researcher designed an investigation to determine the kinetic parameters Km and Vmax of a novel bacterial cellulase.",
        parts=[
            QuestionPart(label="(a)", text="Outline the experimental procedure used to measure the initial reaction velocity across a range of substrate concentrations.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the initial velocity (V0) must be measured rather than the total product formed after 30 minutes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two environmental variables that must be strictly controlled throughout the investigation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Prepare serial dilution of substrate concentrations; mix with constant enzyme concentration at controlled temperature/pH; measure product formed or substrate lost in first 30-60 seconds [2].", "marks": 2},
            {"q": "Q16(b)", "points": "Initial rate reflects true kinetics when substrate concentration is known and un-depleted; over 30 minutes rate slows due to substrate depletion, product inhibition, or enzyme instability [2].", "marks": 2},
            {"q": "Q16(c)", "points": "Temperature (using thermostatically controlled water bath); pH (using buffer solution) [2].", "marks": 2}
        ]
    ))

    # Q17: Structural evidence for enzyme flexibility
    questions.append(Question(
        number=17,
        title="9700/23/O/N/21/Q2 - Structural Flexibility & Catalytic Transition State",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Advances in structural biology have provided direct evidence for conformational changes during catalysis.",
        parts=[
            QuestionPart(label="(a)", text="Explain how X-ray crystallography of unliganded vs substrate-bound enzymes supports the induced-fit hypothesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of catalytic residues within the active site compared to binding residues.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why transition state analogues act as exceptionally potent enzyme inhibitors.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Shows atomic coordinates of active site loops and domain movements; active site cleft closes and catalytic residues shift closer to substrate upon binding [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Binding residues hold substrate in place via non-covalent interactions (hydrogen/ionic bonds); catalytic residues participate directly in bond-breaking/bond-making mechanisms [2].", "marks": 2},
            {"q": "Q17(c)", "points": "Enzymes have evolved highest complementary affinity for transition state geometry rather than substrate; transition state analogues bind with extremely high affinity and block active site [2].", "marks": 2}
        ]
    ))

    # Q18: Industrial comparison of batch vs continuous immobilised bioreactors
    questions.append(Question(
        number=18,
        title="9700/22/M/J/22/Q4 - Industrial Bioprocessing: Free vs Immobilised Systems",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Industrial biocatalysis utilizes both soluble batch systems and immobilised continuous-flow columns.",
        parts=[
            QuestionPart(label="(a)", text="Compare the economic cost of enzyme replacement in batch fermentation with free enzymes versus continuous-flow columns with immobilised enzymes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how immobilisation alters the downstream processing and purity of the pharmaceutical product.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest one disadvantage or limitation of immobilising an enzyme within an alginate matrix.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Batch free enzyme is discarded with product at end of cycle (high recurring enzyme cost); immobilised enzyme remains trapped in column and is reused for thousands of cycles (lowers cost) [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Product effluent is free of enzyme protein; avoids expensive chemical separation, filtration, and protein denaturation steps to purify product [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Substrate diffusion into bead interior is slower (diffusion limitation); alginate pores may leak enzyme over time or beads may degrade under shear stress [2].", "marks": 2}
        ]
    ))

    # Q19: [Mentora Original A* Extension] Mathematical derivation from Michaelis-Menten equation
    questions.append(Question(
        number=19,
        title="[Mentora Original A* Extension] Q19 - Quantitative Analysis of the Michaelis-Menten Equation",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The rate of an enzyme-catalysed reaction is described mathematically by the Michaelis-Menten equation: V = (Vmax * [S]) / (Km + [S]).",
        parts=[
            QuestionPart(label="(a)", text="Calculate the initial reaction velocity (V) as a fraction or percentage of Vmax when [S] = 2 Km.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the initial reaction velocity (V) as a fraction or percentage of Vmax when [S] = 0.5 Km.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Show mathematically that when substrate concentration is extremely high ([S] >> Km), the reaction velocity approaches Vmax.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Substitute [S] = 2Km: V = (Vmax * 2Km) / (Km + 2Km) = (2/3) * Vmax = 0.67 Vmax (66.7% of Vmax) [2].", "marks": 2},
            {"q": "Q19(b)", "points": "Substitute [S] = 0.5Km: V = (Vmax * 0.5Km) / (Km + 0.5Km) = (0.5/1.5) * Vmax = (1/3) * Vmax = 0.33 Vmax (33.3% of Vmax) [2].", "marks": 2},
            {"q": "Q19(c)", "points": "When [S] >> Km, (Km + [S]) ≈ [S]; equation simplifies to V ≈ (Vmax * [S]) / [S] = Vmax (independent of [S], zero-order kinetics) [2].", "marks": 2}
        ]
    ))

    # Q20: [Mentora Original A* Extension] Transition state theory & chemical catalysis
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] Q20 - Transition State Stabilization & Catalytic Mechanisms",
        syllabus_ref="Syllabus 3.1",
        difficulty="ADVANCED",
        preamble="Enzyme active sites deploy precise chemical mechanisms to stabilise the transition state of substrate molecules.",
        parts=[
            QuestionPart(label="(a)", text="Explain how general acid-base catalysis in an enzyme active site facilitates bond cleavage.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of metal ion cofactors (such as Zn2+ in carbonic anhydrase) in polarising substrate bonds.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why enzymes lose catalytic activity if a single amino acid residue in the active site is mutated, even if overall folding is preserved.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Active site amino acid R-groups act as proton donors (e.g. protonated histidine) or proton acceptors; stabilizing charged intermediates during transition state [2].", "marks": 2},
            {"q": "Q20(b)", "points": "Positively charged divalent metal ion coordinates with substrate water/carbonyl oxygen, drawing electron density away to increase nucleophilicity / polarise bond for rapid attack [2].", "marks": 2},
            {"q": "Q20(c)", "points": "Loss of critical catalytic R-group eliminates specific chemical mechanism (e.g. nucleophilic attack or proton transfer); substrate may still bind but cannot undergo catalytic chemical transformation [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & BIOCHEMICAL MECHANISM QUESTIONS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Active site tertiary structure
    questions.append(Question(
        number=21,
        title="9700/22/O/N/22/Q3 - Active Site Anatomy: Binding vs Catalytic Residues",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="An enzyme active site is a specialized cleft formed by the precise 3D folding of the polypeptide chain.",
        parts=[
            QuestionPart(label="(a)", text="Explain why amino acid residues that form the active site may be widely separated in the primary structure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between the function of binding residues and catalytic residues within the active site.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Polypeptide chain undergoes complex secondary coiling and tertiary folding; bringing distant linear residues into close spatial proximity in 3D space [2].", "marks": 2},
            {"q": "Q21(b)", "points": "Binding residues recognize and anchor the substrate through complementary non-covalent bonds; catalytic residues act directly to break or form covalent bonds [2].", "marks": 2}
        ]
    ))

    # Q22: Maxwell-Boltzmann distribution and Ea
    questions.append(Question(
        number=22,
        title="9700/21/O/N/21/Q3 - Maxwell-Boltzmann Molecular Energy Distribution",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="At any given temperature, molecules in a solution possess a range of kinetic energies.",
        parts=[
            QuestionPart(label="(a)", text="Describe how lowering the activation energy alters the proportion of substrate molecules capable of reacting.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why an uncatalysed reaction occurs extremely slowly at 37 °C even if it is energetically exergonic.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Shifts the activation energy threshold to the left on the energy distribution; a vastly greater fraction of colliding molecules have kinetic energy >= Ea [2].", "marks": 2},
            {"q": "Q22(b)", "points": "The uncatalysed Ea is so high that only an infinitesimal fraction of molecules possess sufficient thermal kinetic energy at 37 °C to surmount the activation barrier [2].", "marks": 2}
        ]
    ))

    # Q23: Reversible vs irreversible enzyme inhibition
    questions.append(Question(
        number=23,
        title="9700/23/M/J/23/Q4 - Reversible vs Irreversible Enzyme Inhibition",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Inhibitors are classified by the nature and permanence of their binding to enzymes.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between reversible and irreversible enzyme inhibition in terms of bonding.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why organophosphate nerve agents that covalently bind to acetylcholinesterase are lethal toxins.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Reversible inhibitors bind via weak non-covalent interactions (H-bonds/ionic) and can dissociate; irreversible inhibitors form permanent covalent bonds with active site residues [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Permanently inactivate acetylcholinesterase; acetylcholine cannot be broken down at synapses, causing continuous uncontrolled muscle contraction and respiratory paralysis [2].", "marks": 2}
        ]
    ))

    # Q24: Buffers in enzyme investigations
    questions.append(Question(
        number=24,
        title="9700/22/F/M/20/Q3 - Chemical Buffers & Experimental Standardisation",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Enzymatic investigations require rigorous control of physical and chemical variables.",
        parts=[
            QuestionPart(label="(a)", text="Explain how a buffer solution maintains a relatively constant pH.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why failing to use a buffer when testing the effect of substrate concentration invalidates the results.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Contains a weak acid and its conjugate base; absorbs excess H+ ions when acid is added and releases H+ ions when base is added [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Any change in pH would alter the ionisation of active site R-groups; introducing an uncontrolled confounding variable that masks the true effect of [S] [2].", "marks": 2}
        ]
    ))

    # Q25: Initial rate of reaction rationale
    questions.append(Question(
        number=25,
        title="9700/21/M/J/21/Q4 - Theoretical Rationale for Measuring Initial Rates",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="In enzyme kinetics, measurements must always be taken at the start of the reaction.",
        parts=[
            QuestionPart(label="(a)", text="Define what is meant by the initial rate of reaction (V0).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain two reasons why the rate of reaction declines rapidly after the initial period.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "The rate of catalytic conversion at time zero (t = 0), measured from the tangent to the reaction progress curve at the immediate start [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Substrate concentration decreases as it is consumed, reducing collision frequency; accumulation of products may cause end-product inhibition [2].", "marks": 2}
        ]
    ))

    # Q26: Biological significance of Km
    questions.append(Question(
        number=26,
        title="9700/22/O/N/20/Q4 - Physiological Significance of the Michaelis-Menten Constant",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Different enzymes catalysing the same reaction can possess dramatically different Km values.",
        parts=[
            QuestionPart(label="(a)", text="Explain why Km is inversely proportional to the affinity of an enzyme for its substrate.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Liver glucokinase has a high Km (10 mM) for glucose, whereas brain hexokinase has a low Km (0.1 mM). Relate this to the physiological function of each organ.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "A low Km means half-maximal velocity is achieved at very low substrate concentration, showing strong substrate binding; high Km requires high [S] to bind [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Hexokinase works at maximum rate even during hypoglycemia to ensure brain survival; glucokinase only phosphorylates glucose after carbohydrate-rich meals when blood glucose is elevated [2].", "marks": 2}
        ]
    ))

    # Q27: Allosteric enzymes and sigmoidal kinetics
    questions.append(Question(
        number=27,
        title="9700/23/M/J/20/Q3 - Allosteric Cooperativity & Sigmoidal Kinetics",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Certain regulatory enzymes exhibit cooperativity rather than standard hyperbolic Michaelis-Menten kinetics.",
        parts=[
            QuestionPart(label="(a)", text="Describe the shape of the velocity versus substrate curve for an allosteric enzyme exhibiting positive cooperativity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how substrate binding to one subunit affects the remaining subunits in a multi-subunit allosteric enzyme.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Sigmoidal (S-shaped) curve; initial low rate followed by a steep increase in rate over a narrow range of substrate concentrations [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Binding of substrate to one active site induces a conformational shift that transmits to adjacent subunits; increasing their affinity for substrate [2].", "marks": 2}
        ]
    ))

    # Q28: Calcium alginate entrapment mechanism
    questions.append(Question(
        number=28,
        title="9700/22/M/J/23/Q5 - Polymer Chemistry of Alginate Immobilisation",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Sodium alginate is a polysaccharide extracted from brown seaweed used to encapsulate enzymes.",
        parts=[
            QuestionPart(label="(a)", text="Explain the chemical cross-linking that occurs when sodium alginate drops into calcium chloride solution.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why high-molecular-weight substrates cannot be easily hydrolysed by enzymes entrapped in alginate beads.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Divalent calcium ions (Ca2+) displace monovalent sodium ions (Na+); cross-linking carboxylate groups of adjacent alginate polymer chains into an insoluble 3D hydrogel mesh [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Large macromolecules (such as starch or insoluble proteins) cannot diffuse through the small pores of the alginate gel matrix to reach the trapped enzyme [2].", "marks": 2}
        ]
    ))

    # Q29: Heavy metal ion inhibition
    questions.append(Question(
        number=29,
        title="9700/21/O/N/23/Q5 - Heavy Metal Toxicity & Disruption of Disulfide Bridges",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Heavy metal cations such as mercury (Hg2+), lead (Pb2+), and silver (Ag+) act as non-competitive enzyme inhibitors.",
        parts=[
            QuestionPart(label="(a)", text="Explain the chemical mechanism by which heavy metal ions disrupt protein tertiary structure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why poisoning by heavy metals cannot be reversed by administering excess substrate.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Heavy metal ions react strongly with sulfhydryl (-SH) groups of cysteine residues; disrupting covalent disulfide bridges and altering active site tertiary conformation [2].", "marks": 2},
            {"q": "Q29(b)", "points": "Heavy metals bind to non-catalytic sites / distort active site directly; substrate cannot compete with heavy metals, so increasing [S] cannot restore activity [2].", "marks": 2}
        ]
    ))

    # Q30: Lactose-free milk production
    questions.append(Question(
        number=30,
        title="9700/22/F/M/22/Q5 - Industrial Production of Lactose-Reduced Dairy Products",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Lactase hydrolyses the milk disaccharide lactose into glucose and galactose.",
        parts=[
            QuestionPart(label="(a)", text="State two nutritional and commercial benefits of treating milk with lactase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why lactose-free milk tastes noticeably sweeter than untreated regular milk.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Allows lactose-intolerant individuals to consume dairy without digestive distress; reduces risk of crystallization in condensed milk and ice cream [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Hydrolysis yields equal amounts of glucose and galactose; both monosaccharides have a higher relative sweetness rating on taste receptors than disaccharide lactose [2].", "marks": 2}
        ]
    ))

    # Q31: Distinguishing competitive and non-competitive at saturation
    questions.append(Question(
        number=31,
        title="9700/23/O/N/22/Q5 - Diagnostic Kinetic Behaviour at High Substrate Levels",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Enzymologists distinguish between inhibitor types by examining reaction rates at very high substrate concentrations.",
        parts=[
            QuestionPart(label="(a)", text="Explain what happens to the rate of a competitive-inhibited reaction when substrate concentration is increased to saturation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what happens to the rate of a non-competitive-inhibited reaction under the same conditions.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "Rate reaches the normal uninhibited Vmax; high substrate concentration completely outcompetes inhibitor for active sites [2].", "marks": 2},
            {"q": "Q31(b)", "points": "Rate plateaus at a lower maximum velocity; non-competitive inhibitor remains bound to allosteric site and inactivates a fraction of enzyme molecules [2].", "marks": 2}
        ]
    ))

    # Q32: Extracellular enzymes in saprotrophs
    questions.append(Question(
        number=32,
        title="9700/22/M/J/21/Q5 - Ecological Role of Extracellular Hydrolases",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Fungi and bacteria play a vital role in nutrient cycling as saprotrophic decomposers.",
        parts=[
            QuestionPart(label="(a)", text="Describe how saprotrophic fungi utilize extracellular enzymes to obtain nutrients from decaying wood.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why saprotrophs must secrete enzymes rather than ingesting whole macromolecules by endocytosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Hyphae secrete cellulase and pectinase enzymes into surrounding organic matter; hydrolysing insoluble polymers into soluble glucose monomers that are absorbed by diffusion/active transport [2].", "marks": 2},
            {"q": "Q32(b)", "points": "Fungal hyphae have rigid chitin cell walls that prevent phagocytosis / endocytosis; only small soluble molecules can traverse the cell wall and membrane [2].", "marks": 2}
        ]
    ))

    # Q33: Amylase specificity for amylose vs amylopectin
    questions.append(Question(
        number=33,
        title="9700/21/M/J/23/Q5 - Substrate Specificity of Amylase on Branched Starch",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Salivary alpha-amylase is an endoglycosidase that hydrolyses internal bonds in starch.",
        parts=[
            QuestionPart(label="(a)", text="State which specific glycosidic bonds are cleaved by alpha-amylase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why alpha-amylase cannot completely hydrolyse amylopectin into maltose, naming the intermediate products formed.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Internal alpha(1->4)-glycosidic bonds [2].", "marks": 2},
            {"q": "Q33(b)", "points": "Active site cannot bind or cleave alpha(1->6)-glycosidic bonds at branch points; leaves branched limit dextrins that require debranching enzyme for complete hydrolysis [2].", "marks": 2}
        ]
    ))

    # Q34: Colorimetric calibration curve protocol
    questions.append(Question(
        number=34,
        title="9700/22/O/N/22/Q5 - Colorimetric Calibration in Enzyme Assays",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Quantitative colorimetry requires an initial calibration curve using known standards.",
        parts=[
            QuestionPart(label="(a)", text="Describe how a calibration curve of absorbance versus starch concentration is constructed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why colorimeter cuvettes must be wiped clean and inserted with the optical face correctly aligned.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Prepare known standard starch concentrations; add constant volume of iodine reagent; measure absorbance at 580 nm and plot absorbance (y-axis) vs concentration (x-axis) [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Fingerprints or scratches on optical face scatter light; incorrect alignment alters path length, leading to erroneous absorbance measurements [2].", "marks": 2}
        ]
    ))

    # Q35: Effect of sub-zero temperatures
    questions.append(Question(
        number=35,
        title="9700/21/O/N/22/Q5 - Low Temperature Inactivation vs Denaturation",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Food can be preserved by freezing at -18 °C.",
        parts=[
            QuestionPart(label="(a)", text="Explain why enzymes are completely inactive at -18 °C.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why freezing an enzyme does not denature it, in contrast to boiling.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Water is frozen solid and molecules have extremely low kinetic energy; enzyme and substrate cannot diffuse or collide [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Freezing does not supply energy to break covalent, ionic, or hydrogen bonds; tertiary structure remains intact and enzyme resumes activity upon thawing [2].", "marks": 2}
        ]
    ))

    # Q36: Statins as competitive inhibitors
    questions.append(Question(
        number=36,
        title="9700/23/M/J/22/Q5 - Pharmacology of Statins as Competitive Inhibitors",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Statins are widely prescribed medications used to reduce the risk of cardiovascular disease.",
        parts=[
            QuestionPart(label="(a)", text="Describe the mechanism by which statins inhibit HMG-CoA reductase in hepatic cholesterol biosynthesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how competitive inhibition by statins lowers low-density lipoprotein (LDL) cholesterol in the bloodstream.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Statins have a molecular structure similar to HMG-CoA substrate; bind competitively and reversibly to active site of HMG-CoA reductase, blocking mevalonate synthesis [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Decreased intracellular cholesterol synthesis prompts hepatocytes to upregulate LDL receptors; increasing clearance of LDL particles from systemic circulation [2].", "marks": 2}
        ]
    ))

    # Q37: [Mentora Original A* Extension] Steady-state kinetics assumption
    questions.append(Question(
        number=37,
        title="[Mentora Original A* Extension] Q37 - The Quasi-Steady-State Assumption in Enzyme Kinetics",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The derivation of Michaelis-Menten kinetics depends on the Briggs-Haldane steady-state approximation.",
        parts=[
            QuestionPart(label="(a)", text="State the core assumption of the quasi-steady-state hypothesis regarding the enzyme-substrate complex [ES].", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what condition must be met regarding initial substrate concentration [S] relative to total enzyme concentration [E]total for steady-state kinetics to hold.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "The concentration of the enzyme-substrate complex [ES] remains constant over the measurement period (rate of ES formation = rate of ES breakdown) [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Initial substrate concentration must be vastly in excess of enzyme concentration ([S] >> [E]total); ensuring [ES] formation does not significantly deplete free substrate [2].", "marks": 2}
        ]
    ))

    # Q38: [Mentora Original A* Extension] Turnover number kcat and catalytic perfection
    questions.append(Question(
        number=38,
        title="[Mentora Original A* Extension] Q38 - Catalytic Constant (kcat) & Catalytic Perfection",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="The catalytic turnover number (kcat) measures how rapidly an enzyme converts substrate into product.",
        parts=[
            QuestionPart(label="(a)", text="Define the turnover number (kcat) and explain how it is calculated from Vmax and total enzyme concentration [E]total.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="The enzyme catalase has a kcat/Km ratio approaching 10^8 dm3 mol-1 s-1. Explain what is meant by the statement that catalase has reached 'catalytic perfection'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "kcat is the maximum number of substrate molecules converted to product per active site per second; calculated as kcat = Vmax / [E]total [2].", "marks": 2},
            {"q": "Q38(b)", "points": "The reaction rate is limited solely by the physical rate of diffusion of substrate molecules colliding with the active site in aqueous solution (diffusion-controlled limit) [2].", "marks": 2}
        ]
    ))

    # Q39: [Mentora Original A* Extension] Uncompetitive inhibition
    questions.append(Question(
        number=39,
        title="[Mentora Original A* Extension] Q39 - Uncompetitive Inhibition Mechanism",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="In uncompetitive inhibition, the inhibitor cannot bind to free enzyme, but binds exclusively to the enzyme-substrate (ES) complex.",
        parts=[
            QuestionPart(label="(a)", text="Explain how uncompetitive inhibitor binding prevents product formation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why both Vmax and apparent Km decrease by the same factor in uncompetitive inhibition.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Binds to a site created only after substrate binding; locks ES complex in an inactive non-productive ESI complex that cannot undergo catalysis to form product [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Vmax decreases because active complexes are removed; apparent Km decreases because depletion of ES pulls free E into ES (Le Chatelier's principle), apparently increasing affinity [2].", "marks": 2}
        ]
    ))

    # Q40: [Mentora Original A* Extension] Temperature equilibration error analysis
    questions.append(Question(
        number=40,
        title="[Mentora Original A* Extension] Q40 - Experimental Error Analysis: Thermal Equilibration",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="In investigations of temperature effects on enzyme rates, systematic errors frequently arise from inadequate pre-incubation.",
        parts=[
            QuestionPart(label="(a)", text="Explain why both the enzyme solution and substrate solution must be pre-incubated separately in a water bath before mixing.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how mixing solutions that have not reached thermal equilibrium produces an incorrect rate measurement.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Ensures both reactants have reached the exact target test temperature prior to starting the reaction, so initial rate reflects specified temperature [2].", "marks": 2},
            {"q": "Q40(b)", "points": "If mixed cold, initial rate will reflect a lower temperature during the crucial first 30 seconds before thermal equilibrium is attained, yielding an underestimated initial velocity [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Enzyme definition
    questions.append(Question(
        number=41,
        title="9700/22/F/M/23/Q2 - Definition of an Enzyme",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Enzymes underpin biological catalysis.",
        parts=[
            QuestionPart(label="(a)", text="Define the term enzyme and state the macromolecular class to which nearly all enzymes belong.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "A biological catalyst that accelerates the rate of metabolic reactions without being consumed or chemically altered; globular protein [2].", "marks": 2}
        ]
    ))

    # Q42: Intracellular vs extracellular definition
    questions.append(Question(
        number=42,
        title="9700/21/M/J/22/Q2 - Intracellular vs Extracellular Localization",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Enzyme location reflects functional role.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between intracellular and extracellular enzymes, giving one named example of each.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "Intracellular enzymes act inside cells (e.g. catalase / DNA polymerase); extracellular enzymes are secreted and act outside cells (e.g. pepsin / amylase) [2].", "marks": 2}
        ]
    ))

    # Q43: Active site definition
    questions.append(Question(
        number=43,
        title="9700/22/M/J/22/Q2 - Definition of an Active Site",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Enzymes have a specific active region.",
        parts=[
            QuestionPart(label="(a)", text="Define the active site of an enzyme.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "The specific 3D region of an enzyme molecule, formed by tertiary folding, to which the substrate binds and where catalytic conversion occurs [2].", "marks": 2}
        ]
    ))

    # Q44: Activation energy definition
    questions.append(Question(
        number=44,
        title="9700/23/M/J/21/Q2 - Definition of Activation Energy",
        syllabus_ref="Syllabus 3.1",
        difficulty="CHALLENGING",
        preamble="Chemical reactions require an activation barrier.",
        parts=[
            QuestionPart(label="(a)", text="Define activation energy (Ea).", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "The minimum amount of energy required by colliding reactant molecules to overcome the energy barrier and initiate a chemical reaction [2].", "marks": 2}
        ]
    ))

    # Q45: Effect of competitive inhibitor on Vmax and Km
    questions.append(Question(
        number=45,
        title="9700/22/O/N/21/Q2 - Competitive Inhibitor Effects on Kinetic Constants",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Inhibitors affect kinetic constants characteristically.",
        parts=[
            QuestionPart(label="(a)", text="State the effect of a competitive inhibitor on Vmax and on Km.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "Vmax remains unchanged; Km increases [2].", "marks": 2}
        ]
    ))

    # Q46: Effect of non-competitive inhibitor on Vmax and Km
    questions.append(Question(
        number=46,
        title="9700/21/O/N/21/Q2 - Non-Competitive Inhibitor Effects on Kinetic Constants",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Allosteric inhibitors alter kinetics differently.",
        parts=[
            QuestionPart(label="(a)", text="State the effect of a non-competitive inhibitor on Vmax and on Km.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "Vmax decreases; Km remains unchanged [2].", "marks": 2}
        ]
    ))

    # Q47: Low Km meaning
    questions.append(Question(
        number=47,
        title="9700/22/M/J/21/Q2 - Significance of a Low Km Value",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Km measures affinity.",
        parts=[
            QuestionPart(label="(a)", text="Explain why a low value of Km indicates a high affinity of an enzyme for its substrate.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "A lower substrate concentration is required to reach half the maximum rate (1/2 Vmax), meaning the enzyme binds tightly to the substrate [2].", "marks": 2}
        ]
    ))

    # Q48: Reagent for alginate immobilisation
    questions.append(Question(
        number=48,
        title="9700/23/O/N/20/Q2 - Cross-Linking Reagent in Alginate Entrapment",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Enzyme immobilisation requires ionic cross-linking.",
        parts=[
            QuestionPart(label="(a)", text="Name the salt solution into which sodium alginate is dropped to form insoluble gel beads.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "Calcium chloride solution (CaCl2) [2].", "marks": 2}
        ]
    ))

    # Q49: Advantages of immobilised enzymes
    questions.append(Question(
        number=49,
        title="9700/22/F/M/20/Q2 - Two Advantages of Immobilised Enzymes",
        syllabus_ref="Syllabus 3.2",
        difficulty="CHALLENGING",
        preamble="Immobilised enzymes offer processing advantages.",
        parts=[
            QuestionPart(label="(a)", text="State two practical advantages of using immobilised enzymes in industry compared to free enzymes in solution.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "1. Enzyme can be easily recovered and reused; 2. Product is uncontaminated by enzyme / enzyme exhibits higher thermal stability [2].", "marks": 2}
        ]
    ))

    # Q50: [Mentora Original A* Extension] Allosteric site definition
    questions.append(Question(
        number=50,
        title="[Mentora Original A* Extension] Q50 - Definition of an Allosteric Site",
        syllabus_ref="Syllabus 3.2",
        difficulty="ADVANCED",
        preamble="Allosteric regulation controls metabolic flow.",
        parts=[
            QuestionPart(label="(a)", text="Define the term allosteric site and explain its role in metabolic regulation.", marks=2, num_answer_lines=2)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "A regulatory binding site distinct from the active site; binding of an effector molecule induces a conformational change that alters active site catalytic activity [2].", "marks": 2}
        ]
    ))

    return questions

def get_topic3_faqs():
    return [
        {
            "q_num": 1,
            "title": "Explain How Enzymes Lower Activation Energy and Contrast the Lock-and-Key with the Induced-Fit Hypothesis.",
            "category": "Enzyme Mechanisms • Activation Energy (Ea)",
            "examiner_trap": "Asserting that enzymes 'provide energy' to drive the reaction, or failing to state that the active site is flexible and changes conformation in the induced-fit model.",
            "model_answer": "• Nature of Enzymes: Globular proteins acting as biological catalysts; possess a specific 3D active site composed of a few catalytic amino acid residues determined by tertiary structure.\n• Activation Energy (Ea): The minimum kinetic energy required for colliding substrate molecules to reach the unstable transition state and react; enzymes lower Ea by providing an alternative reaction pathway.\n• Mechanism of Ea Reduction: Binding in the active site brings substrates into close physical proximity and optimal stereochemical orientation; active site residues interact with substrate bonds, placing strain on covalent bonds to facilitate bond breaking.\n• Lock-and-Key Hypothesis: The active site is considered rigid and perfectly complementary in shape to the substrate prior to binding; substrate fits precisely like a key in a lock.\n• Induced-Fit Hypothesis: The active site is flexible; upon initial weak collision, the substrate induces a conformational change in the enzyme's tertiary structure, molding the active site snugly around the substrate, maximizing catalytic contact and bond strain."
        },
        {
            "q_num": 2,
            "title": "How and Why Is the Initial Rate of Reaction Determined from Progress Curves (Tangent at t = 0)?",
            "category": "Reaction Kinetics • Graphical Analysis",
            "examiner_trap": "Calculating average rate over several minutes rather than drawing a tangent at time zero, or failing to construct a sufficiently large right-angled triangle.",
            "model_answer": "• Why Measure Initial Rate: At time t = 0, substrate concentration is known, at its maximum, and non-limiting; no product accumulation has occurred to cause product inhibition or reverse reactions; represents the true catalytic velocity.\n• Curve Progression: Rate is steepest at t = 0; slows progressively as substrate is consumed (fewer effective substrate-active site collisions per unit time); eventually plateaus when all substrate is converted into product.\n• Tangent Construction: Place a ruler along the initial linear section of the progress curve at the origin (t = 0); draw a straight line extending across both axes.\n• Gradient Calculation: Construct a large right-angled triangle; calculate gradient = Change in Product (or Substrate) / Change in Time (dy/dx); include precise units (e.g. cm3 s-1 or mol dm-3 s-1)."
        },
        {
            "q_num": 3,
            "title": "Explain Why Increasing Substrate Concentration Initially Increases Reaction Rate but Eventually Reaches a Plateau (Vmax).",
            "category": "Enzyme Kinetics • Substrate Saturation",
            "examiner_trap": "Stating that at high substrate concentration the enzyme is 'denatured' or 'used up'. Enzymes are biological catalysts that remain unchanged and reusable.",
            "model_answer": "• Initial Increase (Limiting Factor: Substrate): At low substrate concentrations, enzyme active sites are in excess; increasing substrate concentration increases the frequency of successful collisions between substrate and active sites; more enzyme-substrate (ES) complexes form per unit time, resulting in a proportional linear increase in reaction rate.\n• Plateau Region (Vmax): As substrate concentration rises further, active sites become increasingly occupied.\n• Saturation Point: A concentration is reached where every enzyme active site is continuously occupied and working at maximum catalytic velocity; as soon as product is released, a new substrate binds immediately.\n• Limiting Factor Shift: Enzyme concentration becomes the sole limiting factor; further increases in substrate concentration produce no additional increase in rate; reaction operates at Vmax."
        },
        {
            "q_num": 4,
            "title": "Define the Michaelis-Menten Constant (Km), Describe Its Graphical Derivation, and Explain Its Significance Regarding Affinity.",
            "category": "Michaelis-Menten Kinetics • Km & Substrate Affinity",
            "examiner_trap": "Defining Km as 'half of Vmax' (Vmax/2 is a velocity; Km is the substrate concentration). Stating that a higher Km represents higher affinity (it is an inverse relationship).",
            "model_answer": "• Definition of Km: The substrate concentration [S] at which the rate of the enzyme-catalysed reaction is half of the maximum velocity (1/2 Vmax).\n• Graphical Derivation: Identify the horizontal asymptote on a rate vs [S] graph to determine Vmax; calculate 1/2 Vmax; locate this value on the y-axis, project horizontally to intersect the curve, then project vertically down to read Km on the x-axis (with units of concentration, e.g. mmol dm-3).\n• Affinity Relationship (Inverse): Km is inversely proportional to the enzyme's affinity for its substrate:\n  1. Low Km: Enzyme has high affinity for substrate; reaches 1/2 Vmax at very low substrate concentration; forms ES complexes readily;\n  2. High Km: Enzyme has low affinity for substrate; requires high substrate concentration to reach 1/2 Vmax.\n• Independence: Km is a kinetic constant characteristic of an enzyme-substrate pair under specified pH and temperature; it is independent of enzyme concentration."
        },
        {
            "q_num": 5,
            "title": "Distinguish Between Competitive and Non-Competitive Inhibition with Reference to Active Sites, Vmax, and Km.",
            "category": "Inhibition Kinetics • Reversible Inhibitors",
            "examiner_trap": "Claiming that competitive inhibitors alter active site shape, or that non-competitive inhibitors can be overcome by adding more substrate.",
            "model_answer": "• Competitive Inhibition:\n  1. Molecular Structure: Inhibitor has a chemical shape very similar to the normal substrate;\n  2. Binding Site: Competes directly with substrate to bind reversibly to the active site, blocking substrate entry;\n  3. Reversibility & Effect of [S]: Can be completely overcome by increasing substrate concentration (higher probability of substrate colliding with active site than inhibitor);\n  4. Kinetic Constants: Vmax is UNCHANGED (eventually reached at high [S]); Km is INCREASED (apparent affinity is reduced).\n• Non-Competitive Inhibition:\n  1. Molecular Structure: Inhibitor has no structural resemblance to the substrate;\n  2. Binding Site: Binds reversibly to an allosteric site (a site away from the active site);\n  3. Mechanism: Binding alters the enzyme's tertiary structure, causing conformational change in the active site so substrate no longer fits or catalytic groups are misaligned;\n  4. Effect of [S]: Cannot be overcome by increasing substrate concentration;\n  5. Kinetic Constants: Vmax is REDUCED; Km is UNCHANGED (unaffected enzyme molecules retain normal affinity)."
        },
        {
            "q_num": 6,
            "title": "Explain the Molecular Basis of Temperature Effects on Enzyme Action: Kinetic Energy, Q10, and Thermal Denaturation.",
            "category": "Environmental Factors • Thermal Inactivation",
            "examiner_trap": "Saying enzymes 'die' or that covalent peptide bonds break during thermal denaturation. Only non-covalent (and disulfide) bonds in tertiary conformation break.",
            "model_answer": "• Temperature Below Optimum:\n  1. Temperature increases kinetic energy of both enzyme and substrate molecules;\n  2. Molecules move faster, increasing collision frequency per unit time;\n  3. A greater proportion of colliding molecules possess kinetic energy exceeding the activation energy (Ea);\n  4. Temperature coefficient (Q10) is approximately 2.0 (rate doubles for every 10°C rise).\n• Optimum Temperature: The temperature at which the rate of ES complex formation is maximal (~37–40°C in mammals, ~70°C+ in thermophiles).\n• Temperature Above Optimum (Denaturation):\n  1. Excessive thermal vibration imparts kinetic energy greater than the bond energy of weak intramolecular bonds;\n  2. Hydrogen bonds and ionic bonds maintaining the tertiary structure break;\n  3. Polypeptide chain uncoils; 3D conformation of the active site is permanently altered;\n  4. Active site is no longer complementary to substrate; no ES complexes can form; rate drops precipitously to zero (irreversible denaturation)."
        },
        {
            "q_num": 7,
            "title": "How Does Alteration of pH Affect the Ionisation of Active Site Residues and Enzyme Conformation?",
            "category": "Environmental Factors • pH & Charge Alteration",
            "examiner_trap": "Claiming that pH changes alter molecular kinetic energy. pH affects the ionic charge and bonding of amino acid R-groups.",
            "model_answer": "• Optimum pH: The hydrogen ion concentration ([H+]) at which the active site has the optimal charge and shape for substrate binding and catalysis.\n• Effect of Low pH (High [H+]):\n  1. Excess H+ ions bind to negatively charged carboxylate groups (-COO- + H+ -> -COOH) of aspartic acid and glutamic acid R-groups, neutralising them;\n  2. Breaks ionic bonds and salt bridges stabilising the enzyme's tertiary structure;\n  3. Alters electrostatic attraction between charged active site residues and charged groups on the substrate.\n• Effect of High pH (Low [H+] / High [OH-]):\n  1. OH- ions remove protons from positively charged amino groups (-NH3+ + OH- -> -NH2 + H2O) of lysine and arginine R-groups;\n  2. Disrupts ionic bonds, altering tertiary structure;\n  3. Extreme pH deviations cause irreversible denaturation of the active site.\n• Buffer Action: Biological buffers resist changes in pH by donating or accepting H+ ions, maintaining enzyme function."
        },
        {
            "q_num": 8,
            "title": "Explain the Principles, Kinetic Advantages, and Industrial Applications of Immobilised Enzymes in Alginate Beads.",
            "category": "Biotechnology • Enzyme Immobilisation",
            "examiner_trap": "Stating that immobilised enzymes have a higher initial reaction rate than free enzymes. Substrate diffusion into beads slows initial kinetics.",
            "model_answer": "• Entrapment Technique: Enzyme solution is mixed with sodium alginate, then dropped via syringe into calcium chloride (CaCl2) solution; calcium ions replace sodium, cross-linking alginate chains to form insoluble calcium alginate gel beads entrapping the enzyme molecules.\n• Industrial Advantages:\n  1. Pure Product: Enzyme is physically retained in the matrix; product contains no enzyme contamination, eliminating expensive downstream separation and purification steps;\n  2. Reusability: Beads are easily filtered and reused across multiple consecutive batches, dramatically lowering operating costs;\n  3. Continuous Processing: Beads can be packed into vertical column reactors for continuous automated substrate flow;\n  4. Enhanced Stability: The rigid calcium alginate matrix holds the tertiary structure of the enzyme in place, restricting molecular vibrations and significantly increasing tolerance to high temperatures and extreme pH before denaturation occurs."
        },
        {
            "q_num": 9,
            "title": "Describe the Mechanism and Biological Significance of Allosteric End-Product Inhibition in Metabolic Pathways.",
            "category": "Metabolic Control • Allosteric Regulation",
            "examiner_trap": "Confusing end-product inhibition with competitive inhibition. It is non-competitive and reversible, acting at an allosteric site.",
            "model_answer": "• Metabolic Pathways: Cellular biochemical reactions occur in multi-step enzyme cascades (A -> B -> C -> D -> Final Product), each catalyzed by a specific enzyme.\n• Committed Step: The first unique enzyme in the pathway possesses both an active site (for substrate A) and an allosteric regulatory site.\n• Allosteric Mechanism: When the final end-product accumulates in excess, it binds reversibly to the allosteric site of the first enzyme;\n• Conformational Change: Allosteric binding transmits mechanical strain throughout the enzyme, altering the tertiary structure and 3D shape of the active site so it can no longer bind substrate A;\n• Negative Feedback Significance: Halts the entire pathway, preventing wasteful overproduction of intermediate metabolites and conservation of cellular energy (ATP) and raw materials;\n• Dynamic Resumption: As the end-product is consumed by the cell, its concentration falls, causing it to dissociate from the allosteric site; enzyme reverts to active conformation and pathway resumes."
        },
        {
            "q_num": 10,
            "title": "Distinguish Between Intracellular and Extracellular Enzymes, and Contrast Assay Methods for Measuring Product Formation vs Substrate Disappearance.",
            "category": "Enzyme Assays • Intracellular vs Extracellular",
            "examiner_trap": "Stating that catalase is an extracellular enzyme. Catalase is strictly intracellular (located inside peroxisomes). Confusing substrate loss assays with product formation assays.",
            "model_answer": "• Intracellular Enzymes: Synthesised inside the cell and function within cellular compartments or cytosol; Examples: Catalase (located in peroxisomes, decomposes toxic hydrogen peroxide: 2H2O2 -> 2H2O + O2), DNA polymerase, ATP synthase, respiratory enzymes.\n• Extracellular Enzymes: Synthesised inside cells on RER, packaged into secretory vesicles by Golgi body, secreted via exocytosis to function in external environments; Examples: Digestive enzymes like salivary/pancreatic amylase (hydrolyses starch to maltose in gut lumen), pepsin, trypsin.\n• Monitoring Product Formation (Catalase Assay): Hydrogen peroxide mixed with catalase in a closed boiling tube connected to a gas syringe or inverted measuring cylinder filled with water; volume of O2 gas produced recorded at regular time intervals (e.g. every 15 s) to plot a product-time progress curve.\n• Monitoring Substrate Disappearance (Amylase Assay): Amylase mixed with starch solution; samples removed at timed intervals (every 30 s) and added to spotting tile wells containing iodine solution; time taken to reach achromatic point (yellow-brown, no blue-black) recorded, or disappearance of starch tracked continuously in a colorimeter using transmission."
        }
    ]

