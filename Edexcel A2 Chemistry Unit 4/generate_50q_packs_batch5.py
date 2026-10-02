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
# PACK 10: 15D — CARBOXYLIC ACID DERIVATIVES (50 Qs + 10 FAQs)
# ==========================================
p10_meta = {
    'candidate': 'Usman',
    'topic_code': 'Topic 15',
    'topic_name': 'CARBOXYLIC ACID DERIVATIVES AND POLYESTERS',
    'subtopic_code': '15D',
    'subtopic_name': 'Carboxylic Acid Derivatives (Acyl Chlorides, Esters & Polyesters)'
}

p10_questions = []

p10_questions.append(make_edexcel_q(
    1, "Acyl Chloride Reactivity with Water", "WCH14/01/Jan23/Q21", 4,
    "Ethanoyl chloride (CH3COCl) reacts vigorously with water at room temperature.",
    [
        {'label': 'a', 'text': 'Write the balanced equation for the reaction of ethanoyl chloride with water.', 'marks': 1},
        {'label': 'b', 'text': 'State the observation and name the gaseous product formed.', 'marks': 2},
        {'label': 'c', 'text': 'Explain why ethanoyl chloride is much more reactive towards water than chlorobenzene.', 'marks': 1}
    ],
    "1. (a) CH3COCl + H2O -> CH3COOH + HCl (1).<br/>1. (b) Misty / steamy white fumes (1); hydrogen chloride gas (HCl) (1).<br/>1. (c) Carbonyl C in CH3COCl is highly electron deficient (delta+) attached to two electronegative atoms (O and Cl); chlorobenzene has p-orbital overlap with benzene ring strengthening C-Cl bond (1)."
))

p10_questions.append(make_edexcel_q(
    2, "Acid vs Alkaline Hydrolysis of Esters", "WCH14/01/Oct22/Q22", 5,
    "Compare the acid-catalysed hydrolysis and alkaline hydrolysis (saponification) of methyl propanoate.",
    [
        {'label': 'a', 'text': 'Write the equation for the acid-catalysed hydrolysis of methyl propanoate using dilute H2SO4.', 'marks': 2},
        {'label': 'b', 'text': 'Write the equation for the alkaline hydrolysis of methyl propanoate using aqueous NaOH.', 'marks': 2},
        {'label': 'c', 'text': 'Explain why alkaline hydrolysis goes to completion whereas acid hydrolysis is an equilibrium.', 'marks': 1}
    ],
    "2. (a) CH3CH2COOCH3 + H2O ⇌ CH3CH2COOH + CH3OH (2).<br/>2. (b) CH3CH2COOCH3 + NaOH -> CH3CH2COONa + CH3OH (2).<br/>2. (c) Alkaline hydrolysis forms carboxylate ion CH3CH2COO- which is non-reactive towards nucleophilic attack by CH3OH (1)."
))

for i in range(3, 26):
    p10_questions.append(make_edexcel_q(
        i, f"Esterification & Acyl Chloride Reaction Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider ester derivative {i}: CH3COCl + R-OH -> CH3COOR + HCl.",
        [
            {'label': 'a', 'text': 'State one advantage of using an acyl chloride rather than a carboxylic acid to prepare an ester.', 'marks': 2},
            {'label': 'b', 'text': 'State one disadvantage of using an acyl chloride.', 'marks': 1}
        ],
        f"{i}. (a) Reaction is fast at room temperature (1) and goes to 100% completion (irreversible) (1).<br/>{i}. (b) Produces toxic / corrosive HCl gas fumes (1)."
    ))

