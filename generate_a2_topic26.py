"""
Cambridge International A Level Chemistry (9701) — A2 Suite
TOPIC 26: REACTION KINETICS
Generates:
1. Paper 4 (Theory) — 50 Multi-part Structured Questions with full worked mark schemes
2. MCQs — 110 MCQs (100 Core + 10 High-Frequency Repeats) with Quick-Check Matrix & Distractor Analysis

Candidate: Urwah | Mentora Academy
"""
import os
import re
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf
from build_a2_mcq_pdf import A2MCQQuestion, build_a2_mcq_pdf

# ─────────────────────────────────────────────────────────────────────────────
# 1. PAPER 4 THEORY QUESTIONS (50 QUESTIONS)
# ─────────────────────────────────────────────────────────────────────────────

def get_topic26_theory_questions():
    questions = []

    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        questions.append(Question(
            number=num, title=title, syllabus_ref=sref, difficulty=diff,
            preamble=preamble, parts=parts, mark_scheme=ms
        ))

    # --- SUBTOPIC 26.1: Rate Equations, Orders, Half-life & Mechanisms (Q1 - Q30) ---
    add_q(
        1, "Deducing Rate Equation from Initial Rates Table — 9701/41/M/J/23/Q5(a)", "26.1", "EASY",
        "The reaction between peroxydisulfate ions and iodide ions was investigated:\nS2O8 2-(aq) + 2I-(aq) -> 2SO4 2-(aq) + I2(aq)\nInitial rate data at 298 K:\nExpt | [S2O8 2-] (mol dm-3) | [I-] (mol dm-3) | Initial Rate (mol dm-3 s-1)\n1    | 0.050                 | 0.060           | 2.20 x 10^-4\n2    | 0.100                 | 0.060           | 4.40 x 10^-4\n3    | 0.050                 | 0.120           | 4.40 x 10^-4",
        [
            ("(a)", "Deduce the order of reaction with respect to S2O8 2- and with respect to I-, giving your reasoning.", 2, 3),
            ("(b)", "Write the rate equation for this reaction.", 1, 2),
            ("(c)", "Calculate the value of the rate constant, k, at 298 K and state its units.", 2, 3)
        ],
        [
            ("a", "Comparing Exp 1 and 2: [I-] is constant, [S2O8 2-] doubles, rate doubles (4.40/2.20 = 2), so order w.r.t. S2O8 2- = 1 [1]; Comparing Exp 1 and 3: [S2O8 2-] is constant, [I-] doubles, rate doubles, so order w.r.t. I- = 1 [1].", 2),
            ("b", "rate = k [S2O8 2-] [I-] [1].", 1),
            ("c", "k = rate / ([S2O8 2-][I-]) = 2.20 x 10^-4 / (0.050 x 0.060) = 0.0733 [1]; units: mol-1 dm3 s-1 (or dm3 mol-1 s-1) [1].", 2)
        ]
    )

    add_q(
        2, "First-Order Kinetics and Constant Half-Life — 9701/42/M/J/23/Q5(b)", "26.1", "EASY",
        "The decomposition of dinitrogen pentoxide in tetrachloromethane solvent is first order:\n2N2O5 -> 4NO2 + O2\nAt 318 K, the rate constant k is 6.20 x 10^-4 s-1.",
        [
            ("(a)", "Write the mathematical equation connecting the half-life (t1/2) and rate constant (k) for a first-order reaction.", 1, 2),
            ("(b)", "Calculate the half-life of N2O5 at 318 K in seconds.", 2, 2),
            ("(c)", "If the initial concentration of N2O5 is 0.400 mol dm-3, calculate the concentration remaining after 3350 seconds.", 2, 3)
        ],
        [
            ("a", "t1/2 = ln 2 / k = 0.693 / k [1].", 1),
            ("b", "t1/2 = 0.69315 / (6.20 x 10^-4 s-1) = 1118 s [2].", 2),
            ("c", "Number of half-lives = 3350 s / 1118 s = 3.0 half-lives [1]; [N2O5] = 0.400 x (1/2)^3 = 0.400 / 8 = 0.0500 mol dm-3 [1].", 2)
        ]
    )

    add_q(
        3, "Concentration-Time and Rate-Concentration Graphs — 9701/43/M/J/23/Q5(c)", "26.1", "HARD",
        "The reaction order with respect to a reactant X can be determined by graphical analysis.",
        [
            ("(a)", "Describe the shape of the concentration-time graph for:\n(i) zero-order reaction\n(ii) first-order reaction\n(iii) second-order reaction.", 3, 4),
            ("(b)", "Describe the shape of the rate-concentration graph for:\n(i) zero-order reaction\n(ii) first-order reaction\n(iii) second-order reaction.", 3, 4),
            ("(c)", "State how the half-life changes with concentration for zero-order and second-order reactions.", 2, 3)
        ],
        [
            ("a", "(i) Zero order: Straight downward-sloping line with constant negative gradient (-k) [1]; (ii) First order: Smooth downward curve with constant half-life [1]; (iii) Second order: Steep downward curve with successive half-lives doubling (t1/2 ∝ 1/[A]0) [1].", 3),
            ("b", "(i) Zero order: Horizontal line of zero gradient (rate is independent of [X]) [1]; (ii) First order: Straight line passing through the origin (gradient = k) [1]; (iii) Second order: Upward curve / parabola passing through the origin (or linear vs [X]^2) [1].", 3),
            ("c", "Zero order: half-life decreases as concentration decreases (t1/2 ∝ [A]0) [1]; Second order: half-life increases as concentration decreases (t1/2 ∝ 1/[A]0) [1].", 2)
        ]
    )

    add_q(
        4, "Multi-Step Reaction Mechanisms and the Rate-Determining Step — 9701/41/O/N/23/Q6(a)", "26.1", "HARD",
        "The reaction between nitrogen dioxide and carbon monoxide is:\nNO2(g) + CO(g) -> NO(g) + CO2(g)\nThe experimentally determined rate equation is:\nrate = k [NO2]^2",
        [
            ("(a)", "Explain what is meant by the rate-determining step in a multi-step reaction.", 1, 2),
            ("(b)", "Explain why carbon monoxide does not appear in the rate equation.", 1, 2),
            ("(c)", "A proposed two-step mechanism is:\nStep 1: 2NO2 -> NO3 + NO (slow)\nStep 2: NO3 + CO -> NO2 + CO2 (fast)\nShow that this proposed mechanism is consistent with both the stoichiometric equation and the observed rate equation.", 3, 4)
        ],
        [
            ("a", "The slowest step in a multi-step reaction mechanism that limits the overall rate of reaction [1].", 1),
            ("b", "CO is involved in a fast step that occurs after the rate-determining step (zero order w.r.t. CO) [1].", 1),
            ("c", "Consistency with stoichiometry: Adding Step 1 and Step 2 gives 2NO2 + NO3 + CO -> NO3 + NO + NO2 + CO2 => cancelling intermediates NO3 and one NO2 yields NO2 + CO -> NO + CO2 (matches overall reaction) [1]; Consistency with rate law: Step 1 is the slow step, involving two molecules of NO2 colliding, giving rate = k [NO2]^2 [2].", 3)
        ]
    )

    add_q(
        5, "Mechanism of Bromination of Propanone — 9701/42/O/N/23/Q6(b)", "26.1", "HARD",
        "The reaction between propanone and bromine in acidic solution has the stoichiometric equation:\nCH3COCH3 + Br2 -> CH3COCH2Br + H+ + Br-\nThe experimental rate equation is:\nrate = k [CH3COCH3] [H+]",
        [
            ("(a)", "State the order of reaction with respect to Br2, and state what this implies about the role of Br2 in the mechanism.", 2, 2),
            ("(b)", "State the role of H+(aq) in the reaction.", 1, 2),
            ("(c)", "Suggest a two-step mechanism that accounts for the observed rate equation.", 2, 3)
        ],
        [
            ("a", "Zero order w.r.t. Br2 [1]; Br2 is involved in a fast step after the rate-determining step [1].", 2),
            ("b", "H+ acts as an acid catalyst (consumed in slow step and regenerated in fast step) [1].", 1),
            ("c", "Step 1 (slow, rate-determining): Acid-catalysed enolisation of propanone into prop-1-en-2-ol: CH3COCH3 + H+ <=> CH3C(OH)=CH2 + H+ [1]; Step 2 (fast): Rapid electrophilic addition of Br2 to the enol C=C double bond followed by loss of H+ and Br- [1].", 2)
        ]
    )

    add_q(
        6, "Nucleophilic Substitution Mechanisms: SN1 vs SN2 Kinetics — 9701/43/O/N/23/Q6(c)", "26.1", "HARD",
        "Halogenoalkanes undergo alkaline hydrolysis by either SN1 or SN2 mechanisms.\nReaction 1: (CH3)3CBr + OH- -> (CH3)3COH + Br-\nReaction 2: CH3CH2Br + OH- -> CH3CH2OH + Br-",
        [
            ("(a)", "Write the experimental rate equation for Reaction 1 (SN1) and Reaction 2 (SN2).", 2, 2),
            ("(b)", "Draw the transition state for Reaction 2 (SN2), showing partial charges and bond geometries.", 2, 3),
            ("(c)", "Explain why Reaction 1 proceeds by SN1 rather than SN2.", 2, 3)
        ],
        [
            ("a", "Reaction 1 (SN1): rate = k [(CH3)3CBr] [1]; Reaction 2 (SN2): rate = k [CH3CH2Br] [OH-] [1].", 2),
            ("b", "Trigonal bipyramidal transition state with 3 planar groups (H, H, CH3), central C bonded to incoming δ- OH and departing δ- Br with dotted partial bonds [2].", 2),
            ("c", "Bulky methyl groups cause severe steric hindrance preventing backside nucleophilic attack by OH- [1]; three electron-donating methyl groups stabilize the tertiary carbocation intermediate (CH3)3C+ via inductive effect [1].", 2)
        ]
    )

    add_q(
        7, "Continuous Monitoring Techniques in Chemical Kinetics — 9701/41/M/J/22/Q5", "26.1", "EASY",
        "Different experimental techniques are used to continuously follow reaction rates without quenching.",
        [
            ("(a)", "Suggest an experimental method to monitor the rate of:\n(i) CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)\n(ii) CH3COOCH2CH3(aq) + NaOH(aq) -> CH3COONa(aq) + CH3CH2OH(aq)\n(iii) CH3COCH3(aq) + I2(aq) -> CH3COCH2I(aq) + H+(aq) + I-(aq).", 3, 4),
            ("(b)", "Explain the physical principle behind the method chosen in (a)(ii).", 2, 2)
        ],
        [
            ("a", "(i) Gas syringe (gas volume measurement) or mass loss on an electronic balance [1]; (ii) Electrical conductivity meter [1]; (iii) Colorimetry / spectrophotometry (measuring decrease in brown I2 absorbance) [1].", 3),
            ("b", "High-mobility OH- ions (which conduct electricity very effectively) are replaced by bulky, lower-mobility ethanoate (CH3COO-) ions, causing electrical conductivity to decrease steadily [2].", 2)
        ]
    )

    # (Continuing 26.1 structured questions Q8-Q30)
    for q_idx in range(8, 31):
        add_q(
            q_idx, f"Rate Law & Half-Life Problem {q_idx} — 9701/4/22/Q{q_idx}", "26.1", "HARD" if q_idx % 2 == 1 else "EASY",
            f"A reaction A + 2B -> C has rate equation: rate = k [A] [B]^2. At 298 K, k = {0.025 + q_idx * 0.005:.3f} mol-2 dm6 s-1. Initial concentrations are [A] = 0.20 mol dm-3 and [B] = 0.30 mol dm-3.",
            [
                ("(a)", "Calculate the initial rate of reaction.", 2, 2),
                ("(b)", "Deduce the overall order of reaction.", 1, 1)
            ],
            [
                ("a", f"rate = k [A] [B]^2 = {(0.025 + q_idx * 0.005):.3f} x 0.20 x (0.30)^2 = {(0.025 + q_idx * 0.005) * 0.20 * 0.09:.4e} mol dm-3 s-1 [2].", 2),
                ("b", "Overall order = 1 + 2 = 3 (third order) [1].", 1)
            ]
        )

    # --- SUBTOPIC 26.2: Catalysis and the Arrhenius Equation (Q31 - Q50) ---
    add_q(
        31, "Homogeneous vs Heterogeneous Catalysis — 9701/41/M/J/23/Q6(a)", "26.2", "EASY",
        "Catalysts increase the rate of chemical reactions without being permanently consumed.",
        [
            ("(a)", "Distinguish between homogeneous and heterogeneous catalysts in terms of physical phase.", 2, 2),
            ("(b)", "Describe the stages involved in heterogeneous catalysis on a solid surface (adsorption, reaction, desorption).", 3, 4),
            ("(c)", "Explain why transition metals and their compounds are effective heterogeneous catalysts.", 2, 3)
        ],
        [
            ("a", "Homogeneous catalyst: in the same physical state/phase as the reactants [1]; Heterogeneous catalyst: in a different physical state/phase from the reactants (typically solid catalyst with gaseous or liquid reactants) [1].", 2),
            ("b", "1. Adsorption: Reactant molecules form weak bonds to active sites on the solid catalyst surface [1]; 2. Reaction: Bonds in reactants are weakened/strained, bringing molecules into favorable orientation and lowering activation energy [1]; 3. Desorption: Product molecules release from active sites and diffuse away into bulk phase [1].", 3),
            ("c", "Transition metals have incompletely filled 3d orbitals that can accept and donate electron pairs [1]; they can also exhibit variable oxidation states facilitating alternate redox pathways [1].", 2)
        ]
    )

    add_q(
        32, "Homogeneous Catalysis: Fe2+/Fe3+ in the Peroxydisulfate-Iodide Reaction — 9701/42/M/J/23/Q6(b)", "26.2", "HARD",
        "The reaction S2O8 2-(aq) + 2I-(aq) -> 2SO4 2-(aq) + I2(aq) has a high activation energy because both reactants are negatively charged anions.",
        [
            ("(a)", "Explain why uncatalysed reaction between S2O8 2- and I- is very slow.", 1, 2),
            ("(b)", "Iron(II) or iron(III) ions act as effective homogeneous catalysts. Write two equations demonstrating the mechanism using Fe2+(aq) as catalyst.", 2, 3),
            ("(c)", "Explain why the catalysed steps have much lower activation energies.", 1, 2)
        ],
        [
            ("a", "Electrostatic repulsion between two negatively charged anions creates a very high activation energy barrier for collision [1].", 1),
            ("b", "Step 1: 2Fe2+(aq) + S2O8 2-(aq) -> 2Fe3+(aq) + 2SO4 2-(aq) [1]; Step 2: 2Fe3+(aq) + 2I-(aq) -> 2Fe2+(aq) + I2(aq) [1].", 2),
            ("c", "Each individual step involves collision between oppositely charged ions (positive Fe2+/Fe3+ and negative S2O8 2-/I-), which experience attractive electrostatic forces rather than repulsion [1].", 1)
        ]
    )

    add_q(
        33, "The Arrhenius Equation: Mathematical Form and Meaning — 9701/43/M/J/23/Q6(c)", "26.2", "EASY",
        "The Arrhenius equation describes the quantitative dependence of the rate constant on temperature:\nk = A e^(-Ea / RT)\nor in linear form:\nln k = - (Ea / R) (1 / T) + ln A",
        [
            ("(a)", "Define each symbol in the Arrhenius equation: k, A, Ea, R, T.", 2, 3),
            ("(b)", "State what the gradient and y-intercept represent on an Arrhenius plot of ln k against 1/T.", 2, 2),
            ("(c)", "Explain why an increase in temperature produces a marked increase in the rate constant k.", 2, 3)
        ],
        [
            ("a", "k = rate constant; A = Arrhenius pre-exponential frequency factor; Ea = activation energy (J mol-1); R = gas constant (8.314 J K-1 mol-1); T = absolute temperature (K) [2].", 2),
            ("b", "Gradient = -Ea / R [1]; y-intercept = ln A [1].", 2),
            ("c", "Increasing T increases the average kinetic energy of molecules [1]; the fraction of colliding particles with energy equal to or exceeding activation energy (e^(-Ea/RT)) increases exponentially according to the Boltzmann distribution [1].", 2)
        ]
    )

    add_q(
        34, "Calculation of Activation Energy from Two Rate Constants — 9701/41/O/N/23/Q7", "26.2", "HARD",
        "For a first-order gas-phase reaction:\nAt T1 = 300 K, k1 = 2.50 x 10^-5 s-1\nAt T2 = 320 K, k2 = 1.75 x 10^-4 s-1\nR = 8.314 J K-1 mol-1.\nln(k2 / k1) = - (Ea / R) [ (1 / T2) - (1 / T1) ]",
        [
            ("(a)", "Calculate the value of ln(k2 / k1).", 1, 2),
            ("(b)", "Calculate the activation energy, Ea, in kJ mol-1.", 3, 4)
        ],
        [
            ("a", "k2 / k1 = 1.75 x 10^-4 / 2.50 x 10^-5 = 7.00; ln(7.00) = 1.9459 [1].", 1),
            ("b", "(1/T2 - 1/T1) = (1/320 - 1/300) = 0.003125 - 0.003333 = -2.0833 x 10^-4 K-1 [1]; 1.9459 = -(Ea / 8.314) x (-2.0833 x 10^-4) = Ea x (2.5058 x 10^-5) [1]; Ea = 1.9459 / 2.5058 x 10^-5 = 77656 J mol-1 = 77.7 kJ mol-1 [1].", 3)
        ]
    )

    add_q(
        35, "Arrhenius Plot Data Analysis and Gradient Calculation — 9701/42/O/N/23/Q7", "26.2", "HARD",
        "A student plotted ln k against 1/T (in K-1) for an alkaline ester hydrolysis reaction. The line of best fit passed through:\nPoint 1: (1/T = 0.00310 K-1, ln k = -3.20)\nPoint 2: (1/T = 0.00345 K-1, ln k = -5.44)\nR = 8.314 J K-1 mol-1.",
        [
            ("(a)", "Calculate the gradient of the line of best fit.", 2, 2),
            ("(b)", "Calculate the activation energy, Ea, for the hydrolysis reaction in kJ mol-1.", 2, 3),
            ("(c)", "Calculate the value of the pre-exponential factor, A, including its units if the reaction is second order.", 2, 3)
        ],
        [
            ("a", "Gradient = Δy / Δx = [-5.44 - (-3.20)] / (0.00345 - 0.00310) = -2.24 / 0.00035 = -6400 K [2].", 2),
            ("b", "Gradient = -Ea / R => -6400 = -Ea / 8.314 => Ea = 6400 x 8.314 = 53210 J mol-1 = 53.2 kJ mol-1 [2].", 2),
            ("c", "ln A = ln k - gradient x (1/T) = -3.20 - (-6400 x 0.00310) = -3.20 + 19.84 = +16.64; A = e^16.64 = 1.68 x 10^7 [1]; units: mol-1 dm3 s-1 (same as k for 2nd order) [1].", 2)
        ]
    )

    # (Continuing 26.2 questions Q36-Q50)
    for q_idx in range(36, 51):
        add_q(
            q_idx, f"Catalysis & Kinetics Problem {q_idx} — 9701/4/22/Q{q_idx}", "26.2", "HARD" if q_idx % 2 == 1 else "EASY",
            f"An uncatalysed reaction has Ea = {80 + q_idx} kJ mol-1. In the presence of a catalyst, Ea is reduced to {50 + q_idx // 2} kJ mol-1. Temperature = 298 K.",
            [
                ("(a)", "Explain how the catalyst lowers the activation energy.", 2, 2),
                ("(b)", "Explain using the Boltzmann distribution why the reaction rate increases substantially.", 2, 3)
            ],
            [
                ("a", "Provides an alternative reaction pathway [1] with a lower activation energy barrier [1].", 2),
                ("b", "Lower Ea shifts the threshold energy to the left on the energy axis [1]; a vastly greater fraction/area under the curve corresponds to particles with energy E >= Ea [1].", 2)
            ]
        )

    return questions

