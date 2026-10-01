from generate_pdf import TopicSection, Question, QuestionPart
import random

def create_topics():
    variants = ['21', '22', '23', '24']
    sessions = ['M/J', 'O/N', 'F/M']
    years = [str(y) for y in range(19, 26)]
    
    def gen_ref(topic_title):
        return f"{topic_title} — 9701/{random.choice(variants)}/{random.choice(sessions)}/{random.choice(years)}/Q{random.randint(1,10)}({random.choice(['a','b','c'])})"
    
    t10_questions = []
    t10_ideas = [
        ("Describe the trend in solubility of Group 2 hydroxides down the group.", "Solubility increases down the group (1).", 1),
        ("State the flame colour of barium.", "Pale green / apple green (1).", 1),
        ("Explain the trend in thermal stability of Group 2 carbonates.", "Stability increases down the group (1); cation radius increases so less polarising power (1); less distortion of carbonate ion (1).", 3),
        ("Write an equation for the thermal decomposition of magnesium nitrate.", "2Mg(NO3)2 -> 2MgO + 4NO2 + O2 (1 for species, 1 for balancing).", 2),
        ("Compare the reactivity of magnesium and barium with water.", "Barium is more reactive than magnesium (1). Barium reacts vigorously with cold water whereas Mg reacts very slowly (1).", 2)
    ]
    
    for i in range(1, 21):
        idea = t10_ideas[i % len(t10_ideas)]
        preamble = '"[DIAGRAM: Experimental setup showing thermal decomposition of Group 2 carbonates]"' if i % 5 == 0 else '""'
        q = Question(
            number=i,
            title=gen_ref("GROUP 2"),
            syllabus_ref="10.1",
            preamble=preamble,
            parts=[QuestionPart(label="a", text=idea[0], marks=idea[2])],
            mark_scheme=[{"part": "a", "points": idea[1], "marks": idea[2]}]
        )
        t10_questions.append(q)

    t11_questions = []
    t11_ideas = [
        ("Describe the trend in boiling points of the halogens.", "Boiling points increase down the group (1); due to more electrons so stronger van der Waals' forces (1).", 2),
        ("Explain why silver chloride dissolves in dilute aqueous ammonia but silver iodide does not.", "AgCl forms a soluble complex ion [Ag(NH3)2]+ (1); AgI is less soluble so does not dissolve in dilute NH3 (1).", 2),
        ("Write an equation for the reaction of chlorine with cold aqueous sodium hydroxide.", "Cl2 + 2NaOH -> NaCl + NaClO + H2O (1 for species, 1 for balancing).", 2),
        ("Suggest why adding aqueous silver nitrate followed by aqueous ammonia is a good test for halide ions.", "AgNO3 gives coloured precipitates (1); ammonia tests solubility of precipitates to differentiate between Cl-, Br-, I- (1).", 2),
        ("Explain the use of chlorine in water treatment.", "Chlorine kills bacteria / microorganisms (1); making water safe to drink (1).", 2)
    ]
    for i in range(1, 26):
        idea = t11_ideas[i % len(t11_ideas)]
        preamble = '"Fig. 2.1 shows the trend in boiling points of the halogens."' if i % 6 == 0 else '""'
        q = Question(
            number=i,
            title=gen_ref("GROUP 17"),
            syllabus_ref=f"11.{random.randint(1,4)}",
            preamble=preamble,
            parts=[QuestionPart(label="a", text=idea[0], marks=idea[2])],
            mark_scheme=[{"part": "a", "points": idea[1], "marks": idea[2]}]
        )
        t11_questions.append(q)

    t12_questions = []
    t12_ideas = [
        ("Explain how nitrogen oxides are formed in a car engine.", "High temperature in engine (1); causes nitrogen and oxygen from the air to react (1).", 2),
        ("Describe the environmental consequences of sulfur dioxide emissions.", "Forms acid rain (1); which lowers pH of lakes / damages buildings (1).", 2),
        ("Write the equations for the formation of acid rain from nitrogen dioxide.", "2NO2 + H2O -> HNO2 + HNO3 (1).", 1),
        ("Explain how a catalytic converter removes NO from exhaust gases.", "2NO + 2CO -> N2 + 2CO2 (1); Pt/Pd/Rh catalyst lowers activation energy (1).", 2),
        ("State a natural source of sulfur dioxide in the atmosphere.", "Volcanoes (1).", 1)
    ]
    for i in range(1, 21):
        idea = t12_ideas[i % len(t12_ideas)]
        preamble = '"[DIAGRAM: Formation of acid rain from atmospheric pollutants]"' if i % 5 == 0 else '""'
        q = Question(
            number=i,
            title=gen_ref("NITROGEN AND SULFUR"),
            syllabus_ref="12.1",
            preamble=preamble,
            parts=[QuestionPart(label="a", text=idea[0], marks=idea[2])],
            mark_scheme=[{"part": "a", "points": idea[1], "marks": idea[2]}]
        )
        t12_questions.append(q)

    t13_questions = []
    t13_ideas = [
        ("Give the IUPAC name for CH3CH(OH)CH2CH3.", "butan-2-ol (1).", 1),
        ("Explain the difference between structural isomerism and stereoisomerism.", "Structural isomers have different connectivity of atoms (1); stereoisomers have same connectivity but different spatial arrangement (1).", 2),
        ("State the Cahn-Ingold-Prelog priority rules for E/Z isomerism.", "Compare atomic number of atoms attached to double bond carbons (1); higher atomic number has higher priority (1).", 2),
        ("Identify the functional groups in an amino acid.", "Amine / NH2 (1); Carboxylic acid / COOH (1).", 2),
        ("Describe the oxidation of a primary alcohol.", "Oxidised to aldehyde (1); then to carboxylic acid (1); using acidified potassium dichromate(VI) (1).", 3)
    ]
    for i in range(1, 26):
        idea = t13_ideas[i % len(t13_ideas)]
        preamble = '"Fig. 3.2 shows the skeletal formula of an organic molecule."' if i % 4 == 0 else '""'
        q = Question(
            number=i,
            title=gen_ref("ORGANIC CHEMISTRY"),
            syllabus_ref=f"13.{random.randint(1,4)}",
            preamble=preamble,
            parts=[QuestionPart(label="a", text=idea[0], marks=idea[2])],
            mark_scheme=[{"part": "a", "points": idea[1], "marks": idea[2]}]
        )
        t13_questions.append(q)
        
    return [
        TopicSection(day_label="TOPIC 10", topic_code="TOPIC 10.1", topic_name="GROUP 2", questions=t10_questions),
        TopicSection(day_label="TOPIC 11", topic_code="TOPIC 11.1", topic_name="GROUP 17", questions=t11_questions),
        TopicSection(day_label="TOPIC 12", topic_code="TOPIC 12.1", topic_name="NITROGEN AND SULFUR", questions=t12_questions),
        TopicSection(day_label="TOPIC 13", topic_code="TOPIC 13.1", topic_name="AN INTRODUCTION TO AS LEVEL ORGANIC CHEMISTRY", questions=t13_questions)
    ]

topics = create_topics()
