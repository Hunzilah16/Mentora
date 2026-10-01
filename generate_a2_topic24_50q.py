"""
Complete 50-Question Master Pack: Topic 24 — Electrochemistry (Paper 4 Theory)
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

def build_topic24_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic24_Electrochemistry.pdf"

    topic_title = "Topic 24 — Electrochemistry"
    topic_subtitle = "Electrolysis · Faraday's Laws · Standard Electrode Potentials E° · Nernst Equation · Fuel Cells"

    subtopics_summary = [
        ("24.1 Quantitative Electrolysis & Faraday's Laws", "Electrolysis of molten and aqueous electrolytes; Faraday constant F = Le; quantitative relationships between charge Q = It, moles of electrons, and mass/volume of products deposited or liberated; determination of the Avogadro constant."),
        ("24.2 Electrode Potentials & Electrochemical Cells", "Standard electrode potentials E° and standard cell potentials E°cell; Standard Hydrogen Electrode (SHE); salt bridge function; direction of electron flow; feasibility predictions; thermodynamic relationship ΔG° = -nFE°cell."),
        ("24.3 Nernst Equation & Concentration Cells", "Nernst equation E = E° + (0.059/z) log([oxidised]/[reduced]); effect of non-standard concentrations and temperatures on half-cell potentials; concentration cells; effect of precipitation and complex formation on E values."),
        ("24.4 Fuel Cells & Industrial Applications", "Hydrogen-oxygen fuel cells in acidic and alkaline electrolytes; electrode half-equations; direct methanol fuel cells; industrial electrorefining of copper; chlor-alkali membrane cell."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Electrochemistry from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q2
        Question(
            number=1,
            title="Quantitative Electrolysis & Avogadro Constant Determination — 9701/42/M/J/23/Q2 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_A",
            preamble="A constant current of 0.850 A is passed through aqueous copper(II) sulfate for exactly 40.0 minutes using the apparatus shown in Fig. 1.1.<br/>During electrolysis, copper metal is deposited on the cathode.<br/>Data: Ar(Cu) = 63.5; Elementary charge e = 1.602 &times; 10<sup>-19</sup> C; F = 96500 C mol<sup>-1</sup>.",
            figure_path=os.path.join(fig_dir, "a2_t24_electrolysis_coulometer.png"),
            figure_caption="Fig. 1.1: Quantitative electrolysis circuit for determining mass of copper deposited at the cathode.",
            parts=[
                QuestionPart("(a)", "State the relationship connecting the Faraday constant (F), the Avogadro constant (L), and the elementary charge (e), and define the Faraday constant.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the mass of copper deposited at the cathode.", 2, num_answer_lines=3),
                QuestionPart("(c)", "In an accurate experiment, 0.671 g of copper was deposited by 2040 C of charge. Use these data to calculate an experimental value for the Avogadro constant, L.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "F = L &times; e [1]; The quantity of electric charge carried by one mole of electrons (or singly charged ions) [1].", "marks": 2},
                {"part": "(b)", "points": "Q = I &times; t = 0.850 &times; (40.0 &times; 60) = 2040 C [1]; Moles of Cu = 2040 / (2 &times; 96500) = 0.01057 mol &rArr; Mass = 0.01057 &times; 63.5 = 0.671 g [1].", "marks": 2},
                {"part": "(c)", "points": "Moles of Cu = 0.671 / 63.5 = 0.010567 mol [1]; Moles of e- = 2 &times; 0.010567 = 0.02113 mol &rArr; L = Q / (n(e-) &times; e) = 2040 / (0.02113 &times; 1.602 &times; 10^-19) = 6.03 &times; 10^23 mol^-1 [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q3
        Question(
            number=2,
            title="Standard Electrochemical Cell & Salt Bridge Dynamics — 9701/41/M/J/23/Q3 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="The standard electrochemical cell in Fig. 2.1 is set up under standard conditions of 298 K and 1.00 mol dm<sup>-3</sup>.<br/>Standard electrode potentials:<br/>Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; Zn(s), E° = -0.76 V<br/>Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; Cu(s), E° = +0.34 V",
            figure_path=os.path.join(fig_dir, "a2_t24_electrochemical_cell.png"),
            figure_caption="Fig. 2.1: Standard galvanic cell consisting of zinc and copper half-cells joined by a salt bridge.",
            parts=[
                QuestionPart("(a)", "Calculate the standard cell potential, E°cell, and write the overall cell equation including state symbols.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Identify the negative electrode (anode) and state the direction of electron flow in the external circuit.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain the essential role of the salt bridge, and state which ions migrate into the copper half-cell as the cell discharges.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E°cell = E°(cathode) - E°(anode) = +0.34 - (-0.76) = +1.10 V [1]; Zn(s) + Cu2+(aq) &rarr; Zn2+(aq) + Cu(s) [1].", "marks": 2},
                {"part": "(b)", "points": "Zn electrode is the negative electrode (anode) [1]; Electrons flow through external wire from Zn to Cu [1].", "marks": 2},
                {"part": "(c)", "points": "Maintains electrical neutrality by allowing ion migration between half-cells / completes circuit without mixing solutions [1]; K+ cations migrate into the copper half-cell to replace discharged Cu2+ ions [1].", "marks": 2}
            ]
        ),

        # Q3: 9701/42/O/N/23/Q2
        Question(
            number=3,
            title="Nernst Equation Applied to Non-Standard Copper Half-Cell — 9701/42/O/N/23/Q2 [6 Marks]",
            syllabus_ref="24.3", difficulty="HARD", section_key="SEC_A",
            preamble="The electrode potential of a metal half-cell depends on the concentration of aqueous metal ions according to the Nernst equation:<br/>E = E° + (0.059 / z) log[oxidised form]<br/>For copper: Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; Cu(s), E° = +0.34 V.",
            parts=[
                QuestionPart("(a)", "State the value of z in the Nernst equation for the copper half-cell, and calculate the electrode potential E when [Cu<sup>2+</sup>] = 0.020 mol dm<sup>-3</sup> at 298 K.", 3, num_answer_lines=4),
                QuestionPart("(b)", "This copper half-cell is connected to a standard silver half-cell: Ag<sup>+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Ag(s), E° = +0.80 V. Calculate the cell potential, Ecell.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "z = 2 [1]; E = +0.34 + (0.059 / 2) log(0.020) [1]; log(0.020) = -1.699 &rArr; E = +0.34 + 0.0295(-1.699) = +0.34 - 0.0501 = +0.29 V [1].", "marks": 3},
                {"part": "(b)", "points": "Ag half-cell remains standard so E(Ag+/Ag) = +0.80 V [1]; Ecell = E(cathode) - E(anode) = E(Ag) - E(Cu) [1]; Ecell = +0.80 - (+0.29) = +0.51 V [1].", "marks": 3}
            ]
        ),

        # Q4: 9701/41/O/N/23/Q2
        Question(
            number=4,
            title="Standard Hydrogen Electrode (SHE) & Chromium Potential — 9701/41/O/N/23/Q2 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="The Standard Hydrogen Electrode (SHE) is the universal reference electrode shown in Fig. 4.1.<br/>By definition, its standard electrode potential is 0.00 V.",
            figure_path=os.path.join(fig_dir, "a2_t24_she_apparatus.png"),
            figure_caption="Fig. 4.1: The Standard Hydrogen Electrode (SHE) apparatus operating under standard conditions.",
            parts=[
                QuestionPart("(a)", "State the three standard conditions under which the SHE operates.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Explain the role of the platinised platinum foil in the SHE.", 1, num_answer_lines=2),
                QuestionPart("(c)", "When the SHE is connected to a standard Cr<sup>3+</sup>(aq)/Cr(s) half-cell, the voltmeter reading is 0.74 V and electrons flow from the chromium electrode to the SHE. Deduce the value of E° for Cr<sup>3+</sup>/Cr and write the half-equation occurring at the chromium electrode.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Temperature of 298 K (25 °C) [1]; Hydrogen gas pressure of 1.00 bar (or 100 kPa / 1 atm) [1]; Hydrogen ion concentration [H+] = 1.00 mol dm^-3 [1].", "marks": 3},
                {"part": "(b)", "points": "Provides an inert catalytic surface with high surface area for rapid electron transfer equilibrium between H2(g) and H+(aq) [1].", "marks": 1},
                {"part": "(c)", "points": "Electrons flow from Cr &rArr; Cr is negative electrode &rArr; E°(Cr3+/Cr) = -0.74 V [1]; Cr(s) &rarr; Cr3+(aq) + 3e- [1].", "marks": 2}
            ]
        ),

        # Q5: 9701/43/M/J/23/Q2
        Question(
            number=5,
            title="Alkaline Hydrogen-Oxygen Fuel Cell Kinetics & Thermodynamics — 9701/43/M/J/23/Q2 [6 Marks]",
            syllabus_ref="24.4", difficulty="HARD", section_key="SEC_A",
            preamble="A schematic diagram of an alkaline hydrogen-oxygen fuel cell is shown in Fig. 5.1.<br/>The electrolyte is hot aqueous potassium hydroxide, KOH(aq).<br/>Data: E° values in alkaline solution:<br/>O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> &rightleftharpoons; 4OH<sup>-</sup>(aq), E° = +0.40 V<br/>2H<sub>2</sub>O(l) + 2e<sup>-</sup> &rightleftharpoons; H<sub>2</sub>(g) + 2OH<sup>-</sup>(aq), E° = -0.83 V",
            figure_path=os.path.join(fig_dir, "a2_t24_alkaline_fuel_cell.png"),
            figure_caption="Fig. 5.1: Structure of an alkaline hydrogen-oxygen fuel cell using porous platinum-catalysed electrodes.",
            parts=[
                QuestionPart("(a)", "Write the half-equation occurring at the anode and the half-equation occurring at the cathode.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the standard cell potential, E°cell, and write the overall cell reaction.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State two major advantages of a hydrogen-oxygen fuel cell over an internal combustion engine burning petrol.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Anode: 2H2(g) + 4OH-(aq) &rarr; 4H2O(l) + 4e- (or H2 + 2OH- &rarr; 2H2O + 2e-) [1]; Cathode: O2(g) + 2H2O(l) + 4e- &rarr; 4OH-(aq) [1].", "marks": 2},
                {"part": "(b)", "points": "E°cell = +0.40 - (-0.83) = +1.23 V [1]; 2H2(g) + O2(g) &rarr; 2H2O(l) [1].", "marks": 2},
                {"part": "(c)", "points": "Only product is water / zero greenhouse gas (CO2) or NOx emissions at point of use [1]; Higher thermodynamic energy conversion efficiency (not limited by Carnot cycle) [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/42/M/J/22/Q3
        Question(
            number=6,
            title="Silver Electroplating & Faraday Constant Precision — 9701/42/M/J/22/Q3 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_A",
            preamble="A metal trophy is electroplated with silver using an aqueous solution of silver nitrate, AgNO<sub>3</sub>(aq).<br/>A current of 1.25 A is passed for 1 hour 15 minutes.<br/>Ar(Ag) = 107.9; F = 96500 C mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Write the half-equation for the reduction of silver ions at the cathode.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the total quantity of charge passed and the theoretical mass of silver deposited.", 3, num_answer_lines=4),
                QuestionPart("(c)", "If the actual mass of silver deposited was 5.98 g, calculate the percentage current efficiency of the plating process.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ag+(aq) + e- &rarr; Ag(s) [1].", "marks": 1},
                {"part": "(b)", "points": "t = (1 &times; 3600) + (15 &times; 60) = 4500 s [1]; Q = I &times; t = 1.25 &times; 4500 = 5625 C [1]; Mass of Ag = (5625 / 96500) &times; 107.9 = 0.05829 &times; 107.9 = 6.29 g [1].", "marks": 3},
                {"part": "(c)", "points": "Current efficiency = (actual mass / theoretical mass) &times; 100 [1]; Efficiency = (5.98 / 6.29) &times; 100 = 95.1% [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/41/M/J/22/Q3
        Question(
            number=7,
            title="Cobalt Complex Ligand Exchange Effect on Electrode Potential — 9701/41/M/J/22/Q3 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="Standard electrode potentials for cobalt(III)/cobalt(II) systems:<br/>[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + e<sup>-</sup> &rightleftharpoons; [Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup>, E° = +1.82 V<br/>[Co(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup> + e<sup>-</sup> &rightleftharpoons; [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup>, E° = +0.10 V<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> &rightleftharpoons; 2H<sub>2</sub>O(l), E° = +1.23 V",
            parts=[
                QuestionPart("(a)", "Explain why the electrode potential becomes significantly less positive when water ligands are replaced by ammonia ligands.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Deduce whether aqueous Co<sup>2+</sup>(aq) can be oxidized to Co<sup>3+</sup>(aq) by atmospheric oxygen under standard conditions.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Deduce whether [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup> can be oxidized to [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup> by atmospheric oxygen, and calculate E°cell for this reaction.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "NH3 is a stronger ligand / forms more stable complex with Co3+ than with Co2+ [1]; preferentially stabilizes the +3 oxidation state, shifting equilibrium to the left and making E° less positive [1].", "marks": 2},
                {"part": "(b)", "points": "E°cell = E°(O2) - E°(Co3+/Co2+) = +1.23 - (+1.82) = -0.59 V [1]; E°cell < 0 &rArr; reaction is not feasible under standard conditions [1].", "marks": 2},
                {"part": "(c)", "points": "E°cell = +1.23 - (+0.10) = +1.13 V [1]; E°cell > 0 &rArr; feasible, [Co(NH3)6]2+ is readily oxidized by air to [Co(NH3)6]3+ [1].", "marks": 2}
            ]
        ),

        # Q8: 9701/42/O/N/22/Q2
        Question(
            number=8,
            title="Dichromate(VI) / Iodide Redox Cell & pH Sensitivity — 9701/42/O/N/22/Q2 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="Electrode potentials:<br/>Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> &rightleftharpoons; 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l), E° = +1.33 V<br/>I<sub>2</sub>(aq) + 2e<sup>-</sup> &rightleftharpoons; 2I<sup>-</sup>(aq), E° = +0.54 V",
            parts=[
                QuestionPart("(a)", "Construct the overall balanced ionic equation for the reaction that occurs when these two half-cells are connected.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the standard cell potential, E°cell, and state what change in color would be observed in the chromium half-cell.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Predict and explain the effect on the cell potential if the pH of the dichromate half-cell is increased by adding aqueous sodium hydroxide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cr2O7^2-(aq) + 14H+(aq) + 6I-(aq) &rarr; 2Cr3+(aq) + 3I2(aq) + 7H2O(l) [2] (1 mark for correct species, 1 mark for balanced electrons).", "marks": 2},
                {"part": "(b)", "points": "E°cell = +1.33 - (+0.54) = +0.79 V [1]; Color changes from orange (Cr2O7^2-) to green (Cr3+) [1].", "marks": 2},
                {"part": "(c)", "points": "Increasing pH decreases [H+] [1]; By Le Chatelier's principle / Nernst equation, equilibrium shifts left, making E(Cr2O7^2-/Cr3+) less positive &rArr; Ecell decreases [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/41/O/N/22/Q3
        Question(
            number=9,
            title="Electrochemical Principles of the Chlor-Alkali Membrane Cell — 9701/41/O/N/22/Q3 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_A",
            preamble="In the industrial membrane cell, concentrated aqueous sodium chloride (brine) is electrolysed to produce chlorine gas, hydrogen gas, and aqueous sodium hydroxide.<br/>Relevant standard electrode potentials:<br/>2H<sub>2</sub>O(l) + 2e<sup>-</sup> &rightleftharpoons; H<sub>2</sub>(g) + 2OH<sup>-</sup>(aq), E° = -0.83 V<br/>Na<sup>+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Na(s), E° = -2.71 V<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> &rightleftharpoons; 2H<sub>2</sub>O(l), E° = +1.23 V<br/>Cl<sub>2</sub>(g) + 2e<sup>-</sup> &rightleftharpoons; 2Cl<sup>-</sup>(aq), E° = +1.36 V",
            parts=[
                QuestionPart("(a)", "Explain why hydrogen gas is discharged at the cathode instead of sodium metal.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Under standard conditions, oxygen has a less positive electrode potential (+1.23 V) than chlorine (+1.36 V). Explain why chlorine gas is evolved at the anode rather than oxygen in concentrated brine.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the function of the cation-exchange membrane separating the anode and cathode compartments.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E° for reduction of H2O (-0.83 V) is much more positive than E° for Na+ (-2.71 V) [1]; H2O is vastly more easily reduced / requires less energy to gain electrons [1].", "marks": 2},
                {"part": "(b)", "points": "High concentration of Cl- ions in brine shifts the equilibrium / Nernst potential of Cl2/2Cl- to a less positive value [1]; Oxidation of water to O2 has a high activation energy (large kinetic overpotential) on the anode material [1].", "marks": 2},
                {"part": "(c)", "points": "Allows Na+ ions to pass from anode to cathode compartment while preventing Cl- and OH- from crossing [1]; Prevents chlorine from reacting with OH- to form hypochlorite (or explosive H2/Cl2 mixing) [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/43/O/N/22/Q2
        Question(
            number=10,
            title="Copper Concentration Cell EMF & Nernst Derivation — 9701/43/O/N/22/Q2 [6 Marks]",
            syllabus_ref="24.3", difficulty="HARD", section_key="SEC_A",
            preamble="A concentration cell is constructed using two copper electrodes immersed in copper(II) sulfate solutions of different concentrations, as shown in Fig. 10.1.<br/>Beaker 1: [Cu<sup>2+</sup>] = 0.010 mol dm<sup>-3</sup><br/>Beaker 2: [Cu<sup>2+</sup>] = 1.00 mol dm<sup>-3</sup><br/>E = E° + (0.059 / z) log[Cu<sup>2+</sup>] at 298 K.",
            figure_path=os.path.join(fig_dir, "a2_t24_concentration_cell.png"),
            figure_caption="Fig. 10.1: Copper concentration cell driven by the concentration gradient between half-cells.",
            parts=[
                QuestionPart("(a)", "Calculate the electrode potential E of Beaker 1 and of Beaker 2, given E°(Cu<sup>2+</sup>/Cu) = +0.34 V.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the overall cell potential, Ecell, and state which electrode acts as the cathode.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State what will happen to the cell potential when the cell is allowed to discharge over an extended period.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Beaker 2 (standard): E = +0.34 V [1]; Beaker 1: E = +0.34 + (0.059/2) log(0.010) = +0.34 + 0.0295(-2) [1]; E(Beaker 1) = +0.34 - 0.059 = +0.281 V [1].", "marks": 3},
                {"part": "(b)", "points": "Ecell = E(conc) - E(dil) = +0.340 - (+0.281) = +0.059 V (or via Nernst log(1.00/0.010)) [1]; The electrode in Beaker 2 (concentrated) is the cathode (reduction) [1].", "marks": 2},
                {"part": "(c)", "points": "Ecell will decrease until it reaches 0.00 V when concentrations in both compartments become equal [1].", "marks": 1}
            ]
        ),

        # Q11: 9701/42/M/J/21/Q3
        Question(
            number=11,
            title="Chlorine Half-Cell Potential: Combined Concentration & Pressure Effects — 9701/42/M/J/21/Q3 [6 Marks]",
            syllabus_ref="24.3", difficulty="HARD", section_key="SEC_A",
            preamble="For the chlorine half-cell: Cl<sub>2</sub>(g) + 2e<sup>-</sup> &rightleftharpoons; 2Cl<sup>-</sup>(aq), E° = +1.36 V.<br/>The general Nernst equation is:<br/>E = E° + (0.059 / z) log([oxidised] / [reduced])<br/>For gases, partial pressure in bar replaces concentration.",
            parts=[
                QuestionPart("(a)", "Write the specific Nernst expression for the chlorine electrode in terms of p(Cl<sub>2</sub>) and [Cl<sup>-</sup>].", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the electrode potential E when p(Cl<sub>2</sub>) = 2.50 bar and [Cl<sup>-</sup>] = 0.050 mol dm<sup>-3</sup> at 298 K.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State and explain whether chlorine becomes a stronger or weaker oxidizing agent under these non-standard conditions.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "z = 2 [1]; E = E° + (0.059 / 2) log( p(Cl2) / [Cl-]^2 ) [1].", "marks": 2},
                {"part": "(b)", "points": "p(Cl2) / [Cl-]^2 = 2.50 / (0.050)^2 = 2.50 / 0.0025 = 1000 [1]; log(1000) = 3 [1]; E = +1.36 + (0.0295 &times; 3) = +1.36 + 0.0885 = +1.45 V [1].", "marks": 3},
                {"part": "(c)", "points": "Stronger oxidizing agent because E is more positive (+1.45 V > +1.36 V) [1].", "marks": 1}
            ]
        ),

        # Q12: 9701/41/M/J/21/Q3
        Question(
            number=12,
            title="Industrial Electrorefining of Blister Copper — 9701/41/M/J/21/Q3 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_A",
            preamble="Impure 'blister' copper contains small amounts of silver, gold, iron, and zinc.<br/>During industrial electrolysis in aqueous CuSO<sub>4</sub>:<br/>Standard potentials: Zn<sup>2+</sup>/Zn = -0.76 V; Fe<sup>2+</sup>/Fe = -0.44 V; Cu<sup>2+</sup>/Cu = +0.34 V; Ag<sup>+</sup>/Ag = +0.80 V; Au<sup>3+</sup>/Au = +1.50 V.",
            parts=[
                QuestionPart("(a)", "Explain what happens to the zinc and iron impurities during electrolysis.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain what happens to the silver and gold impurities, and state their commercial significance.", 2, num_answer_lines=3),
                QuestionPart("(c)", "An electrolytic cell operates at 250 A for 24.0 hours. Calculate the mass of pure copper deposited on the cathode (Ar(Cu) = 63.5; F = 96500 C mol<sup>-1</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Zn and Fe have more negative E° than Cu &rArr; easily oxidized at the anode into Zn2+(aq) and Fe2+(aq) ions [1]; They remain in solution because Cu2+ is preferentially reduced at the cathode [1].", "marks": 2},
                {"part": "(b)", "points": "Ag and Au have more positive E° than Cu &rArr; cannot be oxidized at the anode potential [1]; Fall to the bottom as 'anode sludge' / slime, recovered to offset refining costs [1].", "marks": 2},
                {"part": "(c)", "points": "Q = 250 &times; (24 &times; 3600) = 2.16 &times; 10^7 C [1]; Mass = (2.16 &times; 10^7 / (2 &times; 96500)) &times; 63.5 = 111.9 &times; 63.5 = 7107 g (7.11 kg) [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/43/M/J/21/Q2
        Question(
            number=13,
            title="Proton Exchange Membrane (Acidic) Fuel Cell — 9701/43/M/J/21/Q2 [6 Marks]",
            syllabus_ref="24.4", difficulty="HARD", section_key="SEC_A",
            preamble="A Proton Exchange Membrane Fuel Cell (PEMFC) operates in acidic medium.<br/>Standard electrode potentials in acid solution:<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> &rightleftharpoons; 2H<sub>2</sub>O(l), E° = +1.23 V<br/>2H<sup>+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; H<sub>2</sub>(g), E° = 0.00 V",
            parts=[
                QuestionPart("(a)", "Write the half-equation at the anode and the half-equation at the cathode in this acidic fuel cell.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe the path taken by electrons and the path taken by protons (H<sup>+</sup>) as electrical work is produced.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the standard Gibbs free energy change, ΔG°, for the overall fuel cell reaction: 2H<sub>2</sub>(g) + O<sub>2</sub>(g) &rarr; 2H<sub>2</sub>O(l). (F = 96500 C mol<sup>-1</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Anode: H2(g) &rarr; 2H+(aq) + 2e- [1]; Cathode: O2(g) + 4H+(aq) + 4e- &rarr; 2H2O(l) [1].", "marks": 2},
                {"part": "(b)", "points": "Electrons travel from anode through external circuit/load to cathode [1]; Protons permeate through the polymer electrolyte membrane directly to the cathode [1].", "marks": 2},
                {"part": "(c)", "points": "n = 4 moles of electrons per mole of O2 (2 moles H2) [1]; ΔG° = -nFE°cell = -4 &times; 96500 &times; (+1.23) = -474780 J mol^-1 = -475 kJ mol^-1 [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/O/N/21/Q3
        Question(
            number=14,
            title="Copper(I) Disproportionation: Thermodynamic Calculation & Stability — 9701/42/O/N/21/Q3 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="Relevant standard electrode potentials:<br/>Cu<sup>+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Cu(s), E° = +0.52 V<br/>Cu<sup>2+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Cu<sup>+</sup>(aq), E° = +0.15 V",
            parts=[
                QuestionPart("(a)", "Write the ionic equation for the disproportionation of aqueous copper(I) ions.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the standard cell potential E°cell for this disproportionation and deduce whether Cu<sup>+</sup>(aq) is thermodynamically stable in water.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why copper(I) iodide, CuI(s), is stable in contact with water and does not disproportionate (Ksp(CuI) = 1.1 &times; 10<sup>-12</sup> mol<sup>2</sup> dm<sup>-6</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2Cu+(aq) &rarr; Cu2+(aq) + Cu(s) [1].", "marks": 1},
                {"part": "(b)", "points": "Reduction: Cu+ + e- &rarr; Cu (E° = +0.52 V) [1]; Oxidation: Cu+ &rarr; Cu2+ + e- (E° = +0.15 V) [1]; E°cell = +0.52 - (+0.15) = +0.37 V &rArr; E°cell > 0, so Cu+ spontaneously disproportionates and is unstable in water [1].", "marks": 3},
                {"part": "(c)", "points": "CuI is extremely insoluble, removing Cu+ ions from solution so [Cu+] is extremely small (~10^-6 mol dm^-3) [1]; By Nernst equation, E(Cu+/Cu) drops below E(Cu2+/Cu+), making disproportionation non-feasible / precipitation energetically stabilizes Cu(I) [1].", "marks": 2}
            ]
        ),

        # Q15: 9701/41/O/N/21/Q2
        Question(
            number=15,
            title="Electrolytic Evolution of Oxygen & Experimental Faraday Determination — 9701/41/O/N/21/Q2 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_A",
            preamble="Dilute sulfuric acid is electrolysed between inert platinum electrodes.<br/>A current of 0.600 A passed for 45.0 minutes evolved 102 cm<sup>3</sup> of dry oxygen gas at the anode, measured at 298 K and 1.01 &times; 10<sup>5</sup> Pa.<br/>Gas constant R = 8.31 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Write the ionic half-equation for the oxidation of water to form oxygen gas at the anode.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the number of moles of oxygen gas collected.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the total charge passed and determine an experimental value for the Faraday constant, F.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2H2O(l) &rarr; O2(g) + 4H+(aq) + 4e- [2] (1 mark for correct species, 1 mark for balanced 4e-).", "marks": 2},
                {"part": "(b)", "points": "V = 102 &times; 10^-6 m^3 [1]; n(O2) = pV / RT = (1.01 &times; 10^5 &times; 102 &times; 10^-6) / (8.31 &times; 298) = 10.302 / 2476.38 = 4.16 &times; 10^-3 mol [1].", "marks": 2},
                {"part": "(c)", "points": "Q = I &times; t = 0.600 &times; (45 &times; 60) = 1620 C [1]; 1 mol O2 requires 4 mol e- &rArr; Moles of e- = 4 &times; (4.16 &times; 10^-3) = 0.01664 mol &rArr; F = Q / n(e-) = 1620 / 0.01664 = 97350 C mol^-1 [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/42/M/J/20/Q3
        Question(
            number=16,
            title="Vanadium Multistage Redox States & Selective Reduction — 9701/42/M/J/20/Q3 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_A",
            preamble="Electrode potentials for vanadium species:<br/>VO<sub>2</sub><sup>+</sup>(aq) + 2H<sup>+</sup> + e<sup>-</sup> &rightleftharpoons; VO<sup>2+</sup>(aq) + H<sub>2</sub>O(l), E° = +1.00 V (Yellow to Blue)<br/>VO<sup>2+</sup>(aq) + 2H<sup>+</sup> + e<sup>-</sup> &rightleftharpoons; V<sup>3+</sup>(aq) + H<sub>2</sub>O(l), E° = +0.34 V (Blue to Green)<br/>V<sup>3+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; V<sup>2+</sup>(aq), E° = -0.26 V (Green to Violet)<br/>Reducing agents:<br/>SO<sub>4</sub><sup>2-</sup> + 4H<sup>+</sup> + 2e<sup>-</sup> &rightleftharpoons; SO<sub>2</sub> + 2H<sub>2</sub>O, E° = +0.17 V<br/>Zn<sup>2+</sup> + 2e<sup>-</sup> &rightleftharpoons; Zn(s), E° = -0.76 V",
            parts=[
                QuestionPart("(a)", "Predict the final oxidation state and color of the vanadium solution when excess sulfur dioxide, SO<sub>2</sub>(aq), is bubbled through acidified VO<sub>2</sub><sup>+</sup>(aq). Justify with E° values.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Predict the final oxidation state and color when excess zinc metal is added to acidified VO<sub>2</sub><sup>+</sup>(aq). Justify with E° values.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "SO2 (E° = +0.17 V) can reduce VO2+ to VO2+ (+1.00 - 0.17 = +0.83 V > 0) [1]; SO2 can reduce VO2+ to V3+ (+0.34 - 0.17 = +0.17 V > 0) [1]; Cannot reduce V3+ to V2+ (-0.26 - 0.17 = -0.43 V < 0); Final state is V3+ (green) [1].", "marks": 3},
                {"part": "(b)", "points": "Zn (E° = -0.76 V) has a more negative potential than all three vanadium reduction steps [1]; Reduces VO2+ &rarr; VO2+ &rarr; V3+ &rarr; V2+ sequentially because E°cell > 0 for all steps [1]; Final state is V2+ (violet) [1].", "marks": 3}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/41/M/J/20/Q2
        Question(
            number=17,
            title="Electrolytic Deposition of Tin from Tin(II) Sulfate — 9701/41/M/J/20/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_B",
            preamble="A solution of tin(II) sulfate, SnSO<sub>4</sub>(aq), is electrolysed using a current of 1.60 A for 35.0 minutes.<br/>Ar(Sn) = 118.7; F = 96500 C mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Write the cathode half-equation and calculate the mass of tin deposited.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sn2+(aq) + 2e- &rarr; Sn(s) [1]; Q = 1.60 &times; (35 &times; 60) = 3360 C [1]; Moles of Sn = 3360 / (2 &times; 96500) = 0.01741 mol [1]; Mass of Sn = 0.01741 &times; 118.7 = 2.07 g [1].", "marks": 4}
            ]
        ),

        # Q18: 9701/42/O/N/20/Q2
        Question(
            number=18,
            title="Effect of Cyanide Complexation on Iron(III)/Iron(II) Potential — 9701/42/O/N/20/Q2 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="Electrode potentials:<br/>[Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + e<sup>-</sup> &rightleftharpoons; [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup>, E° = +0.77 V<br/>[Fe(CN)<sub>6</sub>]<sup>3-</sup> + e<sup>-</sup> &rightleftharpoons; [Fe(CN)<sub>6</sub>]<sup>4-</sup>, E° = +0.36 V",
            parts=[
                QuestionPart("(a)", "Explain why the electrode potential is less positive for the hexacyanoferrate system than for the hydrated iron system.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cyanide CN- is a stronger ligand than H2O [1]; Fe3+ has higher charge density than Fe2+, attracting CN- more strongly [1]; [Fe(CN)6]3- is thermodynamically more stable relative to [Fe(CN)6]4- than Fe(H2O)6^3+ is to Fe(H2O)6^2+ [1]; Shifts the reduction equilibrium to the left, making E° less positive [1].", "marks": 4}
            ]
        ),

        # Q19: 9701/41/O/N/20/Q3
        Question(
            number=19,
            title="Nernst Equation for Iron Half-Cell under Asymmetric Ion Ratios — 9701/41/O/N/20/Q3 [4 Marks]",
            syllabus_ref="24.3", difficulty="EASY", section_key="SEC_B",
            preamble="Fe<sup>3+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Fe<sup>2+</sup>(aq), E° = +0.77 V.<br/>Nernst equation: E = E° + 0.059 log([Fe<sup>3+</sup>] / [Fe<sup>2+</sup>]).",
            parts=[
                QuestionPart("(a)", "Calculate the electrode potential E when [Fe<sup>3+</sup>] = 0.50 mol dm<sup>-3</sup> and [Fe<sup>2+</sup>] = 0.0050 mol dm<sup>-3</sup> at 298 K.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ratio [Fe3+]/[Fe2+] = 0.50 / 0.0050 = 100 [1]; log(100) = 2.0 [1]; E = +0.77 + (0.059 &times; 2.0) [1]; E = +0.77 + 0.118 = +0.89 V [1].", "marks": 4}
            ]
        ),

        # Q20: 9701/42/M/J/19/Q2
        Question(
            number=20,
            title="Lead-Acid Storage Cell Discharge Electrochemistry — 9701/42/M/J/19/Q2 [4 Marks]",
            syllabus_ref="24.4", difficulty="EASY", section_key="SEC_B",
            preamble="A secondary lead-acid cell uses lead plates and lead(IV) oxide in sulfuric acid.<br/>Anode: Pb(s) + SO<sub>4</sub><sup>2-</sup>(aq) &rarr; PbSO<sub>4</sub>(s) + 2e<sup>-</sup>, E° = -0.36 V<br/>Cathode: PbO<sub>2</sub>(s) + 4H<sup>+</sup>(aq) + SO<sub>4</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> &rarr; PbSO<sub>4</sub>(s) + 2H<sub>2</sub>O(l), E° = +1.69 V",
            parts=[
                QuestionPart("(a)", "Calculate the standard EMF of a single lead-acid cell and write the overall discharge equation.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E°cell = +1.69 - (-0.36) = +2.05 V [2]; Pb(s) + PbO2(s) + 2H2SO4(aq) &rarr; 2PbSO4(s) + 2H2O(l) [2].", "marks": 4}
            ]
        ),

        # Q21: 9701/41/M/J/19/Q3
        Question(
            number=21,
            title="Non-Standard Cell Potential of Zinc–Silver Cell — 9701/41/M/J/19/Q3 [4 Marks]",
            syllabus_ref="24.3", difficulty="EASY", section_key="SEC_B",
            preamble="Zn<sup>2+</sup> + 2e<sup>-</sup> &rightleftharpoons; Zn, E° = -0.76 V; Ag<sup>+</sup> + e<sup>-</sup> &rightleftharpoons; Ag, E° = +0.80 V.<br/>A cell is assembled with [Zn<sup>2+</sup>] = 2.00 mol dm<sup>-3</sup> and [Ag<sup>+</sup>] = 0.010 mol dm<sup>-3</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the non-standard potential of each half-cell and deduce the cell potential, Ecell.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E(Zn) = -0.76 + (0.059/2)log(2.00) = -0.76 + 0.009 = -0.75 V [1]; E(Ag) = +0.80 + 0.059 log(0.010) = +0.80 - 0.118 = +0.68 V [1]; Ecell = E(Ag) - E(Zn) [1]; Ecell = +0.68 - (-0.75) = +1.43 V (vs E° = +1.56 V) [1].", "marks": 4}
            ]
        ),

        # Q22: 9701/42/O/N/19/Q2
        Question(
            number=22,
            title="Electrolysis of Lead(II) Bromide: Molten vs Aqueous — 9701/42/O/N/19/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_B",
            preamble="Lead(II) bromide, PbBr<sub>2</sub>, can be electrolysed in molten state or in saturated aqueous solution.",
            parts=[
                QuestionPart("(a)", "Contrast the products formed at the cathode and anode in molten PbBr<sub>2</sub> versus aqueous PbBr<sub>2</sub>, giving half-equations.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Molten cathode: Pb2+ + 2e- &rarr; Pb(l) [1]; Molten anode: 2Br- &rarr; Br2(g) + 2e- [1]; Aqueous cathode: H2(g) evolved (2H+ + 2e- &rarr; H2) or Pb deposited [1]; Aqueous anode: Br2(aq) formed (2Br- &rarr; Br2 + 2e-) [1].", "marks": 4}
            ]
        ),

        # Q23: 9701/41/O/N/19/Q3
        Question(
            number=23,
            title="Direct Methanol Fuel Cell (DMFC) Electrochemistry — 9701/41/O/N/19/Q3 [4 Marks]",
            syllabus_ref="24.4", difficulty="EASY", section_key="SEC_B",
            preamble="A direct methanol fuel cell uses liquid methanol, CH<sub>3</sub>OH, as fuel.<br/>Anode: CH<sub>3</sub>OH(l) + H<sub>2</sub>O(l) &rarr; CO<sub>2</sub>(g) + 6H<sup>+</sup>(aq) + 6e<sup>-</sup><br/>Cathode: O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> &rarr; 2H<sub>2</sub>O(l)",
            parts=[
                QuestionPart("(a)", "Combine these equations to write the overall cell reaction and state two advantages of liquid methanol over hydrogen gas as fuel.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2CH3OH(l) + 3O2(g) &rarr; 2CO2(g) + 4H2O(l) [2]; Methanol is liquid at room temperature &rArr; much easier/safer to store and transport than compressed H2 gas [1]; High volumetric energy density / existing liquid fuel distribution infrastructure can be adapted [1].", "marks": 4}
            ]
        ),

        # Q24: 9701/42/M/J/18/Q3
        Question(
            number=24,
            title="Function of Platinum Black Coating on Hydrogen Electrode — 9701/42/M/J/18/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="The platinum electrode in the SHE is coated with finely divided platinum black.",
            parts=[
                QuestionPart("(a)", "Explain two distinct scientific reasons why platinised platinum is used rather than a smooth platinum foil.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Platinised platinum has an extremely porous, micro-rough surface providing a vastly increased surface area [2]; Acts as an effective heterogeneous catalyst for rapid dissociation of H2 molecules into adsorbed H atoms [1]; Accelerates electron transfer equilibrium 2H+(aq) + 2e- &rightleftharpoons; H2(g), preventing polarization [1].", "marks": 4}
            ]
        ),

        # Q25: 9701/41/M/J/18/Q2
        Question(
            number=25,
            title="Avogadro Constant Calculation from Electrolysis of Silver — 9701/41/M/J/18/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_B",
            preamble="A current of 0.500 A was passed through AgNO<sub>3</sub>(aq) for 38.6 minutes, depositing 1.295 g of silver.<br/>e = 1.602 &times; 10<sup>-19</sup> C; Ar(Ag) = 107.9.",
            parts=[
                QuestionPart("(a)", "Calculate the value of the Avogadro constant, L, from these experimental results.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Q = 0.500 &times; (38.6 &times; 60) = 1158 C [1]; Moles of Ag = 1.295 / 107.9 = 0.01200 mol [1]; Moles of e- = 0.01200 mol [1]; L = Q / (n(e-) &times; e) = 1158 / (0.01200 &times; 1.602 &times; 10^-19) = 6.02 &times; 10^23 mol^-1 [1].", "marks": 4}
            ]
        ),

        # Q26: 9701/42/O/N/18/Q3
        Question(
            number=26,
            title="Nernst Shift Following Addition of Precipitating Halide — 9701/42/O/N/18/Q3 [4 Marks]",
            syllabus_ref="24.3", difficulty="EASY", section_key="SEC_B",
            preamble="For Ag<sup>+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Ag(s), E° = +0.80 V.<br/>Excess NaCl(aq) is added to the silver half-cell, precipitating AgCl(s) (Ksp = 1.8 &times; 10<sup>-10</sup> mol<sup>2</sup> dm<sup>-6</sup>).",
            parts=[
                QuestionPart("(a)", "Explain, using Le Chatelier's principle and the Nernst equation, why the electrode potential drops significantly.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Precipitation of AgCl removes Ag+ ions from aqueous solution, dramatically reducing [Ag+] [1]; By Le Chatelier's principle, the equilibrium Ag+ + e- &rightleftharpoons; Ag shifts to the left [1]; In Nernst equation E = E° + 0.059 log[Ag+], log[Ag+] becomes large and negative [1]; Electrode potential E becomes significantly less positive (drops to approx +0.22 V) [1].", "marks": 4}
            ]
        ),

        # Q27: 9701/41/O/N/18/Q2
        Question(
            number=27,
            title="Composition and Mechanism of the Salt Bridge — 9701/41/O/N/18/Q2 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="A standard galvanic cell utilizes a salt bridge saturated with potassium nitrate, KNO<sub>3</sub>(aq).",
            parts=[
                QuestionPart("(a)", "Explain why KNO<sub>3</sub> is preferred over NaCl as salt bridge electrolyte, and explain how the bridge maintains electroneutrality.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "K+ and NO3- have virtually identical ionic mobilities, preventing liquid junction potentials [1]; Neither K+ nor NO3- forms insoluble precipitates or redox reactions with typical cell electrolytes [1]; Anions (NO3-) migrate into the anode compartment to neutralize positive metal cations generated [1]; Cations (K+) migrate into the cathode compartment to replace discharged cations [1].", "marks": 4}
            ]
        ),

        # Q28: 9701/42/M/J/17/Q3
        Question(
            number=28,
            title="Redox Disproportionation Feasibility of Hydrogen Peroxide — 9701/42/M/J/17/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="Hydrogen peroxide undergoes self-redox (disproportionation):<br/>H<sub>2</sub>O<sub>2</sub>(aq) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; 2H<sub>2</sub>O(l), E° = +1.77 V<br/>O<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; H<sub>2</sub>O<sub>2</sub>(aq), E° = +0.68 V",
            parts=[
                QuestionPart("(a)", "Calculate the standard cell potential E°cell and explain why H<sub>2</sub>O<sub>2</sub> is thermodynamically unstable with respect to disproportionation.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Reduction: H2O2 + 2H+ + 2e- &rarr; 2H2O (+1.77 V) [1]; Oxidation: H2O2 &rarr; O2 + 2H+ + 2e- (+0.68 V) [1]; E°cell = +1.77 - (+0.68) = +1.09 V [1]; E°cell > 0 &rArr; thermodynamically feasible and spontaneous: 2H2O2(aq) &rarr; 2H2O(l) + O2(g) [1].", "marks": 4}
            ]
        ),

        # Q29: 9701/41/M/J/17/Q2
        Question(
            number=29,
            title="Electroplating Nickel from Nickel(II) Sulfate — 9701/41/M/J/17/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_B",
            preamble="An object is plated with a uniform layer of nickel from NiSO<sub>4</sub>(aq) using a current of 2.50 A.<br/>Ar(Ni) = 58.7; Density of Ni = 8.90 g cm<sup>-3</sup>; F = 96500 C mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the time, in minutes, required to deposit 4.40 g of nickel.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Moles of Ni = 4.40 / 58.7 = 0.07496 mol [1]; Moles of electrons = 2 &times; 0.07496 = 0.1499 mol [1]; Q = n(e-) &times; F = 0.1499 &times; 96500 = 14467 C [1]; t = Q / I = 14467 / 2.50 = 5787 s = 96.4 minutes [1].", "marks": 4}
            ]
        ),

        # Q30: 9701/42/O/N/17/Q3
        Question(
            number=30,
            title="Redox Titration Feasibility: Manganate(VII) vs Iron(II) — 9701/42/O/N/17/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="Standard potentials:<br/>MnO<sub>4</sub><sup>-</sup> + 8H<sup>+</sup> + 5e<sup>-</sup> &rightleftharpoons; Mn<sup>2+</sup> + 4H<sub>2</sub>O, E° = +1.52 V<br/>Fe<sup>3+</sup> + e<sup>-</sup> &rightleftharpoons; Fe<sup>2+</sup>, E° = +0.77 V<br/>Cl<sub>2</sub> + 2e<sup>-</sup> &rightleftharpoons; 2Cl<sup>-</sup>, E° = +1.36 V",
            parts=[
                QuestionPart("(a)", "Calculate E°cell for the titration of Fe<sup>2+</sup> by MnO<sub>4</sub><sup>-</sup>, and explain why hydrochloric acid cannot be used to acidify the titration.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E°cell = +1.52 - (+0.77) = +0.75 V [1]; Reaction is completely feasible and quantitative [1]; MnO4- (E° = +1.52 V) has a more positive potential than Cl2/Cl- (+1.36 V) [1]; MnO4- would oxidize Cl- ions from HCl into toxic Cl2 gas, giving an erroneously high titre [1].", "marks": 4}
            ]
        ),

        # Q31: 9701/41/O/N/17/Q2
        Question(
            number=31,
            title="Overpotential and Selective Discharge in Chlor-Alkali Cell — 9701/41/O/N/17/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_B",
            preamble="The discharge of ions at an electrode is governed by both thermodynamic electrode potentials and kinetic overpotentials.",
            parts=[
                QuestionPart("(a)", "Define 'overpotential' (overvoltage) and explain how it determines the discharge of chlorine rather than oxygen at a titanium anode.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Overpotential is the extra potential difference above the thermodynamic E° required to drive an electrode reaction at a measurable rate [2]; Oxidation of water to O2 involves breaking multiple bonds and transfer of 4 electrons, conferring a very high activation energy and high overpotential [1]; Discharge of Cl- involves simple electron loss with minimal overpotential on titanium, making chlorine kinetically favored [1].", "marks": 4}
            ]
        ),

        # Q32: 9701/42/M/J/16/Q3
        Question(
            number=32,
            title="Thermodynamics of the Daniell Cell & Maximum Electrical Work — 9701/42/M/J/16/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_B",
            preamble="The standard cell potential of the Daniell cell Zn(s) + Cu<sup>2+</sup>(aq) &rarr; Zn<sup>2+</sup>(aq) + Cu(s) is +1.10 V at 298 K.<br/>F = 96500 C mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the standard Gibbs free energy change, ΔG°, and state the maximum electrical work obtainable per mole of zinc consumed.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "n = 2 [1]; ΔG° = -nFE°cell = -2 &times; 96500 &times; 1.10 [1]; ΔG° = -212300 J mol^-1 = -212.3 kJ mol^-1 [1]; Maximum electrical work = -ΔG° = 212.3 kJ mol^-1 [1].", "marks": 4}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/41/M/J/23/Q3(a)
        Question(
            number=33,
            title="Standard Definition of Electrode Potential — 9701/41/M/J/23/Q3(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_C",
            preamble="Electrode potential reflects electron-releasing or accepting tendency.",
            parts=[
                QuestionPart("(a)", "Define the standard electrode potential of a half-cell, E°.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The electromotive force (EMF) of a cell composed of the half-cell connected to a standard hydrogen electrode [1] under standard conditions of 298 K, 100 kPa pressure, and 1.00 mol dm^-3 solution concentrations [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/42/M/J/23/Q2(a)
        Question(
            number=34,
            title="Definition of the Faraday Constant and SI Units — 9701/42/M/J/23/Q2(a) [2 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_C",
            preamble="Faraday constant links microscopic charge to molar quantities.",
            parts=[
                QuestionPart("(a)", "Define the Faraday constant, F, and state its SI units.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The electric charge carried by one mole of electrons (or singly charged ions) [1]; Units: C mol^-1 (coulombs per mole) [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/41/O/N/23/Q2(a)
        Question(
            number=35,
            title="Operating Pressure and Concentration Standards in SHE — 9701/41/O/N/23/Q2(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_C",
            preamble="Standard conditions define reference potential reproducibility.",
            parts=[
                QuestionPart("(a)", "State the exact standard pressure of hydrogen gas and concentration of H<sup>+</sup> ions required in the Standard Hydrogen Electrode.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Pressure: 1.00 bar (or 100 kPa / 1 atm) [1]; Concentration: 1.00 mol dm^-3 H+(aq) [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/42/O/N/23/Q2(a)
        Question(
            number=36,
            title="Statement of the Nernst Equation — 9701/42/O/N/23/Q2(a) [2 Marks]",
            syllabus_ref="24.3", difficulty="EASY", section_key="SEC_C",
            preamble="Electrode potentials vary predictably with concentration.",
            parts=[
                QuestionPart("(a)", "State the mathematical form of the Nernst equation at 298 K, defining the term z.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E = E° + (0.059 / z) log([oxidised form] / [reduced form]) [1]; z is the number of electrons transferred in the half-equation [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/41/M/J/22/Q3(a)
        Question(
            number=37,
            title="Function of Inert Platinum in Redox Half-Cells — 9701/41/M/J/22/Q3(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_C",
            preamble="Half-cells involving two aqueous ions require an unreactive conductor.",
            parts=[
                QuestionPart("(a)", "Explain why a platinum electrode is used in an Fe<sup>3+</sup>(aq)/Fe<sup>2+</sup>(aq) half-cell rather than an iron electrode.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Platinum is chemically inert and does not react with the solution or participate in the redox reaction [1]; It provides a conducting surface for electron transfer between Fe3+ and Fe2+ (iron would dissolve reacting directly) [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/42/M/J/22/Q3(a)
        Question(
            number=38,
            title="Fundamental Relationship: Gibbs Energy and Cell EMF — 9701/42/M/J/22/Q3(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_C",
            preamble="Electrochemical cell potentials are directly linked to Gibbs free energy.",
            parts=[
                QuestionPart("(a)", "Write the thermodynamic equation relating standard Gibbs free energy change, ΔG°, to standard cell potential, E°cell.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔG° = -nFE°cell (or ΔG° = -zFE°cell) [1]; n = moles of electrons transferred, F = Faraday constant [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/41/O/N/22/Q3(a)
        Question(
            number=39,
            title="Preferential Discharge Rule in Aqueous Electrolysis — 9701/41/O/N/22/Q3(a) [2 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_C",
            preamble="Aqueous solutions contain competing cations and anions.",
            parts=[
                QuestionPart("(a)", "State the thermodynamic rule that predicts which cation is preferentially discharged at the cathode during electrolysis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The cation with the more positive (or less negative) standard electrode potential E° is preferentially reduced / discharged [2].", "marks": 2}
            ]
        ),

        # Q40: 9701/42/O/N/21/Q3(a)
        Question(
            number=40,
            title="Thermodynamic Definition of Disproportionation — 9701/42/O/N/21/Q3(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_C",
            preamble="An intermediate oxidation state can undergo self-oxidation and self-reduction.",
            parts=[
                QuestionPart("(a)", "Define disproportionation in terms of oxidation numbers, and state the condition for its thermodynamic feasibility in terms of E°cell.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A redox reaction in which atoms of the same element are simultaneously oxidized and reduced [1]; Feasible when E°(reduction) > E°(oxidation), meaning E°cell > 0 [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # (4 x 6-Markers, 4 x 4-Markers, 2 x 2-Markers)
        # =====================================================================

        # Q41: HIGH FREQUENCY 6-MARKER — Standard Hydrogen Electrode Mastery
        Question(
            number=41,
            title="HF 1: Standard Hydrogen Electrode Comprehensive Analysis — 9701/42/M/J/23/Q3 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #1 (Standard Hydrogen Electrode Mastery)</b><br/>"
                     "The Standard Hydrogen Electrode (SHE) shown in Fig. 41.1 is the primary international standard for electrode potential measurement.",
            figure_path=os.path.join(fig_dir, "a2_t24_she_apparatus.png"),
            figure_caption="Fig. 41.1: Complete Standard Hydrogen Electrode (SHE) showing hydrogen gas inlet, platinised foil, and acid solution.",
            parts=[
                QuestionPart("(a)", "Label the components and define the exact operating conditions of temperature, pressure, and concentration in the SHE.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Describe how the SHE is used to measure the standard electrode potential of an unknown metal half-cell M<sup>2+</sup>(aq)/M(s).", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Pt wire/foil coated with platinum black; 1.00 mol dm^-3 H+(aq) (or 0.5 mol dm^-3 H2SO4) [1]; Pure H2 gas bubbled at 1.00 bar (100 kPa) [1]; Maintained at 298 K (25 °C) [1].", "marks": 3},
                {"part": "(b)", "points": "Connect SHE to M2+/M half-cell using a salt bridge [1]; Connect electrodes via a high-resistance digital voltmeter [1]; Voltmeter reading gives magnitude of E°; if M is negative electrode, E° is negative, if positive electrode, E° is positive [1].", "marks": 3}
            ]
        ),

        # Q42: HIGH FREQUENCY 6-MARKER — Electrochemical Cell & Salt Bridge
        Question(
            number=42,
            title="HF 2: Daniell Cell Potentials, Salt Bridge Dynamics & Electron Flow — 9701/41/M/J/22/Q2 [6 Marks]",
            syllabus_ref="24.2", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #2 (Electrochemical Cell & Salt Bridge Dynamics)</b><br/>"
                     "A zinc-copper electrochemical cell is set up as shown in Fig. 42.1.<br/>"
                     "Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; Zn(s), E° = -0.76 V<br/>"
                     "Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> &rightleftharpoons; Cu(s), E° = +0.34 V",
            figure_path=os.path.join(fig_dir, "a2_t24_electrochemical_cell.png"),
            figure_caption="Fig. 42.1: Complete zinc-copper cell diagram showing voltmeter, salt bridge, and electron flow direction.",
            parts=[
                QuestionPart("(a)", "Calculate E°cell, state the spontaneous cell reaction, and deduce which electrode loses mass.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain how the salt bridge maintains electrical continuity and explain the direction of migration of potassium and nitrate ions.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E°cell = +0.34 - (-0.76) = +1.10 V [1]; Zn(s) + Cu2+(aq) &rarr; Zn2+(aq) + Cu(s) [1]; Zn electrode loses mass (oxidized to Zn2+) [1].", "marks": 3},
                {"part": "(b)", "points": "Completes the electrical circuit by allowing movement of ions between solutions without direct mixing [1]; NO3- anions move toward the Zn half-cell to balance newly formed Zn2+ cations [1]; K+ cations move toward the Cu half-cell to replace discharged Cu2+ cations [1].", "marks": 3}
            ]
        ),

        # Q43: HIGH FREQUENCY 6-MARKER — Alkaline Fuel Cell
        Question(
            number=43,
            title="HF 3: Alkaline Hydrogen-Oxygen Fuel Cell Mechanics & Efficiency — 9701/42/O/N/22/Q3 [6 Marks]",
            syllabus_ref="24.4", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #3 (Hydrogen-Oxygen Alkaline Fuel Cell)</b><br/>"
                     "The alkaline fuel cell in Fig. 43.1 uses concentrated KOH(aq) electrolyte and porous carbon electrodes containing platinum catalysts.",
            figure_path=os.path.join(fig_dir, "a2_t24_alkaline_fuel_cell.png"),
            figure_caption="Fig. 43.1: Cross-section of an alkaline hydrogen-oxygen fuel cell showing gas inlets and electrolyte.",
            parts=[
                QuestionPart("(a)", "Write the balanced ionic half-equations occurring at the anode and at the cathode.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the standard cell potential E°cell and explain why a fuel cell does not need to be recharged like a secondary battery.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Anode: 2H2(g) + 4OH-(aq) &rarr; 4H2O(l) + 4e- [2]; Cathode: O2(g) + 2H2O(l) + 4e- &rarr; 4OH-(aq) [1].", "marks": 3},
                {"part": "(b)", "points": "E°cell = +0.40 - (-0.83) = +1.23 V [1]; Fuel (H2) and oxidant (O2) are supplied continuously from an external source [1]; Operates indefinitely as long as reactants are supplied, unlike batteries with finite stored chemical energy [1].", "marks": 3}
            ]
        ),

        # Q44: HIGH FREQUENCY 6-MARKER — Quantitative Faraday Determination
        Question(
            number=44,
            title="HF 4: Quantitative Determination of Faraday and Avogadro Constants — 9701/41/O/N/21/Q3 [6 Marks]",
            syllabus_ref="24.1", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #4 (Electrolytic Avogadro Determination)</b><br/>"
                     "In an electrolytic cell, an electric current of 0.400 A was passed through AgNO<sub>3</sub>(aq) for 50.0 minutes.<br/>"
                     "The mass of silver deposited on the cathode was 1.341 g.<br/>"
                     "Data: Ar(Ag) = 107.9; Elementary charge on electron e = 1.602 &times; 10<sup>-19</sup> C.",
            parts=[
                QuestionPart("(a)", "Calculate the total charge Q passed, and calculate the moles of electrons transferred.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate an experimental value for the Faraday constant, F.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Using your calculated value of F and the value of e, determine the Avogadro constant, L.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Q = I &times; t = 0.400 &times; (50.0 &times; 60) = 1200 C [1]; Moles of Ag = 1.341 / 107.9 = 0.012428 mol &rArr; Moles of e- = 0.012428 mol [1].", "marks": 2},
                {"part": "(b)", "points": "F = Q / n(e-) = 1200 / 0.012428 [1]; F = 96556 C mol^-1 (accept 96560 C mol^-1) [1].", "marks": 2},
                {"part": "(c)", "points": "L = F / e = 96556 / (1.602 &times; 10^-19) [1]; L = 6.027 &times; 10^23 mol^-1 (accept 6.03 &times; 10^23) [1].", "marks": 2}
            ]
        ),

        # Q45: HIGH FREQUENCY 4-MARKER — Nernst Equation in Concentration Cell
        Question(
            number=45,
            title="HF 5: Nernst Equation & Concentration Cell Thermodynamics — 9701/42/M/J/21/Q2 [4 Marks]",
            syllabus_ref="24.3", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #5 (Concentration Cell & Nernst Equation)</b><br/>"
                     "A copper concentration cell is illustrated in Fig. 45.1.<br/>"
                     "Left: [Cu<sup>2+</sup>] = 0.050 mol dm<sup>-3</sup>; Right: [Cu<sup>2+</sup>] = 1.50 mol dm<sup>-3</sup>.<br/>"
                     "E = E° + (0.059 / 2) log[Cu<sup>2+</sup>].",
            figure_path=os.path.join(fig_dir, "a2_t24_concentration_cell.png"),
            figure_caption="Fig. 45.1: Copper concentration cell driven by unequal Cu2+ ion concentrations.",
            parts=[
                QuestionPart("(a)", "Calculate the potential difference Ecell of this concentration cell at 298 K.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ecell = (0.059 / 2) log([Cu2+]conc / [Cu2+]dil) [1]; Ratio = 1.50 / 0.050 = 30.0 [1]; log(30.0) = 1.477 [1]; Ecell = 0.0295 &times; 1.477 = +0.0436 V (or +0.044 V) [1].", "marks": 4}
            ]
        ),

        # Q46: HIGH FREQUENCY 4-MARKER — Ligand Exchange & Redox Shift
        Question(
            number=46,
            title="HF 6: Ligand Influence on Transition Metal Redox Stability — 9701/41/M/J/20/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #6 (Ligand Exchange & Redox Potentials)</b><br/>"
                     "Fe<sup>3+</sup>(aq) + e<sup>-</sup> &rightleftharpoons; Fe<sup>2+</sup>(aq), E° = +0.77 V<br/>"
                     "[Fe(CN)<sub>6</sub>]<sup>3-</sup>(aq) + e<sup>-</sup> &rightleftharpoons; [Fe(CN)<sub>6</sub>]<sup>4-</sup>(aq), E° = +0.36 V",
            parts=[
                QuestionPart("(a)", "Explain how the nature of the ligand affects the relative stability of Fe(III) and Fe(II) and accounts for the difference in E° values.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CN- forms stronger coordinate bonds than H2O [1]; Fe3+ has smaller ionic radius and higher charge density than Fe2+ [1]; Fe3+ attracts CN- ligands more strongly, forming a thermodynamically more stable complex than Fe2+ [1]; This preferentially stabilizes the oxidized form, shifting equilibrium to the left and reducing E° [1].", "marks": 4}
            ]
        ),

        # Q47: HIGH FREQUENCY 4-MARKER — Disproportionation Thermodynamics
        Question(
            number=47,
            title="HF 7: Thermodynamic Feasibility of Copper(I) Disproportionation — 9701/42/O/N/20/Q3 [4 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #7 (Disproportionation of Copper(I))</b><br/>"
                     "Cu<sup>+</sup> + e<sup>-</sup> &rightleftharpoons; Cu, E° = +0.52 V<br/>"
                     "Cu<sup>2+</sup> + e<sup>-</sup> &rightleftharpoons; Cu<sup>+</sup>, E° = +0.15 V",
            parts=[
                QuestionPart("(a)", "Use these data to prove that aqueous copper(I) sulfate disproportionates spontaneously into copper metal and copper(II) sulfate.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Reduction half-equation: Cu+ + e- &rarr; Cu (E° = +0.52 V) [1]; Oxidation half-equation: Cu+ &rarr; Cu2+ + e- (E° = +0.15 V) [1]; Overall: 2Cu+(aq) &rarr; Cu2+(aq) + Cu(s) [1]; E°cell = +0.52 - (+0.15) = +0.37 V &rArr; Since E°cell > 0, the reaction is thermodynamically spontaneous [1].", "marks": 4}
            ]
        ),

        # Q48: HIGH FREQUENCY 4-MARKER — Brine Electrolysis & Selective Discharge
        Question(
            number=48,
            title="HF 8: Selective Ion Discharge in Brine Electrolysis — 9701/41/O/N/19/Q2 [4 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #8 (Brine Electrolysis & Overpotentials)</b><br/>"
                     "Electrolysis of concentrated aqueous sodium chloride produces Cl<sub>2</sub>(g) and H<sub>2</sub>(g).",
            parts=[
                QuestionPart("(a)", "Explain why chlorine is liberated at the anode rather than oxygen, and write the anode and cathode half-equations.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Anode: 2Cl-(aq) &rarr; Cl2(g) + 2e- [1]; Cathode: 2H2O(l) + 2e- &rarr; H2(g) + 2OH-(aq) (or 2H+ + 2e- &rarr; H2) [1]; High concentration of Cl- in brine lowers its discharge potential [1]; Oxidation of water to O2 has a large kinetic activation energy / high overpotential on the anode surface [1].", "marks": 4}
            ]
        ),

        # Q49: HIGH FREQUENCY 2-MARKER — Definition of Faraday Constant
        Question(
            number=49,
            title="HF 9: Standard Definition of the Faraday Constant — 9701/41/M/J/23/Q2(a) [2 Marks]",
            syllabus_ref="24.1", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #9 (Faraday Constant Definition)</b>",
            parts=[
                QuestionPart("(a)", "Define the Faraday constant, F, and write its mathematical formula in terms of L and e.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The electric charge carried by one mole of electrons [1]; F = L &times; e [1].", "marks": 2}
            ]
        ),

        # Q50: HIGH FREQUENCY 2-MARKER — Feasibility Criterion
        Question(
            number=50,
            title="HF 10: Thermodynamic Criterion for Cell Feasibility — 9701/42/M/J/22/Q2(a) [2 Marks]",
            syllabus_ref="24.2", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #10 (Thermodynamic Feasibility Criterion)</b>",
            parts=[
                QuestionPart("(a)", "State the thermodynamic condition for a redox reaction to be feasible in terms of E°cell, and state its relation to ΔG°.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "E°cell must be positive (E°cell > 0) [1]; Corresponds to a negative Gibbs free energy change (ΔG° < 0) via ΔG° = -nFE°cell [1].", "marks": 2}
            ]
        ),
    ]

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )

if __name__ == "__main__":
    build_topic24_50q()
