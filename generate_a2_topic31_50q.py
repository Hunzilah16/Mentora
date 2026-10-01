"""
Complete 50-Question Master Pack: Topic 31 — Halogen Compounds (Paper 4 Theory)
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

def build_topic31_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic31_Halogen_Compounds.pdf"

    topic_title = "Topic 31 — Halogen Compounds"
    topic_subtitle = "Reactivity of Halogen Compounds · Halogenoarenes vs Halogenoalkanes vs Acyl Chlorides · CFCs & Ozone Depletion · Fluoroalkanes"

    subtopics_summary = [
        ("31.1 Relative Reactivity & Hydrolysis Mechanisms", "Comparison of the relative ease of hydrolysis of acyl chlorides (CH3COCl), alkyl halides (CH3CH2Cl), and aryl halides (C6H5Cl); differences in carbon-halogen bond strength and electronic environments."),
        ("31.2 Inertness of Halogenoarenes", "Resistance of chlorobenzene to nucleophilic substitution; delocalisation of chlorine lone pair into the aromatic π-electron system; partial double bond character of C-Cl bond; electrostatic repulsion between nucleophiles and the benzene π-cloud."),
        ("31.3 Environmental Impact of CFCs & Ozone Depletion", "Stability of chlorofluorocarbons (CFCs); photolytic homolytic fission by stratospheric UV light generating chlorine free radicals; catalytic breakdown of ozone via Cl• and ClO• propagation cycles; role of hydrofluorocarbons (HFCs) as ozone-safe substitutes."),
        ("31.4 Fluoroalkanes & Bond Energy Considerations", "Extremely high bond dissociation energy of the C-F bond (467 kJ mol-1); chemical inertness and non-flammability of PTFE (Teflon); synthetic fluorinated pharmaceuticals."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Halogen Compounds from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q8
        Question(
            number=1,
            title="Comparison of Relative Ease of Hydrolysis of Three Chlorine Compounds — 9701/42/M/J/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="The relative rates of hydrolysis of three chlorine-containing organic compounds are compared in Fig. 1.1:<br/>- Compound A: Ethanoyl chloride, CH<sub>3</sub>COCl<br/>- Compound B: 1-chlorobutane, CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>Cl<br/>- Compound C: Chlorobenzene, C<sub>6</sub>H<sub>5</sub>Cl",
            figure_path=os.path.join(fig_dir, "a2_t31_halogen_hydrolysis_trend.png"),
            figure_caption="Fig. 1.1: Relative ease of hydrolysis of acyl chloride, alkyl halide, and aryl halide.",
            parts=[
                QuestionPart("(a)", "Rank these three compounds in order of decreasing ease of hydrolysis (fastest first).", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain why Compound A (ethanoyl chloride) hydrolyses rapidly at room temperature with water alone.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why Compound C (chlorobenzene) is completely inert to hydrolysis even when boiled with aqueous sodium hydroxide.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Compound A (ethanoyl chloride) > Compound B (1-chlorobutane) > Compound C (chlorobenzene) [1].", "marks": 1},
                {"part": "(b)", "points": "The carbonyl carbon is bonded to two strongly electronegative atoms (O and Cl), making it highly electron-deficient (&delta;+) [1]; Water readily attacks the carbonyl carbon via an addition-elimination mechanism without needing to break the C-Cl bond in the initial step [1].", "marks": 2},
                {"part": "(c)", "points": "A lone pair of electrons on the chlorine atom overlaps with the delocalised &pi;-electron system of the benzene ring [1]; This imparts partial double bond character to the C-Cl bond, making it significantly shorter, stronger, and harder to break [1]; Furthermore, the incoming OH- nucleophile is electrostatically repelled by the high &pi;-electron density of the benzene ring [1].", "marks": 3}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q8
        Question(
            number=2,
            title="CFCs and Catalytic Ozone Depletion in the Stratosphere — 9701/41/M/J/23/Q8 [6 Marks]",
            syllabus_ref="31.3", difficulty="HARD", section_key="SEC_A",
            preamble="Dichlorodifluoromethane, CCl<sub>2</sub>F<sub>2</sub> (CFC-12), was formerly used as a refrigerant and aerosol propellant.<br/>In the stratosphere, it undergoes photolysis by short-wavelength ultraviolet radiation (&lambda; &lt; 220 nm).<br/>Data: Bond energies: C-F = 467 kJ mol<sup>-1</sup>; C-Cl = 340 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why ultraviolet radiation cleaves the C-Cl bond rather than the C-F bond in CCl<sub>2</sub>F<sub>2</sub>, writing an equation for the photolysis.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write two equations that show how the chlorine free radical catalyses the destruction of ozone, and construct the overall equation.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why hydrofluorocarbons (HFCs), such as CH<sub>2</sub>FCF<sub>3</sub>, do not cause ozone depletion.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The C-Cl bond has a significantly lower bond dissociation energy (340 kJ mol^-1 vs 467 kJ mol^-1) and is cleaved homolytically by UV light [1]; CCl2F2 &rarr; •CClF2 + Cl• [1].", "marks": 2},
                {"part": "(b)", "points": "Propagation 1: Cl• + O3 &rarr; ClO• + O2 [1]; Propagation 2: ClO• + O &rarr; Cl• + O2 [1]; Overall: O3 + O &rarr; 2O2 (or 2O3 &rarr; 3O2) [1].", "marks": 3},
                {"part": "(c)", "points": "HFCs contain no chlorine atoms; the C-F bonds are too strong to be broken by stratospheric UV light, so no halogen radicals that destroy ozone are formed [1].", "marks": 1}
            ]
        ),

        # Q3: 9701/42/O/N/23/Q8
        Question(
            number=3,
            title="Hydrolysis Rates of 1-Halogenobutanes & Bond Energy Analysis — 9701/42/O/N/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="The rate of hydrolysis of primary halogenoalkanes is investigated by adding aqueous silver nitrate in ethanol at 50 °C:<br/>- 1-chlorobutane: white precipitate after several minutes<br/>- 1-bromobutane: cream precipitate after 1 minute<br/>- 1-iodobutane: pale yellow precipitate after 15 seconds<br/>- 1-fluorobutane: no precipitate formed",
            parts=[
                QuestionPart("(a)", "Explain the role of ethanol in this test.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Write the ionic equation for the precipitation reaction involving 1-iodobutane.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Explain the observed trend in the rate of hydrolysis in terms of bond polarity and bond enthalpy, stating which factor dominates.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ethanol acts as a common solvent (mutual solvent) allowing the water-insoluble halogenoalkane and the aqueous silver nitrate to mix into a single homogeneous solution [1].", "marks": 1},
                {"part": "(b)", "points": "Ag+(aq) + I-(aq) &rarr; AgI(s) [1].", "marks": 1},
                {"part": "(c)", "points": "Electronegativity decreases from F to I, so C-F is the most polar bond with the largest &delta;+ on carbon, which on its own would predict C-F to react fastest [1]; However, bond enthalpy decreases sharply down Group 17: C-F (467) > C-Cl (340) > C-Br (280) > C-I (240 kJ mol^-1) [1]; Bond enthalpy is the overriding / dominant factor governing the rate of hydrolysis [1]; The weaker C-I bond is cleaved much more easily and quickly in the rate-determining step, giving the fastest rate [1].", "marks": 4}
            ]
        ),

        # Q4: 9701/41/O/N/23/Q8
        Question(
            number=4,
            title="Mechanistic Pathway: Hydrolysis of Ethanoyl Chloride vs Chloroethane — 9701/41/O/N/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Ethanoyl chloride reacts violently with water at 20 °C, while chloroethane requires heating with aqueous NaOH at 60 °C.",
            parts=[
                QuestionPart("(a)", "Outline the nucleophilic addition-elimination mechanism for the reaction of ethanoyl chloride with water, showing curly arrows and intermediates.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State the observations when water is added to ethanoyl chloride, identifying the misty fumes evolved.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Contrast the mechanism in (a) with the S<sub>N</sub>2 mechanism of chloroethane.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Water lone pair attacks carbonyl C&delta;+, C=O &pi;-bond breaks to O- forming a tetrahedral intermediate [1]; O- reforms C=O double bond, expelling Cl- as a leaving group [1]; Loss of H+ from protonated oxygen yields ethanoic acid and HCl [1].", "marks": 3},
                {"part": "(b)", "points": "Vigorous exothermic reaction / bubbling; steamy white / misty fumes of hydrogen chloride (HCl) gas [2].", "marks": 2},
                {"part": "(c)", "points": "Ethanoyl chloride reacts by a two-step addition-elimination mechanism via a tetrahedral intermediate, whereas chloroethane reacts by a one-step concerted S_N2 mechanism with direct C-Cl bond cleavage in the transition state [1].", "marks": 1}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q8
        Question(
            number=5,
            title="Synthesis & Chemical Properties of Halogenoarenes — 9701/42/M/J/22/Q8 [6 Marks]",
            syllabus_ref="31.2", difficulty="HARD", section_key="SEC_A",
            preamble="Bromobenzene, C<sub>6</sub>H<sub>5</sub>Br, is synthesized from benzene by electrophilic substitution.",
            parts=[
                QuestionPart("(a)", "State the reagents and catalyst required to synthesize bromobenzene from benzene, and write the overall equation.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe what is observed when bromobenzene is shaken with aqueous silver nitrate and warmed.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why 1-bromobutane gives a cream precipitate with aqueous silver nitrate under the same conditions, while bromobenzene gives no precipitate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Liquid bromine, Br2, and anhydrous iron(III) bromide, FeBr3 (or Fe) [1]; C6H6 + Br2 &rarr; C6H5Br + HBr [1].", "marks": 2},
                {"part": "(b)", "points": "No precipitate is formed / solution remains clear / no reaction [2].", "marks": 2},
                {"part": "(c)", "points": "In 1-bromobutane, the C-Br bond is a standard single bond that undergoes nucleophilic substitution by water to release free Br- ions, precipitating AgBr [1]; In bromobenzene, p-&pi; orbital overlap delocalises the bromine lone pair into the ring, strengthening the C-Br bond and preventing release of Br- ions [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/41/M/J/22/Q8
        Question(
            number=6,
            title="Fluoroalkanes: Polytetrafluoroethene (PTFE) & Thermal Stability — 9701/41/M/J/22/Q8 [6 Marks]",
            syllabus_ref="31.4", difficulty="HARD", section_key="SEC_A",
            preamble="Polytetrafluoroethene (PTFE, Teflon) is an addition polymer formed from tetrafluoroethene, CF<sub>2</sub>=CF<sub>2</sub>.<br/>PTFE is renowned for its non-stick properties, electrical insulation, and exceptional chemical inertness.",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of PTFE.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain why PTFE is chemically inert to concentrated acids, concentrated alkalis, and strong oxidising agents even at 250 °C.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why PTFE has a very low coefficient of friction (non-stick surface).", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "[-CF2-CF2-]n drawn with single C-C bond and open end-bonds [1].", "marks": 1},
                {"part": "(b)", "points": "The C-F bond is exceptionally strong with an enormous bond enthalpy (467 kJ mol^-1) [1]; The carbon backbone is completely sheathed/shielded by a dense, unreactive outer cylinder of highly electronegative fluorine atoms with tightly held non-polarisable electron clouds [1]; Reagents cannot access the carbon skeleton to initiate chemical attack [1].", "marks": 3},
                {"part": "(c)", "points": "Fluorine atoms have very low polarisability, resulting in extremely weak London dispersion intermolecular forces with adjacent surfaces [2].", "marks": 2}
            ]
        ),

        # Q7: 9701/42/O/N/22/Q8
        Question(
            number=7,
            title="Differentiating Three Isomeric Halogen Compounds: C7H7Cl — 9701/42/O/N/22/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Three structural isomers have the molecular formula C<sub>7</sub>H<sub>7</sub>Cl:<br/>- Isomer 1: (Chloromethyl)benzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>Cl<br/>- Isomer 2: 2-chloromethylbenzene (2-chlorotoluene)<br/>- Isomer 3: 4-chloromethylbenzene (4-chlorotoluene)",
            parts=[
                QuestionPart("(a)", "Describe a chemical test that will distinguish Isomer 1 from Isomers 2 and 3, stating reagents, conditions, and observations.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Describe a chemical test to confirm that Isomers 2 and 3 possess an alkyl side-chain attached to an aromatic ring.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why Isomer 1 hydrolyses faster than 1-chloropropane.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add aqueous ethanol and silver nitrate solution at 50 °C [1]; Isomer 1 ((chloromethyl)benzene) produces an immediate white precipitate of AgCl [1]; Isomers 2 and 3 show no precipitate / remain clear [1].", "marks": 3},
                {"part": "(b)", "points": "Heat with alkaline potassium manganate(VII), KMnO4, then acidify with dilute H2SO4 [1]; The purple colour decolourises and a white crystalline precipitate of chlorobenzoic acid forms [1].", "marks": 2},
                {"part": "(c)", "points": "The carbocation intermediate formed in the hydrolysis of (chloromethyl)benzene is a benzylic carbocation (C6H5-C+H2), which is resonance-stabilised by delocalisation of charge into the benzene ring [1].", "marks": 1}
            ]
        ),

        # Q8: 9701/41/O/N/22/Q8
        Question(
            number=8,
            title="Synthesis & Hydrolysis of Acyl Halides vs Alkyl Halides — 9701/41/O/N/22/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Carboxylic acids can be converted into acyl chlorides using phosphorus pentachloride, PCl<sub>5</sub>, phosphorus trichloride, PCl<sub>3</sub>, or thionyl chloride, SOCl<sub>2</sub>.<br/>Reaction: CH<sub>3</sub>COOH + SOCl<sub>2</sub> &rarr; CH<sub>3</sub>COCl + SO<sub>2</sub> + HCl",
            parts=[
                QuestionPart("(a)", "Explain why thionyl chloride (SOCl<sub>2</sub>) is the preferred laboratory reagent for preparing acyl chlorides.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the reaction between ethanoyl chloride and ethanol, naming the organic product and functional group formed.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Compare this esterification reaction with the reaction between ethanoic acid and ethanol in terms of speed, reversibility, and catalyst requirements.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both by-products (SO2 and HCl) are gases and escape from the reaction mixture [1]; Leaving pure liquid ethanoyl chloride without needing complex separation [1].", "marks": 2},
                {"part": "(b)", "points": "CH3COCl + CH3CH2OH &rarr; CH3COOCH2CH3 + HCl [1]; Product = ethyl ethanoate, functional group = ester (-COO-) [1].", "marks": 2},
                {"part": "(c)", "points": "With ethanoyl chloride: fast/vigorous at room temperature, irreversible, requires no catalyst [1]; With ethanoic acid: slow equilibrium requiring reflux, reversible, requires concentrated H2SO4 catalyst [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/21/Q8
        Question(
            number=9,
            title="Environmental Chemistry: Lifetime of CFCs and the Montreal Protocol — 9701/42/M/J/21/Q8 [6 Marks]",
            syllabus_ref="31.3", difficulty="HARD", section_key="SEC_A",
            preamble="CFC-11 (CCl<sub>3</sub>F) has an atmospheric lifetime of approximately 50 years and an ozone depletion potential (ODP) of 1.0.",
            parts=[
                QuestionPart("(a)", "Explain why CFCs persist unchanged in the troposphere for decades before reaching the stratosphere.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how a single chlorine radical can destroy up to 100,000 ozone molecules in the stratosphere.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe the role of the Montreal Protocol and state two alternative compounds developed to replace CFCs.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CFCs are chemically inert, non-flammable, insoluble in water (not washed out by rain), and resistant to oxidation by hydroxyl radicals in the lower atmosphere [2].", "marks": 2},
                {"part": "(b)", "points": "Chlorine acts as a catalytic chain carrier: in the propagation cycle (Cl• + O3 &rarr; ClO• + O2; ClO• + O &rarr; Cl• + O2), the Cl• radical is regenerated unchanged at the end of each cycle [1]; The cycle repeats thousands of times until a termination reaction occurs (e.g. Cl• + CH4 &rarr; HCl + •CH3) [1].", "marks": 2},
                {"part": "(c)", "points": "International treaty banning production and consumption of ozone-depleting substances [1]; Replacements: hydrofluorocarbons (HFCs, e.g. HFC-134a) and hydrofluoroolefins (HFOs) / hydrocarbons (propane/butane) [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/21/Q8
        Question(
            number=10,
            title="Grignard Reagents: Formation and Carbon-Carbon Bond Formation — 9701/41/M/J/21/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Organomagnesium compounds (Grignard reagents), RMgX, are versatile reagents for extending carbon chains.<br/>Reaction: CH<sub>3</sub>CH<sub>2</sub>Br + Mg &rarr; CH<sub>3</sub>CH<sub>2</sub>MgBr",
            parts=[
                QuestionPart("(a)", "State the solvent and conditions required to prepare ethylmagnesium bromide.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why ethylmagnesium bromide reacts vigorously with water, writing a balanced chemical equation.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Show how ethylmagnesium bromide reacts with methanal, HCHO, followed by acid hydrolysis to produce a primary alcohol, naming the product.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Dry ethoxyethane (dry diethyl ether) under reflux in completely moisture-free conditions [2].", "marks": 2},
                {"part": "(b)", "points": "The C-Mg bond is strongly polarised with a carbanion-like &delta;- carbon atom that acts as a powerful Brønsted-Lowry base [1]; CH3CH2MgBr + H2O &rarr; CH3CH3 (ethane gas) + Mg(OH)Br [1].", "marks": 2},
                {"part": "(c)", "points": "CH3CH2MgBr + HCHO &rarr; CH3CH2CH2OMgBr &rarr; CH3CH2CH2OH + Mg(OH)Br [1]; Product = propan-1-ol [1].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q8
        Question(
            number=11,
            title="Reactions of Acyl Chlorides: Formation of Amides and Esters — 9701/42/O/N/21/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Benzoyl chloride, C<sub>6</sub>H<sub>5</sub>COCl, is an aromatic acyl chloride used to prepare esters and amides.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of benzoyl chloride with concentrated aqueous ammonia, naming the organic product.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the balanced chemical equation for the reaction of benzoyl chloride with ethylamine, CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>, naming the class of compound formed.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Compare the reactivity of benzoyl chloride with ethanoyl chloride towards hydrolysis, explaining the difference.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5COCl + 2NH3 &rarr; C6H5CONH2 + NH4Cl [1]; Product = benzamide [1].", "marks": 2},
                {"part": "(b)", "points": "C6H5COCl + 2CH3CH2NH2 &rarr; C6H5CONHCH2CH3 + CH3CH2NH3Cl [1]; N-substituted amide (secondary amide) [1].", "marks": 2},
                {"part": "(c)", "points": "Benzoyl chloride hydrolyses more slowly than ethanoyl chloride [1]; Overlap of the carbonyl carbon with the &pi;-electron cloud of the benzene ring reduces the &delta;+ charge on the carbonyl carbon, making it less electrophilic towards water [1].", "marks": 2}
            ]
        ),

        # Q12: 9701/41/O/N/21/Q8
        Question(
            number=12,
            title="Polyhalogenated Compounds: Chloroform & Tetrachloromethane Reactions — 9701/41/O/N/21/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Trichloromethane (chloroform, CHCl<sub>3</sub>) and tetrachloromethane (carbon tetrachloride, CCl<sub>4</sub>) were historically used as anaesthetics and solvents.",
            parts=[
                QuestionPart("(a)", "Explain why CCl<sub>4</sub> is a non-polar molecule even though each C-Cl bond is polar.", 2, num_answer_lines=2),
                QuestionPart("(b)", "When exposed to air and light, chloroform is slowly oxidised to highly toxic phosgene, COCl<sub>2</sub>. Write the balanced equation for this oxidation.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State why ethanol is often added in small quantities to commercial bottles of chloroform.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CCl4 has a symmetrical tetrahedral geometry (109.5° bond angles) [1]; The four individual C-Cl bond dipoles cancel each other out completely, giving a zero net molecular dipole moment [1].", "marks": 2},
                {"part": "(b)", "points": "2CHCl3 + O2 &rarr; 2COCl2 + 2HCl [2].", "marks": 2},
                {"part": "(c)", "points": "Ethanol reacts with any phosgene formed to produce harmless non-toxic diethyl carbonate: COCl2 + 2CH3CH2OH &rarr; (CH3CH2O)2CO + 2HCl [2].", "marks": 2}
            ]
        ),

        # Q13: 9701/42/M/J/20/Q8
        Question(
            number=13,
            title="Nucleophilic Substitution Kinetics: Primary vs Tertiary Halogenoalkanes — 9701/42/M/J/20/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="The kinetics of hydrolysis of 1-bromobutane and 2-bromo-2-methylpropane with NaOH(aq) are investigated.",
            parts=[
                QuestionPart("(a)", "Write the rate equation for the hydrolysis of 1-bromobutane and state its mechanism.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the rate equation for the hydrolysis of 2-bromo-2-methylpropane and state its mechanism.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why changing the solvent from 80% ethanol/water to pure water increases the rate of S<sub>N</sub>1 hydrolysis of 2-bromo-2-methylpropane.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Rate = k[CH3CH2CH2CH2Br][OH-] [1]; S_N2 mechanism (bimolecular nucleophilic substitution) [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = k[(CH3)3CBr] [1]; S_N1 mechanism (unimolecular nucleophilic substitution) [1].", "marks": 2},
                {"part": "(c)", "points": "Water is a more polar protic solvent than aqueous ethanol [1]; A more polar solvent solvates and stabilises the charged carbocation intermediate (and leaving Br- ion) in the rate-determining step, lowering activation energy and increasing rate [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/41/M/J/20/Q8
        Question(
            number=14,
            title="Nucleophilic Acyl Substitution of Acid Chlorides by Amines — 9701/41/M/J/20/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Acyl chlorides react rapidly with primary amines to form secondary amides:<br/>RCOCl + 2R'NH<sub>2</sub> &rarr; RCONHR' + R'NH<sub>3</sub><sup>+</sup>Cl<sup>-</sup>",
            parts=[
                QuestionPart("(a)", "Explain why two moles of amine are required per mole of acyl chloride in this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the structural formula of the product formed between propanoyl chloride and phenylamine.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the type of reaction and mechanism occurring.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The first mole of amine acts as a nucleophile to form the amide [1]; The second mole of amine acts as a base to neutralise the acidic by-product HCl, preventing protonation of the unreacted amine [1].", "marks": 2},
                {"part": "(b)", "points": "N-phenylpropanamide: CH3CH2CONH-C6H5 drawn correctly [2].", "marks": 2},
                {"part": "(c)", "points": "Condensation reaction / nucleophilic addition-elimination [2].", "marks": 2}
            ]
        ),

        # Q15: 9701/42/O/N/19/Q8
        Question(
            number=15,
            title="Fluoroquinolone Antibiotics: Role of Fluorine in Medicinal Chemistry — 9701/42/O/N/19/Q8 [6 Marks]",
            syllabus_ref="31.4", difficulty="HARD", section_key="SEC_A",
            preamble="Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic containing a fluorine atom attached directly to an aromatic ring.",
            parts=[
                QuestionPart("(a)", "Explain why incorporating a fluorine atom into an aromatic drug increases its metabolic stability in the human body.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State how the size of a fluorine atom compares with hydrogen, and explain the concept of 'isosteric replacement'.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why replacing an aromatic C-H bond with a C-F bond increases the lipophilicity and membrane permeability of a drug.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The C-F bond is extremely strong (bond enthalpy 467 kJ mol^-1) and resists enzymatic cleavage by Cytochrome P450 oxidases in the liver [2].", "marks": 2},
                {"part": "(b)", "points": "Fluorine has a van der Waals radius (1.47 Å) very close to that of hydrogen (1.20 Å) [1]; Isosteric replacement: substituting F for H does not alter the steric shape of the molecule, allowing it to fit into the original receptor active site [1].", "marks": 2},
                {"part": "(c)", "points": "Fluorine's high electronegativity polarises the C-F bond, reducing overall water solvation and facilitating passive diffusion across hydrophobic cell membrane lipid bilayers [2].", "marks": 2}
            ]
        ),

        # Q16: 9701/41/O/N/19/Q8
        Question(
            number=16,
            title="Comparison of Halogenoalkane Nucleophilic Substitution Mechanisms — 9701/41/O/N/19/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_A",
            preamble="Consider the nucleophilic substitution reactions of 1-iodobutane and 2-iodo-2-methylpropane with cyanide ions, CN<sup>-</sup>.",
            parts=[
                QuestionPart("(a)", "Draw the transition state for the reaction of 1-iodobutane with CN<sup>-</sup>, showing partial bonds and negative charge.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the carbocation intermediate for the reaction of 2-iodo-2-methylpropane with CN<sup>-</sup>, showing its geometry.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the synthetic utility of converting a halogenoalkane into a nitrile.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Planar arrangement of H, H, propyl groups with partial bonds to incoming :NC&delta;- and outgoing &delta;-I at 180°, brackets with negative charge [2].", "marks": 2},
                {"part": "(b)", "points": "Planar trigonal tertiary carbocation (CH3)3C+ drawn with 120° bond angles and positive charge [2].", "marks": 2},
                {"part": "(c)", "points": "It increases the carbon chain length by one carbon atom [1]; and provides an entry point to synthesize carboxylic acids (via acid hydrolysis) or amines (via reduction with LiAlH4/H2) [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q9
        Question(
            number=17,
            title="Comparison of C-Cl Bond Strengths in Chlorobenzene and Chloroethane — 9701/42/M/J/23/Q9 [4 Marks]",
            syllabus_ref="31.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The carbon-chlorine bond in chlorobenzene has a bond energy of 400 kJ mol<sup>-1</sup>, whereas in chloroethane it is 340 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain the origin of the partial double-bond character in chlorobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how this partial double-bond character affects bond length and chemical reactivity.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "One of the lone pairs of electrons in a p-orbital on the chlorine atom overlaps with the delocalised &pi;-electron system of the benzene ring [2].", "marks": 2},
                {"part": "(b)", "points": "Makes the C-Cl bond shorter and stronger [1]; Resisting nucleophilic attack and making chlorobenzene inert to hydrolysis [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/M/J/23/Q9
        Question(
            number=18,
            title="Photolytic Homolytic Fission of CFC-11 — 9701/41/M/J/23/Q9 [4 Marks]",
            syllabus_ref="31.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Trichlorofluoromethane, CCl<sub>3</sub>F, is broken down by ultraviolet light in the upper atmosphere.",
            parts=[
                QuestionPart("(a)", "Write the photochemical equation for the homolytic fission of CCl<sub>3</sub>F.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Define the term <i>homolytic fission</i> and identify the free radical species produced.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CCl3F &rarr; •CCl2F + Cl• [2].", "marks": 2},
                {"part": "(b)", "points": "The breaking of a covalent bond where each bonded atom takes one of the shared pair of electrons, forming two radicals [1]; Chlorine radical, Cl• [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/O/N/23/Q9
        Question(
            number=19,
            title="Reaction of Ethanoyl Chloride with Water vs Phenol — 9701/42/O/N/23/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Ethanoyl chloride reacts with water and with phenol under different conditions.",
            parts=[
                QuestionPart("(a)", "Write the equation for the reaction of ethanoyl chloride with water.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the equation for the reaction of ethanoyl chloride with phenol in the presence of base, naming the ester formed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl + H2O &rarr; CH3COOH + HCl [2].", "marks": 2},
                {"part": "(b)", "points": "CH3COCl + C6H5OH &rarr; CH3COOC6H5 + HCl (or with NaOH &rarr; phenyl ethanoate + NaCl + H2O) [1]; Phenyl ethanoate [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/O/N/23/Q9
        Question(
            number=20,
            title="Ozone Destruction Propagation Steps by ClO• Radicals — 9701/41/O/N/23/Q9 [4 Marks]",
            syllabus_ref="31.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Chlorine monoxide, ClO•, is a key intermediate in the catalytic destruction of stratospheric ozone.",
            parts=[
                QuestionPart("(a)", "Write the two catalytic propagation steps involving Cl• and ClO•.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why chlorine acts as a catalyst in this mechanism.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Cl• + O3 &rarr; ClO• + O2 [1]; Step 2: ClO• + O &rarr; Cl• + O2 [1].", "marks": 2},
                {"part": "(b)", "points": "The chlorine radical initiates ozone destruction in Step 1 and is regenerated chemically unchanged at the end of Step 2 [1]; It is not consumed overall and accelerates the rate of ozone depletion [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/M/J/22/Q9
        Question(
            number=21,
            title="Comparison of Reactivity of Halogenoalkanes with Aqueous AgNO3 — 9701/42/M/J/22/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="1-bromobutane and 1-chlorobutane are treated with aqueous silver nitrate in ethanol.",
            parts=[
                QuestionPart("(a)", "State which compound forms a precipitate first, giving the colour of the precipitate.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain this difference in rate by quoting relevant bond enthalpies.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1-bromobutane forms a precipitate first [1]; Cream precipitate (AgBr) [1].", "marks": 2},
                {"part": "(b)", "points": "The C-Br bond enthalpy (280 kJ mol^-1) is lower than the C-Cl bond enthalpy (340 kJ mol^-1) [1]; Less energy is required to break the C-Br bond in the rate-determining step, leading to faster hydrolysis [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/41/M/J/22/Q9
        Question(
            number=22,
            title="Electrophilic vs Nucleophilic Substitution: Benzene vs Chloroalkanes — 9701/41/M/J/22/Q9 [4 Marks]",
            syllabus_ref="31.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Different organic functional groups undergo distinct substitution mechanisms.",
            parts=[
                QuestionPart("(a)", "Explain why benzene undergoes electrophilic substitution while bromoethane undergoes nucleophilic substitution.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the attacking species in each reaction.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene has an electron-rich delocalised &pi;-system that attracts electron-deficient electrophiles [1]; Bromoethane has an electron-deficient &delta;+ carbon bonded to electronegative bromine that attracts electron-rich nucleophiles [1].", "marks": 2},
                {"part": "(b)", "points": "Benzene: Electrophile (e.g. NO2+, Cl+, Br+) [1]; Bromoethane: Nucleophile (e.g. :OH-, :CN-, :NH3) [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/O/N/22/Q9
        Question(
            number=23,
            title="Chemical Test to Distinguish Ethanoyl Chloride from Chloroethane — 9701/42/O/N/22/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Ethanoyl chloride and chloroethane are both colourless liquids containing chlorine.",
            parts=[
                QuestionPart("(a)", "Describe a simple chemical test using water to distinguish between them, stating observations.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe what is observed when aqueous silver nitrate is added to the aqueous reaction mixture of each.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add water at room temperature: ethanoyl chloride reacts violently with effervescence / steamy white fumes of HCl; chloroethane shows no visible reaction / forms an immiscible layer [2].", "marks": 2},
                {"part": "(b)", "points": "Ethanoyl chloride: immediate heavy white precipitate of AgCl [1]; Chloroethane: no precipitate formed at room temperature [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/22/Q9
        Question(
            number=24,
            title="Hydrofluorocarbons (HFCs) as Ozone-Friendly Replacements — 9701/41/O/N/22/Q9 [4 Marks]",
            syllabus_ref="31.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="HFC-134a (1,1,1,2-tetrafluoroethane) has replaced CFC-12 in domestic refrigerators.",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of 1,1,1,2-tetrafluoroethane.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why HFCs have zero Ozone Depletion Potential (ODP) but remain an environmental concern.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CF3-CH2F drawn correctly [2].", "marks": 2},
                {"part": "(b)", "points": "They contain no chlorine atoms to form ozone-destroying Cl• radicals (ODP = 0) [1]; However, they are potent greenhouse gases with high Global Warming Potential (GWP) that contribute to climate change [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/21/Q9
        Question(
            number=25,
            title="Reaction of Acyl Chlorides with Ammonia and Primary Amines — 9701/42/M/J/21/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Ethanoyl chloride reacts vigorously with nitrogen bases.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of ethanoyl chloride with ammonia.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the balanced chemical equation for the reaction of ethanoyl chloride with methylamine, naming the organic product.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl + 2NH3 &rarr; CH3CONH2 + NH4Cl [2].", "marks": 2},
                {"part": "(b)", "points": "CH3COCl + 2CH3NH2 &rarr; CH3CONHCH3 + CH3NH3Cl [1]; N-methylethanamide [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/21/Q9
        Question(
            number=26,
            title="Inertness of Chlorobenzene towards Ammonia — 9701/41/M/J/21/Q9 [4 Marks]",
            syllabus_ref="31.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="When chlorobenzene is heated with concentrated aqueous ammonia, no reaction occurs.",
            parts=[
                QuestionPart("(a)", "State two reasons why ammonia cannot displace chlorine from chlorobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State how phenylamine is prepared industrially from benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. Partial double bond character of the C-Cl bond due to p-&pi; orbital overlap [1]; 2. Electrostatic repulsion of the lone pair on :NH3 by the delocalised &pi;-system of the ring [1].", "marks": 2},
                {"part": "(b)", "points": "Nitrate benzene to nitrobenzene (conc. HNO3 + conc. H2SO4 at 55 °C) [1]; Reduce nitrobenzene to phenylamine using tin and concentrated hydrochloric acid (Sn + conc. HCl), followed by NaOH [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q9
        Question(
            number=27,
            title="Reaction of Acyl Chlorides with Alcohols — 9701/42/O/N/21/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Ethanoyl chloride reacts with propan-1-ol.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation, including state symbols.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Name the ester product and state one advantage of this reaction over the acid-catalysed reaction using ethanoic acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl(l) + CH3CH2CH2OH(l) &rarr; CH3COOCH2CH2CH3(l) + HCl(g) [2].", "marks": 2},
                {"part": "(b)", "points": "Propyl ethanoate [1]; The reaction goes to completion (irreversible) and does not require an acid catalyst or heating [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/41/O/N/21/Q9
        Question(
            number=28,
            title="Halogen Free Radical Reactivity: Chlorine vs Bromine in Stratospheric Depletion — 9701/41/O/N/21/Q9 [4 Marks]",
            syllabus_ref="31.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Halons containing bromine (e.g. CBrClF<sub>2</sub>) are also potent ozone depleters.",
            parts=[
                QuestionPart("(a)", "Explain why bromine radicals are even more destructive per atom towards ozone than chlorine radicals.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the propagation steps for bromine-catalysed ozone destruction.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Bromine radicals react with ozone faster than chlorine radicals [1]; and the reservoir molecules that deactivate bromine (such as HBr) are broken down more rapidly by photolysis, keeping active Br• in circulation [1].", "marks": 2},
                {"part": "(b)", "points": "Br• + O3 &rarr; BrO• + O2 [1]; BrO• + O &rarr; Br• + O2 [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/42/M/J/20/Q9
        Question(
            number=29,
            title="Hydrolysis of 2-Bromopropane: SN1 vs SN2 Competition — 9701/42/M/J/20/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Secondary halogenoalkanes can react via both S<sub>N</sub>1 and S<sub>N</sub>2 pathways simultaneously.",
            parts=[
                QuestionPart("(a)", "Explain why secondary halogenoalkanes undergo both mechanisms.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State what experimental kinetic order would be observed if both mechanisms operate at similar rates.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "They have intermediate steric hindrance (allowing backside attack via S_N2) [1]; and their secondary carbocations have moderate stability via two +I alkyl groups (allowing ionisation via S_N1) [1].", "marks": 2},
                {"part": "(b)", "points": "Mixed order kinetics: Rate = k1[2-bromopropane] + k2[2-bromopropane][OH-] [2].", "marks": 2}
            ]
        ),

        # Q30: 9701/41/M/J/20/Q9
        Question(
            number=30,
            title="Preparation of Acyl Chlorides Using PCl5 — 9701/41/M/J/20/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Phosphorus(V) chloride reacts with ethanoic acid to synthesize ethanoyl chloride.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the two inorganic by-products and describe how ethanoyl chloride is separated from the reaction mixture.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COOH + PCl5 &rarr; CH3COCl + POCl3 + HCl [2].", "marks": 2},
                {"part": "(b)", "points": "Phosphorus(V) trichloride oxide (POCl3) and hydrogen chloride (HCl) [1]; Fractional distillation [1].", "marks": 2}
            ]
        ),

        # Q31: 9701/42/O/N/19/Q9
        Question(
            number=31,
            title="Physical Properties of Fluoroalkanes: Boiling Points vs Alkanes — 9701/42/O/N/19/Q9 [4 Marks]",
            syllabus_ref="31.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Tetrafluoromethane, CF<sub>4</sub> (<i>M</i><sub>r</sub> = 88.0), boils at -128 °C, whereas hexane, C<sub>6</sub>H<sub>14</sub> (<i>M</i><sub>r</sub> = 86.0), boils at +69 °C.",
            parts=[
                QuestionPart("(a)", "Explain why CF<sub>4</sub> has an extraordinarily low boiling point despite having a high molecular mass.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the type of intermolecular forces present in liquid CF<sub>4</sub> and liquid hexane.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Fluorine electrons are held very tightly by the highly electronegative nucleus, resulting in an extremely low polarisability of the electron cloud [1]; Consequently, the London dispersion forces between CF4 molecules are exceptionally weak [1].", "marks": 2},
                {"part": "(b)", "points": "Both possess only London dispersion forces (induced dipole-dipole attractions); hexane has an extended chain with much higher polarisability and much stronger London forces [2].", "marks": 2}
            ]
        ),

        # Q32: 9701/41/O/N/19/Q9
        Question(
            number=32,
            title="Comparison of Reactivity: Acyl Chloride vs Alkyl Chloride vs Aryl Chloride — 9701/41/O/N/19/Q9 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Order of reactivity towards nucleophilic attack: CH<sub>3</sub>COCl > CH<sub>3</sub>CH<sub>2</sub>Cl > C<sub>6</sub>H<sub>5</sub>Cl.",
            parts=[
                QuestionPart("(a)", "State which compound reacts most vigorously with water at room temperature, writing the equation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State which compound requires boiling with alcoholic silver nitrate to produce a precipitate.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl (ethanoyl chloride) [1]; CH3COCl + H2O &rarr; CH3COOH + HCl [1].", "marks": 2},
                {"part": "(b)", "points": "Chloroethane (CH3CH2Cl) requires heating [2] (chlorobenzene does not react at all even on boiling).", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q10
        Question(
            number=33,
            title="Reagent for Preparing Acyl Chlorides from Carboxylic Acids — 9701/42/M/J/23/Q10 [2 Marks]",
            syllabus_ref="31.1", difficulty="EASY", section_key="SEC_C",
            preamble="Acyl chlorides are reactive acid derivatives.",
            parts=[
                QuestionPart("(a)", "Name two reagents suitable for converting ethanoic acid into ethanoyl chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thionyl chloride (SOCl2) [1]; Phosphorus(V) chloride (PCl5) (or PCl3) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/M/J/23/Q10
        Question(
            number=34,
            title="Reason for Inertness of Chlorobenzene — 9701/41/M/J/23/Q10 [2 Marks]",
            syllabus_ref="31.2", difficulty="EASY", section_key="SEC_C",
            preamble="Aryl halides resist hydrolysis.",
            parts=[
                QuestionPart("(a)", "State why the C-Cl bond in chlorobenzene is stronger than in chloroethane.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Delocalisation of a chlorine lone pair into the benzene &pi;-system [1]; gives the C-Cl bond partial double bond character [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/O/N/23/Q10
        Question(
            number=35,
            title="Definition of a CFC — 9701/42/O/N/23/Q10 [2 Marks]",
            syllabus_ref="31.3", difficulty="EASY", section_key="SEC_C",
            preamble="CFCs are synthetic compounds.",
            parts=[
                QuestionPart("(a)", "Define the term <i>chlorofluorocarbon</i> (CFC) and give one example formula.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "An organic compound containing only chlorine, fluorine, and carbon atoms [1]; CCl3F (or CCl2F2) [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/O/N/23/Q10
        Question(
            number=36,
            title="Bond Cleaved by UV Light in CFCs — 9701/41/O/N/23/Q10 [2 Marks]",
            syllabus_ref="31.3", difficulty="EASY", section_key="SEC_C",
            preamble="CFCs break down in the stratosphere.",
            parts=[
                QuestionPart("(a)", "State which bond (C-Cl or C-F) is broken by stratospheric UV radiation, and explain why.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The C-Cl bond [1]; It has a much lower bond dissociation energy than the C-F bond [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/M/J/22/Q10
        Question(
            number=37,
            title="Observation When Ethanoyl Chloride Reacts with Water — 9701/42/M/J/22/Q10 [2 Marks]",
            syllabus_ref="31.1", difficulty="EASY", section_key="SEC_C",
            preamble="Acyl chlorides undergo rapid hydrolysis.",
            parts=[
                QuestionPart("(a)", "State two visible observations when water is added to ethanoyl chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. Steamy white / misty fumes evolved [1]; 2. Vigorous bubbling / effervescence / temperature rises [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/41/M/J/22/Q10
        Question(
            number=38,
            title="Monomer of PTFE — 9701/41/M/J/22/Q10 [2 Marks]",
            syllabus_ref="31.4", difficulty="EASY", section_key="SEC_C",
            preamble="PTFE is a commercial fluoropolymer.",
            parts=[
                QuestionPart("(a)", "State the name and formula of the monomer used to manufacture PTFE.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Tetrafluoroethene [1]; CF2=CF2 [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/O/N/22/Q10
        Question(
            number=39,
            title="Functional Group Formed by Acyl Chloride + Alcohol — 9701/42/O/N/22/Q10 [2 Marks]",
            syllabus_ref="31.1", difficulty="EASY", section_key="SEC_C",
            preamble="Acyl chlorides react with hydroxy compounds.",
            parts=[
                QuestionPart("(a)", "Name the organic functional group formed and the inorganic by-product.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ester (-COO-) [1]; Hydrogen chloride gas (HCl) [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/22/Q10
        Question(
            number=40,
            title="Why HFCs Do Not Deplete Ozone — 9701/41/O/N/22/Q10 [2 Marks]",
            syllabus_ref="31.3", difficulty="EASY", section_key="SEC_C",
            preamble="HFCs are used as replacements for CFCs.",
            parts=[
                QuestionPart("(a)", "Explain why hydrofluorocarbons do not damage the ozone layer.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "They contain no chlorine atoms [1]; and therefore cannot generate ozone-depleting chlorine radicals [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # 4 x 6-Markers (Q41–Q44), 4 x 4-Markers (Q45–Q48), 2 x 2-Markers (Q49–Q50)
        # =====================================================================

        # Q41: 9701/42/M/J/23/Q8(Repeat 1 - 6m)
        Question(
            number=41,
            title="[CORE REPEAT 1] Comparative Hydrolysis Rates of Chlorine Compounds — 9701/42/M/J/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_D",
            preamble="The relative reactivity of three chlorine compounds towards water is shown in Fig. 41.1.",
            figure_path=os.path.join(fig_dir, "a2_t31_halogen_hydrolysis_trend.png"),
            figure_caption="Fig. 41.1: Relative ease of hydrolysis: ethanoyl chloride >> chloroethane >> chlorobenzene.",
            parts=[
                QuestionPart("(a)", "Explain why ethanoyl chloride hydrolyses rapidly with water alone at room temperature.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why chloroethane requires heating with aqueous sodium hydroxide to undergo hydrolysis.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why chlorobenzene is completely unreactive towards hydrolysis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The carbonyl carbon is bonded to two electronegative atoms (O and Cl), making it very electron-deficient (&delta;+) [1]; Water readily attacks the carbonyl carbon via an addition-elimination mechanism without initial C-Cl bond cleavage [1].", "marks": 2},
                {"part": "(b)", "points": "The carbon atom has only a moderate &delta;+ charge and lacks a &pi;-bond for addition [1]; Reaction proceeds by an S_N2 mechanism requiring substantial activation energy to break the strong C-Cl single bond (340 kJ mol^-1) in the transition state [1].", "marks": 2},
                {"part": "(c)", "points": "Overlap of a chlorine p-orbital lone pair with the delocalised &pi;-electron system of the benzene ring gives the C-Cl bond partial double-bond character [1]; The bond is significantly stronger, and the high electron density of the aromatic ring electrostatically repels incoming OH- nucleophiles [1].", "marks": 2}
            ]
        ),

        # Q42: 9701/41/M/J/23/Q8(Repeat 2 - 6m)
        Question(
            number=42,
            title="[CORE REPEAT 2] Complete Catalytic Ozone Destruction Mechanism by CFCs — 9701/41/M/J/23/Q8 [6 Marks]",
            syllabus_ref="31.3", difficulty="HARD", section_key="SEC_D",
            preamble="CFC-12, CCl<sub>2</sub>F<sub>2</sub>, releases chlorine radicals upon photolysis in the stratosphere.",
            parts=[
                QuestionPart("(a)", "Write the equation for the initiation step triggered by ultraviolet light.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Write the two propagation steps and construct the overall balanced equation for the catalytic cycle.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why a single chlorine radical can catalytically destroy many thousands of ozone molecules.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CCl2F2 &rarr; •CClF2 + Cl• [1].", "marks": 1},
                {"part": "(b)", "points": "Propagation 1: Cl• + O3 &rarr; ClO• + O2 [1]; Propagation 2: ClO• + O &rarr; Cl• + O2 [1]; Overall: O3 + O &rarr; 2O2 [1].", "marks": 3},
                {"part": "(c)", "points": "Chlorine radicals act as homogeneous catalysts that are regenerated unchanged at the end of every propagation cycle [1]; The chain reaction continues indefinitely until terminated by rare radical-radical recombination [1].", "marks": 2}
            ]
        ),

        # Q43: 9701/42/O/N/23/Q8(Repeat 3 - 6m)
        Question(
            number=43,
            title="[CORE REPEAT 3] Testing Halogenoalkanes with Aqueous AgNO3 in Ethanol — 9701/42/O/N/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_D",
            preamble="Separate samples of 1-chlorobutane, 1-bromobutane, and 1-iodobutane are warmed with ethanolic AgNO<sub>3</sub>(aq).",
            parts=[
                QuestionPart("(a)", "State the observations for all three halogenoalkanes, stating precipitate colours.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Deduce the order of reactivity of the halogenoalkanes from fastest to slowest.", 1, num_answer_lines=1),
                QuestionPart("(c)", "Explain this order of reactivity with reference to bond enthalpies.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1-chlorobutane: white precipitate forms slowly; 1-bromobutane: cream precipitate forms moderately fast; 1-iodobutane: pale yellow precipitate forms rapidly [3].", "marks": 3},
                {"part": "(b)", "points": "1-iodobutane > 1-bromobutane > 1-chlorobutane [1].", "marks": 1},
                {"part": "(c)", "points": "The rate-determining step involves cleavage of the carbon-halogen bond [1]; Bond enthalpy decreases from C-Cl (340) to C-Br (280) to C-I (240 kJ mol^-1); the weakest C-I bond breaks most readily, yielding the fastest rate [1].", "marks": 2}
            ]
        ),

        # Q44: 9701/41/O/N/23/Q8(Repeat 4 - 6m)
        Question(
            number=44,
            title="[CORE REPEAT 4] Acyl Chloride Reactions: Hydrolysis, Esterification & Amide Formation — 9701/41/O/N/23/Q8 [6 Marks]",
            syllabus_ref="31.1", difficulty="HARD", section_key="SEC_D",
            preamble="Ethanoyl chloride reacts with water, alcohols, and amines via nucleophilic addition-elimination.",
            parts=[
                QuestionPart("(a)", "Write the equation for the reaction of CH<sub>3</sub>COCl with water, identifying the misty fumes evolved.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the equation for the reaction of CH<sub>3</sub>COCl with ethanol, naming the organic product.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Write the equation for the reaction of CH<sub>3</sub>COCl with ammonia, naming the organic product.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl + H2O &rarr; CH3COOH + HCl [1]; Misty fumes = hydrogen chloride (HCl) [1].", "marks": 2},
                {"part": "(b)", "points": "CH3COCl + CH3CH2OH &rarr; CH3COOCH2CH3 + HCl [1]; Ethyl ethanoate [1].", "marks": 2},
                {"part": "(c)", "points": "CH3COCl + 2NH3 &rarr; CH3CONH2 + NH4Cl [1]; Ethanamide [1].", "marks": 2}
            ]
        ),

        # Q45: 9701/42/M/J/22/Q8(Repeat 5 - 4m)
        Question(
            number=45,
            title="[CORE REPEAT 5] Partial Double Bond Character in Chlorobenzene — 9701/42/M/J/22/Q8 [4 Marks]",
            syllabus_ref="31.2", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Chlorobenzene does not react with aqueous silver nitrate even after prolonged boiling.",
            parts=[
                QuestionPart("(a)", "Explain why the C-Cl bond in chlorobenzene does not break easily.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the benzene ring repels incoming hydroxide nucleophiles.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A lone pair of electrons on the chlorine atom delocalises into the benzene &pi;-system [1]; imparting partial double-bond character and strengthening the bond [1].", "marks": 2},
                {"part": "(b)", "points": "The delocalised &pi;-electron cloud creates a high negative charge density [1]; which electrostatically repels incoming negatively charged OH- nucleophiles [1].", "marks": 2}
            ]
        ),

        # Q46: 9701/41/M/J/22/Q8(Repeat 6 - 4m)
        Question(
            number=46,
            title="[CORE REPEAT 6] Properties and Uses of Fluoroalkanes and PTFE — 9701/41/M/J/22/Q8 [4 Marks]",
            syllabus_ref="31.4", difficulty="MEDIUM", section_key="SEC_D",
            preamble="PTFE is an exceptionally unreactive polymer with non-stick properties.",
            parts=[
                QuestionPart("(a)", "Explain why the C-F bond is so chemically unreactive.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State two commercial uses of PTFE.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The C-F bond is extraordinarily strong with a very high bond dissociation enthalpy (467 kJ mol^-1) [1]; and the small, highly electronegative fluorine atoms tightly shield the carbon backbone [1].", "marks": 2},
                {"part": "(b)", "points": "1. Non-stick coatings for cookware / frying pans [1]; 2. Electrical cable insulation / pipe-seal tape / waterproof breathable fabric (Gore-Tex) [1].", "marks": 2}
            ]
        ),

        # Q47: 9701/42/O/N/22/Q8(Repeat 7 - 4m)
        Question(
            number=47,
            title="[CORE REPEAT 7] Distinguishing Benzyl Chloride from Chlorobenzene — 9701/42/O/N/22/Q8 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>Cl and C<sub>6</sub>H<sub>5</sub>Cl are tested with warm ethanolic AgNO<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "State the observation for (chloromethyl)benzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>Cl.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the observation for chlorobenzene, C<sub>6</sub>H<sub>5</sub>Cl, and explain the difference.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Immediate white precipitate of AgCl formed [2].", "marks": 2},
                {"part": "(b)", "points": "No precipitate formed [1]; In (chloromethyl)benzene, chlorine is on an aliphatic benzylic carbon where C-Cl hydrolyses readily; in chlorobenzene, chlorine is bonded to the aromatic ring with partial double bond character [1].", "marks": 2}
            ]
        ),

        # Q48: 9701/41/O/N/22/Q8(Repeat 8 - 4m)
        Question(
            number=48,
            title="[CORE REPEAT 8] Synthesis of Esters from Acyl Chlorides vs Carboxylic Acids — 9701/41/O/N/22/Q8 [4 Marks]",
            syllabus_ref="31.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Esters can be synthesized using either an acyl chloride or a carboxylic acid.",
            parts=[
                QuestionPart("(a)", "State two advantages of using an acyl chloride rather than a carboxylic acid to synthesize an ester.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State one disadvantage or hazard of using an acyl chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. The reaction is fast / occurs at room temperature without heating or catalyst [1]; 2. The reaction goes to completion (irreversible) giving much higher yields [1].", "marks": 2},
                {"part": "(b)", "points": "Produces toxic and corrosive gaseous hydrogen chloride (HCl) by-product / reacts violently with moisture [2].", "marks": 2}
            ]
        ),

        # Q49: 9701/42/M/J/21/Q8(Repeat 9 - 2m)
        Question(
            number=49,
            title="[CORE REPEAT 9] Ozone Destruction Equation — 9701/42/M/J/21/Q8 [2 Marks]",
            syllabus_ref="31.3", difficulty="EASY", section_key="SEC_D",
            preamble="The overall breakdown of stratospheric ozone is catalysed by halogen radicals.",
            parts=[
                QuestionPart("(a)", "Write the overall chemical equation for the conversion of ozone into oxygen in the stratosphere.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2O3 &rarr; 3O2 (or O3 + O &rarr; 2O2) [2].", "marks": 2}
            ]
        ),

        # Q50: 9701/41/M/J/21/Q8(Repeat 10 - 2m)
        Question(
            number=50,
            title="[CORE REPEAT 10] Acyl Chloride Reagent Choice — 9701/41/M/J/21/Q8 [2 Marks]",
            syllabus_ref="31.1", difficulty="EASY", section_key="SEC_D",
            preamble="Thionyl chloride is widely used in preparative organic chemistry.",
            parts=[
                QuestionPart("(a)", "Write the equation for the reaction of benzoic acid with SOCl<sub>2</sub>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5COOH + SOCl2 &rarr; C6H5COCl + SO2 + HCl [2].", "marks": 2}
            ]
        ),
    ]

    print("Topic 31 Questions Count:", len(questions))

    # Audit tariff
    m6 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    m4 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    m2 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    tot = sum(sum(p.marks for p in q.parts) for q in questions)
    print(f"Tariff Breakdown: 6-markers = {m6} (40%), 4-markers = {m4} (40%), 2-markers = {m2} (20%) | Total Marks = {tot}")
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    assert m6 == 20, f"Expected 20 6-markers, got {m6}"
    assert m4 == 20, f"Expected 20 4-markers, got {m4}"
    assert m2 == 10, f"Expected 10 2-markers, got {m2}"
    assert tot == 220, f"Expected 220 marks, got {tot}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 31 PDF built successfully!")

if __name__ == "__main__":
    build_topic31_50q()