for i in range(26, 51):
    p10_questions.append(make_edexcel_q(
        i, f"A* Challenge: Condensation Polymers & Biodegradability {i}", f"WCH14/01/Hard/Q{i}", 5,
        f"Terylene (PET) is formed by the condensation polymerisation of benzene-1,4-dicarboxylic acid and ethane-1,2-diol.",
        [
            {'label': 'a', 'text': 'Draw the repeat unit of Terylene showing all ester linkages.', 'marks': 2},
            {'label': 'b', 'text': 'Explain why polyesters are biodegradable in the environment whereas poly(ethene) is non-biodegradable.', 'marks': 3}
        ],
        f"{i}. (a) -O-CO-C6H4-CO-O-CH2-CH2- with open continuation bonds at ends (2).<br/>{i}. (b) Polyesters contain polar C=O and C-O ester bonds (1) susceptible to nucleophilic attack / hydrolysis by water and enzymes (1). Poly(ethene) contains strong non-polar C-C and C-H bonds resistant to chemical and enzymatic attack (1)."
    ))

p10_faqs = []
p10_faq_titles = [
    ("Acyl Chloride vs Carboxylic Acid Esterification", "Ester Synthesis", "Claiming carboxylic acid esterification is faster than acyl chloride.", "Acyl chlorides react VIGOROUSLY at room temperature with alcohols giving 100% yield (irreversible). Carboxylic acids require heating with conc H2SO4 catalyst and reach an equilibrium."),
    ("Gaseous Product in Acyl Chloride Hydrolysis", "Observations", "Stating chlorine gas is evolved when acyl chlorides react with water.", "Acyl chlorides evolve HYDROGEN CHLORIDE gas (HCl), which forms misty white fumes in moist air. Chlorine gas (Cl2) is NOT formed."),
    ("Saponification Irreversibility", "Alkaline Hydrolysis", "Assuming alkaline hydrolysis of esters is reversible.", "Alkaline hydrolysis (saponification) forms a CARBOXYLATE ANION (RCOO-). The negative charge on RCOO- prevents nucleophilic attack by the alcohol, driving the reaction 100% to completion."),
    ("Polyester Repeat Unit Continuation Bonds", "Polymer Drawing", "Omitting open bonds at the ends of polymer repeat units.", "Always extend open continuation bonds OUTSIDE the brackets of the repeat unit to show it is a repeating polymer chain."),
    ("Biodegradability Mechanism", "Environmental Chemistry", "Stating polyesters break down because they are soft.", "Polyesters are biodegradable because the C=O ester links are POLAR and can be HYDROLYSED by water and microbial enzymes. Addition polymers have non-polar C-C backbones resistant to hydrolysis."),
    ("Acyl Chloride Reaction with Amines", "Amide Formation", "Writing 1 mole of amine per mole of acyl chloride.", "Acyl chloride + 2 moles of primary amine -> N-substituted amide + alkylammonium chloride salt. 2 moles of amine are needed because 1 mole reacts with HCl formed."),
    ("Acid vs Alkaline Hydrolysis Products", "Hydrolysis Products", "Writing carboxylic acid as the product of alkaline hydrolysis.", "Acid hydrolysis yields the CARBOXYLIC ACID (RCOOH). Alkaline hydrolysis yields the SODIUM CARBOXYLATE SALT (RCOONa). To get the free acid from saponification, acidify with dilute HCl."),
    ("Acyl Chloride Preparation", "Reagents", "Using dilute HCl to prepare acyl chlorides from carboxylic acids.", "Acyl chlorides are prepared using phosphorus(V) chloride PCl5, phosphorus(III) chloride PCl3, or thionyl chloride SOCl2 with dry carboxylic acids."),
    ("Chlorobenzene Unreactivity", "Aromatic Chlorides", "Expecting chlorobenzene to react with water like acyl chlorides.", "Chlorobenzene C6H5Cl is UNREACTIVITY towards nucleophilic substitution because p-orbitals on Cl overlap with the pi-cloud of the benzene ring, strengthening the C-Cl bond and increasing electron density."),
    ("Transesterification Reactions", "Biodiesel Synthesis", "Confusing transesterification with ester hydrolysis.", "Transesterification converts one ester into another by reacting it with an alcohol in the presence of an acid/base catalyst (e.g. vegetable oil + methanol -> biodiesel + glycerol).")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p10_faq_titles, 1):
    p10_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

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

p11_questions = []

