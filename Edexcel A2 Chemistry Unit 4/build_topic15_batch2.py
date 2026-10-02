import os
import sys
from build_edexcel_u4_pdf import build_pdf_pack

t15_batch2 = [
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15D.1',
            'subtopic_name': 'Carboxylic Acid Derivatives: Acyl Chlorides'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15D1_Acyl_Chlorides.pdf',
        'questions': [
            {
                'title': '1. (a) Ethanoyl chloride reacts vigorously with water. Write the equation for this reaction and state the observation.',
                'marks': 2,
                'ref': 'WCH14/01/Jan23/Q8(a)',
                'mark_scheme': '1. CH3COCl + H2O -> CH3COOH + HCl.\n2. Misty / steamy white fumes of HCl gas observed.'
            },
            {
                'title': '(b) Compare the reactivity of ethanoyl chloride and chlorobenzene towards nucleophilic attack by water. Explain the difference.',
                'marks': 3,
                'ref': 'WCH14/01/Jan23/Q8(b)',
                'mark_scheme': '1. Ethanoyl chloride is extremely reactive due to delta+ carbonyl carbon attached to two electronegative atoms (O and Cl).\n2. Chlorobenzene is unreactive because p-orbital lone pair on Cl overlaps with pi-system of benzene ring.\n3. Strengthens C-Cl bond and increases electron density of ring -> repels nucleophiles.'
            },
            {
                'title': '(c) Write equations for ethanoyl chloride reacting with (i) ethanol and (ii) concentrated ammonia.',
                'marks': 3,
                'ref': 'WCH14/01/Jan23/Q8(c)',
                'mark_scheme': '1. (i) CH3COCl + C2H5OH -> CH3COOC2H5 + HCl (ethyl ethanoate + HCl).\n2. (ii) CH3COCl + 2NH3 -> CH3CONH2 + NH4Cl (ethanamide + ammonium chloride).'
            }
        ],
        'faqs': [
            {
                'title': 'Why does ethanoyl chloride react with 2 moles of ammonia?',
                'category': 'Stoichiometry & Mechanisms',
                'examiner_trap': 'Writing CH3COCl + NH3 -> CH3CONH2 + HCl without accounting for HCl reacting with excess NH3.',
                'model_answer': 'The reaction produces HCl gas which immediately reacts with a second mole of basic ammonia to form solid ammonium chloride (NH4Cl). Thus 2 moles of NH3 are required per mole of acyl chloride.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15D.2',
            'subtopic_name': 'Carboxylic Acid Derivatives: Esters'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15D2_Esters.pdf',
        'questions': [
            {
                'title': '1. (a) Write the equation for the acid-catalysed hydrolysis of ethyl ethanoate with dilute H2SO4.',
                'marks': 2,
                'ref': 'WCH14/01/Oct22/Q7(a)',
                'mark_scheme': '1. CH3COOCH2CH3 + H2O ⇌ CH3COOH + CH3CH2OH.\n2. Reversible equilibrium reaction.'
            },
            {
                'title': '(b) Contrast the acid-catalysed hydrolysis with alkaline hydrolysis (saponification) using aqueous NaOH.',
                'marks': 3,
                'ref': 'WCH14/01/Oct22/Q7(b)',
                'mark_scheme': '1. CH3COOCH2CH3 + NaOH -> CH3COONa + CH3CH2OH.\n2. Alkaline hydrolysis goes to completion (irreversible) yielding sodium carboxylate salt.\n3. Gives higher yield of alcohol product than acid hydrolysis.'
            }
        ],
        'faqs': [
            {
                'title': 'Why is alkaline hydrolysis of esters preferred over acid hydrolysis for preparation?',
                'category': 'Reaction Yields',
                'examiner_trap': 'Stating acid hydrolysis gives a higher yield.',
                'model_answer': 'Acid hydrolysis is reversible and reaches an equilibrium position (lower yield). Alkaline hydrolysis is irreversible because the carboxylate ion (CH3COO-) is unreactive towards nucleophilic attack by the alcohol, driving the reaction 100% to completion.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15D.3',
            'subtopic_name': 'Carboxylic Acid Derivatives: Polyesters'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15D3_Polyesters.pdf',
        'questions': [
            {
                'title': '1. (a) Terylene (PET) is a condensation polymer formed from benzene-1,4-dicarboxylic acid and ethane-1,2-diol. Draw the structural formula of the repeat unit of Terylene.',
                'marks': 2,
                'ref': 'WCH14/01/Jun21/Q7(a)',
                'mark_scheme': '1. Correct ester linkage -O-CO-C6H4-CO-O-CH2-CH2-.\n2. Open continuation bonds at both ends of the repeat unit.'
            },
            {
                'title': '(b) Explain why polyesters are biodegradable whereas addition polymers like poly(ethene) are not.',
                'marks': 3,
                'ref': 'WCH14/01/Jun21/Q7(b)',
                'mark_scheme': '1. Polyesters contain polar ester links (-CO-O-) susceptible to hydrolysis by microorganisms/water.\n2. Poly(ethene) has strong non-polar C-C and C-H single bonds resistant to chemical and enzymatic attack.'
            }
        ],
        'faqs': [
            {
                'title': 'How do I identify the monomers from a polymer repeat unit?',
                'category': 'Polymer Analysis',
                'examiner_trap': 'Adding water in the wrong places when breaking ester links.',
                'model_answer': 'Break the C-O ester single bond in the repeat unit. Add -OH to the carbonyl C=O group to regenerate the carboxylic acid, and add -H to the oxygen atom to regenerate the alcohol.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.1',
            'subtopic_name': 'Simple Chromatography (Paper & TLC)'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E1_Simple_Chromatography.pdf',
        'questions': [
            {
                'title': '1. (a) Define Rf value in thin-layer chromatography (TLC) and state its mathematical formula.',
                'marks': 2,
                'ref': 'WCH14/01/Jan22/Q5(a)',
                'mark_scheme': '1. Rf = (distance travelled by spot) / (distance travelled by solvent front).\n2. Ratio of solute movement relative to solvent.'
            },
            {
                'title': '(b) Explain why different amino acids have different Rf values on a silica TLC plate developed in a polar solvent.',
                'marks': 3,
                'ref': 'WCH14/01/Jan22/Q5(b)',
                'mark_scheme': '1. Stationary phase (silica) is polar; mobile phase (solvent) is polar/non-polar.\n2. Amino acids adsorb onto stationary phase and dissolve in mobile phase.\n3. Amino acid with greater affinity/solubility in mobile phase moves faster -> larger Rf value.'
            }
        ],
        'faqs': [
            {
                'title': 'Why must the solvent level be below the baseline spot in TLC?',
                'category': 'Experimental Technique',
                'examiner_trap': 'Stating the solvent level doesn\'t matter.',
                'model_answer': 'If the solvent level is above the baseline, the sample spots will dissolve directly into the bulk solvent reservoir rather than moving up the plate with the mobile phase.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.2',
            'subtopic_name': 'Determining Structures Using Mass Spectra'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E2_Mass_Spectrometry.pdf',
        'questions': [
            {
                'title': '1. (a) The mass spectrum of an organic compound shows a molecular ion peak M+ at m/z = 58 and a major fragment peak at m/z = 43. Identify the compound and the species responsible for m/z = 43.',
                'marks': 3,
                'ref': 'WCH14/01/Oct21/Q8(a)',
                'mark_scheme': '1. M+ at m/z = 58 corresponds to propanal or propanone (C3H6O, Mr = 58).\n2. m/z = 43 corresponds to [CH3CO]+ fragment ion (loss of CH3 = 15).\n3. Positive charge must be shown on fragment ion.'
            },
            {
                'title': '(b) Explain how the M+1 peak arises in mass spectra.',
                'marks': 2,
                'ref': 'WCH14/01/Oct21/Q8(b)',
                'mark_scheme': '1. Caused by the naturally occurring carbon-13 (13C) isotope (1.1% abundance).\n2. Ratio of M+1 to M+ peak height can be used to determine the number of carbon atoms.'
            }
        ],
        'faqs': [
            {
                'title': 'Why must mass spectrum fragment ions carry a positive charge in equations?',
                'category': 'Mass Spectrometry',
                'examiner_trap': 'Omitting the + sign on fragment formulas e.g. writing CH3CO instead of [CH3CO]+.',
                'model_answer': 'Only POSITIVELY CHARGED ions are accelerated and deflected by the magnetic field onto the detector. Uncharged free radicals are not detected.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.3',
            'subtopic_name': 'Chromatography: HPLC and GC'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E3_HPLC_GC.pdf',
        'questions': [
            {
                'title': '1. (a) Define retention time (tR) in Gas Chromatography (GC) and High-Performance Liquid Chromatography (HPLC).',
                'marks': 2,
                'ref': 'WCH14/01/Jun23/Q9(a)',
                'mark_scheme': '1. Time taken from injection of sample to detection of maximum peak intensity for a component.\n2. Characteristic property under fixed operating conditions.'
            },
            {
                'title': '(b) State how the concentration of a component is determined from a GC chromatogram.',
                'marks': 2,
                'ref': 'WCH14/01/Jun23/Q9(b)',
                'mark_scheme': '1. Area under the peak (or peak height).\n2. Compare with a calibration curve constructed using standard solutions of known concentration.'
            }
        ],
        'faqs': [
            {
                'title': 'What factors affect retention time in Gas Chromatography?',
                'category': 'Chromatographic Parameters',
                'examiner_trap': 'Listing only one factor.',
                'model_answer': 'Retention time depends on (1) boiling point of compound (volatility), (2) solubility/affinity for stationary phase, (3) temperature of column, (4) flow rate of carrier gas.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.4',
            'subtopic_name': 'Chromatography and Mass Spectrometry (GC-MS, HPLC-MS)'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E4_GC_MS_HPLC_MS.pdf',
        'questions': [
            {
                'title': '1. (a) Explain why gas chromatography combined with mass spectrometry (GC-MS) is superior to GC alone for identifying unknown substances in forensic analysis.',
                'marks': 3,
                'ref': 'WCH14/01/Jan23/Q9(a)',
                'mark_scheme': '1. GC separates complex mixtures into individual pure components.\n2. MS provides molecular mass (M+ peak) and characteristic fragmentation pattern for unambiguous structural identification.\n3. GC alone only gives retention times, which may overlap for different compounds.'
            }
        ],
        'faqs': [
            {
                'title': 'Why is GC-MS widely used in drug testing and environmental monitoring?',
                'category': 'Analytical Applications',
                'examiner_trap': 'Giving general answers without mentioning separation vs identification.',
                'model_answer': 'GC provides high separation efficiency for trace mixtures, while MS provides definitive structural confirmation by matching fragmentation patterns against spectral databases.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.5',
            'subtopic_name': 'Principles of NMR Spectroscopy'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E5_NMR_Principles.pdf',
        'questions': [
            {
                'title': '1. (a) Explain why tetramethylsilane, Si(CH3)4 (TMS), is added as an internal standard in NMR spectroscopy.',
                'marks': 3,
                'ref': 'WCH14/01/Oct22/Q9(a)',
                'mark_scheme': '1. Gives a single sharp peak at delta = 0 ppm.\n2. Si is less electronegative than C, so 12 H atoms are highly shielded (far right of spectrum).\n3. Non-toxic, volatile, and inert (easily recovered from sample).'
            },
            {
                'title': '(b) State why CDCl3 or CCl4 is used as a solvent in 1H NMR rather than CHCl3 or water.',
                'marks': 2,
                'ref': 'WCH14/01/Oct22/Q9(b)',
                'mark_scheme': '1. Deuterated solvents (CDCl3) contain deuterium (2H) which does not absorb in the 1H NMR frequency range.\n2. Prevents solvent 1H peak from obscuring sample peaks.'
            }
        ],
        'faqs': [
            {
                'title': 'Why is TMS used as the standard at 0 ppm?',
                'category': 'NMR Standards',
                'examiner_trap': 'Stating TMS has 4 protons.',
                'model_answer': 'TMS has 12 IDENTICAL protons (or 4 identical carbons), giving a single intense signal. Silicon\'s low electronegativity shields the nuclei, placing the peak at delta = 0.0 ppm.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.6',
            'subtopic_name': '13C NMR Spectroscopy'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E6_13C_NMR.pdf',
        'questions': [
            {
                'title': '1. (a) Predict the number of peaks in the 13C NMR spectrum of (i) propan-1-ol and (ii) propan-2-ol.',
                'marks': 2,
                'ref': 'WCH14/01/Jun22/Q9(a)',
                'mark_scheme': '1. (i) Propan-1-ol: 3 peaks (3 non-equivalent C environments).\n2. (ii) Propan-2-ol: 2 peaks (symmetrical, two identical CH3 carbons).'
            },
            {
                'title': '(b) A compound with molecular formula C4H8O2 has 3 peaks in its 13C NMR spectrum at delta = 20 ppm, 60 ppm, and 170 ppm. Deduce its structure.',
                'marks': 3,
                'ref': 'WCH14/01/Jun22/Q9(b)',
                'mark_scheme': '1. Peak at 170 ppm = carbonyl carbon of ester/carboxylic acid (C=O).\n2. Peak at 60 ppm = carbon attached to oxygen (-O-CH2-).\n3. Structure = ethyl ethanoate, CH3COOCH2CH3.'
            }
        ],
        'faqs': [
            {
                'title': 'How do I determine the number of 13C NMR peaks?',
                'category': 'Symmetry & Environments',
                'examiner_trap': 'Counting total carbon atoms instead of carbon environments.',
                'model_answer': 'Look for molecular symmetry. Carbon atoms in identical chemical environments give a single peak. Asymmetric molecules give one peak per carbon atom.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.7',
            'subtopic_name': '1H NMR Spectroscopy'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E7_1H_NMR.pdf',
        'questions': [
            {
                'title': '1. (a) Explain how D2O (heavy water) is used in 1H NMR to identify -OH and -NH protons (D2O shake).',
                'marks': 3,
                'ref': 'WCH14/01/Jan23/Q10(a)',
                'mark_scheme': '1. Add D2O to sample tube and shake.\n2. Labile -OH / -NH protons undergo rapid deuterium exchange: -OH + D2O ⇌ -OD + HOD.\n3. Deuterium (2H) does not absorb in 1H NMR -> the -OH / -NH peak disappears from the spectrum.'
            },
            {
                'title': '(b) State what information is obtained from the integration trace (peak area ratio) in a 1H NMR spectrum.',
                'marks': 1,
                'ref': 'WCH14/01/Jan23/Q10(b)',
                'mark_scheme': 'Relative ratio of hydrogen atoms (protons) in each chemical environment.'
            }
        ],
        'faqs': [
            {
                'title': 'Why does the -OH peak disappear when D2O is added?',
                'category': 'D2O Exchange',
                'examiner_trap': 'Stating D2O reacts with the C=O group.',
                'model_answer': 'Protons on -OH and -NH groups are acidic/labile and exchange rapidly with D in D2O. Since D absorbs at a different frequency, the -OH peak vanishes.'
            }
        ]
    },
    {
        'meta': {
            'candidate': 'Usman',
            'topic_code': 'Topic 15',
            'topic_name': 'CARBOXYLIC ACID DERIVATIVES, SPECTROSCOPY AND CHROMATOGRAPHY',
            'subtopic_code': '15E.8',
            'subtopic_name': 'Splitting Patterns in 1H NMR Spectra'
        },
        'filename': 'Usman_Edexcel_Chem_U4_15E8_Splitting_Patterns_1H_NMR.pdf',
        'questions': [
            {
                'title': '1. (a) Apply the n+1 rule to explain the splitting pattern observed in the 1H NMR spectrum of ethyl ethanoate, CH3COOCH2CH3.',
                'marks': 4,
                'ref': 'WCH14/01/Jun23/Q10(a)',
                'mark_scheme': '1. CH3 of ethanoate (CH3CO-): singlet (0 adjacent H atoms, n=0 -> 1 peak).\n2. -CH2- of ethyl (-OCH2CH3): quartet (split by 3 adjacent H of CH3, n=3 -> 4 peaks, 1:3:3:1 ratio).\n3. -CH3 of ethyl (-OCH2CH3): triplet (split by 2 adjacent H of CH2, n=2 -> 3 peaks, 1:2:1 ratio).'
            },
            {
                'title': '(b) State why -OH and -NH protons usually appear as singlets regardless of adjacent protons.',
                'marks': 1,
                'ref': 'WCH14/01/Jun23/Q10(b)',
                'mark_scheme': 'Rapid proton exchange with trace water/solvents averages out spin-spin coupling.'
            }
        ],
        'faqs': [
            {
                'title': 'What is the n+1 rule in 1H NMR?',
                'category': 'Spin-Spin Coupling',
                'examiner_trap': 'Counting protons on the SAME carbon atom.',
                'model_answer': 'The number of peaks in a multiplet is n+1, where n is the number of hydrogen atoms on ADJACENT carbon atoms (none-equivalent protons 3 bonds away).'
            }
        ]
    }
]

if __name__ == "__main__":
    count = 0
    for pack in t15_batch2:
        build_pdf_pack(pack['filename'], pack['meta'], pack['questions'], pack['faqs'])
        count += 1
        print(f"Built Topic 15 Batch 2 [{count}/{len(t15_batch2)}]: {pack['filename']}")
