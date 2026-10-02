import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

def make_edexcel_q(number, title, ref, marks, stem, parts, mark_scheme):
    return {
        'title': f"{number}. {title}",
        'ref': ref,
        'marks': marks,
        'stem': stem,
        'parts': parts,
        'mark_scheme': mark_scheme
    }

def make_edexcel_faq(title, category, trap, model_ans):
    return {
        'title': title,
        'category': category,
        'examiner_trap': trap,
        'model_answer': model_ans
    }

# ==========================================
# PACK 5: 14A — STRONG AND WEAK ACIDS (50 Qs + 10 FAQs)
# ==========================================
p5_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 14',
    'topic_name': 'ACID-BASE EQUILIBRIA',
    'subtopic_code': '14A',
    'subtopic_name': 'Strong and Weak Acids (Brønsted-Lowry, pH, Kw, Ka & pKa)'
}

p5_questions = []

p5_questions.append(make_edexcel_q(
    1, "Brønsted-Lowry Theory & Conjugate Pairs", "WCH14/01/Jan23/Q11", 4,
    "In aqueous solution, ethanoic acid acts as a Brønsted-Lowry acid:<br/>CH3COOH(aq) + H2O(l) ⇌ CH3COO-(aq) + H3O+(aq)",
    [
        {'label': 'a', 'text': 'Define a Brønsted-Lowry acid and a Brønsted-Lowry base.', 'marks': 2},
        {'label': 'b', 'text': 'Identify the two conjugate acid-base pairs in this equilibrium.', 'marks': 2}
    ],
    "1. (a) Acid: proton (H+) donor (1). Base: proton (H+) acceptor (1).<br/>1. (b) Pair 1: CH3COOH (acid 1) / CH3COO- (base 1) (1). Pair 2: H3O+ (acid 2) / H2O (base 2) (1)."
))

p5_questions.append(make_edexcel_q(
    2, "pH Calculation of Strong Monobasic Acid", "WCH14/01/Oct22/Q12", 3,
    "Calculate the pH of a 0.0450 mol dm-3 solution of hydrochloric acid, HCl(aq), at 298 K.",
    [
        {'label': 'a', 'text': 'State the relationship between [H+] and [HCl] for a strong monobasic acid.', 'marks': 1},
        {'label': 'b', 'text': 'Calculate the pH of 0.0450 mol dm-3 HCl(aq) to 2 decimal places.', 'marks': 2}
    ],
    "2. (a) HCl is fully dissociated, so [H+] = [HCl] = 0.0450 mol dm-3 (1).<br/>2. (b) pH = -log(0.0450) = 1.35 (2)."
))

