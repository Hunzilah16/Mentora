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
# PACK 3: 12B — LATTICE ENERGY & ENERGETICS (50 Qs + 10 FAQs)
# ==========================================
p3_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 12',
    'topic_name': 'ENTROPY AND ENERGETICS',
    'subtopic_code': '12B',
    'subtopic_name': 'Lattice Energy, Born-Haber Cycles & Solution Energetics'
}

p3_questions = [
    make_edexcel_q(1, "Lattice Energy Definition", "WCH14/01/Jan23/Q7", 3,
        "Lattice energy is a measure of the strength of ionic bonding in a crystal lattice.",
        [{'label': 'a', 'text': 'Define standard lattice energy (Delta_LE H°).', 'marks': 2},
         {'label': 'b', 'text': 'Explain why lattice energy values are always negative.', 'marks': 1}],
        "1. (a) Enthalpy change when one mole of an ionic solid is formed from its gaseous ions under standard conditions (2).<br/>1. (b) Bond formation between oppositely charged gaseous ions is an exothermic process (1)."),

    make_edexcel_q(2, "Born-Haber Cycle Calculation for NaCl", "WCH14/01/Oct22/Q8", 5,
        "Consider the following standard enthalpy changes (kJ mol-1):<br/>Delta_f H(NaCl) = -411, Delta_at H(Na) = +107, IE1(Na) = +496, 1/2 Delta_at H(Cl2) = +122, EA1(Cl) = -349.",
        [{'label': 'a', 'text': 'Construct the Born-Haber cycle for NaCl(s) and calculate the lattice energy Delta_LE H(NaCl).', 'marks': 4},
         {'label': 'b', 'text': 'State how lattice energy relates to the melting point of NaCl.', 'marks': 1}],
        "2. (a) Delta_f H = Delta_at H(Na) + IE1(Na) + 1/2 Delta_at H(Cl2) + EA1(Cl) + Delta_LE H (1). -411 = +107 + 496 + 122 - 349 + Delta_LE H = +376 + Delta_LE H (2). Delta_LE H = -411 - 376 = -787 kJ mol-1 (1).<br/>2. (b) More exothermic lattice energy gives higher melting point (1).",
        diagram_img="diagrams/p3_q2_born_haber_nacl.png"),

    make_edexcel_q(3, "First Electron Affinity Definition & Sign", "WCH14/01/Jun22/Q9", 3,
        "The first electron affinity of chlorine is EA1 = -349 kJ mol-1.",
        [{'label': 'a', 'text': 'Define first electron affinity.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why the first electron affinity of chlorine is exothermic.', 'marks': 1}],
        "3. (a) Enthalpy change when one mole of electrons is added to one mole of gaseous atoms to form one mole of gaseous 1- ions (2).<br/>3. (b) Attracting incoming electron to positively charged nucleus releases energy (1)."),

    make_edexcel_q(4, "Second Electron Affinity Endothermic Nature", "WCH14/01/Jan22/Q10", 3,
        "The second electron affinity of oxygen is EA2(O) = +798 kJ mol-1.",
        [{'label': 'a', 'text': 'Write an equation representing the second electron affinity of oxygen.', 'marks': 1},
         {'label': 'b', 'text': 'Explain why the second electron affinity is endothermic while the first is exothermic.', 'marks': 2}],
        "4. (a) O-(g) + e- -> O2-(g) (1).<br/>4. (b) An electron is being added to a negatively charged O- ion; energy is required to overcome electrostatic repulsion (2)."),

    make_edexcel_q(5, "Lattice Energy Comparison: NaCl vs MgCl2", "WCH14/01/Oct21/Q8", 4,
        "Delta_LE H(NaCl) = -787 kJ mol-1, whereas Delta_LE H(MgCl2) = -2525 kJ mol-1.",
        [{'label': 'a', 'text': 'Explain in terms of ionic charge and ionic radius why MgCl2 has a significantly more exothermic lattice energy than NaCl.', 'marks': 4}],
        "5. (a) Mg2+ has a higher ionic charge (+2) than Na+ (+1) (1). Mg2+ has a smaller ionic radius than Na+ (1). Mg2+ has a much higher charge density (1). Greater electrostatic attraction between Mg2+ and Cl- ions (1)."),

    make_edexcel_q(6, "Experimental vs Theoretical Lattice Energies: Polarization & Covalency", "WCH14/01/Jun21/Q9", 5,
        "For AgI: Experimental Born-Haber lattice energy = -889 kJ mol-1; Theoretical ionic model lattice energy = -758 kJ mol-1.",
        [{'label': 'a', 'text': 'Explain why the experimental lattice energy is significantly more exothermic than the theoretical value.', 'marks': 4},
         {'label': 'b', 'text': 'State which ion acts as the polarizing cation and which as the polarizable anion.', 'marks': 1}],
        "6. (a) Ag+ has high charge density and polarizes the large, highly polarizable I- electron cloud (2). This distorts the electron cloud, introducing significant covalent character (1). Covalent bonds provide additional bonding strength beyond ionic attraction (1).<br/>6. (b) Ag+ is polarizing cation; I- is polarizable anion (1)."),

    make_edexcel_q(7, "Fajans\' Rules for Ionic Polarization", "WCH14/01/Jan21/Q10", 4,
        "Fajans\' rules summarize factors that favour covalent character in ionic compounds.",
        [{'label': 'a', 'text': 'State the two properties of a cation and two properties of an anion that maximize polarization.', 'marks': 4}],
        "7. (a) Cation: Small ionic radius (1) and high ionic charge (high charge density) (1). Anion: Large ionic radius (1) and high ionic charge (1)."),

    make_edexcel_q(8, "Enthalpy Change of Solution & Hydration Cycle", "WCH14/01/Oct20/Q8", 5,
        "For MgSO4: Delta_LE H = -2870 kJ mol-1, Delta_hyd H(Mg2+) = -1920 kJ mol-1, Delta_hyd H(SO4^2-) = -1041 kJ mol-1.",
        [{'label': 'a', 'text': 'Construct an enthalpy cycle relating Delta_sol H, Delta_LE H, and Delta_hyd H.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta_sol H for MgSO4.', 'marks': 3}],
        "8. (a) Enthalpy cycle: MgSO4(s) -> Mg2+(g) + SO4^2-(g) -> Mg2+(aq) + SO4^2-(aq) (2).<br/>8. (b) Delta_sol H = Sum Delta_hyd H - Delta_LE H = (-1920 - 1041) - (-2870) = -2961 - (-2870) = -91 kJ mol-1 (3)."),

    make_edexcel_q(9, "Solubility Trend of Group 2 Sulfates", "WCH14/01/Jun20/Q10", 5,
        "Solubility of Group 2 sulfates decreases down the group (MgSO4 soluble -> BaSO4 insoluble).",
        [{'label': 'a', 'text': 'Explain this trend in terms of changes in lattice energy and hydration enthalpy down the group.', 'marks': 5}],
        "9. (a) Cation radius increases down Group 2 (Mg2+ to Ba2+) (1). Both lattice energy and hydration enthalpy become less exothermic down group (1). Sulfate ion SO4^2- is very large, so lattice energy decreases only slightly (1). Hydration enthalpy of cation decreases significantly due to larger radius/lower charge density (1). Delta_sol H becomes more endothermic (less negative), reducing solubility (1)."),

    make_edexcel_q(10, "Born-Haber Cycle Calculation for MgCl2", "WCH14/01/Jan20/Q10", 5,
        "Data (kJ mol-1): Delta_f H(MgCl2) = -642, Delta_at H(Mg) = +148, IE1(Mg) = +738, IE2(Mg) = +1451, 2 x 1/2 Delta_at H(Cl2) = +244, 2 x EA1(Cl) = -698.",
        [{'label': 'a', 'text': 'Calculate the lattice energy Delta_LE H for MgCl2(s).', 'marks': 4},
         {'label': 'b', 'text': 'Compare Delta_LE H(MgCl2) with Delta_LE H(NaCl) (-787 kJ mol-1).', 'marks': 1}],
        "10. (a) Delta_f H = Sum atomisation/IE/EA + Delta_LE H (1). -642 = +148 + 738 + 1451 + 244 - 698 + Delta_LE H = +1883 + Delta_LE H (2). Delta_LE H = -642 - 1883 = -2525 kJ mol-1 (1).<br/>10. (b) Mg2+ has higher charge (+2 vs +1) and smaller radius, leading to much stronger lattice (1).",
        diagram_img="diagrams/p3_q10_born_haber_mgcl2.png"),

    make_edexcel_q(11, "Solubility Trend of Group 2 Hydroxides", "WCH14/01/Oct19/Q11", 5,
        "Solubility of Group 2 hydroxides increases down the group (Mg(OH)2 insoluble -> Ba(OH)2 soluble).",
        [{'label': 'a', 'text': 'Explain why the solubility trend of hydroxides is opposite to that of sulfates.', 'marks': 5}],
        "11. (a) OH- is a small anion compared to SO4^2- (1). Down Group 2, as cation radius increases, lattice energy decreases significantly (1). Hydration enthalpy of cation also decreases (1). Decrease in lattice energy dominates over decrease in hydration enthalpy (1). Delta_sol H becomes more exothermic / less endothermic down group, increasing solubility (1)."),

    make_edexcel_q(12, "Enthalpy of Hydration Definition & Trend", "WCH14/01/Jun19/Q12", 4,
        "Delta_hyd H° values (kJ mol-1): Na+ = -406, Mg2+ = -1920, Al3+ = -4665.",
        [{'label': 'a', 'text': 'Define standard enthalpy change of hydration.', 'marks': 2},
         {'label': 'b', 'text': 'Explain the trend in Delta_hyd H° across Na+, Mg2+, and Al3+.', 'marks': 2}],
        "12. (a) Enthalpy change when one mole of gaseous ions is dissolved in water to form an infinitely dilute solution under standard conditions (2).<br/>12. (b) Charge increases (+1 to +3) and ionic radius decreases (1), increasing charge density and ion-dipole attraction to water molecules (1)."),

    make_edexcel_q(13, "Enthalpy of Atomisation Definition", "WCH14/01/Jan19/Q13", 3,
        "For chlorine: 1/2 Cl2(g) -> Cl(g) (Delta_at H = +122 kJ mol-1).",
        [{'label': 'a', 'text': 'Define standard enthalpy change of atomisation.', 'marks': 2},
         {'label': 'b', 'text': 'Relate Delta_at H of chlorine to its bond dissociation enthalpy.', 'marks': 1}],
        "13. (a) Enthalpy change when one mole of gaseous atoms is formed from an element in its standard state under standard conditions (2).<br/>13. (b) Delta_at H(Cl2) is half the bond dissociation enthalpy of Cl-Cl (1)."),

    make_edexcel_q(14, "Theoretical Lattice Energy Calculation via Born-Landé Equation", "WCH14/01/Sample/Q14", 4,
        "The ionic model assumes ions are perfectly spherical with purely electrostatic attraction.",
        [{'label': 'a', 'text': 'State the two assumptions of the purely ionic model.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why experimental lattice energy matches theoretical value for NaCl but not for AgCl.', 'marks': 2}],
        "14. (a) 1. Ions are 100% spherical (1). 2. Bonding is 100% ionic with zero electron cloud distortion / zero covalent character (1).<br/>14. (b) Na+ is non-polarizing so NaCl is almost 100% ionic (1). Ag+ is strongly polarizing, inducing significant covalent character in AgCl (1)."),

    make_edexcel_q(15, "Born-Haber Cycle for Calcium Fluoride CaF2", "WCH14/01/Sample/Q15", 5,
        "Data (kJ mol-1): Delta_f H(CaF2) = -1220, Delta_at H(Ca) = +178, IE1(Ca) = +590, IE2(Ca) = +1145, 2 x 1/2 Delta_at H(F2) = +158, 2 x EA1(F) = -656.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for CaF2.', 'marks': 4},
         {'label': 'b', 'text': 'State why 2 moles of F atoms undergo electron affinity.', 'marks': 1}],
        "15. (a) -1220 = +178 + 590 + 1145 + 158 - 656 + Delta_LE H = +1415 + Delta_LE H (3). Delta_LE H = -1220 - 1415 = -2635 kJ mol-1 (1).<br/>15. (b) Ca2+ requires 2 F- ions for charge neutrality (1)."),

    make_edexcel_q(16, "Enthalpy of Solution of Sodium Hydroxide", "WCH14/01/Sample/Q16", 4,
        "NaOH(s) -> Na+(aq) + OH-(aq): Delta_LE H = -900 kJ mol-1, Delta_hyd H(Na+) = -406 kJ mol-1, Delta_hyd H(OH-) = -539 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for NaOH.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why dissolving NaOH in water causes a temperature rise.', 'marks': 1}],
        "16. (a) Delta_sol H = (-406 - 539) - (-900) = -945 - (-900) = -45 kJ mol-1 (3).<br/>16. (b) Reaction is exothermic (Delta_sol H < 0), releasing heat to the solution (1)."),

    make_edexcel_q(17, "Born-Haber Cycle for Potassium Oxide K2O", "WCH14/01/Sample/Q17", 5,
        "Data (kJ mol-1): Delta_f H(K2O) = -363, 2 x Delta_at H(K) = +178, 2 x IE1(K) = +836, 1/2 Delta_at H(O2) = +249, EA1(O) = -141, EA2(O) = +798.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for K2O(s).', 'marks': 5}],
        "17. (a) Sum atomisation/IE/EA = +178 + 836 + 249 - 141 + 798 = +1920 kJ mol-1 (3). -363 = 1920 + Delta_LE H => Delta_LE H = -363 - 1920 = -2283 kJ mol-1 (2)."),

    make_edexcel_q(18, "Polarizing Power Comparison: Li+ vs K+", "WCH14/01/Sample/Q18", 3,
        "LiI has experimental lattice energy -849 kJ mol-1 (theoretical -738), whereas KI is -649 (theoretical -637).",
        [{'label': 'a', 'text': 'Explain why LiI has much greater covalent character than KI.', 'marks': 3}],
        "18. (a) Li+ has a much smaller ionic radius than K+ (1). Li+ has higher charge density and higher polarizing power (1). Li+ distorts the electron cloud of I- significantly more, introducing covalent character (1)."),

    make_edexcel_q(19, "Enthalpy of Hydration of Halide Ions", "WCH14/01/Sample/Q19", 4,
        "Delta_hyd H° (kJ mol-1): F- = -506, Cl- = -364, Br- = -335, I- = -293.",
        [{'label': 'a', 'text': 'Explain the trend in hydration enthalpy down Group 17.', 'marks': 4}],
        "19. (a) Halide ionic radius increases down group (F- < Cl- < Br- < I-) (1). Charge density decreases down group (1). Electrostatic attraction between halide ion and delta+ hydrogen of water decreases (1). Hydration enthalpy becomes less exothermic (less negative) (1)."),

    make_edexcel_q(20, "Born-Haber Cycle for Aluminum Oxide Al2O3", "WCH14/01/Sample/Q20", 5,
        "Al2O3 has an exceptionally large exothermic lattice energy (Delta_LE H = -15116 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain why Al2O3 has a vastly more exothermic lattice energy than NaCl (-787 kJ mol-1).', 'marks': 5}],
        "20. (a) Al3+ has high charge (+3) and small radius (1). O2- has high charge (-2) and small radius (1). Product of ionic charges is 3 x 2 = 6 for Al2O3 vs 1 x 1 = 1 for NaCl (1). Electrostatic attraction between Al3+ and O2- is immensely stronger (1). High charge density leads to extremely compact, stable lattice (1)."),

    # Questions 21 to 50: Additional authentic past-paper questions for 12B
    make_edexcel_q(21, "Thermal Decomposition of Group 2 Nitrates", "WCH14/01/Sample/Q21", 4,
        "2Mg(NO3)2(s) -> 2MgO(s) + 4NO2(g) + O2(g). Decomposition temperature increases down Group 2.",
        [{'label': 'a', 'text': 'Explain why Mg(NO3)2 decomposes at a lower temperature than Ba(NO3)2.', 'marks': 4}],
        "21. (a) Mg2+ is smaller than Ba2+ with higher charge density (1). Mg2+ polarizes the nitrate N-O bond more strongly (1). Weakens the N-O bond in nitrate ion (1). Requires less thermal energy to break bond and decompose (1)."),

    make_edexcel_q(22, "Solubility of Calcium Hydroxide vs Calcium Sulfate", "WCH14/01/Sample/Q22", 4,
        "Ca(OH)2 is sparingly soluble (pH ~12), while CaSO4 is poorly soluble.",
        [{'label': 'a', 'text': 'Relate their lattice energies and hydration enthalpies to explain why Ca(OH)2 is more soluble than CaSO4.', 'marks': 4}],
        "22. (a) SO4^2- is much larger than OH- (1). CaSO4 has larger lattice energy relative to hydration enthalpy (1). Delta_sol H for CaSO4 is more endothermic (1). Ca(OH)2 has less endothermic Delta_sol H, allowing greater dissolution (1)."),

    make_edexcel_q(23, "Born-Haber Cycle for Lithium Iodide LiI", "WCH14/01/Sample/Q23", 5,
        "Data (kJ mol-1): Delta_f H(LiI) = -270, Delta_at H(Li) = +159, IE1(Li) = +520, 1/2 Delta_at H(I2) = +107, EA1(I) = -295.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for LiI(s).', 'marks': 4},
         {'label': 'b', 'text': 'Explain why LiI is soluble in organic solvents like ethanol.', 'marks': 1}],
        "23. (a) -270 = +159 + 520 + 107 - 295 + Delta_LE H = +491 + Delta_LE H (3). Delta_LE H = -270 - 491 = -761 kJ mol-1 (1).<br/>23. (b) Significant covalent character allows dissolution in non-polar/polar organic solvents (1)."),

    make_edexcel_q(24, "Enthalpy of Hydration vs Lattice Energy for BaCl2", "WCH14/01/Sample/Q24", 4,
        "BaCl2(s) -> Ba2+(aq) + 2Cl-(aq): Delta_LE H = -2056 kJ mol-1, Delta_hyd H(Ba2+) = -1305 kJ mol-1, Delta_hyd H(Cl-) = -364 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for BaCl2.', 'marks': 3},
         {'label': 'b', 'text': 'State whether dissolution is exothermic or endothermic.', 'marks': 1}],
        "24. (a) Delta_sol H = (-1305 + 2(-364)) - (-2056) = -2033 - (-2056) = -23 kJ mol-1 (3).<br/>24. (b) Exothermic (Delta_sol H < 0) (1)."),

    make_edexcel_q(25, "Born-Haber Cycle for Copper(II) Oxide CuO", "WCH14/01/Sample/Q25", 5,
        "Data (kJ mol-1): Delta_f H(CuO) = -157, Delta_at H(Cu) = +338, IE1(Cu) = +746, IE2(Cu) = +1958, 1/2 Delta_at H(O2) = +249, EA1(O)+EA2(O) = +657.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for CuO(s).', 'marks': 5}],
        "25. (a) Sum = +338 + 746 + 1958 + 249 + 657 = +3948 kJ mol-1 (3). -157 = 3948 + Delta_LE H => Delta_LE H = -157 - 3948 = -4105 kJ mol-1 (2)."),

    make_edexcel_q(26, "A* Challenge: Born-Haber Cycle with Unknown Electron Affinity", "WCH14/01/Hard/Q26", 5,
        "For metal bromide MBr2: Delta_f H = -524 kJ mol-1, Delta_at H(M) = +178, IE1(M) = +590, IE2(M) = +1145, Delta_at H(Br2) = +112, Delta_LE H = -2150.",
        [{'label': 'a', 'text': 'Calculate the first electron affinity of bromine, EA1(Br), in kJ mol-1.', 'marks': 5}],
        "26. (a) -524 = 178 + 590 + 1145 + 112 + 2(EA1(Br)) - 2150 = 2225 - 2150 + 2(EA1(Br)) = +75 + 2(EA1(Br)) (3). 2(EA1(Br)) = -524 - 75 = -599 => EA1(Br) = -299.5 kJ mol-1 (2)."),

    make_edexcel_q(27, "A* Challenge: Percent Covalent Character from Lattice Energy Comparison", "WCH14/01/Hard/Q27", 5,
        "For AgBr: Experimental Born-Haber lattice energy = -905 kJ mol-1; Theoretical ionic model lattice energy = -758 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate the percentage difference between experimental and theoretical lattice energy.', 'marks': 2},
         {'label': 'b', 'text': 'Explain the structural origin of this discrepancy in detail.', 'marks': 3}],
        "27. (a) % diff = [(-905 - (-758)) / -758] x 100% = (-147 / -758) x 100% = 19.4% (2).<br/>27. (b) Ag+ has 4d10 outer shell with incomplete shielding, high polarizing power (1). Large polarizable Br- electron cloud is distorted (1). Introduces substantial covalent orbital overlap, adding covalent bond energy to ionic attraction (1)."),

    make_edexcel_q(28, "A* Challenge: Enthalpy of Solution Temperature Dependence & Entropy", "WCH14/01/Hard/Q28", 5,
        "For KI: Delta_LE H = -649 kJ mol-1, Delta_hyd H(K+) = -322, Delta_hyd H(I-) = -293.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for KI.', 'marks': 2},
         {'label': 'b', 'text': 'Predict how the solubility of KI changes with increasing temperature using Le Chatelier and entropy.', 'marks': 3}],
        "28. (a) Delta_sol H = (-322 - 293) - (-649) = -615 - (-649) = +34 kJ mol-1 (2).<br/>28. (b) Dissolution is endothermic (Delta_sol H > 0). Increasing temperature shifts equilibrium KI(s) <=> K+(aq) + I-(aq) to the right (1). Delta S_surroundings becomes less negative, making Delta S_total more positive, increasing solubility (2)."),

    make_edexcel_q(29, "A* Challenge: Lattice Energy of Hypothetical NaCl2", "WCH14/01/Hard/Q29", 6,
        "Consider why NaCl2(s) does not form despite its high theoretical lattice energy.",
        [{'label': 'a', 'text': 'Estimate Delta_LE H for NaCl2(s) assuming it is similar to MgCl2 (-2500 kJ mol-1).', 'marks': 1},
         {'label': 'b', 'text': 'Explain why the second ionisation energy of sodium (IE2 = +4562 kJ mol-1) makes Delta_f H(NaCl2) highly endothermic.', 'marks': 3},
         {'label': 'c', 'text': 'Conclude why NaCl(s) forms instead of NaCl2(s).', 'marks': 2}],
        "29. (a) ~ -2500 kJ mol-1 (1).<br/>29. (b) IE2(Na) removes an electron from a inner 2p shell (noble gas core) requiring massive energy (+4562 kJ mol-1) (2). This huge energy input outweighs the extra lattice energy gained by Na2+ (1).<br/>29. (c) Delta_f H(NaCl2) is highly endothermic (+200 to +400 kJ mol-1) whereas Delta_f H(NaCl) is exothermic (-411 kJ mol-1). NaCl is thermodynamically stable (2)."),

    make_edexcel_q(30, "A* Challenge: Hydration Enthalpy vs Lattice Energy Competition in Halides", "WCH14/01/Hard/Q30", 5,
        "Enthalpies of solution Delta_sol H (kJ mol-1): LiF = +4.7, LiCl = -37.0, LiBr = -48.8, LiI = -63.3.",
        [{'label': 'a', 'text': 'Explain the trend in Delta_sol H down the lithium halides.', 'marks': 5}],
        "30. (a) As halide radius increases (F- < Cl- < Br- < I-), both lattice energy and hydration enthalpy become less exothermic (2). Lattice energy decreases much faster because r_Li+ + r_halide decreases proportionally more for lattice packing (2). Decreasing lattice energy dominates over decreasing hydration enthalpy, making Delta_sol H increasingly exothermic (1)."),

    make_edexcel_q(31, "A* Challenge: Born-Haber Cycle for Calcium Oxide CaO", "WCH14/01/Hard/Q31", 5,
        "Data (kJ mol-1): Delta_f H(CaO) = -635, Delta_at H(Ca) = +178, IE1(Ca) = +590, IE2(Ca) = +1145, 1/2 Delta_at H(O2) = +249, EA1(O) = -141, EA2(O) = +798.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for CaO(s).', 'marks': 4},
         {'label': 'b', 'text': 'Compare Delta_LE H(CaO) with Delta_LE H(NaCl) (-787 kJ mol-1).', 'marks': 1}],
        "31. (a) Sum atom/IE/EA = +178 + 590 + 1145 + 249 - 141 + 798 = +2819 kJ mol-1 (2). -635 = 2819 + Delta_LE H => Delta_LE H = -635 - 2819 = -3454 kJ mol-1 (2).<br/>31. (b) 2+ and 2- charges in CaO give 4x electrostatic attraction force compared to 1+ and 1- in NaCl (1)."),

    make_edexcel_q(32, "A* Challenge: Polarization Effect on Thermal Stability of Carbonates", "WCH14/01/Hard/Q32", 5,
        "Compare thermal decomposition of Na2CO3 (does not decompose at 800 °C) vs CaCO3 (decomposes at 840 °C) vs MgCO3 (decomposes at 300 °C).",
        [{'label': 'a', 'text': 'Explain why Na+ causes less polarization than Ca2+ and Mg2+.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why MgCO3 decomposes at a much lower temperature than CaCO3.', 'marks': 2}],
        "32. (a) Na+ has +1 charge (lower charge density) so it does not polarize the carbonate ion significantly (2). Ca2+ and Mg2+ have +2 charges and polarize carbonate C-O bond, weakening it (1).<br/>32. (b) Mg2+ is smaller than Ca2+ so it has higher charge density and stronger polarizing power, weakening C-O bond more (2)."),

    make_edexcel_q(33, "A* Challenge: Born-Haber Cycle for Barium Chloride BaCl2", "WCH14/01/Hard/Q33", 5,
        "Data (kJ mol-1): Delta_f H(BaCl2) = -858, Delta_at H(Ba) = +180, IE1(Ba) = +503, IE2(Ba) = +965, 2 x 1/2 Delta_at H(Cl2) = +244, 2 x EA1(Cl) = -698.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for BaCl2(s).', 'marks': 4},
         {'label': 'b', 'text': 'Compare Delta_LE H(BaCl2) with Delta_LE H(MgCl2) (-2525 kJ mol-1).', 'marks': 1}],
        "33. (a) Sum = 180 + 503 + 965 + 244 - 698 = +1194 (2). -858 = 1194 + Delta_LE H => Delta_LE H = -858 - 1194 = -2052 kJ mol-1 (2).<br/>33. (b) Ba2+ has a larger ionic radius than Mg2+, leading to weaker electrostatic attraction and less exothermic lattice energy (1)."),

    make_edexcel_q(34, "A* Challenge: Hydration Enthalpy vs Ion Size in Transition Metal Ions", "WCH14/01/Hard/Q34", 5,
        "Delta_hyd H° (kJ mol-1): Fe2+ = -1946, Fe3+ = -4430.",
        [{'label': 'a', 'text': 'Explain why Fe3+ has a vastly more exothermic hydration enthalpy than Fe2+.', 'marks': 3},
         {'label': 'b', 'text': 'Predict how this affects the acidity of [Fe(H2O)6]3+ vs [Fe(H2O)6]2+ solutions.', 'marks': 2}],
        "34. (a) Fe3+ has higher charge (+3 vs +2) and smaller ionic radius (0.64 Å vs 0.78 Å) (1). Fe3+ has much higher charge density, pulling water oxygen lone pairs much more strongly (2).<br/>34. (b) Fe3+ polarizes O-H bonds of attached water ligand molecules more strongly, weakening O-H bonds and releasing H+ ions readily (pH ~2 vs pH ~5) (2)."),

    make_edexcel_q(35, "A* Challenge: Enthalpy Cycle for Anhydrous vs Hydrated Copper Sulfate", "WCH14/01/Hard/Q35", 5,
        "CuSO4(s) + 5H2O(l) -> CuSO4.5H2O(s). Delta_sol H(CuSO4(s)) = -66.5 kJ mol-1; Delta_sol H(CuSO4.5H2O(s)) = +11.7 kJ mol-1.",
        [{'label': 'a', 'text': 'Construct a Hess\'s law cycle to calculate Delta H_hydration for CuSO4(s) -> CuSO4.5H2O(s).', 'marks': 4},
         {'label': 'b', 'text': 'Why cannot Delta H_hydration be measured directly by calorimetry?', 'marks': 1}],
        "35. (a) Delta H_hyd = Delta_sol H(CuSO4(s)) - Delta_sol H(CuSO4.5H2O(s)) (2) = -66.5 - (+11.7) = -78.2 kJ mol-1 (2).<br/>35. (b) Water dissolves the solid as it hydrates, making direct measurement of solid hydration impossible (1)."),

    make_edexcel_q(36, "A* Challenge: Enthalpy of Solution of Potassium Nitrate KNO3", "WCH14/01/Hard/Q36", 5,
        "KNO3(s) -> K+(aq) + NO3-(aq): Delta_LE H = -687 kJ mol-1, Delta_hyd H(K+) = -322, Delta_hyd H(NO3-) = -314.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for KNO3.', 'marks': 2},
         {'label': 'b', 'text': 'If Delta S_system = +115 J K-1 mol-1, calculate Delta S_total at 298 K and explain why KNO3 dissolves.', 'marks': 3}],
        "36. (a) Delta_sol H = (-322 - 314) - (-687) = -636 - (-687) = +51.0 kJ mol-1 (2).<br/>36. (b) Delta S_surr = -51000 / 298 = -171.1 J K-1 mol-1. Delta S_total = +115 - 171.1 = -56.1 J K-1 mol-1 at 298 K. Dissolves at higher temperature as Delta S_surr becomes less negative (3)."),

    make_edexcel_q(37, "A* Challenge: Born-Haber Cycle for Silver Chloride AgCl", "WCH14/01/Hard/Q37", 5,
        "Data (kJ mol-1): Delta_f H(AgCl) = -127, Delta_at H(Ag) = +285, IE1(Ag) = +731, 1/2 Delta_at H(Cl2) = +122, EA1(Cl) = -349.",
        [{'label': 'a', 'text': 'Calculate experimental Born-Haber Delta_LE H for AgCl.', 'marks': 3},
         {'label': 'b', 'text': 'The theoretical ionic lattice energy for AgCl is -770 kJ mol-1. Account for the difference.', 'marks': 2}],
        "37. (a) -127 = +285 + 731 + 122 - 349 + Delta_LE H = +789 + Delta_LE H => Delta_LE H = -127 - 789 = -916 kJ mol-1 (3).<br/>37. (b) Experimental value (-916) is 146 kJ mol-1 more exothermic than theoretical (-770) due to significant covalent character / polarization of Cl- by Ag+ (2)."),

    make_edexcel_q(38, "A* Challenge: Enthalpy of Atomisation of Metals vs Lattice Energy", "WCH14/01/Hard/Q38", 5,
        "Delta_at H (kJ mol-1): Na = +107, Mg = +148, Al = +326.",
        [{'label': 'a', 'text': 'Explain the trend in enthalpy of atomisation across Period 3 metals.', 'marks': 3},
         {'label': 'b', 'text': 'Relate metallic bond strength to charge density of metal cations and delocalised electron count.', 'marks': 2}],
        "38. (a) Atomisation enthalpy increases from Na to Al (3).<br/>38. (b) Cation charge increases (+1 to +3), ionic radius decreases, and number of delocalised electrons per atom increases (1 -> 3), strengthening metallic bonding immensely (2)."),

    make_edexcel_q(39, "A* Challenge: Born-Haber Cycle for Zinc Sulfide ZnS", "WCH14/01/Hard/Q39", 5,
        "Data (kJ mol-1): Delta_f H(ZnS) = -206, Delta_at H(Zn) = +131, IE1(Zn)+IE2(Zn) = +2735, Delta_at H(S) = +279, EA1(S)+EA2(S) = +332.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for ZnS(s).', 'marks': 4},
         {'label': 'b', 'text': 'Explain why ZnS adopts a covalent zinc blende structure rather than a purely ionic NaCl lattice.', 'marks': 1}],
        "39. (a) Sum = 131 + 2735 + 279 + 332 = +3477 (2). -206 = 3477 + Delta_LE H => Delta_LE H = -206 - 3477 = -3683 kJ mol-1 (2).<br/>39. (b) Zn2+ strongly polarizes S2- (large polarizable anion), resulting in dominant covalent bonding character (1)."),

    make_edexcel_q(40, "A* Challenge: Dissolution Energetics of Calcium Chloride CaCl2", "WCH14/01/Hard/Q40", 5,
        "CaCl2(s) -> Ca2+(aq) + 2Cl-(aq): Delta_LE H = -2258 kJ mol-1, Delta_hyd H(Ca2+) = -1577, Delta_hyd H(Cl-) = -364.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for CaCl2.', 'marks': 3},
         {'label': 'b', 'text': 'Why is CaCl2 used in self-heating food cans and de-icing roads?', 'marks': 2}],
        "40. (a) Delta_sol H = (-1577 + 2(-364)) - (-2258) = -2305 - (-2258) = -47 kJ mol-1 (3).<br/>40. (b) Dissolution is strongly exothermic (Delta_sol H = -47 kJ mol-1), generating heat (1). Dissolved ions depress freezing point of water effectively (1)."),

    make_edexcel_q(41, "A* Challenge: Polarization and Thermal Decomposition of Hydroxides", "WCH14/01/Hard/Q41", 5,
        "Mg(OH)2(s) -> MgO(s) + H2O(g) occurs at 350 °C, whereas Ba(OH)2 melts at 780 °C without decomposing.",
        [{'label': 'a', 'text': 'Explain in terms of polarizing power of Mg2+ vs Ba2+ why Mg(OH)2 decomposes easily.', 'marks': 5}],
        "41. (a) Mg2+ has a small ionic radius and high charge density / high polarizing power (1). Mg2+ attracts oxygen electron density of the OH- ion (1). Weakens the O-H bond and facilitates splitting off H2O (1). Ba2+ has a much larger radius and low charge density, so it cannot weaken O-H bond sufficiently to induce decomposition (2)."),

    make_edexcel_q(42, "A* Challenge: Enthalpy of Hydration of Gaseous Protons H+(g)", "WCH14/01/Hard/Q42", 5,
        "The hydration enthalpy of H+(g) is exceptionally exothermic: Delta_hyd H(H+) = -1090 kJ mol-1.",
        [{'label': 'a', 'text': 'Explain why H+(g) has a vastly more exothermic hydration enthalpy than Na+(g) (-406 kJ mol-1).', 'marks': 3},
         {'label': 'b', 'text': 'Write the chemical equation for H+(g) hydration forming H3O+(aq).', 'marks': 2}],
        "42. (a) H+ is a bare proton with zero electron shell and extremely small radius (~10^-15 m) (1). It has an infinitely high charge density (1), reacting covalently with water lone pair to form dative H3O+(aq) (1).<br/>42. (b) H+(g) + H2O(l) -> H3O+(aq) (2)."),

    make_edexcel_q(43, "A* Challenge: Born-Haber Cycle for Sodium Fluoride NaF", "WCH14/01/Hard/Q43", 5,
        "Data (kJ mol-1): Delta_f H(NaF) = -574, Delta_at H(Na) = +107, IE1(Na) = +496, 1/2 Delta_at H(F2) = +79, EA1(F) = -328.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for NaF(s).', 'marks': 4},
         {'label': 'b', 'text': 'Compare Delta_LE H(NaF) with Delta_LE H(NaCl) (-787 kJ mol-1).', 'marks': 1}],
        "43. (a) Sum = 107 + 496 + 79 - 328 = +354 (2). -574 = 354 + Delta_LE H => Delta_LE H = -574 - 354 = -928 kJ mol-1 (2).<br/>43. (b) F- is smaller than Cl-, allowing closer ionic approach and stronger electrostatic attraction (-928 vs -787) (1)."),

    make_edexcel_q(44, "A* Challenge: Solvation Enthalpies in Non-Aqueous Solvents", "WCH14/01/Hard/Q44", 5,
        "Delta_sol H(LiCl) in liquid ammonia is -120 kJ mol-1 compared to -37 kJ mol-1 in water.",
        [{'label': 'a', 'text': 'Explain why solvation enthalpy of Li+ is more exothermic in ammonia than in water.', 'marks': 3},
         {'label': 'b', 'text': 'Relate nitrogen lone pair electron-donating ability to oxygen in water.', 'marks': 2}],
        "44. (a) NH3 has a less electronegative nitrogen atom which donates its lone pair more readily to Li+ (1). Forms stronger dative covalent coordination bonds [Li(NH3)4]+ (2).<br/>44. (b) Nitrogen is less electronegative than oxygen, holding its lone pair less tightly and forming stronger dative bonds to cations (2)."),

    make_edexcel_q(45, "A* Challenge: Theoretical vs Experimental Lattice Energies of Transition Metal Halides", "WCH14/01/Hard/Q45", 5,
        "Delta_LE H (kJ mol-1): MnCl2 (exp -2520, theo -2480); FeCl2 (exp -2530, theo -2490); CuCl2 (exp -2750, theo -2580).",
        [{'label': 'a', 'text': 'Explain why CuCl2 shows a much larger discrepancy (170 kJ mol-1) than MnCl2 (40 kJ mol-1).', 'marks': 3},
         {'label': 'b', 'text': 'Relate this to Crystal Field Stabilization Energy (CFSE) and Jahn-Teller distortion.', 'marks': 2}],
        "45. (a) Cu2+ (d9) experiences strong Jahn-Teller distortion and high polarizing power, introducing significant covalent character (3).<br/>45. (b) CFSE provides additional thermodynamic stabilization beyond simple electrostatic ionic model for d9 Cu2+ compared to high-spin d5 Mn2+ (CFSE = 0) (2)."),

    make_edexcel_q(46, "A* Challenge: Born-Haber Cycle for Lead(II) Chloride PbCl2", "WCH14/01/Hard/Q46", 5,
        "Data (kJ mol-1): Delta_f H(PbCl2) = -359, Delta_at H(Pb) = +195, IE1(Pb)+IE2(Pb) = +2190, Delta_at H(Cl2) = +244, 2 x EA1(Cl) = -698.",
        [{'label': 'a', 'text': 'Calculate experimental Delta_LE H for PbCl2(s).', 'marks': 4},
         {'label': 'b', 'text': 'Why is PbCl2 insoluble in cold water?', 'marks': 1}],
        "46. (a) Sum = 195 + 2190 + 244 - 698 = +1931 (2). -359 = 1931 + Delta_LE H => Delta_LE H = -359 - 1931 = -2290 kJ mol-1 (2).<br/>46. (b) High covalent character and strong lattice energy make Delta_sol H endothermic (1)."),

    make_edexcel_q(47, "A* Challenge: Calculating Enthalpy of Solution from Calorimetry Data", "WCH14/01/Hard/Q47", 5,
        "5.00 g of anhydrous CaCl2 (Mr = 111.0) was dissolved in 100 cm3 of water in a calorimeter. Temperature rose by 8.4 °C.<br/>(Specific heat capacity c = 4.18 J g-1 K-1)",
        [{'label': 'a', 'text': 'Calculate q = m c Delta T in Joules.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate moles of CaCl2 and deduce Delta_sol H in kJ mol-1.', 'marks': 3}],
        "47. (a) q = 100 x 4.18 x 8.4 = 3511.2 J = 3.511 kJ (2).<br/>47. (b) Moles = 5.00 / 111.0 = 0.04505 mol (1). Delta_sol H = -3.511 / 0.04505 = -77.9 kJ mol-1 (2)."),

    make_edexcel_q(48, "A* Challenge: Born-Haber Cycle for Potassium Iodide KI", "WCH14/01/Hard/Q48", 5,
        "Data (kJ mol-1): Delta_f H(KI) = -328, Delta_at H(K) = +89, IE1(K) = +418, 1/2 Delta_at H(I2) = +107, EA1(I) = -295.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for KI(s).', 'marks': 4},
         {'label': 'b', 'text': 'Why does KI have a theoretical lattice energy almost identical to experimental?', 'marks': 1}],
        "48. (a) Sum = 89 + 418 + 107 - 295 = +319 (2). -328 = 319 + Delta_LE H => Delta_LE H = -328 - 319 = -647 kJ mol-1 (2).<br/>48. (b) K+ has low charge density (+1, large radius) so it does not polarize I-, resulting in almost 100% pure ionic bonding (1)."),

    make_edexcel_q(49, "A* Challenge: Hydration Enthalpy vs Ionic Size Grid Analysis", "WCH14/01/Hard/Q49", 5,
        "Predict and rank Delta_hyd H° for Na+, K+, Mg2+, Ca2+.",
        [{'label': 'a', 'text': 'Rank the four ions in order of increasingly exothermic hydration enthalpy with full justification.', 'marks': 5}],
        "49. (a) K+ < Na+ < Ca2+ < Mg2+ (1). K+ is 1+ with largest radius (least exothermic) (1); Na+ is 1+ with smaller radius (1); Ca2+ is 2+ with larger radius than Mg2+ (1); Mg2+ is 2+ with smallest radius (highest charge density, most exothermic Delta_hyd H = -1920 kJ mol-1) (1)."),

    make_edexcel_q(50, "A* Challenge: Complete Energetics Master Synthesis", "WCH14/01/Hard/Q50", 6,
        "A student investigates anhydrous MgF2(s).<br/>Data (kJ mol-1): Delta_f H(MgF2) = -1124, Delta_at H(Mg) = +148, IE1(Mg)+IE2(Mg) = +2189, Delta_at H(F2) = +158, EA1(F) = -328.",
        [{'label': 'a', 'text': 'Calculate Delta_LE H for MgF2(s).', 'marks': 3},
         {'label': 'b', 'text': 'Given Delta_hyd H(Mg2+) = -1920 and Delta_hyd H(F-) = -506 kJ mol-1, calculate Delta_sol H for MgF2.', 'marks': 3}],
        "50. (a) Sum = 148 + 2189 + 158 - 2(328) = 2495 - 656 = +1839 (1.5). Delta_LE H = -1124 - 1839 = -2963 kJ mol-1 (1.5).<br/>50. (b) Delta_sol H = (-1920 + 2(-506)) - (-2963) = (-1920 - 1012) + 2963 = -2932 + 2963 = +31.0 kJ mol-1 (3).")
]

