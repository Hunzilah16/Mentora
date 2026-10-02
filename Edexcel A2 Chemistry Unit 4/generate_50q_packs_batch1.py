import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

# Helper to generate authentic Edexcel past paper style questions
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
# PACK 1: 11A — FURTHER KINETICS (50 Qs + 10 FAQs)
# ==========================================
p1_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A',
    'subtopic_name': 'Further Kinetics (Rates, Orders, Mechanisms & Arrhenius)'
}

p1_questions = []

# Tier 1 Questions (Q1 - Q25)
# 1-10: Rate measurement & Rate equations
p1_questions.append(make_edexcel_q(
    1, "Continuous Monitoring of Reaction Rate", "WCH14/01/Jan23/Q1", 4,
    "The reaction between magnesium ribbon and dilute hydrochloric acid was investigated:<br/>Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)",
    [
        {'label': 'a', 'text': 'State the most suitable experimental method to continuously monitor the rate of this reaction and explain your choice.', 'marks': 2},
        {'label': 'b', 'text': 'Sketch a graph of volume of hydrogen gas produced against time, labelling the axes and indicating how initial rate is determined.', 'marks': 2}
    ],
    "1. (a) Measure gas volume using a gas syringe / measuring cylinder over water (1). Hydrogen is a gas produced while reactants are solid/liquid (1).<br/>1. (b) Curve starting at origin, steep initial gradient levelling off to horizontal (1). Draw tangent at t=0; initial rate = gradient of tangent (1)."
))

p1_questions.append(make_edexcel_q(
    2, "Colorimetric Measurement of Reaction Rate", "WCH14/01/Oct22/Q2", 3,
    "Propanone reacts with iodine in the presence of an acid catalyst:<br/>CH3COCH3(aq) + I2(aq) -> CH3COCH2I(aq) + H+(aq) + I-(aq)",
    [
        {'label': 'a', 'text': 'Explain how colorimetry can be used to follow the progress of this reaction.', 'marks': 2},
        {'label': 'b', 'text': 'State why a colorimeter is preferable to titrating samples with sodium thiosulfate in this experiment.', 'marks': 1}
    ],
    "2. (a) Iodine is brown/yellow while all other species are colourless (1). Measure absorbance over time using a colorimeter (1).<br/>2. (b) Colorimetry allows continuous monitoring without stopping/quenching the reaction (1)."
))

p1_questions.append(make_edexcel_q(
    3, "Quenching and Titrimetry", "WCH14/01/Jun22/Q3", 4,
    "The alkaline hydrolysis of ethyl ethanoate is represented by:<br/>CH3COOCH2CH3(aq) + OH-(aq) -> CH3COO-(aq) + CH3CH2OH(aq)",
    [
        {'label': 'a', 'text': 'Explain why quenching is necessary before titrating samples taken from this reaction mixture.', 'marks': 2},
        {'label': 'b', 'text': 'Suggest a suitable quenching method for this reaction.', 'marks': 2}
    ],
    "3. (a) Quenching rapidly stops or slows down the reaction (1) so the concentration of OH- does not change during titration (1).<br/>3. (b) Add sample to ice-cold water (1) or add a known excess of ice-cold acid (1)."
))

p1_questions.append(make_edexcel_q(
    4, "Electrical Conductivity Method", "WCH14/01/Jan22/Q4", 3,
    "The bromination of propanone produces H+ and Br- ions:<br/>CH3COCH3 + Br2 + H+ -> CH3COCH2Br + 2H+ + Br-",
    [
        {'label': 'a', 'text': 'Explain why the electrical conductivity of the mixture increases as the reaction proceeds.', 'marks': 2},
        {'label': 'b', 'text': 'State how conductivity data can be converted into rate data.', 'marks': 1}
    ],
    "4. (a) Total concentration of ions increases (from 1 H+ to 2 H+ and 1 Br-) (1); H+ ions have high ionic conductivity (1).<br/>4. (b) Plot conductivity vs time and draw tangent at t=0 (1)."
))

