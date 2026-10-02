# t14_1_bronsted.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14A.1',
    'subtopic_name': 'The Brønsted-Lowry Theory'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'State the Brønsted-Lowry definition of an acid.',
        'marks': 1,
        'mark_scheme': 'A proton (H+) donor.',
        'ref': 'WCH14/01/Jan23/Q3(a)'
    },
    {
        'q_num': 2,
        'question': 'Identify the conjugate acid-base pairs in the following reaction:\nNH3(aq) + H2O(l) ⇌ NH4+(aq) + OH-(aq)',
        'marks': 2,
        'mark_scheme': 'NH3 is the base and NH4+ is its conjugate acid. (1)\nH2O is the acid and OH- is its conjugate base. (1)',
        'ref': 'WCH14/01/Oct22/Q11(a)'
    }
]

FAQS = [
    {
        'question': 'What is the most common mistake when identifying conjugate pairs?',
        'answer': 'Students often pair up the wrong species. A conjugate pair always differs by exactly one H+ ion.'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_{PACK_META['subtopic_code']}_Bronsted_Lowry.pdf ...")
    # PDF generation logic here

if __name__ == '__main__':
    generate_pdf()
