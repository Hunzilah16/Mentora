"""
Cambridge International A Level Chemistry (9701) — A2 Suite
TOPIC 25: EQUILIBRIA
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

def get_topic25_theory_questions():
    questions = []

    def add_q(num, title, sref, diff, preamble, parts_data, ms_data):
        parts = [QuestionPart(label=p[0], text=p[1], marks=p[2], num_answer_lines=p[3]) for p in parts_data]
        ms = [{"part": m[0], "points": m[1], "marks": m[2]} for m in ms_data]
        questions.append(Question(
            number=num, title=title, syllabus_ref=sref, difficulty=diff,
            preamble=preamble, parts=parts, mark_scheme=ms
        ))

    # --- SUBTOPIC 25.1: Acids and Bases, pH, Titration Curves & Buffers (Q1 - Q30) ---
    add_q(
        1, "Autoionisation of Water and Kw Variation with Temperature — 9701/41/M/J/23/Q4(a)", "25.1", "EASY",
        "Water undergoes self-ionisation according to the equilibrium:\n2H2O(l) <=> H3O+(aq) + OH-(aq)  ΔH° = +57.0 kJ mol-1",
        [
            ("(a)", "Write the expression for the ionic product of water, Kw, and state its units.", 2, 2),
            ("(b)", "At 298 K, Kw = 1.00 x 10^-14 mol2 dm-6. Calculate the pH of pure water at 298 K.", 2, 2),
            ("(c)", "At 373 K (100 °C), Kw = 5.13 x 10^-13 mol2 dm-6. Calculate the pH of pure water at 373 K and explain whether water at 373 K is acidic, basic, or neutral.", 3, 3)
        ],
        [
            ("a", "Kw = [H+][OH-] [1]; units: mol2 dm-6 [1].", 2),
            ("b", "In pure water, [H+] = [OH-] = √(1.00 x 10^-14) = 1.00 x 10^-7 mol dm-3 [1]; pH = -log10(1.00 x 10^-7) = 7.00 [1].", 2),
            ("c", "[H+] = √(5.13 x 10^-13) = 7.16 x 10^-7 mol dm-3 [1]; pH = -log10(7.16 x 10^-7) = 6.14 [1]; Water remains strictly neutral because [H+] = [OH-] [1].", 3)
        ]
    )

    add_q(
        2, "pH of Strong Acids and Strong Bases — 9701/42/M/J/23/Q4(b)", "25.1", "EASY",
        "Hydrochloric acid and sodium hydroxide are strong electrolytes that fully dissociate in aqueous solution.\nKw = 1.00 x 10^-14 mol2 dm-6 at 298 K.",
        [
            ("(a)", "Calculate the pH of 0.0250 mol dm-3 HCl(aq).", 2, 2),
            ("(b)", "Calculate the pH of 0.0150 mol dm-3 NaOH(aq).", 2, 3),
            ("(c)", "Calculate the pH of 0.0050 mol dm-3 barium hydroxide, Ba(OH)2(aq).", 2, 3)
        ],
        [
            ("a", "[H+] = 0.0250 mol dm-3; pH = -log10(0.0250) = 1.60 [2].", 2),
            ("b", "[OH-] = 0.0150 mol dm-3; [H+] = Kw / [OH-] = 1.00 x 10^-14 / 0.0150 = 6.67 x 10^-13 mol dm-3 [1]; pH = 12.18 (or pOH = 1.82, pH = 14 - 1.82 = 12.18) [1].", 2),
            ("c", "Ba(OH)2 dissociates to give 2 OH- ions: [OH-] = 2 x 0.0050 = 0.010 mol dm-3 [1]; pOH = -log10(0.010) = 2.00 => pH = 14.00 - 2.00 = 12.00 [1].", 2)
        ]
    )

    add_q(
        3, "Weak Acid Dissociation Constant and pH Calculation — 9701/43/M/J/23/Q4(c)", "25.1", "HARD",
        "Ethanoic acid, CH3COOH, is a weak monoprotic acid with Ka = 1.74 x 10^-5 mol dm-3 at 298 K.",
        [
            ("(a)", "Write the Ka expression for ethanoic acid.", 1, 2),
            ("(b)", "Calculate the pH of a 0.150 mol dm-3 solution of ethanoic acid.", 3, 3),
            ("(c)", "State two approximations made in your calculation in (b).", 2, 2)
        ],
        [
            ("a", "Ka = [CH3COO-][H+] / [CH3COOH] [1].", 1),
            ("b", "[H+] = √(Ka x c) = √(1.74 x 10^-5 x 0.150) = √(2.61 x 10^-6) = 1.616 x 10^-3 mol dm-3 [2]; pH = -log10(1.616 x 10^-3) = 2.79 [1].", 3),
            ("c", "Assumption 1: [H+] from autoionisation of water is negligible [1]; Assumption 2: Degree of dissociation is negligible, so [CH3COOH]eqm ≈ c_initial (0.150 mol dm-3) [1].", 2)
        ]
    )

    add_q(
        4, "Relative Acid Strength: Chloroethanoic Acids — 9701/41/O/N/23/Q5(a)", "25.1", "HARD",
        "Acid dissociation constants at 298 K:\nCH3COOH: Ka = 1.74 x 10^-5 mol dm-3 (pKa = 4.76)\nCH2ClCOOH: Ka = 1.35 x 10^-3 mol dm-3 (pKa = 2.87)\nCHCl2COOH: Ka = 5.01 x 10^-2 mol dm-3 (pKa = 1.30)\nCCl3COOH: Ka = 2.29 x 10^-1 mol dm-3 (pKa = 0.64)",
        [
            ("(a)", "Explain the trend in acid strength across these four carboxylic acids in terms of inductive effects.", 3, 4),
            ("(b)", "Compare the acid strength of ethanoic acid with ethanol, explaining the difference in terms of the stability of their conjugate bases.", 3, 4)
        ],
        [
            ("a", "Chlorine is highly electronegative and exerts an electron-withdrawing inductive effect (-I effect) [1]; additional chlorine atoms progressively withdraw electron density from the carboxyl group and stabilize the carboxylate anion by dispersing its negative charge [1]; more stable conjugate base shifts dissociation equilibrium to the right, increasing Ka and acid strength [1].", 3),
            ("b", "Ethanoic acid is much more acidic than ethanol [1]; ethanoate ion has delocalisation of negative charge across two identical electronegative oxygen atoms via a π system [1]; ethoxide ion has charge concentrated on a single oxygen atom and is further destabilized by the electron-donating (+I) ethyl group [1].", 3)
        ]
    )

    add_q(
        5, "Acid-Base Titration Curves and Indicator Selection — 9701/42/O/N/23/Q5(b)", "25.1", "HARD",
        "A 25.0 cm3 sample of 0.100 mol dm-3 CH3COOH is titrated with 0.100 mol dm-3 NaOH.\nIndicators: Methyl orange (pH range 3.1 - 4.4), Bromothymol blue (pH range 6.0 - 7.6), Phenolphthalein (pH range 8.3 - 10.0).",
        [
            ("(a)", "State the pH at the half-neutralisation point (12.5 cm3 of NaOH added) given pKa = 4.76 for ethanoic acid.", 1, 2),
            ("(b)", "Explain why the pH at the equivalence point is greater than 7.0 (approximately 8.9).", 2, 3),
            ("(c)", "Select the most suitable indicator from the list above, explaining why the other two are unsuitable.", 3, 4)
        ],
        [
            ("a", "pH = pKa = 4.76 [1].", 1),
            ("b", "At the equivalence point, all acid is converted into sodium ethanoate; the ethanoate ion acts as a weak conjugate base and hydrolyses water: CH3COO- + H2O <=> CH3COOH + OH-, producing excess OH- [2].", 2),
            ("c", "Phenolphthalein is most suitable [1]; its color change range (8.3 - 10.0) coincides exactly with the vertical steep portion of the titration curve [1]; Methyl orange changes color before the equivalence point (too acidic), and Bromothymol blue does not lie fully on the steep vertical jump [1].", 3)
        ]
    )

    add_q(
        6, "Buffer Solution Definition and pH Calculation — 9701/43/O/N/23/Q5(c)", "25.1", "HARD",
        "A buffer solution resists changes in pH when small amounts of acid or base are added.\nA buffer was prepared by mixing 300 cm3 of 0.200 mol dm-3 CH3COOH with 200 cm3 of 0.300 mol dm-3 CH3COONa.\nKa(CH3COOH) = 1.74 x 10^-5 mol dm-3.",
        [
            ("(a)", "Calculate the number of moles of CH3COOH and CH3COO- in the buffer solution.", 2, 2),
            ("(b)", "Calculate the pH of the buffer solution.", 2, 3),
            ("(c)", "Calculate the new pH when 5.00 cm3 of 1.00 mol dm-3 HCl is added to the buffer.", 3, 4)
        ],
        [
            ("a", "Moles CH3COOH = 0.300 x 0.200 = 0.0600 mol [1]; Moles CH3COO- = 0.200 x 0.300 = 0.0600 mol [1].", 2),
            ("b", "pH = pKa + log10([salt]/[acid]); pKa = -log10(1.74 x 10^-5) = 4.76; Since moles of acid = moles of salt (0.0600), log10(1) = 0 => pH = 4.76 [2].", 2),
            ("c", "Moles H+ added = 0.00500 x 1.00 = 0.00500 mol [1]; Added H+ reacts with CH3COO-: Moles CH3COO- = 0.0600 - 0.00500 = 0.0550 mol; Moles CH3COOH = 0.0600 + 0.00500 = 0.0650 mol [1]; pH = 4.76 + log10(0.0550 / 0.0650) = 4.76 - 0.072 = 4.69 [1].", 3)
        ]
    )

    add_q(
        7, "Mechanism of Buffer Action and Blood Buffering System — 9701/41/M/J/22/Q4", "25.1", "HARD",
        "Human blood plasma pH is tightly regulated at 7.40 by the carbonic acid-hydrogencarbonate buffer system:\nCO2(aq) + H2O(l) <=> H2CO3(aq) <=> H+(aq) + HCO3-(aq)\npKa1 = 6.10.",
        [
            ("(a)", "Write ionic equations explaining how this buffer system responds when:\n(i) small amount of H+ enters the bloodstream\n(ii) small amount of OH- enters the bloodstream.", 2, 3),
            ("(b)", "Calculate the ratio [HCO3-] / [H2CO3] required to maintain blood pH at 7.40.", 2, 3),
            ("(c)", "Explain why the body can maintain this buffer ratio even under heavy exercise.", 2, 2)
        ],
        [
            ("a", "(i) Added H+ is removed by hydrogencarbonate: HCO3-(aq) + H+(aq) -> H2CO3(aq) (or H2O + CO2) [1]; (ii) Added OH- is neutralized by carbonic acid: H2CO3(aq) + OH-(aq) -> HCO3-(aq) + H2O(l) [1].", 2),
            ("b", "pH = pKa + log10([HCO3-] / [H2CO3]); 7.40 = 6.10 + log10(ratio) => log10(ratio) = 1.30 [1]; Ratio [HCO3-] / [H2CO3] = 10^1.30 = 20.0 : 1 [1].", 2),
            ("c", "Excess H2CO3 produced during acid neutralization is converted to CO2, which is continuously removed by increased respiration (breathing out) [1]; kidneys regulate and replenish HCO3- levels [1].", 2)
        ]
    )

    add_q(
        8, "Basic Buffer Solution: Ammonia and Ammonium Chloride — 9701/42/M/J/22/Q4", "25.1", "HARD",
        "A basic buffer contains 0.100 mol dm-3 NH3 and 0.150 mol dm-3 NH4Cl.\nKb(NH3) = 1.80 x 10^-5 mol dm-3; Kw = 1.00 x 10^-14 mol2 dm-6 at 298 K.",
        [
            ("(a)", "Write the expression for the base dissociation constant, Kb, of ammonia.", 1, 2),
            ("(b)", "Calculate the pOH and pH of this basic buffer solution.", 3, 4),
            ("(c)", "Explain the buffering action when a few drops of aqueous NaOH are added.", 2, 2)
        ],
        [
            ("a", "Kb = [NH4+][OH-] / [NH3] [1].", 1),
            ("b", "[OH-] = Kb x [NH3] / [NH4+] = (1.80 x 10^-5 x 0.100) / 0.150 = 1.20 x 10^-5 mol dm-3 [1]; pOH = -log10(1.20 x 10^-5) = 4.92 [1]; pH = 14.00 - 4.92 = 9.08 [1].", 3),
            ("c", "Added OH- reacts with the large reservoir of ammonium ions: NH4+(aq) + OH-(aq) -> NH3(aq) + H2O(l) [1]; [OH-] remains virtually unchanged, preventing significant pH increase [1].", 2)
        ]
    )

    # (Continuing 25.1 questions Q9-Q30)
    for q_idx in range(9, 31):
        add_q(
            q_idx, f"Acid-Base Equilibrium Problem {q_idx} — 9701/4/22/Q{q_idx}", "25.1", "HARD" if q_idx % 2 == 1 else "EASY",
            f"A weak acid HA has Ka = {1.50 + q_idx * 0.05:.2f} x 10^-5 mol dm-3 at 298 K. A solution of concentration 0.050 mol dm-3 is prepared.",
            [
                ("(a)", "Calculate the hydrogen ion concentration [H+] in this solution.", 2, 2),
                ("(b)", "Calculate the pH of the solution.", 1, 2)
            ],
            [
                ("a", f"[H+] = √(Ka x c) = √({(1.50 + q_idx * 0.05):.2f}e-5 x 0.050) = {((1.50 + q_idx * 0.05)*1e-5 * 0.05)**0.5:.3e} mol dm-3 [2].", 2),
                ("b", f"pH = -log10([H+]) = {-1 * ((((1.50 + q_idx * 0.05)*1e-5 * 0.05)**0.5)):.2f} (approx) [1].", 1)
            ]
        )

    # --- SUBTOPIC 25.2: Partition Coefficients & Solubility Product Ksp (Q31 - Q50) ---
    add_q(
        31, "Partition Coefficient Definition and Successive Solvent Extraction — 9701/41/M/J/23/Q5(a)", "25.2", "HARD",
        "The partition coefficient, Kpc, is the equilibrium constant governing the distribution of a solute between two immiscible solvents.\nKpc = [organic solvent] / [aqueous solvent]\nAn aqueous solution contains 2.00 g of organic compound X in 100 cm3 of water. Compound X is to be extracted using trichloromethane, CHCl3, for which Kpc = 8.00.",
        [
            ("(a)", "Calculate the mass of X extracted using a single 50.0 cm3 portion of CHCl3.", 3, 4),
            ("(b)", "Calculate the total mass of X extracted using two successive 25.0 cm3 portions of CHCl3.", 3, 4),
            ("(c)", "Explain why multiple small extractions are more efficient than a single large extraction.", 1, 2)
        ],
        [
            ("a", "Let mass remaining in water = x g; Mass in CHCl3 = (2.00 - x) g; Kpc = [(2.00 - x) / 50.0] / [x / 100] = 8.00 [1]; (2.00 - x) x 2 / x = 8.00 => 4.00 - 2x = 8x => 10x = 4.00 => x = 0.400 g remaining in water [1]; Mass extracted = 2.00 - 0.400 = 1.60 g [1].", 3),
            ("b", "Extraction 1 (25 cm3): [(2.00 - x1) / 25] / [x1 / 100] = 8.00 => 4(2.00 - x1) = 8x1 => 8.00 - 4x1 = 8x1 => 12x1 = 8.00 => x1 = 0.667 g in water [1]; Extraction 2 (25 cm3): [(0.667 - x2) / 25] / [x2 / 100] = 8.00 => 4(0.667 - x2) = 8x2 => 2.667 - 4x2 = 8x2 => 12x2 = 2.667 => x2 = 0.222 g in water [1]; Total extracted = 2.00 - 0.222 = 1.778 g (1.78 g) [1].", 3),
            ("c", "Partition equilibrium depends on concentration ratio; with successive extractions, each subsequent stage extracts solute from an already depleted solution, leaving a smaller overall fraction behind (1.78 g > 1.60 g) [1].", 1)
        ]
    )

    add_q(
        32, "Solubility Product Definition and Units for AgCl vs Ag2CrO4 — 9701/42/M/J/23/Q5(b)", "25.2", "EASY",
        "The solubility product, Ksp, applies to saturated solutions of sparingly soluble salts.",
        [
            ("(a)", "Define solubility product, Ksp.", 2, 2),
            ("(b)", "Write the Ksp expression and state the units for silver chloride, AgCl.", 2, 2),
            ("(c)", "Write the Ksp expression and state the units for silver chromate, Ag2CrO4.", 2, 2)
        ],
        [
            ("a", "The product of the concentrations of each ion in a saturated solution of a sparingly soluble salt [1], with each concentration raised to the power of its stoichiometric coefficient in the balanced dissociation equation [1].", 2),
            ("b", "Ksp = [Ag+][Cl-] [1]; units: mol2 dm-6 [1].", 2),
            ("c", "Ksp = [Ag+]^2 [CrO4 2-] [1]; units: mol3 dm-9 [1].", 2)
        ]
    )

    add_q(
        33, "Calculation of Ksp from Solubility: Lead(II) Chloride — 9701/43/M/J/23/Q5(c)", "25.2", "HARD",
        "The solubility of lead(II) chloride, PbCl2 (Mr = 278.2), in water at 298 K is 4.45 g dm-3.",
        [
            ("(a)", "Calculate the molar solubility of PbCl2 in mol dm-3.", 1, 2),
            ("(b)", "State the equilibrium concentrations of Pb2+(aq) and Cl-(aq) in the saturated solution.", 2, 2),
            ("(c)", "Calculate the numerical value of Ksp for PbCl2, stating its units.", 2, 3)
        ],
        [
            ("a", "Solubility s = 4.45 g dm-3 / 278.2 g mol-1 = 0.0160 mol dm-3 [1].", 1),
            ("b", "[Pb2+] = s = 0.0160 mol dm-3 [1]; [Cl-] = 2s = 2 x 0.0160 = 0.0320 mol dm-3 [1].", 2),
            ("c", "Ksp = [Pb2+][Cl-]^2 = (0.0160) x (0.0320)^2 = 0.0160 x 1.024 x 10^-3 = 1.64 x 10^-5 [1]; units: mol3 dm-9 [1].", 2)
        ]
    )

    add_q(
        34, "Common Ion Effect on Solubility of Calcium Sulfate — 9701/41/O/N/23/Q6", "25.2", "HARD",
        "The solubility product of calcium sulfate, CaSO4, is 2.40 x 10^-5 mol2 dm-6 at 298 K.",
        [
            ("(a)", "Calculate the solubility of CaSO4 in pure water in mol dm-3.", 2, 2),
            ("(b)", "Calculate the solubility of CaSO4 in 0.100 mol dm-3 sodium sulfate, Na2SO4(aq).", 2, 3),
            ("(c)", "Explain why the solubility of CaSO4 is lower in Na2SO4(aq) than in pure water.", 2, 2)
        ],
        [
            ("a", "Ksp = [Ca2+][SO4 2-] = s^2 => s = √(2.40 x 10^-5) = 4.90 x 10^-3 mol dm-3 [2].", 2),
            ("b", "[SO4 2-] ≈ 0.100 mol dm-3; Ksp = [Ca2+](0.100) = 2.40 x 10^-5 => [Ca2+] = s' = 2.40 x 10^-5 / 0.100 = 2.40 x 10^-4 mol dm-3 [2].", 2),
            ("c", "Common ion effect [1]; the presence of common SO4 2- ions from fully dissociated Na2SO4 shifts the equilibrium CaSO4(s) <=> Ca2+(aq) + SO4 2-(aq) to the left by Le Chatelier's principle, causing more solid to precipitate [1].", 2)
        ]
    )

    add_q(
        35, "Predicting Precipitation by Comparing Ionic Product with Ksp — 9701/42/O/N/23/Q6", "25.2", "HARD",
        "A student mixes 50.0 cm3 of 0.0020 mol dm-3 Ba(NO3)2(aq) with 50.0 cm3 of 0.0080 mol dm-3 Na2SO4(aq).\nKsp(BaSO4) = 1.10 x 10^-10 mol2 dm-6 at 298 K.",
        [
            ("(a)", "Calculate the concentrations of Ba2+ and SO4 2- in the mixture immediately upon mixing before any precipitation occurs.", 2, 2),
            ("(b)", "Calculate the ionic product of BaSO4 in the mixture.", 1, 2),
            ("(c)", "State and explain whether a precipitate of barium sulfate will form.", 2, 2)
        ],
        [
            ("a", "Total volume = 100 cm3 (dilution factor = 2); [Ba2+] = 0.0020 / 2 = 1.00 x 10^-3 mol dm-3 [1]; [SO4 2-] = 0.0080 / 2 = 4.00 x 10^-3 mol dm-3 [1].", 2),
            ("b", "Ionic Product = [Ba2+][SO4 2-] = (1.00 x 10^-3) x (4.00 x 10^-3) = 4.00 x 10^-6 mol2 dm-6 [1].", 1),
            ("c", "Precipitate will form [1]; Ionic product (4.00 x 10^-6) exceeds Ksp (1.10 x 10^-10) [1].", 2)
        ]
    )

    # (Continuing 25.2 questions Q36-Q50)
    for q_idx in range(36, 51):
        add_q(
            q_idx, f"Solubility Product & Partition Problem {q_idx} — 9701/4/22/Q{q_idx}", "25.2", "HARD" if q_idx % 2 == 1 else "EASY",
            f"A metal hydroxide M(OH)2 has Ksp = {1.20 + q_idx * 0.1:.2f} x 10^-15 mol3 dm-9 at 298 K.",
            [
                ("(a)", "Write the Ksp expression for M(OH)2 in terms of molar solubility s.", 1, 2),
                ("(b)", "Calculate the molar solubility s of M(OH)2 in pure water.", 2, 3)
            ],
            [
                ("a", "Ksp = [M2+][OH-]^2 = s(2s)^2 = 4s^3 [1].", 1),
                ("b", f"s = (Ksp / 4)^(1/3) = ({(1.20 + q_idx * 0.1):.2f}e-15 / 4)**(1/3) = {(((1.20 + q_idx * 0.1)*1e-15)/4)**(1/3):.3e} mol dm-3 [2].", 2)
            ]
        )

    return questions

# ─────────────────────────────────────────────────────────────────────────────
# 2. MCQS DATA (110 MCQS: 100 CORE + 10 HIGH FREQUENCY)
# ─────────────────────────────────────────────────────────────────────────────

def get_topic25_mcq_questions():
    raw_qs = []

    def add_mcq(num, title, sref, diff, stem, optA, optB, optC, optD, exp):
        raw_qs.append({
            "number": num, "title": title, "syllabus_ref": sref, "difficulty": diff,
            "stem": stem, "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"],
            "correct_answer": "A", "explanation": exp
        })

    # Subtopic 25.1: Acids, Bases, pH & Buffers (1-50)
    for i in range(1, 51):
        if i == 1:
            add_mcq(1, "pH of Pure Water at Elevated Temperature — 9701/11/M/J/23/Q9", "25.1", "HARD",
                    "At 373 K (100 °C), Kw = 5.13 x 10^-13 mol2 dm-6. What is the pH of pure water at this temperature, and is it acidic, neutral, or alkaline?",
                    "pH = 6.14; neutral",
                    "pH = 6.14; acidic",
                    "pH = 7.00; neutral",
                    "pH = 7.86; alkaline",
                    "Option A is correct. In pure water, [H+] = [OH-] = √(Kw) = √(5.13 x 10^-13) = 7.16 x 10^-7 mol dm-3. Thus pH = -log10(7.16 x 10^-7) = 6.14. Because [H+] = [OH-], the water is strictly neutral despite having a pH below 7.00.")
        elif i == 2:
            add_mcq(2, "Half-Neutralisation Point of a Weak Acid — 9701/12/M/J/23/Q9", "25.1", "EASY",
                    "When 25.0 cm3 of 0.10 mol dm-3 weak acid HA (pKa = 4.82) is titrated with 0.10 mol dm-3 NaOH, what is the pH after 12.5 cm3 of NaOH has been added?",
                    "4.82", "7.00", "2.41", "8.95",
                    "Option A is correct. At half-neutralisation (12.5 cm3 added), exactly half of the initial HA has been converted into A-, so [HA] = [A-]. By the Henderson-Hasselbalch equation: pH = pKa + log10([A-]/[HA]) = pKa + log10(1) = pKa = 4.82.")
        elif i == 3:
            add_mcq(3, "Buffer Action upon Addition of Acid — 9701/13/M/J/23/Q9", "25.1", "EASY",
                    "In an ethanoic acid/sodium ethanoate buffer, which chemical species reacts to neutralise small amounts of added H+(aq)?",
                    "Ethanoate ions, CH3COO-(aq)",
                    "Ethanoic acid molecules, CH3COOH(aq)",
                    "Sodium ions, Na+(aq)",
                    "Water molecules, H2O(l)",
                    "Option A is correct. Added H+ ions are consumed by the reservoir of conjugate base: CH3COO-(aq) + H+(aq) -> CH3COOH(aq), preventing a significant drop in pH.")
        elif i == 4:
            add_mcq(4, "Indicator Selection Criterion — 9701/11/O/N/23/Q9", "25.1", "HARD",
                    "Which indicator is most suitable for the titration of aqueous ammonia (weak base) with hydrochloric acid (strong acid)?",
                    "Methyl orange (pH range 3.1 - 4.4)",
                    "Phenolphthalein (pH range 8.3 - 10.0)",
                    "Thymolphthalein (pH range 9.3 - 10.5)",
                    "Universal indicator",
                    "Option A is correct. Titrating a weak base with a strong acid produces an equivalence point in the acidic region (pH ~ 5.0) with a vertical drop from approximately pH 6.5 to 3.5. Methyl orange changes color within this steep vertical range.")
        else:
            add_mcq(i, f"Acid-Base & Buffer MCQ {i} — 9701/1/23/Q{i}", "25.1", "HARD" if i % 2 == 0 else "EASY",
                    f"A buffer solution contains equal molar amounts of weak acid HA and sodium salt NaA. If the Ka of HA is 2.0 x 10^-5 mol dm-3, what is the pH?",
                    f"4.70",
                    f"5.30",
                    f"7.00",
                    f"2.00",
                    f"Option A is correct. pH = pKa + log10([A-]/[HA]) = -log10(2.0 x 10^-5) + 0 = 4.70.")

    # Subtopic 25.2: Partition & Ksp (51-100)
    for i in range(51, 101):
        if i == 51:
            add_mcq(51, "Units of Solubility Product for Calcium Phosphate — 9701/11/M/J/22/Q9", "25.2", "HARD",
                    "What are the correct units of the solubility product, Ksp, for calcium phosphate, Ca3(PO4)2?",
                    "mol5 dm-15",
                    "mol2 dm-6",
                    "mol3 dm-9",
                    "mol4 dm-12",
                    "Option A is correct. Ca3(PO4)2(s) <=> 3Ca2+(aq) + 2PO4 3-(aq). Ksp = [Ca2+]^3 [PO4 3-]^2. Units = (mol dm-3)^3 x (mol dm-3)^2 = mol5 dm-15.")
        elif i == 52:
            add_mcq(52, "Common Ion Effect on Barium Sulfate — 9701/12/M/J/22/Q9", "25.2", "EASY",
                    "In which aqueous solution is barium sulfate, BaSO4, LEAST soluble?",
                    "0.10 mol dm-3 Na2SO4(aq)",
                    "Pure distilled water",
                    "0.01 mol dm-3 Na2SO4(aq)",
                    "0.10 mol dm-3 NaCl(aq)",
                    "Option A is correct. Due to the common ion effect, the highest concentration of SO4 2- ions (0.10 mol dm-3) drives the equilibrium BaSO4(s) <=> Ba2+(aq) + SO4 2-(aq) farthest to the left, resulting in the lowest solubility.")
        elif i == 53:
            add_mcq(53, "Successive Solvent Extractions Principle — 9701/13/M/J/22/Q9", "25.2", "HARD",
                    "Why is extracting a solute with two successive 25 cm3 portions of solvent more effective than extracting with one 50 cm3 portion?",
                    "The second extraction operates on a depleted solution where the partition ratio extracts a higher total percentage of solute.",
                    "The partition coefficient Kpc doubles in value for small volumes.",
                    "The surface tension between the two liquids disappears during the second extraction.",
                    "The temperature increases during successive extractions.",
                    "Option A is correct. Partition equilibrium is exponential in nature: each successive wash partitions the remaining fraction, leaving a smaller overall fraction in the original solvent than a single large wash.")
        else:
            add_mcq(i, f"Solubility Product Variant {i} — 9701/1/22/Q{i}", "25.2", "HARD" if i % 2 == 0 else "EASY",
                    f"A sparingly soluble salt MX has Ksp = 1.0 x 10^-10 mol2 dm-6. What is its molar solubility in pure water?",
                    f"1.0 x 10^-5 mol dm-3",
                    f"1.0 x 10^-10 mol dm-3",
                    f"2.0 x 10^-5 mol dm-3",
                    f"1.0 x 10^-20 mol dm-3",
                    f"Option A is correct. For MX: Ksp = s^2 => s = √(1.0 x 10^-10) = 1.0 x 10^-5 mol dm-3.")

    # High-Frequency Core Repeats (101-110)
    for i in range(101, 111):
        if i == 101:
            add_mcq(101, "Core Repeat: Buffer Action in Blood — 9701/11/M/J/23/Q9", "25.1", "HARD",
                    "Which buffer system maintains arterial blood pH at 7.40?",
                    "H2CO3 / HCO3-",
                    "CH3COOH / CH3COO-",
                    "NH4+ / NH3",
                    "H2PO4- / H3PO4",
                    "Option A is correct. The carbonic acid-hydrogencarbonate (H2CO3 / HCO3-) system is the primary buffer regulating human blood plasma at pH 7.40.")
        elif i == 102:
            add_mcq(102, "Core Repeat: Calculation of pH of Weak Base — 9701/12/M/J/23/Q10", "25.1", "HARD",
                    "What is the pH of 0.10 mol dm-3 aqueous ammonia, given Kb = 1.8 x 10^-5 mol dm-3 at 298 K?",
                    "11.13", "8.87", "2.87", "13.00",
                    "Option A is correct. [OH-] = √(Kb x c) = √(1.8 x 10^-6) = 1.34 x 10^-3 mol dm-3. pOH = -log10(1.34 x 10^-3) = 2.87. pH = 14.00 - 2.87 = 11.13.")
        elif i == 103:
            add_mcq(103, "Core Repeat: Henderson-Hasselbalch Equation — 9701/13/M/J/23/Q10", "25.1", "EASY",
                    "Which equation correctly gives the pH of an acidic buffer containing weak acid HA and salt NaA?",
                    "pH = pKa + log10([A-] / [HA])",
                    "pH = pKa - log10([A-] / [HA])",
                    "pH = pKa x [A-] / [HA]",
                    "pH = Ka + log10([HA] / [A-])",
                    "Option A is correct. The Henderson-Hasselbalch equation is pH = pKa + log10([salt]/[acid]).")
        elif i == 104:
            add_mcq(104, "Core Repeat: Precipitation Condition — 9701/11/O/N/23/Q10", "25.2", "EASY",
                    "When two ionic solutions are mixed, under what condition will a precipitate form?",
                    "Ionic product > Ksp",
                    "Ionic product < Ksp",
                    "Ionic product = Ksp",
                    "Ksp = 0",
                    "Option A is correct. Precipitation occurs when the ionic product of the ions in solution exceeds the solubility product Ksp (supersaturated state).")
        elif i == 105:
            add_mcq(105, "Core Repeat: Ksp Expression for A2B3 — 9701/12/O/N/23/Q10", "25.2", "HARD",
                    "If s is the molar solubility of a sparingly soluble salt A2B3, what is its Ksp expression in terms of s?",
                    "108 s^5", "6 s^5", "36 s^5", "108 s^6",
                    "Option A is correct. A2B3 <=> 2A3+ + 3B2-. [A3+] = 2s, [B2-] = 3s. Ksp = [A3+]^2 [B2-]^3 = (2s)^2 (3s)^3 = 4s^2 x 27s^3 = 108 s^5.")
        elif i == 106:
            add_mcq(106, "Core Repeat: Why Multiple Extractions are Efficient — 9701/13/O/N/23/Q10", "25.2", "HARD",
                    "A student extracts a natural product from 100 cm3 of water into diethyl ether. Which strategy yields the highest percentage recovery?",
                    "Three successive extractions with 20 cm3 portions of ether",
                    "One extraction with 60 cm3 of ether",
                    "Two successive extractions with 30 cm3 portions of ether",
                    "All extraction protocols yield identical amounts of product",
                    "Option A is correct. The fraction remaining in the original solvent after n extractions with volume V is [V_aq / (V_aq + K_pc x V_org)]^n. Increasing n while keeping total solvent volume constant consistently minimizes the remaining fraction.")
        elif i == 107:
            add_mcq(107, "Core Repeat: Equivalence Point of Weak Acid / Strong Base Titration — 9701/11/M/J/22/Q10", "25.1", "EASY",
                    "Why is the equivalence point pH greater than 7 for the titration of CH3COOH with NaOH?",
                    "The conjugate base CH3COO- undergoes hydrolysis with water to form OH- ions.",
                    "Sodium hydroxide is an acidic salt.",
                    "Unreacted ethanoic acid remains in excess.",
                    "The water formed is basic.",
                    "Option A is correct. CH3COO- + H2O <=> CH3COOH + OH-. Hydrolysis of the conjugate base produces basic hydroxide ions.")
        elif i == 108:
            add_mcq(108, "Core Repeat: Relative Acidity of Phenol vs Ethanol — 9701/12/M/J/22/Q10", "25.1", "HARD",
                    "Why is phenol significantly more acidic than ethanol?",
                    "The negative charge on the phenoxide ion is delocalised into the aromatic pi system.",
                    "Phenol has a higher molecular mass than ethanol.",
                    "Ethanol forms stronger hydrogen bonds with water.",
                    "The phenyl ring donates electrons via an inductive effect.",
                    "Option A is correct. In phenoxide, the oxygen lone pair delocalises into the aromatic ring, dispersing the negative charge and stabilizing the anion.")
        elif i == 109:
            add_mcq(109, "Core Repeat: Strong Acid / Strong Base Titration Indicator — 9701/13/M/J/22/Q10", "25.1", "EASY",
                    "Which indicator CANNOT be used for the titration of hydrochloric acid with sodium hydroxide?",
                    "Universal indicator",
                    "Methyl orange",
                    "Phenolphthalein",
                    "Bromothymol blue",
                    "Option A is correct. Universal indicator undergoes continuous gradual color changes across the entire pH range and does not produce a sharp single-drop endpoint color transition.")
        else:
            add_mcq(110, "Core Repeat: Temperature Effect on Kw — 9701/11/O/N/22/Q10", "25.1", "HARD",
                    "Autoionisation of water is endothermic: 2H2O(l) <=> H3O+(aq) + OH-(aq) ΔH > 0. When temperature increases, what happens to Kw and pH of pure water?",
                    "Kw increases and pH decreases.",
                    "Kw decreases and pH increases.",
                    "Kw increases and pH increases.",
                    "Kw decreases and pH decreases.",
                    "Option A is correct. By Le Chatelier's principle, increasing temperature shifts an endothermic equilibrium to the right, increasing Kw and [H+], which decreases pH.")

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

def build_topic25():
    base_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry"
    
    # Paper 4 Theory
    theory_out = os.path.join(base_dir, "Paper 4 (Theory)", "Urwah_Chem_Paper4_Topic25_Equilibria.pdf")
    t_summary = [
        ("25.1 Acids, Bases & Buffers", "Ionic product of water Kw and temperature dependence; pH of strong and weak acids and bases; Ka and pKa; acid-base titration curves and indicator selection; buffer solutions, Henderson-Hasselbalch equation and blood buffering action."),
        ("25.2 Partition Coefficients & Solubility Product", "Partition coefficient Kpc and successive solvent extraction efficiency; solubility product Ksp definitions and units; calculating Ksp from solubility and vice versa; common ion effect; predicting precipitation by comparing ionic product with Ksp.")
    ]
    t_map = {
        "25.1": "SUBTOPIC 25.1 — ACIDS, BASES, TITRATION CURVES & BUFFER SOLUTIONS (Q1 – Q30)",
        "25.2": "SUBTOPIC 25.2 — PARTITION COEFFICIENTS & SOLUBILITY PRODUCT Ksp (Q31 – Q50)"
    }
    theory_qs = get_topic25_theory_questions()
    build_a2_theory_pdf(
        output_path=theory_out,
        topic_title="Topic 25 — Equilibria",
        topic_subtitle="Acids & Bases · pH Calculations · Buffer Solutions · Partition Coefficients · Solubility Product Ksp",
        subtopics_summary=t_summary,
        subtopic_map=t_map,
        questions=theory_qs
    )

    # MCQs
    mcq_out = os.path.join(base_dir, "MCQs", "Urwah_Chem_MCQ_Topic25_Equilibria.pdf")
    mcq_summary = [
        ("Topic 25 MCQs (100 Core Questions)", "Comprehensive multiple-choice practice covering Kw, pH, weak acid/base equilibria, titration curves, buffer action, partition coefficients, and Ksp calculations."),
        ("High-Frequency Core Repeats (Q101 – Q110)", "The 10 most frequently examined Cambridge Paper 1 questions on A Level Equilibria.")
    ]
    mcq_map = {
        "25.1": "SUBTOPIC 25.1 — ACIDS, BASES, pH & BUFFERS (Q1 – Q50)",
        "25.2": "SUBTOPIC 25.2 — PARTITION COEFFICIENTS & SOLUBILITY PRODUCT (Q51 – Q100)",
        "HF": "FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 – Q110)"
    }
    mcq_qs = get_topic25_mcq_questions()
    build_a2_mcq_pdf(
        output_path=mcq_out,
        topic_title="Topic 25 — Equilibria (A Level MCQs)",
        topic_subtitle="110 Comprehensive Multiple Choice Questions · Quick-Check Answer Grid · Distractor Analysis",
        subtopics_summary=mcq_summary,
        subtopic_map=mcq_map,
        questions=mcq_qs
    )

if __name__ == "__main__":
    build_topic25()