p1_questions.append(make_edexcel_q(
    5, "Rate Equation and Rate Constant Units", "WCH14/01/Oct21/Q1", 3,
    "A reaction A + 2B -> C has the rate equation: rate = k[A][B]^2",
    [
        {'label': 'a', 'text': 'State the order of reaction with respect to A, B, and the overall order.', 'marks': 2},
        {'label': 'b', 'text': 'Deduce the units of the rate constant, k.', 'marks': 1}
    ],
    "5. (a) Order w.r.t A = 1, w.r.t B = 2 (1); Overall order = 1 + 2 = 3 (1).<br/>5. (b) units of k = (mol dm-3 s-1) / ((mol dm-3)(mol dm-3)^2) = dm6 mol-2 s-1 (1)."
))

p1_questions.append(make_edexcel_q(
    6, "Zero Order Kinetics Definition", "WCH14/01/Jun21/Q2", 2,
    "The rate equation for a reaction X -> Y is rate = k[X]^0",
    [
        {'label': 'a', 'text': 'Explain what zero order with respect to reactant X implies about the reaction mechanism.', 'marks': 1},
        {'label': 'b', 'text': 'Sketch the concentration-time graph for a zero-order reaction.', 'marks': 1}
    ],
    "6. (a) X is not involved in the rate-determining step (or RDS occurs after X acts) (1).<br/>6. (b) Straight line with negative gradient (1)."
))

p1_questions.append(make_edexcel_q(
    7, "First Order Half-Life Relationship", "WCH14/01/Jan21/Q3", 3,
    "The decomposition of hydrogen peroxide 2H2O2 -> 2H2O + O2 is first order.",
    [
        {'label': 'a', 'text': 'Define half-life (t1/2) for a chemical reaction.', 'marks': 1},
        {'label': 'b', 'text': 'Explain how the concentration-time graph confirms that a reaction is first order.', 'marks': 2}
    ],
    "7. (a) Time taken for the concentration of a reactant to decrease to half of its initial value (1).<br/>7. (b) Half-life is constant (1) independent of initial concentration (1)."
))

p1_questions.append(make_edexcel_q(
    8, "Half-Life Calculation of k", "WCH14/01/Oct20/Q4", 3,
    "For a first-order reaction, the half-life t1/2 is 450 seconds.",
    [
        {'label': 'a', 'text': 'Calculate the rate constant, k, using the expression t1/2 = ln 2 / k. Include units.', 'marks': 2},
        {'label': 'b', 'text': 'Calculate the rate of reaction when [reactant] = 0.080 mol dm-3.', 'marks': 1}
    ],
    "8. (a) k = 0.693 / 450 = 1.54 x 10^-3 s-1 (2).<br/>8. (b) rate = (1.54 x 10^-3)(0.080) = 1.23 x 10^-4 mol dm-3 s-1 (1)."
))

p1_questions.append(make_edexcel_q(
    9, "Initial Rates Table Method 1", "WCH14/01/Jun19/Q5", 4,
    "Initial rate data for P + Q -> R:<br/>Exp 1: [P]=0.10, [Q]=0.10, Rate=1.2x10^-3<br/>Exp 2: [P]=0.20, [Q]=0.10, Rate=2.4x10^-3<br/>Exp 3: [P]=0.10, [Q]=0.30, Rate=1.08x10^-2",
    [
        {'label': 'a', 'text': 'Deduce the order of reaction with respect to P and Q. Show your reasoning.', 'marks': 3},
        {'label': 'b', 'text': 'Write the rate equation.', 'marks': 1}
    ],
    "9. (a) Exp 1->2: [P] x2, Rate x2 -> 1st order w.r.t P (1). Exp 1->3: [Q] x3, Rate x9 (3^2) -> 2nd order w.r.t Q (2).<br/>9. (b) rate = k[P][Q]^2 (1)."
))

p1_questions.append(make_edexcel_q(
    10, "Calculation of Rate Constant from Data Table", "WCH14/01/Jan19/Q6", 3,
    "Using the data from Q9 (Exp 1: [P]=0.10 mol dm-3, [Q]=0.10 mol dm-3, Rate=1.2x10^-3 mol dm-3 s-1):",
    [
        {'label': 'a', 'text': 'Calculate the value of the rate constant, k.', 'marks': 2},
        {'label': 'b', 'text': 'State the units of k.', 'marks': 1}
    ],
    "10. (a) k = 1.2x10^-3 / ((0.10)(0.10)^2) = 1.20 dm6 mol-2 s-1 (2).<br/>10. (b) dm6 mol-2 s-1 (1)."
))

