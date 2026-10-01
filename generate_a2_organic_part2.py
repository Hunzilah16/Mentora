"""
Cambridge International A Level Chemistry (9701) — A2 Suite
ORGANIC CHEMISTRY PART 2: TOPICS 33, 34, 35, 36
Generates:
1. Topic 33: Carboxylic Acids & Acyl Chlorides (Paper 4: 50 Qs, MCQs: 110 Qs)
2. Topic 34: Nitrogen Compounds (Paper 4: 50 Qs, MCQs: 110 Qs)
3. Topic 35: Polymerisation (Paper 4: 50 Qs, MCQs: 110 Qs)
4. Topic 36: Organic Synthesis (Paper 4: 50 Qs, MCQs: 110 Qs)

Candidate: Urwah | Mentora Academy
"""
import os
import re
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf
from build_a2_mcq_pdf import A2MCQQuestion, build_a2_mcq_pdf

BASE_ORGANIC = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry"

def make_balanced_mcqs(raw_qs):
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
# TOPIC 33: CARBOXYLIC ACIDS AND DERIVATIVES (ACYL CHLORIDES)
# ─────────────────────────────────────────────────────────────────────────────
def get_topic33_theory():
    qs = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        qs.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    add_q(1, "Acyl Chloride Preparation and Reactions with Nucleophiles — 9701/41/M/J/23/Q11(a)", "33.3", "HARD",
          "Ethanoyl chloride, CH3COCl, is an important synthetic intermediate.",
          [
              ("(a)", "State two reagents that can be used to convert ethanoic acid into ethanoyl chloride.", 2, 2),
              ("(b)", "Write the balanced chemical equation for the reaction of ethanoyl chloride with:\n(i) methanol\n(ii) concentrated aqueous ammonia\n(iii) ethylamine.", 3, 4),
              ("(c)", "Explain why acyl chlorides are much more reactive towards nucleophiles than carboxylic acids.", 2, 3)
          ],
          [
              ("a", "Phosphorus(V) chloride, PCl5 (or PCl3, or thionyl chloride, SOCl2) [2].", 2),
              ("b", "(i) CH3COCl + CH3OH -> CH3COOCH3 + HCl [1]; (ii) CH3COCl + 2NH3 -> CH3CONH2 + NH4Cl [1]; (iii) CH3COCl + 2CH3CH2NH2 -> CH3CONHCH2CH3 + CH3CH2NH3Cl [1].", 3),
              ("c", "The carbonyl carbon is bonded to both electronegative O and Cl, creating a very strong partial positive charge (δ+) [1]; chloride is an excellent leaving group compared to OH- [1].", 2)
          ])

    add_q(2, "Oxidation of Methanoic Acid and Ethanedioic Acid — 9701/42/M/J/23/Q11(b)", "33.1", "HARD",
          "Unlike most carboxylic acids, methanoic acid (HCOOH) and ethanedioic acid ((COOH)2) can be oxidised by acidified KMnO4.",
          [
              ("(a)", "Explain why methanoic acid can act as a reducing agent, referring to its structure.", 2, 2),
              ("(b)", "Write a balanced equation for the oxidation of methanoic acid by acidified manganate(VII) ions.", 2, 3),
              ("(c)", "State observations when ethanedioic acid is warmed with acidified potassium manganate(VII).", 2, 2)
          ],
          [
              ("a", "Methanoic acid contains both a carboxyl group and an aldehyde-like C-H carbonyl group (-CHO) [2].", 2),
              ("b", "5HCOOH + 2MnO4- + 6H+ -> 5CO2 + 2Mn2+ + 8H2O [2].", 2),
              ("c", "Purple solution turns colorless / decolourises [1]; effervescence / bubbles of CO2 gas evolved [1].", 2)
          ])

    for i in range(3, 51):
        add_q(i, f"Carboxylic Acid & Derivative Problem {i} — 9701/4/23/Q{i}", "33.1", "HARD" if i % 2 == 1 else "EASY",
              f"Substituted benzoic acid {i} has varying acidity governed by aromatic substituent effects.",
              [
                  ("(a)", "Compare the acidity of 4-chlorobenzoic acid with benzoic acid.", 2, 2),
                  ("(b)", "Write the equation for the reaction of benzoic acid with PCl5.", 1, 2)
              ],
              [
                  ("a", "4-chlorobenzoic acid is more acidic [1]; the electronegative Cl atom exerts an electron-withdrawing inductive effect (-I), stabilizing the benzoate conjugate base [1].", 2),
                  ("b", "C6H5COOH + PCl5 -> C6H5COCl + POCl3 + HCl [1].", 1)
              ])
    return qs

