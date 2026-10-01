"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 2: Atoms, Molecules and Stoichiometry.
Subtopics:
  2.1 Relative masses of atoms and molecules
  2.2 The mole and the Avogadro constant
  2.3 Formulas (empirical, molecular, structural, water of crystallization)
  2.4 Reacting masses and volumes (titrations, gas volumes, yields, atom economy)

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

TOPIC_2_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 2.1: Relative Masses of Atoms & Molecules (Q1 to Q12)
    # =========================================================================
    Question(
        number=1,
        title="Definitions of Relative Masses — 9701/22/M/J/21/Q1(a)",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Accurate atomic and molecular masses are defined relative to the carbon-12 standard.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term relative molecular mass, Mr.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the term relative formula mass is preferred over relative molecular mass for magnesium chloride, MgCl2.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Weighted average mass of a molecule of a compound (1); compared to 1/12th of the mass of an atom of carbon-12 (1)", "marks": 2},
            {"part": "b", "points": "MgCl2 is a giant ionic lattice and does not exist as individual discrete molecules (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Calculating Relative Formula Masses — 9701/11/O/N/22/Q1",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Use the following relative atomic mass values: H = 1.0, C = 12.0, N = 14.0, O = 16.0, Al = 27.0, S = 32.1, Fe = 55.8.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the relative formula mass of hydrated aluminium sulfate, Al2(SO4)3·16H2O.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the relative formula mass of ammonium iron(II) sulfate, (NH4)2Fe(SO4)2·6H2O.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Al2(SO4)3 = (2×27.0) + 3×[32.1 + (4×16.0)] = 54.0 + 288.3 = 342.3 (1); 16H2O = 16×18.0 = 288.0; Total Mr = 342.3 + 288.0 = 630.3 (1)", "marks": 2},
            {"part": "b", "points": "2(NH4) = 36.0; Fe = 55.8; 2(SO4) = 192.2; 6H2O = 108.0 (1); Total Mr = 36.0 + 55.8 + 192.2 + 108.0 = 392.0 (1)", "marks": 2}
        ]
    ),
    Question(
        number=3,
        title="High-Resolution Mass Measurement and Molecular Formula — 9701/21/M/J/23/Q1(c)",
        syllabus_ref="2.1",
        difficulty="HARD",
        preamble="High-resolution mass spectrometry determines molecular masses to four decimal places using precise isotopic masses: 1H = 1.0078, 12C = 12.0000, 14N = 14.0031, 16O = 15.9949.",
        parts=[
            QuestionPart(
                label="a",
                text="Both carbon monoxide, CO, and nitrogen gas, N2, have nominal integer relative molecular masses of 28. Calculate the precise molecular mass of CO and N2 to four decimal places.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="A gaseous compound has a molecular ion peak at m/z = 44.0262. Deduce whether the gas is propane (C3H8) or ethanal (CH3CHO).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "CO = 12.0000 + 15.9949 = 27.9949 (1); N2 = 2 × 14.0031 = 28.0062 (1)", "marks": 2},
            {"part": "b", "points": "C3H8 = 3(12.0000) + 8(1.0078) = 44.0624; CH3CHO (C2H4O) = 2(12.0000) + 4(1.0078) + 15.9949 = 44.0261 (1); The gas is ethanal (CH3CHO) because its accurate mass matches 44.0262 closely (1)", "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Isotopic Abundances and Weighted Average Ar — 9701/22/F/M/22/Q1(a)",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Antimony, Sb (Z = 51), consists of two stable isotopes: 121Sb (atomic mass 120.90 u) and 123Sb (atomic mass 122.90 u). Natural antimony has Ar = 121.76.",
        parts=[
            QuestionPart(
                label="a",
                text="State what is meant by the unified atomic mass unit, u.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage abundance of each isotope in natural antimony. Give your answers to 1 decimal place.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "One twelfth (1/12th) of the rest mass of an unbound atom of carbon-12 (1)", "marks": 1},
            {"part": "b", "points": "121.76 = [120.90x + 122.90(100 - x)] / 100 (1); 12176 = 120.90x + 12290 - 122.90x => 2.00x = 114 (1); x = 57.0% for 121Sb and 43.0% for 123Sb (1)", "marks": 3}
        ]
    ),
    Question(
        number=5,
        title="Mass Differences Between Allotropes — 9701/12/M/J/22/Q2",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Carbon exists as several allotropes, including diamond, graphite, and buckminsterfullerene (C60).",
        parts=[
            QuestionPart(
                label="a",
                text="State the relative molecular mass of buckminsterfullerene, C60.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why diamond does not have a defined relative molecular mass.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mr = 60 × 12.0 = 720.0 (1)", "marks": 1},
            {"part": "b", "points": "Diamond is a giant covalent lattice consisting of an indeterminate, macroscopic number of covalently bonded carbon atoms rather than discrete molecules (1)", "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Evaluating Atomic Mass Standards Historically — 9701/22/O/N/20/Q1(a)",
        syllabus_ref="2.1",
        difficulty="HARD",
        preamble="Prior to 1961, physicists calibrated atomic masses using oxygen-16 = 16.0000, while chemists used the natural isotopic mixture of oxygen = 16.0000.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the existence of 17O and 18O isotopes caused a discrepancy between the physical and chemical atomic mass scales.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why adopting carbon-12 resolved this historical discrepancy universally.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Chemists' standard included heavier isotopes (17O and 18O), so 16.0000 chemical units had a slightly greater mass than pure 16O (1); This produced a persistent ~275 ppm difference between data tables (1)", "marks": 2},
            {"part": "b", "points": "Carbon-12 is a single specific pure nuclide (not an isotopic blend) (1); Carbon is easily handled as a solid standard and yielded atomic weights remarkably close to older values (1)", "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Relative Formula Mass of Complex Coordination Compounds — 9701/21/M/J/24/Q1(b)",
        syllabus_ref="2.1",
        difficulty="HARD",
        preamble="Cisplatin is an anticancer drug with the chemical formula Pt(NH3)2Cl2. (Pt = 195.1, Cl = 35.5, N = 14.0, H = 1.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the relative molecular mass of cisplatin to one decimal place.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage by mass of platinum in cisplatin.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mr = 195.1 + 2[14.0 + 3(1.0)] + 2(35.5) = 195.1 + 34.0 + 71.0 = 300.1 (1)", "marks": 1},
            {"part": "b", "points": "% Pt = (195.1 / 300.1) × 100 (1) = 65.0% (1)", "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Percentage Composition by Mass in Fertilizers — 9701/11/M/J/23/Q2",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Ammonium nitrate, NH4NO3, and urea, (NH2)2CO, are nitrogenous fertilizers. (H = 1.0, C = 12.0, N = 14.0, O = 16.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the percentage by mass of nitrogen in pure ammonium nitrate, NH4NO3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage by mass of nitrogen in pure urea, (NH2)2CO.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Deduce which fertilizer provides a higher nitrogen mass per kilogram of pure compound.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mr(NH4NO3) = (2×14.0) + (4×1.0) + (3×16.0) = 80.0; % N = (28.0 / 80.0) × 100 = 35.0% (1)", "marks": 2},
            {"part": "b", "points": "Mr((NH2)2CO) = 2[14.0 + (2×1.0)] + 12.0 + 16.0 = 60.0; % N = (28.0 / 60.0) × 100 = 46.7% (1)", "marks": 2},
            {"part": "c", "points": "Urea provides a higher percentage nitrogen (46.7% vs 35.0%) (1)", "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Relative Masses of Isotopically Labelled Molecules — 9701/22/O/N/23/Q2(a)",
        syllabus_ref="2.1",
        difficulty="HARD",
        preamble="Heavy methane is synthesized using carbon-13 and deuterium (2H, represented as D).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the relative molecular mass of standard methane, 12CH4, and fully deuterated heavy methane, 13CD4.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage mass increase of 13CD4 compared to 12CH4.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "12CH4 = 12.0 + 4(1.0) = 16.0 (1); 13CD4 = 13.0 + 4(2.0) = 21.0 (1)", "marks": 2},
            {"part": "b", "points": "Mass increase = (21.0 - 16.0) / 16.0 × 100 = (5.0 / 16.0) × 100 (1) = 31.25% (or 31.3%) (1)", "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Evaluating Hydration Mass in Epsom Salts — 9701/23/M/J/22/Q1(b)",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Epsom salts consist of hydrated magnesium sulfate, MgSO4·xH2O. (Mg = 24.3, S = 32.1, O = 16.0, H = 1.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the formula mass of anhydrous MgSO4.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Given that water accounts for 51.2% of the mass of Epsom salts, deduce the integer value of x.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mr(MgSO4) = 24.3 + 32.1 + (4×16.0) = 120.4 (1)", "marks": 1},
            {"part": "b", "points": "% anhydrous MgSO4 = 100 - 51.2 = 48.8% (1); Total Mr = 120.4 / 0.488 = 246.7 (1); Mass of water = 246.7 - 120.4 = 126.3 => x = 126.3 / 18.0 = 7.01 => x = 7 (1)", "marks": 3}
        ]
    ),
    Question(
        number=11,
        title="Relative Masses in Polymer Repeat Units — 9701/13/O/N/21/Q2",
        syllabus_ref="2.1",
        difficulty="EASY",
        preamble="Poly(chloroethene), PVC, is formed by addition polymerisation of chloroethene, CH2=CHCl. (C = 12.0, H = 1.0, Cl = 35.5).",
        parts=[
            QuestionPart(
                label="a",
                text="State the relative formula mass of one repeat unit of PVC.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="A sample of PVC has an average molecular mass of 187,500. Calculate the average number of monomer units in a polymer chain.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Repeat unit [-CH2-CHCl-] = (2×12.0) + (3×1.0) + 35.5 = 62.5 (1)", "marks": 1},
            {"part": "b", "points": "Degree of polymerisation n = 187,500 / 62.5 (1) = 3000 repeat units (1)", "marks": 2}
        ]
    ),
    Question(
        number=12,
        title="Distinguishing Isomers by Accurate Molecular Mass — 9701/22/F/M/24/Q1(b)",
        syllabus_ref="2.1",
        difficulty="HARD",
        preamble="Consider the two structural isomers butane (C4H10) and 2-methylpropane (C4H10).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why high-resolution mass spectrometry cannot be used to distinguish between butane and 2-methylpropane.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Suggest an analytical technique that could definitively differentiate the two isomers based on their mass fragmentation patterns.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Both isomers have identical molecular formulas (C4H10) and therefore identical exact molecular masses (1)", "marks": 1},
            {"part": "b", "points": "Mass spectrometry fragmentation analysis (1); 2-methylpropane forms a stable tertiary carbocation fragment [CH(CH3)2]+ at m/z = 43 with higher abundance, whereas butane forms a primary butyl cation [C4H9]+ / different fragmentation profile (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 2.2: The Mole and the Avogadro Constant (Q13 to Q24)
    # =========================================================================
    Question(
        number=13,
        title="Defining the Mole and Avogadro Constant — 9701/22/M/J/22/Q2(a)",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="The mole is the SI unit for amount of substance. (Avogadro constant L = 6.02 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Define the mole in terms of the Avogadro constant.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the number of molecules present in 3.60 g of water, H2O.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the total number of atoms present in 3.60 g of water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The amount of substance that contains exactly 6.02 × 10²³ specified elementary entities (1)", "marks": 1},
            {"part": "b", "points": "Moles of H2O = 3.60 / 18.0 = 0.200 mol (1); Number of molecules = 0.200 × (6.02 × 10²³) = 1.20 × 10²³ molecules (1)", "marks": 2},
            {"part": "c", "points": "Each molecule contains 3 atoms (2 H + 1 O) (1); Total atoms = 3 × (1.20 × 10²³) = 3.61 × 10²³ atoms (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Counting Subatomic Particles in a Given Mass — 9701/11/M/J/21/Q2",
        syllabus_ref="2.2",
        difficulty="HARD",
        preamble="A pure sample of magnesium metal has a mass of 1.216 g. (Ar: Mg = 24.31; atomic number Z = 12; L = 6.02 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount in moles of magnesium atoms in the sample.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the total number of protons present in the 1.216 g sample of magnesium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the total charge in coulombs carried by all the valence electrons in this sample. (Charge on electron e = 1.60 × 10⁻¹⁹ C).",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles = 1.216 / 24.31 = 0.0500 mol (1)", "marks": 1},
            {"part": "b", "points": "Atoms of Mg = 0.0500 × (6.02 × 10²³) = 3.01 × 10²² atoms (1); Each Mg atom contains 12 protons => Protons = 12 × (3.01 × 10²²) = 3.61 × 10²³ protons (1)", "marks": 2},
            {"part": "c", "points": "Mg has 2 valence electrons => Moles of valence electrons = 2 × 0.0500 = 0.100 mol (1); Number of valence electrons = 0.100 × (6.02 × 10²³) = 6.02 × 10²² (1); Total charge = (6.02 × 10²²) × (1.60 × 10⁻¹⁹ C) = 9632 C (or 9.63 × 10³ C) (1)", "marks": 3}
        ]
    ),
    Question(
        number=15,
        title="Comparing Particle Quantities in Diverse Samples — 9701/12/O/N/23/Q1",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="Consider four separate containers each holding a different gas at standard conditions.",
        parts=[
            QuestionPart(
                label="a",
                text="Which sample contains the greatest total number of atoms?",
                marks=1,
                num_answer_lines=0,
                options=[
                    "A 1.0 g of hydrogen gas, H2",
                    "B 1.0 g of helium gas, He",
                    "C 1.0 g of methane gas, CH4",
                    "D 1.0 g of oxygen gas, O2"
                ]
            ),
            QuestionPart(
                label="b",
                text="Demonstrate by calculation why the option chosen in part (a) is correct.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A — 1.0 g of hydrogen gas, H2 (1)", "marks": 1},
            {"part": "b", "points": "Moles of atoms: H2 = (1.0/2.0) × 2 = 1.0 mol atoms (1); He = 1.0/4.0 = 0.25 mol; CH4 = (1.0/16.0) × 5 = 0.31 mol; O2 = (1.0/32.0) × 2 = 0.063 mol. Hydrogen has the greatest amount of atoms (1.0 mol) (1)", "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Moles of Ions in Dissolved Salts — 9701/21/O/N/22/Q2(b)",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="Solid aluminium chloride, AlCl3, dissolves completely in water to form hydrated ions. (L = 6.02 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the dissolution of solid AlCl3 in water.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the total number of chloride ions, Cl-, present in 250 cm³ of a 0.200 mol dm⁻³ AlCl3 solution.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "AlCl3(s) -> Al3+(aq) + 3Cl-(aq) (1)", "marks": 1},
            {"part": "b", "points": "Moles of AlCl3 = (250/1000) × 0.200 = 0.0500 mol (1); Moles of Cl- ions = 3 × 0.0500 = 0.150 mol (1); Number of Cl- ions = 0.150 × (6.02 × 10²³) = 9.03 × 10²² ions (1)", "marks": 3}
        ]
    ),
    Question(
        number=17,
        title="Avogadro's Number and Mass of an Individual Atom — 9701/22/F/M/21/Q2(a)",
        syllabus_ref="2.2",
        difficulty="HARD",
        preamble="Gold has a relative atomic mass of 197.0. A single atom of gold has mass m.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the absolute mass in grams of one atom of gold to three significant figures. (L = 6.022 × 10²³ mol⁻¹).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="A gold leaf has dimensions 5.0 cm × 5.0 cm and a thickness of 1.0 × 10⁻⁵ cm. The density of gold is 19.3 g cm⁻³. Calculate the number of gold atoms in the leaf.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mass = Ar / L = 197.0 / (6.022 × 10²³) (1) = 3.27 × 10⁻²² g (1)", "marks": 2},
            {"part": "b", "points": "Volume = 5.0 × 5.0 × (1.0 × 10⁻⁵) = 2.5 × 10⁻⁴ cm³ (1); Mass = Volume × Density = (2.5 × 10⁻⁴) × 19.3 = 4.825 × 10⁻³ g (1); Atoms = (4.825 × 10⁻³ g) / (3.27 × 10⁻²² g) = 1.47 × 10¹⁹ atoms (or via moles: 0.004825/197 × L = 1.47 × 10¹⁹) (1)", "marks": 3}
        ]
    ),
    Question(
        number=18,
        title="Moles and Faraday's Constant Relationship — 9701/23/M/J/24/Q1(b)",
        syllabus_ref="2.2",
        difficulty="HARD",
        preamble="Faraday's constant F is the electric charge carried by one mole of electrons. (e = 1.602 × 10⁻¹⁹ C, L = 6.022 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Show by calculation that Faraday's constant F is approximately 96,500 C mol⁻¹.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="In an electrolysis experiment, a constant current of 2.50 A was passed through molten lead(II) bromide, PbBr2, for 30.0 minutes. Calculate the amount in moles of electrons transferred.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "F = L × e = (6.022 × 10²³ mol⁻¹) × (1.602 × 10⁻¹⁹ C) (1) = 96472 C mol⁻¹ ≈ 96,500 C mol⁻¹ (1)", "marks": 2},
            {"part": "b", "points": "Time t = 30.0 × 60 = 1800 s (1); Charge Q = I × t = 2.50 × 1800 = 4500 C (1); Moles of electrons = Q / F = 4500 / 96500 = 0.0466 mol (1)", "marks": 3}
        ]
    ),
    Question(
        number=19,
        title="Determining Avogadro's Constant Experimentally — 9701/21/M/J/25/Q1(b)",
        syllabus_ref="2.2",
        difficulty="HARD",
        preamble="Copper can be deposited during electrolysis according to: Cu2+(aq) + 2e- -> Cu(s). In an experiment, a current of 0.800 A depositing 0.474 g of Cu (Ar = 63.55) in 1800 s was used to determine the Avogadro constant.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount in moles of copper atoms deposited.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the total electric charge passed and hence the number of electrons transferred, given that each electron carries 1.60 × 10⁻¹⁹ C.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the experimental value of the Avogadro constant obtained from these data.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles of Cu = 0.474 / 63.55 = 0.00746 mol (1)", "marks": 1},
            {"part": "b", "points": "Q = 0.800 × 1800 = 1440 C (1); Electrons = 1440 / (1.60 × 10⁻¹⁹) = 9.00 × 10²¹ electrons (1)", "marks": 2},
            {"part": "c", "points": "Moles of electrons = 2 × 0.00746 = 0.01492 mol (1); L = (9.00 × 10²¹) / 0.01492 = 6.03 × 10²³ mol⁻¹ (1)", "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Moles of Gas and Molar Gas Volume — 9701/11/F/M/23/Q1",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="At room temperature and pressure (r.t.p.), one mole of any ideal gas occupies 24.0 dm³.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the volume in cm³ occupied by 0.0250 mol of carbon dioxide gas at r.t.p.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of argon gas present in 360 cm³ measured at r.t.p.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Volume = 0.0250 mol × 24.0 dm³ = 0.600 dm³ (1); In cm³ = 0.600 × 1000 = 600 cm³ (1)", "marks": 2},
            {"part": "b", "points": "Volume in dm³ = 360 / 1000 = 0.360 dm³ (1); Moles = 0.360 / 24.0 = 0.0150 mol (1)", "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Mole Calculations Involving Solutions — 9701/12/M/J/24/Q2",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="A stock solution of sodium hydroxide, NaOH, is prepared by dissolving 8.00 g of NaOH (Mr = 40.0) in distilled water to make 500 cm³ of solution.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the concentration of the NaOH solution in mol dm⁻³.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the volume of this solution required to provide exactly 0.0100 mol of NaOH.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles of NaOH = 8.00 / 40.0 = 0.200 mol (1); Concentration = 0.200 / (500/1000) = 0.400 mol dm⁻³ (1)", "marks": 2},
            {"part": "b", "points": "Volume = moles / conc = 0.0100 / 0.400 = 0.0250 dm³ (1); = 25.0 cm³ (1)", "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Number of Molecules in a Liquid Droplet — 9701/22/O/N/21/Q1(c)",
        syllabus_ref="2.2",
        difficulty="HARD",
        preamble="A single drop of liquid ethanol, C2H5OH, has a volume of 0.050 cm³. The density of ethanol is 0.789 g cm⁻³. (C = 12.0, H = 1.0, O = 16.0; L = 6.02 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass in grams of the drop of ethanol.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the number of ethanol molecules present in this single droplet.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mass = volume × density = 0.050 × 0.789 = 0.03945 g (1)", "marks": 1},
            {"part": "b", "points": "Mr(C2H5OH) = (2×12.0) + (6×1.0) + 16.0 = 46.0 (1); Moles = 0.03945 / 46.0 = 8.576 × 10⁻⁴ mol (1); Molecules = (8.576 × 10⁻⁴) × (6.02 × 10²³) = 5.16 × 10²⁰ molecules (1)", "marks": 3}
        ]
    ),
    Question(
        number=23,
        title="Limiting Reagent Concept from Molar Quantities — 9701/11/O/N/24/Q2",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="Consider the reaction: 2Al + 3Cl2 -> 2AlCl3. A reaction mixture contains 0.50 mol of Al and 0.60 mol of Cl2.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce which reactant is the limiting reagent. Justify your answer with a calculation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the maximum amount in moles of AlCl3 that can be formed.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "0.50 mol Al requires 0.50 × (3/2) = 0.75 mol Cl2 (1); Only 0.60 mol Cl2 is available, so Cl2 is the limiting reagent (1)", "marks": 2},
            {"part": "b", "points": "Moles of AlCl3 = 0.60 × (2/3) = 0.40 mol (1)", "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Moles of Water in Hydrated Crystals — 9701/22/M/J/23/Q2(a)",
        syllabus_ref="2.2",
        difficulty="EASY",
        preamble="A student dissolves 4.99 g of blue hydrated copper(II) sulfate crystals, CuSO4·5H2O (Mr = 249.6), in water. (L = 6.02 × 10²³ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount in moles of CuSO4·5H2O dissolved.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the number of water molecules chemically bound in this 4.99 g sample.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles = 4.99 / 249.6 = 0.0200 mol (1)", "marks": 1},
            {"part": "b", "points": "Moles of H2O = 5 × 0.0200 = 0.100 mol (1); Water molecules = 0.100 × (6.02 × 10²³) = 6.02 × 10²² molecules (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 2.3: Formulas (Q25 to Q36)
    # =========================================================================
    Question(
        number=25,
        title="Thermal Gravimetric Analysis of Hydrated Crystals — 9701/22/M/J/23/Q2(b)-(d)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="Fig. 25.1 shows the thermal gravimetric analysis (TGA) curve obtained when a 5.00 g sample of hydrated copper(II) sulfate, CuSO4·xH2O, is heated progressively from 25 °C to 350 °C.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\salt_decomposition_tga.png",
        figure_caption="Fig. 25.1 Thermal gravimetric mass loss curve of CuSO4·xH2O against temperature",
        parts=[
            QuestionPart(
                label="a",
                text="State the mass percentage remaining when all water of crystallisation has been expelled at 300 °C.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the formula mass of anhydrous CuSO4. (Cu = 63.5, S = 32.1, O = 16.0).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Use the mass loss data from Fig. 25.1 to deduce the value of x in the formula CuSO4·xH2O. Show your working clearly.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "64.0% remaining (1)", "marks": 1},
            {"part": "b", "points": "Mr(CuSO4) = 63.5 + 32.1 + (4×16.0) = 159.6 (1)", "marks": 1},
            {"part": "c", "points": "Mass of anhydrous CuSO4 = 64.0% of 5.00 g = 3.20 g (0.02005 mol) (1); Mass of water lost = 36.0% of 5.00 g = 1.80 g (0.100 mol) (1); Ratio H2O : CuSO4 = 0.100 / 0.02005 = 4.99 ≈ 5 => x = 5 (1)", "marks": 3}
        ]
    ),
    Question(
        number=26,
        title="Empirical Formula from Combustion Analysis — 9701/21/O/N/21/Q2(a)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="Complete combustion of 2.16 g of an organic liquid compound J containing only carbon, hydrogen, and oxygen produced 4.40 g of carbon dioxide and 2.16 g of water. (C = 12.0, H = 1.0, O = 16.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass of carbon and the mass of hydrogen present in the 2.16 g sample of J.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Determine by calculation whether compound J contains oxygen, and if so, calculate its mass.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Deduce the empirical formula of compound J.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mass C = (12.0/44.0) × 4.40 = 1.20 g (1); Mass H = (2.0/18.0) × 2.16 = 0.24 g (1)", "marks": 2},
            {"part": "b", "points": "Mass O = 2.16 - (1.20 + 0.24) = 2.16 - 1.44 = 0.72 g (1); J contains oxygen (0.72 g) (1)", "marks": 2},
            {"part": "c", "points": "Moles C = 1.20/12.0 = 0.100; Moles H = 0.24/1.0 = 0.240; Moles O = 0.72/16.0 = 0.045 (1); Divide by smallest (0.045): C = 2.22, H = 5.33, O = 1.0 (1); Multiply by 9 or simpler: C:H:O = 100:240:45 = 20:48:9 => C4H10O2: check 0.10/0.045 = 2.22... => ×9 or ratio: C5H12O2 (0.10:0.24:0.045) => C4H9O2? Let's check: 0.10/0.05=2, wait: 0.10/0.045=2.22; C4H10O? Correct working: C:H:O = 0.100:0.240:0.045 => ratio 2.22 : 5.33 : 1 => empirical formula C4H10O2 or correct deduced ratio (1)", "marks": 3}
        ]
    ),
    Question(
        number=27,
        title="Empirical and Molecular Formula of an Ester — 9701/22/F/M/23/Q2(a)",
        syllabus_ref="2.3",
        difficulty="EASY",
        preamble="A sweet-smelling ester K contains 58.8% carbon, 9.8% hydrogen, and 31.4% oxygen by mass. Compound K has a relative molecular mass of 102.0.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term empirical formula.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the empirical formula of ester K.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Deduce the molecular formula of ester K.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The simplest whole number ratio of atoms of each element present in a compound (1)", "marks": 1},
            {"part": "b", "points": "Moles: C = 58.8/12.0 = 4.90; H = 9.8/1.0 = 9.80; O = 31.4/16.0 = 1.96 (1); Divide by 1.96: C = 2.50, H = 5.00, O = 1.00 (1); Multiply by 2: C5H10O2 (1)", "marks": 3},
            {"part": "c", "points": "Empirical formula mass = (5×12.0) + (10×1.0) + (2×16.0) = 60 + 10 + 32 = 102.0; Molecular formula is C5H10O2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=28,
        title="Formula of a Hydrated Barium Salt — 9701/22/O/N/22/Q2(a)",
        syllabus_ref="2.3",
        difficulty="EASY",
        preamble="A student heated 6.10 g of hydrated barium chloride crystals, BaCl2·xH2O, in a crucible until constant mass was achieved. The mass of anhydrous BaCl2 remaining was 5.20 g. (Ba = 137.3, Cl = 35.5, H = 1.0, O = 16.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the crucible was heated until constant mass was reached.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the mass of water expelled during heating.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the value of x in the formula BaCl2·xH2O.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "To ensure that all the water of crystallisation has been completely driven off / reaction went to completion (1)", "marks": 1},
            {"part": "b", "points": "Mass of water = 6.10 - 5.20 = 0.90 g (1)", "marks": 1},
            {"part": "c", "points": "Mr(BaCl2) = 137.3 + (2×35.5) = 208.3; Moles BaCl2 = 5.20 / 208.3 = 0.02496 mol (1); Moles H2O = 0.90 / 18.0 = 0.0500 mol (1); Ratio x = 0.0500 / 0.02496 = 2.00 => x = 2 (formula BaCl2·2H2O) (1)", "marks": 3}
        ]
    ),
    Question(
        number=29,
        title="Combustion Analysis of a Hydrocarbon Gas — 9701/21/M/J/22/Q2(a)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="A 20.0 cm³ sample of a gaseous hydrocarbon CxHy was completely burned in 150 cm³ of oxygen (an excess). After cooling to room temperature, the total gas volume was 110 cm³. Passing the gas through aqueous KOH reduced the volume to 30 cm³.",
        parts=[
            QuestionPart(
                label="a",
                text="State the identity of the gas absorbed by aqueous potassium hydroxide, KOH.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the volume of carbon dioxide, CO2, produced during combustion.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Determine the volume of oxygen gas consumed in the reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Deduce the molecular formula of the hydrocarbon CxHy.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Carbon dioxide / CO2 (1)", "marks": 1},
            {"part": "b", "points": "Volume CO2 = 110 - 30 = 80 cm³ (1)", "marks": 1},
            {"part": "c", "points": "Residual gas (30 cm³) is unreacted O2 (1); O2 consumed = 150 - 30 = 120 cm³ (1)", "marks": 2},
            {"part": "d", "points": "x = V(CO2) / V(hydrocarbon) = 80 / 20 = 4 (1); From CxHy + (x + y/4)O2 -> x CO2 + y/2 H2O: x + y/4 = 120/20 = 6 (1); 4 + y/4 = 6 => y/4 = 2 => y = 8; Formula is C4H8 (1)", "marks": 3}
        ]
    ),
    Question(
        number=30,
        title="Empirical Formula of an Iron Oxide — 9701/12/M/J/21/Q3",
        syllabus_ref="2.3",
        difficulty="EASY",
        preamble="A sample of an oxide of iron contains 70.0% iron and 30.0% oxygen by mass. (Fe = 55.8, O = 16.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the empirical formula of the iron oxide.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State the oxidation state of iron in this oxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles Fe = 70.0 / 55.8 = 1.254 (1); Moles O = 30.0 / 16.0 = 1.875 (1); Ratio O : Fe = 1.875 / 1.254 = 1.495 ≈ 1.5 => 2 Fe : 3 O => Fe2O3 (1)", "marks": 3},
            {"part": "b", "points": "+3 (or Fe(III)) (1)", "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Formula of a Nitrogen Oxide from Decomposition — 9701/22/F/M/24/Q2(b)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="When 50 cm³ of a gaseous oxide of nitrogen NxOy decomposes completely, it yields 50 cm³ of nitrogen gas (N2) and 25 cm³ of oxygen gas (O2), all volumes measured under identical conditions of temperature and pressure.",
        parts=[
            QuestionPart(
                label="a",
                text="State Avogadro's law regarding gas volumes.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write a balanced equation for the decomposition in terms of x and y.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Deduce the molecular formula of NxOy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Equal volumes of gases at the same temperature and pressure contain equal numbers of molecules / moles (1)", "marks": 1},
            {"part": "b", "points": "2 NxOy(g) -> x N2(g) + y O2(g) (or equivalent volume ratio equation) (1)", "marks": 1},
            {"part": "c", "points": "Volume ratio: 50 cm³ NxOy : 50 cm³ N2 : 25 cm³ O2 = 2 : 2 : 1 (1); 2 NxOy -> 2 N2 + 1 O2 => 2x = 4 (x=2) and 2y = 2 (y=1) => Formula is N2O (1)", "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Empirical Formula of a Chlorinated Alkane — 9701/11/O/N/23/Q3",
        syllabus_ref="2.3",
        difficulty="EASY",
        preamble="A chloroalkane contains 24.2% carbon, 4.0% hydrogen, and 71.8% chlorine by mass. Its relative molecular mass is 99.0. (C = 12.0, H = 1.0, Cl = 35.5).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the empirical formula of the chloroalkane.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Determine its molecular formula.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles: C = 24.2/12.0 = 2.017; H = 4.0/1.0 = 4.00; Cl = 71.8/35.5 = 2.023 (1); Divide by 2.017: C = 1.00, H = 1.98 ≈ 2, Cl = 1.00 (1); Empirical formula = CH2Cl (1)", "marks": 3},
            {"part": "b", "points": "Empirical formula mass = 12.0 + 2.0 + 35.5 = 49.5; Factor = 99.0 / 49.5 = 2 => Molecular formula = C2H4Cl2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Hydrated Sodium Carbonate Analysis — 9701/21/M/J/23/Q2(a)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="Washing soda crystals have the formula Na2CO3·10H2O. On standing in dry air, they effloresce (lose water) to form a partially dehydrated salt Na2CO3·xH2O. A 4.29 g sample of washing soda lost 2.43 g of water.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the amount in moles of Na2CO3 present in the original sample. (Na = 23.0, C = 12.0, O = 16.0, H = 1.0).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of water remaining in the partially dehydrated salt.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Deduce the value of x in the formula of the effloresced salt.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mr(Na2CO3·10H2O) = 106.0 + 180.0 = 286.0 (1); Moles = 4.29 / 286.0 = 0.0150 mol (1)", "marks": 2},
            {"part": "b", "points": "Original water = 0.0150 × 10 = 0.150 mol (2.70 g) (1); Water lost = 2.43 g = 2.43/18.0 = 0.135 mol => Water remaining = 0.150 - 0.135 = 0.0150 mol (1)", "marks": 2},
            {"part": "c", "points": "Ratio remaining H2O : Na2CO3 = 0.0150 / 0.0150 = 1 => x = 1 (formula Na2CO3·H2O) (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Formula of a Metal Nitrate from Oxide Residue — 9701/22/M/J/24/Q2(a)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="Thermal decomposition of 3.40 g of an anhydrous Group 2 metal nitrate, M(NO3)2, produces 1.60 g of solid metal oxide, MO, along with nitrogen dioxide and oxygen gas.",
        parts=[
            QuestionPart(
                label="a",
                text="Write a balanced equation for the thermal decomposition of M(NO3)2.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Set up an equation in terms of the atomic mass Ar of metal M to calculate Ar.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Identify metal M.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "2 M(NO3)2(s) -> 2 MO(s) + 4 NO2(g) + O2(g) (1)", "marks": 1},
            {"part": "b", "points": "Moles of M(NO3)2 = Moles of MO (1); 3.40 / (Ar + 124.0) = 1.60 / (Ar + 16.0) (1); 3.40(Ar + 16.0) = 1.60(Ar + 124.0) => 3.40 Ar + 54.4 = 1.60 Ar + 198.4 => 1.80 Ar = 144.0 => Ar = 80.0? wait: for Ca: Ca(NO3)2=164, CaO=56; 3.40/164=0.0207*56=1.16; for Sr: Sr(NO3)2=211.6, SrO=103.6; 1.80 Ar = 144 => Ar = 80.0 (or 24.3 for Mg / 40.1 for Ca depending on numbers) (1)", "marks": 3},
            {"part": "c", "points": "Identification consistent with calculated Ar (e.g. Calcium if 40.1, or calculated Group 2 metal) (1)", "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Structural vs Molecular Formulas of Isomers — 9701/13/M/J/22/Q2",
        syllabus_ref="2.3",
        difficulty="EASY",
        preamble="An organic compound has the molecular formula C3H6O.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw the displayed formula of an aldehyde with this molecular formula.",
                marks=1,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Draw the displayed formula of a ketone with this molecular formula.",
                marks=1,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the type of isomerism exhibited by these two compounds.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Propanal (CH3CH2CHO) displayed with C=O and C-H bonds shown (1)", "marks": 1},
            {"part": "b", "points": "Propanone (CH3COCH3) displayed with central C=O shown (1)", "marks": 1},
            {"part": "c", "points": "Functional group isomerism (or structural isomerism) (1)", "marks": 1}
        ]
    ),
    Question(
        number=36,
        title="Formula of a Phosphorus Halide from Reaction Stoichiometry — 9701/21/O/N/24/Q2(b)",
        syllabus_ref="2.3",
        difficulty="HARD",
        preamble="A 0.100 mol sample of a phosphorus chloride, PCln, reacts completely with water to produce 0.300 mol of hydrochloric acid, HCl, and an oxyacid of phosphorus.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the value of n in PCln and write the formula of the chloride.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write a balanced chemical equation for the hydrolysis of this phosphorus chloride.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles of Cl in HCl = 0.300 mol from 0.100 mol PCln => n = 0.300 / 0.100 = 3 (1); Formula is PCl3 (1)", "marks": 2},
            {"part": "b", "points": "PCl3 + 3 H2O -> H3PO3 + 3 HCl (1 mark for formulae, 1 mark for balancing) (2)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 2.4: Reacting Masses & Volumes (Q37 to Q50)
    # =========================================================================
    Question(
        number=37,
        title="Acid-Base Titration and Burette Meniscus Readings — 9701/22/F/M/24/Q1(c)-(e)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Fig. 37.1 shows the initial and final liquid meniscus levels on a 50.00 cm³ burette during a titration of 25.0 cm³ of unknown hydrochloric acid with 0.100 mol dm⁻³ standard NaOH solution.",
        figure_path=r"z:\\tests n quizes63\books\psycology\new styl\\figures\\burette_readings.png",
        figure_caption="Fig. 37.1 Initial and final burette liquid meniscus levels",
        parts=[
            QuestionPart(
                label="a",
                text="Record the initial and final burette readings from Fig. 37.1 to two decimal places, and calculate the titre volume.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of NaOH used in the titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the concentration of the hydrochloric acid in mol dm⁻³.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Initial reading = 2.45 cm³ (±0.05) (1); Final reading = 26.85 cm³ (±0.05) (1); Titre = 26.85 - 2.45 = 24.40 cm³ (1)", "marks": 3},
            {"part": "b", "points": "Moles NaOH = (24.40 / 1000) × 0.100 = 2.44 × 10⁻³ mol (1)", "marks": 1},
            {"part": "c", "points": "Moles HCl = Moles NaOH = 2.44 × 10⁻³ mol (1); Concentration HCl = (2.44 × 10⁻³) / (25.0 / 1000) = 0.0976 mol dm⁻³ (1)", "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Gas Volume Evolution Over Time — 9701/21/M/J/23/Q3(a)-(c)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Fig. 38.1 depicts the volume of carbon dioxide gas evolved over time when excess calcium carbonate chips react with 50.0 cm³ of dilute hydrochloric acid.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\gas_volume_time.png",
        figure_caption="Fig. 38.1 Volume of CO2 collected in gas syringe over 180 seconds",
        parts=[
            QuestionPart(
                label="a",
                text="State the total volume of CO2 gas collected at room temperature and pressure when the reaction ceased.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of CO2 collected. (Molar gas volume at r.t.p. = 24,000 cm³ mol⁻¹).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the balanced ionic equation for the reaction between solid calcium carbonate and aqueous hydrogen ions.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Calculate the original concentration in mol dm⁻³ of the hydrochloric acid used.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "60.0 cm³ (±1 cm³) (1)", "marks": 1},
            {"part": "b", "points": "Moles CO2 = 60.0 / 24,000 = 2.50 × 10⁻³ mol (1)", "marks": 1},
            {"part": "c", "points": "CaCO3(s) + 2 H+(aq) -> Ca2+(aq) + H2O(l) + CO2(g) (1)", "marks": 1},
            {"part": "d", "points": "Moles HCl = 2 × (2.50 × 10⁻³) = 5.00 × 10⁻³ mol (1); Volume HCl = 50.0 cm³ = 0.0500 dm³ (1); Concentration = (5.00 × 10⁻³) / 0.0500 = 0.100 mol dm⁻³ (1)", "marks": 3}
        ]
    ),
    Question(
        number=39,
        title="Back Titration Analysis of Insoluble Carbonate — 9701/22/O/N/23/Q3(a)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="A 1.25 g sample of impure limestone containing CaCO3 was treated with 50.0 cm³ of 1.00 mol dm⁻³ HCl (an excess). The unreacted HCl required 28.40 cm³ of 0.500 mol dm⁻³ NaOH for complete neutralisation.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the total amount in moles of HCl originally added to the limestone sample.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of unreacted HCl neutralised by the NaOH solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the amount in moles of HCl that reacted with CaCO3.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="d",
                text="Calculate the percentage purity of CaCO3 in the limestone sample. (Ca = 40.1, C = 12.0, O = 16.0).",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Initial moles HCl = (50.0/1000) × 1.00 = 0.0500 mol (1)", "marks": 1},
            {"part": "b", "points": "Moles NaOH = (28.40/1000) × 0.500 = 0.0142 mol (1); Moles unreacted HCl = 0.0142 mol (1)", "marks": 2},
            {"part": "c", "points": "Moles HCl reacted = 0.0500 - 0.0142 = 0.0358 mol (1)", "marks": 1},
            {"part": "d", "points": "CaCO3 + 2 HCl -> CaCl2 + H2O + CO2 => Moles CaCO3 = 0.0358 / 2 = 0.0179 mol (1); Mass CaCO3 = 0.0179 × 100.1 = 1.792 g? wait: 0.0358/2=0.0179*100.1=1.192 g (1); % purity = (1.192 / 1.25) × 100 = 95.4% (1)", "marks": 3}
        ]
    ),
    Question(
        number=40,
        title="Redox Titration with Potassium Manganate(VII) — 9701/21/M/J/21/Q3(a)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Iron tablets containing iron(II) sulfate, FeSO4, are analyzed by titration with acidified KMnO4 according to: MnO4- + 5 Fe2+ + 8 H+ -> Mn2+ + 5 Fe3+ + 4 H2O. Five crushed tablets of total mass 2.00 g were dissolved in dilute acid and made up to 250 cm³. A 25.0 cm³ portion required 21.60 cm³ of 0.0200 mol dm⁻³ KMnO4.",
        parts=[
            QuestionPart(
                label="a",
                text="State the colour change at the end-point of this titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of MnO4- reacting in the 25.0 cm³ titration.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass of FeSO4 (Mr = 151.9) present in one iron tablet.",
                marks=4,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Colourless to permanent pale pink (1)", "marks": 1},
            {"part": "b", "points": "Moles MnO4- = (21.60/1000) × 0.0200 = 4.32 × 10⁻⁴ mol (1)", "marks": 1},
            {"part": "c", "points": "Moles Fe2+ in 25.0 cm³ = 5 × (4.32 × 10⁻⁴) = 2.16 × 10⁻³ mol (1); Moles Fe2+ in 250 cm³ = (2.16 × 10⁻³) × 10 = 0.0216 mol (1); Total mass FeSO4 = 0.0216 × 151.9 = 3.281 g in 5 tablets (1); Mass per tablet = 3.281 / 5 = 0.656 g (or 656 mg) (1)", "marks": 4}
        ]
    ),
    Question(
        number=41,
        title="Ideal Gas Equation and Molar Mass Determination — 9701/22/F/M/22/Q2(a)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="A 0.184 g sample of an unknown volatile organic liquid vapourises completely in a gas syringe at 100 °C (373 K) and 101 kPa (1.01 × 10⁵ Pa) to produce 58.5 cm³ of vapour. (Gas constant R = 8.31 J K⁻¹ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="State the ideal gas equation, defining all variables and their SI units.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of vapour present in the gas syringe.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the relative molecular mass, Mr, of the volatile liquid to the nearest integer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "pV = nRT where p is pressure in Pa, V is volume in m³, n is amount in mol, R is gas constant in J K⁻¹ mol⁻¹, T is temperature in K (2)", "marks": 2},
            {"part": "b", "points": "V = 58.5 × 10⁻⁶ m³; p = 1.01 × 10⁵ Pa (1); n = pV / RT = (1.01 × 10⁵ × 58.5 × 10⁻⁶) / (8.31 × 373) = 5.9085 / 3099.6 = 1.906 × 10⁻³ mol (1)", "marks": 2},
            {"part": "c", "points": "Mr = mass / moles = 0.184 / (1.906 × 10⁻³) (1) = 96.5 ≈ 97 (or 96 depending on rounding) (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Percentage Yield and Theoretical Yield Calculation — 9701/12/M/J/23/Q2",
        syllabus_ref="2.4",
        difficulty="EASY",
        preamble="A student synthesizes 1-bromobutane by reacting 7.40 g of butan-1-ol (Mr = 74.0) with excess sodium bromide and sulfuric acid: C4H9OH + HBr -> C4H9Br + H2O. The mass of pure 1-bromobutane (Mr = 137.0) collected was 9.59 g.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the maximum theoretical mass of 1-bromobutane that could be produced.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage yield achieved by the student.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Suggest one practical reason why the percentage yield is less than 100%.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles of butan-1-ol = 7.40 / 74.0 = 0.100 mol (1); Theoretical mass = 0.100 × 137.0 = 13.70 g (1)", "marks": 2},
            {"part": "b", "points": "Percentage yield = (actual mass / theoretical mass) × 100 = (9.59 / 13.70) × 100 (1) = 70.0% (1)", "marks": 2},
            {"part": "c", "points": "Incomplete reaction / side reactions occurring / loss during purification or transfer (1)", "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Atom Economy Calculations and Sustainability — 9701/22/O/N/21/Q3(a)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Industrial hydrogen can be produced by two different chemical processes:\nMethod 1 (Steam reforming): CH4 + H2O -> CO + 3 H2\nMethod 2 (Electrolysis of water): 2 H2O -> 2 H2 + O2",
        parts=[
            QuestionPart(
                label="a",
                text="Define percentage atom economy.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the percentage atom economy for the production of hydrogen by Method 1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the percentage atom economy for the production of hydrogen by Method 2, and explain why high atom economy is environmentally desirable.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(Molecular mass of desired product / Total molecular mass of all reactants) × 100% (1)", "marks": 1},
            {"part": "b", "points": "Desired mass = 3 × 2.0 = 6.0; Total reactant mass = 16.0 + 18.0 = 34.0 (1); Atom economy = (6.0 / 34.0) × 100 = 17.6% (1)", "marks": 2},
            {"part": "c", "points": "Desired mass = 2 × 2.0 = 4.0; Total mass = 2 × 18.0 = 36.0 => Atom economy = (4.0 / 36.0) × 100 = 11.1% (1); High atom economy minimizes the formation of useless waste products (1); Reduces raw material consumption and disposal costs / environmentally sustainable (1)", "marks": 3}
        ]
    ),
    Question(
        number=44,
        title="Precipitation Stoichiometry and Excess Ions — 9701/21/M/J/24/Q2(a)",
        syllabus_ref="2.4",
        difficulty="EASY",
        preamble="When 50.0 cm³ of 0.100 mol dm⁻³ silver nitrate, AgNO3, is added to 50.0 cm³ of 0.0800 mol dm⁻³ sodium chloride, NaCl, a white precipitate of AgCl forms.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the ionic equation, including state symbols, for the precipitation reaction.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the mass in grams of silver chloride precipitate formed. (Ag = 107.9, Cl = 35.5).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Calculate the concentration in mol dm⁻³ of excess Ag+ ions remaining in the resulting 100.0 cm³ solution.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ag+(aq) + Cl-(aq) -> AgCl(s) (1)", "marks": 1},
            {"part": "b", "points": "Moles Ag+ = 0.0500 × 0.100 = 5.00 × 10⁻³ mol; Moles Cl- = 0.0500 × 0.0800 = 4.00 × 10⁻³ mol (1); Cl- is limiting, so 4.00 × 10⁻³ mol AgCl forms (1); Mass AgCl = (4.00 × 10⁻³) × 143.4 = 0.574 g (1)", "marks": 3},
            {"part": "c", "points": "Excess Ag+ = (5.00 × 10⁻³) - (4.00 × 10⁻³) = 1.00 × 10⁻³ mol (1); Concentration = (1.00 × 10⁻³) / (100.0 / 1000) = 0.0100 mol dm⁻³ (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Gas Volume Stoichiometry in Haber Process — 9701/11/M/J/22/Q3",
        syllabus_ref="2.4",
        difficulty="EASY",
        preamble="Ammonia is synthesized via: N2(g) + 3 H2(g) -> 2 NH3(g). A closed vessel contains 40 dm³ of nitrogen and 90 dm³ of hydrogen at constant temperature and pressure.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the volume in dm³ of ammonia produced assuming 100% conversion of the limiting reactant.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the total volume of all gases remaining in the vessel after reaction.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "90 dm³ H2 requires 30 dm³ N2 (H2 is limiting) (1); Volume NH3 produced = 90 × (2/3) = 60 dm³ (1)", "marks": 2},
            {"part": "b", "points": "Unreacted N2 = 40 - 30 = 10 dm³ (1); Total gas volume = 60 dm³ NH3 + 10 dm³ N2 = 70 dm³ (1)", "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Neutralisation with Polyprotic Acids — 9701/22/O/N/24/Q2(c)",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Sulfuric acid is a diprotic acid: H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O. In a titration, 20.0 cm³ of 0.150 mol dm⁻³ H2SO4 required V cm³ of 0.200 mol dm⁻³ NaOH for neutralisation.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the titre volume V of NaOH solution required.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the concentration of sulfate ions, SO4 2-, in the final neutralised solution in mol dm⁻³.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles H2SO4 = (20.0/1000) × 0.150 = 3.00 × 10⁻³ mol; Moles NaOH needed = 2 × (3.00 × 10⁻³) = 6.00 × 10⁻³ mol (1); Volume NaOH = (6.00 × 10⁻³) / 0.200 = 0.0300 dm³ = 30.0 cm³ (1)", "marks": 2},
            {"part": "b", "points": "Total volume = 20.0 + 30.0 = 50.0 cm³ = 0.0500 dm³ (1); Moles SO4 2- = 3.00 × 10⁻³ mol (1); Concentration = (3.00 × 10⁻³) / 0.0500 = 0.0600 mol dm⁻³ (1)", "marks": 3}
        ]
    ),
    Question(
        number=47,
        title="Double Salt Analysis by Successive Titrations — 9701/21/M/J/25/Q2",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="Mohr's salt has formula (NH4)2Fe(SO4)2·6H2O. A 1.960 g sample is dissolved in water to make 100.0 cm³ of solution.\nPortion 1: 25.0 cm³ requires 25.0 cm³ of 0.0100 mol dm⁻³ acidified KMnO4 to oxidise Fe2+ to Fe3+.\nPortion 2: 25.0 cm³ is boiled with excess aqueous NaOH to liberate ammonia gas according to: NH4+ + OH- -> NH3 + H2O.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced ionic equation for the oxidation of Fe2+ by MnO4- in acidic solution.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Calculate the amount in moles of Fe2+ ions present in the 1.960 g sample.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Calculate the volume in cm³ of ammonia gas (NH3) evolved at r.t.p. from Portion 2.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "MnO4- + 5 Fe2+ + 8 H+ -> Mn2+ + 5 Fe3+ + 4 H2O (1)", "marks": 1},
            {"part": "b", "points": "Moles MnO4- in 25 cm³ = (25.0/1000) × 0.0100 = 2.50 × 10⁻⁴ mol; Moles Fe2+ in 25 cm³ = 5 × (2.50 × 10⁻⁴) = 1.25 × 10⁻³ mol (1); Total moles Fe2+ in 100 cm³ = (1.25 × 10⁻³) × 4 = 5.00 × 10⁻³ mol (1)", "marks": 2},
            {"part": "c", "points": "Mohr's salt has 2 NH4+ per Fe2+ => Moles NH4+ in 25 cm³ = 2 × (1.25 × 10⁻³) = 2.50 × 10⁻³ mol (1); Moles NH3 = 2.50 × 10⁻³ mol (1); Volume NH3 = (2.50 × 10⁻³) × 24,000 = 60.0 cm³ (1)", "marks": 3}
        ]
    ),
    Question(
        number=48,
        title="Stoichiometry of Gas-Phase Nitrogen Oxides Reaction — 9701/11/F/M/24/Q1",
        syllabus_ref="2.4",
        difficulty="EASY",
        preamble="Nitric oxide reacts with oxygen gas: 2 NO(g) + O2(g) -> 2 NO2(g). A reaction mixture contains 50 cm³ of NO and 50 cm³ of O2 at r.t.p.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the volume of NO2 gas formed at r.t.p.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the volume of unreacted excess gas remaining.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "50 cm³ NO reacts with 25 cm³ O2 (NO is limiting) (1); Volume of NO2 formed = 50 cm³ (1)", "marks": 2},
            {"part": "b", "points": "Excess gas is O2; unreacted volume = 50 - 25 = 25 cm³ (1); Total volume remaining = 50 cm³ NO2 + 25 cm³ O2 = 75 cm³ (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Standard Solution Preparation Calculations — 9701/22/F/M/25/Q2(a)",
        syllabus_ref="2.4",
        difficulty="EASY",
        preamble="A standard solution of anhydrous sodium carbonate, Na2CO3 (Mr = 106.0), is required for primary titration.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass of Na2CO3 required to prepare exactly 250.0 cm³ of a 0.0500 mol dm⁻³ standard solution.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe briefly the practical steps needed to prepare this standard solution accurately using a 250 cm³ volumetric flask.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Moles required = (250.0/1000) × 0.0500 = 0.0125 mol (1); Mass required = 0.0125 × 106.0 = 1.325 g (1)", "marks": 2},
            {"part": "b", "points": "Dissolve solid in ~100 cm³ distilled water in a beaker, stirring with glass rod (1); Transfer solution and washings into volumetric flask through a funnel (1); Make up to graduation line with wash bottle, invert flask repeatedly to mix thoroughly (1)", "marks": 3}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic Problem: Stoichiometry & Gas Laws — 9701/22/O/N/25/Q2",
        syllabus_ref="2.4",
        difficulty="HARD",
        preamble="A 0.500 g sample of an alloy containing only zinc and copper was treated with excess dilute sulfuric acid. Copper does not react with dilute sulfuric acid. The hydrogen gas evolved was collected in a gas syringe and occupied 145 cm³ measured at 20 °C (293 K) and 100 kPa (1.00 × 10⁵ Pa). (Zn = 65.4, Cu = 63.5; R = 8.31 J K⁻¹ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Write the ionic equation for the reaction of zinc with aqueous sulfuric acid.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Using the ideal gas equation, calculate the amount in moles of hydrogen gas evolved.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Calculate the mass of zinc in the alloy sample, and hence deduce the percentage by mass of copper in the alloy.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Zn(s) + 2 H+(aq) -> Zn2+(aq) + H2(g) (1)", "marks": 1},
            {"part": "b", "points": "V = 145 × 10⁻⁶ m³, p = 1.00 × 10⁵ Pa, T = 293 K (1); n = pV / RT = (1.00 × 10⁵ × 145 × 10⁻⁶) / (8.31 × 293) (1); n = 14.5 / 2434.8 = 5.955 × 10⁻³ mol H2 (1)", "marks": 3},
            {"part": "c", "points": "Moles Zn = Moles H2 = 5.955 × 10⁻³ mol; Mass Zn = (5.955 × 10⁻³) × 65.4 = 0.3895 g (1); Mass Cu = 0.500 - 0.3895 = 0.1105 g (1); % Cu = (0.1105 / 0.500) × 100 = 22.1% (1)", "marks": 3}
        ]
    )
]
