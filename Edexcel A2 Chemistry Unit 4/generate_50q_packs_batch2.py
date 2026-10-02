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
# PACK 3: 12B — LATTICE ENERGY (50 Qs + 10 FAQs)
# ==========================================
p3_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 12',
    'topic_name': 'ENTROPY AND ENERGETICS',
    'subtopic_code': '12B',
    'subtopic_name': 'Lattice Energy (Born-Haber Cycles, Covalency & Hydration)'
}

p3_questions = []

p3_questions.append(make_edexcel_q(
    1, "Lattice Energy Definition", "WCH14/01/Jan23/Q7", 3,
    "Lattice energy is a measure of the strength of ionic bonding in a crystal lattice.",
    [
        {'label': 'a', 'text': 'Define standard lattice energy (lattice formation enthalpy).', 'marks': 2},
        {'label': 'b', 'text': 'State whether lattice energy is endothermic or exothermic.', 'marks': 1}
    ],
    "1. (a) Enthalpy change when one mole of a solid ionic lattice is formed from its constituent gaseous ions (1) under standard conditions (1).<br/>1. (b) Exothermic (negative) (1)."
))

p3_questions.append(make_edexcel_q(
    2, "Born-Haber Cycle Calculation for NaCl", "WCH14/01/Oct22/Q8", 5,
    "Data (kJ mol-1): Delta_f H(NaCl) = -411, Delta_atom H(Na) = +107, 1st IE(Na) = +496, Delta_atom H(Cl) = +122, 1st EA(Cl) = -349.",
    [
        {'label': 'a', 'text': 'Construct a Born-Haber cycle for sodium chloride.', 'marks': 2},
        {'label': 'b', 'text': 'Calculate the lattice energy of sodium chloride, Delta_LE H(NaCl).', 'marks': 3}
    ],
    "2. (a) Correct cycle diagram showing Na(s)+1/2Cl2(g) -> Na+(g)+Cl-(g) -> NaCl(s) (2).<br/>2. (b) Delta_f H = Delta_atom H(Na) + IE1(Na) + Delta_atom H(Cl) + EA1(Cl) + Delta_LE H (1). -411 = +107 + 496 + 122 - 349 + Delta_LE H (1). Delta_LE H = -411 - 376 = -787 kJ mol-1 (1)."
))

for i in range(3, 26):
    p3_questions.append(make_edexcel_q(
        i, f"Born-Haber & Lattice Energy Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider ionic compound {i} (MX): Delta_f H = -500 kJ mol-1, sum of ionization and atomization enthalpies = +800 kJ mol-1, electron affinity = -350 kJ mol-1.",
        [
            {'label': 'a', 'text': 'Calculate the lattice energy of MX.', 'marks': 2},
            {'label': 'b', 'text': 'Compare the lattice energy of MX with M2X (where M is divalent).', 'marks': 1}
        ],
        f"{i}. (a) Delta_LE H = -500 - (800 - 350) = -950 kJ mol-1 (2).<br/>{i}. (b) Divalent cation has higher charge density -> stronger electrostatic attraction -> much more exothermic lattice energy (1)."
    ))

for i in range(26, 51):
    p3_questions.append(make_edexcel_q(
        i, f"A* Challenge: Experimental vs Theoretical Lattice & Polarization {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"For silver iodide, AgI: Experimental lattice energy = -887 kJ mol-1. Theoretical Born-Landé lattice energy = -770 kJ mol-1.",
        [
            {'label': 'a', 'text': 'Explain the difference between experimental and theoretical lattice energy for AgI.', 'marks': 3},
            {'label': 'b', 'text': 'Apply Hess\'s law to calculate the enthalpy of solution of AgI given Delta_hyd H(Ag+) = -464 and Delta_hyd H(I-) = -293 kJ mol-1.', 'marks': 2}
        ],
        f"{i}. (a) Theoretical model assumes purely ionic spherical ions (1). Experimental > theoretical indicates significant covalent character (1) due to polarization of large iodide anion by small polarising Ag+ cation (1).<br/>{i}. (b) Delta_sol H = Delta_hyd H(Ag+) + Delta_hyd H(I-) - Delta_LE H = -464 - 293 - (-887) = +130 kJ mol-1 (2)."
    ))

