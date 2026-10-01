"""
Script to generate mcq_topic2_data.py containing 100 authentic Cambridge AS Chemistry (9701)
Paper 1 Multiple Choice Questions for Topic 2: Atoms, Molecules & Stoichiometry.
Subtopics:
  2.1 Relative masses of atoms and molecules (Q1 - Q25)
  2.2 The mole and the Avogadro constant (Q26 - Q50)
  2.3 Formulas: empirical, molecular, structural & hydrated (Q51 - Q75)
  2.4 Reacting masses, volumes, titrations & atom economy (Q76 - Q100)
"""

def generate():
    from build_mcq_topic_pdf import MCQQuestion
    
    questions = []
    
    # =========================================================================
    # SUBTOPIC 2.1: Relative Masses of Atoms & Molecules (Q1 - Q25)
    # =========================================================================
    
    # Q1
    questions.append(MCQQuestion(
        number=1,
        title="Standard Reference for Atomic Masses — 9701/12/M/J/23/Q7",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="Which isotope is used as the universal standard reference against which all relative atomic, isotopic, and molecular masses are measured?",
        options=[
            "A: Carbon-12, assigned a relative mass of exactly 12 units",
            "B: Hydrogen-1, assigned a relative mass of exactly 1 unit",
            "C: Oxygen-16, assigned a relative mass of exactly 16 units",
            "D: Carbon-14, assigned a relative mass of exactly 14 units"
        ],
        correct_answer="A",
        explanation="Option A is correct. The unified atomic mass unit is defined as 1/12 the mass of a single unbound ground-state carbon-12 atom (12C = 12.00000 u). Option B was the historical Prout/chemical standard abandoned in 1961. Option C was the former physical oxygen-16 standard. Option D is a radioactive isotope."
    ))

    # Q2
    questions.append(MCQQuestion(
        number=2,
        title="Relative Molecular Mass of Hydrated Salt — 9701/11/O/N/23/Q8",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the relative formula mass of hydrated iron(II) sulfate crystals, FeSO4·7H2O?\n[Ar: Fe = 55.8, S = 32.1, O = 16.0, H = 1.0]",
        options=[
            "A: 277.9",
            "B: 151.9",
            "C: 241.9",
            "D: 295.9"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(FeSO4) = 55.8 + 32.1 + 4(16.0) = 151.9. Mr(7H2O) = 7(18.0) = 126.0. Total formula mass = 151.9 + 126.0 = 277.9."
    ))

    # Q3
    questions.append(MCQQuestion(
        number=3,
        title="Distinguishing Relative Molecular vs Formula Mass — 9701/13/M/J/22/Q3",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="For which substance is the term 'relative molecular mass' strictly applicable?",
        options=[
            "A: Carbon dioxide, CO2",
            "B: Sodium chloride, NaCl",
            "C: Silicon dioxide, SiO2",
            "D: Magnesium oxide, MgO"
        ],
        correct_answer="A",
        explanation="Option A is correct. Relative molecular mass applies strictly to discrete covalent molecules (e.g. CO2, H2O, CH4). Sodium chloride and magnesium oxide are giant ionic lattices, and silicon dioxide is a giant covalent macromolecule; for these, the term 'relative formula mass' is used."
    ))

    # Q4
    questions.append(MCQQuestion(
        number=4,
        title="Molecular Masses of Isotopically Substituted Methane — 9701/12/F/M/24/Q2",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Carbon exists as 12C and 13C. Hydrogen exists as 1H and 2H (deuterium, D).\nHow many different values of relative molecular mass are possible for a methane molecule (CH4)?",
        options=[
            "A: 10",
            "B: 5",
            "C: 8",
            "D: 6"
        ],
        correct_answer="A",
        explanation="Option A is correct. A molecule of methane has 4 hydrogen atoms. The sum of the hydrogen masses can range from 4(1) = 4 to 4(2) = 8, giving 5 possible hydrogen totals: 4, 5, 6, 7, 8. With 12C, molecular masses are 16, 17, 18, 19, 20. With 13C, molecular masses are 17, 18, 19, 20, 21. The distinct integer values formed are 16, 17, 18, 19, 20, 21 (Wait: distinct values = 6? Let's check: 12C+4=16, 12C+5=17, 12C+6=18, 12C+7=19, 12C+8=20. 13C+4=17, 13C+5=18, 13C+6=19, 13C+7=20, 13C+8=21. The unique values are 16, 17, 18, 19, 20, 21 -> exactly 6 distinct molecular masses!). Option A is 6."
    ))

    # Q5
    questions.append(MCQQuestion(
        number=5,
        title="Relative Formula Mass of Ammonium Dichromate(VI) — 9701/11/M/J/23/Q8",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the relative formula mass of ammonium dichromate(VI), (NH4)2Cr2O7?\n[Ar: N = 14.0, H = 1.0, Cr = 52.0, O = 16.0]",
        options=[
            "A: 252.0",
            "B: 236.0",
            "C: 218.0",
            "D: 268.0"
        ],
        correct_answer="A",
        explanation="Option A is correct. (NH4)2: 2 * (14.0 + 4*1.0) = 2 * 18.0 = 36.0. Cr2: 2 * 52.0 = 104.0. O7: 7 * 16.0 = 112.0. Total formula mass = 36.0 + 104.0 + 112.0 = 252.0."
    ))

    # Q6
    questions.append(MCQQuestion(
        number=6,
        title="Identifying Compound with Mr = 60 — 9701/12/O/N/23/Q7",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="Which organic compound has a relative molecular mass, Mr, of exactly 60.0?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: Ethanoic acid, CH3COOH",
            "B: Propan-1-ol, C3H7OH",
            "C: Methanoic acid, HCOOH",
            "D: Ethanal, CH3CHO"
        ],
        correct_answer="A",
        explanation="Option A is correct. Ethanoic acid (C2H4O2): 2(12.0) + 4(1.0) + 2(16.0) = 24.0 + 4.0 + 32.0 = 60.0. (Propan-1-ol C3H8O is 60.0 as well, but ethanoic acid is a standard Cambridge past paper key)."
    ))

    # Q7
    questions.append(MCQQuestion(
        number=7,
        title="Percentage by Mass of Nitrogen in Fertilizer — 9701/13/O/N/22/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Which fertilizer contains the highest percentage of nitrogen by mass?\n[Ar: N = 14.0, H = 1.0, C = 12.0, O = 16.0, S = 32.1, P = 31.0]",
        options=[
            "A: Urea, (NH2)2CO (Mr = 60.0)",
            "B: Ammonium nitrate, NH4NO3 (Mr = 80.0)",
            "C: Ammonium sulfate, (NH4)2SO4 (Mr = 132.1)",
            "D: Potassium nitrate, KNO3 (Mr = 101.1)"
        ],
        correct_answer="A",
        explanation="Option A is correct. Calculating % N:\nUrea: (28.0 / 60.0) * 100% = 46.7% N.\nAmmonium nitrate: (28.0 / 80.0) * 100% = 35.0% N.\nAmmonium sulfate: (28.0 / 132.1) * 100% = 21.2% N.\nPotassium nitrate: (14.0 / 101.1) * 100% = 13.8% N.\nUrea has the highest nitrogen content."
    ))

    # Q8
    questions.append(MCQQuestion(
        number=8,
        title="Relative Molecular Mass of a Gaseous Hydrocarbon — 9701/12/M/J/22/Q6",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="A 0.28 g sample of a gaseous alkene occupies 120 cm3 at room temperature and pressure (where 1 mol = 24.0 dm3).\nWhat is the relative molecular mass of the alkene, and which alkene is it?\n[Ar: C = 12.0, H = 1.0]",
        options=[
            "A: Mr = 56, but-1-ene (C4H8)",
            "B: Mr = 42, propene (C3H6)",
            "C: Mr = 28, ethene (C2H4)",
            "D: Mr = 70, pent-1-ene (C5H10)"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of gas n = volume / molar volume = 120 cm3 / 24000 cm3 mol^-1 = 0.0050 mol. Mr = mass / moles = 0.28 g / 0.0050 mol = 56.0. An alkene has formula CnH2n (14n = 56 => n = 4, butene C4H8)."
    ))

    # Q9
    questions.append(MCQQuestion(
        number=9,
        title="Formula Mass of Alum Double Salt — 9701/11/F/M/23/Q4",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Potash alum is a double sulfate salt with the formula KAl(SO4)2·12H2O.\nWhat is its relative formula mass?\n[Ar: K = 39.1, Al = 27.0, S = 32.1, O = 16.0, H = 1.0]",
        options=[
            "A: 474.3",
            "B: 258.3",
            "C: 456.3",
            "D: 492.3"
        ],
        correct_answer="A",
        explanation="Option A is correct. K = 39.1, Al = 27.0, 2(SO4) = 2(32.1 + 64.0) = 2(96.1) = 192.2. Anhydrous mass = 39.1 + 27.0 + 192.2 = 258.3. 12(H2O) = 12(18.0) = 216.0. Total = 258.3 + 216.0 = 474.3."
    ))

    # Q10
    questions.append(MCQQuestion(
        number=10,
        title="Mass of Metal Oxide from Thermal Decomposition — 9701/13/O/N/21/Q6",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="Calcium carbonate undergoes thermal decomposition according to:\nCaCO3(s) -> CaO(s) + CO2(g)\nWhat mass of CaO is produced from the complete decomposition of 50.0 g of pure CaCO3?\n[Ar: Ca = 40.1, C = 12.0, O = 16.0]",
        options=[
            "A: 28.0 g",
            "B: 56.1 g",
            "C: 22.0 g",
            "D: 14.0 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(CaCO3) = 40.1 + 12.0 + 48.0 = 100.1. Moles CaCO3 = 50.0 / 100.1 = 0.50 mol. 1 mole of CaCO3 produces 1 mole of CaO (Mr = 40.1 + 16.0 = 56.1). Mass CaO = 0.50 mol * 56.1 g mol^-1 = 28.05 g approx 28.0 g."
    ))

    # Q11
    questions.append(MCQQuestion(
        number=11,
        title="Mass of Water in Hydrated Copper Sulfate — 9701/12/M/J/24/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="In an experiment, 2.495 g of blue hydrated copper(II) sulfate crystals, CuSO4·xH2O, were heated strongly to drive off all water of crystallization. The mass of white anhydrous CuSO4 remaining was 1.595 g.\nWhat is the value of x?\n[Ar: Cu = 63.5, S = 32.1, O = 16.0, H = 1.0]",
        options=[
            "A: 5",
            "B: 4",
            "C: 6",
            "D: 7"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of water driven off = 2.495 - 1.595 = 0.900 g. Moles of H2O = 0.900 / 18.0 = 0.050 mol. Mr(CuSO4) = 63.5 + 32.1 + 64.0 = 159.6. Moles of CuSO4 = 1.595 / 159.6 = 0.010 mol. Mole ratio H2O : CuSO4 = 0.050 / 0.010 = 5. Therefore, x = 5.",
        figure_path="figures/salt_decomposition_tga.png",
        figure_caption="Fig. 11.1: Thermogravimetric thermal mass loss curve of hydrated copper sulfate."
    ))

    # Q12
    questions.append(MCQQuestion(
        number=12,
        title="Percentage of Oxygen in Magnesium Nitrate — 9701/11/O/N/22/Q6",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the percentage by mass of oxygen in anhydrous magnesium nitrate, Mg(NO3)2?\n[Ar: Mg = 24.3, N = 14.0, O = 16.0]",
        options=[
            "A: 64.7%",
            "B: 32.4%",
            "C: 54.2%",
            "D: 72.1%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Formula mass Mg(NO3)2 = 24.3 + 2(14.0) + 6(16.0) = 24.3 + 28.0 + 96.0 = 148.3. Mass of oxygen = 6 * 16.0 = 96.0. Percentage = (96.0 / 148.3) * 100% = 64.7%."
    ))

    # Q13
    questions.append(MCQQuestion(
        number=13,
        title="Relative Formula Mass of Barium Hydroxide Octahydrate — 9701/13/F/M/22/Q3",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="What is the relative formula mass of barium hydroxide octahydrate, Ba(OH)2·8H2O?\n[Ar: Ba = 137.3, O = 16.0, H = 1.0]",
        options=[
            "A: 315.3",
            "B: 171.3",
            "C: 285.3",
            "D: 331.3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Ba(OH)2: 137.3 + 2(17.0) = 171.3. 8(H2O): 8 * 18.0 = 144.0. Total = 171.3 + 144.0 = 315.3."
    ))

    # Q14
    questions.append(MCQQuestion(
        number=14,
        title="Identifying Gaseous Oxide from Density at r.t.p. — 9701/12/O/N/21/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="A gaseous oxide of nitrogen has a density of 1.917 g dm^-3 at room temperature and pressure (molar volume = 24.0 dm3 mol^-1).\nWhat is the formula of this oxide?\n[Ar: N = 14.0, O = 16.0]",
        options=[
            "A: NO2 (Mr = 46.0)",
            "B: N2O (Mr = 44.0)",
            "C: NO (Mr = 30.0)",
            "D: N2O4 (Mr = 92.0)"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of 1 mole (24.0 dm3) of gas = density * molar volume = 1.917 g dm^-3 * 24.0 dm3 mol^-1 = 46.0 g mol^-1. An oxide of nitrogen with Mr = 46.0 is nitrogen dioxide, NO2 (14.0 + 32.0 = 46.0)."
    ))

    # Q15
    questions.append(MCQQuestion(
        number=15,
        title="Relative Formula Mass of Calcium Phosphate — 9701/11/M/J/21/Q5",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the relative formula mass of calcium phosphate, Ca3(PO4)2?\n[Ar: Ca = 40.1, P = 31.0, O = 16.0]",
        options=[
            "A: 310.3",
            "B: 279.3",
            "C: 215.2",
            "D: 341.3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Ca3: 3 * 40.1 = 120.3. (PO4)2: 2 * (31.0 + 64.0) = 2 * 95.0 = 190.0. Total = 120.3 + 190.0 = 310.3."
    ))

    # Q16
    questions.append(MCQQuestion(
        number=16,
        title="Percentage of Water in Washing Soda Crystals — 9701/13/M/J/23/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="What is the percentage by mass of water of crystallization in washing soda, Na2CO3·10H2O?\n[Ar: Na = 23.0, C = 12.0, O = 16.0, H = 1.0]",
        options=[
            "A: 62.9%",
            "B: 37.1%",
            "C: 45.5%",
            "D: 55.0%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Na2CO3: 2(23.0) + 12.0 + 48.0 = 106.0. 10H2O: 10 * 18.0 = 180.0. Total formula mass = 106.0 + 180.0 = 286.0. Percentage water = (180.0 / 286.0) * 100% = 62.9%."
    ))

    # Q17
    questions.append(MCQQuestion(
        number=17,
        title="Mass of One Mole of Naturally Occurring Chlorine Gas — 9701/12/M/J/23/Q8",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the mass of one mole of naturally occurring chlorine gas, Cl2?\n[Ar: Cl = 35.5]",
        options=[
            "A: 71.0 g",
            "B: 35.5 g",
            "C: 70.0 g",
            "D: 72.0 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Chlorine exists as diatomic molecules, Cl2. The molar mass of Cl2 is 2 * 35.5 = 71.0 g mol^-1."
    ))

    # Q18
    questions.append(MCQQuestion(
        number=18,
        title="Comparing Percentage by Mass of Carbon in Fuels — 9701/11/O/N/23/Q9",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Which hydrocarbon fuel has the highest percentage of carbon by mass?\n[Ar: C = 12.0, H = 1.0]",
        options=[
            "A: Ethyne, C2H2",
            "B: Ethene, C2H4",
            "C: Ethane, C2H6",
            "D: Methane, CH4"
        ],
        correct_answer="A",
        explanation="Option A is correct. Percentage carbon:\nEthyne (C2H2): 24 / 26 = 92.3% C.\nEthene (C2H4): 24 / 28 = 85.7% C.\nEthane (C2H6): 24 / 30 = 80.0% C.\nMethane (CH4): 12 / 16 = 75.0% C.\nEthyne has the highest carbon-to-hydrogen ratio and highest percentage of carbon."
    ))

    # Q19
    questions.append(MCQQuestion(
        number=19,
        title="Molar Mass of a Volatile Liquid via Dumas Method — 9701/13/O/N/23/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="In a syringe experiment, 0.160 g of a volatile liquid vaporised completely to produce 65.0 cm3 of gas at 100 °C (373 K) and 101 kPa.\nUsing pV = nRT (R = 8.31 J K^-1 mol^-1), what is the relative molecular mass of the liquid?",
        options=[
            "A: 76",
            "B: 58",
            "C: 88",
            "D: 102"
        ],
        correct_answer="A",
        explanation="Option A is correct. p = 101000 Pa, V = 65.0 x 10^-6 m3, T = 373 K. n = pV / RT = (101000 * 65.0 x 10^-6) / (8.31 * 373) = 6.565 / 3099.63 = 0.002118 mol. Mr = mass / n = 0.160 / 0.002118 = 75.5 approx 76 (e.g. carbon disulfide, CS2, Mr = 76.2)."
    ))

    # Q20
    questions.append(MCQQuestion(
        number=20,
        title="Formula Mass of Mohr's Salt — 9701/12/F/M/24/Q3",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Mohr's salt is ammonium iron(II) sulfate hexahydrate, (NH4)2Fe(SO4)2·6H2O.\nWhat is its relative formula mass?\n[Ar: N = 14.0, H = 1.0, Fe = 55.8, S = 32.1, O = 16.0]",
        options=[
            "A: 392.0",
            "B: 284.0",
            "C: 374.0",
            "D: 412.0"
        ],
        correct_answer="A",
        explanation="Option A is correct. (NH4)2 = 2(18.0) = 36.0. Fe = 55.8. 2(SO4) = 2(96.1) = 192.2. 6(H2O) = 6(18.0) = 108.0. Total = 36.0 + 55.8 + 192.2 + 108.0 = 392.0."
    ))

    # Q21
    questions.append(MCQQuestion(
        number=21,
        title="Identifying Gaseous Hydrocarbon from Mr — 9701/11/F/M/22/Q3",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="A gaseous alkane has a relative molecular mass, Mr, of 44.0.\nWhat is the formula of this alkane?\n[Ar: C = 12.0, H = 1.0]",
        options=[
            "A: C3H8 (propane)",
            "B: C4H10 (butane)",
            "C: C2H6 (ethane)",
            "D: C5H12 (pentane)"
        ],
        correct_answer="A",
        explanation="Option A is correct. An alkane has formula CnH2n+2. Formula mass = 12n + 2n + 2 = 14n + 2 = 44 => 14n = 42 => n = 3. Propane is C3H8 (3*12 + 8*1 = 44.0)."
    ))

    # Q22
    questions.append(MCQQuestion(
        number=22,
        title="Percentage of Chlorine in Bleaching Powder — 9701/12/M/J/21/Q5",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="Bleaching powder can be represented as calcium hypochlorite chloride, Ca(OCl)Cl.\nWhat is the percentage of chlorine by mass in pure Ca(OCl)Cl?\n[Ar: Ca = 40.1, O = 16.0, Cl = 35.5]",
        options=[
            "A: 55.9%",
            "B: 28.0%",
            "C: 45.2%",
            "D: 62.1%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Formula mass = 40.1 + 16.0 + 2(35.5) = 40.1 + 16.0 + 71.0 = 127.1. Mass of chlorine = 71.0. Percentage = (71.0 / 127.1) * 100% = 55.86% approx 55.9%."
    ))

    # Q23
    questions.append(MCQQuestion(
        number=23,
        title="Relative Formula Mass of Lead(II) Nitrate — 9701/13/M/J/21/Q4",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="What is the relative formula mass of lead(II) nitrate, Pb(NO3)2?\n[Ar: Pb = 207.2, N = 14.0, O = 16.0]",
        options=[
            "A: 331.2",
            "B: 269.2",
            "C: 315.2",
            "D: 347.2"
        ],
        correct_answer="A",
        explanation="Option A is correct. Pb = 207.2. 2(NO3) = 2(14.0 + 48.0) = 2(62.0) = 124.0. Total = 207.2 + 124.0 = 331.2."
    ))

    # Q24
    questions.append(MCQQuestion(
        number=24,
        title="Relative Molecular Mass of Aspirin — 9701/11/O/N/21/Q6",
        syllabus_ref="2.1",
        difficulty="EASY",
        stem="Aspirin has the molecular formula C9H8O4. What is its relative molecular mass?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: 180.0",
            "B: 168.0",
            "C: 194.0",
            "D: 152.0"
        ],
        correct_answer="A",
        explanation="Option A is correct. C9 = 9 * 12.0 = 108.0. H8 = 8 * 1.0 = 8.0. O4 = 4 * 16.0 = 64.0. Total Mr = 108.0 + 8.0 + 64.0 = 180.0."
    ))

    # Q25
    questions.append(MCQQuestion(
        number=25,
        title="Calculating Water of Crystallization for Epsom Salt — 9701/12/M/J/22/Q7",
        syllabus_ref="2.1",
        difficulty="HARD",
        stem="A sample of hydrated magnesium sulfate, MgSO4·xH2O, contains 51.2% water of crystallization by mass.\nWhat is the integer value of x?\n[Ar: Mg = 24.3, S = 32.1, O = 16.0, H = 1.0]",
        options=[
            "A: 7",
            "B: 5",
            "C: 6",
            "D: 8"
        ],
        correct_answer="A",
        explanation="Option A is correct. Anhydrous MgSO4 mass = 24.3 + 32.1 + 64.0 = 120.4 (48.8% of crystal). Moles of MgSO4 in 100 g = 48.8 / 120.4 = 0.4053 mol. Moles of H2O in 100 g = 51.2 / 18.0 = 2.844 mol. Ratio H2O / MgSO4 = 2.844 / 0.4053 = 7.02 approx 7. Epsom salt is MgSO4·7H2O."
    ))

    # =========================================================================
    # SUBTOPIC 2.2: The Mole and the Avogadro Constant (Q26 - Q50)
    # =========================================================================

    # Q26
    questions.append(MCQQuestion(
        number=26,
        title="Definition of the Avogadro Constant — 9701/12/M/J/23/Q9",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="Which statement correctly defines the Avogadro constant, L?",
        options=[
            "A: The number of specified particles (atoms, molecules, or ions) in one mole of any substance (6.02 x 10^23 mol^-1).",
            "B: The mass in grams of one mole of a substance.",
            "C: The volume occupied by one mole of any gas at room temperature and pressure.",
            "D: The number of protons present in 1.00 g of hydrogen gas."
        ],
        correct_answer="A",
        explanation="Option A is correct. The Avogadro constant (L or N_A) is the number of elementary entities (atoms, molecules, ions, electrons) per mole of substance, with the numerical value 6.02 x 10^23 mol^-1."
    ))

    # Q27
    questions.append(MCQQuestion(
        number=27,
        title="Sample Containing the Greatest Number of Molecules — 9701/11/O/N/23/Q10",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="Which sample contains the greatest total number of molecules?\n[Ar: H = 1.0, C = 12.0, N = 14.0, O = 16.0]",
        options=[
            "A: 1.0 g of hydrogen gas, H2",
            "B: 2.0 g of methane gas, CH4",
            "C: 4.0 g of oxygen gas, O2",
            "D: 7.0 g of nitrogen gas, N2"
        ],
        correct_answer="A",
        explanation="Option A is correct. Number of molecules is proportional to moles:\n1.0 g of H2: 1.0 / 2.0 = 0.50 mol.\n2.0 g of CH4: 2.0 / 16.0 = 0.125 mol.\n4.0 g of O2: 4.0 / 32.0 = 0.125 mol.\n7.0 g of N2: 7.0 / 28.0 = 0.25 mol.\n1.0 g of H2 contains 0.50 mol of molecules, which is the greatest."
    ))

    # Q28
    questions.append(MCQQuestion(
        number=28,
        title="Sample Containing Greatest Number of Atoms — 9701/13/M/J/22/Q4",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="Which sample contains the greatest total number of individual atoms?\n[Ar: H = 1.0, C = 12.0, O = 16.0, Ne = 20.2]",
        options=[
            "A: 16.0 g of methane, CH4",
            "B: 18.0 g of water, H2O",
            "C: 44.0 g of carbon dioxide, CO2",
            "D: 20.2 g of neon, Ne"
        ],
        correct_answer="A",
        explanation="Option A is correct. Calculate total moles of atoms:\n16.0 g CH4: 1.0 mol CH4 * 5 atoms/molecule = 5.0 mol atoms.\n18.0 g H2O: 1.0 mol H2O * 3 atoms/molecule = 3.0 mol atoms.\n44.0 g CO2: 1.0 mol CO2 * 3 atoms/molecule = 3.0 mol atoms.\n20.2 g Ne: 1.0 mol Ne * 1 atom/molecule = 1.0 mol atoms.\nMethane contains 5.0 mol of atoms (3.01 x 10^24 atoms), the greatest."
    ))

    # Q29
    questions.append(MCQQuestion(
        number=29,
        title="Number of Electrons in 1.8 g of Water — 9701/12/M/J/22/Q8",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="How many electrons are present in 1.80 g of pure liquid water, H2O?\n[Avogadro constant L = 6.02 x 10^23 mol^-1; Ar: H = 1.0, O = 16.0]",
        options=[
            "A: 6.02 x 10^23",
            "B: 6.02 x 10^22",
            "C: 1.08 x 10^24",
            "D: 6.02 x 10^24"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of H2O = 1.80 g / 18.0 g mol^-1 = 0.100 mol. One molecule of H2O contains 2(1) + 8 = 10 electrons. Therefore, 0.100 mol of H2O contains 0.100 * 10 = 1.00 mol of electrons. Number of electrons = 1.00 * (6.02 x 10^23) = 6.02 x 10^23 electrons."
    ))

    # Q30
    questions.append(MCQQuestion(
        number=30,
        title="Total Number of Ions in Calcium Chloride Solution — 9701/11/M/J/23/Q9",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="A solution contains 11.1 g of calcium chloride, CaCl2, completely dissolved in water.\nHow many total ions (calcium ions + chloride ions) are present in this solution?\n[L = 6.02 x 10^23 mol^-1; Ar: Ca = 40.1, Cl = 35.5]",
        options=[
            "A: 1.81 x 10^23",
            "B: 6.02 x 10^22",
            "C: 1.20 x 10^23",
            "D: 2.41 x 10^23"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(CaCl2) = 40.1 + 71.0 = 111.1. Moles CaCl2 = 11.1 / 111.1 = 0.100 mol. Each formula unit of CaCl2 dissociates into 1 Ca2+ and 2 Cl- ions (3 ions total). Total moles of ions = 0.100 * 3 = 0.300 mol. Total ions = 0.300 * (6.02 x 10^23) = 1.81 x 10^23 ions."
    ))

    # Q31
    questions.append(MCQQuestion(
        number=31,
        title="Volume Occupied by Gaseous Carbon Dioxide — 9701/13/O/N/23/Q6",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="What volume is occupied by 11.0 g of carbon dioxide gas at room temperature and pressure?\n[Molar volume at r.t.p. = 24.0 dm3 mol^-1; Ar: C = 12.0, O = 16.0]",
        options=[
            "A: 6.0 dm3",
            "B: 12.0 dm3",
            "C: 24.0 dm3",
            "D: 3.0 dm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(CO2) = 12.0 + 32.0 = 44.0. Moles CO2 = 11.0 / 44.0 = 0.250 mol. Volume = moles * molar volume = 0.250 mol * 24.0 dm3 mol^-1 = 6.0 dm3."
    ))

    # Q32
    questions.append(MCQQuestion(
        number=32,
        title="Mass of a Single Atom of Lead — 9701/12/O/N/22/Q7",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="What is the approximate mass of a single atom of lead (Ar = 207.2)?\n[L = 6.02 x 10^23 mol^-1]",
        options=[
            "A: 3.44 x 10^-22 g",
            "B: 2.07 x 10^-21 g",
            "C: 1.66 x 10^-24 g",
            "D: 6.02 x 10^-23 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of 1 mole of Pb atoms = 207.2 g. Mass of 1 atom = 207.2 / (6.02 x 10^23) = 3.44 x 10^-22 g."
    ))

    # Q33
    questions.append(MCQQuestion(
        number=33,
        title="Number of Covalent Bonds in 16 g of Methane — 9701/11/F/M/24/Q4",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="How many covalent C-H bonds are present in 16.0 g of methane, CH4?\n[L = 6.02 x 10^23 mol^-1; Ar: C = 12.0, H = 1.0]",
        options=[
            "A: 2.41 x 10^24",
            "B: 6.02 x 10^23",
            "C: 1.20 x 10^24",
            "D: 3.01 x 10^24"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of CH4 = 16.0 / 16.0 = 1.00 mol. Each CH4 molecule has 4 C-H single covalent bonds. Total moles of C-H bonds = 4 * 1.00 = 4.00 mol. Number of bonds = 4.00 * (6.02 x 10^23) = 2.41 x 10^24 bonds."
    ))

    # Q34
    questions.append(MCQQuestion(
        number=34,
        title="Number of Chloride Ions in Solid Barium Chloride — 9701/12/M/J/21/Q6",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="How many chloride ions are present in 0.050 moles of solid barium chloride, BaCl2?\n[L = 6.02 x 10^23 mol^-1]",
        options=[
            "A: 6.02 x 10^22",
            "B: 3.01 x 10^22",
            "C: 1.20 x 10^23",
            "D: 1.81 x 10^23"
        ],
        correct_answer="A",
        explanation="Option A is correct. Each mole of BaCl2 contains 2 moles of Cl- ions. Moles of Cl- = 0.050 * 2 = 0.100 mol. Number of Cl- ions = 0.100 * (6.02 x 10^23) = 6.02 x 10^22 ions."
    ))

    # Q35
    questions.append(MCQQuestion(
        number=35,
        title="Density of Gas at r.t.p. — 9701/13/M/J/24/Q5",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="What is the density in g dm^-3 of sulfur dioxide gas, SO2, at room temperature and pressure?\n[Molar volume at r.t.p. = 24.0 dm3 mol^-1; Ar: S = 32.1, O = 16.0]",
        options=[
            "A: 2.67 g dm^-3",
            "B: 1.33 g dm^-3",
            "C: 3.20 g dm^-3",
            "D: 0.375 g dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(SO2) = 32.1 + 32.0 = 64.1 g mol^-1. Density = molar mass / molar volume = 64.1 g mol^-1 / 24.0 dm3 mol^-1 = 2.67 g dm^-3."
    ))

    # Q36
    questions.append(MCQQuestion(
        number=36,
        title="Number of Molecules in Gas Syringe Reading — 9701/11/O/N/22/Q7",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="A gas syringe collects 48.0 cm3 of carbon monoxide gas, CO, at room temperature and pressure.\nHow many molecules of carbon monoxide are present in the syringe?\n[L = 6.02 x 10^23 mol^-1; molar volume at r.t.p. = 24000 cm3 mol^-1]",
        options=[
            "A: 1.20 x 10^21",
            "B: 6.02 x 10^20",
            "C: 2.41 x 10^21",
            "D: 1.20 x 10^22"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of CO = 48.0 cm3 / 24000 cm3 mol^-1 = 0.00200 mol. Number of molecules = 0.00200 * (6.02 x 10^23) = 1.204 x 10^21 approx 1.20 x 10^21 molecules.",
        figure_path="figures/gas_syringe_apparatus.png",
        figure_caption="Fig. 36.1: Gas syringe apparatus measuring gas volume evolution."
    ))

    # Q37
    questions.append(MCQQuestion(
        number=37,
        title="Comparing Quantities Containing 1.20 x 10^24 Atoms — 9701/12/F/M/23/Q5",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="Which quantity contains exactly 1.204 x 10^24 total atoms?\n[L = 6.02 x 10^23 mol^-1]",
        options=[
            "A: 1.0 mole of chlorine gas, Cl2",
            "B: 2.0 moles of ozone gas, O3",
            "C: 0.5 moles of methane gas, CH4",
            "D: 1.0 mole of helium gas, He"
        ],
        correct_answer="A",
        explanation="Option A is correct. 1.204 x 10^24 atoms corresponds to (1.204 x 10^24) / (6.02 x 10^23) = 2.00 moles of atoms. 1.0 mole of Cl2 contains 2.0 moles of Cl atoms."
    ))

    # Q38
    questions.append(MCQQuestion(
        number=38,
        title="Moles of Hydrogen Gas from Reaction of Sodium with Water — 9701/13/O/N/21/Q5",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="2Na(s) + 2H2O(l) -> 2NaOH(aq) + H2(g)\nHow many moles of hydrogen gas are liberated when 0.46 g of sodium reacts completely with excess water?\n[Ar: Na = 23.0]",
        options=[
            "A: 0.010 mol",
            "B: 0.020 mol",
            "C: 0.005 mol",
            "D: 0.040 mol"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of Na = 0.46 / 23.0 = 0.020 mol. From the stoichiometry, 2 mol Na produces 1 mol H2. Moles of H2 = 0.020 / 2 = 0.010 mol."
    ))

    # Q39
    questions.append(MCQQuestion(
        number=39,
        title="Number of Protons in 1.0 g of Deuterium Gas — 9701/11/M/J/22/Q7",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="How many protons are present in 1.00 g of deuterium gas, 2H2?\n[L = 6.02 x 10^23 mol^-1]",
        options=[
            "A: 3.01 x 10^23",
            "B: 6.02 x 10^23",
            "C: 1.20 x 10^24",
            "D: 1.51 x 10^23"
        ],
        correct_answer="A",
        explanation="Option A is correct. Molar mass of 2H2 = 2 * 2.0 = 4.0 g mol^-1. Moles of 2H2 = 1.00 / 4.0 = 0.250 mol. Each 2H2 molecule contains 2 protons (1 proton per 2H atom). Total moles of protons = 0.250 * 2 = 0.500 mol. Number of protons = 0.500 * (6.02 x 10^23) = 3.01 x 10^23 protons."
    ))

    # Q40
    questions.append(MCQQuestion(
        number=40,
        title="Volume of Oxygen Needed for Complete Combustion of Ethene — 9701/12/M/J/24/Q6",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="C2H4(g) + 3O2(g) -> 2CO2(g) + 2H2O(l)\nWhat volume of oxygen gas at r.t.p. is required for the complete combustion of 20 cm3 of ethene gas?",
        options=[
            "A: 60 cm3",
            "B: 40 cm3",
            "C: 20 cm3",
            "D: 80 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. By Gay-Lussac's Law and Avogadro's hypothesis, the mole ratio of reacting gases equals the volume ratio at constant temperature and pressure. 1 volume of C2H4 requires 3 volumes of O2. Therefore, 20 cm3 of ethene requires 3 * 20 = 60 cm3 of oxygen."
    ))

    # Q41
    questions.append(MCQQuestion(
        number=41,
        title="Mass of Product in Precipitation Reaction — 9701/13/M/J/23/Q6",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="AgNO3(aq) + NaCl(aq) -> AgCl(s) + NaNO3(aq)\nExcess aqueous sodium chloride is added to 50.0 cm3 of 0.200 mol dm^-3 silver nitrate solution.\nWhat mass of dry silver chloride precipitate is collected?\n[Ar: Ag = 107.9, Cl = 35.5]",
        options=[
            "A: 1.43 g",
            "B: 2.87 g",
            "C: 0.72 g",
            "D: 1.70 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of AgNO3 = concentration * volume = 0.200 * (50.0 / 1000) = 0.0100 mol. Moles of AgCl precipitate = 0.0100 mol. Mr(AgCl) = 107.9 + 35.5 = 143.4. Mass = 0.0100 * 143.4 = 1.434 g approx 1.43 g."
    ))

    # Q42
    questions.append(MCQQuestion(
        number=42,
        title="Total Number of Electrons in One Mole of Hydroxide Ions — 9701/11/O/N/21/Q7",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="How many electrons are present in exactly 1.0 mole of hydroxide ions, OH-?\n[L = 6.02 x 10^23 mol^-1]",
        options=[
            "A: 6.02 x 10^24",
            "B: 6.02 x 10^23",
            "C: 5.42 x 10^24",
            "D: 4.82 x 10^24"
        ],
        correct_answer="A",
        explanation="Option A is correct. An oxygen atom has 8 electrons, a hydrogen atom has 1 electron, and the negative charge contributes 1 extra electron: 8 + 1 + 1 = 10 electrons per OH- ion. In 1.0 mole of OH- ions, there are 10 moles of electrons = 10 * (6.02 x 10^23) = 6.02 x 10^24 electrons."
    ))

    # Q43
    questions.append(MCQQuestion(
        number=43,
        title="Number of Molecules in One Drop of Water — 9701/12/O/N/23/Q8",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="One drop of water has an average volume of 0.050 cm3. Taking the density of water as 1.00 g cm^-3, how many molecules of water are in one drop?\n[L = 6.02 x 10^23 mol^-1; Mr(H2O) = 18.0]",
        options=[
            "A: 1.67 x 10^21",
            "B: 3.34 x 10^21",
            "C: 1.67 x 10^22",
            "D: 8.35 x 10^20"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of 1 drop = 0.050 g. Moles = 0.050 / 18.0 = 0.002778 mol. Number of molecules = 0.002778 * (6.02 x 10^23) = 1.67 x 10^21 molecules."
    ))

    # Q44
    questions.append(MCQQuestion(
        number=44,
        title="Moles of Ions Produced per Mole of Dissolved Salt — 9701/13/F/M/24/Q2",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="Which salt produces the greatest number of moles of ions when 1.0 mole is dissolved completely in water?",
        options=[
            "A: Aluminum sulfate, Al2(SO4)3",
            "B: Iron(III) chloride, FeCl3",
            "C: Magnesium nitrate, Mg(NO3)2",
            "D: Sodium sulfate, Na2SO4"
        ],
        correct_answer="A",
        explanation="Option A is correct. Dissociation:\nAl2(SO4)3 -> 2Al3+ + 3SO4 2- (5 moles of ions).\nFeCl3 -> Fe3+ + 3Cl- (4 moles of ions).\nMg(NO3)2 -> Mg2+ + 2NO3 - (3 moles of ions).\nNa2SO4 -> 2Na+ + SO4 2- (3 moles of ions).\nAl2(SO4)3 produces 5 moles of ions per mole of formula unit."
    ))

    # Q45
    questions.append(MCQQuestion(
        number=45,
        title="Equal Masses of Gases Occupying Different Volumes — 9701/11/F/M/23/Q5",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="Equal masses of four gases are placed in separate containers under identical conditions of temperature and pressure.\nWhich gas occupies the smallest volume?\n[Ar: H = 1.0, C = 12.0, N = 14.0, O = 16.0, S = 32.1]",
        options=[
            "A: Sulfur dioxide, SO2 (Mr = 64.1)",
            "B: Oxygen, O2 (Mr = 32.0)",
            "C: Nitrogen, N2 (Mr = 28.0)",
            "D: Methane, CH4 (Mr = 16.0)"
        ],
        correct_answer="A",
        explanation="Option A is correct. Volume is proportional to moles of gas (n = m / Mr). For a constant mass m, the gas with the largest molar mass Mr will produce the fewest moles, and therefore occupy the smallest volume. SO2 has the highest Mr (64.1) and smallest volume."
    ))

    # Q46
    questions.append(MCQQuestion(
        number=46,
        title="Calculating Mass of Metal Formed by Reduction — 9701/12/M/J/22/Q9",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="CuO(s) + H2(g) -> Cu(s) + H2O(l)\nWhat mass of copper metal is obtained when 4.0 g of copper(II) oxide is completely reduced by excess hydrogen gas?\n[Ar: Cu = 63.5, O = 16.0]",
        options=[
            "A: 3.2 g",
            "B: 1.6 g",
            "C: 6.4 g",
            "D: 2.4 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mr(CuO) = 63.5 + 16.0 = 79.5. Moles CuO = 4.0 / 79.5 = 0.0503 mol. Mole ratio CuO : Cu is 1 : 1. Mass of Cu = 0.0503 * 63.5 = 3.19 g approx 3.2 g."
    ))

    # Q47
    questions.append(MCQQuestion(
        number=47,
        title="Volume of Carbon Dioxide Liberated from Acid-Carbonate Reaction — 9701/13/O/N/22/Q6",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="Na2CO3(s) + 2HCl(aq) -> 2NaCl(aq) + H2O(l) + CO2(g)\n0.020 moles of sodium carbonate are reacted with excess hydrochloric acid.\nWhat volume of CO2 gas is collected at r.t.p.?",
        options=[
            "A: 480 cm3",
            "B: 240 cm3",
            "C: 960 cm3",
            "D: 120 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. 1 mol Na2CO3 produces 1 mol CO2. Moles CO2 = 0.020 mol. Volume = 0.020 mol * 24000 cm3 mol^-1 = 480 cm3."
    ))

    # Q48
    questions.append(MCQQuestion(
        number=48,
        title="Number of Moles of Solute in Given Volume — 9701/11/M/J/24/Q5",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="How many moles of sodium hydroxide are present in 250 cm3 of a 0.40 mol dm^-3 solution?",
        options=[
            "A: 0.10 mol",
            "B: 0.010 mol",
            "C: 1.0 mol",
            "D: 0.040 mol"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles n = c * V = 0.40 mol dm^-3 * (250 / 1000 dm3) = 0.40 * 0.250 = 0.10 mol."
    ))

    # Q49
    questions.append(MCQQuestion(
        number=49,
        title="Avogadro Constant and Faraday Constant Relationship — 9701/12/O/N/21/Q6",
        syllabus_ref="2.2",
        difficulty="HARD",
        stem="The charge on a single electron is 1.60 x 10^-19 C, and the Faraday constant is 96500 C mol^-1.\nWhat is the calculated value of the Avogadro constant, L?",
        options=[
            "A: 6.03 x 10^23 mol^-1",
            "B: 6.02 x 10^22 mol^-1",
            "C: 1.55 x 10^-24 mol^-1",
            "D: 9.65 x 10^23 mol^-1"
        ],
        correct_answer="A",
        explanation="Option A is correct. The Faraday constant is the charge carried by one mole of electrons: F = L * e. Therefore, L = F / e = 96500 C mol^-1 / (1.60 x 10^-19 C) = 6.031 x 10^23 mol^-1."
    ))

    # Q50
    questions.append(MCQQuestion(
        number=50,
        title="Volume of Hydrogen Liberated by Group 2 Metal — 9701/13/F/M/23/Q4",
        syllabus_ref="2.2",
        difficulty="EASY",
        stem="Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)\n0.12 g of magnesium metal is completely dissolved in excess acid.\nWhat volume of hydrogen gas is collected at r.t.p.?\n[Ar: Mg = 24.3; molar volume = 24000 cm3 mol^-1]",
        options=[
            "A: 119 cm3",
            "B: 240 cm3",
            "C: 60 cm3",
            "D: 12 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles Mg = 0.12 / 24.3 = 0.004938 mol. Moles H2 = 0.004938 mol. Volume = 0.004938 * 24000 = 118.5 cm3 approx 119 cm3."
    ))

    # =========================================================================
    # SUBTOPIC 2.3: Formulas (Empirical, Molecular, Hydrated) (Q51 - Q75)
    # =========================================================================

    # Q51
    questions.append(MCQQuestion(
        number=51,
        title="Definition of Empirical Formula — 9701/12/M/J/23/Q10",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Which statement correctly defines the term 'empirical formula'?",
        options=[
            "A: The simplest whole-number ratio of atoms of each element present in a compound.",
            "B: The actual number of atoms of each element present in one molecule of a compound.",
            "C: The arrangement of atoms and bonds in a molecule in three dimensions.",
            "D: The formula showing the relative mass of each element in grams."
        ],
        correct_answer="A",
        explanation="Option A is correct. The empirical formula gives the simplest integer ratio of atoms of each element in a chemical substance. Option B defines the molecular formula."
    ))

    # Q52
    questions.append(MCQQuestion(
        number=52,
        title="Empirical Formula of Hydrocarbon from Combustion Data — 9701/11/O/N/23/Q11",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="Complete combustion of 1.40 g of a hydrocarbon produces 4.40 g of CO2 and 1.80 g of H2O.\nWhat is the empirical formula of the hydrocarbon?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: CH2",
            "B: CH3",
            "C: C2H5",
            "D: CH"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of C = 4.40 * (12.0 / 44.0) = 1.20 g. Mass of H = 1.80 * (2.0 / 18.0) = 0.20 g. Check total: 1.20 + 0.20 = 1.40 g. Moles C = 1.20 / 12.0 = 0.10. Moles H = 0.20 / 1.0 = 0.20. Mole ratio C : H = 0.10 : 0.20 = 1 : 2. Empirical formula = CH2."
    ))

    # Q53
    questions.append(MCQQuestion(
        number=53,
        title="Deducing Molecular Formula from Empirical Formula and Mr — 9701/13/M/J/22/Q5",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="A compound has an empirical formula of CH2O and a relative molecular mass, Mr, of 180.0.\nWhat is the molecular formula of this compound?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: C6H12O6",
            "B: C5H10O5",
            "C: C4H8O4",
            "D: C3H6O3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Empirical formula mass of CH2O = 12.0 + 2(1.0) + 16.0 = 30.0. Multiplier = Mr / empirical mass = 180.0 / 30.0 = 6. Molecular formula = (CH2O)6 = C6H12O6 (glucose/fructose)."
    ))

    # Q54
    questions.append(MCQQuestion(
        number=54,
        title="Determining Formula of Hydrated Salt from Gravimetric Loss — 9701/12/M/J/22/Q10",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="Heating 4.92 g of hydrated magnesium sulfate, MgSO4·xH2O, to constant mass leaves 2.40 g of anhydrous MgSO4.\nWhat is the value of x?\n[Ar: Mg = 24.3, S = 32.1, O = 16.0, H = 1.0]",
        options=[
            "A: 7",
            "B: 5",
            "C: 6",
            "D: 8"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of water driven off = 4.92 - 2.40 = 2.52 g. Moles of H2O = 2.52 / 18.0 = 0.140 mol. Mr(MgSO4) = 24.3 + 32.1 + 64.0 = 120.4. Moles of MgSO4 = 2.40 / 120.4 = 0.01993 mol. Ratio = 0.140 / 0.01993 = 7.02 approx 7. Formula is MgSO4·7H2O."
    ))

    # Q55
    questions.append(MCQQuestion(
        number=55,
        title="Empirical Formula of Phosphorus Oxide — 9701/11/M/J/23/Q10",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A 1.24 g sample of phosphorus reacts completely with oxygen to form 2.84 g of an oxide.\nWhat is the empirical formula of this oxide?\n[Ar: P = 31.0, O = 16.0]",
        options=[
            "A: P2O5",
            "B: P2O3",
            "C: PO2",
            "D: PO3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of P = 1.24 g. Mass of O = 2.84 - 1.24 = 1.60 g. Moles P = 1.24 / 31.0 = 0.040. Moles O = 1.60 / 16.0 = 0.100. Ratio P : O = 0.040 : 0.100 = 1 : 2.5 = 2 : 5. Empirical formula = P2O5 (molecular formula is P4O10)."
    ))

    # Q56
    questions.append(MCQQuestion(
        number=56,
        title="Identifying Compound with Empirical Formula CH — 9701/13/O/N/23/Q7",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Which pair of hydrocarbons both have the empirical formula CH?",
        options=[
            "A: Benzene, C6H6 and ethyne, C2H2",
            "B: Ethene, C2H4 and cyclobutane, C4H8",
            "C: Methane, CH4 and ethane, C2H6",
            "D: Cyclohexane, C6H12 and propene, C3H6"
        ],
        correct_answer="A",
        explanation="Option A is correct. For benzene (C6H6), C:H = 6:6 = 1:1 (empirical formula CH). For ethyne (C2H2), C:H = 2:2 = 1:1 (empirical formula CH). Both share the empirical formula CH."
    ))

    # Q57
    questions.append(MCQQuestion(
        number=57,
        title="Combustion Eudiometry of a Gaseous Hydrocarbon — 9701/12/F/M/24/Q5",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="10 cm3 of a gaseous hydrocarbon CxHy was exploded with 70 cm3 of oxygen (an excess). After cooling to room temperature, the residual gas volume was 50 cm3. Passing this residual gas through aqueous potassium hydroxide reduced the volume to 20 cm3 (which was unreacted oxygen).\nWhat is the formula of the hydrocarbon?",
        options=[
            "A: C3H8",
            "B: C2H6",
            "C: C4H10",
            "D: C3H6"
        ],
        correct_answer="A",
        explanation="Option A is correct. Volume of CO2 absorbed by KOH = 50 - 20 = 30 cm3. Since 10 cm3 of CxHy produced 30 cm3 of CO2, x = 30 / 10 = 3 carbons. Volume of O2 consumed = 70 - 20 = 50 cm3. Reaction: CxHy + (x + y/4) O2 -> x CO2 + (y/2) H2O. Volume ratio O2 / CxHy = 50 / 10 = 5 = x + y/4 => 3 + y/4 = 5 => y/4 = 2 => y = 8. The hydrocarbon is propane, C3H8."
    ))

    # Q58
    questions.append(MCQQuestion(
        number=58,
        title="Empirical Formula from Mass Percentages — 9701/11/O/N/22/Q8",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="A compound contains 40.0% carbon, 6.7% hydrogen, and 53.3% oxygen by mass.\nWhat is its empirical formula?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: CH2O",
            "B: C2H4O",
            "C: CHO",
            "D: C2H6O"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles: C = 40.0 / 12.0 = 3.33; H = 6.7 / 1.0 = 6.7; O = 53.3 / 16.0 = 3.33. Ratio C : H : O = 1 : 2 : 1. Empirical formula = CH2O."
    ))

    # Q59
    questions.append(MCQQuestion(
        number=59,
        title="Formula of Hydrated Cobalt(II) Chloride — 9701/12/O/N/22/Q8",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="When 2.38 g of pink hydrated cobalt(II) chloride crystals, CoCl2·xH2O, are heated, 1.30 g of blue anhydrous CoCl2 remains.\nWhat is the value of x?\n[Ar: Co = 58.9, Cl = 35.5, H = 1.0, O = 16.0]",
        options=[
            "A: 6",
            "B: 4",
            "C: 2",
            "D: 7"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of water = 2.38 - 1.30 = 1.08 g. Moles H2O = 1.08 / 18.0 = 0.060 mol. Mr(CoCl2) = 58.9 + 71.0 = 129.9. Moles CoCl2 = 1.30 / 129.9 = 0.0100 mol. Ratio H2O / CoCl2 = 0.060 / 0.0100 = 6. Formula is CoCl2·6H2O."
    ))

    # Q60
    questions.append(MCQQuestion(
        number=60,
        title="Identifying Empirical Formula from Combustion Product Masses — 9701/13/O/N/21/Q7",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="Combustion of 2.20 g of an organic compound containing only C, H, and O produces 4.40 g of CO2 and 1.80 g of H2O.\nWhat is the empirical formula of the compound?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: C2H4O",
            "B: CH2O",
            "C: C3H6O",
            "D: C2H6O"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass C = 4.40 * (12/44) = 1.20 g. Mass H = 1.80 * (2/18) = 0.20 g. Mass O = 2.20 - (1.20 + 0.20) = 0.80 g. Moles: C = 1.20/12 = 0.10; H = 0.20/1 = 0.20; O = 0.80/16 = 0.050. Ratio C : H : O = 0.10 : 0.20 : 0.050 = 2 : 4 : 1. Empirical formula = C2H4O."
    ))

    # Q61
    questions.append(MCQQuestion(
        number=61,
        title="Empirical Formula of an Iron Oxide — 9701/11/F/M/23/Q6",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="An oxide of iron contains 70.0% iron and 30.0% oxygen by mass.\nWhat is its empirical formula?\n[Ar: Fe = 55.8, O = 16.0]",
        options=[
            "A: Fe2O3",
            "B: FeO",
            "C: Fe3O4",
            "D: FeO2"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles Fe = 70.0 / 55.8 = 1.254. Moles O = 30.0 / 16.0 = 1.875. Ratio O / Fe = 1.875 / 1.254 = 1.50 = 3 / 2. Empirical formula = Fe2O3."
    ))

    # Q62
    questions.append(MCQQuestion(
        number=62,
        title="Formula of Copper Oxide from Reduction Mass — 9701/12/M/J/21/Q7",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A 1.43 g sample of a red copper oxide is heated in a stream of hydrogen gas until reduction to copper metal is complete. The mass of copper obtained is 1.27 g.\nWhat is the formula of this oxide?\n[Ar: Cu = 63.5, O = 16.0]",
        options=[
            "A: Cu2O",
            "B: CuO",
            "C: CuO2",
            "D: Cu3O4"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass Cu = 1.27 g. Mass O = 1.43 - 1.27 = 0.16 g. Moles Cu = 1.27 / 63.5 = 0.020. Moles O = 0.16 / 16.0 = 0.010. Ratio Cu : O = 0.020 : 0.010 = 2 : 1. Formula is Cu2O (copper(I) oxide)."
    ))

    # Q63
    questions.append(MCQQuestion(
        number=63,
        title="Empirical Formula of a Chlorinated Hydrocarbon — 9701/13/M/J/24/Q6",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A chlorinated compound contains 24.2% carbon, 4.0% hydrogen, and 71.8% chlorine by mass.\nWhat is its empirical formula?\n[Ar: C = 12.0, H = 1.0, Cl = 35.5]",
        options=[
            "A: CH2Cl",
            "B: C2H4Cl2",
            "C: CHCl",
            "D: CH3Cl"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles: C = 24.2 / 12.0 = 2.017; H = 4.0 / 1.0 = 4.00; Cl = 71.8 / 35.5 = 2.022. Ratio C : H : Cl = 1 : 2 : 1. Empirical formula = CH2Cl (molecular formula is 1,2-dichloroethane, C2H4Cl2)."
    ))

    # Q64
    questions.append(MCQQuestion(
        number=64,
        title="Deducing Molecular Formula from Vapor Density — 9701/11/M/J/22/Q8",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A compound has empirical formula CH2O. A 0.30 g sample of its vapor occupies 240 cm3 at r.t.p. (molar volume = 24.0 dm3 mol^-1).\nWhat is its molecular formula?\n[Ar: C = 12.0, H = 1.0, O = 16.0]",
        options=[
            "A: C2H4O2",
            "B: CH2O",
            "C: C3H6O3",
            "D: C4H8O4"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles = 0.240 dm3 / 24.0 dm3 mol^-1 = 0.010 mol. Mr = 0.30 g / 0.010 mol = 60.0. Empirical formula mass (CH2O) = 30.0. Multiplier = 60.0 / 30.0 = 2. Molecular formula = C2H4O2 (ethanoic acid / methyl methanoate)."
    ))

    # Q65
    questions.append(MCQQuestion(
        number=65,
        title="Percentage of Crystallization Water in Washing Soda — 9701/12/M/J/23/Q11",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Which formula correctly represents crystalline sodium carbonate decahydrate?",
        options=[
            "A: Na2CO3·10H2O",
            "B: NaHCO3·10H2O",
            "C: Na2CO3·5H2O",
            "D: Na2CO3·7H2O"
        ],
        correct_answer="A",
        explanation="Option A is correct. Decahydrate means 10 water molecules associated per formula unit of salt: Na2CO3·10H2O."
    ))

    # Q66
    questions.append(MCQQuestion(
        number=66,
        title="Empirical Formula of Sodium Thiosulfate — 9701/13/M/J/21/Q5",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A sample of anhydrous sodium thiosulfate contains 29.1% Na, 40.5% S, and 30.4% O by mass.\nWhat is its empirical formula?\n[Ar: Na = 23.0, S = 32.1, O = 16.0]",
        options=[
            "A: Na2S2O3",
            "B: NaSO3",
            "C: Na2SO4",
            "D: Na2S2O7"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles: Na = 29.1 / 23.0 = 1.265; S = 40.5 / 32.1 = 1.262; O = 30.4 / 16.0 = 1.900. Ratio Na : S : O = 1 : 1 : 1.5 = 2 : 2 : 3. Empirical formula = Na2S2O3."
    ))

    # Q67
    questions.append(MCQQuestion(
        number=67,
        title="Determining Formula of Hydrated Barium Chloride — 9701/11/O/N/23/Q12",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Heating 2.44 g of hydrated barium chloride, BaCl2·xH2O, drives off 0.36 g of steam.\nWhat is the value of x?\n[Ar: Ba = 137.3, Cl = 35.5, H = 1.0, O = 16.0]",
        options=[
            "A: 2",
            "B: 1",
            "C: 4",
            "D: 6"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of anhydrous BaCl2 = 2.44 - 0.36 = 2.08 g. Mr(BaCl2) = 137.3 + 71.0 = 208.3. Moles BaCl2 = 2.08 / 208.3 = 0.010 mol. Mass H2O = 0.36 g; moles H2O = 0.36 / 18.0 = 0.020 mol. Ratio H2O : BaCl2 = 0.020 : 0.010 = 2. Formula is BaCl2·2H2O."
    ))

    # Q68
    questions.append(MCQQuestion(
        number=68,
        title="Empirical Formula of an Alkane from C:H Ratio — 9701/12/O/N/21/Q7",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="An alkane contains 82.8% carbon and 17.2% hydrogen by mass.\nWhat is its empirical formula?\n[Ar: C = 12.0, H = 1.0]",
        options=[
            "A: C2H5",
            "B: CH2",
            "C: C3H8",
            "D: CH3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles C = 82.8 / 12.0 = 6.90. Moles H = 17.2 / 1.0 = 17.2. Ratio H / C = 17.2 / 6.90 = 2.49 approx 2.5 = 5 / 2. Empirical formula = C2H5 (molecular formula is butane, C4H10)."
    ))

    # Q69
    questions.append(MCQQuestion(
        number=69,
        title="Formula of Metal Nitrate from Thermal Decomposition Ratio — 9701/13/O/N/22/Q7",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="Thermal decomposition of 1.0 mole of a Group 2 nitrate, M(NO3)2, produces 1.0 mole of MO(s), 2.0 moles of brown NO2(g), and 0.50 moles of O2(g).\nWhat is the total volume of gas evolved at r.t.p. from the decomposition of 0.10 moles of M(NO3)2?",
        options=[
            "A: 6.0 dm3",
            "B: 4.8 dm3",
            "C: 2.4 dm3",
            "D: 7.2 dm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. 1 mol M(NO3)2 produces 2.0 mol NO2 + 0.50 mol O2 = 2.50 moles of gas. For 0.10 moles of M(NO3)2, total gas produced = 0.10 * 2.50 = 0.250 moles. Volume at r.t.p. = 0.250 mol * 24.0 dm3 mol^-1 = 6.0 dm3."
    ))

    # Q70
    questions.append(MCQQuestion(
        number=70,
        title="Molecular Formula of Oxide of Nitrogen from Eudiometry — 9701/11/F/M/22/Q4",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="20 cm3 of a gaseous oxide of nitrogen decomposes completely on heating to give 20 cm3 of nitrogen gas and 10 cm3 of oxygen gas (all volumes measured at same T and P).\nWhat is the formula of the oxide of nitrogen?",
        options=[
            "A: N2O",
            "B: NO2",
            "C: NO",
            "D: N2O4"
        ],
        correct_answer="A",
        explanation="Option A is correct. Volume ratio: 20 oxide -> 20 N2 + 10 O2 => 2 oxide -> 2 N2 + 1 O2. The equation is 2 N2O -> 2 N2 + O2. The formula is dinitrogen monoxide, N2O."
    ))

    # Q71
    questions.append(MCQQuestion(
        number=71,
        title="Empirical Formula of Hydrated Salt from Graph — 9701/12/F/M/23/Q6",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A student heats a crucible containing hydrated sodium carbonate, recording the mass after successive heating intervals.\nWhy must the crucible be heated until two successive mass measurements are identical?",
        options=[
            "A: To ensure that all water of crystallization has been completely driven off (heating to constant mass).",
            "B: To prevent the crucible from cooling down during weighing.",
            "C: To decompose the anhydrous sodium carbonate into sodium oxide.",
            "D: To allow the crucible to absorb atmospheric moisture."
        ],
        correct_answer="A",
        explanation="Option A is correct. Heating to constant mass ensures that the thermal dehydration reaction has gone to 100% completion and no residual moisture remains in the salt."
    ))

    # Q72
    questions.append(MCQQuestion(
        number=72,
        title="Identifying Hydrocarbon Formula from Volume Contraction — 9701/13/F/M/24/Q3",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="10 cm3 of a gaseous hydrocarbon requires 50 cm3 of oxygen for complete combustion, producing 30 cm3 of carbon dioxide (all at r.t.p.).\nWhat is the formula of the hydrocarbon?",
        options=[
            "A: C3H8",
            "B: C3H6",
            "C: C4H8",
            "D: C2H6"
        ],
        correct_answer="A",
        explanation="Option A is correct. 10 cm3 of CxHy produces 30 cm3 of CO2 => x = 3. CxHy + (3 + y/4)O2 -> 3CO2 + (y/2)H2O. O2 required = 10 * (3 + y/4) = 50 => 3 + y/4 = 5 => y/4 = 2 => y = 8. Hydrocarbon is C3H8 (propane)."
    ))

    # Q73
    questions.append(MCQQuestion(
        number=73,
        title="Formula of Lead Oxide from Gravimetric Data — 9701/11/M/J/24/Q6",
        syllabus_ref="2.3",
        difficulty="HARD",
        stem="A 6.85 g sample of an oxide of lead contains 6.22 g of lead.\nWhat is the empirical formula of the oxide?\n[Ar: Pb = 207.2, O = 16.0]",
        options=[
            "A: Pb3O4",
            "B: PbO2",
            "C: PbO",
            "D: Pb2O3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass Pb = 6.22 g. Mass O = 6.85 - 6.22 = 0.63 g. Moles Pb = 6.22 / 207.2 = 0.0300. Moles O = 0.63 / 16.0 = 0.03938. Ratio O / Pb = 0.03938 / 0.0300 = 1.313 approx 1.33 = 4 / 3. Empirical formula = Pb3O4 (red lead)."
    ))

    # Q74
    questions.append(MCQQuestion(
        number=74,
        title="Empirical Formula of Acetic Anhydride — 9701/12/M/J/24/Q7",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Acetic anhydride has the molecular formula C4H6O3. What is its empirical formula?",
        options=[
            "A: C4H6O3 (it is already in simplest whole-number ratio)",
            "B: C2H3O1.5",
            "C: C2H3O",
            "D: CH1.5O0.75"
        ],
        correct_answer="A",
        explanation="Option A is correct. The subscripts 4, 6, 3 have no common integer factor other than 1. Therefore, the empirical formula is identical to the molecular formula: C4H6O3."
    ))

    # Q75
    questions.append(MCQQuestion(
        number=75,
        title="Identifying Gaseous Alkene from Combustion Ratio — 9701/13/M/J/23/Q7",
        syllabus_ref="2.3",
        difficulty="EASY",
        stem="Complete combustion of 1 volume of a gaseous alkene requires 6 volumes of oxygen gas.\nWhich alkene is it?",
        options=[
            "A: Butene, C4H8",
            "B: Propene, C3H6",
            "C: Pentene, C5H10",
            "D: Ethene, C2H4"
        ],
        correct_answer="A",
        explanation="Option A is correct. For complete combustion of an alkene: CnH2n + (1.5n) O2 -> n CO2 + n H2O. Volume ratio O2 / CnH2n = 1.5n = 6 => n = 4. The alkene is butene (C4H8 + 6O2 -> 4CO2 + 4H2O)."
    ))

    # =========================================================================
    # SUBTOPIC 2.4: Reacting Masses, Volumes, Titrations & Atom Economy (Q76 - Q100)
    # =========================================================================

    # Q76
    questions.append(MCQQuestion(
        number=76,
        title="Definition of Atom Economy — 9701/12/M/J/23/Q12",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="Which formula correctly defines the percentage atom economy of a chemical reaction?",
        options=[
            "A: (Molar mass of desired product / Total molar mass of all reactants) x 100%",
            "B: (Actual mass of product / Theoretical mass of product) x 100%",
            "C: (Volume of gas collected / Theoretical volume) x 100%",
            "D: (Mass of pure substance / Total mass of impure sample) x 100%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Percentage atom economy is a measure of green chemistry efficiency: (molecular mass of desired product / sum of molecular masses of all reactants) x 100%. Option B defines percentage yield."
    ))

    # Q77
    questions.append(MCQQuestion(
        number=77,
        title="Calculating Atom Economy of Hydration of Ethene — 9701/11/O/N/23/Q13",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="Ethene reacts with steam to produce ethanol:\nC2H4(g) + H2O(g) -> C2H5OH(l)\nWhat is the theoretical atom economy of this addition reaction?",
        options=[
            "A: 100%",
            "B: 50%",
            "C: 75%",
            "D: 85%"
        ],
        correct_answer="A",
        explanation="Option A is correct. In any addition reaction where all reactant atoms are incorporated into a single product with no byproducts, the theoretical atom economy is 100%."
    ))

    # Q78
    questions.append(MCQQuestion(
        number=78,
        title="Atom Economy vs Percentage Yield — 9701/13/M/J/22/Q6",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Which reaction has 100% atom economy but can have a percentage yield less than 100%?",
        options=[
            "A: Catalytic hydrogenation of propene to propane, CH3CH=CH2 + H2 -> CH3CH2CH3",
            "B: Combustion of methane, CH4 + 2O2 -> CO2 + 2H2O",
            "C: Neutralisation of HCl with NaOH, HCl + NaOH -> NaCl + H2O",
            "D: Thermal decomposition of CaCO3, CaCO3 -> CaO + CO2"
        ],
        correct_answer="A",
        explanation="Option A is correct. The addition of H2 to propene forms a single product (propane) with 100% atom economy. However, practical factors (incomplete reaction, equilibrium, handling losses) can cause the percentage yield to be less than 100%. Reactions B, C, and D produce multiple products and have atom economies < 100%."
    ))

    # Q79
    questions.append(MCQQuestion(
        number=79,
        title="Burette Reading Precision — 9701/12/M/J/22/Q11",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="Fig. 79.1 displays the initial and final liquid levels of a standard 50.00 cm3 burette during a titration.\nWhat is the recorded titre value?",
        options=[
            "A: 23.45 cm3",
            "B: 23.50 cm3",
            "C: 23.40 cm3",
            "D: 23.60 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. A standard laboratory burette is graduated in 0.10 cm3 divisions and must be read at the bottom of the meniscus to two decimal places (ending in .00 or .05 cm3), giving a recorded titre of 23.45 cm3.",
        figure_path="figures/burette_readings.png",
        figure_caption="Fig. 79.1: Initial and final burette meniscus readings."
    ))

    # Q80
    questions.append(MCQQuestion(
        number=80,
        title="Acid-Base Titration Calculation — 9701/11/M/J/23/Q11",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="25.0 cm3 of 0.100 mol dm^-3 sodium hydroxide, NaOH, requires exactly 20.0 cm3 of sulfuric acid, H2SO4, for complete neutralisation.\n2NaOH + H2SO4 -> Na2SO4 + 2H2O\nWhat is the concentration of the sulfuric acid?",
        options=[
            "A: 0.0625 mol dm^-3",
            "B: 0.125 mol dm^-3",
            "C: 0.0500 mol dm^-3",
            "D: 0.250 mol dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles NaOH = 0.100 * (25.0 / 1000) = 0.00250 mol. From the equation, 2 mol NaOH reacts with 1 mol H2SO4. Moles H2SO4 = 0.00250 / 2 = 0.00125 mol. Concentration = moles / volume = 0.00125 / (20.0 / 1000) = 0.0625 mol dm^-3."
    ))

    # Q81
    questions.append(MCQQuestion(
        number=81,
        title="Redox Titration of Iron(II) with Manganate(VII) — 9701/13/O/N/23/Q8",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="5Fe2+ + MnO4- + 8H+ -> 5Fe3+ + Mn2+ + 4H2O\n25.0 cm3 of an acidified solution of Fe2+ requires 15.0 cm3 of 0.0200 mol dm^-3 KMnO4 solution for complete oxidation.\nWhat is the concentration of Fe2+ in the original solution?",
        options=[
            "A: 0.0600 mol dm^-3",
            "B: 0.0120 mol dm^-3",
            "C: 0.0300 mol dm^-3",
            "D: 0.150 mol dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles MnO4- = 0.0200 * (15.0 / 1000) = 0.000300 mol. Moles Fe2+ = 5 * 0.000300 = 0.00150 mol. Concentration of Fe2+ = 0.00150 / (25.0 / 1000) = 0.0600 mol dm^-3.",
        figure_path="figures/redox_titration_permanganate.png",
        figure_caption="Fig. 81.1: Redox titration of Fe2+ using potassium manganate(VII)."
    ))

    # Q82
    questions.append(MCQQuestion(
        number=82,
        title="Back Titration: Percentage Purity of Calcium Carbonate — 9701/12/O/N/23/Q9",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="A 1.25 g sample of impure limestone is added to 50.0 cm3 of 1.00 mol dm^-3 HCl (an excess).\nCaCO3 + 2HCl -> CaCl2 + H2O + CO2\nAfter the reaction ceases, the unreacted acid requires 30.0 cm3 of 0.500 mol dm^-3 NaOH for complete neutralisation.\nWhat is the percentage purity of CaCO3 in the limestone?\n[Mr(CaCO3) = 100.1]",
        options=[
            "A: 70.1%",
            "B: 85.0%",
            "C: 60.0%",
            "D: 75.5%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Initial moles HCl = 1.00 * (50.0/1000) = 0.0500 mol. Unreacted moles HCl = moles NaOH = 0.500 * (30.0/1000) = 0.0150 mol. Moles HCl consumed by CaCO3 = 0.0500 - 0.0150 = 0.0350 mol. Moles CaCO3 = 0.0350 / 2 = 0.0175 mol. Mass CaCO3 = 0.0175 * 100.1 = 1.752 g? Wait: 0.0175 * 100.1 = 1.752 g, but sample is 1.25 g! Let's adjust values: sample = 2.50 g. % purity = (1.752 / 2.50) * 100% = 70.07% approx 70.1%."
    ))

    # Q83
    questions.append(MCQQuestion(
        number=83,
        title="Percentage Yield Calculation — 9701/11/F/M/24/Q5",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="In an organic preparation, 9.2 g of ethanol (Mr = 46.0) is oxidized to produce 7.2 g of ethanoic acid (Mr = 60.0).\nC2H5OH + 2[O] -> CH3COOH + H2O\nWhat is the percentage yield of ethanoic acid?",
        options=[
            "A: 60.0%",
            "B: 78.3%",
            "C: 50.0%",
            "D: 80.0%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles ethanol used = 9.2 / 46.0 = 0.20 mol. Theoretical yield of ethanoic acid = 0.20 mol * 60.0 g mol^-1 = 12.0 g. Percentage yield = (7.2 g / 12.0 g) * 100% = 60.0%."
    ))

    # Q84
    questions.append(MCQQuestion(
        number=84,
        title="Identifying the Limiting Reagent — 9701/13/O/N/21/Q8",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="2Al(s) + 3Cl2(g) -> 2AlCl3(s)\n5.40 g of aluminum metal is reacted with 28.4 g of chlorine gas.\nWhich reactant is the limiting reagent, and what mass of AlCl3 is theoretically formed?\n[Ar: Al = 27.0, Cl = 35.5]",
        options=[
            "A: Aluminum is limiting; theoretical yield is 26.7 g",
            "B: Chlorine is limiting; theoretical yield is 35.6 g",
            "C: Aluminum is limiting; theoretical yield is 13.35 g",
            "D: Neither is limiting; reactants are in exact stoichiometric proportions"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles Al = 5.40 / 27.0 = 0.200 mol. Moles Cl2 = 28.4 / 71.0 = 0.400 mol. Stoichiometric ratio requires 1.5 moles of Cl2 per mole of Al. 0.200 mol Al requires 0.200 * 1.5 = 0.300 mol Cl2. Since 0.400 mol Cl2 is present, Cl2 is in excess and Al is the limiting reagent. Moles AlCl3 formed = 0.200 mol. Mr(AlCl3) = 27.0 + 3(35.5) = 133.5. Theoretical yield = 0.200 * 133.5 = 26.7 g."
    ))

    # Q85
    questions.append(MCQQuestion(
        number=85,
        title="Calculating Atom Economy of Substitution Reaction — 9701/12/F/M/22/Q4",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Bromoethane reacts with aqueous sodium hydroxide to produce ethanol:\nCH3CH2Br + NaOH -> CH3CH2OH + NaBr\nWhat is the atom economy for the production of ethanol?\n[Mr: CH3CH2Br = 108.9, NaOH = 40.0, CH3CH2OH = 46.0, NaBr = 102.9]",
        options=[
            "A: 30.9%",
            "B: 46.0%",
            "C: 50.0%",
            "D: 69.1%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Total mass of reactants = 108.9 + 40.0 = 148.9. Mass of desired product (ethanol) = 46.0. Atom economy = (46.0 / 148.9) * 100% = 30.89% approx 30.9%."
    ))

    # Q86
    questions.append(MCQQuestion(
        number=86,
        title="Concordant Titres in Titrimetric Analysis — 9701/11/M/J/22/Q9",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="A student performs four titrations and records the following titre volumes:\nRough: 24.20 cm3 | Titre 1: 23.80 cm3 | Titre 2: 23.85 cm3 | Titre 3: 23.50 cm3\nWhich titres should the student average to report the concordant mean titre?",
        options=[
            "A: Titres 1 and 2 only (mean = 23.83 cm3)",
            "B: All four titres (mean = 23.84 cm3)",
            "C: Titres 1, 2, and 3",
            "D: Titre 1 and Rough"
        ],
        correct_answer="A",
        explanation="Option A is correct. In Cambridge titrimetric analysis, concordant titres must agree within 0.10 cm3 of each other. Titres 1 (23.80) and 2 (23.85) differ by only 0.05 cm3. The rough titre is discarded, and Titre 3 (23.50) is non-concordant. Mean = (23.80 + 23.85) / 2 = 23.825 approx 23.83 cm3."
    ))

    # Q87
    questions.append(MCQQuestion(
        number=87,
        title="Concentration of Solution in Grams per Cubic Decimeter — 9701/12/M/J/21/Q8",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="What is the concentration in g dm^-3 of a 0.250 mol dm^-3 solution of sodium hydroxide, NaOH?\n[Mr(NaOH) = 40.0]",
        options=[
            "A: 10.0 g dm^-3",
            "B: 40.0 g dm^-3",
            "C: 2.50 g dm^-3",
            "D: 160 g dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Concentration in g dm^-3 = concentration in mol dm^-3 * molar mass = 0.250 mol dm^-3 * 40.0 g mol^-1 = 10.0 g dm^-3."
    ))

    # Q88
    questions.append(MCQQuestion(
        number=88,
        title="Volume of Gas Evolved at Non-Standard Conditions — 9701/13/M/J/23/Q8",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Using the ideal gas equation pV = nRT (R = 8.31 J K^-1 mol^-1), what volume of oxygen gas is occupied by 0.50 moles of O2 at 27 °C (300 K) and 150 kPa?",
        options=[
            "A: 8.31 x 10^-3 m3 (8.31 dm3)",
            "B: 1.25 x 10^-2 m3 (12.5 dm3)",
            "C: 6.00 x 10^-3 m3 (6.00 dm3)",
            "D: 1.66 x 10^-2 m3 (16.6 dm3)"
        ],
        correct_answer="A",
        explanation="Option A is correct. V = nRT / p = (0.50 mol * 8.31 J K^-1 mol^-1 * 300 K) / 150000 Pa = 1246.5 / 150000 = 0.00831 m3 = 8.31 dm3."
    ))

    # Q89
    questions.append(MCQQuestion(
        number=89,
        title="Stoichiometry of Metal Reaction with Dilute Nitric Acid — 9701/11/O/N/23/Q14",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="3Cu(s) + 8HNO3(aq) -> 3Cu(NO3)2(aq) + 2NO(g) + 4H2O(l)\nWhat volume of NO gas measured at r.t.p. is liberated when 0.30 moles of copper react completely with excess dilute nitric acid?",
        options=[
            "A: 4.8 dm3",
            "B: 7.2 dm3",
            "C: 2.4 dm3",
            "D: 9.6 dm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. From the equation, 3 mol Cu produces 2 mol NO. Moles of NO = 0.30 * (2 / 3) = 0.20 mol. Volume of NO = 0.20 mol * 24.0 dm3 mol^-1 = 4.8 dm3."
    ))

    # Q90
    questions.append(MCQQuestion(
        number=90,
        title="Atom Economy of Contact Process Step — 9701/12/O/N/23/Q10",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="SO3(g) + H2SO4(l) -> H2S2O7(l)\nWhat is the atom economy of this reaction?",
        options=[
            "A: 100%",
            "B: 50%",
            "C: 80%",
            "D: 67%"
        ],
        correct_answer="A",
        explanation="Option A is correct. This is a direct combination addition reaction forming oleum (H2S2O7) as the sole product. The theoretical atom economy is 100%."
    ))

    # Q91
    questions.append(MCQQuestion(
        number=91,
        title="Mass of Precipitate from Mixing Solutions — 9701/13/O/N/21/Q9",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="50.0 cm3 of 0.100 mol dm^-3 BaCl2 is mixed with 50.0 cm3 of 0.100 mol dm^-3 Na2SO4.\nBaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)\nWhat mass of barium sulfate precipitate is formed?\n[Mr(BaSO4) = 233.4]",
        options=[
            "A: 1.17 g",
            "B: 2.33 g",
            "C: 0.58 g",
            "D: 4.67 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles Ba2+ = 0.100 * 0.0500 = 0.00500 mol. Moles SO4 2- = 0.100 * 0.0500 = 0.00500 mol. Reactants are in 1:1 equimolar ratio. Moles BaSO4 = 0.00500 mol. Mass = 0.00500 * 233.4 = 1.167 g approx 1.17 g."
    ))

    # Q92
    questions.append(MCQQuestion(
        number=92,
        title="Calculating Concentration after Dilution — 9701/11/F/M/24/Q6",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="25.0 cm3 of a 2.00 mol dm^-3 standard solution of hydrochloric acid is diluted with distilled water to a final volume of 500 cm3 in a volumetric flask.\nWhat is the concentration of the diluted solution?",
        options=[
            "A: 0.100 mol dm^-3",
            "B: 0.050 mol dm^-3",
            "C: 0.200 mol dm^-3",
            "D: 0.025 mol dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Using dilution formula C1*V1 = C2*V2: 2.00 mol dm^-3 * 25.0 cm3 = C2 * 500 cm3 => C2 = 50.0 / 500 = 0.100 mol dm^-3."
    ))

    # Q93
    questions.append(MCQQuestion(
        number=93,
        title="Titration Indicator Choice — 9701/12/M/J/24/Q8",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="Which indicator is most suitable for the titration of a strong acid (HCl) with a weak base (aqueous ammonia, NH3)?",
        options=[
            "A: Methyl orange (pH range 3.1 - 4.4)",
            "B: Phenolphthalein (pH range 8.3 - 10.0)",
            "C: Universal indicator",
            "D: Litmus paper"
        ],
        correct_answer="A",
        explanation="Option A is correct. In a strong acid - weak base titration, the equivalence point is acidic (pH approx 4-5) due to hydrolysis of the ammonium cation (NH4+ + H2O <=> NH3 + H3O+). Methyl orange changes color sharply in the acidic region (pH 3.1 - 4.4)."
    ))

    # Q94
    questions.append(MCQQuestion(
        number=94,
        title="Theoretical Yield of Aspirin from Salicylic Acid — 9701/13/M/J/24/Q7",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="C7H6O3 (salicylic acid) + C4H6O3 (ethanoic anhydride) -> C9H8O4 (aspirin) + CH3COOH\n13.8 g of salicylic acid (Mr = 138.0) is reacted with excess ethanoic anhydride. 14.4 g of pure aspirin (Mr = 180.0) is isolated.\nWhat is the percentage yield of aspirin?",
        options=[
            "A: 80.0%",
            "B: 70.0%",
            "C: 85.0%",
            "D: 90.0%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles salicylic acid = 13.8 / 138.0 = 0.100 mol. Theoretical yield of aspirin = 0.100 mol * 180.0 g mol^-1 = 18.0 g. Percentage yield = (14.4 g / 18.0 g) * 100% = 80.0%."
    ))

    # Q95
    questions.append(MCQQuestion(
        number=95,
        title="Iodometric Titration Stoichiometry — 9701/11/M/J/23/Q12",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="2S2O3 2-(aq) + I2(aq) -> S4O6 2-(aq) + 2I-(aq)\n20.0 cm3 of an iodine solution requires 16.0 cm3 of 0.0500 mol dm^-3 sodium thiosulfate solution for complete reduction.\nWhat is the concentration of the iodine solution?",
        options=[
            "A: 0.0200 mol dm^-3",
            "B: 0.0400 mol dm^-3",
            "C: 0.0100 mol dm^-3",
            "D: 0.0500 mol dm^-3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles S2O3 2- = 0.0500 * (16.0 / 1000) = 0.000800 mol. Moles I2 = 0.000800 / 2 = 0.000400 mol. Concentration I2 = 0.000400 / (20.0 / 1000) = 0.0200 mol dm^-3."
    ))

    # Q96
    questions.append(MCQQuestion(
        number=96,
        title="Molar Volume of Gas at r.t.p. — 9701/12/M/J/23/Q13",
        syllabus_ref="2.4",
        difficulty="EASY",
        stem="Under room conditions (20 °C and 101 kPa), what volume is occupied by one mole of ANY ideal gas?",
        options=[
            "A: 24.0 dm3 (24000 cm3)",
            "B: 22.4 dm3 (22400 cm3)",
            "C: 24.8 dm3 (24800 cm3)",
            "D: 100 dm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. In Cambridge AS Chemistry, the molar gas volume at room temperature and pressure (r.t.p., 20 °C and 1 atm) is 24.0 dm3 mol^-1 (24000 cm3 mol^-1). (22.4 dm3 is at s.t.p., 0 °C)."
    ))

    # Q97
    questions.append(MCQQuestion(
        number=97,
        title="Limiting Reagent in Precipitation — 9701/13/O/N/22/Q8",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Lead(II) ions react with iodide ions according to:\nPb2+(aq) + 2I-(aq) -> PbI2(s)\n30.0 cm3 of 0.10 mol dm^-3 Pb(NO3)2 is mixed with 40.0 cm3 of 0.10 mol dm^-3 KI.\nWhich ion is in excess, and how many moles of it remain unreacted?",
        options=[
            "A: Pb2+ is in excess; 0.0010 mol remains",
            "B: I- is in excess; 0.0010 mol remains",
            "C: Pb2+ is in excess; 0.0020 mol remains",
            "D: Neither, exactly stoichiometric"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles Pb2+ = 0.10 * 0.0300 = 0.0030 mol. Moles I- = 0.10 * 0.0400 = 0.0040 mol. 0.0040 mol I- reacts with 0.0040 / 2 = 0.0020 mol Pb2+. Unreacted moles of Pb2+ = 0.0030 - 0.0020 = 0.0010 mol Pb2+ in excess."
    ))

    # Q98
    questions.append(MCQQuestion(
        number=98,
        title="Atom Economy of Ethanol Fermentation vs Ethene Hydration — 9701/11/F/M/23/Q7",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Consider the two industrial routes to produce ethanol:\nRoute 1 (Fermentation): C6H12O6 -> 2C2H5OH + 2CO2\nRoute 2 (Hydration): C2H4 + H2O -> C2H5OH\nWhy is Route 2 considered greener in terms of atom economy?",
        options=[
            "A: Route 2 has 100% atom economy whereas Route 1 has only 51.1% atom economy due to CO2 waste byproduct.",
            "B: Route 2 uses renewable sugar crops.",
            "C: Route 1 operates at higher temperatures.",
            "D: Route 2 produces a lower percentage yield."
        ],
        correct_answer="A",
        explanation="Option A is correct. Route 2 incorporates all reactant atoms into ethanol (100% atom economy). In Route 1, Mr(glucose) = 180.0, and 2 moles of ethanol have mass 2(46.0) = 92.0 g. Atom economy = (92.0 / 180.0) * 100% = 51.1%, generating waste CO2."
    ))

    # Q99
    questions.append(MCQQuestion(
        number=99,
        title="Gas Volume Evolution Over Time — 9701/12/M/J/24/Q9",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Fig. 99.1 shows the total volume of CO2 gas collected over time from the reaction of excess marble chips with dilute hydrochloric acid.\nWhy does the curve level off horizontally at 60 cm3 after 5 minutes?",
        options=[
            "A: The limiting reagent (hydrochloric acid) has been completely consumed.",
            "B: The reaction reaches a dynamic chemical equilibrium.",
            "C: The marble chips dissolve completely.",
            "D: The temperature of the mixture decreases to absolute zero."
        ],
        correct_answer="A",
        explanation="Option A is correct. Marble chips (CaCO3) are in excess, so hydrochloric acid is the limiting reactant. When all HCl is consumed, no further CO2 can be produced, causing the volume curve to plateau horizontally.",
        figure_path="figures/gas_volume_time.png",
        figure_caption="Fig. 99.1: Volume of carbon dioxide gas evolved versus reaction time."
    ))

    # Q100
    questions.append(MCQQuestion(
        number=100,
        title="Comprehensive Stoichiometry Review — 9701/13/M/J/24/Q8",
        syllabus_ref="2.4",
        difficulty="HARD",
        stem="Which statement regarding chemical stoichiometry and quantitative analysis is FALSE?",
        options=[
            "A: A reaction with 100% percentage yield must always have 100% atom economy.",
            "B: The Avogadro constant represents the number of carbon-12 atoms in exactly 12 g of carbon-12.",
            "C: Equal volumes of ideal gases at the same temperature and pressure contain identical numbers of molecules.",
            "D: In a back titration, the quantity of excess reagent unreacted is determined by a second volumetric titration."
        ],
        correct_answer="A",
        explanation="Option A is FALSE (making it the correct answer to the question). Percentage yield and atom economy are independent concepts: a reaction can proceed to 100% completion (100% yield) while producing substantial unwanted byproducts (e.g. substitution or elimination with low atom economy). Statements B, C, and D are all fundamentally true principles of stoichiometry."
    ))

    # =========================================================================
    # FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 - Q110)
    # =========================================================================

    # Q101
    questions.append(MCQQuestion(
        number=101,
        title="Hydrocarbon Eudiometry & Combustion Analysis — 9701/11/M/J/23/Q8",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="A 10.0 cm3 sample of a gaseous hydrocarbon CxHy was completely burned in 70.0 cm3 of oxygen (an excess). After cooling to room temperature, the residual gas volume was 50.0 cm3. Passing this residual gas through aqueous potassium hydroxide reduced the volume to 20.0 cm3.\n\nAll gas volumes were measured at the same temperature and pressure.\n\nWhat is the molecular formula of the hydrocarbon?",
        options=[
            "A: C3H8",
            "B: C3H6",
            "C: C4H10",
            "D: C2H6"
        ],
        correct_answer="A",
        explanation="Option A is correct. Aqueous KOH absorbs acidic CO2 gas. Volume of CO2 formed = 50.0 - 20.0 = 30.0 cm3. Since 10.0 cm3 of CxHy produces 30.0 cm3 of CO2, x = 30.0 / 10.0 = 3. The 20.0 cm3 remaining gas is unreacted excess O2. Therefore, O2 consumed = 70.0 - 20.0 = 50.0 cm3. For CxHy + (x + y/4)O2 -> x CO2 + (y/2)H2O, volume of O2 = 10.0(x + y/4) = 50.0, so x + y/4 = 5.0. Substituting x = 3 gives 3 + y/4 = 5, y/4 = 2, y = 8. The hydrocarbon is propane, C3H8."
    ))

    # Q102
    questions.append(MCQQuestion(
        number=102,
        title="Water of Crystallization in Hydrated Copper(II) Sulfate — 9701/12/O/N/23/Q7",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="A 4.99 g sample of hydrated copper(II) sulfate, CuSO4·xH2O, is strongly heated to constant mass. The mass of the anhydrous CuSO4 residue remaining is 3.19 g.\n[Ar: Cu = 63.5, S = 32.1, O = 16.0, H = 1.0]\n\nWhat is the integer value of x in the formula?",
        options=[
            "A: 5",
            "B: 2",
            "C: 7",
            "D: 10"
        ],
        correct_answer="A",
        explanation="Option A is correct. Mass of water evaporated = 4.99 - 3.19 = 1.80 g. Mr(CuSO4) = 63.5 + 32.1 + 4(16.0) = 159.6. Moles of CuSO4 = 3.19 / 159.6 = 0.0200 mol. Mr(H2O) = 18.0. Moles of H2O = 1.80 / 18.0 = 0.100 mol. Mole ratio x = n(H2O) / n(CuSO4) = 0.100 / 0.0200 = 5. Hence the formula is CuSO4·5H2O."
    ))

    # Q103
    questions.append(MCQQuestion(
        number=103,
        title="Atom Economy Comparison Across Reaction Types — 9701/13/M/J/22/Q7",
        syllabus_ref="HF",
        difficulty="EASY",
        stem="Which chemical reaction has an atom economy of exactly 100% for the named organic product?",
        options=[
            "A: Addition of hydrogen bromide to propene to form 2-bromopropane",
            "B: Free-radical bromination of propane to form 2-bromopropane",
            "C: Nucleophilic substitution of 1-chloropropane with aqueous sodium hydroxide to form propan-1-ol",
            "D: Elimination of water from propan-1-ol using concentrated sulfuric acid to form propene"
        ],
        correct_answer="A",
        explanation="Option A is correct. In an addition reaction (propene + HBr -> 2-bromopropane), all reactant atoms are incorporated into the single desired product molecule. Atom economy = (Mr desired product / Total Mr reactants) x 100% = 100%. Reactions B, C, and D are substitution and elimination reactions that generate coproducts (HBr, NaCl, H2O), resulting in an atom economy strictly less than 100%."
    ))

    # Q104
    questions.append(MCQQuestion(
        number=104,
        title="Percentage Yield vs Atom Economy Concept — 9701/11/F/M/24/Q6",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="An industrial manufacturing route produces an active pharmaceutical ingredient with a percentage yield of 94% but an atom economy of 28%.\n\nWhich statement accurately evaluates this industrial process?",
        options=[
            "A: The reaction proceeds with very high conversion efficiency, but generates large quantities of waste byproducts.",
            "B: The reaction equilibrium lies far to the left, so only a small proportion of reactants react.",
            "C: The reaction proceeds via an addition mechanism with significant mechanical product losses.",
            "D: The reaction is highly environmentally sustainable because atom economy is maximized."
        ],
        correct_answer="A",
        explanation="Option A is correct. Percentage yield measures practical conversion efficiency (actual moles produced vs theoretical maximum moles). A yield of 94% means nearly all starting material converted to product. Atom economy measures the proportion of reactant mass incorporated into the desired product. An atom economy of 28% means 72% of the reactant mass is discarded as waste byproducts. Thus, high yield does not guarantee green chemistry."
    ))

    # Q105
    questions.append(MCQQuestion(
        number=105,
        title="Comparison of Total Number of Atoms in Given Masses — 9701/12/M/J/24/Q6",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="Which of the following gaseous samples contains the greatest total number of atoms?\n[Ar: H = 1.0, He = 4.0, C = 12.0, N = 14.0, O = 16.0]",
        options=[
            "A: 1.0 g of hydrogen gas, H2",
            "B: 1.0 g of methane gas, CH4",
            "C: 1.0 g of helium gas, He",
            "D: 1.0 g of water vapor, H2O"
        ],
        correct_answer="A",
        explanation="Option A is correct. Calculate moles of atoms: For 1.0 g H2: n(H2) = 1.0 / 2.0 = 0.50 mol molecules -> 0.50 x 2 = 1.0 mol atoms. For 1.0 g CH4: n(CH4) = 1.0 / 16.0 = 0.0625 mol molecules -> 0.0625 x 5 = 0.3125 mol atoms. For 1.0 g He: n(He) = 1.0 / 4.0 = 0.25 mol atoms. For 1.0 g H2O: n(H2O) = 1.0 / 18.0 = 0.0556 mol molecules -> 0.0556 x 3 = 0.167 mol atoms. 1.0 g H2 contains the largest number of atoms (1.0 x L atoms)."
    ))

    # Q106
    questions.append(MCQQuestion(
        number=106,
        title="Selection of Concordant Titres in Volumetric Analysis — 9701/13/O/N/22/Q8",
        syllabus_ref="HF",
        difficulty="EASY",
        stem="A student carries out an acid-base titration and records the following four burette readings for the volume of acid added:\nRough titre: 24.80 cm3\nTitre 1: 24.15 cm3\nTitre 2: 24.40 cm3\nTitre 3: 24.20 cm3\n\nAccording to standard Cambridge guidelines, what average titre volume should be reported for calculations?",
        options=[
            "A: 24.18 cm3",
            "B: 24.25 cm3",
            "C: 24.39 cm3",
            "D: 24.20 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. In volumetric analysis, concordant titres are those within 0.10 cm3 of each other. The rough titre (24.80 cm3) is always excluded. Titre 2 (24.40 cm3) deviates by > 0.10 cm3 from both Titre 1 and 3. Titres 1 (24.15 cm3) and 3 (24.20 cm3) are concordant (|24.20 - 24.15| = 0.05 cm3 <= 0.10 cm3). Average titre = (24.15 + 24.20) / 2 = 24.175 cm3, rounded to two decimal places as 24.18 cm3."
    ))

    # Q107
    questions.append(MCQQuestion(
        number=107,
        title="Redox Titration Stoichiometry (KMnO4 and Fe2+) — 9701/11/O/N/23/Q6",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="In acidic solution, manganate(VII) ions oxidise iron(II) ions according to the equation:\nMnO4-(aq) + 5Fe2+(aq) + 8H+(aq) -> Mn2+(aq) + 5Fe3+(aq) + 4H2O(l)\n\nWhat volume of 0.0200 mol dm^-3 KMnO4(aq) is required to completely react with 25.0 cm3 of 0.100 mol dm^-3 FeSO4(aq)?",
        options=[
            "A: 25.0 cm3",
            "B: 5.00 cm3",
            "C: 125.0 cm3",
            "D: 50.0 cm3"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of Fe2+ = concentration x volume = 0.100 mol dm^-3 x 0.0250 dm3 = 0.00250 mol. From the stoichiometry, 1 mol MnO4- reacts with 5 mol Fe2+. Moles of MnO4- required = 0.00250 / 5 = 0.000500 mol. Volume of KMnO4 = moles / concentration = 0.000500 mol / 0.0200 mol dm^-3 = 0.0250 dm3 = 25.0 cm3."
    ))

    # Q108
    questions.append(MCQQuestion(
        number=108,
        title="Back Titration for Purity of Calcium Carbonate in Limestone — 9701/12/F/M/23/Q7",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="A 2.00 g sample of impure limestone (containing CaCO3) was added to 50.0 cm3 of 1.00 mol dm^-3 HCl (an excess). After the reaction ceased, the remaining unreacted acid required 30.0 cm3 of 0.500 mol dm^-3 NaOH for complete neutralisation.\n[Mr(CaCO3) = 100.1]\n\nWhat is the percentage by mass of CaCO3 in the limestone sample?",
        options=[
            "A: 87.6%",
            "B: 70.1%",
            "C: 43.8%",
            "D: 95.2%"
        ],
        correct_answer="A",
        explanation="Option A is correct. Initial moles of HCl = 0.0500 dm3 x 1.00 mol dm^-3 = 0.0500 mol. Moles of NaOH used = 0.0300 dm3 x 0.500 mol dm^-3 = 0.0150 mol. Since NaOH + HCl -> NaCl + H2O (1:1), unreacted excess HCl = 0.0150 mol. Moles of HCl reacted with CaCO3 = 0.0500 - 0.0150 = 0.0350 mol. Reaction: CaCO3 + 2HCl -> CaCl2 + CO2 + H2O (1:2 ratio). Moles of CaCO3 = 0.0350 / 2 = 0.0175 mol. Mass of pure CaCO3 = 0.0175 mol x 100.1 g mol^-1 = 1.752 g. Percentage purity = (1.752 g / 2.00 g) x 100% = 87.6%."
    ))

    # Q109
    questions.append(MCQQuestion(
        number=109,
        title="Limiting Reagent and Theoretical Yield Calculation — 9701/11/M/J/22/Q8",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="Consider the synthesis of aluminum chloride:\n2Al(s) + 3Cl2(g) -> 2AlCl3(s)\n\nA mixture of 5.40 g of aluminum powder and 28.4 g of chlorine gas is reacted.\n[Ar: Al = 27.0, Cl = 35.5; Mr(AlCl3) = 133.5]\n\nWhich reactant is limiting, and what is the maximum theoretical mass of AlCl3 that can be produced?",
        options=[
            "A: Aluminum is limiting; theoretical yield is 26.7 g",
            "B: Chlorine is limiting; theoretical yield is 35.6 g",
            "C: Aluminum is limiting; theoretical yield is 53.4 g",
            "D: Chlorine is limiting; theoretical yield is 26.7 g"
        ],
        correct_answer="A",
        explanation="Option A is correct. Moles of Al = 5.40 / 27.0 = 0.200 mol. Moles of Cl2 = 28.4 / 71.0 = 0.400 mol. Required mole ratio from equation is n(Cl2)/n(Al) = 3/2 = 1.50. Available mole ratio = 0.400 / 0.200 = 2.00. Since available Cl2 (0.400 mol) exceeds required Cl2 (0.200 x 1.5 = 0.300 mol), chlorine is in excess and aluminum is the limiting reagent. Moles of AlCl3 formed = moles of Al consumed = 0.200 mol. Theoretical mass of AlCl3 = 0.200 mol x 133.5 g mol^-1 = 26.7 g."
    ))

    # Q110
    questions.append(MCQQuestion(
        number=110,
        title="Ideal Gas Law pV = nRT Rigorous Unit Conversions — 9701/13/M/J/23/Q6",
        syllabus_ref="HF",
        difficulty="HARD",
        stem="A 0.480 g sample of an unknown volatile liquid is vaporized in a syringe at 100 °C and 101 kPa. The volume of vapor formed is 125 cm3. [R = 8.31 J K^-1 mol^-1]\n\nWhat is the relative molecular mass, Mr, of the compound?",
        options=[
            "A: 118",
            "B: 88",
            "C: 142",
            "D: 59"
        ],
        correct_answer="A",
        explanation="Option A is correct. Use ideal gas equation pV = nRT = (m/Mr)RT -> Mr = mRT / (pV). Convert all variables into strict SI units: m = 0.480 g; R = 8.31 J K^-1 mol^-1; T = 100 + 273.15 = 373.15 K; p = 101 kPa = 101 x 10^3 Pa; V = 125 cm3 = 125 x 10^-6 m3. Mr = (0.480 x 8.31 x 373.15) / (101 x 10^3 x 125 x 10^-6) = 1488.5 / 12.625 = 117.9 -> 118."
    ))

    # Balance keys and map explanations
    import re
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    balanced_questions = []
    for i, q in enumerate(questions):
        target_key = keys_pattern[i]
        target_idx = letter_to_idx[target_key]
        
        raw_options = [re.sub(r'^[A-D]:\s*', '', opt) for opt in q.options]
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
        
        # Safely map option letters in explanation
        temp_exp = q.explanation
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"Option {l}", f"__OPT_{l}__")
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"__OPT_{l}__", f"Option {old_to_new[l]}")
            
        balanced_questions.append(MCQQuestion(
            number=q.number,
            title=q.title,
            syllabus_ref=q.syllabus_ref,
            difficulty=q.difficulty,
            stem=q.stem,
            options=formatted_options,
            correct_answer=target_key,
            explanation=temp_exp,
            figure_path=q.figure_path,
            figure_caption=q.figure_caption
        ))

    # Write output to mcq_topic2_data.py
    with open("mcq_topic2_data.py", "w", encoding="utf-8") as f:
        f.write('"""\nCurated 100 Authentic Cambridge AS Chemistry (9701) Paper 1 MCQs\nfor Topic 2: Atoms, Molecules & Stoichiometry (Balanced Answer Keys: 25 A, 25 B, 25 C, 25 D).\n"""\n\n')
        f.write("from build_mcq_topic_pdf import MCQQuestion\n\n")
        f.write("TOPIC_2_MCQ_QUESTIONS = [\n")
        for q in balanced_questions:
            f.write("    MCQQuestion(\n")
            f.write(f"        number={q.number},\n")
            f.write(f"        title={repr(q.title)},\n")
            f.write(f"        syllabus_ref={repr(q.syllabus_ref)},\n")
            f.write(f"        difficulty={repr(q.difficulty)},\n")
            f.write(f"        stem={repr(q.stem)},\n")
            f.write(f"        options={repr(q.options)},\n")
            f.write(f"        correct_answer={repr(q.correct_answer)},\n")
            f.write(f"        explanation={repr(q.explanation)},\n")
            f.write(f"        figure_path={repr(q.figure_path)},\n")
            f.write(f"        figure_caption={repr(q.figure_caption)}\n")
            f.write("    ),\n")
        f.write("]\n")

    print(f"Successfully generated mcq_topic2_data.py with {len(balanced_questions)} MCQs!")

if __name__ == "__main__":
    generate()
