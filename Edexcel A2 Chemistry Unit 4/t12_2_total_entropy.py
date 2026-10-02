# t12_2_total_entropy.py
PACK_META = {
    "candidate": "Usman",
    "topic_code": "12",
    "topic_name": "Entropy and Energetics",
    "subtopic_code": "12A.2",
    "subtopic_name": "Total Entropy",
    "institution": "Mentora Academy",
    "contact": "mentoraonlineacademy@gmail.com   •   +923164586836"
}

QUESTIONS = [
    {
        "type": "Structured",
        "question": "For a reaction, Delta H = -92.2 kJ mol-1. Calculate the entropy change of the surroundings at 298 K. [WCH14/01/Jan23/Q5(b)]",
        "mark_scheme": "Delta S_surroundings = -Delta H / T\n= -(-92200 J mol-1) / 298 K (1)\n= +309.4 J K-1 mol-1 (1)",
        "marks": 2
    },
    {
        "type": "Structured",
        "question": "The entropy change of the system is -198.8 J K-1 mol-1. Use the answer from the previous part to calculate the total entropy change at 298 K. [WCH14/01/Jan23/Q5(c)]",
        "mark_scheme": "Delta S_total = Delta S_system + Delta S_surroundings\n= -198.8 + 309.4 (1)\n= +110.6 J K-1 mol-1 (1)",
        "marks": 2
    }
]

FAQS = [
    {
        "question": "Why do students lose marks in calculating Delta S_surroundings?",
        "answer": "Candidates forget to convert Delta H from kJ mol-1 to J mol-1 before dividing by temperature in Kelvin. This results in a value that is 1000 times too small."
    },
    {
        "question": "What is the common sign error for Delta S_surroundings?",
        "answer": "Students often forget the negative sign in the equation Delta S_surr = -Delta H / T. An exothermic reaction (-Delta H) always leads to a positive Delta S_surroundings."
    }
]
