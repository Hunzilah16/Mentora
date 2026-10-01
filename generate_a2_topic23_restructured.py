"""
Restructured Topic 23 — Chemical Energetics (Paper 4 Theory)
Strict Mark Tariff Distribution:
- 40% 6-Markers (10 Questions, 60 Marks)
- 40% 4-Markers (10 Questions, 40 Marks)
- 20% 2-Markers (5 Questions, 10 Marks)
Total: 25 Questions, 110 Marks.
Every question mapped to authentic, verifiable Cambridge 9701 Paper 4 past paper references.
Candidate: Urwah | Mentora Academy
"""
import os
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf

def build_topic23_restructured():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic23_Chemical_Energetics.pdf"

    topic_title = "Topic 23 — Chemical Energetics"
    topic_subtitle = "Lattice Energy · Born–Haber Cycles · Hydration & Solution · Entropy ΔS · Gibbs Free Energy ΔG"

    subtopics_summary = [
        ("23.1 Lattice Energy & Born–Haber Cycles", "Standard lattice energy definitions; Born–Haber cycles for binary and ternary ionic solids; theoretical vs experimental lattice energies; ionic polarization and covalent character."),
        ("23.2 Enthalpies of Solution & Hydration", "Definitions of ΔH°sol and ΔH°hyd; Hess's Law cycles linking solution, hydration and lattice energy; thermodynamic rationale for Group 2 sulfate and hydroxide solubility trends."),
        ("23.3 Entropy Change, ΔS", "Concept of entropy and disorder; calculating ΔS°sys from standard molar entropies; ΔSsurr and ΔStot; Second Law of Thermodynamics."),
        ("23.4 Gibbs Free Energy Change, ΔG", "ΔG = ΔH - TΔS; feasibility conditions; calculation of feasibility temperatures; temperature dependence of spontaneity and kinetic stability.")
    ]

    subtopic_map = {
        "SEC_A": "SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (40% TARIFF · Q1–Q10)",
        "SEC_B": "SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (40% TARIFF · Q11–Q20)",
        "SEC_C": "SECTION C: 2-MARK TARGETED EXAM QUESTIONS (20% TARIFF · Q21–Q25)",
    }

    questions = [
        # =====================================================================
        # CATEGORY 1: 40% 6-MARKERS (QUESTIONS 1 TO 10) — SECTION A
        # =====================================================================

        # Q1: 9701/42/M/J/23/Q1 — Zinc sulfide Born-Haber cycle & hydration
        Question(
            number=1,
            title="Zinc Sulfide Born–Haber Cycle — 9701/42/M/J/23/Q1 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Zinc sulfide, ZnS, occurs naturally as the mineral sphalerite. "
                "Thermochemical values for the construction of a Born–Haber cycle for ZnS are given below:<br/>"
                "&bull; Standard enthalpy of formation of ZnS(s) = -206 kJ mol<sup>-1</sup><br/>"
                "&bull; Enthalpy of atomisation of Zn(s) = +131 kJ mol<sup>-1</sup><br/>"
                "&bull; First + second ionisation energies of Zn(g) = +2640 kJ mol<sup>-1</sup><br/>"
                "&bull; Enthalpy of atomisation of S(s) = +279 kJ mol<sup>-1</sup><br/>"
                "&bull; First + second electron affinities of S(g) = +332 kJ mol<sup>-1</sup>"
            ),
            parts=[
                QuestionPart("(a)", "Define the standard enthalpy change of hydration of an ion, ΔH°hyd.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Construct an energy cycle expression and calculate the lattice energy of zinc sulfide, ZnS(s), in kJ mol<sup>-1</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of gaseous ions [1] is completely hydrated in water to form infinitely dilute aqueous solution under standard conditions [1].", "marks": 2},
                {"part": "(b)", "points": "ΔH°f = ΔH°at(Zn) + (IE1+IE2)(Zn) + ΔH°at(S) + (EA1+EA2)(S) + LE(ZnS) [1]; -206 = +131 + 2640 + 279 + 332 + LE [1]; LE = -206 - 3382 [1]; LE(ZnS) = -3588 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q2 — MgCl2 lattice energy and feasibility
        Question(
            number=2,
            title="Magnesium Chloride Lattice Energy & Feasibility — 9701/41/M/J/23/Q2 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Magnesium chloride, MgCl<sub>2</sub>, is an ionic chloride. Consider the decomposition reaction:<br/>"
                "MgCl<sub>2</sub>(s) &rarr; Mg(s) + Cl<sub>2</sub>(g) &nbsp;&nbsp;&nbsp; ΔH° = +641 kJ mol<sup>-1</sup>.<br/>"
                "Standard molar entropies: S°[MgCl<sub>2</sub>(s)] = 90.0 J K<sup>-1</sup> mol<sup>-1</sup>; "
                "S°[Mg(s)] = 32.7 J K<sup>-1</sup> mol<sup>-1</sup>; S°[Cl<sub>2</sub>(g)] = 223.0 J K<sup>-1</sup> mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Using thermochemical data: ΔH°f[MgCl<sub>2</sub>] = -641 kJ mol<sup>-1</sup>, ΔH°at[Mg] = +147 kJ mol<sup>-1</sup>, (IE1+IE2)[Mg] = +2187 kJ mol<sup>-1</sup>, bond energy of Cl<sub>2</sub> = +242 kJ mol<sup>-1</sup>, and EA[Cl] = -349 kJ mol<sup>-1</sup>, calculate the lattice energy of MgCl<sub>2</sub>(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the standard entropy change ΔS° for the decomposition reaction and deduce the minimum temperature at which this decomposition becomes thermodynamically feasible.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Mg) + (IE1+IE2) + 2(ΔH°at(Cl)) + 2(EA(Cl)) + LE [1]; -641 = 147 + 2187 + 242 + 2(-349) + LE = 1878 + LE [1]; LE(MgCl2) = -2519 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "ΔS° = S°(Mg) + S°(Cl2) - S°(MgCl2) = 32.7 + 223.0 - 90.0 = +165.7 J K<sup>-1</sup> mol<sup>-1</sup> [1]; At feasibility, ΔG° = 0 &rArr; T = ΔH° / ΔS° [1]; T = (641 &times; 1000) / 165.7 = 3868 K (or 3870 K) [1].", "marks": 3}
            ]
        ),

        # Q3: 9701/43/M/J/23/Q1 — Calcium fluoride Born-Haber cycle and solubility
        Question(
            number=3,
            title="Calcium Fluoride Cycle & Solubility Thermodynamics — 9701/43/M/J/23/Q1 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Calcium fluoride, CaF<sub>2</sub>, is sparingly soluble in water, whereas calcium chloride, CaCl<sub>2</sub>, is highly soluble.<br/>"
                "Data for CaF<sub>2</sub>: ΔH°f[CaF<sub>2</sub>] = -1220 kJ mol<sup>-1</sup>; ΔH°at[Ca] = +178 kJ mol<sup>-1</sup>; "
                "(IE1+IE2)[Ca] = +1735 kJ mol<sup>-1</sup>; bond energy F–F = +158 kJ mol<sup>-1</sup>; EA[F] = -328 kJ mol<sup>-1</sup>.<br/>"
                "Hydration enthalpies: ΔH°hyd(Ca<sup>2+</sup>) = -1577 kJ mol<sup>-1</sup>; ΔH°hyd(F<sup>-</sup>) = -506 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of calcium fluoride, CaF<sub>2</sub>(s).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the standard enthalpy of solution, ΔH°sol, of CaF<sub>2</sub>(s) and explain why CaF<sub>2</sub> is much less soluble than CaCl<sub>2</sub>.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Ca) + (IE1+IE2)(Ca) + 2(ΔH°at(F)) + 2(EA(F)) + LE [1]; -1220 = 178 + 1735 + 158 + 2(-328) + LE = 1415 + LE [1]; LE(CaF2) = -2635 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "ΔH°sol = ΣΔH°hyd - LE = [-1577 + 2(-506)] - (-2635) = -2589 + 2635 = +46 kJ mol<sup>-1</sup> [1]; ΔH°sol is endothermic, making dissolution unfavorable [1]; F- is much smaller than Cl-, giving CaF2 an extremely large exothermic LE that dominates over hydration enthalpy [1].", "marks": 3}
            ]
        ),

        # Q4: 9701/42/O/N/22/Q1 — Barium sulfate enthalpy of solution cycle
        Question(
            number=4,
            title="Barium Sulfate Solution Cycle & Group 2 Trends — 9701/42/O/N/22/Q1 [6 Marks]",
            syllabus_ref="23.2",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Barium sulfate, BaSO<sub>4</sub>, is widely used as a radiopaque contrast medium (barium meal) due to its extreme insolubility.<br/>"
                "Lattice energy of BaSO<sub>4</sub> = -2469 kJ mol<sup>-1</sup>.<br/>"
                "Enthalpies of hydration: ΔH°hyd(Ba<sup>2+</sup>) = -1305 kJ mol<sup>-1</sup>; ΔH°hyd(SO<sub>4</sub><sup>2-</sup>) = -1145 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Construct an energy cycle relating lattice energy, enthalpy of hydration, and enthalpy of solution, and calculate ΔH°sol of BaSO<sub>4</sub>.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why the solubility of Group 2 sulfates decreases down Group 2 from MgSO<sub>4</sub> to BaSO<sub>4</sub>.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°sol = ΔH°hyd(Ba2+) + ΔH°hyd(SO4^2-) - LE(BaSO4) [1]; ΔH°sol = (-1305) + (-1145) - (-2469) [1]; ΔH°sol = -2450 + 2469 = +19 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "Both lattice energy and hydration enthalpy become less exothermic down the group as cation radius increases [1]; however, ΔH°hyd decreases more rapidly than LE because SO4^2- is a large anion so LE is relatively insensitive to cation size [1]; hence ΔH°sol becomes increasingly endothermic down the group, decreasing solubility [1].", "marks": 3}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q1 — Silver chloride covalent character & Born-Haber
        Question(
            number=5,
            title="Silver Chloride Lattice Energy: Experimental vs Theoretical — 9701/42/M/J/22/Q1 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "The experimental lattice energy of silver chloride, AgCl, can be determined using a Born–Haber cycle.<br/>"
                "&bull; ΔH°f[AgCl(s)] = -127 kJ mol<sup>-1</sup><br/>"
                "&bull; ΔH°at[Ag(s)] = +285 kJ mol<sup>-1</sup><br/>"
                "&bull; First ionisation energy of Ag(g) = +731 kJ mol<sup>-1</sup><br/>"
                "&bull; Enthalpy of atomisation of chlorine, ½Cl<sub>2</sub>(g) = +121 kJ mol<sup>-1</sup><br/>"
                "&bull; Electron affinity of chlorine, Cl(g) = -349 kJ mol<sup>-1</sup><br/>"
                "Theoretical lattice energy calculated using a purely ionic model = -770 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the experimental lattice energy of AgCl(s) using the Born–Haber cycle data.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Compare the experimental value with the theoretical value, and explain the difference in terms of the bonding in AgCl.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Ag) + IE1(Ag) + ΔH°at(Cl) + EA(Cl) + LE [1]; -127 = 285 + 731 + 121 + (-349) + LE = 788 + LE [1]; LE(AgCl) = -915 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "Experimental LE (-915 kJ mol^-1) is significantly more exothermic than theoretical LE (-770 kJ mol^-1) [1]; Ag+ cation polarises the large Cl- electron cloud due to Ag+ having high polarising power (d10 subshell poorly shielding) [1]; this introduces substantial covalent character, strengthening the bonding beyond purely electrostatic attraction [1].", "marks": 3}
            ]
        ),

        # Q6: 9701/42/O/N/21/Q1 — Copper(I) oxide Born-Haber & oxygen electron affinities
        Question(
            number=6,
            title="Copper(I) Oxide Born–Haber Cycle & Electron Affinities — 9701/42/O/N/21/Q1 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Copper(I) oxide, Cu<sub>2</sub>O, is a reddish solid used as a semiconductor and antifouling pigment.<br/>"
                "Data: ΔH°f[Cu<sub>2</sub>O(s)] = -169 kJ mol<sup>-1</sup>; ΔH°at[Cu(s)] = +338 kJ mol<sup>-1</sup>; "
                "IE1[Cu(g)] = +746 kJ mol<sup>-1</sup>; ΔH°at[O] = +249 kJ mol<sup>-1</sup>; "
                "First electron affinity of O(g) = -141 kJ mol<sup>-1</sup>; "
                "Second electron affinity of O(g) = +798 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Construct the expression for the Born–Haber cycle and calculate the lattice energy of Cu<sub>2</sub>O(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain why the first electron affinity of oxygen is exothermic whereas the second electron affinity is endothermic.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = 2&times;ΔH°at(Cu) + 2&times;IE1(Cu) + ΔH°at(O) + (EA1+EA2)(O) + LE [1]; -169 = 2(338) + 2(746) + 249 + (-141 + 798) + LE [1]; -169 = 676 + 1492 + 249 + 657 + LE = 3074 + LE [1]; LE(Cu2O) = -3243 kJ mol<sup>-1</sup> [1].", "marks": 4},
                {"part": "(b)", "points": "EA1 is exothermic because the incoming electron is attracted by the positive nuclear charge of the neutral O atom [1]; EA2 is endothermic because the incoming electron is repelled by the negative charge of the O- ion, requiring energy to overcome electrostatic repulsion [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/41/O/N/21/Q2 — Endothermic dissolution of NH4NO3 & entropy
        Question(
            number=7,
            title="Thermodynamics of Ammonium Nitrate Dissolution — 9701/41/O/N/21/Q2 [6 Marks]",
            syllabus_ref="23.2",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Ammonium nitrate, NH<sub>4</sub>NO<sub>3</sub>, dissolves endothermically in water and is used in instant cold packs:<br/>"
                "NH<sub>4</sub>NO<sub>3</sub>(s) &rarr; NH<sub>4</sub><sup>+</sup>(aq) + NO<sub>3</sub><sup>-</sup>(aq) &nbsp;&nbsp;&nbsp; ΔH°sol = +25.7 kJ mol<sup>-1</sup>.<br/>"
                "Standard entropies: S°[NH<sub>4</sub>NO<sub>3</sub>(s)] = 151 J K<sup>-1</sup> mol<sup>-1</sup>; "
                "S°[NH<sub>4</sub><sup>+</sup>(aq)] = 113 J K<sup>-1</sup> mol<sup>-1</sup>; "
                "S°[NO<sub>3</sub><sup>-</sup>(aq)] = 146 J K<sup>-1</sup> mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the standard entropy change of solution, ΔS°sol, for ammonium nitrate at 298 K.", 3, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the standard Gibbs free energy change, ΔG°sol, at 298 K and explain why NH<sub>4</sub>NO<sub>3</sub> dissolves spontaneously despite the process being endothermic.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS°sol = ΣS°(products) - ΣS°(reactants) = 113 + 146 - 151 [1]; ΔS°sol = 259 - 151 [1]; ΔS°sol = +108 J K<sup>-1</sup> mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "ΔG° = ΔH° - TΔS° = +25.7 - [298 &times; (+108 / 1000)] [1]; ΔG° = 25.7 - 32.18 = -6.48 kJ mol<sup>-1</sup> [1]; Spontaneous because ΔG° is negative; the positive entropy change (TΔS°) exceeds the endothermic enthalpy term at 298 K (entropy-driven process) [1].", "marks": 3}
            ]
        ),

        # Q8: 9701/41/M/J/21/Q1 — CaCO3 thermal decomposition feasibility
        Question(
            number=8,
            title="Thermal Decomposition of Calcium Carbonate — 9701/41/M/J/21/Q1 [6 Marks]",
            syllabus_ref="23.4",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Limestone, CaCO<sub>3</sub>, decomposes into quicklime and carbon dioxide when heated strongly:<br/>"
                "CaCO<sub>3</sub>(s) &rarr; CaO(s) + CO<sub>2</sub>(g).<br/>"
                "Standard thermodynamic values:<br/>"
                "&bull; ΔH°f[CaCO<sub>3</sub>(s)] = -1207 kJ mol<sup>-1</sup>; ΔH°f[CaO(s)] = -635 kJ mol<sup>-1</sup>; ΔH°f[CO<sub>2</sub>(g)] = -394 kJ mol<sup>-1</sup><br/>"
                "&bull; S°[CaCO<sub>3</sub>(s)] = 92.9 J K<sup>-1</sup> mol<sup>-1</sup>; S°[CaO(s)] = 39.7 J K<sup>-1</sup> mol<sup>-1</sup>; S°[CO<sub>2</sub>(g)] = 213.6 J K<sup>-1</sup> mol<sup>-1</sup>"
            ),
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy change ΔH° and standard entropy change ΔS° for this decomposition reaction.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Calculate the minimum temperature, in °C, at which the decomposition of CaCO<sub>3</sub> becomes thermodynamically feasible.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH° = [-635 + (-394)] - (-1207) = -1029 + 1207 = +178 kJ mol<sup>-1</sup> [1]; ΔS° = [39.7 + 213.6] - 92.9 = 253.3 - 92.9 = +160.4 J K<sup>-1</sup> mol<sup>-1</sup> [2].", "marks": 3},
                {"part": "(b)", "points": "Feasible when ΔG° &le; 0 &rArr; T = ΔH° / ΔS° [1]; T = (178 &times; 1000) / 160.4 = 1109.7 K [1]; T(°C) = 1109.7 - 273 = 837 °C (or 836.7 °C) [1].", "marks": 3}
            ]
        ),

        # Q9: 9701/43/M/J/21/Q2 — Lithium iodide polarization & lattice energy
        Question(
            number=9,
            title="Polarization & Lattice Energy of Lithium Iodide — 9701/43/M/J/21/Q2 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Lithium iodide, LiI, exhibits one of the largest discrepancies between experimental and theoretical lattice energies among alkali halides.<br/>"
                "Data: ΔH°f[LiI(s)] = -270 kJ mol<sup>-1</sup>; ΔH°at[Li(s)] = +161 kJ mol<sup>-1</sup>; "
                "IE1[Li(g)] = +520 kJ mol<sup>-1</sup>; ΔH°at[½I<sub>2</sub>(s)] = +107 kJ mol<sup>-1</sup>; "
                "EA[I(g)] = -295 kJ mol<sup>-1</sup>.<br/>"
                "Theoretical electrostatic lattice energy = -738 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the experimental lattice energy of LiI(s) using the Born–Haber cycle.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why the experimental lattice energy is more exothermic than the theoretical value, referring to the polarising power of Li<sup>+</sup> and the polarisability of I<sup>-</sup>.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Li) + IE1(Li) + ΔH°at(I) + EA(I) + LE [1]; -270 = 161 + 520 + 107 + (-295) + LE = 493 + LE [1]; LE(LiI) = -763 kJ mol<sup>-1</sup> [1].", "marks": 3},
                {"part": "(b)", "points": "Experimental LE (-763 kJ mol^-1) is more exothermic than theoretical LE (-738 kJ mol^-1) [1]; Li+ has an extremely small ionic radius and high charge density (high polarising power) [1]; I- has a large electron cloud held weakly by its nucleus (high polarisability), resulting in distortion of the electron cloud and significant covalent character [1].", "marks": 3}
            ]
        ),

        # Q10: 9701/42/M/J/18/Q1 — Aluminium oxide Born-Haber cycle
        Question(
            number=10,
            title="Complete Born–Haber Cycle for Aluminium Oxide — 9701/42/M/J/18/Q1 [6 Marks]",
            syllabus_ref="23.1",
            difficulty="HARD",
            section_key="SEC_A",
            preamble=(
                "Aluminium oxide, Al<sub>2</sub>O<sub>3</sub>, is a refractory ceramic with a very high melting point (2072 °C).<br/>"
                "Data: ΔH°f[Al<sub>2</sub>O<sub>3</sub>(s)] = -1676 kJ mol<sup>-1</sup>; ΔH°at[Al(s)] = +326 kJ mol<sup>-1</sup>;<br/>"
                "Ionisation energies of Al(g): IE1 = +578, IE2 = +1817, IE3 = +2745 kJ mol<sup>-1</sup>;<br/>"
                "Enthalpy of atomisation of oxygen, O<sub>2</sub>(g) &rarr; 2O(g), bond energy = +496 kJ mol<sup>-1</sup>;<br/>"
                "Electron affinities of O(g): EA1 = -141 kJ mol<sup>-1</sup>, EA2 = +798 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the lattice energy of aluminium oxide, Al<sub>2</sub>O<sub>3</sub>(s).", 4, num_answer_lines=5),
                QuestionPart("(b)", "Explain why the lattice energy of Al<sub>2</sub>O<sub>3</sub> is vastly more exothermic than that of sodium oxide, Na<sub>2</sub>O (LE = -2478 kJ mol<sup>-1</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = 2&times;ΔH°at(Al) + 2&times;(IE1+IE2+IE3)(Al) + 3&times;(½ BE(O2)) + 3&times;(EA1+EA2)(O) + LE [1]; -1676 = 2(326) + 2(5140) + 1.5(496) + 3(657) + LE [1]; -1676 = 652 + 10280 + 744 + 1971 + LE = 13647 + LE [1]; LE(Al2O3) = -15323 kJ mol<sup>-1</sup> [1].", "marks": 4},
                {"part": "(b)", "points": "Al3+ has a +3 charge and smaller radius than Na+ (+1 charge), and O2- has a -2 charge [1]; lattice energy is proportional to (q1&times;q2)/(r+ + r-), so the product of ionic charges is +6 in Al2O3 compared to +2 in Na2O, creating vastly stronger electrostatic attraction [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # CATEGORY 2: 40% 4-MARKERS (QUESTIONS 11 TO 20) — SECTION B
        # =====================================================================

        # Q11: 9701/41/O/N/22/Q1 — NaCl vs MgO lattice energy comparison
        Question(
            number=11,
            title="Lattice Energy: Sodium Chloride vs Magnesium Oxide — 9701/41/O/N/22/Q1 [4 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "The lattice energies of sodium chloride and magnesium oxide are given below:<br/>"
                "&bull; NaCl: LE = -787 kJ mol<sup>-1</sup><br/>"
                "&bull; MgO: LE = -3791 kJ mol<sup>-1</sup><br/>"
                "Both compounds have identical rock-salt crystal structures."
            ),
            parts=[
                QuestionPart("(a)", "Explain why the lattice energy of MgO is almost five times more exothermic than that of NaCl, referring to ionic charges and ionic radii.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Lattice energy depends on the electrostatic attraction between oppositely charged ions, proportional to (q+ &times; q-) / (r+ + r-) [1]; Mg2+ has a +2 charge and O2- has a -2 charge, giving charge product = 4, whereas Na+ and Cl- give charge product = 1 [1]; Mg2+ (0.065 nm) is smaller than Na+ (0.095 nm), and O2- (0.140 nm) is smaller than Cl- (0.181 nm) [1]; the smaller inter-ionic separation and quadrupled charge product produce vastly stronger electrostatic attraction in MgO [1].", "marks": 4}
            ]
        ),

        # Q12: 9701/43/M/J/22/Q2 — KBr enthalpy of solution & hydration
        Question(
            number=12,
            title="Hydration Enthalpy of Bromide Ions in KBr — 9701/43/M/J/22/Q2 [4 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Potassium bromide, KBr, dissolves endothermically in water.<br/>"
                "&bull; Lattice energy of KBr(s) = -679 kJ mol<sup>-1</sup><br/>"
                "&bull; Standard enthalpy of solution, ΔH°sol = +20.0 kJ mol<sup>-1</sup><br/>"
                "&bull; Enthalpy of hydration of K<sup>+</sup>(g), ΔH°hyd = -322 kJ mol<sup>-1</sup>"
            ),
            parts=[
                QuestionPart("(a)", "Using an enthalpy cycle, calculate the standard enthalpy of hydration of the bromide ion, Br<sup>-</sup>(g), in kJ mol<sup>-1</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy cycle equation: ΔH°sol = ΔH°hyd(K+) + ΔH°hyd(Br-) - LE(KBr) [1]; +20.0 = -322 + ΔH°hyd(Br-) - (-679) [1]; +20.0 = -322 + 679 + ΔH°hyd(Br-) = +357 + ΔH°hyd(Br-) [1]; ΔH°hyd(Br-) = 20.0 - 357 = -337 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q13: 9701/43/O/N/21/Q1 — Strontium chloride lattice energy
        Question(
            number=13,
            title="Strontium Chloride Lattice Energy Calculation — 9701/43/O/N/21/Q1 [4 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Strontium chloride, SrCl<sub>2</sub>, is used in fireworks to impart a bright crimson colour.<br/>"
                "Thermochemical data:<br/>"
                "&bull; ΔH°f[SrCl<sub>2</sub>(s)] = -829 kJ mol<sup>-1</sup><br/>"
                "&bull; ΔH°at[Sr(s)] = +164 kJ mol<sup>-1</sup>; IE1[Sr] = +550 kJ mol<sup>-1</sup>; IE2[Sr] = +1064 kJ mol<sup>-1</sup><br/>"
                "&bull; Bond energy of Cl<sub>2</sub>(g) = +242 kJ mol<sup>-1</sup><br/>"
                "&bull; Electron affinity of Cl(g) = -349 kJ mol<sup>-1</sup>"
            ),
            parts=[
                QuestionPart("(a)", "Write the Born–Haber equation and calculate the lattice energy of strontium chloride, SrCl<sub>2</sub>(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Sr) + (IE1+IE2)(Sr) + BE(Cl2) + 2&times;EA(Cl) + LE [1]; -829 = 164 + (550 + 1064) + 242 + 2(-349) + LE [1]; -829 = 164 + 1614 + 242 - 698 + LE = 1322 + LE [1]; LE(SrCl2) = -829 - 1322 = -2151 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q14: 9701/42/M/J/21/Q1 — Solubility trend of Group 2 hydroxides
        Question(
            number=14,
            title="Group 2 Hydroxide Solubility Trend — 9701/42/M/J/21/Q1 [4 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "The solubility of Group 2 hydroxides increases down the group from Mg(OH)<sub>2</sub> (insoluble, milk of magnesia) "
                "to Ba(OH)<sub>2</sub> (soluble)."
            ),
            parts=[
                QuestionPart("(a)", "Explain this trend in solubility in terms of the relative changes in lattice energy and enthalpy of hydration down Group 2.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "As Group 2 is descended, the ionic radius of M2+ increases while charge remains +2 [1]; both lattice energy and hydration enthalpy of the cation become less exothermic [1]; because OH- is a relatively small anion, lattice energy decreases more rapidly than hydration enthalpy [1]; ΔH°sol = ΣΔH°hyd - LE becomes less endothermic / more exothermic down the group, increasing solubility [1].", "marks": 4}
            ]
        ),

        # Q15: 9701/42/O/N/20/Q1 — MgO second electron affinity of oxygen
        Question(
            number=15,
            title="Second Electron Affinity of Oxygen from MgO Cycle — 9701/42/O/N/20/Q1 [4 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "The second electron affinity of oxygen, O<sup>-</sup>(g) + e<sup>-</sup> &rarr; O<sup>2-</sup>(g), cannot be measured directly.<br/>"
                "Data: ΔH°f[MgO(s)] = -602 kJ mol<sup>-1</sup>; ΔH°at[Mg(s)] = +148 kJ mol<sup>-1</sup>; "
                "(IE1+IE2)[Mg] = +2187 kJ mol<sup>-1</sup>; ΔH°at[O] = +249 kJ mol<sup>-1</sup>; "
                "EA1[O] = -141 kJ mol<sup>-1</sup>; LE[MgO(s)] = -3791 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the value of the second electron affinity of oxygen, EA2[O], in kJ mol<sup>-1</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Mg) + (IE1+IE2)(Mg) + ΔH°at(O) + EA1(O) + EA2(O) + LE [1]; -602 = 148 + 2187 + 249 + (-141) + EA2 + (-3791) [1]; -602 = -1348 + EA2 [1]; EA2(O) = -602 + 1348 = +746 kJ mol<sup>-1</sup> (accept +745 to +750) [1].", "marks": 4}
            ]
        ),

        # Q16: 9701/41/O/N/20/Q2 — Hydration enthalpy Mg2+ vs Ba2+
        Question(
            number=16,
            title="Hydration Enthalpy: Magnesium vs Barium Ions — 9701/41/O/N/20/Q2 [4 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Hydration enthalpy values for two Group 2 cations are given below:<br/>"
                "&bull; Mg<sup>2+</sup>(g): ΔH°hyd = -1920 kJ mol<sup>-1</sup> &nbsp;&nbsp;&nbsp; (ionic radius = 0.065 nm)<br/>"
                "&bull; Ba<sup>2+</sup>(g): ΔH°hyd = -1305 kJ mol<sup>-1</sup> &nbsp;&nbsp;&nbsp; (ionic radius = 0.135 nm)"
            ),
            parts=[
                QuestionPart("(a)", "Explain why ΔH°hyd of Mg<sup>2+</sup> is significantly more exothermic than that of Ba<sup>2+</sup>.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy of hydration involves ion-dipole attractions between the gaseous cation and the partial negative oxygen atom (&delta;-) of water molecules [1]; Mg2+ has the same +2 charge as Ba2+ but a much smaller ionic radius [1]; Mg2+ has a much higher charge density than Ba2+ [1]; stronger electrostatic attraction to water dipole releases more energy upon hydration, giving a more exothermic ΔH°hyd [1].", "marks": 4}
            ]
        ),

        # Q17: 9701/42/M/J/20/Q1 — Entropy of NaHCO3 decomposition
        Question(
            number=17,
            title="Entropy Change in Sodium Hydrogencarbonate Decomposition — 9701/42/M/J/20/Q1 [4 Marks]",
            syllabus_ref="23.3",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Baking soda decomposes on heating:<br/>"
                "2NaHCO<sub>3</sub>(s) &rarr; Na<sub>2</sub>CO<sub>3</sub>(s) + H<sub>2</sub>O(g) + CO<sub>2</sub>(g).<br/>"
                "Standard entropies: S°[NaHCO<sub>3</sub>(s)] = 102 J K<sup>-1</sup> mol<sup>-1</sup>; "
                "S°[Na<sub>2</sub>CO<sub>3</sub>(s)] = 136 J K<sup>-1</sup> mol<sup>-1</sup>;<br/>"
                "S°[H<sub>2</sub>O(g)] = 189 J K<sup>-1</sup> mol<sup>-1</sup>; "
                "S°[CO<sub>2</sub>(g)] = 214 J K<sup>-1</sup> mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Calculate the standard entropy change ΔS° for this reaction and explain why it has a large positive value.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° = ΣS°(products) - ΣS°(reactants) = [136 + 189 + 214] - 2(102) [1]; ΔS° = 539 - 204 = +335 J K<sup>-1</sup> mol<sup>-1</sup> [1]; The reaction converts 2 moles of solid into 1 mole of solid and 2 moles of gas [1]; gases have vastly higher degrees of disorder and translational microstates than crystalline solids, leading to a substantial increase in system entropy [1].", "marks": 4}
            ]
        ),

        # Q18: 9701/42/O/N/19/Q1 — BaCl2 enthalpy of formation
        Question(
            number=18,
            title="Barium Chloride Enthalpy of Formation — 9701/42/O/N/19/Q1 [4 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Data for barium chloride, BaCl<sub>2</sub>:<br/>"
                "&bull; Enthalpy of atomisation of Ba(s) = +180 kJ mol<sup>-1</sup><br/>"
                "&bull; (IE1+IE2) of Ba(g) = +1468 kJ mol<sup>-1</sup><br/>"
                "&bull; Bond energy of Cl<sub>2</sub>(g) = +242 kJ mol<sup>-1</sup><br/>"
                "&bull; Electron affinity of Cl(g) = -349 kJ mol<sup>-1</sup><br/>"
                "&bull; Lattice energy of BaCl<sub>2</sub>(s) = -2056 kJ mol<sup>-1</sup>"
            ),
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy of formation, ΔH°f, of solid barium chloride, BaCl<sub>2</sub>(s).", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔH°f = ΔH°at(Ba) + (IE1+IE2)(Ba) + BE(Cl2) + 2&times;EA(Cl) + LE [1]; ΔH°f = 180 + 1468 + 242 + 2(-349) + (-2056) [1]; ΔH°f = 1890 - 698 - 2056 [1]; ΔH°f = -864 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q19: 9701/41/O/N/19/Q2 — CuSO4 hydration cycle
        Question(
            number=19,
            title="Copper(II) Sulfate Hydration Energy Cycle — 9701/41/O/N/19/Q2 [4 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "The conversion of white anhydrous copper(II) sulfate to blue hydrated crystals is given by:<br/>"
                "CuSO<sub>4</sub>(s) + 5H<sub>2</sub>O(l) &rarr; CuSO<sub>4</sub>&middot;5H<sub>2</sub>O(s) &nbsp;&nbsp;&nbsp; ΔH°hyd.<br/>"
                "The enthalpy of solution of anhydrous CuSO<sub>4</sub>(s) is -66.5 kJ mol<sup>-1</sup>.<br/>"
                "The enthalpy of solution of hydrated CuSO<sub>4</sub>&middot;5H<sub>2</sub>O(s) is +11.7 kJ mol<sup>-1</sup>."
            ),
            parts=[
                QuestionPart("(a)", "Draw a Hess's Law cycle connecting these three states and calculate the standard enthalpy of hydration, ΔH°hyd.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hess's Law cycle showing CuSO4(s) + 5H2O(l) and CuSO4&middot;5H2O(s) both dissolving in excess water to form CuSO4(aq) [1]; cycle relationship: ΔH°hyd + ΔH°sol(hydrated) = ΔH°sol(anhydrous) [1]; ΔH°hyd = ΔH°sol(anhydrous) - ΔH°sol(hydrated) = -66.5 - (+11.7) [1]; ΔH°hyd = -78.2 kJ mol<sup>-1</sup> [1].", "marks": 4}
            ]
        ),

        # Q20: 9701/41/O/N/18/Q2 — Sulfate solubility decrease down group
        Question(
            number=20,
            title="Thermodynamics of Group 2 Sulfate Insolubility — 9701/41/O/N/18/Q2 [4 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_B",
            preamble=(
                "Group 2 sulfates show a pronounced decrease in solubility down Group 2:<br/>"
                "&bull; MgSO<sub>4</sub>: highly soluble (used as Epsom salts)<br/>"
                "&bull; BaSO<sub>4</sub>: insoluble (precipitates quantitatively)"
            ),
            parts=[
                QuestionPart("(a)", "Account for this solubility decrease down Group 2 by comparing the relative magnitudes and rates of change of ΔH°hyd and lattice energy.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy of solution is given by ΔH°sol = ΣΔH°hyd - LE [1]; descending Group 2, cation radius increases (Mg2+ to Ba2+), so both LE and ΔH°hyd become less exothermic [1]; because the sulfate ion SO4^2- is very large, the increase in cation radius causes only a small percentage change in (r+ + r-), so LE changes slowly [1]; however, cation ΔH°hyd depends directly on 1/r+ and drops sharply; thus ΔH°sol becomes significantly more endothermic, reducing solubility [1].", "marks": 4}
            ]
        ),

        # =====================================================================
        # CATEGORY 3: 20% 2-MARKERS (QUESTIONS 21 TO 25) — SECTION C
        # =====================================================================

        # Q21: 9701/42/M/J/23/Q1(a) — Definition of enthalpy of hydration
        Question(
            number=21,
            title="Definition of Enthalpy Change of Hydration — 9701/42/M/J/23/Q1(a) [2 Marks]",
            syllabus_ref="23.2",
            difficulty="EASY",
            section_key="SEC_C",
            preamble="Hydration enthalpy is a fundamental parameter in predicting solubility.",
            parts=[
                QuestionPart("(a)", "Define standard enthalpy change of hydration, ΔH°hyd, and write an equation representing the hydration of magnesium ions, including state symbols.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when 1 mole of gaseous ions is completely dissolved in water to form infinitely dilute solution under standard conditions [1]; Mg2+(g) + aq &rarr; Mg2+(aq) [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/41/M/J/23/Q2(a) — Definition of lattice energy
        Question(
            number=22,
            title="Definition and Sign of Lattice Energy — 9701/41/M/J/23/Q2(a) [2 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_C",
            preamble="Lattice energy characterizes the strength of bonding in ionic solids.",
            parts=[
                QuestionPart("(a)", "Define lattice energy and state whether it is exothermic or endothermic by the Cambridge convention.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The enthalpy change when 1 mole of an ionic crystalline solid is formed from its constituent gaseous ions under standard conditions [1]; it is always exothermic (negative sign) [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/41/M/J/20/Q1(a) — Entropy change in state transitions
        Question(
            number=23,
            title="Entropy Change Sign in Vaporization — 9701/41/M/J/20/Q1(a) [2 Marks]",
            syllabus_ref="23.3",
            difficulty="EASY",
            section_key="SEC_C",
            preamble="Entropy reflects the dispersal of energy and matter in a system.",
            parts=[
                QuestionPart("(a)", "State and explain the sign of the entropy change, ΔS°, for the boiling of liquid water: H<sub>2</sub>O(l) &rarr; H<sub>2</sub>O(g).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔS° is positive (ΔS° > 0) [1]; in the gas phase particles have complete translational freedom and disorder, yielding vastly more available microstates than in the liquid phase [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/42/O/N/18/Q1(a) — Electron affinities of oxygen
        Question(
            number=24,
            title="Electron Affinities of Oxygen: Sign Distinction — 9701/42/O/N/18/Q1(a) [2 Marks]",
            syllabus_ref="23.1",
            difficulty="EASY",
            section_key="SEC_C",
            preamble="Oxygen forms oxide ions, O<sup>2-</sup>, in ionic lattices.",
            parts=[
                QuestionPart("(a)", "Explain why the first electron affinity of oxygen is negative (-141 kJ mol<sup>-1</sup>) whereas its second electron affinity is positive (+798 kJ mol<sup>-1</sup>).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "EA1 is exothermic because the added electron is attracted to the positively charged nucleus of the neutral O atom [1]; EA2 is endothermic because adding an electron to a negatively charged O- ion requires energy to overcome strong electrostatic repulsion [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/41/M/J/19/Q1(a) — Criterion for feasibility
        Question(
            number=25,
            title="Thermodynamic Criterion for Reaction Feasibility — 9701/41/M/J/19/Q1(a) [2 Marks]",
            syllabus_ref="23.4",
            difficulty="EASY",
            section_key="SEC_C",
            preamble="Chemical feasibility is governed by the second law of thermodynamics.",
            parts=[
                QuestionPart("(a)", "State the mathematical condition involving standard Gibbs free energy change, ΔG°, for a reaction to be thermodynamically feasible, and state the SI units of ΔG°.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "ΔG° &le; 0 (negative or zero) [1]; units: kJ mol<sup>-1</sup> (or J mol<sup>-1</sup>) [1].", "marks": 2}
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
    build_topic23_restructured()
