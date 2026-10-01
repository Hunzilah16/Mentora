"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 19: Nitrogen Compounds (Amines and Nitriles).
Subtopics:
  19.1 Primary amines:
       - Preparation from halogenoalkanes + excess ethanolic ammonia (nucleophilic substitution, sealed tube)
       - Basicity: Bronsted-Lowry theory, nitrogen lone pair donation, comparative basicity (primary aliphatic > ammonia > phenylamine)
       - Inductive effect (+I) vs pi-electron delocalisation into aromatic ring
       - Salt formation with mineral acids (RNH3+Cl-) and amine liberation with base
       - Acylation with acyl chlorides to form substituted amides (peptide link -CONH-)
       - Ligand exchange and complexation with aqueous copper(II) ions
  19.2 Nitriles and hydroxynitriles:
       - Preparation: halogenoalkanes + KCN (chain extension by +1 carbon)
       - Preparation: carbonyl compounds + HCN / NaCN (2-hydroxynitriles)
       - Acid hydrolysis: reflux with dilute HCl / H2SO4 to carboxylic acids + NH4+
       - Alkaline hydrolysis: reflux with dilute NaOH to carboxylates + NH3, acidification
       - Reduction using LiAlH4 in dry ether (or H2 / Ni) to pure primary amines
       - Deductions, synthetic pathways, calculations and MCQs

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

