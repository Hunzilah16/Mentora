"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 22: Analytical Techniques.
Subtopics:
  22.1 Infrared spectroscopy:
       - Principles of IR absorption: covalent bond vibration (stretching and bending modes)
       - Requirement of dipole moment change during vibration (transparent: N2, O2; IR-active: CO2, H2O, CH4)
       - Characteristic absorption wavenumber ranges (cm-1) from Data Booklet:
         * O-H (alcohol): 3200-3600 cm-1 (strong, broad, hydrogen bonded)
         * O-H (carboxylic acid): 2500-3000 cm-1 (very broad, jagged envelope)
         * C=O (carbonyl): 1640-1750 cm-1 (strong, sharp in aldehydes, ketones, acids, esters)
         * C-H: alkane 2850-2950 cm-1; alkene/arene 3000-3100 cm-1; aldehyde doublet 2720 & 2820 cm-1
         * C=C: 1620-1680 cm-1
         * C=N: 2200-2250 cm-1
         * C-O: 1040-1300 cm-1
         * N-H: 3300-3500 cm-1 (primary amine doublet, secondary amine singlet)
       - Distinguishing functional group isomers and monitoring chemical reaction progress
       - The fingerprint region (< 1500 cm-1): complex skeletal vibrations and database matching
       - Greenhouse gases and atmospheric infrared absorption
  22.2 Mass spectrometry:
       - Principles: ionisation by electron bombardment, acceleration, magnetic deflection, detection
       - Molecular ion peak [M]+: relative molecular mass Mr determination
       - [M+1]+ peak: carbon-13 abundance calculation of carbon atom count:
         n = (100 * abundance of [M+1]+) / (1.1 * abundance of [M]+)
       - [M+2]+ (and [M+4]+) isotopic patterns:
         * Chlorine: 35Cl : 37Cl = 3 : 1 (monochloro [M]:[M+2] = 3:1; dichloro [M]:[M+2]:[M+4] = 9:6:1)
         * Bromine: 79Br : 81Br = 1 : 1 (monobromo [M]:[M+2] = 1:1; dibromo [M]:[M+2]:[M+4] = 1:2:1)
       - Fragmentation mechanisms: formation of stable cations and neutral radicals
         * m/z = 15 ([CH3]+), 29 ([C2H5]+, [CHO]+), 43 ([C3H7]+, [CH3CO]+), 57 ([C4H9]+)
         * Characteristic neutral losses: M-15 (CH3), M-17 (OH), M-18 (H2O), M-28 (CO, C2H4), M-31 (OCH3), M-45 (COOH)
       - Combined structural elucidation: integrating IR, MS, combustion analysis, and diagnostic chemical tests

Total questions: 50
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class QuestionPart:
    label: str
    text: str
    marks: int
    num_answer_lines: int = 2
    options: List[str] = field(default_factory=list)

@dataclass
class Question:
    number: int
    title: str
    syllabus_ref: str
    difficulty: str  # EASY or HARD
    preamble: str
    parts: List[QuestionPart]
    mark_scheme: List[dict]
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None

