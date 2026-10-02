# t14_6_buffers.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14B.2',
    'subtopic_name': 'Buffer Solutions'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'Define a buffer solution.',
        'marks': 2,
        'mark_scheme': 'A solution that resists changes in pH (1) when small amounts of acid or base are added (1).',
        'ref': 'WCH14/01/Jan21/Q18(a)'
    }
]

FAQS = [
    {
        'question': 'How does an acidic buffer work when H+ is added?',
        'answer': 'The conjugate base reacts with the added H+ to form the weak acid, minimising the change in pH.'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_14B2_Buffer_Solutions.pdf ...")

if __name__ == '__main__':
    generate_pdf()
