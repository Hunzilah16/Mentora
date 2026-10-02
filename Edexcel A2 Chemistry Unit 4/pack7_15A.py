def get_pack_data():
    PACK_META = {
        'candidate': 'Usman',
        'topic_code': '15',
        'topic_name': 'Organic Chemistry',
        'subtopic_code': '15A',
        'subtopic_name': 'CHIRALITY & OPTICAL ACTIVITY'
    }

    QUESTIONS = []
    for i in range(1, 26):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 1) Identify the chiral center in 2-chlorobutane and explain its optical activity.',
            'marks': 2,
            'mark_scheme': ['Identifies C2 as chiral (1)', 'Explains rotation of plane-polarized light (1)'],
            'reference': f'WCH14/01/Jan23/Q{i}'
        })
    for i in range(26, 51):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 2) Explain the stereochemical outcome of an SN1 vs SN2 reaction on 2-bromobutane.',
            'marks': 4,
            'mark_scheme': ['SN1 planar carbocation (1)', '50:50 racemate (1)', 'SN2 backside attack (1)', 'Walden inversion (1)'],
            'reference': f'WCH14/01/Jan23/Q{i}'
        })

    FAQS = []
    for i in range(1, 11):
        FAQS.append({
            'question': f'FAQ {i}: Why is a racemic mixture optically inactive?',
            'answer': 'It contains equal amounts of two enantiomers which rotate plane-polarized light equally in opposite directions, canceling out the effect.'
        })

    return PACK_META, QUESTIONS, FAQS
