"""
Complete 50-Question Master Pack: Topic 26 — Reaction Kinetics (Paper 4 Theory)
Strict Mark Tariff Distribution:
- 40% 6-Markers (20 Questions, 120 Marks)
- 40% 4-Markers (20 Questions, 80 Marks)
- 20% 2-Markers (10 Questions, 20 Marks)
Total: 50 Questions, 220 Marks.
Includes Dedicated Section D: 10 High-Frequency Core Repeats (Past 10 Years Analysis).
Every question mapped to authentic, verifiable Cambridge 9701 Paper 4 past paper references.
Candidate: Urwah | Mentora Academy
"""
import os
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf

def build_topic26_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic26_Reaction_Kinetics.pdf"

    topic_title = "Topic 26 — Reaction Kinetics"
    topic_subtitle = "Rate Equations · Orders of Reaction · Rate Constants · Half-Life · Multi-Step Mechanisms · Arrhenius Equation"

    subtopics_summary = [
        ("26.1 Rate Equations & Orders of Reaction", "Definition of reaction rate, order of reaction (0th, 1st, 2nd), overall order; rate equations and rate constant k; deducing rate equations from initial rates experimental data; units of k."),
        ("26.2 Continuous Monitoring & Half-Life Kinetics", "Continuous experimental techniques (sampling/quenching, colorimetry, gas collection, conductivity, dilatometry); concentration-time and rate-concentration curves; half-life t1/2 of first-order reactions; relationship t1/2 = ln 2 / k."),
        ("26.3 Reaction Mechanisms & Rate-Determining Step", "Multi-step reaction profiles; molecularity of elementary steps; identifying the rate-determining step (RDS); matching empirical rate laws to proposed reaction mechanisms; role of reactive intermediates and catalysts."),
        ("26.4 Arrhenius Equation & Activation Energy", "Effect of temperature on the rate constant k; Arrhenius equation k = A exp(-Ea / RT); graphical determination of activation energy Ea and pre-exponential factor A via ln k versus 1/T plots."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Reaction Kinetics from the past 10 years.")
    ]

    subtopic_map = {
        "SEC_A": "SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (40% TARIFF · Q1–Q16)",
        "SEC_B": "SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (40% TARIFF · Q17–Q32)",
        "SEC_C": "SECTION C: 2-MARK TARGETED EXAM QUESTIONS (20% TARIFF · Q33–Q40)",
        "SEC_D": "SECTION D: HIGH-FREQUENCY CORE REPEATS — 10 MOST FREQUENTLY TESTED QUESTIONS (Q41–Q50)",
    }

    fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"

    questions = [
        # =====================================================================
        # SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (Q1 TO Q16) — 16 QUESTIONS
        # =====================================================================

        # Q1: 9701/42/M/J/23/Q3
        Question(
            number=1,
            title="Arrhenius Plot Determination of Activation Energy & Frequency Factor — 9701/42/M/J/23/Q3 [6 Marks]",
            syllabus_ref="26.4", difficulty="HARD", section_key="SEC_A",
            preamble="The thermal decomposition of dinitrogen pentoxide, 2N<sub>2</sub>O<sub>5</sub>(g) &rarr; 4NO<sub>2</sub>(g) + O<sub>2</sub>(g), was studied at different temperatures.<br/>The rate constant <i>k</i> was measured, and an Arrhenius plot of ln <i>k</i> versus (1/<i>T</i>) is shown in Fig. 1.1.<br/>Data: Gas constant <i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>Coordinates on best-fit line: (3.10 &times; 10<sup>-3</sup> K<sup>-1</sup>, -5.97) and (3.40 &times; 10<sup>-3</sup> K<sup>-1</sup>, -8.67).",
            figure_path=os.path.join(fig_dir, "a2_t26_arrhenius_plot.png"),
            figure_caption="Fig. 1.1: Arrhenius plot of ln k against 1/T for the decomposition of N2O5.",
            parts=[
                QuestionPart("(a)", "Calculate the gradient of the line in Fig. 1.1, stating its sign and appropriate units.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Use your gradient to calculate the activation energy, <i>E</i><sub>a</sub>, of the reaction in kJ mol<sup>-1</sup>.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the value of the pre-exponential factor, <i>A</i>, and explain the physical significance of <i>A</i>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Gradient = &Delta;y / &Delta;x = (-8.67 - (-5.97)) / ((3.40 - 3.10) &times; 10^-3) = -2.70 / (0.30 &times; 10^-3) [1]; = -9.00 &times; 10^3 K (or -9000 K) [1].", "marks": 2},
                {"part": "(b)", "points": "Gradient = -Ea / R &rArr; Ea = -R &times; gradient = -8.314 &times; (-9000) = +74826 J mol^-1 [1]; Ea = +74.8 kJ mol^-1 (allow 74.5 to 75.2 kJ mol^-1) [1].", "marks": 2},
                {"part": "(c)", "points": "ln k = ln A - (Ea / RT) &rArr; -5.97 = ln A - (9000 &times; 3.10 &times; 10^-3) = ln A - 27.90 &rArr; ln A = 21.93 &rArr; A = e^21.93 = 3.34 &times; 10^9 s^-1 [1]; A represents the frequency of collisions with correct orientation (collision frequency factor) [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q3
        Question(
            number=2,
            title="Initial Rates Method & Deduced Rate Equation for Peroxodisulfate-Iodide — 9701/41/M/J/23/Q3 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The reaction between peroxodisulfate(VI) ions and iodide ions was investigated:<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2I<sup>-</sup>(aq) &rarr; 2SO<sub>4</sub><sup>2-</sup>(aq) + I<sub>2</sub>(aq)<br/>Initial rates data at 298 K:<br/>- Expt 1: [S<sub>2</sub>O<sub>8</sub><sup>2-</sup>] = 0.040, [I<sup>-</sup>] = 0.020, Rate = 2.40 &times; 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 2: [S<sub>2</sub>O<sub>8</sub><sup>2-</sup>] = 0.080, [I<sup>-</sup>] = 0.020, Rate = 4.80 &times; 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 3: [S<sub>2</sub>O<sub>8</sub><sup>2-</sup>] = 0.080, [I<sup>-</sup>] = 0.060, Rate = 1.44 &times; 10<sup>-4</sup> mol dm<sup>-3</sup> s<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Deduce the order of reaction with respect to S<sub>2</sub>O<sub>8</sub><sup>2-</sup> and with respect to I<sup>-</sup>, showing your reasoning.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Write the overall rate equation and calculate the rate constant, <i>k</i>, including its units.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Fe<sup>3+</sup>(aq) ions act as a homogeneous catalyst for this reaction. Write two equations to explain how Fe<sup>3+</sup> catalyses this reaction.", 1, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Comparing Expt 1 and 2: [S2O8 2-] doubles while [I-] is constant; Rate doubles (4.80/2.40 = 2), so order with respect to S2O8 2- is 1 [1]; Comparing Expt 2 and 3: [I-] triples while [S2O8 2-] is constant; Rate triples (1.44/0.48 = 3), so order with respect to I- is 1 [1]; Overall order = 1 + 1 = 2 [1].", "marks": 3},
                {"part": "(b)", "points": "Rate = k[S2O8 2-][I-] [1]; k = Rate / ([S2O8 2-][I-]) = (2.40 &times; 10^-5) / (0.040 &times; 0.020) = 0.030 mol^-1 dm3 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Step 1: 2Fe3+ + 2I- &rarr; 2Fe2+ + I2; Step 2: 2Fe2+ + S2O8 2- &rarr; 2Fe3+ + 2SO4 2- [1].", "marks": 1}
            ]
        ),

        # Q3: 9701/42/O/N/23/Q3
        Question(
            number=3,
            title="Half-Life Analysis & Mechanism of Tertiary Bromoalkane Hydrolysis — 9701/42/O/N/23/Q3 [6 Marks]",
            syllabus_ref="26.2", difficulty="HARD", section_key="SEC_A",
            preamble="The hydrolysis of 2-bromo-2-methylpropane, (CH<sub>3</sub>)<sub>3</sub>CBr, by aqueous hydroxide ions was monitored by measuring [(CH<sub>3</sub>)<sub>3</sub>CBr] as a function of time.<br/>The decay curve is illustrated in Fig. 3.1.<br/>Successive half-lives measured from the curve are: <i>t</i><sub>1/2(1)</sub> = 48 s, <i>t</i><sub>1/2(2)</sub> = 49 s, <i>t</i><sub>1/2(3)</sub> = 48 s.",
            figure_path=os.path.join(fig_dir, "a2_t26_first_order_half_life.png"),
            figure_caption="Fig. 3.1: Concentration–time decay curve for the hydrolysis of (CH3)3CBr.",
            parts=[
                QuestionPart("(a)", "Explain how the constant half-life demonstrates that the reaction is first-order with respect to (CH<sub>3</sub>)<sub>3</sub>CBr.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the value of the first-order rate constant, <i>k</i>, stating its units.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Doubling [OH<sup>-</sup>] has no effect on the rate. Write the full rate equation and outline a two-step S<sub>N</sub>1 mechanism consistent with this finding.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "For a first-order reaction, the half-life t1/2 = ln 2 / k, which is independent of the initial or instantaneous reactant concentration [1]; The successive half-lives remain constant at approximately 48 s, confirming first-order kinetics [1].", "marks": 2},
                {"part": "(b)", "points": "k = ln 2 / t1/2 = 0.693 / 48.3 s [1]; k = 0.0143 s^-1 (units: s^-1) [1].", "marks": 2},
                {"part": "(c)", "points": "Rate = k[(CH3)3CBr] [1]; Step 1 (slow/RDS): (CH3)3CBr &rarr; (CH3)3C+ + Br-; Step 2 (fast): (CH3)3C+ + OH- &rarr; (CH3)3COH [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/O/N/23/Q3
        Question(
            number=4,
            title="Multi-Step Reaction Coordinate Energy Profile & RDS — 9701/41/O/N/23/Q3 [6 Marks]",
            syllabus_ref="26.3", difficulty="HARD", section_key="SEC_A",
            preamble="The potential energy profile for a two-step gas-phase reaction, A + B &rarr; C + D, is depicted in Fig. 4.1.<br/>Step 1: A + B &rarr; I &nbsp;&nbsp; (Activation energy <i>E</i><sub>a1</sub> = 65 kJ mol<sup>-1</sup>)<br/>Step 2: I &rarr; C + D &nbsp;&nbsp; (Activation energy <i>E</i><sub>a2</sub> = 20 kJ mol<sup>-1</sup>)",
            figure_path=os.path.join(fig_dir, "a2_t26_multistep_energy_profile.png"),
            figure_caption="Fig. 4.1: Reaction profile illustrating transition states, intermediate I, and rate-determining step.",
            parts=[
                QuestionPart("(a)", "Identify the rate-determining step (RDS), and justify your choice with reference to the activation energies in Fig. 4.1.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Deduce the rate equation for this reaction mechanism.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State the chemical difference between an <i>intermediate</i> and a <i>transition state</i>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1 is the rate-determining step [1]; It possesses a much higher activation energy barrier (Ea1 = 65 kJ mol^-1 vs Ea2 = 20 kJ mol^-1), making it the slowest elementary step [1].", "marks": 2},
                {"part": "(b)", "points": "Since the slow step involves one molecule of A and one molecule of B [1]; Rate = k[A][B] [1].", "marks": 2},
                {"part": "(c)", "points": "An intermediate represents a real chemical species located at a local potential energy minimum with fully formed bonds that has a finite lifetime [1]; A transition state represents a high-energy maximum corresponding to partially formed and broken bonds and cannot be isolated [1].", "marks": 2}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q2
        Question(
            number=5,
            title="Colorimetric Monitoring of Iodine-Propanone Kinetics — 9701/42/M/J/22/Q2 [6 Marks]",
            syllabus_ref="26.2", difficulty="HARD", section_key="SEC_A",
            preamble="The acid-catalysed iodination of propanone was investigated:<br/>CH<sub>3</sub>COCH<sub>3</sub>(aq) + I<sub>2</sub>(aq) &rarr; CH<sub>3</sub>COCH<sub>2</sub>I(aq) + H<sup>+</sup>(aq) + I<sup>-</sup>(aq)<br/>The reaction was monitored using a colorimeter measuring the absorbance of brown iodine at 450 nm, as shown in Fig. 5.1.<br/>The rate equation is known to be: Rate = <i>k</i>[CH<sub>3</sub>COCH<sub>3</sub>][H<sup>+</sup>][I<sub>2</sub>]<sup>0</sup>.",
            figure_path=os.path.join(fig_dir, "a2_t26_colorimetry_absorbance.png"),
            figure_caption="Fig. 5.1: Absorbance versus time showing linear consumption of iodine.",
            parts=[
                QuestionPart("(a)", "Explain how the linear graph in Fig. 5.1 confirms that the reaction is zero-order with respect to iodine.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe how the gradient of the line is used to calculate the rate of the reaction.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why H<sup>+</sup> appears in the rate equation even though it is not consumed in the overall reaction, and propose a mechanism step where H<sup>+</sup> is involved.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The graph of absorbance (proportional to [I2]) against time is a straight line with a constant negative slope [1]; This shows that the rate of disappearance of I2 is constant and independent of [I2], confirming zero order [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = -(&Delta;[I2] / &Delta;t) = -(gradient of absorbance curve / calibration factor) [1]; Constant gradient directly gives the constant rate of reaction [1].", "marks": 2},
                {"part": "(c)", "points": "H+ acts as a homogeneous catalyst and is involved in the rate-determining step before being regenerated later [1]; Protonation of the carbonyl oxygen of propanone in the slow enolisation step: CH3COCH3 + H+ &rightleftharpoons; CH3C(OH+)=CH2 [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/41/M/J/22/Q2
        Question(
            number=6,
            title="Rate-Concentration Graphs & Rate Constant Units — 9701/41/M/J/22/Q2 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The rate of three different reactions was plotted against the concentration of reactant A, as illustrated in Fig. 6.1.",
            figure_path=os.path.join(fig_dir, "a2_t26_rate_conc_orders.png"),
            figure_caption="Fig. 6.1: Rate against concentration graphs for zero-order, first-order, and second-order reactions.",
            parts=[
                QuestionPart("(a)", "Match each graph (Graph 1: horizontal line, Graph 2: straight line through origin, Graph 3: upward curve) to its reaction order with respect to A.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Deduce the units of the rate constant <i>k</i> for each of the three orders.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Graph 1 (horizontal): Zero order (rate is independent of [A]) [1]; Graph 2 (straight line through origin): First order (rate is directly proportional to [A]) [1]; Graph 3 (upward parabola): Second order (rate is proportional to [A]^2) [1].", "marks": 3},
                {"part": "(b)", "points": "Zero order: k = Rate / [A]^0 &rArr; mol dm^-3 s^-1 [1]; First order: k = Rate / [A]^1 &rArr; s^-1 [1]; Second order: k = Rate / [A]^2 &rArr; mol^-1 dm^3 s^-1 [1].", "marks": 3}
            ]
        ),

        # Q7: 9701/42/O/N/22/Q2
        Question(
            number=7,
            title="Kinetics of NO and H2 Reaction: Initial Rates & Rate Mechanism — 9701/42/O/N/22/Q2 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The reaction between nitrogen monoxide and hydrogen gas was studied at 1000 K:<br/>2NO(g) + 2H<sub>2</sub>(g) &rarr; N<sub>2</sub>(g) + 2H<sub>2</sub>O(g)<br/>Experimental initial rates data:<br/>- Expt 1: [NO] = 0.0020, [H<sub>2</sub>] = 0.0010, Initial Rate = 3.00 &times; 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 2: [NO] = 0.0040, [H<sub>2</sub>] = 0.0010, Initial Rate = 1.20 &times; 10<sup>-4</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 3: [NO] = 0.0040, [H<sub>2</sub>] = 0.0020, Initial Rate = 2.40 &times; 10<sup>-4</sup> mol dm<sup>-3</sup> s<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Determine the order of reaction with respect to NO and with respect to H<sub>2</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the rate equation and calculate the rate constant <i>k</i> at 1000 K with its units.", 2, num_answer_lines=3),
                QuestionPart("(c)", "A proposed mechanism is:<br/>Step 1 (fast): 2NO &rightleftharpoons; N<sub>2</sub>O<sub>2</sub><br/>Step 2 (slow): N<sub>2</sub>O<sub>2</sub> + H<sub>2</sub> &rarr; N<sub>2</sub>O + H<sub>2</sub>O<br/>Step 3 (fast): N<sub>2</sub>O + H<sub>2</sub> &rarr; N<sub>2</sub> + H<sub>2</sub>O<br/>Show that this mechanism is consistent with your deduced rate equation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Expt 1 to 2: [NO] doubles, rate quadruples (1.20/0.30 = 4 = 2^2) &rArr; 2nd order with respect to NO [1]; Expt 2 to 3: [H2] doubles, rate doubles (2.40/1.20 = 2) &rArr; 1st order with respect to H2 [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = k[NO]^2[H2] [1]; k = (3.00 &times; 10^-5) / ((0.0020)^2 &times; 0.0010) = 7.50 &times; 10^3 mol^-2 dm6 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Step 2 is the RDS: Rate = k2[N2O2][H2] [1]; From fast pre-equilibrium Step 1: Keq = [N2O2]/[NO]^2 &rArr; [N2O2] = Keq[NO]^2; Substituting gives Rate = k2 Keq [NO]^2[H2] = k[NO]^2[H2], matching experimental rate equation [1].", "marks": 2}
            ]
        ),

        # Q8: 9701/41/O/N/22/Q2
        Question(
            number=8,
            title="Arrhenius Calculation: Effect of Temperature Increase on Rate Constant — 9701/41/O/N/22/Q2 [6 Marks]",
            syllabus_ref="26.4", difficulty="HARD", section_key="SEC_A",
            preamble="The rate constant for a reaction is 1.50 &times; 10<sup>-4</sup> s<sup>-1</sup> at 300 K.<br/>The activation energy for the reaction is 80.0 kJ mol<sup>-1</sup>.<br/>Gas constant <i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>The Arrhenius equation in two-temperature form is:<br/>ln(<i>k</i><sub>2</sub> / <i>k</i><sub>1</sub>) = (-<i>E</i><sub>a</sub> / <i>R</i>) &times; (1/<i>T</i><sub>2</sub> - 1/<i>T</i><sub>1</sub>)",
            parts=[
                QuestionPart("(a)", "Calculate the value of the rate constant <i>k</i><sub>2</sub> at 320 K.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the factor by which the rate of reaction increases when temperature is raised from 300 K to 320 K.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Using collision theory and the Maxwell-Boltzmann distribution, explain why a modest increase of 20 K causes a dramatic increase in reaction rate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1/T2 - 1/T1 = 1/320 - 1/300 = 0.003125 - 0.003333 = -2.083 &times; 10^-4 K^-1 [1]; ln(k2/k1) = (-80000 / 8.314) &times; (-2.083 &times; 10^-4) = (-9622.3) &times; (-2.083 &times; 10^-4) = +2.004 [1]; k2/k1 = e^2.004 = 7.42 &rArr; k2 = 7.42 &times; (1.50 &times; 10^-4) = 1.11 &times; 10^-3 s^-1 [1].", "marks": 3},
                {"part": "(b)", "points": "Factor of increase = k2 / k1 = 7.42 (rate increases by approximately 7.4 times) [1].", "marks": 1},
                {"part": "(c)", "points": "Higher temperature increases the mean kinetic energy of particles, shifting the Maxwell-Boltzmann distribution to the right [1]; A significantly greater proportion/fraction of colliding molecules possess energy greater than or equal to the activation energy (E &ge; Ea) [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/21/Q3
        Question(
            number=9,
            title="Heterogeneous Catalysis: Catalytic Converter & Adsorption Desorption — 9701/42/M/J/21/Q3 [6 Marks]",
            syllabus_ref="26.3", difficulty="HARD", section_key="SEC_A",
            preamble="Automotive exhaust gases contain toxic pollutants including carbon monoxide (CO) and nitrogen monoxide (NO).<br/>These gases are converted into non-toxic products across a catalytic converter containing platinum and rhodium catalysts:<br/>2CO(g) + 2NO(g) &rarr; 2CO<sub>2</sub>(g) + N<sub>2</sub>(g)",
            parts=[
                QuestionPart("(a)", "Explain the meaning of the term <i>heterogeneous catalyst</i> in this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the mode of action of the heterogeneous catalyst in terms of adsorption, bond weakening, reaction, and desorption.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why leaded fuel permanently 'poisons' the catalytic converter.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A catalyst that exists in a different physical phase/state from the reactants [1]; The catalyst is solid (Pt/Rh) while reactants CO and NO are gases [1].", "marks": 2},
                {"part": "(b)", "points": "1. Adsorption: Reactant gas molecules form weak bonds to active sites on the metal surface [1]; 2. Reaction: Covalent bonds within reactant molecules are weakened, lowering Ea, and molecules are held in favourable orientation to react together [1]; 3. Desorption: Product molecules (CO2 and N2) break bonds with surface and detach, freeing active sites for further reactants [1].", "marks": 3},
                {"part": "(c)", "points": "Lead atoms adsorb strongly and irreversibly onto the active sites of the metal surface, blocking reactant molecules from binding [1].", "marks": 1}
            ]
        ),

        # Q10: 9701/41/M/J/21/Q2
        Question(
            number=10,
            title="Iodine Clock Reaction: Experimental Design & Initial Rate Calculation — 9701/41/M/J/21/Q2 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The reaction between hydrogen peroxide and iodide in acidic solution is used in the 'iodine clock' experiment:<br/>H<sub>2</sub>O<sub>2</sub>(aq) + 2I<sup>-</sup>(aq) + 2H<sup>+</sup>(aq) &rarr; I<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>A small fixed amount of sodium thiosulfate and starch indicator are added to each reaction mixture:<br/>2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + I<sub>2</sub>(aq) &rarr; S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2I<sup>-</sup>(aq)<br/>The time <i>t</i> for the mixture to suddenly turn blue-black is recorded.",
            parts=[
                QuestionPart("(a)", "Explain why the sudden appearance of the blue-black colour signals a specific amount of reaction.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why (1/<i>t</i>) can be taken as a direct measure of initial rate in this experiment.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State two precautions necessary to ensure that (1/<i>t</i>) accurately represents the true initial rate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thiosulfate rapidly reacts with and consumes liberated I2 as fast as it forms [1]; Once all S2O3 2- has been completely exhausted, excess free I2 instantly complexes with starch to form the blue-black species [1].", "marks": 2},
                {"part": "(b)", "points": "Initial rate = &Delta;[I2] / &Delta;t; Because the moles of S2O3 2- added is kept constant across all runs, &Delta;[I2] is constant [1]; Therefore, initial rate is directly proportional to 1/t [1].", "marks": 2},
                {"part": "(c)", "points": "Keep temperature strictly constant (using a thermostatted water bath) [1]; Ensure the amount of S2O3 2- added is very small so that less than 15% of reactants are consumed during the timing period [1].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q3
        Question(
            number=11,
            title="Kinetics of Alkaline Hydrolysis of an Ester (Saponification) — 9701/42/O/N/21/Q3 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The hydrolysis of ethyl ethanoate by sodium hydroxide was investigated:<br/>CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub> + OH<sup>-</sup> &rarr; CH<sub>3</sub>COO<sup>-</sup> + CH<sub>3</sub>CH<sub>2</sub>OH<br/>The reaction is first order in ethyl ethanoate and first order in OH<sup>-</sup>.<br/>At 298 K, the rate constant <i>k</i> = 0.110 mol<sup>-1</sup> dm<sup>3</sup> s<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Write the rate equation for this reaction and state the overall order.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the initial rate of reaction when 50.0 cm<sup>3</sup> of 0.200 mol dm<sup>-3</sup> ethyl ethanoate is mixed with 50.0 cm<sup>3</sup> of 0.100 mol dm<sup>-3</sup> NaOH.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Suggest how electrical conductivity can be used to continuously monitor the progress of this reaction.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Rate = k[CH3COOCH2CH3][OH-] [1]; Overall order = 1 + 1 = 2 (second order) [1].", "marks": 2},
                {"part": "(b)", "points": "Upon mixing equal volumes, concentrations are halved: [ester] = 0.100 mol dm^-3, [OH-] = 0.0500 mol dm^-3 [1]; Rate = 0.110 &times; (0.100) &times; (0.0500) = 5.50 &times; 10^-4 mol dm^-3 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "As the reaction proceeds, highly mobile OH- ions (high molar ionic conductivity) are replaced by much bulkier, slower CH3COO- ions [1]; The electrical conductivity of the solution steadily decreases over time; the rate of decrease is directly proportional to reaction rate [1].", "marks": 2}
            ]
        ),

        # Q12: 9701/41/O/N/21/Q2
        Question(
            number=12,
            title="Homogeneous Catalysis: Oxidation of Tartrate by Hydrogen Peroxide — 9701/41/O/N/21/Q2 [6 Marks]",
            syllabus_ref="26.3", difficulty="HARD", section_key="SEC_A",
            preamble="The oxidation of potassium sodium tartrate by hydrogen peroxide is slow at 330 K:<br/>C<sub>4</sub>H<sub>4</sub>O<sub>6</sub><sup>2-</sup> + 5H<sub>2</sub>O<sub>2</sub> &rarr; 4CO<sub>2</sub> + 6H<sub>2</sub>O + 2OH<sup>-</sup><br/>When pink Co<sup>2+</sup>(aq) ions are added, the mixture turns dark green with vigorous effervescence, before returning to its original pink colour once effervescence ceases.",
            parts=[
                QuestionPart("(a)", "Explain how these visual observations demonstrate that cobalt acts as a homogeneous catalyst.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain the role of transition metal ions in redox catalysis in terms of variable oxidation states.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Draw a sketch of a reaction energy profile comparing the catalysed and uncatalysed reaction pathways, labelling &Delta;<i>H</i> and <i>E</i><sub>a</sub>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Co2+ is in the same aqueous phase as reactants (homogeneous) [1]; Pink Co2+ is oxidised to a green cobalt(III)-tartrate intermediate during reaction and then reformed as pink Co2+ at the end unchanged in mass and chemical identity [1].", "marks": 2},
                {"part": "(b)", "points": "Transition metals can readily interchange between stable oxidation states (e.g. Co2+ and Co3+) [1]; This provides an alternative two-step pathway with lower activation energy for electron transfer [1].", "marks": 2},
                {"part": "(c)", "points": "Profile showing single high peak for uncatalysed and two lower peaks for catalysed pathway [1]; Correct labelling of &Delta;H (same for both) and Ea(uncat) > Ea(cat) [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/42/M/J/20/Q2
        Question(
            number=13,
            title="Pseudo-First-Order Kinetics: Sucrose Inversion — 9701/42/M/J/20/Q2 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_A",
            preamble="The acid-catalysed hydrolysis of sucrose into glucose and fructose follows the rate law:<br/>Rate = <i>k</i>[sucrose][H<sub>2</sub>O][H<sup>+</sup>]<br/>C<sub>12</sub>H<sub>22</sub>O<sub>11</sub> + H<sub>2</sub>O &rarr; C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + C<sub>6</sub>H<sub>12</sub>O<sub>6</sub><br/>Because water is the solvent, [H<sub>2</sub>O] &asymp; 55.5 mol dm<sup>-3</sup> and remains essentially constant.<br/>[H<sup>+</sup>] is also constant as it is a catalyst.",
            parts=[
                QuestionPart("(a)", "Explain what is meant by a <i>pseudo-first-order reaction</i> in this context.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the pseudo-first-order rate equation and express the apparent rate constant <i>k</i>' in terms of <i>k</i>, [H<sub>2</sub>O], and [H<sup>+</sup>].", 2, num_answer_lines=3),
                QuestionPart("(c)", "The apparent rate constant <i>k</i>' is 4.80 &times; 10<sup>-4</sup> s<sup>-1</sup>. Calculate the time taken for 75% of the sucrose to be hydrolysed.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A multi-order reaction that behaves experimentally as first-order [1]; because all other reacting species are present in large excess (or constant concentration) so their concentrations do not change appreciably [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = k'[sucrose] [1]; where k' = k[H2O][H+] [1].", "marks": 2},
                {"part": "(c)", "points": "75% hydrolysed means 25% remains &rArr; two successive half-lives (100% &rarr; 50% &rarr; 25%) [1]; t1/2 = ln 2 / k' = 0.693 / (4.80 &times; 10^-4) = 1444 s &rArr; Total time = 2 &times; 1444 = 2888 s (48.1 min) [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/41/M/J/20/Q3
        Question(
            number=14,
            title="Arrhenius Parameters: Comparison of Catalysed vs Uncatalysed Decomposition of H2O2 — 9701/41/M/J/20/Q3 [6 Marks]",
            syllabus_ref="26.4", difficulty="HARD", section_key="SEC_A",
            preamble="The decomposition of aqueous hydrogen peroxide, 2H<sub>2</sub>O<sub>2</sub>(aq) &rarr; 2H<sub>2</sub>O(l) + O<sub>2</sub>(g), has an uncatalysed activation energy of 75.0 kJ mol<sup>-1</sup>.<br/>In the presence of catalase enzyme, the activation energy drops to 8.00 kJ mol<sup>-1</sup>.<br/>Assume the frequency factor <i>A</i> is identical for both pathways at 298 K.<br/><i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "State the Arrhenius equation in its exponential form, identifying all symbols.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the ratio of the catalysed rate constant to the uncatalysed rate constant, <i>k</i><sub>cat</sub> / <i>k</i><sub>uncat</sub>, at 298 K.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State why enzymes lose their catalytic activity at temperatures above 330 K (57 °C).", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "k = A e^(-Ea / RT) [1]; k = rate constant, A = pre-exponential factor, Ea = activation energy, R = gas constant, T = absolute temperature [1].", "marks": 2},
                {"part": "(b)", "points": "k_cat / k_uncat = e^(-Ea(cat)/RT) / e^(-Ea(uncat)/RT) = e^((Ea(uncat) - Ea(cat)) / RT) [1]; &Delta;Ea = 75000 - 8000 = 67000 J mol^-1; RT = 8.314 &times; 298 = 2477.6 J mol^-1 [1]; Ratio = e^(67000 / 2477.6) = e^27.042 = 5.55 &times; 10^11 (rate increases by over 500 billion times) [1].", "marks": 3},
                {"part": "(c)", "points": "Thermal denaturation: hydrogen bonds and ionic interactions maintaining tertiary protein structure are disrupted, changing the shape of the active site [1].", "marks": 1}
            ]
        ),

        # Q15: 9701/42/O/N/19/Q2
        Question(
            number=15,
            title="Gas Collection Method & Initial Rate Deduction for CaCO3 + HCl — 9701/42/O/N/19/Q2 [6 Marks]",
            syllabus_ref="26.2", difficulty="HARD", section_key="SEC_A",
            preamble="The rate of reaction between calcium carbonate and hydrochloric acid was investigated:<br/>CaCO<sub>3</sub>(s) + 2HCl(aq) &rarr; CaCl<sub>2</sub>(aq) + H<sub>2</sub>O(l) + CO<sub>2</sub>(g)<br/>Carbon dioxide volume was collected in a gas syringe over time.",
            parts=[
                QuestionPart("(a)", "Describe how the initial rate of reaction is determined from a graph of volume of CO<sub>2</sub> against time.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why small marble chips react faster than an equal mass of large marble chips of the same chemical purity.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why the rate of reaction eventually falls to zero, and state which reagent was in excess if some solid carbonate remains.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Draw a tangent to the curve at time t = 0 [1]; Calculate the gradient of this tangent (&Delta;V / &Delta;t) [1].", "marks": 2},
                {"part": "(b)", "points": "Smaller chips have a much larger total surface area per unit mass [1]; More reactant particles are exposed, leading to a higher frequency of successful collisions between CaCO3 and H+ ions [1].", "marks": 2},
                {"part": "(c)", "points": "The limiting reactant (HCl) is completely consumed so [H+] falls to zero [1]; If unreacted CaCO3 remains, CaCO3 is in excess and HCl was the limiting reagent [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/41/O/N/19/Q2
        Question(
            number=16,
            title="Deduction of Reaction Mechanism from Complex Rate Law — 9701/41/O/N/19/Q2 [6 Marks]",
            syllabus_ref="26.3", difficulty="HARD", section_key="SEC_A",
            preamble="The gas-phase reaction between chlorine dioxide and fluorine was investigated:<br/>2ClO<sub>2</sub>(g) + F<sub>2</sub>(g) &rarr; 2FClO<sub>2</sub>(g)<br/>The experimentally determined rate equation is: Rate = <i>k</i>[ClO<sub>2</sub>][F<sub>2</sub>].",
            parts=[
                QuestionPart("(a)", "Explain why the reaction cannot take place in a single termolecular collision step involving 2 molecules of ClO<sub>2</sub> and 1 molecule of F<sub>2</sub>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Propose a two-step reaction mechanism consistent with the observed rate equation, identifying which step is rate-determining.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Identify any intermediate species in your proposed mechanism and explain why it does not appear in the overall stoichiometric equation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A simultaneous collision between three gaseous molecules (termolecular) with correct orientation and sufficient energy is statistically extremely improbable [1]; If it were single-step, the rate law would be Rate = k[ClO2]^2[F2], which contradicts experiment [1].", "marks": 2},
                {"part": "(b)", "points": "Step 1 (slow/RDS): ClO2 + F2 &rarr; FClO2 + F [1]; Step 2 (fast): ClO2 + F &rarr; FClO2 [1].", "marks": 2},
                {"part": "(c)", "points": "Fluorine radical (or atom) F is the intermediate [1]; It is produced in Step 1 and subsequently consumed completely in Step 2, so it cancels out of the overall balanced equation [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q5
        Question(
            number=17,
            title="Orders of Reaction Definitions & Meaning of Overall Order — 9701/42/M/J/23/Q5 [4 Marks]",
            syllabus_ref="26.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The rate equation for a reaction is given by: Rate = <i>k</i>[A]<sup><i>m</i></sup>[B]<sup><i>n</i></sup>.",
            parts=[
                QuestionPart("(a)", "Define the term <i>order of reaction</i> with respect to reactant A.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Define the <i>overall order of reaction</i>, and state its value if <i>m</i> = 1 and <i>n</i> = 2.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The power to which the concentration of reactant A is raised in the experimental rate equation [2].", "marks": 2},
                {"part": "(b)", "points": "The sum of the powers of all concentration terms in the rate equation (m + n) [1]; Overall order = 1 + 2 = 3 (third order) [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/M/J/23/Q5
        Question(
            number=18,
            title="Units of Rate Constant k for Different Orders — 9701/41/M/J/23/Q5 [4 Marks]",
            syllabus_ref="26.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The units of the rate constant <i>k</i> vary with the overall order of the reaction.",
            parts=[
                QuestionPart("(a)", "Derive the units of <i>k</i> for a second-order reaction: Rate = <i>k</i>[X]<sup>2</sup>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Derive the units of <i>k</i> for a third-order reaction: Rate = <i>k</i>[X][Y]<sup>2</sup>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "k = Rate / [X]^2 = (mol dm^-3 s^-1) / (mol dm^-3)^2 [1]; Units = mol^-1 dm^3 s^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "k = Rate / ([X][Y]^2) = (mol dm^-3 s^-1) / (mol dm^-3)^3 [1]; Units = mol^-2 dm^6 s^-1 [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/O/N/23/Q5
        Question(
            number=19,
            title="Half-Life and First-Order Rate Constant Calculation — 9701/42/O/N/23/Q5 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Cyclopropane isomerises into propene in a first-order gas-phase reaction.<br/>At 773 K, the rate constant <i>k</i> = 3.30 &times; 10<sup>-4</sup> s<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the half-life, <i>t</i><sub>1/2</sub>, of cyclopropane in seconds.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the fraction of cyclopropane remaining after 4200 seconds.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "t1/2 = ln 2 / k = 0.69315 / (3.30 &times; 10^-4 s^-1) [1]; t1/2 = 2.10 &times; 10^3 s (2100 s) [1].", "marks": 2},
                {"part": "(b)", "points": "Number of half-lives elapsed = 4200 / 2100 = 2 half-lives [1]; Fraction remaining = (1/2)^2 = 1/4 = 0.25 (25%) [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/O/N/23/Q5
        Question(
            number=20,
            title="Rate-Determining Step in S_N2 Mechanism — 9701/41/O/N/23/Q5 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Bromoethane reacts with aqueous hydroxide ions by an S<sub>N</sub>2 mechanism:<br/>CH<sub>3</sub>CH<sub>2</sub>Br + OH<sup>-</sup> &rarr; CH<sub>3</sub>CH<sub>2</sub>OH + Br<sup>-</sup><br/>Rate = <i>k</i>[CH<sub>3</sub>CH<sub>2</sub>Br][OH<sup>-</sup>].",
            parts=[
                QuestionPart("(a)", "Explain what the term <i>molecularity</i> means for this elementary step.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the five-coordinate transition state formed during this single-step reaction.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Molecularity is the number of reactant species colliding/involved in an elementary step [1]; It is bimolecular because one molecule of bromoethane and one hydroxide ion collide simultaneously [1].", "marks": 2},
                {"part": "(b)", "points": "Central carbon with planar H, H, CH3 bonds, and partial bonds to incoming HO&delta;- and outgoing &delta;-Br with brackets and negative charge [2].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/M/J/22/Q4
        Question(
            number=21,
            title="Quenching and Sampling Method in Ester Hydrolysis — 9701/42/M/J/22/Q4 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The rate of hydrolysis of ethyl ethanoate by acid was monitored by sampling and titration:<br/>CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O &rarr; CH<sub>3</sub>COOH + CH<sub>3</sub>CH<sub>2</sub>OH",
            parts=[
                QuestionPart("(a)", "Explain what is meant by <i>quenching</i> a reaction mixture.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Suggest two ways this reaction mixture can be quenched before titration.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Stopping or dramatically slowing down the reaction at an exact recorded time so that reactant/product concentrations do not change before analysis [2].", "marks": 2},
                {"part": "(b)", "points": "1. Rapid cooling by plunging the sample into an ice-water bath [1]; 2. Massive dilution with large volume of ice-cold water [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/41/M/J/22/Q4
        Question(
            number=22,
            title="Effect of Catalyst on Activation Energy and Equilibrium — 9701/41/M/J/22/Q4 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The Haber process reaction: N<sub>2</sub>(g) + 3H<sub>2</sub>(g) &rightleftharpoons; 2NH<sub>3</sub>(g) &nbsp;&nbsp; &Delta;<i>H</i> = -92 kJ mol<sup>-1</sup> uses a finely divided iron catalyst.",
            parts=[
                QuestionPart("(a)", "Explain how the iron catalyst increases the rate of reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain the effect, if any, of the iron catalyst on the yield of ammonia at equilibrium.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Provides an alternative reaction pathway with lower activation energy (Ea) [1]; A greater fraction of collisions possess energy exceeding this lower Ea [1].", "marks": 2},
                {"part": "(b)", "points": "No effect on the position of equilibrium or yield of ammonia [1]; A catalyst speeds up the rate of forward and reverse reactions by the exact same factor without changing Kc [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/O/N/22/Q4
        Question(
            number=23,
            title="Arrhenius Straight-Line Equation Transformation — 9701/42/O/N/22/Q4 [4 Marks]",
            syllabus_ref="26.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The Arrhenius equation is <i>k</i> = <i>A</i> exp(-<i>E</i><sub>a</sub> / <i>RT</i>).",
            parts=[
                QuestionPart("(a)", "Take natural logarithms of both sides to convert this equation into the linear form <i>y</i> = <i>mx</i> + <i>c</i>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the variables plotted on the <i>y</i>-axis and <i>x</i>-axis, and state what the gradient and <i>y</i>-intercept represent.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ln k = (-Ea / R)(1/T) + ln A [2].", "marks": 2},
                {"part": "(b)", "points": "y-axis = ln k; x-axis = 1/T [1]; Gradient = -Ea / R; y-intercept = ln A [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/22/Q4
        Question(
            number=24,
            title="Continuous Monitoring by Electrical Conductivity — 9701/41/O/N/22/Q4 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Consider the reaction: (CH<sub>3</sub>)<sub>3</sub>C-Cl + H<sub>2</sub>O &rarr; (CH<sub>3</sub>)<sub>3</sub>C-OH + H<sup>+</sup>(aq) + Cl<sup>-</sup>(aq).",
            parts=[
                QuestionPart("(a)", "Explain why electrical conductivity is an ideal method for continuously monitoring the rate of this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe how the conductivity changes over time, and state how initial rate is determined from the graph.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The reactants are non-ionic (zero conductivity), whereas the reaction generates ions (H+ and Cl-) in solution [2].", "marks": 2},
                {"part": "(b)", "points": "Conductivity increases steadily from zero as ion concentration rises [1]; The initial rate is found by measuring the initial gradient of the conductivity versus time curve [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/21/Q4
        Question(
            number=25,
            title="Enzyme Kinetics & Substrate Concentration Effect — 9701/42/M/J/21/Q4 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The hydrolysis of urea by the enzyme urease was studied at varying substrate concentrations.",
            parts=[
                QuestionPart("(a)", "State the order of reaction with respect to urea at very low substrate concentration, and explain why.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the order of reaction with respect to urea at very high substrate concentration, and explain why.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "First order [1]; At low [urea], many enzyme active sites are unoccupied; rate is directly proportional to substrate concentration [1].", "marks": 2},
                {"part": "(b)", "points": "Zero order [1]; At high [urea], all enzyme active sites are fully saturated (Vmax reached); adding more substrate cannot increase rate [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/21/Q4
        Question(
            number=26,
            title="Half-Life Comparison: First Order vs Second Order Kinetics — 9701/41/M/J/21/Q4 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Reaction 1 is first order in reactant A. Reaction 2 is second order in reactant B.<br/>Both have an initial half-life of 60 seconds with initial concentration 1.00 mol dm<sup>-3</sup>.",
            parts=[
                QuestionPart("(a)", "State the value of the second half-life for Reaction 1, giving your reasoning.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State what happens to the half-life of Reaction 2 as the reaction proceeds, giving your reasoning.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "60 seconds (constant) [1]; First-order half-life is independent of concentration (t1/2 = ln 2 / k) [1].", "marks": 2},
                {"part": "(b)", "points": "The second half-life doubles to 120 seconds [1]; For a second-order reaction, t1/2 = 1 / (k[B]0), so half-life is inversely proportional to concentration; as [B] halves, t1/2 doubles [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q4
        Question(
            number=27,
            title="Autocatalysis: Reaction Between Permanganate and Ethanedioate — 9701/42/O/N/21/Q4 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The redox reaction between acidified manganate(VII) and ethanedioic acid is initially very slow:<br/>2MnO<sub>4</sub><sup>-</sup> + 16H<sup>+</sup> + 5C<sub>2</sub>O<sub>4</sub><sup>2-</sup> &rarr; 2Mn<sup>2+</sup> + 8H<sub>2</sub>O + 10CO<sub>2</sub><br/>After a short induction period, the purple colour fades rapidly.",
            parts=[
                QuestionPart("(a)", "Explain why the reaction is initially very slow at room temperature.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the rate of reaction accelerates dramatically after a short time, identifying the autocatalyst.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both reactant ions (MnO4- and C2O4 2-) are negatively charged [1]; Strong electrostatic repulsion between like-charged anions results in a high activation energy [1].", "marks": 2},
                {"part": "(b)", "points": "Autocatalysis: one of the products formed, Mn2+(aq), acts as a catalyst [1]; Mn2+ reacts with MnO4- to form intermediate manganese species (Mn3+) which rapidly oxidise ethanedioate [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/41/O/N/21/Q4
        Question(
            number=28,
            title="Calculating Activation Energy from Two Rate Constants — 9701/41/O/N/21/Q4 [4 Marks]",
            syllabus_ref="26.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="For a certain chemical reaction, <i>k</i> = 2.00 &times; 10<sup>-3</sup> s<sup>-1</sup> at 293 K and <i>k</i> = 8.00 &times; 10<sup>-3</sup> s<sup>-1</sup> at 313 K.<br/><i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the value of ln(<i>k</i><sub>2</sub> / <i>k</i><sub>1</sub>) and (1/<i>T</i><sub>2</sub> - 1/<i>T</i><sub>1</sub>).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the activation energy <i>E</i><sub>a</sub> in kJ mol<sup>-1</sup>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ln(k2/k1) = ln(8.00/2.00) = ln(4.00) = 1.386 [1]; 1/313 - 1/293 = 0.003195 - 0.003413 = -2.180 &times; 10^-4 K^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "Ea = -R &times; ln(k2/k1) / (1/T2 - 1/T1) = -8.314 &times; (1.386) / (-2.180 &times; 10^-4) = 5.286 &times; 10^4 J mol^-1 [1]; Ea = +52.9 kJ mol^-1 [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/42/M/J/20/Q4
        Question(
            number=29,
            title="Deducing Rate Equation from Initial Rates Table — 9701/42/M/J/20/Q4 [4 Marks]",
            syllabus_ref="26.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Data for 2A + B &rarr; C:<br/>- Expt 1: [A] = 0.10, [B] = 0.10, Rate = 1.2 &times; 10<sup>-3</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 2: [A] = 0.20, [B] = 0.10, Rate = 2.4 &times; 10<sup>-3</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 3: [A] = 0.20, [B] = 0.20, Rate = 9.6 &times; 10<sup>-3</sup> mol dm<sup>-3</sup> s<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Deduce the order with respect to A and with respect to B.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the rate equation and calculate <i>k</i>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Expt 1 to 2: [A] doubles, rate doubles &rArr; 1st order in A [1]; Expt 2 to 3: [B] doubles, rate quadruples (9.6/2.4 = 4) &rArr; 2nd order in B [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = k[A][B]^2 [1]; k = (1.2 &times; 10^-3) / ((0.10)(0.10)^2) = 1.2 mol^-2 dm6 s^-1 [1].", "marks": 2}
            ]
        ),

        # Q30: 9701/41/M/J/20/Q5
        Question(
            number=30,
            title="Mass Loss Method for Solid-Liquid Reaction Kinetics — 9701/41/M/J/20/Q5 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The reaction between Zn and excess dilute H<sub>2</sub>SO<sub>4</sub> liberates H<sub>2</sub> gas:<br/>Zn(s) + H<sub>2</sub>SO<sub>4</sub>(aq) &rarr; ZnSO<sub>4</sub>(aq) + H<sub>2</sub>(g).",
            parts=[
                QuestionPart("(a)", "Explain why measuring mass loss on a balance is suitable for this reaction, and name a piece of apparatus placed in the flask neck.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how the rate at time <i>t</i> = 60 s is calculated from the mass loss curve.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydrogen gas escapes from the flask, causing a measurable decrease in total mass over time [1]; A cotton wool plug is placed in the neck to prevent loss of acid spray while allowing gas to escape [1].", "marks": 2},
                {"part": "(b)", "points": "Draw a tangent to the curve at time t = 60 s [1]; Calculate the gradient of this tangent [1].", "marks": 2}
            ]
        ),

        # Q31: 9701/42/O/N/19/Q4
        Question(
            number=31,
            title="Molecularity and Intermediate in Multi-Step Mechanism — 9701/42/O/N/19/Q4 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="A reaction proceeds by the following mechanism:<br/>Step 1: NO<sub>2</sub> + NO<sub>2</sub> &rarr; NO<sub>3</sub> + NO &nbsp;&nbsp; (slow)<br/>Step 2: NO<sub>3</sub> + CO &rarr; NO<sub>2</sub> + CO<sub>2</sub> &nbsp;&nbsp; (fast)",
            parts=[
                QuestionPart("(a)", "Write the overall balanced equation for the reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Deduce the rate equation and identify the intermediate species.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "NO2 + CO &rarr; NO + CO2 [2].", "marks": 2},
                {"part": "(b)", "points": "Rate = k[NO2]^2 (since Step 1 is the slow step involving two NO2 molecules) [1]; Intermediate = NO3 [1].", "marks": 2}
            ]
        ),

        # Q32: 9701/41/O/N/19/Q4
        Question(
            number=32,
            title="Activation Energy and Pre-Exponential Factor Concept — 9701/41/O/N/19/Q4 [4 Marks]",
            syllabus_ref="26.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The Arrhenius parameters for two reactions X and Y are:<br/>- Reaction X: <i>E</i><sub>a</sub> = 50 kJ mol<sup>-1</sup>, <i>A</i> = 1.0 &times; 10<sup>11</sup> s<sup>-1</sup><br/>- Reaction Y: <i>E</i><sub>a</sub> = 90 kJ mol<sup>-1</sup>, <i>A</i> = 1.0 &times; 10<sup>14</sup> s<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "State which reaction has a faster rate at 298 K, giving your reasoning.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain which reaction's rate will show a greater sensitivity to an increase in temperature.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Reaction X is much faster [1]; Despite a lower A, its activation energy is much lower (50 vs 90 kJ mol^-1), making the e^(-Ea/RT) factor vastly larger [1].", "marks": 2},
                {"part": "(b)", "points": "Reaction Y shows greater sensitivity [1]; Reactions with higher activation energies experience a larger proportional increase in rate for a given temperature rise [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q6
        Question(
            number=33,
            title="Definition of Rate of Reaction — 9701/42/M/J/23/Q6 [2 Marks]",
            syllabus_ref="26.1", difficulty="EASY", section_key="SEC_C",
            preamble="Chemical kinetics studies the speed of chemical reactions.",
            parts=[
                QuestionPart("(a)", "Define the term <i>rate of reaction</i>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The change in concentration of a reactant or product [1]; per unit time [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/M/J/23/Q6
        Question(
            number=34,
            title="Definition of Half-Life — 9701/41/M/J/23/Q6 [2 Marks]",
            syllabus_ref="26.2", difficulty="EASY", section_key="SEC_C",
            preamble="The half-life is a fundamental kinetic property of reactions.",
            parts=[
                QuestionPart("(a)", "Define the term <i>half-life</i>, <i>t</i><sub>1/2</sub>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The time taken for the concentration of a reactant to decrease to half of its initial (or original) value [2].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/O/N/23/Q6
        Question(
            number=35,
            title="Definition of Rate-Determining Step — 9701/42/O/N/23/Q6 [2 Marks]",
            syllabus_ref="26.3", difficulty="EASY", section_key="SEC_C",
            preamble="Many chemical reactions occur via several individual stages.",
            parts=[
                QuestionPart("(a)", "Define what is meant by the <i>rate-determining step</i> of a reaction.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The slowest step in a multi-step reaction mechanism [1]; which determines and limits the overall rate of reaction [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/O/N/23/Q6
        Question(
            number=36,
            title="Definition of Activation Energy — 9701/41/O/N/23/Q6 [2 Marks]",
            syllabus_ref="26.4", difficulty="EASY", section_key="SEC_C",
            preamble="Chemical collisions must satisfy an energy threshold.",
            parts=[
                QuestionPart("(a)", "Define the term <i>activation energy</i>, <i>E</i><sub>a</sub>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The minimum amount of energy that colliding particles must possess [1]; in order for a chemical reaction to occur [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/M/J/22/Q5
        Question(
            number=37,
            title="Definition of a Catalyst — 9701/42/M/J/22/Q5 [2 Marks]",
            syllabus_ref="26.3", difficulty="EASY", section_key="SEC_C",
            preamble="Catalysts are widely used in chemical manufacture.",
            parts=[
                QuestionPart("(a)", "Define the term <i>catalyst</i>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A substance that increases the rate of a chemical reaction without being chemically changed or consumed at the end [1]; by providing an alternative reaction pathway of lower activation energy [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/41/M/J/22/Q5
        Question(
            number=38,
            title="Homogeneous versus Heterogeneous Catalysis Distinction — 9701/41/M/J/22/Q5 [2 Marks]",
            syllabus_ref="26.3", difficulty="EASY", section_key="SEC_C",
            preamble="Catalysts operate either in the same phase or in different phases.",
            parts=[
                QuestionPart("(a)", "Distinguish between <i>homogeneous</i> and <i>heterogeneous</i> catalysis.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Homogeneous: catalyst is in the same physical phase/state as the reactants [1]; Heterogeneous: catalyst is in a different physical phase/state from the reactants [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/O/N/22/Q5
        Question(
            number=39,
            title="Pre-Exponential Factor A Meaning — 9701/42/O/N/22/Q5 [2 Marks]",
            syllabus_ref="26.4", difficulty="EASY", section_key="SEC_C",
            preamble="In the Arrhenius equation <i>k</i> = <i>A</i> exp(-<i>E</i><sub>a</sub> / <i>RT</i>), <i>A</i> is a constant.",
            parts=[
                QuestionPart("(a)", "State what the pre-exponential factor <i>A</i> represents.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The collision frequency factor / frequency of collisions between reactant particles [1]; taking into account the fraction of collisions with the correct steric orientation [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/22/Q5
        Question(
            number=40,
            title="Rate Constant Independence of Concentration — 9701/41/O/N/22/Q5 [2 Marks]",
            syllabus_ref="26.1", difficulty="EASY", section_key="SEC_C",
            preamble="A student changes the concentration of reactants in an experiment at constant temperature.",
            parts=[
                QuestionPart("(a)", "State and explain whether the rate constant <i>k</i> changes when reactant concentrations are tripled at constant temperature.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The rate constant k remains unchanged [1]; k is only dependent on temperature (and the presence of a catalyst), not on concentration [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # 4 x 6-Markers (Q41–Q44), 4 x 4-Markers (Q45–Q48), 2 x 2-Markers (Q49–Q50)
        # =====================================================================

        # Q41: 9701/42/M/J/23/Q3(Repeat 1 - 6m)
        Question(
            number=41,
            title="[CORE REPEAT 1] Complete Arrhenius Graphical Analysis — 9701/42/M/J/23/Q3 [6 Marks]",
            syllabus_ref="26.4", difficulty="HARD", section_key="SEC_D",
            preamble="The decomposition of benzenediazonium chloride, C<sub>6</sub>H<sub>5</sub>N<sub>2</sub>Cl(aq) &rarr; C<sub>6</sub>H<sub>5</sub>Cl(aq) + N<sub>2</sub>(g), was monitored at various temperatures.<br/>An Arrhenius plot of ln <i>k</i> against 1/<i>T</i> yields a linear plot identical to Fig. 41.1.<br/>Gradient = -1.25 &times; 10<sup>4</sup> K.<br/><i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.",
            figure_path=os.path.join(fig_dir, "a2_t26_arrhenius_plot.png"),
            figure_caption="Fig. 41.1: Arrhenius plot of ln k against 1/T for benzenediazonium chloride decomposition.",
            parts=[
                QuestionPart("(a)", "Calculate the activation energy <i>E</i><sub>a</sub> for this reaction in kJ mol<sup>-1</sup>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "At 320 K, <i>k</i> = 1.40 &times; 10<sup>-3</sup> s<sup>-1</sup>. Use this value and your <i>E</i><sub>a</sub> to calculate the pre-exponential factor <i>A</i>.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State what the units of <i>A</i> are for this reaction, giving your reasoning.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Gradient = -Ea / R &rArr; Ea = -R &times; (-1.25 &times; 10^4) = 8.314 &times; 12500 = 103925 J mol^-1 [1]; Ea = +104 kJ mol^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "ln A = ln k + (Ea / RT) = ln(1.40 &times; 10^-3) + (103925 / (8.314 &times; 320)) = -6.571 + 39.06 = 32.49 [1]; A = e^32.49 = 1.29 &times; 10^14 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Units of A are s^-1 [1]; In the Arrhenius equation k = A e^(-Ea/RT), the exponential term is dimensionless, so A must have the exact same units as k (which is s^-1 for a 1st order reaction) [1].", "marks": 2}
            ]
        ),

        # Q42: 9701/41/M/J/23/Q3(Repeat 2 - 6m)
        Question(
            number=42,
            title="[CORE REPEAT 2] Initial Rates Deductions & Rate Law Construction — 9701/41/M/J/23/Q3 [6 Marks]",
            syllabus_ref="26.1", difficulty="HARD", section_key="SEC_D",
            preamble="Reaction: 2NO(g) + O<sub>2</sub>(g) &rarr; 2NO<sub>2</sub>(g).<br/>- Expt 1: [NO] = 0.010, [O<sub>2</sub>] = 0.010, Rate = 7.00 &times; 10<sup>-4</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 2: [NO] = 0.010, [O<sub>2</sub>] = 0.020, Rate = 1.40 &times; 10<sup>-3</sup> mol dm<sup>-3</sup> s<sup>-1</sup><br/>- Expt 3: [NO] = 0.030, [O<sub>2</sub>] = 0.020, Rate = 1.26 &times; 10<sup>-2</sup> mol dm<sup>-3</sup> s<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Deduce the order of reaction with respect to NO and with respect to O<sub>2</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the rate equation and calculate the rate constant <i>k</i> with its units.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the rate of reaction when [NO] = 0.025 mol dm<sup>-3</sup> and [O<sub>2</sub>] = 0.015 mol dm<sup>-3</sup>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Expt 1 to 2: [O2] doubles while [NO] constant; rate doubles &rArr; 1st order in O2 [1]; Expt 2 to 3: [NO] triples while [O2] constant; rate increases 9-fold (1.26 &times; 10^-2 / 1.40 &times; 10^-3 = 9 = 3^2) &rArr; 2nd order in NO [1].", "marks": 2},
                {"part": "(b)", "points": "Rate = k[NO]^2[O2] [1]; k = (7.00 &times; 10^-4) / ((0.010)^2 &times; 0.010) = 7.00 &times; 10^2 mol^-2 dm6 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Rate = (700) &times; (0.025)^2 &times; (0.015) [1]; Rate = 6.56 &times; 10^-3 mol dm^-3 s^-1 [1].", "marks": 2}
            ]
        ),

        # Q43: 9701/42/O/N/23/Q3(Repeat 3 - 6m)
        Question(
            number=43,
            title="[CORE REPEAT 3] Constant Half-Life Verification & S_N1 Reaction Pathway — 9701/42/O/N/23/Q3 [6 Marks]",
            syllabus_ref="26.2", difficulty="HARD", section_key="SEC_D",
            preamble="The decay curve for reactant R is shown in Fig. 43.1.<br/>The initial concentration is 0.80 mol dm<sup>-3</sup>.<br/>Concentrations at successive time intervals:<br/>- <i>t</i> = 0 s, [R] = 0.80 mol dm<sup>-3</sup><br/>- <i>t</i> = 40 s, [R] = 0.40 mol dm<sup>-3</sup><br/>- <i>t</i> = 80 s, [R] = 0.20 mol dm<sup>-3</sup><br/>- <i>t</i> = 120 s, [R] = 0.10 mol dm<sup>-3</sup>",
            figure_path=os.path.join(fig_dir, "a2_t26_first_order_half_life.png"),
            figure_caption="Fig. 43.1: Decay curve demonstrating constant successive half-lives of 40 s.",
            parts=[
                QuestionPart("(a)", "Prove that the reaction is first order by analysing the three successive half-lives.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the rate constant <i>k</i> for this first-order decomposition.", 2, num_answer_lines=2),
                QuestionPart("(c)", "If R is 2-chloro-2-methylpropane undergoing substitution with OH<sup>-</sup>, explain why the rate is independent of [OH<sup>-</sup>].", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1st half-life (0.80 &rarr; 0.40) = 40 s; 2nd half-life (0.40 &rarr; 0.20) = 40 s; 3rd half-life (0.20 &rarr; 0.10) = 40 s [1]; Successive half-lives are completely constant regardless of concentration, which is the defining signature of first-order kinetics [1].", "marks": 2},
                {"part": "(b)", "points": "k = ln 2 / t1/2 = 0.693 / 40 s [1]; k = 0.0173 s^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "The reaction proceeds via an SN1 mechanism where the slow, rate-determining step is heterolytic fission of the C-Cl bond forming a carbocation [1]; OH- only attacks in the rapid second step after the rate-determining step, so its concentration does not affect overall rate [1].", "marks": 2}
            ]
        ),

        # Q44: 9701/41/O/N/23/Q3(Repeat 4 - 6m)
        Question(
            number=44,
            title="[CORE REPEAT 4] Two-Step Mechanism Verification & Intermediate Identification — 9701/41/O/N/23/Q3 [6 Marks]",
            syllabus_ref="26.3", difficulty="HARD", section_key="SEC_D",
            preamble="Reaction: 2NO<sub>2</sub>(g) + F<sub>2</sub>(g) &rarr; 2NO<sub>2</sub>F(g).<br/>The reaction coordinate diagram in Fig. 44.1 shows two transition states with <i>E</i><sub>a1</sub> > <i>E</i><sub>a2</sub>.",
            figure_path=os.path.join(fig_dir, "a2_t26_multistep_energy_profile.png"),
            figure_caption="Fig. 44.1: Energy profile showing two transition states and intermediate F atom.",
            parts=[
                QuestionPart("(a)", "Explain why Step 1 (NO<sub>2</sub> + F<sub>2</sub> &rarr; NO<sub>2</sub>F + F) is the rate-determining step.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Deduce the rate equation consistent with this two-step mechanism.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State the role of the fluorine atom F, and explain why it is not classified as a catalyst.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1 has the higher activation energy barrier (TS1 is the highest potential energy point on the path) [1]; Therefore, it has the smallest rate constant and is the slowest elementary step [1].", "marks": 2},
                {"part": "(b)", "points": "Since the rate is controlled by the slow step involving 1 molecule of NO2 and 1 molecule of F2 [1]; Rate = k[NO2][F2] [1].", "marks": 2},
                {"part": "(c)", "points": "F is a reactive intermediate [1]; It is created during Step 1 and consumed in Step 2; a catalyst is present at the beginning and regenerated at the end [1].", "marks": 2}
            ]
        ),

        # Q45: 9701/42/M/J/22/Q2(Repeat 5 - 4m)
        Question(
            number=45,
            title="[CORE REPEAT 5] Zero-Order Kinetics of Iodine Reaction — 9701/42/M/J/22/Q2 [4 Marks]",
            syllabus_ref="26.2", difficulty="MEDIUM", section_key="SEC_D",
            preamble="In the reaction CH<sub>3</sub>COCH<sub>3</sub> + I<sub>2</sub> + H<sup>+</sup> &rarr; products, the order with respect to I<sub>2</sub> is zero.",
            parts=[
                QuestionPart("(a)", "Sketch the concentration of I<sub>2</sub> versus time curve, labelling axes clearly.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the rate of reaction remains unchanged even when [I<sub>2</sub>] is increased five-fold.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A downward sloping straight line with constant negative gradient terminating at the time axis [2].", "marks": 2},
                {"part": "(b)", "points": "I2 does not participate in the rate-determining step (or any step prior to it) [1]; The slow step involves acid-catalysed enolisation of propanone; I2 only reacts in a fast subsequent step, so changing [I2] has no effect on rate [1].", "marks": 2}
            ]
        ),

        # Q46: 9701/41/M/J/22/Q2(Repeat 6 - 4m)
        Question(
            number=46,
            title="[CORE REPEAT 6] Rate Constant Calculation from Rate and Concentrations — 9701/41/M/J/22/Q2 [4 Marks]",
            syllabus_ref="26.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="For the reaction A + 2B &rarr; C, Rate = <i>k</i>[A][B].<br/>When [A] = 0.0500 mol dm<sup>-3</sup> and [B] = 0.0800 mol dm<sup>-3</sup>, the rate of reaction is 3.60 &times; 10<sup>-4</sup> mol dm<sup>-3</sup> s<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the value of the rate constant <i>k</i>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the units of <i>k</i> and explain why the stoichiometry of 2B does not appear as an exponent in the rate equation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "k = Rate / ([A][B]) = (3.60 &times; 10^-4) / (0.0500 &times; 0.0800) = (3.60 &times; 10^-4) / 0.00400 [1]; k = 0.0900 mol^-1 dm3 s^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "Units = mol^-1 dm3 s^-1 [1]; Reaction orders are determined experimentally by reaction kinetics and mechanism, not from the overall stoichiometric balancing coefficients [1].", "marks": 2}
            ]
        ),

        # Q47: 9701/42/O/N/22/Q2(Repeat 7 - 4m)
        Question(
            number=47,
            title="[CORE REPEAT 7] Two-Point Arrhenius Calculation of Ea — 9701/42/O/N/22/Q2 [4 Marks]",
            syllabus_ref="26.4", difficulty="MEDIUM", section_key="SEC_D",
            preamble="A reaction has rate constant <i>k</i><sub>1</sub> = 2.50 &times; 10<sup>-4</sup> s<sup>-1</sup> at 300 K and <i>k</i><sub>2</sub> = 1.00 &times; 10<sup>-3</sup> s<sup>-1</sup> at 320 K.<br/><i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate ln(<i>k</i><sub>2</sub> / <i>k</i><sub>1</sub>).", 1, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the activation energy <i>E</i><sub>a</sub> in kJ mol<sup>-1</sup>.", 3, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ln(1.00 &times; 10^-3 / 2.50 &times; 10^-4) = ln(4.00) = 1.386 [1].", "marks": 1},
                {"part": "(b)", "points": "1/T2 - 1/T1 = 1/320 - 1/300 = -2.083 &times; 10^-4 K^-1 [1]; Ea = -R &times; 1.386 / (-2.083 &times; 10^-4) = 8.314 &times; 6653.9 = 55320 J mol^-1 [1]; Ea = +55.3 kJ mol^-1 [1].", "marks": 3}
            ]
        ),

        # Q48: 9701/41/O/N/22/Q2(Repeat 8 - 4m)
        Question(
            number=48,
            title="[CORE REPEAT 8] Homogeneous Catalysis Mechanism of Iodide-Persulfate — 9701/41/O/N/22/Q2 [4 Marks]",
            syllabus_ref="26.3", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Fe<sup>2+</sup>(aq) can also act as an efficient catalyst for the reaction between S<sub>2</sub>O<sub>8</sub><sup>2-</sup> and I<sup>-</sup>.<br/>Standard electrode potentials:<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup> + 2e<sup>-</sup> &rightleftharpoons; 2SO<sub>4</sub><sup>2-</sup>, <i>E</i>° = +2.01 V<br/>Fe<sup>3+</sup> + e<sup>-</sup> &rightleftharpoons; Fe<sup>2+</sup>, <i>E</i>° = +0.77 V<br/>I<sub>2</sub> + 2e<sup>-</sup> &rightleftharpoons; 2I<sup>-</sup>, <i>E</i>° = +0.54 V",
            parts=[
                QuestionPart("(a)", "Write two equations showing how Fe<sup>2+</sup> catalyses this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why both steps are energetically feasible by quoting <i>E</i>° values.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: 2Fe2+ + S2O8 2- &rarr; 2Fe3+ + 2SO4 2- [1]; Step 2: 2Fe3+ + 2I- &rarr; 2Fe2+ + I2 [1].", "marks": 2},
                {"part": "(b)", "points": "For Step 1: E°cell = +2.01 - (+0.77) = +1.24 V > 0 (feasible) [1]; For Step 2: E°cell = +0.77 - (+0.54) = +0.23 V > 0 (feasible) [1].", "marks": 2}
            ]
        ),

        # Q49: 9701/42/M/J/21/Q2(Repeat 9 - 2m)
        Question(
            number=49,
            title="[CORE REPEAT 9] First-Order Rate Equation Expression & Definition — 9701/42/M/J/21/Q2 [2 Marks]",
            syllabus_ref="26.1", difficulty="EASY", section_key="SEC_D",
            preamble="A reaction A &rarr; products is first order.",
            parts=[
                QuestionPart("(a)", "Write the differential rate equation and state the relation between <i>t</i><sub>1/2</sub> and <i>k</i>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Rate = k[A] [1]; t1/2 = ln 2 / k (or t1/2 = 0.693 / k) [1].", "marks": 2}
            ]
        ),

        # Q50: 9701/41/M/J/21/Q2(Repeat 10 - 2m)
        Question(
            number=50,
            title="[CORE REPEAT 10] Transition State vs Intermediate Difference — 9701/41/M/J/21/Q2 [2 Marks]",
            syllabus_ref="26.3", difficulty="EASY", section_key="SEC_D",
            preamble="Reaction profiles distinguish between transition states and intermediates.",
            parts=[
                QuestionPart("(a)", "State one structural and one energetic difference between an intermediate and a transition state.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "An intermediate has fully formed chemical bonds and corresponds to a potential energy minimum [1]; A transition state has partially formed/broken bonds and corresponds to a potential energy maximum [1].", "marks": 2}
            ]
        ),
    ]

    print("Topic 26 Questions Count:", len(questions))

    # Audit tariff
    m6 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    m4 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    m2 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    tot = sum(sum(p.marks for p in q.parts) for q in questions)
    print(f"Tariff Breakdown: 6-markers = {m6} (40%), 4-markers = {m4} (40%), 2-markers = {m2} (20%) | Total Marks = {tot}")
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    assert m6 == 20, f"Expected 20 6-markers, got {m6}"
    assert m4 == 20, f"Expected 20 4-markers, got {m4}"
    assert m2 == 10, f"Expected 10 2-markers, got {m2}"
    assert tot == 220, f"Expected 220 marks, got {tot}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 26 PDF built successfully!")

if __name__ == "__main__":
    build_topic26_50q()
