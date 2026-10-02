# t12_1_intro_entropy.py
PACK_META = {
    "candidate": "Usman",
    "topic_code": "12",
    "topic_name": "Entropy and Energetics",
    "subtopic_code": "12A.1",
    "subtopic_name": "Introduction to Entropy",
    "institution": "Mentora Academy",
    "contact": "mentoraonlineacademy@gmail.com   •   +923164586836"
}

QUESTIONS = [
    {
        "type": "MCQ",
        "question": "Which of the following processes involves an increase in the entropy of the system? [WCH14/01/Jan23/Q1]",
        "options": ["A  Freezing of water", "B  Condensation of steam", "C  Sublimation of dry ice", "D  Precipitation of silver chloride"],
        "answer": "C",
        "marks": 1
    },
    {
        "type": "Structured",
        "question": "Explain why the standard entropy of gaseous carbon dioxide is greater than that of solid carbon dioxide. [WCH14/01/Oct22/Q3(a)]",
        "mark_scheme": "- Gases have more ways of arranging their particles / more disorder / more random motion than solids (1)\n- Gases have more microstates / energy is distributed over more energy levels (1)",
        "marks": 2
    },
    {
        "type": "Structured",
        "question": "Calculate the entropy change of the system for the reaction: N2(g) + 3H2(g) -> 2NH3(g). Given standard molar entropies: N2(g) = 191.6, H2(g) = 130.6, NH3(g) = 192.3 J K-1 mol-1. [WCH14/01/Jan22/Q4(a)]",
        "mark_scheme": "Delta S_system = (2 x 192.3) - (191.6 + 3 x 130.6) (1)\n= 384.6 - 583.4 = -198.8 J K-1 mol-1 (1)",
        "marks": 2
    }
]

FAQS = [
    {
        "question": "Why do students often get the sign of Delta S_system wrong for gas reactions?",
        "answer": "Students often forget to check the number of moles of gas on each side. If gas moles decrease, Delta S_system is negative. Always count the moles of gaseous reactants and products carefully."
    },
    {
        "question": "What is the common mistake in calculating standard entropy changes?",
        "answer": "Candidates forget to multiply the standard entropy of each substance by its stoichiometric coefficient in the balanced equation."
    }
]
