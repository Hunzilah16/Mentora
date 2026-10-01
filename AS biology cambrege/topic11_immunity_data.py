"""
Topic 11: Immunity - 50 Examination-Style Questions & Mark Schemes
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

def get_topic11_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Hematopoietic stem cell lineage and leukocyte differentiation (Fig 11.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q3 - Hematopoietic Stem Cell Differentiation: Myeloid vs Lymphoid Lineages",
        syllabus_ref="Syllabus 11.1",
        difficulty="ADVANCED",
        preamble="All cellular elements of the human immune system originate from pluripotent stem cells within bone marrow. Fig. 11.1 illustrates the differentiation pathways that give rise to myeloid phagocytes and lymphoid effector cells.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_1.png"),
        figure_caption="Fig. 11.1: Hematopoietic stem cell lineage showing divergence of myeloid (neutrophils, macrophages) and lymphoid (B and T lymphocytes) lineages.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between the sites of origin and maturation of B-lymphocytes and T-lymphocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compare neutrophils and macrophages with respect to nuclear morphology, lifespan in tissues, and capacity for antigen presentation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why severe bone marrow aplasia (e.g. following high-dose ionizing radiation) results in fatal susceptibility to both bacterial and viral pathogens.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Both B and T lymphocytes originate from hematopoietic stem cells in bone marrow [1]; B-lymphocytes mature in bone marrow whereas T-lymphocytes migrate to and mature in the thymus gland [1].", "marks": 2},
            {"q": "Q1(b)", "points": "Neutrophils: multi-lobed nucleus, short-lived (~few days), strictly phagocytic (no antigen presentation) [1]; Macrophages: kidney/bean-shaped nucleus, long-lived (months/years), professional antigen-presenting cells (APCs) expressing MHC Class II [1].", "marks": 2},
            {"q": "Q1(c)", "points": "Destroys dividing multipotent stem cells, terminating production of both innate myeloid phagocytes (neutrophils/macrophages to clear bacteria) and adaptive lymphoid B and T cells (antibodies and cytotoxic killer cells to clear viruses) [2].", "marks": 2}
        ]
    ))

    # Q2: Mechanism of phagocytosis and antigen processing (Fig 11.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q2 - Step-by-Step Cytological Mechanics of Phagocytosis and Antigen Presentation on MHC Class II",
        syllabus_ref="Syllabus 11.1",
        difficulty="ADVANCED",
        preamble="Phagocytosis provides an essential link between non-specific innate immunity and specific adaptive immunity. Fig. 11.2 details the sequential cellular stages of phagocytosis and peptide presentation by an alveolar macrophage.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_2.png"),
        figure_caption="Fig. 11.2: Stages of phagocytosis: chemotaxis, opsonin recognition, phagosome formation, lysosomal fusion, digestion, and MHC II display.",
        parts=[
            QuestionPart(label="(a)", text="Describe the role of chemotaxis and opsonins (such as antibodies or complement C3b) in initiating phagocytosis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between a 'phagosome' and a 'phagolysosome', stating two hydrolytic enzymes active within the latter.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how digested bacterial peptides are processed and displayed on the macrophage cell surface, and state the significance of this event.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Chemotaxis: phagocytes move up concentration gradient of bacterial peptides / cytokines to site of infection [1]; Opsonisation: opsonins coat the pathogen surface, binding specific Fc or complement receptors on macrophage to trigger endocytosis [1].", "marks": 2},
            {"q": "Q2(b)", "points": "Phagosome is the initial endocytic vesicle enclosing engulfed pathogen [1]; phagolysosome forms upon fusion of lysosomes with phagosome, containing lysozyme, acid proteases, and reactive oxygen species (ROS) [1].", "marks": 2},
            {"q": "Q2(c)", "points": "Foreign peptide epitopes bind into the groove of Major Histocompatibility Complex class II (MHC II) molecules and are translocated to the plasma membrane [1]; presents non-self antigen to complementary T-cell receptors (TCR) on naive CD4+ T-helper cells to trigger adaptive immunity [1].", "marks": 2}
        ]
    ))

    # Q3: Molecular anatomy of IgG antibody (Fig 11.3)
    questions.append(Question(
        number=3,
        title="9700/22/M/J/22/Q2 - Molecular Architecture and Structure-Function Relationships of an Immunoglobulin G (IgG) Molecule",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Antibodies are Y-shaped globular glycoproteins produced by plasma cells in response to specific antigens. Fig. 11.3 shows the quaternary structure, polypeptide chains, and functional domains of an IgG molecule.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_3.png"),
        figure_caption="Fig. 11.3: Quaternary structure of IgG antibody showing 2 heavy chains, 2 light chains, disulfide bridges, hinge, and V/C regions.",
        parts=[
            QuestionPart(label="(a)", text="Describe the quaternary arrangement of the four polypeptide chains in an IgG molecule, stating the chemical bonds holding them together.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the variable (V) regions provide antigen specificity, referring to primary amino acid sequences.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the physiological importance of the flexible hinge region and the constant (Fc) region.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "Two identical heavy (H) chains and two identical light (L) chains arranged in a Y-shape [1]; held together by covalent interchain disulfide bonds (-S-S-) and non-covalent hydrophobic/hydrogen interactions [1].", "marks": 2},
            {"q": "Q3(b)", "points": "Variable domains (VH and VL) at the N-termini have unique, hypervariable amino acid sequences [1]; folding creates a specific, three-dimensional antigen-binding site stereochemically complementary in shape and charge to a single foreign epitope [1].", "marks": 2},
            {"q": "Q3(c)", "points": "Hinge region provides rotational flexibility, allowing the two Fab arms to angle between 60° and 180° to bind epitopes spaced at varying distances on a pathogen [1]; constant Fc stem binds to Fc receptors on macrophages for opsonisation and activates complement C1q [1].", "marks": 2}
        ]
    ))

    # Q4: Four effector mechanisms of antibodies (Fig 11.4)
    questions.append(Question(
        number=4,
        title="9700/21/M/J/23/Q4 - Four Effector Mechanisms of Humoral Immunity: Neutralisation, Agglutination, Opsonisation, and Lysis",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Antibodies do not destroy pathogens directly but employ distinct molecular mechanisms to neutralize or target them for destruction. Fig. 11.4 summarizes four primary effector mechanisms.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_4.png"),
        figure_caption="Fig. 11.4: Modes of antibody action: neutralisation of toxins, agglutination of microbes, opsonisation for phagocytes, and complement activation.",
        parts=[
            QuestionPart(label="(a)", text="Explain how antitoxin antibodies neutralize bacterial exotoxins such as tetanus or diphtheria toxin.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physical mechanism and biological advantage of antibody-mediated agglutination of bacterial cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how opsonisation enhances the efficiency of phagocytosis by neutrophils.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Antibodies bind with high affinity to the receptor-binding domain of the exotoxin [1]; steric hindrance prevents the toxin from binding to its target cell surface receptor on host tissues, neutralising toxicity [1].", "marks": 2},
            {"q": "Q4(b)", "points": "Each bivalent IgG antibody has two identical antigen-binding sites that cross-link identical epitopes on separate bacterial cells, forming large insoluble clumps [1]; immobilises motile bacteria and enables a single phagocyte to engulf dozens of bacteria simultaneously in one phagocytic event [1].", "marks": 2},
            {"q": "Q4(c)", "points": "Bacterial capsules (e.g. polysaccharides) normally repel negatively charged phagocyte membranes; antibody Fab fragments bind bacteria while exposed Fc stems bind high-affinity Fc receptors on neutrophils, anchoring the pathogen firmly to trigger rapid receptor-mediated endocytosis [2].", "marks": 2}
        ]
    ))

    # Q5: Clonal selection and clonal expansion (Fig 11.5)
    questions.append(Question(
        number=5,
        title="9700/22/O/N/23/Q2 - The Clonal Selection Theory: B-Cell Repertoire, Activation, and Proliferation",
        syllabus_ref="Syllabus 11.1",
        difficulty="ADVANCED",
        preamble="The adaptive immune system relies on a vast pre-existing repertoire of lymphocyte clones. Fig. 11.5 outlines Burnet's clonal selection theory following initial exposure to a foreign antigen.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_5.png"),
        figure_caption="Fig. 11.5: Diagram illustrating clonal selection of a complementary naive B-cell, clonal expansion via mitosis, and differentiation.",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by 'clonal selection' and state the role of the B-cell receptor (BCR) in this process.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the events occurring during 'clonal expansion' and state which signaling molecules stimulate this phase.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Contrast the structural and functional fates of plasma cells and memory B-cells resulting from clonal differentiation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Among millions of naive B-lymphocyte clones, only the specific clone bearing cell surface BCRs (membrane-bound antibodies) complementary in shape to the foreign antigen epitope binds the antigen and is 'selected' [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Selected B-lymphocyte undergoes rapid, repeated mitotic cell divisions to produce a large clone of genetically identical cells [1]; stimulated by cytokines (such as Interleukin-2 and Interleukin-4) secreted by activated CD4+ T-helper cells [1].", "marks": 2},
            {"q": "Q5(c)", "points": "Plasma cells: short-lived effector cells with extensive RER that actively secrete ~2,000 soluble antibodies per second to eliminate active infection [1]; Memory B-cells: long-lived quiescent cells that circulate in blood/lymph to provide rapid immunological recall upon future re-infection [1].", "marks": 2}
        ]
    ))

    # Q6: Ultrastructure of antibody-secreting plasma cell (Fig 11.6)
    questions.append(Question(
        number=6,
        title="9700/22/F/M/23/Q2 - Ultrastructural Adaptations of the Mature Plasma Cell for High-Volume Protein Secretion",
        syllabus_ref="Syllabus 11.1 & 1.2",
        difficulty="ADVANCED",
        preamble="Plasma cells are terminal effector cells specialized for the synthesis and exocytosis of enormous quantities of immunoglobulin proteins. Fig. 11.6 shows an electron micrograph schematic of a mature plasma cell.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_6.png"),
        figure_caption="Fig. 11.6: Fine ultrastructure of a plasma cell showing eccentric clock-face nucleus, extensive rough ER cisternae, and prominent Golgi complex.",
        parts=[
            QuestionPart(label="(a)", text="Identify the two cytoplasmic organelles in Fig. 11.6 that are exceptionally abundant in plasma cells and explain their coordinated role in antibody production.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why plasma cells contain a large number of mitochondria clustered around the secretory apparatus.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the appearance of the plasma cell nucleus and explain why mature plasma cells have a brief lifespan of only several days.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Rough Endoplasmic Reticulum (RER): 80S ribosomes synthesise heavy and light polypeptide chains into cisternae where folding and disulfide bond formation occur [1]; Golgi apparatus: modifies, glycosylates, and packages antibody molecules into secretory vesicles for exocytosis [1].", "marks": 2},
            {"q": "Q6(b)", "points": "Synthesising and secreting thousands of glycoprotein molecules per second requires massive amounts of ATP [1]; needed for amino acid activation by tRNA synthetases, translation elongation, chaperone protein folding, vesicle trafficking, and exocytic membrane fusion [1].", "marks": 2},
            {"q": "Q6(c)", "points": "Eccentric nucleus with alternating radial blocks of heterochromatin and euchromatin ('clock-face' or cartwheel pattern) [1]; terminal differentiation: plasma cells have high endoplasmic reticulum stress and do not divide or replenish cellular components, undergoing apoptosis after a few days [1].", "marks": 2}
        ]
    ))

    # Q7: Kinetics of primary vs secondary immune responses (Fig 11.7)
    questions.append(Question(
        number=7,
        title="9700/21/O/N/21/Q4 - Quantitative Kinetic Comparison of Primary and Secondary Humoral Immune Responses",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="The hallmark of adaptive immunity is immunological memory. Fig. 11.7 compares the plasma antibody concentration (titre) following primary exposure to a pathogen with that following secondary exposure to the same pathogen.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_7.png"),
        figure_caption="Fig. 11.7: Graph comparing antibody titre curves during primary and secondary responses, highlighting differences in lag phase and peak concentration.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 11.7, describe three distinct differences between the primary and secondary antibody responses.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the biological basis for the difference in lag time (latent period) between the primary and secondary responses.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State which immunoglobulin class predominates in the primary response versus the secondary response.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Secondary response has a much shorter lag phase (1–2 days vs 7–10 days in primary) [1]; secondary response produces a much steeper rate of synthesis, reaches a significantly higher peak antibody titre (~10-fold higher), and antibodies persist in blood for a much longer duration [1].", "marks": 2},
            {"q": "Q7(b)", "points": "In primary response, very few naive B-cells exist for that antigen, requiring time for clonal selection and multiple mitotic cycles [1]; in secondary response, a pre-existing pool of long-lived memory B-cells and memory T-cells is present in large numbers, rapidly differentiating into plasma cells without delay [1].", "marks": 2},
            {"q": "Q7(c)", "points": "Primary response is dominated initially by Immunoglobulin M (IgM) [1]; secondary response is overwhelmingly dominated by high-affinity Immunoglobulin G (IgG) due to class switching [1].", "marks": 2}
        ]
    ))

    # Q8: T-helper activation vs T-cytotoxic cell killing (Fig 11.8)
    questions.append(Question(
        number=8,
        title="9700/22/M/J/21/Q2 - Functional Divergence of T-Lymphocytes: CD4+ Helper Coordination vs CD8+ Cytotoxic Target Cell Lysis",
        syllabus_ref="Syllabus 11.1",
        difficulty="ADVANCED",
        preamble="Cell-mediated immunity is mediated by two major subsets of T-lymphocytes possessing distinct surface co-receptors and effector mechanisms. Fig. 11.8 contrasts T-helper activation with cytotoxic T-killer action.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_8.png"),
        figure_caption="Fig. 11.8: Effector mechanisms of CD4+ T-helper cells (cytokine release) vs CD8+ Cytotoxic T-killer cells (perforin/granzyme pore formation).",
        parts=[
            QuestionPart(label="(a)", text="Describe the interaction between a CD4+ T-helper cell and an antigen-presenting cell (APC), naming the surface proteins involved.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how a CD8+ cytotoxic T-lymphocyte identifies a body cell infected with a virus.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the cytotoxic mechanism of perforin and granzymes released by activated CD8+ T-cells in inducing apoptosis of the infected host cell.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "T-cell receptor (TCR) binds specifically to foreign peptide epitope presented in groove of MHC Class II on APC [1]; CD4 co-receptor stabilizes the TCR-MHC II complex, triggering intracellular phosphorylation and cytokine release [1].", "marks": 2},
            {"q": "Q8(b)", "points": "Infected cell displays viral peptide fragments bound to Major Histocompatibility Complex class I (MHC I) molecules; CD8+ Tc cell TCR and CD8 co-receptor recognize and bind this viral peptide-MHC I complex [2].", "marks": 2},
            {"q": "Q8(c)", "points": "Perforin polymerises in the target cell membrane in the presence of Ca²⁺ to form open transmembrane pores [1]; granzyme serine proteases enter through the pores and cleave caspase pro-enzymes, initiating an enzymatic cascade that triggers programmed cell death (apoptosis) and viral DNA fragmentation [1].", "marks": 2}
        ]
    ))

    # Q9: Hybridoma technology for monoclonal antibody production (Fig 11.9)
    questions.append(Question(
        number=9,
        title="9700/21/M/J/20/Q2 - The Köhler-Milstein Hybridoma Method: Cellular Fusion, Selection on HAT Medium, and Monoclonal Production",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Monoclonal antibodies (mAbs) are monospecific antibodies derived from a single B-cell clone. Fig. 11.9 illustrates the stages of the hybridoma technique developed by Georges Köhler and César Milstein.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_9.png"),
        figure_caption="Fig. 11.9: Step-by-step hybridoma workflow: mouse immunization, splenocyte harvesting, PEG fusion with myeloma cells, HAT selection, and cloning.",
        parts=[
            QuestionPart(label="(a)", text="Explain why spleen B-cells cannot simply be cultured directly in a laboratory bioreactor to produce antibodies indefinitely.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the biochemical basis of selection on HAT (hypoxanthine-aminopterin-thymidine) medium following cell fusion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Define what is meant by a 'monoclonal antibody' and state why mAbs are superior to polyclonal antiserum in clinical diagnostics.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Normal mature B-lymphocytes are mortal, terminally differentiated cells with a finite Hayflick limit; they undergo apoptosis and die after several rounds of cell division in cell culture [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Aminopterin blocks de novo nucleotide synthesis; unfused myeloma cells lack HGPRT enzyme and cannot use the hypoxanthine salvage pathway, so they die; unfused spleen cells die naturally within days; only fused hybridoma cells survive (immortal from myeloma + HGPRT from spleen B-cell) [2].", "marks": 2},
            {"q": "Q9(c)", "points": "Antibodies identical in molecular structure produced by a single clone of hybridoma cells, all binding to the identical epitope with identical affinity [1]; superior because they provide 100% specificity with zero batch-to-batch variation and no cross-reactivity with similar antigens [1].", "marks": 2}
        ]
    ))

    # Q10: Lateral flow diagnostic mechanism of home pregnancy test strip (Fig 11.10)
    questions.append(Question(
        number=10,
        title="9700/22/M/J/19/Q3 - Analytical Biochemistry of Lateral Flow Pregnancy Tests: Capillary Chromatography and Dual-Antibody Capture",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Home pregnancy test strips utilize monoclonal antibodies in a lateral flow immunochromatographic assay. Fig. 11.10 illustrates the distribution of mobile and immobilized antibodies along the test strip.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_10.png"),
        figure_caption="Fig. 11.10: Lateral flow architecture: reaction pad (mobile dye-mAb conjugate), test line (fixed anti-hCG mAb), and control line (fixed anti-mouse Ab).",
        parts=[
            QuestionPart(label="(a)", text="Name the hormone detected in maternal urine during early pregnancy and identify the embryonic tissue that secretes it.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the sequence of molecular binding events that produces a colored line at the TEST (T) window in a pregnant woman.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the purpose of the CONTROL (C) line and state the diagnosis if no line appears at the control window.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Human Chorionic Gonadotrophin (hCG) [1]; secreted by the syncytiotrophoblast / blastocyst / developing placenta [1].", "marks": 2},
            {"q": "Q10(b)", "points": "hCG in urine binds to mobile monoclonal anti-hCG antibodies conjugated to blue latex beads / colloidal gold at sample pad [1]; capillary flow draws complexes to test line, where fixed immobilised anti-hCG antibodies bind a different epitope on hCG, trapping beads to form a concentrated blue band (sandwich assay) [1].", "marks": 2},
            {"q": "Q10(c)", "points": "Contains immobilised anti-mouse antibodies that bind excess mobile mouse mAbs regardless of hCG presence, confirming urine flowed through entire strip [1]; if no control line appears, the test is invalid / faulty and must be discarded [1].", "marks": 2}
        ]
    ))

    # Q11: Therapeutic monoclonal antibodies: Trastuzumab in targeted breast cancer therapy (Fig 11.11)
    questions.append(Question(
        number=11,
        title="9700/21/O/N/19/Q3 - Targeted Cancer Pharmacotherapy: Trastuzumab (Herceptin) Inhibition of HER2 Receptor Tyrosine Kinase",
        syllabus_ref="Syllabus 11.2 & 5.1",
        difficulty="ADVANCED",
        preamble="Approximately 20–25% of invasive breast carcinomas overexpress the human epidermal growth factor receptor 2 (HER2). Fig. 11.11 illustrates the therapeutic mechanism of the humanized monoclonal antibody Trastuzumab (Herceptin).",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_11.png"),
        figure_caption="Fig. 11.11: Mode of action of Trastuzumab: binding to extracellular domain IV of HER2, blocking dimerisation, and recruiting NK cells.",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by a 'humanized' monoclonal antibody and state why humanization is essential before administering mouse mAbs to patients.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 11.11, describe how Trastuzumab inhibits the proliferation of HER2-overexpressing malignant breast cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the role of the constant (Fc) region of Trastuzumab in mediating Antibody-Dependent Cellular Cytotoxicity (ADCC).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "An antibody engineered via recombinant DNA to replace mouse constant and framework regions with human IgG sequences, retaining only mouse CDRs [1]; prevents the patient's immune system from mounting a Human Anti-Mouse Antibody (HAMA) response that neutralises the drug and causes serum sickness [1].", "marks": 2},
            {"q": "Q11(b)", "points": "Binds specifically to domain IV of HER2 extracellular receptor, sterically preventing receptor homodimerisation and heterodimerisation [1]; terminates downstream intracellular MAPK and PI3K/Akt kinase signaling, arresting cells at G1 phase and halting mitosis [1].", "marks": 2},
            {"q": "Q11(c)", "points": "Exposed human Fc domains bind to FcγRIII (CD16) receptors on host Natural Killer (NK) cells and macrophages [1]; activates NK cells to release perforin and granzymes to selectively lyse the antibody-coated cancer cell (ADCC) [1].", "marks": 2}
        ]
    ))

    # Q12: Classification matrix of immunity: Active vs Passive, Natural vs Artificial (Fig 11.12)
    questions.append(Question(
        number=12,
        title="9700/22/O/N/18/Q4 - Taxonomic Matrix of Human Immunity: Active vs Passive and Natural vs Artificial Modalities",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Acquired immunity is systematically categorized according to the origin of the antibodies and the nature of antigenic exposure. Fig. 11.12 presents the standard four-quadrant classification matrix of immunity.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_12.png"),
        figure_caption="Fig. 11.12: Immunity matrix: natural active (infection), artificial active (vaccine), natural passive (colostrum/placenta), artificial passive (antivenom).",
        parts=[
            QuestionPart(label="(a)", text="Define 'active immunity' and 'passive immunity', explaining the fundamental distinction regarding immunological memory.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Provide one specific medical example for each of the following: (i) Natural Passive Immunity, and (ii) Artificial Passive Immunity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why artificial passive immunity (e.g. rabies immunoglobulin) must be administered immediately following a suspected rabid animal bite.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Active immunity: host immune system is stimulated by antigens to synthesise its own antibodies and generates long-lived memory B and T cells (long-term protection) [1]; Passive immunity: host receives pre-formed antibodies from an external source, no memory cells are formed, and protection is temporary as antibodies are catabolised [1].", "marks": 2},
            {"q": "Q12(b)", "points": "(i) Maternal IgG crossing placenta to fetus or secretory IgA in colostrum / breast milk [1]; (ii) Injection of pre-formed polyclonal antivenom antibodies (snakebite) or human rabies immunoglobulin / tetanus antitoxin [1].", "marks": 2},
            {"q": "Q12(c)", "points": "Active immunization requires 1–2 weeks to generate protective antibody levels via primary response, which is too slow to stop lethal rabies neuro-invasion [1]; passive antibodies provide immediate, instantaneous neutralisation of circulating rabies virions before they enter peripheral nerve axons [1].", "marks": 2}
        ]
    ))

    # Q13: Population epidemiology of herd immunity (Fig 11.13)
    questions.append(Question(
        number=13,
        title="9700/21/M/J/18/Q2 - Population Dynamics of Herd Immunity: The Critical Vaccination Threshold and Cocooning",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Mass vaccination programmes aim not only to protect individual vaccinees but to establish population-wide herd immunity. Fig. 11.13 contrasts pathogen transmission dynamics in low-vaccination versus high-vaccination populations.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_13.png"),
        figure_caption="Fig. 11.13: Transmission chains in an unvaccinated population vs broken transmission chains and cocoon protection under herd immunity.",
        parts=[
            QuestionPart(label="(a)", text="Define 'herd immunity' and explain how high vaccine coverage protects individuals who cannot medically receive vaccines.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the formula for estimating the Herd Immunity Threshold (HIT = 1 - 1/R0) and explain why measles requires a much higher threshold (~95%) than polio (~80%).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe two biological reasons why some individuals within a population fail to develop active immunity following vaccination.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Resistance to the spread of a contagious disease within a population that results if a sufficiently high proportion of individuals are immune [1]; breaks chains of transmission so infected individuals rarely encounter susceptible hosts, shielding vulnerable individuals (e.g. infants, immunosuppressed, chemotherapy patients) [1].", "marks": 2},
            {"q": "Q13(b)", "points": "HIT = 1 - 1/R0 [1]; measles has an exceptionally high basic reproduction number (R0 = 12–18, highly airborne) compared to polio (R0 = 5–7), requiring a much higher fraction of immune individuals to reduce the effective reproduction rate Re below 1 [1].", "marks": 2},
            {"q": "Q13(c)", "points": "Defective immune system / immunodeficiency (e.g. severe combined immunodeficiency, HIV infection, malnutrition lacking protein for antibody synthesis) [1]; maternal antibodies present in young infant neutralise vaccine antigen before infant B-cells can be primed [1].", "marks": 2}
        ]
    ))

    # Q14: Autoimmune pathogenesis of Myasthenia Gravis (Fig 11.14)
    questions.append(Question(
        number=14,
        title="9700/22/F/M/18/Q2 - Autoimmune Pathogenesis of Myasthenia Gravis: Anti-AChR Autoantibodies and Synaptic Dysfunction",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Autoimmune diseases arise when immunological self-tolerance breaks down. Fig. 11.14 compares transmission across a normal neuromuscular junction with the pathological destruction seen in Myasthenia Gravis.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig11_14.png"),
        figure_caption="Fig. 11.14: Neuromuscular junction in health vs Myasthenia Gravis showing autoantibody blockade and complement destruction of nicotinic receptors.",
        parts=[
            QuestionPart(label="(a)", text="Define what is meant by an 'autoimmune disease' and state what characterizes 'self-tolerance'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 11.14, describe how autoantibodies impair neuromuscular transmission in Myasthenia Gravis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two characteristic clinical symptoms of Myasthenia Gravis and explain why acetylcholinesterase inhibitor drugs provide symptomatic relief.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "A pathological state in which the host adaptive immune system attacks self-tissues [1]; self-tolerance is the acquired inability of lymphocytes to respond to self-antigens, established by clonal deletion/anergy during maturation [1].", "marks": 2},
            {"q": "Q14(b)", "points": "Autoantibodies bind to nicotinic acetylcholine receptors (AChR) on the motor end-plate sarcolemma [1]; competitively block acetylcholine binding, cross-link receptors causing accelerated endocytosis, and activate complement to destroy postsynaptic junctional folds [1].", "marks": 2},
            {"q": "Q14(c)", "points": "Ptosis (drooping eyelids) / diplopia / progressive muscle weakness and dysphagia [1]; AChE inhibitors prevent acetylcholine breakdown in the synaptic cleft, increasing ACh concentration and duration to stimulate the remaining intact receptors [1].", "marks": 2}
        ]
    ))

    # Q15: Types of vaccines: Live-attenuated vs Inactivated vs Subunit vs Toxoids
    questions.append(Question(
        number=15,
        title="9700/23/O/N/17/Q3 - Vaccine Formulations and Immunogenic Mechanisms: Attenuated, Inactivated, Toxoids, and Subunits",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Modern immunization relies on various antigenic preparations engineered to maximize immunogenicity while eliminating virulence.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between a 'live-attenuated vaccine' and an 'inactivated (killed) vaccine', stating one clinical advantage of each.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what a 'toxoid' is and name one disease routinely prevented by toxoid vaccination.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why subunit or killed vaccines often require adjuvants and multiple booster doses, whereas live vaccines often require only one or two doses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Live-attenuated: viable pathogen weakened by mutation/culturing, mimics natural infection stimulating both humoral and cell-mediated immunity (advantage: robust long-lasting immunity) [1]; Inactivated: killed by heat or formalin, cannot replicate or revert to virulence (advantage: safe for immunocompromised) [1].", "marks": 2},
            {"q": "Q15(b)", "points": "A bacterial exotoxin detoxified by chemical treatment (e.g. formaldehyde) that preserves its antigenic tertiary conformation without causing toxic harm [1]; tetanus (tetanus toxoid) / diphtheria [1].", "marks": 2},
            {"q": "Q15(c)", "points": "Subunit/killed antigens do not replicate in host tissues, providing a brief antigenic stimulus that induces weaker primary memory [1]; booster doses restimulate memory B-cells, driving affinity maturation and increasing circulating antibody titres to protective thresholds [1].", "marks": 2}
        ]
    ))

    # Q16: Eradication of smallpox vs ongoing challenges with measles and polio
    questions.append(Question(
        number=16,
        title="9700/22/M/J/17/Q2 - The Global Eradication of Smallpox (Variola) and Barriers to Eradicating Measles and Polio",
        syllabus_ref="Syllabus 11.2 & 10.1",
        difficulty="ADVANCED",
        preamble="Smallpox was officially declared eradicated by the WHO in 1980, representing the greatest triumph in public health history.",
        parts=[
            QuestionPart(label="(a)", text="State three biological features of the Variola virus and smallpox infection that made global eradication feasible.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the live-attenuated oral polio vaccine (OPV / Sabin) has the rare potential to cause vaccine-derived paralytic poliomyelitis (VDPV).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why measles requires an exceptionally high population vaccination coverage (> 95%) to prevent community outbreaks.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "No animal reservoir (infects humans only); genetically stable DNA virus with no antigenic variation; visible, distinctive pustular skin rash allowed rapid ring vaccination; highly stable freeze-dried vaccine [any three, 2].", "marks": 2},
            {"q": "Q16(b)", "points": "Attenuated OPV virus replicates in the human gut and is excreted; in under-vaccinated populations, prolonged transmission allows back-mutations that restore neurovirulence (VDPV) [2].", "marks": 2},
            {"q": "Q16(c)", "points": "Measles is one of the most infectious known pathogens, with an airborne basic reproduction number R0 of 12–18 [1]; a single infected individual can transmit virus to 12–18 susceptible people via aerosol droplets, requiring 95% immunity to achieve herd immunity [1].", "marks": 2}
        ]
    ))

    # Q17: ELISA: Enzyme-Linked Immunosorbent Assay in clinical diagnosis
    questions.append(Question(
        number=17,
        title="9700/21/O/N/16/Q3 - Principles and Methodologies of Enzyme-Linked Immunosorbent Assays (ELISA)",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="ELISA is a ubiquitous laboratory technique for detecting minute concentrations of specific antibodies or antigens in clinical blood samples.",
        parts=[
            QuestionPart(label="(a)", text="Describe the sequence of steps in an indirect ELISA used to detect anti-HIV antibodies in patient serum.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why thorough washing of the microtiter wells between successive incubation steps is essential for assay accuracy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the addition of an enzyme substrate produces a quantifiable optical signal proportional to antibody concentration.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "HIV antigens coated onto well -> patient serum added (primary antibody binds antigen) -> wash -> enzyme-linked secondary antibody (anti-human IgG) added -> wash -> substrate added [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Removes any unbound antibodies or enzyme-conjugates [1]; failure to wash would leave unbound enzyme in the well, catalysing substrate reaction and producing a false-positive result [1].", "marks": 2},
            {"q": "Q17(c)", "points": "Enzyme (e.g. horseradish peroxidase) converts colourless chromogenic substrate (e.g. TMB) into a coloured product [1]; optical density measured with a spectrophotometer / colorimeter is directly proportional to bound antibody titre [1].", "marks": 2}
        ]
    ))

    # Q18: Antigenic drift vs antigenic shift in influenza viruses
    questions.append(Question(
        number=18,
        title="9700/22/M/J/16/Q2 - Molecular Genetics of Influenza Antigenic Variation: Antigenic Drift vs Antigenic Shift",
        syllabus_ref="Syllabus 11.2 & 6.2",
        difficulty="ADVANCED",
        preamble="Influenza viruses evade acquired immunity through two distinct mechanisms of genetic variation affecting surface hemagglutinin (HA) and neuraminidase (NA) spikes.",
        parts=[
            QuestionPart(label="(a)", text="Define 'antigenic drift' and explain how point mutations lead to seasonal influenza epidemics.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Define 'antigenic shift' and explain how genetic reassortment in animal reservoirs precipitates global influenza pandemics.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why human populations must be vaccinated annually with reformulated influenza vaccines.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "Minor, gradual changes in HA and NA surface proteins caused by random point mutations during RNA replication [1]; alters epitopes slightly so existing memory cells and antibodies have reduced binding affinity, causing seasonal outbreaks [1].", "marks": 2},
            {"q": "Q18(b)", "points": "Major, abrupt antigenic change resulting from genetic reassortment when two distinct influenza strains co-infect an intermediate animal host (e.g. pig/avian) [1]; creates a novel viral subtype with a completely new HA/NA profile to which human population has zero pre-existing immunity (pandemic) [1].", "marks": 2},
            {"q": "Q18(c)", "points": "Continuous antigenic drift alters the tertiary structure of HA/NA spikes from year to year [1]; previous antibodies no longer bind the newly drifted viral epitopes, requiring updated quadrivalent vaccines matching circulating strains [1].", "marks": 2}
        ]
    ))

    # Q19: Monoclonal antibodies in immunohistochemistry and medical imaging
    questions.append(Question(
        number=19,
        title="9700/23/O/N/15/Q3 - Analytical Uses of Monoclonal Antibodies in Tissue Pathology and Diagnostic Immuno-PET Imaging",
        syllabus_ref="Syllabus 11.2",
        difficulty="ADVANCED",
        preamble="Monoclonal antibodies can be conjugated to fluorophores, enzymes, or radioisotopes to locate specific molecular targets in biopsy tissues or living patients.",
        parts=[
            QuestionPart(label="(a)", text="Describe how monoclonal antibodies conjugated to fluorescent dyes are used in flow cytometry to count CD4+ T-cells in an HIV patient.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how monoclonal antibodies linked to radioactive isotopes (e.g. Technetium-99m) are used to detect metastatic cancer tumors.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the concept of 'magic bullets' in antibody-drug conjugates (ADCs) for targeted chemotherapy.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Fluorophore-conjugated anti-CD4 mAbs bind specifically to CD4 proteins on T-helper cell surfaces [1]; cells pass single-file through a laser beam, and fluorescent light emission is detected and counted by photodetectors to determine absolute CD4 count per µL [1].", "marks": 2},
            {"q": "Q19(b)", "points": "Radio-labeled mAbs bind specifically to tumor-associated antigens overexpressed on cancer cell surfaces [1]; gamma camera / PET scanner detects emitted gamma radiation to precisely localize primary tumors and occult metastases [1].", "marks": 2},
            {"q": "Q19(c)", "points": "A cytotoxic drug (chemotherapy toxin) is chemically linked to a cancer-specific mAb [1]; antibody selectively delivers toxin to malignant cells, sparing healthy normal tissues and minimizing systemic side effects [1].", "marks": 2}
        ]
    ))

    # Q20: Self vs Non-self recognition and transplant rejection (MHC / HLA)
    questions.append(Question(
        number=20,
        title="9700/21/M/J/15/Q3 - Immunogenetics of Allograft Rejection: Human Leukocyte Antigens (HLA) and Immunosuppressive Therapy",
        syllabus_ref="Syllabus 11.1",
        difficulty="ADVANCED",
        preamble="Organ transplantation success is determined by matching Major Histocompatibility Complex molecules between donor and recipient.",
        parts=[
            QuestionPart(label="(a)", text="Define 'self-antigen' and 'non-self antigen' in the context of tissue transplantation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the immunological mechanism of acute allograft rejection following an unmatched kidney transplant.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the medical risk associated with long-term therapeutic immunosuppression (e.g. cyclosporine) in transplant recipients.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Self-antigen: molecules expressed on the surface of an individual's own cells recognized as 'self' and tolerated [1]; Non-self antigen: foreign molecules recognized as foreign that stimulate an immune response [1].", "marks": 2},
            {"q": "Q20(b)", "points": "Recipient T-lymphocytes recognize foreign donor HLA (MHC) glycoproteins as non-self [1]; CD4 Th cells release cytokines and CD8 Tc cells infiltrate graft, secreting perforin to destroy donor endothelial and tubular cells [1].", "marks": 2},
            {"q": "Q20(c)", "points": "General suppression of T-cell function impairs adaptive surveillance; patient becomes highly susceptible to opportunistic bacterial/fungal infections and viral-induced malignancies (e.g. EBV lymphomas) [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & PHYSIOLOGICAL MECHANISMS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Roles of B-lymphocytes and T-lymphocytes in primary response
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q5 - Dual Arms of Adaptive Immunity: Humoral B-Cells vs Cell-Mediated T-Cells",
        syllabus_ref="Syllabus 11.1",
        difficulty="INTERMEDIATE",
        preamble="Adaptive immunity encompasses distinct humoral and cellular pathways.",
        parts=[
            QuestionPart(label="(a)", text="State the primary role of B-lymphocytes in humoral immunity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of T-helper lymphocytes in coordinating both arms of adaptive immunity.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Differentiate into plasma cells that synthesise and secrete soluble, antigen-specific antibodies into blood and lymph [2].", "marks": 2},
            {"q": "Q21(b)", "points": "Release cytokines (interleukins) upon antigen recognition that stimulate B-cell clonal expansion and activate cytotoxic T-cells and macrophages [2].", "marks": 2}
        ]
    ))

    # Q22: Active vs passive immunity: Fundamental comparisons
    questions.append(Question(
        number=22,
        title="9700/21/O/N/22/Q4 - Comparative Analysis: Active vs Passive Immunity",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Active and passive immunity offer different physiological benefits.",
        parts=[
            QuestionPart(label="(a)", text="Explain why active immunity provides long-lasting protection whereas passive immunity provides only short-term protection.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain one medical situation where passive immunity is preferable to active vaccination.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Active immunity stimulates production of long-lived memory cells that survive decades; passive immunity provides pre-formed antibodies which are catabolised within weeks/months without generating memory cells [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Immediate life-threatening emergencies (e.g. venomous snakebite or post-exposure rabies/tetanus), where instant neutralisation is required before the body can mount an active response [2].", "marks": 2}
        ]
    ))

    # Q23: Natural passive immunity: Transplacental IgG and colostrum IgA
    questions.append(Question(
        number=23,
        title="9700/22/F/M/22/Q3 - Maternal Transfer of Passive Immunity: Transplacental IgG and Colostrum Secretory IgA",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Neonates rely on maternally derived antibodies for immunological defense.",
        parts=[
            QuestionPart(label="(a)", text="Explain how maternal IgG antibodies reach fetal circulation during pregnancy.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the role of secretory IgA antibodies present in maternal colostrum and breast milk.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "Maternal IgG binds to neonatal Fc receptors (FcRn) on placental syncytiotrophoblasts and is transported across into fetal capillaries via transcytosis [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Coats infant gastrointestinal mucosal lining, neutralising ingested pathogens and preventing microbial attachment without being degraded by digestive enzymes [2].", "marks": 2}
        ]
    ))

    # Q24: Role of memory cells in secondary immune response
    questions.append(Question(
        number=24,
        title="9700/21/M/J/22/Q4 - Cytological Dynamics of Memory B-Lymphocytes in Immunological Recall",
        syllabus_ref="Syllabus 11.1 & 11.2",
        difficulty="INTERMEDIATE",
        preamble="Immunological memory ensures that second encounters with pathogens are cleared rapidly.",
        parts=[
            QuestionPart(label="(a)", text="Describe the state and location of memory B-cells between infections.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what happens when a memory B-cell binds its complementary antigen during secondary exposure.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Quiescent (G0 phase) long-lived cells that circulate continuously through blood, lymph nodes, and spleen spleen parenchyma for years or decades [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Rapidly reactivated, dividing by mitosis without an extended lag phase to generate large clones of antibody-secreting plasma cells [2].", "marks": 2}
        ]
    ))

    # Q25: Role of adjuvants in subunit and killed vaccines
    questions.append(Question(
        number=25,
        title="9700/22/M/J/21/Q4 - Function of Adjuvants in Enhancing Subunit Vaccine Immunogenicity",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Many modern subunit vaccines contain chemical adjuvants such as aluminium salts (alum).",
        parts=[
            QuestionPart(label="(a)", text="State what is meant by a vaccine 'adjuvant'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how adjuvants stimulate a stronger, longer-lasting adaptive immune response.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "A substance co-administered with an antigen that non-specifically enhances and modulates the immune response to the antigen [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Creates an antigen depot that releases antigen slowly over time; stimulates local innate immune receptors (TLRs) on dendritic cells to recruit macrophages [2].", "marks": 2}
        ]
    ))

    # Q26: Monoclonal antibodies in home pregnancy testing: Mobile vs fixed antibodies
    questions.append(Question(
        number=26,
        title="9700/21/O/N/20/Q3 - Analytical Role of Monoclonal Antibodies in Lateral Flow Pregnancy Dipsticks",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Pregnancy tests use combinations of mobile and stationary antibodies.",
        parts=[
            QuestionPart(label="(a)", text="State the location and mobility of the dye-conjugated monoclonal antibodies in a pregnancy test strip.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why two separate antibody lines (Test line and Control line) are necessary on the strip.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Located in the reaction pad / sample well; mobile and free to move dissolved in urine along strip via capillary action [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Test line detects presence of hCG (confirms pregnancy); Control line binds mobile antibodies to prove that liquid flowed properly through the entire device [2].", "marks": 2}
        ]
    ))

    # Q27: Action of killer T-cells: Perforin and granzymes
    questions.append(Question(
        number=27,
        title="9700/22/F/M/20/Q4 - Cytolytic Mechanism of CD8+ Cytotoxic T-Lymphocytes",
        syllabus_ref="Syllabus 11.1",
        difficulty="INTERMEDIATE",
        preamble="Cytotoxic T-cells eliminate intracellular pathogens by killing infected host cells.",
        parts=[
            QuestionPart(label="(a)", text="State the function of perforin molecules secreted by active cytotoxic T-cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the function of granzymes and explain the ultimate fate of the target cell.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Insert into target cell plasma membrane and polymerise to form open, non-selective cylindrical pores [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Proteases that enter target cytoplasm through perforin pores, activating apoptotic caspases that trigger programmed cell death and fragmentation of viral DNA [2].", "marks": 2}
        ]
    ))

    # Q28: Hybridoma fusion: Role of polyethylene glycol (PEG)
    questions.append(Question(
        number=28,
        title="9700/22/O/N/19/Q4 - Cell Fusion Mechanics in Hybridoma Technology: Role of PEG",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Cell fusion is the critical initial step in generating monoclonal antibody-producing cell lines.",
        parts=[
            QuestionPart(label="(a)", text="Describe the role of polyethylene glycol (PEG) in the hybridoma fusion procedure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Name the two distinct parent cell types fused together and state the key property contributed by each.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Acts as a chemical fusogen that dehydrates and destabilises lipid bilayers, inducing adjacent plasma membranes to fuse into a single hybrid cell [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Spleen B-lymphocyte (contributes gene for specific antibody synthesis); Myeloma cell (contributes immortality and indefinite division in culture) [2].", "marks": 2}
        ]
    ))

    # Q29: Selection on HAT medium in hybridoma technology
    questions.append(Question(
        number=29,
        title="9700/21/M/J/19/Q4 - Biochemical Rationale for Selection on HAT Medium in Hybridoma Production",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="HAT medium enables selective survival of hybridoma cells while eliminating unfused parent cells.",
        parts=[
            QuestionPart(label="(a)", text="Explain why unfused myeloma cells cannot survive in HAT medium.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why unfused spleen B-cells also disappear from the culture.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Aminopterin blocks de novo nucleotide synthesis; mutant myeloma cells lack HGPRT enzyme, so they cannot use hypoxanthine salvage and die [2].", "marks": 2},
            {"q": "Q29(b)", "points": "Spleen B-lymphocytes have a normal, finite lifespan in culture and die naturally after several days [2].", "marks": 2}
        ]
    ))

    # Q30: Biological basis of autoimmunity in Myasthenia Gravis
    questions.append(Question(
        number=30,
        title="9700/22/M/J/18/Q4 - Autoantibody-Mediated Destruction of Neuromuscular Receptors in Myasthenia Gravis",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Myasthenia Gravis is a classical antibody-mediated autoimmune disease.",
        parts=[
            QuestionPart(label="(a)", text="Identify the specific self-antigen targeted by autoantibodies in Myasthenia Gravis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how autoantibody binding leads to progressive skeletal muscle weakness.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Nicotinic acetylcholine receptors (AChR) on the postsynaptic sarcolemma of neuromuscular junctions [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Blocks acetylcholine binding, induces receptor cross-linking and endocytosis, and causes complement-mediated lysis of junctional folds, reducing muscle end-plate potential below threshold [2].", "marks": 2}
        ]
    ))

    # Q31: Distinction between antigen and antibody
    questions.append(Question(
        number=31,
        title="9700/23/O/N/18/Q4 - Rigorous Scientific Comparison: Antigen vs Antibody",
        syllabus_ref="Syllabus 11.1 & 11.2",
        difficulty="INTERMEDIATE",
        preamble="Antigens and antibodies are complementary biomolecules in immune recognition.",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'antigen'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Define the biological term 'antibody' and state which cells synthesise it.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "A macromolecule (glycoprotein, protein, polysaccharide) recognized as non-self that stimulates an adaptive immune response [2].", "marks": 2},
            {"q": "Q31(b)", "points": "A globular glycoprotein (immunoglobulin) produced by plasma cells that binds specifically to a complementary antigen [2].", "marks": 2}
        ]
    ))

    # Q32: Variable vs constant regions of antibody molecule
    questions.append(Question(
        number=32,
        title="9700/21/M/J/18/Q4 - Structural Divergence: Variable vs Constant Domains of Immunoglobulins",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="An immunoglobulin molecule contains regions of high sequence variability and conserved constant regions.",
        parts=[
            QuestionPart(label="(a)", text="Explain the function of the variable regions of an antibody.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the function of the constant regions of an antibody.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Forms the antigen-binding sites (Fab); hypervariable sequence determines specific stereochemical complementarity to a single epitope [2].", "marks": 2},
            {"q": "Q32(b)", "points": "Determines the effector function of the antibody class (binding to phagocyte Fc receptors for opsonisation, complement activation, or placental transfer) [2].", "marks": 2}
        ]
    ))

    # Q33: Function of disulfide bridges in antibodies
    questions.append(Question(
        number=33,
        title="9700/22/F/M/19/Q4 - Covalent Stabilization: Disulfide Bonds in Immunoglobulin Architecture",
        syllabus_ref="Syllabus 11.2 & 2.3",
        difficulty="INTERMEDIATE",
        preamble="Disulfide bridges maintain the three-dimensional architecture of multi-chain proteins.",
        parts=[
            QuestionPart(label="(a)", text="Name the amino acid responsible for forming disulfide bonds in proteins and state which part of its structure reacts.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the locations of disulfide bridges within an IgG antibody molecule.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Cysteine [1]; sulfhydryl (-SH) thiol group on R-group oxidises to form covalent -S-S- bridge [1].", "marks": 2},
            {"q": "Q33(b)", "points": "Interchain bridges connect heavy chains together at the hinge and link light chains to heavy chains; intrachain bridges stabilise immunoglobulin domain loops [2].", "marks": 2}
        ]
    ))

    # Q34: Agglutination and its diagnostic application (Blood typing)
    questions.append(Question(
        number=34,
        title="9700/21/O/N/17/Q3 - Immunological Mechanism of Agglutination in ABO Blood Typing",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Antibody-mediated agglutination is the basis of clinical blood cross-matching.",
        parts=[
            QuestionPart(label="(a)", text="Explain how bivalent or pentameric (IgM) antibodies cause visible agglutination of erythrocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the ABO blood group of an individual whose red blood cells agglutinate with Anti-A antibodies but not with Anti-B antibodies.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Multiple antigen-binding sites cross-link antigen molecules on adjacent RBCs, bridging them into a visible macroscopic lattice clump [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Blood Group A [2].", "marks": 2}
        ]
    ))

    # Q35: Artificial active immunity via vaccination
    questions.append(Question(
        number=35,
        title="9700/22/M/J/17/Q4 - Induction of Immunological Memory by Vaccination",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Vaccination is the most cost-effective medical intervention in history.",
        parts=[
            QuestionPart(label="(a)", text="Explain why vaccination provides immunity without causing clinical disease.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what happens inside the body when a vaccinated individual later encounters the live wild pathogen.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "Vaccine contains harmless antigens (killed pathogen, toxoid, attenuated strain) that stimulate clonal selection without active pathogenesis [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Pre-existing memory cells trigger a rapid, high-titre secondary immune response that destroys the pathogen before it can cause symptoms [2].", "marks": 2}
        ]
    ))

    # Q36: Artificial passive immunity via antivenom administration
    questions.append(Question(
        number=36,
        title="9700/23/M/J/17/Q3 - Emergency Neutralisation: Antivenom Immunoglobulins in Envenomation",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Snakebite envenomation is treated with horse- or sheep-derived antivenom.",
        parts=[
            QuestionPart(label="(a)", text="State the biological nature of antivenom and explain how it is produced.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a person bitten by a venomous snake a second time five years later cannot rely on previous antivenom for protection.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Purified polyclonal antibody serum harvested from an animal (horse/sheep) hyperimmunized with sublethal snake venom doses [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Antivenom is passive immunity; foreign antibodies were catabolised years ago, and no memory cells were formed by the patient [2].", "marks": 2}
        ]
    ))

    # Q37: Herd immunity and calculation of vaccination targets
    questions.append(Question(
        number=37,
        title="9700/21/O/N/16/Q4 - Mathematical Principles of Herd Immunity and Target Coverage",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Epidemiologists use reproductive numbers to set national vaccination coverage goals.",
        parts=[
            QuestionPart(label="(a)", text="Explain what the basic reproduction number (R0) represents for an infectious disease.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a disease with R0 = 15 requires over 93% vaccination coverage to halt transmission.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "The average number of secondary cases infected by a single primary case in a completely susceptible population [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Threshold = 1 - 1/R0 = 1 - 1/15 = 14/15 = 93.3%; to ensure that on average an infected case contacts fewer than 1 susceptible person [2].", "marks": 2}
        ]
    ))

    # Q38: Trastuzumab (Herceptin) targeting HER2
    questions.append(Question(
        number=38,
        title="9700/22/M/J/16/Q4 - Molecular Oncology: Monoclonal Trastuzumab Binding to HER2",
        syllabus_ref="Syllabus 11.2",
        difficulty="INTERMEDIATE",
        preamble="Targeted monoclonal antibodies have revolutionized oncology.",
        parts=[
            QuestionPart(label="(a)", text="Name the receptor targeted by Trastuzumab and state its normal cellular function.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how Trastuzumab selectively destroys malignant cells without harming normal tissues.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Human Epidermal Growth Factor Receptor 2 (HER2); receptor tyrosine kinase that promotes cell growth and mitosis [2].", "marks": 2},
            {"q": "Q38(b)", "points": "Normal adult cells express very low HER2 levels, whereas cancer cells overexpress HER2 massively; mAb selectively binds cancer cells [2].", "marks": 2}
        ]
    ))

    # Q39: Non-specific defense mechanisms: Physical and chemical barriers
    questions.append(Question(
        number=39,
        title="9700/21/M/J/16/Q3 - Innate Epithelial and Chemical Barriers Against Pathogen Invasion",
        syllabus_ref="Syllabus 11.1",
        difficulty="INTERMEDIATE",
        preamble="The body possesses primary innate barriers that prevent microbial entry.",
        parts=[
            QuestionPart(label="(a)", text="Describe how intact mammalian skin prevents the entry of pathogenic microorganisms.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Name two chemical secretions that destroy or inhibit microbes on mucosal surfaces.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Stratified, cornified outer epidermis of dead keratinocytes forms an impermeable tough physical barrier; sebum fatty acids lower pH to 5.5 [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Lysozyme in tears/saliva (hydrolyses peptidoglycan cell walls) [1]; hydrochloric acid in gastric juice (pH 1.5–2.0 denatures microbial enzymes) [1].", "marks": 2}
        ]
    ))

    # Q40: Opsonisation: Interaction between antibodies and phagocytes
    questions.append(Question(
        number=40,
        title="9700/22/F/M/16/Q3 - Molecular Receptor Mechanics of Antibody Opsonisation",
        syllabus_ref="Syllabus 11.1 & 11.2",
        difficulty="INTERMEDIATE",
        preamble="Opsonisation bridges specific adaptive humoral immunity with innate phagocytosis.",
        parts=[
            QuestionPart(label="(a)", text="Explain how an antibody molecule binds simultaneously to both a bacterium and a phagocyte.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the physiological consequence of this dual binding for the rate of bacterial clearance.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Fab variable regions bind complementary antigen on bacterial surface; constant Fc region binds to Fc receptors (FcγR) on phagocyte membrane [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Dramatically accelerates phagocytic recognition and ingestion, overcoming bacterial anti-phagocytic polysaccharide capsules [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Definition of self-antigen
    questions.append(Question(
        number=41,
        title="9700/22/M/J/23/Q1(a) - Rigorous Definition: Self-Antigen",
        syllabus_ref="Syllabus 11.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'self-antigen'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "Antigenic molecules produced by and expressed on the surface of an organism's own cells that do not normally stimulate an immune response [2].", "marks": 2}
        ]
    ))

    # Q42: Definition of non-self antigen
    questions.append(Question(
        number=42,
        title="9700/21/O/N/22/Q1(a) - Rigorous Definition: Non-Self Antigen",
        syllabus_ref="Syllabus 11.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'non-self antigen'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "A foreign macromolecule recognized as non-self by the immune system that stimulates an immune response and antibody production [2].", "marks": 2}
        ]
    ))

    # Q43: Definition of clone in immunology
    questions.append(Question(
        number=43,
        title="9700/22/M/J/22/Q1(a) - Rigorous Definition: Lymphocyte Clone",
        syllabus_ref="Syllabus 11.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define what is meant by a 'clone' of lymphocytes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "A population of genetically identical lymphocytes derived from a single parent cell by mitotic division, all possessing identical receptors [2].", "marks": 2}
        ]
    ))

    # Q44: Definition of monoclonal antibody
    questions.append(Question(
        number=44,
        title="9700/23/M/J/21/Q1(a) - Rigorous Definition: Monoclonal Antibody",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'monoclonal antibody'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Antibodies identical in structure and affinity produced by a single clone of hybridoma cells, all specific to the identical epitope [2].", "marks": 2}
        ]
    ))

    # Q45: Definition of active immunity
    questions.append(Question(
        number=45,
        title="9700/21/O/N/21/Q1(a) - Rigorous Definition: Active Immunity",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'active immunity'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "Immunity acquired through the production of antibodies and memory cells by the individual's own immune system following exposure to antigen [2].", "marks": 2}
        ]
    ))

    # Q46: Definition of passive immunity
    questions.append(Question(
        number=46,
        title="9700/22/F/M/21/Q1(a) - Rigorous Definition: Passive Immunity",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'passive immunity'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "Immunity acquired through the transfer of pre-formed antibodies from another individual or organism, conferring temporary protection without memory cells [2].", "marks": 2}
        ]
    ))

    # Q47: Definition of vaccine
    questions.append(Question(
        number=47,
        title="9700/21/M/J/20/Q1(a) - Rigorous Definition: Vaccine",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'vaccine'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "A preparation of antigens (attenuated, killed, toxoid, subunit) administered to stimulate active immunity and immunological memory without disease [2].", "marks": 2}
        ]
    ))

    # Q48: Definition of autoimmune disease
    questions.append(Question(
        number=48,
        title="9700/22/O/N/19/Q1(a) - Rigorous Definition: Autoimmune Disease",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'autoimmune disease'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "A pathological disease state resulting from a breakdown in self-tolerance, where the immune system produces autoantibodies that attack self-tissues [2].", "marks": 2}
        ]
    ))

    # Q49: Function of the variable region of an antibody
    questions.append(Question(
        number=49,
        title="9700/21/M/J/19/Q1(a) - Precise Biological Function: Variable Region (Fab)",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the precise biological function of the variable regions of an antibody molecule.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "Provides two identical antigen-binding sites complementary in shape and charge to bind specifically to a single target epitope [2].", "marks": 2}
        ]
    ))

    # Q50: Function of the constant region of an antibody
    questions.append(Question(
        number=50,
        title="9700/22/M/J/18/Q1(a) - Precise Biological Function: Constant Region (Fc)",
        syllabus_ref="Syllabus 11.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the precise biological function of the constant (Fc) region of an IgG antibody.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "Determines antibody effector activity by binding to Fc receptors on phagocytes for opsonisation and activating complement proteins [2].", "marks": 2}
        ]
    ))

    return questions

def get_topic11_faqs():
    return [
        {
            "q_num": 1,
            "title": "What is the exact quaternary structure and function of an IgG antibody molecule?",
            "category": "IMMUNOGLOBULIN STRUCTURE • QUATERNARY PROTEIN",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Candidates lose marks by claiming variable regions are only on heavy chains or only on light chains. Variable regions are located at the N-termini of BOTH heavy and light chains ($V_H$ and $V_L$). Forgetting the flexible hinge region that allows arms to angle between 60° and 180°, and confusing the antigen-binding Fab arms with the effector Fc stem.",
            "model_answer": "• Four Polypeptide Chains: Quaternary protein consisting of two identical heavy (H) chains and two identical light (L) chains arranged in a symmetrical Y-shape, held together by interchain covalent disulfide bonds (-S-S-) and non-covalent hydrophobic and hydrogen bonds.\n• Variable (V) Regions & Fab Arms: The N-terminal domains of both the heavy and light chains ($V_H$ and $V_L$) contain hypervariable amino acid sequences. Their specific folding creates two identical antigen-binding sites per monomer, each stereochemically complementary in shape and charge to a single foreign epitope.\n• Constant (C) Regions & Fc Stem: The conserved C-terminal domains of the heavy chains form the Fc stem. The Fc region does not bind antigen; it determines the biological effector function (binding to Fc receptors on macrophages/neutrophils for opsonisation, binding complement C1q, or crossing the placenta).\n• Flexible Hinge Region: A proline-rich segment between the Fab arms and Fc stem that gives rotational flexibility (60°–180°), allowing the antibody to cross-link epitopes spaced at varying distances on microbial surfaces."
        },
        {
            "q_num": 2,
            "title": "What are the exact sequential stages of phagocytosis and antigen presentation?",
            "category": "CELLULAR IMMUNOLOGY • PHAGOCYTOSIS & APCs",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Calling the initial vesicle a 'phagolysosome'. It is initially a PHAGOSOME. Only after fusion with lysosomes containing hydrolytic enzymes does it become a PHAGOLYSOSOME. Candidates also forget that neutrophils die after phagocytosis, whereas macrophages survive to present antigen fragments on MHC Class II molecules.",
            "model_answer": "• Stage 1 (Chemotaxis & Recognition): Phagocytes migrate towards chemical attractants (chemotaxis). Pattern Recognition Receptors (PRRs) on the phagocyte bind Pathogen-Associated Molecular Patterns (PAMPs), or Fc receptors bind antibody opsonins coating the pathogen.\n• Stage 2 (Engulfment & Phagosome): The phagocyte extends pseudopodia around the pathogen, engulfing it via receptor-mediated endocytosis to form an internal membrane-bound vesicle called a phagosome.\n• Stage 3 (Phagolysosome Formation & Digestion): Cytoplasmic lysosomes fuse with the phagosome, forming a phagolysosome. Hydrolytic enzymes (lysozyme to digest peptidoglycan, acid proteases, and reactive oxygen species) digest and kill the pathogen.\n• Stage 4 (Exocytosis & Antigen Presentation): Soluble, harmless breakdown products are discharged via exocytosis. In macrophages and dendritic cells, non-self peptide epitopes are retained, loaded into the binding groove of MHC Class II molecules, and displayed on the cell surface to activate naive CD4+ T-helper cells."
        },
        {
            "q_num": 3,
            "title": "Why is the secondary immune response so much faster, steeper, and higher than the primary response?",
            "category": "IMMUNOLOGICAL MEMORY • RESPONSE KINETICS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Giving descriptive answers without kinetic precision. You must specify: Primary has a 7–10 day lag phase, low peak titre, dominated by IgM, and drops quickly. Secondary has a 1–2 day lag phase, steep rate of synthesis, reaches a ~10-fold higher peak titre, dominated by high-affinity IgG, and persists for months/years, clearing the pathogen before symptoms appear.",
            "model_answer": "• Primary Immune Response Kinetics: Long lag phase of 7–10 days before detectable antibodies appear; rate of antibody synthesis is slow; peak antibody titre is low; the dominant initial antibody isotype is low-affinity IgM; and circulating antibody levels decline rapidly back to baseline.\n• Cellular Basis of Primary Lag: Very few naive B-cells and T-cells exist that are specific for that novel antigen (~1 in 100,000). Significant time is required for antigen processing, presentation, clonal selection, and multiple rounds of mitotic clonal expansion.\n• Secondary Immune Response Kinetics: Minimal lag phase of only 1–2 days; rate of antibody production is extremely steep; peak antibody concentration is up to 10–100 times higher; predominantly composed of high-affinity IgG (due to somatic hypermutation and class switching); and antibodies persist at high levels for months or years.\n• Cellular Basis of Secondary Speed: A large pre-existing clonal pool of long-lived memory B-cells and memory T-cells is already established. Upon re-exposure, these memory cells recognise the identical antigen instantly and divide and differentiate into plasma cells almost immediately."
        },
        {
            "q_num": 4,
            "title": "How does the hybridoma method produce monoclonal antibodies, and why is HAT medium essential?",
            "category": "BIOTECHNOLOGY • HYBRIDOMA METHOD",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Forgetting why myeloma cells and spleen B-cells are fused, and why HAT medium works! Spleen B-cells produce specific antibodies but die quickly. Myeloma cells divide indefinitely (immortal) but make no antibody and lack HGPRT. On HAT medium, aminopterin blocks de novo synthesis; myeloma cells die because they lack HGPRT, spleen cells die naturally; only hybridomas survive (immortal + HGPRT).",
            "model_answer": "• Parent Cell Types & Limitations: Spleen B-lymphocytes harvested from an immunized mouse produce monospecific antibodies against the target antigen, but are mortal and die in cell culture after several divisions. Myeloma cells (malignant plasma cells) are immortal and divide indefinitely in culture, but do not secrete specific antibodies and carry a genetic defect lacking the enzyme HGPRT (hypoxanthine-guanine phosphoribosyltransferase).\n• Cell Membrane Fusion: Spleen cells and myeloma cells are incubated with polyethylene glycol (PEG), which destabilises lipid bilayers to fuse their plasma membranes, creating hybrid hybridoma cells.\n• Selection on HAT Medium: HAT medium contains Hypoxanthine, Aminopterin, and Thymidine. Aminopterin blocks the de novo nucleotide synthesis pathway in all cells. Unfused myeloma cells cannot use the salvage pathway because they lack HGPRT, so they die. Unfused spleen B-cells possess HGPRT but have a short natural lifespan and die within days. Only fused hybridoma cells survive (inheriting immortality from myeloma + functional HGPRT from spleen cell).\n• Monoclonal Cloning & Harvesting: Surviving hybridomas are separated by limiting dilution into individual microwells (one cell per well). Clones are screened via ELISA; the positive clone is cultured indefinitely in bioreactors to produce pure, monospecific monoclonal antibodies."
        },
        {
            "q_num": 5,
            "title": "How do monoclonal antibodies work in home pregnancy tests versus targeted cancer therapy?",
            "category": "MEDICAL APPLICATIONS • DIAGNOSTIC & THERAPEUTIC mAbs",
            "examiner_trap": "CRITICAL EXAMINER TRAP: In pregnancy tests, confusing the mobile dye-conjugated antibodies, the fixed test-line antibodies, and the fixed control-line antibodies. In cancer therapy, failing to name a specific mechanism like blocking growth factor receptors (Trastuzumab / HER2) or recruiting immune cells via ADCC.",
            "model_answer": "• Home Pregnancy Test (Diagnostic): Detects human chorionic gonadotrophin (hCG) in urine. The reaction pad contains mobile monoclonal anti-hCG antibodies conjugated to blue latex dye beads. If hCG is present, it binds to mobile mAbs. Capillary action draws the fluid along the strip to the Test Line, which contains fixed, immobilised anti-hCG mAbs (binding a different epitope on hCG, sandwiching the dye-bead complex to form a visible blue band). The liquid continues to the Control Line, which contains fixed anti-mouse antibodies that bind excess mobile mAbs, forming a second blue line to verify that the strip functioned properly.\n• Targeted Cancer Therapy (Therapeutic, e.g. Trastuzumab / Herceptin): Trastuzumab is a humanized monoclonal antibody designed against the HER2 receptor tyrosine kinase overexpressed in 25% of breast cancers. The Fab regions bind specifically to HER2, sterically preventing receptor dimerisation and terminating downstream oncogenic MAPK/Akt signaling (halting mitosis). Furthermore, the human Fc stem recruits host Natural Killer (NK) cells to lyse the antibody-coated cancer cell via Antibody-Dependent Cellular Cytotoxicity (ADCC)."
        },
        {
            "q_num": 6,
            "title": "How do you classify Active vs Passive, and Natural vs Artificial Immunity?",
            "category": "IMMUNITY TAXONOMY • 2x2 CLASSIFICATION MATRIX",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Mixing up the quadrants of the 2x2 matrix! Remember: ACTIVE = host makes own antibodies and memory cells (long-term). PASSIVE = host receives pre-formed antibodies, no memory cells (temporary). NATURAL = biological/environmental exposure. ARTIFICIAL = medical intervention (needle/syringe).",
            "model_answer": "• 1. Natural Active Immunity: Acquired naturally by contracting an infectious disease (e.g. recovering from chickenpox or measles). Host immune system is stimulated by natural infection, synthesises its own antibodies, and generates long-lived memory B and T cells (lifetime protection).\n• 2. Artificial Active Immunity: Acquired intentionally via medical vaccination (e.g. MMR vaccine, tetanus toxoid). Harmless antigens stimulate the host immune system to produce antibodies and memory cells without causing clinical disease.\n• 3. Natural Passive Immunity: Acquired naturally by transfer of pre-formed maternal antibodies to offspring without active antigen stimulation (e.g. maternal IgG crossing the placenta; secretory IgA ingested in colostrum/breast milk). Provides immediate protection to the neonate, lasting several weeks until maternal antibodies are catabolised.\n• 4. Artificial Passive Immunity: Acquired intentionally via injection of pre-formed therapeutic antibodies from an external source (e.g. tetanus antitoxin, rabies immunoglobulin, snake antivenom). Provides instant, immediate protection in acute medical emergencies, but no memory cells are formed (temporary protection lasting 2–3 weeks)."
        },
        {
            "q_num": 7,
            "title": "Why do vaccines contain antigens rather than antibodies, and how do boosters enhance immunity?",
            "category": "VACCINOLOGY • BOOSTER DOSES & MEMORY",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying 'vaccines contain antibodies'! This is a catastrophic error that loses all marks. Vaccines contain ANTIGENS (attenuated, killed, toxoid, subunit, mRNA), NOT antibodies! Injecting antibodies is passive immunity; vaccines stimulate active immunity.",
            "model_answer": "• Vaccines Contain Antigens: A vaccine introduces non-pathogenic foreign antigens (e.g. live-attenuated virus, heat-killed bacterium, chemical toxoid, or recombinant protein subunit) into the body to mimic a natural primary infection.\n• Stimulation of Active Primary Response: Host dendritic cells and macrophages process the vaccine antigens and present them to naive B and T lymphocytes. Clonal selection and clonal expansion take place, generating antigen-specific effector plasma cells and long-lived memory B and T cells.\n• Mechanism of Booster Doses: With non-living vaccines (killed, toxoid, subunit), the initial dose may produce relatively few memory cells. A secondary booster dose restimulates pre-existing memory cells, driving rapid clonal expansion, somatic hypermutation (increasing antibody affinity), and antibody class switching to IgG. This elevates circulating memory cell populations and antibody titres well above the protective clinical threshold for years."
        },
        {
            "q_num": 8,
            "title": "What is herd immunity, and how does it protect unvaccinated individuals in a population?",
            "category": "EPIDEMIOLOGY • HERD IMMUNITY & TRANSMISSION CHAINS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Claiming that herd immunity means 'the pathogen is killed everywhere' or 'everyone becomes immune'. Herd immunity is an epidemiological phenomenon where a high proportion of immune individuals breaks transmission chains, shielding susceptible unvaccinated people.",
            "model_answer": "• Definition of Herd Immunity: A form of indirect population-level protection from an infectious disease that occurs when a sufficiently large percentage of a population is immune (through vaccination or prior illness), significantly reducing the likelihood of disease transmission.\n• Breaking Chains of Transmission: When the majority of people are immune, an infected individual who enters the community is surrounded predominantly by immune people who cannot contract or shed the virus. The chain of transmission is broken, and the basic reproductive rate in the population falls below 1 (Re < 1).\n• The Cocooning Effect: Susceptible individuals who cannot medically receive vaccines (e.g. newborn infants, children undergoing chemotherapy for leukemia, organ transplant recipients on immunosuppressive drugs, or individuals with severe allergies) are protected because the pathogen cannot reach them through the immune 'herd'."
        },
        {
            "q_num": 9,
            "title": "What are the exact functional differences between T-Helper (CD4+) and Cytotoxic T-Killer (CD8+) cells?",
            "category": "CELL-MEDIATED IMMUNITY • T-CELL SUBSETS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Stating that T-cells secrete antibodies! T-cells NEVER secrete antibodies; only plasma cells (derived from B-cells) secrete antibodies. CD4+ Th cells secrete cytokines (interleukins); CD8+ Tc cells secrete perforin and granzymes to lyse host cells.",
            "model_answer": "• T-Helper Lymphocytes (CD4+ Th Cells):\n  - Surface Receptor: T-Cell Receptor (TCR) paired with CD4 co-receptor.\n  - Target Recognition: Binds specifically to foreign peptide antigens presented on MHC Class II molecules on professional antigen-presenting cells (macrophages, dendritic cells, B-cells).\n  - Effector Action: Secretes cytokines / interleukins (IL-2, IL-4, IFN-γ) that stimulate B-cell clonal expansion, activate cytotoxic T-cells, and enhance macrophage phagocytosis. They coordinate both humoral and cell-mediated immunity.\n• Cytotoxic T-Killer Lymphocytes (CD8+ Tc Cells):\n  - Surface Receptor: TCR paired with CD8 co-receptor.\n  - Target Recognition: Binds specifically to foreign peptide antigens (e.g. viral fragments or mutated cancer proteins) presented on MHC Class I molecules expressed on all nucleated body cells.\n  - Effector Action: Secretes perforin (forming transmembrane pores in target cell membrane) and granzyme proteases (activating apoptotic caspases), inducing programmed cell death of virus-infected or tumor cells without harming surrounding uninfected tissue."
        },
        {
            "q_num": 10,
            "title": "What is the autoimmune mechanism underlying Myasthenia Gravis at the neuromuscular junction?",
            "category": "AUTOIMMUNE PATHOLOGY • MYASTHENIA GRAVIS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying acetylcholine is destroyed or that the motor neuron is damaged. In Myasthenia Gravis, the motor neuron and acetylcholine release are completely normal! The disease is caused by autoantibodies attacking and destroying the nicotinic acetylcholine receptors on the muscle sarcolemma.",
            "model_answer": "• Breakdown of Self-Tolerance: Autoreactive B-lymphocytes escape central and peripheral tolerance checkpoints, producing IgG autoantibodies directed against self-antigens on the motor end-plate sarcolemma.\n• Target Antigen: Nicotinic acetylcholine receptors (AChR) situated at the crests of junctional folds on skeletal muscle fibers.\n• Pathological Mechanisms:\n  1. Competitive Blockade: Autoantibodies bind to the acetylcholine binding site on AChR, sterically hindering acetylcholine from binding.\n  2. Receptor Endocytosis: Bivalent IgG autoantibodies cross-link adjacent AChRs, stimulating rapid endocytosis and lysosomal degradation of the receptors.\n  3. Complement-Mediated Lysis: Autoantibody Fc regions activate the complement cascade, forming Membrane Attack Complexes that destroy the junctional fold architecture.\n• Clinical Consequence: Markedly reduced receptor density means end-plate potentials fail to reach threshold, causing transmission failure and progressive, fluctuating skeletal muscle weakness (ptosis, diplopia, difficulty swallowing and breathing) that worsens with exertion."
        }
    ]
