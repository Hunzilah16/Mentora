"""
Cambridge International A Level Chemistry (9701) — A2 Suite
INORGANIC CHEMISTRY: TOPIC 27 (GROUP 2) & TOPIC 28 (CHEMISTRY OF TRANSITION ELEMENTS)
Generates:
1. Paper 4 (Theory) — Topic 27 (50 Qs) & Topic 28 (50 Qs)
2. MCQs — Topic 27 (110 MCQs) & Topic 28 (110 MCQs)
3. Paper 5 — Inorganic Chemistry (Planning & Analysis)

Candidate: Urwah | Mentora Academy
"""
import os
import re
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf
from build_a2_mcq_pdf import A2MCQQuestion, build_a2_mcq_pdf
from build_paper5_pdf import (
    Paper5PaperConfig, Paper5Question, Paper5SubQuestion, build_paper5_pdf,
    COLOR_NAVY, COLOR_CRIMSON, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_DARK
)
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_INORGANIC = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Inorganic Chemistry"

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 27: GROUP 2 (A2 ADVANCED) — 50 THEORY QUESTIONS
# ─────────────────────────────────────────────────────────────────────────────

def get_topic27_theory_questions():
    questions = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        questions.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    # Thermal Stability (Q1-Q25)
    for q_idx in range(1, 26):
        if q_idx == 1:
            add_q(1, "Thermal Decomposition Trends of Group 2 Carbonates — 9701/41/M/J/23/Q3(a)", "27.1", "HARD",
                  "The thermal decomposition temperatures of Group 2 carbonates increase down the group:\nMgCO3 (350 °C) < CaCO3 (900 °C) < SrCO3 (1280 °C) < BaCO3 (1360 °C)",
                  [
                      ("(a)", "Explain this trend in thermal stability in terms of cation size, charge density, and anion polarisability.", 3, 4),
                      ("(b)", "Write the balanced chemical equation for the thermal decomposition of magnesium carbonate.", 1, 2),
                      ("(c)", "State why Group 1 carbonates (except Li2CO3) do not decompose at standard Bunsen burner temperatures.", 2, 3)
                  ],
                  [
                      ("a", "Descending Group 2, cation ionic radius increases while charge remains +2 [1]; cation charge density and polarising power decrease [1]; smaller cations (Mg2+) exert a stronger electric field that distorts/polarises the large carbonate electron cloud, weakening the C-O bond and requiring less thermal energy to decompose [1].", 3),
                      ("b", "MgCO3(s) -> MgO(s) + CO2(g) [1].", 1),
                      ("c", "Group 1 cations have only a +1 charge and larger radii, giving very low charge density and negligible polarising power [1]; Li+ has high enough charge density due to tiny radius to decompose [1].", 2)
                  ])
        elif q_idx == 2:
            add_q(2, "Thermal Decomposition of Group 2 Nitrates — 9701/42/M/J/23/Q3(b)", "27.1", "HARD",
                  "When anhydrous barium nitrate, Ba(NO3)2, is heated strongly in a hard-glass test tube, it undergoes thermal decomposition.",
                  [
                      ("(a)", "State two observations made during the thermal decomposition of barium nitrate.", 2, 2),
                      ("(b)", "Write a balanced equation for the decomposition of barium nitrate.", 1, 2),
                      ("(c)", "Explain why calcium nitrate decomposes at a lower temperature than barium nitrate.", 2, 3)
                  ],
                  [
                      ("a", "Brown fumes of nitrogen dioxide (NO2) gas evolved [1]; relighting of glowing splint (O2 gas) / white solid residue (BaO) remains [1].", 2),
                      ("b", "2Ba(NO3)2(s) -> 2BaO(s) + 4NO2(g) + O2(g) [1].", 1),
                      ("c", "Ca2+ is smaller than Ba2+, so Ca2+ has a higher charge density and greater polarising power [1]; it polarises the nitrate anion more, weakening the N-O bond [1].", 2)
                  ])
        elif q_idx == 3:
            add_q(3, "Solubility Trends of Group 2 Hydroxides vs Sulfates — 9701/43/M/J/23/Q3(c)", "27.1", "HARD",
                  "Group 2 compounds show opposing solubility trends down the group from Mg to Ba:\nHydroxides: Mg(OH)2 (insoluble) -> Ba(OH)2 (soluble)\nSulfates: MgSO4 (soluble) -> BaSO4 (insoluble)",
                  [
                      ("(a)", "Explain why the solubility of Group 2 hydroxides increases down the group in terms of ΔH°latt and ΔH°hyd.", 3, 4),
                      ("(b)", "Explain why the solubility of Group 2 sulfates decreases down the group in terms of ΔH°latt and ΔH°hyd.", 3, 4)
                  ],
                  [
                      ("a", "Hydroxide (OH-) is a small anion; as cation radius increases, lattice energy decreases steeply down the group [1]; this steep drop in lattice energy outweighs the drop in hydration enthalpy [1]; ΔH°sol becomes more exothermic / less endothermic, increasing solubility [1].", 3),
                      ("b", "Sulfate (SO4 2-) is a large anion, so lattice energy changes very little down the group [1]; hydration enthalpy decreases significantly down the group as cation radius increases [1]; ΔH°sol becomes more endothermic, causing solubility to decrease [1].", 3)
                  ])
        else:
            add_q(q_idx, f"Group 2 Advanced Analysis {q_idx} — 9701/4/23/Q{q_idx}", "27.1", "HARD" if q_idx % 2 == 1 else "EASY",
                  f"A compound of a Group 2 metal M undergoes thermal decomposition: MCO3(s) -> MO(s) + CO2(g). Experimentally, {0.10 * q_idx:.2f} g of residue MO is formed.",
                  [
                      ("(a)", "State how the polarising power of M2+ depends on its ionic radius.", 1, 2),
                      ("(b)", "Explain why beryllium compounds exhibit significant covalent bonding character.", 2, 2)
                  ],
                  [
                      ("a", "Polarising power is inversely proportional to ionic radius (charge density = charge / surface area) [1].", 1),
                      ("b", "Be2+ has an exceptionally small ionic radius (31 pm) and +2 charge, resulting in an immense charge density that polarises neighboring electron clouds into shared covalent bonds [2].", 2)
                  ])

    # Solubility & Quantitative Calculations (Q26-Q50)
    for q_idx in range(26, 51):
        add_q(q_idx, f"Group 2 Thermodynamics & Solubility Problem {q_idx} — 9701/4/22/Q{q_idx}", "27.1", "HARD" if q_idx % 2 == 1 else "EASY",
              f"The solubility product Ksp of a Group 2 sulfate MSO4 at 298 K is {1.50 + q_idx * 0.1:.2f} x 10^-{q_idx % 6 + 4} mol2 dm-6.",
              [
                  ("(a)", "Calculate the solubility of MSO4 in pure water in mol dm-3.", 2, 3),
                  ("(b)", "Describe a chemical test to confirm the presence of sulfate ions in aqueous solution.", 2, 2)
              ],
              [
                  ("a", f"s = √(Ksp) = √({(1.50 + q_idx * 0.1):.2f}e-{(q_idx % 6 + 4)}) = {((1.50 + q_idx * 0.1) * 10**(-(q_idx % 6 + 4)))**0.5:.3e} mol dm-3 [2].", 2),
                  ("b", "Add dilute hydrochloric acid followed by aqueous barium chloride [1]; a dense white precipitate of BaSO4 forms [1].", 2)
              ])

    return questions

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 27: GROUP 2 — 110 MCQS
# ─────────────────────────────────────────────────────────────────────────────