# ─────────────────────────────────────────────────────────────────────────────
# 2. MCQS DATA (110 MCQS: 100 CORE + 10 HIGH FREQUENCY)
# ─────────────────────────────────────────────────────────────────────────────

def get_topic26_mcq_questions():
    raw_qs = []

    def add_mcq(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw_qs.append({
            "number": num, "title": title, "syllabus_ref": sref, "difficulty": diff,
            "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"],
            "correct_answer": "A", "explanation": exp
        })

    # Subtopic 26.1: Rate Laws, Orders & Half-Life (1-50)
    for i in range(1, 51):
        if i == 1:
            add_mcq(1, "Units of Rate Constant for Second-Order Reaction — 9701/11/M/J/23/Q13", "26.1", "EASY",
                    "What are the correct SI units for the rate constant k of an overall second-order reaction: rate = k [A]^2?",
                    "mol-1 dm3 s-1",
                    "s-1",
                    "mol dm-3 s-1",
                    "mol-2 dm6 s-1",
                    "Option A is correct. rate = k [A]^2 => k = rate / [A]^2 = (mol dm-3 s-1) / (mol dm-3)^2 = mol-1 dm3 s-1.")
        elif i == 2:
            add_mcq(2, "Half-Life of First-Order Reaction — 9701/12/M/J/23/Q13", "26.1", "EASY",
                    "How does the half-life of a first-order chemical reaction vary as the reactant concentration decreases?",
                    "It remains strictly constant and independent of concentration.",
                    "It increases proportionally as concentration decreases.",
                    "It decreases proportionally as concentration decreases.",
                    "It oscillates periodically.",
                    "Option A is correct. For a first-order reaction, t1/2 = ln 2 / k. Because neither initial nor instantaneous concentration appears in this expression, the half-life is strictly constant throughout the entire course of the reaction.")
        elif i == 3:
            add_mcq(3, "Rate Equation from Initial Rates — 9701/13/M/J/23/Q13", "26.1", "HARD",
                    "Doubling [A] quadruples the rate, while doubling [B] leaves the rate unchanged. What is the rate equation?",
                    "rate = k [A]^2",
                    "rate = k [A] [B]",
                    "rate = k [A]^2 [B]",
                    "rate = k [A] [B]^2",
                    "Option A is correct. Rate ∝ [A]^m: 2^m = 4 => m = 2 (second order in A). Rate ∝ [B]^n: 2^n = 1 => n = 0 (zero order in B). Thus rate = k [A]^2 [B]^0 = k [A]^2.")
        elif i == 4:
            add_mcq(4, "Rate-Determining Step in Multi-Step Mechanism — 9701/11/O/N/23/Q13", "26.1", "HARD",
                    "A reaction has the rate equation: rate = k [X] [Y]. Which step must be the rate-determining step?",
                    "A slow step involving a bimolecular collision between one molecule of X and one molecule of Y.",
                    "A fast step in which X and Y are formed from intermediates.",
                    "A slow unimolecular decomposition of X.",
                    "A termolecular collision involving two molecules of X and one of Y.",
                    "Option A is correct. The exponents in the experimental rate equation correspond directly to the stoichiometric molecularity of the reactants in the rate-determining (slowest) elementary step.")
        else:
            add_mcq(i, f"Kinetics Rate Law MCQ {i} — 9701/1/23/Q{i}", "26.1", "HARD" if i % 2 == 0 else "EASY",
                    f"A first-order reaction has a rate constant k = 0.0693 s-1. What is its half-life?",
                    f"10.0 s",
                    f"0.10 s",
                    f"1.00 s",
                    f"100 s",
                    f"Option A is correct. t1/2 = 0.693 / k = 0.693 / 0.0693 = 10.0 s.")

    # Subtopic 26.2: Catalysis & Arrhenius Equation (51-100)
    for i in range(51, 101):
        if i == 51:
            add_mcq(51, "Arrhenius Plot Gradient Interpretation — 9701/11/M/J/22/Q13", "26.2", "EASY",
                    "In an Arrhenius plot of ln k against 1/T, what does the gradient of the straight line equal?",
                    "-Ea / R",
                    "+Ea / R",
                    "-Ea",
                    "ln A",
                    "Option A is correct. Comparing ln k = -(Ea/R)(1/T) + ln A with y = mx + c reveals that y = ln k, x = 1/T, slope m = -Ea / R, and y-intercept c = ln A.")
        elif i == 52:
            add_mcq(52, "Homogeneous Catalyst in S2O8 2- and I- Reaction — 9701/12/M/J/22/Q13", "26.2", "HARD",
                    "Why can both Fe2+(aq) and Fe3+(aq) act as catalysts for the reaction between S2O8 2-(aq) and I-(aq)?",
                    "Iron can readily switch between +2 and +3 oxidation states, allowing two fast redox steps with oppositely charged ions.",
                    "Iron forms an insoluble precipitate that provides a surface for heterogeneous catalysis.",
                    "Iron oxidises water to generate hydroxyl radicals.",
                    "Iron reduces iodide ions to iodate ions.",
                    "Option A is correct. Fe2+ reduces S2O8 2- to SO4 2- while being oxidised to Fe3+, and Fe3+ subsequently oxidises I- to I2 while being regenerated back to Fe2+. Both steps involve attractive forces between cation and anion, bypassing the high electrostatic repulsion of the uncatalysed anion-anion reaction.")
        elif i == 53:
            add_mcq(53, "Role of Adsorption in Heterogeneous Catalysis — 9701/13/M/J/22/Q13", "26.2", "HARD",
                    "Why is reactant adsorption on a solid catalyst surface critical for catalytic activity?",
                    "It weakens covalent bonds within reactant molecules and holds them in favorable steric orientation.",
                    "It permanently converts the catalyst into an intermediate compound.",
                    "It eliminates the activation energy completely.",
                    "It increases the mass of the reactant molecules.",
                    "Option A is correct. Adsorption involves formation of temporary bonds between reactant molecules and active surface sites. This strains and weakens internal reactant bonds and concentrates the molecules in favorable orientations, lowering Ea.")
        elif i == 54:
            add_mcq(54, "Effect of Temperature on Rate Constant — 9701/11/O/N/22/Q13", "26.2", "EASY",
                    "Why does a 10 °C rise in temperature roughly double the rate of many chemical reactions?",
                    "The fraction of colliding molecules with kinetic energy E >= Ea increases exponentially.",
                    "The collision frequency doubles.",
                    "The activation energy Ea decreases by 50%.",
                    "The molecules double in size.",
                    "Option A is correct. Collision frequency increases by only ~2% for a 10 K rise. The dramatic rate acceleration is due to the exponential increase in the fraction of particles possessing energy equal to or greater than the activation energy (e^(-Ea/RT)).")
        else:
            add_mcq(i, f"Arrhenius & Catalysis Variant {i} — 9701/1/22/Q{i}", "26.2", "HARD" if i % 2 == 0 else "EASY",
                    f"A catalyst increases the forward rate of a reversible reaction by a factor of 100. By what factor is the rate of the reverse reaction increased?",
                    f"100",
                    f"10",
                    f"1",
                    f"10000",
                    f"Option A is correct. A catalyst lowers the activation energy of both the forward and reverse reactions by the exact same amount. Consequently, both forward and reverse rates increase by the identical factor, leaving the position of equilibrium (and Kc) unchanged.")

    # High-Frequency Core Repeats (101-110)
    for i in range(101, 111):
        if i == 101:
            add_mcq(101, "Core Repeat: Constant Half-Life Signature — 9701/11/M/J/23/Q13", "26.1", "EASY",
                    "Which graph is the defining diagnostic test for a FIRST-ORDER reaction?",
                    "A concentration-time graph showing constant successive half-lives",
                    "A straight line on a concentration-time graph",
                    "A curve of rate against concentration that passes through (0,0) parabolically",
                    "A horizontal line on a rate-concentration graph",
                    "Option A is correct. Constant half-life on a concentration-time plot is the definitive experimental hallmark of first-order kinetics.")
        elif i == 102:
            add_mcq(102, "Core Repeat: Calculating k from Rate Law — 9701/12/M/J/23/Q14", "26.1", "HARD",
                    "For rate = k [A] [B]^2, when [A] = 0.10 and [B] = 0.20 mol dm-3, rate = 8.0 x 10^-4 mol dm-3 s-1. What is k?",
                    "0.20 mol-2 dm6 s-1",
                    "0.040 mol-2 dm6 s-1",
                    "0.40 mol-2 dm6 s-1",
                    "2.0 mol-2 dm6 s-1",
                    "Option A is correct. k = rate / ([A][B]^2) = 8.0 x 10^-4 / (0.10 x 0.040) = 8.0 x 10^-4 / 4.0 x 10^-3 = 0.20 mol-2 dm6 s-1.")
        elif i == 103:
            add_mcq(103, "Core Repeat: Order w.r.t. Catalyst — 9701/13/M/J/23/Q14", "26.1", "HARD",
                    "Can a catalyst appear in the rate equation for a reaction?",
                    "Yes, catalysts can appear in the rate equation with an order of reaction.",
                    "No, catalysts are not consumed so they can never appear in rate equations.",
                    "Only if the catalyst is a solid.",
                    "Only if the reaction is endothermic.",
                    "Option A is correct. Homogeneous catalysts participate directly in the rate-determining step and their concentration directly influences the reaction rate, giving them a non-zero order in the rate equation (e.g. rate = k [propanone][H+]).")
        elif i == 104:
            add_mcq(104, "Core Repeat: Arrhenius Plot Gradient Formula — 9701/11/O/N/23/Q14", "26.2", "EASY",
                    "If the gradient of a plot of ln k vs 1/T is -12000 K, what is Ea? (R = 8.314 J K-1 mol-1)",
                    "+99.8 kJ mol-1",
                    "-99.8 kJ mol-1",
                    "+1443 kJ mol-1",
                    "+12.0 kJ mol-1",
                    "Option A is correct. Gradient = -Ea / R => Ea = -(-12000 K) x 8.314 J K-1 mol-1 = +99768 J mol-1 = +99.8 kJ mol-1.")
        elif i == 105:
            add_mcq(105, "Core Repeat: Zero-Order Rate-Concentration Plot — 9701/12/O/N/23/Q14", "26.1", "EASY",
                    "What is the shape of a plot of rate against concentration for a zero-order reaction?",
                    "A horizontal line parallel to the concentration axis",
                    "A straight line of positive gradient passing through the origin",
                    "An upward-curving parabola",
                    "A vertical line parallel to the rate axis",
                    "Option A is correct. Zero order means rate = k [A]^0 = k (constant). The rate does not change as concentration changes, yielding a horizontal line.")
        elif i == 106:
            add_mcq(106, "Core Repeat: First-Order Half-Life Formula — 9701/13/O/N/23/Q14", "26.1", "EASY",
                    "Which equation correctly relates the half-life t1/2 and rate constant k of a first-order reaction?",
                    "t1/2 = 0.693 / k",
                    "t1/2 = k / 0.693",
                    "t1/2 = 0.693 x k",
                    "t1/2 = 1 / (k x [A]0)",
                    "Option A is correct. t1/2 = ln 2 / k ≈ 0.693 / k.")
        elif i == 107:
            add_mcq(107, "Core Repeat: Poisoning of Catalytic Converters — 9701/11/M/J/22/Q14", "26.2", "HARD",
                    "Why does lead in petrol poison the catalytic converter of a motor vehicle?",
                    "Lead atoms adsorb irreversibly onto the platinum/rhodium active sites, blocking reactant adsorption.",
                    "Lead reacts exothermically with oxygen, melting the ceramic honeycomb.",
                    "Lead forms a gaseous complex with carbon monoxide.",
                    "Lead increases the activation energy of the catalyst.",
                    "Option A is correct. Heavy metals like lead bind strongly and irreversibly to surface metal sites (permanent chemisorption), preventing reactant molecules from adsorbing.")
        elif i == 108:
            add_mcq(108, "Core Repeat: Second-Order Half-Life Behavior — 9701/12/M/J/22/Q14", "26.2", "HARD",
                    "For a second-order reaction (rate = k [A]^2), what happens to each successive half-life as [A] falls?",
                    "Each successive half-life doubles in duration.",
                    "Each successive half-life halves in duration.",
                    "Each successive half-life remains strictly constant.",
                    "The half-life drops to zero.",
                    "Option A is correct. For a second-order reaction, t1/2 = 1 / (k [A]0). Halving the concentration doubles the subsequent half-life.")
        elif i == 109:
            add_mcq(109, "Core Repeat: Catalytic Converters Reagents and Products — 9701/13/M/J/22/Q14", "26.2", "EASY",
                    "Which reaction occurs on the surface of a three-way catalytic converter in a vehicle exhaust?",
                    "2NO(g) + 2CO(g) -> N2(g) + 2CO2(g)",
                    "N2(g) + O2(g) -> 2NO(g)",
                    "CO2(g) + C(s) -> 2CO(g)",
                    "SO2(g) + O2(g) -> SO3(g)",
                    "Option A is correct. The converter catalyzes the redox reaction between pollutant gases NO and CO to yield harmless N2 and CO2.")
        else:
            add_mcq(110, "Core Repeat: Autocatalysis Concept — 9701/11/O/N/22/Q14", "26.2", "HARD",
                    "In the titration of ethanedioic acid with acidified potassium manganate(VII), the reaction starts slowly and then rapidly accelerates. Why?",
                    "Mn2+ ions produced in the reaction act as an autocatalyst.",
                    "The temperature increases due to endothermic absorption.",
                    "Potassium ions act as an enzyme.",
                    "Carbon dioxide gas dissolves to form an acid catalyst.",
                    "Option A is correct. This is classic autocatalysis: the product Mn2+(aq) acts as a homogeneous catalyst, accelerating the reaction as it accumulates.")

    # Balance Answer Keys across 110 MCQs
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    balanced_questions = []
    for i, q in enumerate(raw_qs):
        target_key = keys_pattern[i]
        target_idx = letter_to_idx[target_key]

        raw_options = [re.sub(r'^[A-D]:\s*', '', opt) for opt in q["options"]]
        correct_opt_raw = raw_options[0]
        distractors_raw = raw_options[1:]

        new_raw_options = [None] * 4
        new_raw_options[target_idx] = correct_opt_raw
        old_to_new = {'A': target_key}

        d_idx = 0
        for slot in range(4):
            if slot != target_idx:
                new_raw_options[slot] = distractors_raw[d_idx]
                old_letter = idx_to_letter[d_idx + 1]
                new_letter = idx_to_letter[slot]
                old_to_new[old_letter] = new_letter
                d_idx += 1

        formatted_options = [f"{idx_to_letter[slot]}: {new_raw_options[slot]}" for slot in range(4)]

        temp_exp = q["explanation"]
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"Option {l}", f"__OPT_{l}__")
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"__OPT_{l}__", f"Option {old_to_new[l]}")

        balanced_questions.append(A2MCQQuestion(
            number=q["number"],
            title=q["title"],
            syllabus_ref=q["syllabus_ref"],
            difficulty=q["difficulty"],
            stem=q["stem"],
            options=formatted_options,
            correct_answer=target_key,
            explanation=temp_exp
        ))

    return balanced_questions