p11_questions.append(make_edexcel_q(
    1, "1H NMR Spectrum Analysis of Ethyl Ethanoate", "WCH14/01/Jan23/Q23", 5,
    "Ethyl ethanoate, CH3COOCH2CH3, is analysed using high-resolution 1H NMR spectroscopy.",
    [
        {'label': 'a', 'text': 'Predict the number of peaks (environments) in the 1H NMR spectrum of ethyl ethanoate.', 'marks': 1},
        {'label': 'b', 'text': 'Describe the splitting pattern (n+1 rule) and relative area for each peak.', 'marks': 4}
    ],
    "1. (a) 3 peaks (3 proton environments) (1).<br/>1. (b) CH3CO- protons: singlet (0 adjacent H, n=0 -> 1 peak), integration = 3H (1). -OCH2- protons: quartet (3 adjacent H on CH3, n=3 -> 4 peaks), integration = 2H (1). -CH3 protons of ethyl: triplet (2 adjacent H on CH2, n=2 -> 3 peaks), integration = 3H (1)."
))

p11_questions.append(make_edexcel_q(
    2, "Mass Spectrometry Fragmentation & D2O Shake", "WCH14/01/Oct22/Q24", 5,
    "Compound X (C3H6O2) has an IR absorption at 1715 cm-1 and a broad absorption at 2500-3300 cm-1.",
    [
        {'label': 'a', 'text': 'Identify the functional group present in X from the IR data.', 'marks': 1},
        {'label': 'b', 'text': 'State the effect of adding D2O (D2O shake) on the 1H NMR spectrum of X.', 'marks': 2},
        {'label': 'c', 'text': 'Identify the fragment ion responsible for the peak at m/z = 45 in the mass spectrum of X.', 'marks': 2}
    ],
    "2. (a) Carboxylic acid (-COOH) group (C=O at 1715, O-H at 2500-3300) (1).<br/>2. (b) The acidic -OH proton exchanges with deuterium (-OH + D2O -> -OD + HOD); the -OH peak at delta ~11 ppm disappears (2).<br/>2. (c) [COOH]+ ion (m/z = 12 + 32 + 1 = 45) (2)."
))

for i in range(3, 26):
    p11_questions.append(make_edexcel_q(
        i, f"13C NMR & Chromatography Step {i}", f"WCH14/01/Sample/Q{i}", 3,
        f"Consider organic compound {i} analysed by 13C NMR and GC-MS.",
        [
            {'label': 'a', 'text': 'Deduce the number of peaks in its 13C NMR spectrum based on symmetry.', 'marks': 2},
            {'label': 'b', 'text': 'State how GC-MS separates and identifies components in a mixture.', 'marks': 1}
        ],
        f"{i}. (a) Count non-equivalent carbon environments considering molecular symmetry (2).<br/>{i}. (b) GC separates components by retention time; MS identifies each component by its molecular ion and fragmentation pattern (1)."
    ))

for i in range(26, 51):
    p11_questions.append(make_edexcel_q(
        i, f"A* Challenge: Multi-Spectral Structural Elucidation {i}", f"WCH14/01/Hard/Q{i}", 6,
        f"Compound Y (C4H8O2) has the following spectroscopic data:<br/>- IR: Strong C=O absorption at 1740 cm-1 (ester).<br/>- 13C NMR: 4 distinct peaks at delta = 14, 21, 60, 171 ppm.<br/>- 1H NMR: Singlet at 2.0 ppm (3H), Quartet at 4.1 ppm (2H), Triplet at 1.2 ppm (3H).",
        [
            {'label': 'a', 'text': 'Analyze each piece of spectroscopic data to deduce the complete structural formula of compound Y.', 'marks': 5},
            {'label': 'b', 'text': 'Give the systematic IUPAC name for compound Y.', 'marks': 1}
        ],
        f"{i}. (a) IR 1740 cm-1 confirms ester C=O (1). 13C NMR 4 peaks confirms 4 distinct carbon environments (1). 1H NMR singlet at 2.0 ppm (3H) = CH3CO- group (1). Quartet at 4.1 ppm (2H) and triplet at 1.2 ppm (3H) = -OCH2CH3 ethyl group (1). Combined structure = CH3COOCH2CH3 (1).<br/>{i}. (b) Ethyl ethanoate (1)."
    ))