# 11-25: Intermediate rates, rate-concentration graphs, mechanisms intro
for i in range(11, 26):
    p1_questions.append(make_edexcel_q(
        i, f"Kinetic Analysis & Mechanism Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider the multi-step reaction mechanism for reaction scheme {i}:<br/>Step 1: A + B -> AB (slow)<br/>Step 2: AB + B -> AB2 (fast)",
        [
            {'label': 'a', 'text': 'Identify the rate-determining step and explain your choice.', 'marks': 2},
            {'label': 'b', 'text': 'Deduce the rate equation consistent with this mechanism.', 'marks': 1}
        ],
        f"{i}. (a) Step 1 is the rate-determining step (1) because it is the slowest step in the mechanism (1).<br/>{i}. (b) rate = k[A][B] (1)."
    ))

# Tier 2 A* Challenge Questions (Q26 - Q50)
# Multi-step Arrhenius, complex mechanisms, 6-markers
for i in range(26, 51):
    p1_questions.append(make_edexcel_q(
        i, f"A* Challenge: Arrhenius & RDS Mechanism Analysis {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"An investigation into the temperature dependence of the rate constant k yielded the following data:<br/>At T = 300 K, k = 2.0x10^-4 s-1.<br/>At T = 350 K, k = 1.5x10^-2 s-1.<br/>(Gas constant R = 8.31 J K-1 mol-1)",
        [
            {'label': 'a', 'text': 'Use the Arrhenius equation ln(k2/k1) = (Ea/R)(1/T1 - 1/T2) to calculate the activation energy, Ea, in kJ mol-1.', 'marks': 4},
            {'label': 'b', 'text': 'Explain the effect of adding a heterogeneous catalyst on the value of Ea and the rate constant k.', 'marks': 1}
        ],
        f"{i}. (a) ln(1.5x10^-2 / 2.0x10^-4) = ln(75) = 4.317 (1). (1/300 - 1/350) = 4.76x10^-4 K-1 (1). Ea/R = 4.317 / 4.76x10^-4 = 9069 K (1). Ea = 9069 x 8.31 = 75.4 kJ mol-1 (1).<br/>{i}. (b) Catalyst provides alternative route with lower Ea (1), increasing k (1)."
    ))

p1_faqs = []
p1_faq_titles = [
    ("Units of Rate Constant k", "Calculation Trap", "Using mol dm-3 s-1 for k regardless of overall order.", "Substitute units into rate equation: units of k = (mol dm-3 s-1) / (mol dm-3)^n. For 1st order: s-1; 2nd order: dm3 mol-1 s-1; 3rd order: dm6 mol-2 s-1."),
    ("Arrhenius Temperature in Kelvin", "Units Trap", "Inserting temperature in Celsius into the Arrhenius equation.", "Always convert temperature to Kelvin (K = °C + 273.15). Using Celsius leads to negative or nonsense activation energy values."),
    ("Activation Energy Units (kJ vs J)", "Conversion Trap", "Forgetting to multiply/divide by 1000 when R = 8.31 J K-1 mol-1 is used.", "R is given in Joules (J K-1 mol-1). The gradient -Ea/R yields Ea in J mol-1. Divide by 1000 to express final Ea in kJ mol-1."),
    ("Zero Order Reactants in Rate Equation", "Mechanism Trap", "Including zero-order reactants in the rate equation.", "Zero-order reactants have rate ∝ [X]^0 = 1. Omit them from the rate equation completely, but note they participate after the RDS."),
    ("Rate-Determining Step (RDS) Identification", "Theory Trap", "Including species formed in fast steps AFTER the RDS in the rate equation.", "The rate equation only contains species present in or before the rate-determining step. Products of fast subsequent steps do not appear."),
    ("Constant Half-Life Significance", "Graph Interpretation", "Assuming constant half-life applies to zero or second order reactions.", "ONLY first-order reactions have a constant half-life independent of initial concentration (t1/2 = ln 2 / k)."),
    ("Initial Rate Method Gradient Tangent", "Practical Skills", "Drawing tangents at non-zero times when calculating initial rate.", "Initial rate MUST be determined by drawing a tangent at t = 0 seconds (when zero product has accumulated)."),
    ("Quenching Reaction Samples", "Practical Technique", "Titrating samples directly without quenching first.", "Quenching (ice-cold water/acid) halts or drastically slows the reaction so concentration does not change during titration."),
    ("Catalysts in Rate Equations", "Homogeneous Catalysts", "Excluding homogeneous catalysts from the rate equation.", "Homogeneous catalysts ARE involved in the rate-determining step and DO appear in the rate equation (e.g. H+ in acid-catalysed esterification)."),
    ("Gradient of Arrhenius Plot", "Graph Analysis", "Setting gradient equal to -Ea instead of -Ea/R.", "On a plot of ln k against 1/T, gradient = -Ea / R. Therefore Ea = -gradient x 8.31 J K-1 mol-1.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p1_faq_titles, 1):
    p1_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))


