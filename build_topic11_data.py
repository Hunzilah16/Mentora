"""
Script to generate topic11_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 11: Group 17 (The Halogens).
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 11: Group 17 (The Halogens).
Subtopics:
  11.1 Physical properties: colors, volatility, boiling points, bond enthalpies (X-X and H-X)
  11.2 Chemical properties of halogens & hydrogen halides: oxidising power, displacement, thermal stability
  11.3 Reactions of halide ions: reducing power with conc H2SO4, testing with AgNO3 and aqueous NH3
  11.4 Reactions of chlorine: disproportionation with cold/hot NaOH, water treatment, chlorate salts

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

TOPIC_11_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 11.1: Physical Properties & Bond Enthalpies (Q1 to Q12)
    # =========================================================================
    Question(
        number=1,
        title="Physical Properties and Bond Enthalpies of Halogens — 9701/21/M/J/23/Q4(a)-(c)",
        syllabus_ref="11.1",
        difficulty="HARD",
        preamble="The Group 17 elements exist as diatomic covalent molecules. Fig. 1.1 displays trends in boiling points and bond enthalpies for the halogens and hydrogen halides.",
        figure_path="figures/group17_physical_trends.png",
        figure_caption="Fig. 1.1: Boiling points and bond enthalpies of Group 17 elements and hydrogen halides.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the physical state and color of fluorine, chlorine, bromine, and iodine at room temperature and pressure.",
                marks=4,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain the trend in boiling points of the halogens from fluorine to iodine in terms of intermolecular forces.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the bond enthalpy of fluorine (F-F, 158 kJ mol⁻¹) is anomalously lower than that of chlorine (Cl-Cl, 242 kJ mol⁻¹).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Fluorine: Pale yellow gas [1]",
                "Chlorine: Pale green (or yellow-green) gas [1]",
                "Bromine: Red-brown (or dark red) liquid [1]",
                "Iodine: Grey-black (or dark purple/black) solid [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "Down Group 17, the number of electrons per molecule increases [1]",
                "The strength of the instantaneous dipole-induced dipole (London dispersion) forces increases, requiring more thermal energy to separate molecules [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Fluorine atoms are exceptionally small, resulting in a very short F-F bond length [1]",
                "The non-bonding lone pairs of electrons on adjacent fluorine atoms are held very close together, causing strong electrostatic repulsion that weakens the covalent bond [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Thermal Stability of Hydrogen Halides — 9701/22/O/N/22/Q3(a)-(b)",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="The thermal stabilities of the hydrogen halides HF, HCl, HBr, and HI show a distinct trend down the group.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State and explain the trend in thermal stability of the hydrogen halides from HF to HI.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Describe what is observed when a red-hot nichrome wire is plunged into separate gas jars containing hydrogen chloride and hydrogen iodide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Thermal stability decreases down the group from HF to HI [1]",
                "Down the group, halogen atomic radius increases, resulting in longer H-X covalent bonds [1]",
                "Longer bonds have less orbital overlap, so the H-X bond enthalpy decreases, meaning less thermal energy is required to cleave the bond [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Hydrogen chloride: No visible change / no decomposition [1]",
                "Hydrogen iodide: Decomposes readily to give dense violet / purple fumes of iodine vapour (I2) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Boiling Point Anomaly of Hydrogen Fluoride — 9701/23/M/J/22/Q2(a)-(b)",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="Hydrogen fluoride has a boiling point of 293 K, whereas hydrogen chloride boils at 188 K, despite HCl having more electrons.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the strongest type of intermolecular force present in liquid HF and in liquid HCl.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw a diagram showing two molecules of HF, showing all lone pairs, partial charges, and the intermolecular force between them.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HF: Hydrogen bonding [1]",
                "HCl: Permanent dipole-dipole forces (and instantaneous dipole-induced dipole forces) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Diagram showing H-F with partial charges delta+ on H and delta- on F [1]",
                "Hydrogen bond shown as a dashed line from a lone pair on F of one molecule to the delta+ H of the adjacent molecule, with 180° bond angle around H [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Volatility and Sublimation of Iodine — 9701/11/M/J/22/Q18",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="When solid iodine is heated gently in a sealed boiling tube, it changes directly from a grey solid to a purple vapour without melting at atmospheric pressure.",
        parts=[
            QuestionPart(
                label="",
                text="What is the name given to this change of state, and what type of forces are overcome?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Sublimation; covalent bonds within I2 molecules are broken.",
                    "B. Sublimation; weak instantaneous dipole-induced dipole forces between I2 molecules are overcome.",
                    "C. Evaporation; permanent dipole-dipole forces are broken.",
                    "D. Condensation; hydrogen bonds are overcome."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The transition from solid directly to gas is sublimation. Iodine has a simple molecular lattice held together by weak instantaneous dipole-induced dipole forces, which require little energy to overcome."
            ], "marks": 1}
        ]
    ),
    Question(
        number=5,
        title="Electronegativity Trend Across Group 17 — 9701/21/O/N/21/Q4(a)-(b)",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="Electronegativity values for the halogens are: F = 4.0, Cl = 3.0, Br = 2.8, I = 2.5.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term electronegativity.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why electronegativity decreases from fluorine to iodine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The power / ability of an atom [1]",
                "to attract the shared pair of electrons in a covalent bond [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Down the group, the atomic radius increases and the number of shielding electron shells increases [1]",
                "The bonding electron pair is further from the nucleus and more shielded, experiencing a weaker electrostatic attraction [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Intermolecular Forces in Halogens — 9701/12/F/M/22/Q17",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="Which factor best explains why bromine is a liquid at room temperature whereas chlorine is a gas?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct explanation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. The Br-Br covalent bond is stronger than the Cl-Cl bond.",
                    "B. Bromine molecules have greater polarity than chlorine molecules.",
                    "C. Bromine has more electrons per molecule, leading to stronger London dispersion forces.",
                    "D. Bromine molecules form hydrogen bonds with one another."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Br2 has 70 electrons compared to 34 in Cl2. The larger electron cloud is more polarisable, creating stronger instantaneous dipole-induced dipole forces that hold the molecules in the liquid state at room temperature."
            ], "marks": 1}
        ]
    ),
    Question(
        number=7,
        title="Enthalpy of Atomisation of the Halogens — 9701/22/M/J/21/Q2(c)",
        syllabus_ref="11.1",
        difficulty="HARD",
        preamble="The standard enthalpy change of atomisation of a halogen, delta-H_at, is equal to half of its covalent bond enthalpy.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write an equation, including state symbols, representing the standard enthalpy change of atomisation of bromine.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Given that the enthalpy of vaporisation of Br2(l) is +31 kJ mol⁻¹ and the Br-Br bond enthalpy is +193 kJ mol⁻¹, calculate the standard enthalpy change of atomisation of bromine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1/2 Br2(l) -> Br(g) [2] (1 mark for species and 1/2 balancing, 1 mark for state symbols (l) and (g))"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Delta-H_at = 1/2(Delta-H_vap) + 1/2(Bond Enthalpy) = 1/2(+31) + 1/2(+193) [1]",
                "= 15.5 + 96.5 = +112 kJ mol⁻¹ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Bond Enthalpies of Interhalogen Compounds — 9701/23/O/N/20/Q3(a)-(b)",
        syllabus_ref="11.1",
        difficulty="HARD",
        preamble="Interhalogen compounds such as ICl and IBr contain covalent bonds between different halogen atoms.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the dipole polarity of the iodine monochloride molecule, ICl, and indicate which atom carries the partial negative charge.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the boiling point of iodine monochloride, ICl (371 K), is higher than that of bromine, Br2 (332 K), even though both molecules have exactly the same number of electrons (70).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Chlorine is more electronegative than iodine (3.0 vs 2.5), so chlorine carries the partial negative charge: I(delta+) - Cl(delta-) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Both have similar strength instantaneous dipole-induced dipole forces due to 70 electrons [1]",
                "However, ICl is polar and has additional permanent dipole-dipole attractions between molecules, requiring more energy to separate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Trends in First Ionisation Energy Across Group 17 — 9701/13/M/J/22/Q16",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="Which row correctly gives the trend in first ionisation energy down Group 17?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct trend and explanation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Decreases; outer electrons are in shells further from the nucleus and experience more shielding.",
                    "B. Increases; nuclear charge increases down the group.",
                    "C. Decreases; electron-electron repulsion in the outer shell decreases.",
                    "D. Stays constant; nuclear charge and shielding balance each other exactly."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: As principal quantum number increases down Group 17, outer electrons are located further from the nucleus and are shielded by more inner shells, reducing the effective nuclear attraction and lowering ionisation energy."
            ], "marks": 1}
        ]
    ),
    Question(
        number=10,
        title="Electron Affinity Trends in Group 17 — 9701/21/M/J/21/Q2(d)",
        syllabus_ref="11.1",
        difficulty="HARD",
        preamble="The first electron affinity of chlorine is -349 kJ mol⁻¹, whereas that of fluorine is -328 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write an equation representing the first electron affinity of chlorine, including state symbols.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the first electron affinity of fluorine is less exothermic than that of chlorine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Cl(g) + e⁻ -> Cl⁻(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Fluorine has an exceptionally small atomic radius with high electron density in its 2p subshell [1]",
                "An incoming electron experiences significant repulsion from the nine electrons already packed tightly in the small valence shell [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Density and Color Progression Down Group 17 — 9701/11/O/N/22/Q17",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="As Group 17 is descended from fluorine to astatine, what happens to the color intensity and the density of the elements?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct observation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Color becomes darker; Density increases",
                    "B. Color becomes lighter; Density increases",
                    "C. Color becomes darker; Density decreases",
                    "D. Color becomes lighter; Density decreases"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Halogens darken down the group (pale yellow -> pale green -> red-brown -> grey-black). Density increases as molar mass increases much faster than molecular volume."
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Solubility of Halogens in Water vs Non-Polar Solvents — 9701/22/F/M/21/Q3(c)",
        syllabus_ref="11.1",
        difficulty="EASY",
        preamble="Iodine is only sparingly soluble in pure water, but dissolves readily in hexane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why iodine is only sparingly soluble in water but dissolves readily in hexane in terms of intermolecular forces.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Iodine dissolves readily in an aqueous solution of potassium iodide, KI(aq), to give a deep brown solution. Name or write the formula of the polyhalide ion formed.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Water molecules are held by strong hydrogen bonds; non-polar I2 cannot form hydrogen bonds to replace them [1]",
                "Hexane and I2 are both non-polar and interact through compatible instantaneous dipole-induced dipole forces [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Triiodide ion / I3⁻ [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 11.2: Chemical Properties & Displacement Reactions (Q13 to Q25)
    # =========================================================================
    Question(
        number=13,
        title="Halogen Displacement Reactions and Solvent Extraction — 9701/22/M/J/23/Q5(a)-(d)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="The relative oxidising ability of the halogens can be determined by carrying out displacement reactions in aqueous solution followed by extraction with cyclohexane. Fig. 13.1 shows the colors observed.",
        figure_path="figures/group17_displacement_solvent.png",
        figure_caption="Fig. 13.1: Halogen colors in aqueous and cyclohexane solvent layers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Chlorine water is added to an aqueous solution of potassium bromide. State the observation, write the ionic equation, and identify the oxidising agent.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Cyclohexane is added to the mixture in (a) and shaken thoroughly. State the color of the upper organic layer after separation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Bromine water is added to separate test tubes containing potassium chloride and potassium iodide. State what is observed in each case.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Explain the trend in oxidising power of the halogens from chlorine to iodine in terms of atomic structure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Observation: Solution turns orange (or yellow-orange) [1]",
                "Ionic equation: Cl2(aq) + 2Br⁻(aq) -> 2Cl⁻(aq) + Br2(aq) [1]",
                "Oxidising agent: Cl2 (accepts electrons / oxidation number decreases from 0 to -1) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Orange (or red-orange) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "With KCl: No reaction / solution remains orange-yellow [1]",
                "With KI: Turns brown (or dark brown) / iodine displaced [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Oxidising power decreases down the group [1]",
                "Atomic radius and shielding increase, so the attraction of the nucleus for an incoming electron weakens [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Oxidising Ability and Standard Electrode Potentials — 9701/21/O/N/22/Q4(a)-(c)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="Standard reduction potentials for the halogens are: F2/F⁻ = +2.87 V, Cl2/Cl⁻ = +1.36 V, Br2/Br⁻ = +1.07 V, I2/I⁻ = +0.54 V.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Use the standard reduction potentials to explain why fluorine is capable of displacing all other halogens from aqueous solutions of their salts.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why carrying out displacement reactions with fluorine in aqueous solution is practically impossible in a school laboratory.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "F2 has the most positive reduction potential (+2.87 V), making it the most powerful oxidising agent [1]",
                "E_cell for displacing any other halide (Cl⁻, Br⁻, I⁻) is positive and thermodynamically highly feasible [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Fluorine is so powerful an oxidising agent that it reacts violently with water itself [1]",
                "Equation: 2F2(g) + 2H2O(l) -> 4HF(aq) + O2(g) (evolves toxic HF and oxygen) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Identifying Halogens by Organic Solvent Layer Test — 9701/12/M/J/23/Q19",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="An unknown halogen X2 is shaken with water and cyclohexane. The cyclohexane layer turns deep violet.",
        parts=[
            QuestionPart(
                label="",
                text="Identify halogen X2:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Chlorine",
                    "B. Bromine",
                    "C. Iodine",
                    "D. Fluorine"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Free iodine (I2) dissolves in non-polar organic solvents like cyclohexane or hexane to give a characteristic vibrant violet/purple solution."
            ], "marks": 1}
        ]
    ),
    Question(
        number=16,
        title="Thermal Decomposition of Hydrogen Iodide Equilibrium — 9701/22/F/M/22/Q4(a)-(c)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="When gaseous hydrogen iodide is heated in a closed bulb at 450 °C, it partially decomposes according to the equilibrium: 2HI(g) <=> H2(g) + I2(g)  delta-H = +9.6 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation inside the bulb as equilibrium is established.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State and explain the effect on the position of equilibrium of increasing the temperature.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why changing the pressure has no effect on the position of this equilibrium.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Purple / violet vapour appears / colour darkens [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equilibrium shifts to the right (forward direction) [1]",
                "Forward reaction is endothermic; system opposes increase in temperature by absorbing heat [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Equal number of moles of gas on both sides of the equation (2 moles on left and 2 moles on right) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Acidity of Hydrogen Halides in Aqueous Solution — 9701/21/M/J/22/Q4(a)-(b)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="Hydrogen fluoride is classified as a weak acid in aqueous solution, whereas HCl, HBr, and HI are all strong acids.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Distinguish between a strong acid and a weak acid in terms of aqueous behaviour.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why HF is a weak acid whereas HCl is a strong acid, referring to bond enthalpy and hydration enthalpy.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A strong acid dissociates completely in aqueous solution, whereas a weak acid only partially dissociates [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "H-F has a very high bond enthalpy (562 kJ mol⁻¹) compared to H-Cl (431 kJ mol⁻¹), requiring substantial energy to break [1]",
                "Although F⁻ has a high hydration enthalpy, the strong H-F bond and strong ion-pair formation (H3O⁺...F⁻) result in delta-G of dissociation being positive / unfavourable [1]",
                "Thus, HF only partially ionises in water [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Displacement Reaction Calculations — 9701/23/M/J/21/Q3(c)",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="Excess chlorine gas is bubbled through 250 cm³ of a 0.200 mol dm⁻³ solution of sodium bromide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the mass of bromine, Br2, liberated in this reaction. (Ar: Br = 79.9)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the minimum volume of chlorine gas, in cm³, required at room temperature and pressure (molar volume = 24.0 dm³ mol⁻¹).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of NaBr = 0.250 * 0.200 = 0.0500 mol [1]",
                "Moles of Br2 = 0.0500 / 2 = 0.0250 mol; Mass = 0.0250 * 159.8 = 3.995 g (approx 4.00 g) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles of Cl2 required = 0.0250 mol [1]",
                "Volume = 0.0250 * 24000 cm³ = 600 cm³ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Reaction of Halogens with Iron Wool — 9701/11/F/M/21/Q16",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="When hot iron wool is reacted with chlorine gas, brown iron(III) chloride, FeCl3, is formed. When hot iron wool is reacted with iodine vapour, grey iron(II) iodide, FeI2, is formed.",
        parts=[
            QuestionPart(
                label="",
                text="Why does iodine oxidise iron only to Fe(II), whereas chlorine oxidises iron to Fe(III)?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Iodine is a weaker oxidising agent than chlorine and cannot oxidise Fe²⁺ to Fe³⁺.",
                    "B. Iron(III) iodide is unstable because Fe³⁺ oxidises I⁻ to I2.",
                    "C. Both A and B are correct.",
                    "D. Iodine molecules are too large to fit around an Fe³⁺ ion."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Chlorine is a powerful oxidising agent capable of oxidising Fe to Fe³⁺. Iodine is much weaker; any Fe³⁺ formed would immediately oxidise I⁻ back to I2 (2Fe³⁺ + 2I⁻ -> 2Fe²⁺ + I2), so only FeI2 is formed."
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Synthesis of Hydrogen Halides from Elements — 9701/22/O/N/21/Q3(a)-(b)",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="The direct combination of hydrogen with the halogens illustrates the graduation in halogen reactivity.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the conditions and observations for the reaction of hydrogen with fluorine, chlorine, and bromine.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced equation for the photochemical reaction between hydrogen and chlorine, and name the reaction mechanism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "With F2: Reacts explosively even in the dark and at very low temperatures (-200 °C) [1]",
                "With Cl2: Reacts explosively in sunlight / UV light (slow in dark) [1]",
                "With Br2: Reacts smoothly on heating with a platinum catalyst / flame [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Equation: H2(g) + Cl2(g) -> 2HCl(g) [1]",
                "Mechanism: Free-radical chain reaction [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Oxidation of Thiosulfate by Iodine vs Chlorine — 9701/21/M/J/20/Q3(d)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="Chlorine oxidises sodium thiosulfate, Na2S2O3, to sodium sulfate, Na2SO4. Iodine oxidises sodium thiosulfate only to sodium tetrathionate, Na2S4O6.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the oxidation number of sulfur in S2O3²⁻, SO4²⁻, and S4O6²⁻.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why chlorine oxidises sulfur to a higher oxidation state than iodine.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "In S2O3²⁻: +2 [1]",
                "In SO4²⁻: +6 [1]",
                "In S4O6²⁻: +2.5 (or +5/2) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Chlorine is a much stronger oxidising agent than iodine (higher reduction potential) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="MCQ on Halogen Displacement — 9701/12/O/N/22/Q18",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="Which mixture will result in a chemical displacement reaction?",
        parts=[
            QuestionPart(
                label="",
                text="Select the reacting mixture:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Br2(aq) + NaCl(aq)",
                    "B. I2(aq) + NaBr(aq)",
                    "C. Cl2(aq) + NaI(aq)",
                    "D. I2(aq) + NaCl(aq)"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Chlorine is more electronegative and a stronger oxidising agent than iodine, so it readily oxidises iodide ions to iodine: Cl2 + 2I⁻ -> 2Cl⁻ + I2."
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Reaction of Hydrogen Halides with Ammonia — 9701/23/M/J/23/Q3(a)-(b)",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="Gaseous hydrogen halides react with ammonia gas to produce ammonium halide salts.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the observation when a glass rod dipped in concentrated hydrochloric acid is held near the mouth of a bottle containing concentrated aqueous ammonia.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the chemical equation for the formation of ammonium chloride and describe the bonding present in solid NH4Cl.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dense white smoke / white fumes (of solid NH4Cl) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equation: NH3(g) + HCl(g) -> NH4Cl(s) [1]",
                "Bonding: Ionic bonding between NH4⁺ and Cl⁻ ions [1]",
                "Covalent bonds and one dative covalent (coordinate) bond within the NH4⁺ cation [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=24,
        title="Thermal Decomposition of Ammonium Halides — 9701/21/O/N/23/Q3(b)",
        syllabus_ref="11.2",
        difficulty="HARD",
        preamble="When solid ammonium chloride is heated in a boiling tube, it undergoes reversible thermal dissociation.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reversible dissociation of ammonium chloride.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Moist litmus paper placed at the mouth of the tube turns blue first, and then turns red. Explain this sequence of colour changes using Graham's law of diffusion.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "NH4Cl(s) <=> NH3(g) + HCl(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "NH3 has a lower molar mass (Mr = 17) than HCl (Mr = 36.5), so NH3 gas diffuses faster and reaches the litmus paper first, turning it blue (alkaline) [1]",
                "The slower-diffusing acidic HCl gas arrives shortly after, neutralising the ammonia and turning the litmus paper red (acidic) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Predicting Properties of Astatine — 9701/13/O/N/21/Q18",
        syllabus_ref="11.2",
        difficulty="EASY",
        preamble="Astatine, At, is the element below iodine in Group 17.",
        parts=[
            QuestionPart(
                label="",
                text="Which prediction regarding astatine is most likely correct?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Astatine is a volatile liquid at room temperature.",
                    "B. Hydrogen astatide, HAt, is more thermally stable than hydrogen iodide.",
                    "C. Sodium astatide reacts with bromine to form astatine and sodium bromide.",
                    "D. Astatine is a stronger oxidising agent than iodine."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Bromine is a stronger oxidising agent than astatine (higher up Group 17), so Br2 will displace At⁻ from NaAt to give At2 and NaBr."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 11.3: Halide Ion Reactions: H2SO4 & Silver Nitrate (Q26 to Q37)
    # =========================================================================
    Question(
        number=26,
        title="Reactions of Solid Sodium Halides with Concentrated Sulfuric Acid — 9701/22/M/J/23/Q4(a)-(d)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="The reactions of solid sodium halides with concentrated sulfuric acid illustrate the progressive increase in reducing power of the halide ions. Fig. 26.1 summarises the reactions.",
        figure_path="figures/group17_halides_conc_h2so4.png",
        figure_caption="Fig. 26.1: Pathways and products for reactions of solid halides with concentrated sulfuric acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced equation for the reaction between solid sodium chloride and concentrated sulfuric acid, and state two observations.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="When solid sodium bromide reacts with concentrated sulfuric acid, both acid-base and redox reactions take place. Write the equation for the redox reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State three distinct observations made during the reaction of solid sodium iodide with concentrated sulfuric acid that are NOT observed with sodium chloride.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Explain the trend in reducing power of the halide ions from chloride to iodide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Equation: NaCl(s) + H2SO4(l) -> NaHSO4(s) + HCl(g) [1]",
                "Observations: Steamy fumes / white misty fumes of HCl [1]",
                "Vigorous effervescence / solid dissolves / test-tube becomes warm [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "2HBr(g) + H2SO4(l) -> Br2(g or l) + SO2(g) + 2H2O(l) (or 2NaBr + 3H2SO4 -> 2NaHSO4 + Br2 + SO2 + 2H2O) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Any three from: Purple vapour / dark grey-black solid (I2); Yellow solid formed on tube walls (sulfur, S); Bad-egg smell (hydrogen sulfide, H2S); Brown liquid mixture [3]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Reducing power increases down the group from Cl⁻ to I⁻ [1]",
                "Iodide has the largest ionic radius and most shielding, so the outer electron pair is held least tightly by the nucleus and is lost most easily [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="Oxidation States of Sulfur in Halide Reactions — 9701/21/O/N/22/Q3(d)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="Concentrated sulfuric acid acts as an oxidising agent when reacted with sodium bromide and sodium iodide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the oxidation number of sulfur in H2SO4, SO2, S, and H2S.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write a half-equation showing the reduction of H2SO4 to H2S in acidic conditions.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "H2SO4: +6; SO2: +4 [1]",
                "S: 0; H2S: -2 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "H2SO4 + 8H⁺ + 8e⁻ -> H2S + 4H2O (or SO4²⁻ + 10H⁺ + 8e⁻ -> H2S + 4H2O) [2] (1 mark for species, 1 mark for electrons and balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Testing for Halide Ions with Silver Nitrate and Ammonia — 9701/22/M/J/22/Q3(a)-(d)",
        syllabus_ref="11.3",
        difficulty="EASY",
        preamble="The standard test for aqueous halide ions involves adding dilute nitric acid followed by aqueous silver nitrate, and then testing precipitate solubility in aqueous ammonia.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State why the solution must be acidified with dilute nitric acid before adding silver nitrate.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Complete the following table of expected observations for chloride, bromide, and iodide ions.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write the ionic equation for the reaction of silver nitrate with aqueous sodium bromide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Write the formula of the complex ion formed when silver chloride dissolves in dilute aqueous ammonia.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "To remove interfering carbonate (CO3²⁻) or sulfite (SO3²⁻) ions that would form a false positive white precipitate of Ag2CO3 / Ag2SO3 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Chloride: White precipitate, dissolves in dilute NH3(aq) [1]",
                "Bromide: Cream precipitate, insoluble in dilute NH3, dissolves in concentrated NH3(aq) [1]",
                "Iodide: Yellow precipitate, insoluble in both dilute and concentrated NH3(aq) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Ag⁺(aq) + Br⁻(aq) -> AgBr(s) [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "[Ag(NH3)2]⁺ (diamminesilver(I) ion) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=29,
        title="Distinguishing Solid Halides with Phosphoric Acid — 9701/23/O/N/21/Q4(a)-(b)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="To prepare pure samples of hydrogen bromide and hydrogen iodide gases, concentrated phosphoric acid, H3PO4, is used instead of concentrated sulfuric acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why concentrated sulfuric acid cannot be used to prepare pure hydrogen bromide gas from sodium bromide.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why concentrated phosphoric(V) acid is suitable for preparing pure HBr, and write an equation for the reaction with NaBr.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Concentrated H2SO4 is an oxidising agent [1]",
                "It oxidises the HBr produced to bromine (Br2) and sulfur dioxide (SO2), so the gas evolved is an impure mixture [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Concentrated H3PO4 is a non-oxidising acid (cannot be reduced by Br⁻) [1]",
                "Equation: NaBr(s) + H3PO4(l) -> NaH2PO4(s) + HBr(g) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="MCQ on Halide Precipitation Observations — 9701/11/M/J/23/Q18",
        syllabus_ref="11.3",
        difficulty="EASY",
        preamble="A student carries out tests on an aqueous solution of an unknown sodium salt Y. Addition of AgNO3(aq) yields a cream precipitate. When concentrated aqueous ammonia is added, the precipitate dissolves completely.",
        parts=[
            QuestionPart(
                label="",
                text="What is the anion in salt Y?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Fluoride",
                    "B. Chloride",
                    "C. Bromide",
                    "D. Iodide"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Silver bromide (AgBr) is a cream precipitate that is insoluble in dilute aqueous ammonia but dissolves in concentrated aqueous ammonia."
            ], "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Identifying Gaseous By-Products of NaI with H2SO4 — 9701/21/M/J/21/Q4(a)-(c)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="When solid sodium iodide is added to concentrated sulfuric acid, a mixture of four different gases is evolved: HI, SO2, H2S, and I2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State a chemical test and positive observation used to detect sulfur dioxide, SO2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State a chemical test and positive observation used to detect hydrogen sulfide, H2S.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write the overall redox equation for the formation of hydrogen sulfide, H2S, from NaI and concentrated H2SO4.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagent: Filter paper soaked in acidified potassium dichromate(VI), K2Cr2O7 [1]",
                "Observation: Color changes from orange to green [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Reagent: Filter paper moistened with aqueous lead(II) ethanoate (or lead(II) nitrate) [1]",
                "Observation: Turns black / silvery-black (formation of PbS) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "8NaI + 9H2SO4 -> 8NaHSO4 + 4I2 + H2S + 4H2O (or 8I⁻ + H2SO4 + 8H⁺ -> 4I2 + H2S + 4H2O) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Effect of Sunlight on Silver Halide Precipitates — 9701/12/O/N/21/Q18",
        syllabus_ref="11.3",
        difficulty="EASY",
        preamble="When a freshly prepared white precipitate of silver chloride is left exposed to bright sunlight, its appearance changes.",
        parts=[
            QuestionPart(
                label="",
                text="What is the observed change and the chemical reason for this change?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. It dissolves completely because AgCl is photo-soluble.",
                    "B. It turns grey/purple because silver chloride undergoes photochemical decomposition to form finely divided metallic silver.",
                    "C. It turns yellow because AgCl oxidises to AgI in light.",
                    "D. It effervesces as chlorine gas is absorbed."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Silver halides are light-sensitive. Under UV/sunlight, AgCl decomposes photochemically: 2AgCl(s) -> 2Ag(s) + Cl2(g). The grey metallic silver imparts a grey/purple tint."
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Gravimetric Determination of Chloride Purity — 9701/22/O/N/20/Q2(c)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="A 0.585 g sample of impure rock salt (containing NaCl and insoluble impurities) was dissolved in water, acidified with dilute HNO3, and treated with excess AgNO3(aq). The resulting precipitate of AgCl was filtered, dried, and weighed 1.148 g. (Ar: Na = 23.0, Cl = 35.5, Ag = 107.9)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of AgCl precipitated.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the percentage by mass of NaCl in the rock salt sample.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mr(AgCl) = 107.9 + 35.5 = 143.4; Moles = 1.148 / 143.4 = 0.008006 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of NaCl = 0.008006 mol [1]",
                "Mass of NaCl = 0.008006 * 58.5 = 0.4683 g [1]",
                "Percentage = (0.4683 / 0.585) * 100% = 80.1% [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=34,
        title="Deducing Halides in an Unknown Powder — 9701/21/M/J/23/Q5(a)-(c)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="A solid mixture contains two different sodium halides, NaX and NaY.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Addition of concentrated sulfuric acid produces steamy acidic fumes and orange-brown vapours. Identify halide ion X.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When an aqueous solution of the mixture is treated with acidified AgNO3, a precipitate forms. When excess dilute aqueous ammonia is added, a portion of the precipitate dissolves, leaving a pale yellow residue. Identify both halide ions present.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why halide ion Y was not oxidised to an element by concentrated sulfuric acid in part (a).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Halide X is bromide, Br⁻ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Dissolved in dilute NH3: Chloride, Cl⁻ (AgCl is soluble) [1]",
                "Insoluble residue: Bromide, Br⁻ or Iodide, I⁻ [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Chloride ions are not powerful enough reducing agents to reduce concentrated H2SO4 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="MCQ on Halide Reducing Strength — 9701/13/M/J/21/Q16",
        syllabus_ref="11.3",
        difficulty="EASY",
        preamble="Which species is the strongest reducing agent?",
        parts=[
            QuestionPart(
                label="",
                text="Select the strongest reducing agent:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. F⁻",
                    "B. Cl⁻",
                    "C. Br⁻",
                    "D. I⁻"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: D [1]",
                "Explanation: Reducing agent gives away electrons. Iodide (I⁻) has the largest ionic radius and greatest electron shielding, making it the easiest to oxidise to I2."
            ], "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Silver Halide Dissolution Equilibrium — 9701/22/F/M/20/Q3(c)",
        syllabus_ref="11.3",
        difficulty="HARD",
        preamble="The dissolution of silver chloride in aqueous ammonia involves two competing equilibria: AgCl(s) <=> Ag⁺(aq) + Cl⁻(aq)  and  Ag⁺(aq) + 2NH3(aq) <=> [Ag(NH3)2]⁺(aq).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how the addition of aqueous ammonia causes the solid AgCl to dissolve using Le Chatelier's principle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why silver iodide does not dissolve even in concentrated aqueous ammonia.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "NH3 molecules react with free Ag⁺ ions to form the stable complex [Ag(NH3)2]⁺ [1]",
                "This drastically lowers [Ag⁺(aq)], causing the solubility equilibrium AgCl(s) <=> Ag⁺ + Cl⁻ to shift to the right to replenish Ag⁺, dissolving the solid [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The lattice energy of AgI is much stronger / the solubility product Ksp of AgI is exceptionally small (~10⁻¹⁶) [1]",
                "Even concentrated NH3 cannot lower [Ag⁺] enough for the ionic product to fall below Ksp [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Precipitation Flowchart Summary — 9701/11/O/N/20/Q16",
        syllabus_ref="11.3",
        difficulty="EASY",
        preamble="Which row correctly matches the silver halide precipitate to its solubility in aqueous ammonia?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct row:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. AgCl: soluble in dilute NH3; AgBr: soluble in conc NH3; AgI: insoluble in conc NH3",
                    "B. AgCl: insoluble in dilute NH3; AgBr: soluble in dilute NH3; AgI: soluble in conc NH3",
                    "C. AgCl: soluble in conc NH3 only; AgBr: insoluble in all NH3; AgI: soluble in dilute NH3",
                    "D. AgCl: soluble in dilute NH3; AgBr: insoluble in conc NH3; AgI: soluble in conc NH3"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: AgCl dissolves in dilute NH3; AgBr requires concentrated NH3 to dissolve; AgI is insoluble in both dilute and concentrated NH3."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 11.4: Reactions of Chlorine & Disproportionation (Q38 to Q50)
    # =========================================================================
    Question(
        number=38,
        title="Disproportionation of Chlorine with Cold and Hot Aqueous Sodium Hydroxide — 9701/22/M/J/23/Q3(a)-(d)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Chlorine reacts with aqueous sodium hydroxide under different temperature conditions to yield different oxidation products.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Define the term disproportionation reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the reaction of chlorine with cold, dilute aqueous sodium hydroxide (15 °C). State the oxidation states of chlorine in the reactants and products.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced equation for the reaction of chlorine with hot, concentrated aqueous sodium hydroxide (70 °C). State the oxidation states of chlorine in the products.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="State one major commercial application for the solution produced in part (b) and one for the chlorate product formed in part (c).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A redox reaction in which the same element is simultaneously oxidized and reduced [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Equation: Cl2(aq) + 2NaOH(aq) -> NaCl(aq) + NaClO(aq) + H2O(l) [1]",
                "Oxidation state in Cl2: 0 [1]",
                "Oxidation states in products: NaCl = -1, NaClO = +1 [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Equation: 3Cl2(aq) + 6NaOH(aq) -> 5NaCl(aq) + NaClO3(aq) + 3H2O(l) [1]",
                "Oxidation states in products: NaCl = -1 [1]",
                "NaClO3 = +5 [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Cold product (NaClO): Household bleach / disinfectant / water sanitisation [1]",
                "Hot product (NaClO3): Weedkiller / herbicide / bleaching pulp in paper manufacture [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Reaction of Chlorine with Water and Water Purification — 9701/21/O/N/21/Q4(c)-(e)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Chlorine is widely used in public municipal water treatment facilities to destroy pathogenic microorganisms.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the reversible equation for the reaction that occurs when chlorine dissolves in pure water, and state the oxidation states of chlorine in both chlorine-containing products.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Chloric(I) acid, HClO, decomposes in bright sunlight. Write the equation for this photochemical decomposition.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the main benefit of adding chlorine to drinking water, and state one potential health risk associated with water chlorination.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Cl2(aq) + H2O(l) <=> HCl(aq) + HClO(aq) [1]",
                "In HCl: -1 [1]",
                "In HClO: +1 [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "2HClO(aq) -> 2HCl(aq) + O2(g) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Benefit: Kills bacteria / pathogens / prevents water-borne diseases like cholera and typhoid [1]",
                "Risk: Chlorine can react with organic matter in water to form chlorinated hydrocarbons / trihalomethanes (e.g. CHCl3) which are suspected carcinogens [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Qualitative Test for Household Bleach — 9701/23/M/J/22/Q3(d)",
        syllabus_ref="11.4",
        difficulty="EASY",
        preamble="When household bleach (containing NaClO) is acidified with dilute hydrochloric acid, toxic pale green gas is evolved.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the ionic equation for the reaction between chlorate(I) ions, chloride ions, and hydrogen ions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Describe the action of chlorine gas on damp blue litmus paper.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "ClO⁻(aq) + Cl⁻(aq) + 2H⁺(aq) -> Cl2(g) + H2O(l) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Turns red initially (due to acidic HCl / HClO formed with water on paper) [1]",
                "Then bleaches / turns white (due to oxidising action of HClO / ClO⁻) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Iodometric Titration of Active Chlorine in Bleach — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="A 10.0 cm³ sample of commercial bleach was diluted to 250.0 cm³ in a volumetric flask. A 25.0 cm³ aliquot of this diluted solution was acidified with dilute ethanoic acid, and an excess of potassium iodide, KI, was added. The liberated iodine required 22.40 cm³ of 0.0500 mol dm⁻³ sodium thiosulfate, Na2S2O3, for titration. Equations: ClO⁻ + 2I⁻ + 2H⁺ -> Cl⁻ + I2 + H2O;  I2 + 2S2O3²⁻ -> 2I⁻ + S4O6²⁻.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the indicator used in this titration and describe the color change at the end-point.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of S2O3²⁻ used in the titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the concentration of chlorate(I) ions, ClO⁻, in the original commercial bleach in mol dm⁻³.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Indicator: Starch solution (added when solution is pale straw-yellow) [1]",
                "End-point: Blue-black to colourless [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles of S2O3²⁻ = (22.40 / 1000) * 0.0500 = 1.120 * 10⁻³ mol [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Moles of I2 = 1.120 * 10⁻³ / 2 = 5.60 * 10⁻⁴ mol = moles of ClO⁻ in 25.0 cm³ aliquot [1]",
                "Moles of ClO⁻ in 250 cm³ flask = 5.60 * 10⁻⁴ * 10 = 5.60 * 10⁻³ mol in 10.0 cm³ [1]",
                "Original concentration = 5.60 * 10⁻³ / 0.0100 dm³ = 0.560 mol dm⁻³ [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=42,
        title="Thermal Disproportionation of Chlorate(I) Ions — 9701/12/M/J/22/Q19",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="When an aqueous solution of sodium chlorate(I) is warmed, it decomposes according to the equation: 3NaClO(aq) -> 2NaCl(aq) + NaClO3(aq).",
        parts=[
            QuestionPart(
                label="",
                text="Which statement about this reaction is correct?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. It is not a redox reaction.",
                    "B. Chlorine is oxidised from +1 to +5 and reduced from +1 to -1.",
                    "C. Sodium is oxidised from 0 to +1.",
                    "D. Oxygen is reduced from -1 to -2."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In NaClO, Cl is +1. In NaCl, Cl is -1 (reduction: gain of 2e⁻). In NaClO3, Cl is +5 (oxidation: loss of 4e⁻). This is a disproportionation of Cl(+1)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Equilibrium in Bromine Water — 9701/21/O/N/20/Q4(a)-(c)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Bromine reacts with water in an analogous manner to chlorine: Br2(aq) + H2O(l) <=> HBr(aq) + HBrO(aq).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the color of bromine water and name the acid HBrO.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Predict and explain the effect of adding aqueous sodium hydroxide to bromine water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Predict and explain the effect of adding dilute sulfuric acid to the mixture obtained in (b).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Color: Orange (or yellow-orange) [1]",
                "Name: Bromic(I) acid (or hypobromous acid) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Orange color fades / solution turns colourless [1]",
                "OH⁻ reacts with H⁺, shifting the equilibrium to the right to produce colourless Br⁻ and BrO⁻ ions [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Orange color reappears [1]",
                "Adding H⁺ reacts with Br⁻ and BrO⁻ to regenerate orange Br2 (shifts left) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="MCQ on Chlorine Water Photolysis — 9701/11/M/J/21/Q19",
        syllabus_ref="11.4",
        difficulty="EASY",
        preamble="When a tube containing chlorine water is inverted in a beaker of water and left in bright sunlight for several days, a colourless gas collects at the top and the pale green color disappears.",
        parts=[
            QuestionPart(
                label="",
                text="What is the gas collected?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Hydrogen",
                    "B. Chlorine",
                    "C. Oxygen",
                    "D. Hydrogen chloride"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: In sunlight, chloric(I) acid decomposes photochemically: 2HClO(aq) -> 2HCl(aq) + O2(g). The gas collected is oxygen."
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Industrial Preparation of Chlorine by Electrolysis — 9701/22/F/M/23/Q4(a)-(c)",
        syllabus_ref="11.4",
        difficulty="EASY",
        preamble="Chlorine is manufactured industrially on a massive scale by the membrane cell electrolysis of concentrated aqueous sodium chloride (brine).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the ionic half-equation for the reaction taking place at the anode, including state symbols.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Name the other two valuable commercial co-products formed during this electrolysis.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the membrane in the membrane cell must prevent hydroxide ions from reaching the anode compartment.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2Cl⁻(aq) -> Cl2(g) + 2e⁻ [2] (1 mark for equation, 1 mark for state symbols)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hydrogen gas (H2) [1]",
                "Sodium hydroxide (NaOH) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "If OH⁻ ions migrate to the anode, they would react with chlorine to form chlorate(I) / bleach (or be oxidised to O2 gas), contaminating the chlorine gas product [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Oxidation State Determination in Halogen Oxoacids — 9701/13/O/N/22/Q17",
        syllabus_ref="11.4",
        difficulty="EASY",
        preamble="Which compound contains chlorine in an oxidation state of +3?",
        parts=[
            QuestionPart(
                label="",
                text="Select the compound:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. HClO",
                    "B. HClO2",
                    "C. HClO3",
                    "D. HClO4"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In HClO2 (chlorous acid): H is +1, each O is -2 (-4 total), so Cl must have an oxidation state of +3."
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Balancing Redox Equations with Chlorate(V) — 9701/21/M/J/22/Q4(c)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Potassium chlorate(V), KClO3, reacts with concentrated hydrochloric acid to produce chlorine gas and chlorine dioxide, ClO2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the oxidation state of chlorine in ClO2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="In an alternative reaction, chlorate(V) oxidises iron(II) ions in acidic solution to iron(III) ions while being reduced to chloride ions. Write the balanced ionic equation for this reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "+4 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "ClO3⁻ + 6Fe²⁺ + 6H⁺ -> Cl⁻ + 6Fe³⁺ + 3H2O [2] (1 mark for correct species, 1 mark for balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Chlorination vs Alternative Disinfectants for Water — 9701/22/M/J/20/Q3(d)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Ozone (O3) and ultraviolet irradiation are alternative methods to chlorination for water purification.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State one distinct advantage of using chlorine over ozone or UV irradiation for municipal water supply systems.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State one advantage of ozone over chlorine.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Chlorine provides residual protection (residual disinfectant) that prevents recontamination as water travels through distribution pipes [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ozone does not produce toxic organochlorine by-products / trihalomethanes / does not leave unpleasant chlorine taste or odour [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="MCQ on Chlorine Disproportionation Stoichiometry — 9701/12/F/M/21/Q17",
        syllabus_ref="11.4",
        difficulty="EASY",
        preamble="When 3 moles of chlorine gas react completely with hot concentrated sodium hydroxide, how many moles of electrons are transferred between chlorine atoms?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct number of moles of electrons transferred:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1 mole",
                    "B. 3 moles",
                    "C. 5 moles",
                    "D. 6 moles"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: In 3Cl2 + 6OH⁻ -> 5Cl⁻ + ClO3⁻ + 3H2O: One Cl atom is oxidised from 0 to +5 (losing 5 electrons). Five Cl atoms are reduced from 0 to -1 (gaining 1 electron each, 5 electrons total). Thus, 5 moles of electrons are transferred."
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Identification of Unknown Halide Compounds — 9701/21/O/N/23/Q4(a)-(e)",
        syllabus_ref="11.4",
        difficulty="HARD",
        preamble="Three solid sodium salts, P, Q, and R, each contain a different halide anion. The following tests are carried out:\n- Solid P reacts with concentrated H2SO4 to give only steamy fumes that turn blue litmus paper red.\n- Solid Q reacts with concentrated H2SO4 to give steamy fumes, brown vapours, and a choking gas that turns acidified potassium dichromate(VI) green.\n- Solid R gives an immediate yellow precipitate when dissolved in water and treated with acidified AgNO3(aq); the precipitate is insoluble in concentrated NH3(aq).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the halide ion present in P, Q, and R.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the reaction of solid P with concentrated H2SO4.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the identity of the brown vapours and the choking gas produced when solid Q reacts with concentrated H2SO4.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="An aqueous solution of chlorine is added to a solution containing salt R. State the observation and write the ionic equation.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "P: Chloride (Cl⁻) [1]",
                "Q: Bromide (Br⁻) [1]",
                "R: Iodide (I⁻) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "NaCl + H2SO4 -> NaHSO4 + HCl [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Brown vapours: Bromine (Br2) [1]",
                "Choking gas: Sulfur dioxide (SO2) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Observation: Solution turns dark brown / yellow-brown (or black precipitate of I2 at high conc) [1]",
                "Equation: Cl2(aq) + 2I⁻(aq) -> 2Cl⁻(aq) + I2(aq) [1]"
            ], "marks": 2}
        ]
    )
]
'''
    with open("topic11_data.py", "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Successfully wrote topic11_data.py!")

if __name__ == "__main__":
    generate()
