# t14_5_titrations.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14B.1',
    'subtopic_name': 'Acid-Base Titrations, pH Curves and Indicators'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'Which indicator is suitable for a weak acid - strong base titration?',
        'marks': 1,
        'mark_scheme': 'Phenolphthalein, because the pH at equivalence point is > 7.',
        'ref': 'WCH14/01/Jun22/Q5'
    }
]

FAQS = [
    {
        'question': 'How do I choose the correct indicator?',
        'answer': 'The pKa of the indicator should fall within the vertical region of the titration curve.'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_14B1_Titrations_pH_Curves_Indicators.pdf ...")

if __name__ == '__main__':
    generate_pdf()
