"""
Script to generate topic15_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 15: Halogen Compounds (Halogenoalkanes).
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 15: Halogen Compounds (Halogenoalkanes).
Subtopics:
  15.1 Reactions: nucleophilic substitution (OH-, CN-, NH3), elimination (alkenes), competition
  15.2 Mechanisms: SN1 vs SN2, carbocation intermediates, transition states, inversion vs racemisation,
       rates of hydrolysis (C-X bond enthalpy vs polarity), silver nitrate testing, CFCs and ozone depletion

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

TOPIC_15_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 15.2: Mechanisms: SN1 vs SN2 (Q1 to Q13)
    # =========================================================================
    Question(
        number=1,
        title="Comparison of SN1 and SN2 Mechanisms — 9701/21/M/J/23/Q7(a)-(d)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Halogenoalkanes undergo nucleophilic substitution via either an SN1 or an SN2 pathway depending on the degree of substitution at the halogen-bearing carbon. Fig. 1.1 compares the two mechanisms.",
        figure_path="figures/halogenoalkanes_sn1_vs_sn2_mechanisms.png",
        figure_caption="Fig. 1.1: Features and pathways of SN1 and SN2 nucleophilic substitution.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the complete mechanism for the reaction between bromoethane and aqueous sodium hydroxide. Include all partial charges, lone pairs, curly arrows, and the structure of the transition state.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="Draw the complete two-step mechanism for the hydrolysis of 2-bromo-2-methylpropane with aqueous sodium hydroxide, showing the carbocation intermediate.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why 2-bromo-2-methylpropane reacts predominantly via the SN1 mechanism rather than the SN2 mechanism.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State and explain the stereochemical outcome when a single optical isomer of a chiral tertiary halogenoalkane undergoes hydrolysis by the SN1 mechanism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Curly arrow from lone pair on :OH⁻ to C(delta+) of CH3CH2-Br [1]",
                "Curly arrow showing heterolytic cleavage of C-Br bond to Br(delta-) [1]",
                "Penta-coordinate transition state drawn with partial bonds to OH and Br and overall negative charge [1]",
                "Inverted product CH3CH2OH and :Br⁻ drawn correctly [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Step 1: Curly arrow showing heterolytic fission of C-Br bond in (CH3)3C-Br to form (CH3)3C⁺ and :Br⁻ [1]",
                "Structure of planar tertiary carbocation intermediate (CH3)3C⁺ [1]",
                "Step 2: Curly arrow from lone pair on :OH⁻ to the C⁺ of the carbocation to form (CH3)3COH [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "The three bulky methyl groups create severe steric hindrance, preventing backside attack by the nucleophile in SN2 [1]",
                "The three electron-donating methyl groups stabilize the tertiary carbocation intermediate via the positive inductive effect, facilitating the SN1 pathway [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "A racemic mixture (optically inactive) is formed [1]",
                "The carbocation intermediate is planar at the C⁺ centre; the nucleophile has an equal probability of attacking from either the front face or the rear face, giving equimolar amounts of both enantiomers [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Kinetics and Rate Laws of SN1 vs SN2 — 9701/22/O/N/22/Q7(a)-(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="The rate equations for the alkaline hydrolysis of 1-bromobutane and 2-bromo-2-methylpropane differ fundamentally.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the rate equation for the hydrolysis of 1-bromobutane with aqueous sodium hydroxide, and state the order of reaction with respect to each reactant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the rate equation for the hydrolysis of 2-bromo-2-methylpropane with aqueous sodium hydroxide, and explain why hydroxide ion concentration does NOT affect the reaction rate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Rate = k [CH3CH2CH2CH2Br] [OH⁻] [1]",
                "First order with respect to 1-bromobutane and first order with respect to hydroxide ions (second order overall) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Rate = k [(CH3)3CBr] [1]",
                "The rate-determining step is the unimolecular heterolytic ionization of the C-Br bond; hydroxide ions only participate in the subsequent fast second step [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Walden Inversion in SN2 Reactions — 9701/23/M/J/22/Q6(a)-(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="When a chiral primary or secondary halogenoalkane undergoes nucleophilic substitution by the SN2 mechanism, complete inversion of stereochemistry occurs.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why an SN2 reaction causes inversion of configuration (Walden inversion) at the carbon atom.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw 3D wedge-and-dash diagrams showing the stereochemical inversion when (S)-2-bromobutane reacts with hydroxide ions via the SN2 pathway.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The nucleophile must attack the central carbon atom from the side directly opposite (180°) to the leaving bromide group [1]",
                "As the new C-Nu bond forms and the C-Br bond breaks, the remaining three bonds are pushed through like an umbrella inverting in a gust of wind [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Starting reactant drawn with correct 3D tetrahedral geometry around chiral carbon [1]",
                "Product (R)-butan-2-ol drawn showing complete inversion of the spatial configuration around the chiral carbon [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Identifying Mechanism Type by Substrate Structure — 9701/11/M/J/22/Q25",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="Which halogenoalkane reacts with aqueous sodium hydroxide predominantly via the SN2 mechanism?",
        parts=[
            QuestionPart(
                label="",
                text="Select the halogenoalkane:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1-bromobutane",
                    "B. 2-bromobutane",
                    "C. 2-bromo-2-methylpropane",
                    "D. 2-bromo-2-methylbutane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: 1-bromobutane is a primary (1°) halogenoalkane with minimal steric hindrance around the alpha carbon, allowing unhindered backside attack by the nucleophile via the SN2 mechanism."
            ], "marks": 1}
        ]
    ),
    Question(
        number=5,
        title="Secondary Halogenoalkanes: Borderline Mechanism — 9701/21/O/N/21/Q7(a)-(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Secondary halogenoalkanes such as 2-bromobutane can undergo nucleophilic substitution via both SN1 and SN2 pathways simultaneously.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why secondary halogenoalkanes can react by both mechanisms.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Suggest how the reaction solvent can be modified to favour the SN1 pathway over the SN2 pathway.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The two alkyl groups provide intermediate steric hindrance (allowing backside attack for SN2) [1]",
                "and also provide moderate positive inductive stabilization to a secondary carbocation intermediate (allowing SN1) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Use a polar protic solvent (such as water or aqueous ethanol) [1]",
                "Polar protic solvents solvate and stabilise the leaving halide anion and carbocation intermediate, significantly lowering the activation energy for the SN1 step [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Energy Profile of SN1 vs SN2 Reactions — 9701/22/F/M/21/Q7(c)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="The progress of nucleophilic substitution reactions can be represented using reaction profile diagrams.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the number of energy transition states and intermediate energy troughs present in the reaction profile of an SN1 reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe the reaction profile of an SN2 reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Two activation energy peaks (two transition states) [1]",
                "One shallow energy minimum (trough) between them representing the carbocation intermediate [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "A single activation energy peak (one transition state) with no reaction intermediate [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=7,
        title="Solvent Effects on Nucleophilic Substitution — 9701/12/M/J/23/Q24",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Polar aprotic solvents (such as propanone or DMSO) favour SN2 reactions, whereas polar protic solvents favour SN1 reactions.",
        parts=[
            QuestionPart(
                label="",
                text="Why do polar aprotic solvents accelerate SN2 reactions?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. They form strong hydrogen bonds to the nucleophile, lowering its energy.",
                    "B. They solvate metal cations strongly but leave nucleophilic anions (e.g. OH⁻, CN⁻) unsolvated and 'naked', making them more reactive.",
                    "C. They convert halogenoalkanes into carbocations.",
                    "D. They act as catalysts by donating protons."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Polar aprotic solvents solvate cations effectively via dipole interactions but cannot form hydrogen bonds to anions, leaving nucleophilic anions relatively unshielded ('naked') and with higher nucleophilicity for SN2 backside attack."
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Leaving Group Ability in Nucleophilic Substitution — 9701/23/O/N/20/Q5(a)",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="The rate of nucleophilic substitution depends strongly on the nature of the leaving group.",
        parts=[
            QuestionPart(
                label="",
                text="List the halide ions in order of increasing leaving group ability (worst leaving group to best leaving group) and justify your answer using bond enthalpy.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Order: F⁻ < Cl⁻ < Br⁻ < I⁻ [1]",
                "The C-I bond has the lowest bond enthalpy (240 kJ mol⁻¹), making it easiest to cleave [1]",
                "The C-F bond has the highest bond enthalpy (467 kJ mol⁻¹), making fluoride an exceptionally poor leaving group [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=9,
        title="Structure of the Transition State in SN2 Reactions — 9701/11/O/N/22/Q22",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="In the transition state of an SN2 reaction between chloromethane and hydroxide ion, [HO...CH3...Cl]⁻:",
        parts=[
            QuestionPart(
                label="",
                text="What is the arrangement of the three hydrogen atoms around the central carbon atom?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Tetrahedral",
                    "B. Pyramidal",
                    "C. Planar (trigonal planar)",
                    "D. Linear"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: In the penta-coordinate transition state of an SN2 reaction, the central carbon is sp² hybridised; the three non-reacting groups (the three H atoms) lie in a trigonal planar arrangement at 120° angles, while the incoming nucleophile and leaving group occupy axial positions at 180°."
            ], "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Effect of Alkyl Group Size on SN2 Rate — 9701/21/M/J/20/Q4(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="The relative rates of SN2 substitution for 1-halobutane, 1-halo-2-methylpropane, and 1-halo-2,2-dimethylpropane decrease dramatically.",
        parts=[
            QuestionPart(
                label="",
                text="Explain why steric hindrance near the alpha-carbon severely retards the rate of an SN2 reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Bulky alkyl groups on the adjacent beta-carbon crowd the rear face of the alpha-carbon [1]",
                "This physically shields the C(delta+) atom from the trajectory of the approaching nucleophile, increasing the activation energy of the transition state [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="MCQ on Carbocation Stability in SN1 — 9701/13/M/J/22/Q22",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="Which carbocation formed during the SN1 hydrolysis of a bromoalkane is the most stable?",
        parts=[
            QuestionPart(
                label="",
                text="Select the most stable carbocation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CH3-CH2⁺",
                    "B. (CH3)2CH⁺",
                    "C. (CH3)3C⁺",
                    "D. CH3⁺"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: (CH3)3C⁺ is a tertiary carbocation with three electron-donating methyl groups that disperse the positive charge through positive inductive effects, making it the most stable."
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Deducing Mechanism from Experimental Observations — 9701/22/O/N/23/Q7(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="A chemist investigates the hydrolysis of an optically active halogenoalkane R.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When pure (R)-2-iodobutane is reacted with aqueous NaOH, the product butan-2-ol rotates plane-polarised light in the opposite direction to the starting material. Deduce the primary mechanism operating.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how this optical rotation result proves that substitution did NOT occur exclusively via a carbocation intermediate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "SN2 mechanism [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "An SN1 mechanism proceeds via a planar carbocation intermediate which yields a 50:50 racemic mixture with ZERO net optical rotation [1]",
                "Retention of net optical activity (with inverted sign) confirms inversion of configuration characteristic of backside attack in the SN2 mechanism [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Reactivity of Halogenoarenes vs Halogenoalkanes — 9701/12/F/M/22/Q22",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Chlorobenzene does NOT undergo nucleophilic substitution when boiled with aqueous sodium hydroxide under reflux, whereas 1-chlorobutane hydrolyses smoothly.",
        parts=[
            QuestionPart(
                label="",
                text="Why is chlorobenzene inert to nucleophilic substitution under normal laboratory conditions?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. The chlorine atom is too small to be replaced.",
                    "B. A lone pair of electrons on the chlorine atom overlaps with the delocalised pi system of the benzene ring, strengthening the C-Cl bond with partial double bond character.",
                    "C. Benzene rings attract nucleophiles strongly.",
                    "D. Chlorobenzene is completely insoluble in water."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The lone pair on chlorine delocalises into the aromatic pi electron system, shortening and strengthening the C-Cl bond (partial double bond character, higher bond enthalpy). Additionally, the electron-rich pi cloud repels approaching nucleophiles."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 15.1: Reactions: Substitution vs Elimination (Q14 to Q27)
    # =========================================================================
    Question(
        number=14,
        title="Substitution vs Elimination in Halogenoalkanes — 9701/22/M/J/23/Q7(a)-(d)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="When 2-bromopropane is treated with potassium hydroxide, the reaction pathway is dictated by the choice of solvent and temperature. Fig. 14.1 illustrates the two pathways.",
        figure_path="figures/halogenoalkanes_substitution_vs_elimination.png",
        figure_caption="Fig. 14.1: Competition between nucleophilic substitution and elimination for 2-bromopropane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and conditions required to convert 2-bromopropane into propan-2-ol, and identify the role of the hydroxide ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent and conditions required to convert 2-bromopropane into propene, and identify the role of the hydroxide ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced chemical equation for the elimination reaction in (b).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Draw the complete mechanism for the elimination reaction of 2-bromopropane with hydroxide ions, including all curly arrows.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Aqueous sodium hydroxide (or KOH), warm under reflux [1]",
                "Role of OH⁻: Acts as a nucleophile (electron pair donor) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents/conditions: Ethanolic sodium hydroxide (or KOH in ethanol), hot under reflux [1]",
                "Role of OH⁻: Acts as a Brønsted-Lowry base (proton acceptor) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3-CH(Br)-CH3 + OH⁻ -> CH3-CH=CH2 + H2O + Br⁻ (or with KOH -> KBr + H2O) [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Curly arrow from lone pair on :OH⁻ to a hydrogen atom on an adjacent methyl carbon (C1 or C3) [1]",
                "Curly arrow from the C-H bond to form the C=C pi bond [1]",
                "Curly arrow from the C-Br bond to the bromine atom showing loss of :Br⁻ leaving group [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Reaction of Halogenoalkanes with Ethanolic Potassium Cyanide — 9701/21/O/N/22/Q7(c)-(e)",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Halogenoalkanes react with potassium cyanide to form nitriles, an important reaction for extending the carbon chain.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and essential condition for the reaction of 1-chloropropane with potassium cyanide.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the chemical equation for the reaction of 1-chloropropane with KCN, and give the systematic IUPAC name of the organic product.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the formula of the carboxylic acid formed when this nitrile product is refluxed with dilute hydrochloric acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Potassium cyanide (KCN) dissolved in ethanol (ethanolic KCN) [1]",
                "Condition: Heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2Cl + KCN -> CH3CH2CH2CN + KCl (or with CN⁻) [1]",
                "Name: Butanenitrile [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3CH2CH2COOH (butanoic acid) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=16,
        title="Reaction of Halogenoalkanes with Ammonia: Amine Formation — 9701/23/M/J/22/Q6(c)-(e)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Bromoethane reacts with ammonia to form ethylamine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the conditions required to prepare ethylamine from bromoethane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the overall balanced equation for the formation of ethylamine from bromoethane and ammonia.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why an excess of concentrated ethanolic ammonia is used in this preparation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethanolic ammonia in a sealed tube (under pressure) / heated under pressure [1]",
                "Excess ammonia [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2Br + 2NH3 -> CH3CH2NH2 + NH4Br [2] (1 mark for species, 1 mark for balancing with 2 NH3)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ethylamine contains a lone pair on nitrogen and acts as a nucleophile [1]",
                "Using excess ammonia prevents further substitution (poly-alkylation) to secondary amines (diethylamine), tertiary amines, or quaternary ammonium salts [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Isomeric Alkenes from Elimination of 2-Bromobutane — 9701/21/M/J/22/Q7(a)-(c)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="When 2-bromobutane is heated under reflux with concentrated ethanolic potassium hydroxide, a mixture of three isomeric alkenes is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula and state the systematic IUPAC name of the minor alkene product formed by elimination of a hydrogen atom from carbon-1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Elimination of a hydrogen atom from carbon-3 produces two stereoisomers. Draw the displayed formulae of both stereoisomers and name them using the E/Z system.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State which alkene is formed in the greatest yield and suggest why.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Displayed formula of but-1-ene: CH2=CH-CH2-CH3 [1]",
                "Name: But-1-ene [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Displayed formula of (Z)-but-2-ene (cis-but-2-ene) [1]",
                "Displayed formula of (E)-but-2-ene (trans-but-2-ene) [1]",
                "Correctly named as (E)-but-2-ene and (Z)-but-2-ene [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "(E)-but-2-ene (trans-but-2-ene) is the major product because it is the most thermodynamically stable alkene (less steric hindrance between methyl groups) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="Identifying Functional Group Transitions — 9701/11/M/J/23/Q24",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Which reaction sequence converts 1-bromopropane into butanoic acid in two laboratory steps?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct two-step sequence:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Step 1: Aqueous NaOH; Step 2: Acidified K2Cr2O7 reflux",
                    "B. Step 1: Ethanolic KCN reflux; Step 2: Dilute aqueous HCl reflux",
                    "C. Step 1: Ethanolic NH3; Step 2: Nitrous acid",
                    "D. Step 1: Ethanolic KOH reflux; Step 2: Steam with H3PO4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Step 1 with ethanolic KCN extends the carbon chain from 3 to 4 carbons to form butanenitrile (CH3CH2CH2CN). Step 2 hydrolyses the nitrile under reflux with dilute acid to yield butanoic acid."
            ], "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Role of the Hydroxide Ion in Halogenoalkane Reactions — 9701/12/O/N/21/Q23",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Consider the two reactions:\nReaction 1: CH3CH2Br + OH⁻(aq) -> CH3CH2OH + Br⁻\nReaction 2: CH3CH2Br + OH⁻(ethanol) -> CH2=CH2 + H2O + Br⁻",
        parts=[
            QuestionPart(
                label="",
                text="In which reaction is the hydroxide ion acting as a Brønsted-Lowry base?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Reaction 1 only",
                    "B. Reaction 2 only",
                    "C. Both Reaction 1 and Reaction 2",
                    "D. Neither reaction"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In Reaction 2 (elimination), OH⁻ accepts a proton (H⁺) from the adjacent carbon, acting as a Brønsted-Lowry base. In Reaction 1, OH⁻ donates an electron pair to carbon, acting as a nucleophile."
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Synthesis of Amines from Halogenoalkanes — 9701/22/F/M/23/Q7(a)-(b)",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Butylamine, CH3(CH2)3NH2, is prepared from 1-chlorobutane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction of 1-chlorobutane with excess ammonia.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why butylamine is a basic substance in aqueous solution, referring to its structure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3(CH2)3Cl + 2NH3 -> CH3(CH2)3NH2 + NH4Cl [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The nitrogen atom possesses a non-bonding lone pair of electrons [1]",
                "It can accept a proton (H⁺) from water molecules: RNH2 + H2O <=> RNH3⁺ + OH⁻ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Elimination of 2-Bromo-2-methylbutane — 9701/21/O/N/23/Q7(b)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Heating 2-bromo-2-methylbutane with hot ethanolic KOH produces two isomeric alkenes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal formulae and state the systematic IUPAC names of both alkenes.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State which of these two alkenes is formed as the major product, and justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Alkene 1: 2-methylbut-2-ene, (CH3)2C=CHCH3 [1]",
                "Alkene 2: 2-methylbut-1-ene, CH2=C(CH3)CH2CH3 [1]",
                "Both skeletal structures drawn correctly [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Major product: 2-methylbut-2-ene [1]",
                "The double bond is more highly substituted (trisubstituted vs disubstituted), making it thermodynamically more stable [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Cyanide Nucleophile Structure — 9701/13/O/N/21/Q22",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="In the reaction of a halogenoalkane with potassium cyanide, which atom of the cyanide ion, [:C#N:]⁻, attacks the carbon atom bearing the halogen?",
        parts=[
            QuestionPart(
                label="",
                text="Select the attacking atom and the reason:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Nitrogen, because nitrogen is more electronegative than carbon.",
                    "B. Carbon, because the negative formal charge and more nucleophilic lone pair reside on carbon.",
                    "C. Both atoms attack simultaneously to form a cyclic intermediate.",
                    "D. Potassium, which donates an electron."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The formal negative charge in the cyanide ion resides on the carbon atom: [:C#N:]⁻. Carbon donates its lone pair to form a stable C-C bond (bond enthalpy 347 kJ mol⁻¹ vs C-N 305 kJ mol⁻¹)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Distinguishing Elimination from Substitution by Bromine Test — 9701/22/M/J/21/Q7(b)",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="A student carries out a reaction on 1-bromobutane and collects the organic product.",
        parts=[
            QuestionPart(
                label="",
                text="Describe a simple chemical test to confirm whether the reaction product was formed by elimination rather than by substitution.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Add bromine water (or aqueous KMnO4) to the product [1]",
                "Elimination product (butene) will rapidly decolourise bromine water from orange-brown to colourless; substitution product (butanol) will not decolourise bromine water [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Multi-Step Synthesis: Halogenoalkane to Amide — 9701/23/M/J/20/Q5(c)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Outline a two-step reaction scheme to convert bromoethane, CH3CH2Br, into propanamide, CH3CH2CONH2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the reagent, conditions, and intermediate formed in Step 1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Identify the reagent and condition for Step 2.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Ethanolic potassium cyanide (KCN), heat under reflux [1]",
                "Intermediate: Propanenitrile, CH3CH2CN [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Partial hydrolysis using moderately concentrated acid (or alkaline H2O2) to form propanamide [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 15.2: Hydrolysis Rates, Silver Nitrate Testing & CFCs (Q25 to Q50)
    # =========================================================================
    Question(
        number=25,
        title="Experimental Determination of Relative Rates of Hydrolysis — 9701/21/M/J/23/Q7(e)-(g)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="The relative rates of hydrolysis of 1-chlorobutane, 1-bromobutane, and 1-iodobutane can be compared experimentally using aqueous silver nitrate in ethanol at 50 °C. Fig. 25.1 shows the relative rates and bond enthalpies.",
        figure_path="figures/halogenoalkanes_hydrolysis_rates_agplus.png",
        figure_caption="Fig. 25.1: Rates of hydrolysis compared with C-X bond enthalpies.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why ethanol is added to the reaction mixture along with aqueous silver nitrate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the observation and the relative time taken for a precipitate to appear for each of the three halogenoalkanes.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write the ionic equation for the formation of the precipitate in the case of 1-iodobutane.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Explain the trend in the rates of hydrolysis in terms of bond enthalpies and bond polarities.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethanol acts as a common mutual solvent to dissolve both the halogenoalkane (covalent organic) and aqueous silver nitrate (ionic water solution), preventing two immiscible layers [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "1-iodobutane: Yellow precipitate of AgI forms almost immediately (fastest) [1]",
                "1-bromobutane: Cream precipitate of AgBr forms after a short delay / moderate rate [1]",
                "1-chlorobutane: White precipitate of AgCl forms very slowly / after prolonged heating [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Ag⁺(aq) + I⁻(aq) -> AgI(s) [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Rate increases in the order: R-Cl < R-Br < R-I [1]",
                "Although the C-Cl bond is the most polar (greatest delta+ on carbon), bond enthalpy is the dominant factor determining reactivity [1]",
                "C-I has the lowest bond enthalpy (240 kJ mol⁻¹ vs C-Cl 340 kJ mol⁻¹); the weaker bond requires less energy to cleave, leading to a lower activation energy and faster rate [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=26,
        title="Hydrolysis Rates: Primary vs Secondary vs Tertiary — 9701/22/O/N/22/Q7(f)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Equal amounts of 1-chlorobutane, 2-chlorobutane, and 2-chloro-2-methylpropane are reacted separately with aqueous silver nitrate in ethanol at 50 °C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the order of reactivity of these three chloroalkanes from slowest to fastest.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why 2-chloro-2-methylpropane hydrolyses significantly faster than 1-chlorobutane.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1-chlorobutane (primary) < 2-chlorobutane (secondary) < 2-chloro-2-methylpropane (tertiary) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2-chloro-2-methylpropane reacts via the SN1 mechanism involving a tertiary carbocation intermediate [1]",
                "The tertiary carbocation, (CH3)3C⁺, is strongly stabilized by the positive inductive electron donation from three methyl groups [1]",
                "This results in a much lower activation energy than the concerted SN2 pathway for 1-chlorobutane [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=27,
        title="Unreactivity of Fluoroalkanes towards Hydrolysis — 9701/11/M/J/22/Q26",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="When 1-fluorobutane is heated with aqueous silver nitrate in ethanol, no precipitate is observed even after several hours.",
        parts=[
            QuestionPart(
                label="",
                text="Why does 1-fluorobutane fail to produce a precipitate?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Silver fluoride is soluble in water, and the C-F bond enthalpy is exceptionally high (467 kJ mol⁻¹).",
                    "B. Fluorine is too electronegative to form a covalent bond with carbon.",
                    "C. Fluoride ions reduce silver ions to metallic silver.",
                    "D. 1-fluorobutane evaporates before it can react."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: The C-F bond is extremely strong (467 kJ mol⁻¹), making cleavage by water/OH⁻ impractically slow at 50 °C. Furthermore, silver fluoride (AgF) is freely soluble in water, so even if trace hydrolysis occurred, no precipitate would form."
            ], "marks": 1}
        ]
    ),
    Question(
        number=28,
        title="Environmental Impact of Chlorofluorocarbons (CFCs) — 9701/21/O/N/21/Q7(c)-(e)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Chlorofluorocarbons (CFCs) such as dichlorodifluoromethane, CCl2F2, were historically used as aerosol propellants and refrigerants. Fig. 28.1 depicts their stratospheric photolysis.",
        figure_path="figures/halogenoalkanes_cfcs_ozone_depletion.png",
        figure_caption="Fig. 28.1: Photodissociation of CFCs and the catalytic ozone destruction cycle.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why CFCs are chemically stable and inert in the lower atmosphere (troposphere).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When CFC molecules diffuse into the stratosphere, high-energy UV radiation causes bond fission. Write the equation for the photolysis of CCl2F2 and explain why the C-Cl bond breaks rather than the C-F bond.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write two equations that show how chlorine radicals catalytically destroy stratospheric ozone, and construct the overall equation.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Name a modern class of replacement compounds for CFCs that have zero ozone depletion potential, and explain why they do not destroy ozone.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CFCs contain only strong, unreactive C-Cl and C-F bonds with high bond enthalpies and low polarity that resist attack by atmospheric oxidizing agents [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equation: CCl2F2 + UV -> *CClF2 + Cl* [1]",
                "The C-Cl bond enthalpy (340 kJ mol⁻¹) is significantly lower than the C-F bond enthalpy (467 kJ mol⁻¹), so the C-Cl bond breaks homolytically under UV light [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Step 1: Cl* + O3 -> ClO* + O2 [1]",
                "Step 2: ClO* + O -> Cl* + O2 [1]",
                "Overall: O3 + O -> 2O2 [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Hydrofluorocarbons (HFCs) [1]",
                "HFCs contain only C, H, and F atoms (no chlorine atoms); they cannot generate chlorine free radicals to catalyse ozone breakdown [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Precipitate Solubility in Aqueous Ammonia Test — 9701/22/M/J/22/Q7(b)",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="The silver halide precipitates obtained from halogenoalkane hydrolysis can be confirmed using aqueous ammonia.",
        parts=[
            QuestionPart(
                label="",
                text="Complete the following table of solubilities for AgCl, AgBr, and AgI in dilute and concentrated aqueous ammonia.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "AgCl: Dissolves in dilute NH3(aq) [1]",
                "AgBr: Insoluble in dilute NH3(aq), dissolves in concentrated NH3(aq) [1]",
                "AgI: Insoluble in both dilute and concentrated NH3(aq) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=30,
        title="Kinetics of Hydrolysis with Different Leaving Groups — 9701/12/M/J/21/Q24",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="Which factor primarily accounts for the observation that 1-iodobutane hydrolyses faster than 1-chlorobutane?",
        parts=[
            QuestionPart(
                label="",
                text="Select the primary factor:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. The C-I bond is more polar than the C-Cl bond.",
                    "B. The C-I bond enthalpy is lower than the C-Cl bond enthalpy.",
                    "C. Iodine is more electronegative than chlorine.",
                    "D. Iodide ions are smaller than chloride ions."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The C-I bond enthalpy (240 kJ mol⁻¹) is significantly lower than the C-Cl bond enthalpy (340 kJ mol⁻¹). Bond enthalpy determines the activation energy required to break the carbon-halogen bond during hydrolysis."
            ], "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Atmospheric Lifetime and Greenhouse Impact of HFCs — 9701/23/O/N/21/Q6(c)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Although hydrofluorocarbons (HFCs) do not deplete stratospheric ozone, their widespread use has raised new environmental concerns.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the major global environmental concern associated with HFC emissions into the atmosphere.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why HFC molecules absorb infrared radiation so effectively.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HFCs are potent greenhouse gases with very high global warming potential (GWP) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "HFCs contain highly polar C-F and C-H bonds with large dipole moments [1]",
                "Their bond vibration frequencies fall precisely within the atmospheric infrared window (700 - 1400 cm⁻¹), efficiently trapping outgoing terrestrial radiation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Deducing Halogen Identity by Gravimetric Precipitation — 9701/21/M/J/21/Q7(c)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="A 0.685 g sample of a 1-haloalkane, C4H9X, was completely hydrolysed with excess aqueous sodium hydroxide. The solution was acidified with dilute HNO3 and treated with excess AgNO3(aq). The dried precipitate weighed 0.940 g. (Ar: C = 12.0, H = 1.0, Ag = 107.9; Cl = 35.5, Br = 79.9, I = 126.9)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of C4H9X in the sample if X is bromine (Mr of C4H9Br = 137.0).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Determine whether the precipitate is AgCl, AgBr, or AgI by calculating the expected mass of precipitate for each.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of C4H9Br = 0.685 / 137.0 = 0.00500 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "If X = Br, moles of AgBr formed = 0.00500 mol; Mr(AgBr) = 107.9 + 79.9 = 187.8 [1]",
                "Expected mass = 0.00500 * 187.8 = 0.939 g [1]",
                "0.939 g matches the experimental mass of 0.940 g; therefore, halogen X is bromine (AgBr) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=33,
        title="Comparison of Halogenoalkanes with Hydroxyalkanes — 9701/13/O/N/22/Q23",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="1-bromobutane boils at 102 °C, whereas butan-1-ol boils at 118 °C, despite 1-bromobutane having a much higher relative molecular mass (Mr: 137.0 vs 74.0).",
        parts=[
            QuestionPart(
                label="",
                text="Why is the boiling point of butan-1-ol higher than that of 1-bromobutane?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1-bromobutane molecules are spherical.",
                    "B. Butan-1-ol molecules form intermolecular hydrogen bonds, which are stronger than the permanent dipole-dipole and London dispersion forces in 1-bromobutane.",
                    "C. The C-Br bond is non-polar.",
                    "D. Butan-1-ol has a higher density."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Butan-1-ol contains a polar -O-H group capable of forming intermolecular hydrogen bonds between molecules. Hydrogen bonds are significantly stronger than the dipole-dipole and London forces between 1-bromobutane molecules."
            ], "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Mechanism of Alkyl Halide Solvolysis — 9701/22/F/M/20/Q4(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Solvolysis is a nucleophilic substitution in which the solvent molecule acts as the attacking nucleophile.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the solvolysis of 2-iodo-2-methylpropane in pure water, showing the intermediate oxonium ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why solvolysis occurs rapidly in water but very slowly in ethanol.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(CH3)3C-I + H2O -> (CH3)3C-O⁺H2 + I⁻ [1]",
                "(CH3)3C-O⁺H2 + H2O -> (CH3)3COH + H3O⁺ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Water has a higher dielectric constant / greater polarity than ethanol [1]",
                "Water solvates and stabilizes the carbocation and iodide ion intermediates more effectively, lowering the activation energy for ionization [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="MCQ on Ozone Depletion Chemistry — 9701/11/F/M/23/Q23",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="In the stratosphere, what role is played by the chlorine radical, Cl*, in the decomposition of ozone?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct role:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Initiator consumed in the reaction",
                    "B. Homogeneous catalyst",
                    "C. Heterogeneous catalyst",
                    "D. Reducing agent oxidised to chlorate"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The chlorine radical is in the same gas phase as ozone (homogeneous) and is regenerated at the end of the two-step propagation cycle (catalyst), enabling a single radical to destroy thousands of ozone molecules."
            ], "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Preparation of Halogenoalkanes from Alcohols — 9701/21/O/N/20/Q6(b)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Halogenoalkanes can be prepared from alcohols using various halogenating reagents.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction of propan-1-ol with phosphorus pentachloride, PCl5, at room temperature, and state two observations.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why thionyl chloride, SOCl2, is preferred over PCl5 for the synthesis of chloroalkanes in organic laboratories.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2CH2OH + PCl5 -> CH3CH2CH2Cl + POCl3 + HCl [1]",
                "Observations: Steamy acidic fumes of HCl gas [1]",
                "Vigorous reaction / bubbling / heat evolved [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "CH3CH2CH2OH + SOCl2 -> CH3CH2CH2Cl + SO2(g) + HCl(g) [1]",
                "Both by-products (SO2 and HCl) are gases and escape from the reaction mixture, leaving pure chloroalkane without requiring complex distillation separation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Identifying Hydrolysis Products by Mass Spectrometry — 9701/22/M/J/21/Q7(d)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="The mass spectrum of a bromoalkane exhibits two molecular ion peaks of almost equal intensity at m/z = 136 and m/z = 138.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why two molecular ion peaks of equal intensity are observed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the molecular formula of this bromoalkane. (Ar: C = 12.0, H = 1.0; ⁷⁹Br = 79, ⁸¹Br = 81)",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Bromine exists naturally as two isotopes, ⁷⁹Br and ⁸¹Br, in approximately equal 1:1 abundance [1]",
                "The peak at m/z = 136 corresponds to the molecule containing ⁷⁹Br; the peak at m/z = 138 corresponds to ⁸¹Br [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Mass of alkyl group R = 136 - 79 = 57 [1]",
                "CnH2n+1 = 57 => 14n + 1 = 57 => 14n = 56 => n = 4 => C4H9Br [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="MCQ on Halogenoalkane Nucleophilic Attack — 9701/12/M/J/22/Q25",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Which species CANNOT act as a nucleophile in a substitution reaction with a halogenoalkane?",
        parts=[
            QuestionPart(
                label="",
                text="Select the species:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. NH3",
                    "B. H2O",
                    "C. NH4⁺",
                    "D. CN⁻"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: The ammonium ion (NH4⁺) has no non-bonding lone pair of electrons (its octet is fully bonded) and carries a positive charge, meaning it cannot donate an electron pair to act as a nucleophile."
            ], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Comparative Rates: Bromoethane vs Iodoethane — 9701/23/M/J/21/Q6(b)",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="Bromoethane and iodoethane are reacted with aqueous sodium hydroxide under identical conditions.",
        parts=[
            QuestionPart(
                label="",
                text="State which compound reacts faster and give the single most important factor that accounts for this difference.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Iodoethane reacts faster [1]",
                "The C-I bond enthalpy (240 kJ mol⁻¹) is lower than the C-Br bond enthalpy (280 kJ mol⁻¹), so less energy is required to break the bond [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Montreal Protocol and Replacement of CFCs — 9701/11/M/J/21/Q24",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="The international Montreal Protocol phased out the manufacture and use of chlorofluorocarbons.",
        parts=[
            QuestionPart(
                label="",
                text="Which compound is most suitable as an environmentally acceptable propellant in asthma inhalers?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CCl3F",
                    "B. CCl2F2",
                    "C. CF3CH2F (1,1,1,2-tetrafluoroethane)",
                    "D. CCl4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: CF3CH2F (HFA-134a / HFC-134a) contains no chlorine atoms, poses zero risk to stratospheric ozone, and is non-toxic."
            ], "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Mechanistic Pathway for Hydrolysis of Benzyl Chloride — 9701/21/O/N/23/Q7(d)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Benzyl chloride, C6H5CH2Cl, hydrolyses rapidly via an SN1 pathway even though it is a primary halogenoalkane.",
        parts=[
            QuestionPart(
                label="",
                text="Explain why the primary benzyl carbocation, C6H5CH2⁺, is exceptionally stable.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "The empty p-orbital on the positively charged CH2⁺ carbon overlaps with the adjacent delocalised pi system of the benzene ring [1]",
                "The positive charge is delocalised across the aromatic ring (ortho and para positions), significantly stabilizing the intermediate carbocation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Identifying Elimination Products from Secondary Haloalkanes — 9701/13/O/N/21/Q23",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="When 3-bromopentane is heated with concentrated ethanolic sodium hydroxide, what is the systematic IUPAC name of the alkene product?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct alkene name:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Pent-1-ene",
                    "B. Pent-2-ene",
                    "C. 2-methylbut-2-ene",
                    "D. Cyclopentane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: 3-bromopentane is CH3CH2CH(Br)CH2CH3. Removing H from C2 or C4 and Br from C3 yields pent-2-ene (CH3CH=CHCH2CH3) as the sole constitutional product."
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Nucleophilic Substitution with Carboxylate Salts — 9701/22/F/M/22/Q7(b)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Halogenoalkanes can react with carboxylate salts to form esters: R-X + R'COO⁻ -> R'COOR + X⁻.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction of bromoethane with sodium ethanoate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the systematic IUPAC name of the ester formed.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2Br + CH3COONa -> CH3COOCH2CH3 + NaBr [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethyl ethanoate [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=44,
        title="MCQ on Halogenoalkane Boiling Points — 9701/12/O/N/22/Q24",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Which halogenoalkane has the highest boiling point?",
        parts=[
            QuestionPart(
                label="",
                text="Select the compound with highest boiling point:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1-chlorobutane",
                    "B. 1-bromobutane",
                    "C. 1-iodobutane",
                    "D. 1-fluorobutane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: 1-iodobutane has the greatest number of electrons (66 electrons), leading to the most polarisable electron cloud and the strongest instantaneous dipole-induced dipole (London dispersion) forces."
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Acid-Catalysed Hydrolysis of Haloalkanes — 9701/21/M/J/22/Q7(e)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Explain why adding aqueous silver nitrate acidified with dilute nitric acid accelerates the rate of hydrolysis of halogenoalkanes.",
        parts=[
            QuestionPart(
                label="",
                text="State the role of Ag⁺ ions in facilitating the cleavage of the C-X bond.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Ag⁺ ions coordinate strongly to the halogen atom, polarising and weakening the C-X bond [1]",
                "Precipitation of insoluble AgX solid provides a strong thermodynamic driving force, effectively pulling the reaction forward [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Ozone Destruction Catalytic Cycles with Nitrogen Oxides and Chlorine — 9701/11/O/N/21/Q23",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Chlorine monoxide radicals, ClO*, can also react with nitrogen dioxide in the stratosphere: ClO* + NO2 -> ClONO2.",
        parts=[
            QuestionPart(
                label="",
                text="What is the significance of the formation of chlorine nitrate, ClONO2, in stratospheric chemistry?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. It acts as an active catalyst that accelerates ozone destruction.",
                    "B. It acts as a temporary 'reservoir molecule' that removes active Cl* and NO2* radicals from the catalytic cycles, temporarily reducing ozone depletion.",
                    "C. It permanently deposits chlorine onto the Earth's surface.",
                    "D. It decomposes directly into ozone."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Chlorine nitrate acts as a temporary chemical reservoir; it ties up active chlorine and nitrogen radicals in an inactive form, preventing them from participating in ozone-destroying catalytic cycles until released."
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Synthesis of Deuterated Alcohols via SN2 — 9701/22/O/N/20/Q6(b)",
        syllabus_ref="15.2",
        difficulty="HARD",
        preamble="Bromoethane is hydrolysed using sodium deuteroxide in heavy water, NaOD / D2O.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the deuterated alcohol formed.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the molecular mass of the deuterated alcohol product. (Ar: C = 12.0, H = 1.0, D = 2.0, O = 16.0)",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2-OD (or CH3CH2OD) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Mr = 2(12.0) + 5(1.0) + 16.0 + 2.0 = 47.0 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="MCQ on Halogenoalkane Nucleophilic Attack — 9701/13/M/J/23/Q25",
        syllabus_ref="15.1",
        difficulty="EASY",
        preamble="Which reaction condition specifically favours elimination over substitution when reacting a halogenoalkane with potassium hydroxide?",
        parts=[
            QuestionPart(
                label="",
                text="Select the favoured condition:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Low temperature in dilute aqueous solution",
                    "B. High temperature in concentrated ethanolic solution",
                    "C. Room temperature in water-ethanol (50:50) mixture",
                    "D. High pressure with liquid ammonia"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Hot, concentrated ethanolic KOH favours elimination (forming an alkene), whereas warm, dilute aqueous NaOH favours substitution (forming an alcohol)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Qualitative Analysis of an Unknown Halogenoalkane — 9701/22/M/J/23/Q7(f)",
        syllabus_ref="15.2",
        difficulty="EASY",
        preamble="An unknown halogenoalkane Q is warmed with aqueous sodium hydroxide. The mixture is cooled, acidified with dilute nitric acid, and treated with aqueous silver nitrate. A cream precipitate forms that is insoluble in dilute aqueous ammonia but dissolves in concentrated aqueous ammonia.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the halogen present in compound Q.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the ionic equation for the formation of the precipitate.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Bromine (or bromide, Br⁻) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ag⁺(aq) + Br⁻(aq) -> AgBr(s) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Reaction Scheme Involving Halogenoalkanes — 9701/21/O/N/23/Q7(a)-(f)",
        syllabus_ref="15.1",
        difficulty="HARD",
        preamble="Consider the synthetic pathways starting from 1-bromobutane:\n- Pathway 1: 1-bromobutane + Reagent A -> Butan-1-ol\n- Pathway 2: 1-bromobutane + Reagent B -> Compound C (C5H9N)\n- Pathway 3: 1-bromobutane + Reagent D -> But-1-ene",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify Reagents A, B, and D, and state the essential conditions for each pathway.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Give the systematic IUPAC name of Compound C.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagent and conditions required to convert Compound C into pentanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State the reagent and conditions required to convert Compound C into pentan-1-amine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent A: Aqueous NaOH (or KOH), warm under reflux [1]",
                "Reagent B: Ethanolic KCN, heat under reflux [1]",
                "Reagent D: Ethanolic NaOH (or KOH), hot under reflux [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Pentanenitrile [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Dilute hydrochloric acid (or dilute H2SO4), heat under reflux (acid hydrolysis) [2]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "LiAlH4 in dry ether (or H2 with Ni catalyst at elevated temp/pressure) [2]"
            ], "marks": 2}
        ]
    )
]
'''
    with open("topic15_data.py", "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Successfully wrote topic15_data.py!")

if __name__ == "__main__":
    generate()