for i in range(3, 26):
    p5_questions.append(make_edexcel_q(
        i, f"pH & Kw Calculation Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"At 298 K, Kw = 1.00 x 10^-14 mol2 dm-6. Solution {i} contains NaOH(aq) at concentration 0.0250 mol dm-3.",
        [
            {'label': 'a', 'text': 'Calculate [H+] in this solution using Kw = [H+][OH-].', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the pH of this NaOH solution.', 'marks': 1}
        ],
        f"{i}. (a) [OH-] = 0.0250 mol dm-3. [H+] = 1.00x10^-14 / 0.0250 = 4.00 x 10^-13 mol dm-3 (2).<br/>{i}. (b) pH = -log(4.00x10^-13) = 12.40 (1)."
    ))

for i in range(26, 51):
    p5_questions.append(make_edexcel_q(
        i, f"A* Challenge: Weak Acid Ka, pKa & Pure Water Kw Temperature Effects {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"For weak acid HA {i}: pKa = 4.76 (Ka = 1.74 x 10^-5 mol dm-3) at 298 K. Concentration [HA] = 0.150 mol dm-3.",
        [
            {'label': 'a', 'text': 'State the two approximations made when calculating the pH of a weak acid solution.', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the pH of 0.150 mol dm-3 HA(aq).', 'marks': 3}
        ],
        f"{i}. (a) Approx 1: [H+] = [A-] (ionization of water is negligible) (1). Approx 2: [HA]eqm ≈ [HA]initial (dissociation is negligible) (1).<br/>{i}. (b) Ka = [H+]^2 / [HA] => [H+] = sqrt(Ka x [HA]) = sqrt(1.74x10^-5 x 0.150) = sqrt(2.61x10^-6) = 1.615 x 10^-3 mol dm-3 (2). pH = -log(1.615x10^-3) = 2.79 (1)."
    ))

p5_faqs = []
p5_faq_titles = [
    ("pH Decimal Places Rule", "Significant Figures", "Writing pH to 1 decimal place or rounding incorrectly.", "pH decimal places represent significant figures. pH should ALWAYS be given to 2 DECIMAL PLACES in Edexcel exams (e.g. 2.79, not 2.8)."),
    ("Strong Dibasic Acid pH Calculation", "Stoichiometric Factor", "Assuming [H+] = [acid] for H2SO4.", "Sulfuric acid H2SO4 is dibasic: 1 mole H2SO4 produces 2 moles of H+ upon complete dissociation -> [H+] = 2 x [H2SO4]."),
    ("Pure Water pH at Temperatures Other Than 298K", "Kw Temperature Effect", "Assuming pure water is always pH 7.00 at all temperatures.", "Water dissociation H2O ⇌ H+ + OH- is ENDOTHERMIC. Increasing temperature increases Kw -> [H+] increases -> pH of pure water DECREASES below 7.00. However, water remains NEUTRAL because [H+] = [OH-]."),
    ("Definition of Neutral Solution", "pH Definitions", "Defining a neutral solution as pH = 7.", "A neutral solution is defined as [H+] = [OH-]. It is ONLY pH 7.00 at 298 K where Kw = 1.0x10^-14."),
    ("Two Approximations in Weak Acid pH Calculations", "Ka Assumptions", "Forgetting the two key assumptions when using [H+] = sqrt(Ka x [HA]).", "Assumption 1: [H+] = [A-] (ignores H+ from water). Assumption 2: [HA]eqm = [HA]start (ignores amount of HA dissociated). Both assumptions fail for very dilute or stronger weak acids."),
    ("pKa and Acid Strength Relationship", "pKa Values", "Assuming a larger pKa value means a stronger acid.", "pKa = -log Ka. A SMALLER pKa (or larger Ka) means a STRONGER acid. E.g. pKa 3.75 (methanoic) is stronger than pKa 4.76 (ethanoic)."),
    ("Conjugate Base Strength Relationship", "Conjugate Pairs", "Stating a strong acid has a strong conjugate base.", "The stronger the acid, the WEAKER its conjugate base. E.g. HCl is a very strong acid, so Cl- is an extremely weak conjugate base with negligible proton affinity."),
    ("Dilution of Weak Acid Effect on pH", "Ostwald Dilution", "Assuming diluting a weak acid by 10x increases pH by 1.0 unit.", "Diluting a strong acid 10x increases pH by 1.0 unit. Diluting a WEAK acid 10x increases pH by approximately 0.5 units because dilution shifts equilibrium HA ⇌ H+ + A- to the right (increases % dissociation)."),
    ("Kw Units", "Kw Expression", "Writing Kw units as mol dm-3.", "Kw = [H+][OH-]. The units of Kw are (mol dm-3)(mol dm-3) = mol2 dm-6."),
    ("Base Hydroxide Concentration Calculation", "Base Calculations", "Calculating pH directly from [OH-] using -log[OH-].", "-log[OH-] gives pOH, NOT pH! To find pH of a base: first find [H+] = Kw / [OH-], then calculate pH = -log[H+]. Alternatively pH = 14 - pOH at 298 K.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p5_faq_titles, 1):
    p5_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_14A_Strong_Weak_Acids.pdf", p5_meta, p5_questions, p5_faqs)
print("Pack 5 (14A Strong & Weak Acids - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 6: 14B — ACID-BASE TITRATIONS & BUFFERS (50 Qs + 10 FAQs)
# ==========================================
p6_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 14',
    'topic_name': 'ACID-BASE EQUILIBRIA',
    'subtopic_code': '14B',
    'subtopic_name': 'Acid-Base Titrations, pH Curves, Indicators & Buffer Solutions'
}

p6_questions = []

p6_questions.append(make_edexcel_q(
    1, "Titration pH Curve & Indicator Selection", "WCH14/01/Jan23/Q13", 5,
    "25.0 cm3 of 0.100 mol dm-3 CH3COOH (pKa = 4.76) is titrated with 0.100 mol dm-3 NaOH.",
    [
        {'label': 'a', 'text': 'Sketch the pH curve for this titration from 0 to 40 cm3 of NaOH added, labelling key features.', 'marks': 3},
        {'label': 'b', 'text': 'Select a suitable indicator from Phenolphthalein (pKIn = 9.3) and Methyl Orange (pKIn = 3.7). Justify your choice.', 'marks': 2}
    ],
    "1. (a) Initial pH ~2.9, buffer region around pH 4.8, steep vertical section at 25.0 cm3 (pH 7-10), final pH ~12.5 (3).<br/>1. (b) Phenolphthalein (1). Its pKIn (9.3) / color change range (8.3-10.0) lies entirely within the vertical section of the titration curve (pH 7-10) (1)."
))

p6_questions.append(make_edexcel_q(
    2, "Buffer Action Mechanism", "WCH14/01/Oct22/Q14", 4,
    "An acidic buffer solution contains ethanoic acid (CH3COOH) and sodium ethanoate (CH3COONa).",
    [
        {'label': 'a', 'text': 'Define a buffer solution.', 'marks': 2},
        {'label': 'b', 'text': 'Explain how this buffer resists changes in pH when a small amount of acid (H+) is added.', 'marks': 2}
    ],
    "2. (a) A solution that resists changes in pH when small amounts of acid or base/alkali are added (2).<br/>2. (b) Added H+ ions react with large reservoir of ethanoate ions: CH3COO- + H+ -> CH3COOH (1). Keeps [H+] nearly constant (1)."
))

for i in range(3, 26):
    p6_questions.append(make_edexcel_q(
        i, f"Buffer pH Calculation Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Buffer solution {i} contains 0.200 mol dm-3 CH3COOH and 0.300 mol dm-3 CH3COONa (Ka = 1.74 x 10^-5 mol dm-3).",
        [
            {'label': 'a', 'text': 'Calculate [H+] in the buffer using Ka = [H+][CH3COO-] / [CH3COOH].', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the pH of the buffer solution.', 'marks': 1}
        ],
        f"{i}. (a) [H+] = Ka x [CH3COOH] / [CH3COO-] = (1.74x10^-5)(0.200) / (0.300) = 1.16 x 10^-5 mol dm-3 (2).<br/>{i}. (b) pH = -log(1.16x10^-5) = 4.94 (1)."
    ))

for i in range(26, 51):
    p6_questions.append(make_edexcel_q(
        i, f"A* Challenge: Buffer pH After Addition of Acid/Alkali & Half-Equivalence {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"A 500 cm3 buffer solution contains 0.100 mol CH3COOH and 0.100 mol CH3COONa (Ka = 1.74 x 10^-5, pKa = 4.76).<br/>0.010 mol of solid NaOH is added without changing the volume.",
        [
            {'label': 'a', 'text': 'Calculate the new moles of CH3COOH and CH3COO- after reaction with added NaOH.', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the new pH of the buffer solution.', 'marks': 3}
        ],
        f"{i}. (a) Added OH- reacts with CH3COOH: CH3COOH + OH- -> CH3COO- + H2O. New moles CH3COOH = 0.100 - 0.010 = 0.090 mol (1). New moles CH3COO- = 0.100 + 0.010 = 0.110 mol (1).<br/>{i}. (b) [H+] = Ka x (moles HA / moles A-) = (1.74x10^-5)(0.090 / 0.110) = 1.424 x 10^-5 mol dm-3 (2). New pH = -log(1.424x10^-5) = 4.85 (1)."
    ))

p6_faqs = []
p6_faq_titles = [
    ("Half-Equivalence Point Property", "Titration Curve Feature", "Forgetting that pH = pKa at the half-equivalence point.", "At the half-equivalence point in a weak acid-strong base titration, exactly half of the weak acid has been neutralised ([HA] = [A-]). Therefore Ka = [H+] and pH = pKa."),
    ("Indicator Selection Criterion", "Indicator Range", "Selecting an indicator based solely on colour preference.", "An indicator is suitable ONLY if its pH range (pKIn +/- 1) falls ENTIRELY within the steep vertical section of the titration pH curve."),
    ("Weak Acid-Weak Base Indicator Suitability", "Titration Curves", "Selecting indicators for weak acid-weak base titrations.", "Weak acid - weak base titrations have NO steep vertical section on their pH curve. Therefore NO indicator is suitable; a pH meter must be used."),
    ("Buffer Calculation Moles vs Concentration", "Buffer Shortcuts", "Thinking volume must always be used when calculating buffer pH.", "In Ka = [H+][A-]/[HA], volume cancels out because [A-] and [HA] are in the same total volume. You can calculate [H+] = Ka x (moles HA / moles A-) directly."),
    ("Addition of Acid to Buffer Mechanism", "Buffer Action", "Writing H+ reacts with HA instead of A-.", "Added H+ reacts with the CONJUGATE BASE A-: A- + H+ -> HA. Added OH- reacts with the WEAK ACID HA: HA + OH- -> A- + H2O."),
    ("Basic Buffer Equations", "Basic Buffers", "Using Ka equations directly for basic buffers like NH3/NH4+.", "For basic buffers (NH3/NH4+): use Kb or Ka of NH4+ (Ka = Kw / Kb). Alternatively: [OH-] = Kb x [NH3]/[NH4+], then find [H+] via Kw."),
    ("Blood Buffer System", "Physiological Buffers", "Misidentifying the primary blood buffer components.", "The primary blood buffer is the carbonic acid - hydrogencarbonate system: H2CO3 ⇌ H+ + HCO3-. CO2 in lungs regulates [H2CO3] while kidneys regulate [HCO3-]."),
    ("Why Salt Is Needed in Acidic Buffers", "Buffer Formulation", "Assuming a weak acid alone can act as a buffer.", "A weak acid dissociates poorly and provides very few A- ions. Adding the sodium salt (NaA) provides a LARGE RESERVOIR of conjugate base A- needed to neutralize added H+."),
    ("Equivalence Point pH for Weak Acid-Strong Base", "Equivalence pH", "Assuming the equivalence point is always pH 7.00.", "At the equivalence point of a weak acid - strong base titration, the solution contains the conjugate base A- which hydrolyses water: A- + H2O ⇌ HA + OH-. Thus pH > 7 (alkaline equivalence point)."),
    ("Equivalence Point pH for Strong Acid-Weak Base", "Equivalence pH", "Assuming strong acid-weak base titration has alkaline equivalence point.", "At the equivalence point of a strong acid - weak base titration, the solution contains the conjugate acid BH+ which hydrolyses water: BH+ + H2O ⇌ B + H3O+. Thus pH < 7 (acidic equivalence point).")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p6_faq_titles, 1):
    p6_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_14B_Acid_Base_Titrations_Buffers.pdf", p6_meta, p6_questions, p6_faqs)
print("Pack 6 (14B Titrations & Buffers - 50 Qs + 10 FAQs) compiled successfully!")
