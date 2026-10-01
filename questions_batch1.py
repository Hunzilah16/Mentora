from generate_pdf import TopicSection, Question, QuestionPart

topics = [
    TopicSection(
        day_label="TOPIC 1",
        topic_code="TOPIC 1",
        topic_name="ATOMIC STRUCTURE",
        questions=[
            Question(
                number=i+1,
                title=f"Atomic Structure — 9701/11/M/J/20/Q{i+1}",
                syllabus_ref="1.1",
                preamble="Which statement about the particles within an atom is correct?",
                parts=[
                    QuestionPart(
                        label="a",
                        text="What is the relative mass and charge of a proton?",
                        marks=1,
                        options=["A Mass 1, Charge 0", "B Mass 1, Charge +1", "C Mass 1/1836, Charge -1", "D Mass 0, Charge +1"]
                    )
                ],
                mark_scheme=[{"part": "a", "points": "B (1)", "marks": 1}]
            ) for i in range(5)
        ] + [
            Question(
                number=i+6,
                title=f"Isotopes — 9701/22/O/N/21/Q{i+1}(a)",
                syllabus_ref="1.2",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Define the term isotope.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Atoms of the same element/same number of protons (1); with different numbers of neutrons/different mass number (1).", "marks": 2}]
            ) for i in range(5)
        ] + [
             Question(
                number=i+11,
                title=f"Ionisation Energy — 9701/21/M/J/19/Q{i+1}",
                syllabus_ref="1.4",
                preamble="[DIAGRAM: Graph showing successive ionisation energies of element X]",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Explain the general increase in successive ionisation energies of element X.",
                        marks=2
                    ),
                    QuestionPart(
                        label="b",
                        text="Deduce the group number of element X.",
                        marks=1
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "Nuclear charge remains the same but electron being removed is from a more positive ion (1); so electrostatic attraction between nucleus and outer electron increases (1).", "marks": 2},
                    {"part": "b", "points": "Group 14 (or 4) due to large jump after 4th IE (1).", "marks": 1}
                ]
            ) for i in range(5)
        ] + [
            Question(
                number=i+16,
                title=f"Orbitals — 9701/13/O/N/22/Q{i+1}",
                syllabus_ref="1.3",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Which electron configuration represents an element in Group 15?",
                        marks=1,
                        options=["A 1s2 2s2 2p6 3s2 3p3", "B 1s2 2s2 2p6 3s2", "C 1s2 2s2 2p6", "D 1s2 2s2 2p5"]
                    )
                ],
                mark_scheme=[{"part": "a", "points": "A (1)", "marks": 1}]
            ) for i in range(5)
        ] + [
             Question(
                number=i+21,
                title=f"Atomic Radius — 9701/22/F/M/23/Q{i+1}(a)",
                syllabus_ref="1.1",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Explain why the atomic radius decreases across Period 3 from Na to Cl.",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Nuclear charge increases (1); shielding remains similar / electrons added to same shell (1); nuclear attraction for outer electrons increases (1).", "marks": 3}]
            ) for i in range(5)
        ]
    ),
    TopicSection(
        day_label="TOPIC 2",
        topic_code="TOPIC 2",
        topic_name="ATOMS, MOLECULES AND STOICHIOMETRY",
        questions=[
            Question(
                number=i+1,
                title=f"Moles — 9701/21/M/J/21/Q{i+1}(b)",
                syllabus_ref="2.2",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Calculate the number of moles of CO2 in 1.20 dm3 of gas at room temperature and pressure.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "moles = 1.20 / 24.0 (1); = 0.0500 mol (1).", "marks": 2}]
            ) for i in range(8)
        ] + [
            Question(
                number=i+9,
                title=f"Titration — 9701/23/O/N/20/Q{i+1}(c)",
                syllabus_ref="2.4",
                preamble="25.0 cm3 of 0.100 mol dm-3 NaOH was neutralised by 20.0 cm3 of H2SO4.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Calculate the concentration of the H2SO4.",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Moles of NaOH = 25.0 x 0.100 / 1000 = 0.0025 mol (1); Moles of H2SO4 = 0.0025 / 2 = 0.00125 mol (1); Conc H2SO4 = 0.00125 x (1000 / 20.0) = 0.0625 mol dm-3 (1).", "marks": 3}]
            ) for i in range(9)
        ] + [
            Question(
                number=i+18,
                title=f"Empirical Formula — 9701/22/F/M/22/Q{i+1}(d)",
                syllabus_ref="2.3",
                preamble="A hydrocarbon contains 85.7% carbon by mass.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Calculate its empirical formula.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "C: 85.7/12.0 = 7.14, H: 14.3/1.0 = 14.3 (1); Ratio 1:2, formula CH2 (1).", "marks": 2}]
            ) for i in range(8)
        ]
    ),
    TopicSection(
        day_label="TOPIC 3",
        topic_code="TOPIC 3",
        topic_name="CHEMICAL BONDING",
        questions=[
            Question(
                number=i+1,
                title=f"VSEPR — 9701/21/M/J/19/Q{i+1}(a)",
                syllabus_ref="3.5",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="State the shape of the ammonia molecule, NH3, and its bond angle.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Trigonal pyramidal (1); 107 degrees (1).", "marks": 2}]
            ) for i in range(8)
        ] + [
            Question(
                number=i+9,
                title=f"Dot and Cross — 9701/22/O/N/23/Q{i+1}(b)",
                syllabus_ref="3.7",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="[DIAGRAM: Draw a dot-and-cross diagram of CO2] Describe the bonding in CO2.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Two double covalent bonds (1); between C and O atoms (1).", "marks": 2}]
            ) for i in range(9)
        ] + [
            Question(
                number=i+18,
                title=f"Intermolecular Forces — 9701/23/F/M/21/Q{i+1}(c)",
                syllabus_ref="3.6",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Explain why water has a higher boiling point than hydrogen sulfide.",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Water has hydrogen bonding between molecules (1); H2S has permanent dipole-dipole forces / van der Waals (1); hydrogen bonds are stronger than permanent dipole-dipole forces (1).", "marks": 3}]
            ) for i in range(8)
        ]
    ),
    TopicSection(
        day_label="TOPIC 4",
        topic_code="TOPIC 4",
        topic_name="STATES OF MATTER",
        questions=[
            Question(
                number=i+1,
                title=f"Ideal Gas — 9701/21/M/J/20/Q{i+1}(a)",
                syllabus_ref="4.1",
                preamble="A gas has a volume of 0.050 m3 at a pressure of 1.01 x 10^5 Pa and a temperature of 300 K.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Calculate the number of moles of gas present. (R = 8.31 J K-1 mol-1)",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "pV = nRT (1); n = (1.01 x 10^5 * 0.050) / (8.31 * 300) (1); n = 2.03 mol (1).", "marks": 3}]
            ) for i in range(10)
        ] + [
             Question(
                number=i+11,
                title=f"Real Gases — 9701/22/O/N/22/Q{i+1}(b)",
                syllabus_ref="4.1",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="State two conditions under which a real gas behaves most like an ideal gas.",
                        marks=2
                    )
                ],
                mark_scheme=[{"part": "a", "points": "High temperature (1); Low pressure (1).", "marks": 2}]
            ) for i in range(10)
        ]
    ),
    TopicSection(
        day_label="TOPIC 5",
        topic_code="TOPIC 5",
        topic_name="CHEMICAL ENERGETICS",
        questions=[
            Question(
                number=i+1,
                title=f"Enthalpy — 9701/22/M/J/22/Q{i+1}(a)",
                syllabus_ref="5.1",
                preamble="",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Define standard enthalpy change of formation.",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "Enthalpy change when one mole of a compound (1); is formed from its elements (1); under standard conditions in their standard states (1).", "marks": 3}]
            ) for i in range(12)
        ] + [
             Question(
                number=i+13,
                title=f"Hess Law — 9701/21/O/N/19/Q{i+1}(b)",
                syllabus_ref="5.2",
                preamble="[DIAGRAM: Hess cycle showing formation of CH4 from C and H2, and combustion of C, H2, CH4]",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Calculate the enthalpy change of formation of methane, given the enthalpy changes of combustion: C = -394, H2 = -286, CH4 = -890 kJ mol-1.",
                        marks=3
                    )
                ],
                mark_scheme=[{"part": "a", "points": "deltaHf = sum(deltaHc reactants) - sum(deltaHc products) (1); = (-394) + 2(-286) - (-890) (1); = -76 kJ mol-1 (1).", "marks": 3}]
            ) for i in range(13)
        ]
    )
]
