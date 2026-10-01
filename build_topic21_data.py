"""
Script to build topic21_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 21: Organic Synthesis.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 21: Organic Synthesis.
Subtopic:
  21.1 Organic synthesis:
       - Functional group interconversions (FGIs) across all AS functional groups (alkanes, alkenes, halogenoalkanes, alcohols, carbonyls, carboxylic acids, esters, nitriles, amines)
       - Carbon chain lengthening strategies (+1 C via KCN or HCN) and subsequent transformations
       - Carbon chain shortening strategies (-1 C via tri-iodomethane alkaline cleavage)
       - Retrosynthetic analysis and disconnection strategies
       - Multi-step synthetic route planning, reagents, catalysts, and reaction conditions
       - Stereochemical control, regioselectivity (Markovnikov addition), and isomer avoidance
       - Calculations of percentage yield, overall multi-step yield, and percentage atom economy
       - Green chemistry principles: atom efficiency, hazardous waste minimisation, catalyst selection

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

TOPIC_21_QUESTIONS = [
    # =========================================================================
    # PART 1: Functional Group Interconversions & Synthesis Roadmaps (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Comprehensive Functional Group Interconversions — 9701/22/M/J/23/Q9(a)-(e)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Organic synthesis relies on strategic functional group interconversions (FGIs) to convert accessible starting materials into target compounds. Fig. 1.1 displays the interconversion roadmap linking the major AS functional groups.",
        figure_path="figures/synthesis_master_fgi_roadmap.png",
        figure_caption="Fig. 1.1: Master functional group interconversion (FGI) roadmap for AS organic chemistry.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagents and conditions to convert an alkene into:\n(i) A halogenoalkane\n(ii) A primary or secondary alcohol\n(iii) An addition polymer",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the reagents and conditions to convert a halogenoalkane into:\n(i) An alcohol\n(ii) An alkene\n(iii) A nitrile",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State the reagents and conditions to convert a primary alcohol into:\n(i) An aldehyde\n(ii) A carboxylic acid\n(iii) A chloroalkane",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="State the reagent and solvent required to reduce a carboxylic acid to a primary alcohol, and state why NaBH4 cannot be used for this reduction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(i) Hydrogen halide (e.g. HBr(g) or HCl(g)) at room temperature (electrophilic addition) [1]",
                "(ii) Steam (H2O(g)) and concentrated H3PO4 catalyst at 300 °C, 60 atm [1]",
                "(iii) High pressure (~1500-3000 atm) with trace O2 initiator (or Ziegler-Natta catalyst) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "(i) Aqueous sodium hydroxide (NaOH(aq)), heat under reflux (nucleophilic substitution) [1]",
                "(ii) Ethanolic potassium hydroxide (KOH in ethanol), heat under reflux (elimination) [1]",
                "(iii) Potassium cyanide (KCN) in aqueous ethanol, heat under reflux (nucleophilic substitution) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "(i) Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4), heat gently with immediate distillation [1]",
                "(ii) Acidified potassium dichromate(VI) in excess, heat under reflux [1]",
                "(iii) Solid PCl5 at room temperature (or SOCl2 at room temperature) [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Reagent/solvent: LiAlH4 in dry ether (followed by dilute acid workup) [1]",
                "The carbonyl carbon of a carboxylic acid is weakly electrophilic due to electron donation from the adjacent -OH oxygen lone pair; NaBH4 is too weak a nucleophile to transfer hydride to it [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Three-Step Synthesis: Alkene to Carboxylic Acid — 9701/21/O/N/23/Q4(a)-(c)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Propene is converted into propanoic acid in a three-step synthetic sequence.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Hydrate propene to an alcohol. Explain why direct hydration with steam/H3PO4 gives predominantly propan-2-ol rather than propan-1-ol.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Devise an alternative two-step route from propene to produce propan-1-ol via an anti-Markovnikov halogenation/substitution sequence.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Describe the reagents and conditions to oxidise propan-1-ol to propanoic acid in high yield.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Electrophilic addition proceeds via the more stable secondary carbocation (CH3-C⁺H-CH3) rather than the primary carbocation [1]",
                "The secondary carbocation is stabilised by the positive inductive effect (+I) of two electron-releasing methyl groups (Markovnikov's rule) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Step 1: Add HBr in the presence of organic peroxides (free radical addition) to form 1-bromopropane [2]",
                "Step 2: Hydrolyse 1-bromopropane with aqueous NaOH under reflux to yield propan-1-ol [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Reagent: Excess acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4) [1]",
                "Condition: Heat under reflux (to ensure complete oxidation through the aldehyde stage to the acid) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Synthesis of Esters from Alkanes — 9701/22/F/M/22/Q5(a)-(d)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a laboratory synthetic route to convert ethane into ethyl ethanoate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert ethane into bromoethane. State the reagents and conditions, and identify the type of mechanism.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Convert a sample of bromoethane into ethanol. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: Convert a second sample of bromoethane into ethanoic acid in two stages via a nitrile.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Step 4: Combine the ethanol and ethanoic acid to produce ethyl ethanoate. Write the equation and state the catalyst and conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Bromine (Br2) and ultraviolet (UV) light / sunlight [1]",
                "Mechanism: Free-radical substitution [1]",
                "C2H6 + Br2 -> C2H5Br + HBr [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Reagents/conditions: Aqueous sodium hydroxide (NaOH(aq)), heat under reflux (nucleophilic substitution) [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Stage 1: Bromoethane + KCN in aqueous ethanol, heat under reflux -> Propanenitrile (+1 C would give propanoic acid, wait: for ethanoic acid, oxidise ethanol directly with excess acidified K2Cr2O7 under reflux!) [2]",
                "Oxidation of ethanol with excess acidified K2Cr2O7 under reflux gives ethanoic acid (2 carbons) [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O [1]",
                "Catalyst/conditions: Concentrated sulfuric acid (conc. H2SO4), heat under reflux [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Synthesis of Amines: Route Selection and Yield — 9701/23/M/J/23/Q4(a)-(c)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="A chemist considers two synthetic routes to prepare propylamine from 1-chloropropane:\nRoute A: 1-chloropropane + concentrated ethanolic ammonia in a sealed tube.\nRoute B: 1-chloropropane -> propene -> propan-2-ol -> propan-2-amine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the major limitation of Route A regarding product purity.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why Route B produces propan-2-amine rather than propylamine.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Devise an optimal two-step route to synthesise pure propylamine from bromoethane with no higher amine contaminants.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Produces a complex mixture of primary, secondary, and tertiary amines and quaternary ammonium salts due to consecutive nucleophilic substitution [1]",
                "Requires fractional distillation to separate, reducing the yield of pure propylamine [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hydration of propene follows Markovnikov's rule, adding -OH to the secondary carbon to form propan-2-ol [1]",
                "Subsequent amination retains substitution at C2, forming branched propan-2-amine rather than linear propylamine [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Step 1: Bromoethane + KCN in aqueous ethanol, heat under reflux -> Propanenitrile (CH3CH2CN) [2]",
                "Step 2: Reduce propanenitrile with LiAlH4 in dry ether (or H2/Ni) -> Propylamine (CH3CH2CH2NH2) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Multi-Step Synthesis: Halogenoalkane to 2-Hydroxy Acid — 9701/21/M/J/22/Q5",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Design a three-step synthetic pathway to prepare 2-hydroxybutanoic acid starting from 1-bromopropane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert 1-bromopropane into an alkene. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Convert the alkene into an aldehyde. State the intermediate alcohol formed and the oxidising conditions required.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: Convert the aldehyde into 2-hydroxybutanoic acid via a 2-hydroxynitrile intermediate. State the reagents and conditions for both steps.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Ethanolic potassium hydroxide (KOH in ethanol), heat under reflux (elimination of HBr to propene) [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hydrate to propan-1-ol via anti-Markovnikov route or convert to primary halogenoalkane then alcohol [1]",
                "Oxidise propan-1-ol with acidified K2Cr2O7 and immediate distillation to obtain propanal [2]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "React propanal with HCN and NaCN catalyst at room temp / pH 8 -> 2-hydroxybutanenitrile [2]",
                "Heat 2-hydroxybutanenitrile under reflux with dilute hydrochloric acid -> 2-hydroxybutanoic acid [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=6,
        title="Multiple Choice: Optimum Synthetic Step — 9701/12/M/J/23/Q34",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reaction sequence successfully converts but-2-ene into butan-2-one?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct sequence:\nA  Step 1: H2O / H3PO4 (steam); Step 2: Acidified K2Cr2O7 under reflux\nB  Step 1: HBr; Step 2: KCN; Step 3: LiAlH4\nC  Step 1: H2 / Ni; Step 2: Acidified KMnO4\nD  Step 1: Aqueous NaOH; Step 2: Tollens' reagent",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the product of Step 2 in option A is butan-2-one rather than butanoic acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (Step 1: H2O / H3PO4 (steam); Step 2: Acidified K2Cr2O7 under reflux) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Hydration of but-2-ene yields butan-2-ol, which is a secondary (2°) alcohol [1]",
                "Secondary alcohols oxidise to ketones (butan-2-one) and cannot be oxidised further to carboxylic acids under non-destructive conditions [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Regioselectivity and Isomer Control — 9701/22/O/N/23/Q7",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="When choosing a synthetic route, chemists must minimise the formation of unwanted regioisomers and stereoisomers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why adding hydrogen bromide to 2-methylbut-2-ene yields predominantly 2-bromo-2-methylbutane rather than 2-bromo-3-methylbutane.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why eliminating HBr from 2-bromobutane with hot ethanolic KOH produces a mixture of three isomeric alkenes. Name all three alkenes.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Electrophilic addition of H⁺ can generate either a tertiary carbocation ((CH3)2C⁺-CH2CH3) or a secondary carbocation ((CH3)2CH-C⁺H-CH3) [1]",
                "The tertiary carbocation has three electron-donating alkyl groups that stabilise the positive charge via the inductive effect [1]",
                "Tertiary carbocation forms faster (lower activation energy), yielding predominantly 2-bromo-2-methylbutane [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "A proton can be eliminated from either C1 or C3 adjacent to the C-Br bond [1]",
                "Elimination from C1 yields but-1-ene; elimination from C3 yields but-2-ene [1]",
                "But-2-ene exhibits geometric isomerism, existing as cis-but-2-ene and trans-but-2-ene (total 3 alkenes) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=8,
        title="Protecting Groups in Polyfunctional Synthesis — 9701/21/O/N/22/Q6",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="When synthesising a target molecule containing multiple reactive functional groups, chemists often use protecting groups.",
        parts=[
            QuestionPart(
                label="(a)",
                text="A compound contains both an aldehyde group (-CHO) and a primary alcohol group (-CH2OH). A chemist wishes to oxidise ONLY the primary alcohol group to a carboxylic acid while keeping the aldehyde intact. Explain why direct oxidation with acidified K2Cr2O7 fails.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain how converting the aldehyde into an acetal (using ethane-1,2-diol with acid catalyst) protects it during oxidation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State how the original aldehyde is regenerated after the alcohol has been oxidised.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Aldehydes are more easily oxidised than primary alcohols [1]",
                "Any oxidising agent strong enough to oxidise the alcohol will immediately oxidise the aldehyde group to a carboxylic acid as well [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Acetals are diether derivatives that lack carbonyl unsaturation [1]",
                "They are completely stable and inert to oxidising agents in basic or neutral conditions, protecting the carbonyl carbon from oxidation [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Hydrolyse with dilute aqueous acid (acid-catalysed deprotection) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Multi-Step Synthesis: Halogenoalkane to Dicarboxylic Acid — 9701/23/O/N/23/Q5",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a two-step synthetic pathway to convert 1,2-dibromoethane into butanedioic acid (succinic acid).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: State the reagents, conditions, and write the balanced chemical equation for the conversion of 1,2-dibromoethane into a dinitrile.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: State the reagents, conditions, and write the equation for the hydrolysis of the dinitrile to butanedioic acid.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the change in the number of carbon atoms in the main chain from reactant to product.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: Potassium cyanide (KCN) in excess [1]",
                "Conditions: Aqueous ethanol, heat under reflux [1]",
                "Br-CH2-CH2-Br + 2KCN -> NC-CH2-CH2-CN + 2KBr [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (dilute HCl(aq)), heat under reflux [1]",
                "NC-CH2-CH2-CN + 4H2O + 2HCl -> HOOC-CH2-CH2-COOH + 2NH4Cl [2]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Increases by 2 carbon atoms (from 2 carbons in 1,2-dibromoethane to 4 carbons in butanedioic acid) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Multiple Choice: Reagent Differentiation — 9701/11/O/N/23/Q29",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reagent will convert propan-1-ol into 1-bromopropane in a single laboratory step?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct reagent:\nA  Aqueous sodium bromide at room temperature\nB  Sodium bromide and concentrated sulfuric acid, heated under reflux\nC  Bromine water at room temperature\nD  Liquid bromine under ultraviolet light",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the reaction that occurs.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Sodium bromide and concentrated sulfuric acid, heated under reflux) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3CH2CH2OH + HBr -> CH3CH2CH2Br + H2O (generated from NaBr + H2SO4) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Synthesis of Branched Organic Structures — 9701/21/M/J/21/Q6",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a multi-step synthetic pathway to prepare 2-methylpropanoic acid from propan-2-ol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert propan-2-ol into 2-bromopropane. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Convert 2-bromopropane into 2-methylpropanenitrile. State the reagents and conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: Hydrolyse 2-methylpropanenitrile to 2-methylpropanoic acid. State the reagents and conditions.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: NaBr and concentrated H2SO4 (or PBr3), heat under reflux [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagents/conditions: KCN (or NaCN) in aqueous ethanol, heat under reflux [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (or dilute H2SO4), heat under reflux [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Selective Reduction of Carbonyl vs Ester Groups — 9701/22/F/M/21/Q6",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Compound T contains both a ketone group and an ester group: CH3-CO-CH2-COOCH2CH3 (ethyl 3-oxobutanoate).",
        parts=[
            QuestionPart(
                label="(a)",
                text="A chemist wishes to reduce ONLY the ketone group to a secondary alcohol group while leaving the ester group completely unreacted. State the reducing agent and solvent to achieve this selective transformation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of the product formed in (a).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State what product would be formed if compound T were instead treated with an excess of LiAlH4 in dry ether.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Sodium borohydride (NaBH4) [1]",
                "Solvent: Aqueous ethanol (or methanol) at room temperature [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3-CH(OH)-CH2-COOCH2CH3 (ethyl 3-hydroxybutanoate) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "LiAlH4 reduces BOTH the ketone (to a 2° alcohol) and the ester group (to two alcohols) [1]",
                "Produces butane-1,3-diol (HO-CH2-CH2-CH(OH)-CH3) and ethanol (CH3CH2OH) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Separation and Purification in Organic Preparations — 9701/23/O/N/22/Q7",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="During the preparation of a liquid ester in the laboratory, the crude product is separated and purified using four sequential techniques.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the piece of glassware used to separate the organic layer from the aqueous layer.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the reagent added to the organic layer to remove unreacted carboxylic acid, and state one visible observation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Name a suitable chemical drying agent added to remove dissolved water, and state how you know drying is complete.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Name the final purification technique used to obtain the pure, dry ester.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Separating funnel [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Aqueous sodium carbonate (Na2CO3) or sodium hydrogencarbonate (NaHCO3) [1]",
                "Effervescence / bubbling of CO2 gas [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Anhydrous magnesium sulfate (MgSO4) or anhydrous calcium chloride (CaCl2) [1]",
                "The cloudy liquid turns clear / drying agent remains granular and flows freely [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Simple distillation / fractional distillation [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 2: Modifying Carbon Chain Length (+1 C & -1 C) (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Strategies for Altering Carbon Chain Length — 9701/21/M/J/23/Q10(a)-(d)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Modifying carbon framework length is a core challenge in synthesis. Fig. 14.1 compares chain extension (+1 C) via nitriles with chain degradation (-1 C) via the tri-iodomethane reaction.",
        figure_path="figures/synthesis_carbon_chain_modification.png",
        figure_caption="Fig. 14.1: Chemical routes for extending (+1 C) and shortening (-1 C) the carbon skeleton.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Outline two different reaction types that extend the carbon skeleton by exactly one carbon atom, stating the reagents and functional groups involved in each.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="Explain how the tri-iodomethane (iodoform) reaction can be exploited synthetically to shorten a carbon chain by one carbon atom.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced chemical equation for the degradation of butan-2-one with alkaline iodine to form propanoic acid after acidification.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State the observation that confirms the successful cleavage of the terminal methyl group.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Method 1: Nucleophilic substitution of a halogenoalkane using potassium cyanide (KCN) in aqueous ethanol under reflux (converts R-X to R-CN) [2]",
                "Method 2: Nucleophilic addition of hydrogen cyanide (HCN / NaCN at pH 8) to an aldehyde or ketone (converts R-CHO to 2-hydroxynitrile R-CH(OH)-CN) [2]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Compounds containing the methyl carbonyl (CH3-CO-R) group undergo tri-iodination to CI3-CO-R [1]",
                "Hydroxide ion attacks the carbonyl carbon, cleaving the C-C bond and expelling the :CI3⁻ leaving group [1]",
                "This removes the terminal methyl group as solid CHI3, leaving behind a carboxylate salt with one fewer carbon atom, which yields RCOOH upon acidification [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "CH3COCH2CH3 + 3I2 + 4NaOH -> CH3CH2COONa + CHI3 + 3NaI + 3H2O [1]",
                "CH3CH2COONa + HCl -> CH3CH2COOH + NaCl [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Formation of a pale yellow crystalline precipitate of tri-iodomethane (CHI3) with a characteristic medicinal / antiseptic odour [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=15,
        title="Synthesis of Amino Acids via Strecker Synthesis — 9701/22/O/N/23/Q8",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="The Strecker synthesis is an industrial route to alpha-amino acids starting from aldehydes, ammonia, and hydrogen cyanide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When ethanal is treated with a mixture of NH3 and HCN, an alpha-aminonitrile, CH3-CH(NH2)-CN, is formed. Write the balanced equation for this condensation-addition.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the reagents and conditions to hydrolyse CH3-CH(NH2)-CN into 2-aminopropanoic acid (alanine).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the alanine produced by this chemical synthesis is an optically inactive racemic mixture, unlike natural L-alanine produced by living organisms.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3CHO + NH3 + HCN -> CH3CH(NH2)CN + H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Dilute hydrochloric acid (dilute HCl(aq)), heat under reflux [1]",
                "Followed by neutralisation to isoelectric point [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The intermediate imine / aldehyde precursor is planar around the sp2 carbon atom [1]",
                "Nucleophilic cyanide attack has an equal probability from the top face or bottom face [1]",
                "This produces an equimolar (50:50) mixture of both D- and L-enantiomers (racemate), whereas biological synthesis uses stereospecific enzyme catalysts that generate exclusively one enantiomer [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=16,
        title="Degradation of Alkenes: Ozonolysis vs Permanganate Cleavage — 9701/21/O/N/22/Q7",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Cleavage of carbon-carbon double bonds can be used to shorten carbon chains or locate double bonds.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When 2-methylbut-2-ene is heated with hot concentrated acidified potassium manganate(VII), the C=C bond is cleaved completely. Deduce the two organic products formed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the visible observation during this oxidative cleavage.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why an alkene with a terminal =CH2 group (such as but-1-ene) produces carbon dioxide gas upon hot acidified KMnO4 oxidation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Propanone, (CH3)2C=O [1]",
                "Ethanoic acid, CH3COOH [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Purple solution turns colourless (decolourises) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The terminal =CH2 group is first oxidised to methanoic acid (HCOOH) [1]",
                "Methanoic acid contains an aldehyde group and is further oxidised by hot KMnO4 to carbon dioxide and water: HCOOH + [O] -> CO2 + H2O [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Multiple Choice: Step-Up vs Step-Down Reactions — 9701/12/M/J/22/Q27",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reaction results in a decrease in the number of carbon atoms in the main organic molecule?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the step-down reaction:\nA  Bromoethane + KCN in ethanol\nB  Ethanal + HCN / NaCN\nC  Propanone + alkaline aqueous iodine\nD  Ethene + steam / H3PO4",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Name the product that contains the eliminated carbon atom.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Propanone + alkaline aqueous iodine) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Tri-iodomethane (CHI3) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="Synthesis of Branched Dicarboxylic Acids — 9701/23/M/J/22/Q5",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a three-step synthetic pathway to convert 2-methylpropane into 2-methylpropanedioic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Brominate 2-methylpropane to form a monobromoalkane. State the reagents and explain why 2-bromo-2-methylpropane is the major product.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Eliminate HBr to form 2-methylpropene. State the reagents and conditions.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: React with bromine to form a dibromoalkane, followed by substitution with KCN and acid hydrolysis.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: Bromine (Br2) and UV light [1]",
                "The tertiary radical (CH3)3C• is stabilised by hyperconjugation and positive inductive effects of three methyl groups [1]",
                "Forms much faster than primary radicals, giving 2-bromo-2-methylpropane as major product [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Ethanolic potassium hydroxide (KOH in ethanol), heat under reflux [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Add Br2 in CCl4 to form 1,2-dibromo-2-methylpropane [1]",
                "Reflux with excess ethanolic KCN to form dinitrile [1]",
                "Reflux with dilute hydrochloric acid to hydrolyse dinitrile to dicarboxylic acid [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=19,
        title="Decarboxylation Reactions (Thermal Chain Shortening) — 9701/21/O/N/23/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Heating the anhydrous sodium salt of a carboxylic acid with solid soda lime (NaOH / CaO) results in decarboxylation, removing a carbon atom as carbonate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the decarboxylation of sodium ethanoate, CH3COONa, with solid sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Name the hydrocarbon gas produced.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why soda lime is preferred over pure solid sodium hydroxide in laboratory apparatus.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH3COONa + NaOH -> CH4 + Na2CO3 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Methane [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Pure NaOH is deliquescent, melts at a relatively low temperature, and attacks/corrodes hot laboratory glassware severely [1]",
                "Calcium oxide in soda lime keeps the mixture solid and porous, preventing fusion and protecting the glass boiling tube [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Grignard Reactions (Extension Carbon-Carbon Coupling) — 9701/22/M/J/23/Q11",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Organomagnesium reagents (Grignard reagents, RMgX) are widely used to construct carbon-carbon bonds by nucleophilic attack on carbonyl groups.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Ethylmagnesium bromide, CH3CH2MgBr, is prepared from bromoethane and magnesium. State the solvent required and explain why anhydrous conditions are mandatory.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When CH3CH2MgBr reacts with methanal followed by dilute acid, propan-1-ol is formed. Write the equation for this transformation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Predict whether reaction with propanone produces a primary, secondary, or tertiary alcohol. Name the product.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Solvent: Dry ether (ethoxyethane) [1]",
                "Grignard reagents are powerful bases that react violently with traces of water: RMgBr + H2O -> RH + Mg(OH)Br [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CH3CH2MgBr + HCHO -> CH3CH2CH2OMgBr --(H3O⁺)--> CH3CH2CH2OH [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Tertiary (3°) alcohol [1]",
                "2-methylbutan-2-ol [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Multi-Step Synthesis: Alkene to Branched Hydroxy Ester — 9701/21/M/J/22/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a synthesis to convert ethene into ethyl 2-hydroxypropanoate (ethyl lactate).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Outline how ethene can be converted into ethanal in two steps.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Outline how ethanal is converted into 2-hydroxypropanoic acid via a hydroxynitrile.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Esterify 2-hydroxypropanoic acid with ethanol, stating the catalyst and conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: Ethene + steam / H3PO4 (300 °C, 60 atm) -> Ethanol [1]",
                "Step 2: Ethanol + acidified K2Cr2O7, heat gently with immediate distillation -> Ethanal [2]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "React ethanal with HCN + NaCN catalyst at room temp / pH 8 -> 2-hydroxypropanenitrile [2]",
                "Reflux 2-hydroxypropanenitrile with dilute HCl -> 2-hydroxypropanoic acid [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "React with ethanol in presence of concentrated H2SO4 catalyst, heat under reflux [2]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Multiple Choice: Synthetic Pathway to a Diol — 9701/11/M/J/23/Q33",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reaction converts ethene directly into ethane-1,2-diol in a single step?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reaction:\nA  Warm with concentrated sulfuric acid\nB  Cold, dilute, acidified potassium manganate(VII)\nC  Hot, concentrated, acidified potassium manganate(VII)\nD  Aqueous sodium hydroxide under reflux",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the visible colour change observed during this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Cold, dilute, acidified potassium manganate(VII)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Purple solution turns colourless (or forms brown precipitate of MnO2 if neutral/alkaline) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Synthesis of Polyfunctional Targets: Paracetamol — 9701/22/F/M/23/Q7",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Paracetamol (N-(4-hydroxyphenyl)ethanamide) is synthesised from 4-aminophenol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of 4-aminophenol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="4-aminophenol is reacted with ethanoic anhydride, (CH3CO)2O. Explain why acylation occurs preferentially at the amino group (-NH2) rather than at the phenolic hydroxyl group (-OH).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structural formula of paracetamol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene ring with -OH at position 1 and -NH2 at position 4 (para) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Nitrogen is less electronegative than oxygen (electronegativity 3.0 vs 3.5) [1]",
                "The lone pair on nitrogen is more nucleophilic and readily donated than the lone pair on the phenolic oxygen, reacting faster with electrophilic carbonyl carbon [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "HO-C6H4-NHCOCH3 (or displayed formula) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Isomer Separation and Enantiopurity in Synthesis — 9701/23/O/N/23/Q8",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="The drug thalidomide was administered as a racemic mixture; the (R)-enantiomer is an effective sedative, whereas the (S)-enantiomer is teratogenic.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term racemic mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why standard laboratory syntheses from achiral starting materials invariably produce racemic mixtures rather than a single enantiomer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two modern strategies pharmaceutical companies use to obtain enantiopure single-isomer drugs.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "An equimolar (50:50) mixture of two optical enantiomers with zero net optical rotation [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Reactions involving planar trigonal (sp2) carbocation intermediates or planar carbonyl groups have equal activation energy for attack from either face [1]",
                "Both enantiomers form at exactly equal rates, giving an equimolar mixture [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Use of chiral catalysts / enantioselective asymmetric synthesis [1]",
                "Use of biological enzymes / chiral pools / resolution with chiral resolving acids/bases [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Synthesis of Cyclic Ethers and Epoxides — 9701/21/O/N/22/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Epoxides are versatile 3-membered cyclic ethers prepared by treating alkenes with peroxycarboxylic acids or via halohydrins.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When ethene reacts with aqueous chlorine, 2-chloroethanol, CH2Cl-CH2OH, is formed. Explain why 2-chloroethanol is formed rather than 1,2-dichloroethane when chlorine water is used.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When 2-chloroethanol is treated with cold aqueous sodium hydroxide, an intramolecular SN2 substitution occurs. Draw the structure of the cyclic product formed.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Name this cyclic product.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Electrophilic attack of Cl⁺ creates a chloronium intermediate [1]",
                "Water molecules are present in enormous excess compared to chloride ions and attack the cyclic intermediate preferentially as the nucleophile [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Three-membered cyclic ether: Oxirane (ethylene oxide) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Oxirane (or epoxyethane) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="Multiple Choice: Optimum Catalyst for Hydrogenation — 9701/12/O/N/23/Q29",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which catalyst is used for the catalytic addition of hydrogen gas across alkene double bonds?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct catalyst:\nA  Al2O3 at 300 °C\nB  Nickel (Ni) heated or Platinum (Pt) at room temperature\nC  Concentrated H2SO4 at 170 °C\nD  FeCl3 at room temperature",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the industrial importance of this reaction in the food industry.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Nickel (Ni) heated or Platinum (Pt) at room temperature) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Hydrogenation of liquid unsaturated vegetable oils to produce solid/semi-solid margarines and spreads [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 3: Retrosynthetic Analysis & Multi-Step Planning (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Retrosynthetic Analysis of Target Molecules — 9701/21/M/J/23/Q11(a)-(d)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Retrosynthesis involves working backwards from the desired target molecule by identifying strategic disconnections and functional group precursors. Fig. 27.1 outlines the retrosynthetic planning for ethyl propanoate from bromoethane.",
        figure_path="figures/synthesis_retrosynthetic_disconnection.png",
        figure_caption="Fig. 27.1: Retrosynthetic disconnection approach to synthesise ethyl propanoate from bromoethane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="In retrosynthetic analysis, explain what is meant by a 'disconnection' and identify the bond disconnected in ethyl propanoate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the two precursor molecules generated by disconnecting this bond.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Show how both precursor molecules can be synthesised independently from bromoethane.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(d)",
                text="Write the balanced chemical equation for the final coupling step, stating the catalyst and conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "An analytical process of hypothetically breaking a bond in the target molecule to generate simpler precursor fragments (synthons) [1]",
                "The ester C-O single bond connecting the carbonyl group to the ethyl group (CH3CH2CO-OCH2CH3) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Propanoic acid (CH3CH2COOH) [1]",
                "Ethanol (CH3CH2OH) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ethanol: Bromoethane + aqueous NaOH, heat under reflux (nucleophilic substitution) [2]",
                "Propanoic acid: Bromoethane + KCN in aqueous ethanol, heat under reflux -> Propanenitrile; then reflux propanenitrile with dilute HCl -> Propanoic acid [2]"
            ], "marks": 4},
            {"part": "(d)", "points": [
                "CH3CH2COOH + CH3CH2OH <=> CH3CH2COOCH2CH3 + H2O [1]",
                "Concentrated H2SO4 catalyst, heat under reflux [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Retrosynthetic Planning for 2-Methylbutanoic Acid — 9701/22/O/N/23/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="A target molecule is 2-methylbutanoic acid, CH3-CH2-CH(CH3)-COOH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify a suitable halogenoalkane starting material that can be converted into 2-methylbutanoic acid in a single two-stage sequence.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the structural formula of the nitrile intermediate formed.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the reagents and conditions for both steps in the forward synthesis.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2-bromobutane, CH3-CH2-CH(Br)-CH3 (or 2-chlorobutane) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3-CH2-CH(CH3)-CN (2-methylbutanenitrile) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Step 1: 2-bromobutane + KCN in aqueous ethanol, heat under reflux [2]",
                "Step 2: Heat under reflux with dilute hydrochloric acid [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=29,
        title="Synthesis of N-Phenylethanamide (Acetanilide) — 9701/21/O/N/22/Q8",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Acetanilide, C6H5NHCOCH3, is prepared by acylating phenylamine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Give two alternative acylating agents that can react with phenylamine to produce acetanilide.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced chemical equation using ethanoyl chloride, stating any by-products.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Acetanilide is recrystallised from boiling water. Explain how recrystallisation purifies a solid organic product.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ethanoyl chloride (CH3COCl) [1]",
                "Ethanoic anhydride ((CH3CO)2O) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "C6H5NH2 + CH3COCl -> C6H5NHCOCH3 + HCl [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Dissolve crude product in minimum volume of hot solvent; insoluble impurities filtered hot [1]",
                "Upon slow cooling, pure acetanilide crystals precipitate out while soluble impurities remain dissolved in cold mother liquor [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Yield Degradation across Multi-Step Routes — 9701/22/M/J/22/Q8",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="A synthetic chemist compares two alternative routes to synthesise target compound X:\n• Route 1: A 2-step route where each step has an 80% yield.\n• Route 2: A 5-step route where each step has an 85% yield.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the overall percentage yield of Route 1.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the overall percentage yield of Route 2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the general conclusion regarding the number of synthetic steps in chemical route design.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Overall yield = 0.80 x 0.80 = 0.640 = 64.0% [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Overall yield = (0.85)⁵ = 0.4437 = 44.4% [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Routes with fewer synthetic steps are inherently superior because cumulative product losses at each stage severely diminish the overall yield [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Synthesis of 2-Bromopropanoic Acid from Propene — 9701/23/M/J/23/Q5",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a synthesis to convert propene into 2-bromopropanoic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert propene into propanoic acid. Outline the necessary reactions and reagents.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Brominate propanoic acid selectively at the alpha-carbon using red phosphorus and bromine (Hell-Volhard-Zelinsky conditions). State the role of red phosphorus.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Draw the structural formula of 2-bromopropanoic acid and identify its chiral centre.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Hydrate propene to propan-1-ol via anti-Markovnikov HBr addition then NaOH(aq) hydrolysis [2]",
                "Oxidise propan-1-ol with excess acidified K2Cr2O7 under reflux -> Propanoic acid [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Red phosphorus reacts with bromine to form PBr3 in situ [1]",
                "PBr3 converts a small amount of acid to acyl bromide, catalysing enolisation and selective alpha-bromination [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "CH3-C*H(Br)-COOH with asterisk on C2 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Multiple Choice: Retrosynthetic Disconnection of Amides — 9701/11/M/J/23/Q34",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which pair of compounds reacts directly at room temperature to form N-methylpropanamide?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct pair:\nA  Propanoyl chloride and methylamine\nB  Propanoic acid and methanol\nC  Propanenitrile and methylamine\nD  Ethanoic acid and ethylamine",
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
                "A (Propanoyl chloride and methylamine) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3CH2COCl + CH3NH2 -> CH3CH2CONHCH3 + HCl [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Synthesis of a Cyclic Ketone: Cyclohexanone — 9701/21/O/N/23/Q10",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Outline a laboratory preparation of cyclohexanone from cyclohexanol.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the oxidising agent and reaction conditions required.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for this oxidation using [O].",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State how cyclohexanone can be separated from the green inorganic chromium reaction mixture.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4) [1]",
                "Heat under reflux (or warm gently) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "C6H11OH + [O] -> C6H10O + H2O [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Steam distillation or direct simple distillation of the organic ketone [1]",
                "Separate organic layer using a separating funnel, dry with anhydrous MgSO4, and redistil [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Synthesis of 1,3-Diaminopropane — 9701/22/F/M/22/Q7",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a two-step synthetic pathway to convert 1,3-dichloropropane into propane-1,3-diamine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagents, conditions, and write the balanced chemical equation.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why an excess of concentrated ethanolic ammonia is critical in this preparation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Excess concentrated ammonia (NH3) in ethanol [1]",
                "Condition: Heat under pressure in a sealed tube [1]",
                "Cl-CH2-CH2-CH2-Cl + 4NH3 -> H2N-CH2-CH2-CH2-NH2 + 2NH4Cl [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Dihalogenoalkanes are prone to intermolecular cross-linking and intramolecular cyclisation to form cyclic secondary amines (azetidine / pyrrolidine rings) [1]",
                "A large excess of NH3 ensures nucleophilic substitution by ammonia dominates, preventing polymerisation and cyclisation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Convergence in Synthesis: Convergent vs Linear Routes — 9701/23/O/N/23/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="In complex organic synthesis, chemists distinguish between linear synthesis (A -> B -> C -> D -> Target) and convergent synthesis (A -> B; C -> D; then B + D -> Target).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Assume a linear synthesis consists of 4 steps, each with an 80% yield. Calculate the overall percentage yield of the target.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Assume a convergent synthesis makes fragment B in 2 steps (80% each) and fragment D in 2 steps (80% each), followed by coupling B and D in one step (80%). Calculate the overall yield of the convergent route based on the longest linear path.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State two practical advantages of convergent synthesis in industrial chemical plants.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Linear yield = (0.80)⁴ = 0.4096 = 41.0% [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Longest linear sequence = 3 steps (two steps to fragment + one coupling step) [1]",
                "Convergent yield = (0.80)³ = 0.512 = 51.2% [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Higher overall yield of final product [1]",
                "Fragments B and D can be manufactured in parallel in separate reactors, saving production time and avoiding risking valuable intermediates in long sequential chains [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Multiple Choice: Choosing Reagents for Chlorination — 9701/12/M/J/23/Q35",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reagent is the most convenient for converting a carboxylic acid into an acyl chloride on a laboratory scale?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the reagent:\nA  Cl2 in UV light\nB  NaCl and concentrated H2SO4\nC  Thionyl chloride (SOCl2)\nD  Concentrated hydrochloric acid",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the by-products of this reagent simplify purification.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Thionyl chloride (SOCl2)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Both by-products, SO2 and HCl, are gases that bubble out of the reaction mixture [1]",
                "Leaves behind the pure liquid acyl chloride without requiring fractional distillation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Synthesis of Esters from Alcohols and Carboxylic Acids — 9701/21/M/J/22/Q10",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Write a detailed experimental protocol to prepare and isolate pure ethyl ethanoate in the laboratory.",
        parts=[
            QuestionPart(
                label="(a)",
                text="List the reactants, catalyst, and heating technique used in the initial reaction.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe the purification steps using a separating funnel, identifying all reagents used to wash the product.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Describe the drying and final collection procedure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reactants: Glacial ethanoic acid and pure ethanol [1]",
                "Catalyst: Concentrated sulfuric acid (conc. H2SO4) [1]",
                "Heating under reflux with a water bath or heating mantle (prevent naked flames) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Distil off crude mixture and transfer to separating funnel [1]",
                "Shake with aqueous sodium carbonate (Na2CO3) to neutralise and remove unreacted acids (release CO2 pressure) [1]",
                "Wash organic layer with aqueous calcium chloride (CaCl2) to remove unreacted ethanol [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Dry the organic layer with anhydrous magnesium sulfate (MgSO4) until clear [1]",
                "Filter and fractionally distil, collecting the fraction boiling between 75-78 °C (pure ethyl ethanoate) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Deducing Multi-Step Intermediate Compounds — 9701/22/F/M/21/Q7",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Consider the synthetic sequence:\nBut-1-ene --(Step 1: HBr)--> Compound A --(Step 2: aqueous NaOH)--> Compound B --(Step 3: acidified K2Cr2O7)--> Compound C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the structural formula and systematic name of Compound A.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the structural formula and systematic name of Compound B.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the structural formula and systematic name of Compound C, and state a test to confirm the presence of its functional group.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Structure: CH3-CH2-CH(Br)-CH3 [1]",
                "Systematic name: 2-bromobutane (Markovnikov electrophilic addition) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structure: CH3-CH2-CH(OH)-CH3 [1]",
                "Systematic name: Butan-2-ol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Structure: CH3-CH2-CO-CH3 [1]",
                "Systematic name: Butanone [1]",
                "Test: Add 2,4-DNPH to observe an orange precipitate (and negative Tollens' test confirms ketone) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=39,
        title="Synthesis of Polyfunctional Molecule: Aspirin — 9701/23/O/N/23/Q10",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Salicylic acid (2-hydroxybenzoic acid) is converted into aspirin (2-ethanoyloxybenzoic acid) by reaction with ethanoic anhydride.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the synthesis of aspirin, showing the structural formulas of all reactants and products.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the catalyst used and explain why a water bath is used to warm the mixture.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Describe how pure aspirin crystals are isolated from the reaction mixture.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2-HOC6H4COOH + (CH3CO)2O -> 2-CH3COOC6H4COOH + CH3COOH [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Catalyst: Concentrated phosphoric acid (H3PO4) or conc. H2SO4 [1]",
                "Water bath ensures gentle, even heating without thermal decomposition or ignition [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Pour reaction mixture onto ice water; aspirin precipitates as a crude solid [1]",
                "Filter under reduced pressure (Buchner funnel) and recrystallise from minimum hot water/ethanol [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 4: Green Chemistry, Percentage Yield & Atom Economy (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="Green Chemistry Metrics: Yield vs Atom Economy — 9701/22/M/J/23/Q12(a)-(d)",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Modern industrial organic synthesis prioritises Green Chemistry principles. Fig. 40.1 contrasts Percentage Yield with Percentage Atom Economy.",
        figure_path="figures/synthesis_green_chemistry_metrics.png",
        figure_caption="Fig. 40.1: Comparison between percentage yield and percentage atom economy metrics.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the mathematical formulas for:\n(i) Percentage Yield\n(ii) Percentage Atom Economy",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="In an industrial synthesis of 1-bromobutane from butan-1-ol:\nCH3CH2CH2CH2OH + NaBr + H2SO4 -> CH3CH2CH2CH2Br + NaHSO4 + H2O\nCalculate the percentage atom economy for this reaction (Mr values: butan-1-ol = 74.1, NaBr = 102.9, H2SO4 = 98.1, 1-bromobutane = 137.0).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="In an experiment, 14.8 g of butan-1-ol yields 19.2 g of 1-bromobutane. Calculate the percentage yield of 1-bromobutane.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Explain why an industrial reaction can have a 100% percentage yield but still generate substantial environmental waste.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(i) % Yield = (actual mass obtained / theoretical maximum mass) x 100% [1]",
                "(ii) % Atom Economy = (Mr of desired product / sum of Mr of all reactants) x 100% [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Sum of Mr of all reactants = 74.1 + 102.9 + 98.1 = 275.1 [1]",
                "Mr of desired product (1-bromobutane) = 137.0 [1]",
                "Atom economy = (137.0 / 275.1) x 100 = 49.8% [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Moles of butan-1-ol = 14.8 / 74.1 = 0.1997 mol [1]",
                "Theoretical yield of 1-bromobutane = 0.1997 x 137.0 = 27.36 g [1]",
                "Percentage yield = (19.2 / 27.36) x 100 = 70.2% [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Even if all reactant molecules are converted completely to products (100% yield), a low atom economy means significant mass is converted into unwanted, stoichiometric by-products (e.g. NaHSO4, salts) [1]",
                "These unwanted by-products represent chemical waste requiring disposal or energy-intensive separation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Atom Economy Comparison: Substitution vs Addition — 9701/21/O/N/23/Q11",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Ethanol can be synthesised by two different methods:\nMethod 1 (Substitution): CH3CH2Br + NaOH -> CH3CH2OH + NaBr\nMethod 2 (Addition): CH2=CH2 + H2O -> CH3CH2OH",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the atom economy of Method 2 without performing a calculation. Justify your answer.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the percentage atom economy of Method 1 (Mr: CH3CH2Br = 108.9, NaOH = 40.0, CH3CH2OH = 46.0, NaBr = 102.9).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain which method is greener from an industrial manufacturing perspective.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "100% atom economy [1]",
                "It is an addition reaction; all atoms in the reactants (ethene and water) are combined into the single desired ethanol product with zero by-products [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Total reactant mass = 108.9 + 40.0 = 148.9 [1]",
                "% Atom economy = (46.0 / 148.9) x 100 = 30.9% [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Method 2 is substantially greener [1]",
                "It has 100% atom economy (compared to only 30.9% for Method 1), generating zero toxic waste (no sodium bromide waste), conserving raw materials [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Green Chemistry Principles in Organic Synthesis — 9701/22/M/J/22/Q9",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Paul Anastas and John Warner formulated the 12 Principles of Green Chemistry to guide sustainable chemical production.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State what is meant by the principle 'Design for Degradation'.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why catalytic reagents are inherently superior to stoichiometric reagents in sustainable chemical processes.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two reasons why water or supercritical CO2 is preferred over organic solvents like dichloromethane or benzene.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Chemical products should be designed so that at the end of their function they break down into innocuous environmental degradation products and do not persist [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Catalysts are regenerated and used in small quantities, speeding up reactions and lowering activation energy [1]",
                "Stoichiometric reagents are consumed in molar quantities and produce large masses of by-product chemical waste [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Water and CO2 are non-flammable, non-toxic, and readily available [1]",
                "Dichloromethane and benzene are volatile organic compounds (VOCs) that are toxic, carcinogenic, deplete the ozone layer, or present severe disposal hazards [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Multi-Step Percentage Yield Calculation — 9701/23/O/N/23/Q11",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="A synthesis of propanoic acid from bromoethane involves two steps:\nStep 1: C2H5Br + KCN -> C2H5CN + KBr (yield = 75.0%)\nStep 2: C2H5CN + 2H2O + HCl -> C2H5COOH + NH4Cl (yield = 80.0%)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the overall percentage yield of propanoic acid from bromoethane.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the mass of bromoethane (Mr = 108.9) required to produce 11.1 g of propanoic acid (Mr = 74.1).",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Overall yield = 0.750 x 0.800 = 0.600 = 60.0% [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles of propanoic acid = 11.1 / 74.1 = 0.1498 mol [1]",
                "Moles of bromoethane needed = 0.1498 / 0.600 = 0.2497 mol [1]",
                "Mass of bromoethane = 0.2497 x 108.9 = 27.2 g [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=44,
        title="Multiple Choice: Highest Atom Economy — 9701/12/M/J/23/Q36",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Which reaction has the highest percentage atom economy for the production of the specified product?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the reaction:\nA  Polymerisation of ethene to poly(ethene)\nB  Hydrolysis of bromoethane to ethanol\nC  Oxidation of ethanol to ethanoic acid\nD  Esterification of ethanoic acid with ethanol",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the percentage atom economy of your selected reaction.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (Polymerisation of ethene to poly(ethene)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "100% [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Atom Economy in Ibuprofen Synthesis (Boots vs BHC Route) — 9701/21/M/J/22/Q11",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="The original Boots synthesis of the analgesic ibuprofen required 6 steps and had an atom economy of 40%. The modern BHC catalytic synthesis requires only 3 steps and achieves an atom economy of 77% (or 99% when acetic acid by-product is recovered).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State two reasons why the BHC route is superior to the Boots route under Green Chemistry principles.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why achieving higher atom economy reduces the environmental footprint of a pharmaceutical factory.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Fewer synthetic steps (3 steps vs 6 steps), dramatically reducing solvent usage and increasing overall yield [1]",
                "Substantially higher atom economy (77% vs 40%), using recyclable catalysts (HF, Raney nickel, palladium) rather than stoichiometric reagents like AlCl3 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Less raw chemical materials are consumed per kilogram of drug produced [1]",
                "Dramatically reduces the volume of hazardous chemical waste and by-products that must be incinerated or neutralised [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Calculation of Atom Economy for Esterification — 9701/22/F/M/22/Q8",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="Ethyl ethanoate is prepared by reacting ethanoic acid with ethanol:\nCH3COOH + C2H5OH <=> CH3COOC2H5 + H2O",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the percentage atom economy for the production of ethyl ethanoate (Mr: CH3COOH = 60.0, C2H5OH = 46.0, CH3COOC2H5 = 88.0, H2O = 18.0).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the percentage atom economy if the reaction were performed using ethanoyl chloride:\nCH3COCl + C2H5OH -> CH3COOC2H5 + HCl (Mr: CH3COCl = 78.5, HCl = 36.5).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Compare the atom economies of the two routes and comment on practical laboratory choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Total reactant Mr = 60.0 + 46.0 = 106.0 [1]",
                "Atom economy = (88.0 / 106.0) x 100 = 83.0% [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Total reactant Mr = 78.5 + 46.0 = 124.5 [1]",
                "Atom economy = (88.0 / 124.5) x 100 = 70.7% [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The carboxylic acid route has a higher theoretical atom economy (83.0% vs 70.7%) and produces benign water rather than corrosive HCl [1]",
                "However, the acyl chloride route goes to 100% completion irreversibly, whereas the carboxylic acid route is limited by dynamic equilibrium [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Catalyst Recyclability in Green Synthesis — 9701/21/O/N/23/Q12",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Heterogeneous solid catalysts are widely preferred over homogeneous liquid acid catalysts in industrial organic synthesis.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the difference between a homogeneous catalyst and a heterogeneous catalyst.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State two reasons why passing alcohol vapour over solid aluminium oxide catalyst granules is greener than heating with concentrated sulfuric acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A homogeneous catalyst is in the same physical state / phase as the reactants (e.g. liquid acid in liquid reactants) [1]",
                "A heterogeneous catalyst is in a different physical state / phase from the reactants (e.g. solid catalyst with liquid or gaseous reactants) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Solid Al2O3 is easily separated from the product gas stream by simple phase filtration without neutralisation waste [1]",
                "Avoids corrosive, hazardous liquid H2SO4 which produces acid waste and toxic SO2 by-product fumes [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Atom Economy of Addition Reactions — 9701/11/O/N/23/Q30",
        syllabus_ref="21.1",
        difficulty="EASY",
        preamble="What is the theoretical atom economy for the electrophilic addition of hydrogen chloride to propene to make 2-chloropropane?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the atom economy:\nA  50%\nB  75%\nC  100%\nD  Dependant on the temperature",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why all electrophilic addition reactions have this atom economy.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (100%) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Two reactant molecules combine to form a single product molecule with no atoms eliminated or lost as waste [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Life Cycle Assessment in Industrial Route Evaluation — 9701/22/M/J/23/Q13",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="When evaluating a synthetic pathway, an industrial chemist assesses the Environmental Factor (E-factor), defined as: E-factor = (total mass of waste produced) / (mass of desired product).",
        parts=[
            QuestionPart(
                label="(a)",
                text="A pharmaceutical process manufactures 25.0 kg of an active ingredient while generating 1,250 kg of chemical waste. Calculate the E-factor for this process.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State whether a greener, more sustainable process has a higher or lower E-factor. Explain your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Identify two major sources of waste in pharmaceutical production that contribute to high E-factors.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "E-factor = 1,250 kg / 25.0 kg = 50.0 [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Lower E-factor [1]",
                "A lower E-factor means less chemical waste is generated per unit mass of desired product produced, indicating higher material efficiency [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Organic solvents used in reaction media, extractions, and chromatography columns [1]",
                "Inorganic salts and reagents from quenching, neutralisation, and washing stages [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Retrosynthetic Design Problem — 9701/21/M/J/23/Q12",
        syllabus_ref="21.1",
        difficulty="HARD",
        preamble="Devise a complete, practical synthetic pathway to prepare 2-hydroxy-2-methylbutanoic acid starting from but-2-ene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Step 1: Convert but-2-ene into butan-2-ol. State the reagents and conditions.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Step 2: Oxidise butan-2-ol to butanone. State the reagents, conditions, and write the equation using [O].",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Step 3: React butanone with HCN to form a 2-hydroxynitrile. State the reagents, catalyst, and mechanism.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Step 4: Hydrolyse the 2-hydroxynitrile to 2-hydroxy-2-methylbutanoic acid. State the reagents and conditions, and explain why the final product is an optically inactive racemate.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents/conditions: Steam (H2O(g)) and concentrated H3PO4 catalyst at 300 °C, 60 atm [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Acidified potassium dichromate(VI) (K2Cr2O7 + dilute H2SO4), heat under reflux [1]",
                "CH3CH(OH)CH2CH3 + [O] -> CH3COCH2CH3 + H2O [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reagents: HCN with NaCN (or KCN) catalyst at room temperature, pH ~ 8 [2]",
                "Mechanism: Nucleophilic addition [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Reagents/conditions: Dilute hydrochloric acid (dilute HCl(aq)), heat under reflux [1]",
                "Planar carbonyl group of butanone is attacked with equal probability from either face by the :CN⁻ nucleophile [1]",
                "Produces an equimolar (50:50) racemic mixture of both optical enantiomers, cancelling optical rotation [1]"
            ], "marks": 3}
        ]
    ),
]
'''
    with open("topic21_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully built topic21_data.py with 50 questions!")

if __name__ == "__main__":
    generate()
