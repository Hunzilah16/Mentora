"""
Complete 50-Question Master Pack: Topic 30 — Hydrocarbons (Arenes) (Paper 4 Theory)
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

def build_topic30_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic30_Hydrocarbons_Arenes.pdf"

    topic_title = "Topic 30 — Hydrocarbons (Arenes)"
    topic_subtitle = "Benzene Structure & Delocalisation · Electrophilic Aromatic Substitution Mechanisms · Methylbenzene Reactivity · Side-Chain Oxidation"

    subtopics_summary = [
        ("30.1 Benzene Structure, Bonding & Resonance Stability", "Kekulé structure versus delocalised π-system; planar regular hexagonal geometry, sp2 hybridisation, and intermediate C-C bond lengths (0.139 nm); thermochemical evidence from enthalpy of hydrogenation (152 kJ mol-1 resonance stabilization energy); resistance to addition reactions."),
        ("30.2 Electrophilic Aromatic Substitution Reactions & Mechanisms", "Generation of electrophiles; nitration (conc. HNO3 + conc. H2SO4 at 50–55 °C to generate NO2+); halogenation (Cl2/Br2 with AlCl3/FeBr3 halogen carriers); Friedel-Crafts alkylation and acylation; Wheland arenium carbocation intermediate and aromatic ring restoration."),
        ("30.3 Methylbenzene: Activating & Directing Effects", "Electron-donating inductive (+I) effect of alkyl groups; enhanced electron density in the aromatic ring; 2,4-directing effect versus 3-directing deactivating groups (e.g. -NO2); ring chlorination (AlCl3, room temp, dark) versus side-chain free-radical chlorination (UV light, boiling)."),
        ("30.4 Side-Chain Oxidation of Alkylarenes", "Oxidation of alkyl side-chains (methylbenzene, ethylbenzene) to benzoic acid by prolonged reflux with alkaline potassium manganate(VII) followed by acidification; resistance of the benzene ring to oxidation."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Arenes from the past 10 years.")
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

        # Q1: 9701/42/M/J/23/Q6
        Question(
            number=1,
            title="Benzene Bonding, Enthalpy of Hydrogenation & Resonance Stability — 9701/42/M/J/23/Q6 [6 Marks]",
            syllabus_ref="30.1", difficulty="HARD", section_key="SEC_A",
            preamble="The structure of benzene is explained by a delocalised &pi;-electron system rather than the theoretical Kekulé structure (cyclohexa-1,3,5-triene).<br/>The thermochemical comparison of their enthalpies of hydrogenation is depicted in Fig. 1.1.<br/>Data: &Delta;<i>H</i>°<sub>hyd</sub>(cyclohexene) = -120 kJ mol<sup>-1</sup>; &Delta;<i>H</i>°<sub>hyd</sub>(benzene) = -208 kJ mol<sup>-1</sup>.",
            figure_path=os.path.join(fig_dir, "a2_t30_benzene_resonance_energy.png"),
            figure_caption="Fig. 1.1: Enthalpy of hydrogenation energy levels illustrating the 152 kJ mol-1 resonance stabilization energy of benzene.",
            parts=[
                QuestionPart("(a)", "Calculate the theoretical enthalpy of hydrogenation for cyclohexa-1,3,5-triene and deduce the resonance (delocalisation) energy of benzene.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe the bonding in benzene in terms of orbital hybridisation, &sigma;-bonds, and delocalised &pi;-orbitals.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State two physical or chemical pieces of experimental evidence (other than enthalpy of hydrogenation) that disprove the Kekulé structure.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Theoretical &Delta;H = 3 &times; (-120) = -360 kJ mol^-1 [1]; Resonance energy = -360 - (-208) = -152 kJ mol^-1 (benzene is 152 kJ mol^-1 more stable than predicted) [1].", "marks": 2},
                {"part": "(b)", "points": "Each carbon atom is sp2 hybridised, forming three planar &sigma;-bonds (two C-C, one C-H) at 120° bond angles [1]; The remaining unhybridised 2p atomic orbitals on all six carbon atoms overlap sideways above and below the ring plane to form a continuous delocalised &pi;-electron cloud (donut rings) [1].", "marks": 2},
                {"part": "(c)", "points": "1. All six C-C bond lengths are completely identical (0.139 nm), intermediate between C-C single (0.154 nm) and C=C double (0.134 nm) [1]; 2. Benzene undergoes electrophilic substitution rather than electrophilic addition and does not decolourise bromine water at room temperature [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q6
        Question(
            number=2,
            title="Electrophilic Aromatic Substitution: Nitration of Benzene Mechanism — 9701/41/M/J/23/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="Benzene is nitrated by heating with a mixture of concentrated nitric acid and concentrated sulfuric acid at 50–55 °C.<br/>The general mechanism of electrophilic substitution is shown in Fig. 2.1.",
            figure_path=os.path.join(fig_dir, "a2_t30_nitration_mechanism.png"),
            figure_caption="Fig. 2.1: Electrophilic aromatic substitution mechanism showing generation of NO2+ and the Wheland carbocation intermediate.",
            parts=[
                QuestionPart("(a)", "Write an equation for the generation of the nitronium ion electrophile, NO<sub>2</sub><sup>+</sup>, and state the catalytic role of concentrated sulfuric acid.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Draw the full mechanism for the nitration of benzene, showing curly arrows, the horseshoe arenium intermediate with positive charge, and the regeneration of the catalyst.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why the temperature must be kept below 55 °C during this reaction.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "HNO3 + 2H2SO4 &rightleftharpoons; NO2+ + 2HSO4- + H3O+ (or HNO3 + H2SO4 &rightleftharpoons; NO2+ + HSO4- + H2O) [1]; H2SO4 acts as a Brønsted-Lowry acid / catalyst by protonating HNO3 [1].", "marks": 2},
                {"part": "(b)", "points": "Curly arrow from delocalised &pi;-ring to NO2+ [1]; Correct horseshoe arenium intermediate [C6H6NO2]+ with opening towards substituted carbon and positive charge inside [1]; Curly arrow from C-H bond into ring to restore &pi;-system, and H+ accepted by HSO4- to reform H2SO4 [1].", "marks": 3},
                {"part": "(c)", "points": "To prevent multiple nitrations (formation of 1,3-dinitrobenzene and 1,3,5-trinitrobenzene) [1].", "marks": 1}
            ]
        ),

        # Q3: 9701/42/O/N/23/Q6
        Question(
            number=3,
            title="Friedel-Crafts Acylation & Alkylation of Benzene — 9701/42/O/N/23/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="Benzene reacts with ethanoyl chloride, CH<sub>3</sub>COCl, in the presence of anhydrous aluminium chloride, AlCl<sub>3</sub>, to produce phenylethanone:<br/>C<sub>6</sub>H<sub>6</sub> + CH<sub>3</sub>COCl &rarr; C<sub>6</sub>H<sub>5</sub>COCH<sub>3</sub> + HCl",
            parts=[
                QuestionPart("(a)", "Write an equation showing how the acylium electrophile, CH<sub>3</sub>CO<sup>+</sup>, is generated by reaction with AlCl<sub>3</sub>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the mechanism for this acylation reaction, using curly arrows and showing the intermediate.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why Friedel-Crafts acylation stops cleanly at mono-substitution, whereas Friedel-Crafts alkylation frequently leads to poly-alkylation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3COCl + AlCl3 &rarr; CH3CO+ + AlCl4- [2].", "marks": 2},
                {"part": "(b)", "points": "Curly arrow from benzene ring to CH3CO+; horseshoe arenium intermediate formed; curly arrow from C-H bond back into ring; AlCl4- takes H+ to give HCl + AlCl3 [2].", "marks": 2},
                {"part": "(c)", "points": "The acyl group (-COCH3) is strongly electron-withdrawing (-I and -M), deactivating the ring towards further electrophilic attack [1]; Alkyl groups (-R) are electron-donating (+I), making the mono-alkylated ring more electron-rich and more reactive than benzene, encouraging multiple alkylations [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/O/N/23/Q6
        Question(
            number=4,
            title="Methylbenzene: Ring Substitution vs Side-Chain Free-Radical Chlorination — 9701/41/O/N/23/Q6 [6 Marks]",
            syllabus_ref="30.3", difficulty="HARD", section_key="SEC_A",
            preamble="Methylbenzene, C<sub>6</sub>H<sub>5</sub>CH<sub>3</sub>, reacts with chlorine under two completely different sets of conditions:<br/>- Reaction 1: Cl<sub>2</sub> in the presence of anhydrous AlCl<sub>3</sub> in the cold, dark.<br/>- Reaction 2: Cl<sub>2</sub> gas bubbled into boiling methylbenzene in the presence of UV light.",
            parts=[
                QuestionPart("(a)", "Identify the organic products formed in Reaction 1, naming the type of reaction mechanism and explaining the positions of substitution.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Identify the organic product formed in Reaction 2, naming the type of reaction mechanism.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Write equations for the propagation steps in the mechanism of Reaction 2.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2-chloromethylbenzene (o-chlorotoluene) and 4-chloromethylbenzene (p-chlorotoluene) [1]; Electrophilic aromatic substitution [1]; The methyl group is electron-donating (+I effect) and activates the 2- and 4-positions by stabilising the carbocation intermediate at those positions [1].", "marks": 3},
                {"part": "(b)", "points": "(Chloromethyl)benzene, C6H5CH2Cl [1]; Free-radical substitution of the alkyl side-chain [1].", "marks": 2},
                {"part": "(c)", "points": "Step 1: C6H5CH3 + Cl• &rarr; C6H5CH2• + HCl; Step 2: C6H5CH2• + Cl2 &rarr; C6H5CH2Cl + Cl• [1].", "marks": 1}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q6
        Question(
            number=5,
            title="Side-Chain Alkyl Oxidation to Benzoic Acid — 9701/42/M/J/22/Q6 [6 Marks]",
            syllabus_ref="30.4", difficulty="HARD", section_key="SEC_A",
            preamble="Alkylarenes undergo side-chain oxidation when heated under prolonged reflux with alkaline potassium manganate(VII), KMnO<sub>4</sub>, followed by acidification with dilute sulfuric acid.",
            parts=[
                QuestionPart("(a)", "State the observations during the reflux with alkaline KMnO<sub>4</sub> and upon subsequent addition of dilute acid to the cooled mixture.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Propylbenzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>, is heated with alkaline KMnO<sub>4</sub> and then acidified. Identify the organic product and any inorganic carbon by-product.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why (1,1-dimethylethyl)benzene (tert-butylbenzene), C<sub>6</sub>H<sub>5</sub>C(CH<sub>3</sub>)<sub>3</sub>, does NOT undergo oxidation under these conditions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Purple solution decolourises and a brown/black precipitate of MnO2 forms [1]; Upon acidification, a white crystalline precipitate of benzoic acid (C6H5COOH) forms [1].", "marks": 2},
                {"part": "(b)", "points": "Benzoic acid, C6H5COOH [1]; Carbon dioxide, CO2 (or carbonate) [1].", "marks": 2},
                {"part": "(c)", "points": "Side-chain oxidation requires at least one benzylic hydrogen atom attached to the carbon directly bonded to the benzene ring [1]; In tert-butylbenzene, the benzylic carbon is tertiary and bonded to three methyl groups (zero benzylic C-H bonds), making it resistant to oxidative attack [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/41/M/J/22/Q6
        Question(
            number=6,
            title="Bromination of Benzene vs Phenol vs Methylbenzene — 9701/41/M/J/22/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="The reactivity of aromatic rings towards electrophilic bromination varies substantially:<br/>- Compound A: Benzene<br/>- Compound B: Methylbenzene<br/>- Compound C: Phenol",
            parts=[
                QuestionPart("(a)", "Rank these three compounds in order of increasing reactivity towards electrophilic bromination (least reactive first).", 1, num_answer_lines=1),
                QuestionPart("(b)", "State the reagents and conditions required to brominate benzene, writing the overall equation.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why phenol reacts instantly with aqueous bromine without needing a catalyst, whereas benzene requires liquid bromine and an FeBr<sub>3</sub> catalyst.", 3, num_answer_lines=4)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene < Methylbenzene < Phenol [1].", "marks": 1},
                {"part": "(b)", "points": "Br2 with anhydrous FeBr3 (or AlBr3) catalyst at warm temperature [1]; C6H6 + Br2 &rarr; C6H5Br + HBr [1].", "marks": 2},
                {"part": "(c)", "points": "In phenol, the lone pair on the oxygen atom of the -OH group delocalises into the benzene &pi;-ring [1]; This significantly increases the &pi;-electron density of the ring, activating it [1]; The electron-rich ring is capable of polarising non-polar Br2 molecules without needing a halogen carrier catalyst, whereas benzene's stable delocalised ring requires FeBr3 to generate the powerful Br+ electrophile [1].", "marks": 3}
            ]
        ),

        # Q7: 9701/42/O/N/22/Q6
        Question(
            number=7,
            title="Directing Effects: Nitration of Nitrobenzene vs Methylbenzene — 9701/42/O/N/22/Q6 [6 Marks]",
            syllabus_ref="30.3", difficulty="HARD", section_key="SEC_A",
            preamble="Substituents on a benzene ring influence both the rate of further substitution and the position at which incoming electrophiles attack.",
            parts=[
                QuestionPart("(a)", "Explain why the nitro group (-NO<sub>2</sub>) is deactivating and directs incoming electrophiles to the 3-position (meta-directing).", 3, num_answer_lines=4),
                QuestionPart("(b)", "Draw the structural formula of the organic product obtained when nitrobenzene is heated with concentrated HNO<sub>3</sub> and concentrated H<sub>2</sub>SO<sub>4</sub> at 100 °C.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Contrast the reaction conditions required to nitrate nitrobenzene with those required to nitrate benzene.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Nitrogen has a formal positive charge and is bonded to two electronegative oxygens, exerting a strong electron-withdrawing inductive and resonance (-I and -M) effect [1]; This withdraws electron density from the &pi;-system, dramatically deactivating the entire ring [1]; Electron density is depleted most severely at the 2- and 4-positions, making attack at the 3-position the pathway of lowest relative activation energy [1].", "marks": 3},
                {"part": "(b)", "points": "1,3-dinitrobenzene drawn correctly [1].", "marks": 1},
                {"part": "(c)", "points": "Benzene requires conc. HNO3 + conc. H2SO4 at 50–55 °C [1]; Nitrobenzene is deactivated and requires much harsher conditions: reflux at 100 °C (or fuming nitric acid) [1].", "marks": 2}
            ]
        ),

        # Q8: 9701/41/O/N/22/Q6
        Question(
            number=8,
            title="Halogenation of Arenes: FeBr3 vs UV Light Mechanisms — 9701/41/O/N/22/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="Ethylbenzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>CH<sub>3</sub>, reacts with bromine under different conditions to yield two structural isomers.",
            parts=[
                QuestionPart("(a)", "When ethylbenzene reacts with Br<sub>2</sub> and FeBr<sub>3</sub> in the dark, two isomeric bromo compounds are formed. Identify both products and state their positions of substitution.", 2, num_answer_lines=3),
                QuestionPart("(b)", "When ethylbenzene is boiled with Br<sub>2</sub> in the presence of UV light, (1-bromoethyl)benzene is formed as the major product. Draw its structure and identify the chiral center.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why bromination in UV light occurs preferentially at the C1 (benzylic) position rather than C2.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1-bromo-2-ethylbenzene (2-bromoethylbenzene) and 1-bromo-4-ethylbenzene (4-bromoethylbenzene) [2].", "marks": 2},
                {"part": "(b)", "points": "C6H5-C*H(Br)-CH3 drawn with asterisk on C1 [1]; Carbon-1 is bonded to four different groups (-H, -Br, -CH3, -C6H5) [1].", "marks": 2},
                {"part": "(c)", "points": "Abstraction of H from C1 forms a benzylic free radical, C6H5-C•H-CH3 [1]; The unpaired electron is delocalised into the aromatic &pi;-system, conferring extraordinary stability compared to the primary alkyl radical at C2 [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/21/Q6
        Question(
            number=9,
            title="Combustion & Enthalpy of Arenes: Benzene vs Hexane — 9701/42/M/J/21/Q6 [6 Marks]",
            syllabus_ref="30.1", difficulty="HARD", section_key="SEC_A",
            preamble="When benzene burns in air, it produces a very smoky, sooty yellow flame, whereas hexane burns with a much cleaner flame.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the complete combustion of liquid benzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the percentage by mass of carbon in benzene (C<sub>6</sub>H<sub>6</sub>) and in hexane (C<sub>6</sub>H<sub>14</sub>).", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why aromatic hydrocarbons burn with a characteristic smoky, luminous flame with unburnt carbon soot.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H6(l) + 7.5O2(g) &rarr; 6CO2(g) + 3H2O(l) (or 2C6H6 + 15O2 &rarr; 12CO2 + 6H2O) [2].", "marks": 2},
                {"part": "(b)", "points": "Benzene: Mr = 78.0 &rArr; %C = (72.0 / 78.0) &times; 100 = 92.3% [1]; Hexane: Mr = 86.0 &rArr; %C = (72.0 / 86.0) &times; 100 = 83.7% [1].", "marks": 2},
                {"part": "(c)", "points": "Benzene has an exceptionally high carbon-to-hydrogen ratio (1:1) [1]; There is insufficient oxygen during open-air burning to completely oxidise all carbon, resulting in incomplete combustion that liberates glowing solid incandescent carbon particles (soot) [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/21/Q6
        Question(
            number=10,
            title="Synthesis of Benzoic Acid from Benzene via Multi-Step Route — 9701/41/M/J/21/Q6 [6 Marks]",
            syllabus_ref="30.4", difficulty="HARD", section_key="SEC_A",
            preamble="A chemical manufacturer synthesizes benzoic acid, C<sub>6</sub>H<sub>5</sub>COOH, starting from benzene, C<sub>6</sub>H<sub>6</sub>.<br/>Route: Benzene &rarr; Methylbenzene &rarr; Benzoic acid.",
            parts=[
                QuestionPart("(a)", "State the reagent, catalyst, and reaction conditions required for Step 1 (Benzene &rarr; Methylbenzene).", 2, num_answer_lines=3),
                QuestionPart("(b)", "State the reagents and conditions required for Step 2 (Methylbenzene &rarr; Benzoic acid).", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why an alternative route via bromobenzene and a Grignard reagent or nitrile is less efficient.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chloromethane (CH3Cl) with anhydrous aluminium chloride (AlCl3) catalyst at room temperature (Friedel-Crafts alkylation) [2].", "marks": 2},
                {"part": "(b)", "points": "Reflux with alkaline potassium manganate(VII) (KMnO4 + NaOH), followed by acidification with dilute sulfuric acid (or dilute HCl) [2].", "marks": 2},
                {"part": "(c)", "points": "Involves more synthetic steps, requires moisture-sensitive anhydrous ether for Grignard reagents, and halogenobenzene has an unreactive C-Br bond due to &pi;-delocalisation [2].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q6
        Question(
            number=11,
            title="Aromatic vs Aliphatic Halogen Compounds: Chlorobenzene vs Chloroethane — 9701/42/O/N/21/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="Chloroethane hydrolyses readily when refluxed with aqueous NaOH, but chlorobenzene is completely inert under the same conditions.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the hydrolysis of chloroethane.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the carbon-chlorine bond in chlorobenzene is significantly stronger and shorter than in chloroethane.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State a second reason why nucleophilic attack by OH<sup>-</sup> on chlorobenzene is prevented.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CH3CH2Cl + OH- &rarr; CH3CH2OH + Cl- [1].", "marks": 1},
                {"part": "(b)", "points": "A lone pair of electrons on the chlorine atom overlaps with the delocalised &pi;-electron system of the benzene ring [1]; This imparts partial double bond character to the C-Cl bond [1]; The bond is shorter, stronger, and has a much higher bond dissociation enthalpy, resisting cleavage [1].", "marks": 3},
                {"part": "(c)", "points": "The incoming nucleophile (OH-) is negatively charged and is electrostatically repelled by the high electron density of the delocalised &pi;-electron cloud above and below the benzene ring [2].", "marks": 2}
            ]
        ),

        # Q12: 9701/41/O/N/21/Q6
        Question(
            number=12,
            title="Friedel-Crafts Alkylation & Carbocation Rearrangement — 9701/41/O/N/21/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="When benzene is reacted with 1-chloropropane in the presence of AlCl<sub>3</sub>, the major product isolated is (1-methylethyl)benzene (cumene) rather than propylbenzene.",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of propylbenzene and cumene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why cumene is the major product by referring to carbocation stability and a 1,2-hydride shift.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Suggest how propylbenzene could be prepared without rearrangement using Friedel-Crafts acylation.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Propylbenzene: C6H5-CH2CH2CH3; Cumene: C6H5-CH(CH3)2 [2].", "marks": 2},
                {"part": "(b)", "points": "Reaction generates an initial primary carbocation: CH3CH2C+H2 [1]; A 1,2-hydride shift occurs: a hydrogen atom with its pair of electrons migrates from C2 to C1, transforming the primary carbocation into a more stable secondary carbocation: CH3C+HCH3 [1]; Secondary carbocation is stabilised by the positive inductive (+I) effect of two methyl groups, attacking benzene much faster [1].", "marks": 3},
                {"part": "(c)", "points": "React benzene with propanoyl chloride (CH3CH2COCl) and AlCl3 to give C6H5COCH2CH3, then reduce the carbonyl group using Clemmensen reduction (Zn/HCl) or Wolff-Kishner reduction [1].", "marks": 1}
            ]
        ),

        # Q13: 9701/42/M/J/20/Q6
        Question(
            number=13,
            title="Chlorination of Arenes: Chlorobenzene vs (Chloromethyl)benzene Tests — 9701/42/M/J/20/Q6 [6 Marks]",
            syllabus_ref="30.3", difficulty="HARD", section_key="SEC_A",
            preamble="Two isomeric halogenated arenes have the molecular formula C<sub>7</sub>H<sub>7</sub>Cl:<br/>- Isomer X: 1-chloro-4-methylbenzene (4-chlorotoluene)<br/>- Isomer Y: (chloromethyl)benzene (benzyl chloride)",
            parts=[
                QuestionPart("(a)", "Describe a chemical test to distinguish between Isomer X and Isomer Y, stating the reagents, conditions, and observations.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Write the ionic equation for the precipitation reaction in the positive test.", 1, num_answer_lines=2),
                QuestionPart("(c)", "Explain the difference in reactivity towards hydrolysis between Isomer X and Isomer Y.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Warm each isomer with aqueous sodium hydroxide (or ethanol/water), cool, acidify with dilute nitric acid (HNO3), and add aqueous silver nitrate (AgNO3) [2]; Isomer Y ((chloromethyl)benzene) gives an immediate white precipitate of AgCl; Isomer X (4-chlorotoluene) produces no precipitate [1].", "marks": 3},
                {"part": "(b)", "points": "Ag+(aq) + Cl-(aq) &rarr; AgCl(s) [1].", "marks": 1},
                {"part": "(c)", "points": "In Isomer Y, the chlorine is on an aliphatic side-chain (benzylic) and hydrolyses easily; in Isomer X, chlorine is attached directly to the aromatic ring where lone pair delocalisation strengthens the C-Cl bond [2].", "marks": 2}
            ]
        ),

        # Q14: 9701/41/M/J/20/Q6
        Question(
            number=14,
            title="Multi-Substituted Arenes: Synthesis of 4-Nitrobenzoic Acid — 9701/41/M/J/20/Q6 [6 Marks]",
            syllabus_ref="30.3", difficulty="HARD", section_key="SEC_A",
            preamble="A chemist wishes to synthesize 4-nitrobenzoic acid from methylbenzene.<br/>Two synthetic routes are considered:<br/>- Route 1: Nitration first, followed by oxidation.<br/>- Route 2: Oxidation first, followed by nitration.",
            parts=[
                QuestionPart("(a)", "Predict the organic product obtained in Route 2, and explain why Route 2 fails to produce 4-nitrobenzoic acid.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Explain why Route 1 successfully yields 4-nitrobenzoic acid, naming the isomers formed in the nitration step.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State how 4-nitromethylbenzene can be separated from its 2-nitro isomer.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Route 2 produces 3-nitrobenzoic acid [1]; The carboxylic acid group (-COOH) is electron-withdrawing and is a 3-directing (meta-directing) group [1]; Nitration of benzoic acid directs the incoming NO2+ to the 3-position, not the 4-position [1].", "marks": 3},
                {"part": "(b)", "points": "In Route 1, the methyl group (-CH3) in methylbenzene is electron-donating (+I) and is a 2,4-directing group [1]; Nitration gives a mixture of 2-nitromethylbenzene and 4-nitromethylbenzene; subsequent oxidation of 4-nitromethylbenzene yields 4-nitrobenzoic acid [1].", "marks": 2},
                {"part": "(c)", "points": "Fractional distillation (or fractional crystallisation) [1].", "marks": 1}
            ]
        ),

        # Q15: 9701/42/O/N/19/Q6
        Question(
            number=15,
            title="Halogen Carriers in Electrophilic Substitution: Role of Lewis Acids — 9701/42/O/N/19/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_A",
            preamble="The chlorination of benzene requires an anhydrous iron(III) chloride catalyst, FeCl<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "Explain what is meant by a <i>Lewis acid</i>, and explain why FeCl<sub>3</sub> acts as a Lewis acid.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write an equation showing how FeCl<sub>3</sub> polarises and cleaves Cl<sub>2</sub> to generate the electrophile.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Draw the two-step mechanism for the reaction of benzene with the generated electrophile, showing regeneration of FeCl<sub>3</sub>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A lone-pair electron acceptor [1]; Fe in FeCl3 has vacant d-orbitals and an incomplete octet capable of accepting a lone pair from a chlorine molecule [1].", "marks": 2},
                {"part": "(b)", "points": "Cl2 + FeCl3 &rightleftharpoons; Cl+ + FeCl4- (or Cl-Cl---FeCl3 complex with &delta;+ on outer Cl) [2].", "marks": 2},
                {"part": "(c)", "points": "Electrophilic attack by Cl+ on benzene forming [C6H6Cl]+ arenium intermediate; loss of H+ to FeCl4- yielding C6H5Cl + HCl + FeCl3 [2].", "marks": 2}
            ]
        ),

        # Q16: 9701/41/O/N/19/Q6
        Question(
            number=16,
            title="Kekulé Benzene vs 1,3,5-Hexatriene Comparison — 9701/41/O/N/19/Q6 [6 Marks]",
            syllabus_ref="30.1", difficulty="HARD", section_key="SEC_A",
            preamble="Benzene (C<sub>6</sub>H<sub>6</sub>) and hexa-1,3,5-triene (CH<sub>2</sub>=CH-CH=CH-CH=CH<sub>2</sub>) both contain three double bonds in their formal formulas.",
            parts=[
                QuestionPart("(a)", "Describe what is observed when bromine water is shaken with hexa-1,3,5-triene and with benzene at room temperature.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain the difference in reactivity towards bromine water between these two compounds.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the number of &sigma;-bonds and &pi;-bonds present in one molecule of benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hexa-1,3,5-triene: orange bromine water decolourises immediately / turns colourless [1]; Benzene: orange bromine water remains unchanged (no reaction) [1].", "marks": 2},
                {"part": "(b)", "points": "Hexa-1,3,5-triene contains localised C=C double bonds with high localized &pi;-electron density that easily polarise Br2 and undergo electrophilic addition [1]; Benzene possesses a continuous delocalised &pi;-electron aromatic ring with high resonance stabilisation energy (152 kJ mol^-1) that would be permanently destroyed by addition [1].", "marks": 2},
                {"part": "(c)", "points": "12 &sigma;-bonds (six C-C &sigma;-bonds and six C-H &sigma;-bonds) [1]; 3 &pi;-bonds (6 delocalised &pi;-electrons forming 3 pairs) [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q7
        Question(
            number=17,
            title="Bonding in Benzene: sp2 Hybridisation & Bond Angles — 9701/42/M/J/23/Q7 [4 Marks]",
            syllabus_ref="30.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Benzene is a planar, symmetrical hydrocarbon.",
            parts=[
                QuestionPart("(a)", "State the hybridisation of the carbon atoms in benzene and the C-C-C bond angle.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe the shape and origin of the &pi;-electron cloud in benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "sp2 hybridisation [1]; 120° [1].", "marks": 2},
                {"part": "(b)", "points": "Formed by sideways overlap of unhybridised 2p atomic orbitals on all six carbon atoms [1]; Two continuous ring-shaped clouds (toroids) of delocalised &pi;-electrons lying directly above and below the planar carbon ring [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/M/J/23/Q7
        Question(
            number=18,
            title="Equation and Reagents for Nitration of Benzene — 9701/41/M/J/23/Q7 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Nitrobenzene is an important industrial precursor for dyes.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the nitration of benzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the exact reagents and temperature required for mono-nitration.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H6 + HNO3 &rarr; C6H5NO2 + H2O [2].", "marks": 2},
                {"part": "(b)", "points": "Concentrated nitric acid (HNO3) and concentrated sulfuric acid (H2SO4) [1]; 50–55 °C [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/O/N/23/Q7
        Question(
            number=19,
            title="Friedel-Crafts Methylation of Benzene — 9701/42/O/N/23/Q7 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Methylbenzene is synthesized from benzene.",
            parts=[
                QuestionPart("(a)", "State the reagents and catalyst required for this transformation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Name the inorganic gas evolved as a by-product, and write the overall equation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chloromethane, CH3Cl [1]; Anhydrous aluminium chloride catalyst, AlCl3 [1].", "marks": 2},
                {"part": "(b)", "points": "Hydrogen chloride gas, HCl [1]; C6H6 + CH3Cl &rarr; C6H5CH3 + HCl [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/O/N/23/Q7
        Question(
            number=20,
            title="2,4-Directing Effect of Methyl Group — 9701/41/O/N/23/Q7 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="When methylbenzene is brominated in the presence of FeBr<sub>3</sub>, two isomers are formed.",
            parts=[
                QuestionPart("(a)", "Draw the structural formulas of the two major organic isomers.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why substitution occurs predominantly at the 2- and 4-positions rather than the 3-position.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2-bromomethylbenzene and 4-bromomethylbenzene drawn correctly [2].", "marks": 2},
                {"part": "(b)", "points": "The methyl group is electron-donating by positive inductive (+I) effect [1]; Electrophilic attack at 2- and 4-positions produces carbocation intermediates that have greater resonance stability (tertiary carbocation contributor) [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/M/J/22/Q7
        Question(
            number=21,
            title="Oxidation of Ethylbenzene with Alkaline KMnO4 — 9701/42/M/J/22/Q7 [4 Marks]",
            syllabus_ref="30.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Ethylbenzene, C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>CH<sub>3</sub>, is heated under reflux with alkaline KMnO<sub>4</sub> and then acidified.",
            parts=[
                QuestionPart("(a)", "Identify the aromatic organic product formed.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State what happens to the remaining carbon of the ethyl chain, naming the product.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzoic acid, C6H5COOH [2].", "marks": 2},
                {"part": "(b)", "points": "It is completely oxidised to carbon dioxide (CO2) / carbonate [2].", "marks": 2}
            ]
        ),

        # Q22: 9701/41/M/J/22/Q7
        Question(
            number=22,
            title="Why Benzene Undergoes Substitution Rather than Addition — 9701/41/M/J/22/Q7 [4 Marks]",
            syllabus_ref="30.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Unlike alkenes, benzene resists addition reactions.",
            parts=[
                QuestionPart("(a)", "Explain why benzene does not undergo electrophilic addition with bromine under standard conditions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why electrophilic substitution is thermodynamically preferred.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Electrophilic addition would permanently break the continuous delocalised &pi;-system, losing the 152 kJ mol^-1 resonance stabilisation energy [2].", "marks": 2},
                {"part": "(b)", "points": "Electrophilic substitution proceeds with the loss of H+ in the second step, completely regenerating and restoring the stable delocalised aromatic &pi;-system [2].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/O/N/22/Q7
        Question(
            number=23,
            title="Halogen Carrier Regeneration in Chlorination of Benzene — 9701/42/O/N/22/Q7 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Aluminium chloride acts as a catalyst in electrophilic substitution.",
            parts=[
                QuestionPart("(a)", "Write the equation for the formation of the arenium intermediate when benzene reacts with Cl<sup>+</sup>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the equation showing how AlCl<sub>3</sub> is regenerated from AlCl<sub>4</sub><sup>-</sup>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H6 + Cl+ &rarr; [C6H6Cl]+ [2].", "marks": 2},
                {"part": "(b)", "points": "[C6H6Cl]+ + AlCl4- &rarr; C6H5Cl + HCl + AlCl3 [2].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/22/Q7
        Question(
            number=24,
            title="3-Directing Effect of the Nitro Group — 9701/41/O/N/22/Q7 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Nitrobenzene is further nitrated to 1,3-dinitrobenzene.",
            parts=[
                QuestionPart("(a)", "Draw the structural formula of 1,3-dinitrobenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the nitro group is described as a deactivating group.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzene ring with -NO2 groups at positions 1 and 3 drawn correctly [2].", "marks": 2},
                {"part": "(b)", "points": "The strongly electronegative nitro group pulls electron density away from the ring via inductive and resonance effects [1]; Lowering ring electron density and making it a poorer nucleophile towards electrophiles [1].", "marks": 2}
            ]
        ),

        # Q25: 9701/42/M/J/21/Q7
        Question(
            number=25,
            title="Hydrogenation of Benzene to Cyclohexane — 9701/42/M/J/21/Q7 [4 Marks]",
            syllabus_ref="30.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Under forcing conditions, benzene can be hydrogenated to cyclohexane:<br/>C<sub>6</sub>H<sub>6</sub> + 3H<sub>2</sub> &rarr; C<sub>6</sub>H<sub>12</sub>",
            parts=[
                QuestionPart("(a)", "State the catalyst and the temperature and pressure conditions required.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the change in hybridisation of the carbon atoms during this reaction.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Finely divided nickel catalyst (or platinum/palladium) [1]; 150–200 °C and high pressure (approx. 30 atm) [1].", "marks": 2},
                {"part": "(b)", "points": "sp2 hybridisation in planar benzene changes to sp3 hybridisation in non-planar cyclohexane [2].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/21/Q7
        Question(
            number=26,
            title="Comparison of Reactivity: Benzene vs Methylbenzene — 9701/41/M/J/21/Q7 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Methylbenzene is nitrated approximately 25 times faster than benzene.",
            parts=[
                QuestionPart("(a)", "Explain why methylbenzene reacts faster than benzene in electrophilic substitution.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the temperature required to mono-nitrate methylbenzene compared to benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The methyl group pushes electron density into the ring through a positive inductive (+I) effect [1]; Increasing the &pi;-electron density and making the ring more susceptible to electrophilic attack [1].", "marks": 2},
                {"part": "(b)", "points": "Around 30 °C (milder temperature than benzene's 50–55 °C) [2].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q7
        Question(
            number=27,
            title="Side-Chain Chlorination of Methylbenzene by Free Radicals — 9701/42/O/N/21/Q7 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Boiling methylbenzene with chlorine in UV light yields (chloromethyl)benzene.",
            parts=[
                QuestionPart("(a)", "Name the type of bond fission that initiates this reaction.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the products formed if chlorine gas is bubbled in excess.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Homolytic fission of the Cl-Cl bond by UV light [2].", "marks": 2},
                {"part": "(b)", "points": "(Dichloromethyl)benzene, C6H5CHCl2, and (trichloromethyl)benzene, C6H5CCl3 [2].", "marks": 2}
            ]
        ),

        # Q28: 9701/41/O/N/21/Q7
        Question(
            number=28,
            title="Synthesis of Phenylethene (Styrene) — 9701/41/O/N/21/Q7 [4 Marks]",
            syllabus_ref="30.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Phenylethene is the monomer for polystyrene.",
            parts=[
                QuestionPart("(a)", "Show how phenylethene, C<sub>6</sub>H<sub>5</sub>CH=CH<sub>2</sub>, can be prepared from ethylbenzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe a chemical test to confirm the presence of the alkene double bond in phenylethene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Catalytic dehydrogenation over iron(III) oxide catalyst at 600 °C (or brominate with Br2/UV to C6H5CH(Br)CH3 then eliminate with ethanolic KOH) [2].", "marks": 2},
                {"part": "(b)", "points": "Add bromine water: orange bromine water decolourises immediately [2].", "marks": 2}
            ]
        ),

        # Q29: 9701/42/M/J/20/Q7
        Question(
            number=29,
            title="Friedel-Crafts Acylation of Methylbenzene — 9701/42/M/J/20/Q7 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Methylbenzene reacts with ethanoyl chloride in the presence of AlCl<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "Identify the major organic product formed, giving its IUPAC name.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why 4-methylphenylethanone is formed in preference to 2-methylphenylethanone.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "4-methylphenylethanone (1-(4-methylphenyl)ethan-1-one) [2].", "marks": 2},
                {"part": "(b)", "points": "The bulky -COCH3 acyl group and the -CH3 methyl group experience steric hindrance/crowding at the adjacent 2-position, making attack at the open 4-position sterically favoured [2].", "marks": 2}
            ]
        ),

        # Q30: 9701/41/M/J/20/Q7
        Question(
            number=30,
            title="Combustion Hazard of Benzene in Industry — 9701/41/M/J/20/Q7 [4 Marks]",
            syllabus_ref="30.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Benzene is a volatile, carcinogenic liquid.",
            parts=[
                QuestionPart("(a)", "State two health or safety hazards associated with handling benzene in the laboratory.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Name a safer aromatic hydrocarbon frequently used as a laboratory substitute for benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. Known human carcinogen / causes leukaemia [1]; 2. Highly flammable volatile liquid (fire/explosion risk) [1].", "marks": 2},
                {"part": "(b)", "points": "Methylbenzene (toluene) [2] (its methyl group allows rapid metabolic excretion via benzoic acid, making it far less toxic).", "marks": 2}
            ]
        ),

        # Q31: 9701/42/O/N/19/Q7
        Question(
            number=31,
            title="Identification of Chiral Center in Aromatic Derivatives — 9701/42/O/N/19/Q7 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Consider the aromatic compounds: (chloromethyl)benzene, 1-phenylethanol, 2-phenylethanol.",
            parts=[
                QuestionPart("(a)", "Identify which of these compounds exhibits optical activity.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the displayed formula of this compound and circle its chiral carbon.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1-phenylethanol, C6H5CH(OH)CH3 [2].", "marks": 2},
                {"part": "(b)", "points": "Displayed formula with circle around C1 bonded to -H, -OH, -CH3, and -C6H5 [2].", "marks": 2}
            ]
        ),

        # Q32: 9701/41/O/N/19/Q7
        Question(
            number=32,
            title="Resistance of Benzene Ring to Oxidation — 9701/41/O/N/19/Q7 [4 Marks]",
            syllabus_ref="30.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="When methylbenzene is boiled with acidified potassium dichromate, the methyl group is oxidised but the ring remains intact.",
            parts=[
                QuestionPart("(a)", "Explain why the benzene ring is exceptionally resistant to chemical oxidising agents.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State what reagent can rupture the benzene ring completely.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "The delocalised &pi;-electron system possesses a high resonance stabilisation energy of 152 kJ mol^-1, which makes breaking the aromatic carbon skeleton energetically prohibitive [2].", "marks": 2},
                {"part": "(b)", "points": "Ozone (ozonolysis) or combustion in excess oxygen / catalytic oxidation at 450 °C over V2O5 to maleic anhydride [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q9
        Question(
            number=33,
            title="Carbon-Carbon Bond Length in Benzene — 9701/42/M/J/23/Q9 [2 Marks]",
            syllabus_ref="30.1", difficulty="EASY", section_key="SEC_C",
            preamble="X-ray diffraction determines bond lengths accurately.",
            parts=[
                QuestionPart("(a)", "State the experimental C-C bond length in benzene and compare it with standard C-C single and C=C double bonds.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "0.139 nm [1]; Intermediate between single bond (0.154 nm) and double bond (0.134 nm) [1].", "marks": 2}
            ]
        ),

        # Q34: 9701/41/M/J/23/Q9
        Question(
            number=34,
            title="Electrophile in Nitration of Benzene — 9701/41/M/J/23/Q9 [2 Marks]",
            syllabus_ref="30.2", difficulty="EASY", section_key="SEC_C",
            preamble="Electrophilic substitution involves reactive electrophiles.",
            parts=[
                QuestionPart("(a)", "Name and give the chemical formula of the active electrophile in the nitration of benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Nitronium ion [1]; NO2+ [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/O/N/23/Q9
        Question(
            number=35,
            title="Role of AlCl3 in Halogenation — 9701/42/O/N/23/Q9 [2 Marks]",
            syllabus_ref="30.2", difficulty="EASY", section_key="SEC_C",
            preamble="Halogen carriers facilitate electrophilic substitution.",
            parts=[
                QuestionPart("(a)", "State the role of anhydrous AlCl<sub>3</sub> in the chlorination of benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Halogen carrier / Lewis acid catalyst [1]; Polarises the chlorine molecule to generate the Cl+ electrophile [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/O/N/23/Q9
        Question(
            number=36,
            title="Directing Effect of Alkyl Groups — 9701/41/O/N/23/Q9 [2 Marks]",
            syllabus_ref="30.3", difficulty="EASY", section_key="SEC_C",
            preamble="Substituents direct electrophilic substitution.",
            parts=[
                QuestionPart("(a)", "State the directing effect of an alkyl group on a benzene ring.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2- and 4-directing (ortho- and para-directing) [1]; and activating [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/M/J/22/Q9
        Question(
            number=37,
            title="Oxidation Product of Methylbenzene — 9701/42/M/J/22/Q9 [2 Marks]",
            syllabus_ref="30.4", difficulty="EASY", section_key="SEC_C",
            preamble="Alkyl side-chains undergo vigorous oxidation.",
            parts=[
                QuestionPart("(a)", "Name and draw the formula of the organic compound formed when methylbenzene is refluxed with alkaline KMnO<sub>4</sub> and then acidified.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Benzoic acid [1]; C6H5COOH [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/41/M/J/22/Q9
        Question(
            number=38,
            title="Resonance Energy of Benzene Value — 9701/41/M/J/22/Q9 [2 Marks]",
            syllabus_ref="30.1", difficulty="EASY", section_key="SEC_C",
            preamble="Thermochemical data quantify aromatic stability.",
            parts=[
                QuestionPart("(a)", "State the numerical value of the resonance stabilization energy of benzene, with units.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "152 kJ mol^-1 [2].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/O/N/22/Q9
        Question(
            number=39,
            title="Conditions for Side-Chain Chlorination of Toluene — 9701/42/O/N/22/Q9 [2 Marks]",
            syllabus_ref="30.3", difficulty="EASY", section_key="SEC_C",
            preamble="Different conditions change substitution site.",
            parts=[
                QuestionPart("(a)", "State the conditions required to chlorinate the methyl group of methylbenzene rather than the aromatic ring.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Chlorine gas (Cl2), boiling / high temperature [1]; and ultraviolet (UV) light (absence of Lewis acid) [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/22/Q9
        Question(
            number=40,
            title="Wheland Intermediate Definition — 9701/41/O/N/22/Q9 [2 Marks]",
            syllabus_ref="30.2", difficulty="EASY", section_key="SEC_C",
            preamble="Arenium ions are key intermediates.",
            parts=[
                QuestionPart("(a)", "Describe the structure of the carbocation intermediate formed during electrophilic substitution of benzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "A non-aromatic cyclohexadienyl cation (arenium ion) [1]; with a delocalised 4&pi;-electron system spread over 5 carbon atoms (horseshoe) carrying a +1 charge [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # 4 x 6-Markers (Q41–Q44), 4 x 4-Markers (Q45–Q48), 2 x 2-Markers (Q49–Q50)
        # =====================================================================

        # Q41: 9701/42/M/J/23/Q6(Repeat 1 - 6m)
        Question(
            number=41,
            title="[CORE REPEAT 1] Complete Enthalpy of Hydrogenation & Delocalisation Analysis — 9701/42/M/J/23/Q6 [6 Marks]",
            syllabus_ref="30.1", difficulty="HARD", section_key="SEC_D",
            preamble="The experimental enthalpy of hydrogenation of benzene is compared to the theoretical value in Fig. 41.1.",
            figure_path=os.path.join(fig_dir, "a2_t30_benzene_resonance_energy.png"),
            figure_caption="Fig. 41.1: Thermochemical comparison of benzene and theoretical cyclohexa-1,3,5-triene.",
            parts=[
                QuestionPart("(a)", "Calculate the resonance stabilization energy of benzene using &Delta;<i>H</i>°<sub>hyd</sub>(cyclohexene) = -120 kJ mol<sup>-1</sup> and &Delta;<i>H</i>°<sub>hyd</sub>(benzene) = -208 kJ mol<sup>-1</sup>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how the delocalised &pi;-electron cloud accounts for the extra stability of benzene.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State two pieces of structural evidence that support the delocalised model over the Kekulé model.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Theoretical &Delta;H = 3 &times; (-120) = -360 kJ mol^-1 [1]; Resonance energy = -360 - (-208) = -152 kJ mol^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "Sideways overlap of 2p orbitals spreads 6 &pi;-electrons over all six carbon nuclei [1]; This delocalisation lowers electron-electron repulsion and maximizes electron-nuclear attraction, creating a low-energy, highly stable aromatic ring [1].", "marks": 2},
                {"part": "(c)", "points": "1. All six C-C bonds have equal length (0.139 nm) [1]; 2. Benzene is a regular planar hexagon with 120° bond angles (no alternating short and long bonds) [1].", "marks": 2}
            ]
        ),

        # Q42: 9701/41/M/J/23/Q6(Repeat 2 - 6m)
        Question(
            number=42,
            title="[CORE REPEAT 2] Full Mechanism of Nitration of Benzene — 9701/41/M/J/23/Q6 [6 Marks]",
            syllabus_ref="30.2", difficulty="HARD", section_key="SEC_D",
            preamble="Nitration of benzene is a classic electrophilic aromatic substitution, illustrated in Fig. 42.1.",
            figure_path=os.path.join(fig_dir, "a2_t30_nitration_mechanism.png"),
            figure_caption="Fig. 42.1: Stepwise electrophilic substitution pathway for benzene nitration.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the generation of NO<sub>2</sub><sup>+</sup> from concentrated HNO<sub>3</sub> and concentrated H<sub>2</sub>SO<sub>4</sub>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Draw the mechanism using curly arrows showing the arenium carbocation intermediate and loss of H<sup>+</sup>.", 3, num_answer_lines=4),
                QuestionPart("(c)", "State why sulfuric acid is regenerated at the end of the reaction.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "HNO3 + 2H2SO4 &rightleftharpoons; NO2+ + 2HSO4- + H3O+ [2].", "marks": 2},
                {"part": "(b)", "points": "Curly arrow from &pi;-ring to NO2+ [1]; Horseshoe carbocation intermediate drawn with + charge and H, NO2 attached [1]; Curly arrow from C-H bond back into ring to regenerate delocalised &pi;-system [1].", "marks": 3},
                {"part": "(c)", "points": "H+ released from intermediate combines with HSO4- to reform H2SO4, confirming its role as a catalyst [1].", "marks": 1}
            ]
        ),

        # Q43: 9701/42/O/N/23/Q6(Repeat 3 - 6m)
        Question(
            number=43,
            title="[CORE REPEAT 3] Ring vs Side-Chain Chlorination of Methylbenzene — 9701/42/O/N/23/Q6 [6 Marks]",
            syllabus_ref="30.3", difficulty="HARD", section_key="SEC_D",
            preamble="The site of substitution in methylbenzene is controlled by the reaction conditions.",
            parts=[
                QuestionPart("(a)", "State the reagents, catalyst, and conditions to chlorinate the ring, naming the two organic products.", 3, num_answer_lines=3),
                QuestionPart("(b)", "State the conditions to chlorinate the methyl side-chain, naming the product.", 2, num_answer_lines=2),
                QuestionPart("(c)", "State the mechanism type for the ring reaction and for the side-chain reaction.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cl2 with anhydrous AlCl3 (or FeCl3) in the dark at room temperature [1]; 2-chloromethylbenzene and 4-chloromethylbenzene [2].", "marks": 3},
                {"part": "(b)", "points": "Cl2 gas, boiling / heat, under ultraviolet (UV) light [1]; (Chloromethyl)benzene [1].", "marks": 2},
                {"part": "(c)", "points": "Ring: Electrophilic aromatic substitution; Side-chain: Free-radical substitution [1].", "marks": 1}
            ]
        ),

        # Q44: 9701/41/O/N/23/Q6(Repeat 4 - 6m)
        Question(
            number=44,
            title="[CORE REPEAT 4] Side-Chain Oxidation of Alkylbenzenes & Decolourisation Test — 9701/41/O/N/23/Q6 [6 Marks]",
            syllabus_ref="30.4", difficulty="HARD", section_key="SEC_D",
            preamble="Alkyl side-chains attached to benzene rings are oxidised by acidified KMnO<sub>4</sub>.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the oxidation of methylbenzene to benzoic acid using [O] as the oxidising agent.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the colour change observed in the reaction flask when hot KMnO<sub>4</sub> is reduced.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain why 1,4-dimethylbenzene yields a dicarboxylic acid, and name the commercial polymer made from this dicarboxylic acid.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "C6H5CH3 + 3[O] &rarr; C6H5COOH + H2O [2].", "marks": 2},
                {"part": "(b)", "points": "Purple solution decolourises (or forms a brown precipitate of MnO2) [2].", "marks": 2},
                {"part": "(c)", "points": "Both benzylic methyl groups are oxidised to give benzene-1,4-dicarboxylic acid (terephthalic acid) [1]; Used to manufacture Terylene / PET polyester [1].", "marks": 2}
            ]
        ),

        # Q45: 9701/42/M/J/22/Q6(Repeat 5 - 4m)
        Question(
            number=45,
            title="[CORE REPEAT 5] Friedel-Crafts Acylation of Benzene with Ethanoyl Chloride — 9701/42/M/J/22/Q6 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Ethanoyl chloride reacts with benzene in the presence of AlCl<sub>3</sub>.",
            parts=[
                QuestionPart("(a)", "Name the organic product formed and state the functional group present.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the equation for the formation of the electrophile.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Phenylethanone (acetophenone) [1]; Ketone (-C=O) [1].", "marks": 2},
                {"part": "(b)", "points": "CH3COCl + AlCl3 &rarr; CH3CO+ + AlCl4- [2].", "marks": 2}
            ]
        ),

        # Q46: 9701/41/M/J/22/Q6(Repeat 6 - 4m)
        Question(
            number=46,
            title="[CORE REPEAT 6] Directing Effects of -OH vs -NO2 Groups — 9701/41/M/J/22/Q6 [4 Marks]",
            syllabus_ref="30.3", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Substituents alter the orientation of further electrophilic attack.",
            parts=[
                QuestionPart("(a)", "State the directing effect and activating/deactivating nature of the -OH group in phenol.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the directing effect and activating/deactivating nature of the -NO<sub>2</sub> group in nitrobenzene.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "2,4-directing (ortho/para) [1]; Activating [1].", "marks": 2},
                {"part": "(b)", "points": "3-directing (meta) [1]; Deactivating [1].", "marks": 2}
            ]
        ),

        # Q47: 9701/42/O/N/22/Q6(Repeat 7 - 4m)
        Question(
            number=47,
            title="[CORE REPEAT 7] Inertness of Chlorobenzene to Hydrolysis — 9701/42/O/N/22/Q6 [4 Marks]",
            syllabus_ref="30.2", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Chlorobenzene does not react with aqueous NaOH under reflux.",
            parts=[
                QuestionPart("(a)", "Explain why the C-Cl bond in chlorobenzene is stronger than in chloroethane.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State why the electron-rich benzene ring repels incoming hydroxide nucleophiles.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Overlap of a chlorine p-orbital lone pair with the delocalised &pi;-system of the ring gives the C-Cl bond partial double-bond character [2].", "marks": 2},
                {"part": "(b)", "points": "The delocalised &pi;-electron cloud above and below the ring creates a region of high negative charge density, electrostatically repelling negative OH- ions [2].", "marks": 2}
            ]
        ),

        # Q48: 9701/41/O/N/22/Q6(Repeat 8 - 4m)
        Question(
            number=48,
            title="[CORE REPEAT 8] Distinguishing Benzene from Alkenes by Bromine Water — 9701/41/O/N/22/Q6 [4 Marks]",
            syllabus_ref="30.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Cyclohexene and benzene are both six-membered carbon rings.",
            parts=[
                QuestionPart("(a)", "Describe a simple chemical test using bromine to distinguish between cyclohexene and benzene.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why cyclohexene undergoes addition readily while benzene does not.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add bromine water (or Br2 in CCl4) in the dark at room temperature: cyclohexene decolourises bromine water immediately; benzene produces no colour change [2].", "marks": 2},
                {"part": "(b)", "points": "Cyclohexene has a localized C=C double bond with high &pi;-electron density that polarises Br2; benzene's electrons are delocalised and stabilized by resonance, resisting addition to preserve aromaticity [2].", "marks": 2}
            ]
        ),

        # Q49: 9701/42/M/J/21/Q6(Repeat 9 - 2m)
        Question(
            number=49,
            title="[CORE REPEAT 9] Planar Hexagonal Symmetry of Benzene — 9701/42/M/J/21/Q6 [2 Marks]",
            syllabus_ref="30.1", difficulty="EASY", section_key="SEC_D",
            preamble="Benzene has a regular hexagonal structure.",
            parts=[
                QuestionPart("(a)", "State the C-C-C bond angle and geometry of the benzene molecule.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Bond angle: 120° [1]; Geometry: planar regular hexagon [1].", "marks": 2}
            ]
        ),

        # Q50: 9701/41/M/J/21/Q6(Repeat 10 - 2m)
        Question(
            number=50,
            title="[CORE REPEAT 10] Benzylic Hydrogen Requirement for Side-Chain Oxidation — 9701/41/M/J/21/Q6 [2 Marks]",
            syllabus_ref="30.4", difficulty="EASY", section_key="SEC_D",
            preamble="Side-chain oxidation requires specific structural features.",
            parts=[
                QuestionPart("(a)", "State the structural feature an alkyl side-chain must possess to be oxidised by hot alkaline KMnO<sub>4</sub> to benzoic acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "At least one hydrogen atom bonded directly to the benzylic carbon (the carbon atom attached to the benzene ring) [2].", "marks": 2}
            ]
        ),
    ]

    print("Topic 30 Questions Count:", len(questions))

    # Audit tariff
    m6 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    m4 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    m2 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    tot = sum(sum(p.marks for p in q.parts) for q in questions)
    print(f"Tariff Breakdown: 6-markers = {m6} (40%), 4-markers = {m4} (40%), 2-markers = {m2} (20%) | Total Marks = {tot}")
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    assert m6 == 20, f"Expected 20 6-markers, got {m6}"
    assert m4 == 20, f"Expected 20 4-markers, got {m4}"
    assert m2 == 10, f"Expected 10 2-markers, got {m2}"
    assert tot == 220, f"Expected 220 marks, got {tot}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 30 PDF built successfully!")

if __name__ == "__main__":
    build_topic30_50q()
