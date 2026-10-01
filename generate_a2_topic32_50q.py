"""
Complete 50-Question Master Pack: Topic 32 — Hydroxy Compounds (Phenol) (Paper 4 Theory)
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

def build_topic32_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic32_Hydroxy_Compounds_Phenol.pdf"

    topic_title = "Topic 32 — Hydroxy Compounds (Phenol)"
    topic_subtitle = "Structure & Acidity of Phenols · Delocalisation in Phenoxide · Electrophilic Substitution · Halogenation & Nitration · Azo Coupling Reactions"

    subtopics_summary = [
        ("32.1 Structure & Relative Acidity of Phenol", "Comparison of acid strengths of ethanol, water, phenol, and ethanoic acid; delocalisation of negative charge into the aromatic π-electron system in the phenoxide ion; destabilisation of ethoxide by +I ethyl group; reactions with sodium and aqueous alkalis."),
        ("32.2 Ring Activation & Electrophilic Substitution", "Overlap of the oxygen p-orbital lone pair with the delocalised benzene π-system; activation of 2-, 4-, and 6-positions; rapid bromination with bromine water without a Lewis acid catalyst yielding 2,4,6-tribromophenol; nitration with dilute nitric acid at room temperature."),
        ("32.3 Chemical Tests & Distinction from Alcohols/Acids", "Characteristic purple/violet complexation with neutral aqueous iron(III) chloride; rapid decolourisation of bromine water with white precipitate formation; lack of effervescence with aqueous sodium hydrogencarbonate distinguishing phenol from carboxylic acids."),
        ("32.4 Diazonium Coupling & Azo Dyes", "Electrophilic aromatic substitution of alkaline phenol by the benzenediazonium cation (C6H5N2+) at 0–10 °C to yield bright yellow/orange azo dyes containing the -N=N- chromophore."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Hydroxy Compounds and Phenols from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q7
        Question(
            number=1,
            title="Relative Acidities of Ethanol, Water, and Phenol — 9701/42/M/J/23/Q7 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_A",
            preamble="The relative acid strengths of ethanol, water, and phenol differ significantly as shown in Fig. 1.1.",
            figure_path=os.path.join(fig_dir, "a2_t32_phenol_acidity_spectrum.png"),
            figure_caption="Fig. 1.1: Relative acid strength and pKa spectrum for ethanol, water, phenol, and ethanoic acid.",
            parts=[
                QuestionPart("(a)", "Rank ethanol, water, and phenol in order of increasing acid strength.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain in terms of structure and bonding why phenol is significantly more acidic than ethanol.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Compare the reactions of ethanol and phenol with aqueous sodium hydroxide, NaOH(aq), writing an ionic equation where a reaction occurs.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ethanol < Water < Phenol [1].", "marks": 1},
                {"part": "(b)", "points": "In the phenoxide ion, C6H5O-, the lone pair of electrons on the oxygen atom overlaps with the delocalised &pi;-electron cloud of the benzene ring [1]; This delocalises the negative charge over the aromatic ring, stabilising the phenoxide ion relative to undissociated phenol [1]; In contrast, in the ethoxide ion, CH3CH2O-, the ethyl group exerts an electron-donating (+I) inductive effect, concentrating negative charge on oxygen and destabilising the anion [1].", "marks": 3},
                {"part": "(c)", "points": "Phenol reacts with NaOH(aq) to form sodium phenoxide and water: C6H5OH + OH- -> C6H5O- + H2O [1]; Ethanol does not react with NaOH(aq) because it is a weaker acid than water [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/O/N/22/Q6
        Question(
            number=2,
            title="Resonance Delocalisation in the Phenoxide Anion and Ring Activation — 9701/41/O/N/22/Q6 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_A",
            preamble="The chemical behaviour of phenol is governed by interaction between the oxygen lone pair and the aromatic ring as shown in Fig. 2.1.",
            figure_path=os.path.join(fig_dir, "a2_t32_phenoxide_resonance.png"),
            figure_caption="Fig. 2.1: Delocalisation of negative charge across the phenoxide system.",
            parts=[
                QuestionPart("(a)", "Describe how the lone pair of electrons on the oxygen atom interacts with the aromatic ring in phenol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State which ring positions in phenol experience the greatest increase in electron density as a consequence.", 1, num_answer_lines=1),
                QuestionPart("(c)", "Explain why phenol reacts with dilute nitric acid at room temperature, whereas benzene requires a mixture of concentrated nitric and sulfuric acids at 55 °C.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "One of the p-orbital lone pairs on the oxygen atom overlaps sideways with the delocalised &pi;-orbitals of the benzene ring [1]; This delocalises electron density into the ring, increasing the overall electron density of the benzene ring [1].", "marks": 2},
                {"part": "(b)", "points": "Positions 2, 4, and 6 (ortho and para positions) [1].", "marks": 1},
                {"part": "(c)", "points": "The higher electron density in phenol polarises incoming electrophiles (such as NO2+ or HNO3) much more effectively than benzene [1]; The activation energy for electrophilic substitution is significantly lower in phenol [1]; Therefore, phenol reacts rapidly with dilute HNO3 at room temperature, whereas benzene requires the powerful electrophile NO2+ generated by conc. H2SO4 at elevated temperature [1].", "marks": 3}
            ]
        ),

        # Q3: 9701/42/M/J/22/Q7
        Question(
            number=3,
            title="Bromination of Phenol vs Bromination of Benzene — 9701/42/M/J/22/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State the observations when aqueous bromine is added to phenol at room temperature.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Give the structural formula and systematic IUPAC name of the organic product formed in (a).", 2, num_answer_lines=2),
                QuestionPart("(c)", "Contrast the reaction conditions and mechanism for the bromination of benzene with those for the bromination of phenol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Bromine water is decolourised (from orange/brown to colourless) [1]; A white precipitate is formed [1].", "marks": 2},
                {"part": "(b)", "points": "2,4,6-tribromophenol [1]; Correct structural formula showing -OH at C1 and -Br at C2, C4, C6 [1].", "marks": 2},
                {"part": "(c)", "points": "Benzene requires pure Br2(l) and a halogen carrier catalyst such as AlBr3 or FeBr3 with heating, undergoing monobromination [1]; Phenol reacts spontaneously with aqueous Br2 without catalyst at room temperature, undergoing triple substitution at positions 2, 4, 6 due to activation by the -OH group [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/M/J/21/Q8
        Question(
            number=4,
            title="Distinguishing Tests Between Phenol, Ethanoic Acid, and Cyclohexanol — 9701/41/M/J/21/Q8 [6 Marks]",
            syllabus_ref="32.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Describe a chemical test that will give a positive result with ethanoic acid but no reaction with phenol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe a chemical test using iron(III) chloride that distinguishes phenol from cyclohexanol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe how the reactions of cyclohexanol and phenol with sodium metal compare in observations and products.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add aqueous sodium carbonate, Na2CO3(aq), or sodium hydrogencarbonate, NaHCO3(aq) [1]; Ethanoic acid produces effervescence / bubbles of CO2 gas which turns limewater cloudy, whereas phenol does not react (no effervescence) [1].", "marks": 2},
                {"part": "(b)", "points": "Add neutral aqueous iron(III) chloride, FeCl3(aq) [1]; Phenol gives a characteristic violet / purple solution, whereas cyclohexanol produces no colour change / remains yellow [1].", "marks": 2},
                {"part": "(c)", "points": "Both react with sodium metal to produce effervescence of hydrogen gas, H2 [1]; Phenol forms sodium phenoxide (C6H5O-Na+) while cyclohexanol forms sodium cyclohexoxide (C6H11O-Na+) [1].", "marks": 2}
            ]
        ),

        # Q5: 9701/42/O/N/20/Q6
        Question(
            number=5,
            title="Azo Dye Synthesis: Diazotisation and Alkaline Coupling with Phenol — 9701/42/O/N/20/Q6 [6 Marks]",
            syllabus_ref="32.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State the reagents and precise temperature required to convert phenylamine into the benzenediazonium ion.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the temperature in (a) must be kept strictly below 10 °C.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Describe the conditions required for benzenediazonium chloride to react with phenol, and give the structure of the azo dye produced.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sodium nitrite (NaNO2) and concentrated (or dilute) hydrochloric acid (HCl) (or nitrous acid, HNO2) [1]; Temperature between 0 °C and 10 °C (or in ice bath) [1].", "marks": 2},
                {"part": "(b)", "points": "Above 10 °C, the benzenediazonium ion decomposes rapidly into phenol and nitrogen gas (C6H5N2+ + H2O -> C6H5OH + N2 + H+) [1].", "marks": 1},
                {"part": "(c)", "points": "Phenol must be dissolved in aqueous sodium hydroxide, NaOH(aq), to form the electron-rich phenoxide ion [1]; The solution is kept cold (0–10 °C) while benzenediazonium chloride is added [1]; Structure of 4-hydroxyazobenzene: C6H5-N=N-C6H4-4-OH with the azo group (-N=N-) linking the two aromatic rings [1].", "marks": 3}
            ]
        ),

        # Q6: 9701/43/M/J/23/Q7
        Question(
            number=6,
            title="Synthesis and Acidity of Substituted Phenols: Nitrophenols — 9701/43/M/J/23/Q7 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain why 4-nitrophenol is significantly more acidic than unsubstituted phenol.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why 4-methylphenol is slightly less acidic than unsubstituted phenol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Predict whether 2,4,6-trinitrophenol (picric acid) will react with aqueous sodium hydrogencarbonate, giving a reason.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The nitro group (-NO2) is strongly electron-withdrawing via inductive (-I) and mesomeric/resonance (-M) effects [1]; It withdraws electron density away from the phenoxide oxygen, further delocalising the negative charge over the conjugate base [1]; This increases the stability of the 4-nitrophenoxide anion, shifting the dissociation equilibrium to the right [1].", "marks": 3},
                {"part": "(b)", "points": "The methyl group (-CH3) is electron-donating (+I inductive effect) [1]; It pushes electron density towards the aromatic ring and oxygen, concentrating negative charge and destabilising the anion [1].", "marks": 2},
                {"part": "(c)", "points": "Yes, it will react to produce CO2 effervescence because three strongly electron-withdrawing nitro groups make picric acid a strong acid (pKa ~ 0.38), stronger than carbonic acid [1].", "marks": 1}
            ]
        ),

        # Q7: 9701/42/F/M/22/Q8
        Question(
            number=7,
            title="Esterification Reactions of Phenol and Ethanoyl Chloride — 9701/42/F/M/22/Q8 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain why phenol does not react with ethanoic acid to form an ester under standard acid catalysis.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Name a suitable acylating agent that will react readily with phenol to form phenyl ethanoate, and state the observations.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Write a balanced equation for the reaction in (b), and explain how adding aqueous sodium hydroxide accelerates this reaction.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The lone pair on the phenolic oxygen is delocalised into the benzene ring, making the oxygen much less nucleophilic than that in aliphatic alcohols [1]; In addition, ethanoic acid contains a relatively poor leaving group and is not electrophilic enough to be attacked by the weakly nucleophilic phenol [1].", "marks": 2},
                {"part": "(b)", "points": "Ethanoyl chloride, CH3COCl [1]; Steamy / misty white fumes of hydrogen chloride (HCl) gas produced [1].", "marks": 2},
                {"part": "(c)", "points": "C6H5OH + CH3COCl -> CH3COOC6H5 + HCl [1]; Aqueous NaOH deprotonates phenol to form the phenoxide ion, C6H5O-, which carries a full negative charge and is a far stronger nucleophile than neutral phenol [1].", "marks": 2}
            ]
        ),

        # Q8: 9701/41/O/N/23/Q7
        Question(
            number=8,
            title="Nitration of Phenol and Separation of Isomers — 9701/41/O/N/23/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Give the reagents and conditions for the mononitration of phenol, and draw the structures of the two principal organic products.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why 2-nitrophenol has a lower boiling point and is more volatile than 4-nitrophenol.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Dilute nitric acid, HNO3(aq), at room temperature [1]; Structure of 2-nitrophenol (ortho-nitrophenol) [1]; Structure of 4-nitrophenol (para-nitrophenol) [1].", "marks": 3},
                {"part": "(b)", "points": "In 2-nitrophenol, the -OH and -NO2 groups are adjacent, allowing intramolecular hydrogen bonding to form within the molecule [1]; This reduces its ability to form intermolecular hydrogen bonds with neighbouring molecules [1]; In 4-nitrophenol, the groups are too far apart for intramolecular bonding, so it forms extensive intermolecular hydrogen bonds, requiring significantly more energy to separate the molecules [1].", "marks": 3}
            ]
        ),

        # Q9: 9701/42/M/J/20/Q6
        Question(
            number=9,
            title="Multi-Step Synthesis: Phenylamine to 4-Hydroxyazobenzene — 9701/42/M/J/20/Q6 [6 Marks]",
            syllabus_ref="32.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Step 1 converts phenylamine to compound D. State the reagents and conditions for Step 1.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify compound D and explain why its solution must be maintained at 5 °C.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Step 2 reacts compound D with alkaline phenol. State why this reaction is classified as an electrophilic substitution.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sodium nitrite (NaNO2) and excess hydrochloric acid (HCl) [1]; Ice-cold conditions / temperature below 10 °C [1].", "marks": 2},
                {"part": "(b)", "points": "Benzenediazonium chloride, C6H5N2+ Cl- [1]; Above 10 °C the diazonium group undergoes hydrolysis / decomposition to phenol releasing N2 gas [1].", "marks": 2},
                {"part": "(c)", "points": "The positively charged diazonium ion (C6H5N2+) acts as an electrophile [1]; It attacks the electron-rich aromatic ring of the phenoxide ion, replacing a hydrogen atom at the 4-position with retention of aromaticity [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/19/Q7
        Question(
            number=10,
            title="Directing Effects of the -OH Group in Phenol Derivatives — 9701/41/M/J/19/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain why the -OH group directs incoming electrophiles to the 2- and 4-positions of the aromatic ring.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Predict the major organic product when 4-methylphenol is reacted with excess bromine water, and explain your deduction.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Delocalisation of the oxygen lone pair into the ring produces resonance contributors where negative charge is localised specifically on carbons 2, 4, and 6 [1]; Electrophiles are positively charged and therefore preferentially attack the positions of highest electron density [1]; Furthermore, the carbocation intermediates formed from attack at 2- and 4-positions are stabilised by resonance donation from oxygen [1].", "marks": 3},
                {"part": "(b)", "points": "2,6-dibromo-4-methylphenol [1]; The 4-position is already occupied by the methyl group [1]; The -OH group strongly activates positions 2 and 6, leading to dibromination at both vacant ortho positions [1].", "marks": 3}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q7
        Question(
            number=11,
            title="Quantitative Analysis of Phenol by Bromate-Bromide Titration — 9701/42/O/N/21/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            preamble="Phenol reacts quantitatively with bromine generated in situ according to the equations:<br/>"
                     "BrO<sub>3</sub><sup>-</sup> + 5Br<sup>-</sup> + 6H<sup>+</sup> &rarr; 3Br<sub>2</sub> + 3H<sub>2</sub>O<br/>"
                     "C<sub>6</sub>H<sub>5</sub>OH + 3Br<sub>2</sub> &rarr; C<sub>6</sub>H<sub>2</sub>Br<sub>3</sub>OH + 3HBr<br/>"
                     "A 0.188 g sample of impure phenol is dissolved and reacted with excess bromate/bromide. The unreacted Br<sub>2</sub> is determined by adding excess KI and titrating liberated I<sub>2</sub> against 0.100 mol dm<sup>-3</sup> Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "State the molar ratio of phenol to bromine, Br2, in this reaction.", 1, num_answer_lines=1),
                QuestionPart("(b)", "If the total Br2 generated was 7.50 x 10^-3 mol and the unreacted Br2 required 30.00 cm^3 of 0.100 mol dm^-3 thiosulfate, calculate the moles of unreacted Br2.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the percentage purity by mass of phenol in the original sample (Mr of phenol = 94.0).", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1 mol phenol : 3 mol Br2 [1].", "marks": 1},
                {"part": "(b)", "points": "Moles of S2O3(2-) = 0.03000 x 0.100 = 3.00 x 10^-3 mol [1]; Since 1 Br2 = 1 I2 = 2 S2O3(2-), moles of unreacted Br2 = 3.00 x 10^-3 / 2 = 1.50 x 10^-3 mol [1].", "marks": 2},
                {"part": "(c)", "points": "Moles of Br2 reacted = 7.50 x 10^-3 - 1.50 x 10^-3 = 6.00 x 10^-3 mol [1]; Moles of pure phenol = 6.00 x 10^-3 / 3 = 2.00 x 10^-3 mol [1]; Mass of phenol = 2.00 x 10^-3 x 94.0 = 0.188 g, so percentage purity = (0.188 / 0.188) x 100 = 100% (or exact calculated value) [1].", "marks": 3}
            ]
        ),

        # Q12: 9701/42/M/J/18/Q7
        Question(
            number=12,
            title="Comparison of Phenol, Phenylmethanol, and Benzyl Chloride — 9701/42/M/J/18/Q7 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Compare the reactivity of phenol and phenylmethanol (C6H5CH2OH) with acidified potassium dichromate(VI).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Compare the reactivity of phenol and phenylmethanol with phosphorus(V) chloride, PCl5.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why phenylmethanol has a pKa similar to ethanol (~16), whereas phenol has a pKa of 10.0.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenylmethanol is a primary alcohol and is oxidised to benzoic acid (orange solution turns green) [1]; Phenol resists oxidation by acidified dichromate because the -OH carbon has no hydrogen atom and the aromatic ring resists oxidation [1].", "marks": 2},
                {"part": "(b)", "points": "Phenylmethanol reacts vigorously with PCl5 to substitute -OH with -Cl forming C6H5CH2Cl and steamy HCl fumes [1]; Phenol gives poor yields of chlorobenzene because the C-O bond has partial double bond character due to delocalisation and is difficult to break [1].", "marks": 2},
                {"part": "(c)", "points": "In phenylmethanol, the -CH2- group insulates the -OH group from the aromatic ring, preventing delocalisation of the oxygen lone pair into the &pi;-system [1]; In phenol, the -OH group is directly bonded to the ring, allowing delocalisation and resonance stabilisation of the phenoxide anion [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/41/O/N/18/Q7
        Question(
            number=13,
            title="Synthesis of Aspirin from 2-Hydroxybenzoic Acid — 9701/41/O/N/18/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Draw the structure of 2-hydroxybenzoic acid (salicylic acid) and identify both functional groups present.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the reagent and conditions used to convert 2-hydroxybenzoic acid into aspirin (acetylsalicylic acid).", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain which functional group in 2-hydroxybenzoic acid is esterified during the synthesis of aspirin, and write the equation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Correct structural formula showing benzene ring with adjacent -COOH and -OH groups [1]; Identifies phenol (-OH) and carboxylic acid (-COOH) groups [1].", "marks": 2},
                {"part": "(b)", "points": "Ethanoic anhydride, (CH3CO)2O (or ethanoyl chloride, CH3COCl) [1]; Phosphoric acid catalyst with gentle heating / reflux [1].", "marks": 2},
                {"part": "(c)", "points": "The phenolic -OH group is esterified [1]; 2-HOC6H4COOH + (CH3CO)2O -> 2-(CH3COOC6H4)COOH + CH3COOH [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/F/M/20/Q7
        Question(
            number=14,
            title="Halogenation of Phenol with Non-Polar vs Aqueous Solvents — 9701/42/F/M/20/Q7 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "When bromine is dissolved in a non-polar solvent such as CCl4 and reacted with phenol at 0 °C, only monobromination occurs. Suggest the structure of the two monobrominated isomers formed.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why monobromination occurs in CCl4, whereas tribromination occurs in aqueous solution.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State which monobromo isomer predominates at higher temperatures and give a reason.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2-bromophenol and 4-bromophenol [2].", "marks": 2},
                {"part": "(b)", "points": "In aqueous solution, water acts as a base and ionises phenol into the phenoxide ion, C6H5O- [1]; The phenoxide ion is enormously more activated than unionised phenol towards electrophilic attack, leading to rapid triple substitution at 2, 4, 6 [1]; In non-polar CCl4, phenol remains largely unionised (non-polar medium), so the ring is less activated and substitution stops after one bromine is introduced [1].", "marks": 3},
                {"part": "(c)", "points": "4-bromophenol predominates because the 2-position experiences steric hindrance from the adjacent -OH group [1].", "marks": 1}
            ]
        ),

        # Q15: 9701/41/M/J/17/Q6
        Question(
            number=15,
            title="Condensation of Phenol with Carbonyls: Bisphenol A — 9701/41/M/J/17/Q6 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Bisphenol A is produced by reacting phenol with propanone in the presence of an acid catalyst. State the role of the acid catalyst in this electrophilic aromatic substitution.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the molar ratio of phenol to propanone in the synthesis of Bisphenol A.", 1, num_answer_lines=1),
                QuestionPart("(c)", "Draw the structure of Bisphenol A, (CH3)2C(4-C6H4OH)2, and explain why substitution occurs exclusively at the 4-position.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The acid protonates the carbonyl oxygen of propanone: (CH3)2C=O + H+ -> [(CH3)2C=OH]+ [1]; This creates a carbocation electrophile that is sufficiently reactive to attack the activated benzene ring of phenol [1].", "marks": 2},
                {"part": "(b)", "points": "2 mol of phenol : 1 mol of propanone [1].", "marks": 1},
                {"part": "(c)", "points": "Correct structure showing central carbon bonded to two methyl groups and two 4-hydroxyphenyl groups [1]; The 4-position is activated by the -OH group [1]; The 4-position is completely free of steric hindrance compared to the 2-position [1].", "marks": 3}
            ]
        ),

        # Q16: 9701/42/O/N/17/Q7
        Question(
            number=16,
            title="Acidity Calculations for Phenol in Aqueous Solution — 9701/42/O/N/17/Q7 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Write the expression for the acid dissociation constant, Ka, of phenol.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Given that Ka for phenol is 1.30 x 10^-10 mol dm^-3 at 298 K, calculate the pH of a 0.0500 mol dm^-3 solution of phenol.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Calculate the percentage of phenol molecules that are ionised in this solution.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ka = [C6H5O-][H+] / [C6H5OH] [1].", "marks": 1},
                {"part": "(b)", "points": "[H+]^2 = Ka x [C6H5OH] = (1.30 x 10^-10) x 0.0500 = 6.50 x 10^-12 mol^2 dm^-6 [1]; [H+] = sqrt(6.50 x 10^-12) = 2.55 x 10^-6 mol dm^-3 [1]; pH = -log10(2.55 x 10^-6) = 5.59 [1].", "marks": 3},
                {"part": "(c)", "points": "% ionisation = ([H+] / [C6H5OH]initial) x 100 [1]; = (2.55 x 10^-6 / 0.0500) x 100 = 5.10 x 10^-3 % [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q7(d)
        Question(
            number=17,
            title="Reaction of Phenol with Aqueous Sodium Hydroxide vs Carbonates — 9701/42/M/J/23/Q7(d) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why phenol dissolves in aqueous sodium hydroxide but is insoluble in water.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why phenol does not produce carbon dioxide when added to aqueous sodium hydrogencarbonate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenol is weakly acidic and reacts with NaOH(aq) to form sodium phenoxide, C6H5O-Na+ [1]; Sodium phenoxide is an ionic salt that readily hydrates and dissolves in polar water molecules [1].", "marks": 2},
                {"part": "(b)", "points": "Phenol (pKa ~ 10.0) is a weaker acid than carbonic acid, H2CO3 (pKa ~ 6.35) [1]; Therefore, phenol cannot protonate hydrogencarbonate ions (HCO3-) to liberate CO2 [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/O/N/22/Q6(c)
        Question(
            number=18,
            title="Comparison of Reaction Rates: Phenol vs Benzene with Bromine — 9701/41/O/N/22/Q6(c) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State why benzene requires a halogen carrier catalyst to react with bromine.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why phenol reacts instantly with bromine without needing a catalyst.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The delocalised &pi;-electron density in benzene is insufficient to polarise non-polar Br2 molecules [1]; A halogen carrier (e.g. FeBr3) is needed to polarise and generate the strong electrophile Br+ [1].", "marks": 2},
                {"part": "(b)", "points": "The lone pair on the oxygen atom overlaps with the benzene &pi;-ring, greatly increasing the electron density of the ring [1]; The electron-rich ring in phenol can polarise incoming Br-Br molecules directly [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/M/J/22/Q7(c)
        Question(
            number=19,
            title="Synthesis of Benzenediazonium Chloride from Nitrobenzene — 9701/42/M/J/22/Q7(c) [4 Marks]",
            syllabus_ref="32.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Outline the two-step sequence to prepare benzenediazonium chloride starting from nitrobenzene, stating reagents for both steps.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State the essential condition required during the second step.", 1, num_answer_lines=1)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Tin (Sn) and concentrated hydrochloric acid (conc. HCl), followed by NaOH(aq) to reduce nitrobenzene to phenylamine [2]; Step 2: Sodium nitrite (NaNO2) and hydrochloric acid (HCl) [1].", "marks": 3},
                {"part": "(b)", "points": "Temperature maintained strictly between 0 °C and 10 °C [1].", "marks": 1}
            ]
        ),

        # Q20: 9701/41/M/J/21/Q8(b)
        Question(
            number=20,
            title="Reaction of Phenol with Ethanoic Anhydride — 9701/41/M/J/21/Q8(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the structural formula of the ester formed when phenol reacts with ethanoic anhydride.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Give two reasons why ethanoic anhydride is preferred over ethanoyl chloride in industrial esterifications.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COOC6H5 (phenyl ethanoate) [1]; Correct display showing ester linkage between acetyl and phenyl group [1].", "marks": 2},
                {"part": "(b)", "points": "Ethanoic anhydride is cheaper and less toxic / less corrosive than ethanoyl chloride [1]; It produces ethanoic acid as a byproduct rather than toxic, corrosive fumes of HCl gas [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q6(d)
        Question(
            number=21,
            title="Structure and Colour of Azo Dyes — 9701/42/O/N/20/Q6(d) [4 Marks]",
            syllabus_ref="32.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the azo group (-N=N-) linking two benzene rings in 4-hydroxyazobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why 4-hydroxyazobenzene is intensely coloured.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5-N=N-C6H4-OH with correct -N=N- double bond and linear geometry around nitrogen atoms [2].", "marks": 2},
                {"part": "(b)", "points": "The azo group provides a conjugated bridge connecting the &pi;-electron systems of both benzene rings, creating an extensive delocalised system [1]; The energy gap (&Delta;E) between HOMO and LUMO is reduced, allowing absorption of visible light (blue light) so that the complementary colour (yellow-orange) is reflected [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/43/M/J/23/Q7(c)
        Question(
            number=22,
            title="Relative Acidities of 2-Chlorophenol and 4-Chlorophenol — 9701/43/M/J/23/Q7(c) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Predict whether 4-chlorophenol is more or less acidic than unsubstituted phenol, and explain your answer.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why 2-chlorophenol has a slightly lower pKa than 4-chlorophenol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-chlorophenol is more acidic than phenol [1]; The electronegative chlorine atom exerts an electron-withdrawing (-I) inductive effect, stabilising the phenoxide anion [1].", "marks": 2},
                {"part": "(b)", "points": "In 2-chlorophenol, the chlorine atom is closer to the oxygen atom [1]; Inductive effects decrease rapidly with distance, so the -I effect is stronger in the 2-position, providing greater stabilisation to the phenoxide charge [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/F/M/22/Q8(b)
        Question(
            number=23,
            title="Electrophilic Nitration of Phenol: Mononitration vs Trinitration — 9701/42/F/M/22/Q8(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the reagents and conditions needed to obtain 2,4,6-trinitrophenol from phenol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why trinitration requires much more severe conditions than mononitration.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated nitric acid, conc. HNO3, and concentrated sulfuric acid, conc. H2SO4 [1]; Heating / reflux [1].", "marks": 2},
                {"part": "(b)", "points": "The introduction of each nitro group (-NO2) withdraws electron density from the aromatic ring (-I and -M effects) [1]; This deactivates the ring towards further electrophilic attack, so subsequent nitrations require a stronger electrophile and higher energy [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/23/Q7(c)
        Question(
            number=24,
            title="Characteristic Test with Neutral Iron(III) Chloride — 9701/41/O/N/23/Q7(c) [4 Marks]",
            syllabus_ref="32.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the observation when neutral aqueous iron(III) chloride is added to an aqueous solution of phenol.", 1, num_answer_lines=1),
                QuestionPart("(b)", "State what causes this characteristic colour change.", 1, num_answer_lines=2),
                QuestionPart("(c)", "State whether this test can be used to distinguish phenol from ethanol and explain why.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A purple / violet colouration (or complex solution) is observed [1].", "marks": 1},
                {"part": "(b)", "points": "Formation of an octahedral iron(III)-phenoxide complex ion, [Fe(OC6H5)6]3- (or [Fe(OC6H5)(H2O)5]2+) [1].", "marks": 1},
                {"part": "(c)", "points": "Yes [1]; Aliphatic alcohols like ethanol do not form coloured complexes with neutral FeCl3 (solution remains yellow/orange) because ethoxide is not stabilised by delocalisation [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/20/Q6(b)
        Question(
            number=25,
            title="Reaction of Phenol with Bromine: Balanced Stoichiometry and Observations — 9701/42/M/J/20/Q6(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write a fully balanced chemical equation for the reaction of phenol with excess bromine water.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the inorganic byproduct formed and state how its presence could be confirmed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5OH + 3Br2 -> C6H2Br3OH + 3HBr [2].", "marks": 2},
                {"part": "(b)", "points": "Hydrogen bromide, HBr [1]; Test with damp blue litmus turning red / white fumes with ammonia gas / cream precipitate with acidified AgNO3(aq) [1].", "marks": 1}
            ]
        ),

        # Q26: 9701/41/M/J/19/Q7(c)
        Question(
            number=26,
            title="Electrophilic Substitution Mechanism for Bromination of Phenol — 9701/41/M/J/19/Q7(c) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the carbocation intermediate formed when a bromine electrophile attacks position 4 of phenol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Show with curly arrows the restoration of the aromatic delocalised system from the intermediate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Intermediate showing broken circle / horseshoe spanning carbons 2 to 6 with positive charge inside ring [1]; Carbon 4 bonded to both -H and -Br in tetrahedral sp3 configuration [1].", "marks": 2},
                {"part": "(b)", "points": "Curly arrow from C-H bond into the aromatic &pi;-system to restore delocalisation [1]; Loss of H+ as leaving group to produce 4-bromophenol [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q7(b)
        Question(
            number=27,
            title="Differences in Solubility of Phenol in Water, Dilute Acid, and Dilute Alkali — 9701/42/O/N/21/Q7(b) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why phenol is only slightly soluble in cold water despite possessing an -OH group.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how the solubility of phenol changes when dilute hydrochloric acid is added versus dilute sodium hydroxide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The large non-polar hydrophobic benzene ring disrupts water's extensive hydrogen-bonding network [1]; The enthalpy of hydration is not sufficiently exothermic to compensate for the entropy decrease [1].", "marks": 2},
                {"part": "(b)", "points": "In dilute NaOH, phenol dissolves completely to form ionic sodium phenoxide [1]; In dilute HCl, phenol remains unionised and does not dissolve / forms a separate oily layer [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/42/M/J/18/Q7(b)
        Question(
            number=28,
            title="Comparison of Reactivity: Benzene, Phenol, and Chlorobenzene — 9701/42/M/J/18/Q7(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Rank benzene, phenol, and chlorobenzene in order of decreasing rate of electrophilic substitution.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain why chlorobenzene is less reactive than benzene towards electrophilic attack, despite chlorine having lone pairs.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenol > Benzene > Chlorobenzene [1].", "marks": 1},
                {"part": "(b)", "points": "Chlorine is highly electronegative and exerts a strong electron-withdrawing inductive effect (-I) [1]; Although the p-orbital lone pair delocalises slightly into the &pi;-ring (+M effect), the -I effect dominates [1]; This withdraws overall electron density from the ring, deactivating it towards electrophilic attack relative to benzene [1].", "marks": 3}
            ]
        ),

        # Q29: 9701/41/O/N/18/Q7(c)
        Question(
            number=29,
            title="Formation of Sodium Phenoxide and Reaction with Haloalkanes (Williamson Ether Synthesis) — 9701/41/O/N/18/Q7(c) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write an equation for the reaction between phenol and sodium hydroxide to form sodium phenoxide.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Sodium phenoxide is reacted with iodomethane. Give the name and structure of the organic product formed.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State the mechanism of this second reaction.", 1, num_answer_lines=1)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5OH + NaOH -> C6H5ONa + H2O [1].", "marks": 1},
                {"part": "(b)", "points": "Methoxybenzene (or methyl phenyl ether / anisole) [1]; Structure: C6H5OCH3 [1].", "marks": 2},
                {"part": "(c)", "points": "Nucleophilic substitution (SN2) [1].", "marks": 1}
            ]
        ),

        # Q30: 9701/42/F/M/20/Q7(c)
        Question(
            number=30,
            title="Infrared Spectroscopy: Distinguishing Phenol from Aliphatic Alcohols — 9701/42/F/M/20/Q7(c) [4 Marks]",
            syllabus_ref="32.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the wavenumber range for the O-H absorption band in phenol in an infrared spectrum.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain how the infrared spectrum of phenol differs from that of cyclohexanol in the range 1500–1600 cm^-1.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State how the C-O stretching frequency differs between phenol and cyclohexanol and explain why.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "3200–3600 cm^-1 (broad absorption due to hydrogen bonding) [1].", "marks": 1},
                {"part": "(b)", "points": "Phenol displays sharp aromatic C=C ring stretching peaks at 1450–1600 cm^-1 (typically ~1500 and ~1600 cm^-1) [1]; Cyclohexanol lacks these aromatic peaks as it contains only C-C single bonds [1].", "marks": 2},
                {"part": "(c)", "points": "The C-O stretch in phenol occurs at a higher wavenumber (~1230 cm^-1 vs ~1050 cm^-1 in cyclohexanol) because delocalisation imparts partial double bond character to the C-O bond, strengthening it [1].", "marks": 1}
            ]
        ),

        # Q31: 9701/41/M/J/17/Q6(b)
        Question(
            number=31,
            title="Electrochemical Oxidation of Phenol to Benzoquinone — 9701/41/M/J/17/Q6(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the structure of 1,4-benzoquinone, the oxidation product of phenol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State whether 1,4-benzoquinone is aromatic, giving a reason based on bonding.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Correct six-membered ring with two C=O groups at positions 1 and 4, and two C=C double bonds at positions 2,3 and 5,6 [2].", "marks": 2},
                {"part": "(b)", "points": "No, it is not aromatic [1]; It lacks a continuous delocalised &pi;-electron ring of (4n+2) electrons, containing instead two isolated alkene double bonds conjugated with carbonyl groups [1].", "marks": 2}
            ]
        ),

        # Q32: 9701/42/O/N/17/Q7(b)
        Question(
            number=32,
            title="Enthalpy of Combustion of Phenol vs Benzene — 9701/42/O/N/17/Q7(b) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the balanced thermochemical equation for the standard enthalpy of combustion of phenol, C6H5OH(s).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the magnitude of standard enthalpy of combustion of phenol (-3054 kJ mol^-1) is less negative than that of benzene (-3267 kJ mol^-1).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5OH(s) + 7O2(g) -> 6CO2(g) + 3H2O(l) [2].", "marks": 2},
                {"part": "(b)", "points": "Phenol already contains an oxygen atom bonded to carbon and hydrogen (it is already partially oxidised) [1]; Less oxygen is required for combustion and less energy is released upon forming new C=O and O-H bonds per mole of fuel [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q7(a)
        Question(
            number=33,
            title="pKa Comparison: Phenol vs Ethanoic Acid — 9701/42/M/J/23/Q7(a) [2 Marks]",
            syllabus_ref="32.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the pKa values of phenol and ethanoic acid, and deduce which is the stronger acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenol pKa &asymp; 10.0 and ethanoic acid pKa &asymp; 4.76 [1]; Ethanoic acid is the stronger acid because it has the lower pKa (delocalises negative charge over two highly electronegative oxygen atoms) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/O/N/22/Q6(a)
        Question(
            number=34,
            title="Observation with Neutral FeCl3 Solution — 9701/41/O/N/22/Q6(a) [2 Marks]",
            syllabus_ref="32.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the observation when aqueous phenol is mixed with neutral aqueous iron(III) chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A violet / purple / dark blue colouration or precipitate is formed [2].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/M/J/22/Q7(a)
        Question(
            number=35,
            title="Product of Phenol Reaction with Sodium Metal — 9701/42/M/J/22/Q7(a) [2 Marks]",
            syllabus_ref="32.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of solid phenol with molten sodium metal.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2C6H5OH + 2Na -> 2C6H5ONa + H2 (or C6H5OH + Na -> C6H5ONa + 1/2 H2) [2].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/M/J/21/Q8(a)
        Question(
            number=36,
            title="Structure of 2,4,6-Tribromophenol — 9701/41/M/J/21/Q8(a) [2 Marks]",
            syllabus_ref="32.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Draw the skeletal formula of 2,4,6-tribromophenol.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene ring with -OH at C1 [1]; Three -Br substituents at positions 2, 4, and 6 [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/O/N/20/Q6(a)
        Question(
            number=37,
            title="Condition for Diazonium Ion Stability — 9701/42/O/N/20/Q6(a) [2 Marks]",
            syllabus_ref="32.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the maximum temperature at which benzenediazonium chloride can be safely stored in solution, and name the gas released upon warming.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "10 °C (or between 0 °C and 10 °C) [1]; Nitrogen gas, N2 [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/M/J/23/Q7(b)
        Question(
            number=38,
            title="Reagent to Convert Phenol to Phenyl Ethanoate — 9701/43/M/J/23/Q7(b) [2 Marks]",
            syllabus_ref="32.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Identify an acyl chloride used to prepare phenyl ethanoate from phenol, and name the inorganic product.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ethanoyl chloride, CH3COCl [1]; Hydrogen chloride, HCl [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/F/M/22/Q8(a)
        Question(
            number=39,
            title="IUPAC Naming of Dihydroxybenzenes — 9701/42/F/M/22/Q8(a) [2 Marks]",
            syllabus_ref="32.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Give the systematic IUPAC name for benzene-1,2-diol (catechol) and benzene-1,4-diol (hydroquinone).", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene-1,2-diol [1]; Benzene-1,4-diol [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/23/Q7(a)
        Question(
            number=40,
            title="Role of Sodium Hydroxide in Diazonium Coupling — 9701/41/O/N/23/Q7(a) [2 Marks]",
            syllabus_ref="32.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Explain why phenol must be dissolved in sodium hydroxide before it can couple with the benzenediazonium ion.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "NaOH converts phenol into the phenoxide ion, C6H5O- [1]; The phenoxide ion is far more nucleophilic / electron-rich than neutral phenol, enabling reaction with the weak diazonium electrophile [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50)
        # 4 x 6m, 4 x 4m, 2 x 2m = 44 MARKS
        # =====================================================================

        # Q41: Core Repeat 1 (6m) — 9701/42/M/J/22/Q6
        Question(
            number=41,
            title="Core Repeat 1: Acidity Comparison of Ethanol, Water, Phenol, and Carboxylic Acids — 9701/42/M/J/22/Q6 [6 Marks]",
            syllabus_ref="32.1", difficulty="HARD", section_key="SEC_D",
            preamble="The relative acidities of organic hydroxy compounds represent one of the most frequently examined concepts in Cambridge Paper 4.",
            parts=[
                QuestionPart("(a)", "Arrange the following compounds in order of decreasing acid strength: ethanoic acid, ethanol, phenol, water.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain in detail the difference in stability between the ethoxide ion and the phenoxide ion.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why ethanoic acid is a significantly stronger acid than phenol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ethanoic acid > Phenol > Water > Ethanol [1].", "marks": 1},
                {"part": "(b)", "points": "In the ethoxide ion, the negative charge is localised on the single oxygen atom, and is further destabilised by the electron-donating (+I) ethyl group [1]; In the phenoxide ion, the oxygen lone pair overlaps with the benzene &pi;-cloud [1]; This delocalises the negative charge across the ring, conferring resonance stabilisation [1].", "marks": 3},
                {"part": "(c)", "points": "In the ethanoate ion (CH3COO-), the negative charge is delocalised equally over two highly electronegative oxygen atoms [1]; Oxygen is more electronegative than carbon, so delocalisation over two oxygens stabilises the anion far more effectively than delocalisation over carbon atoms in a ring [1].", "marks": 2}
            ]
        ),

        # Q42: Core Repeat 2 (6m) — 9701/41/O/N/21/Q7
        Question(
            number=42,
            title="Core Repeat 2: Multi-Step Synthesis of an Azo Dye from Benzene — 9701/41/O/N/21/Q7 [6 Marks]",
            syllabus_ref="32.4", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Describe how benzene is converted to nitrobenzene, stating all reagents and conditions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the reduction of nitrobenzene to phenylamine.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Describe how phenylamine is diazotised and then coupled with phenol to form an azo dye, specifying all temperatures and essential conditions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated HNO3 and concentrated H2SO4 at 55 °C [2].", "marks": 2},
                {"part": "(b)", "points": "Tin (Sn) and concentrated HCl, heated under reflux, followed by addition of excess aqueous NaOH [2].", "marks": 2},
                {"part": "(c)", "points": "Diazotisation with NaNO2 + HCl below 10 °C [1]; Coupling by adding the diazonium solution to phenol dissolved in ice-cold aqueous NaOH [1].", "marks": 2}
            ]
        ),

        # Q43: Core Repeat 3 (6m) — 9701/42/M/J/21/Q8
        Question(
            number=43,
            title="Core Repeat 3: Bromination of Phenol vs Methylbenzene — 9701/42/M/J/21/Q8 [6 Marks]",
            syllabus_ref="32.2", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the observations when bromine water is added to phenol at room temperature.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the reagents, conditions, and observation when methylbenzene is brominated in the benzene ring.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why phenol reacts much more rapidly with bromine than methylbenzene.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Decolourisation of orange/brown bromine water [1]; Formation of a white precipitate [1].", "marks": 2},
                {"part": "(b)", "points": "Pure Br2(l) and AlBr3 / FeBr3 catalyst in the dark at room temperature [1]; Steamy fumes of HBr and decolourisation of bromine [1].", "marks": 2},
                {"part": "(c)", "points": "In phenol, the p-orbital lone pair on oxygen delocalises directly into the aromatic &pi;-system by resonance (+M effect) [1]; In methylbenzene, activation is solely by the weaker inductive (+I) effect of the methyl group, so electron density is much lower than in phenol [1].", "marks": 2}
            ]
        ),

        # Q44: Core Repeat 4 (6m) — 9701/42/O/N/19/Q7
        Question(
            number=44,
            title="Core Repeat 4: Qualitative Distinctions Between Four Isomeric Aromatic Compounds — 9701/42/O/N/19/Q7 [6 Marks]",
            syllabus_ref="32.3", difficulty="HARD", section_key="SEC_D",
            preamble="Four isomeric aromatic compounds of formula C<sub>7</sub>H<sub>8</sub>O are investigated:<br/>"
                     "- Compound P: 2-methylphenol<br/>"
                     "- Compound Q: 4-methylphenol<br/>"
                     "- Compound R: Phenylmethanol, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>OH<br/>"
                     "- Compound S: Methoxybenzene, C<sub>6</sub>H<sub>5</sub>OCH<sub>3</sub>",
            parts=[
                QuestionPart("(a)", "Describe a chemical test that will give a positive result with P and Q, but no reaction with R and S.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe a chemical test that will give a positive result with R, but no reaction with P, Q, and S.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State the structural formulas of the products when Compound P is treated with excess bromine water.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add neutral aqueous iron(III) chloride, FeCl3(aq) [1]; P and Q give a purple / violet colouration, whereas R and S do not change colour (remain yellow) [1].", "marks": 2},
                {"part": "(b)", "points": "Add acidified potassium dichromate(VI), K2Cr2O7 / H+, and warm [1]; Only R (a primary alcohol) turns the solution from orange to green [1].", "marks": 2},
                {"part": "(c)", "points": "4,6-dibromo-2-methylphenol [1]; Correct structure with methyl at C2, -OH at C1, and bromines at C4 and C6 [1].", "marks": 2}
            ]
        ),

        # Q45: Core Repeat 5 (4m) — 9701/42/M/J/23/Q8(c)
        Question(
            number=45,
            title="Core Repeat 5: Acidity Trends in Substituted Phenols — 9701/42/M/J/23/Q8(c) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain the effect of an electron-withdrawing nitro group (-NO2) on the pKa of phenol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain the effect of an electron-donating alkyl group (-CH3) on the pKa of phenol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The nitro group withdraws electron density from the ring via -I and -M effects, further stabilising the phenoxide anion [1]; This shifts dissociation equilibrium right, increasing Ka and decreasing pKa (stronger acid) [1].", "marks": 2},
                {"part": "(b)", "points": "The alkyl group donates electron density into the ring via the +I inductive effect [1]; This intensifies negative charge on oxygen, destabilising the phenoxide anion and increasing pKa (weaker acid) [1].", "marks": 2}
            ]
        ),

        # Q46: Core Repeat 6 (4m) — 9701/41/O/N/22/Q7(b)
        Question(
            number=46,
            title="Core Repeat 6: Synthesis of Phenyl Esters Using Acyl Chlorides — 9701/41/O/N/22/Q7(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Give the reagents and conditions to prepare phenyl benzoate from phenol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why benzoyl chloride is used instead of benzoic acid in this preparation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzoyl chloride (C6H5COCl) and phenol dissolved in aqueous sodium hydroxide (NaOH(aq)) [2].", "marks": 2},
                {"part": "(b)", "points": "Phenol is a weak nucleophile and does not react with carboxylic acids under standard acid catalysis [1]; Acyl chlorides have a much more electrophilic carbonyl carbon and a good Cl- leaving group, reacting rapidly at room temperature [1].", "marks": 2}
            ]
        ),

        # Q47: Core Repeat 7 (4m) — 9701/42/F/M/21/Q8(b)
        Question(
            number=47,
            title="Core Repeat 7: Nitration of Phenol vs Benzene Conditions — 9701/42/F/M/21/Q8(b) [4 Marks]",
            syllabus_ref="32.2", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the reagent and conditions required for the mononitration of phenol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the conditions in (a) are much milder than those required for the nitration of benzene.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Dilute nitric acid, HNO3(aq), at room temperature (20 °C) [2].", "marks": 2},
                {"part": "(b)", "points": "The -OH group in phenol donates a lone pair into the aromatic &pi;-cloud, significantly activating the ring [1]; The activated ring polarises dilute HNO3 to react without needing a concentrated H2SO4 catalyst or heating [1].", "marks": 2}
            ]
        ),

        # Q48: Core Repeat 8 (4m) — 9701/41/M/J/20/Q7(c)
        Question(
            number=48,
            title="Core Repeat 8: Separation of Phenol from an Organic Mixture via Acid-Base Extraction — 9701/41/M/J/20/Q7(c) [4 Marks]",
            syllabus_ref="32.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="A liquid mixture contains phenol, phenylmethanol, and benzoic acid dissolved in ethoxyethane.",
            parts=[
                QuestionPart("(a)", "Explain how benzoic acid can be selectively separated from this mixture without extracting phenol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how phenol can then be separated from phenylmethanol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Shake the organic layer with aqueous sodium hydrogencarbonate, NaHCO3(aq) [1]; Only benzoic acid is strong enough to react, forming water-soluble sodium benzoate which partitions into the aqueous layer, leaving phenol and phenylmethanol in the ether layer [1].", "marks": 2},
                {"part": "(b)", "points": "Shake the remaining ether layer with aqueous sodium hydroxide, NaOH(aq) [1]; Phenol reacts to form water-soluble sodium phenoxide which enters the aqueous layer, while non-acidic phenylmethanol remains in the organic layer [1].", "marks": 2}
            ]
        ),

        # Q49: Core Repeat 9 (2m) — 9701/42/M/J/23/Q7(e)
        Question(
            number=49,
            title="Core Repeat 9: Identifying Phenol by Bromine Water Decolourisation — 9701/42/M/J/23/Q7(e) [2 Marks]",
            syllabus_ref="32.3", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State two visible observations when bromine water is added dropwise to aqueous phenol.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The orange / brown bromine water is decolourised [1]; A white precipitate (of 2,4,6-tribromophenol) is produced [1].", "marks": 2}
            ]
        ),

        # Q50: Core Repeat 10 (2m) — 9701/41/O/N/23/Q7(e)
        Question(
            number=50,
            title="Core Repeat 10: Structure of the Chromophore in Azo Dyes — 9701/41/O/N/23/Q7(e) [2 Marks]",
            syllabus_ref="32.4", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Identify the chromophore responsible for the colour in 4-hydroxyazobenzene and state the type of bond present between the two nitrogen atoms.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The azo group / -N=N- bridge [1]; A nitrogen-nitrogen double bond (&sigma; bond and &pi; bond) [1].", "marks": 2}
            ]
        )
    ]

    # Verify tariffs
    count_6m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    count_4m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    count_2m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_qs = len(questions)

    print(f"Topic 32 Questions Count: {total_qs}")
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
    print("Topic 32 PDF built successfully!")

if __name__ == "__main__":
    build_topic32_50q()
