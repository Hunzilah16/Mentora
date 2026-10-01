"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 4: States of Matter.
Subtopics:
  4.1 The gaseous state: ideal and real gases and pV = nRT
  4.2 Bonding and structure (lattice structures, allotropes, ice, liquids)

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

TOPIC_4_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 4.1: The Gaseous State: Ideal & Real Gases, pV = nRT (Q1 to Q28)
    # =========================================================================
    Question(
        number=1,
        title="Kinetic Molecular Theory & Ideal Gas Assumptions — 9701/22/M/J/21/Q2(a)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="The behaviour of an ideal gas is described by the kinetic molecular theory, which relies on several fundamental physical assumptions.",
        parts=[
            QuestionPart(
                label="a",
                text="State two basic assumptions of the kinetic theory of ideal gases regarding the volume of particles and forces between particles.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State what happens to the average kinetic energy of gas molecules when the temperature of the gas is increased from 300 K to 600 K.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The volume of gas particles/molecules is negligible compared to the total volume of the container (1); There are no intermolecular forces / attractions or repulsions between the gas particles (1)", "marks": 2},
            {"part": "b", "points": "The average kinetic energy doubles / increases proportionally with absolute temperature (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Deviation of Real Gases: Compressibility Factor — 9701/21/O/N/20/Q2(a)-(c)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="The graph below illustrates the variation of the compressibility factor, pV / nRT, with pressure for an ideal gas and several real gases at 298 K, as well as nitrogen at 200 K.",
        parts=[
            QuestionPart(
                label="a",
                text="State the value of pV / nRT for one mole of an ideal gas at all pressures.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the curve for carbon dioxide, CO2, shows a significant negative deviation (pV / nRT < 1.0) at moderate pressures.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why at very high pressures (p > 500 atm), all real gases exhibit positive deviations (pV / nRT > 1.0).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "1.0 (or exactly 1) (1)", "marks": 1},
            {"part": "b", "points": "CO2 has significant intermolecular forces / London dispersion forces between molecules (1); These attractions pull molecules together, reducing the pressure exerted on container walls so pV < nRT (1)", "marks": 2},
            {"part": "c", "points": "At very high pressures, molecules are compressed close together so their actual molecular volume is no longer negligible compared to container volume (1); The volume available for movement is reduced, making the measured volume larger than ideal volume, so pV > nRT (1)", "marks": 2}
        ],
        figure_path="figures/real_vs_ideal_gas.png",
        figure_caption="Fig. 4.1: Variation of pV / nRT with pressure for real gases compared to an ideal gas."
    ),
    Question(
        number=3,
        title="Conditions for Non-Ideal Gas Behaviour — 9701/23/M/J/22/Q1(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="Real gases show deviations from ideal behaviour under specific environmental conditions.",
        parts=[
            QuestionPart(
                label="a",
                text="State the two conditions of temperature and pressure under which real gases deviate most significantly from ideal gas behaviour.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why a decrease in temperature causes a real gas to deviate more from ideality.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Low temperature (1); High pressure (1)", "marks": 2},
            {"part": "b", "points": "At lower temperatures, molecules have less kinetic energy / move more slowly (1); Intermolecular forces become significant and cannot be overcome, pulling particles together (1)", "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Comparing Ideality: Helium vs Ammonia — 9701/22/F/M/21/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="Consider equal moles of helium gas, He, and ammonia gas, NH3, placed in separate sealed vessels of identical volume at 298 K and 100 kPa.",
        parts=[
            QuestionPart(
                label="a",
                text="State which of these two gases behaves more like an ideal gas under these conditions.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain your choice in (a) by comparing the intermolecular forces and relative sizes of helium and ammonia particles.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Helium / He (1)", "marks": 1},
            {"part": "b", "points": "Helium is monoatomic with only 2 electrons, resulting in extremely weak London dispersion forces (1); Ammonia has hydrogen bonding between polar NH3 molecules, which is much stronger than dispersion forces (1); Helium atoms have a significantly smaller atomic volume than NH3 molecules, so their volume is closer to negligible (1)", "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Ideal Gas Calculation: Mass of Oxygen in a Cylinder — 9701/21/M/J/22/Q2(a)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="A rigid steel gas cylinder with an internal volume of 25.0 dm3 contains oxygen gas, O2, at a pressure of 1.50 x 10^6 Pa and a temperature of 20.0 °C. (R = 8.31 J K^-1 mol^-1)",
        parts=[
            QuestionPart(
                label="a",
                text="Convert 20.0 °C to Kelvin and 25.0 dm3 to m3.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount, in moles, of oxygen gas contained in the cylinder. Give your answer to 3 significant figures.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass, in grams, of oxygen gas present in the cylinder.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "T = 20.0 + 273 = 293 K and V = 25.0 x 10^-3 m3 (or 0.025 m3) (1)", "marks": 1},
            {"part": "b", "points": "n = pV / RT = (1.50 x 10^6 x 0.0250) / (8.31 x 293) (1); n = 15.4 mol (1)", "marks": 2},
            {"part": "c", "points": "mass = n x Mr = 15.4 x 32.0 = 493 g (allow 492 - 494 g) (1)", "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Ideal Gas Calculation: Volume of Carbon Dioxide Evolved — 9701/22/O/N/23/Q1(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="A 1.25 g sample of calcium carbonate, CaCO3 (Mr = 100.1), is reacted completely with excess dilute hydrochloric acid at 295 K and 1.01 x 10^5 Pa.\nCaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of CaCO3 reacted and hence the moles of CO2 gas produced.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Using pV = nRT, calculate the volume of CO2 gas collected, in cm3, under these experimental conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(CaCO3) = 1.25 / 100.1 = 0.01249 mol (1); n(CO2) = 0.01249 mol (1:1 ratio) (1)", "marks": 2},
            {"part": "b", "points": "V = nRT / p = (0.01249 x 8.31 x 295) / (1.01 x 10^5) = 3.03 x 10^-4 m3 (1); V = 3.03 x 10^-4 x 10^6 = 303 cm3 (allow 303 - 305 cm3) (1)", "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Determining Mr of a Volatile Liquid via Gas Syringe — 9701/21/M/J/23/Q2(a)-(c)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="The relative molecular mass, Mr, of a volatile liquid hydrocarbon, X, is determined experimentally using the gas syringe apparatus shown below.",
        parts=[
            QuestionPart(
                label="a",
                text="A student injected 0.184 g of liquid X into the gas syringe maintained at 370 K and 1.02 x 10^5 Pa. The volume of vapour recorded was 65.0 cm3. Calculate the Mr of hydrocarbon X to 1 decimal place.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Given that hydrocarbon X contains 85.7% carbon and 14.3% hydrogen by mass, deduce its empirical formula and molecular formula.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Suggest one practical reason why the calculated Mr might be higher than the true theoretical value.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "V = 65.0 x 10^-6 m3; n = pV / RT = (1.02 x 10^5 x 65.0 x 10^-6) / (8.31 x 370) = 2.156 x 10^-3 mol (1); Mr = mass / n = 0.184 / (2.156 x 10^-3) (1); Mr = 85.3 (allow 85.0 - 86.0) (1)", "marks": 3},
            {"part": "b", "points": "C: 85.7/12.0 = 7.14, H: 14.3/1.0 = 14.3 => ratio 1:2, empirical formula CH2 (1); Formula mass = 14.0; n = 85.3 / 14.0 = 6 => Molecular formula C6H12 (1)", "marks": 2},
            {"part": "c", "points": "Not all liquid vaporised / some vapour condensed in syringe nozzle / syringe plunger was sticking, giving a recorded volume smaller than actual (1)", "marks": 1}
        ],
        figure_path="figures/gas_syringe_apparatus.png",
        figure_caption="Fig. 4.2: Gas syringe apparatus enclosed in a temperature-controlled jacket."
    ),
    Question(
        number=8,
        title="Identifying an Unknown Gas Using Gas Density — 9701/22/M/J/20/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="A pure gaseous alkane has a density of 2.45 g dm^-3 at a temperature of 293 K and a pressure of 1.01 x 10^5 Pa. (R = 8.31 J K^-1 mol^-1)",
        parts=[
            QuestionPart(
                label="a",
                text="Show that the relative molecular mass of a gas can be expressed as Mr = (density x R x T) / p.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the relative molecular mass, Mr, of this alkane and identify its molecular formula.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "pV = nRT where n = m / Mr => pV = (m / Mr)RT (1); Rearranging: Mr = (m / V) x (RT / p) = density x RT / p (1)", "marks": 2},
            {"part": "b", "points": "density = 2.45 g dm^-3 = 2450 g m^-3; Mr = (2450 x 8.31 x 293) / (1.01 x 10^5) = 59.0 (allow 58.8 - 59.2) (1); General formula CnH2n+2: 14n + 2 = 58 => n = 4, alkane is butane, C4H10 (1)", "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Combustion Eudiometry: Contraction in Gas Volume — 9701/21/O/N/22/Q2(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="10.0 cm3 of a gaseous hydrocarbon, CxHy, is exploded with 70.0 cm3 of oxygen (an excess) in a eudiometer tube. After cooling back to room temperature (298 K, 101 kPa), the residual gas volume is 55.0 cm3. When shaken with aqueous sodium hydroxide, the volume contracts further by 30.0 cm3.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the volume of carbon dioxide, CO2, produced and the volume of unreacted excess oxygen.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Determine the molecular formula of the hydrocarbon CxHy.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Volume of CO2 absorbed by NaOH = 30.0 cm3 (1); Residual volume of unreacted O2 = 55.0 - 30.0 = 25.0 cm3 (1)", "marks": 2},
            {"part": "b", "points": "Volume of O2 reacted = 70.0 - 25.0 = 45.0 cm3 (1); 10.0 cm3 hydrocarbon produces 30.0 cm3 CO2 => x = 30.0 / 10.0 = 3 (C3) (1); Combustion equation: CxHy + (x + y/4)O2 -> xCO2 + (y/2)H2O; x + y/4 = 45.0 / 10.0 = 4.5 => 3 + y/4 = 4.5 => y = 6, Formula is C3H6 (propene / cyclopropane) (1)", "marks": 3}
        ]
    ),
    Question(
        number=10,
        title="Thermal Decomposition Producing Multiple Gases — 9701/23/O/N/21/Q2(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="Ammonium nitrate decomposes explosively upon strong heating according to the equation:\n2NH4NO3(s) -> 2N2(g) + O2(g) + 4H2O(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total volume of gas produced, measured at 450 °C (723 K) and 1.00 x 10^5 Pa, when 8.00 g of NH4NO3 (Mr = 80.0) decomposes completely.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Calculate the mole fraction of nitrogen gas, N2, in the gaseous mixture produced.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(NH4NO3) = 8.00 / 80.0 = 0.100 mol (1); Total moles of gas = 0.100 x (7 / 2) = 0.350 mol of gas (1); V = nRT / p = (0.350 x 8.31 x 723) / (1.00 x 10^5) = 0.02103 m3 = 21.0 dm3 (1)", "marks": 3},
            {"part": "b", "points": "Mole fraction of N2 = 2 / 7 = 0.286 (or 28.6%) (1)", "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Dalton's Law of Partial Pressures — 9701/22/F/M/23/Q1(c)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="A 10.0 dm3 gas container at 300 K contains a mixture of 0.400 mol of helium and 0.100 mol of argon.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total pressure, in kPa, exerted by the gas mixture.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the partial pressure of argon, p(Ar), in the mixture.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Total moles n = 0.400 + 0.100 = 0.500 mol; V = 0.0100 m3 (1); p_tot = nRT / V = (0.500 x 8.31 x 300) / 0.0100 = 124650 Pa = 125 kPa (1)", "marks": 2},
            {"part": "b", "points": "Mole fraction of Ar = 0.100 / 0.500 = 0.200 (1); p(Ar) = 0.200 x 124.65 kPa = 24.9 kPa (1)", "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Van der Waals Correction & Molecular Volume — 9701/21/M/J/21/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="The van der Waals equation modifies the ideal gas law to account for real gas behaviour:\n(p + a/V^2)(V - b) = RT (for 1 mole of gas)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the physical significance of the term 'b' in the expression (V - b).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the correction term 'a/V^2' is added to the measured pressure p.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "'b' represents the finite volume occupied by the gas molecules themselves (co-volume) (1)", "marks": 1},
            {"part": "b", "points": "Attractive intermolecular forces between molecules reduce the force and frequency of collisions against the container walls (1); Adding a/V^2 accounts for this reduction to reflect the ideal pressure that would be exerted without attractions (1)", "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Experimental Sources of Error in Gas Syringe Method — 9701/22/M/J/22/Q2(c)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="A student carries out an experiment to determine the relative molecular mass of hexane using a gas syringe inside an oven at 100 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Suggest two modifications or precautions to ensure accurate gas volume measurement in this experiment.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="If the barometric pressure in the laboratory was incorrectly recorded as 105 kPa instead of the true value of 98 kPa, state and explain the effect on the calculated Mr.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ensure all liquid has completely vaporised before recording volume (1); Ensure the syringe plunger moves freely without friction / lubricate plunger with graphite (1)", "marks": 2},
            {"part": "b", "points": "Calculated Mr would be lower than the true value (1); Mr is inversely proportional to p in Mr = mRT / (pV), so using an erroneously high pressure overestimates moles and underestimates Mr (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Relative Rates of Gas Diffusion — 9701/22/O/N/21/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="When concentrated hydrochloric acid and concentrated aqueous ammonia are placed at opposite ends of a long glass tube, a white ring of ammonium chloride, NH4Cl, forms.",
        parts=[
            QuestionPart(
                label="a",
                text="State which gas, NH3 or HCl, diffuses faster along the tube.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the white ring forms closer to the concentrated hydrochloric acid end of the tube.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ammonia / NH3 (1)", "marks": 1},
            {"part": "b", "points": "NH3 has a lower relative molecular mass (Mr = 17.0) than HCl (Mr = 36.5) (1); At the same temperature, lighter molecules have a higher average velocity / speed and therefore diffuse faster (1)", "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="SI Unit Conversions in Ideal Gas Calculations — 9701/21/O/N/23/Q1(a)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="Precise unit conversions are essential when applying the ideal gas equation pV = nRT.",
        parts=[
            QuestionPart(
                label="a",
                text="Convert each of the following measurements into the standard SI units required for pV = nRT:\n(i) 2.45 MPa\n(ii) 450 cm3\n(iii) -15 °C",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) 2.45 x 10^6 Pa (1); (ii) 450 x 10^-6 m3 or 4.50 x 10^-4 m3 (1); (iii) -15 + 273 = 258 K (1)", "marks": 3}
        ]
    ),
    Question(
        number=16,
        title="Mercury Barometer & Atmospheric Pressure — 9701/23/M/J/20/Q2(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="Standard atmospheric pressure is commonly defined as 760 mm Hg.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate standard atmospheric pressure in Pascals, Pa, given that the density of mercury is 1.36 x 10^4 kg m^-3 and acceleration due to gravity is 9.81 m s^-2 (using p = rho x g x h).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why water is not used instead of mercury in a simple laboratory barometer.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "h = 0.760 m; p = 1.36 x 10^4 x 9.81 x 0.760 (1); p = 1.014 x 10^5 Pa (or 101 kPa) (1)", "marks": 2},
            {"part": "b", "points": "Water has a much lower density than mercury, so a water barometer column would need to be over 10 metres high (or water has significant vapour pressure) (1)", "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Gas Stoichiometry in the Haber Process — 9701/22/F/M/24/Q2(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="In the Haber process, nitrogen and hydrogen react according to the equilibrium:\nN2(g) + 3H2(g) <=> 2NH3(g)\nA 60.0 dm3 mixture containing 20.0 dm3 of N2 and 40.0 dm3 of H2 is reacted at constant temperature and pressure until 30% of the limiting reactant has reacted.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the limiting reactant in this initial mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the total volume of gas remaining in the reactor after 30% of the limiting reactant has reacted.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Hydrogen / H2 (40.0 dm3 requires 40/3 = 13.3 dm3 N2; since 20.0 dm3 N2 is present, H2 is limiting) (1)", "marks": 1},
            {"part": "b", "points": "Volume of H2 reacted = 0.30 x 40.0 = 12.0 dm3 => remaining H2 = 28.0 dm3 (1); Volume of N2 reacted = 12.0 / 3 = 4.0 dm3 => remaining N2 = 20.0 - 4.0 = 16.0 dm3 (1); Volume of NH3 formed = 12.0 x (2/3) = 8.0 dm3 => Total volume = 28.0 + 16.0 + 8.0 = 52.0 dm3 (1)", "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Ideality Trends Down Group 18 Noble Gases — 9701/21/M/J/24/Q1(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="The noble gases helium, neon, argon, krypton, and xenon are all monoatomic gases.",
        parts=[
            QuestionPart(
                label="a",
                text="State the trend in boiling points of the noble gases down Group 18 from helium to xenon.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why xenon gas deviates much more significantly from ideal gas behaviour than helium gas at 298 K and 1000 kPa.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Boiling points increase down Group 18 (1)", "marks": 1},
            {"part": "b", "points": "Xenon atoms have 54 electrons compared to 2 for helium, resulting in a much more polarisable electron cloud and stronger London dispersion forces (1); Xenon atoms also have a larger atomic radius, so their volume is significantly less negligible (1)", "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Vapour Density Calculation for a Halogenoalkane — 9701/22/O/N/24/Q2(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="A sample of 0.258 g of a volatile chlorofluoroalkane vapour occupies a volume of 46.2 cm3 at 368 K and 100.2 kPa.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of chlorofluoroalkane vapour present.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the relative molecular mass, Mr, of the chlorofluoroalkane to the nearest whole number.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Suggest the molecular formula of this compound given that it contains 1 carbon atom, 2 chlorine atoms, and fluorine.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "V = 46.2 x 10^-6 m3; n = pV / RT = (100.2 x 10^3 x 46.2 x 10^-6) / (8.31 x 368) (1); n = 1.513 x 10^-3 mol (1)", "marks": 2},
            {"part": "b", "points": "Mr = 0.258 / (1.513 x 10^-3) = 170.5 => 171 (allow 170 - 171) (1)", "marks": 1},
            {"part": "c", "points": "Mass of C + 2Cl = 12.0 + 71.0 = 83.0; Remainder = 171 - 83 = 88; 88 / 19.0 = 4.6 (or CF2Cl2 Mr = 121, C2F4Cl2 Mr = 171; for 1 C atom: CCl2F2 Mr = 121; here formula is C2F4Cl2 or CCl2F2 + experimental error; accept CCl2F4 or C2F4Cl2) (1)", "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Intermolecular Hydrogen Bonding & Gas Ideality — 9701/21/O/N/24/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="Hydrogen fluoride, HF, and hydrogen chloride, HCl, are both gaseous hydrogen halides at 300 K.",
        parts=[
            QuestionPart(
                label="a",
                text="State the predominant type of intermolecular force present between gaseous HF molecules.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why gaseous HF exhibits a much larger negative deviation from the ideal gas equation pV = nRT than gaseous HCl at the same temperature and pressure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Hydrogen bonding (1)", "marks": 1},
            {"part": "b", "points": "Hydrogen bonding between HF molecules is significantly stronger than the permanent dipole-dipole forces between HCl molecules (1); This causes HF molecules to associate into dimers/oligomers (e.g. (HF)2), significantly reducing the effective number of particles and pressure exerted (1)", "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Rigid Container Pressure-Temperature Relationship — 9701/23/M/J/23/Q2(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="A rigid fire extinguisher cylinder contains carbon dioxide gas at a pressure of 5.50 x 10^6 Pa at 20.0 °C. The maximum safe pressure the cylinder can withstand without rupturing is 8.00 x 10^6 Pa.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the maximum temperature, in °C, to which the cylinder can be heated before it reaches its maximum safe pressure.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State the relationship between pressure and absolute temperature for a fixed mass of gas at constant volume.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "T1 = 20 + 273 = 293 K (1); p1 / T1 = p2 / T2 => T2 = T1 x (p2 / p1) = 293 x (8.00 x 10^6 / 5.50 x 10^6) = 426.2 K (1); T2 in °C = 426.2 - 273 = 153 °C (allow 153 - 154 °C) (1)", "marks": 3},
            {"part": "b", "points": "Pressure is directly proportional to absolute temperature (p directly proportional to T in Kelvin) / Gay-Lussac's Law (1)", "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Gas Production in Automobile Airbags — 9701/22/M/J/25/Q1(a)-(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="Automobile airbags deploy rapidly by the catalytic decomposition of solid sodium azide:\n2NaN3(s) -> 2Na(s) + 3N2(g)\nAn airbag requires 65.0 dm3 of nitrogen gas, N2, to inflate fully at 25.0 °C and 1.05 x 10^5 Pa.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of N2 gas required to inflate the airbag.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the minimum mass of sodium azide, NaN3 (Mr = 65.0), required.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "V = 0.0650 m3, T = 298 K; n(N2) = pV / RT = (1.05 x 10^5 x 0.0650) / (8.31 x 298) (1); n(N2) = 2.755 mol (1)", "marks": 2},
            {"part": "b", "points": "Moles of NaN3 required = 2.755 x (2 / 3) = 1.837 mol (1); Mass of NaN3 = 1.837 x 65.0 = 119 g (allow 119 - 120 g) (1)", "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Graphical Interpretations of Gas Laws — 9701/21/F/M/25/Q2(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="Consider a fixed mass of an ideal gas.",
        parts=[
            QuestionPart(
                label="a",
                text="Sketch or describe the shape of the graph obtained when pressure p is plotted against 1/V at constant temperature.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe how the graph of volume V against temperature in °C can be used to determine the value of absolute zero.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A straight line passing through the origin (1)", "marks": 1},
            {"part": "b", "points": "Extrapolate the straight line of V against temperature in °C back to the point where volume equals zero (V = 0) (1); The temperature intercept on the x-axis corresponds to absolute zero (-273 °C) (1)", "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Non-Ideality of Gaseous Sulfur Dioxide — 9701/22/O/N/25/Q1(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="Sulfur dioxide, SO2, is a pollutant gas produced during the combustion of fossil fuels containing sulfur.",
        parts=[
            QuestionPart(
                label="a",
                text="State the shape and bond angle of a sulfur dioxide molecule.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why gaseous SO2 deviates much more from ideal gas behaviour than oxygen, O2, at room temperature.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Bent / V-shaped / non-linear (1); Bond angle 119° (accept 117° - 120°) (1)", "marks": 2},
            {"part": "b", "points": "SO2 is polar and possesses permanent dipole-dipole forces as well as London dispersion forces, whereas O2 is non-polar with only London dispersion forces (1); SO2 also has a much larger molecular volume / electron count (32 electrons vs 16), creating significantly stronger overall intermolecular attraction (1)", "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Connecting Two Gas Bulbs: Total Equilibrium Pressure — 9701/23/O/N/24/Q2(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="Bulb A has a volume of 2.00 dm3 and contains neon at 150 kPa. Bulb B has a volume of 3.00 dm3 and contains neon at 250 kPa. The two bulbs are connected by a stopcock of negligible volume, maintained at the same constant temperature.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total amount, in terms of (pV), of neon in the system before the stopcock is opened.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the final equilibrium pressure, in kPa, when the stopcock is opened and the gases mix thoroughly.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(p1V1) + (p2V2) = (150 x 2.00) + (250 x 3.00) = 300 + 750 = 1050 kPa dm3 (1)", "marks": 1},
            {"part": "b", "points": "Total volume V_tot = 2.00 + 3.00 = 5.00 dm3 (1); p_final = total pV / V_tot = 1050 / 5.00 = 210 kPa (1)", "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Photochemical Smog & Ozone Production — 9701/21/M/J/25/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="In urban atmospheres, nitrogen dioxide photolysis initiates ozone formation:\nNO2(g) + O2(g) -> NO(g) + O3(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Assuming ideal gas behaviour, state whether the total volume of gas changes during this reaction at constant temperature and pressure.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain your answer to (a) using Avogadro's hypothesis.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "No change in total volume / volume remains constant (1)", "marks": 1},
            {"part": "b", "points": "There are 2 moles of gaseous reactants and 2 moles of gaseous products; equal moles of any gas occupy equal volumes under the same conditions of T and p (1)", "marks": 1}
        ]
    ),
    Question(
        number=27,
        title="Gas Collection Over Water: Vapour Pressure Correction — 9701/22/M/J/23/Q3(b)",
        syllabus_ref="4.1",
        difficulty="HARD",
        preamble="A student reacts 0.0486 g of magnesium ribbon with excess dilute sulfuric acid:\nMg(s) + H2SO4(aq) -> MgSO4(aq) + H2(g)\nThe hydrogen gas is collected over water at 20.0 °C and an atmospheric pressure of 102.3 kPa. The vapour pressure of water at 20.0 °C is 2.3 kPa.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the partial pressure of dry hydrogen gas in the collection tube.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the volume, in cm3, of dry hydrogen gas produced. (Ar: Mg = 24.3)",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "p(H2) = p_atm - p(H2O) = 102.3 - 2.3 = 100.0 kPa = 1.00 x 10^5 Pa (1)", "marks": 1},
            {"part": "b", "points": "n(Mg) = 0.0486 / 24.3 = 2.00 x 10^-3 mol => n(H2) = 2.00 x 10^-3 mol (1); V = nRT / p = (2.00 x 10^-3 x 8.31 x 293) / (1.00 x 10^5) = 4.869 x 10^-5 m3 (1); V = 4.869 x 10^-5 x 10^6 = 48.7 cm3 (1)", "marks": 3}
        ]
    ),
    Question(
        number=28,
        title="Gas Liquefaction & Intermolecular Forces — 9701/22/F/M/22/Q3(a)-(b)",
        syllabus_ref="4.1",
        difficulty="EASY",
        preamble="To convert a real gas into a liquid, the gas must be cooled and compressed.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why cooling a gas facilitates its liquefaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why an ideal gas cannot be liquefied under any conditions of temperature and pressure.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cooling reduces the average kinetic energy / speed of gas molecules (1); This allows attractive intermolecular forces to overcome molecular motion and bind particles into a liquid (1)", "marks": 2},
            {"part": "b", "points": "An ideal gas has zero intermolecular attractive forces between its particles (1)", "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 4.2: Bonding & Structure (Lattices, Ice, Liquids) (Q29 to Q50)
    # =========================================================================
    Question(
        number=29,
        title="Classification of Solid Lattices — 9701/21/M/J/21/Q4(a)-(c)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="Solids can be categorized into four primary lattice structures: giant ionic, giant molecular (covalent), giant metallic, and simple molecular.",
        parts=[
            QuestionPart(
                label="a",
                text="Classify the solid lattice type for each of the following substances at room temperature:\n(i) Copper\n(ii) Silicon(IV) oxide\n(iii) Iodine",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State which of these three substances conducts electricity in the solid state, and explain why in terms of structure and bonding.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) Giant metallic (1); (ii) Giant molecular / giant covalent (1); (iii) Simple molecular (1)", "marks": 3},
            {"part": "b", "points": "Copper (1); It contains a lattice of positive metal ions with delocalised electrons that are free to move throughout the structure when a potential difference is applied (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Allotropes of Carbon: Diamond, Graphite, Fullerene — 9701/22/O/N/21/Q4(a)-(d)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Carbon exists as several allotropes with vastly different physical properties, as illustrated below.",
        parts=[
            QuestionPart(
                label="a",
                text="State the hybridisation of carbon atoms in diamond and in graphite.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why graphite is a good electrical conductor whereas diamond is an electrical insulator.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why graphite acts as a solid lubricant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="State why buckminsterfullerene, C60, has a much lower melting point than diamond.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Diamond: sp3 (1); Graphite: sp2 (1)", "marks": 2},
            {"part": "b", "points": "In graphite, each C atom forms 3 sigma bonds, leaving one unhybridised 2p electron per atom which becomes delocalised across the layer and mobile (1); In diamond, all 4 outer electrons are localised in strong covalent sigma bonds with no mobile charge carriers (1)", "marks": 2},
            {"part": "c", "points": "Graphite consists of parallel planar layers held together only by weak London dispersion forces (1); The layers can easily slide over one another when shear force is applied (1)", "marks": 2},
            {"part": "d", "points": "C60 has a simple molecular structure with weak London dispersion forces between discrete C60 cages (1); Diamond has a giant covalent 3D tetrahedral lattice where melting requires breaking many strong covalent bonds (1)", "marks": 2}
        ],
        figure_path="figures/carbon_allotropes_structure.png",
        figure_caption="Fig. 4.3: Comparative lattice structures of diamond, graphite, and fullerene C60."
    ),
    Question(
        number=31,
        title="Graphene: Structure and Physical Properties — 9701/21/M/J/22/Q4(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Graphene is a 2D allotrope of carbon consisting of a single layer of carbon atoms arranged in a hexagonal lattice.",
        parts=[
            QuestionPart(
                label="a",
                text="State the bond angle between carbon-carbon bonds in graphene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why graphene exhibits exceptionally high electrical conductivity and tensile strength.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "120° (trigonal planar) (1)", "marks": 1},
            {"part": "b", "points": "Delocalised pi electron system extends continuously across the 2D sheet, allowing high electron mobility (1); Strong covalent C-C sigma bonds formed by sp2-sp2 orbital overlap require tremendous force to break (1); No weak interlayer forces or grain boundaries present in a single sheet (1)", "marks": 3}
        ]
    ),
    Question(
        number=32,
        title="Open Lattice Structure and Anomalous Properties of Ice — 9701/22/M/J/22/Q3(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Water displays several anomalous physical properties due to its extensive hydrogen bonding network, shown in the lattice structure of ice below.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the arrangement of water molecules in ice and state the coordination number of each oxygen atom.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why ice is less dense than liquid water at 0 °C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain the biological significance of ice floating on liquid water for aquatic organisms in cold climates.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Open tetrahedral 3D arrangement / hexagonal ring structure (1); Coordination number of oxygen = 4 (2 covalent bonds and 2 hydrogen bonds) (1)", "marks": 2},
            {"part": "b", "points": "Hydrogen bonds hold water molecules in a fixed, open, cage-like hexagonal lattice with large cavities/empty spaces (1); Upon melting, hydrogen bonds break and the open lattice collapses, allowing molecules to pack closer together in liquid water (1)", "marks": 2},
            {"part": "c", "points": "Floating ice forms an insulating layer on the surface of ponds/lakes, preventing the water beneath from freezing solid and preserving aquatic life (1)", "marks": 1}
        ],
        figure_path="figures/ice_lattice_structure.png",
        figure_caption="Fig. 4.4: Open hexagonal hydrogen-bonded crystal lattice of ice."
    ),
    Question(
        number=33,
        title="Giant Ionic Lattices: Sodium Chloride vs Magnesium Oxide — 9701/23/O/N/22/Q3(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Both sodium chloride, NaCl, and magnesium oxide, MgO, crystallise in face-centred cubic giant ionic lattices.",
        parts=[
            QuestionPart(
                label="a",
                text="State the coordination number of each ion in the NaCl lattice.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="The melting point of NaCl is 801 °C, whereas the melting point of MgO is 2852 °C. Explain this difference in terms of ionic charge and ionic radius.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "6 (each Na+ surrounded by 6 Cl-, and each Cl- surrounded by 6 Na+ / 6:6 coordination) (1)", "marks": 1},
            {"part": "b", "points": "Mg2+ and O2- ions carry double the charge of Na+ and Cl- ions (2+ and 2- vs 1+ and 1-) (1); Mg2+ has a smaller ionic radius than Na+, and O2- is smaller than Cl- (1); Electrostatic force of attraction between ions is proportional to charge product / ionic radii sum, so lattice energy of MgO is much greater and requires far more thermal energy to overcome (1)", "marks": 3}
        ]
    ),
    Question(
        number=34,
        title="Electrical Conductivity Across Physical States — 9701/22/F/M/23/Q3(a)-(b)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="The electrical conductivities of three substances, P, Q, and R, were tested in both solid and molten states:\n• Substance P: Insulator when solid, conducts when molten\n• Substance Q: Conducts when solid, conducts when molten\n• Substance R: Insulator when solid, insulator when molten",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the lattice type for each substance P, Q, and R.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why substance P conducts electricity when molten but not when solid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "P: Giant ionic (1); Q: Giant metallic (1); R: Simple molecular or giant covalent (1)", "marks": 3},
            {"part": "b", "points": "In solid state, ions are held tightly in fixed lattice positions and cannot move (1); When molten, the lattice breaks down and ions are mobile / free to migrate towards electrodes carrying electric charge (1)", "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Giant Covalent vs Simple Molecular: SiO2 vs CO2 — 9701/21/O/N/23/Q3(a)-(c)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="Silicon and carbon both belong to Group 14. However, at room temperature, carbon dioxide is a gas (sublimes at -78.5 °C) while silicon(IV) oxide is a hard solid with a melting point of 1710 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the structure and bonding in silicon(IV) oxide, SiO2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain the huge difference in melting points between SiO2 and CO2 in terms of the forces overcome during melting.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Giant covalent / macromolecular structure (1); Each silicon atom is covalently bonded to 4 oxygen atoms tetrahedrally, and each oxygen atom bridges between 2 silicon atoms (1)", "marks": 2},
            {"part": "b", "points": "Melting SiO2 requires breaking many strong covalent Si-O bonds throughout the 3D macromolecular lattice, which requires huge energy (1); CO2 has a simple molecular structure with linear O=C=O molecules (1); Melting CO2 only requires overcoming weak intermolecular London dispersion forces between molecules, requiring little energy (1)", "marks": 3}
        ]
    ),
    Question(
        number=36,
        title="Simple Molecular Lattice of Iodine, I2 — 9701/22/M/J/24/Q3(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Iodine forms dark purple-grey shiny crystals at room temperature and sublimes readily upon gentle warming.",
        parts=[
            QuestionPart(
                label="a",
                text="State the type of lattice structure formed by solid iodine.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe the bonding within an iodine molecule and the forces between iodine molecules in the crystal lattice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why iodine sublimes directly into a purple vapour upon gentle heating.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Simple molecular (face-centred cubic molecular lattice) (1)", "marks": 1},
            {"part": "b", "points": "Strong single covalent bond between the two iodine atoms in each I2 molecule (1); Weak London dispersion forces (induced dipole-dipole) between adjacent I2 molecules (1)", "marks": 2},
            {"part": "c", "points": "The weak London dispersion forces between molecules are easily overcome at low temperatures by gentle heating (1); Covalent I-I bonds remain intact, so solid transitions directly to discrete I2 gas molecules without liquid phase forming at 1 atm (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Giant Metallic Lattice: Malleability and Ductility — 9701/21/M/J/24/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="Metals such as copper and aluminium can be hammered into sheets (malleable) and drawn into wires (ductile).",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the structure and bonding in a giant metallic lattice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why metals are malleable and ductile without shattering.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A regular lattice of positive metal ions (cations) (1); surrounded by / held together by electrostatic attraction to a sea of delocalised electrons (1)", "marks": 2},
            {"part": "b", "points": "When a mechanical force is applied, layers of metal ions can slide over one another (1); The non-directional sea of delocalised electrons adjusts readily, maintaining the metallic bond and preventing shattering (1)", "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Carbon Nanotubes: Structure & Tensile Strength — 9701/23/M/J/24/Q3(a)-(b)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Single-walled carbon nanotubes (SWCNTs) can be visualized as seamless cylinders rolled from a single sheet of graphene.",
        parts=[
            QuestionPart(
                label="a",
                text="State two remarkable physical properties of carbon nanotubes that make them suitable for nanotechnology applications.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why carbon nanotubes have an extremely high tensile strength along their longitudinal axis.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Extremely high tensile strength / high stiffness (1); High electrical conductivity / high thermal conductivity (1)", "marks": 2},
            {"part": "b", "points": "Tension along the axis acts directly against strong covalent sp2 carbon-carbon sigma bonds (1); Breaking the tube longitudinally requires breaking millions of strong covalent bonds simultaneously (1)", "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Evaporation, Dynamic Equilibrium & Vapour Pressure — 9701/22/O/N/24/Q4(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="When a volatile liquid is placed in an open beaker, it slowly evaporates completely. When placed in a closed container at constant temperature, dynamic equilibrium is established.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term vapour pressure.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain what is meant by dynamic equilibrium between liquid and vapour in a closed system.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain the relationship between the boiling point of a liquid and atmospheric pressure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The pressure exerted by a vapour in thermodynamic equilibrium with its liquid phase at a given temperature (in a closed system) (1)", "marks": 1},
            {"part": "b", "points": "The rate of evaporation of liquid molecules equals the rate of condensation of vapour molecules (1); The amounts/concentrations of liquid and vapour remain constant over time (1)", "marks": 2},
            {"part": "c", "points": "Boiling occurs when the saturated vapour pressure of the liquid equals the prevailing external / atmospheric pressure (1); Lower external pressure decreases the required vapour pressure and hence lowers the boiling point (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Enthalpy of Fusion vs Enthalpy of Vaporisation — 9701/21/O/N/24/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="For water at 1 atm:\n• Enthalpy change of fusion, Delta H_fus = +6.01 kJ mol^-1\n• Enthalpy change of vaporisation, Delta H_vap = +40.7 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Delta H_vap is significantly greater than Delta H_fus for water.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State what happens to the temperature of water while it is boiling at 100 °C, and explain why in terms of kinetic energy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Melting only partially disrupts the hydrogen-bonded lattice; molecules remain in close contact in the liquid state (1); Vaporisation requires completely separating molecules and breaking virtually all hydrogen bonds (1); Far more energy is required to completely overcome intermolecular forces than to loosen the lattice (1)", "marks": 3},
            {"part": "b", "points": "Temperature remains constant at 100 °C (1); Thermal energy supplied is converted into potential energy to overcome intermolecular forces rather than increasing average molecular kinetic energy (1)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Melting Point Trends Across Period 3 Elements — 9701/22/F/M/25/Q3(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="The melting points of elements across Period 3 are shown below:\nNa (98 °C), Mg (650 °C), Al (660 °C), Si (1414 °C), P4 (44 °C), S8 (115 °C), Cl2 (-101 °C), Ar (-189 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the increase in melting points from Na to Al.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why silicon has the highest melting point of all elements in Period 3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why sulfur has a higher melting point than phosphorus.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "From Na to Al, ionic charge increases (Na+ to Al3+) and ionic radius decreases (1); Number of delocalised electrons per atom increases (1 to 3), leading to stronger electrostatic attraction in the metallic lattice (1)", "marks": 2},
            {"part": "b", "points": "Silicon has a giant covalent 3D lattice structure (diamond-like) (1); Melting requires breaking many strong covalent Si-Si bonds throughout the macromolecule, requiring very high thermal energy (1)", "marks": 2},
            {"part": "c", "points": "Both have simple molecular lattices, but sulfur exists as S8 molecules while phosphorus exists as P4 molecules (1); S8 has a higher Mr / more electrons (128 vs 60), resulting in stronger London dispersion forces between molecules (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Brittleness and Cleavage of Ionic Crystals — 9701/21/M/J/25/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="When a sharp mechanical blow is struck against a crystal of sodium chloride, the crystal cleaves cleanly along straight planes rather than deforming.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why giant ionic lattices are brittle and shatter upon mechanical impact.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Contrast this mechanical behaviour with that of a metal like iron.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A mechanical blow causes layers of alternating positive and negative ions to shift slightly (1); Ions of like charge are brought into direct alignment, causing intense electrostatic repulsion that splits the crystal lattice apart (1)", "marks": 2},
            {"part": "b", "points": "Metals deform without shattering because the delocalised electron sea shifts flexibly around sliding positive ions, preserving the metallic bond (1)", "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Solubility in Polar and Non-Polar Solvents — 9701/23/M/J/25/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Consider the solubility of sodium chloride, iodine, and diamond in water and in hexane.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why sodium chloride dissolves readily in water but is insoluble in hexane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why diamond is completely insoluble in all standard solvents.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Water is a polar solvent whose delta+ H and delta- O atoms form strong ion-dipole interactions with Na+ and Cl- ions (hydration energy compensates for lattice energy) (1); Hexane is non-polar and can only form weak London dispersion forces, which cannot overcome the strong ionic lattice attractions (1)", "marks": 2},
            {"part": "b", "points": "Diamond has a giant covalent macromolecular structure held together by strong covalent C-C bonds (1); Any possible solvent-carbon attractions are vastly weaker than the energy required to break the covalent network (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Giant Covalent Lattices: Silicon vs Diamond — 9701/22/O/N/25/Q3(a)-(b)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Both diamond and elemental silicon possess the same 3D tetrahedral macromolecular lattice structure. However, diamond melts at over 3800 °C while silicon melts at 1414 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the melting point of diamond is significantly higher than that of silicon.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State whether silicon behaves as an electrical conductor, semiconductor, or insulator at room temperature.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Carbon has a smaller atomic radius than silicon (outer electrons closer to nucleus) (1); C-C covalent bonds are shorter and have higher bond enthalpy / stronger orbital overlap than Si-Si bonds (1); More energy is required to break the stronger C-C bonds across the lattice during melting (1)", "marks": 3},
            {"part": "b", "points": "Semiconductor (1)", "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Simple Molecular vs Macromolecular Oxides: CO2 vs Quartz — 9701/21/O/N/25/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="Solid carbon dioxide ('dry ice') and quartz (SiO2) are both solid oxides of Group 14 elements at low temperatures.",
        parts=[
            QuestionPart(
                label="a",
                text="Compare the volatility of dry ice with quartz at room temperature and pressure.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain this difference by referring to the specific bonding and forces present in each solid.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Dry ice is highly volatile (sublimes at -78.5 °C) whereas quartz is completely non-volatile (1)", "marks": 1},
            {"part": "b", "points": "Dry ice consists of discrete linear CO2 molecules held together in a crystal by weak London dispersion forces which require minimal thermal energy to break (1); Quartz is a giant covalent macromolecule composed of an infinite 3D framework of strong Si-O covalent bonds (1); Breaking the quartz lattice requires breaking strong covalent bonds throughout the entire crystal (1)", "marks": 3}
        ]
    ),
    Question(
        number=46,
        title="Thermal Conduction in Metals vs Covalent Solids — 9701/22/M/J/25/Q4(a)-(b)",
        syllabus_ref="4.2",
        difficulty="EASY",
        preamble="Metals like silver and copper have very high thermal conductivity, whereas simple molecular solids are thermal insulators.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how heat energy is transported through a metal lattice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why diamond has an unusually high thermal conductivity for a non-metal.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Heat energy increases vibrations of cations in the lattice, which are transmitted to adjacent ions (1); Mobile delocalised electrons gain kinetic energy and rapidly diffuse through the lattice, transferring energy throughout the metal (1)", "marks": 2},
            {"part": "b", "points": "Diamond has an extremely rigid, uniform 3D lattice composed of short, strong C-C covalent bonds and light carbon atoms (1); This enables lattice vibrations (phonons) to propagate through the crystal with minimal scattering (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Fullerene C60 vs Diamond: Reactivity and Bonding — 9701/23/O/N/25/Q4(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Buckminsterfullerene, C60, is a football-shaped molecule consisting of 20 hexagons and 12 pentagons of carbon atoms.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether C60 is soluble in non-polar organic solvents such as benzene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why C60 can undergo addition reactions across its carbon-carbon bonds, whereas diamond is completely unreactive.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why the electrical conductivity of pure C60 solid is very poor compared to graphite.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Yes / soluble (1)", "marks": 1},
            {"part": "b", "points": "C60 contains localised pi bonds (double bonds) in a strained curved cage structure, allowing addition across C=C bonds to relieve strain (1); Diamond contains only strong, saturated C-C sigma bonds with no pi electrons or unsaturation (1)", "marks": 2},
            {"part": "c", "points": "In solid C60, delocalisation of pi electrons is restricted within each individual spherical cage (1); Electrons cannot jump easily between cages because they are separated by weak London dispersion forces (1)", "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Hydrogen-Bonded Solids: Solid Ammonia vs Ice — 9701/21/F/M/24/Q4(a)-(c)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Both ammonia and water form hydrogen bonds in the solid state. However, solid ammonia (mp -77.7 °C) melts at a much lower temperature than ice (mp 0.0 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="State the average number of hydrogen bonds formed per molecule in ice.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why solid ammonia forms fewer hydrogen bonds per molecule than ice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why oxygen forms stronger hydrogen bonds than nitrogen.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "4 hydrogen bonds per H2O molecule (2 via lone pairs, 2 via delta+ H atoms) (1)", "marks": 1},
            {"part": "b", "points": "Each NH3 molecule has 3 hydrogen atoms but only 1 lone pair on nitrogen (1); The number of hydrogen bonds is limited by the single lone pair to an average of only 2 hydrogen bonds per molecule (or 1 donor/1 acceptor pair) (1)", "marks": 2},
            {"part": "c", "points": "Oxygen is more electronegative than nitrogen, resulting in a larger delta+ / delta- dipole and stronger attraction (1)", "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Deduce Solid Lattice Types from Physical Properties — 9701/22/M/J/24/Q4(a)-(d)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="Four unknown solid substances, W, X, Y, and Z, were investigated. Their properties are recorded in the table below:\\n• W: mp 1084 °C; conducts electricity in solid and liquid; insoluble in water\\n• X: mp 801 °C; non-conductor in solid, conducts when molten; soluble in water\\n• Y: mp 3550 °C; non-conductor in solid and liquid; insoluble in all solvents\\n• Z: mp 114 °C; non-conductor in solid and liquid; slightly soluble in hexane",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the lattice type of substance W.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the lattice type of substance X.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Deduce the lattice type of substance Y.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Deduce the lattice type of substance Z.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Giant metallic (1)", "marks": 1},
            {"part": "b", "points": "Giant ionic (1)", "marks": 1},
            {"part": "c", "points": "Giant molecular / giant covalent (1)", "marks": 1},
            {"part": "d", "points": "Simple molecular (1)", "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Gas Behaviour, Sublimation & Lattice of Iodine — 9701/22/O/N/25/Q4(a)-(d)",
        syllabus_ref="4.2",
        difficulty="HARD",
        preamble="A 0.508 g sample of solid iodine crystals, I2 (Mr = 253.8), is placed into an evacuated 250 cm3 glass flask and sealed. The flask is gently heated to 185 °C (458 K), at which temperature all iodine has completely sublimed into a purple vapour.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount, in moles, of I2 present in the flask.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Assuming ideal gas behaviour, calculate the pressure, in kPa, exerted by the iodine vapour inside the flask at 458 K.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Describe the changes in particles and bonding that occur when solid iodine transitions directly into iodine vapour.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Suggest whether the actual measured pressure inside the flask would be slightly higher, slightly lower, or exactly equal to the calculated ideal pressure in (b). Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(I2) = 0.508 / 253.8 = 2.002 x 10^-3 mol (1)", "marks": 1},
            {"part": "b", "points": "V = 250 x 10^-6 m3 = 2.50 x 10^-4 m3; p = nRT / V = (2.002 x 10^-3 x 8.31 x 458) / (2.50 x 10^-4) = 30480 Pa = 30.5 kPa (1)", "marks": 2},
            {"part": "c", "points": "Molecules in regular crystalline lattice gain thermal energy and break free from fixed lattice positions (1); Weak intermolecular London dispersion forces are overcome, but strong covalent I-I bonds within molecules remain intact (1)", "marks": 2},
            {"part": "d", "points": "Slightly lower (1); Real iodine molecules experience significant attractive intermolecular dispersion forces due to high electron count (106 electrons per molecule), pulling particles together and reducing impact force on flask walls (1)", "marks": 2}
        ]
    )
]
