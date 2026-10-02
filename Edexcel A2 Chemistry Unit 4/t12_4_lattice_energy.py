# t12_4_lattice_energy.py
PACK_META = {
    "candidate": "Usman",
    "topic_code": "12",
    "topic_name": "Entropy and Energetics",
    "subtopic_code": "12B.1",
    "subtopic_name": "Lattice Energy and Born-Haber Cycles",
    "institution": "Mentora Academy",
    "contact": "mentoraonlineacademy@gmail.com   •   +923164586836"
}

QUESTIONS = [
    {
        "type": "Structured",
        "question": "Define the term lattice energy. [WCH14/01/Oct22/Q2(a)]",
        "mark_scheme": "The enthalpy change when one mole of a solid ionic compound is formed (1) from its gaseous ions (1) under standard conditions.",
        "marks": 2
    },
    {
        "type": "Structured",
        "question": "Construct a Born-Haber cycle for sodium chloride and use it to calculate the lattice energy of NaCl. Given: Delta_f H = -411, Delta_atm H (Na) = +107, 1st IE (Na) = +496, Delta_atm H (Cl) = +122, 1st EA (Cl) = -349 (all in kJ mol-1). [WCH14/01/Jan22/Q3(b)]",
        "mark_scheme": "Delta_f H = Delta_atm H(Na) + IE(Na) + Delta_atm H(Cl) + EA(Cl) + Delta_LE H (1)\n-411 = 107 + 496 + 122 + (-349) + Delta_LE H (1)\nDelta_LE H = -411 - 107 - 496 - 122 + 349 = -787 kJ mol-1 (1)",
        "marks": 3
    }
]

FAQS = [
    {
        "question": "Why do students lose marks in defining lattice energy?",
        "answer": "They often forget to specify that the ions must be in the gaseous state, or they define it for the formation of one mole of gaseous ions rather than one mole of the solid lattice."
    },
    {
        "question": "What is the common error when calculating lattice energy from a Born-Haber cycle?",
        "answer": "Sign errors are rampant. Ensure that all endothermic processes (atomisation, ionisation energy) are positive and exothermic processes (electron affinity for 1st EA) are negative before solving the equation."
    }
]
