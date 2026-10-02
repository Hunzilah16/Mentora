# t14_3_kw.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14A.3',
    'subtopic_name': 'Ionic Product of Water, Kw'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'Write the expression for the ionic product of water, Kw.',
        'marks': 1,
        'mark_scheme': 'Kw = [H+][OH-]',
        'ref': 'WCH14/01/Jan22/Q12(a)'
    }
]

FAQS = [
    {
        'question': 'How does temperature affect Kw?',
        'answer': 'The dissociation of water is endothermic, so increasing temperature shifts equilibrium to the right, increasing Kw and decreasing the pH of pure water.'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_14A3_Kw.pdf ...")
    # PDF generation logic here

if __name__ == '__main__':
    generate_pdf()
