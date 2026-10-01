"""
Script to generate Organic Chemistry Past 10 Years Practical Papers (Paper 3)
Subfolder: Urwah_Chem_Papers/Organic Chemistry/Paper 3/Past 10 Years/

1. Organic Qualitative Analysis & Functional Groups (10 questions from past 4 years: 2021-2024)
2. Organic Synthesis & Laboratory Techniques (10 questions from past 4 years: 2021-2024)
3. Synoptic Organic Analysis & Deductive Identification (10 questions from past 4 years: 2021-2024)
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_observation_table,
    COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_organic_past10years():
    styles = get_practical_styles()
    dest_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Organic Chemistry\Paper 3\Past 10 Years"
    os.makedirs(dest_dir, exist_ok=True)

    # =========================================================================
    # 1. ORGANIC QUALITATIVE ANALYSIS & FUNCTIONAL GROUPS (2021-2024)
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical: Qualitative Analysis & Functional Group Identification",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p1_questions = [
        # Q1: 2,4-DNPH
        PracticalQuestion(
            number=1,
            title="Carbonyl Identification using 2,4-Dinitrophenylhydrazine (Brady's Reagent)",
            syllabus_ref="9701/31/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Three drops of an unknown liquid are added to 1 cm<sup>3</sup> of 2,4-DNPH solution in a test-tube. "
                "A bright orange-yellow precipitate forms immediately."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the functional group class confirmed by this observation.", 2, lines_count=2,
                    mark_scheme="Carbonyl group / aldehyde or ketone (C=O) [2]."),
                PracticalSubQuestion("(b)", "Identify the type of reaction between 2,4-DNPH and a carbonyl compound.", 2, lines_count=2,
                    mark_scheme="Condensation / addition-elimination reaction [2]."),
                PracticalSubQuestion("(c)", "Describe how the purified precipitate can be used to identify the exact carbonyl compound.", 4, lines_count=4,
                    mark_scheme="Filter and wash the precipitate with cold ethanol [1]; recrystallize from minimum volume of hot solvent [1]; dry and determine the sharp melting point using a melting point apparatus [1]; compare the experimental melting point with literature melting point tables of 2,4-dinitrophenylhydrazone derivatives [1]."),
                PracticalSubQuestion("(d)", "State one safety precaution when handling 2,4-dinitrophenylhydrazine.", 2, lines_count=2,
                    mark_scheme="2,4-DNPH is harmful, a skin sensitizer, and stains skin and clothing yellow; wear nitrile gloves and handle in a well-ventilated area [2].")
            ]
        ),
        # Q2: Tollens' Reagent
        PracticalQuestion(
            number=2,
            title="Discrimination Between Aldehydes and Ketones using Tollens' Reagent",
            syllabus_ref="9701/32/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Tollens' reagent is prepared by adding dilute NaOH to aqueous AgNO3 until a brown precipitate forms, "
                "then adding dilute NH3 dropwise until the precipitate just redissolves. "
                "Organic samples are added and heated in a 60°C water bath."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the observations when Tollens' reagent is warmed with: (i) an aldehyde, (ii) a ketone.", 3, lines_count=3,
                    mark_scheme="(i) Aldehyde: A shiny silver mirror coats the inner glass wall of the tube (or dark grey precipitate of silver metal) [2]; (ii) Ketone: No reaction / solution remains clear and colorless [1]."),
                PracticalSubQuestion("(b)", "State the formula of the active silver species in Tollens' reagent.", 2, lines_count=2,
                    mark_scheme="[Ag(NH3)2]+ (diamminesilver(I) complex ion) [2]."),
                PracticalSubQuestion("(c)", "Write the half-equation for the reduction of the silver species.", 2, lines_count=2,
                    mark_scheme="[Ag(NH3)2]+ + e- -> Ag(s) + 2NH3 [2] (or Ag+ + e- -> Ag)."),
                PracticalSubQuestion("(d)", "Explain why Tollens' reagent residues must be washed away immediately after the practical session.", 3, lines_count=3,
                    mark_scheme="On standing or drying out, Tollens' solutions form silver fulminate (or silver nitride), which is dangerously shock-sensitive and explosive [3].")
            ]
        ),
        # Q3: Fehling's Solution
        PracticalQuestion(
            number=3,
            title="Fehling's Alkaline Copper(II) Test for Aliphatic Aldehydes",
            syllabus_ref="9701/34/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Fehling's solution is a mixture of aqueous copper(II) sulfate (Fehling's A) and alkaline potassium sodium tartrate (Fehling's B). "
                "When warmed in a boiling water bath with ethanal, the royal blue solution turns orange-brown."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the formula and color of the precipitate formed in a positive Fehling's test.", 2, lines_count=2,
                    mark_scheme="Copper(I) oxide, Cu2O [1]; brick-red / orange-brown precipitate [1]."),
                PracticalSubQuestion("(b)", "State the oxidation state change of copper in this reaction.", 2, lines_count=2,
                    mark_scheme="Copper is reduced from +2 (in blue Cu2+ tartrate complex) to +1 (in Cu2O) [2]."),
                PracticalSubQuestion("(c)", "Identify the organic oxidation product formed from ethanal in this alkaline medium.", 2, lines_count=2,
                    mark_scheme="Ethanoate ion, CH3COO- (or sodium ethanoate) [2]."),
                PracticalSubQuestion("(d)", "State how the reaction with Fehling's solution distinguishes aliphatic aldehydes from aromatic aldehydes (such as benzaldehyde).", 4, lines_count=4,
                    mark_scheme="Aliphatic aldehydes (e.g. ethanal, propanal) readily reduce Fehling's solution to red Cu2O [2]; aromatic aldehydes (benzaldehyde) are weaker reducing agents and fail to reduce Fehling's solution (remains blue) [2].")
            ]
        ),
        # Q4: Alcohol Oxidation with Dichromate
        PracticalQuestion(
            number=4,
            title="Classification of Alcohols using Acidified Potassium Dichromate(VI)",
            syllabus_ref="9701/35/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Three isomeric alcohols, A, B, and C (formula C4H10O), are warmed with acidified K2Cr2O7 at 60°C.<br/>"
                "• Alcohol A turns green, and its distillate oxidizes Tollens' reagent.<br/>"
                "• Alcohol B turns green, but its distillate has no reaction with Tollens'.<br/>"
                "• Alcohol C remains orange."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Classify alcohols A, B, and C as primary, secondary, or tertiary.", 3, lines_count=3,
                    mark_scheme="A is primary (1°) [1]; B is secondary (2°) [1]; C is tertiary (3°) [1]."),
                PracticalSubQuestion("(b)", "Identify the species responsible for the green color and state its oxidation number.", 2, lines_count=2,
                    mark_scheme="Chromium(III) ion, Cr3+(aq) [1]; oxidation number = +3 [1]."),
                PracticalSubQuestion("(c)", "Explain why tertiary alcohols resist oxidation by acidified dichromate.", 3, lines_count=3,
                    mark_scheme="The carbon atom bonded to the -OH group is attached to three other carbon atoms and carries no hydrogen atom (no alpha-hydrogen) [1.5]; oxidation would require breaking strong C-C bonds, which does not occur under mild conditions [1.5]."),
                PracticalSubQuestion("(d)", "Deduce the structural formula and systematic name of alcohol C.", 2, lines_count=2,
                    mark_scheme="(CH3)3COH [1]; 2-methylpropan-2-ol [1].")
            ]
        ),
        # Q5: Sodium Metal Test
        PracticalQuestion(
            number=5,
            title="Sodium Metal Effervescence Test for Alcohols and Diagnostic Hydrogen Gas Test",
            syllabus_ref="9701/31/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "A small freshly cut pellet of dry sodium metal is dropped into 2 cm<sup>3</sup> of dry ethanol in a test-tube. "
                "Vigorous effervescence is observed and the tube warms up."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Describe the laboratory test to confirm the identity of the gas evolved.", 2, lines_count=2,
                    mark_scheme="Insert a lighted wooden splint into the neck of the tube: burns with a characteristic squeaky 'pop' (hydrogen gas, H2) [2]."),
                PracticalSubQuestion("(b)", "Write the balanced chemical equation for the reaction of sodium with ethanol.", 3, lines_count=3,
                    mark_scheme="2CH3CH2OH + 2Na -> 2CH3CH2ONa + H2 [3] (1 mark for correct reactants, 1 mark for sodium ethoxide, 1 mark for balancing)."),
                PracticalSubQuestion("(c)", "Name the ionic organic salt formed in this reaction.", 2, lines_count=2,
                    mark_scheme="Sodium ethoxide [2]."),
                PracticalSubQuestion("(d)", "Explain why the ethanol sample and glassware must be completely dry before performing this test.", 3, lines_count=3,
                    mark_scheme="Sodium reacts violently with water: 2Na + 2H2O -> 2NaOH + H2 [1.5]; any trace water present will give a false positive effervescence and can cause dangerous spitting or fire [1.5].")
            ]
        ),
        # Q6: Iodoform Reaction
        PracticalQuestion(
            number=6,
            title="The Tri-iodomethane (Iodoform) Reaction for Methyl Carbonyl and Methyl Carbinol Groups",
            syllabus_ref="9701/33/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Organic liquids are warmed with aqueous iodine in sodium hydroxide solution (alkaline I2). "
                "A positive result yields a pale yellow crystalline precipitate with a distinctive antiseptic medicinal odor."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the formula and chemical name of the yellow precipitate.", 2, lines_count=2,
                    mark_scheme="CHI3 [1]; tri-iodomethane (iodoform) [1]."),
                PracticalSubQuestion("(b)", "Identify the two specific structural features that give a positive tri-iodomethane reaction.", 3, lines_count=3,
                    mark_scheme="1. CH3-C=O (methyl carbonyl / ethanoyl group attached to H or carbon) [1.5]; 2. CH3-CH(OH)- (methyl carbinol group attached to H or carbon) [1.5]."),
                PracticalSubQuestion("(c)", "State which of the following gives a positive test: (i) propan-1-ol, (ii) propan-2-ol, (iii) pentan-3-one, (iv) butanone.", 3, lines_count=3,
                    mark_scheme="Propan-2-ol [1] and butanone [1] give positive tests (contain CH3-CH(OH)- and CH3-C=O respectively); propan-1-ol and pentan-3-one give negative tests [1]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for the reaction of propan-2-ol with iodine in aqueous sodium hydroxide.", 2, lines_count=2,
                    mark_scheme="CH3CH(OH)CH3 + 4I2 + 6NaOH -> CH3COONa + CHI3 + 5NaI + 5H2O [2].")
            ]
        ),
        # Q7: Bromine Water Unsaturation
        PracticalQuestion(
            number=7,
            title="Electrophilic Addition and Unsaturation Testing with Aqueous Bromine",
            syllabus_ref="9701/34/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Bromine water, Br2(aq) (orange-brown), is shaken with an unknown hydrocarbon, Liquid X. "
                "The orange color decolourizes instantly to form a colorless mixture without any catalyst."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Deduce the functional group present in Liquid X.", 2, lines_count=2,
                    mark_scheme="Carbon-carbon double bond / alkene (C=C) / unsaturation [2]."),
                PracticalSubQuestion("(b)", "Identify the type and mechanism of this reaction.", 2, lines_count=2,
                    mark_scheme="Electrophilic addition [2]."),
                PracticalSubQuestion("(c)", "If Liquid X is cyclohexene, write the structural formula of the major product formed when reacted with aqueous bromine.", 3, lines_count=3,
                    mark_scheme="2-bromocyclohexan-1-ol (or 1,2-dibromocyclohexane) [3] (credit either halohydrin in water or dibromoalkane)."),
                PracticalSubQuestion("(d)", "Explain why alkanes (such as hexane) do not decolourize bromine water in the dark at room temperature.", 3, lines_count=3,
                    mark_scheme="Alkanes contain only strong, non-polar single sigma C-C and C-H bonds with no electron-rich pi bonds to polarize halogen molecules [1.5]; free-radical substitution requires ultraviolet (UV) light energy to homolytically cleave Br-Br bonds [1.5].")
            ]
        ),
        # Q8: Bicarbonate Carboxylic Acid Test
        PracticalQuestion(
            number=8,
            title="Diagnostic Differentiation of Carboxylic Acids from Phenols and Alcohols",
            syllabus_ref="9701/31/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Three organic compounds containing the -OH group are tested: ethanol, phenol, and propanoic acid. "
                "Solid sodium hydrogencarbonate, NaHCO3, is added to separate samples."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State which of the three compounds produces effervescence with solid NaHCO3.", 2, lines_count=2,
                    mark_scheme="Propanoic acid only [2]."),
                PracticalSubQuestion("(b)", "Explain in terms of acid strength (pKa) why propanoic acid reacts with NaHCO3 while phenol and ethanol do not.", 4, lines_count=4,
                    mark_scheme="Propanoic acid is a moderately weak acid (pKa ~ 4.9), stronger than carbonic acid (H2CO3, pKa ~ 6.4) [1.5]; it donates a proton to HCO3- to release CO2 gas [1]; phenol (pKa ~ 10) and ethanol (pKa ~ 16) are significantly weaker acids than carbonic acid and cannot protonate HCO3- [1.5]."),
                PracticalSubQuestion("(c)", "Describe how the evolved gas is confirmed as carbon dioxide.", 2, lines_count=2,
                    mark_scheme="Bubble gas through limewater: turns milky / forms a white precipitate [2]."),
                PracticalSubQuestion("(d)", "Write the ionic equation for the reaction of propanoic acid with hydrogencarbonate ions.", 2, lines_count=2,
                    mark_scheme="CH3CH2COOH(aq) + HCO3-(s or aq) -> CH3CH2COO-(aq) + CO2(g) + H2O(l) [2].")
            ]
        ),
        # Q9: Halogenoalkane Hydrolysis
        PracticalQuestion(
            number=9,
            title="Kinetics of Nucleophilic Hydrolysis of 1-Halogenoalkanes and Bond Enthalpy Ranking",
            syllabus_ref="9701/32/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Equal volumes of 1-chlorobutane, 1-bromobutane, and 1-iodobutane in ethanol are placed in test-tubes in a 50°C water bath. "
                "Aqueous silver nitrate is added simultaneously to all three tubes and the time taken for precipitation is recorded."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Rank the three halogenoalkanes in order of increasing time taken for precipitate to appear (fastest to slowest).", 3, lines_count=3,
                    mark_scheme="1-iodobutane (fastest / yellow) < 1-bromobutane (medium / cream) < 1-chlorobutane (slowest / white) [3]."),
                PracticalSubQuestion("(b)", "Explain this rate sequence by referring to carbon-halogen bond enthalpies from the Data Booklet.", 4, lines_count=4,
                    mark_scheme="Bond enthalpies: C-Cl (338 kJ mol^-1) > C-Br (276 kJ mol^-1) > C-I (238 kJ mol^-1) [2]; the rate-determining step involves breaking the C-X bond [1]; C-I has the lowest bond enthalpy and requires the least activation energy to break, hydrolyzing fastest despite having the lowest polarity [1]."),
                PracticalSubQuestion("(c)", "Explain the role of ethanol in this reaction mixture.", 2, lines_count=2,
                    mark_scheme="Acts as a mutual cosolvent: halogenoalkanes are insoluble in water, and ethanol dissolves both the organic halogenoalkane and aqueous silver nitrate to create a homogeneous mixture [2]."),
                PracticalSubQuestion("(d)", "Write the ionic equation for the hydrolysis of 1-bromobutane by water producing bromide ions.", 1, lines_count=2,
                    mark_scheme="CH3CH2CH2CH2Br + H2O -> CH3CH2CH2CH2OH + H+ + Br- [1].")
            ]
        ),
        # Q10: Microscale Esterification
        PracticalQuestion(
            number=10,
            title="Microscale Synthesis and Olfactory Identification of Esters",
            syllabus_ref="9701/35/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "10 drops of glacial ethanoic acid and 10 drops of ethanol are mixed with 3 drops of concentrated sulfuric acid. "
                "The mixture is warmed in a hot water bath at 60°C for 5 minutes, then poured into a beaker containing aqueous sodium carbonate."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the role of concentrated sulfuric acid in this reaction.", 2, lines_count=2,
                    mark_scheme="Acts as an acid catalyst [1] and dehydrating agent (absorbs water to shift equilibrium towards products) [1]."),
                PracticalSubQuestion("(b)", "Explain why the reaction mixture is poured into aqueous sodium carbonate.", 3, lines_count=3,
                    mark_scheme="To neutralize and remove excess unreacted ethanoic acid and sulfuric acid catalyst [2]; this eliminates the pungent vinegar/acid odor, making the sweet fruity smell of the ester distinct [1]."),
                PracticalSubQuestion("(c)", "State the characteristic olfactory observation that confirms ester formation.", 2, lines_count=2,
                    mark_scheme="Sweet, pleasant, fruity odor / pear drops / nail varnish remover aroma [2]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for the formation of ethyl ethanoate, showing structural formulas.", 3, lines_count=3,
                    mark_scheme="CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O [3] (reversible arrow required).")
            ]
        )
    ]

    p1_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Organic_Qualitative_Analysis.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, p1_questions, include_qa_notes=False)

    # =========================================================================
    # 2. ORGANIC SYNTHESIS & LABORATORY TECHNIQUES (2021-2024)
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical: Preparative Organic Synthesis & Laboratory Techniques",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p2_questions = [
        # Q1: Reflux Principles
        PracticalQuestion(
            number=1,
            title="The Principles, Thermodynamics, and Apparatus Setup of Heating Under Reflux",
            syllabus_ref="9701/35/M/J/22/Q2",
            total_marks=10,
            procedure_intro=(
                "In organic synthesis, many reactions between organic molecules have high activation energies and proceed very slowly at room temperature. "
                "Heating under reflux allows prolonged boiling without loss of material."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Define 'reflux' in laboratory organic chemistry.", 2, lines_count=2,
                    mark_scheme="Continuous boiling of a liquid reaction mixture such that vapors condense on a vertical condenser and drip back into the reaction vessel [2]."),
                PracticalSubQuestion("(b)", "Explain two advantages of reflux over heating in an open beaker or conical flask.", 3, lines_count=3,
                    mark_scheme="1. Prevents loss of volatile reactants, solvent, and products by evaporation [1.5]; 2. Maintains a constant, elevated reaction temperature equal to the boiling point of the mixture [1.5]."),
                PracticalSubQuestion("(c)", "State why a stopper must NEVER be placed in the top of a reflux condenser.", 3, lines_count=3,
                    mark_scheme="Creates a completely sealed, closed system [1]; heating causes gas expansion and vapor pressure to build up rapidly, causing an explosion of the glassware [2]."),
                PracticalSubQuestion("(d)", "Explain why electric heating mantles or water baths are preferred over Bunsen burners when refluxing organic liquids.", 2, lines_count=2,
                    mark_scheme="Organic liquids and vapors are highly flammable; eliminates open flames that could ignite flammable vapors [2].")
            ]
        ),
        # Q2: Anti-Bumping Granules
        PracticalQuestion(
            number=2,
            title="Physics of Boiling: Role and Mechanism of Anti-Bumping Granules",
            syllabus_ref="9701/31/O/N/21/Q2",
            total_marks=10,
            procedure_intro=(
                "Anti-bumping granules (small pieces of unglazed porcelain or carborundum) are added to distillation and reflux flasks before heating."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain the physical mechanism of how anti-bumping granules promote smooth boiling.", 4, lines_count=4,
                    mark_scheme="Granules have microscopic pores and rough surfaces containing trapped micro-pockets of air [2]; these act as nucleation sites where vapor bubbles form steadily and release smoothly [2]."),
                PracticalSubQuestion("(b)", "Describe what happens if a liquid is heated without anti-bumping granules (the phenomenon of 'bumping').", 3, lines_count=3,
                    mark_scheme="The liquid can become superheated above its normal boiling point without boiling [1.5]; sudden nucleation triggers an explosive, violent surge of large vapor bubbles that ejects hot liquid out of the flask ('bumping') [1.5]."),
                PracticalSubQuestion("(c)", "Explain why anti-bumping granules must NEVER be added to a hot liquid near its boiling point.", 3, lines_count=3,
                    mark_scheme="Adding granules to superheated liquid introduces countless nucleation sites instantly, causing instantaneous explosive flash boiling that erupts hot liquid over the user [3].")
            ]
        ),
        # Q3: Liebig Condenser Water Flow
        PracticalQuestion(
            number=3,
            title="Heat Exchanger Design: Fluid Dynamics of Liebig Condenser Water Jackets",
            syllabus_ref="9701/33/O/N/22/Q2",
            total_marks=10,
            procedure_intro=(
                "In standard distillation and reflux setups, cold water from the tap must be connected to the condenser in a specific direction."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Specify which nozzle of a Liebig condenser should be connected to the cold water inlet and which to the sink drain.", 2, lines_count=2,
                    mark_scheme="Water inlet: bottom / lower nozzle [1]; Water outlet: top / upper nozzle to drain [1]."),
                PracticalSubQuestion("(b)", "Explain the physical consequences if water is erroneously fed into the top nozzle.", 4, lines_count=4,
                    mark_scheme="Water will trickle down under gravity leaving a large air pocket / void at the top of the jacket [2]; the condenser jacket will not fill completely, resulting in poor heat transfer, incomplete condensation, and escape of flammable vapors [2]."),
                PracticalSubQuestion("(c)", "Explain why countercurrent water flow in distillation provides superior thermal efficiency.", 4, lines_count=4,
                    mark_scheme="In distillation, countercurrent flow ensures that the coolest water meets the exiting vapor at the lowest point, maximizing the temperature gradient along the entire length of the tube [2]; this guarantees complete condensation before vapors can exit into the collection adapter [2].")
            ]
        ),
        # Q4: Separating Funnel Extraction
        PracticalQuestion(
            number=4,
            title="Liquid-Liquid Extraction: Principles and Safety of Separating Funnel Procedures",
            syllabus_ref="9701/34/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "A crude preparation of 1-bromobutane (density = 1.28 g cm^-3) is washed in a separating funnel with aqueous sodium hydrogencarbonate (density ~ 1.05 g cm^-3)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State whether the 1-bromobutane layer is the upper or lower layer. Justify your answer.", 2, lines_count=2,
                    mark_scheme="Lower layer [1]; 1-bromobutane has a higher density (1.28 g cm^-3) than aqueous sodium hydrogencarbonate [1]."),
                PracticalSubQuestion("(b)", "Describe the exact procedure for shaking and venting the separating funnel during washing with aqueous NaHCO3.", 4, lines_count=4,
                    mark_scheme="Hold the stopper firmly with one hand and invert the separating funnel [1]; immediately point the stem away from all people into the back of the fume hood and open the tap/stopcock to vent pressure [1]; close tap, shake gently for 3-5 seconds, invert and vent again [1]; repeat until no further gas 'hiss' is heard, then place in retort ring stand and remove stopper [1]."),
                PracticalSubQuestion("(c)", "Identify the gas responsible for pressure buildup and write an equation for its production.", 2, lines_count=2,
                    mark_scheme="Carbon dioxide, CO2 [1]; H+(aq) + HCO3-(aq) -> H2O(l) + CO2(g) [1]."),
                PracticalSubQuestion("(d)", "Explain why the glass stopper at the top must be removed before draining liquid through the bottom stopcock.", 2, lines_count=2,
                    mark_scheme="If stopper remains in place, a partial vacuum develops inside the funnel above the liquid as it drains, which arrests liquid flow [2].")
            ]
        ),
        # Q5: Chemical Drying Agents
        PracticalQuestion(
            number=5,
            title="Selection, Mechanism, and Removal of Anhydrous Chemical Drying Agents",
            syllabus_ref="9701/32/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "After extraction in a separating funnel, the organic liquid remains cloudy due to microscopic suspended droplets of water. "
                "Anhydrous sodium sulfate, Na2SO4, is added."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State how anhydrous sodium sulfate removes water from the organic liquid.", 2, lines_count=2,
                    mark_scheme="Chemically binds water into its crystal lattice by forming hydrated salt crystals: Na2SO4(s) + 10H2O -> Na2SO4·10H2O(s) [2]."),
                PracticalSubQuestion("(b)", "State two visual indications that confirm the organic liquid is completely dry.", 3, lines_count=3,
                    mark_scheme="1. The organic liquid turns from cloudy/turbid to completely clear and transparent [1.5]; 2. The drying agent particles swirl freely like fine snow rather than sticking/clumping together at the bottom of the flask [1.5]."),
                PracticalSubQuestion("(c)", "Name two alternative anhydrous drying agents commonly used in organic chemistry.", 2, lines_count=2,
                    mark_scheme="Anhydrous calcium chloride (CaCl2) [1]; anhydrous magnesium sulfate (MgSO4) [1]."),
                PracticalSubQuestion("(d)", "Describe how the drying agent is separated from the dry liquid prior to distillation.", 3, lines_count=3,
                    mark_scheme="Careful gravity filtration through fluted filter paper in a glass funnel into a clean flask, or careful decantation of the clear liquid [3].")
            ]
        ),
        # Q6: Distillation vs Reflux in Ethanol Oxidation
        PracticalQuestion(
            number=6,
            title="Kinetic vs Thermodynamic Control in the Oxidation of Ethanol: Ethanal vs Ethanoic Acid",
            syllabus_ref="9701/33/M/J/21/Q2",
            total_marks=10,
            procedure_intro=(
                "The oxidation of ethanol can be controlled to produce either ethanal (b.p. 21°C) or ethanoic acid (b.p. 118°C).<br/>"
                "• Method A: Dropwise addition of ethanol to acidified dichromate in a distillation apparatus.<br/>"
                "• Method B: Heating ethanol with excess acidified dichromate under reflux for 30 minutes."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State which product is synthesized in Method A and which in Method B.", 2, lines_count=2,
                    mark_scheme="Method A: Ethanal, CH3CHO [1]; Method B: Ethanoic acid, CH3COOH [1]."),
                PracticalSubQuestion("(b)", "Explain why immediate distillation in Method A stops the oxidation at ethanal.", 3, lines_count=3,
                    mark_scheme="Ethanal has a very low boiling point (21°C) and vaporizes as soon as it forms [1.5]; it distills out of the reaction flask and into the receiver, removing it from further contact with the oxidizing agent [1.5]."),
                PracticalSubQuestion("(c)", "Write the balanced oxidation equations for both conversions using [O] as oxidizing agent.", 3, lines_count=3,
                    mark_scheme="Method A: CH3CH2OH + [O] -> CH3CHO + H2O [1.5]; Method B: CH3CH2OH + 2[O] -> CH3COOH + H2O [1.5]."),
                PracticalSubQuestion("(d)", "Explain why excess potassium dichromate is required in Method B.", 2, lines_count=2,
                    mark_scheme="To ensure complete oxidation of both ethanol and intermediate ethanal into ethanoic acid without unreacted alcohol remaining [2].")
            ]
        ),
        # Q7: Ice-Water Receiver Cooling
        PracticalQuestion(
            number=7,
            title="Vapor Condensation Engineering: The Use of Ice-Water Receiver Baths",
            syllabus_ref="9701/35/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "During the synthesis and distillation of volatile organic compounds with low boiling points (such as ethanal, b.p. 21°C, or propanone, b.p. 56°C), "
                "the receiving conical flask or collection vial is placed inside a beaker filled with an ice-water slurry."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why receiver cooling is essential when collecting ethanal.", 3, lines_count=3,
                    mark_scheme="Ethanal boils at 21°C, which is at or below typical laboratory ambient room temperature [1.5]; without cooling, ethanal would remain as a vapor and evaporate into the air rather than collecting as a liquid [1.5]."),
                PracticalSubQuestion("(b)", "State two hazards that arise if volatile organic vapors escape into the laboratory.", 3, lines_count=3,
                    mark_scheme="1. Fire and explosion hazard: organic vapors are highly flammable and can ignite on contact with electrical equipment or flames [1.5]; 2. Health hazard: vapors are toxic/irritants causing dizziness and respiratory irritation [1.5]."),
                PracticalSubQuestion("(c)", "Explain why an ice-water slurry is colder and more effective than dry ice blocks or ice cubes alone.", 2, lines_count=2,
                    mark_scheme="Water in the slurry provides complete liquid contact with the outer surface of the flask, maximizing surface area for rapid heat conduction [2]."),
                PracticalSubQuestion("(d)", "Suggest an additional precaution involving the receiver adapter to minimize vapor loss.", 2, lines_count=2,
                    mark_scheme="Attach an adapter with a vent tube leading into a fume cupboard or submerge receiver neck in a cold trap [2].")
            ]
        ),
        # Q8: Percentage Yield Calculations
        PracticalQuestion(
            number=8,
            title="Stoichiometric Yield Analysis and Limiting Reactant Determinations in Organic Preparations",
            syllabus_ref="9701/34/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "A student prepares ethyl ethanoate by reacting 9.20 g of ethanol (Mr = 46.0) with 15.00 g of pure ethanoic acid (Mr = 60.0) "
                "in the presence of concentrated sulfuric acid catalyst. After purification, 11.44 g of pure ethyl ethanoate (Mr = 88.0) is obtained."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the moles of ethanol and ethanoic acid used, and identify the limiting reactant.", 3, lines_count=3,
                    mark_scheme="Moles ethanol = 9.20 / 46.0 = 0.200 mol [1]; Moles ethanoic acid = 15.00 / 60.0 = 0.250 mol [1]; Ratio is 1:1 -> Ethanol is the limiting reactant [1]."),
                PracticalSubQuestion("(b)", "Calculate the theoretical yield of ethyl ethanoate in grams.", 2, lines_count=2,
                    mark_scheme="Theoretical moles = 0.200 mol [1]; Theoretical mass = 0.200 x 88.0 = 17.60 g [1]."),
                PracticalSubQuestion("(c)", "Calculate the percentage yield of ethyl ethanoate obtained.", 2, lines_count=2,
                    mark_scheme="% yield = (11.44 / 17.60) x 100 = 65.0% [2]."),
                PracticalSubQuestion("(d)", "Explain why esterification reactions never achieve 100% theoretical yield even with perfect laboratory technique.", 3, lines_count=3,
                    mark_scheme="Esterification is a reversible, dynamic equilibrium reaction: CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O [1.5]; the reaction stops when equilibrium is reached before all limiting reactant can be converted into product [1.5].")
            ]
        ),
        # Q9: Sources of Yield Loss
        PracticalQuestion(
            number=9,
            title="Systematic Analysis of Practical and Chemical Yield Loss in Multistep Preparations",
            syllabus_ref="9701/31/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "In the preparation of 1-bromobutane from butan-1-ol, the typical student yield ranges from 60% to 75%. "
                "Candidates are evaluated on identifying where the missing 25% to 40% of material is lost."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify two distinct chemical side reactions that reduce the yield of 1-bromobutane.", 4, lines_count=4,
                    mark_scheme="1. Acid-catalyzed elimination / dehydration of butan-1-ol to form gaseous but-1-ene [2]; 2. Intermolecular condensation between two butan-1-ol molecules to form di-n-butyl ether (CH3CH2CH2CH2-O-CH2CH2CH2CH3) [2]."),
                PracticalSubQuestion("(b)", "Identify two physical/mechanical avenues of product loss during the purification procedure.", 4, lines_count=4,
                    mark_scheme="1. Incomplete separation / slight solubility of 1-bromobutane in aqueous wash layers in the separating funnel [2]; 2. Liquid retained on glassware walls, drying agent residue (absorbed by Na2SO4 crystals), or left in distillation flask residue [2]."),
                PracticalSubQuestion("(c)", "Explain why washing with concentrated hydrochloric acid removes unreacted butan-1-ol.", 2, lines_count=2,
                    mark_scheme="Concentrated HCl protonates the alcohol to form an oxonium ion (CH3CH2CH2CH2OH2+), which is highly polar and dissolves into the aqueous acid layer, separating from the non-polar 1-bromobutane [2].")
            ]
        ),
        # Q10: Purity Assessment by Boiling Point
        PracticalQuestion(
            number=10,
            title="Thermometric Characterization: Determining the Purity of Liquid Organic Products",
            syllabus_ref="9701/32/O/N/24/Q2",
            total_marks=10,
            procedure_intro=(
                "The purity of a synthesized liquid product is checked by monitoring the vapor temperature during final redistillation, "
                "or by using a micro-boiling tube method with an inverted capillary tube."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Describe how the thermometer bulb must be positioned in a distillation still-head for accurate boiling point measurement.", 3, lines_count=3,
                    mark_scheme="The bulb of the thermometer must be positioned exactly level with or just below the entrance to the side-arm condenser [2]; this ensures it is completely bathed in the escaping pure equilibrium vapor entering the condenser [1]."),
                PracticalSubQuestion("(b)", "Contrast the distillation temperature profile of a pure substance with that of an impure sample.", 4, lines_count=4,
                    mark_scheme="Pure substance: Distills at a sharp, constant, fixed temperature equal to the literature boiling point (e.g. within ±0.5°C) [2]; Impure sample: Boils over a broad temperature range and the initial boiling point is depressed or elevated depending on the impurity [2]."),
                PracticalSubQuestion("(c)", "In Siwoloboff's micro-method, explain what observation signifies that the true boiling point has been reached.", 3, lines_count=3,
                    mark_scheme="As temperature rises, a rapid continuous stream of bubbles escapes from the inverted capillary [1.5]; upon extinguishing the heat, the exact boiling point is recorded when the stream of bubbles stops and liquid just rushes back up into the capillary [1.5].")
            ]
        )
    ]

    p2_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Organic_Synthesis_Techniques.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, p2_questions, include_qa_notes=False)

    # =========================================================================
    # 3. SYNOPTIC ORGANIC DEDUCTIONS (2021-2024)
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical: Synoptic Organic Deductions & Structural Elucidation",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p3_questions = [
        # Q1: C4H10O Four Isomers
        PracticalQuestion(
            number=1,
            title="Deductive Elucidation of the Four Structural Isomers of C4H10O",
            syllabus_ref="9701/31/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Four liquids, W, X, Y, and Z, are the four constitutional isomers of C4H10O.<br/>"
                "• W, X, and Y react with acidified potassium dichromate(VI) to form green solutions; Z does not react.<br/>"
                "• Only X gives a yellow precipitate with alkaline aqueous iodine.<br/>"
                "• W and Y are oxidized to aldehydes; W has a higher boiling point than Y."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify isomer Z and explain why it does not react with acidified dichromate.", 2, lines_count=2,
                    mark_scheme="Z is 2-methylpropan-2-ol ((CH3)3COH) [1]; it is a tertiary alcohol with no alpha-hydrogen atom [1]."),
                PracticalSubQuestion("(b)", "Identify isomer X and state the formula of the yellow precipitate.", 2, lines_count=2,
                    mark_scheme="X is butan-2-ol (CH3CH2CH(OH)CH3) [1]; precipitate is CHI3 [1]."),
                PracticalSubQuestion("(c)", "Identify isomers W and Y, explaining the difference in their boiling points.", 4, lines_count=4,
                    mark_scheme="W is butan-1-ol (CH3CH2CH2CH2OH); Y is 2-methylpropan-1-ol ((CH3)2CHCH2OH) [2]; W is unbranched and has greater molecular surface area of contact, resulting in stronger London dispersion forces than branched Y [2]."),
                PracticalSubQuestion("(d)", "Draw the skeletal formula of isomer X.", 2, lines_count=2,
                    mark_scheme="Correct 4-carbon chain with -OH group on C2 [2].")
            ]
        ),
        # Q2: Bifunctional C4H6O2 Acid
        PracticalQuestion(
            number=2,
            title="Deductive Identification of an Unknown Bifunctional Organic Acid (C4H6O2)",
            syllabus_ref="9701/32/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "An unknown compound, Acid P (formula C4H6O2), exhibits the following properties:<br/>"
                "• Decolourizes bromine water instantly from orange to colorless.<br/>"
                "• Gives vigorous effervescence with solid NaHCO3.<br/>"
                "• Exists as a pair of diastereomers (geometric isomers)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the two functional groups present in Acid P.", 2, lines_count=2,
                    mark_scheme="Alkene (C=C double bond) [1]; Carboxylic acid (-COOH) [1]."),
                PracticalSubQuestion("(b)", "Draw the displayed formula and state the systematic IUPAC name of Acid P.", 3, lines_count=3,
                    mark_scheme="Formula: CH3-CH=CH-COOH showing all bonds [1.5]; Name: But-2-enoic acid (or 2-butenoic acid) [1.5]."),
                PracticalSubQuestion("(c)", "Explain why Acid P exhibits geometric (cis/trans or E/Z) isomerism.", 3, lines_count=3,
                    mark_scheme="Restricted rotation around the carbon-carbon double bond (C=C) due to pi-bond overlap [1.5]; each carbon atom of the C=C double bond is bonded to two different groups (-H and -CH3 on one C; -H and -COOH on the other) [1.5]."),
                PracticalSubQuestion("(d)", "Draw and label the E and Z isomers of Acid P.", 2, lines_count=2,
                    mark_scheme="E-isomer with -CH3 and -COOH on opposite sides [1]; Z-isomer with -CH3 and -COOH on same side [1].")
            ]
        ),
        # Q3: C4H8O Carbonyl Isomers
        PracticalQuestion(
            number=3,
            title="Differentiation of Carbonyl Constitutional Isomers of Molecular Formula C4H8O",
            syllabus_ref="9701/34/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Three compounds, J, K, and L, have molecular formula C4H8O.<br/>"
                "• All three compounds react with 2,4-DNPH to form orange precipitates.<br/>"
                "• Compounds J and K reduce Tollens' reagent; compound L does not.<br/>"
                "• Compound L gives a yellow precipitate with alkaline aqueous iodine.<br/>"
                "• Compound J has an unbranched carbon chain; compound K has a branched chain."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Classify J, K, and L as aldehydes or ketones.", 2, lines_count=2,
                    mark_scheme="J and K are aldehydes (reduce Tollens') [1]; L is a ketone (fails Tollens') [1]."),
                PracticalSubQuestion("(b)", "Deduce the structural formula and systematic name of compound L.", 3, lines_count=3,
                    mark_scheme="Formula: CH3COCH2CH3 [1.5]; Name: Butanone (or butan-2-one) [1.5]."),
                PracticalSubQuestion("(c)", "Deduce the structural formula and systematic name of compound J.", 2, lines_count=2,
                    mark_scheme="Formula: CH3CH2CH2CHO [1]; Name: Butanal [1]."),
                PracticalSubQuestion("(d)", "Deduce the structural formula and systematic name of compound K.", 3, lines_count=3,
                    mark_scheme="Formula: (CH3)2CHCHO [1.5]; Name: 2-methylpropanal [1.5].")
            ]
        ),
        # Q4: Stereoisomerism in Acids
        PracticalQuestion(
            number=4,
            title="Geometric Stereoisomerism in Unsaturated Dicarboxylic Acids: Maleic vs Fumaric Acid",
            syllabus_ref="9701/33/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Compound M and Compound N are geometric isomers of butenedioic acid, HOOC-CH=CH-COOH.<br/>"
                "• Compound M (cis / Z) dehydrates readily at 130°C to form a cyclic anhydride (maleic anhydride).<br/>"
                "• Compound N (trans / E) does not form a cyclic anhydride at 130°C, requiring heating above 250°C."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Draw the structural formula of Compound M and Compound N clearly showing the geometry.", 4, lines_count=4,
                    mark_scheme="M (cis / Z): both -COOH groups on the same side of the C=C double bond [2]; N (trans / E): -COOH groups on opposite sides of the C=C double bond [2]."),
                PracticalSubQuestion("(b)", "Explain in terms of molecular geometry why Compound M easily forms a cyclic anhydride while Compound N does not.", 4, lines_count=4,
                    mark_scheme="In the Z-isomer (M), the two -COOH groups are in close spatial proximity on the same side of the double bond [2]; elimination of H2O occurs easily to form a stable 5-membered cyclic ring [1]; in the E-isomer (N), the -COOH groups are locked on opposite sides and cannot reach each other without breaking the C=C pi bond [1]."),
                PracticalSubQuestion("(c)", "State whether maleic acid or fumaric acid has a higher melting point. Explain.", 2, lines_count=2,
                    mark_scheme="Fumaric acid (trans) has a higher melting point [1]; linear trans molecules pack more tightly and symmetrically into the crystal lattice, leading to stronger intermolecular forces [1].")
            ]
        ),
        # Q5: Chiral Centre Identification
        PracticalQuestion(
            number=5,
            title="Identification and 3D Representation of Chiral Centres in Practical Unknowns",
            syllabus_ref="9701/35/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "A student hydrolyzes 2-bromobutane with aqueous sodium hydroxide. "
                "The organic product is isolated and analyzed for optical activity."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the organic product formed and state whether it possesses a chiral centre.", 2, lines_count=2,
                    mark_scheme="Butan-2-ol, CH3CH(OH)CH2CH3 [1]; possesses a chiral centre (asymmetric carbon atom, C2) [1]."),
                PracticalSubQuestion("(b)", "Identify the four different groups attached to the chiral carbon atom in this molecule.", 2, lines_count=2,
                    mark_scheme="-H, -OH, -CH3 (methyl), and -CH2CH3 (ethyl) [2]."),
                PracticalSubQuestion("(c)", "Draw 3D wedge-and-dash representations of the two non-superimposable mirror-image enantiomers.", 4, lines_count=4,
                    mark_scheme="Correct 3D tetrahedral geometry with one wedge, one dashed line, and two solid in-plane lines [2]; mirror plane drawn with non-superimposable mirror images [2]."),
                PracticalSubQuestion("(d)", "Explain how the two enantiomers behave when exposed to plane-polarized light.", 2, lines_count=2,
                    mark_scheme="One enantiomer rotates the plane of polarized light clockwise (+ / dextrorotatory); the other rotates it by the exact same angle counterclockwise (- / levorotatory) [2].")
            ]
        ),
        # Q6: Lucas Test Alcohol Classification
        PracticalQuestion(
            number=6,
            title="Classification of Alcohols using Lucas Reagent (Conc. HCl and Anhydrous ZnCl2)",
            syllabus_ref="9701/31/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Lucas reagent is a solution of anhydrous zinc chloride in concentrated hydrochloric acid. "
                "It reacts with alcohols via nucleophilic substitution to form insoluble liquid chloroalkanes, causing cloudiness."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Describe the observations and reaction times when Lucas reagent is added at room temperature to: (i) 1° alcohol, (ii) 2° alcohol, (iii) 3° alcohol.", 4, lines_count=4,
                    mark_scheme="(i) Primary (1°): Solution remains clear at room temperature (no reaction for hours) [1]; (ii) Secondary (2°): Solution turns cloudy after 3 to 5 minutes [1.5]; (iii) Tertiary (3°): Solution turns cloudy immediately within seconds, forming two distinct immiscible layers [1.5]."),
                PracticalSubQuestion("(b)", "Identify the chemical substance causing the cloudiness and phase separation.", 2, lines_count=2,
                    mark_scheme="Insoluble chloroalkane (alkyl chloride) [2]."),
                PracticalSubQuestion("(c)", "Explain the extreme difference in reaction rates in terms of carbocation stability.", 4, lines_count=4,
                    mark_scheme="The reaction proceeds via an SN1 mechanism involving a carbocation intermediate [1]; tertiary carbocations are stabilized by the positive inductive (+I) effect of three electron-releasing alkyl groups, forming almost instantly [1.5]; primary carbocations are extremely unstable, so 1° alcohols cannot react via SN1 at room temperature [1.5].")
            ]
        ),
        # Q7: Halogenoalkane by Hydrolysis & Density
        PracticalQuestion(
            number=7,
            title="Deductive Identification of an Unknown Halogenoalkane by Hydrolysis Rate and Density",
            syllabus_ref="9701/32/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "An unknown halogenoalkane, Liquid Y, has molecular formula C3H7X.<br/>"
                "• When shaken with water, Liquid Y sinks to the bottom (density > 1.0 g cm^-3).<br/>"
                "• When warmed with aqueous NaOH, acidified with HNO3, and tested with AgNO3, a cream precipitate forms within 2 minutes.<br/>"
                "• The cream precipitate is insoluble in dilute NH3 but dissolves in concentrated NH3."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the halogen atom present in Liquid Y from the silver nitrate test.", 2, lines_count=2,
                    mark_scheme="Bromine (forms cream precipitate of AgBr soluble in concentrated NH3) [2]."),
                PracticalSubQuestion("(b)", "Liquid Y exists as two constitutional isomers. Draw and name both isomers.", 4, lines_count=4,
                    mark_scheme="1. 1-bromopropane: CH3CH2CH2Br [2]; 2. 2-bromopropane: CH3CH(Br)CH3 [2]."),
                PracticalSubQuestion("(c)", "When hydrolysed, the resulting alcohol does NOT give a yellow precipitate with alkaline aqueous iodine. Deduce the exact structure of Liquid Y.", 2, lines_count=2,
                    mark_scheme="1-bromopropane [1]; hydrolysis gives propan-1-ol, which does not contain the CH3-CH(OH)- group and thus gives a negative iodoform test (whereas 2-bromopropane would yield propan-2-ol, giving a positive iodoform test) [1]."),
                PracticalSubQuestion("(d)", "Write the ionic equation for the precipitation of silver bromide.", 2, lines_count=2,
                    mark_scheme="Ag+(aq) + Br-(aq) -> AgBr(s) [2].")
            ]
        ),
        # Q8: Nitrogenous Unknown
        PracticalQuestion(
            number=8,
            title="Diagnostic Deductions of Nitrogen-Containing Organic Compounds: Amines vs Amides",
            syllabus_ref="9701/34/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Compound Q is an organic liquid containing nitrogen.<br/>"
                "• When tested with universal indicator paper, Q turns paper blue-green (pH ~ 9).<br/>"
                "• When glass rod dipped in concentrated HCl is held near open bottle of Q, dense white fumes form.<br/>"
                "• When Q is mixed with ethanoyl chloride, vigorous reaction occurs forming misty acidic fumes and a white solid."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the functional group class of Compound Q.", 2, lines_count=2,
                    mark_scheme="Primary amine (or secondary amine / amino group -NH2) [2]."),
                PracticalSubQuestion("(b)", "Identify the chemical formula of the white fumes formed with concentrated HCl.", 2, lines_count=2,
                    mark_scheme="Alkylammonium chloride salt, R-NH3+Cl- (e.g. CH3CH2NH3Cl) [2]."),
                PracticalSubQuestion("(c)", "Explain why amines act as Bronsted-Lowry bases in aqueous solution.", 3, lines_count=3,
                    mark_scheme="The nitrogen atom possesses a non-bonding lone pair of electrons [1.5]; it can accept a proton (H+) by forming a dative covalent bond: R-NH2 + H+ -> R-NH3+ [1.5]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for the reaction of ethylamine with ethanoyl chloride.", 3, lines_count=3,
                    mark_scheme="CH3CH2NH2 + CH3COCl -> CH3CONHCH2CH3 + HCl (forms N-ethylethanamide) [3].")
            ]
        ),
        # Q9: Combustion & Titration Mr
        PracticalQuestion(
            number=9,
            title="Deductive Structure Determination Combining Elemental Analysis and Titrimetric Mr",
            syllabus_ref="9701/35/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "A solid organic acid, Compound R, contains 40.0% C, 6.7% H, and 53.3% O by mass.<br/>"
                "A 0.900 g sample of Compound R is dissolved in water and titrated with 0.200 mol dm^-3 NaOH. "
                "Exactly 50.00 cm<sup>3</sup> of NaOH is required to reach the phenolphthalein endpoint."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the empirical formula of Compound R. [Ar: C = 12.0, H = 1.0, O = 16.0]", 3, lines_count=3,
                    mark_scheme="Moles C = 40.0 / 12.0 = 3.33; Moles H = 6.7 / 1.0 = 6.7; Moles O = 53.3 / 16.0 = 3.33 [1.5]; Ratio = 1:2:1 -> Empirical formula = CH2O [1.5]."),
                PracticalSubQuestion("(b)", "Calculate the moles of NaOH reacted and determine the relative molecular mass (Mr) of Compound R, assuming it is a monoprotic acid.", 3, lines_count=3,
                    mark_scheme="Moles NaOH = 0.200 x 0.0500 = 0.0100 mol [1]; Moles acid = 0.0100 mol [1]; Mr = 0.900 / 0.0100 = 90.0 g mol^-1 [1]."),
                PracticalSubQuestion("(c)", "Determine the molecular formula of Compound R.", 2, lines_count=2,
                    mark_scheme="Empirical mass CH2O = 12 + 2 + 16 = 30.0; Multiple = 90.0 / 30.0 = 3; Molecular formula = C3H6O3 [2]."),
                PracticalSubQuestion("(d)", "Compound R gives a positive tri-iodomethane (iodoform) test. Deduce the structural formula and systematic name of Compound R.", 2, lines_count=2,
                    mark_scheme="CH3-CH(OH)-COOH [1]; 2-hydroxypropanoic acid (lactic acid) [1].")
            ]
        ),
        # Q10: Comprehensive Synoptic Unknown Flowchart
        PracticalQuestion(
            number=10,
            title="Comprehensive Laboratory Decision Tree for the Identification of Unknown Organic Liquids",
            syllabus_ref="9701/33/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Candidates in AS Chemistry practical exams are presented with unknown liquids and must follow a logical, systematic deductive sequence."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the first test performed to determine if an unknown liquid is a carbonyl compound.", 2, lines_count=2,
                    mark_scheme="Add 2,4-dinitrophenylhydrazine (2,4-DNPH / Brady's reagent): bright orange-yellow precipitate confirms a carbonyl (aldehyde or ketone) [2]."),
                PracticalSubQuestion("(b)", "If the 2,4-DNPH test is positive, state the definitive test used to distinguish whether it is an aldehyde or ketone.", 2, lines_count=2,
                    mark_scheme="Tollens' reagent warmed in a water bath: silver mirror confirms aldehyde; clear solution confirms ketone [2] (or Fehling's solution)."),
                PracticalSubQuestion("(c)", "If the 2,4-DNPH test is negative, state the test used to check for a carboxylic acid versus an alcohol.", 3, lines_count=3,
                    mark_scheme="Add solid sodium hydrogencarbonate (NaHCO3): rapid effervescence of CO2 confirms carboxylic acid [1.5]; if negative, test with dry sodium metal: effervescence of H2 confirms an alcohol [1.5]."),
                PracticalSubQuestion("(d)", "If an alcohol is confirmed, state how to differentiate primary/secondary from tertiary alcohols.", 3, lines_count=3,
                    mark_scheme="Warm with acidified potassium dichromate(VI): color change from orange to green confirms 1° or 2° alcohol; remaining orange confirms 3° alcohol [3].")
            ]
        )
    ]

    p3_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Synoptic_Organic_Deductions.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, p3_questions, include_qa_notes=False)

    print("=== Organic Chemistry Past 10 Years Suite Complete (3 Papers) ===")

if __name__ == "__main__":
    build_organic_past10years()
