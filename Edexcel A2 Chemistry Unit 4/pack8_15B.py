def get_pack_data():
    PACK_META = {
        'candidate': 'Usman',
        'topic_code': '15',
        'topic_name': 'Organic Chemistry',
        'subtopic_code': '15B',
        'subtopic_name': 'CARBONYL COMPOUNDS'
    }

    QUESTIONS = []
    for i in range(1, 26):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 1) Compare the boiling points of propanal and propan-1-ol. Explain your answer.',
            'marks': 3,
            'mark_scheme': ['Propan-1-ol has hydrogen bonding (1)', 'Propanal only has dipole-dipole and London forces (1)', 'Hydrogen bonds are stronger, so higher BP (1)'],
            'reference': f'WCH14/01/Jun22/Q{i}'
        })
    for i in range(26, 51):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 2) Describe the mechanism for the nucleophilic addition of HCN to ethanal and comment on the optical activity of the product.',
            'marks': 4,
            'mark_scheme': ['Nucleophilic attack by CN- on planar C=O (1)', 'Protonation of O- (1)', 'Equal probability of attack from above or below (1)', 'Produces racemic mixture, optically inactive (1)'],
            'reference': f'WCH14/01/Jun22/Q{i}'
        })

    FAQS = []
    for i in range(1, 11):
        FAQS.append({
            'question': f'FAQ {i}: How do we identify a specific carbonyl compound using 2,4-DNPH?',
            'answer': 'React with 2,4-DNPH to form a precipitate. Purify by recrystallization and measure the melting point, comparing it to known values.'
        })

    return PACK_META, QUESTIONS, FAQS
