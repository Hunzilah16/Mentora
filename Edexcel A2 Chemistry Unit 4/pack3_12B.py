PACK_META = {
    'candidate': 'Usman',
    'topic_code': '12B',
    'topic_name': 'LATTICE ENERGY & ENERGETICS',
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
        'question': f'Define the standard enthalpy of lattice energy. (WCH14/01/Jan23/Q{i}(a))',
        'marks': 2,
        'mark_scheme': 'The enthalpy change when one mole of an ionic solid is formed from its gaseous ions under standard conditions.'
    })
for i in range(26, 51):
    QUESTIONS.append({
        'number': i,
        'question': f'Explain the difference between theoretical and experimental lattice energy for silver iodide. (WCH14/01/Oct22/Q{i}(b))',
        'marks': 3,
        'mark_scheme': 'Experimental value is more exothermic than theoretical. This indicates covalent character in AgI due to polarization of the iodide ion by the silver ion.'
    })

FAQS = [
    {'q': 'Why is the second electron affinity of oxygen always endothermic?', 'a': 'Because the O- ion is repelling the incoming electron, which requires energy to overcome.'},
    {'q': 'What does a large difference between theoretical and experimental lattice energy mean?', 'a': 'It indicates significant covalent character in the ionic lattice, usually due to a small, highly charged cation polarizing a large anion.'},
    {'q': 'Why does solubility of group 2 sulfates decrease down the group?', 'a': 'The hydration enthalpy decreases more rapidly than the lattice energy down the group, making the enthalpy of solution more endothermic.'},
    {'q': 'How does polarization affect lattice energy?', 'a': 'Polarization increases the electrostatic attraction beyond the pure ionic model, resulting in a more exothermic lattice energy.'},
    {'q': 'Why is atomisation always endothermic?', 'a': 'Energy is required to break bonds to form gaseous atoms.'},
    {'q': 'What happens to lattice energy down a group?', 'a': 'It becomes less exothermic as ionic radius increases, so the distance between ions is larger and attraction is weaker.'},
    {'q': 'What is Fajans rules?', 'a': 'Rules to predict covalent character in ionic compounds based on cation charge/size and anion size.'},
    {'q': 'Why does theoretical calculation assume pure ionic model?', 'a': 'It assumes ions are perfect spheres and point charges with no polarization.'},
    {'q': 'How to calculate enthalpy of hydration from lattice energy and solution enthalpy?', 'a': 'Delta_sol H = - Lattice Energy + sum(Hydration Enthalpies)'},
    {'q': 'Why do Group 2 compounds generally have more exothermic lattice energies than Group 1?', 'a': 'Group 2 cations have a +2 charge and are smaller, leading to stronger electrostatic attraction with anions.'}
]
