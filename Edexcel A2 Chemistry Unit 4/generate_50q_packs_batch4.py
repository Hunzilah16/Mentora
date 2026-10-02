import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

def make_edexcel_q(number, title, ref, marks, stem, parts, mark_scheme):
    return {
        'title': f"{number}. {title}",
        'ref': ref,
        'marks': marks,
        'stem': stem,
        'parts': parts,
        'mark_scheme': mark_scheme
    }

def make_edexcel_faq(title, category, trap, model_ans):
    return {
        'title': title,
        'category': category,
        'examiner_trap': trap,
        'model_answer': model_ans
    }

# ==========================================
# PACK 7: 15A — CHIRALITY (50 Qs + 10 FAQs)
# ==========================================
p7_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
    'subtopic_code': '15A',
    'subtopic_name': 'Chirality, Optical Activity & Reaction Stereochemistry'
}

p7_questions = []

p7_questions.append(make_edexcel_q(
    1, "Chiral Centre Identification", "WCH14/01/Jan23/Q15", 3,
    "Lactic acid, 2-hydroxypropanoic acid, CH3CH(OH)COOH, is found in sour milk.",
    [
        {'label': 'a', 'text': 'Draw the structural formula of 2-hydroxypropanoic acid and circle the chiral carbon atom.', 'marks': 1},
        {'label': 'b', 'text': 'Draw 3D wedge-and-dash diagrams for the two enantiomers of 2-hydroxypropanoic acid.', 'marks': 2}
    ],
    "1. (a) C2 circled (attached to -H, -OH, -CH3, -COOH) (1).<br/>1. (b) Tetrahedral 3D drawings showing non-superimposable mirror images (2)."
))

p7_questions.append(make_edexcel_q(
    2, "Polarimetry and Racemic Mixtures", "WCH14/01/Oct22/Q16", 4,
    "A sample of 2-chlorobutane was synthesized in a laboratory.",
    [
        {'label': 'a', 'text': 'Describe how a polarimeter can be used to show that a sample of 2-chlorobutane is optically active.', 'marks': 2},
        {'label': 'b', 'text': 'Explain why a sample of 2-chlorobutane prepared by reacting but-2-ene with HCl is optically inactive.', 'marks': 2}
    ],
    "2. (a) Pass plane-polarised light through the sample (1); optically active sample rotates the plane of polarisation (1).<br/>2. (b) Electrophilic addition involves a planar carbocation intermediate (1); H+ / Cl- can attack from top or bottom of the plane with equal probability, forming a 50:50 racemic mixture (1)."
))

for i in range(3, 26):
    p7_questions.append(make_edexcel_q(
        i, f"Chirality & Enantiomer Property Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider organic molecule {i} with a single chiral centre.",
        [
            {'label': 'a', 'text': 'State two physical properties that are identical for both enantiomers.', 'marks': 2},
            {'label': 'b', 'text': 'State one property in which the two enantiomers differ.', 'marks': 1}
        ],
        f"{i}. (a) Melting point, boiling point, density, solubility in achiral solvents (any 2) (2).<br/>{i}. (b) Rotation of plane-polarised light (opposite directions) / biological reaction with chiral enzymes (1)."
    ))

for i in range(26, 51):
    p7_questions.append(make_edexcel_q(
        i, f"A* Challenge: SN1 vs SN2 Stereochemical Outcomes {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"Hydrolysis of optically active (R)-2-bromobutane with aqueous NaOH yields a mixture of products.",
        [
            {'label': 'a', 'text': 'Explain why an SN1 mechanism leads to a racemic mixture (loss of optical activity).', 'marks': 3},
            {'label': 'b', 'text': 'Explain why an SN2 mechanism leads to complete inversion of optical configuration (Walden inversion).', 'marks': 2}
        ],
        f"{i}. (a) SN1 forms a trigonal planar carbocation intermediate (1). Nucleophile OH- attacks from top or bottom face with 50:50 probability (1) producing equal amounts of (R) and (S) enantiomers -> racemate (1).<br/>{i}. (b) SN2 is a single-step concerted reaction with backside attack of OH- opposite the Br leaving group (1), causing inversion of configuration (1)."
    ))