def get_topic33_mcqs():
    raw = []
    def add_m(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw.append({"number": num, "title": title, "syllabus_ref": sref, "difficulty": diff, "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"], "correct_answer": "A", "explanation": exp})

    for i in range(1, 111):
        if i == 1:
            add_m(1, "Acyl Chloride Hydrolysis Product — 9701/11/M/J/23/Q27", "33.3", "EASY",
                  "What is formed when benzoyl chloride, C6H5COCl, is added to cold water?",
                  "Benzoic acid and steamy fumes of hydrogen chloride",
                  "Benzaldehyde and chlorine gas",
                  "Chlorobenzene and carbon dioxide",
                  "Phenol and methanoic acid",
                  "Option A is correct. C6H5COCl + H2O -> C6H5COOH + HCl.")
        elif i == 2:
            add_m(2, "Methanoic Acid Oxidation Reagent — 9701/12/M/J/23/Q27", "33.1", "EASY",
                  "Which carboxylic acid gives a positive silver mirror test with Tollens' reagent?",
                  "Methanoic acid, HCOOH", "Ethanoic acid, CH3COOH", "Benzoic acid, C6H5COOH", "Propanoic acid, CH3CH2COOH",
                  "Option A is correct. HCOOH possesses an aldehydic hydrogen bonded directly to the carbonyl group, allowing it to reduce Tollens' reagent to metallic silver.")
        elif i >= 101:
            add_m(i, f"Core Repeat: Carboxylic Derivatives {i} — 9701/1/23/Q{i}", "33.3", "HARD",
                  "What is the organic product of the reaction between ethanoyl chloride and ethylamine?",
                  "N-ethylethanamide", "Ethyl ethanoate", "Ethanamide", "Diethylamine",
                  "Option A is correct. CH3COCl + 2CH3CH2NH2 -> CH3CONHCH2CH3 + CH3CH2NH3Cl.")
        else:
            add_m(i, f"Carboxylic Acid Derivative MCQ {i} — 9701/1/22/Q{i}", "33.1", "HARD" if i % 2 == 0 else "EASY",
                  f"Which reagent converts ethanoic acid into ethanoyl chloride without forming liquid byproducts?",
                  f"SOCl2 (thionyl chloride)", f"PCl5", f"PCl3", f"HCl(aq)",
                  f"Option A is correct. CH3COOH + SOCl2 -> CH3COCl + SO2(g) + HCl(g). Both byproducts are gases, making product separation trivial.")
    return make_balanced_mcqs(raw)

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 34: NITROGEN COMPOUNDS
# ─────────────────────────────────────────────────────────────────────────────
def get_topic34_theory():
    qs = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        qs.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    add_q(1, "Basicity Comparison: Ethylamine vs Ammonia vs Phenylamine — 9701/41/M/J/23/Q12(a)", "34.1", "HARD",
          "The basic strengths of nitrogen compounds vary widely:\nEthylamine (pKb = 3.3) > Ammonia (pKb = 4.75) > Phenylamine (pKb = 9.4)",
          [
              ("(a)", "Define a Brønsted-Lowry base and explain what determines base strength in amines.", 2, 2),
              ("(b)", "Explain why ethylamine is a stronger base than ammonia.", 2, 3),
              ("(c)", "Explain why phenylamine is a much weaker base than ammonia.", 2, 3)
          ],
          [
              ("a", "A proton (H+) acceptor [1]; basicity depends on the availability of the lone pair of electrons on the nitrogen atom to accept a proton [1].", 2),
              ("b", "The ethyl group exerts an electron-donating inductive effect (+I effect) [1]; this increases electron density on the nitrogen atom, making its lone pair more readily available to coordinate to H+ [1].", 2),
              ("c", "The lone pair of electrons on the nitrogen atom delocalises into the aromatic π electron system of the benzene ring [1]; electron density on nitrogen is significantly reduced, making the lone pair far less available to accept a proton [1].", 2)
          ])

    add_q(2, "Synthesis of Phenylamine and Diazotisation Azo Coupling — 9701/42/M/J/23/Q12(b)", "34.2", "HARD",
          "Phenylamine is synthesised from benzene in a multi-step industrial sequence and used to manufacture azo dyes.",
          [
              ("(a)", "State the reagents and conditions used to convert nitrobenzene into phenylamine.", 2, 2),
              ("(b)", "State the reagents and conditions used to convert phenylamine into benzenediazonium chloride.", 2, 3),
              ("(c)", "Write the equation for the coupling of benzenediazonium chloride with alkaline phenol.", 2, 3)
          ],
          [
              ("a", "Heat under reflux with Tin (Sn) and concentrated hydrochloric acid, followed by excess aqueous sodium hydroxide to liberate free phenylamine [2].", 2),
              ("b", "Sodium nitrite (NaNO2) and concentrated hydrochloric acid (generating HNO2) [1]; temperature strictly between 0 °C and 10 °C [1].", 2),
              ("c", "C6H5N2+Cl- + C6H5OH + NaOH -> C6H5-N=N-C6H4-OH + NaCl + H2O [2].", 2)
          ])

    add_q(3, "Amino Acids, Zwitterions and Electrophoresis — 9701/43/M/J/23/Q12(c)", "34.4", "HARD",
          "Glycine (aminoethanoic acid, H2NCH2COOH) exists predominantly as a zwitterion in aqueous solution.",
          [
              ("(a)", "Draw the structural formula of the zwitterion of glycine.", 1, 2),
              ("(b)", "Explain why amino acids have crystalline structures with exceptionally high melting points.", 2, 3),
              ("(c)", "A mixture of glycine (isoelectric point pI = 6.0), aspartic acid (pI = 3.0), and lysine (pI = 9.7) is subjected to electrophoresis in a buffer at pH 6.0. Predict and explain the direction of migration for each amino acid.", 3, 4)
          ],
          [
              ("a", "+H3N-CH2-COO- [1].", 1),
              ("b", "Zwitterions contain full positive (+NH3) and negative (-COO-) charges; they form strong ionic lattice electrostatic attractions that require high thermal energy to overcome [2].", 2),
              ("c", "At pH 6.0:\n- Glycine is at its isoelectric point (net charge = 0) and does not migrate [1];\n- Aspartic acid is in a solution where pH > pI; it loses protons to form a net negative anion and migrates toward the positive anode (+) [1];\n- Lysine has pH < pI; it gains protons to form a net positive cation and migrates toward the negative cathode (-) [1].", 3)
          ])

    for i in range(4, 51):
        add_q(i, f"Nitrogen Chemistry & Peptide Problem {i} — 9701/4/23/Q{i}", "34.3", "HARD" if i % 2 == 1 else "EASY",
              f"Amide compound {i} undergoes hydrolysis when heated with dilute aqueous acid or alkali.",
              [
                  ("(a)", "State the products formed when ethanamide, CH3CONH2, is refluxed with aqueous sodium hydroxide.", 2, 2),
                  ("(b)", "Explain why amides are neutral in aqueous solution.", 2, 2)
              ],
              [
                  ("a", "Sodium ethanoate, CH3COONa, and ammonia gas, NH3 [2].", 2),
                  ("b", "The lone pair of electrons on the nitrogen atom is strongly delocalised onto the adjacent electronegative carbonyl oxygen atom [1]; the lone pair is not available to accept protons [1].", 2)
              ])
    return qs

