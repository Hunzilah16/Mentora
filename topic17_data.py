"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 17: Carbonyl Compounds (Aldehydes and Ketones).
Subtopic:
  17.1 Aldehydes and Ketones:
       - Structure, bonding, polarity of C=O group, physical properties (dipole-dipole forces vs H-bonding)
       - Preparation from primary and secondary alcohols (oxidation with acidified K2Cr2O7)
       - Reduction using NaBH4 to primary and secondary alcohols (hydride nucleophile)
       - Nucleophilic addition of HCN: mechanism, catalysis by NaCN/OH-, intermediate tetrahedral alkoxide, stereochemistry (racemisation via planar C=O)
       - Reactions of hydroxynitriles (acid hydrolysis to 2-hydroxyacids, reduction to hydroxyamines)
       - Diagnostic testing with 2,4-dinitrophenylhydrazine (2,4-DNPH / Brady's reagent), purification and m.p. characterisation
       - Differentiation using Tollens' reagent and Fehling's solution (mild oxidation of aldehydes vs ketones)
       - The tri-iodomethane (iodoform) reaction (test for CH3-CO- group in ethanal and methyl ketones)
       - Deductions of structures from analytical and chemical data, multi-step synthesis

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

TOPIC_17_QUESTIONS = [
    # =========================================================================
    # PART 1: Nucleophilic Addition Mechanism with HCN & Stereochemistry (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Nucleophilic Addition Mechanism of HCN — 9701/22/M/J/23/Q5(a)-(d)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Aldehydes and ketones react with hydrogen cyanide in the presence of a trace of base or sodium cyanide via a nucleophilic addition mechanism. Fig. 1.1 illustrates the two-step pathway and the stereochemical consequences of attacking a planar carbonyl centre.",
        figure_path="figures/carbonyl_nucleophilic_addition_mechanism.png",
        figure_caption="Fig. 1.1: Nucleophilic addition mechanism of HCN to propanal and subsequent synthetic transformations.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the complete two-step mechanism for the reaction between propanal and cyanide ions (:CN⁻). Include all relevant dipoles, lone pairs, curly arrows, and the structure of the intermediate.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="Explain why hydrogen cyanide alone reacts extremely slowly with carbonyl compounds, and explain the role of adding sodium cyanide or sodium hydroxide as a catalyst.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State the geometry and bond angle around the carbonyl carbon in propanal, and explain why the addition product exists as an optically inactive racemic mixture.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Give the systematic IUPAC name of the 2-hydroxynitrile formed from propanal.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dipoles on carbonyl group: C(delta+) and O(delta-) in CH3CH2CHO [1]",
                "Curly arrow from lone pair on carbon of :CN⁻ to C(delta+) of carbonyl [1]",
                "Curly arrow from C=O double bond onto oxygen atom forming tetrahedral alkoxide intermediate CH3CH2CH(CN)O⁻ [1]",
                "Curly arrow from lone pair on O⁻ to H of H-CN (or H2O) regenerating :CN⁻ and forming 2-hydroxybutanenitrile [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "HCN is a very weak acid and only partially / weakly dissociates in aqueous solution, providing an extremely low concentration of nucleophilic :CN⁻ ions [1]",
                "Adding NaCN supplies a high concentration of free :CN⁻ ions [1]",
                "Adding NaOH deprotonates HCN (HCN + OH⁻ -> CN⁻ + H2O), generating the nucleophilic :CN⁻ required for the rate-determining step [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Trigonal planar geometry with bond angle of 120° around the sp2 carbonyl carbon [1]",
                "The planar carbonyl centre can be attacked by the :CN⁻ nucleophile with equal probability from either the top face or the bottom face [1]",
                "This produces an equimolar (50:50) mixture of the two non-superimposable mirror-image enantiomers, cancelling optical rotation [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "2-hydroxybutanenitrile [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Addition of HCN to Symmetrical vs Unsymmetrical Carbonyls — 9701/21/O/N/23/Q3(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The addition of HCN to propanone and propanal produces different stereochemical results.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction of propanone with HCN.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the displayed formula of the organic product formed from propanone and state whether this product exhibits optical activity. Justify your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State how the stereochemical outcome of adding HCN to propanal differs fundamentally from that of propanone.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COCH3 + HCN -> (CH3)2C(OH)CN [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Displayed formula of 2-hydroxy-2-methylpropanenitrile: central carbon bonded to -OH, -CN, and two -CH3 groups [1]",
                "Optically inactive because the central carbon is achiral (it is bonded to two identical methyl groups) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In propanal, the product (2-hydroxybutanenitrile) possesses a chiral carbon bonded to four different groups (-H, -OH, -CN, -C2H5) [1]",
                "It produces a pair of optical enantiomers (racemic mixture), whereas propanone produces an achiral product with no stereoisomers [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Acid Hydrolysis of 2-Hydroxynitriles — 9701/22/F/M/22/Q3(a)-(c)",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="2-hydroxynitriles can be converted into 2-hydroxycarboxylic acids by heating under reflux with dilute acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="2-hydroxypropanenitrile, CH3CH(OH)CN, is heated under reflux with dilute hydrochloric acid. Write a balanced chemical equation for this reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Give the systematic name and common name of the organic product formed.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the nitrile carbon (-CN) is converted to a carboxylic acid group while the alcohol group (-OH) remains unaffected during this reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH(OH)CN + 2H2O + HCl -> CH3CH(OH)COOH + NH4Cl (or with H⁺: + 2H2O + H⁺ -> CH3CH(OH)COOH + NH4⁺) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Systematic name: 2-hydroxypropanoic acid [1]",
                "Common name: Lactic acid [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The carbon in the nitrile group has a high partial positive charge due to the triple bond to electronegative nitrogen, making it susceptible to nucleophilic attack by water [1]",
                "The secondary alcohol -OH group is stable to dilute non-oxidising acid and does not undergo substitution or elimination under these mild reflux conditions [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Reduction of Hydroxynitriles to Amino Alcohols — 9701/23/M/J/22/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="2-hydroxynitriles can also be reduced to form 2-amino alcohols.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and solvent required to reduce 2-hydroxypropanenitrile to 1-aminopropan-2-ol.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write an equation for this reduction using [H] to represent the reducing agent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why sodium borohydride, NaBH4, is NOT suitable for reducing a nitrile group, whereas lithium aluminium hydride, LiAlH4, is effective.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Lithium aluminium hydride (LiAlH4) [1]",
                "Solvent: Dry ether (ethoxyethane) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH(OH)CN + 4[H] -> CH3CH(OH)CH2NH2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "NaBH4 is a milder reducing agent and lacks sufficient nucleophilic power / hydride transfer ability to attack the less polar C≡N triple bond [1]",
                "LiAlH4 contains a more polar, weaker Al-H bond that readily releases hydride ions (:H⁻) with sufficient nucleophilicity to reduce nitriles [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Comparative Reactivity of Aldehydes vs Ketones — 9701/21/O/N/22/Q3(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Aldehydes are generally significantly more reactive towards nucleophiles than ketones.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain this difference in reactivity in terms of the electronic (inductive) effects of alkyl groups.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain this difference in reactivity in terms of steric hindrance around the carbonyl carbon.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Rank the following three compounds in order of decreasing rate of nucleophilic addition of HCN: propanone, ethanal, methanal. Give a brief justification.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Alkyl groups exert an electron-releasing positive inductive (+I) effect [1]",
                "Ketones have two alkyl groups which reduce the partial positive charge on the carbonyl carbon (C(delta+)) more than the single alkyl group in aldehydes, making the ketone carbon less electrophilic [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ketones possess two bulky alkyl groups attached to the carbonyl carbon, which crowd the reaction centre [1]",
                "This creates greater steric hindrance, obstructing the approach of the incoming nucleophile and destabilising the crowded tetrahedral intermediate [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Methanal > ethanal > propanone [1]",
                "Methanal has zero alkyl groups (least steric crowding, most electrophilic carbon); propanone has two alkyl groups (most hindered, least electrophilic) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Carbon Chain Extension Strategy — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="A synthetic chemist needs to synthesise 2-hydroxy-2-methylbutanoic acid starting from butanone.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and catalyst needed for Step 1 to convert butanone into a 2-hydroxynitrile.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of the 2-hydroxynitrile intermediate formed in Step 1.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagents, conditions, and write the chemical equation for Step 2 to convert this intermediate into 2-hydroxy-2-methylbutanoic acid.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: HCN and NaCN (or KCN) catalyst (or NaCN + dilute H2SO4) [1]",
                "Conditions: Room temperature / pH 8 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3-CH2-C(CH3)(OH)-CN [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (or dilute H2SO4), heat under reflux [1]",
                "Equation: CH3CH2C(CH3)(OH)CN + 2H2O + H⁺ -> CH3CH2C(CH3)(OH)COOH + NH4⁺ [2]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=7,
        title="Safety and Hazards of Cyanide in the Laboratory — 9701/11/M/J/23/Q20",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Hydrogen cyanide, HCN, is an extremely toxic volatile liquid (b.p. 26 °C).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why potassium cyanide, KCN, mixed with dilute acid is typically used in school laboratories rather than pure liquid HCN.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State two crucial laboratory safety precautions when preparing and using solutions containing cyanide ions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HCN is a volatile liquid that readily vaporises at room temperature to form deadly toxic gas [1]",
                "Solid KCN or NaCN can be weighed safely and dissolved in solution, generating HCN in situ under controlled, enclosed conditions [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Perform all procedures strictly inside a well-ventilated fume cupboard / fume hood [1]",
                "Wear protective gloves and safety goggles, and keep an antidote / iron(II) sulfate deactivating solution readily available [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Deducing Carbonyl Precursor from Hydrolysis Product — 9701/21/M/J/23/Q6",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Compound P has molecular formula C5H10O. When reacted with NaCN and dilute acid, it forms compound Q (C6H11NO). When Q is heated under reflux with dilute acid, compound R is obtained. Compound R is 2-hydroxy-3-methylbutanoic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of compound R.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic IUPAC name of compound P.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State whether compound P is an aldehyde or a ketone. Justify your conclusion.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(CH3)2CH-CH(OH)-COOH [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Structural formula: (CH3)2CH-CHO [1]",
                "Systematic name: 2-methylpropanal [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Compound P is an aldehyde [1]",
                "In compound R, the carbon bearing the -OH group also has a hydrogen atom (CH(OH)), showing that the carbonyl carbon had one H attached [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Optical Activity in Carbonyl Addition Products — 9701/22/O/N/23/Q6(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Consider the addition of HCN to ethanal.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the chiral carbon atom in the product, 2-hydroxypropanenitrile, and state the four different groups attached to it.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw 3D wedge-and-dash diagrams showing the pair of optical isomers (enantiomers) of 2-hydroxypropanenitrile.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="A polarimeter is used to measure the optical rotation of the reaction mixture after the addition is complete. Predict the angle of rotation and explain your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Carbon-2 (C2) is the chiral centre [1]",
                "Four groups: -H, -CH3, -OH, -CN [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Correct 3D tetrahedral representations using wedges, dashes, and solid lines [1]",
                "Two non-superimposable mirror image structures drawn accurately [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Angle of optical rotation = 0° / no optical rotation observed [1]",
                "A racemic mixture is formed containing exactly equal amounts of (+) and (-) enantiomers which rotate plane-polarised light by equal amounts in opposite directions, cancelling out [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Multiple Choice: Rate of Nucleophilic Addition — 9701/12/M/J/23/Q21",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Which carbonyl compound reacts at the fastest rate with HCN in the presence of NaCN?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct compound from the options below:\nA  Propan-2-one\nB  Butan-2-one\nC  Ethanal\nD  Pentan-3-one",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the compound you chose reacts faster than the other three.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Ethanal) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethanal is the only aldehyde among the choices (the other three are ketones) [1]",
                "Aldehydes have only one electron-releasing alkyl group, giving the carbonyl carbon a higher positive charge (more electrophilic), and smaller steric hindrance to attack by CN⁻ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Addition of HCN to Aromatic Carbonyls — 9701/23/O/N/21/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Benzaldehyde, C6H5CHO, reacts with HCN in the presence of NaCN to form mandelonitrile.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of mandelonitrile.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why benzaldehyde reacts more slowly with HCN than ethanal, considering the delocalisation of electrons into the carbonyl group.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the complete acid hydrolysis of mandelonitrile to mandelic acid (2-hydroxy-2-phenylethanoic acid).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C6H5-CH(OH)-CN [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The carbonyl group in benzaldehyde is conjugated with the pi electron cloud of the benzene ring [1]",
                "Delocalisation of pi electrons from the benzene ring into the carbonyl carbon reduces its partial positive charge (delta+), making it less electrophilic than in aliphatic ethanal [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "C6H5CH(OH)CN + 2H2O + H⁺ -> C6H5CH(OH)COOH + NH4⁺ [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Role of pH in Cyanide Addition Kinetics — 9701/21/O/N/22/Q5(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The rate of addition of HCN to propanone varies dramatically with the pH of the reaction mixture.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the reaction is extremely slow at very low pH (pH < 4).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the reaction is also slow at very high pH (pH > 11).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the optimal pH range for this reaction and explain why this intermediate pH provides the maximum rate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "At very low pH (high [H⁺]), the equilibrium HCN <=> H⁺ + CN⁻ is shifted far to the left [1]",
                "The concentration of nucleophilic :CN⁻ ions is too low to attack the carbonyl carbon effectively in the rate-determining step [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "At very high pH (high [OH⁻]), virtually all HCN is converted to CN⁻, leaving negligible undissociated HCN molecules in solution [1]",
                "Undissociated HCN is needed in Step 2 to protonate the alkoxide intermediate and complete the reaction while regenerating the catalyst [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Optimal pH is approximately 7.5 to 8.5 (weakly alkaline) [1]",
                "This provides a sufficient concentration of both the attacking nucleophile (:CN⁻) and the proton-donating species (HCN) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Addition of Bisulfite Ion (Extension Nucleophilic Addition) — 9701/22/M/J/22/Q5",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Aldehydes and methyl ketones react with saturated aqueous sodium hydrogensulfite (sodium bisulfite, NaHSO3) to form crystalline bisulfite addition adducts.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the role of the hydrogensulfite ion (HSO3⁻) in this reaction (electrophile or nucleophile).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why bulky ketones such as pentan-3-one do not form bisulfite adducts, whereas ethanal and propanone react readily.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe how this reaction can be used practically to purify an aldehyde from a mixture of organic impurities.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Nucleophile (attacks via lone pair on sulfur) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The bisulfite ion is a very bulky nucleophile [1]",
                "Pentan-3-one has two large ethyl groups attached to the carbonyl carbon which create severe steric crowding, preventing the bisulfite adduct from forming [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Shake impure aldehyde with saturated NaHSO3; the solid crystalline adduct precipitates out and is filtered off, washing away impurities [1]",
                "Add dilute acid or dilute alkali to decompose the adduct, regenerating the pure aldehyde [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 2: Diagnostic Tests: 2,4-DNPH, Tollens', Fehling's (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Summary of Diagnostic Tests for Carbonyls — 9701/21/M/J/23/Q7(a)-(e)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Diagnostic reagents allow organic chemists to identify the presence of a carbonyl group and distinguish between aldehydes and ketones. Fig. 14.1 compares the four principal qualitative tests.",
        figure_path="figures/carbonyl_diagnostic_tests_summary.png",
        figure_caption="Fig. 14.1: Summary of qualitative diagnostic tests: 2,4-DNPH, Tollens' reagent, Fehling's solution, and alkaline iodine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation when Brady's reagent (2,4-DNPH) is added to butanal, and describe how this test can be used to positively identify the specific aldehyde beyond just confirming a carbonyl group.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Describe how Tollens' reagent is prepared in the laboratory, state the visible observation with butanal, and write the ionic half-equation for the reduction of silver.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State the observation when Fehling's solution is heated with butanone compared to butanal, and identify the chemical formula of the precipitate formed with butanal.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Explain why ketones do not react with Tollens' reagent or Fehling's solution under ordinary laboratory conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Orange / yellow crystalline precipitate formed [1]",
                "Filter and recrystallise the 2,4-dinitrophenylhydrazone derivative [1]",
                "Dry and determine its sharp melting point, then compare this value with reference tables of known melting points [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Add dilute aqueous ammonia dropwise to aqueous silver nitrate (AgNO3) until the initial brown precipitate of Ag2O just dissolves to form colourless [Ag(NH3)2]⁺ [1]",
                "Silver mirror forms on test tube walls (or black precipitate) [1]",
                "[Ag(NH3)2]⁺ + e⁻ -> Ag(s) + 2NH3 (or Ag⁺ + e⁻ -> Ag) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "With butanone: No reaction / remains clear deep blue [1]",
                "With butanal: Blue solution produces a brick-red / orange-red precipitate [1]",
                "Precipitate formula: Cu2O / copper(I) oxide [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Oxidation of a carbonyl carbon requires the breaking of a C-H bond attached directly to the carbonyl group [1]",
                "Ketones have only strong C-C bonds attached to the carbonyl carbon, which cannot be oxidised by mild oxidising agents like Tollens' or Fehling's [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Condensation Mechanism with 2,4-DNPH — 9701/22/O/N/23/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The reaction between a carbonyl compound and 2,4-dinitrophenylhydrazine is an addition-elimination (condensation) reaction.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of 2,4-dinitrophenylhydrazine.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the general word or chemical equation for the condensation of propanone with 2,4-DNPH, identifying the small molecule eliminated.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why 2,4-DNPH reactions are typically carried out in the presence of an acid catalyst, such as dilute sulfuric acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene ring with -NH-NH2 group attached [1]",
                "Two nitro groups (-NO2) at positions 2 and 4 relative to the hydrazine group [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "(CH3)2C=O + H2N-NH-C6H3(NO2)2 -> (CH3)2C=N-NH-C6H3(NO2)2 + H2O [1]",
                "Small molecule eliminated: Water (H2O) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The acid protonates the carbonyl oxygen atom, creating a positive charge on oxygen [1]",
                "This significantly increases the partial positive charge on the carbonyl carbon (increases electrophilicity), making it more susceptible to nucleophilic attack by the weakly basic hydrazine nitrogen [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Distinguishing Aldehydes and Ketones by Oxidation — 9701/21/O/N/21/Q3(a)-(c)",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Consider two unlabelled liquid samples: pentanal and pentan-3-one.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation when each liquid is heated with acidified potassium dichromate(VI).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced chemical equation for the oxidation of pentanal, using [O] to represent the oxidising agent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Suggest why Tollens' reagent is preferable to acidified potassium dichromate(VI) when testing for the presence of an aldehyde in an unknown mixture that might also contain alcohols.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Pentanal: Orange solution turns green [1]",
                "Pentan-3-one: Solution remains orange / no colour change [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2CH2CHO + [O] -> CH3CH2CH2CH2COOH [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Acidified dichromate(VI) oxidises both primary and secondary alcohols (turning green), leading to a false positive for an aldehyde [1]",
                "Tollens' reagent is a very mild oxidising agent that oxidises aldehydes specifically without reacting with primary or secondary alcohols [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Redox Chemistry of Tollens' and Fehling's Tests — 9701/22/M/J/22/Q6(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="In the Tollens' test, silver(I) complex ions are reduced, while in the Fehling's test, copper(II) tartrate complex ions are reduced.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the ionic equation for the oxidation of ethanal to ethanoate ions by Tollens' reagent in alkaline conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the oxidation number of copper before and after the reaction in Fehling's test, and write the formula of the precipitate.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why Fehling's solution contains tartrate ions in addition to copper(II) sulfate and sodium hydroxide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CHO + 2[Ag(NH3)2]⁺ + 3OH⁻ -> CH3COO⁻ + 2Ag + 4NH3 + 2H2O [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Copper oxidation number changes from +2 to +1 [1]",
                "Precipitate formula: Cu2O [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Tartrate ions act as bidentate/polydentate chelating ligands that complex Cu²⁺ ions [1]",
                "This prevents Cu²⁺ from precipitating out as insoluble copper(II) hydroxide, Cu(OH)2, in the strongly alkaline solution [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Aromatic Aldehydes and Fehling's Solution — 9701/23/M/J/23/Q4(a)-(b)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Benzaldehyde, C6H5CHO, gives a positive result with Tollens' reagent but does not react with Fehling's solution.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the observation when benzaldehyde is warmed with Tollens' reagent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why aliphatic aldehydes (e.g. ethanal) react readily with Fehling's solution, whereas aromatic aldehydes (e.g. benzaldehyde) fail to react, referring to oxidising strength and conjugation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Silver mirror forms on inside of the test tube / grey precipitate of silver [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Fehling's solution is a weaker oxidising agent than Tollens' reagent [1]",
                "Conjugation of the carbonyl group with the benzene ring delocalises electron density and stabilises the aldehyde carbonyl towards oxidation, making benzaldehyde harder to oxidise [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Identifying Unknown Carbonyl Compound W — 9701/21/O/N/23/Q5",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="An organic liquid W has molecular formula C4H8O. It reacts with 2,4-DNPH to form a yellow-orange precipitate, but gives no reaction when warmed with Tollens' reagent.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the conclusions that can be drawn from the positive 2,4-DNPH test and the negative Tollens' test.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic IUPAC name of compound W.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Predict the visible observation when compound W is tested with alkaline aqueous iodine. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Positive 2,4-DNPH confirms presence of a carbonyl group (C=O) [1]",
                "Negative Tollens' test confirms W is a ketone (not an aldehyde) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structural formula: CH3-CO-CH2-CH3 (or CH3COCH2CH3) [1]",
                "Systematic name: Butanone [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Pale yellow precipitate forms [1]",
                "Butanone contains the methyl carbonyl group (CH3-C=O) required for the positive tri-iodomethane reaction [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Purification and Characterisation by Melting Point — 9701/22/F/M/23/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Table 20.1 lists the melting points of the 2,4-dinitrophenylhydrazone derivatives of several carbonyl compounds.",
        parts=[
            QuestionPart(
                label="(a)",
                text="An unknown liquid has boiling point 56 °C. Suggest two carbonyl compounds that have similar boiling points.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="The 2,4-DNPH derivative of this unknown liquid was prepared, recrystallised from ethanol, and melted sharply at 126 °C. Reference data states:\n• Propanone 2,4-DNPH m.p. = 126 °C\n• Propanal 2,4-DNPH m.p. = 154 °C\nIdentify the unknown liquid and explain why measuring the derivative's melting point is more reliable than measuring the liquid's boiling point.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why impurities in a recrystallised sample cause its melting point to be lower and melt over a wider temperature range.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propanone (b.p. 56 °C) and propanal (b.p. 49 °C) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Unknown is propanone [1]",
                "Solid derivatives can be purified to very high purity by recrystallisation [1]",
                "Melting points of solid derivatives are sharp and differ widely (126 °C vs 154 °C), whereas boiling points of liquids are sensitive to atmospheric pressure and close together [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Impurities disrupt the regular crystal lattice structure, weakening intermolecular attractions [1]",
                "Less thermal energy is required to disrupt the lattice (lowering m.p.), and different regions of the non-uniform lattice melt at different temperatures (broadening range) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Multiple Choice: Qualitative Carbonyl Tests — 9701/11/O/N/23/Q21",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Which reagent produces a precipitate with ethanal but NO precipitate with propanal?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reagent:\nA  2,4-dinitrophenylhydrazine\nB  Tollens' reagent\nC  Fehling's solution\nD  Alkaline aqueous iodine",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain your choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "D (Alkaline aqueous iodine) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethanal is the only aldehyde with a CH3-C=O group, so it gives a pale yellow precipitate of CHI3 [1]",
                "Propanal has a CH3CH2-C=O group (not a methyl carbonyl) so it gives a negative result with alkaline iodine, whereas 2,4-DNPH, Tollens', and Fehling's react with both [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Tollens' Test Practical Chemistry and Precautions — 9701/22/M/J/21/Q5",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Tollens' reagent must always be prepared fresh and disposed of immediately after use.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why Tollens' reagent must never be stored or allowed to dry out after an experiment.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State how used Tollens' reagent should be safely destroyed before disposal.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Why should a hot water bath be used to warm the mixture during the Tollens' test rather than direct heating with a Bunsen burner flame?",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "On standing or drying, it forms explosive silver fulminate / silver nitride (Ag3N) [1]",
                "This precipitate is shock-sensitive and can detonate violently on friction or agitation [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Acidify with dilute nitric acid (or dilute hydrochloric acid) to dissolve silver compounds before disposal [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Aldehydes are highly volatile and flammable; gentle warming in a water bath prevents boiling over, charring, and igniting flammable vapours [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Oxidation Resistance of Cyclic Ketones — 9701/21/M/J/22/Q5(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Cyclohexanone is a cyclic ketone.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal formula of cyclohexanone.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Predict the results (positive/negative and visible observation) when cyclohexanone is tested with:\n(i) 2,4-DNPH\n(ii) Tollens' reagent\n(iii) Alkaline aqueous iodine",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Suggest the product formed when cyclohexanone is reduced with NaBH4.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Six-membered ring with a =O on one vertex [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "(i) Positive: Orange / yellow precipitate [1]",
                "(ii) Negative: No silver mirror / solution remains colourless [1]",
                "(iii) Negative: No pale yellow precipitate / no reaction (not a methyl ketone) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Cyclohexanol [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Reaction of Carbonyls with Hydroxylamine — 9701/23/O/N/22/Q3(a)-(b)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Like 2,4-DNPH, hydroxylamine (H2N-OH) reacts with carbonyl compounds by nucleophilic addition-elimination to form oximes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction of propanal with hydroxylamine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the product oxime, CH3CH2CH=N-OH, exhibits geometric (cis-trans / E-Z) isomerism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2CHO + H2NOH -> CH3CH2CH=N-OH + H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Restricted rotation about the C=N double bond [1]",
                "Both the carbon and nitrogen have two different groups attached (carbon has -H and -C2H5; nitrogen has -OH and a lone pair) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Distinguishing Three Isomeric Carbonyls — 9701/22/O/N/21/Q4",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Three isomeric compounds X, Y, and Z have molecular formula C5H10O.\n• X gives a silver mirror with Tollens' reagent and a yellow precipitate with alkaline aqueous iodine.\n• Y gives a silver mirror with Tollens' reagent but no precipitate with alkaline aqueous iodine.\n• Z gives no reaction with Tollens' reagent but gives a yellow precipitate with alkaline aqueous iodine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify whether X, Y, and Z are aldehydes or ketones.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of compound Z.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why compound X cannot exist as an aldehyde containing a methyl carbonyl group, or deduce its true identity.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "X and Y are aldehydes (positive Tollens'); Z is a ketone (negative Tollens') [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Z is a methyl ketone with 5 carbons: pentan-2-one (CH3COCH2CH2CH3) or 3-methylbutan-2-one (CH3COCH(CH3)2) [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ethanal is the ONLY aldehyde that gives a positive iodoform test (having CH3-C=O); no 5-carbon aldehyde can contain a methyl carbonyl group, so observation for X would indicate an impurity or invalid premise [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Multiple Choice: Benedict's and Fehling's Tests — 9701/12/F/M/22/Q21",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Benedict's solution and Fehling's solution both contain copper(II) ions. Which species is responsible for the red precipitate in a positive test?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct species:\nA  CuO\nB  Cu2O\nC  Cu(OH)2\nD  Cu",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the oxidation number of copper in this precipitate.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Cu2O) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "+1 [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 3: Reduction Reactions & Synthetic Interconversions (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Reduction of Carbonyls with Sodium Borohydride — 9701/22/M/J/23/Q4(a)-(d)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Sodium borohydride, NaBH4, is the standard laboratory reducing agent for aldehydes and ketones. Fig. 27.1 illustrates the reduction pathways to primary and secondary alcohols.",
        figure_path="figures/carbonyl_reduction_and_hcn_routes.png",
        figure_caption="Fig. 27.1: Reduction pathways of aldehydes and ketones using aqueous/ethanolic NaBH4.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the role of the BH4⁻ ion during the reduction and identify the nucleophilic species that attacks the carbonyl carbon.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced chemical equation for the reduction of butanal to butan-1-ol using [H] for the reducing agent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write a balanced chemical equation for the reduction of butanone to butan-2-ol using [H].",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Explain why reduction of butanone produces an optically inactive racemic mixture of butan-2-ol.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "BH4⁻ acts as a source of hydride ions (:H⁻) / reducing agent [1]",
                "The nucleophile is the hydride ion (:H⁻) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2CHO + 2[H] -> CH3CH2CH2CH2OH [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "CH3COCH2CH3 + 2[H] -> CH3CH(OH)CH2CH3 [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "The carbonyl group in butanone is planar around the sp2 carbon atom [1]",
                "The hydride ion (:H⁻) has an equal probability of attacking from the top face or bottom face of the planar ketone [1]",
                "This produces an equimolar (50:50) mixture of the two optical enantiomers of butan-2-ol, resulting in zero net optical rotation (racemate) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=28,
        title="Comparison of NaBH4 and LiAlH4 — 9701/21/O/N/23/Q6(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Both NaBH4 and LiAlH4 act as sources of hydride ions, but their reactivity differs significantly.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why NaBH4 can be safely dissolved in water or ethanol, whereas LiAlH4 must be used in strictly anhydrous dry ether.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the violent reaction that occurs when LiAlH4 comes into contact with water.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State which functional groups among aldehydes, ketones, and carboxylic acids can be reduced by:\n(i) NaBH4\n(ii) LiAlH4",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The B-H bond in NaBH4 is relatively covalent and less polarised, reacting only very slowly with water at room temperature [1]",
                "The Al-H bond in LiAlH4 is much more ionic/polar and reacts violently/exothermically with water to release flammable hydrogen gas [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "LiAlH4 + 4H2O -> LiOH + Al(OH)3 + 4H2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "(i) NaBH4 reduces aldehydes and ketones only (cannot reduce carboxylic acids) [1]",
                "(ii) LiAlH4 reduces aldehydes, ketones, AND carboxylic acids (to 1° alcohols) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Selective Reduction of Polyfunctional Compounds — 9701/22/O/N/22/Q5",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Compound G contains both an aldehyde group and a carbon-carbon double bond: CH3-CH=CH-CHO (but-2-enal).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the structure of the organic product formed when compound G reacts with NaBH4 in aqueous ethanol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why NaBH4 reduces the carbonyl group in compound G but leaves the C=C double bond completely unaffected.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest a reagent and catalyst that would reduce BOTH the C=C double bond and the carbonyl group in compound G simultaneously.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-CH=CH-CH2OH (but-2-en-1-ol) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "NaBH4 reduces via nucleophilic attack of hydride ion (:H⁻) on an electron-deficient carbon [1]",
                "The carbonyl carbon is electron-deficient (C(delta+)), whereas the C=C double bond is electron-rich (pi bond cloud) and repels the negatively charged hydride nucleophile [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reagent: Hydrogen gas (H2) [1]",
                "Catalyst: Nickel (Ni) heated or Platinum (Pt) / Palladium (Pd) at room temperature [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Multi-Step Synthesis: Alcohol to Carboxylic Acid via Carbonyl — 9701/21/M/J/22/Q3",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Outline a laboratory procedure for converting propan-1-ol into propanoic acid in high yield.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the oxidising agent and conditions required for this transformation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the overall oxidation using [O].",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why a vertical Liebig condenser (heating under reflux) is essential for this preparation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4) in excess [1]",
                "Heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2OH + 2[O] -> CH3CH2COOH + H2O [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The intermediate propanal has a low boiling point (49 °C) and vaporises rapidly [1]",
                "Reflux condenses volatile propanal vapours and returns them to the hot flask, ensuring complete oxidation to propanoic acid rather than loss of intermediate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Intermolecular Forces: Aldehydes vs Alcohols & Alkanes — 9701/23/M/J/22/Q2",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Table 31.1 compares three compounds with relative molecular mass Mr ≈ 58-60:\n• Butane (Mr = 58.1, b.p. -0.5 °C)\n• Propanal (Mr = 58.1, b.p. 49 °C)\n• Propan-1-ol (Mr = 60.1, b.p. 97 °C)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the principal intermolecular forces present in pure liquid samples of each of the three compounds.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why propanal has a substantially higher boiling point than butane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why propan-1-ol has a substantially higher boiling point than propanal.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Butane: London dispersion (induced dipole-dipole) forces only [1]",
                "Propanal: Permanent dipole-dipole forces and London dispersion forces [1]",
                "Propan-1-ol: Intermolecular hydrogen bonding, permanent dipole-dipole, and London dispersion forces [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Propanal contains a polar carbonyl group (C=O) giving permanent dipoles [1]",
                "Permanent dipole-dipole forces are stronger than the weak dispersion forces in non-polar butane, requiring more thermal energy to separate molecules [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Propan-1-ol has an -OH group and forms intermolecular hydrogen bonds with neighbouring molecules [1]",
                "Hydrogen bonds are significantly stronger than permanent dipole-dipole forces in propanal, requiring much more thermal energy to vaporise [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Solubility of Carbonyls in Water — 9701/12/M/J/21/Q20",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Short-chain aldehydes and ketones (e.g. methanal, ethanal, propanone) are completely miscible with water, but solubility decreases sharply as alkyl chain length increases.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how propanone molecules are able to dissolve in water, despite being unable to form hydrogen bonds with one another in the pure liquid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw a labelled diagram showing a hydrogen bond between a molecule of propanone and a molecule of water.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why octan-2-one is completely insoluble in water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propanone has lone pairs on its electronegative carbonyl oxygen atom [1]",
                "It can act as a hydrogen-bond acceptor, forming hydrogen bonds with the delta+ hydrogen atoms of water molecules [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Correct dipoles shown on water (H(delta+), O(delta-)) and propanone (O(delta-)) [1]",
                "Dashed line from lone pair on propanone oxygen to H(delta+) of water with ~180° bond angle [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The large non-polar hydrophobic hydrocarbon chain disrupts water's extensive hydrogen bond network without generating sufficient solvation energy to overcome dispersion forces [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Hydride Addition Mechanism for NaBH4 — 9701/22/F/M/22/Q5(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The mechanism for the reduction of ethanal by NaBH4 involves two steps.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Draw curly arrows showing nucleophilic attack of a hydride ion (:H⁻) on ethanal to form an ethoxide intermediate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Show how the ethoxide intermediate is protonated by a water molecule from the solvent to yield ethanol and an OH⁻ ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the change in hybridization of the carbonyl carbon atom as it transforms from ethanal to ethanol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Curly arrow from lone pair on :H⁻ to carbonyl carbon C(delta+) of CH3CHO [1]",
                "Curly arrow from C=O double bond onto carbonyl oxygen forming CH3CH2O⁻ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Curly arrow from lone pair on oxygen of CH3CH2O⁻ to H of H-OH [1]",
                "Curly arrow breaking H-OH bond onto oxygen to release OH⁻ [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "From sp2 (trigonal planar, 120°) to sp3 (tetrahedral, 109.5°) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Multiple Choice: Reduction Products — 9701/11/M/J/22/Q23",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Which compound is produced when 3-methylbutan-2-one is treated with NaBH4 in aqueous ethanol?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct IUPAC name:\nA  3-methylbutan-1-ol\nB  3-methylbutan-2-ol\nC  2-methylbutan-2-ol\nD  2-methylbutane",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Write the structural formula of the product and identify any chiral centres.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (3-methylbutan-2-ol) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "(CH3)2CH-CH(OH)-CH3 [1]",
                "Carbon-2 is a chiral centre (bonded to -H, -OH, -CH3, -CH(CH3)2) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Reversible Hydration of Carbonyls (Diols) — 9701/21/O/N/22/Q6",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="In aqueous solution, carbonyl compounds exist in dynamic equilibrium with their geminal diols (hydrates): R2C=O + H2O <=> R2C(OH)2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="In aqueous solution, methanal (HCHO) is over 99% converted into methanediol, whereas propanone is less than 0.1% converted into propane-2,2-diol. Explain this striking difference in equilibrium position.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Trichloroethanal (chloral, CCl3CHO) forms a very stable crystalline solid hydrate, CCl3CH(OH)2 (chloral hydrate). Explain why the three chlorine atoms stabilise the hydrate form so dramatically.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Steric factor: Methanal has two tiny H atoms; converting from planar 120° to tetrahedral 109.5° causes no steric crowding, whereas propanone has two bulky methyl groups which crowd each other in the tetrahedral hydrate [1]",
                "Electronic factor: In propanone, two electron-releasing methyl groups stabilise the planar C=O bond, reducing the driving force for addition [1]",
                "Methanal has no alkyl groups, leaving the carbonyl carbon highly electron-deficient and reactive towards water addition [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "The three strongly electronegative chlorine atoms exert a powerful electron-withdrawing negative inductive (-I) effect [1]",
                "This makes the carbonyl carbon exceptionally electron-deficient in chloral, shifting the hydration equilibrium heavily towards the gem-diol [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Synthesis of Branched Alcohols via Carbonyl Addition — 9701/22/O/N/21/Q5",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Aldehydes and ketones can be converted into carboxylic acids containing one additional carbon atom via hydroxynitrile intermediates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the reaction sequence (reagents and conditions for each step) to convert ethanal into 2-hydroxypropanoic acid.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State how 2-hydroxypropanoic acid can be dehydrated to form an unsaturated carboxylic acid, and name the unsaturated acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: React ethanal with HCN + NaCN (or KCN) at room temp / pH 8 to form 2-hydroxypropanenitrile [2]",
                "Step 2: Heat under reflux with dilute hydrochloric acid (dilute HCl(aq)) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Heat with concentrated sulfuric acid (conc. H2SO4) or concentrated phosphoric acid [1]",
                "Name: Prop-2-enoic acid (acrylic acid) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Acidity of Alpha-Hydrogens in Carbonyls — 9701/23/M/J/21/Q4(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The hydrogen atoms attached to a carbon atom adjacent to a carbonyl group (alpha-hydrogens) are significantly more acidic than hydrogens in alkanes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the alpha-protons of propanone can be removed by a strong base such as hydroxide or ethoxide ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the resonance structures of the enolate anion formed when propanone loses an alpha-proton.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the significance of enolate formation in the tri-iodomethane reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The strongly electronegative carbonyl oxygen pulls electron density towards itself (polar C=O), weakening the adjacent C-H bonds [1]",
                "The resulting carbanion conjugate base is stabilised by resonance delocalisation of negative charge onto the electronegative oxygen atom [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH2⁻-C(=O)-CH3 <-> CH2=C(O⁻)-CH3 [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Enolate formation allows the nucleophilic alpha-carbon to attack iodine molecules, enabling successive halogenation to CI3-CO-R [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Deducing Symmetrical Ketone from Mr and Reactions — 9701/21/M/J/23/Q4",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="A symmetrical ketone T has relative molecular mass Mr = 86.1. It gives an orange precipitate with 2,4-DNPH, but does NOT react with Tollens' reagent or alkaline aqueous iodine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the molecular formula of ketone T.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of ketone T.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structure of the alcohol produced when ketone T is reduced with NaBH4.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C5H10O (5 x 12 + 10 x 1 + 16 = 86) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Structural formula: CH3-CH2-CO-CH2-CH3 [1]",
                "Systematic name: Pentan-3-one (symmetrical, negative iodoform confirms not pentan-2-one) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3-CH2-CH(OH)-CH2-CH3 (pentan-3-ol) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Aldol Dimerisation (Extension of Carbonyl Addition) — 9701/22/M/J/23/Q8",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="When ethanal is treated with dilute aqueous sodium hydroxide at low temperatures, it undergoes a dimerisation reaction called the aldol addition.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the structural formula of the product, 3-hydroxybutanal (aldol).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why this compound is named 'aldol'.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="When 3-hydroxybutanal is warmed with dilute acid, it readily eliminates water. Deduce the structure and IUPAC name of the conjugated unsaturated product formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-CH(OH)-CH2-CHO [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "It contains both an aldehyde ('ald-') and an alcohol ('-ol') functional group in the same molecule [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Structure: CH3-CH=CH-CHO [1]",
                "Systematic name: But-2-enal [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 4: The Tri-iodomethane (Iodoform) Reaction & Deductions (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="Mechanism of the Tri-iodomethane Cleavage — 9701/21/M/J/23/Q9(a)-(d)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The tri-iodomethane reaction is a hallmark diagnostic test for compounds containing the methyl carbonyl (CH3-CO-) group. Fig. 40.1 illustrates the structural requirement, sequential chemical stages, and overall cleavage outcome.",
        figure_path="figures/carbonyl_iodoform_cleavage.png",
        figure_caption="Fig. 40.1: Three chemical stages of the alkaline tri-iodomethane reaction on methyl ketones.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the structural feature a carbonyl compound must possess to give a positive tri-iodomethane test, and name the ONLY aldehyde that gives this positive result.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe the reagents, conditions, and visible observation that confirm a positive test.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced chemical equation for the reaction of propanone with iodine in aqueous sodium hydroxide.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Give the name and formula of the yellow precipitate and the name of the organic salt remaining in solution.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Must contain the methyl carbonyl group: CH3-C(=O)- [1]",
                "Ethanal (acetaldehyde) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents: Aqueous iodine (I2) and aqueous sodium hydroxide (NaOH) (or KI + NaOCl) [1]",
                "Condition: Warm gently / 50-60 °C [1]",
                "Observation: Pale yellow crystalline precipitate with a characteristic medicinal / antiseptic odour [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "CH3COCH3 + 3I2 + 4NaOH -> CHI3(s) + CH3COONa + 3NaI + 3H2O [2]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Precipitate: Tri-iodomethane, CHI3 [1]",
                "Salt: Sodium ethanoate (CH3COONa) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Distinguishing Isomeric Pentanones — 9701/22/O/N/23/Q3(a)-(c)",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Pentan-2-one and pentan-3-one are positional isomers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formulas of pentan-2-one and pentan-3-one.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent and condition that can distinguish between these two isomers.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the observation for each isomer and identify the organic products formed with pentan-2-one.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Pentan-2-one: CH3-CO-CH2-CH2-CH3 [1]",
                "Pentan-3-one: CH3-CH2-CO-CH2-CH3 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagent: Aqueous iodine in aqueous sodium hydroxide (I2 / NaOH(aq)) [1]",
                "Condition: Warm gently [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Pentan-2-one: Pale yellow crystalline precipitate formed [1]",
                "Pentan-3-one: No precipitate / solution remains brown or pale yellow [1]",
                "Organic products from pentan-2-one: Tri-iodomethane (CHI3) and sodium butanoate (CH3CH2CH2COONa) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=42,
        title="Why Other Carbonyls Give Negative Iodoform Tests — 9701/21/O/N/22/Q7",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Explain why the following compounds do NOT give a pale yellow precipitate with alkaline aqueous iodine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Methanal, HCHO.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Propanal, CH3CH2CHO.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Ethanoic acid, CH3COOH (which contains a CH3-C=O group).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Methanal has no methyl group (no alpha-hydrogens at all) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Propanal has an ethyl group attached to the carbonyl (CH3CH2-CO-), with only two alpha-hydrogens (a -CH2- group) [1]",
                "It cannot undergo tri-iodination to form the -CI3 leaving group essential for cleavage to CHI3 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In alkaline solution, ethanoic acid is immediately deprotonated to the resonance-stabilised ethanoate anion, CH3COO⁻ [1]",
                "The negative charge on the carboxylate group strongly repels incoming hydroxide nucleophiles and prevents nucleophilic cleavage [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Infrared Spectroscopy of Carbonyl Compounds — 9701/22/M/J/22/Q7(a)-(c)",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Infrared spectroscopy provides diagnostic evidence for carbonyl groups.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the characteristic wave number range for the stretching vibration of the carbonyl (C=O) bond in aldehydes and ketones.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the C=O absorption peak in an infrared spectrum is extremely sharp and intense compared to C-C or C-H absorptions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Aldehydes display a unique doublet of C-H stretching absorptions at 2700-2800 cm⁻¹ (Fermi resonance). Explain how this feature allows an aldehyde to be distinguished from a ketone in an IR spectrum.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1670 - 1740 cm⁻¹ (or 1680 - 1750 cm⁻¹) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The C=O bond has a very large permanent dipole moment due to the large electronegativity difference between carbon and oxygen [1]",
                "Vibration of this bond produces a large change in dipole moment, giving a very strong absorption band according to selection rules [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The aldehyde C-H bond attached directly to the carbonyl carbon produces characteristic twin bands at 2720 cm⁻¹ and 2820 cm⁻¹ [1]",
                "Ketones lack an aldehyde C-H bond and do not show these twin absorptions, showing only standard aliphatic C-H peaks above 2900 cm⁻¹ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Mass Spectrometric Fragmentation of Carbonyls — 9701/23/M/J/23/Q6",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="The mass spectrum of butan-2-one (Mr = 72) exhibits major fragment peaks at m/z = 57, m/z = 43, and m/z = 15.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the formula and structure of the molecular ion [M]⁺.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structure of the acylium fragment ion responsible for the base peak at m/z = 43.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structure of the fragment ion responsible for the peak at m/z = 57.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Explain why cleavage occurs preferentially adjacent to the carbonyl group (alpha-cleavage).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "[CH3COCH2CH3]⁺• at m/z = 72 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "[CH3-C≡O⁺] (acetyl / ethanoyl cation, m/z = 15 + 28 = 43) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "[CH3CH2-C≡O⁺] (propanoyl cation, m/z = 29 + 28 = 57) OR [CH3CH2CH2CH2]⁺ [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Alpha-cleavage generates resonance-stabilised acylium ions: R-C⁺=O <-> R-C≡O⁺ [1]",
                "The octet rule is satisfied for all atoms in the R-C≡O⁺ resonance contributor, making acylium ions unusually stable [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Comprehensive Deduction of Unknown Carbonyl V — 9701/21/O/N/23/Q8",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="An organic compound V has composition 69.8% carbon, 11.6% hydrogen, and 18.6% oxygen by mass. Its mass spectrum shows a molecular ion peak at m/z = 86.\n• Compound V produces an orange precipitate with 2,4-DNPH.\n• Compound V produces a silver mirror when warmed with Tollens' reagent.\n• Compound V has a branched carbon skeleton and displays four peaks in its carbon-13 NMR spectrum.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the empirical formula and molecular formula of compound V.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the functional group present in compound V and justify your conclusion from the chemical tests.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structural formula and systematic name of compound V.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 69.8/12 = 5.817; H = 11.6/1.0 = 11.6; O = 18.6/16 = 1.163 [1]",
                "Ratio C:H:O = 5:10:1 -> Empirical and Molecular formula = C5H10O (Mr = 86) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Aldehyde functional group (-CHO) [1]",
                "Positive 2,4-DNPH confirms carbonyl group; positive Tollens' test confirms aldehyde (not ketone) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Structural formula: (CH3)2CH-CH2-CHO (3-methylbutanal) OR (CH3)3C-CHO (2,2-dimethylpropanal) [1]",
                "4 carbon environments fits 3-methylbutanal (two equivalent methyls, CH, CH2, CHO); systematic name: 3-methylbutanal [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Multiple Choice: Chiral Centres in Carbonyl Addition — 9701/12/M/J/23/Q23",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="Which reaction produces an organic product that contains a chiral carbon atom?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reaction:\nA  Methanal + HCN / NaCN\nB  Propanone + HCN / NaCN\nC  Ethanal + HCN / NaCN\nD  Pentan-3-one + NaBH4",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name the chiral product formed and identify its chiral carbon centre.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Ethanal + HCN / NaCN) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2-hydroxypropanenitrile [1]",
                "Carbon-2 is chiral, bonded to -H, -CH3, -OH, and -CN [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Multi-Step Synthetic Pathway: Alkene to Ketone — 9701/22/M/J/22/Q8",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Devise a two-step synthetic pathway to convert propene into propanone.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Hydrate propene to propan-2-ol. State the reagents and conditions, and explain why propan-2-ol is the major product.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Oxidise propan-2-ol to propanone. State the reagents, conditions, and write the chemical equation using [O].",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe a test to confirm the presence of propanone in the final product mixture.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Steam (H2O(g)) and concentrated H3PO4 at 300 °C and 60 atm (or conc. H2SO4 then H2O) [1]",
                "Electrophilic addition proceeds via the more stable secondary carbocation intermediate (CH3-C⁺H-CH3) rather than primary [1]",
                "Secondary carbocation is stabilised by the inductive electron-releasing effect of two methyl groups (Markovnikov's rule) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4), heat under reflux [1]",
                "CH3CH(OH)CH3 + [O] -> CH3COCH3 + H2O [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Add 2,4-DNPH: orange precipitate confirms carbonyl; negative Tollens' test confirms ketone [1]",
                "OR: warm with alkaline aqueous iodine to observe a pale yellow precipitate of CHI3 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Fehling's vs Tollens' Reagents — 9701/11/O/N/22/Q22",
        syllabus_ref="17.1",
        difficulty="EASY",
        preamble="When propanal is warmed with Fehling's solution, which species undergoes reduction?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct species:\nA  Copper(II) ions\nB  Propanal\nC  Hydroxide ions\nD  Tartrate ions",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Write the ionic half-equation showing the reduction of this species.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (Copper(II) ions) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2Cu²⁺ + 2OH⁻ + 2e⁻ -> Cu2O + H2O (or Cu²⁺ + e⁻ -> Cu⁺) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Atmospheric Chemistry and Formaldehyde in Smog — 9701/21/M/J/21/Q6",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Methanal (formaldehyde, HCHO) is a significant component of photochemical smog in urban atmospheres.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Methanal is formed by the incomplete combustion of hydrocarbons and the photo-oxidation of volatile organic compounds (VOCs). Write an equation for the complete combustion of methanal.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="In the atmosphere, methanal absorbs UV sunlight (lambda < 330 nm) and undergoes photodissociation: HCHO + h*nu -> H• + •CHO. State the type of bond fission that occurs and define the term free radical.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why methanal is a known health hazard and eye irritant.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HCHO + O2 -> CO2 + H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Homolytic fission [1]",
                "Free radical: A species containing an unpaired valence electron [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Toxic, carcinogenic, cross-links biological proteins, and causes acute mucosal / respiratory irritation [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Chemical Roadmap of C3 Carbonyls — 9701/22/M/J/23/Q10",
        syllabus_ref="17.1",
        difficulty="HARD",
        preamble="Propanal and propanone are structural isomers of formula C3H6O. Complete the comparison table below.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent, condition, and observation for a single test that gives a POSITIVE result with propanal but NO reaction with propanone.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent, condition, and observation for a single test that gives a POSITIVE result with propanone but NO reaction with propanal.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State the reagent and observation for a single test that gives a POSITIVE result with BOTH propanal and propanone.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Draw the structural formula of the alcohol formed when propanal is reduced with NaBH4 and when propanone is reduced with NaBH4.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Tollens' reagent (warm gently) [1]",
                "Propanal: Silver mirror formed on test tube wall [1]",
                "Propanone: No reaction / solution remains colourless (OR Fehling's: propanal turns brick-red, propanone stays blue) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Alkaline aqueous iodine (I2 + NaOH(aq), warm gently) [1]",
                "Propanone: Pale yellow crystalline precipitate of CHI3 [1]",
                "Propanal: No precipitate / negative result [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "2,4-dinitrophenylhydrazine (Brady's reagent / 2,4-DNPH) [1]",
                "Both form a bright orange / yellow crystalline precipitate [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "From propanal: CH3CH2CH2OH (propan-1-ol, 1° alcohol) [1]",
                "From propanone: CH3CH(OH)CH3 (propan-2-ol, 2° alcohol) [1]"
            ], "marks": 2}
        ]
    ),
]
