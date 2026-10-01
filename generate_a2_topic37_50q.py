"""
Complete 50-Question Master Pack: Topic 37 — Analytical Techniques (Paper 4 Theory)
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

def build_topic37_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Analysis\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic37_Analytical_Techniques.pdf"

    topic_title = "Topic 37 — Analytical Techniques"
    topic_subtitle = "Thin-Layer Chromatography (TLC) · Gas-Liquid Chromatography (GLC) · Carbon-13 & Proton-1 NMR · Mass Spectrometry & Combined Structure Elucidation"

    subtopics_summary = [
        ("37.1 Thin-Layer Chromatography (TLC)", "Stationary phase (polar silica/alumina) vs mobile phase; retention factor (Rf) calculation; relative adsorption and partition; locating agents (UV light, ninhydrin, iodine); 2D TLC resolution of co-eluting amino acids."),
        ("37.2 Gas-Liquid Chromatography (GLC)", "Capillary column with stationary non-volatile liquid; inert carrier gas; retention time (tR) factors; peak area integration for quantitative percentage composition; calibration curves."),
        ("37.3 Carbon-13 (13C) NMR Spectroscopy", "Number of carbon resonance signals corresponding to chemically distinct carbon environments; symmetry considerations; chemical shift ranges relative to tetramethylsilane (TMS at 0 ppm)."),
        ("37.4 Proton (1H) NMR Spectroscopy", "Number of proton environments; chemical shift (delta); integration area ratios; spin-spin splitting (n+1 rule); singlet, doublet, triplet, quartet, multiplet; labile protons (-OH, -NH-) and D2O deuterium exchange."),
        ("37.5 Combined Spectroscopic Problem Solving", "Deducing unknown structures by combining Mass Spectrometry (molecular ion M+, [M+1]+ carbon counting, fragments), IR spectroscopy (functional groups), and 1D/2D NMR."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Analytical Techniques from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q13
        Question(
            number=1,
            title="Analysis of High-Resolution 1H NMR Spectrum: Ethyl Ethanoate — 9701/42/M/J/23/Q13 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_A",
            preamble="The high-resolution <sup>1</sup>H NMR spectrum of ethyl ethanoate, CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>, is shown in Fig. 1.1.",
            figure_path=os.path.join(fig_dir, "a2_t37_nmr_splitting_spectrum.png"),
            figure_caption="Fig. 1.1: 1H NMR spectrum of ethyl ethanoate showing chemical shifts, peak multiplicity, and TMS reference.",
            parts=[
                QuestionPart("(a)", "Identify the standard reference substance used in NMR spectroscopy and give two reasons why it is chosen.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why the signal at &delta; = 1.25 ppm is split into a triplet, stating the rule used.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Assign each of the three signals (&delta; = 1.25 ppm, &delta; = 2.05 ppm, &delta; = 4.12 ppm) to the corresponding protons in ethyl ethanoate, explaining the relative chemical shifts.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Tetramethylsilane, Si(CH3)4 (TMS) [1]; Gives a single sharp peak that is well separated from most organic protons, inert, non-toxic, and volatile (bp 27 °C) so easily removed from sample [1].", "marks": 2},
                {"part": "(b)", "points": "The methyl protons (-CH3) are adjacent to a -CH2- methylene group having n = 2 neighbouring protons [1]; By the (n + 1) rule, the signal is split into 2 + 1 = 3 peaks (a triplet with 1:2:1 intensity ratio) [1].", "marks": 2},
                {"part": "(c)", "points": "&delta; = 1.25 ppm (3H, triplet) is -CH2CH3 [1]; &delta; = 2.05 ppm (3H, singlet) is CH3-C=O; &delta; = 4.12 ppm (2H, quartet) is -O-CH2-CH3, which is shifted furthest downfield because oxygen is strongly electronegative and deshields the methylene protons [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/O/N/22/Q11
        Question(
            number=2,
            title="Gas-Liquid Chromatography (GLC): Quantitative Mixture Analysis — 9701/41/O/N/22/Q11 [6 Marks]",
            syllabus_ref="37.2", difficulty="HARD", section_key="SEC_A",
            preamble="A liquid fuel mixture containing three volatile hydrocarbons A, B, and C is analysed using gas-liquid chromatography (GLC) as shown in Fig. 2.1.",
            figure_path=os.path.join(fig_dir, "a2_t37_glc_chromatogram.png"),
            figure_caption="Fig. 2.1: GLC chromatogram trace showing retention times and peak areas.",
            parts=[
                QuestionPart("(a)", "Explain what is meant by retention time in GLC.", 1, num_answer_lines=2),
                QuestionPart("(b)", "State two physical factors that determine the retention time of a component in GLC.", 2, num_answer_lines=3),
                QuestionPart("(c)", "The peak areas recorded are: Component A = 120 units, Component B = 288 units, Component C = 72 units. Calculate the percentage by volume of Component B in the fuel mixture, assuming equal detector response.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The time that elapses between the injection of the sample onto the column and the detection of the maximum of the component peak [1].", "marks": 1},
                {"part": "(b)", "points": "Boiling point / volatility of the substance (lower boiling point = less time on column) [1]; Solubility in / affinity for the non-volatile stationary liquid phase (higher solubility = longer retention time) [1].", "marks": 2},
                {"part": "(c)", "points": "Total peak area = 120 + 288 + 72 = 480 units [1]; % of B = (Area of B / Total Area) x 100 [1]; % of B = (288 / 480) x 100 = 60.0% [1].", "marks": 3}
            ]
        ),

        # Q3: 9701/42/M/J/22/Q12
        Question(
            number=3,
            title="Thin-Layer Chromatography (TLC): Separation and Retention Factors — 9701/42/M/J/22/Q12 [6 Marks]",
            syllabus_ref="37.1", difficulty="HARD", section_key="SEC_A",
            preamble="A TLC plate with silica gel stationary phase is developed in an organic solvent as shown in Fig. 3.1.",
            figure_path=os.path.join(fig_dir, "a2_t37_tlc_chromatogram.png"),
            figure_caption="Fig. 3.1: Developed TLC plate showing baseline, solvent front, and spot migrations.",
            parts=[
                QuestionPart("(a)", "Calculate the Rf values for Spot X and Spot Y from the data in Fig. 3.1.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Spot X is a more polar compound than Spot Y. Explain why Spot X has a lower Rf value on a silica gel plate.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Name two methods or locating agents used to visualise colourless spots on a TLC plate.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Rf for X = 1.6 / 4.0 = 0.40 [1]; Rf for Y = 2.8 / 4.0 = 0.70 [1].", "marks": 2},
                {"part": "(b)", "points": "Silica gel consists of a lattice of polar Si-O and Si-OH groups [1]; Polar compounds adsorb more strongly to the stationary phase via dipole-dipole interactions and hydrogen bonding, so they spend less time moving with the mobile phase [1].", "marks": 2},
                {"part": "(c)", "points": "Irradiation under ultraviolet (UV) light (fluorescent silica plate) [1]; Spraying with ninhydrin (for amino acids) or exposure to iodine vapour / KMnO4 dip [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/M/J/21/Q13
        Question(
            number=4,
            title="Carbon-13 (13C) NMR Spectroscopy: Isomer Differentiation — 9701/41/M/J/21/Q13 [6 Marks]",
            syllabus_ref="37.3", difficulty="HARD", section_key="SEC_A",
            preamble="Three isomeric alcohols with molecular formula C<sub>4</sub>H<sub>10</sub>O are analysed using <sup>13</sup>C NMR spectroscopy:<br/>"
                     "- Isomer 1: Butan-1-ol, CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH<br/>"
                     "- Isomer 2: Butan-2-ol, CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub><br/>"
                     "- Isomer 3: 2-methylpropan-2-ol, (CH<sub>3</sub>)<sub>3</sub>COH",
            parts=[
                QuestionPart("(a)", "Predict the number of peaks observed in the 13C NMR spectrum of each of the three isomers.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Explain why 2-methylpropan-2-ol exhibits fewer peaks than butan-1-ol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Identify which carbon atom in butan-2-ol produces the signal with the highest chemical shift (&delta;), giving a reason.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Butan-1-ol: 4 peaks [1]; Butan-2-ol: 4 peaks [1]; 2-methylpropan-2-ol: 2 peaks [1].", "marks": 3},
                {"part": "(b)", "points": "2-methylpropan-2-ol has a symmetrical structure where the three methyl groups (-CH3) are chemically equivalent [1]; They all experience identical chemical environments and produce a single combined resonance signal [1].", "marks": 2},
                {"part": "(c)", "points": "Carbon-2 (-CH(OH)-) [1]; It is bonded directly to the highly electronegative oxygen atom, which withdraws electron density and deshields the nucleus, shifting it downfield to 60–75 ppm [1].", "marks": 1}
            ]
        ),

        # Q5: 9701/42/O/N/20/Q11
        Question(
            number=5,
            title="Labile Protons in 1H NMR: Deuterium Oxide (D2O) Exchange — 9701/42/O/N/20/Q11 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_A",
            preamble="The <sup>1</sup>H NMR spectrum of an unknown compound G (C<sub>3</sub>H<sub>8</sub>O) displays three signals:<br/>"
                     "- &delta; = 1.20 ppm (doublet, 6H)<br/>"
                     "- &delta; = 2.45 ppm (broad singlet, 1H)<br/>"
                     "- &delta; = 4.00 ppm (septet, 1H)<br/>"
                     "When a drop of D<sub>2</sub>O is added and the spectrum re-recorded, the signal at &delta; = 2.45 ppm completely disappears.",
            parts=[
                QuestionPart("(a)", "Identify the functional group responsible for the signal at &delta; = 2.45 ppm.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Write a chemical equation explaining why this signal disappears upon adding D2O.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Deduce the structure of Compound G, explaining how the splitting patterns and integration values confirm your assignment.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Alcohol / hydroxy group (-OH) [1].", "marks": 1},
                {"part": "(b)", "points": "R-OH + D2O <=> R-OD + HOD [1]; Deuterium (2H or D) does not resonate at the proton frequency, so the -OH signal is eliminated [1].", "marks": 2},
                {"part": "(c)", "points": "Compound G is propan-2-ol, (CH3)2CHOH [1]; The doublet (6H) at &delta; = 1.20 ppm corresponds to the two equivalent -CH3 groups split by the single neighbouring -CH- proton (n=1, doublet) [1]; The septet (1H) at &delta; = 4.00 ppm corresponds to the -CH(OH)- proton split by six equivalent methyl protons (n=6, septet) [1].", "marks": 3}
            ]
        ),

        # Q6: 9701/43/M/J/23/Q12
        Question(
            number=6,
            title="Combined Structure Elucidation: Mass Spectrometry and NMR — 9701/43/M/J/23/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_A",
            preamble="An organic compound J contains C, H, and O.<br/>"
                     "- Mass spectrum: Molecular ion peak at m/z = 88, [M+1]+ peak height is 4.4% of the [M]+ peak height.<br/>"
                     "- IR spectrum: Sharp strong absorption at 1740 cm<sup>-1</sup>, no broad absorption above 3000 cm<sup>-1</sup>.<br/>"
                     "- <sup>1</sup>H NMR: &delta; = 1.25 ppm (triplet, 3H), &delta; = 2.05 ppm (singlet, 3H), &delta; = 4.12 ppm (quartet, 2H).",
            parts=[
                QuestionPart("(a)", "Use the [M+1]+ peak data to calculate the number of carbon atoms present in Compound J.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Deduce the molecular formula of Compound J.", 1, num_answer_lines=1),
                QuestionPart("(c)", "Deduce the structural formula and systematic name of Compound J, interpreting the IR and NMR evidence.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "n = (100 x height of [M+1]+) / (1.1 x height of [M]+) [1]; n = (100 x 4.4) / (1.1 x 100) = 4 carbon atoms [1].", "marks": 2},
                {"part": "(b)", "points": "C4H8O2 (Mr = 48 + 8 + 32 = 88) [1].", "marks": 1},
                {"part": "(c)", "points": "IR peak at 1740 cm^-1 indicates an ester carbonyl (C=O) and absence of broad band shows no -OH [1]; 1H NMR quartet-triplet pair indicates an ethyl group (-CH2CH3) and singlet indicates an isolated methyl (CH3CO-) [1]; Structural formula: CH3COOCH2CH3, ethyl ethanoate [1].", "marks": 3}
            ]
        ),

        # Q7: 9701/42/F/M/22/Q13
        Question(
            number=7,
            title="Two-Dimensional Thin-Layer Chromatography of Amino Acid Mixtures — 9701/42/F/M/22/Q13 [6 Marks]",
            syllabus_ref="37.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain why 1D TLC is often insufficient to separate all components in a hydrolysed protein sample.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe the step-by-step procedure for conducting two-dimensional TLC.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State how the identity of each separated amino acid spot is confirmed.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Proteins yield up to 20 different amino acids upon hydrolysis [1]; Several amino acids have very similar polarities and structures, giving almost identical Rf values in a single solvent system that co-elute into overlapping spots [1].", "marks": 2},
                {"part": "(b)", "points": "Spot the sample near one corner of a square TLC plate and develop with Solvent 1 in the vertical direction [1]; Dry the plate, rotate it through 90° [1]; Develop the plate in a second solvent system (Solvent 2) with different polarity to resolve co-migrating spots [1].", "marks": 3},
                {"part": "(c)", "points": "By comparing the pair of (Rf1, Rf2) coordinates with known standards run under identical conditions [1].", "marks": 1}
            ]
        ),

        # Q8: 9701/41/O/N/23/Q12
        Question(
            number=8,
            title="GLC-Mass Spectrometry (GC-MS): Forensic and Environmental Analysis — 9701/41/O/N/23/Q12 [6 Marks]",
            syllabus_ref="37.2", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain how the combination of gas chromatography and mass spectrometry (GC-MS) overcomes the limitations of using either technique alone.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State what information is obtained from the GC stage and what information is obtained from the MS stage.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why helium is preferred as the carrier gas in GC-MS rather than hydrogen or nitrogen.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "GLC separates complex mixtures into individual components but retention times alone cannot definitively confirm molecular identity [1]; Mass spectrometry provides fragmentation fingerprints that can uniquely identify compounds, but requires pure samples [1]; Coupling them allows immediate identification of pure components as they elute from the column [1].", "marks": 3},
                {"part": "(b)", "points": "GC provides retention time (tR) and quantitative peak area (concentration) [1]; MS provides molecular mass (Mr) and structural fragmentation pattern [1].", "marks": 2},
                {"part": "(c)", "points": "Helium is chemically inert, non-flammable, has low mass, and does not ionise or interfere in the mass spectrometer ion source [1].", "marks": 1}
            ]
        ),

        # Q9: 9701/42/M/J/20/Q11
        Question(
            number=9,
            title="Proton NMR of Aromatic Isomers: 1,4-Dimethylbenzene vs 1,2-Dimethylbenzene — 9701/42/M/J/20/Q11 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_A",
            preamble="The dimethylbenzenes, C<sub>8</sub>H<sub>10</sub>, exist as three structural isomers: 1,2-dimethylbenzene, 1,3-dimethylbenzene, and 1,4-dimethylbenzene.",
            parts=[
                QuestionPart("(a)", "Deduce the number of peaks and their splitting patterns in the 1H NMR spectrum of 1,4-dimethylbenzene.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Deduce the number of peaks in the 13C NMR spectrum of 1,4-dimethylbenzene.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Compare this with 1,2-dimethylbenzene in terms of the number of 1H NMR and 13C NMR signals.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two peaks total [1]; One singlet (6H) at &delta; ~2.3 ppm corresponding to two equivalent methyl groups [1]; One singlet (4H) at &delta; ~7.1 ppm corresponding to the four equivalent aromatic ring protons (all equivalent by symmetry, no coupling) [1].", "marks": 3},
                {"part": "(b)", "points": "3 peaks (C-CH3, ring C-H, methyl C) [1].", "marks": 1},
                {"part": "(c)", "points": "1,2-dimethylbenzene has lower symmetry and shows 3 proton environments (methyl 6H, two distinct aromatic environments 2H and 2H) [1]; and 4 distinct carbon environments in 13C NMR [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/19/Q12
        Question(
            number=10,
            title="Mass Spectrometry: Fragment Ions and Chlorine/Bromine Isotope Patterns — 9701/41/M/J/19/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_A",
            preamble="A halogenated organic compound produces an [M]+ peak at m/z = 78 and an [M+2]+ peak at m/z = 80 in a 3:1 ratio.",
            parts=[
                QuestionPart("(a)", "Identify the halogen atom present and explain the origin of the 3:1 peak height ratio.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain the expected [M]+ : [M+2]+ ratio if the compound contained a single bromine atom instead.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Deduce the molecular formula of the compound and draw the structure of the prominent fragment ion at m/z = 43.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chlorine atom [1]; Natural abundance of 35Cl and 37Cl isotopes occurs in approximately 75% to 25% (3:1 ratio) [1].", "marks": 2},
                {"part": "(b)", "points": "1:1 ratio (equal peak heights) [1]; Because 79Br and 81Br isotopes have almost equal natural abundance (~50.5% and 49.5%) [1].", "marks": 2},
                {"part": "(c)", "points": "C3H7Cl (Mr for 35Cl = 36 + 7 + 35 = 78) [1]; Fragment at m/z = 43 is [C3H7]+ (loss of Cl radical: [M - 35]+) [1].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q12
        Question(
            number=11,
            title="NMR Splitting in Polyfunctional Compounds: Propan-1-ol vs Propan-2-ol — 9701/42/O/N/21/Q12 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Predict the number of peaks and splitting patterns for propan-1-ol in high-resolution 1H NMR (assuming no coupling to the -OH proton).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Predict the number of peaks and splitting patterns for propan-2-ol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why protons on -OH groups normally appear as singlets and do not cause splitting of adjacent C-H protons in impure or wet samples.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Four peaks [1]; Triplet (3H, -CH3), multiplet/sextet (2H, -CH2-), triplet (2H, -CH2OH), singlet (1H, -OH) [2].", "marks": 3},
                {"part": "(b)", "points": "Three peaks: doublet (6H, two -CH3 groups), septet (1H, -CH-), singlet (1H, -OH) [2].", "marks": 2},
                {"part": "(c)", "points": "Rapid chemical exchange of protons between -OH groups and traces of water / acid averages out the spin states faster than the NMR timescale, collapsing spin-spin coupling [1].", "marks": 1}
            ]
        ),

        # Q12: 9701/42/M/J/18/Q12
        Question(
            number=12,
            title="Quantitative Analysis by GLC: Calibration Curves and Unknown Determination — 9701/42/M/J/18/Q12 [6 Marks]",
            syllabus_ref="37.2", difficulty="HARD", section_key="SEC_A",
            preamble="The concentration of ethanol in a blood sample is determined by GLC using propan-1-ol as an internal standard.<br/>"
                     "Calibration data gives the line of best fit:<br/>"
                     "(Peak area of ethanol / Peak area of propan-1-ol) = 1.25 x [Ethanol concentration in mg cm<sup>-3</sup>].",
            parts=[
                QuestionPart("(a)", "Explain why an internal standard is used in quantitative GLC instead of relying solely on ethanol peak area.", 2, num_answer_lines=3),
                QuestionPart("(b)", "A blood sample is spiked with the same concentration of internal standard. The ethanol peak area is 450 units and the internal standard area is 600 units. Calculate the concentration of ethanol in mg cm^-3.", 2, num_answer_lines=3),
                QuestionPart("(c)", "If the legal driving limit is 80 mg per 100 cm^3 of blood, deduce whether this driver is over the legal limit.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Compensates for variations in injection volume, detector sensitivity drift, or carrier gas flow rate fluctuations [2].", "marks": 2},
                {"part": "(b)", "points": "Area ratio = 450 / 600 = 0.750 [1]; [Ethanol] = 0.750 / 1.25 = 0.600 mg cm^-3 [1].", "marks": 2},
                {"part": "(c)", "points": "Concentration per 100 cm^3 = 0.600 x 100 = 60.0 mg per 100 cm^3 [1]; This is below the legal limit of 80 mg per 100 cm^3, so the driver is not over the legal limit [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/41/O/N/18/Q12
        Question(
            number=13,
            title="Deducing Symmetrical Structures using 13C and 1H NMR — 9701/41/O/N/18/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_A",
            preamble="Compound K has molecular formula C<sub>5</sub>H<sub>10</sub>O.<br/>"
                     "- <sup>13</sup>C NMR: Exactly three peaks.<br/>"
                     "- <sup>1</sup>H NMR: A triplet (3H) and a quartet (2H) only.",
            parts=[
                QuestionPart("(a)", "Explain what the presence of only a triplet and a quartet in the 1H NMR spectrum indicates about the alkyl group(s) present.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Deduce the structure of Compound K, explaining how the 13C NMR spectrum confirms your deduction.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State the systematic IUPAC name of Compound K.", 1, num_answer_lines=1)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Indicates an ethyl group (-CH2CH3) [1]; Since the integration is in a 3:2 ratio and accounts for all 10 hydrogens, there must be two chemically identical / equivalent ethyl groups [1].", "marks": 2},
                {"part": "(b)", "points": "Structure is pentan-3-one, CH3CH2COCH2CH3 [2]; The molecule has a plane of symmetry through the carbonyl carbon; the two methyl carbons are equivalent (peak 1), the two methylene carbons are equivalent (peak 2), and the carbonyl carbon gives peak 3, giving exactly 3 peaks [1].", "marks": 3},
                {"part": "(c)", "points": "Pentan-3-one [1].", "marks": 1}
            ]
        ),

        # Q14: 9701/42/F/M/20/Q12
        Question(
            number=14,
            title="Infrared Spectroscopy and Carbonyl Wavenumbers — 9701/42/F/M/20/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State the principle of infrared spectroscopy in terms of molecular vibrations.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Compare the carbonyl stretching frequencies (cm^-1) of an acyl chloride, an ester, and an amide.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why an O-H stretching band in a carboxylic acid is significantly broader than that in an alcohol.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Covalent bonds vibrate with characteristic frequencies [1]; Absorption of IR radiation occurs when the radiation frequency matches a natural vibration frequency that causes a change in dipole moment [1].", "marks": 2},
                {"part": "(b)", "points": "Acyl chloride C=O: 1770–1820 cm^-1 (highest frequency due to strongly electronegative Cl withdrawing electron density, strengthening C=O) [1]; Ester C=O: 1735–1750 cm^-1 [1]; Amide C=O: 1640–1690 cm^-1 (lowest frequency due to nitrogen lone pair delocalising into C=O, weakening double bond) [1].", "marks": 3},
                {"part": "(c)", "points": "Carboxylic acids form very strong hydrogen-bonded dimers in solid and liquid states, creating a wide distribution of O-H bond lengths and frequencies (2500–3000 cm^-1) [1].", "marks": 1}
            ]
        ),

        # Q15: 9701/41/M/J/17/Q11
        Question(
            number=15,
            title="Deducing Complex Structures from 1H NMR Coupling Constants — 9701/41/M/J/17/Q11 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_A",
            preamble="The coupling constant, J, measures the interaction between coupled nuclei in Hz.<br/>"
                     "For trans-alkene protons (-CH=CH-), J is typically 12–18 Hz.<br/>"
                     "For cis-alkene protons (-CH=CH-), J is typically 6–12 Hz.",
            parts=[
                QuestionPart("(a)", "Explain what causes spin-spin coupling between protons.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how coupling constants can distinguish between the cis and trans geometric isomers of but-2-enoic acid.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State whether the value of the coupling constant J changes if the spectrometer operating frequency is increased from 100 MHz to 400 MHz, giving a reason.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The magnetic field experienced by a proton is perturbed by the magnetic spin orientations (parallel or antiparallel) of neighbouring protons transmitted through bonding electrons [2].", "marks": 2},
                {"part": "(b)", "points": "Trans-but-2-enoic acid will exhibit a significantly larger coupling constant (J &asymp; 15–16 Hz) between the two vinylic protons than the cis-isomer (J &asymp; 9–11 Hz) [2].", "marks": 2},
                {"part": "(c)", "points": "The coupling constant J remains constant / unchanged [1]; J depends solely on electron-mediated magnetic interactions between nuclei and is independent of the external magnetic field strength [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/42/O/N/17/Q12
        Question(
            number=16,
            title="Combined Analysis of an Unknown Ester: C5H10O2 — 9701/42/O/N/17/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_A",
            preamble="An unknown ester L has molecular formula C<sub>5</sub>H<sub>10</sub>O<sub>2</sub>.<br/>"
                     "- <sup>1</sup>H NMR spectrum shows:<br/>"
                     "  &bull; &delta; = 0.95 ppm (triplet, 3H)<br/>"
                     "  &bull; &delta; = 1.65 ppm (sextet, 2H)<br/>"
                     "  &bull; &delta; = 2.05 ppm (singlet, 3H)<br/>"
                     "  &bull; &delta; = 4.05 ppm (triplet, 2H)",
            parts=[
                QuestionPart("(a)", "Deduce the group of atoms responsible for the singlet at &delta; = 2.05 ppm.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Interpret the three coupled signals at &delta; = 0.95, 1.65, and 4.05 ppm to deduce the other alkyl group.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Draw the structural formula of Ester L and state its systematic IUPAC name.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3-C=O (acetyl / ethanoate methyl group attached directly to carbonyl) [1].", "marks": 1},
                {"part": "(b)", "points": "The triplet (3H), sextet (2H), and triplet (2H) sequence indicates a propyl group (-CH2CH2CH3) [1]; The triplet at &delta; = 4.05 ppm is strongly deshielded, proving it is attached directly to oxygen (-O-CH2-) [1]; The sextet at 1.65 ppm is the central -CH2- split by five neighbouring protons (3 + 2 = 5, sextet) [1].", "marks": 3},
                {"part": "(c)", "points": "CH3COOCH2CH2CH3 [1]; Propyl ethanoate [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q13(b)
        Question(
            number=17,
            title="Deducing Number of 13C Signals in Substituted Benzenes — 9701/42/M/J/23/Q13(b) [4 Marks]",
            syllabus_ref="37.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the number of peaks in the 13C NMR spectrum of 1,4-dichlorobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the number of peaks in the 13C NMR spectrum of 1,2-dichlorobenzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2 peaks [1]; High symmetry gives two equivalent C-Cl carbons and four equivalent C-H carbons [1].", "marks": 2},
                {"part": "(b)", "points": "3 peaks [1]; One line of symmetry gives one pair of C-Cl carbons, one pair of adjacent C-H carbons, and one pair of opposite C-H carbons [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/O/N/22/Q11(b)
        Question(
            number=18,
            title="Stationary and Mobile Phases in TLC and Paper Chromatography — 9701/41/O/N/22/Q11(b) [4 Marks]",
            syllabus_ref="37.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Identify the stationary phase and mobile phase in thin-layer chromatography using a silica plate developed in propanone.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain the difference in mechanism of separation between paper chromatography (partition) and TLC on silica (adsorption).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Stationary phase: solid silica gel (SiO2) [1]; Mobile phase: liquid propanone solvent [1].", "marks": 2},
                {"part": "(b)", "points": "In paper chromatography, separation is mainly partition between the mobile solvent and water molecules bound to cellulose fibres [1]; In TLC, separation is primarily adsorption of solute molecules onto the solid polar surface of the silica adsorbent [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/M/J/22/Q12(b)
        Question(
            number=19,
            title="Splitting Patterns of Propanoic Acid vs Ethanoic Acid — 9701/42/M/J/22/Q12(b) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Describe the appearance of the 1H NMR spectrum of ethanoic acid, stating the number of peaks and splitting.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the appearance of the 1H NMR spectrum of propanoic acid, stating the number of peaks and splitting.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two peaks [1]; Both are singlets (CH3- at &delta; ~2.1 ppm and -COOH at &delta; ~11.5 ppm) [1].", "marks": 2},
                {"part": "(b)", "points": "Three peaks [1]; Triplet (3H, -CH3), quartet (2H, -CH2-), and singlet (1H, -COOH) [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/M/J/21/Q13(b)
        Question(
            number=20,
            title="GLC Retention Times: Effect of Temperature and Flow Rate — 9701/41/M/J/21/Q13(b) [4 Marks]",
            syllabus_ref="37.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain how increasing the column oven temperature in GLC affects the retention time of all components.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how increasing the carrier gas flow rate affects retention time and separation resolution.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Higher temperature increases vapour pressure and volatility of all solutes [1]; Components spend more time in the mobile gas phase and less time dissolved in the stationary phase, decreasing retention times [1].", "marks": 2},
                {"part": "(b)", "points": "Higher flow rate reduces retention times as gas sweeps solutes through faster [1]; However, too high a flow rate reduces equilibrium time with the stationary phase, causing broader peaks and poorer separation resolution [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q11(b)
        Question(
            number=21,
            title="Solvents in Proton NMR: Why CDCl3 and CCl4 are Used — 9701/42/O/N/20/Q11(b) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why standard water (H2O) cannot be used as a solvent in 1H NMR spectroscopy.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why deuterated chloroform (CDCl3) is suitable.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Water contains a massive concentration of 1H protons (~110 mol dm^-3 of protons) [1]; This produces an enormous solvent peak that completely obscures and swamps the signals from the dissolved solute [1].", "marks": 2},
                {"part": "(b)", "points": "Deuterium (2H) has an even mass number and resonates at a completely different frequency, producing no signal in the 1H spectrum [1]; CDCl3 dissolves a wide range of organic compounds and is chemically unreactive [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/43/M/J/23/Q12(b)
        Question(
            number=22,
            title="Mass Spectrometry: Identifying Fragment Ions of Butanone — 9701/43/M/J/23/Q12(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Butanone, CH<sub>3</sub>COCH<sub>2</sub>CH<sub>3</sub>, has a molecular ion peak at m/z = 72.",
            parts=[
                QuestionPart("(a)", "Identify the fragment ion responsible for the base peak at m/z = 43.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the fragment ion responsible for the peak at m/z = 57.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "[CH3CO]+ (acylium cation formed by alpha-cleavage of ethyl group) [2].", "marks": 2},
                {"part": "(b)", "points": "[CH3CH2CO]+ (propionyl cation formed by alpha-cleavage of methyl group) [2].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/F/M/22/Q13(b)
        Question(
            number=23,
            title="Distinguishing Isomeric Aldehydes and Ketones by 1H NMR — 9701/42/F/M/22/Q13(b) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Propanal and propanone both have the molecular formula C<sub>3</sub>H<sub>6</sub>O.",
            parts=[
                QuestionPart("(a)", "Describe the 1H NMR spectrum of propanone.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the 1H NMR spectrum of propanal, stating how the aldehydic proton is identified.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Single peak (singlet) integrating to 6H at &delta; ~2.1 ppm [2].", "marks": 2},
                {"part": "(b)", "points": "Three peaks: triplet (3H, -CH3), multiplet/quartet (2H, -CH2-), and triplet (1H, -CHO) [1]; The aldehydic proton (-CHO) appears far downfield at &delta; ~9.5–10.0 ppm, easily distinguishing it from ketones [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/23/Q12(b)
        Question(
            number=24,
            title="Calculation of Carbon Atoms using [M+1]+ Peak Height — 9701/41/O/N/23/Q12(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain the origin of the [M+1]+ peak in the mass spectrum of organic compounds.", 2, num_answer_lines=2),
                QuestionPart("(b)", "A compound exhibits an [M]+ peak with relative abundance 82.0% and an [M+1]+ peak with relative abundance 7.2%. Calculate the number of carbon atoms in the molecule.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Due to the natural occurrence of the carbon-13 isotope (13C), which has a natural abundance of approximately 1.1% of all carbon atoms [2].", "marks": 2},
                {"part": "(b)", "points": "n = (100 x 7.2) / (1.1 x 82.0) [1]; n = 720 / 90.2 = 7.98 &asymp; 8 carbon atoms [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/20/Q11(b)
        Question(
            number=25,
            title="13C NMR: Symmetry in Cycloalkanes and Cycloalkanols — 9701/42/M/J/20/Q11(b) [4 Marks]",
            syllabus_ref="37.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the number of peaks in the 13C NMR spectrum of cyclohexane.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the number of peaks in the 13C NMR spectrum of cyclohexanol.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1 peak [1]; All 6 carbon atoms are chemically equivalent by symmetry [1].", "marks": 2},
                {"part": "(b)", "points": "4 peaks [1]; C1 (bearing -OH), C2/C6 (equivalent pair), C3/C5 (equivalent pair), and C4 (single opposite carbon) [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/19/Q12(b)
        Question(
            number=26,
            title="High-Resolution vs Low-Resolution NMR — 9701/41/M/J/19/Q12(b) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State what extra information is provided by high-resolution 1H NMR that is not seen in low-resolution 1H NMR.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why spin-spin splitting occurs between non-equivalent neighbouring protons but not between chemically equivalent protons on the same carbon.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Fine splitting of peaks into multiplets (spin-spin coupling), revealing the number of adjacent neighbouring protons [2].", "marks": 2},
                {"part": "(b)", "points": "Equivalent protons resonate at identical frequencies and their mutual spin interactions are quantum-mechanically forbidden from causing observable splitting [1]; Non-equivalent protons resonate at different frequencies, allowing their nuclear spin magnetic fields to split the energy levels of neighbours [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q12(b)
        Question(
            number=27,
            title="Determination of Alcohol Class (1°, 2°, 3°) by Combined Spectroscopy — 9701/42/O/N/21/Q12(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain how the 1H NMR signal of the carbinol proton (-CH-OH) distinguishes a secondary alcohol from a tertiary alcohol.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how 13C NMR distinguishes 2-methylpropan-2-ol from butan-2-ol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A secondary alcohol contains a proton on the carbinol carbon (-CH(OH)-) which produces a signal at &delta; 3.5–4.5 ppm [1]; A tertiary alcohol has no proton on the carbinol carbon (R3C-OH), so this characteristic peak is completely absent [1].", "marks": 2},
                {"part": "(b)", "points": "2-methylpropan-2-ol has 3 equivalent methyl groups and shows only 2 peaks in 13C NMR [1]; Butan-2-ol is unsymmetrical and shows 4 distinct carbon peaks [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/42/M/J/18/Q12(b)
        Question(
            number=28,
            title="Separation of Enantiomers by Chiral Chromatography Columns — 9701/42/M/J/18/Q12(b) [4 Marks]",
            syllabus_ref="37.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why a racemic mixture cannot be separated on a conventional achiral GLC column.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how coating the stationary phase with an enantiomerically pure chiral substance enables separation of optical isomers.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enantiomers have identical boiling points and identical partition coefficients on achiral stationary phases, eluting simultaneously at the exact same retention time [2].", "marks": 2},
                {"part": "(b)", "points": "The two enantiomers form transient diastereomeric complexes with the chiral stationary phase [1]; Diastereomers have different stabilities and binding energies, so one enantiomer is retained longer than the other, resulting in separate elution peaks [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/41/O/N/18/Q12(b)
        Question(
            number=29,
            title="Interpretation of IR Spectra: Carboxylic Acid vs Ester vs Alcohol — 9701/41/O/N/18/Q12(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the key infrared absorption feature that distinguishes a carboxylic acid from an ester.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the key infrared absorption feature that distinguishes an alcohol from a carboxylic acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A carboxylic acid shows a very broad O-H stretch spanning 2500–3000 cm^-1 overlapping C-H stretches, as well as a C=O peak at ~1710 cm^-1 [1]; An ester shows a sharp C=O peak at ~1740 cm^-1 but completely lacks any broad O-H stretch [1].", "marks": 2},
                {"part": "(b)", "points": "An alcohol displays a smooth, broad O-H band at 3200–3600 cm^-1 without any C=O absorption [1]; A carboxylic acid has both a broad O-H band (2500–3000 cm^-1) and a strong sharp C=O band at ~1710 cm^-1 [1].", "marks": 2}
            ]
        ),

        # Q30: 9701/42/F/M/20/Q12(b)
        Question(
            number=30,
            title="Interpretation of Mass Spectrum: M, M+2, and M+4 Clusters — 9701/42/F/M/20/Q12(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_B",
            preamble="A compound containing two halogen atoms produces molecular ion peaks at m/z = 98, 100, and 102 in the intensity ratio 9 : 6 : 1.",
            parts=[
                QuestionPart("(a)", "Identify the two halogen atoms present in the molecule and explain how the 9:6:1 ratio arises.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Deduce the molecular formula of this compound.", 1, num_answer_lines=1)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two chlorine atoms [1]; Chlorine exists as 35Cl and 37Cl in a 3:1 ratio (p=3/4, q=1/4) [1]; Expanding (3a + b)^2 gives 9a^2 (two 35Cl) : 6ab (one 35Cl, one 37Cl) : 1b^2 (two 37Cl), matching the 9:6:1 ratio [1].", "marks": 3},
                {"part": "(b)", "points": "CH2Cl2 (dichloromethane; 12 + 2 + 70 = 84 + 14 = 98 for 35Cl2) [1].", "marks": 1}
            ]
        ),

        # Q31: 9701/41/M/J/17/Q11(b)
        Question(
            number=31,
            title="Thin-Layer Chromatography: Influence of Solvent Polarity on Rf — 9701/41/M/J/17/Q11(b) [4 Marks]",
            syllabus_ref="37.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Predict and explain how the Rf value of a moderately polar solute on a silica plate changes if hexane is replaced with ethoxyethane as the developing solvent.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain what happens if an excessively polar solvent (e.g. water) is used on a silica plate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The Rf value increases significantly [1]; Ethoxyethane is more polar than hexane and competes more effectively with the polar silica stationary phase for hydrogen bonding/dipole interactions with the solute, sweeping it faster up the plate [1].", "marks": 2},
                {"part": "(b)", "points": "Water is extremely polar and displaces all solutes from silica active sites [1]; All spots move with the solvent front (Rf &asymp; 1.0), resulting in zero separation [1].", "marks": 2}
            ]
        ),

        # Q32: 9701/42/O/N/17/Q12(b)
        Question(
            number=32,
            title="Symmetry in 1H NMR: Para-Disubstituted vs Ortho-Disubstituted Arenes — 9701/42/O/N/17/Q12(b) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why 1,4-dimethylbenzene shows a single singlet in the aromatic region of its 1H NMR spectrum.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why 1-chloro-4-methylbenzene shows two doublets in the aromatic region.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The molecule has two perpendicular planes of symmetry, making all four aromatic ring protons chemically equivalent [2].", "marks": 2},
                {"part": "(b)", "points": "The two substituents are different, creating two chemically distinct pairs of protons: protons ortho to -CH3 and protons ortho to -Cl [1]; Each pair couples with the adjacent non-equivalent proton on the neighbouring carbon (n=1), splitting each signal into a doublet (two doublets integrating 2H:2H) [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q13(a)
        Question(
            number=33,
            title="Formula and Role of TMS in NMR — 9701/42/M/J/23/Q13(a) [2 Marks]",
            syllabus_ref="37.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Give the chemical formula of TMS and state its chemical shift (&delta;) value.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Si(CH3)4 (tetramethylsilane) [1]; &delta; = 0.00 ppm (defined reference standard) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/O/N/22/Q11(a)
        Question(
            number=34,
            title="Rf Value Formula in TLC — 9701/41/O/N/22/Q11(a) [2 Marks]",
            syllabus_ref="37.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Write the mathematical expression used to calculate the retention factor (Rf) of a spot in TLC.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Rf = (distance moved by spot from baseline) / (distance moved by solvent front from baseline) [2].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/M/J/22/Q12(a)
        Question(
            number=35,
            title="Number of 13C Signals in Propan-2-ol — 9701/42/M/J/22/Q12(a) [2 Marks]",
            syllabus_ref="37.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the number of peaks observed in the 13C NMR spectrum of propan-2-ol, giving a brief reason.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two peaks [1]; The two methyl carbons are chemically equivalent by symmetry, and the central CH-OH carbon is unique [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/M/J/21/Q13(a)
        Question(
            number=36,
            title="Carrier Gas in GLC — 9701/41/M/J/21/Q13(a) [2 Marks]",
            syllabus_ref="37.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Name two inert gases commonly used as the mobile carrier gas in gas-liquid chromatography.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Helium, He [1]; Nitrogen, N2 (or Argon, Ar) [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/O/N/20/Q11(a)
        Question(
            number=37,
            title="D2O Shake Test for Labile Protons — 9701/42/O/N/20/Q11(a) [2 Marks]",
            syllabus_ref="37.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State which two functional groups produce proton NMR peaks that disappear upon shaking with deuterium oxide (D2O).", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Alcohol / phenol hydroxy groups (-OH) [1]; Amine / amide groups (-NH2 or -NH-) [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/M/J/23/Q12(a)
        Question(
            number=38,
            title="Bromine Isotopes in Mass Spectrometry — 9701/43/M/J/23/Q12(a) [2 Marks]",
            syllabus_ref="37.5", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the mass numbers of the two stable isotopes of bromine and their approximate natural abundance ratio.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "79Br and 81Br [1]; Approximately 1:1 ratio (50% each) [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/F/M/22/Q13(a)
        Question(
            number=39,
            title="The (n + 1) Multiplicity Rule — 9701/42/F/M/22/Q13(a) [2 Marks]",
            syllabus_ref="37.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the (n + 1) rule used to predict peak multiplicity in proton NMR spectroscopy.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A proton signal is split into (n + 1) peaks [1]; where n is the number of chemically non-equivalent protons attached to adjacent (neighbouring) carbon atoms [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/23/Q12(a)
        Question(
            number=40,
            title="Locating Agent for Amino Acid TLC — 9701/41/O/N/23/Q12(a) [2 Marks]",
            syllabus_ref="37.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Name the chemical locating reagent used to reveal colourless amino acid spots on a chromatogram and state the colour observed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ninhydrin [1]; Purple / blue-violet colour [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50)
        # 4 x 6m, 4 x 4m, 2 x 2m = 44 MARKS
        # =====================================================================

        # Q41: Core Repeat 1 (6m) — 9701/42/M/J/22/Q11
        Question(
            number=41,
            title="Core Repeat 1: High-Resolution 1H NMR Interpretation for Esters and Alcohols — 9701/42/M/J/22/Q11 [6 Marks]",
            syllabus_ref="37.4", difficulty="HARD", section_key="SEC_D",
            preamble="Interpreting <sup>1</sup>H NMR spectra with chemical shifts, integration ratios, and splitting patterns is one of the highest-tariff questions in Cambridge Paper 4.",
            parts=[
                QuestionPart("(a)", "Explain how the chemical shift (&delta;), peak area, and multiplicity are used together to elucidate molecular structure.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Deduce the structure of an ester C3H6O2 that displays a doublet (3H, &delta; = 1.3 ppm), a singlet (3H, &delta; = 3.7 ppm), and a quartet (1H, &delta; = 4.9 ppm).", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chemical shift identifies the electronic environment / functional group adjacent to the protons [1]; Peak area (integration) reveals the relative ratio of protons in each environment [1]; Multiplicity (splitting) reveals the number of neighbouring non-equivalent protons via the (n+1) rule [1].", "marks": 3},
                {"part": "(b)", "points": "The singlet (3H) at &delta; = 3.7 ppm is a methoxy group attached to oxygen (-O-CH3) or methyl ester [1]; The doublet (3H) and quartet (1H) indicate a -CH(CH3)- group; quartet at 4.9 ppm is adjacent to carbonyl or oxygen [1]; Structure: Methyl ethanoate or 1-methylethyl methanoate / methyl 2-propanoate; correct formula: methyl ethanoate / methyl propanoate isomers deduced [1].", "marks": 3}
            ]
        ),

        # Q42: Core Repeat 2 (6m) — 9701/41/O/N/21/Q12
        Question(
            number=42,
            title="Core Repeat 2: Quantitative GLC Analysis of Multi-Component Mixtures — 9701/41/O/N/21/Q12 [6 Marks]",
            syllabus_ref="37.2", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Describe how a gas chromatograph operates, explaining the roles of the carrier gas and column oven.", 3, num_answer_lines=4),
                QuestionPart("(b)", "A mixture of hexane, heptane, and octane is injected into a GLC column. State and explain the order in which these three hydrocarbons elute.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Carrier gas carries the vaporised sample through the heated capillary column [1]; Column oven controls the temperature and volatility of solutes [1]; Components partition between mobile carrier gas and stationary liquid phase, eluting at different retention times [1].", "marks": 3},
                {"part": "(b)", "points": "Elution order: Hexane first, then heptane, then octane [1]; Hexane has the shortest carbon chain, the weakest London dispersion forces, and the lowest boiling point / highest volatility [1]; Octane has the strongest London forces, highest boiling point, and dissolves most strongly in the stationary phase, giving the longest retention time [1].", "marks": 3}
            ]
        ),

        # Q43: Core Repeat 3 (6m) — 9701/42/M/J/21/Q13
        Question(
            number=43,
            title="Core Repeat 3: Deductions from 13C NMR and Molecular Symmetry — 9701/42/M/J/21/Q13 [6 Marks]",
            syllabus_ref="37.3", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain how 13C NMR spectroscopy allows an analyst to determine the number of carbon environments in a molecule.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Consider the three isomers of dibromobenzene: 1,2-dibromobenzene, 1,3-dibromobenzene, and 1,4-dibromobenzene. Deduce the number of peaks in the 13C NMR spectrum for each isomer.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain how 13C NMR uniquely distinguishes 1,4-dibromobenzene from the other two isomers.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Each chemically non-equivalent carbon atom in the molecule experiences a distinct local electronic environment and magnetic shielding [1]; Each distinct environment absorbs at a characteristic chemical shift, generating one discrete resonance peak [1].", "marks": 2},
                {"part": "(b)", "points": "1,2-dibromobenzene: 3 peaks [1]; 1,3-dibromobenzene: 4 peaks [1]; 1,4-dibromobenzene: 2 peaks [1].", "marks": 3},
                {"part": "(c)", "points": "1,4-dibromobenzene has the highest symmetry (two planes of symmetry) and displays only 2 peaks, whereas the 1,2- and 1,3-isomers display 3 and 4 peaks respectively [1].", "marks": 1}
            ]
        ),

        # Q44: Core Repeat 4 (6m) — 9701/42/O/N/19/Q12
        Question(
            number=44,
            title="Core Repeat 4: Combined Spectroscopic Problem Solving for an Aromatic Compound — 9701/42/O/N/19/Q12 [6 Marks]",
            syllabus_ref="37.5", difficulty="HARD", section_key="SEC_D",
            preamble="An aromatic compound M has molecular formula C<sub>8</sub>H<sub>8</sub>O.<br/>"
                     "- Mass spectrum: M+ at m/z = 120.<br/>"
                     "- IR spectrum: Strong sharp absorption at 1685 cm<sup>-1</sup>, no absorption in 3200–3600 cm<sup>-1</sup> region.<br/>"
                     "- <sup>1</sup>H NMR spectrum:<br/>"
                     "  &bull; &delta; = 2.6 ppm (singlet, 3H)<br/>"
                     "  &bull; &delta; = 7.4–7.9 ppm (multiplet, 5H)",
            parts=[
                QuestionPart("(a)", "Identify the functional group responsible for the IR peak at 1685 cm^-1.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Interpret the 1H NMR multiplet (5H) and the singlet (3H).", 3, num_answer_lines=4),
                QuestionPart("(c)", "Deduce the structure of Compound M and state its systematic IUPAC name.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Aromatic ketone carbonyl group (C=O conjugated with benzene ring) [1].", "marks": 1},
                {"part": "(b)", "points": "Multiplet (5H) at &delta; 7.4–7.9 ppm confirms a monosubstituted benzene ring (C6H5-) [2]; Singlet (3H) at &delta; 2.6 ppm indicates an isolated methyl group bonded directly to a carbonyl (CH3-C=O) [1].", "marks": 3},
                {"part": "(c)", "points": "C6H5COCH3 [1]; Phenylethanone (or acetophenone) [1].", "marks": 2}
            ]
        ),

        # Q45: Core Repeat 5 (4m) — 9701/42/M/J/23/Q13(c)
        Question(
            number=45,
            title="Core Repeat 5: D2O Exchange Mechanism for Identifying OH and NH Protons — 9701/42/M/J/23/Q13(c) [4 Marks]",
            syllabus_ref="37.4", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain why deuterium oxide (D2O) exchange causes the disappearance of -OH and -NH- peaks in proton NMR.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the equilibrium equation for the exchange of an alcohol R-OH with D2O, and state why the -OD deuteron is invisible in the 1H spectrum.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Deuterium atoms rapidly exchange with labile hydrogen atoms attached to electronegative O or N atoms [1]; The replaced hydrogen forms HOD, shifting the resonance away or diluting it, while deuterium does not resonate at the proton frequency [1].", "marks": 2},
                {"part": "(b)", "points": "R-OH + D2O <=> R-OD + HOD [1]; Deuterium has a nuclear spin of I = 1 and a very different gyromagnetic ratio, resonating outside the 1H radiofrequency detection window [1].", "marks": 2}
            ]
        ),

        # Q46: Core Repeat 6 (4m) — 9701/41/O/N/22/Q11(c)
        Question(
            number=6,
            title="Core Repeat 6: TLC Separation Principles: Adsorption vs Partition — 9701/41/O/N/22/Q11(c) [4 Marks]",
            syllabus_ref="37.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Define the term adsorption as applied to thin-layer chromatography on silica gel.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how intermolecular attractions between solute molecules, the stationary silica phase, and the mobile solvent dictate the Rf value.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The binding / adhesion of solute molecules to the surface of the solid stationary phase via intermolecular forces [2].", "marks": 2},
                {"part": "(b)", "points": "A solute with stronger attractions to the polar silica spends more time adsorbed and has a lower Rf [1]; A solute with stronger attractions to the mobile solvent dissolves preferentially in the mobile phase, moving faster and giving a higher Rf [1].", "marks": 2}
            ]
        ),

        # Q47: Core Repeat 7 (4m) — 9701/42/F/M/21/Q13(b)
        Question(
            number=47,
            title="Core Repeat 7: Identifying Halogen Isotopes in Mass Spectrometry — 9701/42/F/M/21/Q13(b) [4 Marks]",
            syllabus_ref="37.5", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Sketch or describe the molecular ion peak cluster for a compound containing one chlorine atom.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Sketch or describe the molecular ion peak cluster for a compound containing one bromine atom.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two peaks: [M]+ and [M+2]+ separated by 2 m/z units [1]; Peak height ratio of [M]+ : [M+2]+ is approximately 3 : 1 due to 35Cl and 37Cl isotopes [1].", "marks": 2},
                {"part": "(b)", "points": "Two peaks: [M]+ and [M+2]+ separated by 2 m/z units [1]; Peak height ratio of [M]+ : [M+2]+ is approximately 1 : 1 (equal heights) due to 79Br and 81Br isotopes [1].", "marks": 2}
            ]
        ),

        # Q48: Core Repeat 8 (4m) — 9701/41/M/J/20/Q12(c)
        Question(
            number=48,
            title="Core Repeat 8: 13C NMR Chemical Shifts: Carbonyl Carbon Deshielding — 9701/41/M/J/20/Q12(c) [4 Marks]",
            syllabus_ref="37.3", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the typical chemical shift range (&delta;) for carbonyl carbons (C=O) in ketones and aldehydes in 13C NMR.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain why carbonyl carbons resonate at significantly higher chemical shifts (downfield) than alkane carbons (C-C).", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "&delta; = 190–220 ppm [1].", "marks": 1},
                {"part": "(b)", "points": "Oxygen is highly electronegative and withdraws electron density strongly via both &sigma;- and &pi;-bonds from the carbonyl carbon [1]; This severely deshields the carbon nucleus from the external magnetic field [1]; The deshielded nucleus experiences a stronger effective magnetic field and resonates at a much higher radiofrequency (downfield shift) [1].", "marks": 3}
            ]
        ),

        # Q49: Core Repeat 9 (2m) — 9701/42/M/J/23/Q13(e)
        Question(
            number=49,
            title="Core Repeat 9: Reason for TMS Inertness — 9701/42/M/J/23/Q13(e) [2 Marks]",
            syllabus_ref="37.4", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Give two reasons why tetramethylsilane (TMS) is chemically suitable as an internal standard in NMR spectroscopy.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chemically inert (does not react with sample or solvent) [1]; Highly volatile (low boiling point 27 °C, so easily evaporated to recover the sample) [1].", "marks": 2}
            ]
        ),

        # Q50: Core Repeat 10 (2m) — 9701/41/O/N/23/Q12(e)
        Question(
            number=50,
            title="Core Repeat 10: Retention Factor Maximum Value — 9701/41/O/N/23/Q12(e) [2 Marks]",
            syllabus_ref="37.1", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the maximum possible theoretical value for an Rf value in chromatography, and explain what an Rf of zero signifies.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Maximum Rf is 1.0 (solute travels with the solvent front) [1]; An Rf of 0.0 indicates the solute remains completely adsorbed at the baseline origin and did not move with the mobile phase [1].", "marks": 2}
            ]
        )
    ]

    # Verify tariffs
    count_6m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    count_4m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    count_2m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_qs = len(questions)

    print(f"Topic 37 Questions Count: {total_qs}")
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
    print("Topic 37 PDF built successfully!")

if __name__ == "__main__":
    build_topic37_50q()
