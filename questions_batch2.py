from generate_pdf import TopicSection, Question, QuestionPart

topics = []

# TOPIC 6 - ELECTROCHEMISTRY
t6_qs = []
for i in range(1, 21):
    is_mcq = (i <= 8)
    variant = [21, 22, 23, 24][i % 4]
    session = ["M/J", "O/N", "F/M"][i % 3]
    year = 19 + (i % 6)
    
    if i % 2 == 0:
        title = f"Redox Processes — 9701/{variant}/{session}/{year}/Q1(a)"
        subtopic = "6.1"
    else:
        title = f"Electrolysis — 9701/{variant}/{session}/{year}/Q2(b)"
        subtopic = "6.2"
        
    if is_mcq:
        t6_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="What is the oxidation number of sulfur in H2SO4?",
            parts=[QuestionPart(label="a", text="Select the correct option.", marks=1, options=["A +2", "B +4", "C +6", "D -2"])],
            mark_scheme=[{"part": "a", "points": "C (1)", "marks": 1}]
        ))
    else:
        t6_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="A molten salt is electrolysed.",
            parts=[QuestionPart(label="a", text=f"Calculate the mass of metal deposited when a current of {i*2} A flows for 30 minutes. (Ar = {50+i}, charge = +2).", marks=3)],
            mark_scheme=[{"part": "a", "points": f"Q = It = {i*2} * 1800 (1); moles of e- = Q/96500 (1); mass = moles/2 * Ar (1)", "marks": 3}]
        ))

topics.append(TopicSection(day_label="TOPIC 6", topic_code="TOPIC 6", topic_name="ELECTROCHEMISTRY", questions=t6_qs))

# TOPIC 7 - EQUILIBRIA
t7_qs = []
for i in range(1, 26):
    is_mcq = (i <= 10)
    variant = [21, 22, 23, 24][i % 4]
    session = ["M/J", "O/N", "F/M"][i % 3]
    year = 19 + (i % 6)
    title = f"Chemical Equilibria — 9701/{variant}/{session}/{year}/Q3(c)"
    subtopic = "7.1" if i % 2 == 0 else "7.2"
    
    if is_mcq:
        t7_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="[DIAGRAM: Haber process equilibrium curve]",
            parts=[QuestionPart(label="a", text="Which condition increases the yield of NH3?", marks=1, options=["A High T, Low P", "B Low T, High P", "C Low T, Low P", "D High T, High P"])],
            mark_scheme=[{"part": "a", "points": "B (1)", "marks": 1}]
        ))
    else:
        t7_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="Consider the dynamic equilibrium: A + B <=> C + D",
            parts=[
                QuestionPart(label="a", text="Define the term dynamic equilibrium.", marks=2),
                QuestionPart(label="b", text="Explain the effect of adding a catalyst on the position of equilibrium.", marks=2)
            ],
            mark_scheme=[
                {"part": "a", "points": "Rate of forward reaction equals rate of backward reaction (1); concentrations of reactants and products remain constant (1)", "marks": 2},
                {"part": "b", "points": "No effect on position of equilibrium (1); increases rate of forward and backward reactions equally (1)", "marks": 2}
            ]
        ))

topics.append(TopicSection(day_label="TOPIC 7", topic_code="TOPIC 7", topic_name="EQUILIBRIA", questions=t7_qs))

# TOPIC 8 - REACTION KINETICS
t8_qs = []
for i in range(1, 21):
    is_mcq = (i <= 8)
    variant = [21, 22, 23, 24][i % 4]
    session = ["M/J", "O/N", "F/M"][i % 3]
    year = 19 + (i % 6)
    title = f"Rates of Reaction — 9701/{variant}/{session}/{year}/Q4(d)"
    subtopic = f"8.{1 + (i%3)}"
    
    if is_mcq:
        t8_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble=f"Fig {i}.1 shows a Boltzmann distribution curve.",
            parts=[QuestionPart(label="a", text="What happens to the peak of the curve at a higher temperature?", marks=1, options=["A Moves left and higher", "B Moves right and lower", "C Moves right and higher", "D Moves left and lower"])],
            mark_scheme=[{"part": "a", "points": "B (1)", "marks": 1}]
        ))
    else:
        t8_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="The rate of a reaction was measured at different temperatures.",
            parts=[QuestionPart(label="a", text="Use the Boltzmann distribution to explain why a small increase in temperature leads to a large increase in reaction rate.", marks=3)],
            mark_scheme=[{"part": "a", "points": "More particles have energy >= activation energy (1); more successful collisions per unit time (1); higher frequency of collisions (1)", "marks": 3}]
        ))

topics.append(TopicSection(day_label="TOPIC 8", topic_code="TOPIC 8", topic_name="REACTION KINETICS", questions=t8_qs))

# TOPIC 9 - THE PERIODIC TABLE: CHEMICAL PERIODICITY
t9_qs = []
for i in range(1, 26):
    is_mcq = (i <= 10)
    variant = [21, 22, 23, 24][i % 4]
    session = ["M/J", "O/N", "F/M"][i % 3]
    year = 19 + (i % 6)
    title = f"Periodicity — 9701/{variant}/{session}/{year}/Q5(a)"
    subtopic = f"9.{1 + (i%3)}"
    
    if is_mcq:
        t9_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble=f"Fig {i}.2 shows the melting points of Period 3 elements.",
            parts=[QuestionPart(label="a", text="Which element has a giant covalent structure?", marks=1, options=["A Na", "B Mg", "C Si", "D P"])],
            mark_scheme=[{"part": "a", "points": "C (1)", "marks": 1}]
        ))
    else:
        t9_qs.append(Question(
            number=i,
            title=title,
            syllabus_ref=subtopic,
            preamble="Period 3 elements react with oxygen to form oxides.",
            parts=[
                QuestionPart(label="a", text="Write an equation for the reaction of sodium with oxygen.", marks=1),
                QuestionPart(label="b", text="Describe the acid-base character of Al2O3 and provide an equation to support your answer.", marks=3)
            ],
            mark_scheme=[
                {"part": "a", "points": "4Na + O2 -> 2Na2O (1)", "marks": 1},
                {"part": "b", "points": "Amphoteric (1); reacts with acid: Al2O3 + 6HCl -> 2AlCl3 + 3H2O (1); reacts with base: Al2O3 + 2NaOH + 3H2O -> 2NaAl(OH)4 (1)", "marks": 3}
            ]
        ))

topics.append(TopicSection(day_label="TOPIC 9", topic_code="TOPIC 9", topic_name="THE PERIODIC TABLE: CHEMICAL PERIODICITY", questions=t9_qs))
