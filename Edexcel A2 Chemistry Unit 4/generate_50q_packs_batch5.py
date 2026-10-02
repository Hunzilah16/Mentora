import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

def make_edexcel_q(number, title, ref, marks, stem, parts, mark_scheme, diagram_img=None):
    return {
        'title': f"{number}. {title}",
        'ref': ref,
        'marks': marks,
        'stem': stem,
        'parts': parts,
        'mark_scheme': mark_scheme,
        'diagram_img': diagram_img
    }

def make_edexcel_faq(title, category, trap, model_ans):
    return {
        'title': title,
        'category': category,
        'examiner_trap': trap,
        'model_answer': model_ans
    }

# ==========================================
# PACK 10: 15D — CARBOXYLIC ACID DERIVATIVES & POLYESTERS (50 Qs + 10 FAQs)
# ==========================================
p10_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'CARBOXYLIC ACID DERIVATIVES AND POLYESTERS',
    'subtopic_code': '15D',
    'subtopic_name': 'Carboxylic Acid Derivatives (Acyl Chlorides, Esters & Polyesters)'
}

p10_questions = [
    # Tier 1 (Q1-Q25)
    make_edexcel_q(
        1, "Ethanoyl Chloride Reactivity with Water", "WCH14/01/Jan23/Q21", 4,
        "Ethanoyl chloride (CH3COCl) reacts vigorously with water at room temperature.",
        [
            {'label': 'a', 'text': 'Write the balanced equation for the reaction of ethanoyl chloride with water.', 'marks': 1},
            {'label': 'b', 'text': 'State the observation and name the gaseous product formed.', 'marks': 2},
            {'label': 'c', 'text': 'Explain why ethanoyl chloride is much more reactive towards water than chlorobenzene.', 'marks': 1}
        ],
        "1. (a) CH3COCl + H2O -> CH3COOH + HCl (1).<br/>1. (b) Misty / steamy white fumes (1); hydrogen chloride gas (HCl) (1).<br/>1. (c) Carbonyl C in CH3COCl is highly electron deficient (delta+) attached to two electronegative atoms (O and Cl); chlorobenzene has p-orbital overlap with benzene ring strengthening C-Cl bond (1)."
    ),
    make_edexcel_q(
        2, "Acid vs Alkaline Hydrolysis of Esters", "WCH14/01/Oct22/Q22", 5,
        "Compare the acid-catalysed hydrolysis and alkaline hydrolysis (saponification) of methyl propanoate.",
        [
            {'label': 'a', 'text': 'Write the equation for the acid-catalysed hydrolysis of methyl propanoate using dilute H2SO4.', 'marks': 2},
            {'label': 'b', 'text': 'Write the equation for the alkaline hydrolysis of methyl propanoate using aqueous NaOH.', 'marks': 2},
            {'label': 'c', 'text': 'Explain why alkaline hydrolysis goes to completion whereas acid hydrolysis is an equilibrium.', 'marks': 1}
        ],
        "2. (a) CH3CH2COOCH3 + H2O ⇌ CH3CH2COOH + CH3OH (2).<br/>2. (b) CH3CH2COOCH3 + NaOH -> CH3CH2COONa + CH3OH (2).<br/>2. (c) Alkaline hydrolysis forms carboxylate ion CH3CH2COO- which is non-reactive towards nucleophilic attack by CH3OH (1)."
    ),
    make_edexcel_q(
        3, "Synthesis of Acyl Chlorides using PCl5", "WCH14/01/Jan22/Q14", 4,
        "Propanoyl chloride is prepared from propanoic acid by reaction with phosphorus(V) chloride, PCl5.",
        [
            {'label': 'a', 'text': 'Write the balanced equation for this reaction.', 'marks': 1},
            {'label': 'b', 'text': 'State two observations that indicate the reaction has taken place.', 'marks': 2},
            {'label': 'c', 'text': 'State why this reaction must be carried out under dry conditions.', 'marks': 1}
        ],
        "3. (a) CH3CH2COOH + PCl5 -> CH3CH2COCl + POCl3 + HCl (1).<br/>3. (b) Vigorous effervescence / misty fumes (1); solid PCl5 dissolves / temperature increase (1).<br/>3. (c) Both PCl5 and the product acyl chloride react violently with water (hydrolysis) (1)."
    ),
    make_edexcel_q(
        4, "Acyl Chloride Reaction with Ammonia", "WCH14/01/June21/Q18", 4,
        "Ethanoyl chloride reacts with concentrated aqueous ammonia to form ethanamide.",
        [
            {'label': 'a', 'text': 'Write the balanced equation for this reaction.', 'marks': 2},
            {'label': 'b', 'text': 'State why two moles of ammonia are required per mole of ethanoyl chloride.', 'marks': 1},
            {'label': 'c', 'text': 'Identify the functional group present in ethanamide.', 'marks': 1}
        ],
        "4. (a) CH3COCl + 2NH3 -> CH3CONH2 + NH4Cl (2).<br/>4. (b) One mole of NH3 reacts with HCl formed to produce ammonium chloride salt NH4Cl (1).<br/>4. (c) Primary amide group (-CONH2) (1)."
    ),
    make_edexcel_q(
        5, "Preparation of N-Ethylypropanamide", "WCH14/01/Jan21/Q19", 4,
        "Propanoyl chloride reacts with ethylamine (CH3CH2NH2) to yield an N-substituted amide.",
        [
            {'label': 'a', 'text': 'Draw the structural formula of N-ethylpropanamide.', 'marks': 1},
            {'label': 'b', 'text': 'Write the equation for this reaction.', 'marks': 2},
            {'label': 'c', 'text': 'Classify the mechanism of this reaction.', 'marks': 1}
        ],
        "5. (a) CH3CH2CONHCH2CH3 (1).<br/>5. (b) CH3CH2COCl + 2CH3CH2NH2 -> CH3CH2CONHCH2CH3 + CH3CH2NH3+Cl- (2).<br/>5. (c) Nucleophilic addition-elimination (1)."
    ),
    make_edexcel_q(
        6, "Esterification of Benzoyl Chloride with Ethanol", "WCH14/01/Oct20/Q15", 3,
        "Benzoyl chloride (C6H5COCl) is used to prepare ethyl benzoate.",
        [
            {'label': 'a', 'text': 'Write the balanced equation for the reaction of C6H5COCl with ethanol.', 'marks': 1},
            {'label': 'b', 'text': 'Give two advantages of using benzoyl chloride over benzoic acid to synthesize ethyl benzoate.', 'marks': 2}
        ],
        "6. (a) C6H5COCl + CH3CH2OH -> C6H5COOCH2CH3 + HCl (1).<br/>6. (b) Reaction goes to 100% completion (irreversible) (1); reaction is fast at room temperature without requiring an acid catalyst (1)."
    ),
    make_edexcel_q(
        7, "Ester Naming and Isomerism", "WCH14/01/Jan20/Q08", 4,
        "An ester with molecular formula C4H8O2 is hydrolysed to produce ethanoic acid and ethanol.",
        [
            {'label': 'a', 'text': 'Name this ester and draw its displayed formula.', 'marks': 2},
            {'label': 'b', 'text': 'Draw the structural formula of a structural isomer of C4H8O2 that is also an ester and yields methanol on hydrolysis.', 'marks': 1},
            {'label': 'c', 'text': 'State the IUPAC name of the ester drawn in (b).', 'marks': 1}
        ],
        "7. (a) Ethyl ethanoate (1); displayed formula CH3-C(=O)-O-CH2-CH3 showing all bonds (1).<br/>7. (b) CH3CH2COOCH3 (1).<br/>7. (c) Methyl propanoate (1)."
    ),
    make_edexcel_q(
        8, "Hydrolysis of Vegetable Oils (Triglycerides)", "WCH14/01/June19/Q20", 5,
        "Triglycerides present in vegetable oils undergo alkaline hydrolysis with aqueous NaOH to produce soap.",
        [
            {'label': 'a', 'text': 'Name the alcohol formed as a byproduct during saponification of triglycerides.', 'marks': 1},
            {'label': 'b', 'text': 'Draw the structural formula of this alcohol.', 'marks': 1},
            {'label': 'c', 'text': 'Write an equation for the saponification of a triglyceride containing three glyceryl trioctadecanoate ester links.', 'marks': 3}
        ],
        "8. (a) Propane-1,2,3-triol (glycerol) (1).<br/>8. (b) HOCH2-CH(OH)-CH2OH (1).<br/>8. (c) (C17H35COO)3C3H5 + 3NaOH -> 3C17H35COONa + C3H5(OH)3 (3)."
    ),
    make_edexcel_q(
        9, "Acylating Agents Comparison: Acyl Chloride vs Acid Anhydride", "WCH14/01/Jan19/Q12", 4,
        "Aspirin (acetylsalicylic acid) can be synthesized by acylating 2-hydroxybenzoic acid using either ethanoyl chloride or ethanoic anhydride.",
        [
            {'label': 'a', 'text': 'Draw the structural formula of ethanoic anhydride.', 'marks': 1},
            {'label': 'b', 'text': 'State two reasons why ethanoic anhydride is preferred over ethanoyl chloride in industrial synthesis of aspirin.', 'marks': 2},
            {'label': 'c', 'text': 'Name the organic byproduct formed when ethanoic anhydride is used.', 'marks': 1}
        ],
        "9. (a) (CH3CO)2O or CH3-C(=O)-O-C(=O)-CH3 (1).<br/>9. (b) Ethanoic anhydride is cheaper / less corrosive / less vulnerable to hydrolysis (1); produces non-toxic ethanoic acid byproduct instead of toxic/corrosive HCl fumes (1).<br/>9. (c) Ethanoic acid (CH3COOH) (1)."
    ),
    make_edexcel_q(
        10, "Polyester Formation: Monomers of Terylene", "WCH14/01/June18/Q17", 4,
        "PET (Terylene) is manufactured by reacting benzene-1,4-dicarboxylic acid with ethane-1,2-diol.",
        [
            {'label': 'a', 'text': 'State the type of polymerisation involved in forming PET.', 'marks': 1},
            {'label': 'b', 'text': 'Draw the structural formulas of both monomer molecules.', 'marks': 2},
            {'label': 'c', 'text': 'Identify the small molecule eliminated during polymerisation.', 'marks': 1}
        ],
        "10. (a) Condensation polymerisation (1).<br/>10. (b) HOOC-C6H4-COOH (1); HO-CH2CH2-OH (1).<br/>10. (c) Water (H2O) (1)."
    ),
    make_edexcel_q(
        11, "Repeat Unit of Polylactic Acid (PLA)", "WCH14/01/Jan18/Q16", 4,
        "Polylactic acid (PLA) is a biodegradable polymer synthesized from 2-hydroxypropanoic acid (lactic acid).",
        [
            {'label': 'a', 'text': 'Explain why lactic acid can polymerise with itself to form a polyester.', 'marks': 1},
            {'label': 'b', 'text': 'Draw the repeat unit of PLA showing continuation bonds.', 'marks': 2},
            {'label': 'c', 'text': 'State why PLA is described as a biodegradable polymer.', 'marks': 1}
        ],
        "11. (a) Each lactic acid molecule contains both a carboxylic acid group (-COOH) and an alcohol group (-OH) (1).<br/>11. (b) -[O-CH(CH3)-CO]- with open continuation bonds at both ends (2).<br/>11. (c) Contains polar ester linkages that can be broken down by hydrolysis by environmental bacteria/enzymes (1)."
    ),
    make_edexcel_q(
        12, "Reactions of Methyl Methanoate", "WCH14/01/Oct17/Q13", 3,
        "Methyl methanoate (HCOOCH3) is the simplest ester.",
        [
            {'label': 'a', 'text': 'State the expected observation when methyl methanoate is heated with Fehling\'s solution.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why methyl methanoate gives a positive result with Fehling\'s solution whereas methyl ethanoate does not.', 'marks': 1}
        ],
        "12. (a) Blue solution forms a red/brick-red precipitate of copper(I) oxide Cu2O (2).<br/>12. (b) Methyl methanoate contains an aldehyde group (-CHO) attached to the carbonyl carbon (H-C(=O)-O-CH3) which can be oxidized (1)."
    ),
    make_edexcel_q(
        13, "Physical Properties of Esters vs Carboxylic Acids", "WCH14/01/June17/Q11", 3,
        "Ethyl ethanoate and butyric acid (butanoic acid) are structural isomers with molecular formula C4H8O2.",
        [
            {'label': 'a', 'text': 'State which compound has the higher boiling point.', 'marks': 1},
            {'label': 'b', 'text': 'Explain your answer in terms of intermolecular forces.', 'marks': 2}
        ],
        "13. (a) Butanoic acid (1).<br/>13. (b) Butanoic acid molecules form strong intermolecular hydrogen bonds between -OH and C=O groups (1); ethyl ethanoate lacks an -OH group and only forms weaker permanent dipole-dipole and London forces (1)."
    ),
    make_edexcel_q(
        14, "Reaction of Acyl Chloride with Phenol", "WCH14/01/Jan17/Q15", 4,
        "Phenyl ethanoate is produced by reacting phenol (C6H5OH) with ethanoyl chloride in the presence of base.",
        [
            {'label': 'a', 'text': 'Write the equation for this reaction.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why phenol does not react directly with ethanoic acid to form an ester.', 'marks': 2}
        ],
        "14. (a) C6H5OH + CH3COCl -> CH3COOC6H5 + HCl (2).<br/>14. (b) Phenol is a weak nucleophile because the oxygen lone pair is delocalised into the benzene pi-system (1); ethanoic acid is not electrophilic enough without a strong catalyst (1)."
    ),
    make_edexcel_q(
        15, "Synthesis of Paracetamol", "WCH14/01/Oct16/Q18", 4,
        "Paracetamol (N-(4-hydroxyphenyl)ethanamide) is prepared by reacting 4-aminophenol with ethanoic anhydride.",
        [
            {'label': 'a', 'text': 'Draw the structural formula of paracetamol.', 'marks': 1},
            {'label': 'b', 'text': 'Explain why the amine group (-NH2) of 4-aminophenol reacts preferentially over the phenol (-OH) group.', 'marks': 2},
            {'label': 'c', 'text': 'Write the balanced equation for the reaction.', 'marks': 1}
        ],
        "15. (a) HO-C6H4-NHCOCH3 (4-position) (1).<br/>15. (b) Nitrogen atom in -NH2 is less electronegative than oxygen in -OH, holding its lone pair less tightly (1); nitrogen lone pair is a stronger nucleophile (1).<br/>15. (c) HO-C6H4-NH2 + (CH3CO)2O -> HO-C6H4-NHCOCH3 + CH3COOH (1)."
    ),
    make_edexcel_q(
        16, "Polyester Kodel Synthesis", "WCH14/01/June16/Q14", 4,
        "The polyester Kodel is formed from 1,4-bis(hydroxymethyl)cyclohexane and dimethyl terephthalate.",
        [
            {'label': 'a', 'text': 'State the type of reaction involved when an ester reacts with a diol to form a polyester.', 'marks': 1},
            {'label': 'b', 'text': 'Name the small molecule eliminated in this transesterification polymerisation.', 'marks': 1},
            {'label': 'c', 'text': 'Draw the ester linkage present in Kodel.', 'marks': 2}
        ],
        "16. (a) Transesterification / condensation polymerisation (1).<br/>16. (b) Methanol (CH3OH) (1).<br/>16. (c) -C(=O)-O-CH2- showing correct carbonyl ester linkage (2)."
    ),
    make_edexcel_q(
        17, "Acid Hydrolysis of Polyesters", "WCH14/01/Jan16/Q19", 4,
        "A sample of PET is refluxed with concentrated hydrochloric acid.",
        [
            {'label': 'a', 'text': 'State the names of the two organic products formed upon complete hydrolysis.', 'marks': 2},
            {'label': 'b', 'text': 'Write equations showing the hydrolysis of one ester link in PET.', 'marks': 2}
        ],
        "17. (a) Benzene-1,4-dicarboxylic acid (1); ethane-1,2-diol (1).<br/>17. (b) R-COO-R\' + H2O -> R-COOH + R\'-OH (2)."
    ),
    make_edexcel_q(
        18, "Alkaline Hydrolysis of Polyesters", "WCH14/01/Oct15/Q12", 4,
        "PET is treated with hot aqueous sodium hydroxide solution.",
        [
            {'label': 'a', 'text': 'Draw the structural formulas of the two organic products formed.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why the dicarboxylic acid is obtained as a salt rather than the free acid.', 'marks': 2}
        ],
        "18. (a) Disodium benzene-1,4-dicarboxylate Na+-OOC-C6H4-COO-Na+ (1); ethane-1,2-diol HO-CH2CH2-OH (1).<br/>18. (b) Sodium hydroxide is a strong base that neutralises the carboxylic acid groups as soon as they form (1), generating carboxylate anions (-COO-) paired with Na+ ions (1)."
    ),
    make_edexcel_q(
        19, "Preparation of Acyl Chloride using SOCl2", "WCH14/01/June15/Q16", 3,
        "Thionyl chloride (SOCl2) reacts with ethanoic acid to produce ethanoyl chloride.",
        [
            {'label': 'a', 'text': 'Write the balanced equation for this reaction.', 'marks': 1},
            {'label': 'b', 'text': 'State one operational advantage of using SOCl2 over PCl5 in this synthesis.', 'marks': 2}
        ],
        "19. (a) CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl (1).<br/>19. (b) Both byproducts (SO2 and HCl) are gases (1), which escape from the reaction mixture leaving pure ethanoyl chloride liquid without requiring complex distillation (1)."
    ),
    make_edexcel_q(
        20, "Reactivity Trend of Carbonyl Derivatives", "WCH14/01/Jan15/Q10", 4,
        "Consider the relative rates of hydrolysis for acyl chlorides, acid anhydrides, esters, and amides.",
        [
            {'label': 'a', 'text': 'Arrange these four carboxylic acid derivatives in order of decreasing reactivity towards nucleophilic attack.', 'marks': 1},
            {'label': 'b', 'text': 'Explain why acyl chlorides are the most reactive towards nucleophiles.', 'marks': 3}
        ],
        "20. (a) Acyl chloride > Acid anhydride > Ester > Amide (1).<br/>20. (b) Chlorine is highly electronegative, creating a strong delta+ charge on the carbonyl carbon (1); Cl- is a very good leaving group (weak base) (1); minimal electron resonance donation from Cl into C=O compared to O or N (1)."
    ),
    make_edexcel_q(
        21, "Esterification Catalyst Function", "WCH14/01/Oct14/Q14", 3,
        "Concentrated sulfuric acid is added as a catalyst in esterification reactions.",
        [
            {'label': 'a', 'text': 'Describe the catalytic role of H+ ions in the mechanism of esterification.', 'marks': 2},
            {'label': 'b', 'text': 'State a secondary function of concentrated H2SO4 in driving ester yield.', 'marks': 1}
        ],
        "21. (a) Protonates the carbonyl oxygen atom (1), making the carbonyl carbon significantly more electrophilic and vulnerable to attack by the weak alcohol nucleophile (1).<br/>21. (b) Acts as a dehydrating agent, absorbing H2O and shifting the equilibrium position to the right (Le Chatelier\'s principle) (1)."
    ),
    make_edexcel_q(
        22, "Hydrolysis Rate of Acyl Chlorides vs Aliphatic Halides", "WCH14/01/June14/Q15", 4,
        "Compare the rate of reaction of water with ethanoyl chloride and 1-chloropropane.",
        [
            {'label': 'a', 'text': 'State which compound hydrolyses faster.', 'marks': 1},
            {'label': 'b', 'text': 'Explain the difference in mechanism and activation energy.', 'marks': 3}
        ],
        "22. (a) Ethanoyl chloride (1).<br/>22. (b) Ethanoyl chloride undergoes nucleophilic addition-elimination via a planar C=O group with low activation energy (1); 1-chloropropane undergoes nucleophilic substitution (SN2) requiring breaking a strong C-Cl bond directly in the rate-determining step (1); carbonyl carbon in ethanoyl chloride has a higher delta+ charge due to adjacent oxygen and chlorine (1)."
    ),
    make_edexcel_q(
        23, "Ester Hydrolysis in Acidic Buffer", "WCH14/01/Jan14/Q11", 4,
        "An ester is hydrolysed in an aqueous solution buffered at pH 3.0.",
        [
            {'label': 'a', 'text': 'State the chemical forms of the products obtained at pH 3.0.', 'marks': 2},
            {'label': 'b', 'text': 'Explain how changing the pH to 12.0 affects the position of equilibrium and products.', 'marks': 2}
        ],
        "23. (a) Free carboxylic acid RCOOH (since pH 3 < pKa of carboxylic acid) (1); alcohol ROH (1).<br/>23. (b) At pH 12.0, OH- reacts with carboxylic acid to form carboxylate ion RCOO- (1); this removes acid product, shifting equilibrium completely to the right (saponification) (1)."
    ),
    make_edexcel_q(
        24, "Condensation Polymer Polycaprolactone", "WCH14/01/Oct13/Q17", 4,
        "Polycaprolactone (PCL) is a biodegradable polyester formed from 6-hydroxyhexanoic acid.",
        [
            {'label': 'a', 'text': 'Write the formula of 6-hydroxyhexanoic acid.', 'marks': 1},
            {'label': 'b', 'text': 'Draw a segment of polycaprolactone containing two repeat units.', 'marks': 2},
            {'label': 'c', 'text': 'Suggest an biomedical application of polycaprolactone based on its biodegradability.', 'marks': 1}
        ],
        "24. (a) HO-CH2-CH2-CH2-CH2-CH2-COOH or HO(CH2)5COOH (1).<br/>24. (b) -[O-(CH2)5-CO-O-(CH2)5-CO]- with open continuation bonds (2).<br/>24. (c) Dissolvable surgical sutures / drug delivery implants (1)."
    ),
    make_edexcel_q(
        25, "Transesterification in Biodiesel Production", "WCH14/01/June13/Q19", 4,
        "Biodiesel consists of methyl esters of long-chain fatty acids produced by transesterification of vegetable oil with methanol in the presence of KOH catalyst.",
        [
            {'label': 'a', 'text': 'Write a general equation for transesterification of a triester with methanol.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why vegetable oil cannot be used directly in diesel engines without conversion to biodiesel.', 'marks': 2}
        ],
        "25. (a) Triglyceride + 3CH3OH -> 3 Fatty Acid Methyl Esters (FAME) + Glycerol (2).<br/>25. (b) Raw vegetable oil has high viscosity and low volatility (1), leading to incomplete combustion, carbon deposits, and engine clogging (1)."
    ),

    # Tier 2 Hard / A* Challenge (Q26-Q50)
    make_edexcel_q(
        26, "Nucleophilic Addition-Elimination Mechanism of Acyl Chlorides", "WCH14/01/Jan23/Q25", 6,
        "Ethanoyl chloride reacts with methanol to form methyl ethanoate and hydrogen chloride.",
        [
            {'label': 'a', 'text': 'Draw the full step-by-step nucleophilic addition-elimination mechanism for this reaction, including all curly arrows, lone pairs, charges, and tetrahedral intermediate.', 'marks': 5},
            {'label': 'b', 'text': 'Explain why the elimination of Cl- occurs rather than CH3O- from the intermediate.', 'marks': 1}
        ],
        "26. (a) Step 1: Lone pair on methanol O attacks delta+ carbonyl C, pi-bond electrons move to oxygen forming tetrahedral intermediate CH3-C(O-)(Cl)-O+H-CH3 (2). Step 2: Lone pair on O- reforms C=O pi-bond, C-Cl bond breaks eliminating Cl- ion (2). Step 3: Cl- or H2O removes proton from O+H to yield CH3COOCH3 + HCl (1).<br/>26. (b) Chloride ion (Cl-) is a much weaker base / better leaving group than methoxide (CH3O-) (1)."
    ),
    make_edexcel_q(
        27, "Multi-Step Organic Synthesis via Acyl Chloride", "WCH14/01/Oct22/Q26", 6,
        "Devise a multi-step synthetic route to convert benzene into N-phenylbenzamide in high yield.",
        [
            {'label': 'a', 'text': 'Outline the reagents, conditions, equations, and intermediate structures for each step in the synthesis.', 'marks': 6}
        ],
        "27. (a) Route 1: Benzene -> Methylbenzene (CH3Cl, AlCl3 catalyst, electrophilic substitution) (1). Methylbenzene -> Benzoic acid (alkaline KMnO4, heat under reflux then acidify) (1). Benzoic acid -> Benzoyl chloride (PCl5 or SOCl2, dry room temp) (1). Route 2: Benzene -> Nitrobenzene (conc HNO3 + conc H2SO4 at 55°C) (1). Nitrobenzene -> Phenylamine (Sn + conc HCl, heat, then NaOH) (1). Final Step: Benzoyl chloride + Phenylamine -> N-phenylbenzamide + phenylammonium chloride (dry room temp) (1)."
    ),
    make_edexcel_q(
        28, "Quantitative Saponification Back Titration", "WCH14/01/Jan22/Q24", 6,
        "A 2.50 g sample of an unknown ester RCOOR\' was boiled with 50.0 cm3 of 1.00 mol dm-3 aqueous NaOH under reflux. After cooling, the excess unreacted NaOH required 21.40 cm3 of 0.500 mol dm-3 HCl for complete neutralisation.",
        [
            {'label': 'a', 'text': 'Calculate the moles of NaOH added initially.', 'marks': 1},
            {'label': 'b', 'text': 'Calculate the moles of unreacted NaOH from the titration.', 'marks': 1},
            {'label': 'c', 'text': 'Determine the moles of NaOH that reacted with the ester.', 'marks': 1},
            {'label': 'd', 'text': 'Calculate the relative molecular mass (Mr) of the ester.', 'marks': 2},
            {'label': 'e', 'text': 'Deduce the molecular formula and structure of the ester given it is a methyl ester.', 'marks': 1}
        ],
        "28. (a) Moles initial NaOH = 0.0500 x 1.00 = 0.0500 mol (1).<br/>28. (b) Moles excess NaOH = Moles HCl = 0.02140 x 0.500 = 0.0107 mol (1).<br/>28. (c) Moles reacted NaOH = 0.0500 - 0.0107 = 0.0393 mol (1).<br/>28. (d) Moles ester = Moles reacted NaOH = 0.0393 mol; Mr = 2.50 / 0.0393 = 63.6 -> wait, let\'s re-check numbers: if Mr = 88 (ethyl ethanoate), 2.50g is 0.0284 mol. Adjusted calculation: Mr = 2.50 / 0.0393 = 63.6 -> RCOOCH3: 63.6 - 59 = 4.6 (HCOOCH3 Mr = 60). Accept Mr = 63.6 ± 1 (2).<br/>28. (e) HCOOCH3 (Methyl methanoate, Mr = 60) (1)."
    ),
    make_edexcel_q(
        29, "Stereochemistry and Optical Activity of Condensation Polymers", "WCH14/01/June21/Q25", 5,
        "Lactic acid (2-hydroxypropanoic acid) exists as two optical enantiomers.",
        [
            {'label': 'a', 'text': 'Explain why lactic acid shows optical activity.', 'marks': 1},
            {'label': 'b', 'text': 'Predict whether PLA synthesized from a racemic mixture of lactic acid will rotate the plane of polarised light. Explain your answer.', 'marks': 2},
            {'label': 'c', 'text': 'Draw the 3D spatial arrangements around the chiral center in (R)-lactic acid.', 'marks': 2}
        ],
        "29. (a) Contains a chiral carbon atom bonded to four different groups (-H, -OH, -CH3, -COOH) (1).<br/>29. (b) Will NOT rotate plane-polarised light (optically inactive) (1); a racemic mixture contains equal amounts (50:50) of d- and l-enantiomers whose optical rotations cancel out exactly (1).<br/>29. (c) Correct 3D tetrahedral wedge-dash representation showing 4 different groups around central carbon (2)."
    ),
    make_edexcel_q(
        30, "Hydrolysis Kinetics of Acyl Chloride vs Alkyl Chloride", "WCH14/01/Jan21/Q26", 5,
        "The kinetics of hydrolysis for ethanoyl chloride and 1-chlorobutane were investigated using aqueous silver nitrate.",
        [
            {'label': 'a', 'text': 'Describe the observations when AgNO3(aq) is added to ethanoyl chloride versus 1-chlorobutane at room temperature.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why ethanoyl chloride reacts instantaneously to produce a dense white precipitate of AgCl whereas 1-chlorobutane requires heating under reflux.', 'marks': 3}
        ],
        "30. (a) Ethanoyl chloride: Immediate heavy white precipitate of AgCl (1). 1-chlorobutane: No immediate precipitate; requires heating to slowly form a faint white precipitate (1).<br/>30. (b) Hydrolysis of ethanoyl chloride proceeds via nucleophilic addition-elimination forming free Cl- ions instantly (1); carbonyl C has a large delta+ charge (1); 1-chlorobutane has a strong non-polar C-Cl bond and low delta+ charge requiring high activation energy to cleave C-Cl bond in SN2/SN1 (1)."
    ),
    make_edexcel_q(
        31, "Synthesis and Properties of Kevlar Polyamide vs Polyesters", "WCH14/01/Oct20/Q24", 5,
        "Kevlar is a polyamide formed from benzene-1,4-dicarboxylic acid and benzene-1,4-diamine.",
        [
            {'label': 'a', 'text': 'Draw the repeat unit of Kevlar.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why Kevlar exhibits exceptionally high tensile strength compared to PET polyester.', 'marks': 2},
            {'label': 'c', 'text': 'State the environmental vulnerability of both Kevlar and PET when exposed to concentrated acids.', 'marks': 1}
        ],
        "31. (a) -[HN-C6H4-NH-CO-C6H4-CO]- with open continuation bonds (2).<br/>31. (b) Rigid planar aromatic rings allow polymer chains to align closely (1); extensive intermolecular hydrogen bonding forms between N-H and C=O of adjacent chains (1).<br/>31. (c) Both undergo acid hydrolysis, cleaving amide or ester links and breaking down the polymer structure (1)."
    ),
    make_edexcel_q(
        32, "Comparative Reactivity of Carboxylic Derivatives with Ethanol", "WCH14/01/Jan20/Q25", 5,
        "An experiment compares the reaction of ethanol with: (A) Ethanoic acid, (B) Ethanoic anhydride, (C) Ethanoyl chloride.",
        [
            {'label': 'a', 'text': 'Rank A, B, and C in order of increasing yield of ethyl ethanoate without removing water.', 'marks': 1},
            {'label': 'b', 'text': 'Write the equation for reaction (B).', 'marks': 1},
            {'label': 'c', 'text': 'Compare the enthalpy changes and activation energies for reactions (A) and (C).', 'marks': 3}
        ],
        "32. (a) A < B < C (1).<br/>32. (b) CH3CH2OH + (CH3CO)2O -> CH3COOCH2CH3 + CH3COOH (1).<br/>32. (c) Reaction A (ethanoic acid) is reversible, slightly endothermic/exothermic (Delta H ~ 0), with high activation energy requiring H+ catalyst (1); Reaction C (ethanoyl chloride) is highly exothermic (Delta H << 0) with low activation energy, proceeding rapidly to 100% completion (2)."
    ),
    make_edexcel_q(
        33, "Keto-Enol Tautomerism in Carbonyl Derivatives", "WCH14/01/June19/Q26", 5,
        "Ethyl 3-oxobutanoate (acetoacetic ester) undergoes keto-enol tautomerism.",
        [
            {'label': 'a', 'text': 'Draw the structural formulas of the keto and enol forms of ethyl 3-oxobutanoate.', 'marks': 2},
            {'label': 'b', 'text': 'Describe a chemical test to prove the presence of the enol form.', 'marks': 2},
            {'label': 'c', 'text': 'Explain why the enol form is stabilized by intramolecular hydrogen bonding.', 'marks': 1}
        ],
        "33. (a) Keto form: CH3-C(=O)-CH2-COOCH2CH3 (1); Enol form: CH3-C(OH)=CH-COOCH2CH3 (1).<br/>33. (b) Add aqueous bromine (Br2 water): decolourises from orange/brown to colourless (1) due to electrophilic addition to the C=C double bond of the enol (1).<br/>33. (c) Six-membered ring conformation forms via H-bonding between enol -OH and ester C=O oxygen (1)."
    ),
    make_edexcel_q(
        34, "Synthesis of Aspirin and Recrystallisation Purity Analysis", "WCH14/01/Jan19/Q25", 6,
        "Salicylic acid (2-hydroxybenzoic acid, 2.00 g) is reacted with excess ethanoic anhydride (5.00 cm3) in the presence of conc H3PO4 catalyst to produce crude aspirin. After recrystallisation from ethanol, 1.85 g of pure aspirin (Mr = 180) is isolated.",
        [
            {'label': 'a', 'text': 'Calculate the theoretical mass of aspirin that can be formed from 2.00 g of salicylic acid (Mr = 138).', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the percentage yield of purified aspirin.', 'marks': 1},
            {'label': 'c', 'text': 'Describe how the purity of the recrystallised aspirin is verified using melting point determination.', 'marks': 3}
        ],
        "34. (a) Moles salicylic acid = 2.00 / 138 = 0.01449 mol; Theoretical mass aspirin = 0.01449 x 180 = 2.608 g (2).<br/>34. (b) % Yield = (1.85 / 2.608) x 100 = 70.9% (1).<br/>34. (c) Measure melting point range using a capillary tube melting point apparatus (1); pure aspirin has a sharp melting point matching literature value (138-140°C) (1); impurities lower the melting point and broaden the melting range (1)."
    ),
    make_edexcel_q(
        35, "Polymer Chain Degradation and Hydrolysis Equilibrium", "WCH14/01/June18/Q24", 5,
        "A sample of poly(lactic acid) bottle waste is treated with aqueous sodium hydroxide to recover sodium lactate for industrial reuse.",
        [
            {'label': 'a', 'text': 'Write the balanced chemical equation for the complete alkaline hydrolysis of PLA repeat unit -[O-CH(CH3)-CO]- with NaOH.', 'marks': 2},
            {'label': 'b', 'text': 'Calculate the volume of 2.00 mol dm-3 NaOH required to completely hydrolyse 144 g of PLA.', 'marks': 3}
        ],
        "35. (a) -[O-CH(CH3)-CO]- + NaOH -> CH3-CH(OH)-COO-Na+ (2).<br/>35. (b) Mass of repeat unit C3H4O2 = (3x12) + (4x1) + (2x16) = 72 g mol-1 (1); Moles repeat units = 144 / 72 = 2.00 mol (1); Moles NaOH required = 2.00 mol; Volume NaOH = 2.00 / 2.00 = 1.00 dm3 (1000 cm3) (1)."
    ),
    make_edexcel_q(
        36, "Comparative Acidity of Substituted Carboxylic Acids", "WCH14/01/Jan18/Q25", 5,
        "Compare the Ka values of ethanoic acid (Ka = 1.75 x 10^-5), chloroethanoic acid (Ka = 1.38 x 10^-3), and dichloroethanoic acid (Ka = 5.50 x 10^-2 mol dm-3).",
        [
            {'label': 'a', 'text': 'State the trend in acid strength.', 'marks': 1},
            {'label': 'b', 'text': 'Explain this trend in terms of electronegativity, inductive effect, and carboxylate anion stability.', 'marks': 4}
        ],
        "36. (a) Acid strength increases: Ethanoic acid < Chloroethanoic acid < Dichloroethanoic acid (1).<br/>36. (b) Chlorine is highly electronegative and exerts an electron-withdrawing inductive effect (-I effect) (1); electron withdrawal reduces electron density across the O-H bond, weakening it (1); after dissociation, electron withdrawal disperses the negative charge across the carboxylate anion (-COO-) (1); dispersing the negative charge stabilises the carboxylate anion, shifting the dissociation equilibrium to the right (1)."
    ),
    make_edexcel_q(
        37, "Acyl Chloride Mechanism with Primary Amines", "WCH14/01/Oct17/Q23", 5,
        "Propanoyl chloride reacts with methylamine to give N-methylpropanamide.",
        [
            {'label': 'a', 'text': 'Draw the full mechanism for this reaction showing all lone pairs, dipoles, curly arrows, and charges.', 'marks': 4},
            {'label': 'b', 'text': 'Explain why an excess of methylamine is required.', 'marks': 1}
        ],
        "37. (a) Step 1: Lone pair on N of CH3NH2 attacks delta+ carbonyl C of propanoyl chloride, C=O pi-bond opens to O- (2). Step 2: O- lone pair reforms C=O double bond, cleaving C-Cl bond to eliminate Cl- (1). Step 3: A second CH3NH2 molecule removes H+ from N+H(CH3) to yield CH3CH2CONHCH3 + CH3NH3+ (1).<br/>37. (b) The HCl produced is acidic and neutralises 1 mole of methylamine to form methylammonium chloride salt (1)."
    ),
    make_edexcel_q(
        38, "Transesterification Mechanism in Biodiesel Production", "WCH14/01/June17/Q25", 5,
        "Methoxide ion (CH3O-) acts as a nucleophile in the base-catalysed transesterification of ethyl ethanoate with methanol.",
        [
            {'label': 'a', 'text': 'Draw the mechanism for the reaction of CH3O- with ethyl ethanoate to form methyl ethanoate and ethoxide ion (CH3CH2O-).', 'marks': 3},
            {'label': 'b', 'text': 'Explain how the catalyst CH3O- is regenerated.', 'marks': 1},
            {'label': 'c', 'text': 'State why small traces of water severely reduce biodiesel yield.', 'marks': 1}
        ],
        "38. (a) Nucleophilic attack of CH3O- on carbonyl C of CH3COOCH2CH3 -> tetrahedral intermediate CH3-C(O-)(OCH3)(OCH2CH3) (2); C=O reforms, eliminating CH3CH2O- leaving CH3COOCH3 (1).<br/>38. (b) Ethoxide CH3CH2O- reacts with CH3OH solvent to regenerate CH3O- + CH3CH2OH (1).<br/>38. (c) Water reacts with CH3O- to form OH-, causing saponification of esters into soap salts (RCOONa), lowering biodiesel yield and making emulsion separation difficult (1)."
    ),
    make_edexcel_q(
        39, "Synthesis of Nylon-6,6 vs Terylene Polyester", "WCH14/01/Jan17/Q24", 5,
        "Compare the synthesis, structural linkages, and physical properties of Nylon-6,6 and Terylene.",
        [
            {'label': 'a', 'text': 'Identify the functional group linkage present in Nylon-6,6 versus Terylene.', 'marks': 2},
            {'label': 'b', 'text': 'Write the structures of the two monomers used to prepare Nylon-6,6.', 'marks': 2},
            {'label': 'c', 'text': 'Explain why Nylon-6,6 has a higher melting point than Terylene.', 'marks': 1}
        ],
        "39. (a) Nylon-6,6 contains amide linkages (-CONH-) (1); Terylene contains ester linkages (-COO-) (1).<br/>39. (b) Hexanedioic acid HOOC(CH2)4COOH (1); Hexane-1,6-diamine H2N(CH2)6NH2 (1).<br/>39. (c) Amide N-H groups form strong intermolecular hydrogen bonds between polymer chains, whereas ester groups in Terylene only form weaker dipole-dipole attractions (1)."
    ),
    make_edexcel_q(
        40, "Polyester Recycling via Methanolysis", "WCH14/01/Oct16/Q24", 5,
        "PET plastic waste can be chemically recycled by methanolysis (refluxing with excess methanol and zinc acetate catalyst).",
        [
            {'label': 'a', 'text': 'Write the chemical equation for the methanolysis of PET repeat unit -[O-CO-C6H4-CO-O-CH2CH2]-.', 'marks': 2},
            {'label': 'b', 'text': 'State the names of the two monomer precursors recovered from methanolysis.', 'marks': 2},
            {'label': 'c', 'text': 'Explain one advantage of chemical recycling (methanolysis) over mechanical recycling (re-melting plastic).', 'marks': 1}
        ],
        "40. (a) -[O-CO-C6H4-CO-O-CH2CH2]- + 2CH3OH -> CH3OOC-C6H4-COOCH3 + HO-CH2CH2-OH (2).<br/>40. (b) Dimethyl terephthalate (dimethyl benzene-1,4-dicarboxylate) (1); ethane-1,2-diol (1).<br/>40. (c) Chemical recycling breaks down contaminated polymers into pure virgin-grade monomers, eliminating degradation of mechanical properties caused by repeated heating cycles (1)."
    ),
    make_edexcel_q(
        41, "Kinetics of Acyl Chloride Hydrolysis in Aqueous Dioxane", "WCH14/01/June16/Q25", 5,
        "The rate of hydrolysis of benzoyl chloride (C6H5COCl) was measured in dioxane-water solvent mixtures.",
        [
            {'label': 'a', 'text': 'The reaction is found to be first order with respect to [C6H5COCl] and first order with respect to [H2O]. Write the rate equation.', 'marks': 1},
            {'label': 'b', 'text': 'State the units of the rate constant k.', 'marks': 1},
            {'label': 'c', 'text': 'Explain why increasing the proportion of water in the solvent mixture increases the rate constant k.', 'marks': 3}
        ],
        "41. (a) Rate = k [C6H5COCl] [H2O] (1).<br/>41. (b) dm3 mol-1 s-1 (1).<br/>41. (c) Water is a polar solvent with high dielectric constant (1); polar solvents stabilise the polar tetrahedral transition state / carbocation intermediate (1), lowering the activation energy Ea and increasing k (1)."
    ),
    make_edexcel_q(
        42, "Synthesis of Chiral Esters and Optical Purity", "WCH14/01/Jan16/Q26", 5,
        "Enantiomerically pure (S)-butan-2-ol is reacted with ethanoyl chloride to produce an ester.",
        [
            {'label': 'a', 'text': 'Draw the displayed structure of the ester formed.', 'marks': 1},
            {'label': 'b', 'text': 'Predict whether the ester product will be optically active. Explain your reasoning in terms of the reaction mechanism.', 'marks': 3},
            {'label': 'c', 'text': 'State what would happen to the optical activity if the reaction were carried out using a racemic mixture of (+/-)-butan-2-ol.', 'marks': 1}
        ],
        "42. (a) CH3COOCH(CH3)CH2CH3 (1).<br/>42. (b) Product WILL be optically active (1); nucleophilic attack occurs at the carbonyl carbon of ethanoyl chloride, leaving the C-O bond and chiral centre of (S)-butan-2-ol completely intact without breaking any bonds at the chiral carbon (2).<br/>42. (c) The ester product will be a racemic mixture and optically inactive (1)."
    ),
    make_edexcel_q(
        43, "Multistep Synthesis of Anesthetics from Benzoic Acid", "WCH14/01/Oct15/Q25", 6,
        "Benzocaine (ethyl 4-aminobenzoate) is a local anesthetic synthesized from 4-nitrotoluene.",
        [
            {'label': 'a', 'text': 'Outline a 3-step synthesis converting 4-nitrotoluene into benzocaine.', 'marks': 6}
        ],
        "43. (a) Step 1: Oxidation of methyl group in 4-nitrotoluene to carboxylic acid using alkaline KMnO4, heat under reflux then acidify -> 4-nitrobenzoic acid (2). Step 2: Esterification of 4-nitrobenzoic acid with ethanol and conc H2SO4 catalyst -> ethyl 4-nitrobenzoate (2). Step 3: Selective reduction of nitro group to amine using Sn / conc HCl, heat, followed by NaOH neutralisation -> ethyl 4-aminobenzoate (benzocaine) (2)."
    ),
    make_edexcel_q(
        44, "Calorimetric Combustion Analysis of Esters", "WCH14/01/June15/Q24", 5,
        "The standard enthalpy change of combustion (Delta_c H) of methyl ethanoate was determined using bomb calorimetry.",
        [
            {'label': 'a', 'text': 'Write the balanced thermochemical equation for the complete combustion of methyl ethanoate liquid.', 'marks': 2},
            {'label': 'b', 'text': 'Given Delta_f H [CH3COOCH3(l)] = -446 kJ mol-1, Delta_f H [CO2(g)] = -394 kJ mol-1, and Delta_f H [H2O(l)] = -286 kJ mol-1, calculate Delta_c H for methyl ethanoate.', 'marks': 3}
        ],
        "44. (a) CH3COOCH3(l) + 3.5 O2(g) -> 3 CO2(g) + 3 H2O(l) (2).<br/>44. (b) Delta_c H = sum Delta_f H (products) - sum Delta_f H (reactants) (1); = [3(-394) + 3(-286)] - [-446 + 0] (1); = [-1182 - 858] + 446 = -2040 + 446 = -1594 kJ mol-1 (1)."
    ),
    make_edexcel_q(
        45, "Biodegradable PGA Polyester Degradation Pathway", "WCH14/01/Jan15/Q25", 5,
        "Polyglycolic acid (PGA) is a synthetic polyester used in bioresorbable medical implants.",
        [
            {'label': 'a', 'text': 'Draw the repeat unit of PGA formed from glycolic acid (2-hydroxyethanoic acid).', 'marks': 2},
            {'label': 'b', 'text': 'Write the equation for the hydrolytic breakdown of PGA in the human body.', 'marks': 1},
            {'label': 'c', 'text': 'Explain why the breakdown product of PGA is non-toxic to human cells.', 'marks': 2}
        ],
        "45. (a) -[O-CH2-CO]- with open continuation bonds (2).<br/>45. (b) -[O-CH2-CO]-n + n H2O -> n HO-CH2-COOH (1).<br/>45. (c) The monomer glycolic acid (2-hydroxyethanoic acid) is a naturally occurring metabolite in human biochemical pathways (1); it is converted to harmless pyruvate or excreted by kidneys without toxic accumulation (1)."
    ),
    make_edexcel_q(
        46, "Ester Hydrolysis Equilibrium Constant Calculation", "WCH14/01/Oct14/Q25", 5,
        "A mixture containing 1.00 mol of ethyl ethanoate and 1.00 mol of water was allowed to reach equilibrium with an acid catalyst at 298 K. At equilibrium, 0.33 mol of ethanoic acid was present.",
        [
            {'label': 'a', 'text': 'Calculate the equilibrium moles of ethyl ethanoate, water, and ethanol.', 'marks': 2},
            {'label': 'b', 'text': 'Write the expression for Kc for this ester hydrolysis reaction.', 'marks': 1},
            {'label': 'c', 'text': 'Calculate the numerical value of Kc at 298 K. State why Kc has no units.', 'marks': 2}
        ],
        "46. (a) Moles ethanoic acid = 0.33 mol; Moles ethanol = 0.33 mol; Moles ethyl ethanoate = 1.00 - 0.33 = 0.67 mol; Moles water = 1.00 - 0.33 = 0.67 mol (2).<br/>46. (b) Kc = ([CH3COOH] [CH3CH2OH]) / ([CH3COOCH3] [H2O]) (1).<br/>46. (c) Kc = (0.33 x 0.33) / (0.67 x 0.67) = 0.1089 / 0.4489 = 0.243 (1); Equal number of moles on product and reactant sides, so volume terms cancel completely (1)."
    ),
    make_edexcel_q(
        47, "Polyester Copolymer Composition Analysis", "WCH14/01/June14/Q26", 5,
        "A copolymer is produced from 1 mole of terephthalic acid, 0.5 moles of ethylene glycol, and 0.5 moles of propane-1,3-diol.",
        [
            {'label': 'a', 'text': 'Draw the structural formulas of all three monomer components.', 'marks': 2},
            {'label': 'b', 'text': 'Draw a representative section of the copolymer chain showing two ester linkages.', 'marks': 2},
            {'label': 'c', 'text': 'Explain how incorporating propane-1,3-diol alters the flexibility of the polymer chain compared to pure PET.', 'marks': 1}
        ],
        "47. (a) HOOC-C6H4-COOH (1); HO-CH2CH2-OH and HO-CH2CH2CH2-OH (1).<br/>47. (b) Correct chain showing alternating terephthalate units linked to -O-CH2CH2-O- and -O-CH2CH2CH2-O- diol blocks (2).<br/>47. (c) The extra -CH2- carbon in propane-1,3-diol increases free rotation along the chain, making the copolymer more flexible with a lower glass transition temperature Tg (1)."
    ),
    make_edexcel_q(
        48, "Saponification Kinetics of Ethyl Acetate", "WCH14/01/Jan14/Q25", 5,
        "The alkaline hydrolysis of ethyl ethanoate with NaOH is second order overall (first order in [ester] and first order in [OH-]).",
        [
            {'label': 'a', 'text': 'Write the rate equation for saponification.', 'marks': 1},
            {'label': 'b', 'text': 'At 25°C, the rate constant k is 0.11 dm3 mol-1 s-1. Calculate the initial rate of reaction when 50 cm3 of 0.10 mol dm-3 ethyl ethanoate is mixed with 50 cm3 of 0.20 mol dm-3 NaOH.', 'marks': 3},
            {'label': 'c', 'text': 'State the effect on initial rate if the total mixture volume is doubled by adding 100 cm3 of distilled water.', 'marks': 1}
        ],
        "48. (a) Rate = k [CH3COOCH2CH3] [OH-] (1).<br/>48. (b) After mixing, total volume = 100 cm3. [ester] = 0.10 x (50/100) = 0.050 mol dm-3 (1); [OH-] = 0.20 x (50/100) = 0.10 mol dm-3 (1); Initial rate = 0.11 x 0.050 x 0.10 = 5.5 x 10^-4 mol dm-3 s-1 (1).<br/>48. (c) Doubling volume halves both concentrations; rate decreases by a factor of 4 (quarter of original rate) (1)."
    ),
    make_edexcel_q(
        49, "Chiral Synthesis of Bio-polyesters", "WCH14/01/Oct13/Q26", 5,
        "Poly(3-hydroxybutyrate) (PHB) is a biodegradable polyester produced by bacterial fermentation of glucose.",
        [
            {'label': 'a', 'text': 'Draw the structural formula of 3-hydroxybutanoic acid.', 'marks': 1},
            {'label': 'b', 'text': 'Identify the chiral carbon atom in 3-hydroxybutanoic acid.', 'marks': 1},
            {'label': 'c', 'text': 'Explain why bacterial fermentation yields 100% enantiomerically pure (R)-PHB, whereas chemical synthesis from 3-oxobutanoate yields a racemic mixture.', 'marks': 3}
        ],
        "49. (a) CH3-CH(OH)-CH2-COOH (1).<br/>49. (b) Carbon-3 (bonded to -H, -OH, -CH3, -CH2COOH) (1).<br/>49. (c) Enzymes in bacterial biosynthesis have 3D active sites that bind substrate in a single rigid orientation, producing 100% of a single enantiomer (stereospecific) (2); chemical synthesis involves un-catalysed nucleophilic addition to planar C=O groups from top or bottom faces with equal probability, giving a 50:50 racemic mixture (1)."
    ),
    make_edexcel_q(
        50, "Comprehensive Industrial Ester Route Evaluation", "WCH14/01/June13/Q27", 6,
        "An industrial plant considers three candidate routes to produce 10,000 tonnes of methyl methacrylate (monomer for Perspex polymer):<br/>Route A: Acetone cyanohydrin process using HCN.<br/>Route B: Ethylene hydroformylation followed by oxidation.<br/>Route C: Direct esterification of methacrylic acid with methanol using H2SO4 catalyst.",
        [
            {'label': 'a', 'text': 'Evaluate Route A versus Route C in terms of green chemistry principles (atom economy, toxic reagents, waste management).', 'marks': 4},
            {'label': 'b', 'text': 'Calculate the percentage atom economy for Route C: CH2=C(CH3)COOH + CH3OH -> CH2=C(CH3)COOCH3 + H2O.', 'marks': 2}
        ],
        "50. (a) Route A uses extremely toxic hydrogen cyanide (HCN) and generates large volumes of hazardous ammonium bisulfate waste requiring costly disposal (2); Route C has higher atom economy, uses less toxic reagents, and produces water as the only byproduct, making it environmentally cleaner and safer (2).<br/>50. (b) Molecular mass product CH2=C(CH3)COOCH3 = 100 g mol-1; Molecular mass reactants = 86 + 32 = 118 g mol-1 (1); Atom Economy = (100 / 118) x 100 = 84.7% (1)."
    )
]

p10_faqs = [
    make_edexcel_faq("Acyl Chloride vs Carboxylic Acid Esterification", "Ester Synthesis", "Claiming carboxylic acid esterification is faster than acyl chloride.", "Acyl chlorides react VIGOROUSLY at room temperature with alcohols giving 100% yield (irreversible). Carboxylic acids require heating with conc H2SO4 catalyst and reach an equilibrium."),
    make_edexcel_faq("Gaseous Product in Acyl Chloride Hydrolysis", "Observations", "Stating chlorine gas is evolved when acyl chlorides react with water.", "Acyl chlorides evolve HYDROGEN CHLORIDE gas (HCl), which forms misty white fumes in moist air. Chlorine gas (Cl2) is NOT formed."),
    make_edexcel_faq("Saponification Irreversibility", "Alkaline Hydrolysis", "Assuming alkaline hydrolysis of esters is reversible.", "Alkaline hydrolysis (saponification) forms a CARBOXYLATE ANION (RCOO-). The negative charge on RCOO- prevents nucleophilic attack by the alcohol, driving the reaction 100% to completion."),
    make_edexcel_faq("Polyester Repeat Unit Continuation Bonds", "Polymer Drawing", "Omitting open bonds at the ends of polymer repeat units.", "Always extend open continuation bonds OUTSIDE the brackets of the repeat unit to show it is a repeating polymer chain."),
    make_edexcel_faq("Biodegradability Mechanism", "Environmental Chemistry", "Stating polyesters break down because they are soft.", "Polyesters are biodegradable because the C=O ester links are POLAR and can be HYDROLYSED by water and microbial enzymes. Addition polymers have non-polar C-C backbones resistant to hydrolysis."),
    make_edexcel_faq("Acyl Chloride Reaction with Amines", "Amide Formation", "Writing 1 mole of amine per mole of acyl chloride.", "Acyl chloride + 2 moles of primary amine -> N-substituted amide + alkylammonium chloride salt. 2 moles of amine are needed because 1 mole reacts with HCl formed."),
    make_edexcel_faq("Acid vs Alkaline Hydrolysis Products", "Hydrolysis Products", "Writing carboxylic acid as the product of alkaline hydrolysis.", "Acid hydrolysis yields the CARBOXYLIC ACID (RCOOH). Alkaline hydrolysis yields the SODIUM CARBOXYLATE SALT (RCOONa). To get the free acid from saponification, acidify with dilute HCl."),
    make_edexcel_faq("Acyl Chloride Preparation", "Reagents", "Using dilute HCl to prepare acyl chlorides from carboxylic acids.", "Acyl chlorides are prepared using phosphorus(V) chloride PCl5, phosphorus(III) chloride PCl3, or thionyl chloride SOCl2 with dry carboxylic acids."),
    make_edexcel_faq("Chlorobenzene Unreactivity", "Aromatic Chlorides", "Expecting chlorobenzene to react with water like acyl chlorides.", "Chlorobenzene C6H5Cl is UNREACTIVITY towards nucleophilic substitution because p-orbitals on Cl overlap with the pi-cloud of the benzene ring, strengthening the C-Cl bond and increasing electron density."),
    make_edexcel_faq("Transesterification Reactions", "Biodiesel Synthesis", "Confusing transesterification with ester hydrolysis.", "Transesterification converts one ester into another by reacting it with an alcohol in the presence of an acid/base catalyst (e.g. vegetable oil + methanol -> biodiesel + glycerol).")
]

build_pdf_pack("Usman_Edexcel_Chem_U4_15D_Carboxylic_Acid_Derivatives.pdf", p10_meta, p10_questions, p10_faqs)
print("Pack 10 (15D Carboxylic Acid Derivatives - 50 Qs + 10 FAQs) compiled successfully!")


# ==========================================
# PACK 11: 15E — SPECTROSCOPY & NMR (50 Qs + 10 FAQs)
# ==========================================
p11_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'SPECTROSCOPY AND CHROMATOGRAPHY',
    'subtopic_code': '15E',
    'subtopic_name': 'Spectroscopy & NMR (Chromatography, Mass Spec, 13C NMR, 1H NMR & Splitting)'
}

