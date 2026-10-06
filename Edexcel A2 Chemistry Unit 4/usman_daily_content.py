"""
usman_daily_content.py
Comprehensive Daily Syllabus Content for Usman (Grade A* Scholar)
Edexcel International Advanced Level Chemistry — Unit 4 (WCH14)
Timeline: 07 October 2026 to 15 January 2027 (101 Days, 15 Weeks)
Core Teaching Finished by 26 December 2026 (20 Days Buffer before Exam)
"""

import datetime

WEEKS_META = [
    {
        "week": 1,
        "date_range": "07 Oct 2026 – 11 Oct 2026",
        "title": "TOPIC 11A: FURTHER KINETICS — PART 1",
        "focus": "Rate Measurement Techniques, Initial Rates & Rate Equations (11A.1, 11A.2)",
        "objective": "Master continuous vs sampling rate measurement techniques (colorimetry, gas volume, titrimetry, quenching, conductimetry, dilatometry) and formulate rate equations with precise units of k.",
        "checklist": [
            "Understand why colorimeters measure absorbance and the Beer-Lambert linear range.",
            "Compare gas syringe vs loss-in-mass for light (H2) vs dense (CO2) gases.",
            "Explain quenching methods: cooling, dilution, and chemical neutralisation.",
            "Formulate rate equations: rate = k[A]^m[B]^n and deduce units of k.",
            "Complete Saturday Topical Test 1 on 11A.1 & 11A.2.",
            "Review test results and log any missed mark scheme points on Sunday."
        ],
        "test_title": "TOPICAL TEST 1: Rate Measurement & Rate Laws (40 Marks, 45 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_11A1_Rate_Measurement.pdf & 11A2_Rate_Equations.pdf"
    },
    {
        "week": 2,
        "date_range": "12 Oct 2026 – 18 Oct 2026",
        "title": "TOPIC 11A: FURTHER KINETICS — PART 2",
        "focus": "Determining Orders, Graphical Methods & Mechanisms (11A.3, 11A.4)",
        "objective": "Deduce reaction orders from concentration-time tangents, half-life constancy (t½ = ln2/k), integrated rate laws, and evaluate multi-step mechanisms against experimental rate equations.",
        "checklist": [
            "Draw tangents at t = 0 to obtain initial rates accurately.",
            "Verify first-order kinetics by demonstrating at least two consecutive constant half-lives.",
            "Distinguish linear plots: [A] vs t (zero order), ln[A] vs t (1st order), 1/[A] vs t (2nd order).",
            "Identify the rate-determining step (RDS) from orders in experimental rate laws.",
            "Contrast SN1 (unimolecular RDS, carbocation, racemate) vs SN2 (bimolecular, Walden inversion).",
            "Complete Saturday Topical Test 2 on 11A.3 & 11A.4."
        ],
        "test_title": "TOPICAL TEST 2: Determining Orders & Mechanisms (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_11A3_Determining_Orders.pdf & 11A4_Mechanisms.pdf"
    },
    {
        "week": 3,
        "date_range": "19 Oct 2026 – 25 Oct 2026",
        "title": "TOPIC 11A: FURTHER KINETICS — PART 3",
        "focus": "Activation Energy, Catalysis & The Arrhenius Equation (11A.5, 11A.6)",
        "objective": "Explain temperature and catalytic effects using Maxwell-Boltzmann distributions and calculate activation energy and pre-exponential factors using the Arrhenius equation.",
        "checklist": [
            "Draw Maxwell-Boltzmann distribution curves at T1 and T2 showing the rightward/downward peak shift.",
            "Explain heterogeneous catalysis via the 5-step adsorption-reaction-desorption theory.",
            "Contrast homogeneous (Fe²⁺/Fe³⁺ redox) vs heterogeneous (Pt/Rh catalytic converter) mechanisms.",
            "Linearise the Arrhenius equation: ln k = -Ea/RT + ln A and calculate gradient = -Ea/R.",
            "Calculate Ea from two temperature points using ln(k2/k1) = (Ea/R)(1/T1 - 1/T2).",
            "Complete Saturday Topical Test 3 on 11A.5 & 11A.6."
        ],
        "test_title": "TOPICAL TEST 3: Activation Energy & Arrhenius Equation (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_11A5_Activation_Energy.pdf & 11A6_Arrhenius_Equation.pdf"
    },
    {
        "week": 4,
        "date_range": "26 Oct 2026 – 01 Nov 2026",
        "title": "TOPIC 11 SYNOPTIC MASTERY & TOPIC 12A: ENTROPY",
        "focus": "Topic 11 Grand Exam & Introduction to System and Total Entropy (12A.1, 12A.2)",
        "objective": "Achieve full exam mastery on Topic 11 Kinetics and begin Topic 12 by calculating standard system entropy changes and total entropy for spontaneous processes.",
        "checklist": [
            "Sit the Grand Topic 11 Examination (50 Questions, 90 Marks) under strict exam conditions.",
            "Understand entropy as a measure of dispersal of energy and microstates.",
            "Predict sign of ΔS_system from changes in state and number of moles of gas.",
            "Calculate ΔS_system = ΣS(products) - ΣS(reactants) using tabulated standard molar entropy values.",
            "Calculate ΔS_surroundings = -ΔH/T with precise unit conversions (kJ to J).",
            "State the Second Law of Thermodynamics: ΔS_total = ΔS_system + ΔS_surroundings > 0."
        ],
        "test_title": "GRAND TOPIC 11 EXAM: Complete Further Kinetics (50 Qs, 90 Marks, 90 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf"
    },
    {
        "week": 5,
        "date_range": "02 Nov 2026 – 08 Nov 2026",
        "title": "TOPIC 12A & 12B: FEASIBILITY & BORN-HABER CYCLES",
        "focus": "Spontaneity, Crossover Temperature & Lattice Enthalpy (12A.3, 12B.1)",
        "objective": "Determine thermodynamic feasibility conditions (ΔS_total > 0), calculate crossover temperatures, and construct Born-Haber cycles for Group 1 and Group 2 halides and oxides.",
        "checklist": [
            "Calculate temperature at which a non-spontaneous reaction becomes feasible (T = ΔH / ΔS_system).",
            "Explain why thermodynamically feasible reactions (ΔS_total > 0) may not occur at room temperature (kinetic stability).",
            "Define standard enthalpy of atomisation, electron affinity, and lattice energy.",
            "Construct and calculate Born-Haber cycles for NaCl, MgCl2, and CaO.",
            "Distinguish exothermic lattice formation enthalpy from endothermic lattice dissociation enthalpy.",
            "Complete Saturday Topical Test 5 on Entropy & Born-Haber Cycles."
        ],
        "test_title": "TOPICAL TEST 5: Entropy & Born-Haber Cycles (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_12A_Entropy.pdf & 12B1_Lattice_Energy_Born_Haber.pdf"
    },
    {
        "week": 6,
        "date_range": "09 Nov 2026 – 15 Nov 2026",
        "title": "TOPIC 12B: ENERGETICS & SOLUTION CHEMISTRY",
        "focus": "Theoretical vs Experimental Lattice Energies & Solution Enthalpies (12B.2, 12B.3)",
        "objective": "Evaluate the ionic model using Fajans' polarisation rules and relate enthalpy changes of solution and hydration to Group 2 solubility trends.",
        "checklist": [
            "Explain discrepancies between experimental (Born-Haber) and theoretical (Born-Landé) lattice energies.",
            "Apply Fajans' rules to explain covalent character in compounds such as AgCl, AgI, and AlCl3.",
            "Define standard enthalpy of solution (Δ_sol H) and enthalpy of hydration (Δ_hyd H).",
            "Construct Hess's Law cycles linking Δ_sol H, Δ_hyd H(cations), Δ_hyd H(anions), and lattice energy.",
            "Explain solubility trends down Group 2 sulfates and hydroxides in terms of hydration vs lattice energy.",
            "Sit the Grand Topic 12 Examination (50 Questions, 90 Marks)."
        ],
        "test_title": "GRAND TOPIC 12 EXAM: Complete Entropy & Energetics (50 Qs, 90 Marks, 90 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf"
    },
    {
        "week": 7,
        "date_range": "16 Nov 2026 – 22 Nov 2026",
        "title": "TOPIC 13A: CHEMICAL EQUILIBRIA — PART 1",
        "focus": "Equilibrium Constants Kc & Kp, Calculations & Units (13A.1, 13A.2)",
        "objective": "Construct and calculate equilibrium constants Kc and Kp for homogeneous and heterogeneous equilibria using ICE tables, mole fractions, and partial pressures.",
        "checklist": [
            "Write Kc expressions with square brackets and deduce units for any reaction.",
            "Construct ICE tables (Initial, Change, Equilibrium) to calculate equilibrium concentrations.",
            "Write Kp expressions using partial pressures (pA) and deduce units (Pa, kPa, atm).",
            "Calculate mole fractions xA = nA / n_total and partial pressures pA = xA × P_total.",
            "Explain why pure solids and pure liquids are omitted from heterogeneous equilibrium expressions.",
            "Complete Saturday Topical Test 7 on Kc and Kp."
        ],
        "test_title": "TOPICAL TEST 7: Chemical Equilibria Kc & Kp (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_13A1_Equilibrium_Kc.pdf & 13A2_Equilibrium_Kp.pdf"
    },
    {
        "week": 8,
        "date_range": "23 Nov 2026 – 29 Nov 2026",
        "title": "TOPIC 13A: EQUILIBRIA & TOPIC 14A: BRØNSTED-LOWRY",
        "focus": "Factors Affecting K, ΔS_total = R ln K & Brønsted-Lowry Theory (13A.3–13A.5, 14A.1)",
        "objective": "Understand why temperature is the ONLY factor altering K, relate K to total entropy change (ΔS_total = R ln K), and introduce Brønsted-Lowry acid-base conjugate pairs.",
        "checklist": [
            "Explain why temperature alters Kc and Kp for exothermic vs endothermic reactions.",
            "Explain why changes in pressure, concentration, or catalysts do NOT change Kc or Kp.",
            "Derive and apply ΔS_total = R ln K and K = e^(ΔS_total / R).",
            "Sit the Grand Topic 13 Examination (50 Questions, 90 Marks).",
            "Identify conjugate acid-base pairs in aqueous solutions and non-aqueous systems.",
            "Define amphiprotic/amphoteric species (H2O, HCO3⁻, HSO4⁻)."
        ],
        "test_title": "GRAND TOPIC 13 EXAM: Complete Chemical Equilibria (50 Qs, 90 Marks, 90 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf"
    },
    {
        "week": 9,
        "date_range": "30 Nov 2026 – 06 Dec 2026",
        "title": "TOPIC 14A: STRONG AND WEAK ACIDS",
        "focus": "pH Scale, Kw, Strong Bases & Weak Acid Ka Calculations (14A.2–14A.4)",
        "objective": "Calculate pH for strong monobasic and dibasic acids, evaluate Kw and pure water neutrality at varying temperatures, and calculate weak acid pH using Ka and pKa.",
        "checklist": [
            "Calculate pH = -log[H⁺] and [H⁺] = 10^(-pH) for strong monobasic and dibasic acids.",
            "Use Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ mol² dm⁻⁶ to calculate the pH of strong bases.",
            "Explain why pure water at 50 °C has pH < 7 but remains strictly neutral ([H⁺] = [OH⁻]).",
            "Formulate Ka expressions for weak acids and interconvert Ka and pKa (pKa = -log Ka).",
            "Calculate weak acid pH using [H⁺] = √(Ka × c) and state the two core assumptions.",
            "Complete Saturday Topical Test 9 on Strong & Weak Acids."
        ],
        "test_title": "TOPICAL TEST 9: Strong & Weak Acids, Kw & Ka (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_14A_Strong_Weak_Acids.pdf"
    },
    {
        "week": 10,
        "date_range": "07 Dec 2026 – 13 Dec 2026",
        "title": "TOPIC 14B: TITRATIONS, pH CURVES & BUFFERS",
        "focus": "Titration Curves, Indicator Selection & Buffer Action (14B.1–14B.3)",
        "objective": "Interpret the four acid-base titration curves, select suitable indicators based on pKin, calculate buffer solution pH using Henderson-Hasselbalch, and analyze half-equivalence points.",
        "checklist": [
            "Sketch and annotate pH curves for SA-SB, WA-SB, SA-WB, and WA-WB titrations.",
            "Select indicators (methyl orange vs phenolphthalein) matching the vertical equivalence range.",
            "Define buffer solutions and explain the mechanism of resistance to pH changes.",
            "Calculate acidic and basic buffer pH using Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA]).",
            "Show that at the half-equivalence point in a weak acid titration, pH = pKa.",
            "Sit the Grand Topic 14 Examination (50 Questions, 90 Marks)."
        ],
        "test_title": "GRAND TOPIC 14 EXAM: Acid-Base Equilibria & Buffers (50 Qs, 90 Marks, 90 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_14B_Acid_Base_Titrations_Buffers.pdf"
    },
    {
        "week": 11,
        "date_range": "14 Dec 2026 – 20 Dec 2026",
        "title": "TOPIC 15A & 15B: CHIRALITY & CARBONYLS",
        "focus": "Optical Activity, Carbonyl Physical Properties & Redox Reactions (15A.1–15A.3, 15B.1–15B.2)",
        "objective": "Identify chiral centres, represent 3D enantiomers, explain polarimeter rotation and racemic mixtures, and master oxidation and reduction reactions of aldehydes and ketones.",
        "checklist": [
            "Identify asymmetric carbons and draw 3D tetrahedral enantiomer pairs.",
            "Explain optical activity using plane-polarised light and define racemic mixture.",
            "Relate SN1 (planar carbocation intermediate → racemate) and SN2 (backside attack → inversion).",
            "Explain boiling points of carbonyls (dipole-dipole, no intermolecular H-bonding between molecules).",
            "Differentiate aldehydes and ketones using Tollens' (silver mirror) and Fehling's (brick-red Cu2O).",
            "Complete Saturday Topical Test 11 on Chirality & Carbonyls."
        ],
        "test_title": "TOPICAL TEST 11: Chirality, Optical Activity & Carbonyls (60 Marks, 60 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_15A_Chirality.pdf & 15B_Carbonyl_Compounds.pdf"
    },
    {
        "week": 12,
        "date_range": "21 Dec 2026 – 26 Dec 2026",
        "title": "TOPIC 15C, 15D, 15E: CARBOXYLIC DERIVATIVES & SPECTROSCOPY",
        "focus": "Acyl Chlorides, Esters, Polyesters, Chromatography & NMR (15C–15E) — SYLLABUS COMPLETION!",
        "objective": "Master carboxylic acid derivatives, polyester condensation polymerisation, chromatography (TLC, GC-MS), and high-resolution 1H/13C NMR structural elucidation to finish the entire Unit 4 syllabus.",
        "checklist": [
            "Draw curly arrow nucleophilic addition mechanism of HCN to carbonyls forming hydroxynitriles.",
            "Recall 2,4-DNPH (Brady's orange precipitate) and tri-iodomethane iodoform test (CHI3 yellow crystals).",
            "Compare reactivity of acyl chlorides (vigorous with H2O/ROH/NH3/amines) vs carboxylic acids.",
            "Contrast acid hydrolysis (reversible) vs alkaline saponification (irreversible) of esters.",
            "Interpret high-resolution 1H NMR: chemical shifts, integration ratios, and n+1 splitting patterns.",
            "Sit the Grand Topic 15 Examination — CORE TEACHING 100% COMPLETE 20 DAYS BEFORE EXAM!"
        ],
        "test_title": "GRAND TOPIC 15 EXAM: Organic Chemistry & Spectroscopy (50 Qs, 90 Marks, 90 mins)",
        "test_resource": "Usman_Edexcel_Chem_U4_15D_Carboxylic_Acid_Derivatives.pdf & 15E_Spectroscopy_Chromatography.pdf"
    },
    {
        "week": 13,
        "date_range": "27 Dec 2026 – 02 Jan 2027",
        "title": "MOCK EXAM MARATHON: PART 1 (20 DAYS TO EXAM)",
        "focus": "Full Unit 4 Timed Mocks 1, 2, 3 & Deep Remedial Calculation Drills",
        "objective": "Execute full-length Pearson Edexcel IAL Unit 4 (WCH14/01) past paper papers under strict 90-minute timed conditions, auditing marks against official examiner reports.",
        "checklist": [
            "Complete Official Past Paper Mock 1: WCH14/01 Jan 2021 (Target: 80+/90).",
            "Perform line-by-line mark scheme audit and log every lost mark in the A* Error Registry.",
            "Complete Official Past Paper Mock 2: WCH14/01 Jun 2021 under timed exam conditions.",
            "Conduct targeted remedial drills on ICE equilibrium tables and buffer calculations.",
            "Complete Official Past Paper Mock 3: WCH14/01 Oct 2021.",
            "Complete Official Past Paper Mock 4: WCH14/01 Jan 2022 on Saturday."
        ],
        "test_title": "MOCK EXAM 4: WCH14/01 Jan 2022 Official Paper (90 Marks, 90 mins)",
        "test_resource": "Official Pearson Edexcel IAL Past Paper WCH14/01 Jan 2022"
    },
    {
        "week": 14,
        "date_range": "03 Jan 2027 – 09 Jan 2027",
        "title": "MOCK EXAM MARATHON: PART 2 (FINAL 12 DAYS)",
        "focus": "Full Unit 4 Timed Mocks 5, 6, 7, 8 & Advanced Spectroscopic Elucidation",
        "objective": "Advance exam stamina and speed, perfecting multi-spectra organic identification (IR + Mass Spec + 13C NMR + 1H NMR) and complex thermodynamics questions.",
        "checklist": [
            "Complete Official Past Paper Mock 5: WCH14/01 Jun 2022 (Target: 82+/90).",
            "Drill multi-spectral structure deduction problems without reference to data tables.",
            "Complete Official Past Paper Mock 6: WCH14/01 Oct 2022.",
            "Refine Born-Haber cycle and lattice energy polarisability written justifications.",
            "Complete Official Past Paper Mock 7: WCH14/01 Jan 2023.",
            "Complete Official Past Paper Mock 8: WCH14/01 Jun 2023 on Saturday."
        ],
        "test_title": "MOCK EXAM 8: WCH14/01 Jun 2023 Official Paper (90 Marks, 90 mins)",
        "test_resource": "Official Pearson Edexcel IAL Past Paper WCH14/01 Jun 2023"
    },
    {
        "week": 15,
        "date_range": "10 Jan 2027 – 15 Jan 2027",
        "title": "FINAL PREDICTOR MOCKS, EXAMINER TRAP REVIEW & EXAM DAY",
        "focus": "Predictor Mocks, Top 50 Examiner Traps, Formula Sheet Polish & Exam Day!",
        "objective": "Finalise exam strategy, eliminate all residual examiner traps, achieve peak cognitive condition, and sit the official Pearson Edexcel IAL Chemistry Unit 4 exam for a confirmed A*.",
        "checklist": [
            "Complete Official Past Paper Mock 9: WCH14/01 Oct 2023.",
            "Complete Final Predictor Mock 10: WCH14/01 Jan 2024 / Jun 2024 (Target: 85+/90).",
            "Review the Mentora 50 Empirical Examiner Traps & Model Answers document.",
            "Inspect physical stationery: approved scientific calculator, HB pencils, black ink pens, ruler.",
            "Rest, hydrate, and maintain calm confidence on Thursday evening.",
            "SIT THE OFFICIAL EXAM ON FRIDAY, 15 JANUARY 2027 — ACHIEVE GRADE A* (100% UMS)!"
        ],
        "test_title": "OFFICIAL EXAM: PEARSON EDEXCEL IAL UNIT 4 (WCH14/01)",
        "test_resource": "Official Examination Paper (WCH14/01) — 90 Marks, 1 Hour 30 Minutes"
    }
]

