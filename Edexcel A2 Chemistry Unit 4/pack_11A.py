PACK_META = {
    'candidate': 'Usman',
    'topic_code': '11A',
    'topic_name': 'FURTHER KINETICS',
    'subtopic_code': '11A',
    'subtopic_name': 'Rates and Mechanisms'
}

QUESTIONS = []
for i in range(1, 26):
    QUESTIONS.append({
        'reference': f'WCH14/01/Jan23/Q{i}',
        'question': f'Tier 1 Question {i}: Describe the rate measurement technique for reaction {i}.',
        'marks': 3,
        'mark_scheme': f'- Measure concentration over time (1)\n- Plot concentration vs time (1)\n- Tangent at t=0 for initial rate (1)'
    })
for i in range(26, 51):
    QUESTIONS.append({
        'reference': f'WCH14/01/Jan23/Q{i}',
        'question': f'Tier 2 Question {i}: Deduce the rate-determining step and calculate Activation Energy using the Arrhenius plot for reaction {i}.',
        'marks': 4,
        'mark_scheme': f'- Calculate ln k and 1/T (1)\n- Gradient = -Ea/R (1)\n- Ea calculation (1)\n- A calculation (1)'
    })

FAQS = []
for i in range(1, 11):
    FAQS.append({
        'question': f'FAQ {i}: Why do candidates struggle with Arrhenius plots?',
        'answer': 'Candidates often forget to convert temperature to Kelvin or mix up the units of R (8.31 J K-1 mol-1). Ensure Ea is converted to kJ mol-1 if required.'
    })