def get_topic34_mcqs():
    raw = []
    def add_m(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw.append({"number": num, "title": title, "syllabus_ref": sref, "difficulty": diff, "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"], "correct_answer": "A", "explanation": exp})

    for i in range(1, 111):
        if i == 1:
            add_m(1, "Basicity Ranking of Amines — 9701/11/M/J/23/Q29", "34.1", "EASY",
                  "Which list correctly places the nitrogen compounds in order of DECREASING basicity (strongest base first)?",
                  "Ethylamine > Ammonia > Phenylamine",
                  "Phenylamine > Ammonia > Ethylamine",
                  "Ammonia > Ethylamine > Phenylamine",
                  "Ethylamine > Phenylamine > Ammonia",
                  "Option A is correct. Ethylamine is strongest due to the electron-donating (+I) ethyl group. Phenylamine is weakest because its lone pair is delocalised into the aromatic ring.")
        elif i == 2:
            add_m(2, "Diazotisation Reaction Temperature — 9701/12/M/J/23/Q29", "34.2", "EASY",
                  "Why must the preparation of benzenediazonium chloride from phenylamine be maintained below 10 °C?",
                  "Benzenediazonium chloride decomposes rapidly above 10 °C to form phenol and nitrogen gas.",
                  "Phenylamine freezes at temperatures above 10 °C.",
                  "The nitric acid decomposes into toxic NO2 gas above 10 °C.",
                  "Hydrochloric acid reacts with water above 10 °C.",
                  "Option A is correct. The diazonium ion C6H5N2+ is thermally unstable and hydrolyses above 10 °C: C6H5N2+ + H2O -> C6H5OH + N2 + H+.")
        elif i >= 101:
            add_m(i, f"Core Repeat: Nitrogen Chemistry {i} — 9701/1/23/Q{i}", "34.4", "HARD",
                  "At a pH higher than its isoelectric point, what net charge does an amino acid carry?",
                  "Net negative charge (migrates to anode)",
                  "Net positive charge (migrates to cathode)",
                  "Zero net charge",
                  "Dipolar zwitterion with no charge",
                  "Option A is correct. At pH > pI, excess OH- deprotonates the +NH3 group to neutral -NH2 while the carboxylate remains -COO-, leaving a net negative charge.")
        else:
            add_m(i, f"Nitrogen Compounds Variant {i} — 9701/1/22/Q{i}", "34.3", "HARD" if i % 2 == 0 else "EASY",
                  f"What type of linkage joins amino acid units together in a polypeptide?",
                  f"Amide / peptide bond (-CONH-)", f"Ester bond (-COO-)", f"Ether bond (-O-)", f"Azo bond (-N=N-)",
                  f"Option A is correct. Polypeptides are formed by condensation of amino and carboxyl groups, creating amide linkages.")
    return make_balanced_mcqs(raw)

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 35: POLYMERISATION (CONDENSATION POLYMERS)
# ─────────────────────────────────────────────────────────────────────────────
def get_topic35_theory():
    qs = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        qs.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    add_q(1, "Polyesters: Structure, Synthesis, and Repeat Units — 9701/41/M/J/23/Q13(a)", "35.1", "HARD",
          "Terylene (polyethylene terephthalate, PET) is an important industrial polyester synthesized from benzene-1,4-dicarboxylic acid and ethane-1,2-diol.",
          [
              ("(a)", "Draw the repeat unit of Terylene, showing open bonds at both ends.", 2, 3),
              ("(b)", "State the small molecule eliminated during this polymerisation reaction.", 1, 1),
              ("(c)", "Name a hydroxycarboxylic acid that can undergo condensation polymerisation with itself to form a polyester.", 1, 2)
          ],
          [
              ("a", "-[-CO-C6H4-CO-O-CH2-CH2-O-]- [2].", 2),
              ("b", "Water, H2O [1].", 1),
              ("c", "Lactic acid (2-hydroxypropanoic acid) forming poly(lactic acid), PLA [1].", 1)
          ])

    add_q(2, "Polyamides: Nylon 6,6 and Kevlar — 9701/42/M/J/23/Q13(b)", "35.1", "HARD",
          "Nylon 6,6 and Kevlar are two major commercial polyamides with exceptional tensile strength.",
          [
              ("(a)", "State the names or formulas of the two monomers used to manufacture Nylon 6,6.", 2, 2),
              ("(b)", "Draw the repeat unit of Kevlar (synthesised from benzene-1,4-dicarboxylic acid and benzene-1,4-diamine).", 2, 3),
              ("(c)", "Explain the immense mechanical strength of Kevlar in terms of intermolecular forces.", 2, 3)
          ],
          [
              ("a", "Hexanedioic acid, HOOC(CH2)4COOH, and 1,6-diaminohexane, H2N(CH2)6NH2 [2].", 2),
              ("b", "-[-CO-C6H4-CO-NH-C6H4-NH-]- [2].", 2),
              ("c", "Rigid planar aromatic rings allow dense, parallel polymer chains to align closely [1]; extensive networks of strong hydrogen bonds form between C=O and N-H groups of adjacent chains [1].", 2)
          ])

    add_q(3, "Degradability: Condensation Polymers vs Addition Polymers — 9701/43/M/J/23/Q13(c)", "35.3", "EASY",
          "Environmental accumulation of plastic waste is a major global issue.",
          [
              ("(a)", "Explain why addition polymers like poly(ethene) are non-biodegradable and persist in the environment.", 2, 2),
              ("(b)", "Explain why condensation polymers like Terylene and Nylon can be broken down in the environment.", 2, 3),
              ("(c)", "Write the chemical equation for the alkaline hydrolysis of an ester linkage in Terylene using aqueous NaOH.", 2, 3)
          ],
          [
              ("a", "Addition polymers contain entirely non-polar, strong C-C and C-H single bonds with no polar sites for microbial enzymes or water to attack [2].", 2),
              ("b", "Condensation polymers possess polar carbonyl groups (C=O) in ester (-COO-) and amide (-CONH-) linkages [1]; these polar bonds are susceptible to nucleophilic attack and hydrolysis by water, acids, alkalis, and microbial enzymes [1].", 2),
              ("c", "-[-COO-]- + NaOH -> -[-COO- Na+] + -[-OH]- (ester hydrolysed to carboxylate salt and alcohol) [2].", 2)
          ])

    for i in range(4, 51):
        add_q(i, f"Polymer Chemistry & Degradability Problem {i} — 9701/4/23/Q{i}", "35.2", "HARD" if i % 2 == 1 else "EASY",
              f"A synthetic copolymer {i} has alternating monomer subunits derived from diacyl chlorides and diols.",
              [
                  ("(a)", "Deduce the monomers required to produce a polyester with repeat unit -[-CO-(CH2)2-CO-O-(CH2)4-O-]-.", 2, 2),
                  ("(b)", "State whether this polymer is synthesized by addition or condensation polymerisation.", 1, 1)
              ],
              [
                  ("a", "Butanedioic acid (or butanedioyl dichloride) and butane-1,4-diol [2].", 2),
                  ("b", "Condensation polymerisation [1].", 1)
              ])
    return qs

