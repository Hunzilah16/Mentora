"""
Defines Questions 25 to 50 for Topic 1: Atomic Structure and appends them to topic1_data.py.
"""

new_questions_code = '''
    # =========================================================================
    # ADDITIONAL QUESTIONS (Q25 to Q50)
    # =========================================================================
    
    # ── SUBTOPIC 1.1: Particles in the Atom & Atomic Radius (Continued) ─────
    Question(
        number=25,
        title="Deflection of Particles in Electric Fields — 9701/22/F/M/24/Q1(a)-(c)",
        syllabus_ref="1.1",
        difficulty="HARD",
        preamble="Fig. 25.1 shows the paths of three different beams of subatomic particles passing through a uniform electric field between two charged parallel plates.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\electric_field_deflection.png",
        figure_caption="Fig. 25.1 Deflection of subatomic particles in a uniform electric field",
        parts=[
            QuestionPart(
                label="a",
                text="State the identity of the particles responsible for each of the three paths shown in Fig. 25.1.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why electrons are deflected by a significantly greater angle than protons, even though both carry the same magnitude of electric charge.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State two factors that determine the angle of deflection of a charged particle in a uniform electric field.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Path deflected towards positive plate: electrons (1); Straight path: neutrons (1); Path deflected towards negative plate: protons (1)", "marks": 3},
            {"part": "b", "points": "Deflection angle is proportional to charge/mass (q/m) ratio (1); Electrons have a mass roughly 1/1840 of a proton, giving a vastly higher q/m ratio and greater acceleration (1)", "marks": 2},
            {"part": "c", "points": "Charge on the particle / mass of the particle (or charge-to-mass ratio) (1); Strength of electric field / velocity (speed) of the particle (1)", "marks": 2}
        ]
    ),
    Question(
        number=26,
        title="Deducing Subatomic Particle Numbers in Ions — 9701/12/M/J/23/Q1",
        syllabus_ref="1.1",
        difficulty="EASY",
        preamble="Table 26.1 lists four different ionic species.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the number of protons, neutrons, and electrons present in one 34S2- ion.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the number of protons, neutrons, and electrons present in one 56Fe3+ ion.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State which two of the following ions contain the same number of neutrons: 39K+, 40Ca2+, 35Cl-, 37Cl-.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Protons = 16 (1); Neutrons = 34 - 16 = 18 (1); Electrons = 16 + 2 = 18 (1)", "marks": 3},
            {"part": "b", "points": "Protons = 26 (1); Neutrons = 56 - 26 = 30 (1); Electrons = 26 - 3 = 23 (1)", "marks": 3},
            {"part": "c", "points": "39K+ (39-19=20) and 40Ca2+ (40-20=20) (1)", "marks": 1}
        ]
    ),
    Question(
        number=27,
        title="Trends in Halogen and Halide Radii — 9701/21/O/N/23/Q1(b)",
        syllabus_ref="1.1",
        difficulty="EASY",
        preamble="The Group 17 elements (halogens) form halide ions with a 1- charge.",
        parts=[
            QuestionPart(
                label="a",
                text="Describe and explain the trend in atomic radius down Group 17 from fluorine to iodine.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Explain why the ionic radius of a bromide ion, Br-, is greater than the covalent radius of a bromine atom, Br.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Atomic radius increases down the group (1); Number of occupied principal electron shells increases (1); Outermost electrons are further from the nucleus and experience increased inner-shell shielding (1)", "marks": 3},
            {"part": "b", "points": "Br- gains an electron into the 4p sub-shell, increasing electron-electron repulsion (1); The nuclear charge (+35) remains unchanged, allowing the electron cloud to expand (1)", "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Specific Charge Calculations — 9701/22/M/J/20/Q1(b)",
        syllabus_ref="1.1",
        difficulty="HARD",
        preamble="The specific charge of a particle is defined as the ratio of its electric charge to its mass.",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the specific charge (in C kg⁻¹) of a proton. (Elementary charge e = 1.60 × 10⁻¹⁹ C; proton mass mp = 1.67 × 10⁻²⁷ kg).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the specific charge of an alpha particle (4He2+).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State the ratio of the specific charge of an electron to that of a proton.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "q/m = 1.60 × 10⁻¹⁹ / 1.67 × 10⁻²⁷ (1) = 9.58 × 10⁷ C kg⁻¹ (1)", "marks": 2},
            {"part": "b", "points": "q = 2 × (1.60 × 10⁻¹⁹) = 3.20 × 10⁻¹⁹ C, m = 4 × (1.67 × 10⁻²⁷) = 6.68 × 10⁻²⁷ kg (1); q/m = 4.79 × 10⁷ C kg⁻¹ (1)", "marks": 2},
            {"part": "c", "points": "Approximately 1836 to 1840 : 1 (1)", "marks": 1}
        ]
    ),
    Question(
        number=29,
        title="Effective Nuclear Charge Across Period 3 — 9701/23/M/J/21/Q1(a)",
        syllabus_ref="1.1",
        difficulty="HARD",
        preamble="Effective nuclear charge (Zeff) is the net positive charge experienced by valence electrons, taking into account shielding by core electrons.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why the core electron shielding remains approximately constant across Period 3 from Na to Cl.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe how effective nuclear charge (Zeff) changes from Na to Cl, and relate this to the decrease in atomic radius.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "All Period 3 elements possess the identical core electron configuration 1s2 2s2 2p6 (10 core electrons) (1); Incoming valence electrons are added to the same outermost principal quantum shell (n=3) (1)", "marks": 2},
            {"part": "b", "points": "Nuclear charge increases by +1 with each successive element (from +11 to +17) (1); Because core shielding is constant, Zeff increases steadily across the period (1); Greater Zeff pulls the valence shell closer to the nucleus, causing atomic radius to decrease (1)", "marks": 3}
        ]
    ),
    Question(
        number=30,
        title="Rutherford Alpha-Scattering and Nuclear Model — 9701/21/M/J/19/Q1(a)",
        syllabus_ref="1.1",
        difficulty="EASY",
        preamble="In the Geiger-Marsden experiment, a thin gold foil was bombarded with alpha particles.",
        parts=[
            QuestionPart(
                label="a",
                text="State the observation from the experiment that showed that most of the atom is empty space.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State the observation that proved the existence of a small, dense, positively charged nucleus.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Most alpha particles passed straight through the gold foil with little or no deflection (1)", "marks": 1},
            {"part": "b", "points": "A small fraction of alpha particles were deflected through very large angles (> 90°) / bounced straight back (1); Showing that the positive charge and mass are concentrated in a tiny central nucleus (1)", "marks": 2}
        ]
    ),

    # ── SUBTOPIC 1.2: Isotopes & Mass Spectrometry (Continued) ───────────────
    Question(
        number=31,
        title="High-Resolution Mass Spectrum of Zirconium — 9701/22/O/N/21/Q2(a)",
        syllabus_ref="1.2",
        difficulty="HARD",
        preamble="Fig. 31.1 displays the mass spectrum of a naturally occurring sample of zirconium.",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\zirconium_mass_spectrum.png",
        figure_caption="Fig. 31.1 Mass spectrum of a naturally occurring zirconium sample",
        parts=[
            QuestionPart(
                label="a",
                text="State the number of stable isotopes of zirconium indicated by Fig. 31.1.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Using the isotopic abundance data from Fig. 31.1, calculate the relative atomic mass (Ar) of zirconium to two decimal places.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="State the number of neutrons present in the most abundant isotope of zirconium (atomic number Z = 40).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "5 isotopes (1)", "marks": 1},
            {"part": "b", "points": "Ar = [(90 × 51.5) + (91 × 11.2) + (92 × 17.1) + (94 × 17.4) + (96 × 2.8)] / 100 (1); Ar = [4635.0 + 1019.2 + 1573.2 + 1635.6 + 268.8] / 100 = 9131.8 / 100 (1); Ar = 91.32 (must be 2 d.p.) (1)", "marks": 3},
            {"part": "c", "points": "Most abundant is 90Zr; neutrons = 90 - 40 = 50 (1)", "marks": 1}
        ]
    ),
    Question(
        number=32,
        title="Algebraic Determination of Boron Isotopes — 9701/11/F/M/22/Q2",
        syllabus_ref="1.2",
        difficulty="EASY",
        preamble="Naturally occurring boron has a relative atomic mass of 10.81 and consists exclusively of two isotopes: 10B and 11B.",
        parts=[
            QuestionPart(
                label="a",
                text="Which row gives the correct percentage abundance of 10B and 11B in natural boron?",
                marks=1,
                num_answer_lines=0,
                options=[
                    "A 10B = 10.0%, 11B = 90.0%",
                    "B 10B = 19.0%, 11B = 81.0%",
                    "C 10B = 50.0%, 11B = 50.0%",
                    "D 10B = 81.0%, 11B = 19.0%"
                ]
            ),
            QuestionPart(
                label="b",
                text="Show how the correct percentage abundances in part (a) can be calculated mathematically.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "B — 10B = 19.0%, 11B = 81.0% (1)", "marks": 1},
            {"part": "b", "points": "10.81 = [10x + 11(100 - x)] / 100 (1); 1081 = 1100 - x => x = 19.0% (1)", "marks": 2}
        ]
    ),
    Question(
        number=33,
        title="Mass Spectrometry of Lead Isotopes — 9701/22/M/J/23/Q1(a)",
        syllabus_ref="1.2",
        difficulty="HARD",
        preamble="A sample of lead extracted from radioactive galena ore contains the four stable isotopes 204Pb, 206Pb, 207Pb, and 208Pb in relative abundances 1.4%, 24.1%, 22.1%, and 52.4% respectively.",
        parts=[
            QuestionPart(
                label="a",
                text="Define the term relative isotopic mass.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Calculate the relative atomic mass of this sample of lead to one decimal place.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Mass of an atom of an isotope (1); relative to 1/12th of the mass of an atom of carbon-12 (1)", "marks": 2},
            {"part": "b", "points": "Ar = [(204 × 1.4) + (206 × 24.1) + (207 × 22.1) + (208 × 52.4)] / 100 (1); Ar = [285.6 + 4964.6 + 4574.7 + 10899.2] / 100 = 20724.1 / 100 (1); Ar = 207.2 (1)", "marks": 3}
        ]
    ),
    Question(
        number=34,
        title="Diatomic Bromine Molecular Ion Peak Ratios — 9701/21/O/N/24/Q1(b)",
        syllabus_ref="1.2",
        difficulty="HARD",
        preamble="Bromine consists of 79Br and 81Br in an exact 1:1 abundance ratio. When gaseous bromine, Br2, is introduced into a mass spectrometer, molecular ions [Br2]+ are formed.",
        parts=[
            QuestionPart(
                label="a",
                text="List the m/z values of the three molecular ion peaks observed in the mass spectrum of Br2.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Deduce the ratio of the heights of the three peaks identified in part (a), showing your probability calculation.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "m/z = 158 (79Br-79Br), m/z = 160 (79Br-81Br and 81Br-79Br), m/z = 162 (81Br-81Br) (2 marks for all three, 1 mark for any two) (2)", "marks": 2},
            {"part": "b", "points": "Prob(158) = 0.5 × 0.5 = 0.25 (1); Prob(160) = 2 × (0.5 × 0.5) = 0.50 (1); Prob(162) = 0.5 × 0.5 = 0.25, giving ratio 1 : 2 : 1 (1)", "marks": 3}
        ]
    ),
    Question(
        number=35,
        title="The Carbon-12 Standard and Unified Atomic Mass — 9701/23/M/J/22/Q1(c)",
        syllabus_ref="1.2",
        difficulty="EASY",
        preamble="All atomic mass measurements in modern chemistry are calibrated against the unified atomic mass standard.",
        parts=[
            QuestionPart(
                label="a",
                text="State the exact mass assigned by definition to one atom of carbon-12.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the relative atomic mass of chlorine is 35.5 and not an integer, whereas the mass number of any individual isotope is always an integer.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Exactly 12 unified atomic mass units (or 12 u / 12 Da) (1)", "marks": 1},
            {"part": "b", "points": "Mass number is the sum of whole protons and neutrons in a single nucleus (integers) (1); Relative atomic mass is a weighted average of isotopic masses based on natural abundance (1)", "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Principles of Time-of-Flight (TOF) Mass Spectrometry — 9701/22/F/M/25/Q1(a)",
        syllabus_ref="1.2",
        difficulty="EASY",
        preamble="In a time-of-flight (TOF) mass spectrometer, particles undergo four fundamental stages.",
        parts=[
            QuestionPart(
                label="a",
                text="Name the four successive stages in TOF mass spectrometry.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why all ions are given the same kinetic energy during the acceleration stage.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Deduce how the flight time of an ion in the drift region relates to its mass-to-charge ratio (m/z).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Ionisation, acceleration, ion drift / flight tube, detection (2 marks for all four, 1 mark for any two/three) (2)", "marks": 2},
            {"part": "b", "points": "Ions are accelerated by an electric potential difference (V) so that KE = 1/2 mv² = qV (1); With constant KE, velocity depends solely on the mass of the ion (1)", "marks": 2},
            {"part": "c", "points": "Lighter ions (lower m/z) travel faster and arrive at the detector in a shorter time (1); Flight time is proportional to √(m/z) (1)", "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Determining Unknown Isotopic Mass from Peak Heights — 9701/21/M/J/25/Q1(c)",
        syllabus_ref="1.2",
        difficulty="HARD",
        preamble="Silicon has Ar = 28.09. Its mass spectrum shows three peaks: 28Si (92.2%), 29Si (4.7%), and an unknown isotope ASi (3.1%).",
        parts=[
            QuestionPart(
                label="a",
                text="Calculate the mass number A of the third isotope of silicon. Show your working clearly.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="b",
                text="Deduce the number of neutrons in an atom of this third isotope (silicon atomic number = 14).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "28.09 = [(28 × 92.2) + (29 × 4.7) + (A × 3.1)] / 100 (1); 2809 = 2581.6 + 136.3 + 3.1A => 3.1A = 91.1 (1); A = 91.1 / 3.1 = 29.39 => mass number A = 30 (1)", "marks": 3},
            {"part": "b", "points": "Neutrons = 30 - 14 = 16 (1)", "marks": 1}
        ]
    ),

    # ── SUBTOPIC 1.3: Electrons, Energy Levels & Orbitals (Continued) ────────
    Question(
        number=38,
        title="Chromium and Copper Anomalous Configurations — 9701/22/M/J/20/Q2(a)",
        syllabus_ref="1.3",
        difficulty="HARD",
        preamble="Chromium (Z = 24) and copper (Z = 29) do not follow the standard Aufbau filling pattern across the first transition series.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the full electronic configuration (1s²...) of a neutral chromium atom.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the [Ar] 3d5 4s1 configuration of chromium is energetically favoured over [Ar] 3d4 4s2.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Write the full electronic configuration of a copper(I) ion, Cu+.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "1s2 2s2 2p6 3s2 3p6 3d5 4s1 (1)", "marks": 1},
            {"part": "b", "points": "A half-filled 3d5 sub-shell possesses extra exchange energy / symmetrical stability (1); Symmetrical distribution of spin-aligned electrons minimizes inter-electronic repulsion (1)", "marks": 2},
            {"part": "c", "points": "1s2 2s2 2p6 3s2 3p6 3d10 (4s electron is removed first) (1)", "marks": 1}
        ]
    ),
    Question(
        number=39,
        title="Electron Configurations of Transition Metal Ions — 9701/21/O/N/20/Q2(b)",
        syllabus_ref="1.3",
        difficulty="EASY",
        preamble="When d-block transition metals form positive ions, electrons are lost in a specific order.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the shorthand noble gas core configuration for the Co2+ ion (Z = 27).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the shorthand configuration for the Ni2+ ion (Z = 28).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the 4s electrons are removed before 3d electrons when forming transition metal cations.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "[Ar] 3d7 (1)", "marks": 1},
            {"part": "b", "points": "[Ar] 3d8 (1)", "marks": 1},
            {"part": "c", "points": "Once electrons occupy 3d orbitals, they shield the 4s electrons (1); 3d orbitals drop to a lower energy level than 4s, making 4s electrons the outermost valence electrons (1)", "marks": 2}
        ]
    ),
    Question(
        number=40,
        title="Shell Capacities and Orbital Sub-Shells — 9701/12/O/N/22/Q3",
        syllabus_ref="1.3",
        difficulty="EASY",
        preamble="The quantum mechanical model defines orbitals by principal quantum number n and orbital quantum type.",
        parts=[
            QuestionPart(
                label="a",
                text="What is the total maximum number of electrons that can be held in the fourth principal quantum shell (n = 4)?",
                marks=1,
                num_answer_lines=0,
                options=["A 16", "B 18", "C 32", "D 50"]
            ),
            QuestionPart(
                label="b",
                text="State the names of all four sub-shells present in the n = 4 shell, and state the number of orbitals in each.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "C — 32 electrons (2n² = 2 × 4² = 32) (1)", "marks": 1},
            {"part": "b", "points": "4s (1 orbital), 4p (3 orbitals), 4d (5 orbitals), 4f (7 orbitals) (2 marks for all four correct, 1 mark for any two/three) (2)", "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Orbital Geometry and Degeneracy — 9701/22/F/M/23/Q2(a)",
        syllabus_ref="1.3",
        difficulty="HARD",
        preamble="Electrons reside in three-dimensional probability distributions termed atomic orbitals.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain the meaning of the term degenerate orbitals.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Describe the spatial orientation of the three degenerate 2p orbitals: 2px, 2py, and 2pz.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="State two differences between a 1s orbital and a 2s orbital.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Orbitals that possess identical energy levels within an isolated atom (1)", "marks": 1},
            {"part": "b", "points": "Dumbbell-shaped lobes oriented mutually perpendicular (at 90° angles) to one another along the x, y, and z Cartesian axes (1); Each with an electron nodal plane at the nucleus (1)", "marks": 2},
            {"part": "c", "points": "A 2s orbital is larger in size / has greater radial extent than 1s (1); A 2s orbital has higher energy than 1s (or 2s has a radial node) (1)", "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Electron Configurations of Anions — 9701/21/M/J/22/Q2(b)",
        syllabus_ref="1.3",
        difficulty="EASY",
        preamble="Non-metal atoms gain electrons to achieve stable noble-gas valence electron configurations.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the full electron configuration of a phosphide ion, P3-.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="State which noble gas has the identical electron configuration to a P3- ion.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the electron configuration of an oxide ion, O2-.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "1s2 2s2 2p6 3s2 3p6 (1)", "marks": 1},
            {"part": "b", "points": "Argon / Ar (1)", "marks": 1},
            {"part": "c", "points": "1s2 2s2 2p6 (1)", "marks": 1}
        ]
    ),
    Question(
        number=43,
        title="Pauli Exclusion Principle and Orbital Diagrams — 9701/23/M/J/24/Q2(a)",
        syllabus_ref="1.3",
        difficulty="HARD",
        preamble="The Pauli exclusion principle states that an orbital can hold a maximum of two electrons, provided they have opposite spins.",
        parts=[
            QuestionPart(
                label="a",
                text="Explain why two electrons occupying the same orbital must possess opposite spins.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Describe an electrons-in-boxes diagram for an oxygen atom (Z = 8), indicating the number of paired and unpaired electrons in the 2p sub-shell.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Opposite spins generate opposing magnetic fields (1); This partially cancels the electrostatic repulsion between two negatively charged electrons in the same space (1)", "marks": 2},
            {"part": "b", "points": "Three 2p boxes drawn (1); One box contains two paired opposite-spin arrows; the remaining two boxes each contain one single parallel arrow (1); Resulting in 1 paired orbital and 2 unpaired electrons (1)", "marks": 3}
        ]
    ),

    # ── SUBTOPIC 1.4: Ionisation Energy (Continued) ──────────────────────────
    Question(
        number=44,
        title="Comparing Period 2 and Period 3 First Ionisation Energies — 9701/22/M/J/23/Q2(a)-(c)",
        syllabus_ref="1.4",
        difficulty="HARD",
        preamble="Fig. 44.1 compares the first ionisation energies of the elements across Period 2 (Li to Ne) and Period 3 (Na to Ar).",
        figure_path=r"z:\\tests n quizes63\\books\\psycology\\new styl\\figures\\period2_vs_period3_ie.png",
        figure_caption="Fig. 44.1 Comparison of first ionisation energies across Period 2 and Period 3",
        parts=[
            QuestionPart(
                label="a",
                text="State two general similarities in the pattern of first ionisation energies across Period 2 and Period 3 shown in Fig. 44.1.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why every Period 3 element has a significantly lower first ionisation energy than its corresponding Group counterpart in Period 2.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="c",
                text="Identify the two pairs of elements that display anomalies (dips) in both Period 2 and Period 3.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Both periods show a general increase from Group 1 to Group 18 (1); Both display two dips: between Groups 2 and 13, and between Groups 15 and 16 (1)", "marks": 2},
            {"part": "b", "points": "Period 3 elements have their outermost electron in the n=3 shell whereas Period 2 is in n=2 (1); The outer electron is further from the nucleus (larger atomic radius) (1); Greater shielding from inner core electron shells outweighs the increased nuclear charge (1)", "marks": 3},
            {"part": "c", "points": "Between Be and B in Period 2 / Mg and Al in Period 3 (1); Between N and O in Period 2 / P and S in Period 3 (1)", "marks": 2}
        ]
    ),
    Question(
        number=45,
        title="Nitrogen vs Oxygen Ionisation Energy Anomaly — 9701/21/O/N/21/Q2(a)",
        syllabus_ref="1.4",
        difficulty="HARD",
        preamble="The first ionisation energy of nitrogen is 1402 kJ mol⁻¹, whereas that of oxygen is lower at 1314 kJ mol⁻¹, despite oxygen having a greater nuclear charge (+8 vs +7).",
        parts=[
            QuestionPart(
                label="a",
                text="Write the electronic configuration of a nitrogen atom and of an oxygen atom in 2p orbital notation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Explain why the first ionisation energy of oxygen is lower than that of nitrogen.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Nitrogen: 2px1 2py1 2pz1 (1); Oxygen: 2px2 2py1 2pz1 (1)", "marks": 2},
            {"part": "b", "points": "In oxygen, two electrons must pair up in one 2p orbital (1); The mutual electrostatic repulsion between the two paired electrons in the same orbital destabilizes them (1); This spin-pair repulsion makes one electron easier to remove despite the higher nuclear charge of oxygen (1)", "marks": 3}
        ]
    ),
    Question(
        number=46,
        title="Successive Ionisation Energies of Sodium — 9701/22/O/N/22/Q2(c)",
        syllabus_ref="1.4",
        difficulty="HARD",
        preamble="The 11 successive ionisation energies of sodium (in kJ mol⁻¹) are: 496, 4563, 6913, 9544, 13352, 16611, 20115, 25491, 28934, 141367, 159079.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify between which two successive ionisations the first very large jump occurs.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Explain why the 2nd ionisation energy of sodium is nearly 10 times greater than its 1st ionisation energy.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain why there is an immense jump between the 9th and 10th ionisation energies.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Between the 1st and 2nd ionisation energies (4563 vs 496 kJ mol⁻¹) (1)", "marks": 1},
            {"part": "b", "points": "The 1st electron is removed from the outer 3s shell; the 2nd electron is removed from the inner, complete 2p shell (1); The 2p electron is much closer to the nucleus and experiences much less shielding (1)", "marks": 2},
            {"part": "c", "points": "The 10th and 11th electrons are removed from the innermost 1s principal quantum shell (n=1) (1); They are closest to the nucleus with zero inner shielding, experiencing maximum nuclear attraction (1)", "marks": 2}
        ]
    ),
    Question(
        number=47,
        title="Deducing Identity from Successive IE Table — 9701/22/F/M/24/Q2(a)",
        syllabus_ref="1.4",
        difficulty="EASY",
        preamble="An element Z in Period 2 of the Periodic Table exhibits the following first six ionisation energies: 1086, 2353, 4621, 6223, 37832, 47278 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="a",
                text="Identify the group of the Periodic Table to which element Z belongs. Justify your answer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="Deduce the chemical identity of element Z.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Write the formula of the oxide formed by element Z in which Z displays its maximum oxidation state.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Group 14 (or Group 4) (1); There is a massive jump between the 4th and 5th ionisation energies (6223 to 37832), indicating 4 valence electrons before breaking into an inner shell (1)", "marks": 2},
            {"part": "b", "points": "Carbon / C (Period 2, Group 14) (1)", "marks": 1},
            {"part": "c", "points": "CO2 (1)", "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Ionisation Energy Trends Down Group 1 — 9701/11/M/J/24/Q4",
        syllabus_ref="1.4",
        difficulty="EASY",
        preamble="The first ionisation energies of Group 1 metals (alkali metals) are: Li (520), Na (496), K (419), Rb (403), Cs (376 kJ mol⁻¹).",
        parts=[
            QuestionPart(
                label="a",
                text="Which factor is primarily responsible for the decrease in first ionisation energy down Group 1?",
                marks=1,
                num_answer_lines=0,
                options=[
                    "A Decreasing nuclear charge",
                    "B Increased atomic radius and shielding by inner electron shells",
                    "C Decreasing metallic bond strength",
                    "D Decreasing proton-to-neutron ratio"
                ]
            ),
            QuestionPart(
                label="b",
                text="Explain why the increase in nuclear charge down Group 1 does not lead to an increase in first ionisation energy.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "B — Increased atomic radius and shielding by inner electron shells (1)", "marks": 1},
            {"part": "b", "points": "Each row down the group adds a completely new principal quantum shell of core electrons (1); The shielding effect and greater distance of the valence electron from the nucleus outweigh the added nuclear charge (1)", "marks": 2}
        ]
    ),
    Question(
        number=49,
        title="Thermochemical Equations for Ionisation Energies — 9701/21/M/J/21/Q2(a)",
        syllabus_ref="1.4",
        difficulty="EASY",
        preamble="Equations representing ionisation energies must be balanced and include correct state symbols.",
        parts=[
            QuestionPart(
                label="a",
                text="Write the equation representing the first ionisation energy of aluminium.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="b",
                text="Write the equation representing the third ionisation energy of aluminium.",
                marks=2,
                num_answer_lines=2
            ),
            QuestionPart(
                label="c",
                text="Explain why the 3rd ionisation energy of aluminium (2745 kJ mol⁻¹) is significantly higher than its 1st ionisation energy (578 kJ mol⁻¹).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Al(g) -> Al+(g) + e- (1)", "marks": 1},
            {"part": "b", "points": "Al2+(g) -> Al3+(g) + e- (1 mark for formulae and charge, 1 mark for (g) state symbols) (2)", "marks": 2},
            {"part": "c", "points": "The 3rd electron is removed from a dipositive cation (Al2+) with +13 nuclear charge attracting only 11 remaining electrons (1); Greater effective attraction and smaller ionic radius require much more energy (1)", "marks": 2}
        ]
    ),
    Question(
        number=50,
        title="Synoptic Problem: Atomic Structure & Ionisation Energies — 9701/22/O/N/25/Q1",
        syllabus_ref="1.4",
        difficulty="HARD",
        preamble="Element M is a reactive metal. Its mass spectrum indicates a single isotope with nucleon number 24. Its first three ionisation energies are 738, 1451, and 7733 kJ mol⁻¹.",
        parts=[
            QuestionPart(
                label="a",
                text="Deduce the group number of element M from its ionisation energy data, and write the full electron configuration of element M.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="b",
                text="State the number of protons, neutrons, and electrons in an M2+ ion.",
                marks=3,
                num_answer_lines=3
            ),
            QuestionPart(
                label="c",
                text="Explain, with reference to energy levels and sub-shells, why the jump between the 2nd and 3rd ionisation energies is so large.",
                marks=3,
                num_answer_lines=4
            )
        ],
        mark_scheme=[
            {"part": "a", "points": "Group 2 (large jump between 2nd and 3rd IE) (1); Electron configuration: 1s2 2s2 2p6 3s2 (1)", "marks": 2},
            {"part": "b", "points": "Protons = 12 (1); Neutrons = 24 - 12 = 12 (1); Electrons = 12 - 2 = 10 (1)", "marks": 3},
            {"part": "c", "points": "The first two electrons are removed from the outer 3s sub-shell (n=3) (1); The 3rd electron is removed from the inner, complete 2p sub-shell (n=2) (1); The 2p sub-shell is much closer to the nucleus, has significantly less shielding, and experiences an immensely stronger electrostatic pull (1)", "marks": 3}
        ]
    )
]
'''

with open(r"z:\tests n quizes63\books\psycology\new styl\topic1_data.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the closing bracket ']' with new_questions_code
if content.rstrip().endswith("]"):
    content_without_close = content.rstrip()[:-1].rstrip()
    updated_content = content_without_close + ",\n" + new_questions_code
    with open(r"z:\tests n quizes63\books\psycology\new styl\topic1_data.py", "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Successfully appended Questions 25-50 to topic1_data.py!")
else:
    print("Could not find trailing ']' to replace.")
