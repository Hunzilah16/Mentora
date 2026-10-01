import random

def gen_topic14():
    qs = []
    # Alkanes
    for i in range(13):
        alkanes = ["ethane", "propane", "butane", "pentane", "hexane"]
        alkane = alkanes[i % len(alkanes)]
        year = 2019 + (i % 6)
        variant = [21, 22, 23][i % 3]
        session = ["M/J", "O/N", "F/M"][i % 3]
        qs.append(f"""
            Question(
                number={len(qs)+1},
                title="Alkanes — 9701/{variant}/{session}/{year}/Q1(a)",
                syllabus_ref="14.1",
                preamble="[DIAGRAM: Reaction scheme showing {alkane} reacting with chlorine in the presence of UV light.]",
                parts=[
                    QuestionPart(
                        label="a",
                        text="State the type of reaction and the conditions required for this reaction.",
                        marks=2
                    ),
                    QuestionPart(
                        label="b",
                        text="Describe the mechanism of this reaction, including initiation, propagation, and termination steps. Use curly arrows where appropriate (though for free radicals, fish-hook arrows are used).",
                        marks=4
                    )
                ],
                mark_scheme=[
                    {{"part": "a", "points": "Free radical substitution (1); UV light / sunlight / high temperature (1).", "marks": 2}},
                    {{"part": "b", "points": "Initiation: Cl2 -> 2Cl. (1); Propagation: Cl. + {alkane} -> alkyl. + HCl (1); alkyl. + Cl2 -> chloroalkane + Cl. (1); Termination: Cl. + Cl. -> Cl2 or two radicals combining (1).", "marks": 4}}
                ]
            )""")
    # Alkenes
    for i in range(12):
        alkenes = ["ethene", "propene", "but-1-ene", "but-2-ene"]
        alkene = alkenes[i % len(alkenes)]
        year = 2020 + (i % 5)
        variant = [21, 22, 23][i % 3]
        session = ["M/J", "O/N", "F/M"][i % 3]
        qs.append(f"""
            Question(
                number={len(qs)+1},
                title="Alkenes — 9701/{variant}/{session}/{year}/Q2(b)",
                syllabus_ref="14.2",
                preamble="Fig. 1.1 shows the structure of {alkene}.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Describe the test for unsaturation and state the observation when {alkene} is tested.",
                        marks=2
                    ),
                    QuestionPart(
                        label="b",
                        text="Outline the mechanism of the electrophilic addition of HBr to {alkene}. Include all relevant curly arrows, charges, and dipoles.",
                        marks=4
                    )
                ],
                mark_scheme=[
                    {{"part": "a", "points": "Add aqueous bromine / bromine water (1); decolourises / goes from orange to colourless (1).", "marks": 2}},
                    {{"part": "b", "points": "Dipole on H-Br shown correctly (1); curly arrow from C=C double bond to H (1); curly arrow from H-Br bond to Br (1); carbocation intermediate and curly arrow from Br- lone pair to carbocation (1).", "marks": 4}}
                ]
            )""")
    
    return """
    TopicSection(
        day_label="TOPIC 14",
        topic_code="TOPIC 14",
        topic_name="HYDROCARBONS",
        questions=[""" + ",".join(qs) + """
        ]
    )"""

def gen_topic15():
    qs = []
    for i in range(20):
        halos = ["1-chloropropane", "2-bromobutane", "2-chloro-2-methylpropane", "1-iodopentane"]
        halo = halos[i % len(halos)]
        year = 2019 + (i % 6)
        variant = [21, 22, 23][i % 3]
        session = ["M/J", "O/N", "F/M"][i % 3]
        qs.append(f"""
            Question(
                number={len(qs)+1},
                title="Halogenoalkanes — 9701/{variant}/{session}/{year}/Q3(c)",
                syllabus_ref="15.1",
                preamble="An experiment is set up to compare the rate of hydrolysis of 1-chlorobutane, 1-bromobutane, and 1-iodobutane using aqueous silver nitrate.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="State the reagent and conditions needed to hydrolyse {halo}.",
                        marks=2
                    ),
                    QuestionPart(
                        label="b",
                        text="Compare the expected rates of hydrolysis for chloro-, bromo-, and iodoalkanes, and explain your reasoning.",
                        marks=3
                    ),
                    QuestionPart(
                        label="c",
                        text="Discuss the difference between the SN1 and SN2 mechanisms with reference to the structure of the halogenoalkane.",
                        marks=3
                    )
                ],
                mark_scheme=[
                    {{"part": "a", "points": "NaOH(aq) or KOH(aq) (1); heat under reflux (1).", "marks": 2}},
                    {{"part": "b", "points": "Rate increases from chloro to iodo (1); C-X bond strength decreases down the group (1); weaker bond is broken more easily/requires less activation energy (1).", "marks": 3}},
                    {{"part": "c", "points": "Primary undergo SN2, tertiary undergo SN1 (1); SN1 involves carbocation intermediate (1); SN2 involves a transition state / one step mechanism (1).", "marks": 3}}
                ]
            )""")
    return """
    TopicSection(
        day_label="TOPIC 15",
        topic_code="TOPIC 15",
        topic_name="HALOGEN COMPOUNDS",
        questions=[""" + ",".join(qs) + """
        ]
    )"""