p11_faqs = []
p11_faq_titles = [
    ("n+1 Splitting Rule Application", "1H NMR Splitting", "Counting protons on the same carbon atom when determining splitting.", "The n+1 rule states that a proton peak is split into n+1 sub-peaks, where n is the number of protons on ADJACENT carbon atoms (3 bonds away). Protons on the same carbon do not split each other."),
    ("D2O Exchange Mechanism", "D2O Shake", "Expecting C-H protons to exchange with D2O.", "D2O shake ONLY removes peaks for labile -OH and -NH protons because they exchange rapidly with deuterium (-OH + D2O -> -OD + HOD). Protons attached directly to carbon (C-H) do NOT exchange."),
    ("TMS Reference Peak", "NMR Standard", "Forgetting the chemical shift value of TMS.", "Tetramethylsilane Si(CH3)4 (TMS) is assigned a chemical shift of EXACTLY 0.0 ppm. Its 12 identical H atoms give a sharp reference peak at the far right of the spectrum."),
    ("13C NMR Integration Traces", "13C NMR vs 1H NMR", "Assuming peak heights in 13C NMR represent the number of carbons.", "13C NMR peak heights/areas are NOT strictly proportional to the number of carbon atoms (unlike 1H NMR integration). ONLY the number of peaks (carbon environments) and chemical shift values are evaluated."),
    ("Mass Spec Molecular Ion Peak Identification", "Mass Spectrometry", "Confusing the molecular ion M+ peak with fragment peaks.", "The molecular ion M+ peak is the peak with the HIGHEST m/z value (excluding small M+1 isotope peaks). Its m/z value gives the relative molecular mass (Mr) of the compound."),
    ("Mass Spec Fragment Ion Positive Charge Requirement", "Mass Spec Formulas", "Writing fragment species without a positive charge.", "Mass spectrometers ONLY detect POSITIVELY CHARGED ions. Fragment formulas MUST include a positive charge (e.g. [CH3CO]+, [C2H5]+, [COOH]+)."),
    ("Infrared O-H Absorption Differences", "IR Spectroscopy", "Confusing alcohol O-H with carboxylic acid O-H absorption.", "Alcohol O-H absorbs as a smooth broad peak at 3200-3600 cm-1. Carboxylic acid O-H absorbs as a VERY BROAD, distorted peak at 2500-3300 cm-1 overlapping the C-H region."),
    ("Deuterated Solvents in 1H NMR", "NMR Solvents", "Using H2O or CHCl3 as an NMR solvent.", "Solvents like H2O or CHCl3 contain 1H protons that would produce huge peaks masking the sample. Deuterated solvents like CDCl3 or D2O are used because deuterium (2H) does not absorb in the 1H frequency range."),
    ("Singlets for -OH and -NH Protons", "1H NMR Features", "Expecting -OH protons to show splitting from adjacent C-H protons.", "Protons on -OH and -NH groups undergo rapid exchange with trace water/solvents, averaging out spin-spin coupling. Consequently, -OH and -NH protons almost always appear as SINGLETS."),
    ("GC-MS Hyphenated Technique Function", "Chromatography-MS", "Claiming GC identifies compounds without MS.", "Gas Chromatography (GC) SEPARATES the components of a complex mixture based on retention time. Mass Spectrometry (MS) IDENTIFIES each separated component by its mass spectrum fingerprint.")
]

for idx, (ftitle, fcat, ftrap, fmodel) in enumerate(p11_faq_titles, 1):
    p11_faqs.append(make_edexcel_faq(ftitle, fcat, ftrap, fmodel))

build_pdf_pack("Usman_Edexcel_Chem_U4_15E_Spectroscopy_Chromatography.pdf", p11_meta, p11_questions, p11_faqs)
print("Pack 11 (15E Spectroscopy & NMR - 50 Qs + 10 FAQs) compiled successfully!")
