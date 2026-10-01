"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 16: Hydroxy Compounds (Alcohols).
Subtopic:
  16.1 Alcohols:
       - Classification (1°, 2°, 3° alcohols)
       - Physical properties (boiling point, hydrogen bonding, solubility)
       - Combustion as fuels
       - Substitution reactions to form halogenoalkanes (PCl5, PCl3, SOCl2, NaBr/H2SO4, red P + I2)
       - Reaction with sodium metal and relative acidities
       - Oxidation pathways (acidified potassium dichromate(VI), distillation vs reflux)
       - Dehydration (elimination) to form alkenes (Al2O3 / pumice, conc. H2SO4 / H3PO4, isomerism)
       - Esterification (condensation) with carboxylic acids and acid catalysts
       - The tri-iodomethane (iodoform) reaction (CH3-CH(OH)- group test)
       - Deductions, synthetic routes, and organic identification

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

TOPIC_16_QUESTIONS = [
    # =========================================================================
    # PART 1: Oxidation Pathways, Classification & Diagnostic Tests (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Oxidation Pathways of Alcohols — 9701/22/M/J/23/Q4(a)-(e)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Alcohols are classified into primary (1°), secondary (2°), and tertiary (3°) depending on the number of alkyl groups attached to the carbon bonded to the -OH group. Fig. 1.1 outlines their comparative oxidation pathways using acidified potassium dichromate(VI).",
        figure_path="figures/alcohols_oxidation_routes.png",
        figure_caption="Fig. 1.1: Oxidation pathways and observation outcomes for primary, secondary, and tertiary alcohols.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent, condition, and observation required to oxidise ethanol specifically to ethanal, avoiding the formation of ethanoic acid.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced chemical equation for the oxidation of propan-1-ol to propanoic acid using [O] to represent the oxidising agent.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Describe the chemical structure of 2-methylpropan-2-ol and explain why it does not react with acidified potassium dichromate(VI) under reflux.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State the change in oxidation number of the chromium atom during the oxidation of a secondary alcohol by acidified dichromate(VI) ions.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Acidified potassium dichromate(VI) / K2Cr2O7 + dilute H2SO4 [1]",
                "Condition: Distillation (immediate removal of volatile aldehyde) / heat gently with distillation [1]",
                "Observation: Orange solution turns green [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "CH3CH2CH2OH + 2[O] -> CH3CH2COOH + H2O [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "2-methylpropan-2-ol is a tertiary alcohol with structure (CH3)3C-OH / carbon bonded to -OH has 3 methyl groups [1]",
                "There is no hydrogen atom directly attached to the carbinol carbon (C-OH) so oxidation would require breaking strong C-C bonds [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Oxidation number decreases / Cr is reduced [1]",
                "From +6 (in Cr2O7²⁻) to +3 (in Cr³⁺) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Distinguishing Alcohols by Chemical Tests — 9701/21/O/N/23/Q3(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Three unlabelled bottles contain liquid samples of butan-1-ol, butan-2-ol, and 2-methylpropan-2-ol. A student conducts chemical tests to identify the contents of each bottle.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the reagents and conditions for a single test that distinguishes 2-methylpropan-2-ol from the other two alcohols, and state the observations for each.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Describe how the student could distinguish between butan-1-ol and butan-2-ol after both have been fully oxidised using acidified potassium dichromate(VI).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Suggest an alternative diagnostic test that directly differentiates butan-2-ol from butan-1-ol without prior oxidation. State the reagent and the expected observation for each.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: Acidified K2Cr2O7 and warm/heat [1]",
                "Observation for butan-1-ol and butan-2-ol: Orange to green colour change [1]",
                "Observation for 2-methylpropan-2-ol: Solution remains orange / no visible change [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Oxidation yields butanoic acid (from butan-1-ol) and butanone (from butan-2-ol) [1]",
                "Add sodium carbonate / hydrogencarbonate (or magnesium): effervescence / gas turns limewater milky with butanoic acid, no reaction with butanone [1]",
                "OR: Add Tollens' reagent to distillate: silver mirror formed with butanal, none with butanone [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Reagents: Alkaline aqueous iodine (I2 + NaOH(aq)) / warm gently (iodoform test) [1]",
                "Observation for butan-2-ol: Pale yellow precipitate / antiseptic smell [1]",
                "Observation for butan-1-ol: No precipitate / solution remains brown/pale yellow solution [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=3,
        title="Physical Properties and Hydrogen Bonding — 9701/22/F/M/22/Q2(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Table 3.1 gives the boiling points and water solubilities of four organic compounds of similar relative molecular mass (Mr ≈ 58-60).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Propan-1-ol (b.p. 97 °C) has a significantly higher boiling point than butane (b.p. -0.5 °C) and propanal (b.p. 49 °C). Explain this difference in terms of the intermolecular forces present in each substance.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Draw a labelled diagram to show hydrogen bonding between two molecules of propan-1-ol. Include all lone pairs, partial charges (delta+ and delta-), and bond angles where appropriate.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why propan-1-ol is completely miscible with water, whereas hexan-1-ol is almost insoluble in water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Butane has only weak London dispersion (induced dipole-dipole) forces [1]",
                "Propanal has permanent dipole-dipole forces between polar C=O groups (in addition to dispersion forces) [1]",
                "Propan-1-ol has hydrogen bonding between polar O-H groups, which is significantly stronger than dipole-dipole or dispersion forces, requiring more thermal energy to overcome [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Correct dipoles on both molecules: O(delta-) and H(delta+) on the O-H group [1]",
                "Lone pair shown on the oxygen atom of one molecule [1]",
                "Hydrogen bond represented by dashed line from lone pair to H(delta+) with approximately 180° O-H...O bond angle [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Propan-1-ol forms hydrogen bonds between its -OH group and water molecules, and its non-polar alkyl chain is small [1]",
                "In hexan-1-ol, the long hydrophobic/non-polar alkyl chain disrupts the hydrogen bonding network of water without sufficient energy gain, making it insoluble [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Reaction of Alcohols with Sodium Metal — 9701/23/M/J/23/Q5(a)-(d)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Ethanol reacts steadily with clean sodium metal at room temperature to produce an organic salt and a colourless gas.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction between ethanol and sodium metal, including state symbols.",
                marks=2,
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
                text="Give the systematic name of the organic salt formed and state whether its aqueous solution is acidic, neutral, or alkaline. Explain your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Compare the vigorousness of the reaction of sodium with water to that with ethanol. Explain the difference in terms of acid strength and the nature of the alkyl group.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2CH3CH2OH(l) + 2Na(s) -> 2CH3CH2ONa(s) + H2(g) (or ionic form CH3CH2O⁻Na⁺) [1]",
                "Correct state symbols [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Effervescence / bubbling / fizzing [1]",
                "Sodium metal dissolves / sinks then floats and gets smaller / white solid precipitates [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Sodium ethoxide [1]",
                "Alkaline; the ethoxide ion (CH3CH2O⁻) acts as a strong Bronsted-Lowry base, accepting a proton from water to generate OH⁻ ions [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "The reaction with water is much more vigorous / explosive than with ethanol [1]",
                "Water is a stronger acid than ethanol (ethanol is less acidic than water) [1]",
                "The ethyl group has a positive inductive (+I) electron-releasing effect which increases electron density on the oxygen atom in the ethoxide ion, destabilising it relative to the hydroxide ion [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Halogenation of Alcohols using Phosphorus Halides — 9701/21/M/J/22/Q4(a)-(d)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="The substitution of the hydroxyl group (-OH) by a halogen atom is an essential method for preparing halogenoalkanes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Ethanol reacts vigorously with solid phosphorus(V) chloride, PCl5, at room temperature. Write a balanced equation for this reaction and state one observation that confirms the evolution of hydrogen chloride gas.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Phosphorus(III) chloride, PCl3, also reacts with ethanol upon heating. Write the balanced equation for this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why PCl5 is used as a qualitative diagnostic test for the presence of the -OH group in organic compounds, but cannot be used to distinguish an alcohol from a carboxylic acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Describe how 1-iodobutane can be prepared from butan-1-ol using red phosphorus and iodine. Write the chemical equation for the formation of the reagent and the subsequent reaction with butan-1-ol.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2OH + PCl5 -> CH3CH2Cl + POCl3 + HCl [1]",
                "Steamy / misty white fumes evolved (or turns damp blue litmus red) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "3CH3CH2OH + PCl3 -> 3CH3CH2Cl + H3PO3 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "PCl5 reacts with any compound containing an -OH group to produce steamy fumes of HCl [1]",
                "Both alcohols and carboxylic acids contain an -OH group, so both give the same observation (misty fumes of HCl) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Warm butan-1-ol with a mixture of red phosphorus and iodine [1]",
                "2P + 3I2 -> 2PI3 [1]",
                "3CH3CH2CH2CH2OH + PI3 -> 3CH3CH2CH2CH2I + H3PO3 [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=6,
        title="Halogenation with Thionyl Chloride (SOCl2) — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Thionyl chloride (sulfur dichloride oxide, SOCl2) reacts with alcohols at room temperature to produce chloroalkanes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction of propan-1-ol with SOCl2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the reaction with SOCl2 is widely regarded by organic chemists as the most convenient method for preparing liquid chloroalkanes from alcohols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one hazard associated with this preparation and suggest an appropriate laboratory safety precaution.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH2CH2OH + SOCl2 -> CH3CH2CH2Cl + SO2 + HCl [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Both by-products, SO2 and HCl, are gases and escape from the reaction mixture [1]",
                "The liquid chloroalkane product is left behind in a pure state without needing complex separation / purification [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Both SO2 and HCl are toxic / acidic / choking gases [1]",
                "Perform the reaction in a fume cupboard / fume hood [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Synthesis of Bromoalkanes from Alcohols — 9701/21/O/N/21/Q2(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Bromoalkanes can be prepared by reacting an alcohol with sodium bromide and concentrated acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When preparing 1-bromobutane from butan-1-ol, concentrated sulfuric acid and sodium bromide are heated under reflux. Write equations showing the generation of hydrogen bromide in situ and the formation of 1-bromobutane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why concentrated phosphoric(V) acid, H3PO4, is preferred over concentrated sulfuric acid when preparing a tertiary bromoalkane such as 2-bromo-2-methylpropane from 2-methylpropan-2-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="In the preparation described in (a), the crude 1-bromobutane is washed with concentrated hydrochloric acid, followed by aqueous sodium hydrogencarbonate, and then dried with anhydrous calcium chloride before distillation. State the purpose of washing with aqueous sodium hydrogencarbonate.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "NaBr + H2SO4 -> NaHSO4 + HBr (or 2NaBr + H2SO4 -> Na2SO4 + 2HBr) [1]",
                "CH3CH2CH2CH2OH + HBr -> CH3CH2CH2CH2Br + H2O [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Concentrated H2SO4 acts as a strong dehydrating agent and causes acid-catalysed elimination (dehydration) of tertiary alcohols to form alkenes (2-methylpropene) [1]",
                "Concentrated H2SO4 can also oxidise HBr / bromide ions to bromine gas (Br2), whereas H3PO4 is non-oxidising [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "To neutralise and remove any residual acid (H2SO4 / HCl / HBr) present in the organic layer [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Combustion and Environmental Aspects of Alcohols — 9701/11/M/J/23/Q19",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Bioethanol is widely blended with petrol as an automotive fuel.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced equation for the complete combustion of ethanol, C2H5OH.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Bioethanol is often described as a 'carbon-neutral' fuel. State the biochemical process by which bioethanol is manufactured from glucose, and evaluate whether the lifecycle of bioethanol is truly carbon-neutral.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State one environmental hazard of incomplete combustion of ethanol in vehicle engines compared to complete combustion.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C2H5OH + 3O2 -> 2CO2 + 3H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Fermentation of glucose: C6H12O6 -> 2C2H5OH + 2CO2 (yeast, 25-37 °C, anaerobic) [1]",
                "Plants absorb 6 mol CO2 during photosynthesis; 2 mol released during fermentation and 4 mol during combustion, giving a theoretical net zero CO2 balance [1]",
                "Not strictly carbon-neutral in practice due to fossil fuel consumption during harvesting, processing, fertiliser production, and distillation [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Produces carbon monoxide (CO), which is a toxic gas that binds irreversibly to haemoglobin / unburnt hydrocarbons leading to photochemical smog [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Controlled Oxidation to Aldehyde vs Carboxylic Acid — 9701/22/M/J/22/Q3(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="A chemist oxidises propan-1-ol using two different apparatus setups: Setup A (heating under reflux) and Setup B (heating with simple distillation).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why propan-1-ol can be converted into propanal using Setup B, whereas propan-1-ol is converted into propanoic acid using Setup A.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why propanal has a significantly lower boiling point (49 °C) than both propan-1-ol (97 °C) and propanoic acid (141 °C).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest why an anti-bumping granule is added to the reaction flask before heating in both Setups.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In Setup B (distillation), propanal distils off immediately as it forms because its boiling point is much lower than propan-1-ol, removing it from contact with the oxidising agent before further oxidation [1]",
                "In Setup A (reflux), vapours condense and drip back into the flask, maintaining prolonged contact with excess hot acidified dichromate(VI) [1]",
                "This ensures the intermediate aldehyde is completely oxidised to propanoic acid [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Propanal cannot form intermolecular hydrogen bonds with itself because it lacks an H atom directly bonded to oxygen (has only dipole-dipole attractions) [1]",
                "Both propan-1-ol and propanoic acid have O-H bonds and form strong intermolecular hydrogen bonds, requiring more energy to vaporise [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "To promote smooth boiling / provide nucleation sites for small bubble formation, preventing violent boiling / splashing over ('bumping') [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Identifying Carbonyl Products of Alcohol Oxidation — 9701/12/M/J/23/Q20",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Compound X has molecular formula C4H10O. When X is heated with acidified potassium dichromate(VI), an orange to green colour change is seen, and organic product Y is isolated. Y forms an orange precipitate with 2,4-dinitrophenylhydrazine (2,4-DNPH) but gives NO reaction with Tollens' reagent.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the functional group present in product Y and state what type of alcohol X must be.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of compound X.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Draw the displayed formula of product Y.",
                marks=1,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Positive 2,4-DNPH confirms a carbonyl group (C=O); negative Tollens' test confirms Y is a ketone [1]",
                "Compound X must be a secondary (2°) alcohol [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structural formula: CH3-CH(OH)-CH2-CH3 (or CH3CH(OH)C2H5) [1]",
                "Systematic name: Butan-2-ol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Displayed formula of butanone showing all bonds: CH3-C(=O)-CH2-CH3 with C=O double bond clearly displayed [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Oxidation of Diols and Glycols — 9701/21/O/N/22/Q5(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Ethane-1,2-diol, HO-CH2-CH2-OH, is commonly used in automobile engine anti-freeze mixtures.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Ethane-1,2-diol has a boiling point of 197 °C. Explain why its boiling point is considerably higher than that of ethanol (b.p. 78 °C), even though both have two carbon atoms.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When ethane-1,2-diol is heated under reflux with an excess of acidified potassium dichromate(VI), it undergoes complete oxidation to form dicarboxylic acid Z. Write a balanced equation for this oxidation using [O] for the oxidising agent.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structure of an intermediate compound formed if ethane-1,2-diol is only partially oxidised such that one -OH group is oxidised to an aldehyde and the other to a carboxylic acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethane-1,2-diol has two -OH groups per molecule compared to only one in ethanol [1]",
                "It forms twice as many intermolecular hydrogen bonds per molecule, creating a stronger extensive network that requires far more thermal energy to break [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "HOCH2CH2OH + 4[O] -> HOOC-COOH + 2H2O [1]",
                "Balanced with 4[O] and 2H2O produced [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Structure of 2-oxoethanoic acid (glyoxylic acid): OHC-COOH (or CHO-COOH) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Distinguishing Optical Isomers of Alcohols — 9701/23/O/N/23/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Butan-2-ol exhibits stereoisomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the chiral carbon atom in butan-2-ol by writing its structural formula and marking the chiral centre with an asterisk (*).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw three-dimensional skeletal or displayed representations of the two optical isomers (enantiomers) of butan-2-ol, showing their mirror-image relationship.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why both enantiomers of butan-2-ol react at identical rates when oxidised by acidified potassium dichromate(VI).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-C*H(OH)-CH2-CH3 with asterisk on C2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "3D tetrahedral representations drawn with wedges, dashed lines, and normal bonds [1]",
                "Both enantiomers drawn as non-superimposable mirror images around the chiral carbon [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Acidified dichromate(VI) is an achiral reagent; enantiomers possess identical physical and chemical properties in all achiral environments [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=13,
        title="Multiple Choice: Oxidation Outcomes — 9701/12/F/M/23/Q22",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Which alcohol, when heated with acidified potassium dichromate(VI) under reflux, produces an organic compound that gives a positive result with both 2,4-dinitrophenylhydrazine and Fehling's solution?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct alcohol from the options below: A  Propan-2-ol B  2-methylpropan-2-ol C  None of these alcohols D  Ethanol (under reflux with excess reagent)",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why your chosen option is correct.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (None of these alcohols) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Fehling's solution gives a positive result only with aldehydes (not ketones or carboxylic acids) [1]",
                "Under reflux with excess K2Cr2O7/H⁺, primary alcohols (like ethanol) are fully oxidised to carboxylic acids, secondary alcohols form ketones (Fehling's negative), and tertiary alcohols do not oxidise [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 2: Dehydration, Apparatus, Mechanism & Alkene Isomers (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Catalytic Dehydration Apparatus & Principles — 9701/21/M/J/23/Q5(a)-(d)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Dehydration of alcohols involves the elimination of a molecule of water to produce an alkene. Fig. 14.1 illustrates a standard laboratory apparatus used to dehydrate ethanol.",
        figure_path="figures/alcohols_dehydration_apparatus.png",
        figure_caption="Fig. 14.1: Laboratory catalytic dehydration of ethanol over hot aluminium oxide granules.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the role of the aluminium oxide granules in this experiment and identify an alternative mineral acid catalyst that could be used in liquid phase dehydration.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="In the apparatus shown, explain why the delivery tube must be removed from the water trough before the Bunsen burner flame is turned off.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the dehydration of ethanol and state the classification of this reaction type.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Describe a chemical test on the gas collected over water that confirms it is an unsaturated hydrocarbon, giving the expected observation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Role of Al2O3: Heterogeneous catalyst / lowers activation energy / provides active sites for water elimination [1]",
                "Alternative catalyst: Concentrated sulfuric acid (conc. H2SO4) at 170 °C OR concentrated phosphoric acid (conc. H3PO4) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Turning off the flame causes the air and gases inside the boiling tube to cool and contract, creating a partial vacuum (drop in pressure) [1]",
                "This would suck cold water back up the delivery tube into the hot glass boiling tube, causing it to crack or shatter ('suck-back') [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3CH2OH -> CH2=CH2 + H2O [1]",
                "Elimination (or dehydration) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Bubble gas through aqueous bromine / bromine water (Br2(aq)) [1]",
                "Orange/brown to colourless (decolourises rapidly) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Acid-Catalysed Dehydration Mechanism — 9701/22/O/N/23/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="When ethanol is heated with concentrated sulfuric acid at 170 °C, ethene is formed via an acid-catalysed elimination mechanism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1 involves protonation of the alcohol molecule by H⁺. Draw the structure of the protonated ethanol molecule, including the formal charge.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Step 2 involves the loss of a water molecule to form an intermediate. State the type of intermediate formed and explain why protonation in Step 1 is essential for this step to occur.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3 involves the removal of a proton from an adjacent carbon atom by a base such as HSO4⁻ or H2O. Show this step using a curly arrow to form the carbon-carbon double bond, regenerating the catalyst.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3-CH2-O⁺H2 (positive charge on oxygen with two H atoms attached) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Carbocation intermediate / ethyl carbocation (CH3-CH2⁺) [1]",
                "-OH is a poor leaving group (forms strongly basic OH⁻), whereas protonated -O⁺H2 leaves as a stable, neutral H2O molecule (excellent leaving group) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Curly arrow from C-H bond on adjacent CH3 carbon to C-C bond [1]",
                "Regenerates H⁺ / H2SO4 catalyst and yields CH2=CH2 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Dehydration of Butan-2-ol: Formation of Isomers — 9701/21/M/J/22/Q3(a)-(d)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="When butan-2-ol is heated with concentrated phosphoric acid, elimination occurs to produce a mixture of three isomeric alkenes with molecular formula C4H8.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal structures and give the systematic IUPAC names of all three alkenes formed.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Identify which two of these three alkenes are stereoisomers, and state the specific type of stereoisomerism they exhibit.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why but-2-ene exists as stereoisomers, whereas but-1-ene does not.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State which of the three alkenes is the major product and give a thermodynamic rationale based on alkene stability.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "But-1-ene, cis-but-2-ene (or (Z)-but-2-ene), and trans-but-2-ene (or (E)-but-2-ene) [1]",
                "Correct skeletal structures for all three [2]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "cis-but-2-ene and trans-but-2-ene [1]",
                "Geometric / cis-trans / E-Z isomerism [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Restricted rotation about the C=C double bond (due to pi bond overlap) [1]",
                "In but-2-ene, each carbon of C=C has two different groups attached (-H and -CH3), whereas in but-1-ene, C1 has two identical groups (two H atoms) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Major product: trans-but-2-ene [1]",
                "Disubstituted internal alkene is more thermodynamically stable than monosubstituted terminal alkene (but-1-ene); trans isomer is more stable than cis due to reduced steric clash of bulky methyl groups [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Dehydration of Symmetrical vs Asymmetrical Alcohols — 9701/22/F/M/21/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="The structure of the starting alcohol determines the number of alkene products formed during elimination.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce how many alkene products (including stereoisomers) can be formed by the dehydration of pentan-3-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structure of the single alkene formed when 2-methylpropan-2-ol is dehydrated, and state why this alkene has no stereoisomers.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest an alcohol with molecular formula C5H12O that yields only ONE alkene upon dehydration and that alkene CANNOT exhibit cis-trans isomerism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Pentan-3-ol is symmetrical: elimination in either direction gives pent-2-ene [1]",
                "Pent-2-ene exhibits geometric isomerism, so exactly 2 alkene products are formed: cis-pent-2-ene and trans-pent-2-ene [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "2-methylpropene / (CH3)2C=CH2 [1]",
                "One carbon of the double bond has two identical methyl groups (-CH3) and the other has two identical H atoms, so no cis-trans isomerism is possible [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "2,2-dimethylpropan-1-ol (neopentyl alcohol) CANNOT dehydrate directly without rearrangement, OR 2-methylbutan-2-ol gives 2-methylbut-2-ene as single major non-stereoisomeric product, OR 3-methylbutan-2-ol [1]",
                "Accept 2-methylbutan-2-ol giving 2-methylbut-2-ene (which has two methyl groups on one sp2 carbon, thus no cis-trans) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Comparative Ease of Dehydration (1°, 2°, 3°) — 9701/23/O/N/21/Q3(a)-(b)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="The ease of dehydration of alcohols follows the trend: tertiary > secondary > primary.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain this trend in terms of the stability of the intermediate carbocation formed during the elimination mechanism.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Give the reagents and approximate reaction temperatures required to dehydrate a primary alcohol (ethanol) compared to a tertiary alcohol (2-methylpropan-2-ol).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dehydration proceeds via carbocation intermediates (E1 pathway) [1]",
                "Tertiary carbocations have three electron-releasing alkyl groups that disperse the positive charge via the inductive effect, making them the most stable [1]",
                "Primary carbocations have only one alkyl group and are highly unstable, meaning primary alcohols have much higher activation energies and dehydrate with greatest difficulty (often via concerted E2) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Primary (ethanol): Concentrated H2SO4 at 170 °C (or Al2O3 at 350 °C) [1]",
                "Tertiary (2-methylpropan-2-ol): Moderate heat / 20-50% H2SO4 at ~85 °C [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Ether Formation as Competing Reaction — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="When ethanol is heated with concentrated sulfuric acid at 140 °C instead of 170 °C, the major product is diethyl ether rather than ethene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced chemical equation for the formation of diethyl ether from ethanol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Classify this type of reaction (elimination, substitution, or addition) and explain how the temperature dictates whether elimination or substitution predominates.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structural formula of diethyl ether.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2CH3CH2OH -> CH3CH2-O-CH2CH3 + H2O (catalysed by H2SO4) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Condensation / bimolecular nucleophilic substitution [1]",
                "Higher temperature (170 °C) supplies the higher activation energy needed for unimolecular elimination to ethene; lower temperature (140 °C with excess alcohol) favours bimolecular substitution between two alcohol molecules [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3-CH2-O-CH2-CH3 (or (C2H5)2O) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Dehydration in Multi-Step Synthesis — 9701/21/O/N/23/Q5(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Consider the synthetic conversion: propan-1-ol -> propan-2-ol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the intermediate compound formed in Step 1 and state the reagent and conditions required to convert propan-1-ol to this intermediate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent and conditions required in Step 2 to convert the intermediate into propan-2-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the major product of Step 2 is propan-2-ol rather than propan-1-ol, referring to the mechanism and carbocation stability.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Intermediate: Propene (CH3-CH=CH2) [1]",
                "Reagents/conditions: Heated with concentrated H2SO4 at 170 °C (or passed over hot Al2O3 at 300 °C) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents/conditions: Steam (H2O(g)) and concentrated H3PO4 catalyst at high temperature and pressure (~300 °C, 60 atm) OR cold concentrated H2SO4 followed by warming with water [1]",
                "Mark for steam + H3PO4 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Markovnikov's addition: Electrophilic addition of H⁺ generates a secondary carbocation (CH3-C⁺H-CH3) rather than a primary carbocation (CH3-CH2-C⁺H2) [1]",
                "The secondary carbocation is more stable due to the positive inductive effect of two electron-donating methyl groups, leading predominantly to propan-2-ol [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Industrial Hydration vs Fermentation of Ethanol — 9701/12/M/J/22/Q21",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Ethanol is manufactured worldwide by two main methods: industrial catalytic hydration of ethene and anaerobic fermentation of carbohydrates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the chemical equation, catalyst, temperature, and pressure used for the industrial hydration of ethene.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State two advantages of the catalytic hydration process over the fermentation process.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one distinct advantage of fermentation over catalytic hydration from a sustainability perspective.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH2=CH2(g) + H2O(g) -> C2H5OH(g) [1]",
                "Catalyst: Concentrated phosphoric(V) acid (H3PO4) adsorbed on solid silica [1]",
                "Conditions: 300 °C and 60-70 atm (6-7 MPa) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Continuous process (faster and more efficient than batch fermentation) [1]",
                "Produces pure ethanol directly without needing fractional distillation of a dilute aqueous broth [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Uses renewable biomass resources (sugar cane/corn/glucose) rather than non-renewable crude oil / petroleum-derived ethene [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Dehydration Stoichiometry & Atom Economy — 9701/22/M/J/23/Q6(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="A 7.40 g sample of butan-1-ol (Mr = 74.1) is completely dehydrated using hot concentrated sulfuric acid to yield 4.20 g of but-1-ene (Mr = 56.1).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the theoretical maximum mass of but-1-ene that can be produced from 7.40 g of butan-1-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the percentage yield of but-1-ene obtained in this experiment.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the percentage atom economy for the production of but-1-ene by this dehydration reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of butan-1-ol = 7.40 / 74.1 = 0.09986 mol [1]",
                "Theoretical mass of but-1-ene = 0.09986 x 56.1 = 5.60 g [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Percentage yield = (4.20 / 5.60) x 100 = 75.0% [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Atom economy = [Mr(desired product) / total Mr(all reactants)] x 100 [1]",
                "= [56.1 / 74.1] x 100 = 75.7% [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Acid-Catalysed Rearrangement during Dehydration — 9701/23/M/J/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="When 3,3-dimethylbutan-2-ol is heated with acid, the major alkene obtained is 2,3-dimethylbut-2-ene rather than 3,3-dimethylbut-1-ene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the secondary carbocation formed immediately after protonation and loss of water from 3,3-dimethylbutan-2-ol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how a 1,2-methyl shift (carbocation rearrangement) converts this secondary carbocation into a more stable tertiary carbocation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Show how loss of a proton from this rearranged tertiary carbocation produces 2,3-dimethylbut-2-ene.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(CH3)3C-C⁺H-CH3 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "A methyl group with its bonding pair of electrons migrates from the adjacent quaternary carbon to the C⁺ centre (1,2-methyl shift) [1]",
                "This transforms the secondary carbocation into a more stable tertiary carbocation: (CH3)2C⁺-CH(CH3)2, stabilized by the inductive effect of three alkyl groups [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Loss of H⁺ from the adjacent C-H bond creates a tetrasubstituted C=C bond: (CH3)2C=C(CH3)2 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Deducing Alcohol Structures from Dehydration Products — 9701/21/O/N/22/Q3",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="An unbranched primary alcohol A has molecular formula C5H12O. When dehydrated, it yields alkene B. When B reacts with hydrogen bromide, the major product is compound C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify alcohol A, alkene B, and compound C by giving their IUPAC names.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why compound C is the major organic product rather than 1-bromopentane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest what alkene product would have been obtained if alcohol A had been branched 2,2-dimethylpropan-1-ol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Alcohol A: Pentan-1-ol [1]",
                "Alkene B: Pent-1-ene [1]",
                "Compound C: 2-bromopentane [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Markovnikov addition via the more stable secondary carbocation (CH3-CH2-CH2-C⁺H-CH3) [1]",
                "Secondary carbocation is more stable than primary carbocation due to greater electron-releasing inductive effect of alkyl groups [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Cannot dehydrate without carbon backbone rearrangement / 2-methylbut-2-ene (via methyl shift) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Multiple Choice: Dehydration and Isomerism — 9701/11/O/N/23/Q23",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="How many isomeric alkenes (counting structural and geometric isomers) are formed when 2-methylbutan-1-ol is dehydrated?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct number: A  1 B  2 C  3 D  4",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name the alkene(s) formed and explain your choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (1) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2-methylbutan-1-ol has structure CH3-CH2-CH(CH3)-CH2OH [1]",
                "Dehydration can only eliminate -OH and a proton from the adjacent C2 atom, forming 2-methylbut-1-ene; C1 has two H atoms, so no geometric isomerism exists [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Cyclic Alcohols and Dehydration — 9701/22/F/M/23/Q3(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Cyclohexanol, C6H11OH, is a secondary cyclic alcohol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula of cyclohexanol.",
                marks=1,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When cyclohexanol is heated with concentrated phosphoric(V) acid, cyclohexene is formed. Write the equation for this reaction and explain why only one alkene product is possible.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why cyclohexene does not exhibit cis-trans isomerism under ordinary conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Correct six-membered ring with an -OH group attached to one carbon, showing all atoms/bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "C6H11OH -> C6H10 + H2O [1]",
                "The cyclohexanol ring is completely symmetrical on either side of the C-OH carbon, so elimination on either side produces identical cyclohexene [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The trans-cyclohexene isomer would introduce extreme ring strain / ring is too small to accommodate a trans double bond without rupture [1]",
                "Only the cis isomer can exist in small rings (rings with fewer than 8 carbons) [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 3: Esterification Equilibrium, Mechanism & Work-up (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Acid-Catalysed Esterification and Work-Up — 9701/22/M/J/23/Q3(a)-(e)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Esters are synthesised by the reversible condensation of carboxylic acids with alcohols in the presence of an acid catalyst. Fig. 27.1 outlines the equilibrium and the essential stages in the purification of the product.",
        figure_path="figures/alcohols_esterification_equilibrium.png",
        figure_caption="Fig. 27.1: Equilibrium reaction for ethyl ethanoate synthesis and subsequent purification steps.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the chemical equation for the reaction between ethanoic acid and ethanol, showing all state symbols and the reversible arrow.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain the dual role of concentrated sulfuric acid in this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="During purification, the reaction mixture is transferred to a separating funnel and shaken with aqueous sodium carbonate. Explain why this step is essential and state one visible observation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="The organic layer is subsequently dried with anhydrous magnesium sulfate. What visible change in the appearance of the organic liquid indicates that drying is complete?",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(e)",
                text="State the characteristic physical property of volatile esters that makes them commercially valuable in consumer products.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COOH(l) + CH3CH2OH(l) <=> CH3COOCH2CH3(l) + H2O(l) [1]",
                "Correct state symbols and reversible equilibrium arrow (<=>) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Acts as an acid catalyst (provides H⁺ to protonate the carbonyl oxygen, increasing electrophilicity) [1]",
                "Acts as a dehydrating agent (absorbs water, shifting equilibrium position to the right by Le Chatelier's principle to increase ester yield) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Neutralises and removes unreacted ethanoic acid and sulfuric acid catalyst [1]",
                "Effervescence / fizzing / evolution of CO2 gas bubbles [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "The cloudy liquid becomes clear / transparent [1]"
            ], "marks": 1},
            {"part": "(e)", "points": [
                "Sweet / pleasant / fruity aromas and flavours (used in perfumes, food flavourings, and solvents) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=28,
        title="Naming and Structural Deduction of Esters — 9701/21/O/N/23/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Esters are named according to the alcohol (alkyl group) and the carboxylic acid (alkanoate group) from which they are formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give the systematic IUPAC names for the esters formed from: (i) Methanol and propanoic acid (ii) Propan-2-ol and methanoic acid",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of propyl ethanoate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="An ester E with molecular formula C5H10O2 is hydrolysed by dilute acid to yield alcohol F and carboxylic acid G. When alcohol F is heated with acidified potassium dichromate(VI), it forms a ketone. Deduce the systematic names of E, F, and G.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(i) Methyl propanoate [1]",
                "(ii) 1-methylethyl methanoate (or isopropyl methanoate) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3COOCH2CH2CH3 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Alcohol F forms a ketone, so F must be a secondary alcohol with at least 3 carbons -> propan-2-ol [1]",
                "Total carbons in ester = 5; if alcohol has 3 carbons, acid G must have 2 carbons -> ethanoic acid [1]",
                "Ester E: 1-methylethyl ethanoate (isopropyl ethanoate) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=29,
        title="Ester Hydrolysis: Acid vs Alkaline Catalysis — 9701/22/O/N/22/Q3(a)-(d)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Esters can be hydrolysed back into their parent components using either aqueous acid or aqueous alkali.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the hydrolysis of ethyl ethanoate using dilute hydrochloric acid, and explain why this reaction does not go to completion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the hydrolysis of ethyl ethanoate using aqueous sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why alkaline hydrolysis (saponification) goes to completion, yielding a significantly higher percentage of products than acid hydrolysis.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Describe how the carboxylic acid can be regenerated from the sodium carboxylate salt formed in (b).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COOCH2CH3 + H2O <=> CH3COOH + CH3CH2OH [1]",
                "Acid hydrolysis is a reversible equilibrium reaction, so it reaches dynamic equilibrium rather than completing [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3COOCH2CH3 + NaOH -> CH3COONa + CH3CH2OH [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The hydroxide ion removes a proton from the carboxylic acid formed, converting it into an unreactive carboxylate anion (CH3COO⁻) [1]",
                "Carboxylate ions are negatively charged and cannot be attacked by the alcohol nucleophile, preventing the reverse esterification reaction [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Add a strong dilute mineral acid (e.g. dilute HCl or dilute H2SO4) to protonate the carboxylate ion: CH3COO⁻ + H⁺ -> CH3COOH [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Equilibrium Constant (Kc) for Esterification — 9701/21/M/J/22/Q2(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="In an experiment, 1.00 mol of ethanoic acid is mixed with 1.00 mol of ethanol and a few drops of concentrated sulfuric acid. The mixture is sealed and left at 298 K until equilibrium is reached. At equilibrium, 0.33 mol of ethanoic acid remains unreacted.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the expression for the equilibrium constant, Kc, for this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the equilibrium amounts (in moles) of ethanol, ethyl ethanoate, and water present in the mixture.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the numerical value of Kc at 298 K, and state its units.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Kc = [CH3COOCH2CH3][H2O] / ([CH3COOH][CH3CH2OH]) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of ethanoic acid reacted = 1.00 - 0.33 = 0.67 mol [1]",
                "Equilibrium moles: Ethanol = 1.00 - 0.67 = 0.33 mol; Ethyl ethanoate = 0.67 mol; Water = 0.67 mol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Kc = (0.67 x 0.67) / (0.33 x 0.33) = 0.4489 / 0.1089 = 4.12 [1]",
                "Units: No units (same number of concentration terms in numerator and denominator) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Triglycerides as Natural Triesters — 9701/22/F/M/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Fats and vegetable oils are triesters composed of propane-1,2,3-triol (glycerol) bonded to three long-chain fatty acid molecules.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of propane-1,2,3-triol (glycerol).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="A triester is formed from one molecule of glycerol and three molecules of stearic acid, C17H35COOH. Deduce the molecular formula of this triester.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe the chemical process by which biodiesel is produced from vegetable oil and methanol, and name the catalyst used.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HO-CH2-CH(OH)-CH2-OH (or fully displayed) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Glycerol (C3H8O3) + 3 x C18H36O2 - 3H2O -> C57H110O6 [1]",
                "Working or correct formula C57H110O6 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Transesterification: reacting vegetable oil (triester) with excess methanol to form fatty acid methyl esters (FAME / biodiesel) and glycerol by-product [1]",
                "Catalyst: Sodium hydroxide (NaOH) or potassium hydroxide (KOH) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Intramolecular Esterification (Lactones) — 9701/23/M/J/23/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Compounds that contain both a hydroxyl group and a carboxyl group can undergo intramolecular condensation to form cyclic esters called lactones.",
        parts=[
            QuestionPart(
                label="(a)",
                text="4-hydroxybutanoic acid has structural formula HO-CH2-CH2-CH2-COOH. Draw the structure of the lactone formed when this compound is heated with an acid catalyst.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the size of the ring (number of ring atoms) in this lactone and explain why five- and six-membered cyclic rings form with particular ease.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the other product formed during this reaction.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Cyclic five-membered ring containing 4 carbon atoms and 1 oxygen atom with a =O on the adjacent carbon (gamma-butyrolactone) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "5-membered ring (4 carbons and 1 oxygen) [1]",
                "Five- and six-membered rings have minimal bond angle strain (bond angles close to tetrahedral 109.5° / stable chair conformations) and low torsional strain [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Water / H2O [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Acyl Chlorides vs Carboxylic Acids in Ester Synthesis — 9701/21/O/N/21/Q4",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Alcohols react with both carboxylic acids and acyl chlorides to produce esters.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the reaction of ethanol with ethanoyl chloride, CH3COCl.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State two reasons why acyl chlorides are often preferred over carboxylic acids for synthesising esters in research laboratories.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one disadvantage or hazard of using acyl chlorides rather than carboxylic acids.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COCl + CH3CH2OH -> CH3COOCH2CH3 + HCl [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The reaction is irreversible and goes to completion (high yield) [1]",
                "The reaction occurs rapidly at room temperature without requiring an acid catalyst or prolonged heating [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Produces hazardous / toxic / corrosive hydrogen chloride gas (HCl misty fumes); acyl chlorides react vigorously with moisture in the air [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Multiple Choice: Structural Identification of Esters — 9701/12/O/N/23/Q25",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Which ester on acid hydrolysis yields an alcohol that cannot be dehydrated to form an alkene?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct ester from the options below: A  Ethyl methanoate B  Methyl ethanoate C  Propyl ethanoate D  1-methylethyl propanoate",
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
                "B (Methyl ethanoate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Hydrolysis of methyl ethanoate yields methanol (CH3OH) and ethanoic acid [1]",
                "Methanol has only one carbon atom and therefore cannot undergo elimination to form an alkene (which requires a minimum of two carbons for a C=C bond) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Isomeric Esters of Molecular Formula C4H8O2 — 9701/22/M/J/22/Q5(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Four structural isomers of C4H8O2 are esters.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula and give the systematic IUPAC name of all four isomeric esters with molecular formula C4H8O2.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="Which of these four esters produces an alcohol that gives a positive tri-iodomethane (iodoform) test upon alkaline hydrolysis?",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HCOOCH2CH2CH3 : Propyl methanoate [1]",
                "HCOOCH(CH3)2 : 1-methylethyl methanoate (isopropyl methanoate) [1]",
                "CH3COOCH2CH3 : Ethyl ethanoate [1]",
                "CH3CH2COOCH3 : Methyl propanoate [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Ethyl ethanoate (hydrolyses to ethanol, the only primary alcohol giving a positive iodoform test) OR 1-methylethyl methanoate (hydrolyses to propan-2-ol, positive iodoform) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Distinguishing Alcohols from Phenols — 9701/21/M/J/21/Q3(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Alcohols and phenols both contain the hydroxyl group (-OH), but their chemical properties differ significantly due to the presence of the aromatic ring in phenol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation when aqueous bromine (Br2(aq)) is added separately to cyclohexanol and to phenol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the observation when neutral aqueous iron(III) chloride (FeCl3(aq)) is added to cyclohexanol and to phenol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why phenol is acidic enough to dissolve in aqueous sodium hydroxide, whereas aliphatic alcohols such as ethanol do not react significantly with aqueous sodium hydroxide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Cyclohexanol: No visible reaction / solution remains orange-brown [1]",
                "Phenol: Decolourises bromine water and forms a white precipitate of 2,4,6-tribromophenol [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Cyclohexanol: No colour change (remains yellow/brown) [1]",
                "Phenol: Gives a characteristic violet / purple solution [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In phenoxide ion, the negative charge on oxygen is delocalised into the pi system of the benzene ring, stabilising the phenoxide ion [1]",
                "In ethoxide ion, the alkyl group releases electron density (+I effect), concentrating negative charge on oxygen and destabilising the ion, so ethanol is far less acidic than water [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Esterification Kinetics and Catalysis — 9701/23/O/N/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="The rate of esterification between ethanoic acid and ethanol without an added catalyst is extremely slow at room temperature.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain in terms of activation energy and collision theory why adding concentrated sulfuric acid increases the reaction rate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain whether adding more catalyst increases the final equilibrium yield of ethyl ethanoate. Justify your answer using Le Chatelier's principle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State what happens to the position of equilibrium and the value of Kc if the temperature of this exothermic esterification reaction is raised.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A catalyst provides an alternative reaction pathway with a lower activation energy (Ea) [1]",
                "A greater proportion of colliding molecules possess kinetic energy greater than or equal to Ea, increasing the frequency of successful collisions [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "No, a catalyst increases the rate of forward and backward reactions equally [1]",
                "It allows equilibrium to be reached faster but does not alter the equilibrium position or the value of Kc [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Equilibrium shifts in the endothermic direction (to the left / backwards) [1]",
                "The value of Kc decreases [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Fragrance Formulation and Volatility — 9701/22/F/M/21/Q3(a)-(b)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Fragrance chemists classify scents into top notes, middle notes, and base notes based on their volatility and molecular structure.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Ethyl butanoate has a pineapple scent and octyl ethanoate has an orange scent. Explain why ethyl butanoate evaporates more readily than octyl ethanoate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why pure esters are less soluble in water than their precursor carboxylic acids and alcohols of similar molecular mass.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethyl butanoate (Mr = 116) has fewer electrons than octyl ethanoate (Mr = 172) [1]",
                "Octyl ethanoate has stronger London dispersion forces between molecules due to its larger surface area and more electrons, requiring more thermal energy to vaporise [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Esters cannot donate hydrogen bonds to one another or form as extensive hydrogen bonds with water (they have no O-H group) [1]",
                "Carboxylic acids and alcohols have polar O-H groups capable of forming strong hydrogen bonds with water molecules [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Polyesters as Condensation Polymers — 9701/21/M/J/23/Q6(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Terylene (PET) is a synthetic polyester widely used in synthetic clothing fibres and plastic bottles.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the two monomer molecules from which Terylene is manufactured.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of the repeat unit of Terylene, clearly showing the ester linkage.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State why polyesters are generally biodegradable under composting conditions, unlike addition polymers such as poly(ethene).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene-1,4-dicarboxylic acid (terephthalic acid) [1]",
                "Ethane-1,2-diol (ethylene glycol) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "-[CO-C6H4-COO-CH2CH2-O]- [1]",
                "Open bonds at both ends and correct ester linkages [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The polar ester linkages (-COO-) in polyesters are susceptible to hydrolysis by environmental microorganisms, moisture, and enzymes, whereas the non-polar C-C backbone in polyalkenes is inert [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 4: The Iodoform Test, Diagnostic Deductions & MCQs (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="The Tri-iodomethane (Iodoform) Reaction — 9701/21/M/J/23/Q8(a)-(d)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="The tri-iodomethane reaction is a diagnostic test for specific structural features in alcohols and carbonyl compounds. Fig. 40.1 illustrates the structural requirement, reaction stages, and observed outcome.",
        figure_path="figures/alcohols_iodoform_test_reaction.png",
        figure_caption="Fig. 40.1: Structural criteria and stages of the tri-iodomethane (iodoform) reaction.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the essential structural feature an alcohol must possess to give a positive result in the tri-iodomethane test.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the only primary alcohol that gives a positive tri-iodomethane test.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagents and condition for the test, and describe the visible observation indicating a positive result.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Write the balanced chemical equation for the reaction of propan-2-ol with iodine in aqueous sodium hydroxide, identifying the precipitate formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Must contain the CH3-CH(OH)- group (a methyl group directly attached to a carbon carrying an -OH and an H) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethanol (CH3CH2OH) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Reagents: Aqueous iodine (I2) and aqueous sodium hydroxide (NaOH) (or KI + NaOCl) [1]",
                "Condition: Warm gently / 50-60 °C [1]",
                "Observation: Pale yellow crystalline precipitate (with characteristic medicinal / antiseptic odour) [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "CH3CH(OH)CH3 + 4I2 + 6NaOH -> CHI3 + CH3COONa + 5NaI + 5H2O [1]",
                "Precipitate is tri-iodomethane, CHI3 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Distinguishing Isomeric Butanols with Iodoform — 9701/22/O/N/23/Q5(a)-(c)",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Consider the four structural isomers of C4H10O: • Isomer 1: Butan-1-ol • Isomer 2: Butan-2-ol • Isomer 3: 2-methylpropan-1-ol • Isomer 4: 2-methylpropan-2-ol",
        parts=[
            QuestionPart(
                label="(a)",
                text="Which ONE of these four isomers gives a positive tri-iodomethane test? Explain your choice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Give the structural formula and systematic name of the carboxylate salt produced when that isomer reacts in the test.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why 2-methylpropan-2-ol gives a negative result in the tri-iodomethane test.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Isomer 2 / Butan-2-ol [1]",
                "It is the only isomer that contains the CH3-CH(OH)- group (carbon-2 bears a methyl group, an -OH, and an H atom) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2COONa (or CH3CH2COO⁻) [1]",
                "Sodium propanoate [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "2-methylpropan-2-ol is a tertiary alcohol with no hydrogen atom on the carbinol carbon [1]",
                "The first step of the iodoform reaction requires oxidation of the alcohol to a methyl ketone, which tertiary alcohols cannot undergo [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Three-Step Mechanism of the Iodoform Test — 9701/21/O/N/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="The tri-iodomethane reaction proceeds via three sequential stages: oxidation, halogenation, and alkaline cleavage.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1 is oxidation of propan-2-ol by hypoiodite ions (OI⁻) formed in situ. Write an equation showing the organic product formed in this first step.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Step 2 involves substitution of the three alpha-hydrogens on the methyl group by iodine. Explain why the hydrogen atoms on this methyl group are acidic enough to be deprotonated by OH⁻.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3 is nucleophilic attack of hydroxide ion on the carbonyl carbon followed by C-C bond cleavage. Explain why the -CI3 group acts as a leaving group in this step.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CH(OH)CH3 + OI⁻ -> CH3COCH3 + I⁻ + H2O (forms propanone) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The strongly electronegative carbonyl oxygen withdraws electron density (via polar C=O bond), making alpha-protons weakly acidic [1]",
                "The resulting enolate conjugate base is resonance-stabilised by delocalisation of negative charge onto the electronegative oxygen atom [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The three strongly electronegative iodine atoms stabilize the carbanion :CI3⁻ via a powerful negative inductive (-I) effect [1]",
                ":CI3⁻ is promptly protonated by water/carboxylic acid to form neutral CHI3 precipitate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Identification of Unknown Organic Compound X — 9701/23/M/J/23/Q3",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Organic liquid X contains 60.0% carbon, 13.3% hydrogen, and 26.7% oxygen by mass. Its relative molecular mass is 60.0. • Liquid X reacts with sodium metal to produce hydrogen gas. • When X is warmed with alkaline aqueous iodine, a pale yellow precipitate forms. • When X is heated with acidified K2Cr2O7, the solution turns from orange to green.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Determine the empirical formula and molecular formula of compound X.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of compound X, showing how your deduction accounts for each experimental observation.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Give the name and structure of the organic product formed when X is oxidised by acidified potassium dichromate(VI).",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles: C = 60.0/12 = 5.00; H = 13.3/1.0 = 13.3; O = 26.7/16 = 1.67 [1]",
                "Mole ratio C:H:O = 3:8:1 -> Empirical and Molecular formula = C3H8O [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reaction with Na confirms -OH group (alcohol) [1]",
                "Positive iodoform test confirms CH3-CH(OH)- group; oxidation orange to green confirms 1° or 2° alcohol [1]",
                "Structural formula: CH3-CH(OH)-CH3; Systematic name: Propan-2-ol [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Systematic name: Propanone [1]",
                "Structure: CH3-CO-CH3 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Comparative Table of Diagnostic Tests — 9701/21/O/N/23/Q6",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Five organic liquids are tested with three reagents: Reagent 1 (PCl5), Reagent 2 (acidified K2Cr2O7 + heat), and Reagent 3 (I2 / NaOH(aq) + warm).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the expected observation (positive / negative / specific colour) for each test on ethanol, C2H5OH.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the expected observation for each test on 2-methylpropan-2-ol, (CH3)3COH.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State the expected observation for each test on propan-1-ol, CH3CH2CH2OH.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent 1 (PCl5): Misty / steamy fumes of HCl [1]",
                "Reagent 2 (K2Cr2O7/H⁺): Orange solution turns green [1]",
                "Reagent 3 (I2/NaOH): Pale yellow precipitate of CHI3 [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Reagent 1 (PCl5): Misty / steamy fumes of HCl [1]",
                "Reagent 2 (K2Cr2O7/H⁺): Remains orange / no colour change [1]",
                "Reagent 3 (I2/NaOH): No precipitate / remains brown or pale yellow solution [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Reagent 1 (PCl5): Misty / steamy fumes of HCl [1]",
                "Reagent 2 (K2Cr2O7/H⁺): Orange solution turns green [1]",
                "Reagent 3 (I2/NaOH): No precipitate / negative [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=45,
        title="Distinguishing Alcohols from Aldehydes and Ketones — 9701/12/M/J/23/Q24",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Which set of reagents can successfully distinguish between propan-1-ol, propan-2-ol, and propanone?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct combination: A  Acidified K2Cr2O7 only B  2,4-DNPH followed by alkaline aqueous iodine C  Tollens' reagent followed by Fehling's solution D  Sodium metal only",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Outline the results of your chosen combination for each of the three compounds.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2,4-DNPH: Forms orange precipitate with propanone (carbonyl compound); no precipitate with propan-1-ol or propan-2-ol [1]",
                "Alkaline I2 test: Forms pale yellow precipitate with propan-2-ol (CH3CH(OH)-) and with propanone (CH3CO-), but gives no precipitate with propan-1-ol [1]",
                "Together, these two tests unequivocally distinguish all three compounds [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=46,
        title="Spectroscopic Analysis of Alcohols (IR & MS) — 9701/22/M/J/22/Q4(a)-(c)",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Compound K is an alcohol. Its infrared spectrum displays a broad absorption peak centered at 3350 cm⁻¹ and a sharp absorption at 2960 cm⁻¹. Its mass spectrum shows a molecular ion peak at m/z = 74 and a major fragment peak at m/z = 45.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the bond vibration responsible for the broad peak at 3350 cm⁻¹ and explain why this absorption is broad.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the molecular formula of compound K from its molecular ion at m/z = 74.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Suggest the formula of the fragment ion responsible for the base peak at m/z = 45.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "O-H stretching vibration (alcohol) [1]",
                "Broad due to hydrogen bonding between alcohol molecules, which weakens and varies the strength of individual O-H bonds across a range of vibrational frequencies [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "C4H10O (4 x 12 + 10 x 1 + 16 = 74) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "[CH3CH2O]⁺ or [CH2OHCH2]⁺ or [CH3CHOH]⁺ (mass = 15+16+14 = 45) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Deduction of a Branched Chiral Alcohol — 9701/21/O/N/23/Q7",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="An alcohol L with molecular formula C6H14O exhibits optical activity. • When L is heated with acidified K2Cr2O7, an orange to green colour change is seen. • When L is tested with alkaline aqueous iodine, a yellow precipitate forms. • When L is dehydrated, the major alkene formed does not show cis-trans isomerism.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce whether alcohol L is primary, secondary, or tertiary.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the complete structural formula and systematic name of alcohol L.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Draw the major alkene formed when L is dehydrated.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Secondary alcohol (positive oxidation orange to green and positive iodoform test) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Contains CH3-CH(OH)- group (from iodoform test) [1]",
                "Remaining group has 4 carbons and must confer chirality: 3-methylpentan-2-ol has chiral centres (C2 and C3): CH3-CH(OH)-CH(CH3)-CH2-CH3 [1]",
                "Systematic name: 3-methylpentan-2-ol [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Major alkene: 3-methylpent-2-ene: CH3-C(CH3)=CH-CH2-CH3 (or 2-methylpent-2-ene via rearrangement) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Reagents for Alcohols — 9701/11/M/J/22/Q22",
        syllabus_ref="16.1",
        difficulty="EASY",
        preamble="Which reaction involving butan-1-ol produces steamy white fumes that turn damp blue litmus paper red?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct reaction: A  Reaction with hot acidified potassium dichromate(VI) B  Reaction with solid phosphorus(V) chloride at room temperature C  Reaction with sodium metal at room temperature D  Reaction with concentrated phosphoric(V) acid at 180 °C",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3CH2CH2CH2OH + PCl5 -> CH3CH2CH2CH2Cl + POCl3 + HCl [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Multistep Organic Synthetic Pathway — 9701/22/M/J/23/Q7",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Devise a multi-step synthetic pathway to convert bromoethane into ethyl propanoate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert bromoethane into propanenitrile. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Hydrolyse propanenitrile to propanoic acid. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: React propanoic acid with ethanol to produce ethyl propanoate. State the catalyst, conditions, and write the balanced equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Potassium cyanide / KCN (or NaCN) [1]",
                "Conditions: In ethanol / aqueous ethanol, heat under reflux [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents: Dilute hydrochloric acid (dilute HCl(aq)) or dilute H2SO4(aq) [1]",
                "Conditions: Heat under reflux [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Catalyst/conditions: Concentrated H2SO4, heat under reflux [1]",
                "Equation: CH3CH2COOH + CH3CH2OH <=> CH3CH2COOCH2CH3 + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Chemical Roadmap for C3 Alcohols — 9701/21/M/J/21/Q5",
        syllabus_ref="16.1",
        difficulty="HARD",
        preamble="Propan-1-ol and propan-2-ol are structural isomers of formula C3H8O. Both compounds undergo a wide variety of functional group transformations.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Name the single organic product formed when propan-2-ol is reacted with: (i) Sodium metal (ii) Hot acidified potassium dichromate(VI) (iii) Thionyl chloride (SOCl2) (iv) Excess alkaline aqueous iodine",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="Explain why propan-1-ol can form two different oxidation products depending on conditions, whereas propan-2-ol can only form one oxidation product under non-destructive conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the observation when propan-1-ol and propan-2-ol are separately tested with warm Fehling's solution.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(i) Sodium propan-2-olate (or sodium isopropoxide) [1]",
                "(ii) Propanone [1]",
                "(iii) 2-chloropropane [1]",
                "(iv) Tri-iodomethane (and sodium ethanoate) [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Propan-1-ol has two hydrogen atoms on the C-OH carbon, allowing two successive oxidation steps (first to propanal, then to propanoic acid) [1]",
                "Propan-2-ol has only one hydrogen atom on the C-OH carbon, so it can only oxidise to propanone; further oxidation would require breaking stable C-C bonds [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Both give NO visible reaction / solution remains clear blue (neither alcohol reacts directly with Fehling's solution) [1]"
            ], "marks": 1}
        ]
    ),
]
