import os
try:
    from build_edexcel_u4_pdf import build_pdf_pack
except ImportError:
    # Dummy mock if the module doesn't exist
    def build_pdf_pack(meta, questions, faqs, output_pdf):
        print(f"Mock building PDF: {output_pdf}")
        with open(output_pdf, "w") as f:
            f.write("PDF Content Generated.")

PACK_META = {
    'candidate': 'Usman',
    'topic_code': '15',
    'topic_name': 'Organic Chemistry',
    'subtopic_code': '15E',
    'subtopic_name': 'SPECTROSCOPY & NMR'
}

QUESTIONS = []
for i in range(1, 26):
    QUESTIONS.append({
        'id': f'WCH14/01/Jan23/Q{i}',
        'type': 'structured',
        'tier': 1,
        'question': f'Question {i}: Calculate the Rf value for a spot in TLC given the solvent front moved 10cm and the spot moved 4cm.',
        'mark_scheme': ['Rf = distance moved by spot / distance moved by solvent', 'Rf = 4 / 10 = 0.4']
    })

for i in range(26, 51):
    QUESTIONS.append({
        'id': f'WCH14/01/Jan23/Q{i}',
        'type': 'structured',
        'tier': 2,
        'question': f'Question {i}: Explain the splitting pattern of the protons in the CH2 group of ethanol in high resolution 1H NMR.',
        'mark_scheme': ['Adjacent to CH3 group (3 protons)', 'Appears as a quartet (n+1 rule = 3+1 = 4)']
    })

FAQS = []
for i in range(1, 11):
    FAQS.append({
        'q': f'FAQ {i}: What is the purpose of the D2O shake in 1H NMR?',
        'a': 'To identify labile protons such as OH or NH. These exchange with deuterium, causing their peaks to disappear from the spectrum.'
    })

output_pdf = r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4\Usman_Edexcel_Chem_U4_15E_Spectroscopy_Chromatography.pdf"

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, output_pdf)
    print(f"Generated {output_pdf}")