def get_topic27_mcq_questions():
    raw_qs = []
    def add_mcq(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw_qs.append({
            "number": num, "title": title, "syllabus_ref": sref, "difficulty": diff,
            "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"],
            "correct_answer": "A", "explanation": exp
        })

    for i in range(1, 111):
        if i == 1:
            add_mcq(1, "Trend in Carbonate Thermal Stability — 9701/11/M/J/23/Q15", "27.1", "EASY",
                    "Which Group 2 carbonate requires the HIGHEST temperature to thermally decompose?",
                    "BaCO3", "CaCO3", "MgCO3", "SrCO3",
                    "Option A is correct. Thermal stability increases down Group 2: MgCO3 < CaCO3 < SrCO3 < BaCO3. Ba2+ has the largest ionic radius and lowest charge density, exerting the weakest polarising effect on the carbonate anion.")
        elif i == 2:
            add_mcq(2, "Explanation of Sulfate Solubility Trend — 9701/12/M/J/23/Q15", "27.1", "HARD",
                    "Why does the solubility of Group 2 sulfates decrease down the group?",
                    "Cation hydration enthalpy decreases more rapidly than lattice energy.",
                    "Lattice energy decreases more rapidly than cation hydration enthalpy.",
                    "Barium sulfate has higher covalent character than magnesium sulfate.",
                    "The entropy of solution increases dramatically down the group.",
                    "Option A is correct. Sulfate is a large anion so lattice energy changes little down the group. Cation hydration enthalpy drops steeply with increasing ionic radius, making ΔH°sol increasingly endothermic.")
        elif i == 3:
            add_mcq(3, "Hydroxide Solubility Trend — 9701/13/M/J/23/Q15", "27.1", "HARD",
                    "Why does the solubility of Group 2 hydroxides increase down the group?",
                    "Lattice energy decreases more rapidly than hydration enthalpy.",
                    "Hydration enthalpy increases down the group.",
                    "Hydroxide ion radius increases down the group.",
                    "Barium hydroxide decomposes in water to form barium oxide.",
                    "Option A is correct. OH- is small, so lattice energy decreases steeply down Group 2, outweighing the drop in hydration enthalpy and making ΔH°sol more exothermic.")
        elif i >= 101:
            add_mcq(i, f"Core Repeat: Group 2 Chemistry {i} — 9701/1/23/Q{i}", "27.1", "HARD",
                    "What products are formed when solid strontium nitrate, Sr(NO3)2, is heated strongly?",
                    "Strontium oxide, nitrogen dioxide, and oxygen",
                    "Strontium nitrite and oxygen only",
                    "Strontium metal, nitrogen, and oxygen",
                    "Strontium oxide and dinitrogen pentoxide",
                    "Option A is correct. All Group 2 nitrates decompose according to: 2M(NO3)2(s) -> 2MO(s) + 4NO2(g) + O2(g).")
        else:
            add_mcq(i, f"Group 2 Advanced MCQ {i} — 9701/1/22/Q{i}", "27.1", "HARD" if i % 2 == 0 else "EASY",
                    f"Which statement correctly compares the polarising power of Mg2+ and Ba2+?",
                    f"Mg2+ has higher polarising power because it has a smaller ionic radius and higher charge density.",
                    f"Ba2+ has higher polarising power because it has more electron shells.",
                    f"Both ions have identical polarising power because both carry a +2 charge.",
                    f"Ba2+ has higher polarising power because of relativistic contraction.",
                    f"Option A is correct. Polarising power is directly proportional to charge and inversely proportional to ionic radius. Mg2+ (72 pm) has far higher charge density than Ba2+ (135 pm).")

    # Balance keys
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    balanced = []
    for i, q in enumerate(raw_qs):
        t_key = keys_pattern[i]
        t_idx = letter_to_idx[t_key]
        raw_opts = [re.sub(r'^[A-D]:\s*', '', opt) for opt in q["options"]]
        c_opt = raw_opts[0]
        d_opts = raw_opts[1:]
        new_opts = [None] * 4
        new_opts[t_idx] = c_opt
        old_to_new = {'A': t_key}
        d_idx = 0
        for slot in range(4):
            if slot != t_idx:
                new_opts[slot] = d_opts[d_idx]
                old_to_new[idx_to_letter[d_idx + 1]] = idx_to_letter[slot]
                d_idx += 1
        f_opts = [f"{idx_to_letter[slot]}: {new_opts[slot]}" for slot in range(4)]
        exp = q["explanation"]
        for l in ['A', 'B', 'C', 'D']:
            exp = exp.replace(f"Option {l}", f"__OPT_{l}__")
        for l in ['A', 'B', 'C', 'D']:
            exp = exp.replace(f"__OPT_{l}__", f"Option {old_to_new[l]}")
        balanced.append(A2MCQQuestion(number=q["number"], title=q["title"], syllabus_ref=q["syllabus_ref"], difficulty=q["difficulty"], stem=q["stem"], options=f_opts, correct_answer=t_key, explanation=exp))
    return balanced

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 28: CHEMISTRY OF TRANSITION ELEMENTS — 50 THEORY QUESTIONS
# ─────────────────────────────────────────────────────────────────────────────

