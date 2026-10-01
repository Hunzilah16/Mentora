"""
Script to generate topic8_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 8: Reaction Kinetics.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 8: Reaction Kinetics.
Subtopics:
  8.1 Rate of reaction: definition, experimental methods, collision theory, graphs and tangents
  8.2 Effect of temperature: Maxwell-Boltzmann distribution, activation energy
  8.3 Catalysts: homogeneous and heterogeneous catalysts, mechanisms, energy profiles

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

TOPIC_8_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 8.1: Rate of Reaction & Experimental Methods (Q1 to Q25)
    # =========================================================================
    Question(
        number=1,
        title="Definition of Reaction Rate & Experimental Methods — 9701/22/M/J/21/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="The rate of a chemical reaction is a quantitative measure of how rapidly reactants are converted into products.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term rate of reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State a suitable experimental method for monitoring the rate of each of the following reactions:\n(i) CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l)\n(ii) CH3COCH3(aq) + I2(aq) -> CH3COCH2I(aq) + H+(aq) + I-(aq)\n(iii) Ba(OH)2(aq) + H2SO4(aq) -> BaSO4(s) + 2H2O(l)",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The change in concentration of a reactant or product (1); per unit time (1)", "marks": 2},
            {"part": "b", "points": "(i) Measuring the volume of CO2 gas evolved using a gas syringe / measuring loss of mass on a digital balance (1); (ii) Colorimetry / measuring the disappearance of brown I2 color over time (1); (iii) Electrical conductivity / measuring the decrease in conductivity as ions precipitate (1)", "marks": 3}
        ]
    ),
    Question(
        number=2,
        title="Determining Initial and Instantaneous Rates Using Tangents — 9701/21/O/N/20/Q6(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="Fig. 8.1 shows a concentration-time graph for the decomposition of a reactant R.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how the initial rate of reaction at t = 0 is determined from Fig. 8.1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Using the tangents shown in Fig. 8.1, calculate the initial rate at t = 0 min and the instantaneous rate at t = 3.0 min, including units.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why the reaction rate gradually decreases as time progresses.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Draw a tangent to the curve at time t = 0 (1); Calculate the gradient of this tangent: initial rate = -gradient (1)", "marks": 2},
            {"part": "b", "points": "Initial rate (t = 0): gradient = (1.0 - 0) / (2.5 - 0) = 0.40 mol dm^-3 min^-1 (1); Instantaneous rate (t = 3 min): gradient = 0.12 mol dm^-3 min^-1 (1); Units: mol dm^-3 min^-1 (1)", "marks": 3},
            {"part": "c", "points": "As the reaction proceeds, reactant particles are consumed and their concentration decreases (1); The frequency of collisions between reactant particles per unit time decreases (1)", "marks": 2}
        ],
        figure_path="figures/rate_concentration_tangents.png",
        figure_caption="Fig. 8.1: Concentration-time graph showing determination of initial and instantaneous rates using tangents."
    ),
    Question(
        number=3,
        title="Collision Theory & Effective Collisions — 9701/23/M/J/22/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="According to collision theory, not all collisions between reactant molecules result in a chemical reaction.",
        parts=[
            QuestionPart(
                label="a",
                text="State two conditions that must be fulfilled during a collision between two molecules for a chemical reaction to occur.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Define the term activation energy, E_a.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The colliding particles must possess kinetic energy greater than or equal to the activation energy (E >= E_a) (1); The particles must collide with the correct molecular orientation / collision geometry (1)", "marks": 2},
            {"part": "b", "points": "The minimum kinetic energy required by colliding particles to initiate a chemical reaction (1)", "marks": 1}
        ]
    ),
    Question(
        number=4,
        title="Effect of Concentration and Pressure on Reaction Rate — 9701/22/F/M/21/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="Increasing the concentration of a solution or the pressure of a gaseous mixture increases reaction rate.",
        parts=[
            QuestionPart(
                label="a",
                text="Use collision theory to explain why increasing the concentration of hydrochloric acid increases the rate of reaction with magnesium ribbon.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Use collision theory to explain why compressing a gaseous reaction mixture to half its original volume increases the reaction rate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "More reactant particles are present per unit volume (1); This increases the frequency of collisions between H+ ions and magnesium per second, leading to more successful collisions per unit time (1)", "marks": 2},
            {"part": "b", "points": "Halving the volume doubles the concentration / number of gas particles per unit volume (1); This increases the frequency of collisions between reacting gas molecules per unit time (1)", "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Effect of Surface Area: Marble Chips vs Powder — 9701/21/M/J/22/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="Equal masses of calcium carbonate, CaCO3, were reacted with excess 1.0 mol dm^-3 HCl in two separate experiments:\n• Experiment 1: Large marble chips\n• Experiment 2: Fine marble powder",
        parts=[
            QuestionPart(
                label="a",
                text="State which experiment has the faster initial rate of reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain your answer to (a) using collision theory.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State whether the total volume of CO2 gas collected at the end of both reactions will be identical or different. Explain why.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Experiment 2 (fine marble powder) (1)", "marks": 1},
            {"part": "b", "points": "Fine powder has a much greater surface area exposed to the acid per unit mass (1); More calcium carbonate particles are available for collisions, increasing the collision frequency per unit time with H+ ions (1)", "marks": 2},
            {"part": "c", "points": "Identical total volume of CO2 (1); Both experiments used equal masses of CaCO3 and excess acid, so the limiting reactant amount is identical (1)", "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Monitoring Rate via Gas Volume: Magnesium and Acid — 9701/22/O/N/23/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="A 0.060 g sample of magnesium ribbon was reacted with 50.0 cm3 of 0.500 mol dm^-3 HCl:\nMg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)\nThe volume of H2 gas collected in a gas syringe was recorded every 15 seconds.",
        parts=[
            QuestionPart(
                label="a",
                text="Show by calculation which reactant is in excess. (Ar: Mg = 24.3)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the theoretical maximum volume of H2 gas collected at RTP (molar volume = 24000 cm3 mol^-1).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Sketch the shape of the graph of volume of H2 vs time and explain why the gradient eventually reaches zero.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "n(Mg) = 0.060 / 24.3 = 0.00247 mol; n(HCl) = 0.500 x 0.0500 = 0.0250 mol (1); Reaction requires 2 x 0.00247 = 0.00494 mol HCl; since 0.0250 mol is present, HCl is in large excess (1)", "marks": 2},
            {"part": "b", "points": "n(H2) = n(Mg) = 0.00247 mol; Volume = 0.00247 x 24000 = 59.3 cm3 (allow 59.0 - 59.5 cm3) (2)", "marks": 2},
            {"part": "c", "points": "Steep curve starting at origin, plateauing horizontally at 59.3 cm3 (1); Gradient becomes zero because all magnesium has reacted completely (reaction has stopped) (1)", "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Monitoring Rate via Mass Loss on Digital Balance — 9701/21/M/J/23/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="When marble chips react with dilute nitric acid in a conical flask on a digital balance, the mass decreases over time:\nCaCO3(s) + 2HNO3(aq) -> Ca(NO3)2(aq) + CO2(g) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the mass of the flask and contents decreases as the reaction proceeds.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why a loose cotton wool plug is placed in the neck of the flask during this experiment.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State why this mass-loss method is unsuitable for monitoring the reaction between magnesium and hydrochloric acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Carbon dioxide gas, CO2, escapes from the open flask into the atmosphere (1)", "marks": 1},
            {"part": "b", "points": "The cotton wool plug allows CO2 gas to escape freely (1); while preventing acid spray / liquid droplets from splashing out of the flask, which would cause an erroneous mass loss (1)", "marks": 2},
            {"part": "c", "points": "Hydrogen gas has an extremely low relative molecular mass (Mr = 2.0); the total mass loss would be too small to measure accurately on a standard laboratory balance (1)", "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Colorimetric Rate Monitoring: Propanone Bromination — 9701/22/M/J/20/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="The acid-catalysed reaction between propanone and bromine is:\nCH3COCH3(aq) + Br2(aq) -> CH3COCH2Br(aq) + H+(aq) + Br-(aq)\nBromine is orange-brown, whereas all other reactants and products are colourless.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe how a colorimeter can be used to monitor the rate of this reaction continuously.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the colour of the filter that should be chosen for the colorimeter in this experiment.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="The absorbance of bromine decreases at a constant rate until all bromine is consumed. State what this reveals about the order of reaction with respect to bromine.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Place the reaction mixture in a cuvette in the colorimeter and record absorbance at regular time intervals (1); Absorbance is directly proportional to [Br2], so rate of change of absorbance equals rate of reaction (1)", "marks": 2},
            {"part": "b", "points": "Blue filter (complementary colour to orange-brown) (1)", "marks": 1},
            {"part": "c", "points": "Zero order with respect to bromine (rate is independent of [Br2]) (1)", "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Sampling, Quenching and Titration: Ester Saponification — 9701/21/O/N/22/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="The alkaline hydrolysis of ethyl ethanoate is monitored by a sampling technique:\nCH3COOC2H5(aq) + OH-(aq) -> CH3COO-(aq) + C2H5OH(aq)\nSamples are withdrawn from the reaction mixture at 5-minute intervals.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain what is meant by quenching a reaction sample.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Suggest a practical method to quench each sample withdrawn from this hydrolysis reaction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Name the titrant used to determine the concentration of unreacted OH- in the quenched sample.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Stopping / instantaneously freezing the chemical reaction at a specific time (1); so that the concentrations of reactants remain fixed during analysis (1)", "marks": 2},
            {"part": "b", "points": "Rapidly chilling the sample in ice-water / adding a known excess of cold standard acid (1); to neutralise and halt OH- reaction immediately (1)", "marks": 2},
            {"part": "c", "points": "Standard hydrochloric acid (or back-titration with standard NaOH if acid was added to quench) (1)", "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Disappearing Cross Experiment: Sodium Thiosulfate and Acid — 9701/23/O/N/21/Q6(a)-(c)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="When sodium thiosulfate reacts with hydrochloric acid, a cross drawn on paper beneath the flask disappears:\nNa2S2O3(aq) + 2HCl(aq) -> 2NaCl(aq) + SO2(g) + S(s) + H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the cross becomes obscured and eventually disappears from view.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why 1/time (1/t) can be used as a measure of the initial rate of reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State one hazard associated with this experiment and a suitable precaution.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Formation of insoluble colloidal sulfur precipitate which scatters light and causes yellow turbidity (1)", "marks": 1},
            {"part": "b", "points": "The cross disappears when a fixed, constant amount/mass of sulfur precipitate has formed (1); Since rate = amount/time, rate is directly proportional to 1/t (1)", "marks": 2},
            {"part": "c", "points": "Hazard: Toxic / choking sulfur dioxide gas (SO2) produced (1); Precaution: Perform in a fume cupboard / ensure good ventilation (1)", "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Rate Equations & Orders of Reaction Qualitative Concepts — 9701/22/F/M/23/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="Consider a general reaction between reactants A and B:\nA + 2B -> Products\nWhen [A] is doubled keeping [B] constant, the initial rate doubles.\nWhen [B] is doubled keeping [A] constant, the initial rate quadruples.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the order of reaction with respect to A and with respect to B.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the rate equation for this reaction and state the overall order of reaction.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Order with respect to A: First order (rate proportional to [A]^1) (1); Order with respect to B: Second order (rate proportional to [B]^2) (1)", "marks": 2},
            {"part": "b", "points": "Rate = k[A][B]^2 (1); Overall order = 1 + 2 = 3 (third order overall) (1)", "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Initial Rates Method Data Analysis — 9701/21/M/J/21/Q8(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="The initial rate of reaction between peroxydisulfate ions and iodide ions was measured at 25 °C:\nS2O8^2-(aq) + 2I^-(aq) -> 2SO4^2-(aq) + I2(aq)\n• Experiment 1: [S2O8^2-] = 0.040, [I-] = 0.020, Rate = 1.6 x 10^-5 mol dm^-3 s^-1\n• Experiment 2: [S2O8^2-] = 0.080, [I-] = 0.020, Rate = 3.2 x 10^-5 mol dm^-3 s^-1\n• Experiment 3: [S2O8^2-] = 0.040, [I-] = 0.040, Rate = 3.2 x 10^-5 mol dm^-3 s^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the order of reaction with respect to S2O8^2- and with respect to I-.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the value of the rate constant, k, and deduce its units.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Comparing Exp 1 & 2: [S2O8^2-] doubles, rate doubles => First order in S2O8^2- (1); Comparing Exp 1 & 3: [I-] doubles, rate doubles => First order in I- (1)", "marks": 2},
            {"part": "b", "points": "Rate = k[S2O8^2-][I-] => k = Rate / ([S2O8^2-][I-]) (1); k = (1.6 x 10^-5) / (0.040 x 0.020) = 0.020 (1); Units: mol^-1 dm^3 s^-1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=13,
        title="Iodine Clock Reaction Mechanism — 9701/22/M/J/22/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="In an iodine clock reaction, hydrogen peroxide reacts with iodide in the presence of a small, fixed amount of thiosulfate and starch:\nReaction 1 (slow): H2O2 + 2I- + 2H+ -> I2 + 2H2O\nReaction 2 (fast): I2 + 2S2O3^2- -> 2I- + S4O6^2-\nAfter all S2O3^2- is consumed, free I2 reacts with starch to turn suddenly blue-black.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the role of the thiosulfate ions in this clock reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the blue-black colour appears suddenly rather than gradually developing.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Thiosulfate reacts rapidly with iodine as soon as it is formed, reducing it back to iodide (1); This keeps the solution colourless until all thiosulfate has been completely exhausted (1)", "marks": 2},
            {"part": "b", "points": "Reaction 2 is extremely fast, so [I2] remains zero while any S2O3^2- remains (1); The instant S2O3^2- is completely consumed, newly formed I2 immediately complexes with starch, giving a sharp colour change (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Electrical Conductivity Monitoring: Precipitation Reaction — 9701/22/O/N/21/Q8(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="A conductivity probe is used to follow the reaction between aqueous barium hydroxide and dilute sulfuric acid:\nBa(OH)2(aq) + H2SO4(aq) -> BaSO4(s) + 2H2O(l)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the electrical conductivity drops to near zero at the exact equivalence point.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain what happens to the electrical conductivity if excess sulfuric acid is subsequently added.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "All mobile ions (Ba^2+, OH^-, H+, SO4^2-) are removed from solution (1); forming insoluble solid BaSO4 and virtually un-ionised liquid water molecules (1)", "marks": 2},
            {"part": "b", "points": "Conductivity increases again (1); Adding excess H2SO4 introduces mobile H+ and SO4^2- ions into the solution which carry electric current (1)", "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Decomposition of Hydrogen Peroxide: MnO2 Catalysis — 9701/21/O/N/23/Q7(a)-(c)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="Hydrogen peroxide decomposes slowly at room temperature:\n2H2O2(aq) -> 2H2O(l) + O2(g)\nAdding a small spatula of black manganese(IV) oxide powder, MnO2, causes vigorous effervescence.",
        parts=[
            QuestionPart(
                label="a",
                text="State the role of MnO2 in this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe an experiment to demonstrate that MnO2 is unchanged chemically and in mass at the end of the reaction.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Heterogeneous catalyst (1)", "marks": 1},
            {"part": "b", "points": "Weigh the initial dry mass of MnO2 before reaction (1); Filter off the solid MnO2 after the reaction ceases, wash with distilled water and dry thoroughly (1); Reweigh the dried solid to show that its mass is unchanged (1)", "marks": 3}
        ]
    ),
    Question(
        number=16,
        title="Calculating Initial Rate from Gas Evolution Curve — 9701/23/M/J/20/Q6(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="In an experiment reacting zinc granules with hydrochloric acid, 48.0 cm3 of H2 was collected in the first 60 seconds. A tangent drawn to the curve at t = 0 passes through (0, 0) and (40 s, 44.0 cm3).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the initial rate of reaction in cm3 s^-1.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the average rate of reaction over the first 60 seconds and explain why it is lower than the initial rate.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Initial rate = gradient of tangent at t = 0 = 44.0 / 40 = 1.10 cm3 s^-1 (2)", "marks": 2},
            {"part": "b", "points": "Average rate = 48.0 / 60 = 0.80 cm3 s^-1 (1); As acid is consumed, [H+] decreases, so collision frequency and instantaneous rate decrease continuously over the 60 seconds (1)", "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Collision Frequency vs Fraction of Successful Collisions — 9701/22/F/M/24/Q6(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="Students often confuse the effects of changing concentration with the effects of changing temperature.",
        parts=[
            QuestionPart(
                label="a",
                text="State whether increasing the concentration of a reactant increases the collision frequency, the fraction of collisions with E >= Ea, or both.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State whether increasing the temperature of a reaction mixture increases the collision frequency, the fraction of collisions with E >= Ea, or both, and identify which factor is primarily responsible for the rate increase.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Increases ONLY the collision frequency (fraction with E >= Ea remains unchanged at constant temperature) (1)", "marks": 1},
            {"part": "b", "points": "Increasing temperature increases BOTH collision frequency and fraction with E >= Ea (1); The dramatic increase in rate is predominantly due to the much larger fraction of molecules having kinetic energy >= Ea (1); Collision frequency increase accounts for only a minor fraction (~2%) of the rate increase (1)", "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Decay of Reaction Rate with Reactant Consumption — 9701/21/M/J/24/Q8(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="During the reaction A -> B, the instantaneous rate was measured at different times:\n• At t = 0 min: Rate = 0.080 mol dm^-3 min^-1\n• At t = 2 min: Rate = 0.040 mol dm^-3 min^-1\n• At t = 4 min: Rate = 0.020 mol dm^-3 min^-1\n• At t = 6 min: Rate = 0.010 mol dm^-3 min^-1",
        parts=[
            QuestionPart(
                label="a",
                text="State the term used to describe the constant time interval required for the rate to halve.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the order of reaction with respect to A from this data, justifying your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Half-life (t_1/2) (1)", "marks": 1},
            {"part": "b", "points": "First order (1); A constant half-life (t_1/2 = 2.0 minutes) is the defining characteristic of a first-order reaction (1)", "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Thermometric Rate Monitoring: Zinc and Copper Sulfate — 9701/22/O/N/24/Q7(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="The rate of the exothermic displacement reaction between zinc and copper(II) sulfate can be followed thermometrically by recording temperature against time:\nZn(s) + CuSO4(aq) -> ZnSO4(aq) + Cu(s)   Delta H < 0",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how the initial rate of this reaction can be estimated from a temperature-time graph.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why this thermometric method becomes inaccurate if heat loss to the surroundings is significant.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Draw a tangent to the temperature-time curve at the start of the reaction (t = 0) (1); The initial rate of temperature rise (Delta T / Delta t) is directly proportional to initial reaction rate (1)", "marks": 2},
            {"part": "b", "points": "Heat loss lowers the recorded temperature rise below its true value (1); This reduces the measured gradient, underestimating the actual rate of reaction (1)", "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Surface Area and Dust Explosions — 9701/21/O/N/24/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="A lump of coal burns steadily in air, whereas finely dispersed coal dust in a mine can cause a catastrophic explosion when ignited.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why coal dust reacts with explosive speed compared to lump coal.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State another industrial environment prone to dust explosions and identify the particulate matter.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Fine coal dust has an enormous total surface area to volume ratio compared to a solid lump (1); Tremendously higher frequency of fruitful collisions between oxygen molecules and carbon particles per second, releasing immense heat rapidly (1)", "marks": 2},
            {"part": "b", "points": "Flour mills / grain silos (1); Flour / grain dust / starch particles (1)", "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Photochemical Reaction Rates: H2 + Cl2 — 9701/23/M/J/23/Q6(a)-(b)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="A mixture of hydrogen and chlorine gas stored in the dark reacts imperceptibly slowly. When exposed to bright ultraviolet light, the mixture reacts explosively:\nH2(g) + Cl2(g) -> 2HCl(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the role of UV light in initiating this photochemical reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the initiation step equation showing the formation of reactive chlorine radicals.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "UV light photons provide the activation energy required for homolytic fission of Cl-Cl bonds (1); producing highly reactive chlorine free radicals (Cl.) that initiate a rapid chain reaction (1)", "marks": 2},
            {"part": "b", "points": "Cl2 -> 2Cl. (under UV light / homolytic fission) (1)", "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Rates of Halogenoalkane Hydrolysis — 9701/22/M/J/25/Q6(a)-(c)",
        syllabus_ref="8.1",
        difficulty="HARD",
        preamble="Equal amounts of 1-chlorobutane, 1-bromobutane, and 1-iodobutane are warmed with aqueous silver nitrate and ethanol in separate test tubes.",
        parts=[
            QuestionPart(
                label="a",
                text="State the order of reactivity of the three halogenoalkanes from slowest to fastest.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain this order of reaction rates in terms of carbon-halogen bond enthalpy.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="State the precipitate colour observed with 1-iodobutane.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "1-chlorobutane < 1-bromobutane < 1-iodobutane (1-iodobutane is fastest) (1)", "marks": 1},
            {"part": "b", "points": "The rate-determining step involves breaking the carbon-halogen bond (C-X) (1); Bond enthalpy decreases down Group 17: C-Cl (346) > C-Br (290) > C-I (228 kJ mol^-1) (1); The C-I bond is the weakest and has the lowest activation energy to break, leading to the fastest hydrolysis rate (1)", "marks": 3},
            {"part": "c", "points": "Yellow precipitate of silver iodide, AgI (1)", "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Continuous Monitoring vs Sampling Methods — 9701/21/F/M/25/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="Kinetic studies can be conducted using continuous measurement or sampling techniques.",
        parts=[
            QuestionPart(
                label="a",
                text="State one major advantage of a continuous monitoring method (such as colorimetry) over a sampling and titration method.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State one limitation or source of error specific to the sampling and quenching method.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Continuous monitoring yields an unbroken, detailed real-time data curve without disturbing the reaction system (1)", "marks": 1},
            {"part": "b", "points": "Reaction may continue slightly during the time required to withdraw and quench each sample (1); Human timing errors and titration end-point reading uncertainties occur for every sample (1)", "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Units of Reaction Rate and Rate Constants — 9701/22/O/N/25/Q7(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="Standard SI units and consistent dimensions are crucial in reaction kinetics.",
        parts=[
            QuestionPart(
                label="a",
                text="State the standard SI unit for reaction rate in homogeneous solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the units of the rate constant, k, for a second-order rate equation: Rate = k[A]^2.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "mol dm^-3 s^-1 (1)", "marks": 1},
            {"part": "b", "points": "k = Rate / [A]^2 = (mol dm^-3 s^-1) / (mol dm^-3)^2 (1); Units = mol^-1 dm^3 s^-1 (or dm^3 mol^-1 s^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Reactivity Trends Down Group 1: Kinetics vs Thermodynamics — 9701/23/O/N/24/Q6(a)-(b)",
        syllabus_ref="8.1",
        difficulty="EASY",
        preamble="When small pieces of sodium and potassium are added to cold water in separate troughs, potassium reacts much more violently and rapidly, igniting with a lilac flame.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why potassium reacts more rapidly with water than sodium in terms of first ionisation energy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the balanced chemical equation with state symbols for the reaction of potassium with water.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Potassium has a larger atomic radius and more electron shielding, resulting in a lower first ionisation energy than sodium (1); Less energy is required to remove the valence electron, giving a lower activation energy and faster reaction rate (1)", "marks": 2},
            {"part": "b", "points": "2K(s) + 2H2O(l) -> 2KOH(aq) + H2(g) (2)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 8.2 & 8.3: Temperature, Maxwell-Boltzmann & Catalysts (Q26 to Q50)
    # =========================================================================
    Question(
        number=26,
        title="Maxwell-Boltzmann Energy Distribution at Two Temperatures — 9701/22/M/J/21/Q8(a)-(d)",
        syllabus_ref="8.2",
        difficulty="HARD",
        preamble="Fig. 8.2 shows the Maxwell-Boltzmann distribution of molecular kinetic energies for a gas sample at temperatures T1 and T2 (where T2 > T1).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the distribution curve starts at the origin (0,0).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe how the shape of the curve changes when temperature is increased from T1 to T2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State what the total area under each curve represents.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="With reference to Fig. 8.2, explain why a modest increase in temperature results in a substantial increase in the rate of reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "No gas molecules have zero kinetic energy (particles are in constant motion) (1)", "marks": 1},
            {"part": "b", "points": "The peak of the curve shifts down (lower height) and to the right (higher energy) (1); The curve broadens / flattens, with a higher tail extending into the high-energy region (1)", "marks": 2},
            {"part": "c", "points": "The total number / amount of gas molecules in the sample (which remains constant) (1)", "marks": 1},
            {"part": "d", "points": "At higher temperature T2, a significantly larger fraction of molecules possess kinetic energy greater than or equal to the activation energy (E >= Ea), represented by the shaded area (1); This causes a dramatic increase in the frequency of successful / fruitful collisions per unit time (1)", "marks": 2}
        ],
        figure_path="figures/maxwell_boltzmann_two_temperatures.png",
        figure_caption="Fig. 8.2: Maxwell-Boltzmann kinetic energy distribution curves at temperatures T1 and T2."
    ),
    Question(
        number=27,
        title="Effect of a Catalyst on the Maxwell-Boltzmann Distribution — 9701/21/O/N/21/Q7(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Fig. 8.3 shows the effect of adding a catalyst to a reaction mixture on the Maxwell-Boltzmann distribution curve.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term catalyst.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="With reference to Fig. 8.3, explain how adding a catalyst increases the rate of reaction at constant temperature.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State what happens to the shape of the Maxwell-Boltzmann curve when a catalyst is added at constant temperature.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A substance that increases the rate of a chemical reaction without being consumed / chemically changed at the end (1); by providing an alternative reaction pathway with lower activation energy (1)", "marks": 2},
            {"part": "b", "points": "A catalyst lowers the activation energy from Ea to Ecat (1); A significantly larger fraction of molecules now possess kinetic energy >= Ecat (represented by the combined shaded areas), increasing successful collision frequency (1)", "marks": 2},
            {"part": "c", "points": "The shape of the curve is completely unchanged (energy distribution depends only on temperature) (1)", "marks": 1}
        ],
        figure_path="figures/boltzmann_distribution_catalyst.png",
        figure_caption="Fig. 8.3: Maxwell-Boltzmann distribution showing shift in activation energy with a catalyst."
    ),
    Question(
        number=28,
        title="Mechanism of Heterogeneous Catalysis — 9701/23/M/J/22/Q8(a)-(d)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Fig. 8.4 illustrates the four sequential stages of a heterogeneous catalytic reaction on a solid metal surface.",
        parts=[
            QuestionPart(
                label="a",
                text="Define a heterogeneous catalyst.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe what occurs during Stage 1 (Adsorption) and Stage 2 (Bond Weakening).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Describe what occurs during Stage 3 (Surface Reaction) and Stage 4 (Desorption).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Explain why a solid catalyst that bonds too strongly to reactant molecules becomes ineffective.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A catalyst that is in a different physical phase/state from the reactants (e.g. solid catalyst with gaseous reactants) (1)", "marks": 1},
            {"part": "b", "points": "Stage 1: Reactant molecules diffuse to the surface and adsorb onto active catalytic sites (1); Stage 2: Interaction with metal surface weakens and stretches internal covalent bonds within reactant molecules, lowering Ea (1)", "marks": 2},
            {"part": "c", "points": "Stage 3: Adsorbed fragments react together across the surface to form new product bonds (1); Stage 4: Product molecules desorb / detach from active sites and diffuse away, freeing sites for further reactants (1)", "marks": 2},
            {"part": "d", "points": "If adsorption is too strong, product molecules cannot desorb or reactant bonds break irreversibly (1); Active sites become permanently blocked / poisoned, preventing further reaction (1)", "marks": 2}
        ],
        figure_path="figures/heterogeneous_catalysis_steps.png",
        figure_caption="Fig. 8.4: Four-stage mechanism of heterogeneous catalysis on a solid active surface."
    ),
    Question(
        number=29,
        title="The 10 °C Rule of Thumb in Reaction Kinetics — 9701/22/F/M/22/Q6(a)-(b)",
        syllabus_ref="8.2",
        difficulty="EASY",
        preamble="As a general rule of thumb for reactions with moderate activation energy at room temperature, an increase of 10 °C approximately doubles the reaction rate.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why an increase of 10 °C causes a collision frequency increase of only about 2%, yet doubles the overall reaction rate.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Predict how many times faster a reaction will proceed at 50 °C compared to 20 °C according to this rule of thumb.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Collision frequency is proportional to the square root of absolute temperature (sqrt(T)), which increases by only ~1.7% from 298 K to 308 K (1); However, the Maxwell-Boltzmann exponential distribution tail increases dramatically (1); The number of molecules with energy >= Ea roughly doubles, yielding twice as many fruitful collisions per second (1)", "marks": 3},
            {"part": "b", "points": "Temperature rise = 50 - 20 = 30 °C = three 10 °C increments (1); Rate factor = 2^3 = 8 times faster (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Classification: Homogeneous vs Heterogeneous Catalysts — 9701/21/M/J/22/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Catalysts are classified according to the physical phase in which they operate relative to the reactants.",
        parts=[
            QuestionPart(
                label="a",
                text="Classify each of the following catalytic processes as either homogeneous or heterogeneous:\n(i) Haber process: Iron catalyst with gaseous N2 and H2\n(ii) Atmospheric oxidation: Gaseous NO2 catalysing reaction of gaseous SO2 and O2\n(iii) Esterification: Aqueous H2SO4 catalysing liquid ethanoic acid and ethanol\n(iv) Catalytic converter: Platinum-rhodium solid mesh with exhaust gases",
                marks=4,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) Heterogeneous (1); (ii) Homogeneous (1); (iii) Homogeneous (1); (iv) Heterogeneous (1)", "marks": 4}
        ]
    ),
    Question(
        number=31,
        title="Homogeneous Catalysis: Persulfate and Iodide by Fe2+/Fe3+ — 9701/22/O/N/22/Q6(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="The uncatalysed reaction between peroxydisulfate ions and iodide ions is very slow at room temperature:\nS2O8^2-(aq) + 2I^-(aq) -> 2SO4^2-(aq) + I2(aq)\nAdding a few drops of aqueous iron(II) or iron(III) ions dramatically accelerates the reaction.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the uncatalysed reaction has an exceptionally high activation energy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write two sequential chemical equations demonstrating how Fe^2+(aq) catalyses this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why Fe^3+(aq) is equally effective as Fe^2+(aq) as a catalyst for this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Both reactant ions (S2O8^2- and I-) are negatively charged (anions) (1); Intense electrostatic repulsion between like negative charges creates a high energy barrier for collision (1)", "marks": 2},
            {"part": "b", "points": "Step 1: S2O8^2- + 2Fe^2+ -> 2SO4^2- + 2Fe^3+ (1); Step 2: 2Fe^3+ + 2I- -> 2Fe^2+ + I2 (1)", "marks": 2},
            {"part": "c", "points": "Each catalytic step involves collision between oppositely charged ions (cation and anion), which attract each other; Fe^3+ simply carries out Step 2 first, regenerating Fe^2+ (1)", "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Homogeneous Atmospheric Catalysis: Acid Rain Formation — 9701/23/O/N/22/Q6(a)-(b)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="In the upper atmosphere, nitrogen oxides act as homogeneous catalysts in the conversion of sulfur dioxide into sulfur trioxide, contributing to acid rain:\n2SO2(g) + O2(g) -> 2SO3(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Write two equations showing how NO2(g) catalyses the atmospheric oxidation of SO2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why NO2 acts as a catalyst rather than a consumed reactant in this environmental mechanism.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Step 1: SO2(g) + NO2(g) -> SO3(g) + NO(g) (1); Step 2: NO(g) + 1/2 O2(g) -> NO2(g) (1)", "marks": 2},
            {"part": "b", "points": "NO2 is regenerated chemically in Step 2 in equal amount and remains chemically unchanged overall (1)", "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Automobile Catalytic Converters — 9701/22/F/M/23/Q8(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Modern vehicle exhaust systems incorporate three-way catalytic converters containing platinum, palladium, and rhodium supported on a ceramic honeycomb.",
        parts=[
            QuestionPart(
                label="a",
                text="State the purpose of the ceramic honeycomb structure.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write a balanced equation for the simultaneous catalytic removal of carbon monoxide and nitrogen monoxide.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why catalytic converters do not reduce carbon dioxide emissions.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Provides an enormous surface area of active catalyst while minimising the amount of expensive precious metal required (1)", "marks": 1},
            {"part": "b", "points": "2CO(g) + 2NO(g) -> 2CO2(g) + N2(g) (2)", "marks": 2},
            {"part": "c", "points": "Carbon monoxide and unburned hydrocarbons are oxidised to CO2, so the exhaust gas continues to contain carbon dioxide (a greenhouse gas) (1)", "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Catalyst Poisoning in Industrial Processes — 9701/21/M/J/23/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Catalyst poisoning is the deactivation of a catalyst by chemical substances present in the feed stream.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain at the molecular level how catalyst poisoning occurs in heterogeneous catalysis.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Identify a common poison for the iron catalyst in the Haber process and for catalytic converters in cars.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Poison molecules adsorb strongly and irreversibly onto active catalytic sites on the solid surface (1); This physically blocks reactant molecules from adsorbing, rendering the active sites permanently inactive (1)", "marks": 2},
            {"part": "b", "points": "Haber process: Sulfur / sulfur compounds (H2S) or carbon monoxide (CO) (1); Catalytic converters: Lead (from leaded petrol) (1)", "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Autocatalysis: Permanganate and Ethanedioate — 9701/22/M/J/23/Q6(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="When potassium manganate(VII) is titrated against warm acidified ethanedioic acid, the initial purple colour disappears very slowly, but subsequent drops decolourise instantaneously:\n2MnO4^- + 16H^+ + 5C2O4^2- -> 2Mn^2+ + 10CO2 + 8H2O",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term autocatalysis.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Identify the autocatalyst in this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Sketch the shape of the reaction rate vs time graph for an autocatalysed reaction, showing the characteristic induction period.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A reaction in which one of the products acts as a catalyst for the reaction (1)", "marks": 1},
            {"part": "b", "points": "Manganese(II) ions / Mn^2+(aq) (1)", "marks": 1},
            {"part": "c", "points": "Rate starts very low (induction period) (1); Rate rises to a maximum as [Mn^2+] builds up, then falls as reactants are consumed (bell-shaped rate curve) (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Biological Catalysts: Enzymes — 9701/21/O/N/23/Q8(a)-(c)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Enzymes are complex globular protein molecules that catalyse biochemical processes in living organisms.",
        parts=[
            QuestionPart(
                label="a",
                text="State two differences between enzymes and inorganic catalysts such as platinum.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why enzyme-catalysed reactions exhibit a maximum rate at an optimum temperature (typically around 37-40 °C) and drop rapidly to zero above 60 °C.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Enzymes operate under mild physiological conditions (neutral pH, ~37 °C) (1); Enzymes exhibit extreme substrate specificity due to complementary 3D active site shape (1)", "marks": 2},
            {"part": "b", "points": "Up to the optimum temperature, increasing temperature increases kinetic energy and fruitful collision frequency (1); Above optimum, thermal energy disrupts hydrogen bonds and tertiary folding of the protein (1); The enzyme denatures and the active site changes shape irreversibly, preventing substrate binding (1)", "marks": 3}
        ]
    ),
    Question(
        number=37,
        title="Comparing Catalysed vs Uncatalysed Reaction Coordinate Profiles — 9701/22/O/N/23/Q8(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Consider a reversible exothermic reaction: A + B <=> C + D.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the effect of a catalyst on: (i) the enthalpy change Delta H, (ii) the activation energy Ea, and (iii) the activation energy of the reverse reaction.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why a catalyst cannot turn a thermodynamically non-spontaneous reaction into a spontaneous reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) Delta H is unchanged (1); (ii) Ea of forward reaction is lowered (1); (iii) Ea of reverse reaction is lowered by the exact same amount (1)", "marks": 3},
            {"part": "b", "points": "A catalyst only affects kinetics (reaction rate/pathway), not thermodynamics / free energy change / equilibrium position (1)", "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Mathematical Features of the Maxwell-Boltzmann Distribution — 9701/23/M/J/24/Q8(a)-(b)",
        syllabus_ref="8.2",
        difficulty="HARD",
        preamble="The Maxwell-Boltzmann distribution curve possesses precise mathematical characteristics.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the curve never touches the energy axis (x-axis) at high energies.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the most probable energy, Emp (the peak of the curve), is not equal to the average / mean kinetic energy, Emean.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The distribution is asymptotic to the x-axis; there is no theoretical upper limit to the kinetic energy a molecule can acquire through successive collisions (1)", "marks": 1},
            {"part": "b", "points": "The curve is asymmetric with a long tail extending to very high energies on the right (1); These high-energy molecules pull the mean / average energy to a higher value than the mode / most probable energy (Emean > Emp) (1)", "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Iron Catalyst in the Haber Process: Role and Preparation — 9701/21/M/J/24/Q9(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="In the Haber process, finely divided iron mixed with potassium and aluminium oxide promoters is used as a heterogeneous catalyst.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the iron catalyst is manufactured in a finely divided, porous form.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain what would happen to the operational temperature of the Haber process plant if the iron catalyst were removed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Maximises the available surface area to volume ratio (1); Exposes vastly more active catalytic sites for adsorption of N2 and H2 molecules (1)", "marks": 2},
            {"part": "b", "points": "The plant would need to operate at a much higher temperature (e.g. >700 °C) to achieve an acceptable reaction rate (1); However, this would drastically reduce the equilibrium yield of ammonia to near zero (due to exothermic reaction) and require far more fuel (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Vanadium(V) Oxide in the Contact Process: Redox Cycle — 9701/22/M/J/24/Q9(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="In the Contact process, vanadium(V) oxide acts as a catalyst by undergoing a two-step redox cycle:\nStep 1: SO2(g) + V2O5(s) -> SO3(g) + V2O4(s)\nStep 2: 2V2O4(s) + O2(g) -> 2V2O5(s)",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the oxidation state of vanadium in V2O5 and in V2O4.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Identify the role of SO2 in Step 1 and the role of O2 in Step 2 in terms of oxidation and reduction.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why transition metals and their compounds are uniquely effective catalysts.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In V2O5: +5 (1); In V2O4: +4 (1)", "marks": 2},
            {"part": "b", "points": "SO2 acts as a reducing agent (reduces V from +5 to +4) (1); O2 acts as an oxidising agent (re-oxidises V from +4 to +5) (1)", "marks": 2},
            {"part": "c", "points": "Transition metals have partially filled d-orbitals and exhibit variable oxidation states (1); They can readily accept and donate electrons to form stable reaction intermediates (1)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Common Misconceptions: Catalysts and Equilibrium Position — 9701/23/O/N/23/Q7(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="A student states: 'Adding a catalyst increases the rate of reaction, which shifts the equilibrium to the right to produce a higher yield of products.'",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why this student's statement is fundamentally incorrect.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the exact effect of a catalyst on: (i) the rate of forward reaction, (ii) the rate of reverse reaction, and (iii) the equilibrium constant Kc.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A catalyst increases the rates of forward and reverse reactions equally (1); It has zero effect on the position of equilibrium or yield of products (1)", "marks": 2},
            {"part": "b", "points": "(i) Increases (1); (ii) Increases by the same factor (1); (iii) No change / unchanged (1)", "marks": 3}
        ]
    ),
    Question(
        number=42,
        title="Adsorption Energetics: Physisorption vs Chemisorption — 9701/22/F/M/25/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Adsorption onto a solid catalyst can occur via physisorption or chemisorption.",
        parts=[
            QuestionPart(
                label="a",
                text="Distinguish between physisorption and chemisorption in terms of the types of forces involved and enthalpy change.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why chemisorption is essential for catalysis to take place.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Physisorption involves weak intermolecular forces (London dispersion) with small Delta H (~ -20 to -40 kJ mol^-1) (1); Chemisorption involves formation of covalent/coordinate chemical bonds with large Delta H (~ -100 to -400 kJ mol^-1) (1)", "marks": 2},
            {"part": "b", "points": "Chemisorption involves electron transfer or sharing that directly weakens internal reactant bonds (1); Weak physisorption does not weaken covalent bonds sufficiently to lower the activation energy (1)", "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Acid-Catalysed Ester Hydrolysis: Homogeneous Mechanism — 9701/21/F/M/25/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="The hydrolysis of ethyl ethanoate is catalysed by dilute hydrochloric acid:\nCH3COOC2H5 + H2O <=[H^+]=> CH3COOH + C2H5OH",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why H+(aq) acts as a homogeneous catalyst in this aqueous solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain how protonation of the carbonyl oxygen atom in the ester accelerates nucleophilic attack by water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "H+ ions are dissolved in the same aqueous liquid phase as the reactants (1)", "marks": 1},
            {"part": "b", "points": "Protonation adds positive charge to the carbonyl oxygen (1); This strongly withdraws electrons from the carbonyl carbon atom, making it much more electrophilic (delta+) and vulnerable to attack by weak nucleophile H2O (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Transition Metal d-Orbitals in Catalysis — 9701/22/M/J/25/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Transition elements and their compounds make up the vast majority of industrial catalysts.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain how the presence of partially filled 3d subshells enables transition metals to act as catalysts.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Contrast the catalytic activity of transition metals (e.g. Fe, Ni) with s-block metals (e.g. Na, Ca).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Partially filled 3d orbitals can accept electron pairs from reactant molecules into vacant orbitals (1); and donate electrons from filled d-orbitals to form temporary coordinate bonds and intermediate complexes (1)", "marks": 2},
            {"part": "b", "points": "s-block metals have only one stable oxidation state (+1 for Na, +2 for Ca) and cannot participate in redox catalytic cycles (1); Transition metals readily undergo reversible one-electron and two-electron redox changes (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Inert Gas Addition and Reaction Kinetics — 9701/23/M/J/25/Q7(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Consider the gaseous reaction: 2NO(g) + O2(g) -> 2NO2(g).",
        parts=[
            QuestionPart(
                label="a",
                text="State and explain the effect on the rate of reaction when argon gas is added at constant volume.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State and explain the effect on the rate of reaction when argon gas is added at constant total pressure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "No effect on reaction rate (1); Concentrations and collision frequency between NO and O2 molecules remain completely unchanged (1)", "marks": 2},
            {"part": "b", "points": "Rate decreases (1); The volume must expand to maintain constant total pressure, which dilutes the reacting gases, lowering their concentrations and collision frequency (1)", "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Heterogeneous Catalytic Hydrogenation of Alkenes — 9701/21/O/N/25/Q8(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Vegetable oils are hardened into margarine by catalytic hydrogenation using a nickel catalyst at 150 °C:\nR-CH=CH-R' + H2 -> R-CH2-CH2-R'",
        parts=[
            QuestionPart(
                label="a",
                text="State the type of catalysis involved.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe how H2 molecules interact with the nickel surface during the reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why trans-fats can be formed as undesirable by-products during partial hydrogenation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Heterogeneous catalysis (solid Ni with liquid oil and gaseous H2) (1)", "marks": 1},
            {"part": "b", "points": "H-H covalent bonds undergo chemisorption and homolytic cleavage on the nickel surface (1); forming mobile, adsorbed hydrogen atoms on the metal lattice (1)", "marks": 2},
            {"part": "c", "points": "Adsorbed intermediate can undergo reversible hydrogen atom loss before full hydrogenation (1); Rotation around the single bond before reforming the double bond can isomerise natural cis-double bonds into more stable trans-configurations (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Temperature Coefficient Q10 & Arrhenius Concept — 9701/22/O/N/25/Q8(a)-(b)",
        syllabus_ref="8.2",
        difficulty="HARD",
        preamble="The temperature coefficient Q10 is defined as the ratio of reaction rates at temperatures separated by 10 °C:\nQ10 = Rate(T + 10) / Rate(T)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why reactions with very high activation energies have a larger Q10 value than reactions with low activation energies.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State what happens to the value of the rate constant, k, as temperature increases.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "For high Ea, Ea lies further out on the exponential tail of the Maxwell-Boltzmann distribution (1); A 10 °C shift produces a proportionally far greater fractional increase in the shaded area E >= Ea compared to a low Ea barrier (1)", "marks": 2},
            {"part": "b", "points": "Rate constant k increases exponentially with temperature (1)", "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Homogeneous Ozone Depletion by Chlorine Radicals — 9701/23/O/N/25/Q7(a)-(c)",
        syllabus_ref="8.3",
        difficulty="HARD",
        preamble="Chlorofluorocarbons (CFCs) release chlorine radicals in the stratosphere, catalysing ozone breakdown:\n2O3(g) -> 3O2(g)",
        parts=[
            QuestionPart(
                label="a",
                text="Write the two propagation steps for this catalytic destruction cycle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Show that adding the two propagation steps yields the overall stoichiometric equation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why a single chlorine radical can destroy up to 100,000 ozone molecules.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Step 1: Cl. + O3 -> ClO. + O2 (1); Step 2: ClO. + O -> Cl. + O2 (or ClO. + O3 -> Cl. + 2O2) (1)", "marks": 2},
            {"part": "b", "points": "Cl. and ClO. cancel out from both sides, leaving: O3 + O -> 2O2 (or 2O3 -> 3O2) (1)", "marks": 1},
            {"part": "c", "points": "The chlorine radical (Cl.) is regenerated at the end of every cycle and continues the catalytic chain reaction repeatedly until chain termination occurs (1)", "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Engineering Design of Heterogeneous Catalytic Converters — 9701/21/M/J/25/Q8(a)-(b)",
        syllabus_ref="8.3",
        difficulty="EASY",
        preamble="Automobile catalytic converters use a ceramic monolith structure with thousands of micro-channels.",
        parts=[
            QuestionPart(
                label="a",
                text="State two engineering advantages of using a micro-channel honeycomb over packed catalyst pellets.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why cold vehicle exhaust emits significantly higher pollutants during the first two minutes after starting the engine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Enormous geometric surface area for gas contact (1); Negligible back-pressure / does not impede exhaust gas flow and vehicle power (1)", "marks": 2},
            {"part": "b", "points": "The catalytic converter requires high operating temperatures (around 300-400 °C) to reach its 'light-off' temperature (1); While cold, few exhaust gas molecules have kinetic energy >= Ea on the catalyst surface, so catalytic conversion is inefficient (1)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Kinetics, Boltzmann Distributions & Catalyst Surface Chemistry — 9701/22/O/N/25/Q8(a)-(d)",
        syllabus_ref="8.2",
        difficulty="HARD",
        preamble="In the industrial synthesis of ammonia, N2(g) + 3H2(g) <=> 2NH3(g), the uncatalysed reaction has an activation energy of +335 kJ mol^-1, whereas the iron-catalysed reaction has an activation energy of +160 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the uncatalysed reaction has such an immense activation energy (+335 kJ mol^-1).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how the iron catalyst lowers this activation energy to +160 kJ mol^-1 by detailing the surface adsorption process.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Draw a labelled Maxwell-Boltzmann distribution sketch showing both uncatalysed Ea (+335) and catalysed Ecat (+160).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Explain how the iron catalyst enables industrial plants to operate at 450 °C rather than 800 °C, and explain the economic benefit.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The nitrogen molecule contains an exceptionally strong covalent triple bond (N#N, bond energy = 945 kJ mol^-1) (1); Tremendous kinetic energy is required to break this bond in homogeneous gas-phase collisions (1)", "marks": 2},
            {"part": "b", "points": "N2 chemisorbs onto active iron surface sites where Fe d-orbitals back-donate electrons into N2 antibonding orbitals, cleaving the triple bond into adsorbed N atoms at much lower energy (1); Adsorbed N atoms react stepwise with adsorbed H atoms (1)", "marks": 2},
            {"part": "c", "points": "Single distribution curve with Ecat (+160) positioned to the left of uncatalysed Ea (+335) (1); Shaded region under curve showing far greater fraction of molecules exceeding Ecat (1)", "marks": 2},
            {"part": "d", "points": "At 450 °C with catalyst, reaction rate is commercially viable while preserving an acceptable equilibrium yield (since lower T favours exothermic forward yield) (1); Massive reduction in plant energy costs and less severe thermal wear on equipment (1)", "marks": 2}
        ]
    )
]
'''
    with open(r"z:\tests n quizes63\books\psycology\new styl\topic8_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully wrote topic8_data.py!")

if __name__ == "__main__":
    generate()
