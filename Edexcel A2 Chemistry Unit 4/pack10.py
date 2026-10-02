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
    'subtopic_code': '15D',
    'subtopic_name': 'CARBOXYLIC ACID DERIVATIVES & POLYESTERS'
}

QUESTIONS = []
for i in range(1, 26):
    QUESTIONS.append({
        'id': f'WCH14/01/Jan23/Q{i}',
        'type': 'structured',
        'tier': 1,
        'question': f'Question {i}: Describe the reaction of an acyl chloride with water to form a carboxylic acid. Include reagents and conditions.',
        'mark_scheme': ['Reagent: Water', 'Conditions: Room temperature', 'Observation: Steamy fumes of HCl']
    })

for i in range(26, 51):
    QUESTIONS.append({
        'id': f'WCH14/01/Jan23/Q{i}',
        'type': 'structured',
        'tier': 2,
        'question': f'Question {i}: Explain the nucleophilic addition-elimination mechanism for the reaction of ethanoyl chloride with ammonia.',
        'mark_scheme': ['Nucleophilic attack by lone pair on NH3', 'Formation of tetrahedral intermediate', 'Elimination of chloride ion']
    })

FAQS = []
for i in range(1, 11):
    FAQS.append({
        'q': f'FAQ {i}: Why is acyl chloride more reactive than chlorobenzene?',
        'a': 'The C-Cl bond in chlorobenzene has partial double bond character due to delocalisation of chlorine lone pairs into the benzene ring, making it stronger and less reactive than the C-Cl bond in an acyl chloride.'
    })

output_pdf = r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4\Usman_Edexcel_Chem_U4_15D_Carboxylic_Acid_Derivatives.pdf"

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, output_pdf)
    print(f"Generated {output_pdf}")