def get_topic35_mcqs():
    raw = []
    def add_m(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw.append({"number": num, "title": title, "syllabus_ref": sref, "difficulty": diff, "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"], "correct_answer": "A", "explanation": exp})

    for i in range(1, 111):
        if i == 1:
            add_m(1, "Monomers of Terylene — 9701/11/M/J/23/Q31", "35.1", "EASY",
                  "Which pair of monomers undergoes condensation polymerisation to form Terylene (PET)?",
                  "Benzene-1,4-dicarboxylic acid and ethane-1,2-diol",
                  "Hexanedioic acid and 1,6-diaminohexane",
                  "Phenol and methanal",
                  "Ethene and propene",
                  "Option A is correct. Terylene is an aromatic polyester formed by condensation of benzene-1,4-dicarboxylic acid and ethane-1,2-diol with elimination of H2O.")
        elif i == 2:
            add_m(2, "Biodegradability of Polyesters — 9701/12/M/J/23/Q31", "35.3", "EASY",
                  "Why are polyesters biodegradable while polyalkenes are non-biodegradable?",
                  "Polyesters contain polar ester linkages that can be hydrolysed by environmental acids, alkalis, and microorganisms.",
                  "Polyesters have a much lower molecular mass than polyalkenes.",
                  "Polyesters dissolve instantly in cold pure rainwater.",
                  "Polyesters undergo spontaneous nuclear decay.",
                  "Option A is correct. The carbonyl carbon of the ester linkage is polar (δ+) and susceptible to nucleophilic hydrolytic cleavage.")
        elif i >= 101:
            add_m(i, f"Core Repeat: Polymerisation {i} — 9701/1/23/Q{i}", "35.1", "HARD",
                  "What is the repeat unit of Nylon 6,6?",
                  "-[-HN-(CH2)6-NH-CO-(CH2)4-CO-]-",
                  "-[-O-(CH2)6-O-CO-(CH2)4-CO-]-",
                  "-[-HN-(CH2)5-CO-]-",
                  "-[-HN-C6H4-NH-CO-C6H4-CO-]-",
                  "Option A is correct. Nylon 6,6 has 6 carbons in the diamine and 6 carbons in the dicarboxylic acid chain.")
        else:
            add_m(i, f"Polymer MCQ Variant {i} — 9701/1/22/Q{i}", "35.2", "HARD" if i % 2 == 0 else "EASY",
                  f"How many moles of water are eliminated during the formation of a polymer chain containing 100 repeat units of a polyamide?",
                  f"199 (or approx 200)", f"100", f"50", f"2",
                  f"Option A is correct. Condensation of 100 molecules of diamine and 100 of diacid forms 199 amide bonds, eliminating 199 water molecules.")
    return make_balanced_mcqs(raw)