p7_faqs = []
p7_faq_titles = [
    ("Identifying Chiral Carbons in Rings", "Ring Chirality", "Overlooking chiral carbons inside saturated ring systems.", "Check carbons in rings: if the two pathways around the ring from that carbon are DIFFERENT, the attached ring paths count as two distinct groups! E.g. 3-methylcyclohexanol has 2 chiral carbons."),
    ("Symmetry Plane in Molecules", "Mesocompounds", "Assuming any molecule with 2 chiral carbons MUST be optically active.", "If a molecule contains a plane of internal symmetry (meso form), it is achiral and optically inactive despite having 2 chiral centers."),
    ("SN1 vs SN2 Stereochemical Distinction", "Mechanism Evidence", "Swapping SN1 and SN2 stereochemical products.", "SN1 -> planar carbocation -> 50:50 attack -> RACEMIC MIXTURE (optically inactive). SN2 -> backside attack -> INVERSION -> single optically active enantiomer."),
    ("Physical Properties of Enantiomers", "Enantiomer Properties", "Claiming enantiomers have different boiling points.", "Enantiomers have IDENTICAL physical properties (b.p., m.p., density, solubility in achiral solvents). They ONLY differ in direction of rotation of plane-polarised light."),
    ("Enzymatic Reactivity of Enantiomers", "Biological Action", "Expecting both enantiomers to have equal pharmaceutical activity.", "Enzymes and biological receptors are CHIRAL (lock-and-key). Usually only ONE enantiomer fits the active site (e.g. Thalidomide, Ibuprofen)."),
    ("Racemate Optical Rotation", "Racemic Mixture", "Writing that a racemate rotates light by 0.5 degrees.", "A racemic mixture contains EQUAL MOLES of (+) and (-) enantiomers. The opposite rotations cancel out completely -> 0.0° optical rotation."),
    ("Drawing 3D Enantiomers", "3D Projection", "Drawing mirror images that are superimposable.", "Use wedge (pointing out), dash (pointing in), and two solid lines (in page plane). Ensure the mirror image is non-superimposable upon 180° rotation."),
    ("Electrophilic Addition to Alkenes Stereochemistry", "Alkene Addition", "Expecting alkene addition to yield a single optically active enantiomer.", "Planar C=C double bond allows attack from top or bottom with equal probability -> ALWAYS forms a racemic mixture if a chiral center is created."),
    ("Nucleophilic Addition to Carbonyls Stereochemistry", "Carbonyl Addition", "Assuming HCN addition to aldehydes gives optically active product.", "Planar C=O carbonyl group is attacked by CN- from top or bottom with equal probability -> yields a RACEMIC mixture of hydroxynitrile."),
    ("Polarimeter Source Light", "Experimental Setup", "Using unpolarised white light in a polarimeter.", "A polarimeter MUST use PLANE-POLARISED light (produced using a Nicol prism / polarising filter). Unpolarised light contains waves vibrating in all planes.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p7_faq_titles, 1):
    p7_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_15A_Chirality.pdf", p7_meta, p7_questions, p7_faqs)
print("Pack 7 (15A Chirality - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 8: 15B — CARBONYL COMPOUNDS (50 Qs + 10 FAQs)
# ==========================================
p8_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
    'subtopic_code': '15B',
    'subtopic_name': 'Carbonyl Compounds (Aldehydes, Ketones, Redox & Nucleophilic Addition)'
}

p8_questions = []

p8_questions.append(make_edexcel_q(
    1, "Distinguishing Aldehydes and Ketones", "WCH14/01/Jan23/Q17", 5,
    "Propanal (CH3CH2CHO) and propanone (CH3COCH3) are structural isomers.",
    [
        {'label': 'a', 'text': 'Describe the observation when propanal is warmed with Tollens reagent [Ag(NH3)2]+.', 'marks': 2},
        {'label': 'b', 'text': 'Describe the observation when propanal is warmed with Fehling solution.', 'marks': 2},
        {'label': 'c', 'text': 'State why propanone gives no reaction with Tollens reagent or Fehling solution.', 'marks': 1}
    ],
    "1. (a) Silver mirror / grey precipitate forms (2).<br/>1. (b) Blue solution forms a brick-red precipitate of Cu2O (2).<br/>1. (c) Propanone is a ketone and cannot be easily oxidized without breaking C-C bonds (1)."
))

p8_questions.append(make_edexcel_q(
    2, "Nucleophilic Addition Mechanism of HCN", "WCH14/01/Oct22/Q18", 5,
    "Ethanal reacts with HCN in the presence of KCN catalyst to form 2-hydroxypropanenitrile.",
    [
        {'label': 'a', 'text': 'Draw the mechanism for this nucleophilic addition reaction, showing all dipoles, lone pairs, and curly arrows.', 'marks': 4},
        {'label': 'b', 'text': 'Explain why KCN is added as a catalyst.', 'marks': 1}
    ],
    "2. (a) Nucleophilic attack by :CN- lone pair on delta+ C of C=O bond (1). Arrow from C=O bond onto O (1). Intermediate CH3CH(O-)CN formed (1). Protonation of O- by H+ / HCN to form -OH (1).<br/>2. (b) KCN dissociates fully to provide a high concentration of CN- nucleophiles (HCN is a weak acid) (1)."
))

for i in range(3, 26):
    p8_questions.append(make_edexcel_q(
        i, f"Carbonyl Reaction & Test Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider carbonyl compound {i} reacting with 2,4-dinitrophenylhydrazine (2,4-DNPH) and iodine/NaOH (iodoform test).",
        [
            {'label': 'a', 'text': 'State the observation when 2,4-DNPH is added.', 'marks': 1},
            {'label': 'b', 'text': 'State the observation in the iodoform test if the compound contains a CH3C=O group.', 'marks': 2}
        ],
        f"{i}. (a) Bright orange / yellow precipitate (1).<br/>{i}. (b) Pale yellow precipitate of tri-iodomethane (CHI3) (1) with an antiseptic smell (1)."
    ))

for i in range(26, 51):
    p8_questions.append(make_edexcel_q(
        i, f"A* Challenge: Carbonyl Reduction & Multi-Step Identification {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"An unknown carbonyl compound Z (C4H8O) gives an orange precipitate with 2,4-DNPH and a yellow precipitate with I2/NaOH.<br/>Z is reduced by NaBH4 to form alcohol W.",
        [
            {'label': 'a', 'text': 'Deduce the structural formula of Z and alcohol W.', 'marks': 3},
            {'label': 'b', 'text': 'Write the equation for the reduction of Z using NaBH4 (represented by [H]).', 'marks': 2}
        ],
        f"{i}. (a) Z gives iodoform test -> contains CH3C=O. Z is a C4 ketone -> butanone, CH3COCH2CH3 (2). W = butan-2-ol, CH3CH(OH)CH2CH3 (1).<br/>{i}. (b) CH3COCH2CH3 + 2[H] -> CH3CH(OH)CH2CH3 (2)."
    ))

p8_faqs = []
p8_faq_titles = [
    ("Tollens Reagent Preparation and Hazard", "Tollens Test", "Heating Tollens reagent strongly or storing it.", "Tollens reagent [Ag(NH3)2]+ must be freshly prepared by adding dilute NH3 to AgNO3 until Ag2O ppt redissolves. Never heat strongly or store (forms explosive silver fulminate)."),
    ("Fehling Solution Color Change", "Fehling Test", "Writing 'solution turns red' instead of precipitate.", "Fehling solution starts BLUE. Upon warming with an aldehyde, a BRICK-RED PRECIPITATE of copper(I) oxide (Cu2O) forms."),
    ("Role of KCN in HCN Addition", "Nucleophilic Addition", "Omitting KCN and claiming HCN alone is sufficient.", "HCN is a weak acid with negligible dissociation. KCN is added to supply CN- nucleophiles to initiate the attack on the carbonyl carbon."),
    ("2,4-DNPH Derivative Purification", "Qualitative Analysis", "Stating 2,4-DNPH identifies the specific aldehyde/ketone by color.", "2,4-DNPH gives an orange ppt for ALL aldehydes and ketones. To identify the specific compound: filter, purify by recrystallisation, measure its sharp MELTING POINT, and compare with data tables."),
    ("Iodoform Test Positive Structures", "Tri-iodomethane Test", "Assuming ONLY methyl ketones give a positive iodoform test.", "Iodoform test (I2 + NaOH) is positive for: (1) Methyl ketones CH3C=O, (2) Ethanal CH3CHO, (3) Secondary methyl alcohols CH3CH(OH)R, and (4) Ethanol CH3CH2OH (oxidized in situ to ethanal)."),
    ("LiAlH4 vs NaBH4 Reducing Agents", "Reduction Reagents", "Using NaBH4 in dry ether or LiAlH4 in water.", "LiAlH4 is a stronger reducing agent reacting violently with water -> MUST be used in DRY ETHER. NaBH4 is milder and safe in AQUEOUS ETHANOL solvent."),
    ("Reduction Product Class", "Reduction", "Assuming NaBH4 reduces ketones to primary alcohols.", "Reduction of aldehydes with NaBH4 yields PRIMARY alcohols (RCH2OH). Reduction of ketones yields SECONDARY alcohols (RCH(OH)R')."),
    ("Nucleophilic Addition Curly Arrow Direction", "Mechanism", "Drawing arrow from C=O onto CN-.", "Curly arrow MUST start from the LONE PAIR on the CN- carbon atom and point to the delta+ carbonyl carbon. A second arrow goes from C=O double bond onto the oxygen atom."),
    ("Why Aldehydes are More Reactive Than Ketones", "Reactivity Comparison", "Attributing aldehyde reactivity solely to steric factors.", "Aldehydes are more reactive than ketones due to BOTH (1) Steric factors (only 1 bulky alkyl group blocking attack) and (2) Electronic factors (alkyl groups are electron-donating, reducing delta+ on carbonyl carbon in ketones)."),
    ("Aldehyde Oxidation Products", "Oxidation", "Stating propanal oxidizes to propan-1-ol.", "Oxidation of aldehydes produces CARBOXYLIC ACIDS (e.g. propanal -> propanoic acid). Reduction produces primary alcohols.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p8_faq_titles, 1):
    p8_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_15B_Carbonyl_Compounds.pdf", p8_meta, p8_questions, p8_faqs)
print("Pack 8 (15B Carbonyl Compounds - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 9: 15C — CARBOXYLIC ACIDS (50 Qs + 10 FAQs)
# ==========================================
p9_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
    'subtopic_code': '15C',
    'subtopic_name': 'Carboxylic Acids (Dimers, Acidity, Reactions with NaHCO3 & PCl5)'
}

p9_questions = []

p9_questions.append(make_edexcel_q(
    1, "Carboxylic Acid Dimer Structure", "WCH14/01/Jan23/Q19", 4,
    "Ethanoic acid has a higher boiling point than expected from its molar mass.",
    [
        {'label': 'a', 'text': 'Draw the structure of an ethanoic acid dimer, showing all atoms and hydrogen bonds.', 'marks': 2},
        {'label': 'b', 'text': 'Explain why dimerisation increases the boiling point.', 'marks': 2}
    ],
    "1. (a) Two ethanoic acid molecules linked by 2 hydrogen bonds between C=O...H-O (2).<br/>1. (b) Dimerisation effectively doubles the molecular size and strength of intermolecular forces (2)."
))

p9_questions.append(make_edexcel_q(
    2, "Reactions of Carboxylic Acids with NaHCO3 and PCl5", "WCH14/01/Oct22/Q20", 5,
    "Propanoic acid reacts with (i) aqueous NaHCO3 and (ii) solid PCl5.",
    [
        {'label': 'a', 'text': 'Write the equation for propanoic acid reacting with NaHCO3 and state the observation.', 'marks': 2},
        {'label': 'b', 'text': 'Write the equation for propanoic acid reacting with PCl5 and state the observation.', 'marks': 3}
    ],
    "2. (a) CH3CH2COOH + NaHCO3 -> CH3CH2COONa + H2O + CO2 (1). Effervescence / bubbles of gas (1).<br/>2. (b) CH3CH2COOH + PCl5 -> CH3CH2COCl + POCl3 + HCl (2). Misty / steamy white fumes of HCl (1)."
))

for i in range(3, 26):
    p9_questions.append(make_edexcel_q(
        i, f"Carboxylic Acid Synthesis & Reaction Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider synthesis of carboxylic acid {i} (RCOOH) from nitrile RCN via acid hydrolysis.",
        [
            {'label': 'a', 'text': 'Write the equation for the hydrolysis of RCN using dilute HCl.', 'marks': 2},
            {'label': 'b', 'text': 'State the essential reaction condition for nitrile hydrolysis.', 'marks': 1}
        ],
        f"{i}. (a) RCN + HCl + 2H2O -> RCOOH + NH4Cl (2).<br/>{i}. (b) Reflux with dilute acid / alkali (1)."
    ))

for i in range(26, 51):
    p9_questions.append(make_edexcel_q(
        i, f"A* Challenge: Relative Acidity & Inductive Effects {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"Compare the acid strength (Ka values) of ethanoic acid (Ka = 1.74x10^-5), chloroethanoic acid (Ka = 1.38x10^-3), and dichloroethanoic acid (Ka = 5.0x10^-2).",
        [
            {'label': 'a', 'text': 'Explain the trend in Ka values in terms of the inductive effect of chlorine atoms.', 'marks': 3},
            {'label': 'b', 'text': 'Predict, with a reason, whether trichloroethanoic acid is a stronger or weaker acid than dichloroethanoic acid.', 'marks': 2}
        ],
        f"{i}. (a) Chlorine is electronegative and exerts an electron-withdrawing inductive effect (-I effect) (1). Withdraws electron density from carboxylate C-O group, delocalising the negative charge on COO- anion (1). Stabilises the carboxylate anion, shifting RCOOH ⇌ RCOO- + H+ equilibrium to the right -> higher Ka (1).<br/>{i}. (b) Stronger acid (higher Ka) (1). Three Cl atoms exert an even greater electron-withdrawing effect, further stabilising CCl3COO- (1)."
    ))

p9_faqs = []
p9_faq_titles = [
    ("PCl5 Test Observations", "Inorganic Reagents", "Writing 'white precipitate' for PCl5 test.", "PCl5 reacts with -OH groups to evolve HCl gas which forms MISTY / STEAMY WHITE FUMES when exposed to moist air. No precipitate is formed."),
    ("NaHCO3 vs Na2CO3 Reactions", "Carbonate Testing", "Thinking NaHCO3 gives different products than Na2CO3.", "Both NaHCO3 and Na2CO3 react with carboxylic acids to evolve CO2 gas (effervescence). NaHCO3 is preferred to test for carboxylic acids because weaker acids like phenol do NOT react with NaHCO3."),
    ("Nitrile Hydrolysis Stoichiometry", "Nitrile Reactions", "Forgetting the water and acid stoichiometry in nitrile hydrolysis.", "Acidic hydrolysis: RCN + 2H2O + HCl -> RCOOH + NH4Cl (requires 2 H2O and 1 HCl). Alkaline hydrolysis: RCN + H2O + NaOH -> RCOONa + NH3."),
    ("Inductive Effect on Carboxylic Acid Strength", "Acid Strength Factors", "Claiming chlorine atoms make the O-H bond stronger.", "Chlorine is electron-withdrawing (-I effect). It STABILISES THE CARBOXYLATE ANION (RCOO-) by spreading out the negative charge. A more stable anion -> equilibrium shifts right -> STRONGER acid."),
    ("Alkyl Group Effect on Acidity", "Inductive Effects", "Expecting methanoic acid to be weaker than ethanoic acid.", "Alkyl groups (CH3-) are electron-DONATING (+I effect). They push electron density onto the COO- group, destabilising the anion. Thus ethanoic acid is WEAKER than methanoic acid."),
    ("Reduction of Carboxylic Acids", "Reduction Products", "Using NaBH4 to reduce carboxylic acids.", "NaBH4 is TOO WEAK to reduce carboxylic acids! LiAlH4 in dry ether MUST be used, reducing the carboxylic acid all the way to a PRIMARY ALCOHOL (RCH2OH)."),
    ("Decarboxylation Reactions", "Decarboxylation", "Forgetting the reagent for removing a carboxyl group.", "Heating a carboxylic acid sodium salt (RCOONa) with soda lime (NaOH/CaO) removes CO2 to form an alkane (RH) with ONE LESS CARBON atom."),
    ("Carboxylic Acid Solubilities", "Hydrogen Bonding", "Stating long-chain carboxylic acids are water-soluble.", "Carboxylic acids C1-C4 are miscible with water due to H-bonding. Beyond C4, the hydrophobic non-polar alkyl chain dominates, drastically REDUCING water solubility."),
    ("Esterification Equilibrium Shifting", "Reversible Reactions", "Adding water to shift esterification equilibrium to the right.", "Esterification RCOOH + R'OH ⇌ RCOOR' + H2O is reversible. To increase ester yield: remove water as it forms or use a large excess of alcohol/acid."),
    ("Distinguishing Phenol from Carboxylic Acids", "Functional Group Tests", "Assuming neutral FeCl3 distinguishes carboxylic acids from phenols.", "Phenol reacts with neutral FeCl3 to give a PURPLE solution, but does NOT react with NaHCO3. Carboxylic acids react with NaHCO3 to evolve CO2 gas.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p9_faq_titles, 1):
    p9_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_15C_Carboxylic_Acids.pdf", p9_meta, p9_questions, p9_faqs)
print("Pack 9 (15C Carboxylic Acids - 50 Qs + 10 FAQs) compiled successfully!")
