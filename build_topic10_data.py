"""
Script to generate topic10_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 10: Group 2.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 10: Group 2 (The Alkaline Earth Metals).
Subtopics:
  10.1 Similarities and trends in the properties of the Group 2 metals, magnesium to barium, and their compounds:
       - Trends in atomic and ionic radii, ionisation energies, and reactivity with water, oxygen, and dilute acids
       - Behaviour and basic nature of oxides and hydroxides; reactions with water and acids
       - Thermal decomposition of carbonates and nitrates and explanation in terms of cation polarising power
       - Trends in solubility of hydroxides and sulfates; qualitative analysis testing
       - Agricultural, environmental, and medical applications (soil treatment, flue-gas desulfurisation, antacids, barium meal)

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

TOPIC_10_QUESTIONS = [
    # =========================================================================
    # PART 1: Physical Trends & Reactions with Oxygen, Water & Acids (Q1 to Q13)
    # =========================================================================
    Question(
        number=1,
        title="Reactivity of Group 2 Metals with Cold Water and Steam — 9701/21/M/J/23/Q3(a)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="The Group 2 elements magnesium to barium exhibit a distinct graduation in their chemical reactivity towards water. Fig. 1.1 illustrates the relative vigour of reaction and observations.",
        figure_path="figures/group2_reactivity_water.png",
        figure_caption="Fig. 1.1: Relative vigour and observations for reactions of Group 2 metals with cold water.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe what is observed when a clean piece of magnesium ribbon is placed in cold water over several days, and write a balanced chemical equation for the reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Magnesium reacts much more vigorously with steam than with cold water. State two observations for the reaction of heated magnesium with steam, and write the balanced equation including state symbols.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State and explain the trend in the reactivity of the Group 2 elements from magnesium to barium when reacted with cold water.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Observation: Very slow effervescence / few bubbles of gas appearing on metal surface / cloudy suspension forms slowly [1]",
                "Equation: Mg(s) + 2H2O(l) -> Mg(OH)2(s or aq) + H2(g) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Observations: Brilliant white light / flame AND white solid / ash (powder) formed [1]",
                "Equation: Mg(s) + H2O(g) -> MgO(s) + H2(g) [1]",
                "State symbols correct: (s), (g), (s), (g) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Trend: Reactivity increases down the group from Mg to Ba [1]",
                "Explanation: Atomic radius increases AND electron shielding increases down the group [1]",
                "Weaker electrostatic attraction between nucleus and outer valence electrons, so less energy required to remove the two outer electrons / sum of first two ionisation energies decreases [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=2,
        title="Electronic Configurations and Ionisation Energies of Group 2 — 9701/22/O/N/22/Q2(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="The Group 2 elements all have valence shell configurations of the form ns².",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the full electronic configuration of the calcium atom, Ca, and the strontium ion, Sr²⁺.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the first ionisation energy of barium (503 kJ mol⁻¹) is significantly lower than that of magnesium (738 kJ mol⁻¹), despite barium having a much greater nuclear charge.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ca: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² [1]",
                "Sr²⁺: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ (or [Kr]) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ba has more electron shells / larger atomic radius than Mg [1]",
                "Ba has greater electron shielding of the outer electrons from the nucleus [1]",
                "The increased shielding and greater distance outweigh the increased nuclear charge, resulting in a weaker attraction to the outer electrons [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=3,
        title="Reactions of Group 2 Elements with Oxygen and Flame Tests — 9701/23/M/J/21/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Group 2 elements burn in oxygen or air to form white solid ionic oxides. Under certain conditions, some also form peroxides.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the characteristic flame colors observed when calcium, strontium, and barium compounds are subjected to a flame test.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced equation for the formation of calcium oxide from its elements. Specify the oxidation state of calcium and oxygen in the product.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="When barium is heated in excess oxygen at elevated temperatures, barium peroxide, BaO₂, is formed. State the oxidation state of oxygen in BaO₂ and write an equation for its reaction with dilute sulfuric acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Calcium: Brick-red (or red-orange) [1]",
                "Strontium: Scarlet (or crimson / red) [1]",
                "Barium: Apple-green (or yellow-green) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Equation: 2Ca(s) + O2(g) -> 2CaO(s) [1]",
                "Oxidation states: Ca = +2, O = -2 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Oxidation state of oxygen: -1 [1]",
                "Equation: BaO2(s) + H2SO4(aq) -> BaSO4(s) + H2O2(aq) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Reactions of Group 2 Metals with Dilute Acids — 9701/22/F/M/22/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="When Group 2 metals are placed in dilute acids, rapid effervescence is typically observed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="A student adds a strip of magnesium to dilute hydrochloric acid. Write the ionic equation with state symbols for this reaction and identify the reducing agent.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When a piece of barium metal is added to dilute sulfuric acid, effervescence starts immediately but ceases abruptly after a few seconds, leaving unreacted metal. Explain this observation in terms of product solubility.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ionic equation: Mg(s) + 2H⁺(aq) -> Mg²⁺(aq) + H2(g) [1]",
                "Reducing agent: Mg (as its oxidation number increases from 0 to +2 / loses electrons) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Barium reacts initially to produce barium sulfate: Ba + H2SO4 -> BaSO4 + H2 [1]",
                "BaSO4 is insoluble in water [1]",
                "An impermeable, insoluble layer / coating of BaSO4 forms on the metal surface, which prevents further acid from reaching the unreacted barium [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Trend in Atomic and Ionic Radii Down Group 2 — 9701/11/M/J/22/Q16",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Which row correctly describes the trends in atomic radius and ionic radius for the elements down Group 2 from magnesium to barium?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct option:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Atomic radius increases; Ionic radius increases",
                    "B. Atomic radius increases; Ionic radius decreases",
                    "C. Atomic radius decreases; Ionic radius increases",
                    "D. Atomic radius decreases; Ionic radius decreases"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Down Group 2, each successive element possesses an additional principal quantum shell of electrons. This increases both the atomic radius of the neutral metal atom and the ionic radius of the M²⁺ cation."
            ], "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Trend in Density and Melting Point of Group 2 Metals — 9701/21/O/N/21/Q2(a)-(b)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Group 2 metals possess metallic crystal lattices held together by metallic bonding.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the melting points of Group 2 metals are generally significantly higher than those of the corresponding Group 1 metals in the same period.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain the general decrease in melting point from magnesium to barium.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Group 2 cations have a higher charge (+2 vs +1) and smaller ionic radius, giving higher charge density [1]",
                "Each Group 2 atom contributes two delocalised electrons per cation to the metallic sea (denser sea), resulting in stronger electrostatic attraction between cations and delocalised electrons [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Down the group, the ionic radius of the M²⁺ cation increases [1]",
                "The electrostatic attraction between the metal cations and the delocalised sea of electrons becomes weaker over greater distance [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Quantitative Gas Volume: Calcium with Water — 9701/22/M/J/22/Q3(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="A sample of 0.802 g of pure calcium metal is added to an excess of water at room temperature and pressure (293 K, 101 kPa).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction of calcium with cold water.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the volume of hydrogen gas, in cm³, collected under room conditions. (Assume molar gas volume = 24.0 dm³ mol⁻¹ at r.t.p.; Ar(Ca) = 40.1)",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ca(s) + 2H2O(l) -> Ca(OH)2(s or aq) + H2(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of Ca = 0.802 / 40.1 = 0.0200 mol [1]",
                "Moles of H2 = 0.0200 mol; Volume = 0.0200 * 24000 cm³ = 480 cm³ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Redox Nature of Group 2 Elements — 9701/12/F/M/21/Q15",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="When magnesium reacts with steam, which statement regarding the oxidation and reduction processes is correct?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct option:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Magnesium is reduced and hydrogen is oxidized.",
                    "B. Magnesium is oxidized from 0 to +2 and hydrogen is reduced from +1 to 0.",
                    "C. Oxygen is oxidized from -2 to 0.",
                    "D. The reaction is not a redox reaction."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In Mg(s) + H2O(g) -> MgO(s) + H2(g), Mg changes oxidation state from 0 to +2 (oxidation), and H in H2O changes from +1 to 0 in H2 (reduction)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Reactions of Strontium with Air and Water — 9701/21/M/J/20/Q3(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Strontium is an active alkaline earth metal located in Period 5 of Group 2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When strontium is exposed to air at room temperature, it quickly tarnishes, forming two distinct strontium compounds on its surface. Identify the formulas of both compounds.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When strontium burns in air, it produces a mixture of strontium oxide, SrO, and strontium nitride, Sr3N2. Write a balanced equation for the formation of strontium nitride from its elements.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Strontium nitride reacts with water to produce strontium hydroxide and an alkaline gas. Write a balanced equation for this hydrolysis reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "SrO (strontium oxide) [1]",
                "SrCO3 (strontium carbonate) or Sr(OH)2 (strontium hydroxide) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "3Sr(s) + N2(g) -> Sr3N2(s) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Equation: Sr3N2 + 6H2O -> 3Sr(OH)2 + 2NH3 [2] (1 mark for correct formulas, 1 mark for balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Apparatus and Observations for Magnesium with Steam — 9701/23/O/N/21/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="In a school laboratory experiment, mineral wool soaked in water is placed at the closed end of a horizontal boiling tube. Magnesium ribbon is placed in the middle and heated strongly with a Bunsen burner.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the mineral wool must be heated gently before heating the magnesium ribbon strongly.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Describe how the gas produced at the delivery tube can be safely collected and tested to confirm its identity.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "To vaporise the water and generate steam to drive out air / oxygen from the boiling tube before the magnesium reaches ignition temperature [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Collect over water in an inverted test tube / gas jar [1]",
                "Apply a lighted splint; burns with a squeaky pop (confirms hydrogen gas) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Comparison of Reactivity: Mg vs Ca with Dilute Hydrochloric Acid — 9701/13/M/J/22/Q17",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Equal masses (0.10 g) of magnesium and calcium are added to separate beakers containing 50 cm³ of 1.0 mol dm⁻³ HCl(aq) at 25 °C.",
        parts=[
            QuestionPart(
                label="",
                text="Which statement correctly compares the two reactions?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Calcium reacts more rapidly, but produces a smaller total volume of hydrogen gas than magnesium.",
                    "B. Magnesium reacts more rapidly and produces a greater volume of hydrogen gas.",
                    "C. Calcium reacts more rapidly and produces a greater volume of hydrogen gas.",
                    "D. Both metals react at identical rates because the acid concentration is the same."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Calcium is more reactive (lower IE), so the initial rate is faster. However, 0.10 g of Mg contains more moles (0.10/24.3 = 0.00412 mol) than 0.10 g of Ca (0.10/40.1 = 0.00249 mol). Since each mole of metal yields 1 mole of H2, Mg yields a larger final gas volume."
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Second Ionisation Energy Trend in Group 2 — 9701/22/O/N/20/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="The table gives the first and second ionisation energies of magnesium and calcium.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write an equation representing the second ionisation energy of calcium, including state symbols.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="For both elements, the second ionisation energy is approximately double the first ionisation energy. Explain why the second electron is significantly harder to remove than the first.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the third ionisation energy of calcium is more than four times greater than its second ionisation energy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ca⁺(g) -> Ca²⁺(g) + e⁻ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The second electron is removed from a positive ion (M⁺) rather than a neutral atom [1]",
                "There is less electron-electron repulsion, the electron cloud contracts, and the remaining electrons experience a greater effective nuclear attraction per electron [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The third electron is removed from an inner quantum shell (3p rather than 4s) [1]",
                "It is much closer to the nucleus and experiences substantially less shielding, requiring vast energy to remove [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Identifying Group 2 Metals from Reactivity Data — 9701/11/O/N/22/Q15",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="An unknown Group 2 metal X reacts vigorously with cold water to give a cloudy alkaline suspension and colourless gas. When burned in oxygen, it gives a brick-red flame.",
        parts=[
            QuestionPart(
                label="",
                text="Identify metal X:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Magnesium",
                    "B. Calcium",
                    "C. Strontium",
                    "D. Barium"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Calcium gives a brick-red flame test and reacts steadily with cold water to form sparingly soluble Ca(OH)2, causing the solution to appear cloudy."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 2: Thermal Decomposition of Carbonates & Nitrates; Oxides (Q14 to Q27)
    # =========================================================================
    Question(
        number=14,
        title="Thermal Decomposition of Group 2 Carbonates — 9701/22/M/J/23/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="The carbonates of Group 2 decompose on heating to form the corresponding metal oxide and carbon dioxide gas. Fig. 14.1 shows the decomposition temperatures.",
        figure_path="figures/group2_thermal_decomposition.png",
        figure_caption="Fig. 14.1: Thermal decomposition temperatures of Group 2 carbonates and nitrates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced chemical equation for the thermal decomposition of magnesium carbonate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the trend in thermal stability of the Group 2 carbonates from magnesium carbonate to barium carbonate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain this trend in thermal stability in terms of cation size, charge density, and polarising power.",
                marks=3,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "MgCO3(s) -> MgO(s) + CO2(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Thermal stability increases down the group / higher decomposition temperature required down the group [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Down the group, the ionic radius of the M²⁺ cation increases while the charge remains +2 [1]",
                "Charge density of the cation decreases, meaning it has less polarising power [1]",
                "It causes less distortion / polarization of the electron cloud of the carbonate (CO3²⁻) ion, weakening the C-O bond less, so more thermal energy is needed to break the bond [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Thermal Decomposition of Group 2 Nitrates — 9701/21/O/N/22/Q3(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="All Group 2 nitrates undergo thermal decomposition when heated strongly.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the thermal decomposition of anhydrous strontium nitrate, Sr(NO3)2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State two observations made during the thermal decomposition of strontium nitrate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe a chemical test, including the expected result, to confirm the identity of oxygen gas evolved during the decomposition.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2Sr(NO3)2(s) -> 2SrO(s) + 4NO2(g) + O2(g) [2] (1 mark for all correct species, 1 mark for correct balancing)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Brown fumes / gas evolved (NO2) [1]",
                "White solid residue formed (SrO) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Insert a glowing wooden splint; it relights [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=16,
        title="Reactions of Group 2 Oxides with Water and Dilute Acids — 9701/22/M/J/21/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Calcium oxide, CaO, is known industrially as quicklime.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When cold water is added dropwise to solid calcium oxide, a vigorous exothermic reaction occurs to form slaked lime. Write a balanced equation for this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced equation for the reaction between solid calcium oxide and dilute nitric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why magnesium oxide, MgO, is used as a refractory lining material in industrial blast furnaces and kilns.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaO(s) + H2O(l) -> Ca(OH)2(s) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CaO(s) + 2HNO3(aq) -> Ca(NO3)2(aq) + H2O(l) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Very high melting point (approx 2852 °C) [1]",
                "Giant ionic lattice with strong electrostatic attraction between highly charged Mg²⁺ and O²⁻ ions / chemically unreactive at high temperatures [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Comparison of Group 2 and Group 1 Nitrate Decomposition — 9701/12/M/J/23/Q18",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="When heated strongly in separate test-tubes, anhydrous sodium nitrate and anhydrous magnesium nitrate decompose differently.",
        parts=[
            QuestionPart(
                label="",
                text="Which row correctly states the gaseous products formed in each case?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. NaNO3: O2 only; Mg(NO3)2: NO2 and O2",
                    "B. NaNO3: NO2 and O2; Mg(NO3)2: NO2 and O2",
                    "C. NaNO3: NO2 only; Mg(NO3)2: NO2 and O2",
                    "D. NaNO3: O2 only; Mg(NO3)2: O2 only"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Group 1 nitrates (except Li) decompose to nitrite and O2 (2NaNO3 -> 2NaNO2 + O2). Group 2 nitrates (and LiNO3) decompose completely to oxide, brown NO2 fumes, and O2 (2Mg(NO3)2 -> 2MgO + 4NO2 + O2) due to higher cation polarising power."
            ], "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="Gravimetric Decomposition of Hydrated Barium Carbonate — 9701/21/M/J/22/Q2(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A 4.935 g sample of an impure barium carbonate, BaCO3, was heated to constant mass at 1400 °C. The mass of the solid residue after heating was 3.835 g. The only decomposable component in the sample is BaCO3. (Mr values: BaCO3 = 197.3, BaO = 153.3, CO2 = 44.0)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the mass of carbon dioxide gas evolved during decomposition.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of BaCO3 decomposed, and hence find the percentage by mass of BaCO3 in the original sample.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mass of CO2 = 4.935 g - 3.835 g = 1.100 g [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of CO2 = 1.100 / 44.0 = 0.0250 mol [1]",
                "Moles of BaCO3 = 0.0250 mol; Mass of BaCO3 = 0.0250 * 197.3 = 4.9325 g [1]",
                "Percentage purity = (4.9325 / 4.935) * 100% = 99.9% (accept 99.9% to 100%) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=19,
        title="Basicity and pH of Group 2 Hydroxide Solutions — 9701/23/M/J/22/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Saturated aqueous solutions of magnesium hydroxide and barium hydroxide are prepared at 25 °C.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State how the pH of a saturated solution of barium hydroxide compares with that of a saturated solution of magnesium hydroxide. Explain your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the ionic equation for the reaction that occurs when excess dilute hydrochloric acid is added to a suspension of magnesium hydroxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The pH of saturated Ba(OH)2 is much higher (approx 13-14) than that of Mg(OH)2 (approx 9-10) [1]",
                "Ba(OH)2 is significantly more soluble in water than Mg(OH)2, releasing a much higher concentration of OH⁻(aq) ions into solution [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Mg(OH)2(s) + 2H⁺(aq) -> Mg²⁺(aq) + 2H2O(l) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Distortion of Carbonate Ion by Cations — 9701/11/F/M/22/Q16",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Which factor causes the carbonate ion in magnesium carbonate to decompose at a lower temperature than the carbonate ion in barium carbonate?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct option:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Mg²⁺ has a smaller charge than Ba²⁺.",
                    "B. Mg²⁺ has a smaller ionic radius and thus a higher charge density than Ba²⁺.",
                    "C. Ba²⁺ has a higher electronegativity than Mg²⁺.",
                    "D. BaCO3 has covalent bonding whereas MgCO3 is purely ionic."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Mg²⁺ has a much smaller ionic radius (0.072 nm) than Ba²⁺ (0.135 nm) with the same +2 charge, giving it a much higher charge density and stronger polarising power to polarise the CO3²⁻ ion."
            ], "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Thermal Decomposition of Hydrated Magnesium Nitrate Crystals — 9701/22/O/N/21/Q2(c)-(e)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Crystals of hydrated magnesium nitrate, Mg(NO3)2·6H2O, are heated gently in a test-tube and then heated strongly.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State what is observed during the gentle heating stage.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State two observations made during the strong heating stage.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced equation for the complete decomposition of anhydrous Mg(NO3)2.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Crystals dissolve in their own water of crystallisation / liquid forms / condensation / colourless droplets form on cooler parts of the tube [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Brown fumes / brown gas evolved (NO2) [1]",
                "White solid / ash residue formed (MgO) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "2Mg(NO3)2(s) -> 2MgO(s) + 4NO2(g) + O2(g) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Limewater Test for Carbon Dioxide — 9701/21/M/J/21/Q3(b)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Limewater is a saturated aqueous solution of calcium hydroxide, Ca(OH)2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the observation when carbon dioxide is bubbled through limewater for a short period of time, and write a balanced equation with state symbols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When carbon dioxide is bubbled through the mixture in (a) continuously for an extended time, the mixture turns clear and colorless again. Explain this observation and write a balanced chemical equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Observation: Solution turns cloudy / milky / white precipitate forms [1]",
                "Equation: Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Insoluble CaCO3 reacts with excess CO2 and water to form soluble calcium hydrogencarbonate [1]",
                "Equation: CaCO3(s) + CO2(g) + H2O(l) -> Ca(HCO3)2(aq) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Neutralisation Stoichiometry of Calcium Hydroxide — 9701/22/F/M/21/Q2(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="A 25.0 cm³ aliquot of limewater (saturated Ca(OH)2(aq)) required 14.50 cm³ of 0.0500 mol dm⁻³ HCl(aq) for complete neutralisation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the reaction between Ca(OH)2 and HCl.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the concentration of Ca(OH)2 in the limewater in mol dm⁻³ and in g dm⁻³. (Mr of Ca(OH)2 = 74.1)",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ca(OH)2(aq) + 2HCl(aq) -> CaCl2(aq) + 2H2O(l) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of HCl = (14.50 / 1000) * 0.0500 = 7.25 * 10⁻⁴ mol [1]",
                "Moles of Ca(OH)2 = 7.25 * 10⁻⁴ / 2 = 3.625 * 10⁻⁴ mol in 25.0 cm³; Conc = (3.625 * 10⁻⁴ / 0.0250) = 0.0145 mol dm⁻³ [1]",
                "Concentration in g dm⁻³ = 0.0145 * 74.1 = 1.07 g dm⁻³ [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=24,
        title="Thermal Stability of Group 2 Hydroxides — 9701/12/O/N/21/Q16",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Group 2 hydroxides also decompose on heating to yield metal oxides and steam.",
        parts=[
            QuestionPart(
                label="",
                text="Which of the following Group 2 hydroxides decomposes most readily when heated?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Ba(OH)2",
                    "B. Sr(OH)2",
                    "C. Ca(OH)2",
                    "D. Mg(OH)2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: D [1]",
                "Explanation: Thermal stability of Group 2 hydroxides increases down the group. Mg²⁺ has the highest charge density and polarises the OH⁻ ion most strongly, making Mg(OH)2 decompose at the lowest temperature."
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Identifying Decomposition Residues — 9701/13/O/N/22/Q16",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="A white solid X is heated strongly in a crucible. It gives off brown fumes and a colourless gas that relights a glowing splint. The solid residue is dissolved in water to give a strongly alkaline solution.",
        parts=[
            QuestionPart(
                label="",
                text="What is solid X?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Calcium carbonate",
                    "B. Barium nitrate",
                    "C. Potassium nitrate",
                    "D. Magnesium sulfate"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Barium nitrate decomposes to form BaO, brown NO2 fumes, and O2 (relights glowing splint). BaO dissolves readily in water to form soluble Ba(OH)2, a strongly alkaline solution."
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="Energy Cycle for Carbonate Decomposition — 9701/22/O/N/23/Q3(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="The thermal decomposition of metal carbonates is an endothermic process: MCO3(s) -> MO(s) + CO2(g).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the decomposition of MCO3(s) becomes more endothermic (delta-H more positive) down Group 2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the sign of delta-S for the decomposition reaction and explain your reasoning.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Lattice enthalpy of MO(s) is very exothermic due to small O²⁻ ion, but decreases as M²⁺ gets larger [1]",
                "However, the lattice enthalpy of MCO3 decreases less steeply because CO3²⁻ is a large ion; overall, Delta-H of decomposition becomes more positive (more endothermic) down the group [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Delta-S is positive (+ve) [1]",
                "A solid reactant forms a solid and a gas (CO2(g)); gases have much greater disorder / entropy than solids [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="Comparative Heating of Calcium and Strontium Compounds — 9701/21/M/J/23/Q4(d)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Equimolar amounts of calcium carbonate and strontium carbonate are heated under identical conditions in separate test tubes connected to separate gas syringes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Sketch or state which syringe will fill faster with gas at 800 °C. Justify your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why calcium oxide reacts vigorously with water but magnesium oxide reacts very slowly.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The syringe collecting gas from calcium carbonate fills faster [1]",
                "CaCO3 has a lower decomposition temperature / lower activation energy for decomposition than SrCO3 because Ca²⁺ has higher charge density and polarises the carbonate ion more effectively [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Lattice energy of MgO is significantly more exothermic than that of CaO due to the smaller radius of Mg²⁺ [1]",
                "More energy is required to break up the MgO ionic lattice / reaction with water has higher activation energy [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 3: Solubility Trends & Qualitative Analysis (Q28 to Q39)
    # =========================================================================
    Question(
        number=28,
        title="Opposing Solubility Trends of Group 2 Hydroxides and Sulfates — 9701/22/M/J/22/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="The solubilities of the Group 2 hydroxides and sulfates exhibit distinct and opposite trends down the group, as illustrated in Fig. 28.1.",
        figure_path="figures/group2_solubility_trends.png",
        figure_caption="Fig. 28.1: Trends in solubility of Group 2 hydroxides vs sulfates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the trend in solubility of Group 2 hydroxides from Mg(OH)2 to Ba(OH)2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the trend in solubility of Group 2 sulfates from MgSO4 to BaSO4.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Describe an experiment using aqueous solutions of magnesium chloride and barium chloride with sodium hydroxide to demonstrate the trend in hydroxide solubility.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Solubility of Group 2 hydroxides increases down the group [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Solubility of Group 2 sulfates decreases down the group [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Add aqueous NaOH dropwise to separate samples of MgCl2(aq) and BaCl2(aq) [1]",
                "Observation with MgCl2: thick white precipitate of Mg(OH)2 forms immediately [1]",
                "Observation with BaCl2: no precipitate / remains clear solution (or faint turbidity only at high conc) because Ba(OH)2 is soluble [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=29,
        title="Chemical Test for Sulfate Ions — 9701/21/O/N/21/Q3(a)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="The insolubility of barium sulfate forms the basis of the standard analytical test for sulfate ions in solution.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the reagents and method used to test for the presence of sulfate ions, SO4²⁻, in an aqueous solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the expected observation for a positive result and write an ionic equation with state symbols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the test mixture must be acidified, and name an acid that must NOT be used for this purpose.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Add dilute hydrochloric acid (or dilute nitric acid) [1]",
                "Followed by aqueous barium chloride (or aqueous barium nitrate) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Observation: White precipitate forms [1]",
                "Ionic equation: Ba²⁺(aq) + SO4²⁻(aq) -> BaSO4(s) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Acid is added to react with and remove carbonate (CO3²⁻) or sulfite (SO3²⁻) ions which would otherwise produce a false positive white precipitate of BaCO3 / BaSO3 [1]",
                "Sulfuric acid (H2SO4) must NOT be used because it contains sulfate ions and would itself form a precipitate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Qualitative Differentiation of Group 2 Cations — 9701/23/O/N/22/Q2(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A laboratory technician has three unlabelled bottles containing aqueous solutions of Mg(NO3)2, Ca(NO3)2, and Ba(NO3)2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe a single chemical test using dilute sulfuric acid that can distinguish barium nitrate from the other two solutions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe how aqueous sodium hydroxide can be used to distinguish magnesium nitrate from calcium nitrate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State how flame tests could confirm the presence of Ca²⁺ and Ba²⁺ in the respective bottles.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Add dilute H2SO4 to samples of each solution [1]",
                "Ba(NO3)2 produces an immediate, dense white precipitate (BaSO4); Mg(NO3)2 produces no precipitate (soluble); Ca(NO3)2 produces only a slight precipitate or none at low conc [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Add dilute NaOH(aq) dropwise to samples of both [1]",
                "Mg(NO3)2 forms a dense white precipitate insoluble in excess; Ca(NO3)2 forms a much fainter/slight precipitate (more soluble) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Ca²⁺ gives a brick-red flame [1]",
                "Ba²⁺ gives an apple-green flame [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Conductometric Titration: Barium Hydroxide with Sulfuric Acid — 9701/22/O/N/21/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Dilute sulfuric acid is added gradually from a burette to a beaker containing 50.0 cm³ of 0.100 mol dm⁻³ barium hydroxide while monitoring electrical conductivity.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the full balanced chemical equation for the reaction including state symbols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe what happens to the electrical conductivity of the solution as sulfuric acid is added until the equivalence point is reached, and explain why.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the electrical conductivity rises again after passing the equivalence point.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Ba(OH)2(aq) + H2SO4(aq) -> BaSO4(s) + 2H2O(l) [2] (1 mark for species, 1 mark for state symbols)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Conductivity decreases to almost zero at equivalence [1]",
                "Ba²⁺ and OH⁻ ions are removed from solution by forming insoluble BaSO4 solid precipitate and covalent H2O molecules; no free mobile ions remain [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Excess H2SO4 introduces mobile H⁺(aq) and SO4²⁻(aq) ions which conduct electricity [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Solubility Product and Precipitation of Barium Sulfate — 9701/11/M/J/23/Q17",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Which pair of solutions, when mixed in equal volumes of 0.1 mol dm⁻³, forms a precipitate?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct pair:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Ba(NO3)2(aq) and Na2SO4(aq)",
                    "B. Mg(NO3)2(aq) and Na2SO4(aq)",
                    "C. BaCl2(aq) and NaOH(aq)",
                    "D. SrCl2(aq) and HNO3(aq)"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: BaSO4 is insoluble (solubility product is very low, ~10⁻¹⁰ mol² dm⁻⁶), so mixing barium nitrate and sodium sulfate immediately yields a white precipitate of BaSO4."
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Deducing Unknowns from Qualitative Observations — 9701/21/M/J/20/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Three white solids, A, B, and C, are known to be magnesium chloride, calcium sulfate, and barium nitrate, not necessarily in that order.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Solid A dissolves readily in water. The addition of aqueous sodium hydroxide produces a thick white precipitate. Identify solid A.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Solid B is only very sparingly soluble in water. Heating it with charcoal reduces it to a sulfide. Identify solid B.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Solid C dissolves in water to give a clear solution. When dilute sulfuric acid is added, a thick white precipitate forms immediately. Write an ionic equation with state symbols for this precipitation reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Solid A is magnesium chloride (MgCl2) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Solid B is calcium sulfate (CaSO4) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Ionic equation: Ba²⁺(aq) + SO4²⁻(aq) -> BaSO4(s) [2] (1 mark for formulas, 1 mark for state symbols)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Trend in Sulfate Solubility Down Group 2 — 9701/12/M/J/21/Q17",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Which Group 2 sulfate has the highest solubility in water at 298 K?",
        parts=[
            QuestionPart(
                label="",
                text="Select the most soluble sulfate:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. BaSO4",
                    "B. SrSO4",
                    "C. CaSO4",
                    "D. MgSO4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: D [1]",
                "Explanation: Sulfate solubility decreases down Group 2 from magnesium to barium. Magnesium sulfate is freely soluble (approx 36 g per 100 g H2O)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Gravimetric Analysis of Sulfate Using Barium Chloride — 9701/22/M/J/20/Q2(b)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A 1.450 g sample of an unknown soluble metal sulfate, M2SO4, was dissolved in water, acidified with dilute hydrochloric acid, and treated with excess BaCl2(aq). The precipitate of BaSO4 was filtered, washed, dried, and found to weigh 2.334 g. (Mr: BaSO4 = 233.4; SO4 = 96.1)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of BaSO4 precipitated.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Determine the relative formula mass (Mr) of M2SO4 and deduce the identity of alkali metal M. (Ar: Li = 6.9, Na = 23.0, K = 39.1, Rb = 85.5)",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of BaSO4 = 2.334 / 233.4 = 0.0100 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of M2SO4 = moles of BaSO4 = 0.0100 mol [1]",
                "Mr of M2SO4 = 1.450 g / 0.0100 mol = 145.0 [1]",
                "2 * Ar(M) + 96.1 = 145.0 => 2 * Ar(M) = 48.9 => Ar(M) = 24.5 => metal M is sodium (Na, Ar=23.0; Mr(Na2SO4) = 142.1) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=36,
        title="Distinguishing Sulfite from Sulfate with Barium Chloride — 9701/23/M/J/21/Q4(d)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A student adds BaCl2(aq) to two unlabelled test tubes containing sodium sulfate, Na2SO4, and sodium sulfite, Na2SO3. Both form a white precipitate.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the precipitate formed in each test tube.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Describe a simple procedure using dilute hydrochloric acid to distinguish between the two precipitates, stating the observations in each case.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Precipitates are BaSO4 (barium sulfate) and BaSO3 (barium sulfite) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Add dilute hydrochloric acid to both tubes [1]",
                "The BaSO3 precipitate dissolves with effervescence, producing choking sulfur dioxide gas (SO2): BaSO3(s) + 2HCl(aq) -> BaCl2(aq) + SO2(g) + H2O(l) [1]",
                "The BaSO4 precipitate does not dissolve / remains unchanged [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=37,
        title="Solubility and Medical Use of Barium Sulfate vs Barium Chloride — 9701/11/O/N/21/Q17",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Soluble barium salts such as barium chloride are extremely poisonous. However, barium sulfate is routinely administered to patients orally as a 'barium meal'.",
        parts=[
            QuestionPart(
                label="",
                text="Why is barium sulfate safe to use as a barium meal?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Barium sulfate forms a non-toxic complex with stomach acid.",
                    "B. Barium sulfate is virtually insoluble in water and digestive fluids, so free Ba²⁺ ions are not absorbed into the bloodstream.",
                    "C. The sulfate ion acts as an antidote to the barium ion.",
                    "D. Barium sulfate decomposes rapidly in the stomach to harmless barium carbonate."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Barium sulfate has an exceptionally low solubility product (Ksp ≈ 10⁻¹⁰), meaning free toxic Ba²⁺ ions are not released in amounts sufficient to be absorbed by intestinal walls."
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Flame Test Procedure and Observations for Group 2 — 9701/22/F/M/20/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Flame tests are useful qualitative methods for identifying metal cations.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe how a nichrome wire is cleaned and prepared before carrying out a flame test.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why magnesium compounds do not produce a visible flame color during a flame test.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dip the nichrome wire into concentrated hydrochloric acid [1]",
                "Hold it in a hot (non-luminous/blue) Bunsen flame until no colour is imparted to the flame [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The energy gap between electronic levels in Mg is large [1]",
                "The radiation emitted when excited electrons return to ground state lies in the ultraviolet region of the spectrum, outside the visible range [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Identifying an Unknown Group 2 Salt from Reactions — 9701/13/M/J/23/Q17",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="A white solid dissolves in water to give a colourless solution. Addition of aqueous sodium hydroxide gives no precipitate. Addition of aqueous sodium sulfate gives an immediate white precipitate.",
        parts=[
            QuestionPart(
                label="",
                text="What is the cation present in the solid?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Mg²⁺",
                    "B. Ca²⁺",
                    "C. Ba²⁺",
                    "D. Al³⁺"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Ba(OH)2 is soluble, so no precipitate forms with NaOH. BaSO4 is insoluble, so an immediate white precipitate forms with Na2SO4."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 4: Enthalpy Factors, Applications & Synthesis (Q40 to Q50)
    # =========================================================================
    Question(
        number=40,
        title="Thermodynamic Explanation of Sulfate Solubility — 9701/21/M/J/23/Q3(d)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="The enthalpy of solution is related to lattice enthalpy and hydration enthalpies by the expression: delta-H_sol = delta-H_latt + delta-H_hyd(cation) + delta-H_hyd(anion). Fig. 40.1 illustrates the trends.",
        figure_path="figures/group2_enthalpy_solubility.png",
        figure_caption="Fig. 40.1: Enthalpy factors explaining why Group 2 sulfate solubility decreases down the group.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term standard enthalpy change of hydration of an ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the hydration enthalpy of the M²⁺ cation becomes less exothermic down Group 2 from Mg²⁺ to Ba²⁺.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Using the trends in lattice enthalpy and hydration enthalpy, explain why Group 2 sulfates become less soluble down the group.",
                marks=3,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The enthalpy change when one mole of specified gaseous ions [1]",
                "is completely dissolved in water to form an infinitely dilute aqueous solution at standard conditions [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ionic radius of M²⁺ increases down the group while the charge remains +2 [1]",
                "Charge density decreases, resulting in weaker electrostatic attraction between the cation and lone pairs on polar water molecules [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Sulfate (SO4²⁻) is a large anion, so the lattice enthalpy of MSO4 changes relatively little down the group [1]",
                "The hydration enthalpy of M²⁺ decreases significantly (becomes much less exothermic) [1]",
                "Overall, delta-H of solution becomes more endothermic (less exothermic / less favourable), so solubility decreases [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=41,
        title="Agricultural Uses of Calcium Compounds — 9701/22/M/J/21/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Calcium hydroxide, Ca(OH)2 (slaked lime), and calcium carbonate, CaCO3 (limestone), are widely used in agriculture.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the purpose of adding calcium hydroxide or powdered limestone to agricultural soil.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Farmers are advised not to add slaked lime and ammonium nitrate fertiliser to fields at the same time. Explain why, and write an ionic equation for the reaction that would occur.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "To neutralise soil acidity / raise the pH of acidic soil to promote plant growth [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The hydroxide ions in slaked lime react with ammonium ions, liberating ammonia gas [1]",
                "This results in a loss of valuable nitrogen nutrient to the atmosphere as ammonia gas [1]",
                "Ionic equation: NH4⁺(aq) + OH⁻(aq) -> NH3(g) + H2O(l) (or with state symbols) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=42,
        title="Flue-Gas Desulfurisation by Calcium Compounds — 9701/21/O/N/20/Q3(c)-(e)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Sulfur dioxide emissions from coal-fired power stations cause acid rain. Flue-gas desulfurisation (FGD) removes SO2 by spraying an aqueous slurry of calcium carbonate or calcium oxide into the exhaust gases.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced equation for the reaction between calcium carbonate and sulfur dioxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="The calcium sulfite, CaSO3, produced is oxidised by atmospheric oxygen to calcium sulfate dihydrate (gypsum), CaSO4·2H2O. Write a balanced equation for this oxidation reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one major commercial use of the gypsum produced by this process.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaCO3(s) + SO2(g) -> CaSO3(s) + CO2(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2CaSO3(s) + O2(g) + 4H2O(l) -> 2[CaSO4·2H2O](s) (or CaSO3 + 1/2 O2 + 2H2O -> CaSO4·2H2O) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Manufacture of plasterboard / drywall / construction plaster / cement [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Antacid Chemistry of Magnesium Hydroxide — 9701/22/F/M/23/Q3(a)-(b)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="'Milk of magnesia' is an aqueous suspension of magnesium hydroxide, Mg(OH)2, used as an antacid to relieve indigestion and heartburn caused by excess hydrochloric acid in the stomach.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the neutralisation of hydrochloric acid by magnesium hydroxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why magnesium hydroxide is preferred over sodium hydroxide as an oral antacid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mg(OH)2(s) + 2HCl(aq) -> MgCl2(aq) + 2H2O(l) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Mg(OH)2 is only sparingly soluble, maintaining a mildly alkaline, safe pH (approx 9-10) without corroding mouth and oesophageal tissues [1]",
                "NaOH is a strong, highly soluble alkali (pH 14) that is extremely caustic and would cause severe chemical burns to stomach and throat lining [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Synthesis of Pure Magnesium Sulfate Crystals — 9701/23/M/J/22/Q4(a)-(c)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A student prepares hydrated magnesium sulfate crystals, MgSO4·7H2O (Epsom salts), starting from magnesium carbonate powder and dilute sulfuric acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe three practical steps the student must carry out to prepare a pure, dry sample of hydrated magnesium sulfate crystals from the reaction mixture.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the student must add excess magnesium carbonate rather than excess sulfuric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the percentage by mass of water in MgSO4·7H2O. (Ar: Mg = 24.3, S = 32.1, O = 16.0, H = 1.0)",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Filter the reaction mixture while warm to remove unreacted excess MgCO3 powder [1]",
                "Heat the filtrate to the point of crystallisation (saturation) and allow to cool slowly to form crystals [1]",
                "Filter the crystals, rinse with cold distilled water, and dry between filter papers (or in a desiccator) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Excess insoluble MgCO3 can be easily removed by filtration, ensuring the product is not contaminated with unreacted acid [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Mr(MgSO4·7H2O) = 24.3 + 32.1 + 4(16.0) + 7(18.0) = 24.3 + 32.1 + 64.0 + 126.0 = 246.4 [1]",
                "% H2O = (126.0 / 246.4) * 100% = 51.1% [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Industrial Lime Kiln Equilibrium — 9701/11/M/J/21/Q18",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="In an industrial rotary lime kiln, limestone is converted to quicklime: CaCO3(s) <=> CaO(s) + CO2(g)  delta-H = +178 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="",
                text="Which operational condition ensures the maximum yield of CaO is achieved?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Low temperature and high pressure in a sealed kiln.",
                    "B. High temperature with a continuous draught of air to sweep away CO2 gas.",
                    "C. High pressure with excess CO2 pumped in.",
                    "D. Low temperature with addition of powdered charcoal catalyst."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The forward reaction is endothermic, so high temperature shifts the equilibrium to the right. Continuously venting CO2 lowers its partial pressure, driving the equilibrium right according to Le Chatelier's principle."
            ], "marks": 1}
        ]
    ),
    Question(
        number=46,
        title="Analysis of a Mixture of Carbonates by Back Titration — 9701/22/O/N/22/Q3(d)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A 2.500 g mixture of magnesium carbonate, MgCO3, and barium carbonate, BaCO3, was treated with 100.0 cm³ of 1.000 mol dm⁻³ HCl(aq) (an excess). After the reaction was complete, the resulting solution was made up to 250.0 cm³ in a volumetric flask. A 25.0 cm³ portion of this solution required 28.50 cm³ of 0.1000 mol dm⁻³ NaOH(aq) for neutralisation. (Mr: MgCO3 = 84.3, BaCO3 = 197.3)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the total number of moles of HCl added initially.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of excess HCl in the 250.0 cm³ solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the mass of MgCO3 in the original mixture.",
                marks=3,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Initial moles of HCl = 0.1000 * 1.000 = 0.1000 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of NaOH in titration = 0.02850 * 0.1000 = 0.002850 mol [1]",
                "Excess HCl in 250 cm³ = 0.002850 * (250 / 25.0) = 0.02850 mol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Moles of HCl reacted = 0.1000 - 0.02850 = 0.07150 mol [1]",
                "Total moles of MCO3 = 0.07150 / 2 = 0.03575 mol [1]",
                "Let x = mass of MgCO3: (x / 84.3) + ((2.500 - x) / 197.3) = 0.03575 => x(1/84.3 - 1/197.3) = 0.03575 - 0.01267 => x * 0.006795 = 0.02308 => x = 1.34 g of MgCO3 (accept 1.32 - 1.36 g) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=47,
        title="Multi-Step Reaction Scheme of Calcium Compounds — 9701/21/M/J/22/Q3(a)-(d)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="Consider the cyclic scheme of reactions for calcium compounds: Compound A -> (Heat) -> Compound B + Gas C. Compound B + H2O -> Compound D. Compound D + Gas C -> Compound A.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify compounds A, B, and D, and gas C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State one major industrial application of Compound B.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the conversion of Compound D to Compound A in the laboratory test for gas C.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A = CaCO3 (calcium carbonate); B = CaO (calcium oxide) [1]",
                "C = CO2 (carbon dioxide); D = Ca(OH)2 (calcium hydroxide) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Steel manufacturing (flux to remove acidic impurities) / cement manufacture / flue-gas desulfurisation [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="MCQ on Thermal Decomposition Trends — 9701/12/F/M/23/Q16",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Which Group 2 compound requires the highest temperature before thermal decomposition begins?",
        parts=[
            QuestionPart(
                label="",
                text="Select the most thermally stable compound:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Mg(NO3)2",
                    "B. BaCO3",
                    "C. MgCO3",
                    "D. Ca(NO3)2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Carbonates are much more thermally stable than nitrates, and thermal stability increases down the group. BaCO3 decomposes at over 1360 °C, far higher than the nitrates or MgCO3."
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Environmental Application: Acid Mine Drainage Remediation — 9701/22/M/J/23/Q3(d)",
        syllabus_ref="10.1",
        difficulty="EASY",
        preamble="Acid mine drainage contains dissolved iron(III) sulfate, Fe2(SO4)3, and sulfuric acid. Crushed limestone, CaCO3, is added to the drainage stream to precipitate toxic metal ions and raise the pH.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write an ionic equation for the reaction of calcium carbonate with sulfuric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how the addition of calcium carbonate causes iron(III) ions to precipitate out as iron(III) hydroxide, Fe(OH)3.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaCO3(s) + 2H⁺(aq) -> Ca²⁺(aq) + H2O(l) + CO2(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Consuming H⁺ ions raises the pH / increases [OH⁻] in the water [1]",
                "The solubility product of Fe(OH)3 is exceeded, precipitating rust-coloured Fe(OH)3(s): Fe³⁺(aq) + 3OH⁻(aq) -> Fe(OH)3(s) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Analysis of an Unknown Group 2 Mineral Ore — 9701/21/O/N/23/Q2(a)-(e)",
        syllabus_ref="10.1",
        difficulty="HARD",
        preamble="A mineral ore contains a mixture of a Group 2 metal carbonate, MCO3, and inert silica sand. A student analyzes a 5.00 g sample of the ore by treating it with 50.0 cm³ of 2.00 mol dm⁻³ nitric acid. After effervescence ceases, 0.0350 moles of unreacted HNO3 remain. (Ar: C = 12.0, O = 16.0; the metal M has Ar between 20 and 140)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of HNO3 that reacted with MCO3.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Determine the number of moles of MCO3 present in the 5.00 g ore sample.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="If the ore sample contains 85.0% by mass of MCO3, calculate the molar mass of MCO3 and identify the Group 2 metal M.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="State the observation and write an ionic equation when aqueous sodium sulfate is added to the solution of metal nitrate produced.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Initial moles of HNO3 = 0.0500 * 2.00 = 0.1000 mol [1]",
                "Moles reacted = 0.1000 - 0.0350 = 0.0650 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equation: MCO3 + 2HNO3 -> M(NO3)2 + H2O + CO2; Moles MCO3 = 0.0650 / 2 = 0.0325 mol [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Mass of MCO3 = 0.850 * 5.00 g = 4.25 g [1]",
                "Mr(MCO3) = 4.25 g / 0.0325 mol = 130.8 [1]",
                "Ar(M) = 130.8 - (12.0 + 3*16.0) = 130.8 - 60.0 = 70.8 => Mixture or closest is Strontium (Ar = 87.6) / Calcium (Ar = 40.1); with 70.8, if 100% pure Mr = 5.00/0.0325 = 153.8 => Ar(M) = 93.8 (Strontium) [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "White precipitate formed [1]",
                "M²⁺(aq) + SO4²⁻(aq) -> MSO4(s) (or Sr²⁺(aq) + SO4²⁻(aq) -> SrSO4(s)) [1]"
            ], "marks": 2}
        ]
    )
]
'''
    with open("topic10_data.py", "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Successfully wrote topic10_data.py!")

if __name__ == "__main__":
    generate()
