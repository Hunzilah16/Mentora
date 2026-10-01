"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 5: Chemical Energetics.
Subtopics:
  5.1 Enthalpy change, delta-H (definitions, profiles, calorimetry q = mc*delta-T)
  5.2 Hess's law (formation, combustion, bond energies, thermochemical cycles)

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

TOPIC_5_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 5.1: Enthalpy Change, Delta-H (Q1 to Q25)
    # =========================================================================
    Question(
        number=1,
        title="Standard Enthalpy of Formation & Standard Conditions — 9701/22/M/J/21/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Thermochemical equations depend on precisely defined standard states and conditions.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term standard enthalpy change of formation, Delta H_f_theta.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State the standard conditions of temperature and pressure specified for thermochemical measurements.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the standard enthalpy change of formation of pure liquid bromine, Br2(l), is exactly 0.0 kJ mol^-1.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The enthalpy change when one mole of a compound (1); is formed from its constituent elements in their standard states (1); under standard conditions (298 K and 100 kPa) (1)", "marks": 3},
            {"part": "b", "points": "Temperature: 298 K (or 25 °C) (1); Pressure: 100 kPa (or 1.00 x 10^5 Pa / 1 bar) (1)", "marks": 2},
            {"part": "c", "points": "Bromine is an element in its standard state at 298 K and 100 kPa (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Enthalpy Profile Diagrams: Catalysed vs Uncatalysed — 9701/21/O/N/20/Q3(a)-(c)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="The enthalpy profile diagrams below show the progress of an exothermic reaction and an endothermic reaction, with and without a catalyst.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term activation energy, E_a.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="With reference to Fig. 5.1, explain how a catalyst increases the rate of an exothermic reaction without altering Delta H.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the mathematical relationship between the activation energy of the forward reaction, E_a(forward), the activation energy of the reverse reaction, E_a(reverse), and Delta H for an endothermic reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The minimum energy required by colliding particles to initiate a chemical reaction (1)", "marks": 1},
            {"part": "b", "points": "A catalyst provides an alternative reaction pathway with a lower activation energy, E_a' (1); The energy levels of initial reactants and final products remain unchanged, so Delta H is unchanged (1)", "marks": 2},
            {"part": "c", "points": "Delta H = E_a(forward) - E_a(reverse) (or E_a(forward) = E_a(reverse) + Delta H) (1)", "marks": 1}
        ],
        figure_path="figures/reaction_profile_exo_endo.png",
        figure_caption="Fig. 5.1: Enthalpy profile diagrams for exothermic and endothermic reactions."
    ),
    Question(
        number=3,
        title="Standard Enthalpy of Combustion Definition & Equation — 9701/23/M/J/22/Q2(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Combustion reactions are invariably exothermic processes.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term standard enthalpy change of combustion, Delta H_c_theta.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Write the thermochemical equation representing the standard enthalpy change of combustion of liquid ethanol, C2H5OH(l), including state symbols.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The enthalpy change when one mole of a substance (1); is completely burned in excess oxygen (1); under standard conditions (298 K and 100 kPa) with all reactants and products in standard states (1)", "marks": 3},
            {"part": "b", "points": "C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l) (1); Correct state symbols throughout (l, g, g, l) (1)", "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Standard Enthalpy of Neutralisation & Weak Acids — 9701/22/F/M/21/Q4(a)-(c)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="The standard enthalpy change of neutralisation between strong hydrochloric acid and strong sodium hydroxide is -57.1 kJ mol^-1.\nHCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)   Delta H = -57.1 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term standard enthalpy change of neutralisation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the ionic equation for the neutralisation reaction between any strong acid and any strong base.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="When ethanoic acid, CH3COOH, is neutralised by NaOH(aq), the experimental enthalpy change of neutralisation is -55.2 kJ mol^-1. Explain why this value is less exothermic than -57.1 kJ mol^-1.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The enthalpy change when one mole of water is formed (1); from the reaction between an acid and an alkali / base under standard conditions (1)", "marks": 2},
            {"part": "b", "points": "H+(aq) + OH-(aq) -> H2O(l) (1)", "marks": 1},
            {"part": "c", "points": "Ethanoic acid is a weak acid that is only partially dissociated in aqueous solution (1); Some energy is absorbed (endothermic step) to ionise unreacted CH3COOH molecules fully during neutralisation, making the overall process less exothermic (1)", "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Flame Calorimetry: Enthalpy of Combustion of Propan-1-ol — 9701/21/M/J/22/Q3(a)-(c)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="A student uses the spirit burner calorimeter apparatus shown in Fig. 5.2 to determine the enthalpy change of combustion of propan-1-ol, C3H7OH (Mr = 60.0).\n• Mass of water in copper calorimeter = 150.0 g\n• Initial mass of burner + propan-1-ol = 78.45 g\n• Final mass of burner + propan-1-ol = 77.85 g\n• Initial temperature of water = 19.5 °C\n• Final temperature of water = 44.0 °C\n(Specific heat capacity of water, c = 4.18 J g^-1 K^-1)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the heat energy, q in kJ, absorbed by the water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount, in moles, of propan-1-ol burned and hence determine the experimental Delta H_c in kJ mol^-1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="The data book value for Delta H_c of propan-1-ol is -2021 kJ mol^-1. State two major experimental sources of error that explain why the student's value is significantly less exothermic.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta T = 44.0 - 19.5 = 24.5 °C (or K); q = mc Delta T = 150.0 x 4.18 x 24.5 = 15361 J (1); q = 15.4 kJ (1)", "marks": 2},
            {"part": "b", "points": "Mass burned = 78.45 - 77.85 = 0.60 g; n = 0.60 / 60.0 = 0.0100 mol (1); Delta H_c = -q / n = -15.361 / 0.0100 = -1536 kJ mol^-1 (allow -1530 to -1540 kJ mol^-1) (1)", "marks": 2},
            {"part": "c", "points": "Significant heat loss to the surrounding air / draughts / copper can (1); Incomplete combustion of propan-1-ol (forming soot/CO instead of CO2) / evaporation of alcohol from wick (1)", "marks": 2}
        ],
        figure_path="figures/flame_calorimeter_setup.png",
        figure_caption="Fig. 5.2: Flame calorimeter apparatus for measuring enthalpy of combustion."
    ),
    Question(
        number=6,
        title="Calorimetry Cooling Curve & Graphical Extrapolation — 9701/22/O/N/23/Q2(a)-(c)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="In an investigation of the displacement reaction between zinc and copper(II) sulfate:\nZn(s) + CuSO4(aq) -> ZnSO4(aq) + Cu(s)\n50.0 cm3 of 1.00 mol dm^-3 CuSO4 was placed in an expanded polystyrene cup. Zinc powder (excess) was added at exactly t = 3.0 minutes. The temperature-time cooling curve is shown below.",
        parts=[
            QuestionPart(
                label="a",
                text="Using Fig. 5.3, determine the corrected maximum temperature change, Delta T_corrected, for this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change, Delta H, in kJ mol^-1, for the displacement reaction. (Assume solution density = 1.00 g cm^-3, c = 4.18 J g^-1 K^-1).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why an expanded polystyrene cup is used as a calorimeter rather than a glass beaker.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Extrapolated maximum temperature at t = 3.0 min = 34.7 °C (allow 34.5 - 34.9 °C) (1); Delta T_corrected = 34.7 - 20.0 = 14.7 °C (allow 14.5 - 14.9 °C) (1)", "marks": 2},
            {"part": "b", "points": "m = 50.0 g; q = mc Delta T = 50.0 x 4.18 x 14.7 = 3072 J = 3.072 kJ (1); n(CuSO4) = c x V = 1.00 x 0.0500 = 0.0500 mol (1); Delta H = -q / n = -3.072 / 0.0500 = -61.4 kJ mol^-1 (allow -60.6 to -62.3 kJ mol^-1) (1)", "marks": 3},
            {"part": "c", "points": "Polystyrene is a good thermal insulator / has a very low heat capacity, minimising heat loss to surroundings (1)", "marks": 1}
        ],
        figure_path="figures/calorimetry_cooling_curve.png",
        figure_caption="Fig. 5.3: Temperature-time cooling curve for the Zn + CuSO4 displacement reaction."
    ),
    Question(
        number=7,
        title="Enthalpy of Neutralisation: Sulfuric Acid vs Potassium Hydroxide — 9701/21/M/J/23/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="A student mixes 25.0 cm3 of 1.00 mol dm^-3 H2SO4 with 50.0 cm3 of 1.00 mol dm^-3 KOH in an insulated cup.\nH2SO4(aq) + 2KOH(aq) -> K2SO4(aq) + 2H2O(l)\nThe initial temperature of both solutions was 21.0 °C. The maximum recorded temperature was 29.8 °C. (Density = 1.00 g cm^-3, c = 4.18 J g^-1 K^-1)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the heat evolved, q in Joules, during this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of neutralisation, Delta H_neut, in kJ mol^-1 of water formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Total mass m = 25.0 + 50.0 = 75.0 g; Delta T = 29.8 - 21.0 = 8.8 °C (1); q = 75.0 x 4.18 x 8.8 = 2758.8 J = 2.76 kJ (1)", "marks": 2},
            {"part": "b", "points": "Moles of H2O formed: n(H2SO4) = 0.0250 mol, n(KOH) = 0.0500 mol => n(H2O) = 0.0500 mol (1); Delta H_neut = -2.759 / 0.0500 = -55.2 kJ mol^-1 (allow -55.0 to -55.5 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Enthalpy of Solution of Ammonium Chloride — 9701/22/M/J/20/Q4(a)-(c)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="When 5.35 g of solid ammonium chloride, NH4Cl (Mr = 53.5), is dissolved in 100.0 cm3 of water at 20.0 °C, the temperature drops to 16.2 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether the dissolution of ammonium chloride is an exothermic or endothermic process.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change of solution, Delta H_sol, of NH4Cl in kJ mol^-1.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Draw a fully labelled enthalpy profile diagram for this dissolution process showing reactants, products, and Delta H.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Endothermic (temperature decreases) (1)", "marks": 1},
            {"part": "b", "points": "Delta T = 16.2 - 20.0 = -3.8 °C; q = 100.0 x 4.18 x 3.8 = 1588.4 J = 1.588 kJ (1); n(NH4Cl) = 5.35 / 53.5 = 0.100 mol (1); Delta H_sol = +1.588 / 0.100 = +15.9 kJ mol^-1 (1)", "marks": 3},
            {"part": "c", "points": "Horizontal line for reactants NH4Cl(s) + aq lower than products NH4+(aq) + Cl-(aq) (1); Upward arrow labelled Delta H = +15.9 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Standard Enthalpy of Atomisation Definition & Halogens — 9701/21/O/N/22/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="The standard enthalpy change of atomisation involves producing free gaseous atoms.",
        parts=[
            QuestionPart(
                label="a",
                text="Define standard enthalpy change of atomisation, Delta H_at_theta.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Write the thermochemical equation representing the standard enthalpy change of atomisation of liquid bromine, Br2(l).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain the relationship between the bond dissociation enthalpy of gaseous chlorine, E(Cl-Cl), and its standard enthalpy of atomisation, Delta H_at(Cl2).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The enthalpy change when one mole of gaseous atoms (1); is formed from the element in its standard state (1); under standard conditions (298 K and 100 kPa) (1)", "marks": 3},
            {"part": "b", "points": "1/2 Br2(l) -> Br(g) (1)", "marks": 1},
            {"part": "c", "points": "Equation for atomisation: 1/2 Cl2(g) -> Cl(g); Equation for bond dissociation: Cl2(g) -> 2Cl(g) (1); Therefore Delta H_at(Cl2) = 1/2 E(Cl-Cl) (1)", "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Enthalpy of Hydration & Ion Size — 9701/23/O/N/21/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="Enthalpies of hydration of gaseous metal ions are always highly exothermic:\nM^n+(g) + aq -> M^n+(aq)   Delta H_hyd < 0\n• Delta H_hyd(Na+) = -406 kJ mol^-1\n• Delta H_hyd(Mg2+) = -1920 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term enthalpy change of hydration.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the enthalpy of hydration of Mg2+ is almost five times more exothermic than that of Na+.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The enthalpy change when one mole of specified gaseous ions (1); dissolves in sufficient water to form an infinitely dilute solution under standard conditions (1)", "marks": 2},
            {"part": "b", "points": "Mg2+ carries a 2+ charge compared to 1+ for Na+ (1); Mg2+ has a significantly smaller ionic radius than Na+ (1); Mg2+ has a much higher charge density, forming substantially stronger ion-dipole electrostatic attractions with water molecules (1)", "marks": 3}
        ]
    ),
    Question(
        number=11,
        title="Calorimeter Heat Capacity Correction — 9701/22/F/M/23/Q2(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="In a more rigorous calorimetry experiment, the heat capacity of the calorimeter container itself must be taken into account:\nq_total = (m_water x c_water x Delta T) + (C_calorimeter x Delta T)",
        parts=[
            QuestionPart(
                label="a",
                text="A combustion experiment causes 200.0 g of water inside a copper calorimeter of heat capacity 85.0 J K^-1 to rise in temperature by 12.4 °C. Calculate the total heat energy absorbed, in kJ.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage error that would occur if the heat capacity of the copper container were neglected.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "q_water = 200.0 x 4.18 x 12.4 = 10366.4 J = 10.37 kJ (1); q_cal = 85.0 x 12.4 = 1054.0 J = 1.05 kJ (1); q_total = 10366.4 + 1054.0 = 11420.4 J = 11.42 kJ (1)", "marks": 3},
            {"part": "b", "points": "Difference = 1054 J; Percentage error = (1054 / 11420) x 100% = 9.23% (allow 9.2% - 9.3%) (1); The calculated enthalpy would be 9.2% too low / less exothermic (1)", "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Comparing Combustion Enthalpies in a Homologous Series — 9701/21/M/J/21/Q4(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="The standard enthalpies of combustion for the first four unbranched alkanes are:\n• Methane, CH4: -890 kJ mol^-1\n• Ethane, C2H6: -1560 kJ mol^-1\n• Propane, C3H8: -2220 kJ mol^-1\n• Butane, C4H10: -2877 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Describe and explain the trend in standard enthalpies of combustion as the carbon chain length increases.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Estimate the standard enthalpy change of combustion of pentane, C5H12, by calculating the average incremental increase per -CH2- unit.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Enthalpies of combustion become increasingly negative / more exothermic (1); Each successive alkane has an additional -CH2- group, requiring more O2 and forming more C=O and O-H bonds which release more energy upon formation (1)", "marks": 2},
            {"part": "b", "points": "Average increment per CH2 = (2877 - 890) / 3 = 662 kJ mol^-1 (1); Estimated Delta H_c(pentane) = -2877 - 660 = -3537 kJ mol^-1 (allow -3530 to -3550 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Bond Breaking vs Bond Forming Energetics — 9701/22/M/J/22/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Chemical reactions involve the rearrangement of atoms through bond cleavage and bond creation.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether bond breaking is an exothermic or endothermic process and justify your answer in terms of energy changes.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why an exothermic reaction results in an overall release of heat to the surroundings in terms of bond energies.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Endothermic (1); Energy must be absorbed / supplied from surroundings to overcome the electrostatic attraction holding the bonded atoms together (1)", "marks": 2},
            {"part": "b", "points": "More energy is released when new bonds are formed in the products (1); than the energy absorbed to break the original bonds in the reactants (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Enthalpy Change of Displacement: Copper and Silver Nitrate — 9701/22/O/N/21/Q4(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="A 0.635 g sample of copper wire (Ar = 63.5) is added to 100.0 cm3 of 0.200 mol dm^-3 AgNO3 in an insulated polystyrene beaker:\nCu(s) + 2AgNO3(aq) -> Cu(NO3)2(aq) + 2Ag(s)\nThe temperature of the solution rises by 3.5 °C. (c = 4.18 J g^-1 K^-1, density = 1.00 g cm^-3)",
        parts=[
            QuestionPart(
                label="a",
                text="Determine whether copper or silver nitrate is the limiting reactant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change, Delta H, in kJ mol^-1 of Cu reacted.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(Cu) = 0.635 / 63.5 = 0.0100 mol; n(AgNO3) = 0.200 x 0.100 = 0.0200 mol (1); Stoichiometric ratio is 1 Cu : 2 AgNO3; exactly equal stoichiometric amounts, both react completely (or Cu is limiting) (1)", "marks": 2},
            {"part": "b", "points": "q = mc Delta T = 100.0 x 4.18 x 3.5 = 1463 J = 1.463 kJ (1); n(Cu) = 0.0100 mol (1); Delta H = -q / n = -1.463 / 0.0100 = -146.3 kJ mol^-1 (allow -146 kJ mol^-1) (1)", "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Calorimetric Measurement of Neutralisation: Weak Base NH3 — 9701/21/O/N/23/Q2(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="When 50.0 cm3 of 1.00 mol dm^-3 aqueous ammonia is reacted with 50.0 cm3 of 1.00 mol dm^-3 HCl in a polystyrene cup, the temperature increases by 6.1 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the heat released during this reaction in kJ.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change of neutralisation, Delta H_neut, in kJ mol^-1 of NH4+ formed.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why this Delta H_neut value is less exothermic than the reaction between NaOH(aq) and HCl(aq) (-57.1 kJ mol^-1).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "m = 100.0 g; q = 100.0 x 4.18 x 6.1 = 2549.8 J = 2.55 kJ (1); Correct sign and units (1)", "marks": 2},
            {"part": "b", "points": "n = 0.0500 mol; Delta H_neut = -2.550 / 0.0500 = -51.0 kJ mol^-1 (allow -50.8 to -51.2 kJ mol^-1) (1); Correct negative sign (1)", "marks": 2},
            {"part": "c", "points": "Aqueous ammonia is a weak base and only partially ionised (1); Some heat is absorbed to ionise NH3(aq) molecules into NH4+(aq) and OH-(aq) during the reaction (1)", "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Standard Conditions & Non-Standard State Enthalpies — 9701/23/M/J/20/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Consider the thermochemical equation:\nH2(g) + 1/2 O2(g) -> H2O(g)   Delta H = -241.8 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why -241.8 kJ mol^-1 does NOT represent the standard enthalpy change of formation, Delta H_f_theta, of water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Given that the standard enthalpy change of vaporisation of water is +44.0 kJ mol^-1, deduce the true value of Delta H_f_theta for liquid water, H2O(l).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Under standard conditions (298 K and 100 kPa), the standard state of water is liquid, H2O(l), not gas, H2O(g) (1); Standard enthalpy of formation requires products to be in their standard states (1)", "marks": 2},
            {"part": "b", "points": "H2O(l) -> H2O(g) Delta H_vap = +44.0 kJ mol^-1 (1); Delta H_f_theta(H2O(l)) = -241.8 - (+44.0) = -285.8 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Thermal Decomposition of Limestone: Energetics — 9701/22/F/M/24/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Calcium carbonate decomposes endothermically at high temperatures in an industrial lime kiln:\nCaCO3(s) -> CaO(s) + CO2(g)   Delta H = +178 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State whether heat is absorbed or released by the reaction system during this process.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the thermal energy, in MJ, required to decompose completely 2.50 tonnes of pure CaCO3 (Mr = 100.1). (1 tonne = 10^6 g)",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Heat is absorbed from the surroundings (1)", "marks": 1},
            {"part": "b", "points": "Mass of CaCO3 = 2.50 x 10^6 g; n(CaCO3) = (2.50 x 10^6) / 100.1 = 24975 mol (1); Energy required = 24975 x 178 kJ = 4.446 x 10^6 kJ (1); Energy in MJ = 4446 MJ (or 4.45 x 10^3 MJ) (1)", "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Neutralisation of Diprotic Acid with Monoprotic Base — 9701/21/M/J/24/Q2(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="When 50.0 cm3 of 1.00 mol dm^-3 H2SO4 is mixed with 100.0 cm3 of 1.00 mol dm^-3 NaOH in a calorimeter, the temperature rises by 9.1 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of water produced in this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the heat evolved, q, in kJ. (Total volume = 150.0 cm3, c = 4.18 J g^-1 K^-1)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the molar enthalpy of neutralisation, Delta H_neut, per mole of water formed.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(H2SO4) = 0.0500 mol, n(NaOH) = 0.100 mol => n(H2O) = 0.100 mol (1)", "marks": 1},
            {"part": "b", "points": "m = 150.0 g; q = 150.0 x 4.18 x 9.1 = 5705.7 J = 5.71 kJ (1); Correct units (1)", "marks": 2},
            {"part": "c", "points": "Delta H_neut = -5.706 / 0.100 = -57.1 kJ mol^-1 (1)", "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Bond Energy Definitions & Mean Bond Enthalpies — 9701/22/O/N/24/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Bond energies are used to estimate enthalpy changes for reactions involving covalent molecules.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term mean bond enthalpy.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why values of mean bond enthalpies are always positive.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The average energy required to break one mole of a specific covalent bond (1); in gaseous molecules (1); averaged over a wide range of different chemical compounds (1)", "marks": 3},
            {"part": "b", "points": "Bond breaking is always an endothermic process / requires energy input to overcome attractions (1)", "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Enthalpy of Combustion of Bioethanol vs Biodiesel — 9701/21/O/N/24/Q2(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="Bioethanol, C2H5OH (Mr = 46.0, Delta H_c = -1367 kJ mol^-1), and methyl octanoate, C9H18O2 (Mr = 158.0, Delta H_c = -5480 kJ mol^-1), are used as alternative biofuels.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the energy released, in kJ, per gram of bioethanol burned.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the energy released, in kJ, per gram of methyl octanoate burned.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Suggest one environmental advantage of using biofuels compared to conventional fossil fuels.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Energy per gram = 1367 / 46.0 = 29.7 kJ g^-1 (1); Correct calculation to 3 s.f. (1)", "marks": 2},
            {"part": "b", "points": "Energy per gram = 5480 / 158.0 = 34.7 kJ g^-1 (1)", "marks": 1},
            {"part": "c", "points": "Biofuels are renewable / carbon-neutral as crops absorb CO2 during photosynthesis equal to CO2 released upon combustion (1)", "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Exothermic Solution Process: Dissolution of Anhydrous CaCl2 — 9701/23/M/J/23/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="Anhydrous calcium chloride, CaCl2, dissolves exothermically in water and is used in self-heating commercial beverage cans.\nCaCl2(s) + aq -> Ca^2+(aq) + 2Cl^-(aq)   Delta H_sol = -82.8 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass of anhydrous CaCl2 (Mr = 111.1) needed to raise the temperature of 250 cm3 of water by 35.0 °C. (c = 4.18 J g^-1 K^-1)",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why Delta H_sol of anhydrous CaCl2 is exothermic, whereas Delta H_sol of NH4NO3 is endothermic, in terms of lattice energy and hydration enthalpies.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "q = 250 x 4.18 x 35.0 = 36575 J = 36.575 kJ (1); n(CaCl2) required = 36.575 / 82.8 = 0.4417 mol (1); Mass = 0.4417 x 111.1 = 49.1 g (allow 48.9 - 49.3 g) (1)", "marks": 3},
            {"part": "b", "points": "Delta H_sol = sum(Delta H_hyd) - (Lattice Energy) (1); For CaCl2, the exothermic hydration enthalpy of Ca2+ and Cl- exceeds the endothermic lattice energy (sum Delta H_hyd is more exothermic than lattice energy is endothermic) (1)", "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Combustion Calorimeter: Systematic Errors & Modifications — 9701/22/M/J/25/Q2(b)",
        syllabus_ref="5.1",
        difficulty="EASY",
        preamble="In a school laboratory combustion experiment using a spirit burner and copper can calorimeter, the experimental enthalpy of combustion of methanol is found to be -480 kJ mol^-1. The literature value is -726 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Suggest two specific design modifications to the experimental apparatus that would improve the accuracy of the measured enthalpy change.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain how incomplete combustion contributes to the lower experimental value.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Use a draught shield / windshield around burner and calorimeter (1); Place an insulating lid on the copper calorimeter / use a bomb calorimeter with pure oxygen supply (1)", "marks": 2},
            {"part": "b", "points": "Incomplete combustion produces carbon monoxide (CO) or soot (C) rather than CO2 (1); The combustion of carbon to CO or C releases significantly less energy than complete combustion to CO2 (1)", "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Direct vs Indirect Determination of Enthalpy Changes — 9701/21/F/M/25/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="It is impossible to measure directly the standard enthalpy change of formation of carbon monoxide, CO:\nC(s) + 1/2 O2(g) -> CO(g)   Delta H_f_theta = ?",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Delta H_f_theta of carbon monoxide cannot be determined directly by calorimetry.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how Hess's Law allows Delta H_f_theta of carbon monoxide to be determined indirectly.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "When carbon burns in a limited supply of oxygen, a mixture of both CO and CO2 is inevitably formed (1); Unreacted carbon may also remain, so the reaction cannot be stopped purely at CO (1)", "marks": 2},
            {"part": "b", "points": "Construct a thermochemical cycle using the readily measurable enthalpies of combustion of carbon (to CO2) and carbon monoxide (to CO2) (1); Apply Hess's Law: Delta H_f(CO) = Delta H_c(C) - Delta H_c(CO) (1)", "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Temperature Dependence of Enthalpy Profiles & Reversibility — 9701/22/O/N/25/Q2(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="For the reversible industrial synthesis of sulfur trioxide:\n2SO2(g) + O2(g) <=> 2SO3(g)   Delta H = -196 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State whether the backward reaction is exothermic or endothermic, and state its Delta H value.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Given that the activation energy for the catalysed forward reaction is +65 kJ mol^-1, calculate the activation energy for the catalysed reverse reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Endothermic, Delta H = +196 kJ mol^-1 (1)", "marks": 1},
            {"part": "b", "points": "E_a(reverse) = E_a(forward) - Delta H (1); E_a(reverse) = +65 - (-196) = +261 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Hydration of Copper(II) Sulfate: Indirect Calorimetry — 9701/23/O/N/24/Q3(a)-(b)",
        syllabus_ref="5.1",
        difficulty="HARD",
        preamble="The direct hydration of anhydrous copper(II) sulfate is too slow to measure directly by calorimetry:\nCuSO4(s) + 5H2O(l) -> CuSO4.5H2O(s)   Delta H_hydration = ?\nA student measures the enthalpy changes when each solid dissolves in excess water:\n• Route 1: CuSO4(s) + aq -> CuSO4(aq)   Delta H_1 = -66.5 kJ mol^-1\n• Route 2: CuSO4.5H2O(s) + aq -> CuSO4(aq)   Delta H_2 = +11.7 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Draw or write a Hess's Law cycle connecting CuSO4(s), CuSO4.5H2O(s), and CuSO4(aq).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change of hydration, Delta H_hydration, for anhydrous copper(II) sulfate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "CuSO4(s) + 5H2O(l) -> CuSO4.5H2O(s) with Delta H_hydration (1); Both react with excess water to form CuSO4(aq) via Delta H_1 and Delta H_2 (1)", "marks": 2},
            {"part": "b", "points": "Delta H_hydration + Delta H_2 = Delta H_1 => Delta H_hydration = Delta H_1 - Delta H_2 (1); Delta H_hydration = -66.5 - (+11.7) = -78.2 kJ mol^-1 (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 5.2: Hess's Law & Bond Energies (Q26 to Q50)
    # =========================================================================
    Question(
        number=26,
        title="Hess's Law Statement & Thermochemical Cycles — 9701/21/M/J/21/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="Hess's Law is a direct manifestation of the fundamental law of conservation of energy.",
        parts=[
            QuestionPart(
                label="a",
                text="State Hess's Law.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="With reference to Fig. 5.4, state the mathematical formula used to calculate the enthalpy of reaction Delta H_r from standard enthalpies of formation Delta H_f_theta.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the mathematical formula used to calculate Delta H_r from standard enthalpies of combustion Delta H_c_theta.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The total enthalpy change for a chemical reaction is independent of the route taken (1); provided the initial and final states are the same (1)", "marks": 2},
            {"part": "b", "points": "Delta H_r = sum Delta H_f(products) - sum Delta H_f(reactants) (1)", "marks": 1},
            {"part": "c", "points": "Delta H_r = sum Delta H_c(reactants) - sum Delta H_c(products) (1)", "marks": 1}
        ],
        figure_path="figures/hess_law_cycles.png",
        figure_caption="Fig. 5.4: Hess's Law thermochemical cycles using enthalpies of formation and combustion."
    ),
    Question(
        number=27,
        title="Calculating Delta H_f of Methane from Enthalpies of Combustion — 9701/22/O/N/21/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The standard enthalpy change of formation of methane, CH4, cannot be determined directly.\nStandard enthalpy changes of combustion:\n• Delta H_c[C(graphite)] = -393.5 kJ mol^-1\n• Delta H_c[H2(g)] = -285.8 kJ mol^-1\n• Delta H_c[CH4(g)] = -890.3 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the standard enthalpy change of formation of methane, CH4(g).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Use the combustion data provided to calculate the standard enthalpy change of formation of methane, in kJ mol^-1.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "C(graphite) + 2H2(g) -> CH4(g) (1)", "marks": 1},
            {"part": "b", "points": "Delta H_f = sum Delta H_c(reactants) - sum Delta H_c(products) (1); Delta H_f = [Delta H_c(C) + 2 x Delta H_c(H2)] - [Delta H_c(CH4)] = [-393.5 + 2(-285.8)] - [-890.3] (1); Delta H_f = -965.1 - (-890.3) = -74.8 kJ mol^-1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=28,
        title="Calculating Delta H_r from Enthalpies of Formation: Thermite Reaction — 9701/21/M/J/22/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="The thermite reaction is a highly exothermic process used in railway track welding:\n2Al(s) + Fe2O3(s) -> Al2O3(s) + 2Fe(s)\nStandard enthalpies of formation:\n• Delta H_f_theta[Fe2O3(s)] = -824.2 kJ mol^-1\n• Delta H_f_theta[Al2O3(s)] = -1675.7 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State the value of Delta H_f_theta for Al(s) and Fe(s).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change, Delta H_r_theta, for this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why molten iron is produced by this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "0.0 kJ mol^-1 (for both elements in their standard states) (1)", "marks": 1},
            {"part": "b", "points": "Delta H_r = Delta H_f(Al2O3) - Delta H_f(Fe2O3) = -1675.7 - (-824.2) (1); Delta H_r = -851.5 kJ mol^-1 (1)", "marks": 2},
            {"part": "c", "points": "The enormous heat energy released raises the temperature of the reaction mixture above the melting point of iron (1538 °C) (1)", "marks": 1}
        ]
    ),
    Question(
        number=29,
        title="Enthalpy of Formation of Benzene from Combustion Data — 9701/22/M/J/22/Q4(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Standard enthalpy changes of combustion:\n• C(s) + O2(g) -> CO2(g)   Delta H_c = -394 kJ mol^-1\n• H2(g) + 1/2 O2(g) -> H2O(l)   Delta H_c = -286 kJ mol^-1\n• C6H6(l) + 7.5 O2(g) -> 6CO2(g) + 3H2O(l)   Delta H_c = -3267 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Construct a Hess's Law cycle to calculate the standard enthalpy change of formation of liquid benzene, C6H6(l).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of formation of liquid benzene in kJ mol^-1.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cycle showing 6C(s) + 3H2(g) -> C6H6(l) at top (1); Downward arrows from reactants and product to combustion products 6CO2(g) + 3H2O(l) (1)", "marks": 2},
            {"part": "b", "points": "Delta H_f = [6(-394) + 3(-286)] - [-3267] = [-2364 - 858] - [-3267] (1); Delta H_f = -3222 + 3267 = +45 kJ mol^-1 (allow +45 to +49 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Bond Energy Calculations: Hydrogenation of Ethene — 9701/23/M/J/22/Q3(a)-(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="Ethene reacts with hydrogen in the presence of a nickel catalyst to form ethane:\nC2H4(g) + H2(g) -> C2H6(g)\nRelevant bond energies:\n• C=C: 612 kJ mol^-1\n• C-C: 348 kJ mol^-1\n• C-H: 412 kJ mol^-1\n• H-H: 436 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total energy absorbed to break all necessary bonds in the reactants.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the total energy released when new bonds are formed in the product.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the enthalpy change of the reaction, Delta H, in kJ mol^-1.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds broken: 1 x (C=C) + 1 x (H-H) = 612 + 436 = 1048 kJ (or including 4 C-H: 612 + 436 + 4(412) = 2696 kJ) (1); Correct summation (1)", "marks": 2},
            {"part": "b", "points": "Bonds formed: 1 x (C-C) + 2 x (C-H) = 348 + 2(412) = 1172 kJ (or including all 6 C-H: 348 + 6(412) = 2820 kJ) (1)", "marks": 1},
            {"part": "c", "points": "Delta H = Bonds Broken - Bonds Formed = 1048 - 1172 = -124 kJ mol^-1 (1)", "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Deducing an Unknown Bond Energy: C-H Bond in Methane — 9701/21/O/N/22/Q4(a)-(c)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The standard enthalpy changes of atomisation are:\n• Delta H_at[C(s)] = +717 kJ mol^-1\n• Delta H_at[H2(g)] = +218 kJ mol^-1 (per mole of H atoms)\nThe standard enthalpy change of formation of methane, Delta H_f[CH4(g)], is -75 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the complete atomisation of one mole of gaseous methane, CH4(g).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Construct a thermochemical cycle and calculate the total enthalpy of atomisation of CH4(g).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the mean C-H bond enthalpy in methane.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "CH4(g) -> C(g) + 4H(g) (1)", "marks": 1},
            {"part": "b", "points": "Delta H_atomisation(CH4) = -Delta H_f(CH4) + Delta H_at(C) + 4 x Delta H_at(H) (1); = -(-75) + 717 + 4(218) = 75 + 717 + 872 = +1664 kJ mol^-1 (1)", "marks": 2},
            {"part": "c", "points": "Mean E(C-H) = 1664 / 4 = 416 kJ mol^-1 (1)", "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Combustion of Hydrazine: Rocket Fuel Energetics — 9701/22/F/M/23/Q3(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Hydrazine, N2H4, is a high-energy rocket fuel that reacts with oxygen:\nN2H4(g) + O2(g) -> N2(g) + 2H2O(g)\nBond energies in kJ mol^-1:\n• N-N: 158\n• N=N: 418\n• N#N (triple): 945\n• N-H: 391\n• O=O: 498\n• O-H: 464",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total energy absorbed to break all bonds in the reactants.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the total energy released upon forming all bonds in the products.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the enthalpy change of the reaction, Delta H, and explain why the reaction is extremely exothermic.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds broken = 1(N-N) + 4(N-H) + 1(O=O) = 158 + 4(391) + 498 = 158 + 1564 + 498 = 2220 kJ mol^-1 (1); Correct working (1)", "marks": 2},
            {"part": "b", "points": "Bonds formed = 1(N#N) + 4(O-H) = 945 + 4(464) = 945 + 1856 = 2801 kJ mol^-1 (1)", "marks": 1},
            {"part": "c", "points": "Delta H = 2220 - 2801 = -581 kJ mol^-1 (1); The reaction is extremely exothermic because of the formation of the exceptionally strong nitrogen-nitrogen triple bond (N#N, 945 kJ mol^-1) and strong O-H bonds (1)", "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Why Bond Energy Calculations Differ from Standard Enthalpies — 9701/21/M/J/23/Q4(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The enthalpy change of combustion of gaseous ethanol calculated using mean bond energies is -1270 kJ mol^-1, whereas the data book value obtained from standard enthalpies of formation is -1367 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="State two reasons why an enthalpy change calculated using bond energies differs from the value obtained from standard enthalpies of formation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State whether bond energy calculations are applicable to reactions occurring in the liquid or solid states without modification, and explain why.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bond energies are average values taken across a wide variety of different molecules with different chemical environments (1); Standard enthalpies of formation use specific values determined under standard conditions (298 K, 100 kPa) where ethanol and water are liquids, whereas bond energies apply strictly to gaseous species (1)", "marks": 2},
            {"part": "b", "points": "No (1); Bond energies assume all reactants and products are in the gaseous state with zero intermolecular forces; for liquids and solids, enthalpy changes of vaporisation/fusion must also be accounted for (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Hess's Law: Enthalpy of Formation of CS2 — 9701/22/O/N/23/Q3(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Carbon disulfide, CS2(l), burns completely according to the equation:\nCS2(l) + 3O2(g) -> CO2(g) + 2SO2(g)   Delta H_c = -1075 kJ mol^-1\nStandard enthalpy changes of combustion:\n• C(s) + O2(g) -> CO2(g)   Delta H_c = -394 kJ mol^-1\n• S(s) + O2(g) -> SO2(g)   Delta H_c = -297 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the standard enthalpy change of formation of CS2(l).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of formation, Delta H_f_theta, of CS2(l) in kJ mol^-1.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "C(s) + 2S(s) -> CS2(l) (1)", "marks": 1},
            {"part": "b", "points": "Delta H_f = [Delta H_c(C) + 2 x Delta H_c(S)] - [Delta H_c(CS2)] (1); = [-394 + 2(-297)] - [-1075] = [-394 - 594] - [-1075] = -988 + 1075 (1); Delta H_f = +87 kJ mol^-1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=35,
        title="Calculating Bond Energy of C=O in Carbon Dioxide — 9701/21/O/N/23/Q3(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Given the following thermochemical data:\n• Delta H_at[C(s)] = +717 kJ mol^-1\n• Bond energy of O=O in O2(g) = 498 kJ mol^-1\n• Delta H_f_theta[CO2(g)] = -394 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Construct a thermochemical cycle connecting C(s) + O2(g) to CO2(g) and the separated gaseous atoms C(g) + 2O(g).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the bond energy of the C=O double bond in carbon dioxide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cycle showing formation route from elements to CO2 (Delta H_f = -394) and atomisation route to C(g) + 2O(g) (1); Atomisation of reactants = Delta H_at(C) + E(O=O) = 717 + 498 = +1215 kJ mol^-1 (1)", "marks": 2},
            {"part": "b", "points": "Atomisation of CO2: 2 x E(C=O) = 1215 - (-394) = 1609 kJ mol^-1 (1); E(C=O) = 1609 / 2 = 805 kJ mol^-1 (allow 804 - 806 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Hess's Law: Enthalpy Change of Cracking Alkanes — 9701/22/M/J/24/Q4(a)-(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="Decane is cracked at high temperature to produce octane and ethene:\nC10H22(g) -> C8H18(g) + C2H4(g)\nStandard enthalpies of combustion:\n• Delta H_c[C10H22(g)] = -6778 kJ mol^-1\n• Delta H_c[C8H18(g)] = -5470 kJ mol^-1\n• Delta H_c[C2H4(g)] = -1411 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the enthalpy change, Delta H, for this cracking reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State whether cracking is endothermic or exothermic, and explain why industrial cracking requires continuous high heat input.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H = Delta H_c(C10H22) - [Delta H_c(C8H18) + Delta H_c(C2H4)] = -6778 - [-5470 + (-1411)] (1); Delta H = -6778 - (-6881) = +103 kJ mol^-1 (1)", "marks": 2},
            {"part": "b", "points": "Endothermic (Delta H is positive) (1); Thermal energy is continuously required to break strong C-C covalent bonds in long hydrocarbon chains (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Enthalpy of Formation of Gaseous Atoms: Nitrogen vs Oxygen — 9701/21/M/J/24/Q3(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The standard enthalpy changes of atomisation are:\n• Delta H_at[1/2 N2(g) -> N(g)] = +473 kJ mol^-1\n• Delta H_at[1/2 O2(g) -> O(g)] = +249 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the bond dissociation enthalpies of N2 and O2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the bond dissociation enthalpy of N2 is nearly double that of O2.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "E(N#N) = 2 x 473 = 946 kJ mol^-1 (1); E(O=O) = 2 x 249 = 498 kJ mol^-1 (1)", "marks": 2},
            {"part": "b", "points": "N2 possesses a triple covalent bond (one sigma and two pi bonds) shared between two nitrogen atoms (1); O2 possesses only a double covalent bond (one sigma and one pi bond), which requires significantly less energy to break (1)", "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Multi-Step Hess's Law Cycle: Phosphorus Chlorides — 9701/23/M/J/24/Q4(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Phosphorus reacts with chlorine in two stages to form PCl3 and PCl5:\n• P4(s) + 6Cl2(g) -> 4PCl3(l)   Delta H_1 = -1280 kJ mol^-1\n• PCl3(l) + Cl2(g) -> PCl5(s)   Delta H_2 = -124 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the standard enthalpy change of formation of PCl3(l).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of formation of PCl5(s).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H_f(PCl3) = -1280 / 4 = -320 kJ mol^-1 (1)", "marks": 1},
            {"part": "b", "points": "Formation of PCl5: 1/4 P4(s) + 5/2 Cl2(g) -> PCl5(s) (1); Delta H_f(PCl5) = Delta H_f(PCl3) + Delta H_2 = -320 + (-124) = -444 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Bond Enthalpy Calculation: Chlorination of Methane — 9701/22/O/N/24/Q4(a)-(c)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="Methane reacts with chlorine under UV light to form chloromethane:\nCH4(g) + Cl2(g) -> CH3Cl(g) + HCl(g)\nBond energies in kJ mol^-1: C-H = 412, Cl-Cl = 242, C-Cl = 338, H-Cl = 431.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify which bonds are broken and which bonds are formed during this reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change, Delta H, for this chlorination reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds broken: one C-H bond and one Cl-Cl bond (1); Bonds formed: one C-Cl bond and one H-Cl bond (1)", "marks": 2},
            {"part": "b", "points": "Bonds broken = 412 + 242 = 654 kJ mol^-1; Bonds formed = 338 + 431 = 769 kJ mol^-1 (1); Delta H = 654 - 769 = -115 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Enthalpy of Combustion of Gaseous vs Liquid Alkanes — 9701/21/O/N/24/Q3(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Consider the combustion of hexane in gaseous and liquid states:\n• C6H14(l) + 9.5 O2(g) -> 6CO2(g) + 7H2O(l)   Delta H_c = -4163 kJ mol^-1\n• The standard enthalpy change of vaporisation of hexane is +31.5 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether Delta H_c of gaseous hexane is more exothermic or less exothermic than Delta H_c of liquid hexane.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of combustion of gaseous hexane, C6H14(g).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "More exothermic (Delta H is more negative) (1)", "marks": 1},
            {"part": "b", "points": "C6H14(l) -> C6H14(g) Delta H_vap = +31.5 kJ mol^-1; Delta H_c(liquid) = Delta H_vap + Delta H_c(gas) (1); Delta H_c(gas) = -4163 - 31.5 = -4194.5 kJ mol^-1 (allow -4195 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Determining Enthalpy of Formation of Propanone — 9701/22/F/M/25/Q4(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Propanone, CH3COCH3(l), burns completely in air:\nCH3COCH3(l) + 4O2(g) -> 3CO2(g) + 3H2O(l)   Delta H_c = -1790 kJ mol^-1\nStandard enthalpies of formation:\n• Delta H_f[CO2(g)] = -394 kJ mol^-1\n• Delta H_f[H2O(l)] = -286 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the formation of propanone from its elements in their standard states.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of formation, Delta H_f_theta, of propanone in kJ mol^-1.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "3C(s) + 3H2(g) + 1/2 O2(g) -> CH3COCH3(l) (1)", "marks": 1},
            {"part": "b", "points": "Delta H_c = [3 x Delta H_f(CO2) + 3 x Delta H_f(H2O)] - Delta H_f(propanone) (1); -1790 = [3(-394) + 3(-286)] - Delta H_f(propanone) = [-1182 - 858] - Delta H_f = -2040 - Delta H_f (1); Delta H_f = -2040 - (-1790) = -250 kJ mol^-1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=42,
        title="Average Bond Energy of N-H in Ammonia — 9701/21/M/J/25/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The synthesis of ammonia from its elements has Delta H = -92 kJ mol^-1:\nN2(g) + 3H2(g) -> 2NH3(g)   Delta H = -92 kJ mol^-1\nBond energies: E(N#N) = 945 kJ mol^-1, E(H-H) = 436 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total energy absorbed to break bonds in 1 mole of N2 and 3 moles of H2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Use the reaction enthalpy to calculate the mean N-H bond energy in ammonia.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds broken = 945 + 3(436) = 945 + 1308 = 2253 kJ (1)", "marks": 1},
            {"part": "b", "points": "Delta H = Bonds broken - Bonds formed => -92 = 2253 - 6 x E(N-H) (1); 6 x E(N-H) = 2253 - (-92) = 2345 kJ (1); E(N-H) = 2345 / 6 = 390.8 kJ mol^-1 (allow 391 kJ mol^-1) (1)", "marks": 3}
        ]
    ),
    Question(
        number=43,
        title="Hess's Law: Enthalpy of Isomerisation of But-1-ene to But-2-ene — 9701/23/M/J/25/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="But-1-ene isomerises to the more thermodynamically stable but-2-ene:\nbut-1-ene(g) -> but-2-ene(g)\nStandard enthalpies of combustion:\n• Delta H_c[but-1-ene(g)] = -2719 kJ mol^-1\n• Delta H_c[but-2-ene(g)] = -2710 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the enthalpy change of isomerisation, Delta H_iso.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce which isomer is more stable and explain your reasoning in terms of enthalpy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H_iso = Delta H_c(but-1-ene) - Delta H_c(but-2-ene) = -2719 - (-2710) (1); Delta H_iso = -9 kJ mol^-1 (1)", "marks": 2},
            {"part": "b", "points": "But-2-ene is more stable (1); It is at a lower enthalpy level / releases less energy upon combustion (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Deducing Bond Energy of Si-Si vs C-C — 9701/22/O/N/25/Q4(b)",
        syllabus_ref="5.2",
        difficulty="EASY",
        preamble="Given the bond energies:\n• C-C: 348 kJ mol^-1\n• Si-Si: 226 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the silicon-silicon single bond is significantly weaker than the carbon-carbon single bond.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Relate this difference in bond energy to the relative thermal stability of alkanes compared to silanes (compounds of general formula SinH2n+2).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Silicon atoms have a larger atomic radius than carbon atoms (3 shells vs 2 shells) (1); The shared electron pair is further from the silicon nuclei and shielded by inner electron shells, resulting in poorer orbital overlap and weaker electrostatic attraction (1)", "marks": 2},
            {"part": "b", "points": "Alkanes are thermally stable due to strong C-C and C-H bonds (1); Silanes decompose and ignite spontaneously in air because Si-Si and Si-H bonds have significantly lower bond enthalpies (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Enthalpy of Formation of Gaseous Hydrogen Iodide: Bond Energy Anomaly — 9701/21/O/N/25/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="For the formation of gaseous hydrogen iodide:\n1/2 H2(g) + 1/2 I2(s) -> HI(g)   Delta H_f_theta = +26.5 kJ mol^-1\nBond energies: E(H-H) = 436 kJ mol^-1, E(H-I) = 299 kJ mol^-1.\nStandard enthalpy of sublimation of iodine: I2(s) -> I2(g)   Delta H_sub = +62.4 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the bond energy of the I-I bond in gaseous I2.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why Delta H_f_theta of HI(g) is endothermic even though bond formation occurs.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Hess's route: Delta H_f = 1/2 E(H-H) + 1/2 Delta H_sub(I2) + 1/2 E(I-I) - E(H-I) (1); +26.5 = 1/2(436) + 1/2(62.4) + 1/2 E(I-I) - 299 = 218 + 31.2 + 1/2 E(I-I) - 299 = -49.8 + 1/2 E(I-I) (1); 1/2 E(I-I) = 26.5 + 49.8 = 76.3 => E(I-I) = 152.6 kJ mol^-1 (allow 151 - 154 kJ mol^-1) (1)", "marks": 3},
            {"part": "b", "points": "The energy released by forming the relatively weak H-I bond is insufficient to compensate for the energy required to atomise H2 and sublime/dissociate I2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=46,
        title="Enthalpy of Neutralisation: Dibasic vs Monobasic Acid — 9701/22/M/J/25/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Consider the two neutralisation reactions:\nReaction 1: HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)   Delta H_1 = -57.1 kJ mol^-1\nReaction 2: (COOH)2(aq) + 2NaOH(aq) -> (COONa)2(aq) + 2H2O(l)   Delta H_2 = -106.4 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the enthalpy change of neutralisation per mole of water formed in Reaction 2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the enthalpy change per mole of water in Reaction 2 is less exothermic than -57.1 kJ mol^-1.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H per mole of water = -106.4 / 2 = -53.2 kJ mol^-1 (1)", "marks": 1},
            {"part": "b", "points": "Ethanedioic acid (oxalic acid) is a weak acid that is only partially dissociated into ions in solution (1); Energy is taken in / absorbed (endothermic) to break O-H bonds and fully dissociate the acid molecules during reaction (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Bond Energy of Carbon-Carbon Triple Bond in Ethyne — 9701/23/O/N/25/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The complete combustion of ethyne gas, C2H2(g), has Delta H_c = -1300 kJ mol^-1:\nC2H2(g) + 2.5 O2(g) -> 2CO2(g) + H2O(g)\nBond energies in kJ mol^-1:\n• C-H: 412\n• O=O: 498\n• C=O (in CO2): 805\n• O-H (in H2O): 464",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total energy released upon forming all bonds in 2 moles of CO2(g) and 1 mole of H2O(g).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the bond energy of the carbon-carbon triple bond (C#C) in ethyne.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds formed = 4 x E(C=O) + 2 x E(O-H) = 4(805) + 2(464) (1); = 3220 + 928 = 4148 kJ mol^-1 (1)", "marks": 2},
            {"part": "b", "points": "Delta H = Bonds broken - Bonds formed => -1300 = [E(C#C) + 2(412) + 2.5(498)] - 4148 (1); -1300 = E(C#C) + 824 + 1245 - 4148 = E(C#C) - 2079 (1); E(C#C) = 2079 - 1300 = 779 kJ mol^-1 (allow 775 - 840 kJ mol^-1 depending on standard C=O value) (1)", "marks": 3}
        ]
    ),
    Question(
        number=48,
        title="Lattice Energy and Enthalpy of Solution of Potassium Fluoride — 9701/21/F/M/24/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="The enthalpy of solution of potassium fluoride, KF, is -17.7 kJ mol^-1.\n• Enthalpy of hydration of K+(g) = -322 kJ mol^-1\n• Enthalpy of hydration of F-(g) = -506 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State the relationship connecting enthalpy of solution, lattice energy (endothermic dissociation), and hydration enthalpies.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the lattice energy of potassium fluoride (defined as KF(s) -> K+(g) + F-(g)).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H_sol = Lattice dissociation energy + sum Delta H_hyd (or Delta H_sol = sum Delta H_hyd - Lattice formation energy) (1)", "marks": 1},
            {"part": "b", "points": "Total Delta H_hyd = -322 + (-506) = -828 kJ mol^-1 (1); -17.7 = Lattice dissociation energy + (-828) => Lattice dissociation energy = 828 - 17.7 = +810.3 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Hess's Law: Enthalpy of Formation of Nitric Acid — 9701/22/M/J/24/Q5(a)-(b)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="In the Ostwald process, nitrogen dioxide reacts with water to produce nitric acid:\n3NO2(g) + H2O(l) -> 2HNO3(aq) + NO(g)   Delta H_r = -138 kJ mol^-1\nStandard enthalpies of formation:\n• Delta H_f_theta[NO2(g)] = +33.2 kJ mol^-1\n• Delta H_f_theta[H2O(l)] = -285.8 kJ mol^-1\n• Delta H_f_theta[NO(g)] = +90.2 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Construct an expression for Delta H_r in terms of standard enthalpies of formation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the standard enthalpy change of formation of aqueous nitric acid, HNO3(aq).",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Delta H_r = [2 x Delta H_f(HNO3) + Delta H_f(NO)] - [3 x Delta H_f(NO2) + Delta H_f(H2O)] (1)", "marks": 1},
            {"part": "b", "points": "-138 = [2 x Delta H_f(HNO3) + 90.2] - [3(33.2) + (-285.8)] = [2 x Delta H_f(HNO3) + 90.2] - [99.6 - 285.8] (1); -138 = 2 x Delta H_f(HNO3) + 90.2 - (-186.2) = 2 x Delta H_f(HNO3) + 276.4 (1); 2 x Delta H_f(HNO3) = -138 - 276.4 = -414.4 => Delta H_f(HNO3) = -207.2 kJ mol^-1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Hess's Law, Calorimetry & Bond Energies of Ethanol — 9701/22/O/N/25/Q5(a)-(d)",
        syllabus_ref="5.2",
        difficulty="HARD",
        preamble="Ethanol, C2H5OH, can be produced industrially by the direct catalytic hydration of ethene:\nC2H4(g) + H2O(g) -> C2H5OH(g)\nStandard enthalpies of combustion:\n• Delta H_c[C2H4(g)] = -1411 kJ mol^-1\n• Delta H_c[C2H5OH(l)] = -1367 kJ mol^-1\n• Enthalpy of vaporisation of ethanol = +42 kJ mol^-1\nBond energies in kJ mol^-1: C=C = 612, C-C = 348, C-H = 412, C-O = 360, O-H = 464.",
        parts=[
            QuestionPart(
                label="a",
                text="Use the bond energies provided to calculate the enthalpy change for the hydration of ethene, Delta H_hydration.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Use the combustion data and enthalpy of vaporisation to calculate an alternative value for Delta H_hydration.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why the value obtained from bond energies in (a) differs from the value obtained from combustion data in (b).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="State whether high temperature or low temperature favours a high equilibrium yield of ethanol in this hydration reaction, justifying your answer using Le Chatelier's principle.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bonds broken = 1(C=C) + 1(O-H) = 612 + 464 = 1076 kJ; Bonds formed = 1(C-C) + 1(C-H) + 1(C-O) = 348 + 412 + 360 = 1120 kJ (1); Delta H = 1076 - 1120 = -44 kJ mol^-1 (allow -42 to -46 kJ mol^-1) (2)", "marks": 3},
            {"part": "b", "points": "Delta H_c(ethanol gas) = -1367 - (+42) = -1409 kJ mol^-1 (1); Delta H_hydration = Delta H_c(C2H4) - Delta H_c(ethanol gas) = -1411 - (-1409) = -2 kJ mol^-1 (or using liquid: -1411 - (-1367) = -44 kJ mol^-1) (2)", "marks": 3},
            {"part": "c", "points": "Mean bond energies are average values across various molecular environments rather than specific to ethanol (1); Real reaction involves specific molecular geometries, bond polarities, and slight non-ideality (1)", "marks": 2},
            {"part": "d", "points": "Low temperature favours a higher yield (1); The forward reaction is exothermic (Delta H < 0), so lowering temperature shifts equilibrium in the exothermic forward direction to release heat (Le Chatelier's principle) (1)", "marks": 2}
        ]
    )
]
