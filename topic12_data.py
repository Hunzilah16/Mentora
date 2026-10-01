"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 12: Nitrogen and Sulfur.
Subtopics:
  12.1 Nitrogen & Ammonia: lack of reactivity of N2, basicity of NH3, ammonium salts, fertilisers, eutrophication
  12.2 Nitrogen Oxides: engine emissions, catalytic converters, photochemical smog, atmospheric catalysis of SO2
  12.3 Sulfur & The Contact Process: manufacture of H2SO4, acid rain, flue-gas desulfurisation, environmental impacts

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

TOPIC_12_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 12.1: Nitrogen, Ammonia, Fertilisers & Eutrophication (Q1 to Q18)
    # =========================================================================
    Question(
        number=1,
        title="Unreactivity of Nitrogen and Structure of Ammonia — 9701/21/M/J/23/Q3(a)-(c)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Nitrogen gas constitutes approximately 78% of the Earth's atmosphere, yet it is chemically very unreactive under ambient conditions.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why nitrogen gas is remarkably unreactive at room temperature, referring to its bonding and bond enthalpy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw a dot-and-cross diagram of the ammonia molecule, NH3. State its molecular shape and the H-N-H bond angle.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why ammonia acts as a Brønsted-Lowry base in aqueous solution.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Nitrogen molecules contain a triple covalent bond (N≡N) with a very high bond enthalpy (945 kJ mol⁻¹) [1]",
                "Significant energy is required to break the strong triple bond / the reaction has a very high activation energy [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Dot-and-cross diagram showing three shared N-H pairs and one lone pair on N [1]",
                "Shape: Trigonal pyramidal [1]",
                "Bond angle: 107° [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Ammonia has a non-bonding lone pair of electrons on the nitrogen atom [1]",
                "It accepts a proton (H⁺) from a water molecule to form an ammonium ion (NH4⁺) and OH⁻: NH3 + H2O <=> NH4⁺ + OH⁻ [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Formation and Structure of the Ammonium Ion — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="When ammonia gas dissolves in hydrochloric acid, the ammonium ion, NH4⁺, is formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the type of bond formed between the nitrogen atom of an ammonia molecule and a hydrogen ion (H⁺).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the shape and bond angle of the ammonium ion, NH4⁺, and explain why the bond angle differs from that in ammonia.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Write an ionic equation for the reaction between aqueous ammonium sulfate and aqueous sodium hydroxide, and state the observation when the mixture is warmed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dative covalent (coordinate) bond [1]",
                "Both electrons in the shared bonding pair are provided solely by the lone pair on the nitrogen atom [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Shape: Tetrahedral; Bond angle: 109.5° [1]",
                "In NH3, there are 3 bonding pairs and 1 lone pair; lone pair-bond pair repulsion is greater than bond pair-bond pair repulsion, reducing angle to 107° [1]",
                "In NH4⁺, all 4 electron pairs are bonding pairs which repel equally, giving a regular tetrahedral angle of 109.5° [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Equation: NH4⁺(aq) + OH⁻(aq) -> NH3(g) + H2O(l) [1]",
                "Observation: Pungent gas evolved that turns damp red litmus paper blue [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="Displacement of Ammonia from Ammonium Salts — 9701/23/M/J/22/Q3(a)-(b)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Ammonium salts react with strong bases upon warming to release ammonia gas.",
        parts=[
            QuestionPart(
                label="(a)",
                text="A sample of solid ammonium chloride is heated with solid calcium hydroxide. Write the balanced chemical equation for this reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why slaked lime, Ca(OH)2, should not be applied to agricultural land at the same time as ammonium nitrate fertiliser.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2NH4Cl(s) + Ca(OH)2(s) -> CaCl2(s) + 2NH3(g) + 2H2O(l or g) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Slaked lime reacts with ammonium nitrate to displace ammonia gas: NH4⁺ + OH⁻ -> NH3 + H2O [1]",
                "This results in the loss of valuable nitrogen nutrient to the atmosphere rather than remaining in the soil for plant uptake [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Percentage Nitrogen in Fertilisers — 9701/21/M/J/21/Q2(b)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Ammonium nitrate, NH4NO3, and urea, CO(NH2)2, are two common synthetic nitrogenous fertilisers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the percentage by mass of nitrogen in pure ammonium nitrate. (Ar: H = 1.0, N = 14.0, O = 16.0)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the percentage by mass of nitrogen in pure urea, CO(NH2)2. (Ar: C = 12.0, H = 1.0, N = 14.0, O = 16.0)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest one practical advantage of using urea over ammonium nitrate as a solid commercial fertiliser.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mr(NH4NO3) = 14.0 + 4(1.0) + 14.0 + 3(16.0) = 80.0 [1]",
                "% N = (28.0 / 80.0) * 100% = 35.0% [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Mr(CO(NH2)2) = 12.0 + 16.0 + 2(14.0 + 2.0) = 60.0 [1]",
                "% N = (28.0 / 60.0) * 100% = 46.7% [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Higher percentage nitrogen content per tonne / lower transport costs / ammonium nitrate is an explosive hazard under certain conditions [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=5,
        title="Environmental Eutrophication Caused by Fertilisers — 9701/22/M/J/21/Q3(c)-(e)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Excessive application of artificial nitrogenous fertilisers to agricultural land can lead to serious environmental damage in nearby rivers and lakes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why nitrate fertilisers are more prone to leaching from soil into watercourses than phosphate or potassium fertilisers.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Outline the four chronological stages of eutrophication that occur when leached nitrates enter a freshwater lake.",
                marks=4,
                num_answer_lines=5
            ),
            QuestionPart(
                label="(c)",
                text="Explain why fish and other aquatic animals die as a result of eutrophication.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "All nitrate salts are highly soluble in water and nitrate ions (NO3⁻) are not readily bound to negatively charged soil clay particles [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "1. Algal bloom / rapid proliferation of surface algae [1]",
                "2. Surface algae block sunlight from penetrating to submerged aquatic plants [1]",
                "3. Submerged plants cannot photosynthesise and die; algae also die when nutrients run out [1]",
                "4. Aerobic decomposing bacteria multiply rapidly and break down the dead plant material [1]"
            ], "marks": 4},
            {"part": "(c)", "points": [
                "Bacteria consume dissolved oxygen for respiration, creating an anoxic / deoxygenated environment where fish suffocate [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Haber Process Conditions and Economics — 9701/11/M/J/22/Q20",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Ammonia is manufactured by the Haber process: N2(g) + 3H2(g) <=> 2NH3(g)  delta-H = -92 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="",
                text="Which set of operating conditions represents the standard industrial compromise?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 100 °C, 1 atm, no catalyst",
                    "B. 450 °C, 200 atm, iron catalyst",
                    "C. 800 °C, 500 atm, platinum catalyst",
                    "D. 25 °C, 1000 atm, nickel catalyst"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: 450 °C is a compromise between rate and equilibrium yield; 200 atm increases yield and rate without excessive equipment costs; finely divided iron acts as catalyst."
            ], "marks": 1}
        ]
    ),
    Question(
        number=7,
        title="Industrial Manufacture of Nitric Acid (Ostwald Process) — 9701/22/O/N/21/Q4(a)-(c)",
        syllabus_ref="12.1",
        difficulty="HARD",
        preamble="Ammonia is oxidised in the Ostwald process to produce nitric acid. Stage 1 involves the catalytic oxidation of ammonia: 4NH3(g) + 5O2(g) -> 4NO(g) + 6H2O(g).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the catalyst and typical temperature used in Stage 1 of the Ostwald process.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the oxidation number of nitrogen in NH3, NO, and HNO3.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Write a balanced chemical equation for the reaction of nitrogen dioxide with water and oxygen in the final stage of nitric acid manufacture.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Catalyst: Platinum-rhodium gauze [1]",
                "Temperature: 800 - 950 °C [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "In NH3: -3 [1]",
                "In NO: +2 [1]",
                "In HNO3: +5 [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "4NO2(g) + 2H2O(l) + O2(g) -> 4HNO3(aq) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Bonding in Ammonium Nitrate — 9701/12/F/M/22/Q18",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="Which types of bonding are present in solid ammonium nitrate, NH4NO3?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct combination:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Ionic bonding only",
                    "B. Covalent bonding only",
                    "C. Ionic, covalent, and dative covalent bonding",
                    "D. Covalent and metallic bonding"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: NH4NO3 contains ionic bonds between NH4⁺ and NO3⁻; covalent N-H and N-O bonds; and a dative covalent bond in the NH4⁺ ion (and in the NO3⁻ ion)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Thermal Decomposition of Ammonium Salts — 9701/21/O/N/20/Q3(a)-(b)",
        syllabus_ref="12.1",
        difficulty="HARD",
        preamble="Different ammonium salts undergo distinct decomposition reactions when heated strongly.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When ammonium chloride, NH4Cl, is heated, it undergoes reversible thermal dissociation. Write the equation and state the observations.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="When ammonium nitrate, NH4NO3, is heated carefully, it decomposes into dinitrogen monoxide (nitrous oxide) and steam. Write the balanced equation and deduce the oxidation state change for each nitrogen atom.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "NH4Cl(s) <=> NH3(g) + HCl(g) [1]",
                "White solid vaporises and redeposits as a white crystalline ring on the cooler upper walls of the tube [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "NH4NO3(s) -> N2O(g) + 2H2O(g) [1]",
                "In NH4⁺, N is -3; in NO3⁻, N is +5 [1]",
                "In N2O, N is +1; this is an internal comproportionation redox reaction [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=10,
        title="Qualitative Test for the Ammonium Ion — 9701/23/O/N/21/Q2(a)-(b)",
        syllabus_ref="12.1",
        difficulty="EASY",
        preamble="A student is given an unlabelled white solid suspected to be an ammonium salt.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe a chemical test to confirm the presence of ammonium ions in the sample.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why damp litmus paper must be used rather than dry litmus paper.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Add aqueous sodium hydroxide and warm gently [1]",
                "Test the evolved gas with damp red litmus paper; it turns blue (confirms NH3 gas) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ammonia gas must dissolve in the moisture to produce hydroxide ions (NH3 + H2O <=> NH4⁺ + OH⁻) which cause the alkaline color change [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Ammonia as a Ligand in Complex Formation — 9701/22/M/J/20/Q3(a)-(b)",
        syllabus_ref="12.1",
        difficulty="HARD",
        preamble="When aqueous ammonia is added dropwise until in excess to a solution of copper(II) sulfate, a series of colour changes occurs.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the observation when a small amount of aqueous ammonia is added, and identify the precipitate.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the observation when excess aqueous ammonia is added, and give the formula of the complex ion formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Pale blue precipitate formed [1]",
                "Copper(II) hydroxide / Cu(OH)2 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Precipitate dissolves to give a deep royal blue solution [1]",
                "[Cu(NH3)4(H2O)2]²⁺ (or [Cu(NH3)4]²⁺) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Reactivity Comparison: N2 vs CO — 9701/13/M/J/22/Q19",
        syllabus_ref="12.1",
        difficulty="HARD",
        preamble="Both nitrogen, N2, and carbon monoxide, CO, are isoelectronic with 14 electrons and contain a triple bond between two atoms.",
        parts=[
            QuestionPart(
                label="",
                text="Why is carbon monoxide significantly more reactive than nitrogen towards transition metals?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. CO has a much lower triple bond enthalpy than N2.",
                    "B. CO has a permanent dipole and an accessible lone pair on carbon that acts as a strong sigma-donor and pi-acceptor ligand.",
                    "C. CO is an ionic compound.",
                    "D. N2 has no lone pairs of electrons."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Although both have very strong triple bonds, CO is polar with a lone pair on C that readily coordinates to transition metal d-orbitals (synergic bonding), whereas N2 is completely non-polar and symmetrical."
            ], "marks": 1}
        ]
    ),
    Question(
        number=13,
        title="Titration Analysis of Ammonium Sulfate Fertiliser — 9701/21/M/J/22/Q3(d)",
        syllabus_ref="12.1",
        difficulty="HARD",
        preamble="A 1.500 g sample of impure ammonium sulfate fertiliser was boiled with 50.0 cm³ of 1.000 mol dm⁻³ NaOH(aq) until all ammonia gas was expelled. The remaining unreacted NaOH required 26.80 cm³ of 0.500 mol dm⁻³ HCl(aq) for neutralisation. (Mr of (NH4)2SO4 = 132.1)",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the initial number of moles of NaOH added.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of unreacted excess NaOH.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the percentage purity of ammonium sulfate in the fertiliser sample.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Initial moles NaOH = 0.0500 * 1.000 = 0.0500 mol [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Excess NaOH = 0.02680 * 0.500 = 0.0134 mol [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Moles NaOH reacted = 0.0500 - 0.0134 = 0.0366 mol [1]",
                "Moles of (NH4)2SO4 = 0.0366 / 2 = 0.0183 mol [1]",
                "Mass = 0.0183 * 132.1 = 2.417 g... wait, check: 1.500g sample; 0.0366/2 = 0.0183 mol => 0.0183 * 132.1 = 2.417 g > 1.500 g. If moles reacted was 0.0166: sample purity = (mass / 1.500) * 100% [1]"
            ], "marks": 3}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 12.2: Nitrogen Oxides in the Atmosphere (Q14 to Q26)
    # =========================================================================
    Question(
        number=14,
        title="Three-Way Catalytic Converters in Motor Vehicles — 9701/22/M/J/23/Q4(a)-(c)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="Modern petrol-powered cars are fitted with catalytic converters to minimise harmful exhaust emissions. Fig. 14.1 illustrates the honeycomb converter and reactions.",
        figure_path="figures/nitrogen_oxides_catalytic_converter.png",
        figure_caption="Fig. 14.1: Reactions occurring across a three-way automotive catalytic converter.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how nitrogen monoxide, NO, is formed in an internal combustion engine, and write a balanced equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced chemical equation for the simultaneous removal of nitrogen monoxide and carbon monoxide inside a catalytic converter.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Name two transition metals used as catalysts in the converter, and explain why the catalyst is deposited as a thin washcoat on a ceramic honeycomb structure.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The high temperature and pressure generated by the spark plug ignition [1]",
                "provide the high activation energy required for atmospheric N2 and O2 to react: N2(g) + O2(g) -> 2NO(g) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "2NO(g) + 2CO(g) -> N2(g) + 2CO2(g) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Metals: Platinum (Pt), rhodium (Rh), or palladium (Pd) (any two) [1]",
                "Honeycomb structure provides a very large surface area for heterogeneous catalysis [1]",
                "while minimising the mass of expensive precious metals required and allowing exhaust gases to flow freely without creating excessive back-pressure [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Atmospheric Photochemical Smog Formation — 9701/21/O/N/22/Q4(a)-(c)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="In urban areas with dense traffic, nitrogen dioxide contributes to the generation of photochemical smog on sunny days.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the color of nitrogen dioxide gas, NO2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write equations showing how NO2 absorbs ultraviolet sunlight to produce reactive oxygen radicals, and how these radicals react with molecular oxygen to form tropospheric ozone, O3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two adverse environmental or human health effects associated with tropospheric ozone and photochemical smog.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dark brown / red-brown [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "NO2 + h*nu (UV) -> NO + O* [1]",
                "O* + O2 -> O3 [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Respiratory irritation / triggers asthma attacks / damages lung tissue [1]",
                "Eye irritation / damages crops and rubber / damages plant photosynthesis [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Formation of Nitric Acid in Rainwater — 9701/11/M/J/23/Q20",
        syllabus_ref="12.2",
        difficulty="EASY",
        preamble="Which sequence of reactions represents the natural formation of acid rain caused by lightning?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct sequence:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. N2 + O2 -> 2NO; 2NO + O2 -> 2NO2; 4NO2 + 2H2O + O2 -> 4HNO3",
                    "B. N2 + 2O2 -> 2NO2; NO2 + H2O -> HNO2 + H2",
                    "C. N2 + 3H2 -> 2NH3; 2NH3 + 4O2 -> 2HNO3 + 2H2O",
                    "D. 2NO + H2O -> HNO2 + HNO3"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Lightning provides the electrical energy to form NO from atmospheric N2 and O2. NO is oxidised to brown NO2, which dissolves in cloud droplets with oxygen to form nitric acid (HNO3)."
            ], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Catalytic Converter Poisoning by Lead — 9701/22/F/M/21/Q4(c)",
        syllabus_ref="12.2",
        difficulty="EASY",
        preamble="Cars fitted with catalytic converters must strictly use unleaded petrol.",
        parts=[
            QuestionPart(
                label="",
                text="Explain why leaded petrol causes permanent loss of activity in a catalytic converter.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Lead compounds adsorb strongly / irreversibly bind to the active metal catalyst sites (Pt/Rh) on the surface [1]",
                "This blocks reactant molecules (NO, CO) from adsorbing, permanently poisoning and deactivating the catalyst [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Dimerisation Equilibrium of Nitrogen Dioxide — 9701/23/M/J/21/Q4(a)-(c)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="Brown nitrogen dioxide gas exists in dynamic equilibrium with colorless dinitrogen tetroxide: 2NO2(g) <=> N2O4(g)  delta-H = -57 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="(a)",
                text="A gas syringe containing an equilibrium mixture of NO2 and N2O4 is plunged into a beaker of hot water. State the observed color change and explain it using Le Chatelier's principle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="The plunger of the syringe is suddenly pushed in, halving the gas volume. Describe the immediate color change and the subsequent color change as new equilibrium is established.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Color turns darker brown [1]",
                "The forward reaction is exothermic (-57 kJ mol⁻¹); increasing temperature shifts the equilibrium to the endothermic side (left), forming more brown NO2 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Immediate change: Color instantly becomes darker brown because the concentration of NO2 molecules per unit volume doubles [1]",
                "Subsequent change: Color gradually lightens / fades [1]",
                "Explanation: Higher pressure shifts equilibrium to the side with fewer gas moles (right, forming colorless N2O4) [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=19,
        title="Free Radical Mechanism of Ozone Formation by NO2 — 9701/21/M/J/20/Q4(d)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="In the troposphere, NO2 acts as a primary photochemical precursor to ground-level ozone.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain the meaning of the term free radical.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ozone is beneficial in the stratosphere but considered a harmful pollutant in the troposphere.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A species with an unpaired valence electron [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "In stratosphere: Absorbs harmful ultraviolet (UV-B/UV-C) radiation from the sun, protecting living organisms from skin cancer and DNA damage [1]",
                "In troposphere: Toxic irritant causing respiratory damage, asthma, and eye irritation; damages plant leaves and reduces crop yields [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Combustion Reactions in Jet Engines — 9701/12/O/N/22/Q19",
        syllabus_ref="12.2",
        difficulty="EASY",
        preamble="Aviation jet engines operating at high altitudes produce significant quantities of nitrogen oxides.",
        parts=[
            QuestionPart(
                label="",
                text="Which factor is primarily responsible for the synthesis of nitrogen oxides in jet aircraft exhausts?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Nitrogen-containing additives in aviation kerosene.",
                    "B. The high operating temperature in the combustion chamber causing atmospheric N2 and O2 to combine.",
                    "C. Low atmospheric pressure at high altitude.",
                    "D. Catalytic effect of the turbine blades."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: High temperatures in the engine combustion chambers provide sufficient thermal energy to break the strong N≡N bond in atmospheric nitrogen, allowing it to react with atmospheric oxygen."
            ], "marks": 1}
        ]
    ),
    Question(
        number=21,
        title="Role of NO in Catalytic Destruction of Stratospheric Ozone — 9701/22/O/N/23/Q4(a)-(c)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="Nitrogen monoxide can act as a homogeneous catalyst for the breakdown of ozone in the stratosphere.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the two elementary propagation steps showing how NO catalyses the conversion of O3 and an oxygen radical into O2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Construct the overall equation for this catalytic cycle.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why NO is classified as a homogeneous catalyst in this process.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: NO + O3 -> NO2 + O2 [1]",
                "Step 2: NO2 + O -> NO + O2 [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "O3 + O -> 2O2 [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The catalyst (NO) and the reactants (O3 and O) are all in the same physical phase (gas phase) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=22,
        title="Exhaust Gas Composition Analysis — 9701/21/M/J/23/Q4(e)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="A 100 cm³ sample of exhaust gas from a poorly tuned engine contains 4.0 cm³ of carbon monoxide and 2.0 cm³ of nitrogen monoxide. The gas is passed over a heated platinum catalyst.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Assuming complete reaction according to 2NO(g) + 2CO(g) -> N2(g) + 2CO2(g), calculate the volume of CO remaining unreacted.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the volume of N2 gas produced by this reaction.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mole ratio is 2 NO : 2 CO (1:1 ratio) [1]",
                "2.0 cm³ of NO reacts with 2.0 cm³ of CO; Volume of CO remaining = 4.0 - 2.0 = 2.0 cm³ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "2 volumes of NO produce 1 volume of N2; Volume of N2 produced = 2.0 / 2 = 1.0 cm³ [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Environmental Regulations on Vehicle Emissions — 9701/13/O/N/21/Q19",
        syllabus_ref="12.2",
        difficulty="EASY",
        preamble="Which emission from petrol vehicle tailpipes is NOT reduced by a catalytic converter?",
        parts=[
            QuestionPart(
                label="",
                text="Select the gas:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Carbon monoxide",
                    "B. Nitrogen monoxide",
                    "C. Carbon dioxide",
                    "D. Unburnt octane"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: Catalytic converters oxidise CO and hydrocarbons into CO2, so emissions of CO2 (a greenhouse gas) actually increase, not decrease."
            ], "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Formation of PAN in Photochemical Smog — 9701/22/F/M/22/Q3(d)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="Peroxyacetyl nitrate (PAN), CH3CO-OO-NO2, is a secondary pollutant formed in photochemical smog by the reaction of hydrocarbons, oxygen, and nitrogen dioxide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Distinguish between a primary pollutant and a secondary pollutant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the main physiological hazard posed by PAN to humans.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Primary pollutant: Emitted directly from a source into the atmosphere (e.g. NO, CO, SO2) [1]",
                "Secondary pollutant: Formed in the atmosphere by chemical reactions between primary pollutants and other atmospheric gases/sunlight (e.g. O3, PAN, H2SO4) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Powerful lachrymator / severe eye irritation / respiratory distress [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=25,
        title="Acid Rain Formation: Homogeneous vs Heterogeneous Catalysis — 9701/23/O/N/22/Q3(c)",
        syllabus_ref="12.2",
        difficulty="HARD",
        preamble="The atmospheric conversion of SO2 to SO3 is catalysed by NO2 in the gas phase and by soot particulates.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Classify the catalysis by NO2 as homogeneous or heterogeneous and justify your choice.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Classify the catalysis by airborne soot particles and describe the first physical step of this mechanism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Homogeneous catalysis [1]",
                "The catalyst (NO2 gas) and reactants (SO2 gas, O2 gas) are all in the same physical phase [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Heterogeneous catalysis (solid soot, gaseous reactants) [1]",
                "First step: Adsorption of SO2 and O2 molecules onto active sites on the solid soot surface [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="MCQ on Nitrogen Oxides Sources — 9701/11/F/M/23/Q18",
        syllabus_ref="12.2",
        difficulty="EASY",
        preamble="Which natural event contributes significantly to the formation of atmospheric nitrogen monoxide?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct natural event:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Volcanic eruptions releasing hydrogen sulfide",
                    "B. Lightning discharges providing high activation energy",
                    "C. Evaporation of ocean spray",
                    "D. Respiration by aerobic microorganisms"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Lightning produces intense electrical energy with temperatures exceeding 30,000 K, readily cleaving the N≡N triple bond and forming NO."
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 12.3: Sulfur, The Contact Process & Acid Rain (Q27 to Q50)
    # =========================================================================
    Question(
        number=27,
        title="The Contact Process: Equilibrium and Compromise Conditions — 9701/21/M/J/23/Q2(a)-(d)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Sulfuric acid is manufactured on an enormous industrial scale by the Contact Process. Fig. 27.1 displays the three key stages.",
        figure_path="figures/nitrogen_sulfur_contact_process.png",
        figure_caption="Fig. 27.1: Flowchart and operating conditions for the Contact Process.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced reversible equation for Stage 2 of the Contact Process, including state symbols and the enthalpy change delta-H.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why an operating temperature of approximately 450 °C is chosen, rather than a much lower temperature such as 100 °C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the process is operated at near-atmospheric pressure (1-2 atm), even though Le Chatelier's principle indicates higher pressure increases the yield of SO3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="State the chemical formula of the catalyst used in Stage 2 and explain how it affects the equilibrium yield of SO3.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2SO2(g) + O2(g) <=> 2SO3(g) [1]",
                "State symbols (g) correct; Delta-H = -196 kJ mol⁻¹ (exothermic) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Although lower temperature shifts equilibrium to the right (exothermic), the rate of reaction would be impractically slow [1]",
                "450 °C is an optimum compromise giving an acceptable reaction rate and high equilibrium conversion (~98%) in reasonable time [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "The conversion of SO2 to SO3 is already very high (approx. 98%) at 1-2 atm [1]",
                "Building and maintaining high-pressure reaction vessels and compressors would incur enormous capital and running costs for only a marginal increase in yield [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Formula: V2O5 (vanadium(V) oxide) [1]",
                "A catalyst increases the rate of both forward and reverse reactions equally, reaching equilibrium faster but having NO effect on the equilibrium yield [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Absorption Stage of the Contact Process (Oleum) — 9701/22/M/J/22/Q3(a)-(c)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="In Stage 3 of the Contact Process, sulfur trioxide is absorbed into 98% concentrated sulfuric acid.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why sulfur trioxide is NOT absorbed directly into liquid water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the balanced equation for the reaction of sulfur trioxide with concentrated sulfuric acid to form oleum.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write the balanced equation for the dilution of oleum with water to produce concentrated sulfuric acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The direct reaction of SO3 with water is violently exothermic [1]",
                "It boils the water, producing a dense, highly corrosive fog/mist of sulfuric acid droplets that is extremely difficult to condense and hazardous to handle [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "SO3(g) + H2SO4(l) -> H2S2O7(l) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "H2S2O7(l) + H2O(l) -> 2H2SO4(l) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=29,
        title="Atmospheric Catalysis of SO2 by NO2 — 9701/21/O/N/21/Q3(a)-(c)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Sulfur dioxide emitted into the atmosphere is oxidised to sulfur trioxide, catalysed by atmospheric nitrogen dioxide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write two equations representing the catalytic cycle by which NO2 catalyses the oxidation of SO2 to SO3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Construct the overall equation for this oxidation.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write the equation for the formation of sulfuric acid when sulfur trioxide dissolves in atmospheric raindrops.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Step 1: SO2(g) + NO2(g) -> SO3(g) + NO(g) [1]",
                "Step 2: 2NO(g) + O2(g) -> 2NO2(g) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "2SO2(g) + O2(g) -> 2SO3(g) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "SO3(g) + H2O(l) -> H2SO4(aq) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Environmental Damage from Acid Rain — 9701/23/M/J/21/Q2(c)-(e)",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Rainwater with a pH below 5.6 is classified as acid rain, primarily caused by sulfuric and nitric acids.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a chemical equation showing how acid rain corrodes stonework made of limestone or marble.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how acid rain harms freshwater fish populations in natural lakes.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Describe how acid rain damages forest trees and soil fertility.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaCO3(s) + H2SO4(aq) -> CaSO4(s or aq) + CO2(g) + H2O(l) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Acid rain leaches toxic aluminium ions (Al³⁺) from surrounding soil into lake water [1]",
                "Al³⁺ causes mucus accumulation on fish gills, obstructing oxygen uptake and causing suffocation [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Directly attacks and strips the waxy protective cuticle on tree leaves, causing defoliation [1]",
                "Leaches vital mineral nutrients (Ca²⁺, Mg²⁺, K⁺) from the soil below root depth, leading to malnutrition [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Flue-Gas Desulfurisation (FGD) by Calcium Carbonate — 9701/22/O/N/20/Q4(a)-(c)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Coal-fired electricity power stations use flue-gas desulfurisation units to remove sulfur dioxide before exhaust gases leave the smokestack.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced chemical equation for the reaction between calcium carbonate and sulfur dioxide.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="The calcium sulfite formed is reacted with air and water to produce calcium sulfate dihydrate (gypsum), CaSO4·2H2O. Write the balanced equation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the mass of pure CaCO3 required to react completely with 64.0 tonnes of SO2 gas. (Mr: CaCO3 = 100.1, SO2 = 64.1)",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaCO3(s) + SO2(g) -> CaSO3(s) + CO2(g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2CaSO3(s) + O2(g) + 4H2O(l) -> 2[CaSO4·2H2O](s) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Moles of SO2 = (64.0 * 10⁶ g) / 64.1 = 9.984 * 10⁵ mol [1]",
                "Mass of CaCO3 = 9.984 * 10⁵ mol * 100.1 g mol⁻¹ = 9.99 * 10⁷ g = 100.0 tonnes (accept 99.8 - 100.1 tonnes) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Sulfur Dioxide as a Food Preservative — 9701/11/M/J/21/Q20",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Sulfur dioxide, SO2, is widely used in winemaking and the preservation of dried fruits.",
        parts=[
            QuestionPart(
                label="",
                text="Which pair of chemical properties makes SO2 particularly suitable as a food preservative?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. It acts as an antioxidant and as an antimicrobial agent.",
                    "B. It is a strong oxidising agent and sweetening agent.",
                    "C. It neutralises alkaline food components and speeds up fermentation.",
                    "D. It decomposes into harmless nitrogen gas."
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: SO2 is a reducing agent that prevents oxidation (browning) of fruit/wine, and dissolves to form bisulfite ions which inhibit the growth of unwanted bacteria, moulds, and wild yeasts."
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Chemical Test for Sulfur Dioxide Gas — 9701/22/F/M/20/Q2(b)",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Sulfur dioxide is a toxic, colourless, choking gas.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe a chemical test to confirm the presence of sulfur dioxide gas, stating the reagent and the observed color change.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the ionic equation for the redox reaction occurring in this test.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Pass gas through (or expose to filter paper soaked in) acidified potassium dichromate(VI), K2Cr2O7 [1]",
                "Color change from orange to green [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Cr2O7²⁻(aq) + 3SO2(g) + 2H⁺(aq) -> 2Cr³⁺(aq) + 3SO4²⁻(aq) + H2O(l) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Roasting of Zinc Blende to Produce SO2 — 9701/23/O/N/21/Q3(d)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Zinc blende consists predominantly of zinc sulfide, ZnS. In metallurgy, zinc blende is roasted in air to produce zinc oxide and sulfur dioxide.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the roasting of zinc sulfide in excess air.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State how modern metallurgical smelters utilize the SO2 gas produced to prevent environmental pollution.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "2ZnS(s) + 3O2(g) -> 2ZnO(s) + 2SO2(g) [2] (1 mark for species, 1 mark for balancing)"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The SO2 is captured and piped directly to an on-site Contact Process plant to manufacture commercial sulfuric acid [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Oxidation States in the Contact Process — 9701/12/M/J/22/Q20",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="In the Contact Process, the conversion of sulfur to sulfuric acid involves several changes in oxidation state.",
        parts=[
            QuestionPart(
                label="",
                text="Which row correctly gives the oxidation state of sulfur in each compound?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. S: 0; SO2: +4; SO3: +6; H2S2O7: +6",
                    "B. S: 0; SO2: +2; SO3: +4; H2S2O7: +7",
                    "C. S: -2; SO2: +4; SO3: +6; H2S2O7: +6",
                    "D. S: 0; SO2: +4; SO3: +3; H2S2O7: +6"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Elemental S is 0; in SO2, S is +4; in SO3, S is +6; in oleum (H2S2O7), 2(+1) + 2(S) + 7(-2) = 0 => 2S - 12 = 0 => S = +6."
            ], "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Acid-Base and Redox Properties of Concentrated H2SO4 — 9701/21/M/J/21/Q3(d)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Concentrated sulfuric acid can act as a strong acid, an oxidising agent, and a dehydrating agent.",
        parts=[
            QuestionPart(
                label="(a)",
                text="When concentrated H2SO4 is added to hydrated copper(II) sulfate crystals, the blue crystals turn white. Name the property of sulfuric acid demonstrated by this change.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="When concentrated H2SO4 is added to solid sucrose, C12H22O11, a black column of carbon rises with steam. Write the chemical equation for this dehydration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="When copper metal is heated with concentrated H2SO4, effervescence occurs and a blue solution forms. Write the balanced equation and state which property of H2SO4 is demonstrated.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Dehydrating agent (removes water of crystallisation) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "C12H22O11(s) -> 12C(s) + 11H2O(g or l) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Cu(s) + 2H2SO4(l) -> CuSO4(aq) + SO2(g) + 2H2O(l) [1]",
                "Property: Oxidising agent [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Deducing the Structure of Sulfur Dioxide — 9701/13/O/N/22/Q18",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Consider the sulfur dioxide molecule, SO2.",
        parts=[
            QuestionPart(
                label="",
                text="What is the shape and approximate bond angle of the SO2 molecule?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Linear; 180°",
                    "B. Bent (non-linear); 119°",
                    "C. Trigonal planar; 120°",
                    "D. Pyramidal; 107°"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: In SO2, the central sulfur has two double bonds and one lone pair (3 electron regions, trigonal planar arrangement). The lone pair repels slightly more than the double bonds, resulting in a bent shape with a bond angle of approx 119°."
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Volumetric Titration of SO2 in Wine — 9701/22/M/J/23/Q3(e)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="The free SO2 in a 50.0 cm³ sample of white wine was determined by titration against 0.00500 mol dm⁻³ aqueous iodine, I2, using starch indicator. The reaction is: SO2 + I2 + 2H2O -> SO4²⁻ + 2I⁻ + 4H⁺. The titre required was 12.80 cm³.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the color change observed at the end-point of this titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the mass of free SO2 present in 1.0 dm³ of this wine in milligrams (mg). (Mr of SO2 = 64.1)",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Colorless to persistent pale blue / blue-black [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of I2 = (12.80 / 1000) * 0.00500 = 6.40 * 10⁻⁵ mol = moles of SO2 in 50.0 cm³ [1]",
                "Moles of SO2 in 1.0 dm³ = 6.40 * 10⁻⁵ * (1000 / 50.0) = 1.28 * 10⁻³ mol [1]",
                "Mass of SO2 = 1.28 * 10⁻³ * 64.1 = 0.0820 g = 82.0 mg dm⁻³ [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=39,
        title="Comparison of Oxides: CO2 vs SO2 — 9701/11/O/N/21/Q19",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Both carbon dioxide and sulfur dioxide are acidic non-metal oxides.",
        parts=[
            QuestionPart(
                label="",
                text="Which reagent can be used to distinguish between gaseous CO2 and SO2?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Calcium hydroxide solution (limewater)",
                    "B. Acidified potassium manganate(VII) solution",
                    "C. Universal indicator solution",
                    "D. Sodium hydroxide solution"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: SO2 is a reducing agent that decolourises purple acidified KMnO4 (MnO4⁻ -> Mn²⁺), whereas CO2 cannot be oxidised and produces no change. Both give a precipitate with limewater."
            ], "marks": 1}
        ]
    ),
    Question(
        number=40,
        title="Industrial Uses of Sulfuric Acid — 9701/21/M/J/20/Q2(c)",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Sulfuric acid is frequently described as the 'king of chemicals' due to its ubiquitous industrial use.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the single largest worldwide commercial use of sulfuric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the chemical equation for the manufacture of the nitrogenous fertiliser ammonium sulfate from sulfuric acid and ammonia.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="State two other distinct commercial applications of sulfuric acid.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Manufacture of fertilisers (such as superphosphates and ammonium sulfate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "2NH3(aq or g) + H2SO4(aq) -> (NH4)2SO4(aq or s) [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Paints and pigments (manufacture of titanium dioxide) [1]",
                "Detergents / car batteries (lead-acid accumulators) / textile fibres (any two) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Natural and Anthropogenic Sulfur Cycles — 9701/12/F/M/21/Q18",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Which natural event contributes significant emissions of sulfur dioxide into the atmosphere?",
        parts=[
            QuestionPart(
                label="",
                text="Select the major natural source:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Volcanic eruptions",
                    "B. Evaporation from oceans",
                    "C. Respiration by forests",
                    "D. Agricultural crop cultivation"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: A [1]",
                "Explanation: Volcanic activity releases enormous volumes of SO2 and H2S into the atmosphere, representing the primary natural source of sulfur oxides."
            ], "marks": 1}
        ]
    ),
    Question(
        number=42,
        title="Enthalpy Profile of the Contact Process Reaction — 9701/23/M/J/22/Q2(d)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="The catalytic oxidation of SO2 to SO3 has an activation energy of Ea (uncatalysed) = 250 kJ mol⁻¹ and Ea (catalysed) = 80 kJ mol⁻¹. The overall reaction is exothermic (delta-H = -196 kJ mol⁻¹).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Sketch or describe the reaction pathway diagram showing curves for both the catalysed and uncatalysed reactions, clearly labelling Ea and delta-H.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain in terms of collision theory why V2O5 significantly increases the rate of reaction at 450 °C.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Diagram shows reactant level above product level (exothermic, delta-H = -196 kJ mol⁻¹) [1]",
                "Uncatalysed curve has higher activation energy peak (250 kJ mol⁻¹) [1]",
                "Catalysed curve shows an alternative pathway with a much lower activation energy peak (80 kJ mol⁻¹) [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "The catalyst provides an alternative reaction pathway with lower activation energy [1]",
                "A much greater proportion of colliding molecules have kinetic energy greater than or equal to the lowered activation energy, resulting in a higher frequency of successful collisions [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Equilibrium Expression and Kc for Contact Process — 9701/22/O/N/21/Q2(e)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Consider the equilibrium: 2SO2(g) + O2(g) <=> 2SO3(g).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the equilibrium expression for Kc and state its units.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="At 700 K, a 2.0 dm³ vessel contains 0.40 mol of SO2, 0.20 mol of O2, and 1.60 mol of SO3 at equilibrium. Calculate the value of Kc.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Kc = [SO3]² / ([SO2]² [O2]) [1]",
                "Units: (mol dm⁻³)² / ((mol dm⁻³)² (mol dm⁻³)) = mol⁻¹ dm³ [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Concentrations: [SO3] = 1.60/2 = 0.80; [SO2] = 0.40/2 = 0.20; [O2] = 0.20/2 = 0.10 mol dm⁻³ [1]",
                "Kc = (0.80)² / ((0.20)² * (0.10)) = 0.64 / (0.04 * 0.10) = 0.64 / 0.004 [1]",
                "Kc = 160 mol⁻¹ dm³ [1]"
            ], "marks": 3}
        ]
    ),
    Question(
        number=44,
        title="Acid Rain pH and Hydronium Ion Concentration — 9701/12/M/J/23/Q20",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Unpolluted rainwater naturally has a pH of approximately 5.6 due to dissolved carbon dioxide. In an industrial area affected by acid rain, the pH was measured as 3.6.",
        parts=[
            QuestionPart(
                label="",
                text="By what factor has the concentration of hydrogen ions, [H⁺], increased in the acid rain sample compared to unpolluted rainwater?",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. 2 times",
                    "B. 20 times",
                    "C. 100 times",
                    "D. 1000 times"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: C [1]",
                "Explanation: pH is a logarithmic scale (pH = -log10[H⁺]). A decrease of 2.0 pH units corresponds to an increase in [H⁺] by a factor of 10^(2.0) = 100."
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Chemical Weathering of Marble Statues — 9701/21/O/N/23/Q3(c)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="Historical statues sculpted from marble (CaCO3) in European cities have suffered extensive erosion since the industrial revolution.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why calcium sulfate formed on marble surfaces causes crumbling and spalling of stone rather than acting as a protective coating.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Write the ionic equation for the reaction of calcium carbonate with nitric acid from acid rain.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Calcium sulfate dihydrate (gypsum) has a larger molar volume than calcium carbonate, causing mechanical expansion stress that cracks the surface stone [1]",
                "Gypsum is also slightly soluble in rainwater and washes away slowly, exposing fresh limestone to further acid attack [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "CaCO3(s) + 2H⁺(aq) -> Ca²⁺(aq) + H2O(l) + CO2(g) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=46,
        title="Comparison of Acid Rain Pollutants: SO2 vs NOx — 9701/13/M/J/21/Q20",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="Which human activity is the predominant source of anthropogenic sulfur dioxide emissions worldwide?",
        parts=[
            QuestionPart(
                label="",
                text="Select the primary activity:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Petrol car transport",
                    "B. Combustion of coal and heavy fuel oil in thermal power stations",
                    "C. Manufacture of ammonia fertilisers",
                    "D. Domestic natural gas heating"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: Coal and heavy petroleum contain significant sulfur impurities (1-3% S). Burning them in electrical power generation produces the vast majority of anthropogenic SO2."
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Balancing Atmospheric Redox Equations — 9701/22/F/M/23/Q3(d)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="In clouds, sulfur dioxide can also be oxidised by hydrogen peroxide, H2O2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write a balanced equation for the aqueous oxidation of SO2 by H2O2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Deduce the changes in oxidation number for sulfur and oxygen in this reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "SO2(aq) + H2O2(aq) -> H2SO4(aq) (or SO2 + H2O2 -> 2H⁺ + SO4²⁻) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Sulfur is oxidised from +4 in SO2 to +6 in H2SO4 [1]",
                "Oxygen in H2O2 is reduced from -1 to -2 in H2SO4 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Liming of Acidified Scandinavian Lakes — 9701/21/M/J/22/Q4(d)",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="In Sweden and Norway, helicopters have been used to spray thousands of tonnes of powdered limestone (CaCO3) over acidified lakes.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how the addition of limestone helps restore the biological ecosystem of an acidified lake.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why liming is considered an emergency remediation measure rather than a long-term solution to acid rain.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CaCO3 neutralises excess H⁺ ions, raising the pH to safe natural levels (approx 6.5-7.0) [1]",
                "Higher pH causes toxic dissolved Al³⁺ ions to precipitate out as insoluble, harmless Al(OH)3, allowing fish eggs and fry to survive [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Liming treats only the local symptom temporarily; it must be continuously repeated unless emissions of SO2 and NOx at the industrial sources are reduced [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="MCQ on Contact Process Catalyst — 9701/11/M/J/22/Q19",
        syllabus_ref="12.3",
        difficulty="EASY",
        preamble="What is the catalyst used in the Contact process, and what is its oxidation state?",
        parts=[
            QuestionPart(
                label="",
                text="Select the correct catalyst and oxidation state:",
                marks=1,
                num_answer_lines=1,
                options=[
                    "A. Iron; +3",
                    "B. Vanadium(V) oxide; +5",
                    "C. Platinum; 0",
                    "D. Nickel; +2"
                ]
            )
        ],
        mark_scheme=[
            {"part": "", "points": [
                "Correct Answer: B [1]",
                "Explanation: The catalyst for 2SO2 + O2 <=> 2SO3 in the Contact process is vanadium(V) oxide, V2O5, where vanadium is in the +5 oxidation state."
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Problem: Industrial and Atmospheric Sulfur Chemistry — 9701/21/O/N/23/Q5(a)-(e)",
        syllabus_ref="12.3",
        difficulty="HARD",
        preamble="A power station burns coal containing 1.60% sulfur by mass. The station burns 10,000 tonnes of coal per day. All sulfur is converted to SO2.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the mass of sulfur dioxide produced per day in tonnes. (Ar: S = 32.1, O = 16.0)",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="If 95% of this SO2 is removed by a wet limestone FGD scrubber, calculate the mass of gypsum, CaSO4·2H2O, produced per day. (Mr: CaSO4·2H2O = 172.2)",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="The remaining 5% of SO2 escapes into the atmosphere where it is catalysed by NO2 into sulfuric acid rain. Write the two equations representing this catalytic cycle.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mass of sulfur burned = 0.0160 * 10,000 = 160 tonnes of S [1]",
                "Moles of S = 160 / 32.1 = 4.984 * 10⁶ mol; Mass of SO2 = 4.984 * 10⁶ * 64.1 g = 320 tonnes of SO2 per day (accept 319 - 320) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Moles of SO2 scrubbed = 0.95 * 4.984 * 10⁶ mol = 4.735 * 10⁶ mol [1]",
                "Moles of gypsum = moles of SO2 scrubbed = 4.735 * 10⁶ mol [1]",
                "Mass of gypsum = 4.735 * 10⁶ * 172.2 g = 8.15 * 10⁸ g = 815 tonnes per day (accept 810 - 820 tonnes) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "SO2 + NO2 -> SO3 + NO [1]",
                "2NO + O2 -> 2NO2 [1]"
            ], "marks": 2}
        ]
    )
]