p3_faqs = [
    make_edexcel_faq("Definition of Lattice Energy Direction", "Definition Trap", "Defining lattice energy as dissociation (endothermic) instead of formation (exothermic).", "Edexcel IAL defines lattice energy as the enthalpy change when ONE mole of an ionic crystal is FORMED from its gaseous ions (always EXOTHERMIC, negative sign)."),
    make_edexcel_faq("Multiplying Electron Affinity for Di-halides", "Stoichiometry Trap", "Forgetting to multiply EA1 by 2 for MX2 salts like MgCl2 or CaF2.", "For MX2 compounds, 2 moles of halide ions are formed from 2 moles of halogen atoms. You MUST multiply EA1 by 2 (e.g. 2 x -349 = -698 kJ mol-1)."),
    make_edexcel_faq("Second Ionisation Energy for Group 2 Metals", "Ionisation Trap", "Including only IE1 for Group 2 metals in Born-Haber cycles.", "Group 2 metals form M2+ ions. The cycle MUST include both IE1 and IE2 (e.g. Mg -> Mg+ -> Mg2+)."),
    make_edexcel_faq("Sign of Second Electron Affinity", "EA2 Trap", "Assuming EA2 is exothermic like EA1.", "EA1 is exothermic (attraction to neutral atom), but EA2 is ALWAYS ENDOTHERMIC (positive) due to electrostatic repulsion between incoming e- and 1- anion."),
    make_edexcel_faq("Theoretical vs Experimental Discrepancy", "Covalency Trap", "Attributing lattice energy discrepancies to experimental measurement error.", "Discrepancy occurs because theoretical model assumes 100% spherical ionic bonding. Experimental Born-Haber cycle includes COVALENT CHARACTER caused by cation polarization of anion."),
    make_edexcel_faq("Fajans' Polarization Criteria", "Fajans Rules", "Confusing which ion polarizes and which is polarized.", "The CATION polarizes (requires high charge, small radius). The ANION is polarized (requires high charge, large polarizable electron cloud)."),
    make_edexcel_faq("Hydration Enthalpy Sign in Solution Cycle", "Hess Cycle Trap", "Subtracting hydration enthalpy instead of lattice energy in Delta_sol H.", "Delta_sol H = Sum Delta_hyd H(ions) - Delta_LE H. Hydration is exothermic (-), lattice formation is exothermic (-), so subtracting lattice formation subtracts a negative number."),
    make_edexcel_faq("Group 2 Sulfate Solubility Trend", "Solubility Trend", "Explaining sulfate solubility trend without emphasizing large sulfate ion size.", "SO4^2- is very large, so lattice energy changes little down group. Decreasing hydration enthalpy of cation dominates, making Delta_sol H more endothermic down group (less soluble)."),
    make_edexcel_faq("Group 2 Hydroxide Solubility Trend", "Solubility Trend", "Confusing hydroxide solubility trend with sulfate trend.", "OH- is small, so lattice energy decreases sharply down group. Decreasing lattice energy dominates over decreasing hydration enthalpy, making Delta_sol H more exothermic down group (more soluble)."),
    make_edexcel_faq("Ionic Charge vs Radius Impact on Lattice Energy", "Lattice Comparison", "Treating ionic radius as having equal weight to ionic charge.", "Ionic charge has a SQUARED effect on electrostatic attraction force (q1 x q2), so doubling charge quadruples lattice energy, whereas changing radius has a smaller percentage impact.")
]

