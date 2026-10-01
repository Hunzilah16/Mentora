"""
Script to generate Inorganic Chemistry Past 10 Years Practical Papers (Paper 3)
Subfolder: Urwah_Chem_Papers/Inorganic Chemistry/Paper 3/Past 10 Years/

1. Topic 10: Group 2 & Gravimetric Thermal Decomposition (10 questions from past 4 years: 2021-2024)
2. Topic 11: Group 17 Halides & Precipitation Reactions (10 questions from past 4 years: 2021-2024)
3. Qualitative Analysis: Systematic Cations, Anions & Gases (10 questions from past 4 years: 2021-2024)
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_crucible_table,
    make_observation_table, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_inorganic_past10years():
    styles = get_practical_styles()
    dest_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Inorganic Chemistry\Paper 3\Past 10 Years"
    os.makedirs(dest_dir, exist_ok=True)

    # =========================================================================
    # 1. TOPIC 10: GROUP 2 & GRAVIMETRIC DECOMPOSITION (PAST 4 YEARS: 2021-2024)
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical: Topic 10 — Group 2 & Gravimetric Analysis",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p1_questions = [
        # Q1: Hydrated Magnesium Sulfate
        PracticalQuestion(
            number=1,
            title="Determination of Water of Crystallization in Hydrated Magnesium Sulfate to Constant Mass",
            syllabus_ref="9701/31/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> 3.25 g of MgSO4.xH2O is heated in a crucible with lid. "
                "The sample is heated gently for 3 minutes, strongly for 7 minutes, cooled in a desiccator, and weighed. "
                "Reheating yields constant residue mass = 1.59 g."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Complete the crucible weighing table below with recorded masses.", 3, lines_count=0, table_data=make_crucible_table(styles),
                    mark_scheme="Table formatted correctly with appropriate units (/ g) [1]; balance readings to 2 d.p. [1]; constant mass agreement within ±0.02 g [1]."),
                PracticalSubQuestion("(b)", "Calculate the mass of anhydrous MgSO4 remaining and the mass of water driven off.", 2, lines_count=2,
                    mark_scheme="Mass of MgSO4 = 1.59 g [1]; Mass of water = 3.25 - 1.59 = 1.66 g [1]."),
                PracticalSubQuestion("(c)", "Calculate moles of MgSO4 and H2O, and deduce the integer value of x. [Mr: MgSO4 = 120.4, H2O = 18.0]", 3, lines_count=3,
                    mark_scheme="Moles MgSO4 = 1.59 / 120.4 = 0.01321 mol [1]; Moles H2O = 1.66 / 18.0 = 0.09222 mol [1]; x = 0.09222 / 0.01321 = 6.98 ~ 7 (MgSO4·7H2O) [1]."),
                PracticalSubQuestion("(d)", "Explain the role of the desiccator in this experiment.", 2, lines_count=2,
                    mark_scheme="Allows the hot crucible to cool to room temperature in an environment free of moisture, preventing anhydrous MgSO4 from reabsorbing water vapor from air [2].")
            ]
        ),
        # Q2: Malachite Thermal Decomposition
        PracticalQuestion(
            number=2,
            title="Thermal Decomposition of Basic Copper(II) Carbonate (Malachite)",
            syllabus_ref="9701/33/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> CuCO<sub>3</sub>·Cu(OH)<sub>2</sub>(s) &rarr; 2CuO(s) + CO<sub>2</sub>(g) + H<sub>2</sub>O(g)<br/>"
                "<b>Method:</b> 4.42 g of green malachite powder is heated in a boiling tube connected to a limewater trap. "
                "The powder turns jet black and gas bubbles through the limewater. Final black residue mass = 3.18 g."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the theoretical percentage mass loss for pure CuCO3.Cu(OH)2. [Mr = 221.0, (CO2 + H2O) = 62.0]", 3, lines_count=3,
                    mark_scheme="Theoretical % loss = (62.0 / 221.0) x 100 = 28.05% [3]."),
                PracticalSubQuestion("(b)", "Calculate the experimental mass loss and the percentage purity of the malachite sample.", 3, lines_count=3,
                    mark_scheme="Experimental mass loss = 4.42 - 3.18 = 1.24 g [1]; % purity = (1.24 / (0.2805 x 4.42)) x 100 = 100% (or exact proportional purity calculation) [2]."),
                PracticalSubQuestion("(c)", "State the observation in the limewater and write an ionic equation for this reaction.", 2, lines_count=2,
                    mark_scheme="Limewater turns milky / forms white precipitate [1]; Ca2+(aq) + 2OH-(aq) + CO2(g) -> CaCO3(s) + H2O(l) [1]."),
                PracticalSubQuestion("(d)", "Explain why the delivery tube must be removed from limewater before removing the heat source.", 2, lines_count=2,
                    mark_scheme="To prevent cold limewater being sucked back into the hot tube as cooling gas contracts, which would shatter the hot glass tube [2].")
            ]
        ),
        # Q3: CaCO3 Gravimetric Decomposition
        PracticalQuestion(
            number=3,
            title="Gravimetric Analysis of Calcium Carbonate Thermal Decomposition",
            syllabus_ref="9701/34/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> CaCO<sub>3</sub>(s) &rarr; CaO(s) + CO<sub>2</sub>(g)<br/>"
                "<b>Data:</b> 2.50 g of limestone is strongly heated in a porcelain crucible until no further mass loss is observed. "
                "Residue mass = 1.51 g. [Mr: CaCO3 = 100.1, CaO = 56.1, CO2 = 44.0]"
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the mass of carbon dioxide lost during heating.", 2, lines_count=2,
                    mark_scheme="Mass of CO2 = 2.50 - 1.51 = 0.99 g [2]."),
                PracticalSubQuestion("(b)", "Calculate the moles of CO2 evolved and hence the mass of CaCO3 decomposed.", 3, lines_count=3,
                    mark_scheme="Moles CO2 = 0.99 / 44.0 = 0.0225 mol [1]; Moles CaCO3 = 0.0225 mol [1]; Mass CaCO3 = 0.0225 x 100.1 = 2.252 g [1]."),
                PracticalSubQuestion("(c)", "Calculate the percentage purity of the limestone sample.", 2, lines_count=2,
                    mark_scheme="% purity = (2.252 / 2.50) x 100 = 90.1% [2]."),
                PracticalSubQuestion("(d)", "Explain why a Bunsen burner flame alone cannot fully decompose barium carbonate, BaCO3.", 3, lines_count=3,
                    mark_scheme="Ba2+ has a larger ionic radius and lower charge density than Ca2+, causing significantly less polarization of the carbonate ion; hence BaCO3 has a much higher decomposition temperature exceeding standard Bunsen flame temperature [3].")
            ]
        ),
        # Q4: Group 2 Nitrates Decomposition
        PracticalQuestion(
            number=4,
            title="Comparative Thermal Decomposition of Group 2 Nitrates: Calcium Nitrate vs Barium Nitrate",
            syllabus_ref="9701/35/M/J/22/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Equation:</b> 2M(NO<sub>3</sub>)<sub>2</sub>(s) &rarr; 2MO(s) + 4NO<sub>2</sub>(g) + O<sub>2</sub>(g)<br/>"
                "Samples of Ca(NO3)2 and Ba(NO3)2 are heated in boiling tubes in a fume cupboard. "
                "Brown fumes are observed and a glowing splint is tested at the mouth of each tube."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the gas responsible for the brown fumes and the gas that relights a glowing splint.", 2, lines_count=2,
                    mark_scheme="Brown fumes: Nitrogen dioxide, NO2 [1]; Relights glowing splint: Oxygen, O2 [1]."),
                PracticalSubQuestion("(b)", "State which nitrate decomposes more readily (requires less heating) and explain why.", 4, lines_count=4,
                    mark_scheme="Calcium nitrate decomposes more readily [1]; Ca2+ is smaller than Ba2+ and has a higher charge density [1]; Ca2+ polarizes the nitrate anion more strongly [1], weakening the N-O covalent bond and lowering thermal stability [1]."),
                PracticalSubQuestion("(c)", "Write the balanced chemical equation for the thermal decomposition of calcium nitrate.", 2, lines_count=2,
                    mark_scheme="2Ca(NO3)2(s) -> 2CaO(s) + 4NO2(g) + O2(g) [2]."),
                PracticalSubQuestion("(d)", "State the hazard associated with NO2 gas and specify the required safety measure.", 2, lines_count=2,
                    mark_scheme="NO2 is toxic and corrosive to respiratory system [1]; must be carried out in a fume cupboard [1].")
            ]
        ),
        # Q5: Group 2 Hydroxide Solubility Trends
        PracticalQuestion(
            number=5,
            title="Qualitative Investigation of Solubility Trends in Group 2 Hydroxides",
            syllabus_ref="9701/32/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Aqueous solutions of Mg2+, Ca2+, and Ba2+ (0.1 mol dm^-3) are tested with 2.0 mol dm^-3 NaOH dropwise and in excess.<br/>"
                "• Mg2+: Thick white precipitate insoluble in excess.<br/>"
                "• Ca2+: Faint white precipitate formed.<br/>"
                "• Ba2+: Solution remains clear (no precipitate)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Deduce the trend in solubility of Group 2 hydroxides down the group from Mg to Ba.", 2, lines_count=2,
                    mark_scheme="Solubility of Group 2 hydroxides increases down the group from Mg(OH)2 (least soluble) to Ba(OH)2 (most soluble) [2]."),
                PracticalSubQuestion("(b)", "Explain this trend in terms of lattice energy and hydration enthalpy changes down Group 2.", 4, lines_count=4,
                    mark_scheme="Down the group, cation radius increases while OH- radius is small and fixed [1]; lattice energy decreases faster than the hydration enthalpy of the cation [2]; hence enthalpy of solution becomes more exothermic / less endothermic, increasing solubility [1]."),
                PracticalSubQuestion("(c)", "Write the ionic equation for the precipitation of magnesium hydroxide.", 2, lines_count=2,
                    mark_scheme="Mg2+(aq) + 2OH-(aq) -> Mg(OH)2(s) [2]."),
                PracticalSubQuestion("(d)", "State one common pharmaceutical use of a suspension of magnesium hydroxide.", 2, lines_count=2,
                    mark_scheme="Used as an antacid (Milk of Magnesia) to neutralize excess stomach hydrochloric acid without causing caustic burns [2].")
            ]
        ),
        # Q6: Group 2 Sulfate Solubility Trends
        PracticalQuestion(
            number=6,
            title="Qualitative Investigation of Solubility Trends in Group 2 Sulfates",
            syllabus_ref="9701/33/O/N/21/Q3",
            total_marks=10,
            procedure_intro=(
                "Aqueous solutions of Mg2+, Ca2+, and Ba2+ are tested with dilute sulfuric acid, H2SO4(aq).<br/>"
                "• Mg2+: No precipitate (clear solution).<br/>"
                "• Ca2+: Faint/slight white precipitate.<br/>"
                "• Ba2+: Dense, heavy white precipitate immediately formed."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Deduce the trend in solubility of Group 2 sulfates down the group.", 2, lines_count=2,
                    mark_scheme="Solubility of Group 2 sulfates decreases down the group from MgSO4 (soluble) to BaSO4 (insoluble) [2]."),
                PracticalSubQuestion("(b)", "Explain why sulfate solubility decreases down the group whereas hydroxide solubility increases.", 4, lines_count=4,
                    mark_scheme="Sulfate ion (SO4^2-) is very large compared to OH- [1]; down the group, lattice energy changes very little because anion size dominates [1]; however, hydration enthalpy of the cation decreases significantly as cation radius increases [1]; hence delta-H_solution becomes increasingly endothermic, decreasing solubility [1]."),
                PracticalSubQuestion("(c)", "Write the ionic equation for the precipitation of barium sulfate.", 2, lines_count=2,
                    mark_scheme="Ba2+(aq) + SO4^2-(aq) -> BaSO4(s) [2]."),
                PracticalSubQuestion("(d)", "Explain why barium sulfate can be safely swallowed by patients undergoing X-ray imaging despite Ba2+ being highly toxic.", 2, lines_count=2,
                    mark_scheme="BaSO4 has an extremely low solubility product (virtually insoluble in water and stomach acid), so negligible free toxic Ba2+ ions enter the bloodstream [2].")
            ]
        ),
        # Q7: Crucible Lid Orientation
        PracticalQuestion(
            number=7,
            title="Analysis of Experimental Technique: Crucible Lid Positioning in Thermal Analysis",
            syllabus_ref="9701/31/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "In thermal gravimetric analysis, instructions specify:<br/>"
                "1. Heat with the crucible lid partially ajar.<br/>"
                "2. Cool with the crucible lid completely closed in a desiccator."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain the consequence if the lid is left completely closed during strong heating.", 3, lines_count=3,
                    mark_scheme="Water vapor / steam cannot escape freely, building up pressure which can blow off the lid or condense on the underside and drip back into the salt residue [3]."),
                PracticalSubQuestion("(b)", "Explain the consequence if the crucible has no lid at all during heating.", 3, lines_count=3,
                    mark_scheme="Rapid boiling and thermal turbulence can cause solid salt crystals to 'spit' out of the crucible, resulting in an erroneously high recorded mass loss [3]."),
                PracticalSubQuestion("(c)", "Explain why the lid must be placed tightly shut during the cooling phase.", 2, lines_count=2,
                    mark_scheme="Prevents the anhydrous hygroscopic residue from absorbing moisture from the air while cooling [2]."),
                PracticalSubQuestion("(d)", "State why tongs must always be used rather than fingers when moving crucibles.", 2, lines_count=2,
                    mark_scheme="Avoids severe burns from hot porcelain and prevents oils, sweat, and moisture from fingertips transferring onto the crucible and altering measured mass [2].")
            ]
        ),
        # Q8: Spitting Prevention in Gravimetry
        PracticalQuestion(
            number=8,
            title="Mitigation of Mechanical Spitting and Thermal Shock in Gravimetric Preparations",
            syllabus_ref="9701/35/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "When hydrated crystals are placed directly over a roaring Bunsen flame, violent cracking sounds and spitting of solid particles occur. "
                "A student records an apparent formula of MgSO4.9H2O instead of MgSO4.7H2O."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain how solid spitting leads to an erroneously high calculated value for x.", 3, lines_count=3,
                    mark_scheme="Lost solid crystals reduce the final mass of residue [1]; the calculated mass loss is assumed to be water vapor only [1]; this overestimates moles of water relative to residue, yielding x > 7 [1]."),
                PracticalSubQuestion("(b)", "Describe the proper heating sequence that prevents mechanical spitting of crystals.", 3, lines_count=3,
                    mark_scheme="Begin by heating gently with a low, waving yellow/blue flame for 2-3 minutes to allow water to vaporize smoothly [1.5]; only after sputtering ceases, heat strongly with a roaring non-luminous flame [1.5]."),
                PracticalSubQuestion("(c)", "Explain why placing a hot crucible directly onto a cold stone bench can cause thermal shock.", 2, lines_count=2,
                    mark_scheme="Rapid, uneven thermal contraction of the porcelain causes internal mechanical stress that cracks the crucible [2]."),
                PracticalSubQuestion("(d)", "Identify the proper heat-resistant support used to hold a crucible on a tripod.", 2, lines_count=2,
                    mark_scheme="Pipe-clay triangle (or silica triangle) [2].")
            ]
        ),
        # Q9: Chemical Confirmation of Copper(II) in Residue
        PracticalQuestion(
            number=9,
            title="Chemical Confirmation of Transition Metal Oxidation State in Decomposition Residue",
            syllabus_ref="9701/34/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "Following the thermal decomposition of basic copper carbonate, a black residue remains in the tube. "
                "A student must prove chemically that the black powder is copper(II) oxide, CuO."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Name the acid used to dissolve the black residue and state the observation.", 2, lines_count=2,
                    mark_scheme="Dilute sulfuric acid, H2SO4 [1]; the black solid dissolves to form a clear sky-blue solution of CuSO4(aq) [1]."),
                PracticalSubQuestion("(b)", "Describe the two-step test using aqueous ammonia to confirm copper(II) ions in the blue solution.", 4, lines_count=4,
                    mark_scheme="Step 1: Add dilute NH3 dropwise: a pale blue precipitate of Cu(OH)2 forms [2]; Step 2: Add excess NH3: the precipitate dissolves to give an intense deep royal blue solution of [Cu(NH3)4(H2O)2]2+ [2]."),
                PracticalSubQuestion("(c)", "Write the ionic formula of the complex ion responsible for the deep royal blue color.", 2, lines_count=2,
                    mark_scheme="[Cu(NH3)4(H2O)2]2+ (or [Cu(NH3)4]2+) [2]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for the reaction of CuO with sulfuric acid.", 2, lines_count=2,
                    mark_scheme="CuO(s) + H2SO4(aq) -> CuSO4(aq) + H2O(l) [2].")
            ]
        ),
        # Q10: Limewater Suck-Back Physics
        PracticalQuestion(
            number=10,
            title="Physical Principles of Suck-Back Prevention and Laboratory Safety in Gas Evolution",
            syllabus_ref="9701/32/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "When heating solids in a boiling tube with an attached delivery tube submerged in limewater, "
                "extinguishing the flame before removing the delivery tube causes liquid to rush up the tube."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain the physical mechanism that drives suck-back when the flame is removed.", 4, lines_count=4,
                    mark_scheme="When heating stops, the air and gas inside the boiling tube cool rapidly [1]; the volume of the gas contracts and pressure inside the tube drops below atmospheric pressure [2]; atmospheric pressure forces the cold limewater solution up the delivery tube into the hot boiling tube [1]."),
                PracticalSubQuestion("(b)", "Explain why suck-back of cold liquid into a hot glass tube is dangerous.", 2, lines_count=2,
                    mark_scheme="The extreme temperature differential between cold liquid and hot borosilicate glass causes sudden uneven contraction (thermal shock), shattering the tube and spraying hot chemicals [2]."),
                PracticalSubQuestion("(c)", "State two methods to prevent suck-back during an experiment.", 2, lines_count=2,
                    mark_scheme="1. Lift the delivery tube out of the liquid before removing the Bunsen flame [1]; 2. Use a Bunsen valve or safety trap bottle between the reaction vessel and collection liquid [1]."),
                PracticalSubQuestion("(d)", "State the correct angle for clamping a boiling tube during strong heating of solids.", 2, lines_count=2,
                    mark_scheme="Clamped near the mouth at a 45-degree angle pointing away from all personnel [2].")
            ]
        )
    ]

    p1_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Topic10_Group2_Gravimetric.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, p1_questions, include_qa_notes=False)

    # =========================================================================
    # 2. TOPIC 11: GROUP 17 HALIDES (PAST 4 YEARS: 2021-2024 — 10 MASTER QUESTIONS)
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical: Topic 11 — Group 17 Halides & Precipitation Reactions",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p2_questions = [
        # Q1: Halide Precipitation
        PracticalQuestion(
            number=1,
            title="Diagnostic Precipitation of Aqueous Halide Ions with Silver Nitrate",
            syllabus_ref="9701/31/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Three unlabelled solutions, FA 1, FA 2, and FA 3, contain chloride, bromide, and iodide ions.<br/>"
                "Aqueous silver nitrate is added to each solution after acidification with dilute nitric acid."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Complete the table describing the precipitate color formed with each halide ion.", 3, lines_count=0, table_data=Table([
                    [Paragraph("<b>Halide Ion</b>", styles['table_header']), Paragraph("<b>Formula of Precipitate</b>", styles['table_header']), Paragraph("<b>Precipitate Color</b>", styles['table_header'])],
                    [Paragraph("Chloride, Cl-", styles['table_cell']), Paragraph("AgCl", styles['table_cell_center']), Paragraph("White", styles['table_cell_center'])],
                    [Paragraph("Bromide, Br-", styles['table_cell']), Paragraph("AgBr", styles['table_cell_center']), Paragraph("Cream", styles['table_cell_center'])],
                    [Paragraph("Iodide, I-", styles['table_cell']), Paragraph("AgI", styles['table_cell_center']), Paragraph("Yellow", styles['table_cell_center'])]
                ], colWidths=[150, 170, 170], style=[
                    ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
                    ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
                    ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ]),
                    mark_scheme="AgCl = White [1]; AgBr = Cream [1]; AgI = Yellow [1]."),
                PracticalSubQuestion("(b)", "Write the ionic equation with state symbols for the precipitation of silver iodide.", 2, lines_count=2,
                    mark_scheme="Ag+(aq) + I-(aq) -> AgI(s) [2]."),
                PracticalSubQuestion("(c)", "Explain why dilute nitric acid is added prior to silver nitrate.", 3, lines_count=3,
                    mark_scheme="To decompose any carbonate (CO3^2-) or sulfite (SO3^2-) ions [1.5], preventing the formation of insoluble Ag2CO3 or Ag2SO3 which would give a false positive precipitate [1.5]."),
                PracticalSubQuestion("(d)", "Explain why dilute hydrochloric acid CANNOT be used to acidify the solution.", 2, lines_count=2,
                    mark_scheme="HCl contains Cl- ions which would immediately precipitate white AgCl with silver nitrate, invalidating the test [2].")
            ]
        ),
        # Q2: Ammonia Solubility
        PracticalQuestion(
            number=2,
            title="Differential Solubility of Silver Halide Precipitates in Aqueous Ammonia",
            syllabus_ref="9701/33/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Silver halide precipitates are often difficult to distinguish by visual inspection of color alone. "
                "Addition of dilute vs concentrated aqueous ammonia provides unambiguous confirmation."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the solubility behavior of AgCl, AgBr, and AgI in dilute aqueous ammonia.", 3, lines_count=3,
                    mark_scheme="AgCl: Dissolves completely to form a colorless solution [1]; AgBr: Insoluble / does not dissolve in dilute NH3 [1]; AgI: Insoluble in dilute NH3 [1]."),
                PracticalSubQuestion("(b)", "State the solubility behavior of AgBr and AgI in concentrated aqueous ammonia.", 2, lines_count=2,
                    mark_scheme="AgBr: Dissolves completely in concentrated NH3 [1]; AgI: Remains insoluble in concentrated NH3 [1]."),
                PracticalSubQuestion("(c)", "Explain why AgCl dissolves in dilute NH3 while AgI is insoluble even in concentrated NH3.", 3, lines_count=3,
                    mark_scheme="AgCl has a higher solubility product (Ksp) than AgI [1]; complexing of Ag+ with NH3 lowers [Ag+] enough to exceed the Ksp threshold for AgCl [1]; for AgI, Ksp is so extremely small that even with concentrated NH3 [Ag+][I-] remains greater than Ksp [1]."),
                PracticalSubQuestion("(d)", "Write the formula of the complex ion formed when AgCl dissolves in ammonia.", 2, lines_count=2,
                    mark_scheme="[Ag(NH3)2]+ (diamminesilver(I) ion) [2].")
            ]
        ),
        # Q3: Halogen Displacement & Cyclohexane
        PracticalQuestion(
            number=3,
            title="Halogen Displacement Reactions and Non-Polar Extraction into Cyclohexane",
            syllabus_ref="9701/32/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Aqueous chlorine water is added to separate solutions of NaBr(aq) and NaI(aq). "
                "Cyclohexane (density = 0.78 g cm^-3) is added, and the test-tubes are stoppered and shaken vigorously."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the color observed in the upper organic (cyclohexane) layer for the NaBr test.", 2, lines_count=2,
                    mark_scheme="Orange / reddish-brown (due to dissolved non-polar bromine, Br2) [2]."),
                PracticalSubQuestion("(b)", "State the color observed in the upper organic layer for the NaI test.", 2, lines_count=2,
                    mark_scheme="Bright violet / purple (due to dissolved non-polar iodine, I2) [2]."),
                PracticalSubQuestion("(c)", "Explain why halogens dissolve preferentially in cyclohexane rather than water.", 3, lines_count=3,
                    mark_scheme="Halogen molecules (Br2, I2) are non-polar [1]; they form favorable London dispersion forces with non-polar cyclohexane molecules [1], whereas they cannot form hydrogen bonds with polar water molecules [1]."),
                PracticalSubQuestion("(d)", "Write the ionic equation for the displacement of iodide ions by chlorine.", 3, lines_count=3,
                    mark_scheme="Cl2(aq) + 2I-(aq) -> 2Cl-(aq) + I2(aq) [3] (1 mark for species, 1 mark for balancing, 1 mark for state symbols).")
            ]
        ),
        # Q4: Solid Halides + Conc H2SO4 (NaCl vs NaBr)
        PracticalQuestion(
            number=4,
            title="Reactions of Solid Sodium Chloride and Sodium Bromide with Concentrated Sulfuric Acid",
            syllabus_ref="9701/34/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Solid samples of NaCl and NaBr are placed in dry boiling tubes in a fume cupboard. "
                "Concentrated sulfuric acid is added dropwise to each tube."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the observations when concentrated H2SO4 is added to solid NaCl.", 2, lines_count=2,
                    mark_scheme="Steamy / misty acidic fumes of HCl gas [1]; effervescence / solid dissolves [1]."),
                PracticalSubQuestion("(b)", "State the observations when concentrated H2SO4 is added to solid NaBr.", 3, lines_count=3,
                    mark_scheme="Steamy fumes of HBr [1]; reddish-brown / orange vapor of Br2 gas [1]; choking pungent gas (SO2) evolved [1]."),
                PracticalSubQuestion("(c)", "Identify the type of reaction occurring with NaCl and explain why no redox occurs.", 2, lines_count=2,
                    mark_scheme="Acid-base (proton transfer) reaction [1]; chloride (Cl-) is too weak a reducing agent to reduce concentrated H2SO4 [1]."),
                PracticalSubQuestion("(d)", "Write the balanced redox equation for the oxidation of bromide ions by concentrated sulfuric acid.", 3, lines_count=3,
                    mark_scheme="2H+ + H2SO4 + 2Br- -> Br2 + SO2 + 2H2O (or 2NaBr + 2H2SO4 -> Na2SO4 + Br2 + SO2 + 2H2O) [3].")
            ]
        ),
        # Q5: Solid NaI + Conc H2SO4
        PracticalQuestion(
            number=5,
            title="Reactions of Solid Sodium Iodide with Concentrated Sulfuric Acid: Deep Reduction",
            syllabus_ref="9701/31/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "When concentrated sulfuric acid is added to solid sodium iodide, an exothermic reaction occurs. "
                "Multiple products are detected, including purple vapors, a dark solid, a yellow deposit, and an offensive odor."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the chemicals responsible for: (i) purple vapor, (ii) yellow solid, (iii) bad egg smell.", 3, lines_count=3,
                    mark_scheme="(i) Purple vapor: Iodine (I2) [1]; (ii) Yellow solid: Sulfur (S) [1]; (iii) Bad egg smell: Hydrogen sulfide (H2S) [1]."),
                PracticalSubQuestion("(b)", "State the changes in oxidation number of sulfur in H2SO4 when it is reduced to: (i) SO2, (ii) S, (iii) H2S.", 3, lines_count=3,
                    mark_scheme="In H2SO4, S is +6; (i) In SO2: +4 (reduction of 2) [1]; (ii) In S: 0 (reduction of 6) [1]; (iii) In H2S: -2 (reduction of 8) [1]."),
                PracticalSubQuestion("(c)", "Write the half-equation for the reduction of H2SO4 to H2S.", 2, lines_count=2,
                    mark_scheme="H2SO4 + 8H+ + 8e- -> H2S + 4H2O (or SO4^2- + 10H+ + 8e- -> H2S + 4H2O) [2]."),
                PracticalSubQuestion("(d)", "Write the overall balanced equation for the reaction producing H2S and I2.", 2, lines_count=2,
                    mark_scheme="8NaI + 5H2SO4 -> 4Na2SO4 + 4I2 + H2S + 4H2O (or 8I- + H2SO4 + 8H+ -> 4I2 + H2S + 4H2O) [2].")
            ]
        ),
        # Q6: Reducing Trend down Group 17
        PracticalQuestion(
            number=6,
            title="Theoretical Justification of Reducing Ability Trends of Halide Ions Down Group 17",
            syllabus_ref="9701/35/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "The experimental reactions with concentrated sulfuric acid demonstrate that the reducing strength of halide ions increases: Cl<sup>-</sup> &lt; Br<sup>-</sup> &lt; I<sup>-</sup>."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Define 'reducing agent' in terms of electron transfer.", 2, lines_count=2,
                    mark_scheme="An electron donor / species that loses electrons to reduce another substance [2]."),
                PracticalSubQuestion("(b)", "Explain in terms of atomic structure why iodide is a much stronger reducing agent than chloride.", 4, lines_count=4,
                    mark_scheme="Down Group 17, ionic radius increases significantly (I- > Br- > Cl-) [1]; valence electrons are in higher energy levels with greater distance from nucleus [1]; increased shielding by inner electron shells weakens electrostatic attraction between nucleus and outer electrons [1]; outer electrons are lost much more readily [1]."),
                PracticalSubQuestion("(c)", "Predict whether fluoride, F-, would react with concentrated H2SO4 in a redox reaction. Justify.", 2, lines_count=2,
                    mark_scheme="No redox reaction occurs [1]; fluoride is an even weaker reducing agent than chloride due to very small ionic radius and extremely tight electron hold [1]."),
                PracticalSubQuestion("(d)", "State the formula of the dangerous gas produced when NaF reacts with conc H2SO4.", 2, lines_count=2,
                    mark_scheme="Hydrogen fluoride, HF (highly corrosive gas that etches glass) [2].")
            ]
        ),
        # Q7: Pre-Acidification with HNO3
        PracticalQuestion(
            number=7,
            title="Analytical Methodology: Rationale for Nitric Acid Addition in Halide Analysis",
            syllabus_ref="9701/32/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "A student tests an unknown solution X by adding silver nitrate directly without adding dilute nitric acid first. "
                "A pale yellow-white precipitate forms. The student concludes that solution X contains bromide ions. "
                "In reality, solution X contains sodium carbonate, Na2CO3."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the precipitate formed when AgNO3 is added to aqueous Na2CO3.", 2, lines_count=2,
                    mark_scheme="Silver carbonate, Ag2CO3 (pale yellow / off-white precipitate) [2]."),
                PracticalSubQuestion("(b)", "Explain how adding dilute HNO3 prevents this false positive conclusion.", 3, lines_count=3,
                    mark_scheme="Nitric acid reacts with carbonate ions to form soluble nitrate, CO2 gas, and water: 2H+ + CO3^2- -> H2O + CO2 [2]; this completely eliminates carbonate ions before silver ions are introduced [1]."),
                PracticalSubQuestion("(c)", "Explain why sulfuric acid, H2SO4, cannot be used to acidify before AgNO3.", 3, lines_count=3,
                    mark_scheme="Sulfuric acid contains sulfate ions (SO4^2-) [1]; silver sulfate (Ag2SO4) is sparingly soluble and can precipitate as a white solid [1], which would interfere with the halide test [1]."),
                PracticalSubQuestion("(d)", "Write the balanced ionic equation for the reaction of Ag2CO3 with nitric acid.", 2, lines_count=2,
                    mark_scheme="Ag2CO3(s) + 2H+(aq) -> 2Ag+(aq) + CO2(g) + H2O(l) [2].")
            ]
        ),
        # Q8: Diamminesilver(I) Complex Equation
        PracticalQuestion(
            number=8,
            title="Coordination Chemistry: Dissolution of Silver Chloride in Aqueous Ammonia",
            syllabus_ref="9701/33/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "When excess dilute aqueous ammonia is added to a test-tube containing a precipitate of silver chloride, "
                "the cloudy suspension dissolves completely to form a transparent colorless solution."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Write the balanced chemical equation for the dissolution of AgCl in aqueous ammonia.", 3, lines_count=3,
                    mark_scheme="AgCl(s) + 2NH3(aq) -> [Ag(NH3)2]+(aq) + Cl-(aq) [3] (or AgCl + 2NH3 -> [Ag(NH3)2]Cl)."),
                PracticalSubQuestion("(b)", "State the coordination number and the shape of the [Ag(NH3)2]+ complex ion.", 2, lines_count=2,
                    mark_scheme="Coordination number: 2 [1]; Shape: Linear (180° bond angle) [1]."),
                PracticalSubQuestion("(c)", "Identify the type of bond between the silver ion and the nitrogen atom of ammonia.", 2, lines_count=2,
                    mark_scheme="Dative covalent (coordinate) bond [2]."),
                PracticalSubQuestion("(d)", "Describe what happens when dilute nitric acid is added to the resulting clear solution.", 3, lines_count=3,
                    mark_scheme="Dilute HNO3 neutralizes the NH3 ligands to form NH4+ [1.5]; the diamminesilver complex is destroyed and white AgCl precipitates again [1.5].")
            ]
        ),
        # Q9: Chloride vs Chlorate(I)
        PracticalQuestion(
            number=9,
            title="Discrimination Between Chloride (Cl-) and Chlorate(I) (ClO-) in Commercial Bleach",
            syllabus_ref="9701/34/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Household bleach contains both sodium chlorate(I), NaClO, and sodium chloride, NaCl.<br/>"
                "A student must design tests to distinguish between Cl- and ClO- ions in the solution."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the oxidation state of chlorine in: (i) Cl-, (ii) ClO-.", 2, lines_count=2,
                    mark_scheme="(i) In Cl-: -1 [1]; (ii) In ClO-: +1 [1]."),
                PracticalSubQuestion("(b)", "Describe a chemical test that demonstrates the bleaching (oxidizing) action of ClO-.", 3, lines_count=3,
                    mark_scheme="Add blue litmus paper: the litmus turns red momentarily due to acidity and then is rapidly bleached completely white [3]."),
                PracticalSubQuestion("(c)", "When dilute sulfuric acid is added to bleach, chlorine gas is evolved. Write the ionic equation.", 3, lines_count=3,
                    mark_scheme="ClO-(aq) + Cl-(aq) + 2H+(aq) -> Cl2(g) + H2O(l) [3]."),
                PracticalSubQuestion("(d)", "Identify the type of redox reaction described in (c).", 2, lines_count=2,
                    mark_scheme="Comproportionation (synproportionation) [2].")
            ]
        ),
        # Q10: Photochemical Decomposition of AgX
        PracticalQuestion(
            number=10,
            title="Photochemical Decomposition of Silver Halides and Storage in Amber Glassware",
            syllabus_ref="9701/35/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "When freshly precipitated white AgCl is left on a watch-glass exposed to bright laboratory light, "
                "it gradually darkens through lavender to grey-violet and finally dark grey/black."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Write the balanced chemical equation for the photochemical decomposition of silver chloride.", 3, lines_count=3,
                    mark_scheme="2AgCl(s) -> 2Ag(s) + Cl2(g) [3] (under UV / visible light)."),
                PracticalSubQuestion("(b)", "Identify the grey-black substance formed on the surface of the precipitate.", 2, lines_count=2,
                    mark_scheme="Finely divided metallic silver, Ag(s) [2]."),
                PracticalSubQuestion("(c)", "Explain why aqueous silver nitrate must be stored in dark brown (amber) glass bottles.", 2, lines_count=2,
                    mark_scheme="Amber glass filters out UV and high-energy visible light, preventing photochemical reduction of Ag+ to Ag metal during storage [2]."),
                PracticalSubQuestion("(d)", "State the historical industrial application of this photochemical property.", 3, lines_count=3,
                    mark_scheme="Traditional black-and-white photographic film and photographic paper development [3].")
            ]
        )
    ]

    p2_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Topic11_Halides_Precipitation.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, p2_questions, include_qa_notes=False)

    # =========================================================================
    # 3. QUALITATIVE ANALYSIS: CATIONS, ANIONS & GASES (PAST 4 YEARS: 2021-2024)
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical: Systematic Qualitative Analysis — Cations, Anions & Gases",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p3_questions = [
        # Q1: Amphoteric Cations
        PracticalQuestion(
            number=1,
            title="Systematic Differentiation of Amphoteric Metal Ions: Al3+, Zn2+, and Mg2+",
            syllabus_ref="9701/31/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Three solutions, FA 1, FA 2, and FA 3, contain Al3+, Zn2+, and Mg2+.<br/>"
                "Test 1: Add NaOH(aq) dropwise, then in excess.<br/>"
                "Test 2: Add NH3(aq) dropwise, then in excess."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Complete the observation table below.", 4, lines_count=0, table_data=make_observation_table(styles, [
                    ("<b>Al3+:</b><br/>(i) NaOH dropwise & excess<br/>(ii) NH3 dropwise & excess", "", ""),
                    ("<b>Zn2+:</b><br/>(i) NaOH dropwise & excess<br/>(ii) NH3 dropwise & excess", "", ""),
                    ("<b>Mg2+:</b><br/>(i) NaOH dropwise & excess<br/>(ii) NH3 dropwise & excess", "", "")
                ]),
                    mark_scheme="Al3+: White ppt soluble in excess NaOH, insoluble in excess NH3 [1.5]; Zn2+: White ppt soluble in excess of both NaOH and NH3 [1.5]; Mg2+: White ppt insoluble in excess of both [1]."),
                PracticalSubQuestion("(b)", "Write the formula of the complex ion formed when zinc hydroxide dissolves in excess ammonia.", 2, lines_count=2,
                    mark_scheme="[Zn(NH3)4]2+ (tetraamminezinc(II) ion) [2]."),
                PracticalSubQuestion("(c)", "Write the balanced ionic equation for the reaction of aluminium hydroxide with excess hydroxide ions.", 2, lines_count=2,
                    mark_scheme="Al(OH)3(s) + OH-(aq) -> [Al(OH)4]-(aq) [2]."),
                PracticalSubQuestion("(d)", "Explain why magnesium hydroxide does not dissolve in excess sodium hydroxide.", 2, lines_count=2,
                    mark_scheme="Mg(OH)2 is a purely basic hydroxide with strong ionic character; it lacks amphoteric character and cannot accept further OH- ions [2].")
            ]
        ),
        # Q2: Transition Metal Precipitation (Cu2+)
        PracticalQuestion(
            number=2,
            title="Precipitation and Complex Ion Ligand Substitution of Copper(II) Ions",
            syllabus_ref="9701/35/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "Copper(II) sulfate solution is subjected to tests with aqueous sodium hydroxide, aqueous ammonia, and potassium iodide."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the observations when aqueous NaOH is added dropwise and then in excess to Cu2+(aq).", 2, lines_count=2,
                    mark_scheme="Pale blue precipitate forms [1]; precipitate is insoluble in excess NaOH [1]."),
                PracticalSubQuestion("(b)", "State the observations when aqueous NH3 is added dropwise and then in excess to Cu2+(aq).", 3, lines_count=3,
                    mark_scheme="Pale blue precipitate forms with dropwise NH3 [1]; dissolves in excess NH3 to give an intense deep royal blue solution [2]."),
                PracticalSubQuestion("(c)", "State the formula and geometry of the deep royal blue complex ion.", 2, lines_count=2,
                    mark_scheme="Formula: [Cu(NH3)4(H2O)2]2+ [1]; Geometry: Octahedral (distorted octahedral) [1]."),
                PracticalSubQuestion("(d)", "State the observations when aqueous potassium iodide, KI, is added to aqueous copper(II) sulfate.", 3, lines_count=3,
                    mark_scheme="White / off-white precipitate of copper(I) iodide (CuI) [1.5]; in a dark brown solution of iodine (I2) [1.5].")
            ]
        ),
        # Q3: Aerial Oxidation of Fe2+
        PracticalQuestion(
            number=3,
            title="Redox Precipitation and Aerial Oxidation of Iron(II) Hydroxide",
            syllabus_ref="9701/32/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "A fresh green solution of iron(II) sulfate is treated with aqueous sodium hydroxide. "
                "The test-tube is left open to the atmosphere for 10 minutes."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the initial observation upon adding aqueous NaOH to Fe2+(aq).", 2, lines_count=2,
                    mark_scheme="Dirty green / dark green precipitate of Fe(OH)2 formed [2]."),
                PracticalSubQuestion("(b)", "Describe the change in appearance of the precipitate after standing exposed to air.", 2, lines_count=2,
                    mark_scheme="The surface of the green precipitate turns reddish-brown [2]."),
                PracticalSubQuestion("(c)", "Explain this color change chemically and identify the species responsible.", 3, lines_count=3,
                    mark_scheme="Fe(OH)2 is oxidized by atmospheric dissolved oxygen to iron(III) hydroxide, Fe(OH)3 (red-brown) [2]; iron is oxidized from +2 to +3 [1]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for this aerial oxidation.", 3, lines_count=3,
                    mark_scheme="4Fe(OH)2(s) + O2(g) + 2H2O(l) -> 4Fe(OH)3(s) [3].")
            ]
        ),
        # Q4: Cr3+ Alkaline Oxidation
        PracticalQuestion(
            number=4,
            title="Alkaline Oxidation of Chromium(III) Ions by Hydrogen Peroxide",
            syllabus_ref="9701/34/M/J/23/Q3",
            total_marks=10,
            procedure_intro=(
                "A grey-green solution containing Cr3+ is treated with excess aqueous NaOH to form a dark green solution. "
                "Aqueous hydrogen peroxide, H2O2, is added and the mixture is warmed gently."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the formula of the chromium species in the dark green solution before adding H2O2.", 2, lines_count=2,
                    mark_scheme="[Cr(OH)6]3- or [Cr(OH)4]- (tetrahydroxochromate(III)) [2]."),
                PracticalSubQuestion("(b)", "State the observation when the mixture is warmed with hydrogen peroxide.", 2, lines_count=2,
                    mark_scheme="Effervescence (O2 gas) and the solution turns bright yellow [2]."),
                PracticalSubQuestion("(c)", "Identify the yellow species formed and state the oxidation state of chromium in it.", 3, lines_count=3,
                    mark_scheme="Chromate(VI) ion, CrO4^2- [2]; Oxidation state of Cr = +6 [1]."),
                PracticalSubQuestion("(d)", "Write the balanced redox equation for the oxidation of [Cr(OH)4]- by H2O2 in alkaline conditions.", 3, lines_count=3,
                    mark_scheme="2[Cr(OH)4]-(aq) + 3H2O2(aq) + 2OH-(aq) -> 2CrO4^2-(aq) + 8H2O(l) [3].")
            ]
        ),
        # Q5: Sulfate vs Sulfite Discrimination
        PracticalQuestion(
            number=5,
            title="Chemical Discrimination of Sulfate (SO4^2-) and Sulfite (SO3^2-) Ions",
            syllabus_ref="9701/31/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "Solution A contains sodium sulfate, Na2SO4. Solution B contains sodium sulfite, Na2SO3.<br/>"
                "Both solutions are tested with aqueous barium chloride, BaCl2, followed by dilute hydrochloric acid."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the observations when BaCl2 is added to Solution A, followed by dilute HCl.", 3, lines_count=3,
                    mark_scheme="Dense white precipitate forms with BaCl2 [1.5]; precipitate remains completely insoluble upon adding dilute HCl [1.5]."),
                PracticalSubQuestion("(b)", "State the observations when BaCl2 is added to Solution B, followed by dilute HCl and warming.", 4, lines_count=4,
                    mark_scheme="White precipitate forms with BaCl2 [1]; precipitate dissolves completely in dilute HCl with effervescence [1.5]; choking gas evolved turns acidified potassium dichromate(VI) paper from orange to green [1.5]."),
                PracticalSubQuestion("(c)", "Identify the gas evolved in (b) and write an ionic equation for its reaction with dichromate.", 3, lines_count=3,
                    mark_scheme="Sulfur dioxide, SO2 [1]; Cr2O7^2-(aq) + 3SO2(g) + 2H+(aq) -> 2Cr3+(aq) + 3SO4^2-(aq) + H2O(l) [2].")
            ]
        ),
        # Q6: Nitrate Reduction to Ammonia
        PracticalQuestion(
            number=6,
            title="Reduction of Nitrate Ions by Aluminium in Alkaline Solution",
            syllabus_ref="9701/33/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "A sample of potassium nitrate, KNO3, is dissolved in water. "
                "Aqueous sodium hydroxide is added, followed by small pieces of aluminium foil. The mixture is heated gently."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the observation during heating and describe how the gas evolved is identified.", 3, lines_count=3,
                    mark_scheme="Vigorous effervescence / aluminium dissolves [1]; choking pungent gas turns damp red litmus paper blue (ammonia, NH3) [2]."),
                PracticalSubQuestion("(b)", "State the changes in oxidation number of nitrogen and aluminium in this reaction.", 3, lines_count=3,
                    mark_scheme="Nitrogen is reduced from +5 (in NO3-) to -3 (in NH3) [1.5]; Aluminium is oxidized from 0 (in Al) to +3 (in [Al(OH)4]-) [1.5]."),
                PracticalSubQuestion("(c)", "Write the balanced ionic equation for this reduction.", 2, lines_count=2,
                    mark_scheme="3NO3-(aq) + 8Al(s) + 5OH-(aq) + 18H2O(l) -> 3NH3(g) + 8[Al(OH)4]-(aq) [2]."),
                PracticalSubQuestion("(d)", "Explain why red litmus paper used to test the gas must be damp.", 2, lines_count=2,
                    mark_scheme="Water is required to dissolve NH3 gas to produce OH- ions that trigger the alkaline color change of litmus: NH3 + H2O <=> NH4+ + OH- [2].")
            ]
        ),
        # Q7: Carbonate Effervescence
        PracticalQuestion(
            number=7,
            title="Analytical Verification of Carbonate Ions and Limewater Precipitation",
            syllabus_ref="9701/32/M/J/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Solid sodium carbonate, Na2CO3, is treated with dilute hydrochloric acid. "
                "The evolved gas is bubbled through limewater, Ca(OH)2(aq)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State two observations in the reaction flask when acid is added to the carbonate.", 2, lines_count=2,
                    mark_scheme="Rapid effervescence / vigorous bubbling [1]; solid dissolves to form a clear colorless solution [1]."),
                PracticalSubQuestion("(b)", "State the initial observation in the limewater and explain what happens if gas continues to bubble for several minutes.", 4, lines_count=4,
                    mark_scheme="Initial: Limewater turns milky / white precipitate of CaCO3 forms [2]; Prolonged bubbling: The milky precipitate redissolves to give a clear colorless solution [1] due to the formation of soluble calcium hydrogencarbonate, Ca(HCO3)2 [1]."),
                PracticalSubQuestion("(c)", "Write the ionic equation for the redissolution of calcium carbonate in excess CO2 and water.", 2, lines_count=2,
                    mark_scheme="CaCO3(s) + CO2(g) + H2O(l) -> Ca2+(aq) + 2HCO3-(aq) [2]."),
                PracticalSubQuestion("(d)", "Describe how to distinguish solid Na2CO3 from solid NaHCO3 using aqueous magnesium sulfate.", 2, lines_count=2,
                    mark_scheme="Add MgSO4(aq): Na2CO3 forms a white precipitate of MgCO3 immediately at room temperature [1]; NaHCO3 forms no precipitate in the cold, but gives a precipitate upon boiling [1].")
            ]
        ),
        # Q8: Diagnostic Gas Tests Suite
        PracticalQuestion(
            number=8,
            title="Comprehensive Laboratory Protocol for Analytical Gas Detection",
            syllabus_ref="9701/34/O/N/22/Q3",
            total_marks=10,
            procedure_intro=(
                "Cambridge 9701 Paper 3 tests six standard laboratory gases: NH3, CO2, Cl2, H2, O2, SO2. "
                "Candidates must apply appropriate confirmatory tests and observations."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the test and positive result for hydrogen gas, H2.", 2, lines_count=2,
                    mark_scheme="Insert a lighted wooden splint into the gas: 'pops' with a squeaky sound [2]."),
                PracticalSubQuestion("(b)", "State the test and positive result for oxygen gas, O2.", 2, lines_count=2,
                    mark_scheme="Insert a glowing wooden splint into the gas: splint relights [2]."),
                PracticalSubQuestion("(c)", "State the test and positive result for chlorine gas, Cl2.", 2, lines_count=2,
                    mark_scheme="Hold damp blue litmus paper in the gas: turns momentarily red, then is bleached completely white [2]."),
                PracticalSubQuestion("(d)", "State the test and positive result for sulfur dioxide gas, SO2.", 2, lines_count=2,
                    mark_scheme="Pass gas over paper soaked in acidified potassium dichromate(VI): color changes from orange to green [2]."),
                PracticalSubQuestion("(e)", "State the test and positive result for ammonia gas, NH3.", 2, lines_count=2,
                    mark_scheme="Hold damp red litmus paper in the gas: turns blue [2].")
            ]
        ),
        # Q9: Ammonium Ion Testing
        PracticalQuestion(
            number=9,
            title="Systematic Confirmation of the Ammonium Ion (NH4+) in Unknown Salts",
            syllabus_ref="9701/35/O/N/23/Q3",
            total_marks=10,
            procedure_intro=(
                "A solid salt contains ammonium sulfate, (NH4)2SO4. "
                "A student tests for the cation by warming with aqueous sodium hydroxide."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Describe the step-by-step method and observations to confirm NH4+.", 4, lines_count=4,
                    mark_scheme="Add aqueous NaOH to the sample in a test-tube [1]; warm gently with a Bunsen flame [1]; test vapors with damp red litmus paper held at tube mouth [1]; damp red litmus turns blue and a choking pungent smell of ammonia is detected [1]."),
                PracticalSubQuestion("(b)", "Write the ionic equation for the reaction producing ammonia.", 2, lines_count=2,
                    mark_scheme="NH4+(aq) + OH-(aq) -> NH3(g) + H2O(l) [2]."),
                PracticalSubQuestion("(c)", "Explain why red litmus must NOT touch the rim or inner wall of the test-tube.", 2, lines_count=2,
                    mark_scheme="Splashes of alkaline NaOH liquid on the tube wall would turn the paper blue directly, producing a false positive result [2]."),
                PracticalSubQuestion("(d)", "Explain why aqueous ammonia cannot be used as the reagent to test for ammonium ions.", 2, lines_count=2,
                    mark_scheme="Aqueous ammonia already contains NH3 molecules and NH4+ ions in dynamic equilibrium, making it impossible to detect NH4+ from the salt [2].")
            ]
        ),
        # Q10: Multi-Ion Unknown Salt Deduction
        PracticalQuestion(
            number=10,
            title="Deductive Identification of an Unknown Binary Inorganic Salt (Salt X)",
            syllabus_ref="9701/33/M/J/24/Q3",
            total_marks=10,
            procedure_intro=(
                "An unknown pale green solid salt, X, dissolves in distilled water to form a pale green solution.<br/>"
                "• Test 1: Addition of NaOH(aq) gives a green precipitate that turns brown on standing.<br/>"
                "• Test 2: Addition of dilute HNO3 followed by aqueous Ba(NO3)2 gives a dense white precipitate."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the cation present in salt X from Test 1, justifying your deduction.", 3, lines_count=3,
                    mark_scheme="Cation: Iron(II), Fe2+ [1]; Green precipitate of Fe(OH)2 insoluble in excess NaOH, oxidizing to brown Fe(OH)3 in air [2]."),
                PracticalSubQuestion("(b)", "Identify the anion present in salt X from Test 2, justifying your deduction.", 3, lines_count=3,
                    mark_scheme="Anion: Sulfate, SO4^2- [1]; Forms insoluble dense white precipitate of BaSO4 with acidified barium nitrate [2]."),
                PracticalSubQuestion("(c)", "Deduce the chemical formula of salt X.", 2, lines_count=2,
                    mark_scheme="FeSO4 (iron(II) sulfate) [2]."),
                PracticalSubQuestion("(d)", "Write the ionic equation for the reaction occurring in Test 2.", 2, lines_count=2,
                    mark_scheme="Ba2+(aq) + SO4^2-(aq) -> BaSO4(s) [2].")
            ]
        )
    ]

    p3_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Qualitative_Analysis_Inorganic.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, p3_questions, include_qa_notes=True)

    print("=== Inorganic Chemistry Past 10 Years Suite Complete (3 Papers) ===")

if __name__ == "__main__":
    build_inorganic_past10years()
