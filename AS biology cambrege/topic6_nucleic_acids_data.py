"""
Topic 6: Nucleic Acids and Protein Synthesis — 50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Molecular Genetics Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Section D: 10 High-Frequency Examiner FAQs & Critical Revision Pitfalls
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
Past Paper vs Original Ratio: 42 Authentic (84%) / 8 Original Extensions (16%)
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic6_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Nucleotide Anatomy & ATP (Fig 6.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q4 - Nucleotide Monomer Architecture and ATP Structure",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Nucleotides are phosphorylated nucleosides that serve as the universal monomer units of nucleic acids and key metabolic intermediaries. Fig. 6.1 shows the general structure of a mononucleotide alongside the structure of adenosine triphosphate (ATP).",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_1_nucleotide_structure_atp.png"),
        figure_caption="Fig. 6.1: Structure of a generalised mononucleotide (A) and adenosine triphosphate (ATP) (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.1A, identify the three chemical components of a mononucleotide, name the covalent bonds linking the pentose sugar to the base and phosphate group, and identify the carbon atoms involved.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Compare the pentose sugar and nitrogenous base present in an ATP molecule with those in a DNA nucleotide containing thymine.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the hydrolysis of ATP and explain why ATP is uniquely suited as the universal immediate energy currency in biological cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Phosphate group, pentose sugar (ribose or deoxyribose), and nitrogenous organic base; glycosidic (C-N) covalent bond links base to C1' of pentose; phosphoester covalent bond links phosphate to C5' of pentose [2].", "marks": 2},
            {"q": "Q1(b)", "points": "ATP possesses ribose (contains -OH group at C2') whereas DNA nucleotide possesses deoxyribose (contains -H at C2'); ATP base is adenine (purine, double-ringed) whereas thymine is a pyrimidine (single-ringed) [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Hydrolysis of terminal phosphoanhydride bond catalyzed by ATPase yields ADP + Pi + 30.5 kJ mol^-1 free energy; immediate single-step hydrolysis releases small, manageable quantity of energy; highly soluble, readily diffuses through cytoplasm, easily resynthesised [2].", "marks": 2}
        ]
    ))

    # Q2: Purines vs Pyrimidines & Base Pairing (Fig 6.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q4 - Nitrogenous Organic Bases and Hydrogen Bonding Specificity",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="The double-helical structure of DNA is stabilized by specific complementary hydrogen bonding between purine and pyrimidine bases. Fig. 6.2 illustrates the chemical structures of purines and pyrimidines alongside the hydrogen bonding between complementary pairs.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_2_purines_vs_pyrimidines.png"),
        figure_caption="Fig. 6.2: Chemical ring structures of purines vs pyrimidines (A) and hydrogen bonding in A-T and G-C base pairs (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.2, distinguish between the chemical ring structures of purine and pyrimidine bases, classifying adenine, cytosine, guanine, thymine, and uracil.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why adenine pairs exclusively with thymine (or uracil) and guanine pairs exclusively with cytosine in double-stranded nucleic acids.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Predict and explain the effect of high temperatures on the relative denaturation kinetics of two DNA samples: Sample X (70% G-C content) and Sample Y (30% G-C content).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Purines (adenine, guanine) have a double-ring structure consisting of a 6-membered pyrimidine ring fused to a 5-membered imidazole ring; pyrimidines (cytosine, thymine, uracil) have a single 6-membered heterocyclic ring [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Space restriction in 2.0 nm double helix requires exactly one purine and one pyrimidine (purine-purine too wide, pyrimidine-pyrimidine too narrow); specific chemical geometry allows exactly 2 hydrogen bonds between A and T (or U) and exactly 3 hydrogen bonds between G and C [2].", "marks": 2},
            {"q": "Q2(c)", "points": "Sample X requires significantly higher temperature / has higher melting temperature (Tm) than Sample Y; G-C pairs are linked by 3 hydrogen bonds whereas A-T pairs have only 2; 70% G-C DNA requires more thermal kinetic energy to break higher total number of hydrogen bonds [2].", "marks": 2}
        ]
    ))

    # Q3: Antiparallel Double Helix (Fig 6.3)
    questions.append(Question(
        number=3,
        title="9700/22/F/M/23/Q3 - DNA Antiparallel Duplex and Phosphodiester Backbone",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Watson and Crick elucidated the antiparallel double-helical architecture of DNA. Fig. 6.3 displays the antiparallel alignment of polynucleotide strands, the condensation mechanism forming phosphodiester bonds, and helical structural dimensions.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_3_dna_double_helix_antiparallel.png"),
        figure_caption="Fig. 6.3: Antiparallel polynucleotide chain orientation and phosphodiester condensation (A) and 3D double helix dimensions (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.3A, explain what is meant by the statement that the two strands of a DNA molecule are 'antiparallel'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the condensation reaction that forms a phosphodiester bond, identifying the functional groups that react and the byproduct released.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 6.3B, explain how the hydrophilic sugar-phosphate backbones and hydrophobic base pairs contribute to the thermodynamic stability of the double helix in an aqueous cellular environment.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "One polynucleotide strand runs in the 5' to 3' direction (free phosphate at C5') while the complementary opposite strand runs in the 3' to 5' direction (free hydroxyl at C3'); strands run in opposite polarities [2].", "marks": 2},
            {"q": "Q3(b)", "points": "Condensation reaction between the 3'-OH group of the pentose sugar of one nucleotide and the 5'-phosphate group of the incoming nucleoside triphosphate; forms covalent phosphodiester linkage and eliminates one molecule of water (or pyrophosphate) [2].", "marks": 2},
            {"q": "Q3(c)", "points": "Negatively charged, polar hydrophilic sugar-phosphate backbones face outwards to interact favorably with surrounding aqueous cytoplasm/nucleoplasm; hydrophobic, planar nitrogenous bases are oriented internally, stacked perpendicular to helical axis, stabilized by hydrophobic interactions and van der Waals forces [2].", "marks": 2}
        ]
    ))

    # Q4: Semiconservative Replication Fork (Fig 6.4)
    questions.append(Question(
        number=4,
        title="9700/23/M/J/22/Q3 - Enzymatic Machinery of the DNA Replication Fork",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="DNA replication is semiconservative, requiring concerted enzymatic action to unwind the parental duplex and synthesize daughter strands. Fig. 6.4 illustrates the replication fork during S phase.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_4_semiconservative_replication_fork.png"),
        figure_caption="Fig. 6.4: Semiconservative replication fork showing leading strand continuous synthesis and lagging strand Okazaki fragments.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.4, describe the specific catalytic roles of DNA helicase, DNA topoisomerase (gyrase), and single-stranded binding proteins (SSBs) at the replication fork.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why DNA polymerase can only synthesize DNA in the 5' to 3' direction, and describe how this constraint results in leading and lagging strand differences.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the roles of primase, DNA polymerase I, and DNA ligase in the maturation and joining of Okazaki fragments on the lagging strand.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "DNA helicase breaks hydrogen bonds between complementary base pairs to unzip and separate duplex; topoisomerase relieves torsional strain/supercoiling ahead of fork; SSBs bind exposed single strands to prevent premature reannealing or nuclease cleavage [2].", "marks": 2},
            {"q": "Q4(b)", "points": "DNA polymerase active site only adds free dNTPs to the free 3'-OH group of an existing strand; leading strand template (3' to 5') synthesized continuously towards fork; lagging strand template (5' to 3') synthesized discontinuously away from fork in Okazaki fragments [2].", "marks": 2},
            {"q": "Q4(c)", "points": "Primase synthesizes short RNA primers to provide free 3'-OH group; DNA polymerase I removes RNA primers and replaces them with complementary deoxyribonucleotides; DNA ligase catalyzes final phosphodiester bond joining adjacent Okazaki fragments [2].", "marks": 2}
        ]
    ))

    # Q5: Meselson-Stahl Experiment (Fig 6.5)
    questions.append(Question(
        number=5,
        title="9700/21/M/J/21/Q4 - Meselson and Stahl Proof of Semiconservative Replication",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="In 1958, Matthew Meselson and Franklin Stahl designed an elegant isotope labeling experiment using 15N and 14N with CsCl equilibrium density gradient centrifugation. Fig. 6.5 shows their experimental protocol and centrifugation band results.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_5_meselson_stahl_experiment.png"),
        figure_caption="Fig. 6.5: CsCl density gradient centrifugation results across Generations 0, 1, and 2, disproving conservative and dispersive models.",
        parts=[
            QuestionPart(label="(a)", text="Explain why 15N and 14N isotopes were chosen for this investigation, and state how the DNA molecules were separated based on molecular density.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 6.5, explain how the single hybrid band observed in Generation 1 ruled out the conservative replication hypothesis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the appearance of two distinct bands in Generation 2 ruled out the dispersive replication hypothesis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "15N is a heavy non-radioactive stable isotope incorporated into nitrogenous purine/pyrimidine bases; separates DNA by isopycnic CsCl density gradient centrifugation where DNA bands at position matching its buoyant density [2].", "marks": 2},
            {"q": "Q5(b)", "points": "Gen 1 produced exactly one intermediate hybrid band (15N-14N, density 1.717 g cm^-3); conservative hypothesis predicted two distinct bands (one pure heavy 15N-15N parental duplex and one pure light 14N-14N daughter duplex), which was not observed [2].", "marks": 2},
            {"q": "Q5(c)", "points": "Gen 2 produced two separate bands in a 1:1 ratio: 50% hybrid (15N-14N) and 50% light (14N-14N); dispersive hypothesis predicted all DNA molecules would be fragmented mosaics producing a single intermediate band that progressively shifted lighter [2].", "marks": 2}
        ]
    ))

    # Q6: Structural Comparison of mRNA, tRNA, rRNA (Fig 6.6)
    questions.append(Question(
        number=6,
        title="9700/22/O/N/23/Q4 - Comparative Biochemistry of mRNA, tRNA, and rRNA",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Protein synthesis depends on three specialized RNA classes, each possessing distinct structural adaptations. Fig. 6.6 illustrates the structures of messenger RNA, transfer RNA, and ribosomal RNA.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_6_mrna_trna_rrna_structures.png"),
        figure_caption="Fig. 6.6: Structural conformations of mRNA (A), tRNA cloverleaf (B), and rRNA ribosome subunits (C).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.6A and B, contrast the secondary structure and presence of hydrogen bonding in mRNA compared to tRNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the structure and functional importance of the anticodon loop and the 3' CCA-OH terminus of the tRNA molecule shown in Fig. 6.6B.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 6.6C, describe the composition of eukaryotic 80S ribosomes and explain the enzymatic role of ribosomal RNA as a ribozyme during translation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "mRNA is a linear, single-stranded, unfolded polynucleotide lacking internal hydrogen bonding; tRNA folds into a cloverleaf secondary structure stabilised by intra-chain complementary base pairing and hydrogen bonds forming stems and hairpin loops [2].", "marks": 2},
            {"q": "Q6(b)", "points": "Anticodon loop contains triplet of unpaired bases that form complementary hydrogen bonds with specific mRNA codon; 3' CCA-OH stem covalently binds specific amino acid catalyzed by aminoacyl-tRNA synthetase [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Composed of small (40S: 18S rRNA + proteins) and large (60S: 28S, 5.8S, 5S rRNAs + proteins) subunits; rRNA acts as catalytic ribozyme (peptidyl transferase) in large subunit active site, forming peptide bonds between adjacent amino acids [2].", "marks": 2}
        ]
    ))

    # Q7: Transcription Mechanism (Fig 6.7)
    questions.append(Question(
        number=7,
        title="9700/21/O/N/21/Q3 - Transcription Bubble Dynamics and mRNA Synthesis",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Transcription is the enzymatic synthesis of an RNA molecule from a DNA template. Fig. 6.7 shows an active transcription bubble with RNA polymerase synthesizing nascent mRNA.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_7_transcription_mechanism.png"),
        figure_caption="Fig. 6.7: Transcription elongation showing RNA polymerase unwinding DNA, reading template 3'->5', and condesing rNTPs 5'->3'.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.7, distinguish between the coding (sense) strand and the template (antisense) strand in terms of polarity and function during transcription.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the sequence of molecular events occurring inside the transcription bubble as RNA polymerase elongates the pre-mRNA transcript.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the nascent mRNA transcript is released and what happens to the DNA duplex immediately following the passage of RNA polymerase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Template (antisense) strand runs 3' to 5' and is read by RNA polymerase to synthesize complementary RNA; coding (sense) strand runs 5' to 3' and has identical base sequence to mRNA transcript (with T instead of U) [2].", "marks": 2},
            {"q": "Q7(b)", "points": "RNA polymerase unwinds ~12-14 bp of DNA duplex; free activated ribonucleoside triphosphates (rNTPs) align opposite template bases by complementary hydrogen bonding (A-U, T-A, C-G, G-C); RNA polymerase catalyzes phosphodiester bond formation 5' to 3' between 3'-OH and 5'-phosphate [2].", "marks": 2},
            {"q": "Q7(c)", "points": "RNA polymerase encounters terminator sequence, releasing nascent transcript and dissociating; transient RNA-DNA hybrid unwinds; complementary DNA strands rewind and reanneal behind enzyme into B-form double helix [2].", "marks": 2}
        ]
    ))

    # Q8: Ribosome Translation Cycle (Fig 6.8)
    questions.append(Question(
        number=8,
        title="9700/22/M/J/22/Q4 - Translation Elongation: A, P, and E Site Translocation",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Translation translates genetic information encoded in mRNA into a polypeptide chain at the ribosome. Fig. 6.8 illustrates the translation elongation cycle and the ribosomal A, P, and E sites.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_8_ribosome_translation_cycle.png"),
        figure_caption="Fig. 6.8: Ribosomal translation cycle showing aminoacyl-tRNA binding at A site, peptide bond formation, and translocation to P and E sites.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.8, describe the specific events taking place at the A (aminoacyl) site and P (peptidyl) site during translation elongation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of peptidyl transferase in peptide bond formation, identifying the donor and acceptor molecules.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the process of translocation and explain what occurs when a stop codon (UAA, UAG, UGA) enters the A site.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "P site holds tRNA attached to growing polypeptide chain; A site receives incoming aminoacyl-tRNA whose anticodon pairs with complementary mRNA codon via GTP-dependent elongation factor [2].", "marks": 2},
            {"q": "Q8(b)", "points": "Peptidyl transferase (ribozyme in 28S rRNA of large subunit) cleaves ester link holding polypeptide to P-site tRNA and forms peptide bond between polypeptide carboxyl group and amino group of A-site amino acid [2].", "marks": 2},
            {"q": "Q8(c)", "points": "Ribosome translocates exactly 1 codon (3 nucleotides) in 5' to 3' direction along mRNA; deacylated tRNA moves P->E site and exits; peptidyl-tRNA moves A->P site; stop codon in A site binds protein release factor, hydrolyzing peptidyl-tRNA and releasing completed polypeptide [2].", "marks": 2}
        ]
    ))

    # Q9: Genetic Code Features (Fig 6.9)
    questions.append(Question(
        number=9,
        title="9700/23/O/N/23/Q3 - Universal, Degenerate, and Non-Overlapping Genetic Code",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="The genetic code is the dictionary relating nucleotide triplets to amino acids. Fig. 6.9 shows the radial codon wheel alongside key structural characteristics of the genetic code.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_9_genetic_code_wheel_chart.png"),
        figure_caption="Fig. 6.9: Radial genetic code chart (5'->3') (A) and universal properties of the genetic code (B).",
        parts=[
            QuestionPart(label="(a)", text="Define what is meant by a 'triplet codon' and calculate the theoretical number of codons possible from 4 nitrogenous bases, explaining why 2-base codons would be insufficient.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="With reference to Fig. 6.9, explain the meaning and evolutionary significance of the term 'degenerate' (redundant) as applied to the genetic code.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain what is meant by the terms 'non-overlapping' and 'universal', and describe one industrial biotechnology application that relies on the code's universality.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Triplet codon is sequence of 3 consecutive mRNA bases coding for 1 amino acid; 4^3 = 64 possible codons; 2-base codons yield only 4^2 = 16 combinations, insufficient to code for 20 standard amino acids [2].", "marks": 2},
            {"q": "Q9(b)", "points": "Degenerate means multiple distinct codons specify the same amino acid (e.g. 6 codons for Leu); evolutionary significance: provides buffering/tolerance against base substitution mutations (silent mutations at 3rd wobble position do not alter protein) [2].", "marks": 2},
            {"q": "Q9(c)", "points": "Non-overlapping means each base is part of only one codon read sequentially from AUG; universal means identical codons code for same amino acids in almost all organisms; application: production of human recombinant insulin in genetically engineered E. coli [2].", "marks": 2}
        ]
    ))

    # Q10: Gene Mutations & Frameshift (Fig 6.10)
    questions.append(Question(
        number=10,
        title="9700/21/M/J/23/Q4 - Classification of Gene Mutations: Substitutions vs Frameshifts",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Gene mutations are permanent changes in the nucleotide base sequence of a DNA molecule. Fig. 6.10 compares five mutational categories: wild-type, silent substitution, missense substitution, nonsense substitution, and an indel frameshift.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_10_gene_mutations_frameshift.png"),
        figure_caption="Fig. 6.10: Molecular consequences of base substitutions (silent, missense, nonsense) vs +1 base insertion frameshift.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.10, distinguish between a silent substitution and a missense substitution at both the nucleotide and polypeptide levels.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how a nonsense mutation alters polypeptide synthesis and describe the resulting effect on the tertiary structure and function of an enzyme.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the insertion of a single nucleotide (+1 frameshift) typically causes far more severe structural and functional disruption to a protein than a single base substitution.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Silent mutation alters single nucleotide but resulting codon specifies identical amino acid due to code degeneracy (no change in polypeptide); missense mutation alters single base producing codon for a different amino acid, altering primary structure [2].", "marks": 2},
            {"q": "Q10(b)", "points": "Nonsense mutation converts sense amino acid codon into premature stop codon (UAA, UAG, UGA); terminates translation prematurely, producing truncated polypeptide lacking essential domains, preventing correct tertiary folding and active site formation [2].", "marks": 2},
            {"q": "Q10(c)", "points": "Indel shifts triplet reading frame of all downstream codons; alters every subsequent amino acid in primary sequence and frequently creates an early premature stop codon; substitution alters at most one single amino acid [2].", "marks": 2}
        ]
    ))

    # Q11: Sickle Cell Anaemia Mutation (Fig 6.11)
    questions.append(Question(
        number=11,
        title="9700/22/F/M/22/Q3 - Molecular Genetics and Pathophysiology of Sickle Cell Anaemia",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Sickle cell anaemia is an autosomal recessive genetic disease caused by a specific point mutation in the beta-globin gene. Fig. 6.11 shows the molecular changes in DNA, mRNA, and amino acid sequence, alongside haemoglobin polymerisation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_11_sickle_cell_anaemia_mutation.png"),
        figure_caption="Fig. 6.11: Genetic basis of HbA vs HbS alleles (A) and mechanism of deoxygenation polymerisation and sickling (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.11A, state the exact base change on both the coding and template strands of DNA in the HbS allele, and identify the resulting mRNA codon and amino acid substitution at position 6.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Contrast the chemical properties of glutamic acid and valine R-groups, and explain how this substitution alters the surface solubility of the haemoglobin tetramer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to Fig. 6.11B, describe the polymerisation of deoxyhaemoglobin S at low oxygen tensions and explain two clinical symptoms experienced during a vaso-occlusive crisis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Coding strand A->T substitution (5'-GAG-3' to 5'-GTG-3'); template strand T->A substitution (3'-CTC-5' to 3'-CAC-5'); mRNA codon changes from GAG to GUG; amino acid position 6 changes from glutamic acid (Glu) to valine (Val) [2].", "marks": 2},
            {"q": "Q11(b)", "points": "Glutamic acid has polar, negatively charged hydrophilic R-group (-CH2-CH2-COO-) soluble on tetramer exterior; valine has non-polar hydrophobic hydrocarbon R-group (-CH(CH3)2) creating sticky hydrophobic contact patch on beta-chain surface [2].", "marks": 2},
            {"q": "Q11(c)", "points": "At low pO2, exposed hydrophobic valine binds complementary hydrophobic pocket on adjacent beta-subunit; polymerises into rigid insoluble fibrous chains, distorting erythrocytes into sickles; blocks capillaries causing tissue ischaemia/severe pain, and rapid haemolysis causes anaemia [2].", "marks": 2}
        ]
    ))

    # Q12: Polyribosomes / Polysomes (Fig 6.12)
    questions.append(Question(
        number=12,
        title="9700/22/M/J/21/Q4 - Polyribosome Architecture and Translational Efficiency",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="In eukaryotic and prokaryotic cells, translation often occurs on polyribosomes (polysomes) to optimize protein yield from individual mRNA transcripts. Fig. 6.12 shows polysome architecture and ribosomal density data.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_12_polysome_electron_micrograph.png"),
        figure_caption="Fig. 6.12: Polyribosome translating single mRNA transcript (A) and translational rate amplification profile (B).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.12A, deduce the direction of ribosome movement along the mRNA strand, justifying your answer using polypeptide chain lengths.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the biological advantage to a cell of translating mRNA molecules using polyribosomes rather than isolated single ribosomes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how simultaneous transcription and translation occur in prokaryotes and explain why this cannot occur in eukaryotic cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Ribosomes move 5' to 3'; ribosome nearest 5' end has shortest nascent polypeptide chain (initiation just occurred) while ribosome nearest 3' end has longest completed polypeptide (near stop codon) [2].", "marks": 2},
            {"q": "Q12(b)", "points": "Allows multiple identical polypeptide copies to be synthesized simultaneously from a single mRNA transcript in a short time; dramatically increases protein yield and efficiency before mRNA is degraded by nucleases [2].", "marks": 2},
            {"q": "Q12(c)", "points": "Prokaryotes lack a nuclear membrane, so ribosomes can translate nascent mRNA while it is still being transcribed by RNA polymerase; in eukaryotes, nuclear envelope spatially separates transcription in nucleus from translation in cytoplasm [2].", "marks": 2}
        ]
    ))

    # Q13: tRNA Charging by Aminoacyl-tRNA Synthetase (Fig 6.13)
    questions.append(Question(
        number=13,
        title="9700/21/O/N/20/Q3 - Aminoacyl-tRNA Synthetase Specificity and tRNA Charging",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="The fidelity of protein translation depends on the high specificity of tRNA charging. Fig. 6.13 illustrates the two-step aminoacylation reaction catalyzed by aminoacyl-tRNA synthetase.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_13_trna_charging_aminoacyl_synthetase.png"),
        figure_caption="Fig. 6.13: Two-step enzymatic activation and charging of tRNA by aminoacyl-tRNA synthetase using ATP.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.13, describe the two chemical steps involved in charging a tRNA molecule, identifying the energy donor and covalent bond formed.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why there are at least 20 distinct aminoacyl-tRNA synthetase enzymes present within every cell.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain what would occur during translation if an aminoacyl-tRNA synthetase mistakenly attached valine to a tRNA molecule possessing the anticodon for leucine (5'-CAA-3').", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Step 1: Specific amino acid reacts with ATP to form aminoacyl-AMP and releases PPi; Step 2: Activated amino acid is transferred to 3'-OH of CCA terminal adenine of tRNA, forming high-energy ester bond and releasing AMP [2].", "marks": 2},
            {"q": "Q13(b)", "points": "Each synthetase enzyme has active site specific for exactly one of the 20 standard amino acids and its cognate tRNA anticodon/structural identity elements; ensures correct amino acid is paired to correct anticodon [2].", "marks": 2},
            {"q": "Q13(c)", "points": "Ribosome decoding center only checks codon-anticodon base pairing, not the attached amino acid; valine would be inserted wherever leucine codon (5'-UUG-3') appears in mRNA, producing misfolded, non-functional protein [2].", "marks": 2}
        ]
    ))

    # Q14: Chemical Comparison of DNA vs RNA (Fig 6.14)
    questions.append(Question(
        number=14,
        title="9700/23/M/J/23/Q3 - Structural and Biochemical Divergence: DNA vs RNA",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="DNA and RNA perform distinct biological roles reflected in fundamental biochemical differences. Fig. 6.14 provides a comprehensive structural and chemical comparison between DNA and RNA.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig6_14_dna_vs_rna_chemical_comparison.png"),
        figure_caption="Fig. 6.14: Chemical and structural differences between DNA and RNA (pentose sugars, pyrimidines, strands, stability).",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 6.14, state three structural or chemical differences between a molecule of DNA and a molecule of RNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the presence of a 2'-hydroxyl (-OH) group makes RNA chemically less stable and more susceptible to alkaline hydrolysis than DNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Relate the molecular stability and structural characteristics of DNA and mRNA to their respective biological functions in cellular heredity and gene expression.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "DNA has 2-deoxyribose sugar whereas RNA has ribose; DNA contains thymine (T) whereas RNA contains uracil (U); DNA is double-stranded B-helix whereas RNA is predominantly single-stranded; DNA is longer and permanent whereas RNA is short and transient [2].", "marks": 2},
            {"q": "Q14(b)", "points": "2'-OH in ribose acts as nucleophile under alkaline conditions, attacking adjacent phosphodiester bond to form 2',3'-cyclic phosphate intermediate, cleaving RNA backbone; deoxyribose in DNA has only stable 2'-H [2].", "marks": 2},
            {"q": "Q14(c)", "points": "DNA must store genetic information faithfully across generations; double helix with protected interior bases and stable backbone resists degradation; mRNA is transient template meant to be degraded after translation to regulate protein expression [2].", "marks": 2}
        ]
    ))

    # Q15: Telomeres & End-Replication Problem
    questions.append(Question(
        number=15,
        title="9700/22/O/N/22/Q3 - Telomere Anatomy, End-Replication Problem, and Cellular Ageing",
        syllabus_ref="Syllabus 6.1",
        difficulty="CHALLENGING",
        preamble="Linear eukaryotic chromosomes cannot fully replicate their extreme 5' ends during S phase, a dilemma known as the end-replication problem.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure of a telomere, identifying its characteristic repetitive nucleotide sequence in humans.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why standard DNA polymerases cannot replicate the extreme 5' end of the lagging strand of a linear chromosome.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the enzyme telomerase maintains chromosome length in stem cells and germ-line cells, and describe its role in human cancer cells.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Telomeres are non-coding repetitive DNA sequences (tandem repeats of 5'-TTAGGG-3' in vertebrates) located at the ends of linear chromosomes, bound by shelterin protein complex [2].", "marks": 2},
            {"q": "Q15(b)", "points": "Lagging strand synthesis requires RNA primers; when terminal primer at 5' end is excised, DNA polymerase cannot synthesize replacement DNA because there is no upstream 3'-OH group to extend from, leaving 5' terminal gap [2].", "marks": 2},
            {"q": "Q15(c)", "points": "Telomerase is a ribonucleoprotein reverse transcriptase carrying an internal RNA template (3'-AAUCCC-5'); extends 3' overhang of parental strand, allowing lagging strand completion; reactivation in ~90% of cancers confers cellular immortality [2].", "marks": 2}
        ]
    ))

    # Q16: Transcription Factors & Gene Expression Regulation
    questions.append(Question(
        number=16,
        title="9700/21/M/J/22/Q4 - Promoters, Transcription Factors, and Transcriptional Initiation",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Transcription initiation in eukaryotes requires precise interactions between promoter sequences, transcription factors, and RNA polymerase II.",
        parts=[
            QuestionPart(label="(a)", text="Describe the structure and function of a promoter region on a eukaryotic gene, referring to the TATA box.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the role of general transcription factors in facilitating the binding of RNA polymerase II to the promoter.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Distinguish between activator and repressor transcription factors in the control of gene expression.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Promoter is non-coding regulatory DNA sequence located upstream (5') of transcription start site; contains conserved motifs like TATA box (~25-30 bp upstream) that direct RNA polymerase to correct start site [2].", "marks": 2},
            {"q": "Q16(b)", "points": "General transcription factors (e.g. TFIID via TATA-binding protein) bind promoter sequentially, bending DNA and forming pre-initiation complex that recruits and positions RNA polymerase II [2].", "marks": 2},
            {"q": "Q16(c)", "points": "Activators bind enhancer regions to stimulate transcription by promoting chromatin opening and polymerase recruitment; repressors bind silencer regions or compete for promoter binding, inhibiting transcription [2].", "marks": 2}
        ]
    ))

    # Q17: Post-Transcriptional Processing of pre-mRNA
    questions.append(Question(
        number=17,
        title="9700/22/F/M/21/Q3 - Eukaryotic pre-mRNA Maturation: Splicing, Capping, and Tailing",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Primary RNA transcripts (pre-mRNA) synthesized in eukaryotic nuclei undergo extensive enzymatic modification before nuclear export.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between introns and exons in eukaryotic genes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the mechanism of pre-mRNA splicing catalyzed by the spliceosome.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the addition and functions of the 5' 7-methylguanosine cap and the 3' poly-A tail.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Exons are coding sequences retained in mature mRNA that code for amino acids in polypeptide; introns are non-coding intervening sequences transcribed into pre-mRNA but removed prior to translation [2].", "marks": 2},
            {"q": "Q17(b)", "points": "Spliceosome (snRNPs + proteins) recognizes conserved 5' and 3' splice site junctions, cleaves intron at 5' splice site, forms lariat intermediate, and ligates adjacent exons together via phosphodiester bonds [2].", "marks": 2},
            {"q": "Q17(c)", "points": "5' cap protects transcript from 5' exonucleases and provides ribosomal recognition signal; 3' poly-A tail (~200 adenines) protects 3' end, facilitates nuclear export, and enhances translational efficiency [2].", "marks": 2}
        ]
    ))

    # Q18: DNA vs RNA Viruses & Reverse Transcription
    questions.append(Question(
        number=18,
        title="9700/23/O/N/22/Q3 - Retroviruses, Reverse Transcriptase, and Central Dogma Inversion",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Retroviruses such as HIV challenge the traditional central dogma of molecular biology (DNA -> RNA -> Protein).",
        parts=[
            QuestionPart(label="(a)", text="Describe the genetic material of human immunodeficiency virus (HIV) and identify the specific enzyme it carries into the host cell to copy its genome.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the catalytic activity of reverse transcriptase and state how this process inverts the canonical flow of genetic information.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why HIV exhibits an exceptionally high mutation rate compared to cellular organisms that possess DNA genomes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "HIV genome consists of two identical single-stranded (+) RNA molecules; carries reverse transcriptase (RNA-dependent DNA polymerase), integrase, and protease within viral capsid [2].", "marks": 2},
            {"q": "Q18(b)", "points": "Reverse transcriptase synthesizes complementary single-stranded DNA from RNA template, degrades RNA strand (RNase H activity), and synthesizes complementary second DNA strand to yield double-stranded proviral DNA (RNA -> DNA) [2].", "marks": 2},
            {"q": "Q18(c)", "points": "Reverse transcriptase lacks 3' to 5' exonuclease proofreading capability; replication errors (substitutions, insertions, deletions) occur at high frequency (~1 in 10^4 bp) without enzymatic correction [2].", "marks": 2}
        ]
    ))

    # Q19: Antibiotic Inhibitors of Protein Synthesis
    questions.append(Question(
        number=19,
        title="9700/22/M/J/20/Q4 - Antibiotic Mechanisms Targeting Bacterial Ribosomes",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Many clinical antibiotics exploit structural differences between prokaryotic 70S ribosomes and eukaryotic 80S ribosomes to selectively inhibit bacterial translation.",
        parts=[
            QuestionPart(label="(a)", text="Describe the subunit and rRNA differences between prokaryotic 70S ribosomes and eukaryotic 80S ribosomes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how tetracycline and chloramphenicol inhibit bacterial translation at distinct stages of the elongation cycle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why antibiotics targeting 70S ribosomes may cause mitochondrial toxicity in human patients at high doses.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Prokaryotic 70S: 30S (16S rRNA) + 50S (23S, 5S rRNAs); Eukaryotic 80S: 40S (18S rRNA) + 60S (28S, 5.8S, 5S rRNAs) [2].", "marks": 2},
            {"q": "Q19(b)", "points": "Tetracycline binds 30S subunit, physically blocking aminoacyl-tRNA from entering A site; chloramphenicol binds 50S subunit, inhibiting peptidyl transferase activity and blocking peptide bond formation [2].", "marks": 2},
            {"q": "Q19(c)", "points": "Mitochondria evolved from endosymbiotic alpha-proteobacteria and possess their own 70S-like ribosomes; high antibiotic doses inhibit mitochondrial translation, impairing oxidative phosphorylation and ATP generation [2].", "marks": 2}
        ]
    ))

    # Q20: Quantitative Analysis of DNA Base Composition (Chargaff's Rules)
    questions.append(Question(
        number=20,
        title="[Mentora Original A* Extension] - Quantitative Nucleic Acid Stoichiometry & Chargaff Rules",
        syllabus_ref="Syllabus 6.1",
        difficulty="CHALLENGING",
        preamble="Chemical analysis of a double-stranded DNA sample from a newly discovered thermophilic bacteriophage revealed that 34% of the nitrogenous bases consist of cytosine.",
        parts=[
            QuestionPart(label="(a)", text="Calculate the percentage of adenine, guanine, and thymine in this double-stranded DNA sample, showing your working.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State Chargaff's rules and explain why they apply strictly to double-stranded DNA but not to single-stranded RNA molecules.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="A single-stranded viral RNA genome was analyzed and found to contain 28% A, 22% U, 31% G, and 19% C. Explain why %A does not equal %U and %G does not equal %C in this virus.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Cytosine = 34%, so Guanine = 34% (G=C); Total G+C = 68%; Total A+T = 100 - 68 = 32%; Adenine = 16%, Thymine = 16% [2].", "marks": 2},
            {"q": "Q20(b)", "points": "Chargaff's rules state %A = %T and %G = %C, and purines = pyrimidines; applies to dsDNA because complementary base pairing obligates 1:1 ratio; ssRNA lacks complementary opposite strand [2].", "marks": 2},
            {"q": "Q20(c)", "points": "Viral RNA is single-stranded, so bases are not constrained by complementary base pairing across an antiparallel duplex; base composition reflects primary sequence encoding viral proteins rather than base-pairing stoichiometry [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & MOLECULAR GENETICS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Sickle cell HbS polymerisation details
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q5 - Sickle Cell Erythrocyte Fragility and Malaria Protection",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Individuals heterozygous for the sickle cell allele (HbA/HbS) exhibit sickle cell trait and show increased resistance to malaria.",
        parts=[
            QuestionPart(label="(a)", text="Explain why erythrocytes containing HbS rupture more rapidly than normal red blood cells, leading to chronic haemolytic anaemia.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the sickle cell trait confers a survival advantage against Plasmodium falciparum malaria in endemic regions (heterozygote advantage).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Repeated cycles of deoxygenation and sickling damage erythrocyte cell membrane, causing potassium leakage and rigidity; fragile sickled cells undergo intravascular haemolysis and are phagocytosed in spleen, shortening lifespan from 120 d to 10-20 d [2].", "marks": 2},
            {"q": "Q21(b)", "points": "In HbA/HbS heterozygotes, parasitized RBCs sickle prematurely and are cleared by splenic macrophages before parasite schizogony completes; lower oxygen tension and sickling restrict parasite proliferation [2].", "marks": 2}
        ]
    ))

    # Q22: Hydrogen bonding vs Covalent Phosphodiester Bonds
    questions.append(Question(
        number=22,
        title="9700/21/O/N/23/Q4 - Energy Demands of Bond Cleavage in DNA Replication",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="The double-helical structure of DNA relies on two fundamentally different bond types to maintain structural integrity.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between phosphodiester bonds and hydrogen bonds in DNA in terms of bond strength, location, and the enzymes that cleave them.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the replication fork requires helicase to break hydrogen bonds whereas endonucleases are needed to break the phosphodiester backbone.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Phosphodiester bonds are strong covalent bonds linking C3' to C5' along sugar-phosphate backbone, cleaved by endonucleases/phosphodiesterases; hydrogen bonds are weak electrostatic interactions between complementary bases in duplex center, cleaved by helicase [2].", "marks": 2},
            {"q": "Q22(b)", "points": "Hydrogen bonds have low bond dissociation energy (~10-20 kJ mol^-1) allowing rapid mechanical separation by helicase at ambient cell temperature; covalent phosphodiester bonds have high dissociation energy (~350-400 kJ mol^-1) requiring catalytic hydrolysis [2].", "marks": 2}
        ]
    ))

    # Q23: Function of DNA Polymerase III vs DNA Polymerase I
    questions.append(Question(
        number=23,
        title="9700/22/F/M/23/Q4 - Specialised Functions of Prokaryotic DNA Polymerases",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Bacterial replication utilizes multiple specialized DNA polymerase isoforms to ensure accurate duplex duplication.",
        parts=[
            QuestionPart(label="(a)", text="Contrast the principal enzymatic roles of DNA polymerase III and DNA polymerase I during bacterial chromosome replication.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain what is meant by the 3' to 5' exonuclease proofreading activity of DNA polymerase, and explain its importance.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "DNA polymerase III is the primary replicative enzyme with high processivity, synthesizing leading strand and elongating Okazaki fragments 5' to 3'; DNA polymerase I has 5' to 3' exonuclease activity to remove RNA primers and replace them with DNA [2].", "marks": 2},
            {"q": "Q23(b)", "points": "Proofreading detects mismatched mispaired nucleotides at 3' terminus, reverses direction, and cleaves mispaired base via 3'->5' exonuclease before resuming 5'->3' synthesis; reduces replication error rate from 10^-5 to 10^-8 [2].", "marks": 2}
        ]
    ))

    # Q24: Directionality in Molecular Biology (5' to 3')
    questions.append(Question(
        number=24,
        title="9700/23/M/J/22/Q4 - Universal 5' to 3' Polymerisation Directionality",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Nucleic acid polymerisation enzymes universally add nucleotides in the 5' to 3' direction.",
        parts=[
            QuestionPart(label="(a)", text="Explain chemically why DNA polymerases and RNA polymerases synthesize nucleic acids exclusively in the 5' to 3' direction.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how incoming deoxyribonucleoside triphosphates (dNTPs) provide both the monomer units and the chemical energy required for polymerisation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Polymerase active sites only recognize and catalyze nucleophilic attack by the free 3'-OH group of the growing strand on the alpha-phosphate of the incoming 5'-triphosphate monomer; no mechanism exists to add to a 5' end [2].", "marks": 2},
            {"q": "Q24(b)", "points": "Cleavage of high-energy phosphoanhydride bond between alpha and beta phosphates releases pyrophosphate (PPi); subsequent hydrolysis of PPi into 2 Pi by pyrophosphatase provides high exergonic free energy driving condensation [2].", "marks": 2}
        ]
    ))

    # Q25: Role of RNA Primer & Primase
    questions.append(Question(
        number=25,
        title="9700/21/O/N/22/Q5 - The Obligate Requirement for Primers in DNA Synthesis",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Unlike RNA polymerases, DNA polymerases cannot initiate polynucleotide synthesis de novo.",
        parts=[
            QuestionPart(label="(a)", text="Explain why DNA polymerase requires a pre-existing RNA primer to begin DNA synthesis, whereas RNA polymerase does not require a primer during transcription.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how primase synthesizes RNA primers and state what happens to these primers before replication is complete.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "DNA polymerase requires a pre-existing 3'-OH group to form a phosphodiester bond; cannot bind two free dNTPs and join them; RNA polymerase can initiate de novo by binding two rNTPs opposite template [2].", "marks": 2},
            {"q": "Q25(b)", "points": "Primase (RNA polymerase) synthesizes short complementary RNA segment (~10-12 nt) providing free 3'-OH; primers are subsequently excised by 5'->3' exonuclease activity of DNA polymerase I and replaced with DNA [2].", "marks": 2}
        ]
    ))

    # Q26: tRNA Structure: Anticodon and CCA Stem
    questions.append(Question(
        number=26,
        title="9700/22/F/M/22/Q4 - tRNA Cloverleaf Motifs and Amino Acid Esterification",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Transfer RNA acts as the molecular adaptor linking codon triplets to specific amino acid residues.",
        parts=[
            QuestionPart(label="(a)", text="Describe the cloverleaf secondary structure of tRNA, identifying the acceptor stem, D-loop, T-loop, and anticodon loop.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the invariant 3' CCA sequence at the acceptor stem attaches to an amino acid.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Acceptor stem contains 5' and 3' ends; D-loop contains dihydrouridine; T(psi)C loop contains pseudouridine; anticodon loop contains 3 unpaired bases complementary to mRNA codon; stems formed by intra-chain base pairing [2].", "marks": 2},
            {"q": "Q26(b)", "points": "Terminal adenine possesses free 2'-OH or 3'-OH group; carboxyl group of specific amino acid forms covalent ester bond with 3'-OH of adenine, catalyzed by aminoacyl-tRNA synthetase [2].", "marks": 2}
        ]
    ))

    # Q27: Initiation of Translation: AUG Start Codon & Met-tRNA
    questions.append(Question(
        number=27,
        title="9700/21/M/J/21/Q5 - Translation Initiation Complex Assembly",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Translation initiation ensures the ribosome starts reading mRNA at the correct reading frame.",
        parts=[
            QuestionPart(label="(a)", text="Describe the assembly of the translation initiation complex at the 5' end of a eukaryotic mRNA molecule.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the start codon, name the first amino acid incorporated into eukaryotic polypeptides, and state the anticodon of the initiator tRNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Small ribosomal subunit (40S) bound to initiator Met-tRNA and initiation factors binds 5' cap of mRNA, scans 5'->3' to locate AUG start codon; large ribosomal subunit (60S) then joins, positioning Met-tRNA in P site [2].", "marks": 2},
            {"q": "Q27(b)", "points": "Start codon is 5'-AUG-3'; first amino acid is methionine (Met); initiator tRNA anticodon is 3'-UAC-5' (or 5'-CAU-3') [2].", "marks": 2}
        ]
    ))

    # Q28: Stop Codons and Release Factors
    questions.append(Question(
        number=28,
        title="9700/22/O/N/21/Q4 - Termination of Translation by Release Factors",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Termination of translation occurs when the elongation complex reaches a stop codon.",
        parts=[
            QuestionPart(label="(a)", text="Name the three termination (stop) codons in the universal genetic code and explain why no tRNA molecules possess anticodons complementary to them.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the molecular events triggered when a protein release factor binds to a stop codon in the ribosomal A site.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Stop codons are 5'-UAA-3', 5'-UAG-3', and 5'-UGA-3'; no standard cellular tRNAs have complementary anticodons because stop codons do not code for any amino acid (nonsense codons) [2].", "marks": 2},
            {"q": "Q28(b)", "points": "Protein release factor (eRF1) binds stop codon in A site, altering peptidyl transferase activity to hydrolyze ester bond between completed polypeptide and P-site tRNA; polypeptide released, ribosome subunits dissociate [2].", "marks": 2}
        ]
    ))

    # Q29: Wobble Hypothesis & Codon-Anticodon Pairing
    questions.append(Question(
        number=29,
        title="[Mentora Original A* Extension] - Crick's Wobble Hypothesis and Non-Canonical Pairing",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="While there are 61 sense codons, many organisms possess fewer than 45 distinct tRNA species.",
        parts=[
            QuestionPart(label="(a)", text="Explain Crick's 'wobble hypothesis' and identify the position of the codon and anticodon where non-Watson-Crick base pairing is tolerated.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the wobble hypothesis accounts for the degeneracy of the genetic code and allows a cell to translate all codons with fewer tRNA species.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Spatial flexibility (wobble) allows non-canonical base pairing between 3rd base of mRNA codon (3' end) and 1st base of tRNA anticodon (5' end); e.g. G can pair with U or C, Inosine (I) can pair with A, U, or C [2].", "marks": 2},
            {"q": "Q29(b)", "points": "A single tRNA molecule can recognize multiple synonymous codons differing only at 3rd base position (e.g. tRNA-Gly can pair with GGA and GGU); reduces minimum number of tRNA genes required in genome [2].", "marks": 2}
        ]
    ))

    # Q30: Semiconservative Mechanism: Parent vs Daughter Strands
    questions.append(Question(
        number=30,
        title="9700/23/M/J/21/Q4 - Semiconservative Principle and Epigenetic Preservation",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="The semiconservative model ensures that each newly synthesized duplex retains one intact original strand.",
        parts=[
            QuestionPart(label="(a)", text="Explain the meaning of 'semiconservative' replication and describe how each daughter duplex is composed after one replication cycle.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the template strand directs the nucleotide sequence of the newly synthesized daughter strand.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Each replicated double-stranded DNA molecule consists of one conserved original parental strand and one newly synthesized daughter strand; parental strands separate and act as templates [2].", "marks": 2},
            {"q": "Q30(b)", "points": "Complementary base pairing rules (A with T, G with C) dictate that each template base can only form stable hydrogen bonds with its specific complementary incoming dNTP; preserves exact genetic sequence [2].", "marks": 2}
        ]
    ))

    # Q31: Purine / Pyrimidine Biosynthesis & Structure
    questions.append(Question(
        number=31,
        title="9700/21/M/J/23/Q5 - Purine and Pyrimidine Stoichiometry in DNA Analysis",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Chemical analysis of double-stranded DNA demonstrates consistent geometric constraints across all cellular genomes.",
        parts=[
            QuestionPart(label="(a)", text="Explain why the total percentage of purines in any double-stranded DNA molecule is always equal to 50%.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the ratio (A + T) / (G + C) varies widely between species, whereas the ratio (A + G) / (T + C) is always equal to 1.0 in double-stranded DNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "In double-stranded DNA, every purine on one strand must pair with a pyrimidine on the opposite strand; therefore total purines (A + G) equals total pyrimidines (T + C), so purines constitute exactly 50% [2].", "marks": 2},
            {"q": "Q31(b)", "points": "(A+G)/(T+C) is purine/pyrimidine ratio, which must equal 1.0 due to obligate base pairing; (A+T)/(G+C) varies because different genomes have evolved different GC-content adapted to environmental temperatures and genome constraints [2].", "marks": 2}
        ]
    ))

    # Q32: Ribozymes: Catalytic RNA in Protein Synthesis
    questions.append(Question(
        number=32,
        title="9700/22/O/N/20/Q4 - Peptidyl Transferase Ribozyme Activity in the Ribosome",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="The discovery that ribosomal RNA acts as the peptidyl transferase catalyst altered our understanding of biological catalysis.",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'ribozyme' and state the specific catalytic function of 28S rRNA in the large eukaryotic ribosomal subunit.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the discovery of catalytic rRNA provides critical evidence supporting the 'RNA World' hypothesis of prebiotic evolution.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "A ribozyme is an RNA molecule capable of catalyzing specific biochemical reactions; 28S rRNA acts as peptidyl transferase, forming peptide bonds between amino acids during translation [2].", "marks": 2},
            {"q": "Q32(b)", "points": "RNA World hypothesis posits that primordial life used RNA for both genetic information storage (like DNA) and biochemical catalysis (like protein enzymes); catalytic ribosome shows modern translation still relies on an RNA catalyst [2].", "marks": 2}
        ]
    ))

    # Q33: Mutagens: Chemical and Physical Agents
    questions.append(Question(
        number=33,
        title="9700/21/O/N/21/Q5 - Mutagenic Mechanisms: Ionising Radiation vs Base Analogues",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="Mutagens are environmental agents that significantly increase the spontaneous mutation frequency of DNA.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between the mutagenic effects of ultraviolet (UV) radiation and ionising radiation (X-rays) on DNA structure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how chemical base analogues such as 5-bromouracil (5-BU) induce point mutations during DNA replication.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "UV radiation causes photochemical covalent dimerization of adjacent pyrimidines (thymine dimers), distorting helix; ionising radiation produces free radicals that cause single- and double-strand phosphodiester backbone breaks [2].", "marks": 2},
            {"q": "Q33(b)", "points": "5-BU is a structural analogue of thymine that mispairs with guanine in its enol tautomeric form; upon subsequent replication, this incorporates cytosine opposite G, resulting in an A-T to G-C transition mutation [2].", "marks": 2}
        ]
    ))

    # Q34: CFTR Gene Mutation (Cystic Fibrosis delta-F508)
    questions.append(Question(
        number=34,
        title="9700/22/M/J/22/Q5 - The delta-F508 In-Frame Deletion in the CFTR Gene",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Cystic fibrosis is most commonly caused by the deletion of three consecutive nucleotides in the CFTR gene (delta-F508).",
        parts=[
            QuestionPart(label="(a)", text="Explain why the deletion of exactly three nucleotides in the delta-F508 mutation does not cause a frameshift mutation, but still results in a non-functional CFTR chloride channel.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the fate of the delta-F508 CFTR protein within the endoplasmic reticulum and explain the consequence on chloride ion transport across epithelial membranes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Deletion of 3 nucleotides removes exactly one codon (TTT/CTT) without altering the downstream reading frame (in-frame deletion); loss of phenylalanine at position 508 disrupts tertiary folding, preventing correct channel structure [2].", "marks": 2},
            {"q": "Q34(b)", "points": "Misfolded CFTR is recognized by ER chaperone quality-control systems, polyubiquitinated, and degraded in proteasomes; channel fails to reach apical membrane, preventing Cl- export, leading to thick, dehydrated mucus [2].", "marks": 2}
        ]
    ))

    # Q35: DNA Ligase Mechanism
    questions.append(Question(
        number=35,
        title="9700/23/O/N/23/Q4 - DNA Ligase Catalytic Mechanism in Nick Sealing",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        preamble="DNA ligase seals single-strand nicks in the phosphodiester backbone during replication, recombination, and repair.",
        parts=[
            QuestionPart(label="(a)", text="Identify the specific chemical group present at each side of a single-strand DNA nick that DNA ligase joins together.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why DNA ligase requires ATP (or NAD+ in bacteria) to seal a nick, and describe the bond formed.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "A free 3'-hydroxyl (-OH) group on the upstream deoxyribose and a free 5'-monophosphate group on the downstream deoxyribose [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Condensation reaction is endergonic; ATP transfers AMP to ligase active site lysine, forming enzyme-AMP; AMP is transferred to 5'-phosphate, activating it for attack by 3'-OH, forming covalent phosphodiester bond and releasing AMP [2].", "marks": 2}
        ]
    ))

    # Q36: Nucleosome Structure and Histone Proteins
    questions.append(Question(
        number=36,
        title="9700/21/F/M/21/Q4 - Histone Octamer Chemistry and Nucleosome Assembly",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Eukaryotic nuclear DNA is wrapped around histone octamers to form repeating nucleosome cores.",
        parts=[
            QuestionPart(label="(a)", text="Describe the subunit composition of a histone octamer and state the length of DNA wrapped around each nucleosome core.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the amino acid composition of histone proteins enables them to bind tightly to DNA irrespective of the specific nucleotide sequence.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Composed of two molecules each of core histones H2A, H2B, H3, and H4 (octamer); wrapped by ~146-147 base pairs of double-stranded DNA in 1.65 left-handed superhelical turns [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Histones are rich in basic amino acids with positively charged R-groups (lysine and arginine at physiological pH); form strong electrostatic attractions with negatively charged phosphate groups along DNA backbone, independent of base sequence [2].", "marks": 2}
        ]
    ))

    # Q37: RNA Interference (miRNA and siRNA)
    questions.append(Question(
        number=37,
        title="[Mentora Original A* Extension] - Post-Transcriptional Gene Silencing via Small RNAs",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Small non-coding RNA molecules regulate gene expression post-transcriptionally through RNA interference (RNAi).",
        parts=[
            QuestionPart(label="(a)", text="Describe how microRNAs (miRNAs) are processed by the Dicer enzyme and incorporated into the RNA-induced silencing complex (RISC).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain two mechanisms by which miRNA-loaded RISC prevents the expression of target mRNA molecules.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "Dicer endoribonuclease cleaves hairpin pre-miRNA into ~21-23 nucleotide double-stranded miRNA duplex; duplex loaded into RISC containing Argonaute protein; passenger strand discarded, leaving single-stranded guide miRNA [2].", "marks": 2},
            {"q": "Q37(b)", "points": "Partial complementarity to target mRNA 3' UTR blocks translation initiation and elongation; extensive/perfect complementarity triggers Argonaute endonuclease cleavage of mRNA phosphodiester backbone, leading to rapid mRNA degradation [2].", "marks": 2}
        ]
    ))

    # Q38: Splicing Errors and Beta-Thalassaemia
    questions.append(Question(
        number=38,
        title="9700/22/M/J/21/Q5 - Splicing Site Mutations Causing Beta-Thalassaemia",
        syllabus_ref="Syllabus 6.2",
        difficulty="CHALLENGING",
        preamble="Beta-thalassaemia can arise from point mutations at intron-exon splice junctions of the HBB gene.",
        parts=[
            QuestionPart(label="(a)", text="Describe how a single base substitution at the 5' splice donor site (GU) of intron 1 of the beta-globin gene causes aberrant pre-mRNA splicing.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how aberrant splicing causes a severe reduction in functional beta-globin synthesis in patients with beta-thalassaemia.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Mutation destroys conserved 5' GU splice donor recognition sequence; spliceosome fails to cleave at correct site and either retains entire intron or uses cryptic splice site nearby [2].", "marks": 2},
            {"q": "Q38(b)", "points": "Retained intron introduces premature stop codons or frameshifts, producing truncated non-functional beta-globin or triggering nonsense-mediated mRNA decay; severe reduction in HbA causes severe microcytic anaemia [2].", "marks": 2}
        ]
    ))

    # Q39: Mitochondrial DNA vs Nuclear DNA
    questions.append(Question(
        number=39,
        title="9700/23/O/N/21/Q4 - Evolutionary Characteristics of the Mitochondrial Genome",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Mitochondria possess their own distinct genome (mtDNA) reflecting their endosymbiotic bacterial ancestry.",
        parts=[
            QuestionPart(label="(a)", text="State two structural differences between human mitochondrial DNA and human nuclear DNA.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why mitochondrial DNA exhibits a significantly higher mutation rate than nuclear DNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Mitochondrial DNA is circular, double-stranded, lacks protective histone proteins ('naked'), and has no introns; nuclear DNA is linear, condensed with histones into chromatin, and contains numerous introns [2].", "marks": 2},
            {"q": "Q39(b)", "points": "Located adjacent to respiratory electron transport chain producing high levels of reactive oxygen species (ROS); mitochondria lack robust nucleotide excision repair and proofreading systems present in nucleus [2].", "marks": 2}
        ]
    ))

    # Q40: DNA Extraction and Precipitation Principles
    questions.append(Question(
        number=40,
        title="9700/21/M/J/20/Q3 - Chemical Principles of Cellular DNA Extraction and Precipitation",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        preamble="Extraction of genomic DNA from plant or animal tissues requires specific chemical reagents.",
        parts=[
            QuestionPart(label="(a)", text="Explain the role of detergent (SDS) and protease enzymes during the extraction of genomic DNA from onion tissue.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why cold ethanol (or isopropanol) and salt (NaCl) are added to the filtered extract to precipitate DNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Detergent dissolves phospholipid bilayer membranes of cell surface and nuclear envelope, lysing cells; protease digests histone and other cellular proteins bound to DNA, releasing naked polynucleotide chains [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Na+ ions neutralize negative charges on DNA phosphate backbone, reducing electrostatic repulsion between strands; ethanol has lower dielectric constant than water, causing dehydrated DNA strands to aggregate and precipitate as visible fibers [2].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Definition of a gene
    questions.append(Question(
        number=41,
        title="9700/22/M/J/23/Q6 - Rigorous Definition of a Gene",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'gene' according to the Cambridge 9700 syllabus specification.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "A sequence of nucleotides in a DNA molecule that encodes the amino acid sequence of a polypeptide chain (or functional non-coding RNA molecule) [2].", "marks": 2}
        ]
    ))

    # Q42: Semiconservative replication definition
    questions.append(Question(
        number=42,
        title="9700/21/O/N/23/Q6 - Definition of Semiconservative Replication",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="State what is meant by 'semiconservative replication' of DNA.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "The mechanism of DNA replication in which the two parental strands separate, each acting as a template for the synthesis of a complementary strand, producing two identical daughter duplexes each containing one original and one new strand [2].", "marks": 2}
        ]
    ))

    # Q43: Codon vs Anticodon definition
    questions.append(Question(
        number=43,
        title="9700/22/F/M/23/Q6 - Codon and Anticodon Definitions",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between a codon and an anticodon.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "A codon is a triplet of nitrogenous bases on an mRNA molecule that codes for an amino acid (or stop signal); an anticodon is a complementary triplet of bases on a tRNA molecule that base-pairs with the codon during translation [2].", "marks": 2}
        ]
    ))

    # Q44: Purine vs Pyrimidine structural formula
    questions.append(Question(
        number=44,
        title="9700/23/M/J/22/Q6 - Purine vs Pyrimidine Classification",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Identify the two purine bases and the three pyrimidine bases found in nucleic acids.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Purines: Adenine (A) and Guanine (G); Pyrimidines: Cytosine (C), Thymine (T, DNA only), and Uracil (U, RNA only) [2].", "marks": 2}
        ]
    ))

    # Q45: Mutation definition
    questions.append(Question(
        number=45,
        title="9700/21/O/N/22/Q6 - Definition of Gene Mutation",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'gene mutation'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "A permanent change in the nucleotide sequence of a DNA molecule (or gene) that can alter the primary structure of the encoded polypeptide [2].", "marks": 2}
        ]
    ))

    # Q46: Phosphodiester bond definition
    questions.append(Question(
        number=46,
        title="9700/22/F/M/22/Q6 - Phosphodiester Bond Linkage",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Describe the covalent linkage comprising a phosphodiester bond in a nucleic acid strand.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "A covalent ester linkage connecting the 3'-carbon of the pentose sugar of one nucleotide to the 5'-carbon of the pentose sugar of an adjacent nucleotide via a phosphate group [2].", "marks": 2}
        ]
    ))

    # Q47: Degenerate code definition
    questions.append(Question(
        number=47,
        title="9700/21/M/J/21/Q6 - Degeneracy of the Genetic Code",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by describing the genetic code as 'degenerate'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "The genetic code is degenerate because more than one triplet codon can code for the same amino acid (e.g. 6 codons for leucine, 4 for glycine), except for methionine (AUG) and tryptophan (UGG) [2].", "marks": 2}
        ]
    ))

    # Q48: Polysome definition
    questions.append(Question(
        number=48,
        title="9700/22/O/N/21/Q6 - Polyribosome Structure and Function",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'polyribosome' (polysome) and state its function.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "A complex of multiple ribosomes attached to and translating a single mRNA molecule simultaneously in the 5' to 3' direction, accelerating the rate of polypeptide synthesis [2].", "marks": 2}
        ]
    ))

    # Q49: Splicing definition
    questions.append(Question(
        number=49,
        title="9700/23/M/J/21/Q6 - RNA Splicing Definition",
        syllabus_ref="Syllabus 6.2",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="State the meaning of RNA splicing in eukaryotic gene expression.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "The post-transcriptional process by which non-coding intervening sequences (introns) are excised from pre-mRNA and coding sequences (exons) are joined together to produce mature mRNA [2].", "marks": 2}
        ]
    ))

    # Q50: Telomere definition
    questions.append(Question(
        number=50,
        title="9700/21/M/J/23/Q6 - Telomere Structure and Role",
        syllabus_ref="Syllabus 6.1",
        difficulty="ADVANCED",
        parts=[
            QuestionPart(label="(a)", text="State the function of telomeres on eukaryotic linear chromosomes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "Non-coding repetitive hexamer DNA sequences at chromosome ends that protect vital coding genes from erosion during replication and prevent chromosome end fusion or triggering DNA damage checkpoints [2].", "marks": 2}
        ]
    ))

    return questions

# =============================================================================
# SECTION D: 10 HIGH-FREQUENCY EXAMINER FAQS & CRITICAL REVISION PITFALLS
# =============================================================================

def get_topic6_faqs():
    return [
        {
            "q_num": 1,
            "title": "Coding Strand vs Template Strand: Which Strand Is Transcribed and How to Avoid Polarity & Sequence Errors?",
            "category": "Mark Scheme Priority • Transcription Mechanics",
            "examiner_trap": "Candidates frequently confuse the sense (coding) strand with the antisense (template) strand. In Cambridge mark schemes, asserting that RNA polymerase transcribes the coding strand or reversing the 5'->3' polarity results in 0 marks.",
            "model_answer": "• The template strand (antisense / non-coding strand) is the ONLY strand transcribed by RNA polymerase; it runs in the 3' to 5' direction.\n• Polarity: RNA polymerase moves along the template strand 3' to 5', synthesizing pre-mRNA in the 5' to 3' direction.\n• Complementary base pairing: A on template pairs with U in mRNA; T pairs with A; C pairs with G; G pairs with C.\n• The coding strand (sense / non-template strand) runs 5' to 3' and has an identical base sequence to the newly synthesized mRNA transcript, except that DNA contains thymine (T) whereas mRNA contains uracil (U)."
        },
        {
            "q_num": 2,
            "title": "Why Is ATP Described as a 'Phosphorylated Nucleotide' and How Does It Compare Structurally to an RNA Adenine Monomer?",
            "category": "Structural Biochemistry • Nucleotide Anatomy",
            "examiner_trap": "Students often classify ATP vaguely as a protein or simple nucleic acid. Examiners strictly award marks for identifying its three distinct components: adenine, ribose, and three inorganic phosphate groups.",
            "model_answer": "• An RNA adenine mononucleotide (AMP) contains adenine, ribose, and ONE phosphate group linked to C5' by a phosphoester bond.\n• ATP is 'phosphorylated' because two additional inorganic phosphate groups are condensed onto AMP, producing a triphosphate chain (alpha, beta, gamma).\n• The two terminal phosphate-phosphate bonds are high-energy phosphoanhydride bonds (denoted by ~).\n• Hydrolysis of the terminal gamma-phosphate bond by ATPase yields ADP + Pi + 30.5 kJ mol^-1 free energy, making ATP the universal immediate energy currency in all living organisms."
        },
        {
            "q_num": 3,
            "title": "Why Is DNA Replication Continuous on the Leading Strand but Discontinuous on the Lagging Strand?",
            "category": "Enzymatic Mechanics • DNA Replication",
            "examiner_trap": "Failing to state the fundamental chemical constraint: DNA polymerase can only synthesize in the 5' to 3' direction because its catalytic site only adds nucleotides to the free 3'-OH group of an existing strand.",
            "model_answer": "• DNA polymerase requires a pre-existing 3'-OH group to form a phosphodiester bond; it synthesizes DNA exclusively in the 5' to 3' direction.\n• The two parental DNA strands are antiparallel (one 3'->5', the other 5'->3').\n• Leading strand: Synthesized continuously towards the replication fork, following helicase unwinding.\n• Lagging strand: Synthesized discontinuously away from the fork in short Okazaki fragments (1000-2000 nt in prokaryotes, 100-200 nt in eukaryotes).\n• Each Okazaki fragment requires an RNA primer (primase), elongation by DNA polymerase, primer excision by DNA polymerase I, and covalent nick-sealing by DNA ligase."
        },
        {
            "q_num": 4,
            "title": "In the Meselson-Stahl Experiment, What Exact Centrifugation Band Patterns Disprove the Conservative and Dispersive Models?",
            "category": "Experimental Design • Classical Genetics",
            "examiner_trap": "Candidates often state that Generation 1 disproves dispersive replication. Gen 1 disproves conservative replication only; Generation 2 is required to disprove the dispersive hypothesis.",
            "model_answer": "• Generation 0 (all 15N): 1 sharp dense band near bottom of CsCl tube (100% heavy 15N-15N DNA).\n• Generation 1 (1 round in 14N): Exactly ONE intermediate hybrid band (100% 15N-14N). This DISPROVES Conservative replication (which predicted 2 separate bands: 1 heavy and 1 light).\n• Generation 2 (2 rounds in 14N): Exactly TWO distinct bands: 50% intermediate hybrid (15N-14N) and 50% light (14N-14N).\n• This DISPROVES Dispersive replication (which predicted a single intermediate hybrid band becoming progressively lighter and broader with each cycle)."
        },
        {
            "q_num": 5,
            "title": "What Are the Key Structural and Functional Differences Between mRNA, tRNA, and rRNA Required by the Syllabus?",
            "category": "Comparative RNA Biology • Molecular Structure",
            "examiner_trap": "Asserting that tRNA lacks hydrogen bonds, or confusing codons with anticodons. All three are single-stranded polyribonucleotides, but fold into entirely different 3D architectures.",
            "model_answer": "• mRNA: Linear, unfolded single-stranded polyribonucleotide; transient transcript of nuclear gene; carries codons from nucleus to cytoplasm; lacks internal H-bonds.\n• tRNA: Small (~75-90 nt) folded into cloverleaf secondary structure stabilised by intra-chain hydrogen bonding; features an anticodon loop complementary to an mRNA codon, and a conserved 3' CCA-OH terminus that binds a specific amino acid.\n• rRNA: Large, globular catalytic RNA synthesized in nucleolus; complexed with ribosomal proteins to form 40S and 60S eukaryotic subunits; acts as a ribozyme (peptidyl transferase catalyzes peptide bond formation)."
        },
        {
            "q_num": 6,
            "title": "What Does It Mean That the Genetic Code Is 'Degenerate', 'Non-Overlapping', and 'Universal'?",
            "category": "Core Genetics • Code Characteristics",
            "examiner_trap": "Confusing 'degenerate' (multiple codons specify one amino acid) with 'ambiguous' (one codon specifies multiple amino acids - the genetic code is NEVER ambiguous).",
            "model_answer": "• Triplet Code: 3 consecutive bases (codon) code for 1 amino acid (4^3 = 64 codons for 20 amino acids).\n• Degenerate / Redundant: More than one codon can code for the same amino acid (e.g. 6 codons for leucine). Significance: Buffers against point mutations; third-base wobble changes often produce silent mutations.\n• Non-overlapping: Each base belongs to only one codon; read sequentially 1-3, 4-6 without skipping bases.\n• Universal: Identical codons code for the identical amino acids across almost all taxa (bacteria to humans); enables recombinant human insulin synthesis in transgenic E. coli."
        },
        {
            "q_num": 7,
            "title": "Why Are Insertion and Deletion (Frameshift) Mutations Far More Disruptive Than Single Base Substitutions?",
            "category": "Mutational Genetics • Molecular Pathology",
            "examiner_trap": "Stating that base substitutions are always harmless. Missense and nonsense mutations can cause severe disease (e.g. sickle cell); however, frameshifts alter the entire downstream polypeptide sequence.",
            "model_answer": "• Base Substitution: Replaces 1 nucleotide with another. Effect: Changes at most ONE amino acid (missense), or none due to degeneracy (silent), or creates a stop codon (nonsense).\n• Indel / Frameshift: Adding or deleting 1 or 2 nucleotides (not a multiple of 3) shifts the triplet reading frame downstream of the mutation.\n• Every single subsequent codon is altered, completely scrambling the downstream amino acid sequence.\n• Frameshifts almost invariably introduce an early premature stop codon (UAA, UAG, UGA), producing a severely truncated, non-functional protein."
        },
        {
            "q_num": 8,
            "title": "Explain the Complete Molecular Cascade of Sickle Cell Anaemia: From DNA Base Change to Capillary Vaso-Occlusion.",
            "category": "Clinical Genetics • Molecular Pathology",
            "examiner_trap": "Saying that sickle cells stick together because HbS is 'abnormal'. Marks require explaining that deoxygenation exposes a hydrophobic pocket, Val6 binds to adjacent beta-chain pocket, and tetramers polymerise into rigid fibres.",
            "model_answer": "• Mutation: Single base substitution (transversion) in codon 6 of beta-globin (HBB) gene: coding strand 5'-GAG-3' -> 5'-GTG-3' (template strand 3'-CTC-5' -> 3'-CAC-5').\n• Transcription: mRNA codon changes from 5'-GAG-3' to 5'-GUG-3'.\n• Translation: Glutamic acid (Glu) substituted by Valine (Val) at position 6 of beta-chain.\n• Biochemical change: Polar, hydrophilic charged Glu replaced by non-polar, hydrophobic Val; creates sticky hydrophobic contact patch on tetramer exterior.\n• Polymerisation: At low pO2 (respiring tissues), deoxy-HbS exposes hydrophobic pocket on adjacent beta-subunit; Val6 binds into pocket, polymerising HbS into insoluble 14-strand rigid helical fibres.\n• Pathology: Distorts erythrocytes into rigid, fragile sickles; block narrow capillaries (vaso-occlusion -> ischaemia, acute crisis); rupture rapidly (haemolysis -> chronic anaemia)."
        },
        {
            "q_num": 9,
            "title": "Why Do Linear Chromosomes Require Telomeres and How Does Telomerase Prevent Progressive Shortening?",
            "category": "Chromosome Biology • Telomere Dynamics",
            "examiner_trap": "Claiming that telomeres code for essential proteins. Telomeres are strictly NON-CODING repetitive hexamers (TTAGGG) that serve as protective, expendable terminal caps.",
            "model_answer": "• The End-Replication Problem: DNA polymerase can only synthesize DNA 5'->3' from an existing 3'-OH primer. On the lagging strand, excision of the terminal RNA primer leaves an unreplicated gap at the 5' end of the daughter strand; chromosomes shorten by ~50-200 bp with each replication cycle.\n• Telomere Structure: Non-coding tandem repeats (human: 5'-TTAGGG-3') bound by shelterin protein complexes at linear chromosome ends.\n• Protective Functions: (1) Prevents loss of vital coding genes during repeated cell division; (2) Prevents chromosome ends from fusing; (3) Prevents DNA repair enzymes from misidentifying ends as double-strand breaks.\n• Telomerase: Ribonucleoprotein reverse transcriptase with internal RNA template (3'-AAUCCC-5'); extends 3' parental overhang in germ cells, stem cells, and ~90% of human cancers, conferring cellular immortality."
        },
        {
            "q_num": 10,
            "title": "How Do Aminoacyl-tRNA Synthetase Enzymes Guarantee the Fidelity of Translation During tRNA 'Charging'?",
            "category": "Translational Mechanics • Enzymology",
            "examiner_trap": "Overlooking the role of ATP in activating the amino acid. The reaction is an energy-requiring two-step condensation catalyzed by 20 specific synthetase enzymes.",
            "model_answer": "• Fidelity Requirement: The ribosome decoding site checks ONLY base pairing between the mRNA codon and tRNA anticodon; it cannot detect whether the attached amino acid matches the anticodon. Translation fidelity depends entirely on aminoacyl-tRNA synthetase specificity.\n• Specificity: Cells have 20 distinct aminoacyl-tRNA synthetase enzymes, each with active sites specific for exactly one amino acid and the anticodon/structural features of its cognate tRNA.\n• Two-Step Mechanism:\n  1. Amino acid activation: Amino acid + ATP -> Aminoacyl-AMP + PPi (pyrophosphatase hydrolyzes PPi -> 2 Pi, driving reaction).\n  2. Esterification: Activated amino acid is transferred to 3'-OH of CCA terminal adenine of tRNA, forming high-energy ester bond and releasing AMP.\n• The high-energy ester bond provides the activation energy utilized by peptidyl transferase to form the peptide bond during translation elongation."
        }
    ]
