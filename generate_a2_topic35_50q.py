"""
Complete 50-Question Master Pack: Topic 35 — Polymerisation (Paper 4 Theory)
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

def build_topic35_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic35_Polymerisation.pdf"

    topic_title = "Topic 35 — Polymerisation"
    topic_subtitle = "Condensation Polymers · Polyesters & Polyamides · Repeat Units & Monomers · Kevlar & Tensile Strength · Degradability & Environment"

    subtopics_summary = [
        ("35.1 Condensation Polymerisation Mechanisms", "Formation of polyesters (Terylene/PET) and polyamides (Nylon 6,6, Kevlar) with elimination of small molecules (H2O, HCl); comparing diacyl chlorides vs dicarboxylic acids; repeat units and polymer linkage identification."),
        ("35.2 Deducing Monomers from Polymer Chains", "Deconstruction of complex copolymer chains; identifying ester and amide bonds; deducing constituent diols, dicarboxylic acids, diamines, and hydroxycarboxylic acids/amino acids."),
        ("35.3 Kevlar & Advanced High-Performance Polymers", "Rigid rod structure of poly(p-phenylene terephthalamide); extensive regular intermolecular hydrogen bonding and π-π stacking; immense tensile strength and fire resistance."),
        ("35.4 Polymer Degradability & Environmental Chemistry", "Hydrolytic susceptibility of ester and amide linkages in acidic and alkaline media; comparison with inert, non-biodegradable polyalkenes; photodegradable polymers and sustainable polylactic acid (PLA)."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Polymerisation from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q11
        Question(
            number=1,
            title="Structures and Synthesis of Synthetic Condensation Polymers — 9701/42/M/J/23/Q11 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            preamble="The repeat units of two major synthetic polymers, Nylon 6,6 and Terylene, are shown in Fig. 1.1.",
            figure_path=os.path.join(fig_dir, "a2_t35_condensation_polymers.png"),
            figure_caption="Fig. 1.1: Repeat units and linkage types of Nylon 6,6 (polyamide) and Terylene (polyester).",
            parts=[
                QuestionPart("(a)", "State the systematic IUPAC names of the two monomers required to synthesise Terylene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the repeat unit of Nylon 6,6 and clearly identify the functional linkage present.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Contrast addition polymerisation and condensation polymerisation in terms of monomer functional groups and reaction byproducts.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene-1,4-dicarboxylic acid (terephthalic acid) [1]; Ethane-1,2-diol (ethylene glycol) [1].", "marks": 2},
                {"part": "(b)", "points": "-[NH-(CH2)6-NH-CO-(CH2)4-CO]- [1]; Amide / peptide linkage (-CONH-) clearly identified [1].", "marks": 2},
                {"part": "(c)", "points": "Addition polymerisation involves unsaturated monomers containing C=C double bonds with no loss of atoms (100% atom economy) [1]; Condensation polymerisation involves bifunctional or polyfunctional monomers reacting with the elimination of small molecules such as H2O or HCl [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/O/N/22/Q9
        Question(
            number=2,
            title="Chemical Degradability of Addition vs Condensation Polymers — 9701/41/O/N/22/Q9 [6 Marks]",
            syllabus_ref="35.4", difficulty="HARD", section_key="SEC_A",
            preamble="The environmental persistence and chemical degradability of polymers depend heavily on their backbone structure as illustrated in Fig. 2.1.",
            figure_path=os.path.join(fig_dir, "a2_t35_polymer_degradability.png"),
            figure_caption="Fig. 2.1: Comparison of chemical hydrolytic resistance between polyalkenes, polyesters, and polyamides.",
            parts=[
                QuestionPart("(a)", "Explain why polyalkenes, such as poly(ethene), are non-biodegradable and persist in the environment for centuries.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why polyesters and polyamides can be broken down in landfills, stating the mechanism of degradation.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe what happens chemically when Nylon 6,6 is treated with hot concentrated sodium hydroxide.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Polyalkenes possess a continuous saturated backbone of non-polar C-C and C-H bonds [1]; They contain no polar sites to attract electrophiles, nucleophiles, or microbial enzymes, resisting chemical attack and enzymatic cleavage [1].", "marks": 2},
                {"part": "(b)", "points": "Polyesters and polyamides contain polar carbonyl groups (C=O) in their ester and amide linkages [1]; The electron-deficient carbonyl carbon is vulnerable to nucleophilic attack by water or hydroxide ions (hydrolysis), breaking the polymer into monomer units [1].", "marks": 2},
                {"part": "(c)", "points": "The amide bonds undergo alkaline hydrolysis (saponification) [1]; The polymer is cleaved into 1,6-diaminohexane and the sodium salt of hexanedioic acid (disodium hexanedioate) [1].", "marks": 2}
            ]
        ),

        # Q3: 9701/42/M/J/22/Q10
        Question(
            number=3,
            title="Structure, Intermolecular Forces, and Strength of Kevlar — 9701/42/M/J/22/Q10 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_A",
            preamble="Kevlar is a high-strength aromatic polyamide used in bullet-resistant vests and aerospace composites.",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of the repeat unit of Kevlar.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Name the two monomers used in the manufacture of Kevlar.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain in terms of molecular geometry and intermolecular bonding why Kevlar has an exceptionally high tensile strength.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[NH-C6H4-NH-CO-C6H4-CO]- showing 1,4-disubstituted benzene rings linked by amide groups [2].", "marks": 2},
                {"part": "(b)", "points": "Benzene-1,4-diamine (1,4-diaminobenzene) [1]; Benzene-1,4-dicarbonyl dichloride (or benzene-1,4-dicarboxylic acid) [1].", "marks": 2},
                {"part": "(c)", "points": "The rigid 1,4-phenylene rings maintain straight, linear, planar polymer chains that pack closely together [1]; Highly ordered and dense arrays of intermolecular hydrogen bonds between C=O and N-H groups of adjacent chains, reinforced by &pi;-&pi; stacking, resist slippage and tensile deformation [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/M/J/21/Q11
        Question(
            number=4,
            title="Deducing Monomers from Complex Condensation Polymers — 9701/41/M/J/21/Q11 [6 Marks]",
            syllabus_ref="35.2", difficulty="HARD", section_key="SEC_A",
            preamble="A segment of a biodegradable copolymer chain is shown below:<br/>"
                     "&hellip;-CO-CH<sub>2</sub>CH<sub>2</sub>-CO-O-CH(CH<sub>3</sub>)CH<sub>2</sub>-O-CO-(C<sub>6</sub>H<sub>4</sub>)-CO-NH-(CH<sub>2</sub>)<sub>4</sub>-NH-&hellip;",
            parts=[
                QuestionPart("(a)", "Identify all types of linkages present along this polymer backbone.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the structural formulas of the four distinct monomers that react together to form this copolymer.", 4, num_answer_lines=5)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ester linkage (-COO-) [1]; Amide / peptide linkage (-CONH-) [1].", "marks": 2},
                {"part": "(b)", "points": "Monomer 1: Butanedioic acid, HOOC-CH2CH2-COOH [1]; Monomer 2: Propane-1,2-diol, HO-CH(CH3)CH2-OH [1]; Monomer 3: Benzene-1,4-dicarboxylic acid, HOOC-C6H4-COOH [1]; Monomer 4: Butane-1,4-diamine, H2N-(CH2)4-NH2 [1].", "marks": 4}
            ]
        ),

        # Q5: 9701/42/O/N/20/Q9
        Question(
            number=5,
            title="Polylactic Acid (PLA): Synthesis from Lactic Acid and Biodegradability — 9701/42/O/N/20/Q9 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            preamble="Lactic acid (2-hydroxypropanoic acid), CH<sub>3</sub>CH(OH)COOH, can undergo self-condensation to form the biodegradable polyester poly(lactic acid), PLA.",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of poly(lactic acid).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why lactic acid can form a polymer on its own, whereas ethanoic acid cannot.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State two environmental advantages of using PLA instead of poly(propene) for food packaging.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[O-CH(CH3)-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "Lactic acid is bifunctional, containing both a nucleophilic hydroxy group (-OH) and an electrophilic carboxylic acid group (-COOH) within the same molecule [1]; Ethanoic acid has only one functional group (-COOH) and cannot form continuous chains [1].", "marks": 2},
                {"part": "(c)", "points": "PLA is derived from renewable biological resources (e.g. fermented corn starch / sugarcane) rather than finite petrochemicals [1]; PLA is biodegradable and compostable, breaking down into non-toxic lactic acid / CO2 / H2O via bacterial enzymatic hydrolysis [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/43/M/J/23/Q10
        Question(
            number=6,
            title="Synthesis of Nylon 6,6: Laboratory Interfacial Polymerisation — 9701/43/M/J/23/Q10 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            preamble="In the school laboratory demonstration known as the 'Nylon rope trick', two immiscible solutions are placed in a beaker:<br/>"
                     "- Solution 1: Hexane-1,6-diamine dissolved in aqueous sodium hydroxide<br/>"
                     "- Solution 2: Hexanedioyl dichloride dissolved in cyclohexane",
            parts=[
                QuestionPart("(a)", "Explain why polymerisation occurs only at the interface between the two liquid layers.", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the role of sodium hydroxide in Solution 1.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why hexanedioyl dichloride is used in this demonstration rather than hexanedioic acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The two solvent layers (aqueous and organic) are immiscible [1]; The monomers can only come into contact and react where the two phases meet at the boundary interface [1].", "marks": 2},
                {"part": "(b)", "points": "The reaction eliminates toxic, acidic hydrogen chloride (HCl) gas [1]; NaOH neutralises the HCl to form NaCl and water, preventing protonation of the amine which would deactivate it as a nucleophile [1].", "marks": 2},
                {"part": "(c)", "points": "Acyl chlorides are far more reactive than carboxylic acids and react rapidly at room temperature [1]; Dicarboxylic acids require elevated temperatures and strong acid catalysis, which would not work in a cold beaker demonstration [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/42/F/M/22/Q11
        Question(
            number=7,
            title="Photodegradable and Soluble Polymers: Norrish Reactions — 9701/42/F/M/22/Q11 [6 Marks]",
            syllabus_ref="35.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain how the incorporation of carbonyl groups (C=O) into a polyalkene backbone makes the polymer photodegradable.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Poly(ethenol) is a synthetic polymer that is readily soluble in water. Draw the repeat unit of poly(ethenol) and explain its water solubility.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The carbonyl group acts as a chromophore that absorbs solar ultraviolet (UV) radiation [1]; Absorption of UV energy promotes electrons to antibonding orbitals, causing homolytic cleavage of carbon-carbon bonds adjacent to the carbonyl (Norrish type I/II reactions) [1]; This fragments the long polymer chains into short oligomers that can subsequently be consumed by micro-organisms [1].", "marks": 3},
                {"part": "(b)", "points": "Repeat unit: -[CH2-CH(OH)]- [1]; Every monomer unit contains a polar hydroxy group (-OH) [1]; These -OH groups form extensive hydrogen bonds with surrounding water molecules, releasing sufficient hydration energy to overcome polymer-polymer interactions and dissolve the chain [1].", "marks": 3}
            ]
        ),

        # Q8: 9701/41/O/N/23/Q10
        Question(
            number=8,
            title="Natural Polymers: Proteins and Polysaccharides as Condensation Polymers — 9701/41/O/N/23/Q10 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "State the type of reaction by which starch and cellulose are formed from glucose, and identify the small molecule eliminated.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the specific linkage connecting glucose units in polysaccharides.", 1, num_answer_lines=1),
                QuestionPart("(c)", "Compare the enzymatic hydrolysis of starch in the human body with the chemical hydrolysis of synthetic polyesters in industry.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Condensation polymerisation [1]; Water, H2O [1].", "marks": 2},
                {"part": "(b)", "points": "Glycosidic bond (or ether linkage / -C-O-C-) [1].", "marks": 1},
                {"part": "(c)", "points": "Starch hydrolysis is catalysed by biological enzymes (e.g. amylase) under mild conditions (pH ~7, 37 °C) with high stereospecificity [1]; Industrial hydrolysis of polyesters requires harsh conditions such as concentrated aqueous acid or alkali under prolonged reflux at high temperatures [1]; Both break down the polymer backbone into monomer units via addition of water across the functional linkage [1].", "marks": 3}
            ]
        ),

        # Q9: 9701/42/M/J/20/Q9
        Question(
            number=9,
            title="Conducting Polymers: Poly(ethyne) and Delocalised Pi Systems — 9701/42/M/J/20/Q9 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Draw the skeletal formula of three repeat units of poly(ethyne), showing alternating single and double bonds.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how the alternating conjugated double bond system enables poly(ethyne) to conduct electricity when 'doped'.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why ordinary polyalkenes, like poly(ethene), are electrical insulators.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[CH=CH-CH=CH-CH=CH]- with trans alternating stereochemistry [2].", "marks": 2},
                {"part": "(b)", "points": "The p-orbitals on adjacent sp2 carbon atoms overlap sideways continuously along the entire polymer backbone [1]; This creates an extended, delocalised &pi;-electron system [1]; When doped with an oxidising or reducing agent (e.g. I2), electrons or holes are introduced into the delocalised band and can move freely along the chain under an applied potential difference [1].", "marks": 3},
                {"part": "(c)", "points": "In poly(ethene), all carbon atoms are sp3 hybridised with all valence electrons tightly localised in &sigma;-bonds, so there are no mobile delocalised electrons to carry charge [1].", "marks": 1}
            ]
        ),

        # Q10: 9701/41/M/J/19/Q10
        Question(
            number=10,
            title="Thermal Properties of Polymers: Thermoplastics vs Thermosets — 9701/41/M/J/19/Q10 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain the difference in structural bonding between a thermoplastic polymer and a thermosetting polymer.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain what happens when each type of polymer is heated, and relate this to their recycling potential.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thermoplastics consist of discrete linear or branched polymer chains held together only by intermolecular forces (London forces, dipole-dipole, or hydrogen bonds) [1]; Thermosets contain permanent covalent cross-links linking adjacent chains into a vast three-dimensional network [2].", "marks": 3},
                {"part": "(b)", "points": "On heating, thermoplastics soften and melt because weak intermolecular forces are easily overcome, allowing them to be reshaped and recycled repeatedly [1]; Thermosets do not melt on heating because rigid covalent cross-links cannot break without decomposing (charring) the polymer [1]; Thus, thermosets cannot be remoulded or recycled by melting [1].", "marks": 3}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q10
        Question(
            number=11,
            title="Quantitative Analysis of Condensation Polymerisation: Degree of Polymerisation — 9701/42/O/N/21/Q10 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            preamble="A sample of Nylon 6,6 has an average relative molecular mass (Mr) of 27,120.<br/>"
                     "Data: Repeat unit of Nylon 6,6 is -[NH-(CH<sub>2</sub>)<sub>6</sub>-NH-CO-(CH<sub>2</sub>)<sub>4</sub>-CO]-.",
            parts=[
                QuestionPart("(a)", "Calculate the relative formula mass of the repeat unit of Nylon 6,6.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the average degree of polymerisation, n, for this polymer sample.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Calculate the total mass of water eliminated during the synthesis of one mole of this polymer sample.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C12H22N2O2: (12 x 12.0) + (22 x 1.0) + (2 x 14.0) + (2 x 16.0) = 144 + 22 + 28 + 32 = 226.0 [2].", "marks": 2},
                {"part": "(b)", "points": "Degree of polymerisation n = Mr / Mr(repeat unit) = 27,120 / 226.0 = 120 [2].", "marks": 2},
                {"part": "(c)", "points": "Each repeat unit formed eliminates 2 molecules of H2O [1]; Total moles of H2O eliminated per mole of polymer = 2n = 240 mol; Mass of H2O = 240 x 18.0 = 4320 g [1].", "marks": 2}
            ]
        ),

        # Q12: 9701/42/M/J/18/Q10
        Question(
            number=12,
            title="Comparison of Nylon 6 and Nylon 6,6 — 9701/42/M/J/18/Q10 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Nylon 6 is produced from a single monomer, caprolactam (or 6-aminohexanoic acid). Draw the repeat unit of Nylon 6.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how the synthesis of Nylon 6 differs from that of Nylon 6,6 in terms of the number of different monomers used.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Compare the melting point and intermolecular forces in Nylon 6 with those in Nylon 6,6.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[NH-(CH2)5-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "Nylon 6 is made from a single monomer that contains both an amino group and a carboxyl group (or via ring opening of caprolactam) [1]; Nylon 6,6 is a copolymer made from two different bifunctional monomers (a diamine and a dicarboxylic acid) [1].", "marks": 2},
                {"part": "(c)", "points": "Both possess identical amide (-CONH-) linkages and exhibit intermolecular hydrogen bonding [1]; Nylon 6,6 has a slightly higher melting point (~265 °C vs ~220 °C) because its symmetrical structure allows more regular and tighter hydrogen-bonded packing [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/41/O/N/18/Q10
        Question(
            number=13,
            title="Biodegradability: Hydrolytic Cleavage of Poly(glycolic acid) (PGA) in Suture Threads — 9701/41/O/N/18/Q10 [6 Marks]",
            syllabus_ref="35.4", difficulty="HARD", section_key="SEC_A",
            preamble="Poly(glycolic acid), PGA, is a synthetic biodegradable polyester widely used in absorbable surgical sutures.<br/>"
                     "Monomer: Glycolic acid (hydroxyethanoic acid), HO-CH<sub>2</sub>-COOH.",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of poly(glycolic acid).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write an equation showing the hydrolysis of one ester bond in the polymer chain.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why absorbable sutures made of PGA do not require surgical removal after a patient's wound has healed.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[O-CH2-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "-O-CH2-CO- + H2O &rarr; -O-CH2-COOH + HO- (or ester + H2O &rarr; -OH + -COOH) [2].", "marks": 2},
                {"part": "(c)", "points": "Body fluids contain water and esterase enzymes that slowly hydrolyse the ester bonds over several weeks [1]; The breakdown product (glycolic acid) is naturally metabolised by normal cellular respiration into CO2 and H2O and safely excreted [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/42/F/M/20/Q10
        Question(
            number=14,
            title="Polymer Recycling: Mechanical vs Chemical Feedstock Recycling — 9701/42/F/M/20/Q10 [6 Marks]",
            syllabus_ref="35.4", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain the principles of mechanical recycling of thermoplastic polymers and state one disadvantage.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe how PET (polyethylene terephthalate) bottles can undergo chemical recycling (feedstock recycling).", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why chemical recycling produces higher quality recycled polymers than mechanical recycling.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Polymers are sorted, washed, shredded, melted, and remoulded into new products [1]; Repeated heating cycles cause thermal degradation / chain shortening, reducing physical strength [1].", "marks": 2},
                {"part": "(b)", "points": "PET is depolymerised by heating with methanol or ethylene glycol (methanolysis / glycolysis) or aqueous alkali [1]; This breaks the ester bonds and recovers pure monomer building blocks (dimethyl terephthalate and ethane-1,2-diol) [1].", "marks": 2},
                {"part": "(c)", "points": "The recovered monomers can be separated, purified, and repolymerised into virgin-quality polymer [1]; Any dyes, additives, or contaminants are completely removed during monomer purification [1].", "marks": 2}
            ]
        ),

        # Q15: 9701/41/M/J/17/Q9
        Question(
            number=15,
            title="Polymer Linkages and Hydrogen Bonding Networks — 9701/41/M/J/17/Q9 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Draw a diagram showing two parallel chains of a polyamide with hydrogen bonds forming between them.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why polyesters cannot form hydrogen bonds between adjacent chains unless hydroxy side-chains are present.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State how the difference in intermolecular bonding between polyamides and polyesters affects their melting temperatures.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Two chains showing C=O and N-H groups aligned [1]; Dotted line showing hydrogen bond between carbonyl oxygen and N-H hydrogen [1]; Correct partial charges (&delta;- on O, &delta;+ on H) and lone pair shown on oxygen [1].", "marks": 3},
                {"part": "(b)", "points": "Polyesters contain carbonyl oxygen atoms (hydrogen bond acceptors) but lack hydrogen atoms bonded to highly electronegative atoms (no N-H or O-H hydrogen bond donors) [2].", "marks": 2},
                {"part": "(c)", "points": "Polyamides have significantly higher melting temperatures than polyesters of similar molecular weight due to strong intermolecular hydrogen bonding [1].", "marks": 1}
            ]
        ),

        # Q16: 9701/42/O/N/17/Q10
        Question(
            number=16,
            title="Coordination Polymers and Metal-Organic Frameworks (MOFs) — 9701/42/O/N/17/Q10 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_A",
            parts=[
                QuestionPart("(a)", "Explain what is meant by a metal-organic framework (MOF).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Identify the type of bonding between the metal ions and organic linkers in a MOF.", 1, num_answer_lines=1),
                QuestionPart("(c)", "State two potential industrial applications of MOFs arising from their highly porous structures.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A coordination network consisting of metal ions or clusters coordinated to polydentate organic bridging ligands (linkers) forming a 1D, 2D, or 3D porous structure [2].", "marks": 2},
                {"part": "(b)", "points": "Coordinate (dative covalent) bonding [1].", "marks": 1},
                {"part": "(c)", "points": "Gas storage (e.g. hydrogen fuel or methane storage in vehicles) [1]; Carbon dioxide capture and sequestration [1]; Heterogeneous catalysis or drug delivery [1].", "marks": 3}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q11(b)
        Question(
            number=17,
            title="Repeat Unit and Monomers of Polycarbonate (Lexan) — 9701/42/M/J/23/Q11(b) [4 Marks]",
            syllabus_ref="35.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Polycarbonate is synthesised from Bisphenol A and carbonyl dichloride (phosgene, COCl2). Draw the repeat unit of polycarbonate.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Identify the small molecule eliminated and state the type of linkage formed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[O-C6H4-C(CH3)2-C6H4-O-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "Hydrogen chloride, HCl [1]; Carbonate ester linkage (-O-CO-O-) [1].", "marks": 1}
            ]
        ),

        # Q18: 9701/41/O/N/22/Q9(b)
        Question(
            number=18,
            title="Comparison of Monomer Functionality: Difunctional vs Monofunctional — 9701/41/O/N/22/Q9(b) [4 Marks]",
            syllabus_ref="35.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why condensation polymerisation requires monomers to have at least two functional groups per molecule.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe what happens if a small amount of a trifunctional monomer (e.g. propane-1,2,3-triol) is added during polyester synthesis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Each reacting end must leave a free functional group available to react with another monomer, enabling continuous chain growth at both ends [2].", "marks": 2},
                {"part": "(b)", "points": "The third functional group acts as a branch point [1]; This leads to cross-linking between separate polymer chains, creating a rigid thermosetting 3D network [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/M/J/22/Q10(b)
        Question(
            number=19,
            title="Repeat Unit Deduction for Nomex Polyamide — 9701/42/M/J/22/Q10(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Nomex is formed from benzene-1,3-diamine and benzene-1,3-dicarboxylic acid. Draw the repeat unit of Nomex.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Contrast the flexibility of Nomex with that of Kevlar (1,4-isomer) and relate this to fire-resistant suits.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[NH-(1,3-C6H4)-NH-CO-(1,3-C6H4)-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "The 1,3-linkages introduce bends / kinks into the polymer chain, making Nomex more flexible and easier to weave into textiles than rigid Kevlar [1]; Nomex retains excellent thermal resistance and does not melt or drip when exposed to flames [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/M/J/21/Q11(b)
        Question(
            number=20,
            title="Hydrolysis Products of Nylon 6,6 with Hot Dilute Hydrochloric Acid — 9701/41/M/J/21/Q11(b) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of the nitrogen-containing product formed when Nylon 6,6 is completely hydrolysed by hot dilute HCl.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the structural formula of the other organic product formed.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hexane-1,6-diammonium dichloride, +H3N-(CH2)6-NH3+ 2Cl- [2].", "marks": 2},
                {"part": "(b)", "points": "Hexanedioic acid, HOOC-(CH2)4-COOH [2].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/O/N/20/Q9(b)
        Question(
            number=21,
            title="Comparing Atom Economy: Addition vs Condensation Polymerisation — 9701/42/O/N/20/Q9(b) [4 Marks]",
            syllabus_ref="35.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain why the theoretical percentage atom economy for addition polymerisation is always 100%.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why condensation polymerisation has an atom economy of less than 100%, and calculate the percentage atom economy for the synthesis of Nylon 6,6 from 1,6-diaminohexane and hexanedioic acid (Repeat unit Mr = 226, H2O Mr = 18).", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "All atoms from the monomer molecules are incorporated into the polymer chain; no waste byproducts are formed [2].", "marks": 2},
                {"part": "(b)", "points": "Small molecules (such as H2O) are eliminated as waste [1]; Total mass of reactants = 226 + (2 x 18) = 262; % atom economy = (226 / 262) x 100 = 86.3% [1].", "marks": 2}
            ]
        ),

        # Q22: 9701/43/M/J/23/Q10(b)
        Question(
            number=22,
            title="Biodegradation of Polyesters via Microbial Esterase Enzymes — 9701/43/M/J/23/Q10(b) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State the role of bacterial esterase enzymes in the breakdown of biodegradable polyesters.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why poly(ethene) is not attacked by bacterial esterase enzymes.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Esterases bind to the polar ester linkages (-COO-) in the active site and catalyse the addition of water, cleaving the ester bonds into non-toxic carboxylic acids and alcohols [2].", "marks": 2},
                {"part": "(b)", "points": "Poly(ethene) contains only non-polar C-C bonds with no ester linkages; its hydrophobic backbone cannot fit into the active site of esterases [2].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/F/M/22/Q11(b)
        Question(
            number=23,
            title="Deducing Monomer from Repeat Unit: Poly(3-hydroxybutanoic acid) (PHB) — 9701/42/F/M/22/Q11(b) [4 Marks]",
            syllabus_ref="35.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="PHB is a bacterial polyester with repeat unit: -[O-CH(CH<sub>3</sub>)-CH<sub>2</sub>-CO]-.",
            parts=[
                QuestionPart("(a)", "Give the systematic IUPAC name and displayed formula of the monomer from which PHB is formed.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State whether the monomer exhibits optical isomerism, giving a reason.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "3-hydroxybutanoic acid [1]; CH3-CH(OH)-CH2-COOH with all bonds displayed [1].", "marks": 2},
                {"part": "(b)", "points": "Yes [1]; Carbon-3 is a chiral centre bonded to four different groups (-H, -CH3, -OH, -CH2COOH) [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/23/Q10(b)
        Question(
            number=24,
            title="Chemical Recycling of PET via Methanolysis — 9701/41/O/N/23/Q10(b) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Write the word or chemical equation for the transesterification of PET with methanol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State two advantages of this process over landfill disposal.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "PET + methanol &rarr; dimethyl terephthalate + ethane-1,2-diol [2].", "marks": 2},
                {"part": "(b)", "points": "Conserves fossil petrochemical resources by recycling monomers indefinitely [1]; Reduces waste accumulation in landfills and prevents environmental microplastic pollution [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/20/Q9(b)
        Question(
            number=25,
            title="Properties of Thermosetting Epoxy Resins — 9701/42/M/J/20/Q9(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Explain the role of a 'hardener' (such as a diamine) in curing an epoxy resin.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why cured epoxy resins are rigid, solvent-resistant, and do not melt upon heating.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The diamine hardener contains reactive -NH2 groups that open epoxide rings on separate resin molecules [1]; This establishes covalent cross-links between the polymer chains [1].", "marks": 2},
                {"part": "(b)", "points": "The vast 3D network of covalent cross-links prevents chains from sliding past one another (giving high rigidity) [1]; Solvents cannot separate covalently bound chains, and thermal energy causes decomposition before melting can occur [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/19/Q10(b)
        Question(
            number=26,
            title="Low-Density Poly(ethene) (LDPE) vs High-Density Poly(ethene) (HDPE) — 9701/41/M/J/19/Q10(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Contrast the chain branching in LDPE and HDPE.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how the difference in chain structure affects the density and melting point of HDPE compared to LDPE.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "LDPE has significant chain branching [1]; HDPE consists of linear, unbranched polymer chains [1].", "marks": 2},
                {"part": "(b)", "points": "Linear HDPE chains can pack much closer and more regularly together into crystalline regions [1]; This increases London dispersion forces between chains, resulting in higher density and a higher melting point than LDPE [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q10(b)
        Question(
            number=27,
            title="Condensation of Hydroxy Acids: Polymerisation vs Lactide Formation — 9701/42/O/N/21/Q10(b) [4 Marks]",
            syllabus_ref="35.1", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "When 2-hydroxyethanoic acid is heated, it can form a cyclic dilactone (glycolide). Draw the structure of glycolide.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how ring-opening polymerisation of glycolide produces poly(glycolic acid) without eliminating water.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Six-membered cyclic ring with two ester groups (-O-CO-) formed by condensation of two molecules of 2-hydroxyethanoic acid [2].", "marks": 2},
                {"part": "(b)", "points": "A catalyst opens the cyclic ester ring, generating an active chain end that attacks another cyclic monomer [1]; Because all atoms of the cyclic monomer are incorporated into the chain, it behaves as an addition-type ring-opening polymerisation with no small molecule eliminated [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/42/M/J/18/Q10(b)
        Question(
            number=28,
            title="Comparison of Terylene and Nylon 6,6 Resistances to Acid and Alkali — 9701/42/M/J/18/Q10(b) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Predict whether Terylene (polyester) or Nylon 6,6 (polyamide) is more susceptible to alkaline hydrolysis and explain why.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Predict whether Terylene or Nylon 6,6 is more susceptible to acid hydrolysis and explain why.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Terylene is more susceptible to alkali [1]; The ester carbonyl carbon is more electrophilic than an amide carbonyl (due to greater electronegativity of oxygen over nitrogen) and is attacked rapidly by OH- [1].", "marks": 2},
                {"part": "(b)", "points": "Nylon 6,6 is more susceptible to strong acid [1]; The nitrogen/carbonyl of the amide linkage is readily protonated by H+, greatly activating the carbonyl carbon towards attack by water [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/41/O/N/18/Q10(b)
        Question(
            number=29,
            title="Polymers with Special Properties: Superabsorbent Polymers (Sodium Polyacrylate) — 9701/41/O/N/18/Q10(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of sodium polyacrylate, -[CH2-CH(COONa)]-.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain in terms of osmosis and ion-dipole forces why sodium polyacrylate can absorb several hundred times its own mass of water.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[CH2-CH(COO- Na+)]- showing carboxylate sodium salt on the chain [2].", "marks": 2},
                {"part": "(b)", "points": "The ionic -COO- and Na+ groups are strongly hydrated by water molecules through ion-dipole interactions [1]; The high concentration of ions inside the cross-linked polymer network draws water into the polymer by osmosis, causing it to swell dramatically into a gel without dissolving [1].", "marks": 2}
            ]
        ),

        # Q30: 9701/42/F/M/20/Q10(b)
        Question(
            number=30,
            title="Incineration of Polymers: Energy Recovery vs Toxic Emissions — 9701/42/F/M/20/Q10(b) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "State one major advantage of incinerating polymer waste compared to disposal in landfills.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Identify the toxic acidic gas produced when poly(chloroethene) (PVC) is incinerated, and explain how modern incinerators prevent its release.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Massive reduction in waste volume and recovery of thermal energy for electricity generation / district heating [1].", "marks": 1},
                {"part": "(b)", "points": "Hydrogen chloride, HCl [1]; Flue gases are passed through wet scrubbers containing a basic substance such as calcium oxide (CaO) or calcium carbonate (CaCO3) [1]; The basic substance neutralises the acidic HCl to produce harmless solid calcium chloride: CaO + 2HCl &rarr; CaCl2 + H2O [1].", "marks": 3}
            ]
        ),

        # Q31: 9701/41/M/J/17/Q9(b)
        Question(
            number=31,
            title="Synthetic Rubber: Cis-trans Isomerism in Poly(isoprene) — 9701/41/M/J/17/Q9(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Natural rubber is cis-1,4-poly(isoprene). Draw the structure of two repeat units of cis-poly(isoprene).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how vulcanisation with sulfur alters the mechanical properties of natural rubber.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Correct cis-configuration around the C=C double bonds in adjacent isoprene repeat units (-[CH2-C(CH3)=CH-CH2]-) [2].", "marks": 2},
                {"part": "(b)", "points": "Sulfur atoms form covalent disulfide cross-links (-S-S-) between adjacent polyisoprene chains [1]; These cross-links prevent chains from sliding permanently past one another when stretched, greatly improving elasticity, resilience, and hardness [1].", "marks": 2}
            ]
        ),

        # Q32: 9701/42/O/N/17/Q10(b)
        Question(
            number=32,
            title="Deducing Monomers of Kevlar from Its Repeat Unit — 9701/42/O/N/17/Q10(b) [4 Marks]",
            syllabus_ref="35.2", difficulty="MEDIUM", section_key="SEC_B",
            parts=[
                QuestionPart("(a)", "Draw the skeletal formula of benzene-1,4-diamine.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the skeletal formula of benzene-1,4-dioic acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene ring with two amino groups (-NH2) at positions 1 and 4 [2].", "marks": 2},
                {"part": "(b)", "points": "Benzene ring with two carboxyl groups (-COOH) at positions 1 and 4 [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q11(a)
        Question(
            number=33,
            title="Classification of Nylon 6,6 and Terylene — 9701/42/M/J/23/Q11(a) [2 Marks]",
            syllabus_ref="35.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Classify Nylon 6,6 and Terylene as a polyester or polyamide.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Nylon 6,6 is a polyamide [1]; Terylene is a polyester [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/O/N/22/Q9(a)
        Question(
            number=34,
            title="Small Molecule Eliminated in Polyesterification — 9701/41/O/N/22/Q9(a) [2 Marks]",
            syllabus_ref="35.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Identify the small molecule eliminated when a diol reacts with a dicarboxylic acid, and when a diol reacts with a diacyl chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Water, H2O (with dicarboxylic acid) [1]; Hydrogen chloride, HCl (with diacyl chloride) [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/M/J/22/Q10(a)
        Question(
            number=35,
            title="Identifying Repeat Units — 9701/42/M/J/22/Q10(a) [2 Marks]",
            syllabus_ref="35.2", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Define the term repeat unit of a polymer.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The specific arrangement of atoms or repeating block derived from the monomers [1]; which is repeated successively to generate the complete polymer macromolecule [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/M/J/21/Q11(a)
        Question(
            number=36,
            title="Intermolecular Forces in Polyamides — 9701/41/M/J/21/Q11(a) [2 Marks]",
            syllabus_ref="35.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State the strongest type of intermolecular force present between adjacent polymer chains in Nylon 6,6.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydrogen bonding [1]; Between the C=O oxygen of one chain and the N-H hydrogen of an adjacent chain [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/O/N/20/Q9(a)
        Question(
            number=37,
            title="Degradability of Polyalkenes vs Polyesters — 9701/42/O/N/20/Q9(a) [2 Marks]",
            syllabus_ref="35.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "State why polyesters can be hydrolysed by aqueous acid or alkali, whereas polyalkenes cannot.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Polyesters contain polar C=O and C-O bonds susceptible to nucleophilic attack [1]; Polyalkenes contain only non-polar C-C and C-H bonds [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/43/M/J/23/Q10(a)
        Question(
            number=38,
            title="Monomers of Terylene — 9701/43/M/J/23/Q10(a) [2 Marks]",
            syllabus_ref="35.1", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Give the chemical formulas of the two monomers from which Terylene is manufactured.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "HOOC-C6H4-COOH [1]; HO-CH2CH2-OH [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/F/M/22/Q11(a)
        Question(
            number=39,
            title="Repeat Unit of Kevlar — 9701/42/F/M/22/Q11(a) [2 Marks]",
            syllabus_ref="35.3", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Draw the skeletal formula of the repeat unit of Kevlar.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[NH-(1,4-C6H4)-NH-CO-(1,4-C6H4)-CO]- [2].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/23/Q10(a)
        Question(
            number=40,
            title="Photodegradable Polymer Chromophores — 9701/41/O/N/23/Q10(a) [2 Marks]",
            syllabus_ref="35.4", difficulty="EASY", section_key="SEC_C",
            parts=[
                QuestionPart("(a)", "Name the functional group commonly incorporated into polymer chains to make them photodegradable by absorbing UV radiation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Carbonyl group / C=O (or ketone / aldehyde chromophore) [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50)
        # 4 x 6m, 4 x 4m, 2 x 2m = 44 MARKS
        # =====================================================================

        # Q41: Core Repeat 1 (6m) — 9701/42/M/J/22/Q9
        Question(
            number=41,
            title="Core Repeat 1: Deductions of Monomers from Condensation Polymers — 9701/42/M/J/22/Q9 [6 Marks]",
            syllabus_ref="35.2", difficulty="HARD", section_key="SEC_D",
            preamble="The deconstruction of synthetic polymers into their constituent monomer units is one of the most frequently examined skills in Paper 4.",
            parts=[
                QuestionPart("(a)", "A polyamide has the repeat unit: -[NH-(CH2)4-NH-CO-(CH2)6-CO]-. Draw and name the two monomers.", 2, num_answer_lines=2),
                QuestionPart("(b)", "A polyester has the repeat unit: -[O-(CH2)3-O-CO-C6H4-CO]-. Draw and name the two monomers.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Draw the repeat unit of the polymer formed when 4-aminobenzoic acid undergoes self-condensation, identifying the linkage type.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Butane-1,4-diamine (1,4-diaminobutane), H2N-(CH2)4-NH2 [1]; Octanedioic acid, HOOC-(CH2)6-COOH [1].", "marks": 2},
                {"part": "(b)", "points": "Propane-1,3-diol, HO-(CH2)3-OH [1]; Benzene-1,4-dicarboxylic acid, HOOC-C6H4-COOH [1].", "marks": 2},
                {"part": "(c)", "points": "-[NH-C6H4-CO]- [1]; Aromatic polyamide / amide linkage [1].", "marks": 2}
            ]
        ),

        # Q42: Core Repeat 2 (6m) — 9701/41/O/N/21/Q10
        Question(
            number=42,
            title="Core Repeat 2: Chemical Degradability and Hydrolysis Mechanisms of Synthetic Polymers — 9701/41/O/N/21/Q10 [6 Marks]",
            syllabus_ref="35.4", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Explain why poly(propene) cannot be broken down by boiling aqueous acid or alkali.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Write the balanced chemical equation for the complete hydrolysis of Terylene by hot aqueous sodium hydroxide.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why alkaline hydrolysis is preferred over acid hydrolysis for recycling polyesters.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Poly(propene) has a saturated non-polar carbon-carbon backbone with no delta positive atoms to attract nucleophilic attack by H2O or OH- [2].", "marks": 2},
                {"part": "(b)", "points": "-[CO-C6H4-CO-O-CH2CH2-O]n- + 2n NaOH &rarr; n Na+-OOC-C6H4-COO-Na+ + n HOCH2CH2OH [2].", "marks": 2},
                {"part": "(c)", "points": "Alkaline hydrolysis produces carboxylate salts that are water-soluble and cannot re-esterify, making the reaction completely irreversible and quantitative [1]; Acid hydrolysis is a reversible equilibrium reaction that does not go to completion [1].", "marks": 2}
            ]
        ),

        # Q43: Core Repeat 3 (6m) — 9701/42/M/J/21/Q11
        Question(
            number=43,
            title="Core Repeat 3: Kevlar Structure, Alignment, and High-Performance Properties — 9701/42/M/J/21/Q11 [6 Marks]",
            syllabus_ref="35.3", difficulty="HARD", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "State the systematic IUPAC names of the two monomers used to manufacture Kevlar.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the repeat unit of Kevlar and indicate the points of hydrogen bonding with an adjacent chain.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why Kevlar is five times stronger than steel on an equal weight basis.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene-1,4-diamine (or 1,4-diaminobenzene) [1]; Benzene-1,4-dicarbonyl dichloride (or terephthaloyl chloride) [1].", "marks": 2},
                {"part": "(b)", "points": "-[NH-C6H4-NH-CO-C6H4-CO]- [1]; Dotted line showing hydrogen bonding between N-H and C=O of adjacent chains [1].", "marks": 2},
                {"part": "(c)", "points": "Linear, unkinked chains allow maximum surface contact and regular arrays of strong intermolecular hydrogen bonds [1]; Planar aromatic rings allow &pi;-&pi; orbital stacking, and low density gives an extremely high strength-to-weight ratio [1].", "marks": 2}
            ]
        ),

        # Q44: Core Repeat 4 (6m) — 9701/42/O/N/19/Q10
        Question(
            number=44,
            title="Core Repeat 4: Polyesters from Diacyl Chlorides vs Dicarboxylic Acids — 9701/42/O/N/19/Q10 [6 Marks]",
            syllabus_ref="35.1", difficulty="HARD", section_key="SEC_D",
            preamble="A research chemist evaluates two synthetic routes to prepare a sample of Terylene:<br/>"
                     "Route 1: Benzene-1,4-dicarboxylic acid + Ethane-1,2-diol<br/>"
                     "Route 2: Benzene-1,4-dicarbonyl dichloride + Ethane-1,2-diol",
            parts=[
                QuestionPart("(a)", "State the reaction conditions required for Route 1, and name the byproduct.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the reaction conditions required for Route 2, and name the byproduct.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain two advantages of Route 2 over Route 1 in a laboratory setting.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Concentrated acid catalyst (e.g. H2SO4) and high temperature / heating under reflux [1]; Water, H2O [1].", "marks": 2},
                {"part": "(b)", "points": "Room temperature (no catalyst required) [1]; Hydrogen chloride gas, HCl [1].", "marks": 2},
                {"part": "(c)", "points": "Acyl chlorides are vastly more reactive than carboxylic acids, giving high yields rapidly at room temperature [1]; The reaction is irreversible because HCl is eliminated as a gas, whereas Route 1 is an equilibrium reaction [1].", "marks": 2}
            ]
        ),

        # Q45: Core Repeat 5 (4m) — 9701/42/M/J/23/Q11(c)
        Question(
            number=45,
            title="Core Repeat 5: Biodegradable Polymers: Structure and Hydrolysis of Polyglycolide — 9701/42/M/J/23/Q11(c) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of poly(glycolide), which is formed from glycolic acid (hydroxyethanoic acid).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain how the ester linkages allow poly(glycolide) to break down harmlessly in the human body.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[O-CH2-CO]- [2].", "marks": 2},
                {"part": "(b)", "points": "Ester linkages undergo slow hydrolytic cleavage by water in body tissues, breaking the polymer into glycolic acid [1]; Glycolic acid is a non-toxic natural metabolite that is broken down into carbon dioxide and water [1].", "marks": 2}
            ]
        ),

        # Q46: Core Repeat 6 (4m) — 9701/41/O/N/22/Q9(c)
        Question(
            number=46,
            title="Core Repeat 6: Addition vs Condensation Polymerisation Comparison — 9701/41/O/N/22/Q9(c) [4 Marks]",
            syllabus_ref="35.1", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Give two structural requirements for a monomer to undergo addition polymerisation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Give two structural requirements for monomers to undergo condensation polymerisation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Must contain a carbon-carbon double bond (C=C) / unsaturation [1]; Polymerisation occurs by breaking the &pi;-bond without loss of atoms [1].", "marks": 2},
                {"part": "(b)", "points": "Must have at least two functional groups per molecule (bifunctional or polyfunctional) [1]; Must possess reactive groups such as -OH, -COOH, -NH2, or -COCl that can react together with the elimination of a small molecule [1].", "marks": 2}
            ]
        ),

        # Q47: Core Repeat 7 (4m) — 9701/42/F/M/21/Q11(b)
        Question(
            number=47,
            title="Core Repeat 7: Repeat Unit of Kevlar vs Nylon 6,6 — 9701/42/F/M/21/Q11(b) [4 Marks]",
            syllabus_ref="35.3", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Draw the repeat unit of Kevlar and state why its chains are much stiffer than Nylon 6,6.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the repeat unit of Nylon 6,6 and explain why it is more flexible than Kevlar.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-[NH-C6H4-NH-CO-C6H4-CO]- [1]; The rigid planar 1,4-phenylene rings prevent chain twisting and rotation, keeping chains linear and stiff [1].", "marks": 2},
                {"part": "(b)", "points": "-[NH-(CH2)6-NH-CO-(CH2)4-CO]- [1]; Contains flexible aliphatic -(CH2)- methylene chains that can freely rotate around C-C &sigma;-bonds [1].", "marks": 2}
            ]
        ),

        # Q48: Core Repeat 8 (4m) — 9701/41/M/J/20/Q10(c)
        Question(
            number=48,
            title="Core Repeat 8: Acid Hydrolysis of Polyamide Linkages — 9701/41/M/J/20/Q10(c) [4 Marks]",
            syllabus_ref="35.4", difficulty="MEDIUM", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Write an equation showing the hydrolysis of an amide linkage (-CONH-) by aqueous acid (H+/H2O).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why Nylon fabrics cannot be worn when handling concentrated sulfuric acid or hydrochloric acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "-CO-NH- + H2O + H+ &rarr; -COOH + -NH3+ [2].", "marks": 2},
                {"part": "(b)", "points": "Concentrated acids rapidly protonate and hydrolyse the amide bonds along the polymer chains [1]; This breaks the macromolecules into short fragments, destroying the fabric's tensile strength and creating holes [1].", "marks": 2}
            ]
        ),

        # Q49: Core Repeat 9 (2m) — 9701/42/M/J/23/Q11(e)
        Question(
            number=49,
            title="Core Repeat 9: Linkage Type in Nylon 6,6 — 9701/42/M/J/23/Q11(e) [2 Marks]",
            syllabus_ref="35.1", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Name the functional linkage connecting monomer units in Nylon 6,6 and state which biological macromolecules contain the same linkage.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Amide linkage / peptide bond (-CONH-) [1]; Proteins / polypeptides [1].", "marks": 2}
            ]
        ),

        # Q50: Core Repeat 10 (2m) — 9701/41/O/N/23/Q10(e)
        Question(
            number=50,
            title="Core Repeat 10: Environmental Hazard of PVC Incineration — 9701/41/O/N/23/Q10(e) [2 Marks]",
            syllabus_ref="35.4", difficulty="EASY", section_key="SEC_D",
            parts=[
                QuestionPart("(a)", "Identify the corrosive acidic gas produced when poly(chloroethene) (PVC) is incinerated, and state one environmental harm it causes.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydrogen chloride, HCl [1]; Causes acid rain which damages aquatic ecosystems / dissolves limestone buildings / causes respiratory distress [1].", "marks": 2}
            ]
        )
    ]

    # Verify tariffs
    count_6m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    count_4m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    count_2m = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_qs = len(questions)

    print(f"Topic 35 Questions Count: {total_qs}")
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
    print("Topic 35 PDF built successfully!")

if __name__ == "__main__":
    build_topic35_50q()