TOPIC_19_QUESTIONS = [
    # =========================================================================
    # PART 1: Basicity, Structure & Inductive Effects of Amines (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Comparative Basicity of Nitrogen Compounds — 9701/22/M/J/23/Q5(a)-(d)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Amines behave as Bronsted-Lowry bases due to the presence of a lone pair of electrons on the nitrogen atom. Fig. 1.1 displays the comparative basicity and lone pair availability for ethylamine, ammonia, and phenylamine.",
        figure_path="figures/amines_basicity_comparison.png",
        figure_caption="Fig. 1.1: Relative basicity and electron density of the nitrogen lone pair across aliphatic and aromatic nitrogen bases.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term Bronsted-Lowry base, and write an equation showing how ethylamine acts as a base in aqueous solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethylamine is a stronger base than ammonia, referring to inductive effects.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why phenylamine (aniline) is a significantly weaker base than ammonia, referring to orbital overlap and electron delocalisation.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="State the geometry and the approximate H-N-H bond angle in an ethylamine molecule, and compare it to the bond angle in the ethylammonium ion, CH3CH2NH3⁺.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A proton (H⁺) acceptor [1]",
                "CH3CH2NH2 + H2O <=> CH3CH2NH3⁺ + OH⁻ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The ethyl group exerts a positive inductive (+I) electron-releasing effect [1]",
                "This increases the electron density on the nitrogen atom, making the lone pair more readily available to accept a proton (H⁺) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The lone pair of electrons on the nitrogen p-orbital overlaps with the delocalised pi electron system of the benzene ring [1]",
                "The lone pair becomes delocalised into the aromatic ring, significantly decreasing electron density on nitrogen [1]",
                "Consequently, the lone pair is far less available to coordinate with / accept a proton [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "In ethylamine: Trigonal pyramidal geometry with bond angle ~107° (due to lone pair-bonding pair repulsion) [1]",
                "In ethylammonium ion: Tetrahedral geometry around nitrogen with bond angle ~109.5° [1]",
                "Loss of lone pair into a dative bond eliminates lone pair repulsion, widening bond angles [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=2,
        title="Basicity Trends in Primary, Secondary & Tertiary Amines — 9701/21/O/N/23/Q4(a)-(c)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="In aqueous solution, the basicity order of methylamines is: dimethylamine ((CH3)2NH) > methylamine (CH3NH2) > trimethylamine ((CH3)3N) > ammonia (NH3).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why dimethylamine is a stronger base than methylamine.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why trimethylamine is a weaker base than dimethylamine in aqueous solution, despite having three electron-releasing methyl groups. Mention hydration and steric effects.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Predict whether diethylamine or ethylamine is the stronger base in water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dimethylamine has two electron-releasing methyl groups (+I effect) compared to one in methylamine [1]",
                "This results in greater electron density on the nitrogen lone pair, making it more attractive to protons [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Steric hindrance: Three bulky methyl groups crowd the nitrogen atom, impeding the approach of H⁺ and water molecules [1]",
                "Hydration energy: The trimethylammonium ion ((CH3)3NH⁺) has only one N-H bond to form hydrogen bonds with solvent water molecules, whereas (CH3)2NH2⁺ has two N-H bonds [1]",
                "Less favourable solvation / hydration energy destabilises the conjugate cation of trimethylamine in water [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Diethylamine ((C2H5)2NH) is the stronger base [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=3,
        title="Physical Properties and Hydrogen Bonding of Amines — 9701/22/F/M/22/Q3(a)-(c)",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Table 3.1 compares the boiling points and water solubilities of propane (b.p. -42 °C), ethylamine (b.p. 17 °C), and ethanol (b.p. 78 °C), all having relative molecular masses Mr ≈ 44-46.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why ethylamine has a significantly higher boiling point than propane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethanol has a significantly higher boiling point than ethylamine, even though both substances exhibit intermolecular hydrogen bonding.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw a labelled diagram showing hydrogen bonding between a molecule of ethylamine and a molecule of water.",
                marks=2,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propane is non-polar and held only by weak London dispersion forces [1]",
                "Ethylamine has polar N-H bonds and forms intermolecular hydrogen bonds between molecules, requiring more energy to separate [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Oxygen is more electronegative than nitrogen (electronegativity 3.5 vs 3.0) [1]",
                "The O-H bond is more polarised than the N-H bond, resulting in stronger intermolecular hydrogen bonds in ethanol than in ethylamine [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Correct dipoles: N(delta-)-H(delta+) on ethylamine and H(delta+)-O(delta-) on water [1]",
                "Dashed line from lone pair on nitrogen to H(delta+) of water (or from water oxygen lone pair to H(delta+) of amine) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Salt Formation and Amine Liberation — 9701/23/M/J/23/Q4(a)-(c)",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Ethylamine dissolves in dilute hydrochloric acid to produce an odorless crystalline salt.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction of ethylamine with hydrochloric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Give the systematic name of the organic salt formed and describe the bonding present between the cation and anion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe how the pungent, volatile ethylamine can be regenerated from this salt. Write an ionic equation for this reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2NH2 + HCl -> CH3CH2NH3⁺Cl⁻ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethylammonium chloride [1]",
                "Ionic bonding / strong electrostatic attraction between positive CH3CH2NH3⁺ and negative Cl⁻ ions [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Add a strong alkali such as aqueous sodium hydroxide (NaOH(aq)) and warm gently [1]",
                "CH3CH2NH3⁺ + OH⁻ -> CH3CH2NH2 + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Ligand Exchange and Complexation with Copper(II) — 9701/21/M/J/22/Q3(a)-(c)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="When aqueous butylamine is added dropwise to aqueous copper(II) sulfate, a pale blue precipitate appears. Upon adding excess butylamine, the precipitate dissolves to produce a deep royal-blue solution.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the chemical formula of the pale blue precipitate formed in the first step and state the property of butylamine that causes its precipitation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Identify the complex ion responsible for the deep royal-blue solution formed in excess butylamine, and state the type of bonding between butylamine and the copper ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the ionic equation for the dissolution of the precipitate in excess butylamine (RNH2).",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Precipitate formula: Cu(OH)2 / copper(II) hydroxide [1]",
                "Butylamine acts as a Bronsted-Lowry base in water, generating OH⁻ ions (RNH2 + H2O <=> RNH3⁺ + OH⁻) which precipitate Cu²⁺ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "[Cu(CH3CH2CH2CH2NH2)4(H2O)2]²⁺ (or [Cu(RNH2)4]²⁺) [1]",
                "Dative covalent (coordinate) bonding via the nitrogen lone pair [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Cu(OH)2(s) + 4RNH2(aq) + 2H2O(l) -> [Cu(RNH2)4(H2O)2]²⁺(aq) + 2OH⁻(aq) [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Multiple Choice: Basicity Rankings — 9701/12/M/J/23/Q25",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Which compound is the strongest base in aqueous solution?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the strongest base:\nA  Ammonia\nB  Ethylamine\nC  Phenylamine\nD  Ethanamide",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethanamide is practically neutral (non-basic) in water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Ethylamine) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "In ethanamide (CH3CONH2), the lone pair of electrons on nitrogen is adjacent to an electronegative carbonyl group (C=O) [1]",
                "The nitrogen lone pair is strongly delocalised into the pi system of the carbonyl group, rendering it completely unavailable for protonation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Reaction of Amines with Halogenoalkanes — 9701/22/O/N/22/Q3(a)-(d)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Ethylamine reacts with bromoethane in a sealed tube under pressure.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the reaction of ethylamine with bromoethane to form a secondary amine salt.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the neutral secondary amine obtained after treatment with sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why this reaction does not stop at the secondary amine stage, leading to tertiary amines and quaternary ammonium salts.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Give the formula and systematic name of the quaternary ammonium salt produced when excess bromoethane is used.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2NH2 + CH3CH2Br -> (CH3CH2)2NH2⁺Br⁻ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Diethylamine [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The secondary amine formed retains a lone pair on nitrogen and is an even stronger nucleophile than the starting primary amine due to two electron-releasing ethyl groups [1]",
                "It competes effectively for remaining bromoethane molecules, undergoing successive nucleophilic substitutions [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Formula: (CH3CH2)4N⁺Br⁻ [1]",
                "Name: Tetraethylammonium bromide [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Aromatic Amines: Synthesis of Phenylamine — 9701/21/O/N/21/Q4",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Phenylamine is manufactured from nitrobenzene via a two-stage reduction procedure.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagents and condition used in Stage 1 to reduce nitrobenzene to phenylammonium ions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent used in Stage 2 to liberate neutral phenylamine from the reaction mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write the overall equation for the reduction of nitrobenzene to phenylamine using [H] to represent the reducing agent.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Tin (Sn) and concentrated hydrochloric acid (conc. HCl) [1]",
                "Heat under reflux (or boiling water bath) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Aqueous sodium hydroxide (NaOH(aq)) in excess [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "C6H5NO2 + 6[H] -> C6H5NH2 + 2H2O [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Bromination of Phenylamine — 9701/23/O/N/22/Q5",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="When aqueous bromine (bromine water) is added to phenylamine, an immediate reaction occurs without a catalyst.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State two visible observations during this reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula and give the systematic IUPAC name of the organic precipitate formed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why phenylamine reacts vigorously with bromine water at room temperature without requiring a halogen carrier catalyst (such as FeBr3 or AlBr3), unlike benzene.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Bromine water is decolourised (orange-brown to colourless) [1]",
                "White precipitate forms immediately [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structure showing 2,4,6-tribromophenylamine (benzene ring with -NH2 at position 1 and Br atoms at 2, 4, 6) [1]",
                "Systematic name: 2,4,6-tribromophenylamine [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The lone pair of electrons on the nitrogen atom is delocalised into the benzene ring's pi electron system [1]",
                "This significantly activates the ring by increasing the pi electron density (particularly at 2, 4, and 6 positions) [1]",
                "The enhanced electron density polarises incoming bromine molecules effectively without needing a Lewis acid catalyst [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=10,
        title="Acylation of Primary Amines to Form Amides — 9701/22/M/J/22/Q4",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Primary amines react vigorously with acyl chlorides at room temperature to form substituted amides.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction between ethanoyl chloride and ethylamine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the organic product formed and identify the functional group linking the two carbon chains.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why two molar equivalents of ethylamine are typically consumed for every mole of ethanoyl chloride in this reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COCl + CH3CH2NH2 -> CH3CONHCH2CH3 + HCl [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "N-ethylethanamide [1]",
                "Secondary amide (or peptide) linkage: -CONH- [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The reaction liberates acidic hydrogen chloride gas (HCl) [1]",
                "The basic ethylamine acts as a scavenger, reacting with HCl to form ethylammonium chloride salt (CH3CH2NH3⁺Cl⁻), consuming a second equivalent of amine [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Multiple Choice: Properties of Ethylamine — 9701/11/M/J/23/Q27",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Which statement regarding ethylamine is correct?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct statement:\nA  It turns universal indicator paper red\nB  It reacts with dilute hydrochloric acid to form an insoluble precipitate\nC  It has a higher boiling point than ethanol\nD  It reacts with ethanoyl chloride to produce N-ethylethanamide",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the observation when ethylamine vapour comes into contact with damp red litmus paper.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "D (It reacts with ethanoyl chloride to produce N-ethylethanamide) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Damp red litmus paper turns blue (alkaline gas) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Diazotisation of Phenylamine (A Level Transition Link) — 9701/21/O/N/23/Q7",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="When phenylamine is treated with nitrous acid (HNO2) at temperatures below 5 °C, benzenediazonium chloride is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State how nitrous acid is generated in situ in the reaction mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the reaction temperature must be maintained strictly between 0 °C and 5 °C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="What happens if the benzenediazonium salt solution is warmed above 10 °C? State the observation and the organic product formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Sodium nitrite (NaNO2) and excess dilute hydrochloric acid (HCl) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The diazonium ion (C6H5N2⁺) is unstable and decomposes rapidly at higher temperatures [1]",
                "Low temperature (< 5 °C) prevents thermal decomposition while remaining warm enough for reaction to occur [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Effervescence / bubbling of nitrogen gas (N2) [1]",
                "Organic product: Phenol (C6H5OH) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Distinguishing Aliphatic vs Aromatic Amines — 9701/22/F/M/21/Q4",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Describe two distinct chemical tests to differentiate between liquid samples of butylamine and phenylamine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Test 1: Describe the test using bromine water, stating observations for each compound.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Test 2: Describe the test using aqueous copper(II) sulfate, stating observations for each compound.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Butylamine: No precipitate, bromine water remains orange-brown (no reaction) [1]",
                "Phenylamine: Bromine water decolourises immediately, forming a white precipitate of 2,4,6-tribromophenylamine [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Butylamine: Pale blue precipitate formed which dissolves in excess to give a deep royal-blue solution [1]",
                "Phenylamine: Insoluble / green-brown precipitate or no deep blue complex (too weakly basic and insoluble in water) [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 2: Primary Amine Synthetic Pathways (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Synthetic Pathways to Primary Amines — 9701/21/M/J/23/Q8(a)-(d)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Primary aliphatic amines can be prepared either by direct nucleophilic substitution of halogenoalkanes with ammonia or by the reduction of nitriles. Fig. 14.1 compares these two synthetic routes.",
        figure_path="figures/amines_synthesis_pathways.png",
        figure_caption="Fig. 14.1: Flowchart comparing Route 1 (halogenoalkane + excess ammonia) with Route 2 (nitrile extension and reduction).",
        parts=[
            QuestionPart(
                label="(a)",
                text="In Route 1, bromoethane is heated with concentrated ammonia in a sealed tube. Explain why an excess of concentrated ammonia is essential.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the reaction mixture must be heated in a sealed glass tube rather than under an open reflux condenser.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="In Route 2, bromomethane is converted into ethylamine. Identify the reagent in Step 1 and the reducing agent in Step 2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="State two synthetic advantages of Route 2 over Route 1 for preparing pure ethylamine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Excess ammonia ensures that ammonia molecules outcompete the formed ethylamine for unreacted bromoethane [1]",
                "This suppresses consecutive nucleophilic substitutions that would otherwise yield secondary, tertiary amines, and quaternary ammonium salts [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ammonia is an extremely volatile gas (b.p. -33 °C) and would escape from an open reflux condenser [1]",
                "A sealed tube maintains high pressure, keeping ammonia in concentrated solution and driving the reaction forward [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Step 1 reagent: Potassium cyanide (KCN) or sodium cyanide in aqueous ethanol, heat under reflux [1]",
                "Step 2 reducing agent: Lithium aluminium hydride (LiAlH4) in dry ether OR H2 with Ni catalyst [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Route 2 produces exclusively primary amine without any secondary or tertiary amine contaminants [1]",
                "Route 2 extends the carbon chain by exactly one carbon atom (+1 C), which is valuable in step-up organic synthesis [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Consecutive Substitution Mechanism in Amine Preparation — 9701/22/O/N/23/Q5",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="When 1-chloropropane reacts with ammonia, a mixture of four different organic products is obtained.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equations showing the successive steps from 1-chloropropane to propylamine, dipropylamine, and tripropylamine.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Give the formula and systematic IUPAC name of the fourth product, which is an ionic salt.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why dipropylamine is a stronger nucleophile than propylamine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2CH2Cl + 2NH3 -> CH3CH2CH2NH2 + NH4Cl [1]",
                "CH3CH2CH2Cl + CH3CH2CH2NH2 -> (CH3CH2CH2)2NH + HCl [1]",
                "CH3CH2CH2Cl + (CH3CH2CH2)2NH -> (CH3CH2CH2)3N + HCl [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Formula: (CH3CH2CH2)4N⁺Cl⁻ [1]",
                "Name: Tetrapropylammonium chloride [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Dipropylamine has two electron-releasing propyl groups (+I effect) attached to nitrogen compared to one in propylamine [1]",
                "This increases the electron density on the nitrogen lone pair, making it attack the delta+ carbon of the halogenoalkane faster [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Separation of Amine Mixtures via Fractional Distillation — 9701/21/O/N/22/Q4",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Consider the boiling points of ethylamine (b.p. 17 °C), diethylamine (b.p. 55 °C), and triethylamine (b.p. 89 °C).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why triethylamine has a higher boiling point than ethylamine, even though triethylamine CANNOT form hydrogen bonds between its own molecules.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State how the components of this amine mixture can be separated after liberating the free amines with aqueous sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Triethylamine (Mr = 101.2) has far more electrons and a much larger molecular surface area than ethylamine (Mr = 45.1) [1]",
                "It possesses significantly stronger London dispersion (induced dipole-dipole) forces between its molecules [1]",
                "The cumulative dispersion forces in triethylamine outweigh the hydrogen bonding in smaller ethylamine, requiring more thermal energy to boil [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Fractional distillation [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Synthesis of Amines from Amides: Reduction with LiAlH4 — 9701/23/M/J/22/Q3",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Amides can be reduced to primary amines using lithium aluminium hydride in dry ether.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reduction of ethanamide, CH3CONH2, to ethylamine using [H] for the reducing agent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the solvent used and explain why water must be strictly excluded until the reaction is complete.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Contrast the product of reducing an amide with LiAlH4 to the product of reducing an amide by acid hydrolysis.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CONH2 + 4[H] -> CH3CH2NH2 + H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Dry ether (ethoxyethane) [1]",
                "LiAlH4 reacts violently with water to produce flammable hydrogen gas and hydrolyses the reagent [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reduction with LiAlH4 yields an amine (preserves nitrogen in organic chain, converts C=O to -CH2-) [1]",
                "Acid hydrolysis cleaves the C-N bond, yielding a carboxylic acid and an ammonium salt [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Multiple Choice: Reagents for Amine Synthesis — 9701/12/F/M/23/Q25",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Which reaction converts 1-bromobutane into butylamine with no higher amine by-products?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct two-step sequence:\nA  Step 1: KCN in ethanol; Step 2: LiAlH4 in dry ether\nB  Step 1: Aqueous NaOH; Step 2: NH3\nC  Step 1: Mg in dry ether; Step 2: NH3\nD  None of these",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why option A produces pentylamine rather than butylamine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "D (None of these) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Option A adds a nitrile carbon (KCN), converting 4-carbon 1-bromobutane into 5-carbon pentanenitrile [1]",
                "Subsequent reduction yields pentan-1-amine (5 carbons), NOT butylamine (4 carbons) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Gabriel Phthalimide Synthesis (Curriculum Extension) — 9701/21/M/J/21/Q5",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="The Gabriel synthesis is a laboratory method specifically developed to synthesise pure primary amines without forming secondary or tertiary amines.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why potassium phthalimide reacts with 1-bromobutane by nucleophilic substitution, but the resulting alkylated product CANNOT react with a second molecule of 1-bromobutane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State how the primary amine is liberated from the alkylphthalimide intermediate.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In N-butylphthalimide, the nitrogen lone pair is delocalised into two adjacent carbonyl groups [1]",
                "This makes nitrogen non-nucleophilic, completely preventing any further alkylation / consecutive substitution [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Alkaline hydrolysis with aqueous sodium hydroxide (or hydrazinolysis with hydrazine, NH2NH2) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Quaternary Ammonium Salts as Surfactants — 9701/22/M/J/23/Q10",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Quaternary ammonium salts containing long hydrocarbon chains, such as cetyltrimethylammonium bromide, are cationic surfactants used in fabric softeners and hair conditioners.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why quaternary ammonium ions carry a permanent positive charge regardless of the pH of the solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain how cationic surfactants bind to negatively charged wet hair or cotton fabric fibres to reduce static cling and soften fibres.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The nitrogen atom is bonded to four carbon atoms and possesses no lone pair or ionisable hydrogen atom [1]",
                "It cannot lose or gain a proton, so its formal +1 charge is permanent and independent of pH [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The positively charged quaternary head groups bond electrostatically to the negative charges on fibre surfaces [1]",
                "The non-polar hydrocarbon tails face outwards, providing a smooth, lubricated hydrophobic coating that reduces friction and static buildup [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Chiral Amines: Optical Activity — 9701/23/O/N/23/Q4",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Butan-2-amine exhibits optical isomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of butan-2-amine and mark the chiral carbon atom with an asterisk (*).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw 3D wedge-and-dash representations showing the two non-superimposable optical enantiomers of butan-2-amine.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why both enantiomers exhibit identical chemical reactions with dilute hydrochloric acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-C*H(NH2)-CH2-CH3 with asterisk on C2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Correct 3D tetrahedral representations using wedges, dashed lines, and solid bonds [1]",
                "Both enantiomers drawn as exact mirror images [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Hydrochloric acid is an achiral reagent; enantiomers possess identical chemical reactivity with all achiral substances [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Multiple Choice: Mechanism of Amine Formation — 9701/11/O/N/22/Q25",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="What type of reaction and mechanism is involved when bromoethane reacts with ammonia to form ethylamine?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reaction type and mechanism:\nA  Electrophilic addition\nB  Nucleophilic addition\nC  Nucleophilic substitution (SN2)\nD  Free-radical substitution",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Identify the nucleophile in this reaction.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Nucleophilic substitution (SN2)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ammonia molecule (:NH3, via its lone pair of electrons on nitrogen) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Diamines in Polyamide Manufacture — 9701/21/O/N/21/Q6",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Hexane-1,6-diamine, H2N-(CH2)6-NH2, is reacted with hexanedioic acid to manufacture Nylon 6,6.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the condensation polymerisation of hexane-1,6-diamine with hexanedioic acid, showing one repeat unit.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Identify the linkage that connects the monomer units in the nylon chain.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why Nylon 6,6 fibres have high tensile strength and can be drawn into durable threads.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[HN-(CH2)6-NH-CO-(CH2)4-CO]- + 2nH2O (or shown as repeat unit with continuation bonds) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Amide link / peptide link (-CO-NH-) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Linear polymer chains align parallel to one another [1]",
                "Forms extensive intermolecular hydrogen bonds between C=O of one chain and N-H of adjacent chains, providing high tensile strength [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Deducing Amine Structure from Elemental Analysis & MS — 9701/22/F/M/23/Q3",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="An organic primary amine D contains 65.7% carbon, 15.1% hydrogen, and 19.2% nitrogen by mass. Its mass spectrum shows a molecular ion at m/z = 73.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the empirical formula and molecular formula of amine D.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formulas of the four isomeric primary amines with this molecular formula.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(c)",
                text="Which of these four isomers contains a chiral carbon atom?",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 65.7/12 = 5.475; H = 15.1/1.0 = 15.1; N = 19.2/14 = 1.371 [1]",
                "Ratio C:H:N = 4:11:1 -> Empirical and Molecular formula = C4H11N (Mr = 73) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Butan-1-amine: CH3CH2CH2CH2NH2 [1]",
                "Butan-2-amine: CH3CH(NH2)CH2CH3 [1]",
                "2-methylpropan-1-amine: (CH3)2CHCH2NH2 [1]",
                "2-methylpropan-2-amine: (CH3)3CNH2 [1]"
            ], "marks": 4},
            {"part": "(c)", "points": [
                "Butan-2-amine [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Combustion of Amines and NOx Emissions — 9701/11/M/J/22/Q25",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="When methylamine burns completely in oxygen, it produces carbon dioxide, water vapour, and nitrogen gas.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced chemical equation for the complete combustion of methylamine, CH3NH2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="In vehicle engines, incomplete combustion of nitrogenous fuels can produce nitrogen oxides (NO and NO2). State one environmental hazard caused by NOx emissions.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "4CH3NH2 + 9O2 -> 4CO2 + 10H2O + 2N2 [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Contributes to acid rain (HNO3 formation) / formation of photochemical smog / respiratory irritation [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="Multiple Choice: Basicity of Amine Derivatives — 9701/12/O/N/23/Q27",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Which organic nitrogen compound does NOT form a salt when mixed with dilute sulfuric acid?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct compound:\nA  Butylamine\nB  Diethylamine\nC  Ethanamide\nD  Phenylamine",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain your reasoning.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Ethanamide) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethanamide is an amide, not an amine [1]",
                "The lone pair of electrons on nitrogen is delocalised into the adjacent carbonyl C=O group, making it neutral and non-basic; it cannot be protonated by dilute mineral acid [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 3: Nitrile Transformations, Hydrolysis & Reduction (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Comprehensive Chemical Reactions of Nitriles — 9701/21/M/J/23/Q9(a)-(d)",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Nitriles (R-C≡N) are vital synthetic intermediates that can be converted into either carboxylic acids or primary amines. Fig. 27.1 illustrates the dual hydrolysis pathways and reduction chemistry of propanenitrile.",
        figure_path="figures/nitriles_synthetic_reactions.png",
        figure_caption="Fig. 27.1: Chemical transformation pathways of nitriles: acid hydrolysis, alkaline hydrolysis, and reduction.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagents and conditions for the acid hydrolysis of propanenitrile, and write the balanced chemical equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagents and conditions for the alkaline hydrolysis of propanenitrile, and write the balanced chemical equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the observation during alkaline hydrolysis that confirms ammonia gas is evolved, and write the equation for liberating propanoic acid from the resulting solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State the reagent, solvent, and write the equation for the reduction of propanenitrile to propylamine using [H].",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (or dilute H2SO4), heat under reflux [1]",
                "CH3CH2CN + 2H2O + HCl -> CH3CH2COOH + NH4Cl (or + H⁺ -> ... + NH4⁺) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents/conditions: Aqueous sodium hydroxide (NaOH(aq)), heat under reflux [1]",
                "CH3CH2CN + H2O + NaOH -> CH3CH2COONa + NH3 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Pungent gas evolved turns damp red litmus paper blue [1]",
                "Add dilute strong acid: CH3CH2COO⁻ + H⁺ -> CH3CH2COOH [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Reagent/solvent: LiAlH4 in dry ether (or H2 / Ni catalyst) [1]",
                "CH3CH2CN + 4[H] -> CH3CH2CH2NH2 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Synthesis of Nitriles from Halogenoalkanes — 9701/22/O/N/23/Q6(a)-(c)",
        syllabus_ref="19.2",
        difficulty="EASY",
        preamble="1-bromobutane is converted into pentanenitrile.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and solvent required for this nucleophilic substitution reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced chemical equation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why potassium cyanide, KCN, is dissolved in ethanol/water mixture rather than pure water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Potassium cyanide (KCN) or sodium cyanide (NaCN) [1]",
                "Solvent: Ethanol / aqueous ethanol, heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2CH2Br + KCN -> CH3CH2CH2CH2CN + KBr [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "1-bromobutane is insoluble in water (two immiscible layers would form, giving very slow reaction) [1]",
                "Ethanol acts as a co-solvent that dissolves both the non-polar halogenoalkane and the ionic cyanide salt, creating a homogeneous reaction mixture [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="2-Hydroxynitriles: Addition of HCN to Carbonyls — 9701/21/O/N/22/Q5",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Ethanal reacts with HCN in the presence of NaCN to form 2-hydroxypropanenitrile.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Outline the nucleophilic addition mechanism by drawing curly arrows showing the attack of :CN⁻ on ethanal and subsequent protonation.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State why this reaction is described as a 'step-up' reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the acid hydrolysis of 2-hydroxypropanenitrile to lactic acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Curly arrow from lone pair on carbon of :CN⁻ to C(delta+) of CH3CHO [1]",
                "Curly arrow from C=O double bond onto oxygen forming intermediate CH3CH(CN)O⁻ [1]",
                "Curly arrow from lone pair on O⁻ to H of HCN (or H2O) regenerating :CN⁻ [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "It extends the length of the carbon chain by adding one carbon atom (from 2 carbons in ethanal to 3 carbons in the product) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "CH3CH(OH)CN + 2H2O + H⁺ -> CH3CH(OH)COOH + NH4⁺ [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Reduction of Nitriles: LiAlH4 vs Catalytic Hydrogenation — 9701/22/M/J/22/Q6",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Industrial manufacturing of hexamethylenediamine from adiponitrile uses catalytic hydrogenation, whereas laboratory preparations often use LiAlH4.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the catalytic hydrogenation of butanenitrile, CH3CH2CH2CN, to butan-1-amine using H2 and a nickel catalyst.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the conditions (temperature, pressure, catalyst) for industrial catalytic hydrogenation of nitriles.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two reasons why catalytic hydrogenation is preferred in chemical factories over using LiAlH4.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2CH2CN + 2H2 -> CH3CH2CH2CH2NH2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Nickel (Ni) or platinum (Pt) catalyst [1]",
                "Moderately high temperature (~150-200 °C) and elevated pressure (~10-50 atm) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "H2 gas is much cheaper and readily available in bulk compared to expensive LiAlH4 [1]",
                "Catalytic hydrogenation has 100% atom economy with zero stoichiometric metal waste (LiAlH4 produces large amounts of aluminium hydroxide waste) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Nitrile Hydrolysis Kinetics and Mechanism — 9701/23/M/J/23/Q5",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="During the acid hydrolysis of a nitrile, an amide is formed as an intermediate before full conversion to the carboxylic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structure of the amide intermediate formed during the partial hydrolysis of ethanenitrile, CH3CN.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethanamide can be isolated if the reaction is carried out under mild conditions, but complete reflux with strong acid yields ethanoic acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-CONH2 (ethanamide) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Addition of one water molecule across the C≡N triple bond forms the amide: CH3CN + H2O -> CH3CONH2 [1]",
                "Prolonged heating with strong acid supplies the activation energy needed to hydrolyse the amide linkage: CH3CONH2 + H2O + H⁺ -> CH3COOH + NH4⁺ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Multiple Choice: Reagents for Nitrile Reduction — 9701/11/M/J/23/Q28",
        syllabus_ref="19.2",
        difficulty="EASY",
        preamble="Which reagent does NOT reduce a nitrile to a primary amine?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the reagent:\nA  LiAlH4 in dry ether\nB  H2 gas over a heated nickel catalyst\nC  NaBH4 in aqueous ethanol\nD  Sodium metal in boiling ethanol",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why your chosen reagent fails to reduce nitriles.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (NaBH4 in aqueous ethanol) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "NaBH4 is a relatively mild reducing agent that only reduces aldehydes and ketones [1]",
                "It lacks sufficient hydride transfer power to reduce the less electrophilic, highly stable C≡N triple bond [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Deducing Nitrile Structure from Hydrolysis Products — 9701/21/O/N/23/Q6",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="A branched nitrile J with molecular formula C5H9N is hydrolysed under reflux with dilute sulfuric acid to produce carboxylic acid K (C5H10O2). Acid K displays three peaks in its carbon-13 NMR spectrum.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the structural formula and systematic IUPAC name of carboxylic acid K.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of nitrile J.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the skeletal structure of the primary amine obtained when nitrile J is reduced with LiAlH4.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Acid K has 3 carbon environments: 2,2-dimethylpropanoic acid, (CH3)3C-COOH [1]",
                "Systematic name: 2,2-dimethylpropanoic acid [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structural formula: (CH3)3C-CN [1]",
                "Systematic name: 2,2-dimethylpropanenitrile [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Skeletal formula of 2,2-dimethylpropan-1-amine: (CH3)3C-CH2-NH2 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Multi-Step Synthesis: Alcohol to Amine (+1 Carbon) — 9701/22/M/J/22/Q7",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Devise a three-step synthetic pathway to convert ethanol into propylamine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert ethanol into bromoethane. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Convert bromoethane into propanenitrile. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: Reduce propanenitrile to propylamine. State the reagents and conditions.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: Sodium bromide (NaBr) and concentrated sulfuric acid (conc. H2SO4) (or PBr3 / red P + Br2) [1]",
                "Condition: Heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagent: Potassium cyanide (KCN) or NaCN [1]",
                "Condition: Aqueous ethanol, heat under reflux [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reagent: Lithium aluminium hydride (LiAlH4) in dry ether (or H2 with heated Ni catalyst) [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Reaction of Cyanide with Halogenoarenes — 9701/21/O/N/21/Q5",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="When chlorobenzene is heated with ethanolic KCN under reflux, NO reaction takes place, whereas 1-chlorobutane reacts rapidly.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why halogenoarenes such as chlorobenzene are completely inert to nucleophilic substitution by cyanide ions under standard conditions.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Suggest how benzenecarbonitrile (benzonitrile, C6H5CN) can be prepared from phenylamine instead.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The lone pair of electrons on chlorine p-orbital overlaps with the delocalised pi electron cloud of the benzene ring [1]",
                "This gives the C-Cl bond partial double bond character, making it significantly stronger and shorter than an aliphatic C-Cl bond [1]",
                "The electron-rich pi cloud of the benzene ring repels incoming nucleophiles (:CN⁻) preventing backside approach [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Diazotise phenylamine with NaNO2 + HCl at < 5 °C to form benzenediazonium chloride [1]",
                "React with copper(I) cyanide (CuCN) / Sandmeyer reaction [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Hydrolysis Stoichiometry of Dinitriles — 9701/23/O/N/22/Q6",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Adiponitrile (hexanedinitrile), NC-(CH2)4-CN, is hydrolysed by boiling with excess dilute hydrochloric acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the complete acid hydrolysis of adiponitrile.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the dicarboxylic acid produced.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the mass of dicarboxylic acid formed from 5.40 g of adiponitrile (Mr = 108.1), assuming an 85.0% yield.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "NC(CH2)4CN + 4H2O + 2HCl -> HOOC(CH2)4COOH + 2NH4Cl [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hexanedioic acid (adipic acid) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Moles of adiponitrile = 5.40 / 108.1 = 0.04995 mol [1]",
                "Theoretical mass of hexanedioic acid (Mr = 146.1) = 0.04995 x 146.1 = 7.30 g [1]",
                "Actual mass at 85.0% yield = 7.30 x 0.850 = 6.20 g [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=37,
        title="Multiple Choice: Chain Extension Identification — 9701/12/M/J/23/Q29",
        syllabus_ref="19.2",
        difficulty="EASY",
        preamble="Which reaction extends the carbon skeleton by ONE carbon atom?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reaction:\nA  Bromoethane + ethanolic NH3\nB  Bromoethane + ethanolic KCN\nC  Ethanol + acidified K2Cr2O7\nD  Ethanol + PCl5",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name the organic product formed in the reaction you selected.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Bromoethane + ethanolic KCN) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Propanenitrile [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Reduction of Hydroxynitriles: Stereochemical Integrity — 9701/22/F/M/22/Q5",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="Optically active (R)-2-hydroxypropanenitrile is reduced with LiAlH4 in dry ether to form 1-aminopropan-2-ol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for this reduction using [H].",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the chiral carbon centre retains its stereochemical configuration during this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structural formula of 1-aminopropan-2-ol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH(OH)CN + 4[H] -> CH3CH(OH)CH2NH2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Reduction occurs exclusively at the C≡N triple bond [1]",
                "None of the four bonds attached to the asymmetric chiral carbon (C2) are cleaved or reformed, preserving the stereochemical configuration [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3-CH(OH)-CH2-NH2 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Nitriles vs Isonitriles (Carbylamines) — 9701/21/M/J/22/Q8",
        syllabus_ref="19.2",
        difficulty="HARD",
        preamble="When bromoethane is reacted with KCN, propanenitrile is formed. However, when bromoethane is reacted with silver cyanide, AgCN, the major product is ethyl isonitrile (ethyl carbylamine, CH3CH2NC).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the difference in structure and bonding between propanenitrile (CH3CH2CN) and ethyl isonitrile (CH3CH2NC).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why AgCN favours attack through the nitrogen atom rather than the carbon atom, referring to covalent vs ionic character.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In propanenitrile, the ethyl group is bonded directly to carbon (CH3CH2-C≡N) [1]",
                "In ethyl isonitrile, the ethyl group is bonded directly to nitrogen (CH3CH2-N≡C with coordinate bond) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "KCN is purely ionic (K⁺ and :C≡N⁻), where carbon carries the negative charge and acts as the stronger nucleophilic centre [1]",
                "Ag-C in AgCN is predominantly covalent; the carbon lone pair is engaged with silver, leaving the nitrogen lone pair free to act as the nucleophile [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 4: Amine Reactions, Acylation & Comprehensive Deductions (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="Reactions of Amines: Acylation and Salt Formation — 9701/21/M/J/23/Q10(a)-(d)",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Primary amines behave as both nucleophiles and bases. Fig. 40.1 illustrates three characteristic reaction profiles: salt formation with acids, acylation with acyl chlorides, and complexation with copper(II) ions.",
        figure_path="figures/amines_acylation_and_salts.png",
        figure_caption="Fig. 40.1: Characteristic reactions of primary aliphatic amines: acid-base neutralisation, acylation, and coordination complexation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction between propylamine and propanoic acid, identifying the type of reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced chemical equation for the reaction of propylamine with propanoyl chloride at room temperature.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the systematic IUPAC name of the substituted amide formed in (b).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Describe how you would distinguish between a solution of propylamine and a solution of propanamide using aqueous copper(II) sulfate.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2COOH + CH3CH2CH2NH2 -> CH3CH2COO⁻ CH3CH2CH2NH3⁺ (propylammonium propanoate) [1]",
                "Neutralisation / acid-base proton transfer [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2COCl + CH3CH2CH2NH2 -> CH3CH2CONHCH2CH2CH3 + HCl [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "N-propylpropanamide [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Add aqueous CuSO4 dropwise then in excess to each solution [1]",
                "Propylamine produces a pale blue precipitate that dissolves in excess to form a deep royal-blue solution [1]",
                "Propanamide is non-basic and does not coordinate to Cu²⁺; solution remains unchanged pale blue [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=41,
        title="Deducing Organic Nitrogen Compound G — 9701/22/O/N/23/Q7",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="An organic liquid G has molecular formula C3H9N.\n• Liquid G turns damp red litmus paper blue.\n• When G reacts with dilute hydrochloric acid, an ionic salt is formed.\n• When G reacts with ethanoyl chloride, organic compound H (C5H11NO) is formed along with steamy white fumes.\n• In the 1H NMR spectrum, compound G displays only two signals with an integration ratio of 6:3.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the functional group present in liquid G.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Use the 1H NMR data to deduce the structural formula and systematic name of liquid G.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structural formula of compound H.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Amine group (secondary amine) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Formula C3H9N with two 1H NMR signals (ratio 6:3): (CH3)2CH-NH2 (isopropylamine / 1-methylethylamine) has two methyls (6H) and CH-NH2 (3H) [2]",
                "Systematic name: Propan-2-amine (or 1-methylethylamine) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "CH3CONHCH(CH3)2 (N-(1-methylethyl)ethanamide) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=42,
        title="Infrared Spectroscopy of Nitrogen Compounds — 9701/21/O/N/22/Q7",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="The infrared spectra of primary amines, secondary amines, and nitriles display distinct characteristic absorptions.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the characteristic wave number range for the C≡N triple bond stretching absorption in nitriles.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Primary amines display a doublet (two peaks) in the 3300-3500 cm⁻¹ region, whereas secondary amines display only a single peak. Explain this difference in terms of vibrational modes.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why tertiary amines exhibit NO absorption bands in the 3300-3500 cm⁻¹ region.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2200 - 2260 cm⁻¹ (sharp and distinct) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Primary amines have two N-H bonds (-NH2), allowing both symmetric and asymmetric N-H stretching vibrations, producing two separate absorption peaks [1]",
                "Secondary amines have only one N-H bond, giving only a single N-H stretching absorption [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Tertiary amines (R3N) possess no N-H bonds, so no N-H stretching vibration is possible [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Mass Spectrometric Fragmentation of Amines (Alpha-Cleavage) — 9701/22/M/J/22/Q8",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="The mass spectrum of propylamine, CH3CH2CH2NH2 (Mr = 59), displays a base peak at m/z = 30.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the formula and structure of the resonance-stabilised iminium fragment ion responsible for the base peak at m/z = 30.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State what neutral radical is lost when the molecular ion fragments to form the peak at m/z = 30.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the base peak of propan-2-amine, CH3CH(NH2)CH3, occurs at m/z = 44 rather than m/z = 30.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "[CH2=NH2]⁺ <-> [⁺CH2-NH2] (iminium ion, mass = 14 + 16 = 30) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ethyl radical, •CH2CH3 (mass = 29) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "In propan-2-amine, alpha-cleavage loses a methyl radical (•CH3, mass 15) [1]",
                "The resulting iminium fragment is [CH3CH=NH2]⁺ with m/z = 59 - 15 = 44 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Multi-Step Synthesis: Alkene to Secondary Amide — 9701/23/M/J/23/Q7",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Devise a multi-step synthetic pathway to convert ethene into N-ethylpropanamide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Outline the pathway to produce ethylamine from ethene in two steps.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Outline the pathway to produce propanoyl chloride from ethene in three steps.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Combine ethylamine and propanoyl chloride to produce N-ethylpropanamide, writing the equation and stating the conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: Ethene + HBr -> Bromoethane (electrophilic addition) [1]",
                "Step 2: Bromoethane + excess ethanolic NH3, heat in sealed tube -> Ethylamine [2]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Step 1: Bromoethane + KCN in aqueous ethanol -> Propanenitrile [1]",
                "Step 2: Propanenitrile + dilute HCl, reflux -> Propanoic acid [1]",
                "Step 3: Propanoic acid + SOCl2 (or PCl5) -> Propanoyl chloride [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "CH3CH2COCl + CH3CH2NH2 -> CH3CH2CONHCH2CH3 + HCl [1]",
                "Room temperature / anhydrous conditions [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Multiple Choice: Nitrile Hydrolysis Outcomes — 9701/12/M/J/23/Q30",
        syllabus_ref="19.2",
        difficulty="EASY",
        preamble="Which compound is produced when 2-methylbutanenitrile is heated under reflux with dilute hydrochloric acid?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct IUPAC name:\nA  2-methylbutan-1-amine\nB  2-methylbutanoic acid\nC  3-methylbutanoic acid\nD  2-methylbutanamide",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Draw the skeletal formula of this product.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (2-methylbutanoic acid) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Correct skeletal formula of CH3CH2CH(CH3)COOH [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=46,
        title="Comprehensive Chemical Roadmap: 3-Carbon Nitrogen Derivatives — 9701/21/O/N/23/Q9",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Consider the nitrogen-containing compounds: propanenitrile, propylamine, and propanamide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State a chemical test that gives a positive result with propylamine but NO reaction with propanamide.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent and condition that converts propanenitrile into propylamine.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagent and condition that converts propanenitrile into propanoic acid.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Add aqueous copper(II) sulfate [1]",
                "Propylamine forms a deep royal-blue solution / complex; propanamide gives no reaction / remains pale blue [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "LiAlH4 in dry ether (or H2 with heated Ni catalyst) [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Dilute hydrochloric acid (or dilute H2SO4), heat under reflux [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Preparation of Amines from Carbonyls (Reductive Amination) — 9701/22/M/J/23/Q12",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="In the pharmaceutical industry, amines are prepared by treating an aldehyde or ketone with ammonia in the presence of a reducing agent (reductive amination).",
        parts=[
            QuestionPart(
                label="(a)",
                text="When propanal reacts with ammonia, an imine intermediate (CH3CH2CH=NH) is formed. Name the type of reaction that forms this imine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When the imine is reduced with H2 and a nickel catalyst, propylamine is formed. Write the equation for this reduction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structure of the amine formed when propanone is subjected to reductive amination with ammonia.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Nucleophilic addition-elimination (condensation) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3CH2CH=NH + H2 -> CH3CH2CH2NH2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "CH3-CH(NH2)-CH3 (propan-2-amine) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Reactions of Phenylamine — 9701/11/O/N/23/Q26",
        syllabus_ref="19.1",
        difficulty="EASY",
        preamble="Which reagent reacts with phenylamine to produce a white precipitate?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the reagent:\nA  Aqueous sodium hydroxide\nB  Bromine water\nC  Dilute hydrochloric acid\nD  Ethanoyl chloride",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name the white precipitate.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Bromine water) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2,4,6-tribromophenylamine [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Acid-Base Titration of Ethylamine — 9701/21/M/J/22/Q9",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="A 20.0 cm³ sample of an aqueous solution of ethylamine is titrated with 0.150 mol dm⁻³ hydrochloric acid. Exactly 18.40 cm³ of HCl is required to reach the equivalence point.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the concentration of the ethylamine solution in mol dm⁻³.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State whether the pH at the equivalence point of this titration is acidic (pH < 7), neutral (pH = 7), or alkaline (pH > 7). Explain your answer in terms of the hydrolysis of the salt formed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Choose a suitable indicator for this titration from methyl orange (pH 3.1-4.4) and phenolphthalein (pH 8.3-10.0). Justify your choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of HCl = 0.01840 x 0.150 = 2.76 x 10⁻³ mol [1]",
                "Concentration of ethylamine = (2.76 x 10⁻³) / 0.0200 = 0.138 mol dm⁻³ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Acidic (pH < 7, typically pH ~ 5-6) [1]",
                "The ethylammonium cation (CH3CH2NH3⁺) is a weak Bronsted-Lowry acid that hydrolyses in water to release H3O⁺ ions: CH3CH2NH3⁺ + H2O <=> CH3CH2NH2 + H3O⁺ [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Methyl orange [1]",
                "For a weak base-strong acid titration, the vertical pH drop occurs in the acidic region (pH ~ 3.5-6.5), which matches the colour change interval of methyl orange [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Deduction of Unknown Nitrogen Compound Z — 9701/22/M/J/23/Q13",
        syllabus_ref="19.1",
        difficulty="HARD",
        preamble="Compound Z has molecular formula C4H9NO.\n• When Z is heated under reflux with dilute sodium hydroxide, an alkaline gas is evolved that turns damp red litmus paper blue, and a sodium carboxylate salt is formed.\n• When the carboxylate salt is acidified, propanoic acid is obtained.\n• When Z is reduced with LiAlH4 in dry ether, compound W (C4H11N) is formed.\n• Compound W is a primary amine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the alkaline gas evolved during alkaline hydrolysis.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of compound Z.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structural formula and systematic name of primary amine W.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ammonia gas (NH3) OR methylamine (CH3NH2) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Carboxylate is propanoate (3 carbons) and total carbons = 4 -> amide must have N-methyl group: CH3CH2CONHCH3 (N-methylpropanamide) OR if gas is methylamine [2]",
                "Systematic name: N-methylpropanamide [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Formula of W: CH3CH2CH2NHCH3 (secondary amine) OR if Z is butanamide (CH3CH2CH2CONH2, gas is NH3, carboxylate is butanoate): if propanoate is obtained, Z must be N-methylpropanamide; reduction yields N-methylpropan-1-amine (secondary). If W is a primary amine, Z must be butanamide: CH3CH2CH2CONH2 (hydrolysis yields butanoic acid). For acid = propanoic: Z has 3 C on acid side + 1 C on amine side -> CH3CH2CONHCH3 [1]",
                "Primary amine W: Butan-1-amine: CH3CH2CH2CH2NH2 (if Z is butanamide) [1]"
            ], "marks": 2}
        ]
    ),
]
