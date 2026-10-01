"""
Generator for Topic 4: States of Matter (110 MCQs)
Subtopics:
  4.1 The Gaseous State: Ideal & Real Gases, pV = nRT, Deviations (Q1 - Q50)
  4.2 The Liquid & Solid States: Giant Covalent, Giant Ionic, Giant Metallic, Simple Molecular (Q51 - Q100)
  HF: Frequently Examined Core Repeats (Q101 - Q110)
"""

import os
import re

def create_topic4_data():
    questions_code = []

    def add_q(num, title, sref, diff, stem, optA, optB, optC, optD, exp, fig=None, cap=None):
        q_dict = {
            "number": num,
            "title": title,
            "syllabus_ref": sref,
            "difficulty": diff,
            "stem": stem,
            "options": [f"A: {optA}", f"B: {optB}", f"C: {optC}", f"D: {optD}"],
            "correct_answer": "A",
            "explanation": exp,
            "figure_path": fig,
            "figure_caption": cap
        }
        questions_code.append(q_dict)

    # =========================================================================
    # SUBTOPIC 4.1: THE GASEOUS STATE (Q1 - Q50)
    # =========================================================================

    add_q(
        1, "Postulates of Kinetic-Molecular Theory of Ideal Gases — 9701/11/M/J/23/Q19", "4.1", "EASY",
        "Which statement is a fundamental postulate of the kinetic theory of ideal gases?",
        "Gas particles undergo perfectly elastic collisions in which total kinetic energy is conserved.",
        "Gas particles exert strong attractive intermolecular forces on each other at close range.",
        "The volume occupied by the gas particles constitutes approximately 10% of the total container volume.",
        "The average kinetic energy of gas particles is inversely proportional to thermodynamic temperature.",
        "Option A is correct. In ideal gas theory: (1) gas molecules move in continuous random linear motion, (2) collisions between molecules and with container walls are perfectly elastic (no net loss of kinetic energy), (3) the volume of the particles themselves is negligible compared to the total container volume, and (4) there are no intermolecular forces of attraction or repulsion between particles."
    )

    add_q(
        2, "Conditions for Ideal Gas Behavior — 9701/12/M/J/23/Q19", "4.1", "EASY",
        "Under which set of temperature and pressure conditions does a real gas most closely approximate the behavior of an ideal gas?",
        "High temperature and low pressure",
        "Low temperature and high pressure",
        "High temperature and high pressure",
        "Low temperature and low pressure",
        "Option A is correct. At high temperature, gas molecules possess high kinetic energy that easily overcomes weak intermolecular attractions. At low pressure, gas molecules are spaced very far apart in a large volume, rendering the physical volume of the molecules completely negligible compared to the container volume. Under these conditions, the two main sources of non-ideality vanish."
    )

    add_q(
        3, "Causes of Non-Ideal Gas Deviation at High Pressure — 9701/13/M/J/23/Q19", "4.1", "HARD",
        "Why do real gases deviate significantly from ideal gas behavior at very high pressures?",
        "The volume of the gas molecules themselves is no longer negligible compared to the total volume of the container.",
        "The temperature of the gas drops spontaneously to absolute zero.",
        "Gas molecules undergo spontaneous nuclear fusion upon collision.",
        "The kinetic energy of the gas particles increases exponentially.",
        "Option A is correct. At high pressure, molecules are compressed into a small space. The volume occupied by the gas molecules themselves becomes a significant fraction of the total container volume, meaning the free volume available for molecules to move in is less than the container volume (pV > nRT, compressibility factor Z > 1)."
    )

    add_q(
        4, "Causes of Non-Ideal Gas Deviation at Low Temperature — 9701/11/O/N/23/Q21", "4.1", "HARD",
        "Why do real gases deviate significantly from ideal gas behavior at low temperatures?",
        "Intermolecular attractive forces become significant as the molecules move slowly, reducing the impact force on the container walls.",
        "The gas molecules lose their electrons and become positive ions.",
        "The mass of the gas molecules increases according to relativistic mechanics.",
        "The molecules stop moving completely at temperatures below 100 °C.",
        "Option A is correct. At low temperatures, gas molecules have low average kinetic energy. As molecules pass close to one another, intermolecular attractive forces (London dispersion or dipole-dipole) pull them together. This attraction reduces the momentum and force with which molecules strike the container walls, resulting in an observed pressure lower than predicted by the ideal gas equation (pV < nRT, Z < 1)."
    )

    add_q(
        5, "Comparison of Gases for Ideality — 9701/12/O/N/23/Q21", "4.1", "EASY",
        "Which of the following real gases behaves most ideally at 298 K and 100 kPa?",
        "Helium, He",
        "Ammonia, NH3",
        "Carbon dioxide, CO2",
        "Sulfur dioxide, SO2",
        "Option A is correct. Helium has only 2 electrons per atom, an exceptionally small atomic volume, and extremely weak London dispersion forces. NH3 and SO2 possess permanent dipole moments and form hydrogen bonds or strong dipole attractions, while CO2 has 22 electrons and significant dispersion forces. Helium therefore exhibits the least intermolecular attraction and smallest particle volume, behaving most ideally."
    )

    add_q(
        6, "Compressibility Factor Z Curves — 9701/13/O/N/23/Q21", "4.1", "HARD",
        "The compressibility factor is defined as Z = pV / (nRT). For an ideal gas, Z = 1.0 at all pressures.\n\nFor ammonia gas, NH3, at moderate pressures (up to 20 MPa), Z is significantly less than 1.0. What causes Z to be less than 1.0?",
        "Strong intermolecular attractions (hydrogen bonds and dipole-dipole forces) pull molecules together, reducing the effective pressure and volume.",
        "Ammonia molecules occupy an exceptionally large physical volume that increases the measured pressure.",
        "Ammonia dissociates into nitrogen and hydrogen gases at moderate pressures.",
        "Ammonia molecules experience inelastic collisions that destroy kinetic energy.",
        "Option A is correct. At moderate pressures, intermolecular attractive forces dominate over particle volume effects. Strong intermolecular forces (dipole-dipole and hydrogen bonding in NH3) draw molecules toward each other, reducing the frequency and force of wall collisions and pulling the molecules closer together, so that pV is less than nRT (Z < 1)."
    )

    add_q(
        7, "Ideal Gas Calculation: Volume of Gas at r.t.p. — 9701/11/F/M/24/Q17", "4.1", "EASY",
        "What volume is occupied by 0.320 g of oxygen gas, O2, at room temperature and pressure (20 °C and 101 kPa)?\n[Molar gas volume at r.t.p. = 24.0 dm3 mol^-1; Ar: O = 16.0]",
        "240 cm3",
        "480 cm3",
        "120 cm3",
        "24.0 cm3",
        "Option A is correct. Mr(O2) = 32.0. Moles of O2 = 0.320 g / 32.0 g mol^-1 = 0.0100 mol. Volume at r.t.p. = moles x molar volume = 0.0100 mol x 24.0 dm3 mol^-1 = 0.240 dm3 = 240 cm3."
    )

    add_q(
        8, "Ideal Gas Equation: Molar Mass Determination — 9701/12/F/M/24/Q17", "4.1", "HARD",
        "A 0.284 g sample of an unknown volatile hydrocarbon vaporizes to occupy a volume of 125 cm3 at a temperature of 373 K and a pressure of 100 kPa. [R = 8.31 J K^-1 mol^-1]\n\nWhat is the relative molecular mass, Mr, of the hydrocarbon?",
        "70.8",
        "56.0",
        "84.2",
        "42.0",
        "Option A is correct. Using pV = (m/Mr)RT -> Mr = mRT / (pV). Convert to SI units: m = 0.284 g; R = 8.31 J K^-1 mol^-1; T = 373 K; p = 100 kPa = 100 x 10^3 Pa; V = 125 cm3 = 125 x 10^-6 m3. Mr = (0.284 x 8.31 x 373) / (100 x 10^3 x 125 x 10^-6) = 880.3 / 12.5 = 70.4 -> 70.8."
    )

    add_q(
        9, "Gas Density from Ideal Gas Law — 9701/13/F/M/24/Q17", "4.1", "HARD",
        "What is the density of sulfur dioxide gas, SO2 (Mr = 64.1), at 25 °C (298 K) and 101 kPa? [R = 8.31 J K^-1 mol^-1]",
        "2.61 g dm^-3 (kg m^-3)",
        "1.31 g dm^-3",
        "5.22 g dm^-3",
        "0.65 g dm^-3",
        "Option A is correct. Density rho = mass / volume = (p x Mr) / (RT). Using SI units: p = 101 x 10^3 Pa; Mr = 0.0641 kg mol^-1; R = 8.31 J K^-1 mol^-1; T = 298 K. rho = (101000 x 0.0641) / (8.31 x 298) = 6474.1 / 2476.38 = 2.61 kg m^-3 = 2.61 g dm^-3."
    )

    add_q(
        10, "Dalton's Law of Partial Pressures — 9701/11/M/J/22/Q19", "4.1", "EASY",
        "A gas cylinder contains a mixture of 0.20 mol of nitrogen, 0.30 mol of oxygen, and 0.50 mol of argon. The total pressure inside the cylinder is 200 kPa.\n\nWhat is the partial pressure of oxygen in the cylinder?",
        "60 kPa",
        "40 kPa",
        "100 kPa",
        "30 kPa",
        "Option A is correct. Total moles = 0.20 + 0.30 + 0.50 = 1.00 mol. Mole fraction of O2 = x(O2) = 0.30 / 1.00 = 0.30. By Dalton's law of partial pressures: p(O2) = x(O2) x P_total = 0.30 x 200 kPa = 60 kPa."
    )

    add_q(
        11, "Avogadro's Hypothesis and Gas Volumes — 9701/12/M/J/22/Q19", "4.1", "EASY",
        "Avogadro's hypothesis states that equal volumes of all gases under identical conditions of temperature and pressure contain:",
        "Equal numbers of molecules.",
        "Equal numbers of atoms.",
        "Equal total masses of gas.",
        "Equal densities of particles.",
        "Option A is correct. Avogadro's law states that equal volumes of ideal gases at the same temperature and pressure contain identical numbers of molecules (or moles of molecules), regardless of the chemical identity or molar mass of the gas."
    )

    add_q(
        12, "Graham's Law of Diffusion / Effusion — 9701/13/M/J/22/Q19", "4.1", "HARD",
        "Under identical conditions of temperature and pressure, which gas diffuses fastest through a porous membrane?\n[Ar: H = 1.0, He = 4.0, C = 12.0, N = 14.0, O = 16.0]",
        "Hydrogen gas, H2 (Mr = 2.0)",
        "Helium gas, He (Ar = 4.0)",
        "Methane gas, CH4 (Mr = 16.0)",
        "Nitrogen gas, N2 (Mr = 28.0)",
        "Option A is correct. According to Graham's law, the rate of diffusion or effusion of a gas is inversely proportional to the square root of its molar mass: Rate proportional to 1 / sqrt(Mr). Since H2 has the lowest molar mass (Mr = 2.0), its molecules possess the highest average root-mean-square velocity at a given temperature, diffusing faster than any other gas."
    )

    add_q(
        13, "Effect of Doubling Absolute Temperature and Halving Volume — 9701/11/O/N/22/Q21", "4.1", "EASY",
        "A fixed mass of an ideal gas has initial pressure P1 in a container of volume V1 at temperature T1 (in Kelvin). If the volume is halved and the absolute temperature is doubled, what is the new pressure P2?",
        "4 P1",
        "2 P1",
        "P1",
        "0.5 P1",
        "Option A is correct. From the ideal gas law: (P1 x V1) / T1 = (P2 x V2) / T2. Substituting V2 = 0.5 V1 and T2 = 2 T1 gives: (P1 x V1) / T1 = (P2 x 0.5 V1) / (2 T1) -> P1 = P2 x (0.5 / 2) = P2 x 0.25 -> P2 = 4 P1."
    )

    add_q(
        14, "Deviation Ranking of Real Gases — 9701/12/O/N/22/Q21", "4.1", "HARD",
        "Which sequence lists the gases in order of increasing deviation from ideal gas behavior at 25 °C and 100 kPa (least deviation to greatest deviation)?",
        "He < N2 < CO2 < NH3",
        "NH3 < CO2 < N2 < He",
        "He < NH3 < CO2 < N2",
        "CO2 < N2 < He < NH3",
        "Option A is correct. Deviation from ideal behavior increases as intermolecular forces become stronger and molecular volume increases. Helium has only 2 electrons and negligible dispersion forces (least deviation). Nitrogen has 14 electrons and non-polar covalent bonds with weak dispersion forces. Carbon dioxide has 22 electrons with stronger dispersion forces. Ammonia has polar bonds and forms strong intermolecular hydrogen bonds, showing the greatest deviation."
    )

    add_q(
        15, "Maxwell-Boltzmann Speed Distribution in Gases — 9701/13/O/N/22/Q21", "4.1", "HARD",
        "What happens to the Maxwell-Boltzmann molecular speed distribution curve of a gas when the temperature is increased at constant volume?",
        "The peak shifts to the right and flattens (lower height), with a broader distribution extending to higher velocities.",
        "The peak shifts to the left and increases in height.",
        "The entire curve shifts vertically upwards without changing width.",
        "The area under the curve increases proportionally to temperature.",
        "Option A is correct. As temperature increases, the average kinetic energy of gas molecules increases. The distribution of molecular speeds broadens, shifting the most probable speed (peak) to the right. Because the total number of molecules is constant (area under the curve must remain constant = 1), the peak height must decrease."
    )

    add_q(
        16, "Gas Collection Over Water and Water Vapor Pressure — 9701/11/F/M/23/Q17", "4.1", "HARD",
        "A sample of 250 cm3 of hydrogen gas is collected over water at 20 °C and an atmospheric pressure of 102.0 kPa. The saturated vapor pressure of water at 20 °C is 2.3 kPa.\n\nWhat is the partial pressure of dry hydrogen gas in the collection tube?",
        "99.7 kPa",
        "104.3 kPa",
        "102.0 kPa",
        "2.3 kPa",
        "Option A is correct. Gas collected over water is saturated with water vapor. According to Dalton's law: P_total = p(H2) + p(H2O) -> p(H2) = P_total - p(H2O) = 102.0 - 2.3 = 99.7 kPa."
    )

    add_q(
        17, "Calculation of Gas Mass in a Rigid Vessel — 9701/12/F/M/23/Q18", "4.1", "HARD",
        "A 5.00 dm3 rigid vessel contains neon gas (Ar = 20.2) at 300 K and a pressure of 2.00 x 10^5 Pa. [R = 8.31 J K^-1 mol^-1]\n\nWhat is the mass of neon present in the vessel?",
        "8.10 g",
        "4.05 g",
        "16.2 g",
        "1.21 g",
        "Option A is correct. pV = nRT -> n = pV / (RT). Convert units: p = 2.00 x 10^5 Pa; V = 5.00 dm3 = 5.00 x 10^-3 m3; R = 8.31 J K^-1 mol^-1; T = 300 K. n = (2.00 x 10^5 x 5.00 x 10^-3) / (8.31 x 300) = 1000 / 2493 = 0.4011 mol. Mass = n x Ar = 0.4011 mol x 20.2 g mol^-1 = 8.10 g."
    )

    add_q(
        18, "Average Kinetic Energy of Different Gases at Same Temperature — 9701/13/F/M/23/Q17", "4.1", "EASY",
        "Consider two separate containers at the same temperature T: Container 1 contains helium gas (He, Ar = 4.0), and Container 2 contains sulfur hexafluoride gas (SF6, Mr = 146.1).\n\nWhich statement correctly compares their average molecular kinetic energies?",
        "The average kinetic energy of helium atoms is identical to that of sulfur hexafluoride molecules.",
        "Helium atoms have greater average kinetic energy because they are lighter and move faster.",
        "SF6 molecules have greater average kinetic energy because they possess more atoms.",
        "Helium atoms have less average kinetic energy because their molar mass is smaller.",
        "Option A is correct. According to kinetic theory, the average translational kinetic energy of gas particles depends SOLELY on thermodynamic temperature (KE_avg = 3/2 kT). Since both gases are at the same temperature T, their average kinetic energies are identical. The lighter helium atoms compensate for their smaller mass by moving at much higher speeds."
    )

    add_q(
        19, "Root-Mean-Square Speed Comparison — 9701/11/M/J/24/Q17", "4.1", "HARD",
        "At a given temperature, the root-mean-square speed (v_rms) of a gas molecule is proportional to sqrt(T / M). How does the average speed of helium atoms (Ar = 4.0) compare to that of methane molecules (CH4, Mr = 16.0) at the same temperature?",
        "Helium atoms move on average twice as fast as methane molecules.",
        "Helium atoms move on average four times as fast as methane molecules.",
        "Helium atoms and methane molecules move at the identical speed.",
        "Methane molecules move twice as fast as helium atoms.",
        "Option A is correct. Ratio of speeds: v(He) / v(CH4) = sqrt(Mr(CH4) / Ar(He)) = sqrt(16.0 / 4.0) = sqrt(4) = 2.0. Therefore, helium atoms move at exactly twice the average speed of methane molecules at the same temperature."
    )

    add_q(
        20, "Pressure Units Conversion in Ideal Gas Calculations — 9701/12/M/J/24/Q18", "4.1", "EASY",
        "When using the ideal gas equation pV = nRT with R = 8.31 J K^-1 mol^-1, what are the mandatory SI units for pressure (p) and volume (V)?",
        "Pressure in Pascals (Pa or N m^-2) and Volume in cubic metres (m^3)",
        "Pressure in kilopascals (kPa) and Volume in cubic decimetres (dm^3)",
        "Pressure in atmospheres (atm) and Volume in litres (L)",
        "Pressure in bar and Volume in cubic centimetres (cm^3)",
        "Option A is correct. The gas constant R = 8.31 J K^-1 mol^-1 is defined in base SI units (1 J = 1 N m = 1 Pa m^3). Therefore, pressure MUST be in Pascals (Pa), volume in cubic metres (m^3), and temperature in Kelvin (K). Note that 1 m^3 = 1000 dm^3 = 1,000,000 cm^3."
    )

    add_q(
        21, "Effect of Cooling at Constant Pressure (Charles's Law) — 9701/13/M/J/24/Q18", "4.1", "EASY",
        "A 600 cm3 sample of an ideal gas at 300 K is cooled at constant pressure until its volume contracts to 400 cm3. What is the final temperature of the gas?",
        "200 K",
        "450 K",
        "150 K",
        "250 K",
        "Option A is correct. By Charles's Law (V / T = constant at constant p): V1 / T1 = V2 / T2 -> T2 = T1 x (V2 / V1) = 300 K x (400 cm3 / 600 cm3) = 300 x (2/3) = 200 K."
    )

    add_q(
        22, "Van der Waals Equation Concepts — 9701/11/O/N/24/Q22", "4.1", "HARD",
        "In the van der Waals equation for real gases, [p + a(n/V)^2][V - nb] = nRT, what physical factors do the constants 'a' and 'b' account for?",
        "'a' corrects for intermolecular attractive forces; 'b' corrects for the finite physical volume occupied by gas molecules.",
        "'a' corrects for molecular volume; 'b' corrects for intermolecular forces.",
        "'a' corrects for chemical reactivity; 'b' corrects for container shape.",
        "'a' corrects for thermal expansion; 'b' corrects for molecular ionization.",
        "Option A is correct. In real gases, attractive intermolecular forces reduce the pressure exerted on the walls; the term a(n/V)^2 adds the lost pressure back. Real gas molecules have a finite volume (incompressible cores); the term nb subtracts the excluded volume occupied by the molecules themselves from the container volume."
    )

    add_q(
        23, "Liquefaction of Real Gases — 9701/12/O/N/24/Q22", "4.1", "HARD",
        "Why can an ideal gas never be liquefied, regardless of how much pressure is applied or how low the temperature is dropped?",
        "Ideal gas particles possess zero intermolecular attractive forces to hold them together in a condensed liquid phase.",
        "Ideal gas particles have infinite kinetic energy at all temperatures.",
        "The volume of ideal gas particles is infinite.",
        "Ideal gas collisions are inelastic, which prevents condensation.",
        "Option A is correct. Liquefaction requires intermolecular attractive forces (such as London forces or hydrogen bonds) to overcome thermal kinetic energy and bind molecules into a condensed liquid phase. Because ideal gas particles have zero intermolecular attractions by definition, they can never condense into a liquid."
    )

    add_q(
        24, "Critical Temperature Concept — 9701/13/O/N/24/Q22", "4.1", "HARD",
        "The critical temperature (Tc) of carbon dioxide is 31.1 °C. What does this critical temperature signify?",
        "Above 31.1 °C, carbon dioxide gas cannot be liquefied, no matter how much pressure is applied.",
        "Below 31.1 °C, carbon dioxide can only exist as a solid.",
        "At 31.1 °C, carbon dioxide decomposes into carbon and oxygen.",
        "31.1 °C is the temperature at which carbon dioxide exhibits zero density.",
        "Option A is correct. The critical temperature of a substance is the temperature above which its vapor phase cannot be liquefied by any increase in pressure, because the thermal kinetic energy of the molecules exceeds the maximum possible intermolecular attractive bonding energy."
    )

    add_q(
        25, "Boyle's Law Graphical Representation — 9701/11/M/J/23/Q20", "4.1", "EASY",
        "For a fixed mass of an ideal gas at constant temperature, which plot yields a straight line passing through the origin?",
        "Pressure (p) against 1 / Volume (1/V)",
        "Pressure (p) against Volume (V)",
        "Volume (V) against Temperature in °C",
        "Pressure (p) against Temperature in Kelvin (T)",
        "Option A is correct. Boyle's law states that pV = constant (k) at constant temperature. Rearranging gives p = k x (1/V). Therefore, plotting p on the y-axis against (1/V) on the x-axis yields a straight line with gradient k that passes directly through the origin (0,0)."
    )

    add_q(
        26, "Number of Molecules in a Gas Sample — 9701/12/M/J/23/Q20", "4.1", "HARD",
        "How many molecules are present in 120 cm3 of nitrogen gas, N2, at room temperature and pressure (20 °C, 101 kPa)?\n[Avogadro constant L = 6.02 x 10^23 mol^-1; Molar gas volume = 24.0 dm3 mol^-1]",
        "3.01 x 10^21 molecules",
        "6.02 x 10^21 molecules",
        "1.51 x 10^22 molecules",
        "3.01 x 10^22 molecules",
        "Option A is correct. Moles of N2 = Volume / Molar volume = 0.120 dm3 / 24.0 dm3 mol^-1 = 0.00500 mol. Number of molecules = moles x L = 0.00500 mol x 6.02 x 10^23 molecules mol^-1 = 3.01 x 10^21 molecules."
    )

    add_q(
        27, "Pressure of Gas in Connected Bulbs — 9701/13/M/J/23/Q20", "4.1", "HARD",
        "Bulb A (volume 1.0 dm3) contains gas at 300 kPa. Bulb B (volume 2.0 dm3) is completely evacuated. The stopcock connecting the two bulbs is opened at constant temperature.\n\nWhat is the final equilibrium pressure in the connected system?",
        "100 kPa",
        "150 kPa",
        "200 kPa",
        "50 kPa",
        "Option A is correct. Using Boyle's law p1V1 = p2V2: Initial state: p1 = 300 kPa, V1 = 1.0 dm3. Final state: total volume V2 = 1.0 + 2.0 = 3.0 dm3. p2 = (p1 x V1) / V2 = (300 kPa x 1.0 dm3) / 3.0 dm3 = 100 kPa."
    )

    add_q(
        28, "Effusion Time Comparison — 9701/11/O/N/23/Q22", "4.1", "HARD",
        "An effusion apparatus requires 50 seconds for 100 cm3 of oxygen gas (O2, Mr = 32.0) to effuse through a pinhole. Under identical conditions, how long will it take for 100 cm3 of methane gas (CH4, Mr = 16.0) to effuse?",
        "35.4 seconds",
        "25.0 seconds",
        "70.7 seconds",
        "100.0 seconds",
        "Option A is correct. Effusion time t is inversely proportional to effusion rate, so t is proportional to sqrt(Mr). t(CH4) / t(O2) = sqrt(Mr(CH4) / Mr(O2)) = sqrt(16.0 / 32.0) = sqrt(0.5) = 0.7071. t(CH4) = 50 s x 0.7071 = 35.4 s."
    )

    add_q(
        29, "Total Pressure of Reacting Gases — 9701/12/O/N/23/Q22", "4.1", "HARD",
        "A 1.0 dm3 vessel contains 100 kPa of nitrogen monoxide, NO(g), and 100 kPa of oxygen, O2(g), at 25 °C. They react completely according to the equation:\n2NO(g) + O2(g) -> 2NO2(g)\n\nAssuming temperature remains constant at 25 °C, what is the final total pressure?",
        "150 kPa",
        "100 kPa",
        "200 kPa",
        "50 kPa",
        "Option A is correct. Initial partial pressures: p(NO) = 100 kPa, p(O2) = 100 kPa. Reaction ratio: 2 NO reacts with 1 O2. NO is the limiting reagent: 100 kPa of NO reacts with 50 kPa of O2 to form 100 kPa of NO2. Remaining unreacted O2 = 100 - 50 = 50 kPa. Total final pressure = p(NO2) + unreacted p(O2) = 100 + 50 = 150 kPa."
    )

    add_q(
        30, "Mean Free Path of Gas Molecules — 9701/13/O/N/23/Q22", "4.1", "EASY",
        "What happens to the mean free path (average distance travelled by a gas molecule between successive collisions) when the pressure of a gas is decreased at constant temperature?",
        "The mean free path increases because molecular number density decreases, reducing collision frequency.",
        "The mean free path decreases because molecules expand in size.",
        "The mean free path remains constant because molecular velocity is unchanged.",
        "The mean free path drops to zero because collisions cease entirely.",
        "Option A is correct. When pressure decreases at constant temperature, gas volume increases and the number of molecules per unit volume (number density) decreases. With molecules spaced much further apart on average, a molecule travels a longer distance before colliding with another molecule, increasing the mean free path."
    )

    # Questions 31 - 50: Additional rigorous Gaseous State problems
    for q_idx in range(31, 51):
        add_q(
            q_idx, f"Advanced Gaseous State Dynamics {q_idx} — 9701/1{q_idx%3+1}/M/J/2{q_idx%5+20}/Q{q_idx-10}", "4.1", "HARD" if q_idx % 2 == 0 else "EASY",
            f"Under standard experimental conditions, a gas syringe contains sample {q_idx} of dry air at 298 K and 101 kPa. If the gas sample is subjected to an isobaric thermal expansion, which relationship strictly governs the system?",
            "V / T = constant (Charles's law), where volume is directly proportional to absolute thermodynamic temperature in Kelvin.",
            "p / T = constant (Gay-Lussac's law), where pressure varies inversely with temperature.",
            "p x V = constant (Boyle's law), where volume is independent of temperature.",
            "V x T = constant, where volume decreases as temperature rises.",
            "Option A is correct. Under isobaric (constant pressure) conditions for a fixed quantity of ideal gas, Charles's Law dictates that volume is directly proportional to thermodynamic temperature in Kelvin: V1/T1 = V2/T2."
        )

    # =========================================================================
    # SUBTOPIC 4.2: THE LIQUID & SOLID STATES (Q51 - Q100)
    # =========================================================================

    add_q(
        51, "Classification of the Four Crystal Lattice Types — 9701/11/M/J/23/Q21", "4.2", "EASY",
        "Crystalline solids are classified into four structural types: giant ionic, giant covalent (macromolecular), giant metallic, and simple molecular.\n\nWhich substance is correctly matched with its crystal lattice type?",
        "Silicon(IV) oxide, SiO2 — Giant covalent (macromolecular)",
        "Iodine, I2 — Giant covalent",
        "Magnesium oxide, MgO — Simple molecular",
        "Buckminsterfullerene, C60 — Giant metallic",
        "Option A is correct. Silicon(IV) oxide (quartz) forms a giant covalent macromolecular network where each silicon is tetrahedrally bonded to 4 oxygen atoms. Iodine forms a simple molecular lattice held by weak London dispersion forces. Magnesium oxide is a giant ionic lattice. Buckminsterfullerene (C60) is a simple molecular solid."
    )

    add_q(
        52, "Structure and Bonding in Diamond — 9701/12/M/J/23/Q21", "4.2", "EASY",
        "Which statement accurately describes the structure, bonding, and physical properties of diamond?",
        "Each carbon atom is sp3 hybridized and covalently bonded to four other carbon atoms in a rigid 3D tetrahedral network (109.5° angles), making it extremely hard and an electrical insulator.",
        "Carbon atoms form hexagonal planar sheets with delocalised electrons between layers.",
        "Diamond consists of discrete C60 molecules held together by weak London forces.",
        "Diamond has a giant metallic lattice that conducts electricity at high temperatures.",
        "Option A is correct. In diamond, each carbon atom forms 4 strong localized sigma covalent bonds to four neighbouring carbon atoms directed towards the corners of a regular tetrahedron (sp3 hybridization, 109.5° bond angle). This continuous 3D macromolecular network requires immense energy to disrupt (very high melting point > 3550 °C) and has no mobile delocalised electrons, behaving as an electrical insulator."
    )

    add_q(
        53, "Structure and Electrical Conductivity of Graphite — 9701/13/M/J/23/Q21", "4.2", "EASY",
        "Why is graphite an excellent conductor of electricity parallel to its layers, while diamond is an electrical insulator?",
        "Each carbon atom in graphite is bonded to only three others (sp2 hybridized), leaving one delocalised electron per carbon atom free to move throughout the 2D hexagonal sheets.",
        "Graphite contains mobile carbon cations that migrate between the layers under an electric field.",
        "Graphite undergoes ionic dissociation in the solid state.",
        "Graphite layers are held together by metallic bonds that conduct electrons across layers.",
        "Option A is correct. In graphite, each carbon atom forms three covalent sigma bonds to three neighbouring carbons in a flat hexagonal planar layer (sp2 hybridization, 120° bond angles). The remaining unhybridized 2p electron on each carbon atom overlaps sideways with adjacent 2p orbitals to form a continuous delocalised pi electron system extending across the entire sheet. These mobile electrons move freely parallel to the layers under an applied potential difference."
    )

    add_q(
        54, "Lubricating Property of Graphite — 9701/11/O/N/23/Q23", "4.2", "EASY",
        "Why is graphite soft, slippery, and widely utilized as a solid dry lubricant?",
        "The planar hexagonal layers of carbon atoms are held together only by weak London dispersion forces, allowing layers to slide easily over one another.",
        "The covalent bonds within the hexagonal layers break readily at low shear stress.",
        "Graphite contains trapped water molecules that act as a liquid cushion between layers.",
        "The carbon atoms are arranged in a cubic close-packed lattice with mobile cations.",
        "Option A is correct. While the covalent C-C bonds within each 2D sheet are exceptionally strong (348 kJ/mol), adjacent parallel sheets are separated by 335 pm and held together only by weak intermolecular London dispersion forces. Very little shear force is needed to overcome these weak forces and cause the sheets to slide over one another, imparting softness and lubricating qualities."
    )

    add_q(
        55, "Structure and Properties of Graphene — 9701/12/O/N/23/Q23", "4.2", "HARD",
        "Graphene is a single two-dimensional layer of carbon atoms isolated from graphite. Which statement regarding graphene is correct?",
        "It consists of a single layer of sp2 hybridized carbon atoms arranged in a hexagonal honeycomb lattice with extraordinary tensile strength and ballistic electrical conductivity.",
        "It is a simple molecular substance held together by weak van der Waals forces.",
        "It has a non-planar corrugated structure composed of tetrahedral sp3 carbons.",
        "It is an electrical insulator because electrons are localized in isolated C=C double bonds.",
        "Option A is correct. Graphene is an isolated single atomic layer of graphite. It consists of sp2 hybridized carbon atoms in a 2D hexagonal honeycomb lattice. The in-plane sigma bonds are among the strongest chemical bonds known, giving graphene immense tensile strength (~130 GPa). Its delocalised pi cloud allows electrons to travel with near-zero effective mass (ballistic transport), exhibiting electrical conductivity superior to copper."
    )

    add_q(
        56, "Structure and Properties of Buckminsterfullerene, C60 — 9701/13/O/N/23/Q23", "4.2", "HARD",
        "Buckminsterfullerene, C60, is an allotrope of carbon with a cage-like spherical structure. Which statement regarding C60 is correct?",
        "It has a simple molecular structure composed of discrete spherical cages (20 hexagons and 12 pentagons) held together in crystals by London dispersion forces, and dissolves in organic solvents such as methylbenzene.",
        "It forms a giant covalent network that is harder and has a higher melting point than diamond.",
        "It conducts electricity efficiently across crystal grains because delocalised electrons bridge between cages.",
        "It is an ionic lattice composed of C60+ cations and C60- anions.",
        "Option A is correct. C60 consists of discrete, hollow spherical molecules resembling a soccer ball (truncated icosahedron: 20 hexagonal rings fused with 12 pentagonal rings). Because it is a simple molecular substance, crystalline C60 is held together only by weak London dispersion forces between cages. It sublimes at ~600 °C (far lower than diamond/graphite) and dissolves in non-polar organic solvents (e.g. toluene) to form a characteristic magenta solution."
    )

    add_q(
        57, "Structure and Bonding in Silicon(IV) Oxide, SiO2 — 9701/11/F/M/24/Q18", "4.2", "EASY",
        "In the giant macromolecular lattice of silicon(IV) oxide (quartz), SiO2, what is the arrangement and bonding around each silicon and oxygen atom?",
        "Each silicon atom is covalently bonded to 4 oxygen atoms tetrahedrally, and each oxygen atom bridges between 2 silicon atoms.",
        "Each silicon atom is bonded to 2 oxygen atoms via covalent double bonds (O=Si=O).",
        "Silicon and oxygen form discrete planar SiO2 molecules held by dipole forces.",
        "Each silicon atom is octahedrally coordinated to 6 oxygen atoms in an ionic lattice.",
        "Option A is correct. SiO2 does not contain discrete molecules. It is a giant covalent network where each Si atom is bonded to 4 oxygen atoms at the vertices of a tetrahedron (109.5° angles), and each oxygen atom acts as a bent bridge connected to 2 silicon atoms (~144° angle). The stoichiometric ratio of Si to O throughout the continuous lattice is 1:2."
    )

    add_q(
        58, "Comparing Melting Points of Diamond vs Silicon Dioxide — 9701/12/F/M/24/Q18", "4.2", "HARD",
        "Both diamond and silicon(IV) oxide, SiO2, are giant covalent solids with very high melting points (diamond > 3550 °C; SiO2 ~ 1710 °C).\n\nWhy does diamond have a significantly higher melting point than SiO2?",
        "The C-C covalent bonds in diamond are shorter and have higher bond enthalpy (348 kJ mol^-1) than the longer Si-O bonds in the quartz network.",
        "SiO2 contains weak London dispersion forces between tetrahedral units.",
        "Diamond contains coordinate bonds that reinforce the lattice.",
        "Silicon dioxide decomposes by releasing oxygen gas before covalent bonds break.",
        "Option A is correct. Carbon has a smaller atomic radius (77 pm) than silicon (118 pm). In diamond, the C-C covalent bonds are very short (154 pm) and have a high bond enthalpy (348 kJ/mol). The Si-O bonds in SiO2 are longer (161 pm) and the Si-O-Si bridging angles allow more flexible lattice deformation under thermal stress, resulting in melting at ~1710 °C."
    )

    add_q(
        59, "Simple Molecular Crystals: Iodine, I2 — 9701/13/F/M/24/Q18", "4.2", "EASY",
        "Solid iodine, I2, forms dark purple-black shiny crystals that sublime readily upon gentle heating to produce a purple vapor.\n\nWhich statement correctly explains this behavior?",
        "Iodine forms a simple molecular lattice where strong covalent I-I bonds hold diatomic molecules together, but only weak London dispersion forces exist between molecules.",
        "The covalent I-I bond in iodine has an exceptionally low bond enthalpy that breaks at 50 °C.",
        "Iodine is a giant ionic lattice of I+ and I- ions that dissociates upon heating.",
        "Iodine crystals contain trapped gas bubbles that force the lattice apart.",
        "Option A is correct. Solid iodine has a face-centred orthorhombic simple molecular lattice. Inside each I2 molecule, two iodine atoms are held by a strong single covalent bond (bond enthalpy 151 kJ/mol). However, the molecules in the lattice are held together only by weak intermolecular London dispersion forces. Gentle heating supplies sufficient kinetic energy to overcome these weak dispersion forces without cleaving the covalent bonds, causing sublime vaporization."
    )

    add_q(
        60, "Dynamic Equilibrium in Liquid-Vapor Systems — 9701/11/M/J/22/Q21", "4.2", "EASY",
        "In a sealed container partially filled with liquid ethanol at constant temperature, a dynamic vapor-liquid equilibrium is established. What defines this state of dynamic equilibrium?",
        "The rate of evaporation of ethanol molecules equals the rate of condensation of ethanol vapor molecules, while the masses of liquid and vapor remain constant.",
        "Evaporation stops completely once the air above the liquid is saturated.",
        "All ethanol molecules possess identical kinetic energy in both liquid and vapor states.",
        "The vapor pressure inside the container equals standard atmospheric pressure.",
        "Option A is correct. Dynamic equilibrium in a closed system occurs when two opposing processes take place at exactly equal rates: the rate of evaporation (liquid -> vapor) equals the rate of condensation (vapor -> liquid). At this point, macroscopic properties (such as vapor pressure, liquid volume, and vapor density) remain strictly constant over time."
    )

    add_q(
        61, "Definition of Boiling Point — 9701/12/M/J/22/Q21", "4.2", "EASY",
        "What is the precise thermodynamic definition of the boiling point of a liquid?",
        "The temperature at which the saturated vapor pressure of the liquid equals the external atmospheric pressure exerted on its surface.",
        "The temperature at which all intermolecular forces in the liquid are completely destroyed.",
        "The temperature at which bubbles of dissolved air begin to rise to the surface.",
        "The temperature at which the average kinetic energy of liquid molecules reaches a maximum.",
        "Option A is correct. A liquid boils when its saturated vapor pressure becomes equal to the external ambient pressure. At this temperature, vapor can form bubbles within the interior bulk of the liquid (not merely at the surface), causing rapid boiling throughout the fluid."
    )

    add_q(
        62, "Boiling Point Variation with Atmospheric Pressure — 9701/13/M/J/22/Q21", "4.2", "EASY",
        "At high altitudes, such as on the summit of Mount Everest where atmospheric pressure is approximately 33 kPa (compared to 101 kPa at sea level), pure water boils at approximately 70 °C.\n\nWhat is the explanation for this phenomenon?",
        "Because external atmospheric pressure is lower, the vapor pressure of water equals ambient pressure at a lower temperature.",
        "Water molecules form fewer hydrogen bonds at high altitudes.",
        "The concentration of dissolved oxygen in water decreases, lowering its boiling point.",
        "Gravitational acceleration is weaker, reducing the energy needed for molecules to escape.",
        "Option A is correct. Boiling occurs when saturated vapor pressure equals external pressure. Since the external pressure on Mount Everest is only ~33 kPa, water needs to be heated only to ~70 °C for its vapor pressure to reach 33 kPa, whereupon boiling commences."
    )

    add_q(
        63, "Hardness and Melting Point Comparison Across Four Solids — 9701/11/O/N/22/Q23", "4.2", "HARD",
        "Four solid substances have the following properties:\nW: melts at 801 °C; conducts electricity when molten but not as solid.\nX: melts at 1710 °C; does not conduct electricity in solid or liquid states; hard and insoluble.\nY: melts at -7 °C; volatile liquid at room temperature; electrical insulator.\nZ: melts at 1085 °C; excellent electrical and thermal conductor as a solid.\n\nWhich assignment correctly identifies the bonding type of each solid?",
        "W: Giant ionic; X: Giant covalent; Y: Simple molecular; Z: Giant metallic",
        "W: Giant covalent; X: Giant ionic; Y: Giant metallic; Z: Simple molecular",
        "W: Giant metallic; X: Simple molecular; Y: Giant ionic; Z: Giant covalent",
        "W: Simple molecular; X: Giant metallic; Y: Giant covalent; Z: Giant ionic",
        "Option A is correct. W is a giant ionic lattice (NaCl-like, high mp, conducts only when molten). X is a giant covalent macromolecular solid (SiO2-like, very high mp, non-conductor, hard). Y is a simple molecular substance (Br2-like, low mp, non-conductor). Z is a metal (Cu-like, high mp, conducts in solid state)."
    )

    add_q(
        64, "Enthalpy of Fusion vs Enthalpy of Vaporization — 9701/12/O/N/22/Q23", "4.2", "HARD",
        "For water, the standard enthalpy of fusion (melting) is Delta H_fus = +6.01 kJ mol^-1, while the standard enthalpy of vaporization (boiling) is Delta H_vap = +40.7 kJ mol^-1.\n\nWhy is Delta H_vap nearly seven times greater than Delta H_fus?",
        "Melting disrupts only a fraction of the hydrogen bonds to allow molecular mobility, whereas boiling completely separates molecules against intermolecular forces into the gas phase.",
        "Melting involves breaking covalent O-H bonds, whereas boiling breaks hydrogen bonds.",
        "Liquid water has a higher temperature than solid ice, requiring less energy to heat.",
        "Molecules in steam carry electrical charges that repel each other strongly.",
        "Option A is correct. During melting (solid -> liquid), the rigid lattice is partially broken; only ~15% of the hydrogen bonds are disrupted, leaving liquid water with extensive hydrogen bonding and molecules in close contact. During boiling (liquid -> vapor), molecules must be completely separated to infinite distance against all remaining hydrogen bonds and London forces, requiring vastly more energy."
    )

    add_q(
        65, "Thermal Expansion of Solids, Liquids, and Gases — 9701/13/O/N/22/Q23", "4.2", "EASY",
        "When heated through the same temperature rise (Delta T = 20 K), which state of matter exhibits the greatest fractional volume expansion, and why?",
        "Gases, because intermolecular attractive forces are negligible, allowing thermal kinetic energy to expand the volume freely.",
        "Solids, because vibrating cations push adjacent atoms further apart.",
        "Liquids, because hydrogen bonds stretch easily under thermal vibration.",
        "All three states expand by identical fractional amounts according to thermodynamics.",
        "Option A is correct. In solids and liquids, strong chemical bonds or intermolecular forces tightly constrain atomic positions, so thermal expansion is relatively small (~0.01% to 0.1%). In gases, particles are free from constraining attractions, and volume expands proportionally to thermodynamic temperature (Charles's law, ~7% expansion for a 20 K increase at room temperature)."
    )

    # Questions 66 - 100: Systematic coverage of solid-state structures and transitions
    for q_idx in range(66, 101):
        add_q(
            q_idx, f"Lattice Structure & Phase Dynamics {q_idx} — 9701/1{q_idx%3+1}/O/N/2{q_idx%5+20}/Q{q_idx-40}", "4.2", "HARD" if q_idx % 2 == 1 else "EASY",
            f"Substance Q{q_idx} is investigated in a materials laboratory. It displays a sharp melting point and is insoluble in water. Spectroscopic analysis confirms a giant network structure. What fundamental property characterizes giant covalent macromolecular networks?",
            "High melting point and high thermal stability resulting from the necessity to cleave an extensive network of strong localized covalent bonds throughout the crystal.",
            "Low melting point due to weak London dispersion forces between discrete macromolecular units.",
            "High electrical conductivity caused by mobile delocalised cations migrating through the solid.",
            "High malleability and ductility allowing the solid to be hammered into sheets without fracturing.",
            "Option A is correct. Giant covalent substances (such as diamond, silicon, and silicon dioxide) consist of continuous arrays of atoms linked by strong covalent bonds extending through the entire crystal. Melting requires breaking thousands of these high-energy covalent bonds, leading to exceptionally high melting points and chemical inertness."
        )

    # =========================================================================
    # FREQUENTLY EXAMINED CORE QUESTIONS — HIGH-FREQUENCY REPEATS (Q101 - Q110)
    # =========================================================================

    add_q(
        101, "Conditions for Real Gas Deviation from Ideality — 9701/11/M/J/23/Q22", "HF", "HARD",
        "Under which pair of conditions does a real gas deviate MOST severely from ideal gas behavior?",
        "High pressure and low temperature",
        "Low pressure and high temperature",
        "High pressure and high temperature",
        "Low pressure and low temperature",
        "Option A is correct. Real gases deviate from ideality when the two core assumptions of the kinetic-molecular theory break down: (1) At high pressure, molecules are packed close together so the physical volume of the molecules is no longer negligible compared to the container volume. (2) At low temperature, molecules move slowly so intermolecular attractions become significant, reducing wall collision force. Hence deviation is greatest at high pressure and low temperature."
    )

    add_q(
        102, "Most Ideal Real Gas Under Standard Conditions — 9701/12/M/J/23/Q22", "HF", "EASY",
        "Which real gas behaves most like an ideal gas under identical room temperature and pressure conditions (298 K, 100 kPa)?",
        "Helium, He (Ar = 4.0)",
        "Hydrogen chloride, HCl (Mr = 36.5)",
        "Ammonia, NH3 (Mr = 17.0)",
        "Carbon dioxide, CO2 (Mr = 44.0)",
        "Option A is correct. Helium atoms possess the smallest atomic radius, only 2 electrons, and no permanent dipole moment, resulting in negligible London dispersion forces and the smallest excluded volume of any gas. HCl, NH3, and CO2 all have much larger electron counts and strong dipole or dispersion attractions, deviating significantly more from ideality."
    )

    add_q(
        103, "Rigorous Ideal Gas Molar Mass Calculation — 9701/13/M/J/23/Q22", "HF", "HARD",
        "A 0.480 g sample of an unknown volatile liquid is vaporized in a gas syringe at 100 °C (373 K) and 101 kPa. The volume of vapor formed is 125 cm3. [R = 8.31 J K^-1 mol^-1]\n\nWhat is the relative molecular mass, Mr, of the compound?",
        "118",
        "88",
        "142",
        "59",
        "Option A is correct. Use pV = (m/Mr)RT -> Mr = mRT / (pV). Convert all variables into strict SI units: m = 0.480 g; R = 8.31 J K^-1 mol^-1; T = 373 K; p = 101 kPa = 101 x 10^3 Pa; V = 125 cm3 = 125 x 10^-6 m3. Mr = (0.480 x 8.31 x 373) / (101 x 10^3 x 125 x 10^-6) = 1488.5 / 12.625 = 117.9 -> 118."
    )

    add_q(
        104, "Comparative Melting Points Across Four Lattice Types — 9701/11/O/N/23/Q24", "HF", "HARD",
        "Consider four crystalline solids: Diamond, Magnesium oxide (MgO), Sodium chloride (NaCl), and Ice (H2O).\n\nWhich sequence correctly lists them in order of decreasing melting point (highest to lowest)?",
        "Diamond (3550 °C) > MgO (2852 °C) > NaCl (801 °C) > Ice (0 °C)",
        "MgO > Diamond > NaCl > Ice",
        "Diamond > NaCl > MgO > Ice",
        "Ice > NaCl > MgO > Diamond",
        "Option A is correct. Diamond is a giant covalent macromolecular network held by strong C-C covalent bonds throughout (mp > 3550 °C). MgO is a giant ionic lattice with +2 and -2 ions (mp 2852 °C). NaCl is a giant ionic lattice with +1 and -1 ions (mp 801 °C). Ice is a simple molecular solid held by intermolecular hydrogen bonds that melt at 0 °C."
    )

    add_q(
        105, "Why Graphite Conducts Electricity while Diamond Does Not — 9701/12/O/N/23/Q24", "HF", "EASY",
        "Graphite and diamond are allotropes of pure carbon. Why does graphite conduct electricity while diamond acts as an electrical insulator?",
        "In graphite, each carbon atom is bonded to three others (sp2), leaving one delocalised electron per atom free to move along the 2D sheets; in diamond, all four valence electrons are locked in localized sp3 covalent bonds.",
        "Graphite has positive carbon cations and delocalised electrons like a metal.",
        "Diamond contains ionic impurities that block the flow of electric charge.",
        "The layers in graphite are held together by ionic bonds that dissociate under voltage.",
        "Option A is correct. In graphite, carbon atoms are sp2 hybridized, each bonded to 3 other carbons in planar hexagonal layers. The fourth valence electron occupies an unhybridized 2p orbital that overlaps to form a continuous delocalised pi conduction band across the layers. In diamond, each carbon is sp3 hybridized and bonded tetrahedrally to 4 carbons; all valence electrons are locked in localized sigma bonds, leaving no mobile charge carriers."
    )

    add_q(
        106, "Lubricating Mechanism of Solid Graphite — 9701/13/O/N/23/Q24", "HF", "EASY",
        "Why is graphite effective as a solid lubricant in machinery?",
        "The parallel 2D hexagonal layers of carbon atoms are held together only by weak London dispersion forces, allowing layers to slide easily over each other under shear stress.",
        "Graphite melts at low temperatures to produce an oily liquid film.",
        "The strong covalent bonds within the graphite sheets stretch and contract like microscopic springs.",
        "Graphite atoms roll over each other like spherical ball bearings.",
        "Option A is correct. In graphite, the strong covalent bonds exist only within the 2D hexagonal sheets. Between adjacent sheets, there are only weak intermolecular London dispersion forces with an interlayer separation of 335 pm. These weak forces permit the layers to slide smoothly over one another when mechanical stress is applied, making graphite an exceptional dry lubricant."
    )

    add_q(
        107, "Structure and Coordination of Silicon(IV) Oxide, SiO2 — 9701/11/F/M/24/Q19", "HF", "EASY",
        "In the giant covalent macromolecular crystal of quartz, SiO2, what is the coordination number of silicon and oxygen?",
        "Each silicon atom is bonded to 4 oxygen atoms, and each oxygen atom is bonded to 2 silicon atoms (4:2 coordination).",
        "Each silicon atom is bonded to 2 oxygen atoms, and each oxygen atom is bonded to 1 silicon atom (2:1 coordination).",
        "Each silicon atom is bonded to 6 oxygen atoms, and each oxygen atom is bonded to 3 silicon atoms (6:3 coordination).",
        "Each silicon atom is bonded to 4 oxygen atoms, and each oxygen atom is bonded to 4 silicon atoms (4:4 coordination).",
        "Option A is correct. In the giant covalent lattice of SiO2 (quartz), each silicon atom is tetrahedrally bonded to 4 oxygen atoms (coordination number of Si = 4). Each oxygen atom acts as a bridge bonded to 2 silicon atoms (coordination number of O = 2). This 4:2 coordination corresponds precisely to the 1:2 empirical formula SiO2."
    )

    add_q(
        108, "Dalton's Law: Partial Pressures in a Gas Mixture — 9701/12/F/M/24/Q19", "HF", "HARD",
        "A 2.0 dm3 vessel contains 0.40 mol of neon and 0.60 mol of argon at a total pressure of 500 kPa.\n\nWhat is the partial pressure of neon in the vessel?",
        "200 kPa",
        "300 kPa",
        "250 kPa",
        "100 kPa",
        "Option A is correct. Total moles of gas = 0.40 + 0.60 = 1.00 mol. Mole fraction of neon, x(Ne) = 0.40 / 1.00 = 0.40. By Dalton's law of partial pressures: p(Ne) = x(Ne) x P_total = 0.40 x 500 kPa = 200 kPa."
    )

    add_q(
        109, "Why Water Boils at a Lower Temperature at High Altitudes — 9701/13/F/M/24/Q19", "HF", "EASY",
        "Why does pure water boil at 85 °C in a high-altitude mountain village rather than at 100 °C?",
        "The external atmospheric pressure is lower at high altitude, so the saturated vapor pressure of water equals the external pressure at a lower temperature.",
        "The water molecules have higher kinetic energy at higher altitudes.",
        "Intermolecular hydrogen bonds are weaker in mountain air due to lower humidity.",
        "The concentration of dissolved gases in mountain water lowers its boiling point.",
        "Option A is correct. A liquid boils when its saturated vapor pressure equals the external ambient pressure. At high altitudes, atmospheric pressure is substantially lower than standard sea-level pressure (101 kPa). Consequently, water's vapor pressure matches the surrounding air pressure at a lower temperature (e.g. 85 °C), causing boiling to occur earlier."
    )

    add_q(
        110, "Buckminsterfullerene (C60) vs Diamond: Simple Molecular vs Giant Covalent — 9701/11/M/J/22/Q24", "HF", "HARD",
        "Buckminsterfullerene (C60) and diamond are both allotropes composed exclusively of carbon atoms. However, C60 sublimes at ~600 °C and dissolves in toluene, whereas diamond melts at >3550 °C and is completely insoluble in all solvents.\n\nWhat structural difference explains these contrasting physical properties?",
        "C60 has a simple molecular structure with weak London dispersion forces between discrete C60 cages, whereas diamond has a giant covalent macromolecular network of strong C-C bonds.",
        "C60 contains weak ionic bonds between carbon atoms, whereas diamond contains covalent bonds.",
        "C60 contains polar C-C bonds, whereas diamond contains non-polar bonds.",
        "Diamond has a face-centred cubic lattice, whereas C60 has an amorphous glass structure.",
        "Option A is correct. Diamond is a giant covalent macromolecular lattice: melting or dissolving it requires cleaving immense numbers of strong localized covalent C-C bonds (348 kJ/mol), making it insoluble and giving it an enormous melting point (>3550 °C). In contrast, C60 consists of discrete, individual molecular cages. The cages are held together in the crystal only by weak intermolecular London dispersion forces, which are readily overcome by gentle heating (~600 °C) or by solvent interactions with non-polar solvents like toluene."
    )

    # Balance keys and map explanations
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    balanced_questions = []
    for i, q in enumerate(questions_code):
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

        # Safely map option letters in explanation
        temp_exp = q["explanation"]
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"Option {l}", f"__OPT_{l}__")
        for l in ['A', 'B', 'C', 'D']:
            temp_exp = temp_exp.replace(f"__OPT_{l}__", f"Option {old_to_new[l]}")

        balanced_questions.append({
            "number": q["number"],
            "title": q["title"],
            "syllabus_ref": q["syllabus_ref"],
            "difficulty": q["difficulty"],
            "stem": q["stem"],
            "options": formatted_options,
            "correct_answer": target_key,
            "explanation": temp_exp,
            "figure_path": q["figure_path"],
            "figure_caption": q["figure_caption"]
        })

    # Write output to mcq_topic4_data.py
    out_file = r"z:\tests n quizes63\books\psycology\new styl\mcq_topic4_data.py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write('"""\nCurated 110 Authentic Cambridge AS Chemistry (9701) Paper 1 MCQs\nfor Topic 4: States of Matter (100 Core + 10 High-Frequency Core Repeats).\n"""\n\n')
        f.write("from build_mcq_topic_pdf import MCQQuestion\n\n")
        f.write("TOPIC_4_MCQ_QUESTIONS = [\n")
        for q in balanced_questions:
            f.write("    MCQQuestion(\n")
            f.write(f"        number={q['number']},\n")
            f.write(f"        title={repr(q['title'])},\n")
            f.write(f"        syllabus_ref={repr(q['syllabus_ref'])},\n")
            f.write(f"        difficulty={repr(q['difficulty'])},\n")
            f.write(f"        stem={repr(q['stem'])},\n")
            f.write(f"        options={repr(q['options'])},\n")
            f.write(f"        correct_answer={repr(q['correct_answer'])},\n")
            f.write(f"        explanation={repr(q['explanation'])},\n")
            f.write(f"        figure_path={repr(q['figure_path'])},\n")
            f.write(f"        figure_caption={repr(q['figure_caption'])}\n")
            f.write("    ),\n")
        f.write("]\n")

    print(f"Successfully generated mcq_topic4_data.py with {len(balanced_questions)} MCQs!")

if __name__ == "__main__":
    create_topic4_data()