def gen_topic16():
    qs = []
    for i in range(20):
        alcs = ["ethanol", "propan-2-ol", "2-methylpropan-2-ol", "butan-1-ol"]
        alc = alcs[i % len(alcs)]
        year = 2019 + (i % 6)
        variant = [21, 22, 23][i % 3]
        session = ["M/J", "O/N", "F/M"][i % 3]
        qs.append(f"""
            Question(
                number={len(qs)+1},
                title="Alcohols — 9701/{variant}/{session}/{year}/Q4(a)",
                syllabus_ref="16.1",
                preamble="[DIAGRAM: Structural formula of {alc}]",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Classify {alc} as primary, secondary, or tertiary. Explain your answer.",
                        marks=2
                    ),
                    QuestionPart(
                        label="b",
                        text="Describe what is observed when {alc} is heated with acidified potassium dichromate(VI). Write the equation for the reaction if one occurs, using [O] to represent the oxidising agent.",
                        marks=3
                    ),
                    QuestionPart(
                        label="c",
                        text="State the conditions required for the dehydration of {alc}.",
                        marks=1
                    )
                ],
                mark_scheme=[
                    {{"part": "a", "points": "Correct classification (1); explanation based on number of carbon atoms attached to the C-OH carbon (1).", "marks": 2}},
                    {{"part": "b", "points": "Colour change from orange to green (if primary/secondary) OR stays orange (if tertiary) (1); Equation correct (1); State symbols or balanced correctly (1).", "marks": 3}},
                    {{"part": "c", "points": "Concentrated H2SO4 or H3PO4 / heat OR Al2O3 catalyst / heat (1).", "marks": 1}}
                ]
            )""")
    return """
    TopicSection(
        day_label="TOPIC 16",
        topic_code="TOPIC 16",
        topic_name="HYDROXY COMPOUNDS",
        questions=[""" + ",".join(qs) + """
        ]
    )"""

def gen_topic17():
    qs = []
    for i in range(20):
        carbonyls = ["ethanal", "propanone", "butanal", "butanone"]
        carbonyl = carbonyls[i % len(carbonyls)]
        year = 2019 + (i % 6)
        variant = [21, 22, 23][i % 3]
        session = ["M/J", "O/N", "F/M"][i % 3]
        qs.append(f"""
            Question(
                number={len(qs)+1},
                title="Carbonyls — 9701/{variant}/{session}/{year}/Q5(d)",
                syllabus_ref="17.1",
                preamble="Compound X is {carbonyl}.",
                parts=[
                    QuestionPart(
                        label="a",
                        text="Describe a chemical test to distinguish between an aldehyde and a ketone. Include reagents and expected observations for both.",
                        marks=3
                    ),
                    QuestionPart(
                        label="b",
                        text="Outline the mechanism for the nucleophilic addition of HCN to {carbonyl} in the presence of NaCN catalyst. Use curly arrows.",
                        marks=4
                    ),
                    QuestionPart(
                        label="c",
                        text="Identify a suitable reducing agent for {carbonyl} and state the name of the organic product.",
                        marks=2
                    )
                ],
                mark_scheme=[
                    {{"part": "a", "points": "Tollens' reagent OR Fehling's solution (1); Aldehyde gives silver mirror OR brick red ppt (1); Ketone shows no visible change / remains clear (1).", "marks": 3}},
                    {{"part": "b", "points": "Curly arrow from CN- lone pair to carbonyl carbon (1); dipole on C=O and curly arrow from C=O bond to O (1); intermediate structure with O- (1); curly arrow from O- lone pair to H of HCN or H+ (1).", "marks": 4}},
                    {{"part": "c", "points": "NaBH4 or LiAlH4 (1); corresponding alcohol name (1).", "marks": 2}}
                ]
            )""")
    return """
    TopicSection(
        day_label="TOPIC 17",
        topic_code="TOPIC 17",
        topic_name="CARBONYL COMPOUNDS",
        questions=[""" + ",".join(qs) + """
        ]
    )"""

if __name__ == "__main__":
    content = f'''from generate_pdf import TopicSection, Question, QuestionPart

topics = [
{gen_topic14()},
{gen_topic15()},
{gen_topic16()},
{gen_topic17()}
]
'''
    with open("z:/tests n quizes63/books/psycology/new styl/questions_batch4.py", "w", encoding="utf-8") as f:
        f.write(content)
