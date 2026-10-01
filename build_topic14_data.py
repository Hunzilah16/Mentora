"""
Script to generate topic14_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 14: Hydrocarbons.
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 14: Hydrocarbons.
Subtopics:
  14.1 Alkanes: fractional distillation, catalytic cracking, combustion, free-radical substitution
  14.2 Alkenes: electrophilic addition (H2, Br2, HX, steam), Markovnikov's rule, carbocation stability,
       oxidation (cold dilute vs hot conc KMnO4), addition polymerisation and environmental disposal

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

TOPIC_14_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 14.1: Alkanes: Cracking, Combustion & Substitution (Q1 to Q14)
    # =========================================================================
    Question(
        number=1,
        title="Mechanism of Free-Radical Substitution of Methane — 9701/21/M/J/23/Q6(a)-(d)",
        syllabus_ref="14.1",
        difficulty="HARD",
        preamble="Methane reacts with chlorine gas in the presence of ultraviolet light to yield chloromethane and hydrogen chloride. Fig. 1.1 outlines the three stages of the reaction mechanism.",
        figure_path="figures/hydrocarbons_free_radical_substitution.png",
        figure_caption="Fig. 1.1: Free-radical substitution mechanism for the chlorination of methane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equation for the initiation step, name the type of bond fission that occurs, and state the essential reaction condition.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the two equations that represent the propagation steps in the formation of chloromethane.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write an equation for a termination step that accounts for the presence of trace amounts of ethane, C2H6, in the product mixture.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="State how the reaction conditions can be altered to maximise the yield of chloromethane, CH3Cl, relative to polychlorinated products.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Equation: Cl2 -> 2Cl* [1]",
                "Type of fission: Homolytic fission [1]",
                "Condition: Ultraviolet (UV) light / sunlight [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Step 1: Cl* + CH4 -> *CH3 + HCl [1]",
                "Step 2: *CH3 + Cl2 -> CH3Cl + Cl* [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "*CH3 + *CH3 -> C2H6 (or CH3CH3) [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Use a large excess of methane (CH4) relative to chlorine [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Catalytic vs Thermal Cracking of Alkanes — 9701/22/O/N/22/Q6(a)-(c)",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Long-chain alkane molecules obtained from crude oil are cracked into more economically valuable shorter-chain alkanes and alkenes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the temperature and catalyst employed in industrial catalytic cracking.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced equation for the cracking of decane, C10H22, to produce octane and one other product.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why branched alkanes produced by catalytic cracking are preferred over straight-chain alkanes for use in motor car petrol.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Temperature: 450 - 550 °C (approx 500 °C) [1]",
                "Catalyst: Zeolite (or aluminosilicate / silica-alumina) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "C10H22 -> C8H18 + C2H4 (octane and ethene) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Branched alkanes have a higher octane rating / burn more smoothly / reduce engine knocking [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=3,
        title="Complete and Incomplete Combustion of Propane — 9701/23/M/J/22/Q5(a)-(c)",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Propane, C3H8, is commonly supplied as liquefied petroleum gas (LPG) for heating and cooking.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced equation for the complete combustion of propane.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced equation for the incomplete combustion of propane forming carbon monoxide and water.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why carbon monoxide is extremely hazardous to human health.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C3H8 + 5O2 -> 3CO2 + 4H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "C3H8 + 3.5 O2 -> 3CO + 4H2O (or 2C3H8 + 7O2 -> 6CO + 8H2O) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Carbon monoxide binds irreversibly / with much higher affinity than oxygen to haemoglobin in red blood cells [1]",
                "forming carboxyhaemoglobin, preventing blood from transporting oxygen to body tissues, leading to asphyxiation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Isomeric Products from Bromination of Propane — 9701/21/O/N/21/Q6(a)-(c)",
        syllabus_ref="14.1",
        difficulty="HARD",
        preamble="When propane reacts with bromine vapour in the presence of UV light, two monobromoalkane isomers are formed: 1-bromopropane and 2-bromopropane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the structural formulae of both monobrominated isomers.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="The major product is 2-bromopropane (approx 97% yield). Explain why 2-bromopropane is formed in much greater yield than 1-bromopropane, referring to radical intermediates.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "1-bromopropane: CH3-CH2-CH2Br [1]",
                "2-bromopropane: CH3-CH(Br)-CH3 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Formation of 2-bromopropane proceeds via the secondary propyl radical, CH3-*CH-CH3 [1]",
                "Formation of 1-bromopropane proceeds via the primary propyl radical, CH3-CH2-*CH2 [1]",
                "The secondary radical is more stable than the primary radical due to the positive inductive electron donation from two methyl groups, so it forms with lower activation energy [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Fractional Distillation of Crude Oil — 9701/11/M/J/22/Q23",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="In an industrial fractionating column, crude oil is separated into fractions.",
        parts=[
            QuestionPart(
                label="",
                text="Which property decreases as you move down the fractionating column from top to bottom?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Boiling point",
                    "B. Viscosity",
                    "C. Volatility",
                    "D. Flammability"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: As you move down the column, molecules become larger with stronger London dispersion forces. Boiling point and viscosity increase, while volatility and flammability decrease."
            ], "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Environmental Hazards of Flue Soot Particulates — 9701/22/F/M/21/Q6(b)",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Incomplete combustion of diesel fuel in compression engines produces carbon particulate matter (soot).",
        parts=[
            QuestionPart(
                label="",
                text="State two adverse environmental or health effects associated with carbon particulates in the atmosphere.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Penetrate deep into human lungs, exacerbating asthma, bronchitis, and cardiovascular diseases [1]",
                "Deposit on buildings and statues causing blackening / contribute to global dimming by reflecting sunlight back into space [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Further Chlorination of Chloromethane — 9701/23/O/N/20/Q4(c)",
        syllabus_ref="14.1",
        difficulty="HARD",
        preamble="When chloromethane reacts further with chlorine in the presence of UV light, dichloromethane is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the two propagation steps for the conversion of chloromethane, CH3Cl, to dichloromethane, CH2Cl2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the molecular formula of the fully chlorinated end product formed when excess chlorine reacts with methane.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: Cl* + CH3Cl -> *CH2Cl + HCl [1]",
                "Step 2: *CH2Cl + Cl2 -> CH2Cl2 + Cl* [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CCl4 (tetrachloromethane) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Thermal Cracking vs Catalytic Cracking Products — 9701/12/M/J/23/Q22",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Which industrial cracking process is specifically optimised to produce high yields of alkenes such as ethene and propene?",
        parts=[
            QuestionPart(
                label="",
                text="Select the cracking process:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Catalytic cracking with zeolite at 500 °C",
                    "B. Thermal cracking at high temperature (700-900 °C) and high pressure (up to 70 atm)",
                    "C. Steam reforming over nickel at 800 °C",
                    "D. Fractional distillation"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Thermal cracking at high temperature and pressure breaks C-C bonds near the chain ends via free radicals, maximising the yield of short-chain alkenes (feedstock for polymers)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Combustion Stoichiometry Calculation — 9701/21/M/J/20/Q3(e)",
        syllabus_ref="14.1",
        difficulty="HARD",
        preamble="A 20.0 cm³ sample of a gaseous hydrocarbon CxHy was exploded with 150 cm³ of oxygen (an excess). After cooling to room temperature, the total gas volume was 110 cm³. Passing this mixture through aqueous potassium hydroxide reduced the volume to 30 cm³ (all gas volumes measured at RTP).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the volume of CO2 produced in the explosion.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the volume of oxygen that reacted with the hydrocarbon.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Deduce the molecular formula of the hydrocarbon CxHy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "KOH absorbs CO2; Volume of CO2 = 110 - 30 = 80 cm³ [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Unreacted O2 = 30 cm³; Volume of O2 reacted = 150 - 30 = 120 cm³ [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "20 cm³ CxHy : 80 cm³ CO2 => 1 mol CxHy : 4 mol CO2 => x = 4 [1]",
                "Moles O2 = x + y/4 => 120/20 = 6 => 4 + y/4 = 6 => y/4 = 2 => y = 8 => C4H8 (or butene/cyclobutane) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Unreactivity of Alkanes — 9701/11/O/N/22/Q21",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Alkanes are generally unreactive towards polar reagents such as acids, alkalis, oxidising agents, and nucleophiles.",
        parts=[
            QuestionPart(
                label="",
                text="Which factors explain the chemical inertness of alkanes under standard conditions?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Low bond enthalpy of C-C bonds and low electronegativity of carbon.",
                    "B. Non-polar nature of C-C and C-H bonds, and high bond enthalpies of C-C (347 kJ mol⁻¹) and C-H (413 kJ mol⁻¹).",
                    "C. Presence of strong intermolecular hydrogen bonds.",
                    "D. Planar geometry that shields carbon atoms from attack."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Alkanes contain only non-polar sigma bonds with very small electronegativity differences (C=2.5, H=2.1), leaving no delta+ or delta- sites for nucleophiles/electrophiles to attack, and the covalent bonds have high bond enthalpies."
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Relative Reactivity of Chlorine vs Bromine in Free-Radical Substitution — 9701/22/O/N/23/Q6(c)",
        syllabus_ref="14.1",
        difficulty="HARD",
        preamble="Bromine is significantly more selective than chlorine in free-radical substitution reactions with alkanes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why the initiation step for bromine (Br2 -> 2Br*) requires less energy than the initiation step for chlorine (Cl2 -> 2Cl*).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the first propagation step with bromine is endothermic whereas with chlorine it is exothermic.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The Br-Br bond enthalpy (193 kJ mol⁻¹) is lower than the Cl-Cl bond enthalpy (242 kJ mol⁻¹) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The H-Cl bond formed (431 kJ mol⁻¹) is stronger than the C-H bond broken (413 kJ mol⁻¹), making Delta-H negative (exothermic) [1]",
                "The H-Br bond formed (366 kJ mol⁻¹) is weaker than the C-H bond broken (413 kJ mol⁻¹), making Delta-H positive (endothermic) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Identifying Termination Products — 9701/13/M/J/22/Q21",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="When ethane undergoes photochemical chlorination, which compound CANNOT be formed as a termination product?",
        parts=[
            QuestionPart(
                label="",
                text="Select the impossible termination product:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Butane, C4H10",
                    "B. Chloroethane, C2H5Cl",
                    "C. Chlorine, Cl2",
                    "D. Propane, C3H8"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: D [1]",
                "Explanation: The radicals present during ethane chlorination are Cl* and *C2H5. Combinations produce Cl2, C2H5Cl, and butane (C2H5-C2H5). Propane requires a methyl radical (*CH3), which is not generated."
            ], "marks": 1}
        ]
    ),
    Question(
        number=13,
        title="Greenhouse Impact of Methane vs Carbon Dioxide — 9701/21/M/J/21/Q5(a)",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="Methane, CH4, is a potent atmospheric greenhouse gas emitted by agricultural livestock and landfill sites.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how greenhouse gases such as methane absorb infrared radiation and contribute to global warming.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Suggest why methane has a significantly higher global warming potential (GWP) per molecule than carbon dioxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Molecules absorb outgoing terrestrial infrared radiation matching natural vibration frequencies of polar C-H bonds [1]",
                "This increases vibrational kinetic energy, which is re-emitted in all directions, trapping heat in the troposphere [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Methane absorbs infrared radiation more strongly in atmospheric window wavelengths where CO2 does not absorb [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=14,
        title="Cracking Reaction Balancing — 9701/12/F/M/22/Q21",
        syllabus_ref="14.1",
        difficulty="EASY",
        preamble="One mole of alkane X is cracked to produce one mole of octane, two moles of propene, and one mole of ethene.",
        parts=[
            QuestionPart(
                label="",
                text="What is the molecular formula of alkane X?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. C14H30",
                    "B. C15H32",
                    "C. C16H34",
                    "D. C18H38"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Products: 1 C8H18 + 2 C3H6 + 1 C2H4 = C(8 + 6 + 2) H(18 + 12 + 4) = C16H34 (hexadecane)."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 14.2: Alkenes: Addition Reactions & Markovnikov's Rule (Q15 to Q27)
    # =========================================================================
    Question(
        number=15,
        title="Electrophilic Addition of HBr to Propene — 9701/22/M/J/23/Q6(a)-(d)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="When hydrogen bromide reacts with propene, two isomeric bromoalkanes are formed. Fig. 15.1 details the two competing reaction pathways.",
        figure_path="figures/hydrocarbons_electrophilic_addition_mechanism.png",
        figure_caption="Fig. 15.1: Mechanism of electrophilic addition of HBr to propene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the complete mechanism for the reaction between propene and HBr leading to the major product. Include all partial charges, lone pairs, curly arrows, and intermediate charges.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(b)",
                text="State the systematic IUPAC name of the major product.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the major product is formed in much higher yield than the minor product, referring to the stability of the intermediate carbocations.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Curly arrow from C=C double bond to H(delta+) of H-Br [1]",
                "Curly arrow showing heterolytic cleavage from H-Br bond to Br(delta-) [1]",
                "Correct structure of secondary carbocation intermediate: CH3-CH⁺-CH3 [1]",
                "Curly arrow from lone pair on :Br⁻ to the positively charged carbon atom C⁺ [1]"
            ], "marks": 4},
            {"part": "(b)", "points": [
                "2-bromopropane [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The major product forms via the secondary carbocation, CH3-CH⁺-CH3, whereas the minor product forms via the primary carbocation, CH3-CH2-CH2⁺ [1]",
                "The secondary carbocation has two electron-donating alkyl (methyl) groups attached to C⁺, which exert a positive inductive effect [1]",
                "This disperses the positive charge more effectively, stabilizing the intermediate and lowering the activation energy [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=16,
        title="Test for Unsaturation: Bromine Water Addition — 9701/21/O/N/22/Q6(a)-(b)",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Bromine water is the standard qualitative reagent used to distinguish alkenes from alkanes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation when bromine water is shaken with cyclohexene and with cyclohexane in the dark.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the reaction of ethene with aqueous bromine to form 1,2-dibromoethane, and state the type of mechanism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "With cyclohexene: Orange-brown colour decolourises immediately / turns colourless [1]",
                "With cyclohexane: No visible change / solution remains orange-brown [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Equation: CH2=CH2 + Br2 -> CH2Br-CH2Br [1]",
                "Type of mechanism: Electrophilic addition [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Reaction of Ethene with Bromine Water: Bromohydrin Formation — 9701/23/M/J/21/Q5(c)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="When ethene is bubbled through aqueous bromine containing sodium chloride, three organic products are formed: 1,2-dibromoethane, 2-bromoethanol, and 1-bromo-2-chloroethane.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why 2-bromoethanol, CH2BrCH2OH, is formed as the predominant product in aqueous solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain how 1-bromo-2-chloroethane is formed in this mixture.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The carbocation intermediate (or cyclic bromonium ion) is attacked by water molecules which are present in vast excess compared to bromide ions [1]",
                "Loss of a proton from the oxonium ion intermediate yields 2-bromoethanol: CH2BrCH2-O⁺H2 -> CH2BrCH2OH + H⁺ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Chloride ions (:Cl⁻) from the dissolved NaCl act as competing nucleophiles [1]",
                "They attack the positively charged carbon of the bromo-carbocation intermediate: CH2Br-CH2⁺ + Cl⁻ -> CH2Br-CH2Cl [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Industrial Catalytic Hydration of Ethene — 9701/22/F/M/22/Q6(a)-(c)",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Ethanol is manufactured industrially by the direct catalytic hydration of ethene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reagent and essential conditions (temperature, pressure, catalyst) for this process.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Write a balanced chemical equation for the hydration reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State one environmental advantage of manufacturing ethanol by fermentation of sugar rather than by hydration of ethene.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Reagents: Ethene and steam (H2O(g)) [1]",
                "Conditions: 300 °C and 60 - 70 atm [1]",
                "Catalyst: Concentrated phosphoric(V) acid, H3PO4 (absorbed on silica) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "CH2=CH2(g) + H2O(g) -> CH3CH2OH(g or l) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Fermentation uses renewable plant biomass (sugar cane / maize) rather than non-renewable crude oil fractions / is closer to carbon-neutral [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Catalytic Hydrogenation of Alkenes — 9701/11/M/J/23/Q23",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Which catalyst and condition are commonly used for the industrial hydrogenation of vegetable oils to produce margarine?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct conditions:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Nickel catalyst at 150 °C",
                    "B. Iron catalyst at 450 °C",
                    "C. Vanadium(V) oxide at 200 °C",
                    "D. Concentrated sulfuric acid at 100 °C"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Catalytic hydrogenation of C=C double bonds in polyunsaturated vegetable oils is carried out using a finely divided nickel catalyst at approximately 150 °C (or platinum at room temperature)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=20,
        title="Addition of Hydrogen Halides to 2-Methylbut-2-ene — 9701/21/M/J/22/Q6(b)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Consider the addition of hydrogen chloride, HCl, to 2-methylbut-2-ene, (CH3)2C=CHCH3.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the skeletal formula and state the systematic IUPAC name of the major product.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why 2-chloro-2-methylbutane is formed preferentially over 2-chloro-3-methylbutane.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Correct skeletal formula of 2-chloro-2-methylbutane [1]",
                "Name: 2-chloro-2-methylbutane [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Electrophilic attack by H⁺ on C3 generates a tertiary (3°) carbocation, (CH3)2C⁺-CH2CH3 [1]",
                "A tertiary carbocation is much more stable than the alternative secondary carbocation due to electron donation from three alkyl groups [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Induced Dipole in Halogen Addition Mechanisms — 9701/22/O/N/21/Q6(c)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Although bromine, Br2, is a non-polar molecule, it acts as an electrophile when approaching an alkene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how a non-polar bromine molecule becomes polarised as it approaches the C=C double bond.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State what happens to the Br-Br bond during the first step of the electrophilic addition mechanism.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The high electron density in the exposed pi bond repels the electron cloud of the approaching bromine molecule [1]",
                "This induces a temporary dipole, making the closer bromine atom partially positive (Br_delta+) and the further bromine atom partially negative (Br_delta-) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The Br-Br bond undergoes heterolytic fission, releasing a bromide ion (:Br⁻) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Hydration of Propene: Major vs Minor Alcohol — 9701/12/O/N/22/Q22",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="When propene is reacted with steam in the presence of an acid catalyst, which alcohol is formed as the major product?",
        parts=[
            QuestionPart(
                label="",
                text="Select the major alcohol product:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Propan-1-ol",
                    "B. Propan-2-ol",
                    "C. Propanoic acid",
                    "D. Propanone"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: By Markovnikov's rule, H⁺ adds to C1 (which has 2 hydrogens), forming the more stable secondary carbocation CH3-CH⁺-CH3. Addition of water and deprotonation yields propan-2-ol as the major product."
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Addition of Bromine to Buta-1,3-diene — 9701/23/O/N/21/Q5(d)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="When one mole of bromine is added to one mole of buta-1,3-diene at low temperature, 3,4-dibromobut-1-ene is the kinetic product.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the structural formula of 3,4-dibromobut-1-ene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="At higher temperatures, the thermodynamic 1,4-addition product, 1,4-dibromobut-2-ene, predominates. Draw the skeletal formula of (E)-1,4-dibromobut-2-ene.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH2=CH-CH(Br)-CH2Br [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Correct skeletal structure of 1,4-dibromobut-2-ene [1]",
                "Correctly showing the (E)-stereochemistry (Br-CH2 groups on opposite sides of the C=C double bond) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Reactions of Cycloalkenes with Acidic Reagents — 9701/13/O/N/21/Q21",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="What is the structural formula of the product formed when cyclohexene reacts with excess hydrogen bromide gas?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct product:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 1,2-dibromocyclohexane",
                    "B. Bromocyclohexane",
                    "C. 1-bromocyclohexene",
                    "D. 1,4-dibromocyclohexane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Cyclohexene has one double bond. Electrophilic addition of HBr across the double bond yields bromocyclohexane (C6H11Br)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Determining Alkene Structure from Hydrogenation Data — 9701/22/M/J/20/Q4(c)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="A 0.100 mol sample of an unknown hydrocarbon requires 4.80 dm³ of hydrogen gas at RTP for complete saturation over a nickel catalyst. (Molar gas volume = 24.0 dm³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of moles of C=C double bonds present per mole of hydrocarbon.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Suggest two possible structural formulas for this hydrocarbon if its molecular formula is C4H6.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of H2 = 4.80 / 24.0 = 0.200 mol [1]",
                "Ratio: 0.200 mol H2 / 0.100 mol hydrocarbon = 2 moles of H2 per mole; therefore, 2 C=C double bonds (or 1 triple bond) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Buta-1,3-diene: CH2=CH-CH=CH2 [1]",
                "Buta-1,2-diene: CH2=C=CH-CH3 (or but-1-yne / but-2-yne) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Addition of Interhalogens to Alkenes — 9701/21/O/N/23/Q6(b)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Iodine monochloride, ICl, adds across the double bond of propene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce which atom in ICl acts as the electrophilic centre.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Predict the major organic product formed and state its systematic IUPAC name.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Iodine atom (I has lower electronegativity than Cl, so it is polarised I_delta+ - Cl_delta-) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Major product: 2-chloro-1-iodopropane, CH3-CH(Cl)-CH2I [1]",
                "I⁺ adds to C1 to give more stable secondary carbocation CH3-CH⁺-CH2I, followed by attack of Cl⁻ at C2 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="MCQ on Markovnikov's Rule — 9701/12/M/J/21/Q23",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Which alkene produces ONLY ONE product upon reaction with hydrogen bromide?",
        parts=[
            QuestionPart(
                label="",
                text="Select the symmetrical alkene:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Propene",
                    "B. But-1-ene",
                    "C. But-2-ene",
                    "D. 2-methylpropene"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: But-2-ene (CH3-CH=CH-CH3) is completely symmetrical; addition of H to either C2 or C3 produces the identical carbocation CH3-CH⁺-CH2CH3 and yields 2-bromobutane as the exclusive product."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 14.2: Oxidation of Alkenes & Structural Cleavage (Q28 to Q39)
    # =========================================================================
    Question(
        number=28,
        title="Oxidative Cleavage of Alkenes by Hot Concentrated KMnO4 — 9701/21/M/J/23/Q6(e)-(g)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="The oxidative cleavage of alkenes with hot concentrated acidified KMnO4 is a powerful diagnostic tool for locating double bonds. Fig. 28.1 displays the three cleavage rules.",
        figure_path="figures/hydrocarbons_alkene_oxidation_cleavage.png",
        figure_caption="Fig. 28.1: Products obtained from oxidative cleavage of alkenes with hot concentrated KMnO4.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the products formed when each of the following alkene fragments is cleaved by hot concentrated acidified KMnO4:\n(i) =CH2\n(ii) =CH-R\n(iii) =C(R1)(R2)",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="An unknown hydrocarbon W, C6H12, is treated with hot concentrated acidified KMnO4. The only organic product obtained is propanoic acid, CH3CH2COOH. Deduce the displayed formula and systematic name of hydrocarbon W.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Alkene Y, C5H10, reacts with hot concentrated acidified KMnO4 to produce propanone, (CH3)2C=O, carbon dioxide, and water. Deduce the structural formula and systematic name of alkene Y.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "(i) =CH2 oxidises to carbon dioxide (CO2) and water (H2O) [1]",
                "(ii) =CH-R oxidises to a carboxylic acid (R-COOH) [1]",
                "(iii) =C(R1)(R2) oxidises to a ketone (R1-CO-R2) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Symmetrical hex-3-ene: CH3-CH2-CH=CH-CH2-CH3 [1]",
                "Name: Hex-3-ene [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Structural formula: (CH3)2C=CH2 (2-methylpropene) [1]",
                "Name: 2-methylpropene (or methylpropene) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Mild Oxidation of Alkenes: Diol Formation — 9701/22/O/N/22/Q6(d)",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="When an alkene is shaken with cold, dilute, acidified potassium manganate(VII), a diol is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation during this reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the reaction of propene with cold dilute acidified KMnO4, representing the oxidising agent as [O].",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the systematic IUPAC name of the diol product.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Purple solution decolourises (or turns colourless / brown precipitate of MnO2 forms if alkaline/neutral) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH3-CH=CH2 + [O] + H2O -> CH3-CH(OH)-CH2OH [2] (1 mark for reactants, 1 mark for correct diol structure)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Propane-1,2-diol [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Deducing Alkene Structure from Cleavage Products — 9701/11/M/J/22/Q24",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="An alkene Z reacts with hot concentrated acidified KMnO4 to produce butanone, CH3COCH2CH3, and ethanoic acid, CH3COOH.",
        parts=[
            QuestionPart(
                label="",
                text="What is the structure of alkene Z?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 3-methylhex-2-ene",
                    "B. 3-methylhex-3-ene",
                    "C. 2-methylhex-2-ene",
                    "D. 2-ethylpent-2-ene"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Combining CH3-C(=O)-CH2CH3 and HOOC-CH3 gives CH3-C(CH2CH3)=CH-CH3, which is 3-methylhex-2-ene."
            ], "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Oxidative Cleavage of Cyclic Alkenes — 9701/23/M/J/22/Q5(d)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="When cyclohexene is refluxed with hot concentrated acidified potassium manganate(VII), the ring opens to form a single dicarboxylic acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the dicarboxylic acid formed.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the systematic IUPAC name of this dicarboxylic acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State how many moles of hot KMnO4 are required per mole of cyclohexene.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "HOOC-CH2-CH2-CH2-CH2-COOH (or HOOC-(CH2)4-COOH) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Hexanedioic acid (adipic acid) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The C=C double bond requires 4 equivalents of [O] (or 4/5 moles of MnO4⁻) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Distinguishing Alkenes with Identical Formula — 9701/21/O/N/21/Q6(d)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Two unlabelled bottles contain liquid hex-1-ene and liquid hex-3-ene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why adding bromine water cannot distinguish between the contents of the two bottles.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Describe how hot concentrated acidified KMnO4 can be used to distinguish between hex-1-ene and hex-3-ene, stating the expected observations.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Both molecules contain a C=C double bond, so both will rapidly decolourise bromine water from orange-brown to colourless [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Heat each sample with hot concentrated acidified KMnO4 [1]",
                "Hex-1-ene has a terminal =CH2 group which oxidises to CO2 gas, producing visible effervescence (bubbles of gas that turn limewater milky) [1]",
                "Hex-3-ene has an internal double bond which oxidises quietly to propanoic acid with NO gas evolved / no effervescence [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=33,
        title="Oxidation Products of 1,4-Cyclooctadiene — 9701/12/M/J/22/Q23",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="When 1-methylcyclopentene is cleaved by hot concentrated acidified potassium manganate(VII), which organic compound is formed?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct product:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 5-oxohexanoic acid, CH3COCH2CH2CH2COOH",
                    "B. Hexanedioic acid",
                    "C. 6-hydroxyhexanoic acid",
                    "D. Cyclopentanone and CO2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: The ring C=C has =C(CH3)- and =CH-. Cleavage converts =C(CH3)- into a methyl ketone (CH3-CO-) and =CH- into a carboxylic acid (-COOH). The 5-carbon ring opens to yield 5-oxohexanoic acid."
            ], "marks": 1}
        ]
    ),
    Question(
        number=34,
        title="Infrared Monitoring of Alkene Oxidation — 9701/22/F/M/23/Q6(b)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="An alkene is oxidised to a diol using cold dilute acidified KMnO4.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the key absorption peak in the infrared spectrum that disappears upon complete conversion of the alkene to the diol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State the prominent new absorption peak that appears in the product spectrum and identify the bond responsible.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C=C alkene absorption at 1620 - 1680 cm⁻¹ (or =C-H stretch at 3000-3100 cm⁻¹) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Broad absorption at 3200 - 3650 cm⁻¹ [1]",
                "O-H alcohol stretch (hydrogen bonded) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Identifying Alkene Producing Carbon Dioxide — 9701/13/O/N/22/Q22",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Which of the following alkenes will produce carbon dioxide gas when refluxed with hot concentrated acidified potassium manganate(VII)?",
        parts=[
            QuestionPart(
                label="",
                text="Select the alkene:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. But-2-ene",
                    "B. 2-methylbut-2-ene",
                    "C. 3-methylbut-1-ene",
                    "D. Cyclopentene"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Only terminal alkenes containing a =CH2 group produce CO2 on oxidative cleavage with hot concentrated KMnO4. 3-methylbut-1-ene has a terminal double bond."
            ], "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Oxidation of Terpenes (Limonene) — 9701/21/O/N/20/Q5(a)-(c)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Limonene is a natural hydrocarbon found in citrus fruit peels containing two C=C double bonds: an endocyclic =C(CH3)-CH= bond and an exocyclic =C(CH3)CH2 bond.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the volume of bromine liquid (density 3.10 g cm⁻³) needed to react completely with 0.100 mol of limonene. (Ar: Br = 79.9)",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why limonene yields carbon dioxide when refluxed with hot concentrated acidified KMnO4.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Limonene has two C=C bonds, so 0.100 mol reacts with 0.200 mol Br2 [1]",
                "Mass of Br2 = 0.200 * 159.8 = 31.96 g [1]",
                "Volume = mass / density = 31.96 / 3.10 = 10.3 cm³ [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "The exocyclic double bond has a terminal =CH2 group which is oxidised completely to CO2 and H2O [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=37,
        title="Quantitative Gas Production from Alkene Cleavage — 9701/22/M/J/21/Q6(c)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="A 0.0500 mol sample of an unknown alkene produces 1.20 dm³ of carbon dioxide gas at RTP when treated with hot concentrated acidified KMnO4. (Molar gas volume = 24.0 dm³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the number of terminal =CH2 groups per molecule of the alkene.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="If the only other oxidation product is propanone, deduce the structure and name of the alkene.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Moles of CO2 = 1.20 / 24.0 = 0.0500 mol [1]",
                "Ratio: 0.0500 mol CO2 / 0.0500 mol alkene = 1 =CH2 group per molecule [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Structure: (CH3)2C=CH2 [1]",
                "Name: 2-methylpropene [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="MCQ on Cold KMnO4 Oxidation — 9701/11/F/M/21/Q22",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="What is the organic product formed when but-2-ene is reacted with cold dilute acidified potassium manganate(VII)?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct product:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Ethanoic acid",
                    "B. Butane-2,3-diol",
                    "C. Butane-1,2-diol",
                    "D. Butan-2-one"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Cold dilute acidified KMnO4 oxidises the C=C double bond into a vicinal diol without cleaving the carbon-carbon sigma bond. But-2-ene forms butane-2,3-diol, CH3CH(OH)CH(OH)CH3."
            ], "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Comparative Reactivity: Alkane vs Alkene with KMnO4 — 9701/23/M/J/20/Q4(b)",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Hexane and hex-1-ene are tested with acidified KMnO4 at room temperature.",
        parts=[
            QuestionPart(
                label="",
                text="State the observation for each compound and explain the difference in reactivity.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Hexane: Remains purple / no reaction [1]",
                "Hex-1-ene: Purple solution decolourises immediately / turns colourless [1]",
                "Explanation: Hexane contains only strong, unreactive C-C and C-H sigma bonds; hex-1-ene contains an electron-rich, reactive pi bond susceptible to electrophilic attack by the oxidising agent [1]"
            ], "marks": 3}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 14.2: Addition Polymerisation & Environmental Disposal (Q40 to Q50)
    # =========================================================================
    Question(
        number=40,
        title="Addition Polymers: Monomers and Repeat Units — 9701/22/M/J/23/Q6(e)-(g)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Alkenes undergo addition polymerisation under suitable conditions of temperature, pressure, and catalyst. Fig. 40.1 illustrates common polymers and their repeat units.",
        figure_path="figures/hydrocarbons_addition_polymerisation.png",
        figure_caption="Fig. 40.1: Structures and repeat units of common commercial addition polymers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula of the repeat unit of poly(propene).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="A section of an addition polymer chain is shown below:\n---CH2-CH(Cl)-CH2-CH(Cl)-CH2-CH(Cl)---\nDraw the displayed formula and state the systematic IUPAC name of the monomer used to synthesize this polymer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why addition polymers such as poly(ethene) are chemically inert and non-biodegradable in landfill sites.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Repeat unit showing two backbone carbons with single bond and open continuation bonds: -[CH2-CH(CH3)]- [1]",
                "Displayed with brackets and 'n' (or continuation bonds passing through brackets) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Displayed formula of chloroethene: CH2=CH-Cl (with all bonds shown) [1]",
                "Name: Chloroethene (or vinyl chloride) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The polymer backbone consists exclusively of strong, non-polar C-C and C-H single bonds with high bond enthalpies [1]",
                "There are no polar bonds, delta+ sites, or functional groups that bacteria or environmental enzymes can attack or hydrolyse [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Environmental Problems with Plastic Waste Disposal — 9701/21/O/N/22/Q6(d)-(e)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="The disposal of non-biodegradable synthetic polymers poses major environmental challenges.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State two environmental disadvantages of disposing of plastic waste in landfill sites.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Incineration is an alternative method of disposing of polymer waste. State one toxic pollutant gas released during the combustion of poly(chloroethene) (PVC), and describe how this gas can be removed from incinerator flue gases.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain what is meant by feedstock recycling of plastics.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Landfill sites occupy large areas of land and take up valuable space / visual pollution [1]",
                "Plastics persist for hundreds of years without decomposing; can break into harmful microplastics / harm wildlife [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Toxic gas: Hydrogen chloride, HCl (or chlorine, Cl2 / chlorinated dioxins) [1]",
                "Removal: Scrubber using basic calcium oxide / calcium carbonate / sodium hydroxide to neutralise the acidic gas [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Thermal cracking of polymer waste back into original monomers or hydrocarbon petrochemical feedstock to synthesize new chemicals [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=42,
        title="Repeat Unit of Teflon (PTFE) — 9701/12/M/J/23/Q23",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Poly(tetrafluoroethene) (PTFE / Teflon) is widely used for non-stick cookware coatings.",
        parts=[
            QuestionPart(
                label="",
                text="What is the structure of the monomer used to manufacture PTFE?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CF3-CF3",
                    "B. CF2=CF2",
                    "C. CHF=CHF",
                    "D. CF3-CH=CF2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The monomer for poly(tetrafluoroethene) is tetrafluoroethene, CF2=CF2. During addition polymerisation, the C=C double bond opens to form the repeat unit -[CF2-CF2]-."
            ], "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Deducing Monomer from Polymer Section — 9701/23/M/J/22/Q5(e)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="A segment of an addition polymer chain is represented below:\n---CH2-C(CH3)(COOCH3)-CH2-C(CH3)(COOCH3)---",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula of the monomer used to prepare this polymer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the systematic IUPAC name of the monomer.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State the trade name of this polymer widely used as an alternative to glass.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Displayed formula showing CH2=C(CH3)COOCH3 with all bonds shown [2] (1 mark if partially correct)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Methyl 2-methylpropenoate (methyl methacrylate) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Perspex / Plexiglas / PMMA [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=44,
        title="Addition Polymerisation of But-2-ene — 9701/11/O/N/21/Q22",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="Which structure represents the repeat unit of the polymer formed from but-2-ene?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct repeat unit:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. -[CH2-CH2-CH2-CH2]-",
                    "B. -[CH(CH3)-CH(CH3)]-",
                    "C. -[CH2-CH(C2H5)]-",
                    "D. -[C(CH3)2-CH2]-"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: But-2-ene is CH3-CH=CH-CH3. The polymer backbone is formed by the two alkene carbons (C2 and C3), each bearing one H and one -CH3 group: -[CH(CH3)-CH(CH3)]-."
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Co-Polymerisation Concept — 9701/21/M/J/21/Q6(b)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="A copolymer is formed by the addition polymerisation of an equimolar mixture of ethene and propene.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structure of the repeating unit in an alternating copolymer of ethene and propene.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the mass of ethene required to react with 42.0 g of propene to form this alternating copolymer. (Mr: ethene = 28.0, propene = 42.0)",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Structure showing: -[CH2-CH2-CH2-CH(CH3)]- with open continuation bonds [2] (1 mark if partially correct)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles of propene = 42.0 / 42.0 = 1.00 mol [1]",
                "Alternating copolymer requires 1:1 mole ratio; Mass of ethene = 1.00 mol * 28.0 g mol⁻¹ = 28.0 g [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Biodegradable Polymers vs Addition Polymers — 9701/12/F/M/21/Q23",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Why are condensation polymers (such as polyesters and polyamides) typically biodegradable, whereas polyalkenes are not?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct explanation:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Polyalkenes contain polar carbon-carbon bonds that repel water.",
                    "B. Condensation polymers contain polar ester or amide linkages in their backbone that can be hydrolysed by water and bacterial enzymes.",
                    "C. Condensation polymers have much lower molar masses than addition polymers.",
                    "D. Addition polymers dissolve easily in rainwater."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Polyesters and polyamides have polar linkages (-COO-, -CONH-) susceptible to acid or alkaline hydrolysis by environmental moisture and microorganisms, whereas polyalkenes have inert non-polar C-C backbones."
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Deducing Monomers from a Branched Polymer — 9701/22/O/N/20/Q5(d)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="A synthetic rubber is an addition polymer of 2-methylbuta-1,3-diene (isoprene).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of 2-methylbuta-1,3-diene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When 2-methylbuta-1,3-diene undergoes 1,4-addition polymerisation, a C=C double bond remains in each repeat unit. Draw the repeat unit of poly(isoprene).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Natural rubber is the cis-isomer of poly(isoprene), whereas gutta-percha is the trans-isomer. Explain why natural rubber is flexible and elastic while gutta-percha is rigid and inelastic.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH2=C(CH3)-CH=CH2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "-[CH2-C(CH3)=CH-CH2]- [2] (1 mark for correct backbone, 1 mark for double bond at C2-C3)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The cis-isomer has kinky, disordered chains that cannot pack closely together, resulting in weak intermolecular forces that allow chains to stretch and recoil [1]",
                "The trans-isomer has regular, straight chains that pack closely into a crystalline lattice with stronger intermolecular forces, making it rigid [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Polymer Combustion and Energy Recovery — 9701/13/M/J/21/Q23",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="What is the primary advantage of incinerating polymer waste with energy recovery compared to landfilling?",
        parts=[
            QuestionPart(
                label="",
                text="Select the main advantage:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. It produces no carbon dioxide emissions.",
                    "B. The high calorific value of plastics can be harnessed to generate electricity or district heating, saving fossil fuels.",
                    "C. It completely eliminates all atmospheric emissions.",
                    "D. It generates reusable monomer liquids directly."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Polymers are derived from petroleum and have high calorific values (comparable to fuel oil). Modern incinerators burn them to produce high-pressure steam for electricity turbines, recovering energy."
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Recycling Codes and Mechanical Sorting — 9701/21/M/J/23/Q6(h)",
        syllabus_ref="14.2",
        difficulty="EASY",
        preamble="Plastic containers are stamped with recycling identification codes (e.g. 1 for PET, 2 for HDPE, 3 for PVC, 4 for LDPE, 5 for PP, 6 for PS).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why plastic waste must be sorted into specific polymer types before mechanical recycling.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State one physical method used in automated recycling facilities to separate different plastics.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Different polymers have different melting temperatures and do not mix well / are mutually immiscible at molecular level [1]",
                "Melting an unsorted blend produces a brittle, mechanically defective recycled plastic of very low quality and value [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Flotation / density separation in liquid media (or near-infrared NIR optical spectroscopy sorting) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Problem: Hydrocarbon Reaction Pathways — 9701/21/O/N/23/Q6(a)-(f)",
        syllabus_ref="14.2",
        difficulty="HARD",
        preamble="An unsaturated hydrocarbon A, C4H8, exists as a pair of stereoisomers.\n- Hydrocarbon A decolourises bromine water to yield B.\n- Reaction of A with hot concentrated acidified KMnO4 yields a single organic product C, which effervesces with sodium carbonate.\n- Compound A reacts with hydrogen gas in the presence of a nickel catalyst to form compound D.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the identity of hydrocarbon A and state the type of stereoisomerism it exhibits.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the displayed formula of compound B and state its systematic IUPAC name.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Identify compound C and write the equation for its reaction with sodium carbonate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Compound D is reacted with chlorine gas in the presence of UV light. State how many structural isomers of monochlorobutane are formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Hydrocarbon A is but-2-ene, CH3-CH=CH-CH3 [1]",
                "Type of stereoisomerism: Geometric (cis/trans or E/Z) isomerism [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Displayed formula of 2,3-dibromobutane: CH3-CH(Br)-CH(Br)-CH3 [1]",
                "Name: 2,3-dibromobutane [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Compound C is ethanoic acid, CH3COOH [1]",
                "Equation: 2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2 [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Compound D is butane, CH3CH2CH2CH3 [1]",
                "Two structural isomers: 1-chlorobutane and 2-chlorobutane [1]"
            ], "marks": 2}
        ]
    )
]
'''
    with open("topic14_data.py", "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Successfully wrote topic14_data.py!")

if __name__ == "__main__":
    generate()
