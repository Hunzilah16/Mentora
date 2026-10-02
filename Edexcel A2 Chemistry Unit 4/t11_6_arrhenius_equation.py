from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.6',
    'subtopic_name': 'Effect of Temperature on the Rate Constant'
}

QUESTIONS = [
    {
        'question': 'Q1. State the Arrhenius equation and define all terms within it.',
        'marks': 4,
        'mark_scheme': [
            'k = A e^(-Ea/RT) (1)',
            'k = rate constant, A = pre-exponential/frequency factor (1)',
            'Ea = activation energy, R = gas constant (1)',
            'T = temperature in Kelvin (1)'
        ],
        'reference': 'WCH14/01/Jan23/Q5(a)'
    },
    {
        'question': 'Q2. A graph of ln k against 1/T is plotted for a reaction. The gradient is -10500 K. Calculate the activation energy in kJ mol^-1. (R = 8.31 J K^-1 mol^-1)',
        'marks': 3,
        'mark_scheme': [
            'gradient = -Ea / R (1)',
            '-10500 = -Ea / 8.31 (1)',
            'Ea = +87255 J mol^-1 = +87.3 kJ mol^-1 (1)'
        ],
        'reference': 'WCH14/01/Jan23/Q5(b)'
    },
    {
        'question': 'Q3. What does the y-intercept of a graph of ln k against 1/T represent?',
        'marks': 1,
        'mark_scheme': [
            'ln A (the natural log of the pre-exponential factor) (1)'
        ],
        'reference': 'WCH14/01/Oct21/Q6(a)'
    },
    {
        'question': 'Q4. Explain the effect of increasing temperature on the value of the rate constant, k.',
        'marks': 2,
        'mark_scheme': [
            'k increases exponentially as temperature increases (1)',
            'Because the term e^(-Ea/RT) increases (1)'
        ],
        'reference': 'WCH14/01/Oct21/Q6(b)'
    }
]

FAQS = [
    {
        'question': 'What are the units for activation energy?',
        'answer': 'When calculated using R = 8.31 J K^-1 mol^-1, Ea is in J mol^-1. It is usually converted to kJ mol^-1 for the final answer.'
    },
    {
        'question': 'Do I need to convert temperature to Kelvin?',
        'answer': 'Yes, T must always be in Kelvin (K) when using the Arrhenius equation.'
    },
    {
        'question': 'What is the significance of the pre-exponential factor A?',
        'answer': 'It represents the frequency of collisions with the correct orientation for reaction.'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A6_Arrhenius_Equation.pdf")
