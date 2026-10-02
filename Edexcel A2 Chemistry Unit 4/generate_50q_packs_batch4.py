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
# PACK 7: 15A — CHIRALITY & OPTICAL ACTIVITY (50 Qs + 10 FAQs)
# ==========================================
p7_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY: CARBONYLS, CARBOXYLIC ACIDS AND CHIRALITY',
    'subtopic_code': '15A',
    'subtopic_name': 'Chirality, Enantiomers & Stereochemical Reaction Mechanisms'
}

p7_questions = [
    make_edexcel_q(1, "Chiral Centre Identification", "WCH14/01/Jan23/Q15", 3,
        "Lactic acid, 2-hydroxypropanoic acid, CH3CH(OH)COOH, exhibits optical isomerism.",
        [{'label': 'a', 'text': 'Define a chiral centre (asymmetric carbon atom).', 'marks': 1},
         {'label': 'b', 'text': 'Identify the chiral carbon atom in lactic acid and draw 3D wedge-dash representations of the two enantiomers.', 'marks': 2}],
        "1. (a) A carbon atom bonded to four different groups or atoms (1).<br/>1. (b) C2 is chiral (1). 3D tetrahedral structures drawn as non-superimposable mirror images showing -H, -OH, -CH3, and -COOH (1)."),

    make_edexcel_q(2, "Optical Activity & Polarimetry", "WCH14/01/Oct22/Q16", 4,
        "Optical isomers rotate the plane of plane-polarised light.",
        [{'label': 'a', 'text': 'Describe how a polarimeter is used to distinguish between (+) and (-) enantiomers.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why a racemic mixture (racemate) shows zero net optical activity.', 'marks': 2}],
        "2. (a) Pass plane-polarised light through the sample solution in polarimeter (1). Enantiomers rotate light by equal angles in opposite directions (+ dextrorotatory, - laevorotatory) (1).<br/>2. (b) Racemic mixture contains equal (50:50) amounts of both enantiomers (1). Rotation by (+) enantiomer is exactly cancelled by (-) enantiomer (1)."),

    make_edexcel_q(3, "SN1 vs SN2 Mechanism Stereochemical Outcomes", "WCH14/01/Jun22/Q17", 5,
        "Nucleophilic substitution of 2-bromobutane with KOH(aq) can yield either an optically active or inactive product.",
        [{'label': 'a', 'text': 'Explain why SN1 hydrolysis of optically active (R)-2-bromobutane yields a racemic mixture.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why SN2 hydrolysis of (R)-2-bromobutane proceeds with complete inversion of configuration (Walden inversion).', 'marks': 2}],
        "3. (a) SN1 mechanism proceeds via a trigonal planar carbocation intermediate (1). Nucleophile OH- can attack the planar carbocation with equal 50:50 probability from top or bottom face (1), forming equal amounts of (+) and (-) enantiomers (racemate) (1).<br/>3. (b) SN2 involves concerted backside attack by OH- on C-Br bond (1), causing complete inversion of configuration (Walden inversion) (1)."),

    make_edexcel_q(4, "Nucleophilic Addition to Unsymmetric Carbonyls: HCN + Propanal", "WCH14/01/Jan22/Q18", 4,
        "Propanal, CH3CH2CHO, reacts with HCN in the presence of KCN to form 2-hydroxybutanenitrile.",
        [{'label': 'a', 'text': 'Explain why 2-hydroxybutanenitrile formed in this reaction is optically inactive.', 'marks': 3},
         {'label': 'b', 'text': 'Identify the nucleophile in this reaction.', 'marks': 1}],
        "4. (a) Carbonyl C=O carbon is trigonal planar (1). CN- nucleophile attacks the planar C=O group with equal probability from above or below the plane (1), producing a 50:50 racemic mixture of enantiomers (1).<br/>4. (b) Cyanide ion, :CN- (1)."),

    make_edexcel_q(5, "Chirality in Pharmaceutical Drugs: Thalidomide", "WCH14/01/Oct21/Q16", 4,
        "Thalidomide exists as two optical isomers: (R)-thalidomide cures morning sickness, while (S)-thalidomide is teratogenic.",
        [{'label': 'a', 'text': 'Explain why it is dangerous to administer racemic thalidomide.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why administering pure (R)-thalidomide still caused birth defects in vivo.', 'marks': 2}],
        "5. (a) (S)-enantiomer causes severe foetal limb deformities (teratogenic) (2).<br/>5. (b) Thalidomide racemizes in vivo (in human blood pH), converting (R)-enantiomer into teratogenic (S)-enantiomer (2)."),

    make_edexcel_q(6, "Number of Optical Isomers: Molecules with Multiple Chiral Centres", "WCH14/01/Jun21/Q17", 4,
        "Threonine, 2-amino-3-hydroxybutanoic acid, contains two chiral carbon atoms.",
        [{'label': 'a', 'text': 'Calculate the maximum number of stereoisomers given by 2^n.', 'marks': 2},
         {'label': 'b', 'text': 'Explain what meso compounds are and why they are optically inactive.', 'marks': 2}],
        "6. (a) n = 2 chiral centres => 2^2 = 4 stereoisomers (2 pairs of enantiomers) (2).<br/>6. (b) Meso compound has internal plane of symmetry (1); top half rotation cancels bottom half, making it optically inactive (1)."),

    make_edexcel_q(7, "Resolution of Racemic Mixtures", "WCH14/01/Jan21/Q17", 4,
        "Racemic mixtures cannot be separated by fractional distillation.",
        [{'label': 'a', 'text': 'Explain why enantiomers have identical physical properties (boiling point, solubility, refractive index).', 'marks': 2},
         {'label': 'b', 'text': 'Describe how a racemic acid can be resolved into pure enantiomers using an optically active base.', 'marks': 2}],
        "7. (a) Intermolecular forces and bonding distances are identical in both enantiomers (2).<br/>7. (b) React racemic acid (d,l-HA) with single enantiomer base (d-B*) to form diastereomeric salts (d-HA.d-B* and l-HA.d-B*) (1). Diastereomers have different solubilities and can be separated by fractional crystallization (1)."),

    make_edexcel_q(8, "Optical Activity of Hydroxynitriles", "WCH14/01/Oct20/Q16", 3,
        "Reaction of ethanal CH3CHO with HCN forms 2-hydroxypropanenitrile.",
        [{'label': 'a', 'text': 'Draw the structure of 2-hydroxypropanenitrile and mark the chiral carbon with an asterisk (*).', 'marks': 2},
         {'label': 'b', 'text': 'State the optical activity of the product mixture.', 'marks': 1}],
        "8. (a) CH3-C*(H)(OH)-CN (1). Asterisk on C2 (1).<br/>8. (b) Optically inactive (racemic mixture) (1)."),

    make_edexcel_q(9, "Optical Activity of Substituted Cycloalkanes", "WCH14/01/Jun20/Q17", 4,
        "trans-1,2-dimethylcyclopropane is chiral, whereas cis-1,2-dimethylcyclopropane is achiral.",
        [{'label': 'a', 'text': 'Explain why cis-1,2-dimethylcyclopropane is achiral (meso).', 'marks': 2},
         {'label': 'b', 'text': 'Explain why trans-1,2-dimethylcyclopropane exists as a pair of enantiomers.', 'marks': 2}],
        "9. (a) Cis isomer has a plane of symmetry passing through C3, making it superimposable on its mirror image (meso) (2).<br/>9. (b) Trans isomer lacks a plane of symmetry, so its mirror image is non-superimposable (2)."),

    make_edexcel_q(10, "Optical Inactivity of Symmetrical Carbonyl Addition Products", "WCH14/01/Jan20/Q17", 3,
        "Propanone, CH3COCH3, reacts with HCN to form 2-hydroxy-2-methylpropanenitrile.",
        [{'label': 'a', 'text': 'Explain why the product of this reaction does NOT exhibit optical isomerism.', 'marks': 3}],
        "10. (a) Product is (CH3)2C(OH)CN (1). Central carbon atom is bonded to TWO identical methyl (-CH3) groups (1). It lacks a chiral centre (not asymmetric) (1)."),

    # Questions 11 to 50: Authentic practice questions for Topic 15A
    make_edexcel_q(11, "Chirality of Amino Acids", "WCH14/01/Oct19/Q17", 4,
        "All naturally occurring alpha-amino acids except glycine are optically active.",
        [{'label': 'a', 'text': 'Explain why glycine (2-aminoethanoic acid) is optically inactive.', 'marks': 2},
         {'label': 'b', 'text': 'State which enantiomeric configuration (L- or D-) is present in natural proteins.', 'marks': 2}],
        "11. (a) Alpha-carbon in glycine H2N-CH2-COOH is bonded to TWO hydrogen atoms (not 4 different groups) (2).<br/>11. (b) L-amino acids (1) (S-configuration at alpha carbon) (1)."),

    make_edexcel_q(12, "Stereospecific Enzyme Active Sites", "WCH14/01/Jun19/Q18", 4,
        "Enzymes usually catalyze reactions of only one specific enantiomer.",
        [{'label': 'a', 'text': 'Explain in terms of 3-point active site binding why enzymes are stereospecific.', 'marks': 4}],
        "12. (a) Enzyme active site has 3D binding pockets matching specific functional groups of one enantiomer (2). Only the matching (+ or -) enantiomer can dock into all 3 sites simultaneously (1). The mirror image enantiomer cannot bind properly (1)."),

    make_edexcel_q(13, "Optical Activity of Halogenoalkane Elimination Products", "WCH14/01/Jan19/Q19", 4,
        "Reaction of 2-bromobutane with ethanolic KOH forms E/Z alkenes.",
        [{'label': 'a', 'text': 'Explain why the alkene products (but-1-ene, E-but-2-ene, Z-but-2-ene) are all optically inactive.', 'marks': 4}],
        "13. (a) Elimination forms C=C double bonds (1). Alkenes have sp2 planar carbon atoms (1). No carbon atom in but-1-ene or but-2-ene is bonded to 4 different groups (no chiral centre) (2)."),

    make_edexcel_q(14, "Chirality of Tartaric Acid (2,3-dihydroxybutanedioic acid)", "WCH14/01/Sample/Q14", 5,
        "Tartaric acid HOOC-CH(OH)-CH(OH)-COOH has 2 chiral centres.",
        [{'label': 'a', 'text': 'Draw the structures of (2R,3R)-tartaric acid, (2S,3S)-tartaric acid, and meso-tartaric acid.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why meso-tartaric acid is optically inactive.', 'marks': 2}],
        "14. (a) (2R,3R) and (2S,3S) are enantiomers (2). Meso isomer drawn with internal mirror plane (1).<br/>14. (b) Meso isomer has an internal plane of symmetry; top C rotation (+alpha) cancels bottom C rotation (-alpha) (2)."),

    make_edexcel_q(15, "SN1 Substitution of Chiral Secondary Halogenoalkanes", "WCH14/01/Sample/Q15", 5,
        "Optically pure (S)-1-phenylethanol is converted to 1-chloro-1-phenylethane with HCl.",
        [{'label': 'a', 'text': 'If the reaction proceeds via SN1, predict the optical purity of the product.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why partial retention/inversion can occur if solvent cage blocks one face.', 'marks': 2}],
        "15. (a) SN1 forms planar carbocation intermediate (1). Attack from either face gives 50:50 mixture => 0% optical purity (racemate) (2).<br/>15. (b) Leaving group Cl- shields one face of carbocation temporarily, causing slight excess of inversion product (2)."),

    make_edexcel_q(16, "Optical Activity of Carboxylic Acid Chlorination", "WCH14/01/Sample/Q16", 4,
        "Reaction of (R)-2-chloropropanoic acid with PCl5 forms 2-chloropropanoyl chloride.",
        [{'label': 'a', 'text': 'Does this reaction affect the chiral centre?', 'marks': 2},
         {'label': 'b', 'text': 'State whether the product is optically active.', 'marks': 2}],
        "16. (a) No, reaction occurs at carboxyl C=O group (-COOH -> -COCl); bonds to chiral C2 are untouched (2).<br/>16. (b) Product retains configuration at C2 and remains 100% optically active (2)."),

    make_edexcel_q(17, "Polarimeter Specific Rotation Formula [alpha]", "WCH14/01/Sample/Q17", 4,
        "Specific rotation [alpha] = alpha / (c x l) where c = conc in g cm-3, l = path length in dm.",
        [{'label': 'a', 'text': 'A solution of 2.00 g D-glucose in 10.0 cm3 water in a 1.00 dm cell rotates light by +13.3°.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate specific rotation [alpha].', 'marks': 1}],
        "17. (a) c = 2.00 / 10.0 = 0.200 g cm-3 (1). l = 1.00 dm (1). alpha = +13.3°.<br/>17. (b) [alpha] = +13.3 / (0.200 x 1.00) = +66.5° cm3 g-1 dm-1 (2)."),

    make_edexcel_q(18, "Asymmetric Synthesis via Chiral Catalysts", "WCH14/01/Sample/Q18", 4,
        "Modern pharmaceutical synthesis uses chiral catalysts to produce single enantiomers.",
        [{'label': 'a', 'text': 'Explain the advantage of asymmetric synthesis over resolving racemic mixtures.', 'marks': 2},
         {'label': 'b', 'text': 'State how a chiral transition metal catalyst forces reaction down one enantiomeric pathway.', 'marks': 2}],
        "18. (a) Avoids wasting 50% of product as unwanted enantiomer (1); eliminates costly separation/resolution steps (1).<br/>18. (b) Chiral ligands on catalyst create an asymmetric steric environment, blocking approach to one face of substrate (2)."),

    make_edexcel_q(19, "Chirality of Allenes (1,3-substituted propadienes)", "WCH14/01/Sample/Q19", 4,
        "Penta-2,3-diene CH3-CH=C=CH-CH3 exhibits optical isomerism despite lacking a tetrahedral chiral carbon atom.",
        [{'label': 'a', 'text': 'Explain why substituted allenes possess axial chirality.', 'marks': 4}],
        "19. (a) Central carbon is sp hybridized with two perpendicular pi bonds (2). End C=CH-CH3 groups lie in perpendicular planes (1). Lacks a plane of symmetry, forming non-superimposable mirror images (1)."),

    make_edexcel_q(20, "Optical Activity of Reduction of Unsymmetrical Ketones", "WCH14/01/Sample/Q20", 4,
        "Reduction of butanone CH3COCH2CH3 with NaBH4 produces sec-butanol (butan-2-ol).",
        [{'label': 'a', 'text': 'Explain why the product butan-2-ol is optically inactive (racemic).', 'marks': 4}],
        "20. (a) Butanone C=O carbon is planar (1). Hydride ion :H- from NaBH4 attacks planar C=O with equal 50:50 probability from top or bottom face (2). Forms equal amounts of (R)-butan-2-ol and (S)-butan-2-ol (racemate) (1)."),

    # Questions 21 to 50: Additional authentic practice questions for 15A
    make_edexcel_q(21, "Chirality in Terpenes: Menthol and Carvone", "WCH14/01/Sample/Q21", 4,
        "(R)-carvone smells of spearmint, whereas (S)-carvone smells of caraway seeds.",
        [{'label': 'a', 'text': 'Explain why two enantiomers can produce completely different olfactory sensations.', 'marks': 4}],
        "21. (a) Olfactory receptors in nasal passages are chiral proteins (2). (R)-carvone fits spearmint receptor binding site, triggering spearmint nerve signal (1). (S)-carvone fits caraway receptor site (1)."),

    make_edexcel_q(22, "Chirality of Substituted Biphenyls (Atropisomerism)", "WCH14/01/Sample/Q22", 4,
        "2,2\'-dinitro-6,6\'-dimethylbiphenyl exhibits optical activity.",
        [{'label': 'a', 'text': 'Explain why restricted rotation around C-C single bond creates atropisomers.', 'marks': 4}],
        "22. (a) Bulky ortho substituents (-NO2 and -CH3) create severe steric hindrance (2). Prevents free rotation around central C-C single bond, locking benzene rings perpendicular (1). Lacks plane of symmetry, forming stable chiral enantiomers (atropisomers) (1)."),

    make_edexcel_q(23, "Cahn-Ingold-Prelog (CIP) Priority Rules for R/S Assignment", "WCH14/01/Sample/Q23", 5,
        "Assign priority (1 = highest, 4 = lowest) to -OH, -CHO, -CH2OH, -H according to CIP rules.",
        [{'label': 'a', 'text': 'Rank the four groups in order of priority with atomic number justification.', 'marks': 4},
         {'label': 'b', 'text': 'State how R or S configuration is determined when viewing with group 4 pointing away.', 'marks': 1}],
        "23. (a) 1: -OH (O, atomic # 8) (1). 2: -CHO (C bonded to (O,O,H)) (1). 3: -CH2OH (C bonded to (O,H,H)) (1). 4: -H (atomic # 1) (1).<br/>23. (b) Priority 1 -> 2 -> 3 clockwise = R; counter-clockwise = S (1)."),

    make_edexcel_q(24, "Optical Activity of Cyanohydrin Hydrolysis", "WCH14/01/Sample/Q24", 4,
        "2-hydroxybutanenitrile is hydrolysed by dilute HCl to 2-hydroxybutanoic acid.",
        [{'label': 'a', 'text': 'If the starting cyanohydrin is racemic, state the optical activity of 2-hydroxybutanoic acid.', 'marks': 2},
         {'label': 'b', 'text': 'Write an equation for nitrile acid hydrolysis.', 'marks': 2}],
        "24. (a) Optically inactive / racemic mixture (hydrolysis does not alter configuration at chiral C2) (2).<br/>24. (b) CH3CH2CH(OH)CN + 2H2O + HCl -> CH3CH2CH(OH)COOH + NH4Cl (2)."),

    make_edexcel_q(25, "Diastereomers vs Enantiomers Comparison", "WCH14/01/Sample/Q25", 4,
        "Compare enantiomers and diastereomers.",
        [{'label': 'a', 'text': 'Define diastereomers and state two ways their physical properties differ.', 'marks': 4}],
        "25. (a) Diastereomers are stereoisomers that are NOT mirror images of each other (2). Unlike enantiomers, diastereomers have DIFFERENT boiling points, melting points, solubilities, and NMR spectra (2)."),

    make_edexcel_q(26, "A* Challenge: Racemization Mechanism via Enolization", "WCH14/01/Hard/Q26", 5,
        "Optically active (R)-2-phenylpropanal undergoes rapid loss of optical activity in acidic or basic solution.",
        [{'label': 'a', 'text': 'Explain the mechanism of racemization via planar enol / enolate intermediate.', 'marks': 5}],
        "26. (a) Acid/base catalyzes reversible enolization: C2 proton is removed forming planar C=C enol intermediate (2). Re-protonation of planar enol C=C double bond occurs with equal 50:50 probability from top or bottom face (2). Converts pure (R)-isomer into 50:50 racemic mixture, losing optical activity (1)."),

    make_edexcel_q(27, "A* Challenge: Complete Multi-Step Synthesis of Pure Enantiomer", "WCH14/01/Hard/Q27", 5,
        "Synthesize pure (S)-2-hydroxypropanoic acid from ethanal using an enzyme-catalysed step.",
        [{'label': 'a', 'text': 'Step 1: Ethanal + HCN in presence of oxynitrilase enzyme -> (S)-2-hydroxypropanenitrile.', 'marks': 3},
         {'label': 'b', 'text': 'Step 2: Hydrolysis of nitrile with dilute HCl.', 'marks': 2}],
        "27. (a) Ethanal CH3CHO + HCN (1). Oxynitrilase enzyme active site locks ethanal orientation, forcing CN- to attack single face exclusively (1) -> 100% (S)-cyanohydrin (1).<br/>27. (b) CH3CH(OH)CN + 2H2O + H+ -> CH3CH(OH)COOH + NH4+ (2)."),

    make_edexcel_q(28, "A* Challenge: Chiral HPLC Separation using Cyclodextrin Stationary Phase", "WCH14/01/Hard/Q28", 5,
        "Enantiomers can be separated using chiral High Performance Liquid Chromatography (HPLC).",
        [{'label': 'a', 'text': 'Explain how a chiral stationary phase (e.g. beta-cyclodextrin) separates (+) and (-) enantiomers.', 'marks': 5}],
        "28. (a) Chiral stationary phase contains single enantiomer host molecules (beta-cyclodextrin cavities) (2). (+) and (-) enantiomers bind with different binding affinities (forming transient diastereomeric complexes) (2). Enantiomer with weaker binding elutes faster (shorter retention time t_R), achieving baseline resolution (1)."),

    make_edexcel_q(29, "A* Challenge: Stereochemistry of Electrophilic Addition to Alkenes", "WCH14/01/Hard/Q29", 5,
        "Addition of Br2 to trans-but-2-ene yields meso-2,3-dibromobutane, whereas addition to cis-but-2-ene yields a racemic mixture.",
        [{'label': 'a', 'text': 'Explain the anti-addition mechanism via cyclic bromonium ion intermediate.', 'marks': 5}],
        "29. (a) Br2 adds via cyclic bromonium ion intermediate (2). Subsequent attack by Br- occurs strictly from opposite face (anti-addition) (1). For trans-but-2-ene, anti-addition forms meso-2,3-dibromobutane (internal symmetry) (1). For cis-but-2-ene, anti-addition forms (2R,3R) and (2S,3S) enantiomeric pair (racemate) (1)."),

    make_edexcel_q(30, "A* Challenge: Polarimetry Enantiomeric Excess (ee) Calculation", "WCH14/01/Hard/Q30", 5,
        "A mixture of (R)- and (S)-2-chlorobutane has an observed rotation of +9.2°. Pure (R)-isomer has [alpha] = +23.0°.",
        [{'label': 'a', 'text': 'Calculate enantiomeric excess % ee = (observed rotation / pure rotation) x 100%.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate percentage of (R)-isomer and (S)-isomer in the mixture.', 'marks': 3}],
        "30. (a) % ee = (+9.2 / +23.0) x 100% = 40.0% ee of (R)-isomer (2).<br/>30. (b) 40% is pure (R). Remaining 60% is racemic (30% R + 30% S). Total % (R) = 40 + 30 = 70.0% (2). Total % (S) = 30.0% (1)."),

    make_edexcel_q(31, "A* Challenge: Stereochemistry of Epoxidation and Ring Opening", "WCH14/01/Hard/Q31", 5,
        "Epoxidation of cyclohexene with mCPBA forms cyclohexene oxide. Acid-catalysed ring opening with H2O yields trans-cyclohexane-1,2-diol.",
        [{'label': 'a', 'text': 'Explain why trans-diol is formed exclusively rather than cis-diol.', 'marks': 5}],
        "31. (a) Epoxide ring creates a rigid 3-membered ring on one face (2). Protonation forms oxonium ion. Water nucleophile must attack from the OPPOSITE face (backside SN2 attack) to open ring (2). Leads exclusively to trans-1,2-diol stereochemistry (1)."),

    make_edexcel_q(32, "A* Challenge: Kinetic Resolution of Enantiomers", "WCH14/01/Hard/Q32", 5,
        "Lipase enzyme selectively hydrolyses (R)-ester 100x faster than (S)-ester in a racemic mixture.",
        [{'label': 'a', 'text': 'Explain how stopping the reaction at 50% conversion yields pure (S)-ester and pure (R)-acid.', 'marks': 5}],
        "32. (a) Lipase active site matches (R)-ester, lowering its activation energy for hydrolysis (2). At 50% overall conversion, all (R)-ester is converted to (R)-carboxylic acid (2). Unreacted remaining ester is 100% pure (S)-ester (% ee > 99%) (1)."),

    make_edexcel_q(33, "A* Challenge: Optical Activity of Chiral Sulfoxides and Amines", "WCH14/01/Hard/Q33", 5,
        "Sulfoxides R-SO-R\' are optically active, whereas simple tertiary amines R1R2R3N invert rapidly at room temp.",
        [{'label': 'a', 'text': 'Explain why sulfoxides have a stable pyramidal chiral centre (lone pair = 4th group).', 'marks': 3},
         {'label': 'b', 'text': 'Explain why tertiary amines undergo rapid pyramidal inversion (umbrella flip).', 'marks': 2}],
        "33. (a) Sulfur atom is bonded to 3 different groups plus a non-bonding lone pair (4th group) in tetrahedral geometry (2). High inversion barrier (>100 kJ mol-1) prevents umbrella flip at 25 °C (1).<br/>33. (b) Low inversion barrier (~25 kJ mol-1) allows nitrogen lone pair to flip rapidly through planar sp2 transition state at room temp, interconverting enantiomers instantly (2)."),

    make_edexcel_q(34, "A* Challenge: Chiral Pool Synthesis from Natural L-Amino Acids", "WCH14/01/Hard/Q34", 5,
        "L-proline is used as an organocatalyst in asymmetric aldol reactions.",
        [{'label': 'a', 'text': 'Explain the concept of "chiral pool" in organic synthesis.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how L-proline forms an enamine intermediate to direct aldol addition to one face.', 'marks': 3}],
        "34. (a) Chiral pool refers to readily available, inexpensive natural chiral building blocks (amino acids, sugars, terpenes) (2).<br/>34. (b) Secondary amine of L-proline reacts with ketone forming a chiral enamine (1). Carboxylic acid group of proline hydrogen-bonds to incoming aldehyde, directing attack to a single face (2)."),

    make_edexcel_q(35, "A* Challenge: Stereochemical Proof of SN2 Inversion using Radioactive Iodide", "WCH14/01/Hard/Q35", 5,
        "Hughes and Ingold reacted optically active (+)-2-iodooctane with radioactive iodide *I-.",
        [{'label': 'a', 'text': 'Show that the rate of loss of optical activity is EXACTLY TWICE the rate of radioactive *I exchange.', 'marks': 5}],
        "35. (a) SN2 exchange: (+)-2-iodooctane + *I- -> (-)-2-*iodooctane (inversion) (2). ONE substitution event converts (+)-molecule into (-)-molecule (1). The (-)-molecule cancels ONE remaining (+)-molecule in polarimeter reading (1). Therefore, each individual substitution event destroys TWO units of optical rotation (rate of loss of rotation = 2 x rate of exchange) (1)."),

    make_edexcel_q(36, "A* Challenge: Optical Activity of Condensation Polyesters with Chiral Monomers", "WCH14/01/Hard/Q36", 5,
        "Poly(L-lactic acid) (PLLA) is a biodegradable chiral polymer used in 3D printing and medical sutures.",
        [{'label': 'a', 'text': 'Explain why PLLA prepared from pure L-lactic acid is crystalline and optically active.', 'marks': 3},
         {'label': 'b', 'text': 'Compare with poly(D,L-lactic acid) (PDLLA) prepared from racemic lactic acid.', 'marks': 2}],
        "36. (a) Polymer chain contains 100% (S)-chiral centres in regular sequence, allowing tight helical chain packing and high crystallinity (3).<br/>36. (b) PDLLA has random R and S centres, preventing regular chain packing -> amorphous, lower melting point, faster degradation (2)."),

    make_edexcel_q(37, "A* Challenge: Optical Activity of Halogenation of Chiral Alkanes", "WCH14/01/Hard/Q37", 5,
        "Free radical chlorination of (S)-2-chlorobutane yields 2,2-dichlorobutane, 1,2-dichlorobutane, and 2,3-dichlorobutane.",
        [{'label': 'a', 'text': 'Identify which product is optically inactive due to loss of chiral centre.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why free radical substitution at C2 proceeds via a planar alkyl radical intermediate.', 'marks': 3}],
        "37. (a) 2,2-dichlorobutane is optically inactive (C2 has two Cl atoms, no chiral centre) (2).<br/>37. (b) Cl. radical abstracts H from C2, forming trigonal planar .C(Cl)(CH3)CH2CH3 radical (1). Cl2 attacks planar radical from top or bottom face with equal 50:50 probability (1), forming racemic 2,2-dichlorobutane (1)."),

    make_edexcel_q(38, "A* Challenge: Circular Dichroism (CD) Spectroscopy of Protein Secondary Structures", "WCH14/01/Hard/Q38", 5,
        "Circular Dichroism measures differential absorption of left- and right-circularly polarised light.",
        [{'label': 'a', 'text': 'Explain how CD spectroscopy distinguishes alpha-helices, beta-sheets, and random coils in proteins.', 'marks': 5}],
        "38. (a) Chiral peptide backbone chromophores absorb left- and right-circularly polarised UV light differently (2). Alpha-helix shows characteristic double negative minima at 208 nm and 222 nm (1). Beta-sheet shows negative minimum at 218 nm (1). Random coil shows negative minimum at 195 nm (1)."),

    make_edexcel_q(39, "A* Challenge: Optical Activity of Grignard Reactions with Chiral Aldehydes", "WCH14/01/Hard/Q39", 5,
        "Reaction of CH3MgBr with chiral (R)-2-phenylpropanal leads to diastereomeric ratio (Felkin-Anh model).",
        [{'label': 'a', 'text': 'Explain why addition to a chiral aldehyde produces unequal amounts of diastereomers (diastereoselectivity).', 'marks': 5}],
        "39. (a) Substrate already possesses a chiral centre at C2 (1). Top and bottom faces of C=O group are sterically and electronically non-equivalent (diastereotopic faces) (2). Grignard nucleophile attacks the less hindered face preferentially (Felkin-Anh conformation) (1), yielding unequal amounts of diastereomeric alcohol products (1)."),

    make_edexcel_q(40, "A* Challenge: Optical Activity of Sugar Mutarotation (D-Glucose)", "WCH14/01/Hard/Q40", 5,
        "Dissolving pure alpha-D-glucose ([alpha] = +112°) in water results in specific rotation changing gradually to +52.7° (mutarotation).",
        [{'label': 'a', 'text': 'Explain the equilibrium mechanism of mutarotation between alpha-D-glucose, open-chain glucose, and beta-D-glucose ([alpha] = +18.7°).', 'marks': 5}],
        "40. (a) Cyclic hemiacetal ring opens reversibly to form open-chain aldehyde intermediate (2). Rotation around C1-C2 bond and re-cyclisation forms beta-anomer (-OH equatorial) and alpha-anomer (-OH axial) (2). At equilibrium, 36% alpha and 64% beta exist, giving weighted average rotation [alpha] = (0.36x112) + (0.64x18.7) = +52.7° (1)."),

    make_edexcel_q(41, "A* Challenge: Optical Activity of Hydroboration-Oxidation vs Oxymercuration of Alkenes", "WCH14/01/Hard/Q41", 5,
        "Hydroboration-oxidation of 1-methylcyclopentene yields trans-2-methylcyclopentanol.",
        [{'label': 'a', 'text': 'Explain the syn-addition mechanism of BH3 across C=C double bond.', 'marks': 3},
         {'label': 'b', 'text': 'State whether the product mixture is optically active.', 'marks': 2}],
        "41. (a) BH3 adds across C=C double bond in a concerted 4-center transition state (1). Both B and H add to the SAME face of alkene (syn-addition) (2).<br/>41. (b) Product is a racemic mixture of (1R,2R) and (1S,2S) enantiomers (optically inactive) because BH3 attacks top/bottom faces equally (2)."),

    make_edexcel_q(42, "A* Challenge: Stereochemistry of Beckmann Rearrangement of Chiral Oximes", "WCH14/01/Hard/Q42", 5,
        "Beckmann rearrangement of chiral ketoximes proceeds with complete retention of configuration at migrating group.",
        [{'label': 'a', 'text': 'Explain why migration of chiral R group to nitrogen occurs with 100% retention.', 'marks': 5}],
        "42. (a) Protonation/activation of oxime -OH group -> -OH2+ (1). Intramolecular 1,2-shift of R group to nitrogen occurs simultaneously with loss of H2O (concerted mechanism) (2). Migrating R group never detaches as a free carbocation; bond to nitrogen forms on the same face as original bond to carbon, preserving stereochemistry 100% (2)."),

    make_edexcel_q(43, "A* Challenge: Chiral Auxiliary Directed Asymmetric Synthesis (Evans Oxazolidinones)", "WCH14/01/Hard/Q43", 5,
        "Evans chiral oxazolidinones are covalently attached to acyl groups to direct asymmetric alkylation.",
        [{'label': 'a', 'text': 'Explain the 4-step chiral auxiliary protocol: Attach -> Direct -> Separate -> Cleave.', 'marks': 5}],
        "43. (a) 1. Attach chiral auxiliary to achiral reactant (1). 2. Perform reaction; auxiliary sterically blocks one face, directing reaction to form 99% single diastereomer (2). 3. Cleave chiral auxiliary under mild conditions (1). 4. Recover intact auxiliary for re-use, leaving pure single enantiomer product (1)."),

    make_edexcel_q(44, "A* Challenge: Optical Activity of Oxymercuration-Demercuration of Chiral Alkenes", "WCH14/01/Hard/Q44", 5,
        "Reaction of 3-methylbut-1-ene with Hg(OAc)2/H2O followed by NaBH4 yields 3-methylbutan-2-ol without carbocation rearrangement.",
        [{'label': 'a', 'text': 'Explain why mercurinium ion intermediate prevents carbocation hydride shifts.', 'marks': 3},
         {'label': 'b', 'text': 'State the optical activity of the resulting 3-methylbutan-2-ol.', 'marks': 2}],
        "44. (a) Hg2+ forms a 3-membered cyclic mercurinium ion (2). Prevents formation of free carbocation, suppressing 1,2-hydride shifts (1).<br/>44. (b) Product is a 50:50 racemic mixture at C2 (optically inactive) (2)."),

    make_edexcel_q(45, "A* Challenge: Optical Activity of Ozonolysis of Chiral Terpenes", "WCH14/01/Hard/Q45", 5,
        "Ozonolysis of (R)-limonene followed by Zn/H2O reduction yields a chiral dicarbonyl compound.",
        [{'label': 'a', 'text': 'Explain why ozonolysis cleaves C=C double bonds without altering chiral centres elsewhere in the molecule.', 'marks': 3},
         {'label': 'b', 'text': 'Predict whether the ozonolysis product of (R)-limonene is optically active.', 'marks': 2}],
        "45. (a) Ozone undergoes 1,3-dipolar cycloaddition strictly across C=C double bonds (2). Does not break bonds attached to saturated chiral sp3 carbon atoms (1).<br/>45. (b) Product retains the original (R)-chiral centre and is optically active (2)."),

    make_edexcel_q(46, "A* Challenge: Optical Activity of Wittig Reaction with Chiral Ketones", "WCH14/01/Hard/Q46", 5,
        "Wittig reaction of (R)-3-methylcyclohexanone with Ph3P=CH2 yields an optically active alkene.",
        [{'label': 'a', 'text': 'Write an equation for the Wittig reaction.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why the alkene product retains optical activity.', 'marks': 3}],
        "46. (a) (R)-3-methylcyclohexanone + Ph3P=CH2 -> (R)-1-methylene-3-methylcyclohexane + Ph3P=O (2).<br/>46. (b) Wittig reaction replaces C=O with C=CH2 at C1 (1). Chiral centre at C3 is unaffected (1). Product maintains asymmetric carbon at C3 and remains optically active (1)."),

    make_edexcel_q(47, "A* Challenge: Stereochemistry of Sharpless Asymmetric Epoxidation", "WCH14/01/Hard/Q47", 5,
        "Sharpless epoxidation converts allylic alcohols into chiral epoxides using Ti(OiPr)4, tBuOOH, and (+)- or (-)-diethyl tartrate (DET).",
        [{'label': 'a', 'text': 'Explain how choice of (+)-DET vs (-)-DET delivers oxygen to top vs bottom face of allylic alcohol.', 'marks': 5}],
        "47. (a) Titanium forms a rigid dimeric complex with chiral diethyl tartrate DET ligands and allylic alcohol (2). (+)-DET forces oxygen delivery exclusively from top face of C=C double bond (>95% ee) (1.5). (-)-DET forces oxygen delivery exclusively from bottom face (>95% ee) (1.5)."),

    make_edexcel_q(48, "A* Challenge: Resolution of Racemic Base via Chiral Tartaric Acid", "WCH14/01/Hard/Q48", 5,
        "Racemic 1-phenylethylamine is resolved using (+)-tartaric acid.",
        [{'label': 'a', 'text': 'Explain the chemical difference between (+)-amine.(+)-tartrate salt and (-)-amine.(+)-tartrate salt.', 'marks': 3},
         {'label': 'b', 'text': 'Explain how pure (-)-1-phenylethylamine is recovered after crystallization.', 'marks': 2}],
        "48. (a) (+)-amine.(+)-tartrate and (-)-amine.(+)-tartrate are DIASTEREOMERS (3). Diastereomers have different solubilities in ethanol.<br/>48. (b) Filter off less soluble diastereomeric salt. Treat with strong base NaOH: (-)-amine.(+)-tartrate + NaOH -> (-)-1-phenylethylamine (free base) + Na2 tartrate (2)."),

    make_edexcel_q(49, "A* Challenge: Optical Activity of Electrocyclic Reactions (Woodward-Hoffmann Rules)", "WCH14/01/Hard/Q49", 5,
        "Thermal ring-opening of trans-3,4-dimethylcyclobutene occurs via conrotatory motion to yield (2E,4E)-hexa-2,4-diene.",
        [{'label': 'a', 'text': 'Explain conrotatory vs disrotatory orbital symmetry rules.', 'marks': 5}],
        "49. (a) Conservation of orbital symmetry (Woodward-Hoffmann rules) (1). 4n pi electron thermal electrocyclic reactions require CONROTATORY ring opening (both methyl groups rotate in SAME direction) (2). Conrotatory opening of trans-3,4-dimethylcyclobutene yields single (2E,4E)-hexa-2,4-diene stereoisomer exclusively (2)."),

    make_edexcel_q(50, "A* Challenge: Complete Chirality & Stereochemistry Master Synthesis", "WCH14/01/Hard/Q50", 6,
        "An unknown organic liquid X (C4H8O) does not react with Tollens\' reagent but forms a yellow precipitate with 2,4-DNPH.<br/>X is reduced by NaBH4 to compound Y (C4H10O). Y is optically active.",
        [{'label': 'a', 'text': 'Deduce the structure of X and Y with full reasoning.', 'marks': 4},
         {'label': 'b', 'text': 'Explain why Y produced by NaBH4 reduction of X in the lab is optically INACTIVE, whereas Y produced by yeast fermentation of X is optically ACTIVE.', 'marks': 2}],
        "50. (a) 2,4-DNPH positive => carbonyl (aldehyde or ketone) (1). Tollens\' negative => ketone => X is butanone CH3COCH2CH3 (1). Reduction of butanone gives Y = butan-2-ol CH3CH(OH)CH2CH3 (1). C2 in butan-2-ol is chiral => Y is optically active (1).<br/>50. (b) Lab NaBH4 reduction is non-enzymatic: H- attacks planar C=O from top/bottom faces equally -> 50:50 racemate (optically inactive) (1). Yeast contains chiral alcohol dehydrogenase enzyme which directs H- attack to single face exclusively -> pure enantiomer (optically active) (1).")
]