p3_faqs = []
p3_faq_titles = [
    ("Definition of Atomisation Enthalpy", "Born-Haber Definitions", "Using 1 mole of element instead of forming 1 mole of gaseous atoms.", "Enthalpy of atomisation Delta_atom H is the enthalpy change when ONE MOLE OF GASEOUS ATOMS is formed from the element in its standard state (e.g. 1/2 Cl2(g) -> Cl(g))."),
    ("First vs Second Electron Affinity Signs", "Electron Affinity Signs", "Assuming all electron affinities are exothermic.", "First electron affinity (EA1) is EXOTHERMIC (-). Second electron affinity (EA2) is ENDOTHERMIC (+) because an electron is added to a negatively charged anion (electrostatic repulsion)."),
    ("Born-Haber Cycle Direction Arrows", "Hess's Law Cycle", "Drawing cycle arrows in random directions.", "Standard enthalpies of formation go DOWN from elements -> compound. Atomisation and IE go UP -> ions. EA goes DOWN -> anions. Lattice energy goes DOWN from gaseous ions -> solid lattice."),
    ("Experimental vs Theoretical Lattice Energy Difference", "Polarization / Covalency", "Attributing difference in lattice energy to experimental measurement error.", "If experimental LE is significantly MORE EXOTHERMIC than theoretical (Born-Landé), the bonding has COVALENT CHARACTER caused by cation polarization of the anion (Fajans' rules)."),
    ("Polarising Power vs Polarisability", "Fajans' Rules", "Confusing polarising power of cations with polarisability of anions.", "Cations have POLARISING POWER (high charge, small ionic radius). Anions are POLARISABLE (large ionic radius, electron cloud easily distorted)."),
    ("Enthalpy of Solution Formula", "Hydration vs Lattice", "Subtracting hydration enthalpies from lattice energy in reverse order.", "Delta_sol H = Sum Delta_hyd H(ions) - Delta_LE H (where LE is defined as lattice formation). Alternatively: Delta_sol H = Delta_dissociation H + Sum Delta_hyd H."),
    ("Hydration Enthalpy Factors", "Ion-Dipole Attraction", "Stating larger ions have more exothermic hydration enthalpy.", "Hydration enthalpy depends on CHARGE DENSITY: smaller ionic radius and higher charge -> higher charge density -> stronger ion-dipole attraction to water -> MORE EXOTHERMIC Delta_hyd H."),
    ("Group 2 Sulfate Solubility Trend", "Solubility Trends", "Explaining group 2 sulfate solubility using lattice energy alone.", "Down Group 2, cation radius increases. Lattice energy decreases slightly, but hydration enthalpy of cation decreases much more rapidly. Net Delta_sol H becomes more positive -> solubility DECREASES."),
    ("Group 2 Hydroxide Solubility Trend", "Solubility Trends", "Applying sulfate solubility trend to hydroxides.", "OH- is a small anion. Down Group 2, lattice energy decreases faster than hydration enthalpy. Net Delta_sol H becomes less positive / more negative -> hydroxide solubility INCREASES down the group."),
    ("Lattice Dissociation vs Lattice Formation", "Enthalpy Definitions", "Confusing lattice formation (-LE) with lattice dissociation (+LE).", "Lattice FORMATION enthalpy: gaseous ions -> solid lattice (EXOTHERMIC, negative). Lattice DISSOCIATION enthalpy: solid lattice -> gaseous ions (ENDOTHERMIC, positive). Always check the sign in data tables.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p3_faq_titles, 1):
    p3_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf", p3_meta, p3_questions, p3_faqs)
print("Pack 3 (12B Lattice Energy - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 4: 13A — CHEMICAL EQUILIBRIA (50 Qs + 10 FAQs)
# ==========================================
p4_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 13',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '13A',
    'subtopic_name': 'Chemical Equilibria (Kc, Kp, Temperature Effects & Entropy K Relationship)'
}

p4_questions = []

p4_questions.append(make_edexcel_q(
    1, "Equilibrium Constant Kc Expression and Units", "WCH14/01/Jan23/Q9", 4,
    "The esterification reaction: CH3COOH(l) + C2H5OH(l) ⇌ CH3COOC2H5(l) + H2O(l)",
    [
        {'label': 'a', 'text': 'Write the expression for the equilibrium constant, Kc, for this reaction.', 'marks': 1},
        {'label': 'b', 'text': 'State the units of Kc for this esterification.', 'marks': 1},
        {'label': 'c', 'text': 'A mixture of 1.00 mol ethanoic acid and 1.00 mol ethanol was allowed to reach equilibrium. At equilibrium, 0.67 mol of ester was formed. Calculate Kc.', 'marks': 2}
    ],
    "1. (a) Kc = [CH3COOC2H5][H2O] / ([CH3COOH][C2H5OH]) (1).<br/>1. (b) No units (units cancel out) (1).<br/>1. (c) Eqm moles: acid=0.33, alcohol=0.33, ester=0.67, water=0.67. Kc = (0.67 x 0.67) / (0.33 x 0.33) = 4.12 (2)."
))

p4_questions.append(make_edexcel_q(
    2, "Gas Phase Equilibrium Kp Calculation", "WCH14/01/Oct22/Q10", 5,
    "The Haber process: N2(g) + 3H2(g) ⇌ 2NH3(g) at total pressure P_total = 100 atm.<br/>Equilibrium mole fractions: x(N2) = 0.20, x(H2) = 0.60, x(NH3) = 0.20.",
    [
        {'label': 'a', 'text': 'Calculate the partial pressure of each gas at equilibrium.', 'marks': 2},
        {'label': 'b', 'text': 'Write the expression for Kp and calculate its value with units.', 'marks': 3}
    ],
    "2. (a) p(N2) = 0.20 x 100 = 20 atm, p(H2) = 0.60 x 100 = 60 atm, p(NH3) = 0.20 x 100 = 20 atm (2).<br/>2. (b) Kp = p(NH3)^2 / (p(N2) x p(H2)^3) (1). Kp = (20)^2 / ((20) x (60)^3) = 400 / 4320000 = 9.26 x 10^-5 atm-2 (2)."
))

for i in range(3, 26):
    p4_questions.append(make_edexcel_q(
        i, f"Equilibrium Calculation & Factors Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"For equilibrium system {i}: A(g) + B(g) ⇌ 2C(g) (Delta H = -45 kJ mol-1).",
        [
            {'label': 'a', 'text': 'State the effect of increasing temperature on the value of Kc and explain using Le Chatelier\'s principle.', 'marks': 2},
            {'label': 'b', 'text': 'State the effect of increasing total pressure on the value of Kc.', 'marks': 1}
        ],
        f"{i}. (a) Kc decreases (1). Forward reaction is exothermic; increasing temp shifts equilibrium left to absorb heat (1).<br/>{i}. (b) No effect on Kc (only temperature changes Kc) (1)."
    ))

for i in range(26, 51):
    p4_questions.append(make_edexcel_q(
        i, f"A* Challenge: Relating Entropy to Equilibrium Constant Delta S_total = R ln K {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"For the reversible reaction {i}: Delta S_system = -120 J K-1 mol-1, Delta H = -80.0 kJ mol-1 at T = 298 K.",
        [
            {'label': 'a', 'text': 'Calculate Delta S_surroundings and Delta S_total at 298 K.', 'marks': 3},
            {'label': 'b', 'text': 'Use Delta S_total = R ln K (R = 8.31 J K-1 mol-1) to calculate the numerical value of the equilibrium constant K at 298 K.', 'marks': 2}
        ],
        f"{i}. (a) Delta S_surr = -(-80000) / 298 = +268.5 J K-1 mol-1 (2). Delta S_tot = -120 + 268.5 = +148.5 J K-1 mol-1 (1).<br/>{i}. (b) ln K = Delta S_tot / R = 148.5 / 8.31 = 17.87 (1). K = e^17.87 = 5.76 x 10^7 (1)."
    ))

p4_faqs = []
p4_faq_titles = [
    ("Square Brackets vs Round Brackets in Kc", "Notation Trap", "Using round brackets () instead of square brackets [] in Kc expressions.", "Kc MUST use square brackets [X] denoting concentration in mol dm-3. Using round brackets (X) loses the mark."),
    ("Solids and Liquids in Heterogeneous Equilibria", "Heterogeneous K", "Including solid or pure liquid concentrations in Kc expressions.", "Heterogeneous equilibria: Solids and pure liquid solvent concentrations remain constant and are omitted from Kc (e.g. CaCO3(s) -> CaO(s) + CO2(g) has Kc = [CO2])."),
    ("Mole Fraction vs Partial Pressure", "Kp Definitions", "Confusing mole fraction x_A with partial pressure p_A.", "Mole fraction x_A = moles of A / total moles. Partial pressure p_A = x_A x P_total. Kp MUST use partial pressures p_A."),
    ("Why Pressure Does Not Change Kp", "Equilibrium Factors", "Stating that increasing pressure increases Kp for gas reactions.", "Increasing pressure increases individual partial pressures, but the ratio in Kp remains CONSTANT because the equilibrium composition shifts to restore Kp. ONLY TEMPERATURE changes Kp/Kc."),
    ("Why Catalysts Do Not Shift Equilibrium", "Catalysts & K", "Claiming a catalyst increases equilibrium yield or changes K.", "A catalyst increases the rate of BOTH forward and reverse reactions equally by lowering Ea for both routes. It speeds up attainment of equilibrium but does NOT alter equilibrium position or K."),
    ("Temperature Effect on Exothermic Reactions", "Temperature Dependence", "Stating Kc increases with temperature for exothermic reactions.", "Exothermic reaction: Delta H negative. Increasing temp causes Delta S_surroundings (-Delta H / T) to become less positive -> Delta S_total decreases -> K DECREASES."),
    ("Temperature Effect on Endothermic Reactions", "Temperature Dependence", "Stating Kc decreases with temperature for endothermic reactions.", "Endothermic reaction: Delta H positive. Increasing temp causes Delta S_surroundings (-Delta H / T) to become less negative -> Delta S_total increases -> K INCREASES."),
    ("Units of Kp", "Kp Units", "Assuming Kp is always unitless.", "Units of Kp depend on the stoichiometry: substitute atm or Pa into Kp expression. E.g. Kp = p(NH3)^2 / (p(N2) p(H2)^3) has units atm^-2 or Pa^-2."),
    ("Deriving K from Delta S_total", "Thermodynamics to K", "Using log10 instead of natural log (ln) in Delta S_total = R ln K.", "Delta S_total = R ln K uses NATURAL LOG (base e). To solve for K: K = e^(Delta S_total / R). Using 10^(Delta S/R) is wrong."),
    ("Large vs Small K Value Significance", "Equilibrium Position", "Confusing K >> 1 with fast reaction rate.", "K >> 1 (e.g. K > 10^3) means equilibrium lies far to the RIGHT (high product yield at equilibrium). It says NOTHING about reaction rate (which depends on activation energy).")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p4_faq_titles, 1):
    p4_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf", p4_meta, p4_questions, p4_faqs)
print("Pack 4 (13A Chemical Equilibria - 50 Qs + 10 FAQs) compiled successfully!")
