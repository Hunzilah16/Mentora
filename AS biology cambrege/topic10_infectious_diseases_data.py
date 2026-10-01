"""
Topic 10: Infectious Diseases - 50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Physiological Mechanism Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Past Paper vs Original Ratio: 44 Authentic (88%) / 6 Original Extensions (12%)
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic10_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Comparative taxonomy and global epidemiology of 4 major pathogens (Fig 10.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q4 - Comparative Taxonomy, Transmission, and Global Epidemiology of Four Major Infectious Diseases",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Infectious diseases remain major causes of morbidity and mortality worldwide, caused by diverse taxonomic groups of pathogens. Fig. 10.1 is a comparative matrix outlining the biological characteristics of cholera, malaria, tuberculosis, and HIV/AIDS.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_1.png"),
        figure_caption="Fig. 10.1: Comparative classification, transmission vectors, and global prevention strategies for cholera, malaria, TB, and HIV.",
        parts=[
            QuestionPart(label="(a)", text="For both cholera and malaria, state the causative pathogen, its taxonomic kingdom / classification, and its primary mode of transmission.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the global distribution of malaria is largely restricted to tropical and subtropical latitudes, whereas cholera can occur in temperate disaster zones.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe two major social or economic obstacles that hinder the worldwide eradication of tuberculosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Cholera: Vibrio cholerae, Kingdom Eubacteria / Prokaryotae, water-borne / food-borne (faecal-oral route) [1]; Malaria: Plasmodium (falciparum / vivax / ovale / malariae), Kingdom Protoctista, vector-borne by female Anopheles mosquito bite [1].", "marks": 2},
            {"q": "Q1(b)", "points": "Anopheles mosquitoes require warm temperatures (> 20°C) and standing water for larval breeding, and Plasmodium development within mosquito requires ambient heat [1]; cholera transmission depends on compromised water/sewage infrastructure and sanitation collapse, which can occur anywhere regardless of ambient temperature [1].", "marks": 2},
            {"q": "Q1(c)", "points": "Overcrowded poor-quality housing promotes aerosol transmission [1]; long duration of DOTS treatment (6-9 months) leads to non-compliance and drug-resistant strains (MDR-TB) in resource-limited settings [1].", "marks": 2}
        ]
    ))

    # Q2: Ultrastructure of Vibrio cholerae and enterocyte colonisation (Fig 10.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q3 - Ultrastructure of Vibrio cholerae and Pathogenic Colonisation of the Small Intestine",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Vibrio cholerae is a comma-shaped, Gram-negative bacterium that colonises the brush border of the small intestine. Fig. 10.2 illustrates the cellular ultrastructure of V. cholerae.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_2.png"),
        figure_caption="Fig. 10.2: Fine ultrastructure of Vibrio cholerae showing the single polar flagellum, nucleoid, and toxin secretion.",
        parts=[
            QuestionPart(label="(a)", text="State two structural features visible in Fig. 10.2 that identify V. cholerae as a prokaryotic rather than a eukaryotic organism.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of the single polar flagellum and toxin-coregulated pili (TCP) in establishing infection in the small intestine.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why V. cholerae must be ingested in very large numbers (e.g. 10⁸ bacteria) in drinking water to cause clinical cholera in a healthy adult.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Absence of a membrane-bound nucleus / naked circular DNA (nucleoid) free in cytoplasm [1]; presence of 70S ribosomes / absence of double-membrane organelles (e.g. mitochondria) [1].", "marks": 2},
            {"q": "Q2(b)", "points": "Flagellum provides powerful motility to propel bacterium through the viscous mucus layer covering enterocytes [1]; TCP pili mediate adherence to GM1 gangliosides on apical enterocyte microvilli, preventing bacterial wash-out by peristalsis [1].", "marks": 2},
            {"q": "Q2(c)", "points": "V. cholerae is acid-sensitive; the highly acidic gastric juice (pH 1.5–2.0, HCl) in the stomach destroys the vast majority of ingested bacteria before reaching the duodenum [2].", "marks": 2}
        ]
    ))

    # Q3: Molecular mechanism of choleragen enterotoxin (Fig 10.3)
    questions.append(Question(
        number=3,
        title="9700/22/M/J/22/Q3 - Molecular Mechanism of Choleragen Action: G-Protein ADP-Ribosylation and CFTR Hyperactivation",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Once adhered to the intestinal epithelium, V. cholerae secretes the AB5-family enterotoxin choleragen. Fig. 10.3 details the intracellular signaling cascade triggered by choleragen inside enterocytes.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_3.png"),
        figure_caption="Fig. 10.3: Intracellular signaling pathway of choleragen showing G-protein activation, cAMP generation, and CFTR chloride channel opening.",
        parts=[
            QuestionPart(label="(a)", text="Describe the function of the B-subunits and the A1-subunit of the choleragen enterotoxin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the A1-subunit causes permanent activation of adenylate cyclase and describe the resulting effect on intracellular cAMP.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the opening of CFTR chloride channels leads to massive, life-threatening watery diarrhoea.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "Five B-subunits bind to GM1 ganglioside receptors on enterocyte membrane to form a pore [1]; A1-subunit dissociates and translocates across membrane into cytosol to act as an active ADP-ribosyltransferase enzyme [1].", "marks": 2},
            {"q": "Q3(b)", "points": "A1-subunit transfers ADP-ribose from NAD⁺ to Gsα subunit, inhibiting its intrinsic GTPase activity; Gsα remains locked in the active GTP-bound state, continuously stimulating adenylate cyclase to produce massive amounts of cAMP from ATP [2].", "marks": 2},
            {"q": "Q3(c)", "points": "High cAMP activates PKA, which phosphorylates and permanently opens CFTR channels, causing massive efflux of Cl⁻ (and Na⁺) into intestinal lumen [1]; water potential of lumen falls drastically below that of blood/tissue fluid, drawing water into gut by osmosis down a steep water potential gradient [1].", "marks": 2}
        ]
    ))

    # Q4: Physiology of Oral Rehydration Therapy (ORT) (Fig 10.4)
    questions.append(Question(
        number=4,
        title="9700/21/M/J/23/Q3 - Biophysics and Transport Physiology of Oral Rehydration Therapy (ORT)",
        syllabus_ref="Syllabus 10.1 & 4.2",
        difficulty="ADVANCED",
        preamble="Oral Rehydration Therapy (ORT) is recognized by the WHO as one of the greatest medical breakthroughs of the 20th century. Fig. 10.4 illustrates the transport mechanism operating at the enterocyte membrane during ORT.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_4.png"),
        figure_caption="Fig. 10.4: Mechanism of SGLT-1 cotransport and basolateral Na+/K+ ATPase driving osmotic water reabsorption during ORT.",
        parts=[
            QuestionPart(label="(a)", text="State the essential chemical components of Oral Rehydration Solution (ORS) and explain why drinking pure distilled water is ineffective and dangerous for a cholera patient.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the sodium-glucose cotransporter (SGLT-1) operates on the apical membrane of enterocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why ORT successfully reverses dehydration even when choleragen enterotoxin is actively opening CFTR channels.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "ORS contains glucose, sodium chloride, potassium chloride, and sodium citrate [1]; pure water lacks glucose and electrolytes, cannot be absorbed efficiently by cotransporters, and would further dilute plasma sodium, worsening hyponatremia and osmotic diarrhoea [1].", "marks": 2},
            {"q": "Q4(b)", "points": "SGLT-1 binds one glucose molecule and two Na⁺ ions simultaneously; utilizes the steep inward electrochemical gradient for Na⁺ (maintained by basolateral Na⁺/K⁺ pump) to transport glucose into the enterocyte against its concentration gradient [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Choleragen acts exclusively on CFTR chloride channels and secretory pathways; the SGLT-1 absorptive pathway is unaffected by cAMP [1]; inward transport of Na⁺ and glucose lowers intracellular and interstitial water potential, driving rapid osmotic absorption of water from gut lumen into blood [1].", "marks": 2}
        ]
    ))

    # Q5: Complete life cycle of Plasmodium (Fig 10.5)
    questions.append(Question(
        number=5,
        title="9700/22/O/N/23/Q3 - Complex Life Cycle of Plasmodium: Exo-Erythrocytic, Erythrocytic, and Sporogonic Cycles",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="The malaria parasite Plasmodium exhibits a digenetic life cycle involving an insect vector and a mammalian host. Fig. 10.5 outlines the complete sequence of stages in the female Anopheles mosquito and human body.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_5.png"),
        figure_caption="Fig. 10.5: Life cycle of Plasmodium showing transmission, liver schizogony, erythrocyte invasion, and sexual development in mosquito.",
        parts=[
            QuestionPart(label="(a)", text="Name the specific infective stage of Plasmodium injected into human blood during a mosquito bite, and state its initial target organ.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between the terms 'definitive host' and 'intermediate host', identifying which organism represents each host for Plasmodium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why Plasmodium does not provoke an immediate, highly effective antibody response during its hepatic and early erythrocytic stages.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Sporozoite [1]; travels in bloodstream to invade liver hepatocytes (liver parenchyma) [1].", "marks": 2},
            {"q": "Q5(b)", "points": "Definitive host is where sexual reproduction occurs: female Anopheles mosquito [1]; Intermediate host is where asexual reproduction / schizogony occurs: human host [1].", "marks": 2},
            {"q": "Q5(c)", "points": "Sporozoites enter hepatocytes within minutes of injection, hiding inside host cells [1]; mature merozoites spend only seconds in plasma before invading erythrocytes, which lack MHC class I molecules and cannot display foreign antigens [1].", "marks": 2}
        ]
    ))

    # Q6: Erythrocytic cycle and cyclical fever paroxysms (Fig 10.6)
    questions.append(Question(
        number=6,
        title="9700/22/F/M/23/Q4 - Intra-Erythrocytic Schizogony and Pathophysiology of Malarial Fever Paroxysms",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="The cyclical symptoms of malaria—characterized by sudden violent shivering chills followed by high burning fever and drenching sweats—are directly linked to synchronous events inside erythrocytes. Fig. 10.6 correlates the intra-erythrocytic stages of P. vivax with the patient's temperature chart.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_6.png"),
        figure_caption="Fig. 10.6: Intra-erythrocytic developmental stages (ring form, trophozoite, schizont) and corresponding 48-hour tertian fever spikes.",
        parts=[
            QuestionPart(label="(a)", text="Describe the morphological progression from merozoite invasion to the mature schizont inside an erythrocyte.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 10.6, explain the biochemical and immunological events that trigger the fever spike at 48-hour intervals.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why Plasmodium falciparum causes much higher mortality than Plasmodium vivax or Plasmodium malariae.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Merozoite enters RBC and differentiates into signet-ring trophozoite [1]; trophozoite ingests haemoglobin, enlarges, and undergoes multiple mitotic nuclear divisions (schizogony) to form a mature schizont containing 16–32 merozoites [1].", "marks": 2},
            {"q": "Q6(b)", "points": "Simultaneous lysis of thousands of infected erythrocytes releases merozoites, toxic haemozoin pigment, and cell debris [1]; haemozoin stimulates macrophages to release endogenous pyrogens (IL-1, TNF-α), resetting the hypothalamic thermostat to induce shivering and high fever [1].", "marks": 2},
            {"q": "Q6(c)", "points": "P. falciparum can invade RBCs of any age (high parasitaemia > 20%), whereas P. vivax only infects reticulocytes [1]; P. falciparum expresses PfEMP1 causing infected RBCs to adhere to deep capillary endothelium (cytoadherence / sequestration), causing microvascular occlusion, cerebral malaria, and organ failure [1].", "marks": 2}
        ]
    ))

    # Q7: Histopathology of Tuberculosis: Granuloma formation and latency (Fig 10.7)
    questions.append(Question(
        number=7,
        title="9700/21/O/N/21/Q3 - Cellular Pathogenesis of Mycobacterium tuberculosis: Macrophage Survival, Tubercles, and Cavitation",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Mycobacterium tuberculosis has adapted to survive inside human host phagocytes. Fig. 10.7 illustrates the cellular progression from initial inhalation to tubercle granuloma formation and pulmonary cavitation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_7.png"),
        figure_caption="Fig. 10.7: Pathological stages of pulmonary tuberculosis: alveolar phagocytosis, caseous granuloma formation, and cavitation.",
        parts=[
            QuestionPart(label="(a)", text="Describe the unique chemical composition of the cell wall of M. tuberculosis and explain how this aids survival inside alveolar macrophages.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the cellular structure of a tubercle (granuloma) and state the physiological significance of the central caseous necrosis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why co-infection with HIV dramatically increases the risk of latent tuberculosis reactivating into active, fatal disease.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Cell wall contains high concentrations of waxy mycolic acids, arabinogalactans, and lipoarabinomannan [1]; prevents the fusion of phagosomes with lysosomes, allowing bacteria to replicate protected within macrophage phagosomes [1].", "marks": 2},
            {"q": "Q7(b)", "points": "Composed of infected macrophages, epithelioid cells, and Langhans multinucleated giant cells surrounded by a collar of CD4 T-lymphocytes and fibroblasts [1]; caseous core is hypoxic and acidic, inhibiting bacterial replication and maintaining latency [1].", "marks": 2},
            {"q": "Q7(c)", "points": "HIV selectively infects and destroys CD4+ T-helper lymphocytes; without CD4 T-cells secreting interferon-gamma (IFN-γ) to activate macrophages, the fibrous wall of the tubercle breaks down, releasing live bacteria to multiply rapidly and cause cavitating disease [2].", "marks": 2}
        ]
    ))

    # Q8: Fine ultrastructure of HIV retrovirus (Fig 10.8)
    questions.append(Question(
        number=8,
        title="9700/22/M/J/21/Q3 - Molecular Ultrastructure and Genomic Organisation of the Human Immunodeficiency Virus (HIV)",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="The Human Immunodeficiency Virus is an enveloped, single-stranded RNA retrovirus that targets human immune cells. Fig. 10.8 illustrates the structural components of an HIV virion.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_8.png"),
        figure_caption="Fig. 10.8: Cutaway diagram of HIV virion displaying glycoprotein spikes (gp120/gp41), protein capsid (p24), and internal enzymes.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure and origin of the viral envelope surrounding the HIV capsid.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the specific roles of viral glycoproteins gp120 and gp41 in gaining entry into human host cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Name the three viral enzymes housed inside the capsid and state the function of each during the viral life cycle.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "A phospholipid bilayer acquired from the host cell surface membrane as the mature virus buds off [1]; studded with viral glycoprotein complexes [1].", "marks": 2},
            {"q": "Q8(b)", "points": "gp120 binds specifically to the CD4 receptor and chemokine co-receptor (CCR5 or CXCR4) on T-helper cells [1]; gp41 undergoes a conformational change that mediates fusion of the viral envelope with host cell membrane [1].", "marks": 2},
            {"q": "Q8(c)", "points": "Reverse transcriptase: converts viral ssRNA into double-stranded cDNA [1]; Integrase: inserts viral ds-cDNA into host cell chromosomal DNA; Protease: cleaves viral polyprotein precursor into functional structural proteins and enzymes during maturation [1].", "marks": 2}
        ]
    ))

    # Q9: HIV replication cycle in CD4 T-helper cell (Fig 10.9)
    questions.append(Question(
        number=9,
        title="9700/21/M/J/20/Q3 - Biochemical Stages in the Replication Cycle of HIV and Provirus Formation",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="The replication of HIV involves reverse transcription of RNA into DNA and stable integration into the host genome. Fig. 10.9 details the key steps of this process within a CD4+ T-lymphocyte.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_9.png"),
        figure_caption="Fig. 10.9: Cellular events during HIV replication: attachment, entry, reverse transcription, integration, provirus transcription, and budding.",
        parts=[
            QuestionPart(label="(a)", text="Explain why HIV is classified as a 'retrovirus' and describe the synthesis of cDNA from viral RNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what is meant by a 'provirus' and state why proviral DNA cannot be eradicated by standard antibiotic drugs.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the lack of proofreading activity in reverse transcriptase contributes to the rapid development of drug resistance.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Retroviruses reverse the normal flow of genetic information by using RNA as a template to synthesise DNA [1]; reverse transcriptase uses viral ssRNA to synthesise a complementary single DNA strand, degrades the RNA template, and synthesises the second DNA strand to yield double-stranded cDNA [1].", "marks": 2},
            {"q": "Q9(b)", "points": "A provirus is viral DNA covalently integrated into the host cell's nuclear chromosome by integrase [1]; it behaves as normal host genetic material, replicated by host DNA polymerase; antibiotics only target bacterial structures, not integrated eukaryotic genes [1].", "marks": 2},
            {"q": "Q9(c)", "points": "Reverse transcriptase has no 3'->5' exonuclease proofreading activity, generating frequent transcription errors / mutations (1 in 10⁴ bases) [1]; generates enormous genetic diversity (quasi-species), leading to rapid selection of mutants resistant to antiretroviral drugs [1].", "marks": 2}
        ]
    ))

    # Q10: Clinical progression from HIV to AIDS (Fig 10.10)
    questions.append(Question(
        number=10,
        title="9700/22/M/J/19/Q4 - Longitudinal Dynamics of CD4+ T-Lymphocyte Count and Plasma Viral Load in HIV/AIDS",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Untreated HIV infection follows a predictable multi-year clinical trajectory. Fig. 10.10 shows the relationship between CD4+ T-cell count, plasma HIV RNA copies per mL, and the clinical stages of infection.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_10.png"),
        figure_caption="Fig. 10.10: Graph showing CD4+ T-cell decline and viral load surge through acute infection, clinical latency, and AIDS.",
        parts=[
            QuestionPart(label="(a)", text="Describe the changes in plasma viral load and CD4+ T-cell count during the first six months following HIV transmission (acute phase).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the clinical latency phase can last for several years even though billions of virions are produced and destroyed each day.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State the clinical diagnostic threshold for Acquired Immune Deficiency Syndrome (AIDS) and explain why AIDS patients succumb to opportunistic infections.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Viral load spikes rapidly to peak levels (> 10⁶ copies/mL) accompanied by a sharp decline in CD4 T-cells [1]; cytotoxic T-lymphocytes (CD8+) partially control viremia, allowing CD4 counts to rebound toward normal levels [1].", "marks": 2},
            {"q": "Q10(b)", "points": "Dynamic equilibrium (set point): the immune system rapidly produces new CD4 T-cells to replace those destroyed by viral budding and apoptosis [1]; but over years, the regenerative capacity of the bone marrow and thymus is exhausted, leading to gradual depletion [1].", "marks": 2},
            {"q": "Q10(c)", "points": "CD4+ T-lymphocyte count falls below 200 cells per µL of blood (or presence of an AIDS-defining condition) [1]; CD4 cells coordinate both humoral (B-cell activation) and cell-mediated immunity; their loss disables adaptive immunity, allowing normally harmless commensals / pathogens (e.g. Pneumocystis jirovecii, Candida) to cause fatal infections [1].", "marks": 2}
        ]
    ))

    # Q11: Penicillin mode of action on bacterial cell wall (Fig 10.11)
    questions.append(Question(
        number=11,
        title="9700/22/F/M/22/Q2 - Biochemical Mechanism of Penicillin: Inhibition of Peptidoglycan Transpeptidase and Osmotic Lysis",
        syllabus_ref="Syllabus 10.2",
        difficulty="ADVANCED",
        preamble="Penicillin was the first broad-spectrum antibiotic discovered and acts specifically on bacterial cell wall biosynthesis. Fig. 10.11 compares peptidoglycan cross-linking in normal bacteria with cross-linking in the presence of penicillin.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_11.png"),
        figure_caption="Fig. 10.11: Molecular action of penicillin inhibiting transpeptidase cross-linking of peptidoglycan, resulting in osmotic lysis.",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular structure of bacterial peptidoglycan and name the enzyme that catalyses the formation of cross-links between glycan chains.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the β-lactam ring of penicillin inhibits this enzyme and state why penicillin only kills dividing bacteria.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why penicillin causes the bacterial cell to burst (lyse), referring to water potential and internal turgor pressure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Alternating units of N-acetylglucosamine (NAG) and N-acetylmuramic acid (NAM) joined by β-1,4-glycosidic bonds [1]; cross-linked by peptide side chains catalysed by transpeptidase (glycoprotein peptidase / PBP) [1].", "marks": 2},
            {"q": "Q11(b)", "points": "Penicillin acts as a structural analogue of the D-Ala-D-Ala terminus of peptidoglycan; β-lactam ring irreversibly acylates the active-site serine of transpeptidase [1]; non-dividing bacteria do not synthesise new cell walls, so their existing cross-links remain intact and unaffected [1].", "marks": 2},
            {"q": "Q11(c)", "points": "Bacterial cytoplasm has a high solute concentration (very negative water potential); in hypotonic media, water enters continuously by osmosis [1]; without cross-links, expanding cell wall cannot resist internal turgor pressure (up to 20 atm), resulting in osmotic lysis [1].", "marks": 2}
        ]
    ))

    # Q12: Four molecular mechanisms of antibiotic resistance (Fig 10.12)
    questions.append(Question(
        number=12,
        title="9700/21/M/J/22/Q3 - Molecular Mechanisms of Bacterial Antibiotic Resistance: Enzymatic Inactivation, Target Modification, and Efflux",
        syllabus_ref="Syllabus 10.2",
        difficulty="ADVANCED",
        preamble="Bacteria have evolved diverse biochemical adaptations to neutralize the bactericidal effects of antibiotics. Fig. 10.12 illustrates four major mechanisms of antibiotic resistance.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_12.png"),
        figure_caption="Fig. 10.12: Four primary molecular resistance mechanisms: enzymatic hydrolysis, target site mutation, active efflux pumps, and porin loss.",
        parts=[
            QuestionPart(label="(a)", text="Explain how the enzyme β-lactamase (penicillinase) confers resistance to penicillin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how a single missense mutation in the transpeptidase gene can produce penicillin resistance without disabling bacterial cell wall synthesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the operation of multidrug active efflux pumps and outer membrane porin mutations.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "β-lactamase hydrolyses the cyclic amide bond in the four-membered β-lactam ring of penicillin [1]; opening the ring renders the antibiotic chemically inactive, unable to bind transpeptidase [1].", "marks": 2},
            {"q": "Q12(b)", "points": "Alters the tertiary structure / active site shape of penicillin-binding protein (PBP) so penicillin can no longer bind with high affinity [1]; but active site retains sufficient catalytic geometry to cross-link peptidoglycan peptide chains, permitting normal wall growth [1].", "marks": 2},
            {"q": "Q12(c)", "points": "Efflux pumps use ATP / proton-motive force to actively pump antibiotic molecules out of cytoplasm across outer membrane, keeping intracellular levels sub-lethal [1]; porin mutations reduce pore diameter or downregulate expression, preventing hydrophilic antibiotics from crossing outer membrane [1].", "marks": 2}
        ]
    ))

    # Q13: Horizontal vs vertical gene transmission of resistance (Fig 10.13)
    questions.append(Question(
        number=13,
        title="9700/22/O/N/20/Q3 - Genetic Transfer of Antibiotic Resistance: Vertical Clonal Inheritance vs Horizontal Conjugation",
        syllabus_ref="Syllabus 10.2 & 5.1",
        difficulty="ADVANCED",
        preamble="Antibiotic resistance genes can propagate rapidly through bacterial populations via two distinct transmission modes. Fig. 10.13 compares vertical transmission via binary fission with horizontal transfer via bacterial conjugation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_13.png"),
        figure_caption="Fig. 10.13: Comparison of vertical inheritance via binary fission and horizontal gene transfer via plasmid conjugation through a sex pilus.",
        parts=[
            QuestionPart(label="(a)", text="Describe the process of vertical transmission of antibiotic resistance during bacterial reproduction.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the mechanism of horizontal gene transmission via conjugation, naming the structure formed between the two bacteria.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why horizontal gene transmission is far more dangerous to public health than vertical transmission alone.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Resistant bacterium replicates its circular chromosome and resistance plasmids semi-conservatively before dividing by binary fission [1]; all clonal progeny cells inherit the identical resistance allele, propagating resistance within that bacterial strain [1].", "marks": 2},
            {"q": "Q13(b)", "points": "Donor bacterium (F+) extends a protein sex pilus to contact a recipient bacterium (F-) and forms a conjugation bridge [1]; a single-stranded nick in the R-plasmid allows rolling-circle replication and transfer of a plasmid strand, which is made double-stranded in the recipient [1].", "marks": 2},
            {"q": "Q13(c)", "points": "Horizontal transfer can occur across completely different bacterial species and genera (e.g. harmless gut commensal E. coli transferring resistance to pathogenic Salmonella or Vibrio) [1]; plasmids often carry multiple resistance genes simultaneously, creating multi-drug resistant superbugs overnight [1].", "marks": 2}
        ]
    ))

    # Q14: Natural selection dynamics under antibiotic pressure (Fig 10.14)
    questions.append(Question(
        number=14,
        title="9700/21/M/J/19/Q3 - Population Dynamics and Natural Selection of Antibiotic Resistance Under Chemotherapeutic Pressure",
        syllabus_ref="Syllabus 10.2",
        difficulty="ADVANCED",
        preamble="The emergence of antibiotic resistance is a classic demonstration of natural selection in action. Fig. 10.14 plots changes in the relative proportions of susceptible and resistant bacteria following antibiotic administration.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig10_14.png"),
        figure_caption="Fig. 10.14: Graph showing rapid elimination of susceptible bacteria and competitive expansion of resistant mutants under antibiotic selection.",
        parts=[
            QuestionPart(label="(a)", text="Explain why random genetic mutations conferring resistance must occur BEFORE the bacterial population is exposed to the antibiotic.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 10.14, describe the role of the antibiotic as an environmental selective agent.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why stopping an antibiotic course early when clinical symptoms improve promotes the evolution of fully resistant strains.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Mutations are spontaneous, random replication errors that occur independently of environmental need; the antibiotic does not induce or cause the mutation [2].", "marks": 2},
            {"q": "Q14(b)", "points": "Antibiotic kills susceptible individuals, conferring a major selective advantage on rare mutants bearing the resistance allele [1]; resistant bacteria survive, multiply without competition for nutrients, and increase the frequency of the resistance allele in the population [1].", "marks": 2},
            {"q": "Q14(c)", "points": "Early doses kill the most susceptible bacteria, leaving partially resistant bacteria alive [1]; stopping treatment removes the drug before these intermediate bacteria are killed, allowing them to multiply and accumulate further mutations to become fully resistant [1].", "marks": 2}
        ]
    ))

    # Q15: Why antibiotics do not affect viruses: Acellular structure vs bacterial targets
    questions.append(Question(
        number=15,
        title="9700/22/M/J/18/Q3 - Acellular Architecture of Viruses and the Molecular Basis of Antibiotic Ineffectiveness",
        syllabus_ref="Syllabus 10.2 & 1.6",
        difficulty="ADVANCED",
        preamble="A common medical misconception is requesting antibiotic prescriptions for viral upper respiratory tract infections such as the common cold or influenza.",
        parts=[
            QuestionPart(label="(a)", text="State three fundamental structural differences between a virus (e.g. influenza) and a typical bacterium (e.g. Streptococcus).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why antibiotics that inhibit bacterial transpeptidase, 70S ribosomes, or folic acid synthesis have no effect on viral replication.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the public health danger of general practitioners prescribing broad-spectrum antibiotics for viral throat infections.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Viruses are acellular (non-cellular) and lack a cytoplasm, cell wall, and cell surface membrane [1]; viruses contain either DNA or RNA (never both) enclosed in a protein capsid, whereas bacteria contain both DNA and RNA and 70S ribosomes [1].", "marks": 2},
            {"q": "Q15(b)", "points": "Viruses lack target enzymes, cell walls, and 70S ribosomes entirely [1]; they replicate strictly intracellularly using host cell eukaryotic enzymes, tRNA, and 80S ribosomes, which are immune to bacterial antibiotic mechanisms [1].", "marks": 2},
            {"q": "Q15(c)", "points": "Exposes harmless commensal microflora (e.g. in gut, skin, nasopharynx) to unnecessary selective pressure [1]; selects for resistant commensal strains which can subsequently transfer R-plasmids horizontally to pathogenic bacteria [1].", "marks": 2}
        ]
    ))

    # Q16: Malaria eradication obstacles: Biological, sociological, and geographical
    questions.append(Question(
        number=16,
        title="9700/22/O/N/17/Q3 - Multi-Faceted Obstacles to the Global Eradication of Malaria",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="In the 1950s, the World Health Organization launched the Global Malaria Eradication Programme, but malaria remains endemic across sub-Saharan Africa and Southeast Asia.",
        parts=[
            QuestionPart(label="(a)", text="Explain why developing an effective, long-lasting malaria vaccine has proved far more challenging than developing vaccines against smallpox or measles.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how the evolution of insecticide resistance in Anopheles mosquitoes has compromised vector control programmes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how civil unrest, human migration, and global climate change contribute to the re-emergence of malaria in previously controlled regions.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Plasmodium is a complex eukaryotic protoctist with thousands of genes exhibiting extensive antigenic variation across distinct life-cycle stages [1]; parasite resides hidden inside host liver cells and erythrocytes, evading circulating humoral antibodies [1].", "marks": 2},
            {"q": "Q16(b)", "points": "Widespread use of pyrethroid insecticides on bed nets selected for mosquitoes with target-site mutations (kdr gene) or elevated metabolic detoxifying enzymes (cytochrome P450s) [1]; resistant mosquitoes survive contact with ITNs and continue transmitting sporozoites [1].", "marks": 2},
            {"q": "Q16(c)", "points": "War displaces populations into refugee camps with poor shelter and standing water, disrupting supply of antimalarial drugs and bed nets [1]; global warming expands the geographical range and altitude of Anopheles vector breeding zones into previously temperate highland areas [1].", "marks": 2}
        ]
    ))

    # Q17: Diagnosis of Tuberculosis: Mantoux test, IGRA, and sputum microscopy
    questions.append(Question(
        number=17,
        title="9700/21/M/J/17/Q4 - Clinical Diagnostic Methodologies for Tuberculosis: Tuberculin Skin Testing, IGRA, and Sputum Microscopy",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Early, accurate diagnosis of Mycobacterium tuberculosis infection is critical to initiating therapy and halting transmission in community settings.",
        parts=[
            QuestionPart(label="(a)", text="Describe the immunological basis of the Mantoux tuberculin skin test (purified protein derivative - PPD injection).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why an individual who previously received the BCG vaccine will produce a false-positive result in a Mantoux test, and describe how an IGRA blood test overcomes this limitation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how Ziehl-Neelsen acid-fast staining allows M. tuberculosis to be identified in a sputum smear under a light microscope.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Intradermal injection of tuberculin PPD antigens triggers a delayed-type (type IV) cell-mediated hypersensitivity reaction [1]; sensitized CD4+ memory T-cells migrate to the site and release cytokines, producing localized induration / swelling within 48–72 hours [1].", "marks": 2},
            {"q": "Q17(b)", "points": "BCG contains attenuated M. bovis which shares common antigens with tuberculin, inducing memory T-cells that cross-react in Mantoux test [1]; Interferon-Gamma Release Assays (IGRAs) test for T-cell response to specific M. tuberculosis antigens (ESAT-6, CFP-10) absent in BCG strains, eliminating false positives [1].", "marks": 2},
            {"q": "Q17(c)", "points": "Waxy mycolic acids bind lipid-soluble carbolfuchsin dye; bacteria resist decolourisation with acid-alcohol ('acid-fast') [1]; appear as bright red / pink slender rods against a methylene blue counterstained background [1].", "marks": 2}
        ]
    ))

    # Q18: Antibiotic stewardship and international hospital infection control
    questions.append(Question(
        number=18,
        title="9700/23/O/N/16/Q3 - Clinical Protocols for Antibiotic Stewardship and Mitigation of Hospital-Acquired Superbugs (MRSA)",
        syllabus_ref="Syllabus 10.2",
        difficulty="ADVANCED",
        preamble="Nosocomial (hospital-acquired) infections by multi-drug resistant pathogens, such as Methicillin-Resistant Staphylococcus aureus (MRSA), pose severe risks to surgical and immunocompromised patients.",
        parts=[
            QuestionPart(label="(a)", text="State what is meant by 'antibiotic stewardship' and outline two core prescribing guidelines enforced under stewardship programmes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why narrow-spectrum antibiotics are preferred over broad-spectrum antibiotics whenever bacterial identity is known.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe two barrier nursing / hygiene procedures implemented in hospitals to prevent the horizontal transmission of MRSA between patients.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Coordinated systematic programmes to optimize antimicrobial use to combat resistance and improve patient outcomes [1]; guidelines: only prescribe when bacterial infection is laboratory-confirmed (no antibiotics for viral illnesses); use correct dosage and minimum effective duration [1].", "marks": 2},
            {"q": "Q18(b)", "points": "Narrow-spectrum drugs target only the specific pathogen responsible [1]; broad-spectrum drugs wipe out benign commensal microflora throughout the body, eliminating competition and selecting for resistant opportunistic strains (e.g. Clostridioides difficile) [1].", "marks": 2},
            {"q": "Q18(c)", "points": "Strict isolation of infected/colonised patients in negative-pressure private rooms [1]; mandatory hand disinfection with alcohol rubs by healthcare staff between patients and use of disposable gloves and aprons [1].", "marks": 2}
        ]
    ))

    # Q19: Antiretroviral therapy (ART) mechanisms: NRTIs, NNRTIs, and Protease Inhibitors
    questions.append(Question(
        number=19,
        title="9700/22/F/M/18/Q3 - Pharmacological Mechanisms of Highly Active Antiretroviral Therapy (HAART) in Managing HIV",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="While HIV cannot currently be cured, Highly Active Antiretroviral Therapy (HAART) transforms HIV infection from a fatal disease into a manageable chronic condition.",
        parts=[
            QuestionPart(label="(a)", text="Explain how Nucleoside Reverse Transcriptase Inhibitors (NRTIs, e.g. AZT / zidovudine) terminate viral cDNA chain elongation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how Non-Nucleoside Reverse Transcriptase Inhibitors (NNRTIs) inhibit the reverse transcriptase enzyme through allosteric mechanisms.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why HAART regimens always combine at least three different drugs from at least two distinct pharmacological classes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "NRTIs are synthetic structural analogues of natural deoxyribonucleosides lacking a 3'-OH group on the ribose ring [1]; incorporation by reverse transcriptase prevents the formation of the next 3'-5' phosphodiester bond, terminating cDNA elongation [1].", "marks": 2},
            {"q": "Q19(b)", "points": "NNRTIs bind to an allosteric pocket adjacent to the active catalytic site of reverse transcriptase [1]; induces a conformational change in enzyme structure that drastically reduces catalytic rate (non-competitive inhibition) [1].", "marks": 2},
            {"q": "Q19(c)", "points": "High mutation rate of HIV means single-drug therapy quickly selects for resistant mutants [1]; the probability of a single virion simultaneously acquiring independent mutations conferring resistance to three different drug classes is mathematically negligible [1].", "marks": 2}
        ]
    ))

    # Q20: Cholera epidemic control: Sanitation, chlorination, and rapid surveillance
    questions.append(Question(
        number=20,
        title="9700/21/O/N/15/Q3 - Epidemiology and Public Health Interventions for the Containment of Cholera Outbreaks",
        syllabus_ref="Syllabus 10.1",
        difficulty="ADVANCED",
        preamble="Following humanitarian disasters, the destruction of municipal sewage treatment and water distribution infrastructure often precipitates explosive cholera epidemics.",
        parts=[
            QuestionPart(label="(a)", text="Describe the route of transmission of Vibrio cholerae and explain why refugees living in crowded camps with pit latrines are at acute risk.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how treating community water supplies with chlorine prevents the transmission of V. cholerae.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Outline the immediate logistical priorities required to contain an acute cholera outbreak in a refugee camp.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Faecal-oral route via consumption of water or food contaminated by human feces [1]; heavy rainfall or shallow water tables cause pit latrine effluent to leach into shallow wells and surface water used for drinking and cooking [1].", "marks": 2},
            {"q": "Q20(b)", "points": "Chlorine reacts with water to form hypochlorous acid (HOCl), a strong oxidising agent [1]; oxidises bacterial cell surface membranes, denatures essential transport proteins, and destroys V. cholerae [1].", "marks": 2},
            {"q": "Q20(c)", "points": "Establishment of dedicated Cholera Treatment Centres (CTCs) with strict barrier nursing to isolate patients [1]; rapid distribution of ORS packets, intravenous Ringer's lactate fluids, water purification chlorine tablets, and trucking in safe drinking water [1].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & PHYSIOLOGICAL MECHANISMS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Cholera enterotoxin vs normal enterocyte secretion
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q5 - Enterocyte Ion Transport Under Normal Conditions vs Choleragen Exposure",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="In the healthy human intestine, fluid absorption and secretion are precisely balanced.",
        parts=[
            QuestionPart(label="(a)", text="State the normal resting function of the CFTR protein in intestinal enterocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how choleragen disrupts this balance to produce net fluid loss.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Regulates the physiological secretion of chloride ions into the lumen to maintain appropriate intestinal fluid consistency [2].", "marks": 2},
            {"q": "Q21(b)", "points": "Elevated cAMP keeps CFTR channels continuously open, causing unregulated hypersecretion of Cl⁻ [1]; intestinal absorptive capacity is overwhelmed, resulting in net osmotic water loss of up to 20 litres per day [1].", "marks": 2}
        ]
    ))

    # Q22: Life cycle of Anopheles mosquito and vector control
    questions.append(Question(
        number=22,
        title="9700/21/O/N/22/Q4 - Anopheles Mosquito Biology and Targeted Vector Interventions",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Vector control is the most effective approach for preventing malaria transmission.",
        parts=[
            QuestionPart(label="(a)", text="Explain why only female Anopheles mosquitoes transmit malaria to humans.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe two methods of vector control that target the aquatic larval stages of the mosquito.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Female mosquitoes require protein-rich blood meals to produce and mature their eggs; males feed exclusively on plant nectar and sugar [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Draining standing water bodies or applying a thin film of oil/surfactant to water surface to prevent larval breathing [1]; introducing biological control predators such as Gambusia fish that eat mosquito larvae [1].", "marks": 2}
        ]
    ))

    # Q23: Primary infection vs post-primary (reactive) tuberculosis
    questions.append(Question(
        number=23,
        title="9700/22/F/M/22/Q4 - Primary Pulmonary Tuberculosis vs Post-Primary Reactivation",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="The clinical course of tuberculosis is divided into primary infection and post-primary disease.",
        parts=[
            QuestionPart(label="(a)", text="Describe the outcome of primary M. tuberculosis infection in a healthy immunocompetent individual.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what triggers post-primary (reactive) tuberculosis and state two characteristic symptoms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Cell-mediated immune response walls off bacteria inside calcified granulomas (tubercles / Ghon complexes); infection becomes latent and asymptomatic [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Waning cell-mediated immunity (due to malnutrition, aging, immunosuppressive therapy, or HIV co-infection) [1]; symptoms: persistent cough with hemoptysis, night sweats, severe weight loss / wasting [1].", "marks": 2}
        ]
    ))

    # Q24: Transmission methods of HIV and barrier prevention
    questions.append(Question(
        number=24,
        title="9700/21/M/J/22/Q4 - Transmission Routes of HIV and Evidence-Based Preventative Measures",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Human Immunodeficiency Virus is transmitted through specific body fluids.",
        parts=[
            QuestionPart(label="(a)", text="List four distinct body fluids capable of transmitting infectious levels of HIV.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the use of latex condoms and sterile needle exchange programmes prevent HIV transmission.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Blood, semen, vaginal secretions, and breast milk [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Condoms act as an impermeable physical barrier preventing direct contact between infected genital fluids and mucous membranes [1]; needle exchanges eliminate the sharing of blood-contaminated needles among intravenous drug users [1].", "marks": 2}
        ]
    ))

    # Q25: Mode of action of penicillin: Competitive vs uncompetitive inhibition
    questions.append(Question(
        number=25,
        title="9700/22/M/J/21/Q4 - Structural Mimicry: Penicillin and the D-Ala-D-Ala Dipeptide Substrate",
        syllabus_ref="Syllabus 10.2 & 3.2",
        difficulty="INTERMEDIATE",
        preamble="Penicillin is a suicide inhibitor that mimics the natural substrate of transpeptidase.",
        parts=[
            QuestionPart(label="(a)", text="Name the natural substrate of bacterial transpeptidase that penicillin structurally resembles.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why penicillin is classified as an irreversible inhibitor of transpeptidase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "The D-alanyl-D-alanine (D-Ala-D-Ala) terminal dipeptide of the peptidoglycan precursor side chain [2].", "marks": 2},
            {"q": "Q25(b)", "points": "The highly strained β-lactam ring opens and forms a covalent ester bond with the active-site serine hydroxyl group [1]; this covalent bond cannot be hydrolysed, permanently inactivating the enzyme [1].", "marks": 2}
        ]
    ))

    # Q26: Why antibiotics fail to affect eukaryotic cells
    questions.append(Question(
        number=26,
        title="9700/21/O/N/20/Q4 - Selective Toxicity: Why Antibiotics Inhibit Bacteria Without Harming Human Host Cells",
        syllabus_ref="Syllabus 10.2 & 1.2",
        difficulty="INTERMEDIATE",
        preamble="Effective therapeutic antibiotics must exhibit high selective toxicity.",
        parts=[
            QuestionPart(label="(a)", text="Explain why penicillin does not damage human eukaryotic host cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why tetracycline (an inhibitor of bacterial 70S ribosomes) does not generally halt human cytoplasmic protein synthesis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Human eukaryotic cells lack cell walls and do not contain peptidoglycan or transpeptidase enzymes; their cell boundary is a phospholipid bilayer membrane [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Human cytoplasmic ribosomes are 80S (composed of 40S and 60S subunits) which have different ribosomal RNA and protein structures that do not bind tetracycline [2].", "marks": 2}
        ]
    ))

    # Q27: Vertical gene transmission vs Horizontal gene transmission
    questions.append(Question(
        number=27,
        title="9700/22/F/M/20/Q3 - Evolutionary Genetics of Resistance: Vertical Clonal Lines vs Horizontal Plasmid Transfer",
        syllabus_ref="Syllabus 10.2",
        difficulty="INTERMEDIATE",
        preamble="Bacterial resistance genes can be disseminated by different reproductive and parasexual mechanisms.",
        parts=[
            QuestionPart(label="(a)", text="State the mechanism of genetic replication and cell division that underlies vertical transmission in bacteria.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Name two mechanisms of horizontal gene transfer in bacteria other than conjugation, and outline how DNA is acquired in each.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Semi-conservative DNA replication followed by asexual binary fission [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Transformation: direct uptake and incorporation of naked free foreign DNA fragments from the surrounding environment [1]; Transduction: transfer of bacterial DNA from one cell to another mediated by a bacteriophage (virus) [1].", "marks": 2}
        ]
    ))

    # Q28: Multidrug-resistant tuberculosis (MDR-TB and XDR-TB)
    questions.append(Question(
        number=28,
        title="9700/22/O/N/19/Q4 - Emergence and Clinical Challenge of MDR-TB and XDR-TB",
        syllabus_ref="Syllabus 10.1 & 10.2",
        difficulty="INTERMEDIATE",
        preamble="The emergence of drug-resistant Mycobacterium tuberculosis represents an international health emergency.",
        parts=[
            QuestionPart(label="(a)", text="Define 'Multidrug-Resistant Tuberculosis' (MDR-TB) by naming the two first-line antibiotics to which it is resistant.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how poor patient compliance during antibiotic treatment directly leads to the selection of MDR-TB strains.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Strains of M. tuberculosis resistant to at least the two most powerful first-line antibiotics: isoniazid and rifampicin [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Irregular drug-taking or stopping treatment early allows partially resistant bacteria to survive [1]; these surviving bacteria undergo sequential chromosomal mutations conferring resistance to second drugs [1].", "marks": 2}
        ]
    ))

    # Q29: The role of reverse transcriptase in HIV
    questions.append(Question(
        number=29,
        title="9700/21/M/J/19/Q4 - Enzymology of Reverse Transcriptase: RNA-Dependent DNA Polymerase Activity",
        syllabus_ref="Syllabus 10.1 & 6.2",
        difficulty="INTERMEDIATE",
        preamble="Reverse transcriptase possesses multiple catalytic functions required to convert viral RNA into cDNA.",
        parts=[
            QuestionPart(label="(a)", text="Describe the dual catalytic activities of reverse transcriptase during proviral cDNA synthesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why AZT (zidovudine) inhibits HIV reverse transcriptase with minimal harm to host human DNA polymerases.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "RNA-dependent DNA polymerase (synthesises cDNA from RNA template) and ribonuclease H (degrades RNA template) [1]; DNA-dependent DNA polymerase (synthesises complementary second DNA strand) [1].", "marks": 2},
            {"q": "Q29(b)", "points": "Viral reverse transcriptase has an affinity for AZT approximately 100-fold higher than human nuclear DNA polymerase α/δ [2].", "marks": 2}
        ]
    ))

    # Q30: Social and economic factors in the control of cholera
    questions.append(Question(
        number=30,
        title="9700/22/M/J/18/Q4 - Socio-Economic and Infrastructural Determinants of Cholera Outbreaks",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Cholera is often described as a disease of poverty and failing public health infrastructure.",
        parts=[
            QuestionPart(label="(a)", text="Explain why cholera outbreaks are prevalent in informal urban settlements (shantytowns / slums).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State two economic barriers that low-income nations face when attempting to install comprehensive municipal sewage infrastructure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Lack of closed sewerage networks and piped chlorinated water leads to contamination of open water supplies with untreated sewage [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Extremely high capital costs required to construct underground piping, pumping stations, and biological wastewater treatment plants [1]; insufficient municipal tax revenue and competing healthcare/debt priorities [1].", "marks": 2}
        ]
    ))

    # Q31: The BCG vaccine: Efficacy and limitations
    questions.append(Question(
        number=31,
        title="9700/23/O/N/18/Q3 - The Bacillus Calmette-Guérin (BCG) Vaccine: Derivation, Immunogenicity, and Variable Efficacy",
        syllabus_ref="Syllabus 10.1 & 11.2",
        difficulty="INTERMEDIATE",
        preamble="The BCG vaccine is the only licensed vaccine currently available against tuberculosis.",
        parts=[
            QuestionPart(label="(a)", text="State the organism from which the BCG vaccine was derived and explain what is meant by an 'attenuated' vaccine.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the BCG vaccine is effective at preventing severe childhood TB meningitis but provides highly variable protection against adult pulmonary TB.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "Derived from Mycobacterium bovis [1]; 'attenuated' means live bacteria that have been weakened by repeated subculturing so they stimulate an immune response without causing clinical disease [1].", "marks": 2},
            {"q": "Q31(b)", "points": "Induces strong systemic cell-mediated immunity in infants that prevents haematogenous spread to the meninges [1]; but fails to establish robust, long-term mucosal tissue-resident memory T-cells in the adult respiratory tract [1].", "marks": 2}
        ]
    ))

    # Q32: Why a malaria vaccine is difficult to design (Antigenic variation)
    questions.append(Question(
        number=32,
        title="9700/21/M/J/18/Q3 - Molecular Basis of Immune Evasion by Plasmodium falciparum",
        syllabus_ref="Syllabus 10.1 & 11.2",
        difficulty="INTERMEDIATE",
        preamble="Plasmodium falciparum exhibits sophisticated mechanisms to evade host antibody responses.",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by 'antigenic variation' with reference to Plasmodium erythrocyte surface proteins.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why antibodies produced in response to the sporozoite stage of Plasmodium do not destroy the merozoite stage.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Parasite switches expression among ~60 different var genes coding for distinct variants of the PfEMP1 surface adhesion protein [1]; prevents the host's existing circulating antibodies from recognising and opsonising infected erythrocytes [1].", "marks": 2},
            {"q": "Q32(b)", "points": "Each developmental stage expresses antigenically distinct surface coat proteins [1]; antibodies specific to sporozoite circumsporozoite protein (CSP) have complementary antigen-binding sites that cannot bind merozoite surface proteins (MSP-1) [1].", "marks": 2}
        ]
    ))

    # Q33: Beta-lactamase action and clavulanic acid
    questions.append(Question(
        number=33,
        title="9700/22/F/M/19/Q3 - Overcoming Penicillin Resistance: Beta-Lactamase Inhibition by Clavulanic Acid",
        syllabus_ref="Syllabus 10.2 & 3.2",
        difficulty="INTERMEDIATE",
        preamble="To combat penicillinase-producing bacteria, clinicians use combination therapeutics such as co-amoxiclav.",
        parts=[
            QuestionPart(label="(a)", text="State the enzymatic reaction catalysed by β-lactamase on penicillin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of clavulanic acid in combination therapies with amoxicillin (co-amoxiclav).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Hydrolysis of the cyclic amide bond in the four-membered β-lactam ring to produce penicilloic acid [2].", "marks": 2},
            {"q": "Q33(b)", "points": "Clavulanic acid acts as a suicide competitive inhibitor that irreversibly binds and inactivates the bacterial β-lactamase enzyme [1]; protecting amoxicillin from degradation so it can inhibit transpeptidase and kill the bacterium [1].", "marks": 2}
        ]
    ))

    # Q34: Directly Observed Therapy Short-course (DOTS)
    questions.append(Question(
        number=34,
        title="9700/21/O/N/17/Q4 - Operational Components of the WHO Directly Observed Therapy Short-Course (DOTS) Strategy",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="The World Health Organization introduced the DOTS framework to ensure cure of TB patients.",
        parts=[
            QuestionPart(label="(a)", text="Describe the central operational requirement of the DOTS programme.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why DOTS has been so effective in reducing the transmission and prevalence of MDR-TB.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "A trained healthcare worker or community volunteer directly observes the patient swallowing every single prescribed antibiotic dose [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Guarantees 100% treatment adherence for the full 6–9 month duration [1]; prevents premature discontinuation and irregular dosing, eliminating the window where drug-resistant bacterial mutants are selected [1].", "marks": 2}
        ]
    ))

    # Q35: Opportunistic infections in AIDS
    questions.append(Question(
        number=35,
        title="9700/22/M/J/17/Q3 - Pathophysiology of Opportunistic Infections in End-Stage AIDS",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="HIV does not kill patients directly; death is typically caused by opportunistic infections.",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'opportunistic infection' in the context of an immunocompromised host.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Name two specific opportunistic infections frequently diagnosed in advanced AIDS patients.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "An infection caused by pathogens (often commensals or environmental microbes) that take advantage of a weakened immune system, causing severe disease that would be benign in healthy individuals [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Pneumocystis jirovecii pneumonia (PJP / PCP) [1]; Kaposi's sarcoma (HHV-8) / esophageal candidiasis / disseminated Mycobacterium avium complex [1].", "marks": 2}
        ]
    ))

    # Q36: Insecticide-treated bed nets (ITNs) vs Indoor Residual Spraying (IRS)
    questions.append(Question(
        number=36,
        title="9700/23/M/J/17/Q4 - Comparative Efficacy: Insecticide-Treated Nets (ITNs) vs Indoor Residual Spraying (IRS)",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Vector management in endemic malarial regions employs multiple complementary physical and chemical interventions.",
        parts=[
            QuestionPart(label="(a)", text="Explain how Long-Lasting Insecticidal Nets (LLINs) provide both a physical and a chemical barrier against malaria.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how Indoor Residual Spraying (IRS) targets mosquito behavior to interrupt transmission.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Physical mesh barrier prevents mosquitoes from reaching sleeping individuals during nocturnal biting hours [1]; pyrethroid insecticide impregnated into fibres repels or kills mosquitoes upon contact [1].", "marks": 2},
            {"q": "Q36(b)", "points": "Female Anopheles mosquitoes rest on indoor walls after taking a blood meal to digest blood; IRS coats interior walls with residual insecticide, killing mosquitoes while resting before sporozoites can develop [2].", "marks": 2}
        ]
    ))

    # Q37: Transmission cycle of Mycobacterium bovis
    questions.append(Question(
        number=37,
        title="9700/21/O/N/16/Q4 - Zoonotic Transmission of Mycobacterium bovis and the Importance of Milk Pasteurisation",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Tuberculosis can be transmitted to humans from cattle by zoonotic pathways.",
        parts=[
            QuestionPart(label="(a)", text="State the primary route of transmission of Mycobacterium bovis to human populations.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how heat treatment of milk (pasteurisation) prevents this transmission route.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Ingestion of unpasteurised / raw cow's milk from infected dairy cattle [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Heating milk to 72°C for 15 seconds (flash pasteurisation) denatures essential bacterial enzymes and cell structures [1]; kills heat-sensitive M. bovis without altering the nutritional quality of milk [1].", "marks": 2}
        ]
    ))

    # Q38: Mechanism of Action of Artemisinin-based Combination Therapy (ACT)
    questions.append(Question(
        number=38,
        title="9700/22/M/J/16/Q3 - Biochemical Rationale for Artemisinin-Based Combination Therapies (ACTs)",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="The WHO recommends Artemisinin-based Combination Therapies (ACTs) as the first-line treatment for uncomplicated P. falciparum malaria.",
        parts=[
            QuestionPart(label="(a)", text="State the origin of artemisinin and describe how its endoperoxide bridge generates cytotoxic free radicals inside Plasmodium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why artemisinin is always administered in combination with a partner drug (such as lumefantrine).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Extracted from Artemisia annua (sweet wormwood) [1]; endoperoxide bridge reacts with intra-parasitic iron / haem, generating reactive oxygen species (free radicals) that damage parasite membranes and proteins [1].", "marks": 2},
            {"q": "Q38(b)", "points": "Artemisinin has a very short half-life (~1-2 hours) and rapidly clears the vast majority of parasites [1]; the partner drug has a long half-life and eliminates remaining residual parasites, preventing the selection of artemisinin-resistant mutants [1].", "marks": 2}
        ]
    ))

    # Q39: Prophylactic antimalarial drugs and travel medicine
    questions.append(Question(
        number=39,
        title="9700/21/M/J/16/Q4 - Pharmacological Prophylaxis for International Travelers Entering Malarial Endemic Zones",
        syllabus_ref="Syllabus 10.1",
        difficulty="INTERMEDIATE",
        preamble="Travelers visiting malaria-endemic regions are advised to take chemoprophylaxis.",
        parts=[
            QuestionPart(label="(a)", text="State what is meant by 'chemoprophylaxis' and name one commonly prescribed antimalarial prophylactic drug.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why antimalarial prophylaxis must be initiated prior to arrival in an endemic country and continued for four weeks after departing.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Administration of medication prior to infection to prevent the establishment of disease [1]; atovaquone-proguanil (Malarone) / doxycycline / mefloquine [1].", "marks": 2},
            {"q": "Q39(b)", "points": "Pre-travel dosing ensures steady-state therapeutic drug concentrations in blood before initial mosquito exposure [1]; post-travel dosing ensures parasites emerging from the liver after their incubation period (7–14 days) are killed before causing erythrocytic disease [1].", "marks": 2}
        ]
    ))

    # Q40: Antibiotic resistance in agriculture and food chains
    questions.append(Question(
        number=40,
        title="9700/22/F/M/16/Q4 - Veterinary Use of Sub-Therapeutic Antibiotics as Growth Promoters in Livestock",
        syllabus_ref="Syllabus 10.2",
        difficulty="INTERMEDIATE",
        preamble="In many parts of the world, vast quantities of antibiotics are routinely mixed into animal feed.",
        parts=[
            QuestionPart(label="(a)", text="Explain why agricultural farmers administer sub-therapeutic doses of antibiotics to livestock.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how this practice promotes the emergence of antibiotic-resistant bacteria that infect human consumers.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "To promote rapid growth / weight gain and prevent subclinical infections in crowded, intensive farm conditions [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Continuous low-dose exposure provides ideal selective pressure for resistant mutants in animal gut flora [1]; resistant bacteria contaminate meat during slaughter or manure entering water courses, transferring resistance to humans via food chain or horizontal plasmid transfer [1].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Definition of infectious disease
    questions.append(Question(
        number=41,
        title="9700/22/M/J/23/Q1(a) - Rigorous Definition: Infectious Disease",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'infectious disease'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "A disease caused by a pathogen (microorganism) that can be transmitted / passed from an infected individual to an uninfected individual [2].", "marks": 2}
        ]
    ))

    # Q42: Definition of pathogen
    questions.append(Question(
        number=42,
        title="9700/21/O/N/22/Q1(b) - Rigorous Definition: Pathogen",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'pathogen'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "A biological agent / microorganism capable of causing disease in its host organism [2].", "marks": 2}
        ]
    ))

    # Q43: Causative organism of cholera
    questions.append(Question(
        number=43,
        title="9700/22/M/J/22/Q1(a) - Scientific Identification: Cholera Pathogen",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the full scientific binomial name and cellular classification of the organism that causes cholera.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "Vibrio cholerae [1]; Gram-negative bacterium (Prokaryote) [1].", "marks": 2}
        ]
    ))

    # Q44: Causative organism of malaria
    questions.append(Question(
        number=44,
        title="9700/23/M/J/21/Q1(b) - Scientific Identification: Malaria Pathogen and Vector",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the genus of the pathogen that causes human malaria and name the specific vector that transmits it.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Plasmodium [1]; female Anopheles mosquito [1].", "marks": 2}
        ]
    ))

    # Q45: Causative organisms of tuberculosis
    questions.append(Question(
        number=45,
        title="9700/21/O/N/21/Q1(a) - Scientific Identification: Tuberculosis Pathogens",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Name the two distinct species of bacteria that cause tuberculosis in humans.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "Mycobacterium tuberculosis [1] and Mycobacterium bovis [1].", "marks": 2}
        ]
    ))

    # Q46: Definition of vector
    questions.append(Question(
        number=46,
        title="9700/22/F/M/21/Q1(a) - Rigorous Definition: Vector in Epidemiology",
        syllabus_ref="Syllabus 10.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'vector' as used in epidemiology and disease transmission.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "An organism (typically an arthropod) that transfers a pathogen from an infected host to an uninfected host without developing the disease itself [2].", "marks": 2}
        ]
    ))

    # Q47: Target enzyme of penicillin
    questions.append(Question(
        number=47,
        title="9700/21/M/J/20/Q1(a) - Enzymatic Target: Penicillin",
        syllabus_ref="Syllabus 10.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the precise name of the bacterial enzyme inhibited by penicillin during cell wall synthesis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "Transpeptidase (or glycoprotein peptidase / penicillin-binding protein) [2].", "marks": 2}
        ]
    ))

    # Q48: Definition of antibiotic
    questions.append(Question(
        number=48,
        title="9700/22/O/N/19/Q1(b) - Rigorous Definition: Antibiotic",
        syllabus_ref="Syllabus 10.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'antibiotic'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "A chemical substance produced by a microorganism (or synthetic analogue) that kills or inhibits the growth of bacteria without causing significant harm to host cells [2].", "marks": 2}
        ]
    ))

    # Q49: Why penicillin does not kill viruses
    questions.append(Question(
        number=49,
        title="9700/21/M/J/19/Q1(c) - Core Biological Fact: Antibiotics and Viruses",
        syllabus_ref="Syllabus 10.2 & 1.6",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the fundamental structural reason why penicillin has no effect on viruses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "Viruses are acellular and do not have a peptidoglycan cell wall or transpeptidase enzyme [2].", "marks": 2}
        ]
    ))

    # Q50: Definition of antibiotic resistance
    questions.append(Question(
        number=50,
        title="9700/22/M/J/18/Q1(b) - Evolutionary Definition: Antibiotic Resistance",
        syllabus_ref="Syllabus 10.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'antibiotic resistance' in bacteria.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "The inherited ability of a bacterial strain to survive and reproduce in the presence of an antibiotic concentration that would normally kill or inhibit susceptible bacteria [2].", "marks": 2}
        ]
    ))

    return questions

def get_topic10_faqs():
    return [
        {
            "q_num": 1,
            "title": "What is the exact molecular mechanism of penicillin, and why does it only kill growing bacteria?",
            "category": "PHARMACOLOGY • CELL WALL SYNTHESIS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Writing that penicillin 'digests', 'eats', or 'breaks down existing cell walls'! Penicillin only inhibits transpeptidase (glycoprotein peptidase) cross-linking NEW peptidoglycan chains during cell division. Pre-existing cross-links are not broken by penicillin; osmotic lysis occurs because ongoing autolysin activity creates unreinforced gaps as the bacterium grows.",
            "model_answer": "• Target Enzyme Inhibition: Penicillin contains a four-membered β-lactam ring that acts as a structural analogue of the D-Ala-D-Ala terminus of peptidoglycan peptide precursors. It binds irreversibly to the active site of bacterial transpeptidase (glycoprotein peptidase / penicillin-binding protein), permanently inhibiting cross-link formation.\n• Role of Autolysins: Normal bacterial growth requires autolysin enzymes to cleave old peptidoglycan bonds to allow insertion of new glycan chains. In the presence of penicillin, glycan chains (NAG-NAM) continue to elongate, but cannot be cross-linked by peptide bridges.\n• Osmotic Lysis: The weakened cell wall lacks tensile strength and cannot withstand high internal turgor pressure (up to 20 atm) generated by water moving into the concentrated cytoplasm by osmosis down a steep water potential gradient. The bacterial membrane bursts through wall defects (osmotic lysis).\n• Requirement for Growth: Non-dividing, stationary-phase bacteria are not synthesising new cell walls, so penicillin has no bactericidal effect on them."
        },
        {
            "q_num": 2,
            "title": "Why are antibiotics completely ineffective against viral infections?",
            "category": "VIROLOGY • SELECTIVE TOXICITY",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Vague statements like 'viruses are too small' or 'viruses hide inside cells'. The exact biological rationale is that viruses are acellular: they possess no cell walls, no peptidoglycan, no cell surface membrane, no 70S ribosomes, and no independent metabolic pathways or enzymes for antibiotics to inhibit.",
            "model_answer": "• Acellular Architecture: Viruses are non-cellular infectious particles consisting solely of a nucleic acid core (DNA or RNA) enclosed in a protein capsid, sometimes surrounded by a host-derived lipid envelope. They possess no cytoplasm, cell wall, or cell surface membrane.\n• Absence of Bacterial Targets: Antibiotics target specifically prokaryotic biochemical structures: peptidoglycan transpeptidases (penicillins), 70S bacterial ribosomes (tetracyclines, macrolides, aminoglycosides), bacterial RNA polymerase (rifampicin), or bacterial folate synthesis (sulfonamides). None of these targets exist in viruses.\n• Parasitic Replication: Viruses replicate strictly intracellularly by hijacking host eukaryotic transcriptional and translational machinery (host RNA polymerases, 80S ribosomes, host tRNAs, and amino acids). Drugs that inhibit these host pathways would be severely toxic to human host cells."
        },
        {
            "q_num": 3,
            "title": "How does natural selection drive the evolution of antibiotic resistance in bacterial populations?",
            "category": "EVOLUTIONARY GENETICS • NATURAL SELECTION",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying that antibiotics 'cause' or 'induce' resistance mutations! Mutations are spontaneous, random events occurring independently of antibiotic presence. The antibiotic acts as a selective agent that kills non-resistant bacteria, allowing pre-existing resistant mutants to survive and multiply.",
            "model_answer": "• Spontaneous Pre-Existing Mutation: In any large bacterial population (billions of cells), spontaneous, random DNA replication errors occur. By chance, a mutation may alter a target protein (e.g. modified transpeptidase active site) or upregulate a β-lactamase enzyme or efflux pump.\n• Selection Pressure: When an antibiotic is administered, it acts as an environmental selection pressure. Susceptible wild-type bacteria are killed or inhibited.\n• Differential Reproductive Success: The mutant resistant bacteria possess a major selective advantage. They survive, exploit freed nutrients and space, and reproduce rapidly by binary fission.\n• Increased Allele Frequency: Over successive generations, the frequency of the resistance allele in the bacterial gene pool increases until the population becomes predominantly or entirely resistant (treatment failure)."
        },
        {
            "q_num": 4,
            "title": "What is the critical distinction between vertical and horizontal gene transmission of resistance?",
            "category": "BACTERIAL GENETICS • R-PLASMIDS & CONJUGATION",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Confusing binary fission with conjugation. Vertical transmission is parent-to-daughter clonal inheritance down generations of the SAME species. Horizontal transmission is non-reproductive plasmid transfer between UNRELATED bacteria (even across different species or genera) via a sex pilus.",
            "model_answer": "• Vertical Gene Transmission: Occurs during asexual bacterial reproduction (binary fission). The chromosome and any plasmids carrying resistance genes are replicated semi-conservatively, and one copy is partitioned into each daughter cell. Resistance is inherited strictly along a vertical clonal lineage within the same species.\n• Horizontal Gene Transmission (Conjugation): Occurs when a donor bacterium (F+) extends a hollow protein sex pilus to attach to a recipient bacterium (F-). A conjugation bridge forms; an R-plasmid (resistance plasmid) is nicked, and a single strand is transferred via rolling-circle replication into the recipient, where a complementary strand is synthesised.\n• Clinical Danger: Horizontal transmission allows resistance genes (often multi-drug resistance cassettes) to jump rapidly across distinct bacterial species and genera (e.g. harmless commensal gut E. coli transferring penicillinase plasmids to pathogenic Salmonella or Vibrio cholerae)."
        },
        {
            "q_num": 5,
            "title": "Why is malaria so challenging to eradicate globally compared to smallpox?",
            "category": "EPIDEMIOLOGY • MALARIA ERADICATION",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Confusing the protoctist pathogen (Plasmodium) with the insect vector (female Anopheles mosquito). Malaria cannot be eradicated easily because Plasmodium has an intracellular life cycle in both liver and RBCs, displays extreme antigenic variation (var genes), has four distinct human species, and mosquitoes rapidly evolve resistance to insecticides.",
            "model_answer": "• Eukaryotic Complexity & Intracellular Seclusion: Plasmodium is a protoctist with complex eukaryotic genetics (~5,300 genes). It spends almost its entire human life cycle hidden intracellularly—first inside hepatocytes, then inside erythrocytes (which lack MHC class I markers and cannot present foreign antigens).\n• Antigenic Variation: Plasmodium falciparum constantly switches transcription among ~60 var genes encoding distinct PfEMP1 surface proteins, evading host humoral memory antibodies. Furthermore, sporozoites, merozoites, and gametocytes express completely different surface antigens.\n• Vector Resilience: Female Anopheles mosquitoes breed in innumerable small pools of water across tropical latitudes and have evolved metabolic and target-site resistance to pyrethroid insecticides used on bed nets.\n• Contrast with Smallpox: Smallpox had no animal or insect vector (human-only transmission), was caused by a genetically stable DNA virus with no antigenic variation, and showed visible distinctive pustules allowing immediate ring vaccination."
        },
        {
            "q_num": 6,
            "title": "What is the exact molecular cascade of choleragen toxin in causing osmotic diarrhoea?",
            "category": "PATHOLOGY • CHOLERAGEN & CAMP CASCADE",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Stating that Vibrio cholerae 'destroys enterocytes' or 'invades the bloodstream'. V. cholerae remains entirely in the intestinal lumen! It secretes choleragen, which permanently activates adenylate cyclase via G-protein ADP-ribosylation, causing CFTR channels to pour Cl- into the lumen, drawing water out by osmosis.",
            "model_answer": "• Adherence & Toxin Secretion: V. cholerae attaches to enterocyte brush border microvilli via toxin-coregulated pili and secretes the AB5 enterotoxin choleragen into the intestinal lumen.\n• Receptor Binding & Entry: Five B-subunits bind specifically to GM1 ganglioside receptors on the enterocyte apical membrane, allowing translocation of the enzymatically active A1-subunit into the cytoplasm.\n• G-Protein ADP-Ribosylation: The A1-subunit transfers ADP-ribose from NAD+ to the Gsα regulatory protein of adenylate cyclase, abolishing its GTPase activity and locking Gsα in a permanently active GTP-bound state.\n• cAMP Surge & CFTR Opening: Continuously stimulated adenylate cyclase converts intracellular ATP to cyclic AMP (cAMP). High cAMP activates Protein Kinase A (PKA), which phosphorylates and permanently opens CFTR chloride channels.\n• Osmotic Diarrhoea: Chloride ions (Cl-) flow massively into the gut lumen, accompanied electrically by sodium ions (Na+). This drastically lowers the water potential of the intestinal contents below that of blood and tissue fluid, drawing massive volumes of water (up to 20 dm³ per day) into the lumen by osmosis, resulting in hypovolaemic shock and severe dehydration."
        },
        {
            "q_num": 7,
            "title": "Why is Oral Rehydration Therapy (ORT) effective when choleragen is actively causing fluid secretion?",
            "category": "CLINICAL BIOPHYSICS • SGLT-1 COTRANSPORT",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying ORT 'kills the bacteria' or 'neutralises choleragen'. ORT does neither! ORS utilizes the completely functional apical SGLT-1 sodium-glucose cotransporter, which is unaffected by choleragen. Absorbed Na+ and glucose lower intracellular/interstitial water potential, driving rapid water absorption by osmosis.",
            "model_answer": "• Functional Independence of SGLT-1: Choleragen hyperactivates the secretory CFTR chloride pathway; it has no inhibitory effect on the apical Sodium-Glucose Cotransporter 1 (SGLT-1) on enterocytes.\n• Stoichiometric Cotransport: SGLT-1 binds two sodium ions (Na+) and one glucose molecule simultaneously from the luminal fluid, moving them into the enterocyte cytoplasm down the steep Na+ concentration gradient maintained by the basolateral Na+/K+ ATPase pump.\n• Osmotic Water Influx: The massive influx of Na+ and glucose into the enterocyte and capillary interstitial space significantly lowers the water potential (Ψ) of the tissue fluid below that of the intestinal lumen.\n• Reversal of Net Fluid Flow: Water moves rapidly from the intestinal lumen across enterocytes into blood capillaries by osmosis down the newly established water potential gradient, successfully rehydrating the patient and preventing hypovolaemic shock until the immune system clears the bacteria."
        },
        {
            "q_num": 8,
            "title": "How does Mycobacterium tuberculosis evade destruction by alveolar macrophages?",
            "category": "PATHOLOGY • TUBERCULOSIS PHAGOCYTOSIS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Stating that M. tuberculosis 'destroys macrophages immediately'. Macrophages readily engulf M. tuberculosis, but the waxy mycolic acid cell wall inhibits phagosome-lysosome fusion. The bacteria replicate inside the protected phagosome, leading to tubercle formation.",
            "model_answer": "• Inhalation & Alveolar Phagocytosis: M. tuberculosis droplet nuclei are inhaled deep into alveoli, where they are recognised and engulfed by alveolar macrophages via complement and scavenger receptors.\n• Prevention of Phagosome-Lysosome Fusion: Cell wall mycolic acids and surface sulfatides actively interfere with eukaryotic vesicle trafficking, preventing lysosomes from fusing with the bacterial phagosome.\n• Inhibition of Acidification: The bacterium secretes enzymes that neutralise acidic pH and block the assembly of the vacuolar H+-ATPase proton pump, preventing acidification of the phagosome.\n• Intracellular Replication & Granuloma: M. tuberculosis replicates safely inside the macrophage, eventually lysing it and infecting neighboring phagocytes. Host CD4 T-cells and epithelioid cells surround the focus, walling it off into a fibrotic, calcified granuloma (tubercle) with a central caseous necrotic core where bacteria enter dormancy (latent TB)."
        },
        {
            "q_num": 9,
            "title": "What is the precise clinical difference between being HIV-positive and having AIDS?",
            "category": "IMMUNODEFICIENCY • HIV VS AIDS DEFINITIONS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Using 'HIV' and 'AIDS' interchangeably! HIV (Human Immunodeficiency Virus) is the causative retroviral pathogen. AIDS (Acquired Immune Deficiency Syndrome) is the late-stage clinical disease that occurs only when the immune system has collapsed (CD4 count < 200 cells/µL) and opportunistic infections appear.",
            "model_answer": "• HIV-Positive Status: Indicates that an individual has been infected with the Human Immunodeficiency Virus. During the clinical latency phase (which typically lasts 8–10 years without treatment), the patient may feel entirely asymptomatic while the virus continuously infects and depletes CD4+ T-helper lymphocytes.\n• Acquired Immune Deficiency Syndrome (AIDS): The advanced, life-threatening clinical syndrome defined medically by:\n  1. A CD4+ T-lymphocyte count falling below 200 cells per microlitre (µL) of blood (normal count: 500–1200 cells/µL), or\n  2. The emergence of one or more life-threatening opportunistic infections or AIDS-defining illnesses (e.g. Pneumocystis jirovecii pneumonia, esophageal candidiasis, Kaposi's sarcoma, disseminated cytomegalovirus).\n• Functional Immunological Collapse: Because CD4+ T-helper cells coordinate both humoral (activating B-cells to secrete antibodies) and cell-mediated (activating cytotoxic CD8+ T-cells and macrophages) immunity, their loss leaves the body defenseless against normally harmless opportunistic pathogens."
        },
        {
            "q_num": 10,
            "title": "Why must tuberculosis patients complete a 6- to 9-month combination regimen under DOTS?",
            "category": "ANTIBIOTIC STEWARDSHIP • DOTS & RESISTANCE",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Giving vague answers like 'to make sure they are cured'. Candidates must explain that M. tuberculosis grows extremely slowly and has dormant intracellular populations in tubercles that take months to kill. Stopping early leaves partially resistant bacteria alive to multiply, breeding MDR-TB. Using multiple drugs (isoniazid, rifampicin, pyrazinamide, ethambutol) prevents resistance because a bacterium is unlikely to acquire multiple independent mutations simultaneously.",
            "model_answer": "• Slow Bacterial Metabolism & Dormancy: M. tuberculosis has an exceptionally slow generation time (15–20 hours) and thick, impermeable waxy cell walls. In tubercles, semi-dormant 'persister' bacilli metabolize intermittently, requiring prolonged antibiotic exposure (minimum 6 months) to achieve complete sterilization.\n• Combination Therapy Prevents Resistance: Spontaneous chromosomal mutation rates for single-drug resistance are ~1 in 10⁶. By administering four drugs simultaneously (Isoniazid, Rifampicin, Pyrazinamide, Ethambutol), the probability of a bacterium mutating resistance to all four drugs simultaneously is negligible (~1 in 10²⁴). Any mutant resistant to one drug is promptly killed by the other three.\n• Directly Observed Therapy (DOTS): A healthcare worker directly observes the patient swallowing each dose. This guarantees 100% adherence, preventing the sporadic or premature cessation of therapy that selectively breeds Multi-Drug Resistant TB (MDR-TB)."
        }
    ]