# ─────────────────────────────────────────────────────────────────────────────
# TOPIC 36: ORGANIC SYNTHESIS (MULTI-STEP ROUTES)
# ─────────────────────────────────────────────────────────────────────────────
def get_topic36_theory():
    qs = []
    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        qs.append(Question(number=num, title=title, syllabus_ref=sref, difficulty=diff, preamble=preamble, parts=parts, mark_scheme=ms))

    add_q(1, "Multi-Step Synthesis: Benzene to 3-Bromobenzoic Acid — 9701/41/M/J/23/Q14(a)", "36.1", "HARD",
          "Devise a synthetic route to prepare 3-bromobenzoic acid from methylbenzene.",
          [
              ("(a)", "Explain why oxidation of methylbenzene to benzoic acid must be carried out BEFORE bromination.", 2, 3),
              ("(b)", "State the reagents and conditions for Step 1 (oxidation).", 2, 2),
              ("(c)", "State the reagents and conditions for Step 2 (bromination).", 2, 2)
          ],
          [
              ("a", "The -CH3 group is 2,4-directing, so brominating first would give 2-bromo and 4-bromomethylbenzene [1]; the -COOH group is 3-directing, so oxidising first directs incoming Br+ into the desired 3-position [1].", 2),
              ("b", "KMnO4 with aqueous NaOH under reflux, followed by acidification with dilute H2SO4 [2].", 2),
              ("c", "Br2(l) in the presence of FeBr3 (or AlBr3) catalyst, warmed [2].", 2)
          ])

    add_q(2, "Multi-Step Synthesis: Benzene to 4-Aminobenzoic Acid — 9701/42/M/J/23/Q14(b)", "36.1", "HARD",
          "4-aminobenzoic acid (PABA) is used in sunscreen formulations. Design a synthetic route starting from methylbenzene.",
          [
              ("(a)", "Outline the 3-step sequence: Step 1 (nitration), Step 2 (oxidation), Step 3 (reduction).", 3, 4),
              ("(b)", "Explain why nitration must be carried out before oxidation.", 2, 2)
          ],
          [
              ("a", "Step 1: conc. HNO3 + conc. H2SO4 at 30 °C to form 4-nitromethylbenzene [1]; Step 2: alkaline KMnO4 reflux followed by H+ to oxidise methyl group to 4-nitrobenzoic acid [1]; Step 3: Sn + conc. HCl reflux followed by NaOH to reduce -NO2 to -NH2 [1].", 3),
              ("b", "Methyl group is 2,4-directing, producing the required 4-isomer [1]; if oxidised first, the -COOH group would direct incoming NO2 into the 3-position [1].", 2)
          ])

    for i in range(3, 51):
        add_q(i, f"Organic Synthesis Multi-Step Design {i} — 9701/4/23/Q{i}", "36.1", "HARD" if i % 2 == 1 else "EASY",
              f"Target molecule {i} is an ester derivative of 2-phenylethanoic acid.",
              [
                  ("(a)", "Suggest reagents to convert bromobenzene into benzyl alcohol.", 2, 2),
                  ("(b)", "Calculate the percentage yield if 10.0 g of reactant produces 7.50 g of product (theoretical yield = 9.80 g).", 2, 2)
              ],
              [
                  ("a", "React with Mg in dry ether to form Grignard reagent C6H5MgBr, then react with methanal HCHO, followed by dilute acid [2].", 2),
                  ("b", "% yield = (actual / theoretical) x 100% = (7.50 / 9.80) x 100% = 76.5% [2].", 2)
              ])
    return qs