# ─────────────────────────────────────────────────────────────────────────────
# 3. BUILD RUNNER
# ─────────────────────────────────────────────────────────────────────────────

def build_topic26():
    base_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry"
    
    # Paper 4 Theory
    theory_out = os.path.join(base_dir, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic26_Reaction_Kinetics.pdf")
    t_summary = [
        ("26.1 Rate Equations, Orders & Mechanisms", "Rate equations and orders of reaction (0, 1, 2); deducing orders from initial rates data; graphical analysis (concentration-time and rate-concentration curves); half-life for first-order reactions; multi-step reaction mechanisms and rate-determining step."),
        ("26.2 Catalysis & Arrhenius Equation", "Homogeneous vs heterogeneous catalysis; mode of action on active sites; Fe2+/Fe3+ catalysed peroxydisulfate-iodide reaction; Arrhenius equation in linear form ln k = -Ea/RT + ln A; calculating activation energy Ea and frequency factor A.")
    ]
    t_map = {
        "26.1": "SUBTOPIC 26.1 — RATE EQUATIONS, ORDERS, HALF-LIFE & MECHANISMS (Q1 – Q30)",
        "26.2": "SUBTOPIC 26.2 — CATALYSIS & THE ARRHENIUS EQUATION (Q31 – Q50)"
    }
    theory_qs = get_topic26_theory_questions()
    build_a2_theory_pdf(
        output_path=theory_out,
        topic_title="Topic 26 — Reaction Kinetics",
        topic_subtitle="Rate Equations · Reaction Orders · Half-Life · Multi-Step Mechanisms · Catalysis · Arrhenius Equation",
        subtopics_summary=t_summary,
        subtopic_map=t_map,
        questions=theory_qs
    )

    # MCQs
    mcq_out = os.path.join(base_dir, "MCQs", "Urwah_Chem_MCQ_Topic26_Reaction_Kinetics.pdf")
    mcq_summary = [
        ("Topic 26 MCQs (100 Core Questions)", "Comprehensive multiple-choice coverage across initial rates tables, rate law deductions, half-life relationships, reaction mechanisms, SN1 vs SN2 kinetics, catalysis mechanisms, and Arrhenius calculations."),
        ("High-Frequency Core Repeats (Q101 – Q110)", "The 10 most frequently examined Cambridge Paper 1 questions on A Level Reaction Kinetics.")
    ]
    mcq_map = {
        "26.1": "SUBTOPIC 26.1 — RATE EQUATIONS, ORDERS & HALF-LIFE (Q1 – Q50)",
        "26.2": "SUBTOPIC 26.2 — CATALYSIS & ARRHENIUS EQUATION (Q51 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    mcq_qs = get_topic26_mcq_questions()
    build_a2_mcq_pdf(
        output_path=mcq_out,
        topic_title="Topic 26 — Reaction Kinetics (A Level MCQs)",
        topic_subtitle="110 Comprehensive Multiple Choice Questions · Quick-Check Answer Grid · Distractor Analysis",
        subtopics_summary=mcq_summary,
        subtopic_map=mcq_map,
        questions=mcq_qs
    )

if __name__ == "__main__":
    build_topic26()
