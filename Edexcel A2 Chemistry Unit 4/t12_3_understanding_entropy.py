# t12_3_understanding_entropy.py
PACK_META = {
    "candidate": "Usman",
    "topic_code": "12",
    "topic_name": "Entropy and Energetics",
    "subtopic_code": "12A.3",
    "subtopic_name": "Understanding Entropy Changes",
    "institution": "Mentora Academy",
    "contact": "mentoraonlineacademy@gmail.com   •   +923164586836"
}

QUESTIONS = [
    {
        "type": "Structured",
        "question": "Explain, in terms of entropy, why a reaction is feasible at all temperatures if Delta H is negative and Delta S_system is positive. [WCH14/01/Oct21/Q4(b)]",
        "mark_scheme": "- Delta S_surroundings = -Delta H / T, so if Delta H is negative, Delta S_surroundings is positive at all T (1)\n- Delta S_total = Delta S_system + Delta S_surroundings, so Delta S_total must be positive (1)\n- Since Delta S_total > 0, the reaction is feasible (1)",
        "marks": 3
    },
    {
        "type": "Structured",
        "question": "Calculate the minimum temperature at which a reaction becomes feasible given Delta H = +135 kJ mol-1 and Delta S_system = +334 J K-1 mol-1. [WCH14/01/Jan21/Q6(c)]",
        "mark_scheme": "For feasibility, Delta S_total = 0 (minimum condition)\nSo T = Delta H / Delta S_system (1)\n= (+135000 J mol-1) / (+334 J K-1 mol-1)\n= 404 K (1)",
        "marks": 2
    }
]

FAQS = [
    {
        "question": "Why do students struggle with finding the minimum temperature for feasibility?",
        "answer": "Candidates often set Delta S_total to 0 but fail to convert Delta H to J mol-1. This gives a completely wrong temperature. Always ensure Delta H and Delta S_system have the same energy units before dividing."
    },
    {
        "question": "What is meant by thermodynamic feasibility?",
        "answer": "Thermodynamic feasibility means Delta S_total is positive. It indicates a reaction can occur, but it does NOT mean the reaction will happen quickly (kinetic aspect is ignored)."
    }
]