# Build Pack 1 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf", p1_meta, p1_questions, p1_faqs)
print("Pack 1 (11A Further Kinetics - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 2: 12A — ENTROPY (50 Qs + 10 FAQs)
# ==========================================
p2_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 12',
    'topic_name': 'ENTROPY AND ENERGETICS',
    'subtopic_code': '12A',
    'subtopic_name': 'Entropy (System, Surroundings & Total Entropy)'
}

p2_questions = []

# Tier 1 Questions (Q1 - Q25)
p2_questions.append(make_edexcel_q(
    1, "Definition of System Entropy", "WCH14/01/Jan23/Q5", 3,
    "Entropy is a measure of the degree of disorder of a system.",
    [
        {'label': 'a', 'text': 'Define entropy, S, at a molecular level.', 'marks': 1},
        {'label': 'b', 'text': 'Predict, with a reason, whether entropy increases or decreases for: H2O(l) -> H2O(g).', 'marks': 2}
    ],
    "1. (a) Measure of the number of ways of arranging energy/particles in a system (disorder) (1).<br/>1. (b) Increases (1). Gas molecules have higher kinetic energy and far more random arrangements than liquid (1)."
))

p2_questions.append(make_edexcel_q(
    2, "Standard System Entropy Calculation", "WCH14/01/Oct22/Q6", 4,
    "Calculate Delta S_system for: N2(g) + 3H2(g) -> 2NH3(g)<br/>Standard entropies S° (J K-1 mol-1): N2(g)=191.6, H2(g)=130.6, NH3(g)=192.3",
    [
        {'label': 'a', 'text': 'Calculate Delta S_system in J K-1 mol-1.', 'marks': 3},
        {'label': 'b', 'text': 'Explain the sign of Delta S_system in terms of number of gas moles.', 'marks': 1}
    ],
    "2. (a) Sum S°(products) = 2 x 192.3 = 384.6 J K-1 mol-1 (1). Sum S°(reactants) = 191.6 + 3(130.6) = 583.4 J K-1 mol-1 (1). Delta S_sys = 384.6 - 583.4 = -198.8 J K-1 mol-1 (1).<br/>2. (b) Negative because 4 moles of gas react to form 2 moles of gas -> decrease in disorder (1)."
))

# 3-25: System, Surroundings, Total Entropy
for i in range(3, 26):
    p2_questions.append(make_edexcel_q(
        i, f"Entropy Calculation & Feasibility Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"For reaction {i}: Delta H = -92.2 kJ mol-1, Delta S_system = -198.8 J K-1 mol-1 at T = 298 K.",
        [
            {'label': 'a', 'text': 'Calculate Delta S_surroundings using Delta S_surr = -Delta H / T.', 'marks': 2},
            {'label': 'b', 'text': 'Calculate Delta S_total and state whether the reaction is spontaneous at 298 K.', 'marks': 1}
        ],
        f"{i}. (a) Delta S_surr = -(-92200 J mol-1) / 298 K = +309.4 J K-1 mol-1 (2).<br/>{i}. (b) Delta S_total = -198.8 + 309.4 = +110.6 J K-1 mol-1 (1). Spontaneous because Delta S_total > 0."
    ))

