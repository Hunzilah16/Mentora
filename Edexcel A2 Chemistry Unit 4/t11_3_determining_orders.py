from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.3',
    'subtopic_name': 'Determining Orders of Reaction'
}

QUESTIONS = [
    {
        'question': 'Q1. Explain how a concentration-time graph can be used to show that a reaction is first order.',
        'marks': 2,
        'mark_scheme': [
            'Measure successive half-lives (1)',
            'Half-life is constant / independent of concentration (1)'
        ],
        'reference': 'WCH14/01/Jan22/Q3(a)'
    },
    {
        'question': 'Q2. A first order reaction has a rate constant of 2.5 x 10^-3 s^-1. Calculate its half-life.',
        'marks': 2,
        'mark_scheme': [
            't_1/2 = ln2 / k (1)',
            't_1/2 = 0.693 / 2.5x10^-3 = 277 s (1)'
        ],
        'reference': 'WCH14/01/Jan22/Q3(b)'
    },
    {
        'question': 'Q3. Describe how the initial rate of reaction can be found from a concentration-time graph.',
        'marks': 2,
        'mark_scheme': [
            'Draw a tangent to the curve at time t=0 (1)',
            'Calculate the gradient of the tangent (1)'
        ],
        'reference': 'WCH14/01/Oct21/Q4(a)'
    },
    {
        'question': 'Q4. In an iodine clock reaction, the time taken for a color change is measured. State the assumption made when calculating the initial rate as 1/t.',
        'marks': 1,
        'mark_scheme': [
            'The rate is constant over the time measured / concentration changes are small (1)'
        ],
        'reference': 'WCH14/01/Oct21/Q4(b)'
    }
]

FAQS = [
    {
        'question': 'Why is drawing a tangent at t=0 difficult?',
        'answer': 'Because the curve is steepest at the start, slight errors in drawing the line can lead to large variations in the calculated initial rate.'
    },
    {
        'question': 'How many half-lives must be measured to prove first order?',
        'answer': 'At least two successive half-lives must be measured to show that they are constant.'
    },
    {
        'question': 'What does a zero order concentration-time graph look like?',
        'answer': 'It is a straight line with a constant negative gradient.'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A3_Determining_Orders.pdf")