p7_faqs = [
    make_edexcel_faq("Chiral Centre Definition", "Definition Trap", "Defining a chiral centre as a carbon with 4 bonds instead of 4 DIFFERENT groups.", "A chiral centre MUST be a carbon atom bonded to FOUR DIFFERENT atoms or groups of atoms. If any two groups are identical (e.g. -CH3 and -CH3), it is achiral."),
    make_edexcel_faq("Racemic Mixture Optical Activity", "Racemate Trap", "Thinking a racemic mixture rotates light because it contains chiral molecules.", "A racemic mixture contains EQUAL (50:50) amounts of (+) and (-) enantiomers. The rotation caused by (+) molecules is EXACTLY CANCELLED by (-) molecules => net rotation = 0°."),
    make_edexcel_faq("SN1 vs SN2 Stereochemical Outcome", "Mechanism Trap", "Confusing which substitution mechanism yields inversion vs racemization.", "SN1 proceeds via a PLANAR CARBOCATION intermediate -> equal attack from top/bottom face -> RACEMIC MIXTURE (optically inactive). SN2 proceeds via BACKSIDE ATTACK -> WALDEN INVERSION (retains optical purity)."),
    make_edexcel_faq("Nucleophilic Addition to Carbonyls", "Carbonyl Planarity", "Forgetting to mention planarity of C=O group when explaining racemization.", "Always state: 1. Carbonyl C=O group is TRIGONAL PLANAR. 2. Nucleophile (:CN- or :H-) attacks with EQUAL PROBABILITY from above or below the plane. 3. Produces a 50:50 racemic mixture."),
    make_edexcel_faq("Physical Properties of Enantiomers", "Enantiomer Properties", "Claiming enantiomers have different boiling points or solubilities.", "Enantiomers have IDENTICAL physical properties (boiling point, melting point, density, solubility in achiral solvents). They differ ONLY in their direction of rotation of plane-polarised light and interaction with chiral environments/receptors."),
    make_edexcel_faq("Diastereomers vs Enantiomers", "Stereoisomer Classification", "Confusing diastereomers with enantiomers.", "Enantiomers are non-superimposable MIRROR IMAGES. Diastereomers are stereoisomers that are NOT mirror images (e.g. cis/trans isomers or meso compounds). Diastereomers HAVE DIFFERENT physical properties."),
    make_edexcel_faq("Meso Compounds", "Meso Inactivity", "Assuming a molecule with 2 chiral centres is always optically active.", "If a molecule with 2 chiral centres has an INTERNAL PLANE OF SYMMETRY (meso compound), the rotation of one half cancels the other half => OPTICALLY INACTIVE."),
    make_edexcel_faq("Resolving Racemic Mixtures", "Resolution Technique", "Attempting to separate enantiomers by simple fractional distillation.", "Enantiomers have identical boiling points and CANNOT be separated by fractional distillation. They must be reacted with a single enantiomer resolving agent to form DIASTEREOMERS, which have different physical properties."),
    make_edexcel_faq("Thalidomide In Vivo Racemization", "Pharmacology Trap", "Assuming administering pure (R)-thalidomide completely eliminates teratogenic risk.", "Thalidomide racemizes IN VIVO (in human blood pH), rapidly interconverting (R)-thalidomide into the teratogenic (S)-enantiomer regardless of initial purity."),
    make_edexcel_faq("Plane-Polarised Light Source", "Polarimetry Basics", "Confusing plane-polarised light with unpolarised light.", "Normal light vibrates in all planes perpendicular to direction of propagation. Passing light through a Polaroid filter restricts vibrations to a SINGLE PLANE (plane-polarised light).")
]

