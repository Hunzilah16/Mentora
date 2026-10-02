from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.1',
    'subtopic_name': 'Techniques for Measuring the Rate of Reaction'
}

QUESTIONS = [
    {
        'question': 'Q1. Explain why the rate of reaction between iodine and propanone can be measured by colorimetry.',
        'marks': 2,
        'mark_scheme': [
            'Iodine is colored (1)',
            'Absorbance is proportional to concentration (1)'
        ],
        'reference': 'WCH14/01/Jan23/Q1(a)'
    }
]

FAQS = [
    {
        'question': 'Can gas collection be used for all reactions?',
        'answer': 'No, only those that produce a significant volume of gas.'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A1_Rate_Measurement.pdf")
