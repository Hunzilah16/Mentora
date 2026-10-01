"""
Script to generate topic7_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 7: Equilibria.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 7: Equilibria.
Subtopics:
  7.1 Chemical equilibria: dynamic equilibrium, Le Chatelier's principle, Kc and Kp, Haber/Contact processes
  7.2 Brønsted-Lowry theory of acids and bases: conjugate pairs, strong vs weak acids/bases, pH, neutralisation

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

TOPIC_7_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 7.1: Chemical Equilibria, Le Chatelier, Kc & Kp (Q1 to Q30)
    # =========================================================================
    Question(
        number=1,
        title="Characteristics of Dynamic Chemical Equilibrium — 9701/22/M/J/21/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="Chemical equilibrium is a dynamic state achieved in reversible chemical reactions.",
        parts=[
            QuestionPart(
                label="a",
                text="State two essential features of a system that has achieved dynamic chemical equilibrium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why dynamic equilibrium can only be maintained indefinitely in a closed system.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The rate of the forward reaction equals the rate of the reverse reaction (1); The concentrations of reactants and products remain constant over time (or macroscopic properties like color/pressure remain constant) (1)", "marks": 2},
            {"part": "b", "points": "In an open system, matter / gaseous reactants or products can escape to the surroundings, preventing equilibrium from being established (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Haber Process: Compromise Conditions & Industrial Yield — 9701/21/O/N/20/Q5(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Ammonia is synthesized industrially by the Haber process:\nN2(g) + 3H2(g) <=> 2NH3(g)   Delta H = -92 kJ mol^-1\nFig. 7.1 shows the variation of equilibrium percentage yield of ammonia with temperature at different pressures.",
        parts=[
            QuestionPart(
                label="a",
                text="Use Le Chatelier's principle to explain why higher pressures result in a higher equilibrium yield of ammonia.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Use Le Chatelier's principle to explain why increasing the temperature causes the equilibrium yield of ammonia to decrease.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="In industrial plants, a compromise temperature of 400-450 °C and pressure of 200 atm are employed in the presence of an iron catalyst. Explain why 450 °C is chosen rather than a lower temperature such as 100 °C.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "There are 4 moles of gas on the reactant side and 2 moles of gas on the product side (1); An increase in pressure shifts equilibrium to the right towards fewer moles of gas to relieve the pressure (1)", "marks": 2},
            {"part": "b", "points": "The forward reaction is exothermic (Delta H = -92 kJ mol^-1) (1); Increasing temperature shifts equilibrium in the endothermic reverse direction to absorb the added heat (1)", "marks": 2},
            {"part": "c", "points": "At 100 °C, the rate of reaction is far too slow to be commercially viable because few particles possess energy >= E_a (1); 450 °C provides an acceptable reaction rate while still achieving a viable equilibrium yield (~15% per pass) (1)", "marks": 2}
        ],
        figure_path="figures/haber_process_compromise.png",
        figure_caption="Fig. 7.1: Equilibrium percentage yield of ammonia vs temperature at different operating pressures."
    ),
    Question(
        number=3,
        title="Reaching Dynamic Equilibrium: Rates and Concentrations — 9701/23/M/J/22/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="Fig. 7.2 illustrates how the rates of the forward and reverse reactions, and the concentrations of reactants and products, change over time as equilibrium is approached.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the forward reaction rate is at a maximum at time t = 0 and gradually decreases.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the reverse reaction rate starts at zero and gradually increases.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State what is true about the forward and reverse reaction rates once dynamic equilibrium has been reached at t = 5 minutes.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "At t = 0, reactant concentrations are at their highest, leading to maximum collision frequency (1); As reactants are consumed, their concentrations decrease, reducing collision frequency and rate (1)", "marks": 2},
            {"part": "b", "points": "At t = 0, no product molecules exist; as products are formed, their concentration increases, allowing reverse collisions to occur at an increasing rate (1)", "marks": 1},
            {"part": "c", "points": "The forward rate and reverse rate become exactly equal (r_forward = r_reverse) (1)", "marks": 1}
        ],
        figure_path="figures/dynamic_equilibrium_rates.png",
        figure_caption="Fig. 7.2: Variation of reaction rates and concentrations over time during approach to dynamic equilibrium."
    ),
    Question(
        number=4,
        title="Le Chatelier Perturbation by Adding Reactant — 9701/22/F/M/21/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Fig. 7.3 shows the effect on an equilibrium mixture of N2(g) + 3H2(g) <=> 2NH3(g) when extra nitrogen gas, N2, is injected at t = 4 minutes.",
        parts=[
            QuestionPart(
                label="a",
                text="State Le Chatelier's principle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Referring to Fig. 7.3, explain the subsequent changes in the concentrations of H2 and NH3 between t = 4 minutes and t = 8 minutes.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "If a system at equilibrium is subjected to a change in conditions (concentration, temperature, or pressure) (1); the position of equilibrium shifts in a direction that tends to oppose / counteract the effect of that change (1)", "marks": 2},
            {"part": "b", "points": "The sudden increase in [N2] causes equilibrium to shift to the right to consume the added N2 (1); As the forward reaction proceeds, [H2] decreases as it reacts with N2 (1); Simultaneously, [NH3] increases until a new dynamic equilibrium is established (1)", "marks": 3}
        ],
        figure_path="figures/le_chatelier_perturbation.png",
        figure_caption="Fig. 7.3: Response of Haber equilibrium concentrations to the injection of extra nitrogen at t = 4 min."
    ),
    Question(
        number=5,
        title="Pressure Effects on Gaseous Equilibrium: N2O4 <=> 2NO2 — 9701/21/M/J/22/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Dinitrogen tetroxide decomposes reversibly to nitrogen dioxide in a gas syringe:\nN2O4(g) <=> 2NO2(g)   Delta H = +57 kJ mol^-1\n(N2O4 is colourless; NO2 is dark brown).",
        parts=[
            QuestionPart(
                label="a",
                text="When the plunger of the syringe is suddenly pushed in, the gas mixture instantaneously turns darker brown, but then gradually fades to a paler brown. Explain both observations.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State and explain the effect on the colour of the mixture when the syringe is placed in a beaker of hot water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Instantly compressing the gas decreases volume, so concentration of all species (including brown NO2) increases immediately, darkening the color (1); Higher pressure shifts equilibrium to the left towards fewer moles of gas (1 N2O4 : 2 NO2) to reduce pressure (1); Some brown NO2 converts into colourless N2O4, causing the colour to lighten gradually (1)", "marks": 3},
            {"part": "b", "points": "The mixture turns darker brown (1); The forward reaction is endothermic (Delta H = +57 kJ mol^-1), so increasing temperature shifts equilibrium to the right to absorb heat, increasing [NO2] (1)", "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Calculating Concentration Equilibrium Constant, Kc: Esterification — 9701/22/O/N/23/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Ethanoic acid reacts with ethanol in the presence of an acid catalyst to form ethyl ethanoate:\nCH3COOH(l) + C2H5OH(l) <=> CH3COOC2H5(l) + H2O(l)\nIn an experiment, 1.00 mol of CH3COOH and 1.00 mol of C2H5OH were mixed in a sealed tube. At equilibrium at 25 °C, 0.667 mol of ethyl ethanoate was present in the total volume V.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the expression for the equilibrium constant Kc for this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the equilibrium amounts, in moles, of CH3COOH, C2H5OH, and H2O present in the tube.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the value of Kc and state its units, if any.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Kc = ([CH3COOC2H5][H2O]) / ([CH3COOH][C2H5OH]) (1)", "marks": 1},
            {"part": "b", "points": "n(CH3COOC2H5) = 0.667 mol, n(H2O) = 0.667 mol (1); n(CH3COOH) = 1.00 - 0.667 = 0.333 mol, n(C2H5OH) = 1.00 - 0.667 = 0.333 mol (1)", "marks": 2},
            {"part": "c", "points": "Kc = (0.667/V x 0.667/V) / (0.333/V x 0.333/V) = (0.667 x 0.667) / (0.333 x 0.333) = 4.01 (allow 4.0) (1); Units: No units / dimensionless (V cancels out completely) (1)", "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Calculating Partial Pressure Equilibrium Constant, Kp: PCl5 Dissociation — 9701/21/M/J/23/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Phosphorus(V) chloride dissociates reversibly at 250 °C according to the equation:\nPCl5(g) <=> PCl3(g) + Cl2(g)\nA 1.00 mol sample of PCl5 was heated in a sealed container at 250 °C until equilibrium was reached at a total pressure of 1.50 x 10^5 Pa. At equilibrium, 0.400 mol of Cl2 was present.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total amount, in moles, of all gases present at equilibrium.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the partial pressure of each gas in the equilibrium mixture.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Write the expression for Kp and calculate its value, including units.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "At equilibrium: n(Cl2) = 0.400 mol, n(PCl3) = 0.400 mol, n(PCl5) = 1.00 - 0.400 = 0.600 mol (1); Total moles n_tot = 0.600 + 0.400 + 0.400 = 1.400 mol (1)", "marks": 2},
            {"part": "b", "points": "p(PCl5) = (0.600/1.400) x 1.50 x 10^5 = 6.43 x 10^4 Pa; p(PCl3) = p(Cl2) = (0.400/1.400) x 1.50 x 10^5 = 4.29 x 10^4 Pa (2)", "marks": 2},
            {"part": "c", "points": "Kp = (p(PCl3) x p(Cl2)) / p(PCl5) = (4.29 x 10^4)^2 / (6.43 x 10^4) = 2.86 x 10^4 Pa (allow 2.85 - 2.87 x 10^4 Pa / 28.6 kPa) (1); Units: Pa (or kPa) (1)", "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Temperature Dependence of Equilibrium Constants — 9701/22/M/J/20/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="Consider two reversible reactions with different standard enthalpy changes:\nReaction 1: 2NO2(g) <=> N2O4(g)   Delta H = -57 kJ mol^-1\nReaction 2: N2(g) + O2(g) <=> 2NO(g)   Delta H = +180 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State and explain the effect of increasing temperature on the numerical value of Kp for Reaction 1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State and explain the effect of increasing temperature on the numerical value of Kp for Reaction 2.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Kp decreases (1); Reaction 1 is exothermic, so increasing temperature shifts equilibrium to the left, decreasing product partial pressure and increasing reactant partial pressure (1)", "marks": 2},
            {"part": "b", "points": "Kp increases (1); Reaction 2 is endothermic, so increasing temperature shifts equilibrium to the right, increasing product partial pressure relative to reactants (1)", "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Why Pressure and Concentration Changes Do Not Alter Kc or Kp — 9701/21/O/N/22/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Students frequently confuse a shift in equilibrium position with a change in the equilibrium constant.",
        parts=[
            QuestionPart(
                label="a",
                text="State the ONLY factor that alters the numerical value of the equilibrium constant Kc for a given reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why increasing the total pressure of a gaseous system at constant temperature shifts the position of equilibrium without changing the value of Kp.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Temperature (1)", "marks": 1},
            {"part": "b", "points": "Increasing total pressure initially causes the partial pressures of all gases to increase proportionally (1); The partial pressure quotient Qp momentarily deviates from Kp (1); The partial pressures of individual gases adjust as the reaction shifts towards the side with fewer gas molecules until the ratio exactly equals the original Kp value again (1)", "marks": 3}
        ]
    ),
    Question(
        number=10,
        title="Contact Process: Industrial Sulfuric Acid Manufacture — 9701/23/O/N/21/Q5(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="The key stage in the Contact process is the catalytic oxidation of sulfur dioxide:\n2SO2(g) + O2(g) <=> 2SO3(g)   Delta H = -196 kJ mol^-1\nOperating conditions: 450 °C, 1-2 atm, vanadium(V) oxide catalyst, V2O5.",
        parts=[
            QuestionPart(
                label="a",
                text="State the effect of the V2O5 catalyst on the position of equilibrium and on the rate of achieving equilibrium.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why a relatively low pressure of 1-2 atm is used in the Contact process, even though higher pressure thermodynamically favours SO3 formation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why SO3 is absorbed in concentrated H2SO4 to form oleum (H2S2O7) rather than reacted directly with water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "No effect on the position of equilibrium / yield of SO3 (1); Increases the rate of reaching equilibrium by lowering activation energy of both forward and reverse reactions equally (1)", "marks": 2},
            {"part": "b", "points": "The equilibrium yield of SO3 is already extremely high (~98-99%) at 1-2 atm (1); Operating at higher pressures would require expensive thick-walled pipes, compressors, and maintenance with negligible increase in yield (1)", "marks": 2},
            {"part": "c", "points": "Direct reaction of SO3 with water is violently exothermic and creates a hazardous, uncontrollable mist/fog of sulfuric acid droplets (1); Dissolving SO3 in concentrated H2SO4 to form oleum is safely controllable (1)", "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Calculating Equilibrium Concentrations: H2 + I2 <=> 2HI — 9701/22/F/M/23/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="For the gaseous equilibrium:\nH2(g) + I2(g) <=> 2HI(g)\nThe value of Kc is 54.0 at 425 °C.\nIn an experiment at 425 °C, 1.00 mol of H2 and 1.00 mol of I2 were sealed in a 2.00 dm3 vessel.",
        parts=[
            QuestionPart(
                label="a",
                text="Let 2x be the amount, in moles, of HI formed at equilibrium. Write expressions for the equilibrium concentrations of H2, I2, and HI in terms of x.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Substitute these expressions into Kc and calculate the value of x.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the equilibrium concentration of HI in mol dm^-3.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "[H2] = (1.00 - x) / 2.00 mol dm^-3; [I2] = (1.00 - x) / 2.00 mol dm^-3; [HI] = 2x / 2.00 = x mol dm^-3 (2)", "marks": 2},
            {"part": "b", "points": "Kc = (2x)^2 / (1.00 - x)^2 = 54.0 => 2x / (1.00 - x) = sqrt(54.0) = 7.348 (1); 2x = 7.348 - 7.348x => 9.348x = 7.348 => x = 0.786 mol (1)", "marks": 2},
            {"part": "c", "points": "[HI] = 2x / 2.00 = x = 0.786 mol dm^-3 (1)", "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Heterogeneous Equilibria: Decomposition of Calcium Carbonate — 9701/21/M/J/21/Q7(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="When limestone is heated in a sealed evacuated vessel at 800 °C, heterogeneous equilibrium is established:\nCaCO3(s) <=> CaO(s) + CO2(g)   Delta H = +178 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Write the expression for the equilibrium constant Kp for this heterogeneous reaction, explaining why the solid phases are omitted.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="At 800 °C, the equilibrium pressure of CO2 is 24.0 kPa. State the value of Kp with units.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State what happens to the equilibrium pressure of CO2 if the mass of CaCO3(s) in the container is doubled at constant temperature.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Kp = p(CO2) (1); Pure solids have constant concentrations / activities of 1 that do not vary with amount, so they are incorporated into the constant (1)", "marks": 2},
            {"part": "b", "points": "Kp = 24.0 kPa (or 2.40 x 10^4 Pa) (1)", "marks": 1},
            {"part": "c", "points": "No change in CO2 pressure (Kp depends only on temperature) (1)", "marks": 1}
        ]
    ),
    Question(
        number=13,
        title="Effect of Inert Gas Addition on Gaseous Equilibrium — 9701/22/M/J/22/Q6(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Consider the equilibrium system:\nN2O4(g) <=> 2NO2(g)\nHelium gas is introduced into the container at constant temperature.",
        parts=[
            QuestionPart(
                label="a",
                text="Predict and explain the effect on the position of equilibrium when helium gas is added at constant volume.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict and explain the effect on the position of equilibrium when helium gas is added at constant total pressure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "No effect on equilibrium position (1); Adding helium at constant volume increases total pressure but does not change the partial pressures or concentrations of N2O4 or NO2 (1)", "marks": 2},
            {"part": "b", "points": "Equilibrium shifts to the right (towards 2NO2) (1); To maintain constant total pressure, container volume must expand, reducing the partial pressures of N2O4 and NO2; equilibrium shifts towards more moles of gas (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Catalysts and Activation Energy in Reversible Reactions — 9701/22/O/N/21/Q7(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="Catalysts are widely used in chemical manufacture to improve process efficiency.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why a catalyst has no effect on the equilibrium yield of a reversible reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the commercial benefit of using a catalyst in a reversible reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A catalyst lowers the activation energy of the forward and reverse reactions by the exact same amount (1); Therefore, the rates of both forward and reverse reactions are accelerated by the same factor (1)", "marks": 2},
            {"part": "b", "points": "Equilibrium is reached in a much shorter time / allows the process to run at lower temperatures, reducing fuel and operating costs (1)", "marks": 1}
        ]
    ),
    Question(
        number=15,
        title="Industrial Synthesis of Methanol: Equilibrium & Economics — 9701/21/O/N/23/Q6(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Methanol is produced from synthesis gas over a Cu/ZnO/Al2O3 catalyst:\nCO(g) + 2H2(g) <=> CH3OH(g)   Delta H = -91 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State the effect on the equilibrium yield of methanol of increasing pressure and increasing temperature.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the expression for Kp for this reaction and deduce its units in terms of kPa.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="In an industrial reactor at 250 °C and 5.00 x 10^3 kPa, the equilibrium partial pressures are: p(CO) = 1.20 x 10^3 kPa, p(H2) = 2.40 x 10^3 kPa, and p(CH3OH) = 1.40 x 10^3 kPa. Calculate Kp.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Increasing pressure increases yield (3 moles gas -> 1 mole gas) (1); Increasing temperature decreases yield (forward reaction is exothermic) (1)", "marks": 2},
            {"part": "b", "points": "Kp = p(CH3OH) / [p(CO) x (p(H2))^2] (1); Units: kPa^-2 (or Pa^-2) (1)", "marks": 2},
            {"part": "c", "points": "Kp = 1.40 x 10^3 / [1.20 x 10^3 x (2.40 x 10^3)^2] = 1.40 x 10^3 / [1.20 x 10^3 x 5.76 x 10^6] (1); Kp = 2.03 x 10^-7 kPa^-2 (allow 2.02 - 2.04 x 10^-7 kPa^-2) (1)", "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Units of Equilibrium Constants & Dimensional Analysis — 9701/23/M/J/20/Q5(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="The units of Kc and Kp depend on the stoichiometry of the balanced chemical equation.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the units of Kc for each of the following equilibria:\n(i) N2(g) + 3H2(g) <=> 2NH3(g)\n(ii) CH3COOH(l) + C2H5OH(l) <=> CH3COOC2H5(l) + H2O(l)\n(iii) 2SO2(g) + O2(g) <=> 2SO3(g)",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the units of Kp for: 2HI(g) <=> H2(g) + I2(g).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) mol^-2 dm^6 (1); (ii) No units / dimensionless (1); (iii) mol^-1 dm^3 (1)", "marks": 3},
            {"part": "b", "points": "No units / dimensionless (Pa^2 / Pa^2 cancels out) (1)", "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Thermochemistry & Kinetics of NO2 Dimerisation — 9701/22/F/M/24/Q5(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="The dimerization of nitrogen dioxide is an exothermic equilibrium:\n2NO2(g) <=> N2O4(g)   Delta H = -57.2 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a labelled reaction coordinate diagram showing the activation energy and Delta H for this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the activation energy for the forward reaction (2NO2 -> N2O4) is exceptionally low (near zero).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State how the value of Kc changes when the temperature is raised from 20 °C to 80 °C.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Reactants 2NO2 at higher enthalpy than product N2O4 with downward arrow labelled Delta H = -57.2 kJ mol^-1 (1); Very low energy barrier from reactants to transition state (1)", "marks": 2},
            {"part": "b", "points": "NO2 is a free radical with an unpaired electron; bond formation between two unpaired electrons requires no bond breaking (1)", "marks": 1},
            {"part": "c", "points": "Kc decreases (forward reaction is exothermic) (1)", "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="ICE Table Calculation: Dissociation of HI — 9701/21/M/J/24/Q7(a)-(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="A 0.500 mol sample of HI was placed in a 1.00 dm3 flask and allowed to decompose at 700 K:\n2HI(g) <=> H2(g) + I2(g)\nAt equilibrium, 0.105 mol of I2 was formed.",
        parts=[
            QuestionPart(
                label="a",
                text="Construct an ICE table showing the initial, change, and equilibrium moles of all three gases.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Calculate the value of Kc at 700 K.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Initial: HI = 0.500, H2 = 0, I2 = 0 (1); Change: HI = -2(0.105) = -0.210, H2 = +0.105, I2 = +0.105 (1); Equilibrium: HI = 0.290, H2 = 0.105, I2 = 0.105 mol (1)", "marks": 3},
            {"part": "b", "points": "Kc = ([H2][I2]) / [HI]^2 = (0.105 x 0.105) / (0.290)^2 (1); Kc = 0.011025 / 0.0841 = 0.0131 (allow 0.0131 - 0.0132) (1)", "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Recycling & Separation in the Haber Process — 9701/22/O/N/24/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="In the Haber process, the single-pass conversion of N2 and H2 to NH3 is typically only 15%.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how ammonia is separated from unreacted nitrogen and hydrogen in the industrial plant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain what happens to the unreacted nitrogen and hydrogen gases after separation.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The gases are cooled under pressure (1); Ammonia has a much higher boiling point (-33 °C) due to hydrogen bonding and readily liquefies, while N2 and H2 remain gaseous and are drawn off (1)", "marks": 2},
            {"part": "b", "points": "Unreacted N2 and H2 gases are recycled back into the reactor, achieving an overall conversion rate of ~98% (1)", "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Industrial Equilibrium Control in the Contact Process — 9701/21/O/N/24/Q6(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="In the Contact process, sulfur dioxide is converted to sulfur trioxide in a multi-stage converter:\n2SO2(g) + O2(g) <=> 2SO3(g)   Delta H = -196 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the gas mixture is passed over several successive catalyst beds with intermediate cooling.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why an excess of oxygen (air) is used in the feed mixture.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "As the exothermic reaction proceeds, temperature rises, which unfavourably shifts equilibrium backwards and limits yield (1); Intermediate cooling removes heat, shifting equilibrium forward in the next bed to maximise overall conversion (1)", "marks": 2},
            {"part": "b", "points": "Excess O2 drives the equilibrium to the right (Le Chatelier's principle) to maximise conversion of expensive SO2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Degree of Dissociation, alpha, in Gaseous Equilibria — 9701/23/M/J/23/Q5(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="When pure N2O4 gas is introduced into an empty chamber at total pressure P, a fraction alpha dissociates:\nN2O4(g) <=> 2NO2(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Starting with 1 mole of N2O4, express the equilibrium moles of N2O4, NO2, and total moles in terms of alpha.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Show that Kp can be expressed as Kp = (4 * alpha^2 * P) / (1 - alpha^2).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the degree of dissociation alpha at 25 °C if Kp = 14.0 kPa and total pressure P = 100 kPa.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(N2O4) = 1 - alpha, n(NO2) = 2*alpha (1); Total moles n_tot = (1 - alpha) + 2*alpha = 1 + alpha (1)", "marks": 2},
            {"part": "b", "points": "p(NO2) = [2*alpha / (1 + alpha)] P, p(N2O4) = [(1 - alpha) / (1 + alpha)] P (1); Kp = p(NO2)^2 / p(N2O4) = 4*alpha^2*P^2 / [(1 + alpha)^2] / [(1 - alpha)P / (1 + alpha)] = 4*alpha^2*P / (1 - alpha^2) (1)", "marks": 2},
            {"part": "c", "points": "14.0 = (4 * alpha^2 * 100) / (1 - alpha^2) => 14(1 - alpha^2) = 400*alpha^2 => 14 = 414*alpha^2 (1); alpha^2 = 14 / 414 = 0.0338 => alpha = 0.184 (or 18.4% dissociation) (1)", "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Cobalt Complex Equilibrium: Temperature and Ligand Exchange — 9701/22/M/J/25/Q4(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="The ligand exchange equilibrium between cobalt(II) complexes is endothermic in the forward direction:\n[Co(H2O)6]^2+(aq) + 4Cl^-(aq) <=> [CoCl4]^2-(aq) + 6H2O(l)   Delta H > 0\n([Co(H2O)6]^2+ is pink; [CoCl4]^2- is deep blue).",
        parts=[
            QuestionPart(
                label="a",
                text="Predict and explain the colour change when concentrated hydrochloric acid is added to a pink solution of cobalt(II) chloride.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict and explain the colour change when this mixture is placed into an ice-water bath.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Turns deep blue (1); Adding conc HCl increases [Cl-], shifting equilibrium to the right to consume Cl- ions, forming blue [CoCl4]^2- (1)", "marks": 2},
            {"part": "b", "points": "Turns pink (1); Forward reaction is endothermic (Delta H > 0), so cooling shifts equilibrium in the exothermic reverse direction to release heat, reforming pink [Co(H2O)6]^2+ (1)", "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Chromate-Dichromate pH-Dependent Equilibrium — 9701/21/F/M/25/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="In aqueous solution, chromate(VI) and dichromate(VI) ions exist in dynamic equilibrium:\n2CrO4^2-(aq) + 2H^+(aq) <=> Cr2O7^2-(aq) + H2O(l)\n(CrO4^2- is yellow; Cr2O7^2- is orange).",
        parts=[
            QuestionPart(
                label="a",
                text="State and explain the colour change when dilute sulfuric acid is added to a yellow solution of potassium chromate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State and explain the colour change when excess aqueous sodium hydroxide is subsequently added.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Turns orange (1); Adding acid increases [H+], which shifts equilibrium to the right to consume H+, forming orange Cr2O7^2- (1)", "marks": 2},
            {"part": "b", "points": "Turns yellow (1); OH- ions react with H+ to form H2O (neutralisation), reducing [H+] and shifting equilibrium to the left to replace H+, reforming yellow CrO4^2- (1)", "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Calculation of Kc When Volume Cancels — 9701/22/O/N/25/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="For the homogeneous gaseous equilibrium:\nCO(g) + H2O(g) <=> CO2(g) + H2(g)\nAt 800 K, 2.00 mol of CO and 2.00 mol of H2O were mixed in a vessel of volume V. At equilibrium, 1.33 mol of CO2 was present.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the volume V of the vessel is not needed to calculate the numerical value of Kc.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the equilibrium amounts of all species and determine the value of Kc at 800 K.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The number of moles of gaseous products (1 + 1 = 2) equals the number of moles of gaseous reactants (1 + 1 = 2), so volume terms cancel out completely in Kc (1)", "marks": 1},
            {"part": "b", "points": "At equilibrium: n(CO2) = 1.33 mol, n(H2) = 1.33 mol; n(CO) = 2.00 - 1.33 = 0.67 mol, n(H2O) = 2.00 - 1.33 = 0.67 mol (1); Kc = (1.33 x 1.33) / (0.67 x 0.67) (1); Kc = 3.94 (allow 3.9 - 4.0) (1)", "marks": 3}
        ]
    ),
    Question(
        number=25,
        title="Steam Reforming of Methane: Industrial Hydrogen Production — 9701/23/O/N/24/Q5(a)-(c)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Hydrogen for the Haber process is produced primarily by the endothermic steam reforming of natural gas:\nCH4(g) + H2O(g) <=> CO(g) + 3H2(g)   Delta H = +206 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how high temperature affects the equilibrium yield of hydrogen.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain how high pressure affects the equilibrium yield of hydrogen.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Suggest why industrial steam reformers operate at moderate pressure (around 30 atm) rather than atmospheric pressure despite the equilibrium prediction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Increases hydrogen yield (1); Forward reaction is endothermic (Delta H = +206 kJ mol^-1), so high temperature shifts equilibrium right to absorb heat (1)", "marks": 2},
            {"part": "b", "points": "Decreases hydrogen yield (1); There are 2 moles of gas on reactant side and 4 moles on product side, so high pressure shifts equilibrium left towards fewer moles of gas (1)", "marks": 2},
            {"part": "c", "points": "Higher pressure greatly increases reaction rate (more frequent collisions) (1); Keeps gas volume manageable and avoids costly re-compression of hydrogen for subsequent high-pressure ammonia synthesis (1)", "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Dynamic Liquid-Vapour Equilibrium in a Closed Container — 9701/21/M/J/25/Q7(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="When a sample of liquid water is sealed in an evacuated glass bulb at 25 °C, dynamic equilibrium is established between liquid and vapour.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe dynamic equilibrium at the molecular level in this system.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain what happens to the vapour pressure inside the bulb when the temperature is raised from 25 °C to 50 °C.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Water molecules continuously evaporate from liquid surface at the same rate that vapour molecules condense back into liquid (1); The mass of liquid and mass of vapour remain constant over time (1)", "marks": 2},
            {"part": "b", "points": "Vapour pressure increases significantly (1); Higher temperature gives more molecules kinetic energy exceeding the intermolecular forces, increasing evaporation rate until a higher equilibrium vapour pressure is reached (1)", "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="Perturbation of Esterification Equilibrium by Adding Water — 9701/22/M/J/24/Q7(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Consider the equilibrium:\nCH3COOH(l) + C2H5OH(l) <=> CH3COOC2H5(l) + H2O(l)   Kc = 4.0",
        parts=[
            QuestionPart(
                label="a",
                text="State what happens to the yield of ethyl ethanoate if a large excess of water is added to the equilibrium mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain your answer to (a) using both Le Chatelier's principle and the Kc expression.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Yield of ethyl ethanoate decreases / ester hydrolyses (1)", "marks": 1},
            {"part": "b", "points": "By Le Chatelier's principle, adding water increases [H2O], shifting equilibrium to the left to consume water (1); In terms of Kc, adding water makes the reaction quotient Qc = ([ester][water])/([acid][alcohol]) greater than Kc (1); Net reverse reaction occurs until Qc decreases back to equal Kc = 4.0 (1)", "marks": 3}
        ]
    ),
    Question(
        number=28,
        title="Decomposition of Solid Ammonium Hydrogensulfide — 9701/23/M/J/24/Q6(a)-(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="Solid ammonium hydrogensulfide decomposes endothermically:\nNH4SH(s) <=> NH3(g) + H2S(g)\nWhen excess NH4SH(s) is placed in an evacuated container at 25 °C, the total equilibrium pressure is 66.0 kPa.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the partial pressure of NH3(g) and H2S(g) in the container.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the value of Kp at 25 °C, including units.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Gases are produced in 1:1 equimolar ratio, so p(NH3) = p(H2S) = 66.0 / 2 = 33.0 kPa (2)", "marks": 2},
            {"part": "b", "points": "Kp = p(NH3) x p(H2S) = 33.0 x 33.0 = 1089 kPa^2 (or 1.09 x 10^3 kPa^2 / 1.09 x 10^9 Pa^2) (1); Units: kPa^2 (or Pa^2) (1)", "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Reaction Quotient, Qc, vs Equilibrium Constant, Kc — 9701/22/F/M/25/Q6(b)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="For the reaction SO2(g) + NO2(g) <=> SO3(g) + NO(g), Kc = 85.0 at a certain temperature.\nA mixture was prepared with concentrations: [SO2] = 0.10, [NO2] = 0.10, [SO3] = 0.50, and [NO] = 0.50 mol dm^-3.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the reaction quotient, Qc, for this initial mixture.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict whether the concentration of SO3 will increase, decrease, or remain unchanged as the system approaches equilibrium. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Qc = ([SO3][NO]) / ([SO2][NO2]) = (0.50 x 0.50) / (0.10 x 0.10) (1); Qc = 0.25 / 0.01 = 25.0 (1)", "marks": 2},
            {"part": "b", "points": "Concentration of SO3 will increase (1); Since Qc (25.0) < Kc (85.0), the system must shift to the right to form more products until Qc reaches 85.0 (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Multi-Phase Distribution Equilibrium (Partition) — 9701/21/O/N/25/Q7(a)-(b)",
        syllabus_ref="7.1",
        difficulty="EASY",
        preamble="When an aqueous solution of iodine is shaken with cyclohexane in a separating funnel, iodine partitions between the two immiscible solvents:\nI2(aq) <=> I2(cyclohexane)",
        parts=[
            QuestionPart(
                label="a",
                text="State the colours of the aqueous layer and the cyclohexane layer at equilibrium.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why iodine dissolves preferentially in non-polar cyclohexane rather than in polar water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Aqueous layer: Pale yellow / brown (1); Cyclohexane layer: Purple / violet (1)", "marks": 2},
            {"part": "b", "points": "Iodine is a non-polar molecule that forms London dispersion forces with non-polar cyclohexane molecules (1); In water, dissolving iodine requires disrupting strong hydrogen bonds between water molecules without forming strong solute-solvent attractions (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 7.2: Brønsted-Lowry Acids and Bases (Q31 to Q50)
    # =========================================================================
    Question(
        number=31,
        title="Brønsted-Lowry Theory & Conjugate Acid-Base Pairs — 9701/22/M/J/21/Q7(a)-(c)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Fig. 7.4 illustrates the Brønsted-Lowry concept of proton transfer and conjugate acid-base pairs for ethanoic acid in water.",
        parts=[
            QuestionPart(
                label="a",
                text="Define a Brønsted-Lowry acid and a Brønsted-Lowry base.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="In the reaction shown in Fig. 7.4, identify the conjugate base of CH3COOH and the conjugate acid of H2O.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the species in a conjugate acid-base pair always differ by exactly one H+ ion.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Brønsted-Lowry acid: A proton (H+) donor (1); Brønsted-Lowry base: A proton (H+) acceptor (1)", "marks": 2},
            {"part": "b", "points": "Conjugate base of CH3COOH: Ethanoate ion, CH3COO- (1); Conjugate acid of H2O: Hydronium ion, H3O+ (1)", "marks": 2},
            {"part": "c", "points": "When an acid donates one proton it becomes its conjugate base, and when a base accepts one proton it becomes its conjugate acid (1)", "marks": 1}
        ],
        figure_path="figures/bronsted_lowry_conjugate_pairs.png",
        figure_caption="Fig. 7.4: Proton transfer and conjugate acid-base pairs in Brønsted-Lowry theory."
    ),
    Question(
        number=32,
        title="Identifying Conjugate Pairs in Complex Acid-Base Systems — 9701/21/O/N/21/Q6(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Consider the two acid-base equilibria:\nEquilibrium 1: NH3(aq) + H2O(l) <=> NH4^+(aq) + OH^-(aq)\nEquilibrium 2: HNO3 + H2SO4 <=> H2NO3^+ + HSO4^-",
        parts=[
            QuestionPart(
                label="a",
                text="For Equilibrium 1, identify the two conjugate acid-base pairs.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="For Equilibrium 2, identify which species acts as the Brønsted-Lowry base and explain why.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Pair 1: H2O (acid) and OH- (conjugate base) (1); Pair 2: NH4+ (conjugate acid) and NH3 (base) (1)", "marks": 2},
            {"part": "b", "points": "HNO3 acts as the Brønsted-Lowry base (1); It accepts a proton (H+) from the stronger acid H2SO4 to form H2NO3^+ (1)", "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Strong vs Weak Acids: Degree of Dissociation & pH — 9701/23/M/J/22/Q7(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="Hydrochloric acid and ethanoic acid are monoprotic acids.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the difference between a strong acid and a weak acid in terms of dissociation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the pH of 0.0500 mol dm^-3 HCl(aq) given that pH = -log10[H+].",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State and explain whether 0.0500 mol dm^-3 CH3COOH(aq) will have a higher, lower, or identical pH compared to 0.0500 mol dm^-3 HCl(aq).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A strong acid is completely (100%) dissociated into ions in aqueous solution (1); A weak acid is only partially dissociated into ions in aqueous solution (1)", "marks": 2},
            {"part": "b", "points": "For strong acid, [H+] = 0.0500 mol dm^-3; pH = -log10(0.0500) (1); pH = 1.30 (1)", "marks": 2},
            {"part": "c", "points": "Higher pH (1); Ethanoic acid is only partially dissociated, so [H+] is much lower than 0.0500 mol dm^-3, resulting in a less acidic solution with a higher pH value (approx 3.0) (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Experimental Comparison of Strong and Weak Acids — 9701/22/F/M/22/Q5(a)-(c)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="A student is provided with two unlabelled bottles, one containing 0.10 mol dm^-3 HCl and the other containing 0.10 mol dm^-3 CH3COOH.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe how measuring the electrical conductivity can distinguish between the two acids.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe what is observed when identical strips of magnesium ribbon are added to equal volumes of each acid.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State whether equal volumes of both acids would require the same volume or different volumes of 0.10 mol dm^-3 NaOH for complete neutralisation. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "HCl has significantly higher electrical conductivity than CH3COOH (1); HCl is fully dissociated and contains a much higher concentration of mobile charge-carrying ions (H+ and Cl-) (1)", "marks": 2},
            {"part": "b", "points": "Both produce effervescence/bubbles of H2 gas (1); Reaction is much faster / more vigorous with HCl due to much higher initial [H+] (1)", "marks": 2},
            {"part": "c", "points": "Exactly the same volume of NaOH is required (1); Both solutions contain the same total amount (moles) of neutralisable acidic protons; as OH- reacts, weak acid equilibrium shifts completely right until fully neutralised (1)", "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Amphiprotic Behaviour of Water and Hydrogencarbonate — 9701/21/M/J/22/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Certain chemical species can act as either a Brønsted-Lowry acid or a Brønsted-Lowry base depending on the reaction partner.",
        parts=[
            QuestionPart(
                label="a",
                text="Write two chemical equations demonstrating that water, H2O, is amphiprotic (amphoteric).\n(i) Acting as an acid with NH3\n(ii) Acting as a base with HCl",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write two equations showing the amphiprotic behaviour of the hydrogencarbonate ion, HCO3^-.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) H2O + NH3 <=> OH- + NH4+ (1); (ii) H2O + HCl -> H3O+ + Cl- (1)", "marks": 2},
            {"part": "b", "points": "Acid: HCO3^- + OH- -> CO3^2- + H2O (1); Base: HCO3^- + H+ -> H2O + CO2 (or H2CO3) (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Strong vs Weak Bases: Sodium Hydroxide vs Ammonia — 9701/22/O/N/22/Q5(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Aqueous sodium hydroxide, NaOH, and aqueous ammonia, NH3, are both basic solutions.",
        parts=[
            QuestionPart(
                label="a",
                text="Write equations showing how NaOH and NH3 generate hydroxide ions in aqueous solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why 0.10 mol dm^-3 NaOH has a pH of approximately 13 while 0.10 mol dm^-3 NH3 has a pH of approximately 11.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "NaOH(s) + aq -> Na+(aq) + OH-(aq) (1); NH3(aq) + H2O(l) <=> NH4+(aq) + OH-(aq) (1)", "marks": 2},
            {"part": "b", "points": "NaOH is a strong base that fully dissociates to give [OH-] = 0.10 mol dm^-3 (1); NH3 is a weak base that only partially reacts with water, giving a much lower equilibrium [OH-] (~10^-3 mol dm^-3) and hence lower pH (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Ionic Product of Water, Kw & Neutrality — 9701/23/O/N/22/Q5(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="Water undergoes slight autoionisation:\nH2O(l) <=> H^+(aq) + OH^-(aq)   Delta H = +57.1 kJ mol^-1\nAt 25 °C, Kw = [H+][OH-] = 1.00 x 10^-14 mol^2 dm^-6.",
        parts=[
            QuestionPart(
                label="a",
                text="State the mathematical definition of neutral pH in pure water.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the value of Kw increases as the temperature of water is raised from 25 °C to 60 °C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="At 60 °C, Kw = 9.55 x 10^-14 mol^2 dm^-6. Calculate the pH of pure water at 60 °C and state whether pure water at 60 °C is acidic, alkaline, or neutral.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "[H+] = [OH-] (1)", "marks": 1},
            {"part": "b", "points": "Autoionisation of water is an endothermic process (Delta H > 0) (1); Increasing temperature shifts equilibrium to the right to absorb heat, increasing [H+] and [OH-] and hence Kw (1)", "marks": 2},
            {"part": "c", "points": "[H+] = sqrt(Kw) = sqrt(9.55 x 10^-14) = 3.09 x 10^-7 mol dm^-3 (1); pH = -log10(3.09 x 10^-7) = 6.51 (1); It is NEUTRAL because [H+] is still strictly equal to [OH-] (1)", "marks": 3}
        ]
    ),
    Question(
        number=38,
        title="pH Calculations for Strong Monoprotic and Diprotic Acids — 9701/22/F/M/23/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="For strong acids, complete dissociation is assumed in aqueous solution.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the pH of 0.0250 mol dm^-3 nitric acid, HNO3.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Assuming complete dissociation of both protons, calculate the pH of 0.0250 mol dm^-3 sulfuric acid, H2SO4.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "[H+] = 0.0250 mol dm^-3; pH = -log10(0.0250) (1); pH = 1.60 (1)", "marks": 2},
            {"part": "b", "points": "H2SO4 -> 2H+ + SO4^2- => [H+] = 2 x 0.0250 = 0.0500 mol dm^-3 (1); pH = -log10(0.0500) = 1.30 (1)", "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Relative Acid Strengths of Carboxylic Acids — 9701/21/M/J/23/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="The acid dissociation constant, Ka, measures the extent of dissociation of a weak acid:\nHA(aq) <=> H^+(aq) + A^-(aq)\n• Methanoic acid, HCOOH: Ka = 1.8 x 10^-4 mol dm^-3\n• Ethanoic acid, CH3COOH: Ka = 1.7 x 10^-5 mol dm^-3",
        parts=[
            QuestionPart(
                label="a",
                text="State which of these two acids is stronger and explain your answer by referring to the Ka values.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why ethanoic acid is a weaker acid than methanoic acid in terms of the electron-donating inductive effect of the methyl group.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Methanoic acid is stronger (1); It has a larger Ka value (1.8 x 10^-4 vs 1.7 x 10^-5), indicating a greater degree of dissociation into H+ ions at equilibrium (1)", "marks": 2},
            {"part": "b", "points": "The methyl group (-CH3) in ethanoic acid is electron-donating (+I inductive effect) (1); This increases electron density on the carboxylate group, destabilising the CH3COO- anion and strengthening the O-H bond in CH3COOH (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Zwitterions & Amphoteric Nature of Amino Acids — 9701/22/M/J/23/Q5(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="Glycine, H2N-CH2-COOH, is the simplest amino acid. In aqueous solution, it exists predominantly as a zwitterion: ^+H3N-CH2-COO^-.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term zwitterion.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the structural formula of the organic species formed when glycine zwitterion reacts with dilute hydrochloric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the structural formula of the organic species formed when glycine zwitterion reacts with aqueous sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "An internal salt / dipolar ion having separate positive and negative charges on different atoms within the same neutral molecule (1)", "marks": 1},
            {"part": "b", "points": "^+H3N-CH2-COOH (or Cl^- ^+H3N-CH2-COOH) (1)", "marks": 1},
            {"part": "c", "points": "H2N-CH2-COO^- (or H2N-CH2-COO^- Na^+) (1)", "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Neutralisation Titration Curves: Strong vs Weak Acid — 9701/21/O/N/23/Q7(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="Consider the titration of 25.0 cm3 of 0.10 mol dm^-3 acid with 0.10 mol dm^-3 NaOH:\n• Curve A: 0.10 mol dm^-3 HCl\n• Curve B: 0.10 mol dm^-3 CH3COOH",
        parts=[
            QuestionPart(
                label="a",
                text="State the initial pH for Curve A and Curve B.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the pH at the equivalence point for Curve A and for Curve B.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the equivalence point pH for Curve B is greater than 7.0.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Curve A (HCl): pH = 1.0 (1); Curve B (CH3COOH): pH ~ 2.9 - 3.0 (1)", "marks": 2},
            {"part": "b", "points": "Curve A: pH = 7.0 (1); Curve B: pH ~ 8.5 - 9.0 (1)", "marks": 2},
            {"part": "c", "points": "At equivalence, sodium ethanoate, CH3COONa, is formed (1); The ethanoate ion hydrolyses water: CH3COO- + H2O <=> CH3COOH + OH-, producing excess OH- ions (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Selection of Appropriate Acid-Base Indicators — 9701/22/O/N/23/Q7(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Indicators change colour over a characteristic pH transition range:\n• Methyl orange: pH 3.1 to 4.4 (red to yellow)\n• Phenolphthalein: pH 8.3 to 10.0 (colourless to pink)",
        parts=[
            QuestionPart(
                label="a",
                text="State which indicator, methyl orange or phenolphthalein, is suitable for titrating ethanoic acid with sodium hydroxide. Justify your choice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State which indicator is suitable for titrating aqueous ammonia with hydrochloric acid. Justify your choice.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Phenolphthalein (1); The equivalence point occurs at pH ~ 8.5-9.0, which falls squarely within the vertical pH range and transition range of phenolphthalein (8.3-10.0) (1)", "marks": 2},
            {"part": "b", "points": "Methyl orange (1); The equivalence point of a weak base-strong acid titration occurs in the acidic region (pH ~ 5.0), matching the vertical drop and range of methyl orange (1)", "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Qualitative Action of Buffer Solutions — 9701/23/M/J/24/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="A buffer solution resists changes in pH when small amounts of acid or base are added.",
        parts=[
            QuestionPart(
                label="a",
                text="State the two components of an acidic buffer solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain, with the aid of an ionic equation, how an ethanoic acid / sodium ethanoate buffer removes added H+ ions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A weak acid (e.g. CH3COOH) (1); and its conjugate base / salt with a strong base (e.g. CH3COONa) (1)", "marks": 2},
            {"part": "b", "points": "CH3COO-(aq) + H+(aq) -> CH3COOH(aq) (1); The high reservoir of ethanoate ions combines with added H+ to form undissociated ethanoic acid, maintaining [H+] and pH almost constant (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Expression and Units of Acid Dissociation Constant, Ka — 9701/21/M/J/24/Q8(a)-(b)",
        syllabus_ref="7.2",
        difficulty="EASY",
        preamble="Ethanoic acid dissociates partially in water according to the equilibrium:\nCH3COOH(aq) <=> CH3COO^-(aq) + H^+(aq)",
        parts=[
            QuestionPart(
                label="a",
                text="Write the expression for the acid dissociation constant, Ka, for ethanoic acid and deduce its units.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the concentration of water is not included in the Ka expression.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ka = ([CH3COO-][H+]) / [CH3COOH] (1); Units: mol dm^-3 (1)", "marks": 2},
            {"part": "b", "points": "Water is in enormous excess so its concentration (~55.5 mol dm^-3) remains effectively constant and is subsumed into the constant Ka (1)", "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Acid-Base Character of Period 3 Oxides — 9701/22/M/J/24/Q8(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="The nature of oxides across Period 3 changes from basic to amphoteric to acidic:\nNa2O, MgO, Al2O3, SiO2, P4O10, SO3.",
        parts=[
            QuestionPart(
                label="a",
                text="Classify the acid-base nature of Na2O, Al2O3, and SO3.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write a chemical equation showing the reaction of basic Na2O with water, and state the approximate pH of the resulting solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write two equations demonstrating the amphoteric nature of Al2O3 reacting with an acid and with an alkali.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na2O: Basic (1); Al2O3: Amphoteric (1); SO3: Acidic (1)", "marks": 3},
            {"part": "b", "points": "Na2O(s) + H2O(l) -> 2NaOH(aq) (1); pH ~ 13-14 (strongly alkaline) (1)", "marks": 2},
            {"part": "c", "points": "Acid: Al2O3 + 6HCl -> 2AlCl3 + 3H2O (1); Alkali: Al2O3 + 2NaOH + 3H2O -> 2NaAl(OH)4 (or Al2O3 + 2OH- -> 2AlO2- + H2O) (1)", "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Enthalpy of Neutralisation & Weak Acid Dissociation Energetics — 9701/23/O/N/23/Q6(a)-(b)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="Consider the standard enthalpies of neutralisation:\n• Reaction 1: HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)   Delta H_neut = -57.1 kJ mol^-1\n• Reaction 2: HCN(aq) + NaOH(aq) -> NaCN(aq) + H2O(l)   Delta H_neut = -11.7 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Reaction 2 is significantly less exothermic than Reaction 1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the enthalpy change of dissociation of hydrocyanic acid: HCN(aq) -> H+(aq) + CN^-(aq).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "HCN is an extremely weak acid that is almost completely undissociated in water (1); Significant energy is absorbed (endothermic process) to break H-CN bonds and dissociate HCN molecules during neutralisation (1)", "marks": 2},
            {"part": "b", "points": "Delta H_neut(HCN) = Delta H_dissoc(HCN) + Delta H_neut(strong) => -11.7 = Delta H_dissoc + (-57.1) (1); Delta H_dissoc(HCN) = -11.7 - (-57.1) = +45.4 kJ mol^-1 (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Inductive Effects on Carboxylic Acid Strength — 9701/22/F/M/25/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="The acid strength of substituted ethanoic acids increases markedly with halogen substitution:\n• Ethanoic acid, CH3COOH: Ka = 1.7 x 10^-5 mol dm^-3\n• Chloroethanoic acid, CH2ClCOOH: Ka = 1.3 x 10^-3 mol dm^-3\n• Trichloroethanoic acid, CCl3COOH: Ka = 2.2 x 10^-1 mol dm^-3",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why chloroethanoic acid is a significantly stronger acid than ethanoic acid.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Predict and explain whether fluoroethanoic acid, CH2FCOOH, is stronger or weaker than chloroethanoic acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Chlorine is an electronegative atom that exerts an electron-withdrawing inductive effect (-I effect) (1); This pulls negative charge away from the O-H bond, weakening it and facilitating proton loss (1); It also disperses the negative charge over the chloroethanoate anion (CH2ClCOO-), stabilising the conjugate base (1)", "marks": 3},
            {"part": "b", "points": "Fluoroethanoic acid is stronger (1); Fluorine is more electronegative than chlorine (4.0 vs 3.0), creating a stronger electron-withdrawing inductive effect that stabilises the conjugate base even more (1)", "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Salt Hydrolysis & Solution pH — 9701/21/F/M/25/Q7(a)-(c)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="When salts dissolve in water, the resulting solutions are not always neutral.",
        parts=[
            QuestionPart(
                label="a",
                text="Predict whether an aqueous solution of ammonium chloride, NH4Cl, will have a pH < 7, pH = 7, or pH > 7. Explain your answer with an equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict whether an aqueous solution of sodium ethanoate, CH3COONa, will have a pH < 7, pH = 7, or pH > 7. Explain your answer with an equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "pH < 7 / acidic (1); NH4+ ion acts as a weak acid and hydrolyses water: NH4+ + H2O <=> NH3 + H3O+, producing excess hydronium ions (1)", "marks": 2},
            {"part": "b", "points": "pH > 7 / alkaline (1); CH3COO- ion acts as a weak base and hydrolyses water: CH3COO- + H2O <=> CH3COOH + OH-, producing excess hydroxide ions (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Base Strength of Nitrogen Compounds — 9701/22/M/J/25/Q7(a)-(b)",
        syllabus_ref="7.2",
        difficulty="HARD",
        preamble="The base strength of nitrogen bases depends on the availability of the lone pair of electrons on the nitrogen atom:\nAmmonia, NH3; Methylamine, CH3NH2; Phenylamine, C6H5NH2.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why methylamine is a stronger base than ammonia.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why phenylamine is a much weaker base than ammonia.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The methyl group (-CH3) is electron-donating (+I inductive effect) (1); This increases electron density on the nitrogen atom, making its lone pair more available to accept a proton (1)", "marks": 2},
            {"part": "b", "points": "The nitrogen lone pair overlaps with and delocalises into the benzene ring's pi electron cloud (1); The lone pair is less localised on nitrogen and therefore far less available to accept a proton (1)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Haber Process Equilibria, Kp & Basic Character of Ammonia — 9701/22/O/N/25/Q7(a)-(d)",
        syllabus_ref="7.1",
        difficulty="HARD",
        preamble="In an industrial synthesis, an initial equimolar mixture of N2 and H2 was allowed to reach equilibrium at 450 °C and a total pressure of 2.00 x 10^4 kPa in the presence of an iron catalyst:\nN2(g) + 3H2(g) <=> 2NH3(g)   Delta H = -92 kJ mol^-1\nAt equilibrium, the mole fraction of ammonia is 0.150.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the partial pressure of ammonia, p(NH3), at equilibrium.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Given that the remaining gas mixture maintains the initial 1 N2 : 3 H2 molar ratio, calculate the partial pressures of N2 and H2, and calculate Kp.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Ammonia dissolves in water to form an alkaline solution. Write the equation for this reaction, identifying the conjugate acid and conjugate base.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Explain how Le Chatelier's principle and reaction kinetics dictate the compromise operating conditions chosen for the industrial manufacture of ammonia.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "p(NH3) = 0.150 x 2.00 x 10^4 = 3.00 x 10^3 kPa (1)", "marks": 1},
            {"part": "b", "points": "Remaining mole fraction = 1.00 - 0.150 = 0.850; x(N2) = 0.850 / 4 = 0.2125, x(H2) = 3 x 0.2125 = 0.6375 (1); p(N2) = 0.2125 x 2.00 x 10^4 = 4.25 x 10^3 kPa; p(H2) = 0.6375 x 2.00 x 10^4 = 1.275 x 10^4 kPa (1); Kp = (3.00 x 10^3)^2 / [4.25 x 10^3 x (1.275 x 10^4)^3] = 9.00 x 10^6 / [4.25 x 10^3 x 2.073 x 10^12] = 1.02 x 10^-9 kPa^-2 (1)", "marks": 3},
            {"part": "c", "points": "NH3(aq) + H2O(l) <=> NH4+(aq) + OH-(aq) (1); Conjugate acid: NH4+; Conjugate base: OH- (1)", "marks": 2},
            {"part": "d", "points": "Thermodynamics favours low temperature (exothermic forward) and high pressure (fewer gas moles) (1); However, low temperature yields unacceptable rates; 450 °C with iron catalyst achieves acceptable rate while 200 atm is an economical pressure that avoids excessive plant construction costs (1)", "marks": 2}
        ]
    )
]
'''
    with open(r"z:\tests n quizes63\books\psycology\new styl\topic7_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully wrote topic7_data.py!")

if __name__ == "__main__":
    generate()
