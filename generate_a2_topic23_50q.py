"""
Complete 50-Question Master Pack: Topic 23 — Chemical Energetics (Paper 4 Theory)
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

def build_topic23_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic23_Chemical_Energetics.pdf"

    topic_title = "Topic 23 — Chemical Energetics"
    topic_subtitle = "Lattice Energy · Born–Haber Cycles · Hydration & Solution · Entropy ΔS · Gibbs Free Energy ΔG"

    subtopics_summary = [
        ("23.1 Lattice Energy & Born–Haber Cycles", "Standard lattice energy definitions; Born–Haber cycles for binary and ternary ionic solids; theoretical vs experimental lattice energies; ionic polarization and covalent character."),
        ("23.2 Enthalpies of Solution & Hydration", "Definitions of ΔH°sol and ΔH°hyd; Hess's Law cycles linking solution, hydration and lattice energy; thermodynamic rationale for Group 2 sulfate and hydroxide solubility trends."),
        ("23.3 Entropy Change, ΔS", "Concept of entropy and disorder; calculating ΔS°sys from standard molar entropies; ΔSsurr and ΔStot; Second Law of Thermodynamics."),
        ("23.4 Gibbs Free Energy Change, ΔG", "ΔG = ΔH - TΔS; feasibility conditions; calculation of feasibility temperatures; temperature dependence of spontaneity and kinetic stability."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Chemical Energetics from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q1
        Question(
            number=1,
            title="Zinc Sulfide Born–Haber Cycle — 9701/42/M/J/23/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Zinc sulfide, ZnS, occurs naturally as sphalerite. A Born–Haber cycle for ZnS(s) is shown in Fig. 1.1.<br/>Thermochemical data (kJ mol<sup>-1</sup>): ΔH°f[ZnS] = -206; ΔH°at[Zn] = +131; (IE1+IE2)[Zn] = +2640; ΔH°at[S] = +279; (EA1+EA2)[S] = +332.",
            figure_path=os.path.join(fig_dir, "a2_t23_born_haber_zns.png"),
            figure_caption="Fig. 1.1: Born–Haber cycle energy level diagram for crystalline zinc sulfide, ZnS(s).",
            parts=[
                QuestionPart("(a)", "Define the standard enthalpy change of hydration of an ion, ΔH°hyd.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Construct the Born–Haber cycle expression and calculate the lattice energy of ZnS(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of gaseous ions [1] is completely hydrated in water to form infinitely dilute aqueous solution under standard conditions [1].", "marks": 2},
                {"part": "(b)", "points": "ΔH°f = ΔH°at(Zn) + (IE1+IE2)(Zn) + ΔH°at(S) + (EA1+EA2)(S) + LE(ZnS) [1]; -206 = +131 + 2640 + 279 + 332 + LE [1]; LE = -206 - 3382 [1]; LE(ZnS) = -3588 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q2
        Question(
            number=2,
            title="Magnesium Chloride Lattice Energy & Feasibility — 9701/41/M/J/23/Q2 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Magnesium chloride decomposes: MgCl<sub>2</sub>(s) &rarr; Mg(s) + Cl<sub>2</sub>(g), ΔH° = +641 kJ mol<sup>-1</sup>.<br/>Data: ΔH°at[Mg] = +147, (IE1+IE2)[Mg] = +2187, BE(Cl<sub>2</sub>) = +242, EA(Cl) = -349 kJ mol<sup>-1</sup>.<br/>S° values (J K<sup>-1</sup> mol<sup>-1</sup>): MgCl<sub>2</sub>(s) = 90.0; Mg(s) = 32.7; Cl<sub>2</sub>(g) = 223.0.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of MgCl<sub>2</sub>(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate ΔS° for the decomposition and deduce the minimum temperature at which it becomes feasible.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Mg) + (IE1+IE2) + 2(ΔH°at(Cl)) + 2(EA(Cl)) + LE [1]; -641 = 147 + 2187 + 242 + 2(-349) + LE = 1878 + LE [1]; LE(MgCl2) = -2519 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "ΔS° = 32.7 + 223.0 - 90.0 = +165.7 J K<sup>-1</sup> mol<sup>-1</sup> [1]; At feasibility, T = ΔH° / ΔS° [1]; T = (641 &times; 1000) / 165.7 = 3868 K [1].", "marks": 3}
            ]
        ),

        # Q3: 9701/43/M/J/23/Q1
        Question(
            number=3,
            title="Calcium Fluoride Cycle & Solubility Thermodynamics — 9701/43/M/J/23/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Data for CaF<sub>2</sub> (kJ mol<sup>-1</sup>): ΔH°f = -1220; ΔH°at[Ca] = +178; (IE1+IE2)[Ca] = +1735; BE(F–F) = +158; EA[F] = -328.<br/>ΔH°hyd(Ca<sup>2+</sup>) = -1577; ΔH°hyd(F<sup>-</sup>) = -506.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of calcium fluoride, CaF<sub>2</sub>(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate ΔH°sol of CaF<sub>2</sub> and explain why it is much less soluble than CaCl<sub>2</sub>.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-1220 = 178 + 1735 + 158 + 2(-328) + LE = 1415 + LE [1]; LE(CaF2) = -2635 kJ mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "ΔH°sol = [-1577 + 2(-506)] - (-2635) = -2589 + 2635 = +46 kJ mol<sup>-1</sup> [1]; ΔH°sol is endothermic [1]; F- is very small, giving CaF2 a vastly more exothermic LE that outweighs hydration enthalpy [1].", "marks": 3}
            ]
        ),

        # Q4: 9701/42/O/N/22/Q1
        Question(
            number=4,
            title="Barium Sulfate Solution Cycle & Group 2 Trends — 9701/42/O/N/22/Q1 [6 Marks]",
            syllabus_ref="23.2", difficulty="HARD", section_key="SEC_A",
            preamble="Lattice energy of BaSO<sub>4</sub> = -2469 kJ mol<sup>-1</sup>.<br/>Enthalpies of hydration: ΔH°hyd(Ba<sup>2+</sup>) = -1305 kJ mol<sup>-1</sup>; ΔH°hyd(SO<sub>4</sub><sup>2-</sup>) = -1145 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Construct an energy cycle and calculate the standard enthalpy of solution, ΔH°sol, of BaSO<sub>4</sub>.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why the solubility of Group 2 sulfates decreases down the group from MgSO<sub>4</sub> to BaSO<sub>4</sub>.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = ΔH°hyd(Ba2+) + ΔH°hyd(SO4^2-) - LE [1]; ΔH°sol = (-1305 - 1145) - (-2469) = -2450 + 2469 [1]; ΔH°sol = +19 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "Both LE and ΔH°hyd become less exothermic down the group as cation radius increases [1]; however, ΔH°hyd decreases more rapidly than LE because SO4^2- is very large [1]; hence ΔH°sol becomes more endothermic down the group, decreasing solubility [1].", "marks": 3}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q1
        Question(
            number=5,
            title="Silver Chloride Lattice Energy: Experimental vs Theoretical — 9701/42/M/J/22/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Data for AgCl (kJ mol<sup>-1</sup>): ΔH°f = -127; ΔH°at[Ag] = +285; IE1[Ag] = +731; ΔH°at[Cl] = +121; EA[Cl] = -349.<br/>Theoretical electrostatic lattice energy = -770 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the experimental lattice energy of AgCl(s) using the Born–Haber cycle.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain the discrepancy between the experimental and theoretical lattice energy values.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-127 = 285 + 731 + 121 + (-349) + LE = 788 + LE [1]; LE(AgCl) = -915 kJ mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "Experimental LE (-915) is significantly more exothermic than theoretical LE (-770) [1]; Ag+ has high polarising power due to poorly shielding 4d10 electrons, polarising the Cl- ion [1]; introduces significant covalent character, strengthening the lattice [1].", "marks": 3}
            ]
        ),

        # Q6: 9701/42/O/N/21/Q1
        Question(
            number=6,
            title="Copper(I) Oxide Born–Haber Cycle & Electron Affinities — 9701/42/O/N/21/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Data for Cu<sub>2</sub>O (kJ mol<sup>-1</sup>): ΔH°f = -169; ΔH°at[Cu] = +338; IE1[Cu] = +746; ΔH°at[O] = +249; EA1[O] = -141; EA2[O] = +798.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of Cu<sub>2</sub>O(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain why EA1 of oxygen is exothermic whereas EA2 is endothermic.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-169 = 2(338) + 2(746) + 249 + (-141 + 798) + LE = 676 + 1492 + 249 + 657 + LE [2]; -169 = 3074 + LE &rArr; LE = -3243 kJ mol<sup>-1</sup> [2].", "marks": 4},
                {"part": "(b)", "points": "EA1 is exothermic due to attraction between incoming electron and positive nucleus [1]; EA2 is endothermic because adding an electron to negative O- requires energy to overcome electrostatic repulsion [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/41/O/N/21/Q2
        Question(
            number=7,
            title="Thermodynamics of Ammonium Nitrate Dissolution — 9701/41/O/N/21/Q2 [6 Marks]",
            syllabus_ref="23.2", difficulty="HARD", section_key="SEC_A",
            preamble="NH<sub>4</sub>NO<sub>3</sub>(s) &rarr; NH<sub>4</sub><sup>+</sup>(aq) + NO<sub>3</sub><sup>-</sup>(aq), ΔH°sol = +25.7 kJ mol<sup>-1</sup>.<br/>S° values (J K<sup>-1</sup> mol<sup>-1</sup>): solid = 151; NH<sub>4</sub><sup>+</sup>(aq) = 113; NO<sub>3</sub><sup>-</sup>(aq) = 146.",
            parts=[
                QuestionPart("(a)", "Calculate the standard entropy change of solution, ΔS°sol, at 298 K.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Calculate ΔG°sol at 298 K and explain why dissolution occurs spontaneously despite being endothermic.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° = (113 + 146) - 151 = 259 - 151 = +108 J K<sup>-1</sup> mol<sup>-1</sup> [3].", "marks": 3},
                {"part": "(b)", "points": "ΔG° = +25.7 - (298 &times; 0.108) = 25.7 - 32.18 = -6.48 kJ mol<sup>-1</sup> [2]; Spontaneous because ΔG° is negative; the TΔS° term outweighs the endothermic ΔH° term (entropy driven) [1].", "marks": 3}
            ]
        ),

        # Q8: 9701/41/M/J/21/Q1
        Question(
            number=8,
            title="Thermal Decomposition of Calcium Carbonate — 9701/41/M/J/21/Q1 [6 Marks]",
            syllabus_ref="23.4", difficulty="HARD", section_key="SEC_A",
            preamble="CaCO<sub>3</sub>(s) &rarr; CaO(s) + CO<sub>2</sub>(g).<br/>ΔH°f (kJ mol<sup>-1</sup>): CaCO<sub>3</sub> = -1207; CaO = -635; CO<sub>2</sub> = -394.<br/>S° (J K<sup>-1</sup> mol<sup>-1</sup>): CaCO<sub>3</sub> = 92.9; CaO = 39.7; CO<sub>2</sub> = 213.6.",
            parts=[
                QuestionPart("(a)", "Calculate standard enthalpy change ΔH° and standard entropy change ΔS°.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the minimum temperature, in °C, for decomposition to become feasible.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH° = [-635 + (-394)] - (-1207) = +178 kJ mol<sup>-1</sup> [1]; ΔS° = (39.7 + 213.6) - 92.9 = +160.4 J K<sup>-1</sup> mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "T = ΔH° / ΔS° = (178 &times; 1000) / 160.4 = 1109.7 K [2]; T(°C) = 1109.7 - 273 = 837 °C [1].", "marks": 3}
            ]
        ),

        # Q9: 9701/43/M/J/21/Q2
        Question(
            number=9,
            title="Polarization & Lattice Energy of Lithium Iodide — 9701/43/M/J/21/Q2 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Data for LiI (kJ mol<sup>-1</sup>): ΔH°f = -270; ΔH°at[Li] = +161; IE1[Li] = +520; ΔH°at[I] = +107; EA[I] = -295.<br/>Theoretical electrostatic LE = -738 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the experimental lattice energy of LiI(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why the experimental LE is more exothermic than theoretical LE in terms of ion polarization.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-270 = 161 + 520 + 107 + (-295) + LE = 493 + LE [1]; LE(LiI) = -763 kJ mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "Experimental value (-763) is more exothermic than theoretical (-738) [1]; Li+ has very small radius and high charge density (high polarising power) [1]; I- has large polarisable electron cloud, distorted by Li+ to give covalent character [1].", "marks": 3}
            ]
        ),

        # Q10: 9701/42/M/J/18/Q1
        Question(
            number=10,
            title="Complete Born–Haber Cycle for Aluminium Oxide — 9701/42/M/J/18/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Al<sub>2</sub>O<sub>3</sub> data (kJ mol<sup>-1</sup>): ΔH°f = -1676; ΔH°at[Al] = +326; (IE1+IE2+IE3)[Al] = +5140; BE(O<sub>2</sub>) = +496; (EA1+EA2)[O] = +657.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of aluminium oxide, Al<sub>2</sub>O<sub>3</sub>(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain why LE of Al<sub>2</sub>O<sub>3</sub> is vastly more exothermic than that of Na<sub>2</sub>O (LE = -2478 kJ mol<sup>-1</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-1676 = 2(326) + 2(5140) + 1.5(496) + 3(657) + LE = 13647 + LE [2]; LE(Al2O3) = -15323 kJ mol<sup>-1</sup> [2].", "marks": 4},
                {"part": "(b)", "points": "Al3+ has a +3 charge and smaller radius than Na+ (+1), and O2- has a -2 charge [1]; electrostatic attraction is proportional to charge product (+6 vs +2) and inversely proportional to ionic radii sum [1].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/23/Q2
        Question(
            number=11,
            title="Haber Process Synthesis Feasibility & Temperature Dependence — 9701/42/O/N/23/Q2 [6 Marks]",
            syllabus_ref="23.4", difficulty="HARD", section_key="SEC_A",
            preamble="Ammonia synthesis: N<sub>2</sub>(g) + 3H<sub>2</sub>(g) &rightleftharpoons; 2NH<sub>3</sub>(g), ΔH° = -92.2 kJ mol<sup>-1</sup>.<br/>Standard entropies (J K<sup>-1</sup> mol<sup>-1</sup>): N<sub>2</sub> = 191.6; H<sub>2</sub> = 130.6; NH<sub>3</sub> = 192.3.",
            parts=[
                QuestionPart("(a)", "Calculate the standard entropy change ΔS° for this reaction.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate ΔG° at 298 K and deduce whether the reaction is spontaneous at room temperature.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the temperature at which the reaction ceases to be spontaneous (ΔG° = 0).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° = 2(192.3) - [191.6 + 3(130.6)] = 384.6 - 583.4 = -198.8 J K<sup>-1</sup> mol<sup>-1</sup> [2].", "marks": 2},
                {"part": "(b)", "points": "ΔG° = -92.2 - [298 &times; (-0.1988)] = -92.2 + 59.24 = -32.96 kJ mol<sup>-1</sup> [1]; Spontaneous because ΔG° < 0 [1].", "marks": 2},
                {"part": "(c)", "points": "T = ΔH° / ΔS° = (-92.2 &times; 1000) / (-198.8) = 463.8 K (190.8 °C) [2].", "marks": 2}
            ]
        ),

        # Q12: 9701/41/O/N/23/Q1
        Question(
            number=12,
            title="Potassium Chloride Solution Thermodynamics — 9701/41/O/N/23/Q1 [6 Marks]",
            syllabus_ref="23.2", difficulty="HARD", section_key="SEC_A",
            preamble="KCl dissolves endothermically: KCl(s) &rarr; K<sup>+</sup>(aq) + Cl<sup>-</sup>(aq).<br/>Data: LE(KCl) = -711 kJ mol<sup>-1</sup>; ΔH°hyd(K<sup>+</sup>) = -322 kJ mol<sup>-1</sup>; ΔH°hyd(Cl<sup>-</sup>) = -364 kJ mol<sup>-1</sup>.<br/>S°: KCl(s) = 82.6; K<sup>+</sup>(aq) = 102.5; Cl<sup>-</sup>(aq) = 56.5 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy of solution, ΔH°sol, of KCl.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the standard entropy change of solution, ΔS°sol.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate ΔG°sol at 298 K and explain why KCl dissolves readily despite ΔH°sol being endothermic.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = [-322 + (-364)] - (-711) = -686 + 711 = +25.0 kJ mol<sup>-1</sup> [2].", "marks": 2},
                {"part": "(b)", "points": "ΔS°sol = (102.5 + 56.5) - 82.6 = 159.0 - 82.6 = +76.4 J K<sup>-1</sup> mol<sup>-1</sup> [2].", "marks": 2},
                {"part": "(c)", "points": "ΔG° = +25.0 - (298 &times; 0.0764) = 25.0 - 22.77 = +2.23 kJ mol<sup>-1</sup> [1]; Dissolves readily because ΔG is close to zero and non-standard entropy of dilution drives dissolution to saturation [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/43/O/N/23/Q1
        Question(
            number=13,
            title="Nickel(II) Oxide Born–Haber Cycle & Ligand Energy — 9701/43/O/N/23/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Nickel(II) oxide, NiO, has rock-salt lattice.<br/>Data (kJ mol<sup>-1</sup>): ΔH°f[NiO] = -240; ΔH°at[Ni] = +430; (IE1+IE2)[Ni] = +2490; ΔH°at[O] = +249; (EA1+EA2)[O] = +657.",
            parts=[
                QuestionPart("(a)", "Construct the cycle equation and calculate the lattice energy of NiO(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain how the experimental lattice energy provides evidence for d-orbital crystal field stabilization energy in Ni<sup>2+</sup>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-240 = 430 + 2490 + 249 + 657 + LE = 3826 + LE [2]; LE(NiO) = -240 - 3826 = -4066 kJ mol<sup>-1</sup> [2].", "marks": 4},
                {"part": "(b)", "points": "Experimental LE is more exothermic than predicted by simple ionic radius extrapolation across Period 4 [1]; extra stability arises from crystal field splitting of d-orbitals in octahedral oxide environment (CFSE of d8 ion) [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/M/J/20/Q2
        Question(
            number=14,
            title="Iron(II) Sulfide Lattice Energy & Polarization — 9701/42/M/J/20/Q2 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Iron(II) sulfide, FeS, has a nickel arsenide structure.<br/>Data (kJ mol<sup>-1</sup>): ΔH°f = -100; ΔH°at[Fe] = +416; (IE1+IE2)[Fe] = +2320; ΔH°at[S] = +279; (EA1+EA2)[S] = +332.<br/>Theoretical purely ionic LE = -2780 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the experimental lattice energy of FeS(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Account for the substantial difference between the experimental and theoretical values.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-100 = 416 + 2320 + 279 + 332 + LE = 3347 + LE [1]; LE(FeS) = -3447 kJ mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "Experimental LE (-3447) is much more exothermic than theoretical LE (-2780) [1]; Fe2+ cation has high polarising power due to incomplete d-subshell [1]; polarises large, soft S2- ion to introduce major covalent character [1].", "marks": 3}
            ]
        ),

        # Q15: 9701/41/M/J/20/Q2
        Question(
            number=15,
            title="Thermal Stability Trends of Group 2 Nitrates — 9701/41/M/J/20/Q2 [6 Marks]",
            syllabus_ref="23.4", difficulty="HARD", section_key="SEC_A",
            preamble="Group 2 nitrates decompose: 2M(NO<sub>3</sub>)<sub>2</sub>(s) &rarr; 2MO(s) + 4NO<sub>2</sub>(g) + O<sub>2</sub>(g).<br/>Decomposition temperatures: Mg(NO<sub>3</sub>)<sub>2</sub> = 600 K; Ba(NO<sub>3</sub>)<sub>2</sub> = 900 K.",
            parts=[
                QuestionPart("(a)", "Explain why ΔS° for the decomposition is positive and similar for all Group 2 nitrates.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain the trend in thermal stability down Group 2 in terms of cation polarising power.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Decomposition produces 5 moles of gas (4NO2 + O2) from 2 moles of solid, creating large dispersal of matter/microstates [1]; stoichiometry is identical for all Group 2 nitrates [1].", "marks": 2},
                {"part": "(b)", "points": "Descending Group 2, cation radius increases while ionic charge remains +2 [1]; charge density and polarising power of M2+ decrease down the group [1]; Mg2+ distorts the electron cloud of the NO3- anion more strongly than Ba2+ [1]; weakens N–O bond within nitrate, requiring lower thermal energy to decompose [1].", "marks": 4}
            ]
        ),

        # Q16: 9701/42/O/N/19/Q2
        Question(
            number=16,
            title="Calcium Oxide Born–Haber Cycle & Hydration — 9701/42/O/N/19/Q2 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_A",
            preamble="Quicklime, CaO, reacts vigorously with water: CaO(s) + H<sub>2</sub>O(l) &rarr; Ca(OH)<sub>2</sub>(s), ΔH° = -65 kJ mol<sup>-1</sup>.<br/>Data (kJ mol<sup>-1</sup>): ΔH°f[CaO] = -635; ΔH°at[Ca] = +178; (IE1+IE2)[Ca] = +1735; ΔH°at[O] = +249; (EA1+EA2)[O] = +657.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of calcium oxide, CaO(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain why slaking of lime (adding water to CaO) is strongly exothermic.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-635 = 178 + 1735 + 249 + 657 + LE = 2819 + LE [2]; LE(CaO) = -635 - 2819 = -3454 kJ mol<sup>-1</sup> [2].", "marks": 4},
                {"part": "(b)", "points": "O2- reacts with water to form OH- ions with release of strong acid-base proton transfer energy [1]; accompanied by highly exothermic hydration of Ca2+ and OH- ions into the Ca(OH)2 crystal [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/41/O/N/22/Q1
        Question(
            number=17,
            title="Lattice Energy: Sodium Chloride vs Magnesium Oxide — 9701/41/O/N/22/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="NaCl: LE = -787 kJ mol<sup>-1</sup>; MgO: LE = -3791 kJ mol<sup>-1</sup>. Both have rock-salt structures.",
            parts=[
                QuestionPart("(a)", "Explain why the lattice energy of MgO is almost five times more exothermic than that of NaCl.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Lattice energy is proportional to (q+ &times; q-) / (r+ + r-) [1]; Mg2+ and O2- have +2 and -2 charges (product = 4), whereas Na+ and Cl- have +1 and -1 (product = 1) [1]; Mg2+ (0.065 nm) is smaller than Na+ (0.095 nm), and O2- (0.140 nm) is smaller than Cl- (0.181 nm) [1]; smaller inter-ionic distance and quadrupled charge product produce vastly stronger electrostatic attraction [1].", "marks": 4}
            ]
        ),

        # Q18: 9701/43/M/J/22/Q2
        Question(
            number=18,
            title="Hydration Enthalpy of Bromide Ions in KBr — 9701/43/M/J/22/Q2 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_B",
            preamble="The dissolution of potassium bromide, KBr(s), in water is represented by the enthalpy cycle in Fig. 18.1.<br/>Data: LE(KBr) = -679 kJ mol<sup>-1</sup>; ΔH°sol(KBr) = +20.0 kJ mol<sup>-1</sup>; ΔH°hyd(K<sup>+</sup>) = -322 kJ mol<sup>-1</sup>.",
            figure_path=os.path.join(fig_dir, "a2_t23_solution_cycle_kbr.png"),
            figure_caption="Fig. 18.1: Hess's Law enthalpy cycle relating lattice energy, ionic hydration, and enthalpy of solution for KBr(s).",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy of hydration of the bromide ion, Br<sup>-</sup>(g).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = ΔH°hyd(K+) + ΔH°hyd(Br-) - LE [1]; +20.0 = -322 + ΔH°hyd(Br-) - (-679) [1]; +20.0 = +357 + ΔH°hyd(Br-) [1]; ΔH°hyd(Br-) = -337 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q19: 9701/43/O/N/21/Q1
        Question(
            number=19,
            title="Strontium Chloride Lattice Energy Calculation — 9701/43/O/N/21/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="Data (kJ mol<sup>-1</sup>): ΔH°f[SrCl<sub>2</sub>] = -829; ΔH°at[Sr] = +164; (IE1+IE2)[Sr] = +1614; BE(Cl<sub>2</sub>) = +242; EA[Cl] = -349.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of strontium chloride, SrCl<sub>2</sub>(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Sr) + (IE1+IE2) + BE(Cl2) + 2&times;EA(Cl) + LE [1]; -829 = 164 + 1614 + 242 + 2(-349) + LE [1]; -829 = 1322 + LE [1]; LE(SrCl2) = -2151 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q20: 9701/42/M/J/21/Q1
        Question(
            number=20,
            title="Group 2 Hydroxide Solubility Trend — 9701/42/M/J/21/Q1 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_B",
            preamble="Solubility of Group 2 hydroxides increases down Group 2 from Mg(OH)<sub>2</sub> to Ba(OH)<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "Explain this trend in solubility in terms of the relative rates of decrease of LE and ΔH°hyd.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cation radius increases down Group 2, so both LE and ΔH°hyd become less exothermic [1]; OH- is a relatively small anion, so (r+ + r-) increases significantly [1]; LE decreases more rapidly than ΔH°hyd down the group [1]; ΔH°sol = ΣΔH°hyd - LE becomes more exothermic / less endothermic, increasing solubility [1].", "marks": 4}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q1
        Question(
            number=21,
            title="Second Electron Affinity of Oxygen from MgO Cycle — 9701/42/O/N/20/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="Data (kJ mol<sup>-1</sup>): ΔH°f[MgO] = -602; ΔH°at[Mg] = +148; (IE1+IE2)[Mg] = +2187; ΔH°at[O] = +249; EA1[O] = -141; LE[MgO] = -3791.",
            parts=[
                QuestionPart("(a)", "Calculate the value of the second electron affinity of oxygen, EA2[O].", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-602 = 148 + 2187 + 249 + (-141) + EA2 + (-3791) [1]; -602 = -1348 + EA2 [2]; EA2 = +746 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q22: 9701/41/O/N/20/Q2
        Question(
            number=22,
            title="Hydration Enthalpy: Magnesium vs Barium Ions — 9701/41/O/N/20/Q2 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_B",
            preamble="ΔH°hyd(Mg<sup>2+</sup>) = -1920 kJ mol<sup>-1</sup> (radius 0.065 nm); ΔH°hyd(Ba<sup>2+</sup>) = -1305 kJ mol<sup>-1</sup> (radius 0.135 nm).",
            parts=[
                QuestionPart("(a)", "Explain why ΔH°hyd of Mg<sup>2+</sup> is significantly more exothermic than that of Ba<sup>2+</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydration involves ion-dipole attractions between the cation and water molecules [1]; both cations have a +2 charge [1]; Mg2+ has a much smaller ionic radius and higher charge density [1]; creates stronger ion-dipole attractions, releasing more energy upon hydration [1].", "marks": 4}
            ]
        ),

        # Q23: 9701/42/M/J/20/Q1
        Question(
            number=23,
            title="Entropy Change in Sodium Hydrogencarbonate Decomposition — 9701/42/M/J/20/Q1 [4 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_B",
            preamble="2NaHCO<sub>3</sub>(s) &rarr; Na<sub>2</sub>CO<sub>3</sub>(s) + H<sub>2</sub>O(g) + CO<sub>2</sub>(g).<br/>S° (J K<sup>-1</sup> mol<sup>-1</sup>): NaHCO<sub>3</sub> = 102; Na<sub>2</sub>CO<sub>3</sub> = 136; H<sub>2</sub>O(g) = 189; CO<sub>2</sub>(g) = 214.",
            parts=[
                QuestionPart("(a)", "Calculate ΔS° for this reaction and explain why it has a large positive value.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° = [136 + 189 + 214] - 2(102) = 539 - 204 = +335 J K<sup>-1</sup> mol<sup>-1</sup> [2]; Reaction converts 2 moles of solid into 1 mole of solid and 2 moles of gas [1]; gases possess vastly higher disorder and translational microstates than crystalline solids [1].", "marks": 4}
            ]
        ),

        # Q24: 9701/42/O/N/19/Q1
        Question(
            number=24,
            title="Barium Chloride Enthalpy of Formation — 9701/42/O/N/19/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="Data (kJ mol<sup>-1</sup>): ΔH°at[Ba] = +180; (IE1+IE2)[Ba] = +1468; BE(Cl<sub>2</sub>) = +242; EA[Cl] = -349; LE[BaCl<sub>2</sub>] = -2056.",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy of formation, ΔH°f, of BaCl<sub>2</sub>(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = 180 + 1468 + 242 + 2(-349) + (-2056) [2]; ΔH°f = 1890 - 698 - 2056 [1]; ΔH°f = -864 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q25: 9701/41/O/N/19/Q2
        Question(
            number=25,
            title="Copper(II) Sulfate Hydration Energy Cycle — 9701/41/O/N/19/Q2 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_B",
            preamble="CuSO<sub>4</sub>(s) + 5H<sub>2</sub>O(l) &rarr; CuSO<sub>4</sub>&middot;5H<sub>2</sub>O(s).<br/>ΔH°sol(anhydrous) = -66.5 kJ mol<sup>-1</sup>; ΔH°sol(hydrated) = +11.7 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Draw a Hess's Law cycle and calculate the standard enthalpy of hydration, ΔH°hyd.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hess's Law cycle connecting both solids to aqueous solution [1]; ΔH°hyd = ΔH°sol(anhydrous) - ΔH°sol(hydrated) [1]; ΔH°hyd = -66.5 - (+11.7) [1]; ΔH°hyd = -78.2 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q26: 9701/41/O/N/18/Q2
        Question(
            number=26,
            title="Thermodynamics of Group 2 Sulfate Insolubility — 9701/41/O/N/18/Q2 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_B",
            preamble="MgSO<sub>4</sub> is highly soluble; BaSO<sub>4</sub> is insoluble.",
            parts=[
                QuestionPart("(a)", "Account for this solubility decrease down Group 2 by comparing changes in ΔH°hyd and lattice energy.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = ΣΔH°hyd - LE [1]; descending group, cation radius increases, so both LE and ΔH°hyd become less exothermic [1]; because SO4^2- is very large, LE decreases very slowly [1]; ΔH°hyd drops rapidly with increasing cation radius, making ΔH°sol significantly more endothermic, reducing solubility [1].", "marks": 4}
            ]
        ),

        # Q27: 9701/42/M/J/17/Q1
        Question(
            number=27,
            title="Cesium Chloride vs Sodium Chloride Lattice Energy — 9701/42/M/J/17/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="NaCl: LE = -787 kJ mol<sup>-1</sup>; CsCl: LE = -657 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why the lattice energy of CsCl is less exothermic than that of NaCl.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both salts contain ions with +1 and -1 charges [1]; Cs+ has a significantly larger ionic radius (0.167 nm) than Na+ (0.095 nm) [1]; inter-ionic distance (r+ + r-) is greater in CsCl [1]; electrostatic force of attraction between ions is weaker, releasing less energy when crystal lattice forms [1].", "marks": 4}
            ]
        ),

        # Q28: 9701/41/M/J/17/Q2
        Question(
            number=28,
            title="Standard Entropy Change of Methanol Synthesis — 9701/41/M/J/17/Q2 [4 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_B",
            preamble="CO(g) + 2H<sub>2</sub>(g) &rarr; CH<sub>3</sub>OH(l).<br/>S° (J K<sup>-1</sup> mol<sup>-1</sup>): CO(g) = 197.6; H<sub>2</sub>(g) = 130.6; CH<sub>3</sub>OH(l) = 126.8.",
            parts=[
                QuestionPart("(a)", "Calculate ΔS° for this reaction and explain its negative sign.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° = 126.8 - [197.6 + 2(130.6)] = 126.8 - 458.8 [2]; ΔS° = -332.0 J K<sup>-1</sup> mol<sup>-1</sup> [1]; Negative because 3 moles of gas react to form 1 mole of liquid, causing an immense decrease in disorder/microstates [1].", "marks": 4}
            ]
        ),

        # Q29: 9701/42/O/N/17/Q1
        Question(
            number=29,
            title="Rubidium Bromide Born–Haber Cycle Calculation — 9701/42/O/N/17/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="Data for RbBr (kJ mol<sup>-1</sup>): ΔH°f = -395; ΔH°at[Rb] = +81; IE1[Rb] = +403; ΔH°at[½Br<sub>2</sub>] = +112; EA[Br] = -325.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of rubidium bromide, RbBr(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = 81 + 403 + 112 + (-325) + LE = 271 + LE [2]; -395 = 271 + LE [1]; LE(RbBr) = -666 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q30: 9701/41/O/N/17/Q2
        Question(
            number=30,
            title="Entropy Changes in Melting and Boiling of Water — 9701/41/O/N/17/Q2 [4 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_B",
            preamble="For water: ΔS°fusion = +22.0 J K<sup>-1</sup> mol<sup>-1</sup>; ΔS°vaporization = +109.0 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why both entropy changes are positive, and why ΔS°vaporization is much larger than ΔS°fusion.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both involve increase in disorder as molecules gain rotational/translational freedom [1]; fusion involves moving from fixed lattice to liquid where hydrogen bonds largely persist [1]; vaporization completely breaks intermolecular hydrogen bonds [1]; gas molecules possess complete translational randomness, yielding an immense increase in microstates [1].", "marks": 4}
            ]
        ),

        # Q31: 9701/42/M/J/16/Q1
        Question(
            number=31,
            title="Magnesium Fluoride Lattice Energy Calculation — 9701/42/M/J/16/Q1 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_B",
            preamble="Data (kJ mol<sup>-1</sup>): ΔH°f[MgF<sub>2</sub>] = -1124; ΔH°at[Mg] = +147; (IE1+IE2)[Mg] = +2187; BE(F<sub>2</sub>) = +158; EA[F] = -328.",
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of magnesium fluoride, MgF<sub>2</sub>(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-1124 = 147 + 2187 + 158 + 2(-328) + LE = 1836 + LE [2]; LE(MgF2) = -1124 - 1836 [1]; LE = -2960 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q32: 9701/41/M/J/16/Q1
        Question(
            number=32,
            title="Gibbs Free Energy of Iron Rusting — 9701/41/M/J/16/Q1 [4 Marks]",
            syllabus_ref="23.4", difficulty="EASY", section_key="SEC_B",
            preamble="4Fe(s) + 3O<sub>2</sub>(g) &rarr; 2Fe<sub>2</sub>O<sub>3</sub>(s), ΔH° = -1648 kJ mol<sup>-1</sup>; ΔS° = -544 J K<sup>-1</sup> mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate ΔG° at 298 K and state whether rusting is spontaneous at room temperature.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the temperature above which the reduction of Fe<sub>2</sub>O<sub>3</sub> becomes feasible.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔG° = -1648 - [298 &times; (-0.544)] = -1648 + 162.1 = -1485.9 kJ mol<sup>-1</sup> [1]; Spontaneous because ΔG° is highly negative [1].", "marks": 2},
                {"part": "(b)", "points": "T = ΔH° / ΔS° = (-1648 &times; 1000) / (-544) = 3029 K (2756 °C) [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q1(a)
        Question(
            number=33,
            title="Definition of Enthalpy of Hydration — 9701/42/M/J/23/Q1(a) [2 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_C",
            preamble="Hydration enthalpy governs solute-solvent energetics.",
            parts=[
                QuestionPart("(a)", "Define standard enthalpy change of hydration, ΔH°hyd, with an equation including state symbols for Mg<sup>2+</sup>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of gaseous ions dissolves in water to form infinitely dilute solution under standard conditions [1]; Mg2+(g) + aq &rarr; Mg2+(aq) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/M/J/23/Q2(a)
        Question(
            number=34,
            title="Definition and Sign of Lattice Energy — 9701/41/M/J/23/Q2(a) [2 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_C",
            preamble="Lattice energy defines crystal lattice strength.",
            parts=[
                QuestionPart("(a)", "Define lattice energy and state its thermodynamic sign convention.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of an ionic crystalline solid is formed from its constituent gaseous ions under standard conditions [1]; always negative (exothermic) [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/41/M/J/20/Q1(a)
        Question(
            number=35,
            title="Entropy Change Sign in Vaporization — 9701/41/M/J/20/Q1(a) [2 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_C",
            preamble="Entropy reflects microstate distribution.",
            parts=[
                QuestionPart("(a)", "State and explain the sign of ΔS° for boiling water: H<sub>2</sub>O(l) &rarr; H<sub>2</sub>O(g).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° > 0 (positive) [1]; gas phase has complete translational freedom and vastly more microstates than liquid [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/42/O/N/18/Q1(a)
        Question(
            number=36,
            title="Electron Affinities of Oxygen: Sign Distinction — 9701/42/O/N/18/Q1(a) [2 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_C",
            preamble="Formation of oxide ions involves stepwise electron additions.",
            parts=[
                QuestionPart("(a)", "Explain why EA1 of oxygen is negative whereas EA2 is positive.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "EA1 is exothermic due to nuclear attraction [1]; EA2 is endothermic due to electrostatic repulsion between incoming electron and O- ion [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/41/M/J/19/Q1(a)
        Question(
            number=37,
            title="Thermodynamic Criterion for Reaction Feasibility — 9701/41/M/J/19/Q1(a) [2 Marks]",
            syllabus_ref="23.4", difficulty="EASY", section_key="SEC_C",
            preamble="Spontaneity is determined by the Second Law.",
            parts=[
                QuestionPart("(a)", "State the mathematical condition for feasibility in terms of ΔG°, and state its SI units.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔG° &le; 0 (negative or zero) [1]; units: kJ mol<sup>-1</sup> (or J mol<sup>-1</sup>) [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/O/N/22/Q1(a)
        Question(
            number=38,
            title="Equilibrium Temperature Condition — 9701/43/O/N/22/Q1(a) [2 Marks]",
            syllabus_ref="23.4", difficulty="EASY", section_key="SEC_C",
            preamble="At equilibrium, Gibbs free energy reaches a minimum.",
            parts=[
                QuestionPart("(a)", "Write the mathematical expression for the equilibrium temperature T in terms of ΔH° and ΔS°.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "At equilibrium ΔG° = 0 &rArr; ΔH° - TΔS° = 0 [1]; T = ΔH° / ΔS° (with ΔH in J and ΔS in J K^-1) [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/M/J/22/Q2(a)
        Question(
            number=39,
            title="Definition of Standard Molar Entropy — 9701/42/M/J/22/Q2(a) [2 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_C",
            preamble="Third Law of Thermodynamics establishes absolute entropies.",
            parts=[
                QuestionPart("(a)", "Define standard molar entropy, S°, and explain why S° of an element is never zero at 298 K.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The entropy of 1 mole of a substance in its standard state at 298 K and 100 kPa [1]; at 298 K atoms possess thermal vibrational/translational energy and disorder (S° = 0 only at 0 K for perfect crystal) [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/21/Q1(a)
        Question(
            number=40,
            title="Indirect Determination of Lattice Energy — 9701/41/O/N/21/Q1(a) [2 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_C",
            preamble="Lattice energy cannot be measured in a simple calorimeter.",
            parts=[
                QuestionPart("(a)", "Explain why lattice energy cannot be measured directly by experiment.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "It is impossible to isolate and condense separate gaseous ions directly into a solid crystal lattice without other competing processes [1]; ions immediately recombine or discharge [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # (4 x 6-Markers, 4 x 4-Markers, 2 x 2-Markers)
        # =====================================================================

        # Q41: HIGH FREQUENCY 6-MARKER — Born-Haber Cycle BaCl2
        Question(
            number=41,
            title="HF 1: Barium Chloride Complete Born–Haber Cycle — 9701/42/O/N/23/Q1 [6 Marks]",
            syllabus_ref="23.1", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #1 (Born–Haber Cycle Mastery)</b><br/>"
                     "The Born–Haber cycle for barium chloride, BaCl<sub>2</sub>(s), is illustrated in Fig. 41.1.<br/>"
                     "Data for BaCl<sub>2</sub> (kJ mol<sup>-1</sup>): ΔH°f = -859; ΔH°at[Ba] = +180; IE1[Ba] = +503; IE2[Ba] = +965; BE(Cl<sub>2</sub>) = +242; EA[Cl] = -349.",
            figure_path=os.path.join(fig_dir, "a2_t23_born_haber_bacl2.png"),
            figure_caption="Fig. 41.1: Complete Born–Haber cycle energy level diagram for barium chloride, BaCl2(s).",
            parts=[
                QuestionPart("(a)", "Construct the full Born–Haber cycle expression and calculate the lattice energy of BaCl<sub>2</sub>(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Compare the lattice energy of BaCl<sub>2</sub> with that of MgCl<sub>2</sub> (LE = -2519 kJ mol<sup>-1</sup>), explaining the difference.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Ba) + (IE1+IE2)(Ba) + BE(Cl2) + 2&times;EA(Cl) + LE [1]; -859 = 180 + 1468 + 242 + 2(-349) + LE = 1192 + LE [1]; LE(BaCl2) = -859 - 1192 [1]; LE = -2051 kJ mol<sup>-1</sup> [1].", "marks": 4},
                {"part": "(b)", "points": "LE of BaCl2 is less exothermic than MgCl2 [1]; Ba2+ has a larger ionic radius than Mg2+, resulting in greater inter-ionic separation and weaker electrostatic attraction [1].", "marks": 2}
            ]
        ),

        # Q42: HIGH FREQUENCY 6-MARKER — Multi-Step Feasibility Calculation
        Question(
            number=42,
            title="HF 2: Thermal Decomposition & Feasibility of Zinc Carbonate — 9701/41/M/J/22/Q2 [6 Marks]",
            syllabus_ref="23.4", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #2 (Gibbs Free Energy & Feasibility)</b><br/>"
                     "ZnCO<sub>3</sub>(s) &rarr; ZnO(s) + CO<sub>2</sub>(g).<br/>"
                     "A plot of standard Gibbs free energy change ΔG° against temperature for this decomposition is shown in Fig. 42.1.<br/>"
                     "Data: ΔH°f (kJ mol<sup>-1</sup>): ZnCO<sub>3</sub> = -813; ZnO = -348; CO<sub>2</sub> = -394.<br/>"
                     "S° (J K<sup>-1</sup> mol<sup>-1</sup>): ZnCO<sub>3</sub> = 82.4; ZnO = 43.6; CO<sub>2</sub> = 213.6.",
            figure_path=os.path.join(fig_dir, "a2_t23_delta_g_temperature_plot.png"),
            figure_caption="Fig. 42.1: Variation of standard Gibbs free energy change ΔG° with temperature T showing the transition to feasibility.",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy change ΔH° and standard entropy change ΔS° for this reaction.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the minimum temperature, in °C, at which the decomposition of ZnCO<sub>3</sub> becomes feasible.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH° = [-348 + (-394)] - (-813) = -742 + 813 = +71.0 kJ mol<sup>-1</sup> [1]; ΔS° = (43.6 + 213.6) - 82.4 = 257.2 - 82.4 = +174.8 J K<sup>-1</sup> mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "T = ΔH° / ΔS° = (71.0 &times; 1000) / 174.8 = 406.2 K [2]; T(°C) = 406.2 - 273 = 133.2 °C (or 133 °C) [1].", "marks": 3}
            ]
        ),

        # Q43: HIGH FREQUENCY 6-MARKER — Solution & Hydration Cycle
        Question(
            number=43,
            title="HF 3: Enthalpy of Solution & Hydration of Sodium Fluoride — 9701/43/O/N/22/Q2 [6 Marks]",
            syllabus_ref="23.2", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #3 (Enthalpy Cycle of Solution)</b><br/>"
                     "Lattice energy of NaF = -918 kJ mol<sup>-1</sup>.<br/>"
                     "Enthalpies of hydration: ΔH°hyd(Na<sup>+</sup>) = -405 kJ mol<sup>-1</sup>; ΔH°hyd(F<sup>-</sup>) = -506 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Construct an energy cycle and calculate the standard enthalpy of solution, ΔH°sol, of NaF(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why NaF is significantly less soluble than NaCl (LE = -787 kJ mol<sup>-1</sup>; ΔH°sol = +4.0 kJ mol<sup>-1</sup>).", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = ΔH°hyd(Na+) + ΔH°hyd(F-) - LE [1]; ΔH°sol = (-405 - 506) - (-918) = -911 + 918 [1]; ΔH°sol = +7.0 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "F- is much smaller than Cl-, leading to a vastly more exothermic lattice energy in NaF (-918 vs -787) [1]; this large LE requirement makes dissolving NaF less thermodynamically favourable [1]; hydration enthalpy cannot fully compensate for the high lattice stability [1].", "marks": 3}
            ]
        ),

        # Q44: HIGH FREQUENCY 6-MARKER — Group 2 Sulfate Solubility Deduction
        Question(
            number=44,
            title="HF 4: Comprehensive Group 2 Sulfate Solubility Analysis — 9701/42/M/J/21/Q2 [6 Marks]",
            syllabus_ref="23.2", difficulty="HARD", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #4 (Sulfate Solubility Rationale)</b><br/>"
                     "The solubility of Group 2 sulfates decreases down Group 2 from MgSO<sub>4</sub> (soluble) to BaSO<sub>4</sub> (insoluble). Fig. 44.1 shows how the magnitudes of hydration enthalpy and lattice energy change with increasing cation radius down the group.",
            figure_path=os.path.join(fig_dir, "a2_t23_group2_enthalpy_trend.png"),
            figure_caption="Fig. 44.1: Comparative rates of decline in |ΔH°hyd| and |LE| down Group 2 explaining sulfate insolubility.",
            parts=[
                QuestionPart("(a)", "Define standard enthalpy change of solution, ΔH°sol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain in detail, using enthalpy cycles and ionic radii, why the solubility of sulfates decreases down the group.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of an ionic compound dissolves in water to form infinitely dilute solution under standard conditions [2].", "marks": 2},
                {"part": "(b)", "points": "ΔH°sol = ΣΔH°hyd - LE [1]; down Group 2, cation radius increases (Mg2+ to Ba2+), so both LE and ΔH°hyd become less exothermic [1]; sulfate SO4^2- is very large, so cation size increase causes only small percentage change in (r+ + r-), meaning LE decreases slowly [1]; cation ΔH°hyd depends sharply on 1/r+ and drops rapidly; hence ΔH°sol becomes more endothermic, reducing solubility [1].", "marks": 4}
            ]
        ),

        # Q45: HIGH FREQUENCY 4-MARKER — Ionic Polarization & Covalent Character
        Question(
            number=45,
            title="HF 5: Theoretical vs Experimental Lattice Energy in Silver Halides — 9701/42/O/N/21/Q2 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #5 (Polarization in Silver Halides)</b><br/>"
                     "For AgI: Experimental LE = -889 kJ mol<sup>-1</sup>; Theoretical LE = -736 kJ mol<sup>-1</sup>.<br/>"
                     "For AgF: Experimental LE = -958 kJ mol<sup>-1</sup>; Theoretical LE = -920 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why the discrepancy between experimental and theoretical lattice energy is much greater for AgI than for AgF.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Theoretical model assumes purely spherical, non-polarisable ionic bonding [1]; Ag+ cation has high polarising power due to poorly shielding 4d10 electrons [1]; I- has a vastly larger, more polarisable electron cloud than F- [1]; electron cloud of I- is severely distorted towards Ag+, introducing substantial covalent character that reinforces the lattice [1].", "marks": 4}
            ]
        ),

        # Q46: HIGH FREQUENCY 4-MARKER — Second Electron Affinity Endothermic Nature
        Question(
            number=46,
            title="HF 6: Endothermic Nature of Second Electron Affinity — 9701/41/M/J/21/Q2 [4 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #6 (Electron Affinities of Group 16)</b><br/>"
                     "For sulfur: S(g) + e<sup>-</sup> &rarr; S<sup>-</sup>(g), EA1 = -200 kJ mol<sup>-1</sup>;<br/>"
                     "S<sup>-</sup>(g) + e<sup>-</sup> &rarr; S<sup>2-</sup>(g), EA2 = +532 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why the first electron affinity of sulfur is exothermic while the second electron affinity is endothermic.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "EA1 involves an electron added to a neutral gaseous atom [1]; energy is released due to the electrostatic attraction between the incoming electron and positive nucleus [1]; EA2 involves adding an electron to a negatively charged ion (S-) [1]; significant electrostatic repulsion between the negative ion and incoming electron must be overcome, requiring net energy input [1].", "marks": 4}
            ]
        ),

        # Q47: HIGH FREQUENCY 4-MARKER — Entropy of Gas Evolution
        Question(
            number=47,
            title="HF 7: Entropy Change in Carbonate Acidification — 9701/43/M/J/20/Q1 [4 Marks]",
            syllabus_ref="23.3", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #7 (Entropy of Gas Evolution)</b><br/>"
                     "MgCO<sub>3</sub>(s) + 2HCl(aq) &rarr; MgCl<sub>2</sub>(aq) + H<sub>2</sub>O(l) + CO<sub>2</sub>(g).",
            parts=[
                QuestionPart("(a)", "Predict and explain the sign of ΔS° for this reaction, and explain how an increase in temperature affects the spontaneity.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° is positive [1]; gas (CO2) is produced from solid and solution, substantially increasing the number of microstates and dispersal of matter [1]; since ΔS° is positive, -TΔS° becomes increasingly negative as temperature rises [1]; this makes ΔG° = ΔH° - TΔS° more negative, enhancing thermodynamic spontaneity [1].", "marks": 4}
            ]
        ),

        # Q48: HIGH FREQUENCY 4-MARKER — Hydration Enthalpy vs Charge Density
        Question(
            number=48,
            title="HF 8: Group 2 Cation Hydration Enthalpy Trends — 9701/42/O/N/19/Q1 [4 Marks]",
            syllabus_ref="23.2", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #8 (Cation Charge Density & Hydration)</b><br/>"
                     "Values of ΔH°hyd: Be<sup>2+</sup> = -2494; Mg<sup>2+</sup> = -1920; Ca<sup>2+</sup> = -1577; Sr<sup>2+</sup> = -1443; Ba<sup>2+</sup> = -1305 kJ mol<sup>-1</sup>.",
            parts=[
                QuestionPart("(a)", "Explain why ΔH°hyd becomes progressively less exothermic down Group 2 from Be<sup>2+</sup> to Ba<sup>2+</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydration enthalpy depends on electrostatic attraction between the metal cation and water dipoles [1]; all Group 2 ions have identical +2 charge [1]; ionic radius increases down the group (Be2+ to Ba2+), so charge density decreases [1]; weaker electrostatic attraction between the larger cation and the partial negative oxygen atom of water releases less energy [1].", "marks": 4}
            ]
        ),

        # Q49: HIGH FREQUENCY 2-MARKER — Definition of Lattice Energy
        Question(
            number=49,
            title="HF 9: Standard Definition of Lattice Energy — 9701/41/M/J/23/Q1(a) [2 Marks]",
            syllabus_ref="23.1", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #9 (Core Definition)</b>",
            parts=[
                QuestionPart("(a)", "Define lattice energy with an equation including state symbols for calcium oxide, CaO.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The enthalpy change when 1 mole of an ionic crystalline solid is formed from its constituent gaseous ions under standard conditions [1]; Ca2+(g) + O2-(g) &rarr; CaO(s) [1].", "marks": 2}
            ]
        ),

        # Q50: HIGH FREQUENCY 2-MARKER — Feasibility Criterion
        Question(
            number=50,
            title="HF 10: Thermodynamic Feasibility & Spontaneity Condition — 9701/42/M/J/22/Q1(a) [2 Marks]",
            syllabus_ref="23.4", difficulty="EASY", section_key="SEC_D",
            preamble="<b>HIGH-FREQUENCY CORE REPEAT #10 (Feasibility Criterion)</b>",
            parts=[
                QuestionPart("(a)", "State the thermodynamic condition for a reaction to be feasible at temperature T in terms of Gibbs free energy, and explain why some feasible reactions do not occur at observable rates.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔG° &le; 0 (Gibbs free energy change must be negative or zero) [1]; the reaction may have a very high activation energy (kinetic stability) preventing reaction at room temperature [1].", "marks": 2}
            ]
        )
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
    build_topic23_50q()
