PACK_META = {
    'candidate': 'Usman',
    'topic_code': '13',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '13A.2',
    'subtopic_name': 'Equilibrium Constant, Kp',
    'institution': 'Mentora Academy',
    'branding': 'Mentora Visual Style (Navy #0b1b36, Crimson #a81717, Steel Blue #1e3a8a, Poppins fonts)',
    'contact_line': 'mentoraonlineacademy@gmail.com   •   +923164586836'
}

QUESTIONS = [
    {
        'type': 'structured',
        'question': '1. (a) Write the expression for the equilibrium constant, Kp, for the reaction:\n\nCO(g) + 2H2(g) ⇌ CH3OH(g)',
        'marks': 1,
        'reference': 'WCH14/01/Jun23/Q4(a)',
        'mark_scheme': 'Kp = (pCH3OH) / (pCO * (pH2)^2)\nAllow use of P or p for partial pressure. Do not allow square brackets [].'
    },
    {
        'type': 'structured',
        'question': '(b) In an experiment, a mixture of CO and H2 was allowed to reach equilibrium at a total pressure of 50 atm. At equilibrium, the mole fractions were: CO = 0.15, H2 = 0.35, CH3OH = 0.50. Calculate the value of Kp and state its units.',
        'marks': 3,
        'reference': 'WCH14/01/Jun23/Q4(b)',
        'mark_scheme': '1. Partial pressures: pCH3OH = 0.50 * 50 = 25 atm, pCO = 0.15 * 50 = 7.5 atm, pH2 = 0.35 * 50 = 17.5 atm\n2. Kp = 25 / (7.5 * 17.5^2)\n3. = 0.0109 atm-2 (allow pa-2 if Pa used, but units must match)'
    },
    {
        'type': 'mcq',
        'question': '2. What is the unit of Kp for the reaction H2(g) + I2(g) ⇌ 2HI(g)?',
        'options': ['A. atm', 'B. atm-1', 'C. atm2', 'D. No units'],
        'answer': 'D',
        'marks': 1,
        'reference': 'WCH14/01/Jan22/Q3'
    },
    {
        'type': 'structured',
        'question': '3. Define the term partial pressure.',
        'marks': 1,
        'reference': 'WCH14/01/Oct21/Q2',
        'mark_scheme': 'The pressure a gas would exert if it alone occupied the whole container / total pressure × mole fraction.'
    }
]

FAQS = [
    {
        'question': 'Can I use square brackets [] for Kp expressions?',
        'answer': 'No, using square brackets in a Kp expression will result in 0 marks. Square brackets mean concentration. You must use p() or P() to denote partial pressure.'
    },
    {
        'question': 'How do I calculate mole fraction?',
        'answer': 'Mole fraction = (number of moles of the specific gas) / (total number of moles of all gases in the mixture). Make sure the sum of all mole fractions is exactly 1.'
    },
    {
        'question': 'What units should I use for total pressure?',
        'answer': 'You can use atm or Pa (or kPa), but you must be consistent. The unit of Kp will depend on the unit you used for pressure. Always check what unit the question provides.'
    }
]
