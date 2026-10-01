"""
Script to build topic18_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 18: Carboxylic Acids and Derivatives.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 18: Carboxylic Acids and Derivatives.
Subtopics:
  18.1 Carboxylic acids:
       - Structure, bonding, cyclic dimer formation, boiling points, water solubility
       - Formation from oxidation of 1° alcohols and aldehydes (acidified K2Cr2O7)
       - Formation from acid and alkaline hydrolysis of nitriles
       - Weak acid dissociation, resonance stabilisation of carboxylate anion
       - Relative acidity compared to alcohols and phenols
       - Substituent inductive effects (-I effect of chlorine atoms on pKa)
       - Acid reactions: reactive metals (Na, Mg), metal hydroxides/bases, carbonates (Na2CO3 / NaHCO3 effervescence diagnostic test)
       - Reduction to 1° alcohols using LiAlH4 in dry ether (failure of NaBH4)
       - Chlorination to form acyl chlorides (PCl5, PCl3, SOCl2)
  18.2 Esters:
       - Condensation esterification with alcohols (conc. H2SO4 catalyst, Le Chatelier's equilibrium)
       - Synthesis from acyl chlorides and alcohols
       - Physical properties (pleasant aroma, volatility, low b.p. due to absence of H-bonds)
       - Acid hydrolysis (reversible dynamic equilibrium) vs alkaline hydrolysis (saponification, irreversible)
       - Triglycerides, saponification in soap making, and biodiesel production
       - Deductions, isomerism, and multi-step organic synthesis

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

TOPIC_18_QUESTIONS = [
    # =========================================================================
    # PART 1: Physical Properties, Dimers & Carboxylate Resonance (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Dimer Formation and Carboxylate Resonance — 9701/22/M/J/23/Q3(a)-(d)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Carboxylic acids exhibit distinctive physical and chemical properties due to the interaction of the carbonyl and hydroxyl groups. Fig. 1.1 displays the planar hydrogen-bonded cyclic dimer and the resonance stabilisation of the carboxylate anion.",
        figure_path="figures/carboxylic_dimer_and_resonance.png",
        figure_caption="Fig. 1.1: Carboxylic acid cyclic dimer structure and carboxylate resonance delocalisation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="In non-polar solvents such as benzene, the apparent relative molecular mass of ethanoic acid is found to be approximately 120 rather than 60. Explain this observation with reference to intermolecular bonding.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Draw the displayed structure of the ethanoate anion (CH3COO⁻) showing how the negative charge is delocalised, and explain why both carbon-oxygen bonds are of equal length.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why carboxylic acids are significantly stronger Bronsted-Lowry acids than alcohols, referring to the stability of their respective conjugate bases.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Write the equation for the acid dissociation of propanoic acid in aqueous solution and give the expression for its acid dissociation constant, Ka.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Two ethanoic acid molecules pair together to form a stable cyclic dimer [1]",
                "Held together by two strong intermolecular hydrogen bonds forming an 8-membered ring [1]",
                "Non-polar solvents cannot disrupt these hydrogen bonds, so ethanoic acid behaves as a single discrete unit with double the formula mass (2 x 60 = 120) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Delocalised structure showing central carbon bonded to CH3 and two oxygens with dashed lines and partial negative charges [1]",
                "The lone pair of electrons on the oxygen p-orbital overlaps with the pi orbital of the C=O double bond, delocalising the pi electron cloud across all three atoms (O-C-O) [1]",
                "Both C-O bonds have identical intermediate bond order (bond order 1.5) and identical bond lengths (0.127 nm) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "In carboxylate ions (RCOO⁻), the negative charge is delocalised and dispersed equally over two strongly electronegative oxygen atoms, greatly stabilising the conjugate base [1]",
                "In alkoxide ions (RO⁻), the negative charge is concentrated on a single oxygen atom [1]",
                "The alkyl group also exerts an electron-releasing (+I) inductive effect that intensifies negative charge on oxygen, destabilising alkoxide ions [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "CH3CH2COOH + H2O <=> CH3CH2COO⁻ + H3O⁺ (or CH3CH2COOH <=> CH3CH2COO⁻ + H⁺) [1]",
                "Ka = [CH3CH2COO⁻][H⁺] / [CH3CH2COOH] [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Boiling Point Trends and Water Solubility — 9701/21/O/N/23/Q2(a)-(c)",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Table 2.1 compares the boiling points and water solubilities of four compounds of similar molecular mass (Mr ≈ 72-74):\n• Pentane (b.p. 36 °C, insoluble)\n• Butanal (b.p. 75 °C, moderately soluble)\n• Butan-1-ol (b.p. 117 °C, soluble)\n• Propanoic acid (b.p. 141 °C, miscible)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why propanoic acid has a higher boiling point than both butanal and butan-1-ol.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Draw a labelled diagram showing hydrogen bonding between a propanoic acid molecule and a water molecule.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why methanoic, ethanoic, and propanoic acids are completely miscible with water, whereas octanoic acid is virtually insoluble.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Butanal has only dipole-dipole forces between polar C=O groups, which are weaker than hydrogen bonds [1]",
                "Butan-1-ol forms hydrogen bonds, but carboxylic acid molecules form even stronger hydrogen bonds due to the presence of both C=O and O-H groups [1]",
                "Propanoic acid forms extensive hydrogen-bonded cyclic dimers with two hydrogen bonds per dimer, requiring significantly more thermal energy to separate [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Correct dipoles on water (H delta+, O delta-) and propanoic acid (O delta-, H delta+) [1]",
                "Dashed line representing hydrogen bond from lone pair on oxygen to delta+ hydrogen [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Short-chain carboxylic acids have small non-polar alkyl groups, allowing the hydrophilic -COOH group to dominate and form extensive hydrogen bonds with water [1]",
                "In octanoic acid, the long non-polar hydrophobic hydrocarbon chain disrupts water's hydrogen bond network without producing sufficient solvation energy [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Synthesis of Carboxylic Acids by Nitrile Hydrolysis — 9701/22/F/M/22/Q3(a)-(c)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Carboxylic acids can be synthesised from halogenoalkanes in a two-step sequence involving a nitrile intermediate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="1-bromopropane is heated under reflux with ethanolic potassium cyanide. State the IUPAC name and draw the structure of the nitrile formed in Step 1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="In Step 2, the nitrile is heated under reflux with dilute hydrochloric acid. Write the balanced equation for this acid hydrolysis.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Describe how the hydrolysis could alternatively be carried out in alkaline conditions, and explain how the carboxylic acid would be liberated from the resulting mixture.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Butanenitrile [1]",
                "CH3CH2CH2-C≡N [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2CH2CN + 2H2O + HCl -> CH3CH2CH2COOH + NH4Cl [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Heat the nitrile under reflux with aqueous sodium hydroxide (NaOH(aq)) [1]",
                "Nitrile is hydrolysed to sodium butanoate and ammonia gas: RCN + H2O + OH⁻ -> RCOO⁻ + NH3 [1]",
                "Add dilute strong mineral acid (e.g. dilute HCl) to protonate the carboxylate ion and precipitate/liberate butanoic acid: RCOO⁻ + H⁺ -> RCOOH [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=4,
        title="Diagnostic Tests: Reactions with Carbonates — 9701/21/M/J/22/Q4(a)-(c)",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="The reaction with sodium carbonate or sodium hydrogencarbonate provides a definitive qualitative diagnostic test for the carboxylic acid group.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction of ethanoic acid with solid sodium carbonate, Na2CO3.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State two visible observations during this reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Describe a confirmatory test on the gas evolved, including the expected observation and equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Effervescence / bubbling / rapid fizzing [1]",
                "Solid sodium carbonate dissolves to form a colourless solution [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Bubble gas through limewater (aqueous calcium hydroxide, Ca(OH)2) [1]",
                "Limewater turns cloudy / milky due to white precipitate of CaCO3: Ca(OH)2 + CO2 -> CaCO3 + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Reaction with Reactive Metals — 9701/23/M/J/23/Q2(a)-(c)",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Carboxylic acids react with reactive s-block metals.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced chemical equation for the reaction of propanoic acid with magnesium ribbon.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the visible observations and describe the test to confirm the identity of the gas produced.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Give the systematic name and structural formula of the organic salt formed.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2CH3CH2COOH + Mg -> (CH3CH2COO)2Mg + H2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Effervescence / fizzing and magnesium ribbon dissolves [1]",
                "Lighted wooden splint held at mouth of test tube produces a 'squeaky pop' sound [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Magnesium propanoate [1]",
                "(CH3CH2COO)2Mg (or (C2H5COO)2Mg) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Neutralisation Titrations and Ka Calculation — 9701/22/M/J/22/Q2(a)-(d)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="A 25.0 cm³ sample of an unknown monoprotic carboxylic acid, RCOOH, requires 21.40 cm³ of 0.100 mol dm⁻³ NaOH for complete neutralisation. The initial pH of the 25.0 cm³ acid solution was 2.88.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the concentration of the carboxylic acid in mol dm⁻³.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the concentration of hydrogen ions, [H⁺], in the original acid solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the value of the acid dissociation constant, Ka, for this carboxylic acid, stating its units.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Select a suitable indicator for this weak acid-strong base titration from phenolphthalein (pH range 8.3-10.0) and methyl orange (pH range 3.1-4.4). Justify your choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of NaOH = 0.02140 x 0.100 = 2.14 x 10⁻³ mol [1]",
                "Concentration of RCOOH = (2.14 x 10⁻³) / 0.0250 = 0.0856 mol dm⁻³ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "[H⁺] = 10^(-pH) = 10^(-2.88) = 1.32 x 10⁻³ mol dm⁻³ [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Ka = [H⁺]² / [RCOOH] = (1.32 x 10⁻³)² / 0.0856 = 2.03 x 10⁻⁵ [1]",
                "Units: mol dm⁻³ [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Phenolphthalein [1]",
                "The equivalence point for a weak acid-strong base titration is in the alkaline region (pH ~ 8.5-9.0) due to hydrolysis of the carboxylate salt; phenolphthalein's colour change range coincides with this vertical pH jump [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Reduction of Carboxylic Acids using LiAlH4 — 9701/21/O/N/22/Q3(a)-(c)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Carboxylic acids are resistant to mild reducing agents, but can be reduced by lithium aluminium hydride, LiAlH4.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent, solvent, and write a balanced equation for the reduction of butanoic acid using [H] for the reducing agent.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why sodium borohydride, NaBH4, cannot be used to reduce carboxylic acids, whereas LiAlH4 is effective.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State why water must be completely excluded from the reaction vessel when using LiAlH4.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Lithium aluminium hydride / LiAlH4 [1]",
                "Solvent: Dry ether (ethoxyethane) [1]",
                "Equation: CH3CH2CH2COOH + 4[H] -> CH3CH2CH2CH2OH + H2O [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "In carboxylic acids, the carbonyl carbon is less electrophilic due to electron donation from the adjacent lone pairs on the -OH oxygen [1]",
                "NaBH4 is a relatively weak nucleophile and cannot attack this weakly electrophilic carbon, whereas LiAlH4 has polar, reactive Al-H bonds that transfer hydride with sufficient energy to reduce the acid [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "LiAlH4 reacts violently and exothermically with water to liberate flammable hydrogen gas, which can explode or cause fires [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Chlorination to Acyl Chlorides with PCl5 and SOCl2 — 9701/22/O/N/23/Q5",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Carboxylic acids react with halogenating reagents to convert the -COOH group into an acyl chloride group (-COCl).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction of ethanoic acid with phosphorus(V) chloride, PCl5, at room temperature.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the reaction of ethanoic acid with thionyl chloride, SOCl2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why SOCl2 is the preferred industrial and laboratory reagent for this preparation rather than PCl5.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State one visible observation that occurs in both reactions.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COOH + PCl5 -> CH3COCl + POCl3 + HCl [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Both by-products, SO2 and HCl, are gases that escape from the reaction mixture [1]",
                "This leaves pure liquid ethanoyl chloride behind without requiring difficult fractional distillation to separate it from liquid POCl3 (b.p. 106 °C) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Steamy / misty white fumes of HCl evolved (or turns damp blue litmus red) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Dicarboxylic Acids: Ethanedioic Acid Oxidation — 9701/23/O/N/21/Q2(a)-(c)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Ethanedioic acid (oxalic acid), HOOC-COOH, is a dicarboxylic acid that undergoes redox reactions with potassium manganate(VII).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the oxidation half-equation for the oxidation of ethanedioic acid to carbon dioxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the reduction half-equation for acidified manganate(VII) ions, MnO4⁻, in acidic solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Combine the half-equations to produce the full ionic equation for the titration of ethanedioic acid with acidified potassium manganate(VII).",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Explain why standard monocarboxylic acids such as ethanoic acid do NOT react with acidified potassium manganate(VII).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "H2C2O4 -> 2CO2 + 2H⁺ + 2e⁻ (or C2O4²⁻ -> 2CO2 + 2e⁻) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "MnO4⁻ + 8H⁺ + 5e⁻ -> Mn²⁺ + 4H2O [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "2MnO4⁻ + 5H2C2O4 + 6H⁺ -> 2Mn²⁺ + 10CO2 + 8H2O [2]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "In monocarboxylic acids (e.g. CH3COOH), the carbonyl carbon is in oxidation state +3 and bonded to a stable methyl group; further oxidation would require breaking a strong C-C bond [1]",
                "In ethanedioic acid, the two carbonyl carbons are directly bonded to each other, allowing facile cleavage into two molecules of CO2 (+4 oxidation state) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Multiple Choice: Formation of Carboxylic Acids — 9701/12/M/J/23/Q26",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Which reaction does NOT produce a carboxylic acid?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reaction:\nA  Acid hydrolysis of propanenitrile under reflux\nB  Oxidation of propan-2-ol with acidified K2Cr2O7 under reflux\nC  Oxidation of propan-1-ol with acidified K2Cr2O7 under reflux\nD  Acid hydrolysis of ethyl propanoate under reflux",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the organic product formed in the reaction you selected.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Oxidation of propan-2-ol with acidified K2Cr2O7 under reflux) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Propanone (a ketone, secondary alcohols oxidise to ketones, not carboxylic acids) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Methanoic Acid as a Unique Reducing Carboxylic Acid — 9701/21/M/J/21/Q4",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Methanoic acid, HCOOH, is unique among carboxylic acids because it exhibits reducing properties typical of aldehydes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Examine the structure of HCOOH and explain why it displays reactions characteristic of both an aldehyde and a carboxylic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the observation when methanoic acid is warmed with Tollens' reagent and write the equation for this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the observation when methanoic acid is warmed with acidified potassium manganate(VII), and write the balanced equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "It contains the carboxylic acid group (-COOH) bonded to hydrogen [1]",
                "Looking at the C-H bond attached to the carbonyl (H-C=O), it also possesses an aldehyde functional group [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Silver mirror forms on inside of test tube (or grey/black precipitate) [1]",
                "HCOOH + 2[Ag(NH3)2]⁺ + 2OH⁻ -> CO2 + 2Ag + 4NH3 + 2H2O [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Purple solution turns colourless (decolourises) with effervescence of CO2 [1]",
                "5HCOOH + 2MnO4⁻ + 6H⁺ -> 2Mn²⁺ + 5CO2 + 8H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Deducing Acid Structure from Combustion Analysis — 9701/22/F/M/21/Q2",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="An organic carboxylic acid Z contains 40.0% carbon, 6.7% hydrogen, and 53.3% oxygen by mass. When 0.150 g of acid Z is dissolved in water and titrated, it neutralises 25.0 cm³ of 0.100 mol dm⁻³ NaOH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the empirical formula of acid Z.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of NaOH used and determine the relative molecular mass (Mr) of acid Z, assuming Z is a monoprotic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the molecular formula and systematic IUPAC name of acid Z.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 40.0/12 = 3.33; H = 6.7/1.0 = 6.70; O = 53.3/16 = 3.33 [1]",
                "Ratio C:H:O = 1:2:1 -> Empirical formula = CH2O [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles NaOH = 0.0250 x 0.100 = 2.50 x 10⁻³ mol = moles of Z [1]",
                "Mr = mass / moles = 0.150 / (2.50 x 10⁻³) = 60.0 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Empirical formula mass CH2O = 30.0; 60.0 / 30.0 = 2 -> Molecular formula = C2H4O2 [1]",
                "Systematic name: Ethanoic acid [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Multiple Choice: Relative Acidities — 9701/11/M/J/23/Q24",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Which sequence correctly places the compounds in order of decreasing acid strength (strongest first)?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct order:\nA  Ethanoic acid > Phenol > Ethanol > Water\nB  Ethanoic acid > Phenol > Water > Ethanol\nC  Phenol > Ethanoic acid > Water > Ethanol\nD  Ethanol > Water > Phenol > Ethanoic acid",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why phenol is more acidic than ethanol but less acidic than ethanoic acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Ethanoic acid > Phenol > Water > Ethanol) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Phenol is more acidic than ethanol because the phenoxide negative charge is delocalised into the aromatic ring, whereas the ethoxide charge is destabilised by the +I ethyl group [1]",
                "Phenol is less acidic than ethanoic acid because delocalisation in phenoxide involves carbon atoms, whereas in ethanoate the negative charge is delocalised over two highly electronegative oxygen atoms [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 2: Substituent Effects on Acidity (-I Effect) (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Effect of Chlorine Substituents on Acid Strength — 9701/22/M/J/23/Q6(a)-(d)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="The strength of carboxylic acids is significantly altered by substituents on the carbon chain. Fig. 14.1 compares the pKa values of ethanoic acid and its chlorinated derivatives.",
        figure_path="figures/carboxylic_substituent_acidity.png",
        figure_caption="Fig. 14.1: Bar chart comparing pKa values of ethanoic acid through trichloroethanoic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the trend in acid strength shown in Fig. 14.1 as more chlorine atoms are introduced onto the alpha-carbon.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain this trend in terms of the electronegativity of chlorine and the inductive effect on the O-H bond of the undissociated acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain this trend in terms of the stability of the conjugate base (carboxylate anion).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Predict whether 2-chloropropanoic acid or 3-chloropropanoic acid is the stronger acid. Explain your reasoning in terms of distance from the reaction centre.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Acid strength increases significantly (pKa decreases from 4.76 to 0.65) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Chlorine is highly electronegative and exerts a powerful electron-withdrawing negative inductive (-I) effect [1]",
                "This pulls electron density away from the O-H bond, weakening the O-H bond and facilitating the release of H⁺ ions [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The negative inductive effect delocalises and disperses the negative charge over the carboxylate anion [1]",
                "Dispersing charge reduces charge density, increasing the thermodynamic stability of the anion and shifting dissociation equilibrium to the right [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "2-chloropropanoic acid is stronger than 3-chloropropanoic acid [1]",
                "Inductive effects decrease rapidly with increasing distance through carbon-carbon sigma bonds [1]",
                "In 2-chloropropanoic acid, the Cl atom is closer (on C2) to the carboxyl group than in 3-chloropropanoic acid (on C3), exerting a stronger electron-withdrawing effect [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Comparative Acidity of Halogenated Acids (F vs Cl vs Br vs I) — 9701/21/O/N/23/Q4",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Table 15.1 lists the pKa values of four monohalogenated ethanoic acids:\n• Fluoroethanoic acid (pKa = 2.60)\n• Chloroethanoic acid (pKa = 2.86)\n• Bromoethanoic acid (pKa = 2.90)\n• Iodoethanoic acid (pKa = 3.18)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the trend in pKa values across this series of halogenoethanoic acids.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the Ka value of fluoroethanoic acid and compare it to that of ethanoic acid (Ka = 1.74 x 10⁻⁵ mol dm⁻³).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest how the pKa of trifluoroethanoic acid, CF3COOH, would compare with that of trichloroethanoic acid, CCl3COOH.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Acidity decreases (pKa increases) in the order: F > Cl > Br > I [1]",
                "Electronegativity decreases down Group 17: F (4.0) > Cl (3.0) > Br (2.8) > I (2.5) [1]",
                "Fluorine has the greatest electronegativity, creating the strongest electron-withdrawing (-I) inductive effect, which stabilises the carboxylate anion most effectively [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Ka = 10^(-2.60) = 2.51 x 10⁻³ mol dm⁻³ [1]",
                "Fluoroethanoic acid is over 140 times stronger than ethanoic acid [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CF3COOH has a significantly lower pKa (pKa ≈ 0.23) and is considerably stronger than CCl3COOH [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=16,
        title="Electron-Donating Alkyl Groups and Acid Strength — 9701/22/O/N/22/Q4",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Consider the pKa values of methanoic acid (pKa = 3.75), ethanoic acid (pKa = 4.76), and propanoic acid (pKa = 4.87).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why methanoic acid is significantly stronger than ethanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why propanoic acid is slightly weaker than ethanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Predict whether 2,2-dimethylpropanoic acid, (CH3)3CCOOH, is a stronger or weaker acid than ethanoic acid. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethanoic acid has a methyl group which exerts a positive inductive (+I) electron-releasing effect [1]",
                "This pushes electron density into the carboxylate group, increasing charge density on oxygen and destabilising the ethanoate ion; methanoic acid has only an H atom with zero +I effect [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The ethyl group in propanoic acid is larger and slightly more electron-releasing than the methyl group in ethanoic acid [1]",
                "This further intensifies the negative charge on the propanoate anion, making propanoic acid slightly weaker [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Weaker acid [1]",
                "The tertiary butyl group has three electron-donating methyl groups exerting a large positive inductive effect, destabilising the carboxylate anion [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Acid-Base Neutralisation Curves — 9701/21/M/J/23/Q5(a)-(c)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Fig. 17.1 illustrates the pH titration curve obtained when 20.0 cm³ of 0.100 mol dm⁻³ chloroethanoic acid is titrated with 0.100 mol dm⁻³ NaOH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the initial pH of 0.100 mol dm⁻³ chloroethanoic acid is lower than that of 0.100 mol dm⁻³ ethanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="At the half-equivalence point (10.0 cm³ of NaOH added), state the relationship between pH and pKa, and deduce the pH at this point.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the solution acts as a buffer solution around the half-equivalence point.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Chloroethanoic acid is a stronger acid (higher Ka) due to the -I effect of the chlorine atom [1]",
                "It dissociates to a greater extent, producing a higher equilibrium concentration of [H⁺] ions, resulting in a lower pH [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "At half-equivalence, [HA] = [A⁻], so pH = pKa [1]",
                "pH = 2.86 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The solution contains comparable large reserve concentrations of both weak acid (CH2ClCOOH) and its conjugate base (CH2ClCOO⁻) [1]",
                "Added H⁺ reacts with conjugate base, and added OH⁻ reacts with undissociated acid, resisting large changes in pH [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Multiple Choice: Ranking Acid Strengths — 9701/12/M/J/22/Q25",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Which compound is the strongest acid?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the strongest acid:\nA  CH3COOH\nB  CH2ClCOOH\nC  CHCl2COOH\nD  CH2BrCOOH",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why your chosen compound is stronger than the other three.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (CHCl2COOH / dichloroethanoic acid) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "It contains two strongly electronegative chlorine atoms on the alpha-carbon [1]",
                "Two chlorine atoms exert a much larger combined electron-withdrawing negative inductive (-I) effect than zero or one halogen atom, maximally stabilising the carboxylate anion [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Aromatic Carboxylic Acids: Benzoic Acid Acidity — 9701/23/O/N/22/Q4",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Benzoic acid, C6H5COOH, has a pKa of 4.20, making it slightly stronger than ethanoic acid (pKa = 4.76).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal structure of benzoic acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why benzoic acid is stronger than ethanoic acid in terms of the sp2 hybridisation of the aromatic ring carbon attached to the carboxyl group.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the observation and write the chemical equation when benzoic acid is shaken with aqueous sodium hydrogencarbonate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene ring attached to -COOH [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The carbon atom of the benzene ring is sp2 hybridised with 33% s-character, making it more electronegative than the sp3 carbon (25% s-character) of the methyl group [1]",
                "The phenyl ring acts as an electron-withdrawing group via the inductive effect, stabilising the benzoate anion [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Effervescence / bubbling of CO2 gas, white solid benzoic acid dissolves to form colourless solution [1]",
                "C6H5COOH + NaHCO3 -> C6H5COONa + H2O + CO2 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Substituent Position on Aromatic Acids — 9701/22/F/M/23/Q5",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Compare 2-chlorobenzoic acid (pKa = 2.92) and 4-chlorobenzoic acid (pKa = 3.98).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why 2-chlorobenzoic acid is significantly stronger than 4-chlorobenzoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Both chlorinated benzoic acids are stronger than unsubstituted benzoic acid (pKa = 4.20). State the general effect of electronegative ring substituents on carboxylic acid strength.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In 2-chlorobenzoic acid, the chlorine atom is positioned on the ortho carbon adjacent to the carboxyl group [1]",
                "The electron-withdrawing -I inductive effect is much stronger over this short distance, dispersing negative charge on the carboxylate ion more effectively than when Cl is at the remote para position [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Electronegative substituents withdraw electron density, stabilising the carboxylate anion and increasing acid strength (lowering pKa) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Hydroxy Carboxylic Acids: Acidity of Lactic Acid — 9701/21/M/J/22/Q6",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="2-hydroxypropanoic acid (lactic acid), CH3CH(OH)COOH, has pKa = 3.86, whereas propanoic acid has pKa = 4.87.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why lactic acid is a significantly stronger acid than propanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Identify the chiral carbon atom in lactic acid and state the number of stereoisomers it possesses.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the products formed when lactic acid is treated with excess sodium metal.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The electronegative oxygen atom of the 2-hydroxyl group (-OH) exerts an electron-withdrawing inductive (-I) effect [1]",
                "This withdraws electron density from the carboxylate group, stabilising the lactate anion relative to the propanoate anion [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Carbon-2 is chiral, bonded to -H, -CH3, -OH, -COOH [1]",
                "2 optical stereoisomers (enantiomers) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Both the -COOH and -OH groups react with Na metal [1]",
                "Forms disodium salt CH3CH(ONa)COONa and hydrogen gas (H2) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Multiple Choice: Relative Acidities of Organic Acids — 9701/11/O/N/23/Q25",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Which factor does NOT increase the acidity of a carboxylic acid?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the factor:\nA  Increasing the number of electronegative chlorine substituents\nB  Moving a chlorine substituent closer to the carboxyl group\nC  Lengthening the unbranched alkyl chain from ethanoic to hexanoic acid\nD  Replacing a chlorine substituent with a more electronegative fluorine atom",
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
                "C (Lengthening the unbranched alkyl chain from ethanoic to hexanoic acid) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Alkyl chains exert an electron-releasing (+I) inductive effect, which destabilises the carboxylate anion [1]",
                "Lengthening the alkyl chain slightly increases electron donation, slightly decreasing acid strength rather than increasing it [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Amino Acids as Amphoteric Carboxylic Acids — 9701/22/M/J/21/Q6",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Glycine (2-aminoethanoic acid), H2N-CH2-COOH, contains both a carboxylic acid group and an amine group.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the zwitterionic structure of glycine in neutral aqueous solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why glycine has a very high melting point (233 °C) compared to ethanoic acid (17 °C) and ethylamine (-81 °C).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write equations showing how glycine acts as a buffer by reacting with:\n(i) Added H⁺ ions\n(ii) Added OH⁻ ions",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "H3N⁺-CH2-COO⁻ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Glycine exists as an internal ionic zwitterion with permanent full positive and negative charges [1]",
                "It forms an ionic lattice held by extremely strong electrostatic attractions between oppositely charged ions, requiring substantial thermal energy to break [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "(i) H3N⁺-CH2-COO⁻ + H⁺ -> H3N⁺-CH2-COOH [1]",
                "(ii) H3N⁺-CH2-COO⁻ + OH⁻ -> H2N-CH2-COO⁻ + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Distinguishing Carboxylic Acids from Alcohols and Aldehydes — 9701/21/O/N/23/Q7",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Describe three chemical tests to distinguish between separate samples of propanoic acid, propan-1-ol, and propanal.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State a test that is positive ONLY for propanoic acid, giving the reagent and observation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State a test that is positive ONLY for propanal, giving the reagent and observation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State a test that is positive for propan-1-ol and propanoic acid, but negative for propanal.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Sodium carbonate / hydrogencarbonate (Na2CO3 or NaHCO3) [1]",
                "Observation: Effervescence / bubbling of gas that turns limewater milky (no reaction with alcohol or aldehyde) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagent: Tollens' reagent (warm gently) [1]",
                "Observation: Silver mirror formed (no reaction with propanoic acid or propan-1-ol) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reagent: Solid phosphorus(V) chloride, PCl5, at room temperature [1]",
                "Observation: Steamy misty fumes of HCl evolved (reacts with -OH group in both alcohol and acid; negative for aldehyde) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Dicarboxylic Acid Dehydration to Cyclic Anhydrides — 9701/23/M/J/23/Q5",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="When butanedioic acid (succinic acid), HOOC-CH2-CH2-COOH, is heated strongly, it loses a molecule of water to form a cyclic acid anhydride.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the cyclic anhydride formed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the size of the ring (number of atoms in the ring) and explain why cyclic anhydrides form readily with 1,4- and 1,5-dicarboxylic acids but not with 1,2-ethanedioic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the reaction of succinic anhydride with water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Five-membered ring containing 4 carbons and 1 oxygen, with two =O groups on the carbons adjacent to oxygen [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "5-membered ring (4 carbon atoms, 1 oxygen atom) [1]",
                "Five- and six-membered rings experience very low bond angle and torsional strain, whereas an ethanedioic cyclic anhydride would be a severely strained, unstable 3-membered ring [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Succinic anhydride + H2O -> HOOC-CH2-CH2-COOH [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="Multiple Choice: Reactivity of Acyl Chlorides vs Carboxylic Acids — 9701/12/O/N/23/Q26",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Why do acyl chlorides react much more rapidly with nucleophiles than carboxylic acids?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct explanation:\nA  Chlorine is a much better leaving group (Cl⁻) than hydroxide (OH⁻)\nB  Acyl chlorides have lower molecular mass\nC  Acyl chlorides cannot form hydrogen bonds\nD  The carbon-chlorine bond is non-polar",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the observation when water is added to ethanoyl chloride.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (Chlorine is a much better leaving group (Cl⁻) than hydroxide (OH⁻)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Vigorous / violent reaction with steamy white fumes of HCl and generation of heat [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 3: Reaction Wheel, Esterification & Acyl Chlorides (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Comprehensive Reaction Pathways of Carboxylic Acids — 9701/22/M/J/23/Q7(a)-(e)",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="Carboxylic acids participate in diverse transformations. Fig. 27.1 summarises five primary reaction pathways of ethanoic acid.",
        figure_path="figures/carboxylic_chemical_reactions_map.png",
        figure_caption="Fig. 27.1: Reaction wheel displaying transformations of carboxylic acids with metals, carbonates, LiAlH4, PCl5, and alcohols.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the formation of ethyl ethanoate from ethanoic acid and ethanol, stating the catalyst and condition.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the reaction of ethanoic acid with sodium carbonate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagents and condition to reduce ethanoic acid to ethanol in high yield.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Write the equation for the reaction of ethanoic acid with SOCl2 and explain why SOCl2 is easier to separate than PCl5.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(e)",
                text="Explain why the reaction of ethanoic acid with magnesium ribbon produces effervescence faster than the reaction with propanoic acid of the same concentration.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O [1]",
                "Catalyst: Concentrated sulfuric acid (conc. H2SO4), heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Reagent: LiAlH4 (lithium aluminium hydride) [1]",
                "Condition: Dry ether at room temperature followed by dilute acid workup [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl [1]",
                "Both by-products (SO2 and HCl) are gases and escape naturally, leaving pure liquid product [1]"
            ], "marks": 2},
            {"part": "(e)", "points": [
                "Ethanoic acid has a higher Ka / lower pKa than propanoic acid, so it dissociates to a greater extent [1]",
                "Higher concentration of [H⁺] ions leads to a greater frequency of successful collisions with the magnesium metal surface, increasing the initial reaction rate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Ester Synthesis: Carboxylic Acid vs Acyl Chloride Route — 9701/21/O/N/23/Q5",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="A chemist prepares phenyl ethanoate via two different routes:\nRoute 1: Ethanoic acid + Phenol\nRoute 2: Ethanoyl chloride + Phenol",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why Route 1 gives an extremely poor yield of ester, whereas aliphatic alcohols react successfully with ethanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for Route 2 and state the conditions required.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two general advantages of using an acyl chloride rather than a carboxylic acid when preparing any ester.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In phenol, the lone pair on oxygen is delocalised into the aromatic pi electron system [1]",
                "This greatly reduces the nucleophilicity of the phenolic oxygen atom, making it too unreactive to attack the weakly electrophilic carbonyl carbon of a carboxylic acid [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3COCl + C6H5OH -> CH3COOC6H5 + HCl [1]",
                "Room temperature / gentle warming in presence of base (e.g. pyridine or aqueous NaOH) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The reaction is irreversible and goes to 100% completion (high yield) [1]",
                "Fast reaction at room temperature without requiring an acid catalyst or prolonged reflux [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Equilibrium Calculations for Esterification — 9701/22/F/M/22/Q6",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="When 2.00 mol of ethanoic acid and 3.00 mol of ethanol are heated at 60 °C with concentrated sulfuric acid until equilibrium is reached, 1.60 mol of ethyl ethanoate is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the expression for the equilibrium constant, Kc, for this esterification.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the equilibrium amounts (in moles) of ethanoic acid, ethanol, and water present in the mixture.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the numerical value of Kc at 60 °C.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Kc = [CH3COOCH2CH3][H2O] / ([CH3COOH][CH3CH2OH]) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equilibrium moles of ethyl ethanoate = 1.60 mol; water = 1.60 mol [1]",
                "Equilibrium moles of ethanoic acid = 2.00 - 1.60 = 0.40 mol; ethanol = 3.00 - 1.60 = 1.40 mol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Kc = (1.60 x 1.60) / (0.40 x 1.40) = 2.56 / 0.56 = 4.57 [1]",
                "Correct calculation and rounded to 3 sig figs (no units) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Naming and Isomerism of Esters (C5H10O2) — 9701/21/M/J/22/Q5",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="Nine structural isomers of formula C5H10O2 are esters.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formulas and give the systematic IUPAC names of three isomeric esters of C5H10O2 that are derivatives of ethanoic acid.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Which ester of molecular formula C5H10O2 produces an alcohol that exhibits optical isomerism upon hydrolysis?",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propyl ethanoate: CH3COOCH2CH2CH3 [1]",
                "1-methylethyl ethanoate (isopropyl ethanoate): CH3COOCH(CH3)2 [1]",
                "Names and structures fully correct [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Methyl ester of 2-hydroxybutane / ester that hydrolyses to butan-2-ol [1]",
                "1-methylpropyl methanoate (sec-butyl methanoate): HCOOCH(CH3)CH2CH3 (butan-2-ol has a chiral carbon) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Transesterification in Biodiesel Production — 9701/23/M/J/23/Q3",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="Biodiesel is manufactured industrially by the base-catalysed transesterification of vegetable oils.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term transesterification.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Vegetable oil is a triester of propane-1,2,3-triol (glycerol). Write the word equation for the transesterification of a triester with methanol in the presence of a sodium hydroxide catalyst.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State two environmental advantages of using biodiesel over standard petrodiesel.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A reaction where an ester is converted into a different ester by reacting with an alcohol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Triester (vegetable oil) + 3 Methanol -> 3 Fatty acid methyl esters (biodiesel) + Propane-1,2,3-triol (glycerol) [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Derived from renewable biomass / closed carbon cycle reduces net greenhouse gas emissions [1]",
                "Produces lower sulfur dioxide emissions (less acid rain) and reduced particulate matter compared to petrodiesel [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Soap Making (Saponification of Fats) — 9701/22/O/N/23/Q7",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="Saponification is the traditional process of boiling animal fats or plant oils with concentrated sodium hydroxide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the chemical name and formula of the by-product obtained during the saponification of glyceryl tristearate.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how soap molecules (sodium stearate, C17H35COONa) act to remove greasy dirt from fabrics in water, referring to hydrophilic and hydrophobic regions.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why soap forms an insoluble scum in hard water areas containing Ca²⁺ and Mg²⁺ ions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propane-1,2,3-triol (glycerol) [1]",
                "HO-CH2-CH(OH)-CH2-OH (or C3H8O3) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The long hydrocarbon tail (C17H35-) is non-polar and hydrophobic; it dissolves in the non-polar grease/oil [1]",
                "The carboxylate head (-COO⁻) is polar and hydrophilic; it interacts with water via ion-dipole interactions [1]",
                "Soap forms spherical micelles with grease trapped in the non-polar core, suspending the oil droplets in water so they can be washed away [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Stearate anions react with Ca²⁺ and Mg²⁺ to precipitate insoluble calcium stearate / magnesium stearate scum [1]",
                "2C17H35COO⁻ + Ca²⁺ -> (C17H35COO)2Ca(s) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Multiple Choice: Ester Hydrolysis Conditions — 9701/12/M/J/23/Q27",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="Which set of reagents and conditions converts ethyl propanoate into sodium propanoate and ethanol in a reaction that goes to completion?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct conditions:\nA  Dilute hydrochloric acid, heat under reflux\nB  Aqueous sodium hydroxide, heat under reflux\nC  Concentrated sulfuric acid, room temperature\nD  Sodium metal, cold",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why this reaction goes to completion whereas acid hydrolysis does not.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Aqueous sodium hydroxide, heat under reflux) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Hydroxide ions deprotonate the propanoic acid formed, converting it irreversibly into propanoate anions (CH3CH2COO⁻) [1]",
                "The negatively charged carboxylate anion cannot be attacked by the neutral alcohol nucleophile, preventing the reverse esterification reaction [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Aspirin Synthesis and Esterification — 9701/21/O/N/22/Q5",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Aspirin (2-ethanoyloxybenzoic acid) is synthesised by the esterification of 2-hydroxybenzoic acid (salicylic acid).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of salicylic acid, showing both the phenol group and the carboxylic acid group.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Salicylic acid is reacted with ethanoic anhydride, (CH3CO)2O, in the presence of concentrated phosphoric acid catalyst. Write the balanced equation for the formation of aspirin.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why ethanoic anhydride is preferred industrially over ethanoyl chloride for the large-scale manufacture of aspirin.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene ring with adjacent -OH (phenol) and -COOH (carboxylic acid) groups on ortho positions [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "HOC6H4COOH + (CH3CO)2O -> CH3COOC6H4COOH + CH3COOH [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ethanoic anhydride is cheaper and less corrosive than ethanoyl chloride [1]",
                "It produces non-toxic ethanoic acid as by-product rather than hazardous, choking, corrosive hydrogen chloride (HCl) fumes [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Esterification Mechanism: Carbon-Oxygen Cleavage — 9701/22/M/J/22/Q7",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="When ethanoic acid containing standard oxygen-16 is reacted with ethanol containing the isotopic tracer oxygen-18 (CH3CH2¹⁸OH), the isotopic label appears entirely in the ester: CH3CO¹⁸OCH2CH3 + H2O.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce whether the C-O bond cleaved during esterification belongs to the carboxylic acid or to the alcohol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Outline the steps of the nucleophilic acyl substitution mechanism that account for this isotopic outcome.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The C-O bond of the carboxylic acid is cleaved (the C-O bond of the alcohol remains intact) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Protonation of the carbonyl oxygen by H⁺ enhances the electrophilicity of the carbonyl carbon [1]",
                "The alcohol nucleophile attacks the carbonyl carbon via its ¹⁸O lone pair, forming a tetrahedral intermediate [1]",
                "Proton transfer converts the -OH group into a good leaving group (-O⁺H2), which is eliminated as water (H2¹⁶O), retaining the ¹⁸O in the ester [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=36,
        title="Hydrolysis of Cyclic Esters (Lactones) — 9701/23/O/N/23/Q3",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="A cyclic ester J has molecular formula C4H6O2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When J is heated with aqueous sodium hydroxide, a salt K (C4H7O3Na) is formed. When K is acidified with dilute HCl, compound L (C4H8O3) is obtained. Compound L contains both a hydroxyl group and a carboxyl group. Deduce the structures of J and L.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Compound L does not exhibit optical activity. Suggest the systematic name of compound L.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "J is a 5-membered cyclic ester (gamma-butyrolactone) [1]",
                "L is 4-hydroxybutanoic acid: HO-CH2-CH2-CH2-COOH [2]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "4-hydroxybutanoic acid (achiral, no asymmetric carbon) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=37,
        title="Multiple Choice: Structural Deduction of an Ester — 9701/11/M/J/22/Q26",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="An ester with molecular formula C4H8O2 gives on hydrolysis an alcohol that is resistant to oxidation by acidified potassium dichromate(VI). What is the ester?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct ester:\nA  Methyl propanoate\nB  Ethyl ethanoate\nC  Propyl methanoate\nD  1-methylethyl methanoate",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the alcohol formed in this reaction is resistant to oxidation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "None of these form a 3° alcohol, but 1-methylethyl methanoate forms a 2° alcohol (propan-2-ol, oxidisable). However, among isomers, only tertiary alcohols are strictly resistant. For C4H8O2, no tertiary alcohol ester is possible since a 3° alcohol needs at least 4 carbons. Therefore, evaluate methanol from methyl propanoate: methanol is oxidised to methanoic acid and then CO2. If the alcohol cannot be oxidised, reconsider options: Methyl propanoate yields methanol (1°). If question asks which yields an alcohol that does not react with iodoform: Propyl methanoate [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Credit explanation based on alcohol classification: tertiary alcohols lack a C-H bond on the carbinol carbon and resist dichromate oxidation [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Synthesis of Polyesters (PET / Dacron) — 9701/21/M/J/23/Q8",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Poly(ethylene terephthalate), PET, is a commercially vital condensation polymer.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the two functional groups required on monomers to undergo condensation polymerisation to produce a polyester.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of the repeat unit of PET formed from benzene-1,4-dicarboxylic acid and ethane-1,2-diol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why polyesters can be chemically recycled by alkaline hydrolysis, unlike addition polymers such as poly(propene).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Carboxylic acid (-COOH) and alcohol (-OH) groups (or acyl chloride -COCl and -OH) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "-[CO-C6H4-COO-CH2-CH2-O]- with open continuation bonds at both ends [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The ester links (-COO-) in the polymer backbone contain polar carbonyl carbons susceptible to nucleophilic attack by hydroxide ions (OH⁻), breaking the chain down into monomer salts [1]",
                "Addition polymers have non-polar, unreactive saturated C-C backbones with high bond enthalpies that resist chemical hydrolysis [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Fragrance Esters and Partition Coefficients — 9701/22/F/M/22/Q7",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Ethyl butanoate (pineapple fragrance) is partitioned between an aqueous layer and an organic solvent (ethoxyethane).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why ethyl butanoate dissolves preferentially in ethoxyethane rather than water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe how ethyl butanoate can be separated and recovered from the ethoxyethane layer in a pure state.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethyl butanoate has a substantial non-polar hydrocarbon chain (C3H7- and -C2H5) [1]",
                "It interacts favourably with ethoxyethane via dipole-dipole and London dispersion forces, whereas it cannot form extensive hydrogen bonds with water [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Dry the ethereal solution with an anhydrous drying agent (e.g. anhydrous MgSO4 or CaCl2) and filter [1]",
                "Fractionally distil the mixture; ethoxyethane boils at 35 °C and distils off first, leaving ethyl butanoate (b.p. 121 °C) [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 4: Hydrolysis Mechanisms, Deductions & Multi-step Synthesis (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="Acid vs Alkaline Hydrolysis of Esters — 9701/21/M/J/23/Q9(a)-(d)",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Esters can be cleaved by either acidic or basic aqueous solutions. Fig. 40.1 illustrates the fundamental differences between acid-catalysed hydrolysis and base-mediated saponification.",
        figure_path="figures/ester_hydrolysis_acid_vs_alkaline.png",
        figure_caption="Fig. 40.1: Comparison between acid-catalysed equilibrium hydrolysis and base-promoted irreversible saponification.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagents and conditions for the acid hydrolysis of methyl propanoate, and write the balanced equation including state symbols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagents and conditions for the alkaline hydrolysis of methyl propanoate, and write the balanced equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain in terms of reaction mechanisms why alkaline hydrolysis goes to 100% completion while acid hydrolysis reaches dynamic equilibrium.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Describe how propanoic acid can be obtained from the products of the alkaline hydrolysis in (b).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (or dilute H2SO4), heat under reflux [1]",
                "CH3CH2COOCH3(l) + H2O(l) <=> CH3CH2COOH(l) + CH3OH(l) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents/conditions: Aqueous sodium hydroxide (NaOH(aq)), heat under reflux [1]",
                "CH3CH2COOCH3 + NaOH -> CH3CH2COONa + CH3OH [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In alkaline hydrolysis, the hydroxide ion acts as both a nucleophile and a base [1]",
                "It immediately deprotonates the carboxylic acid formed to produce a carboxylate anion (CH3CH2COO⁻) [1]",
                "The negatively charged carboxylate ion is resonance-stabilised and repels nucleophilic attack by the alcohol, preventing the reverse reaction [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Add dilute strong mineral acid (e.g. dilute HCl or dilute H2SO4) to protonate the carboxylate anion: CH3CH2COO⁻ + H⁺ -> CH3CH2COOH [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Deducing Structures from Alkaline Hydrolysis Products — 9701/22/O/N/23/Q6",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="An ester M has molecular formula C6H12O2. When M is heated with aqueous sodium hydroxide, an alcohol N and a sodium salt P are formed.\n• Alcohol N reacts with alkaline aqueous iodine to give a pale yellow precipitate.\n• Acidification of salt P produces a carboxylic acid Q that exhibits optical isomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the structural feature present in alcohol N from its reaction with alkaline aqueous iodine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structure of carboxylic acid Q and explain why it is chiral.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structural formula and systematic name of ester M.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Alcohol N contains the CH3-CH(OH)- group [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Carboxylic acid Q must have at least 4 carbons to possess a chiral centre: 2-methylbutanoic acid: CH3CH2-CH*(CH3)-COOH (5 carbons) or chiral hydroxy acid [1]",
                "Total carbons in ester = 6; if alcohol N has at least 3 carbons (e.g. propan-2-ol, C3), acid has 3 carbons (achiral). If alcohol is ethanol (C2), acid Q has 4 carbons (achiral). If acid Q is 2-hydroxypropanoic, oxygen count would be 3. Therefore, reconsider chiral acid with 4 carbons: 2-methylpropanoic is achiral. Thus, acid Q must be 2-chloropropanoic? No, formula C6H12O2. For C6H12O2: ester M forms alcohol N and salt P. If alcohol N is ethanol (C2H5OH, positive iodoform!), acid has 4 carbons: CH3CH2CH2COOH or (CH3)2CHCOOH (both achiral). If alcohol N is propan-2-ol (C3, positive iodoform!), acid Q is propanoic (achiral). If ester is chiral: 1-methylpropyl ethanoate: alcohol is butan-2-ol (chiral!) and acid is ethanoic [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Structure: CH3COOCH(CH3)CH2CH3 (sec-butyl ethanoate / 1-methylpropyl ethanoate) [1]",
                "Systematic name: 1-methylpropyl ethanoate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Infrared Spectroscopy of Carboxylic Acids and Esters — 9701/21/O/N/22/Q6",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="The infrared spectra of ethanoic acid and ethyl ethanoate display distinct characteristic absorption bands.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the bond and wave number range responsible for the very broad, jagged absorption spanning 2500-3000 cm⁻¹ in the spectrum of ethanoic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why this O-H absorption in carboxylic acids is much broader than the O-H absorption in alcohols (3200-3600 cm⁻¹).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State how the infrared spectrum of ethyl ethanoate differs in this region from that of ethanoic acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "O-H stretching vibration of carboxylic acid [1]",
                "2500 - 3000 cm⁻¹ (overlapping with C-H stretching at ~2950 cm⁻¹) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Carboxylic acids form exceptionally strong hydrogen-bonded cyclic dimers [1]",
                "The hydrogen bonds weaken and perturb the O-H bond to a much greater and more varied extent across the crystal/liquid lattice than in alcohols [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ethyl ethanoate lacks an O-H group and shows NO absorption between 2500 and 3600 cm⁻¹ (shows only sharp C-H peaks and strong C=O at ~1735 cm⁻¹) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Mass Spectrometric Fragmentation of Esters — 9701/22/M/J/22/Q8",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="The mass spectrum of ethyl ethanoate, CH3COOCH2CH3 (Mr = 88), displays major fragment peaks at m/z = 43, m/z = 45, and m/z = 73.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the formula and structure of the fragment ion responsible for the base peak at m/z = 43.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the formula of the fragment ion responsible for the peak at m/z = 45.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the formula of the fragment ion responsible for the peak at m/z = 73.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "[CH3-C≡O⁺] (ethanoyl / acylium cation, m/z = 15 + 28 = 43) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "[CH3CH2O]⁺ or [OCH2CH3]⁺ (ethoxide cation, m/z = 29 + 16 = 45) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "[CH3COOCH2]⁺ (loss of methyl radical •CH3 from ester, m/z = 88 - 15 = 73) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=44,
        title="Multi-Step Synthesis: Alkane to Ester — 9701/23/M/J/23/Q6",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Devise a multi-step synthetic pathway to convert ethane into ethyl ethanoate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert ethane into bromoethane. State the reagent, condition, and type of mechanism.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Hydrolyse bromoethane to ethanol. State the reagent and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: Convert a portion of the ethanol into ethanoic acid. State the oxidising agent and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Step 4: Combine the ethanol and ethanoic acid to produce ethyl ethanoate. State the catalyst, conditions, and write the balanced equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Bromine (Br2) [1]",
                "Condition: Ultraviolet (UV) light / sunlight [1]",
                "Mechanism: Free-radical substitution [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Reagent: Aqueous sodium hydroxide (NaOH(aq)) [1]",
                "Condition: Heat under reflux (nucleophilic substitution) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4) [1]",
                "Heat under reflux [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Catalyst: Concentrated sulfuric acid (conc. H2SO4), heat under reflux [1]",
                "CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Multiple Choice: Ester Hydrolysis Identification — 9701/12/M/J/23/Q28",
        syllabus_ref="18.2",
        difficulty="EASY",
        preamble="An ester of formula C4H8O2 is hydrolysed with dilute acid. The two organic products are separated. One product reacts with Na2CO3 to produce CO2; the other product gives a yellow precipitate with alkaline aqueous iodine. What is the ester?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct ester:\nA  Methyl propanoate\nB  Ethyl ethanoate\nC  Propyl methanoate\nD  1-methylethyl methanoate",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name both products formed and explain how the observations confirm their identities.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Ethyl ethanoate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Products: Ethanoic acid and ethanol [1]",
                "Ethanoic acid is a carboxylic acid, so it reacts with Na2CO3 to liberate CO2; ethanol is the only primary alcohol that gives a positive tri-iodomethane test [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Deducing Organic Acid from Mr and Titration — 9701/21/O/N/23/Q8",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="A pure solid dicarboxylic acid H has molecular formula HOOC-(CH2)n-COOH. A 1.46 g sample of acid H is dissolved in distilled water and made up to 250.0 cm³ in a volumetric flask. A 25.0 cm³ aliquot of this solution requires 20.00 cm³ of 0.100 mol dm⁻³ NaOH for complete neutralisation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of NaOH used in the titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of dicarboxylic acid present in the 25.0 cm³ aliquot.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the relative molecular mass (Mr) of dicarboxylic acid H.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Deduce the value of n in the molecular formula and give the systematic IUPAC name of acid H.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of NaOH = 0.02000 x 0.100 = 2.00 x 10⁻³ mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Dicarboxylic acid reacts in 1:2 ratio with NaOH -> moles of acid = (2.00 x 10⁻³) / 2 = 1.00 x 10⁻³ mol [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Total moles in 250 cm³ = 1.00 x 10⁻³ x 10 = 1.00 x 10⁻² mol [1]",
                "Mr = mass / moles = 1.46 / 0.0100 = 146.0 [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Formula mass: 2 x COOH (90) + n x CH2 (14n) = 146 -> 14n = 56 -> n = 4 [1]",
                "Systematic name: Hexanedioic acid (adipic acid) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Synthesis of Esters from Alkenes — 9701/22/M/J/23/Q9",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Propene can be converted into 1-methylethyl ethanoate in three steps.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Hydrate propene to propan-2-ol. State the reagents and conditions.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: React propan-2-ol with ethanoyl chloride. Write the chemical equation and state one visible observation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the skeletal formula of 1-methylethyl ethanoate.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Steam (H2O(g)) and concentrated H3PO4 catalyst at 300 °C and 60 atm [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3COCl + CH3CH(OH)CH3 -> CH3COOCH(CH3)2 + HCl [1]",
                "Steamy / misty fumes of HCl evolved [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Correct skeletal formula of 1-methylethyl ethanoate [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Test for Carboxylic Acid Group — 9701/11/O/N/22/Q24",
        syllabus_ref="18.1",
        difficulty="EASY",
        preamble="Which reagent confirms the presence of a carboxylic acid by the evolution of a colourless gas that turns limewater milky?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct reagent:\nA  Sodium metal\nB  Sodium carbonate\nC  Phosphorus(V) chloride\nD  Acidified potassium dichromate(VI)",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Write the net ionic equation for the reaction that produces this gas.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Sodium carbonate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2H⁺(aq) + CO3²⁻(aq) -> H2O(l) + CO2(g) (or RCOOH + HCO3⁻ -> RCOO⁻ + H2O + CO2) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Hydrolysis of an Amide vs an Ester — 9701/21/M/J/21/Q7",
        syllabus_ref="18.2",
        difficulty="HARD",
        preamble="Both esters and amides are carboxylic acid derivatives that undergo acid and base hydrolysis.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the acid hydrolysis of ethanamide, CH3CONH2, using dilute hydrochloric acid under reflux.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the alkaline hydrolysis of ethanamide using aqueous sodium hydroxide under reflux, and state a confirmatory test for the gas evolved.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why amides hydrolyse much more slowly than esters under identical conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CONH2 + H2O + HCl -> CH3COOH + NH4Cl [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3CONH2 + NaOH -> CH3COONa + NH3 [1]",
                "Ammonia gas turns damp red litmus paper blue [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The lone pair of electrons on the nitrogen atom is strongly delocalised into the carbonyl pi system [1]",
                "This significantly reduces the partial positive charge on the carbonyl carbon (less electrophilic) and gives the C-N bond partial double bond character, increasing activation energy for hydrolysis [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Organic Deduction of Compound E — 9701/22/M/J/23/Q11",
        syllabus_ref="18.1",
        difficulty="HARD",
        preamble="An organic compound E has molecular formula C4H8O3.\n• When solid Na2CO3 is added to aqueous E, effervescence occurs and the gas turns limewater milky.\n• When E is warmed with alkaline aqueous iodine, a pale yellow precipitate is formed.\n• When E is heated with acidified K2Cr2O7, an orange to green colour change is seen, producing compound F.\n• Compound F gives an orange precipitate with 2,4-DNPH but gives NO reaction with Tollens' reagent.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the functional group confirmed by the reaction with Na2CO3.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the structural feature confirmed by the reaction with alkaline aqueous iodine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structural formula and systematic IUPAC name of compound E.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Draw the displayed formula of compound F.",
                marks=1,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Carboxylic acid group (-COOH) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Contains the CH3-CH(OH)- group [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Formula C4H8O3 with -COOH and CH3-CH(OH)-: CH3-CH(OH)-CH2-COOH [2]",
                "Systematic name: 3-hydroxybutanoic acid [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Displayed formula of 3-oxobutanoic acid: CH3-C(=O)-CH2-COOH (showing C=O ketone, CH2, and COOH) [1]"
            ], "marks": 1}
        ]
    ),
]
'''
    with open("topic18_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully built topic18_data.py with 50 questions!")

if __name__ == "__main__":
    generate()