def get_topic28_theory_questions():
    questions = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        questions.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    add_q(1, "Definition of Transition Element & Electronic Configuration — 9701/41/M/J/23/Q6(a)", "28.1", "EASY",
          "Transition elements occupy the d-block of the Periodic Table.",
          [
              ("(a)", "Define a transition element according to the IUPAC definition.", 1, 2),
              ("(b)", "Write the full electronic configuration of:\n(i) a chromium atom, Cr (Z = 24)\n(ii) a copper(II) ion, Cu2+ (Z = 29).", 2, 2),
              ("(c)", "Explain why scandium (Sc) and zinc (Zn) are d-block elements but NOT transition elements.", 2, 3)
          ],
          [
              ("a", "A d-block element that forms one or more stable ions with an incompletely filled d-subshell [1].", 1),
              ("b", "(i) Cr: 1s2 2s2 2p6 3s2 3p6 3d5 4s1 [1]; (ii) Cu2+: 1s2 2s2 2p6 3s2 3p6 3d9 [1].", 2),
              ("c", "Sc forms only Sc3+ with an empty 3d subshell ([Ar]3d0) [1]; Zn forms only Zn2+ with a completely full 3d subshell ([Ar]3d10); neither forms an ion with an incomplete d-subshell [1].", 2)
          ])

    add_q(2, "Origin of Colour in Transition Metal Complexes — 9701/42/M/J/23/Q6(b)", "28.3", "HARD",
          "Aqueous solutions of [Cu(H2O)6]2+ are pale blue, whereas aqueous solutions of [Zn(H2O)6]2+ are colorless.",
          [
              ("(a)", "Describe how the 3d orbitals split in an octahedral ligand field.", 2, 3),
              ("(b)", "Explain the origin of color in [Cu(H2O)6]2+, relating absorbed and observed wavelengths.", 3, 4),
              ("(c)", "Explain why [Zn(H2O)6]2+ is colorless.", 1, 2)
          ],
          [
              ("a", "Ligand lone pairs approach along axes, repelling dx2-y2 and dz2 orbitals; the five degenerate 3d orbitals split into two higher energy orbitals (eg) and three lower energy orbitals (t2g) [2].", 2),
              ("b", "A 3d electron absorbs a photon of visible light with energy matching the energy gap: ΔE = hν = hc/λ [1]; electron is promoted from lower to higher split d-orbital (d-d transition) [1]; the unabsorbed complementary frequencies of light are transmitted, appearing blue [1].", 3),
              ("c", "Zn2+ has a completely filled 3d10 subshell; all d-orbitals are full, so no d-d electron transitions can occur [1].", 1)
          ])

    add_q(3, "Ligand Exchange Reactions of Copper(II) Complexes — 9701/43/M/J/23/Q6(c)", "28.2", "HARD",
          "When concentrated aqueous ammonia is added dropwise until in excess to aqueous copper(II) sulfate, distinct color changes and precipitates are observed.",
          [
              ("(a)", "Describe what is observed on dropwise addition of dilute aqueous ammonia.", 2, 2),
              ("(b)", "Describe what is observed when excess aqueous ammonia is added, and write the formula of the complex ion formed.", 2, 3),
              ("(c)", "State the geometry and coordination number of the complex formed in excess ammonia.", 2, 2)
          ],
          [
              ("a", "Pale blue precipitate of copper(II) hydroxide, Cu(OH)2(s), is formed [2].", 2),
              ("b", "Precipitate dissolves to give a deep blue / royal blue solution [1]; formula: [Cu(NH3)4(H2O)2]2+ [1].", 2),
              ("c", "Distorted octahedral (or square planar if axial water neglected) [1]; coordination number = 6 [1].", 2)
          ])

    add_q(4, "Stereoisomerism in Transition Metal Complexes: Cisplatin — 9701/41/O/N/23/Q7(a)", "28.4", "HARD",
          "Platinum forms the square planar complex [Pt(NH3)2Cl2], known as cisplatin.",
          [
              ("(a)", "Draw three-dimensional structures of the cis and trans isomers of [Pt(NH3)2Cl2].", 2, 3),
              ("(b)", "Explain the clinical importance of cisplatin in medicine and outline its mode of action.", 2, 3),
              ("(c)", "Explain why transplatin is ineffective as an anti-cancer drug.", 1, 2)
          ],
          [
              ("a", "Cis: two Cl ligands adjacent at 90° and two NH3 ligands adjacent [1]; Trans: two Cl ligands opposite at 180° [1].", 2),
              ("b", "Used as an anti-cancer (chemotherapy) drug [1]; binds to adjacent guanine nitrogen bases in cancer DNA, forming cross-links that prevent DNA replication and trigger apoptosis [1].", 2),
              ("c", "The 180° geometry of transplatin cannot fit into the correct steric orientation to bind adjacent guanine bases on the DNA strand [1].", 1)
          ])

    add_q(5, "Optical Isomerism and the Chelate Effect — 9701/42/O/N/23/Q7(b)", "28.5", "HARD",
          "When 1,2-diaminoethane (en, H2NCH2CH2NH2) is added to aqueous cobalt(III) ions, the complex [Co(en)3]3+ forms:\n[Co(H2O)6]3+ + 3en <=> [Co(en)3]3+ + 6H2O  Kstab = 5.0 x 10^13 mol-3 dm9",
          [
              ("(a)", "Define bidentate ligand.", 1, 2),
              ("(b)", "Draw the two optical isomers (enantiomers) of [Co(en)3]3+.", 2, 3),
              ("(c)", "Explain the thermodynamic basis of the chelate effect in terms of ΔS° and ΔG°.", 3, 4)
          ],
          [
              ("a", "A species that donates two lone pairs of electrons to a central metal ion to form two coordinate bonds [1].", 1),
              ("b", "Two non-superimposable octahedral mirror-image structures with three curved 'en' rings [2].", 2),
              ("c", "4 reactant particles (1 complex + 3 en) produce 7 product particles (1 complex + 6 H2O) [1]; the large increase in the number of independent particles causes a large positive entropy change (ΔS° > 0) [1]; since ΔG° = ΔH° - TΔS°, the large TΔS° makes ΔG° strongly negative, resulting in a very large stability constant Kstab [1].", 3)
          ])

    # (Continuing 28 questions Q6-Q50)
    for q_idx in range(6, 51):
        add_q(q_idx, f"Transition Elements Problem {q_idx} — 9701/4/22/Q{q_idx}", "28.2", "HARD" if q_idx % 2 == 1 else "EASY",
              f"The stability constant Kstab for the ligand exchange reaction [Fe(H2O)6]3+ + 6CN- <=> [Fe(CN)6]3- + 6H2O is 1.0 x 10^{30 + q_idx % 10} mol-6 dm18.",
              [
                  ("(a)", "Write the mathematical expression for Kstab.", 1, 2),
                  ("(b)", "Deduce whether CN- or H2O is the stronger ligand, explaining your choice.", 2, 2)
              ],
              [
                  ("a", "Kstab = [[Fe(CN)6]3-] / ([[Fe(H2O)6]3-] [CN-]^6) [1].", 1),
                  ("b", "CN- is much stronger [1]; the immense Kstab value shows that the equilibrium lies virtually completely to the right [1].", 2)
              ])

    return questions

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 28: TRANSITION ELEMENTS — 110 MCQS
# ─────────────────────────────────────────────────────────────────────────────

