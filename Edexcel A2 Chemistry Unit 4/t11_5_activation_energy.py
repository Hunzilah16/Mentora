from build_edexcel_u4_pdf import build_pdf_pack
import os

PACK_META = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A.5',
    'subtopic_name': 'Activation Energy and Catalysis'
}

QUESTIONS = [
    {
        'question': 'Q1. Explain how a catalyst increases the rate of a chemical reaction.',
        'marks': 2,
        'mark_scheme': [
            'Provides an alternative pathway/mechanism (1)',
            'With a lower activation energy (1)'
        ],
        'reference': 'WCH14/01/Oct22/Q3(a)'
    },
    {
        'question': 'Q2. Distinguish between homogeneous and heterogeneous catalysis.',
        'marks': 2,
        'mark_scheme': [
            'Homogeneous: catalyst is in the same phase/state as the reactants (1)',
            'Heterogeneous: catalyst is in a different phase/state from the reactants (1)'
        ],
        'reference': 'WCH14/01/Oct22/Q3(b)'
    },
    {
        'question': 'Q3. Describe the steps involved in heterogeneous catalysis.',
        'marks': 3,
        'mark_scheme': [
            'Adsorption of reactants onto the catalyst surface (1)',
            'Bonds break and form / reaction occurs on the surface (1)',
            'Desorption of products from the surface (1)'
        ],
        'reference': 'WCH14/01/Jun21/Q4(a)'
    },
    {
        'question': 'Q4. Using the Maxwell-Boltzmann distribution, explain why a small increase in temperature leads to a large increase in the rate of reaction.',
        'marks': 2,
        'mark_scheme': [
            'Many more molecules have energy greater than or equal to the activation energy (1)',
            'Higher frequency of successful collisions (1)'
        ],
        'reference': 'WCH14/01/Jun21/Q4(b)'
    }
]

FAQS = [
    {
        'question': 'Does a catalyst change the position of equilibrium?',
        'answer': 'No, it increases the rate of both the forward and backward reactions equally, so the equilibrium position remains unchanged.'
    },
    {
        'question': 'What is catalyst poisoning?',
        'answer': 'When impurities bind strongly to the active sites of a heterogeneous catalyst, blocking reactants from adsorbing and reducing catalytic efficiency.'
    },
    {
        'question': 'Why is adsorption strength important for a heterogeneous catalyst?',
        'answer': 'It must be strong enough to weaken bonds in the reactants, but weak enough to allow products to desorb.'
    }
]

if __name__ == "__main__":
    build_pdf_pack(PACK_META, QUESTIONS, FAQS, "Usman_Edexcel_Chem_U4_11A5_Activation_Energy.pdf")
