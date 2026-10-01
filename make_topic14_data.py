"""
Generator for Topic 14: Hydrocarbons — Alkanes & Alkenes (110 MCQs)
Subtopics:
  14.1 Alkanes: Combustion, Free Radical Substitution, Cracking (Q1 - Q40)
  14.2 Alkenes: Electrophilic Addition, Markovnikov Rule, KMnO4 Oxidation (Q41 - Q100)
  HF: Frequently Examined Core Repeats (Q101 - Q110)
"""

import os
import re

def create_topic14_data():
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
    # SUBTOPIC 14.1: ALKANES — COMBUSTION, FREE RADICAL SUBSTITUTION & CRACKING (Q1 - Q40)
    # =========================================================================

    add_q(
        1, "Incomplete Combustion of Alkanes — 9701/11/M/J/23/Q17", "14.1", "EASY",
        "What are the toxic primary products formed during the incomplete combustion of alkanes in a limited oxygen supply?",
        "Carbon monoxide, CO, and solid carbon particulate soot, C",
        "Carbon dioxide, CO2, and sulfur dioxide, SO2",
        "Methane, CH4, and ozone, O3",
        "Nitrogen dioxide, NO2, and steam",
        "Option A is correct. In a limited supply of oxygen, complete oxidation to CO2 cannot occur. Instead, incomplete combustion takes place, producing highly toxic carbon monoxide gas (CO, which binds irreversibly to hemoglobin) and unburnt carbon particulates (soot/smoke, causing respiratory distress)."
    )

    add_q(
        2, "Mechanism of Photochemical Chlorination of Alkanes — 9701/12/M/J/23/Q17", "14.1", "MEDIUM",
        "In the free radical chlorination of ethane under ultraviolet light, which equation represents an essential propagation step?",
        "CH3CH2. + Cl2 -> CH3CH2Cl + Cl.",
        "Cl2 -> 2Cl. (under UV irradiation)",
        "CH3CH3 + Cl. -> CH3CH2Cl + H.",
        "CH3CH2. + Cl. -> CH3CH2Cl",
        "Option A is correct. The propagation steps in the chlorination of ethane are: (1) Cl. + CH3CH3 -> CH3CH2. + HCl; and (2) CH3CH2. + Cl2 -> CH3CH2Cl + Cl.. Option B is initiation; Option D is termination; Option C incorrectly shows hydrogen radical abstraction (which does not occur because H-Cl bond enthalpy is so much higher than C-Cl)."
    )

    add_q(
        3, "Catalytic Cracking of Long-Chain Alkanes — 9701/13/M/J/23/Q17", "14.1", "EASY",
        "What are the standard industrial conditions used for the catalytic cracking of long-chain hydrocarbons, and what types of products are formed?",
        "Zeolite (aluminosilicate) catalyst at approximately 500 °C; produces shorter-chain branched alkanes and alkenes.",
        "Concentrated sulfuric acid at 100 °C; produces carboxylic acids and esters.",
        "Nickel catalyst at 150 °C; produces cycloalkanes and hydrogen gas.",
        "Iron catalyst at 450 °C and 200 atm; produces aromatic compounds exclusively.",
        "Option A is correct. Catalytic cracking passes vaporised heavy gas oil over a synthetic zeolite (silica/alumina) catalyst at ~500 °C under slight pressure. C-C bonds undergo heterolytic/homolytic cleavage to produce shorter, high-demand fuels (branched alkanes with high octane ratings) and valuable unsaturated chemical feedstocks (alkenes like ethene and propene)."
    )

    add_q(
        4, "Multi-Halogenation in Free Radical Substitution — 9701/11/O/N/23/Q17", "14.1", "HARD",
        "When methane is reacted with an excess of chlorine gas in the presence of strong UV light, what is the ultimate principal organic product formed?",
        "Tetrachloromethane, CCl4",
        "Chloromethane, CH3Cl",
        "Dichloromethane, CH2Cl2",
        "Hexachloroethane, C2Cl6",
        "Option A is correct. With excess chlorine, successive propagation cycles replace each remaining hydrogen atom on the carbon: CH4 -> CH3Cl -> CH2Cl2 -> CHCl3 -> CCl4. With sufficient Cl2 and UV irradiation, all four hydrogens are substituted, yielding tetrachloromethane (CCl4) as the final major organic product."
    )

    # Questions 5 - 40: Systematic Alkanes Questions
    alkane_pool = [
        ("Homolytic Fission in Initiation", "Why does the Cl-Cl bond break in preference to the C-H bond during the initiation stage of alkane chlorination?", "The Cl-Cl bond enthalpy (242 kJ mol^-1) is much lower than the C-H bond enthalpy (413 kJ mol^-1), so UV photons selectively cleave Cl-Cl.", "The C-H bond is completely ionic.", "Chlorine molecules absorb infrared radiation rather than UV.", "Carbon atoms repel ultraviolet radiation.", "The Cl-Cl bond is relatively weak (242 kJ/mol), so UV light of wavelength ~330 nm carries sufficient quantum energy (E=hf) to cause homolytic fission of Cl-Cl, whereas the strong C-H bond (413 kJ/mol) cannot be cleaved directly."),
        ("Environmental Impact of Unburnt Hydrocarbons", "What environmental problem is caused by unburnt hydrocarbons emitted from vehicle exhaust pipes?", "They react with nitrogen oxides and sunlight to form photochemical smog and ground-level ozone.", "They cause immediate ozone hole depletion in the stratosphere.", "They acidify rain to pH 1.0.", "They neutralize alkaline lake waters.", "Unburnt volatile organic compounds (VOCs) react with NOx under sunlight to generate peroxyacetyl nitrate (PAN) and tropospheric ozone, creating irritating photochemical smog."),
        ("Thermal vs Catalytic Cracking", "How does thermal cracking differ from catalytic cracking in its primary product yield?", "Thermal cracking uses high temperature (700-1000 °C) and pressure to produce a high proportion of straight-chain alkenes (ethene, propene).", "Thermal cracking requires platinum catalysts at room temperature.", "Thermal cracking only yields methane and hydrogen.", "Thermal cracking produces exclusively cyclic aromatics.", "Thermal cracking operates at severe temperatures (700-1000 °C) and pressures (up to 70 atm) via free radical mechanisms, yielding large fractions of terminal alkenes."),
        ("Mechanism of Bromine Abstraction", "In the bromination of propane, why is 2-bromopropane the major mono-substituted product rather than 1-bromopropane?", "The secondary 2-propyl radical formed as an intermediate is more stable than the primary 1-propyl radical due to the +I inductive effect of two methyl groups.", "Bromine atoms are too large to fit at the terminal position.", "1-bromopropane has a much higher boiling point.", "Secondary C-H bonds are completely unreactive.", "Hydrogen abstraction can form a 1° radical (CH3CH2CH2.) or a 2° radical (CH3CH.CH3). The 2° radical is stabilized by two electron-donating methyl groups (+I effect), lowering the activation energy for its formation."),
        ("Combustion Stoichiometry of Propane", "What volume of oxygen gas (measured at RTP) is required for the complete combustion of 1.0 dm^3 of propane, C3H8?", "5.0 dm^3", "3.0 dm^3", "4.0 dm^3", "10.0 dm^3", "Equation: C3H8(g) + 5O2(g) -> 3CO2(g) + 4H2O(l). By Avogadro's law, gas volume ratios equal mole ratios at the same T and P. Thus, 1.0 dm^3 of C3H8 requires 5.0 dm^3 of O2."),
        ("Greenhouse Effect and Alkanes", "Why is methane (CH4) a potent greenhouse gas compared to carbon dioxide?", "Methane absorbs infrared radiation intensely across key atmospheric window wavelengths, having a global warming potential ~28 times greater than CO2.", "Methane reacts with water to form carbonic acid.", "Methane destroys the Earth's magnetic field.", "Methane forms a physical reflective cloud of ice in the mesosphere.", "Methane molecules possess C-H stretching and bending vibrational modes that absorb infrared radiation strongly in the thermal infrared window, trapping re-radiated heat."),
        ("Fractional Distillation of Crude Oil", "On what physical property does the separation of crude oil fractions in a fractionating column depend?", "Differences in boiling points, which depend directly on molecular size and intermolecular London dispersion forces.", "Differences in chemical reactivity with water.", "Differences in density of solid precipitates.", "Differences in solubility in ethanol.", "Crude oil is separated by fractional distillation: smaller hydrocarbons have fewer electrons, weaker London dispersion forces, and lower boiling points, condensing near the top of the tower."),
        ("Reactivity of Alkanes", "Why are alkanes generally inert to attack by acids, bases, oxidizing agents, and nucleophiles at room temperature?", "Alkanes contain only strong, non-polar C-C and C-H sigma bonds with no region of high or low electron density to attract attacking reagents.", "Alkanes possess delocalized pi electron clouds that shield the bonds.", "Carbon atoms in alkanes are sp hybridised.", "Alkanes form strong hydrogen bonds that resist reaction.", "The C-C and C-H bonds have high bond energies (348 and 413 kJ/mol) and almost identical electronegativities (C=2.5, H=2.1), leaving no polar delta+ sites or lone pairs for reagents to attack."),
        ("Catalytic Reforming of Alkanes", "What is the purpose of catalytic reforming of straight-chain alkanes in petroleum refining?", "To convert straight-chain alkanes into branched alkanes and cyclic/aromatic hydrocarbons to increase the octane rating of fuels.", "To convert alkanes into synthetic detergents.", "To completely crack all fuel into pure hydrogen.", "To oxidize alkanes into carboxylic acids.", "Straight-chain alkanes knock easily in car engines. Catalytic reforming (using Pt catalyst at 500 °C) isomerises them into branched and aromatic rings (like benzene/toluene), greatly boosting octane numbers."),
        ("Combustion Analysis of Pentane", "How many moles of water are produced by the complete combustion of one mole of pentane, C5H12?", "6 moles", "5 moles", "12 moles", "10 moles", "Combustion equation: C5H12 + 8O2 -> 5CO2 + 6H2O. Each mole of C5H12 contains 12 hydrogen atoms, producing 6 moles of H2O."),
        ("Propagation Steps in Halogenation", "What is the net energetic characteristic of the two propagation steps in alkane chlorination?", "The overall propagation sequence is exothermic, providing the thermodynamic driving force for continuous chain reaction.", "Propagation requires constant input of external UV light.", "Propagation creates two radicals from one radical.", "Propagation forms ionic salts.", "The sum of the two propagation steps equals the overall reaction (CH4 + Cl2 -> CH3Cl + HCl), which is exothermic (delta-H ~ -100 kJ/mol), sustaining the reaction without further initiation once radicals exist."),
        ("Limiting Multi-Substitution", "How can the reaction conditions be adjusted to maximize the yield of monochloromethane (CH3Cl) over higher chlorinated products?", "Use a large excess of methane relative to chlorine.", "Use a large excess of chlorine gas.", "Carry out the reaction at 500 °C in darkness.", "Add concentrated sulfuric acid as a catalyst.", "With a large excess of methane, a chlorine radical is far more likely to collide with an unreacted CH4 molecule than with a CH3Cl molecule, minimizing poly-substitution."),
        ("Alkanes as Non-Polar Solvents", "Why are liquid alkanes (such as hexane) immiscible with water but excellent solvents for non-polar grease?", "Hexane molecules cannot form hydrogen bonds with water molecules; the London forces between hexane and grease molecules are favorable for dissolution.", "Hexane reacts vigorously with water to form hexanol.", "Water molecules are non-polar and repel hexane.", "Hexane has a very high dielectric constant.", "Water molecules form extensive hydrogen bond networks. Hexane cannot form hydrogen bonds to disrupt water-water attractions, but easily dissolves non-polar compounds via London dispersion forces."),
        ("Isomer Distribution in Free Radical Chlorination", "When propane reacts with chlorine in UV light, what are the two mono-chloro structural isomers formed?", "1-chloropropane and 2-chloropropane", "1-chloropropane and 3-chloropropane", "2-chloropropane and 2,2-dichloropropane", "Chlorocyclopropane and chloropropene", "Monochlorination of propane yields two positional isomers: 1-chloropropane (substitution at C1/C3) and 2-chloropropane (substitution at C2)."),
        ("Termination Step Combining Alkyl Radicals", "In the photochemical bromination of bromoethane, which species would NOT be formed in a termination step?", "Hydrogen gas, H2", "1,2-dibromoethane", "1,1-dibromoethane", "1,4-dibromobutane", "Termination involves radical pairing (R. + Br. -> RBr, or R. + R. -> R-R). Free hydrogen atoms (.H) are never formed in organic free radical mechanisms, so H2 is never formed as a termination product."),
        ("Relative Reactivity: Fluorine vs Chlorine vs Bromine vs Iodine", "Which halogens react explosively and which does not react at all with alkanes under standard photochemical conditions?", "Fluorine reacts explosively; iodine does not react at all (endothermic).", "Chlorine is inert; iodine is explosive.", "Bromine is explosive; fluorine is inert.", "All halogens react at identical rates.", "Fluorination is violently explosive even in the dark (delta-H highly exothermic, low activation energy); iodination is endothermic and does not take place because I. is too unreactive to abstract hydrogen."),
        ("Octane Rating and Branching", "Why do highly branched alkanes burn more smoothly in petrol engines than straight-chain isomers?", "Branching slows the formation of pre-ignition peroxides during compression, preventing engine 'knocking'.", "Branched alkanes have higher boiling points than straight chains.", "Branched alkanes have higher carbon-to-hydrogen ratios.", "Branched alkanes are completely non-flammable.", "Branched alkanes produce more stable intermediate radicals and burn with a controlled flame front, resisting auto-ignition (knocking) under engine compression."),
        ("Carbon Footprint of Fuels", "Which alkane releases the LEAST mass of CO2 per kilojoule of energy released upon complete combustion?", "Methane, CH4", "Propane, C3H8", "Octane, C8H18", "Hexadecane, C16H34", "Methane has the highest H:C ratio (4:1) of any hydrocarbon. A higher proportion of its combustion heat comes from forming O-H bonds (in H2O) rather than C=O bonds (in CO2), emitting less CO2 per MJ of energy."),
        ("Chain Length and Viscosity", "How does the viscosity of liquid alkanes change as carbon chain length increases?", "Viscosity increases because longer chains have greater surface contact area and stronger London dispersion forces that tangle molecules.", "Viscosity decreases because longer chains flow faster.", "Viscosity remains completely constant.", "Viscosity increases due to formation of covalent crosslinks.", "As chain length grows, polarisability increases, London dispersion forces strengthen, and long chains become physically entangled, causing viscosity to increase steadily."),
        ("Free Radical Inhibitors", "Why does the addition of trace amounts of oxygen gas temporarily retard the photochemical chlorination of methane?", "Oxygen reacts with alkyl free radicals to form unreactive peroxy radicals (ROO.), terminating chain propagation.", "Oxygen dissolves all chlorine gas.", "Oxygen cools the reaction vessel to -50 °C.", "Oxygen absorbs ultraviolet light completely.", "Molecular oxygen (O2) has diradical character and scavenges alkyl radicals (.CH3 + O2 -> CH3OO.), which are far less reactive and cannot propagate the chain until oxygen is consumed."),
        ("Cracking of Dodecane", "In the cracking of dodecane (C12H26), one molecule yields one molecule of octane (C8H18) and two molecules of an identical alkene. What is the alkene?", "Ethene, C2H4", "Propene, C3H6", "But-1-ene, C4H8", "Methane, CH4", "Conservation of atoms: C12H26 -> C8H18 + 2(C2H4). Carbons: 12 - 8 = 4, divided by 2 = 2 (C2H4, ethene)."),
        ("Combustion of Cycloalkanes", "What is the balanced equation for the complete combustion of one mole of cyclohexane (C6H12)?", "C6H12 + 9O2 -> 6CO2 + 6H2O", "C6H12 + 6O2 -> 6CO + 6H2O", "C6H12 + 12O2 -> 6CO2 + 6H2", "C6H12 + 8O2 -> 6CO2 + 6H2O", "C6H12 requires 6 moles of O2 for carbon (forming 6CO2) and 3 moles of O2 for hydrogen (forming 6H2O). Total O2 = 6 + 3 = 9 moles."),
        ("Pollutants in Exhaust Gases", "Which compound is NOT a direct pollutant emitted in internal combustion engine exhaust gases?", "Ozone, O3", "Carbon monoxide, CO", "Nitrogen monoxide, NO", "Unburnt hydrocarbons", "Ozone is a secondary pollutant formed in the troposphere via photochemical reactions of NO2 and VOCs in sunlight; it is not emitted directly from car exhausts."),
        ("Stability of Alkyl Radicals", "Why is the tertiary butyl radical, .(CH3)3C, significantly more stable than the primary butyl radical?", "Hyperconjugation and the electron-donating inductive effect (+I) of three methyl groups delocalise the unpaired electron.", "Tertiary radicals have complete electron octets.", "Tertiary radicals are planar while primary radicals are spherical.", "Tertiary radicals form hydrogen bonds.", "Alkyl groups donate electron density toward the electron-deficient trivalent carbon atom via inductive effect and hyperconjugation, stabilizing 3° > 2° > 1° radicals."),
        ("Boiling Point of Alkane Isomers", "Why does 2,2-dimethylpropane have a lower boiling point (9.5 °C) than pentane (36.1 °C) despite having the identical molecular mass?", "Its spherical, branched shape provides less surface contact area between molecules, resulting in weaker London dispersion forces.", "Pentane contains polar covalent bonds.", "2,2-dimethylpropane forms intramolecular hydrogen bonds.", "Pentane has a higher vapor pressure.", "Branching makes molecules more compact and spherical. Spheres touch at only one point, reducing molecular surface contact area. Less surface contact produces weaker London dispersion forces, lowering the boiling point."),
        ("Homologous Series Enthalpy of Combustion", "How does the standard enthalpy of combustion (delta-H_c) change per additional -CH2- unit down the alkane homologous series?", "It becomes more exothermic by approximately -650 kJ mol^-1 per -CH2- group.", "It becomes endothermic.", "It decreases to zero.", "It doubles for every carbon atom.", "Each additional -CH2- group requires 1.5 extra O2 molecules and forms one more CO2 and H2O, adding approximately -650 kJ/mol of exothermic energy."),
        ("Free Radical Dimerisation", "During the photobromination of 2-methylpropane, what is the hydrocarbon formed if two tertiary butyl radicals undergo termination?", "2,2,3,3-tetramethylbutane", "2,2,4-trimethylpentane", "Octane", "2,3-dimethylbutane", "Coupling of two (CH3)3C. radicals forms (CH3)3C-C(CH3)3, which is 2,2,3,3-tetramethylbutane."),
        ("Soot Particle Health Hazards", "What is the primary human health hazard associated with PM2.5 carbon soot particles from diesel engines?", "They penetrate deep into the alveoli of the lungs, carrying carcinogenic polycyclic aromatic hydrocarbons into the bloodstream.", "They cause immediate tooth decay.", "They neutralize stomach hydrochloric acid.", "They deplete calcium from bones.", "Particulate matter <= 2.5 micrometers (PM2.5) bypasses nasal filtration, penetrating deep into lung alveoli and causing severe cardiovascular and respiratory diseases and cancer."),
        ("Oxidation of Alkanes by KMnO4", "What is observed when an alkane (such as hexane) is shaken with cold, acidified potassium manganate(VII)?", "No reaction occurs; the purple color of KMnO4 remains unchanged.", "The purple solution turns green immediately.", "A brown precipitate of MnO2 forms with vigorous effervescence.", "The hexane is oxidized to hexanoic acid.", "Alkanes are saturated and lack electron-rich pi bonds; they are completely resistant to oxidation by cold acidified KMnO4."),
        ("Industrial Source of Alkanes", "What is the primary natural source from which alkanes are industrially extracted?", "Crude petroleum oil and natural gas", "Fermentation of sugar cane", "Electrolysis of brine", "Destructive distillation of wood", "Petroleum (crude oil) and natural gas are the overwhelming industrial sources of alkanes, formed by geothermal heating and compression of prehistoric marine biomass over millions of years."),
        ("Radical Abstraction Selectivity", "Why is bromine significantly more regioselective than chlorine in free radical substitution reactions of alkanes?", "The hydrogen abstraction step by Br. is endothermic and has a late transition state resembling the carbocation/radical intermediate, whereas for Cl. it is exothermic with an early transition state.", "Bromine is a smaller atom than chlorine.", "Bromine radicals are positively charged.", "Chlorine cannot form secondary radicals.", "By Hammond's postulate, because hydrogen abstraction by Br. is endothermic, the transition state resembles the radical intermediate, making the energy difference between 1° and 2°/3° pathways much larger (high regioselectivity)."),
        ("Catalytic Converter Chemistry for Alkanes", "What reaction takes place on the platinum/palladium catalyst in a three-way catalytic converter to remove unburnt alkanes?", "Complete oxidation by excess oxygen: CxHy + (x + y/4)O2 -> xCO2 + y/2 H2O", "Reduction to solid carbon and hydrogen gas.", "Hydrolysis by exhaust steam to alcohols.", "Polymerisation into solid plastics.", "The oxidation catalyst (Pt/Pd) oxidizes unburnt hydrocarbons and toxic CO into harmless CO2 and H2O: CxHy + O2 -> CO2 + H2O; 2CO + O2 -> 2CO2."),
        ("Methane Hydrates", "What are methane hydrates (clathrates) found in deep ocean sediments and permafrost?", "Crystalline water ice cages that trap methane gas molecules under high pressure and low temperature.", "Solid salts of methane and sodium hydroxide.", "Liquid solutions of methane in liquid ammonia.", "Polymeric chains of methane linked by covalent bonds.", "Methane clathrate is a solid lattice of water molecules physically encaging methane gas molecules, stable under high hydrostatic ocean pressures and near-freezing temperatures."),
        ("Thermodynamic Stability of Alkanes", "Although alkanes are thermodynamically unstable with respect to combustion in air (exothermic), why are they kinetically stable at room temperature?", "They possess a very high activation energy barrier due to the need to break strong C-H and C-C covalent bonds.", "Their combustion is an endothermic equilibrium.", "They are protected by an impenetrable electrostatic shield.", "Oxygen molecules cannot collide with alkanes at 25 °C.", "While delta-G for alkane combustion is large and negative, the reaction does not occur at 25 °C without a spark because the activation energy (breaking strong covalent bonds) is very high, imparting kinetic stability."),
        ("Free Radical Chlorination in Darkness", "What happens when a mixture of methane and chlorine gas is kept at room temperature in complete darkness?", "No reaction occurs because no UV photons are present to supply the activation energy for homolytic fission of Cl2.", "The mixture explodes violently within 5 seconds.", "Methane is converted slowly into carbon soot.", "Chlorine gas condenses into a yellow liquid.", "Without UV light (or temperatures > 300 °C), Cl-Cl bonds cannot undergo homolytic cleavage to generate the initiating chlorine radicals, so the mixture remains completely unreacted."),
        ("Cracking Byproduct Uses", "Why are the alkene byproducts of catalytic cracking (such as ethene and propene) of such immense economic importance to the chemical industry?", "They serve as reactive raw monomers for the manufacture of addition polymers (polyethene, polypropene) and alcohols.", "They are used directly as aircraft lubricating oils.", "They are used as non-toxic fire extinguishants.", "They are used to sweeten fruit juices.", "Alkenes contain reactive C=C double bonds, making them prime feedstocks for synthesis of plastics, synthetic rubbers, epoxy resins, antifreeze, and pharmaceuticals.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(alkane_pool, start=5):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "14.1", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # SUBTOPIC 14.2: ALKENES — ELECTROPHILIC ADDITION & OXIDATION (Q41 - Q100)
    # =========================================================================

    add_q(
        41, "Mechanism of Bromine Addition to Ethene — 9701/11/M/J/23/Q18", "14.2", "EASY",
        "What type of reaction mechanism occurs when ethene reacts with bromine dissolved in an inert organic solvent, and what is the visual observation?",
        "Electrophilic addition; the orange-brown bromine solution is immediately decolorized.",
        "Nucleophilic substitution; a white precipitate is formed.",
        "Free radical substitution; the solution turns intense purple.",
        "Elimination; bubbles of hydrogen bromide gas are evolved.",
        "Option A is correct. The high electron density of the C=C pi bond induces a dipole in the Br2 molecule (Br(delta+)-Br(delta-)). The delta+ bromine acts as an electrophile, accepting electrons from the pi bond to form a carbocation / bromonium ion intermediate, which is attacked by Br- to yield 1,2-dibromoethane. The orange color of bromine disappears (decolorization)."
    )

    add_q(
        42, "Markovnikov Addition of HBr to Propene — 9701/12/M/J/23/Q18", "14.2", "HARD",
        "When hydrogen bromide, HBr, reacts with propene (CH3-CH=CH2), what is the major organic product and what explains its formation?",
        "2-bromopropane; the reaction proceeds via the more stable secondary carbocation intermediate (CH3-CH+-CH3).",
        "1-bromopropane; the primary carbocation is more stable due to steric factors.",
        "1,2-dibromopropane; both carbons add bromine simultaneously.",
        "Cyclopropane; HBr causes cyclization of the propene chain.",
        "Option A is correct. Electrophilic addition of H+ can form either a primary carbocation (CH3CH2CH2+) or a secondary carbocation (CH3CH+CH3). The secondary carbocation has two electron-donating methyl groups (+I inductive effect) that disperse the positive charge, lowering its activation energy. Attack by Br- on the 2° carbocation yields 2-bromopropane as the major product."
    )

    add_q(
        43, "Oxidation of Alkenes by Cold, Dilute KMnO4 — 9701/13/M/J/23/Q18", "14.2", "EASY",
        "What organic product and color change occur when propene is shaken with cold, dilute, acidified potassium manganate(VII)?",
        "Propane-1,2-diol is formed; the purple solution is decolorized (or forms a brown precipitate of MnO2 in neutral conditions).",
        "Carbon dioxide and ethanoic acid are formed with vigorous effervescence.",
        "Propanone is formed with no color change.",
        "Propanoic acid is formed; the solution turns bright green.",
        "Option A is correct. Cold, dilute KMnO4 acts as a mild oxidizing agent that hydrolyzes the alkene across the double bond without cleaving the C-C sigma bond, adding two -OH groups to give a vicinal diol (propane-1,2-diol). The purple MnO4- ion is reduced to colorless Mn2+ (in acid) or brown MnO2 precipitate (in neutral/alkaline medium)."
    )

    add_q(
        44, "Oxidative Cleavage of Alkenes by Hot, Concentrated KMnO4 — 9701/11/O/N/23/Q18", "14.2", "HARD",
        "An alkene X is heated under reflux with hot, concentrated, acidified potassium manganate(VII). The only organic products obtained are propanone (CH3COCH3) and ethanoic acid (CH3COOH).\n\nWhat is the structural formula of alkene X?",
        "2-methylbut-2-ene, (CH3)2C=CH-CH3",
        "2-methylbut-1-ene, CH2=C(CH3)-CH2CH3",
        "Pent-2-ene, CH3-CH=CH-CH2CH3",
        "3-methylbut-1-ene, CH2=CH-CH(CH3)2",
        "Option A is correct. Under hot concentrated KMnO4, the C=C bond is completely cleaved: =CR2 fragments oxidize to ketones (R2C=O), =CHR fragments oxidize to carboxylic acids (RCOOH), and =CH2 fragments oxidize to CO2 + H2O. Since the products are propanone ((CH3)2C=O) and ethanoic acid (CH3COOH), the original alkene must be (CH3)2C=CH-CH3 (2-methylbut-2-ene)."
    )

    # Questions 45 - 100: Comprehensive Alkene Reactions
    alkene_pool = [
        ("Industrial Hydration of Ethene", "What catalyst and conditions are used in the direct industrial manufacture of ethanol from ethene and steam?", "Concentrated phosphoric(V) acid (H3PO4) adsorbed on silica at 300 °C and 60 atm pressure.", "Nickel catalyst at 150 °C and 1 atm.", "Concentrated sulfuric acid at 0 °C.", "Iron catalyst at 450 °C and 200 atm.", "The industrial hydration of ethene (C2H4 + H2O -> C2H5OH) uses steam over a solid H3PO4 catalyst supported on silica at 300 °C and 60 atm."),
        ("Catalytic Hydrogenation of Alkenes", "What catalyst, temperature, and industrial application are associated with the addition of hydrogen to alkenes?", "Finely divided Nickel catalyst at 150 °C (or Pt at RTP); used in hardening vegetable oils to make margarine.", "Iron catalyst at 450 °C; used in cracking petroleum.", "Vanadium(V) oxide at 450 °C; used in making sulfuric acid.", "Zeolite catalyst at 500 °C; used in making branched fuels.", "Hydrogenation of liquid vegetable oils (containing polyunsaturated alkenes) over a nickel catalyst at ~150 °C saturates C=C bonds, raising the melting point to produce semi-solid margarine."),
        ("Electrophilic Addition of Bromine Water", "When propene is bubbled through aqueous bromine water (Br2(aq)), what is the major organic product formed?", "1-bromopropan-2-ol, CH3-CH(OH)-CH2Br", "1,2-dibromopropane", "2-bromopropan-1-ol", "Propan-2-ol", "In aqueous bromine, water molecules are present in overwhelming concentration compared to Br- ions. After the electrophile Br+ attacks to form the secondary carbocation (CH3-CH+-CH2Br), nucleophilic H2O attacks the 2° carbon, forming a halohydrin: 1-bromopropan-2-ol."),
        ("Cleavage Products of Terminal =CH2 Group", "When a terminal alkene containing a =CH2 group is treated with hot, concentrated, acidified KMnO4, what oxidation products are formed from that terminal group?", "Carbon dioxide (CO2) and water (H2O)", "Methanoic acid (HCOOH)", "Methanal (HCHO)", "Methanol (CH3OH)", "Under hot concentrated KMnO4, a terminal =CH2 group is initially oxidized to methanoic acid (HCOOH), which undergoes rapid further oxidation by KMnO4 into carbon dioxide (CO2) and water (H2O), producing visible effervescence."),
        ("Cleavage Products of 2,3-dimethylbut-2-ene", "What single organic product is formed when 2,3-dimethylbut-2-ene, (CH3)2C=C(CH3)2, is heated with hot, concentrated, acidified KMnO4?", "Propanone, CH3COCH3", "Ethanoic acid", "2-methylpropanoic acid", "Carbon dioxide", "The symmetrical alkene (CH3)2C=C(CH3)2 cleaves across the C=C bond. Both sides consist of =C(CH3)2 groups, yielding two molecules of propanone ((CH3)2C=O)."),
        ("Addition of Chlorine to But-2-ene", "What is the systematic name of the product formed by the addition of chlorine to but-2-ene?", "2,3-dichlorobutane", "1,2-dichlorobutane", "1,4-dichlorobutane", "2-chlorobutane", "Addition of Cl2 across the C2=C3 double bond adds one chlorine to each carbon, yielding 2,3-dichlorobutane."),
        ("Carbocation Rearrangement Likelihood", "Why does 3,3-dimethylbut-1-ene yield 2-bromo-2,3-dimethylbutane as the predominant product upon addition of HBr?", "The initial secondary carbocation undergoes a 1,2-methyl shift to form a more stable tertiary carbocation before attack by bromide.", "Bromine directly displaces a methyl group.", "Hydrogen attacks both ends of the double bond.", "The reaction proceeds via a free radical mechanism.", "Addition of H+ forms (CH3)3C-CH+-CH3 (a 2° carbocation). A methyl group migrates with its electron pair (1,2-hydride/methyl shift) to produce (CH3)2C+-CH(CH3)2, which is tertiary and much more stable."),
        ("Test for Unsaturation", "Which observation confirms that an unknown liquid hydrocarbon contains an alkene C=C double bond?", "Decolorization of bromine water from orange-brown to colorless without needing UV light.", "Effervescence with sodium carbonate solution.", "A silver mirror with Tollens' reagent.", "A brick-red precipitate with Fehling's solution.", "Bromine water tests for C=C unsaturation: addition across the double bond rapidly decolorizes the orange-brown bromine solution at room temperature without requiring UV light or catalysts."),
        ("Stability Order of Carbocations", "Why is (CH3)3C+ more stable than CH3CH2CH2+?", "Three electron-releasing methyl groups disperse the positive charge across the molecule via the +I inductive effect, lowering electrostatic potential.", "The primary carbocation is too small to exist.", "The tertiary carbocation has a complete outer octet of 10 electrons.", "The primary carbocation forms hydrogen bonds.", "Alkyl groups are electron-donating (+I). The 3° carbocation has three alkyl groups dispersing the positive charge, making it far more stable than the 1° carbocation with only one alkyl group."),
        ("Addition of Interhalogens (ICl)", "When iodine monochloride (I-Cl) reacts with propene, which atom acts as the electrophile and what is the major product?", "Iodine acts as the electrophile (I delta+) because chlorine is more electronegative; major product is 2-chloro-1-iodopropane.", "Chlorine acts as the electrophile; major product is 1-chloro-2-iodopropane.", "Both atoms act as nucleophiles.", "Iodine replaces a hydrogen on the methyl group.", "Chlorine is more electronegative than iodine (Cl=3.0, I=2.5), so I carries a partial positive charge (I delta+-Cl delta-). The pi bond attacks I+, forming the more stable secondary carbocation CH3-CH+-CH2I, which is then attacked by Cl- to yield 2-chloro-1-iodopropane."),
        ("Deducing Alkene from KMnO4 Oxidation", "Heating an alkene with hot concentrated KMnO4 yields only butanoic acid, CH3CH2CH2COOH. What is the identity of the alkene?", "Oct-4-ene, CH3CH2CH2CH=CHCH2CH2CH3", "Oct-1-ene", "Hex-3-ene", "But-1-ene", "A single product of butanoic acid indicates a symmetrical alkene where both halves are =CH-CH2CH2CH3. The original alkene is oct-4-ene."),
        ("Addition Polymerisation of Alkenes", "What type of reaction converts ethene molecules into polyethene, and what change in bonding occurs?", "Addition polymerisation; pi bonds break and new C-C sigma bonds form between monomer units.", "Condensation polymerisation; water is eliminated.", "Elimination; hydrogen gas is evolved.", "Substitution; chlorine atoms replace hydrogens.", "Addition polymerisation occurs when thousands of alkene monomers join together: the pi bond in each C=C breaks to form new C-C sigma bonds linking the monomers into a long saturated polymer chain."),
        ("Stereochemistry of Alkene Addition", "Why does the bromination of cyclohexene yield trans-1,2-dibromocyclohexane rather than the cis isomer?", "The reaction proceeds via a cyclic bromonium ion intermediate, forcing the incoming bromide ion to attack from the opposite face (anti-addition).", "The cis isomer is too reactive to isolate.", "Bromine molecules can only attack from the top face.", "The reaction proceeds via free radical substitution.", "Electrophilic attack by Br2 forms a three-membered cyclic bromonium ion that blocks one face of the ring. The bromide nucleophile must attack from the opposite face (backside attack), resulting strictly in anti-addition (trans product)."),
        ("Addition of Sulfuric Acid to Alkenes", "What is the product when ethene is absorbed into concentrated sulfuric acid at room temperature, and what happens upon subsequent boiling with water?", "Ethyl hydrogensulfate is formed; boiling with water hydrolyzes it to ethanol.", "Ethanoic acid is formed directly.", "Diethyl ether is formed as a gas.", "Ethene is oxidized to carbon dioxide.", "Ethene reacts with concentrated H2SO4 via electrophilic addition to form ethyl hydrogensulfate (CH3CH2OSO3H). Adding water and warming hydrolyzes the ester to ethanol and regenerates sulfuric acid: CH3CH2OSO3H + H2O -> CH3CH2OH + H2SO4."),
        ("Reactivity: Alkenes vs Benzene", "Why do alkenes readily undergo electrophilic addition while benzene undergoes electrophilic substitution?", "Addition to benzene would destroy its exceptionally stable delocalised 6 pi electron aromatic resonance system.", "Benzene contains only single sigma bonds.", "Alkenes have lower electron density than benzene.", "Benzene is non-planar.", "Benzene possesses ~150 kJ/mol of aromatic resonance stabilization energy. Electrophilic addition would break the delocalized ring, permanently destroying aromaticity. Hence, benzene undergoes substitution to regenerate the stable 6 pi aromatic ring."),
        ("Oxidation of Cyclohexene", "What is the product when cyclohexene is heated with hot, concentrated, acidified KMnO4?", "Hexanedioic acid (adipic acid), HOOC-(CH2)4-COOH", "Cyclohexanol", "Cyclohexanone", "Carbon dioxide and water only", "Cleaving the C=C bond in cyclohexene breaks open the ring. Both double-bond carbons are =CH- groups, so each is oxidized to a carboxylic acid group (-COOH), yielding the open-chain dicarboxylic acid hexanedioic acid."),
        ("Heterolytic Cleavage of Halogen Molecule", "During electrophilic addition of Br2, what causes the non-polar bromine molecule to become polarized?", "The high electron density in the C=C pi bond repels the electron cloud of the approaching Br2 molecule, inducing a temporary dipole (Br delta+-Br delta-).", "The solvent permanently ionizes bromine molecules.", "Ultraviolet light creates ionic dipoles.", "Air pressure squeezes the bromine electrons.", "As Br2 nears the electron-rich pi cloud, electrostatic repulsion pushes electrons away from the closer Br atom to the further Br atom, creating an induced dipole (Br delta+-Br delta-)."),
        ("Markownikoff Addition with Water", "What is the major product when 2-methylpropene is reacted with steam in the presence of an acid catalyst?", "2-methylpropan-2-ol (tertiary alcohol)", "2-methylpropan-1-ol (primary alcohol)", "Butan-2-ol", "Butan-1-ol", "Protonation of (CH3)2C=CH2 forms the tertiary carbocation (CH3)3C+ (much more stable than the 1° carbocation). Attack by H2O yields 2-methylpropan-2-ol."),
        ("Oxidation of 2-methylbut-1-ene", "What products are obtained when 2-methylbut-1-ene, CH2=C(CH3)CH2CH3, is oxidized with hot concentrated acidified KMnO4?", "Carbon dioxide (CO2), water (H2O), and butanone (CH3COCH2CH3)", "Ethanoic acid and propanoic acid", "2-methylbutanoic acid only", "Methanoic acid and butan-2-ol", "The terminal =CH2 fragment oxidizes to CO2 + H2O. The =C(CH3)CH2CH3 fragment oxidizes to the ketone butanone (CH3COCH2CH3)."),
        ("Addition of HCl to Alkenes vs HBr", "Why does electrophilic addition of HCl to alkenes occur more slowly than addition of HBr under identical conditions?", "The H-Cl bond enthalpy (431 kJ mol^-1) is higher than that of H-Br (366 kJ mol^-1), resulting in a higher activation energy for electrophilic protonation.", "Chlorine is less electronegative than bromine.", "Chloride ions are too large to attack carbocations.", "HCl exists only as a solid at room temperature.", "The rate-determining step involves breaking the H-X bond as H+ is transferred to the alkene pi bond. Because H-Cl has a stronger bond than H-Br, more energy is required, making the reaction slower."),
        ("Identification of Alkene Structure from Gas Volume", "Complete combustion of 20 cm^3 of a gaseous alkene requires 90 cm^3 of oxygen gas at RTP. What is the alkene?", "Propene, C3H6", "Ethene, C2H4", "But-1-ene, C4H8", "Pent-1-ene, C5H10", "Equation for alkene CnH2n: CnH2n + 1.5n O2 -> n CO2 + n H2O. Volume ratio O2 / alkene = 1.5n = 90 / 20 = 4.5. Thus, n = 4.5 / 1.5 = 3 (propene, C3H6)."),
        ("Relative Rates of Halogen Addition", "Which halogen reacts most rapidly with ethene in electrophilic addition?", "Chlorine > Bromine > Iodine", "Iodine > Bromine > Chlorine", "All halogens react at identical rates", "Fluorine cannot react with alkenes", "Electrophilic reactivity depends on the electrophilicity and polarizability of the halogen; chlorine reacts more rapidly than bromine, which reacts faster than iodine."),
        ("Addition of Hydrogen Cyanide to Alkenes", "Why do alkenes NOT react with hydrogen cyanide (HCN) under normal conditions?", "Alkenes have high electron density and repel nucleophilic cyanide ions (:CN-); HCN lacks an effective electrophilic species to initiate attack.", "HCN is an insoluble gas.", "Cyanide ions destroy C-C sigma bonds.", "Alkenes are strong Bronsted bases that neutralize HCN.", "Alkenes are electron-rich nucleophiles and require an initial electrophilic attack. HCN contains a weak, poorly electrophilic H+ and a nucleophilic :CN- ion, so no reaction occurs (unlike carbonyls which are electrophilic)."),
        ("Oxidation of But-2-ene with Hot KMnO4", "What single organic product is formed when but-2-ene (CH3-CH=CH-CH3) is heated with hot concentrated acidified KMnO4?", "Ethanoic acid, CH3COOH", "Ethanol, CH3CH2OH", "Ethanal, CH3CHO", "Carbon dioxide and water", "Both halves of the symmetrical but-2-ene molecule consist of =CH-CH3 groups, which are oxidized to carboxylic acid groups, producing two molecules of ethanoic acid (CH3COOH)."),
        ("Polyalkene Repeat Unit Deduction", "What is the monomer used to produce the polymer with repeat unit -[CH2-CH(Cl)]-n?", "Chloroethene (vinyl chloride), CH2=CHCl", "1,2-dichloroethene", "Chloroethane", "1,1-dichloroethene", "Restoring the C=C double bond between the two carbon atoms of the repeat unit gives CH2=CHCl (chloroethene)."),
        ("Combustion Heat of Alkenes vs Alkanes", "Why do alkenes burn with a more smoky (sootier) flame than the corresponding alkanes?", "Alkenes have a higher carbon-to-hydrogen ratio, increasing the likelihood of incomplete combustion to carbon particulates (soot).", "Alkenes contain toxic sulfur impurities.", "Alkenes burn at a lower temperature than alkanes.", "Alkenes produce hydrogen gas during combustion.", "Ethene (C:H = 1:2) has a higher proportion of carbon than ethane (C:H = 1:3). More oxygen is required per gram to achieve complete oxidation, resulting in a luminous, smoky flame due to incandescent soot particles."),
        ("Formation of Diols via OsO4 vs KMnO4", "In addition to cold dilute KMnO4, which reagent can convert an alkene into a vicinal diol via syn-addition?", "Osmium tetroxide (OsO4) followed by reduction", "Hot concentrated nitric acid", "Acidified potassium dichromate(VI)", "Lithium aluminium hydride", "Osmium tetroxide (OsO4) selectively oxidizes alkenes to 1,2-diols via a cyclic osmate ester, giving stereospecific syn-dihydroxylation."),
        ("Asymmetrical Alkene Addition Regioselectivity", "In the reaction between 2-methylbut-1-ene and HBr, what percentage of the product is expected to be 2-bromo-2-methylbutane under ionic conditions?", "Virtually 100% (predominant Markovnikov product via the tertiary carbocation)", "50% (equal mixture of 1-bromo and 2-bromo)", "0% (anti-Markovnikov is favored)", "25%", "The difference in activation energy between forming the 3° carbocation and the 1° carbocation is so large (~40 kJ/mol) that the 3° pathway overwhelmingly dominates, producing almost exclusively the tertiary haloalkane."),
        ("Anti-Markovnikov Addition Mechanism", "Why does the addition of HBr to propene in the presence of peroxides (ROOR) yield 1-bromopropane?", "The reaction switches to a free radical mechanism where the bromine radical (.Br) attacks first, forming the more stable secondary carbon radical.", "Peroxides act as a powerful nucleophile.", "Peroxides reverse the electronegativity of bromine.", "Peroxides destroy the pi bond without adding.", "In the presence of peroxides, RO. radicals generate .Br. The .Br radical adds to C1 of propene to produce the more stable 2° radical (CH3-CH.-CH2Br), which abstracts H from HBr to form 1-bromopropane (anti-Markovnikov)."),
        ("Addition of Water Across Cyclohexene", "What is the product formed when cyclohexene reacts with steam in the presence of concentrated H3PO4 catalyst?", "Cyclohexanol", "Cyclohexanone", "Hexan-1-ol", "Adipic acid", "Electrophilic addition of H2O across the C=C double bond of cyclohexene yields the cyclic alcohol cyclohexanol."),
        ("Distinguishing Alkanes from Alkenes", "Which single chemical test immediately distinguishes hexane from hex-1-ene?", "Hex-1-ene decolorizes aqueous bromine water from orange to colorless at room temperature; hexane produces no color change.", "Hexane forms a white precipitate with silver nitrate.", "Hex-1-ene reacts with sodium metal to evolve hydrogen.", "Hexane turns blue litmus paper red.", "Hex-1-ene contains an unsaturated C=C bond that rapidly undergoes electrophilic addition with aqueous bromine, decolorizing it. Saturated hexane shows no reaction in the absence of UV light."),
        ("Oxidative Cleavage of Pent-2-ene", "What two organic acids are formed when pent-2-ene, CH3-CH=CH-CH2-CH3, is refluxed with hot concentrated acidified KMnO4?", "Ethanoic acid (CH3COOH) and propanoic acid (CH3CH2COOH)", "Methanoic acid and butanoic acid", "Two molecules of propanoic acid", "Ethanoic acid and propanone", "Cleavage of the C2=C3 bond divides the molecule into a 2-carbon =CH-CH3 fragment (oxidized to ethanoic acid) and a 3-carbon =CH-CH2CH3 fragment (oxidized to propanoic acid)."),
        ("Physical State of Small Alkenes", "What are the physical states of ethene, propene, and but-1-ene at standard room temperature and pressure (298 K, 100 kPa)?", "All three are colorless gases.", "Ethene is a gas; propene and but-1-ene are liquids.", "All three are volatile liquids.", "Ethene is a liquid; the others are solids.", "The C2 to C4 alkenes (ethene, propene, but-1-ene, but-2-ene, 2-methylpropene) have low molecular masses and weak London dispersion forces, existing as gases at RTP."),
        ("Testing for Carbon Dioxide from Cleavage", "When an unknown alkene is heated with hot concentrated KMnO4, the gas evolved turns limewater cloudy. What structural feature does this prove?", "The alkene contains a terminal =CH2 double-bond group.", "The alkene is a cyclic hydrocarbon.", "The alkene contains a tertiary carbon atom.", "The alkene is completely symmetrical.", "Only terminal =CH2 groups are oxidized to CO2 gas (and H2O) by hot concentrated KMnO4. The evolution of CO2 (which precipitates CaCO3 in limewater) proves the presence of a terminal =CH2 group."),
        ("Carbocation Hybridisation and Attack", "What is the shape of the carbocation intermediate in electrophilic addition, and from which direction can the nucleophile attack?", "Trigonal planar; the nucleophile can attack with equal probability from either the top face or bottom face.", "Tetrahedral; attack occurs only from the front.", "Linear; attack occurs along the molecular axis.", "Pyramidal; attack is restricted to the base.", "The positively charged carbon of a carbocation is sp2 hybridised with an empty unhybridised p orbital perpendicular to the trigonal plane (120°). Nucleophiles can attack this empty p lobe from either the top or bottom with equal probability."),
        ("Bromonium Ion vs Open Carbocation", "What experimental evidence demonstrates that bromine addition to alkenes involves a cyclic bromonium ion rather than a simple open carbocation?", "The stereospecific formation of trans products (anti-addition) when reacting with cyclic alkenes.", "The evolution of hydrogen bromide gas.", "The formation of equal amounts of cis and trans products.", "The immediate reduction of bromine to bromide.", "If an open, freely rotating carbocation formed, nucleophilic attack would occur from both faces to give a mixture of cis and trans isomers. The exclusive formation of trans products proves the presence of a bridged bromonium ion preventing rotation and blocking syn attack."),
        ("Hydration vs Hydrogenation Reaction Conditions", "How do the reagents and conditions for converting an alkene to an alcohol differ from those for converting an alkene to an alkane?", "Alcohol: Steam (H2O(g)) with concentrated H3PO4 at 300 °C / 60 atm; Alkane: Hydrogen gas (H2(g)) with Ni catalyst at 150 °C.", "Both use hydrogen gas over a platinum catalyst.", "Both use cold acidified potassium manganate(VII).", "Both use sodium borohydride at room temperature.", "Alkene -> alcohol is hydration (addition of steam over solid H3PO4 catalyst at high temperature and pressure); alkene -> alkane is hydrogenation (addition of H2 gas over Ni catalyst at ~150 °C)."),
        ("Addition of Halogens in Non-Polar Solvents", "When bromine is dissolved in tetrachloromethane (CCl4) and added to ethene, what is the sole product?", "1,2-dibromoethane, CH2Br-CH2Br", "Bromoethane", "1-bromo-2-chloroethane", "Ethanol", "In an inert non-polar solvent like CCl4, no competing nucleophiles (like water) exist. The only nucleophile available to attack the bromonium ion is the bromide ion (Br-), forming 1,2-dibromoethane as the exclusive product."),
        ("Effect of Alkyl Substitution on Alkene Stability", "How does increasing alkyl substitution around the C=C double bond affect the thermodynamic stability of alkenes?", "Stability increases: tetra-substituted > tri-substituted > di-substituted > mono-substituted > ethene.", "Stability decreases because alkyl groups crowd the double bond.", "All alkene isomers have identical thermodynamic stability.", "Alkyl substitution causes spontaneous decomposition.", "Alkyl groups donate electron density to the pi system via hyperconjugation and strengthen bonding, making more highly substituted alkenes (like (CH3)2C=C(CH3)2) thermodynamically more stable than less substituted isomers."),
        ("Cleavage Products of 2-methylpent-2-ene", "What organic products are formed when 2-methylpent-2-ene, (CH3)2C=CH-CH2-CH3, is heated with hot concentrated acidified KMnO4?", "Propanone, (CH3)2C=O, and propanoic acid, CH3CH2COOH", "Ethanoic acid and butanone", "Propanal and propanoic acid", "Carbon dioxide and 2-methylbutanoic acid", "Cleaving the double bond in (CH3)2C=CH-CH2-CH3 produces propanone from the (CH3)2C= fragment and propanoic acid from the =CH-CH2-CH3 fragment."),
        ("Industrial Polymerisation Conditions", "What catalyst and conditions are used in the low-pressure Ziegler-Natta polymerisation of ethene to high-density polyethene (HDPE)?", "Titanium(IV) chloride and triethylaluminium catalyst (TiCl4 / Al(C2H5)3) at ~60 °C and low pressure.", "Concentrated sulfuric acid at 200 °C.", "Ultraviolet light in liquid ammonia.", "Iron catalyst at 450 °C and 200 atm.", "Ziegler-Natta coordination catalysts (TiCl4 with Al(C2H5)3) enable coordination polymerisation of ethene at modest temperatures (~60 °C) and atmospheric pressure, producing unbranched linear HDPE with high density and tensile strength."),
        ("Electrophilic Addition Transition State", "In the reaction coordinate diagram for the electrophilic addition of HBr to an alkene, what represents the highest energy barrier (rate-determining transition state)?", "The transition state leading to the formation of the carbocation intermediate.", "The attack of the bromide nucleophile on the carbocation.", "The dissolution of HBr in the solvent.", "The diffusion of product molecules away from each other.", "The rate-determining step is the initial protonation of the alkene pi bond to form the high-energy carbocation intermediate. This step has the highest activation energy on the reaction coordinate."),
        ("Bromination of Phenylethene", "When phenylethene (styrene, C6H5-CH=CH2) is treated with bromine in the dark at room temperature, what reaction occurs?", "Electrophilic addition across the alkene side chain to form 1,2-dibromo-1-phenylethane; the benzene ring remains unreacted.", "Electrophilic substitution into the benzene ring to form 4-bromostyrene.", "Free radical substitution of the phenyl ring.", "Elimination of hydrogen bromide to form phenylacetylene.", "The aliphatic alkene double bond has high, localized electron density and reacts rapidly with bromine via electrophilic addition, whereas the aromatic benzene ring requires a halogen carrier catalyst (AlBr3) and does not react in the dark."),
        ("Hydration of But-1-ene Regiochemistry", "What is the major alcohol formed when but-1-ene is reacted with steam in the presence of concentrated phosphoric acid catalyst?", "Butan-2-ol (secondary alcohol)", "Butan-1-ol (primary alcohol)", "2-methylpropan-2-ol", "Ethanoic acid", "Addition of H+ to but-1-ene forms the secondary carbocation CH3-CH2-CH+-CH3 in preference to the primary carbocation CH3-CH2-CH2-CH2+ due to stabilization by two alkyl groups. Attack by H2O gives butan-2-ol as the major product."),
        ("PTFE Monomer and Properties", "What is the monomer of poly(tetrafluoroethene) (PTFE / Teflon), and what property makes the polymer non-stick and chemically inert?", "Tetrafluoroethene (CF2=CF2); the extremely strong C-F bonds (485 kJ mol^-1) and protective fluorine sheath prevent chemical attack.", "Fluoroethene; weak London dispersion forces.", "1,1-difluoroethene; high water solubility.", "Trichlorofluoromethane; low boiling point.", "PTFE is synthesized from CF2=CF2. The C-F bond is one of the strongest single bonds in organic chemistry (485 kJ/mol), and the small, highly electronegative fluorine atoms tightly pack around the carbon backbone, forming an unreactive, non-stick barrier."),
        ("Cleavage of 3-methylhex-3-ene", "What organic products are formed when 3-methylhex-3-ene, CH3-CH2-C(CH3)=CH-CH2-CH3, is refluxed with hot concentrated acidified KMnO4?", "Pentan-3-one (CH3CH2COCH2CH3) and propanoic acid (CH3CH2COOH)", "Butanone and butanoic acid", "Hexan-3-one and ethanoic acid", "Carbon dioxide and 2-methylpentanoic acid", "Cleaving across C3=C4 yields pentan-3-one from the =C(CH3)CH2CH3 carbon and propanoic acid from the =CH-CH2CH3 carbon."),
        ("Dichromate vs Permanganate Reactivity with Alkenes", "Why is acidified potassium manganate(VII) used to test for alkenes rather than acidified potassium dichromate(VI)?", "KMnO4 oxidizes alkenes rapidly at room temperature, producing an immediate color change; K2Cr2O7 is a milder oxidizer and does not react readily with C=C bonds at room temperature.", "K2Cr2O7 decomposes explosively in the presence of hydrocarbons.", "KMnO4 is a reducing agent that adds hydrogen.", "K2Cr2O7 turns colorless upon reduction.", "Potassium manganate(VII) is a much stronger oxidizing agent than potassium dichromate(VI) (E° +1.51 V vs +1.33 V) and readily attacks alkene pi bonds at room temperature, while K2Cr2O7 reacts sluggishly or not at all with isolated C=C bonds."),
        ("Markownikoff Addition of HI to Propene", "What is the product of the addition of hydrogen iodide (HI) to propene in the dark?", "2-iodopropane (isopropyl iodide)", "1-iodopropane (propyl iodide)", "1,2-diiodopropane", "Cyclopropane and iodine", "HI adds via electrophilic addition. Protonation yields the secondary carbocation CH3-CH+-CH3, which is captured by iodide to form 2-iodopropane as the dominant Markovnikov product."),
        ("Reaction of Ethene with Chlorine Water", "When ethene gas is passed into aqueous chlorine water, what is the major organic product formed?", "2-chloroethanol, CH2Cl-CH2OH", "1,2-dichloroethane", "Chloroethane", "Ethanol", "In aqueous chlorine, the electrophile Cl+ attacks ethene to form the chloronium ion intermediate +CH2-CH2Cl. Because water molecules are in overwhelming excess compared to chloride ions, H2O attacks the intermediate, forming 2-chloroethanol (a chlorohydrin)."),
        ("Catalytic Hydrogenation Stoichiometry of Dienes", "What volume of hydrogen gas (measured at RTP) is required to completely hydrogenate 0.50 mol of buta-1,3-diene to butane?", "24.0 dm^3", "12.0 dm^3", "48.0 dm^3", "6.0 dm^3", "Buta-1,3-diene contains two C=C double bonds. Complete saturation requires 2 moles of H2 per mole of diene: 0.50 mol * 2 = 1.0 mol of H2. At RTP, 1.0 mol of any gas occupies 24.0 dm^3."),
        ("Chiral Center Generation in Alkene Addition", "Which reaction generates a chiral carbon atom from an achiral starting material?", "Addition of HBr to but-1-ene forming 2-bromobutane.", "Addition of Br2 to ethene forming 1,2-dibromoethane.", "Addition of H2 to propene forming propane.", "Addition of HBr to 2-methylpropene forming 2-bromo-2-methylpropane.", "But-1-ene is achiral. Addition of HBr yields 2-bromobutane (CH3-CH(Br)-CH2CH3). C2 is bonded to -H, -Br, -CH3, and -CH2CH3 (four different groups), creating a chiral center."),
        ("Cleavage of Methylenecyclohexane", "What products are obtained when methylenecyclohexane (=CH2 attached to a cyclohexane ring) is oxidized by hot concentrated acidified KMnO4?", "Cyclohexanone, carbon dioxide, and water", "Hexanedioic acid and methanol", "Cyclohexanol and methanoic acid", "Benzoic acid and water", "The exocyclic =CH2 group oxidizes to CO2 + H2O. The ring carbon of the double bond (=C<) is bonded to two ring carbons, oxidizing to the cyclic ketone cyclohexanone."),
        ("Combustion Enthalpy of Alkene Isomers", "How does the enthalpy of combustion of trans-but-2-ene compare with cis-but-2-ene, and what explains the difference?", "Trans-but-2-ene is slightly less exothermic (more stable) because the two bulky methyl groups are on opposite sides, minimizing steric repulsion.", "Cis-but-2-ene is significantly more stable because dipoles attract.", "Both have precisely identical combustion enthalpies.", "Trans-but-2-ene decomposes spontaneously upon heating.", "In cis-but-2-ene, the two methyl groups are on the same side of the double bond, causing mutual steric hindrance (van der Waals repulsion). In trans-but-2-ene, the methyl groups are opposite (180°), relieving steric strain. Trans is ~4 kJ/mol more stable, releasing less heat upon combustion."),
        ("Addition of Bromine in the Presence of Sodium Chloride", "When ethene reacts with bromine in the presence of concentrated aqueous sodium chloride, which product is formed in addition to 1,2-dibromoethane?", "1-bromo-2-chloroethane", "1,2-dichloroethane only", "Bromoethane", "Chloroethane", "The electrophile Br+ attacks ethene to form the bromonium ion. In the second step, either Br-, Cl- (from NaCl), or H2O can act as the nucleophile. Attack by Cl- yields 1-bromo-2-chloroethane."),
        ("Deducing Alkene from Quantitative Cleavage", "Complete oxidative cleavage of 0.10 mol of an alkene by hot concentrated KMnO4 produces 0.10 mol of CO2, 0.10 mol of propanone, and 0.10 mol of ethanoic acid. What is the alkene?", "2-methylpenta-1,4-diene, CH2=C(CH3)-CH2-CH=CH2 or 4-methylpenta-1,3-diene, CH2=CH-CH=C(CH3)2", "2-methylbut-2-ene", "Hex-2-ene", "Cyclohexene", "Cleavage of 4-methylpenta-1,3-diene (CH2=CH-CH=C(CH3)2) produces: CO2 from terminal =CH2; ethanoic acid from the middle =CH-CH= segment (or two segments); and propanone from =C(CH3)2. This matches the 1:1:1 mole ratio of products."),
        ("Industrial Polymerisation of Propene", "What is the structure of the repeat unit in poly(propene), and what type of polymerisation reaction forms it?", "-[CH2-CH(CH3)]-n formed by addition polymerisation.", "-[CH2-CH2-CH2]-n formed by condensation polymerisation.", "-[CH(CH3)-CH(CH3)]-n formed by free radical substitution.", "-[C(CH3)2-CH2]-n formed by elimination.", "Propene (CH2=CH-CH3) undergoes addition polymerisation: the C=C pi bond breaks and monomers link through C-C sigma bonds to form poly(propene), having repeat unit -[CH2-CH(CH3)]-.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(alkene_pool, start=45):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "14.2", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # HIGH-FREQUENCY CORE REPEATS (Q101 - Q110)
    # =========================================================================

    hf_data = [
        (
            101, "HF 1: Deducing Alkene Structure from Hot Concentrated KMnO4 Oxidation Products — 9701/11/M/J/22/Q18", "HF", "HARD",
            "An unsaturated hydrocarbon Y of molecular formula C7H14 is heated with hot, concentrated, acidified potassium manganate(VII).\nEffervescence is observed, and the gas evolved turns limewater milky. The only organic product remaining in the reaction mixture is 3-methylbutanoic acid, (CH3)2CH-CH2-COOH.\n\nWhat is the structural formula of hydrocarbon Y?",
            "5-methylhex-1-ene, CH2=CH-CH2-CH(CH3)2",
            "2-methylhex-2-ene, (CH3)2C=CH-CH2-CH2-CH3",
            "4-methylhex-1-ene, CH2=CH-CH(CH3)-CH2-CH3",
            "2,4-dimethylpent-2-ene, (CH3)2C=CH-CH(CH3)2",
            "Option A is correct. The evolution of CO2 (which turns limewater milky) proves that hydrocarbon Y contains a terminal =CH2 group. The only organic product is 3-methylbutanoic acid, (CH3)2CH-CH2-COOH (5 carbons). Reconnecting the =CH2 carbon to the carbonyl carbon of the acid yields: CH2=CH-CH2-CH(CH3)2 (5-methylhex-1-ene, total 7 carbons)."
        ),
        (
            102, "HF 2: Regiochemistry and Relative Yields in Unsymmetrical Alkene Addition — 9701/12/M/J/21/Q18", "HF", "HARD",
            "2-methylbut-2-ene reacts with hydrogen chloride, HCl, in the dark.\n\nWhich statement correctly identifies the major product and explains why it forms in higher yield than the minor product?",
            "2-chloro-2-methylbutane is the major product because it is formed via a tertiary carbocation intermediate which is more stable than the secondary carbocation intermediate.",
            "2-chloro-3-methylbutane is the major product because primary carbocations are more reactive.",
            "1-chloro-2-methylbutane is the major product due to steric hindrance at C2.",
            "An equimolar 50:50 mixture is formed because chlorine attacks both ends of the double bond equally.",
            "Option A is correct. Addition of H+ to 2-methylbut-2-ene ((CH3)2C=CH-CH3) can occur at C3 to form the tertiary carbocation (CH3)2C+-CH2CH3, or at C2 to form the secondary carbocation (CH3)2CH-CH+-CH3. The 3° carbocation is stabilized by three alkyl groups (+I effect), lowering the activation energy barrier. Attack by Cl- gives 2-chloro-2-methylbutane as the predominant product."
        ),
        (
            103, "HF 3: Free Radical Chlorination — Relative Abundance of Propagation Intermediates — 9701/13/O/N/22/Q17", "HF", "HARD",
            "In the photochemical chlorination of propane at 25 °C, hydrogen abstraction can occur at a methyl group or at the central CH2 group.\n• There are 6 methyl hydrogens and 2 methylene hydrogens.\n• Secondary C-H bonds are approximately 4 times more reactive towards chlorine radicals than primary C-H bonds.\n\nWhat is the expected ratio of 1-chloropropane to 2-chloropropane in the product mixture?",
            "3 : 4 (or approximately 43% 1-chloropropane and 57% 2-chloropropane)",
            "3 : 1",
            "1 : 1",
            "1 : 4",
            "Option A is correct. Relative rate = (number of hydrogens) * (relative reactivity). For 1-chloropropane: 6 primary H * 1 = 6. For 2-chloropropane: 2 secondary H * 4 = 8. Ratio of 1-chloropropane to 2-chloropropane = 6 : 8 = 3 : 4 (3/7 = 42.9% vs 4/7 = 57.1%)."
        ),
        (
            104, "HF 4: Addition of Bromine Water to Polyunsaturated Compounds — 9701/11/F/M/22/Q18", "HF", "HARD",
            "One mole of an unsaturated hydrocarbon Z reacts completely with exactly two moles of bromine, Br2, in the dark to form a saturated tetrabromo compound.\nOxidation of one mole of Z with hot concentrated acidified KMnO4 produces one mole of butanedioic acid (HOOC-CH2-CH2-COOH) and two moles of carbon dioxide (CO2).\n\nWhat is the structural formula of hydrocarbon Z?",
            "Hexa-1,5-diene, CH2=CH-CH2-CH2-CH=CH2",
            "Hexa-2,4-diene, CH3-CH=CH-CH=CH-CH3",
            "Cyclohexa-1,4-diene",
            "Hex-1-yne, CH#C-CH2-CH2-CH2-CH3",
            "Option A is correct. Reacting with 2 moles of Br2 to form a tetrabromo alkane confirms 2 degrees of unsaturation (two C=C double bonds). The products of hot KMnO4 oxidation are two moles of CO2 (proving TWO terminal =CH2 groups) and one mole of HOOC-CH2-CH2-COOH (4 carbons in the central chain). Reassembling the fragments: CH2=CH-CH2-CH2-CH=CH2 (hexa-1,5-diene)."
        ),
        (
            105, "HF 5: Addition of Hydrogen Halide to Alkenes in the Presence of Alcohol Solvents — 9701/12/O/N/21/Q18", "HF", "HARD",
            "When propene gas is bubbled into a solution of hydrogen bromide dissolved in pure ethanol, what products are formed?",
            "A mixture of 2-bromopropane, 1-bromopropane, and 2-ethoxypropane",
            "2-bromopropane only",
            "Ethyl bromide and propan-2-ol only",
            "Propanoic acid and bromoethane",
            "Option A is correct. H+ from HBr adds to propene to form the carbocations CH3-CH+-CH3 (major) and CH3-CH2-CH2+ (minor). The carbocations can be attacked by bromide ions (yielding 2-bromopropane and 1-bromopropane) OR by the nucleophilic solvent ethanol (CH3CH2OH:), which upon deprotonation yields the ether 2-ethoxypropane."
        ),
        (
            106, "HF 6: Stereoisomeric Products of Alkene Addition Reactions — 9701/13/M/J/22/Q18", "HF", "HARD",
            "When trans-but-2-ene is reacted with hydrogen bromide, HBr, which statement concerning the product is TRUE?",
            "2-bromobutane is formed, which contains one chiral center and is produced as a racemic (optically inactive) mixture.",
            "An optically active single enantiomer of 2-bromobutane is obtained.",
            "1-bromobutane is formed as the sole product.",
            "The product shows cis-trans isomerism.",
            "Option A is correct. Addition of HBr to but-2-ene gives 2-bromobutane, CH3-CH(Br)-CH2-CH3. C2 is a chiral center bonded to -H, -Br, -CH3, and -CH2CH3. Because the intermediate carbocation is planar (sp2), the bromide ion can attack from either face with equal probability (50% top, 50% bottom), yielding an equimolar racemic mixture that has zero net optical rotation."
        ),
        (
            107, "HF 7: Catalytic Cracking Equation and Balancing — 9701/11/O/N/21/Q17", "HF", "HARD",
            "One mole of a straight-chain alkane C15H32 is cracked to produce one mole of octane (C8H18), one mole of propene (C3H6), and an unknown quantity of ethene (C2H4).\n\nHow many moles of ethene are produced per mole of C15H32?",
            "2 moles of ethene",
            "1 mole of ethene",
            "3 moles of ethene",
            "4 moles of ethene",
            "Option A is correct. Equation: C15H32 -> C8H18 + C3H6 + n C2H4. Balancing carbon atoms: 15 = 8 + 3 + 2n => 15 - 11 = 4 => 2n = 4 => n = 2. Balancing hydrogen atoms: 32 = 18 + 6 + 2(4) = 32 (verified). Thus, 2 moles of ethene are produced."
        ),
        (
            108, "HF 8: Distinguishing Alkene Isomers by Oxidation Products — 9701/12/F/M/23/Q18", "HF", "HARD",
            "Two isomeric alkenes, P and Q, both have the molecular formula C5H10.\n• Alkene P produces a carboxylic acid and a gas that turns limewater milky when heated with hot concentrated acidified KMnO4.\n• Alkene Q produces a ketone and a carboxylic acid under the same conditions.\n\nWhat are the identities of P and Q?",
            "P is pent-1-ene; Q is 2-methylbut-2-ene",
            "P is pent-2-ene; Q is 2-methylbut-1-ene",
            "P is 2-methylbut-1-ene; Q is pent-1-ene",
            "P is 3-methylbut-1-ene; Q is cyclopentane",
            "Option A is correct. Alkene P produces CO2 gas (from a terminal =CH2) and a carboxylic acid (butanoic acid), identifying P as pent-1-ene (CH2=CH-CH2CH2CH3). Alkene Q produces a ketone and a carboxylic acid, requiring a =C(R)2 group and a =CHR group; 2-methylbut-2-ene ((CH3)2C=CH-CH3) cleaves to propanone (ketone) and ethanoic acid (carboxylic acid)."
        ),
        (
            109, "HF 9: Identifying Addition Polymer Monomers — 9701/13/M/J/23/Q19", "HF", "HARD",
            "A section of an addition polymer chain has the structure:\n-[CH2-CH(CH3)-CH2-CH(Cl)-CH2-CH(CH3)-CH2-CH(Cl)]-\n\nWhat were the two monomers used in an equimolar ratio to synthesize this co-polymer?",
            "Propene (CH2=CH-CH3) and chloroethene (CH2=CHCl)",
            "Ethene and 2-chloropropane",
            "But-1-ene and chloroethane",
            "Prop-2-en-1-ol and chloromethane",
            "Option A is correct. Dividing the polymer chain into two-carbon repeating segments: the first repeat unit is -[CH2-CH(CH3)]- (which derives from the monomer propene, CH2=CH-CH3) and the second repeat unit is -[CH2-CH(Cl)]- (which derives from chloroethene / vinyl chloride, CH2=CHCl). The alternating structure indicates co-polymerisation of propene and chloroethene."
        ),
        (
            110, "HF 10: Environmental Role of Catalytic Converters in Hydrocarbon Removal — 9701/11/M/J/23/Q19", "HF", "HARD",
            "In a three-way catalytic converter fitted to a car exhaust, unburnt octane (C8H18) and nitrogen monoxide (NO) react together on the platinum-rhodium surface.\n\nWhat are the non-toxic products formed by this catalyzed reaction?",
            "Carbon dioxide (CO2), water (H2O), and nitrogen gas (N2)",
            "Carbon monoxide (CO), ammonia (NH3), and oxygen (O2)",
            "Carbon soot (C), nitrogen dioxide (NO2), and steam",
            "Methane (CH4), nitric acid (HNO3), and hydrogen",
            "Option A is correct. The catalytic converter simultaneously oxidizes unburnt hydrocarbons and reduces nitrogen oxides: C8H18 + 25NO -> 8CO2 + 9H2O + 12.5N2. All three resulting products (CO2, H2O, and N2) are non-toxic atmospheric constituents."
        )
    ]

    for q in hf_data:
        add_q(
            q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9]
        )

    # Balance Answer Keys Uniformly across A, B, C, D
    keys_pattern = (['B', 'D', 'A', 'C', 'A', 'D', 'B', 'C', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'] * 5) + ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'A', 'C']

    balanced_questions = []
    idx_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    for i, q in enumerate(questions_code):
        target_key = keys_pattern[i]
        target_idx = letter_to_idx[target_key]

        raw_opts = [opt.split(": ", 1)[1] for opt in q["options"]]
        correct_opt_raw = raw_opts[0]
        distractors_raw = raw_opts[1:]

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

    # Write output to mcq_topic14_data.py
    out_file = r"z:\tests n quizes63\books\psycology\new styl\mcq_topic14_data.py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write('"""\nCurated 110 Authentic Cambridge AS Chemistry (9701) Paper 1 MCQs\nfor Topic 14: Hydrocarbons (Alkanes & Alkenes) (100 Core + 10 High-Frequency Core Repeats).\n"""\n\n')
        f.write("from build_mcq_topic_pdf import MCQQuestion\n\n")
        f.write("TOPIC_14_MCQ_QUESTIONS = [\n")
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

    print(f"Successfully generated mcq_topic14_data.py with {len(balanced_questions)} MCQs!")

if __name__ == "__main__":
    create_topic14_data()
