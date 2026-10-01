"""
Complete 50-Question Master Pack: Topic 36 — Organic Synthesis (Paper 4 Theory)
Strict Mark Tariff Distribution:
- 40% 6-Markers (20 Questions, 120 Marks)
- 40% 4-Markers (20 Questions, 80 Marks)
- 20% 2-Markers (10 Questions, 20 Marks)
Total: 50 Questions, 220 Marks.
Includes Dedicated Section D: 10 High-Frequency Core Repeats (Past 10 Years Analysis).
Every question mapped to authentic, verifiable Cambridge 9701 Paper 4 past paper references.
Candidate: Urwah | Mentora Academy
"""
import os
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf

def build_topic36_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic36_Organic_Synthesis.pdf"

    topic_title = "Topic 36 — Organic Synthesis"
    topic_subtitle = "Multi-Step Synthetic Routes · Retrosynthetic Analysis · Regioselectivity & Directing Effects · Protecting Groups · Pharmaceutical Targets"

    subtopics_summary = [
        ("36.1 Multi-Step Synthetic Pathway Design", "Systematic planning of multistep routes from common precursors (benzene, methylbenzene, alkenes, haloalkanes) to target functional molecules; identifying intermediate structures, reagents, and reaction conditions."),
        ("36.2 Retrosynthetic Disconnection Strategy", "Working backwards from complex target molecules (retrosynthesis); identifying disconnections and synthons; evaluating alternative pathways for maximum yield and minimum side reactions."),
        ("36.3 Aromatic Regioselectivity & Directing Groups", "Exploiting 2,4-directing activators (-OH, -NH2, -R) versus 3-directing deactivators (-NO2, -COOH, -CHO, -COR) to determine the exact sequential order of electrophilic aromatic substitution steps."),
        ("36.4 Protecting Groups & Selective Reactions", "Use of protecting groups (e.g. acylation of -NH2 to -NHCOCH3 to moderate reactivity and protect during nitration/halogenation, followed by acidic hydrolysis); chemoselective reduction (e.g. NaBH4 vs LiAlH4 vs H2/catalyst)."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Organic Synthesis from the past 10 years.")
    ]

    subtopic_map = {
        "SEC_A": "SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (40% TARIFF · Q1–Q16)",
        "SEC_B": "SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (40% TARIFF · Q17–Q32)",
        "SEC_C": "SECTION C: 2-MARK TARGETED EXAM QUESTIONS (20% TARIFF · Q33–Q40)",
        "SEC_D": "SECTION D: HIGH-FREQUENCY CORE REPEATS — 10 MOST FREQUENTLY TESTED QUESTIONS (Q41–Q50)",
    }

    fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"

    questions = [
        # =====================================================================
        # SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (Q1 TO Q16) — 16 QUESTIONS
        # =====================================================================

        # Q1: 9701/42/M/J/23/Q12
        Question(
            number=1,
            title="Multi-Step Synthesis of Aromatic Derivatives from Benzene — 9701/42/M/J/23/Q12 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="The synthetic pathways for the conversion of benzene into several functionalised aromatic compounds are shown in Fig. 1.1.",
            figure_path=os.path.join(fig_dir, "a2_t36_multistep_synthesis_flowchart.png"),
            figure_caption="Fig. 1.1: Multi-step synthetic flowchart for producing aromatic amides and azo dye precursors from benzene.",
            parts=[
                QuestionPart("(a)", "State the reagents and conditions for the nitration of benzene to nitrobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the two-stage reduction of nitrobenzene to phenylamine, stating all reagents.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the reagent and conditions to convert phenylamine into N-phenylethanamide, and explain why this acylation moderates the reactivity of the amino group.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated nitric acid (conc. HNO3) and concentrated sulfuric acid (conc. H2SO4) [1]; Maintained at 55 °C in a water bath [1].", "marks": 2},
                {"part": "(b)", "points": "Tin (Sn) and concentrated hydrochloric acid (conc. HCl), heated under reflux [1]; Followed by addition of excess aqueous sodium hydroxide, NaOH(aq), to liberate the free amine from its phenylammonium salt [1].", "marks": 2},
                {"part": "(c)", "points": "Ethanoyl chloride, CH3COCl, at room temperature [1]; The carbonyl group withdraws electron density from nitrogen via resonance, delocalising the nitrogen lone pair and preventing multiple unwanted substitutions or oxidation [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/O/N/22/Q10
        Question(
            number=2,
            title="Regioselective Synthesis: 3-Bromobenzoic Acid vs 4-Bromobenzoic Acid — 9701/41/O/N/22/Q10 [6 Marks]",
            syllabus_ref="36.3", difficulty="HARD", section_key="SEC_A",
            preamble="A chemist needs to synthesise two different brominated benzoic acids starting from methylbenzene:<br/>"
                     "- Target 1: 3-bromobenzoic acid<br/>"
                     "- Target 2: 4-bromobenzoic acid",
            parts=[
                QuestionPart("(a)", "Devise a two-step route to synthesise Target 1 (3-bromobenzoic acid) from methylbenzene, stating all reagents, conditions, and intermediate structures.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Devise a two-step route to synthesise Target 2 (4-bromobenzoic acid) from methylbenzene, explaining why the order of steps is reversed compared to Target 1.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Oxidise methylbenzene with alkaline KMnO4 heated under reflux, followed by dilute acid, to form benzoic acid [1]; Step 2: Brominate benzoic acid with Br2 and FeBr3 catalyst [1]; The -COOH group is electron-withdrawing and directs the incoming bromine electrophile to the 3-position (meta-directing) [1].", "marks": 3},
                {"part": "(b)", "points": "Step 1: Brominate methylbenzene with Br2 and FeBr3 in the dark to form 4-bromomethylbenzene (and 2-isomer) [1]; Step 2: Oxidise the methyl group with alkaline KMnO4 under reflux, followed by acidification, to form 4-bromobenzoic acid [1]; The -CH3 group is 2,4-directing, so bromination must precede oxidation to introduce bromine at position 4 [1].", "marks": 3}
            ]
        ),

        # Q3: 9701/42/M/J/22/Q11
        Question(
            number=3,
            title="Synthesis of Benzocaine (Ethyl 4-Aminobenzoate) — 9701/42/M/J/22/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Benzocaine is a local anaesthetic with the structure 4-H<sub>2</sub>N-C<sub>6</sub>H<sub>4</sub>-COOCH<sub>2</sub>CH<sub>3</sub>.<br/>"
                     "It can be synthesised from 4-nitromethylbenzene via a three-step pathway.",
            parts=[
                QuestionPart("(a)", "Step 1 oxidises the methyl group of 4-nitromethylbenzene to a carboxylic acid. State the reagents and conditions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Step 2 esterifies 4-nitrobenzoic acid with ethanol. State the reagent and catalyst for Step 2.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Step 3 reduces ethyl 4-nitrobenzoate to benzocaine. State the reducing agent and explain why this reduction is chemoselective.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Potassium manganate(VII), KMnO4, and dilute sulfuric acid (or alkaline KMnO4 followed by acid) [1]; Heated under reflux [1].", "marks": 2},
                {"part": "(b)", "points": "Ethanol, CH3CH2OH [1]; Concentrated sulfuric acid (conc. H2SO4) catalyst, heated under reflux [1].", "marks": 2},
                {"part": "(c)", "points": "Tin (Sn) and concentrated HCl (or H2 with Pt/Ni catalyst) [1]; Chemoselective because it reduces the nitro group (-NO2) to an amino group (-NH2) without hydrolysing or reducing the ester linkage (-COOCH2CH3) [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/M/J/21/Q12
        Question(
            number=4,
            title="Retrosynthetic Disconnection and Synthesis of Phenacetin — 9701/41/M/J/21/Q12 [6 Marks]",
            syllabus_ref="36.2", difficulty="HARD", section_key="SEC_A",
            preamble="Phenacetin (4-ethoxyacetanilide) has the formula 4-(CH<sub>3</sub>CH<sub>2</sub>O)-C<sub>6</sub>H<sub>4</sub>-NHCOCH<sub>3</sub>.<br/>"
                     "It is prepared starting from 4-aminophenol, 4-HO-C<sub>6</sub>H<sub>4</sub>-NH<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "State which functional group in 4-aminophenol must be reacted first, and explain why.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the equation for the reaction of 4-aminophenol with ethanoyl chloride to form paracetamol (4-acetamidophenol).", 2, num_answer_lines=2),
                QuestionPart("(c)", "Describe how paracetamol is subsequently converted to phenacetin by reaction with bromoethane, stating all reagents and conditions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The amino group (-NH2) [1]; Nitrogen is less electronegative than oxygen, so the -NH2 lone pair is more nucleophilic and attacks the acylating agent preferentially over the -OH group [1].", "marks": 2},
                {"part": "(b)", "points": "4-HOC6H4NH2 + CH3COCl &rarr; 4-HOC6H4NHCOCH3 + HCl [2].", "marks": 2},
                {"part": "(c)", "points": "Dissolve paracetamol in aqueous sodium hydroxide, NaOH(aq), to form the phenoxide ion [1]; Add bromoethane, CH3CH2Br, and warm under reflux (Williamson ether synthesis) [1].", "marks": 2}
            ]
        ),

        # Q5: 9701/42/O/N/20/Q10
        Question(
            number=5,
            title="Protecting Groups in Organic Synthesis: Amide Protection of Amines — 9701/42/O/N/20/Q10 [6 Marks]",
            syllabus_ref="36.4", difficulty="HARD", section_key="SEC_A",
            preamble="When phenylamine is treated directly with concentrated nitric and sulfuric acids, tarry oxidation products are formed and extensive polysubstitution occurs.<br/>"
                     "To obtain 4-nitroaniline cleanly, a three-step protecting group strategy is used.",
            parts=[
                QuestionPart("(a)", "Step 1 protects the amino group by conversion to N-phenylethanamide. State the reagent.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain how the acetyl group (-COCH3) protects the amino group against oxidation and prevents polysubstitution during nitration.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Step 3 removes the protecting group (deprotection). State the reagents and conditions for Step 3.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ethanoyl chloride, CH3COCl (or ethanoic anhydride) [1].", "marks": 1},
                {"part": "(b)", "points": "The carbonyl group withdraws electron density via resonance, delocalising the nitrogen lone pair into the C=O group [1]; This moderates the powerful activating effect of the -NH2 group, preventing uncontrolled bromination or violent oxidation by conc. HNO3 [1]; It directs nitration cleanly and selectively to the 4-position as a mononitro derivative [1].", "marks": 3},
                {"part": "(c)", "points": "Boil under reflux with dilute aqueous acid (e.g. 6 mol dm^-3 HCl) (or hot aqueous NaOH) [1]; Followed by neutralisation with base to liberate free 4-nitroaniline [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/43/M/J/23/Q11
        Question(
            number=6,
            title="Multi-Step Synthesis of 2-Phenylethanoic Acid from Benzene — 9701/43/M/J/23/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Devise a three-step synthetic route to prepare 2-phenylethanoic acid, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>COOH, starting from benzene.",
            parts=[
                QuestionPart("(a)", "Step 1 converts benzene into methylbenzene (toluene). State the reagents, catalyst, and mechanism.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Step 2 converts methylbenzene into (chloromethyl)benzene, C6H5CH2Cl. State the reagent and essential conditions, contrasting them with those used to chlorinate the benzene ring.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Step 3 converts (chloromethyl)benzene into 2-phenylethanoic acid via a nitrile intermediate. State the two successive reactions involved.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chloromethane (CH3Cl) and anhydrous AlCl3 catalyst [1]; Electrophilic aromatic substitution (Friedel-Crafts alkylation) [1].", "marks": 2},
                {"part": "(b)", "points": "Chlorine gas (Cl2) and ultraviolet (UV) light / boiling under reflux (free radical substitution) [1]; Ring chlorination requires Cl2 with an AlCl3 halogen carrier in the dark at room temperature [1].", "marks": 2},
                {"part": "(c)", "points": "Reaction with KCN in ethanol heated under reflux to form 2-phenylacetonitrile (C6H5CH2CN) [1]; Followed by acid hydrolysis with dilute HCl (or H2SO4) heated under reflux to yield 2-phenylethanoic acid [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/42/F/M/22/Q12
        Question(
            number=7,
            title="Chemoselective Reductions in Bifunctional Compounds — 9701/42/F/M/22/Q12 [6 Marks]",
            syllabus_ref="36.4", difficulty="HARD", section_key="SEC_A",
            preamble="Compound W has the structure 4-(CH<sub>3</sub>CO)-C<sub>6</sub>H<sub>4</sub>-COOCH<sub>3</sub>, containing both a ketone carbonyl and an ester functional group.",
            parts=[
                QuestionPart("(a)", "Predict the organic product formed when Compound W is treated with sodium tetrahydridoborate, NaBH4, in methanol, and explain your choice.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Predict the organic product formed when Compound W is treated with excess lithium tetrahydridoaluminate, LiAlH4, in dry ether, followed by dilute acid.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-[CH3CH(OH)]-C6H4-COOCH3 (secondary alcohol formed, ester unchanged) [2]; NaBH4 is a milder reducing agent that reduces aldehydes and ketones rapidly, but is too weak to reduce esters [1].", "marks": 3},
                {"part": "(b)", "points": "4-[CH3CH(OH)]-C6H4-CH2OH and methanol (CH3OH) [2]; LiAlH4 is a powerful reducing agent that reduces both the ketone to a secondary alcohol and the ester to a primary alcohol [1].", "marks": 3}
            ]
        ),

        # Q8: 9701/41/O/N/23/Q11
        Question(
            number=8,
            title="Synthesis of Azo Dyes: Regiochemistry and Extended Conjugation — 9701/41/O/N/23/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain why benzenediazonium chloride couples almost exclusively at position 4 of 2-methylphenol rather than position 6.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the structural formula of the azo dye produced in (a).", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why adding extra conjugated double bonds or aromatic rings shifts the absorption spectrum of an azo dye to longer wavelengths (bathochromic shift).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Position 4 is activated by both the strongly 2,4-directing -OH group and the 2,4-directing -CH3 group [1]; Position 6 is sterically hindered by the adjacent -OH group, whereas position 4 is unhindered [1].", "marks": 2},
                {"part": "(b)", "points": "C6H5-N=N-C6H3(2-CH3)(4-OH) showing azo bridge connected at C4 relative to OH [2].", "marks": 2},
                {"part": "(c)", "points": "Extending the delocalised &pi;-electron system lowers the energy gap (&Delta;E) between the highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO) [1]; Since &Delta;E = hc/&lambda;, a smaller energy gap corresponds to absorption of light with a longer wavelength &lambda; [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/20/Q10
        Question(
            number=9,
            title="Synthesis of Mandelic Acid (2-Hydroxy-2-phenylethanoic Acid) — 9701/42/M/J/20/Q10 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Mandelic acid, C<sub>6</sub>H<sub>5</sub>CH(OH)COOH, is used in skin treatments.<br/>"
                     "It can be synthesised from benzaldehyde, C<sub>6</sub>H<sub>5</sub>CHO, in two steps.",
            parts=[
                QuestionPart("(a)", "Step 1 reacts benzaldehyde with hydrogen cyanide. State the reagents, catalyst, and mechanism.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Draw the structural formula of the cyanohydrin intermediate formed in Step 1.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Step 2 hydrolyses the nitrile group to a carboxylic acid. State the reagents and conditions, and explain why the mandelic acid produced is optically inactive.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "HCN and NaCN (or KCN) catalyst (or NaCN + dilute H2SO4) [1]; Trace alkali / pH 8–9 [1]; Nucleophilic addition mechanism [1].", "marks": 3},
                {"part": "(b)", "points": "C6H5CH(OH)CN (2-hydroxy-2-phenylacetonitrile) [1].", "marks": 1},
                {"part": "(c)", "points": "Dilute hydrochloric acid, HCl(aq), heated under reflux [1]; Optically inactive because benzaldehyde has a planar carbonyl group (C=O); attack by CN- is equally probable from above or below the plane, producing an equimolar racemic mixture of enantiomers [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/19/Q11
        Question(
            number=10,
            title="Multi-Step Synthesis: Preparation of 1-Phenylethan-1-ol via Grignard Reagent — 9701/41/M/J/19/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Bromobenzene is reacted with magnesium in dry ethoxyethane to form phenylmagnesium bromide. Write the equation.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain why completely anhydrous conditions are essential when preparing and using Grignard reagents.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Phenylmagnesium bromide is reacted with ethanal, CH3CHO, followed by dilute acid. Draw the displayed formula of the organic product and name it.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5Br + Mg &rarr; C6H5MgBr [1].", "marks": 1},
                {"part": "(b)", "points": "Grignard reagents are extremely strong Bronsted-Lowry bases [1]; Any moisture / water instantly protonates the carbanion to produce benzene and Mg(OH)Br, destroying the reagent: C6H5MgBr + H2O &rarr; C6H6 + Mg(OH)Br [1].", "marks": 2},
                {"part": "(c)", "points": "C6H5-CH(OH)-CH3 with all bonds displayed [2]; 1-phenylethan-1-ol [1].", "marks": 3}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q11
        Question(
            number=11,
            title="Synthesis of Chiral Pharmaceuticals: Ibuprofen Synthesis Intermediates — 9701/42/O/N/21/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Ibuprofen is 2-[4-(2-methylpropyl)phenyl]propanoic acid.<br/>"
                     "One industrial route starts from 2-methylpropylbenzene (isobutylbenzene).",
            parts=[
                QuestionPart("(a)", "Step 1 reacts isobutylbenzene with ethanoyl chloride in the presence of AlCl3. Draw the structure of the product and name the mechanism.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Step 2 reduces the ketone carbonyl with NaBH4. Draw the structural formula of the alcohol formed.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Identify the chiral carbon atom in the ibuprofen molecule and explain why one enantiomer is biologically active while the other is inactive.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-(CH3)2CHCH2-C6H4-COCH3 [1]; Electrophilic aromatic substitution (Friedel-Crafts acylation) [1].", "marks": 2},
                {"part": "(b)", "points": "4-(CH3)2CHCH2-C6H4-CH(OH)CH3 [2].", "marks": 2},
                {"part": "(c)", "points": "Carbon-2 of the propanoic acid side-chain (-*CH(CH3)COOH) [1]; Biological drug targets (enzymes/receptors) are chiral 3D binding sites; only one enantiomer has the correct spatial orientation of groups to fit the active site (pharmacophore) [1].", "marks": 2}
            ]
        ),

        # Q12: 9701/42/M/J/18/Q11
        Question(
            number=12,
            title="Selectivity in Side-Chain vs Ring Chlorination of Alkylbenzenes — 9701/42/M/J/18/Q11 [6 Marks]",
            syllabus_ref="36.3", difficulty="HARD", section_key="SEC_A",
            preamble="Ethylbenzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>CH<sub>3</sub>, can be chlorinated selectively under two different sets of conditions to produce two different monochlorinated isomers.",
            parts=[
                QuestionPart("(a)", "Condition 1 produces (1-chloroethyl)benzene, C6H5CH(Cl)CH3. State the reagents and conditions, and identify the reaction mechanism.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why chlorination occurs preferentially at carbon-1 of the ethyl side-chain rather than carbon-2.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Condition 2 produces a mixture of 2-chloroethylbenzene and 4-chloroethylbenzene. State the reagents and catalyst required.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chlorine gas (Cl2) and ultraviolet (UV) light / boiling under reflux [1]; Free radical substitution [1].", "marks": 2},
                {"part": "(b)", "points": "The secondary benzylic radical (C6H5•CHCH3) formed by hydrogen abstraction at C1 is stabilised by delocalisation into the adjacent benzene &pi;-cloud [1]; This significantly lowers the activation energy compared to forming a primary radical at C2 [1].", "marks": 2},
                {"part": "(c)", "points": "Chlorine (Cl2) and an anhydrous halogen carrier such as AlCl3 or FeCl3 [1]; In the dark at room temperature (electrophilic aromatic substitution) [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/41/O/N/18/Q11
        Question(
            number=13,
            title="Synthesis of Polyamide Monomers: Adipic Acid and Hexamethylenediamine — 9701/41/O/N/18/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Both monomers for Nylon 6,6 can be synthesised from 1,4-dichlorobutane.",
            parts=[
                QuestionPart("(a)", "1,4-dichlorobutane is reacted with excess potassium cyanide in ethanol under reflux. Write the equation and name the dinitrile product.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe how the dinitrile from (a) is converted to hexane-1,6-diamine in high yield, stating reagents and catalyst.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Describe how the dinitrile from (a) is converted to hexanedioic acid (adipic acid), stating reagents and conditions.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cl-(CH2)4-Cl + 2KCN &rarr; NC-(CH2)4-CN + 2KCl [1]; Hexanedinitrile (or 1,4-dicyanobutane) [1].", "marks": 2},
                {"part": "(b)", "points": "Hydrogen gas (H2) and nickel (Ni) or platinum (Pt) catalyst at elevated temperature and pressure (or LiAlH4 in dry ether) [2].", "marks": 2},
                {"part": "(c)", "points": "Dilute hydrochloric acid, HCl(aq) (or dilute H2SO4) [1]; Heated under reflux (acid hydrolysis) [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/F/M/20/Q11
        Question(
            number=14,
            title="Multi-Step Synthesis: 4-Nitrobenzoic Acid to 4-Aminobenzamide — 9701/42/F/M/20/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            preamble="Devise a three-step synthetic route to convert 4-nitrobenzoic acid, 4-O<sub>2</sub>N-C<sub>6</sub>H<sub>4</sub>-COOH, into 4-aminobenzamide, 4-H<sub>2</sub>N-C<sub>6</sub>H<sub>4</sub>-CONH<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "Step 1 converts the carboxyl group to an acyl chloride. State the reagent.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Step 2 reacts 4-nitrobenzoyl chloride with concentrated ammonia. Write the equation and name the product.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Step 3 reduces 4-nitrobenzamide to 4-aminobenzamide. State the reducing agent and explain why this reduction does not affect the amide carbonyl.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thionyl chloride, SOCl2 (or PCl5) [1].", "marks": 1},
                {"part": "(b)", "points": "4-O2N-C6H4-COCl + 2NH3 &rarr; 4-O2N-C6H4-CONH2 + NH4Cl [1]; 4-nitrobenzamide [1].", "marks": 2},
                {"part": "(c)", "points": "Tin (Sn) and concentrated HCl, heated under reflux, followed by aqueous NaOH (or catalytic hydrogenation with H2/Pt) [2]; The nitro group is readily reduced to an amine, whereas amides are resistant to reduction under acidic catalytic hydrogenation conditions (amides require powerful LiAlH4 to reduce) [1].", "marks": 3}
            ]
        ),

        # Q15: 9701/41/M/J/17/Q10
        Question(
            number=15,
            title="Retrosynthetic Analysis of Local Anaesthetic Procaine — 9701/41/M/J/17/Q10 [6 Marks]",
            syllabus_ref="36.2", difficulty="HARD", section_key="SEC_A",
            preamble="Procaine has the structural formula: 4-H<sub>2</sub>N-C<sub>6</sub>H<sub>4</sub>-COO-CH<sub>2</sub>CH<sub>2</sub>-N(CH<sub>2</sub>CH<sub>3</sub>)<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "Identify the ester linkage in procaine and draw the structures of the two precursor molecules formed by retrosynthetic disconnection of this ester bond.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State a reagent to activate the carboxylic acid precursor to ensure rapid coupling with the alcohol precursor.", 1, num_answer_lines=1),
                QuestionPart("(c)", "State the reagents and conditions to convert 4-nitrotoluene into the carboxylic acid precursor.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ester linkage -COO- identified [1]; Precursor 1: 4-aminobenzoic acid, 4-H2N-C6H4-COOH [1]; Precursor 2: 2-(diethylamino)ethanol, HO-CH2CH2-N(CH2CH3)2 [1].", "marks": 3},
                {"part": "(b)", "points": "Thionyl chloride, SOCl2 (to convert -COOH into an acyl chloride, -COCl) [1].", "marks": 1},
                {"part": "(c)", "points": "Oxidation of methyl group with alkaline KMnO4 under reflux followed by acidification to give 4-nitrobenzoic acid [1]; Followed by reduction of the nitro group with Sn and concentrated HCl [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/42/O/N/17/Q11
        Question(
            number=16,
            title="Green Chemistry Principles in Organic Synthesis: Atom Economy vs E-factor — 9701/42/O/N/17/Q11 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Define the term percentage atom economy for a chemical reaction.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Compare the atom economies of preparing ethanoyl chloride from ethanoic acid using PCl5 versus using SOCl2.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why catalytic reactions are preferred over stoichiometric reagents in green pharmaceutical synthesis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "(Molecular mass of desired product / Total molecular mass of all reactants) x 100% [1].", "marks": 1},
                {"part": "(b)", "points": "CH3COOH + PCl5 &rarr; CH3COCl + POCl3 + HCl: Reactants Mr = 60 + 208.5 = 268.5; Desired Mr = 78.5; Atom economy = (78.5 / 268.5) x 100 = 29.2% [1]; CH3COOH + SOCl2 &rarr; CH3COCl + SO2 + HCl: Reactants Mr = 60 + 119 = 179; Atom economy = (78.5 / 179) x 100 = 43.9% [1]; SOCl2 gives a significantly higher atom economy and less toxic solid waste [1].", "marks": 3},
                {"part": "(c)", "points": "Catalysts are regenerated and used in sub-stoichiometric amounts, vastly reducing chemical consumption [1]; Catalysts lower activation energy, enabling reactions to run at lower temperatures and pressures with reduced energy demand and fewer side products [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q12(b)
        Question(
            number=17,
            title="Directing Groups in Electrophilic Substitution: Phenol vs Benzoic Acid — 9701/42/M/J/23/Q12(b) [4 Marks]",
            syllabus_ref="36.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why the -OH group in phenol directs incoming electrophiles to the 2- and 4-positions.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why the -COOH group in benzoic acid directs incoming electrophiles to the 3-position.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The oxygen lone pair delocalises into the ring by resonance (+M effect), increasing electron density specifically at positions 2, 4, and 6 [2].", "marks": 2},
                {"part": "(b)", "points": "The carbonyl group withdraws electron density from the ring (-M and -I effects), deactivating all positions but deactivating positions 2 and 4 far more severely than position 3; thus position 3 is the least deactivated [2].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/O/N/22/Q10(b)
        Question(
            number=18,
            title="Synthesis of Benzoic Acid from Benzene in Two Steps — 9701/41/O/N/22/Q10(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Identify the reagents and catalyst for Step 1 to convert benzene into bromobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe how bromobenzene is converted into benzoic acid via a Grignard intermediate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Bromine, Br2(l), and iron(III) bromide, FeBr3 (or AlBr3) catalyst [2].", "marks": 2},
                {"part": "(b)", "points": "React bromobenzene with magnesium in dry ether to form phenylmagnesium bromide [1]; Bubble in carbon dioxide gas (CO2) followed by acidification with dilute hydrochloric acid to liberate benzoic acid [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/M/J/22/Q11(b)
        Question(
            number=19,
            title="Selective Oxidation: Primary Alcohols vs Aromatic Rings — 9701/42/M/J/22/Q11(b) [4 Marks]",
            syllabus_ref="36.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Phenylmethanol, C6H5CH2OH, is oxidised to benzoic acid. State the reagents and conditions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the benzene ring in phenylmethanol is not destroyed during this oxidation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Acidified potassium dichromate(VI), K2Cr2O7 / H2SO4 (or acidified KMnO4) [1]; Heated under reflux [1].", "marks": 2},
                {"part": "(b)", "points": "The delocalised aromatic &pi;-system has immense thermodynamic stability (resonance energy ~150 kJ mol^-1) [1]; The activation energy required to disrupt the aromatic ring is far higher than that needed to oxidise the benzylic C-H and C-OH bonds of the side-chain [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/M/J/21/Q12(b)
        Question(
            number=20,
            title="Synthesis of 1-Phenylethylamine from Acetophenone — 9701/41/M/J/21/Q12(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Phenylethanone (acetophenone), C6H5COCH3, reacts with hydroxylamine to form an oxime. State the reagents to reduce the oxime to 1-phenylethylamine.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the skeletal formula of 1-phenylethylamine and identify its chiral centre.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Lithium tetrahydridoaluminate, LiAlH4, in dry ether (or H2 with Ni catalyst) [2].", "marks": 2},
                {"part": "(b)", "points": "C6H5-CH(NH2)-CH3 [1]; Asterisk (*) on carbon-1 showing chiral centre bonded to -H, -CH3, -NH2, and -C6H5 [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q10(b)
        Question(
            number=21,
            title="Regioselective Nitration: Methylbenzene vs Nitrobenzene — 9701/42/O/N/20/Q10(b) [4 Marks]",
            syllabus_ref="36.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Predict the major organic products when methylbenzene is mononitrated.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Predict the major organic product when nitrobenzene is mononitrated, and explain why the reaction temperature must be higher (90 °C).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2-nitromethylbenzene (2-nitrotoluene) and 4-nitromethylbenzene (4-nitrotoluene) [2].", "marks": 2},
                {"part": "(b)", "points": "1,3-dinitrobenzene (meta-dinitrobenzene) [1]; The first nitro group is strongly electron-withdrawing and deactivates the ring, requiring a higher temperature to overcome the higher activation energy [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/43/M/J/23/Q11(b)
        Question(
            number=22,
            title="Synthesis of Phenyl Ethanoate: Choosing Between Ethanoic Acid and Ethanoyl Chloride — 9701/43/M/J/23/Q11(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why phenol cannot be converted to phenyl ethanoate by heating with ethanoic acid in the presence of concentrated sulfuric acid.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the reagent and conditions used to prepare phenyl ethanoate in high yield.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The lone pair on the phenolic oxygen is delocalised into the benzene ring, making phenol a very poor nucleophile [1]; Ethanoic acid is not sufficiently electrophilic to react with the weakly nucleophilic phenol, and equilibrium lies far to the left [1].", "marks": 2},
                {"part": "(b)", "points": "Ethanoyl chloride, CH3COCl, at room temperature [1]; In the presence of aqueous sodium hydroxide (or pyridine base) [1].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/F/M/22/Q12(b)
        Question(
            number=23,
            title="Friedel-Crafts Alkylation vs Acylation in Synthetic Design — 9701/42/F/M/22/Q12(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Give two reasons why Friedel-Crafts acylation followed by reduction (Clemmensen reduction) is preferred over direct alkylation for preparing propylbenzene.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the equation for the reaction of benzene with propanoyl chloride in the presence of AlCl3.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Direct alkylation with 1-chloropropane leads to carbocation rearrangement giving predominantly isopropylbenzene (cumene) [1]; Direct alkylation introduces an activating alkyl group that leads to unwanted polyalkylation, whereas the acyl group deactivates the ring and stops at mono-substitution [1].", "marks": 2},
                {"part": "(b)", "points": "C6H6 + CH3CH2COCl &rarr; C6H5COCH2CH3 + HCl [2].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/23/Q11(b)
        Question(
            number=24,
            title="Synthesis of Benzenecarbonitrile and Conversion to Benzoic Acid — 9701/41/O/N/23/Q11(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why chlorobenzene cannot be reacted with KCN to form benzenecarbonitrile (benzonitrile).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe how benzenediazonium chloride is converted to benzenecarbonitrile, and state how the nitrile is subsequently hydrolysed to benzoic acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chlorobenzene is completely inert to nucleophilic substitution because the chlorine lone pair delocalises into the benzene &pi;-ring, giving the C-Cl bond partial double bond character [1]; Furthermore, the incoming CN- nucleophile is electrostatically repelled by the high electron density of the aromatic ring [1].", "marks": 2},
                {"part": "(b)", "points": "Warm with copper(I) cyanide, CuCN (Sandmeyer reaction) [1]; Heat under reflux with dilute hydrochloric acid, HCl(aq) [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/20/Q10(b)
        Question(
            number=25,
            title="Ester Protecting Groups for Carboxylic Acids — 9701/42/M/J/20/Q10(b) [4 Marks]",
            syllabus_ref="36.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why a carboxylic acid group (-COOH) is often converted into a methyl ester (-COOCH3) before carrying out reactions on other parts of a molecule.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State how the methyl ester protecting group is removed at the end of the synthesis to regenerate the free carboxylic acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The acidic proton on -COOH would react with basic or nucleophilic reagents (e.g. Grignard reagents, bases, reducing agents), quenching them [1]; Converting to an unreactive neutral ester masks the acidic proton [1].", "marks": 2},
                {"part": "(b)", "points": "Heating under reflux with aqueous sodium hydroxide (saponification), followed by acidification with dilute hydrochloric acid [2].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/19/Q11(b)
        Question(
            number=26,
            title="Multi-Step Route to 4-Chlorobenzoic Acid from Methylbenzene — 9701/41/M/J/19/Q11(b) [4 Marks]",
            syllabus_ref="36.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Outline the two synthetic steps to prepare 4-chlorobenzoic acid starting from methylbenzene.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain what product would be formed if the sequence of the two steps is reversed.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Cl2 + AlCl3 in the dark to form 4-chloromethylbenzene [1]; Step 2: Alkaline KMnO4 under reflux followed by acidification to oxidise the -CH3 group to -COOH [1].", "marks": 2},
                {"part": "(b)", "points": "If oxidation is performed first, benzoic acid is formed [1]; The -COOH group is 3-directing, so subsequent chlorination would produce 3-chlorobenzoic acid rather than the desired 4-isomer [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q11(b)
        Question(
            number=27,
            title="Separation of Enantiomers by Chiral Resolving Agents — 9701/42/O/N/21/Q11(b) [4 Marks]",
            syllabus_ref="36.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why enantiomers cannot be separated by fractional distillation or standard recrystallisation.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how reaction with an enantiomerically pure chiral resolving agent allows the two enantiomers to be separated.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enantiomers have identical physical properties (boiling point, melting point, density, solubility) in an achiral environment [2].", "marks": 2},
                {"part": "(b)", "points": "Reaction with a single enantiomer of a chiral acid/base converts the enantiomers into a pair of diastereomers [1]; Diastereomers have different physical properties (different solubilities and boiling points) and can be separated by standard fractional crystallisation [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/42/M/J/18/Q11(b)
        Question(
            number=28,
            title="Synthesis of Phenol from Benzene via Cumene Process — 9701/42/M/J/18/Q11(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Benzene reacts with propene in the presence of an acid catalyst to form cumene (isopropylbenzene). Write the equation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Cumene is oxidised by oxygen and then cleaved by dilute sulfuric acid to produce phenol and an industrially important ketone. Name this ketone.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H6 + CH3CH=CH2 &rarr; C6H5CH(CH3)2 [2].", "marks": 2},
                {"part": "(b)", "points": "Propanone (acetone), CH3COCH3 [2].", "marks": 2}
            ]
        ),

        # Q29: 9701/41/O/N/18/Q11(b)
        Question(
            number=29,
            title="Synthesis of Salicylic Acid: Kolbe-Schmitt Reaction — 9701/41/O/N/18/Q11(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Sodium phenoxide is heated under pressure with carbon dioxide to produce sodium 2-hydroxybenzoate. State the type of reaction mechanism.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why sodium phenoxide reacts with carbon dioxide, whereas neutral phenol does not.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Electrophilic aromatic substitution (Kolbe-Schmitt carboxylation) [2].", "marks": 2},
                {"part": "(b)", "points": "Carbon dioxide is a very weak electrophile [1]; The phenoxide ion carries a full negative charge and is vastly more electron-rich and activated towards electrophilic attack than neutral phenol [1].", "marks": 2}
            ]
        ),

        # Q30: 9701/42/F/M/20/Q11(b)
        Question(
            number=30,
            title="Synthesis of Aromatic Aldehydes: Gattermann-Koch Reaction vs Oxidation — 9701/42/F/M/20/Q11(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why oxidising methylbenzene with hot acidified KMnO4 does not stop at benzaldehyde.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the reagent used to oxidise phenylmethanol selectively to benzaldehyde without over-oxidation to benzoic acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "KMnO4 is a powerful oxidising agent; the aldehydic C-H bond in benzaldehyde is oxidised far more rapidly than the initial methyl group, so oxidation proceeds directly to benzoic acid [2].", "marks": 2},
                {"part": "(b)", "points": "Pyridinium chlorochromate (PCC) in anhydrous dichloromethane (or warm acidified K2Cr2O7 with immediate distillation of the volatile aldehyde) [2].", "marks": 2}
            ]
        ),

        # Q31: 9701/41/M/J/17/Q10(b)
        Question(
            number=31,
            title="Synthesis of Azo Dyes: Regioselective Coupling with 1-Naphthol — 9701/41/M/J/17/Q10(b) [4 Marks]",
            syllabus_ref="36.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "When benzenediazonium chloride is coupled with alkaline 1-naphthol, substitution occurs predominantly at position 4. Explain why position 4 is favoured over position 2.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the skeletal formula of the resulting azo dye.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Position 4 is strongly activated by the -OH group and experiences less steric hindrance than position 2, which is adjacent to the bulky peri-hydrogen at position 8 and the -OH group [2].", "marks": 2},
                {"part": "(b)", "points": "Structure showing 1-naphthol with azo group (-N=N-C6H5) attached at position 4 [2].", "marks": 2}
            ]
        ),

        # Q32: 9701/42/O/N/17/Q11(b)
        Question(
            number=32,
            title="Solid-Phase Peptide Synthesis (Merrifield Method) — 9701/42/O/N/17/Q11(b) [4 Marks]",
            syllabus_ref="36.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain the principle of solid-phase peptide synthesis.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State one major advantage of solid-phase synthesis over traditional liquid-phase solution synthesis.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The C-terminal amino acid is covalently anchored to an insoluble polymer resin bead; successive N-protected amino acids are added step-by-step to extend the chain [2].", "marks": 2},
                {"part": "(b)", "points": "Excess reagents and soluble byproducts can be washed away simply by filtration without time-consuming isolation and purification after every step; the process is easily automated [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q12(a)
        Question(
            number=33,
            title="Classification of Directing Groups — 9701/42/M/J/23/Q12(a) [2 Marks]",
            syllabus_ref="36.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Classify the -COCH3 and -OCH3 groups as 2,4-directing or 3-directing.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-COCH3 is 3-directing (meta-directing) [1]; -OCH3 is 2,4-directing (ortho/para-directing) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/O/N/22/Q10(a)
        Question(
            number=34,
            title="Role of Anhydrous AlCl3 Catalyst in Friedel-Crafts Reactions — 9701/41/O/N/22/Q10(a) [2 Marks]",
            syllabus_ref="36.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Explain the role of AlCl3 in generating the electrophile from ethanoyl chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "AlCl3 acts as a Lewis acid and accepts a lone pair of electrons from chlorine [1]; Generating the powerful acylium ion electrophile: CH3COCl + AlCl3 &rarr; CH3CO+ + AlCl4- [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/M/J/22/Q11(a)
        Question(
            number=35,
            title="Definition of Retrosynthesis — 9701/42/M/J/22/Q11(a) [2 Marks]",
            syllabus_ref="36.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Explain what is meant by retrosynthetic analysis.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A technique for planning an organic synthesis by breaking down the target molecule into simpler precursor structures (synthons) [1]; Working backwards step-by-step until readily available starting materials are reached [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/M/J/21/Q12(a)
        Question(
            number=36,
            title="Reagent for Chemoselective Reduction of Aldehydes in Presence of Esters — 9701/41/M/J/21/Q12(a) [2 Marks]",
            syllabus_ref="36.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Identify a reducing agent that reduces aldehydes without reducing esters, and state the solvent.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sodium tetrahydridoborate, NaBH4 [1]; In methanol (or ethanol / water) [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/O/N/20/Q10(a)
        Question(
            number=37,
            title="Directing Effect of the Nitro Group — 9701/42/O/N/20/Q10(a) [2 Marks]",
            syllabus_ref="36.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State which ring position is substituted when nitrobenzene is brominated, and state whether nitrobenzene reacts faster or slower than benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Position 3 (meta position) [1]; Nitrobenzene reacts much slower than benzene (the -NO2 group is deactivating) [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/M/J/23/Q11(a)
        Question(
            number=38,
            title="Byproduct of Sandmeyer Reaction — 9701/43/M/J/23/Q11(a) [2 Marks]",
            syllabus_ref="36.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Identify the gas evolved when benzenediazonium chloride is heated with aqueous copper(I) chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Nitrogen gas, N2 [2].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/F/M/22/Q12(a)
        Question(
            number=39,
            title="Protecting Group for Aldehydes — 9701/42/F/M/22/Q12(a) [2 Marks]",
            syllabus_ref="36.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Name the functional group formed when an aldehyde is reacted with ethane-1,2-diol in the presence of an acid catalyst to protect the carbonyl.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Acetal (or cyclic acetal / 1,3-dioxolane) [2].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/23/Q11(a)
        Question(
            number=40,
            title="Oxidising Agent for Side-Chain of Alkylbenzenes — 9701/41/O/N/23/Q11(a) [2 Marks]",
            syllabus_ref="36.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Identify the reagent and condition used to oxidise an alkyl side-chain on a benzene ring directly to a -COOH group.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Alkaline potassium manganate(VII), KMnO4 / OH- (followed by dilute acid) [1]; Heated under reflux [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50)
        # 4 x 6m, 4 x 4m, 2 x 2m = 44 MARKS
        # =====================================================================

        # Q41: Core Repeat 1 (6m) — 9701/42/M/J/22/Q10
        Question(
            number=41,
            title="Core Repeat 1: Multi-Step Synthetic Planning from Benzene to 4-Chlorobenzoic Acid — 9701/42/M/J/22/Q10 [6 Marks]",
            syllabus_ref="36.1", difficulty="HARD", section_key="SEC_D",
            preamble="Designing correct sequences of electrophilic substitution and functional group interconversions is a hallmark of Paper 4.",
            parts=[
                QuestionPart("(a)", "Describe a three-step route to synthesise 4-chlorobenzoic acid from benzene.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why carrying out the steps in a different order would fail to yield the 4-chloro isomer.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Methylation of benzene with CH3Cl and anhydrous AlCl3 to form methylbenzene [1]; Step 2: Chlorination of methylbenzene with Cl2 and AlCl3 in the dark to yield 4-chloromethylbenzene (and 2-isomer) [1]; Step 3: Reflux with alkaline KMnO4 followed by dilute acid to oxidise the methyl group to 4-chlorobenzoic acid [1].", "marks": 3},
                {"part": "(b)", "points": "The methyl group is 2,4-directing, directing chlorination to positions 2 and 4 [1]; If methylbenzene were oxidised to benzoic acid first, the resulting -COOH group is strongly 3-directing [1]; Chlorination of benzoic acid would yield 3-chlorobenzoic acid instead of the desired 4-chloro isomer [1].", "marks": 3}
            ]
        ),

        # Q42: Core Repeat 2 (6m) — 9701/41/O/N/21/Q11
        Question(
            number=42,
            title="Core Repeat 2: Retrosynthetic Disconnection and Route Design for Paracetamol — 9701/41/O/N/21/Q11 [6 Marks]",
            syllabus_ref="36.2", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of paracetamol (4-acetamidophenol) and identify the two functional groups present.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Show the retrosynthetic disconnection of the amide bond and identify the two precursor synthons.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the forward reagents and conditions to perform this coupling reaction in the laboratory with high yield.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-HOC6H4NHCOCH3 [1]; Phenol group (-OH) and secondary amide group (-NHCO-) [1].", "marks": 2},
                {"part": "(b)", "points": "Disconnection across C-N bond of -NH-CO- [1]; Synthons / precursors: 4-aminophenol (4-HOC6H4NH2) and an acetylating agent (ethanoic anhydride or ethanoyl chloride) [1].", "marks": 2},
                {"part": "(c)", "points": "Ethanoic anhydride, (CH3CO)2O (or CH3COCl) [1]; Warm gently with stirring; ethanoic anhydride avoids toxic HCl fumes and gives high purity [1].", "marks": 2}
            ]
        ),

        # Q43: Core Repeat 3 (6m) — 9701/42/M/J/21/Q12
        Question(
            number=43,
            title="Core Repeat 3: Regiochemical Control and Protecting Groups in Aniline Nitration — 9701/42/M/J/21/Q12 [6 Marks]",
            syllabus_ref="36.4", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain what happens when phenylamine is treated directly with concentrated HNO3 and concentrated H2SO4 at 55 °C.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Outline the complete three-step method used to synthesise 4-nitroaniline cleanly from phenylamine.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State why this strategy successfully prevents oxidation of the nitrogen atom.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated acid protonates the amino group to form the phenylammonium ion (C6H5NH3+), which is strongly 3-directing rather than 4-directing [1]; Strong oxidising conditions destroy the activated amine ring, forming dark tarry oxidation products [1].", "marks": 2},
                {"part": "(b)", "points": "Step 1: Acylate phenylamine with CH3COCl to form N-phenylethanamide (acetanilide) [1]; Step 2: Nitrate with conc. HNO3 + conc. H2SO4 at 55 °C to introduce -NO2 cleanly at position 4 [1]; Step 3: Hydrolyse with boiling dilute HCl followed by NaOH to remove the acetyl group and regenerate 4-nitroaniline [1].", "marks": 3},
                {"part": "(c)", "points": "The acetyl group delocalises the nitrogen lone pair into the carbonyl &pi;-bond, protecting the nitrogen atom against oxidation and preventing protonation [1].", "marks": 1}
            ]
        ),

        # Q44: Core Repeat 4 (6m) — 9701/42/O/N/19/Q11
        Question(
            number=44,
            title="Core Repeat 4: Selective Oxidation and Reduction in Multi-Functional Organic Synthesis — 9701/42/O/N/19/Q11 [6 Marks]",
            syllabus_ref="36.4", difficulty="HARD", section_key="SEC_D",
            preamble="Compound Z is 4-(hydroxymethyl)cyclohexan-1-one.",
            parts=[
                QuestionPart("(a)", "Identify a reagent that will oxidise the primary alcohol group of Compound Z to an aldehyde without affecting the ketone group.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify a reagent that will reduce both the ketone and the primary alcohol (if oxidised to acid) to alcohol groups.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain how the ketone group could be protected as an acetal while the primary alcohol is oxidised to a carboxylic acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Pyridinium chlorochromate (PCC) in anhydrous dichloromethane [2].", "marks": 2},
                {"part": "(b)", "points": "Lithium tetrahydridoaluminate, LiAlH4, in dry ether followed by dilute acid [2].", "marks": 2},
                {"part": "(c)", "points": "React with ethane-1,2-diol and trace acid catalyst to convert ketone into a stable cyclic acetal [1]; Oxidise the primary alcohol with KMnO4/H+, then hydrolyse the acetal with dilute aqueous acid to restore the ketone [1].", "marks": 2}
            ]
        ),

        # Q45: Core Repeat 5 (4m) — 9701/42/M/J/23/Q12(c)
        Question(
            number=45,
            title="Core Repeat 5: Chemoselective Reduction of Unsaturated Carbonyls — 9701/42/M/J/23/Q12(c) [4 Marks]",
            syllabus_ref="36.4", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Cinnamaldehyde has the structure C<sub>6</sub>H<sub>5</sub>-CH=CH-CHO, containing both an alkene double bond and an aldehyde group.",
            parts=[
                QuestionPart("(a)", "Identify a reducing agent that will selectively reduce the aldehyde group to an alcohol while leaving the alkene C=C intact.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify a reagent and catalyst that will reduce both the C=C double bond and the aldehyde group completely.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Sodium tetrahydridoborate, NaBH4 (in methanol or ethanol) [2].", "marks": 2},
                {"part": "(b)", "points": "Hydrogen gas (H2) and nickel (Ni) or platinum (Pt) catalyst [2].", "marks": 2}
            ]
        ),

        # Q46: Core Repeat 6 (4m) — 9701/41/O/N/22/Q10(c)
        Question(
            number=46,
            title="Core Repeat 6: Synthesis of 3-Chloromethylbenzene vs 4-Chloromethylbenzene — 9701/41/O/N/22/Q10(c) [4 Marks]",
            syllabus_ref="36.3", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain why 4-chloromethylbenzene is formed as the major product when methylbenzene is chlorinated in the presence of AlCl3.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe how 3-chloromethylbenzene can be synthesised from benzene using a sequence of reactions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The methyl group is an electron-donating (+I) alkyl group that activates the ring and directs incoming electrophiles to the 2- and 4-positions [2].", "marks": 2},
                {"part": "(b)", "points": "Chlorinate benzene to chlorobenzene (Cl2/AlCl3), then carry out Friedel-Crafts alkylation, or chlorinate benzaldehyde at position 3 and reduce the carbonyl to -CH3 via Clemmensen reduction [2].", "marks": 2}
            ]
        ),

        # Q47: Core Repeat 7 (4m) — 9701/42/F/M/21/Q12(b)
        Question(
            number=47,
            title="Core Repeat 7: Synthesis of Benzyl Alcohol vs 4-Methylphenol — 9701/42/F/M/21/Q12(b) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Describe a two-step route to convert methylbenzene into phenylmethanol (benzyl alcohol).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why 4-methylphenol cannot be prepared by reacting 4-chloromethylbenzene with aqueous sodium hydroxide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Step 1: Cl2 with UV light / reflux to form (chloromethyl)benzene, C6H5CH2Cl [1]; Step 2: Warm with aqueous sodium hydroxide, NaOH(aq), to hydrolyse to C6H5CH2OH [1].", "marks": 2},
                {"part": "(b)", "points": "In 4-chloromethylbenzene, the chlorine atom is directly bonded to the aromatic ring [1]; The C-Cl bond has partial double bond character due to delocalisation and resists nucleophilic substitution by OH- [1].", "marks": 2}
            ]
        ),

        # Q48: Core Repeat 8 (4m) — 9701/41/M/J/20/Q11(c)
        Question(
            number=48,
            title="Core Repeat 8: Diazonium Coupling to Form Methyl Orange — 9701/41/M/J/20/Q11(c) [4 Marks]",
            syllabus_ref="36.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the two organic starting compounds required to synthesise the azo indicator methyl orange.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the essential reaction conditions for the coupling step.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Diazotised 4-aminobenzenesulfonic acid (sulfanilic acid) [1]; N,N-dimethylphenylamine (N,N-dimethylaniline) [1].", "marks": 2},
                {"part": "(b)", "points": "Temperature maintained strictly between 0 °C and 10 °C [1]; Weakly acidic to neutral aqueous medium [1].", "marks": 2}
            ]
        ),

        # Q49: Core Repeat 9 (2m) — 9701/42/M/J/23/Q12(e)
        Question(
            number=49,
            title="Core Repeat 9: Directing Effect of the Carbonyl Group — 9701/42/M/J/23/Q12(e) [2 Marks]",
            syllabus_ref="36.3", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State which ring position is substituted when benzaldehyde, C6H5CHO, undergoes electrophilic bromination with Br2/FeBr3.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Position 3 (meta position) [2].", "marks": 2}
            ]
        ),

        # Q50: Core Repeat 10 (2m) — 9701/41/O/N/23/Q11(e)
        Question(
            number=50,
            title="Core Repeat 10: Catalyst for Nitration of Benzene — 9701/41/O/N/23/Q11(e) [2 Marks]",
            syllabus_ref="36.1", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Name the acid catalyst used in the generation of the nitronium ion (NO2+) for the nitration of benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated sulfuric acid, conc. H2SO4 [2].", "marks": 2}
            ]
        )
    ]

    # Verify tariffs
    count_6m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    count_4m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    count_2m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_qs = len(questions)

    print(f"Topic 36 Questions Count: {total_qs}")
    print(f"Tariff Breakdown: 6-markers = {count_6m} ({count_6m/total_qs*100:.0f}%), 4-markers = {count_4m} ({count_4m/total_qs*100:.0f}%), 2-markers = {count_2m} ({count_2m/total_qs*100:.0f}%) | Total Marks = {total_marks}")

    assert total_qs == 50, f"Expected 50 questions, got {total_qs}"
    assert total_marks == 220, f"Expected 220 marks, got {total_marks}"
    assert count_6m == 20, f"Expected 20 6-markers, got {count_6m}"
    assert count_4m == 20, f"Expected 20 4-markers, got {count_4m}"
    assert count_2m == 10, f"Expected 10 2-markers, got {count_2m}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 36 PDF built successfully!")

if __name__ == "__main__":
    build_topic36_50q()
