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
# PACK 1: 11A — FURTHER KINETICS (50 Qs + 10 FAQs)
# ==========================================
p1_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 11',
    'topic_name': 'KINETICS 2',
    'subtopic_code': '11A',
    'subtopic_name': 'Further Kinetics (Rates, Orders, Mechanisms & Arrhenius)'
}

p1_questions = [
    make_edexcel_q(1, "Continuous Monitoring of Reaction Rate", "WCH14/01/Jan23/Q1", 4,
        "The reaction between magnesium ribbon and dilute hydrochloric acid was investigated:<br/>Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)",
        [{'label': 'a', 'text': 'State the most suitable experimental method to continuously monitor the rate of this reaction and explain your choice.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how the initial rate of reaction is determined from the gas volume vs time graph.', 'marks': 2}],
        "1. (a) Measure volume of H2 gas using a gas syringe over time (1). H2 is the only gas produced while reactants are solid/liquid (1).<br/>1. (b) Draw a tangent to the curve at t = 0 seconds (1). Calculate gradient of tangent = Change in volume / Change in time (1).",
        diagram_img="diagrams/p1_q1_mg_hcl.png"),
    
    make_edexcel_q(2, "Colorimetric Measurement of Reaction Rate", "WCH14/01/Oct22/Q2", 3,
        "Propanone reacts with iodine in the presence of an acid catalyst:<br/>CH3COCH3(aq) + I2(aq) + H+(aq) -> CH3COCH2I(aq) + 2H+(aq) + I-(aq)",
        [{'label': 'a', 'text': 'Explain how colorimetry can be used to follow the progress of this reaction.', 'marks': 2},
         {'label': 'b', 'text': 'State why colorimetry is preferred over titrametric quenching in this experiment.', 'marks': 1}],
        "2. (a) Iodine is brown/yellow while all other species are colourless (1). Absorbance decreases proportionally as iodine is consumed (1).<br/>2. (b) Allows continuous non-destructive monitoring without disturbing the reaction mixture (1).",
        diagram_img="diagrams/p1_q2_propanone_i2.png"),
    
    make_edexcel_q(3, "Quenching and Titrimetry", "WCH14/01/Jun22/Q3", 4,
        "The alkaline hydrolysis of ethyl ethanoate is represented by:<br/>CH3COOCH2CH3(aq) + OH-(aq) -> CH3COO-(aq) + CH3CH2OH(aq)",
        [{'label': 'a', 'text': 'Explain why quenching is necessary before titrating samples taken from this reaction mixture.', 'marks': 2},
         {'label': 'b', 'text': 'Suggest a suitable quenching method for this reaction.', 'marks': 2}],
        "3. (a) Quenching halts or drastically slows the reaction (1) so OH- concentration does not continue to change during titration (1).<br/>3. (b) Pipette sample into ice-cold water (1) or add a known excess of ice-cold acid (1)."),

    make_edexcel_q(4, "Electrical Conductivity Method", "WCH14/01/Jan22/Q4", 3,
        "The bromination of propanone produces H+ and Br- ions:<br/>CH3COCH3 + Br2 + H+ -> CH3COCH2Br + 2H+ + Br-",
        [{'label': 'a', 'text': 'Explain why electrical conductivity increases as the reaction proceeds.', 'marks': 2},
         {'label': 'b', 'text': 'State how conductivity data is converted into rate data.', 'marks': 1}],
        "4. (a) Number of mobile ions increases from 1 mole to 3 moles of ions (2 H+ and 1 Br-) (1); H+ has exceptionally high ionic mobility (1).<br/>4. (b) Plot conductivity vs time and find the gradient at t=0 (1)."),

    make_edexcel_q(5, "Rate Equation and Rate Constant Units", "WCH14/01/Oct21/Q1", 3,
        "A reaction A + 2B -> C has the rate equation: rate = k[A][B]^2",
        [{'label': 'a', 'text': 'State the order of reaction with respect to A, B, and the overall order.', 'marks': 2},
         {'label': 'b', 'text': 'Deduce the units of the rate constant, k.', 'marks': 1}],
        "5. (a) Order w.r.t A = 1, w.r.t B = 2 (1); Overall order = 1 + 2 = 3 (1).<br/>5. (b) units of k = (mol dm-3 s-1) / ((mol dm-3)(mol dm-3)^2) = dm6 mol-2 s-1 (1)."),

    make_edexcel_q(6, "Zero Order Kinetics Definition", "WCH14/01/Jun21/Q2", 2,
        "The rate equation for a reaction X -> Y is rate = k[X]^0",
        [{'label': 'a', 'text': 'Explain what zero order with respect to reactant X implies about the reaction mechanism.', 'marks': 1},
         {'label': 'b', 'text': 'Describe the shape of the concentration-time graph for a zero-order reaction.', 'marks': 1}],
        "6. (a) X is not involved in the rate-determining step (1).<br/>6. (b) Straight line with constant negative gradient (1).",
        diagram_img="diagrams/p1_q6_zero_order_conctime.png"),

    make_edexcel_q(7, "First Order Half-Life Relationship", "WCH14/01/Jan21/Q3", 3,
        "The decomposition of hydrogen peroxide 2H2O2 -> 2H2O + O2 is first order.",
        [{'label': 'a', 'text': 'Define half-life (t1/2) for a chemical reaction.', 'marks': 1},
         {'label': 'b', 'text': 'Explain how the concentration-time graph confirms that a reaction is first order.', 'marks': 2}],
        "7. (a) Time taken for the concentration of a reactant to fall to half its initial value (1).<br/>7. (b) The half-life is constant (1) regardless of the starting concentration (1).",
        diagram_img="diagrams/p1_q7_first_order_halflife.png"),

    make_edexcel_q(8, "Calculation of Rate Constant from Half-Life", "WCH14/01/Oct20/Q4", 3,
        "For a first-order decomposition reaction, the half-life t1/2 is 450 seconds.",
        [{'label': 'a', 'text': 'Calculate the rate constant, k, using t1/2 = ln 2 / k. Include units.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the rate when [reactant] = 0.080 mol dm-3.', 'marks': 1}],
        "8. (a) k = 0.69315 / 450 = 1.54 x 10^-3 s-1 (2).<br/>8. (b) rate = (1.54 x 10^-3)(0.080) = 1.23 x 10^-4 mol dm-3 s-1 (1)."),

    make_edexcel_q(9, "Initial Rates Method: Deduction of Orders", "WCH14/01/Jun20/Q5", 4,
        "Initial rate data for 2NO(g) + O2(g) -> 2NO2(g):<br/>Exp 1: [NO]=0.010, [O2]=0.010, Rate=1.4x10^-4<br/>Exp 2: [NO]=0.020, [O2]=0.010, Rate=5.6x10^-4<br/>Exp 3: [NO]=0.010, [O2]=0.030, Rate=4.2x10^-4",
        [{'label': 'a', 'text': 'Deduce the order w.r.t NO and O2 with full reasoning.', 'marks': 3},
         {'label': 'b', 'text': 'Write the overall rate equation.', 'marks': 1}],
        "9. (a) Exp 1->2: [NO] x2, [O2] constant -> Rate x4 (2^2) => 2nd order w.r.t NO (2). Exp 1->3: [O2] x3, [NO] constant -> Rate x3 (3^1) => 1st order w.r.t O2 (1).<br/>9. (b) rate = k[NO]^2[O2] (1)."),

    make_edexcel_q(10, "Calculation of Rate Constant k from Experimental Table", "WCH14/01/Jan20/Q6", 3,
        "Using data from Q9 (Exp 1: [NO]=0.010, [O2]=0.010, Rate=1.4x10^-4 mol dm-3 s-1):",
        [{'label': 'a', 'text': 'Calculate the value of the rate constant, k.', 'marks': 2},
         {'label': 'b', 'text': 'State the units of k.', 'marks': 1}],
        "10. (a) k = (1.4x10^-4) / ((0.010)^2(0.010)) = 14000 dm6 mol-2 s-1 (2).<br/>10. (b) dm6 mol-2 s-1 (1)."),

    make_edexcel_q(11, "Rate-Determining Step Deduction from Rate Equation", "WCH14/01/Oct19/Q7", 4,
        "The reaction NO2(g) + CO(g) -> NO(g) + CO2(g) has rate = k[NO2]^2.",
        [{'label': 'a', 'text': 'Explain why CO does not appear in the rate equation.', 'marks': 2},
         {'label': 'b', 'text': 'Propose a two-step mechanism consistent with this rate equation.', 'marks': 2}],
        "11. (a) CO is not involved in the rate-determining step (RDS) or acts in a fast step after RDS (2).<br/>11. (b) Step 1: NO2 + NO2 -> NO3 + NO (slow) (1). Step 2: NO3 + CO -> NO2 + CO2 (fast) (1)."),

    make_edexcel_q(12, "Catalysis & Rate Equation Inclusion", "WCH14/01/Jun19/Q8", 3,
        "In the acid-catalysed reaction of propanone with iodine, rate = k[CH3COCH3][H+].",
        [{'label': 'a', 'text': 'Explain why H+ appears in the rate equation despite being a catalyst.', 'marks': 2},
         {'label': 'b', 'text': 'State the order with respect to iodine.', 'marks': 1}],
        "12. (a) H+ is a homogeneous catalyst involved in the rate-determining step (2).<br/>12. (b) Zero order w.r.t I2 (1)."),

    make_edexcel_q(13, "Initial Rates Table with Fractional / Higher Orders", "WCH14/01/Jan19/Q9", 4,
        "Reaction: A + B -> C<br/>Exp 1: [A]=0.20, [B]=0.20, Rate=2.0x10^-3<br/>Exp 2: [A]=0.40, [B]=0.20, Rate=8.0x10^-3<br/>Exp 3: [A]=0.20, [B]=0.40, Rate=2.0x10^-3",
        [{'label': 'a', 'text': 'Deduce the order with respect to A and B.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate k including units.', 'marks': 1}],
        "13. (a) Exp 1->2: [A] x2, Rate x4 -> 2nd order w.r.t A (2). Exp 1->3: [B] x2, Rate unchanged -> 0 order w.r.t B (1).<br/>13. (b) k = (2.0x10^-3) / (0.20)^2 = 0.050 dm3 mol-1 s-1 (1)."),

    make_edexcel_q(14, "Multi-Step Mechanism Validation", "WCH14/01/Sample/Q14", 4,
        "Consider the reaction: 2H2 + 2NO -> N2 + 2H2O<br/>Proposed mechanism:<br/>Step 1: 2NO -> N2O2 (fast)<br/>Step 2: N2O2 + H2 -> N2O + H2O (slow)<br/>Step 3: N2O + H2 -> N2 + H2O (fast)",
        [{'label': 'a', 'text': 'Deduce the rate equation predicted by this mechanism.', 'marks': 3},
         {'label': 'b', 'text': 'Identify any intermediate species.', 'marks': 1}],
        "14. (a) From Step 1 equilibrium: [N2O2] = K[NO]^2 (1). Step 2 is RDS: rate = k2[N2O2][H2] (1). Substitute [N2O2]: rate = k[NO]^2[H2] (1).<br/>14. (b) Intermediates: N2O2 and N2O (1)."),

    make_edexcel_q(15, "Rate-Concentration Graph Summary", "WCH14/01/Sample/Q15", 3,
        "Distinguish between Zero, 1st, and 2nd order Rate vs Concentration graphs.",
        [{'label': 'a', 'text': 'Sketch and describe the Rate vs [A] graphs for 0, 1st, and 2nd order.', 'marks': 3}],
        "15. (a) Zero order: Horizontal line (rate independent of [A]) (1). 1st order: Straight line through origin (rate proportional to [A]) (1). 2nd order: Parabolic curve upwards (rate proportional to [A]^2) (1)."),

    make_edexcel_q(16, "Hydrolysis of Tertiary Halogenoalkanes Mechanism", "WCH14/01/Sample/Q16", 4,
        "The hydrolysis of (CH3)3CBr with NaOH is first order overall: rate = k[(CH3)3CBr].",
        [{'label': 'a', 'text': 'Explain why OH- does not appear in the rate equation (SN1 mechanism).', 'marks': 2},
         {'label': 'b', 'text': 'Write the equation for the rate-determining step.', 'marks': 2}],
        "16. (a) Hydrolysis proceeds via SN1 mechanism where heterolytic fission of C-Br bond to form carbocation is slow (1). Nucleophilic attack by OH- occurs in a fast step (1).<br/>16. (b) (CH3)3CBr -> (CH3)3C+ + Br- (slow) (2)."),

    make_edexcel_q(17, "Hydrolysis of Primary Halogenoalkanes Mechanism", "WCH14/01/Sample/Q17", 4,
        "The hydrolysis of CH3CH2Br with NaOH is second order overall: rate = k[CH3CH2Br][OH-].",
        [{'label': 'a', 'text': 'Explain why this reaction follows an SN2 mechanism.', 'marks': 2},
         {'label': 'b', 'text': 'Describe the transition state formed during the rate-determining step.', 'marks': 2}],
        "17. (a) Both CH3CH2Br and OH- are involved in the single rate-determining step (2).<br/>17. (b) Five-coordinate transition state (1) with partial C...OH bond formation and partial C...Br bond cleavage (1)."),

    make_edexcel_q(18, "Effect of Temperature on Rate Constant k", "WCH14/01/Sample/Q18", 3,
        "As temperature increases from 298 K to 308 K, the rate of a reaction doubles.",
        [{'label': 'a', 'text': 'Explain why a small increase in temperature causes a large increase in rate.', 'marks': 2},
         {'label': 'b', 'text': 'State the relationship between temperature and the rate constant k.', 'marks': 1}],
        "18. (a) Significantly larger fraction of molecules have energy E >= Ea (Maxwell-Boltzmann distribution) (2).<br/>18. (b) Rate constant k increases exponentially with temperature (1)."),

    make_edexcel_q(19, "Arrhenius Equation Formulation", "WCH14/01/Sample/Q19", 3,
        "The Arrhenius equation is k = A e^(-Ea / RT).",
        [{'label': 'a', 'text': 'State the meaning of terms A, Ea, R, and T.', 'marks': 2},
         {'label': 'b', 'text': 'Write the logarithmic form of the Arrhenius equation (ln k vs 1/T).', 'marks': 1}],
        "19. (a) A = pre-exponential frequency factor, Ea = activation energy (J mol-1), R = gas constant (8.31 J K-1 mol-1), T = temperature in Kelvin (2).<br/>19. (b) ln k = -Ea / (RT) + ln A (1)."),

    make_edexcel_q(20, "Arrhenius Plot Graphical Analysis: N2O5 Decomposition", "WCH14/01/Oct19/Q8", 5,
        "Data for the decomposition of N2O5 yielded an Arrhenius plot of ln k against 1/T with a straight line gradient of -11000 K.",
        [{'label': 'a', 'text': 'Calculate the activation energy, Ea, in kJ mol-1. (R = 8.31 J K-1 mol-1)', 'marks': 3},
         {'label': 'b', 'text': 'If the y-intercept is +29.4, calculate the pre-exponential factor A.', 'marks': 2}],
        "20. (a) Gradient = -Ea / R = -11000 K (1). Ea = 11000 x 8.31 = 91410 J mol-1 (1) = +91.4 kJ mol-1 (1).<br/>20. (b) ln A = 29.4 => A = e^29.4 = 5.86 x 10^12 s-1 (2).",
        diagram_img="diagrams/p1_q20_arrhenius_n2o5.png"),

    make_edexcel_q(21, "Heterogeneous Catalysis Surface Adsorption", "WCH14/01/Sample/Q21", 3,
        "In the Haber process: N2(g) + 3H2(g) -> 2NH3(g) using an iron catalyst.",
        [{'label': 'a', 'text': 'Describe the steps involved in heterogeneous catalysis on the iron surface.', 'marks': 3}],
        "21. (a) Adsorption of N2 and H2 onto active sites on iron surface (1); weakening of N=N and H-H bonds (1); reaction forms NH3 followed by desorption of NH3 product (1)."),

    make_edexcel_q(22, "Homogeneous Catalysis Mechanism: Fe2+ and S2O8^2-", "WCH14/01/Sample/Q22", 4,
        "The reaction S2O8^2- + 2I- -> 2SO4^2- + I2 is catalysed by Fe2+(aq) ions.",
        [{'label': 'a', 'text': 'Explain why the uncatalysed reaction between S2O8^2- and I- has a high activation energy.', 'marks': 1},
         {'label': 'b', 'text': 'Write two ionic equations showing how Fe2+ acts as a catalyst.', 'marks': 3}],
        "22. (a) High activation energy due to electrostatic repulsion between two negatively charged ions (1).<br/>22. (b) Step 1: S2O8^2- + 2Fe2+ -> 2SO4^2- + 2Fe3+ (2). Step 2: 2Fe3+ + 2I- -> 2Fe2+ + I2 (1)."),

    make_edexcel_q(23, "Maxwell-Boltzmann Temperature Shift Analysis", "WCH14/01/Sample/Q23", 4,
        "The diagram shows Maxwell-Boltzmann distributions at T1 (300 K) and T2 (320 K).",
        [{'label': 'a', 'text': 'Explain why the peak shifts to the right and lowers at higher temperature.', 'marks': 2},
         {'label': 'b', 'text': 'Shade and explain the area representing molecules with E >= Ea at T2.', 'marks': 2}],
        "23. (a) Total number of molecules remains constant (area under curve equal) (1); average kinetic energy increases, spreading the distribution (1).<br/>23. (b) Area to the right of Ea line is significantly greater at T2, resulting in a much higher frequency of successful collisions (2).",
        diagram_img="diagrams/p1_q23_maxwell_boltzmann_temp.png"),

    make_edexcel_q(24, "Autocatalysis Mechanism: MnO4- and C2O4^2-", "WCH14/01/Sample/Q24", 4,
        "The reaction between acidified KMnO4 and ethanedioic acid (H2C2O4) is autocatalysed by Mn2+.",
        [{'label': 'a', 'text': 'Define autocatalysis.', 'marks': 1},
         {'label': 'b', 'text': 'Describe the rate of reaction over time (sigmoidal rate profile).', 'marks': 3}],
        "24. (a) Autocatalysis is when one of the products of the reaction acts as a catalyst for the reaction (1).<br/>24. (b) Initially slow due to repulsion between MnO4- and C2O4^2- (1); rate speeds up rapidly as Mn2+ catalyst is generated (1); rate slows down near completion as reactants are exhausted (1)."),

    make_edexcel_q(25, "Maxwell-Boltzmann Catalysed Activation Energy Barrier", "WCH14/01/Sample/Q25", 3,
        "A catalyst lowers activation energy from Ea(uncat) to Ea(cat).",
        [{'label': 'a', 'text': 'Explain using a Maxwell-Boltzmann curve how a catalyst increases reaction rate without changing temperature.', 'marks': 3}],
        "25. (a) Catalyst provides an alternative pathway with lower activation energy Ea(cat) (1). Position of Ea line shifts left (1). A larger fraction of molecules have E >= Ea(cat), increasing successful collision frequency (1)."),

    # Tier 2 A* Challenge Questions (Q26 - Q50)
    make_edexcel_q(26, "A* Challenge: Two-Point Arrhenius Activation Energy Calculation", "WCH14/01/Hard/Q26", 5,
        "Rate constants for a reaction were measured at two temperatures:<br/>At T1 = 300 K, k1 = 2.50 x 10^-4 s-1.<br/>At T2 = 340 K, k2 = 1.25 x 10^-2 s-1.<br/>(R = 8.31 J K-1 mol-1)",
        [{'label': 'a', 'text': 'Use ln(k2/k1) = (Ea/R)(1/T1 - 1/T2) to calculate the activation energy Ea in kJ mol-1.', 'marks': 4},
         {'label': 'b', 'text': 'Calculate the pre-exponential factor A at 300 K.', 'marks': 1}],
        "26. (a) ln(1.25x10^-2 / 2.50x10^-4) = ln(50) = 3.912 (1). (1/300 - 1/340) = 3.922 x 10^-4 K-1 (1). Ea/R = 3.912 / 3.922x10^-4 = 9975 K (1). Ea = 9975 x 8.31 = 82.9 kJ mol-1 (1).<br/>26. (b) A = k / e^(-Ea/RT) = (2.50x10^-4) / e^(-82890/(8.31x300)) = 6.64 x 10^10 s-1 (1)."),

    make_edexcel_q(27, "A* Challenge: Deduction of Complex Rate Equation from Mechanism", "WCH14/01/Hard/Q27", 5,
        "Reaction: 2A + B -> C + D<br/>Proposed Mechanism:<br/>Step 1: A + A <=> A2 (fast equilibrium, K1)<br/>Step 2: A2 + B -> C + E (slow, rate constant k2)<br/>Step 3: E -> D (fast)",
        [{'label': 'a', 'text': 'Deduce the overall rate equation in terms of [A] and [B].', 'marks': 3},
         {'label': 'b', 'text': 'State the overall order and units of the rate constant k.', 'marks': 2}],
        "27. (a) Step 2 is RDS: rate = k2[A2][B] (1). From Step 1 equilibrium: [A2] = K1[A]^2 (1). Substitute: rate = k2 K1 [A]^2 [B] = k[A]^2[B] (1).<br/>27. (b) Overall order = 3 (1). Units of k = dm6 mol-2 s-1 (1)."),

    make_edexcel_q(28, "A* Challenge: Initial Rates Table with 3 Reactants", "WCH14/01/Hard/Q28", 5,
        "Initial rate data for A + B + C -> Products:<br/>Exp 1: [A]=0.10, [B]=0.10, [C]=0.10, Rate=1.5x10^-3<br/>Exp 2: [A]=0.20, [B]=0.10, [C]=0.10, Rate=6.0x10^-3<br/>Exp 3: [A]=0.10, [B]=0.30, [C]=0.10, Rate=4.5x10^-3<br/>Exp 4: [A]=0.10, [B]=0.10, [C]=0.20, Rate=1.5x10^-3",
        [{'label': 'a', 'text': 'Determine the order w.r.t A, B, and C with full mathematical justification.', 'marks': 4},
         {'label': 'b', 'text': 'Calculate k including units.', 'marks': 1}],
        "28. (a) Exp 1->2: [A] x2, Rate x4 => 2nd order w.r.t A (1). Exp 1->3: [B] x3, Rate x3 => 1st order w.r.t B (1). Exp 1->4: [C] x2, Rate unchanged => 0 order w.r.t C (1). Rate equation = k[A]^2[B] (1).<br/>28. (b) k = (1.5x10^-3) / ((0.10)^2(0.10)) = 1.50 dm6 mol-2 s-1 (1)."),

    make_edexcel_q(29, "A* Challenge: Half-Life Determination for 2nd Order Kinetics", "WCH14/01/Hard/Q29", 5,
        "For a second-order reaction 2A -> B, rate = k[A]^2 where k = 0.40 dm3 mol-1 s-1.",
        [{'label': 'a', 'text': 'Show that the half-life for a second-order reaction is given by t1/2 = 1 / (k[A]0).', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the first half-life when [A]0 = 0.50 mol dm-3 and the second half-life as [A] falls from 0.25 to 0.125 mol dm-3.', 'marks': 2}],
        "29. (a) Integrated 2nd order rate law: 1/[A] - 1/[A]0 = k t (1). At t = t1/2, [A] = [A]0/2 => 2/[A]0 - 1/[A]0 = k t1/2 (1) => t1/2 = 1 / (k[A]0) (1).<br/>29. (b) 1st t1/2 = 1 / (0.40 x 0.50) = 5.0 s (1). 2nd t1/2 = 1 / (0.40 x 0.25) = 10.0 s (1). Half-life doubles as concentration halves."),

    make_edexcel_q(30, "A* Challenge: Arrhenius Graph Data Interpretation with Table", "WCH14/01/Hard/Q30", 5,
        "Experimental data for reaction rate constant k at various temperatures T:<br/>T=290K (1/T=0.00345, ln k=-8.25)<br/>T=310K (1/T=0.00323, ln k=-5.80)<br/>T=330K (1/T=0.00303, ln k=-3.58)<br/>T=350K (1/T=0.00286, ln k=-1.68)",
        [{'label': 'a', 'text': 'Calculate the gradient of the ln k vs 1/T line.', 'marks': 2},
         {'label': 'b', 'text': 'Determine the activation energy, Ea, in kJ mol-1 and pre-exponential factor A.', 'marks': 3}],
        "30. (a) Gradient = (-1.68 - (-8.25)) / (0.00286 - 0.00345) = 6.57 / (-0.00059) = -11135 K (2).<br/>30. (b) Ea = 11135 x 8.31 = 92530 J mol-1 = +92.5 kJ mol-1 (2). ln A = -1.68 + (11135 x 0.00286) = 30.16 => A = e^30.16 = 1.25 x 10^13 s-1 (1)."),

    make_edexcel_q(31, "A* Challenge: Iodine Clock Reaction Kinetics (Persulfate & Iodide)", "WCH14/01/Hard/Q31", 5,
        "In an iodine clock reaction: S2O8^2- + 2I- -> 2SO4^2- + I2<br/>Fixed amount of Na2S2O3 and starch indicator added. Time t taken for blue-black colour to appear is recorded.",
        [{'label': 'a', 'text': 'Explain why 1/t can be used as a measure of initial rate of reaction.', 'marks': 2},
         {'label': 'b', 'text': 'State the role of Na2S2O3 in the clock reaction.', 'marks': 2},
         {'label': 'c', 'text': 'Why must the amount of Na2S2O3 be small relative to reactants?', 'marks': 1}],
        "31. (a) 1/t is proportional to rate because the amount of I2 produced to reach the blue-black endpoint is constant (2).<br/>31. (b) Thiosulfate reacts immediately with I2 as it forms: 2S2O3^2- + I2 -> S4O6^2- + 2I- (1), delaying the appearance of starch-iodine blue-black colour (1).<br/>31. (c) Ensures initial rate is measured before significant reactant depletion (1)."),

    make_edexcel_q(32, "A* Challenge: Gas Volume Kinetics Data Analysis", "WCH14/01/Hard/Q32", 5,
        "Decomposition of benzenediazonium chloride: C6H5N2Cl(aq) -> C6H5Cl(l) + N2(g)<br/>At t=0s (V=0cm3), t=100s (V=18cm3), t=200s (V=32cm3), t=infinity (V=58cm3).",
        [{'label': 'a', 'text': 'Calculate (V_inf - V_t) at t=0, 100, and 200 s, which is proportional to reactant concentration.', 'marks': 2},
         {'label': 'b', 'text': 'Prove that the reaction is first order by calculating constant half-life or rate constants.', 'marks': 3}],
        "32. (a) At t=0: 58 - 0 = 58 cm3 (1). At t=100: 58 - 18 = 40 cm3. At t=200: 58 - 32 = 26 cm3 (1).<br/>32. (b) k1 = (1/100) ln(58/40) = 0.00372 s-1 (1). k2 = (1/200) ln(58/26) = 0.00401 s-1 (1). k is approximately constant => 1st order kinetics (1)."),

    make_edexcel_q(33, "A* Challenge: Acid-Catalysed Hydrolysis Rate Law & Solvent Excess", "WCH14/01/Hard/Q33", 5,
        "The hydrolysis of methyl ethanoate in large excess of water:<br/>CH3COOCH3 + H2O -> CH3COOH + CH3OH (catalysed by H+).<br/>Overall rate law: rate = k\' [CH3COOCH3][H2O][H+].",
        [{'label': 'a', 'text': 'Explain why the reaction behaves as pseudo-first order w.r.t methyl ethanoate.', 'marks': 3},
         {'label': 'b', 'text': 'Relate the observed rate constant k_obs to k\', [H2O], and [H+].', 'marks': 2}],
        "33. (a) [H2O] is in large excess so its concentration remains effectively constant (1). [H+] is a catalyst so its concentration is constant (1). Therefore rate = k_obs [CH3COOCH3] where k_obs = k\' [H2O][H+] (1).<br/>33. (b) k_obs = k\' [H2O][H+] (2)."),

    make_edexcel_q(34, "A* Challenge: Boltzmann Distribution & Activation Energy Shift", "WCH14/01/Hard/Q34", 5,
        "A reaction has Ea = 100 kJ mol-1. Rate doubles when temperature increases from 300 K to 310 K.",
        [{'label': 'a', 'text': 'Use the Arrhenius equation to calculate the exact ratio of rate constants k310 / k300.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why the fraction of collisions with E >= Ea increases more significantly for high Ea reactions.', 'marks': 2}],
        "34. (a) ln(k310/k300) = (100000/8.31) * (1/300 - 1/310) = 12033.7 * (0.0001075) = 1.294 (2). k310/k300 = e^1.294 = 3.65 (1).<br/>34. (b) High Ea sits far out on the tail of the Boltzmann curve where the relative percentage increase in area under curve upon heating is largest (2)."),

    make_edexcel_q(35, "A* Challenge: Initial Rates with Stoichiometry Considerations", "WCH14/01/Hard/Q35", 5,
        "For 2A + 3B -> C + 2D, the rate of disappearance of A is 4.0 x 10^-3 mol dm-3 s-1.",
        [{'label': 'a', 'text': 'Calculate the rate of disappearance of B and the rate of formation of C and D.', 'marks': 3},
         {'label': 'b', 'text': 'Define reaction rate in terms of d[C]/dt.', 'marks': 2}],
        "35. (a) -d[B]/dt = 1.5 x (-d[A]/dt) = 6.0 x 10^-3 mol dm-3 s-1 (1). d[C]/dt = 0.5 x 4.0x10^-3 = 2.0 x 10^-3 mol dm-3 s-1 (1). d[D]/dt = 4.0 x 10^-3 mol dm-3 s-1 (1).<br/>35. (b) Overall rate = d[C]/dt = -1/2 d[A]/dt = -1/3 d[B]/dt = 1/2 d[D]/dt (2)."),

    make_edexcel_q(36, "A* Challenge: Homogeneous Catalysis Mechanism of S2O8^2- and I-", "WCH14/01/Hard/Q36", 5,
        "The reaction S2O8^2- + 2I- -> 2SO4^2- + I2 is catalysed by Fe3+(aq) ions.",
        [{'label': 'a', 'text': 'Write two step-wise equations showing how Fe3+ acts as a catalyst.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why catalysis by Fe3+ is faster than the uncatalysed reaction.', 'marks': 2}],
        "36. (a) Step 1: 2Fe3+ + 2I- -> 2Fe2+ + I2 (2). Step 2: 2Fe2+ + S2O8^2- -> 2Fe3+ + 2SO4^2- (1).<br/>36. (b) Both steps involve reaction between oppositely charged ions (Fe3+ and I-, Fe2+ and S2O8^2-) which attract, whereas uncatalysed reaction is between two negatively charged ions (S2O8^2- and I-) which repel (2)."),

    make_edexcel_q(37, "A* Challenge: Rate Law Determination from Multi-Step Mechanism with Fast Pre-Equilibrium", "WCH14/01/Hard/Q37", 5,
        "Mechanism:<br/>Step 1: A + B <=> AB (fast equilibrium, K1 = [AB]/([A][B]))<br/>Step 2: AB + A -> A2B (slow, k2)",
        [{'label': 'a', 'text': 'Deduce the rate equation.', 'marks': 3},
         {'label': 'b', 'text': 'What is the order w.r.t A and B?', 'marks': 2}],
        "37. (a) RDS is Step 2: rate = k2[AB][A] (1). From Step 1 equilibrium: [AB] = K1[A][B] (1). Substitute: rate = k2 K1 [A]^2 [B] = k[A]^2[B] (1).<br/>37. (b) Order w.r.t A = 2, w.r.t B = 1 (2)."),

    make_edexcel_q(38, "A* Challenge: Arrhenius Activation Energy from Arrhenius Equation Ratio", "WCH14/01/Hard/Q38", 5,
        "If a reaction rate triples (k2/k1 = 3.0) when temperature increases from 298 K to 318 K, calculate Ea.",
        [{'label': 'a', 'text': 'Calculate Ea in kJ mol-1 using R = 8.31 J K-1 mol-1.', 'marks': 5}],
        "38. (a) ln(3.0) = 1.0986 (1). 1/T1 - 1/T2 = (1/298 - 1/318) = 3.3556 x 10^-4 K-1 (1). Ea/R = 1.0986 / 3.3556x10^-4 = 3273.9 K (2). Ea = 3273.9 x 8.31 = 27206 J mol-1 = +27.2 kJ mol-1 (1)."),

    make_edexcel_q(39, "A* Challenge: Colorimetry Calibration Curve & Kinetics Data Analysis", "WCH14/01/Hard/Q39", 5,
        "A colorimeter was calibrated using standard iodine solutions. Absorbance A was proportional to [I2].<br/>At t=0s (A=1.00), t=200s (A=0.70), t=400s (A=0.40), t=600s (A=0.10).",
        [{'label': 'a', 'text': 'Deduce the order w.r.t I2 from the constant rate of decrease of absorbance.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the rate of reaction in absorbance units per second.', 'marks': 2}],
        "39. (a) Absorbance decreases linearly over equal time intervals (Delta A = 0.30 every 200 s) (2). Constant rate independent of concentration => Zero order w.r.t I2 (1).<br/>39. (b) Rate = 0.30 / 200 = 1.50 x 10^-3 a.u. s-1 (2)."),

    make_edexcel_q(40, "A* Challenge: Quenching Kinetics of Ester Alkaline Hydrolysis", "WCH14/01/Hard/Q40", 5,
        "Samples of 25.0 cm3 of a hydrolysing ethyl ethanoate mixture were quenched in ice-cold water and titrated with 0.100 M HCl.<br/>t=0 min: V_HCl = 24.0 cm3; t=10 min: V_HCl = 16.0 cm3; t=20 min: V_HCl = 12.0 cm3; t=40 min: V_HCl = 8.0 cm3.",
        [{'label': 'a', 'text': 'Calculate [OH-] at each time.', 'marks': 2},
         {'label': 'b', 'text': 'Show that the reaction is second order overall (1st order in ester, 1st order in OH-).', 'marks': 3}],
        "40. (a) [OH-] is proportional to V_HCl: t=0: 0.096 M; t=10: 0.064 M; t=20: 0.048 M; t=40: 0.032 M (2).<br/>40. (b) Plot 1/[OH-] vs time: t=0 (10.4), t=10 (15.6), t=20 (20.8), t=40 (31.3). Straight line plot confirms 2nd order kinetics (3)."),

    make_edexcel_q(41, "A* Challenge: Integrated Rate Law Calculation for 1st Order Kinetics", "WCH14/01/Hard/Q41", 5,
        "The first-order decomposition of N2O5 has k = 3.38 x 10^-5 s-1 at 298 K.<br/>Initial concentration [N2O5]0 = 0.500 mol dm-3.",
        [{'label': 'a', 'text': 'Calculate [N2O5] remaining after 5.00 hours (18000 s).', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the percentage of N2O5 decomposed after 5.00 hours.', 'marks': 2}],
        "41. (a) ln([N2O5]t / 0.500) = -k t = -(3.38x10^-5)(18000) = -0.6084 (2). [N2O5]t = 0.500 x e^-0.6084 = 0.272 mol dm-3 (1).<br/>41. (b) Decomposed = 0.500 - 0.272 = 0.228 M. Percentage = (0.228 / 0.500) x 100% = 45.6% (2)."),

    make_edexcel_q(42, "A* Challenge: Temperature Coefficient Q10 Calculation", "WCH14/01/Hard/Q42", 5,
        "The temperature coefficient Q10 is the factor by which rate increases for a 10 K rise in temperature.<br/>For a reaction with Ea = 50 kJ mol-1 between 298 K and 308 K.",
        [{'label': 'a', 'text': 'Calculate Q10 = k308 / k298 using the Arrhenius equation.', 'marks': 4},
         {'label': 'b', 'text': 'Why is Q10 approximately equal to 2 for many reactions near room temperature?', 'marks': 1}],
        "42. (a) ln(k308/k298) = (50000 / 8.31) x (1/298 - 1/308) = 6016.8 x (1.0888x10^-4) = 0.6551 (3). Q10 = e^0.6551 = 1.93 (1).<br/>42. (b) For reactions with Ea ~ 50-60 kJ mol-1, a 10 K rise doubles the fraction of molecules with E >= Ea (1)."),

    make_edexcel_q(43, "A* Challenge: Continuous Pressure Measurement Kinetics of Gas Phase Reaction", "WCH14/01/Hard/Q43", 5,
        "Decomposition of azomethane: CH3N2CH3(g) -> C2H6(g) + N2(g)<br/>Initial pressure P0 = 200 mmHg. Total pressure P_total at time t: t=0 (200), t=100s (250), t=200s (287.5), t=inf (400).",
        [{'label': 'a', 'text': 'Express partial pressure of azomethane P_azo in terms of P0 and P_total.', 'marks': 2},
         {'label': 'b', 'text': 'Show that the reaction is first order by half-life analysis of P_azo.', 'marks': 3}],
        "43. (a) CH3N2CH3 -> C2H6 + N2. At time t: P_azo = P0 - x, P_total = P0 + x => x = P_total - P0 => P_azo = 2P0 - P_total (2).<br/>43. (b) At t=0: P_azo = 200. At t=100: P_azo = 400 - 250 = 150. At t=200: P_azo = 400 - 287.5 = 112.5. Constant t1/2 = 240 s => 1st order (3)."),

    make_edexcel_q(44, "A* Challenge: Initial Rates Deduction with Fractional Orders", "WCH14/01/Hard/Q44", 5,
        "Reaction: CHCl3(g) + Cl2(g) -> CCl4(g) + HCl(g)<br/>Exp 1: [CHCl3]=0.10, [Cl2]=0.10, Rate=1.0x10^-4<br/>Exp 2: [CHCl3]=0.20, [Cl2]=0.10, Rate=2.0x10^-4<br/>Exp 3: [CHCl3]=0.10, [Cl2]=0.40, Rate=2.0x10^-4",
        [{'label': 'a', 'text': 'Deduce the order w.r.t CHCl3 and Cl2 (note: Cl2 order is 0.5).', 'marks': 4},
         {'label': 'b', 'text': 'Write the rate equation.', 'marks': 1}],
        "44. (a) Exp 1->2: [CHCl3] x2, Rate x2 => 1st order w.r.t CHCl3 (2). Exp 1->3: [Cl2] x4, Rate x2 (4^0.5) => 0.5 order w.r.t Cl2 (2).<br/>44. (b) rate = k[CHCl3][Cl2]^0.5 (1)."),

    make_edexcel_q(45, "A* Challenge: Multi-Step Mechanism Derivation with Intermediate Steady State", "WCH14/01/Hard/Q45", 5,
        "Ozone decomposition: 2O3 -> 3O2<br/>Step 1: O3 <=> O2 + O (fast equilibrium, K1)<br/>Step 2: O + O3 -> 2O2 (slow, k2)",
        [{'label': 'a', 'text': 'Deduce the rate equation rate = k [O3]^2 [O2]^-1.', 'marks': 4},
         {'label': 'b', 'text': 'Explain what negative order w.r.t O2 signifies.', 'marks': 1}],
        "45. (a) Step 2 is RDS: rate = k2[O][O3] (1). From Step 1 equilibrium: [O] = K1 [O3] / [O2] (2). Substitute: rate = k2 K1 [O3]^2 / [O2] = k [O3]^2 [O2]^-1 (1).<br/>45. (b) O2 acts as an inhibitor by driving the reverse of Step 1 (1)."),

    make_edexcel_q(46, "A* Challenge: Arrhenius Activation Energy Bar Graph & Energy Profile Comparison", "WCH14/01/Hard/Q46", 5,
        "Compare the activation energy profile of uncatalysed vs catalysed decomposition of H2O2.",
        [{'label': 'a', 'text': 'Draw an enthalpy profile diagram for exothermic decomposition 2H2O2 -> 2H2O + O2 showing Ea(uncat) and Ea(cat).', 'marks': 3},
         {'label': 'b', 'text': 'Explain how I- ions act as a homogeneous catalyst via IO- intermediate.', 'marks': 2}],
        "46. (a) Reactants (2H2O2) higher energy than products (2H2O + O2) (1); uncatalysed single high hump Ea(uncat) = 75 kJ mol-1 (1); catalysed two lower humps Ea(cat) = 56 kJ mol-1 (1).<br/>46. (b) Step 1: H2O2 + I- -> H2O + IO- (slow) (1). Step 2: H2O2 + IO- -> H2O + O2 + I- (fast) (1)."),

    make_edexcel_q(47, "A* Challenge: Arrhenius Line Plot with Experimental Errors", "WCH14/01/Hard/Q47", 5,
        "An Arrhenius plot for the hydrolysis of ethyl ethanoate has a slope of -5800 K.",
        [{'label': 'a', 'text': 'Calculate Ea in kJ mol-1.', 'marks': 2},
         {'label': 'b', 'text': 'Discuss how a +/- 1.0 K error in temperature measurement affects the calculated Ea at high vs low temperatures.', 'marks': 3}],
        "47. (a) Ea = 5800 x 8.31 = 48200 J mol-1 = +48.2 kJ mol-1 (2).<br/>47. (b) Since 1/T is non-linear, a 1 K error at low temperature (e.g. 280 K) produces a larger absolute error in 1/T than at high temperature (e.g. 350 K) (3)."),

    make_edexcel_q(48, "A* Challenge: Clock Reaction Order Determination via Variable Initial Concentrations", "WCH14/01/Hard/Q48", 5,
        "In a persulfate clock reaction, varying [I-] while keeping [S2O8^2-] constant gave times t: [I-]=0.05 M (t=160s), [I-]=0.10 M (t=80s), [I-]=0.20 M (t=40s).",
        [{'label': 'a', 'text': 'Calculate initial rates (1/t) and deduce the order w.r.t I-.', 'marks': 3},
         {'label': 'b', 'text': 'Predict the time t if [I-] = 0.15 M.', 'marks': 2}],
        "48. (a) 1/t = 0.00625, 0.0125, 0.0250. Doubling [I-] doubles rate (1/t) => 1st order w.r.t I- (3).<br/>48. (b) Rate is proportional to [I-]: t = 80 x (0.10 / 0.15) = 53.3 s (2)."),

    make_edexcel_q(49, "A* Challenge: Complex Reaction Mechanism with Enzyme Michaelis-Menten Kinetics", "WCH14/01/Hard/Q49", 5,
        "Enzyme kinetics: E + S <=> ES (fast equilibrium) -> E + P (slow, k2).",
        [{'label': 'a', 'text': 'Explain why at low [S], reaction is 1st order w.r.t S, but at high [S], reaction becomes 0 order w.r.t S.', 'marks': 3},
         {'label': 'b', 'text': 'Define Vmax and Km.', 'marks': 2}],
        "49. (a) At low [S], active sites are available so rate = k2 [ES] ∝ [S] (1st order) (1.5). At high [S], all enzyme active sites are saturated so [ES] = [E]total (constant), making rate independent of [S] (0 order) (1.5).<br/>49. (b) Vmax = maximum rate at saturation; Km = substrate concentration at half Vmax (2)."),

    make_edexcel_q(50, "A* Challenge: Complete Rate Law, Mechanism & Arrhenius Synthesis", "WCH14/01/Hard/Q50", 6,
        "The gas-phase reaction 2NO2 + F2 -> 2NO2F was investigated.<br/>Exp data: 1st order in NO2, 1st order in F2.<br/>At 300 K, k = 0.80 dm3 mol-1 s-1; at 350 K, k = 12.0 dm3 mol-1 s-1.",
        [{'label': 'a', 'text': 'Write the rate equation.', 'marks': 1},
         {'label': 'b', 'text': 'Propose a valid two-step mechanism.', 'marks': 2},
         {'label': 'c', 'text': 'Calculate the activation energy Ea in kJ mol-1.', 'marks': 3}],
        "50. (a) rate = k[NO2][F2] (1).<br/>50. (b) Step 1: NO2 + F2 -> NO2F + F (slow, RDS) (1). Step 2: NO2 + F -> NO2F (fast) (1).<br/>50. (c) ln(12.0 / 0.80) = ln(15) = 2.708 (1). (1/300 - 1/350) = 4.762x10^-4 K-1 (1). Ea = (2.708 / 4.762x10^-4) x 8.31 = 47.3 kJ mol-1 (1).")
]

p1_faqs = [
    make_edexcel_faq("Units of Rate Constant k", "Calculation Trap", "Using mol dm-3 s-1 for k regardless of overall order.", "Substitute units into rate equation: units of k = (mol dm-3 s-1) / (mol dm-3)^n. For 1st order: s-1; 2nd order: dm3 mol-1 s-1; 3rd order: dm6 mol-2 s-1."),
    make_edexcel_faq("Arrhenius Temperature in Kelvin", "Units Trap", "Inserting temperature in Celsius into the Arrhenius equation.", "Always convert temperature to Kelvin (K = °C + 273.15). Using Celsius leads to negative or nonsense activation energy values."),
    make_edexcel_faq("Activation Energy Units (kJ vs J)", "Conversion Trap", "Forgetting to multiply/divide by 1000 when R = 8.31 J K-1 mol-1 is used.", "R is given in Joules (J K-1 mol-1). The gradient -Ea/R yields Ea in J mol-1. Divide by 1000 to express final Ea in kJ mol-1."),
    make_edexcel_faq("Zero Order Reactants in Rate Equation", "Mechanism Trap", "Including zero-order reactants in the rate equation.", "Zero-order reactants have rate ∝ [X]^0 = 1. Omit them from the rate equation completely, but note they participate after the RDS."),
    make_edexcel_faq("Rate-Determining Step (RDS) Identification", "Theory Trap", "Including species formed in fast steps AFTER the RDS in the rate equation.", "The rate equation only contains species present in or before the rate-determining step. Products of fast subsequent steps do not appear."),
    make_edexcel_faq("Constant Half-Life Significance", "Graph Interpretation", "Assuming constant half-life applies to zero or second order reactions.", "ONLY first-order reactions have a constant half-life independent of initial concentration (t1/2 = ln 2 / k)."),
    make_edexcel_faq("Initial Rate Method Gradient Tangent", "Practical Skills", "Drawing tangents at non-zero times when calculating initial rate.", "Initial rate MUST be determined by drawing a tangent at t = 0 seconds (when zero product has accumulated)."),
    make_edexcel_faq("Quenching Reaction Samples", "Practical Technique", "Titrating samples directly without quenching first.", "Quenching (ice-cold water/acid) halts or drastically slows the reaction so concentration does not change during titration."),
    make_edexcel_faq("Catalysts in Rate Equations", "Homogeneous Catalysts", "Excluding homogeneous catalysts from the rate equation.", "Homogeneous catalysts ARE involved in the rate-determining step and DO appear in the rate equation (e.g. H+ in acid-catalysed esterification)."),
    make_edexcel_faq("Gradient of Arrhenius Plot", "Graph Analysis", "Setting gradient equal to -Ea instead of -Ea/R.", "On a plot of ln k against 1/T, gradient = -Ea / R. Therefore Ea = -gradient x 8.31 J K-1 mol-1.")
]

# Build Pack 1 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf", p1_meta, p1_questions, p1_faqs)
print("Pack 1 (11A Further Kinetics - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 2: 12A — ENTROPY (50 Qs + 10 FAQs)
# ==========================================
p2_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 12',
    'topic_name': 'ENTROPY AND ENERGETICS',
    'subtopic_code': '12A',
    'subtopic_name': 'Entropy (System, Surroundings & Total Entropy)'
}

p2_questions = [
    make_edexcel_q(1, "Definition of System Entropy", "WCH14/01/Jan23/Q5", 3,
        "Entropy is a measure of the degree of disorder of a system.",
        [{'label': 'a', 'text': 'Define entropy, S, at a molecular level.', 'marks': 1},
         {'label': 'b', 'text': 'Predict, with a reason, whether entropy increases or decreases for: H2O(l) -> H2O(g).', 'marks': 2}],
        "1. (a) Measure of the number of ways of arranging energy/particles in a system (disorder) (1).<br/>1. (b) Increases (1). Gas molecules have higher kinetic energy and far more random arrangements than liquid (1)."),

    make_edexcel_q(2, "Standard System Entropy Calculation: Haber Process", "WCH14/01/Oct22/Q6", 4,
        "Calculate Delta S_system for: N2(g) + 3H2(g) -> 2NH3(g)<br/>Standard entropies S° (J K-1 mol-1): N2(g)=191.6, H2(g)=130.6, NH3(g)=192.3",
        [{'label': 'a', 'text': 'Calculate Delta S_system in J K-1 mol-1.', 'marks': 3},
         {'label': 'b', 'text': 'Explain the sign of Delta S_system in terms of number of gas moles.', 'marks': 1}],
        "2. (a) Sum S°(products) = 2 x 192.3 = 384.6 (1). Sum S°(reactants) = 191.6 + 3(130.6) = 583.4 (1). Delta S_sys = 384.6 - 583.4 = -198.8 J K-1 mol-1 (1).<br/>2. (b) Negative because 4 moles of gas react to form 2 moles of gas -> decrease in disorder (1)."),

    make_edexcel_q(3, "Surroundings Entropy Calculation", "WCH14/01/Jun22/Q7", 3,
        "For N2(g) + 3H2(g) -> 2NH3(g), Delta H = -92.2 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_surroundings at 298 K using Delta S_surr = -Delta H / T.', 'marks': 2},
         {'label': 'b', 'text': 'State the units of Delta S_surroundings.', 'marks': 1}],
        "3. (a) Delta S_surr = -(-92200 J mol-1) / 298 K = +309.4 J K-1 mol-1 (2).<br/>3. (b) J K-1 mol-1 (1)."),

    make_edexcel_q(4, "Total Entropy and Feasibility Criterion", "WCH14/01/Jan22/Q8", 3,
        "For N2(g) + 3H2(g) -> 2NH3(g) at 298 K, Delta S_system = -198.8 J K-1 mol-1 and Delta S_surroundings = +309.4 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K.', 'marks': 1},
         {'label': 'b', 'text': 'State the criterion for a reaction to be spontaneous/feasible and deduce whether this reaction is spontaneous at 298 K.', 'marks': 2}],
        "4. (a) Delta S_total = -198.8 + 309.4 = +110.6 J K-1 mol-1 (1).<br/>4. (b) Spontaneous when Delta S_total > 0 (1). Yes, feasible because +110.6 > 0 (1)."),

    make_edexcel_q(5, "Effect of Temperature on Feasibility", "WCH14/01/Oct21/Q5", 4,
        "For N2(g) + 3H2(g) -> 2NH3(g), Delta H = -92.2 kJ mol-1 and Delta S_system = -198.8 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 500 K.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why increasing temperature makes this reaction less spontaneous.', 'marks': 2}],
        "5. (a) At 500 K: Delta S_surr = -(-92200) / 500 = +184.4 J K-1 mol-1. Delta S_total = -198.8 + 184.4 = -14.4 J K-1 mol-1 (2).<br/>5. (b) As T increases, Delta S_surroundings (-Delta H / T) becomes less positive, making Delta S_total negative (2)."),

    make_edexcel_q(6, "Minimum Temperature of Feasibility Calculation", "WCH14/01/Jun21/Q6", 4,
        "Thermal decomposition of CaCO3(s) -> CaO(s) + CO2(g): Delta H = +178 kJ mol-1, Delta S_system = +161 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate the minimum temperature T_min at which this reaction becomes spontaneous (Delta S_total >= 0).', 'marks': 4}],
        "6. (a) At feasibility boundary: Delta S_total = 0 => Delta S_surroundings = -Delta S_system = -161 J K-1 mol-1 (1). -Delta H / T = -161 => -178000 / T = -161 (1). T = 178000 / 161 = 1105.6 K (2)."),

    make_edexcel_q(7, "Entropy of Dissolution: Ammonium Nitrate", "WCH14/01/Jan21/Q7", 4,
        "NH4NO3(s) -> NH4+(aq) + NO3-(aq) is endothermic (Delta H = +25.7 kJ mol-1) but dissolves spontaneously at 298 K.",
        [{'label': 'a', 'text': 'Explain in terms of Delta S_system why NH4NO3 dissolves spontaneously.', 'marks': 2},
         {'label': 'b', 'text': 'If Delta S_system = +108.7 J K-1 mol-1, calculate Delta S_total at 298 K.', 'marks': 2}],
        "7. (a) Solid ionic lattice breaks down into free mobile hydrated ions, creating a large increase in disorder (Delta S_system > 0) (2).<br/>7. (b) Delta S_surr = -25700 / 298 = -86.24 J K-1 mol-1. Delta S_total = +108.7 - 86.24 = +22.46 J K-1 mol-1 (2)."),

    make_edexcel_q(8, "Relating Total Entropy to Equilibrium Constant K", "WCH14/01/Oct20/Q6", 3,
        "The total entropy change for a reaction is Delta S_total = R ln K.",
        [{'label': 'a', 'text': 'Calculate K when Delta S_total = +22.46 J K-1 mol-1 at 298 K. (R = 8.31 J K-1 mol-1)', 'marks': 2},
         {'label': 'b', 'text': 'State what K > 1 implies about the position of equilibrium.', 'marks': 1}],
        "8. (a) ln K = Delta S_total / R = 22.46 / 8.31 = 2.7028 (1). K = e^2.7028 = 14.9 (1).<br/>8. (b) Equilibrium lies predominantly to the right (products favoured) (1)."),

    make_edexcel_q(9, "Third Law of Thermodynamics & Absolute Zero Entropy", "WCH14/01/Jun20/Q8", 2,
        "At 0 K, a perfect crystalline substance has S = 0 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Explain why entropy is zero at absolute zero (0 K).', 'marks': 2}],
        "9. (a) At 0 K, all molecular translational, rotational, and vibrational motion ceases (1). There is only 1 microstate / zero disorder (1)."),

    make_edexcel_q(10, "Qualitative Entropy Changes Across States of Matter", "WCH14/01/Jan20/Q9", 4,
        "Predict whether Delta S_system is positive or negative for:<br/>(i) H2O(s) -> H2O(l)<br/>(ii) 2SO2(g) + O2(g) -> 2SO3(g)<br/>(iii) C(s) + O2(g) -> CO2(g)<br/>(iv) NaCl(s) -> Na+(aq) + Cl-(aq)",
        [{'label': 'a', 'text': 'Give the sign of Delta S_system for each reaction with a brief reason.', 'marks': 4}],
        "10. (a) (i) Positive (solid to liquid) (1). (ii) Negative (3 mol gas to 2 mol gas) (1). (iii) Approximately zero / slightly positive (1 mol gas to 1 mol gas) (1). (iv) Positive (lattice breaks into mobile hydrated ions) (1)."),

    make_edexcel_q(11, "Entropy of Combustion of Methane", "WCH14/01/Oct19/Q10", 4,
        "CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l): Delta H = -890 kJ mol-1, Delta S_system = -242 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_surroundings at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta S_total and explain why methane combustion is highly spontaneous.', 'marks': 2}],
        "11. (a) Delta S_surr = -(-890000) / 298 = +2986.6 J K-1 mol-1 (2).<br/>11. (b) Delta S_total = -242 + 2986.6 = +2744.6 J K-1 mol-1 (1). Extremely positive Delta S_total makes combustion overwhelming spontaneous (1)."),

    make_edexcel_q(12, "Entropy vs Kinetic Inertness: Diamond to Graphite Conversion", "WCH14/01/Jun19/Q11", 3,
        "C(diamond) -> C(graphite): Delta H = -1.9 kJ mol-1, Delta S_system = +3.3 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K and prove the conversion is thermodynamically spontaneous.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why diamonds do not noticeably convert to graphite at room temperature.', 'marks': 1}],
        "12. (a) Delta S_surr = -(-1900) / 298 = +6.38 J K-1 mol-1. Delta S_total = +3.3 + 6.38 = +9.68 J K-1 mol-1 > 0 (spontaneous) (2).<br/>12. (b) High activation energy due to breaking strong covalent C-C bonds makes the reaction kinetically inert (1)."),

    make_edexcel_q(13, "Entropy of Evaporation of Water vs Ethanol", "WCH14/01/Jan19/Q12", 4,
        "Trouton's rule states that Delta S_vapourisation is approximately +85 to +90 J K-1 mol-1 for many liquids.",
        [{'label': 'a', 'text': 'Explain why Delta S_vapourisation is similar for most simple liquids.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why water has a higher Delta S_vapourisation (+109 J K-1 mol-1) than predicted by Trouton\'s rule.', 'marks': 2}],
        "13. (a) Boiling represents transition from a disordered liquid to an ideal gas with similar disorder increase for 1 mole (2).<br/>13. (b) Liquid water has an unusually ordered hydrogen-bonded network. Breaking this ordered structure requires extra entropy gain (2)."),

    make_edexcel_q(14, "Calculating Standard Entropies from Experimental Data Table", "WCH14/01/Sample/Q14", 4,
        "Reaction: 2NaHCO3(s) -> Na2CO3(s) + CO2(g) + H2O(g)<br/>S° values (J K-1 mol-1): NaHCO3(s)=102, Na2CO3(s)=136, CO2(g)=214, H2O(g)=189",
        [{'label': 'a', 'text': 'Calculate Delta S_system.', 'marks': 3},
         {'label': 'b', 'text': 'Explain the large positive sign of Delta S_system.', 'marks': 1}],
        "14. (a) Sum S°(products) = 136 + 214 + 189 = 539 J K-1 mol-1 (1). Sum S°(reactants) = 2 x 102 = 204 J K-1 mol-1 (1). Delta S_sys = 539 - 204 = +335 J K-1 mol-1 (1).<br/>14. (b) 2 moles of solid produce 1 mole of solid and 2 moles of gas (2 gas moles formed) (1)."),

    make_edexcel_q(15, "Graphical Plot of Entropy S° vs Temperature T", "WCH14/01/Sample/Q15", 4,
        "A graph of standard entropy S° against temperature T from 0 K to 400 K shows two sharp vertical discontinuities.",
        [{'label': 'a', 'text': 'Identify what occurs at these two vertical jumps.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why Delta S_vapourisation is larger than Delta S_fusion.', 'marks': 2}],
        "15. (a) Melting point (solid to liquid) and boiling point (liquid to gas) phase changes (2).<br/>15. (b) Gas phase has vastly greater disorder and volume expansion than liquid phase compared to minor disorder change from solid to liquid (2).",
        diagram_img="diagrams/p2_q15_entropy_vs_temp.png"),

    make_edexcel_q(16, "Endothermic Spontaneous Reactions", "WCH14/01/Sample/Q16", 3,
        "Ba(OH)2.8H2O(s) + 2NH4Cl(s) -> BaCl2(s) + 2NH3(g) + 10H2O(l) is strongly endothermic (Delta H = +164 kJ mol-1).",
        [{'label': 'a', 'text': 'Explain how an endothermic reaction can occur spontaneously at room temperature.', 'marks': 3}],
        "16. (a) 3 moles of solid produce 1 mole of solid, 2 moles of gas, and 10 moles of liquid (huge increase in particles/disorder) (1). Delta S_system is extremely positive (1). Delta S_system > |Delta S_surroundings|, so Delta S_total > 0 (1)."),

    make_edexcel_q(17, "Solubility Trends and Entropy of Hydration", "WCH14/01/Sample/Q17", 4,
        "Dissolving MgSO4 in water is exothermic (Delta H = -91 kJ mol-1), whereas BaSO4 is insoluble.",
        [{'label': 'a', 'text': 'Explain how cation charge density affects Delta S_hydration and Delta S_system.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta S_surroundings for MgSO4 dissolution at 298 K.', 'marks': 2}],
        "17. (a) Mg2+ has higher charge density than Ba2+, causing stronger ordering of surrounding water molecules (-S_hyd) (2).<br/>17. (b) Delta S_surr = -(-91000) / 298 = +305.4 J K-1 mol-1 (2)."),

    make_edexcel_q(18, "Thermodynamic Equilibrium Constant Derivation from Entropy", "WCH14/01/Sample/Q18", 4,
        "At equilibrium, Delta S_total = 0 for the universe, leading to Delta S_total = R ln K.",
        [{'label': 'a', 'text': 'Deduce the expression for ln K in terms of Delta H and Delta S_system.', 'marks': 2},
         {'label': 'b', 'text': 'If Delta S_total = +50.0 J K-1 mol-1 at 298 K, calculate K.', 'marks': 2}],
        "18. (a) Delta S_total = Delta S_system - Delta H / T = R ln K => ln K = Delta S_system / R - Delta H / (RT) (2).<br/>18. (b) ln K = 50.0 / 8.31 = 6.0169 => K = e^6.0169 = 410.3 (2)."),

    make_edexcel_q(19, "Temperature Dependence of K via van 't Hoff and Entropy", "WCH14/01/Sample/Q19", 3,
        "For an exothermic reaction (Delta H < 0), explain how increasing temperature affects Delta S_surroundings and the equilibrium constant K.",
        [{'label': 'a', 'text': 'Relate Delta S_surroundings = -Delta H / T to K using Delta S_total = R ln K.', 'marks': 3}],
        "19. (a) As T increases, Delta S_surroundings (-Delta H / T) becomes less positive (1). Delta S_total decreases (1). Since ln K = Delta S_total / R, K decreases (equilibrium shifts left) (1)."),

    make_edexcel_q(20, "Entropy Change in Gas Expansion", "WCH14/01/Sample/Q20", 3,
        "1 mole of an ideal gas expands isothermally from 10 dm3 to 20 dm3 at 298 K.",
        [{'label': 'a', 'text': 'Calculate Delta S = R ln(V2/V1).', 'marks': 2},
         {'label': 'b', 'text': 'Explain why expanding into a vacuum is spontaneous.', 'marks': 1}],
        "20. (a) Delta S = 8.31 x ln(20 / 10) = 8.31 x 0.69315 = +5.76 J K-1 mol-1 (2).<br/>20. (b) Gas molecules have double the volume/microstates available, increasing disorder (1)."),

    make_edexcel_q(21, "Entropy of Neutralisation Reaction", "WCH14/01/Sample/Q21", 3,
        "H+(aq) + OH-(aq) -> H2O(l): Delta H = -57.1 kJ mol-1, Delta S_system = +80 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why Delta S_system is positive when 2 ions form 1 liquid molecule.', 'marks': 1}],
        "21. (a) Delta S_surr = -(-57100) / 298 = +191.6 J K-1 mol-1. Delta S_total = 80 + 191.6 = +271.6 J K-1 mol-1 (2).<br/>21. (b) H+ and OH- ions strongly order surrounding water molecules; forming H2O releases ordered hydration shells (1)."),

    make_edexcel_q(22, "Entropy Change of Rusting Iron", "WCH14/01/Sample/Q22", 4,
        "4Fe(s) + 3O2(g) -> 2Fe2O3(s): Delta H = -1648 kJ mol-1, Delta S_system = -549 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_surroundings and Delta S_total at 298 K.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why iron rusts spontaneously despite a large decrease in system entropy.', 'marks': 1}],
        "22. (a) Delta S_surr = -(-1648000) / 298 = +5530.2 J K-1 mol-1 (2). Delta S_total = -549 + 5530.2 = +4981.2 J K-1 mol-1 (1).<br/>22. (b) The huge exothermic heat release creates an overwhelming positive surroundings entropy change (1)."),

    make_edexcel_q(23, "Entropy of Dehydration of Copper Sulfate Pentahydrate", "WCH14/01/Sample/Q23", 3,
        "CuSO4.5H2O(s) -> CuSO4(s) + 5H2O(g): Delta H = +298 kJ mol-1, Delta S_system = +700 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate the temperature at which CuSO4.5H2O dehydrates spontaneously.', 'marks': 3}],
        "23. (a) T_min = Delta H / Delta S_system = 298000 J mol-1 / 700 J K-1 mol-1 = 425.7 K (152.6 °C) (3)."),

    make_edexcel_q(24, "Microstates and Boltzmann Entropy Equation S = k ln W", "WCH14/01/Sample/Q24", 3,
        "Boltzmann\'s equation relates entropy to microstates: S = kB ln W.",
        [{'label': 'a', 'text': 'Explain what W represents.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate S for a system with W = 1.0 x 10^23 microstates. (kB = 1.38 x 10^-23 J K-1)', 'marks': 2}],
        "24. (a) W = number of energetically equivalent microstates / arrangements (1).<br/>24. (b) S = (1.38x10^-23) x ln(1.0x10^23) = (1.38x10^-23) x 52.956 = 7.31 x 10^-22 J K-1 (2)."),

    make_edexcel_q(25, "Standard Entropy Comparison Across Halogen Elements", "WCH14/01/Sample/Q25", 3,
        "S° values (J K-1 mol-1): F2(g)=202.7, Cl2(g)=223.0, Br2(l)=152.2, I2(s)=116.1.",
        [{'label': 'a', 'text': 'Explain why F2(g) and Cl2(g) have higher entropy than Br2(l) and I2(s).', 'marks': 2},
         {'label': 'b', 'text': 'Explain why Cl2(g) has higher entropy than F2(g).', 'marks': 1}],
        "25. (a) Gases have far higher molecular kinetic motion and freedom of movement than liquids or solids (2).<br/>25. (b) Cl2 has more electrons / higher molar mass, giving more vibrational and rotational energy levels (1)."),

    # Tier 2 A* Challenge Questions (Q26 - Q50)
    make_edexcel_q(26, "A* Challenge: Complete Entropy Calculation & Equilibrium Constant K", "WCH14/01/Hard/Q26", 6,
        "For the reaction: 2NO2(g) <=> N2O4(g)<br/>Delta H° = -57.2 kJ mol-1.<br/>S° (J K-1 mol-1): NO2(g) = 240.0, N2O4(g) = 304.0.",
        [{'label': 'a', 'text': 'Calculate Delta S_system.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta S_surroundings and Delta S_total at 298 K.', 'marks': 2},
         {'label': 'c', 'text': 'Calculate the equilibrium constant K at 298 K.', 'marks': 2}],
        "26. (a) Delta S_sys = 304.0 - 2(240.0) = -176.0 J K-1 mol-1 (2).<br/>26. (b) Delta S_surr = -(-57200)/298 = +191.95 J K-1 mol-1. Delta S_total = -176.0 + 191.95 = +15.95 J K-1 mol-1 (2).<br/>26. (c) ln K = 15.95 / 8.31 = 1.9194 => K = e^1.9194 = 6.82 (2)."),

    make_edexcel_q(27, "A* Challenge: Temperature at Which Equilibrium Constant K = 1", "WCH14/01/Hard/Q27", 5,
        "For a reaction with Delta H = +125 kJ mol-1 and Delta S_system = +160 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Show that when K = 1, Delta S_total = 0.', 'marks': 1},
         {'label': 'b', 'text': 'Calculate the exact temperature in °C at which K = 1.', 'marks': 3},
         {'label': 'c', 'text': 'Calculate K at 1000 K.', 'marks': 1}],
        "27. (a) Delta S_total = R ln K = R ln(1) = 0 J K-1 mol-1 (1).<br/>27. (b) T = Delta H / Delta S_sys = 125000 / 160 = 781.25 K = 508.1 °C (3).<br/>27. (c) At 1000 K, Delta S_surr = -125000/1000 = -125. Delta S_tot = 160 - 125 = +35. ln K = 35/8.31 = 4.211 => K = 67.4 (1)."),

    make_edexcel_q(28, "A* Challenge: Thermodynamic Feasibility vs Rate Profile of Ammonia Synthesis", "WCH14/01/Hard/Q28", 5,
        "Haber Process: N2(g) + 3H2(g) <=> 2NH3(g)<br/>Delta H = -92.2 kJ mol-1, Delta S_system = -198.8 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Explain why industrial production uses 400-450 °C despite thermodynamics favouring low temperatures.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate Delta S_total at 700 K and explain why high temperature prevents high equilibrium yield.', 'marks': 2}],
        "28. (a) Low temperature gives high equilibrium yield (Delta S_total > 0) but reaction rate is too slow (high activation energy) (2). 400-450 °C is a compromise temperature giving acceptable rate with catalyst (1).<br/>28. (b) At 700 K: Delta S_surr = -(-92200)/700 = +131.7 J K-1 mol-1. Delta S_total = -198.8 + 131.7 = -67.1 J K-1 mol-1 < 0 (unfeasible/low yield) (2)."),

    make_edexcel_q(29, "A* Challenge: Entropy of Solution and Lattice Energy Interplay", "WCH14/01/Hard/Q29", 5,
        "Dissolving NaCl: NaCl(s) -> Na+(aq) + Cl-(aq)<br/>Delta_LE H = -787 kJ mol-1, Delta_hyd H(Na+) = -406 kJ mol-1, Delta_hyd H(Cl-) = -364 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta_sol H for NaCl.', 'marks': 2},
         {'label': 'b', 'text': 'If Delta S_system = +43.0 J K-1 mol-1, calculate Delta S_total at 298 K and explain why NaCl dissolves.', 'marks': 3}],
        "29. (a) Delta_sol H = Delta_hyd H(Na+) + Delta_hyd H(Cl-) - Delta_LE H = (-406 - 364) - (-787) = +17.0 kJ mol-1 (2).<br/>29. (b) Delta S_surr = -17000 / 298 = -57.05 J K-1 mol-1. Delta S_total = +43.0 - 57.05 = -14.05 J K-1 mol-1 (2). Dissolves due to local concentration/entropy effects (1)."),

    make_edexcel_q(30, "A* Challenge: Temperature Feasibility Boundary Plot", "WCH14/01/Hard/Q30", 5,
        "For CaCO3(s) -> CaO(s) + CO2(g), Delta H = +178 kJ mol-1, Delta S_system = +161 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 800 K, 1105.6 K, and 1400 K.', 'marks': 3},
         {'label': 'b', 'text': 'Describe the graph of Delta S_total against temperature T.', 'marks': 2}],
        "30. (a) At 800 K: Delta S_surr = -178000/800 = -222.5 => Delta S_tot = -61.5 J K-1 mol-1 (1). At 1105.6 K: Delta S_tot = 0 (1). At 1400 K: Delta S_surr = -127.1 => Delta S_tot = +33.9 J K-1 mol-1 (1).<br/>30. (b) Curve increases monotonically with increasing T, crossing from negative to positive at T = 1105.6 K (2)."),

    make_edexcel_q(31, "A* Challenge: Industrial Extraction of Titanium via K and Entropy", "WCH14/01/Hard/Q31", 5,
        "Kroll Process: TiO2(s) + 2C(s) + 2Cl2(g) -> TiCl4(l) + 2CO(g)<br/>Delta H = -230 kJ mol-1, Delta S_system = +295 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 1000 K.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why both enthalpy and entropy drive this reaction at high temperature.', 'marks': 3}],
        "31. (a) Delta S_surr = -(-230000)/1000 = +230 J K-1 mol-1. Delta S_total = +295 + 230 = +525 J K-1 mol-1 (2).<br/>31. (b) Exothermic (Delta H < 0 => Delta S_surr > 0) AND gas moles increase from 2 mol Cl2 to 2 mol CO gas plus liquid TiCl4 (Delta S_sys > 0). Both terms are positive at all T (3)."),

    make_edexcel_q(32, "A* Challenge: Thermal Decomposition Trends of Group 2 Carbonates", "WCH14/01/Hard/Q32", 5,
        "Decomposition temperatures T_decomp: MgCO3 (540 K), CaCO3 (1110 K), SrCO3 (1550 K), BaCO3 (1630 K).",
        [{'label': 'a', 'text': 'Explain in terms of cation radius and polarizing power why T_decomp increases down Group 2.', 'marks': 3},
         {'label': 'b', 'text': 'Relate this trend to Delta H and T_decomp = Delta H / Delta S_system.', 'marks': 2}],
        "32. (a) Cation radius increases down Group 2 (Mg2+ < Ca2+ < Sr2+ < Ba2+) (1); charge density and polarizing power decrease (1); less distortion of carbonate C-O bond => lattice more thermally stable (1).<br/>32. (b) Delta H becomes more endothermic (more positive) down Group 2, increasing T_decomp = Delta H / Delta S_system (2)."),

    make_edexcel_q(33, "A* Challenge: Entropy of Polymerisation of Ethene", "WCH14/01/Hard/Q33", 5,
        "n CH2=CH2(g) -> -[CH2-CH2]-n(s): Delta H = -105 kJ mol-1 per monomer unit.",
        [{'label': 'a', 'text': 'Predict the sign of Delta S_system for addition polymerisation and explain why.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the maximum temperature T_max at which poly(ethene) is stable if Delta S_system = -70 J K-1 mol-1.', 'marks': 3}],
        "33. (a) Delta S_system is negative because n moles of free gas monomers form 1 mole of rigid solid polymer chain (2).<br/>33. (b) T_max = Delta H / Delta S_sys = 105000 J mol-1 / 70 J K-1 mol-1 = 1500 K (1227 °C) (3). Above this temp, polymer unzips into monomer."),

    make_edexcel_q(34, "A* Challenge: Entropy of Protein Folding & Hydrophobic Effect", "WCH14/01/Hard/Q34", 5,
        "Unfolded polypeptide (random coil) -> Folded native protein structure.",
        [{'label': 'a', 'text': 'Explain why polypeptide chain ordering gives negative Delta S_chain.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how the hydrophobic effect (release of ordered water molecules) makes overall Delta S_system positive.', 'marks': 3}],
        "34. (a) Folding restricts conformational freedom of the backbone and side chains, reducing microstates (Delta S_chain < 0) (2).<br/>34. (b) Non-polar side chains force surrounding water into ordered clathrate cages. When hydrophobic core buries side chains, ordered water is released into bulk water, giving a large positive Delta S_water > |Delta S_chain| (3)."),

    make_edexcel_q(35, "A* Challenge: Calculating Delta S_total for Cell Respiration", "WCH14/01/Hard/Q35", 5,
        "C6H12O6(s) + 6O2(g) -> 6CO2(g) + 6H2O(l): Delta H = -2803 kJ mol-1, Delta S_system = +259 J K-1 mol-1 at 310 K (37 °C).",
        [{'label': 'a', 'text': 'Calculate Delta S_surroundings and Delta S_total at body temperature (310 K).', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the thermodynamic efficiency if 32 ATP molecules are formed (Delta G_ATP = +30.5 kJ mol-1 each).', 'marks': 2}],
        "35. (a) Delta S_surr = -(-2803000)/310 = +9041.9 J K-1 mol-1 (2). Delta S_total = 259 + 9041.9 = +9300.9 J K-1 mol-1 (1).<br/>35. (b) Energy captured = 32 x 30.5 = 976 kJ mol-1. Efficiency = (976 / 2803) x 100% = 34.8% (2)."),

    make_edexcel_q(36, "A* Challenge: Entropy Changes in Electrochemical Fuel Cells", "WCH14/01/Hard/Q36", 5,
        "In a hydrogen-oxygen fuel cell: 2H2(g) + O2(g) -> 2H2O(l)<br/>Delta H = -572 kJ mol-1, Delta S_system = -327 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate maximum electrical work W_max = Delta G = Delta H - T Delta S_system at 298 K.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate theoretical cell emf E° using Delta G = -n F E°. (n = 4, F = 96500 C mol-1)', 'marks': 2}],
        "36. (a) Delta G = -572000 - 298(-327) = -572000 + 97446 = -474554 J mol-1 = -474.6 kJ mol-1 (3).<br/>36. (b) E° = -(-474554) / (4 x 96500) = 474554 / 386000 = +1.23 V (2)."),

    make_edexcel_q(37, "A* Challenge: Entropy of Vaporisation vs Hydrogen Bonding in Alcohols", "WCH14/01/Hard/Q37", 5,
        "S° data: Methanol CH3OH(l)=127, CH3OH(g)=240; Ethanol C2H5OH(l)=161, C2H5OH(g)=283.",
        [{'label': 'a', 'text': 'Calculate Delta S_vap for methanol and ethanol.', 'marks': 2},
         {'label': 'b', 'text': 'Compare with propane C3H8 (Delta S_vap = +87.5 J K-1 mol-1) and explain differences.', 'marks': 3}],
        "37. (a) Methanol: 240 - 127 = +113 J K-1 mol-1 (1). Ethanol: 283 - 161 = +122 J K-1 mol-1 (1).<br/>37. (b) Alcohols have hydrogen bonding in liquid state, increasing liquid order compared to non-polar propane. Breaking H-bonds requires additional entropy increase upon vaporisation (3)."),

    make_edexcel_q(38, "A* Challenge: Temperature Coefficient of Equilibrium Constant K", "WCH14/01/Hard/Q38", 5,
        "For N2O4(g) <=> 2NO2(g), K = 0.144 at 298 K and K = 2.67 at 373 K.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K and 373 K.', 'marks': 2},
         {'label': 'b', 'text': 'Deduce whether the forward reaction is endothermic or exothermic using Delta S_surroundings = -Delta H / T.', 'marks': 3}],
        "38. (a) At 298 K: Delta S_tot = 8.31 ln(0.144) = -16.1 J K-1 mol-1 (1). At 373 K: Delta S_tot = 8.31 ln(2.67) = +8.16 J K-1 mol-1 (1).<br/>38. (b) As T increases, K increases => Delta S_total becomes more positive => Delta S_surroundings (-Delta H / T) becomes less negative => Delta H > 0 (Endothermic) (3)."),

    make_edexcel_q(39, "A* Challenge: Multi-Component Reaction Entropy Analysis", "WCH14/01/Hard/Q39", 5,
        "Solvay process step: Na2CO3(s) + CO2(g) + H2O(l) -> 2NaHCO3(s)<br/>Delta H = -128 kJ mol-1, Delta S_system = -335 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K and state if reaction is spontaneous.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate the temperature above which the reverse reaction (decomposition of NaHCO3) becomes spontaneous.', 'marks': 2}],
        "39. (a) Delta S_surr = -(-128000)/298 = +429.5 J K-1 mol-1. Delta S_total = -335 + 429.5 = +94.5 J K-1 mol-1 (spontaneous) (3).<br/>39. (b) For reverse reaction: Delta H_rev = +128 kJ mol-1, Delta S_sys_rev = +335 J K-1 mol-1. T_decomp = 128000 / 335 = 382.1 K (109 °C) (2)."),

    make_edexcel_q(40, "A* Challenge: Gibbs-Helmholtz Relationship and Feasibility Plots", "WCH14/01/Hard/Q40", 5,
        "The Gibbs-Helmholtz equation is Delta G = Delta H - T Delta S_system.",
        [{'label': 'a', 'text': 'Show that Delta S_total = -Delta G / T.', 'marks': 2},
         {'label': 'b', 'text': 'For a reaction with Delta H > 0 and Delta S_system < 0, explain why the reaction is unfeasible at ALL temperatures.', 'marks': 3}],
        "40. (a) Delta S_total = Delta S_sys + Delta S_surr = Delta S_sys - Delta H / T = -(Delta H - T Delta S_sys) / T = -Delta G / T (2).<br/>40. (b) If Delta H > 0, Delta S_surr (-Delta H / T) is negative at all T. If Delta S_sys < 0, both terms are negative, so Delta S_total is negative (Delta G positive) at all temperatures (3)."),

    make_edexcel_q(41, "A* Challenge: Entropy of Sublimation of Iodine", "WCH14/01/Hard/Q41", 5,
        "I2(s) -> I2(g): Delta H_sub = +62.4 kJ mol-1, Delta S_system = +145 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the sublimation temperature of iodine at 1 atm pressure.', 'marks': 3}],
        "41. (a) Delta S_surr = -62400 / 298 = -209.4 J K-1 mol-1. Delta S_total = +145 - 209.4 = -64.4 J K-1 mol-1 (2).<br/>41. (b) T_sub = Delta H_sub / Delta S_sys = 62400 / 145 = 430.3 K (157.2 °C) (3)."),

    make_edexcel_q(42, "A* Challenge: Entropy of Mixing Ideal Gases", "WCH14/01/Hard/Q42", 5,
        "Mixing 1 mole of Ar(g) and 1 mole of Ne(g) at 298 K and 1 atm pressure.",
        [{'label': 'a', 'text': 'Calculate Delta S_mix = -R (n_A ln x_A + n_B ln x_B) where x_A = x_B = 0.5.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why mixing ideal gases involves Delta H_mix = 0 but is strongly spontaneous.', 'marks': 2}],
        "42. (a) x_Ar = 0.5, x_Ne = 0.5. Delta S_mix = -8.31 x (1 x ln 0.5 + 1 x ln 0.5) = -8.31 x 2 x (-0.69315) = +11.52 J K-1 (3).<br/>42. (b) Ideal gas molecules have zero intermolecular forces so Delta H_mix = 0 (Delta S_surr = 0). Spontaneity is driven entirely by system entropy gain Delta S_mix > 0 (2)."),

    make_edexcel_q(43, "A* Challenge: Entropy Analysis of Biological ATP Hydrolysis", "WCH14/01/Hard/Q43", 5,
        "ATP4-(aq) + H2O(l) -> ADP3-(aq) + HPO4^2-(aq) + H+(aq): Delta H = -20.5 kJ mol-1, Delta S_system = +34.0 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 310 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate Delta G and equilibrium constant K at 310 K.', 'marks': 3}],
        "43. (a) Delta S_surr = -(-20500)/310 = +66.13 J K-1 mol-1. Delta S_total = 34.0 + 66.13 = +100.13 J K-1 mol-1 (2).<br/>43. (b) Delta G = -T Delta S_tot = -310 x 100.13 = -31040 J mol-1 = -31.04 kJ mol-1 (1). ln K = 100.13 / 8.31 = 12.049 => K = e^12.049 = 1.71 x 10^5 (2)."),

    make_edexcel_q(44, "A* Challenge: High Temperature Thermal Cracking Entropy", "WCH14/01/Hard/Q44", 5,
        "C10H22(g) -> C8H18(g) + C2H4(g): Delta H = +82 kJ mol-1, Delta S_system = +140 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 500 K and 900 K.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why thermal cracking is carried out at high temperatures (700-900 K).', 'marks': 2}],
        "44. (a) At 500 K: Delta S_surr = -82000/500 = -164 => Delta S_tot = 140 - 164 = -24 J K-1 mol-1 (unfeasible) (1.5). At 900 K: Delta S_surr = -82000/900 = -91.1 => Delta S_tot = 140 - 91.1 = +48.9 J K-1 mol-1 (feasible) (1.5).<br/>44. (b) High temp is required both to make Delta S_total > 0 (thermodynamics) and overcome high C-C bond activation energy (kinetics) (2)."),

    make_edexcel_q(45, "A* Challenge: Entropy of Hydration vs Ionic Radius Trend", "WCH14/01/Hard/Q45", 5,
        "Hydration entropies Delta S_hyd (J K-1 mol-1): Li+ = -119, Na+ = -89, K+ = -67, Rb+ = -52.",
        [{'label': 'a', 'text': 'Explain the trend in Delta S_hyd down Group 1.', 'marks': 3},
         {'label': 'b', 'text': 'Relate this to ionic charge density and water orientation.', 'marks': 2}],
        "45. (a) Delta S_hyd becomes less negative down Group 1 as ionic radius increases (3).<br/>45. (b) Li+ has highest charge density, forming the most tightly ordered hydration shell (-S). Larger ions (K+, Rb+) have lower charge density and organize surrounding water less strongly (2)."),

    make_edexcel_q(46, "A* Challenge: Entropy of Combustion of Carbon Monoxide", "WCH14/01/Hard/Q46", 5,
        "2CO(g) + O2(g) -> 2CO2(g): Delta H = -566 kJ mol-1, Delta S_system = -173 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the upper temperature limit T_max above which CO combustion becomes unfeasible.', 'marks': 3}],
        "46. (a) Delta S_surr = -(-566000)/298 = +1899.3 J K-1 mol-1. Delta S_total = -173 + 1899.3 = +1726.3 J K-1 mol-1 (2).<br/>46. (b) T_max = Delta H / Delta S_sys = 566000 J mol-1 / 173 J K-1 mol-1 = 3271.7 K (2998.5 °C) (3)."),

    make_edexcel_q(47, "A* Challenge: Calculating System Entropy from Experimental S° Data", "WCH14/01/Hard/Q47", 5,
        "For Fe2O3(s) + 3H2(g) -> 2Fe(s) + 3H2O(g)<br/>S° (J K-1 mol-1): Fe2O3(s)=87.4, H2(g)=130.6, Fe(s)=27.3, H2O(g)=188.7.",
        [{'label': 'a', 'text': 'Calculate Delta S_system.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why Delta S_system is positive despite 3 gas moles reacting to form 3 gas moles.', 'marks': 2}],
        "47. (a) Sum S°(products) = 2(27.3) + 3(188.7) = 54.6 + 566.1 = 620.7 (1). Sum S°(reactants) = 87.4 + 3(130.6) = 479.2 (1). Delta S_sys = 620.7 - 479.2 = +141.5 J K-1 mol-1 (1).<br/>47. (b) H2O(g) has higher molar entropy (188.7) than H2(g) (130.6) due to more rotational/vibrational modes, and Fe(s) is formed (2)."),

    make_edexcel_q(48, "A* Challenge: Total Entropy vs Cell Potential E° Proof", "WCH14/01/Hard/Q48", 5,
        "Prove that Delta S_total = n F E° / T.",
        [{'label': 'a', 'text': 'Combine Delta G = -n F E° and Delta S_total = -Delta G / T to derive the expression.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate Delta S_total at 298 K for a cell with E° = +1.10 V and n = 2.', 'marks': 2}],
        "48. (a) Delta S_total = -Delta G / T (1). Substitute Delta G = -n F E° => Delta S_total = -(-n F E°) / T = n F E° / T (2).<br/>48. (b) Delta S_total = (2 x 96500 x 1.10) / 298 = 212300 / 298 = +712.4 J K-1 mol-1 (2)."),

    make_edexcel_q(49, "A* Challenge: Entropy of Crystallisation of Hydrated Salts", "WCH14/01/Hard/Q49", 5,
        "Cu2+(aq) + SO4^2-(aq) + 5H2O(l) -> CuSO4.5H2O(s): Delta H = -78 kJ mol-1, Delta S_system = -210 J K-1 mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why crystallisation occurs spontaneously below 371 K.', 'marks': 3}],
        "49. (a) Delta S_surr = -(-78000)/298 = +261.7 J K-1 mol-1. Delta S_total = -210 + 261.7 = +51.7 J K-1 mol-1 (2).<br/>49. (b) Exothermic heat release (+S_surr) outweighs system entropy decrease (-S_sys) at temperatures below T = 78000 / 210 = 371.4 K (3)."),

    make_edexcel_q(50, "A* Challenge: Comprehensive Synthesis of Thermodynamics & Kinetics", "WCH14/01/Hard/Q50", 6,
        "For N2(g) + O2(g) -> 2NO(g): Delta H = +180.6 kJ mol-1, Delta S_system = +24.7 J K-1 mol-1, Ea = +315 kJ mol-1.",
        [{'label': 'a', 'text': 'Calculate Delta S_total at 298 K and 2000 K.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why NO is not formed in air at 298 K due to BOTH thermodynamics and kinetics.', 'marks': 3}],
        "50. (a) At 298 K: Delta S_surr = -180600/298 = -606.0 => Delta S_tot = +24.7 - 606.0 = -581.3 J K-1 mol-1 (unfeasible) (1.5). At 2000 K: Delta S_surr = -180600/2000 = -90.3 => Delta S_tot = +24.7 - 90.3 = -65.6 J K-1 mol-1 (1.5).<br/>50. (b) Thermodynamically unfeasible at 298 K (Delta S_total << 0) AND kinetically inert due to high activation energy (+315 kJ mol-1 for N=N triple bond cleavage) (3).")
]