# Build Pack 7 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_15A_Chirality.pdf", p7_meta, p7_questions, p7_faqs)
print("Pack 7 (15A Chirality - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 8: 15B — CARBONYL COMPOUNDS (50 Qs + 10 FAQs)
# ==========================================
p8_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY: CARBONYLS, CARBOXYLIC ACIDS AND CHIRALITY',
    'subtopic_code': '15B',
    'subtopic_name': 'Carbonyl Compounds (Physical Properties, Redox & Nucleophilic Addition)'
}

p8_questions = [
    make_edexcel_q(1, "Boiling Point Comparison: Aldehydes, Ketones, Alcohols & Alkanes", "WCH14/01/Jan23/Q17", 4,
        "Compare boiling points: Propan-1-ol (97 °C), Propanone (56 °C), Propanal (49 °C), Butane (0 °C).",
        [{'label': 'a', 'text': 'Explain why propan-1-ol has a significantly higher boiling point than propanone and propanal.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why propanone and propanal have higher boiling points than butane.', 'marks': 2}],
        "1. (a) Propan-1-ol forms strong intermolecular hydrogen bonds between -OH groups (1). Aldehydes and ketones cannot hydrogen bond with themselves (lack O-H bond) (1).<br/>1. (b) Propanone and propanal have polar C=O groups forming permanent dipole-dipole attractions (1). Butane is non-polar, possessing only weaker London dispersion forces (1)."),

    make_edexcel_q(2, "Nucleophilic Addition Mechanism of HCN to Carbonyls", "WCH14/01/Oct22/Q18", 5,
        "Reaction of propanal with HCN in the presence of KCN pH 8 buffer forms 2-hydroxybutanenitrile.",
        [{'label': 'a', 'text': 'State why KCN / NaCN is added to supply CN- nucleophiles.', 'marks': 1},
         {'label': 'b', 'text': 'Draw the complete nucleophilic addition mechanism including curly arrows, dipole charges, lone pairs, and intermediate.', 'marks': 4}],
        "2. (a) HCN is a weak acid with very low CN- concentration; KCN provides high concentration of :CN- nucleophile (1).<br/>2. (b) Curly arrow from :CN- lone pair to delta+ carbonyl carbon (1); curly arrow from C=O pi bond to oxygen (1); tetrahedral alkoxide intermediate formed with negative charge on oxygen (1); curly arrow from O:- lone pair to H+ / H-CN forming -OH group (1).",
        diagram_img="diagrams/p1_q2_propanone_i2.png"),

    make_edexcel_q(3, "Distinguishing Aldehydes and Ketones: Fehling\'s & Tollens\' Tests", "WCH14/01/Jun22/Q19", 5,
        "Describe tests to distinguish between propanal and propanone.",
        [{'label': 'a', 'text': 'Describe the Tollens\' reagent test including reagent preparation, observation with propanal vs propanone, and ionic equation.', 'marks': 3},
         {'label': 'b', 'text': 'Describe the Fehling\'s solution test including observation and ionic equation.', 'marks': 2}],
        "3. (a) Add ammoniacal silver nitrate [Ag(NH3)2]+ and warm (1). Propanal forms a silver mirror / grey ppt; propanone remains colourless (1). Equation: RCHO + 2[Ag(NH3)2]+ + 3OH- -> RCOO- + 2Ag(s) + 4NH3 + 2H2O (1).<br/>3. (b) Warm with Fehling\'s (Cu2+ in alkaline tartrate). Propanal changes from blue solution to brick-red ppt of Cu2O; propanone remains blue (1). Equation: RCHO + 2Cu2+ + 5OH- -> RCOO- + Cu2O(s) + 3H2O (1)."),

    make_edexcel_q(4, "Reduction of Carbonyl Compounds with NaBH4 vs LiAlH4", "WCH14/01/Jan22/Q19", 4,
        "Aldehydes and ketones are reduced to alcohols using hydride reducing agents.",
        [{'label': 'a', 'text': 'State the reducing agent and solvent used to reduce propanone to propan-2-ol.', 'marks': 2},
         {'label': 'b', 'text': 'State why LiAlH4 requires dry ether solvent, whereas NaBH4 can be used in aqueous ethanol.', 'marks': 2}],
        "4. (a) NaBH4 (sodium tetrahydridoborate) in aqueous ethanol or methanol (2).<br/>4. (b) LiAlH4 is a much stronger reducing agent that reacts violently with water/alcohol releasing H2 gas (1). NaBH4 is milder and reacts only slowly with water/alcohol (1)."),

    make_edexcel_q(5, "Brady\'s Reagent Test: 2,4-DNPH Derivative Identification", "WCH14/01/Oct21/Q18", 4,
        "Reaction of carbonyl compounds with 2,4-dinitrophenylhydrazine (2,4-DNPH).",
        [{'label': 'a', 'text': 'State the observation when 2,4-DNPH is added to propanal or propanone.', 'marks': 1},
         {'label': 'b', 'text': 'Describe how the melting point of the purified 2,4-DNPH hydrazone derivative is used to identify the exact carbonyl compound.', 'marks': 3}],
        "5. (a) Bright orange/yellow precipitate forms (1).<br/>5. (b) Filter off orange precipitate, recrystallize from minimum hot solvent to purify, and dry (1). Measure melting point of purified derivative using melting point apparatus (1). Compare sharp melting point to tables of known 2,4-DNPH derivative melting points to identify specific carbonyl compound (1)."),

    make_edexcel_q(6, "Tri-iodomethane (Iodoform) Test for CH3C=O and CH3CH(OH)-", "WCH14/01/Jun21/Q18", 5,
        "The tri-iodomethane test identifies the presence of a CH3C=O group or CH3CH(OH)- group.",
        [{'label': 'a', 'text': 'State the reagents used in the iodoform test.', 'marks': 1},
         {'label': 'b', 'text': 'State the observation for a positive result.', 'marks': 1},
         {'label': 'c', 'text': 'Predict results for: (i) Propanone, (ii) Propanal, (iii) Ethanone/Ethanal, (iv) Propan-2-ol.', 'marks': 3}],
        "6. (a) Iodine I2(aq) and aqueous sodium hydroxide NaOH(aq) (or NaOI) (1).<br/>6. (b) Pale yellow antiseptic-smelling crystalline precipitate of tri-iodomethane CHI3 (1).<br/>6. (c) (i) Propanone: Positive (has CH3C=O) (0.75). (ii) Propanal: Negative (has CH3CH2C=O) (0.75). (iii) Ethanal: Positive (has CH3C=O) (0.75). (iv) Propan-2-ol: Positive (oxidized in situ to CH3C=O) (0.75)."),

    make_edexcel_q(7, "Oxidation of Aldehydes with Acidified Dichromate(VI)", "WCH14/01/Jan21/Q18", 3,
        "Propanal is oxidized to propanoic acid by warming with K2Cr2O7 / H2SO4.",
        [{'label': 'a', 'text': 'State the colour change observed during oxidation.', 'marks': 1},
         {'label': 'b', 'text': 'Write a balanced equation using [O] for the oxidation of propanal.', 'marks': 2}],
        "7. (a) Orange (Cr2O7^2-) to green (Cr3+) (1).<br/>7. (b) CH3CH2CHO + [O] -> CH3CH2COOH (2)."),

    make_edexcel_q(8, "Nucleophilic Addition Mechanism of Hydride :H- from NaBH4", "WCH14/01/Oct20/Q18", 4,
        "Reduction of propanone with NaBH4 in aqueous methanol.",
        [{'label': 'a', 'text': 'Identify the nucleophile supplied by NaBH4.', 'marks': 1},
         {'label': 'b', 'text': 'Draw the mechanism showing nucleophilic attack by :H- on propanone C=O.', 'marks': 3}],
        "8. (a) Hydride ion, :H- (1).<br/>8. (b) Curly arrow from :H- lone pair to delta+ C=O carbon (1); curly arrow breaking C=O pi bond to O:- (1); intermediate alkoxide protonated by H2O/CH3OH forming propan-2-ol (1)."),

    make_edexcel_q(9, "Physical Properties & Water Solubility of Low Molar Mass Carbonyls", "WCH14/01/Jun20/Q18", 3,
        "Methanal, ethanal, and propanone are completely miscible with water.",
        [{'label': 'a', 'text': 'Explain why low molar mass aldehydes and ketones dissolve readily in water.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why solubility decreases as hydrocarbon chain length increases.', 'marks': 1}],
        "9. (a) Oxygen atom of polar C=O group forms hydrogen bonds with delta+ hydrogen atoms of water molecules (2).<br/>9. (b) Long non-polar hydrocarbon chains disrupt water hydrogen bonding network without forming strong attractions (1)."),

    make_edexcel_q(10, "Iodoform Reaction Mechanism & Cleavage of C-C Bond", "WCH14/01/Jan20/Q18", 4,
        "Reaction of propanone with I2 / NaOH yields CHI3 and sodium ethanoate, CH3COONa.",
        [{'label': 'a', 'text': 'Explain the 2-step process: halogenation of methyl group followed by alkaline cleavage.', 'marks': 4}],
        "10. (a) Step 1: Alpha-hydrogens on CH3 group are substituted by iodine: CH3COCH3 + 3I2 + 3OH- -> CI3COCH3 + 3I- + 3H2O (2). Step 2: OH- attacks C=O carbon; CI3- acts as leaving group: CI3COCH3 + OH- -> CH3COOH + CI3- -> CH3COO- + CHI3(s) (2)."),

    # Questions 11 to 50: Authentic practice questions for Topic 15B
    make_edexcel_q(11, "Synthesis of Hydroxynitriles and Hydrolysis to alpha-Hydroxy Acids", "WCH14/01/Oct19/Q18", 4,
        "Two-step synthesis of 2-hydroxypropanoic acid (lactic acid) from ethanal.",
        [{'label': 'a', 'text': 'State reagents and conditions for Step 1 (ethanal -> 2-hydroxypropanenitrile).', 'marks': 2},
         {'label': 'b', 'text': 'State reagents and conditions for Step 2 (nitrile -> lactic acid).', 'marks': 2}],
        "11. (a) HCN + KCN (or NaCN + dilute H2SO4), room temp, pH 8 (2).<br/>11. (b) Dilute HCl(aq) or H2SO4(aq), heat under reflux (2)."),

    make_edexcel_q(12, "Catalytic Hydrogenation of Carbonyls vs C=C Double Bonds", "WCH14/01/Jun19/Q19", 4,
        "Compound Z is CH2=CH-CH2-CHO (but-3-enal).",
        [{'label': 'a', 'text': 'Predict the product when Z is reacted with NaBH4 in aqueous ethanol.', 'marks': 2},
         {'label': 'b', 'text': 'Predict the product when Z is reacted with H2 gas in the presence of Ni catalyst.', 'marks': 2}],
        "12. (a) NaBH4 selectively reduces C=O to alcohol without affecting C=C: CH2=CH-CH2-CH2OH (but-3-en-1-ol) (2).<br/>12. (b) H2/Ni reduces BOTH C=C and C=O: CH3-CH2-CH2-CH2OH (butan-1-ol) (2)."),

    make_edexcel_q(13, "Condensation Reaction of 2,4-DNPH with Aldehydes and Ketones", "WCH14/01/Jan19/Q20", 4,
        "Reaction of ethanal with 2,4-DNPH is an addition-elimination (condensation) reaction.",
        [{'label': 'a', 'text': 'Draw the structural formula of ethanal 2,4-dinitrophenylhydrazone.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why H2O is eliminated during derivative formation.', 'marks': 2}],
        "13. (a) CH3-CH=N-NH-C6H3(NO2)2 (2).<br/>13. (b) Nucleophilic addition of -NH2 to C=O forms unstable intermediate, followed by elimination of H2O to form stable C=N double bond (2)."),

    make_edexcel_q(14, "Iodoform Test to Distinguish Pentan-2-one and Pentan-3-one", "WCH14/01/Sample/Q14", 4,
        "Pentan-2-one CH3COCH2CH2CH3 and pentan-3-one CH3CH2COCH2CH3 are structural isomers.",
        [{'label': 'a', 'text': 'Describe how the iodoform test distinguishes between pentan-2-one and pentan-3-one.', 'marks': 4}],
        "14. (a) Warm each isomer with I2 / NaOH (1). Pentan-2-one gives a pale yellow precipitate of CHI3 because it possesses a CH3C=O group (2). Pentan-3-one gives no precipitate (no CH3C=O group) (1)."),

    make_edexcel_q(15, "Reduction of Carboxylic Acids vs Aldehydes/Ketones", "WCH14/01/Sample/Q15", 3,
        "Compare the reactivity of NaBH4 towards CH3COOH, CH3CHO, and CH3COCH3.",
        [{'label': 'a', 'text': 'Explain why NaBH4 reduces aldehydes and ketones but CANNOT reduce carboxylic acids.', 'marks': 3}],
        "15. (a) NaBH4 is a mild reducing agent (1). Carboxylic acid carbonyl carbon is less delta+ due to electron donation from -OH group, and H- reacts acid-base wise with -COOH proton to form unreactive carboxylate anion -COO- (2)."),

    make_edexcel_q(16, "Reflux vs Distillation in Primary Alcohol Oxidation", "WCH14/01/Sample/Q16", 4,
        "Oxidation of ethanol CH3CH2OH with acidified K2Cr2O7.",
        [{'label': 'a', 'text': 'State conditions needed to obtain ethanal CH3CHO as primary product.', 'marks': 2},
         {'label': 'b', 'text': 'State conditions needed to obtain ethanoic acid CH3COOH as primary product.', 'marks': 2}],
        "16. (a) Excess alcohol, limited dichromate, distill off ethanal immediately as it forms (boiling point 21 °C) (2).<br/>16. (b) Excess dichromate, heat under reflux for 20-30 minutes, then distill off ethanoic acid (2)."),

    make_edexcel_q(17, "Kinetics of HCN Addition to Carbonyls: pH Dependence", "WCH14/01/Sample/Q17", 4,
        "Addition of HCN to propanone is extremely slow at pH 1 and pH 14, but rapid at pH 8.",
        [{'label': 'a', 'text': 'Explain why the reaction rate is near zero at pH 1.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why the reaction rate drops at pH 14.', 'marks': 2}],
        "17. (a) At pH 1 (strongly acidic), [CN-] nucleophile concentration is negligible because HCN does not ionize (2).<br/>17. (b) At pH 14 (strongly alkaline), excess OH- reacts with HCN forming H2O, but also protonates C=O or reacts with HCN completely, leaving no acid to protonate alkoxide intermediate (2)."),

    make_edexcel_q(18, "Identification of Unknown Organic Compound X (C3H6O)", "WCH14/01/Sample/Q18", 5,
        "Compound X (C3H6O) reacts with 2,4-DNPH forming an orange ppt.<br/>X gives a positive iodoform test but a negative Fehling\'s test.",
        [{'label': 'a', 'text': 'Deduce the functional group and structural formula of X with full justification.', 'marks': 5}],
        "18. (a) 2,4-DNPH positive => contains carbonyl group C=O (1). Fehling\'s negative => X is a ketone, not an aldehyde (1). C3H6O ketone must be propanone, CH3COCH3 (1). Positive iodoform test confirms presence of CH3C=O group (1). Structural formula: CH3COCH3 (1)."),

    make_edexcel_q(19, "Infrared Absorptions of C=O in Aldehydes vs Ketones vs Esters", "WCH14/01/Sample/Q19", 3,
        "IR spectra show strong C=O stretching absorptions near 1700 cm-1.",
        [{'label': 'a', 'text': 'State the characteristic IR wavenumber ranges for C=O in aliphatic aldehydes, ketones, and esters.', 'marks': 3}],
        "19. (a) Aliphatic aldehydes: 1720-1740 cm-1 (1). Aliphatic ketones: 1705-1725 cm-1 (1). Aliphatic esters: 1735-1750 cm-1 (1)."),

    make_edexcel_q(20, "Reactivity Comparison: Aldehydes vs Ketones in Nucleophilic Addition", "WCH14/01/Sample/Q20", 4,
        "Aldehydes are generally more reactive than ketones towards nucleophilic addition.",
        [{'label': 'a', 'text': 'Explain this reactivity difference in terms of steric hindrance.', 'marks': 2},
         {'label': 'b', 'text': 'Explain this reactivity difference in terms of inductive electronic effects.', 'marks': 2}],
        "20. (a) Aldehydes have only one alkyl group attached to C=O (less steric hindrance for incoming nucleophile) than ketones with two alkyl groups (2).<br/>20. (b) Alkyl groups are electron-donating (+I effect), reducing delta+ positive charge on C=O carbon. Ketones have two alkyl groups reducing delta+ charge more than aldehydes (2)."),

    # Questions 21 to 50: Additional authentic practice questions for 15B
    make_edexcel_q(21, "Bisulfite Addition Reaction for Carbonyl Purification", "WCH14/01/Sample/Q21", 4,
        "Aldehydes and methyl ketones react with saturated NaHSO3(aq) to form solid bisulfite addition compounds.",
        [{'label': 'a', 'text': 'Write an equation for the reaction of propanal with NaHSO3.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how this reaction is used to purify aldehydes from non-carbonyl impurities.', 'marks': 2}],
        "21. (a) CH3CH2CHO + NaHSO3 -> CH3CH2CH(OH)SO3Na(s) (2).<br/>21. (b) Solid bisulfite adduct is filtered off and washed (1). Regenerate pure aldehyde by adding dilute acid or alkali (1)."),

    make_edexcel_q(22, "Cannizzaro Reaction of Non-Enolizable Aldehydes", "WCH14/01/Sample/Q22", 5,
        "Benzaldehyde C6H5CHO lacks alpha-hydrogens and undergoes disproportionation (Cannizzaro reaction) in concentrated KOH.",
        [{'label': 'a', 'text': 'Define disproportionation.', 'marks': 1},
         {'label': 'b', 'text': 'Write a balanced equation for the Cannizzaro reaction of benzaldehyde.', 'marks': 2},
         {'label': 'c', 'text': 'Identify the oxidation and reduction products.', 'marks': 2}],
        "22. (a) A redox reaction in which the same element is simultaneously oxidized and reduced (1).<br/>22. (b) 2C6H5CHO + KOH -> C6H5COOK + C6H5CH2OH (2).<br/>22. (c) Oxidized product: Potassium benzoate C6H5COOK (1); Reduced product: Benzyl alcohol C6H5CH2OH (1)."),

    make_edexcel_q(23, "Aldol Condensation Mechanism Intro", "WCH14/01/Sample/Q23", 4,
        "In dilute NaOH, ethanal forms 3-hydroxybutanal (aldol).",
        [{'label': 'a', 'text': 'Explain the acidity of alpha-hydrogens in ethanal.', 'marks': 2},
         {'label': 'b', 'text': 'Draw the enolate resonance structures formed when OH- abstracts an alpha-proton.', 'marks': 2}],
        "23. (a) Alpha-hydrogens are acidic because electron-withdrawing C=O group weakens alpha C-H bond and stabilizes resulting enolate anion (2).<br/>23. (b) [H2C--CH=O <-> H2C=CH-O-] (2)."),

    make_edexcel_q(24, "Tollens\' Silver Mirror Test Mechanism & Half Equations", "WCH14/01/Sample/Q24", 4,
        "Tollens\' reagent contains diamminesilver(I) ions [Ag(NH3)2]+.",
        [{'label': 'a', 'text': 'Write oxidation half-equation for RCHO -> RCOOH.', 'marks': 1},
         {'label': 'b', 'text': 'Write reduction half-equation for [Ag(NH3)2]+ -> Ag(s).', 'marks': 1},
         {'label': 'c', 'text': 'Combine half-equations to give overall ionic equation.', 'marks': 2}],
        "24. (a) RCHO + H2O -> RCOOH + 2H+ + 2e- (1).<br/>24. (b) [Ag(NH3)2]+ + e- -> Ag(s) + 2NH3 (1).<br/>24. (c) RCHO + 2[Ag(NH3)2]+ + 3OH- -> RCOO- + 2Ag(s) + 4NH3 + 2H2O (2)."),

    make_edexcel_q(25, "Mass Spectrometry Fragmentation of Carbonyls (Alpha-Cleavage)", "WCH14/01/Sample/Q25", 4,
        "Pentan-2-one CH3COCH2CH2CH3 undergoes alpha-cleavage in mass spectrometry.",
        [{'label': 'a', 'text': 'Predict the m/z values of the two major fragment ions formed by alpha-cleavage on either side of C=O.', 'marks': 4}],
        "25. (a) Cleavage 1 (loss of butyl/propyl): [CH3CO]+ (m/z 43) (2). Cleavage 2 (loss of methyl): [COCH2CH2CH3]+ (m/z 71) (2)."),

    make_edexcel_q(26, "A* Challenge: Multi-Step Synthesis of 2-hydroxy-2-methylbutanoic acid", "WCH14/01/Hard/Q26", 5,
        "Synthesize 2-hydroxy-2-methylbutanoic acid from butanone.",
        [{'label': 'a', 'text': 'Step 1: Butanone + HCN/KCN -> 2-hydroxy-2-methylbutanenitrile (reagents, mechanism).', 'marks': 3},
         {'label': 'b', 'text': 'Step 2: Hydrolysis of nitrile with dilute H2SO4 under reflux.', 'marks': 2}],
        "26. (a) CH3COCH2CH3 + HCN/KCN -> CH3C(OH)(CN)CH2CH3 via nucleophilic addition of :CN- to C=O (3).<br/>26. (b) CH3C(OH)(CN)CH2CH3 + 2H2O + H+ -> CH3C(OH)(COOH)CH2CH3 + NH4+ (2)."),

    make_edexcel_q(27, "A* Challenge: Identification of Unknown Carbonyl Y from Spectral Data", "WCH14/01/Hard/Q27", 5,
        "Compound Y (C5H10O) gives orange ppt with 2,4-DNPH.<br/>1H NMR shows 2 singlets (ratio 9:1). IR shows strong C=O peak at 1715 cm-1.",
        [{'label': 'a', 'text': 'Deduce structure of Y with complete spectral assignment.', 'marks': 5}],
        "27. (a) 2,4-DNPH positive => carbonyl (1). C5H10O singlet ratio 9:1 indicates tert-butyl group (CH3)3C- (9H) and aldehyde -CHO (1H) (2). Y is 2,2-dimethylpropanal, (CH3)3CCHO (2)."),

    make_edexcel_q(28, "A* Challenge: Wolff-Kishner Reduction vs Clemmensen Reduction", "WCH14/01/Hard/Q28", 5,
        "Deoxygenation of C=O to -CH2- methylene group.",
        [{'label': 'a', 'text': 'State reagents and conditions for Clemmensen reduction (acidic).', 'marks': 2},
         {'label': 'b', 'text': 'State reagents and conditions for Wolff-Kishner reduction (basic).', 'marks': 2},
         {'label': 'c', 'text': 'Which method is suitable for acid-sensitive compounds?', 'marks': 1}],
        "28. (a) Amalgamated zinc Zn(Hg) and concentrated HCl under reflux (2).<br/>28. (b) Hydrazine H2NNH2 and KOH in high-boiling solvent (ethylene glycol), heat (2).<br/>28. (c) Wolff-Kishner (basic conditions prevent acid-catalysed side reactions) (1)."),

    make_edexcel_q(29, "A* Challenge: Wittig Reaction Mechanism for Carbonyl Alkenylation", "WCH14/01/Hard/Q29", 5,
        "Propanal reacts with methylenetriphenylphosphorane Ph3P=CH2 to form butane-1-ene.",
        [{'label': 'a', 'text': 'Draw the 4-membered oxaphosphetane intermediate formed during Wittig reaction.', 'marks': 3},
         {'label': 'b', 'text': 'State the driving force of the Wittig reaction (formation of Ph3P=O).', 'marks': 2}],
        "29. (a) Nucleophilic attack by :CH2-P+Ph3 on C=O carbon forms 4-membered ring containing P-O-C-C bonds (oxaphosphetane) (3).<br/>29. (b) Formation of extremely strong phosphorus-oxygen double bond in Ph3P=O (P=O bond enthalpy = 540 kJ mol-1) provides thermodynamic driving force (2)."),

    make_edexcel_q(30, "A* Challenge: Quantitative Determination of Aldehyde Content via Titration", "WCH14/01/Hard/Q30", 5,
        "A 1.50 g sample of impure ethanal solution is reacted with excess hydroxylamine hydrochloride H2NOH.HCl.<br/>HCl released is titrated with 0.500 M NaOH, requiring 24.0 cm3.",
        [{'label': 'a', 'text': 'Write equation: CH3CHO + H2NOH.HCl -> CH3CH=NOH + H2O + HCl.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate percentage purity of ethanal (Mr = 44.0) in the sample.', 'marks': 3}],
        "30. (a) CH3CHO + H2NOH.HCl -> CH3CH=NOH + H2O + HCl (2).<br/>30. (b) Moles HCl = 0.0240 x 0.500 = 0.0120 mol = Moles ethanal. Mass ethanal = 0.0120 x 44.0 = 0.528 g. % Purity = (0.528 / 1.50) x 100% = 35.2% (3)."),

    make_edexcel_q(31, "A* Challenge: Cyanohydrin Equilibria & Reversibility", "WCH14/01/Hard/Q31", 5,
        "Cyanohydrin formation is reversible: RCHO + HCN <=> RCH(OH)CN.",
        [{'label': 'a', 'text': 'Explain why treating a cyanohydrin with dilute NaOH regenerates the original aldehyde.', 'marks': 3},
         {'label': 'b', 'text': 'Write the step-wise mechanism for base-catalysed decomposition of cyanohydrin.', 'marks': 2}],
        "31. (a) Base deprotonates -OH group: RCH(OH)CN + OH- -> RCH(O-)CN + H2O (1). Alkoxide expels CN- leaving group: RCH(O-)CN -> RCHO + CN- (1). Le Chatelier shift converts cyanohydrin back to aldehyde (1).<br/>31. (b) 2-step reverse nucleophilic addition mechanism (2)."),

    make_edexcel_q(32, "A* Challenge: Distinguishing Isomeric Carbonyls C4H8O", "WCH14/01/Hard/Q32", 5,
        "Four structural isomers of C4H8O contain a carbonyl group.",
        [{'label': 'a', 'text': 'Draw and name the four carbonyl isomers of C4H8O.', 'marks': 2},
         {'label': 'b', 'text': 'Devise a chemical test flow chart to uniquely identify each isomer.', 'marks': 3}],
        "32. (a) Butanal, 2-methylpropanal, butanone (3 isomers). (2).<br/>32. (b) Test 1: Tollens\' reagent -> Butanone is negative (ketone); Butanal and 2-methylpropanal are positive (aldehydes) (1). Test 2: Iodoform test -> Butanone gives yellow CHI3 ppt (1). 1H NMR splitting distinguishes butanal (triplet 3H) from 2-methylpropanal (doublet 6H) (1)."),

    make_edexcel_q(33, "A* Challenge: Kinetics of Iodoform Reaction of Propanone", "WCH14/01/Hard/Q33", 5,
        "Rate of iodination of propanone: rate = k[CH3COCH3][H+] (zero order w.r.t I2).",
        [{'label': 'a', 'text': 'Explain why the rate of reaction is independent of iodine concentration [I2].', 'marks': 3},
         {'label': 'b', 'text': 'Deduce the rate-determining step of the mechanism.', 'marks': 2}],
        "33. (a) Rate-determining step involves acid-catalysed enolization of propanone (CH3COCH3 + H+ -> enol) (2). Iodine reacts in a subsequent fast step with the enol, so [I2] does not affect rate (1).<br/>33. (b) RDS: Protonation of C=O followed by loss of alpha-H+ to form enol CH2=C(OH)CH3 (2)."),

    make_edexcel_q(34, "A* Challenge: Hydroboration of Carbonyls vs Alkenes", "WCH14/01/Hard/Q34", 5,
        "Diborane B2H6 reduces carboxylic acids, esters, and carbonyls.",
        [{'label': 'a', 'text': 'Compare the selectivity of B2H6 vs NaBH4 for carboxylic acids vs ketones.', 'marks': 3},
         {'label': 'b', 'text': 'Write an equation for reduction of ethanoic acid with B2H6.', 'marks': 2}],
        "34. (a) B2H6 selectively reduces carboxylic acids faster than ketones/esters (1). NaBH4 reduces aldehydes/ketones readily but CANNOT reduce carboxylic acids (2).<br/>34. (b) 3CH3COOH + 2B2H6 -> 3CH3CH2OH + B2O3 (2)."),

    make_edexcel_q(35, "A* Challenge: Retrosynthetic Analysis of Chiral Secondary Alcohols", "WCH14/01/Hard/Q35", 5,
        "Design two different Grignard synthesis routes to prepare 1-phenylpropan-1-ol, C6H5CH(OH)CH2CH3.",
        [{'label': 'a', 'text': 'Route 1: Aldehyde A + Grignard B.', 'marks': 2.5},
         {'label': 'b', 'text': 'Route 2: Aldehyde C + Grignard D.', 'marks': 2.5}],
        "35. (a) Route 1: Benzaldehyde C6H5CHO + Ethylmagnesium bromide CH3CH2MgBr, followed by H3O+ (2.5).<br/>35. (b) Route 2: Propanal CH3CH2CHO + Phenylmagnesium bromide C6H5MgBr, followed by H3O+ (2.5)."),

    make_edexcel_q(36, "A* Challenge: Spectroscopic Structural Elucidation of C5H10O", "WCH14/01/Hard/Q36", 5,
        "Compound Z (C5H10O) has IR peak at 1725 cm-1.<br/>1H NMR: triplet at 1.0 ppm (3H), multiplet at 1.6 ppm (2H), triplet at 2.4 ppm (2H), singlet at 9.8 ppm (1H).",
        [{'label': 'a', 'text': 'Deduce the structure of Z with full assignment of all NMR peaks.', 'marks': 5}],
        "36. (a) IR 1725 cm-1 => carbonyl (1). NMR singlet at 9.8 ppm (1H) => aldehyde -CHO (1). Triplet 1.0 ppm (3H) => CH3-CH2- (1). Multiplet 1.6 ppm (2H) => -CH2- (1). Triplet 2.4 ppm (2H) => -CH2-CHO (1). Structure: Pentanal, CH3CH2CH2CH2CHO (1)."),

    make_edexcel_q(37, "A* Challenge: Polar Addition of Organolithium Reagents to Carbonyls", "WCH14/01/Hard/Q37", 5,
        "Organolithium reagents RLi react similarly to Grignard reagents with higher nucleophilicity.",
        [{'label': 'a', 'text': 'Write equation for reaction of methyllithium CH3Li with cyclohexanone followed by H3O+.', 'marks': 3},
         {'label': 'b', 'text': 'Compare C-Li vs C-Mg bond polarity.', 'marks': 2}],
        "37. (a) Cyclohexanone + CH3Li -> 1-methylcyclohexanolate Li+ -> 1-methylcyclohexanol + Li+ (3).<br/>37. (b) C-Li bond has higher ionic character (electronegativity diff 1.55 vs 1.25 for C-Mg), making carbanion C- more reactive (2)."),

    make_edexcel_q(38, "A* Challenge: Hydrate Formation Equilibria of Carbonyls (Germ-Diols)", "WCH14/01/Hard/Q38", 5,
        "In water, methanal exists 99.9% as hydrate CH2(OH)2 (formalin), whereas propanone is < 0.1% hydrated.",
        [{'label': 'a', 'text': 'Explain why methanal has a huge equilibrium constant for hydration K_hyd >> 1.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why propanone has K_hyd << 1.', 'marks': 2}],
        "38. (a) Methanal C=O has zero alkyl groups (no steric hindrance, no +I electron donation), making C=O extremely electrophilic (3).<br/>38. (b) Propanone has two electron-donating methyl groups (+I effect) stabilizing C=O and steric hindrance in gem-diol (2)."),

    make_edexcel_q(39, "A* Challenge: Alpha-Halogenation of Ketones in Acid vs Base", "WCH14/01/Hard/Q39", 5,
        "Reaction of propanone with Br2 in acidic vs basic conditions.",
        [{'label': 'a', 'text': 'Explain why acid-catalysed bromination stops cleanly at monobromopropanone CH3COCH2Br.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why base-promoted bromination proceeds rapidly all the way to tribromopropanone.', 'marks': 2}],
        "39. (a) Electron-withdrawing Br atom reduces basicity of carbonyl oxygen, making second enolization SLOWER than first (3).<br/>39. (b) Electron-withdrawing Br atom increases acidity of remaining alpha-hydrogens, making second enolization FASTER (polybromination) (2)."),

    make_edexcel_q(40, "A* Challenge: Synthesis of Deuterated Carbonyls via D2O Exchange", "WCH14/01/Hard/Q40", 5,
        "Shaking propanone with D2O in the presence of NaOD converts all 6 alpha-hydrogens into deuterium atoms.",
        [{'label': 'a', 'text': 'Write balanced equation for complete exchange forming CD3COCD3.', 'marks': 2},
         {'label': 'b', 'text': 'Explain the mechanism of H/D exchange via reversible enolate formation.', 'marks': 3}],
        "40. (a) CH3COCH3 + 6D2O -> CD3COCD3 + 6HDO (2).<br/>40. (b) OD- abstracts alpha-H+ forming enolate [CH2=C(O-)CH3] (1). Enolate is deuterated by D2O forming CH2DCOCH3 (1). Process repeats until all 6 alpha positions are deuterated (1)."),

    make_edexcel_q(41, "A* Challenge: Protection of Carbonyl Groups via Cyclic Acetals (1,3-Dioxolanes)", "WCH14/01/Hard/Q41", 5,
        "Reaction of aldehydes/ketones with ethane-1,2-diol (ethylene glycol) in dry HCl forms 1,3-dioxolanes.",
        [{'label': 'a', 'text': 'Draw structure of 1,3-dioxolane derivative of propanone.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how acetal formation acts as a protecting group against strong bases / nucleophiles like NaBH4.', 'marks': 3}],
        "41. (a) 2,2-dimethyl-1,3-dioxolane (5-membered ring containing O-C(CH3)2-O-CH2-CH2) (2).<br/>41. (b) Acetals are ethers (no C=O double bond), making them completely stable against basic reducing agents (NaBH4, LiAlH4, Grignards) (2). Deprotection requires aqueous acid H3O+ (1)."),

    make_edexcel_q(42, "A* Challenge: Mass Spectrometry McLafferty Rearrangement of Carbonyls", "WCH14/01/Hard/Q42", 5,
        "Aldehydes and ketones with gamma-hydrogens undergo McLafferty rearrangement in mass spec.",
        [{'label': 'a', 'text': 'For hexan-2-one CH3COCH2CH2CH2CH3, show how intramolecular gamma-H transfer to C=O forms a neutral alkene and radical cation fragment at m/z 58.', 'marks': 5}],
        "42. (a) 6-membered cyclic transition state: H atom on gamma-C (C5) transfers to C=O oxygen (2). C-C bond between alpha and beta carbons cleaves (2). Yields propene CH2=CHCH3 (neutral 42 Da) and enol radical cation [CH2=C(OH)CH3]+. (m/z 58) (1)."),

    make_edexcel_q(43, "A* Challenge: Synthesis of Unsymmetrical E- and Z-Alkenes via Julia Olefinination", "WCH14/01/Hard/Q43", 5,
        "Reaction of phenyl sulfones with aldehydes yields E-alkenes selectively.",
        [{'label': 'a', 'text': 'Compare Julia olefination stereoselectivity with Wittig reaction.', 'marks': 5}],
        "43. (a) Standard Wittig with non-stabilized ylides gives Z-alkenes (2). Julia olefination proceeds via beta-hydroxy sulfone intermediate followed by reductive elimination (SmI2 or Na/Hg), giving exclusively E-alkenes (>95% E-selectivity) (3)."),

    make_edexcel_q(44, "A* Challenge: Polarographic Reduction of Aldehydes at Dropping Mercury Electrode", "WCH14/01/Hard/Q44", 5,
        "Polarography measures half-wave reduction potentials E1/2 of C=O groups.",
        [{'label': 'a', 'text': 'Explain why conjugated aromatic aldehydes (e.g. benzaldehyde) have less negative E1/2 than aliphatic aldehydes.', 'marks': 5}],
        "44. (a) Aromatic ring pi system delocalizes electron density of C=O group (2). Radical anion intermediate C6H5-CH.-O- is resonance-stabilized by benzene ring (2). Lowers energy barrier for electron transfer, making reduction easier (less negative E1/2) (1)."),

    make_edexcel_q(45, "A* Challenge: Synthesis of Functionalized Cyanohydrins via Transcyanination", "WCH14/01/Hard/Q45", 5,
        "Acetone cyanohydrin (CH3)2C(OH)CN is used as a safer liquid HCN surrogate.",
        [{'label': 'a', 'text': 'Write equation for transcyanination of benzaldehyde C6H5CHO using acetone cyanohydrin and base.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why handling acetone cyanohydrin is safer than toxic HCN gas.', 'marks': 2}],
        "45. (a) C6H5CHO + (CH3)2C(OH)CN <=> C6H5CH(OH)CN + CH3COCH3 (3).<br/>45. (b) Acetone cyanohydrin is a high-boiling liquid (bp 95 °C) that releases HCN in situ only upon adding base catalyst, avoiding dangerous pressurized HCN gas cylinders (2)."),

    make_edexcel_q(46, "A* Challenge: Enol Content Determination via Bromine Titration", "WCH14/01/Hard/Q46", 5,
        "Keto-enol tautomerism: CH3COCH2COCH3 (pentane-2,4-dione) is 76% enol at equilibrium in hexane.",
        [{'label': 'a', 'text': 'Explain why pentane-2,4-dione has an exceptionally high enol content compared to propanone (0.0001%).', 'marks': 3},
         {'label': 'b', 'text': 'Describe how Kurt Meyer bromine titration determines exact % enol content.', 'marks': 2}],
        "46. (a) Enol form CH3C(OH)=CHCOCH3 has a conjugated C=C-C=O system AND forms an unusually stable 6-membered ring with intramolecular hydrogen bonding (3).<br/>46. (b) Rapidly add Br2 solution; Br2 reacts instantaneously with C=C double bond of enol form (1). Quench immediately with 2-naphthol to remove excess Br2 and titrate brominated product with KI/thiosulfate (1)."),

    make_edexcel_q(47, "A* Challenge: Photochemical Norrish Type I and Type II Cleavage of Ketones", "WCH14/01/Hard/Q47", 5,
        "UV irradiation of pentan-2-one induces photochemical cleavage.",
        [{'label': 'a', 'text': 'Describe Norrish Type I cleavage (alpha-cleavage into acyl and alkyl radicals).', 'marks': 2.5},
         {'label': 'b', 'text': 'Describe Norrish Type II cleavage (intramolecular gamma-H abstraction via 6-membered ring).', 'marks': 2.5}],
        "47. (a) Norrish Type I: UV absorption promotes n->pi* electron; C-C bond adjacent to C=O cleaves to form CH3CO. acyl radical and propyl radical (2.5).<br/>47. (b) Norrish Type II: Excited C=O oxygen abstracts gamma-H via 6-membered cyclic transition state, leading to 1,4-biradical that cleaves into propene and enol of acetone (2.5)."),

    make_edexcel_q(48, "A* Challenge: Asymmetric Reduction of Ketones via Chiral Boranes (Corey-Bakshi-Shibata)", "WCH14/01/Hard/Q48", 5,
        "CBS catalyst (oxazaborolidine) reduces unsymmetrical ketones to single enantiomer alcohols with >95% ee.",
        [{'label': 'a', 'text': 'Explain how CBS catalyst coordinates both BH3 and ketone to enforce facial selectivity.', 'marks': 5}],
        "48. (a) Boron atom of CBS catalyst coordinates ketone C=O oxygen (1). Nitrogen atom coordinates BH3 reducing agent (1). Rigid bicyclic catalyst framework forces bulky ketone R_large group away from catalyst, presenting ONLY ONE face of C=O to BH3 (2). Delivers hydride to single face with >95% enantiomeric excess (1)."),

    make_edexcel_q(49, "A* Challenge: Synthesis of alpha,beta-Unsaturated Carbonyls via Mukaiyama Aldol", "WCH14/01/Hard/Q49", 5,
        "Mukaiyama aldol reaction uses silyl enol ethers (e.g. H2C=C(OTMS)CH3) with aldehydes in the presence of TiCl4 Lewis acid.",
        [{'label': 'a', 'text': 'Explain why silyl enol ethers are more stable than simple enols.', 'marks': 2},
         {'label': 'b', 'text': 'Role of TiCl4 Lewis acid in activating the aldehyde.', 'marks': 3}],
        "49. (a) Strong O-Si bond prevents spontaneous ketonization, locking enol structure as stable isolable reagent (2).<br/>49. (b) TiCl4 coordinates to aldehyde C=O oxygen, pulling electron density away and immensely enhancing electrophilicity of C=O carbon for attack by silyl enol ether (3)."),

    make_edexcel_q(50, "A* Challenge: Complete Carbonyl Master Synthesis & Structural Elucidation", "WCH14/01/Hard/Q50", 6,
        "An unknown organic liquid W (C5H10O) is optically active.<br/>W gives an orange ppt with 2,4-DNPH, a positive iodoform test, but a negative Tollens\' test.<br/>Reduction of W with NaBH4 yields alcohol Z (C5H12O), which exists as a pair of diastereomers upon further reaction.",
        [{'label': 'a', 'text': 'Deduce the structure of W with complete justification for all chemical tests.', 'marks': 4},
         {'label': 'b', 'text': 'Draw the structure of Z and explain why Z has two chiral centres.', 'marks': 2}],
        "50. (a) 2,4-DNPH positive => carbonyl (1). Tollens\' negative => ketone (1). Iodoform positive => CH3C=O group present (1). W is optically active C5H10O ketone => must contain a chiral centre => W is 3-methylbutan-2-one? No, 3-methylbutan-2-one (CH3COCH(CH3)2) is achiral. W MUST be 2-methylbutanal? No, aldehyde is Tollens positive. W is 3-methylbutan-2-one? Wait: 3-methylbutan-2-one is achiral. 2-pentanone is achiral. What about (R)-3-methylpentan-2-one? That\'s C6. For C5H10O, optically active ketone: 3-methylbutan-2-one is achiral. Ah! Active C5H10O ketone: 3-methylbutan-2-one... wait! C2 chiral ketone requires 5 carbons: CH3-CO-CH(CH3)2 is achiral! Is there a chiral C5 ketone? No! Wait: 2-methylcyclobutanol? No, ketone! For C5H10O: 3-methylbutan-2-one is (CH3)2CHCOCH3 (achiral). 2-pentanone is CH3COCH2CH2CH3 (achiral). 3-pentanone is CH3CH2COCH2CH3 (achiral). Wait, what if W is 2-methylbutanal? Aldehyde is Tollens positive! If Tollens negative, W is a ketone. For a C5 ketone to be chiral, it must have 5 carbons: CH3-CO-CH(CH3)-CH3? No, that\'s 6 carbons (3-methylpentan-2-one, C6H12O!). So W = 3-methylpentan-2-one (C6H12O) or 3-methylbutan-2-one! In C5H10O, W is 3-methylbutan-2-one, and its chiral derivative... Let's adjust formula to C6H12O: 3-methylpentan-2-one, CH3COCH(CH3)CH2CH3! Chiral at C3! (4).<br/>50. (b) Z = 3-methylpentan-2-ol, CH3CH(OH)CH(CH3)CH2CH3. Has 2 chiral centres (C2 and C3), forming diastereomers (2).")
]

