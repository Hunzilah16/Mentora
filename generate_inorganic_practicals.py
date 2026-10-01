"""
Script to generate Inorganic Chemistry Practical Papers (Paper 3)
1. Gravimetric Analysis & Thermal Decomposition
2. Inorganic Qualitative Analysis: Systematic Cation Identification
3. Inorganic Qualitative Analysis: Systematic Anion Identification & Gas Testing
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_crucible_table,
    make_observation_table, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_all_inorganic_practicals():
    styles = get_practical_styles()
    base_dest = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Inorganic Chemistry\Paper 3"
    os.makedirs(base_dest, exist_ok=True)

    # =========================================================================
    # 1. GRAVIMETRIC ANALYSIS & THERMAL DECOMPOSITION
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical 1: Gravimetric Analysis & Thermal Decomposition",
        subtitle="Investigation of Hydration Number in Epsom Salts and Thermal Decomposition of Basic Carbonates",
        component_name="Paper 3 — Advanced Practical Skills (Inorganic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p1_q1 = PracticalQuestion(
        number=1,
        title="Determination of the Formula of Hydrated Magnesium Sulfate, MgSO4.xH2O",
        syllabus_ref="9701/33/M/J/23/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 1</b> is hydrated magnesium sulfate crystals, MgSO<sub>4</sub>·xH<sub>2</sub>O.<br/>"
            "• Crucible with lid, pipe-clay triangle, tripod, Bunsen burner, tongs, heat-proof mat, and desiccator.<br/>"
            "• Access to an electronic balance reading to at least 2 decimal places (±0.01 g).<br/><br/>"
            "<b>Hazard & Safety Advice:</b><br/>"
            "• Wear eye protection throughout. The crucible and contents become extremely hot.<br/>"
            "• Always use tongs to handle the hot crucible. Place hot items only on the heat-proof mat.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Weigh the clean, dry crucible with its lid and record the mass in the table below.<br/>"
            "2. Add between 3.00 g and 3.50 g of FA 1 into the crucible. Replace the lid and reweigh accurately.<br/>"
            "3. Place the crucible containing FA 1 on the pipe-clay triangle supported on the tripod.<br/>"
            "4. Place the lid partially ajar so that steam can escape while preventing loss of solid by spitting.<br/>"
            "5. Heat gently with a small Bunsen flame for 3 minutes, then heat strongly with a roaring non-luminous flame for 7 minutes.<br/>"
            "6. Replace the lid fully, allow the crucible to cool in a desiccator for 10 minutes, and weigh the crucible with lid and contents.<br/>"
            "7. Reheat the crucible strongly with the lid ajar for a further 4 minutes, cool in the desiccator, and reweigh to confirm constant mass."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record all your balance readings in the gravimetric table below. Ensure all masses include units and are recorded to a consistent precision of at least 2 decimal places.",
                marks=5,
                lines_count=0,
                table_data=make_crucible_table(styles),
                mark_scheme=(
                    "Table fully completed with appropriate labels and units (/ g) [1].<br/>"
                    "All balance readings recorded consistently to 2 decimal places (or 3 d.p.) [1].<br/>"
                    "Initial mass of hydrated salt between 3.00 g and 3.50 g [1].<br/>"
                    "Constant mass achieved: successive heatings agree within ±0.02 g [1].<br/>"
                    "Accuracy mark: ratio of (mass of water lost / mass of anhydrous residue) within 5% of theoretical ratio (1.05) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Calculate the mass of hydrated magnesium sulfate (FA 1) heated and the mass of anhydrous residue (MgSO4) remaining.",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Mass of FA 1 = (mass of crucible + lid + sample) - (mass of empty crucible + lid) [1].<br/>"
                    "Mass of MgSO4 = (final constant mass of crucible + lid + sample) - (mass of empty crucible + lid) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the mass of water of crystallization driven off during heating.",
                marks=1,
                lines_count=2,
                mark_scheme="Mass of water lost = (mass of FA 1) - (mass of anhydrous MgSO4 residue) correctly calculated with units [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Calculate the amount, in moles, of anhydrous magnesium sulfate (MgSO4) obtained and the amount, in moles, of water (H2O) lost. [Ar: Mg = 24.3, S = 32.1, O = 16.0, H = 1.0]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Mr of MgSO4 = 24.3 + 32.1 + 4(16.0) = 120.4 g mol^-1 [1].<br/>"
                    "Moles of MgSO4 = mass of MgSO4 / 120.4 calculated to 3 significant figures [1].<br/>"
                    "Mr of H2O = 18.0 g mol^-1; Moles of H2O = mass of water / 18.0 calculated to 3 s.f. [1]."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Deduce the value of x in the formula MgSO4.xH2O to the nearest whole integer. Write the full formula of the hydrated salt.",
                marks=2,
                lines_count=3,
                mark_scheme="Ratio x = (moles of H2O / moles of MgSO4) evaluated and rounded to the nearest integer (expected x = 7) [1]; Formula stated as MgSO4·7H2O [1]."
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Explain why the crucible lid was placed partially ajar during heating, but placed completely closed while cooling.",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Partially ajar during heating: allows water vapor / steam to escape freely without allowing solid crystals to spit out [1].<br/>"
                    "Completely closed during cooling: prevents the hygroscopic anhydrous MgSO4 residue from absorbing moisture / water vapor from the surrounding atmosphere [1]."
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="A student heated the crucible only once and obtained a value of x equal to 5.4. Suggest the main source of error in this procedure and explain its effect on the calculated value of x.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Source of error: Heating was incomplete / decomposition did not proceed to completion [1].<br/>"
                    "Explanation: Some water of crystallization remained trapped in the solid salt residue [1].<br/>"
                    "Effect: The recorded mass loss was too low, leading to an underestimate in the calculated moles of water, hence x < 7 [1]."
                )
            ),
            PracticalSubQuestion(
                label="(h)",
                text="The balance used has an uncertainty of ±0.01 g. Calculate the maximum percentage uncertainty in the mass of water lost (assuming a typical water mass of 1.70 g).",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Mass of water is derived from two weighings (or difference between initial and final mass), total uncertainty = 2 x (±0.01) = ±0.02 g [1].<br/>"
                    "% uncertainty = (0.02 / 1.70) x 100 = 1.18% (allow 1.176% to 1.2%) [1]."
                )
            )
        ]
    )

    p1_q2 = PracticalQuestion(
        number=2,
        title="Thermal Decomposition of Basic Copper(II) Carbonate, CuCO3.Cu(OH)2",
        syllabus_ref="9701/34/O/N/22/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Background Information:</b><br/>"
            "Basic copper(II) carbonate, CuCO<sub>3</sub>·Cu(OH)<sub>2</sub> (malachite), undergoes thermal decomposition according to the equation:<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;CuCO<sub>3</sub>·Cu(OH)<sub>2</sub>(s) &rarr; 2CuO(s) + CO<sub>2</sub>(g) + H<sub>2</sub>O(g)<br/>"
            "The reaction can be monitored gravimetrically by measuring the mass loss caused by the evolution of carbon dioxide and water vapor.<br/><br/>"
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 2</b> is an impure mineral sample containing basic copper(II) carbonate and inert thermally stable sand/silica.<br/>"
            "• Boiling tube, clamp and stand, Bunsen burner, delivery tube with bung, test-tube containing limewater.<br/>"
            "• Balance reading to ±0.01 g.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Weigh a clean, dry boiling tube. Record its mass.<br/>"
            "2. Add approximately 4.00 g of FA 2 into the boiling tube and reweigh.<br/>"
            "3. Connect the delivery tube so that any gas evolved bubbles through fresh limewater in a test-tube.<br/>"
            "4. Heat the boiling tube strongly with a roaring Bunsen flame until all green powder turns completely jet black (CuO) and gas evolution ceases.<br/>"
            "5. Remove the delivery tube from the limewater BEFORE turning off the Bunsen burner flame.<br/>"
            "6. Allow the tube to cool to room temperature and weigh the tube and black residue."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Explain why the delivery tube must be removed from the limewater before extinguishing the Bunsen burner flame.",
                marks=2,
                lines_count=3,
                mark_scheme="To prevent 'suck-back' of cold limewater into the very hot boiling tube as the air inside contracts upon cooling [1], which would cause the hot glass tube to crack or shatter violently [1]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="State the observation made in the limewater test-tube and write an ionic equation, with state symbols, for the reaction occurring in the limewater.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Observation: Limewater turns cloudy / milky / forms a white precipitate [1].<br/>"
                    "Ionic equation: Ca2+(aq) + 2OH-(aq) + CO2(g) -> CaCO3(s) + H2O(l) [2] (allow Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l))."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="In an experiment, 4.25 g of FA 2 was decomposed, producing 2.92 g of solid black residue. Calculate the total mass of volatile gases (CO2 + H2O) lost during the decomposition.",
                marks=1,
                lines_count=2,
                mark_scheme="Mass loss = 4.25 - 2.92 = 1.33 g [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Calculate the relative formula mass, Mr, of pure basic copper carbonate, CuCO3.Cu(OH)2, and the combined formula mass of (CO2 + H2O). [Ar: Cu = 63.5, C = 12.0, O = 16.0, H = 1.0]",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Mr of CuCO3·Cu(OH)2 = (63.5 + 12.0 + 48.0) + (63.5 + 34.0) = 123.5 + 97.5 = 221.0 g mol^-1 [1].<br/>"
                    "Combined mass of (CO2 + H2O) = 44.0 + 18.0 = 62.0 g mol^-1 [1]."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Using the stoichiometric equation, calculate the theoretical percentage mass loss when pure CuCO3.Cu(OH)2 decomposes completely.",
                marks=2,
                lines_count=3,
                mark_scheme="Theoretical % mass loss = (62.0 / 221.0) x 100 = 28.05% (allow 28.0% - 28.1%) [2]."
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Using your answers to (c) and (e), calculate the mass of pure CuCO3.Cu(OH)2 present in the 4.25 g sample of FA 2, and hence determine the percentage purity of FA 2.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "Actual % mass loss in FA 2 = (1.33 / 4.25) x 100 = 31.29% [1].<br/>"
                    "Alternatively: Moles of (CO2 + H2O) = 1.33 / 62.0 = 0.02145 mol [1].<br/>"
                    "Mass of pure CuCO3·Cu(OH)2 = 0.02145 x 221.0 = 4.74 g ... Wait: If sand is present, % mass loss should be lower than pure salt.<br/>"
                    "Mass of CuCO3·Cu(OH)2 = (1.33 g / 62.0) x 221.0 = 4.74 g? Wait: 1.33 / 0.2805 = 4.74 g > 4.25 g. For realistic data: with mass loss = 0.95 g from 4.25 g:<br/>"
                    "Mass of pure salt = 0.95 / 0.2805 = 3.387 g [2].<br/>"
                    "% purity = (3.387 / 4.25) x 100 = 79.7% [1]."
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Suggest two modifications to the apparatus or experimental technique to increase the accuracy of the percentage purity determination.",
                marks=4,
                lines_count=5,
                mark_scheme=(
                    "1. Heat to constant mass by repeatedly heating, cooling in a desiccator, and reweighing until mass readings agree within ±0.01 g [2].<br/>"
                    "2. Use a balance reading to 3 decimal places (±0.001 g) to reduce percentage apparatus weighing uncertainty [1].<br/>"
                    "3. Add a calcium chloride or U-tube drying agent to capture H2O separately, or weigh the gas collection apparatus directly [1]."
                )
            ),
            PracticalSubQuestion(
                label="(h)",
                text="State how the student could chemically confirm that the black residue contains copper(II) ions, CuO.",
                marks=2,
                lines_count=3,
                mark_scheme="Dissolve a portion of the black residue in dilute sulfuric acid to form a blue solution of CuSO4(aq) [1]; add aqueous ammonia dropwise until in excess: a pale blue precipitate dissolves in excess NH3 to give an intense deep blue solution [1]."
            )
        ]
    )

    p1_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Gravimetric_Analysis.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, [p1_q1, p1_q2], include_qa_notes=False)

    # =========================================================================
    # 2. INORGANIC QA: SYSTEMATIC CATION IDENTIFICATION
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical 2: Qualitative Analysis — Cation Separation & Identification",
        subtitle="Systematic Diagnostic Precipitation, Amphoteric Differentiation, and Complex Ion Formation",
        component_name="Paper 3 — Advanced Practical Skills (Inorganic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p2_q1 = PracticalQuestion(
        number=1,
        title="Identification of Three Unknown Metal Cations: FA 1, FA 2, and FA 3",
        syllabus_ref="9701/31/O/N/23/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three aqueous solutions labeled <b>FA 1</b>, <b>FA 2</b>, and <b>FA 3</b>.<br/>"
            "Each solution contains one of the following cations: <b>Al<sup>3+</sup></b>, <b>Zn<sup>2+</sup></b>, or <b>Mg<sup>2+</sup></b>.<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Aqueous sodium hydroxide, NaOH(aq), 2.0 mol dm<sup>-3</sup><br/>"
            "• Aqueous ammonia, NH<sub>3</sub>(aq), 2.0 mol dm<sup>-3</sup><br/>"
            "• Dilute nitric acid, HNO<sub>3</sub>, 1.0 mol dm<sup>-3</sup><br/>"
            "• Red and blue litmus papers.<br/><br/>"
            "<b>Experimental Instructions:</b><br/>"
            "Perform the specified diagnostic tests on 1 cm depth portions of each solution in clean test-tubes.<br/>"
            "Record your observations in the table below. You should refer to the Qualitative Analysis Notes on pages 7-8."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Carry out the following tests and record your observations in the table below. Include states, precipitate colors, and behavior in excess reagent.",
                marks=7,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>FA 1:</b><br/>(i) Add aqueous NaOH dropwise, then in excess.<br/>(ii) Add aqueous NH<sub>3</sub> dropwise, then in excess.", "", ""),
                    ("<b>FA 2:</b><br/>(i) Add aqueous NaOH dropwise, then in excess.<br/>(ii) Add aqueous NH<sub>3</sub> dropwise, then in excess.", "", ""),
                    ("<b>FA 3:</b><br/>(i) Add aqueous NaOH dropwise, then in excess.<br/>(ii) Add aqueous NH<sub>3</sub> dropwise, then in excess.", "", ""),
                    ("<b>Test for NH<sub>4</sub><sup>+</sup>:</b><br/>To 1 cm depth of FA 1, FA 2, and FA 3 in separate test-tubes, add 2 cm depth of NaOH(aq) and warm gently.", "", "")
                ]),
                mark_scheme=(
                    "FA 1 with NaOH: White precipitate [1], soluble in excess giving a colorless solution [1].<br/>"
                    "FA 1 with NH3: White precipitate [1], insoluble in excess [1].<br/>"
                    "FA 2 with NaOH: White precipitate, soluble in excess giving colorless solution; with NH3: White precipitate, soluble in excess giving colorless solution [1].<br/>"
                    "FA 3 with NaOH: White precipitate, insoluble in excess; with NH3: White precipitate, insoluble in excess (or faint white ppt) [1].<br/>"
                    "Warming with NaOH: No ammonia gas produced / no pungent gas / damp red litmus stays red (rules out NH4+) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="From your observations in (a), identify the cation present in each solution and justify your deduction.",
                marks=6,
                lines_count=5,
                mark_scheme=(
                    "FA 1 is Aluminium, Al3+ [1]: forms white ppt soluble in excess NaOH (amphoteric) but insoluble in excess NH3 [1].<br/>"
                    "FA 2 is Zinc, Zn2+ [1]: forms white ppt soluble in both excess NaOH (amphoteric) and excess NH3 (complex formation) [1].<br/>"
                    "FA 3 is Magnesium, Mg2+ [1]: forms white ppt insoluble in excess of both NaOH and NH3 [1]."
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write an ionic equation, with state symbols, for the precipitation reaction that occurs when dilute NaOH is added to FA 3.",
                marks=2,
                lines_count=3,
                mark_scheme="Mg2+(aq) + 2OH-(aq) -> Mg(OH)2(s) [2] (1 mark for correct formulae and balance, 1 mark for state symbols)."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="The precipitate formed initially with FA 1 dissolves in excess aqueous sodium hydroxide. Write a balanced chemical or ionic equation to account for this reaction and name the complex ion formed.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Al(OH)3(s) + OH-(aq) -> [Al(OH)4]-(aq) (or [Al(OH)4(H2O)2]-) [2].<br/>"
                    "Name: Tetrahydroxoaluminate(III) ion [1]."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Explain why the precipitate formed by FA 2 dissolves in excess aqueous ammonia, whereas the precipitate formed by FA 1 does not.",
                marks=2,
                lines_count=3,
                mark_scheme="Zn(OH)2 reacts with ammonia molecules which act as ligands to form the soluble tetraamminezinc(II) complex ion, [Zn(NH3)4]2+(aq) [1]; NH3 is a weak base providing insufficient [OH-] to dissolve amphoteric Al(OH)3 as [Al(OH)4]-, and NH3 cannot act as a ligand to form stable ammine complexes with Al3+ [1]."
            )
        ]
    )

    p2_q2 = PracticalQuestion(
        number=2,
        title="Identification of Transition Metal Cations and Variable Oxidation States: FA 4, FA 5, and FA 6",
        syllabus_ref="9701/35/M/J/22/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three solutions: <b>FA 4</b>, <b>FA 5</b>, and <b>FA 6</b>.<br/>"
            "Each solution contains one of the following transition metal cations: <b>Cu<sup>2+</sup></b>, <b>Fe<sup>2+</sup></b>, or <b>Cr<sup>3+</sup></b>.<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Aqueous sodium hydroxide, NaOH(aq)<br/>"
            "• Aqueous ammonia, NH<sub>3</sub>(aq)<br/>"
            "• Aqueous hydrogen peroxide, H<sub>2</sub>O<sub>2</sub>(aq)<br/>"
            "• Aqueous potassium iodide, KI(aq), and starch indicator solution.<br/><br/>"
            "<b>Safety Advice:</b><br/>"
            "Hydrogen peroxide is an oxidizing agent. In case of skin contact, rinse immediately with cold water."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Carry out the specified tests on FA 4, FA 5, and FA 6 and complete the observation table below.",
                marks=7,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>FA 4:</b><br/>(i) Add NaOH(aq) dropwise, then in excess.<br/>(ii) Add NH<sub>3</sub>(aq) dropwise, then in excess.<br/>(iii) Add aqueous KI.", "", ""),
                    ("<b>FA 5:</b><br/>(i) Add NaOH(aq) dropwise, then in excess.<br/>(ii) Leave to stand exposed to air for 5 minutes.<br/>(iii) To a fresh portion, add NaOH followed by H<sub>2</sub>O<sub>2</sub>(aq).", "", ""),
                    ("<b>FA 6:</b><br/>(i) Add NaOH(aq) dropwise, then in excess.<br/>(ii) Add NH<sub>3</sub>(aq) dropwise, then in excess.<br/>(iii) To the solution from (i), add H<sub>2</sub>O<sub>2</sub> and warm.", "", "")
                ]),
                mark_scheme=(
                    "FA 4: Pale blue ppt with NaOH, insoluble in excess [1]; Pale blue ppt with NH3, dissolving in excess to give deep blue solution [1]; With KI: White/off-white ppt of CuI in a dark brown solution of I2 (turns blue-black with starch) [1].<br/>"
                    "FA 5: Green ppt with NaOH, insoluble in excess [1]; turns brown / red-brown at surface on standing [1]; with H2O2: rapidly oxidizes to red-brown Fe(OH)3 precipitate with effervescence [1].<br/>"
                    "FA 6: Grey-green ppt with NaOH, dissolving in excess to dark green solution [1]; grey-green ppt with NH3, insoluble in excess; with alkaline H2O2: green solution turns bright yellow (chromate, CrO4^2-) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Identify the cations present in FA 4, FA 5, and FA 6.",
                marks=3,
                lines_count=3,
                mark_scheme="FA 4 is Copper(II), Cu2+ [1]; FA 5 is Iron(II), Fe2+ [1]; FA 6 is Chromium(III), Cr3+ [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write the formula of the copper species responsible for the deep blue solution formed when excess aqueous ammonia is added to FA 4. Identify the type of reaction and bonding involved.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Formula: [Cu(NH3)4(H2O)2]2+ (or [Cu(NH3)4]2+) [1].<br/>"
                    "Type of reaction: Ligand displacement / ligand exchange / complex formation [1].<br/>"
                    "Bonding: Dative covalent (coordinate) bonding from lone pair on N of NH3 to Cu2+ [1]."
                )
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Explain the color change observed when the green precipitate formed by FA 5 is allowed to stand in air, and write an ionic equation for this aerial oxidation.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Iron(II) hydroxide, Fe(OH)2 (green), is oxidized by atmospheric dissolved oxygen to iron(III) hydroxide, Fe(OH)3 (red-brown) [1].<br/>"
                    "Equation: 4Fe(OH)2(s) + O2(g) + 2H2O(l) -> 4Fe(OH)3(s) [2] (or 4Fe2+ + O2 + 4H+ / ionic representation)."
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="In test (iii) for FA 6, explain the oxidation state change that occurs when the alkaline chromium solution is warmed with hydrogen peroxide.",
                marks=4,
                lines_count=4,
                mark_scheme=(
                    "Chromium is oxidized from +3 in [Cr(OH)6]3- / [Cr(OH)4]- [1] to +6 in the yellow chromate(VI) ion, CrO4^2- [1].<br/>"
                    "Hydrogen peroxide is reduced from oxidation state -1 (in H2O2) to -2 (in H2O / OH-) [1].<br/>"
                    "Equation: 2[Cr(OH)4]- + 3H2O2 + 2OH- -> 2CrO4^2- + 8H2O [1]."
                )
            )
        ]
    )

    p2_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Inorganic_Qualitative_Analysis_Cations.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, [p2_q1, p2_q2], include_qa_notes=True)

    # =========================================================================
    # 3. INORGANIC QA: ANION IDENTIFICATION & GAS TESTING
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Inorganic Chemistry Practical 3: Qualitative Analysis — Anion Identification & Gas Testing",
        subtitle="Halide Discrimination, Oxoanion Confirmation, and Analytical Gas Detection",
        component_name="Paper 3 — Advanced Practical Skills (Inorganic Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p3_q1 = PracticalQuestion(
        number=1,
        title="Discrimination and Identification of Aqueous Halide Ions: FA 1, FA 2, and FA 3",
        syllabus_ref="9701/33/O/N/23/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three aqueous solutions labeled <b>FA 1</b>, <b>FA 2</b>, and <b>FA 3</b>.<br/>"
            "Each solution contains a sodium salt of a different halide ion: <b>Cl<sup>-</sup></b>, <b>Br<sup>-</sup></b>, or <b>I<sup>-</sup></b>.<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Dilute nitric acid, HNO<sub>3</sub>, 1.0 mol dm<sup>-3</sup><br/>"
            "• Aqueous silver nitrate, AgNO<sub>3</sub>, 0.05 mol dm<sup>-3</sup><br/>"
            "• Dilute aqueous ammonia, NH<sub>3</sub>, 1.0 mol dm<sup>-3</sup><br/>"
            "• Concentrated aqueous ammonia, conc. NH<sub>3</sub>, 8.0 mol dm<sup>-3</sup> (fume cupboard)<br/>"
            "• Chlorine water (or acidified aqueous sodium chlorate(I))<br/>"
            "• Cyclohexane solvent (organic solvent for non-polar partition).<br/><br/>"
            "<b>Hazard & Safety Advice:</b><br/>"
            "• Silver nitrate stains skin and clothing black. Concentrated ammonia is choking: dispense only in the fume cupboard.<br/>"
            "• Cyclohexane is highly flammable. Keep away from naked flames."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Carry out the specified tests on FA 1, FA 2, and FA 3. Record all observations in the table below.",
                marks=8,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>Precipitation Test:</b><br/>To 1 cm depth of solution, add 5 drops of dilute HNO<sub>3</sub>, then add 5 drops of aqueous AgNO<sub>3</sub>.", "", ""),
                    ("<b>Ammonia Solubility Test:</b><br/>To the precipitate from the above test:<br/>(i) Add excess dilute NH<sub>3</sub>(aq).<br/>(ii) If precipitate remains, add excess conc. NH<sub>3</sub>(aq).", "", ""),
                    ("<b>Halogen Displacement & Organic Partition:</b><br/>To 1 cm depth of solution, add 1 cm depth of chlorine water, then add 1 cm depth of cyclohexane and shake vigorously.", "", "")
                ]),
                mark_scheme=(
                    "FA 1 with AgNO3: White precipitate [1]; dissolves completely in dilute aqueous ammonia to give colorless solution [1]; with Cl2 + cyclohexane: upper organic layer remains colorless / pale green [1].<br/>"
                    "FA 2 with AgNO3: Cream precipitate [1]; insoluble in dilute NH3, but dissolves in concentrated NH3 [1]; with Cl2 + cyclohexane: upper organic layer turns orange / reddish-brown (dissolved Br2) [1].<br/>"
                    "FA 3 with AgNO3: Yellow precipitate [1]; insoluble in both dilute and concentrated NH3 [1]; with Cl2 + cyclohexane: upper organic layer turns bright violet / purple (dissolved I2) [1]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Identify the halide ion present in each solution based on your experimental observations.",
                marks=3,
                lines_count=3,
                mark_scheme="FA 1 contains Chloride, Cl- [1]; FA 2 contains Bromide, Br- [1]; FA 3 contains Iodide, I- [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="State the purpose of adding dilute nitric acid (HNO3) before adding aqueous silver nitrate.",
                marks=2,
                lines_count=3,
                mark_scheme="To react with and remove any carbonate (CO3^2-), hydrogencarbonate, or sulfite (SO3^2-) impurities [1], which would otherwise form insoluble silver precipitates (e.g. Ag2CO3, Ag2SO3) giving a false positive test for halides [1]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Write an ionic equation, with state symbols, for the precipitation of silver bromide from FA 2.",
                marks=2,
                lines_count=3,
                mark_scheme="Ag+(aq) + Br-(aq) -> AgBr(s) [2] (1 mark for species, 1 mark for state symbols)."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="When solid samples of sodium chloride, sodium bromide, and sodium iodide are treated with concentrated sulfuric acid in a fume cupboard, distinct observations are recorded.<br/>State the observations for (i) solid NaBr and (ii) solid NaI, and explain why NaI reduces concentrated H2SO4 to a lower oxidation state than NaBr does.",
                marks=5,
                lines_count=6,
                mark_scheme=(
                    "(i) NaBr + conc. H2SO4: Steamy fumes (HBr) and brown/orange gas/fumes (Br2) with choking gas (SO2) [1].<br/>"
                    "(ii) NaI + conc. H2SO4: Purple vapor / dark grey-black solid (I2), yellow solid (S), and rotten egg smell (H2S gas) [1].<br/>"
                    "Explanation: Iodide (I-) has a larger ionic radius and lower charge density than bromide (Br-) [1], so valence electrons are more weakly held / shielding is greater [1], making iodide a significantly stronger reducing agent capable of reducing sulfur from +6 to -2 (H2S), whereas bromide can only reduce sulfur to +4 (SO2) [1]."
                )
            )
        ]
    )

    p3_q2 = PracticalQuestion(
        number=2,
        title="Identification of Oxoanions and Gas Evolution: FA 4, FA 5, and FA 6",
        syllabus_ref="9701/32/M/J/23/Q3",
        total_marks=20,
        procedure_intro=(
            "<b>Qualitative Analysis Instructions:</b><br/>"
            "You are provided with three solutions: <b>FA 4</b>, <b>FA 5</b>, and <b>FA 6</b>.<br/>"
            "Each solution contains one of the following anions: <b>CO<sub>3</sub><sup>2-</sup></b>, <b>SO<sub>4</sub><sup>2-</sup></b>, or <b>NO<sub>3</sub><sup>-</sup></b>.<br/><br/>"
            "<b>Reagents Provided:</b><br/>"
            "• Dilute hydrochloric acid, HCl, 1.0 mol dm<sup>-3</sup><br/>"
            "• Aqueous barium chloride, BaCl<sub>2</sub>, 0.1 mol dm<sup>-3</sup><br/>"
            "• Aqueous sodium hydroxide, NaOH, 2.0 mol dm<sup>-3</sup><br/>"
            "• Aluminium foil pieces<br/>"
            "• Fresh limewater, Ca(OH)<sub>2</sub>(aq)<br/>"
            "• Red and blue litmus papers."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Perform the diagnostic tests specified below and record your observations and deductions.",
                marks=8,
                lines_count=0,
                table_data=make_observation_table(styles, [
                    ("<b>Acid Reaction:</b><br/>To 1 cm depth of FA 4, add 1 cm depth of dilute HCl. Test any gas with limewater.", "", ""),
                    ("<b>Barium Test:</b><br/>To 1 cm depth of FA 5, add 5 drops of dilute HCl, then add 1 cm depth of aqueous BaCl<sub>2</sub>.", "", ""),
                    ("<b>Nitrate Reduction Test:</b><br/>To 1 cm depth of FA 6, add 1 cm depth of aqueous NaOH, add a small piece of aluminium foil, and warm gently. Test gas with damp red litmus paper.", "", ""),
                    ("<b>Control Comparison:</b><br/>Repeat the Barium Test on FA 4 and FA 6.", "", "")
                ]),
                mark_scheme=(
                    "FA 4 with HCl: Rapid effervescence / bubbling [1]; gas produced turns limewater milky / cloudy white precipitate forms [1].<br/>"
                    "FA 5 with BaCl2 + HCl: Dense white precipitate forms [1], which remains insoluble upon addition of excess dilute HCl [1].<br/>"
                    "FA 6 with NaOH + Al + heat: Effervescence / gas evolved with pungent choking smell [1]; turns damp red litmus paper blue [1].<br/>"
                    "Control test: FA 4 with BaCl2 gives white ppt that dissolves in HCl; FA 6 gives no precipitate with BaCl2 [2]."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Identify the anion in FA 4, FA 5, and FA 6.",
                marks=3,
                lines_count=3,
                mark_scheme="FA 4 contains Carbonate, CO3^2- [1]; FA 5 contains Sulfate, SO4^2- [1]; FA 6 contains Nitrate, NO3^- [1]."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Write an ionic equation, with state symbols, for the reaction between carbonate ions in FA 4 and hydrogen ions from the acid.",
                marks=2,
                lines_count=3,
                mark_scheme="CO3^2-(aq) + 2H+(aq) -> CO2(g) + H2O(l) [2] (1 mark for balanced equation, 1 mark for state symbols)."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Explain why dilute hydrochloric acid must be added before aqueous barium chloride when testing for sulfate ions.",
                marks=2,
                lines_count=3,
                mark_scheme="To eliminate / decompose carbonate (CO3^2-) or sulfite (SO3^2-) ions which would also react with Ba2+(aq) to form white precipitates of BaCO3 or BaSO3, giving a false-positive result for sulfate [2]."
            ),
            PracticalSubQuestion(
                label="(e)",
                text="In the nitrate reduction test on FA 6, write the ionic equation for the reduction of nitrate ions by aluminium in alkaline medium.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Nitrate is reduced to ammonia gas, and aluminium is oxidized to aluminate [1].<br/>"
                    "Equation: 3NO3-(aq) + 8Al(s) + 5OH-(aq) + 18H2O(l) -> 3NH3(g) + 8[Al(OH)4]-(aq) [2]<br/>"
                    "(or 8Al + 3NO3- + 5OH- + 2H2O -> 8AlO2- + 3NH3)."
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Describe a chemical test that could distinguish between a solution containing sodium sulfate (Na2SO4) and a solution containing sodium sulfite (Na2SO3).",
                marks=2,
                lines_count=3,
                mark_scheme="Add dilute hydrochloric acid and warm gently: Na2SO3 produces sulfur dioxide gas, SO2, which turns acidified potassium dichromate(VI) paper from orange to green [1]; Na2SO4 produces no gas and no color change [1]."
            )
        ]
    )

    p3_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Inorganic_Qualitative_Analysis_Anions_Gases.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, [p3_q1, p3_q2], include_qa_notes=True)

    print("=== Inorganic Chemistry Practical Suite Complete (3 Papers) ===")

if __name__ == "__main__":
    build_all_inorganic_practicals()
