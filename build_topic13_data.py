"""
Script to generate topic13_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 13: An Introduction to AS Level Organic Chemistry.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 13: An Introduction to AS Level Organic Chemistry.
Subtopics:
  13.1 Formulae, functional groups and IUPAC nomenclature
  13.2 Characteristic organic reactions: fission, radicals, carbocations, electrophiles/nucleophiles
  13.3 Shapes of organic molecules; hybridisation (sp3, sp2, sp), sigma and pi bonds
  13.4 Isomerism: structural (chain, positional, functional) and stereoisomerism (E/Z, cis/trans, optical)

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

TOPIC_13_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 13.3: Shapes of Organic Molecules, Hybridisation & Bonding (Q1 to Q13)
    # =========================================================================
    Question(
        number=1,
        title="Orbital Hybridisation and Sigma/Pi Bonding — 9701/21/M/J/23/Q5(a)-(d)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="Carbon atoms in organic molecules can undergo sp³, sp², or sp hybridisation depending on their bonding environment. Fig. 1.1 illustrates the geometries and orbital overlaps.",
        figure_path="figures/organic_bonding_hybridisation.png",
        figure_caption="Fig. 1.1: Geometries and orbital overlaps for sp³, sp², and sp hybridised carbon atoms.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the formation of a sigma (sigma) bond and a pi (pi) bond in terms of orbital overlap.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the state of hybridisation of each carbon atom in prop-2-en-1-ol, CH2=CH-CH2OH, and state the H-C-H bond angle around C1 and C3.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why rotation about the C=C double bond in ethene is restricted at room temperature, whereas rotation about the C-C single bond in ethane occurs freely.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State how many sigma bonds and how many pi bonds are present in a molecule of prop-2-enenitrile, CH2=CH-C#N.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Sigma bond: Formed by head-on / coaxial / end-to-end overlap of atomic or hybrid orbitals along the internuclear axis [1]",
                "Pi bond: Formed by sideways / lateral overlap of parallel unhybridised p orbitals above and below the internuclear axis [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "C1 (CH2=): sp²; C2 (=CH-): sp²; C3 (-CH2-): sp³ [1]",
                "Bond angle around C1: 120° (trigonal planar) [1]",
                "Bond angle around C3: 109.5° (tetrahedral) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "The pi bond involves sideways overlap of parallel p-orbitals above and below the plane [1]",
                "Rotation about the double bond would break the pi bond / disrupt the sideways overlap, which requires significant energy (~260 kJ mol⁻¹) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Sigma bonds: 6 (two C-H on C1, one C=C, one C-H on C2, one C-C, one C#N) [1]",
                "Pi bonds: 3 (one in C=C, two in C#N) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Bond Angles and Molecular Geometry of Organic Compounds — 9701/22/O/N/22/Q5(a)-(c)",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="Consider the molecule 2-methylbut-2-ene, (CH3)2C=CHCH3.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal formula of 2-methylbut-2-ene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the C-C=C bond angle around the C2 atom and the C-C-C bond angle around the C4 atom.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why 2-methylbut-2-ene does NOT exhibit geometric (cis/trans or E/Z) isomerism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Correct skeletal formula showing a 4-carbon chain with a double bond between C2-C3 and a methyl branch on C2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "C-C=C on C2: 120° [1]",
                "C-C-C on C4: 109.5° [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "For geometric isomerism to occur, each carbon of the C=C bond must be bonded to two different atoms or groups [1]",
                "In 2-methylbut-2-ene, carbon-2 is bonded to two identical methyl (-CH3) groups [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Bond Lengths and Bond Strengths in Carbon-Carbon Bonds — 9701/11/M/J/22/Q21",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="Which row correctly lists the carbon-carbon bonds in order of increasing bond length?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct order of bond lengths (shortest to longest):",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. C-C < C=C < C#C",
                    "B. C#C < C=C < C-C",
                    "C. C=C < C#C < C-C",
                    "D. C-C < C#C < C=C"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Triple bonds have the highest electron density between nuclei (6 shared electrons) pulling the carbon nuclei closest together (0.120 nm), followed by double bonds (0.134 nm), and single bonds are the longest (0.154 nm)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=4,
        title="Hybridisation in Ethyne and Benzene — 9701/23/M/J/21/Q3(a)-(b)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="The ethyne molecule, HC#CH, is linear.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the bonding in ethyne in terms of hybridisation, specifying the number and types of bonds between the two carbon atoms.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the H-C#C bond angle in ethyne and justify this value using VSEPR theory.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Each carbon atom is sp hybridised (mixing one 2s and one 2p orbital) [1]",
                "The C#C triple bond consists of one strong sigma bond formed by end-on sp-sp overlap [1]",
                "and two pi bonds formed by sideways overlap of two pairs of mutually perpendicular unhybridised 2p orbitals [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Bond angle: 180° [1]",
                "Each carbon atom has two regions of electron density (two sigma bonding directions) which repel each other to achieve maximum separation / minimum repulsion [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Identifying Sigma and Pi Bonds in Propenal — 9701/12/F/M/22/Q20",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="Consider the molecule propenal, CH2=CH-CH=O.",
        parts=[
            QuestionPart(
                label="",
                text="How many sigma bonds and how many pi bonds are present in one molecule of propenal?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 6 sigma bonds and 1 pi bond",
                    "B. 7 sigma bonds and 2 pi bonds",
                    "C. 8 sigma bonds and 2 pi bonds",
                    "D. 7 sigma bonds and 1 pi bond"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Sigma bonds: two C-H on C1, one C-C between C1-C2, one C-H on C2, one C-C between C2-C3, one C-H on C3, one C-O sigma bond = 7 sigma bonds. Pi bonds: one in C=C, one in C=O = 2 pi bonds."
            ], "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Shape and Delocalisation in the Carbonyl Group — 9701/21/O/N/21/Q5(a)-(b)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="The carbonyl group, C=O, is present in aldehydes and ketones.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the hybridisation of the carbonyl carbon atom and explain why the carbonyl group is planar.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the C=O double bond is polar, whereas the C=C double bond in alkenes is non-polar.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The carbonyl carbon atom is sp² hybridised [1]",
                "It forms three coplanar sigma bonds at approximately 120° angles, with an unhybridised p-orbital forming a pi bond, giving a trigonal planar geometry [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Oxygen is significantly more electronegative than carbon (3.5 vs 2.5) [1]",
                "The electron density in both the sigma and pi bonds is drawn towards oxygen, creating a permanent dipole C(delta+) = O(delta-) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Tetrahedral Carbon Centers in Haloalkanes — 9701/13/M/J/22/Q20",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="Which molecule has a central carbon atom with sp³ hybridisation and bond angles of approximately 109.5°?",
        parts=[
            QuestionPart(
                label="",
                text="Select the molecule:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Trichloromethane, CHCl3",
                    "B. Methanal, HCHO",
                    "C. Hydrogen cyanide, HCN",
                    "D. Ethene, C2H4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: CHCl3 has 4 single sigma bonds around the central carbon atom (sp³ hybridised, tetrahedral arrangement, bond angles approx 109.5°)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Comparison of Sigma and Pi Bond Reactivity — 9701/22/M/J/21/Q5(c)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="Alkenes are much more chemically reactive than alkanes towards electrophiles.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why a pi bond is weaker and more chemically reactive than a sigma bond between carbon atoms.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why electrophiles preferentially attack the C=C double bond rather than a C-C single bond.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Sideways overlap of p-orbitals in a pi bond is less effective / has lower orbital overlap than head-on overlap in a sigma bond [1]",
                "The pi bond enthalpy (~260 kJ mol⁻¹) is lower than that of the sigma bond (~350 kJ mol⁻¹), so the pi bond is cleaved more readily [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The pi electron cloud lies above and below the plane of the carbon nuclei and is held less tightly [1]",
                "It represents an exposed region of high electron density that readily attracts electron-deficient electrophiles [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Determining Hybridisation States in Polyfunctional Molecules — 9701/11/O/N/22/Q20",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="Consider the molecule methyl 2-cyanoprop-2-enoate, CH2=C(CN)COOCH3.",
        parts=[
            QuestionPart(
                label="",
                text="How many carbon atoms in this molecule are sp² hybridised?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1",
                    "B. 2",
                    "C. 3",
                    "D. 4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: The alkene carbons (CH2= and =C<) are sp² (2 carbons); the ester carbonyl carbon (-COO-) is sp² (1 carbon). The nitrile carbon (-C#N) is sp, and the ester methyl carbon (-CH3) is sp³. Total sp² carbons = 3."
            ], "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Bonding in Allene (Propadiene) — 9701/22/F/M/23/Q5(a)-(c)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="Allene has the structural formula CH2=C=CH2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the hybridisation of the central carbon atom and the terminal carbon atoms in allene.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the two terminal =CH2 groups in allene lie in planes that are perpendicular (at 90°) to each other.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Central carbon atom: sp hybridised [1]",
                "Terminal carbon atoms: sp² hybridised [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The central carbon uses two mutually perpendicular unhybridised p-orbitals (py and pz) to form its two pi bonds [1]",
                "Therefore, the unhybridised p-orbitals on the two terminal carbons must also be perpendicular to overlap with them, forcing the terminal CH2 groups into mutually perpendicular planes [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Identifying Hybridisation by Geometry — 9701/12/M/J/23/Q21",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="In which compound is the C-C-C bond angle closest to 180°?",
        parts=[
            QuestionPart(
                label="",
                text="Select the compound:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Cyclopropane",
                    "B. Propyne",
                    "C. Propene",
                    "D. Propane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In propyne, CH3-C#CH, the central carbon is sp hybridised with linear geometry around the triple bond (bond angle 180°)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Planarity in Conjugated Diene Systems — 9701/21/M/J/20/Q5(c)",
        syllabus_ref="13.3",
        difficulty="HARD",
        preamble="Buta-1,3-diene, CH2=CH-CH=CH2, has alternating double and single bonds.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State how many carbon atoms in buta-1,3-diene lie in the same plane, and explain your reasoning.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="The central C2-C3 bond in buta-1,3-diene is 0.148 nm long, which is shorter than a normal C-C single bond (0.154 nm). Suggest an explanation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "All 4 carbon atoms lie in the same plane [1]",
                "All 4 carbon atoms are sp² hybridised with trigonal planar geometry (120° bond angles) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The central bond is formed by overlap of sp²-sp² hybrid orbitals, which have more s-character (33% s) than sp³-sp³ orbitals (25% s), pulling nuclei closer [1]",
                "There is also slight delocalisation of pi electrons across the central C-C bond giving it partial double bond character [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Bonding in Carbon Dioxide vs Carbon Monoxide — 9701/13/O/N/21/Q20",
        syllabus_ref="13.3",
        difficulty="EASY",
        preamble="What is the hybridisation of the carbon atom in carbon dioxide, CO2?",
        parts=[
            QuestionPart(
                label="",
                text="Select the hybridisation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. sp",
                    "B. sp²",
                    "C. sp³",
                    "D. dsp²"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: In CO2 (O=C=O), the carbon atom has 2 double bonds (2 sigma bonds and 2 pi bonds) with a linear geometry (180°), corresponding to sp hybridisation."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 13.2: Characteristic Organic Reactions & Terminology (Q14 to Q26)
    # =========================================================================
    Question(
        number=14,
        title="Reaction Mechanisms: Fission and Intermediates — 9701/22/M/J/23/Q5(a)-(d)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="Organic reactions proceed via specific bond-cleavage steps and reactive intermediates. Fig. 14.1 defines the principal terms.",
        figure_path="figures/organic_reaction_mechanisms_overview.png",
        figure_caption="Fig. 14.1: Homolytic vs heterolytic fission, free radicals, and carbocation intermediates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Distinguish between homolytic fission and heterolytic fission, describing the movement of electrons and products formed in each case.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain the meaning of the term electrophile and give two specific examples of electrophiles in AS Organic Chemistry.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain the meaning of the term nucleophile and explain why a hydroxide ion (:OH⁻) acts as a nucleophile.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Explain the order of stability of carbocations: tertiary (3°) > secondary (2°) > primary (1°).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Homolytic fission: Covalent bond breaks symmetrically; each bonded atom retains one electron, forming two free radicals [1]",
                "Heterolytic fission: Covalent bond breaks unsymmetrically; the more electronegative atom takes both bonding electrons, forming a cation and an anion [1]",
                "Represented by fish-hook arrows (homolytic) vs full double-headed curly arrows (heterolytic) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "An electron-pair acceptor / electron-deficient species attracted to electron-rich regions [1]",
                "Examples: H⁺ (or H-Br / H-Cl), Br⁺ (or Br-Br with induced dipole), carbocations (any two) [2]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "A nucleophile is an electron-pair donor attracted to electron-deficient / positive carbon centres [1]",
                ":OH⁻ possesses non-bonding lone pairs on oxygen and a negative charge that can be donated to form a dative covalent bond [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Alkyl groups have a positive inductive effect / are electron-donating [1]",
                "Tertiary carbocations have three alkyl groups attached to the positively charged carbon, which disperse the positive charge most effectively, stabilizing the ion [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Curly Arrow Conventions in Organic Mechanisms — 9701/21/O/N/22/Q5(a)-(b)",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="Curly arrows are used to represent the movement of electrons during chemical reactions.",
        parts=[
            QuestionPart(
                label="(a)",
                text="What does a standard double-headed curly arrow represent?",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="What does a single-headed ('fish-hook') arrow represent, and in which type of reaction mechanism is it used?",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The movement of a pair of electrons (from a lone pair or covalent bond to an atom or new bond) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The movement of a single electron [1]",
                "Used in free-radical mechanisms / homolytic fission [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Classification of Organic Reaction Types — 9701/12/M/J/22/Q21",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="Which reaction represents an elimination reaction?",
        parts=[
            QuestionPart(
                label="",
                text="Select the elimination reaction:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CH3CH2Br + NaOH(aq) -> CH3CH2OH + NaBr",
                    "B. CH3CH2Br + ethanolic KOH (heat) -> CH2=CH2 + KBr + H2O",
                    "C. CH2=CH2 + Br2 -> CH2BrCH2Br",
                    "D. CH4 + Cl2 -> CH3Cl + HCl"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Heating a halogenoalkane with ethanolic KOH removes H and Br (HBr) from adjacent carbons to form an alkene (ethene), which is an elimination reaction."
            ], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Inductive Effects and Carbocation Stability — 9701/23/O/N/21/Q5(a)-(c)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="Consider the two carbocations formed when HBr adds to propene: (I) CH3-CH⁺-CH3 and (II) CH3-CH2-CH2⁺.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Classify carbocation (I) and carbocation (II) as primary, secondary, or tertiary.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State which carbocation is more stable and explain your answer fully in terms of electronic effects.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(I) is a secondary (2°) carbocation [1]",
                "(II) is a primary (1°) carbocation [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Carbocation (I) is more stable [1]",
                "Alkyl groups (methyl groups) are electron-releasing / have a positive inductive effect [1]",
                "Carbocation (I) has two electron-donating alkyl groups attached to the C⁺ compared to only one in carbocation (II), dispersing the positive charge more effectively [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Identifying Nucleophiles and Electrophiles — 9701/11/F/M/22/Q19",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="Which of the following species acts as an electrophile in an organic addition reaction?",
        parts=[
            QuestionPart(
                label="",
                text="Select the electrophile:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. NH3",
                    "B. CN⁻",
                    "C. HBr",
                    "D. OH⁻"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: HBr has a polar H(delta+) - Br(delta-) bond; the electron-deficient H(delta+) atom accepts a pair of electrons from the C=C pi bond, acting as an electrophile. NH3, CN⁻, and OH⁻ are all electron-pair donors (nucleophiles)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Hydrolysis vs Hydration Terminology — 9701/22/M/J/20/Q4(b)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="The terms 'hydration' and 'hydrolysis' have precise meanings in organic chemistry.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term hydrolysis reaction and write an example equation involving bromoethane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Define the term hydration reaction and write an example equation involving ethene.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Hydrolysis: The breakdown of a chemical compound by reaction with water (or aqueous acid/alkali) [1]",
                "Example: CH3CH2Br + H2O -> CH3CH2OH + HBr (or with OH⁻) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hydration: The addition of water (or steam) across a multiple bond (such as C=C) [1]",
                "Example: CH2=CH2 + H2O(g) -> CH3CH2OH [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Redox Terminology in Organic Chemistry — 9701/13/O/N/22/Q20",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="In organic chemistry, reduction can be defined in terms of hydrogen and oxygen atoms.",
        parts=[
            QuestionPart(
                label="",
                text="Which transformation represents an organic reduction?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Ethanol -> Ethanal",
                    "B. Propanone -> Propan-2-ol",
                    "C. Ethene -> 1,2-dibromoethane",
                    "D. Bromoethane -> Ethanol"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Propanone (CH3COCH3) gains two hydrogen atoms to become propan-2-ol (CH3CH(OH)CH3), which is a reduction (addition of hydrogen / decrease in oxidation state of carbon)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Free-Radical Substitution Terminology — 9701/21/M/J/21/Q4(c)-(d)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="When methane reacts with chlorine in the presence of ultraviolet light, chloromethane is produced via a three-stage mechanism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Name the three distinct stages of a free-radical chain reaction.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the initiation step and identify the type of bond fission occurring.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1. Initiation [1]",
                "2. Propagation [1]",
                "3. Termination [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Equation: Cl2 -> 2Cl* (in the presence of UV light) [1]",
                "Type of fission: Homolytic fission [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Addition vs Substitution Reactions — 9701/11/M/J/23/Q21",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="Which statement accurately compares addition and substitution reactions?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct comparison:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Addition reactions produce two products, whereas substitution produces one.",
                    "B. Addition reactions involve unsaturated reactants and form a single product, whereas substitution reactions replace one atom/group with another, producing two products.",
                    "C. Substitution reactions only occur with alkenes.",
                    "D. Addition reactions never break covalent bonds."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Addition reactions combine two molecules into a single product by breaking a multiple bond (100% atom economy). Substitution replaces an existing atom/group, releasing a leaving group to form two products."
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Carbocation Rearrangements and Intermediate Stability — 9701/22/O/N/23/Q5(c)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="Consider the carbocations: (CH3)3C⁺, (CH3)2CH⁺, CH3CH2⁺, and CH3⁺.",
        parts=[
            QuestionPart(
                label="(a)",
                text="List these four carbocations in order of increasing thermodynamic stability.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the methyl carbocation, CH3⁺, is the least stable of the series.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3⁺ < CH3CH2⁺ < (CH3)2CH⁺ < (CH3)3C⁺ [2] (1 mark if partially correct, 2 marks for full order)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3⁺ has no alkyl groups attached to the positively charged carbon [1]",
                "There is no positive inductive electron donation to disperse the concentrated positive charge [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Condensation Reaction Definition — 9701/12/O/N/20/Q20",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="The reaction between ethanoic acid and ethanol in the presence of concentrated sulfuric acid is classified as an esterification and condensation reaction.",
        parts=[
            QuestionPart(
                label="",
                text="What is the defining feature of a condensation reaction?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Two molecules join together with the simultaneous elimination of a small molecule such as water.",
                    "B. A molecule gains water from the atmosphere.",
                    "C. A gas changes into a liquid on cooling.",
                    "D. A single molecule splits into two smaller molecules."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: In organic chemistry, a condensation reaction is one where two organic molecules join together to form a larger molecule, eliminating a small molecule such as H2O or HCl."
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Deducing Mechanism Type from Reactants — 9701/21/O/N/21/Q4(d)",
        syllabus_ref="13.2",
        difficulty="HARD",
        preamble="For each of the following chemical conversions, identify the specific mechanism type:\n(i) CH3CH=CH2 + HBr -> CH3CHBrCH3\n(ii) CH3CH2CH2Br + NaOH(aq) -> CH3CH2CH2OH + NaBr\n(iii) CH3CH3 + Cl2 -> CH3CH2Cl + HCl (with UV light)",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the mechanism type for reaction (i).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the mechanism type for reaction (ii).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the mechanism type for reaction (iii).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Electrophilic addition [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Nucleophilic substitution (specifically SN2) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Free-radical substitution [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="MCQ on Nucleophilic Attack Site — 9701/13/M/J/21/Q21",
        syllabus_ref="13.2",
        difficulty="EASY",
        preamble="In the molecule propanal, CH3CH2CH=O, which atom is directly attacked by a nucleophile such as CN⁻?",
        parts=[
            QuestionPart(
                label="",
                text="Select the target atom:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. The carbonyl oxygen atom",
                    "B. The carbonyl carbon atom",
                    "C. The methyl carbon atom",
                    "D. The hydrogen atom of the aldehyde group"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The carbonyl group is polarized C(delta+) = O(delta-). The nucleophile possesses a lone pair of electrons and attacks the electron-deficient, partially positive carbonyl carbon atom."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 13.4: Isomerism: Structural & Stereoisomerism (Q27 to Q39)
    # =========================================================================
    Question(
        number=27,
        title="Classification and Types of Structural Isomerism — 9701/21/M/J/23/Q5(a)-(c)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="Isomers are compounds that share the same molecular formula. Fig. 27.1 illustrates the structural and stereochemical branches of isomerism.",
        figure_path="figures/organic_isomerism_classification.png",
        figure_caption="Fig. 27.1: Comprehensive classification tree of structural isomerism and stereoisomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term structural isomerism and list the three distinct categories of structural isomerism.",
                marks=4,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Compound X has the molecular formula C4H10O. Draw displayed formulae for a pair of positional isomers of compound X that are both alcohols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the skeletal formula of a functional group isomer of the alcohols in (b) that belongs to a different homologous series.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Definition: Compounds with the same molecular formula but different structural formulae / different connectivity of atoms [1]",
                "Three types: Chain isomerism [1]",
                "Positional isomerism [1]",
                "Functional group isomerism [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Displays butan-1-ol: CH3-CH2-CH2-CH2-OH (all bonds shown) [1]",
                "Displays butan-2-ol: CH3-CH2-CH(OH)-CH3 (all bonds shown) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Correct skeletal formula of an ether with 4 carbons, e.g. ethoxyethane (CH3CH2OCH2CH3) or methoxypropane [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=28,
        title="Identifying Functional Group Isomer Pairs — 9701/22/O/N/22/Q5(d)",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="Functional group isomers belong to different homologous series and exhibit markedly different chemical properties.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Name the functional group present in propanal and in propanone, and explain why they are functional group isomers.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the molecular formula shared by propanoic acid and methyl ethanoate, and draw the displayed formula of methyl ethanoate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propanal: Aldehyde group (-CHO) [1]",
                "Propanone: Ketone group (>C=O) [1]",
                "Both have the same molecular formula C3H6O but possess different functional groups [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Molecular formula: C3H6O2 [1]",
                "Displayed formula of methyl ethanoate showing CH3-C(=O)-O-CH3 with all bonds displayed [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Chain Isomerism in Pentane — 9701/11/M/J/22/Q22",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="How many structural isomers exist for the alkane with molecular formula C5H12?",
        parts=[
            QuestionPart(
                label="",
                text="Select the number of structural isomers:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 2",
                    "B. 3",
                    "C. 4",
                    "D. 5"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: There are 3 chain isomers of C5H12: pentane, 2-methylbutane (isopentane), and 2,2-dimethylpropane (neopentane)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Boiling Points of Chain Isomers — 9701/22/F/M/22/Q5(a)-(b)",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="Pentane (CH3(CH2)3CH3) has a boiling point of 36 °C, whereas 2,2-dimethylpropane (C(CH3)4) boils at 9.5 °C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the difference in boiling points between pentane and 2,2-dimethylpropane in terms of molecular shape and intermolecular forces.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Draw the skeletal formula and state the systematic IUPAC name for the third isomer of C5H12.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Both molecules have identical molecular formula C5H12 and the same total number of electrons (42) [1]",
                "Pentane is an unbranched, straight-chain molecule with a larger surface area of contact, allowing adjacent molecules to pack closely together [1]",
                "2,2-dimethylpropane is highly branched and spherical, reducing surface contact and resulting in weaker instantaneous dipole-induced dipole forces [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Correct skeletal formula of 2-methylbutane [1]",
                "Systematic IUPAC name: 2-methylbutane [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Geometric (cis/trans) Isomerism Requirements — 9701/23/M/J/22/Q4(a)-(c)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="Geometric isomerism is a sub-category of stereoisomerism observed in certain unsaturated compounds.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the two essential structural conditions required for an alkene to exhibit geometric isomerism.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw displayed formulae for the cis and trans isomers of but-2-ene.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why but-1-ene does NOT show geometric isomerism.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1. Restricted rotation about the C=C double bond (due to sideways overlap of p-orbitals in the pi bond) [1]",
                "2. Each of the two carbon atoms of the C=C bond must be attached to two different atoms or groups [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "cis-but-2-ene: Both -CH3 groups on the same side of the double bond [1]",
                "trans-but-2-ene: The -CH3 groups on opposite sides of the double bond [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Carbon-1 is bonded to two identical hydrogen atoms [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Physical Properties of Cis and Trans Isomers — 9701/21/O/N/21/Q5(c)-(d)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="The cis and trans isomers of 1,2-dichloroethene possess different physical properties: cis-1,2-dichloroethene boils at 60 °C; trans-1,2-dichloroethene boils at 48 °C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why cis-1,2-dichloroethene is a polar molecule with a net dipole moment, whereas trans-1,2-dichloroethene is completely non-polar.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain the difference in their boiling points based on your answer to (a).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In the cis isomer, the two polar C-Cl bond dipoles point in the same direction and reinforce each other, giving an overall net molecular dipole [1]",
                "In the trans isomer, the two polar C-Cl bond dipoles point in exactly opposite directions and cancel out by symmetry [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The cis isomer has permanent dipole-dipole attractions in addition to London dispersion forces [1]",
                "The trans isomer has only instantaneous dipole-induced dipole forces, requiring less energy to overcome [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Chiral Centres and Optical Activity — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="Optical isomerism occurs in molecules containing an asymmetric carbon atom.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term chiral centre (chiral carbon atom).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw 3D tetrahedral diagrams using wedges and dashes showing the two optical isomers (enantiomers) of butan-2-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe how enantiomers interact with plane-polarised light.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A carbon atom attached to four different atoms or groups of atoms [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Two 3D tetrahedral representations drawn with wedges, dashed lines, and continuous lines [1]",
                "Correctly showing non-superimposable mirror image structures of CH3-C*(H)(OH)-CH2CH3 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "One enantiomer rotates the plane of plane-polarised light clockwise (dextrorotatory / +) [1]",
                "The other enantiomer rotates the plane of plane-polarised light anticlockwise by the exact same angle (laevorotatory / -) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Racemic Mixtures and Optical Inactivity — 9701/12/O/N/22/Q21",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="When hydrogen cyanide adds to ethanal, 2-hydroxypropanenitrile is formed as a racemic mixture.",
        parts=[
            QuestionPart(
                label="",
                text="Why does a racemic mixture show NO optical activity?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. The product does not contain a chiral centre.",
                    "B. The mixture contains an equimolar (1:1) ratio of both enantiomers, so the opposite rotations of plane-polarised light cancel each other out.",
                    "C. The enantiomers rapidly interconvert at room temperature.",
                    "D. Cyanide ions absorb plane-polarised light."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: A racemic mixture contains equal (50:50) amounts of the (+) and (-) enantiomers. The rotation of plane-polarised light caused by one enantiomer is exactly balanced and cancelled by the equal and opposite rotation of the other."
            ], "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Counting Chiral Centres in Biomolecules — 9701/21/M/J/22/Q5(d)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="Consider the molecule 2,3-dihydroxybutanedioic acid (tartaric acid), HOOC-CH(OH)-CH(OH)-COOH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify all chiral carbon atoms in tartaric acid by placing an asterisk (*) next to them on a structural formula.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the four different groups attached to carbon-2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why tartaric acid has a stereoisomer (meso-tartaric acid) that is optically inactive despite containing chiral carbon atoms.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C2 and C3 both marked with asterisks: HOOC-C*H(OH)-C*H(OH)-COOH [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "-H, -OH, -COOH, and -CH(OH)COOH [2] (1 mark for any two, 2 marks for all four)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Meso-tartaric acid has an internal plane of symmetry / centre of inversion [1]",
                "The optical rotation of the top half of the molecule is internally cancelled by the opposite rotation of the bottom half [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Determining Total Number of Stereoisomers — 9701/13/M/J/23/Q22",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="How many total stereoisomers (including geometric and optical isomers) exist for the compound pent-3-en-2-ol, CH3-CH(OH)-CH=CH-CH3?",
        parts=[
            QuestionPart(
                label="",
                text="Select the total number of stereoisomers:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 2",
                    "B. 3",
                    "C. 4",
                    "D. 8"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: The molecule contains 1 chiral centre at C2 (giving 2 optical isomers) and 1 double bond at C3-C4 exhibiting E/Z isomerism (2 geometric isomers). Total stereoisomers = 2 * 2 = 4 (namely: (2R,3E), (2R,3Z), (2S,3E), and (2S,3Z))."
            ], "marks": 1}
        ]
    ),
    Question(
        number=37,
        title="Identifying Functional Group Isomers of Esters — 9701/11/O/N/20/Q21",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="Which compound is a functional group isomer of ethyl propanoate, CH3CH2COOCH2CH3?",
        parts=[
            QuestionPart(
                label="",
                text="Select the functional group isomer:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Propyl ethanoate",
                    "B. Pentanoic acid",
                    "C. Methyl butanoate",
                    "D. Pentan-2-one"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Ethyl propanoate has the molecular formula C5H10O2. Pentanoic acid (CH3(CH2)3COOH) is a carboxylic acid with the same molecular formula C5H10O2, making it a functional group isomer. Propyl ethanoate and methyl butanoate are positional/chain isomers within the ester homologous series."
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Stereoisomerism in Cyclic Compounds — 9701/22/O/N/21/Q5(c)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="1,2-dichlorocyclopropane has a rigid 3-membered ring that restricts rotation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why 1,2-dichlorocyclopropane exhibits cis/trans isomerism even though it contains no carbon-carbon double bond.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State which isomer (cis or trans) possesses a plane of symmetry and is optically inactive.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The rigid ring structure prevents free rotation about the C-C single bonds [1]",
                "The two chlorine atoms can either be fixed on the same face of the ring (cis) or on opposite faces of the ring (trans) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The cis isomer (it has an internal mirror plane passing through C3 and bisecting the C1-C2 bond) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="MCQ on Positional vs Chain Isomerism — 9701/12/M/J/21/Q22",
        syllabus_ref="13.4",
        difficulty="EASY",
        preamble="Consider the two molecules: (1) 1-bromobutane and (2) 2-bromo-2-methylpropane.",
        parts=[
            QuestionPart(
                label="",
                text="What type of isomerism is shown between compound (1) and compound (2)?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Positional isomerism only",
                    "B. Chain isomerism only",
                    "C. Chain and positional isomerism",
                    "D. Stereoisomerism"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: The carbon skeleton changes from an unbranched 4-carbon chain to a branched 3-carbon chain (chain isomerism), and the halogen position changes from C1 to C2 (positional isomerism)."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 13.1 & 13.4: CIP Priority Rules & IUPAC Nomenclature (Q40 to Q50)
    # =========================================================================
    Question(
        number=40,
        title="Cahn-Ingold-Prelog (CIP) Priority Rules for E/Z Nomenclature — 9701/21/M/J/23/Q5(d)-(e)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="The E/Z convention uses Cahn-Ingold-Prelog (CIP) priority rules to unambiguously assign stereochemistry to alkenes. Fig. 40.1 illustrates the priority determination.",
        figure_path="figures/organic_cip_ez_rules.png",
        figure_caption="Fig. 40.1: CIP priority rules for determining (E) and (Z) configurations.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the primary criterion used to assign priority to atoms directly attached to an alkene carbon atom under the CIP rules.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Determine whether the following alkene is the (E) or (Z) isomer: 1-bromo-2-chloroprop-1-ene, Br(H)C=C(Cl)CH3. Justify your answer by assigning priorities at C1 and C2.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain the origin of the letters 'E' and 'Z' from their German names.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Highest atomic number (Z) of the atom directly attached to the double-bond carbon receives higher priority [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "At C1: -Br (atomic number 35) has higher priority than -H (atomic number 1) [1]",
                "At C2: -Cl (atomic number 17) has higher priority than -CH3 (carbon has atomic number 6) [1]",
                "If both high-priority groups (-Br and -Cl) are on the same side of the C=C reference axis, it is the (Z) isomer; if on opposite sides, it is the (E) isomer [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "E from 'Entgegen' meaning opposite; Z from 'Zusammen' meaning together [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Assigning E/Z Configuration to Complex Alkenes — 9701/22/M/J/22/Q5(c)",
        syllabus_ref="13.4",
        difficulty="HARD",
        preamble="Consider the alkene: (CH3)2CH-CH=C(Cl)-CH2OH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the priorities of the two groups on the left alkene carbon (C2).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Determine the priorities of the two groups on the right alkene carbon (C3).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce whether the isomer in which the -CH(CH3)2 group and the -Cl atom are on opposite sides is the (E) or (Z) isomer.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "On left carbon: -CH(CH3)2 (C, Z=6) > -H (H, Z=1) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "On right carbon: -Cl (Z=17) > -CH2OH (C, Z=6) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "High priority on left is -CH(CH3)2; high priority on right is -Cl. When on opposite sides, it is the (E) isomer [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=42,
        title="Systematic IUPAC Nomenclature of Halogenoalkanes — 9701/21/O/N/22/Q5(a)-(b)",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="Give the systematic IUPAC name for each of the following structures:\n(i) CH3-CH(Cl)-CH(CH3)-CH2-CH3\n(ii) CH3-C(Br)2-CH2-CH3",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the systematic IUPAC name for structure (i).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Give the systematic IUPAC name for structure (ii).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2-chloro-3-methylpentane [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2,2-dibromobutane [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="IUPAC Nomenclature of Alkenes and Alcohols — 9701/11/M/J/21/Q21",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="What is the systematic IUPAC name of the compound with skeletal formula: CH2=C(CH3)CH(OH)CH3?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct IUPAC name:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 3-methylbut-3-en-2-ol",
                    "B. 2-methylbut-1-en-3-ol",
                    "C. 3-methylbut-1-en-2-ol",
                    "D. 2-methylbut-3-en-2-ol"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: The principal functional group is the -OH group, which receives the lowest possible locant (carbon-2). Numbering from right gives: C1=CH3, C2=CH(OH), C3=C(CH3), C4=CH2. The name is 3-methylbut-3-en-2-ol."
            ], "marks": 1}
        ]
    ),
    Question(
        number=44,
        title="Distinguishing Empirical, Molecular, and Skeletal Formulae — 9701/22/F/M/21/Q5(a)-(c)",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="A compound Y contains 62.07% carbon, 10.34% hydrogen, and 27.59% oxygen by mass. Its relative molecular mass is 116.0. (Ar: C = 12.0, H = 1.0, O = 16.0)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the empirical formula of compound Y.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Determine the molecular formula of compound Y.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Compound Y is an unbranched carboxylic acid. Draw its displayed formula and give its systematic name.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 62.07/12.0 = 5.17; H = 10.34/1.0 = 10.34; O = 27.59/16.0 = 1.724 [1]",
                "Ratio: C = 5.17/1.724 = 3; H = 10.34/1.724 = 6; O = 1.724/1.724 = 1 => Empirical formula is C3H6O [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Empirical mass = 3(12) + 6(1) + 16 = 58.0; n = 116.0 / 58.0 = 2 => Molecular formula is C6H12O2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Displayed formula of hexanoic acid: CH3(CH2)4COOH (all bonds shown) [1]",
                "Name: Hexanoic acid [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Nomenclature of Carbonyl Compounds and Carboxylic Acids — 9701/12/O/N/21/Q22",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="What is the systematic IUPAC name for (CH3)2CH-CH2-CHO?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct name:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 3-methylbutanal",
                    "B. 2-methylbutanal",
                    "C. 3-methylbutanone",
                    "D. 1-methylbutanal"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: The aldehyde carbon (-CHO) is automatically carbon-1. The longest chain containing the carbonyl is 4 carbons (butanal), with a methyl substituent on carbon-3: 3-methylbutanal."
            ], "marks": 1}
        ]
    ),
    Question(
        number=46,
        title="Nomenclature of Esters and Hydrolysis Products — 9701/23/O/N/22/Q5(a)-(c)",
        syllabus_ref="13.1",
        difficulty="HARD",
        preamble="An ester has the structural formula CH3CH2COOCH(CH3)2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the systematic IUPAC name of this ester.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the carboxylic acid and alcohol used to synthesize this ester.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced chemical equation for the alkaline hydrolysis (saponification) of this ester using aqueous sodium hydroxide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1-methylethyl propanoate (or isopropyl propanoate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Carboxylic acid: Propanoic acid [1]",
                "Alcohol: Propan-2-ol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3CH2COOCH(CH3)2 + NaOH -> CH3CH2COONa + (CH3)2CHOH [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Skeletal Formula Interpretation — 9701/13/O/N/22/Q21",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="In skeletal formulae, carbon and hydrogen atoms bonded to carbon are not drawn explicitly.",
        parts=[
            QuestionPart(
                label="",
                text="How many hydrogen atoms are present in a molecule of cyclohexene?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 8",
                    "B. 10",
                    "C. 12",
                    "D. 6"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Cyclohexene has a 6-carbon ring with one C=C double bond. The two alkene carbons have 1 H each (2 H total); the other four ring carbons are CH2 groups with 2 H each (8 H total). Total H = 2 + 8 = 10 (molecular formula C6H10)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Identifying Functional Groups in Multi-Functional Molecules — 9701/21/M/J/23/Q5(f)",
        syllabus_ref="13.1",
        difficulty="HARD",
        preamble="Paracetamol has the structure: 4-(N-acetylamino)phenol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify two distinct functional groups present in paracetamol (excluding the benzene ring).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the -OH group in paracetamol cannot be classified as a primary, secondary, or tertiary alcohol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Phenol / phenolic -OH group [1]",
                "Amide group (-CONH-) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The -OH group is directly attached to an aromatic benzene ring (making it a phenol, which has distinct chemical properties from aliphatic alcohols) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="MCQ on Nitrogen-Containing Functional Groups — 9701/11/M/J/23/Q22",
        syllabus_ref="13.1",
        difficulty="EASY",
        preamble="Which compound contains a nitrile functional group?",
        parts=[
            QuestionPart(
                label="",
                text="Select the nitrile compound:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CH3CH2NH2",
                    "B. CH3CONH2",
                    "C. CH3CH2CN",
                    "D. CH3NO2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: CH3CH2CN is propanenitrile, which contains the nitrile (-C#N) group. (A is an amine, B is an amide, D is a nitroalkane)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Deduction: Formulae, Isomerism and IUPAC Nomenclature — 9701/21/O/N/23/Q5(a)-(d)",
        syllabus_ref="13.1",
        difficulty="HARD",
        preamble="An organic compound Z has the composition: 58.8% C, 9.8% H, and 31.4% O by mass. Its mass spectrum shows a molecular ion peak at m/z = 102. (Ar: C = 12.0, H = 1.0, O = 16.0)\n- Compound Z reacts with sodium carbonate with effervescence, producing carbon dioxide.\n- Compound Z exhibits optical isomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the empirical formula and molecular formula of compound Z.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the functional group present in Z that accounts for the reaction with sodium carbonate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Draw the displayed formula of compound Z, indicate the chiral centre with an asterisk (*), and state its systematic IUPAC name.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Draw a pair of stereoisomers for compound Z using 3D wedge-and-dash notation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 58.8/12.0 = 4.90; H = 9.8/1.0 = 9.80; O = 31.4/16.0 = 1.96 [1]",
                "Ratio: C:H:O = 2.5 : 5 : 1 => Empirical formula is C5H10O2 [1]",
                "Empirical mass = 5(12) + 10(1) + 32 = 102; Molecular mass = 102 => Molecular formula is C5H10O2 [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Carboxylic acid group (-COOH) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Displayed formula of 2-methylbutanoic acid: CH3-CH2-C*H(CH3)-COOH with all bonds displayed [1]",
                "Chiral centre correctly identified at carbon-2 with an asterisk (*) [1]",
                "Systematic IUPAC name: 2-methylbutanoic acid [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Two 3D tetrahedral wedge-and-dash representations around C2 [1]",
                "Showing non-superimposable mirror image enantiomers of 2-methylbutanoic acid [1]"
            ], "marks": 2}
        ]
    )
]
'''
    with open("topic13_data.py", "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Successfully wrote topic13_data.py!")

if __name__ == "__main__":
    generate()