# Helper to generate daily content programmatically with explicit rich chemistry detail
def get_daily_content(day_num, date_obj):
    day_name = date_obj.strftime("%A")
    date_str = date_obj.strftime("%A, %d %B %Y")
    
    # PHASE 2: Mock Exam Marathon (Days 82 to 101, Dec 27 to Jan 15)
    if day_num >= 82:
        return _get_phase2_content(day_num, date_str, day_name)
    
    # PHASE 1: Core Syllabus Teaching & Weekly Testing (Days 1 to 81, Oct 7 to Dec 26)
    if day_name == "Saturday":
        return _get_saturday_test_content(day_num, date_str)
    elif day_name == "Sunday":
        return _get_sunday_review_content(day_num, date_str)
    else:
        return _get_teaching_content(day_num, date_str)

def _get_saturday_test_content(day_num, date_str):
    test_map = {
        4: ("TOPICAL TEST 1: Rate Measurement Techniques & Rate Equations", "11A.1 & 11A.2", 40, 45, "Usman_Edexcel_Chem_U4_11A1_Rate_Measurement.pdf & 11A2_Rate_Equations.pdf"),
        11: ("TOPICAL TEST 2: Determining Orders & Reaction Mechanisms", "11A.3 & 11A.4", 60, 60, "Usman_Edexcel_Chem_U4_11A3_Determining_Orders.pdf & 11A4_Mechanisms.pdf"),
        18: ("TOPICAL TEST 3: Activation Energy & Arrhenius Equation", "11A.5 & 11A.6", 60, 60, "Usman_Edexcel_Chem_U4_11A5_Activation_Energy.pdf & 11A6_Arrhenius_Equation.pdf"),
        25: ("GRAND TOPIC 11 EXAM: Complete Further Kinetics Mastery", "Topic 11 (11A.1–11A.6)", 90, 90, "Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf"),
        32: ("TOPICAL TEST 5: Entropy, Spontaneity & Born-Haber Cycles", "12A.1–12A.3, 12B.1", 60, 60, "Usman_Edexcel_Chem_U4_12A_Entropy.pdf & 12B1_Lattice_Energy_Born_Haber.pdf"),
        39: ("GRAND TOPIC 12 EXAM: Complete Entropy & Energetics", "Topic 12 (12A & 12B)", 90, 90, "Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf"),
        46: ("TOPICAL TEST 7: Chemical Equilibria Kc & Kp", "13A.1–13A.3", 60, 60, "Usman_Edexcel_Chem_U4_13A1_Equilibrium_Kc.pdf & 13A2_Equilibrium_Kp.pdf"),
        53: ("GRAND TOPIC 13 EXAM: Complete Chemical Equilibria", "Topic 13 (13A.1–13A.5)", 90, 90, "Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf"),
        60: ("TOPICAL TEST 9: Strong & Weak Acids, Kw & Ka Calculations", "14A.1–14A.4", 60, 60, "Usman_Edexcel_Chem_U4_14A_Strong_Weak_Acids.pdf"),
        67: ("GRAND TOPIC 14 EXAM: Acid-Base Equilibria, Titrations & Buffers", "Topic 14 (14A & 14B)", 90, 90, "Usman_Edexcel_Chem_U4_14B_Acid_Base_Titrations_Buffers.pdf"),
        74: ("TOPICAL TEST 11: Chirality, Optical Activity & Carbonyl Chemistry", "15A & 15B", 60, 60, "Usman_Edexcel_Chem_U4_15A_Chirality.pdf & 15B_Carbonyl_Compounds.pdf"),
        81: ("GRAND TOPIC 15 EXAM: Organic Synthesis, Derivatives & Spectroscopy", "Topic 15 (15A–15E)", 90, 90, "Usman_Edexcel_Chem_U4_15D_Carboxylic_Acid_Derivatives.pdf & 15E_Spectroscopy_Chromatography.pdf")
    }
    title, sub, marks, time_m, res = test_map.get(day_num, ("WEEKLY SATURDAY TOPICAL TEST", "Unit 4 Content", 60, 60, "Usman Mentora Exam Pack"))
    return {
        "day": day_num,
        "date_str": date_str,
        "day_type": "SATURDAY_TEST",
        "topic_code": f"Weekly Assessment — {sub}",
        "subtopic": title,
        "learning_objective": f"Execute a strict timed examination simulation under official Pearson Edexcel conditions ({marks} marks, {time_m} minutes).",
        "what_to_learn": [
            f"(1) Examination conditions: Sit test in absolute silence with only an approved scientific calculator, data booklet, and black ink pen.",
            f"(2) Pacing strategy: Allocate exactly 1 minute per mark; leave 10 minutes at the end for rigorous numerical and unit checks.",
            f"(3) High-yield focus: Show every intermediate step in calculations; examiners deduct method marks if unrounded values are missing.",
            f"(4) Graphical questions: Always draw tangents with a sharp pencil and construct a large gradient triangle covering >= 50% of the line.",
            f"(5) Organic questions: Clearly draw all bonds, lone pairs, and non-superimposable 3D wedged/dashed conventions where required.",
            f"(6) Mark target: A* standard benchmark is >= 85% raw score."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates lose 3-4 marks per paper by omitting units on rate constants k, lattice energies, and entropy changes.",
            "Always state chemical equations with state symbols when requested in Energetics and Equilibria questions.",
            "In mechanism questions, ensure curly arrows start PRECISELY from a lone pair or the center of a covalent bond.",
            "Do not round intermediate answers on your calculator; round only the final answer to 2 or 3 significant figures.",
            "Audit every 6-mark extended response against the three Level 3 indicative scientific content descriptors."
        ],
        "resources": res,
        "self_assessment": [
            f"Completed {marks}-mark timed test in {time_m} mins without notes",
            "Self-assessed or teacher-assessed against official mark scheme",
            "Entered every lost mark and specific misconception into A* Error Registry"
        ]
    }

def _get_sunday_review_content(day_num, date_str):
    return {
        "day": day_num,
        "date_str": date_str,
        "day_type": "SUNDAY_CONSOLIDATION",
        "topic_code": "Weekly Consolidation & Remedial Analysis",
        "subtopic": "Error Registry Audit, Flashcard Review & Cognitive Reset",
        "learning_objective": "Perform deep error logging on Saturday's test, re-attempt missed problems from first principles, and reinforce active recall.",
        "what_to_learn": [
            "(1) Error Taxonomy: Classify every lost mark into (A) Conceptual Gap, (B) Calculation/Unit Error, or (C) Examiner Keyword Omission.",
            "(2) Redo without mark scheme: Re-attempt every question where marks were dropped from a completely blank sheet.",
            "(3) Active Recall: Review Section D Examiner FAQs from the Mentora packs covering this week's sub-topics.",
            "(4) Flashcard deck review: Test active recall of all chemical definitions, Arrhenius/entropy/buffer formulas, and reagents.",
            "(5) Organic reaction map: Trace all interconversions and mechanism pathways covered so far on a single A3 whiteboard or paper.",
            "(6) Rest and recovery: Complete focused review in 2 hours, then enjoy physical exercise and mental relaxation for the upcoming week."
        ],
        "how_to_outstand": [
            "The difference between Grade A (80%) and Grade A* (90%+) is the rigor of post-test error analysis.",
            "Never simply 'read' the mark scheme and think 'I knew that' — write out the full model response independently.",
            "Memorise the exact examiner wording: e.g. 'high temperature denatures' vs 'destroys', 'equilibrium shifts' vs 'Kc changes'.",
            "Maintain an updated physical or digital formula sheet containing all Unit 4 thermodynamic and kinetic formulas."
        ],
        "resources": "Mentora Unit 4 Examiner FAQ Repository & Student Personal Error Registry",
        "self_assessment": [
            "Logged every lost mark from Saturday's test into Error Registry",
            "Re-solved all missed questions independently with 100% accuracy",
            "Reviewed flashcards and feel confident for the upcoming week"
        ]
    }