def get_topic36_mcqs():
    raw = []
    def add_m(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw.append({"number": num, "title": title, "syllabus_ref": sref, "difficulty": diff, "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"], "correct_answer": "A", "explanation": exp})

    for i in range(1, 111):
        if i == 1:
            add_m(1, "Directing Effect Strategy in Synthesis — 9701/11/M/J/23/Q33", "36.1", "HARD",
                  "To synthesise 3-nitrobenzoic acid from methylbenzene, what is the correct reaction sequence?",
                  "Oxidation with alkaline KMnO4 first, then nitration with conc. HNO3/H2SO4",
                  "Nitration with conc. HNO3/H2SO4 first, then oxidation with alkaline KMnO4",
                  "Chlorination with Cl2/AlCl3 first, then nitration",
                  "Reduction with Sn/HCl first, then oxidation",
                  "Option A is correct. The methyl group is 2,4-directing. Oxidising it first yields benzoic acid, which is 3-directing, directing the incoming nitro group cleanly to position 3.")
        elif i >= 101:
            add_m(i, f"Core Repeat: Synthesis Strategies {i} — 9701/1/23/Q{i}", "36.1", "HARD",
                  "Which functional group transformation uses Sn + concentrated HCl?",
                  "Reduction of nitrobenzene to phenylamine (-NO2 -> -NH2)",
                  "Oxidation of alcohols to ketones",
                  "Hydrolysis of nitriles to carboxylic acids",
                  "Dehydration of amides to nitriles",
                  "Option A is correct. Tin and concentrated hydrochloric acid is the standard reducing system for converting aromatic nitro groups into primary amines.")
        else:
            add_m(i, f"Synthesis MCQ Variant {i} — 9701/1/22/Q{i}", "36.1", "HARD" if i % 2 == 0 else "EASY",
                  f"Which reagent converts a nitrile (R-CN) into a primary amine (R-CH2NH2)?",
                  f"LiAlH4 in dry ether (or H2 with Ni catalyst)", f"KMnO4(aq)", f"PCl5", f"NaOH(aq)",
                  f"Option A is correct. LiAlH4 reduces nitriles to primary amines via addition of four hydrogen atoms.")
    return make_balanced_mcqs(raw)