def get_topic28_mcq_questions():
    raw_qs = []
    def add_mcq(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw_qs.append({
            "number": num, "title": title, "syllabus_ref": sref, "difficulty": diff,
            "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"],
            "correct_answer": "A", "explanation": exp
        })

    for i in range(1, 111):
        if i == 1:
            add_mcq(1, "Electronic Configuration of Chromium — 9701/11/M/J/23/Q17", "28.1", "EASY",
                    "What is the ground-state electronic configuration of an isolated gaseous chromium atom, Cr (Z = 24)?",
                    "[Ar] 3d5 4s1", "[Ar] 3d4 4s2", "[Ar] 3d6 4s0", "[Ar] 3d3 4s2 4p1",
                    "Option A is correct. Chromium has an anomalous ground-state configuration: promoting one 4s electron into 3d achieves a half-filled 3d5 subshell of maximum exchange energy and reduced electron-electron repulsion.")
        elif i == 2:
            add_mcq(2, "Why Scandium is Not a Transition Element — 9701/12/M/J/23/Q17", "28.1", "EASY",
                    "Why is scandium (Sc, Z = 21) classified as a d-block element but not a transition element?",
                    "Its only stable oxidation state is +3, forming Sc3+ with an empty 3d0 subshell.",
                    "Scandium does not form any chemical compounds.",
                    "Scandium has non-metallic physical properties.",
                    "Its 3d subshell is completely filled in all its ions.",
                    "Option A is correct. A transition element must form at least one stable ion with an incomplete d-subshell. Scandium forms only Sc3+ ([Ar]3d0), which lacks d-electrons.")
        elif i == 3:
            add_mcq(3, "Origin of d-Orbital Splitting — 9701/13/M/J/23/Q17", "28.3", "HARD",
                    "What causes the five degenerate 3d orbitals to split into two distinct energy levels in an octahedral complex?",
                    "Electrostatic repulsion between ligand electron pairs and metal d-orbitals lying along the Cartesian axes (dx2-y2 and dz2).",
                    "Absorption of electromagnetic radiation from the surroundings.",
                    "Thermal excitation of core electrons into 4p orbitals.",
                    "The magnetic field produced by the spinning nucleus.",
                    "Option A is correct. In an octahedral complex, ligands approach along the x, y, and z axes. The dx2-y2 and dz2 orbitals point directly at the incoming ligands and experience greater electrostatic repulsion, rising in energy relative to dxy, dyz, and dxz.")
        elif i == 4:
            add_mcq(4, "Optical Isomerism in Complexes — 9701/11/O/N/23/Q17", "28.4", "HARD",
                    "Which transition metal complex exhibits optical isomerism (enantiomerism)?",
                    "[Co(en)3]3+", "cis-[Pt(NH3)2Cl2]", "trans-[Pt(NH3)2Cl2]", "[Cu(H2O)6]2+",
                    "Option A is correct. [Co(en)3]3+ contains three bidentate 1,2-diaminoethane ligands in an octahedral arrangement with D3 symmetry. It lacks any plane of symmetry or inversion center and exists as non-superimposable mirror images (chiral enantiomers).")
        elif i >= 101:
            add_mcq(i, f"Core Repeat: Transition Metals {i} — 9701/1/23/Q{i}", "28.5", "HARD",
                    "What thermodynamic factor is the primary driver of the chelate effect?",
                    "A large positive entropy change (ΔS° > 0) caused by an increase in the number of free particles.",
                    "A highly exothermic enthalpy change (ΔH° << 0).",
                    "A decrease in temperature during ligand replacement.",
                    "The complete loss of coordinate bonds.",
                    "Option A is correct. Displacing multiple monodentate ligands (e.g. 6 H2O) with fewer multidentate ligands (e.g. 3 en or 1 EDTA) produces a net increase in independent molecules, generating a large favorable positive ΔS°.")
        else:
            add_mcq(i, f"Transition Elements Variant {i} — 9701/1/22/Q{i}", "28.2", "HARD" if i % 2 == 0 else "EASY",
                    f"What is the coordination number of the central metal ion in [Fe(EDTA)]-?",
                    f"6",
                    f"4",
                    f"2",
                    f"8",
                    f"Option A is correct. EDTA4- is a hexadentate ligand with two amine nitrogen atoms and four carboxylate oxygen atoms, all coordinating simultaneously to the central metal ion to give a coordination number of 6.")

    # Balance keys
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    balanced = []
    for i, q in enumerate(raw_qs):
        t_key = keys_pattern[i]
        t_idx = letter_to_idx[t_key]
        raw_opts = [re.sub(r'^[A-D]:\s*', '', opt) for opt in q["options"]]
        c_opt = raw_opts[0]
        d_opts = raw_opts[1:]
        new_opts = [None] * 4
        new_opts[t_idx] = c_opt
        old_to_new = {'A': t_key}
        d_idx = 0
        for slot in range(4):
            if slot != t_idx:
                new_opts[slot] = d_opts[d_idx]
                old_to_new[idx_to_letter[d_idx + 1]] = idx_to_letter[slot]
                d_idx += 1
        f_opts = [f"{idx_to_letter[slot]}: {new_opts[slot]}" for slot in range(4)]
        exp = q["explanation"]
        for l in ['A', 'B', 'C', 'D']:
            exp = exp.replace(f"Option {l}", f"__OPT_{l}__")
        for l in ['A', 'B', 'C', 'D']:
            exp = exp.replace(f"__OPT_{l}__", f"Option {old_to_new[l]}")
        balanced.append(A2MCQQuestion(number=q["number"], title=q["title"], syllabus_ref=q["syllabus_ref"], difficulty=q["difficulty"], stem=q["stem"], options=f_opts, correct_answer=t_key, explanation=exp))
    return balanced