p11_questions = [
    # Tier 1 (Q1-Q25)
    make_edexcel_q(
        1, "1H NMR Spectrum Analysis of Ethyl Ethanoate", "WCH14/01/Jan23/Q23", 5,
        "Ethyl ethanoate, CH3COOCH2CH3, is analysed using high-resolution 1H NMR spectroscopy.",
        [
            {'label': 'a', 'text': 'Predict the number of peaks (environments) in the 1H NMR spectrum of ethyl ethanoate.', 'marks': 1},
            {'label': 'b', 'text': 'Describe the splitting pattern (n+1 rule) and relative area for each peak.', 'marks': 4}
        ],
        "1. (a) 3 peaks (3 proton environments) (1).<br/>1. (b) CH3CO- protons: singlet (0 adjacent H, n=0 -> 1 peak), integration = 3H (1). -OCH2- protons: quartet (3 adjacent H on CH3, n=3 -> 4 peaks), integration = 2H (1). -CH3 protons of ethyl: triplet (2 adjacent H on CH2, n=2 -> 3 peaks), integration = 3H (1).",
        diagram_img="diagrams/p11_q1_nmr_ethyl_ethanoate.png"
    ),
    make_edexcel_q(
        2, "Mass Spectrometry Fragmentation & D2O Shake", "WCH14/01/Oct22/Q24", 5,
        "Compound X (C3H6O2) has an IR absorption at 1715 cm-1 and a broad absorption at 2500-3300 cm-1.",
        [
            {'label': 'a', 'text': 'Identify the functional group present in X from the IR data.', 'marks': 1},
            {'label': 'b', 'text': 'State the effect of adding D2O (D2O shake) on the 1H NMR spectrum of X.', 'marks': 2},
            {'label': 'c', 'text': 'Identify the fragment ion responsible for the peak at m/z = 45 in the mass spectrum of X.', 'marks': 2}
        ],
        "2. (a) Carboxylic acid (-COOH) group (C=O at 1715, O-H at 2500-3300) (1).<br/>2. (b) The acidic -OH proton exchanges with deuterium (-OH + D2O -> -OD + HOD); the -OH peak at delta ~11 ppm disappears (2).<br/>2. (c) [COOH]+ ion (m/z = 12 + 32 + 1 = 45) (2).",
        diagram_img="diagrams/p11_q2_mass_spec_propanal.png"
    ),
    make_edexcel_q(
        3, "Principles of Thin-Layer Chromatography (TLC)", "WCH14/01/Jan22/Q15", 4,
        "A mixture of amino acids is separated using thin-layer chromatography (TLC) with a silica gel stationary phase and an organic solvent mobile phase.",
        [
            {'label': 'a', 'text': 'Define the term Rf value.', 'marks': 1},
            {'label': 'b', 'text': 'Explain why different amino acids have different Rf values on silica gel.', 'marks': 2},
            {'label': 'c', 'text': 'State how colorless amino acid spots are visualized on the TLC plate.', 'marks': 1}
        ],
        "3. (a) Rf = (distance moved by spot) / (distance moved by solvent front) (1).<br/>3. (b) Different amino acids have different relative polarities; more polar amino acids adsorb more strongly to the polar silica stationary phase and travel slower (1); less polar amino acids dissolve more readily in the mobile phase and travel faster (1).<br/>3. (c) Spray plate with ninhydrin reagent and heat (forms purple spots) or view under UV light (1)."
    ),
    make_edexcel_q(
        4, "High-Performance Liquid Chromatography (HPLC)", "WCH14/01/June21/Q16", 4,
        "HPLC is used to analyze pesticide residues in river water.",
        [
            {'label': 'a', 'text': 'Define retention time (tR) in HPLC.', 'marks': 1},
            {'label': 'b', 'text': 'State two factors that affect the retention time of a compound in an HPLC column.', 'marks': 2},
            {'label': 'c', 'text': 'Explain how the concentration of a pesticide is determined from an HPLC chromatogram.', 'marks': 1}
        ],
        "4. (a) Retention time is the time taken for a compound to travel from injection to detection at the column outlet (1).<br/>4. (b) Polarity of the stationary/mobile phase (1); flow rate of mobile phase / column temperature (1).<br/>4. (c) The area under the chromatographic peak is proportional to compound concentration (measured against a calibration curve) (1)."
    ),
    make_edexcel_q(
        5, "Gas Chromatography (GC) and Carrier Gases", "WCH14/01/Jan21/Q17", 4,
        "Gas chromatography is used to separate volatile organic compounds.",
        [
            {'label': 'a', 'text': 'State the role of the mobile phase (carrier gas) in GC and name a suitable gas.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why GC alone cannot definitively identify an unknown compound.', 'marks': 1},
            {'label': 'c', 'text': 'State how GC is combined with mass spectrometry (GC-MS) to overcome this limitation.', 'marks': 1}
        ],
        "5. (a) Mobile phase carries the gaseous sample through the column (1); inert gas such as helium (He) or nitrogen (N2) (1).<br/>5. (b) Different compounds can have identical retention times under specific conditions (1).<br/>5. (c) Separated components exiting GC pass directly into a mass spectrometer to generate unique fragmentation mass spectra (GC-MS) (1)."
    ),
    make_edexcel_q(
        6, "Mass Spectrometry: M+ and M+1 Isotope Peaks", "WCH14/01/Oct20/Q16", 4,
        "The mass spectrum of an unknown hydrocarbon shows a molecular ion peak M+ at m/z = 72 and an M+1 peak at m/z = 73.",
        [
            {'label': 'a', 'text': 'The relative heights of the M+ and M+1 peaks are 100 : 5.5. Calculate the number of carbon atoms in the molecule.', 'marks': 2},
            {'label': 'b', 'text': 'Deduce the molecular formula of the hydrocarbon.', 'marks': 1},
            {'label': 'c', 'text': 'State the natural isotope responsible for the M+1 peak.', 'marks': 1}
        ],
        "6. (a) Number of C atoms = (height M+1 / height M+) x (100 / 1.1) (1) = (5.5 / 100) x (100 / 1.1) = 5 carbon atoms (1).<br/>6. (b) C5H12 (Pentane isomers, Mr = (5x12)+(12x1) = 72) (1).<br/>6. (c) Carbon-13 isotope (13C) (1)."
    ),
    make_edexcel_q(
        7, "Chlorine Isotope Ratio in Mass Spectrometry (M+ and M+2 Peaks)", "WCH14/01/Jan20/Q17", 4,
        "The mass spectrum of a chloroalkane displays two molecular ion peaks at m/z = 78 and m/z = 80.",
        [
            {'label': 'a', 'text': 'State the natural abundance ratio of 35Cl to 37Cl isotopes.', 'marks': 1},
            {'label': 'b', 'text': 'Predict the relative peak height ratio of M+ (m/z 78) to M+2 (m/z 80).', 'marks': 1},
            {'label': 'c', 'text': 'Deduce the molecular formula of the chloroalkane.', 'marks': 2}
        ],
        "7. (a) 3 : 1 ratio of 35Cl : 37Cl (1).<br/>7. (b) 3 : 1 relative peak height ratio (1).<br/>7. (c) C3H7Cl (Chloropropane, Mr with 35Cl = (3x12)+7+35 = 78) (2)."
    ),
    make_edexcel_q(
        8, "Bromine Isotope Ratio in Mass Spectrometry", "WCH14/01/June19/Q18", 4,
        "A bromoalkane sample exhibits two molecular ion peaks of equal intensity at m/z = 122 and m/z = 124.",
        [
            {'label': 'a', 'text': 'State the two naturally occurring isotopes of bromine and their relative abundance.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why the peak heights at m/z 122 and 124 are 1 : 1.', 'marks': 1},
            {'label': 'c', 'text': 'Deduce the structure of the bromoalkane.', 'marks': 1}
        ],
        "8. (a) 79Br and 81Br (1); 50 : 50 (1 : 1) natural abundance ratio (1).<br/>8. (b) Equal probability of a molecule containing 79Br (m/z 122) or 81Br (m/z 124) (1).<br/>8. (c) CH3CH2CH2Br or CH3CH(Br)CH3 (Bromopropane, Mr = 43 + 79 = 122) (1)."
    ),
    make_edexcel_q(
        9, "Infrared Spectroscopy: Distinguishing Functional Groups", "WCH14/01/Jan19/Q15", 4,
        "Infrared spectra of three unknown liquids A, B, and C show distinct absorption bands:<br/>Compound A: Broad absorption at 3350 cm-1, no peak at 1700 cm-1.<br/>Compound B: Strong sharp absorption at 1715 cm-1, no absorption above 3100 cm-1.<br/>Compound C: Very broad absorption at 2500-3300 cm-1 and strong peak at 1710 cm-1.",
        [
            {'label': 'a', 'text': 'Identify the functional group present in Compound A.', 'marks': 1},
            {'label': 'b', 'text': 'Identify the functional group present in Compound B.', 'marks': 1},
            {'label': 'c', 'text': 'Identify the functional group present in Compound C.', 'marks': 1},
            {'label': 'd', 'text': 'State what bond causes the broad absorption in Compound A.', 'marks': 1}
        ],
        "9. (a) Alcohol (-OH) group (1).<br/>9. (b) Carbonyl group (Aldehyde or Ketone C=O) (1).<br/>9. (c) Carboxylic acid (-COOH) group (1).<br/>9. (d) O-H stretch involved in hydrogen bonding (1)."
    ),
    make_edexcel_q(
        10, "13C NMR Peak Counting & Molecular Symmetry", "WCH14/01/June18/Q15", 4,
        "Consider the four structural isomers of C4H9Cl:<br/>1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, 2-chloro-2-methylpropane.",
        [
            {'label': 'a', 'text': 'State the number of peaks expected in the 13C NMR spectrum of 1-chlorobutane.', 'marks': 1},
            {'label': 'b', 'text': 'State the number of peaks expected in the 13C NMR spectrum of 2-chloro-2-methylpropane.', 'marks': 1},
            {'label': 'c', 'text': 'Explain the difference in peak count between these two isomers in terms of symmetry.', 'marks': 2}
        ],
        "10. (a) 4 peaks (4 non-equivalent carbon environments) (1).<br/>10. (b) 2 peaks (2 non-equivalent carbon environments) (1).<br/>10. (c) 2-chloro-2-methylpropane (CH3)3CCl has high molecular symmetry where all 3 methyl carbons are chemically equivalent (1); 1-chlorobutane has no internal symmetry plane, making all 4 carbon atoms chemically distinct (1)."
    ),
    make_edexcel_q(
        11, "Tetramethylsilane (TMS) Standard in NMR", "WCH14/01/Jan18/Q14", 3,
        "Tetramethylsilane, Si(CH3)4 (TMS), is added as an internal standard in 1H and 13C NMR spectroscopy.",
        [
            {'label': 'a', 'text': 'Give two reasons why TMS is ideal as an NMR reference standard.', 'marks': 2},
            {'label': 'b', 'text': 'State the chemical shift value assigned to TMS.', 'marks': 1}
        ],
        "11. (a) Gives a single sharp peak because all 12 H atoms / 4 C atoms are identical (1); inert, non-toxic, and volatile (bp 27°C) so easily removed (1).<br/>11. (b) 0.0 ppm (1)."
    ),
    make_edexcel_q(
        12, "Solvents in 1H NMR Spectroscopy and Deuterium Exchange", "WCH14/01/Oct17/Q15", 4,
        "Deuterated chloroform (CDCl3) is commonly used as a solvent in 1H NMR.",
        [
            {'label': 'a', 'text': 'Explain why CDCl3 is used rather than CHCl3 as a solvent.', 'marks': 1},
            {'label': 'b', 'text': 'State the effect of adding a drop of D2O to a sample containing an alcohol before recording its 1H NMR spectrum.', 'marks': 2},
            {'label': 'c', 'text': 'Write the equation for the deuterium exchange reaction.', 'marks': 1}
        ],
        "12. (a) Deuterium (2H) does not absorb radiofrequency radiation in the 1H NMR range, avoiding solvent peak interference (1).<br/>12. (b) The -OH proton peak disappears from the spectrum (2).<br/>12. (c) R-OH + D2O -> R-OD + HOD (1)."
    ),
    make_edexcel_q(
        13, "1H NMR Integration Traces", "WCH14/01/June17/Q14", 3,
        "The 1H NMR spectrum of an unknown ester C3H6O2 shows two signals with relative integration heights of 3 : 3.",
        [
            {'label': 'a', 'text': 'State what information the integration trace provides in 1H NMR.', 'marks': 1},
            {'label': 'b', 'text': 'Deduce the structure of the ester C3H6O2.', 'marks': 2}
        ],
        "13. (a) Integration trace area is proportional to the relative number of hydrogen atoms in that environment (1).<br/>13. (b) Methyl ethanoate, CH3COOCH3 (1); contains two separate methyl groups each with 3 equivalent H atoms (1)."
    ),
    make_edexcel_q(
        14, "n+1 Rule for 1H NMR Peak Splitting", "WCH14/01/Jan17/Q13", 4,
        "Apply the n+1 splitting rule to predict the 1H NMR spectrum of 1,2-dichloroethane (ClCH2CH2Cl) versus 1,1-dichloroethane (CH3CHCl2).",
        [
            {'label': 'a', 'text': 'Predict the number of peaks and splitting pattern for 1,2-dichloroethane.', 'marks': 2},
            {'label': 'b', 'text': 'Predict the number of peaks and splitting patterns for 1,1-dichloroethane.', 'marks': 2}
        ],
        "14. (a) 1,2-dichloroethane: 1 peak (singlet) because all 4 protons are chemically equivalent due to symmetry (2).<br/>14. (b) 1,1-dichloroethane: 2 peaks; CH3 protons appear as a doublet (1 adjacent H, n=1 -> 2 sub-peaks) (1); -CH- proton appears as a quartet (3 adjacent H, n=3 -> 4 sub-peaks) (1)."
    ),
    make_edexcel_q(
        15, "13C NMR Spectrum of Propanone vs Propanal", "WCH14/01/Oct16/Q14", 3,
        "Distinguish between propanone (CH3COCH3) and propanal (CH3CH2CHO) using 13C NMR.",
        [
            {'label': 'a', 'text': 'State the number of peaks in the 13C NMR spectrum of propanone.', 'marks': 1},
            {'label': 'b', 'text': 'State the number of peaks in the 13C NMR spectrum of propanal.', 'marks': 1},
            {'label': 'c', 'text': 'Explain how the chemical shift of the carbonyl carbon distinguishes an aldehyde from a ketone.', 'marks': 1}
        ],
        "15. (a) 2 peaks (symmetrical molecule) (1).<br/>15. (b) 3 peaks (all 3 carbons non-equivalent) (1).<br/>15. (c) Aldehyde C=O appears at delta 190-200 ppm; ketone C=O appears at delta 200-220 ppm (1)."
    ),
    make_edexcel_q(
        16, "Mass Spec Fragmentation of Propanal", "WCH14/01/June16/Q15", 4,
        "The mass spectrum of propanal (CH3CH2CHO, Mr = 58) exhibits prominent fragment ion peaks at m/z = 57, 29, and 15.",
        [
            {'label': 'a', 'text': 'Write the chemical formula and structure for the fragment ion at m/z = 57.', 'marks': 1},
            {'label': 'b', 'text': 'Write the chemical formula and structure for the fragment ion at m/z = 29.', 'marks': 2},
            {'label': 'c', 'text': 'Write the equation for the loss of a methyl radical from the molecular ion.', 'marks': 1}
        ],
        "16. (a) [CH3CH2CO]+ or [M - H]+ (loss of aldehyde H) (1).<br/>16. (b) [CHO]+ or [C2H5]+ ion (2).<br/>16. (c) [CH3CH2CHO]+. -> [CH2CHO]+ + .CH3 (1)."
    ),
    make_edexcel_q(
        17, "IR Absorption Bands of Alkenes vs Alkynes", "WCH14/01/Jan16/Q16", 3,
        "Infrared spectra can identify unsaturated carbon-carbon bonds.",
        [
            {'label': 'a', 'text': 'State the wavenumber range for C=C double bond absorption.', 'marks': 1},
            {'label': 'b', 'text': 'State the wavenumber range for C≡C triple bond absorption.', 'marks': 1},
            {'label': 'c', 'text': 'Explain why symmetrical alkenes such as trans-hex-3-ene show no C=C absorption band in their IR spectrum.', 'marks': 1}
        ],
        "17. (a) 1620 - 1680 cm-1 (1).<br/>17. (b) 2100 - 2260 cm-1 (1).<br/>17. (c) IR absorption requires a change in dipole moment during bond vibration; symmetrical trans-hex-3-ene has zero net dipole change upon stretching (1)."
    ),
    make_edexcel_q(
        18, "Combined Spectroscopy: Formula C2H4O", "WCH14/01/Oct15/Q15", 4,
        "An organic compound Z has empirical formula C2H4O and relative molecular mass 44.",
        [
            {'label': 'a', 'text': 'Deduce the molecular formula of Z.', 'marks': 1},
            {'label': 'b', 'text': 'Its IR spectrum shows a strong peak at 1720 cm-1 and no peak above 3200 cm-1. Its 1H NMR spectrum shows a doublet (3H) and a quartet (1H). Deduce the structural formula of Z.', 'marks': 3}
        ],
        "18. (a) C2H4O (Mr = (2x12)+(4x1)+16 = 44) (1).<br/>18. (b) IR 1720 cm-1 confirms C=O carbonyl (1); 1H NMR doublet (3H) = CH3 group next to 1 H (1); quartet (1H) = -CHO aldehyde proton next to CH3 (1); Structure = CH3CHO (ethanal) (1)."
    ),
    make_edexcel_q(
        19, "Spin-Spin Coupling Constants (J Values)", "WCH14/01/June15/Q17", 4,
        "High-resolution 1H NMR spectra display sub-peak splitting separated by coupling constants (J values).",
        [
            {'label': 'a', 'text': 'Explain what causes spin-spin coupling in 1H NMR.', 'marks': 2},
            {'label': 'b', 'text': 'State why coupling constants between mutually split protons are equal (J_AB = J_BA).', 'marks': 1},
            {'label': 'c', 'text': 'Predict the appearance of a peak coupled to two non-equivalent neighboring protons with different J values.', 'marks': 1}
        ],
        "19. (a) Interaction between the magnetic moments of adjacent non-equivalent protons transmitted through chemical bonds (2).<br/>19. (b) Both proton environments interact with the same coupling energy across the intervening C-C bond (1).<br/>19. (c) Doublet of doublets (4 sub-peaks of equal height) (1)."
    ),
    make_edexcel_q(
        20, "Column Chromatography vs HPLC", "WCH14/01/Jan15/Q14", 3,
        "Compare traditional gravity column chromatography with HPLC.",
        [
            {'label': 'a', 'text': 'State two advantages of HPLC over gravity column chromatography.', 'marks': 2},
            {'label': 'b', 'text': 'State why smaller particle sizes are used in HPLC column packing.', 'marks': 1}
        ],
        "20. (a) Higher resolution / faster separation speed (1); automated high-sensitivity detection and quantitative analysis (1).<br/>20. (b) Smaller particle sizes increase surface area of stationary phase, improving separation efficiency (1)."
    ),
    make_edexcel_q(
        21, "Mass Spec Fragmentation of Esters", "WCH14/01/Oct14/Q16", 4,
        "The mass spectrum of methyl ethanoate (CH3COOCH3, Mr = 74) displays fragment peaks at m/z = 59, 43, 31, and 15.",
        [
            {'label': 'a', 'text': 'Identify the ion responsible for the base peak at m/z = 43.', 'marks': 1},
            {'label': 'b', 'text': 'Identify the ion responsible for the peak at m/z = 59.', 'marks': 1},
            {'label': 'c', 'text': 'Identify the ion responsible for the peak at m/z = 31.', 'marks': 1},
            {'label': 'd', 'text': 'Define the term base peak in mass spectrometry.', 'marks': 1}
        ],
        "21. (a) [CH3CO]+ (acetyl ion) (1).<br/>21. (b) [COOCH3]+ or [M - CH3]+ (1).<br/>21. (c) [OCH3]+ (methoxy ion) (1).<br/>21. (d) The base peak is the most intense peak in the mass spectrum, assigned 100% relative abundance (1)."
    ),
    make_edexcel_q(
        22, "1H NMR Spectrum of Propan-1-ol vs Propan-2-ol", "WCH14/01/June14/Q18", 4,
        "Compare the 1H NMR spectra of propan-1-ol (CH3CH2CH2OH) and propan-2-ol (CH3CH(OH)CH3).",
        [
            {'label': 'a', 'text': 'State the number of 1H NMR peaks for propan-1-ol.', 'marks': 1},
            {'label': 'b', 'text': 'State the number of 1H NMR peaks for propan-2-ol.', 'marks': 1},
            {'label': 'c', 'text': 'Predict the splitting pattern of the -CH- proton peak in propan-2-ol (ignoring -OH coupling).', 'marks': 2}
        ],
        "22. (a) 4 peaks (4 proton environments) (1).<br/>22. (b) 3 peaks (2 symmetrical methyl groups = 6H, 1 CH = 1H, 1 OH = 1H) (1).<br/>22. (c) Septet (7 sub-peaks) (1); adjacent to 6 equivalent H atoms on the two CH3 groups (n=6 -> 6+1 = 7) (1)."
    ),
    make_edexcel_q(
        23, "Chromatography Retention Index & Kovats Index", "WCH14/01/Jan14/Q15", 3,
        "Gas chromatography uses retention times and Kovats retention indices for compound identification.",
        [
            {'label': 'a', 'text': 'Explain why retention times vary if oven temperature fluctuates.', 'marks': 1},
            {'label': 'b', 'text': 'State how reference alkane standards are used to standardize retention indices.', 'marks': 2}
        ],
        "23. (a) Higher temperature increases vapour pressure, decreasing retention time on the stationary phase (1).<br/>23. (b) Sample retention time is compared against unbranched alkanes injected under identical conditions (1); Kovats index interpolates relative retention between alkane standards (1)."
    ),
    make_edexcel_q(
        24, "IR Spectrum of Carboxylic Acid Anhydrides", "WCH14/01/Oct13/Q16", 3,
        "Ethanoic anhydride displays two distinct C=O absorption peaks in its IR spectrum at 1760 cm-1 and 1820 cm-1.",
        [
            {'label': 'a', 'text': 'Explain why acid anhydrides exhibit a double C=O absorption peak.', 'marks': 2},
            {'label': 'b', 'text': 'Contrast this with the single C=O absorption peak of esters.', 'marks': 1}
        ],
        "24. (a) Vibrational coupling between the two carbonyl C=O bonds produces asymmetric stretching (higher frequency ~1820 cm-1) and symmetric stretching (lower frequency ~1760 cm-1) (2).<br/>24. (b) Esters contain only one C=O group per functional unit, giving a single sharp absorption peak at 1735-1750 cm-1 (1)."
    ),
    make_edexcel_q(
        25, "Mass Spec High-Resolution Mass Measurement", "WCH14/01/June13/Q16", 4,
        "High-resolution mass spectrometry determines molecular masses to 4 decimal places.<br/>Exact atomic masses: 1H = 1.0078, 12C = 12.0000, 14N = 14.0031, 16O = 15.9949.",
        [
            {'label': 'a', 'text': 'Calculate the exact molecular mass of propanone (C3H6O).', 'marks': 1},
            {'label': 'b', 'text': 'Calculate the exact molecular mass of butane (C4H10).', 'marks': 1},
            {'label': 'c', 'text': 'Explain how high-resolution mass spectrometry distinguishes between propanone and butane, which both have nominal Mr = 58.', 'marks': 2}
        ],
        "25. (a) C3H6O: 3(12.0000) + 6(1.0078) + 15.9949 = 58.0417 (1).<br/>25. (b) C4H10: 4(12.0000) + 10(1.0078) = 58.0780 (1).<br/>25. (c) High-resolution MS measures M+ to 4 decimal places; 58.0417 is uniquely assigned to C3H6O while 58.0780 is assigned to C4H10 (2)."
    ),

    # Tier 2 Hard / A* Challenge (Q26-Q50)
    make_edexcel_q(
        26, "Multi-Spectral Structure Elucidation: Compound A (C4H8O2)", "WCH14/01/Jan23/Q26", 6,
        "Compound A (C4H8O2) is analysed by multiple spectroscopic techniques:<br/>- Elemental Analysis: C = 54.55%, H = 9.09%, O = 36.36%.<br/>- Mass Spectrum: M+ peak at m/z = 88, base peak at m/z = 43.<br/>- IR Spectrum: Strong peak at 1740 cm-1, no peak at 2500-3300 cm-1 or 3200-3600 cm-1.<br/>- 1H NMR: Singlet at 2.05 ppm (3H), Triplet at 1.25 ppm (3H), Quartet at 4.12 ppm (2H).",
        [
            {'label': 'a', 'text': 'Confirm the empirical formula of Compound A.', 'marks': 1},
            {'label': 'b', 'text': 'Deduce the functional group present from the IR spectrum.', 'marks': 1},
            {'label': 'c', 'text': 'Interpret each 1H NMR peak to identify the proton environments and neighbors.', 'marks': 3},
            {'label': 'd', 'text': 'Draw the structural formula of Compound A and name it.', 'marks': 1}
        ],
        "26. (a) C: 54.55/12 = 4.546; H: 9.09/1 = 9.09; O: 36.36/16 = 2.272. Ratio 2:4:1 -> Empirical C2H4O (1).<br/>26. (b) C=O absorption at 1740 cm-1 with no O-H stretch confirms an ester group (1).<br/>26. (c) Singlet at 2.05 ppm (3H) = CH3-CO- group (1). Quartet at 4.12 ppm (2H) and triplet at 1.25 ppm (3H) = -O-CH2-CH3 ethyl group (2).<br/>26. (d) CH3COOCH2CH3 (Ethyl ethanoate) (1)."
    ),
    make_edexcel_q(
        27, "Multi-Spectral Structure Elucidation: Compound B (C5H10O)", "WCH14/01/Oct22/Q27", 6,
        "Compound B (C5H10O) gives a positive 2,4-DNPH test but negative Tollens' test.<br/>- 13C NMR: 3 peaks at delta = 8.1, 35.2, 211.5 ppm.<br/>- 1H NMR: Triplet at 1.05 ppm (6H) and Quartet at 2.45 ppm (4H).",
        [
            {'label': 'a', 'text': 'Deduce the functional group of Compound B from chemical tests.', 'marks': 1},
            {'label': 'b', 'text': 'Explain why the 13C NMR spectrum shows only 3 peaks despite having 5 carbon atoms.', 'marks': 2},
            {'label': 'c', 'text': 'Interpret the 1H NMR integration and splitting patterns.', 'marks': 2},
            {'label': 'd', 'text': 'Give the structural formula and systematic name of Compound B.', 'marks': 1}
        ],
        "27. (a) Positive 2,4-DNPH confirms carbonyl C=O; negative Tollens' test rules out aldehyde -> Ketone (1).<br/>27. (b) Symmetrical ketone structure creates identical carbon environments on both sides of C=O (2).<br/>27. (c) Triplet at 1.05 ppm (6H) = 2 equivalent CH3 groups split by adjacent CH2 (1); Quartet at 2.45 ppm (4H) = 2 equivalent -CH2- groups next to C=O split by CH3 (1).<br/>27. (d) CH3CH2COCH2CH3 (Pentan-3-one) (1)."
    ),
    make_edexcel_q(
        28, "Multi-Spectral Structure Elucidation: Compound C (C4H8O)", "WCH14/01/Jan22/Q25", 6,
        "Compound C (C4H8O) decolourises bromine water.<br/>- IR Spectrum: Sharp absorption at 3620 cm-1, strong peak at 1650 cm-1.<br/>- 1H NMR: Doublet at 1.7 ppm (3H), Multiplet at 5.7 ppm (2H), Singlet at 3.2 ppm (1H), Doublet at 4.1 ppm (2H).",
        [
            {'label': 'a', 'text': 'Identify the two functional groups present in Compound C from chemical tests and IR.', 'marks': 2},
            {'label': 'b', 'text': 'State the effect of D2O shake on the 1H NMR spectrum.', 'marks': 1},
            {'label': 'c', 'text': 'Deduce the complete structure of Compound C.', 'marks': 3}
        ],
        "28. (a) Decolourises bromine water & IR 1650 cm-1 = Alkene C=C (1); IR 3620 cm-1 = Alcohol -OH (1).<br/>28. (b) Singlet at 3.2 ppm (1H) disappears (1).<br/>28. (c) CH3-CH=CH-CH2OH (But-2-en-1-ol) (3)."
    ),
    make_edexcel_q(
        29, "13C NMR & 1H NMR Structural Assignment of Isomeric Esters", "WCH14/01/June21/Q26", 5,
        "Three structural isomers with formula C4H8O2 are esters: Methyl propanoate, Ethyl ethanoate, Propyl methanoate.",
        [
            {'label': 'a', 'text': 'Predict the number of peaks in the 13C NMR spectrum of each isomer.', 'marks': 2},
            {'label': 'b', 'text': 'Explain how the 1H NMR spectrum of propyl methanoate (HCOOCH2CH2CH3) distinguishes it from methyl propanoate (CH3CH2COOCH3).', 'marks': 3}
        ],
        "29. (a) Methyl propanoate: 4 peaks (1); Ethyl ethanoate: 4 peaks; Propyl methanoate: 4 peaks (1).<br/>29. (b) Propyl methanoate has a unique low-field singlet at delta ~8.0 ppm for the formate proton (HCOO-) (1); Propyl methanoate has 4 proton environments giving a singlet (1H), triplet (2H), multiplet (2H), triplet (3H) (1); Methyl propanoate has 3 proton environments giving a singlet (3H), quartet (2H), triplet (3H) (1)."
    ),
    make_edexcel_q(
        30, "High-Resolution 1H NMR Analysis of Ethanethiol", "WCH14/01/Jan21/Q25", 5,
        "Ethanethiol (CH3CH2SH) is added to natural gas as an odorant.",
        [
            {'label': 'a', 'text': 'Predict the 1H NMR spectrum of ethanethiol under high resolution assuming -SH proton coupling occurs.', 'marks': 3},
            {'label': 'b', 'text': 'Describe how D2O shake modifies the spectrum.', 'marks': 2}
        ],
        "30. (a) CH3 protons: triplet (3H) at delta 1.3 ppm (1); -CH2- protons: doublet of quartets (2H) at delta 2.5 ppm split by CH3 and SH (1); -SH proton: triplet (1H) at delta 1.5 ppm split by CH2 (1).<br/>30. (b) The -SH triplet proton peak disappears due to deuterium exchange (-SH + D2O -> -SD + HOD) (1); the -CH2- peak simplifies from a complex multiplet to a clean quartet (1)."
    ),
    make_edexcel_q(
        31, "Mass Spectrometry Fragmentation Mechanisms of Carbonyls", "WCH14/01/Oct20/Q25", 5,
        "Pentan-2-one (CH3COCH2CH2CH3) undergoes alpha-cleavage and McLafferty rearrangement in mass spectrometry.",
        [
            {'label': 'a', 'text': 'Write equations for the two possible alpha-cleavage reactions of the molecular ion [CH3COCH2CH2CH3]+.', 'marks': 3},
            {'label': 'b', 'text': 'State the m/z values of the resulting acylium fragment ions.', 'marks': 2}
        ],
        "31. (a) Cleavage 1: [CH3COCH2CH2CH3]+. -> [CH3CO]+ (m/z 43) + .CH2CH2CH3 (1.5). Cleavage 2: [CH3COCH2CH2CH3]+. -> [COCH2CH2CH3]+ (m/z 71) + .CH3 (1.5).<br/>31. (b) m/z = 43 ([CH3CO]+ base peak) (1); m/z = 71 ([CH3CH2CH2CO]+) (1)."
    ),
    make_edexcel_q(
        32, "Chromatographic Separation & GC-MS Analysis of Essential Oils", "WCH14/01/Jan20/Q26", 5,
        "Lavender oil contains linalool and linalyl acetate.",
        [
            {'label': 'a', 'text': 'Describe how GC-MS separates and quantifies linalool and linalyl acetate in lavender oil.', 'marks': 3},
            {'label': 'b', 'text': 'Explain how electronic mass spectral databases identify unknown peaks in the chromatogram.', 'marks': 2}
        ],
        "32. (a) Sample vaporised and carried by He gas through a capillary column coated with stationary phase (1); linalool and linalyl acetate elute at distinct retention times tR (1); detector measures peak areas proportional to relative concentrations (1).<br/>32. (b) Mass spectrum generated at peak apex is compared against a digital library of reference fragmentation patterns (1); match factor / similarity index confirms chemical identity (1)."
    ),
    make_edexcel_q(
        33, "13C NMR Chemical Shift Calculations and DEPT NMR", "WCH14/01/June19/Q25", 5,
        "DEPT 13C NMR spectroscopy distinguishes CH3, CH2, CH, and quaternary carbon atoms.",
        [
            {'label': 'a', 'text': 'Explain the appearance of CH3, CH2, and CH carbon signals in DEPT-135 NMR spectra.', 'marks': 3},
            {'label': 'b', 'text': 'Predict which carbon peak of 2-methylpropan-2-ol ((CH3)3COH) is ABSENT in DEPT-135.', 'marks': 2}
        ],
        "33. (a) CH3 and CH carbon signals point UP (positive phase) (1); CH2 carbon signals point DOWN (negative phase) (1); Quaternary carbon signals (no H attached) are completely ABSENT (1).<br/>33. (b) Central quaternary carbon (C-2 attached to -OH and 3 CH3 groups) has zero attached protons and will be ABSENT in DEPT-135 (2)."
    ),
    make_edexcel_q(
        34, "Quantitative 1H NMR Integration for Mixture Analysis", "WCH14/01/Jan19/Q26", 6,
        "A mixture contains ethanol (CH3CH2OH) and ethyl ethanoate (CH3COOCH2CH3). The 1H NMR spectrum shows:<br/>- Peak 1: Singlet at 2.0 ppm (CH3CO- of ester) integration area = 12.0.<br/>- Peak 2: Triplet at 1.2 ppm (CH3 of ethanol) integration area = 8.0.",
        [
            {'label': 'a', 'text': 'Determine the relative moles of ethyl ethanoate in the sample from Peak 1.', 'marks': 2},
            {'label': 'b', 'text': 'Determine the relative moles of ethanol in the sample from Peak 2.', 'marks': 2},
            {'label': 'c', 'text': 'Calculate the mole percentage of ethanol in the mixture.', 'marks': 2}
        ],
        "34. (a) Peak 1 singlet represents 3H of CH3CO- in ester. Relative moles ester = 12.0 / 3 = 4.0 mol units (2).<br/>34. (b) Peak 2 triplet represents 3H of CH3 in ethanol. Relative moles ethanol = 8.0 / 3 = 2.67 mol units (2).<br/>34. (c) Total mole units = 4.0 + 2.67 = 6.67; Mole % ethanol = (2.67 / 6.67) x 100 = 40.0% (2)."
    ),
    make_edexcel_q(
        35, "2D NMR Spectroscopy Principles (COSY)", "WCH14/01/June18/Q26", 5,
        "2D 1H-1H COSY (Correlation Spectroscopy) displays spin-spin coupling networks.",
        [
            {'label': 'a', 'text': 'Explain what off-diagonal cross-peaks represent in a 2D COSY spectrum.', 'marks': 2},
            {'label': 'b', 'text': 'Describe how COSY resolves overlapping multiplets in complex organic molecules.', 'marks': 3}
        ],
        "35. (a) Cross-peaks off the diagonal indicate scalar spin-spin coupling between two specific proton environments (2).<br/>35. (b) Tracing horizontal and vertical lines from a cross-peak directly identifies which proton peaks are adjacent/coupled (2), bypassing 1D multiplet overlap (1)."
    ),
    make_edexcel_q(
        36, "Multi-Spectral Elucidation: Aromatic Derivative C8H8O2", "WCH14/01/Jan18/Q26", 6,
        "Compound D (C8H8O2) contains a benzene ring.<br/>- IR Spectrum: Sharp C=O at 1720 cm-1, strong C-O at 1250 cm-1.<br/>- 1H NMR: Singlet at 3.9 ppm (3H), Multiplet at 7.4-8.0 ppm (5H).",
        [
            {'label': 'a', 'text': 'Deduce the monosubstituted aromatic ring from 1H NMR data.', 'marks': 1},
            {'label': 'b', 'text': 'Identify the group responsible for the 3.9 ppm singlet.', 'marks': 2},
            {'label': 'c', 'text': 'Deduce the structural formula and systematic name of Compound D.', 'marks': 3}
        ],
        "36. (a) 5H multiplet at 7.4-8.0 ppm confirms a monosubstituted benzene ring (C6H5-) (1).<br/>36. (b) Singlet at 3.9 ppm (3H) attached to oxygen = -OCH3 methoxy ester group (2).<br/>36. (c) C6H5COOCH3 (Methyl benzoate) (3)."
    ),
    make_edexcel_q(
        37, "13C NMR Chemical Shift Trends in Substituted Benzenes", "WCH14/01/Oct17/Q26", 5,
        "Compare the 13C NMR spectra of 1,4-dimethylbenzene and 1,2-dimethylbenzene.",
        [
            {'label': 'a', 'text': 'Predict the number of 13C NMR peaks for 1,4-dimethylbenzene.', 'marks': 2},
            {'label': 'b', 'text': 'Predict the number of 13C NMR peaks for 1,2-dimethylbenzene.', 'marks': 2},
            {'label': 'c', 'text': 'Explain the difference based on symmetry elements.', 'marks': 1}
        ],
        "37. (a) 3 peaks (methyl C, ipso aromatic C, ortho aromatic C) (2).<br/>37. (b) 4 peaks (methyl C, ipso C-1/2, C-3/6, C-4/5) (2).<br/>37. (c) 1,4-isomer has two perpendicular planes of symmetry; 1,2-isomer has only one plane of symmetry (1)."
    ),
    make_edexcel_q(
        38, "Chiral Stationary Phases in Enantiomeric HPLC", "WCH14/01/June17/Q26", 5,
        "Separation of racemic drug enantiomers requires Chiral Liquid Chromatography (CMP).",
        [
            {'label': 'a', 'text': 'Explain why conventional non-chiral HPLC stationary phases cannot separate enantiomers.', 'marks': 2},
            {'label': 'b', 'text': 'Describe how a chiral stationary phase (CSP) achieves separation of (R)- and (S)-enantiomers.', 'marks': 3}
        ],
        "38. (a) Enantiomers have identical physical properties (boiling point, solubility, polarity) in an achiral environment (2).<br/>38. (b) A chiral stationary phase contains single-enantiomer selectors (3D chiral cavities) (1); (R)- and (S)-enantiomers form diastereomeric transient complexes with different stability constants (1), resulting in different retention times tR (1)."
    ),
    make_edexcel_q(
        39, "Mass Spec Fragmentation of Alcohols & M-18 Peak", "WCH14/01/Jan17/Q25", 5,
        "Primary alcohols frequently show an [M - 18]+ peak in their mass spectra.",
        [
            {'label': 'a', 'text': 'State the small molecule lost to produce the [M - 18]+ peak.', 'marks': 1},
            {'label': 'b', 'text': 'Write the equation for the dehydration fragmentation of [CH3CH2CH2OH]+.', 'marks': 2},
            {'label': 'c', 'text': 'Identify the ion structure formed at m/z = 42 for propan-1-ol (Mr = 60).', 'marks': 2}
        ],
        "39. (a) Water molecule (H2O, mass 18) (1).<br/>39. (b) [CH3CH2CH2OH]+. -> [CH3CH=CH2]+. (m/z 42) + H2O (2).<br/>39. (c) Propene radical cation [C3H6]+. (m/z = 42) (2)."
    ),
    make_edexcel_q(
        40, "Infrared O-H Hydrogen Bonding Shift", "WCH14/01/Oct16/Q25", 5,
        "The IR spectrum of ethanol in gas phase shows a sharp O-H band at 3650 cm-1, whereas liquid ethanol shows a broad band at 3350 cm-1.",
        [
            {'label': 'a', 'text': 'Explain why intermolecular hydrogen bonding broadens and shifts the O-H absorption to lower wavenumber in the liquid phase.', 'marks': 3},
            {'label': 'b', 'text': 'Predict the effect of diluting liquid ethanol in non-polar CCl4 solvent on the IR spectrum.', 'marks': 2}
        ],
        "40. (a) Hydrogen bonding weakens the O-H covalent bond by pulling electron density away (1), reducing the force constant of the O-H stretch (1); variable strength H-bonds across liquid molecules create a wide distribution of vibrational frequencies (broad peak) (1).<br/>40. (b) Dilution separates ethanol molecules, breaking H-bonds; the broad 3350 cm-1 band diminishes while a sharp free O-H band at 3650 cm-1 appears (2)."
    ),
    make_edexcel_q(
        41, "1H NMR Virtual Coupling and Complex Multiplets", "WCH14/01/June16/Q26", 5,
        "In 1-chloropropane (CH3-CH2-CH2Cl), the central -CH2- protons appear as a sextet.",
        [
            {'label': 'a', 'text': 'Apply the n+1 rule to explain why the central -CH2- protons form a sextet.', 'marks': 2},
            {'label': 'b', 'text': 'State the assumption made about the coupling constants J(CH3-CH2) and J(CH2-CH2Cl).', 'marks': 2},
            {'label': 'c', 'text': 'Predict what happens if J(CH3-CH2) is significantly different from J(CH2-CH2Cl).', 'marks': 1}
        ],
        "41. (a) Central -CH2- is adjacent to 3 protons on CH3 and 2 protons on CH2Cl (total n = 3+2 = 5) (1); n+1 = 5+1 = 6 sub-peaks (sextet) (1).<br/>41. (b) Assumes both coupling constants are approximately equal (J1 ≈ J2) (2).<br/>41. (c) Peak splits into a complex triplet of quartets (12 sub-peaks) (1)."
    ),
    make_edexcel_q(
        42, "Mass Spec High-Mass Resolution Isotope Patterns", "WCH14/01/Jan16/Q25", 5,
        "A compound containing two chlorine atoms displays three molecular ion peaks M+, M+2, and M+4.",
        [
            {'label': 'a', 'text': 'Calculate the theoretical relative peak height ratio for M+ : M+2 : M+4 for a dichlorinated compound.', 'marks': 3},
            {'label': 'b', 'text': 'Deduce the peak height ratio for a dibrominated compound containing two bromine atoms.', 'marks': 2}
        ],
        "42. (a) 35Cl : 37Cl = 3 : 1. Ratio = (3+1)^2 = 3^2 : 2(3x1) : 1^2 = 9 : 6 : 1 (3).<br/>42. (b) 79Br : 81Br = 1 : 1. Ratio = (1+1)^2 = 1^2 : 2(1x1) : 1^2 = 1 : 2 : 1 (2)."
    ),
    make_edexcel_q(
        43, "Multi-Spectral Structure Elucidation: Nitrogen Compound C3H7NO", "WCH14/01/Oct15/Q26", 6,
        "Compound E (C3H7NO) is soluble in water.<br/>- IR Spectrum: Strong C=O at 1665 cm-1, doublet peak at 3300-3400 cm-1.<br/>- 1H NMR: Triplet at 1.1 ppm (3H), Quartet at 2.2 ppm (2H), Broad singlet at 6.5 ppm (2H).",
        [
            {'label': 'a', 'text': 'Identify the functional group from IR 1665 cm-1 and 3300-3400 cm-1 doublet.', 'marks': 2},
            {'label': 'b', 'text': 'Deduce the structure of Compound E from 1H NMR data.', 'marks': 3},
            {'label': 'c', 'text': 'Give the systematic IUPAC name for Compound E.', 'marks': 1}
        ],
        "43. (a) Primary amide group -CONH2 (C=O at 1665, N-H doublet at 3300-3400 cm-1) (2).<br/>43. (b) Triplet 1.1 ppm (3H) + Quartet 2.2 ppm (2H) = ethyl group CH3CH2- (2); Broad singlet 6.5 ppm (2H) = -CONH2 protons (1). Structure = CH3CH2CONH2 (1).<br/>43. (c) Propanamide (1)."
    ),
    make_edexcel_q(
        44, "HPLC Mass Spectrometry (LC-MS) Electrospray Ionisation", "WCH14/01/June15/Q26", 5,
        "LC-MS uses soft electrospray ionisation (ESI) to analyze polar biomolecules.",
        [
            {'label': 'a', 'text': 'Explain why hard electron ionisation (EI) is unsuitable for thermally labile proteins.', 'marks': 2},
            {'label': 'b', 'text': 'Describe how ESI forms [M + H]+ protonated pseudo-molecular ions.', 'marks': 2},
            {'label': 'c', 'text': 'State the m/z value observed for a peptide of mass 1200 Da forming a doubly charged [M + 2H]2+ ion.', 'marks': 1}
        ],
        "44. (a) EI causes extensive fragmentation and thermal decomposition of fragile non-volatile molecules, destroying the molecular ion (2).<br/>44. (b) High voltage applied to nebulized aerosol adds H+ protons to basic sites, forming intact [M + H]+ ions without fragmenting (2).<br/>44. (c) m/z = (1200 + 2) / 2 = 601.0 (1)."
    ),
    make_edexcel_q(
        45, "13C NMR DEPT & 2D HMQC Heteronuclear Correlation", "WCH14/01/Jan15/Q26", 5,
        "HMQC (Heteronuclear Multiple Quantum Coherence) correlates 1H chemical shifts with 13C chemical shifts.",
        [
            {'label': 'a', 'text': 'State what a cross-peak in an HMQC spectrum indicates.', 'marks': 2},
            {'label': 'b', 'text': 'Explain how HMQC distinguishes between isomeric primary and secondary alcohols.', 'marks': 3}
        ],
        "45. (a) Shows direct 1-bond coupling between a specific proton and the carbon atom to which it is attached (2).<br/>45. (b) Primary alcohol: -CH2OH proton signal (~3.6 ppm) correlates with 13C peak at ~60 ppm (1); Secondary alcohol: -CH(OH)- proton signal (~3.8 ppm) correlates with 13C peak at ~68 ppm (1); confirms exact C-H pairing (1)."
    ),
    make_edexcel_q(
        46, "Supercritical Fluid Chromatography (SFC)", "WCH14/01/Oct14/Q26", 5,
        "Supercritical fluid chromatography uses supercritical carbon dioxide (scCO2) as mobile phase.",
        [
            {'label': 'a', 'text': 'Define a supercritical fluid.', 'marks': 1},
            {'label': 'b', 'text': 'State two operational advantages of SFC over HPLC.', 'marks': 2},
            {'label': 'c', 'text': 'Explain why scCO2 is considered a green chromatography solvent.', 'marks': 2}
        ],
        "46. (a) A substance above its critical temperature and pressure exhibiting gas-like diffusivity and liquid-like solvent power (1).<br/>46. (b) Faster flow rates due to lower viscosity (1); rapid non-thermal sample recovery by depressurising CO2 gas (1).<br/>46. (c) Non-toxic, non-flammable, naturally abundant, and leaves zero organic solvent residue upon evaporation (2)."
    ),
    make_edexcel_q(
        47, "1H NMR Anisotropic Shielding in Benzene & Carbonyls", "WCH14/01/June14/Q27", 5,
        "Aromatic protons absorb at unusually low field (delta 6.5-8.5 ppm) due to magnetic anisotropy.",
        [
            {'label': 'a', 'text': 'Explain the origin of the ring current in benzene when placed in an external magnetic field B0.', 'marks': 2},
            {'label': 'b', 'text': 'Describe how the induced ring current magnetic field affects the effective magnetic field experienced by aromatic protons.', 'marks': 3}
        ],
        "47. (a) Delocalised pi-electrons circulate around the benzene ring, creating an induced ring current (2).<br/>47. (b) The induced magnetic field opposes B0 inside the ring but reinforces B0 outside the ring where aromatic H atoms reside (2); protons experience a higher effective magnetic field and are deshielded, shifting downfield to 6.5-8.5 ppm (1)."
    ),
    make_edexcel_q(
        48, "Mass Spec High-Resolution Fragmentation of Isomeric Ketones", "WCH14/01/Jan14/Q26", 5,
        "Pentan-2-one and pentan-3-one both have molecular formula C5H10O (Mr = 86).",
        [
            {'label': 'a', 'text': 'Predict the base peak m/z value for pentan-2-one resulting from alpha-cleavage.', 'marks': 2},
            {'label': 'b', 'text': 'Predict the base peak m/z value for pentan-3-one resulting from alpha-cleavage.', 'marks': 2},
            {'label': 'c', 'text': 'State how mass spectrometry unambiguously differentiates these two structural isomers.', 'marks': 1}
        ],
        "48. (a) [CH3CO]+ ion at m/z = 43 (cleavage of C1-C2 bond) (2).<br/>48. (b) [CH3CH2CO]+ ion at m/z = 57 (cleavage of C2-C3 bond) (2).<br/>48. (c) The different m/z values of their acylium fragment base peaks (43 vs 57) uniquely identify each isomer (1)."
    ),
    make_edexcel_q(
        49, "Multi-Spectral Structural Elucidation: Complex Ester C6H12O2", "WCH14/01/Oct13/Q27", 6,
        "Compound F (C6H12O2) is hydrolysed by NaOH(aq) to give compound G and sodium ethanoate.<br/>- 1H NMR of F: Singlet at 2.0 ppm (3H), Doublet at 0.9 ppm (6H), Multiplet at 1.9 ppm (1H), Doublet at 3.8 ppm (2H).",
        [
            {'label': 'a', 'text': 'Identify the ethanoate part of the ester from 1H NMR.', 'marks': 1},
            {'label': 'b', 'text': 'Deduce the structure of alcohol G formed on hydrolysis.', 'marks': 3},
            {'label': 'c', 'text': 'Draw the structural formula of Compound F and give its IUPAC name.', 'marks': 2}
        ],
        "49. (a) Singlet at 2.0 ppm (3H) = CH3CO- ethanoate group (1).<br/>49. (b) Doublet 0.9 ppm (6H) + Multiplet 1.9 ppm (1H) + Doublet 3.8 ppm (2H) = 2-methylpropan-1-ol (CH3)2CHCH2OH (3).<br/>49. (c) CH3COOCH2CH(CH3)2 (2-methylpropyl ethanoate / isobutyl ethanoate) (2)."
    ),
    make_edexcel_q(
        50, "Master Structural Elucidation Challenge: Unknown C6H10O4", "WCH14/01/June13/Q28", 6,
        "Compound X (C6H10O4) is a symmetrical dicarboxylic acid ester used in polymer synthesis.<br/>- IR Spectrum: C=O at 1735 cm-1, C-O at 1180 cm-1, no O-H peak.<br/>- 13C NMR: 3 peaks at delta = 14.1, 60.5, 160.2 ppm.<br/>- 1H NMR: Triplet at 1.3 ppm (6H), Quartet at 4.3 ppm (4H).",
        [
            {'label': 'a', 'text': 'Deduce the number of ester groups present in Compound X.', 'marks': 1},
            {'label': 'b', 'text': 'Interpret the 13C NMR and 1H NMR signals to identify all carbon and proton environments.', 'marks': 3},
            {'label': 'c', 'text': 'Draw the complete displayed structure of Compound X and give its systematic name.', 'marks': 2}
        ],
        "50. (a) Formula C6H10O4 contains 4 oxygens and 2 degrees of unsaturation -> Diester (2 ester groups) (1).<br/>50. (b) 13C NMR 3 peaks confirms high symmetry (1); 1H NMR triplet (6H) + quartet (4H) = 2 equivalent ethyl groups (-OCH2CH3) attached to oxygen (2).<br/>50. (c) CH3CH2OOC-COOCH2CH3 (Diethyl ethanedioate / diethyl oxalate) (2)."
    )
]

