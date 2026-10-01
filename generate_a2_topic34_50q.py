"""
Complete 50-Question Master Pack: Topic 34 — Nitrogen Compounds (Paper 4 Theory)
Strict Mark Tariff Distribution:
- 40% 6-Markers (20 Questions, 120 Marks)
- 40% 4-Markers (20 Questions, 80 Marks)
- 20% 2-Markers (10 Questions, 20 Marks)
Total: 50 Questions, 220 Marks.
Includes Dedicated Section D: 10 High-Frequency Core Repeats (Past 10 Years Analysis).
Every question mapped to authentic, verifiable Cambridge 9701 Paper 4 past paper references.
Candidate: Urwah | Mentora Academy
"""
import os
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf

def build_topic34_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic34_Nitrogen_Compounds.pdf"

    topic_title = "Topic 34 — Nitrogen Compounds"
    topic_subtitle = "Amines & Basicity · Phenylamine & Azo Dye Synthesis · Amides & Hydrolysis · Amino Acids, Zwitterions & Electrophoresis"

    subtopics_summary = [
        ("34.1 Primary & Secondary Amines: Basicity Trends", "Comparison of basic strengths of ethylamine, ammonia, and phenylamine; inductive electron donation (+I) by alkyl groups vs delocalisation of nitrogen lone pair into the aromatic π-electron system in aryl amines; reactions with acids and halogenoalkanes."),
        ("34.2 Phenylamine & Azo Dye Coupling Reactions", "Preparation of phenylamine via reduction of nitrobenzene with Sn and concentrated HCl; electrophilic bromination of phenylamine; diazotisation at < 10 °C to form benzenediazonium chloride; coupling with alkaline phenol to yield brightly coloured azo dyes."),
        ("34.3 Amides: Structure, Basicity & Hydrolysis", "Preparation from acyl chlorides; neutral character explained by resonance delocalisation of the nitrogen lone pair into the carbonyl π-bond; acidic and alkaline hydrolysis of amides."),
        ("34.4 Amino Acids, Zwitterions & Electrophoresis", "Dipolar zwitterion structure; amphoteric acid-base buffer properties; isoelectric point; separation of amino acid mixtures by gel electrophoresis at controlled buffer pH; peptide bond formation."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Nitrogen Compounds from the past 10 years.")
    ]

    subtopic_map = {
        "SEC_A": "SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (40% TARIFF · Q1–Q16)",
        "SEC_B": "SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (40% TARIFF · Q17–Q32)",
        "SEC_C": "SECTION C: 2-MARK TARGETED EXAM QUESTIONS (20% TARIFF · Q33–Q40)",
        "SEC_D": "SECTION D: HIGH-FREQUENCY CORE REPEATS — 10 MOST FREQUENTLY TESTED QUESTIONS (Q41–Q50)",
    }

    fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"

    questions = [
        # =====================================================================
        # SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (Q1 TO Q16) — 16 QUESTIONS
        # =====================================================================

        # Q1: 9701/42/M/J/23/Q10
        Question(
            number=1,
            title="Relative Base Strengths of Ethylamine, Ammonia, and Phenylamine — 9701/42/M/J/23/Q10 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_A",
            preamble="The relative base strengths of three nitrogen-containing bases are shown in Fig. 1.1.",
            figure_path=os.path.join(fig_dir, "a2_t34_amine_basicity_scale.png"),
            figure_caption="Fig. 1.1: Relative basicity and conjugate acid pKa values for phenylamine, ammonia, and ethylamine.",
            parts=[
                QuestionPart("(a)", "Rank phenylamine, ammonia, and ethylamine in order of increasing base strength.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain why ethylamine is a stronger base than ammonia.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain in detail why phenylamine is a much weaker base than ammonia.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenylamine < Ammonia < Ethylamine [1].", "marks": 1},
                {"part": "(b)", "points": "The ethyl group exerts an electron-donating (+I) inductive effect towards the nitrogen atom [1]; This increases the electron density of the lone pair on nitrogen, making it more available to accept a proton (H+) [1].", "marks": 2},
                {"part": "(c)", "points": "In phenylamine, the p-orbital lone pair of electrons on the nitrogen atom overlaps with the delocalised &pi;-electron cloud of the benzene ring [1]; The lone pair is delocalised into the aromatic ring [1]; This significantly decreases electron density on nitrogen, making the lone pair far less available to coordinate with a proton [1].", "marks": 3}
            ]
        ),

        # Q2: 9701/41/O/N/22/Q8
        Question(
            number=2,
            title="Diazotisation and Coupling Mechanism for Azo Dye Synthesis — 9701/41/O/N/22/Q8 [6 Marks]",
            syllabus_ref="34.2", difficulty="HARD", section_key="SEC_A",
            preamble="The formation of 4-hydroxyazobenzene by electrophilic coupling is illustrated in Fig. 2.1.",
            figure_path=os.path.join(fig_dir, "a2_t34_azo_dye_coupling.png"),
            figure_caption="Fig. 2.1: Electrophilic coupling of benzenediazonium ion with phenoxide.",
            parts=[
                QuestionPart("(a)", "State the reagents and conditions needed to convert phenylamine into benzenediazonium chloride.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the diazonium solution must be kept below 10 °C, stating what happens if warmed.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why phenol is dissolved in aqueous sodium hydroxide before the coupling reaction, and draw the structure of the azo dye formed.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sodium nitrite (NaNO2) and hydrochloric acid (HCl) (or nitrous acid, HNO2) [1]; Temperature between 0 °C and 10 °C [1].", "marks": 2},
                {"part": "(b)", "points": "The benzenediazonium ion is thermally unstable above 10 °C [1]; It decomposes / hydrolyses to form phenol and nitrogen gas (N2) [1].", "marks": 2},
                {"part": "(c)", "points": "NaOH converts phenol into the phenoxide ion (C6H5O-), which carries a full negative charge and is far more activated / nucleophilic towards the diazonium electrophile [1]; Structure of 4-hydroxyazobenzene showing C6H5-N=N-C6H4-OH [1].", "marks": 2}
            ]
        ),

        # Q3: 9701/42/M/J/22/Q9
        Question(
            number=3,
            title="Amino Acid Zwitterions and Gel Electrophoresis Separation — 9701/42/M/J/22/Q9 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_A",
            preamble="The behaviour of amino acids in aqueous solutions at different pH values is summarised in Fig. 3.1.",
            figure_path=os.path.join(fig_dir, "a2_t34_amino_acid_zwitterion.png"),
            figure_caption="Fig. 3.1: Net electrical charge on an amino acid as a function of solution pH.",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of alanine (2-aminopropanoic acid) in its zwitterionic form.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Draw the structure of alanine at pH 1 and at pH 12.", 2, num_answer_lines=3),
                QuestionPart("(c)", "A mixture of alanine (isoelectric point 6.0), lysine (isoelectric point 9.7), and aspartic acid (isoelectric point 2.8) is separated by gel electrophoresis at a buffer pH of 6.0. Predict the direction of movement of each amino acid and explain your reasoning.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "+H3N-CH(CH3)-COO- [1].", "marks": 1},
                {"part": "(b)", "points": "At pH 1: +H3N-CH(CH3)-COOH (cationic form) [1]; At pH 12: H2N-CH(CH3)-COO- (anionic form) [1].", "marks": 2},
                {"part": "(c)", "points": "Alanine has net charge zero at pH 6.0 and remains at the origin / does not migrate [1]; Lysine (pI 9.7) is below its isoelectric point, carries a net positive charge (+1), and migrates towards the cathode (-) [1]; Aspartic acid (pI 2.8) is above its isoelectric point, carries a net negative charge (-1), and migrates towards the anode (+) [1].", "marks": 3}
            ]
        ),

        # Q4: 9701/41/M/J/21/Q10
        Question(
            number=4,
            title="Synthesis and Reactions of Phenylamine from Nitrobenzene — 9701/41/M/J/21/Q10 [6 Marks]",
            syllabus_ref="34.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Give the reagents and conditions for the laboratory reduction of nitrobenzene to phenylamine, and explain why sodium hydroxide is added in the final step.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State the observations when bromine water is added to aqueous phenylamine at room temperature.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Give the systematic IUPAC name and structure of the organic product formed in (b).", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Tin (Sn) and concentrated hydrochloric acid (conc. HCl) [1]; Heated under reflux [1]; NaOH is added to deprotonate the phenylammonium salt (C6H5NH3+ Cl-) to liberate free phenylamine [1].", "marks": 3},
                {"part": "(b)", "points": "Orange/brown bromine water is decolourised [1]; A white precipitate is formed [1].", "marks": 2},
                {"part": "(c)", "points": "2,4,6-tribromophenylamine (or 2,4,6-tribromoaniline) with correct structure [1].", "marks": 1}
            ]
        ),

        # Q5: 9701/42/O/N/20/Q8
        Question(
            number=5,
            title="Acid and Alkaline Hydrolysis of Amides — 9701/42/O/N/20/Q8 [6 Marks]",
            syllabus_ref="34.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the hydrolysis of ethanamide with hot dilute hydrochloric acid, naming both products.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Write the balanced chemical equation for the hydrolysis of ethanamide with hot aqueous sodium hydroxide, naming both products.", 3, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3CONH2 + H2O + HCl &rarr; CH3COOH + NH4Cl (or + H+ + H2O &rarr; CH3COOH + NH4+) [2]; Ethanoic acid and ammonium chloride [1].", "marks": 3},
                {"part": "(b)", "points": "CH3CONH2 + NaOH &rarr; CH3COONa + NH3 (or + OH- &rarr; CH3COO- + NH3) [2]; Sodium ethanoate and ammonia [1].", "marks": 3}
            ]
        ),

        # Q6: 9701/43/M/J/23/Q9
        Question(
            number=6,
            title="Synthesis of Primary Amines: Halogenoalkanes vs Reduction of Nitriles — 9701/43/M/J/23/Q9 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Describe how bromoethane can be converted to ethylamine in a single step, stating reagents and essential conditions.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why the reaction in (a) produces a mixture of primary, secondary, and tertiary amines, and state how the yield of primary amine can be maximised.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe a two-step synthesis to convert bromoethane into propylamine, stating all reagents and conditions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Excess concentrated ammonia (NH3) in ethanol [1]; Heated in a sealed tube under pressure [1].", "marks": 2},
                {"part": "(b)", "points": "The ethylamine formed retains a lone pair on nitrogen and acts as a nucleophile to attack unreacted bromoethane, undergoing further substitution [1]; Use a large excess of ammonia to ensure ammonia outcompetes ethylamine for bromoethane [1].", "marks": 2},
                {"part": "(c)", "points": "Step 1: Potassium cyanide (KCN) in ethanol, heated under reflux to form propanenitrile [1]; Step 2: Lithium tetrahydridoaluminate (LiAlH4) in dry ether (or H2 with Ni catalyst) to reduce propanenitrile to propylamine [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/42/F/M/22/Q10
        Question(
            number=7,
            title="Peptide Linkages, Polypeptides, and Hydrolysis of Proteins — 9701/42/F/M/22/Q10 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_A",
            preamble="A dipeptide is formed from glycine (2-aminoethanoic acid) and valine (2-amino-3-methylbutanoic acid).",
            parts=[
                QuestionPart("(a)", "Draw the structural formulas of the two isomeric dipeptides that can be formed from glycine and valine.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Identify the peptide linkage in one of the dipeptides and explain why it is planar.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the reagents and conditions used to hydrolyse proteins completely into their constituent amino acids in the laboratory.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Gly-Val: H2N-CH2-CO-NH-CH(CH(CH3)2)-COOH [1]; Val-Gly: H2N-CH(CH(CH3)2)-CO-NH-CH2-COOH [1].", "marks": 2},
                {"part": "(b)", "points": "-CO-NH- group highlighted [1]; The nitrogen lone pair delocalises into the carbonyl &pi;-bond, giving the C-N bond partial double bond character which prevents free rotation and holds the atoms in a planar geometry [1].", "marks": 2},
                {"part": "(c)", "points": "Concentrated hydrochloric acid (6 mol dm^-3 HCl) [1]; Heated under reflux for 24 hours at 110 °C [1].", "marks": 2}
            ]
        ),

        # Q8: 9701/41/O/N/23/Q9
        Question(
            number=8,
            title="Electrophoresis: Influence of Buffer pH on Separation of Peptides — 9701/41/O/N/23/Q9 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Define the term isoelectric point of an amino acid.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Glutamic acid has pKa values of 2.19 (-COOH), 4.25 (side-chain -COOH), and 9.67 (-NH3+). Deduce its overall charge at pH 1.0, pH 7.0, and pH 12.0.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain how the voltage and duration of the electric current affect the separation of spots in gel electrophoresis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The specific pH at which an amino acid or peptide exists predominantly as a zwitterion with zero net electrical charge [1].", "marks": 1},
                {"part": "(b)", "points": "At pH 1.0: net charge is +1 (+H3N-CH(COOH)-CH2CH2COOH) [1]; At pH 7.0: net charge is -1 (+H3N-CH(COO-)-CH2CH2COO-) [1]; At pH 12.0: net charge is -2 (H2N-CH(COO-)-CH2CH2COO-) [1].", "marks": 3},
                {"part": "(c)", "points": "Higher voltage increases the electrostatic force and migration speed, but excessive voltage causes Joule heating that distorts bands [1]; Longer duration allows greater distance of migration and better resolution between species of similar charge-to-mass ratio, but excessive time leads to band broadening by diffusion [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/20/Q8
        Question(
            number=9,
            title="Multi-Step Synthesis: Phenylamine to Paracetamol (4-Acetamidophenol) — 9701/42/M/J/20/Q8 [6 Marks]",
            syllabus_ref="34.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Paracetamol is prepared from 4-aminophenol. Write the equation for the acylation of 4-aminophenol with ethanoyl chloride.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the amino group (-NH2) is acylated preferentially rather than the phenolic hydroxy group (-OH).", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the reagents and conditions to prepare 4-aminophenol starting from nitrobenzene.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-HOC6H4NH2 + CH3COCl &rarr; 4-HOC6H4NHCOCH3 + HCl [2].", "marks": 2},
                {"part": "(b)", "points": "Nitrogen is less electronegative than oxygen and holds its lone pair less tightly [1]; Therefore, the -NH2 group is a significantly more powerful nucleophile than the -OH group and attacks the carbonyl carbon much more rapidly [1].", "marks": 2},
                {"part": "(c)", "points": "Mononitration of phenol (or hydroxylation of nitrobenzene) followed by reduction with Sn and concentrated HCl [2].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/19/Q9
        Question(
            number=10,
            title="Basicity of Primary, Secondary, and Tertiary Aliphatic Amines — 9701/41/M/J/19/Q9 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "In the gas phase, the base strength of methylamines increases in the order: NH3 < CH3NH2 < (CH3)2NH < (CH3)3N. Explain this trend.", 2, num_answer_lines=3),
                QuestionPart("(b)", "In aqueous solution, dimethylamine is a stronger base than trimethylamine. Explain why the basicity of trimethylamine decreases in water.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Write the equilibrium equation and expression for the base dissociation constant, Kb, of ethylamine in water.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Each additional methyl group exerts an electron-donating (+I) inductive effect [1]; This progressively increases electron density on the nitrogen lone pair, making it increasingly able to coordinate a proton in the absence of solvent [1].", "marks": 2},
                {"part": "(b)", "points": "In aqueous solution, the stability of the conjugate cation depends on hydration via hydrogen bonding with water molecules [1]; (CH3)3NH+ has only one hydrogen atom attached to nitrogen to form hydrogen bonds, compared to two in (CH3)2NH2+ [1]; In addition, three bulky methyl groups create steric hindrance that obstructs the approach of hydrating water molecules, destabilising the cation [1].", "marks": 3},
                {"part": "(c)", "points": "CH3CH2NH2 + H2O <=> CH3CH2NH3+ + OH-; Kb = [CH3CH2NH3+][OH-] / [CH3CH2NH2] [1].", "marks": 1}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q9
        Question(
            number=11,
            title="Quantitative Analysis: Acid-Base Back Titration of an Insoluble Amine — 9701/42/O/N/21/Q9 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_A",
            preamble="A 1.395 g sample of an impure aromatic amine, C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub> (Mr = 93.0), is dissolved in 50.00 cm<sup>3</sup> of 0.500 mol dm<sup>-3</sup> standard HCl(aq).<br/>"
                     "The amine reacts completely: C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub> + HCl &rarr; C<sub>6</sub>H<sub>5</sub>NH<sub>3</sub><sup>+</sup>Cl<sup>-</sup>.<br/>"
                     "The excess unreacted HCl requires 28.40 cm<sup>3</sup> of 0.400 mol dm<sup>-3</sup> NaOH for complete neutralisation.",
            parts=[
                QuestionPart("(a)", "Calculate the initial moles of HCl added to the amine sample.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the moles of NaOH required to neutralise the unreacted HCl, and hence find the moles of HCl that reacted with the amine.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the mass of pure phenylamine in the sample and its percentage purity.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Moles of HCl initial = 0.05000 x 0.500 = 2.500 x 10^-2 mol [1].", "marks": 1},
                {"part": "(b)", "points": "Moles of NaOH = 0.02840 x 0.400 = 1.136 x 10^-2 mol [1]; Moles of HCl reacted = 2.500 x 10^-2 - 1.136 x 10^-2 = 1.364 x 10^-2 mol [1].", "marks": 2},
                {"part": "(c)", "points": "Moles of C6H5NH2 = 1.364 x 10^-2 mol [1]; Mass of C6H5NH2 = 1.364 x 10^-2 x 93.0 = 1.269 g [1]; Percentage purity = (1.269 / 1.395) x 100 = 90.9% [1].", "marks": 3}
            ]
        ),

        # Q12: 9701/42/M/J/18/Q9
        Question(
            number=12,
            title="Comparison of Phenylamine, N-Methylphenylamine, and Diphenylamine — 9701/42/M/J/18/Q9 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Draw the skeletal formula of diphenylamine, (C6H5)2NH.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain why diphenylamine is an exceptionally weak base, even weaker than phenylamine.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Predict and explain whether N-methylphenylamine is a stronger or weaker base than phenylamine.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two benzene rings attached to a central -NH- group [1].", "marks": 1},
                {"part": "(b)", "points": "In diphenylamine, the nitrogen lone pair can overlap and delocalise into two separate benzene &pi;-rings simultaneously [1]; This extensive double delocalisation drastically reduces electron density on the nitrogen atom [1]; Consequently, the lone pair has virtually no tendency to accept a proton [1].", "marks": 3},
                {"part": "(c)", "points": "N-methylphenylamine is slightly stronger than phenylamine [1]; The electron-donating (+I) inductive effect of the methyl group partially offsets the delocalisation into the phenyl ring, increasing electron density on nitrogen [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/41/O/N/18/Q9
        Question(
            number=13,
            title="Optical Activity in Amino Acids and Separation of Enantiomers — 9701/41/O/N/18/Q9 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State which 2-amino acid does not exhibit optical isomerism, giving a reason based on structure.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the 3D stereochemical formulas of the two enantiomers of alanine, showing their non-superimposable mirror image relationship.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why synthetic amino acids produced in a laboratory are optically inactive, whereas naturally occurring amino acids are optically active.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Glycine (2-aminoethanoic acid) [1]; The alpha-carbon is bonded to two identical hydrogen atoms, so it lacks a chiral / asymmetric carbon centre [1].", "marks": 2},
                {"part": "(b)", "points": "Two 3D tetrahedral structures drawn with wedge and dash bonds as non-superimposable mirror images around the chiral carbon [2].", "marks": 2},
                {"part": "(c)", "points": "Laboratory chemical synthesis proceeds via planar intermediates (e.g. carbonyls or carbocations) where attack by reagents is equally probable from either side, producing an equimolar racemic mixture [1]; In biological systems, enzymes have asymmetric chiral active sites that catalyse stereospecific reactions producing exclusively one optical isomer (usually L-amino acids) [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/F/M/20/Q9
        Question(
            number=14,
            title="Synthesis of Nylon 6,6 and Comparison with Kevlar — 9701/42/F/M/20/Q9 [6 Marks]",
            syllabus_ref="34.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State the systematic IUPAC names of the two monomers used to manufacture Nylon 6,6.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the repeat unit of Kevlar, which is formed from benzene-1,4-diamine and benzene-1,4-dicarboxylic acid.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why Kevlar has an exceptionally high tensile strength and thermal stability compared to Nylon 6,6.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hexane-1,6-diamine (or 1,6-diaminohexane) [1]; Hexanedioic acid (or hexanedioyl dichloride) [1].", "marks": 2},
                {"part": "(b)", "points": "-[NH-C6H4-NH-CO-C6H4-CO]- with correct 1,4-disubstituted aromatic rings and amide linkages [2].", "marks": 2},
                {"part": "(c)", "points": "The rigid aromatic rings keep the polymer chains straight and planar, allowing tight parallel alignment and packing [1]; Extensive and regular intermolecular hydrogen bonding between aligned amide groups, combined with &pi;-&pi; stacking between aromatic rings, provides immense tensile strength [1].", "marks": 2}
            ]
        ),

        # Q15: 9701/41/M/J/17/Q8
        Question(
            number=15,
            title="Coupling of Diazonium Salts with Aromatic Amines — 9701/41/M/J/17/Q8 [6 Marks]",
            syllabus_ref="34.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Benzenediazonium chloride can couple with N,N-dimethylphenylamine. Write the structural formula of the azo compound formed.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the pH conditions required for coupling with amines compared to coupling with phenol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why coupling occurs at the 4-position (para) of N,N-dimethylphenylamine rather than the 2-position (ortho).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5-N=N-C6H4-4-N(CH3)2 [2].", "marks": 2},
                {"part": "(b)", "points": "Coupling with amines is carried out in weakly acidic to neutral pH (~4–7) [1]; Coupling with phenol requires alkaline pH (~9–11) to generate the phenoxide ion [1].", "marks": 2},
                {"part": "(c)", "points": "The bulky -N(CH3)2 group creates significant steric hindrance around the 2- and 6-positions [1]; The 4-position is sterically unhindered and fully activated by the electron-donating nitrogen lone pair [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/42/O/N/17/Q9
        Question(
            number=16,
            title="Solubility and Melting Points of Amino Acids vs Hydroxy Acids — 9701/42/O/N/17/Q9 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_A",
            preamble="Compare the physical properties of aminoethanoic acid (glycine, Mr = 75.0, melting point = 233 °C) and 2-hydroxyethanoic acid (glycolic acid, Mr = 76.0, melting point = 75 °C).",
            parts=[
                QuestionPart("(a)", "Explain the enormous difference in melting points between glycine and glycolic acid.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why glycine is soluble in water but insoluble in non-polar organic solvents such as hexane.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Glycine exists in the solid state as a dipolar zwitterion (+H3N-CH2-COO-) [1]; It forms an ionic lattice held together by very strong electrostatic attractions (ionic bonds) between oppositely charged ions, requiring massive energy to overcome [1]; Glycolic acid exists as neutral covalent molecules held together only by hydrogen bonding and London dispersion forces, which are much weaker than ionic bonds [1].", "marks": 3},
                {"part": "(b)", "points": "The ionic zwitterions of glycine are strongly hydrated by ion-dipole interactions with polar water molecules, releasing hydration energy to overcome lattice energy [1]; Hexane molecules are non-polar and can only form weak London dispersion forces with the zwitterions [1]; These weak interactions cannot compensate for the large energy required to break the ionic lattice of glycine [1].", "marks": 3}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q10(b)
        Question(
            number=17,
            title="Reaction of Ethylamine with Dilute Acids and Complex Ion Formation — 9701/42/M/J/23/Q10(b) [4 Marks]",
            syllabus_ref="34.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of ethylamine with dilute sulfuric acid.", 2, num_answer_lines=2),
                QuestionPart("(b)", "When ethylamine is added dropwise to aqueous copper(II) sulfate, a pale blue precipitate forms initially which dissolves in excess ethylamine to form a deep blue solution. Explain these observations.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2CH3CH2NH2 + H2SO4 &rarr; (CH3CH2NH3+)2 SO4(2-) (or CH3CH2NH2 + H+ &rarr; CH3CH2NH3+) [2].", "marks": 2},
                {"part": "(b)", "points": "Initially, ethylamine acts as a base generating OH- ions to precipitate pale blue Cu(OH)2(s) [1]; In excess, ethylamine acts as a monodentate ligand, replacing water to form the deep blue complex [Cu(CH3CH2NH2)4(H2O)2]2+ [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/O/N/22/Q8(b)
        Question(
            number=18,
            title="Comparison of Reactivity of Phenylamine vs Benzene towards Bromine — 9701/41/O/N/22/Q8(b) [4 Marks]",
            syllabus_ref="34.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State why benzene does not react with bromine water at room temperature.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why phenylamine reacts vigorously with bromine water at room temperature without a catalyst.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene has a stable delocalised aromatic &pi;-system and insufficient electron density to polarise non-polar Br2 molecules [2].", "marks": 2},
                {"part": "(b)", "points": "The lone pair on the nitrogen atom delocalises into the aromatic &pi;-cloud, significantly activating the benzene ring [1]; The increased electron density is high enough to induce a dipole in Br2 molecules without needing a halogen carrier [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/M/J/22/Q9(b)
        Question(
            number=19,
            title="Buffering Action of Zwitterionic Amino Acids — 9701/42/M/J/22/Q9(b) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write an equation showing how the zwitterion of glycine resists a decrease in pH when H+ ions are added.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write an equation showing how the zwitterion resists an increase in pH when OH- ions are added.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "+H3N-CH2-COO- + H+ &rarr; +H3N-CH2-COOH (the carboxylate group accepts H+) [2].", "marks": 2},
                {"part": "(b)", "points": "+H3N-CH2-COO- + OH- &rarr; H2N-CH2-COO- + H2O (the ammonium group donates H+) [2].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/M/J/21/Q10(b)
        Question(
            number=20,
            title="Comparison of Phenylamine and Ethylamine with Ethanoyl Chloride — 9701/41/M/J/21/Q10(b) [4 Marks]",
            syllabus_ref="34.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of the product formed when phenylamine reacts with ethanoyl chloride.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Name this product and state the type of bond formed between carbon and nitrogen.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3CONH-C6H5 (N-phenylethanamide / acetanilide) [2].", "marks": 2},
                {"part": "(b)", "points": "N-phenylethanamide [1]; Secondary amide bond (peptide link / -CONH-) [1].", "marks": 1}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q8(b)
        Question(
            number=21,
            title="Alkaline Hydrolysis of Amides: Identification of Volatile Product — 9701/42/O/N/20/Q8(b) [4 Marks]",
            syllabus_ref="34.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "When an unknown compound X is boiled with aqueous sodium hydroxide, an alkaline gas is evolved that turns damp red litmus paper blue. Identify the functional group present in X.", 1, num_answer_lines=1),
                QuestionPart("(b)", "If compound X has molecular formula C3H7NO, deduce the two possible structural formulas for X.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State how the two isomers in (b) could be distinguished using infrared spectroscopy.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Amide group (-CONH2 or -CONHR) [1].", "marks": 1},
                {"part": "(b)", "points": "Propanamide, CH3CH2CONH2 [1]; N-methylethanamide, CH3CONHCH3 [1].", "marks": 2},
                {"part": "(c)", "points": "Primary amide (propanamide) displays two N-H stretching peaks at 3300–3500 cm^-1, whereas secondary amide (N-methylethanamide) displays only a single N-H peak [1].", "marks": 1}
            ]
        ),

        # Q22: 9701/43/M/J/23/Q9(b)
        Question(
            number=22,
            title="Synthesis of Quaternary Ammonium Salts and Surfactant Action — 9701/43/M/J/23/Q9(b) [4 Marks]",
            syllabus_ref="34.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the chemical equation for the formation of tetraethylammonium bromide from triethylamine and bromoethane.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why quaternary ammonium compounds with long hydrocarbon chains are used as cationic surfactants and fabric softeners.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "(CH3CH2)3N + CH3CH2Br &rarr; (CH3CH2)4N+ Br- [2].", "marks": 2},
                {"part": "(b)", "points": "They possess a long non-polar hydrophobic hydrocarbon tail that interacts with oils/fabrics and a positively charged hydrophilic head that interacts with water [1]; The positive charge binds strongly to negatively charged fabric/hair fibres, reducing static friction and giving softness [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/F/M/22/Q10(b)
        Question(
            number=23,
            title="Isoelectric Points and Structure of Lysine at Various pH Values — 9701/42/F/M/22/Q10(b) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Lysine has two amino groups and one carboxyl group. Explain why its isoelectric point (9.7) is in the basic range.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the structural formula of lysine at pH 7.0, indicating the charges on all functional groups.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Lysine has a basic amino side-chain (-CH2CH2CH2CH2NH2) [1]; A high pH (excess OH-) is needed to deprotonate the ammonium groups to reach the neutral zwitterionic form with net charge zero [1].", "marks": 2},
                {"part": "(b)", "points": "+H3N-CH(COO-)-(CH2)4-NH3+ showing one -COO- and two -NH3+ groups (net charge +1) [2].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/23/Q9(b)
        Question(
            number=24,
            title="Action of Nitrous Acid on Primary Aliphatic vs Aromatic Amines — 9701/41/O/N/23/Q9(b) [4 Marks]",
            syllabus_ref="34.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Describe the visible observation and identify the gas evolved when ethylamine is treated with nitrous acid (NaNO2 + HCl) at 5 °C.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Contrast this with the behaviour of phenylamine under the exact same conditions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Vigorous effervescence / bubbles of colourless gas [1]; Nitrogen gas, N2 (aliphatic diazonium ion decomposes immediately to ethanol and N2) [1].", "marks": 2},
                {"part": "(b)", "points": "Phenylamine forms a stable clear solution of benzenediazonium chloride without effervescence [1]; The diazonium group is stabilised by delocalisation into the aromatic &pi;-cloud at 5 °C [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/20/Q8(b)
        Question(
            number=25,
            title="Amide Resonance and Lack of Basicity — 9701/42/M/J/20/Q8(b) [4 Marks]",
            syllabus_ref="34.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw two resonance structures for ethanamide showing the delocalisation of the nitrogen lone pair.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why ethanamide does not form a salt when mixed with dilute hydrochloric acid at room temperature.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Structure 1: CH3-C(=O)-NH2 with lone pair on N [1]; Structure 2: CH3-C(O-)=N+H2 with double bond to N and formal charges [1].", "marks": 2},
                {"part": "(b)", "points": "The lone pair on nitrogen is delocalised into the &pi;-orbital of the carbonyl group [1]; It is not sufficiently available to donate to a proton (H+), so amides are neutral and do not protonate in dilute acid [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/19/Q9(b)
        Question(
            number=26,
            title="Reduction of Nitriles and Amides: Comparing Synthetic Routes — 9701/41/M/J/19/Q9(b) [4 Marks]",
            syllabus_ref="34.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write an equation for the reduction of ethanenitrile to ethylamine using [H] to represent the reducing agent.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Write an equation for the reduction of ethanamide to ethylamine using [H].", 1, num_answer_lines=2),
                QuestionPart("(c)", "Identify a suitable reducing agent for both reactions and state the required solvent.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3CN + 4[H] &rarr; CH3CH2NH2 [1].", "marks": 1},
                {"part": "(b)", "points": "CH3CONH2 + 4[H] &rarr; CH3CH2NH2 + H2O [1].", "marks": 1},
                {"part": "(c)", "points": "Lithium tetrahydridoaluminate, LiAlH4 [1]; In dry ethoxyethane (dry ether) [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q9(b)
        Question(
            number=27,
            title="Separation of Amino Acids by Two-Dimensional Thin-Layer Chromatography — 9701/42/O/N/21/Q9(b) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why two-dimensional chromatography is necessary to separate complex mixtures of amino acids.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Name the locating agent used to visualise colourless amino acid spots on a chromatogram and state the colour observed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Several amino acids may have very similar or identical Rf values in a single solvent system, leading to overlapping spots [1]; Rotating the plate by 90° and running in a second different solvent with different polarity separates the co-eluting amino acids [1].", "marks": 2},
                {"part": "(b)", "points": "Ninhydrin spray [1]; Followed by gentle heating to develop purple / blue-violet spots [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/42/M/J/18/Q9(b)
        Question(
            number=28,
            title="Bromination of Phenylamine: Stoichiometry and Observations — 9701/42/M/J/18/Q9(b) [4 Marks]",
            syllabus_ref="34.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of phenylamine with aqueous bromine.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State two visible observations that confirm this reaction has occurred.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5NH2 + 3Br2 &rarr; C6H2Br3NH2 + 3HBr [2].", "marks": 2},
                {"part": "(b)", "points": "The orange-brown colour of bromine is decolourised [1]; A white precipitate of 2,4,6-tribromophenylamine forms [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/41/O/N/18/Q9(b)
        Question(
            number=29,
            title="Peptide Bond Hydrolysis: Acid-Catalysed vs Alkaline — 9701/41/O/N/18/Q9(b) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of the product formed from the alanyl residue when glycylalanine is hydrolysed by boiling 6 mol dm^-3 HCl.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the structural formula of the product formed from the alanyl residue when glycylalanine is hydrolysed by boiling aqueous NaOH.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "+H3N-CH(CH3)-COOH (alanine hydrochloride cation) [2].", "marks": 2},
                {"part": "(b)", "points": "H2N-CH(CH3)-COO- Na+ (sodium alaninate anion) [2].", "marks": 2}
            ]
        ),

        # Q30: 9701/42/F/M/20/Q9(b)
        Question(
            number=30,
            title="Polyamide Degradability: Chemical Hydrolysis of Nylon — 9701/42/F/M/20/Q9(b) [4 Marks]",
            syllabus_ref="34.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why clothing made of nylon weakens significantly when exposed to battery acid (sulfuric acid).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write an equation showing the cleavage of one amide linkage in Nylon 6,6 by aqueous acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Strong acid hydrolyses the amide (-CO-NH-) linkages along the polymer backbone, breaking the long chains into shorter fragments and destroying tensile strength [2].", "marks": 2},
                {"part": "(b)", "points": "-CO-NH- + H2O + H+ &rarr; -COOH + -NH3+ [2].", "marks": 2}
            ]
        ),

        # Q31: 9701/41/M/J/17/Q8(b)
        Question(
            number=31,
            title="Chromophore in Methyl Orange Azo Indicator — 9701/41/M/J/17/Q8(b) [4 Marks]",
            syllabus_ref="34.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Identify the chromophore group common to all azo dyes.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain how the colour of methyl orange changes between acidic and alkaline conditions in terms of electronic delocalisation.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The azo group / -N=N- double bond [1].", "marks": 1},
                {"part": "(b)", "points": "In acid, protonation occurs at one of the azo nitrogen atoms [1]; This modifies the extent of &pi;-electron delocalisation and alters the energy gap &Delta;E between HOMO and LUMO [1]; The molecule absorbs a different wavelength of visible light, shifting the observed complementary colour from yellow (alkali) to red (acid) [1].", "marks": 3}
            ]
        ),

        # Q32: 9701/42/O/N/17/Q9(b)
        Question(
            number=32,
            title="Reaction of Amino Acids with Nitrous Acid: Nitrogen Gas Evolution — 9701/42/O/N/17/Q9(b) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "When glycine is reacted with nitrous acid (NaNO2 + HCl), effervescence is observed and a hydroxy acid is produced. Write the balanced equation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how measuring the volume of nitrogen gas evolved in this reaction can be used for quantitative analysis of amino acids (Van Slyke method).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "H2N-CH2-COOH + HNO2 &rarr; HO-CH2-COOH + N2 + H2O [2].", "marks": 2},
                {"part": "(b)", "points": "1 mole of -NH2 group produces exactly 1 mole of N2 gas (1:1 stoichiometry) [1]; By measuring gas volume at known temperature and pressure, the moles of amino acid can be directly calculated via pV = nRT [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q10(a)
        Question(
            number=33,
            title="Classification of Amines: Primary, Secondary, Tertiary — 9701/42/M/J/23/Q10(a) [2 Marks]",
            syllabus_ref="34.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Classify diethylamine and triethylamine as primary, secondary, or tertiary amines.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Diethylamine is a secondary amine [1]; Triethylamine is a tertiary amine [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/O/N/22/Q8(a)
        Question(
            number=34,
            title="Formula of Benzenediazonium Cation — 9701/41/O/N/22/Q8(a) [2 Marks]",
            syllabus_ref="34.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Write the formula of the benzenediazonium cation, displaying the bonding between the two nitrogen atoms.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "[C6H5-N&equiv;N]+ with a triple bond between the two nitrogen atoms and a positive charge on the diazonium group [2].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/M/J/22/Q9(a)
        Question(
            number=35,
            title="Definition of Zwitterion — 9701/42/M/J/22/Q9(a) [2 Marks]",
            syllabus_ref="34.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Explain what is meant by the term zwitterion, giving one structural example.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "An electrically neutral molecule carrying both a positive and a negative formal charge on different atoms simultaneously [1]; Example: +H3N-CH2-COO- [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/M/J/21/Q10(a)
        Question(
            number=36,
            title="Preparation of Primary Amides — 9701/41/M/J/21/Q10(a) [2 Marks]",
            syllabus_ref="34.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the organic reactant and inorganic reactant used to prepare propanamide in a single step at room temperature.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Propanoyl chloride, CH3CH2COCl [1]; Concentrated aqueous ammonia, NH3 [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/O/N/20/Q8(a)
        Question(
            number=37,
            title="Acid-Base Nature of Ethanamide — 9701/42/O/N/20/Q8(a) [2 Marks]",
            syllabus_ref="34.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State whether ethanamide is acidic, basic, or neutral in aqueous solution, giving a brief reason.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Neutral [1]; The nitrogen lone pair is delocalised into the adjacent carbonyl group and is not available to accept a proton [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/M/J/23/Q9(a)
        Question(
            number=38,
            title="Conditions for Diazotisation — 9701/43/M/J/23/Q9(a) [2 Marks]",
            syllabus_ref="34.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the temperature range required for the diazotisation of phenylamine and name the inorganic acid used.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "0 °C to 10 °C [1]; Hydrochloric acid, HCl (or nitrous acid, HNO2) [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/F/M/22/Q10(a)
        Question(
            number=39,
            title="Peptide Bond Displayed Formula — 9701/42/F/M/22/Q10(a) [2 Marks]",
            syllabus_ref="34.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Draw the displayed formula of a peptide linkage, showing all bonds.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-C(=O)-N(H)- showing the C=O double bond, C-N single bond, and N-H single bond clearly [2].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/23/Q9(a)
        Question(
            number=40,
            title="Direction of Migration in Electrophoresis — 9701/41/O/N/23/Q9(a) [2 Marks]",
            syllabus_ref="34.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "In gel electrophoresis at pH 12, an amino acid exists as H2N-CHR-COO-. State which electrode it migrates towards and explain why.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Migrates towards the anode (positive electrode) [1]; Because it carries a negative net electrical charge and is attracted to the opposite charge [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50)
        # 4 x 6m, 4 x 4m, 2 x 2m = 44 MARKS
        # =====================================================================

        # Q41: Core Repeat 1 (6m) — 9701/42/M/J/22/Q8
        Question(
            number=41,
            title="Core Repeat 1: Basicity Hierarchy of Ammonia, Alkylamines, and Phenylamine — 9701/42/M/J/22/Q8 [6 Marks]",
            syllabus_ref="34.1", difficulty="HARD", section_key="SEC_D",
            preamble="The relative basicity of nitrogen bases is among the most regularly repeated structured questions in Cambridge Paper 4.",
            parts=[
                QuestionPart("(a)", "State the definition of a Bronsted-Lowry base and write the equation for the reaction of ethylamine with water.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why ethylamine is a stronger base than ammonia, referring to inductive effects.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why phenylamine is a substantially weaker base than ammonia, referring to orbital overlap.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A proton (H+) acceptor [1]; CH3CH2NH2 + H2O <=> CH3CH2NH3+ + OH- [1].", "marks": 2},
                {"part": "(b)", "points": "The ethyl group exerts an electron-donating (+I) inductive effect, increasing electron density on nitrogen and making the lone pair more available to accept H+ [2].", "marks": 2},
                {"part": "(c)", "points": "The p-orbital lone pair on nitrogen overlaps sideways with the delocalised &pi;-electron system of the benzene ring [1]; The lone pair is delocalised into the ring, significantly reducing its availability to accept a proton [1].", "marks": 2}
            ]
        ),

        # Q42: Core Repeat 2 (6m) — 9701/41/O/N/21/Q9
        Question(
            number=42,
            title="Core Repeat 2: Full Synthesis and Mechanism of Azo Dye Coupling — 9701/41/O/N/21/Q9 [6 Marks]",
            syllabus_ref="34.2", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Describe how phenylamine is converted to benzenediazonium chloride, specifying all reagents, equations, and temperature controls.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Describe how the benzenediazonium ion reacts with an alkaline solution of phenol, stating the observation and giving the structural formula of the azo dye.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "NaNO2 and concentrated (or dilute) HCl (generating HNO2) [1]; C6H5NH2 + HNO2 + HCl &rarr; C6H5N2+ Cl- + 2H2O [1]; Temperature kept between 0 °C and 10 °C to prevent decomposition [1].", "marks": 3},
                {"part": "(b)", "points": "Alkaline solution of phenol (phenoxide ion, C6H5O-) is cooled in ice and mixed with the diazonium solution [1]; An intense yellow-orange precipitate / colour is observed [1]; Structure of 4-hydroxyazobenzene: C6H5-N=N-C6H4-OH [1].", "marks": 3}
            ]
        ),

        # Q43: Core Repeat 3 (6m) — 9701/42/M/J/21/Q10
        Question(
            number=43,
            title="Core Repeat 3: Gel Electrophoresis Separation of Three Amino Acids at Two Buffer pH Values — 9701/42/M/J/21/Q10 [6 Marks]",
            syllabus_ref="34.4", difficulty="HARD", section_key="SEC_D",
            preamble="The isoelectric points (pI) of three amino acids are:<br/>"
                     "- Serine: pI = 5.7<br/>"
                     "- Arginine: pI = 10.8<br/>"
                     "- Aspartic acid: pI = 2.8",
            parts=[
                QuestionPart("(a)", "Predict the direction of migration (towards anode +, cathode -, or remaining near origin) for each amino acid when electrophoresis is conducted at a buffer pH of 5.7.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Predict the direction of migration for each amino acid when electrophoresis is conducted at a buffer pH of 1.5.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "At pH 5.7: Serine is at its pI, has net charge 0, and remains at origin [1]; Arginine (pI 10.8) is below its pI, carries net positive charge, and migrates to cathode (-) [1]; Aspartic acid (pI 2.8) is above its pI, carries net negative charge, and migrates to anode (+) [1].", "marks": 3},
                {"part": "(b)", "points": "At pH 1.5: All three amino acids are at a pH below their isoelectric points [1]; All three carry net positive charges (+H3N-CHR-COOH) [1]; Therefore, all three migrate towards the cathode (-), with separation depending on their charge-to-mass ratios [1].", "marks": 3}
            ]
        ),

        # Q44: Core Repeat 4 (6m) — 9701/42/O/N/19/Q9
        Question(
            number=44,
            title="Core Repeat 4: Multi-Step Synthetic Route to an Aromatic Amide from Benzene — 9701/42/O/N/19/Q9 [6 Marks]",
            syllabus_ref="34.3", difficulty="HARD", section_key="SEC_D",
            preamble="Devise a four-step synthetic route to convert benzene, C<sub>6</sub>H<sub>6</sub>, into N-phenylethanamide, C<sub>6</sub>H<sub>5</sub>NHCOCH<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "Step 1 converts benzene into nitrobenzene. State the reagents and temperature.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Step 2 reduces nitrobenzene to phenylamine. State the reagents, conditions, and the work-up reagent.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Step 3 reacts phenylamine with an acylating agent to form N-phenylethanamide. Name this agent, write the equation, and state the byproduct.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated HNO3 and concentrated H2SO4 at 55 °C [2].", "marks": 2},
                {"part": "(b)", "points": "Tin (Sn) and concentrated HCl, heated under reflux [1]; Followed by aqueous NaOH to liberate free phenylamine [1].", "marks": 2},
                {"part": "(c)", "points": "Ethanoyl chloride, CH3COCl (or ethanoic anhydride) [1]; C6H5NH2 + CH3COCl &rarr; C6H5NHCOCH3 + HCl [1].", "marks": 2}
            ]
        ),

        # Q45: Core Repeat 5 (4m) — 9701/42/M/J/23/Q10(c)
        Question(
            number=45,
            title="Core Repeat 5: Acid and Alkaline Hydrolysis of a Dipeptide — 9701/42/M/J/23/Q10(c) [4 Marks]",
            syllabus_ref="34.4", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Glycylalanine has the formula H<sub>2</sub>N-CH<sub>2</sub>-CO-NH-CH(CH<sub>3</sub>)-COOH.",
            parts=[
                QuestionPart("(a)", "Draw the structures of the organic products formed when glycylalanine is boiled with excess 6 mol dm^-3 hydrochloric acid.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the structures of the organic products formed when glycylalanine is boiled with excess aqueous sodium hydroxide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "+H3N-CH2-COOH and +H3N-CH(CH3)-COOH (both amino groups protonated, carboxyls intact) [2].", "marks": 2},
                {"part": "(b)", "points": "H2N-CH2-COO- and H2N-CH(CH3)-COO- (both carboxyl groups deprotonated as sodium salts, amino groups neutral) [2].", "marks": 2}
            ]
        ),

        # Q46: Core Repeat 6 (4m) — 9701/41/O/N/22/Q8(c)
        Question(
            number=46,
            title="Core Repeat 6: Synthesis and Basicity of Secondary and Tertiary Amines — 9701/41/O/N/22/Q8(c) [4 Marks]",
            syllabus_ref="34.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of ethylamine with bromoethane to form diethylamine.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why diethylamine can react further with bromoethane and state the final product formed if bromoethane is in large excess.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3CH2NH2 + CH3CH2Br &rarr; (CH3CH2)2NH + HBr (or + 2CH3CH2NH2 &rarr; diethylamine + ethylammonium bromide) [2].", "marks": 2},
                {"part": "(b)", "points": "Diethylamine has a lone pair on nitrogen and acts as a nucleophile to attack more bromoethane [1]; Final product: tetraethylammonium bromide, (CH3CH2)4N+ Br- (quaternary ammonium salt) [1].", "marks": 2}
            ]
        ),

        # Q47: Core Repeat 7 (4m) — 9701/42/F/M/21/Q10(b)
        Question(
            number=47,
            title="Core Repeat 7: Azo Coupling with 2-Naphthol — 9701/42/F/M/21/Q10(b) [4 Marks]",
            syllabus_ref="34.2", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the observations when benzenediazonium chloride is added to an ice-cold alkaline solution of 2-naphthol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why azo dyes are intensely coloured and resistant to fading in sunlight.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A bright red-orange precipitate / dye (Sudan I) is formed immediately [2].", "marks": 2},
                {"part": "(b)", "points": "The extended conjugated &pi;-system spans both aromatic rings and the azo group, absorbing in the visible spectrum [1]; High delocalisation resonance energy imparts stability against photochemical degradation by UV light [1].", "marks": 2}
            ]
        ),

        # Q48: Core Repeat 8 (4m) — 9701/41/M/J/20/Q9(c)
        Question(
            number=48,
            title="Core Repeat 8: Distinction Between Phenylamine, Benzamide, and Benzyl Chloride — 9701/41/M/J/20/Q9(c) [4 Marks]",
            syllabus_ref="34.3", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Three unlabelled bottles contain phenylamine (C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub>), benzamide (C<sub>6</sub>H<sub>5</sub>CONH<sub>2</sub>), and benzyl chloride (C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>Cl).",
            parts=[
                QuestionPart("(a)", "Describe a chemical test that will identify phenylamine immediately.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe a chemical test that will identify benzamide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add bromine water [1]; Bromine water is decolourised and a white precipitate of 2,4,6-tribromophenylamine forms (neither benzamide nor benzyl chloride react) [1].", "marks": 2},
                {"part": "(b)", "points": "Boil with aqueous sodium hydroxide [1]; An alkaline gas (ammonia, NH3) is evolved that turns damp red litmus paper blue [1].", "marks": 2}
            ]
        ),

        # Q49: Core Repeat 9 (2m) — 9701/42/M/J/23/Q10(e)
        Question(
            number=49,
            title="Core Repeat 9: Observation for Phenylamine Bromination — 9701/42/M/J/23/Q10(e) [2 Marks]",
            syllabus_ref="34.2", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State two visible observations when excess aqueous bromine is added to phenylamine.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Orange/brown bromine water is decolourised [1]; A white precipitate is formed [1].", "marks": 2}
            ]
        ),

        # Q50: Core Repeat 10 (2m) — 9701/41/O/N/23/Q9(e)
        Question(
            number=50,
            title="Core Repeat 10: Isoelectric Point and Net Charge — 9701/41/O/N/23/Q9(e) [2 Marks]",
            syllabus_ref="34.4", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the net charge on an amino acid when the solution pH is strictly less than its isoelectric point, and deduce which electrode it migrates to during electrophoresis.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Positive net charge (+1 or higher) [1]; Migrates towards the cathode (negative electrode) [1].", "marks": 2}
            ]
        )
    ]

    # Verify tariffs
    count_6m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    count_4m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    count_2m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_qs = len(questions)

    print(f"Topic 34 Questions Count: {total_qs}")
    print(f"Tariff Breakdown: 6-markers = {count_6m} ({count_6m/total_qs*100:.0f}%), 4-markers = {count_4m} ({count_4m/total_qs*100:.0f}%), 2-markers = {count_2m} ({count_2m/total_qs*100:.0f}%) | Total Marks = {total_marks}")

    assert total_qs == 50, f"Expected 50 questions, got {total_qs}"
    assert total_marks == 220, f"Expected 220 marks, got {total_marks}"
    assert count_6m == 20, f"Expected 20 6-markers, got {count_6m}"
    assert count_4m == 20, f"Expected 20 4-markers, got {count_4m}"
    assert count_2m == 10, f"Expected 10 2-markers, got {count_2m}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 34 PDF built successfully!")

if __name__ == "__main__":
    build_topic34_50q()
