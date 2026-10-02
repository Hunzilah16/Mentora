PACK_META = {
    'candidate': 'Usman',
    'topic_code': '13A',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '',
    'subtopic_name': '',
    'brand': 'Mentora Academy',
    'contact': 'mentoraonlineacademy@gmail.com   •   +923164586836'
}

# Generate 50 questions
QUESTIONS = []
for i in range(1, 26):
    QUESTIONS.append({
        'number': i,
        'question': f'Write the Kc expression for the reaction A + 2B <-> C and determine its units. (WCH14/01/Jan23/Q{i}(a))',
        'marks': 2,
        'mark_scheme': 'Kc = [C] / ([A][B]^2), Units: dm^3 mol^-1'
    })
for i in range(26, 51):
    QUESTIONS.append({
        'number': i,
        'question': f'Calculate Kp given the partial pressures: p(A) = 1.2 atm, p(B) = 2.0 atm, p(C) = 4.8 atm for A + B <-> 2C. (WCH14/01/Oct22/Q{i}(b))',
        'marks': 3,
        'mark_scheme': 'Kp = (4.8)^2 / (1.2 * 2.0) = 23.04 / 2.4 = 9.6 atm^0 / no units'
    })

FAQS = [
    {'q': 'Does adding a catalyst change the value of Kc?', 'a': 'No, a catalyst speeds up both forward and backward reactions equally, reaching equilibrium faster but not changing the equilibrium constant.'},
    {'q': 'Why does an increase in pressure not change Kp?', 'a': 'The equilibrium position shifts to counteract the change and keep Kp constant. Kp is only dependent on temperature.'},
    {'q': 'How does temperature affect K for an exothermic reaction?', 'a': 'Increasing temperature decreases K, as the equilibrium shifts to the endothermic (backward) direction.'},
    {'q': 'What does a large value of Kc indicate?', 'a': 'A large Kc indicates that products are favored at equilibrium.'},
    {'q': 'How to calculate mole fraction?', 'a': 'Mole fraction = moles of substance / total moles in the mixture.'},
    {'q': 'What is the relation between Delta S_total and K?', 'a': 'Delta S_total = R ln K'},
    {'q': 'Why do we ignore solids in heterogeneous equilibrium expressions?', 'a': 'The concentration of a pure solid is constant and is incorporated into the equilibrium constant.'},
    {'q': 'When do Kc and Kp have no units?', 'a': 'When the number of moles of gaseous reactants equals the number of moles of gaseous products.'},
    {'q': 'How is partial pressure calculated?', 'a': 'Partial pressure = mole fraction * total pressure.'},
    {'q': 'How do you solve a quadratic equation for Kc?', 'a': 'Use the quadratic formula, ensuring the chosen root makes physical sense (i.e. positive concentrations).'}
]