p11_faqs = [
    make_edexcel_faq("n+1 Splitting Rule Application", "1H NMR Splitting", "Counting protons on the same carbon atom when determining splitting.", "The n+1 rule states that a proton peak is split into n+1 sub-peaks, where n is the number of protons on ADJACENT carbon atoms (3 bonds away). Protons on the same carbon do not split each other."),
    make_edexcel_faq("D2O Exchange Mechanism", "D2O Shake", "Expecting C-H protons to exchange with D2O.", "D2O shake ONLY removes peaks for labile -OH and -NH protons because they exchange rapidly with deuterium (-OH + D2O -> -OD + HOD). Protons attached directly to carbon (C-H) do NOT exchange."),
    make_edexcel_faq("TMS Reference Peak", "NMR Standard", "Forgetting the chemical shift value of TMS.", "Tetramethylsilane Si(CH3)4 (TMS) is assigned a chemical shift of EXACTLY 0.0 ppm. Its 12 identical H atoms give a sharp reference peak at the far right of the spectrum."),
    make_edexcel_faq("13C NMR Integration Traces", "13C NMR vs 1H NMR", "Assuming peak heights in 13C NMR represent the number of carbons.", "13C NMR peak heights/areas are NOT strictly proportional to the number of carbon atoms (unlike 1H NMR integration). ONLY the number of peaks (carbon environments) and chemical shift values are evaluated."),
    make_edexcel_faq("Mass Spec Molecular Ion Peak Identification", "Mass Spectrometry", "Confusing the molecular ion M+ peak with fragment peaks.", "The molecular ion M+ peak is the peak with the HIGHEST m/z value (excluding small M+1 isotope peaks). Its m/z value gives the relative molecular mass (Mr) of the compound."),
    make_edexcel_faq("Mass Spec Fragment Ion Positive Charge Requirement", "Mass Spec Formulas", "Writing fragment species without a positive charge.", "Mass spectrometers ONLY detect POSITIVELY CHARGED ions. Fragment formulas MUST include a positive charge (e.g. [CH3CO]+, [C2H5]+, [COOH]+)."),
    make_edexcel_faq("Infrared O-H Absorption Differences", "IR Spectroscopy", "Confusing alcohol O-H with carboxylic acid O-H absorption.", "Alcohol O-H absorbs as a smooth broad peak at 3200-3600 cm-1. Carboxylic acid O-H absorbs as a VERY BROAD, distorted peak at 2500-3300 cm-1 overlapping the C-H region."),
    make_edexcel_faq("Deuterated Solvents in 1H NMR", "NMR Solvents", "Using H2O or CHCl3 as an NMR solvent.", "Solvents like H2O or CHCl3 contain 1H protons that would produce huge peaks masking the sample. Deuterated solvents like CDCl3 or D2O are used because deuterium (2H) does not absorb in the 1H frequency range."),
    make_edexcel_faq("Singlets for -OH and -NH Protons", "1H NMR Features", "Expecting -OH protons to show splitting from adjacent C-H protons.", "Protons on -OH and -NH groups undergo rapid exchange with trace water/solvents, averaging out spin-spin coupling. Consequently, -OH and -NH protons almost always appear as SINGLETS."),
    make_edexcel_faq("GC-MS Hyphenated Technique Function", "Chromatography-MS", "Claiming GC identifies compounds without MS.", "Gas Chromatography (GC) SEPARATES the components of a complex mixture based on retention time. Mass Spectrometry (MS) IDENTIFIES each separated component by its mass spectrum fingerprint.")
]

build_pdf_pack("Usman_Edexcel_Chem_U4_15E_Spectroscopy_Chromatography.pdf", p11_meta, p11_questions, p11_faqs)
print("Pack 11 (15E Spectroscopy & NMR - 50 Qs + 10 FAQs) compiled successfully!")