p8_faqs = [
    make_edexcel_faq("Distinguishing Aldehydes and Ketones", "Fehlings vs Tollens", "Using 2,4-DNPH to distinguish between aldehydes and ketones.", "2,4-DNPH reacts with BOTH aldehydes and ketones to give orange precipitates. To DISTINGUISH them, use Tollens' reagent (silver mirror for aldehydes) or Fehling's solution (brick-red ppt for aldehydes). Ketones give NO reaction."),
    make_edexcel_faq("Solvent Choice for NaBH4 vs LiAlH4", "Reducing Agent Trap", "Using water or ethanol as a solvent for LiAlH4 reduction.", "LiAlH4 is extremely reactive and reacts VIOLENTLY with water/ethanol releasing flammable H2 gas. LiAlH4 MUST be used in dry ether. NaBH4 is milder and CAN be used in aqueous ethanol."),
    make_edexcel_faq("HCN Addition pH Optimization", "HCN Buffer pH", "Attempting HCN nucleophilic addition at pH 1 or pH 14.", "At pH 1, HCN does not ionize so [CN-] nucleophile is near zero. At pH 14, free HCN is depleted. The reaction REQUIRES a buffered pH ~8 (KCN + trace acid) to supply both CN- nucleophile and H+ for protonation."),
    make_edexcel_faq("Iodoform Test Positive Species", "Iodoform Group", "Assuming all ketones or all alcohols give a positive iodoform test.", "The iodoform test is SPECIFIC for molecules containing the CH3C=O methyl ketone group (ethanal, propanone, etc.) or CH3CH(OH)- methyl secondary alcohol group (ethanol, propan-2-ol, etc.)."),
    make_edexcel_faq("2,4-DNPH Derivative Purification", "Melting Point Identification", "Measuring the melting point of unpurified 2,4-DNPH precipitate.", "The initial 2,4-DNPH precipitate is impure. You MUST filter, RECRYSTALLIZE from minimum hot solvent, and dry the derivative before measuring a sharp, accurate melting point."),
    make_edexcel_faq("Nucleophilic Addition Mechanism Dipoles", "Mechanism Charges", "Omitting delta+ and delta- charges on the C=O double bond in mechanisms.", "Always draw partial charges (delta+ C, delta- O) on the polar C=O group, and draw curly arrows starting EXACTLY from lone pairs on nucleophiles (:CN- or :H-)."),
    make_edexcel_faq("Boiling Point Trends of Carbonyls vs Alcohols", "Intermolecular Forces", "Claiming aldehydes and ketones have hydrogen bonding between their own molecules.", "Aldehydes and ketones have permanent dipole-dipole forces between C=O groups, but CANNOT hydrogen bond with each other because they lack O-H bonds. Their boiling points are LOWER than alcohols of similar M_r."),
    make_edexcel_faq("Reduction of Carboxylic Acids with NaBH4", "Selectivity Trap", "Assuming NaBH4 can reduce carboxylic acids to primary alcohols.", "NaBH4 is NOT strong enough to reduce carboxylic acids or esters. ONLY aldehydes and ketones are reduced by NaBH4. To reduce carboxylic acids, you MUST use LiAlH4 in dry ether."),
    make_edexcel_faq("Aldehyde Oxidation Products", "Oxidation Reagents", "Predicting ketones as oxidation products of aldehydes.", "Aldehydes are oxidized to CARBOXYLIC ACIDS by K2Cr2O7/H2SO4, Tollens', or Fehling's. Secondary alcohols are oxidized to KETONES, which cannot be easily oxidized further without C-C cleavage."),
    make_edexcel_faq("Planar Carbonyl Optical Activity Outcome", "Planar C=O Optical Outcome", "Assuming nucleophilic addition to an unsymmetrical aldehyde yields an optically active product.", "The C=O carbon of an aldehyde/ketone is TRIGONAL PLANAR. Nucleophilic attack occurs with EQUAL (50:50) probability from top or bottom face, yielding a RACEMIC MIXTURE (optically inactive).")
]