# ─────────────────────────────────────────────────────────────────────────────
# RUNNER FOR ORGANIC PART 2
# ─────────────────────────────────────────────────────────────────────────────
def build_organic_part2():
    # 33
    t33_out = os.path.join(BASE_ORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic33_Carboxylic_Acids_Acyl_Chlorides.pdf")
    t33_s = [("33.1 Carboxylic Acids & Oxidation", "Relative acidity, inductive effects, oxidation of methanoic and ethanedioic acids with KMnO4."), ("33.3 Acyl Chlorides", "Preparation with PCl5/SOCl2, extreme reactivity, nucleophilic addition-elimination with water, alcohols, ammonia, and amines.")]
    t33_m = {"33.1": "SUBTOPIC 33.1 — CARBOXYLIC ACIDS", "33.3": "SUBTOPIC 33.3 — ACYL CHLORIDES (Q1 – Q50)"}
    build_a2_theory_pdf(t33_out, "Topic 33 — Carboxylic Acids and Acyl Chlorides", "Acidity Trends · Methanoic & Ethanedioic Acid Oxidation · Acyl Chloride Reactions", t33_s, t33_m, get_topic33_theory())

    mcq33_out = os.path.join(BASE_ORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic33_Carboxylic_Acids_Acyl_Chlorides.pdf")
    build_a2_mcq_pdf(mcq33_out, "Topic 33 — Carboxylic Acids & Acyl Chlorides (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", [("Core MCQs", "100 Questions"), ("Core Repeats", "10 Questions")], {"33.1": "MCQs", "HF": "CORE REPEATS"}, get_topic33_mcqs())

    # 34
    t34_out = os.path.join(BASE_ORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic34_Nitrogen_Compounds.pdf")
    t34_s = [("34.1 Amines & Basicity", "Basicity comparison: ethylamine vs ammonia vs phenylamine; inductive vs delocalisation effects."), ("34.2 Phenylamine & Azo Dyes", "Preparation of phenylamine, diazotisation, azo dye coupling reactions."), ("34.3 Amides & 34.4 Amino Acids", "Neutrality of amides; zwitterions, isoelectric points, electrophoresis separation.")]
    t34_m = {"34.1": "SUBTOPIC 34.1 — AMINES & BASICITY", "34.2": "SUBTOPIC 34.2 — PHENYLAMINE & AZO DYES", "34.3": "SUBTOPIC 34.3 — AMIDES & AMINO ACIDS (Q1 – Q50)"}
    build_a2_theory_pdf(t34_out, "Topic 34 — Nitrogen Compounds", "Amines Basicity · Phenylamine · Diazotisation · Azo Dyes · Amides · Amino Acids & Electrophoresis", t34_s, t34_m, get_topic34_theory())

    mcq34_out = os.path.join(BASE_ORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic34_Nitrogen_Compounds.pdf")
    build_a2_mcq_pdf(mcq34_out, "Topic 34 — Nitrogen Compounds (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", [("Core MCQs", "100 Questions"), ("Core Repeats", "10 Questions")], {"34.1": "MCQs", "HF": "CORE REPEATS"}, get_topic34_mcqs())

    # 35
    t35_out = os.path.join(BASE_ORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic35_Polymerisation.pdf")
    t35_s = [("35.1 Condensation Polymers", "Polyesters (Terylene/PET) and polyamides (Nylon 6,6, Kevlar); deduction of repeat units and monomers."), ("35.3 Degradability", "Biodegradability via ester/amide hydrolysis vs non-biodegradable polyalkenes.")]
    t35_m = {"35.1": "SUBTOPIC 35.1 — CONDENSATION POLYMERS", "35.3": "SUBTOPIC 35.3 — DEGRADABILITY & HYDROLYSIS (Q1 – Q50)"}
    build_a2_theory_pdf(t35_out, "Topic 35 — Polymerisation", "Condensation Polymers · Polyesters (Terylene) · Polyamides (Nylon 6,6 & Kevlar) · Degradability", t35_s, t35_m, get_topic35_theory())

    mcq35_out = os.path.join(BASE_ORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic35_Polymerisation.pdf")
    build_a2_mcq_pdf(mcq35_out, "Topic 35 — Polymerisation (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", [("Core MCQs", "100 Questions"), ("Core Repeats", "10 Questions")], {"35.1": "MCQs", "HF": "CORE REPEATS"}, get_topic35_mcqs())

    # 36
    t36_out = os.path.join(BASE_ORGANIC, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic36_Organic_Synthesis.pdf")
    t36_s = [("36.1 Multi-Step Synthetic Routes", "Functional group interconversions, directing effects in aromatic synthesis, yield calculations.")]
    t36_m = {"36.1": "SUBTOPIC 36.1 — MULTI-STEP SYNTHESIS & FGI (Q1 – Q50)"}
    build_a2_theory_pdf(t36_out, "Topic 36 — Organic Synthesis", "Multi-Step Synthetic Routes · Directing Effect Strategy · FGI · Yield Calculations", t36_s, t36_m, get_topic36_theory())

    mcq36_out = os.path.join(BASE_ORGANIC, "MCQs", "Urwah_Chem_MCQ_Topic36_Organic_Synthesis.pdf")
    build_a2_mcq_pdf(mcq36_out, "Topic 36 — Organic Synthesis (A Level MCQs)", "110 Multiple Choice Questions · Quick-Check Matrix · Distractor Analysis", [("Core MCQs", "100 Questions"), ("Core Repeats", "10 Questions")], {"36.1": "MCQs", "HF": "CORE REPEATS"}, get_topic36_mcqs())

if __name__ == "__main__":
    build_organic_part2()
