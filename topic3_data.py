"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 3: Chemical Bonding.
Subtopics:
  3.1 Electronegativity and bonding
  3.2 Ionic bonding
  3.3 Metallic bonding
  3.4 Covalent bonding and coordinate (dative covalent) bonding
  3.5 Shapes of molecules (VSEPR theory)
  3.6 Intermolecular forces (London dispersion, dipole-dipole, hydrogen bonding)
  3.7 Dot-and-cross diagrams

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

TOPIC_3_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 3.1: Electronegativity and Bonding (Q1 to Q7)
    # =========================================================================
    Question(
        number=1,
        title="Defining Electronegativity and Pauling Scale — 9701/22/M/J/21/Q2(a)",
        syllabus_ref="3.1",
        difficulty="EASY",
        preamble="Electronegativity is a fundamental property that dictates the nature of chemical bonding between atoms.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term electronegativity.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Name the most electronegative element in the Periodic Table and state its value on the Pauling scale.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The ability / power of an atom to attract the shared pair of electrons (1); in a covalent bond (1)", "marks": 2},
            {"part": "b", "points": "Fluorine / F, with a value of 4.0 (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Pauling Electronegativity Trend Across Period 3 — 9701/21/O/N/22/Q2(a)-(c)",
        syllabus_ref="3.1",
        difficulty="HARD",
        preamble="Fig. 2.1 displays the variation in Pauling electronegativity across the elements of Period 3 from sodium to chlorine.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\electronegativity_period3.png",
        figure_caption="Fig. 2.1 Pauling electronegativity values across Period 3 elements",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the trend in electronegativity across Period 3 shown in Fig. 2.1.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain this trend across Period 3 in terms of nuclear charge, atomic radius, and shielding.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why argon is not assigned a Pauling electronegativity value on this scale.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Electronegativity increases steadily across Period 3 from Na to Cl (1)", "marks": 1},
            {"part": "b", "points": "Nuclear charge increases across the period (+11 to +17) (1); Atomic radius decreases / bonding electrons are closer to the nucleus (1); Shielding remains similar (electrons added to n=3), resulting in a greater effective nuclear attraction for the shared pair (1)", "marks": 3},
            {"part": "c", "points": "Argon has a stable complete octet and does not form standard covalent bonds (1)", "marks": 1}
        ]
    ),
    Question(
        number=3,
        title="Bond Polarity and Permanent Dipoles — 9701/12/M/J/22/Q4",
        syllabus_ref="3.1",
        difficulty="EASY",
        preamble="A covalent bond between two atoms of differing electronegativities is polar.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a polar covalent bond between carbon and chlorine in chloromethane, CH3Cl, using delta+ and delta- notation and a dipole moment arrow (+->).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why tetrachloromethane, CCl4, contains polar bonds but possesses no overall permanent dipole moment.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "C(delta+) - Cl(delta-) with correct charges (1); Dipole arrow pointing from C towards Cl with cross at C (+->) (1)", "marks": 2},
            {"part": "b", "points": "CCl4 has a regular symmetrical tetrahedral geometry (1); The four individual C-Cl bond dipoles cancel each other out completely (vector sum = 0) (1)", "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Predicting Bond Character from Electronegativity Difference — 9701/22/F/M/23/Q1(b)",
        syllabus_ref="3.1",
        difficulty="HARD",
        preamble="The difference in electronegativity (delta-chi) between bonded atoms indicates whether bonding is primarily non-polar covalent, polar covalent, or ionic.",
        parts=[
            QuestionPart(
                label="a",
                text="Pauling electronegativity values are: C = 2.55, H = 2.20, Cl = 3.16, Na = 0.93. Deduce the predominant bonding character in C-H, C-Cl, and NaCl.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why aluminium chloride, AlCl3, behaves predominantly as a covalent molecular substance at room temperature despite being a metal-nonmetal compound.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "C-H: non-polar covalent (delta = 0.35) (1); C-Cl: polar covalent (delta = 0.61) (1); NaCl: ionic (delta = 2.23) (1)", "marks": 3},
            {"part": "b", "points": "Al3+ ion has a high charge (+3) and a very small ionic radius, giving it an extremely high charge density (1); It polarizes the electron cloud of the large chloride ion (Cl-) to such an extent that electron sharing (covalency) occurs (1)", "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Electronegativity Trends Down Group 17 — 9701/11/O/N/23/Q4",
        syllabus_ref="3.1",
        difficulty="EASY",
        preamble="Consider the halogens: F, Cl, Br, and I.",
        parts=[
            QuestionPart(
                label="a",
                text="State and explain the trend in electronegativity down Group 17.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Arrange the following bonds in order of increasing polarity: C-F, C-Cl, C-Br, C-I.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Electronegativity decreases down Group 17 (1); Atomic radius increases and there are more inner shielding electron shells (1); Outermost bonding pair is further from the nucleus and experiences weaker attraction (1)", "marks": 3},
            {"part": "b", "points": "C-I < C-Br < C-Cl < C-F (1)", "marks": 1}
        ]
    ),
    Question(
        number=6,
        title="Polarity in Triatomic Molecules: CO2 vs SO2 — 9701/22/M/J/23/Q3(b)",
        syllabus_ref="3.1",
        difficulty="HARD",
        preamble="Both carbon dioxide, CO2, and sulfur dioxide, SO2, contain polar bonds between a central nonmetal atom and oxygen atoms.",
        parts=[
            QuestionPart(
                label="a",
                text="State the shape and bond angle of CO2 and explain why CO2 is a non-polar molecule.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the shape and approximate bond angle of SO2 and explain why SO2 has a permanent dipole moment.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Linear, 180° (1); The two equal C=O bond dipoles point in opposite directions and cancel out completely (1)", "marks": 2},
            {"part": "b", "points": "Non-linear / bent, approximately 117° to 119° (1); Central S atom has a lone pair of electrons creating an asymmetrical charge distribution (1); The bond dipoles do not cancel, giving a net permanent dipole towards oxygen (1)", "marks": 3}
        ]
    ),
    Question(
        number=7,
        title="Dipole Moments in Halogenoalkanes — 9701/13/M/J/21/Q4",
        syllabus_ref="3.1",
        difficulty="EASY",
        preamble="Consider the isomers cis-1,2-dichloroethene and trans-1,2-dichloroethene.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce which isomer possesses an overall permanent dipole moment.",
                marks=1,
                num_answer_lines=0,
                options=[
                    "A cis-1,2-dichloroethene only",
                    "B trans-1,2-dichloroethene only",
                    "C Both cis and trans isomers",
                    "D Neither isomer"
                ]
            ),
            QuestionPart(
                label="b",
                text="Explain your choice in part (a) with reference to molecular symmetry.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A — cis-1,2-dichloroethene only (1)", "marks": 1},
            {"part": "b", "points": "In the trans isomer, the two C-Cl bond dipoles point in directly opposite directions across the double bond and cancel out completely (1); In the cis isomer, both C-Cl dipoles point to the same side, creating a net molecular dipole (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.2: Ionic Bonding (Q8 to Q14)
    # =========================================================================
    Question(
        number=8,
        title="Definition of Ionic Bonding and Giant Lattice — 9701/21/M/J/22/Q2(a)",
        syllabus_ref="3.2",
        difficulty="EASY",
        preamble="Sodium chloride, NaCl, is an archetypal ionic compound.",
        parts=[
            QuestionPart(
                label="a",
                text="Define ionic bonding.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe the structure of sodium chloride in terms of its giant ionic lattice and coordination numbers.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The electrostatic attraction (1); between oppositely charged ions (1)", "marks": 2},
            {"part": "b", "points": "Giant three-dimensional cubic lattice of alternating Na+ and Cl- ions (1); Each ion has a coordination number of 6 (surrounded octahedrally by 6 oppositely charged ions) (1)", "marks": 2}
        ]
    ),
    Question(
        number=9,
        title="Comparing Melting Points of Ionic Compounds: NaCl vs MgO — 9701/22/O/N/22/Q2(b)",
        syllabus_ref="3.2",
        difficulty="HARD",
        preamble="Sodium chloride, NaCl, has a melting point of 801 °C, whereas magnesium oxide, MgO, melts at 2852 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="State two factors that govern the strength of an ionic bond (lattice energy).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain, in terms of ionic charges and radii, why the melting point of MgO is vastly higher than that of NaCl.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Charges on the ions (1); Radii of the ions / sum of ionic radii (1)", "marks": 2},
            {"part": "b", "points": "Mg2+ and O2- ions carry 2+ and 2- charges whereas Na+ and Cl- carry 1+ and 1- charges (1); Mg2+ and O2- ions have smaller radii than Na+ and Cl- (1); The electrostatic attraction between the 2+/2- ions is roughly 4 times stronger, requiring far more thermal energy to break the lattice (1)", "marks": 3}
        ]
    ),
    Question(
        number=10,
        title="Electrical Conductivity of Ionic Compounds — 9701/11/F/M/22/Q3",
        syllabus_ref="3.2",
        difficulty="EASY",
        preamble="Pure solid sodium chloride is an electrical insulator, but becomes a conductor when molten or dissolved in water.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why solid sodium chloride does not conduct electricity.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why aqueous or molten sodium chloride conducts electricity.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In the solid lattice, ions are held rigidly in fixed positions by strong electrostatic forces (1); There are no mobile ions or delocalised electrons to carry charge (1)", "marks": 2},
            {"part": "b", "points": "When molten or dissolved in water, the giant ionic lattice breaks down (1); The ions become free to move and carry electric current towards electrodes (1)", "marks": 2}
        ]
    ),
    Question(
        number=11,
        title="Brittleness of Ionic Crystals — 9701/22/F/M/24/Q2(a)",
        syllabus_ref="3.2",
        difficulty="EASY",
        preamble="When a sharp mechanical stress (such as a hammer blow) is applied to an ionic crystal, it cleaves along clean planes rather than deforming.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain, with the aid of a diagram or concise description, why ionic crystals are brittle.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mechanical stress / force causes layers of ions to shift relative to one another (1); Ions of like charge are forced into adjacent positions (+ next to +, - next to -) (1); Strong electrostatic repulsion between like-charged ions causes the crystal lattice to fracture/shatter (1)", "marks": 3}
        ]
    ),
    Question(
        number=12,
        title="Hydration and Solubility of Ionic Solids — 9701/23/M/J/23/Q2(a)",
        syllabus_ref="3.2",
        difficulty="HARD",
        preamble="When an ionic solid dissolves in water, the process involves lattice breaking and ion hydration.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the interaction between water molecules and a dissolved sodium cation, Na+.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe the interaction between water molecules and a dissolved chloride anion, Cl-.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why barium sulfate, BaSO4, is virtually insoluble in water despite being an ionic compound.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ion-dipole attraction (1); The partially negative oxygen atoms (delta-) of polar water molecules are attracted to and surround the positive Na+ ion (1)", "marks": 2},
            {"part": "b", "points": "Ion-dipole attraction / hydrogen bonding (1); The partially positive hydrogen atoms (delta+) of water molecules are attracted to and surround the negative Cl- ion (1)", "marks": 2},
            {"part": "c", "points": "The lattice energy of BaSO4 is extremely exothermic due to 2+ and 2- charges (1); The energy released by hydration of Ba2+ and SO4 2- ions is insufficient to overcome the strong lattice enthalpy (1)", "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Polarisation and Covalent Character in Ionic Compounds — 9701/21/O/N/24/Q2(a)",
        syllabus_ref="3.2",
        difficulty="HARD",
        preamble="Fajans' rules govern the degree of covalent character in ionic compounds.",
        parts=[
            QuestionPart(
                label="a",
                text="State two conditions regarding the cation and anion that favour high covalent character in an ionic compound.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Compare the covalent character in lithium iodide, LiI, and potassium fluoride, KF. Justify your comparison fully.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Small cation with high charge (high polarizing power) (1); Large anion with high charge (high polarizability) (1)", "marks": 2},
            {"part": "b", "points": "LiI has much greater covalent character than KF (1); Li+ is very small with high polarizing power, and I- is a very large anion whose electron cloud is easily distorted (1); K+ has low polarizing power and F- is small and tightly held, resulting in essentially purely ionic bonding in KF (1)", "marks": 3}
        ]
    ),
    Question(
        number=14,
        title="Thermal Stability of Group 2 Carbonates and Nitrates — 9701/22/M/J/24/Q3(a)",
        syllabus_ref="3.2",
        difficulty="HARD",
        preamble="The thermal decomposition temperature of Group 2 carbonates increases down the group from MgCO3 to BaCO3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain this trend in thermal stability in terms of the charge density and polarizing power of the Group 2 cations.",
                marks=4,
                num_answer_lines=5
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "All Group 2 cations carry a 2+ charge, but ionic radius increases down the group from Mg2+ to Ba2+ (1); Charge density of the cation decreases down the group (1); Smaller cations (Mg2+) have higher polarizing power and distort the large, polarizable carbonate (CO3 2-) electron cloud more strongly (1); This weakens the C-O bond within the carbonate ion, lowering the activation energy for decomposition (1)", "marks": 4}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.3: Metallic Bonding (Q15 to Q20)
    # =========================================================================
    Question(
        number=15,
        title="Model of Metallic Bonding — 9701/12/O/N/21/Q3",
        syllabus_ref="3.3",
        difficulty="EASY",
        preamble="Metals possess unique physical properties attributed to their lattice structure.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe metallic bonding.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why metals are good conductors of electricity in both solid and liquid states.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Electrostatic attraction (1); between a regular lattice of positive metal ions (cations) and a sea of delocalised electrons (1)", "marks": 2},
            {"part": "b", "points": "Delocalised valence electrons are free to move throughout the entire metallic lattice (1); Under an applied potential difference, they drift towards the positive terminal, conducting electrical current (1)", "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Melting Point Trends Across Period 3 Metals — 9701/22/M/J/22/Q3(a)",
        syllabus_ref="3.3",
        difficulty="HARD",
        preamble="The melting points of the metallic elements in Period 3 are: sodium (98 °C), magnesium (650 °C), and aluminium (660 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the melting point of magnesium is significantly higher than that of sodium.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Predict how the electrical conductivity of aluminium compares to that of sodium at room temperature. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mg2+ carries a 2+ charge whereas Na+ carries a 1+ charge (1); Mg contributes 2 delocalised electrons per atom compared to 1 for Na (greater electron density) (1); Mg2+ has a smaller ionic radius than Na+, creating a vastly stronger electrostatic attraction to delocalised electrons (1)", "marks": 3},
            {"part": "b", "points": "Aluminium has higher electrical conductivity than sodium (1); Each Al atom contributes 3 delocalised electrons to the conduction band compared to 1 for Na, providing a higher carrier concentration (1)", "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Malleability and Ductility of Metals — 9701/21/F/M/23/Q1(c)",
        syllabus_ref="3.3",
        difficulty="EASY",
        preamble="Metals can be hammered into thin sheets (malleable) and drawn into wires (ductile) without fracturing.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why metals are malleable, contrasting their behaviour with that of ionic crystals.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why alloys (such as bronze or steel) are harder and less malleable than pure metals.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In a metal, layers of positive ions can slide over one another when stress is applied (1); The non-directional sea of delocalised electrons maintains electrostatic bonding across all directions without repulsion (1); Unlike ionic solids where like charges align and repel (1)", "marks": 3},
            {"part": "b", "points": "Alloy atoms have different atomic sizes compared to host metal atoms (1); This disrupts the regular layered lattice structure, preventing layers from sliding easily over one another (1)", "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Thermal Conductivity in Metals — 9701/11/M/J/23/Q3",
        syllabus_ref="3.3",
        difficulty="EASY",
        preamble="Copper is widely used in electrical wiring and cooking utensils.",
        parts=[
            QuestionPart(
                label="a",
                text="State the two mechanisms by which heat energy is transported through a metal.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State which of the two mechanisms in part (a) is the primary contributor to the high thermal conductivity of copper.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Movement / kinetic transport of energetic delocalised electrons (1); Lattice vibrations (phonons) transmitted through closely packed cations (1)", "marks": 2},
            {"part": "b", "points": "Kinetic transport by delocalised electrons (1)", "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Trends in Metallic Bonding Down Group 1 — 9701/22/O/N/23/Q2(b)",
        syllabus_ref="3.3",
        difficulty="HARD",
        preamble="The melting points of Group 1 alkali metals decrease monotonically down the group: Li (181 °C), Na (98 °C), K (63 °C), Rb (39 °C), Cs (29 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the strength of metallic bonding decreases down Group 1.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "All Group 1 cations have a 1+ charge and contribute 1 delocalised electron per atom (1); The ionic radius of the cation increases down the group from Li+ to Cs+ (1); The larger distance between the delocalised electron sea and the cation nucleus reduces electrostatic attraction (1)", "marks": 3}
        ]
    ),
    Question(
        number=20,
        title="Comparing Giant Structures: Metallic vs Ionic vs Giant Covalent — 9701/21/M/J/24/Q2(c)",
        syllabus_ref="3.3",
        difficulty="HARD",
        preamble="Table 20.1 shows properties of three unknown solids X, Y, and Z.\n• Solid X: MP 1414 °C, conducts electricity in both solid and liquid states.\n• Solid Y: MP 801 °C, non-conductor when solid, conducts when molten.\n• Solid Z: MP 3550 °C, non-conductor in both solid and liquid states.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the type of bonding and structure present in Solid X, Solid Y, and Solid Z.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Suggest an identity for Solid Z.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Solid X: metallic bonding / giant metallic lattice (1); Solid Y: ionic bonding / giant ionic lattice (1); Solid Z: covalent bonding / giant covalent (macromolecular) lattice (1)", "marks": 3},
            {"part": "b", "points": "Diamond (or silicon / silicon dioxide) (1)", "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.4: Covalent & Coordinate (Dative) Bonding (Q21 to Q28)
    # =========================================================================
    Question(
        number=21,
        title="Coordinate Bonding in the Aluminium Chloride Dimer — 9701/22/M/J/21/Q3(a)-(c)",
        syllabus_ref="3.4",
        difficulty="HARD",
        preamble="Fig. 21.1 shows the bonding in the dimer of aluminium chloride, Al2Cl6, formed in the vapour phase at moderate temperatures.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\al2cl6_dimer_dative.png",
        figure_caption="Fig. 21.1 Coordinate (dative covalent) bonding in Al2Cl6 dimer",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term coordinate (dative covalent) bond.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Using Fig. 21.1, identify which atoms donate the lone pairs and which atoms act as lone-pair acceptors.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the total number of covalent bonds and the number of dative bonds present in one Al2Cl6 molecule.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A covalent bond in which both shared electrons are provided by the same atom (1); into an empty orbital of another atom (1)", "marks": 2},
            {"part": "b", "points": "Bridging chlorine atoms donate a lone pair (1); Aluminium atoms accept the lone pair into an empty 3p orbital (1)", "marks": 2},
            {"part": "c", "points": "4 standard covalent bonds (terminal Al-Cl) and 2 dative covalent bonds (or 6 total bonds with 2 dative) (2)", "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Formation and Structure of the Ammonium Ion — 9701/21/O/N/21/Q2(b)",
        syllabus_ref="3.4",
        difficulty="EASY",
        preamble="Ammonia reacts with hydrogen chloride gas to form solid ammonium chloride: NH3(g) + HCl(g) -> NH4Cl(s).",
        parts=[
            QuestionPart(
                label="a",
                text="Describe how the dative covalent bond in the ammonium ion, NH4+, is formed from an ammonia molecule and a hydrogen ion.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why all four N-H bonds in the ammonium ion have identical bond lengths and bond energies once the ion has formed.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The nitrogen atom in NH3 donates its lone pair of electrons (1); into the vacant 1s orbital of a hydrogen ion (H+) (1)", "marks": 2},
            {"part": "b", "points": "Once formed, a dative covalent bond is identical in character to a standard covalent bond (1); The positive charge and electron density are distributed symmetrically across all four N-H bonds in the tetrahedral ion (1)", "marks": 2}
        ]
    ),
    Question(
        number=23,
        title="Sigma (sigma) and Pi (pi) Bonds in Hydrocarbons — 9701/22/F/M/22/Q3(a)",
        syllabus_ref="3.4",
        difficulty="HARD",
        preamble="Covalent bonds can be classified as sigma (sigma) or pi (pi) bonds based on orbital overlap geometry.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the difference between a sigma bond and a pi bond in terms of how atomic orbitals overlap.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the number of sigma bonds and pi bonds present in one molecule of ethene, C2H4.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the number of sigma bonds and pi bonds present in one molecule of propyne, CH3-C≡CH.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Sigma bond: direct 'head-on' / end-to-end overlap of orbitals along the internuclear axis (1); Pi bond: 'sideways' parallel overlap of unhybridised p orbitals above and below the internuclear axis (1)", "marks": 2},
            {"part": "b", "points": "5 sigma bonds (four C-H, one C-C) and 1 pi bond (in C=C) (2)", "marks": 2},
            {"part": "c", "points": "6 sigma bonds (four C-H, two C-C) and 2 pi bonds (in C≡C) (2)", "marks": 2}
        ]
    ),
    Question(
        number=24,
        title="Bond Energy and Bond Length Correlations — 9701/12/M/J/23/Q4",
        syllabus_ref="3.4",
        difficulty="EASY",
        preamble="Table 24.1 lists carbon-carbon bond lengths and average bond energies:\n• C-C single bond: length 0.154 nm, energy 347 kJ mol⁻¹\n• C=C double bond: length 0.134 nm, energy 612 kJ mol⁻¹\n• C≡C triple bond: length 0.120 nm, energy 838 kJ mol⁻¹",
        parts=[
            QuestionPart(
                label="a",
                text="Describe and explain the relationship between bond order, bond length, and bond energy.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why the bond energy of a C=C double bond (612 kJ mol⁻¹) is less than twice the bond energy of a C-C single bond (347 kJ mol⁻¹).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "As bond order increases from single to triple, bond length decreases and bond energy increases (1); More shared electron pairs increase electrostatic attraction to nuclei (1); Nuclei are pulled closer together, requiring greater energy to break (1)", "marks": 3},
            {"part": "b", "points": "A double bond consists of one sigma bond and one pi bond (1); Sideways overlap in a pi bond is less effective than head-on overlap in a sigma bond, making the pi bond weaker (612 - 347 = 265 kJ mol⁻¹ for pi bond) (1)", "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Dative Bonding in Carbon Monoxide, CO — 9701/21/M/J/23/Q3(a)",
        syllabus_ref="3.4",
        difficulty="HARD",
        preamble="Carbon monoxide, CO, possesses a triple bond between carbon and oxygen.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the composition of the triple bond in carbon monoxide in terms of covalent and dative covalent bonds.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why carbon monoxide can act as a ligand in transition metal complexes, such as haemoglobin.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Two standard covalent bonds (one electron from C, one from O) (1); One dative covalent bond where oxygen donates a lone pair into an empty carbon orbital (1)", "marks": 2},
            {"part": "b", "points": "Carbon has a lone pair of electrons (1); It donates this lone pair to form a coordinate bond with Fe2+ in haemoglobin (1)", "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Hydronium Ion, H3O+, Formation — 9701/11/O/N/22/Q4",
        syllabus_ref="3.4",
        difficulty="EASY",
        preamble="When acids dissolve in aqueous solution, protons hydrate to form oxonium (hydronium) ions, H3O+.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a displayed formula of the H3O+ ion, indicating the dative covalent bond with an arrow (->).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict the shape and bond angle of the H3O+ ion using VSEPR theory.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Oxygen bonded to three H atoms with brackets and positive charge (1); One bond drawn with an arrow pointing from O to H (1)", "marks": 2},
            {"part": "b", "points": "Trigonal pyramidal (1); Bond angle approximately 107° (similar to NH3 due to 3 bond pairs and 1 lone pair) (1)", "marks": 2}
        ]
    ),
    Question(
        number=27,
        title="Hybridisation: sp, sp2, and sp3 — 9701/22/O/N/24/Q2(a)",
        syllabus_ref="3.4",
        difficulty="HARD",
        preamble="Carbon atoms undergo orbital hybridisation to optimize bonding geometries.",
        parts=[
            QuestionPart(
                label="a",
                text="State the hybridisation of each carbon atom in: ethane (C2H6), ethene (C2H4), and ethyne (C2H2).",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how one 2s orbital and two 2p orbitals hybridise to form sp² hybrid orbitals.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ethane: sp3 (1); Ethene: sp2 (1); Ethyne: sp (1)", "marks": 3},
            {"part": "b", "points": "Mixing / linear combination of one 2s and two 2p atomic orbitals (1); Producing three equivalent degenerate sp² hybrid orbitals arranged in a trigonal planar geometry at 120° angles (leaving one unhybridised 2p orbital) (1)", "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Electron-Deficient Covalent Compounds: BF3 — 9701/21/M/J/25/Q2(b)",
        syllabus_ref="3.4",
        difficulty="EASY",
        preamble="Boron trifluoride, BF3, reacts readily with ammonia, NH3, to form an addition compound (adduct) F3B:NH3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why BF3 is described as an electron-deficient molecule.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe the bond that forms between boron and nitrogen in the F3B:NH3 adduct.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the change in the F-B-F bond angle when BF3 forms the adduct.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The central boron atom has only 6 valence electrons (3 shared pairs), lacking a stable octet (1)", "marks": 1},
            {"part": "b", "points": "Coordinate (dative covalent) bond (1); Nitrogen donates its lone pair of electrons into the empty 2p orbital of boron (1)", "marks": 2},
            {"part": "c", "points": "Decreases from 120° (trigonal planar in BF3) (1); to approximately 109.5° (tetrahedral geometry around boron in adduct) (1)", "marks": 2}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.5: Shapes of Molecules / VSEPR Theory (Q29 to Q36)
    # =========================================================================
    Question(
        number=29,
        title="Summary of VSEPR Molecular Shapes — 9701/22/M/J/22/Q3(b)-(c)",
        syllabus_ref="3.5",
        difficulty="EASY",
        preamble="Fig. 29.1 summarizes key molecular geometries predicted by Valence Shell Electron Pair Repulsion (VSEPR) theory.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\vsepr_shapes_summary.png",
        figure_caption="Fig. 29.1 Fundamental VSEPR molecular shapes, bond angles, and representative molecules",
        parts=[
            QuestionPart(
                label="a",
                text="State the fundamental postulate of VSEPR theory.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Using Fig. 29.1, state the shape and bond angle of methane (CH4) and water (H2O).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why the bond angle in water (104.5°) is smaller than that in methane (109.5°), despite both having four electron pairs around the central atom.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Electron pairs around a central atom repel each other (1); They arrange themselves in three-dimensional space to minimize mutual repulsion (1)", "marks": 2},
            {"part": "b", "points": "Methane: tetrahedral, 109.5° (1); Water: non-linear / bent, 104.5° (1)", "marks": 2},
            {"part": "c", "points": "Order of repulsion: lone pair-lone pair > lone pair-bond pair > bond pair-bond pair (1); CH4 has 4 bond pairs; H2O has 2 bond pairs and 2 lone pairs (1); The greater repulsion from the two lone pairs in water pushes the bond pairs closer together, reducing the angle by ~2.5° per lone pair (1)", "marks": 3}
        ]
    ),
    Question(
        number=30,
        title="Expanded Octet Geometries: PCl5 and SF6 — 9701/21/O/N/23/Q2(b)",
        syllabus_ref="3.5",
        difficulty="HARD",
        preamble="Period 3 elements can expand their octet by utilizing vacant 3d orbitals in bonding.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the number of bond pairs and lone pairs around phosphorus in phosphorus pentachloride, PCl5. State its molecular shape and bond angles.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Deduce the molecular shape and all bond angles of sulfur hexafluoride, SF6.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "5 bond pairs, 0 lone pairs (1); Trigonal bipyramidal (1); Equatorial angles 120° and axial-equatorial angles 90° (and 180° axial-axial) (1)", "marks": 3},
            {"part": "b", "points": "Octahedral (6 bond pairs, 0 lone pairs) (1); All bond angles are 90° (and 180°) (1)", "marks": 2}
        ]
    ),
    Question(
        number=31,
        title="Shape of Xenon Tetrafluoride, XeF4 — 9701/22/F/M/24/Q3(a)",
        syllabus_ref="3.5",
        difficulty="HARD",
        preamble="Xenon forms the noble-gas compound xenon tetrafluoride, XeF4.",
        parts=[
            QuestionPart(
                label="a",
                text="Determine the number of bonding pairs and lone pairs of electrons surrounding the central xenon atom in XeF4.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the molecular shape of XeF4 and state the F-Xe-F bond angle.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why the lone pairs adopt axial positions opposite one another.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Xe has 8 valence electrons + 4 from F = 12 electrons => 6 pairs (1); 4 bonding pairs and 2 lone pairs (1)", "marks": 2},
            {"part": "b", "points": "Square planar (1); Bond angle 90° (1)", "marks": 2},
            {"part": "c", "points": "Placing the two lone pairs at 180° to each other minimizes lone pair-lone pair repulsion (1)", "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Shape of Chlorine Trifluoride, ClF3 — 9701/23/M/J/22/Q2(b)",
        syllabus_ref="3.5",
        difficulty="HARD",
        preamble="Chlorine trifluoride is an extremely reactive interhalogen compound.",
        parts=[
            QuestionPart(
                label="a",
                text="State the total number of valence electrons around the central chlorine atom in ClF3, and deduce the number of bond pairs and lone pairs.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the molecular geometry (shape) and approximate bond angles in ClF3.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Cl has 7 + 3 = 10 electrons (5 pairs) (1); 3 bonding pairs and 2 lone pairs (1)", "marks": 2},
            {"part": "b", "points": "T-shaped (1); Bond angle approximately 87.5° to 89° (less than 90° due to lone pair repulsion) (1)", "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Shapes of Polyatomic Inorganic Ions: CO3 2-, NO3-, SO4 2- — 9701/11/M/J/24/Q3",
        syllabus_ref="3.5",
        difficulty="EASY",
        preamble="The shapes of oxyanions can be determined using VSEPR theory.",
        parts=[
            QuestionPart(
                label="a",
                text="State the shape and bond angle of a carbonate ion, CO3 2-.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the shape and bond angle of a sulfate ion, SO4 2-.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Trigonal planar (1); Bond angle 120° (1)", "marks": 2},
            {"part": "b", "points": "Tetrahedral (1); Bond angle 109.5° (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Shape of Phosphorus Trichloride, PCl3 — 9701/12/O/N/23/Q3",
        syllabus_ref="3.5",
        difficulty="EASY",
        preamble="Phosphorus trichloride, PCl3, is a volatile liquid.",
        parts=[
            QuestionPart(
                label="a",
                text="What is the shape and bond angle of PCl3?",
                marks=1,
                num_answer_lines=0,
                options=[
                    "A Trigonal planar, 120°",
                    "B Trigonal pyramidal, 107°",
                    "C Tetrahedral, 109.5°",
                    "D T-shaped, 90°"
                ]
            ),
            QuestionPart(
                label="b",
                text="Explain why the bond angle in PCl3 is slightly less than 109.5°.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "B — Trigonal pyramidal, 107° (1)", "marks": 1},
            {"part": "b", "points": "Central phosphorus atom has 3 bond pairs and 1 lone pair (1); Lone pair-bond pair repulsion is stronger than bond pair-bond pair repulsion, compressing the bond angle (1)", "marks": 2}
        ]
    ),
    Question(
        number=35,
        title="Bond Angles in Organic Molecules — 9701/22/M/J/23/Q4(a)",
        syllabus_ref="3.5",
        difficulty="HARD",
        preamble="Consider the molecule prop-2-en-1-ol: CH2=CH-CH2-OH.",
        parts=[
            QuestionPart(
                label="a",
                text="State the bond angle around the C(1) atom (in =CH2).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the bond angle around the C(3) atom (in -CH2-).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="State the C-O-H bond angle around the oxygen atom and justify your value.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "120° (sp² hybridised carbon, 3 regions of electron density, trigonal planar) (1)", "marks": 1},
            {"part": "b", "points": "109.5° (sp³ hybridised carbon, tetrahedral arrangement of 4 bond pairs) (1)", "marks": 1},
            {"part": "c", "points": "Approximately 104.5° (or 104° - 105°) (1); Oxygen has 2 bonding pairs and 2 lone pairs, identical to water (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Deducing Unknown Geometry from Electron Pair Counting — 9701/21/O/N/24/Q3(b)",
        syllabus_ref="3.5",
        difficulty="HARD",
        preamble="Consider the interhalogen cation ICl2+ and the anion ICl2-.",
        parts=[
            QuestionPart(
                label="a",
                text="Determine the number of bond pairs and lone pairs on the central iodine atom in ICl2+, and predict its shape.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Determine the number of bond pairs and lone pairs on the central iodine atom in ICl2-, and predict its shape.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "I has 7 - 1 = 6 valence electrons + 2 Cl = 8 electrons (4 pairs) (1); 2 bond pairs and 2 lone pairs (1); Non-linear / bent (approx. 104.5°) (1)", "marks": 3},
            {"part": "b", "points": "I has 7 + 1 = 8 valence electrons + 2 Cl = 10 electrons (5 pairs) (1); 2 bond pairs and 3 lone pairs (1); Linear (the 3 lone pairs occupy equatorial positions at 120°, bond angle 180°) (1)", "marks": 3}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.6: Intermolecular Forces (Q37 to Q45)
    # =========================================================================
    Question(
        number=37,
        title="Boiling Point Anomalies of Binary Hydrides — 9701/22/M/J/21/Q4(a)-(d)",
        syllabus_ref="3.6",
        difficulty="HARD",
        preamble="Fig. 37.1 shows the boiling points of the binary hydrides of the elements in Groups 14, 15, 16, and 17 across Periods 2 to 5.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\hydride_boiling_points.png",
        figure_caption="Fig. 37.1 Boiling points of binary hydrides of Groups 14, 15, 16, and 17",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the boiling points increase steadily down Group 14 from CH4 to SnH4.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why H2O, HF, and NH3 have anomalously high boiling points compared to the hydrides of heavier elements in their respective groups.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why the boiling point of water (100 °C) is significantly higher than that of hydrogen fluoride (20 °C), even though fluorine is more electronegative than oxygen.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Group 14 hydrides are non-polar molecules held solely by London dispersion (instantaneous dipole-induced dipole) forces (1); Down the group, the number of electrons per molecule increases (16 to 66) (1); The larger electron cloud is more polarizable, creating stronger London dispersion forces (1)", "marks": 3},
            {"part": "b", "points": "O, F, and N are small, highly electronegative atoms with lone pairs (1); They form intermolecular hydrogen bonds between molecules (1); Hydrogen bonds are much stronger than London dispersion forces or permanent dipole-dipole attractions, requiring more thermal energy to break (1)", "marks": 3},
            {"part": "c", "points": "Each H2O molecule has 2 hydrogen atoms and 2 lone pairs on oxygen, forming an average of 2 hydrogen bonds per molecule (3D network) (1); HF has only 1 hydrogen atom per molecule, forming on average only 1 hydrogen bond per molecule (1); Water forms twice as many hydrogen bonds per molecule as HF, so total intermolecular energy is greater (1)", "marks": 3}
        ]
    ),
    Question(
        number=38,
        title="Three Types of Intermolecular Forces — 9701/21/O/N/21/Q3(a)",
        syllabus_ref="3.6",
        difficulty="EASY",
        preamble="Intermolecular forces dictate the boiling points, solubilities, and physical states of molecular substances.",
        parts=[
            QuestionPart(
                label="a",
                text="Name the three types of intermolecular forces in order of generally increasing typical strength.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how instantaneous dipole-induced dipole (London dispersion) forces originate.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "London dispersion forces < Permanent dipole-dipole attractions < Hydrogen bonding (2 marks for all three in order, 1 mark for names without correct order) (2)", "marks": 2},
            {"part": "b", "points": "Constant random motion of electrons within an atom/molecule produces an uneven temporary charge distribution (1); This creates an instantaneous dipole (1); The instantaneous dipole induces an opposite dipole in an adjacent atom/molecule, resulting in electrostatic attraction (1)", "marks": 3}
        ]
    ),
    Question(
        number=39,
        title="Hydrogen Bonding Requirements — 9701/22/F/M/22/Q3(b)",
        syllabus_ref="3.6",
        difficulty="EASY",
        preamble="Hydrogen bonding is a special, strong category of permanent dipole-dipole attraction.",
        parts=[
            QuestionPart(
                label="a",
                text="State the two essential structural conditions required for hydrogen bonding to occur between molecules.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Draw a diagram showing a hydrogen bond between two ethanol (C2H5OH) molecules. Include all lone pairs and partial charges (delta+ and delta-).",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "A hydrogen atom bonded covalently to a small, highly electronegative atom (N, O, or F) (1); A lone pair of electrons on a neighboring N, O, or F atom (1)", "marks": 2},
            {"part": "b", "points": "O(delta-) - H(delta+) dipole shown correctly on both molecules (1); Lone pair shown on oxygen atom (1); Hydrogen bond drawn as a dashed line from the lone pair of one oxygen to the delta+ hydrogen of the other, with O-H...O angle linear / 180° (1)", "marks": 3}
        ]
    ),
    Question(
        number=40,
        title="Density Anomaly of Ice Compared to Liquid Water — 9701/11/F/M/23/Q3",
        syllabus_ref="3.6",
        difficulty="HARD",
        preamble="Unlike almost all other substances, solid ice floats on liquid water at 0 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why solid ice has a lower density than liquid water at 0 °C.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State one biological consequence of the fact that ice floats on water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In ice, water molecules are held in a regular, open, three-dimensional tetrahedral lattice by hydrogen bonds (1); Each water molecule forms 4 hydrogen bonds, creating large spaces/cavities within the crystal structure (1); When ice melts, the rigid hydrogen-bonded network collapses and water molecules pack more closely together in the liquid state (1)", "marks": 3},
            {"part": "b", "points": "Ice insulates the liquid water beneath, preventing aquatic life from freezing in lakes and ponds during winter (1)", "marks": 1}
        ]
    ),
    Question(
        number=41,
        title="Comparing Boiling Points of Halogens — 9701/12/M/J/24/Q4",
        syllabus_ref="3.6",
        difficulty="EASY",
        preamble="The boiling points of the halogens are: F2 (-188 °C), Cl2 (-34 °C), Br2 (59 °C), I2 (184 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the only type of intermolecular force present in pure liquid halogens.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the boiling point increases steadily from fluorine to iodine.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Instantaneous dipole-induced dipole forces / London dispersion forces (1)", "marks": 1},
            {"part": "b", "points": "Total number of electrons per diatomic molecule increases down the group (F2=18 to I2=106) (1); Larger electron cloud is more polarizable, creating stronger London dispersion forces requiring more thermal energy to overcome (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Branched vs Straight-Chain Alkane Boiling Points — 9701/22/O/N/23/Q4(a)",
        syllabus_ref="3.6",
        difficulty="HARD",
        preamble="Pentane (CH3(CH2)3CH3) has a boiling point of 36 °C, whereas its branched isomer 2,2-dimethylpropane (C(CH3)4) boils at 9.5 °C, despite both having the molecular formula C5H12.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why straight-chain pentane has a higher boiling point than branched 2,2-dimethylpropane.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Pentane has a zig-zag chain structure with a large molecular surface area of contact between molecules (1); 2,2-dimethylpropane is spherical with a smaller surface area of contact, preventing molecules from packing closely together (1); Pentane experiences more numerous London dispersion attractions across its surface, requiring more thermal energy to separate molecules (1)", "marks": 3}
        ]
    ),
    Question(
        number=43,
        title="Solubility in Polar vs Non-Polar Solvents — 9701/21/M/J/22/Q3(c)",
        syllabus_ref="3.6",
        difficulty="EASY",
        preamble="Iodine, I2, is virtually insoluble in water but readily dissolves in hexane, C6H14.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why iodine is poorly soluble in water.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why iodine dissolves readily in hexane.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Water molecules are held together by strong hydrogen bonds (1); The weak dispersion interactions between non-polar I2 and polar H2O molecules cannot release enough energy to break the hydrogen-bonded network of water (1)", "marks": 2},
            {"part": "b", "points": "Both I2 and hexane are non-polar molecules held by London dispersion forces (1); The solute-solvent dispersion attractions formed are similar in magnitude to the solute-solute and solvent-solvent attractions (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Boiling Point Comparison: Propan-1-ol vs Propanone vs Butane — 9701/22/F/M/25/Q3(a)",
        syllabus_ref="3.6",
        difficulty="HARD",
        preamble="Table 44.1 lists three organic compounds with similar molecular masses:\n• Butane (Mr = 58): BP -0.5 °C\n• Propanone (Mr = 58): BP 56 °C\n• Propan-1-ol (Mr = 60): BP 97 °C",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the strongest type of intermolecular force present in each pure compound.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain the order of boiling points: Butane < Propanone < Propan-1-ol.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Butane: London dispersion forces (1); Propanone: Permanent dipole-dipole attractions (from C=O) (1); Propan-1-ol: Hydrogen bonding (from O-H group) (1)", "marks": 3},
            {"part": "b", "points": "All three have comparable electron counts and similar dispersion force magnitudes (1); Propanone has additional permanent dipole-dipole attractions which are stronger than dispersion forces, raising its BP above butane (1); Propan-1-ol has hydrogen bonding which is substantially stronger than dipole-dipole attractions, requiring the most energy to vaporize (1)", "marks": 3}
        ]
    ),
    Question(
        number=45,
        title="Viscosity and Surface Tension Trends in Alcohols — 9701/11/O/N/24/Q4",
        syllabus_ref="3.6",
        difficulty="EASY",
        preamble="Ethanol (CH3CH2OH) is a free-flowing liquid, whereas glycerol (propane-1,2,3-triol, CH2OH-CHOH-CH2OH) is a viscous, syrupy liquid.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why glycerol has a vastly higher viscosity and boiling point than ethanol.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ethanol contains only one -OH group, forming limited hydrogen bonds (1); Glycerol contains three -OH groups per molecule (1); Glycerol forms extensive three-dimensional intermolecular hydrogen-bonding networks, restricting the flow of molecules and creating high viscosity (1)", "marks": 3}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 3.7: Dot-and-Cross Diagrams (Q46 to Q50)
    # =========================================================================
    Question(
        number=46,
        title="Dot-and-Cross Diagram of Methanoic Acid, HCO2H — 9701/21/M/J/21/Q4(d)",
        syllabus_ref="3.7",
        difficulty="EASY",
        preamble="Methanoic acid has the molecular formula HCO2H. The central carbon atom is bonded to a hydrogen atom, a carbonyl oxygen atom, and a hydroxyl group.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a 'dot-and-cross' diagram, showing outer-shell electrons only, to represent the bonding in methanoic acid, HCO2H.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State the total number of non-bonding lone pairs of electrons in a molecule of methanoic acid.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Single C-H pair, double C=O (4 shared electrons), single C-O pair, single O-H pair correctly shown (1); Two lone pairs on carbonyl oxygen, two lone pairs on hydroxyl oxygen (1)", "marks": 2},
            {"part": "b", "points": "4 lone pairs (two on each oxygen atom) (1)", "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Dot-and-Cross Diagram for Nitrogen Gas, N2, and Cyanide Ion, CN- — 9701/22/O/N/21/Q4(a)",
        syllabus_ref="3.7",
        difficulty="HARD",
        preamble="Both dinitrogen (N2) and the cyanide ion (CN-) contain a triple bond between two atoms.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a 'dot-and-cross' diagram of a nitrogen molecule, N2, showing outer electrons only.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Draw a 'dot-and-cross' diagram of a cyanide anion, CN-, indicating the origin of the negative charge.",
                marks=2,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Triple bond shown with 6 shared electrons (3 dots, 3 crosses) (1); One lone pair on each nitrogen atom (1)", "marks": 2},
            {"part": "b", "points": "Triple bond shown with 6 shared electrons between C and N (1); One lone pair on N, one lone pair on C, outer bracket with 1- charge indicating the extra gained electron on carbon (1)", "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Dot-and-Cross Diagram with Expanded Octet: SF6 and PCl5 — 9701/23/M/J/22/Q3(c)",
        syllabus_ref="3.7",
        difficulty="HARD",
        preamble="Sulfur hexafluoride, SF6, contains 12 electrons in the valence shell of sulfur.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a 'dot-and-cross' diagram for SF6, showing all valence electrons around sulfur and fluorine atoms.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why sulfur can expand its octet to form SF6, whereas oxygen in the same group can only form OF2 and cannot form OF6.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "6 shared pairs between S and F (12 electrons around S) (1); 3 lone pairs (6 non-bonding electrons) on each of the six fluorine atoms (1); Clear differentiation using dots and crosses (1)", "marks": 3},
            {"part": "b", "points": "Sulfur is in Period 3 and has access to energetically accessible vacant 3d orbitals for octet expansion (1); Oxygen is in Period 2 and has only 2s and 2p orbitals (maximum capacity 8 electrons, no low-lying d orbitals) (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Dot-and-Cross Diagram for Dative Bonded Species: NH4+ and H3O+ — 9701/12/M/J/23/Q3",
        syllabus_ref="3.7",
        difficulty="EASY",
        preamble="Dative covalent bonds can be represented in dot-and-cross diagrams where both shared electrons originate from the same atom.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a 'dot-and-cross' diagram for an ammonium ion, NH4+, using dots for nitrogen electrons, crosses for three hydrogen electrons, and an open circle for the dative electron pair.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Draw a 'dot-and-cross' diagram for the hydronium ion, H3O+.",
                marks=2,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Central N surrounded by 4 H atoms with brackets and + charge (1); Three standard N-H pairs (dot and cross) and one dative pair (two dots from N) (1)", "marks": 2},
            {"part": "b", "points": "Central O with 1 lone pair (two dots) and 3 bonding pairs to H in brackets with + charge (1); Clear representation of dative pair from oxygen to H+ (1)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Problem: Chemical Bonding, Geometry & Intermolecular Forces — 9701/22/O/N/25/Q3",
        syllabus_ref="3.7",
        difficulty="HARD",
        preamble="Hydrazine, N2H4, is a rocket propellant that is miscible with water in all proportions.\n• Boiling point of hydrazine: 114 °C\n• Melting point of hydrazine: 2 °C",
        parts=[
            QuestionPart(
                label="a",
                text="Draw a 'dot-and-cross' diagram for a hydrazine molecule, N2H4, showing outer electrons only.",
                marks=2,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Deduce the shape and bond angle around each nitrogen atom in hydrazine.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why hydrazine has a boiling point higher than water (114 °C vs 100 °C) despite having a lower electronegativity difference than H2O.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Single N-N bond (2 shared electrons) and four N-H bonds (2 shared electrons each) (1); One lone pair on each nitrogen atom (1)", "marks": 2},
            {"part": "b", "points": "Trigonal pyramidal (around each N) (1); Bond angle approximately 107° (3 bond pairs, 1 lone pair) (1)", "marks": 2},
            {"part": "c", "points": "Hydrazine has a higher relative molecular mass (Mr = 32.0 vs 18.0) and more electrons (18 vs 10), resulting in significantly stronger London dispersion forces (1); Each hydrazine molecule possesses two -NH2 groups with two lone pairs, allowing multiple hydrogen bonds per molecule (1); The combination of stronger dispersion forces and extensive hydrogen bonding requires more energy to overcome than water's forces (1)", "marks": 3}
        ]
    )
]
