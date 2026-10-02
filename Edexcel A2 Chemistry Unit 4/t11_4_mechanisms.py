from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.4',
    'subtopic_name': 'Rate Equations and Mechanisms'
}

QUESTIONS = [
    {
        'question': 'Q1. The rate equation for a reaction is rate = k[A][B]^2. Suggest the species involved in the rate-determining step.',
        'marks': 1,
        'mark_scheme': [
            'One molecule of A and two molecules of B (1)'
        ],
        'reference': 'WCH14/01/Jun22/Q5(a)'
    },
    {
        'question': 'Q2. Define the term "rate-determining step".',
        'marks': 1,
        'mark_scheme': [
            'The slowest step in a multi-step reaction mechanism (1)'
        ],
        'reference': 'WCH14/01/Jun22/Q5(b)'
    },
    {
        'question': 'Q3. The reaction between propanone and iodine in acidic conditions is zero order with respect to iodine. Explain what this tells you about the mechanism.',
        'marks': 1,
        'mark_scheme': [
            'Iodine is not involved in the rate-determining step / is involved after the rate-determining step (1)'
        ],
        'reference': 'WCH14/01/Jan21/Q2(a)'
    },
    {
        'question': 'Q4. SN1 and SN2 mechanisms have different kinetics. Which mechanism is associated with a first-order overall rate equation?',
        'marks': 1,
        'mark_scheme': [
            'SN1 mechanism (1)'
        ],
        'reference': 'WCH14/01/Jan21/Q2(b)'
    }
]

FAQS = [
    {
        'question': 'Can a reaction have a termolecular rate-determining step?',
        'answer': 'It is very rare as the probability of three species colliding simultaneously with the correct orientation and sufficient energy is extremely low.'
    },
    {
        'question': 'Does the rate-determining step always occur first?',
        'answer': 'No, it can occur at any point in the mechanism. Intermediates formed before the RDS will appear in the rate equation.'
    },
    {
        'question': 'How do SN1 and SN2 differ in their RDS?',
        'answer': 'SN1 RDS involves only the halogenoalkane (unimolecular), while SN2 RDS involves both the halogenoalkane and the nucleophile (bimolecular).'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A4_Mechanisms.pdf")