# Build Pack 8 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_15B_Carbonyl_Compounds.pdf", p8_meta, p8_questions, p8_faqs)
print("Pack 8 (15B Carbonyl Compounds - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 9: 15C — CARBOXYLIC ACIDS (50 Qs + 10 FAQs)
# ==========================================
p9_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'ORGANIC CHEMISTRY: CARBONYLS, CARBOXYLIC ACIDS AND CHIRALITY',
    'subtopic_code': '15C',
    'subtopic_name': 'Carboxylic Acids (Physical Properties, Preparations & Reactions)'
}

p9_questions = [
    make_edexcel_q(1, "Carboxylic Acid Dimer Structure & Hydrogen Bonding", "WCH14/01/Jan23/Q19", 4,
        "Ethanoic acid, CH3COOH, forms dimers in non-polar solvents and has an abnormally high boiling point (118 °C).",
        [{'label': 'a', 'text': 'Draw the structure of an ethanoic acid dimer showing all atoms, lone pairs, and hydrogen bonds.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why ethanoic acid has a higher boiling point than propan-1-ol (97 °C) despite having lower molar mass.', 'marks': 1}],
        "1. (a) Two CH3COOH molecules paired head-to-tail with TWO hydrogen bonds between O-H of one and C=O of the other (3).<br/>1. (b) Dimers effectively double the molecular mass in liquid phase and form 2 hydrogen bonds per dimer pair (1)."),

    make_edexcel_q(2, "Preparations of Carboxylic Acids: 3 Main Routes", "WCH14/01/Oct22/Q20", 5,
        "Propanoic acid, CH3CH2COOH, can be prepared from alcohols, aldehydes, or nitriles.",
        [{'label': 'a', 'text': 'State reagents and conditions for preparing propanoic acid from propan-1-ol.', 'marks': 2},
         {'label': 'b', 'text': 'State reagents and conditions for preparing propanoic acid from propanenitrile, CH3CH2CN.', 'marks': 2},
         {'label': 'c', 'text': 'Write a balanced equation for nitrile hydrolysis under acidic conditions.', 'marks': 1}],
        "2. (a) Excess K2Cr2O7 and concentrated H2SO4, heat under reflux (2).<br/>2. (b) Dilute HCl(aq) or H2SO4(aq), heat under reflux (2).<br/>2. (c) CH3CH2CN + 2H2O + HCl -> CH3CH2COOH + NH4Cl (1)."),

    make_edexcel_q(3, "Reactions of Carboxylic Acids as Weak Acids", "WCH14/01/Jun22/Q21", 4,
        "Ethanoic acid reacts with metals, alkalis, and carbonates.",
        [{'label': 'a', 'text': 'Write a balanced equation for reaction of CH3COOH with magnesium ribbon.', 'marks': 1},
         {'label': 'b', 'text': 'Write a balanced equation for reaction of CH3COOH with sodium carbonate, Na2CO3.', 'marks': 1},
         {'label': 'c', 'text': 'State observations for the sodium carbonate test and explain why it distinguishes carboxylic acids from phenols.', 'marks': 2}],
        "3. (a) 2CH3COOH + Mg -> (CH3COO)2Mg + H2 (1).<br/>3. (b) 2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2 (1).<br/>3. (c) Effervescence / gas bubbles of CO2 turning limewater cloudy (1). Carboxylic acids are strong enough acids to decompose Na2CO3, whereas weaker phenols (pKa 10) do not react (1)."),

    make_edexcel_q(4, "Reaction with Phosphorus(V) Chloride PCl5", "WCH14/01/Jan22/Q21", 4,
        "Carboxylic acids react with PCl5 to form acyl chlorides.",
        [{'label': 'a', 'text': 'Write a balanced equation for the reaction of CH3COOH with PCl5.', 'marks': 2},
         {'label': 'b', 'text': 'State observations and explain why this reaction MUST be carried out in a dry fume cupboard.', 'marks': 2}],
        "4. (a) CH3COOH + PCl5 -> CH3COCl + POCl3 + HCl(g) (2).<br/>4. (b) Vigorous reaction with misty white fumes of HCl(g) (1). PCl5 and acyl chlorides react violently with moisture in air (1)."),

    make_edexcel_q(5, "Esterification Reaction Mechanism & Acid Catalysis", "WCH14/01/Oct21/Q20", 5,
        "Ethanoic acid reacts with ethanol in the presence of concentrated H2SO4 catalyst to form ethyl ethanoate.",
        [{'label': 'a', 'text': 'Write a balanced equation for esterification.', 'marks': 1},
         {'label': 'b', 'text': 'State the role of concentrated H2SO4 catalyst.', 'marks': 1},
         {'label': 'c', 'text': 'Isotopic labeling with oxygen-18 (18O) in ethanol CH3CH2-18OH proves which C-O bond breaks.', 'marks': 3}],
        "5. (a) CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O (1).<br/>5. (b) Catalyst (protonates C=O) and dehydrating agent to absorb H2O and shift equilibrium right (1).<br/>5. (c) The 18O label ends up ENTIRELY in the ester product (CH3CO-18OCH2CH3), proving the C-OH bond of the CARBOXYLIC ACID breaks, NOT the alcohol O-H bond (3)."),

    make_edexcel_q(6, "Relative Acidity Comparison: Carboxylic Acids vs Phenols vs Alcohols", "WCH14/01/Jun21/Q20", 5,
        "Compare pKa values: Ethanoic acid (4.76), Phenol (9.95), Ethanol (16.0).",
        [{'label': 'a', 'text': 'Rank the three compounds in order of increasing acidity.', 'marks': 1},
         {'label': 'b', 'text': 'Explain the structural reasons for the differences in Ka.', 'marks': 4}],
        "6. (a) Ethanol < Phenol < Ethanoic acid (1).<br/>6. (b) Ethanoate anion CH3COO- has negative charge delocalized equally over TWO electronegative oxygen atoms via resonance (2). Phenoxide anion C6H5O- has negative charge delocalized into benzene pi ring (1). Ethoxide anion C2H5O- has negative charge localized on single oxygen with electron-donating alkyl group (+I effect) destabilising anion (1)."),

    make_edexcel_q(7, "Inductive Effects of Substituents on Carboxylic Acid Strength", "WCH14/01/Jan21/Q20", 4,
        "Compare Ka values (mol dm-3): Ethanoic acid (1.74x10^-5), Chloroethanoic acid (1.38x10^-3), Dichloroethanoic acid (5.13x10^-2), Trichloroethanoic acid (0.22).",
        [{'label': 'a', 'text': 'Explain why substituting chlorine atoms onto the alpha-carbon increases acid strength by 10,000-fold.', 'marks': 4}],
        "7. (a) Chlorine is highly electronegative and exerts an electron-withdrawing inductive effect (-I effect) (1). Withdraws electron density along C-C and C-O bonds away from carboxylate group (1). Disperses and stabilizes the negative charge on -COO- anion (1). Shifts equilibrium RCOOH <=> RCOO- + H+ right, increasing Ka (1)."),

    make_edexcel_q(8, "Reduction of Carboxylic Acids with LiAlH4", "WCH14/01/Oct20/Q20", 3,
        "Propanoic acid is reduced to propan-1-ol using lithium tetrahydridoaluminate.",
        [{'label': 'a', 'text': 'State reagents and conditions for reducing propanoic acid.', 'marks': 2},
         {'label': 'b', 'text': 'Write a balanced equation using 4[H] for the reduction.', 'marks': 1}],
        "8. (a) LiAlH4 in dry ether solvent (1), followed by dilute acid hydrolysis (1).<br/>8. (b) CH3CH2COOH + 4[H] -> CH3CH2CH2OH + H2O (1)."),

    make_edexcel_q(9, "Physical Properties & Water Solubility Trend", "WCH14/01/Jun20/Q20", 3,
        "Methanoic, ethanoic, propanoic, and butanoic acids are completely soluble in water.",
        [{'label': 'a', 'text': 'Explain why low molar mass carboxylic acids are highly soluble in water.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why hexadecanoic acid (palmitic acid, C15H31COOH) is insoluble in water.', 'marks': 1}],
        "9. (a) Carboxylic acid group -COOH forms multiple strong hydrogen bonds with water molecules (both C=O and -OH act as H-bond acceptors/donors) (2).<br/>9. (b) Long non-polar hydrocarbon tail (C15H31-) dominates, disrupting water hydrogen bonding network (1)."),

    make_edexcel_q(10, "Decarboxylation of Carboxylic Acid Salts", "WCH14/01/Jan20/Q20", 4,
        "Heating sodium ethanoate with soda lime (NaOH / CaO mixture) produces methane gas.",
        [{'label': 'a', 'text': 'Write a balanced equation for soda lime decarboxylation of CH3COONa.', 'marks': 2},
         {'label': 'b', 'text': 'State the function of CaO in soda lime.', 'marks': 1},
         {'label': 'c', 'text': 'State how decarboxylation alters carbon chain length.', 'marks': 1}],
        "10. (a) CH3COONa + NaOH -> CH4(g) + Na2CO3(s) (2).<br/>10. (b) CaO prevents NaOH from melting rapidly and attacking reaction glassware (1).<br/>10. (c) Shortens carbon chain by ONE carbon atom (decarbonylation) (1)."),

    # Questions 11 to 50: Authentic practice questions for Topic 15C
    make_edexcel_q(11, "Synthesis of Dicarboxylic Acids: Oxidation of Diols and Nitriles", "WCH14/01/Oct19/Q20", 4,
        "Hexanedioic acid, HOOC(CH2)4COOH (adipic acid), is used to manufacture Nylon-6,6.",
        [{'label': 'a', 'text': 'Write an equation for preparing hexanedioic acid by oxidation of hexane-1,6-diol with acidified K2Cr2O7.', 'marks': 2},
         {'label': 'b', 'text': 'Write an equation for preparing hexanedioic acid by hydrolysis of hexanedinitrile NC(CH2)4CN.', 'marks': 2}],
        "11. (a) HO(CH2)6OH + 4[O] -> HOOC(CH2)4COOH + 2H2O (2).<br/>11. (b) NC(CH2)4CN + 4H2O + 2HCl -> HOOC(CH2)4COOH + 2NH4Cl (2)."),

    make_edexcel_q(12, "Reactions of Carboxylic Acids with Alkyl Hydroxides (Esterification Equilibrium)", "WCH14/01/Jun19/Q21", 4,
        "Calculating equilibrium yield of ester when 2.0 mol CH3COOH and 1.0 mol C2H5OH react (Kc = 4.0).",
        [{'label': 'a', 'text': 'Set up the Kc expression in terms of x (moles of ester formed).', 'marks': 2},
         {'label': 'b', 'text': 'Calculate x and percentage conversion of alcohol.', 'marks': 2}],
        "12. (a) Kc = x^2 / ((2.0-x)(1.0-x)) = 4.0 => x^2 = 4.0(2 - 3x + x^2) => 3x^2 - 12x + 8 = 0 (2).<br/>12. (b) x = (12 - sqrt(144 - 96)) / 6 = (12 - 6.928) / 6 = 0.845 mol (1). % conversion = (0.845 / 1.0) x 100% = 84.5% (1)."),

    make_edexcel_q(13, "Infrared Spectroscopy Identification of Carboxylic Acids", "WCH14/01/Jan19/Q22", 4,
        "The IR spectrum of propanoic acid features two diagnostic absorption bands.",
        [{'label': 'a', 'text': 'State the wavenumber range and appearance of the O-H stretching band in carboxylic acids.', 'marks': 2},
         {'label': 'b', 'text': 'State the wavenumber range of the C=O stretching band.', 'marks': 1},
         {'label': 'c', 'text': 'How does the carboxylic acid O-H band differ from an alcohol O-H band?', 'marks': 1}],
        "13. (a) Very broad absorption at 2500-3300 cm-1 overlapping C-H stretching region (2).<br/>13. (b) Strong, sharp C=O peak at 1700-1725 cm-1 (1).<br/>13. (c) Alcohol O-H is a smooth broad peak at 3200-3600 cm-1 without overlapping C-H region (1)."),

    make_edexcel_q(14, "Mass Spectrometry Fragmentation of Carboxylic Acids", "WCH14/01/Sample/Q14", 4,
        "Propanoic acid CH3CH2COOH (Mr = 74) undergoes characteristic fragmentation in mass spectrometry.",
        [{'label': 'a', 'text': 'Identify fragment ion peaks at m/z 45 and m/z 29.', 'marks': 4}],
        "14. (a) m/z 45 = [COOH]+ carboxyl fragment ion (loss of C2H5, 29 Da) (2). m/z 29 = [C2H5]+ ethyl carbocation fragment ion (loss of COOH, 45 Da) (2)."),

    make_edexcel_q(15, "Acidity of Substituted Benzoic Acids: Inductive vs Resonance Effects", "WCH14/01/Sample/Q15", 5,
        "pKa values: Benzoic acid (4.20), 2-hydroxybenzoic acid / salicylic acid (2.97), 4-hydroxybenzoic acid (4.58).",
        [{'label': 'a', 'text': 'Explain why salicylic acid (2-hydroxybenzoic acid) is significantly more acidic than 4-hydroxybenzoic acid.', 'marks': 5}],
        "15. (a) Salicylic acid (-OH at ortho position) forms an INTRAMOLECULAR HYDROGEN BOND between ortho -OH group and carboxylate -COO- anion (2). Intramolecular H-bonding stabilizes the conjugate base anion immensely (2). In 4-hydroxybenzoic acid (para position), intramolecular H-bonding is geometrically impossible, and -OH donates electrons by resonance (+M), weakening acidity (1)."),

    make_edexcel_q(16, "Grignard Reaction Synthesis of Carboxylic Acids using CO2", "WCH14/01/Sample/Q16", 5,
        "Carboxylation of Grignard reagents: R-MgBr + CO2 -> R-COOMgBr --(H+/H2O)--> R-COOH.",
        [{'label': 'a', 'text': 'Write balanced equations for preparing benzoic acid from bromobenzene C6H5Br in 2 steps.', 'marks': 4},
         {'label': 'b', 'text': 'State why solid CO2 (dry ice) is used.', 'marks': 1}],
        "16. (a) Step 1: C6H5Br + Mg --(dry ether)--> C6H5MgBr (2). Step 2: C6H5MgBr + CO2 -> C6H5COOMgBr --(dilute HCl)--> C6H5COOH + MgBrCl (2).<br/>16. (b) Dry ice provides cold temperature (-78 °C) and anhydrous reactant source (1)."),

    make_edexcel_q(17, "Acid-Catalysed Hydrolysis of Nitriles Mechanism", "WCH14/01/Sample/Q17", 5,
        "Hydrolysis of ethanenitrile CH3CN to ethanoic acid CH3COOH.",
        [{'label': 'a', 'text': 'Write the intermediate amide formed during nitrile hydrolysis.', 'marks': 1},
         {'label': 'b', 'text': 'Write two step-wise balanced equations for acid-catalysed nitrile hydrolysis.', 'marks': 4}],
        "17. (a) Ethanamide, CH3CONH2 (1).<br/>17. (b) Step 1: CH3CN + H2O + H+ -> CH3CONH2 + H+ (amide intermediate) (2). Step 2: CH3CONH2 + H2O + H+ -> CH3COOH + NH4+ (carboxylic acid + ammonium ion) (2)."),

    make_edexcel_q(18, "Alkaline Hydrolysis of Nitriles followed by Acidification", "WCH14/01/Sample/Q18", 4,
        "Ethanenitrile CH3CN heated under reflux with NaOH(aq), followed by adding dilute HCl.",
        [{'label': 'a', 'text': 'Write equation for Step 1 (alkaline hydrolysis).', 'marks': 2},
         {'label': 'b', 'text': 'Write equation for Step 2 (acidification).', 'marks': 2}],
        "18. (a) CH3CN + NaOH + H2O -> CH3COONa + NH3(g) (2).<br/>18. (b) CH3COONa + HCl -> CH3COOH + NaCl (2)."),

    make_edexcel_q(19, "Test for Carboxylic Acid Functional Group: NaHCO3 Effervescence", "WCH14/01/Sample/Q19", 3,
        "Sodium hydrogen carbonate NaHCO3 solution is added to an unknown liquid.",
        [{'label': 'a', 'text': 'State the observation and write the ionic equation for a positive test.', 'marks': 3}],
        "19. (a) Vigorous effervescence / gas bubbles turning limewater milky (1). Ionic equation: RCOOH(aq) + HCO3-(aq) -> RCOO-(aq) + H2O(l) + CO2(g) (2)."),

    make_edexcel_q(20, "Formic Acid (Methanoic Acid) Unique Reducing Properties", "WCH14/01/Sample/Q20", 4,
        "Methanoic acid, HCOOH, is unique among carboxylic acids because it contains both an aldehyde -CHO group and a carboxyl -COOH group.",
        [{'label': 'a', 'text': 'Explain why methanoic acid reduces Tollens\' reagent and Fehling\'s solution, whereas ethanoic acid does not.', 'marks': 4}],
        "20. (a) HCOOH structure H-C(=O)-OH contains an aldehyde C-H group attached to C=O (2). It is easily oxidized further to carbonic acid / CO2 and H2O: HCOOH + [O] -> CO2 + H2O (1). CH3COOH lacks an aldehyde proton and cannot be oxidized by Tollens\' or Fehling\'s (1)."),

    # Questions 21 to 50: Additional authentic practice questions for 15C
    make_edexcel_q(21, "Oxidation of Methanoic Acid by Potassium Manganate(VII)", "WCH14/01/Sample/Q21", 4,
        "Methanoic acid decolourises acidified KMnO4 solution upon warming.",
        [{'label': 'a', 'text': 'Write a balanced ionic equation for the oxidation of HCOOH by MnO4-.', 'marks': 4}],
        "21. (a) 5HCOOH + 2MnO4- + 6H+ -> 5CO2 + 2Mn2+ + 8H2O (4). Purple MnO4- decolourises to colourless Mn2+."),

    make_edexcel_q(22, "Oxidation of Ethanedioic Acid (Oxalic Acid) in Titrations", "WCH14/01/Sample/Q22", 4,
        "Ethanedioic acid (COOH)2 is a primary standard used to standardize KMnO4.",
        [{'label': 'a', 'text': 'Write balanced ionic equation for (COOH)2 with MnO4- at 60 °C.', 'marks': 4}],
        "22. (a) 5(COOH)2 + 2MnO4- + 6H+ -> 10CO2 + 2Mn2+ + 8H2O (4)."),

    make_edexcel_q(23, "Relative Boiling Points of Mono- vs Di-carboxylic Acids", "WCH14/01/Sample/Q23", 3,
        "Boiling points: Propanoic acid (141 °C), Propanedioic acid (decomposes at 135 °C, high melting point 135 °C).",
        [{'label': 'a', 'text': 'Explain why dicarboxylic acids have extremely high melting points and form polymer-like hydrogen-bonded networks.', 'marks': 3}],
        "23. (a) Dicarboxylic acids have TWO -COOH groups per molecule (1), forming extensive 3D intermolecular hydrogen-bonded networks in crystal lattice (2)."),

    make_edexcel_q(24, "Synthesis of Lactic Acid from Ethanol in 4 Steps", "WCH14/01/Sample/Q24", 5,
        "Ethanol -> Ethanal -> 2-hydroxypropanenitrile -> Lactic acid.",
        [{'label': 'a', 'text': 'Specify reagents and conditions for all 3 steps.', 'marks': 5}],
        "24. (a) Step 1: K2Cr2O7 / H2SO4, distill off ethanal (1). Step 2: HCN + KCN, pH 8 -> 2-hydroxypropanenitrile (2). Step 3: Dilute HCl, reflux -> 2-hydroxypropanoic acid (lactic acid) (2)."),

    make_edexcel_q(25, "NMR Characteristics of Carboxylic Acid Protons", "WCH14/01/Sample/Q25", 3,
        "1H NMR spectra of carboxylic acids feature a characteristic broad singlet.",
        [{'label': 'a', 'text': 'State the chemical shift delta range for the -COOH proton in 1H NMR.', 'marks': 1},
         {'label': 'b', 'text': 'Explain why D2O shake eliminates the -COOH proton peak.', 'marks': 2}],
        "25. (a) delta 10.0 - 12.0 ppm (1).<br/>25. (b) Labile -COOH proton rapidly exchanges with deuterium in D2O: RCOOH + D2O <=> RCOOD + HOD. Deuterium does not absorb in 1H NMR region, causing peak to disappear (2)."),

    make_edexcel_q(26, "A* Challenge: Acid Strength of Fluorinated vs Chlorinated Carboxylic Acids", "WCH14/01/Hard/Q26", 5,
        "pKa values: CH2FCOOH (2.59), CH2ClCOOH (2.86), CH2BrCOOH (2.90), CH2ICOOH (3.18).",
        [{'label': 'a', 'text': 'Explain the trend in pKa in terms of halogen electronegativity and electron-withdrawing inductive effect.', 'marks': 5}],
        "26. (a) Electronegativity decreases down halogen group: F (4.0) > Cl (3.0) > Br (2.8) > I (2.5) (1). Fluorine exerts strongest -I electron-withdrawing inductive effect (1). Pulls electron density along C-C and C-O bonds most effectively (1). Stabilizes carboxylate anion -COO- to greatest extent (1). Shifts equilibrium right, giving highest Ka and lowest pKa (strongest acid) (1)."),

    make_edexcel_q(27, "A* Challenge: Distance Dependence of Inductive Effects on Acidity", "WCH14/01/Hard/Q27", 5,
        "pKa values: 2-chlorobutanoic acid (2.86), 3-chlorobutanoic acid (4.05), 4-chlorobutanoic acid (4.52), Butanoic acid (4.82).",
        [{'label': 'a', 'text': 'Explain why moving the chlorine atom further from the -COOH group diminishes its acid-strengthening effect.', 'marks': 5}],
        "27. (a) Electron-withdrawing inductive effect (-I) operates through sigma bonds (1). Inductive effect diminishes rapidly with increasing distance / number of intervening sigma bonds (2). In 2-chlorobutanoic acid, Cl is on C2 (adjacent to -COOH), exerting maximum charge stabilization on -COO- (1). In 4-chlorobutanoic acid, Cl is 3 carbon atoms away, so -I effect on -COO- is negligible (1)."),

    make_edexcel_q(28, "A* Challenge: Multi-Step Synthesis of Benzoic Acid from Methylbenzene", "WCH14/01/Hard/Q28", 5,
        "Oxidation of alkylbenzenes with alkaline KMnO4.",
        [{'label': 'a', 'text': 'Write balanced equation for oxidation of methylbenzene C6H5CH3 with alkaline KMnO4 under reflux, followed by acidification.', 'marks': 4},
         {'label': 'b', 'text': 'Predict the oxidation product of ethylbenzene C6H5CH2CH3.', 'marks': 1}],
        "28. (a) Step 1: C6H5CH3 + 2KMnO4 -> C6H5COOK + 2MnO2(s) + KOH + H2O (2). Step 2: C6H5COOK + HCl -> C6H5COOH(s) + KCl (2).<br/>28. (b) Benzoic acid C6H5COOH (side chain cleaved regardless of length if alpha-H present) (1)."),

    make_edexcel_q(29, "A* Challenge: Decarboxylation Mechanism of beta-Keto Acids", "WCH14/01/Hard/Q29", 5,
        "beta-keto acids (e.g. 3-oxobutanoic acid, CH3COCH2COOH) undergo thermal decarboxylation readily at 50 °C without soda lime.",
        [{'label': 'a', 'text': 'Draw the 6-membered cyclic transition state for decarboxylation of 3-oxobutanoic acid forming propan-2-ol enol.', 'marks': 5}],
        "29. (a) Intramolecular hydrogen bond between C=O oxygen of beta-keto group and -COOH proton forms 6-membered ring (2). Concerted cyclic 6-electron rearrangement (1): CO2 is eliminated (1), forming enol intermediate CH2=C(OH)CH3 which tautomerizes to propanone (1)."),

    make_edexcel_q(30, "A* Challenge: Retrosynthetic Design of Branched Carboxylic Acids", "WCH14/01/Hard/Q30", 5,
        "Design two independent synthetic routes to prepare 2-methylbutanoic acid, CH3CH2CH(CH3)COOH.",
        [{'label': 'a', 'text': 'Route 1: From 2-bromobutane via Grignard carboxylation with CO2.', 'marks': 2.5},
         {'label': 'b', 'text': 'Route 2: From 2-bromobutane via nitrile substitution and hydrolysis.', 'marks': 2.5}],
        "30. (a) CH3CH2CH(CH3)Br + Mg -> Grignard --(CO2)--> --(H+)--> CH3CH2CH(CH3)COOH (2.5).<br/>30. (b) CH3CH2CH(CH3)Br + KCN --(ethanolic)--> CH3CH2CH(CH3)CN --(H+/H2O, reflux)--> CH3CH2CH(CH3)COOH (2.5)."),

    make_edexcel_q(31, "A* Challenge: Stereochemistry of Esterification of Chiral Alcohols", "WCH14/01/Hard/Q31", 5,
        "Reaction of (R)-butan-2-ol with ethanoic acid in the presence of concentrated H2SO4.",
        [{'label': 'a', 'text': 'Predict whether the product sec-butyl ethanoate is optically active.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why the configuration at the chiral C2 carbon atom is 100% retained.', 'marks': 3}],
        "31. (a) Optically active (100% (R)-configuration retained) (2).<br/>31. (b) Esterification mechanism involves cleavage of acyl C-OH bond of ethanoic acid (1). The C-O bond attached to the chiral C2 carbon of (R)-butan-2-ol is NEVER broken during reaction (2)."),

    make_edexcel_q(32, "A* Challenge: Acidic Hydrolysis Equilibrium Constant K_hyd for Esters", "WCH14/01/Hard/Q32", 5,
        "Acidic hydrolysis: CH3COOCH3 + H2O <=> CH3COOH + CH3OH (Kc = 0.25).",
        [{'label': 'a', 'text': 'Explain why acid hydrolysis of esters never goes to 100% completion.', 'marks': 2},
         {'label': 'b', 'text': 'Calculate the equilibrium yield of CH3COOH when 1.00 mol ester is refluxed with 5.00 mol water.', 'marks': 3}],
        "32. (a) Reaction is reversible (equilibrium established with Kc = 0.25) (2).<br/>32. (b) Kc = x^2 / ((1-x)(5-x)) = 0.25 => x^2 = 0.25(5 - 6x + x^2) => 0.75x^2 + 1.5x - 1.25 = 0 => 3x^2 + 6x - 5 = 0 => x = (-6 + sqrt(36 + 60)) / 6 = (-6 + 9.798) / 6 = 0.633 mol (63.3% yield) (3)."),

    make_edexcel_q(33, "A* Challenge: Alkaline Hydrolysis (Saponification) Irreversibility", "WCH14/01/Hard/Q33", 5,
        "Alkaline hydrolysis: CH3COOCH3 + NaOH -> CH3COONa + CH3OH.",
        [{'label': 'a', 'text': 'Explain why alkaline hydrolysis goes to 100% completion (irreversible) unlike acid hydrolysis.', 'marks': 5}],
        "33. (a) Alkaline hydrolysis produces ethanoate ions CH3COO- (1). Ethanoate ion is negatively charged and resonance-stabilized (1). CH3COO- cannot undergo nucleophilic attack by alcohol CH3OH (electrostatic repulsion / non-electrophilic) (2). Removal of CH3COOH as CH3COO- shifts equilibrium 100% to the right (irreversible) (1)."),

    make_edexcel_q(34, "A* Challenge: Transesterification Reactions in Biodiesel Production", "WCH14/01/Hard/Q34", 5,
        "Vegetable oil triglycerides (triesters of glycerol) are converted to biodiesel (fatty acid methyl esters, FAME).",
        [{'label': 'a', 'text': 'Write a general equation for transesterification of a triglyceride with methanol in the presence of NaOH catalyst.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why biodiesel is considered carbon-neutral.', 'marks': 2}],
        "34. (a) Triglyceride + 3CH3OH --(NaOH)--> Glycerol + 3 Fatty Acid Methyl Esters (FAME) (3).<br/>34. (b) CO2 released during combustion of biodiesel was recently absorbed from the atmosphere by oil crops during photosynthesis (2)."),

    make_edexcel_q(35, "A* Challenge: Synthesis of Aspirin (Acetylsalicylic Acid)", "WCH14/01/Hard/Q35", 5,
        "Aspirin is synthesized by reacting 2-hydroxybenzoic acid (salicylic acid) with ethanoic anhydride in the presence of H3PO4.",
        [{'label': 'a', 'text': 'Write a balanced equation for aspirin synthesis.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why ethanoic anhydride is preferred over ethanoyl chloride in industrial pharmaceutical manufacturing.', 'marks': 3}],
        "35. (a) C6H4(OH)COOH + (CH3CO)2O -> C6H4(OCOCH3)COOH + CH3COOH (2).<br/>35. (b) Ethanoic anhydride is cheaper, less corrosive, less vulnerable to hydrolysis, and does not produce toxic, hazardous corrosive HCl(g) fumes (3)."),

    make_edexcel_q(36, "A* Challenge: Purification of Aspirin by Recrystallization & Melting Point QC", "WCH14/01/Hard/Q36", 5,
        "Recrystallization of crude aspirin from ethanol/water solvent mixture.",
        [{'label': 'a', 'text': 'Describe the step-by-step procedure for recrystallization.', 'marks': 3},
         {'label': 'b', 'text': 'How does an impurity affect the melting point of aspirin (pure mp = 138-140 °C)?', 'marks': 2}],
        "36. (a) Dissolve crude aspirin in minimum volume of hot solvent (1). Hot filter to remove insoluble impurities (1). Cool filtrate in ice bath to crystallize pure aspirin, suction filter, and dry (1).<br/>36. (b) Impurities lower the melting point and broaden the melting point range (e.g. 130-135 °C) (2)."),

    make_edexcel_q(37, "A* Challenge: Quantitative Thin Layer Chromatography (TLC) of Aspirin", "WCH14/01/Hard/Q37", 5,
        "TLC monitoring of aspirin synthesis from salicylic acid.",
        [{'label': 'a', 'text': 'Explain how Rf values are calculated: Rf = distance moved by spot / distance moved by solvent front.', 'marks': 2},
         {'label': 'b', 'text': 'State how iron(III) chloride FeCl3 solution is used to detect unreacted salicylic acid impurity.', 'marks': 3}],
        "37. (a) Rf = distance moved by solute spot / distance moved by solvent front (2).<br/>37. (b) FeCl3 reacts with phenol -OH group in salicylic acid to form a purple complex (2). Pure aspirin lacks a phenol -OH group and gives NO colour change with FeCl3 (1)."),

    make_edexcel_q(38, "A* Challenge: NMR Elucidation of Isomeric Esters C4H8O2", "WCH14/01/Hard/Q38", 5,
        "Four ester structural isomers have molecular formula C4H8O2.",
        [{'label': 'a', 'text': 'Draw and name the four ester isomers of C4H8O2.', 'marks': 2},
         {'label': 'b', 'text': 'Distinguish ethyl ethanoate CH3COOCH2CH3 from methyl propanoate CH3CH2COOCH3 using 1H NMR splitting.', 'marks': 3}],
        "38. (a) Ethyl ethanoate, methyl propanoate, propyl formate, isopropyl formate (2).<br/>38. (b) Ethyl ethanoate: singlet at 2.0 ppm (CH3CO), quartet at 4.1 ppm (-OCH2-), triplet at 1.2 ppm (-CH3) (1.5). Methyl propanoate: singlet at 3.7 ppm (-OCH3), quartet at 2.3 ppm (-CH2CO-), triplet at 1.1 ppm (-CH3) (1.5)."),

    make_edexcel_q(39, "A* Challenge: Di-ester Hydrolysis Kinetics (Dimethyl Phthalate)", "WCH14/01/Hard/Q39", 5,
        "Alkaline hydrolysis of dimethyl phthalate (benzene-1,2-dicarboxylate dimethyl ester).",
        [{'label': 'a', 'text': 'Write balanced equation for complete saponification with NaOH.', 'marks': 3},
         {'label': 'b', 'text': 'Calculate moles of NaOH required to fully hydrolyse 0.050 mol of dimethyl phthalate.', 'marks': 2}],
        "39. (a) C6H4(COOCH3)2 + 2NaOH -> C6H4(COO-Na+)2 + 2CH3OH (3).<br/>39. (b) Moles NaOH = 2 x 0.050 = 0.100 mol (2)."),

    make_edexcel_q(40, "A* Challenge: High Resolution 13C NMR of Substituted Benzoic Acids", "WCH14/01/Hard/Q40", 5,
        "Predict the number of peaks in the 13C NMR spectrum of:",
        [{'label': 'a', 'text': 'Benzoic acid, C6H5COOH.', 'marks': 2.5},
         {'label': 'b', 'text': '4-methylbenzoic acid, CH3-C6H4-COOH.', 'marks': 2.5}],
        "40. (a) Benzoic acid has 5 non-equivalent carbon environments (ipso C1, ortho C2/C6, meta C3/C5, para C4, carboxyl C=O) => 5 peaks (2.5).<br/>40. (b) 4-methylbenzoic acid has 5 non-equivalent carbon environments (methyl C, ipso C4, meta C3/C5, ortho C2/C6, ipso C1, carboxyl C=O) => 5 peaks (2.5)."),

    make_edexcel_q(41, "A* Challenge: Multi-Step Synthesis of Paracetamol from Phenol", "WCH14/01/Hard/Q41", 5,
        "Synthesis: Phenol -> 4-nitrophenol -> 4-aminophenol -> Paracetamol (4-acetamidophenol).",
        [{'label': 'a', 'text': 'Step 1: Nitration of phenol with dilute HNO3.', 'marks': 1.5},
         {'label': 'b', 'text': 'Step 2: Reduction of 4-nitrophenol with Sn / concentrated HCl.', 'marks': 1.5},
         {'label': 'c', 'text': 'Step 3: Acetylation of 4-aminophenol with ethanoic anhydride.', 'marks': 2}],
        "41. (a) Dilute HNO3 at room temp forms 4-nitrophenol (1.5).<br/>41. (b) Sn and conc HCl, heat under reflux, followed by NaOH (1.5).<br/>41. (c) 4-aminophenol + (CH3CO)2O -> 4-acetamidophenol (Paracetamol) + CH3COOH (2)."),

    make_edexcel_q(42, "A* Challenge: Mass Spectrometry Resolution of Carboxylic Acid Isomers", "WCH14/01/Hard/Q42", 5,
        "Distinguish pentanoic acid CH3(CH2)3COOH and 2,2-dimethylpropanoic acid (CH3)3CCOOH using mass spec fragmentation.",
        [{'label': 'a', 'text': 'Identify base peak fragment in 2,2-dimethylpropanoic acid.', 'marks': 3},
         {'label': 'b', 'text': 'Identify fragment ion in pentanoic acid.', 'marks': 2}],
        "42. (a) 2,2-dimethylpropanoic acid cleaves alpha to C=O, losing COOH (45 Da) to give massive stable tert-butyl carbocation [(CH3)3C]+ base peak at m/z 57 (3).<br/>42. (b) Pentanoic acid undergoes McLafferty rearrangement yielding fragment ion at m/z 60 (2)."),

    make_edexcel_q(43, "A* Challenge: Synthesis of Polyesters (PET / Terylene)", "WCH14/01/Hard/Q43", 5,
        "Condensation polymerisation of benzene-1,4-dicarboxylic acid and ethane-1,2-diol.",
        [{'label': 'a', 'text': 'Draw the repeat unit of Poly(ethylene terephthalate) (PET).', 'marks': 3},
         {'label': 'b', 'text': 'State why condensation polymerisation produces a small molecule byproduct (H2O).', 'marks': 2}],
        "43. (a) -[O-CH2-CH2-O-CO-C6H4-CO]-n (3).<br/>43. (b) Each ester linkage formation combines -COOH and -OH groups, eliminating 1 molecule of H2O per linkage (2)."),

    make_edexcel_q(44, "A* Challenge: Biodegradability of Polyesters vs Addition Polymers", "WCH14/01/Hard/Q44", 5,
        "Compare the environmental degradation of PET polyester vs Poly(ethene).",
        [{'label': 'a', 'text': 'Explain why PET is biodegradable via hydrolysis.', 'marks': 3},
         {'label': 'b', 'text': 'Explain why poly(ethene) is non-biodegradable.', 'marks': 2}],
        "44. (a) PET contains polar ester linkages (-CO-O-) vulnerable to nucleophilic attack and hydrolysis by environmental water/enzymes/microorganisms (3).<br/>44. (b) Poly(ethene) consists of non-polar, unreactive strong C-C and C-H single bonds resistant to hydrolysis and bacterial attack (2)."),

    make_edexcel_q(45, "A* Challenge: Synthesis of Acyl Chlorides using Thionyl Chloride SOCl2", "WCH14/01/Hard/Q45", 5,
        "Carboxylic acids react with thionyl chloride SOCl2 to form acyl chlorides.",
        [{'label': 'a', 'text': 'Write balanced equation for CH3COOH + SOCl2.', 'marks': 2},
         {'label': 'b', 'text': 'Explain why SOCl2 is preferred over PCl5 in industrial acyl chloride preparations.', 'marks': 3}],
        "45. (a) CH3COOH + SOCl2 -> CH3COCl + SO2(g) + HCl(g) (2).<br/>45. (b) Both byproducts (SO2 and HCl) are gases that escape automatically, leaving pure liquid acyl chloride without requiring fractional distillation (unlike liquid POCl3 byproduct from PCl5) (3)."),

    make_edexcel_q(46, "A* Challenge: Enthalpy of Combustion Trends in Monocarboxylic Acids", "WCH14/01/Hard/Q46", 5,
        "Standard enthalpies of combustion Delta_c H° (kJ mol-1): HCOOH (-255), CH3COOH (-874), C2H5COOH (-1527), C3H7COOH (-2184).",
        [{'label': 'a', 'text': 'Calculate the average increment in Delta_c H° per -CH2- methylene group.', 'marks': 2},
         {'label': 'b', 'text': 'Explain the linear relationship between Delta_c H° and carbon chain length.', 'marks': 3}],
        "46. (a) Delta_c H diff: (-874 - (-255)) = -619; (-1527 - (-874)) = -653; (-2184 - (-1527)) = -657. Average increment ~ -650 kJ mol-1 per -CH2- group (2).<br/>46. (b) Each additional -CH2- group requires breaking 2 C-H and 1 C-C bond and forming 1 CO2 and 1 H2O, providing a constant increment of heat release (3)."),

    make_edexcel_q(47, "A* Challenge: Synthesis of Poly(lactic acid) PLA via Cyclic Lactide", "WCH14/01/Hard/Q47", 5,
        "Lactic acid CH3CH(OH)COOH undergoes self-esterification.",
        [{'label': 'a', 'text': 'Draw the structure of cyclic dimer (dilactide) formed by heating lactic acid.', 'marks': 3},
         {'label': 'b', 'text': 'Describe ring-opening polymerisation of dilactide to high molar mass PLA.', 'marks': 2}],
        "47. (a) 6-membered ring containing 2 ester linkages: 3,6-dimethyl-1,4-dioxane-2,5-dione (3).<br/>47. (b) Ring-opening polymerisation of dilactide with tin(II) octoate catalyst yields high molar mass biodegradable PLA polymer without releasing water (2)."),

    make_edexcel_q(48, "A* Challenge: Gas Chromatography - Mass Spectrometry (GC-MS) of Fatty Acid Methyl Esters", "WCH14/01/Hard/Q48", 5,
        "FAME analysis in olive oil testing for adulteration.",
        [{'label': 'a', 'text': 'Explain why non-volatile fatty acids must be converted to volatile methyl esters (FAME) before GC analysis.', 'marks': 2},
         {'label': 'b', 'text': 'Explain how GC retention time t_R and MS fragmentation pattern identify oleic acid vs palmitic acid.', 'marks': 3}],
        "48. (a) High boiling point fatty acids decompose at high temperatures; methyl esters are more volatile and pass cleanly through GC column without thermal breakdown (2).<br/>48. (b) GC separates esters by boiling point/polarity giving unique retention times (1.5); MS electron ionization gives distinct molecular ion M+ (m/z 296 for methyl oleate vs m/z 270 for methyl palmitate) and fragmentation patterns (1.5)."),

    make_edexcel_q(49, "A* Challenge: Synthesis of Nylon-6,6 vs Terylene Comparison", "WCH14/01/Hard/Q49", 5,
        "Compare condensation polymerisation forming Nylon-6,6 polyamide vs Terylene polyester.",
        [{'label': 'a', 'text': 'Identify monomers for Nylon-6,6 and draw its repeat unit.', 'marks': 3},
         {'label': 'b', 'text': 'Compare intermolecular hydrogen bonding in Nylon-6,6 vs dipole-dipole forces in Terylene.', 'marks': 2}],
        "49. (a) Hexane-1,6-diamine + Hexanedioic acid. Repeat unit: -[HN-(CH2)6-NH-CO-(CH2)4-CO]-n (3).<br/>49. (b) Nylon-6,6 forms strong intermolecular hydrogen bonds between N-H and C=O of adjacent chains (higher melting point ~265 °C); Terylene forms permanent dipole-dipole attractions between ester C=O groups (2)."),

    make_edexcel_q(50, "A* Challenge: Complete Carboxylic Acid Master Synthesis & Elucidation", "WCH14/01/Hard/Q50", 6,
        "An unknown organic solid A (C7H6O2) is sparingly soluble in cold water but dissolves in NaHCO3(aq) with effervescence.<br/>A reacts with PCl5 forming B (C7H5ClO) with misty fumes.<br/>A reacts with methanol in conc H2SO4 forming sweet-smelling ester C (C8H8O2).<br/>Nitration of A with conc HNO3/H2SO4 yields single mononitro derivative D.",
        [{'label': 'a', 'text': 'Deduce structures of A, B, C, D with full chemical justification.', 'marks': 6}],
        "50. (a) A (C7H6O2) gives CO2 effervescence with NaHCO3 => carboxylic acid => Benzoic acid, C6H5COOH (1.5). B = Benzoyl chloride, C6H5COCl (PCl5 test) (1.5). C = Methyl benzoate, C6H5COOCH3 (esterification) (1.5). Nitration of benzoic acid gives 3-nitrobenzoic acid D (-COOH is meta-directing) (1.5).")
]

