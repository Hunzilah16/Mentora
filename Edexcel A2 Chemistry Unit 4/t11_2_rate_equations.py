from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.2',
    'subtopic_name': 'Rate Equations, Rate Constants and Orders of Reaction'
}

QUESTIONS = [
    {
        'question': 'Q1. The reaction between NO and O2 is second order with respect to NO and first order with respect to O2. Write the rate equation for this reaction.',
        'marks': 1,
        'mark_scheme': [
            'rate = k[NO]^2[O2] (1)'
        ],
        'reference': 'WCH14/01/Oct22/Q2(a)'
    },
    {
        'question': 'Q2. Deduce the units of the rate constant, k, for the reaction in Q1.',
        'marks': 1,
        'mark_scheme': [
            'dm^6 mol^-2 s^-1 (1)'
        ],
        'reference': 'WCH14/01/Oct22/Q2(b)'
    },
    {
        'question': 'Q3. What is meant by the term "order of reaction" with respect to a given reactant?',
        'marks': 1,
        'mark_scheme': [
            'The power to which the concentration of that reactant is raised in the rate equation (1)'
        ],
        'reference': 'WCH14/01/Jun21/Q1(a)'
    },
    {
        'question': 'Q4. Explain what is meant by the overall order of a reaction.',
        'marks': 1,
        'mark_scheme': [
            'The sum of the powers of the concentration terms in the rate equation (1)'
        ],
        'reference': 'WCH14/01/Jun21/Q1(b)'
    }
]

FAQS = [
    {
        'question': 'How do I determine units for k?',
        'answer': 'Substitute the units of rate (mol dm^-3 s^-1) and concentrations (mol dm^-3) into the rate equation and cancel them out.'
    },
    {
        'question': 'Is zero order included in the rate equation?',
        'answer': 'No, any concentration raised to the power of zero is 1, so it is typically omitted from the rate equation.'
    },
    {
        'question': 'Can orders of reaction be fractional?',
        'answer': 'Yes, though they are usually integers (0, 1, 2) in A-level questions, fractional orders are possible.'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A2_Rate_Equations.pdf")