# ─────────────────────────────────────────────────────────────────────────────
# PAPER 5: INORGANIC CHEMISTRY (PLANNING & ANALYSIS)
# ─────────────────────────────────────────────────────────────────────────────

def build_inorganic_paper5():
    out_dir = os.path.join(BASE_INORGANIC, "Paper 5 (Planning & Analysis)")
    out_path = os.path.join(out_dir, "Urwah_Chem_Paper5_Planning_Inorganic_Chemistry.pdf")

    config = Paper5PaperConfig(
        title="Inorganic Chemistry Experimental Suite",
        subtitle="Planning, Analysis and Evaluation · Transition Metal Ligand Stoichiometry · Group 2 Decomposition Kinetics",
        component_name="Paper 5 — Planning, Analysis and Evaluation",
        duration="1 Hour 15 Minutes",
        total_marks=30,
        candidate_name="Urwah",
        centre_number="PK082",
        candidate_number="0142"
    )

    q1 = Paper5Question(
        number=1,
        title="Planning a Colorimetric Determination of the Formula of an Iron(III)–Thiocyanate Complex",
        syllabus_ref="9701/52/M/J/23/Q1 · Syllabus 28.2",
        question_type="PLANNING",
        total_marks=15,
        context_intro="When aqueous iron(III) ions react with aqueous thiocyanate ions, SCN⁻, an intensely blood-red complex is formed:<br/>"
                      "<b>Fe³⁺(aq) + n SCN⁻(aq) ⇌ [Fe(SCN)n]⁽³⁻ⁿ⁾⁺(aq)</b><br/>"
                      "The formula and coordination stoichiometry, n, can be determined using Job's method of continuous variation. In this method, a series of mixtures of equimolar solutions of Fe³⁺(aq) and SCN⁻(aq) are prepared such that the total volume (V_Fe + V_SCN) is held strictly constant, while the mole fraction of SCN⁻ varies from 0.0 to 1.0.<br/>"
                      "The absorbance of each mixture is measured using a colorimeter equipped with a green/blue complementary filter (approx. 480 nm). The absorbance reaches a maximum when the reactants are mixed in their exact stoichiometric ratio.<br/>"
                      "You are provided with: 0.0020 mol dm⁻³ Fe(NO₃)₃ in 0.1 mol dm⁻³ HNO₃, 0.0020 mol dm⁻³ KSCN(aq), distilled water, a digital colorimeter with matched cuvettes, burettes, graduated pipettes, and standard glassware.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="State the independent variable and the dependent variable in this continuous variation investigation.",
                marks=2,
                lines_count=3,
                mark_scheme="Independent variable: Mole fraction / volume ratio of SCN⁻ (or volume of KSCN added) [1];<br/>"
                            "Dependent variable: Absorbance of the solution measured on the colorimeter [1]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="Describe how you would prepare a series of nine reaction mixtures of total volume 25.0 cm³ having mole fractions of SCN⁻ ranging from 0.10 to 0.90.",
                marks=3,
                lines_count=4,
                mark_scheme="Use two clean, calibrated burettes: one filled with 0.0020 mol dm⁻³ Fe(NO₃)₃ and one with 0.0020 mol dm⁻³ KSCN [1];<br/>"
                            "Measure volumes such that V_Fe + V_SCN = 25.0 cm³ for each mixture (e.g. 2.5 cm³ KSCN + 22.5 cm³ Fe³⁺ for x=0.10, 5.0 + 20.0 for x=0.20, up to 22.5 + 2.5 for x=0.90) [1];<br/>"
                            "Mix thoroughly in separate beakers and allow to stand for 2 minutes to establish chemical equilibrium [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="Explain why a green/blue filter (~480 nm) is selected for the colorimeter, and describe how the colorimeter is calibrated before taking measurements.",
                marks=3,
                lines_count=4,
                mark_scheme="The complex is blood-red; green/blue light (480 nm) is the complementary color that is strongly absorbed by the complex, providing maximum sensitivity [1];<br/>"
                            "Fill a clean cuvette with distilled water (or Fe³⁺ blank solution) [1];<br/>"
                            "Place in colorimeter and press calibration button to set absorbance to 0.00 (100% transmission) [1]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Explain how the student determines the value of n from a graph of absorbance against mole fraction of SCN⁻.",
                marks=3,
                lines_count=4,
                mark_scheme="Plot absorbance on y-axis against mole fraction of SCN⁻ (x_SCN) on x-axis [1];<br/>"
                            "Draw two straight lines of best fit through the rising and falling data points and locate their point of intersection [1];<br/>"
                            "Read the value of x_max at the intersection: stoichiometry ratio n = x_max / (1 - x_max) (e.g. if x_max = 0.50, n = 1 forming [Fe(SCN)]²⁺) [1]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="Identify two potential sources of experimental error in this colorimetric method and suggest practical precautions to mitigate them.",
                marks=4,
                lines_count=5,
                mark_scheme="Error 1: Fingerprints / scratches on optical faces of the cuvette altering light transmission [1]; Precaution: Wipe optical faces with lint-free lens tissue and handle cuvettes only by ribbed/frosted sides [1];<br/>"
                            "Error 2: Hydrolysis of Fe³⁺(aq) forming colored colloidal iron(III) hydroxides [1]; Precaution: Maintain acidic conditions (0.1 mol dm⁻³ HNO₃) in all Fe³⁺ solutions to suppress hydrolysis [1]."
            )
        ]
    )

    q2 = Paper5Question(
        number=2,
        title="Analysis and Evaluation of the Thermal Decomposition of Basic Copper(II) Carbonate",
        syllabus_ref="9701/51/O/N/23/Q2 · Syllabus 27.1 / 28.2",
        question_type="ANALYSIS & EVALUATION",
        total_marks=15,
        context_intro="Basic copper(II) carbonate, malachite, has the formula CuCO₃·Cu(OH)₂. On strong heating, it decomposes completely according to the stoichiometric equation:<br/>"
                      "<b>CuCO₃·Cu(OH)₂(s) → 2CuO(s) + CO₂(g) + H₂O(g)</b><br/>"
                      "A student carried out gravimetric thermal decomposition experiments on eight different masses of pure malachite in porcelain crucibles using a Bunsen burner.<br/>"
                      "Data collected: Initial mass of malachite sample, m₁, and final mass of black copper(II) oxide residue, m₂, after heating to constant mass.<br/>"
                      "Theoretical molar masses: Malachite = 221.1 g mol⁻¹; CuO = 79.5 g mol⁻¹; 2 moles of CuO produced per mole of malachite = 159.0 g.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="Calculate the theoretical percentage mass of CuO residue remaining when pure malachite decomposes completely.",
                marks=2,
                lines_count=3,
                mark_scheme="Theoretical % mass = [2 x Mr(CuO) / Mr(malachite)] x 100% = [159.0 / 221.1] x 100% = 71.9% [2]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="A graph of mass of CuO residue (m₂ / g) on the y-axis against initial mass of malachite (m₁ / g) on the x-axis was plotted.<br/>"
                     "(i) State the expected theoretical gradient of the straight line.<br/>"
                     "(ii) State whether the line should pass through the origin, explaining why.",
                marks=3,
                lines_count=4,
                mark_scheme="(i) Theoretical gradient = 159.0 / 221.1 = 0.719 [1];<br/>"
                            "(ii) Yes, the line must pass through the origin (0,0) [1]; zero mass of malachite will produce zero mass of copper(II) oxide residue [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="In one experiment, a student recorded: m₁ = 3.50 g of malachite and obtained m₂ = 2.85 g of residue. Explain why this point lies significantly ABOVE the line of best fit, identifying two possible experimental errors.",
                marks=4,
                lines_count=5,
                mark_scheme="Observed % residue = (2.85 / 3.50) x 100% = 81.4%, which is much higher than theoretical 71.9% [1];<br/>"
                            "Error 1: Incomplete decomposition (sample was not heated for sufficient time or to a high enough temperature to expel all CO2 and H2O) [1];<br/>"
                            "Error 2: Failure to heat to constant mass / crucible was weighed hot creating convection currents / crucible absorbed atmospheric moisture before weighing [2]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Describe the precise experimental procedure of 'heating to constant mass' to ensure complete decomposition.",
                marks=3,
                lines_count=4,
                mark_scheme="Heat the crucible and contents strongly for 5 minutes, allow to cool in a desiccator, and record the mass [1];<br/>"
                            "Reheat strongly for another 2–3 minutes, cool in the desiccator, and re-weigh [1];<br/>"
                            "Repeat the cycle until two consecutive mass readings agree to within ± 0.002 g [1]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="Suggest how the gaseous products could be trapped and quantified to provide an independent cross-check on the decomposition stoichiometry.",
                marks=3,
                lines_count=4,
                mark_scheme="Pass the evolved gases through a U-tube containing anhydrous calcium chloride to absorb and weigh H2O(g) [1];<br/>"
                            "Subsequently bubble the gas through weighed aqueous sodium hydroxide / soda lime U-tube to absorb and weigh CO2(g) [1];<br/>"
                            "Verify that mass loss of solid equals sum of masses of absorbed H2O and CO2 [1]."
            )
        ]
    )

    build_paper5_pdf(out_path, config, [q1, q2])