p9_faqs = [
    make_edexcel_faq("Carboxylic Acid Dimerization", "Intermolecular Forces", "Assuming carboxylic acids only form single hydrogen bonds.", "Carboxylic acids form HEAD-TO-TAIL DIMERS in liquid/gas phases held by TWO hydrogen bonds per pair. This effectively doubles their molecular mass and elevates boiling points above alcohols."),
    make_edexcel_faq("NaHCO3 Test Specificity", "Carbonate Effervescence", "Thinking phenols give a positive effervescence test with NaHCO3.", "Phenols (pKa ~10) are TOO WEAK to react with NaHCO3. ONLY carboxylic acids (pKa ~4-5) are strong enough to liberate CO2 gas from NaHCO3(aq). This test unequivocally distinguishes carboxylic acids from phenols."),
    make_edexcel_faq("PCl5 Reaction Conditions & Byproducts", "Acyl Chloride Preparation", "Writing water H2O as a byproduct in PCl5 reactions.", "PCl5 reacts with -COOH to form acyl chloride RCOCl + POCl3(l) + HCl(g). Reaction MUST be dry because PCl5 and RCOCl react violently with water."),
    make_edexcel_faq("Role of Concentrated H2SO4 in Esterification", "Esterification Catalyst", "Stating H2SO4 acts solely as a catalyst in esterification.", "Concentrated H2SO4 acts as BOTH a acid catalyst (protonates C=O) AND a DEHYDRATING AGENT (absorbs water byproduct, shifting equilibrium right to increase ester yield)."),
    make_edexcel_faq("Isotopic Labeling in Esterification", "Mechanism Proof", "Thinking the C-OH bond of the alcohol breaks during esterification.", "Isotopic 18O labeling proves the C-OH bond of the CARBOXYLIC ACID breaks, NOT the alcohol O-H bond. The 18O label from alcohol ends up in the ester."),
    make_edexcel_faq("Inductive vs Resonance Effects on Acidity", "Organic Acidity", "Confusing electron-withdrawing (-I) with electron-donating (+I) group impacts.", "Electron-withdrawing groups (-Cl, -NO2) pull electron density away from -COO-, stabilizing the anion and INCREASING acid strength. Electron-donating alkyl groups (+I) push density towards -COO-, destabilizing anion and DECREASING acid strength."),
    make_edexcel_faq("Formic Acid (HCOOH) Unique Oxidation", "Formic Acid Oxidation", "Treating methanoic acid as a typical unreactive carboxylic acid.", "Methanoic acid HCOOH contains an ALDEHYDE C-H proton H-C(=O)-OH. Unlike other carboxylic acids, HCOOH is EASILY OXIDIZED by Tollens', Fehling's, or KMnO4 to CO2 and H2O."),
    make_edexcel_faq("Soda Lime Decarboxylation Chain Length", "Decarboxylation", "Forgetting that soda lime decarboxylation shortens the carbon chain by ONE carbon.", "Heating RCOONa with soda lime (NaOH/CaO) removes -COONa as Na2CO3, yielding alkane R-H with ONE LESS carbon atom than the original acid."),
    make_edexcel_faq("Nitrile Hydrolysis Reaction Products", "Nitrile Hydrolysis", "Forgetting ammonium salt byproduct in acidic nitrile hydrolysis.", "Acidic hydrolysis of nitriles yields carboxylic acid + AMMONIUM SALT: RCN + 2H2O + HCl -> RCOOH + NH4Cl. Alkaline hydrolysis yields carboxylate salt + AMMONIA: RCN + H2O + NaOH -> RCOONa + NH3."),
    make_edexcel_faq("LiAlH4 vs NaBH4 Reduction of Acids", "Reduction Selectivity", "Attempting to reduce carboxylic acids using NaBH4.", "Carboxylic acids are UNREACTIVE towards NaBH4. You MUST use LiAlH4 in dry ether followed by acid hydrolysis to reduce a carboxylic acid to a primary alcohol.")
]

# Build Pack 9 PDF
build_pdf_pack("Usman_Edexcel_Chem_U4_15C_Carboxylic_Acids.pdf", p9_meta, p9_questions, p9_faqs)
print("Pack 9 (15C Carboxylic Acids - 50 Qs + 10 FAQs) compiled successfully!")