# Complete teaching day content library
TEACHING_DAYS = {
    1: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.1)",
        "subtopic": "Continuous Rate Monitoring: Colorimetry & Gas Volume",
        "learning_objective": "Master continuous experimental techniques for measuring reaction rates, focusing on colorimetry and gas syringe collection.",
        "what_to_learn": [
            "(1) Principle of continuous monitoring: measuring physical property changes at regular time intervals without interrupting the reaction.",
            "(2) Colorimetry: measures absorbance of light by a coloured species; absorbance is directly proportional to concentration (Beer-Lambert Law: A = εcl).",
            "(3) Colorimeter filter selection: filter must transmit the wavelength complementary to the colour of the solution (e.g. blue filter for orange Cr2O7²⁻, yellow/green for purple MnO4⁻).",
            "(4) Gas collection using gas syringe: suitable for both light (H2) and dense (CO2, O2) gases; volume measured at regular time intervals.",
            "(5) Loss-in-mass method: conical flask on balance with cotton wool plug (prevents acid spray loss); best for dense gases (CO2, SO2), unsuitable for light H2.",
            "(6) Graphical treatment: plot volume or absorbance against time; gradient of tangent at t = 0 gives initial rate."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates state 'colorimeter measures transmission' — mark schemes insist on ABSORBANCE.",
            "Always state that a calibration curve of known concentrations vs absorbance is required to convert absorbance into mol dm⁻³.",
            "For loss-in-mass with H2: explain why this method fails — H2 has Mr = 2.0, so mass lost is too small to measure on standard 2 d.p. balances.",
            "State why cotton wool is used: prevents liquid spray escaping while allowing gas to vent freely."
        ],
        "resources": "Usman Pack 11A1 Q1–Q15 (Colorimetry and Gas Syringe Methods)"
    },
    2: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.1)",
        "subtopic": "Sampling & Discontinuous Methods: Quenching, Titrimetry & Conductimetry",
        "learning_objective": "Evaluate sampling techniques with quenching, electrical conductivity, dilatometry, and clock reactions.",
        "what_to_learn": [
            "(1) Discontinuous / sampling method: withdrawing aliquots of reaction mixture at recorded times and stopping (quenching) reaction immediately.",
            "(2) Quenching mechanisms: (a) rapid cooling in ice-water bath; (b) large dilution with cold water; (c) chemical quenching (e.g. adding excess NaHCO3 to quench acid-catalysed reactions).",
            "(3) Titrimetric analysis: titrating quenched aliquots (e.g. against standard Na2S2O3 for iodine or standard NaOH for ester hydrolysis).",
            "(4) Electrical conductivity: monitors changes in total ionic concentrations or replacement of high-mobility ions (H⁺, OH⁻) with lower-mobility ions (CH3COO⁻).",
            "(5) Dilatometry: measures small liquid volume contractions/expansions during reaction (common in polymerisation where density increases).",
            "(6) Clock reactions: time taken for a fixed, small amount of reactant to be consumed (e.g. thiosulfate exhaustion in iodine clock); 1/t ∝ initial rate."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates state 1/t IS the initial rate — mark schemes award marks only for stating '1/t is PROPORTIONAL TO initial rate'.",
            "Quenching must be INSTANTANEOUS — explain that without effective quenching, the reaction continues during the titration, invalidating time data.",
            "Conductivity questions: explicitly state WHICH ion is replaced and why conductivity changes (e.g. OH⁻ has high molar ionic conductivity, replaced by bulky ethanoate).",
            "Clock reactions: explain that the method assumes the reaction has progressed by less than 1-2% so concentrations remain essentially constant."
        ],
        "resources": "Usman Pack 11A1 Q16–Q50 & FAQs (Titrimetry, Conductivity, Clock Reactions)"
    },
    3: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.2)",
        "subtopic": "Rate Equations, Rate Constants and Orders of Reaction",
        "learning_objective": "Formulate rate equations, define orders of reaction (0, 1st, 2nd), and deduce units of the rate constant k.",
        "what_to_learn": [
            "(1) General rate equation: rate = k[A]^m[B]^n, where m and n are the orders of reaction with respect to A and B.",
            "(2) Order of reaction definition: the power to which the concentration of a reactant is raised in the experimental rate equation.",
            "(3) Zero order (m = 0): rate is independent of [A]; doubling [A] has no effect on rate (rate = k).",
            "(4) First order (m = 1): rate is directly proportional to [A]; doubling [A] doubles the rate.",
            "(5) Second order (m = 2): rate is proportional to [A]²; doubling [A] quadruples the rate (2² = 4).",
            "(6) Overall order = sum of individual orders (m + n); rate constant k is constant at fixed temperature.",
            "(7) Deducing units of k: divide units of rate (mol dm⁻³ s⁻¹) by units of concentration terms."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Deducing orders from stoichiometric coefficients — orders can ONLY be determined experimentally, never from balanced equations.",
            "Units of k: memorize derivations! Zero order: mol dm⁻³ s⁻¹; 1st order: s⁻¹; 2nd order: dm³ mol⁻¹ s⁻¹; 3rd order: dm⁶ mol⁻² s⁻¹.",
            "Rate constant k changes ONLY with temperature (and catalysts); changing reactant concentration changes rate, but k remains UNCHANGED.",
            "Always show the algebraic cancellation when working out units of k to secure method marks."
        ],
        "resources": "Usman Pack 11A2 Q1–Q50 & FAQs (Rate Equations and Orders)"
    },
    6: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.3)",
        "subtopic": "Determining Orders: Initial Rates Method & Concentration-Time Graphs",
        "learning_objective": "Determine reaction orders using initial rates data tables and analyze concentration-time curves.",
        "what_to_learn": [
            "(1) Initial rate method: varying concentration of one reactant while keeping all other reactant concentrations and temperature constant.",
            "(2) Comparing experimental runs: if [A] changes by factor x and rate changes by factor y, then x^m = y (e.g. 2^m = 4 → m = 2).",
            "(3) Concentration-time graph shapes: zero order gives a straight line with constant negative gradient (gradient = -k).",
            "(4) First order [A]-t curve: exponential decay curve with a constant half-life (t½ independent of concentration).",
            "(5) Second order [A]-t curve: steep initial drop that flattens rapidly; successive half-lives double as concentration halves.",
            "(6) Drawing tangents at t = 0: gradient = Δ[A] / Δt = -(initial rate); construct large triangle for precision."
        ],
        "how_to_outstand": [
            "In data table questions, always write a clear narrative: 'Comparing Exp 1 and 2: [B] is constant, [A] doubles, rate quadruples (2² = 4), therefore 2nd order in A'.",
            "When drawing tangents, ensure the tangent line touches the curve ONLY at t = 0 and does not cross into the curve.",
            "Zero order: rate is k, NOT zero! The gradient is non-zero and negative.",
            "Remember that initial rates avoid complications from reverse reactions or product inhibition."
        ],
        "resources": "Usman Pack 11A3 Q1–Q25 (Initial Rates Tables and [A]-t Graphs)"
    },
    7: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.3)",
        "subtopic": "Half-Life Analysis & Linear Integrated Rate Plots",
        "learning_objective": "Prove first-order kinetics using half-life constancy (t½ = ln2/k) and linear integrated rate graphs.",
        "what_to_learn": [
            "(1) Half-life (t½) definition: the time taken for the concentration of a reactant to decrease to half of its initial value.",
            "(2) First-order half-life relationship: t½ = ln 2 / k = 0.693 / k; t½ is completely independent of initial concentration.",
            "(3) Proving first order from graphs: measure at least two consecutive half-lives (e.g. [A] 0.8→0.4 and 0.4→0.2); if t½₁ ≈ t½₂, order is 1.",
            "(4) Second-order half-life: t½ = 1 / (k[A]₀); half-life is inversely proportional to initial concentration (doubles each time).",
            "(5) Zero-order half-life: t½ = [A]₀ / 2k; half-life halves each successive interval.",
            "(6) Integrated linear plots: [A] vs t linear → zero order (gradient = -k); ln[A] vs t linear → 1st order (gradient = -k); 1/[A] vs t linear → 2nd order (gradient = +k)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates measure only ONE half-life and conclude first order — mark schemes REQUIRE at least TWO consecutive half-lives.",
            "For ln[A] vs t graphs, remember gradient is NEGATIVE (-k), but rate constant k must always be reported as a POSITIVE value.",
            "Calculate k directly from t½ for first order using k = 0.693 / t½; always check units (s⁻¹ or min⁻¹ depending on time axis).",
            "State the equation of the straight line (y = mx + c) when interpreting integrated rate plots."
        ],
        "resources": "Usman Pack 11A3 Q26–Q50 & FAQs (Half-Lives and Integrated Plots)"
    },
    8: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.4)",
        "subtopic": "Reaction Mechanisms: The Rate-Determining Step (RDS) & Molecularity",
        "learning_objective": "Deduce reaction mechanisms, identify the rate-determining step, and determine molecularity of elementary steps.",
        "what_to_learn": [
            "(1) Reaction mechanism: the sequence of elementary molecular steps by which an overall reaction occurs.",
            "(2) Rate-determining step (RDS): the slowest elementary step in the mechanism that controls the overall reaction rate.",
            "(3) Molecularity: the number of reactant particles that collide and react in an elementary step (unimolecular = 1, bimolecular = 2).",
            "(4) Deducing RDS from rate equation: the species appearing in the rate equation (and their powers) correspond to the reactants in the RDS.",
            "(5) Zero-order reactants: do NOT take part in the RDS or any step prior to the RDS; they react in fast steps AFTER the RDS.",
            "(6) Reaction intermediate: a species formed in one step and consumed in a subsequent step; does not appear in overall equation or rate law."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates write 'termolecular step' (3 particles colliding) — termolecular collisions are statistically improbable; mechanisms proceed via unimolecular or bimolecular steps.",
            "Never say a zero-order reactant 'does not react' — it DOES react in the overall equation, but in a fast step AFTER the slow step.",
            "Intermediates vs Transition States: an intermediate has fully formed bonds (local energy minimum); a transition state has partially made/broken bonds (energy maximum).",
            "To prove a mechanism is valid: (1) derived rate law matches experimental rate law; (2) sum of elementary steps equals overall balanced equation."
        ],
        "resources": "Usman Pack 11A4 Q1–Q25 (RDS Concepts and Elementary Steps)"
    },
    9: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.4)",
        "subtopic": "Kinetics & Stereochemistry: SN1 vs SN2 Nucleophilic Substitution",
        "learning_objective": "Link kinetic orders to the stereochemical outcomes of SN1 and SN2 hydrolysis mechanisms.",
        "what_to_learn": [
            "(1) SN1 Mechanism (Substitution Nucleophilic Unimolecular): 2 steps; typical for tertiary halogenoalkanes (e.g. (CH3)3CBr).",
            "(2) SN1 Kinetics: Step 1 (slow heterolysis): (CH3)3CBr → (CH3)3C⁺ + Br⁻ (RDS); Step 2 (fast): (CH3)3C⁺ + OH⁻ → (CH3)3COH.",
            "(3) SN1 Rate Law: rate = k[(CH3)3CBr]; 1st order in halogenoalkane, ZERO order in nucleophile [OH⁻].",
            "(4) SN1 Stereochemistry: carbocation intermediate is TRIGONAL PLANAR around C⁺; nucleophile attacks equally from either face → 50:50 RACEMIC MIXTURE (optically inactive).",
            "(5) SN2 Mechanism (Substitution Nucleophilic Bimolecular): 1 concerted step; typical for primary halogenoalkanes (e.g. CH3CH2Br).",
            "(6) SN2 Kinetics: OH⁻ attacks from backside simultaneously as C-Br bond breaks via a five-coordinate transition state; rate = k[R-Br][OH⁻].",
            "(7) SN2 Stereochemistry: backside attack causes complete WALDEN INVERSION of configuration (optical inversion)."
        ],
        "how_to_outstand": [
            "Explain WHY tertiary halides undergo SN1: 3 alkyl groups exert positive inductive (+I) effect stabilising the carbocation; steric hindrance blocks SN2 backside attack.",
            "Explain WHY primary halides undergo SN2: primary carbocation is too unstable to form, but little steric hindrance allows backside attack.",
            "In optical activity questions: state TRIGONAL PLANAR intermediate attacked with EQUAL PROBABILITY from top and bottom faces, producing equal enantiomer amounts.",
            "Changing nucleophile concentration: doubling [OH⁻] doubles rate in SN2, but has ZERO effect on rate in SN1."
        ],
        "resources": "Usman Pack 11A4 Q26–Q40 (SN1/SN2 Kinetics and Stereochemistry)"
    },
    10: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.4)",
        "subtopic": "Fast Pre-Equilibrium Steps & Deriving Complex Rate Laws",
        "learning_objective": "Derive rate equations for mechanisms involving fast pre-equilibrium steps preceding the rate-determining step.",
        "what_to_learn": [
            "(1) Fast pre-equilibrium: Step 1: 2NO ⇌ N2O2 (fast equilibrium, K = [N2O2]/[NO]²); Step 2: N2O2 + O2 → 2NO2 (slow RDS).",
            "(2) Derivation rule: rate = k₂[N2O2][O2]; since N2O2 is an intermediate, substitute [N2O2] = K[NO]².",
            "(3) Overall rate equation: rate = k₂K[NO]²[O2] = k[NO]²[O2], explaining third-order kinetics via bimolecular steps.",
            "(4) Propanone iodination mechanism: Step 1 (fast protonation): CH3COCH3 + H⁺ ⇌ CH3C(OH⁺)CH3.",
            "(5) Step 2 (slow enolisation, RDS): CH3C(OH⁺)CH3 → CH3C(OH)=CH2 + H⁺; rate = k[CH3COCH3][H⁺].",
            "(6) Step 3 (fast electrophilic iodination): enol + I2 → CH3COCH2I + H⁺ + I⁻ (explains why I2 is zero order)."
        ],
        "how_to_outstand": [
            "Never leave an unmeasurable intermediate in a final rate equation; always substitute using the pre-equilibrium constant K.",
            "Explain role of H⁺ in propanone iodination: H⁺ is a homogeneous catalyst; it takes part in the RDS so it appears in the rate law.",
            "The composite rate constant k = k₂ × K; temperature affects both K (equilibrium) and k₂ (activation energy).",
            "Be prepared to explain why termolecular collisions are avoided by the two-step pre-equilibrium route."
        ],
        "resources": "Usman Pack 11A4 Q41–Q50 & FAQs (Pre-Equilibrium Mechanisms)"
    },
    13: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.5)",
        "subtopic": "Maxwell-Boltzmann Energy Distributions & Temperature Effects",
        "learning_objective": "Interpret Maxwell-Boltzmann distributions and explain the exponential rate increase with temperature.",
        "what_to_learn": [
            "(1) Maxwell-Boltzmann distribution: shows the spread of molecular kinetic energies in a gas at temperature T.",
            "(2) Crucial curve features: starts at origin (0,0) (no molecules with 0 energy); peak = most probable energy (Emp); mean energy is to the right of Emp; asymptote at high energy (never touches x-axis).",
            "(3) Total area under curve: represents the total number of gas molecules (constant at fixed quantity).",
            "(4) Effect of increasing temperature (T2 > T1): peak shifts down and to the right; curve broadens; total area remains identical.",
            "(5) Activation energy Ea: marked as a vertical line; area under curve to right of Ea represents fraction of molecules with E >= Ea.",
            "(6) Why 10 °C rise roughly doubles rate: collision frequency increases by only ~2%, but the fraction of particles with E >= Ea increases EXPONENTIALLY."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Drawing the higher temperature T2 curve with its peak at the same height or higher — mark schemes REQUIRE peak to be LOWER and to the RIGHT.",
            "Do NOT say 'particles have more energy so they collide more' as the main factor — collision frequency accounts for only ~2% of the increase; the EXPONENTIAL increase in particles with E >= Ea is the primary cause.",
            "The curve must NEVER touch the x-axis at high energy — there is no theoretical maximum kinetic energy.",
            "Always state that total area under both curves must remain equal."
        ],
        "resources": "Usman Pack 11A5 Q1–Q25 (Maxwell-Boltzmann Curves and Temperature Shifts)"
    },
    14: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.5)",
        "subtopic": "Catalysis: Homogeneous vs Heterogeneous & Adsorption Theory",
        "learning_objective": "Classify homogeneous and heterogeneous catalysts and explain surface adsorption theory and catalyst poisoning.",
        "what_to_learn": [
            "(1) Catalyst definition: increases the rate of reaction by providing an alternative pathway of lower activation energy, remaining chemically unchanged at the end.",
            "(2) Catalyst effect on Maxwell-Boltzmann curve: curve shape DOES NOT CHANGE; Ea line moves to the LEFT (Ea(cat) < Ea(uncat)), increasing shaded area.",
            "(3) Homogeneous catalyst: same physical phase as reactants (e.g. Fe²⁺/Fe³⁺ in S2O8²⁻ + 2I⁻; H⁺ in ester hydrolysis; Cl• in ozone depletion).",
            "(4) Heterogeneous catalyst: different physical phase from reactants (e.g. solid V2O5 in Contact process; solid Fe in Haber process; Pt/Rh in catalytic converters).",
            "(5) 5-step adsorption mechanism: 1. Diffusion to surface; 2. Chemisorption onto active sites (bonds weakened, favourable orientation); 3. Reaction on surface; 4. Desorption of products; 5. Diffusion away.",
            "(6) Catalyst poisoning: impurities (e.g. sulfur in Haber, lead in catalytic converters) adsorb irreversibly onto active sites, blocking reactants."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Stating a catalyst 'changes the kinetic energy of particles' or 'shifts the curve to the right' — the curve does NOT change; only Ea shifts left.",
            "Adsorption vs Absorption: use ADSORPTION (molecules bind to the surface); absorption is uptake into the bulk material.",
            "Fe²⁺/Fe³⁺ homogeneous catalysis: explain both steps (S2O8²⁻ + 2Fe²⁺ → 2SO4²⁻ + 2Fe³⁺, then 2Fe³⁺ + 2I⁻ → 2Fe²⁺ + I2); overcomes negative ion repulsion.",
            "Explain why transition metals make great catalysts: variable oxidation states and partially filled d-orbitals form temporary bonds."
        ],
        "resources": "Usman Pack 11A5 Q26–Q50 & FAQs (Catalysis Types and Surface Chemistry)"
    },
    15: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.6)",
        "subtopic": "The Arrhenius Equation: Mathematical Forms & Parameter Meanings",
        "learning_objective": "Understand the exponential and logarithmic forms of the Arrhenius equation and define all parameters.",
        "what_to_learn": [
            "(1) Arrhenius equation: k = A e^(-Ea / RT), quantifying the relationship between rate constant k, temperature T, and activation energy Ea.",
            "(2) Parameters: k = rate constant; A = pre-exponential (frequency) factor (accounts for collision frequency and correct steric orientation).",
            "(3) Boltzmann factor: e^(-Ea / RT) represents the fraction of collisions with energy greater than or equal to Ea.",
            "(4) R = gas constant (8.31 J K⁻¹ mol⁻¹); T = temperature in KELVIN (T(K) = θ(°C) + 273).",
            "(5) Natural logarithm form: ln k = -Ea / RT + ln A  (in the form of y = mx + c).",
            "(6) Two-point formula: ln(k2 / k1) = (Ea / R) × (1/T1 - 1/T2) or ln(k2 / k1) = -Ea/R × (1/T2 - 1/T1)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Forgetting to convert temperature to Kelvin (+273) — always check T is in K.",
            "R is in J K⁻¹ mol⁻¹, so calculating Ea gives J mol⁻¹ — mark schemes frequently require conversion to kJ mol⁻¹ (divide by 1000).",
            "Units of pre-exponential factor A are identical to the units of rate constant k for that specific reaction order.",
            "As T increases, e^(-Ea/RT) approaches 1, meaning k approaches the maximum collision factor A."
        ],
        "resources": "Usman Pack 11A6 Q1–Q25 (Arrhenius Formula Parameters and Calculations)"
    },
    16: {
        "topic_code": "Topic 11 — Kinetics 2 (11A.6)",
        "subtopic": "Arrhenius Plots: Graphical Determination of Ea and Pre-Exponential Factor A",
        "learning_objective": "Plot and interpret ln k vs 1/T graphs to determine activation energy from the gradient and A from the y-intercept.",
        "what_to_learn": [
            "(1) Linear relationship: ln k = (-Ea / R) × (1/T) + ln A.",
            "(2) Axes: y-axis = ln k (dimensionless); x-axis = 1/T (in K⁻¹, typically scaled as 10⁻³ K⁻¹).",
            "(3) Gradient m = -Ea / R; since the gradient is negative, Ea = -m × R = -(gradient) × 8.31 J mol⁻¹.",
            "(4) y-intercept c = ln A; calculate A = e^c (with same units as k).",
            "(5) Constructing the table: given T(°C) and k → calculate T(K) → calculate 1/T (K⁻¹) → calculate ln k.",
            "(6) Calculating Ea from two coordinates: gradient = (ln k2 - ln k1) / (1/T2 - 1/T1)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Scaling on the x-axis! If x-axis is labelled '1/T × 10³ / K⁻¹' and you read a value of 3.2, the actual value of 1/T is 3.2 × 10⁻³ K⁻¹.",
            "Ea is ALWAYS a positive quantity! The gradient of ln k vs 1/T is negative, so Ea = -(gradient) × 8.31.",
            "When drawing line of best fit on past paper grids, ensure points are plotted with small crosses (+) within ±½ square.",
            "Show full working: gradient = Δy / Δx with values extracted from points on your line of best fit, NOT raw table data points."
        ],
        "resources": "Usman Pack 11A6 Q26–Q50 & FAQs (Arrhenius Plots and Graph Work)"
    },
    17: {
        "topic_code": "Topic 11 — Thinking Bigger & Synoptic Kinetics",
        "subtopic": "Catalyst Craft: Industrial Design & Synoptic Kinetics Integration",
        "learning_objective": "Integrate reaction rates, orders, mechanisms, and Arrhenius plots to evaluate real-world industrial catalysis.",
        "what_to_learn": [
            "(1) Thinking Bigger: Catalyst Craft — transition metal catalysts in green chemical engineering (e.g. organometallic catalysts, enzyme mimetics).",
            "(2) Industrial compromises: balancing rate (high T, high P) against equilibrium yield and energy/capital costs in the Haber and Contact processes.",
            "(3) Zeolite catalysts: shape-selective heterogeneous catalysis; pore size matches specific molecular dimensions, controlling product selectivity.",
            "(4) Autocatalysis kinetics: sigmoidal (S-shaped) product-time curve (e.g. Mn²⁺ catalysing MnO4⁻ + C2O4²⁻ titration).",
            "(5) Synoptic integration: linking rate equations to proposed reaction profiles, multi-step mechanisms, and stereochemical products."
        ],
        "how_to_outstand": [
            "In 6-mark synoptic questions, connect the three pillars: (1) Experimental rate law, (2) Molecularity of RDS, (3) Arrhenius energy barrier.",
            "Autocatalytic sigmoidal curve: explain three phases: initial induction lag (no catalyst), rapid acceleration (catalyst forms), leveling off (reactants depleted).",
            "Explain economic benefits of catalysts: lower operating temperatures save fossil fuel energy and reduce carbon footprint."
        ],
        "resources": "Topic 11 Thinking Bigger Case Study & Synoptic Practice Pack"
    },
    20: {
        "topic_code": "Topic 11 — Exam Practice",
        "subtopic": "Unit 4 Topic 11 Exam Practice & Past Paper Synthesis",
        "learning_objective": "Synthesize all Kinetics 2 concepts under exam pressure, solving authentic multi-part past paper questions.",
        "what_to_learn": [
            "(1) Timed practice on complex 6-mark rate-mechanism synthesis questions from WCH14 past papers.",
            "(2) Identifying examiner traps across the entire Topic 11 syllabus.",
            "(3) Auditing calculation layouts: significant figures, intermediate rounding errors, explicit unit statements.",
            "(4) Reviewing complete worked answers against Edexcel indicative content levels."
        ],
        "how_to_outstand": [
            "Ensure full mastery of both graphical methods: tangents on [A]-t and gradients on Arrhenius ln k vs 1/T.",
            "Keep definitions word-perfect: activation energy, rate-determining step, order of reaction, catalyst.",
            "Pre-exam review of all Section D FAQs from Packs 11A1 through 11A6."
        ],
        "resources": "Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf (Complete 50Q Pack)"
    },
    21: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.1)",
        "subtopic": "Introduction to Entropy: Disorder, Microstates & Physical States",
        "learning_objective": "Define entropy as the dispersal of energy and compare standard molar entropies across physical states.",
        "what_to_learn": [
            "(1) Entropy (S): a measure of the degree of disorder or randomness of a system, or the number of microscopic ways (microstates, W) that energy can be distributed (S = k ln W).",
            "(2) Units of entropy: Joules per Kelvin per mole (J K⁻¹ mol⁻¹); contrast with enthalpy in kJ mol⁻¹.",
            "(3) Physical states: S(solid) < S(liquid) << S(gas). Gas molecules have rapid random translational motion and enormous numbers of microstates.",
            "(4) Factors increasing entropy: (a) melting and boiling; (b) increasing temperature; (c) dissolving solid in liquid; (d) increasing number of gas moles.",
            "(5) Third Law of Thermodynamics: a perfectly crystalline substance at absolute zero (0 K) has zero entropy (S = 0 J K⁻¹ mol⁻¹).",
            "(6) Standard molar entropy (S°): entropy content of one mole of a substance in its standard state at 298 K and 1 bar."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates state standard entropy of elements in standard states is zero — NO! Enthalpy of formation is zero, but standard entropy of elements is ALWAYS POSITIVE (e.g. S°(O2(g)) = 205 J K⁻¹ mol⁻¹).",
            "Units must be J K⁻¹ mol⁻¹ (Joules, NOT kJ).",
            "Why vaporization causes a much larger entropy increase than melting: melting disrupts the lattice slightly, but vaporization expands volume by ~1000×, vastly multiplying translational microstates.",
            "Dissolving ionic solids: two opposing factors — lattice breakdown increases entropy, but hydration of ions orders water molecules, decreasing entropy."
        ],
        "resources": "Usman Pack 12A1 Q1–Q25 (Entropy Concepts and States)"
    },
    22: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.1)",
        "subtopic": "Calculating System Entropy Changes (ΔS_system)",
        "learning_objective": "Calculate standard entropy changes of the system from tabulated standard molar entropy values.",
        "what_to_learn": [
            "(1) System entropy change formula: ΔS_system = ΣS°(products) - ΣS°(reactants).",
            "(2) Stoichiometric coefficients: multiply each S° value by its balancing number in the balanced equation.",
            "(3) Predicting sign of ΔS_system: if moles of gas increase (Δn_gas > 0), ΔS_system > 0 (positive); if moles of gas decrease, ΔS_system < 0 (negative).",
            "(4) Worked example 1 (Haber process): N2(g) + 3H2(g) → 2NH3(g); 4 mol gas → 2 mol gas; ΔS_system is large and negative (-198 J K⁻¹ mol⁻¹).",
            "(5) Worked example 2 (Thermal decomposition): CaCO3(s) → CaO(s) + CO2(g); 0 mol gas → 1 mol gas; ΔS_system is positive (+160 J K⁻¹ mol⁻¹)."
        ],
        "how_to_outstand": [
            "Show full substitution with products first, then reactants: [2 × S(NH3)] - [S(N2) + 3 × S(H2)].",
            "Always include the correct sign (+ or -) and units (J K⁻¹ mol⁻¹).",
            "Explain WHY ΔS_system is positive or negative in terms of gas mole count and energy dispersal."
        ],
        "resources": "Usman Pack 12A1 Q26–Q50 & FAQs (ΔS_system Calculations)"
    },
    23: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.2)",
        "subtopic": "Entropy of the Surroundings (ΔS_surroundings) & Temperature Dependence",
        "learning_objective": "Calculate entropy changes of the surroundings and understand its inverse dependence on temperature.",
        "what_to_learn": [
            "(1) Surroundings: everything outside the chemical system (the flask, air, solvent, universe).",
            "(2) Surroundings entropy formula: ΔS_surroundings = -ΔH_system / T.",
            "(3) Exothermic reactions (ΔH < 0): heat energy is released to surroundings → thermal motion of surroundings increases → ΔS_surroundings > 0 (positive).",
            "(4) Endothermic reactions (ΔH > 0): heat energy is absorbed from surroundings → surroundings cool down → ΔS_surroundings < 0 (negative).",
            "(5) Unit conversion: ΔH is given in kJ mol⁻¹; MUST multiply by 1000 to convert to J mol⁻¹ before dividing by T in Kelvin.",
            "(6) Temperature effect: at high T, adding a fixed quantity of heat causes only a tiny fractional increase in disorder; at low T, the same heat causes a huge entropy jump."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: The negative sign in -ΔH/T! Exothermic reactions have ΔH < 0, so -(-ΔH) gives a POSITIVE ΔS_surroundings.",
            "EXAMINER TRAP: Units! Candidates divide kJ by T and mix with J for ΔS_system. ALWAYS convert ΔH to J mol⁻¹ (× 1000).",
            "Temperature MUST be in Kelvin (K).",
            "Analogy for temperature dependence: shouting in a quiet library (low T) creates huge disturbance; shouting in a noisy stadium (high T) has negligible effect."
        ],
        "resources": "Usman Pack 12A2 Q1–Q25 (ΔS_surroundings Calculations)"
    },
    24: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.2)",
        "subtopic": "Total Entropy Change (ΔS_total) & Spontaneity Criteria",
        "learning_objective": "Calculate total entropy change and apply the Second Law criterion for feasible chemical reactions.",
        "what_to_learn": [
            "(1) Second Law of Thermodynamics: for any spontaneous (feasible) process, the total entropy of the universe must increase.",
            "(2) Total entropy formula: ΔS_total = ΔS_system + ΔS_surroundings = ΔS_system - (ΔH / T).",
            "(3) Feasibility criteria: if ΔS_total > 0, the reaction is spontaneous/feasible; if ΔS_total < 0, the reaction is not feasible; if ΔS_total = 0, the system is at equilibrium.",
            "(4) Four thermodynamic cases: (A) Exothermic (ΔH < 0) & ΔS_sys > 0: ΔS_total always > 0 (feasible at all T); (B) Endothermic & ΔS_sys < 0: ΔS_total always < 0 (never feasible).",
            "(5) Case C: Exothermic & ΔS_sys < 0: feasible at LOW temperatures (where -ΔH/T dominates).",
            "(6) Case D: Endothermic & ΔS_sys > 0: feasible at HIGH temperatures (where ΔS_sys dominates)."
        ],
        "how_to_outstand": [
            "Always state: 'Reaction is feasible because ΔS_total > 0' — cite the numerical value to back your conclusion.",
            "Both ΔS_system and ΔS_surroundings must be in J K⁻¹ mol⁻¹ before adding them.",
            "At equilibrium, ΔS_total = 0 — memorize this link to Topic 13 equilibrium constants (ΔS_total = R ln K).",
            "Explain how an endothermic reaction (e.g. dissolving NH4NO3 in water) can occur spontaneously: ΔS_system is so large and positive that it overcomes negative ΔS_surroundings."
        ],
        "resources": "Usman Pack 12A2 Q26–Q50 & FAQs (Total Entropy and Feasibility)"
    },
    27: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.3)",
        "subtopic": "Understanding Entropy Changes & Crossover Temperature",
        "learning_objective": "Calculate the crossover temperature at which feasibility changes and distinguish kinetic stability from thermodynamic feasibility.",
        "what_to_learn": [
            "(1) Crossover temperature: the temperature at which a reaction transitions between spontaneous and non-spontaneous (where ΔS_total = 0).",
            "(2) Derivation: at crossover, ΔS_total = 0 → ΔS_system - ΔH/T = 0 → T = ΔH / ΔS_system.",
            "(3) Units check in crossover formula: ΔH in J mol⁻¹ (or both ΔH and ΔS in kJ); T in Kelvin.",
            "(4) Graphical analysis: plot of ΔS_total against temperature T is curved (hyperbolic since ΔS_surr ∝ 1/T); plot of ΔS_total vs 1/T is linear.",
            "(5) Kinetic stability: a reaction may have ΔS_total > 0 (thermodynamically feasible) but show zero observable rate at 298 K due to very high activation energy (e.g. diamond → graphite, or H2 + O2 → H2O)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Writing 'the reaction is impossible' when ΔS_total < 0 — say 'the reaction is not thermodynamically feasible under these conditions'.",
            "Distinguish KINETICALLY INERT vs THERMODYNAMICALLY STABLE: a mixture of H2 and O2 is thermodynamically unstable (ΔS_total >> 0) but kinetically inert due to high Ea.",
            "For crossover calculations: always state whether reaction is feasible ABOVE or BELOW that temperature (check signs of ΔH and ΔS_sys).",
            "Remember that S and H values are assumed to remain approximately constant with temperature."
        ],
        "resources": "Usman Pack 12A3 Q1–Q50 & FAQs (Crossover Temp and Kinetic Stability)"
    },
    28: {
        "topic_code": "Topic 12 — Entropy and Energetics (12A.3)",
        "subtopic": "Thermodynamics vs Kinetics: Industrial Trade-Offs",
        "learning_objective": "Evaluate industrial chemical processes by balancing thermodynamic feasibility against reaction kinetics.",
        "what_to_learn": [
            "(1) Industrial case study: The Haber Process N2(g) + 3H2(g) ⇌ 2NH3(g) (ΔH = -92 kJ mol⁻¹, ΔS_sys = -198 J K⁻¹ mol⁻¹).",
            "(2) Feasibility vs temperature: as T increases, ΔS_surroundings (-ΔH/T) becomes less positive, so ΔS_total decreases and becomes negative above ~465 K (192 °C).",
            "(3) The compromise: at 192 °C, reaction is feasible but too slow; at 450 °C, reaction has acceptable rate (kinetics) but lower equilibrium conversion (~15%).",
            "(4) Steam reforming of methane: CH4(g) + H2O(g) ⇌ CO(g) + 3H2(g) (endothermic, ΔS_sys > 0); feasible only at high temperatures (> 700 °C)."
        ],
        "how_to_outstand": [
            "In 6-mark evaluation questions, structure answer in two distinct paragraphs: (1) Thermodynamics (ΔS_total, equilibrium position), (2) Kinetics (collision frequency, fraction with E >= Ea, catalyst).",
            "Clearly distinguish ΔS_total from rate of reaction: ΔS_total tells you IF it can happen; kinetics tells you HOW FAST it happens."
        ],
        "resources": "Topic 12 Exam Practice & Synoptic Feasibility Worksheets"
    },
    29: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.1)",
        "subtopic": "Lattice Energy & Standard Enthalpy Definitions",
        "learning_objective": "Define standard lattice energy, atomisation, ionisation energy, and electron affinity with balanced thermochemical equations.",
        "what_to_learn": [
            "(1) Lattice energy (formation convention): the standard enthalpy change when ONE mole of an ionic crystalline solid is formed from its gaseous ions under standard conditions (e.g. Na⁺(g) + Cl⁻(g) → NaCl(s); always negative/exothermic).",
            "(2) Lattice dissociation enthalpy: standard enthalpy change when ONE mole of ionic solid is completely separated into gaseous ions (always positive/endothermic; equal magnitude, opposite sign).",
            "(3) Standard enthalpy of atomisation (Δ_at H): enthalpy change when ONE mole of gaseous atoms is formed from the element in its standard state (e.g. ½Cl2(g) → Cl(g), Na(s) → Na(g); always positive).",
            "(4) First ionisation energy (IE1): enthalpy change when ONE mole of electrons is removed from one mole of gaseous atoms to form 1+ ions (e.g. Na(g) → Na⁺(g) + e⁻; endothermic).",
            "(5) First electron affinity (EA1): enthalpy change when ONE mole of gaseous atoms gains one mole of electrons to form 1- ions (e.g. Cl(g) + e⁻ → Cl⁻(g); exothermic).",
            "(6) Second electron affinity (EA2): enthalpy change when 1- gaseous ions gain an electron to form 2- ions (e.g. O⁻(g) + e⁻ → O²⁻(g); ALWAYS ENDOTHERMIC due to electron-electron repulsion)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Definitions must specify ONE MOLE of gaseous atoms/ions or ONE MOLE of ionic compound.",
            "State symbols are STRICTLY mandatory: mark schemes deduct marks if (g) or (s) is omitted.",
            "Explain why EA2 is endothermic: adding a negative electron to a negatively charged ion (O⁻) requires overcoming strong electrostatic repulsion.",
            "Check Pearson Edexcel convention: Unit 4 uses negative lattice formation enthalpy (Δ_latt H < 0)."
        ],
        "resources": "Usman Pack 12B1 Q1–Q25 (Enthalpy Definitions and State Symbols)"
    },
    30: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.1)",
        "subtopic": "Constructing Born-Haber Cycles: NaCl, MgCl2 & CaO",
        "learning_objective": "Construct complete Born-Haber cycles and calculate unknown enthalpy values using Hess's Law.",
        "what_to_learn": [
            "(1) Born-Haber cycle: an energy level cycle applying Hess's Law to calculate lattice energy from experimentally measurable enthalpy changes.",
            "(2) Cycle steps for Group 1 halide (NaCl): Formation (Δ_f H) = Δ_at H(Na) + IE1(Na) + Δ_at H(Cl) + EA1(Cl) + Δ_latt H(NaCl).",
            "(3) Cycle steps for Group 2 halide (MgCl2): Formation = Δ_at H(Mg) + IE1(Mg) + IE2(Mg) + 2×Δ_at H(Cl) + 2×EA1(Cl) + Δ_latt H(MgCl2).",
            "(4) Cycle steps for Group 2 oxide (CaO): Formation = Δ_at H(Ca) + IE1(Ca) + IE2(Ca) + Δ_at H(O) + EA1(O) + EA2(O) + Δ_latt H(CaO).",
            "(5) Calculation method: clockwise route = anticlockwise route, or Δ_f H = Σ(all upward formation steps) + Δ_latt H.",
            "(6) Rearranging for lattice energy: Δ_latt H = Δ_f H - [Δ_at H(metal) + ΣIE + Δ_at H(non-metal) + ΣEA]."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Multiplying by 2! For MgCl2, you must include IE1 + IE2 of Mg, and MULTIPLY Δ_at H(Cl) and EA1(Cl) by 2 (for 2 moles of Cl atoms).",
            "For bond enthalpy of Cl2: note that Δ_at H(Cl) = ½ E(Cl-Cl); if given bond enthalpy of Cl2, use it directly for 2Cl atoms in MgCl2.",
            "Ensure the arrow directions on the energy level diagram correspond to the sign: endothermic arrows point UP; exothermic arrows point DOWN.",
            "Always check that the calculated lattice energy is a large negative value (e.g. ~ -780 kJ mol⁻¹ for NaCl, ~ -2500 for MgCl2, ~ -3400 for CaO)."
        ],
        "resources": "Usman Pack 12B1 Q26–Q50 & FAQs (Born-Haber Cycle Calculations)"
    },
    31: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.2)",
        "subtopic": "Experimental vs Theoretical Lattice Energies & The Ionic Model",
        "learning_objective": "Compare Born-Haber experimental lattice energies with theoretical Born-Landé values and evaluate ionic model assumptions.",
        "what_to_learn": [
            "(1) Theoretical lattice energy: calculated using electrostatics (Born-Landé equation: LE ∝ (z⁺ × z⁻) / (r⁺ + r⁻)).",
            "(2) Perfect ionic model assumptions: (a) ions are completely spherical; (b) charge is evenly distributed (point charges); (c) bonding is 100% ionic with no covalent character / electron sharing.",
            "(3) Experimental lattice energy: obtained from the empirical Born-Haber cycle.",
            "(4) Agreement: for compounds with large cations and small anions (NaCl, KCl, NaF), theoretical and experimental LE agree within 1–2% → bonding is almost purely ionic.",
            "(5) Discrepancy: for compounds with small/polarising cations and large/oxidisable anions (AgCl, AgI, MgI2), experimental LE is significantly more negative than theoretical LE → covalent character exists.",
            "(6) Reason for extra stability: partial covalent bonding provides additional bonding overlap beyond pure electrostatics, releasing more energy when the lattice forms."
        ],
        "how_to_outstand": [
            "Explain WHY experimental LE is MORE NEGATIVE than theoretical: partial covalent character means additional electron sharing occurs, strengthening the lattice.",
            "State the two core assumptions of the ionic model: spherical ions with purely electrostatic attraction (point charges).",
            "Compare AgCl vs NaCl: Ag⁺ and Na⁺ have similar ionic radii, but Ag⁺ has a (4d¹⁰) outer subshell which is less effective at shielding nuclear charge, making Ag⁺ much more polarising than Na⁺ (2p⁶)."
        ],
        "resources": "Usman Pack 12B2 Q1–Q25 (Ionic Model and LE Discrepancies)"
    },
    34: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.2)",
        "subtopic": "Polarisation & Fajans' Rules: Explaining Covalent Character",
        "learning_objective": "Apply Fajans' rules to predict and explain the degree of covalent character in ionic compounds.",
        "what_to_learn": [
            "(1) Polarisation: the distortion of the electron cloud of an anion by the electric field of an adjacent cation.",
            "(2) Polarising power of a cation: ability to attract and distort electrons; depends on charge density (charge / ionic radius). Small, highly charged cations have maximum polarising power (e.g. Al³⁺ > Mg²⁺ > Na⁺; Li⁺ > Na⁺ > K⁺).",
            "(3) Polarisability of an anion: ease with which its electron cloud is distorted; depends on ionic radius. Large, highly charged anions are most polarisable (e.g. I⁻ > Br⁻ > Cl⁻ > F⁻; S²⁻ > O²⁻).",
            "(4) Fajans' Rules: covalent character is maximised when: (a) cation is small and highly charged; (b) anion is large and highly charged.",
            "(5) Consequences of covalent character: (a) lattice energy more exothermic than theoretical; (b) lower melting point; (c) decreased electrical conductivity when molten; (d) decreased solubility in water."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Confusing polarising power and polarisability — CATIONS polarise (polarising power); ANIONS are polarised (polarisability).",
            "Quote both factors for cations: HIGH charge and SMALL ionic radius (high charge density).",
            "Quote both factors for anions: LARGE ionic radius and HIGH negative charge (outer electrons held less tightly by nucleus).",
            "Example trend: AlF3 is ionic (F⁻ small, resistant to polarisation), but AlCl3 and AlI3 are predominantly covalent molecules."
        ],
        "resources": "Usman Pack 12B2 Q26–Q50 & FAQs (Fajans' Rules and Trends)"
    },
    35: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.3)",
        "subtopic": "Enthalpy Changes of Solution and Hydration",
        "learning_objective": "Construct Hess's Law cycles linking lattice energy, hydration enthalpy, and enthalpy of solution.",
        "what_to_learn": [
            "(1) Enthalpy of solution (Δ_sol H): standard enthalpy change when ONE mole of an ionic solid dissolves in water to give infinitely dilute aqueous ions (NaCl(s) + aq → Na⁺(aq) + Cl⁻(aq); can be positive or negative).",
            "(2) Enthalpy of hydration (Δ_hyd H): standard enthalpy change when ONE mole of gaseous ions dissolves in water to form aqueous ions (e.g. Na⁺(g) + aq → Na⁺(aq); ALWAYS EXOTHERMIC/NEGATIVE due to ion-dipole attractions).",
            "(3) Energy cycle / Hess's Law relationship: Dissolving an ionic solid involves: (a) breaking the lattice into gaseous ions (+Δ_latt_diss H = -Δ_latt H); (b) hydrating the gaseous ions (ΣΔ_hyd H).",
            "(4) Formula: Δ_sol H = ΣΔ_hyd H(cations) + ΣΔ_hyd H(anions) - Δ_latt H  (where Δ_latt H is negative formation energy).",
            "(5) Factors affecting Δ_hyd H: hydration enthalpy becomes more exothermic as ionic charge increases and ionic radius decreases (higher charge density forms stronger ion-dipole bonds with water delta-minus oxygen or delta-plus hydrogen)."
        ],
        "how_to_outstand": [
            "State symbols are crucial: (s) → (aq) for solution; (g) → (aq) for hydration.",
            "Remember that hydration enthalpy is ALWAYS negative (exothermic) because new attractive ion-dipole forces are formed.",
            "When calculating Δ_sol H for MgCl2: multiply Δ_hyd H(Cl⁻) by 2 for the two chloride ions.",
            "Why dissolving NaCl (Δ_sol H = +3.8 kJ mol⁻¹) occurs spontaneously even though it is slightly endothermic: ΔS_system increases substantially as the rigid lattice dissolves into free aqueous ions, making ΔS_total > 0."
        ],
        "resources": "Usman Pack 12B3 Q1–Q25 (Solution and Hydration Calculations)"
    },
    36: {
        "topic_code": "Topic 12 — Entropy and Energetics (12B.3)",
        "subtopic": "Solubility Trends of Group 2 Sulfates and Hydroxides",
        "learning_objective": "Explain the opposing solubility trends of Group 2 sulfates and hydroxides using lattice and hydration enthalpies.",
        "what_to_learn": [
            "(1) Group 2 Hydroxide solubility: increases down the group (Mg(OH)2 insoluble, Ca(OH)2 sparingly, Ba(OH)2 soluble).",
            "(2) Group 2 Sulfate solubility: decreases down the group (MgSO4 soluble, CaSO4 sparingly, BaSO4 insoluble).",
            "(3) Explanation for sulfates: SO4²⁻ is a very large anion. Down Group 2, cation radius increases (Mg²⁺ to Ba²⁺).",
            "(4) Because SO4²⁻ is large, the fractional change in (r⁺ + r⁻) is small, so lattice energy decreases only slightly down the group.",
            "(5) However, Δ_hyd H(M²⁺) depends only on r⁺ and decreases significantly (becomes much less exothermic) from Mg²⁺ to Ba²⁺.",
            "(6) Consequently, Δ_sol H becomes more endothermic (less negative) down the group, so BaSO4 is insoluble.",
            "(7) Explanation for hydroxides: OH⁻ is a small anion, so (r⁺ + r⁻) changes significantly; lattice energy decreases much faster than hydration enthalpy, so Δ_sol H becomes more exothermic and solubility increases."
        ],
        "how_to_outstand": [
            "In 6-mark questions on Group 2 solubility, structure your answer into 4 points: (1) State the trend, (2) Compare relative sizes of cation vs anion, (3) Contrast rate of decrease of lattice energy vs hydration enthalpy, (4) Conclude on the overall sign of Δ_sol H.",
            "Key phrase: 'Δ_hyd H of the cation decreases more rapidly than the lattice energy for sulfates because the sulfate ion is relatively large.'",
            "Medical application: BaSO4 is used as a barium meal radiocontrast agent for stomach X-rays because it is completely insoluble and therefore non-toxic."
        ],
        "resources": "Usman Pack 12B3 Q26–Q50 & FAQs (Group 2 Solubility Trends)"
    },
    37: {
        "topic_code": "Topic 12 — Thinking Bigger & Synoptic Energetics",
        "subtopic": "Hydrogen Revolution: Energetics of Hydrogen Storage & Fuel Cells",
        "learning_objective": "Apply thermodynamic and entropy concepts to evaluate hydrogen storage and fuel cell technology.",
        "what_to_learn": [
            "(1) Hydrogen fuel cell reaction: 2H2(g) + O2(g) → 2H2O(l) (ΔH = -572 kJ mol⁻¹, ΔS_sys = -327 J K⁻¹ mol⁻¹).",
            "(2) Thermodynamic efficiency: fuel cells convert chemical energy directly into electrical energy without thermal combustion limits (Carnot cycle).",
            "(3) Hydrogen storage challenge: H2 has high energy density by mass (142 MJ/kg) but very low energy density by volume at STP (0.01 MJ/L).",
            "(4) Metal hydride storage (e.g. MgH2, LaNi5H6): hydrogen absorbed reversibly into metal lattice; forming hydride is exothermic; releasing H2 requires endothermic heating.",
            "(5) Entropy trade-off in metal hydrides: absorption has ΔS_sys << 0 (gas to solid); requires high pressure or low temperature to be feasible."
        ],
        "how_to_outstand": [
            "Link fuel cell thermodynamics to ΔG = -nFE° and ΔS_total = R ln K.",
            "Explain green vs grey vs blue hydrogen: green uses electrolysis powered by renewables; blue uses natural gas with carbon capture; grey vents CO2."
        ],
        "resources": "Topic 12 Thinking Bigger Case Study & Fuel Cell Energetics"
    },
    38: {
        "topic_code": "Topic 12 — Exam Practice",
        "subtopic": "Unit 4 Topic 12 Exam Practice & Energetics Past Paper Synthesis",
        "learning_objective": "Synthesize entropy, feasibility, Born-Haber cycles, and solution energetics under timed conditions.",
        "what_to_learn": [
            "(1) Timed practice on complex Born-Haber and solubility past paper problems.",
            "(2) Multi-step calculations: calculating ΔS_system, ΔS_surroundings, ΔS_total, and predicting crossover temperatures.",
            "(3) Fajans' rules justification drills comparing experimental and theoretical lattice energies.",
            "(4) Full mark scheme audit against Pearson Edexcel Unit 4 examiner reports."
        ],
        "how_to_outstand": [
            "Check all signs (+/-) and units (J vs kJ) before writing final answers.",
            "In Born-Haber diagrams, write complete species with state symbols at each horizontal energy level.",
            "Review Top 10 Examiner FAQs from Pack 12B."
        ],
        "resources": "Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf (Complete 50Q Pack)"
    },
    41: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.1)",
        "subtopic": "The Equilibrium Constant Kc: Expressions & Heterogeneous Equilibria",
        "learning_objective": "Formulate equilibrium constant Kc expressions and deduce units for homogeneous and heterogeneous equilibria.",
        "what_to_learn": [
            "(1) Dynamic equilibrium: rate of forward reaction = rate of reverse reaction; concentrations of reactants and products remain constant.",
            "(2) Equilibrium constant Kc: for aA + bB ⇌ cC + dD, Kc = ([C]^c [D]^d) / ([A]^a [B]^b).",
            "(3) Square brackets [ ]: STRICTLY denote equilibrium concentrations in mol dm⁻³.",
            "(4) Deducing units of Kc: substitute (mol dm⁻³) into numerator and denominator and cancel powers.",
            "(5) Homogeneous equilibrium: all reactants and products are in the same phase (e.g. all gases or all aqueous).",
            "(6) Heterogeneous equilibrium: species exist in different phases; concentrations of pure solids (s) and pure liquid solvents (l) are constant and OMITTED from Kc (incorporated into Kc).",
            "(7) Examples: CaCO3(s) ⇌ CaO(s) + CO2(g) → Kc = [CO2]; C(s) + H2O(g) ⇌ CO(g) + H2(g) → Kc = ([CO][H2]) / [H2O]."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Writing round brackets ( ) instead of square brackets [ ] in Kc expressions — mark schemes strictly require SQUARE BRACKETS.",
            "Do NOT include solids in Kc expressions — if you write Kc = [CaO][CO2]/[CaCO3], you score ZERO.",
            "When units cancel completely (e.g. esterification), write 'no units' — do NOT leave the space blank.",
            "Always state that equilibrium concentrations must be used, not initial concentrations."
        ],
        "resources": "Usman Pack 13A1 Q1–Q25 (Kc Expressions and Heterogeneous Systems)"
    },
    42: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.1)",
        "subtopic": "ICE Table Calculations for Kc: Equilibrium Moles & Volumes",
        "learning_objective": "Calculate Kc values from initial and equilibrium moles using ICE tables and convert to concentrations.",
        "what_to_learn": [
            "(1) ICE Table method: Initial moles (I), Change in moles (C), Equilibrium moles (E).",
            "(2) Change row must follow stoichiometric ratios: if x moles of reactant react, products form in stoichiometric ratio.",
            "(3) Volume division: divide equilibrium moles by vessel volume V (in dm³) to obtain concentrations: [A] = n_eq / V.",
            "(4) When volume cancels: if total moles of gas on left = total moles of gas on right (e.g. H2 + I2 ⇌ 2HI), the volume V cancels in Kc expression; moles can be used directly.",
            "(5) When volume does NOT cancel: if total moles differ (e.g. N2 + 3H2 ⇌ 2NH3), V does not cancel; forgetting to divide by V leads to severe mark loss.",
            "(6) Esterification equilibrium: CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O; water is a product and NOT in huge excess, so [H2O] MUST be included in Kc."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Omitting water in non-aqueous esterification equilibria — in organic esterification, H2O is formed in stoichiometric amounts and MUST be included in Kc.",
            "Always set up a neat 4-row table: Reaction / Initial moles / Change / Equilibrium moles / Equilibrium concentration.",
            "Check whether volume cancels before calculating; if volume is given, always show the division by V.",
            "Check that Kc is positive; negative or zero Kc is impossible."
        ],
        "resources": "Usman Pack 13A1 Q26–Q50 & FAQs (ICE Table Kc Calculations)"
    },
    43: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.2)",
        "subtopic": "The Equilibrium Constant Kp: Partial Pressures & Mole Fractions",
        "learning_objective": "Formulate Kp expressions, calculate mole fractions and partial pressures, and deduce Kp units.",
        "what_to_learn": [
            "(1) Gas equilibria: for gas reactions, it is often more convenient to express equilibrium position in terms of partial pressures (Kp).",
            "(2) Mole fraction (xA): fraction of total gas molecules that are species A; xA = nA / n_total (sum of all mole fractions = 1.0).",
            "(3) Dalton's Law of Partial Pressures: partial pressure pA = xA × P_total (sum of partial pressures = total pressure P_total).",
            "(4) Kp expression: for aA(g) + bB(g) ⇌ cC(g) + dD(g), Kp = (pC^c × pD^d) / (pA^a × pB^b).",
            "(5) Notation: use round brackets with small p (e.g. (pNH3)² or p(NH3)²); DO NOT use square brackets.",
            "(6) Heterogeneous gas equilibria: solids and pure liquids are excluded from Kp (e.g. CaCO3(s) ⇌ CaO(s) + CO2(g) → Kp = pCO2).",
            "(7) Units of Kp: deduce from pressure units (kPa, Pa, or atm) raised to the power Δn_gas."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Using square brackets [pA] in Kp expressions — mark schemes penalise square brackets in Kp! Use pA or p(A).",
            "Units of Kp: substitute the exact pressure unit given in the question (e.g. if partial pressures are in kPa, units might be kPa⁻²; do NOT convert to Pa unless requested).",
            "Always check that sum of mole fractions equals 1.000 before calculating partial pressures.",
            "Solids have negligible vapour pressure and are strictly omitted from Kp."
        ],
        "resources": "Usman Pack 13A2 Q1–Q25 (Mole Fractions and Kp Expressions)"
    },
    44: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.2)",
        "subtopic": "Complex Kp Calculations: Haber & Contact Process Systems",
        "learning_objective": "Calculate Kp values from gas equilibrium mixtures and determine equilibrium partial pressures.",
        "what_to_learn": [
            "(1) Haber Process Kp: N2(g) + 3H2(g) ⇌ 2NH3(g); Kp = (pNH3)² / ((pN2) × (pH2)³); units: kPa⁻² or atm⁻².",
            "(2) Step-by-step calculation: (a) Find equilibrium moles of all gases; (b) Find total moles n_total; (c) Calculate mole fractions x = n/n_total; (d) Multiply by P_total to get pA; (e) Substitute into Kp.",
            "(3) Contact Process Kp: 2SO2(g) + O2(g) ⇌ 2SO3(g); Kp = (pSO3)² / ((pSO2)² × pO2).",
            "(4) Dissociation of N2O4: N2O4(g) ⇌ 2NO2(g); if fraction α dissociates, total moles = 1 + α; calculate Kp in terms of P_total and α.",
            "(5) Decomposition of PCl5: PCl5(g) ⇌ PCl3(g) + Cl2(g); Kp = (pPCl3 × pCl2) / pPCl5; units: kPa or atm."
        ],
        "how_to_outstand": [
            "Show every intermediate step: n_total, individual x values, individual p values, and final substitution.",
            "Double-check powers in denominator: in Haber process, pH2 is CUBED (³).",
            "Give final answers to 3 significant figures with correct units."
        ],
        "resources": "Usman Pack 13A2 Q26–Q50 & FAQs (Haber & Contact Kp Problems)"
    },
    45: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.3)",
        "subtopic": "Factors Affecting K 1: Temperature Dependence",
        "learning_objective": "Explain why temperature is the ONLY factor that changes equilibrium constants Kc and Kp.",
        "what_to_learn": [
            "(1) Temperature is the ONLY variable that alters the numerical value of Kc and Kp.",
            "(2) Exothermic reactions (ΔH < 0, e.g. Haber process): increasing temperature shifts equilibrium to the left (Le Chatelier) → [products] decrease, [reactants] increase → Kc and Kp DECREASE.",
            "(3) Decreasing temperature for exothermic reaction: shifts equilibrium to the right → Kc and Kp INCREASE.",
            "(4) Endothermic reactions (ΔH > 0, e.g. N2O4 ⇌ 2NO2): increasing temperature shifts equilibrium to the right → [products] increase, [reactants] decrease → Kc and Kp INCREASE.",
            "(5) Decreasing temperature for endothermic reaction: shifts equilibrium to the left → Kc and Kp DECREASE.",
            "(6) Van 't Hoff relationship: quantitative link between ln K and 1/T (ln K = -ΔH/RT + constant)."
        ],
        "how_to_outstand": [
            "State clearly: 'Temperature is the ONLY factor that changes the value of Kc and Kp.'",
            "When explaining why K changes with T: quote Le Chatelier's principle AND specify how the numerator and denominator of the K expression change.",
            "Connect to Topic 12 entropy: as T rises, -ΔH/T decreases, altering ΔS_total and therefore K (since ΔS_total = R ln K)."
        ],
        "resources": "Usman Pack 13A3 Q1–Q50 & FAQs (Temperature Effects on K)"
    },
    48: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.4)",
        "subtopic": "Factors Affecting K 2: Why Pressure, Concentration & Catalysts Do NOT Change K",
        "learning_objective": "Explain why pressure, concentration, and catalysts shift equilibrium positions while keeping K completely constant.",
        "what_to_learn": [
            "(1) Changing pressure: does NOT change Kp! For N2 + 3H2 ⇌ 2NH3, doubling total pressure initially quadruples the denominator more than the numerator (ratio Q < Kp).",
            "(2) To restore the ratio back to the constant Kp value, the position of equilibrium shifts to the right (fewer gas molecules), increasing pNH3 until Q = Kp again.",
            "(3) Changing concentration: does NOT change Kc! Adding reactant momentarily decreases reaction quotient Q below Kc; equilibrium shifts right until [products]/[reactants] ratio equals Kc again.",
            "(4) Adding a catalyst: does NOT change Kc or Kp! A catalyst increases the rates of forward and reverse reactions by the EXACT SAME factor (lowers forward and reverse Ea equally).",
            "(5) Adding an inert gas at constant volume: partial pressures of reactants and products are unchanged → no shift in equilibrium.",
            "(6) Adding an inert gas at constant pressure: total volume increases, partial pressures decrease → shifts towards side with more gas moles."
        ],
        "how_to_outstand": [
            "MAJOR EXAMINER TRAP: Candidates write 'increasing pressure increases Kp' — NO! Kp is completely UNCHANGED by pressure.",
            "Explain in terms of the reaction quotient / expression ratio: 'The system shifts to the side with fewer moles of gas so that the ratio of partial pressures returns to the constant value of Kp.'",
            "A catalyst speeds up attainment of equilibrium, but has ZERO effect on yield or K."
        ],
        "resources": "Usman Pack 13A4 Q1–Q50 & FAQs (Pressure, Concentration & Catalyst Proofs)"
    },
    49: {
        "topic_code": "Topic 13 — Chemical Equilibria (13A.5)",
        "subtopic": "Relating Entropy to Equilibrium Constants: ΔS_total = R ln K",
        "learning_objective": "Derive and apply the fundamental thermodynamic relationship ΔS_total = R ln K.",
        "what_to_learn": [
            "(1) Fundamental equation: ΔS_total = R ln K, linking the total entropy change to the equilibrium constant.",
            "(2) R = gas constant (8.31 J K⁻¹ mol⁻¹); K = equilibrium constant (Kc or Kp in dimensionless standard state ratio).",
            "(3) Rearranged formula: K = e^(ΔS_total / R).",
            "(4) Physical interpretation: (a) If ΔS_total > 0, ln K > 0 → K > 1 (equilibrium favours products); (b) If ΔS_total >> 0 (+100 J K⁻¹ mol⁻¹), K is very large (reaction goes virtually to completion).",
            "(5) (c) If ΔS_total < 0, ln K < 0 → K < 1 (equilibrium favours reactants); (d) If ΔS_total = 0, ln K = 0 → K = 1 (equal tendency forward and reverse).",
            "(6) Connection to temperature: since ΔS_total = ΔS_system - ΔH/T, as T changes, ΔS_total changes, which explains quantitatively WHY K changes with temperature."
        ],
        "how_to_outstand": [
            "Show the mathematical derivation: K = e^(ΔS_total / R).",
            "Be very careful with units: ΔS_total MUST be in J K⁻¹ mol⁻¹ before dividing by R (8.31 J K⁻¹ mol⁻¹).",
            "Explain why a tiny increase in ΔS_total causes a massive increase in K: exponential relationship!",
            "Connect to Gibbs Free Energy: ΔG = -T ΔS_total = -RT ln K."
        ],
        "resources": "Usman Pack 13A5 Q1–Q50 & FAQs (Entropy and K Relationships)"
    },
    50: {
        "topic_code": "Topic 13 — Thinking Bigger & Synoptic Equilibria",
        "subtopic": "Catastrophe for Coral: Ocean Acidification & Carbonate Equilibria",
        "learning_objective": "Apply chemical equilibria and Le Chatelier's principle to analyze ocean acidification and coral reef degradation.",
        "what_to_learn": [
            "(1) Thinking Bigger Case Study: Atmospheric CO2 dissolves in oceans: CO2(g) ⇌ CO2(aq).",
            "(2) Acid formation: CO2(aq) + H2O(l) ⇌ H2CO3(aq) ⇌ H⁺(aq) + HCO3⁻(aq).",
            "(3) Carbonate depletion: H⁺ ions react with dissolved carbonate ions: H⁺(aq) + CO3²⁻(aq) ⇌ HCO3⁻(aq).",
            "(4) Impact on coral calcification: corals build calcium carbonate skeletons: Ca²⁺(aq) + CO3²⁻(aq) ⇌ CaCO3(s).",
            "(5) Le Chatelier analysis: as [CO3²⁻] falls due to reaction with H⁺, the calcification equilibrium shifts left, preventing coral growth and dissolving existing aragonite/calcite reefs.",
            "(6) Temperature feedback: warmer oceans hold less dissolved CO2 (Henry's law, exothermic dissolution), but increased atmospheric pCO2 drives overall ocean pH down (from 8.2 to 8.1, a 26% increase in [H⁺])."
        ],
        "how_to_outstand": [
            "Write all four linked equilibrium equations sequentially.",
            "Explain why a 0.1 unit drop in pH represents a major biological hazard: pH is a logarithmic scale, so ΔpH = -0.1 means [H⁺] has increased by factor 10^0.1 = 1.26 (+26%).",
            "Show how carbonate ion concentration governs the saturation state (Ω) of aragonite."
        ],
        "resources": "Topic 13 Thinking Bigger Case Study & Carbonate Equilibria"
    },
    51: {
        "topic_code": "Topic 13 — Exam Practice",
        "subtopic": "Unit 4 Topic 13 Exam Practice & Past Paper Synthesis",
        "learning_objective": "Synthesize Kc, Kp, Le Chatelier proofs, and ΔS_total = R ln K under timed exam conditions.",
        "what_to_learn": [
            "(1) Solving multi-part equilibrium past paper questions under timed conditions.",
            "(2) ICE table calculation speed and accuracy drills.",
            "(3) Perfecting written explanations for why catalysts and pressure do not change K.",
            "(4) Auditing unit deductions and significant figures."
        ],
        "how_to_outstand": [
            "Master ICE table setup with algebraic x terms.",
            "Review Top 10 Examiner FAQs from Pack 13A."
        ],
        "resources": "Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf (Complete 50Q Pack)"
    },
    52: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14A.1)",
        "subtopic": "The Brønsted-Lowry Theory: Conjugate Pairs & Amphiprotic Species",
        "learning_objective": "Define Brønsted-Lowry acids and bases, identify conjugate acid-base pairs, and explain amphiprotic behaviour.",
        "what_to_learn": [
            "(1) Brønsted-Lowry Acid: a proton (H⁺ ion) DONOR.",
            "(2) Brønsted-Lowry Base: a proton (H⁺ ion) ACCEPTOR.",
            "(3) Conjugate acid-base pair: two species that transform into each other by the gain or loss of a SINGLE proton (H⁺).",
            "(4) Examples: CH3COOH (acid) / CH3COO⁻ (conjugate base); NH4⁺ (conjugate acid) / NH3 (base); H3O⁺ / H2O; H2O / OH⁻.",
            "(5) Amphiprotic / Amphoteric species: can act as either an acid (donate H⁺) or a base (accept H⁺) depending on reaction conditions.",
            "(6) Water as amphiprotic: in HCl + H2O → H3O⁺ + Cl⁻, H2O acts as a base; in NH3 + H2O ⇌ NH4⁺ + OH⁻, H2O acts as an acid.",
            "(7) Non-aqueous acid-base systems: H2SO4 + HNO3 ⇌ H2NO3⁺ + HSO4⁻ (H2SO4 acts as acid, HNO3 acts as base)."
        ],
        "how_to_outstand": [
            "Conjugate pairs MUST differ by exactly ONE H⁺ ion (e.g. H2SO4 and SO4²⁻ are NOT a conjugate pair — H2SO4 and HSO4⁻ are).",
            "Clearly label both conjugate pairs in any given equation (Acid 1 / Base 1 and Acid 2 / Base 2).",
            "In non-aqueous acid mixtures: the STRONGER acid donates a proton to the weaker acid (e.g. H2SO4 protonates HNO3 in the nitrating mixture)."
        ],
        "resources": "Usman Pack 14A1 Q1–Q50 & FAQs (Brønsted-Lowry Theory)"
    },
    55: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14A.2)",
        "subtopic": "Hydrogen Ion Concentration & The pH Scale: Strong Acids",
        "learning_objective": "Calculate pH and [H⁺] for strong monobasic and dibasic acids, including dilution effects.",
        "what_to_learn": [
            "(1) pH definition: pH = -log₁₀[H⁺]  (or [H⁺] = 10^(-pH)).",
            "(2) Strong acid definition: an acid that is COMPLETELY DISSOCIATED into ions in aqueous solution (e.g. HCl, HNO3, HClO4).",
            "(3) Strong monobasic acid calculation: [H⁺] = c_acid; e.g. 0.050 mol dm⁻³ HCl has [H⁺] = 0.050 mol dm⁻³ → pH = -log(0.050) = 1.30.",
            "(4) Strong dibasic acid calculation: H2SO4 dissociates fully in dilute solution to release 2 protons; [H⁺] = 2 × c_acid; e.g. 0.025 mol dm⁻³ H2SO4 has [H⁺] = 0.050 mol dm⁻³ → pH = 1.30.",
            "(5) Dilution formula: c1 V1 = c2 V2; diluting a strong acid by a factor of 10 increases its pH by exactly 1 unit (e.g. pH 1.0 to 2.0).",
            "(6) Significant figures rule for pH: the number of decimal places in pH equals the number of significant figures in [H⁺] (e.g. [H⁺] = 2.4 × 10⁻³ (2 s.f.) → pH = 2.62 (2 d.p.)).",
            "(7) Negative pH: possible for very concentrated strong acids (e.g. 2.0 mol dm⁻³ HCl has pH = -log(2.0) = -0.30)."
        ],
        "how_to_outstand": [
            "Always quote pH values to TWO DECIMAL PLACES.",
            "Remember that H2SO4 releases TWO protons per mole in dilute solution — multiply concentration by 2 before taking -log.",
            "Dilution questions: always calculate total final volume (V1 + V_water) to find new concentration."
        ],
        "resources": "Usman Pack 14A2 Q1–Q50 & FAQs (pH Scale and Strong Acids)"
    },
    56: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14A.3)",
        "subtopic": "The Ionic Product of Water Kw & Strong Bases",
        "learning_objective": "Calculate pH for strong bases using Kw, and evaluate the effect of temperature on water neutrality.",
        "what_to_learn": [
            "(1) Auto-ionisation of water: H2O(l) ⇌ H⁺(aq) + OH⁻(aq)  (ΔH = +57.4 kJ mol⁻¹, endothermic).",
            "(2) Ionic product of water Kw: Kw = [H⁺][OH⁻] = 1.00 × 10⁻¹⁴ mol² dm⁻⁶ at 298 K (25 °C).",
            "(3) pKw definition: pKw = -log₁₀ Kw = 14.00 at 298 K; pH + pOH = pKw.",
            "(4) Strong base calculations: strong bases (NaOH, KOH, Ba(OH)2) dissociate completely.",
            "(5) Step-by-step strong base pH: (a) Find [OH⁻] = c_base (or 2 × c_base for Ba(OH)2); (b) [H⁺] = Kw / [OH⁻]; (c) pH = -log[H⁺].",
            "(6) Worked example: 0.15 mol dm⁻³ Ba(OH)2 → [OH⁻] = 0.30 mol dm⁻³ → [H⁺] = (1.0×10⁻¹⁴)/0.30 = 3.33×10⁻¹⁴ → pH = 13.48.",
            "(7) Temperature effect on Kw: auto-ionisation is endothermic; increasing temperature shifts equilibrium to the right → Kw increases.",
            "(8) Neutrality at higher temperature: at 373 K (100 °C), Kw = 5.13 × 10⁻¹³ mol² dm⁻⁶ → [H⁺] = √Kw = 7.16 × 10⁻⁷ mol dm⁻³ → pH = 6.14.",
            "(9) WHY water is still neutral at pH 6.14: neutrality is defined as [H⁺] = [OH⁻], NOT pH = 7! Since [H⁺] = [OH⁻], boiling water is strictly neutral."
        ],
        "how_to_outstand": [
            "MAJOR EXAMINER TRAP: Candidates state water at 50 °C is acidic because pH < 7 — NO! Water is STRICTLY NEUTRAL because [H⁺] = [OH⁻]. pH 7 is neutral ONLY at 298 K.",
            "Ba(OH)2 is dibasic: multiply concentration by 2 to get [OH⁻].",
            "Always state: auto-ionisation of water is endothermic, so increasing T shifts equilibrium right (Le Chatelier), increasing Kw."
        ],
        "resources": "Usman Pack 14A3 Q1–Q50 & FAQs (Kw and Strong Bases)"
    },
    57: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14A.4)",
        "subtopic": "Weak Acids: Acid Dissociation Constant Ka & pKa",
        "learning_objective": "Formulate Ka expressions, calculate weak acid pH using standard approximations, and define pKa.",
        "what_to_learn": [
            "(1) Weak acid definition: an acid that is only PARTIALLY dissociated into ions in aqueous solution (e.g. CH3COOH, HCOOH, HCN).",
            "(2) Acid dissociation constant Ka: for HA(aq) ⇌ H⁺(aq) + A⁻(aq), Ka = ([H⁺][A⁻]) / [HA]; units: mol dm⁻³.",
            "(3) pKa definition: pKa = -log₁₀ Ka  (Ka = 10^(-pKa)); smaller pKa → larger Ka → stronger acid.",
            "(4) Weak acid pH derivation: Assumption 1: [H⁺] ≈ [A⁻] (H⁺ from auto-ionisation of water is negligible); Assumption 2: [HA]eq ≈ [HA]initial (dissociation is very small, < 5%).",
            "(5) Simplified formula: Ka = [H⁺]² / c_acid  →  [H⁺] = √(Ka × c_acid).",
            "(6) Calculating pH: pH = -log[H⁺] = -log√(Ka × c_acid) = ½(pKa - log c_acid).",
            "(7) Calculating Ka from pH: [H⁺] = 10^(-pH) → Ka = [H⁺]² / c_acid."
        ],
        "how_to_outstand": [
            "State BOTH assumptions explicitly when asked: (1) [H⁺] = [A⁻] (dissociation of water ignored); (2) [HA] at equilibrium = initial concentration (negligible dissociation).",
            "When Assumption 2 breaks down: if Ka is relatively large (> 10⁻³ mol dm⁻³) or the solution is very dilute, quadratic formula must be used.",
            "Compare acid strengths: acid with lower pKa is stronger because it dissociates to a greater extent.",
            "Always state units of Ka: mol dm⁻³."
        ],
        "resources": "Usman Pack 14A4 Q1–Q25 (Ka Expressions and Weak Acid pH)"
    },
    58: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14A.4)",
        "subtopic": "Weak Acid Dilution, Degree of Dissociation & Inductive Effects",
        "learning_objective": "Calculate degree of dissociation α, evaluate dilution effects on weak acid pH, and explain inductive effects on Ka.",
        "what_to_learn": [
            "(1) Degree of dissociation (α): fraction of acid molecules that dissociate; α = [H⁺] / c_acid = √(Ka / c_acid).",
            "(2) Percentage dissociation: % = α × 100%.",
            "(3) Dilution effect on weak acids: diluting a weak acid 10-fold increases its pH by only ~0.5 units (contrast with 1.0 unit for strong acids).",
            "(4) Why % dissociation increases with dilution: Ostwald's dilution law; adding water shifts HA ⇌ H⁺ + A⁻ to the right (Le Chatelier).",
            "(5) Inductive effects on carboxylic acid strength: electronegative halogen substituents on the alpha carbon (e.g. ClCH2COOH vs CH3COOH).",
            "(6) Mechanism of inductive effect: -I electron-withdrawing effect delocalises and disperses negative charge on carboxylate anion (-COO⁻), stabilising conjugate base and increasing Ka.",
            "(7) Strength order: CCl3COOH (pKa 0.65) > CHCl2COOH (1.29) > CH2ClCOOH (2.86) > CH3COOH (4.76)."
        ],
        "how_to_outstand": [
            "Explain inductive effect: 'Electronegative chlorine atoms withdraw electron density through the sigma bonds (-I effect), stabilising the carboxylate anion by dispersing negative charge, shifting dissociation equilibrium to the right.'",
            "Dilution comparison: strong acid pH increases by 1.0 per 10× dilution; weak acid pH increases by ~0.5 per 10× dilution (because [H⁺] = √(Ka × c/10) = [H⁺]/√10 = [H⁺]/3.16).",
            "Quote degree of dissociation as a fraction or percentage."
        ],
        "resources": "Usman Pack 14A4 Q26–Q50 & FAQs (Dilution and Inductive Effects on Ka)"
    },
    59: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14B.1)",
        "subtopic": "Acid-Base Titrations: Four Titration Curve Profiles & Equivalence Points",
        "learning_objective": "Sketch, annotate, and interpret pH curves for the four combinations of strong and weak acids and bases.",
        "what_to_learn": [
            "(1) Strong Acid – Strong Base (e.g. HCl + NaOH): starts at pH ~1; flat initial region; huge vertical equivalence section from pH 3 to 11; equivalence point at pH 7.0; ends at pH ~13.",
            "(2) Weak Acid – Strong Base (e.g. CH3COOH + NaOH): starts at pH ~3; initial steep rise followed by flat BUFFER REGION; vertical section from pH 7 to 11; equivalence point > 7 (pH ~8.5–9.0 due to basic A⁻ salt hydrolysis); ends at pH ~13.",
            "(3) Strong Acid – Weak Base (e.g. HCl + NH3): starts at pH ~1; vertical section from pH 3 to 7; equivalence point < 7 (pH ~5.0 due to acidic NH4⁺ salt hydrolysis); flat buffer region at pH ~9; ends at pH ~11.",
            "(4) Weak Acid – Weak Base (e.g. CH3COOH + NH3): starts at pH ~3; no steep vertical section (gradual inflection point around pH 7); ends at pH ~11; NO suitable indicator can detect end-point.",
            "(5) Equivalence point: the point at which stoichiometric amounts of acid and base have reacted.",
            "(6) End-point: the point at which the indicator changes colour."
        ],
        "how_to_outstand": [
            "Clearly label all key features on sketches: initial pH, buffer region, vertical equivalence region, equivalence point volume and pH, and final plateau pH.",
            "Explain why WA-SB equivalence point is > 7: the conjugate base of the weak acid (e.g. CH3COO⁻) hydrolyses water: CH3COO⁻ + H2O ⇌ CH3COOH + OH⁻, producing alkaline solution.",
            "Explain why SA-WB equivalence point is < 7: NH4⁺ hydrolyses water: NH4⁺ + H2O ⇌ NH3 + H3O⁺, producing acidic solution.",
            "Explain why WA-WB has no sharp end-point: vertical section is missing, so indicator colour changes gradually over several cm³."
        ],
        "resources": "Usman Pack 14B1 Q1–Q25 (Titration Curves and Equivalence Points)"
    },
    62: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14B.1)",
        "subtopic": "Acid-Base Indicators: Equilibrium & Selection Principles",
        "learning_objective": "Explain how indicators work as weak acids and select appropriate indicators based on titration curve vertical regions.",
        "what_to_learn": [
            "(1) Indicator nature: an acid-base indicator is a weak acid (HIn) where the un-ionised acid has a distinctly different colour from its conjugate base (In⁻).",
            "(2) Equilibrium: HIn(aq) ⇌ H⁺(aq) + In⁻(aq)  (Colour A ⇌ Colour B).",
            "(3) Indicator constant KIn: KIn = ([H⁺][In⁻]) / [HIn]; pKIn = -log KIn.",
            "(4) Midpoint of colour change: when [HIn] = [In⁻], [H⁺] = KIn → pH = pKIn.",
            "(5) Working pH range: colour change is detectable over approximately pH = pKIn ± 1 (a 2 pH unit range).",
            "(6) Selection criterion: the indicator's pH transition range MUST fall completely within the vertical section of the titration curve.",
            "(7) Common indicators: Methyl orange (pH range 3.1–4.4, pKin 3.7; red in acid, yellow in alkali); Phenolphthalein (pH range 8.3–10.0, pKin 9.3; colourless in acid, pink in alkali).",
            "(8) Matchings: SA-SB (either works); WA-SB (only phenolphthalein); SA-WB (only methyl orange); WA-WB (neither works)."
        ],
        "how_to_outstand": [
            "Selection rule: 'The indicator's pH range must coincide with the vertical section / rapid pH change of the titration curve.'",
            "Explain why methyl orange fails for WA-SB: vertical section is pH 7–11; methyl orange changes colour at pH 3.1–4.4, which is in the buffer region long before the equivalence point.",
            "Explain why phenolphthalein fails for SA-WB: changes at pH 8.3–10.0, which is after the equivalence point in the weak base plateau.",
            "In Le Chatelier terms: adding acid increases [H⁺], shifting HIn ⇌ H⁺ + In⁻ left to Colour A; adding alkali removes H⁺, shifting right to Colour B."
        ],
        "resources": "Usman Pack 14B1 Q26–Q50 & FAQs (Indicator Selection and Working Ranges)"
    },
    63: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14B.2)",
        "subtopic": "Buffer Solutions: Types & Mechanism of Buffer Action",
        "learning_objective": "Define buffer solutions, classify acidic and basic buffers, and write chemical equations explaining buffer action.",
        "what_to_learn": [
            "(1) Buffer solution definition: a solution that resists changes in pH when small amounts of acid or alkali are added.",
            "(2) Acidic buffer: mixture of a weak acid and its conjugate base salt (e.g. ethanoic acid CH3COOH + sodium ethanoate CH3COONa).",
            "(3) Reservoir of species in acidic buffer: large reservoir of un-ionised weak acid HA and large reservoir of conjugate base A⁻.",
            "(4) Buffer action when small amount of H⁺ added: added H⁺ reacts with conjugate base reservoir: A⁻(aq) + H⁺(aq) → HA(aq); [H⁺] is removed, pH remains almost constant.",
            "(5) Buffer action when small amount of OH⁻ added: added OH⁻ reacts with weak acid reservoir: HA(aq) + OH⁻(aq) → A⁻(aq) + H2O(l); [OH⁻] is removed, pH remains almost constant.",
            "(6) Basic buffer: mixture of a weak base and its conjugate acid salt (e.g. ammonia NH3 + ammonium chloride NH4Cl).",
            "(7) Preparing buffers: (a) mixing weak acid + salt directly; (b) partial neutralisation of weak acid with half-moles of strong base (e.g. excess CH3COOH + NaOH)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Stating a buffer 'prevents any pH change' — buffers RESIST pH changes (pH changes only slightly, not zero).",
            "Always write full ionic equations for buffer action: adding H⁺ reacts with A⁻ (not salt); adding OH⁻ reacts with HA.",
            "Explain WHY pH stays almost constant: the ratio [A⁻]/[HA] changes only marginally when small amounts of H⁺ or OH⁻ are added.",
            "State why strong acids cannot form buffers: strong acids dissociate completely, leaving no reservoir of un-ionised acid to absorb added OH⁻."
        ],
        "resources": "Usman Pack 14B2 Q1–Q25 (Buffer Definitions and Action Equations)"
    },
    64: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14B.2)",
        "subtopic": "Calculating Buffer pH: The Henderson-Hasselbalch Equation",
        "learning_objective": "Calculate buffer pH using the Henderson-Hasselbalch equation and determine pH changes upon adding acid or alkali.",
        "what_to_learn": [
            "(1) Ka expression for buffer: Ka = ([H⁺][A⁻]) / [HA]  →  [H⁺] = Ka × ([HA] / [A⁻]).",
            "(2) Henderson-Hasselbalch equation: pH = pKa + log₁₀([A⁻] / [HA])  (or pH = pKa + log([salt] / [acid])).",
            "(3) Equimolar buffer ([A⁻] = [HA]): log(1) = 0 → pH = pKa; the buffer pH is determined by the pKa of the weak acid.",
            "(4) Calculating pH after adding strong acid (H⁺): moles of HA increase (n_HA + x); moles of A⁻ decrease (n_A⁻ - x); recalculate ratio.",
            "(5) Calculating pH after adding strong base (OH⁻): moles of HA decrease (n_HA - x); moles of A⁻ increase (n_A⁻ + x); recalculate ratio.",
            "(6) Buffer capacity: greatest when [A⁻] = [HA] (pH = pKa) and when concentrations of components are high."
        ],
        "how_to_outstand": [
            "In Henderson-Hasselbalch: ensure salt/base is on TOP and acid is on BOTTOM: +log([A⁻]/[HA]).",
            "When adding acid/base: show moles calculation first before finding new ratio.",
            "Notice that volume cancels in [A⁻]/[HA] ratio — mole ratio n(A⁻)/n(HA) can be used directly.",
            "Always verify: adding acid MUST lower pH slightly; adding alkali MUST raise pH slightly."
        ],
        "resources": "Usman Pack 14B2 Q26–Q50 & FAQs (Henderson-Hasselbalch Calculations)"
    },
    65: {
        "topic_code": "Topic 14 — Acid-Base Equilibria (14B.3)",
        "subtopic": "Buffers and pH Curves: The Half-Equivalence Point",
        "learning_objective": "Analyze the buffer region on titration curves and prove that pH = pKa at the half-equivalence point.",
        "what_to_learn": [
            "(1) Buffer region on titration curve: the relatively flat section of a weak acid – strong base titration curve before the vertical equivalence jump.",
            "(2) Half-equivalence point: the point during titration where exactly HALF of the initial weak acid has been neutralised by strong base.",
            "(3) Volume relationship: V(half-equivalence) = ½ × V(equivalence).",
            "(4) Species concentrations at half-equivalence: [HA] = [A⁻] (exactly half converted to salt).",
            "(5) Proof that pH = pKa: Ka = ([H⁺][A⁻])/[HA]; since [A⁻] = [HA], Ka = [H⁺] → -log Ka = -log[H⁺] → pKa = pH.",
            "(6) Experimental determination of Ka: read pH at half-equivalence volume directly off the titration curve; Ka = 10^(-pH)."
        ],
        "how_to_outstand": [
            "Use the titration curve to find Ka: find equivalence volume (e.g. 24.0 cm³) → halve it (12.0 cm³) → read pH at 12.0 cm³ (e.g. 4.76) → Ka = 10^(-4.76) = 1.74 × 10⁻⁵ mol dm⁻³.",
            "Explain why the curve is flattest at half-equivalence: buffer capacity is maximum because [HA] = [A⁻].",
            "Examiners reward concise proof: 'At half-equivalence, [HA] = [A⁻], so Ka = [H⁺], hence pH = pKa.'"
        ],
        "resources": "Usman Pack 14B3 Q1–Q25 (Half-Equivalence Point Analysis)"
    },
    66: {
        "topic_code": "Topic 14 — Thinking Bigger & Biological Buffers",
        "subtopic": "A Problem Grows: Biological Buffers & Blood pH Regulation",
        "learning_objective": "Evaluate physiological buffer systems maintaining human arterial blood pH between 7.35 and 7.45.",
        "what_to_learn": [
            "(1) Blood pH homeostasis: normal arterial blood pH is tightly regulated at 7.40 ± 0.05; pH < 7.35 = acidosis; pH > 7.45 = alkalosis.",
            "(2) Carbonic acid – hydrogencarbonate buffer system: H2CO3(aq) ⇌ H⁺(aq) + HCO3⁻(aq).",
            "(3) Open buffer system linked to respiration: CO2(g) [lungs] ⇌ CO2(aq) + H2O(l) ⇌ H2CO3(aq) ⇌ H⁺(aq) + HCO3⁻(aq).",
            "(4) Response to excess H⁺ (e.g. lactic acid from exercise): H⁺ + HCO3⁻ → H2CO3 → H2O + CO2; breathing rate increases to expel CO2.",
            "(5) Response to excess OH⁻: OH⁻ + H2CO3 → HCO3⁻ + H2O; kidneys regulate [HCO3⁻] by excretion/reabsorption.",
            "(6) Ratio in blood: at pH 7.40, [HCO3⁻]/[H2CO3] ≈ 20:1; skewed towards base to protect against metabolic acid accumulation."
        ],
        "how_to_outstand": [
            "Explain why the carbonic acid buffer is uniquely effective in vivo: it is an OPEN system where CO2 can be vented via lungs and HCO3⁻ retained by kidneys.",
            "Use Henderson-Hasselbalch to calculate blood ratio: pH = pKa + log([HCO3⁻]/[H2CO3]); with pKa = 6.1, 7.4 = 6.1 + log(20) → ratio = 20."
        ],
        "resources": "Topic 14 Thinking Bigger Case Study & Biological Buffers"
    },
    69: {
        "topic_code": "Topic 15 — Organic Chemistry (15A.1)",
        "subtopic": "Chirality & Enantiomers: Asymmetric Carbons & 3D Stereochemistry",
        "learning_objective": "Identify chiral centres, represent 3D enantiomers, and explain non-superimposable mirror images.",
        "what_to_learn": [
            "(1) Chiral (asymmetric) carbon: a carbon atom bonded to FOUR DIFFERENT atoms or groups of atoms.",
            "(2) Enantiomers (optical isomers): non-superimposable mirror image forms of a chiral molecule.",
            "(3) 3D tetrahedral drawing conventions: solid line (in plane), wedged bond (pointing out towards viewer), dashed bond (pointing into page).",
            "(4) Drawing enantiomers: draw a vertical dashed mirror line; reflect the four groups across the mirror ensuring 3D tetrahedral geometry is preserved.",
            "(5) Identical physical properties: enantiomers have identical melting points, boiling points, densities, and solubilities in achiral solvents.",
            "(6) Distinguishing enantiomers: they differ ONLY in: (a) the direction in which they rotate plane-polarised light; (b) interactions with other chiral molecules (e.g. biological enzymes and drug receptors)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates miss chiral carbons in rings — check ring carbons by tracing both pathways around the ring; if paths differ, the carbon is chiral.",
            "When drawing 3D structures: ensure tetrahedral bond angles (~109.5°) look realistic with two in-plane bonds, one wedge, one dash.",
            "Always label chiral centres with an asterisk (*).",
            "Molecules with multiple chiral centres: a molecule with n chiral centres can have up to 2^n stereoisomers (enantiomers and diastereomers)."
        ],
        "resources": "Usman Pack 15A1 Q1–Q50 & FAQs (Chirality and 3D Drawings)"
    },
    70: {
        "topic_code": "Topic 15 — Organic Chemistry (15A.2)",
        "subtopic": "Optical Activity & Polarimetry: Racemic Mixtures",
        "learning_objective": "Explain how polarimeters detect optical activity and why racemic mixtures are optically inactive.",
        "what_to_learn": [
            "(1) Plane-polarised light: light waves that oscillate in a SINGLE plane, produced by passing unpolarised light through a Polaroid filter.",
            "(2) Polarimeter operation: polarised light passes through a tube containing the sample; an analyser filter is rotated to measure angle of optical rotation (α).",
            "(3) Dextrorotatory (+ or d): rotates plane of polarised light CLOCKWISE.",
            "(4) Laevorotatory (- or l): rotates plane of polarised light ANTICLOCKWISE by the exact same angle.",
            "(5) Racemic mixture (racemate): an EQUIMOLAR (50:50) mixture of two enantiomers.",
            "(6) Optical inactivity of racemates: the clockwise rotation by one enantiomer is EXACTLY CANCELLED by the equal anticlockwise rotation of the other enantiomer (net rotation = 0°).",
            "(7) Enantiomeric excess (ee): percentage excess of one enantiomer over the other in a non-racemic mixture."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Saying a racemate is inactive because 'the molecule is not chiral' — the molecules ARE individually chiral, but optical rotation is CANCELLED by equal amounts of both enantiomers.",
            "Phrase to memorize: 'Clockwise rotation of one enantiomer is cancelled by the equal anticlockwise rotation of the other enantiomer.'",
            "Thalidomide case study: (R)-enantiomer is a safe sedative; (S)-enantiomer causes severe birth defects (teratogen); in vivo racemisation occurs rapidly."
        ],
        "resources": "Usman Pack 15A2 Q1–Q50 & FAQs (Optical Activity and Polarimetry)"
    },
    71: {
        "topic_code": "Topic 15 — Organic Chemistry (15A.3)",
        "subtopic": "Optical Activity and Reaction Mechanisms: Stereochemical Evidence",
        "learning_objective": "Use stereochemical outcomes of reactions to provide definitive evidence for SN1 vs SN2 and nucleophilic addition mechanisms.",
        "what_to_learn": [
            "(1) SN1 stereochemical outcome: proceeds via a TRIGONAL PLANAR carbocation intermediate in the slow step.",
            "(2) Attack on planar carbocation: nucleophile has an EQUAL PROBABILITY of attacking from either the top face or bottom face.",
            "(3) Result of SN1: produces an equimolar (50:50) RACEMIC MIXTURE → loss of optical activity (racemisation).",
            "(4) SN2 stereochemical outcome: nucleophile attacks the back of the C-X bond (180° to leaving group) simultaneously as leaving group departs.",
            "(5) Result of SN2: complete WALDEN INVERSION of configuration (like an umbrella turning inside out) → product is a SINGLE ENANTIOMER (optically active).",
            "(6) Nucleophilic addition to planar carbonyls: adding HCN to aldehydes (except methanal) or unsymmetrical ketones produces a chiral hydroxynitrile.",
            "(7) Since the C=O group is trigonal planar, CN⁻ attacks with equal probability from above and below the plane → RACEMIC MIXTURE (optically inactive)."
        ],
        "how_to_outstand": [
            "In organic mechanism exams, quote the geometry: 'The intermediate/carbonyl is TRIGONAL PLANAR around the carbon atom.'",
            "Quote the probability: 'The nucleophile can attack with EQUAL PROBABILITY from EITHER SIDE / FACE of the plane.'",
            "Conclude the optical outcome: 'Producing an EQUAL AMOUNT of both enantiomers, forming a RACEMATE which is OPTICALLY INACTIVE.'"
        ],
        "resources": "Usman Pack 15A3 Q1–Q50 & FAQs (Mechanisms and Stereochemistry)"
    },
    72: {
        "topic_code": "Topic 15 — Organic Chemistry (15B.1)",
        "subtopic": "Carbonyl Compounds: Structures & Physical Properties",
        "learning_objective": "Compare the boiling points and water solubilities of aldehydes and ketones with alkanes and alcohols.",
        "what_to_learn": [
            "(1) Carbonyl group: C=O double bond composed of a strong sigma bond and a pi bond; strongly polar due to electronegative oxygen (δ+ C = O δ-).",
            "(2) Aldehydes (R-CHO): carbonyl group at the end of carbon chain; Ketones (R-CO-R'): carbonyl group within the carbon chain.",
            "(3) Boiling point trends: Alkanes < Aldehydes/Ketones < Alcohols (for similar Mr).",
            "(4) Intermolecular forces in carbonyls: permanent dipole-dipole attractions and London dispersion forces; NO hydrogen bonding between carbonyl molecules (no H bonded to O).",
            "(5) Comparison with alcohols: alcohols have intermolecular hydrogen bonding, so alcohols have significantly higher boiling points than carbonyls.",
            "(6) Solubility in water: lower carbonyls (methanal, ethanal, propanone) are completely miscible with water because lone pairs on oxygen form HYDROGEN BONDS with water molecules.",
            "(7) Chain length effect: solubility decreases as hydrocarbon chain lengthens (non-polar alkyl chain disrupts water H-bonding)."
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: Candidates state aldehydes have hydrogen bonds between molecules — NO! They form hydrogen bonds WITH WATER, but NOT with each other.",
            "Draw the hydrogen bond: show lone pair on carbonyl oxygen, dashed line to delta-plus H of water, and 180° bond angle around H.",
            "Explain boiling point order: Alkanes (London only) < Carbonyls (London + dipole-dipole) < Alcohols (London + dipole-dipole + hydrogen bonding)."
        ],
        "resources": "Usman Pack 15B1 Q1–Q50 & FAQs (Carbonyl Physical Properties)"
    },
    73: {
        "topic_code": "Topic 15 — Organic Chemistry (15B.2)",
        "subtopic": "Redox Reactions of Carbonyl Compounds: Tollens', Fehling's & Reduction",
        "learning_objective": "Differentiate aldehydes and ketones using oxidising agents and formulate reduction equations using NaBH4.",
        "what_to_learn": [
            "(1) Oxidation of aldehydes: aldehydes are easily oxidised to carboxylic acids because of the H atom attached to the carbonyl carbon (R-CHO → R-COOH).",
            "(2) Ketones resist oxidation: ketones have no H atom attached to the carbonyl carbon; C-C bond breaking requires harsh destructive conditions.",
            "(3) Tollens' Reagent (ammoniacal silver nitrate [Ag(NH3)2]⁺): Aldehyde oxidised to carboxylate; Ag⁺ reduced to metallic silver → SILVER MIRROR (or black precipitate). Ketone → no reaction.",
            "(4) Fehling's / Benedict's Solution (alkaline copper(II) tartrate/citrate): Aldehyde oxidised; blue Cu²⁺ reduced to BRICK-RED Cu2O precipitate. Ketone → remains blue.",
            "(5) Acidified potassium dichromate(VI) (K2Cr2O7 / H2SO4): Aldehyde oxidised; orange Cr2O7²⁻ reduced to GREEN Cr³⁺. Ketone → remains orange.",
            "(6) Reduction of carbonyls: sodium tetrahydridoborate(III) (NaBH4) in aqueous alcohol reduces aldehydes to PRIMARY alcohols, and ketones to SECONDARY alcohols.",
            "(7) Formulating equations: use [O] for oxidising agent and 2[H] for reducing agent."
        ],
        "how_to_outstand": [
            "Always state BOTH the initial and final colours: 'Orange to green' (dichromate), 'Blue to brick-red precipitate' (Fehling's), 'Colourless to silver mirror' (Tollens').",
            "Write ionic half-equations: Tollens': Ag⁺ + e⁻ → Ag(s); Fehling's: 2Cu²⁺ + 2OH⁻ + 2e⁻ → Cu2O(s) + H2O(l).",
            "Reducing agents: NaBH4 reduces C=O but DOES NOT reduce C=C double bonds (nucleophilic H⁻ is repelled by electron-rich C=C pi bond)."
        ],
        "resources": "Usman Pack 15B2 Q1–Q50 & FAQs (Redox Reactions of Carbonyls)"
    },
    76: {
        "topic_code": "Topic 15 — Organic Chemistry (15B.3)",
        "subtopic": "Nucleophilic Addition of HCN, 2,4-DNPH & The Iodoform Test",
        "learning_objective": "Master the mechanism of nucleophilic addition of HCN and apply 2,4-DNPH and the tri-iodomethane test for structural identification.",
        "what_to_learn": [
            "(1) Nucleophilic addition of HCN: reagent is KCN/NaCN with dilute H2SO4 (pH 5–8) to provide cyanide nucleophile CN⁻.",
            "(2) Mechanism: Step 1 (slow): :CN⁻ attacks delta-positive carbonyl carbon, breaking C=O pi bond and pushing electron pair to oxygen (alkoxide intermediate).",
            "(3) Step 2 (fast): alkoxide oxygen protonated by H⁺ (or HCN) to form a HYDROXYNITRILE (cyanohydrin).",
            "(4) Synthetic importance: adds one extra carbon atom to the carbon chain; nitrile group (-C≡N) can be hydrolysed to -COOH or reduced to -CH2NH2.",
            "(5) 2,4-DNPH (Brady's reagent): reacts with BOTH aldehydes and ketones via condensation/addition-elimination to form an ORANGE/YELLOW PRECIPITATE.",
            "(6) Characterisation: precipitate is filtered, recrystallised, and its sharp MELTING POINT measured and compared with database values to identify carbonyl.",
            "(7) Tri-iodomethane (iodoform) test: reagent is I2 + NaOH (or NaOI); tests for methyl carbonyl group (CH3-C=O) or methyl secondary alcohol (CH3-CH(OH)-); positive result = PALE YELLOW PRECIPITATE of CHI3 with antiseptic medicinal smell."
        ],
        "how_to_outstand": [
            "In HCN mechanism: curly arrow must start from the LONE PAIR on the CARBON of :CN⁻ (not the nitrogen!).",
            "Explain pH control in HCN reaction: if pH too low, all CN⁻ is converted to molecular HCN (weak acid, no nucleophile); if pH too high, too few H⁺ to protonate alkoxide in step 2.",
            "Iodoform test positives: ethanol is the ONLY primary alcohol that gives positive test; propanal gives NEGATIVE test (no CH3C=O group, it has CH3CH2C=O)."
        ],
        "resources": "Usman Pack 15B3 Q1–Q50 & FAQs (HCN Mechanism, Brady's & Iodoform)"
    },
    77: {
        "topic_code": "Topic 15 — Organic Chemistry (15C.1 & 15C.2)",
        "subtopic": "Carboxylic Acids: Physical Properties & Chemical Reactions",
        "learning_objective": "Explain dimerisation and acidic properties of carboxylic acids and formulate reactions with metals, carbonates, PCl5, and alcohols.",
        "what_to_learn": [
            "(1) Carboxylic acid group (-COOH): polar carbonyl and hydroxyl groups; forms strong intermolecular HYDROGEN BONDS.",
            "(2) Dimerisation: in pure liquid or non-polar solvents, two carboxylic acid molecules pair up via TWO hydrogen bonds to form a stable DIMER.",
            "(3) Physical consequences: very high boiling points (higher than alcohols of same Mr); dimerisation doubles effective molecular mass.",
            "(4) Weak acidity: dissociate partially in water: RCOOH ⇌ RCOO⁻ + H⁺; carboxylate ion RCOO⁻ is resonance-stabilised by delocalisation of negative charge across both oxygen atoms.",
            "(5) Reactions as acids: (a) with reactive metals (Mg) → carboxylate salt + H2(g); (b) with metal carbonates/hydrogencarbonates (Na2CO3) → salt + H2O + CO2(g) (effervescence; tests for -COOH group).",
            "(6) Reaction with phosphorus(V) chloride (PCl5): RCOOH + PCl5 → RCOCl (acyl chloride) + POCl3 + HCl(g) (steamy misty acidic fumes of HCl).",
            "(7) Esterification: RCOOH + R'OH ⇌ RCOOR' + H2O (heated under reflux with concentrated H2SO4 catalyst)."
        ],
        "how_to_outstand": [
            "Draw the carboxylic acid dimer showing two parallel hydrogen bonds (dashed lines) between C=O and H-O of adjacent molecules.",
            "Effervescence with Na2CO3/NaHCO3 is the definitive functional group test distinguishing carboxylic acids from phenols (phenols are too weakly acidic to react with carbonates).",
            "Reaction with PCl5: occurs vigorously at room temperature with evolution of misty fumes of HCl (turns damp blue litmus red)."
        ],
        "resources": "Usman Pack 15C Q1–Q50 & FAQs (Carboxylic Acids and Reactions)"
    },
    78: {
        "topic_code": "Topic 15 — Organic Chemistry (15D.1 & 15D.2)",
        "subtopic": "Acyl Chlorides & Esters: Nucleophilic Addition-Elimination & Saponification",
        "learning_objective": "Formulate reactions of acyl chlorides, compare with carboxylic acids, and contrast acid vs alkaline ester hydrolysis.",
        "what_to_learn": [
            "(1) Acyl chlorides (R-COCl): highly reactive carboxylic acid derivatives; carbonyl carbon is bonded to two strongly electronegative atoms (O and Cl), making it intensely electron-deficient (very delta-positive).",
            "(2) Reactions of acyl chlorides (nucleophilic addition-elimination, vigorous at room temp, steamy HCl fumes): (a) + H2O → carboxylic acid + HCl; (b) + alcohol → ester + HCl; (c) + NH3 → primary amide + NH4Cl; (d) + primary amine → secondary N-substituted amide + RNH3Cl.",
            "(3) Advantage over carboxylic acids: acyl chloride reactions go to COMPLETION (irreversible), require NO catalyst, and occur rapidly at room temperature.",
            "(4) Ester naming and structure: named from alcohol alkyl group first, then carboxylate (e.g. ethyl ethanoate CH3COOCH2CH3).",
            "(5) Acid hydrolysis of esters: heated with dilute acid catalyst (HCl/H2SO4); REVERSIBLE EQUILIBRIUM: RCOOR' + H2O ⇌ RCOOH + R'OH; low yield.",
            "(6) Alkaline hydrolysis (saponification): heated under reflux with aqueous NaOH; IRREVERSIBLE (goes to completion): RCOOR' + OH⁻ → RCOO⁻ + R'OH; forms carboxylate salt."
        ],
        "how_to_outstand": [
            "Explain WHY acyl chlorides are far more reactive than chloroalkanes: carbonyl carbon is attacked by nucleophiles via addition-elimination, and Cl⁻ is an excellent leaving group.",
            "Compare acid vs alkaline hydrolysis: alkaline hydrolysis goes to COMPLETION because the carboxylate ion RCOO⁻ is formed, which cannot be attacked by alcohol.",
            "To regenerate free carboxylic acid from alkaline hydrolysis: acidify the reaction mixture with strong acid (e.g. dilute HCl): RCOO⁻ + H⁺ → RCOOH."
        ],
        "resources": "Usman Pack 15D Q1–Q35 (Acyl Chlorides and Ester Hydrolysis)"
    },
    79: {
        "topic_code": "Topic 15 — Organic Chemistry (15D.3 & 15E.1–15E.4)",
        "subtopic": "Polyesters, Chromatography (TLC, GC, HPLC) & GC-MS",
        "learning_objective": "Draw polyester repeat units, explain condensation polymerisation, and interpret chromatography and GC-MS data.",
        "what_to_learn": [
            "(1) Condensation polymerisation: monomers link together with the elimination of a small molecule (usually H2O or HCl).",
            "(2) Polyesters from dicarboxylic acid + diol: e.g. benzene-1,4-dicarboxylic acid + ethane-1,2-diol → PET (Terylene).",
            "(3) Drawing repeat unit: open brackets with extending bonds passing through brackets: -[-CO-C6H4-CO-O-CH2CH2-O-]n-.",
            "(4) Biodegradability: polyesters can be hydrolysed by acid or alkali (ester link can be broken), making them biodegradable, unlike non-biodegradable polyalkenes.",
            "(5) Thin Layer Chromatography (TLC): silica stationary phase, organic solvent mobile phase; Rf = distance moved by spot / distance moved by solvent.",
            "(6) Gas Chromatography (GC) and HPLC: retention time (tR) identifies components; area under each peak is proportional to relative quantity.",
            "(7) GC-MS (Gas Chromatography - Mass Spectrometry): GC separates mixture components; each separated component enters MS to produce a fragmentation spectrum matched against a computer library."
        ],
        "how_to_outstand": [
            "In polyester repeat units, ensure the extending open bonds pass completely through the brackets on both ends.",
            "Explain TLC Rf differences: polar stationary phase (silica) binds polar compounds strongly by dipole-dipole/H-bonding → lower Rf; non-polar compounds move further → higher Rf.",
            "GC-MS advantages: combines the high separation efficiency of GC with the sensitive, unambiguous structural identification of mass spectrometry."
        ],
        "resources": "Usman Pack 15D Q36–Q50 & 15E1–15E4 (Polyesters and Chromatography)"
    },
    80: {
        "topic_code": "Topic 15 — Organic Chemistry (15E.5–15E.8)",
        "subtopic": "NMR Spectroscopy: ¹³C NMR, ¹H NMR Shifts & Splitting Patterns",
        "learning_objective": "Deduce organic structures using ¹³C and high-resolution ¹H NMR spectroscopy, integration traces, and the n+1 splitting rule.",
        "what_to_learn": [
            "(1) NMR principles: nuclei with odd atomic/mass numbers (¹H, ¹³C) possess nuclear spin; placed in magnetic field and irradiated with radio frequencies.",
            "(2) Tetramethylsilane (TMS, (CH3)4Si): internal reference standard; inert, non-toxic, volatile (easily removed), gives a single sharp singlet at δ = 0 ppm.",
            "(3) ¹³C NMR spectroscopy: number of peaks = number of unique chemical environments of carbon atoms; chemical shift indicates functional group.",
            "(4) ¹H NMR chemical shifts (δ in ppm): TMS (0); alkyl C-H (0.9–1.8); -O-CH3 (3.3–4.0); Ar-H (6.5–8.5); -CHO (9.0–10.0); -COOH (10.0–12.0).",
            "(5) Integration trace (peak area): height/area of peak is directly proportional to the number of equivalent protons in that environment.",
            "(6) Spin-spin coupling (n+1 rule): non-equivalent protons on adjacent carbon atoms cause peak splitting: n adjacent protons split peak into n+1 sub-peaks (0 H → singlet; 1 H → doublet (1:1); 2 H → triplet (1:2:1); 3 H → quartet (1:3:3:1)).",
            "(7) D2O shake: labile OH (alcohols, acids) and NH protons undergo deuterium exchange (R-OH + D2O ⇌ R-OD + HOD); the OH/NH peak DISAPPEARS from the ¹H NMR spectrum, confirming its presence."
        ],
        "how_to_outstand": [
            "Equivalent protons DO NOT split each other! Splitting is caused ONLY by non-equivalent protons on ADJACENT carbons.",
            "OH and NH protons generally appear as broad singlets and do NOT cause splitting of adjacent CH protons due to rapid chemical exchange.",
            "D2O exchange is the definitive spectroscopic test: 'The peak at δ ~4.5 ppm disappears upon addition of D2O, confirming an OH or NH group.'",
            "Combined spectral analysis strategy: (1) Find Mr from mass spec M⁺ peak; (2) Count carbons from ¹³C NMR; (3) Identify functional groups from chemical shifts; (4) Determine carbon connectivity from ¹H NMR splitting."
        ],
        "resources": "Usman Pack 15E5–15E8 Q1–Q50 & FAQs (Complete NMR Mastery)"
    }
}

