import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

t15_batch1 = [
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15A.1',
            'subtopic_name': 'Chirality and Enantiomers'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15A1_Chirality_Enantiomers.pdf',
        'questions': [
            {
                'title': '1. (a) Explain what is meant by a chiral centre in an organic molecule.',
                'marks': 1,
                'ref': 'WCH14/01/Jan23/Q4(a)',
                'mark_scheme': 'A carbon atom attached to four different groups/atoms.'
            },
            {
                'title': '(b) Lactic acid, CH3CH(OH)COOH, displays optical isomerism. Draw 3D wedge-and-dash diagrams of the two enantiomers of lactic acid.',
                'marks': 2,
                'ref': 'WCH14/01/Jan23/Q4(b)',
                'mark_scheme': '1. Correct 3D tetrahedral arrangement around central carbon.\n2. Non-superimposable mirror images clearly shown.'
            },
            {
                'title': '(c) Explain why 2-chlorobutane is chiral whereas 1-chlorobutane is achiral.',
                'marks': 2,
                'ref': 'WCH14/01/Oct22/Q3(c)',
                'mark_scheme': '1. 2-chlorobutane has C2 bonded to -H, -Cl, -CH3, -CH2CH3 (4 different groups).\n2. 1-chlorobutane C1 has two -H atoms attached (not 4 different groups).'
            },
            {
                'title': '2. MCQ: Which of the following molecules exists as a pair of optical isomers?',
                'options': ['A. Propan-2-ol', 'B. Butan-2-ol', 'C. Pentan-3-ol', 'D. 2-methylpropan-2-ol'],
                'marks': 1,
                'ref': 'WCH14/01/Jun22/Q1',
                'mark_scheme': 'B (Butan-2-ol has C2 attached to H, OH, CH3, C2H5).'
            }
        ],
        'faqs': [
            {
                'title': 'How do I identify a chiral carbon in a skeletal formula?',
                'category': 'Structural Recognition',
                'examiner_trap': 'Forgetting implicit hydrogen atoms attached to carbons in skeletal structures.',
                'model_answer': 'Count all four bonds from the carbon node. Include any implicit H atom. If all 4 attached groups are distinct, it is a chiral centre.'
            },
            {
                'title': 'Are enantiomers chemically identical?',
                'category': 'Physical & Chemical Properties',
                'examiner_trap': 'Stating enantiomers have different boiling points or chemical reactions with achiral reagents.',
                'model_answer': 'Enantiomers have identical physical properties (b.p., m.p., solubility) and chemical reactions with achiral reagents. They ONLY differ in their rotation of plane-polarised light and reactions with chiral reagents/enzymes.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15A.2',
            'subtopic_name': 'Optical Activity'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15A2_Optical_Activity.pdf',
        'questions': [
            {
                'title': '1. (a) Describe how a polarimeter is used to distinguish between two optical isomers.',
                'marks': 3,
                'ref': 'WCH14/01/Jun23/Q5(a)',
                'mark_scheme': '1. Plane-polarised light is passed through a solution of each enantiomer.\n2. One enantiomer rotates the plane of polarisation clockwise (dextrorotatory).\n3. The other enantiomer rotates the plane by an equal angle anticlockwise (laevorotatory).'
            },
            {
                'title': '(b) Explain why a racemic mixture (racemate) exhibits no optical activity.',
                'marks': 2,
                'ref': 'WCH14/01/Jun23/Q5(b)',
                'mark_scheme': '1. A racemic mixture contains equal amounts (50:50) of both enantiomers.\n2. The clockwise rotation by one enantiomer is exactly cancelled by the equal anticlockwise rotation of the other.'
            },
            {
                'title': '2. MCQ: A solution containing 0.10 mol dm-3 of an enantiomer rotates plane-polarised light by +12°. What rotation is observed for a 50:50 mixture of both enantiomers?',
                'options': ['A. +12°', 'B. -12°', 'C. +6°', 'D. 0°'],
                'marks': 1,
                'ref': 'WCH14/01/Jan22/Q2',
                'mark_scheme': 'D (0° due to cancellation in racemic mixture).'
            }
        ],
        'faqs': [
            {
                'title': 'Why does a racemate show 0° optical rotation?',
                'category': 'Polarimetry',
                'examiner_trap': 'Stating that the molecules in a racemate do not rotate light at all.',
                'model_answer': 'Each individual enantiomer molecule rotates light, but because equal numbers of (+) and (-) enantiomers are present, the opposite rotations cancel out macroscopically.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15A.3',
            'subtopic_name': 'Optical Activity and Reaction Mechanisms'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15A3_Optical_Activity_Reaction_Mechanisms.pdf',
        'questions': [
            {
                'title': '1. (a) Nucleophilic substitution of (R)-2-bromobutane with aqueous KOH produces a racemic mixture of butan-2-ol. Deduce whether this reaction proceeds via SN1 or SN2 mechanism and explain your reasoning.',
                'marks': 4,
                'ref': 'WCH14/01/Oct22/Q6(a)',
                'mark_scheme': '1. SN1 mechanism.\n2. SN1 involves formation of a planar carbocation intermediate.\n3. The hydroxide nucleophile can attack the planar carbocation with equal probability from above or below the plane.\n4. This forms equal amounts of both enantiomers (50:50 racemic mixture).'
            },
            {
                'title': '(b) Contrast the optical activity of the product formed when (R)-2-bromobutane undergoes SN2 nucleophilic substitution.',
                'marks': 2,
                'ref': 'WCH14/01/Oct22/Q6(b)',
                'mark_scheme': '1. SN2 involves backside attack in a single concerted step.\n2. Causes inversion of configuration (Walden inversion), yielding a single optically active enantiomer.'
            }
        ],
        'faqs': [
            {
                'title': 'How does optical activity prove the mechanism of nucleophilic substitution?',
                'category': 'Mechanisms & Evidence',
                'examiner_trap': 'Confusing SN1 (planar carbocation -> racemic / inactive) with SN2 (inversion -> optically active).',
                'model_answer': 'SN1 produces a trigonal planar carbocation intermediate allowing attack from top/bottom equally -> racemic mixture (optically inactive). SN2 proceeds via single-step backside attack -> inversion of configuration -> single optically active product.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15B.1',
            'subtopic_name': 'Carbonyl Compounds and Their Physical Properties'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15B1_Carbonyl_Compounds_Physical_Properties.pdf',
        'questions': [
            {
                'title': '1. (a) Compare the boiling points of propanal (59°C), propan-1-ol (97°C), and butane (0°C). Explain these differences in terms of intermolecular forces.',
                'marks': 4,
                'ref': 'WCH14/01/Jan23/Q7(a)',
                'mark_scheme': '1. Butane has London dispersion forces only (weakest).\n2. Propanal has polar C=O bond causing permanent dipole-dipole interactions (stronger than London forces).\n3. Propan-1-ol has -OH group forming hydrogen bonds (strongest intermolecular force).\n4. Higher energy required to break hydrogen bonds in propan-1-ol -> highest boiling point.'
            },
            {
                'title': '(b) Explain why lower aldehydes and ketones are soluble in water, but their solubility decreases as chain length increases.',
                'marks': 3,
                'ref': 'WCH14/01/Jan23/Q7(b)',
                'mark_scheme': '1. Lone pair on carbonyl oxygen forms hydrogen bonds with delta+ H of water molecules.\n2. As hydrocarbon chain length increases, non-polar hydrophobic alkyl group dominates.\n3. Disrupts hydrogen bonding network in water -> solubility decreases.'
            }
        ],
        'faqs': [
            {
                'title': 'Can aldehydes form hydrogen bonds with themselves?',
                'category': 'Intermolecular Forces',
                'examiner_trap': 'Claiming aldehydes have hydrogen bonding between aldehyde molecules.',
                'model_answer': 'No! Aldehydes do NOT have a H atom directly bonded to O, so they cannot form H-bonds with other aldehyde molecules (only dipole-dipole). However, they CAN form H-bonds with water because water has O-H.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15B.2',
            'subtopic_name': 'Redox Reactions of Carbonyl Compounds'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15B2_Redox_Reactions_Carbonyls.pdf',
        'questions': [
            {
                'title': '1. (a) Describe tests to distinguish between propanal and propanone using Tollens reagent and Fehling solution.',
                'marks': 4,
                'ref': 'WCH14/01/Jun21/Q6(a)',
                'mark_scheme': '1. Tollens reagent [Ag(NH3)2]+: propanal produces a silver mirror / grey ppt; propanone shows no reaction / stays colourless.\n2. Fehling solution Cu2+: propanal produces a brick-red ppt of Cu2O; propanone stays blue.'
            },
            {
                'title': '(b) State the reducing agent and conditions used to reduce propanone to propan-2-ol.',
                'marks': 2,
                'ref': 'WCH14/01/Jun21/Q6(b)',
                'mark_scheme': '1. Sodium tetrahydridoborate(III), NaBH4 (or LiAlH4 in dry ether).\n2. Aqueous ethanol / water solvent.'
            }
        ],
        'faqs': [
            {
                'title': 'Why don\'t ketones react with Tollens or Fehling reagents?',
                'category': 'Oxidation Reactions',
                'examiner_trap': 'Forgetting that oxidation of ketones requires breaking C-C bonds.',
                'model_answer': 'Aldehydes have a C-H bond on the carbonyl carbon that is easily oxidized to C-OH (carboxylic acid). Ketones lack this H atom, so oxidation would require breaking strong C-C bonds.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15B.3',
            'subtopic_name': 'Nucleophilic Addition Reactions'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15B3_Nucleophilic_Addition.pdf',
        'questions': [
            {
                'title': '1. (a) Draw the mechanism for the reaction of ethanal with HCN in the presence of KCN catalyst to form 2-hydroxypropanenitrile.',
                'marks': 4,
                'ref': 'WCH14/01/Jan22/Q7(a)',
                'mark_scheme': '1. Nucleophilic attack by CN- lone pair on delta+ carbonyl carbon.\n2. Curly arrow from C=O bond onto oxygen atom.\n3. Formation of tetrahedral intermediate [CH3CH(O-)CN].\n4. Protonation of O- by H+ / HCN to form -OH group.'
            },
            {
                'title': '(b) Describe the observation and result when propanone reacts with 2,4-dinitrophenylhydrazine (2,4-DNPH).',
                'marks': 2,
                'ref': 'WCH14/01/Jan22/Q7(b)',
                'mark_scheme': '1. Orange / yellow precipitate forms.\n2. Confirms presence of carbonyl group (C=O aldehyde or ketone).'
            },
            {
                'title': '(c) Describe the iodoform (tri-iodomethane) test for methyl ketones.',
                'marks': 3,
                'ref': 'WCH14/01/Jan22/Q7(c)',
                'mark_scheme': '1. Reagent: I2 and NaOH (aq).\n2. Observation: Yellow precipitate of CHI3 with antiseptic smell.\n3. Confirms presence of CH3C=O or CH3CH(OH) group.'
            }
        ],
        'faqs': [
            {
                'title': 'Why is KCN added in addition to HCN in nucleophilic addition?',
                'category': 'Reaction Conditions',
                'examiner_trap': 'Thinking HCN alone is reactive enough.',
                'model_answer': 'HCN is a weak acid and dissociates poorly. KCN provides a high concentration of CN- nucleophiles to initiate the reaction.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15C.1',
            'subtopic_name': 'Carboxylic Acids and Their Physical Properties'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15C1_Carboxylic_Acids_Physical_Properties.pdf',
        'questions': [
            {
                'title': '1. (a) Ethanoic acid forms dimers in the gas phase and non-polar solvents. Draw a diagram showing the structure of an ethanoic acid dimer, including hydrogen bonds.',
                'marks': 2,
                'ref': 'WCH14/01/Oct21/Q4(a)',
                'mark_scheme': '1. Two ethanoic acid molecules oriented anti-parallel.\n2. Two hydrogen bonds shown between C=O of one molecule and O-H of the other (dotted lines O...H).'
            },
            {
                'title': '(b) Explain why ethanoic acid has a higher boiling point (118°C) than propan-1-ol (97°C) despite having similar molar mass.',
                'marks': 3,
                'ref': 'WCH14/01/Oct21/Q4(b)',
                'mark_scheme': '1. Both form hydrogen bonds.\n2. Ethanoic acid forms dimers via 2 hydrogen bonds per dimer unit.\n3. Effectively doubles the molecular mass and strength of intermolecular attraction -> higher boiling point.'
            }
        ],
        'faqs': [
            {
                'title': 'What is a carboxylic acid dimer?',
                'category': 'Intermolecular Bonding',
                'examiner_trap': 'Drawing only 1 hydrogen bond between two carboxylic acid molecules.',
                'model_answer': 'A dimer consists of TWO carboxylic acid molecules joined by TWO hydrogen bonds between C=O...H-O of adjacent molecules, forming a 6-membered ring structure.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'ORGANIC CHEMISTRY, CARBONYLS AND CHIRALITY',
            'subtopic_code': '15C.2',
            'subtopic_name': 'Preparations and Reactions of Carboxylic Acids'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15C2_Preparations_Reactions_Carboxylic_Acids.pdf',
        'questions': [
            {
                'title': '1. (a) Write equations for the synthesis of propanoic acid starting from (i) propan-1-ol and (ii) propanenitrile.',
                'marks': 4,
                'ref': 'WCH14/01/Jun22/Q8(a)',
                'mark_scheme': '1. (i) CH3CH2CH2OH + 2[O] -> CH3CH2COOH + H2O (Reagents: K2Cr2O7 / H2SO4, reflux).\n2. (ii) CH3CH2CN + HCl + 2H2O -> CH3CH2COOH + NH4Cl (Reagents: dilute HCl, reflux).'
            },
            {
                'title': '(b) Describe the test to distinguish a carboxylic acid from an alcohol using sodium hydrogencarbonate, NaHCO3.',
                'marks': 2,
                'ref': 'WCH14/01/Jun22/Q8(b)',
                'mark_scheme': '1. Add NaHCO3 (aq).\n2. Carboxylic acid produces effervescence / CO2 gas (turns limewater cloudy); alcohol shows no reaction.'
            },
            {
                'title': '(c) Write the reaction equation for ethanoic acid with PCl5 and state the observation.',
                'marks': 2,
                'ref': 'WCH14/01/Jun22/Q8(c)',
                'mark_scheme': '1. CH3COOH + PCl5 -> CH3COCl + POCl3 + HCl.\n2. Steamy / misty white fumes of HCl gas observed.'
            }
        ],
        'faqs': [
            {
                'title': 'Why does NaHCO3 react with carboxylic acids but not phenols or alcohols?',
                'category': 'Acidity Comparison',
                'examiner_trap': 'Thinking phenols are strong enough acids to liberate CO2 from carbonates.',
                'model_answer': 'Carboxylic acids are stronger acids (Ka ~ 10^-5) than carbonic acid, so they displace CO2 from NaHCO3. Phenols (Ka ~ 10^-10) and alcohols are weaker acids than carbonic acid, so no reaction occurs.'
            }
        ]
    }
]

if __name__ == "__main__":
    count = 0
    for pack in t15_batch1:
        build_pdf_pack(pack['filename'], pack['meta'], pack['questions'], pack['faqs'])
        count += 1
        print(f"Built Topic 15 Batch 1 [{count}/{len(t15_batch1)}]: {pack['filename']}")