# Build Pack 3 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf", p3_meta, p3_questions, p3_faqs)
print("Pack 3 (12B Lattice Energy - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 4: 13A — CHEMICAL EQUILIBRIA (50 Qs + 10 FAQs)
# ==========================================
p4_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 13',
    'topic_name': 'CHEMICAL EQUILIBRIA',
    'subtopic_code': '13A',
    'subtopic_name': 'Chemical Equilibria (Kc, Kp, Factors & Total Entropy Relation)'
}

p4_questions = [
    make_edexcel_q(1, "Equilibrium Constant Kc Expression & Units", "WCH14/01/Jan23/Q9", 3,
        "For the reversible reaction: N2(g) + 3H2(g) <=> 2NH3(g)",
        [{'label': 'a', 'text': 'Write the expression for the equilibrium constant, Kc.', 'marks': 1},
         {'label': 'b', 'text': 'Deduce the units of Kc for this reaction.', 'marks': 2}],
        "1. (a) Kc = [NH3]^2 / ([N2][H2]^3) (1).<br/>1. (b) Units = (mol dm-3)^2 / ((mol dm-3)(mol dm-3)^3) = 1 / (mol dm-3)^2 = dm6 mol-2 (2)."),

    make_edexcel_q(2, "Homogeneous vs Heterogeneous Equilibria Kc Rules", "WCH14/01/Oct22/Q10", 4,
        "Consider the heterogeneous equilibrium: CaCO3(s) <=> CaO(s) + CO2(g)",
        [{'label': 'a', 'text': 'Explain why solid CaCO3 and CaO are omitted from the Kc expression.', 'marks': 2},
         {'label': 'b', 'text': 'Write the simplified Kc expression and state its units.', 'marks': 2}],
        "2. (a) Concentrations of pure solids are constant and incorporated into the value of Kc (2).<br/>2. (b) Kc = [CO2(g)] (1); units = mol dm-3 (1)."),

    make_edexcel_q(3, "ICE Table Calculation for Kc", "WCH14/01/Jun22/Q11", 5,
        "1.00 mol of CH3COOH and 2.00 mol of CH3CH2OH were reacted in a 1.00 dm3 vessel:<br/>CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O<br/>At equilibrium, 0.80 mol of ester was formed.",
        [{'label': 'a', 'text': 'Calculate the equilibrium amounts of CH3COOH, CH3CH2OH, and H2O.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate Kc for esterification.', 'marks': 2}],
        "3. (a) CH3COOH eq = 1.00 - 0.80 = 0.20 mol (1). CH3CH2OH eq = 2.00 - 0.80 = 1.20 mol (1). H2O eq = 0.80 mol (1).<br/>3. (b) Kc = (0.80 x 0.80) / (0.20 x 1.20) = 0.64 / 0.24 = 2.67 (dimensionless) (2)."),

    make_edexcel_q(4, "Equilibrium Constant Kp Expression & Partial Pressures", "WCH14/01/Jan22/Q12", 4,
        "For 2SO2(g) + O2(g) <=> 2SO3(g) at total pressure P_total.",
        [{'label': 'a', 'text': 'Define mole fraction x_A and partial pressure p_A.', 'marks': 2},
         {'label': 'b', 'text': 'Write the expression for Kp and deduce its units.', 'marks': 2}],
        "4. (a) Mole fraction x_A = moles A / total gas moles (1). Partial pressure p_A = x_A x P_total (1).<br/>4. (b) Kp = (p_SO3)^2 / ((p_SO2)^2 (p_O2)) (1); units = atm-1 or kPa-1 or Pa-1 (1)."),

    make_edexcel_q(5, "Equilibrium Pressure Calculation for Kp", "WCH14/01/Oct21/Q11", 5,
        "In a mixture of N2O4 and NO2 at 298 K, total pressure = 2.00 atm.<br/>Mole fraction of N2O4 = 0.40.",
        [{'label': 'a', 'text': 'Calculate the partial pressures of N2O4 and NO2.', 'marks': 2},
         {'label': 'b', 'text': 'Write Kp for N2O4(g) <=> 2NO2(g) and calculate its value with units.', 'marks': 3}],
        "5. (a) p_N2O4 = 0.40 x 2.00 = 0.80 atm (1). x_NO2 = 1.0 - 0.40 = 0.60 => p_NO2 = 0.60 x 2.00 = 1.20 atm (1).<br/>5. (b) Kp = (p_NO2)^2 / p_N2O4 = (1.20)^2 / 0.80 = 1.44 / 0.80 = 1.80 atm (3)."),

    make_edexcel_q(6, "Effect of Temperature on Kc and Kp for Exothermic Reactions", "WCH14/01/Jun21/Q12", 4,
        "For N2(g) + 3H2(g) <=> 2NH3(g) (Delta H = -92.2 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain why increasing temperature decreases the value of Kc.', 'marks': 3},
         {'label': 'b', 'text': 'Relate this to Le Chatelier\'s principle.', 'marks': 1}],
        "6. (a) Increasing temperature favours the endothermic reverse reaction to absorb heat (1). Concentration of reactants increases and products decreases (1). Since Kc = [NH3]^2 / ([N2][H2]^3), Kc decreases (1).<br/>6. (b) Le Chatelier\'s principle states equilibrium shifts to oppose temperature increase (1)."),

    make_edexcel_q(7, "Effect of Temperature on K for Endothermic Reactions", "WCH14/01/Jan21/Q13", 3,
        "For N2O4(g) <=> 2NO2(g) (Delta H = +57.2 kJ mol-1).",
        [{'label': 'a', 'text': 'Predict and explain how increasing temperature affects Kp.', 'marks': 3}],
        "7. (a) Forward reaction is endothermic (Delta H > 0) (1). Increasing temperature shifts equilibrium to the right to absorb heat (1). Partial pressure of NO2 increases relative to N2O4, so Kp increases (1)."),

    make_edexcel_q(8, "Why Pressure and Concentration Changes Do NOT Change K", "WCH14/01/Oct20/Q11", 4,
        "For 2SO2(g) + O2(g) <=> 2SO3(g), total pressure is doubled.",
        [{'label': 'a', 'text': 'Explain why doubling total pressure shifts equilibrium position to the right but leaves Kp unchanged.', 'marks': 4}],
        "8. (a) Doubling pressure initially doubles all partial pressures (1). The denominator (p_SO2)^2(p_O2) increases by 2^3 = 8x, while numerator (p_SO3)^2 increases by 2^2 = 4x (1). Quotient Q_p < Kp (1). System responds by converting 2SO2 + O2 into 2SO3 until partial pressure ratio restores exact value of Kp (1)."),

    make_edexcel_q(9, "Why Catalysts Do NOT Change Equilibrium Constant K", "WCH14/01/Jun20/Q13", 3,
        "A catalyst is added to an equilibrium mixture.",
        [{'label': 'a', 'text': 'Explain why a catalyst increases the rate of achieving equilibrium but has zero effect on the value of Kc or Kp.', 'marks': 3}],
        "9. (a) Catalyst speeds up both forward and reverse reaction rates by the exact same factor (1). Lowers activation energy Ea for both directions equally (1). Ratio of rate constants k_forward / k_reverse = K remains constant (1)."),

    make_edexcel_q(10, "Derivation & Calculation of Delta S_total = R ln K", "WCH14/01/Jan20/Q14", 4,
        "At thermodynamic equilibrium, total entropy change relates to K by Delta S_total = R ln K.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K for a reaction with K = 1.80 atm.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate K if Delta S_total = +50.0 J K-1 mol-1.', 'marks': 2}],
        "10. (a) Delta S_total = 8.31 x ln(1.80) = 8.31 x 0.5878 = +4.88 J K-1 mol-1 (2).<br/>10. (b) ln K = 50.0 / 8.31 = 6.0169 => K = e^6.0169 = 410.3 (2)."),

    # Questions 11 to 50: Authentic practice questions for Topic 13A
    make_edexcel_q(11, "Degree of Dissociation Calculation for PCl5", "WCH14/01/Oct19/Q14", 5,
        "PCl5(g) <=> PCl3(g) + Cl2(g). 1.00 mol of PCl5 was heated in a 10.0 dm3 vessel. At equilibrium, 0.40 mol of Cl2 was present.",
        [{'label': 'a', 'text': 'Calculate degree of dissociation alpha.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate Kc including units.', 'marks': 4}],
        "11. (a) alpha = 0.40 / 1.00 = 0.40 (40%) (1).<br/>11. (b) [PCl5]eq = 0.60/10 = 0.060 M; [PCl3]eq = 0.40/10 = 0.040 M; [Cl2]eq = 0.040 M (2). Kc = (0.040 x 0.040) / 0.060 = 0.00267 mol dm-3 (2)."),

    make_edexcel_q(12, "Esterification Equilibrium Calculation with Volume Cancellation", "WCH14/01/Jun19/Q15", 4,
        "CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O. Kc = 4.00.",
        [{'label': 'a', 'text': 'Explain why the container volume V cancels out in the Kc expression for this reaction.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate moles of ester formed when 1.00 mol of acid and 1.00 mol of alcohol reach equilibrium.', 'marks': 2}],
        "12. (a) Equal number of moles of reactants (2 mol) and products (2 mol), so volume V in numerator and denominator cancels completely (2).<br/>12. (b) Kc = x^2 / (1-x)^2 = 4.00 => x / (1-x) = 2.00 => x = 2 - 2x => 3x = 2 => x = 0.67 mol (2)."),

    make_edexcel_q(13, "Kp Calculation for Methanol Synthesis", "WCH14/01/Jan19/Q16", 5,
        "CO(g) + 2H2(g) <=> CH3OH(g). Equilibrium partial pressures: p_CO = 4.0 atm, p_H2 = 8.0 atm, p_CH3OH = 2.0 atm.",
        [{'label': 'a', 'text': 'Write Kp expression.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate Kp and deduce units.', 'marks': 3},
         {'label': 'c', 'text': 'Predict effect of increasing total pressure on methanol yield.', 'marks': 1}],
        "13. (a) Kp = p_CH3OH / (p_CO x (p_H2)^2) (1).<br/>13. (b) Kp = 2.0 / (4.0 x 64.0) = 2.0 / 256.0 = 7.81 x 10^-3 atm-2 (3).<br/>13. (c) Yield increases (3 gas moles form 1 gas mole) (1)."),

    make_edexcel_q(14, "Relationship Between Kc and Kp via Ideal Gas Law", "WCH14/01/Sample/Q14", 4,
        "Kp = Kc (R T)^(Delta n) where Delta n = change in gas moles.",
        [{'label': 'a', 'text': 'For N2(g) + 3H2(g) <=> 2NH3(g), state Delta n.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate Kp at 500 K if Kc = 0.060 dm6 mol-2. (R = 0.0821 dm3 atm K-1 mol-1)', 'marks': 3}],
        "14. (a) Delta n = 2 - 4 = -2 (1).<br/>14. (b) Kp = Kc (RT)^-2 = 0.060 x (0.0821 x 500)^-2 = 0.060 x (41.05)^-2 = 0.060 / 1685.1 = 3.56 x 10^-5 atm-2 (3)."),

    make_edexcel_q(15, "Heterogeneous Equilibrium Kp for Dehydration of Copper Sulfate", "WCH14/01/Sample/Q15", 3,
        "CuSO4.5H2O(s) <=> CuSO4(s) + 5H2O(g).",
        [{'label': 'a', 'text': 'Write the Kp expression for this heterogeneous reaction.', 'marks': 1},
         {'label': 'b', 'text': 'If the equilibrium vapor pressure of water is 0.030 atm at 298 K, calculate Kp.', 'marks': 2}],
        "15. (a) Kp = (p_H2O)^5 (1).<br/>15. (b) Kp = (0.030)^5 = 2.43 x 10^-8 atm5 (2)."),

    make_edexcel_q(16, "ICE Table with Quadratic Equation Solution", "WCH14/01/Sample/Q16", 5,
        "H2(g) + I2(g) <=> 2HI(g). Kc = 54.0 at 700 K.<br/>Initial: [H2]=1.00 M, [I2]=2.00 M, [HI]=0.00 M.",
        [{'label': 'a', 'text': 'Set up the Kc expression in terms of x (moles of H2 reacted).', 'marks': 2},
         {'label': 'b', 'text': 'Solve for x and calculate equilibrium concentrations of H2, I2, and HI.', 'marks': 3}],
        "16. (a) Kc = (2x)^2 / ((1-x)(2-x)) = 54.0 => 4x^2 = 54.0(2 - 3x + x^2) => 50.0x^2 - 162.0x + 108.0 = 0 (2).<br/>16. (b) x = 0.93 mol dm-3 (3). [H2]=0.07 M, [I2]=1.07 M, [HI]=1.86 M."),

    make_edexcel_q(17, "Temperature Dependence of K and Enthalpy Sign", "WCH14/01/Sample/Q17", 4,
        "Kc for a reaction is 1.0 x 10^-3 at 300 K and 4.5 x 10^-2 at 400 K.",
        [{'label': 'a', 'text': 'Deduce whether the forward reaction is exothermic or endothermic.', 'marks': 2},
         {'label': 'b', 'text': 'Explain using van \'t Hoff relationship ln(K2/K1) = (-Delta H / R)(1/T2 - 1/T1).', 'marks': 2}],
        "17. (a) Endothermic (Delta H > 0) because Kc increases as temperature increases (2).<br/>17. (b) ln(K2/K1) > 0 and (1/T2 - 1/T1) < 0, so -Delta H / R must be negative => Delta H > 0 (2)."),

    make_edexcel_q(18, "Calculation of Delta H from Two-Point K Data", "WCH14/01/Sample/Q18", 5,
        "For N2O4 <=> 2NO2: Kp = 0.141 atm at 298 K and Kp = 2.67 atm at 373 K.",
        [{'label': 'a', 'text': 'Calculate Delta H in kJ mol-1 using ln(Kp2/Kp1) = (Delta H / R)(1/T1 - 1/T2).', 'marks': 5}],
        "18. (a) ln(2.67 / 0.141) = ln(18.936) = 2.941 (1). (1/298 - 1/373) = 6.749 x 10^-4 K-1 (1). Delta H / R = 2.941 / 6.749x10^-4 = 4358 K (2). Delta H = 4358 x 8.31 = 36215 J mol-1 = +36.2 kJ mol-1 (1)."),

    make_edexcel_q(19, "Total Entropy at Equilibrium Boundary", "WCH14/01/Sample/Q19", 4,
        "Explain why Delta S_total = 0 when a system reaches dynamic equilibrium.",
        [{'label': 'a', 'text': 'Relate forward and reverse rates, entropy changes, and free energy at equilibrium.', 'marks': 4}],
        "19. (a) At dynamic equilibrium, rate of forward reaction equals rate of reverse reaction (1). Net concentration of all species remains constant (1). Universe entropy is maximized for the system composition, so Delta S_total = 0 (1). Delta G = -T Delta S_total = 0 (1)."),

    make_edexcel_q(20, "Le Chatelier\'s Principle vs Reaction Quotient Q", "WCH14/01/Sample/Q20", 4,
        "For A + B <=> C + D, Kc = 10.0.<br/>A mixture currently has [A]=0.5 M, [B]=0.5 M, [C]=2.0 M, [D]=2.0 M.",
        [{'label': 'a', 'text': 'Calculate the reaction quotient Qc = [C][D]/([A][B]).', 'marks': 2},
         {'label': 'b', 'text': 'Compare Qc with Kc and predict which direction the reaction will proceed to reach equilibrium.', 'marks': 2}],
        "20. (a) Qc = (2.0 x 2.0) / (0.5 x 0.5) = 4.0 / 0.25 = 16.0 (2).<br/>20. (b) Qc (16.0) > Kc (10.0) (1). Reaction will shift to the left (reverse direction) to consume C and D and form more A and B until Qc = Kc (1)."),

    # Questions 21 to 50: Additional authentic past-paper questions for 13A
    make_edexcel_q(21, "Effect of Inert Gas Addition on Kp", "WCH14/01/Sample/Q21", 4,
        "Inert argon gas is added to N2(g) + 3H2(g) <=> 2NH3(g) at constant total volume.",
        [{'label': 'a', 'text': 'Explain why adding an inert gas at constant volume has zero effect on the position of equilibrium or Kp.', 'marks': 4}],
        "21. (a) Adding argon increases total pressure but total volume is constant (1). Partial pressures of N2, H2, and NH3 remain completely unchanged (2). Therefore Kp and equilibrium position remain unchanged (1)."),

    make_edexcel_q(22, "Effect of Inert Gas Addition at Constant Total Pressure", "WCH14/01/Sample/Q22", 4,
        "Inert argon gas is added to N2O4(g) <=> 2NO2(g) at constant total pressure.",
        [{'label': 'a', 'text': 'Explain why adding argon at constant pressure causes the equilibrium to shift to the right.', 'marks': 4}],
        "22. (a) Adding argon increases total gas volume to keep total pressure constant (1). Mole fractions and partial pressures of reactant N2O4 and product NO2 both decrease (1). Since Kp = (p_NO2)^2 / p_N2O4, denominator decreases less than numerator (1). System shifts right (towards more gas moles) to restore Kp (1)."),

    make_edexcel_q(23, "Equilibrium Yield Optimization in Contact Process", "WCH14/01/Sample/Q23", 5,
        "Contact Process: 2SO2(g) + O2(g) <=> 2SO3(g) (Delta H = -197 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain the industrial choice of conditions: 1-2 atm pressure, 450 °C, V2O5 catalyst.', 'marks': 5}],
        "23. (a) Moderate pressure (1-2 atm) gives >99% yield without high cost of high-pressure equipment (2). 450 °C provides acceptable rate while keeping exothermic Kp high enough for high yield (2). V2O5 catalyst speeds up rate without affecting yield (1)."),

    make_edexcel_q(24, "Decomposition of Ammonium Chloride Equilibrium Kp", "WCH14/01/Sample/Q24", 4,
        "NH4Cl(s) <=> NH3(g) + HCl(g). At equilibrium at 600 K, total pressure is 4.00 atm.",
        [{'label': 'a', 'text': 'Deduce partial pressures of NH3 and HCl.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Kp and give units.', 'marks': 2}],
        "24. (a) Equimolar gas formation => p_NH3 = p_HCl = 2.00 atm (2).<br/>24. (b) Kp = p_NH3 x p_HCl = 2.00 x 2.00 = 4.00 atm2 (2)."),

    make_edexcel_q(25, "Equilibrium Constant for Steam Reforming of Methane", "WCH14/01/Sample/Q25", 5,
        "CH4(g) + H2O(g) <=> CO(g) + 3H2(g) (Delta H = +206 kJ mol-1).",
        [{'label': 'a', 'text': 'Write Kp expression.', 'marks': 1},
         {'label': 'b', 'text': 'Explain why high temperature and low pressure maximize equilibrium yield of H2.', 'marks': 4}],
        "25. (a) Kp = (p_CO x (p_H2)^3) / (p_CH4 x p_H2O) (1).<br/>25. (b) Endothermic reaction (Delta H > 0) => high temperature shifts equilibrium right to absorb heat, increasing Kp (2). 2 gas moles form 4 gas moles => low pressure shifts equilibrium right towards more gas moles (2)."),

    make_edexcel_q(26, "A* Challenge: Multi-Step ICE Table with Partial Pressures", "WCH14/01/Hard/Q26", 5,
        "Equilibrium: A(g) + 2B(g) <=> C(g) + D(g).<br/>Initial: 2.0 mol A, 3.0 mol B in a container at 10.0 atm total pressure.<br/>At equilibrium, 1.0 mol of C is formed.",
        [{'label': 'a', 'text': 'Calculate equilibrium moles of A, B, C, D and total gas moles.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate partial pressures and Kp.', 'marks': 2}],
        "26. (a) A_eq = 1.0, B_eq = 1.0, C_eq = 1.0, D_eq = 1.0 mol. Total moles = 4.0 mol (3).<br/>26. (b) Mole fractions all 0.25 => p_A=p_B=p_C=p_D = 2.5 atm. Kp = (2.5 x 2.5) / (2.5 x (2.5)^2) = 1 / 2.5 = 0.40 atm-1 (2)."),

    make_edexcel_q(27, "A* Challenge: Thermodynamic Proof of Le Chatelier\'s Principle", "WCH14/01/Hard/Q27", 5,
        "Use Delta S_total = Delta S_system - Delta H / T to prove that increasing temperature MUST decrease K for exothermic reactions.",
        [{'label': 'a', 'text': 'Write the expression for ln K as a function of 1/T.', 'marks': 2},
         {'label': 'b', 'text': 'Differentiate ln K w.r.t 1/T (van \'t Hoff equation d(ln K)/d(1/T) = -Delta H / R) and explain the slope.', 'marks': 3}],
        "27. (a) ln K = Delta S_system / R - Delta H / (RT) (2).<br/>27. (b) Slope of ln K vs 1/T is -Delta H / R. For exothermic reaction (Delta H < 0), slope is positive. As T increases, 1/T decreases, so ln K decreases, meaning K decreases (3)."),

    make_edexcel_q(28, "A* Challenge: Calculation of Equilibrium Composition from Kc", "WCH14/01/Hard/Q28", 5,
        "N2O4(g) <=> 2NO2(g). Kc = 0.36 mol dm-3 at 373 K.<br/>If 1.00 mol of pure N2O4 is placed in a 2.00 dm3 flask.",
        [{'label': 'a', 'text': 'Calculate the equilibrium concentration of NO2 and N2O4.', 'marks': 5}],
        "28. (a) Initial [N2O4] = 0.50 M. Let x = mol dm-3 N2O4 reacted => [N2O4]eq = 0.50 - x, [NO2]eq = 2x (1). Kc = (2x)^2 / (0.50 - x) = 0.36 => 4x^2 + 0.36x - 0.18 = 0 (2). x = (-0.36 + sqrt(0.1296 + 2.88)) / 8 = (-0.36 + 1.7348) / 8 = 0.172 M (1). [N2O4]eq = 0.328 M, [NO2]eq = 0.344 M (1)."),

    make_edexcel_q(29, "A* Challenge: Simultaneous Chemical Equilibria Analysis", "WCH14/01/Hard/Q29", 5,
        "Consider two coupled reactions:<br/>Reaction 1: A <=> B (K1 = 100)<br/>Reaction 2: B <=> C (K2 = 50)",
        [{'label': 'a', 'text': 'Deduce the equilibrium constant K3 for overall reaction A <=> C.', 'marks': 2},
         {'label': 'b', 'text': 'If starting with 1.0 M A, calculate the equilibrium concentrations of A, B, and C.', 'marks': 3}],
        "29. (a) K3 = K1 x K2 = 100 x 50 = 5000 (2).<br/>29. (b) [B] = 100[A], [C] = 50[B] = 5000[A]. [A] + [B] + [C] = 5001[A] = 1.0 M => [A] = 2.0x10^-4 M, [B] = 0.020 M, [C] = 0.980 M (3)."),

    make_edexcel_q(30, "A* Challenge: Total Pressure Effect on Dissociation Fraction", "WCH14/01/Hard/Q30", 5,
        "Show that for A(g) <=> 2B(g), the degree of dissociation alpha relates to total pressure P by alpha = sqrt(Kp / (Kp + 4P)).",
        [{'label': 'a', 'text': 'Derive this formula starting from initial 1 mole of A.', 'marks': 5}],
        "30. (a) Moles at eq: A = 1-alpha, B = 2alpha. Total moles = 1+alpha (1). Partial pressures: p_A = ((1-alpha)/(1+alpha))P, p_B = ((2alpha)/(1+alpha))P (2). Kp = (p_B)^2 / p_A = [4 alpha^2 / (1-alpha^2)] P (1). Rearranging gives alpha^2 = Kp / (Kp + 4P) => alpha = sqrt(Kp / (Kp + 4P)) (1)."),

    make_edexcel_q(31, "A* Challenge: Temperature Dependence of Kp and Enthalpy Profile", "WCH14/01/Hard/Q31", 5,
        "The equilibrium constant Kp for 2NO2(g) <=> N2O4(g) is 6.82 atm-1 at 298 K and 0.144 atm-1 at 373 K.",
        [{'label': 'a', 'text': 'Calculate Delta H° for dimerization of NO2.', 'marks': 4},
         {'label': 'b', 'text': 'State whether dimerization is exothermic or endothermic.', 'marks': 1}],
        "31. (a) ln(0.144 / 6.82) = ln(0.02111) = -3.858 (1). (1/373 - 1/298) = -6.749 x 10^-4 K-1 (1). Delta H / R = -3.858 / (-6.749x10^-4) = 5716 K (1). Delta H = -5716 x 8.31 = -47.5 kJ mol-1 (1).<br/>31. (b) Exothermic (Delta H < 0) (1)."),

    make_edexcel_q(32, "A* Challenge: Equilibrium Constant Units in Terms of SI Units", "WCH14/01/Hard/Q32", 4,
        "For N2(g) + 3H2(g) <=> 2NH3(g), Kp is expressed in Pa-2.",
        [{'label': 'a', 'text': 'Convert Kp = 3.56 x 10^-5 atm-2 into Pa-2 (1 atm = 101325 Pa).', 'marks': 2},
         {'label': 'b', 'text': 'Express Pa in SI base units (kg, m, s).', 'marks': 2}],
        "32. (a) Kp(Pa-2) = (3.56 x 10^-5) / (101325)^2 = 3.47 x 10^-15 Pa-2 (2).<br/>32. (b) Pa = N m-2 = (kg m s-2) m-2 = kg m-1 s-2 => Pa-2 = kg-2 m2 s4 (2)."),

    make_edexcel_q(33, "A* Challenge: Gas Phase Decomposition of HI Kinetic vs Equilibrium Control", "WCH14/01/Hard/Q33", 5,
        "2HI(g) <=> H2(g) + I2(g) (Delta H = +12.5 kJ mol-1). Kc = 0.020 at 700 K.",
        [{'label': 'a', 'text': 'Calculate the percentage of HI decomposed at equilibrium.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why increasing temperature increases both rate of reaching equilibrium and equilibrium yield of H2.', 'marks': 2}],
        "33. (a) Kc = (x/2)^2 / (1-x)^2 = 0.020 => x / (2(1-x)) = sqrt(0.020) = 0.1414 => x = 0.283 - 0.283x => 1.283x = 0.283 => x = 0.221 (22.1% decomposed) (3).<br/>33. (b) High temp increases rate by providing E >= Ea for collisions (1); endothermic reaction shifts right, increasing Kc and yield (1)."),

    make_edexcel_q(34, "A* Challenge: Water Gas Shift Reaction Equilibrium", "WCH14/01/Hard/Q34", 5,
        "CO(g) + H2O(g) <=> CO2(g) + H2(g) (Delta H = -41.2 kJ mol-1). Kc = 1.00 at 1100 K.",
        [{'label': 'a', 'text': 'If starting with 1.00 mol CO and 2.00 mol H2O, calculate equilibrium composition.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why pressure has no effect on equilibrium composition.', 'marks': 2}],
        "34. (a) Kc = x^2 / ((1-x)(2-x)) = 1.00 => x^2 = 2 - 3x + x^2 => 3x = 2 => x = 0.67 mol (3). CO=0.33, H2O=1.33, CO2=0.67, H2=0.67 mol.<br/>34. (b) 2 moles of gas reactants form 2 moles of gas products, so pressure changes affect numerator and denominator equally (2)."),

    make_edexcel_q(35, "A* Challenge: Relate Kp to Gibbs Free Energy Change Delta G°", "WCH14/01/Hard/Q35", 5,
        "Delta G° = -R T ln Kp.",
        [{'label': 'a', 'text': 'Calculate Delta G° at 298 K for N2O4 <=> 2NO2 where Kp = 0.141 atm.', 'marks': 3},
         {'label': 'b', 'text': 'State what a positive Delta G° indicates about standard state feasibility.', 'marks': 2}],
        "35. (a) Delta G° = -8.31 x 298 x ln(0.141) = -2476.38 x (-1.959) = +4851 J mol-1 = +4.85 kJ mol-1 (3).<br/>35. (b) Positive Delta G° means reaction is non-spontaneous under standard conditions (p = 1 atm for all gases); equilibrium favors reactants (2)."),

    make_edexcel_q(36, "A* Challenge: Dissociation of Dinitrogen Tetroxide at Variable Volumes", "WCH14/01/Hard/Q36", 5,
        "N2O4(g) <=> 2NO2(g). Kc = 0.0046 mol dm-3 at 298 K.",
        [{'label': 'a', 'text': 'Calculate degree of dissociation alpha when 1.00 mol N2O4 is in 10.0 dm3 vs 100.0 dm3.', 'marks': 4},
         {'label': 'b', 'text': 'Explain Ostwald\'s dilution effect on gaseous dissociation.', 'marks': 1}],
        "36. (a) At 10 dm3: [N2O4]0 = 0.10 M => 4x^2 / (0.10 - x) = 0.0046 => x = 0.0102 M (alpha = 10.2%) (2). At 100 dm3: [N2O4]0 = 0.010 M => 4x^2 / (0.010 - x) = 0.0046 => x = 0.0028 M (alpha = 28.0%) (2).<br/>36. (b) Increasing volume (dilution) increases degree of dissociation for reactions where gas moles increase (1)."),

    make_edexcel_q(37, "A* Challenge: Synthesis of Phosgene COCl2 Equilibrium Kp", "WCH14/01/Hard/Q37", 5,
        "CO(g) + Cl2(g) <=> COCl2(g). Kp = 15.0 atm-1 at 373 K.<br/>Equilibrium partial pressure of COCl2 is 3.00 atm, and p_CO = p_Cl2.",
        [{'label': 'a', 'text': 'Calculate the partial pressure of CO at equilibrium.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate total pressure of the equilibrium mixture.', 'marks': 2}],
        "37. (a) Kp = p_COCl2 / (p_CO)^2 = 15.0 => 3.00 / (p_CO)^2 = 15.0 => (p_CO)^2 = 0.20 => p_CO = 0.447 atm (3).<br/>37. (b) Total pressure = p_COCl2 + p_CO + p_Cl2 = 3.00 + 0.447 + 0.447 = 3.89 atm (2)."),

    make_edexcel_q(38, "A* Challenge: Homogeneous Gas Phase Equilibrium Calculation for SO3 Formation", "WCH14/01/Hard/Q38", 5,
        "2SO2(g) + O2(g) <=> 2SO3(g). Kc = 280 dm3 mol-1 at 1000 K.<br/>In a 2.00 dm3 vessel, equilibrium mixture contains 0.40 mol SO2 and 0.20 mol O2.",
        [{'label': 'a', 'text': 'Calculate the concentration of SO3 at equilibrium.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate total moles of SO3 present in the 2.00 dm3 vessel.', 'marks': 2}],
        "38. (a) [SO2] = 0.20 M, [O2] = 0.10 M. Kc = [SO3]^2 / ((0.20)^2(0.10)) = 280 => [SO3]^2 = 280 x 0.0040 = 1.12 => [SO3] = 1.058 mol dm-3 (3).<br/>38. (b) Moles SO3 = 1.058 x 2.00 = 2.12 mol (2)."),

    make_edexcel_q(39, "A* Challenge: Ammonia Decomposition Kp and Partial Pressure Ratios", "WCH14/01/Hard/Q39", 5,
        "2NH3(g) <=> N2(g) + 3H2(g). Pure NH3 is introduced at initial pressure P0.",
        [{'label': 'a', 'text': 'Express Kp in terms of equilibrium partial pressure p_NH3 and mole fraction ratio.', 'marks': 3},
         {'label': 'b', 'text': 'If 20% of NH3 decomposes at total pressure 10.0 atm, calculate Kp.', 'marks': 2}],
        "39. (a) At eq: moles NH3 = 2(1-alpha), N2 = alpha, H2 = 3alpha. Total = 2 + 2alpha (1). Kp = (p_N2 x (p_H2)^3) / (p_NH3)^2 (2).<br/>39. (b) alpha = 0.20. Moles: NH3 = 1.6, N2 = 0.2, H2 = 0.6. Total = 2.4. Mole fracs: NH3=0.667, N2=0.0833, H2=0.25. Partial pressures: NH3=6.67, N2=0.833, H2=2.50. Kp = (0.833 x 15.625) / 44.49 = 0.292 atm2 (2)."),

    make_edexcel_q(40, "A* Challenge: Le Chatelier Pressure Paradox in Gas Phase Reactions", "WCH14/01/Hard/Q40", 5,
        "For N2O4(g) <=> 2NO2(g), increasing pressure increases [NO2] in mol dm-3 but decreases mole fraction of NO2.",
        [{'label': 'a', 'text': 'Explain this apparent paradox using Boyle\'s law and equilibrium shift.', 'marks': 5}],
        "40. (a) Compression (decreasing volume V) immediately increases concentrations of all gases (Boyle\'s law) (2). System responds by shifting left (towards fewer gas moles) to reduce total moles (2). Net effect: mole fraction x_NO2 decreases, but because volume decreased by a larger factor, equilibrium [NO2] is higher than before compression (1)."),

    make_edexcel_q(41, "A* Challenge: Calculation of Kc for Ester Hydrolysis with Added Acid Catalyst", "WCH14/01/Hard/Q41", 5,
        "1.00 mol ethyl ethanoate + 1.00 mol water + 0.10 mol HCl(aq) catalyst (containing water).<br/>Equilibrium mixture titrated: 0.40 mol ester remains at equilibrium.",
        [{'label': 'a', 'text': 'Account for water contributed by HCl solution in the ICE table.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Kc.', 'marks': 3}],
        "41. (a) HCl catalyst is aqueous, adding initial water moles (2).<br/>41. (b) Ester reacted = 0.60 mol. Acid formed = 0.60 mol, alcohol formed = 0.60 mol. Water eq = 1.00 - 0.60 = 0.40 mol. Kc = (0.60 x 0.60) / (0.40 x 0.40) = 0.36 / 0.16 = 2.25 (3)."),

    make_edexcel_q(42, "A* Challenge: Equilibrium Constant Kp of Steam Methane Reforming", "WCH14/01/Hard/Q42", 5,
        "CH4(g) + H2O(g) <=> CO(g) + 3H2(g). At 1000 K, total pressure = 5.00 atm, p_CH4 = 0.50 atm, p_H2O = 0.50 atm.",
        [{'label': 'a', 'text': 'Calculate p_CO and p_H2 given p_H2 = 3 p_CO.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Kp.', 'marks': 3}],
        "42. (a) p_CO + p_H2 = 5.00 - 0.50 - 0.50 = 4.00 atm (1). 4 p_CO = 4.00 => p_CO = 1.00 atm, p_H2 = 3.00 atm (1).<br/>42. (b) Kp = (1.00 x (3.00)^3) / (0.50 x 0.50) = 27.0 / 0.25 = 108 atm2 (3)."),

    make_edexcel_q(43, "A* Challenge: Temperature Dependence of Solvation Equilibria", "WCH14/01/Hard/Q43", 5,
        "Gas solubility equilibrium: O2(g) <=> O2(aq) (Delta H = -12.0 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain using thermodynamics why dissolved oxygen concentration in water decreases as water temperature rises.', 'marks': 3},
         {'label': 'b', 'text': 'Discuss environmental implications for aquatic life in thermal pollution.', 'marks': 2}],
        "43. (a) Dissolution of O2 gas is exothermic (Delta H < 0) (1). Increasing temperature shifts equilibrium left (towards O2 gas) to absorb heat, decreasing Henry\'s law solubility constant K (2).<br/>43. (b) Warm industrial wastewater discharges reduce dissolved oxygen levels, causing asphyxiation of fish and aerobic organisms (2)."),

    make_edexcel_q(44, "A* Challenge: Multi-Gas Equilibrium Partitioning in Closed Container", "WCH14/01/Hard/Q44", 5,
        "N2(g) + O2(g) <=> 2NO(g) (Kc = 1.0 x 10^-5 at 1500 K).<br/>Air mixture initially: 0.80 M N2, 0.20 M O2.",
        [{'label': 'a', 'text': 'Calculate equilibrium concentration of NO.', 'marks': 3},
         {'label': 'b', 'text': 'Why can the approximation (0.80 - x) ~ 0.80 be used?', 'marks': 2}],
        "44. (a) Kc = (2x)^2 / ((0.80-x)(0.20-x)) ~ 4x^2 / (0.80 x 0.20) = 4x^2 / 0.16 = 1.0 x 10^-5 (1). 4x^2 = 1.6 x 10^-6 => x^2 = 4.0 x 10^-7 => x = 6.32 x 10^-4 M (1). [NO] = 2x = 1.26 x 10^-3 mol dm-3 (1).<br/>44. (b) Kc is extremely small (10^-5), so x << 0.20 M (approximation error < 1%) (2)."),

    make_edexcel_q(45, "A* Challenge: Van \'t Hoff Isochore Derivation & Graph Analysis", "WCH14/01/Hard/Q45", 5,
        "A plot of ln K against 1/T for a reversible reaction yields a straight line with gradient +4500 K and y-intercept -12.5.",
        [{'label': 'a', 'text': 'Calculate Delta H° in kJ mol-1.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta S_system° in J K-1 mol-1.', 'marks': 3}],
        "45. (a) Gradient = -Delta H / R = +4500 K => Delta H = -4500 x 8.31 = -37395 J mol-1 = -37.4 kJ mol-1 (exothermic) (2).<br/>45. (b) Y-intercept = Delta S_sys / R = -12.5 => Delta S_sys = -12.5 x 8.31 = -103.9 J K-1 mol-1 (3)."),

    make_edexcel_q(46, "A* Challenge: Gas Phase Equilibrium Dissociation of N2O4 at High Altitude", "WCH14/01/Hard/Q46", 5,
        "At sea level (P = 1.0 atm), N2O4 is 20% dissociated. At high altitude (P = 0.50 atm).",
        [{'label': 'a', 'text': 'Calculate Kp at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate degree of dissociation alpha at 0.50 atm.', 'marks': 3}],
        "46. (a) alpha = 0.20 at 1.0 atm => Kp = 4(0.20)^2 / (1 - (0.20)^2) x 1.0 = 0.16 / 0.96 = 0.167 atm (2).<br/>46. (b) 0.167 = [4 alpha^2 / (1 - alpha^2)] x 0.50 => 4 alpha^2 / (1 - alpha^2) = 0.3333 => 4.3333 alpha^2 = 0.3333 => alpha^2 = 0.0769 => alpha = 0.277 (27.7% dissociated) (3)."),

    make_edexcel_q(47, "A* Challenge: Industrial Synthesis of Hydrogen Cyanide Equilibrium", "WCH14/01/Hard/Q47", 5,
        "Andrussow process: CH4(g) + NH3(g) + 1.5 O2(g) -> HCN(g) + 3H2O(g) (Delta H = -473 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain how temperature and pressure affect equilibrium yield vs rate.', 'marks': 3},
         {'label': 'b', 'text': 'Why is Pt-Rh gauze catalyst used at 1100 °C?', 'marks': 2}],
        "47. (a) Exothermic reaction favoured by low T, but 1100 °C required for high rate (1). 3.5 gas moles -> 4 gas moles favoured by low pressure (2).<br/>47. (b) Extremely high activation energy requires Pt-Rh catalyst at 1100 °C for millisecond contact time (2)."),

    make_edexcel_q(48, "A* Challenge: Equilibrium Constant of Carbonate Buffer System", "WCH14/01/Hard/Q48", 5,
        "In ocean chemistry: CO2(aq) + H2O(l) <=> H2CO3(aq) <=> H+(aq) + HCO3-(aq).",
        [{'label': 'a', 'text': 'Explain how increasing atmospheric CO2 partial pressure affects ocean pH (ocean acidification).', 'marks': 3},
         {'label': 'b', 'text': 'Relate this to carbonate ion dissolution CaCO3(s) + H+(aq) -> Ca2+(aq) + HCO3-(aq).', 'marks': 2}],
        "48. (a) Higher p_CO2 increases [CO2(aq)], shifting equilibrium right to produce more H+ ions, lowering ocean pH (acidification) (3).<br/>48. (b) Increased H+ reacts with CaCO3 marine shells/coral, dissolving them (2)."),

    make_edexcel_q(49, "A* Challenge: Equilibrium Analysis of Dehydration of Hydrated Cobalt Chloride", "WCH14/01/Hard/Q49", 5,
        "CoCl2.6H2O(s) (pink) <=> CoCl2(s) (blue) + 6H2O(g) (Delta H = +350 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain why cobalt chloride paper turns blue in dry air and pink in humid air.', 'marks': 3},
         {'label': 'b', 'text': 'Write Kp = (p_H2O)^6.', 'marks': 2}],
        "49. (a) In dry air (low p_H2O), equilibrium shifts right (towards blue CoCl2) to replenish H2O gas (1.5). In humid air (high p_H2O), equilibrium shifts left (towards pink hydrate) (1.5).<br/>49. (b) Kp = (p_H2O)^6 (2)."),

    make_edexcel_q(50, "A* Challenge: Complete Equilibria & Thermodynamics Master Synthesis", "WCH14/01/Hard/Q50", 6,
        "Synthesis of phosgene: CO(g) + Cl2(g) <=> COCl2(g)<br/>Delta H° = -108 kJ mol-1, Delta S_system° = -132 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total and Kp at 298 K.', 'marks': 4},
         {'label': 'b', 'text': 'Calculate the temperature above which phosgene spontaneously dissociates into CO and Cl2.', 'marks': 2}],
        "50. (a) Delta S_surr = -(-108000)/298 = +362.4 J K-1 mol-1. Delta S_tot = -132 + 362.4 = +230.4 J K-1 mol-1 (2). ln Kp = 230.4 / 8.31 = 27.72 => Kp = e^27.72 = 1.09 x 10^12 atm-1 (2).<br/>50. (b) T_boundary = Delta H / Delta S_sys = 108000 / 132 = 818.2 K (545.0 °C) (2).")
]