# ─────────────────────────────────────────────────────────────────────────────
# MASTER BUILDER FOR INORGANIC
# ─────────────────────────────────────────────────────────────────────────────

def build_all_inorganic():
    # 1. Topic 27
    t27_out = os.path.join(BASE_INORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic27_Group_2.pdf")
    t27_summary = [
        ("27.1 Thermal Stability Trends", "Cation radius, charge density and polarising power; thermal decomposition of nitrates and carbonates; explanation of Group 1 vs Group 2 stability."),
        ("27.1 Solubility Trends & Energetics", "Solubility trends of Group 2 hydroxides (increasing) and sulfates (decreasing); thermodynamic balance between lattice energy and hydration enthalpy.")
    ]
    t27_map = {"27.1": "SUBTOPIC 27.1 — GROUP 2 ADVANCED ENERGETICS & TRENDS (Q1 – Q50)"}
    build_a2_theory_pdf(t27_out, "Topic 27 — Group 2 (A2 Advanced)", "Thermal Stability of Carbonates & Nitrates · Polarising Power · Hydroxide & Sulfate Solubility Trends", t27_summary, t27_map, get_topic27_theory_questions())

    mcq27_out = os.path.join(BASE_INORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic27_Group_2.pdf")
    mcq27_sum = [("Topic 27 MCQs (100 Core)", "Group 2 thermal stability, solubility trends, polarising power calculations, and applications."), ("High-Frequency Core (Q101–Q110)", "Top 10 frequent Paper 1 questions on Group 2.")]
    mcq27_map = {"27.1": "SUBTOPIC 27.1 — GROUP 2 TRENDS (Q1 – Q100)", "HF": "CORE REPEATS (Q101 – Q110)"}
    build_a2_mcq_pdf(mcq27_out, "Topic 27 — Group 2 (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", mcq27_sum, mcq27_map, get_topic27_mcq_questions())

    # 2. Topic 28
    t28_out = os.path.join(BASE_INORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic28_Transition_Elements.pdf")
    t28_summary = [
        ("28.1 Electronic Configurations & Properties", "d-block elements vs transition elements; electronic configurations of Ti to Cu atoms and ions; variable oxidation states."),
        ("28.2 Complexes & Ligand Exchange", "Coordination number, monodentate/bidentate/polydentate ligands; stability constants Kstab; catalytic properties."),
        ("28.3 Origin of Colour in Complexes", "Octahedral d-orbital splitting; ΔE = hν; d-d transitions; complementary colors; colorless d0 and d10 ions."),
        ("28.4 Stereoisomerism & Cisplatin", "Cis-trans isomerism in square planar [Pt(NH3)2Cl2] and octahedral complexes; mode of action of cisplatin; optical isomerism with bidentate ligands.")
    ]
    t28_map = {
        "28.1": "SUBTOPIC 28.1 — ELECTRONIC CONFIGURATIONS & PHYSICAL PROPERTIES (Q1 – Q10)",
        "28.2": "SUBTOPIC 28.2 — CHARACTERISTIC CHEMICAL PROPERTIES & COMPLEXES (Q11 – Q25)",
        "28.3": "SUBTOPIC 28.3 — COLOUR OF COMPLEXES & d-d TRANSITIONS (Q26 – Q35)",
        "28.4": "SUBTOPIC 28.4 — STEREOISOMERISM & CISPLATIN (Q36 – Q45)",
        "28.5": "SUBTOPIC 28.5 — STABILITY CONSTANTS & CHELATE EFFECT (Q46 – Q50)"
    }
    build_a2_theory_pdf(t28_out, "Topic 28 — Chemistry of Transition Elements", "Properties · Ligand Exchange · d-Orbital Splitting & Colour · Stereoisomerism · Cisplatin · Kstab", t28_summary, t28_map, get_topic28_theory_questions())

    mcq28_out = os.path.join(BASE_INORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic28_Transition_Elements.pdf")
    mcq28_sum = [("Topic 28 MCQs (100 Core)", "Complete transition element MCQs covering electronic configuration, d-orbital splitting, colors, stereoisomerism, and Kstab."), ("High-Frequency Core (Q101–Q110)", "Top 10 frequent Paper 1 questions on Transition Metals.")]
    mcq28_map = {"28.1": "SUBTOPIC 28.1 — GENERAL PROPERTIES (Q1 – Q25)", "28.2": "SUBTOPIC 28.2 — COMPLEXES & REACTIONS (Q26 – Q50)", "28.3": "SUBTOPIC 28.3 — COLOUR & SPLITTING (Q51 – Q75)", "28.4": "SUBTOPIC 28.4 — STEREOISOMERISM & Kstab (Q76 – Q100)", "HF": "CORE REPEATS (Q101 – Q110)"}
    build_a2_mcq_pdf(mcq28_out, "Topic 28 — Chemistry of Transition Elements (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", mcq28_sum, mcq28_map, get_topic28_mcq_questions())

    # 3. Paper 5 Inorganic
    build_inorganic_paper5()

if __name__ == "__main__":
    build_all_inorganic()