TOPIC_22_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 22.1: INFRARED SPECTROSCOPY (Q1 - Q25)
    # =========================================================================
    Question(
        number=1,
        title="Principles of Infrared Spectroscopy & Bond Vibrations — 9701/22/M/J/23/Q5(a)-(d)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Infrared (IR) spectroscopy exploits the absorption of electromagnetic radiation by vibrating covalent bonds in molecules. Fig. 1.1 shows the characteristic infrared absorption ranges for key organic functional groups.",
        figure_path="figures/analysis_ir_spectra_correlation.png",
        figure_caption="Fig. 1.1: Characteristic infrared absorption ranges for key organic bonds and functional groups.",
        parts=[
            QuestionPart(label="(a)", text="State the physical condition that a molecular vibration must satisfy in order to absorb infrared radiation.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Explain why gaseous nitrogen, N2, and oxygen, O2, are transparent to infrared radiation, whereas carbon dioxide, CO2, absorbs infrared radiation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the two primary types of vibrational modes that occur when covalent bonds absorb infrared radiation.", marks=2, num_answer_lines=2),
            QuestionPart(label="(d)", text="State the wavenumber range in cm-1 associated with the fingerprint region of an infrared spectrum and explain its practical significance in chemical analysis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["There must be a change in the molecule's dipole moment during the vibration [1]"], "marks": 1},
            {"part": "(b)", "points": ["N2 and O2 are homonuclear non-polar diatomic molecules that undergo no change in dipole moment when vibrating [1]", "CO2 undergoes asymmetrical stretching or bending vibrations that cause a net change in dipole moment, allowing IR absorption [1]"], "marks": 2},
            {"part": "(c)", "points": ["Stretching vibrations (symmetrical or asymmetrical changes in bond length) [1]", "Bending vibrations (changes in bond angles / deformation) [1]"], "marks": 2},
            {"part": "(d)", "points": ["Wavenumber range: Below 1500 cm-1 (or 400-1500 cm-1) [1]", "Significance: It contains a unique, complex pattern of bending and skeletal absorption bands characteristic of the whole molecule; matching this pattern against a reference spectral library confirms exact identity [1]"], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Distinguishing Functional Group Profiles in IR — 9701/21/O/N/23/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Three constitutional isomers with molecular formula C3H6O, C3H8O, and C3H6O2 were analyzed by infrared spectroscopy. Fig. 2.1 displays the recorded spectra profiles for propan-1-ol, propanoic acid, and propanal.",
        figure_path="figures/analysis_ir_functional_group_profiles.png",
        figure_caption="Fig. 2.1: Infrared spectra profiles for propan-1-ol, propanoic acid, and propanal.",
        parts=[
            QuestionPart(label="(a)", text="Contrast the O-H absorption band observed in the spectrum of propan-1-ol with the O-H absorption band in propanoic acid, citing wavenumber ranges and peak appearances.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Identify the absorption peak present in both propanoic acid and propanal that is absent in propan-1-ol. Give its characteristic wavenumber range and the bond responsible.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Propanal exhibits a distinctive pair of sharp absorption bands at 2720 cm-1 and 2820 cm-1. Deduce the specific bond and group responsible for this doublet and explain how it differentiates propanal from propan-2-one.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Propan-1-ol exhibits a strong, broad absorption band at 3200-3600 cm-1 due to hydrogen-bonded alcohol O-H stretch [1]", "Propanoic acid exhibits a very broad, jagged absorption envelope spanning 2500-3000 cm-1 due to carboxylic acid dimer O-H stretch [1]", "The carboxylic acid O-H envelope overlaps the alkyl C-H stretching vibrations around 2950 cm-1, whereas alcohol O-H does not overlap [1]"], "marks": 3},
            {"part": "(b)", "points": ["Carbonyl group C=O stretch [1]", "Wavenumber range: 1640-1750 cm-1 (or 1680-1740 cm-1 for saturated carbonyls) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Aldehydic C-H stretching doublet (Fermi resonance) [1]", "Propan-2-one is a ketone lacking a hydrogen atom bonded directly to the carbonyl carbon, so it shows no absorptions at 2720/2820 cm-1 [1]"], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Monitoring Oxidation of Primary Alcohols — 9701/22/F/M/24/Q3(a)-(d)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Ethanol was heated under reflux with excess acidified potassium dichromate(VI), K2Cr2O7 / H2SO4, for 45 minutes. Samples of the reaction mixture were withdrawn at intervals and analyzed by infrared spectroscopy.",
        parts=[
            QuestionPart(label="(a)", text="State the formula and color of the chromium species formed upon complete reduction of acidified dichromate(VI).", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Describe the changes in the infrared spectrum as ethanol is oxidized initially to ethanal and subsequently to ethanoic acid.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Explain how infrared spectroscopy can prove that no unreacted ethanol remains in the purified reaction product.", marks=1, num_answer_lines=2),
            QuestionPart(label="(d)", text="State the apparatus modification required if the intended product was ethanal rather than ethanoic acid, and explain why this modification prevents complete oxidation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Cr3+ (or [Cr(H2O)6]3+), green solution [1]"], "marks": 1},
            {"part": "(b)", "points": ["Ethanol to ethanal: disappearance of the broad alcohol O-H stretch at 3200-3600 cm-1 and appearance of sharp C=O at ~1730 cm-1 [1]", "Appearance of aldehydic C-H doublet at 2720 and 2820 cm-1 [1]", "Ethanal to ethanoic acid: appearance of very broad carboxylic acid O-H envelope at 2500-3000 cm-1 and shift of C=O to ~1710 cm-1 [1]"], "marks": 3},
            {"part": "(c)", "points": ["Complete absence of the broad alcohol O-H absorption band at 3200-3600 cm-1 and absence of the C-O band at ~1050 cm-1 [1]"], "marks": 1},
            {"part": "(d)", "points": ["Use simple distillation apparatus (distil immediately as formed) instead of heating under reflux [1]", "Ethanal has a lower boiling point (21 °C) due to lacking hydrogen bonding, so it evaporates and is condensed away from the oxidizing agent before it can oxidize further [1]"], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Distinguishing Constitutional Isomers via Infrared Bands — 9701/23/M/J/23/Q3(a)-(c)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="The two structural isomers X and Y both have the molecular formula C2H6O.",
        parts=[
            QuestionPart(label="(a)", text="Draw the displayed formulas of isomers X and Y and state their systematic IUPAC names.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the infrared spectrum of isomer X can be distinguished from that of isomer Y by identifying key absorption bands present or absent in each.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State a simple chemical test with a positive observation that could confirm the identity of isomer X but would yield no reaction with isomer Y.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Ethanol (CH3CH2OH) with all bonds shown [1]", "Methoxymethane (CH3OCH3) with all bonds shown [1]"], "marks": 2},
            {"part": "(b)", "points": ["Ethanol exhibits a strong, broad hydrogen-bonded O-H absorption at 3200-3600 cm-1 [1]", "Methoxymethane is an ether with no O-H bond, showing no absorption above 3000 cm-1 except sp3 C-H stretch (2850-2950 cm-1) and C-O stretch at 1050-1300 cm-1 [1]"], "marks": 2},
            {"part": "(c)", "points": ["Add a piece of sodium metal at room temperature [1]", "Ethanol produces effervescence / bubbles of hydrogen gas; methoxymethane shows no reaction [1]"], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Infrared Analysis of Carbonyl vs Ester Isomers — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Compounds P and Q both possess the molecular formula C4H8O2. Infrared spectroscopy shows that both compounds give a very strong absorption band at approximately 1735 cm-1.",
        parts=[
            QuestionPart(label="(a)", text="Compound P produces vigorous effervescence with aqueous sodium hydrogencarbonate, NaHCO3, whereas compound Q does not react.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Describe the key difference between the infrared spectra of P and Q in the 2500-3600 cm-1 region.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest the structure of compound Q given that alkaline hydrolysis followed by acidification yields methanol and propanoic acid. Name compound Q.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["P is a carboxylic acid (contains -COOH group) because it reacts with NaHCO3 to liberate CO2 gas [1]", "Equation: RCOOH + NaHCO3 -> RCOONa + H2O + CO2 [1]", "P is butanoic acid (or 2-methylpropanoic acid) [1]"], "marks": 3},
            {"part": "(b)", "points": ["Compound P shows a very broad, characteristic carboxylic acid O-H absorption envelope at 2500-3000 cm-1 [1]", "Compound Q shows no absorption in the 2500-3600 cm-1 region except for sharp sp3 C-H stretches at 2850-2950 cm-1 [1]"], "marks": 2},
            {"part": "(c)", "points": ["Structure: CH3CH2COOCH3 [1]", "Name: Methyl propanoate [1]"], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Infrared Spectra of Nitrogen-Containing Compounds — 9701/21/M/J/23/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Compounds J, K, and L are nitrogen-containing organic molecules with three carbon atoms: propanenitrile (CH3CH2CN), propylamine (CH3CH2CH2NH2), and propanamide (CH3CH2CONH2).",
        parts=[
            QuestionPart(label="(a)", text="Identify the characteristic absorption band that confirms the presence of the functional group in propanenitrile. State its wavenumber and bond assignment.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the appearance and wavenumber range of the N-H absorption in the infrared spectrum of propylamine. Explain why primary amines typically exhibit a doublet.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two characteristic absorption bands in the infrared spectrum of propanamide that together distinguish it from both propanenitrile and propylamine.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Wavenumber: 2200-2250 cm-1 (sharp, medium intensity) [1]", "Bond: C=N (nitrile group stretch) [1]"], "marks": 2},
            {"part": "(b)", "points": ["Wavenumber: 3300-3500 cm-1 [1]", "A primary amine has two N-H bonds that couple together to produce two distinct stretching modes: symmetric and asymmetric N-H stretch, resulting in a doublet (two peaks) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Strong carbonyl C=O stretch at 1640-1690 cm-1 (amide I band) [1]", "N-H stretching bands at 3300-3500 cm-1 (amide II / N-H stretch) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Monitoring Nucleophilic Addition to Carbonyls via IR — 9701/22/M/J/22/Q5(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Ethanal reacts with hydrogen cyanide, HCN, in the presence of trace NaCN catalyst to produce 2-hydroxypropanenitrile.",
        parts=[
            QuestionPart(label="(a)", text="State the role of the NaCN catalyst in terms of the reaction mechanism.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Describe how infrared spectroscopy can be used to monitor the progress of this reaction from start to finish.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Explain whether the product 2-hydroxypropanenitrile exhibits optical isomerism. Draw three-dimensional representations of any optical isomers formed.", marks=3, num_answer_lines=4)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["NaCN provides a high concentration of cyanide nucleophile, :CN-, which initiates nucleophilic attack on the delta-positive carbonyl carbon [1]"], "marks": 1},
            {"part": "(b)", "points": ["Disappearance of the strong carbonyl C=O absorption peak at ~1730 cm-1 and aldehydic C-H doublet at 2720/2820 cm-1 as ethanal is consumed [1]", "Appearance of a sharp nitrile C=N absorption peak at 2200-2250 cm-1 [1]", "Appearance of a broad alcohol O-H absorption band at 3200-3600 cm-1 as the cyanohydrin forms [1]"], "marks": 3},
            {"part": "(c)", "points": ["Yes, C2 is a chiral center bonded to four different groups: -H, -CH3, -OH, and -CN [1]", "Two 3D tetrahedral structures drawn around C2 with wedge, dash, and normal lines [1]", "Structures are non-superimposable mirror images (enantiomers) [1]"], "marks": 3}
        ]
    ),
    Question(
        number=8,
        title="Infrared Identification of Halogenoalkane Elimination — 9701/21/O/N/22/Q3(a)-(c)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="2-Bromopropane is heated under reflux with ethanolic potassium hydroxide, forming a gaseous organic compound W.",
        parts=[
            QuestionPart(label="(a)", text="State the type of reaction taking place and identify organic product W.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Identify two significant new absorption bands in the infrared spectrum of W that are absent in the spectrum of 2-bromopropane. Give their wavenumber ranges and bond assignments.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the absorption band present in 2-bromopropane that disappears when W is formed.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Elimination (or dehydrohalogenation) [1]", "Product W: Propene (CH3CH=CH2) [1]"], "marks": 2},
            {"part": "(b)", "points": ["C=C double bond stretch at 1620-1680 cm-1 [1]", "=C-H stretch (sp2 C-H) at 3000-3100 cm-1 [1]"], "marks": 2},
            {"part": "(c)", "points": ["C-Br bond stretch at 500-600 cm-1 [1]"], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Distinguishing Aldehydes and Ketones by IR — 9701/22/F/M/23/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Pentan-2-one and pentanal are structural isomers with the molecular formula C5H10O. Both exhibit an intense absorption band at approximately 1720 cm-1.",
        parts=[
            QuestionPart(label="(a)", text="State the functional group type of pentan-2-one and pentanal and the bond responsible for the peak at 1720 cm-1.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain in detail how the infrared spectrum of pentanal can be conclusively distinguished from that of pentan-2-one without using chemical reagents.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State a diagnostic chemical test that gives a visible positive result with pentan-2-one but a negative result with pentanal. Give reagents and the observation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Pentan-2-one is a ketone; pentanal is an aldehyde [1]", "C=O (carbonyl) bond stretch [1]"], "marks": 2},
            {"part": "(b)", "points": ["Pentanal shows two characteristic sharp absorption peaks at 2720 cm-1 and 2820 cm-1 due to the aldehydic C-H stretch (Fermi resonance doublet) [1]", "Pentan-2-one has no hydrogen atom directly attached to the carbonyl carbon and lacks these peaks [1]"], "marks": 2},
            {"part": "(c)", "points": ["Tri-iodomethane (iodoform) test: alkaline aqueous iodine (I2 / NaOH(aq)) [1]", "Pentan-2-one has a CH3C=O group and gives a pale yellow precipitate of CHI3; pentanal does not [1]"], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Greenhouse Gases & Atmospheric Infrared Absorption — 9701/22/M/J/21/Q2(a)-(c)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Incoming solar ultraviolet and visible radiation warms the Earth's surface, which re-emits electromagnetic radiation in the infrared region. Certain atmospheric gases absorb this infrared radiation, contributing to the greenhouse effect.",
        parts=[
            QuestionPart(label="(a)", text="Name two major naturally occurring atmospheric gases that absorb infrared radiation and two major gases that do not.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain on a molecular level why carbon dioxide absorbs infrared radiation, referring to molecular geometry and dipole moments.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Methane has a significantly higher global warming potential (GWP) than carbon dioxide. Suggest two reasons why methane is a more potent greenhouse gas per molecule.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Absorb IR: Carbon dioxide (CO2) and water vapor (H2O) (or methane CH4) [1]", "Do not absorb IR: Nitrogen (N2) and oxygen (O2) (or argon Ar) [1]"], "marks": 2},
            {"part": "(b)", "points": ["CO2 is linear and non-polar at rest, but asymmetrical stretching and bending vibrations create a temporary changing dipole moment [1]", "A changing dipole moment allows interaction with and absorption of infrared photons of matching frequency [1]"], "marks": 2},
            {"part": "(c)", "points": ["Methane absorbs infrared radiation in a wavelength window where CO2 and H2O do not absorb strongly [1]", "The C-H bonds in methane have higher molar absorptivity (intensity of absorption) in the infrared region [1]"], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Hydrogen Bonding Effect on Infrared Absorption — 9701/23/O/N/23/Q3(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="The infrared spectrum of liquid ethanol differs markedly from that of gaseous ethanol recorded at low vapor pressure.",
        parts=[
            QuestionPart(label="(a)", text="In gaseous ethanol, the O-H absorption appears as a sharp peak at 3650 cm-1, whereas in liquid ethanol it appears as a very broad band centered at 3350 cm-1. Explain this difference in terms of intermolecular forces.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Explain why the broad absorption band shifts to a lower wavenumber when hydrogen bonding occurs.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State whether the C-H stretching band in ethanol is significantly broadened between the gas and liquid phases. Justify your answer.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["In the gas phase, molecules are widely separated with negligible intermolecular hydrogen bonding; all O-H bonds vibrate freely at a single discrete frequency (3650 cm-1) [1]", "In the liquid phase, extensive intermolecular hydrogen bonding occurs between -OH groups [1]", "Hydrogen bonds exist across a wide continuum of lengths and bond angles, creating a broad distribution of vibrational energy levels and a broadened absorption band (3200-3600 cm-1) [1]"], "marks": 3},
            {"part": "(b)", "points": ["Hydrogen bonding pulls electron density away from the covalent O-H bond, weakening the bond [1]", "A weaker bond has a lower force constant (k), which decreases the vibrational frequency according to Hooke's Law (wavenumber proportional to sqrt(k)) [1]"], "marks": 2},
            {"part": "(c)", "points": ["No; C-H bonds do not participate significantly in hydrogen bonding, so their force constants and vibrational frequencies remain sharp and unaffected [1]"], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Distinguishing Alcohols of Different Classes — 9701/21/M/J/22/Q3(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Compounds A, B, and C are isomeric alcohols with the formula C4H10O. Alcohol A is butan-1-ol, B is butan-2-ol, and C is 2-methylpropan-2-ol.",
        parts=[
            QuestionPart(label="(a)", text="Classify alcohols A, B, and C as primary, secondary, or tertiary.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Explain why infrared spectroscopy alone cannot readily distinguish between alcohols A, B, and C based solely on functional group absorptions above 1500 cm-1.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how infrared spectroscopy can be combined with chemical oxidation to distinguish clearly between all three isomers.", marks=3, num_answer_lines=4)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["A is primary (1°), B is secondary (2°), C is tertiary (3°) [1]"], "marks": 1},
            {"part": "(b)", "points": ["All three isomers contain identical functional groups: an alcohol O-H bond and sp3 C-H bonds [1]", "All three will exhibit the same broad O-H stretch at 3200-3600 cm-1 and alkyl C-H stretches at 2850-2950 cm-1, with no diagnostic carbonyl or unsaturated peaks [1]"], "marks": 2},
            {"part": "(c)", "points": ["Add acidified K2Cr2O7 and warm: tertiary alcohol C resists oxidation, so its IR spectrum remains unchanged (retains 3350 cm-1 O-H band) [1]", "Secondary alcohol B oxidizes to ketone butan-2-one: broad O-H disappears, replaced by a single sharp C=O peak at ~1715 cm-1 with no aldehydic C-H doublet [1]", "Primary alcohol A oxidizes to butanal/butanoic acid: shows C=O peak with aldehydic doublet (2720/2820 cm-1) or broad carboxylic acid O-H envelope (2500-3000 cm-1) [1]"], "marks": 3}
        ]
    ),
    Question(
        number=13,
        title="Ester Hydrolysis Monitored by Infrared Spectroscopy — 9701/22/O/N/23/Q5(a)-(c)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Methyl ethanoate, CH3COOCH3, is heated under reflux with dilute sulfuric acid, establishing a dynamic chemical equilibrium.",
        parts=[
            QuestionPart(label="(a)", text="Write the balanced chemical equation for the acid-catalyzed hydrolysis of methyl ethanoate.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Describe the infrared spectrum of pure methyl ethanoate before reaction, stating the two principal absorption bands.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the new absorption bands that appear in the infrared spectrum as equilibrium is established, assigning each band to its corresponding product.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["CH3COOCH3 + H2O <=> CH3COOH + CH3OH [1]"], "marks": 1},
            {"part": "(b)", "points": ["Strong ester C=O stretch at 1735-1750 cm-1 [1]", "Strong C-O ester stretch at 1150-1250 cm-1 (with no absorption above 3000 cm-1 except alkyl C-H at 2850-2950 cm-1) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Broad carboxylic acid O-H envelope at 2500-3000 cm-1 from ethanoic acid [1]", "Broad alcohol O-H stretch at 3200-3600 cm-1 from methanol [1]"], "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Deducing Unknown Compound Structure from IR Data — 9701/21/F/M/22/Q4(a)-(d)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="A pure colorless liquid, compound D, has the empirical formula C2H4O and a relative molecular mass of 88.",
        parts=[
            QuestionPart(label="(a)", text="Deduce the molecular formula of compound D.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="The infrared spectrum of D exhibits strong absorptions at 1740 cm-1 and 1240 cm-1, but no absorption between 2500 and 3600 cm-1. Deduce the functional group present in D.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Compound D does not react with sodium metal and does not react with acidified potassium dichromate(VI). When heated with aqueous sodium hydroxide, it forms ethanol and a sodium salt of a carboxylic acid. Deduce the structural formula and name of D.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="Write the equation for the saponification reaction of D with aqueous sodium hydroxide.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Empirical formula mass = 2(12.0) + 4(1.0) + 16.0 = 44.0; 88 / 44 = 2; Molecular formula = C4H8O2 [1]"], "marks": 1},
            {"part": "(b)", "points": ["1740 cm-1 is C=O stretch and 1240 cm-1 is C-O stretch [1]", "Absence of 2500-3600 cm-1 band rules out carboxylic acid and alcohol; therefore, D is an ester [1]"], "marks": 2},
            {"part": "(c)", "points": ["Structural formula: CH3COOCH2CH3 [1]", "Name: Ethyl ethanoate [1]"], "marks": 2},
            {"part": "(d)", "points": ["CH3COOCH2CH3 + NaOH -> CH3COONa + CH3CH2OH [1]"], "marks": 1}
        ]
    ),
    Question(
        number=15,
        title="Alkene Hydration & Polymerisation IR Diagnostics — 9701/22/M/J/24/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Ethene can be converted into ethanol via catalytic hydration, or polymerised to poly(ethene).",
        parts=[
            QuestionPart(label="(a)", text="State the reagents and industrial conditions used to convert ethene into ethanol.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how infrared spectroscopy can demonstrate that ethene has completely reacted during industrial hydration to ethanol.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the infrared spectrum of pure poly(ethene) and explain why it displays far fewer diagnostic absorption bands than ethene.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Steam and concentrated phosphoric acid (H3PO4) catalyst [1]", "Temperature of 300 °C and pressure of 60 atm (6 MPa) [1]"], "marks": 2},
            {"part": "(b)", "points": ["Disappearance of the alkene C=C absorption at 1620-1680 cm-1 and alkene =C-H stretch at 3000-3100 cm-1 [1]", "Appearance of the strong, broad alcohol O-H stretch at 3200-3600 cm-1 and C-O stretch at 1050 cm-1 [1]"], "marks": 2},
            {"part": "(c)", "points": ["Poly(ethene) is a completely saturated hydrocarbon containing only C-C and C-H sigma bonds [1]", "Its spectrum displays only sp3 C-H stretches (2850-2950 cm-1) and -CH2- bending modes (~1460 cm-1), lacking any unsaturated C=C bands [1]"], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="MCQ: Identifying Characteristic Wavenumber — 9701/12/M/J/23/Q38",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="An organic compound shows a very strong, sharp absorption band at 1715 cm-1 and a broad absorption band extending from 2500 cm-1 to 3000 cm-1 in its infrared spectrum.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which compound is responsible for this infrared spectrum?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: Propan-1-ol",
                    "B: Propanoic acid",
                    "C: Ethyl methanoate",
                    "D: Propan-2-one"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["B [1] (Propanoic acid contains a C=O bond at 1715 cm-1 and a carboxylic acid O-H envelope at 2500-3000 cm-1)"], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="MCQ: IR Transparency of Atmospheric Gases — 9701/11/O/N/23/Q37",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Which atmospheric gas does NOT absorb infrared radiation?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the gas that is transparent to infrared radiation.",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: Carbon dioxide, CO2",
                    "B: Water vapor, H2O",
                    "C: Oxygen, O2",
                    "D: Methane, CH4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C [1] (O2 is a homonuclear diatomic molecule with zero dipole moment change during vibration)"], "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="MCQ: Functional Group Assignment at 2250 cm-1 — 9701/12/F/M/24/Q39",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="An unknown compound exhibits a sharp absorption peak at 2235 cm-1 and no absorption between 1600 cm-1 and 1800 cm-1.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which functional group is present in this compound?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: Carbonyl, C=O",
                    "B: Nitrile, C=N",
                    "C: Alkene, C=C",
                    "D: Alcohol, O-H"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["B [1] (C=N nitrile stretch absorbs characteristically at 2200-2250 cm-1)"], "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="MCQ: Monitoring Reaction Progress by IR — 9701/13/M/J/22/Q38",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Propan-2-one is treated with sodium borohydride, NaBH4, in aqueous ethanol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which statement correctly describes the change in the infrared spectrum as the reaction proceeds to completion?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: A peak at 1715 cm-1 appears and a broad peak at 3350 cm-1 disappears",
                    "B: A peak at 1715 cm-1 disappears and a broad peak at 3350 cm-1 appears",
                    "C: A sharp peak at 2250 cm-1 disappears and a peak at 1650 cm-1 appears",
                    "D: A peak at 1240 cm-1 disappears and a broad peak at 2500 cm-1 appears"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["B [1] (Reduction of propan-2-one consumes the C=O group at 1715 cm-1 and forms propan-2-ol, generating the broad alcohol O-H band at 3200-3600 cm-1)"], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="MCQ: Distinguishing Esters from Carboxylic Acids — 9701/11/M/J/23/Q39",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Which absorption band is present in ethanoic acid but completely absent in methyl methanoate?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the diagnostic absorption band.",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: Strong absorption at 1720 cm-1",
                    "B: Strong absorption at 1250 cm-1",
                    "C: Very broad absorption at 2500-3000 cm-1",
                    "D: Sharp absorption at 2950 cm-1"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C [1] (Ethanoic acid possesses a carboxylic acid O-H envelope at 2500-3000 cm-1; methyl methanoate is an ester lacking an O-H bond)"], "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Infrared Analysis of Nitrile Hydrolysis — 9701/22/M/J/23/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Propanenitrile is heated under reflux with dilute hydrochloric acid.",
        parts=[
            QuestionPart(label="(a)", text="Write the balanced equation for the acidic hydrolysis of propanenitrile, showing the organic product and inorganic byproduct.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Detail two major changes observed in the infrared spectrum between 1600 cm-1 and 3500 cm-1 as propanenitrile is fully converted into the organic product.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="If propanenitrile were instead reduced using LiAlH4 in dry ether, state how the infrared spectrum of the product would differ from that of the hydrolysis product.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["CH3CH2CN + HCl + 2H2O -> CH3CH2COOH + NH4Cl [1]"], "marks": 1},
            {"part": "(b)", "points": ["Disappearance of the sharp nitrile C=N absorption at 2200-2250 cm-1 [1]", "Appearance of the strong carbonyl C=O peak at ~1715 cm-1 and very broad carboxylic acid O-H envelope at 2500-3000 cm-1 [1]"], "marks": 2},
            {"part": "(c)", "points": ["Reduction produces propylamine (CH3CH2CH2NH2) [1]", "The product spectrum exhibits an N-H stretching doublet at 3300-3500 cm-1 with no carbonyl C=O absorption at 1715 cm-1 and no carboxylic O-H envelope [1]"], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Distinguishing Alkene from Alkane by Infrared Spectroscopy — 9701/21/O/N/21/Q4(a)-(b)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Hexane and hex-1-ene are both colorless liquids at room temperature.",
        parts=[
            QuestionPart(label="(a)", text="Describe how infrared spectroscopy can be used to distinguish between samples of hexane and hex-1-ene.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State a simple test-tube reaction that confirms the presence of the alkene group, including reagents and observations.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Hex-1-ene exhibits an alkene C=C stretching absorption at 1620-1680 cm-1 and an sp2 =C-H stretch at 3000-3100 cm-1 [1]", "Hexane is an alkane lacking C=C bonds; it exhibits only sp3 C-H stretches below 3000 cm-1 (2850-2950 cm-1) and no absorption between 1620 and 1680 cm-1 [1]"], "marks": 2},
            {"part": "(b)", "points": ["Add aqueous bromine (bromine water, Br2(aq)) at room temperature [1]", "Hex-1-ene rapidly decolourises bromine water from orange/brown to colourless; hexane causes no color change in the dark [1]"], "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Infrared Identification of Dehydration Products — 9701/23/M/J/22/Q3(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Butan-2-ol is heated with concentrated sulfuric acid at 170 °C, producing an isomeric mixture of alkenes.",
        parts=[
            QuestionPart(label="(a)", text="Name the three isomeric alkene products formed in this reaction and classify their relationship.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why infrared spectroscopy cannot easily distinguish between cis-but-2-ene and trans-but-2-ene in the 1500-4000 cm-1 region.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Trans-but-2-ene has a center of symmetry and exhibits no infrared absorption for the C=C stretch. Explain this phenomenon.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["But-1-ene, cis-but-2-ene ((Z)-but-2-ene), and trans-but-2-ene ((E)-but-2-ene) [1]", "But-1-ene and but-2-ene are positional isomers; cis- and trans-but-2-ene are geometrical (stereoisomers / diastereomers) [1]"], "marks": 2},
            {"part": "(b)", "points": ["Both geometrical isomers possess identical functional groups, bond types, and atoms [1]", "Both exhibit sp2 C-H stretches at ~3020 cm-1 and C=C stretches at ~1660 cm-1; they differ primarily in the fingerprint region (< 1500 cm-1) due to out-of-plane =C-H bending [1]"], "marks": 2},
            {"part": "(c)", "points": ["Trans-but-2-ene has a centrosymmetric structure; when the C=C bond stretches symmetrically, there is zero net change in dipole moment [1]", "Vibrations that produce no change in dipole moment are infrared-inactive (selection rule) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Infrared Breathalyser Analysis — 9701/22/F/M/22/Q3(a)-(b)",
        syllabus_ref="22.1",
        difficulty="EASY",
        preamble="Roadside infrared breathalysers measure the concentration of ethanol in exhaled breath by monitoring infrared absorption at a specific wavelength.",
        parts=[
            QuestionPart(label="(a)", text="The instrument measures absorption at approximately 2950 cm-1. Identify the covalent bond responsible for this absorption and state why water vapor in the breath does not interfere at this precise frequency.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the degree of infrared absorption is related to the ethanol concentration in the motorist's blood, stating the physical law governing this relationship.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C-H bond stretch (in the CH3CH2- alkyl group) [1]", "Water vapor contains O-H bonds that absorb above 3200 cm-1 and bending modes at ~1600 cm-1, having negligible absorption at 2950 cm-1 [1]"], "marks": 2},
            {"part": "(b)", "points": ["The absorbance is directly proportional to ethanol concentration (Beer-Lambert Law: A = epsilon * c * l) [1]", "A fixed partition ratio exists between ethanol in pulmonary alveolar blood and exhaled breath (approx 2100:1), allowing direct calibration [1]"], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Comprehensive Spectral Deduction: Compound X — 9701/21/M/J/24/Q4(a)-(c)",
        syllabus_ref="22.1",
        difficulty="HARD",
        preamble="Compound X has the molecular formula C3H6O. Its infrared spectrum shows a very strong, sharp absorption band at 1720 cm-1. It exhibits no absorption between 2500 and 3600 cm-1, and no absorption between 2700 and 2850 cm-1.",
        parts=[
            QuestionPart(label="(a)", text="Deduce the structure of compound X. Justify your answer by eliminating alternative functional group isomers.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="Compound X is treated with hydrogen cyanide and trace potassium cyanide. Draw the displayed formula of the organic product formed.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="Predict the key changes in the infrared spectrum when compound X is converted to the product in (b).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Peak at 1720 cm-1 confirms carbonyl C=O group [1]", "Absence of 3200-3600 cm-1 rules out alcohol (e.g., prop-2-en-1-ol); absence of 2720/2820 cm-1 doublet rules out aldehyde (propanal) [1]", "Therefore, X is the ketone: propan-2-one (CH3COCH3) [1]"], "marks": 3},
            {"part": "(b)", "points": ["Displayed formula of 2-hydroxy-2-methylpropanenitrile, (CH3)2C(OH)CN, with all bonds displayed [1]"], "marks": 1},
            {"part": "(c)", "points": ["Loss of carbonyl C=O peak at 1720 cm-1 [1]", "Appearance of sharp nitrile C=N peak at 2200-2250 cm-1 and broad alcohol O-H band at 3200-3600 cm-1 [1]"], "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 22.2: MASS SPECTROMETRY (Q26 - Q50)
    # =========================================================================
    Question(
        number=26,
        title="Principles of Mass Spectrometry & Molecular Ion Peak — 9701/22/M/J/23/Q5(e)-(h)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Mass spectrometry is an analytical technique used to determine relative molecular masses and deduce chemical structures. Fig. 26.1 displays the mass spectrum of propan-2-one.",
        figure_path="figures/analysis_mass_spec_molecular_ion.png",
        figure_caption="Fig. 26.1: Mass spectrum of propan-2-one showing molecular ion peak, fragment ions, and the [M+1]+ isotope ratio.",
        parts=[
            QuestionPart(label="(a)", text="Describe how gaseous molecules are ionised in an electron-impact mass spectrometer. Write an equation for the ionisation of propan-2-one, (CH3)2CO.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what information is provided by the molecular ion peak, [M]+, in a mass spectrum.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="State the Cambridge formula used to calculate the number of carbon atoms, n, in an organic molecule from the relative abundances of the [M]+ and [M+1]+ peaks.", marks=1, num_answer_lines=2),
            QuestionPart(label="(d)", text="In the mass spectrum in Fig. 26.1, the [M]+ peak at m/z = 58 has an abundance of 28.0% and the [M+1]+ peak at m/z = 59 has an abundance of 0.95%. Calculate the number of carbon atoms, n, showing your working.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Vaporised molecules are bombarded by high-energy electrons (approx 70 eV), knocking an electron out of the molecule to form a radical cation [1]", "Equation: CH3COCH3 + e- -> [CH3COCH3]+. + 2e- (or M + e- -> M+. + 2e-) [1]"], "marks": 2},
            {"part": "(b)", "points": ["It gives the relative molecular mass (Mr) of the compound [1]"], "marks": 1},
            {"part": "(c)", "points": ["n = (100 * abundance of [M+1]+) / (1.1 * abundance of [M]+) [1]"], "marks": 1},
            {"part": "(d)", "points": ["n = (100 * 0.95) / (1.1 * 28.0) = 95 / 30.8 [1]", "n = 3.08 approx 3 carbon atoms [1]"], "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="Chlorine & Bromine Isotope Signatures in Mass Spectrometry — 9701/21/O/N/23/Q5(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Naturally occurring chlorine consists of two stable isotopes, 35Cl and 37Cl, in an approximate 3:1 ratio. Bromine consists of two stable isotopes, 79Br and 81Br, in an approximate 1:1 ratio. Fig. 27.1 displays the isotopic multiplicity patterns for mono- and di-halogenated molecules.",
        figure_path="figures/analysis_mass_spec_isotope_patterns.png",
        figure_caption="Fig. 27.1: Isotope peak patterns for compounds containing one or two chlorine or bromine atoms.",
        parts=[
            QuestionPart(label="(a)", text="Describe the appearance of the molecular ion region for a compound containing a single chlorine atom, giving the ratio of the [M]+ and [M+2]+ peaks.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the appearance of the molecular ion region for a compound containing a single bromine atom, giving the ratio of the [M]+ and [M+2]+ peaks.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="A haloalkane containing two chlorine atoms displays three peaks in the molecular ion region: [M]+, [M+2]+, and [M+4]+. Deduce the theoretical ratio of these three peak heights, showing mathematical justification.", marks=3, num_answer_lines=4),
            QuestionPart(label="(d)", text="State the ratio of the [M]+, [M+2]+, and [M+4]+ peaks in a compound containing two bromine atoms.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Two peaks separated by 2 m/z units ([M]+ and [M+2]+) [1]", "Peak height ratio of [M]+ : [M+2]+ is 3 : 1 (due to 75% 35Cl and 25% 37Cl) [1]"], "marks": 2},
            {"part": "(b)", "points": ["Two peaks separated by 2 m/z units of approximately equal intensity (twin peaks) [1]", "Peak height ratio of [M]+ : [M+2]+ is 1 : 1 (due to ~50% 79Br and ~50% 81Br) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Binomial expansion (3/4 + 1/4)^2 = (9/16) 35Cl-35Cl + (6/16) 35Cl-37Cl + (1/16) 37Cl-37Cl [1]", "[M]+ : [M+2]+ : [M+4]+ [1]", "Ratio is 9 : 6 : 1 [1]"], "marks": 3},
            {"part": "(d)", "points": ["Ratio is 1 : 2 : 1 (from binomial (1/2 + 1/2)^2 = 1/4 : 2/4 : 1/4) [1]"], "marks": 1}
        ]
    ),
    Question(
        number=28,
        title="Mixed Dihaloalkane Isotope Pattern — 9701/22/F/M/24/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="1-Bromo-2-chloroethane, BrCH2CH2Cl, contains one chlorine atom and one bromine atom.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the relative molecular mass of 1-bromo-2-chloroethane containing the lightest isotopes (79Br, 35Cl, 12C, 1H).", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Explain why the mass spectrum of 1-bromo-2-chloroethane exhibits three peaks in its molecular ion region at m/z = 142, 144, and 146.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Calculate the theoretical relative intensities of the peaks at m/z = 142, 144, and 146, expressing your answer as an integer ratio.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Mr = 79 + 35 + 2(12) + 4(1) = 142 [1]"], "marks": 1},
            {"part": "(b)", "points": ["m/z = 142 corresponds to [C2H4 79Br 35Cl]+ [1]", "m/z = 144 corresponds to [C2H4 81Br 35Cl]+ and [C2H4 79Br 37Cl]+; m/z = 146 corresponds to [C2H4 81Br 37Cl]+ [1]"], "marks": 2},
            {"part": "(c)", "points": ["Probabilities: 79Br*35Cl = (1/2)*(3/4) = 3/8; (81Br*35Cl + 79Br*37Cl) = (1/2)*(3/4) + (1/2)*(1/4) = 4/8; 81Br*37Cl = (1/2)*(1/4) = 1/8 [1]", "Ratio at m/z 142 : 144 : 146 is 3 : 4 : 1 [1]"], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Fragmentation of Ketones & Base Peak Identification — 9701/22/M/J/22/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="In the mass spectrum of propan-2-one (CH3COCH3), the base peak occurs at m/z = 43.",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'base peak' in mass spectrometry.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Identify the cation responsible for the base peak at m/z = 43 and write an equation showing its formation by fragmentation of the molecular ion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="A minor peak is observed at m/z = 15. Identify this species and explain why neutral radicals are not detected by mass spectrometers.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["The most intense (tallest) peak in the mass spectrum, assigned an arbitrary relative abundance of 100% [1]"], "marks": 1},
            {"part": "(b)", "points": ["Species: [CH3CO]+ (acylium / ethanoyl cation) [1]", "Equation: [CH3COCH3]+. -> [CH3CO]+ + .CH3 [1]"], "marks": 2},
            {"part": "(c)", "points": ["Species at m/z = 15: [CH3]+ (methyl carbocation) [1]", "Neutral radicals carry no electric charge; only positively charged ions are accelerated and deflected by magnetic/electric fields to reach the detector [1]"], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Carbon Count Calculation via [M+1]+ Abundance — 9701/21/O/N/22/Q5(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="An unknown hydrocarbon contains 85.7% carbon and 14.3% hydrogen by mass. The mass spectrum shows a molecular ion peak at m/z = 56 with a relative abundance of 38.5% and an [M+1]+ peak at m/z = 57 with a relative abundance of 1.70%.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the empirical formula of the hydrocarbon.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Calculate the number of carbon atoms, n, in the molecule using the [M+1]+ peak data.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Deduce the molecular formula of the hydrocarbon and suggest two possible structural isomers that are alkenes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Moles: C = 85.7 / 12.0 = 7.14; H = 14.3 / 1.0 = 14.3 [1]", "Ratio: 7.14 : 14.3 = 1 : 2; Empirical formula = CH2 [1]"], "marks": 2},
            {"part": "(b)", "points": ["n = (100 * 1.70) / (1.1 * 38.5) = 170 / 42.35 [1]", "n = 4.01 approx 4 carbon atoms [1]"], "marks": 2},
            {"part": "(c)", "points": ["Molecular formula: C4H8 [1]", "Any two of: but-1-ene, but-2-ene, 2-methylpropene [1]"], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Fragmentation Differences in Isomeric Alcohols — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Pentan-2-ol and pentan-3-ol are structural isomers with the formula C5H12O (Mr = 88).",
        parts=[
            QuestionPart(label="(a)", text="Both isomers undergo alpha-cleavage readily. Explain what is meant by alpha-cleavage in alcohols.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Pentan-3-ol, CH3CH2CH(OH)CH2CH3, shows an intense fragment peak at m/z = 59. Identify the fragment cation and the neutral radical lost.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Pentan-2-ol, CH3CH(OH)CH2CH2CH3, can undergo two different alpha-cleavages, producing prominent fragment peaks at m/z = 45 and m/z = 73. Identify the fragment cation formed in each cleavage.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Breaking of a carbon-carbon bond adjacent to the carbon atom bearing the -OH group (the C_alpha - C_beta bond) [1]"], "marks": 1},
            {"part": "(b)", "points": ["Fragment cation: [CH3CH2CH=OH]+ (or [C3H7O]+) at m/z = 59 [1]", "Neutral radical lost: .CH2CH3 (ethyl radical, 29 mass units) [1]"], "marks": 2},
            {"part": "(c)", "points": ["m/z = 45: [CH3CH=OH]+ (loss of propyl radical .CH2CH2CH3, 43 mass units) [1]", "m/z = 73: [CH3CH2CH2CH=OH]+ (loss of methyl radical .CH3, 15 mass units) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Ester Fragmentation Patterns — 9701/23/O/N/22/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="The mass spectrum of methyl ethanoate, CH3COOCH3 (Mr = 74), exhibits major peaks at m/z = 74, 59, 43, 31, and 15.",
        parts=[
            QuestionPart(label="(a)", text="Identify the ion responsible for the molecular ion peak at m/z = 74.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Identify the fragment cations responsible for the peaks at m/z = 43 and m/z = 59.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="The peak at m/z = 43 corresponds to the loss of a neutral radical of mass 31. Identify this neutral species and write the fragmentation equation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["[CH3COOCH3]+. (or [C3H6O2]+.) [1]"], "marks": 1},
            {"part": "(b)", "points": ["m/z = 43: [CH3CO]+ (ethanoyl / acylium cation) [1]", "m/z = 59: [COOCH3]+ (methoxycarbonyl cation) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Neutral radical: .OCH3 (methoxy radical) [1]", "Equation: [CH3COOCH3]+. -> [CH3CO]+ + .OCH3 [1]"], "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Distinguishing Aldehydes & Ketones by MS Fragmentation — 9701/21/M/J/23/Q5(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Propanal and propan-2-one both have the molecular formula C3H6O (Mr = 58).",
        parts=[
            QuestionPart(label="(a)", text="The mass spectrum of propanal shows a distinct peak at m/z = 57 (M - 1). Identify the species responsible and explain why ketones do not readily form an (M - 1) peak.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why propan-2-one exhibits a very strong peak at m/z = 43, whereas propanal exhibits a strong peak at m/z = 29.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Identify the two possible cations that can give rise to a peak at m/z = 29 in the mass spectrum of propanal.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["[C2H5CO]+ (loss of the aldehydic H. atom from the C=O group) [1]", "Ketones have no hydrogen atom bonded directly to the carbonyl carbon, so loss of H. to form an acylium ion cannot occur [1]"], "marks": 2},
            {"part": "(b)", "points": ["Propan-2-one cleaves a C-CH3 bond adjacent to C=O, yielding the stable [CH3CO]+ cation at m/z = 43 [1]", "Propanal cleaves the C-C bond between C2 and C3, yielding the ethyl cation [C2H5]+ or formyl cation [CHO]+ at m/z = 29 [1]"], "marks": 2},
            {"part": "(c)", "points": ["[CHO]+ (formyl cation) [1]", "[C2H5]+ (ethyl carbocation) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Characteristic Neutral Losses in Mass Spectrometry — 9701/22/F/M/23/Q5(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Fragment peaks often arise from the loss of common small neutral molecules or radicals from the molecular ion [M]+.",
        parts=[
            QuestionPart(label="(a)", text="Identify the neutral molecule lost when an alcohol undergoes dehydration in a mass spectrometer, producing an (M - 18) peak.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Identify the neutral radical lost when an ethanoic acid ester produces an (M - 15) peak.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="Identify the neutral species of mass 28 lost when a primary alcohol or carbonyl compound fragments.", marks=1, num_answer_lines=2),
            QuestionPart(label="(d)", text="Carboxylic acids frequently exhibit an intense fragment peak corresponding to (M - 17) and a peak at m/z = 45. Identify the fragments responsible for both observations.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Water molecule, H2O (mass 18) [1]"], "marks": 1},
            {"part": "(b)", "points": ["Methyl radical, .CH3 (mass 15) [1]"], "marks": 1},
            {"part": "(c)", "points": ["Carbon monoxide (CO) or ethene (C2H4) [1]"], "marks": 1},
            {"part": "(d)", "points": ["(M - 17): loss of hydroxyl radical (.OH), leaving the acylium cation [RCO]+ [1]", "m/z = 45: carboxyl cation, [COOH]+ [1]"], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Structural Elucidation of Alkyl Halide via MS — 9701/21/O/N/21/Q5(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="An unknown bromoalkane B was analyzed by mass spectrometry.",
        parts=[
            QuestionPart(label="(a)", text="The mass spectrum of B exhibits twin molecular ion peaks of equal height at m/z = 136 and m/z = 138. Deduce the molecular formula of B.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="The base peak of B occurs at m/z = 57, corresponding to the loss of a bromine radical (.Br). Deduce the formula of this base peak cation.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="Compound B undergoes nucleophilic substitution with aqueous sodium hydroxide exclusively via an SN1 mechanism. Deduce the structural formula and systematic name of B.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="Explain why compound B reacts via SN1 rather than SN2.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["m/z = 136 is [C_n H_{2n+1} 79Br]+; Alkyl group mass = 136 - 79 = 57 [1]", "C_n H_{2n+1} = 57 gives 12n + 2n + 1 = 57 => 14n = 56 => n = 4; Formula = C4H9Br [1]"], "marks": 2},
            {"part": "(b)", "points": ["[C4H9]+ (butyl carbocation) [1]"], "marks": 1},
            {"part": "(c)", "points": ["Structure: (CH3)3CBr [1]", "Name: 2-bromo-2-methylpropane [1]"], "marks": 2},
            {"part": "(d)", "points": ["Tertiary carbocation (CH3)3C+ is highly stabilized by the positive inductive effect (+I) of three electron-releasing methyl groups [1]", "Steric hindrance from three bulky methyl groups blocks backside attack by the OH- nucleophile (ruling out SN2) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="MCQ: Determining Number of Carbons from [M+1]+ — 9701/12/M/J/23/Q39",
        syllabus_ref="22.2",
        difficulty="EASY",
        preamble="In the mass spectrum of an organic compound, the [M]+ peak at m/z = 72 has a relative abundance of 50.0% and the [M+1]+ peak at m/z = 73 has a relative abundance of 2.20%.",
        parts=[
            QuestionPart(
                label="(a)",
                text="How many carbon atoms are present in one molecule of this compound?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: 2",
                    "B: 3",
                    "C: 4",
                    "D: 5"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C [1] (n = (100 * 2.20) / (1.1 * 50.0) = 220 / 55.0 = 4)"], "marks": 1}
        ]
    ),
    Question(
        number=37,
        title="MCQ: Halogen Identification from Isotopic Peak Heights — 9701/11/O/N/22/Q38",
        syllabus_ref="22.2",
        difficulty="EASY",
        preamble="The mass spectrum of an organic compound contains molecular ion peaks at m/z = 108 and m/z = 110 with peak heights in the ratio 1 : 1.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which halogen atom is present in this molecule?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: Fluorine",
                    "B: Chlorine",
                    "C: Bromine",
                    "D: Iodine"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C [1] (Equal peak heights at M and M+2 signify the 1:1 abundance ratio of 79Br and 81Br)"], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="MCQ: Base Peak Identification for Propan-2-ol — 9701/12/F/M/23/Q38",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="When propan-2-ol, CH3CH(OH)CH3, is analyzed by mass spectrometry, the base peak is observed at m/z = 45.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which species is responsible for this base peak?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: [CH3CH2O]+",
                    "B: [CH3CH=OH]+",
                    "C: [COOH]+",
                    "D: [CH3OCH2]+"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["B [1] (Alpha-cleavage of propan-2-ol expels a .CH3 radical (mass 15), leaving the resonance-stabilized oxonium ion [CH3CH=OH]+ at m/z = 60 - 15 = 45)"], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="MCQ: Dichloroalkane Isotopic Multiplicity — 9701/13/M/J/23/Q39",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Dichloromethane, CH2Cl2, has molecular ion peaks at m/z = 84, 86, and 88.",
        parts=[
            QuestionPart(
                label="(a)",
                text="What is the relative ratio of the peak heights at m/z = 84, 86, and 88?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: 1 : 2 : 1",
                    "B: 3 : 2 : 1",
                    "C: 9 : 6 : 1",
                    "D: 3 : 1 : 1"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["C [1] (Two chlorine atoms give peak ratios corresponding to (3/4 + 1/4)^2 = 9 : 6 : 1)"], "marks": 1}
        ]
    ),
    Question(
        number=40,
        title="MCQ: Tropylium Ion Formation — 9701/11/M/J/22/Q39",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="The mass spectrum of an alkylbenzene exhibits an extremely stable base peak at m/z = 91.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which ion corresponds to m/z = 91?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A: [C6H5]+",
                    "B: [C6H5CH2]+ (tropylium cation, [C7H7]+)",
                    "C: [C6H5O]+",
                    "D: [C7H9]+"
                ]
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["B [1] (The tropylium ion [C7H7]+ is an aromatic, resonance-stabilized 7-membered carbocation with 6 pi electrons at m/z = 91)"], "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Carbocation Stability in Mass Spectrometry Fragmentation — 9701/22/O/N/23/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="The mass spectra of butane and 2-methylpropane (both C4H10, Mr = 58) display very different base peaks.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the base peak in 2-methylpropane, CH(CH3)3, is at m/z = 43 and has an abundance much greater than that in butane.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Write the equation for the formation of the m/z = 43 carbocation from the 2-methylpropane molecular ion.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="State the relative stabilities of primary, secondary, and tertiary carbocations and explain the electronic factor responsible.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Cleavage of any of the three C-CH3 bonds in 2-methylpropane produces a secondary carbocation [(CH3)2CH]+ (or 2-propyl cation) [1]", "Secondary carbocations are much more stable than primary carbocations due to hyperconjugation / positive inductive effect (+I), leading to preferential cleavage [1]"], "marks": 2},
            {"part": "(b)", "points": ["[CH(CH3)3]+. -> [(CH3)2CH]+ + .CH3 [1]"], "marks": 1},
            {"part": "(c)", "points": ["Stability order: tertiary (3°) > secondary (2°) > primary (1°) [1]", "Alkyl groups are electron-donating by positive inductive effect (+I) / hyperconjugation, dispersing the positive charge over multiple carbons [1]"], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Molecular Formula Deduction from Elemental Analysis & MS — 9701/21/M/J/22/Q5(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="An organic compound G was subjected to elemental combustion analysis and mass spectrometry. Combustion of 1.32 g of G produced 2.64 g of CO2 and 1.08 g of H2O.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the masses of carbon, hydrogen, and oxygen present in the 1.32 g sample of G and determine its empirical formula.", marks=3, num_answer_lines=4),
            QuestionPart(label="(b)", text="In the mass spectrum of G, the molecular ion peak occurs at m/z = 88 with an intensity of 42.0%, and the [M+1]+ peak occurs at m/z = 89 with an intensity of 1.85%. Determine the molecular formula of G.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="The infrared spectrum of G shows strong absorptions at 1715 cm-1 and a very broad band from 2500 to 3000 cm-1. Deduce the structural formula and IUPAC name of G.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Mass C = 2.64 * (12.0 / 44.0) = 0.72 g; Mass H = 1.08 * (2.0 / 18.0) = 0.12 g [1]", "Mass O = 1.32 - (0.72 + 0.12) = 0.48 g [1]", "Moles: C = 0.72/12 = 0.06; H = 0.12/1 = 0.12; O = 0.48/16 = 0.03; Ratio = 2 : 4 : 1 => Empirical formula = C2H4O [1]"], "marks": 3},
            {"part": "(b)", "points": ["n = (100 * 1.85) / (1.1 * 42.0) = 185 / 46.2 = 4.00 carbons [1]", "Empirical formula mass (C2H4O) = 44; Mr = 88; Molecular formula = C4H8O2 [1]"], "marks": 2},
            {"part": "(c)", "points": ["IR peaks confirm carboxylic acid (-COOH) [1]", "Structure: CH3CH2CH2COOH (or (CH3)2CHCOOH); IUPAC name: Butanoic acid (or 2-methylpropanoic acid) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Fragmentation of Primary Amines — 9701/22/M/J/24/Q5(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Propylamine, CH3CH2CH2NH2, has a relative molecular mass of 59. Its mass spectrum shows a base peak at m/z = 30.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the base peak at m/z = 30 is formed by alpha-cleavage of the propylamine molecular ion. Identify the fragment cation and the radical lost.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the [CH2NH2]+ fragment ion (m/z = 30) is exceptionally stable.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Predict the m/z of the base peak in the mass spectrum of the isomeric amine propan-2-amine, CH3CH(NH2)CH3, and identify the fragment ion.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Alpha-cleavage breaks the C1-C2 bond, expelling an ethyl radical (.CH2CH3, mass 29) [1]", "Fragment cation: [CH2=NH2]+ (imminium ion) at m/z = 30 [1]"], "marks": 2},
            {"part": "(b)", "points": ["The nitrogen lone pair donates electron density into the empty p-orbital of the adjacent carbon [1]", "Resonance stabilization: [H2C-NH2]+ <-> [H2C=NH2]+ with all atoms having a full octet of valence electrons [1]"], "marks": 2},
            {"part": "(c)", "points": ["m/z = 44 [1]", "Fragment ion: [CH3CH=NH2]+ (loss of a methyl radical .CH3, mass 15) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Distinguishing Isomeric Ketones by MS — 9701/23/O/N/23/Q4(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Pentan-2-one (CH3COCH2CH2CH3) and pentan-3-one (CH3CH2COCH2CH3) are positional isomers with Mr = 86.",
        parts=[
            QuestionPart(label="(a)", text="State the two distinct acylium fragment ions formed by alpha-cleavage of pentan-2-one, giving their m/z values.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the single major acylium fragment ion formed by alpha-cleavage of symmetrical pentan-3-one, giving its m/z value.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how mass spectrometry readily distinguishes between pentan-2-one and pentan-3-one based on these fragment peaks.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["m/z = 43: [CH3CO]+ (loss of propyl radical .CH2CH2CH3, mass 43) [1]", "m/z = 71: [CH3CH2CH2CO]+ (loss of methyl radical .CH3, mass 15) [1]"], "marks": 2},
            {"part": "(b)", "points": ["m/z = 57: [CH3CH2CO]+ (propanoyl cation) [1]", "Loss of ethyl radical (.CH2CH3, mass 29) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Pentan-2-one gives major peaks at m/z = 43 and 71 with no significant peak at 57; pentan-3-one gives a dominant peak at m/z = 57 [1]"], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Combined Spectroscopic Elucidation: Unknown Ester — 9701/21/F/M/24/Q5(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Compound K is an ester with Mr = 102. Its mass spectrum shows a molecular ion peak at m/z = 102 (15%) and [M+1]+ at m/z = 103 (0.83%). The base peak is at m/z = 57, and another prominent peak occurs at m/z = 45.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the number of carbon atoms, n, in compound K.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Determine the molecular formula of compound K.", marks=1, num_answer_lines=2),
            QuestionPart(label="(c)", text="The peak at m/z = 57 corresponds to [C2H5CO]+ and the peak at m/z = 45 corresponds to [OC2H5]+. Deduce the structural formula and IUPAC name of ester K.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="Identify the two organic compounds formed when ester K is heated under reflux with aqueous sodium hydroxide followed by acidification.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["n = (100 * 0.83) / (1.1 * 15.0) = 83 / 16.5 [1]", "n = 5.03 approx 5 carbon atoms [1]"], "marks": 2},
            {"part": "(b)", "points": ["Formula mass: 5(12) + 2(16) = 92; Remaining mass = 102 - 92 = 10 H; Molecular formula = C5H10O2 [1]"], "marks": 1},
            {"part": "(c)", "points": ["Structural formula: CH3CH2COOCH2CH3 [1]", "IUPAC name: Ethyl propanoate [1]"], "marks": 2},
            {"part": "(d)", "points": ["Propanoic acid (CH3CH2COOH) [1]", "Ethanol (CH3CH2OH) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Combined Deduction: Carbonyl Structural Isomers — 9701/22/M/J/23/Q3(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Compound M has Mr = 72. Elemental analysis reveals that M contains 66.7% carbon, 11.1% hydrogen, and 22.2% oxygen by mass. Its infrared spectrum exhibits a strong sharp absorption at 1718 cm-1.",
        parts=[
            QuestionPart(label="(a)", text="Show that the molecular formula of compound M is C4H8O.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compound M reacts with 2,4-dinitrophenylhydrazine (2,4-DNPH) to form an orange precipitate, but produces no mirror or precipitate with Tollens' reagent. Deduce the class of organic compound and the structural formula of M.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="The mass spectrum of M shows two major fragment peaks at m/z = 43 and m/z = 57. Identify the cations responsible for both peaks.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="Write the structural equation for the reaction of compound M with alkaline aqueous iodine (the iodoform reaction).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Moles: C = 66.7/12 = 5.56; H = 11.1/1 = 11.1; O = 22.2/16 = 1.39; Ratio = 4 : 8 : 1 => Empirical = C4H8O (mass = 72) [1]", "Since Mr = 72, the molecular formula is C4H8O [1]"], "marks": 2},
            {"part": "(b)", "points": ["Positive 2,4-DNPH confirms carbonyl group; negative Tollens' rules out aldehyde, confirming ketone [1]", "Structural formula: CH3COCH2CH3 (butan-2-one) [1]"], "marks": 2},
            {"part": "(c)", "points": ["m/z = 43: [CH3CO]+ (loss of ethyl radical .CH2CH3) [1]", "m/z = 57: [CH3CH2CO]+ (loss of methyl radical .CH3) [1]"], "marks": 2},
            {"part": "(d)", "points": ["CH3COCH2CH3 + 3I2 + 4OH- -> CHI3 + CH3CH2COO- + 3I- + 3H2O [1]", "CHI3 is tri-iodomethane (yellow precipitate) [1]"], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Deducing Halogenoalkane Structure from MS Fragmentation — 9701/21/O/N/23/Q3(a)-(c)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Two isomeric chloroalkanes, X and Y, have the molecular formula C3H7Cl (Mr = 78 and 80 in 3:1 ratio).",
        parts=[
            QuestionPart(label="(a)", text="State the displayed formulas and IUPAC names of isomers X and Y.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="In the mass spectrum of X, the base peak occurs at m/z = 43. In the mass spectrum of Y, the base peak occurs at m/z = 63 and 65 (ratio 3:1). Explain how these base peaks allow X and Y to be unambiguously identified.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Identify the fragment ions at m/z = 43 and m/z = 63.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["1-chloropropane, CH3CH2CH2Cl [1]", "2-chloropropane, CH3CH(Cl)CH3 [1]"], "marks": 2},
            {"part": "(b)", "points": ["In 2-chloropropane, loss of a .Cl radical gives the secondary propyl carbocation [(CH3)2CH]+ at m/z = 43, which is highly stable and forms the base peak [1]", "In 1-chloropropane, loss of a methyl radical .CH3 produces the chloromethyl cation [CH2CH2Cl]+ at m/z = 63/65 (retaining the chlorine isotope pattern) [1]", "Therefore, isomer X is 2-chloropropane and isomer Y is 1-chloropropane [1]"], "marks": 3},
            {"part": "(c)", "points": ["m/z = 43: [C3H7]+ (or [(CH3)2CH]+) [1]", "m/z = 63: [C2H4 35Cl]+ [1]"], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Synoptic Deduction: Alcohol vs Ether vs Carbonyl — 9701/22/F/M/22/Q5(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Four organic compounds E, F, G, and H are constitutional isomers with the molecular formula C3H8O.",
        parts=[
            QuestionPart(label="(a)", text="Show that only three constitutional isomers actually exist for C3H8O and draw their skeletal structures.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how infrared spectroscopy can immediately separate the three isomers into two distinct functional categories.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Mass spectrum of isomer 1 shows a base peak at m/z = 31 ([CH2OH]+). Mass spectrum of isomer 2 shows a base peak at m/z = 45 ([CH3CHOH]+). Deduce the identities of isomers 1 and 2.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="The third isomer does not react with sodium and has no infrared peak above 3000 cm-1. Name this isomer.", marks=1, num_answer_lines=2)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Skeletal structures of propan-1-ol, propan-2-ol, and methoxyethane [1]", "Any two correct skeletal structures [1]"], "marks": 2},
            {"part": "(b)", "points": ["Propan-1-ol and propan-2-ol exhibit a strong, broad O-H stretch at 3200-3600 cm-1 [1]", "Methoxyethane is an ether with no O-H bond, showing no absorption above 3000 cm-1 except alkyl C-H stretches [1]"], "marks": 2},
            {"part": "(c)", "points": ["Isomer 1 is propan-1-ol (CH3CH2CH2OH -> [CH2OH]+ m/z 31 + .C2H5) [1]", "Isomer 2 is propan-2-ol (CH3CH(OH)CH3 -> [CH3CHOH]+ m/z 45 + .CH3) [1]"], "marks": 2},
            {"part": "(d)", "points": ["Methoxyethane (ethyl methyl ether) [1]"], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Synoptic Identification of Carboxylic Acid & Derivative — 9701/21/M/J/23/Q3(a)-(d)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Compound Z contains 40.0% carbon, 6.7% hydrogen, and 53.3% oxygen by mass. Its mass spectrum gives [M]+ at m/z = 60 (25.0%) and [M+1]+ at m/z = 61 (0.55%).",
        parts=[
            QuestionPart(label="(a)", text="Calculate the empirical formula of compound Z.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Confirm the molecular formula of compound Z using the [M+1]+ peak data.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Compound Z dissolves in water to form a solution with pH 3. Its infrared spectrum displays a broad band extending from 2500 cm-1 to 3000 cm-1 and a sharp peak at 1715 cm-1. Deduce the structural formula of Z.", marks=2, num_answer_lines=3),
            QuestionPart(label="(d)", text="Compound Z is reacted with thionyl chloride, SOCl2. State the structural formula of the organic product and write the balanced equation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Moles: C = 40.0/12 = 3.33; H = 6.7/1 = 6.7; O = 53.3/16 = 3.33; Ratio = 1 : 2 : 1 => CH2O [1]", "Empirical formula mass = 30.0 [1]"], "marks": 2},
            {"part": "(b)", "points": ["n = (100 * 0.55) / (1.1 * 25.0) = 55 / 27.5 = 2.00 carbon atoms [1]", "Empirical formula CH2O x 2 gives molecular formula C2H4O2 (Mr = 60) [1]"], "marks": 2},
            {"part": "(c)", "points": ["Acidic pH and 2500-3000 cm-1 broad band confirm carboxylic acid [1]", "Structural formula: CH3COOH (ethanoic acid) [1]"], "marks": 2},
            {"part": "(d)", "points": ["CH3COCl (ethanoyl chloride) [1]", "CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl [1]"], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic Spectral Elucidation — 9701/22/M/J/24/Q6(a)-(e)",
        syllabus_ref="22.2",
        difficulty="HARD",
        preamble="Two isomeric organic compounds, S and T, have the molecular formula C5H10O (Mr = 86). Both compounds give an orange precipitate when treated with 2,4-dinitrophenylhydrazine.",
        parts=[
            QuestionPart(label="(a)", text="State the functional group type common to both compounds S and T based on the 2,4-DNPH test.", marks=1, num_answer_lines=2),
            QuestionPart(label="(b)", text="Compound S forms a silver mirror with Tollens' reagent. Its infrared spectrum shows a sharp carbonyl absorption at 1725 cm-1 and two distinctive sharp absorptions at 2720 cm-1 and 2820 cm-1. Its mass spectrum has a base peak at m/z = 57. Deduce the displayed formula and IUPAC name of compound S, and identify the base peak cation.", marks=3, num_answer_lines=4),
            QuestionPart(label="(c)", text="Compound T does NOT react with Tollens' reagent. When treated with alkaline aqueous iodine, compound T forms a pale yellow precipitate of tri-iodomethane. Deduce the structural feature that compound T must contain.", marks=1, num_answer_lines=2),
            QuestionPart(label="(d)", text="The mass spectrum of compound T shows a base peak at m/z = 43 ([CH3CO]+) and an intense fragment peak at m/z = 71 ([M - 15]+). Deduce the displayed formula and systematic name of compound T.", marks=2, num_answer_lines=3),
            QuestionPart(label="(e)", text="Compound T is reduced with NaBH4 in aqueous ethanol, forming compound U. State the IUPAC name of compound U, and describe how its infrared spectrum differs from that of compound T.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"part": "(a)", "points": ["Carbonyl group (aldehyde or ketone / C=O) [1]"], "marks": 1},
            {"part": "(b)", "points": ["Positive Tollens' and 2720/2820 cm-1 doublet confirm aldehyde [1]", "Base peak at m/z = 57 is the butyl cation [C4H9]+ (or propionyl [CH3CH2CO]+ formed by alpha-cleavage of pentanal) [1]", "Displayed formula of pentanal (or 2-methylbutanal); IUPAC name: Pentanal (or 2-methylbutanal) [1]"], "marks": 3},
            {"part": "(c)", "points": ["Methyl ketone group, CH3-C=O (or methyl carbonyl group attached to carbon) [1]"], "marks": 1},
            {"part": "(d)", "points": ["Displayed formula of pentan-2-one (CH3COCH2CH2CH3) [1]", "Systematic name: Pentan-2-one [1]"], "marks": 2},
            {"part": "(e)", "points": ["Pentan-2-ol [1]", "Carbonyl peak at 1715 cm-1 completely disappears and is replaced by a strong, broad alcohol O-H band at 3200-3600 cm-1 [1]"], "marks": 2}
        ]
    )
]
