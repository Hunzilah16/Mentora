PACK_META = {
    'candidate': 'Usman',
    'topic_code': '13',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '13A.1',
    'subtopic_name': 'Equilibrium Constant, Kc',
    'institution': 'Mentora Academy',
    'branding': 'Mentora Visual Style (Navy #0b1b36, Crimson #a81717, Steel Blue #1e3a8a, Poppins fonts)',
    'contact_line': 'mentoraonlineacademy@gmail.com   •   +923164586836'
}

QUESTIONS = [
    {
        'type': 'structured',
        'question': '1. (a) State the expression for the equilibrium constant, Kc, for the following homogeneous reaction:\n\n2SO2(g) + O2(g) ⇌ 2SO3(g)',
        'marks': 1,
        'reference': 'WCH14/01/Jan23/Q3(a)',
        'mark_scheme': 'Kc = [SO3]^2 / ([SO2]^2[O2])\nAllow correct expression without state symbols.'
    },
    {
        'type': 'structured',
        'question': '(b) A mixture of 2.0 mol of SO2 and 1.5 mol of O2 was placed in a 2.0 dm3 flask and allowed to reach equilibrium at a constant temperature. At equilibrium, 1.2 mol of SO3 had formed. Calculate the value of Kc at this temperature and state its units.',
        'marks': 4,
        'reference': 'WCH14/01/Jan23/Q3(b)',
        'mark_scheme': '1. Moles of SO3 at eqm = 1.2 mol\n2. Moles of SO2 at eqm = 2.0 - 1.2 = 0.8 mol\n3. Moles of O2 at eqm = 1.5 - 0.6 = 0.9 mol\n4. Concentration: [SO3] = 0.6, [SO2] = 0.4, [O2] = 0.45 mol dm-3\n5. Kc = (0.6)^2 / ((0.4)^2 * 0.45) = 5.0 dm3 mol-1'
    },
    {
        'type': 'mcq',
        'question': '2. What are the units of Kc for the reaction: N2(g) + 3H2(g) ⇌ 2NH3(g)?',
        'options': ['A. mol dm-3', 'B. dm3 mol-1', 'C. mol2 dm-6', 'D. dm6 mol-2'],
        'answer': 'D',
        'marks': 1,
        'reference': 'WCH14/01/Oct22/Q5'
    },
    {
        'type': 'structured',
        'question': '3. Explain why the concentration of a solid is not included in the Kc expression for a heterogeneous equilibrium.',
        'marks': 2,
        'reference': 'WCH14/01/Jun21/Q4(c)',
        'mark_scheme': '1. The concentration (or density) of a solid is constant.\n2. It is incorporated into the value of the equilibrium constant Kc itself.'
    }
]

FAQS = [
    {
        'question': 'Do I need to include units in my final answer for Kc?',
        'answer': 'Yes, units are strictly required unless the calculation results in no units (e.g., when the moles on both sides cancel out). Always deduce the units by substituting mol dm-3 into the Kc expression.'
    },
    {
        'question': 'Why did I lose marks for my Kc expression?',
        'answer': 'A common trap is using round brackets () instead of square brackets []. In chemistry, square brackets denote concentration in mol dm-3, which is mandatory for Kc expressions. Another error is including solids in heterogeneous equilibria.'
    },
    {
        'question': 'How do I handle equilibrium calculations when volume is not given?',
        'answer': 'If the number of moles of reactants and products are equal, the volume (V) will cancel out in the Kc expression. In such cases, you can use moles directly in the expression without calculating concentration.'
    }
]
