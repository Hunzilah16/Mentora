"""
Script to generate Organic Chemistry Practical Papers (Paper 3)
1. Organic Qualitative Analysis: Systematic Functional Group Identification
2. Organic Synthesis & Laboratory Techniques (Reflux, Distillation, Extraction, Purity)
3. Synoptic Organic Analysis & Deductive Identification (Isomer Elucidation)
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_observation_table,
    COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_all_organic_practicals():
    styles = get_practical_styles()
    base_dest = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Organic Chemistry\Paper 3"
    os.makedirs(base_dest, exist_ok=True)

    # =========================================================================
    # 1. ORGANIC QUALITATIVE ANALYSIS: FUNCTIONAL GROUP IDENTIFICATION
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical 1: Qualitative Analysis — Functional Group Identification",
        subtitle="Systematic Diagnostic Test-Tube Reactions of Alcohols, Carbonyls, Carboxylic Acids & Halogenoalkanes",
        component_name="Paper 3 — Advanced Practical Skills (Organic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p1_q1 = PracticalQuestion(
        number=1,
        title="Diagnostic Differentiation of Alcohols, Aldehydes, and Ketones: FA 1, FA 2, and FA 3",
        syllabus_ref="9701/33/M/J/22/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three unlabelled organic liquids: <b>FA 1</b>, <b>FA 2</b>, and <b>FA 3</b>.<br/>"
            "Each liquid is one of the following compounds: <b>propan-1-ol</b> (primary alcohol), <b>propanal</b> (aldehyde), or <b>propanone</b> (ketone).<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Acidified potassium dichromate(VI), K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / dilute H<sub>2</sub>SO<sub>4</sub><br/>"
            "• Tollens' reagent (prepared freshly from AgNO<sub>3</sub>, dilute NaOH, and dilute NH<sub>3</sub>)<br/>"
            "• Fehling's solution (equal volumes of Fehling's A and Fehling's B)<br/>"
            "• 2,4-dinitrophenylhydrazine (2,4-DNPH / Brady's reagent)<br/>"
            "• Dry sodium metal pieces (stored under paraffin oil).<br/><br/>"
            "<b>Safety Precautions:</b><br/>"
            "• Organic compounds and 2,4-DNPH are flammable and harmful. 2,4-DNPH stains skin and clothing.<br/>"
            "• NEVER heat organic mixtures directly over an open Bunsen burner flame. Always use a hot water bath."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Carry out the specified diagnostic tests on FA 1, FA 2, and FA 3. Record all observations in the table below.",
                marks=8,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>Brady's Reagent Test:</b><br/>To 5 drops of organic sample, add 1 cm<sup>3</sup> of 2,4-DNPH reagent.", "", ""),
                    ("<b>Tollens' Silver Mirror Test:</b><br/>To 1 cm<sup>3</sup> of fresh Tollens' reagent, add 5 drops of organic sample and warm in a water bath at 60°C for 5 minutes.", "", ""),
                    ("<b>Fehling's Alkaline Copper Test:</b><br/>To 1 cm<sup>3</sup> of mixed Fehling's solution, add 5 drops of organic sample and warm in a boiling water bath for 3 minutes.", "", ""),
                    ("<b>Dichromate Oxidation Test:</b><br/>To 1 cm<sup>3</sup> of acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>, add 5 drops of organic sample and warm gently in a water bath.", "", ""),
                    ("<b>Sodium Metal Test:</b><br/>To 1 cm<sup>3</sup> of dry organic liquid in a dry test-tube, add a small freshly cut piece of sodium metal.", "", "")
                ]),
                mark_scheme=(
                    "2,4-DNPH test: FA 1 gives no precipitate / remains yellow solution; FA 2 and FA 3 give bright orange-yellow precipitate [2].<br/>"
                    "Tollens' test: FA 1 and FA 3 show no reaction / solution remains colorless; FA 2 produces a shiny silver mirror on the tube walls (or dark grey ppt) [2].<br/>"
                    "Fehling's test: FA 2 turns from deep royal blue to form a brick-red / orange-brown precipitate of Cu2O; FA 1 and FA 3 remain deep blue [1].<br/>"
                    "Acidified dichromate test: FA 1 and FA 2 turn from orange to green (Cr3+); FA 3 shows no reaction / remains orange [2].<br/>"
                    "Sodium metal test: FA 1 effervesces / produces bubbles of H2 gas; FA 2 and FA 3 show no gas evolution [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="From your experimental observations, identify the chemical identity of FA 1, FA 2, and FA 3 and provide concise justifications for each deduction.",
                marks=6,
                lines_count=5,
                mark_scheme=(
                    "FA 1 is propan-1-ol [1]: negative 2,4-DNPH (not a carbonyl), oxidized by acidified dichromate (turns green), effervesces with sodium metal (contains -OH group) [1].<br/>"
                    "FA 2 is propanal [1]: positive 2,4-DNPH (contains C=O carbonyl), oxidized by Tollens' and Fehling's (aldehyde group -CHO) [1].<br/>"
                    "FA 3 is propanone [1]: positive 2,4-DNPH (carbonyl), but negative Tollens', Fehling's, and dichromate tests (ketone resist oxidation under mild conditions) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write the balanced chemical equation for the reaction of propan-1-ol (FA 1) with sodium metal. Name the organic product formed.",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Equation: 2CH3CH2CH2OH + 2Na -> 2CH3CH2CH2ONa + H2 (or CH3CH2CH2OH + Na -> CH3CH2CH2ONa + 1/2 H2) [1].<br/>"
                    "Name: Sodium propoxide [1]."
                )
            ),
            PracticalSubQuestion(
                label="(d)",
                text="State the identity of the transition metal species responsible for the color change from orange to green when propanal is warmed with acidified potassium dichromate(VI), giving its oxidation number.",
                marks=2,
                lines_count=3,
                mark_scheme="Species: Chromium(III) ion / Cr3+(aq) [1]; Oxidation number: +3 (reduced from +6 in Cr2O7^2-) [1]."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Describe how the silver mirror formed in the Tollens' test on propanal should be safely removed and cleaned from the glassware at the end of the practical session.",
                marks=2,
                lines_count=3,
                mark_scheme="Dissolve the silver mirror with dilute nitric acid (HNO3) in a fume cupboard [1]; Silver fulminate (explosive) can form if Tollens' residues dry out or are left standing, so all solutions must be rinsed immediately with copious water down the sink [1]."
            )
        ]
    )

    p1_q2 = PracticalQuestion(
        number=2,
        title="Identification of Halogenoalkanes and Carboxylic Acids: FA 4, FA 5, and FA 6",
        syllabus_ref="9701/34/O/N/23/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three liquids: <b>FA 4</b>, <b>FA 5</b>, and <b>FA 6</b>.<br/>"
            "Each liquid is one of the following: <b>ethanoic acid</b>, <b>1-chlorobutane</b>, or <b>1-bromobutane</b>.<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Solid sodium hydrogencarbonate, NaHCO<sub>3</sub>(s)<br/>"
            "• Aqueous sodium hydroxide, NaOH(aq), 2.0 mol dm<sup>-3</sup><br/>"
            "• Dilute nitric acid, HNO<sub>3</sub>, 2.0 mol dm<sup>-3</sup><br/>"
            "• Aqueous silver nitrate, AgNO<sub>3</sub>, 0.05 mol dm<sup>-3</sup><br/>"
            "• Dilute aqueous ammonia, NH<sub>3</sub>, 1.0 mol dm<sup>-3</sup><br/>"
            "• Concentrated aqueous ammonia, conc. NH<sub>3</sub>, 8.0 mol dm<sup>-3</sup> (fume cupboard)<br/>"
            "• Fresh limewater, Ca(OH)<sub>2</sub>(aq)."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Perform the diagnostic tests specified below and complete the observation table.",
                marks=8,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>Bicarbonate Test:</b><br/>To 1 cm depth of FA 4, FA 5, and FA 6 in separate tubes, add a spatula-tip of solid NaHCO<sub>3</sub>. Test any evolved gas with limewater.", "", ""),
                    ("<b>Alkaline Hydrolysis & Halide Test:</b><br/>To 1 cm depth of FA 5 and FA 6 in separate tubes:<br/>(i) Add 2 cm depth of NaOH(aq) and heat in a boiling water bath for 5 minutes.<br/>(ii) Cool, acidify with dilute HNO<sub>3</sub> until acidic to litmus.<br/>(iii) Add 5 drops of aqueous AgNO<sub>3</sub>.", "", ""),
                    ("<b>Ammonia Confirmation Test:</b><br/>To the precipitates obtained from the hydrolysis of FA 5 and FA 6:<br/>(i) Add excess dilute aqueous NH<sub>3</sub>.<br/>(ii) If insoluble, add concentrated aqueous NH<sub>3</sub>.", "", "")
                ]),
                mark_scheme=(
                    "NaHCO3 test: FA 4 gives vigorous effervescence / bubbling, gas turns limewater milky; FA 5 and FA 6 show no reaction / no bubbling [2].<br/>"
                    "Hydrolysis + AgNO3 test: FA 5 gives a white precipitate [1]; FA 6 gives a cream precipitate [1].<br/>"
                    "Relative rate: Precipitate forms noticeably faster in FA 6 than in FA 5 [1].<br/>"
                    "Ammonia test: FA 5 white precipitate dissolves completely in dilute aqueous ammonia [1]; FA 6 cream precipitate is insoluble in dilute ammonia but dissolves in concentrated ammonia [2]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Deduce the identity of FA 4, FA 5, and FA 6.",
                marks=3,
                lines_count=3,
                mark_scheme="FA 4 is ethanoic acid [1]; FA 5 is 1-chlorobutane [1]; FA 6 is 1-bromobutane [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write an ionic equation, with state symbols, for the reaction between ethanoic acid and hydrogencarbonate ions in the bicarbonate test.",
                marks=2,
                lines_count=3,
                mark_scheme="CH3COOH(l or aq) + HCO3-(aq or s) -> CH3COO-(aq) + CO2(g) + H2O(l) [2] (1 mark for correct formulae, 1 mark for state symbols)."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Explain why the hydrolysis mixture must be acidified with dilute nitric acid BEFORE adding aqueous silver nitrate.",
                marks=2,
                lines_count=3,
                mark_scheme="To neutralize the unreacted excess sodium hydroxide (OH- ions) [1]; otherwise OH- ions would react with Ag+ to precipitate brown silver(I) oxide (Ag2O), masking or giving a false test for halide ions [1]."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Compare the relative rates of hydrolysis of 1-chlorobutane (FA 5) and 1-bromobutane (FA 6). Explain this difference in rate by reference to bond parameters from the Cambridge Data Booklet.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "1-bromobutane hydrolyzes faster than 1-chlorobutane (cream precipitate appears more rapidly) [1].<br/>"
                    "The rate of nucleophilic substitution is determined by the strength / bond enthalpy of the carbon-halogen bond (C-X), not bond polarity [1].<br/>"
                    "The C-Br bond enthalpy (276 kJ mol^-1) is lower than the C-Cl bond enthalpy (338 kJ mol^-1) [1].<br/>"
                    "Because bromine has a larger atomic radius than chlorine, orbital overlap with carbon is poorer, so less activation energy is required to break the C-Br bond [1]."
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Write the general ionic equation for the nucleophilic substitution hydrolysis of 1-bromobutane with hydroxide ions.",
                marks=1,
                lines_count=2,
                mark_scheme="CH3CH2CH2CH2Br + OH- -> CH3CH2CH2CH2OH + Br- [1]."
            )
        ]
    )

    p1_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Organic_Qualitative_Analysis.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, [p1_q1, p1_q2], include_qa_notes=False)

    # =========================================================================
    # 2. ORGANIC SYNTHESIS & LABORATORY TECHNIQUES
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical 2: Laboratory Techniques & Preparative Organic Synthesis",
        subtitle="Reflux Condensation, Simple/Fractional Distillation, Separating Funnel Extraction & Purity Metrics",
        component_name="Paper 3 — Advanced Practical Skills (Organic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p2_q1 = PracticalQuestion(
        number=1,
        title="Laboratory Preparation and Purification of 1-Bromobutane from Butan-1-ol",
        syllabus_ref="9701/35/O/N/22/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Preparative Organic Synthesis Task:</b><br/>"
            "A student prepares 1-bromobutane according to the following reaction:<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH + NaBr + H<sub>2</sub>SO<sub>4</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>Br + NaHSO<sub>4</sub> + H<sub>2</sub>O<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Place 13.0 g of sodium bromide and 15 cm<sup>3</sup> of water into a 100 cm<sup>3</sup> round-bottomed flask. Cool the flask in an ice-water bath.<br/>"
            "2. Slowly add 10 cm<sup>3</sup> of concentrated sulfuric acid with constant swirling.<br/>"
            "3. Add 7.40 g (9.15 cm<sup>3</sup>) of butan-1-ol and 2-3 anti-bumping granules.<br/>"
            "4. Fit a water-cooled Liebig condenser vertically in the reflux position. Boil under gentle reflux for 45 minutes.<br/>"
            "5. Rearrange the apparatus for distillation and distill until no more oily droplets collect in the receiver.<br/>"
            "6. Transfer the distillate into a separating funnel. Separate the organic layer from the aqueous layer.<br/>"
            "7. Wash the organic layer with an equal volume of concentrated hydrochloric acid, then with aqueous sodium hydrogencarbonate, and finally with distilled water.<br/>"
            "8. Transfer the cloudy organic liquid to a small conical flask, add anhydrous sodium sulfate, and swirl until clear.<br/>"
            "9. Decant into a clean pear-shaped flask and redistill, collecting the pure fraction boiling between 101°C and 104°C."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="State the purpose of adding anti-bumping granules to the reaction mixture before heating under reflux.",
                marks=2,
                lines_count=3,
                mark_scheme="To provide nucleation sites for smooth bubble formation [1], preventing violent boiling, uneven surging, or 'bumping' of the liquid out of the flask [1]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Explain why the reaction mixture must be heated under reflux rather than in an open flask or beaker.",
                marks=2,
                lines_count=3,
                mark_scheme="To prevent the loss of volatile organic reactants (butan-1-ol) and products (1-bromobutane) by evaporation [1], while allowing the reaction to proceed continuously at its boiling temperature [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="State the direction of water flow through the Liebig condenser jacket during reflux and explain why this direction is essential.",
                marks=2,
                lines_count=3,
                mark_scheme="Water enters at the bottom (lower inlet) and leaves at the top (upper outlet) [1]; this ensures the condenser jacket fills completely with cold water without trapping air bubbles or air pockets, ensuring efficient cooling [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="1-Bromobutane has a density of 1.28 g cm^-3, whereas water has a density of 1.00 g cm^-3.<br/>(i) State whether the organic product forms the upper or lower layer in the separating funnel.<br/>(ii) Describe the safety precaution required when shaking the separating funnel with aqueous sodium hydrogencarbonate.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "(i) Lower layer (since its density of 1.28 g cm^-3 is greater than water) [1].<br/>"
                    "(ii) Periodically invert the separating funnel and open the stopcock / tap [1] to release pressure buildup caused by the evolution of carbon dioxide gas (CO2) from neutralizing acid residues [1]."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="State the role of anhydrous sodium sulfate in step 8 and state how the student knows by visual inspection that the organic liquid is completely dry.",
                marks=2,
                lines_count=3,
                mark_scheme="Role: Acts as a chemical drying agent to absorb and remove trace dissolved water [1]; Visual check: The liquid turns from turbid / cloudy / milky to completely clear / transparent, and the solid drying agent moves freely without sticking / clumping to the glass [1]."
            ),
            PracticalSubQuestion(
                label="(f)",
                text="In this preparation, 7.40 g of butan-1-ol (Mr = 74.0) was used with excess NaBr and H2SO4. The student collected 9.59 g of pure 1-bromobutane (Mr = 137.0).<br/>Calculate the theoretical yield of 1-bromobutane in grams and calculate the percentage yield obtained.",
                marks=5,
                lines_count=5,
                mark_scheme=(
                    "Moles of butan-1-ol = 7.40 / 74.0 = 0.100 mol [1].<br/>"
                    "Mole ratio of butan-1-ol to 1-bromobutane is 1:1, so theoretical moles = 0.100 mol [1].<br/>"
                    "Theoretical yield = 0.100 x 137.0 = 13.70 g [1].<br/>"
                    "Actual yield = 9.59 g [1].<br/>"
                    "Percentage yield = (9.59 / 13.70) x 100 = 70.0% (allow 70.0% - 70.1%) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Suggest two realistic experimental reasons why the actual percentage yield of 1-bromobutane is significantly below 100%.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "1. Incomplete reaction / reversible equilibrium or side reactions occurring (e.g. elimination to form but-1-ene gas or condensation to form di-n-butyl ether) [2].<br/>"
                    "2. Mechanical losses during transfers between glassware (flask to condenser, separating funnel stopcock, conical flask drying, redistillation residue left in boiling flask) [2]."
                )
            )
        ]
    )

    p2_q2 = PracticalQuestion(
        number=2,
        title="Distillation vs Reflux in the Oxidation of Ethanol and Determination of Product Purity",
        syllabus_ref="9701/33/M/J/21/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Comparative Laboratory Investigation:</b><br/>"
            "The controlled oxidation of ethanol (CH<sub>3</sub>CH<sub>2</sub>OH, b.p. 78°C) by acidified potassium dichromate(VI) can yield either:<br/>"
            "• <b>Product A:</b> Ethanal (CH<sub>3</sub>CHO, b.p. 21°C)<br/>"
            "• <b>Product B:</b> Ethanoic acid (CH<sub>3</sub>COOH, b.p. 118°C)<br/><br/>"
            "<b>Apparatus Setups:</b><br/>"
            "• <b>Method 1:</b> Ethanol is added dropwise to acidified dichromate in a pear-shaped flask fitted with a still-head, thermometer, and Liebig condenser set for simple distillation. The receiver is immersed in an ice-water bath.<br/>"
            "• <b>Method 2:</b> Excess acidified potassium dichromate is heated under reflux with ethanol for 30 minutes, followed by distillation.<br/><br/>"
            "<b>Experimental Data:</b><br/>"
            "Boiling points: Ethanal = 21°C, Ethanol = 78°C, Ethanoic acid = 118°C, Water = 100°C."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="State which method (Method 1 or Method 2) prepares ethanal as the major product. Explain why the apparatus setup in this method succeeds in preventing ethanal from oxidizing further.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "Method 1 prepares ethanal [1].<br/>"
                    "Explanation: Ethanal has a very low boiling point (21°C) compared to ethanol (78°C) and ethanoic acid (118°C) [1].<br/>"
                    "In Method 1 (distillation), as soon as ethanal forms, it vaporizes immediately and distills over out of the reaction flask [1], removing it from contact with the oxidizing agent before it can be further oxidized to ethanoic acid [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Explain why the receiving flask in Method 1 must be kept thoroughly cooled in an ice-water bath.",
                marks=2,
                lines_count=3,
                mark_scheme="Ethanal has a boiling point of only 21°C (close to room temperature) and high volatility [1]; ice-cooling condenses the vapor and prevents ethanal escaping as flammable vapor into the laboratory [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write the chemical equation for the oxidation of ethanol to ethanoic acid under reflux in Method 2, using [O] to represent the oxidizing agent.",
                marks=2,
                lines_count=3,
                mark_scheme="CH3CH2OH + 2[O] -> CH3COOH + H2O [2] (1 mark for correct formulas, 1 mark for balancing 2[O] and H2O)."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="State the observation made in the reaction flask during the oxidation of ethanol by acidified potassium dichromate(VI).",
                marks=2,
                lines_count=3,
                mark_scheme="The solution turns from orange (Cr2O7^2-) to dark green (Cr3+) [2] (1 mark for orange, 1 mark for green)."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Describe a chemical test on the distillate collected in Method 1 that would confirm the presence of unoxidized ethanol impurity.",
                marks=3,
                lines_count=4,
                mark_scheme="Add a small dry piece of sodium metal: effervescence / bubbles of hydrogen gas produced confirms ethanol [2] (or add PCl5: steamy acidic fumes of HCl that turn damp blue litmus red confirms -OH group [2])."
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Describe how a student can determine the purity of the synthesized liquid product using a simple boiling-point determination technique. State how the boiling point of an impure liquid compares with that of the pure compound.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "Technique: Set up a distillation apparatus with a sensitive thermometer placed with its bulb level with the side-arm condenser entrance [1], or use a micro-boiling tube method (Siwoloboff's method with inverted capillary) [1].<br/>"
                    "Pure compound: Distills at a sharp, constant boiling point identical to literature value (e.g. exactly 118°C for ethanoic acid) [1].<br/>"
                    "Impure compound: Boils over a broad temperature range and the observed boiling point is elevated or shifted compared to the pure substance [1]."
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Identify one major hazard associated with handling concentrated sulfuric acid and ethanol during this preparation and specify the appropriate safety measure.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Hazard: Concentrated sulfuric acid is highly corrosive and causes severe skin burns; reaction with alcohol is violently exothermic; ethanol is highly flammable [2].<br/>"
                    "Safety measure: Add acid slowly with continuous cooling in ice and swirling; wear chemical-resistant nitrile gloves and goggles; keep ethanol away from open Bunsen flames by using an electric heating mantle or water bath [1]."
                )
            )
        ]
    )

    p2_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Organic_Synthesis_Techniques.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, [p2_q1, p2_q2], include_qa_notes=False)

    # =========================================================================
    # 3. SYNOPTIC ORGANIC DEDUCTIONS
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Organic Chemistry Practical 3: Synoptic Organic Analysis & Deductive Identification",
        subtitle="Multi-Step Structural Elucidation of Unknowns from Bench Microscale Tests and Titrimetric Data",
        component_name="Paper 3 — Advanced Practical Skills (Organic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p3_q1 = PracticalQuestion(
        number=1,
        title="Structural Elucidation of Four Isomeric C4H10O Alcohols: FA 1, FA 2, FA 3, and FA 4",
        syllabus_ref="9701/31/M/J/23/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Synoptic Deductive Problem:</b><br/>"
            "Four unlabelled colourless liquids, <b>FA 1</b>, <b>FA 2</b>, <b>FA 3</b>, and <b>FA 4</b>, are the four structural isomers of formula <b>C<sub>4</sub>H<sub>10</sub>O</b>.<br/>"
            "The possible structural isomers are:<br/>"
            "• <b>Butan-1-ol:</b> CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH (primary)<br/>"
            "• <b>Butan-2-ol:</b> CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub> (secondary)<br/>"
            "• <b>2-Methylpropan-1-ol:</b> (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>OH (primary branched)<br/>"
            "• <b>2-Methylpropan-2-ol:</b> (CH<sub>3</sub>)<sub>3</sub>COH (tertiary)<br/><br/>"
            "<b>Diagnostic Bench Tests Carried Out:</b><br/>"
            "• <b>Test 1:</b> Warm with acidified potassium dichromate(VI) at 60°C.<br/>"
            "• <b>Test 2:</b> Warm with alkaline aqueous iodine (I<sub>2</sub> in aqueous NaOH, tri-iodomethane reaction).<br/>"
            "• <b>Test 3:</b> Distill the oxidation product of primary/secondary isomers and test the distillate with Tollens' reagent.<br/>"
            "• <b>Test 4:</b> Add concentrated HCl and anhydrous zinc chloride (Lucas test) at room temperature."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="The results of the bench tests are summarized below. Complete the deduction column in the table.",
                marks=6,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>FA 1:</b><br/>• Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> turns green.<br/>• Alkaline I<sub>2</sub>: no precipitate.<br/>• Distilled oxidation product gives silver mirror with Tollens'.", "Color change: orange to green.<br/>No yellow precipitate.<br/>Shiny silver mirror formed.", ""),
                    ("<b>FA 2:</b><br/>• Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> turns green.<br/>• Alkaline I<sub>2</sub>: bright yellow crystalline precipitate with antiseptic medicinal smell.<br/>• Oxidation product gives no silver mirror.", "Color change: orange to green.<br/>Yellow crystalline precipitate formed.<br/>Solution remains clear with Tollens'.", ""),
                    ("<b>FA 3:</b><br/>• Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> turns green.<br/>• Alkaline I<sub>2</sub>: no precipitate.<br/>• Distilled oxidation product gives silver mirror with Tollens'.<br/>• Lucas test: remains clear after 30 min.", "Color change: orange to green.<br/>No yellow precipitate.<br/>Shiny silver mirror formed.<br/>No cloudiness at room temp.", ""),
                    ("<b>FA 4:</b><br/>• Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> remains orange.<br/>• Alkaline I<sub>2</sub>: no precipitate.<br/>• Lucas test: immediately turns cloudy forming two layers within 1 minute.", "No color change (solution remains orange).<br/>No precipitate.<br/>Instant cloudiness/phase separation.", "")
                ]),
                mark_scheme=(
                    "FA 1 deduction: Primary alcohol, straight-chain / unbranched (butan-1-ol) [2].<br/>"
                    "FA 2 deduction: Secondary alcohol containing CH3-CH(OH)- group (butan-2-ol) [2].<br/>"
                    "FA 3 deduction: Primary alcohol with branch (2-methylpropan-1-ol) [1].<br/>"
                    "FA 4 deduction: Tertiary alcohol resistant to oxidation (2-methylpropan-2-ol) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Draw the displayed formula and state the systematic IUPAC name for each of the four isomeric compounds FA 1, FA 2, FA 3, and FA 4.",
                marks=6,
                lines_count=6,
                mark_scheme=(
                    "FA 1: butan-1-ol, displayed formula showing all C-H, C-C, C-O, O-H bonds clearly [1.5].<br/>"
                    "FA 2: butan-2-ol, displayed formula showing -OH on C2 [1.5].<br/>"
                    "FA 3: 2-methylpropan-1-ol, displayed formula showing methyl branch on C2 and -OH on C1 [1.5].<br/>"
                    "FA 4: 2-methylpropan-2-ol, displayed formula showing central C bonded to 3 methyl groups and -OH [1.5]."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Explain why FA 4 does not react with acidified potassium dichromate(VI).",
                marks=2,
                lines_count=3,
                mark_scheme="FA 4 is a tertiary alcohol [1]; the carbon atom bonded to the -OH group has no hydrogen atom attached to it (no alpha-hydrogen), so C-C bonds would have to be broken for oxidation to take place [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Write the chemical formula of the yellow crystalline precipitate formed in the alkaline iodine test with FA 2 and write an ionic or balanced equation for its formation.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Formula: CHI3 (tri-iodomethane / iodoform) [1].<br/>"
                    "Equation: CH3CH2CH(OH)CH3 + 4I2 + 6NaOH -> CH3CH2COONa + CHI3 + 5NaI + 5H2O [2]<br/>"
                    "(or ionic: CH3CH2CH(OH)CH3 + 4I2 + 6OH- -> CH3CH2COO- + CHI3 + 5I- + 5H2O)."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="One of the four isomers exhibits optical isomerism (enantiomerism). Identify this isomer, state the feature responsible, and draw 3D wedge-and-dash representations of the two enantiomers.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Isomer: Butan-2-ol (FA 2) [1].<br/>"
                    "Feature: Possesses a chiral centre (asymmetric carbon atom, C2) bonded to four different groups: -H, -OH, -CH3, and -C2H5 [1].<br/>"
                    "Drawing: Two non-superimposable tetrahedral mirror-image 3D wedge-dash representations correctly showing the four groups around the central chiral carbon [1]."
                )
            )
        ]
    )

    p3_q2 = PracticalQuestion(
        number=2,
        title="Deductive Identification of an Unknown Bifunctional Organic Acid (FA 5)",
        syllabus_ref="9701/32/M/J/22/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Synoptic Analytical Investigation:</b><br/>"
            "An unknown liquid compound, <b>FA 5</b>, contains carbon, hydrogen, and oxygen only.<br/>"
            "Elemental analysis reveals that FA 5 contains 55.8% C, 7.0% H, and 37.2% O by mass.<br/><br/>"
            "<b>Experimental Observations on FA 5:</b><br/>"
            "• <b>Observation 1:</b> When 1 cm<sup>3</sup> of bromine water, Br<sub>2</sub>(aq), is added to 5 drops of FA 5, the orange color decolourizes immediately without requiring any catalyst.<br/>"
            "• <b>Observation 2:</b> When solid sodium hydrogencarbonate, NaHCO<sub>3</sub>, is added to FA 5, rapid effervescence is observed and the evolved gas turns limewater milky.<br/>"
            "• <b>Observation 3:</b> A 1.720 g sample of FA 5 was dissolved in distilled water and made up to 250.0 cm<sup>3</sup> in a volumetric flask. Titration of 25.0 cm<sup>3</sup> portions of this solution required 20.00 cm<sup>3</sup> of 0.100 mol dm<sup>-3</sup> NaOH for complete neutralization using phenolphthalein indicator.<br/>"
            "• <b>Observation 4:</b> FA 5 displays stereoisomerism and exists as a pair of geometric isomers."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Calculate the empirical formula of FA 5 from its elemental percentage composition. [Ar: C = 12.0, H = 1.0, O = 16.0]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Moles of C = 55.8 / 12.0 = 4.65 mol [1].<br/>"
                    "Moles of H = 7.0 / 1.0 = 7.00 mol; Moles of O = 37.2 / 16.0 = 2.325 mol [1].<br/>"
                    "Divide by smallest (2.325): C = 2.0, H = 3.01, O = 1.0. Empirical formula = C2H3O [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Using the titration data, calculate the relative molecular mass, Mr, of FA 5 (assuming it is a monoprotic acid), and determine its molecular formula.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "Moles of NaOH in titre = 0.100 x (20.00 / 1000) = 2.00 x 10^-3 mol [1].<br/>"
                    "Moles of acid in 25.0 cm<sup>3</sup> = 2.00 x 10^-3 mol; in 250.0 cm<sup>3</sup> = 2.00 x 10^-2 mol [1].<br/>"
                    "Mr of FA 5 = mass / moles = 1.720 g / 0.0200 mol = 86.0 g mol^-1 [1].<br/>"
                    "Empirical formula mass of C2H3O = 2(12.0) + 3(1.0) + 16.0 = 43.0. Multiple = 86.0 / 43.0 = 2. Molecular formula = C4H6O2 [1]."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="State the two functional groups present in FA 5 based on Observations 1 and 2.",
                marks=2,
                lines_count=3,
                mark_scheme="Observation 1 (bromine water decolourized): Alkene / Carbon-carbon double bond (C=C) [1]; Observation 2 (effervescence with NaHCO3): Carboxylic acid group (-COOH) [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Deduce the structural formula of FA 5 and write its systematic IUPAC name.",
                marks=2,
                lines_count=3,
                mark_scheme="Structural formula: CH3-CH=CH-COOH [1]; Systematic name: But-2-enoic acid (or 2-butenoic acid) [1]."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Explain why FA 5 exhibits geometric (cis-trans / E-Z) stereoisomerism. Draw and clearly label the E and Z isomers of FA 5.",
                marks=5,
                lines_count=6,
                mark_scheme=(
                    "Condition 1: Restricted rotation about the carbon-carbon double bond (C=C) due to electron density in the pi bond preventing free rotation [1].<br/>"
                    "Condition 2: Both carbon atoms of the double bond have two different groups attached (one has -H and -CH3; the other has -H and -COOH) [1].<br/>"
                    "Z-isomer (cis): High-priority groups (-CH3 and -COOH) on the same side of the double bond [1.5].<br/>"
                    "E-isomer (trans): High-priority groups (-CH3 and -COOH) on opposite sides of the double bond [1.5]."
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Write the structural formula of the organic product formed when FA 5 reacts with bromine water, Br2(aq). State the type and mechanism of this reaction.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "Product formula: CH3-CH(Br)-CH(Br)-COOH (2,3-dibromobutanoic acid) [2].<br/>"
                    "Type of reaction: Addition [1].<br/>"
                    "Mechanism: Electrophilic addition (involving polarization of Br2 and formation of a cyclic bromonium or carbocation intermediate) [1]."
                )
            )
        ]
    )

    p3_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Synoptic_Unknown_Deductions.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, [p3_q1, p3_q2], include_qa_notes=False)

    print("=== Organic Chemistry Practical Suite Complete (3 Papers) ===")

if __name__ == "__main__":
    build_all_organic_practicals()
