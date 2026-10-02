# t12_6_solution_hydration.py
PACK_META = {
    "candidate": "Usman",
    "topic_code": "12",
    "topic_name": "Entropy and Energetics",
    "subtopic_code": "12B.3",
    "subtopic_name": "Enthalpy Changes of Solution and Hydration",
    "institution": "Mentora Academy",
    "contact": "mentoraonlineacademy@gmail.com   •   +923164586836"
}

QUESTIONS = [
    {
        "type": "Structured",
        "question": "Define the standard enthalpy of hydration of an ion. [WCH14/01/Oct21/Q5(a)]",
        "mark_scheme": "The enthalpy change when one mole of gaseous ions (1) dissolves in sufficient water to form an infinitely dilute solution (1) under standard conditions.",
        "marks": 2
    },
    {
        "type": "Structured",
        "question": "Calculate the enthalpy change of solution for magnesium chloride. Given: Delta_LE H (MgCl2) = -2526, Delta_hyd H (Mg2+) = -1921, Delta_hyd H (Cl-) = -364 (all in kJ mol-1). [WCH14/01/Jan21/Q2(b)]",
        "mark_scheme": "Delta_sol H = Delta_hyd H(cation) + 2 x Delta_hyd H(anion) - Delta_LE H (1)\n= -1921 + 2(-364) - (-2526) (1)\n= -2649 + 2526 = -123 kJ mol-1 (1)",
        "marks": 3
    }
]

FAQS = [
    {
        "question": "Why do students make mistakes calculating Delta_sol H?",
        "answer": "They forget to multiply the hydration enthalpy of the anion (e.g. Cl-) by 2 when there are two anions in the empirical formula (e.g. MgCl2). Always check the stoichiometry."
    },
    {
        "question": "How does solubility relate to these enthalpy changes?",
        "answer": "If Delta_sol H is highly endothermic, the substance is likely insoluble. For a substance to be soluble, Delta_sol H should be exothermic or only slightly endothermic (so that Delta S_total remains positive)."
    }
]