p2_faqs = [
    make_edexcel_faq("Units of System Entropy vs Enthalpy", "Units Conversion", "Adding Delta S_system (J K-1 mol-1) directly to Delta H (kJ mol-1).", "Always convert Delta H to Joules (x1000) before calculating Delta S_surroundings = -Delta H / T. System and surroundings entropy MUST both be in J K-1 mol-1."),
    make_edexcel_faq("Minus Sign in Surroundings Entropy Formula", "Formula Trap", "Forgetting the minus sign in Delta S_surroundings = -Delta H / T.", "Exothermic reactions (Delta H negative) lose heat to surroundings -> surroundings entropy INCREASES (Delta S_surr positive). The minus sign ensures this."),
    make_edexcel_faq("Spontaneity Criterion", "Feasibility", "Stating Delta S_system > 0 is required for spontaneity.", "Spontaneity depends ONLY on TOTAL entropy: Delta S_total = Delta S_system + Delta S_surroundings > 0. An endothermic reaction with negative Delta S_sys can still be spontaneous if surroundings entropy is highly positive."),
    make_edexcel_faq("Temperature of Feasibility Calculation", "Threshold Calculation", "Using Delta S_surroundings = Delta S_system at boundary.", "At the threshold of feasibility, Delta S_total = 0, so Delta S_surroundings = -Delta S_system. Therefore -Delta H / T_min = -Delta S_sys => T_min = Delta H / Delta S_sys."),
    make_edexcel_faq("Entropy at Absolute Zero", "Third Law", "Assuming non-zero entropy at 0 K for perfect crystals.", "Third Law of Thermodynamics: The entropy of a pure, perfectly crystalline substance is EXACTLY ZERO at absolute zero (0 K)."),
    make_edexcel_faq("State Changes and Entropy", "Qualitative Entropy", "Predicting entropy decrease during melting or boiling.", "Melting (solid -> liquid) and boiling (liquid -> gas) ALWAYS increase system entropy due to increased molecular motion and disorder."),
    make_edexcel_faq("Gas Moles and System Entropy Sign", "Qualitative Rules", "Ignoring change in number of gas moles when predicting sign of Delta S_system.", "If gas moles INCREASE (reactants -> products), Delta S_system is POSITIVE. If gas moles DECREASE, Delta S_system is NEGATIVE."),
    make_edexcel_faq("Dissolution of Salts and Entropy", "Solution Entropy", "Assuming dissolving an ionic lattice always increases entropy.", "Dissolving involves lattice breakdown (+S) AND ion hydration (-S due to water ordering). If hydration ordering dominates, Delta S_system can be negative."),
    make_edexcel_faq("Kinetic Inertness vs Thermodynamic Feasibility", "Kinetics vs Thermodynamics", "Assuming Delta S_total > 0 guarantees a rapid reaction.", "Delta S_total > 0 proves a reaction is THERMODYNAMICALLY FEASIBLE, but high activation energy (Ea) can make it kinetically inert (infinitely slow at room temp)."),
    make_edexcel_faq("Relating Delta S_total to Equilibrium Constant K", "Thermodynamic Equilibrium", "Confusing R value or units in Delta S_total = R ln K.", "R = 8.31 J K-1 mol-1. Delta S_total MUST be in J K-1 mol-1. ln K = Delta S_total / R. Exponentiate: K = e^(Delta S_total / R).")
]

# Build Pack 2 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_12A_Entropy.pdf", p2_meta, p2_questions, p2_faqs)
print("Pack 2 (12A Entropy - 50 Qs + 10 FAQs) compiled successfully!")
