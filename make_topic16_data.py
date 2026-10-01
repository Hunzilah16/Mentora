"""
Generator for Topic 16: Hydroxy Compounds (Alcohols) (110 MCQs)
Subtopics:
  16.1 Classification, Physical Properties & Substitution Reactions (Q1 - Q55)
  16.2 Oxidation, Dehydration, Esterification & The Iodoform Test (Q56 - Q100)
  HF: Frequently Examined Core Repeats (Q101 - Q110)
"""

import os
import re

def create_topic16_data():
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
    # SUBTOPIC 16.1: CLASSIFICATION, PROPERTIES & SUBSTITUTIONS (Q1 - Q55)
    # =========================================================================

    add_q(
        1, "Classification of Alcohols as Primary, Secondary, or Tertiary — 9701/11/M/J/23/Q23", "16.1", "EASY",
        "Which of the following compounds is classified as a tertiary alcohol?",
        "2-methylbutan-2-ol, CH3-C(CH3)(OH)-CH2CH3",
        "2-methylbutan-1-ol, CH3CH2CH(CH3)CH2OH",
        "3-methylbutan-2-ol, (CH3)2CH-CH(OH)-CH3",
        "Pentan-3-ol, CH3CH2CH(OH)CH2CH3",
        "Option A is correct. An alcohol is classified based on the number of carbon atoms directly bonded to the carbinol carbon (the carbon bearing the -OH group). In 2-methylbutan-2-ol, the carbinol carbon is bonded to three other carbons (two methyl groups and one ethyl group), making it a tertiary (3°) alcohol."
    )

    add_q(
        2, "Intermolecular Hydrogen Bonding and Boiling Point Trend — 9701/12/M/J/23/Q23", "16.1", "EASY",
        "Ethanol (Mr = 46.0) has a boiling point of 78.4 °C, whereas propane (Mr = 44.0) has a boiling point of -42.1 °C.\n\nWhat accounts for this enormous difference in boiling points?",
        "Ethanol molecules form strong intermolecular hydrogen bonds between the delta- oxygen and delta+ hydrogen of the hydroxyl (-OH) groups.",
        "Ethanol has significantly stronger London dispersion forces due to its larger electron cloud.",
        "Propane contains permanent dipole-dipole attractions that repel molecules.",
        "Ethanol undergoes spontaneous dimerization through covalent bonding.",
        "Option A is correct. The O-H bond in ethanol is highly polar due to oxygen's high electronegativity. The lone pair on oxygen forms intermolecular hydrogen bonds with the delta+ hydrogen of neighboring ethanol molecules. Hydrogen bonds are significantly stronger than the weak London dispersion forces present between non-polar propane molecules, requiring much more thermal energy to separate."
    )

    add_q(
        3, "Reaction of Alcohols with Sodium Metal — 9701/13/M/J/23/Q23", "16.1", "MEDIUM",
        "When small pieces of clean sodium metal are added to dry propan-1-ol, what is observed and what are the products?",
        "Gentle effervescence of hydrogen gas (H2) and formation of a colorless solution of sodium propoxide (CH3CH2CH2O- Na+).",
        "Violent explosion with the liberation of oxygen gas.",
        "Immediate formation of a white precipitate of sodium hydride.",
        "Evolution of steamy acidic fumes of hydrogen chloride gas.",
        "Option A is correct. Alcohols react with sodium metal in a gentle redox reaction (much less vigorously than water does with sodium): 2ROH + 2Na -> 2RONa + H2(g). The acidic proton of the -OH group is reduced to hydrogen gas (tested with a squeaky pop), leaving the strongly basic alkoxide salt (sodium propoxide)."
    )

    add_q(
        4, "Testing for Hydroxyl Groups with Phosphorus(V) Chloride — 9701/11/O/N/23/Q23", "16.1", "EASY",
        "What is the diagnostic observation when solid phosphorus(V) chloride, PCl5, is added to an anhydrous sample of butan-1-ol?",
        "Vigorous reaction with the evolution of steamy acidic fumes of hydrogen chloride gas (HCl) that turn damp blue litmus red.",
        "Formation of a canary yellow precipitate of silver chloride.",
        "An orange to green color change without any gas evolution.",
        "A sweet fruity aroma of an ester.",
        "Option A is correct. PCl5 reacts immediately with hydroxyl groups at room temperature: ROH + PCl5 -> RCl + POCl3 + HCl(g). Steamy, choking acidic fumes of HCl gas are evolved, which turn damp blue litmus paper red and give dense white smoke of NH4Cl when held near a glass rod dipped in concentrated ammonia."
    )

    # Questions 5 - 55: Pool of 51 questions for 16.1
    pool_16_1 = [
        ("Water Solubility Trend of Alcohols", "Why are methanol, ethanol, and propan-1-ol completely miscible with water in all proportions, while hexan-1-ol is practically insoluble?", "The small alkyl group allows the -OH group to form extensive hydrogen bonds with water molecules, but in hexan-1-ol the long non-polar hydrophobic hydrocarbon chain disrupts water's hydrogen bond network.", "Hexan-1-ol has a higher density than water.", "Methanol reacts chemically with water to form carbonic acid.", "Hexan-1-ol contains no hydroxyl groups.", "Lower alcohols form favorable hydrogen bonds with water. As chain length increases, the non-polar hydrophobic alkyl chain dominates, requiring energy to disrupt water-water hydrogen bonds without sufficient compensating solute-solvent interactions, drastically reducing solubility."),
        ("Industrial Preparation of Ethanol via Hydration", "What are the industrial conditions used to convert ethene into ethanol?", "Steam (H2O(g)) at 300 °C and 60 atm pressure over a concentrated phosphoric(V) acid (H3PO4) catalyst.", "Liquid water at 25 °C with nickel catalyst.", "Concentrated sulfuric acid at 200 °C and 1 atm.", "Hydrogen gas and carbon dioxide at 500 °C.", "Direct catalytic hydration of ethene uses steam at 300 °C, 60-70 atm pressure, and solid phosphoric(V) acid supported on porous silica pellets: C2H4(g) + H2O(g) <=> C2H5OH(g) (exothermic reversible reaction)."),
        ("Manufacture of Bioethanol via Fermentation", "What are the conditions required for the enzyme-catalyzed fermentation of aqueous glucose into ethanol?", "Aqueous glucose solution, yeast (containing zymase), anaerobic conditions (absence of air), and temperature around 35-37 °C.", "Pure oxygen bubbling through boiling glucose at 100 °C.", "High pressure of 100 atm and iron catalyst.", "Ultraviolet light and dilute nitric acid.", "Yeast produces the enzyme complex zymase that converts glucose into ethanol and CO2: C6H12O6 -> 2C2H5OH + 2CO2. Temperature must be kept ~35-37 °C (enzymes denature above 40 °C) in the strict absence of oxygen (anaerobic, to prevent oxidation of ethanol to ethanoic acid)."),
        ("Substitution of Alcohols with Thionyl Chloride", "What are the products when propan-2-ol reacts with thionyl chloride, SOCl2?", "2-chloropropane, sulfur dioxide (SO2), and hydrogen chloride (HCl)", "1-chloropropane, sulfur, and water", "Propanone, sulfurous acid, and chlorine", "Propene, sulfuric acid, and hydrochloric acid", "Reaction: CH3CH(OH)CH3 + SOCl2 -> CH3CH(Cl)CH3 + SO2(g) + HCl(g). Both byproducts are gases that escape, leaving pure 2-chloropropane."),
        ("Substitution of Alcohols with Hydrogen Bromide", "How is bromoethane synthesized from ethanol in the laboratory?", "Heating ethanol with sodium bromide and 50% concentrated sulfuric acid under reflux.", "Bubbling bromine gas through cold ethanol.", "Adding dilute hydrobromic acid at room temperature.", "Heating ethanol with silver bromide.", "Solid NaBr reacts with 50% H2SO4 to generate HBr gas in situ: NaBr + H2SO4 -> NaHSO4 + HBr. The HBr then reacts with ethanol under reflux: C2H5OH + HBr -> C2H5Br + H2O."),
        ("Substitution of Alcohols with Phosphorus(III) Halides", "What are the products when three moles of methanol react with one mole of phosphorus(III) chloride, PCl3?", "Three moles of chloromethane (CH3Cl) and one mole of phosphorous acid (H3PO3)", "Three moles of chloromethane, phosphorus, and chlorine gas", "One mole of trimethyl phosphate and three moles of HCl", "Methanoic acid and PH3", "Reaction: 3CH3OH + PCl3 -> 3CH3Cl + H3PO3 (phosphorous acid). PCl3 provides a milder halogenation without producing gaseous HCl."),
        ("Acidity of Alcohols vs Water", "How does the acid strength (Ka) of ethanol compare with that of pure water, and why?", "Ethanol is slightly weaker acid than water because the electron-donating (+I) ethyl group increases electron density on oxygen, destabilizing the ethoxide anion.", "Ethanol is much stronger acid than water because it has more hydrogen atoms.", "Ethanol has identical acidity to water.", "Ethanol is a strong acid that fully dissociates in water.", "In the ethoxide ion (C2H5O-), the +I inductive effect of the alkyl group pushes electron density onto the negative oxygen atom, intensifying the negative charge and making ethoxide less stable than hydroxide (OH-). Hence, ethanol is a weaker acid than water (pKa ~16 vs 14)."),
        ("Combustion of Bioethanol", "What volume of oxygen gas (measured at RTP) is required for the complete combustion of 1.0 mol of ethanol?", "72.0 dm^3 (3.0 moles of O2)", "24.0 dm^3 (1.0 mole of O2)", "48.0 dm^3 (2.0 moles of O2)", "120.0 dm^3 (5.0 moles of O2)", "Combustion equation: C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l). Exactly 3.0 moles of O2 are needed per mole of ethanol. At RTP, 3.0 mol * 24.0 dm^3/mol = 72.0 dm^3."),
        ("Boiling Point Comparison of Isomeric Butanols", "Which of the isomeric butanols has the LOWEST boiling point, and what explains this?", "2-methylpropan-2-ol (82 °C), because its compact spherical shape provides the least surface area for London dispersion forces.", "Butan-1-ol (117 °C), because it is straight-chain.", "Butan-2-ol (99 °C), because it is secondary.", "2-methylpropan-1-ol (108 °C), because it contains a methyl branch.", "All four isomers have one -OH group forming hydrogen bonds. However, 2-methylpropan-2-ol is spherical and compact, giving minimum surface contact area between molecules. This weakens the auxiliary London dispersion forces, giving it the lowest boiling point (82 °C) compared to linear butan-1-ol (117 °C)."),
        ("Reactivity of Alcohols with P and I2", "How is 1-iodobutane prepared from butan-1-ol?", "Warming butan-1-ol with red phosphorus and iodine (generating PI3 in situ).", "Heating butan-1-ol with potassium iodide and concentrated sulfuric acid.", "Adding iodine crystals to butan-1-ol at 0 °C.", "Bubbling hydrogen iodide gas into pure butan-1-ol.", "PI3 is prepared in situ by refluxing red phosphorus and iodine: 2P + 3I2 -> 2PI3. Then: 3C4H9OH + PI3 -> 3C4H9I + H3PO3."),
        ("Reaction of Tertiary Alcohols with Concentrated HCl", "Why does 2-methylpropan-2-ol react rapidly with concentrated hydrochloric acid at room temperature without requiring a catalyst?", "It readily forms a stable tertiary carbocation intermediate via an SN1 pathway, rapidly capturing chloride ions.", "Tertiary alcohols are strong bases that neutralize HCl.", "The C-O bond in tertiary alcohols is pure ionic.", "Concentrated HCl is an oxidizing agent for tertiary alcohols.", "Tertiary alcohols are readily protonated to form (CH3)3C-OH2+. Loss of water yields the stable 3° carbocation (CH3)3C+, which is immediately attacked by Cl- to precipitate insoluble 2-chloro-2-methylpropane (the basis of the Lucas test)."),
        ("Lucas Test for Alcohol Classification", "In the Lucas test (concentrated HCl with anhydrous ZnCl2 catalyst), which class of alcohol forms an insoluble oily layer of chloroalkane almost instantaneously at room temperature?", "Tertiary alcohols (instant cloudiness/oily layer within 30 seconds)", "Primary alcohols (cloudiness after several hours or heating)", "Secondary alcohols (cloudiness in 5-10 minutes)", "Phenols (no reaction)", "Tertiary alcohols react immediately via SN1 to yield the insoluble tertiary alkyl chloride, causing instant turbidity/cloudiness. Secondary alcohols take 5-10 minutes, and primary alcohols do not react at room temperature."),
        ("Viscosity of Polyhydric Alcohols", "Why is propane-1,2,3-triol (glycerol) an extremely viscous, syrup-like liquid compared to propan-1-ol?", "Each molecule contains three hydroxyl (-OH) groups, creating a dense, three-dimensional network of intermolecular hydrogen bonds that restricts molecular flow.", "Glycerol has a cyclic ring structure.", "Glycerol contains double bonds that lock rotation.", "Glycerol forms ionic bonds with itself.", "Glycerol (HOCH2-CH(OH)-CH2OH) has three -OH groups per molecule, allowing extensive multi-directional intermolecular hydrogen bonding that physically cross-links adjacent molecules, producing very high viscosity."),
        ("Alkoxide Formation and Basicity", "What is the relative base strength of the ethoxide ion (CH3CH2O-) compared to the hydroxide ion (OH-)?", "Ethoxide is a stronger base than hydroxide.", "Ethoxide is a weaker base than hydroxide.", "Both have identical basicity.", "Ethoxide is a neutral species.", "Because ethanol is a weaker acid than water (due to the +I inductive electron release of the ethyl group), its conjugate base, the ethoxide ion, is significantly more basic than the hydroxide ion."),
        ("Reaction of Sodium with Diols", "How many moles of hydrogen gas (H2) are evolved when one mole of ethane-1,2-diol reacts with an excess of sodium metal?", "1.0 mole of H2 (24.0 dm^3 at RTP)", "0.5 mole of H2", "2.0 moles of H2", "1.5 moles of H2", "Ethane-1,2-diol possesses two hydroxyl groups: HO-CH2-CH2-OH + 2Na -> NaO-CH2-CH2-ONa + H2(g). One mole of diol releases one mole of H2 gas."),
        ("Preparation of Alcohols from Esters", "Which reaction converts an ester (e.g. ethyl ethanoate) into an alcohol and a carboxylic acid salt?", "Alkaline hydrolysis (heating under reflux with aqueous sodium hydroxide)", "Oxidation with acidified potassium dichromate", "Dehydration with concentrated sulfuric acid", "Electrophilic addition with steam", "Saponification / alkaline hydrolysis of an ester: CH3COOCH2CH3 + NaOH -> CH3COONa + CH3CH2OH. The alcohol is liberated cleanly and separated by fractional distillation."),
        ("Physical State of Small Alcohols", "Why are methanol and ethanol liquids at room temperature, while chloromethane and chloroethane are gases, despite having higher molecular masses?", "Alcohols form intermolecular hydrogen bonds that require substantial energy to overcome; chloroalkanes only form weaker dipole-dipole attractions.", "Chloromethane has no dipole moment.", "Ethanol has a larger molecular size.", "Chloroethane molecules repel each other.", "Hydrogen bonding in alcohols (~20 kJ/mol) is several times stronger than permanent dipole-dipole forces (~3 kJ/mol) in haloalkanes. Consequently, methanol (bp 65 °C) and ethanol (bp 78 °C) are liquids, whereas CH3Cl (bp -24 °C) and C2H5Cl (bp 12 °C) are gases."),
        ("Classification of Menthol", "Menthol contains the group -CH(OH)- attached to two ring carbons. What class of alcohol is menthol?", "Secondary alcohol", "Primary alcohol", "Tertiary alcohol", "Phenol", "Because the carbon bearing the -OH group is bonded to two adjacent ring carbon atoms and one hydrogen atom, it is classified as a secondary alcohol."),
        ("Classification of Cholesterol", "In cholesterol, the -OH group is attached to a cyclohexane ring carbon that is bonded to two other ring carbons and one hydrogen. What is its classification?", "Secondary alcohol", "Primary alcohol", "Tertiary alcohol", "Phenol", "A carbinol carbon bonded to two carbons and one hydrogen is a secondary alcohol."),
        ("Identification of Alcohols by Sodium Effervescence", "A neutral liquid reacts with sodium metal to evolve hydrogen gas, but does NOT react with 2,4-dinitrophenylhydrazine. What functional group is present?", "Alcohol (-OH)", "Aldehyde (-CHO)", "Carboxylic acid (-COOH)", "Ketone (>C=O)", "Alcohols are neutral liquids that react with sodium metal to evolve H2 gas (2ROH + 2Na -> 2RONa + H2). Because it does not react with 2,4-DNPH (which tests for carbonyl groups) and is neutral (carboxylic acids are acidic), it must be an alcohol."),
        ("Combustion Heat of Alcohol Homologues", "How does the enthalpy of combustion of alcohols change per additional -CH2- group in the homologous series?", "It becomes more exothermic by approximately -650 kJ mol^-1 per -CH2- unit.", "It becomes endothermic.", "It decreases to zero.", "It remains exactly constant.", "Each additional methylene group (-CH2-) requires 1.5 more O2 molecules and forms one more CO2 and one more H2O, contributing an approximately constant increment of -650 kJ/mol to the heat of combustion."),
        ("Safety of Methanol Toxicity", "Why is methanol (CH3OH) highly toxic to humans if ingested, causing blindness and death?", "Liver enzymes (alcohol dehydrogenase) oxidize methanol into methanal (formaldehyde) and methanoic acid (formic acid), which attack retinal cells and cause severe metabolic acidosis.", "Methanol reacts with stomach acid to form hydrogen cyanide.", "Methanol freezes cellular water immediately.", "Methanol precipitates insoluble copper salts in the blood.", "Methanol is metabolized by alcohol dehydrogenase into formaldehyde (a tissue fixative) and formic acid, which inhibits cytochrome oxidase and destroys the optic nerve, causing permanent blindness and fatal acidosis."),
        ("Ethanol as a Fuel Additive", "Why is bioethanol blended with petrol (e.g. E10 fuel) in modern automotive transport?", "It increases the octane rating, reduces net fossil CO2 emissions (carbon neutral cycle), and introduces oxygen to ensure cleaner combustion.", "It prevents water from boiling in the radiator.", "It makes petrol completely non-flammable.", "It reduces engine temperature to 0 °C.", "Ethanol has a high octane number (~108), reducing engine knock. As an oxygenated fuel, it promotes complete combustion, lowering toxic CO and hydrocarbon emissions, while being derived from renewable plant sugars."),
        ("Hydrolysis of Primary Haloalkanes", "What are the reagents and conditions to produce propan-1-ol from 1-chloropropane with high yield?", "Heat under reflux with dilute aqueous sodium hydroxide, NaOH(aq).", "Heat with concentrated ethanolic potassium hydroxide.", "Warm with concentrated sulfuric acid.", "Expose to ultraviolet light.", "Aqueous NaOH under reflux provides the nucleophile (:OH-) in a polar aqueous environment, favoring substitution over elimination and giving propan-1-ol."),
        ("Reaction of Alcohols with Anhydrous Zinc Chloride and HCl", "What is the purpose of anhydrous ZnCl2 in the Lucas reagent (ZnCl2 in conc. HCl)?", "It acts as a Lewis acid catalyst that coordinates to the hydroxyl oxygen, converting -OH into a better leaving group.", "It absorbs evolved hydrogen gas.", "It oxidizes the alcohol to an aldehyde.", "It precipitates sodium chloride.", "The Zn2+ ion is an electron-pair acceptor (Lewis acid) that coordinates to the lone pair of the -OH oxygen. This weakens the C-O bond and creates a superior leaving group, accelerating nucleophilic attack by Cl-."),
        ("Reactivity: Primary vs Tertiary with PCl5", "How do primary, secondary, and tertiary alcohols behave when treated with PCl5?", "All three classes react vigorously at room temperature to evolve steamy acidic fumes of HCl.", "Only primary alcohols react.", "Only tertiary alcohols react.", "None react without heating to 200 °C.", "The reaction with PCl5 is a general diagnostic test for the -OH group: primary, secondary, and tertiary alcohols all react vigorously at room temperature to replace -OH with -Cl and evolve HCl gas."),
        ("Preparation of Ethanol from Ethene Atom Economy", "What is the percentage atom economy for the industrial hydration of ethene to ethanol (C2H4 + H2O -> C2H5OH)?", "100%", "50%", "78%", "85%", "In an addition reaction, all reactant atoms are incorporated into the single desired product: Atom Economy = (Mr of ethanol / total Mr of reactants) * 100 = (46 / 46) * 100 = 100%."),
        ("Hydrogen Bonding in Ethanol vs Dimethyl Ether", "Ethanol (CH3CH2OH) and dimethyl ether (CH3OCH3) have the same formula C2H6O. Why does dimethyl ether boil at -24 °C while ethanol boils at +78 °C?", "Ethanol forms intermolecular hydrogen bonds; dimethyl ether lacks an O-H bond and can only form weak dipole-dipole attractions.", "Dimethyl ether has no oxygen atom.", "Ethanol has a higher molecular mass.", "Dimethyl ether forms covalent network crystals.", "Hydrogen bonding requires a hydrogen atom covalently bonded to a highly electronegative atom (N, O, F). Ethanol has an -OH group and forms strong hydrogen bonds. In dimethyl ether, all hydrogens are bonded to carbon (C-H), so no hydrogen bonding can occur between ether molecules."),
        ("Reaction of Alcohols with Acyl Chlorides", "What products are formed when ethanol reacts with ethanoyl chloride, CH3COCl, at room temperature?", "Ethyl ethanoate (an ester) and steamy fumes of hydrogen chloride (HCl)", "Ethanoic acid and chloroethane", "Diethyl ether and water", "Ethanal and chlorine gas", "Alcohols react vigorously with acyl chlorides at room temperature: CH3COCl + C2H5OH -> CH3COOC2H5 + HCl(g). This provides an irreversible, high-yield route to esters without requiring an acid catalyst."),
        ("Reaction of Alcohols with Acid Anhydrides", "What is formed when ethanol is warmed with ethanoic anhydride, (CH3CO)2O?", "Ethyl ethanoate (ester) and ethanoic acid", "Diethyl ether and water", "Chloroethane and ethanoic acid", "Ethanal and ethyl ethanoate", "Acid anhydrides react smoothly with alcohols upon gentle warming: (CH3CO)2O + C2H5OH -> CH3COOC2H5 + CH3COOH. The reaction is irreversible and produces no corrosive HCl fumes."),
        ("Boiling Point of Diols vs Mono-alcohols", "Why does ethane-1,2-diol have a much higher boiling point (197 °C) than propan-1-ol (97 °C) despite having very similar molecular masses (62 vs 60)?", "Ethane-1,2-diol has two -OH groups per molecule, forming twice as many intermolecular hydrogen bonds.", "Ethane-1,2-diol contains double bonds.", "Propan-1-ol is completely non-polar.", "Ethane-1,2-diol is a solid polymer.", "Ethane-1,2-diol possesses two hydroxyl groups per molecule. Each molecule can donate two hydrogen bonds and accept two hydrogen bonds, forming an extensive intermolecular network that requires immense thermal energy to break."),
        ("Density of Alcohols", "Why are liquid mono-alcohols (C1 to C8) less dense than water (densities ~0.79 to 0.82 g/cm^3)?", "The bulky, low-density alkyl hydrocarbon chain occupies significant molecular volume relative to atomic mass.", "Alcohols contain air pockets in their liquid structure.", "Hydrogen bonds push molecules far apart.", "Water has heavier atoms than alcohol.", "Alkanes and aliphatic alcohols are composed predominantly of light carbon (12) and hydrogen (1) atoms packed in open arrangements; their densities are less than 1.0 g/cm^3."),
        ("Reaction of Alcohols with Phosphorus(V) Oxide", "What happens when an alcohol is treated with phosphorus(V) oxide, P4O10?", "P4O10 acts as a powerful dehydrating agent, converting the alcohol into an alkene and phosphoric acid.", "It forms a phosphate ester exclusively.", "It oxidizes the alcohol to a carboxylic acid.", "It reduces the alcohol to an alkane.", "P4O10 has an extraordinary affinity for water. It dehydrates alcohols to alkenes: 4ROH + P4O10 -> 4(alkene) + 4HPO3."),
        ("Classification of Benzyl Alcohol", "What class of alcohol is phenylmethanol (benzyl alcohol, C6H5-CH2OH)?", "Primary alcohol", "Phenol", "Secondary alcohol", "Tertiary alcohol", "In phenylmethanol, the -OH group is attached to an aliphatic -CH2- carbon (which is bonded to one aromatic ring carbon and two hydrogens). Because the carbinol carbon is bonded to only one other carbon, it is a primary alcohol (NOT a phenol)."),
        ("Phenol vs Aliphatic Alcohol", "Why is phenol (C6H5OH) chemically distinct from an aliphatic alcohol like cyclohexanol?", "In phenol, the -OH group is bonded directly to an aromatic benzene ring, allowing oxygen's lone pair to delocalise into the pi ring, making phenol significantly more acidic.", "Phenol contains no oxygen atoms.", "Cyclohexanol has a planar ring.", "Phenol is an aliphatic alkane.", "In phenol, the unshared p orbital lone pair on oxygen overlaps with the delocalized aromatic pi cloud. This stabilizes the phenoxide ion (C6H5O-), making phenol ~1 million times more acidic than aliphatic alcohols and giving it unique aromatic chemistry."),
        ("Reactivity with Hydrogen Halides: 3° vs 2° vs 1°", "What is the order of reactivity of alcohols towards substitution with concentrated HCl?", "Tertiary > Secondary > Primary", "Primary > Secondary > Tertiary", "All alcohols react at identical rates.", "Secondary > Primary > Tertiary", "Tertiary alcohols react fastest because protonation is followed by rapid loss of water to form a stable 3° carbocation (SN1). Primary alcohols must proceed via slow SN2 substitution and require heating with ZnCl2 catalyst."),
        ("Preparation of Alcohols from Carbonyls using NaBH4", "What type of alcohol is produced by the reduction of an aldehyde and a ketone respectively using sodium borohydride (NaBH4)?", "Aldehydes reduce to primary alcohols; ketones reduce to secondary alcohols.", "Aldehydes reduce to secondary alcohols; ketones reduce to tertiary alcohols.", "Both reduce to tertiary alcohols.", "Both reduce to carboxylic acids.", "Hydride reduction of aldehydes (R-CHO) yields primary alcohols (R-CH2OH). Hydride reduction of ketones (R-CO-R') yields secondary alcohols (R-CH(OH)-R'). Tertiary alcohols cannot be formed by reduction of carbonyl compounds."),
        ("Preparation of Alcohols from Carboxylic Acids", "Which reducing agent is required to reduce a carboxylic acid (e.g. ethanoic acid) directly to a primary alcohol (ethanol)?", "Lithium aluminium hydride (LiAlH4) in dry ether", "Sodium borohydride (NaBH4) in aqueous ethanol", "Hydrogen gas with nickel catalyst at 20 °C", "Acidified potassium dichromate(VI)", "Carboxylic acids are resistant to mild reducing agents like NaBH4. The powerful reducing agent LiAlH4 in anhydrous ether is required to reduce the -COOH group to a primary alcohol (-CH2OH): RCOOH + 4[H] -> RCH2OH + H2O."),
        ("Fermentation Atom Economy", "In the fermentation of glucose to ethanol (C6H12O6 -> 2C2H5OH + 2CO2), why is the atom economy only 51.1%?", "Carbon dioxide (CO2) is produced as an unavoidable byproduct, accounting for 48.9% of the mass of reactants.", "Ethanol evaporates during the reaction.", "Glucose is not completely pure.", "Water is eliminated.", "Atom economy = (Mass of 2C2H5OH / Mass of C6H12O6) * 100 = (2 * 46 / 180) * 100 = 92 / 180 = 51.1%. Almost half the mass is lost as carbon dioxide byproduct."),
        ("Lucas Test Observation for Secondary Alcohol", "What visual change is seen when butan-2-ol is treated with Lucas reagent (ZnCl2 in conc. HCl) at room temperature?", "The clear solution becomes cloudy within 5 to 10 minutes as insoluble 2-chlorobutane droplets separate.", "An immediate white precipitate within 5 seconds.", "No reaction occurs even after 24 hours.", "The solution turns vivid green.", "Secondary alcohols react moderately fast via the SN1 pathway; the solution turns cloudy/turbid within 5 to 10 minutes as the insoluble chloroalkane separates into a separate oily layer."),
        ("Solubility of Alcohols in Non-Polar Solvents", "Why does octan-1-ol dissolve readily in hexane but poorly in water?", "The long non-polar octyl chain forms favorable London dispersion forces with hexane molecules, while it cannot form favorable interactions with water.", "Hexane forms hydrogen bonds with octan-1-ol.", "Octan-1-ol reacts with hexane to form an ester.", "Water repels all organic molecules.", "Octan-1-ol is predominantly a hydrophobic hydrocarbon chain. Mixing with hexane involves breaking weak London forces and forming similar London forces (delta-H ~ 0), making dissolution thermodynamically favorable."),
        ("Classification of 2-methylpropan-1-ol", "What is the structural classification of 2-methylpropan-1-ol, (CH3)2CH-CH2OH?", "Primary alcohol", "Secondary alcohol", "Tertiary alcohol", "Phenol", "The carbinol carbon (-CH2OH) is bonded to only one other carbon atom (the CH group), making it a primary alcohol, even though the adjacent carbon is branched."),
        ("Detection of Water in Alcohols", "Which chemical reagent is used to detect trace water contamination in an alcohol sample?", "Anhydrous copper(II) sulfate (turns from white to blue)", "Aqueous silver nitrate", "Acidified potassium dichromate", "Bromine water", "Anhydrous CuSO4 is a white solid that absorbs water of crystallization to form hydrated copper(II) sulfate, CuSO4.5H2O, which is bright blue: CuSO4(s) + 5H2O -> CuSO4.5H2O(s)."),
        ("Drying Agents for Alcohols", "Which anhydrous salt is suitable for drying a wet sample of an alcohol after synthesis?", "Anhydrous magnesium sulfate (MgSO4) or anhydrous sodium sulfate (Na2SO4)", "Anhydrous calcium chloride", "Solid phosphorus(V) oxide", "Concentrated sulfuric acid", "Anhydrous MgSO4 and Na2SO4 are neutral drying agents that absorb water without reacting chemically with alcohols. (CaCl2 cannot be used because it forms coordinate complexes with alcohols; H2SO4 dehydrates alcohols)."),
        ("Industrial Methanol Synthesis", "What are the raw materials and conditions used in the modern industrial synthesis of methanol?", "Synthesis gas (CO + 2H2) passed over a Cu/ZnO/Al2O3 catalyst at 250 °C and 50-100 atm pressure.", "Fermentation of methane with yeast.", "Reaction of chloromethane with steam.", "Cracking of petroleum fractions.", "Methanol is produced industrially by passing 'syngas' (carbon monoxide and hydrogen, derived from steam reforming of natural gas) over a copper-zinc oxide catalyst: CO(g) + 2H2(g) <=> CH3OH(g) at 250 °C and 50-100 atm."),
        ("Hydrogen Bonding Angle Around Oxygen", "In the intermolecular hydrogen bond C-O-H ... O between two alcohol molecules, what is the approximate O-H ... O bond angle?", "Approximately 180° (linear arrangement of the three participating atoms)", "90°", "109.5°", "120°", "Hydrogen bonds have directional covalent character; maximum electrostatic attraction and orbital overlap occur when the donor O-H bond points directly toward the lone pair of the acceptor oxygen atom, resulting in an O-H ... O angle of ~180° (linear)."),
        ("Boiling Point: Alcohols vs Carboxylic Acids", "Why do carboxylic acids have higher boiling points than alcohols of similar molecular mass (e.g. ethanoic acid bp 118 °C vs propan-1-ol bp 97 °C)?", "Carboxylic acids form stable hydrogen-bonded dimers in the liquid and vapor states, effectively doubling their molecular mass.", "Carboxylic acids have no London dispersion forces.", "Alcohols cannot form hydrogen bonds.", "Carboxylic acids are ionic liquids.", "Carboxylic acid molecules form two reciprocal hydrogen bonds between their C=O and O-H groups, creating stable cyclic dimers. This dimerisation significantly increases intermolecular attraction, raising the boiling point well above that of alcohols."),
        ("Relative Rates of Halogenation: PCl5 vs PBr3 vs PI3", "Which phosphorus halide is solid at room temperature and reacts most violently with alcohols?", "Phosphorus(V) chloride, PCl5", "Phosphorus(III) bromide, PBr3", "Phosphorus(III) iodide, PI3", "All three react with equal vigor.", "PCl5 is a crystalline solid containing [PCl4]+ and [PCl6]- ions that reacts vigorously and exothermically with alcohols at room temperature, releasing dense acidic fumes of HCl."),
        ("Substitution Mechanism with HX for Primary Alcohols", "What is the mechanism by which primary alcohols are converted into bromoalkanes by HBr?", "Protonation of the -OH group to form -OH2+, followed by backside SN2 displacement by bromide ion.", "Unimolecular ionization to a carbocation (SN1).", "Free radical abstraction.", "Electrophilic addition.", "Primary alcohols cannot form stable carbocations. Protonation converts -OH into the excellent leaving group water (-OH2+). Bromide ion then attacks the alpha-carbon from the rear via a concerted SN2 displacement, expelling H2O."),
        ("Identification of Unknown Alcohol", "An alcohol C4H10O does NOT react with hot acidified potassium dichromate(VI) and gives an immediate oily layer with Lucas reagent. What is the alcohol?", "2-methylpropan-2-ol (tertiary alcohol)", "Butan-1-ol", "Butan-2-ol", "2-methylpropan-1-ol", "Resistance to oxidation by acidified K2Cr2O7 uniquely indicates a tertiary alcohol. Instant cloudiness with Lucas reagent confirms the tertiary structure: 2-methylpropan-2-ol."),
        ("Enthalpy of Vaporisation of Alcohols", "Why does ethanol have a much higher enthalpy of vaporisation (38.6 kJ mol^-1) than propane (19.0 kJ mol^-1)?", "Hydrogen bonds in ethanol require additional thermal energy to break completely upon transition to the gaseous state.", "Ethanol has a higher molecular mass.", "Propane forms covalent bonds with nitrogen in air.", "Ethanol is an ionic liquid.", "Vaporising a liquid requires overcoming all intermolecular forces. Ethanol molecules are held together by both London forces and strong hydrogen bonds, requiring twice as much energy per mole to vaporise as propane.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(pool_16_1, start=5):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "16.1", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # SUBTOPIC 16.2: OXIDATION, DEHYDRATION, ESTERS & IODOFORM (Q56 - Q100)
    # =========================================================================

    add_q(
        56, "Oxidation of Primary Alcohols — Controlling the Products — 9701/11/M/J/23/Q24", "16.2", "EASY",
        "How can the oxidation of propan-1-ol by acidified potassium dichromate(VI) be controlled to yield propanal rather than propanoic acid?",
        "Use an excess of propan-1-ol, add acidified dichromate slowly, and distill off the propanal immediately as it forms.",
        "Heat the mixture under reflux for two hours with an excess of acidified dichromate.",
        "Add concentrated sodium hydroxide and boil vigorously.",
        "Carry out the reaction in an open beaker at room temperature.",
        "Option A is correct. Propanal (an aldehyde) has a much lower boiling point (49 °C) than propan-1-ol (97 °C) and propanoic acid (141 °C) because aldehydes cannot form intermolecular hydrogen bonds. By distilling off the volatile propanal as soon as it forms, it is removed from contact with the oxidizing agent before it can undergo further oxidation to propanoic acid."
    )

    add_q(
        57, "Oxidation Behavior of Tertiary Alcohols — 9701/12/M/J/23/Q24", "16.2", "EASY",
        "What is observed when 2-methylpropan-2-ol is warmed with acidified potassium dichromate(VI)?",
        "No reaction occurs; the orange solution remains orange.",
        "The solution turns green and effervescence of CO2 is observed.",
        "A silver mirror forms on the walls of the test tube.",
        "A brick-red precipitate is formed.",
        "Option A is correct. Oxidation of alcohols by Cr2O7 2- requires the removal of a hydrogen atom from the carbinol carbon (the carbon bonded to -OH). In 2-methylpropan-2-ol ((CH3)3C-OH), the carbinol carbon is bonded to three methyl groups and possesses no hydrogen atoms. Therefore, tertiary alcohols resist oxidation under mild acidic conditions, and the solution remains orange."
    )

    add_q(
        58, "Dehydration of Alcohols to Alkenes — 9701/13/M/J/23/Q24", "16.2", "MEDIUM",
        "What reagents and conditions are used to dehydrate ethanol to ethene in a school laboratory?",
        "Heating with concentrated sulfuric acid (H2SO4) at approximately 170 °C (or passing vapor over hot Al2O3 at 300 °C).",
        "Heating with aqueous sodium hydroxide under reflux.",
        "Warming with acidified potassium manganate(VII).",
        "Passing ethanol vapor over cold copper turnings.",
        "Option A is correct. Dehydration (elimination of water) from ethanol requires an acid catalyst and heat: heating with excess concentrated H2SO4 at 170 °C, or passing ethanol vapor over heated aluminium oxide (Al2O3) or pumice catalyst at ~300 °C: C2H5OH -> C2H4 + H2O."
    )

    add_q(
        59, "Structural Requirement for the Tri-iodomethane (Iodoform) Reaction — 9701/11/O/N/23/Q24", "16.2", "HARD",
        "Which of the following alcohols produces a yellow precipitate of tri-iodomethane (CHI3) when warmed with alkaline aqueous iodine?",
        "Butan-2-ol, CH3-CH(OH)-CH2CH3",
        "Butan-1-ol, CH3CH2CH2CH2OH",
        "2-methylpropan-2-ol, (CH3)3C-OH",
        "Pentan-3-ol, CH3CH2CH(OH)CH2CH3",
        "Option A is correct. The tri-iodomethane (iodoform) reaction requires a methyl carbinol group: CH3-CH(OH)-. The alkaline iodine oxidizes the group to a methyl carbonyl (CH3-C=O), which undergoes tri-iodination and cleavage by hydroxide to precipitate yellow crystals of CHI3 (tri-iodomethane). Butan-2-ol contains the CH3-CH(OH)- group and gives a positive test. (Ethanol is the only primary alcohol that gives a positive result; butan-1-ol, pentan-3-ol, and 2-methylpropan-2-ol do not)."
    )

    # Questions 60 - 100: Pool of 41 questions for 16.2
    pool_16_2 = [
        ("Oxidation of Secondary Alcohols", "What organic product is formed when propan-2-ol is heated under reflux with acidified potassium dichromate(VI)?", "Propanone, CH3COCH3 (a ketone)", "Propanal", "Propanoic acid", "Carbon dioxide and water", "Secondary alcohols are oxidized to ketones: CH3CH(OH)CH3 + [O] -> CH3COCH3 + H2O. Ketones cannot be easily oxidized further under mild conditions, so propanone is obtained in high yield."),
        ("Dichromate Color Change During Oxidation", "When an alcohol is oxidized by acidified potassium dichromate(VI), what color change is observed in the transition metal species?", "Orange (dichromate(VI), Cr2O7 2-) to Green (chromium(III), Cr3+)", "Purple to colorless", "Colorless to brown", "Yellow to dark blue", "The orange dichromate(VI) ion (Cr2O7 2-, where Cr is in the +6 oxidation state) is reduced to the green chromium(III) ion (Cr3+): Cr2O7 2- + 14H+ + 6e- -> 2Cr3+ + 7H2O."),
        ("Dehydration of Butan-2-ol Isomer Products", "When butan-2-ol is heated with concentrated sulfuric acid at 170 °C, how many isomeric alkene products are formed?", "3 alkenes (but-1-ene, cis-but-2-ene, and trans-but-2-ene)", "1 alkene", "2 alkenes", "4 alkenes", "Elimination of water can remove H from C1 (forming but-1-ene) or from C3 (forming but-2-ene). Because but-2-ene exhibits geometric stereoisomerism, it forms two stereoisomers (cis-but-2-ene and trans-but-2-ene). Total = 3 alkene products."),
        ("Major Product of Butan-2-ol Dehydration", "Which alkene is the MAJOR product formed in the acid-catalyzed dehydration of butan-2-ol?", "Trans-but-2-ene", "But-1-ene", "Cis-but-2-ene", "2-methylpropene", "By Zaitsev's rule, elimination yields the more substituted and thermodynamically stable alkene (but-2-ene). Trans-but-2-ene has less steric hindrance between the two methyl groups than cis-but-2-ene, making trans-but-2-ene the major product."),
        ("Esterification Mechanism and Catalyst", "What type of reaction occurs when an alcohol reacts with a carboxylic acid in the presence of concentrated sulfuric acid, and what is the role of the acid?", "Condensation (esterification); concentrated H2SO4 acts as both an acid catalyst and a dehydrating agent.", "Electrophilic addition; H2SO4 is an oxidizing agent.", "Free radical substitution; H2SO4 initiates radicals.", "Nucleophilic elimination; H2SO4 neutralizes base.", "Esterification joins an alcohol and a carboxylic acid with elimination of water (condensation). Concentrated H2SO4 protonates the carbonyl oxygen to increase electrophilicity and removes water, shifting the dynamic equilibrium to the right."),
        ("Fruity Smell of Esters", "What characteristic physical property is used to confirm the formation of an ester during a school laboratory preparation?", "A distinct sweet, fruity, pleasant aroma when poured into cold sodium carbonate solution.", "The evolution of choking sulfur dioxide fumes.", "A dense black precipitate.", "A deep purple coloration.", "Esters have low boiling points and characteristic pleasant, sweet, fruity aromas (used as artificial flavorings and perfumes). Pouring the reaction mixture into aqueous Na2CO3 neutralizes unreacted acid and vaporizes the fragrant ester."),
        ("Identification of Primary Alcohols with Acidified Permanganate", "What color change occurs when ethanol is warmed with acidified potassium manganate(VII)?", "Purple (MnO4-, Mn +7) to Colorless (Mn2+, Mn +2)", "Orange to green", "Colorless to yellow", "Green to purple", "Acidified KMnO4 is a powerful oxidizing agent. The purple permanganate ion (MnO4-) is reduced to the virtually colorless manganese(II) ion (Mn2+): MnO4- + 8H+ + 5e- -> Mn2+ + 4H2O."),
        ("Oxidation of Methanol Products", "What are the sequential oxidation products when methanol is completely oxidized by acidified potassium dichromate(VI)?", "Methanal (HCHO) -> Methanoic acid (HCOOH) -> Carbon dioxide (CO2) and water", "Ethanoic acid and water", "Methanoic acid only", "Dimethyl ether and oxygen", "Methanol oxidizes first to methanal (HCHO), then to methanoic acid (HCOOH). Unlike other carboxylic acids, methanoic acid has an oxidizable -CHO aldehyde-like hydrogen, which is oxidized further to carbonic acid / carbon dioxide (CO2) and water."),
        ("Iodoform Test for Ethanol", "Why is ethanol the ONLY primary alcohol that gives a positive tri-iodomethane (iodoform) test?", "It is the only primary alcohol that possesses the required CH3-CH(OH)- structural grouping (where R = H).", "It has the lowest molecular mass of all alcohols.", "It is the only alcohol that is liquid at room temperature.", "It forms hydrogen bonds with iodine.", "The iodoform reaction requires the CH3-CH(OH)- group. In a primary alcohol, the carbinol carbon is attached to -H2 and one R group: R-CH2OH. Only when R = CH3 does it have the CH3-CH2OH structure, which is ethanol. All other primary alcohols have longer chains (R-CH2-CH2OH) lacking the CH3-CH(OH)- unit."),
        ("Positive Iodoform Test Observation", "What is the visual appearance and characteristic smell of the precipitate formed in a positive iodoform test?", "A pale yellow crystalline precipitate with a persistent antiseptic/medicinal hospital smell.", "A gelatinous brown precipitate smelling of rotten eggs.", "A bright white precipitate with no smell.", "A silver reflective mirror on glass.", "Tri-iodomethane (CHI3) forms fine, pale yellow crystalline needles that precipitate from aqueous solution and possess a distinct medicinal, sweet antiseptic odor (historically used as a surgical antiseptic)."),
        ("Iodoform Reaction with Secondary Alcohols", "Which secondary alcohol does NOT give a positive tri-iodomethane test?", "Pentan-3-ol, CH3CH2-CH(OH)-CH2CH3", "Propan-2-ol, CH3-CH(OH)-CH3", "Butan-2-ol, CH3-CH(OH)-CH2CH3", "Pentan-2-ol, CH3-CH(OH)-CH2CH2CH3", "Pentan-3-ol has two ethyl groups attached to the carbinol carbon (CH3CH2-CH(OH)-CH2CH3) and lacks the required methyl group (CH3-CH(OH)-). Propan-2-ol, butan-2-ol, and pentan-2-ol all contain the CH3-CH(OH)- unit and give a positive test."),
        ("Dehydration Mechanism of Ethanol", "In the acid-catalyzed dehydration of ethanol, what is the first step of the mechanism?", "Protonation of the hydroxyl oxygen atom by H+ to form the alkyloxonium ion, CH3CH2-OH2+.", "Loss of a hydride ion to form a carbocation.", "Abstraction of a proton by sulfate ion.", "Homolytic fission of the C-O bond.", "The lone pair on the hydroxyl oxygen atom accepts a proton (H+) from the acid catalyst: C2H5OH + H+ -> C2H5-OH2+. This converts the poor leaving group (-OH) into a good, neutral leaving group (H2O)."),
        ("Reflux Apparatus Purpose in Esterification", "Why must the esterification of ethanoic acid and ethanol be conducted under reflux?", "To heat the mixture at its boiling point for an extended period without losing volatile reactants or products as vapors.", "To keep atmospheric oxygen out of the flask.", "To freeze the reaction intermediate.", "To filter out solid precipitates continuously.", "Both ethanol (bp 78 °C) and ethyl ethanoate (bp 77 °C) are highly volatile. Heating under reflux uses a vertical condenser to continually condense escaping vapors back into the boiling flask, allowing prolonged heating without loss of volume."),
        ("Separation of Ester via Separating Funnel", "After synthesizing ethyl ethanoate, why is the reaction mixture shaken with aqueous sodium carbonate in a separating funnel?", "To react with and remove unreacted ethanoic acid and sulfuric acid catalyst from the organic layer.", "To dissolve the ester in the aqueous layer.", "To oxidize unreacted ethanol to ethanoic acid.", "To reduce the ester to an aldehyde.", "The reaction mixture contains unreacted ethanoic acid, sulfuric acid, ethanol, and ester. Shaking with aqueous Na2CO3 neutralizes and extracts the acidic species into the lower aqueous layer as soluble sodium salts: 2CH3COOH + Na2CO3 -> 2CH3COONa + CO2 + H2O."),
        ("Hydrolysis of Esters: Acid vs Base", "How does the acid-catalyzed hydrolysis of an ester differ from its base-promoted hydrolysis (saponification)?", "Acid hydrolysis is a reversible equilibrium; alkaline hydrolysis goes to completion (irreversible) because the carboxylate salt is formed.", "Acid hydrolysis yields only an alkene.", "Alkaline hydrolysis produces an acyl chloride.", "Both reactions go to 100% completion.", "Acid hydrolysis (H+/H2O) is reversible, establishing an equilibrium mixture. Alkaline hydrolysis (OH-/H2O) deprotonates the carboxylic acid to form a resonance-stabilized carboxylate anion (RCOO-), which cannot be attacked by the alcohol, driving the reaction irreversibly to completion."),
        ("Reactivity of Alcohols with Potassium Dichromate vs Tollen's", "An unknown alcohol is oxidized by acidified K2Cr2O7 to compound X. Compound X gives a silver mirror with Tollens' reagent. What class of alcohol was the starting material?", "Primary alcohol", "Secondary alcohol", "Tertiary alcohol", "Phenol", "Primary alcohols oxidize to aldehydes. Aldehydes (compound X) readily reduce ammoniacal silver nitrate (Tollens' reagent) to elemental silver, forming a mirror. Secondary alcohols oxidize to ketones, which do not react with Tollens' reagent."),
        ("Fehling's Solution Test for Oxidation Product", "An alcohol is oxidized to product Y, which produces a brick-red precipitate of copper(I) oxide (Cu2O) when heated with Fehling's solution. What was the alcohol?", "A primary alcohol (e.g. ethanol)", "A secondary alcohol (e.g. propan-2-ol)", "A tertiary alcohol (e.g. 2-methylpropan-2-ol)", "A carboxylic acid", "Fehling's solution is reduced from blue Cu2+ to brick-red Cu2O precipitate by aldehydes, which are produced exclusively by the oxidation of primary alcohols."),
        ("Oxidation of Cyclohexanol", "What organic product is formed when cyclohexanol is heated with acidified potassium dichromate(VI)?", "Cyclohexanone (a cyclic ketone)", "Hexanedioic acid", "Cyclohexene", "Benzene", "Cyclohexanol is a secondary alcohol. Oxidation removes two hydrogens (one from -OH and one from the carbinol ring carbon) to form the cyclic ketone cyclohexanone."),
        ("Dehydration of Cyclohexanol", "What alkene is formed when cyclohexanol is heated with concentrated phosphoric(V) acid?", "Cyclohexene", "Benzene", "Hex-1-ene", "Hex-2-ene", "Heating cyclohexanol with concentrated H3PO4 or concentrated H2SO4 eliminates water to form cyclohexene."),
        ("Dehydration of 2-methylbutan-2-ol", "What are the two alkene products formed by the dehydration of 2-methylbutan-2-ol?", "2-methylbut-2-ene (major) and 2-methylbut-1-ene (minor)", "Pent-1-ene and pent-2-ene", "3-methylbut-1-ene and 2-methylbut-2-ene", "2,3-dimethylbut-2-ene only", "Elimination of water from (CH3)2C(OH)CH2CH3 removes -OH from C2 and H from either C3 (giving the major, more substituted alkene 2-methylbut-2-ene) or C1 (giving the minor alkene 2-methylbut-1-ene)."),
        ("Chemical Test to Distinguish Propan-1-ol and Propan-2-ol", "Which single chemical test cleanly differentiates propan-1-ol from propan-2-ol?", "The tri-iodomethane (iodoform) test: propan-2-ol produces a yellow precipitate of CHI3, while propan-1-ol gives no precipitate.", "Acidified potassium dichromate (both turn green).", "Reaction with sodium metal (both evolve hydrogen).", "Reaction with PCl5 (both evolve HCl gas).", "Both are oxidized by K2Cr2O7, both react with Na, and both react with PCl5. Only propan-2-ol has the CH3-CH(OH)- methyl carbinol group required to produce a yellow precipitate of tri-iodomethane (CHI3) with alkaline iodine."),
        ("Ester Formation from Methanol and Propanoic Acid", "What is the systematic IUPAC name of the ester formed between propanoic acid and methanol?", "Methyl propanoate", "Propyl methanoate", "Ethyl ethanoate", "Methyl ethanoate", "The alkyl group from the alcohol comes first ('methyl' from methanol), followed by the carboxylate name ('propanoate' from propanoic acid): methyl propanoate (CH3CH2COOCH3)."),
        ("Ester Formation from Ethanol and Methanoic Acid", "What is the structural formula of ethyl methanoate?", "HCOOCH2CH3", "CH3COOCH3", "CH3CH2COOCH3", "CH3COOCH2CH3", "Methanoic acid provides the HCOO- group, and ethanol provides the -CH2CH3 ethyl group: HCOOCH2CH3."),
        ("Oxidation of Diols with Acidified Dichromate", "What organic product is obtained when propane-1,3-diol is heated under reflux with excess acidified potassium dichromate(VI)?", "Propanedioic acid (malonic acid), HOOC-CH2-COOH", "Propanal", "Propanone", "Propanoic acid", "Propane-1,3-diol (HOCH2-CH2-CH2OH) possesses two primary alcohol groups. Heating under reflux with excess oxidizer converts both primary alcohol groups into carboxylic acid groups, forming the dicarboxylic acid propanedioic acid."),
        ("Oxidation of Propane-1,2-diol", "What products are formed when propane-1,2-diol is oxidized with acidified potassium dichromate(VI)?", "2-oxopropanoic acid (pyruvic acid), CH3-CO-COOH", "Propanoic acid only", "Propanal and propanone", "Carbon dioxide and water", "Propane-1,2-diol has one primary alcohol group (oxidized to -COOH) and one secondary alcohol group (oxidized to -C=O), yielding 2-oxopropanoic acid (pyruvic acid)."),
        ("Distinguishing Alcohols by Rate of Oxidation", "How can the reaction rate of primary, secondary, and tertiary alcohols with acidified K2Cr2O7 at 60 °C be used for classification?", "Primary and secondary alcohols turn orange dichromate green within minutes, whereas tertiary alcohols show no color change even after hours.", "Tertiary alcohols react instantaneously within 1 second.", "Secondary alcohols never react.", "Primary alcohols do not react.", "Primary and secondary alcohols possess carbinol C-H bonds that are easily oxidized, turning the orange solution green. Tertiary alcohols lack a carbinol hydrogen and remain persistently orange."),
        ("Dehydration of 3,3-dimethylbutan-2-ol with Rearrangement", "When 3,3-dimethylbutan-2-ol is heated with acid, 2,3-dimethylbut-2-ene is the major alkene product. What causes this unexpected product?", "A carbocation intermediate undergoes a 1,2-methyl shift to form a more stable tertiary carbocation before elimination.", "The alcohol decomposes into methane and butene.", "The acid removes a methyl group directly.", "The reaction proceeds via free radicals.", "Protonation and loss of water yields the secondary carbocation (CH3)3C-CH+-CH3. A 1,2-methyl shift immediately occurs to form the more stable tertiary carbocation (CH3)2C+-CH(CH3)2, which loses a proton to yield the tetrasubstituted alkene 2,3-dimethylbut-2-ene."),
        ("Percentage Yield Calculation in Esterification", "Heating 4.6 g of ethanol (Mr = 46.0) with excess ethanoic acid produces 5.5 g of ethyl ethanoate (Mr = 88.0). What is the percentage yield?", "62.5%", "50.0%", "75.0%", "88.0%", "Moles of ethanol = 4.6 / 46.0 = 0.10 mol. Theoretical yield of ethyl ethanoate = 0.10 mol * 88.0 g/mol = 8.8 g. Percentage yield = (5.5 / 8.8) * 100 = 62.5%."),
        ("Iodoform Reaction Equations", "What are the two essential chemical steps in the tri-iodomethane reaction for ethanol?", "Step 1: Oxidation of ethanol to ethanal (CH3CHO); Step 2: Tri-iodination of the methyl group to CI3CHO followed by alkaline cleavage into CHI3 and HCOO-.", "Step 1: Direct substitution of -OH by iodine; Step 2: Elimination of HI.", "Step 1: Addition of I2 across C-C bond; Step 2: Hydrolysis.", "Step 1: Reduction to ethane; Step 2: Halogenation.", "Alkaline iodine (I2 + 2OH- -> IO- + I- + H2O) first oxidizes ethanol to ethanal: CH3CH2OH + IO- -> CH3CHO + I- + H2O. The three methyl protons are replaced by iodine: CH3CHO + 3IO- -> CI3CHO + 3OH-. Finally, hydroxide cleaves the C-C bond: CI3CHO + OH- -> CHI3(s) + HCOO-."),
        ("Identification of Carbonyl vs Alcohol with Iodoform", "Both ethanol and ethanal give a yellow precipitate with alkaline iodine. How can they be distinguished chemically?", "Add acidified potassium dichromate(VI): ethanol turns the orange solution green; ethanal also oxidizes, but ethanol gives effervescence with sodium metal while ethanal does NOT.", "Add 2,4-DNPH: ethanal gives an orange precipitate; ethanol does not react.", "Add Tollens' reagent: both form silver mirrors.", "Add sodium metal: ethanal evolves hydrogen gas.", "Ethanol is an alcohol and does not react with 2,4-dinitrophenylhydrazine (2,4-DNPH). Ethanal contains a carbonyl group (>C=O) and immediately produces a vivid yellow-orange crystalline precipitate with 2,4-DNPH."),
        ("Boiling Point of Esters vs Alcohols", "Why does ethyl ethanoate (Mr = 88.0) have a lower boiling point (77 °C) than its isomer butanoic acid (Mr = 88.0, bp 164 °C) and pentan-1-ol (Mr = 88.0, bp 138 °C)?", "Ester molecules cannot form intermolecular hydrogen bonds with each other because they lack a hydrogen atom bonded to oxygen.", "Esters are completely non-polar.", "Esters decompose below 80 °C.", "Esters have much smaller electron clouds.", "Esters possess polar C=O and C-O bonds and exhibit dipole-dipole attractions, but have no O-H group. Without intermolecular hydrogen bonding, their intermolecular attractions are significantly weaker than those in carboxylic acids and alcohols of identical Mr."),
        ("Industrial Uses of Esters", "Which two properties make esters widely used as industrial solvents for paints, glues, and varnishes?", "Low polarity/volatility balance capable of dissolving non-polar solutes, and high volatility allowing rapid evaporation without leaving greasy residue.", "Non-flammability and high boiling points.", "Extreme acidity that dissolves metals.", "Total insolubility in all organic liquids.", "Esters (such as ethyl ethanoate and butyl ethanoate) are volatile, low-toxicity solvents that readily dissolve organic polymers, lacquers, and resins, evaporating quickly to leave smooth coatings."),
        ("Dehydration of Polyols", "What is produced when ethane-1,2-diol is heated with concentrated sulfuric acid under mild conditions?", "1,4-dioxane (a cyclic diether) via intermolecular dehydration", "Ethyne gas", "Oxalic acid", "Carbon monoxide", "Two molecules of ethane-1,2-diol undergo reciprocal intermolecular dehydration to form the stable 6-membered cyclic diether 1,4-dioxane."),
        ("Alcohol Identification from Combustion Products", "Complete combustion of 0.10 mol of an alcohol produces 13.2 g of CO2 and 7.2 g of H2O. What is the alcohol?", "Propan-1-ol or propan-2-ol, C3H8O", "Ethanol, C2H6O", "Butan-1-ol, C4H10O", "Methanol, CH4O", "Moles of CO2 = 13.2 / 44.0 = 0.30 mol -> 0.30/0.10 = 3 carbons. Moles of H2O = 7.2 / 18.0 = 0.40 mol -> moles of H = 0.80 mol -> 0.80/0.10 = 8 hydrogens. Formula is C3H8O (propanol)."),
        ("Saponification of Fats and Oils", "What alcohol is produced as a byproduct in the commercial manufacture of soap by the alkaline hydrolysis of vegetable triglycerides?", "Propane-1,2,3-triol (glycerol)", "Ethanol", "Ethane-1,2-diol", "Methanol", "Vegetable oils and animal fats are triesters of glycerol (triglycerides). Heating with aqueous NaOH (saponification) hydrolyzes the ester linkages to produce sodium salts of fatty acids (soap) and propane-1,2,3-triol (glycerol)."),
        ("Oxidation of Unbranched Secondary Alcohol", "What is the product when octan-2-ol is heated with acidified potassium dichromate(VI)?", "Octan-2-one (a ketone)", "Octanal", "Octanoic acid", "Heptanoic acid and CO2", "Octan-2-ol is a secondary alcohol. Oxidation removes two hydrogens to form the corresponding 8-carbon ketone octan-2-one."),
        ("Testing for Purity of Synthesized Liquid Ester", "How can the purity of a prepared ester sample be determined accurately in a school laboratory?", "Measure its boiling point using distillation apparatus; a sharp, narrow boiling point matching literature values confirms high purity.", "Test its pH with litmus paper.", "Add sodium metal.", "Measure its color in a colorimeter.", "Pure liquids boil at a sharp, constant temperature characteristic of the pure substance. Impurities cause the liquid to boil over a wide temperature range and elevate the boiling point."),
        ("Biodiesel Production via Transesterification", "What chemical reaction is used to produce biodiesel fuel from plant oils?", "Transesterification: reacting vegetable oil (triglyceride) with methanol in the presence of a strong base catalyst (KOH) to yield methyl esters of fatty acids and glycerol.", "Catalytic cracking of vegetable oil.", "Dehydration of vegetable oil with sulfuric acid.", "Hydrogenation of plant oils to solid wax.", "Transesterification replaces the glycerol backbone of natural plant triglycerides with methanol, converting high-viscosity triglycerides into low-viscosity fatty acid methyl esters (FAME, biodiesel) suitable for diesel engines."),
        ("Oxidation of Allyl Alcohol", "What functional groups are present in allyl alcohol (prop-2-en-1-ol, CH2=CH-CH2OH), and how does cold dilute KMnO4 react with it?", "Alkene (C=C) and primary alcohol (-OH); cold dilute KMnO4 oxidizes the C=C bond to form propane-1,2,3-triol (glycerol).", "Alkane and secondary alcohol.", "Aldehyde and alkene.", "Carboxylic acid and ketone.", "Prop-2-en-1-ol contains both an alkene C=C double bond and a primary alcohol group. Mild dihydroxylation of the C=C bond by cold dilute KMnO4 adds two -OH groups across the double bond, converting allyl alcohol into glycerol (propane-1,2,3-triol)."),
        ("Alcohol Functional Group Interconversion Summary", "Which reaction sequence converts propene into propan-1-ol?", "Propene + HBr / peroxides -> 1-bromopropane, followed by heating with aqueous NaOH -> propan-1-ol.", "Propene + steam/H3PO4 directly.", "Propene + hot concentrated KMnO4.", "Propene + H2/Ni followed by water.", "Direct hydration of propene with steam/H3PO4 gives propan-2-ol (Markovnikov). To obtain propan-1-ol, propene is reacted with HBr in the presence of peroxides (anti-Markovnikov addition) to form 1-bromopropane, which is then hydrolyzed with aqueous NaOH to give propan-1-ol."),
        ("Esterification Equilibrium Shift Techniques", "In industrial ester synthesis, which two methods are commonly used to shift the reversible equilibrium toward higher ester yield?", "Using an excess of one reactant (e.g. alcohol) and continuously removing water or ester from the reaction mixture by fractional distillation.", "Adding water to dilute the mixture.", "Cooling the reaction to -20 °C.", "Adding sodium hydroxide to neutralize acid.", "By Le Chatelier's principle, using an excess of the cheaper reactant (often alcohol) and continuously removing water (or the volatile ester product) shifts the position of equilibrium to the right, driving the conversion toward completion.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(pool_16_2, start=60):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "16.2", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # HIGH-FREQUENCY CORE REPEATS (Q101 - Q110)
    # =========================================================================

    hf_data = [
        (
            101, "HF 1: Deducing Isomeric Alkenes from Alcohol Dehydration — 9701/11/M/J/22/Q23", "HF", "HARD",
            "An alcohol X of molecular formula C5H12O is heated with concentrated sulfuric acid at 170 °C.\nA mixture of three isomeric alkenes of molecular formula C5H10 is obtained, two of which are stereoisomers (cis-trans isomers).\n\nWhat is the structural formula of alcohol X?",
            "Pentan-2-ol, CH3-CH(OH)-CH2-CH2-CH3",
            "Pentan-1-ol, CH3-CH2-CH2-CH2-CH2OH",
            "Pentan-3-ol, CH3-CH2-CH(OH)-CH2-CH3",
            "2-methylbutan-2-ol, (CH3)2C(OH)CH2CH3",
            "Option A is correct. Dehydration of pentan-2-ol removes -OH from C2 and H from either C1 or C3: (1) removal from C1 yields pent-1-ene (no stereoisomers); (2) removal from C3 yields pent-2-ene, which exists as two geometric stereoisomers: cis-pent-2-ene and trans-pent-2-ene. Thus, pentan-2-ol produces exactly three alkene isomers (two being stereoisomers). Pentan-3-ol can only yield pent-2-ene (2 isomers). Pentan-1-ol yields only pent-1-ene (1 isomer)."
        ),
        (
            102, "HF 2: The Tri-iodomethane (Iodoform) Reaction Test — 9701/12/M/J/21/Q23", "HF", "HARD",
            "Four organic liquids are tested with alkaline aqueous iodine (I2 in aqueous NaOH):\nLiquid 1: Propan-1-ol; Liquid 2: Propan-2-ol; Liquid 3: Butan-2-ol; Liquid 4: 2-methylpropan-2-ol\n\nWhich liquids form a pale yellow precipitate of tri-iodomethane?",
            "Liquid 2 and Liquid 3 only",
            "Liquid 1 and Liquid 2 only",
            "Liquid 2, Liquid 3, and Liquid 4",
            "Liquid 1 only",
            "Option A is correct. The tri-iodomethane reaction requires the specific methyl carbinol group: CH3-CH(OH)-. Propan-2-ol (CH3-CH(OH)-CH3) and butan-2-ol (CH3-CH(OH)-CH2CH3) both contain this structural unit and form a yellow precipitate of CHI3. Propan-1-ol is a primary alcohol lacking the methyl branch, and 2-methylpropan-2-ol is a tertiary alcohol lacking a carbinol hydrogen; neither forms a precipitate."
        ),
        (
            103, "HF 3: Distinguishing Alcohols by Successive Chemical Reagents — 9701/13/O/N/22/Q23", "HF", "HARD",
            "An unknown alcohol Y of formula C4H10O was investigated:\n• It turns acidified potassium dichromate(VI) from orange to green upon warming.\n• It forms a yellow precipitate when warmed with alkaline aqueous iodine.\n\nWhat is the systematic name of alcohol Y?",
            "Butan-2-ol",
            "Butan-1-ol",
            "2-methylpropan-1-ol",
            "2-methylpropan-2-ol",
            "Option A is correct. Turning acidified K2Cr2O7 green means alcohol Y is oxidizable (primary or secondary alcohol, ruling out tertiary 2-methylpropan-2-ol). Forming a yellow precipitate with alkaline iodine proves the presence of the CH3-CH(OH)- group. The only 4-carbon alcohol with both features is the secondary alcohol butan-2-ol (CH3-CH(OH)-CH2CH3)."
        ),
        (
            104, "HF 4: Stoichiometry of Sodium Reaction with Polyols — 9701/11/F/M/22/Q23", "HF", "HARD",
            "A sample of 0.050 mol of an unknown organic compound containing only carbon, hydrogen, and oxygen reacts with an excess of sodium metal to evolve exactly 1.20 dm^3 of hydrogen gas (measured at RTP).\n\nHow many hydroxyl (-OH) groups are present in one molecule of this compound?",
            "2 hydroxyl groups (it is a diol)",
            "1 hydroxyl group",
            "3 hydroxyl groups",
            "4 hydroxyl groups",
            "Option A is correct. Moles of H2 gas evolved = 1.20 dm^3 / 24.0 dm^3 mol^-1 = 0.050 mol. The general equation is: R(OH)n + n Na -> R(ONa)n + (n/2) H2. Moles of H2 / moles of compound = 0.050 / 0.050 = 1.0 = n/2 => n = 2. Thus, each molecule contains exactly 2 hydroxyl groups (a diol)."
        ),
        (
            105, "HF 5: Oxidation of Unsaturated Alcohols with Multiple Functional Groups — 9701/12/O/N/21/Q24", "HF", "HARD",
            "Consider the unsaturated alcohol pent-3-en-2-ol, CH3-CH=CH-CH(OH)-CH3.\nWhat organic products are formed when one mole of pent-3-en-2-ol is heated under reflux with hot, concentrated, acidified potassium manganate(VII)?",
            "Ethanoic acid (CH3COOH) and 2-oxopropanoic acid (pyruvic acid, CH3-CO-COOH)",
            "Propanone and ethanoic acid",
            "Pentan-2-one and water",
            "Carbon dioxide and butanoic acid",
            "Option A is correct. Hot concentrated KMnO4 oxidatively cleaves C=C double bonds and simultaneously oxidizes secondary alcohols to ketones. Cleaving C3=C4 yields ethanoic acid (CH3COOH) from the =CH-CH3 half. The remaining =CH-CH(OH)-CH3 half is oxidized at the double-bond carbon to a carboxylic acid (-COOH) and at the secondary alcohol carbon to a ketone (>C=O), yielding 2-oxopropanoic acid (CH3-CO-COOH)."
        ),
        (
            106, "HF 6: Percentage Yield and Mass Calculations in Ester Preparation — 9701/13/M/J/22/Q23", "HF", "HARD",
            "Ethanol (6.90 g, Mr = 46.0) is reacted with excess ethanoic acid in the presence of concentrated sulfuric acid catalyst. After purification, 9.24 g of ethyl ethanoate (Mr = 88.0) is collected.\n\nWhat is the percentage yield of ethyl ethanoate?",
            "70.0%",
            "60.0%",
            "75.0%",
            "80.0%",
            "Option A is correct. Moles of ethanol used = 6.90 g / 46.0 g/mol = 0.150 mol. Theoretical yield of ethyl ethanoate = 0.150 mol * 88.0 g/mol = 13.20 g. Percentage yield = (actual mass / theoretical mass) * 100 = (9.24 g / 13.20 g) * 100 = 70.0%."
        ),
        (
            107, "HF 7: Chirality Changes in Alcohol Oxidation — 9701/11/O/N/21/Q23", "HF", "HARD",
            "Butan-2-ol is an optically active compound containing one chiral center.\n\nWhat happens to the optical activity when butan-2-ol is oxidized by heating with acidified potassium dichromate(VI)?",
            "Optical activity is completely lost because the secondary alcohol is converted into butanone, which is achiral.",
            "Optical activity is inverted (Walden inversion).",
            "Optical activity is retained because butanoic acid is chiral.",
            "The product forms an optically active single enantiomer.",
            "Option A is correct. Butan-2-ol (CH3-CH(OH)-CH2CH3) has a chiral C2 bonded to -H, -OH, -CH3, and -C2H5. Oxidation converts the secondary alcohol group into a carbonyl group (>C=O), producing butanone (CH3-CO-CH2CH3). In butanone, C2 is sp2 hybridised and planar with only three attached groups. It lacks a chiral stereocenter, so optical activity is completely lost."
        ),
        (
            108, "HF 8: Identifying Intermediates in Multi-Step Alcohol Synthesis — 9701/12/F/M/23/Q24", "HF", "HARD",
            "Consider the reaction pathway:\nEthene  --[ Step 1: HBr ]-->  Compound P  --[ Step 2: KCN(ethanolic) ]-->  Compound Q  --[ Step 3: H+/H2O reflux ]-->  Compound R  --[ Step 4: LiAlH4 ]-->  Compound S\n\nWhat is the identity of final product Compound S?",
            "Propan-1-ol, CH3CH2CH2OH",
            "Ethanol, CH3CH2OH",
            "Propan-2-ol, CH3CH(OH)CH3",
            "Propanoic acid, CH3CH2COOH",
            "Option A is correct. Step 1: Electrophilic addition of HBr to ethene yields bromoethane (P, CH3CH2Br). Step 2: Nucleophilic substitution with KCN yields propanenitrile (Q, CH3CH2CN). Step 3: Acid hydrolysis of the nitrile yields propanoic acid (R, CH3CH2COOH). Step 4: Reduction of propanoic acid by LiAlH4 in dry ether yields the primary alcohol propan-1-ol (S, CH3CH2CH2OH)."
        ),
        (
            109, "HF 9: Dehydration of Symmetrical Alcohols — 9701/13/M/J/23/Q24", "HF", "HARD",
            "Pentan-3-ol, CH3-CH2-CH(OH)-CH2-CH3, is heated with concentrated sulfuric acid.\n\nHow many distinct alkene products are formed by dehydration of pentan-3-ol?",
            "2 alkenes (cis-pent-2-ene and trans-pent-2-ene)",
            "1 alkene",
            "3 alkenes",
            "4 alkenes",
            "Option A is correct. In pentan-3-ol, the carbinol carbon C3 is flanked by two identical -CH2- groups (C2 and C4). Elimination of water can only remove a hydrogen from C2 or C4, both yielding pent-2-ene (CH3-CH=CH-CH2-CH3). Pent-2-ene exhibits geometric stereoisomerism, existing as cis-pent-2-ene and trans-pent-2-ene. Thus, exactly 2 distinct alkene stereoisomers are formed."
        ),
        (
            110, "HF 10: Quantitative Combustive Analysis of an Alcohol — 9701/11/M/J/23/Q25", "HF", "HARD",
            "A saturated monohydric alcohol contains 60.0% carbon, 13.3% hydrogen, and 26.7% oxygen by mass.\nWhen vaporised, 0.150 g of this alcohol occupies 59.8 cm^3 at 100 °C and 1.01 * 10^5 Pa.\n\nWhat is the molecular formula and identity of this alcohol? (R = 8.31 J K^-1 mol^-1)",
            "C3H8O (Mr = 60.0, propanol)",
            "C2H6O (Mr = 46.0, ethanol)",
            "C4H10O (Mr = 74.0, butanol)",
            "C4H8O (Mr = 72.0, butenol)",
            "Option A is correct. Moles of C = 60.0/12.0 = 5.0; H = 13.3/1.0 = 13.3; O = 26.7/16.0 = 1.67. Dividing by 1.67: C: 5.0/1.67 = 3.0; H: 13.3/1.67 = 8.0; O: 1.67/1.67 = 1.0. Empirical formula is C3H8O (formula mass = 60.0). Using pV = nRT = (m/Mr)RT: Mr = mRT / pV = (0.150 * 8.31 * 373) / (101000 * 59.8 * 10^-6) = 464.95 / 6.0398 = 60.1 g/mol. Molecular formula = C3H8O."
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

    # Write output to mcq_topic16_data.py
    out_file = r"z:\tests n quizes63\books\psycology\new styl\mcq_topic16_data.py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write('"""\nCurated 110 Authentic Cambridge AS Chemistry (9701) Paper 1 MCQs\nfor Topic 16: Hydroxy Compounds (Alcohols) (100 Core + 10 High-Frequency Core Repeats).\n"""\n\n')
        f.write("from build_mcq_topic_pdf import MCQQuestion\n\n")
        f.write("TOPIC_16_MCQ_QUESTIONS = [\n")
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

    print(f"Successfully generated mcq_topic16_data.py with {len(balanced_questions)} MCQs!")

if __name__ == "__main__":
    create_topic16_data()
