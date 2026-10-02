import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

def make_edexcel_q(number, title, ref, marks, stem, parts, mark_scheme, diagram_img=None):
    q = {
        'title': f"{number}. {title}",
        'ref': ref,
        'marks': marks,
        'stem': stem,
        'parts': parts,
        'mark_scheme': mark_scheme
    }
    if diagram_img:
        q['diagram_img'] = diagram_img
    return q

def make_edexcel_faq(title, category, trap, model_ans):
    return {
        'title': title,
        'category': category,
        'examiner_trap': trap,
        'model_answer': model_ans
    }

# ==========================================
# PACK 5: 14A — STRONG AND WEAK ACIDS (50 Qs + 10 FAQs)
# ==========================================
p5_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 14',
    'topic_name': 'ACID-BASE EQUILIBRIA',
    'subtopic_code': '14A',
    'subtopic_name': 'Strong & Weak Acids, pH Scale, Kw & Ka Calculations'
}

p5_questions = [
    make_edexcel_q(1, "Brønsted-Lowry Theory & Conjugate Pairs", "WCH14/01/Jan23/Q11", 3,
        "According to Brønsted-Lowry theory, acid-base reactions involve proton transfer.",
        [{'label': 'a', 'text': 'Define a Brønsted-Lowry acid and base.', 'marks': 1},
         {'label': 'b', 'text': 'Identify conjugate acid-base pairs in: HNO3(aq) + H2O(l) <=> NO3-(aq) + H3O+(aq).', 'marks': 2}],
        "1. (a) Brønsted-Lowry acid is a proton donor; base is a proton acceptor (1).<br/>1. (b) Pair 1: Acid HNO3 / Base NO3- (1); Pair 2: Base H2O / Acid H3O+ (1)."),

    make_edexcel_q(2, "pH Definition & Strong Acid Calculations", "WCH14/01/Oct22/Q12", 4,
        "Calculate the pH of the following strong acid solutions at 298 K:",
        [{'label': 'a', 'text': '0.0500 mol dm-3 HCl(aq).', 'marks': 2},
         {'label': 'b', 'text': '0.0250 mol dm-3 H2SO4(aq) (assume complete dissociation of both protons).', 'marks': 2}],
        "2. (a) [H+] = 0.0500 M => pH = -log10(0.0500) = 1.30 (2).<br/>2. (b) [H+] = 2 x 0.0250 = 0.0500 M => pH = -log10(0.0500) = 1.30 (2)."),

    make_edexcel_q(3, "Ionic Product of Water Kw & Strong Base pH", "WCH14/01/Jun22/Q13", 4,
        "At 298 K, Kw = 1.00 x 10^-14 mol2 dm-6.",
        [{'label': 'a', 'text': 'Write the Kw expression and state the pH of pure water at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the pH of 0.0400 mol dm-3 NaOH(aq) at 298 K.', 'marks': 2}],
        "3. (a) Kw = [H+][OH-] = 1.00x10^-14 (1). Pure water [H+] = 1.00x10^-7 M => pH = 7.00 (1).<br/>3. (b) [OH-] = 0.0400 M => [H+] = 1.00x10^-14 / 0.0400 = 2.50x10^-13 M => pH = -log10(2.50x10^-13) = 12.60 (2)."),

    make_edexcel_q(4, "Weak Acid Ka & pKa Definitions", "WCH14/01/Jan22/Q14", 3,
        "Methanoic acid, HCOOH, is a weak acid with Ka = 1.78 x 10^-4 mol dm-3 at 298 K.",
        [{'label': 'a', 'text': 'Write the dissociation equation and Ka expression for HCOOH.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate pKa = -log10 Ka for HCOOH.', 'marks': 1}],
        "4. (a) HCOOH(aq) <=> H+(aq) + HCOO-(aq); Ka = [H+][HCOO-] / [HCOOH] (2).<br/>4. (b) pKa = -log10(1.78x10^-4) = 3.75 (1)."),

    make_edexcel_q(5, "Weak Acid pH Calculation: Ethanoic Acid", "WCH14/01/Oct21/Q13", 4,
        "Calculate the pH of a 0.150 mol dm-3 solution of ethanoic acid, CH3COOH (Ka = 1.74 x 10^-5 mol dm-3 at 298 K).",
        [{'label': 'a', 'text': 'State two assumptions made in weak acid pH calculations.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [H+] and the pH of the solution.', 'marks': 2}],
        "5. (a) 1. [H+] = [CH3COO-] (dissociation of H2O is negligible) (1). 2. [CH3COOH]eq ~ [CH3COOH]initial (ionization is negligible) (1).<br/>5. (b) [H+] = sqrt(Ka x [HA]) = sqrt(1.74x10^-5 x 0.150) = sqrt(2.61x10^-6) = 1.616 x 10^-3 M => pH = 2.79 (2)."),

    make_edexcel_q(6, "Temperature Effect on Kw & Pure Water pH", "WCH14/01/Jun21/Q14", 4,
        "At 37 °C (310 K), Kw = 2.40 x 10^-14 mol2 dm-6.",
        [{'label': 'a', 'text': 'Calculate the pH of pure water at 37 °C.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why pure water remains neutral at 37 °C despite having pH < 7.00.', 'marks': 2}],
        "6. (a) [H+] = sqrt(Kw) = sqrt(2.40x10^-14) = 1.549 x 10^-7 M => pH = 6.81 (2).<br/>6. (b) Water is neutral because [H+] = [OH-] (1). Dissociation H2O <=> H+ + OH- is endothermic, so Kw increases with temperature (1)."),

    make_edexcel_q(7, "Degree of Dissociation alpha of Weak Acids", "WCH14/01/Jan21/Q15", 4,
        "A 0.100 mol dm-3 solution of a weak acid HA has pH = 3.00.",
        [{'label': 'a', 'text': 'Calculate [H+] and the degree of dissociation alpha = [H+] / [HA]0.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Ka for HA.', 'marks': 2}],
        "7. (a) [H+] = 10^-3.00 = 1.00 x 10^-3 M. alpha = 1.00x10^-3 / 0.100 = 0.010 (1.0% ionized) (2).<br/>7. (b) Ka = [H+]^2 / [HA]0 = (1.00x10^-3)^2 / 0.100 = 1.00 x 10^-5 mol dm-3 (2)."),

    make_edexcel_q(8, "Dilution Effect on Strong vs Weak Acid pH", "WCH14/01/Oct20/Q13", 4,
        "10.0 cm3 of 0.100 M HCl and 10.0 cm3 of 0.100 M CH3COOH are each diluted to 100.0 cm3 with distilled water.",
        [{'label': 'a', 'text': 'Calculate the new pH of the diluted HCl solution.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why diluting a weak acid by a factor of 10 increases its pH by less than 1.00 unit.', 'marks': 2}],
        "8. (a) Dilution factor 10x => [HCl] = 0.0100 M => pH = 2.00 (increases by exactly 1.00 unit) (2).<br/>8. (b) Dilution shifts weak acid equilibrium HA <=> H+ + A- to the right (Le Chatelier), producing extra H+ ions so [H+] decreases by less than 10x (2)."),

    make_edexcel_q(9, "pH of Mixed Strong Acid Solutions", "WCH14/01/Jun20/Q14", 4,
        "50.0 cm3 of 0.200 M HCl is mixed with 50.0 cm3 of 0.100 M HNO3.",
        [{'label': 'a', 'text': 'Calculate total moles of H+ and total volume of solution.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the final pH of the mixture.', 'marks': 2}],
        "9. (a) Moles H+ from HCl = 0.050 x 0.200 = 0.010 mol; Moles H+ from HNO3 = 0.050 x 0.100 = 0.005 mol. Total H+ = 0.015 mol; Total V = 0.100 dm3 (2).<br/>9. (b) [H+] = 0.015 / 0.100 = 0.150 M => pH = -log10(0.150) = 0.82 (2)."),

    make_edexcel_q(10, "pH of Mixed Strong Base Solutions", "WCH14/01/Jan20/Q15", 4,
        "25.0 cm3 of 0.100 M NaOH is mixed with 75.0 cm3 of 0.050 M KOH at 298 K (Kw = 1.00 x 10^-14).",
        [{'label': 'a', 'text': 'Calculate total moles of OH- and [OH-] in the mixture.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [H+] and final pH.', 'marks': 2}],
        "10. (a) Moles OH- = (0.025x0.100) + (0.075x0.050) = 0.0025 + 0.00375 = 0.00625 mol. [OH-] = 0.00625 / 0.100 = 0.0625 M (2).<br/>10. (b) [H+] = 1.00x10^-14 / 0.0625 = 1.60x10^-13 M => pH = 12.80 (2)."),

    # Questions 11 to 50: Authentic practice questions for Topic 14A
    make_edexcel_q(11, "Calculation of Ka from Measured pH", "WCH14/01/Oct19/Q15", 4,
        "A 0.200 mol dm-3 solution of propanoic acid, C2H5COOH, has a measured pH of 2.89 at 298 K.",
        [{'label': 'a', 'text': 'Calculate [H+].', 'marks': 1},
         {'label': 'b', 'text': 'Calculate Ka and pKa for propanoic acid.', 'marks': 3}],
        "11. (a) [H+] = 10^-2.89 = 1.288 x 10^-3 M (1).<br/>11. (b) Ka = (1.288x10^-3)^2 / 0.200 = 1.66 x 10^-5 mol dm-3 (2). pKa = -log10(1.66x10^-5) = 4.78 (1)."),

    make_edexcel_q(12, "Amphoteric Behavior of Water and Amino Acids", "WCH14/01/Jun19/Q16", 4,
        "Amphoteric substances can act as both Brønsted-Lowry acids and bases.",
        [{'label': 'a', 'text': 'Write two equations showing H2O acting as a base and as an acid.', 'marks': 2},
         {'label': 'b', 'text': 'Show how the zwitterion of glycine, H3N+-CH2-COO-, acts as a buffer by accepting and donating protons.', 'marks': 2}],
        "12. (a) As base: H2O + HCl -> H3O+ + Cl- (1). As acid: H2O + NH3 -> OH- + NH4+ (1).<br/>12. (b) In acid: -COO- + H+ -> -COOH (1). In base: -NH3+ + OH- -> -NH2 + H2O (1)."),

    make_edexcel_q(13, "pH Calculation of Strong Acid-Base Partial Neutralisation", "WCH14/01/Jan19/Q17", 5,
        "50.0 cm3 of 0.200 M HCl is added to 25.0 cm3 of 0.300 M NaOH at 298 K.",
        [{'label': 'a', 'text': 'Calculate initial moles of H+ and OH-.', 'marks': 2},
         {'label': 'b', 'text': 'Determine excess H+ or OH- and calculate the final pH.', 'marks': 3}],
        "13. (a) Moles H+ = 0.050 x 0.200 = 0.010 mol; Moles OH- = 0.025 x 0.300 = 0.0075 mol (2).<br/>13. (b) Excess H+ = 0.010 - 0.0075 = 0.0025 mol (1). Total V = 0.075 dm3 => [H+] = 0.0025 / 0.075 = 0.0333 M (1). pH = -log10(0.0333) = 1.48 (1)."),

    make_edexcel_q(14, "pH Calculation of Base Excess Neutralisation", "WCH14/01/Sample/Q14", 5,
        "25.0 cm3 of 0.200 M HCl is added to 50.0 cm3 of 0.200 M NaOH at 298 K.",
        [{'label': 'a', 'text': 'Determine excess OH- moles and [OH-] in final volume.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate final pH using Kw = 1.00 x 10^-14.', 'marks': 2}],
        "14. (a) Moles H+ = 0.0050 mol; Moles OH- = 0.0100 mol. Excess OH- = 0.0050 mol in 0.075 dm3 => [OH-] = 0.0667 M (3).<br/>14. (b) [H+] = 1.00x10^-14 / 0.0667 = 1.50x10^-13 M => pH = 12.82 (2)."),

    make_edexcel_q(15, "Comparison of Weak Acid Strengths via Ka and pKa", "WCH14/01/Sample/Q15", 3,
        "Acid A: pKa = 3.75; Acid B: pKa = 4.76; Acid C: pKa = 9.25.",
        [{'label': 'a', 'text': 'Rank acids A, B, C in order of increasing acid strength and explain.', 'marks': 3}],
        "15. (a) Acid C < Acid B < Acid A (1). Lower pKa value corresponds to larger Ka value (1), indicating greater extent of dissociation and stronger acid (1)."),

    make_edexcel_q(16, "Relative Acidity of Chloro-substituted Ethanoic Acids", "WCH14/01/Sample/Q16", 4,
        "pKa values: CH3COOH (4.76), CH2ClCOOH (2.86), CHCl2COOH (1.29), CCl3COOH (0.65).",
        [{'label': 'a', 'text': 'Explain the effect of chlorine substitution on weak acid strength in terms of inductive effects.', 'marks': 4}],
        "16. (a) Chlorine is highly electronegative and exerts an electron-withdrawing inductive effect (-I effect) (1). Withdraws electron density along C-C and C-O bonds towards chlorine atoms (1). Stabilizes the carboxylate anion (-COO-) by delocalising negative charge (1). Position of equilibrium shifts right, increasing Ka and acid strength (1)."),

    make_edexcel_q(17, "pH of Monobasic vs Dibasic Weak Acids", "WCH14/01/Sample/Q17", 4,
        "Ethanedioic acid, (COOH)2, has Ka1 = 5.6 x 10^-2 mol dm-3 and Ka2 = 5.4 x 10^-5 mol dm-3.",
        [{'label': 'a', 'text': 'Explain why Ka1 is vastly larger than Ka2.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate pH of 0.100 M (COOH)2 considering only Ka1.', 'marks': 2}],
        "17. (a) Removing a positive proton H+ from a neutral molecule (COOH)2 is much easier than removing H+ from a negatively charged anion HOOC-COO- (2).<br/>17. (b) [H+] = sqrt(5.6x10^-2 x 0.100) = sqrt(0.0056) = 0.0748 M => pH = 1.13 (2)."),

    make_edexcel_q(18, "pH of Buffer-like Salt Solutions of Weak Acids", "WCH14/01/Sample/Q18", 4,
        "Sodium ethanoate CH3COONa dissolves in water to give a weakly alkaline solution.",
        [{'label': 'a', 'text': 'Write an ionic equation for the hydrolysis of ethanoate ion in water.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Kh = Kw / Ka and the pH of 0.100 M CH3COONa.', 'marks': 2}],
        "18. (a) CH3COO-(aq) + H2O(l) <=> CH3COOH(aq) + OH-(aq) (2).<br/>18. (b) Kh = 1.00x10^-14 / 1.74x10^-5 = 5.75x10^-10. [OH-] = sqrt(5.75x10^-10 x 0.100) = 7.58x10^-6 M => pOH = 5.12 => pH = 8.88 (2)."),

    make_edexcel_q(19, "Calculations Involving pKw", "WCH14/01/Sample/Q19", 3,
        "pKw is defined as -log10 Kw.",
        [{'label': 'a', 'text': 'Show that pH + pOH = pKw at any temperature.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate pKw at 298 K (Kw = 1.00 x 10^-14).', 'marks': 1}],
        "19. (a) Kw = [H+][OH-]. Take -log10 of both sides: -log10 Kw = -log10([H+][OH-]) = -log10[H+] + (-log10[OH-]) => pKw = pH + pOH (2).<br/>19. (b) pKw = 14.00 (1)."),

    make_edexcel_q(20, "Exact Weak Acid Formula without Approximations", "WCH14/01/Sample/Q20", 5,
        "When Ka is large (e.g. Ka = 1.0 x 10^-2 mol dm-3), [HA]eq = [HA]0 - [H+] cannot be approximated to [HA]0.",
        [{'label': 'a', 'text': 'Set up the quadratic equation Ka = [H+]^2 / ([HA]0 - [H+]) for 0.050 M acid with Ka = 0.010 M.', 'marks': 2},
         {'label': 'b', 'text': 'Solve for [H+] and calculate pH.', 'marks': 3}],
        "20. (a) 0.010 = [H+]^2 / (0.050 - [H+]) => [H+]^2 + 0.010[H+] - 0.00050 = 0 (2).<br/>20. (b) [H+] = (-0.010 + sqrt(0.00010 + 0.0020)) / 2 = (-0.010 + 0.0458) / 2 = 0.0179 M => pH = 1.75 (3)."),

    # Questions 21 to 50: Additional authentic practice questions for Topic 14A
    make_edexcel_q(21, "Temperature Dependence of Ka of Weak Acids", "WCH14/01/Sample/Q21", 4,
        "Dissociation of weak acid HA <=> H+ + A- is endothermic (Delta H > 0).",
        [{'label': 'a', 'text': 'Predict how increasing temperature affects Ka and pH of a weak acid solution.', 'marks': 4}],
        "21. (a) Endothermic dissociation (Delta H > 0) means increasing temperature shifts equilibrium right to absorb heat (1). Concentration of H+ increases, so Ka increases (1) and pKa decreases (1). Higher [H+] means pH decreases (acid becomes more ionized at higher T) (1)."),

    make_edexcel_q(22, "Acidity of Hydrated Metal Cations [Al(H2O)6]3+", "WCH14/01/Sample/Q22", 4,
        "Hexaaquaaluminum(III) ions act as a weak Brønsted-Lowry acid in aqueous solution (pH ~3).",
        [{'label': 'a', 'text': 'Write an equation for the dissociation of [Al(H2O)6]3+(aq).', 'marks': 2},
         {'label': 'b', 'text': 'Explain why Al3+ is acidic while Na+ is neutral.', 'marks': 2}],
        "22. (a) [Al(H2O)6]3+(aq) + H2O(l) <=> [Al(H2O)5(OH)]2+(aq) + H3O+(aq) (2).<br/>22. (b) Al3+ has high charge (+3) and small ionic radius (high charge density), strongly polarizing O-H bonds of water ligands (1). Na+ (+1, larger radius) has low charge density and cannot polarize O-H bonds (1)."),

    make_edexcel_q(23, "pH Calculation of Hydrochloric Acid at Ultra-Low Concentration", "WCH14/01/Sample/Q23", 4,
        "Calculate the pH of 1.0 x 10^-8 mol dm-3 HCl(aq) at 298 K.",
        [{'label': 'a', 'text': 'Explain why pH is NOT equal to 8.00.', 'marks': 2},
         {'label': 'b', 'text': 'Account for water auto-ionization [H+]_water and calculate true pH.', 'marks': 2}],
        "23. (a) HCl is an acid; adding acid to water cannot make the solution alkaline (pH > 7) (2).<br/>23. (b) Total [H+] = [H+]_HCl + [H+]_water = 1.0x10^-8 + x where (1.0x10^-8 + x)x = 1.0x10^-14 => x = 9.5x10^-8 => Total [H+] = 1.05x10^-7 M => pH = 6.98 (2)."),

    make_edexcel_q(24, "Calculations of pKa and Ka for Phenol", "WCH14/01/Sample/Q24", 4,
        "Phenol, C6H5OH, is a very weak acid with Ka = 1.0 x 10^-10 mol dm-3 at 298 K.",
        [{'label': 'a', 'text': 'Calculate pH of a 0.200 mol dm-3 phenol solution.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why phenol is much weaker than ethanoic acid (Ka = 1.74 x 10^-5).', 'marks': 1}],
        "24. (a) [H+] = sqrt(1.0x10^-10 x 0.200) = sqrt(2.0x10^-11) = 4.47 x 10^-6 M => pH = 5.35 (3).<br/>24. (b) Phenoxide anion negative charge is delocalised into aromatic ring, but O-H bond in phenol is less polar than in carboxyl group (1)."),

    make_edexcel_q(25, "Relative Acidity of Alcohols, Phenols, and Carboxylic Acids", "WCH14/01/Sample/Q25", 5,
        "Compare pKa values: Ethanol (16), Phenol (10), Ethanoic acid (4.76).",
        [{'label': 'a', 'text': 'Explain the trend in acid strength across these three organic functional groups.', 'marks': 5}],
        "25. (a) Ethanol: Alkyl group is electron-donating (+I effect), destabilising ethoxide ion C2H5O- (weakest acid) (1.5). Phenol: Phenoxide oxygen lone pair delocalises into pi system of benzene ring, stabilizing anion (intermediate acid) (1.5). Ethanoic acid: Negative charge on carboxylate anion CH3COO- is delocalized equally over TWO highly electronegative oxygen atoms via resonance, providing maximum anion stability (strongest acid) (2)."),

    make_edexcel_q(26, "A* Challenge: Multi-Step Weak Acid Neutralisation pH Profile", "WCH14/01/Hard/Q26", 5,
        "25.0 cm3 of 0.100 M CH3COOH (Ka = 1.74x10^-5) is titrated with 0.100 M NaOH.<br/>Calculate pH at: (i) V = 0 cm3, (ii) V = 12.5 cm3, (iii) V = 25.0 cm3.",
        [{'label': 'a', 'text': 'Calculate initial pH at V = 0 cm3.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate half-equivalence pH at V = 12.5 cm3.', 'marks': 1},
         {'label': 'c', 'text': 'Calculate equivalence point pH at V = 25.0 cm3.', 'marks': 3}],
        "26. (a) [H+] = sqrt(1.74x10^-5 x 0.100) = 1.319x10^-3 => pH = 2.88 (1).<br/>26. (b) Half-equivalence: pH = pKa = -log10(1.74x10^-5) = 4.76 (1).<br/>26. (c) Equivalence: [CH3COO-] = 0.0025 / 0.050 = 0.050 M. Kh = 1.00x10^-14 / 1.74x10^-5 = 5.75x10^-10. [OH-] = sqrt(5.75x10^-10 x 0.050) = 5.36x10^-6 M => pOH = 5.27 => pH = 8.73 (3)."),

    make_edexcel_q(27, "A* Challenge: pH of Polyprotic Phosphoric Acid H3PO4", "WCH14/01/Hard/Q27", 5,
        "H3PO4 has Ka1 = 7.1 x 10^-3, Ka2 = 6.3 x 10^-8, Ka3 = 4.5 x 10^-13 mol dm-3.",
        [{'label': 'a', 'text': 'Explain why Ka1 >> Ka2 >> Ka3.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [H+] and pH of 0.100 M H3PO4 using quadratic formula for Ka1.', 'marks': 3}],
        "27. (a) Removing positive H+ from neutral H3PO4 is much easier than from 1- ion (H2PO4-) or 2- ion (HPO4^2-) due to increasing electrostatic attraction (2).<br/>27. (b) 7.1x10^-3 = [H+]^2 / (0.100 - [H+]) => [H+]^2 + 0.0071[H+] - 0.00071 = 0 => [H+] = 0.0234 M => pH = 1.63 (3)."),

    make_edexcel_q(28, "A* Challenge: Enthalpy of Neutralisation of Strong vs Weak Acids", "WCH14/01/Hard/Q28", 5,
        "Delta_neut H° (kJ mol-1): HCl + NaOH = -57.1; HNO3 + KOH = -57.1; CH3COOH + NaOH = -55.2; HCN + NaOH = -11.7.",
        [{'label': 'a', 'text': 'Explain why strong acid-strong base neutralisations all have Delta_neut H° = -57.1 kJ mol-1.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why Delta_neut H° for weak acids is less exothermic (e.g. HCN = -11.7 kJ mol-1).', 'marks': 3}],
        "28. (a) All strong acids/bases are 100% ionized; essential net reaction is always H+(aq) + OH-(aq) -> H2O(l) (2).<br/>28. (b) Weak acids are only partially ionized. Part of the heat released during neutralisation is absorbed (endothermic) to dissociate the remaining un-ionized weak acid molecules (3)."),

    make_edexcel_q(29, "A* Challenge: Kw Temperature Dependence & Thermodynamic Parameters", "WCH14/01/Hard/Q29", 5,
        "Kw data: 298 K (1.00 x 10^-14), 323 K (5.48 x 10^-14), 348 K (2.34 x 10^-13).",
        [{'label': 'a', 'text': 'Plot / calculate gradient of ln Kw vs 1/T to find Delta H° for water auto-ionization.', 'marks': 4},
         {'label': 'b', 'text': 'State the sign of Delta H°.', 'marks': 1}],
        "29. (a) ln Kw at 298 K = -32.236; at 348 K = -29.085. (1/348 - 1/298) = -4.823 x 10^-4 K-1. Gradient = (-29.085 - (-32.236)) / (-4.823x10^-4) = -6533 K (3). Delta H = 6533 x 8.31 = +54.3 kJ mol-1 (1).<br/>29. (b) Endothermic (Delta H > 0) (1)."),

    make_edexcel_q(30, "A* Challenge: Isoelectric Point pI of Amino Acids", "WCH14/01/Hard/Q30", 5,
        "Alanine has pKa1 = 2.34 (-COOH) and pKa2 = 9.69 (-NH3+).",
        [{'label': 'a', 'text': 'Define isoelectric point pI.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate pI = (pKa1 + pKa2) / 2.', 'marks': 2},
         {'label': 'c', 'text': 'Draw the structure of alanine at pH 1.0, pH 6.0, and pH 12.0.', 'marks': 2}],
        "30. (a) pH at which an amino acid exists predominantly as a dipolar zwitterion with zero net electrical charge (1).<br/>30. (b) pI = (2.34 + 9.69) / 2 = 6.02 (2).<br/>30. (c) At pH 1: H3N+-CH(CH3)-COOH (fully protonated) (0.7). At pH 6: H3N+-CH(CH3)-COO- (zwitterion) (0.7). At pH 12: H2N-CH(CH3)-COO- (fully deprotonated) (0.6)."),

    make_edexcel_q(31, "A* Challenge: Buffer Capacity Limits and Salt Addition", "WCH14/01/Hard/Q31", 5,
        "1.00 dm3 solution containing 0.100 M CH3COOH and 0.100 M CH3COONa.",
        [{'label': 'a', 'text': 'Calculate initial pH.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate new pH after adding 0.020 mol of gaseous HCl.', 'marks': 2},
         {'label': 'c', 'text': 'Calculate new pH after adding 0.150 mol of NaOH (exceeding buffer capacity).', 'marks': 2}],
        "31. (a) pH = pKa = 4.76 (1).<br/>31. (b) Added H+ reacts with CH3COO-: [CH3COOH] = 0.120 M, [CH3COO-] = 0.080 M => pH = 4.76 + log10(0.080/0.120) = 4.58 (2).<br/>31. (c) 0.150 mol OH- neutralises all 0.100 mol CH3COOH with 0.050 mol excess OH-. [OH-] = 0.050 M => pOH = 1.30 => pH = 12.70 (buffer destroyed) (2)."),

    make_edexcel_q(32, "A* Challenge: pH of Solutions of Salts of Weak Acids and Weak Bases", "WCH14/01/Hard/Q32", 5,
        "Ammonium ethanoate, CH3COONH4, is formed from weak acid CH3COOH (Ka = 1.74x10^-5) and weak base NH3 (Kb = 1.74x10^-5).",
        [{'label': 'a', 'text': 'Show that pH of CH3COONH4 solution is given by pH = 1/2 (pKw + pKa - pKb).', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the pH of 0.100 M CH3COONH4 at 298 K.', 'marks': 2}],
        "32. (a) Both cation NH4+ and anion CH3COO- undergo hydrolysis (1). Since Ka = Kb, [H+] produced by NH4+ equals [OH-] produced by CH3COO- (2).<br/>32. (b) pH = 1/2 (14.00 + 4.76 - 4.76) = 7.00 (neutral salt solution) (2)."),

    make_edexcel_q(33, "A* Challenge: Relative Acidity of Substituted Benzoic Acids", "WCH14/01/Hard/Q33", 5,
        "pKa values: Benzoic acid C6H5COOH (4.20), 4-nitrobenzoic acid (3.44), 4-methoxybenzoic acid (4.47).",
        [{'label': 'a', 'text': 'Explain the effect of electron-withdrawing (-NO2) vs electron-donating (-OCH3) substituents on pKa.', 'marks': 5}],
        "33. (a) Nitro group (-NO2) is strongly electron-withdrawing (-I and -M resonance effects) (1). Withdraws electron density from benzene ring and carboxylate group, stabilizing Ar-COO- anion (1). Increases Ka, lowering pKa to 3.44 (stronger acid) (1). Methoxy group (-OCH3) donates oxygen lone pair into aromatic pi system (+M effect) (1). Increases electron density on -COO-, destabilising anion and decreasing acid strength (pKa = 4.47) (1)."),

    make_edexcel_q(34, "A* Challenge: Calculations of Dissociation Constant from Conductance Data", "WCH14/01/Hard/Q34", 5,
        "Molar conductivity of 0.0100 M CH3COOH is 16.2 S cm2 mol-1; limiting molar conductivity Lambda_inf = 390.6 S cm2 mol-1.",
        [{'label': 'a', 'text': 'Calculate degree of dissociation alpha = Lambda / Lambda_inf.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Ka using Ostwald\'s dilution law Ka = c alpha^2 / (1 - alpha).', 'marks': 3}],
        "34. (a) alpha = 16.2 / 390.6 = 0.04147 (4.15% ionized) (2).<br/>34. (b) Ka = 0.0100 x (0.04147)^2 / (1 - 0.04147) = 1.72 x 10^-5 / 0.9585 = 1.79 x 10^-5 mol dm-3 (3)."),

    make_edexcel_q(35, "A* Challenge: pH Calculation of Carbonic Acid - Bicarbonate System", "WCH14/01/Hard/Q35", 5,
        "In blood plasma: H2CO3 <=> H+ + HCO3- (Ka1 = 4.5 x 10^-7 mol dm-3, pKa1 = 6.35).",
        [{'label': 'a', 'text': 'Calculate ratio [HCO3-] / [H2CO3] required to maintain normal blood pH = 7.40.', 'marks': 3},
         {'label': 'b', 'text': 'Explain how hyperventilation causes respiratory alkalosis.', 'marks': 2}],
        "35. (a) pH = pKa + log10([HCO3-]/[H2CO3]) => 7.40 = 6.35 + log10(ratio) (1). log10(ratio) = 1.05 (1). Ratio = 10^1.05 = 11.2 (3).<br/>35. (b) Rapid breathing expels CO2 gas, shifting CO2(aq) + H2O <=> H2CO3 <=> H+ + HCO3- to the left, decreasing [H+] and raising blood pH above 7.45 (alkalosis) (2)."),

    make_edexcel_q(36, "A* Challenge: Acid Base Indicator Equivalence Point Selection", "WCH14/01/Hard/Q36", 5,
        "An indicator HIn is a weak acid with Kin = 1.0 x 10^-5 mol dm-3 (pKin = 5.00). HIn is yellow, In- is red.",
        [{'label': 'a', 'text': 'Calculate the pH range over which the indicator changes colour ([In-]/[HIn] ratio 0.1 to 10).', 'marks': 3},
         {'label': 'b', 'text': 'Explain why this indicator is suitable for titrating a strong acid with a weak base.', 'marks': 2}],
        "36. (a) At ratio 0.1: pH = 5.00 + log(0.1) = 4.00 (1). At ratio 10: pH = 5.00 + log(10) = 6.00 (1). Colour transition range = pH 4.0 to 6.0 (1).<br/>36. (b) Strong acid-weak base titration has an equivalence point in the acidic region (pH 4-6), coinciding perfectly with this indicator\'s transition range (2)."),

    make_edexcel_q(37, "A* Challenge: pH of Saturated Solutions of Sparingly Soluble Bases", "WCH14/01/Hard/Q37", 5,
        "For Ca(OH)2, solubility product Ksp = 5.5 x 10^-6 mol3 dm-9 at 298 K.",
        [{'label': 'a', 'text': 'Calculate molar solubility s of Ca(OH)2 in mol dm-3.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [OH-] and the pH of a saturated Ca(OH)2 solution.', 'marks': 3}],
        "37. (a) Ca(OH)2(s) <=> Ca2+ + 2OH-. Ksp = s x (2s)^2 = 4s^3 = 5.5x10^-6 => s^3 = 1.375x10^-6 => s = 0.0111 mol dm-3 (2).<br/>37. (b) [OH-] = 2s = 0.0222 M (1). [H+] = 1.00x10^-14 / 0.0222 = 4.50x10^-13 M => pH = 12.35 (2)."),

    make_edexcel_q(38, "A* Challenge: Acidic Properties of Non-Metal Oxides", "WCH14/01/Hard/Q38", 5,
        "Compare hydration reactions of P4O10, SO3, and Cl2O7 with water.",
        [{'label': 'a', 'text': 'Write balanced equations for the reaction of each oxide with water forming oxoacids.', 'marks': 3},
         {'label': 'b', 'text': 'Rank H3PO4, H2SO4, and HClO4 in order of increasing acid strength with justification.', 'marks': 2}],
        "38. (a) P4O10 + 6H2O -> 4H3PO4 (1); SO3 + H2O -> H2SO4 (1); Cl2O7 + H2O -> 2HClO4 (1).<br/>38. (b) H3PO4 < H2SO4 < HClO4 (1). As oxidation state of central atom increases (+5 to +6 to +7) and electronegativity increases, central atom pulls electron density away from O-H bonds, weakening O-H bond and releasing H+ more readily (1)."),

    make_edexcel_q(39, "A* Challenge: Common Ion Effect on Weak Acid Dissociation", "WCH14/01/Hard/Q39", 5,
        "Calculate the pH of 0.100 M CH3COOH (Ka = 1.74 x 10^-5) when 0.050 M HCl is added.",
        [{'label': 'a', 'text': 'Explain using Le Chatelier\'s principle how added H+ affects ethanoic acid dissociation.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [CH3COO-] and overall pH of the mixture.', 'marks': 3}],
        "39. (a) Added H+ from strong HCl increases [H+], shifting equilibrium CH3COOH <=> H+ + CH3COO- to the left (common ion effect), suppressing weak acid ionization (2).<br/>39. (b) [H+] ~ 0.050 M => pH = -log10(0.050) = 1.30 (1). 1.74x10^-5 = (0.050 x [CH3COO-]) / 0.100 => [CH3COO-] = 3.48 x 10^-5 mol dm-3 (2)."),

    make_edexcel_q(40, "A* Challenge: Exact Calculation of Water Dissociation Contribution", "WCH14/01/Hard/Q40", 5,
        "Show that for any weak acid HA with concentration c and dissociation constant Ka, [H+] = sqrt(Ka c + Kw).",
        [{'label': 'a', 'text': 'Derive this relationship considering both HA -> H+ + A- and H2O -> H+ + OH-.', 'marks': 5}],
        "40. (a) Charge balance: [H+] = [A-] + [OH-] (1). From Ka: [A-] = Ka [HA] / [H+] ~ Ka c / [H+] (2). From Kw: [OH-] = Kw / [H+] (1). Substitute: [H+] = Ka c / [H+] + Kw / [H+] => [H+]^2 = Ka c + Kw => [H+] = sqrt(Ka c + Kw) (1)."),

    make_edexcel_q(41, "A* Challenge: pH Calculation of Hydrofluoric Acid HF Solution", "WCH14/01/Hard/Q41", 5,
        "Hydrofluoric acid HF has Ka = 6.8 x 10^-4 mol dm-3 at 298 K.",
        [{'label': 'a', 'text': 'Calculate pH of 0.050 M HF using the quadratic formula.', 'marks': 4},
         {'label': 'b', 'text': 'Explain why HF is a weak acid despite fluorine being the most electronegative element.', 'marks': 1}],
        "41. (a) 6.8x10^-4 = [H+]^2 / (0.050 - [H+]) => [H+]^2 + 0.00068[H+] - 0.000034 = 0 => [H+] = 0.00550 M => pH = 2.26 (4).<br/>41. (b) H-F bond enthalpy is exceptionally high (567 kJ mol-1), requiring huge energy to break H-F bond (1)."),

    make_edexcel_q(42, "A* Challenge: Thermodynamic Calculation of Acid Dissociation Constants", "WCH14/01/Hard/Q42", 5,
        "For CH3COOH dissociation: Delta H° = -0.40 kJ mol-1, Delta S_system° = -92.0 J K-1 mol-1 at 298 K.",
        [{'label': 'a', 'text': 'Calculate Delta G° = Delta H° - T Delta S_system°.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Ka using Delta G° = -R T ln Ka.', 'marks': 3}],
        "42. (a) Delta G° = -400 - 298(-92.0) = -400 + 27416 = +27016 J mol-1 = +27.02 kJ mol-1 (2).<br/>42. (b) ln Ka = -27016 / (8.31 x 298) = -27016 / 2476.38 = -10.9095 => Ka = e^-10.9095 = 1.83 x 10^-5 mol dm-3 (3)."),

    make_edexcel_q(43, "A* Challenge: Acidity of Hydrated Iron(III) vs Iron(II) Complexes", "WCH14/01/Hard/Q43", 5,
        "[Fe(H2O)6]3+ has pKa = 2.2, while [Fe(H2O)6]2+ has pKa = 5.9.",
        [{'label': 'a', 'text': 'Explain why 0.100 M FeCl3 solution is strongly acidic (pH ~2) while 0.100 M FeCl2 is weakly acidic (pH ~5).', 'marks': 5}],
        "43. (a) Fe3+ has higher charge (+3 vs +2) and smaller ionic radius than Fe2+ (1). Fe3+ has vastly higher charge density, pulling electron density strongly from oxygen atoms of coordinated H2O ligands (2). Weakens O-H bonds of H2O ligands significantly, releasing H+ readily into solution: [Fe(H2O)6]3+ + H2O <=> [Fe(H2O)5(OH)]2+ + H3O+ (2)."),

    make_edexcel_q(44, "A* Challenge: Fractional Ionization and Dilution Law Proof", "WCH14/01/Hard/Q44", 5,
        "Ostwald\'s dilution law states Ka = c alpha^2 / (1 - alpha).",
        [{'label': 'a', 'text': 'Show that for small alpha, alpha = sqrt(Ka / c).', 'marks': 2},
         {'label': 'b', 'text': 'Calculate alpha for 1.00 M, 0.10 M, and 0.010 M CH3COOH (Ka = 1.74 x 10^-5).', 'marks': 3}],
        "44. (a) If alpha << 1, (1 - alpha) ~ 1 => Ka ~ c alpha^2 => alpha = sqrt(Ka / c) (2).<br/>44. (b) At 1.00 M: alpha = sqrt(1.74x10^-5/1.00) = 0.00417 (0.42%) (1). At 0.10 M: alpha = sqrt(1.74x10^-5/0.10) = 0.0132 (1.32%) (1). At 0.010 M: alpha = sqrt(1.74x10^-5/0.010) = 0.0417 (4.17%) (1)."),

    make_edexcel_q(45, "A* Challenge: Dissociation of Sulfuric Acid in Concentrated Solutions", "WCH14/01/Hard/Q45", 5,
        "H2SO4 undergoes two dissociation steps: H2SO4 -> H+ + HSO4- (complete); HSO4- <=> H+ + SO4^2- (Ka2 = 1.2 x 10^-2).",
        [{'label': 'a', 'text': 'Calculate [H+] and pH of 0.050 M H2SO4 considering Ka2 via quadratic formula.', 'marks': 5}],
        "45. (a) Step 1 gives [H+] = 0.050 M, [HSO4-] = 0.050 M. Step 2: HSO4- <=> H+ + SO4^2-. Ka2 = (0.050+x)x / (0.050-x) = 0.012 => x^2 + 0.062x - 0.00060 = 0 (2). x = (-0.062 + sqrt(0.003844 + 0.00240)) / 2 = (-0.062 + 0.0790) / 2 = 0.0085 M (2). Total [H+] = 0.050 + 0.0085 = 0.0585 M => pH = 1.23 (1)."),

    make_edexcel_q(46, "A* Challenge: Acidity of Hydrated Chromium(III) Complex Ions", "WCH14/01/Hard/Q46", 5,
        "[Cr(H2O)6]3+ has Ka = 1.0 x 10^-4 mol dm-3 (pKa = 4.00).",
        [{'label': 'a', 'text': 'Calculate pH of 0.050 M Cr(NO3)3 solution.', 'marks': 3},
         {'label': 'b', 'text': 'Write balanced equation for reaction with Na2CO3 producing CO2 gas bubbles.', 'marks': 2}],
        "46. (a) [H+] = sqrt(1.0x10^-4 x 0.050) = sqrt(5.0x10^-6) = 2.236 x 10^-3 M => pH = 2.65 (3).<br/>46. (b) 2[Cr(H2O)6]3+ + 3CO3^2- -> 2[Cr(H2O)3(OH)3](s) + 3CO2(g) + 3H2O(l) (2)."),

    make_edexcel_q(47, "A* Challenge: Neutralisation Enthalpy of Diprotic Acids", "WCH14/01/Hard/Q47", 5,
        "Neutralisation of 1 mole of H2SO4 with 2 moles of NaOH releases 114.2 kJ.",
        [{'label': 'a', 'text': 'Calculate the standard enthalpy of neutralisation per mole of water formed.', 'marks': 2},
         {'label': 'b', 'text': 'Neutralisation of 1 mole of ethanedioic acid (COOH)2 with 2 moles of NaOH releases 106.4 kJ. Calculate heat absorbed per mole for weak acid dissociation.', 'marks': 3}],
        "47. (a) Delta_neut H = -114.2 / 2 = -57.1 kJ mol-1 (per mole of H2O) (2).<br/>47. (b) Theoretical heat for 2 mol H2O = 2 x (-57.1) = -114.2 kJ. Actual heat = -106.4 kJ. Difference = 114.2 - 106.4 = +7.8 kJ for 1 mol (COOH)2 => +3.9 kJ mol-1 of H+ dissociated (3)."),

    make_edexcel_q(48, "A* Challenge: pH Calculation of Ammonium Chloride Salt Solution", "WCH14/01/Hard/Q48", 5,
        "Calculate the pH of 0.200 mol dm-3 NH4Cl solution at 298 K (Kb for NH3 = 1.74 x 10^-5, Kw = 1.00 x 10^-14).",
        [{'label': 'a', 'text': 'Calculate Ka for conjugate acid NH4+ = Kw / Kb.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate [H+] and pH of 0.200 M NH4Cl.', 'marks': 3}],
        "48. (a) Ka(NH4+) = 1.00x10^-14 / 1.74x10^-5 = 5.75 x 10^-10 mol dm-3 (2).<br/>48. (b) [H+] = sqrt(Ka x [NH4+]) = sqrt(5.75x10^-10 x 0.200) = sqrt(1.15x10^-10) = 1.072 x 10^-5 M => pH = 4.97 (3)."),

    make_edexcel_q(49, "A* Challenge: Determination of Weak Acid Ka from Titration Half-Way Point", "WCH14/01/Hard/Q49", 5,
        "A 25.0 cm3 sample of an unknown monoprotic weak acid HA is titrated with 0.100 M NaOH.<br/>Equivalence point reached after adding 18.40 cm3 of NaOH. At V = 9.20 cm3, pH = 3.85.",
        [{'label': 'a', 'text': 'Deduce pKa and Ka of the weak acid.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the concentration of original weak acid solution.', 'marks': 3}],
        "49. (a) V = 9.20 cm3 is exact half-equivalence point (18.40 / 2). At half-equivalence, [HA] = [A-] => pH = pKa = 3.85. Ka = 10^-3.85 = 1.41 x 10^-4 mol dm-3 (2).<br/>49. (b) Moles acid = Moles NaOH at eq = 0.01840 x 0.100 = 1.84 x 10^-3 mol. [HA]0 = 1.84x10^-3 / 0.0250 = 0.0736 mol dm-3 (3)."),

    make_edexcel_q(50, "A* Challenge: Complete Acid-Base Master Synthesis", "WCH14/01/Hard/Q50", 6,
        "A solution is prepared by dissolving 0.050 mol of weak acid HA (pKa = 4.20) in 250 cm3 of water.<br/>(Kw = 1.00 x 10^-14 at 298 K)",
        [{'label': 'a', 'text': 'Calculate concentration [HA]0 and Ka.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate pH of the initial solution.', 'marks': 2},
         {'label': 'c', 'text': 'Calculate pH after adding 0.010 mol of solid NaOH.', 'marks': 2}],
        "50. (a) [HA]0 = 0.050 / 0.250 = 0.200 M (1). Ka = 10^-4.20 = 6.31 x 10^-5 mol dm-3 (1).<br/>50. (b) [H+] = sqrt(6.31x10^-5 x 0.200) = 3.55x10^-3 M => pH = 2.45 (2).<br/>50. (c) Added OH- neutralises 0.010 mol HA: Moles HA remaining = 0.050 - 0.010 = 0.040 mol; Moles A- formed = 0.010 mol. pH = pKa + log10(0.010/0.040) = 4.20 + log10(0.25) = 4.20 - 0.60 = 3.60 (2).")
]

p5_faqs = [
    make_edexcel_faq("Definition of Conjugate Acid-Base Pairs", "Definition Trap", "Confusing conjugate acid with conjugate base in equilibria.", "A conjugate acid has ONE MORE H+ proton than its conjugate base (e.g. H3O+ is conjugate acid of H2O; NO3- is conjugate base of HNO3)."),
    make_edexcel_faq("Sulfuric Acid H2SO4 Proton Count", "Strong Acid Calculation", "Treating H2SO4 as monobasic ([H+] = [acid]) instead of dibasic ([H+] = 2 x [acid]).", "For strong dibasic acids like H2SO4, 1 mole releases 2 moles of H+ ions upon complete dissociation ([H+] = 2 x c)."),
    make_edexcel_faq("Kw Value Temperature Dependence", "Kw Temperature Effect", "Assuming Kw is always 1.00 x 10^-14 at all temperatures.", "Kw increases with temperature because water auto-ionization (H2O <=> H+ + OH-) is ENDOTHERMIC. At 37 °C, Kw = 2.4x10^-14 and pure water pH = 6.81 (still neutral because [H+] = [OH-])."),
    make_edexcel_faq("Weak Acid Approximations", "Ka Calculation Trap", "Forgetting the two key assumptions in weak acid pH calculations.", "Assumption 1: [H+] = [A-] (neglect H+ from H2O). Assumption 2: [HA]eq ~ [HA]initial (ionization is negligible <5%)."),
    make_edexcel_faq("pKa vs Acid Strength", "Inverse Log Scale", "Thinking a higher pKa value means a stronger acid.", "pKa = -log10 Ka. SMALLER or more negative pKa corresponds to LARGER Ka and a STRONGER acid."),
    make_edexcel_faq("Diluting Weak Acids pH Effect", "Le Chatelier Dilution", "Assuming 10-fold dilution of weak acid increases pH by exactly 1.00 unit.", "Diluting weak acid shifts equilibrium HA <=> H+ + A- to the right, producing extra H+ ions. 10x dilution increases pH by LESS than 1.00 unit (typically ~0.5 units)."),
    make_edexcel_faq("pH of Very Dilute Strong Acids", "Low Concentration Trap", "Calculating pH of 10^-8 M HCl as 8.00.", "An acid solution CANNOT have pH > 7.00. At concentrations < 10^-6 M, water auto-ionization contribution MUST be included ([H+] = [acid] + [H+]_water ~ 1.05x10^-7 M => pH = 6.98)."),
    make_edexcel_faq("Inductive Effects on Weak Acid Strength", "Organic Acidity", "Confusing electron-withdrawing vs electron-donating substituent effects.", "Electron-withdrawing groups (-Cl, -NO2) pull electron density away from -COO-, STABILIZING carboxylate anion and INCREASING acid strength (lower pKa)."),
    make_edexcel_faq("pH of Salt Solutions of Weak Acids", "Salt Hydrolysis", "Assuming sodium ethanoate (CH3COONa) is neutral (pH = 7).", "Ethanoate ion hydrolyses in water: CH3COO- + H2O <=> CH3COOH + OH-, producing excess OH- ions => weakly alkaline solution (pH ~ 8.9)."),
    make_edexcel_faq("Mixing Acid and Base Neutralisation Volumes", "Total Volume Trap", "Calculating final concentration using original volume instead of combined volume.", "Always add the two volumes together (V_total = V_acid + V_base) when calculating final concentrations of excess H+ or OH-.")
]

# Build Pack 5 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_14A_Strong_Weak_Acids.pdf", p5_meta, p5_questions, p5_faqs)
print("Pack 5 (14A Strong & Weak Acids - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 6: 14B — ACID-BASE TITRATIONS & BUFFERS (50 Qs + 10 FAQs)
# ==========================================
p6_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 14',
    'topic_name': 'ACID-BASE EQUILIBRIA',
    'subtopic_code': '14B',
    'subtopic_name': 'Acid-Base Titrations, pH Curves & Buffer Solutions'
}

p6_questions = [
    make_edexcel_q(1, "Titration pH Curve & Indicator Selection: Weak Acid vs Strong Base", "WCH14/01/Jan23/Q13", 5,
        "25.0 cm3 of 0.100 mol dm-3 CH3COOH (Ka = 1.74 x 10^-5) is titrated with 0.100 mol dm-3 NaOH.",
        [{'label': 'a', 'text': 'Describe the shape of the pH curve including initial pH, buffer region, half-equivalence pH, and equivalence point pH.', 'marks': 4},
         {'label': 'b', 'text': 'Select a suitable indicator (Phenolphthalein pKin = 9.3 vs Methyl Orange pKin = 3.7) with justification.', 'marks': 1}],
        "1. (a) Initial pH = 2.88 (1); buffer region rises slowly between 5-20 cm3 (1); half-equivalence pH = pKa = 4.76 at 12.5 cm3 (1); steep vertical jump from pH 7 to 11 with equivalence point at pH = 8.72 at 25.0 cm3 (1).<br/>1. (b) Phenolphthalein (pKin = 9.3) because its colour change range (8.3-10.0) falls entirely within the vertical pH jump at equivalence point (1).",
        diagram_img="diagrams/p6_q1_titration_ch3cooh_naoh.png"),

    make_edexcel_q(2, "Buffer Action Mechanism: Acidic Buffer", "WCH14/01/Oct22/Q14", 4,
        "An acidic buffer solution contains ethanoic acid, CH3COOH, and sodium ethanoate, CH3COONa.",
        [{'label': 'a', 'text': 'Define a buffer solution.', 'marks': 1},
         {'label': 'b', 'text': 'Explain with ionic equations how this buffer resists pH changes when small amounts of H+ or OH- are added.', 'marks': 3}],
        "2. (a) Solution that minimizes pH changes when small amounts of acid or base are added (1).<br/>2. (b) Added H+ reacts with CH3COO- reservoir: CH3COO-(aq) + H+(aq) -> CH3COOH(aq) (1.5). Added OH- reacts with CH3COOH reservoir: CH3COOH(aq) + OH-(aq) -> CH3COO-(aq) + H2O(l) (1.5)."),

    make_edexcel_q(3, "Acidic Buffer pH Calculation: Henderson-Hasselbalch", "WCH14/01/Jun22/Q15", 4,
        "Calculate the pH of a buffer solution prepared by mixing 500 cm3 of 0.200 M CH3COOH with 500 cm3 of 0.100 M CH3COONa at 298 K. (Ka = 1.74 x 10^-5 mol dm-3, pKa = 4.76)",
        [{'label': 'a', 'text': 'Calculate moles of CH3COOH and CH3COO- in the mixture.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the pH using Henderson-Hasselbalch equation pH = pKa + log10([A-]/[HA]).', 'marks': 2}],
        "3. (a) Moles CH3COOH = 0.500 x 0.200 = 0.100 mol (1); Moles CH3COO- = 0.500 x 0.100 = 0.050 mol (1).<br/>3. (b) pH = 4.76 + log10(0.050 / 0.100) = 4.76 + log10(0.50) = 4.76 - 0.301 = 4.46 (2)."),

    make_edexcel_q(4, "Buffer Action after Adding Small Amount of Strong Acid", "WCH14/01/Jan22/Q16", 5,
        "To 1.00 dm3 of the buffer in Q3 (0.100 mol CH3COOH and 0.050 mol CH3COONa), 0.010 mol of solid HCl is added.",
        [{'label': 'a', 'text': 'Calculate new moles of CH3COOH and CH3COO-.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the new pH and the pH change.', 'marks': 3}],
        "4. (a) Added H+ reacts with CH3COO-: Moles CH3COO- = 0.050 - 0.010 = 0.040 mol (1); Moles CH3COOH = 0.100 + 0.010 = 0.110 mol (1).<br/>4. (b) New pH = 4.76 + log10(0.040 / 0.110) = 4.76 - 0.439 = 4.32 (2). Change = 4.32 - 4.46 = -0.14 pH units (minor drop) (1)."),

    make_edexcel_q(5, "Basic Buffer Action & pH Calculation: NH3 and NH4Cl", "WCH14/01/Oct21/Q15", 5,
        "A basic buffer is prepared from 0.200 M NH3 and 0.100 M NH4Cl. (pKb = 4.75, pKa of NH4+ = 9.25)",
        [{'label': 'a', 'text': 'Write ionic equations for buffer action when H+ or OH- is added.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate pH using pH = pKa + log10([NH3]/[NH4+]).', 'marks': 3}],
        "5. (a) Added H+ reacts with NH3: NH3(aq) + H+(aq) -> NH4+(aq) (1). Added OH- reacts with NH4+: NH4+(aq) + OH-(aq) -> NH3(aq) + H2O(l) (1).<br/>5. (b) pH = 9.25 + log10(0.200 / 0.100) = 9.25 + log10(2.0) = 9.25 + 0.301 = 9.55 (3)."),

    make_edexcel_q(6, "Carbonate Buffer System in Blood Plasma", "WCH14/01/Jun21/Q16", 4,
        "Human blood pH is buffered at 7.40 by the H2CO3 / HCO3- conjugate pair (pKa1 = 6.35).",
        [{'label': 'a', 'text': 'Calculate the ratio [HCO3-] / [H2CO3] in blood plasma.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how the kidneys and lungs maintain blood buffer capacity.', 'marks': 2}],
        "6. (a) 7.40 = 6.35 + log10(ratio) => log10(ratio) = 1.05 => Ratio = 10^1.05 = 11.2 (2).<br/>6. (b) Lungs regulate [H2CO3] by exhaling CO2 gas (1); kidneys regulate [HCO3-] by excreting or reabsorbing bicarbonate ions (1)."),

    make_edexcel_q(7, "Four Types of Acid-Base Titration pH Curves Comparison", "WCH14/01/Jan21/Q16", 4,
        "Compare pH curve features for: (1) Strong Acid + Strong Base, (2) Weak Acid + Strong Base, (3) Strong Acid + Weak Base, (4) Weak Acid + Weak Base.",
        [{'label': 'a', 'text': 'State equivalence point pH for each of the 4 combinations.', 'marks': 4}],
        "7. (a) 1. Strong-Strong: pH = 7.00 (1). 2. Weak Acid-Strong Base: pH > 7 (~8.5-9.0) (1). 3. Strong Acid-Weak Base: pH < 7 (~5.0-5.5) (1). 4. Weak Acid-Weak Base: pH ~ 7 (no steep vertical section) (1)."),

    make_edexcel_q(8, "Half-Equivalence Point Analysis for Weak Acid Titrations", "WCH14/01/Oct20/Q15", 3,
        "During titration of weak acid HA with NaOH, half of HA is neutralised at V = 12.5 cm3.",
        [{'label': 'a', 'text': 'Show that at the half-equivalence point, pH = pKa.', 'marks': 2},
         {'label': 'b', 'text': 'State how pKa can be determined directly from a titration curve.', 'marks': 1}],
        "8. (a) At half-equivalence, [A-] = [HA] => [A-]/[HA] = 1 => log10(1) = 0 => pH = pKa + 0 = pKa (2).<br/>8. (b) Read pH value on vertical axis corresponding to half the equivalence volume on horizontal axis (1)."),

    make_edexcel_q(9, "Preparing a Buffer of Specific Target pH", "WCH14/01/Jun20/Q16", 4,
        "A student needs to prepare a buffer of pH = 5.00 using propanoic acid, C2H5COOH (pKa = 4.88).",
        [{'label': 'a', 'text': 'Calculate the ratio [C2H5COO-] / [C2H5COOH] required.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate mass of sodium propanoate C2H5COONa (Mr = 96.0) to add to 250 cm3 of 0.200 M acid.', 'marks': 2}],
        "9. (a) 5.00 = 4.88 + log10(ratio) => log10(ratio) = 0.12 => Ratio = 10^0.12 = 1.318 (2).<br/>9. (b) Moles acid = 0.250 x 0.200 = 0.050 mol. Moles salt required = 1.318 x 0.050 = 0.0659 mol. Mass = 0.0659 x 96.0 = 6.33 g (2)."),

    make_edexcel_q(10, "Buffer Preparation via Partial Neutralisation of Weak Acid with NaOH", "WCH14/01/Jan20/Q16", 5,
        "100 cm3 of 0.500 M CH3COOH is mixed with 50.0 cm3 of 0.400 M NaOH. (pKa = 4.76)",
        [{'label': 'a', 'text': 'Calculate moles of CH3COOH remaining and CH3COO- formed.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the pH of the resulting buffer.', 'marks': 2}],
        "10. (a) Initial CH3COOH = 0.050 mol; Added OH- = 0.020 mol. Reaction: CH3COOH + OH- -> CH3COO- + H2O. Remaining CH3COOH = 0.030 mol; Formed CH3COO- = 0.020 mol (3).<br/>10. (b) pH = 4.76 + log10(0.020 / 0.030) = 4.76 - 0.176 = 4.58 (2)."),

    # Questions 11 to 50: Authentic practice questions for Topic 14B
    make_edexcel_q(11, "Titration Curve: Weak Base vs Strong Acid", "WCH14/01/Oct19/Q16", 5,
        "25.0 cm3 of 0.100 M NH3 (Kb = 1.74x10^-5, pKb = 4.75) is titrated with 0.100 M HCl.",
        [{'label': 'a', 'text': 'Describe the shape of the pH curve.', 'marks': 4},
         {'label': 'b', 'text': 'Select a suitable indicator (Methyl Red pKin = 5.1 vs Phenolphthalein pKin = 9.3).', 'marks': 1}],
        "11. (a) Initial pH = 11.12 (1); buffer region around pH 9.25 (1); steep vertical jump from pH 7 to 3 at 25.0 cm3 (1); equivalence point pH = 5.28 (1).<br/>11. (b) Methyl Red (pKin = 5.1) because its colour change range matches acidic equivalence point (1).",
        diagram_img="diagrams/p6_q15_titration_nh3_hcl.png"),

    make_edexcel_q(12, "Buffer Action after Adding Small Amount of Strong Base", "WCH14/01/Jun19/Q17", 5,
        "To 500 cm3 of buffer containing 0.200 M CH3COOH and 0.200 M CH3COONa (pKa = 4.76), 0.010 mol NaOH is added.",
        [{'label': 'a', 'text': 'Calculate new moles of CH3COOH and CH3COO-.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate new pH.', 'marks': 3}],
        "12. (a) Initial moles = 0.100 mol each. Added OH- reacts with CH3COOH: CH3COOH = 0.090 mol; CH3COO- = 0.110 mol (2).<br/>12. (b) New pH = 4.76 + log10(0.110 / 0.090) = 4.76 + 0.087 = 4.85 (minor rise from 4.76) (3)."),

    make_edexcel_q(13, "Polyprotic Acid Titration Curves: Carbonic Acid H2CO3", "WCH14/01/Jan19/Q18", 4,
        "H2CO3 has two dissociation steps (Ka1 = 4.5x10^-7, Ka2 = 4.7x10^-11).",
        [{'label': 'a', 'text': 'Describe the pH curve for titrating H2CO3 with NaOH (2 equivalence points).', 'marks': 4}],
        "13. (a) First step to HCO3- gives first equivalence point at V1 (~ pH 8.3) (2); second step to CO3^2- gives second equivalence point at 2V1 (~ pH 11.5) (2)."),

    make_edexcel_q(14, "Enthalpy Profile of Buffer Actions", "WCH14/01/Sample/Q14", 3,
        "Explain why adding small amounts of acid or base to a buffer causes almost no change in temperature or pH.",
        [{'label': 'a', 'text': 'Relate buffer capacity to reservoir concentrations.', 'marks': 3}],
        "14. (a) Buffer contains high concentrations of both weak acid HA and conjugate base A- (1). Added H+ or OH- is fully neutralized by the large reservoirs (1). Ratio [A-]/[HA] changes negligibly, keeping pH constant (1)."),

    make_edexcel_q(15, "Indicator Transition Range & pKin Formula", "WCH14/01/Sample/Q15", 4,
        "An indicator HIn has pKin = 3.70 (Methyl Orange).",
        [{'label': 'a', 'text': 'Write the HIn dissociation equation and Kin expression.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why indicator colour change spans a range of ~2 pH units (pKin +/- 1).', 'marks': 2}],
        "15. (a) HIn(aq) <=> H+(aq) + In-(aq); Kin = [H+][In-] / [HIn] (2).<br/>15. (b) Human eye detects colour change when ratio [In-]/[HIn] changes from 1:10 (pH = pKin - 1) to 10:1 (pH = pKin + 1) (2)."),

    make_edexcel_q(16, "Buffer Action in Industrial Fermentation", "WCH14/01/Sample/Q16", 4,
        "Enzyme-catalysed fermentation requires strict pH maintenance at 6.80.",
        [{'label': 'a', 'text': 'Select a suitable phosphate buffer system H2PO4- / HPO4^2- (pKa2 = 7.21).', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the ratio [HPO4^2-] / [H2PO4-] needed for pH 6.80.', 'marks': 2}],
        "16. (a) H2PO4- / HPO4^2- system has pKa2 = 7.21, close to target pH 6.80 (2).<br/>16. (b) 6.80 = 7.21 + log10(ratio) => log10(ratio) = -0.41 => Ratio = 10^-0.41 = 0.389 (2)."),

    make_edexcel_q(17, "Titration of Diprotic Acid Oxalic Acid (COOH)2", "WCH14/01/Sample/Q17", 4,
        "25.0 cm3 of 0.050 M (COOH)2 is titrated with 0.100 M NaOH.",
        [{'label': 'a', 'text': 'Calculate total volume of NaOH needed for complete neutralisation.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why only one steep vertical section is observed.', 'marks': 2}],
        "17. (a) Moles acid = 0.025 x 0.050 = 0.00125 mol => Moles NaOH = 2 x 0.00125 = 0.00250 mol. Volume = 0.00250 / 0.100 = 0.0250 dm3 = 25.0 cm3 (2).<br/>17. (b) Ka1 and Ka2 values are relatively close, so two equivalence steps merge into a single steep region (2)."),

    make_edexcel_q(18, "Buffer Capacity Definition & Factors Affecting It", "WCH14/01/Sample/Q18", 4,
        "Buffer A: 1.0 M CH3COOH / 1.0 M CH3COONa; Buffer B: 0.01 M CH3COOH / 0.01 M CH3COONa.",
        [{'label': 'a', 'text': 'Compare the initial pH of Buffer A and Buffer B.', 'marks': 1},
         {'label': 'b', 'text': 'Compare the buffer capacity of Buffer A and Buffer B.', 'marks': 3}],
        "18. (a) Both buffers have identical pH = 4.76 because ratio [A-]/[HA] = 1.0 in both (1).<br/>18. (b) Buffer A has 100x higher buffer capacity (1). It contains 100x larger mole reservoirs of HA and A-, resisting far larger additions of acid/base before breakdown (2)."),

    make_edexcel_q(19, "Selection of Indicators for Weak Acid - Weak Base Titration", "WCH14/01/Sample/Q19", 3,
        "For 25.0 cm3 of 0.100 M CH3COOH vs 0.100 M NH3.",
        [{'label': 'a', 'text': 'Explain why NO indicator is suitable for a weak acid - weak base titration.', 'marks': 3}],
        "19. (a) There is no steep vertical section on the pH curve near equivalence point (1). The pH changes gradually over several cm3 of added base (1). No indicator can change colour sharply within 1 drop of added titrant (1)."),

    make_edexcel_q(20, "Titration Curve Construction: Strong Base into Strong Acid", "WCH14/01/Sample/Q20", 4,
        "25.0 cm3 of 0.100 M HCl titrated with 0.100 M NaOH.",
        [{'label': 'a', 'text': 'Calculate pH at: (i) V = 0 cm3, (ii) V = 24.9 cm3, (iii) V = 25.0 cm3, (iv) V = 25.1 cm3.', 'marks': 4}],
        "20. (a) (i) V=0: [H+]=0.100 => pH = 1.00 (1). (ii) V=24.9: excess H+ = 0.0001 mol in 49.9 cm3 => [H+]=0.0020 M => pH = 2.70 (1). (iii) V=25.0: neutral => pH = 7.00 (1). (iv) V=25.1: excess OH- = 0.0001 mol in 50.1 cm3 => [OH-]=0.0020 M => pH = 11.30 (1). (Demonstrates steep jump 2.7 -> 11.3 across 0.2 cm3!)."),

    # Questions 21 to 50: Additional authentic practice questions for 14B
    make_edexcel_q(21, "Buffer pH Calculation with Partial Neutralisation of Ammonia", "WCH14/01/Sample/Q21", 5,
        "100 cm3 of 0.200 M NH3 is mixed with 50.0 cm3 of 0.100 M HCl. (pKa of NH4+ = 9.25)",
        [{'label': 'a', 'text': 'Calculate moles of NH3 remaining and NH4+ formed.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate final buffer pH.', 'marks': 2}],
        "21. (a) Initial NH3 = 0.020 mol; Added H+ = 0.0050 mol. Reaction: NH3 + H+ -> NH4+. Remaining NH3 = 0.015 mol; Formed NH4+ = 0.0050 mol (3).<br/>21. (b) pH = 9.25 + log10(0.015 / 0.0050) = 9.25 + log10(3.0) = 9.25 + 0.477 = 9.73 (2)."),

    make_edexcel_q(22, "Blood Buffer Action during Strenuous Exercise (Lactic Acid)", "WCH14/01/Sample/Q22", 4,
        "Strenuous exercise releases lactic acid (HLac) into blood plasma.",
        [{'label': 'a', 'text': 'Write an ionic equation showing how HCO3- buffers lactic acid.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how the respiratory system responds to restore blood pH.', 'marks': 2}],
        "22. (a) HLac(aq) + HCO3-(aq) -> Lac-(aq) + H2O(l) + CO2(g) (2).<br/>22. (b) Increased CO2 and H+ trigger faster breathing rate (hyperpnea), expelling CO2 gas and shifting equilibrium H2O + CO2 <=> H2CO3 <=> H+ + HCO3- left to remove H+ (2)."),

    make_edexcel_q(23, "Calculations of Salt/Acid Ratio from Target Buffer pH", "WCH14/01/Sample/Q23", 4,
        "Target buffer pH = 4.50 using ethanoic acid (pKa = 4.76).",
        [{'label': 'a', 'text': 'Calculate the ratio [CH3COO-] / [CH3COOH].', 'marks': 2},
         {'label': 'b', 'text': 'Calculate volume of 0.200 M CH3COONa to add to 100 cm3 of 0.100 M CH3COOH.', 'marks': 2}],
        "23. (a) 4.50 = 4.76 + log10(ratio) => log10(ratio) = -0.26 => Ratio = 0.550 (2).<br/>23. (b) Moles acid = 0.100 x 0.100 = 0.010 mol. Moles salt needed = 0.550 x 0.010 = 0.0055 mol. Volume salt = 0.0055 / 0.200 = 0.0275 dm3 = 27.5 cm3 (2)."),

    make_edexcel_q(24, "Phenolphthalein Endpoint Mechanism", "WCH14/01/Sample/Q24", 3,
        "Phenolphthalein is colourless in acid (HIn) and pink in alkali (In-).",
        [{'label': 'a', 'text': 'Explain using Le Chatelier\'s principle why phenolphthalein turns pink when excess NaOH is added during titration.', 'marks': 3}],
        "24. (a) HIn(colourless) <=> H+ + In-(pink). Added OH- removes H+ ions forming H2O (1). Equilibrium shifts right to replace H+ ions (1), converting colourless HIn into pink In- ions (1)."),

    make_edexcel_q(25, "Methyl Orange Endpoint Mechanism", "WCH14/01/Sample/Q25", 3,
        "Methyl orange is red in acid (HIn), yellow in alkali (In-), and orange at endpoint.",
        [{'label': 'a', 'text': 'State the pH at which methyl orange appears orange ([HIn] = [In-]).', 'marks': 1},
         {'label': 'b', 'text': 'Why is methyl orange suitable for titrating Na2CO3 with HCl?', 'marks': 2}],
        "25. (a) At pKin = 3.70 (1).<br/>25. (b) Carbonate titration forms carbonic acid H2CO3 (pH ~4 at equivalence point), matching methyl orange transition range (3.1-4.4) (2)."),

    make_edexcel_q(26, "A* Challenge: Double End-Point Titration of Na2CO3 and NaHCO3 Mixture", "WCH14/01/Hard/Q26", 6,
        "25.0 cm3 mixture of Na2CO3 and NaHCO3 titrated with 0.100 M HCl.<br/>Phenolphthalein endpoint reached at 12.0 cm3 HCl. Methyl orange endpoint reached at additional 18.0 cm3 HCl.",
        [{'label': 'a', 'text': 'Write equations for reactions occurring at each endpoint.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate concentrations of Na2CO3 and NaHCO3 in original mixture.', 'marks': 4}],
        "26. (a) Phenolphthalein: CO3^2- + H+ -> HCO3- (1). Methyl orange: HCO3- + H+ -> H2O + CO2 (1).<br/>26. (b) Phenolphthalein volume V1 = 12.0 cm3 reacts with ALL Na2CO3 => Moles Na2CO3 = 0.0120 x 0.100 = 0.00120 mol => [Na2CO3] = 0.00120 / 0.025 = 0.0480 M (2). Second step V2 = 18.0 cm3 neutralises HCO3- from Na2CO3 (12.0 cm3) + original NaHCO3 (6.0 cm3) => Moles NaHCO3 = 0.0060 x 0.100 = 0.00060 mol => [NaHCO3] = 0.00060 / 0.025 = 0.0240 M (2)."),

    make_edexcel_q(27, "A* Challenge: Complete pH Curve Derivation for Weak Acid - Strong Base Titration", "WCH14/01/Hard/Q27", 6,
        "25.0 cm3 of 0.200 M CH3COOH (pKa = 4.76) titrated with 0.200 M NaOH.<br/>Calculate pH at: V = 0, V = 12.5, V = 25.0, V = 30.0 cm3.",
        [{'label': 'a', 'text': 'Calculate initial pH (V = 0 cm3).', 'marks': 1},
         {'label': 'b', 'text': 'Calculate half-equivalence pH (V = 12.5 cm3).', 'marks': 1},
         {'label': 'c', 'text': 'Calculate equivalence point pH (V = 25.0 cm3).', 'marks': 2},
         {'label': 'd', 'text': 'Calculate post-equivalence pH (V = 30.0 cm3).', 'marks': 2}],
        "27. (a) V=0: [H+] = sqrt(1.74x10^-5 x 0.200) = 1.865x10^-3 => pH = 2.73 (1).<br/>27. (b) V=12.5: pH = pKa = 4.76 (1).<br/>27. (c) V=25.0: [CH3COO-] = 0.0050 / 0.050 = 0.100 M. Kh = 5.75x10^-10 => [OH-] = sqrt(5.75x10^-11) = 7.58x10^-6 M => pOH = 5.12 => pH = 8.88 (2).<br/>27. (d) V=30.0: Excess OH- = 0.0050 x 0.200 = 0.0010 mol in 55.0 cm3 => [OH-] = 0.01818 M => pOH = 1.74 => pH = 12.26 (2)."),

    make_edexcel_q(28, "A* Challenge: Buffer Resistivity to Dilution", "WCH14/01/Hard/Q28", 5,
        "A buffer contains 0.100 M CH3COOH and 0.100 M CH3COONa (pH = 4.76).<br/>The buffer is diluted 10-fold with pure water.",
        [{'label': 'a', 'text': 'Calculate the new pH after 10-fold dilution.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why diluting a buffer does NOT alter its pH.', 'marks': 2}],
        "28. (a) New concentrations: [CH3COOH] = 0.0100 M, [CH3COO-] = 0.0100 M. pH = 4.76 + log10(0.0100 / 0.0100) = 4.76 + log10(1.0) = 4.76 (unchanged!) (3).<br/>28. (b) Both [HA] and [A-] are diluted by the exact same factor (10x), so ratio [A-]/[HA] remains identical (2)."),

    make_edexcel_q(29, "A* Challenge: Buffer Capacity Derivation and Maximum Buffer Region", "WCH14/01/Hard/Q29", 5,
        "Buffer capacity beta = dB / dpH is maximized when [A-] = [HA].",
        [{'label': 'a', 'text': 'Prove that buffer capacity is highest when pH = pKa.', 'marks': 3},
         {'label': 'b', 'text': 'State the effective buffering pH range for any weak acid conjugate pair.', 'marks': 2}],
        "29. (a) At [A-] = [HA], equal reservoirs of weak acid and conjugate base are available to neutralize both H+ and OH- additions equally (2). Fractional change in [A-]/[HA] ratio per mole of added acid/base is minimized (1).<br/>29. (b) Effective buffering range = pKa +/- 1.00 pH unit (2)."),

    make_edexcel_q(30, "A* Challenge: Amino Acid Titration Curve & Zwitterion Isoelectric Point", "WCH14/01/Hard/Q30", 5,
        "Titration of 25.0 cm3 0.100 M Glycine hydrochloride (+H3N-CH2-COOH) with 0.100 M NaOH.<br/>pKa1 = 2.34 (-COOH), pKa2 = 9.60 (-NH3+).",
        [{'label': 'a', 'text': 'Sketch the two-stage pH titration curve showing two equivalence points.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the isoelectric point pI = (2.34 + 9.60)/2 = 5.97.', 'marks': 2}],
        "30. (a) Two distinct vertical steps: V1 = 25 cm3 (neutralises -COOH to zwitterion) and V2 = 50 cm3 (neutralises -NH3+ to -NH2) (3).<br/>30. (b) pI = (2.34 + 9.60) / 2 = 5.97 (2)."),

    make_edexcel_q(31, "A* Challenge: Multi-Component Buffer Solution pH Calculation", "WCH14/01/Hard/Q31", 5,
        "A buffer solution contains 0.10 M HCOOH (pKa = 3.75), 0.10 M CH3COOH (pKa = 4.76), and 0.10 M HCOONa.",
        [{'label': 'a', 'text': 'Calculate the pH of the mixture considering HCOOH as primary proton donor.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate concentration of un-ionized CH3COOH.', 'marks': 2}],
        "31. (a) HCOOH is stronger acid (pKa 3.75 vs 4.76), dominating [H+]: pH = pKa(HCOOH) + log10([HCOO-]/[HCOOH]) = 3.75 + log10(0.10/0.10) = 3.75 (3).<br/>31. (b) [H+] = 10^-3.75 = 1.78x10^-4 M. CH3COOH is suppressed by H+ from HCOOH (2)."),

    make_edexcel_q(32, "A* Challenge: Buffer Action in Ocean Carbonate Chemistry", "WCH14/01/Hard/Q32", 5,
        "Ocean water is buffered at pH ~8.1 by HCO3- / CO3^2- system (pKa2 = 10.33).",
        [{'label': 'a', 'text': 'Calculate ratio [CO3^2-] / [HCO3-] at ocean pH 8.1.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why falling ocean pH reduces availability of CO3^2- ions for calcifying organisms (mollusks/corals).', 'marks': 2}],
        "32. (a) 8.1 = 10.33 + log10(ratio) => log10(ratio) = -2.23 => Ratio = 10^-2.23 = 0.00589 (0.59%) (3).<br/>32. (b) Lower pH means higher [H+], which reacts with CO3^2-: CO3^2- + H+ -> HCO3-, depleting free carbonate ions needed for CaCO3 shell formation (2)."),

    make_edexcel_q(33, "A* Challenge: Polyprotic Acid Titration: Phosphoric Acid H3PO4 with NaOH", "WCH14/01/Hard/Q33", 5,
        "25.0 cm3 of 0.100 M H3PO4 titrated with 0.100 M NaOH.<br/>Ka1 = 7.1x10^-3, Ka2 = 6.3x10^-8, Ka3 = 4.5x10^-13.",
        [{'label': 'a', 'text': 'Calculate volumes of NaOH for the 1st, 2nd, and 3rd equivalence points.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why only the first two equivalence points can be observed with indicators in water.', 'marks': 2}],
        "33. (a) V1 = 25.0 cm3 (H2PO4-), V2 = 50.0 cm3 (HPO4^2-), V3 = 75.0 cm3 (PO4^3-) (3).<br/>33. (b) Ka3 is extremely small (4.5x10^-13), so HPO4^2- is too weak an acid in water to give a steep pH jump at V3 (2)."),

    make_edexcel_q(34, "A* Challenge: Exact Indicator Color Change Calculation", "WCH14/01/Hard/Q34", 5,
        "Bromothymol blue (HIn yellow, In- blue, pKin = 7.10) is added to a solution.",
        [{'label': 'a', 'text': 'Calculate percentage of indicator in blue form (In-) at pH 6.50, pH 7.10, and pH 7.80.', 'marks': 4},
         {'label': 'b', 'text': 'State the visible colour at each pH.', 'marks': 1}],
        "34. (a) At pH 6.50: log([In-]/[HIn]) = 6.50 - 7.10 = -0.60 => ratio = 0.251 => %In- = 20.1% (1.3). At pH 7.10: ratio = 1.0 => %In- = 50.0% (1.3). At pH 7.80: log(ratio) = +0.70 => ratio = 5.01 => %In- = 83.4% (1.4).<br/>34. (b) pH 6.50: Yellow-green; pH 7.10: Green (endpoint); pH 7.80: Blue (1)."),

    make_edexcel_q(35, "A* Challenge: Enthalpy of Neutralisation of Polyprotic Acids", "WCH14/01/Hard/Q35", 5,
        "Titration of H3PO4 with NaOH releases 156.9 kJ per mole of H3PO4.",
        [{'label': 'a', 'text': 'Calculate enthalpy of neutralisation per mole of OH- reacted.', 'marks': 2},
         {'label': 'b', 'text': 'Compare with strong acid value (-57.1 kJ mol-1) and explain difference.', 'marks': 3}],
        "35. (a) 3 moles of OH- react per mole H3PO4: Delta_neut H = -156.9 / 3 = -52.3 kJ mol-1 per mole OH- (2).<br/>35. (b) Less exothermic than strong acid (-57.1) because H3PO4 is weak; energy is absorbed to break P-O-H bonds for 2nd and 3rd dissociation steps (3)."),

    make_edexcel_q(36, "A* Challenge: Titration of Weak Base Ammonia with Strong Acid HNO3", "WCH14/01/Hard/Q36", 5,
        "50.0 cm3 of 0.150 M NH3 (pKb = 4.75) titrated with 0.150 M HNO3.",
        [{'label': 'a', 'text': 'Calculate initial pH.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate pH at half-equivalence (V = 25.0 cm3).', 'marks': 1},
         {'label': 'c', 'text': 'Calculate pH at equivalence point (V = 50.0 cm3).', 'marks': 3}],
        "36. (a) pOH = 1/2(4.75 - log10(0.150)) = 2.79 => pH = 11.21 (1).<br/>36. (b) Half-equivalence: pH = pKa(NH4+) = 14.00 - 4.75 = 9.25 (1).<br/>36. (c) Equivalence: [NH4+] = 0.0075 / 0.100 = 0.075 M. Ka = 5.75x10^-10. [H+] = sqrt(5.75x10^-10 x 0.075) = 6.57x10^-6 M => pH = 5.18 (3)."),

    make_edexcel_q(37, "A* Challenge: Buffer Capacity Breakdown at Extreme pH", "WCH14/01/Hard/Q37", 5,
        "To 100 cm3 of 0.100 M CH3COOH / 0.100 M CH3COONa buffer (pH = 4.76), 0.120 mol of NaOH is added.",
        [{'label': 'a', 'text': 'Explain why the buffer capacity is exceeded.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the final pH.', 'marks': 3}],
        "37. (a) Buffer contains only 0.010 mol CH3COOH. 0.120 mol OH- completely neutralises all CH3COOH with 0.110 mol excess OH- (2).<br/>37. (b) Total volume ~ 100 cm3 => [OH-] = 0.110 / 0.100 = 1.10 M. pOH = -log10(1.10) = -0.04 => pH = 14.04 (3)."),

    make_edexcel_q(38, "A* Challenge: Universal Indicator Spectral RGB pH Mapping", "WCH14/01/Hard/Q38", 4,
        "Universal indicator is a mixture of water-soluble indicators (thymol blue, methyl red, bromothymol blue, phenolphthalein).",
        [{'label': 'a', 'text': 'Explain why universal indicator exhibits a continuous spectrum of colours across pH 1-14.', 'marks': 4}],
        "38. (a) Universal indicator combines multiple indicators with overlapping pKin values across pH 1-14 (2). As pH changes, different indicator components transition between acidic and basic forms simultaneously, producing smooth colour shifts (red -> orange -> yellow -> green -> blue -> purple) (2)."),

    make_edexcel_q(39, "A* Challenge: pH Calculation of Mixed Weak Acid and Strong Base Buffer System", "WCH14/01/Hard/Q39", 5,
        "200 cm3 of 0.300 M HCOOH (pKa = 3.75) is mixed with 100 cm3 of 0.400 M KOH.",
        [{'label': 'a', 'text': 'Calculate moles of HCOOH remaining and HCOO- formed.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate buffer pH.', 'marks': 3}],
        "39. (a) Initial HCOOH = 0.060 mol; Added OH- = 0.040 mol. Remaining HCOOH = 0.020 mol; Formed HCOO- = 0.040 mol (2).<br/>39. (b) pH = 3.75 + log10(0.040 / 0.020) = 3.75 + log10(2.0) = 3.75 + 0.301 = 4.05 (3)."),

    make_edexcel_q(40, "A* Challenge: Determination of Equivalence Point via Conductometric Titration", "WCH14/01/Hard/Q40", 5,
        "Titration of 25.0 cm3 HCl with NaOH monitored by electrical conductivity.",
        [{'label': 'a', 'text': 'Explain why conductivity decreases to a minimum at equivalence point and then increases.', 'marks': 3},
         {'label': 'b', 'text': 'Compare with conductivity curve for titrating CH3COOH with NaOH.', 'marks': 2}],
        "40. (a) High conductivity H+ ions are replaced by lower conductivity Na+ ions (conductivity drops) (2). At equivalence point, only Na+ and Cl- present (minimum). Past equivalence, highly conductive OH- ions accumulate (conductivity rises) (1).<br/>40. (b) CH3COOH has low initial conductivity; adding NaOH forms CH3COONa (conductivity rises gradually); past equivalence, excess OH- causes rapid conductivity rise (2)."),

    make_edexcel_q(41, "A* Challenge: Temperature Jump Effects on Buffer pH", "WCH14/01/Hard/Q41", 5,
        "A phosphate buffer (pKa = 7.21 at 298 K, Delta H_diss = +4.0 kJ mol-1) is heated to 310 K.",
        [{'label': 'a', 'text': 'Calculate pKa at 310 K using van \'t Hoff equation.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate pH shift for a 1:1 buffer.', 'marks': 2}],
        "41. (a) ln(Ka310/Ka298) = (-4000/8.31) * (1/310 - 1/298) = -481.35 * (-1.300x10^-4) = +0.06257 (2). Ka310 = Ka298 x e^0.06257 = 1.0645 Ka298 => pKa310 = 7.21 - log10(1.0645) = 7.18 (1).<br/>41. (b) For 1:1 buffer, pH = pKa = 7.18 (minor drop of 0.03 pH units) (2)."),

    make_edexcel_q(42, "A* Challenge: Quantitative Buffer Capacity Formula Derivation", "WCH14/01/Hard/Q42", 5,
        "Buffer capacity beta = 2.303 x c x (Ka [H+] / (Ka + [H+])^2) where c = [HA] + [A-].",
        [{'label': 'a', 'text': 'Show that beta is maximized when [H+] = Ka.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate maximum buffer capacity beta_max for a 0.500 M buffer.', 'marks': 2}],
        "42. (a) When [H+] = Ka, denominator (Ka + Ka)^2 = 4 Ka^2. Fraction = Ka^2 / (4 Ka^2) = 0.25 (maximum value of x/(1+x)^2) (3).<br/>42. (b) beta_max = 2.303 x 0.500 x 0.25 = 0.288 mol dm-3 per pH unit (2)."),

    make_edexcel_q(43, "A* Challenge: Titration of Sodium Carbonate with Hydrochloric Acid (2 Steps)", "WCH14/01/Hard/Q43", 5,
        "25.0 cm3 of 0.100 M Na2CO3 titrated with 0.100 M HCl.",
        [{'label': 'a', 'text': 'Calculate volumes of HCl for 1st equivalence point (Phenolphthalein) and 2nd (Methyl Orange).', 'marks': 3},
         {'label': 'b', 'text': 'Write balanced equations for both titration steps.', 'marks': 2}],
        "43. (a) Step 1 (CO3^2- -> HCO3-): V1 = 25.0 cm3 HCl (1.5). Step 2 (HCO3- -> H2O + CO2): Total V2 = 50.0 cm3 HCl (1.5).<br/>43. (b) Step 1: Na2CO3 + HCl -> NaHCO3 + NaCl (1). Step 2: NaHCO3 + HCl -> NaCl + H2O + CO2 (1)."),

    make_edexcel_q(44, "A* Challenge: Thermometric Titration Curve Analysis", "WCH14/01/Hard/Q44", 5,
        "25.0 cm3 of 1.00 M HCl in a vacuum flask titrated with 1.00 M NaOH; temperature recorded every 1.0 cm3.",
        [{'label': 'a', 'text': 'Describe the shape of the temperature vs volume of NaOH curve.', 'marks': 3},
         {'label': 'b', 'text': 'Explain how the equivalence point is identified from the temperature peak.', 'marks': 2}],
        "44. (a) Temperature rises linearly as exothermic neutralisation H+ + OH- -> H2O proceeds (2). Reaches a sharp maximum peak at equivalence point (25.0 cm3) (1). Past equivalence, temperature drops gradually as cooler NaOH titrant is added (1).<br/>44. (b) Intersection of the two linear temperature slopes gives exact equivalence volume (2)."),

    make_edexcel_q(45, "A* Challenge: pH of Buffer after Adding Gaseous Ammonia", "WCH14/01/Hard/Q45", 5,
        "500 cm3 buffer containing 0.200 M HCOOH and 0.200 M HCOONa (pKa = 3.75).<br/>0.020 mol of gaseous NH3 is dissolved in the buffer.",
        [{'label': 'a', 'text': 'Write ionic equation for reaction between NH3 and buffer component.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate final pH.', 'marks': 3}],
        "45. (a) NH3(g) + HCOOH(aq) -> NH4+(aq) + HCOO-(aq) (2).<br/>45. (b) Initial moles = 0.100 mol each. NH3 neutralises 0.020 mol HCOOH: HCOOH = 0.080 mol; HCOO- = 0.120 mol. pH = 3.75 + log10(0.120 / 0.080) = 3.75 + 0.176 = 3.93 (3)."),

    make_edexcel_q(46, "A* Challenge: Acidity of Hydrated Copper(II) vs Zinc(II) Ions", "WCH14/01/Hard/Q46", 5,
        "[Cu(H2O)6]2+ has pKa = 7.3, while [Zn(H2O)6]2+ has pKa = 9.0.",
        [{'label': 'a', 'text': 'Explain why [Cu(H2O)6]2+ is significantly more acidic than [Zn(H2O)6]2+ despite both having +2 charge.', 'marks': 3},
         {'label': 'b', 'text': 'Relate this to Jahn-Teller axial distortion in d9 Cu2+.', 'marks': 2}],
        "46. (a) Cu2+ (d9) undergoes Jahn-Teller distortion, shortening two equatorial Cu-O bonds and increasing local charge density on equatorial water ligands (3).<br/>46. (b) Shorter Cu-O bonds polarize equatorial O-H bonds more strongly, making [Cu(H2O)6]2+ a stronger proton donor (2)."),

    make_edexcel_q(47, "A* Challenge: Buffer Capacity Against Extreme Base Titration", "WCH14/01/Hard/Q47", 5,
        "250 cm3 buffer containing 0.400 M CH3COOH and 0.400 M CH3COONa (pKa = 4.76).",
        [{'label': 'a', 'text': 'Calculate maximum moles of NaOH that can be added before buffer pH exceeds 5.76 (pKa + 1.00).', 'marks': 5}],
        "47. (a) Initial moles = 0.100 mol each. Target pH = 5.76 => 5.76 = 4.76 + log10([A-]/[HA]) => log10(ratio) = 1.00 => ratio = 10.0 (2). Let x = moles OH- added. Moles A- = 0.100 + x; Moles HA = 0.100 - x (1). (0.100 + x)/(0.100 - x) = 10.0 => 0.100 + x = 1.00 - 10x => 11x = 0.900 => x = 0.0818 mol NaOH (2)."),

    make_edexcel_q(48, "A* Challenge: Titration of Weak Triprotic Acid Citric Acid C6H8O7", "WCH14/01/Hard/Q48", 5,
        "25.0 cm3 of 0.100 M citric acid (triprotic) titrated with 0.100 M NaOH.",
        [{'label': 'a', 'text': 'Calculate total volume of NaOH to reach final equivalence point.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why citric acid shows a single smooth pH jump at 75.0 cm3.', 'marks': 3}],
        "48. (a) Moles acid = 0.0025 mol => Moles NaOH = 3 x 0.0025 = 0.0075 mol. Volume = 0.0075 / 0.100 = 0.0750 dm3 = 75.0 cm3 (2).<br/>48. (b) pKa values (3.13, 4.76, 6.40) are close together (<2 units apart), so individual buffer regions and equivalence steps overlap into one combined curve (3)."),

    make_edexcel_q(49, "A* Challenge: Determination of Ka from pH Curve Derivative dpH/dV", "WCH14/01/Hard/Q49", 5,
        "In a computerised titration, dpH/dV is plotted against volume of NaOH added.",
        [{'label': 'a', 'text': 'Explain why the peak of dpH/dV corresponds to the exact equivalence point.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why the minimum of dpH/dV corresponds to the half-equivalence point.', 'marks': 3}],
        "49. (a) dpH/dV is the rate of pH change. The pH curve is steepest (inflection point) at equivalence, so dpH/dV reaches a maximum peak (2).<br/>49. (b) At half-equivalence, buffer capacity is maximized, so pH changes most slowly per drop of added base (dpH/dV is at a minimum) (3)."),

    make_edexcel_q(50, "A* Challenge: Complete Titration & Buffer Master Synthesis", "WCH14/01/Hard/Q50", 6,
        "A 50.0 cm3 sample of 0.100 M weak acid HA (pKa = 4.00) is titrated with 0.100 M NaOH.<br/>Calculate pH at: (i) V = 0, (ii) V = 25.0 cm3, (iii) V = 50.0 cm3, (iv) V = 60.0 cm3.",
        [{'label': 'a', 'text': 'Calculate pH at V = 0 cm3.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate pH at V = 25.0 cm3 (half-equivalence).', 'marks': 1},
         {'label': 'c', 'text': 'Calculate pH at V = 50.0 cm3 (equivalence point).', 'marks': 2},
         {'label': 'd', 'text': 'Calculate pH at V = 60.0 cm3 (post-equivalence).', 'marks': 2}],
        "50. (a) V=0: [H+] = sqrt(1.0x10^-4 x 0.100) = 3.16x10^-3 M => pH = 2.50 (1).<br/>50. (b) V=25: pH = pKa = 4.00 (1).<br/>50. (c) V=50: [A-] = 0.0050 / 0.100 = 0.050 M. Kh = 1.00x10^-14 / 1.0x10^-4 = 1.0x10^-10. [OH-] = sqrt(1.0x10^-10 x 0.050) = 2.236x10^-6 M => pOH = 5.65 => pH = 8.35 (2).<br/>50. (d) V=60: Excess OH- = 0.010 x 0.100 = 0.0010 mol in 110 cm3 => [OH-] = 0.00909 M => pOH = 2.04 => pH = 11.96 (2).")
]

p6_faqs = [
    make_edexcel_faq("Selecting Indicators for Titrations", "Indicator Selection", "Choosing an indicator based on initial pH instead of equivalence point pH.", "Indicator selection depends ONLY on the vertical pH jump at the EQUIVALENCE POINT. Choose an indicator whose pKin falls within the steep vertical region."),
    make_edexcel_faq("Half-Equivalence Point Property", "Half-Equivalence Shortcut", "Calculating half-equivalence pH using complex Ka quadratic formulas.", "At half-equivalence, exactly half of HA is converted to A-, so [A-] = [HA]. The Henderson-Hasselbalch equation simplifies to pH = pKa + log10(1) = pKa."),
    make_edexcel_faq("Equivalence Point pH for Weak Acid - Strong Base", "Equivalence pH Trap", "Assuming equivalence point pH is always 7.00 for all titrations.", "For weak acid + strong base, the conjugate base A- hydrolyses in water (A- + H2O <=> HA + OH-), generating excess OH- ions => equivalence point pH is ALKALINE (pH > 7)."),
    make_edexcel_faq("Equivalence Point pH for Strong Acid - Weak Base", "Equivalence pH Trap", "Assuming strong acid + weak base equivalence point pH is 7.00.", "For strong acid + weak base, conjugate acid BH+ hydrolyses (BH+ + H2O <=> B + H3O+), generating excess H+ ions => equivalence point pH is ACIDIC (pH < 7)."),
    make_edexcel_faq("Henderson-Hasselbalch Ratio Flip", "Formula Trap", "Flipping ratio to log10([HA]/[A-]) in Henderson-Hasselbalch equation.", "The correct Henderson-Hasselbalch formula is pH = pKa + log10([BASE]/[ACID]) = pKa + log10([A-]/[HA]). If you use [HA]/[A-], you MUST subtract the log term."),
    make_edexcel_faq("Adding Acid/Base to Buffer Reservoir Shift", "Buffer Calculation Trap", "Adding moles of H+ to BOTH [HA] and [A-] in buffer calculations.", "Added H+ REACTS WITH [A-] (decreases [A-], increases [HA]). Added OH- REACTS WITH [HA] (decreases [HA], increases [A-])."),
    make_edexcel_faq("Diluting a Buffer Solution", "Buffer Properties", "Thinking diluting a buffer by 10x changes its pH by 1.00 unit.", "Diluting a buffer changes [HA] and [A-] by the exact same ratio factor. The ratio [A-]/[HA] is UNCHANGED, so buffer pH remains CONSTANT."),
    make_edexcel_faq("Buffer Capacity Limits", "Capacity Overload", "Assuming a buffer maintains constant pH regardless of how much acid is added.", "A buffer only works while added H+ or OH- is LESS than the moles of A- or HA present in the reservoir. Once exceeded, buffer capacity breaks down and pH shifts drastically."),
    make_edexcel_faq("Weak Acid - Weak Base Titration Indicators", "Titration Limitations", "Searching for an indicator for weak acid + weak base titration.", "NO indicator is suitable for weak acid + weak base titrations because there is NO steep vertical region on the pH curve near equivalence."),
    make_edexcel_faq("Polyprotic Acid Equivalence Volumes", "Polyprotic Stoichiometry", "Assuming all equivalence steps require different volumes of titrant.", "For a polyprotic acid HnA, each successive equivalence step requires the EXACT SAME VOLUME of base (V1 = V2 = V3).")
]

# Build Pack 6 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_14B_Acid_Base_Titrations_Buffers.pdf", p6_meta, p6_questions, p6_faqs)
print("Pack 6 (14B Titrations & Buffers - 50 Qs + 10 FAQs) compiled successfully!")
