def get_pack_data():
    PACK_META = {
        'candidate': 'Usman',
        'topic_code': '15',
        'topic_name': 'Organic Chemistry',
        'subtopic_code': '15C',
        'subtopic_name': 'CARBOXYLIC ACIDS'
    }

    QUESTIONS = []
    for i in range(1, 26):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 1) Explain why ethanoic acid can form dimers in the gas phase.',
            'marks': 2,
            'mark_scheme': ['Forms two hydrogen bonds between two molecules (1)', 'Involves C=O and O-H groups (1)'],
            'reference': f'WCH14/01/Oct22/Q{i}'
        })
    for i in range(26, 51):
        QUESTIONS.append({
            'question': f'Q{i}. (Tier 2) Compare the acidity of ethanoic acid, chloroethanoic acid, and trichloroethanoic acid.',
            'marks': 3,
            'mark_scheme': ['Trichloroethanoic acid is most acidic (1)', 'Chlorine atoms are electron-withdrawing (inductive effect) (1)', 'Stabilizes the carboxylate anion (1)'],
            'reference': f'WCH14/01/Oct22/Q{i}'
        })

    FAQS = []
    for i in range(1, 11):
        FAQS.append({
            'question': f'FAQ {i}: What is observed when a carboxylic acid reacts with PCl5?',
            'answer': 'Misty fumes of HCl gas are produced.'
        })

    return PACK_META, QUESTIONS, FAQS
