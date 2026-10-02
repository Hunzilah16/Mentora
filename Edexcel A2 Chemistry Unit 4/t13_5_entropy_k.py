PACK_META = {
    'candidate': 'Usman',
    'topic_code': '13',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '13A.5',
    'subtopic_name': 'Relating Entropy to Equilibrium Constants',
    'institution': 'Mentora Academy',
    'branding': 'Mentora Visual Style (Navy #0b1b36, Crimson #a81717, Steel Blue #1e3a8a, Poppins fonts)',
    'contact_line': 'mentoraonlineacademy@gmail.com   •   +923164586836'
}

QUESTIONS = [
    {
        'type': 'structured',
        'question': '1. The total entropy change, ΔS_total, for a reaction at 298 K is +45.0 J K-1 mol-1. Calculate the value of the equilibrium constant, K, for this reaction at 298 K. (R = 8.31 J K-1 mol-1)',
        'marks': 3,
        'reference': 'WCH14/01/Jan23/Q6',
        'mark_scheme': '1. ΔS_total = R ln K\n2. ln K = 45.0 / 8.31 = 5.415\n3. K = e^5.415 = 225'
    },
    {
        'type': 'structured',
        'question': '2. State the relationship between ΔS_total and the position of equilibrium when ΔS_total is very large and negative.',
        'marks': 2,
        'reference': 'WCH14/01/Jun22/Q7',
        'mark_scheme': '1. When ΔS_total is large and negative, ln K is large and negative.\n2. K is very small, so the equilibrium lies very far to the left (reaction effectively does not go).'
    },
    {
        'type': 'mcq',
        'question': '3. Which equation correctly relates total entropy change to the equilibrium constant?',
        'options': ['A. ΔS_total = -R ln K', 'B. ΔS_total = R ln K', 'C. K = R ln ΔS_total', 'D. ΔS_total = e^(R/K)'],
        'answer': 'B',
        'marks': 1,
        'reference': 'WCH14/01/Oct21/Q6'
    }
]

FAQS = [
    {
        'question': 'What are the units for K when calculated from ΔS_total?',
        'answer': 'The K calculated from ΔS_total is a dimensionless thermodynamic equilibrium constant. You do not need to provide units for K in this specific context unless explicitly asked to deduce them from the equation.'
    },
    {
        'question': 'How do I handle the gas constant R?',
        'answer': 'Always use R = 8.31 J K-1 mol-1. Make sure your ΔS_total is in J K-1 mol-1 before using the equation. If ΔS_total is given in kJ K-1 mol-1, multiply by 1000 first.'
    },
    {
        'question': 'Why do I get a math error on my calculator when finding ln K?',
        'answer': 'You might be calculating e to a very large positive or negative power. If ln K > 100, K is huge (reaction goes to completion). If ln K < -100, K is tiny (reaction doesn\'t happen). Write "very large" or "very small" if the calculator overflows.'
    }
]
