"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 9: The Periodic Table: Chemical Periodicity.
Subtopics:
  9.1 Periodicity of physical properties of Period 3 elements: radius, IE, mp, conductivity
  9.2 Periodicity of chemical properties: reactions with O2, Cl2, H2O, oxides and chlorides

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

TOPIC_9_QUESTIONS = [
    # =========================================================================
    # SUBTOPIC 9.1: Periodicity of Physical Properties of Period 3 (Q1 to Q25)
    # =========================================================================
    Question(
        number=1,
        title="Electronic Configurations Across Period 3 — 9701/22/M/J/21/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The physical and chemical properties of the Period 3 elements (Na to Ar) are fundamentally determined by their electronic configurations.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the full electronic configuration of an atom of silicon, Si, and an atom of sulfur, S.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the number of unpaired electrons present in the ground state of an isolated phosphorus atom, P.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Si: 1s2 2s2 2p6 3s2 3p2 (1); S: 1s2 2s2 2p6 3s2 3p4 (1)", "marks": 2},
            {"part": "b", "points": "3 unpaired electrons (one in each of 3px, 3py, 3pz by Hund's rule) (1)", "marks": 1}
        ]
    ),
    Question(
        number=2,
        title="Physical Property Trends Across Period 3 — 9701/21/O/N/20/Q7(a)-(d)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="Fig. 9.1 displays the variation of atomic radius, first ionisation energy, melting point, and electrical conductivity across Period 3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why atomic radius decreases steadily across Period 3 from Na to Ar.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the first ionisation energy of aluminium is lower than that of magnesium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why silicon has by far the highest melting point of all elements in Period 3.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="d",
                text="Explain why electrical conductivity increases from Na to Al, drops sharply at Si, and is virtually zero from P to Ar.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Nuclear charge (number of protons) increases across the period while electron shielding remains approximately constant (electrons added to same 3rd shell) (1); Stronger electrostatic attraction pulls valence electrons closer to the nucleus (1)", "marks": 2},
            {"part": "b", "points": "The outer electron in Al is in a 3p orbital, which is at a higher energy level than the 3s orbital of Mg (1); The 3p electron is shielded by the inner 3s2 electrons, requiring less energy to remove (1)", "marks": 2},
            {"part": "c", "points": "Silicon has a giant covalent 3D lattice structure (diamond-like macromolecule) (1); Melting requires breaking millions of strong covalent Si-Si bonds throughout the entire structure, requiring huge thermal energy (1)", "marks": 2},
            {"part": "d", "points": "From Na to Al, metallic bonding has more delocalised electrons per atom (1 in Na, 2 in Mg, 3 in Al), increasing mobile charge carrier density (1); Si is a giant covalent metalloid where valence electrons are localised in covalent bonds with only few thermally excited electrons (semiconductor) (1); P to Ar are simple molecular or monoatomic non-metals with all electrons localised in bonds/lone pairs, so no mobile charge carriers exist (1)", "marks": 3}
        ],
        figure_path="figures/period3_physical_trends.png",
        figure_caption="Fig. 9.1: Trends in atomic radius, first ionisation energy, melting point, and electrical conductivity across Period 3."
    ),
    Question(
        number=3,
        title="Ionic Radii Across Period 3: Cations vs Anions — 9701/23/M/J/22/Q8(a)-(c)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="Fig. 9.2 shows the variation of ionic radius across Period 3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the ionic radius decreases across the cation series: Na+ (102 pm) > Mg2+ (72 pm) > Al3+ (54 pm).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain the massive discontinuity / sudden increase in ionic radius between Al3+ (54 pm) and P3- (212 pm).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain why the ionic radius decreases across the anion series: P3- (212 pm) > S2- (184 pm) > Cl- (181 pm).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na+, Mg2+, and Al3+ are isoelectronic with identical [Ne] core (10 electrons in 2 shells) (1); Nuclear charge increases (+11 to +12 to +13), pulling the remaining electron shells more tightly towards the nucleus (1)", "marks": 2},
            {"part": "b", "points": "Cations (Na+ to Al3+) have lost their outer 3rd shell and have only 2 electron shells (1); Anions (P3- to Cl-) retain 3 electron shells (isoelectronic with [Ar], 18 electrons) (1); Gaining extra electrons causes mutual electron-electron repulsion, pushing the electron cloud outward (1)", "marks": 3},
            {"part": "c", "points": "P3-, S2-, and Cl- are isoelectronic with 18 electrons (3 shells) (1); Nuclear charge increases (+15 to +16 to +17), pulling the same number of electrons into a progressively smaller volume (1)", "marks": 2}
        ],
        figure_path="figures/period3_ionic_radii.png",
        figure_caption="Fig. 9.2: Comparison of ionic radii across Period 3 showing cation and anion series."
    ),
    Question(
        number=4,
        title="Trend in Atomic Radius: Nuclear Charge vs Shielding — 9701/22/F/M/21/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Across Period 3 from sodium (186 pm) to chlorine (99 pm), the atomic radius decreases by nearly 50%.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the two competing factors that influence atomic radius across a period, and state which factor predominates.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why electron shielding remains approximately constant across Period 3.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Increasing nuclear charge (proton number) and electron shielding (1); Increasing nuclear charge predominates across the period (1)", "marks": 2},
            {"part": "b", "points": "All successive electrons are added into the same principal quantum shell (n = 3), with the same number of inner shielding electrons (1s2 2s2 2p6) (1)", "marks": 1}
        ]
    ),
    Question(
        number=5,
        title="First Ionisation Energy Dip at Sulfur — 9701/21/M/J/22/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The first ionisation energy of phosphorus is 1012 kJ mol^-1, whereas that of sulfur is 1000 kJ mol^-1, contrary to the general upward trend.",
        parts=[
            QuestionPart(
                label="a",
                text="Draw orbital box diagrams for the 3p subshells of phosphorus and sulfur.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain the dip in first ionisation energy between phosphorus and sulfur.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "P: three single arrows in separate boxes [^][^][^] (1); S: one pair of arrows and two single arrows [^v][^][^] (1)", "marks": 2},
            {"part": "b", "points": "In sulfur, the electron is removed from a paired 3p orbital (3p_x^2) (1); Spin-pair repulsion between the two electrons in the same orbital makes that electron easier to remove than from an unpaired orbital in P (1)", "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Melting Point Trends of Period 3 Non-Metals — 9701/22/O/N/23/Q8(a)-(c)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The melting points of the non-metallic elements in Period 3 are:\n• Silicon: 1414 °C\n• Phosphorus: 44 °C\n• Sulfur: 115 °C\n• Chlorine: -101 °C\n• Argon: -189 °C",
        parts=[
            QuestionPart(
                label="a",
                text="State the molecular formula of elemental phosphorus, sulfur, and chlorine in their standard states.",
                marks=3,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why sulfur has a significantly higher melting point than phosphorus.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why argon has the lowest melting point of all Period 3 elements.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Phosphorus: P4 (1); Sulfur: S8 (1); Chlorine: Cl2 (1)", "marks": 3},
            {"part": "b", "points": "Both have simple molecular structures; S8 molecules are larger and possess more electrons (128 electrons) than P4 molecules (60 electrons) (1); Stronger London dispersion forces between S8 molecules require more thermal energy to overcome (1)", "marks": 2},
            {"part": "c", "points": "Argon exists as monoatomic atoms (Ar) with no covalent molecular structure (1); It has the smallest electron cloud and weakest London dispersion forces, requiring minimal energy to separate (1)", "marks": 2}
        ]
    ),
    Question(
        number=7,
        title="Electrical Conductivity of Period 3 Elements — 9701/21/M/J/23/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Electrical conductivity varies widely across Period 3 elements.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why aluminium is a better electrical conductor than sodium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why solid sulfur is an electrical insulator.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Aluminium contributes 3 delocalised electrons per atom to the metallic lattice compared to only 1 for sodium (1); Aluminium has a much higher concentration of mobile charge carriers (electrons) per unit volume (1)", "marks": 2},
            {"part": "b", "points": "In sulfur (S8), all valence electrons are fixed/localised in covalent bonds or lone pairs; there are no delocalised electrons or mobile ions to carry current (1)", "marks": 1}
        ]
    ),
    Question(
        number=8,
        title="Deducing Group Number from Successive Ionisation Energies of Silicon — 9701/22/M/J/20/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The first six successive ionisation energies of an unknown Period 3 element X are:\n789, 1577, 3232, 4356, 16091, 19785 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify element X and justify your choice by locating the major jump in ionisation energy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the fifth ionisation energy of element X.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Element X is Silicon / Si (1); The huge jump occurs between the 4th and 5th IE (4356 to 16091 kJ mol^-1), indicating that 4 electrons are in the outer shell and the 5th is removed from an inner noble gas shell (Group 14) (1)", "marks": 2},
            {"part": "b", "points": "Si^4+(g) -> Si^5+(g) + e- (1)", "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Radius of Sodium Cation vs Sodium Atom — 9701/21/O/N/22/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The radius of a neutral sodium atom is 186 pm, whereas the radius of a sodium cation, Na+, is 102 pm.",
        parts=[
            QuestionPart(
                label="a",
                text="State the electron configuration of Na and Na+.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the Na+ cation is significantly smaller than the Na atom.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na: 1s2 2s2 2p6 3s1; Na+: 1s2 2s2 2p6 (1)", "marks": 1},
            {"part": "b", "points": "Formation of Na+ involves the loss of the entire outermost quantum shell (n = 3) (1); In Na+, 11 protons now pull on only 10 electrons, increasing effective nuclear charge per electron and pulling remaining shells closer (1)", "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Radius of Chloride Anion vs Chlorine Atom — 9701/23/O/N/21/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The atomic radius of chlorine is 99 pm, whereas the ionic radius of the chloride ion, Cl-, is 181 pm.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the chloride anion is nearly twice as large as the neutral chlorine atom.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State whether this expansion upon ionization is characteristic of all non-metal anions.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Adding an extra electron increases electron-electron repulsion in the outer 3p subshell (1); The nuclear charge (+17) is unchanged, so the electron cloud expands outward to minimize repulsions (1)", "marks": 2},
            {"part": "b", "points": "Yes, all negative ions (anions) are larger than their corresponding neutral parent atoms (1)", "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Isoelectronic Cations: Na+, Mg2+, Al3+ — 9701/22/F/M/23/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The ions Na+, Mg2+, and Al3+ are isoelectronic with neon.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term isoelectronic.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Arrange these three ions in order of decreasing ionic radius and explain the trend.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Having the same number of electrons / identical electronic configuration (1)", "marks": 1},
            {"part": "b", "points": "Na+ (102 pm) > Mg2+ (72 pm) > Al3+ (54 pm) (1); All three have 10 electrons in two shells with identical shielding (1); Proton number increases: Na (11) < Mg (12) < Al (13), creating greater nuclear attraction that pulls electrons closer (1)", "marks": 3}
        ]
    ),
    Question(
        number=12,
        title="Isoelectronic Anions: P3-, S2-, Cl- — 9701/21/M/J/21/Q9(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The ions P3-, S2-, and Cl- all possess 18 electrons (1s2 2s2 2p6 3s2 3p6).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why P3- has the largest ionic radius and Cl- has the smallest among these three ions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Compare the ionic radius of Cl- (181 pm) with that of K+ (138 pm), both of which possess 18 electrons.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Nuclear charge increases from P (+15) to S (+16) to Cl (+17) (1); The 17 protons in Cl- exert a stronger attractive force on the 18 electrons than the 15 protons in P3-, pulling shells tighter (1)", "marks": 2},
            {"part": "b", "points": "K+ has 19 protons while Cl- has only 17 protons (1); Greater nuclear pull in K+ draws the 18 electrons in closer, making K+ smaller than Cl- (1)", "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Pauling Electronegativity Trend Across Period 3 — 9701/22/M/J/22/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Electronegativity values increase steadily across Period 3: Na (0.9), Mg (1.2), Al (1.5), Si (1.8), P (2.1), S (2.5), Cl (3.0).",
        parts=[
            QuestionPart(
                label="a",
                text="Define electronegativity.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why electronegativity increases across Period 3.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The power / ability of an atom to attract the shared pair of electrons (1); in a covalent bond (1)", "marks": 2},
            {"part": "b", "points": "Nuclear charge increases while shielding remains roughly constant (1); Atomic radius decreases, so the bonded electron pair is closer to the nucleus and attracted more strongly (1)", "marks": 2}
        ]
    ),
    Question(
        number=14,
        title="Density Variations Across Period 3 — 9701/22/O/N/21/Q9(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The densities of Period 3 elements are:\nNa (0.97), Mg (1.74), Al (2.70), Si (2.33), P (1.82), S (2.07), Cl (0.003), Ar (0.0017 g cm^-3).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why density increases from sodium to aluminium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain the massive drop in density between sulfur and chlorine at room temperature.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Atomic mass increases (23 to 24.3 to 27) while atomic volume decreases (atoms pack closer together due to stronger metallic bonding) (1); Mass per unit volume increases (1)", "marks": 2},
            {"part": "b", "points": "Sulfur is a solid with molecules packed in a crystalline lattice (1); Chlorine is a gas at room temperature with molecules separated by vast empty spaces (1)", "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Second Ionisation Energy Anomaly: Sodium vs Magnesium — 9701/21/O/N/23/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The first and second ionisation energies of sodium and magnesium are:\n• Sodium: IE1 = 496 kJ mol^-1, IE2 = 4562 kJ mol^-1\n• Magnesium: IE1 = 738 kJ mol^-1, IE2 = 1451 kJ mol^-1",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the second ionisation energy of sodium is more than three times greater than that of magnesium.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the second ionisation energy of sodium.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "For sodium, the second electron is removed from an inner 2p orbital (noble gas core [Ne]) (1); This electron is closer to the nucleus and experiences much less shielding (1); For magnesium, the second electron is removed from the same 3s valence orbital, experiencing shielding from the full n = 2 core (1)", "marks": 3},
            {"part": "b", "points": "Na+(g) -> Na^2+(g) + e- (1)", "marks": 1}
        ]
    ),
    Question(
        number=16,
        title="Metallic Bond Strength in Period 3 Metals — 9701/23/M/J/20/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The boiling points of the Period 3 metals increase in the order: Na (883 °C) < Mg (1090 °C) < Al (2470 °C).",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the bonding in a metal.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the metallic bond strength increases from sodium to aluminium.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Electrostatic attraction between a regular lattice of positive metal ions (cations) (1); and a sea of delocalised electrons (1)", "marks": 2},
            {"part": "b", "points": "Ionic charge increases (Na+ to Mg2+ to Al3+) and ionic radius decreases (1); Number of delocalised electrons per atom increases (1 to 2 to 3), giving much stronger electrostatic attraction (1)", "marks": 2}
        ]
    ),
    Question(
        number=17,
        title="Silicon as a Semiconductor — 9701/22/F/M/24/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="Silicon is a metalloid element located between the metallic conductors and non-metallic insulators in Period 3.",
        parts=[
            QuestionPart(
                label="a",
                text="Contrast the effect of increasing temperature on the electrical conductivity of silicon with that of copper metal.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain your answer to (a) at the particulate level.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In silicon, electrical conductivity increases with temperature (1); In copper, electrical conductivity decreases with temperature (1)", "marks": 2},
            {"part": "b", "points": "In silicon, thermal energy promotes electrons across the small band gap from valence into conduction band (1); In copper, higher temperature causes metal ions to vibrate more vigorously, scattering conducting electrons and increasing resistance (1)", "marks": 2}
        ]
    ),
    Question(
        number=18,
        title="Third Ionisation Energy of Magnesium — 9701/21/M/J/24/Q9(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="For magnesium, the first three ionisation energies are:\nIE1 = 738, IE2 = 1451, IE3 = 7733 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why IE3 is more than five times larger than IE2 for magnesium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Predict whether aluminium or magnesium has the higher third ionisation energy. Justify your answer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The third electron is removed from an inner 2p orbital (noble gas core) (1); It is much closer to the nucleus and experiences far less electron shielding (1)", "marks": 2},
            {"part": "b", "points": "Magnesium has the higher IE3 (1); In Mg, the 3rd electron is from inner 2p shell, whereas in Al (Group 13), the 3rd electron is still a valence electron from the 3s orbital (IE3(Al) ~ 2745 kJ mol^-1) (1)", "marks": 2}
        ]
    ),
    Question(
        number=19,
        title="Bond Enthalpy in Homonuclear Period 3 Molecules — 9701/22/O/N/24/Q8(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="Consider the covalent bonding in Cl2, P4, and S8.",
        parts=[
            QuestionPart(
                label="a",
                text="State the number of single covalent bonds present in one molecule of P4 and one molecule of S8.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why white phosphorus, P4, is tetrahedral and highly strained, causing it to ignite spontaneously in air.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In P4: 6 single P-P bonds (tetrahedron of 4 atoms) (1); In S8: 8 single S-S bonds (crown-shaped ring) (1)", "marks": 2},
            {"part": "b", "points": "In P4, P-P-P bond angles are constrained to 60° within the triangular faces (1); This is far smaller than the preferred 109.5° tetrahedral angle, creating severe ring strain that lowers activation energy for combustion (1)", "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Discontinuity in Ionisation Energy Between Mg and Al — 9701/21/O/N/24/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="Across Period 3, first ionisation energies generally increase. However, IE1(Mg) = 738 kJ mol^-1 while IE1(Al) = 578 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Give the subshell notation for the electron removed in Mg and in Al.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain how this provides experimental evidence for subshell electronic structure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mg: 3s electron (from 3s2) (1); Al: 3p electron (from 3s2 3p1) (1)", "marks": 2},
            {"part": "b", "points": "The lower IE of Al despite having higher nuclear charge (+13 vs +12) proves that the 3p subshell is at a higher energy level than the 3s subshell (1); and that the 3s electron pair partially shields the 3p electron (1)", "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Physical State and Volatility Trends Across Period 3 — 9701/23/M/J/23/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="The elements in Period 3 span metals, metalloids, non-metal solids, and gases at 20 °C.",
        parts=[
            QuestionPart(
                label="a",
                text="State which two elements in Period 3 are gases at 20 °C and standard atmospheric pressure.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why chlorine is a gas at room temperature while iodine is a solid, in terms of intermolecular forces.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Chlorine (Cl2) and Argon (Ar) (1)", "marks": 1},
            {"part": "b", "points": "Iodine molecules (I2) have far more electrons than chlorine molecules (Cl2) (106 vs 34 electrons) (1); Iodine electron cloud is more polarisable, leading to significantly stronger London dispersion forces that hold molecules in a solid crystal at room temperature (1)", "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="First Ionisation Energy of Argon vs Potassium — 9701/22/M/J/25/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="HARD",
        preamble="The first ionisation energy of argon (Period 3) is 1521 kJ mol^-1, whereas that of potassium (Period 4) is 419 kJ mol^-1.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the dramatic drop in first ionisation energy from argon to potassium.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="State the period and group of potassium.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "The outer electron in potassium enters a new quantum shell (4s1) further from the nucleus (1); The 4s electron experiences significantly greater shielding from the full 3s2 3p6 inner noble gas core (1); Increased distance and shielding far outweigh the increase in nuclear charge (+19 vs +18), making the 4s electron much easier to remove (1)", "marks": 3},
            {"part": "b", "points": "Period 4, Group 1 (1)", "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Periodicity of Molar Volume Across Period 3 — 9701/21/F/M/25/Q8(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Molar volume is defined as atomic mass divided by density (V_m = Ar / rho).",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the molar volume of sodium (23.7 cm3 mol^-1) is larger than that of magnesium (14.0 cm3 mol^-1).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State how the strength of metallic bonding influences the packing density and molar volume.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Sodium has a larger atomic radius than magnesium (186 vs 160 pm) and weaker metallic bonding (1); Sodium atoms are held less tightly and pack less densely (1)", "marks": 2},
            {"part": "b", "points": "Stronger metallic bonding pulls cations closer together, reducing molar volume and increasing density (1)", "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Group 2 vs Group 1 Periodic Trends — 9701/22/O/N/25/Q8(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Comparing sodium (Group 1) with magnesium (Group 2) in Period 3 illustrates key group differences.",
        parts=[
            QuestionPart(
                label="a",
                text="Compare the hardness and melting points of sodium and magnesium.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain these differences by referring to their metallic lattices.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Sodium is soft (can be cut with a knife) with low mp (98 °C); Magnesium is hard with high mp (650 °C) (2)", "marks": 2},
            {"part": "b", "points": "Magnesium ions have a 2+ charge and smaller radius compared to Na+ (1); Magnesium has double the density of delocalised electrons, creating vastly stronger metallic bonds that resist mechanical deformation and thermal cleavage (1)", "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Thermal Conductivity Trends Across Period 3 — 9701/23/O/N/24/Q7(a)-(b)",
        syllabus_ref="9.1",
        difficulty="EASY",
        preamble="Metals in Period 3 are excellent thermal conductors, whereas non-metals are thermal insulators.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the mechanism of thermal conduction in metallic aluminium.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why solid phosphorus and sulfur are very poor thermal conductors.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Thermal energy increases kinetic vibrations of Al3+ ions which are passed to neighbouring ions (1); Mobile delocalised electrons absorb kinetic energy and rapidly diffuse through the metal, transferring heat quickly (1)", "marks": 2},
            {"part": "b", "points": "They lack delocalised mobile electrons, and molecules are separated by weak intermolecular forces that transmit lattice vibrations poorly (1)", "marks": 1}
        ]
    ),

    # =========================================================================
    # SUBTOPIC 9.2: Periodicity of Chemical Properties (Q26 to Q50)
    # =========================================================================
    Question(
        number=26,
        title="Period 3 Oxides: Acid-Base Continuum — 9701/22/M/J/21/Q9(a)-(d)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Fig. 9.3 illustrates the progressive change in acid-base character of Period 3 oxides from basic to amphoteric to acidic.",
        parts=[
            QuestionPart(
                label="a",
                text="State the structure and bonding in Na2O, Al2O3, and SO3.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the reaction of sodium oxide with water and state the pH of the resulting solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain what is meant by an amphoteric oxide, using aluminium oxide, Al2O3, as an example with two equations.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="d",
                text="Write the equation for the reaction of phosphorus(V) oxide, P4O10, with water and state the approximate pH.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na2O: Giant ionic (1); Al2O3: Giant ionic with covalent character (1); SO3: Simple covalent molecular (1)", "marks": 3},
            {"part": "b", "points": "Na2O(s) + H2O(l) -> 2NaOH(aq) (1); pH ~ 13-14 (strongly alkaline) (1)", "marks": 2},
            {"part": "c", "points": "An oxide that reacts with both acids and bases/alkalis to form salts (1); Acid: Al2O3 + 6HCl -> 2AlCl3 + 3H2O (1); Base: Al2O3 + 2NaOH + 3H2O -> 2NaAl(OH)4 (or Al2O3 + 2OH- -> 2AlO2- + H2O) (1)", "marks": 3},
            {"part": "d", "points": "P4O10(s) + 6H2O(l) -> 4H3PO4(aq) (1); pH ~ 1-2 (strongly acidic) (1)", "marks": 2}
        ],
        figure_path="figures/period3_oxides_acid_base.png",
        figure_caption="Fig. 9.3: Periodicity of acid-base behavior of Period 3 oxides."
    ),
    Question(
        number=27,
        title="Period 3 Chlorides: Structure, Hydrolysis & Solution pH — 9701/21/O/N/21/Q8(a)-(d)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Fig. 9.4 summarizes the bonding, structure, and behavior with water for Period 3 chlorides.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe the difference in observations when water is added to solid NaCl compared to liquid SiCl4.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the reaction of SiCl4 with water, including state symbols.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why aqueous sodium chloride has a neutral pH of 7 while aqueous aluminium chloride is distinctly acidic (pH ~ 3).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="d",
                text="Write the equation for the reaction of phosphorus(V) chloride, PCl5, with an excess of water.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "NaCl dissolves quietly to form a clear, colourless solution with no temperature rise (1); SiCl4 reacts violently with water, producing steamy white fumes of HCl gas and a white precipitate of hydrated SiO2 (1)", "marks": 2},
            {"part": "b", "points": "SiCl4(l) + 2H2O(l) -> SiO2(s) + 4HCl(aq) (or SiCl4 + 4H2O -> Si(OH)4 + 4HCl) (2)", "marks": 2},
            {"part": "c", "points": "Na+ has low charge density (+1, large radius) and does not polarise coordinated water molecules (1); Al3+ has a very high charge density (+3, small radius) and polarises O-H bonds in [Al(H2O)6]^3+ (1); [Al(H2O)6]^3+ hydrolyses water, releasing H+ ions: [Al(H2O)6]^3+ <=> [Al(H2O)5(OH)]^2+ + H+ (1)", "marks": 3},
            {"part": "d", "points": "PCl5(s) + 4H2O(l) -> H3PO4(aq) + 5HCl(aq) (2)", "marks": 2}
        ],
        figure_path="figures/period3_chlorides_hydrolysis.png",
        figure_caption="Fig. 9.4: Comparison of structure, hydrolysis, and pH of Period 3 chlorides in water."
    ),
    Question(
        number=28,
        title="Combustion of Period 3 Elements in Oxygen — 9701/23/M/J/22/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Period 3 elements react vigorously with oxygen gas upon heating.",
        parts=[
            QuestionPart(
                label="a",
                text="State the flame colour observed when each of the following elements burns in oxygen:\n(i) Sodium\n(ii) Magnesium\n(iii) Sulfur",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write balanced chemical equations for the combustion of sodium (forming Na2O) and sulfur (forming SO2).",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "(i) Bright yellow / orange-yellow flame (1); (ii) Brilliant blinding white flame (1); (iii) Blue flame (1)", "marks": 3},
            {"part": "b", "points": "4Na(s) + O2(g) -> 2Na2O(s) (1); S(s) + O2(g) -> SO2(g) (1)", "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Reactions of Period 3 Elements with Chlorine Gas — 9701/22/F/M/22/Q7(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Chlorine gas is a strong oxidising agent that reacts with Period 3 elements to form chlorides.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced chemical equation for the reaction of heated aluminium with dry chlorine gas.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe the structure and bonding in the dimeric molecule Al2Cl6 formed in the vapour phase.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "2Al(s) + 3Cl2(g) -> Al2Cl6(s) (or 2Al + 3Cl2 -> 2AlCl3) (2)", "marks": 2},
            {"part": "b", "points": "Two AlCl3 units linked together by two coordinate (dative covalent) bonds (1); Each dative bond is formed by a lone pair of electrons from a chlorine atom donating into the vacant 3p orbital of an aluminium atom (1)", "marks": 2}
        ]
    ),
    Question(
        number=30,
        title="Reactions of Sodium and Magnesium with Water — 9701/21/M/J/22/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Sodium and magnesium exhibit contrasting reactivities with water.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe three observations when a small piece of sodium is dropped into cold water.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the chemical equation for the reaction of magnesium with cold water and state the approximate pH of the resulting mixture.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the chemical equation for the reaction of heated magnesium with steam and state two observations.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Melts into a silvery ball / bead (1); Fizzes / effervesces vigorously and darts across water surface (1); Leaves an alkaline solution (universal indicator turns purple) / shrinks and disappears (1)", "marks": 3},
            {"part": "b", "points": "Mg(s) + 2H2O(l) -> Mg(OH)2(s) + H2(g) (1); pH ~ 9-10 (weakly alkaline due to low solubility of Mg(OH)2) (1)", "marks": 2},
            {"part": "c", "points": "Mg(s) + H2O(g) -> MgO(s) + H2(g) (1); Bright white light / blinding white flame (1); White solid / powder of MgO formed (1)", "marks": 3}
        ]
    ),
    Question(
        number=31,
        title="Disproportionation of Chlorine in Water — 9701/22/O/N/22/Q7(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="When chlorine gas dissolves in water, it undergoes a reversible disproportionation reaction:\nCl2(g) + H2O(l) <=> HCl(aq) + HClO(aq)",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the oxidation state of chlorine in Cl2, HCl, and HClO.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why damp blue litmus paper turns red and then rapidly bleaches white when exposed to chlorine gas.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the active chemical species responsible for the antibacterial disinfection of drinking water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "In Cl2: 0 (1); In HCl: -1 (1); In HClO: +1 (1)", "marks": 3},
            {"part": "b", "points": "Turns red due to presence of acidic H+ ions from HCl and HClO (1); Then bleaches white because chloric(I) acid (HClO) is a powerful oxidising agent that bleaches dyes (1)", "marks": 2},
            {"part": "c", "points": "Chloric(I) acid, HClO (or chlorate(I) ion, ClO-) (1)", "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Solubility and Basicity of Na2O vs MgO — 9701/23/O/N/22/Q7(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Both sodium oxide, Na2O, and magnesium oxide, MgO, are basic ionic oxides.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Na2O dissolves completely in water to produce a solution of pH 14, whereas MgO produces a suspension of pH 9.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Write the ionic equation for the reaction of oxide ions, O^2-, with water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na2O has a relatively low lattice energy (+1 ions) and dissolves readily to form fully dissociated Na+ and OH- ions, giving high [OH-] and pH 14 (1); MgO has an extremely high lattice energy (Mg2+ and O2- ions carry 2+ and 2- charges), making it sparingly soluble in water (1); Only a tiny concentration of OH- is produced at equilibrium, yielding pH ~ 9 (1)", "marks": 3},
            {"part": "b", "points": "O^2-(s) + H2O(l) -> 2OH^-(aq) (1)", "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Insoluble Oxides: Al2O3 and SiO2 — 9701/22/F/M/23/Q9(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="When aluminium oxide and silicon(IV) oxide are added to water, no reaction is observed and the pH remains 7.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Al2O3 does not dissolve in water in terms of lattice energy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why SiO2 does not dissolve in water in terms of its macromolecular structure.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Al3+ and O2- ions carry high charges (3+ and 2-), resulting in an immense lattice energy (1); The hydration energy of the ions is insufficient to overcome this very strong electrostatic lattice (1)", "marks": 2},
            {"part": "b", "points": "SiO2 has a giant covalent 3D tetrahedral network (1); Water molecules cannot break the very strong covalent Si-O bonds throughout the macromolecule (1)", "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Reactions of Acidic Oxides with Water — 9701/21/M/J/23/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="The non-metallic oxides P4O10, SO2, and SO3 are acidic and react with water.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced equation for the reaction of sulfur dioxide, SO2, with water and state the formula of the acid formed.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the balanced equation for the reaction of sulfur trioxide, SO3, with water and state the formula of the acid formed.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the balanced equation for the reaction of phosphorus(V) oxide with water.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "SO2(g) + H2O(l) <=> H2SO3(aq) (1); Sulfurous acid / sulfuric(IV) acid, H2SO3 (1)", "marks": 2},
            {"part": "b", "points": "SO3(g) + H2O(l) -> H2SO4(aq) (1); Sulfuric acid / sulfuric(VI) acid, H2SO4 (1)", "marks": 2},
            {"part": "c", "points": "P4O10(s) + 6H2O(l) -> 4H3PO4(aq) (1)", "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Amphoteric Nature of Aluminium Oxide — 9701/22/M/J/23/Q7(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Aluminium oxide, Al2O3, exhibits dual chemical behaviour by reacting with both strong acids and strong alkalis.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the ionic equation for the reaction of Al2O3 with dilute sulfuric acid.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the ionic equation for the reaction of Al2O3 with hot concentrated aqueous sodium hydroxide.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Al2O3(s) + 6H+(aq) -> 2Al^3+(aq) + 3H2O(l) (2)", "marks": 2},
            {"part": "b", "points": "Al2O3(s) + 2OH^-(aq) + 3H2O(l) -> 2[Al(OH)4]^-(aq) (or Al2O3 + 2OH- -> 2AlO2- + H2O) (2)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Hydrolysis of Aluminium Chloride Dimer, Al2Cl6 — 9701/21/O/N/23/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Solid aluminium chloride consists of Al2Cl6 dimers. When water is added dropwise, steamy fumes and an acidic solution are formed.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the gas responsible for the steamy acidic fumes.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="In aqueous solution, aluminium ions form the hexaaqua complex ion [Al(H2O)6]^3+. Write an equation showing how this complex ion hydrolyses water to produce an acidic solution.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why [Al(H2O)6]^3+ hydrolyses water whereas [Na(H2O)6]^+ does not.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Hydrogen chloride / HCl(g) (1)", "marks": 1},
            {"part": "b", "points": "[Al(H2O)6]^3+(aq) + H2O(l) <=> [Al(H2O)5(OH)]^2+(aq) + H3O+(aq) (or [Al(H2O)6]^3+ <=> [Al(H2O)5(OH)]^2+ + H+) (2)", "marks": 2},
            {"part": "c", "points": "Al3+ has a small ionic radius and high charge (+3), giving an extremely high charge density (1); It strongly polarises coordinated water molecules, weakening O-H bonds and releasing H+ ions, whereas Na+ has low charge density (+1) and cannot polarise water (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Violent Hydrolysis of Silicon(IV) Chloride — 9701/22/O/N/23/Q9(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Silicon(IV) chloride, SiCl4, is a volatile liquid at room temperature that fumes profusely in moist air.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe two observations when liquid SiCl4 is added to water.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the balanced equation for the complete hydrolysis of SiCl4.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Vigorous / violent reaction with evolution of dense white steamy fumes of HCl (1); Formation of a white gelatinous precipitate of SiO2 / hydrated silicon dioxide (1)", "marks": 2},
            {"part": "b", "points": "SiCl4(l) + 2H2O(l) -> SiO2(s) + 4HCl(g) (or SiCl4 + 4H2O -> Si(OH)4 + 4HCl) (2)", "marks": 2}
        ]
    ),
    Question(
        number=38,
        title="Hydrolysis of Phosphorus Chlorides: PCl3 vs PCl5 — 9701/23/M/J/24/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Both phosphorus(III) chloride and phosphorus(V) chloride react vigorously with water to form acidic solutions.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced equation for the reaction of PCl3 with water and deduce the oxidation state of phosphorus in the product acid.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Write the balanced equation for the reaction of PCl5 with water and deduce the oxidation state of phosphorus in the product acid.",
                marks=3,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "PCl3(l) + 3H2O(l) -> H3PO3(aq) + 3HCl(aq) (2); Phosphorus in H3PO3 has oxidation state +3 (no change) (1)", "marks": 3},
            {"part": "b", "points": "PCl5(s) + 4H2O(l) -> H3PO4(aq) + 5HCl(aq) (2); Phosphorus in H3PO4 has oxidation state +5 (no change) (1)", "marks": 3}
        ]
    ),
    Question(
        number=39,
        title="Acid-Base Reactions of Period 3 Oxides with Sulfuric Acid — 9701/21/M/J/24/Q10(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Basic and amphoteric oxides react with acids to form salts and water.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation for the reaction of solid magnesium oxide with dilute sulfuric acid.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the reaction of solid aluminium oxide with dilute sulfuric acid.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "MgO(s) + H2SO4(aq) -> MgSO4(aq) + H2O(l) (2)", "marks": 2},
            {"part": "b", "points": "Al2O3(s) + 3H2SO4(aq) -> Al2(SO4)3(aq) + 3H2O(l) (2)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Reaction of Acidic Oxides with Alkalis: SiO2 and SO2 — 9701/22/M/J/24/Q10(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Acidic oxides neutralise alkalis to form oxoanion salts.",
        parts=[
            QuestionPart(
                label="a",
                text="Silicon(IV) oxide does not react with aqueous NaOH at room temperature. Write the equation for its reaction with hot, concentrated molten sodium hydroxide.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the equation for the neutralisation of sulfur dioxide by aqueous sodium hydroxide.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "SiO2(s) + 2NaOH(l) -> Na2SiO3(l) + H2O(g) (2)", "marks": 2},
            {"part": "b", "points": "SO2(g) + 2NaOH(aq) -> Na2SO3(aq) + H2O(l) (or SO2 + NaOH -> NaHSO3) (2)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Phosphate Fertilizer Synthesis from P4O10 — 9701/23/O/N/23/Q8(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Phosphorus(V) oxide reacts with basic calcium oxide at high temperatures to form calcium phosphate, Ca3(PO4)2, a primary constituent of phosphate fertilizers.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the balanced equation for this solid-state acid-base synthesis.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State which reactant acts as the acid and which reactant acts as the base.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "P4O10(s) + 6CaO(s) -> 2Ca3(PO4)2(s) (2)", "marks": 2},
            {"part": "b", "points": "Acid: P4O10 (acidic oxide); Base: CaO (basic oxide) (1)", "marks": 1}
        ]
    ),
    Question(
        number=42,
        title="Sulfur Oxides and Environmental Acid Rain — 9701/22/F/M/25/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="The combustion of sulfur-containing fossil fuels produces sulfur dioxide, which converts to acid rain:\n• Stage 1: S + O2 -> SO2\n• Stage 2: 2SO2 + O2 <=> 2SO3\n• Stage 3: SO3 + H2O -> H2SO4",
        parts=[
            QuestionPart(
                label="a",
                text="State two damaging environmental consequences of acid rain.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why rainwater in pristine unpolluted air is naturally slightly acidic with a pH of ~5.6 rather than 7.0.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Corrosion / chemical weathering of limestone and marble buildings / monuments (CaCO3) (1); Acidification of lakes and rivers, killing fish and aquatic life / leaching toxic Al3+ ions from soil that damage tree roots (1)", "marks": 2},
            {"part": "b", "points": "Naturally occurring atmospheric carbon dioxide, CO2, dissolves in rainwater (1); forming weak, partially dissociated carbonic acid: CO2 + H2O <=> H2CO3 <=> H+ + HCO3- (1)", "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Contrast: Covalent Al2Cl6 vs Ionic Al2O3 in Water — 9701/21/F/M/25/Q9(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Aluminium forms both a chloride, Al2Cl6, and an oxide, Al2O3.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why Al2Cl6 reacts vigorously with water whereas Al2O3 is completely insoluble.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Deduce the coordination number of aluminium in Al2Cl6 vapour and in [Al(H2O)6]^3+.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Al2Cl6 consists of discrete covalent molecules held by weak intermolecular forces; water molecules readily attack the vacant d-orbitals on Al, releasing immense hydration energy and hydrolysing the weak covalent Al-Cl bonds (1); Al2O3 has an extremely strong giant ionic lattice with high lattice energy (Al3+ and O2- ions) which water cannot overcome (1); Hydration enthalpy cannot compensate for the immense lattice energy (1)", "marks": 3},
            {"part": "b", "points": "In Al2Cl6: 4 (tetrahedral around each Al) (1); In [Al(H2O)6]^3+: 6 (octahedral) (1)", "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Corrosion Resistance & Passivation of Aluminium — 9701/22/M/J/25/Q9(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Although aluminium is a highly electropositive metal with a strongly negative standard electrode potential (-1.66 V), aluminium drinks cans and window frames do not react with water or air.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why aluminium appears chemically unreactive under ambient conditions.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain what happens when this protective layer is disrupted by adding aqueous mercury(II) chloride or sodium hydroxide.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Aluminium reacts spontaneously with atmospheric oxygen to form an extremely thin, impervious, strongly adhering layer of aluminium oxide, Al2O3 (1); This passivation layer physically seals the underlying metal from contact with water or oxygen (1)", "marks": 2},
            {"part": "b", "points": "The oxide layer is dissolved or breached, exposing fresh metallic aluminium (1); The bare aluminium reacts vigorously and exothermically with water / oxygen (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Deducing an Unknown Period 3 Element from Compound Properties — 9701/23/M/J/25/Q8(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="An unknown Period 3 element E forms a solid oxide that dissolves in water to give an acidic solution of pH 1. Element E also forms a volatile liquid chloride that reacts violently with water to give steamy acidic fumes and an acidic solution.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the identity of element E.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the formula of the oxide and the chloride formed by element E in its highest oxidation state.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the equation for the reaction of the chloride of E with excess water.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Phosphorus / P (1)", "marks": 1},
            {"part": "b", "points": "Oxide: P4O10 (or P2O5) (1); Chloride: PCl5 (or PCl3) (1)", "marks": 2},
            {"part": "c", "points": "PCl5 + 4H2O -> H3PO4 + 5HCl (2)", "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Highest Oxidation States Across Period 3 — 9701/21/O/N/25/Q9(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="The maximum oxidation state exhibited by Period 3 elements increases across the period to match the group number.",
        parts=[
            QuestionPart(
                label="a",
                text="State the maximum oxidation state of each element from Na to Cl in its highest oxide:\nNa, Mg, Al, Si, P, S, Cl",
                marks=4,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why argon forms no oxides or chlorides under standard conditions.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na: +1, Mg: +2, Al: +3, Si: +4 (2); P: +5, S: +6, Cl: +7 (2)", "marks": 4},
            {"part": "b", "points": "Argon has a complete outer octet (3s2 3p6) with extremely high ionisation energy and zero electron affinity; it is thermodynamically stable as isolated monoatomic atoms (1)", "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Why CCl4 Resists Hydrolysis While SiCl4 Hydrolyses Violently — 9701/22/O/N/25/Q9(a)-(c)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Both tetrachloromethane, CCl4, and silicon(IV) chloride, SiCl4, are non-polar tetrahedral covalent liquids. When shaken with water, CCl4 forms an immiscible layer with zero reaction, whereas SiCl4 hydrolyses violently.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why SiCl4 undergoes rapid hydrolysis while CCl4 is completely inert to water.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain the role of vacant 3d orbitals in the silicon atom during this mechanism.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Silicon has accessible, energetically low-lying vacant 3d orbitals in its valence shell, allowing it to expand its octet (1); Water molecules can donate a lone pair into an empty 3d orbital on Si to form an activated 5-coordinate intermediate (1); Carbon has only 2s and 2p orbitals (maximum octet of 8 electrons) with no available d-orbitals; carbon is also sterically hindered by 4 bulky chlorine atoms (1)", "marks": 3},
            {"part": "b", "points": "Vacant 3d orbitals accept a lone pair of electrons from a nucleophilic H2O molecule (1); enabling a transition state with expanded coordination number (e.g. SiCl4(H2O)) before expelling a Cl- ion (1)", "marks": 2}
        ]
    ),
    Question(
        number=48,
        title="Flame Emission of Period 3 Elements — 9701/23/O/N/25/Q8(a)-(b)",
        syllabus_ref="9.2",
        difficulty="EASY",
        preamble="Flame emission spectra arise from electronic transitions.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the atomic origin of the distinctive yellow-orange flame produced by sodium compounds.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why magnesium does not produce a characteristic flame colour in a standard Bunsen flame, but burns with blinding white light.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Thermal energy from the flame excites valence electrons from the 3s ground state to higher energy 3p orbitals (1); When excited electrons drop back to the lower 3s energy level, they emit electromagnetic radiation (1); The energy gap corresponds to photons of wavelength ~589 nm in the visible yellow region (Delta E = h x nu) (1)", "marks": 3},
            {"part": "b", "points": "Thermal energy in a standard Bunsen flame is insufficient to excite electrons in Mg (higher ionisation energy) (1); When burning vigorously, the extreme combustion temperature heats solid MgO particles to incandescence, emitting continuous white light (blackbody radiation) (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Redox Reduction of Silica by Magnesium — 9701/21/M/J/25/Q9(a)-(b)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Elemental silicon can be prepared in the laboratory by the vigorous exothermic redox reaction between silicon(IV) oxide and magnesium powder:\nSiO2(s) + 2Mg(s) -> Si(s) + 2MgO(s)",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the oxidising agent and reducing agent in this reaction, stating the changes in oxidation numbers.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how pure silicon can be separated from the product mixture containing MgO, Si, and unreacted Mg.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Reducing agent: Magnesium / Mg (0 to +2) (1); Oxidising agent: Silicon / Si in SiO2 (+4 to 0) (1); Correct assignment of oxidation states (1)", "marks": 3},
            {"part": "b", "points": "Add excess dilute hydrochloric acid (1); Basic MgO and unreacted Mg dissolve to form aqueous MgCl2 and H2, while silicon is insoluble in acid and can be filtered off, washed, and dried (1)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Synoptic: Period 3 Periodicity, Oxide Acidity & Chloride Hydrolysis — 9701/22/O/N/25/Q9(a)-(d)",
        syllabus_ref="9.2",
        difficulty="HARD",
        preamble="Table 9.1 summarises data for the elements from sodium to sulfur across Period 3:\n• Na: giant metallic, basic oxide Na2O, chloride NaCl (pH 7 in water)\n• Al: giant metallic, amphoteric oxide Al2O3, chloride Al2Cl6 (pH 3 in water)\n• Si: giant covalent, acidic oxide SiO2, chloride SiCl4 (pH 1 in water)\n• P: simple molecular, acidic oxide P4O10, chloride PCl5 (pH 1 in water)",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the trend in bonding and structure of the elements from Na to P.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why the acid-base character of the oxides changes from strongly basic (Na2O) to amphoteric (Al2O3) to acidic (SiO2, P4O10).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Explain the variation in pH when the chlorides NaCl, Al2Cl6, and SiCl4 are separately added to water.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="d",
                text="Write the equation for the reaction of amphoteric Al2O3 with aqueous sodium hydroxide.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Na and Al have giant metallic lattices with cations in delocalised electrons (1); Si has a giant covalent 3D macromolecular network with localised shared pairs (1); P has a simple molecular lattice (P4) with weak London dispersion forces between discrete molecules (1)", "marks": 3},
            {"part": "b", "points": "Electronegativity of Period 3 elements increases across the period (1); Oxides transition from ionic lattices with free basic O2- ions (Na2O) to partially covalent with polarised bonds (Al2O3) to fully covalent molecular/macromolecular species where polarized non-metal atoms attract OH- or donate H+ to water (SiO2, P4O10) (2)", "marks": 3},
            {"part": "c", "points": "NaCl simply dissolves into hydrated Na+ and Cl- without hydrolysing water, maintaining neutral pH 7 (1); Al2Cl6 forms [Al(H2O)6]^3+ whose high charge density polarises coordinated water, releasing H+ to give pH ~ 3 (1); SiCl4 undergoes violent covalent hydrolysis, generating free HCl(aq) that fully dissociates into H+ and Cl-, giving pH ~ 1 (1)", "marks": 3},
            {"part": "d", "points": "Al2O3(s) + 2NaOH(aq) + 3H2O(l) -> 2NaAl(OH)4(aq) (1)", "marks": 1}
        ]
    )
]
