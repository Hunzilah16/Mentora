from generate_pdf import TopicSection, Question, QuestionPart

topics = [
    TopicSection(
        day_label="TOPIC 18",
        topic_code="TOPIC 18",
        topic_name="CARBOXYLIC ACIDS AND DERIVATIVES",
        questions=[
            Question(
                number=i+1,
                title=f"Carboxylic Acids and Derivatives — 9701/22/M/J/23/Q{i+1}(a)",
                syllabus_ref="18.1" if i < 10 else "18.2",
                preamble=f"Question {i+1} on Carboxylic Acids and Derivatives.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="State the reagents and conditions required to form a carboxylic acid from a primary alcohol.",
                        marks=2,
                    ) if i % 2 == 0 else QuestionPart(
                        label="a",
                        text="Which reagent can be used to reduce a carboxylic acid to a primary alcohol?",
                        marks=1,
                        options=["A NaBH4", "B LiAlH4", "C H2/Ni", "D Sn/HCl"]
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "K2Cr2O7 / acidified (1); reflux (1)" if i % 2 == 0 else "B (1)", "marks": 2 if i % 2 == 0 else 1},
                ],
            ) for i in range(20)
        ]
    ),
    TopicSection(
        day_label="TOPIC 19",
        topic_code="TOPIC 19",
        topic_name="NITROGEN COMPOUNDS",
        questions=[
            Question(
                number=i+1,
                title=f"Nitrogen Compounds — 9701/21/O/N/23/Q{i+1}(b)",
                syllabus_ref="19.1" if i < 10 else "19.2",
                preamble=f"Question {i+1} on Nitrogen Compounds.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Describe the formation of ethylamine from bromoethane.",
                        marks=2,
                    ) if i % 2 == 0 else QuestionPart(
                        label="a",
                        text="Explain why ethylamine is a stronger base than ammonia.",
                        marks=2,
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "NH3 in ethanol (1); heat under pressure (1)" if i % 2 == 0 else "Ethyl group is electron-donating / has positive inductive effect (1); increases electron density on nitrogen lone pair (1)", "marks": 2},
                ],
            ) for i in range(20)
        ]
    ),
    TopicSection(
        day_label="TOPIC 20",
        topic_code="TOPIC 20",
        topic_name="POLYMERISATION",
        questions=[
            Question(
                number=i+1,
                title=f"Polymerisation — 9701/23/F/M/24/Q{i+1}(c)",
                syllabus_ref="20.1",
                preamble=f"Question {i+1} on Polymerisation. [DIAGRAM: structure of monomer]",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Draw one repeat unit of the addition polymer formed from this monomer.",
                        marks=1,
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "Correct repeat unit with continuation bonds (1)", "marks": 1},
                ],
            ) for i in range(20)
        ]
    ),
    TopicSection(
        day_label="TOPIC 21",
        topic_code="TOPIC 21",
        topic_name="ORGANIC SYNTHESIS",
        questions=[
            Question(
                number=i+1,
                title=f"Organic Synthesis — 9701/22/M/J/25/Q{i+1}(d)",
                syllabus_ref="21.1",
                preamble=f"Question {i+1} on Organic Synthesis. Fig. 1.1 shows a multi-step synthesis.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Deduce the structure of the intermediate compound and state the reagents for step 1.",
                        marks=2,
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "Correct structure (1); correct reagents (1)", "marks": 2},
                ],
            ) for i in range(20)
        ]
    ),
    TopicSection(
        day_label="TOPIC 22",
        topic_code="TOPIC 22",
        topic_name="ANALYTICAL TECHNIQUES",
        questions=[
            Question(
                number=i+1,
                title=f"Analytical Techniques — 9701/21/O/N/25/Q{i+1}(e)",
                syllabus_ref="22.1" if i < 12 else "22.2",
                preamble=f"Question {i+1} on Analytical Techniques. Fig. 2.1 shows an IR spectrum.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Identify the functional group responsible for the broad absorption at 3200-3600 cm-1.",
                        marks=1,
                    ) if i % 2 == 0 else QuestionPart(
                        label="a",
                        text="State the significance of the molecular ion peak in a mass spectrum.",
                        marks=1,
                    )
                ],
                mark_scheme=[
                    {"part": "a", "points": "O-H / alcohol (1)" if i % 2 == 0 else "Gives the relative molecular mass of the compound (1)", "marks": 1},
                ],
            ) for i in range(25)
        ]
    )
]
