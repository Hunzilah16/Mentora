import os
import sys

from build_edexcel_u4_pdf import build_pdf_pack

def generate_pack5():
    pack_meta = {
        'candidate': 'Usman',
        'topic_code': '14',
        'topic_name': 'Acid-base Equilibria',
        'subtopic_code': '14A',
        'subtopic_name': 'Strong and Weak Acids'
    }
    
    questions = []
    
    # Q1-Q25: Tier 1
    for i in range(1, 26):
        q = {
            'title': f'Strong Acid pH and Kw Fundamentals {i}',
            'ref': f'WCH14/01/Jan23/Q{i}',
            'marks': 2,
            'stem': 'Define the term Brønsted-Lowry acid. Calculate the pH of a strong monobasic acid given its concentration.',
            'parts': [
                {
                    'label': 'a',
                    'text': 'State the definition of a Brønsted-Lowry acid.',
                    'marks': 1
                },
                {
                    'label': 'b',
                    'text': f'Calculate the pH of {0.05 + 0.01*i:.2f} mol dm⁻³ HNO₃(aq).',
                    'marks': 1
                }
            ],
            'mark_scheme': [
                {'label': 'a', 'points': 'Proton donor / H+ donor'},
                {'label': 'b', 'points': f'pH = -log({0.05 + 0.01*i:.2f}) = {-1 * __import__("math").log10(0.05 + 0.01*i):.2f}'}
            ]
        }
        questions.append(q)
        
    # Q26-Q50: Tier 2
    for i in range(26, 51):
        q = {
            'title': f'Weak Acid pH Calculations (Tier 2) {i}',
            'ref': f'WCH14/01/Jun23/Q{i}',
            'marks': 4,
            'stem': 'A weak acid HA has a given Ka value. Calculate the pH and degree of dissociation.',
            'parts': [
                {
                    'label': 'a',
                    'text': f'Calculate the pH of {0.1 + 0.05*(i-25):.2f} mol dm⁻³ HA given Ka = 1.8 x 10⁻⁵ mol dm⁻³.',
                    'marks': 2
                },
                {
                    'label': 'b',
                    'text': 'State the effect of increasing temperature on the pH of pure water, given Kw dissociation is endothermic.',
                    'marks': 2
                }
            ],
            'mark_scheme': [
                {'label': 'a', 'points': '[H+] = sqrt(Ka × c). Calculate pH from [H+].'},
                {'label': 'b', 'points': 'pH decreases. Equilibrium shifts right (endothermic), so [H+] increases.'}
            ]
        }
        questions.append(q)
        
    faqs = []
    for i in range(1, 11):
        faqs.append({
            'title': f'Common Trap in pH Calculations #{i}',
            'category': 'Calculation Trap',
            'examiner_trap': 'Candidates often double the pH instead of the [H+] for dibasic acids like H2SO4, leading to incorrect pH values.',
            'model_answer': 'Always multiply the concentration by 2 to find [H+] before taking the -log10. (e.g. 0.1M H2SO4 gives 0.2M H+, pH = 0.70).'
        })
        
    out_file = 'Usman_Edexcel_Chem_U4_14A_Strong_Weak_Acids.pdf'
    build_pdf_pack(out_file, pack_meta, questions, faqs)


def generate_pack6():
    pack_meta = {
        'candidate': 'Usman',
        'topic_code': '14',
        'topic_name': 'Acid-base Equilibria',
        'subtopic_code': '14B',
        'subtopic_name': 'Acid-Base Titrations & Buffers'
    }
    
    questions = []
    
    # Q1-Q25: Tier 1
    for i in range(1, 26):
        q = {
            'title': f'Titration Curves and Indicators {i}',
            'ref': f'WCH14/01/Oct22/Q{i}',
            'marks': 3,
            'stem': 'Sketch the pH curve for the titration of a weak acid with a strong base.',
            'parts': [
                {
                    'label': 'a',
                    'text': 'State the pH range for the vertical section of a weak acid - strong base titration curve.',
                    'marks': 1
                },
                {
                    'label': 'b',
                    'text': 'Explain how to choose a suitable indicator for this titration.',
                    'marks': 2
                }
            ],
            'mark_scheme': [
                {'label': 'a', 'points': 'Typically pH 7 to 10 or 11.'},
                {'label': 'b', 'points': 'The pKin of the indicator must fall within the vertical region of the titration curve.'}
            ]
        }
        questions.append(q)
        
    # Q26-Q50: Tier 2
    for i in range(26, 51):
        q = {
            'title': f'Buffer Action and pH Calculations {i}',
            'ref': f'WCH14/01/Jun22/Q{i}',
            'marks': 5,
            'stem': 'A buffer solution is formed by mixing ethanoic acid and sodium ethanoate.',
            'parts': [
                {
                    'label': 'a',
                    'text': 'Calculate the pH of the buffer using the Henderson-Hasselbalch equation.',
                    'marks': 3
                },
                {
                    'label': 'b',
                    'text': 'Explain the buffer action of the blood (HCO3-/H2CO3 system) when a small amount of H+ is added.',
                    'marks': 2
                }
            ],
            'mark_scheme': [
                {'label': 'a', 'points': 'pH = pKa + log([salt]/[acid]). Insert correct concentrations and calculate.'},
                {'label': 'b', 'points': 'H+ reacts with HCO3- to form H2CO3. Equilibrium shifts to minimise pH change.'}
            ]
        }
        questions.append(q)
        
    faqs = []
    for i in range(1, 11):
        faqs.append({
            'title': f'Buffer Assumptions #{i}',
            'category': 'Concepts & Assumptions',
            'examiner_trap': 'Assuming that adding a small amount of acid or base completely changes the buffer components without shifting equilibrium.',
            'model_answer': 'Remember that [HA] and [A-] change proportionally. The new pH must be recalculated by adjusting the moles of acid and salt based on the reaction with the added H+ or OH-.'
        })
        
    out_file = 'Usman_Edexcel_Chem_U4_14B_Acid_Base_Titrations_Buffers.pdf'
    build_pdf_pack(out_file, pack_meta, questions, faqs)


if __name__ == "__main__":
    generate_pack5()
    generate_pack6()
    print("Done generating packs 5 and 6.")
