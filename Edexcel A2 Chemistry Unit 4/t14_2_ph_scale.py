# t14_2_ph_scale.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14A.2',
    'subtopic_name': 'Hydrogen Ion Concentration and the pH Scale'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'Calculate the pH of 0.150 mol dm-3 HCl.',
        'marks': 1,
        'mark_scheme': 'pH = -log(0.150) = 0.82',
        'ref': 'WCH14/01/Jun21/Q4(a)'
    }
]

FAQS = [
    {
        'question': 'Do I need to worry about dibasic acids like H2SO4?',
        'answer': 'Yes, for a strong dibasic acid, [H+] is approximately twice the concentration of the acid. Remember to multiply by 2 before taking the -log.'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_{PACK_META['subtopic_code']}_pH_Scale.pdf ...")
    # PDF generation logic here

if __name__ == '__main__':
    generate_pdf()
