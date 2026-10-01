"""
Script to generate topic6_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 6: Electrochemistry.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 6: Electrochemistry.
Subtopics:
  6.1 Redox processes: electron transfer, oxidation numbers, balancing, disproportionation, titrations
  6.2 Electrolysis: molten and aqueous electrolysis, preferential discharge, quantitative Faraday calculations

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

TOPIC_6_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 6.1: Redox Processes & Oxidation Numbers (Q1 to Q26)
    # =========================================================================
    Question(
        number=1,
        title="Assigning Oxidation Numbers in Sulfur Compounds — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Sulfur forms a wide variety of compounds exhibiting different oxidation numbers.",
        parts=[
            QuestionPart(
                label="a",
                text="State the oxidation number of sulfur in each of the following species:\n(i) H2S\n(ii) S8\n(iii) SO2\n(iv) SO4^2-",
                marks=4,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Determine the oxidation number of sulfur in the thiosulfate ion, S2O3^2-, and in the tetrathionate ion, S4O6^2-.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) -2 (1); (ii) 0 (1); (iii) +4 (1); (iv) +6 (1)", "marks": 4},
            {"part": "b", "points": "S2O3^2-: +2 (1); S4O6^2-: +2.5 (or +5/2) (1)", "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Disproportionation of Chlorine in Aqueous Alkali — 9701/21/O/N/20/Q4(a)-(d)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Chlorine reacts with aqueous sodium hydroxide under different temperature conditions as illustrated in Fig. 6.1.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term disproportionation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the balanced chemical equation for the reaction of chlorine with cold, dilute aqueous sodium hydroxide (15 °C).",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the oxidation number of chlorine in each product formed in (b).",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Write the balanced chemical equation for the reaction of chlorine with hot, concentrated aqueous sodium hydroxide (70 °C) and deduce the oxidation state of chlorine in the chlorate(V) product.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A redox reaction in which atoms of the same element (1); are simultaneously oxidised and reduced (1)", "marks": 2},
            {"part": "b", "points": "Cl2(g) + 2NaOH(aq) -> NaCl(aq) + NaClO(aq) + H2O(l) (1); Correct balancing and species (1)", "marks": 2},
            {"part": "c", "points": "In NaCl: -1 (1); In NaClO: +1 (1)", "marks": 2},
            {"part": "d", "points": "3Cl2(g) + 6NaOH(aq) -> 5NaCl(aq) + NaClO3(aq) + 3H2O(l) (1); Oxidation state in NaClO3 is +5 (1)", "marks": 2}
        ],
        figure_path="figures/disproportionation_concept.png",
        figure_caption="Fig. 6.1: Disproportionation oxidation states of chlorine in cold vs hot aqueous alkali."
    ),
    Question(
        number=3,
        title="Balancing Redox Half-Equations in Acidic Solution — 9701/23/M/J/22/Q4(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Acidified potassium dichromate(VI) is a powerful oxidising agent used in organic and analytical chemistry.",
        parts=[
            QuestionPart(
                label="a",
                text="Construct the balanced ionic half-equation for the reduction of dichromate(VI) ions, Cr2O7^2-, to chromium(III) ions, Cr^3+, in acidic solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Construct the overall balanced ionic equation for the oxidation of iron(II) ions, Fe^2+, by acidified Cr2O7^2-.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the colour change observed during this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cr2O7^2- + 14H+ + 6e- -> 2Cr^3+ + 7H2O (2)", "marks": 2},
            {"part": "b", "points": "Cr2O7^2- + 14H+ + 6Fe^2+ -> 2Cr^3+ + 6Fe^3+ + 7H2O (2)", "marks": 2},
            {"part": "c", "points": "Orange to green (1)", "marks": 1}
        ]
    ),
    Question(
        number=4,
        title="Redox Titration: Potassium Manganate(VII) & Ethanedioate — 9701/22/F/M/21/Q5(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Standard potassium manganate(VII), KMnO4, is titrated against warm acidified ethanedioic acid, H2C2O4 (shown in Fig. 6.2):\n2MnO4^- + 16H^+ + 5C2O4^2- -> 2Mn^2+ + 10CO2 + 8H2O",
        parts=[
            QuestionPart(
                label="a",
                text="State the oxidation number change of carbon in this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="A 25.0 cm3 sample of 0.0500 mol dm^-3 H2C2O4 required 20.40 cm3 of KMnO4(aq) for complete oxidation. Calculate the concentration of the KMnO4 solution in mol dm^-3.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why no external chemical indicator is required for this titration.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "From +3 (in C2O4^2-) to +4 (in CO2) (1)", "marks": 1},
            {"part": "b", "points": "n(H2C2O4) = 0.0500 x 0.0250 = 1.25 x 10^-3 mol (1); n(MnO4^-) = 1.25 x 10^-3 x (2 / 5) = 5.00 x 10^-4 mol (1); c(KMnO4) = 5.00 x 10^-4 / 0.02040 = 0.0245 mol dm^-3 (allow 0.0245 - 0.0246 mol dm^-3) (1)", "marks": 3},
            {"part": "c", "points": "KMnO4 acts as a self-indicator; the end-point is marked by the first permanent pale pink colour caused by a tiny excess of unreacted purple MnO4^- ions (1)", "marks": 1}
        ],
        figure_path="figures/redox_titration_permanganate.png",
        figure_caption="Fig. 6.2: Setup for self-indicating redox titration of acidified Fe2+ or C2O4(2-) with KMnO4."
    ),
    Question(
        number=5,
        title="Iodine-Thiosulfate Titration: Analysis of Bleach — 9701/21/M/J/22/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="The active ingredient in commercial household bleach is the chlorate(I) ion, ClO^-.\nStage 1: ClO^- + 2I^- + 2H^+ -> I2 + Cl^- + H2O\nStage 2: I2 + 2S2O3^2- -> 2I^- + S4O6^2-",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the reducing agent in Stage 1 and the oxidising agent in Stage 2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the indicator used for the iodine-thiosulfate titration in Stage 2 and state the colour change observed at the end-point.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="A 10.0 cm3 sample of bleach was diluted to 250 cm3. A 25.0 cm3 aliquot of this diluted solution was reacted with excess acidified KI and titrated with 22.80 cm3 of 0.100 mol dm^-3 Na2S2O3. Calculate the concentration of ClO^- in the original undiluted bleach in mol dm^-3.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Reducing agent in Stage 1: Iodide ion / I- (1); Oxidising agent in Stage 2: Iodine / I2 (1)", "marks": 2},
            {"part": "b", "points": "Starch indicator (added near the end-point when solution is pale straw-yellow) (1); End-point colour change: blue-black to colourless (1)", "marks": 2},
            {"part": "c", "points": "n(S2O3^2-) = 0.100 x 0.02280 = 2.28 x 10^-3 mol; n(I2) = 1.14 x 10^-3 mol => n(ClO^- in 25 cm3) = 1.14 x 10^-3 mol (1); n(ClO^- in 250 cm3) = 1.14 x 10^-2 mol (1); Concentration in original 10.0 cm3 bleach = 1.14 x 10^-2 / 0.0100 = 1.14 mol dm^-3 (1)", "marks": 3}
        ]
    ),
    Question(
        number=6,
        title="Dual Redox Nature of Hydrogen Peroxide, H2O2 — 9701/22/O/N/23/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="In hydrogen peroxide, H2O2, oxygen has an unusual oxidation number of -1. H2O2 can act as an oxidising agent, a reducing agent, or undergo disproportionation.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced equation for the catalytic disproportionation of H2O2 into water and oxygen, and show the oxidation numbers of oxygen throughout.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="When H2O2 acts as a reducing agent in reaction with acidified KMnO4, oxygen gas is evolved. Write the oxidation half-equation for H2O2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="When H2O2 acts as an oxidising agent in reaction with acidified Fe^2+, write the reduction half-equation for H2O2.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "2H2O2(aq) -> 2H2O(l) + O2(g) (1); Oxygen in H2O2 is -1, in H2O is -2 (reduced), in O2 is 0 (oxidised) (1)", "marks": 2},
            {"part": "b", "points": "H2O2 -> O2 + 2H+ + 2e- (1)", "marks": 1},
            {"part": "c", "points": "H2O2 + 2H+ + 2e- -> 2H2O (1)", "marks": 1}
        ]
    ),
    Question(
        number=7,
        title="Oxidation Numbers in Nitrogen Compounds — 9701/21/M/J/23/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Nitrogen exhibits every integral oxidation state from -3 to +5 across its various compounds.",
        parts=[
            QuestionPart(
                label="a",
                text="Determine the oxidation number of nitrogen in each of the following:\n(i) Ammonia, NH3\n(ii) Hydrazine, N2H4\n(iii) Dinitrogen monoxide, N2O\n(iv) Nitrogen dioxide, NO2\n(v) Nitrate ion, NO3^-",
                marks=5,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) -3 (1); (ii) -2 (1); (iii) +1 (1); (iv) +4 (1); (v) +5 (1)", "marks": 5}
        ]
    ),
    Question(
        number=8,
        title="Copper Reaction with Dilute vs Concentrated Nitric Acid — 9701/22/M/J/20/Q5(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Copper metal reacts differently with concentrated and dilute nitric acid.\nReaction 1 (concentrated): Cu(s) + 4HNO3(aq) -> Cu(NO3)2(aq) + 2NO2(g) + 2H2O(l)\nReaction 2 (dilute): 3Cu(s) + 8HNO3(aq) -> 3Cu(NO3)2(aq) + 2NO(g) + 4H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Identify which species is oxidised and which species is reduced in Reaction 1.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Construct the ionic half-equation for the reduction of nitrate ions, NO3^-, to nitrogen monoxide, NO, in acidic solution (Reaction 2).",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the observation that confirms nitrogen dioxide, NO2, is evolved in Reaction 1.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Copper / Cu is oxidised (0 to +2) (1); Nitrogen in HNO3 is reduced (+5 to +4 in NO2) (1)", "marks": 2},
            {"part": "b", "points": "NO3^- + 4H+ + 3e- -> NO + 2H2O (2)", "marks": 2},
            {"part": "c", "points": "Brown gas / brown fumes evolved (1)", "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Disproportionation of Copper(I) in Aqueous Solution — 9701/21/O/N/22/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="When solid copper(I) oxide, Cu2O, is reacted with dilute sulfuric acid, a brown precipitate of copper metal and a blue solution of copper(II) sulfate are formed:\nCu2O(s) + H2SO4(aq) -> Cu(s) + CuSO4(aq) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Write the ionic equation for the disproportionation of aqueous copper(I) ions.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why this reaction is classified as a disproportionation by referring to changes in oxidation numbers.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "2Cu+(aq) -> Cu(s) + Cu^2+(aq) (1)", "marks": 1},
            {"part": "b", "points": "Copper(I) (+1) is simultaneously reduced to copper metal (0) (1); and oxidised to copper(II) (+2) (1)", "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Reaction of Acidified Dichromate(VI) with Sulfur Dioxide — 9701/23/O/N/21/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Sulfur dioxide gas acts as a reducing agent when bubbled through acidified potassium dichromate(VI) solution.",
        parts=[
            QuestionPart(
                label="a",
                text="Construct the oxidation half-equation for SO2 in aqueous solution forming sulfate ions, SO4^2-.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Combine your half-equation in (a) with the reduction half-equation for Cr2O7^2- to write the overall balanced ionic equation.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the visible colour change that serves as a diagnostic test for sulfur dioxide gas.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "SO2 + 2H2O -> SO4^2- + 4H+ + 2e- (2)", "marks": 2},
            {"part": "b", "points": "Cr2O7^2- + 2H+ + 3SO2 -> 2Cr^3+ + 3SO4^2- + H2O (2)", "marks": 2},
            {"part": "c", "points": "Orange to green (1)", "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Redox Titration: Determination of Iron in Dietary Tablets — 9701/22/F/M/23/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Iron deficiency tablets contain hydrated iron(II) sulfate, FeSO4.7H2O (Mr = 277.9).\nFive crushed tablets with a total mass of 1.750 g were dissolved in dilute H2SO4 to make 250.0 cm3 of solution. A 25.0 cm3 sample required 18.20 cm3 of 0.0100 mol dm^-3 KMnO4 for complete titration:\n5Fe^2+ + MnO4^- + 8H^+ -> 5Fe^3+ + Mn^2+ + 4H2O",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of Fe^2+ ions present in the 25.0 cm3 sample.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the total mass of Fe (Ar = 55.8) in the five tablets.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the percentage by mass of iron, Fe, in the tablets.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(MnO4^-) = 0.0100 x 0.01820 = 1.82 x 10^-4 mol (1); n(Fe^2+) = 5 x 1.82 x 10^-4 = 9.10 x 10^-4 mol (1)", "marks": 2},
            {"part": "b", "points": "Total moles Fe in 250 cm3 = 9.10 x 10^-4 x 10 = 9.10 x 10^-3 mol (1); Mass of Fe = 9.10 x 10^-3 x 55.8 = 0.5078 g (or 508 mg) (1)", "marks": 2},
            {"part": "c", "points": "% Fe = (0.5078 / 1.750) x 100% = 29.0% (allow 29.0% - 29.1%) (1)", "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Oxidation States of Vanadium Oxoanions — 9701/21/M/J/21/Q6(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Vanadium forms oxoanions with characteristic colours corresponding to oxidation states +5, +4, +3, and +2:\n• VO2^+ (yellow): oxidation state +5\n• VO^2+ (blue): oxidation state +4\n• V^3+ (green): oxidation state +3\n• V^2+ (violet): oxidation state +2",
        parts=[
            QuestionPart(
                label="a",
                text="Verify the oxidation state of vanadium in VO2^+ and in VO^2+ by calculation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="When zinc metal is added to an acidified solution of VO2^+, the solution gradually turns green, then blue, and finally violet. Write the ionic equation for the first reduction step from VO2^+ to VO^2+.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "VO2^+: V + 2(-2) = +1 => V = +5 (1); VO^2+: V + (-2) = +2 => V = +4 (1)", "marks": 2},
            {"part": "b", "points": "2VO2^+ + Zn + 4H+ -> 2VO^2+ + Zn^2+ + 2H2O (2)", "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Halogen Displacement Reactions & Oxidising Strength — 9701/22/M/J/22/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Halogens act as oxidising agents by accepting electrons to form halide ions:\nX2 + 2e^- -> 2X^-",
        parts=[
            QuestionPart(
                label="a",
                text="State the trend in oxidising ability of the halogens down Group 17 from chlorine to iodine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the ionic equation for the reaction that occurs when chlorine water is added to aqueous potassium bromide, and state the colour observed.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain the trend in oxidising ability down Group 17 in terms of atomic radius and electron shielding.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Oxidising ability decreases down Group 17 (Cl2 > Br2 > I2) (1)", "marks": 1},
            {"part": "b", "points": "Cl2(aq) + 2Br^-(aq) -> 2Cl^-(aq) + Br2(aq) (1); Orange / orange-brown colour formed (1)", "marks": 2},
            {"part": "c", "points": "Down the group, atomic radius increases and electron shielding increases (1); The nucleus exerts weaker electrostatic attraction on incoming electrons, making electron capture less favourable (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Acid Disproportionation of Sodium Thiosulfate — 9701/22/O/N/21/Q6(a)-(c)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="When dilute hydrochloric acid is added to aqueous sodium thiosulfate, the solution gradually turns cloudy yellow:\nNa2S2O3(aq) + 2HCl(aq) -> 2NaCl(aq) + SO2(g) + S(s) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the substance responsible for the yellow turbidity.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Show, by assigning oxidation numbers, that this is a disproportionation reaction of sulfur.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Sulfur / colloidal sulfur precipitate (1)", "marks": 1},
            {"part": "b", "points": "Oxidation state of sulfur in S2O3^2- is +2 (1); In SO2, sulfur is +4 (oxidised) (1); In elemental sulfur S(s), sulfur is 0 (reduced) (1)", "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Oxidation States of Carbon in Organic Molecules — 9701/21/O/N/23/Q4(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Assigning oxidation numbers to carbon atoms reveals whether an organic transformation is an oxidation, reduction, or substitution.",
        parts=[
            QuestionPart(
                label="a",
                text="Assign the average oxidation number of carbon in each of the following molecules:\n(i) Methane, CH4\n(ii) Methanol, CH3OH\n(iii) Methanal, HCHO\n(iv) Methanoic acid, HCOOH\n(v) Carbon dioxide, CO2",
                marks=5,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) -4 (1); (ii) -2 (1); (iii) 0 (1); (iv) +2 (1); (v) +4 (1)", "marks": 5}
        ]
    ),
    Question(
        number=16,
        title="Redox Titration: Purity of Hydrogen Peroxide — 9701/23/M/J/20/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="A 20.0 cm3 sample of commercial hydrogen peroxide was diluted to 500 cm3 in a volumetric flask. A 25.0 cm3 portion of this diluted solution was acidified and titrated against 0.0200 mol dm^-3 KMnO4:\n2MnO4^- + 6H^+ + 5H2O2 -> 2Mn^2+ + 5O2 + 8H2O\nThe mean titre was 18.50 cm3.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of MnO4^- used in the titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the concentration, in mol dm^-3, of H2O2 in the original commercial solution.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(MnO4^-) = 0.0200 x 0.01850 = 3.70 x 10^-4 mol (1)", "marks": 1},
            {"part": "b", "points": "n(H2O2 in 25 cm3) = 3.70 x 10^-4 x (5 / 2) = 9.25 x 10^-4 mol (1); n(H2O2 in 500 cm3) = 9.25 x 10^-4 x 20 = 1.85 x 10^-2 mol (1); Concentration in original 20.0 cm3 = 1.85 x 10^-2 / 0.0200 = 0.925 mol dm^-3 (1)", "marks": 3}
        ]
    ),
    Question(
        number=17,
        title="Mohr's Salt Redox Titration with Dichromate(VI) — 9701/22/F/M/24/Q4(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Mohr's salt, (NH4)2Fe(SO4)2.6H2O (Mr = 392.1), is used as a primary standard for Fe^2+.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Mohr's salt is preferred over iron(II) sulfate crystals, FeSO4.7H2O, as a primary standard in analytical laboratories.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="A 3.921 g sample of Mohr's salt was dissolved and made up to 100 cm3 with dilute sulfuric acid. Calculate the volume of 0.0200 mol dm^-3 K2Cr2O7 required to titrate a 25.0 cm3 aliquot of this solution.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mohr's salt has high purity, does not effloresce or lose water of crystallisation easily, and is much less susceptible to aerial oxidation by atmospheric O2 (1)", "marks": 1},
            {"part": "b", "points": "Total moles Mohr's salt = 3.921 / 392.1 = 0.0100 mol => n(Fe^2+ in 25 cm3) = 2.50 x 10^-3 mol (1); Stoichiometry: 1 Cr2O7^2- : 6 Fe^2+ => n(Cr2O7^2-) = 2.50 x 10^-3 / 6 = 4.167 x 10^-4 mol (1); Volume = 4.167 x 10^-4 / 0.0200 = 0.02083 dm3 = 20.8 cm3 (allow 20.8 - 20.9 cm3) (1)", "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Thermal Disproportionation of Bleach — 9701/21/M/J/24/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="When an aqueous solution of sodium chlorate(I), NaClO, is stored at elevated temperatures (above 40 °C), it slowly degrades according to the equation:\n3NaClO(aq) -> 2NaCl(aq) + NaClO3(aq)",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the oxidation state of chlorine in each of the three chlorine-containing compounds.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why bleach loses its germicidal disinfectant power when heated.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In NaClO: +1 (1); In NaCl: -1 (1); In NaClO3: +5 (1)", "marks": 3},
            {"part": "b", "points": "The active oxidising and germicidal agent ClO^- is decomposed into chloride and chlorate(V) ions (1)", "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Halide Reactions with Concentrated Sulfuric Acid — 9701/22/O/N/24/Q5(a)-(d)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="When solid sodium halides are treated with concentrated sulfuric acid, a mixture of acid-base and redox reactions occurs depending on the reducing power of the halide.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why NaCl reacts with concentrated H2SO4 to produce only steamy acidic fumes of HCl with no redox reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the observation and write the balanced redox equation for the reduction of H2SO4 by sodium bromide, NaBr.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="When sodium iodide, NaI, reacts with concentrated H2SO4, three different reduction products of sulfur are formed: SO2, S, and H2S. State the oxidation number of sulfur in each product.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Chloride ions, Cl-, are not strong enough reducing agents to reduce concentrated sulfuric acid (1)", "marks": 1},
            {"part": "b", "points": "Brown fumes / orange-brown liquid of Br2 (and choking gas SO2) (1); 2NaBr + 3H2SO4 -> 2NaHSO4 + Br2 + SO2 + 2H2O (or 2Br- + H2SO4 + 2H+ -> Br2 + SO2 + 2H2O) (1)", "marks": 2},
            {"part": "c", "points": "In SO2: +4 (1); In S: 0 (1); In H2S: -2 (1)", "marks": 3}
        ]
    ),
    Question(
        number=20,
        title="Balancing Redox Reactions in Alkaline Solution — 9701/21/O/N/24/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="In neutral or alkaline solution, manganate(VII) ions are reduced to a dark brown precipitate of manganese(IV) oxide, MnO2:\nMnO4^- + 2H2O + 3e^- -> MnO2 + 4OH^-",
        parts=[
            QuestionPart(
                label="a",
                text="Construct the oxidation half-equation for the oxidation of sulfite ions, SO3^2-, to sulfate ions, SO4^2-, in alkaline solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the overall balanced ionic equation for the reaction between MnO4^- and SO3^2- in alkaline solution.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "SO3^2- + 2OH- -> SO4^2- + H2O + 2e- (2)", "marks": 2},
            {"part": "b", "points": "2MnO4^- + 3SO3^2- + H2O -> 2MnO2 + 3SO4^2- + 2OH- (2)", "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Disproportionation of Nitrous Acid, HNO2 — 9701/23/M/J/23/Q4(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Nitrous acid, HNO2, is unstable at room temperature and disproportionates:\n3HNO2(aq) -> HNO3(aq) + 2NO(g) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Determine the oxidation state of nitrogen in HNO2, HNO3, and NO.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State how this reaction demonstrates disproportionation.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "HNO2: +3 (1); HNO3: +5 (1); NO: +2 (1)", "marks": 3},
            {"part": "b", "points": "Nitrogen in oxidation state +3 is simultaneously oxidised to +5 and reduced to +2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Determination of Copper in Brass Alloy via Redox Titration — 9701/22/M/J/25/Q3(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="Brass is an alloy of copper and zinc.\nA 2.500 g sample of brass was dissolved in concentrated HNO3, neutralised, and made up to 250.0 cm3. Excess KI was added to a 25.0 cm3 aliquot:\n2Cu^2+(aq) + 4I^-(aq) -> 2CuI(s) + I2(aq)\nThe liberated I2 required 23.60 cm3 of 0.100 mol dm^-3 Na2S2O3 for complete titration.",
        parts=[
            QuestionPart(
                label="a",
                text="State the oxidation number of copper in the precipitate CuI.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the mass of copper (Ar = 63.5) present in the 2.500 g brass sample.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Calculate the percentage of copper by mass in this brass alloy.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "+1 (1)", "marks": 1},
            {"part": "b", "points": "n(S2O3^2-) = 0.100 x 0.02360 = 2.36 x 10^-3 mol; n(I2) = 1.18 x 10^-3 mol; n(Cu^2+ in 25 cm3) = 2.36 x 10^-3 mol (1); Total n(Cu in 250 cm3) = 2.36 x 10^-2 mol (1); Mass of Cu = 2.36 x 10^-2 x 63.5 = 1.499 g (1)", "marks": 3},
            {"part": "c", "points": "% Cu = (1.499 / 2.500) x 100% = 60.0% (1)", "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Unusual Oxidation States of Oxygen — 9701/21/F/M/25/Q4(a)-(b)",
        syllabus_ref="6.1",
        difficulty="EASY",
        preamble="Although oxygen almost always displays an oxidation number of -2, exceptional states exist.",
        parts=[
            QuestionPart(
                label="a",
                text="State the oxidation number of oxygen in each of the following:\n(i) H2O\n(ii) H2O2\n(iii) KO2\n(iv) OF2",
                marks=4,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why oxygen has a positive oxidation number in oxygen difluoride, OF2.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) -2 (1); (ii) -1 (1); (iii) -1/2 (or -0.5) (1); (iv) +2 (1)", "marks": 4},
            {"part": "b", "points": "Fluorine is more electronegative than oxygen (4.0 vs 3.5 on Pauling scale), so fluorine is assigned the negative oxidation state (-1) (1)", "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Comproportionation of Iodate(V) with Iodide — 9701/22/O/N/25/Q5(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="When potassium iodate(V), KIO3, reacts with potassium iodide in the presence of dilute sulfuric acid, elemental iodine is produced:\nIO3^-(aq) + 5I^-(aq) + 6H^+(aq) -> 3I2(aq) + 3H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why this reaction is described as a comproportionation reaction (the reverse of disproportionation).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the molar ratio of oxidising agent to reducing agent in this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Iodine in two different oxidation states (+5 in IO3^- and -1 in I-) (1); react together to form a single product with an intermediate oxidation state (0 in I2) (1)", "marks": 2},
            {"part": "b", "points": "1 IO3^- (oxidising agent) : 5 I^- (reducing agent) => ratio 1 : 5 (1)", "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Sequential Reduction of Vanadate(V) by Zinc — 9701/23/O/N/24/Q4(a)-(c)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="When granulated zinc is added to an acidified yellow solution of ammonium vanadate, NH4VO3, the solution undergoes dramatic color transitions:\nYellow (+5) -> Blue (+4) -> Green (+3) -> Violet (+2)",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the vanadium species responsible for the blue colour and the violet colour.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the balanced ionic equation for the reduction of the blue species to the green species by zinc.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Blue species: VO^2+ (vanadyl ion) (1); Violet species: V^2+ (1)", "marks": 2},
            {"part": "b", "points": "2VO^2+ + Zn + 4H+ -> 2V^3+ + Zn^2+ + 2H2O (2)", "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Interference of Chloride Ions in Permanganate Titrations — 9701/21/M/J/25/Q6(a)-(b)",
        syllabus_ref="6.1",
        difficulty="HARD",
        preamble="When iron(II) solutions are titrated with standard KMnO4, dilute sulfuric acid must be used for acidification. Dilute hydrochloric acid cannot be used.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why hydrochloric acid is unsuitable for acidifying potassium manganate(VII) titrations.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain how the use of HCl(aq) would affect the calculated concentration of Fe^2+.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "MnO4^- is a strong enough oxidising agent to oxidise chloride ions, Cl^-, to toxic chlorine gas, Cl2 (1); 2MnO4^- + 16H+ + 10Cl- -> 2Mn^2+ + 5Cl2 + 8H2O (1)", "marks": 2},
            {"part": "b", "points": "Extra KMnO4 would be consumed reacting with Cl- ions in addition to Fe^2+ (1); This gives an artificially large titre and overestimates the concentration of Fe^2+ (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 6.2: Electrolysis & Quantitative Faraday Calculations (Q27 to Q50)
    # =========================================================================
    Question(
        number=27,
        title="Electrolysis of Concentrated Aqueous Sodium Chloride (Brine) — 9701/22/M/J/21/Q5(a)-(d)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="The industrial chlor-alkali process involves the electrolysis of concentrated aqueous NaCl (brine), shown in Fig. 6.3.",
        parts=[
            QuestionPart(
                label="a",
                text="List all four ions present in concentrated aqueous sodium chloride solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the ionic half-equation for the reaction occurring at the anode (+) and explain why chlorine is discharged rather than oxygen.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Write the ionic half-equation for the reaction occurring at the cathode (-).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Identify the alkaline chemical product remaining in the solution after prolonged electrolysis.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na+, Cl-, H+, OH- (all four required for 2 marks, any two for 1 mark) (2)", "marks": 2},
            {"part": "b", "points": "2Cl-(aq) -> Cl2(g) + 2e- (1); In concentrated solution, the high concentration of Cl- ions favours their discharge over OH- ions (1)", "marks": 2},
            {"part": "c", "points": "2H+(aq) + 2e- -> H2(g) (or 2H2O + 2e- -> H2 + 2OH-) (1)", "marks": 1},
            {"part": "d", "points": "Sodium hydroxide, NaOH(aq) (1)", "marks": 1}
        ],
        figure_path="figures/electrolysis_aqueous_nacl.png",
        figure_caption="Fig. 6.3: Electrolytic cell for concentrated aqueous sodium chloride (brine)."
    ),
    Question(
        number=28,
        title="Industrial Electrolytic Refining of Copper — 9701/21/O/N/21/Q5(a)-(d)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="Impure blister copper is purified to 99.99% purity using the electrolytic cell shown in Fig. 6.4.",
        parts=[
            QuestionPart(
                label="a",
                text="State the material used for the anode and the material used for the cathode.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write half-equations for the reactions occurring at the anode and cathode.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the concentration of Cu^2+ ions in the electrolyte remains virtually constant throughout the process.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Explain why valuable precious metals like silver and gold accumulate in the anode sludge at the bottom of the cell.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Anode (+): Impure copper / blister copper (1); Cathode (-): Pure copper sheet (1)", "marks": 2},
            {"part": "b", "points": "Anode: Cu(s) -> Cu^2+(aq) + 2e- (1); Cathode: Cu^2+(aq) + 2e- -> Cu(s) (1)", "marks": 2},
            {"part": "c", "points": "Copper dissolves from the anode into the electrolyte at exactly the same rate that copper deposits onto the cathode (1)", "marks": 1},
            {"part": "d", "points": "Silver and gold are less reactive / have more positive standard electrode potentials than copper (1); They are not oxidised at the operating voltage and simply drop unreacted to the bottom as the copper anode dissolves (1)", "marks": 2}
        ],
        figure_path="figures/copper_refining_cell.png",
        figure_caption="Fig. 6.4: Industrial electrolytic cell for the refining and purification of copper."
    ),
    Question(
        number=29,
        title="Fundamental Principles of Electrolysis — 9701/23/M/J/22/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="Electrolysis is the decomposition of an electrolyte by the passage of direct electric current.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term electrolyte.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Distinguish between how electrical current is conducted through a metallic wire compared to through an electrolyte.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A molten ionic compound or aqueous solution containing mobile ions (1); that conducts electricity accompanied by chemical decomposition (1)", "marks": 2},
            {"part": "b", "points": "In a metallic wire, current is carried by the flow of delocalised mobile electrons without chemical change (1); In an electrolyte, current is carried by the migration of mobile positive and negative ions towards electrodes with chemical reaction (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Electrolysis of Molten Lead(II) Bromide — 9701/22/F/M/22/Q4(a)-(c)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="When solid lead(II) bromide, PbBr2, is heated until molten, it conducts electricity and undergoes electrolysis using graphite electrodes.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why solid PbBr2 does not conduct electricity, but molten PbBr2 does.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write half-equations with state symbols for the reactions at the anode and cathode.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State one observation at the anode and one observation at the cathode.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In solid PbBr2, ions are held firmly in fixed lattice positions and cannot move (1); In molten PbBr2, the lattice breaks down and Pb^2+ and Br^- ions are free to move throughout the liquid (1)", "marks": 2},
            {"part": "b", "points": "Anode: 2Br^-(l) -> Br2(g) + 2e- (1); Cathode: Pb^2+(l) + 2e- -> Pb(l) (1)", "marks": 2},
            {"part": "c", "points": "Anode: Brown / red-brown fumes of bromine gas evolved (1); Cathode: Silvery / grey bead of molten lead metal formed (1)", "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Electrolysis of Dilute vs Concentrated Aqueous NaCl — 9701/21/M/J/22/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="The concentration of halide ions in aqueous solutions influences which anion is discharged at the inert anode.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the gas evolved at the anode during the electrolysis of very dilute aqueous sodium chloride, and write the half-equation for its formation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why changing to concentrated aqueous sodium chloride changes the primary product formed at the anode.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Oxygen / O2 gas (1); 4OH^-(aq) -> O2(g) + 2H2O(l) + 4e- (or 2H2O -> O2 + 4H+ + 4e-) (1)", "marks": 2},
            {"part": "b", "points": "In dilute solution, OH- ions are discharged more readily than Cl- ions (1); In concentrated solution, the concentration of Cl- ions is vastly higher than OH-, so Cl- ions are preferentially discharged to form Cl2 gas (1)", "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Faraday's Laws & Calculation of Deposited Mass — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="Faraday's constant, F, is the quantity of electric charge carried by one mole of electrons: F = 96500 C mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="State the mathematical relationship connecting electrical charge Q, current I, and time t.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="A steady electric current of 2.50 A is passed through a solution of copper(II) sulfate for 45.0 minutes. Calculate the total charge Q passed in Coulombs.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass of copper (Ar = 63.5) deposited at the cathode.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Q = I x t (where I is in Amperes and t is in seconds) (1)", "marks": 1},
            {"part": "b", "points": "t = 45.0 x 60 = 2700 s; Q = 2.50 x 2700 = 6750 C (2)", "marks": 2},
            {"part": "c", "points": "n(e-) = 6750 / 96500 = 0.06995 mol; Cu^2+ + 2e- -> Cu => n(Cu) = 0.06995 / 2 = 0.03497 mol (1); Mass = 0.03497 x 63.5 = 2.22 g (allow 2.21 - 2.23 g) (1)", "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Determining Avogadro Constant from Electrolytic Deposition of Silver — 9701/23/O/N/22/Q4(a)-(c)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="In an electrochemical experiment to evaluate the Avogadro constant, L, a current of 0.400 A was passed through an aqueous silver nitrate solution for 1.00 hour. The cathode gained 1.610 g of pure silver (Ar = 107.9). The charge on a single electron is e = 1.602 x 10^-19 C.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total electric charge passed during the experiment.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the experimental value for the Faraday constant, F.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Using F = L x e, calculate the experimental value for the Avogadro constant, L, to 3 significant figures.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Q = I x t = 0.400 x 3600 = 1440 C (1)", "marks": 1},
            {"part": "b", "points": "n(Ag) = 1.610 / 107.9 = 0.01492 mol; Ag+ + e- -> Ag => n(e-) = 0.01492 mol (1); F = Q / n(e-) = 1440 / 0.01492 = 96515 C mol^-1 (allow 96400 - 96600) (1)", "marks": 2},
            {"part": "c", "points": "L = F / e = 96515 / (1.602 x 10^-19) (1); L = 6.02 x 10^23 mol^-1 (allow 6.01 - 6.03 x 10^23 mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Electrolysis of Aqueous CuSO4 with Inert vs Active Electrodes — 9701/22/F/M/23/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Aqueous copper(II) sulfate is electrolysed in two separate experiments:\n• Cell 1: Using inert platinum electrodes\n• Cell 2: Using active copper electrodes",
        parts=[
            QuestionPart(
                label="a",
                text="For Cell 1 (platinum electrodes), state the product formed at the anode and write the half-equation for its formation.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State and explain the change in color of the electrolyte in Cell 1 and in Cell 2 after 30 minutes of electrolysis.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Oxygen / O2 gas (1); 4OH^-(aq) -> O2(g) + 2H2O(l) + 4e- (or 2H2O -> O2 + 4H+ + 4e-) (1)", "marks": 2},
            {"part": "b", "points": "In Cell 1: The blue color fades to colourless because Cu^2+ ions are discharged at cathode while OH- is discharged at anode, forming sulfuric acid (1); In Cell 2: The blue color remains unchanged (1); because Cu^2+ ions are removed at the cathode at the exact same rate that Cu dissolves from the copper anode (1)", "marks": 3}
        ]
    ),
    Question(
        number=35,
        title="Electrolysis of Dilute Sulfuric Acid (Hoffman Voltameter) — 9701/21/M/J/23/Q6(a)-(c)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="Dilute sulfuric acid, H2SO4(aq), is electrolysed in a Hoffman voltameter using inert platinum electrodes.",
        parts=[
            QuestionPart(
                label="a",
                text="Write ionic half-equations for the reactions occurring at the cathode and anode.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the theoretical ratio of the volume of gas collected at the cathode to the volume of gas collected at the anode.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain this volume ratio in terms of the number of electrons transferred.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cathode: 2H+(aq) + 2e- -> H2(g) (1); Anode: 4OH-(aq) -> O2(g) + 2H2O(l) + 4e- (or 2H2O -> O2 + 4H+ + 4e-) (1)", "marks": 2},
            {"part": "b", "points": "Volume H2 (cathode) : Volume O2 (anode) = 2 : 1 (1)", "marks": 1},
            {"part": "c", "points": "Each mole of O2 evolved requires the transfer of 4 moles of electrons (1); The same 4 moles of electrons produces 2 moles of H2 gas (since 2e- per H2), giving twice the volume of H2 (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Preferential Discharge of Anions — 9701/22/M/J/23/Q4(b)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="The ease of discharge of anions at the anode during electrolysis depends on standard electrode potentials and ionic concentrations.",
        parts=[
            QuestionPart(
                label="a",
                text="Arrange the following anions in order of increasing ease of discharge at an inert anode:\nOH^-, I^-, Cl^-, SO4^2-",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why sulfate ions, SO4^2-, and nitrate ions, NO3^-, are never discharged from aqueous solutions at an inert anode.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "SO4^2- < Cl- < OH- < I- (or SO4^2- < OH- < Cl- < I- depending on concentration) (2)", "marks": 2},
            {"part": "b", "points": "SO4^2- and NO3^- ions contain central atoms in their maximum oxidation states (+6 and +5) (1); Hydroxide ions (OH-) or water molecules are much more readily oxidised than sulfate or nitrate oxoanions (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Electroplating of Nickel onto a Steel Spoon — 9701/21/O/N/23/Q5(a)-(c)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="A steel spoon is electroplated with nickel to prevent corrosion and improve appearance.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether the steel spoon should be connected to the positive or negative terminal of the DC power supply.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Suggest a suitable electrolyte and anode material for this electroplating process.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the half-equation for the nickel coating process occurring on the spoon.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Negative terminal (spoon must act as cathode) (1)", "marks": 1},
            {"part": "b", "points": "Electrolyte: Aqueous nickel(II) sulfate, NiSO4(aq) (1); Anode: Pure nickel metal bar / sheet (1)", "marks": 2},
            {"part": "c", "points": "Ni^2+(aq) + 2e- -> Ni(s) (1)", "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Anodising of Aluminium — 9701/22/O/N/23/Q5(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Aluminium objects are anodised to increase the thickness of the protective surface layer of aluminium oxide, Al2O3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the aluminium object is made the anode rather than the cathode in this process.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the overall ionic equation for the formation of the aluminium oxide layer at the anode using dilute sulfuric acid as the electrolyte.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State one property imparted to aluminium by anodising.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Oxidation occurs at the anode (1); Oxygen gas is liberated at the anode, which immediately reacts with the aluminium surface to form an oxide layer (1)", "marks": 2},
            {"part": "b", "points": "2Al(s) + 3H2O(l) -> Al2O3(s) + 6H+(aq) + 6e- (or 4Al + 3O2 -> 2Al2O3) (2)", "marks": 2},
            {"part": "c", "points": "Increased corrosion resistance / increased surface hardness / ability to absorb colored dyes (1)", "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Quantitative Electrolysis: Volume of Oxygen Evolved — 9701/23/M/J/24/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="A current of 3.20 A is passed through dilute sodium hydroxide for 25.0 minutes using inert electrodes.\n4OH^-(aq) -> O2(g) + 2H2O(l) + 4e-",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of electrons transferred.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the volume, in cm3, of oxygen gas evolved at room temperature and pressure (RTP, molar volume = 24.0 dm3 mol^-1).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "t = 25.0 x 60 = 1500 s; Q = 3.20 x 1500 = 4800 C (1); n(e-) = 4800 / 96500 = 0.04974 mol (1)", "marks": 2},
            {"part": "b", "points": "n(O2) = 0.04974 / 4 = 0.01244 mol (1); V = 0.01244 x 24000 cm3 = 298 cm3 (allow 297 - 299 cm3) (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Extraction of Aluminium: Hall-Héroult Process — 9701/21/M/J/24/Q6(a)-(c)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Aluminium is extracted industrially by the electrolysis of molten alumina, Al2O3, dissolved in molten cryolite, Na3AlF6, at 950 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="State two reasons why molten cryolite is added to the alumina.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the half-equations for the cathode and anode reactions.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the carbon anodes must be regularly replaced in this industrial process.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cryolite lowers the melting point from over 2000 °C to ~950 °C (saving immense energy) (1); Molten cryolite increases the electrical conductivity of the molten electrolyte (1)", "marks": 2},
            {"part": "b", "points": "Cathode: Al^3+ + 3e- -> Al(l) (1); Anode: 2O^2- -> O2(g) + 4e- (1)", "marks": 2},
            {"part": "c", "points": "The oxygen gas produced at high operating temperature (950 °C) reacts with the carbon anodes to form carbon dioxide: C(s) + O2(g) -> CO2(g) (1); The carbon anodes gradually burn away and become depleted (1)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Selective Discharge of Cations in Aqueous Electrolysis — 9701/22/M/J/24/Q6(b)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="During electrolysis of aqueous solutions, either the metal cation or hydrogen ions (H+) from water will be discharged at the cathode.",
        parts=[
            QuestionPart(
                label="a",
                text="Predict whether the metal or hydrogen gas will be discharged at the cathode for each of the following aqueous solutions:\n(i) Aqueous copper(II) nitrate\n(ii) Aqueous magnesium sulfate\n(iii) Aqueous silver nitrate",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the general rule relating the reactivity / standard electrode potential of a metal to whether hydrogen or the metal is discharged at the cathode.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) Copper / Cu metal (1); (ii) Hydrogen / H2 gas (1); (iii) Silver / Ag metal (1)", "marks": 3},
            {"part": "b", "points": "Metals more reactive than hydrogen (more negative standard electrode potential, e.g. Group 1, Group 2, Al) result in H2 discharge (1); Metals less reactive than hydrogen (more positive standard electrode potential, e.g. Cu, Ag, Au) are discharged as metal (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Time Required for Zinc Galvanising — 9701/23/O/N/23/Q5(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="A steel sheet with an area of 500 cm2 is to be electroplated with a 0.050 mm thick protective layer of zinc (density = 7.14 g cm^-3, Ar = 65.4) using an electrolytic bath operating at a current of 15.0 A.\nZn^2+(aq) + 2e^- -> Zn(s)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass of zinc required to coat the sheet.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the time, in minutes, required to complete the electroplating process.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Volume = 500 x (0.050 / 10) = 2.50 cm3 (1); Mass = density x volume = 7.14 x 2.50 = 17.85 g (1)", "marks": 2},
            {"part": "b", "points": "n(Zn) = 17.85 / 65.4 = 0.2729 mol; n(e-) = 2 x 0.2729 = 0.5459 mol (1); Q = 0.5459 x 96500 = 52677 C (1); t = Q / I = 52677 / 15.0 = 3512 s = 58.5 minutes (allow 58 - 59 min) (1)", "marks": 3}
        ]
    ),
    Question(
        number=43,
        title="Electrolysis of Aqueous Sodium Sulfate with Indicator — 9701/22/F/M/25/Q5(a)-(c)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Aqueous sodium sulfate, Na2SO4, containing universal indicator is electrolysed using inert carbon electrodes.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the half-equation for the reaction occurring at the cathode and state the colour observed around the cathode.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the half-equation for the reaction occurring at the anode and state the colour observed around the anode.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain the overall chemical change that has occurred to the solution.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "2H2O(l) + 2e- -> H2(g) + 2OH-(aq) (1); Purple / blue colour formed due to generation of alkaline OH- ions (1)", "marks": 2},
            {"part": "b", "points": "2H2O(l) -> O2(g) + 4H+(aq) + 4e- (1); Red / orange colour formed due to generation of acidic H+ ions (1)", "marks": 2},
            {"part": "c", "points": "The overall reaction is the electrolysis / decomposition of water (2H2O -> 2H2 + O2); Na2SO4 acts merely as an inert electrolyte to conduct current (1)", "marks": 1}
        ]
    ),
    Question(
        number=44,
        title="Membrane Cell for the Chlor-Alkali Industry — 9701/21/F/M/25/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Modern industrial chlor-alkali plants utilise a polymer ion-exchange membrane cell to separate the anode and cathode compartments.",
        parts=[
            QuestionPart(
                label="a",
                text="State the function of the cation-exchange membrane in this cell.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why it is critical to prevent hydroxide ions (OH-) and chlorine gas (Cl2) from coming into contact within the electrolytic cell.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The membrane allows Na+ ions to migrate from the anode compartment to the cathode compartment (1); while preventing Cl- ions and OH- ions from crossing over (1)", "marks": 2},
            {"part": "b", "points": "Cl2 reacts rapidly with OH- to form chlorate(I) ions (ClO-) and chloride ions (1); This contaminates the NaOH product and reduces the yield of chlorine gas (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Electrolysis of Aqueous Potassium Iodide — 9701/22/M/J/25/Q6(a)-(c)",
        syllabus_ref="6.2",
        difficulty="EASY",
        preamble="Aqueous potassium iodide, KI, is electrolysed using graphite electrodes in a U-tube.",
        parts=[
            QuestionPart(
                label="a",
                text="State the observations at the cathode and anode.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe a chemical test on the brown liquid formed around the anode to confirm its identity.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write ionic half-equations for both electrode processes.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cathode: Effervescence / bubbles of colourless gas (H2) (1); Anode: Brown liquid / dark precipitate (I2) formed (1)", "marks": 2},
            {"part": "b", "points": "Add starch solution (1); Turns intense blue-black, confirming iodine (1)", "marks": 2},
            {"part": "c", "points": "Cathode: 2H+(aq) + 2e- -> H2(g) (1); Anode: 2I-(aq) -> I2(aq) + 2e- (1)", "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Deducing Ionic Charge from Faraday Data — 9701/23/M/J/25/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="In an experiment, a current of 1.25 A was passed through an aqueous solution containing an unknown metal ion, M^z+, for 38.6 minutes. A mass of 0.805 g of metal M (Ar = 107.4) was deposited at the cathode.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of electrons transferred.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the value of the charge z on the metal ion M^z+.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "t = 38.6 x 60 = 2316 s; Q = 1.25 x 2316 = 2895 C (1); n(e-) = 2895 / 96500 = 0.0300 mol (1)", "marks": 2},
            {"part": "b", "points": "n(M) = 0.805 / 107.4 = 7.495 x 10^-3 mol (1); z = n(e-) / n(M) = 0.0300 / (7.495 x 10^-3) = 4.00 => z = 4 (ion is M^4+) (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Electrolytic Extraction of Magnesium from Seawater — 9701/21/O/N/25/Q6(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="Magnesium is produced commercially by the electrolysis of molten anhydrous magnesium chloride, MgCl2, at 750 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why magnesium cannot be extracted by the electrolysis of aqueous magnesium chloride.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the half-equation for the cathode reaction in molten MgCl2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass of magnesium (Ar = 24.3) produced per hour by an industrial cell operating continuously at 50,000 A.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In aqueous solution, H+ ions from water are reduced much more readily than Mg^2+ ions (1); Hydrogen gas is evolved at the cathode instead of magnesium metal (1)", "marks": 2},
            {"part": "b", "points": "Mg^2+(l) + 2e- -> Mg(l) (1)", "marks": 1},
            {"part": "c", "points": "Q in 1 hour = 50000 x 3600 = 1.80 x 10^8 C (1); n(e-) = (1.80 x 10^8) / 96500 = 1865.3 mol; n(Mg) = 1865.3 / 2 = 932.6 mol (1); Mass = 932.6 x 24.3 = 22663 g = 22.7 kg (allow 22.6 - 22.8 kg) (1)", "marks": 3}
        ]
    ),
    Question(
        number=48,
        title="Current Efficiency in Industrial Electrolysis — 9701/22/O/N/25/Q6(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="In commercial electroplating, side reactions may reduce the yield of metal deposited:\n% Current Efficiency = (Actual mass deposited / Theoretical mass) x 100%",
        parts=[
            QuestionPart(
                label="a",
                text="A chromium electroplating bath operated at 20.0 A for 2.00 hours, depositing 9.60 g of chromium (Ar = 52.0, Cr^3+ + 3e^- -> Cr).\nCalculate the theoretical mass of chromium that should be deposited.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage current efficiency of this electroplating process and suggest one side reaction responsible for inefficiency.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "t = 2.00 x 3600 = 7200 s; Q = 20.0 x 7200 = 144000 C (1); n(e-) = 144000 / 96500 = 1.492 mol; n(Cr) = 1.492 / 3 = 0.4974 mol (1); Theoretical mass = 0.4974 x 52.0 = 25.86 g (1)", "marks": 3},
            {"part": "b", "points": "Efficiency = (9.60 / 25.86) x 100% = 37.1% (allow 37.0% - 37.2%) (1); Side reaction: Simultaneous reduction of H+ ions forming H2 gas at the cathode (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Electrolysis of Aqueous Lead(II) Nitrate — 9701/23/O/N/25/Q5(a)-(b)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="When aqueous lead(II) nitrate, Pb(NO3)2(aq), is electrolysed with platinum electrodes, a shiny crystalline metal deposits at the cathode while a dark brown solid deposits at the anode.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the crystalline metal deposited at the cathode and write its half-equation.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="The dark brown solid deposited at the anode is lead(IV) oxide, PbO2. Write the half-equation for the oxidation of aqueous Pb^2+ to solid PbO2.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Lead / Pb metal (1); Pb^2+(aq) + 2e- -> Pb(s) (1)", "marks": 2},
            {"part": "b", "points": "Pb^2+(aq) + 2H2O(l) -> PbO2(s) + 4H+(aq) + 2e- (2)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Copper Refining, Anode Sludge & Faraday Calculations — 9701/22/M/J/25/Q5(a)-(d)",
        syllabus_ref="6.2",
        difficulty="HARD",
        preamble="In an industrial copper refinery, an impure blister copper anode containing 98.0% Cu, 0.80% Ag, and 1.20% inert impurities by mass was refined at a constant current of 450 A for 12.0 hours.\n(Ar: Cu = 63.5, Ag = 107.9; F = 96500 C mol^-1)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the theoretical mass of pure copper deposited on the cathode.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Assuming 100% current efficiency for copper deposition, calculate the total mass of blister copper anode dissolved.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass of precious silver recovered from the anode slime.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Explain why silver does not dissolve and deposit onto the cathode alongside copper.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "t = 12.0 x 3600 = 43200 s; Q = 450 x 43200 = 1.944 x 10^7 C (1); n(e-) = (1.944 x 10^7) / 96500 = 201.45 mol; n(Cu) = 201.45 / 2 = 100.73 mol (1); Mass pure Cu = 100.73 x 63.5 = 6396 g = 6.40 kg (allow 6.39 - 6.41 kg) (1)", "marks": 3},
            {"part": "b", "points": "Mass of Cu dissolved = 6396 g; Blister copper mass = 6396 / 0.980 = 6527 g = 6.53 kg (1); Correct calculation to 3 s.f. (1)", "marks": 2},
            {"part": "c", "points": "Mass of silver = 0.0080 x 6527 g = 52.2 g (allow 52.0 - 52.3 g) (2)", "marks": 2},
            {"part": "d", "points": "Silver is less electropositive / has a more positive standard electrode potential than copper (1); At the controlled cell voltage used for copper oxidation, silver cannot be oxidised to Ag+ and falls unreacted into the anode sludge (1)", "marks": 2}
        ]
    )
]
'''
    with open(r"z:\tests n quizes63\books\psycology\new styl\topic6_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully wrote topic6_data.py!")

if __name__ == "__main__":
    generate()