def _get_teaching_content(day_num, date_str):
    content = TEACHING_DAYS.get(day_num)
    if not content:
        content = {
            "topic_code": "Unit 4 Core Syllabus",
            "subtopic": "Advanced Topic Mastery",
            "learning_objective": "Consolidate Unit 4 learning points and complete past paper question sets.",
            "what_to_learn": [
                "(1) Review core syllabus definitions and equations.",
                "(2) Practice calculation methodologies from past papers.",
                "(3) Verify chemical reaction mechanisms.",
                "(4) Complete assigned topical questions."
            ],
            "how_to_outstand": ["Focus on keyword precision and method marks."],
            "resources": "Mentora Topical Question Packs"
        }
    return {
        "day": day_num,
        "date_str": date_str,
        "day_type": "TEACHING",
        "topic_code": content["topic_code"],
        "subtopic": content["subtopic"],
        "learning_objective": content["learning_objective"],
        "what_to_learn": content["what_to_learn"],
        "how_to_outstand": content["how_to_outstand"],
        "resources": content["resources"],
        "self_assessment": [
            "Mastered all learning objectives and chemical equations",
            "Attempted all assigned practice questions from the topical pack",
            "Audited answers against mark scheme and understood all examiner points"
        ]
    }

def _get_phase2_content(day_num, date_str, day_name):
    phase2_map = {
        82: {
            "title": "GRAND REVISION DAY 1: Full Unit 4 Synoptic Mapping",
            "obj": "Construct comprehensive synoptic concept maps connecting Topic 11 Kinetics, Topic 12 Energetics, Topic 13 Equilibria, Topic 14 Acids, and Topic 15 Organic.",
            "learn": [
                "(1) Thermodynamics & Kinetics Grand Map: Link ΔH, ΔS_sys, ΔS_surr, ΔS_total, K, and rate constant k.",
                "(2) Organic Reaction Pathway Synthesis: Draw complete interconversion flowchart from alcohols, aldehydes, ketones, carboxylic acids, acyl chlorides, esters, and polyesters.",
                "(3) Multi-Spectra Quick Reference: Review characteristic IR absorptions, Mass Spec common fragments (m/z 15, 29, 43, 45, 57, 77), and ¹H/¹³C NMR shift regions.",
                "(4) Formula and Units Audit: Write out all 12 key mathematical formulas and their exact SI units from memory."
            ],
            "outstand": ["A* students see Unit 4 as an interconnected web rather than isolated chapters."],
            "res": "Mentora Full Unit 4 Synoptic Summary Maps"
        },
        83: {
            "title": "OFFICIAL PAST PAPER MOCK 1: WCH14/01 January 2021",
            "obj": "Complete full official Pearson Edexcel IAL Unit 4 exam paper under strict 90-minute timed conditions.",
            "learn": [
                "(1) Full 90-mark exam simulation in silence (9:00 AM - 10:30 AM).",
                "(2) Section A (MCQs 1–20): complete in 20 minutes; use process of elimination.",
                "(3) Section B & C (Structured & Data questions): allocate 1 min per mark; show all intermediate calculations.",
                "(4) Immediate line-by-line mark scheme self-assessment and scoring."
            ],
            "outstand": ["Target: >= 78/90 (Historical A* boundary is typically ~68-72/90; target 80+ for safety)."],
            "res": "Official Past Paper WCH14/01 Jan 2021 & Mark Scheme"
        },
        84: {
            "title": "DEEP ERROR AUDIT 1: Mock 1 Diagnostic & Calculation Surgery",
            "obj": "Perform line-by-line post-mortem on Mock 1, identifying every misconception and drilling calculation weaknesses.",
            "learn": [
                "(1) Enter every lost mark into the A* Error Registry with root-cause categorization.",
                "(2) Redo all missed calculations from scratch without viewing mark scheme.",
                "(3) Targeted drill on rate equation data tables and ICE equilibrium calculations.",
                "(4) Review Examiner Report for Jan 2021 noting worldwide student pitfalls."
            ],
            "outstand": ["Never accept a vague mark loss — understand the exact examiner reason for deduction."],
            "res": "WCH14/01 Jan 2021 Examiner Report & Remedial Worksheets"
        },
        85: {
            "title": "OFFICIAL PAST PAPER MOCK 2: WCH14/01 June 2021",
            "obj": "Complete full official Pearson Edexcel IAL Unit 4 exam paper under timed conditions.",
            "learn": [
                "(1) Full 90-mark timed exam simulation (90 mins).",
                "(2) Focus on clear layout of Born-Haber cycle and Hess's Law steps.",
                "(3) Precise curly arrow drawing in organic mechanisms.",
                "(4) Mark scheme scoring and score logging."
            ],
            "outstand": ["Target: >= 80/90."],
            "res": "Official Past Paper WCH14/01 Jun 2021 & Mark Scheme"
        },
        86: {
            "title": "DEEP ERROR AUDIT 2: Mock 2 Diagnostic & Buffer Calculation Drills",
            "obj": "Eliminate errors identified in Mock 2, focusing on buffer solutions and pH curve interpretations.",
            "learn": [
                "(1) Log Mock 2 errors into registry.",
                "(2) Intensive drills on Henderson-Hasselbalch buffer calculations upon adding small acid/alkali.",
                "(3) Half-equivalence point derivations and indicator range justifications.",
                "(4) Study WCH14/01 Jun 2021 Examiner Report."
            ],
            "outstand": ["Ensure buffer component mole ratios are calculated before volume division."],
            "res": "WCH14/01 Jun 2021 Examiner Report & Buffer Drill Pack"
        },
        87: {
            "title": "OFFICIAL PAST PAPER MOCK 3: WCH14/01 October 2021",
            "obj": "Execute timed past paper mock under full exam conditions.",
            "learn": [
                "(1) Full 90-mark timed simulation (90 mins).",
                "(2) Pacing check: ensure at least 10 minutes remain for final proofreading.",
                "(3) Check significant figures on all numerical answers.",
                "(4) Comprehensive mark scheme evaluation."
            ],
            "outstand": ["Target: >= 80/90."],
            "res": "Official Past Paper WCH14/01 Oct 2021 & Mark Scheme"
        },
        88: {
            "title": "OFFICIAL PAST PAPER MOCK 4: WCH14/01 January 2022",
            "obj": "Execute timed past paper mock under strict exam conditions.",
            "learn": [
                "(1) Full 90-mark timed exam simulation.",
                "(2) High-precision Arrhenius plot gradient construction.",
                "(3) Detailed explanations of Fajans' rules and polarisation.",
                "(4) Scoring and logging against historical grade boundaries."
            ],
            "outstand": ["Target: >= 82/90."],
            "res": "Official Past Paper WCH14/01 Jan 2022 & Mark Scheme"
        },
        89: {
            "title": "DEEP ERROR AUDIT 3: Organic Mechanisms & Spectroscopy Surgery",
            "obj": "Audit organic and spectroscopic questions across Mocks 1–4, perfecting identification skills.",
            "learn": [
                "(1) Review all organic synthesis pathways and reagents (PCl5, NaBH4, Tollens', KCN, 2,4-DNPH).",
                "(2) Practice 5 complete unknown structural elucidation problems combining IR, MS, and NMR.",
                "(3) Review D2O shake mechanism and splitting pattern assignments.",
                "(4) Update organic flashcard deck."
            ],
            "outstand": ["Always show how each piece of spectral data supports specific structural fragments."],
            "res": "Mentora Organic Elucidation Masterclass Worksheets"
        },
        90: {
            "title": "OFFICIAL PAST PAPER MOCK 5: WCH14/01 June 2022",
            "obj": "Execute timed past paper mock under strict exam conditions.",
            "learn": [
                "(1) Full 90-mark timed exam simulation.",
                "(2) Multi-step kinetics mechanisms and pre-equilibrium derivations.",
                "(3) Accurate state symbols on all thermodynamic cycle equations.",
                "(4) Comprehensive scoring."
            ],
            "outstand": ["Target: >= 82/90."],
            "res": "Official Past Paper WCH14/01 Jun 2022 & Mark Scheme"
        },
        91: {
            "title": "DEEP ERROR AUDIT 4: Thermodynamics & Entropy Precision Drills",
            "obj": "Remediate any thermodynamic weaknesses from Mock 5.",
            "learn": [
                "(1) Review ΔS_total = R ln K derivations and unit conversions.",
                "(2) Drill crossover temperature problems and feasibility justifications.",
                "(3) Compare theoretical vs experimental lattice energies for transition metal halides.",
                "(4) Study WCH14/01 Jun 2022 Examiner Report."
            ],
            "outstand": ["Always verify units: ΔS in J K⁻¹ mol⁻¹, ΔH in kJ mol⁻¹."],
            "res": "WCH14/01 Jun 2022 Examiner Report & Thermodynamics Drills"
        },
        92: {
            "title": "OFFICIAL PAST PAPER MOCK 6: WCH14/01 October 2022",
            "obj": "Execute timed past paper mock under strict exam conditions.",
            "learn": [
                "(1) Full 90-mark timed simulation.",
                "(2) Test speed on Section A MCQs (aim for 15-18 mins).",
                "(3) Structured explanations for Group 2 sulfate/hydroxide solubility trends.",
                "(4) Scoring and error logging."
            ],
            "outstand": ["Target: >= 84/90."],
            "res": "Official Past Paper WCH14/01 Oct 2022 & Mark Scheme"
        },
        93: {
            "title": "DEEP ERROR AUDIT 5: Kinetics Graphs & Experimental Techniques",
            "obj": "Review experimental kinetics methods and graph tangent skills.",
            "learn": [
                "(1) Colorimetry filter choice and Beer-Lambert linearity reviews.",
                "(2) Gas collection error sources and quenching procedure validations.",
                "(3) Clock reaction 1/t proportionality proofs.",
                "(4) Study WCH14/01 Oct 2022 Examiner Report."
            ],
            "outstand": ["In experimental design questions, specify apparatus, quantities, and variables to control."],
            "res": "WCH14/01 Oct 2022 Examiner Report & Experimental Kinetics Guide"
        },
        94: {
            "title": "OFFICIAL PAST PAPER MOCK 7: WCH14/01 January 2023",
            "obj": "Execute timed past paper mock under strict exam conditions.",
            "learn": [
                "(1) Full 90-mark timed simulation.",
                "(2) High-speed ICE table calculations for Kp with non-cancelling volumes.",
                "(3) Acyl chloride vs ester reactivity comparisons.",
                "(4) Scoring and performance review."
            ],
            "outstand": ["Target: >= 84/90."],
            "res": "Official Past Paper WCH14/01 Jan 2023 & Mark Scheme"
        },
        95: {
            "title": "OFFICIAL PAST PAPER MOCK 8: WCH14/01 June 2023",
            "obj": "Execute timed past paper mock under strict exam conditions.",
            "learn": [
                "(1) Full 90-mark timed simulation.",
                "(2) Titration curve half-equivalence point analysis.",
                "(3) Complete polyester repeat unit drawing.",
                "(4) Scoring and error logging."
            ],
            "outstand": ["Target: >= 85/90."],
            "res": "Official Past Paper WCH14/01 Jun 2023 & Mark Scheme"
        },
        96: {
            "title": "DEEP ERROR AUDIT 6: Section A MCQ Perfection & Error Registry Scrub",
            "obj": "Analyze all 160 MCQs across Mocks 1–8 to ensure 20/20 in Section A.",
            "learn": [
                "(1) Review every MCQ missed across past papers; identify recurring distractor traps.",
                "(2) Fast-track MCQ elimination strategies (discard 2 obvious incorrects in 10s).",
                "(3) Final review of Error Registry: verify all historical errors have been permanently resolved.",
                "(4) Light evening review of formula sheet."
            ],
            "outstand": ["Scoring 20/20 on Section A provides an unbeatable psychological advantage."],
            "res": "Mentora Unit 4 MCQ Master Vault (200 Questions)"
        },
        97: {
            "title": "OFFICIAL PAST PAPER MOCK 9: WCH14/01 October 2023",
            "obj": "Execute penultimate timed past paper mock.",
            "learn": [
                "(1) Full 90-mark timed simulation under exact exam room timing.",
                "(2) Execute refined exam strategy: calm pacing, neat handwriting, explicit units.",
                "(3) Score against mark scheme and celebrate high consistency.",
                "(4) Final review of Oct 2023 Examiner Report."
            ],
            "outstand": ["Target: >= 85/90."],
            "res": "Official Past Paper WCH14/01 Oct 2023 & Mark Scheme"
        },
        98: {
            "title": "FINAL PREDICTOR MOCK 10: WCH14/01 2024 Series",
            "obj": "Execute final grand predictor mock exam under identical exam hall conditions.",
            "learn": [
                "(1) Sit the most recent Pearson Edexcel paper (Jan/Jun 2024) in strict timed conditions.",
                "(2) Complete paper with maximum focus and confidence.",
                "(3) Final score check: confirm A* readiness (>= 85/90 raw score).",
                "(4) Mark paper, celebrate mastery, and put past papers away."
            ],
            "outstand": ["You are fully prepared. You have solved over 600 authentic past paper questions."],
            "res": "Official Past Paper WCH14/01 2024 Series & Mark Scheme"
        },
        99: {
            "title": "ULTIMATE EXAMINER REPORT AUDIT: Top 50 Examiner Traps",
            "obj": "Review the Mentora 50 Empirical Examiner Traps & Model Answers document.",
            "learn": [
                "(1) Read through all 50 Examiner Traps across Topics 11, 12, 13, 14, and 15.",
                "(2) Reinforce precise examiner keywords for definitions, mechanisms, and equilibrium proofs.",
                "(3) Review data booklet values and periodic table layout.",
                "(4) Check all required mathematical formulas one last time."
            ],
            "outstand": ["Examiners look for specific indicative keywords — ensure they flow naturally onto the paper."],
            "res": "Mentora Unit 4 Top 50 Examiner Traps Document"
        },
        100: {
            "title": "PRE-EXAM READINESS & MENTAL CONDITIONING",
            "obj": "Complete final stationery and logistics check, relax, and achieve peak cognitive readiness.",
            "learn": [
                "(1) Pack pencil case: transparent case, 3 black ballpoint pens, 2 HB pencils, eraser, ruler, calculator.",
                "(2) Reset and verify calculator settings (ensure DEG mode or clean reset, new batteries).",
                "(3) Review 1-page summary formula sheet for 30 minutes in the morning.",
                "(4) NO intense cramming in the afternoon; engage in light exercise, hydrate, and eat nutritious meals.",
                "(5) Early bedtime (by 10:00 PM) to ensure 8 hours of restorative sleep."
            ],
            "outstand": ["Confidence is the product of meticulous preparation. Trust your months of disciplined study."],
            "res": "Mentora Pre-Exam Checklist & Formula Summary Card"
        },
        101: {
            "title": "EXAM DAY: PEARSON EDEXCEL IAL CHEMISTRY UNIT 4 (WCH14/01)",
            "obj": "Execute your exam plan with supreme calm, clarity, and precision to secure Grade A* (100% UMS)!",
            "learn": [
                "(1) Healthy breakfast 2 hours before exam; arrive at exam centre 45 minutes early.",
                "(2) First 2 minutes: read instructions, check all pages present, breathe deeply.",
                "(3) Section A (MCQs): work steadily, mark tricky questions for review, finish in 20 mins.",
                "(4) Sections B & C: read questions carefully, underline key command words, show full working.",
                "(5) Final 10 minutes: check units on every calculation, verify significant figures, re-read 6-mark answers.",
                "(6) Submit paper knowing you delivered your absolute best work!"
            ],
            "outstand": ["MENTORA ACADEMY PROUDLY BACKS USMAN — GO AND ACHIEVE YOUR A*!"],
            "res": "Official Pearson Edexcel Examination Paper WCH14/01"
        }
    }
    
    info = phase2_map.get(day_num, {
        "title": "Intensive Past Paper Revision",
        "obj": "Execute past paper practice.",
        "learn": ["Timed past paper practice.", "Mark scheme review."],
        "outstand": ["Focus on accuracy."],
        "res": "Past Papers"
    })
    
    day_type = "EXAM_DAY" if day_num == 101 else ("FINAL_PREPARATION" if day_num == 100 else "MOCK_EXAM")
    
    return {
        "day": day_num,
        "date_str": date_str,
        "day_type": day_type,
        "topic_code": "Phase 2 — Final 20-Day Mock Marathon",
        "subtopic": info["title"],
        "learning_objective": info["obj"],
        "what_to_learn": info["learn"],
        "how_to_outstand": info["outstand"],
        "resources": info["res"],
        "self_assessment": [
            "Completed planned activity within target timeframe",
            "Audited performance and addressed any remaining questions",
            "Maintained positive mindset and exam readiness"
        ]
    }