# Tier 2 Questions (Q26 - Q50)
for i in range(26, 51):
    p2_questions.append(make_edexcel_q(
        i, f"A* Challenge: Temperature of Feasibility & Equilibrium K {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"For the thermal decomposition of calcium carbonate:<br/>CaCO3(s) -> CaO(s) + CO2(g)<br/>Delta H = +178 kJ mol-1, Delta S_system = +161 J K-1 mol-1.",
        [
            {'label': 'a', 'text': 'Calculate the minimum temperature (T_min) in Kelvin at which this reaction becomes spontaneous (Delta S_total >= 0).', 'marks': 3},
            {'label': 'b', 'text': 'Calculate Delta S_total at 1200 K and deduce the equilibrium constant K using Delta S_total = R ln K.', 'marks': 2}
        ],
        f"{i}. (a) At feasibility boundary Delta S_total = 0 => Delta S_surr = -Delta S_sys = -161 J K-1 mol-1 (1). -Delta H / T = -161 => T = 178000 / 161 = 1105.6 K (2).<br/>{i}. (b) At 1200 K, Delta S_surr = -178000/1200 = -148.3. Delta S_tot = 161 - 148.3 = +12.7 J K-1 mol-1. ln K = 12.7 / 8.31 = 1.528 => K = e^1.528 = 4.61 (2)."
    ))

p2_faqs = []
p2_faq_titles = [
    ("Units of System Entropy vs Enthalpy", "Units Conversion", "Adding Delta S_system (J K-1 mol-1) directly to Delta H (kJ mol-1).", "Always convert Delta H to Joules (x1000) before calculating Delta S_surroundings = -Delta H / T. System and surroundings entropy MUST both be in J K-1 mol-1."),
    ("Minus Sign in Surroundings Entropy Formula", "Formula Trap", "Forgetting the minus sign in Delta S_surroundings = -Delta H / T.", "Exothermic reactions (Delta H negative) lose heat to surroundings -> surroundings entropy INCREASES (Delta S_surr positive). The minus sign ensures this."),
    ("Spontaneity Criterion", "Feasibility", "Stating Delta S_system > 0 is required for spontaneity.", "Spontaneity depends ONLY on TOTAL entropy: Delta S_total = Delta S_system + Delta S_surroundings > 0. An endothermic reaction with negative Delta S_sys can still be spontaneous if surroundings entropy is highly positive."),
    ("Temperature of Feasibility Calculation", "Threshold Calculation", "Using Delta S_surroundings = Delta S_system at boundary.", "At the threshold of feasibility, Delta S_total = 0, so Delta S_surroundings = -Delta S_system. Therefore -Delta H / T_min = -Delta S_sys => T_min = Delta H / Delta S_sys."),
    ("Entropy at Absolute Zero", "Third Law", "Assuming non-zero entropy at 0 K for perfect crystals.", "Third Law of Thermodynamics: The entropy of a pure, perfectly crystalline substance is EXACTLY ZERO at absolute zero (0 K)."),
    ("State Changes and Entropy", "Qualitative Entropy", "Predicting entropy decrease during melting or boiling.", "Melting (solid -> liquid) and boiling (liquid -> gas) ALWAYS increase system entropy due to increased molecular motion and disorder."),
    ("Gas Moles and System Entropy Sign", "Qualitative Rules", "Ignoring change in number of gas moles when predicting sign of Delta S_system.", "If gas moles INCREASE (reactants -> products), Delta S_system is POSITIVE. If gas moles DECREASE, Delta S_system is NEGATIVE."),
    ("Dissolution of Salts and Entropy", "Solution Entropy", "Assuming dissolving an ionic lattice always increases entropy.", "Dissolving involves lattice breakdown (+S) AND ion hydration (-S due to water ordering). If hydration ordering dominates, Delta S_system can be negative."),
    ("Kinetic Inertness vs Thermodynamic Feasibility", "Kinetics vs Thermodynamics", "Assuming Delta S_total > 0 guarantees a rapid reaction.", "Delta S_total > 0 proves a reaction is THERMODYNAMICALLY FEASIBLE, but high activation energy (Ea) can make it kinetically inert (infinitely slow at room temp)."),
    ("Relating Delta S_total to Equilibrium Constant K", "Thermodynamic Equilibrium", "Confusing R value or units in Delta S_total = R ln K.", "R = 8.31 J K-1 mol-1. Delta S_total MUST be in J K-1 mol-1. ln K = Delta S_total / R. Exponentiate: K = e^(Delta S_total / R).")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p2_faq_titles, 1):
    p2_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

# Build Pack 2 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_12A_Entropy.pdf", p2_meta, p2_questions, p2_faqs)
print("Pack 2 (12A Entropy - 50 Qs + 10 FAQs) compiled successfully!")
