# t14_4_ka_pka.py
PACK_META = {
    'candidate': 'Usman',
    'topic_code': '14',
    'topic_name': 'Acid-Base Equilibria',
    'subtopic_code': '14A.4',
    'subtopic_name': 'Analysing Data from pH Measurements'
}

QUESTIONS = [
    {
        'q_num': 1,
        'question': 'Calculate the pH of 0.1 mol dm-3 ethanoic acid (Ka = 1.7x10^-5 mol dm-3).',
        'marks': 2,
        'mark_scheme': '[H+] = sqrt(Ka x [HA]) = sqrt(1.7e-5 x 0.1) = 1.30e-3. pH = 2.89',
        'ref': 'WCH14/01/Oct20/Q19(c)'
    }
]

FAQS = [
    {
        'question': 'When can I use the approximation [HA]eq ≈ [HA]initial?',
        'answer': 'When dissociation is very small (usually when Ka is small and concentration is relatively high).'
    }
]

def generate_pdf():
    print(f"Generating Usman_Edexcel_Chem_U4_14A4_Ka_pKa.pdf ...")

if __name__ == '__main__':
    generate_pdf()