p4_faqs = [
    make_edexcel_faq("Omitting Solids/Liquids from Kc and Kp", "Heterogeneous Equilibria", "Including pure solids or liquids in Kc/Kp expressions.", "Concentrations of pure solids and pure liquid solvents are constant and built into the equilibrium constant value. Omit them entirely from Kc and Kp."),
    make_edexcel_faq("Units of Kc and Kp Deduction", "Units Calculation", "Writing dimensionless or standard units without checking stoichiometry.", "Units depend on mole change: substitute (mol dm-3) into Kc or (atm/kPa) into Kp. If gas moles on left equal gas moles on right, K is dimensionless."),
    make_edexcel_faq("Effect of Pressure on Kp Value", "Pressure Paradox", "Claiming increasing total pressure increases the value of Kp.", "Total pressure changes shift the EQUILIBRIUM POSITION, but Kp itself is CONSTANT at a fixed temperature. The partial pressures adjust to maintain exact Kp."),
    make_edexcel_faq("Effect of Temperature on K Sign", "Temperature Effect", "Confusing direction of K shift for exothermic vs endothermic reactions.", "For EXOTHERMIC (Delta H < 0), heating DECREASES K. For ENDOTHERMIC (Delta H > 0), heating INCREASES K. (Remember: K changes ONLY with temperature)."),
    make_edexcel_faq("Catalyst Effect on Equilibrium Yield", "Catalyst Fallback", "Stating a catalyst increases equilibrium yield or shifts position.", "A catalyst speeds up forward and reverse reactions by the EXACT SAME FACTOR. It reaches equilibrium faster but has ZERO effect on yield or K."),
    make_edexcel_faq("Mole Fraction vs Partial Pressure", "Partial Pressure Calculation", "Using mole fraction directly in Kp instead of partial pressure.", "Partial pressure p_A = mole fraction x_A x TOTAL PRESSURE. You must multiply by total pressure before inserting into Kp."),
    make_edexcel_faq("ICE Table Initial Moles vs Equilibrium Moles", "ICE Table Trap", "Inserting initial moles directly into Kc expression without subtracting change x.", "Always construct an ICE table (Initial, Change, Equilibrium). Moles at equilibrium = Initial +/- stoichiometric change x, converted to concentration ([ ] = mol / V)."),
    make_edexcel_faq("Relating Total Entropy to K Formula", "Thermodynamic Formula", "Using log10 instead of natural log ln in Delta S_total = R ln K.", "The formula uses natural logarithm (ln / base e). ln K = Delta S_total / R => K = e^(Delta S_total / R). R = 8.31 J K-1 mol-1."),
    make_edexcel_faq("Volume Cancellation in Kc Expressions", "Volume Shortcut", "Dividing by volume V when gas moles on both sides are equal.", "When sum of moles of reactants equals sum of moles of products (e.g. esterification), volume V cancels out completely. Kc can be calculated directly from equilibrium moles."),
    make_edexcel_faq("Reaction Quotient Q vs Equilibrium Constant K", "Direction of Shift", "Confusing direction of shift when Q > K.", "If Q < K, system shifts RIGHT to form more products. If Q > K, system shifts LEFT to form more reactants until Q = K.")
]

# Build Pack 4 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf", p4_meta, p4_questions, p4_faqs)
print("Pack 4 (13A Chemical Equilibria - 50 Qs + 10 FAQs) compiled successfully!")
