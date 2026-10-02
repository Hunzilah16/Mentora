PACK_META = {
    'candidate': 'Usman',
    'topic_code': '12A',
    'topic_name': 'ENTROPY',
    'subtopic_code': '12A',
    'subtopic_name': 'System and Total Entropy'
}

QUESTIONS = []
for i in range(1, 26):
    QUESTIONS.append({
        'reference': f'WCH14/01/Oct22/Q{i}',
        'question': f'Tier 1 Question {i}: Calculate the entropy change of the system (Delta S_system) for the given state change.',
        'marks': 2,
        'mark_scheme': f'- Sum of S(products) - Sum of S(reactants) (1)\n- Correct unit J K-1 mol-1 (1)'
    })
for i in range(26, 51):
    QUESTIONS.append({
        'reference': f'WCH14/01/Oct22/Q{i}',
        'question': f'Tier 2 Question {i}: Determine the minimum temperature for the reaction to become spontaneous, given Delta H and Delta S_system.',
        'marks': 3,
        'mark_scheme': f'- Delta S_total > 0 for spontaneity (1)\n- T = Delta H / Delta S_system (1)\n- Correct T in Kelvin (1)'
    })

FAQS = []
for i in range(1, 11):
    FAQS.append({
        'question': f'FAQ {i}: What is the most common error in Delta S_total calculations?',
        'answer': 'Failing to convert Delta H from kJ mol-1 to J mol-1 when dividing by T to find Delta S_surroundings.'
    })
