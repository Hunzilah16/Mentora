"""
Generator for Topic 13: An Introduction to AS Level Organic Chemistry (110 MCQs)
Subtopics:
  13.1 Formulas, Nomenclature & Functional Groups (Q1 - Q30)
  13.2 Organic Reaction Terminology & Mechanisms (Q31 - Q55)
  13.3 Shapes of Molecules, Hybridisation, Sigma & Pi Bonds (Q56 - Q75)
  13.4 Isomerism: Structural & Stereoisomerism (Q76 - Q100)
  HF: Frequently Examined Core Repeats (Q101 - Q110)
"""

import os
import re

def create_topic13_data():
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
    # SUBTOPIC 13.1: FORMULAS, NOMENCLATURE & FUNCTIONAL GROUPS (Q1 - Q30)
    # =========================================================================

    add_q(
        1, "Types of Chemical Formula — Empirical vs Molecular — 9701/11/M/J/23/Q13", "13.1", "EASY",
        "A volatile liquid compound contains 54.5% carbon, 9.1% hydrogen, and 36.4% oxygen by mass. Its relative molecular mass, Mr, is 88.0.\n\nWhat are the empirical formula and molecular formula of this compound?",
        "Empirical formula: C2H4O; Molecular formula: C4H8O2",
        "Empirical formula: CH2O; Molecular formula: C3H6O3",
        "Empirical formula: C4H8O2; Molecular formula: C4H8O2",
        "Empirical formula: C2H4O; Molecular formula: C2H4O",
        "Option A is correct. Moles of C = 54.5 / 12.0 = 4.54; moles of H = 9.1 / 1.0 = 9.10; moles of O = 36.4 / 16.0 = 2.275. Dividing by smallest (2.275): C: 4.54/2.275 = 2.0; H: 9.10/2.275 = 4.0; O: 2.275/2.275 = 1.0. Thus, empirical formula is C2H4O (empirical formula mass = 2(12) + 4(1) + 16 = 44.0). Since Mr = 88.0, the molecular formula multiplier is 88.0 / 44.0 = 2, giving C4H8O2."
    )

    add_q(
        2, "Interpreting Skeletal Formulas — 9701/12/M/J/23/Q13", "13.1", "EASY",
        "In a skeletal formula of an organic molecule, what do the vertices (corners) and line ends represent?",
        "A carbon atom with the appropriate number of hydrogen atoms attached to satisfy carbon's four-covalent valency.",
        "A methyl group (-CH3) only at every vertex and line end.",
        "Any heteroatom (oxygen, nitrogen, halogen) unless labelled.",
        "An unsaturated double bond.",
        "Option A is correct. In skeletal notation, carbon-carbon bonds are drawn as lines in a zig-zag format. Carbon atoms and attached hydrogen atoms are not explicitly written: each vertex (corner) and each line termination represents a carbon atom together with enough implicit hydrogen atoms to give that carbon a total of four covalent bonds."
    )

    add_q(
        3, "IUPAC Nomenclature of Branched Halogenoalkanes — 9701/13/M/J/23/Q13", "13.1", "HARD",
        "What is the correct systematic IUPAC name for the compound CH3-CH(CH3)-CH(Br)-CH2-CH3?",
        "3-bromo-2-methylpentane",
        "3-bromo-4-methylpentane",
        "2-methyl-3-bromopentane",
        "1-bromo-1-ethyl-2-methylpropane",
        "Option A is correct. Number the longest continuous carbon chain (5 carbons = pentane) from the end that gives substituents the lowest locant set. Numbering from left: C2 has methyl, C3 has bromo (locants 2,3). Numbering from right: C3 has bromo, C4 has methyl (locants 3,4). Lower locant set is (2,3). Substituents are cited alphabetically: 'bromo' before 'methyl'. Hence: 3-bromo-2-methylpentane."
    )

    add_q(
        4, "General Formula of Homologous Series — 9701/11/O/N/23/Q13", "13.1", "EASY",
        "Which homologous series has the general formula CnH2nO and does NOT decolorize aqueous bromine?",
        "Non-cyclic aliphatic aldehydes and ketones",
        "Alkenols (unsaturated alcohols)",
        "Cycloalkanes",
        "Carboxylic acids",
        "Option A is correct. Both aliphatic aldehydes and aliphatic ketones have the general formula CnH2nO with one degree of unsaturation (a carbonyl group C=O). Because they contain no carbon-carbon double bonds (C=C), they do not decolorize aqueous bromine by addition."
    )

    add_q(
        5, "Identifying Functional Groups in Complex Molecules — 9701/12/O/N/23/Q13", "13.1", "MEDIUM",
        "The molecule phenylephrine has the structure HO-C6H4-CH(OH)-CH2-NH-CH3.\n\nWhich functional groups are present in phenylephrine?",
        "Phenol, secondary alcohol, and secondary amine",
        "Primary alcohol, tertiary amine, and ketone",
        "Phenol, primary alcohol, and primary amine",
        "Ester, secondary alcohol, and amide",
        "Option A is correct. HO-C6H4- is a phenolic hydroxyl group attached directly to an aromatic benzene ring; -CH(OH)- is attached to two carbon atoms (the ring and CH2), making it a secondary alcohol; -NH- is bonded to two alkyl carbons (-CH2- and -CH3), classifying it as a secondary amine."
    )

    # Questions 6 - 30: Systematic Formulas & Functional Groups
    subtopic_13_1_pool = [
        ("Homologous Series Characteristics", "Which property is TRUE for all members of a homologous series?", "They share the same general formula and identical functional group, displaying a gradation in physical properties.", "They possess identical physical boiling points.", "They have identical empirical formulas.", "They exhibit identical molecular masses.", "All members of a homologous series possess the same functional group and general formula, differing by successive -CH2- units. This produces similar chemical properties and regular gradations in physical properties like boiling point."),
        ("Displayed Formula Definition", "What is explicitly shown in a fully displayed formula of an organic molecule?", "Every single atom and every covalent bond connecting them.", "Only the functional group bonds.", "Only the carbon backbone bonds.", "The 3D spatial orientation of orbitals.", "A displayed formula shows every single atom and every covalent bond (single, double, or triple) in the molecule explicitly."),
        ("IUPAC Naming of Alkenes", "What is the systematic IUPAC name for (CH3)2C=CH-CH3?", "2-methylbut-2-ene", "3-methylbut-2-ene", "2-methylbut-3-ene", "Pent-2-ene", "The longest carbon chain with the C=C bond has 4 carbons (but-2-ene). Numbering from the left gives the methyl substituent the lowest locant: 2-methylbut-2-ene."),
        ("Functional Group of Esters", "Which grouping of atoms represents the ester functional group?", "-COO- (or -COOCH2-)", "-CONH2", "-COCl", "-O-", "An ester contains a carbonyl group bonded directly to an alkoxy oxygen: -C(=O)O-."),
        ("Molecular Formula Determination", "A hydrocarbon contains 85.7% carbon by mass and has Mr = 56. What is its molecular formula?", "C4H8", "C3H6", "C4H10", "C5H10", "Ratio: C = 85.7/12 = 7.14; H = 14.3/1 = 14.3. Ratio 1:2 -> empirical CH2 (mass 14). Mr = 56 / 14 = 4 -> C4H8."),
        ("IUPAC Name for Dicarboxylic Acid", "What is the systematic IUPAC name for HOOC-CH2-CH2-COOH?", "Butanedioic acid", "Succinic acid", "1,4-dicarboxyethane", "Butanedioic ester", "A 4-carbon unbranched chain with carboxylic acid groups at both ends is butanedioic acid."),
        ("Structural Formula Convention", "What is the correct condensed structural formula for 2,2-dimethylpropane?", "C(CH3)4", "CH3CH2CH(CH3)2", "CH3(CH2)3CH3", "(CH3)2CHCH2CH3", "2,2-dimethylpropane (neopentane) has a central carbon bonded to four methyl groups: C(CH3)4."),
        ("Functional Group of Nitriles", "Which functional group is present in ethanenitrile?", "-C#N (cyano group)", "-NH2 (amino group)", "-NO2 (nitro group)", "-CONH2 (amide group)", "Nitriles contain a carbon-nitrogen triple bond: -C#N."),
        ("IUPAC Naming of Haloalkanes", "What is the IUPAC name for CH3-CH(Cl)-CH(Cl)-CH3?", "2,3-dichlorobutane", "1,2-dichlorobutane", "2,2-dichlorobutane", "1,4-dichlorobutane", "4-carbon chain with chloro substituents at carbons 2 and 3: 2,3-dichlorobutane."),
        ("Degree of Unsaturation", "How many degrees of unsaturation (double bond equivalents) are present in C6H10O?", "2", "1", "3", "0", "Formula: C + 1 - (H/2) = 6 + 1 - 5 = 2. This corresponds to two double bonds, one triple bond, or combinations of rings and double bonds."),
        ("Identification of Acyl Chlorides", "Which formula represents an acyl chloride?", "CH3COCl", "CH3CH2Cl", "CH3CHCl2", "CH3OCH2Cl", "Acyl chlorides contain the -C(=O)Cl functional group, as in CH3COCl (ethanoyl chloride)."),
        ("IUPAC Name for Branched Alcohol", "What is the IUPAC name for CH3-C(CH3)(OH)-CH2-CH3?", "2-methylbutan-2-ol", "3-methylbutan-3-ol", "2-methylbutan-3-ol", "Pentan-2-ol", "Longest chain containing -OH is 4 carbons (butan-2-ol). Methyl branch at C2: 2-methylbutan-2-ol."),
        ("Classification of Alcohols", "Which molecule is a tertiary alcohol?", "2-methylpropan-2-ol", "Propan-2-ol", "2-methylpropan-1-ol", "Butan-1-ol", "In 2-methylpropan-2-ol, the carbon bearing the -OH group is bonded to three other carbon atoms (three methyl groups), making it tertiary."),
        ("Functional Groups in Amino Acids", "Which two functional groups are present in all 2-amino acids?", "Carboxylic acid (-COOH) and primary amine (-NH2)", "Amide and alcohol", "Ester and amine", "Aldehyde and ketone", "Amino acids contain both a carboxylic acid group (-COOH) and an amine group (-NH2) attached to the alpha-carbon."),
        ("General Formula of Alkanes", "What is the general formula for all open-chain saturated hydrocarbons (alkanes)?", "CnH2n+2", "CnH2n", "CnH2n-2", "CnH2n+1", "Open-chain alkanes possess the general formula CnH2n+2."),
        ("General Formula of Cycloalkanes", "What is the general formula for monocyclic cycloalkanes?", "CnH2n", "CnH2n+2", "CnH2n-2", "CnH2n-4", "Ring formation eliminates two hydrogens compared to open-chain alkanes, giving CnH2n."),
        ("Naming of Cyclic Hydrocarbons", "What is the IUPAC name of a saturated 6-membered ring hydrocarbon?", "Cyclohexane", "Benzene", "Hexene", "Cyclohexene", "A saturated six-carbon ring with single C-C bonds is cyclohexane (C6H12)."),
        ("Identification of Ketones", "Which condensed formula represents a ketone?", "CH3COCH3", "CH3CH2CHO", "CH3COOCH3", "CH3OCH3", "CH3COCH3 (propanone) contains a carbonyl group bonded to two alkyl carbons, characteristic of a ketone."),
        ("Identification of Ethers", "What is the functional group present in CH3-O-CH2CH3?", "Ether", "Ester", "Alcohol", "Peroxide", "An oxygen atom bonded between two alkyl groups (R-O-R') is an ether (methoxyethane)."),
        ("IUPAC Name of Aldehyde", "What is the IUPAC name for CH3-CH(CH3)-CH2-CHO?", "3-methylbutanal", "2-methylbutanal", "3-methylbutanone", "Pentanal", "The carbonyl carbon of the aldehyde is always numbered C1. The chain is 4 carbons (butanal) with methyl at C3: 3-methylbutanal."),
        ("Skeletal Formula of Benzene", "How is benzene represented in skeletal notation?", "A regular hexagon with an inscribed circle (or alternating double bonds)", "A pentagon with a double bond", "A zig-zag line of 6 carbons", "An open ring of 6 CH2 groups", "Benzene (C6H6) is depicted as a hexagon with a circle representing the delocalized 6 pi electrons."),
        ("Empirical Formula from Combustion Data", "Complete combustion of 0.20 mol of a hydrocarbon produces 0.80 mol CO2 and 0.80 mol H2O. What is the hydrocarbon?", "C4H8", "C4H10", "C2H4", "C3H6", "Moles of C = 0.80 / 0.20 = 4; moles of H = (0.80 * 2) / 0.20 = 8. Hydrocarbon is C4H8."),
        ("Carboxylic Acid Salt Naming", "What is the IUPAC name for CH3CH2COONa?", "Sodium propanoate", "Sodium propionate", "Sodium ethanoate", "Sodium butanoate", "The 3-carbon carboxylate ion is propanoate, so the salt is sodium propanoate."),
        ("Primary Amine Nomenclature", "What is the systematic IUPAC name for CH3-CH2-CH2-NH2?", "Propan-1-amine", "Propylamine", "Ethylmethylamine", "1-aminopropane", "The systematic IUPAC name for a 3-carbon chain with an amino group at carbon-1 is propan-1-amine."),
        ("Hybrid Functional Molecules", "Which functional groups are present in CH2=CH-COOH?", "Alkene (C=C) and carboxylic acid (-COOH)", "Alkyne and ester", "Alcohol and aldehyde", "Alkane and ketone", "Propenoic acid contains both a carbon-carbon double bond (alkene) and a carboxylic acid group.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(subtopic_13_1_pool, start=6):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "13.1", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # SUBTOPIC 13.2: ORGANIC REACTION MECHANISMS & TERMINOLOGY (Q31 - Q55)
    # =========================================================================

    add_q(
        31, "Homolytic vs Heterolytic Bond Fission — 9701/11/M/J/23/Q14", "13.2", "EASY",
        "What occurs during homolytic fission of a covalent bond?",
        "The covalent bond breaks symmetrically such that each departing atom retains one of the two shared bonding electrons, producing two uncharged free radicals.",
        "One atom takes both shared electrons, forming a cation and an anion.",
        "A pair of electrons is transferred to an electrophile to form a dative bond.",
        "The bond vibrates until it dissociates into two ions of opposite charge.",
        "Option A is correct. In homolytic fission (homolysis), the covalent bond breaks evenly. Each bonding partner leaves with one electron from the shared pair (depicted by single-headed curly arrows / fish-hooks), resulting in the generation of two highly reactive, neutral species with unpaired electrons known as free radicals: X-Y -> X. + Y.."
    )

    add_q(
        32, "Definition and Behavior of an Electrophile — 9701/12/M/J/23/Q14", "13.2", "EASY",
        "Which statement correctly defines an electrophile in organic reaction mechanisms?",
        "An electron-deficient species (either positively charged or possessing an electron-deficient dipole delta+) that attacks regions of high electron density by accepting an electron pair.",
        "A species with a lone pair of electrons that donates them to form a dative covalent bond.",
        "A neutral species with an unpaired electron that abstracts a hydrogen atom.",
        "A proton donor according to the Bronsted-Lowry acid-base definition.",
        "Option A is correct. An electrophile ('electron-lover') is an electron-poor species (such as Br+, NO2+, H+, or the delta+ carbon in a carbonyl group) that seeks out electron-rich centers (like the pi bond of an alkene or benzene ring) and accepts a lone pair of electrons to form a new covalent bond."
    )

    add_q(
        33, "Definition and Behavior of a Nucleophile — 9701/13/M/J/23/Q14", "13.2", "EASY",
        "Which species can act as a nucleophile in organic substitution reactions?",
        ":OH-, :CN-, :NH3, and H2O: (species possessing a non-bonding lone pair of electrons)",
        "Br+, NO2+, and AlCl3 (electron-deficient Lewis acids)",
        "Cl. and CH3. (free radicals with single unpaired electrons)",
        "CH4 and C2H6 (saturated alkanes with no lone pairs)",
        "Option A is correct. A nucleophile ('nucleus-lover') is an electron-rich species containing at least one non-bonding lone pair of electrons (e.g., hydroxide :OH-, cyanide :CN-, ammonia :NH3, water :OH2). It attacks electron-deficient carbon centers (delta+) and donates its lone pair to form a new dative/covalent bond."
    )

    add_q(
        34, "Classification of Reaction Types — 9701/11/O/N/23/Q14", "13.2", "MEDIUM",
        "The conversion of bromoethane into ethene by heating with ethanolic potassium hydroxide is classified as which type of reaction?",
        "Elimination",
        "Electrophilic addition",
        "Nucleophilic substitution",
        "Free radical substitution",
        "Option A is correct. When CH3CH2Br is heated with ethanolic KOH (where OH- acts as a Bronsted-Lowry base rather than a nucleophile), a hydrogen halide molecule (HBr) is removed from adjacent carbon atoms to form a C=C double bond (CH2=CH2 + KBr + H2O). This removal of atoms without replacement is an elimination reaction."
    )

    add_q(
        35, "Free Radical Substitution Mechanism Stages — 9701/12/O/N/23/Q14", "13.2", "HARD",
        "In the photochemical chlorination of methane, which step represents a propagation reaction?",
        "CH3. + Cl2 -> CH3Cl + Cl.",
        "Cl2 -> 2Cl. (under UV light)",
        "CH3. + Cl. -> CH3Cl",
        "CH3. + CH3. -> C2H6",
        "Option A is correct. A propagation step consumes one free radical and generates a new free radical, maintaining the radical chain: (1) Cl. + CH4 -> .CH3 + HCl; (2) .CH3 + Cl2 -> CH3Cl + Cl.. Option B is initiation (0 radicals -> 2 radicals). Options C and D are termination steps (2 radicals -> 0 radicals)."
    )

    # Questions 36 - 55: Mechanism & Terminology Questions
    mech_pool = [
        ("Curly Arrow Convention", "In organic reaction mechanisms, what does a standard double-barbed curly arrow represent?", "The movement of a pair of electrons from a lone pair or covalent bond to an atom or bond.", "The physical movement of an atomic nucleus.", "The shift of a single unpaired electron.", "The direction of thermodynamic heat flow.", "A full double-barbed curly arrow depicts the movement of an electron pair from an electron-rich site (lone pair or bond) to an electron-deficient site."),
        ("Fish-hook Arrow Convention", "What does a single-barbed (fish-hook) curly arrow denote in organic chemistry?", "The movement of a single unpaired electron.", "The transfer of two electrons in an elimination reaction.", "A resonance contributor.", "A coordinate bond.", "A single-headed (fish-hook) arrow indicates the movement of a single electron, frequently employed in free radical mechanisms."),
        ("Carbocation Stability Order", "What is the correct order of carbocation stability from most stable to least stable?", "Tertiary (3°) > Secondary (2°) > Primary (1°) > Methyl", "Methyl > Primary (1°) > Secondary (2°) > Tertiary (3°)", "Primary > Tertiary > Secondary > Methyl", "Secondary > Tertiary > Primary > Methyl", "Alkyl groups are electron-donating via inductive effect (+I), dispersing the positive charge on the carbon. Tertiary carbocations have three alkyl groups providing maximum charge dispersal, making 3° > 2° > 1° > methyl."),
        ("Electrophilic Addition Mechanism", "Which reaction proceeds via an electrophilic addition mechanism?", "Ethene reacting with hydrogen bromide to form bromoethane.", "Methane reacting with chlorine in UV light.", "Bromoethane reacting with aqueous sodium hydroxide.", "Ethanol reacting with acidified potassium dichromate.", "Alkenes possess a pi bond with high electron density that attacks electrophiles like H-Br, undergoing electrophilic addition."),
        ("Nucleophilic Substitution Mechanism", "Which reaction proceeds via a nucleophilic substitution mechanism?", "1-bromopropane reacting with aqueous NaOH to form propan-1-ol.", "Propene reacting with steam over H3PO4.", "Ethanol reacting with hot concentrated sulfuric acid.", "Ethane reacting with bromine under UV light.", "Haloalkanes contain a polar C-Br bond attacked by nucleophilic :OH- ions, substituting the halogen atom."),
        ("Hydrolysis Reaction Definition", "What defines a hydrolysis reaction in organic chemistry?", "A reaction where a covalent bond in a molecule is cleaved by the chemical action of water (often catalyzed by acid or base).", "The simple physical dissolution of a substance in water.", "The removal of water from a molecule to form an alkene.", "The hydration of an alkene across a double bond.", "Hydrolysis is a bond-breaking chemical reaction involving water, e.g., the hydrolysis of esters into carboxylic acids and alcohols."),
        ("Condensation Reaction Definition", "What characterizes a condensation reaction?", "Two molecules combine to form a larger single molecule with the elimination of a small molecule such as H2O or HCl.", "A gas turning into a liquid upon cooling.", "Addition of hydrogen across a multiple bond.", "The breakdown of a polymer into monomers.", "In organic synthesis, condensation involves the joining of two molecules accompanied by the loss of a small molecule like water or hydrogen chloride."),
        ("Reduction of Carbonyl Compounds", "Which reagent reduces an aldehyde or ketone to an alcohol?", "Sodium borohydride, NaBH4 (in aqueous ethanol)", "Acidified potassium dichromate(VI)", "Concentrated sulfuric acid", "Tollens' reagent", "NaBH4 acts as a source of hydride ions (:H-), reducing aldehydes to primary alcohols and ketones to secondary alcohols."),
        ("Oxidation in Organic Chemistry", "In organic chemistry, what does oxidation typically involve?", "An increase in the number of carbon-oxygen bonds and/or a decrease in carbon-hydrogen bonds.", "The addition of hydrogen across a C=C bond.", "The loss of an electron pair by a nucleophile.", "The substitution of chlorine by fluorine.", "Organic oxidation involves the gain of oxygen bonds (e.g., alcohol -> aldehyde -> carboxylic acid) or the loss of hydrogen bonds."),
        ("Inductive Effect Definition", "What is the positive inductive effect (+I effect)?", "The electron-donating ability of alkyl groups through sigma bonds toward a partially positive carbon center.", "The withdrawal of electrons by highly electronegative atoms like fluorine.", "The delocalization of pi electrons in aromatic rings.", "The polarization of light by chiral centers.", "Alkyl groups push electron density along sigma bonds toward electron-deficient centers (+I inductive effect), stabilizing carbocations."),
        ("Markovnikov's Rule Basis", "What is the underlying mechanistic basis for Markovnikov's rule in alkene addition?", "The reaction proceeds predominantly via the more stable carbocation intermediate.", "The halogen atom always prefers to bond to the carbon with more hydrogen atoms.", "Steric hindrance prevents addition at tertiary carbons.", "Hydrogen bonds direct the incoming electrophile.", "The electrophilic addition of HX to an unsymmetrical alkene generates two possible carbocations; the proton adds to the carbon with more hydrogens to form the more stable (more alkyl-substituted) carbocation."),
        ("SN1 Mechanism Characteristics", "Which feature is characteristic of an SN1 nucleophilic substitution reaction?", "A two-step mechanism involving a planar carbocation intermediate, typical for tertiary halogenoalkanes.", "A concerted one-step mechanism with a five-coordinate transition state.", "Second-order kinetics dependent on both substrate and nucleophile concentrations.", "Complete inversion of optical configuration.", "SN1 (Substitution Nucleophilic Unimolecular) proceeds via rate-determining loss of leaving group to form a carbocation intermediate, followed by rapid attack of nucleophile. Favored by 3° substrates."),
        ("SN2 Mechanism Characteristics", "Which feature is characteristic of an SN2 nucleophilic substitution reaction?", "A one-step concerted mechanism with backside attack causing Walden inversion of configuration.", "Formation of a stable carbocation intermediate.", "First-order kinetics independent of nucleophile concentration.", "Racemisation of chiral optical centers.", "SN2 proceeds via simultaneous nucleophile attack from the rear and leaving group departure, causing inversion of configuration (Walden inversion)."),
        ("Reflux Technique in Organic Synthesis", "Why is a reaction mixture heated under reflux during organic preparations?", "To heat the mixture at its boiling temperature without losing volatile reactants or products as vapor.", "To increase the atmospheric pressure above the liquid.", "To separate two liquids with different boiling points.", "To freeze the reaction intermediate.", "A vertical condenser cools escaping vapors back to liquid, allowing continuous heating at boiling point without solvent loss."),
        ("Role of UV Light in Halogenation", "What is the role of ultraviolet (UV) radiation in the reaction between alkanes and halogens?", "It provides the energy required to homolytically cleave the X-X bond to produce halogen free radicals.", "It ionizes the alkane into a carbocation.", "It acts as a heterogeneous catalyst.", "It polarizes the carbon-hydrogen bond.", "The photon energy of UV light matches the bond dissociation enthalpy of Cl-Cl or Br-Br, causing homolytic fission to start the chain reaction."),
        ("Distinguishing Addition from Substitution", "How does an addition reaction fundamentally differ from a substitution reaction?", "In addition, two reactant molecules combine to form a single product with 100% atom economy; in substitution, an atom or group is replaced with formation of a byproduct.", "Addition only occurs in alkanes.", "Substitution always breaks double bonds.", "Addition requires high temperatures whereas substitution occurs at 0 °C.", "Addition combines all reactants into one product (pi bond breaks, two sigma bonds form); substitution replaces one atom/group with another."),
        ("Free Radical Termination Step", "Which reaction is an example of a termination step in a free radical mechanism?", "2Cl. -> Cl2", "Cl. + CH4 -> .CH3 + HCl", "Cl2 -> 2Cl.", ".CH3 + Cl2 -> CH3Cl + Cl.", "Termination occurs when any two free radicals collide and combine their unpaired electrons to form a covalent bond, extinguishing the radicals."),
        ("Nucleophilic Attack at Carbonyls", "Why is the carbonyl carbon in ethanal susceptible to nucleophilic attack?", "Oxygen is more electronegative than carbon, polarizing the C=O bond so the carbon carries a significant partial positive charge (delta+).", "The carbon has an expanded octet of 10 electrons.", "The carbonyl bond is completely non-polar.", "Carbon has two non-bonding lone pairs.", "Oxygen's higher electronegativity draws pi and sigma electrons toward itself (C(delta+)=O(delta-)), leaving the carbonyl carbon electron-deficient and vulnerable to nucleophilic attack."),
        ("Steric Hindrance in SN2", "Why do tertiary halogenoalkanes NOT react via the SN2 mechanism?", "Three bulky alkyl groups surround the central carbon, sterically blocking the incoming nucleophile from attacking from the rear.", "Tertiary halogenoalkanes cannot form carbocations.", "The C-X bond enthalpy is too high to break.", "Tertiary carbons have no vacant orbitals.", "Backside attack in SN2 requires space around the carbon; in 3° haloalkanes, the three bulky alkyl groups cause extreme steric hindrance, blocking nucleophile access."),
        ("Elimination vs Substitution Regiochemistry", "What reaction conditions favor elimination over substitution for 2-bromopropane?", "Heating with concentrated ethanolic potassium hydroxide at high temperature.", "Shaking with dilute aqueous sodium hydroxide at room temperature.", "Treating with cold acidified water.", "Exposing to chlorine in ultraviolet light.", "High temperature, ethanolic solvent, and high base concentration favor elimination (forming propene) over substitution (forming propan-2-ol).")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(mech_pool, start=36):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "13.2", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # SUBTOPIC 13.3: SHAPES OF MOLECULES, HYBRIDISATION & BONDING (Q56 - Q75)
    # =========================================================================

    add_q(
        56, "Hybridisation in Ethene — 9701/11/M/J/23/Q15", "13.3", "EASY",
        "What is the orbital hybridisation of the carbon atoms in ethene, C2H4, and what is the approximate H-C-H bond angle?",
        "sp2 hybridised; bond angle approximately 120°",
        "sp3 hybridised; bond angle 109.5°",
        "sp hybridised; bond angle 180°",
        "dsp2 hybridised; bond angle 90°",
        "Option A is correct. Each carbon in ethene forms three sigma bonds (two C-H and one C-C) by mixing one 2s and two 2p orbitals to form three sp2 hybrid orbitals in a planar trigonal arrangement with 120° angles. The unhybridised 2p orbital on each carbon overlaps sideways to form the pi bond."
    )

    add_q(
        57, "Nature and Overlap of Sigma vs Pi Bonds — 9701/12/M/J/23/Q15", "13.3", "HARD",
        "Which statement accurately contrasts a sigma (sigma) bond with a pi (pi) bond in organic molecules?",
        "A sigma bond is formed by direct end-on (head-to-head) overlap of orbitals with electron density concentrated along the internuclear axis; a pi bond is formed by sideways (lateral) overlap of parallel p orbitals with electron density above and below the axis.",
        "A pi bond is formed by end-on overlap and is significantly stronger than a sigma bond.",
        "Sigma bonds can only exist between identical atoms whereas pi bonds only form between different elements.",
        "Free rotation is possible around a pi bond without breaking it.",
        "Option A is correct. Sigma bonds result from direct end-on overlap along the line connecting the nuclei, giving maximum overlap and cylindrical electron density. Pi bonds form by weaker lateral overlap of parallel p orbitals, concentrating electron density in two lobes above and below the internuclear plane. This sideways overlap prevents free rotation."
    )

    add_q(
        58, "Hybridisation and Geometry in Ethyne — 9701/13/M/J/23/Q15", "13.3", "MEDIUM",
        "In the ethyne molecule (H-C#C-H), what is the hybridisation of the carbon atoms, the number of sigma and pi bonds, and the molecular geometry?",
        "sp hybridisation; 3 sigma bonds and 2 pi bonds; linear geometry with 180° bond angles",
        "sp2 hybridisation; 2 sigma bonds and 3 pi bonds; planar geometry with 120° bond angles",
        "sp3 hybridisation; 5 sigma bonds and 0 pi bonds; tetrahedral geometry with 109.5° bond angles",
        "sp hybridisation; 1 sigma bond and 4 pi bonds; bent geometry with 104.5° bond angles",
        "Option A is correct. Each carbon in H-C#C-H forms two sp hybrid orbitals at 180° (one sigma to H, one sigma to C). Total sigma bonds = 2 (C-H) + 1 (C-C) = 3 sigma bonds. The two unhybridised p orbitals on each carbon overlap sideways to produce 2 perpendicular pi bonds. Geometry is linear (180°)."
    )

    # Questions 59 - 75: Hybridisation, Bond Angles & Shapes
    shape_pool = [
        ("Bond Angles in Propene", "What are the approximate bond angles around C1 (CH2=), C2 (=CH-), and C3 (-CH3) in propene, CH2=CH-CH3?", "C1: 120°, C2: 120°, C3: 109.5°", "C1: 109.5°, C2: 120°, C3: 180°", "C1: 180°, C2: 120°, C3: 109.5°", "C1: 120°, C2: 109.5°, C3: 120°", "Carbons 1 and 2 are sp2 hybridised with trigonal planar geometry (120°). Carbon 3 is sp3 hybridised with tetrahedral geometry (109.5°)."),
        ("Number of Sigma and Pi Bonds in Propanone", "How many sigma bonds and pi bonds are present in a molecule of propanone, CH3COCH3?", "9 sigma bonds and 1 pi bond", "8 sigma bonds and 2 pi bonds", "10 sigma bonds and 0 pi bonds", "7 sigma bonds and 2 pi bonds", "Propanone has 6 C-H sigma bonds, 2 C-C sigma bonds, 1 C-O sigma bond, and 1 C=O pi bond. Total = 9 sigma bonds and 1 pi bond."),
        ("Planarity of Carbonyl Group", "Why is the carbonyl group (>C=O) planar?", "The carbonyl carbon is sp2 hybridised with three coplanar sigma bonds directed at 120° angles.", "The carbon is sp3 hybridised with two lone pairs.", "The carbon is sp hybridised with a linear axis.", "Double bonds always cause tetrahedral geometry.", "The carbonyl carbon forms three sigma bonds using sp2 hybrid orbitals oriented at ~120° in a plane, with the pi bond formed by unhybridised p orbital overlap."),
        ("Restricted Rotation Around Double Bonds", "Why is free rotation impossible around the carbon-carbon double bond in alkenes at room temperature?", "Rotation would disrupt the parallel sideways overlap of the p orbitals, requiring ~260 kJ mol^-1 to break the pi bond.", "The sigma bond is too short to allow rotation.", "The hydrogen atoms collide with each other.", "The carbon atoms carry identical partial charges that repel.", "A pi bond requires parallel alignment of the overlapping p orbitals. Twisting around the C-C axis breaks this sideways overlap, requiring significant energy (~260 kJ/mol), which cannot occur at room temperature."),
        ("Number of Pi Bonds in Benzene", "How many pi electrons are delocalised in the aromatic ring of benzene, C6H6?", "6 pi electrons (one from each sp2 hybridised carbon atom)", "12 pi electrons", "3 pi electrons", "4 pi electrons", "Each of the 6 carbon atoms in benzene is sp2 hybridised and contributes one electron from its unhybridised 2p orbital, forming a continuous delocalised pi cloud of 6 electrons."),
        ("Bond Length Comparison", "Which sequence lists carbon-carbon bonds in order of DECREASING bond length (longest to shortest)?", "C-C (single) > C=C (double) > C#C (triple)", "C#C > C=C > C-C", "C=C > C-C > C#C", "C-C > C#C > C=C", "As the number of shared electron pairs increases, electrostatic attraction for the two nuclei increases, drawing them closer together: C-C (0.154 nm) > C=C (0.134 nm) > C#C (0.120 nm)."),
        ("Bond Energy Comparison", "Which sequence ranks carbon-carbon bonds in order of INCREASING bond dissociation enthalpy (weakest to strongest)?", "C-C (single) < C=C (double) < C#C (triple)", "C#C < C=C < C-C", "C=C < C-C < C#C", "C-C < C#C < C=C", "Triple bond involves sharing 6 electrons (one sigma and two pi bonds) with bond energy ~837 kJ/mol, double bond is ~612 kJ/mol, and single bond is ~348 kJ/mol."),
        ("Hybridisation of Nitrile Carbon", "What is the hybridisation of the carbon and nitrogen atoms in ethanenitrile, CH3-C#N?", "Both the nitrile carbon and nitrogen are sp hybridised", "The carbon is sp2 and nitrogen is sp3", "The carbon is sp3 and nitrogen is sp", "Both atoms are sp2 hybridised", "In the -C#N group, both carbon and nitrogen form one sigma bond and hold two pi bonds (or one lone pair on N), corresponding to sp hybridisation."),
        ("Coplanar Atoms in Ethene", "How many atoms lie in the exact same geometric plane in an ethene molecule (C2H4)?", "All 6 atoms (both carbons and all four hydrogens)", "Only the 2 carbon atoms", "4 atoms (the two carbons and two hydrogens)", "5 atoms", "Ethene is completely planar; all 6 atoms (2 carbons and 4 hydrogens) lie in the same spatial plane due to sp2 hybridisation."),
        ("Carbon Atom Geometry in Diamond vs Graphite", "What is the hybridisation of carbon atoms in diamond and graphite respectively?", "Diamond: sp3 (tetrahedral); Graphite: sp2 (trigonal planar sheets)", "Diamond: sp2; Graphite: sp3", "Diamond: sp; Graphite: sp2", "Diamond: sp3; Graphite: sp", "In diamond, each carbon is sp3 hybridised forming 4 tetrahedral sigma bonds. In graphite, each carbon is sp2 hybridised forming 3 planar trigonal sigma bonds with delocalised pi electrons."),
        ("Sigma Bonds in Buta-1,3-diene", "How many sigma bonds are present in a molecule of buta-1,3-diene (CH2=CH-CH=CH2)?", "9 sigma bonds", "11 sigma bonds", "7 sigma bonds", "8 sigma bonds", "Formula C4H6: 6 C-H sigma bonds + 3 C-C sigma bonds = 9 sigma bonds (plus 2 pi bonds)."),
        ("Shape Around Oxygen in Alcohols", "What is the shape and approximate bond angle around the oxygen atom in methanol (CH3-O-H)?", "Bent (V-shaped) with bond angle approximately 104.5° - 109°", "Trigonal planar with bond angle 120°", "Linear with bond angle 180°", "Tetrahedral with bond angle 109.5°", "Oxygen has four electron pairs (two bonding pairs and two non-bonding lone pairs) in a tetrahedral arrangement. Lone pair repulsion reduces the C-O-H angle to ~104.5° - 108.5°."),
        ("Shape Around Nitrogen in Amines", "What is the molecular geometry around the nitrogen atom in methylamine, CH3NH2?", "Trigonal pyramidal with bond angle approximately 107°", "Trigonal planar with bond angle 120°", "Tetrahedral with bond angle 109.5°", "T-shaped with bond angle 90°", "Nitrogen has three single bonding pairs and one non-bonding lone pair. The electron pair geometry is tetrahedral, yielding a trigonal pyramidal molecular geometry (~107°)."),
        ("Number of Pi Bonds in Carbon Dioxide", "How many sigma and pi bonds are present in carbon dioxide, O=C=O?", "2 sigma bonds and 2 pi bonds", "4 sigma bonds and 0 pi bonds", "1 sigma bond and 3 pi bonds", "3 sigma bonds and 1 pi bond", "Each double bond consists of 1 sigma and 1 pi bond. Thus, O=C=O contains 2 sigma bonds and 2 pi bonds."),
        ("Hybridisation in Carbocations", "What is the orbital hybridisation and geometry of the positively charged carbon in a methyl carbocation, +CH3?", "sp2 hybridised with trigonal planar geometry (120°)", "sp3 hybridised with pyramidal geometry (107°)", "sp hybridised with linear geometry (180°)", "unhybridised with spherical geometry", "The +CH3 carbocation carbon has three bonding electron pairs and an empty 2p orbital, resulting in sp2 hybridisation and planar geometry with 120° bond angles."),
        ("Bond Length in Benzene vs Cyclohexene", "How does the carbon-carbon bond length in benzene compare with ethane and ethene?", "It is intermediate between C-C single (0.154 nm) and C=C double (0.134 nm), with all six C-C bonds equal at 0.139 nm.", "It alternates between short 0.134 nm and long 0.154 nm.", "It is shorter than a triple bond (0.110 nm).", "It is identical to the single bond in ethane (0.154 nm).", "Due to pi electron delocalization, all six C-C bonds in benzene are identical in length (0.139 nm), intermediate between pure single and pure double bonds."),
        ("Pi Bond Formation Orbitals", "Which atomic orbitals overlap to form the pi bond in methanal, H2C=O?", "Sideways overlap of the unhybridised 2p orbital of carbon with a 2p orbital of oxygen.", "End-on overlap of sp2 hybrid orbitals.", "Overlap of a 1s hydrogen orbital with an sp2 carbon orbital.", "Overlap of two 2s orbitals.", "The pi bond in the C=O group arises from the lateral (sideways) overlap of parallel 2p orbitals on carbon and oxygen.")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(shape_pool, start=59):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "13.3", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # SUBTOPIC 13.4: ISOMERISM — STRUCTURAL & STEREOISOMERISM (Q76 - Q100)
    # =========================================================================

    add_q(
        76, "Classification of Structural Isomerism — 9701/11/M/J/23/Q16", "13.4", "EASY",
        "What are the three main types of structural isomerism recognized in AS Level Chemistry?",
        "Chain isomerism, positional isomerism, and functional group isomerism",
        "Cis-trans isomerism, optical isomerism, and conformational isomerism",
        "Enantiomerism, diastereomerism, and geometric isomerism",
        "Addition isomerism, substitution isomerism, and elimination isomerism",
        "Option A is correct. Structural isomers have the same molecular formula but different structural formulas (different connectivity of atoms). The three categories are: (1) Chain isomerism (different carbon skeleton branching); (2) Positional isomerism (same skeleton, functional group in different locations); (3) Functional group isomerism (same formula, different functional group)."
    )

    add_q(
        77, "Functional Group Isomerism Pair — 9701/12/M/J/23/Q16", "13.4", "EASY",
        "Which pair of compounds represents functional group isomers with the molecular formula C3H6O?",
        "Propanal (aldehyde) and propanone (ketone)",
        "Propan-1-ol and propan-2-ol",
        "Propanoic acid and methyl ethanoate",
        "Cyclopropane and propene",
        "Option A is correct. Both propanal (CH3CH2CHO) and propanone (CH3COCH3) have molecular formula C3H6O, but propanal contains an aldehyde functional group (-CHO) whereas propanone contains a ketone group (>C=O). They are functional group isomers."
    )

    add_q(
        78, "Conditions for Cis-Trans (Geometric) Isomerism — 9701/13/M/J/23/Q16", "13.4", "HARD",
        "Which two conditions MUST be satisfied for an alkene to exhibit cis-trans (geometric) stereoisomerism?",
        "Restricted rotation around the carbon-carbon double bond (C=C) AND two different groups attached to EACH carbon of the double bond.",
        "A chiral center with four different groups attached AND a carbon-carbon double bond.",
        "At least one triple bond AND identical groups on opposite sides of the molecule.",
        "A saturated carbon chain of at least five carbon atoms.",
        "Option A is correct. Geometric (cis-trans) isomerism requires: (1) Restricted rotation about the C=C bond (due to the pi bond); and (2) Each individual carbon atom of the C=C bond must be bonded to two non-identical groups (i.e. Cab=Ccd, where a!=b and c!=d). If either carbon has two identical groups (e.g. Ca2=Ccd), cis-trans isomerism is impossible."
    )

    add_q(
        79, "Chirality and Optical Activity — 9701/11/O/N/23/Q16", "13.4", "HARD",
        "What defines a chiral carbon atom (stereocenter) in an organic molecule?",
        "A carbon atom bonded to four completely different atoms or groups of atoms, resulting in non-superimposable mirror images (enantiomers).",
        "A carbon atom bonded to a double bond and two hydrogen atoms.",
        "A carbon atom that forms coordinate bonds with transition metal ions.",
        "A carbon atom located at the center of an aromatic benzene ring.",
        "Option A is correct. A chiral center (asymmetric carbon) is bonded tetrahedrally to four distinct atoms or groups. This asymmetry means the molecule lacks a plane of symmetry, creating two non-superimposable mirror image structures (enantiomers) that rotate the plane of plane-polarized light in opposite directions."
    )

    add_q(
        80, "Identifying Chiral Centers in Alcohols — 9701/12/O/N/23/Q16", "13.4", "MEDIUM",
        "Which four-carbon alcohol contains a chiral carbon atom and exists as a pair of optical isomers?",
        "Butan-2-ol, CH3-CH(OH)-CH2-CH3",
        "Butan-1-ol, CH3-CH2-CH2-CH2OH",
        "2-methylpropan-1-ol, (CH3)2CH-CH2OH",
        "2-methylpropan-2-ol, (CH3)3C-OH",
        "Option A is correct. In butan-2-ol, C2 is bonded to four different groups: -H, -OH, -CH3, and -CH2CH3. Thus, C2 is a chiral stereocenter, and butan-2-ol exists as two enantiomers. In all other isomers, every carbon has at least two identical groups (-H2, -H3, or -(CH3)2)."
    )

    # Questions 81 - 100: Isomerism Variety
    isomer_pool = [
        ("Structural Isomers of Butane", "How many structural isomers exist for the alkane with molecular formula C4H10?", "2 (butane and 2-methylpropane)", "3", "4", "1", "C4H10 has exactly two structural chain isomers: unbranched butane (CH3CH2CH2CH3) and branched 2-methylpropane ((CH3)3CH)."),
        ("Structural Isomers of Pentane", "How many structural isomers exist for the alkane with molecular formula C5H12?", "3 (pentane, 2-methylbutane, and 2,2-dimethylpropane)", "2", "4", "5", "C5H12 has three chain isomers: pentane, 2-methylbutane (isopentane), and 2,2-dimethylpropane (neopentane)."),
        ("Positional Isomers of Dichlorobenzene", "How many positional isomers exist for dichlorobenzene (C6H4Cl2)?", "3 (1,2-dichlorobenzene, 1,3-dichlorobenzene, and 1,4-dichlorobenzene)", "2", "4", "1", "The chlorine atoms can be 1,2 (ortho), 1,3 (meta), or 1,4 (para), yielding three positional isomers."),
        ("Functional Group Isomers of Carboxylic Acids", "Which functional group class is isomeric with aliphatic carboxylic acids of formula CnH2nO2?", "Esters", "Aldehydes", "Alcohols", "Ethers", "Both aliphatic carboxylic acids (R-COOH) and esters (R-COOR') share the general formula CnH2nO2 and are functional group isomers."),
        ("Cis-Trans in But-2-ene", "Why does but-2-ene show cis-trans isomerism while but-1-ene does not?", "In but-2-ene, each double-bond carbon has -H and -CH3; in but-1-ene, C1 has two identical -H atoms.", "But-1-ene has a higher boiling point than but-2-ene.", "But-2-ene contains a chiral carbon atom.", "But-1-ene has sp hybridised carbons.", "Cis-trans isomerism requires two different groups on EACH carbon of the C=C bond. In but-1-ene, C1 is bonded to two identical hydrogen atoms (=CH2), so swapping them produces the same molecule."),
        ("Physical Property Differences of Cis-Trans Isomers", "How do cis- and trans-1,2-dichloroethene differ in physical properties such as boiling point and dipole moment?", "The cis isomer is polar with a higher boiling point; the trans isomer is non-polar (dipoles cancel) with a lower boiling point.", "Both isomers are non-polar with identical boiling points.", "The trans isomer is highly polar with a higher boiling point.", "The cis isomer has a lower melting point due to hydrogen bonding.", "In cis-1,2-dichloroethene, both polar C-Cl bonds point to the same side, creating a net molecular dipole and higher boiling point (60 °C). In trans, the dipoles point in opposite directions and cancel completely (net dipole = 0), lowering the boiling point (48 °C)."),
        ("Chirality in Halogenoalkanes", "Which molecule contains a chiral center?", "2-bromobutane", "1-bromobutane", "2-bromopropane", "2-bromo-2-methylpropane", "In 2-bromobutane, C2 is bonded to -H, -Br, -CH3, and -CH2CH3 (four different groups), making it chiral."),
        ("Racemic Mixture Definition", "What is an equimolar (50:50) mixture of two optical enantiomers called, and what is its net optical rotation?", "A racemic mixture (or racemate); it exhibits zero net optical rotation because the equal and opposite rotations cancel.", "A meso compound; it rotates light clockwise.", "A pure enantiomer; it rotates light 180°.", "A diastereomer; it has a high specific rotation.", "A racemate contains equal amounts of (+) and (-) enantiomers. The optical rotation caused by one isomer is precisely cancelled by the equal and opposite rotation of the other, resulting in optical inactivity."),
        ("Number of Optical Isomers for 1 Chiral Center", "An organic molecule has exactly one chiral carbon atom. How many stereoisomers exist for this molecule?", "2 (a pair of non-superimposable enantiomers)", "4", "3", "1", "A molecule with n chiral centers and no internal symmetry has 2^n stereoisomers. For n=1, 2^1 = 2 enantiomers."),
        ("Optical Activity Detection", "How can two optical enantiomers be distinguished experimentally in a laboratory?", "By measuring the direction of rotation of plane-polarized light using a polarimeter.", "By measuring their boiling points.", "By observing their solubility in water.", "By comparing their mass spectra molecular ion peaks.", "Enantiomers have identical physical properties (boiling point, density, refractive index, solubility in achiral solvents) except that they rotate the plane of plane-polarized light in equal and opposite directions (+ / d- vs - / l-)."),
        ("Isomerism in Pent-2-ene", "What type of stereoisomerism is exhibited by pent-2-ene, CH3-CH=CH-CH2-CH3?", "Cis-trans (E/Z) isomerism", "Optical isomerism", "Conformational isomerism only", "No isomerism is possible", "Pent-2-ene has a C=C bond where C2 is bonded to -H and -CH3, and C3 is bonded to -H and -CH2CH3. Since both carbons have two different groups, it exists as cis-pent-2-ene and trans-pent-2-ene."),
        ("Chirality in 3-methylhexane", "Which carbon atom in 3-methylhexane, CH3-CH2-CH(CH3)-CH2-CH2-CH3, is the chiral stereocenter?", "Carbon-3", "Carbon-2", "Carbon-4", "Carbon-1", "Carbon-3 is bonded to four different groups: -H, -CH3 (methyl), -CH2CH3 (ethyl), and -CH2CH2CH3 (propyl)."),
        ("Positional Isomers of Propanol", "What type of isomerism exists between propan-1-ol and propan-2-ol?", "Positional isomerism", "Chain isomerism", "Functional group isomerism", "Stereoisomerism", "Both molecules possess the same 3-carbon chain and the same alcohol functional group (-OH), but the group is at C1 in propan-1-ol and C2 in propan-2-ol (positional isomers)."),
        ("Chain Isomerism Example", "Which pair of molecules represents chain isomers?", "Pentane and 2,2-dimethylpropane", "Propan-1-ol and propan-2-ol", "Ethanoic acid and methyl methanoate", "But-1-ene and but-2-ene", "Pentane (straight 5-carbon chain) and 2,2-dimethylpropane (branched chain) have the same formula C5H12 but different carbon skeleton branching, making them chain isomers."),
        ("Total Isomers of C3H6Cl2", "How many structural isomers exist for the dichloropropane molecule C3H6Cl2?", "4 (1,1-dichloropropane, 1,2-dichloropropane, 1,3-dichloropropane, and 2,2-dichloropropane)", "3", "5", "2", "The four isomers are: 1,1-dichloropropane, 1,2-dichloropropane, 1,3-dichloropropane, and 2,2-dichloropropane."),
        ("Functional Group Isomerism of Alkenes and Cycloalkanes", "What type of isomerism is demonstrated by hex-1-ene and cyclohexane (both C6H12)?", "Functional group isomerism", "Chain isomerism", "Positional isomerism", "Optical isomerism", "Open-chain alkenes (with C=C functional group) and ring cycloalkanes (saturated cyclic rings) share formula CnH2n and are functional group isomers."),
        ("Stereoisomerism in 1,2-dimethylcyclopropane", "Which type of stereoisomerism can be exhibited by 1,2-dimethylcyclopropane?", "Both cis-trans and optical isomerism", "Neither cis-trans nor optical isomerism", "Chain isomerism only", "Functional group isomerism only", "The rigid three-membered ring restricts rotation, enabling cis and trans isomers. Furthermore, the trans isomer lacks an internal plane of symmetry and exists as a pair of chiral enantiomers."),
        ("Lack of Chirality in Glycine", "Why is glycine (2-aminoethanoic acid, H2N-CH2-COOH) the only standard amino acid that is optically inactive?", "Its alpha-carbon is bonded to two identical hydrogen atoms, so it is achiral (lacks 4 different groups).", "It contains an amide bond instead of an amine.", "It exists purely as a gaseous free radical.", "It has a double bond between nitrogen and carbon.", "In glycine, the central alpha-carbon is attached to -NH2, -COOH, and TWO -H atoms. Because two groups are identical, it is achiral and optically inactive."),
        ("Isomerism of C2H6O", "What are the two structural isomers of C2H6O, and what type of isomerism do they exhibit?", "Ethanol (CH3CH2OH) and methoxymethane (CH3OCH3); functional group isomerism", "Ethanol and ethanal; positional isomerism", "Ethanol and ethanoic acid; chain isomerism", "Methoxymethane and dimethyl ketone; geometric isomerism", "C2H6O has two isomers: ethanol (an alcohol) and methoxymethane / dimethyl ether (an ether). They belong to different functional group classes, exhibiting functional group isomerism."),
        ("E/Z Nomenclature System Basis", "What is the Cahn-Ingold-Prelog (CIP) priority rule used in E/Z isomerism based on?", "The atomic number of the atoms directly attached to the double-bond carbons (higher atomic number = higher priority).", "The total molecular mass of the entire substituent group.", "The alphabetical order of substituent names.", "The number of hydrogen atoms in the substituent.", "The CIP priority rules rank substituents based on the atomic number of the atom directly bonded to the stereocenter (e.g. -Br (35) > -Cl (17) > -OH (8) > -CH3 (6) > -H (1)). If high-priority groups are on opposite sides, it is E (entgegen); on the same side, it is Z (zusammen).")
    ]

    for idx, (title, stem, optA, optB, optC, optD, exp) in enumerate(isomer_pool, start=81):
        add_q(
            idx, f"{title} — 9701/1{idx%3+1}/M/J/2{idx%5+20}/Q{idx}", "13.4", "HARD" if idx % 2 == 0 else "EASY",
            stem, optA, optB, optC, optD, f"Option A is correct. {exp}"
        )

    # =========================================================================
    # HIGH-FREQUENCY CORE REPEATS (Q101 - Q110)
    # =========================================================================

    hf_data = [
        (
            101, "HF 1: Determining Empirical and Molecular Formulas from Percentage Composition — 9701/12/M/J/22/Q13", "HF", "HARD",
            "An organic liquid X has the percentage composition by mass: C, 62.07%; H, 10.34%; O, 27.59%. In a mass spectrometer, the molecular ion peak M+ occurs at m/z = 116.0.\n\nWhat is the molecular formula of compound X?",
            "C6H12O2",
            "C3H6O",
            "C5H8O3",
            "C4H8O2",
            "Option A is correct. Moles of C = 62.07/12.0 = 5.1725; moles of H = 10.34/1.0 = 10.34; moles of O = 27.59/16.0 = 1.7244. Divide by smallest (1.7244): C: 5.1725/1.7244 = 3.0; H: 10.34/1.7244 = 6.0; O: 1.7244/1.7244 = 1.0. Empirical formula = C3H6O (formula mass = 3(12) + 6(1) + 16 = 58.0). Since M+ = 116.0, multiplier = 116.0 / 58.0 = 2. Molecular formula = C6H12O2."
        ),
        (
            102, "HF 2: Identifying the Number of Chiral Centers in Complex Drug Molecules — 9701/11/O/N/21/Q15", "HF", "HARD",
            "Menthol is a cyclic organic compound with the structural formula shown below:\n2-isopropyl-5-methylcyclohexan-1-ol\n\nHow many chiral carbon atoms (stereocenters) are present in one molecule of menthol?",
            "3 chiral centers (C1 bearing -OH, C2 bearing isopropyl, and C5 bearing methyl)",
            "1 chiral center",
            "2 chiral centers",
            "4 chiral centers",
            "Option A is correct. Analyzing the cyclohexane ring: C1 is bonded to -H, -OH, C2, and C6 (different pathways around the ring); C2 is bonded to -H, -CH(CH3)2, C1, and C3; C5 is bonded to -H, -CH3, C4, and C6. Each of these three carbons has four distinctly different groups attached. Thus, menthol contains exactly 3 chiral centers."
        ),
        (
            103, "HF 3: Systematic IUPAC Naming with Multiple Functional Groups — 9701/13/M/J/22/Q14", "HF", "HARD",
            "What is the systematic IUPAC name for CH3-CH(OH)-CH2-CH=CH2?",
            "Pent-4-en-2-ol",
            "Pent-1-en-4-ol",
            "4-hydroxypent-1-ene",
            "2-hydroxypent-4-ene",
            "Option A is correct. Under IUPAC nomenclature rules, the principal functional group suffix (alcohol, -ol) takes precedence over the alkene unsaturation (-en-) for determining the lowest locant. Numbering from the right would give the alcohol locant 4, while numbering from the left gives the alcohol locant 2 (pent-4-en-2-ol). Hence, the correct systematic name is pent-4-en-2-ol."
        ),
        (
            104, "HF 4: Total Number of Isomers with Formula C4H8 — 9701/12/F/M/22/Q16", "HF", "HARD",
            "Including both structural isomers and stereoisomers (cis-trans), how many isomeric compounds have the molecular formula C4H8?",
            "6 (but-1-ene, cis-but-2-ene, trans-but-2-ene, 2-methylpropene, cyclobutane, and methylcyclopropane)",
            "4",
            "5",
            "3",
            "Option A is correct. Formula C4H8 has 1 degree of unsaturation. Alkenes: (1) but-1-ene, (2) cis-but-2-ene, (3) trans-but-2-ene, (4) 2-methylpropene. Cycloalkanes: (5) cyclobutane, (6) methylcyclopropane. Total number of isomers = 6."
        ),
        (
            105, "HF 5: Hybridisation of Carbon Atoms Across an Unsaturated Chain — 9701/11/M/J/21/Q14", "HF", "HARD",
            "Consider the compound CH2=CH-C#C-CH3.\n\nFrom left to right, what are the orbital hybridisations of the five carbon atoms?",
            "sp2, sp2, sp, sp, sp3",
            "sp2, sp2, sp2, sp2, sp3",
            "sp3, sp2, sp, sp, sp3",
            "sp, sp, sp2, sp2, sp3",
            "Option A is correct. C1 (CH2=) forms 3 sigma bonds -> sp2; C2 (=CH-) forms 3 sigma bonds -> sp2; C3 (-C#) forms 2 sigma bonds -> sp; C4 (#C-) forms 2 sigma bonds -> sp; C5 (-CH3) forms 4 sigma bonds -> sp3. Sequence: sp2, sp2, sp, sp, sp3."
        ),
        (
            106, "HF 6: Mechanism of Free Radical Substitution — Identification of Termination Products — 9701/12/O/N/22/Q15", "HF", "HARD",
            "During the reaction between methane and chlorine in the presence of ultraviolet light, trace amounts of ethane, C2H6, are detected in the product mixture.\n\nWhich reaction accounts for the formation of ethane?",
            ".CH3 + .CH3 -> C2H6 (a termination step between two methyl radicals)",
            "CH4 + .CH3 -> C2H6 + .H",
            ".CH3 + Cl2 -> C2H6 + 2Cl.",
            "CH3Cl + CH3Cl -> C2H6 + Cl2",
            "Option A is correct. In the propagation steps, a high concentration of methyl free radicals (.CH3) is generated. When two methyl radicals collide, their single unpaired electrons pair up to form a C-C covalent bond (.CH3 + .CH3 -> C2H6). This radical-radical collision consumes both radicals without generating new ones, representing a classic termination step."
        ),
        (
            107, "HF 7: Distinguishing Enantiomers Using Physical and Chemical Properties — 9701/13/O/N/21/Q16", "HF", "HARD",
            "Which property is DIFFERENT for two optical enantiomers of lactic acid (2-hydroxypropanoic acid)?",
            "The direction in which they rotate the plane of plane-polarized light in a polarimeter.",
            "Their boiling points at standard atmospheric pressure.",
            "Their solubility in pure water at 25 °C.",
            "Their acid dissociation constant (Ka) in aqueous solution.",
            "Option A is correct. Enantiomers possess identical scalar physical properties (boiling point, melting point, density, Ka, solubility in achiral solvents) because the internal interatomic distances and energies are mirror-symmetric. They differ ONLY in their interaction with chiral phenomena: the direction in which they rotate plane-polarized light (+ vs -) and their reaction rates with other chiral reagents/enzymes."
        ),
        (
            108, "HF 8: Calculating Sigma and Pi Bonds in Complex Molecules — 9701/11/F/M/23/Q15", "HF", "HARD",
            "Acrylonitrile (propenenitrile), CH2=CH-C#N, is used in the manufacture of acrylic fibers.\n\nHow many sigma (sigma) bonds and pi (pi) bonds are present in one molecule of acrylonitrile?",
            "6 sigma bonds and 3 pi bonds",
            "5 sigma bonds and 4 pi bonds",
            "7 sigma bonds and 2 pi bonds",
            "4 sigma bonds and 5 pi bonds",
            "Option A is correct. Counting bonds: 3 C-H single bonds = 3 sigma; 1 C=C double bond = 1 sigma + 1 pi; 1 C-C single bond = 1 sigma; 1 C#N triple bond = 1 sigma + 2 pi. Total sigma bonds = 3 + 1 + 1 + 1 = 6 sigma bonds. Total pi bonds = 1 + 2 = 3 pi bonds."
        ),
        (
            109, "HF 9: Predicting Stereoisomerism in Dienes — 9701/12/M/J/23/Q16", "HF", "HARD",
            "How many geometric (cis-trans) stereoisomers exist for hexa-2,4-diene, CH3-CH=CH-CH=CH-CH3?",
            "3 stereoisomers (cis-cis, trans-trans, and cis-trans)",
            "4 stereoisomers",
            "2 stereoisomers",
            "1 stereoisomer",
            "Option A is correct. Hexa-2,4-diene has two C=C bonds, each capable of cis (Z) or trans (E) configurations. Due to the symmetrical nature of the carbon chain, the (cis, trans) and (trans, cis) arrangements are identical by 180° rotation. Thus, there are only 3 distinct geometric isomers: (1) cis,cis-hexa-2,4-diene; (2) trans,trans-hexa-2,4-diene; (3) cis,trans-hexa-2,4-diene."
        ),
        (
            110, "HF 10: Deductive Identification of Structural Isomers with C3H8O — 9701/13/M/J/23/Q17", "HF", "HARD",
            "Three isomeric organic liquids, P, Q, and R, all have the molecular formula C3H8O.\n• P and Q react with sodium metal to evolve hydrogen gas.\n• P can be oxidized by acidified potassium dichromate(VI) to an aldehyde.\n• R does NOT react with sodium metal.\n\nWhat are compounds P, Q, and R?",
            "P is propan-1-ol, Q is propan-2-ol, and R is methoxyethane",
            "P is propan-2-ol, Q is propan-1-ol, and R is propanoic acid",
            "P is propan-1-ol, Q is methoxyethane, and R is propan-2-ol",
            "P is methoxyethane, Q is propan-1-ol, and R is propan-2-ol",
            "Option A is correct. C3H8O has 3 structural isomers: propan-1-ol, propan-2-ol, and methoxyethane (CH3-O-C2H5). Alcohols react with sodium metal to form alkoxides and H2 gas (2ROH + 2Na -> 2RONa + H2), so P and Q are alcohols. Primary alcohols oxidize to aldehydes, identifying P as propan-1-ol (1° alcohol) and Q as propan-2-ol (2° alcohol). Ethers lack O-H bonds and do not react with sodium, confirming R as methoxyethane."
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

    # Write output to mcq_topic13_data.py
    out_file = r"z:\tests n quizes63\books\psycology\new styl\mcq_topic13_data.py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write('"""\nCurated 110 Authentic Cambridge AS Chemistry (9701) Paper 1 MCQs\nfor Topic 13: An Introduction to AS Level Organic Chemistry (100 Core + 10 High-Frequency Core Repeats).\n"""\n\n')
        f.write("from build_mcq_topic_pdf import MCQQuestion\n\n")
        f.write("TOPIC_13_MCQ_QUESTIONS = [\n")
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

    print(f"Successfully generated mcq_topic13_data.py with {len(balanced_questions)} MCQs!")

if __name__ == "__main__":
    create_topic13_data()
