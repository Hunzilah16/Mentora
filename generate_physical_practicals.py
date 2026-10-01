"""
Script to generate Physical Chemistry Practical Papers (Paper 3)
1. Acid-Base & Back Titrations
2. Redox Titrations (KMnO4 & Iodine-Thiosulfate)
3. Thermochemistry & Calorimetry (Cooling Curves)
4. Reaction Kinetics (Gas Syringe & Disappearing Cross)
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_titration_table,
    make_thermometry_table, make_observation_table,
    COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_all_physical_practicals():
    styles = get_practical_styles()
    base_dest = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Physical Chemistry\Paper 3"
    os.makedirs(base_dest, exist_ok=True)

    # =========================================================================
    # 1. ACID-BASE & BACK TITRATIONS
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical 1: Volumetric Analysis — Acid-Base & Back Titrations",
        subtitle="Investigation of Monoprotic, Diprotic, and Back Titration Techniques with Purity Analysis",
        component_name="Paper 3 — Advanced Practical Skills (Physical Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p1_q1 = PracticalQuestion(
        number=1,
        title="Determination of the Concentration of a Monoprotic Acid (FA 2) by Titration",
        syllabus_ref="9701/31/M/J/23/Q1",
        total_marks=16,
        procedure_intro=(
            "<b>Chemicals and Solutions Provided:</b><br/>"
            "• <b>FA 1</b> is aqueous sodium hydroxide, containing 4.20 g dm<sup>-3</sup> of NaOH (Mr = 40.0).<br/>"
            "• <b>FA 2</b> is dilute hydrochloric acid, HCl, of unknown concentration.<br/>"
            "• <b>Methyl orange</b> indicator solution.<br/><br/>"
            "<b>Hazard & Safety Advice:</b><br/>"
            "• Wear eye protection. FA 1 is corrosive and an irritant; FA 2 is an irritant. Wash splashes immediately.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Fill the burette with FA 2.<br/>"
            "2. Pipette 25.0 cm<sup>3</sup> of FA 1 into a clean conical flask.<br/>"
            "3. Add 2-3 drops of methyl orange indicator. The solution turns yellow.<br/>"
            "4. Titrate FA 1 with FA 2 until the indicator turns permanently from yellow to orange/red.<br/>"
            "5. Record your burette readings in the table below. Perform sufficient titrations to obtain concordant results (within 0.10 cm<sup>3</sup>)."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your burette readings and the volumes of FA 2 added in the table below. Indicate your concordant titres with a tick (&#10003;).",
                marks=5,
                lines_count=0,
                table_data=make_titration_table(styles),
                mark_scheme=(
                    "Award 1 mark for clear burette table with correct headers and units.<br/>"
                    "Award 1 mark for recording all volumes to 0.05 cm<sup>3</sup>.<br/>"
                    "Award 1 mark for obtaining two concordant titres within 0.10 cm<sup>3</sup>.<br/>"
                    "Award 1-2 marks for accuracy compared to supervisor's titre (within 0.20 cm<sup>3</sup> = 2 marks; within 0.30 cm<sup>3</sup> = 1 mark)."
                )
            ),
            PracticalSubQuestion(
                label="(b)",
                text="From your selected titration results, calculate the mean volume (titre) of FA 2 required. Show which values you used.",
                marks=1,
                lines_count=2,
                mark_scheme="Mean correctly calculated from selected ticked titres within 0.10 cm<sup>3</sup>, quoted to 2 decimal places (e.g. 23.45 cm<sup>3</sup>)."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the amount, in moles, of sodium hydroxide present in the 25.0 cm<sup>3</sup> portion of FA 1 used in each titration.",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "Concentration of NaOH = 4.20 / 40.0 = 0.105 mol dm<sup>-3</sup> [1]<br/>"
                    "Moles in 25.0 cm<sup>3</sup> = 0.105 x (25.0 / 1000) = 2.625 x 10<sup>-3</sup> mol [1]"
                )
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Write the balanced chemical equation for the neutralization reaction between HCl and NaOH. Hence deduce the amount, in moles, of HCl present in your mean titre of FA 2.",
                marks=2,
                lines_count=3,
                mark_scheme=(
                    "HCl + NaOH -> NaCl + H2O [1]<br/>"
                    "Mole ratio is 1:1, so moles of HCl = 2.625 x 10<sup>-3</sup> mol [1]"
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Calculate the concentration of hydrochloric acid in FA 2, in mol dm<sup>-3</sup>. Give your final answer to three significant figures.",
                marks=2,
                lines_count=3,
                mark_scheme="Concentration of FA 2 = (2.625 x 10<sup>-3</sup> / Titre) x 1000. For titre = 23.45 cm<sup>3</sup>, conc = 0.112 mol dm<sup>-3</sup>. (Allow ECF from part (b)). [2]"
            ),
            PracticalSubQuestion(
                label="(f)",
                text="The manufacturer specifies that the uncertainty of each burette reading is ±0.05 cm<sup>3</sup>. Calculate the maximum percentage apparatus uncertainty in your titre volume.",
                marks=2,
                lines_count=3,
                mark_scheme="Two readings per titre, total uncertainty = 2 x 0.05 = 0.10 cm<sup>3</sup>. % uncertainty = (0.10 / Titre) x 100%. (e.g. 0.10 / 23.45 x 100% = 0.426%). [2]"
            ),
            PracticalSubQuestion(
                label="(g)",
                text="A student washed the conical flask with the sodium hydroxide solution FA 1 immediately before pipetting the 25.0 cm<sup>3</sup> sample into it. Explain what effect, if any, this error would have on the calculated concentration of FA 2.",
                marks=2,
                lines_count=3,
                mark_scheme="Droplets of FA 1 adhering to the flask walls increase the total moles of NaOH present. This requires a larger volume of FA 2 to reach the endpoint. Because Titre is in the denominator, the calculated concentration of FA 2 would be lower than the true value. [2]"
            )
        ]
    )

    p1_q2 = PracticalQuestion(
        number=2,
        title="Back Titration: Determination of Calcium Carbonate Purity in Limestone",
        syllabus_ref="9701/33/M/J/23/Q1",
        total_marks=24,
        procedure_intro=(
            "<b>Chemicals and Solutions Provided:</b><br/>"
            "• <b>FA 3</b> is an impure solid limestone sample containing calcium carbonate, CaCO3.<br/>"
            "• <b>FA 4</b> is 1.00 mol dm<sup>-3</sup> hydrochloric acid, HCl.<br/>"
            "• <b>FA 5</b> is 0.100 mol dm<sup>-3</sup> sodium hydroxide, NaOH.<br/>"
            "• <b>Phenolphthalein</b> indicator.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Weigh accurately 1.50 g of the solid limestone sample FA 3 into a 250 cm<sup>3</sup> beaker.<br/>"
            "2. Using a pipette, add exactly 50.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> HCl (FA 4) to the beaker. Effervescence occurs.<br/>"
            "3. Swirl the beaker until all calcium carbonate has reacted and effervescence ceases completely.<br/>"
            "4. Transfer the mixture quantitatively into a 250 cm<sup>3</sup> volumetric flask, rinse the beaker with distilled water, add the washings, and make up to the mark with distilled water. Invert thoroughly to mix. Label this solution <b>FA 6</b>.<br/>"
            "5. Pipette 25.0 cm<sup>3</sup> of FA 6 into a conical flask, add 3 drops of phenolphthalein, and titrate with 0.100 mol dm<sup>-3</sup> NaOH (FA 5) from the burette."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your titration results for the titration of 25.0 cm<sup>3</sup> portions of FA 6 with 0.100 mol dm<sup>-3</sup> NaOH (FA 5) in the table below.",
                marks=5,
                lines_count=0,
                table_data=make_titration_table(styles),
                mark_scheme="Burette table formatted correctly, readings to 0.05 cm<sup>3</sup>, concordant titres within 0.10 cm<sup>3</sup>, accuracy marks [5]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="State the suitable mean titre of FA 5 to be used in your calculations.",
                marks=1,
                lines_count=2,
                mark_scheme="Correct mean titre calculated from concordant runs to 2 decimal places (e.g. 21.80 cm<sup>3</sup>)."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the amount, in moles, of NaOH present in your mean titre of FA 5.",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of NaOH = 0.100 x (Titre / 1000). For 21.80 cm<sup>3</sup>: moles = 2.18 x 10<sup>-3</sup> mol. [2]"
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Deduce the amount, in moles, of unreacted HCl present in the 25.0 cm<sup>3</sup> sample of FA 6, and hence calculate the total amount of unreacted HCl in the entire 250 cm<sup>3</sup> volumetric flask.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "HCl + NaOH -> NaCl + H2O (1:1 ratio), so unreacted HCl in 25.0 cm<sup>3</sup> = 2.18 x 10<sup>-3</sup> mol [1]<br/>"
                    "Total unreacted HCl in 250 cm<sup>3</sup> = 2.18 x 10<sup>-3</sup> x (250 / 25.0) = 2.18 x 10<sup>-2</sup> mol (0.0218 mol) [2]"
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Calculate the initial amount, in moles, of HCl added to the limestone sample (in the 50.0 cm<sup>3</sup> of FA 4).",
                marks=2,
                lines_count=3,
                mark_scheme="Initial moles of HCl = 1.00 mol dm<sup>-3</sup> x (50.0 / 1000) = 0.0500 mol. [2]"
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Calculate the amount, in moles, of HCl that reacted with the calcium carbonate in the limestone sample.",
                marks=2,
                lines_count=3,
                mark_scheme="Reacted moles of HCl = Initial moles - Unreacted moles = 0.0500 - 0.0218 = 0.0282 mol. [2]"
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Write the balanced equation for the reaction of calcium carbonate with hydrochloric acid. Hence calculate the mass of calcium carbonate present in the 1.50 g limestone sample. [Ar: Ca = 40.1, C = 12.0, O = 16.0]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 [1]<br/>"
                    "Moles of CaCO3 = Moles of HCl reacted / 2 = 0.0282 / 2 = 0.0141 mol [1]<br/>"
                    "Mr(CaCO3) = 40.1 + 12.0 + 48.0 = 100.1 g/mol.<br/>"
                    "Mass of CaCO3 = 0.0141 x 100.1 = 1.411 g [1]"
                )
            ),
            PracticalSubQuestion(
                label="(h)",
                text="Calculate the percentage by mass of calcium carbonate in the limestone sample.",
                marks=2,
                lines_count=3,
                mark_scheme="% purity = (1.411 g / 1.50 g) x 100% = 94.1%. [2]"
            ),
            PracticalSubQuestion(
                label="(i)",
                text="Suggest why back-titration is preferred over direct titration of solid calcium carbonate with hydrochloric acid.",
                marks=2,
                lines_count=3,
                mark_scheme="Calcium carbonate is an insoluble solid that reacts slowly with acid near the endpoint; determining a sharp visual indicator endpoint with a solid suspension is difficult and inaccurate. Dissolving completely in excess acid produces a homogeneous solution that allows a sharp, precise endpoint with standard alkali. [2]"
            ),
            PracticalSubQuestion(
                label="(j)",
                text="State how the student could verify that all the calcium carbonate in the limestone had completely dissolved in the acid before making up the solution to the mark.",
                marks=2,
                lines_count=3,
                mark_scheme="Ensure effervescence has completely stopped and no solid particles remain at the bottom of the beaker (or only insoluble siliceous grit/sand remains). Gentle warming can be applied to ensure complete reaction. [2]"
            )
        ]
    )

    p1_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Acid_Base_Titrations.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, [p1_q1, p1_q2], include_qa_notes=False)

    # =========================================================================
    # 2. REDOX TITRATIONS (KMnO4 & Iodine-Thiosulfate)
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical 2: Volumetric Analysis — Redox Titrations",
        subtitle="Potassium Manganate(VII) Iron Analysis & Iodine-Thiosulfate Copper Determinations",
        component_name="Paper 3 — Advanced Practical Skills (Physical Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p2_q1 = PracticalQuestion(
        number=1,
        title="Determination of Iron(II) in Mohr's Salt by Titration with Potassium Manganate(VII)",
        syllabus_ref="9701/32/M/J/23/Q1",
        total_marks=20,
        procedure_intro=(
            "<b>Chemicals and Solutions Provided:</b><br/>"
            "• <b>FA 1</b> is 0.0200 mol dm<sup>-3</sup> potassium manganate(VII), KMnO4.<br/>"
            "• <b>FA 2</b> is a solution prepared by dissolving 19.60 g dm<sup>-3</sup> of hydrated ammonium iron(II) sulfate (Mohr's salt), (NH4)2Fe(SO4)2.xH2O.<br/>"
            "• <b>FA 3</b> is 1.0 mol dm<sup>-3</sup> sulfuric acid, H2SO4.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Fill the burette with 0.0200 mol dm<sup>-3</sup> KMnO4 (FA 1). Note that readings should be taken at the upper meniscus or top edge due to the dark purple color.<br/>"
            "2. Pipette 25.0 cm<sup>3</sup> of FA 2 into a conical flask.<br/>"
            "3. Using a measuring cylinder, add 20 cm<sup>3</sup> of 1.0 mol dm<sup>-3</sup> H2SO4 (FA 3) to acidify the solution.<br/>"
            "4. Titrate with FA 1 until a permanent faint pale pink color persists for at least 30 seconds (no external indicator is required: KMnO4 is self-indicating).<br/>"
            "5. Record your readings and obtain concordant titres within 0.10 cm<sup>3</sup>."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your burette readings and titre volumes for the titration of FA 2 with FA 1 in the table below.",
                marks=5,
                lines_count=0,
                table_data=make_titration_table(styles),
                mark_scheme="Table formatted correctly, readings to 0.05 cm<sup>3</sup>, concordancy <= 0.10 cm<sup>3</sup>, accuracy marks [5]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Calculate your mean titre of FA 1.",
                marks=1,
                lines_count=2,
                mark_scheme="Mean titre correctly calculated to 2 decimal places (e.g. 25.00 cm<sup>3</sup>)."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the amount, in moles, of manganate(VII) ions, MnO4^-, present in your mean titre of FA 1.",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of MnO4^- = 0.0200 mol dm<sup>-3</sup> x (25.00 / 1000) = 5.00 x 10<sup>-4</sup> mol. [2]"
            ),
            PracticalSubQuestion(
                label="(d)",
                text="The ionic half-equations are:<br/>MnO4^- + 8H^+ + 5e^- -> Mn^2+ + 4H2O<br/>Fe^2+ -> Fe^3+ + e^-<br/>Write the overall balanced ionic equation, and deduce the amount, in moles, of Fe^2+ present in 25.0 cm<sup>3</sup> of FA 2.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Overall equation: MnO4^- + 5Fe^2+ + 8H^+ -> Mn^2+ + 5Fe^3+ + 4H2O [1]<br/>"
                    "Mole ratio is 1 MnO4^- : 5 Fe^2+.<br/>"
                    "Moles of Fe^2+ in 25.0 cm<sup>3</sup> = 5 x (5.00 x 10<sup>-4</sup>) = 2.50 x 10<sup>-3</sup> mol [2]"
                )
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Calculate the concentration of Fe^2+ in FA 2 in mol dm<sup>-3</sup>, and hence calculate the relative formula mass (Mr) of the Mohr's salt sample (which contains 19.60 g dm<sup>-3</sup> of the hydrated salt).",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Concentration of Fe^2+ = 2.50 x 10<sup>-3</sup> x (1000 / 25.0) = 0.100 mol dm<sup>-3</sup> [1]<br/>"
                    "Mr of Mohr's salt = Mass concentration / Molar concentration = 19.60 g dm<sup>-3</sup> / 0.100 mol dm<sup>-3</sup> = 196.0 g/mol (anhydrous) or 392.0 g/mol for hexahydrate [2]"
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="The formula of Mohr's salt is (NH4)2Fe(SO4)2.xH2O. Given that the relative formula mass of anhydrous (NH4)2Fe(SO4)2 is 284.0, calculate the value of x (the number of water of crystallization molecules). [Ar: H = 1.0, O = 16.0]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Mass of water per mole = Mr(total) - Mr(anhydrous) = 392.0 - 284.0 = 108.0 g [1]<br/>"
                    "x = 108.0 / 18.0 = 6.0 [1]<br/>"
                    "Therefore, x = 6 (Mohr's salt is a hexahydrate, (NH4)2Fe(SO4)2.6H2O) [1]"
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Explain why hydrochloric acid (HCl) cannot be used instead of sulfuric acid (H2SO4) to acidify the reaction mixture in this titration.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Potassium manganate(VII) is a powerful oxidizing agent that would oxidize chloride ions (Cl^-) in HCl to chlorine gas (Cl2): 2MnO4^- + 10Cl^- + 16H^+ -> 2Mn^2+ + 5Cl2 + 8H2O. [1]<br/>"
                    "This would consume extra KMnO4, leading to an artificially high titre volume and causing false calculated values for iron. Sulfuric acid contains sulfur in its maximum oxidation state (+6) and cannot be oxidized. [2]"
                )
            )
        ]
    )

    p2_q2 = PracticalQuestion(
        number=2,
        title="Iodine-Thiosulfate Titration: Determination of Copper in an Alloy",
        syllabus_ref="9701/34/M/J/23/Q1",
        total_marks=20,
        procedure_intro=(
            "<b>Chemicals and Solutions Provided:</b><br/>"
            "• <b>FA 4</b> is an aqueous solution of copper(II) sulfate, CuSO4, obtained by dissolving 3.50 g of a copper brass alloy in nitric acid and diluting to 250 cm<sup>3</sup>.<br/>"
            "• <b>FA 5</b> is 0.100 mol dm<sup>-3</sup> sodium thiosulfate, Na2S2O3.<br/>"
            "• <b>Aqueous potassium iodide</b>, KI (approx 0.5 mol dm<sup>-3</sup>).<br/>"
            "• <b>Starch indicator</b> solution.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Pipette 25.0 cm<sup>3</sup> of FA 4 into a conical flask.<br/>"
            "2. Using a measuring cylinder, add 15 cm<sup>3</sup> of aqueous potassium iodide. A thick brown precipitate/suspension of iodine and copper(I) iodide forms: 2Cu^2+ + 4I^- -> 2CuI(s) + I2(aq).<br/>"
            "3. Titrate the liberated iodine with 0.100 mol dm<sup>-3</sup> Na2S2O3 (FA 5) from the burette until the dark brown color fades to a pale straw-yellow.<br/>"
            "4. Add 1 cm<sup>3</sup> of starch indicator. The solution turns dark blue-black.<br/>"
            "5. Continue adding FA 5 dropwise with vigorous swirling until the blue-black color disappears, leaving a milky-white precipitate of CuI. Record the endpoint volume."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your titration results for the titration of the liberated iodine with FA 5 in the table below.",
                marks=5,
                lines_count=0,
                table_data=make_titration_table(styles),
                mark_scheme="Table formatted correctly, readings to 0.05 cm<sup>3</sup>, concordancy <= 0.10 cm<sup>3</sup>, accuracy marks [5]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Calculate your mean titre of FA 5.",
                marks=1,
                lines_count=2,
                mark_scheme="Mean titre calculated to 2 decimal places (e.g. 22.50 cm<sup>3</sup>)."
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the amount, in moles, of thiosulfate ions, S2O3^2-, present in your mean titre of FA 5.",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of S2O3^2- = 0.100 x (22.50 / 1000) = 2.25 x 10<sup>-3</sup> mol. [2]"
            ),
            PracticalSubQuestion(
                label="(d)",
                text="The titration reaction is: 2S2O3^2- + I2 -> S4O6^2- + 2I^-.<br/>Calculate the amount, in moles, of I2 liberated in the conical flask.",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of I2 = Moles of S2O3^2- / 2 = 2.25 x 10<sup>-3</sup> / 2 = 1.125 x 10<sup>-3</sup> mol. [2]"
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Given that 2 moles of Cu^2+ liberate 1 mole of I2 (2Cu^2+ + 4I^- -> 2CuI + I2), calculate the amount, in moles, of copper present in the 25.0 cm<sup>3</sup> sample of FA 4, and hence in the original 250 cm<sup>3</sup> flask.",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Moles of Cu^2+ in 25.0 cm<sup>3</sup> = 2 x Moles of I2 = 2 x 1.125 x 10<sup>-3</sup> = 2.25 x 10<sup>-3</sup> mol [1]<br/>"
                    "Total moles of Cu in 250 cm<sup>3</sup> = 2.25 x 10<sup>-3</sup> x 10 = 2.25 x 10<sup>-2</sup> mol (0.0225 mol) [2]"
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Calculate the mass of copper in the alloy sample, and determine the percentage by mass of copper in the alloy. [Ar: Cu = 63.5; Sample mass = 3.50 g]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Mass of copper = 0.0225 mol x 63.5 g/mol = 1.429 g [1]<br/>"
                    "% copper in alloy = (1.429 g / 3.50 g) x 100% = 40.8% [2]"
                )
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Why must the starch indicator NOT be added at the beginning of the titration when the iodine concentration is high?",
                marks=2,
                lines_count=3,
                mark_scheme="At high iodine concentrations, iodine binds irreversibly to the starch helical amylose coils, preventing rapid dissociation at the endpoint and leading to an inaccurate, delayed endpoint. Starch is added only when the straw-yellow color indicates most iodine has reacted. [2]"
            ),
            PracticalSubQuestion(
                label="(h)",
                text="State the function of adding potassium thiocyanate (KSCN) just before the endpoint in precision copper determinations.",
                marks=2,
                lines_count=3,
                mark_scheme="Copper(I) iodide (CuI) adsorbs iodine molecules onto its surface. Adding KSCN displaces adsorbed iodine (forming CuSCN precipitate), releasing all iodine into solution for complete titration with thiosulfate, giving a sharper and more accurate endpoint. [2]"
            )
        ]
    )

    p2_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Redox_Titrations.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, [p2_q1, p2_q2], include_qa_notes=False)

    # =========================================================================
    # 3. THERMOCHEMISTRY & CALORIMETRY (Cooling Curves)
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical 3: Thermochemistry & Calorimetry",
        subtitle="Enthalpy of Displacement with Cooling-Curve Extrapolation & Hess's Law Investigations",
        component_name="Paper 3 — Advanced Practical Skills (Physical Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p3_q1 = PracticalQuestion(
        number=1,
        title="Determination of the Enthalpy Change of Displacement of Copper by Zinc",
        syllabus_ref="9701/31/O/N/23/Q2",
        total_marks=22,
        procedure_intro=(
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 1</b> is 1.00 mol dm<sup>-3</sup> copper(II) sulfate, CuSO4.<br/>"
            "• <b>FA 2</b> is zinc powder, Zn.<br/>"
            "• Polystyrene cup supported in a 250 cm<sup>3</sup> glass beaker.<br/>"
            "• Thermometer (-10 °C to +110 °C, reading to 0.5 °C).<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Using a measuring cylinder, transfer exactly 50.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> CuSO4 (FA 1) into the polystyrene cup.<br/>"
            "2. Weigh 3.50 g of zinc powder (FA 2) in a weighing bottle.<br/>"
            "3. Place the thermometer in the cup, stir gently, and record the temperature every 30 seconds for 2.5 minutes.<br/>"
            "4. At exactly <b>t = 3.0 minutes</b>, add the zinc powder all at once. DO NOT record the temperature at 3.0 minutes. Stir continuously with the thermometer.<br/>"
            "5. Continue recording the temperature every 30 seconds from t = 3.5 minutes to t = 10.0 minutes."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your temperature readings at 30-second intervals in the table below.",
                marks=4,
                lines_count=0,
                table_data=make_thermometry_table(styles),
                mark_scheme="Table formatted correctly, time in minutes, temperature recorded to nearest 0.5 °C, all 14 readings recorded [4]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="On the grid provided, plot a graph of temperature (vertical axis) against time (horizontal axis). Draw two lines of best fit: one through the initial points (0 to 2.5 min) and one through the cooling points (4.0 to 10.0 min). Extrapolate both lines to t = 3.0 minutes to determine the theoretical maximum temperature change, ΔT.",
                marks=6,
                lines_count=2,
                figure_path=r"z:\tests n quizes63\books\psycology\new styl\figures\cooling_curve_graph_grid.png",
                figure_caption="Fig 1.1: Temperature vs Time cooling curve with linear extrapolation to mixing time (t = 3.0 min).",
                mark_scheme=(
                    "Axes correctly labeled with quantity and unit (Temperature / °C, Time / min) [1]<br/>"
                    "Scale chosen so plotted points occupy >= 50% of each axis [1]<br/>"
                    "All points plotted accurately within half a small square [1]<br/>"
                    "Line of best fit drawn for pre-mixing points (horizontal baseline) [1]<br/>"
                    "Line of best fit drawn for cooling points (linear descent) [1]<br/>"
                    "Correct extrapolation of both lines to t = 3.0 min and accurate reading of ΔT [1]"
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="State the value of ΔT obtained from your extrapolated graph.",
                marks=1,
                lines_count=2,
                mark_scheme="ΔT recorded to nearest 0.5 °C (e.g. ΔT = 18.5 °C)."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Calculate the heat energy, q, evolved during the reaction in the polystyrene cup. [Specific heat capacity of solution = 4.18 J g^-1 K^-1; Density of solution = 1.00 g cm^-3]",
                marks=2,
                lines_count=3,
                mark_scheme="Mass of solution m = 50.0 g. q = m x c x ΔT = 50.0 x 4.18 x 18.5 = 3,866.5 J = 3.867 kJ. [2]"
            ),
            PracticalSubQuestion(
                label="(e)",
                text="Calculate the amount, in moles, of CuSO4 used and the amount, in moles, of Zn used. State which reagent is in excess. [Ar: Zn = 65.4]",
                marks=3,
                lines_count=4,
                mark_scheme=(
                    "Moles of CuSO4 = 1.00 mol dm^-3 x (50.0 / 1000) = 0.0500 mol [1]<br/>"
                    "Moles of Zn = 3.50 g / 65.4 g/mol = 0.0535 mol [1]<br/>"
                    "0.0535 > 0.0500, therefore Zn is in excess and CuSO4 is the limiting reagent [1]"
                )
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Calculate the molar enthalpy change of displacement, ΔH, in kJ mol^-1. Include the correct sign and express your answer to three significant figures.",
                marks=2,
                lines_count=3,
                mark_scheme="ΔH = - (q / moles limiting) = - (3.867 kJ / 0.0500 mol) = - 77.3 kJ mol^-1. (Must include negative sign and correct 3 s.f.). [2]"
            ),
            PracticalSubQuestion(
                label="(g)",
                text="The thermometer used has an uncertainty of ±0.5 °C per reading. Calculate the percentage apparatus uncertainty in your value of ΔT.",
                marks=2,
                lines_count=3,
                mark_scheme="Two temperature readings taken, total uncertainty = 2 x 0.5 = 1.0 °C. % uncertainty = (1.0 / ΔT) x 100% = (1.0 / 18.5) x 100% = 5.41%. [2]"
            ),
            PracticalSubQuestion(
                label="(h)",
                text="Explain why extrapolating the cooling curve to the time of mixing (t = 3.0 min) gives a more accurate value for ΔT than simply recording the highest temperature reached on the thermometer.",
                marks=2,
                lines_count=3,
                mark_scheme="The reaction is not instantaneous and heat is continuously lost to the surroundings from the moment reaction begins. The maximum temperature reached on the thermometer is lower than the true theoretical temperature because cooling has already occurred. Extrapolating the cooling curve backwards compensates for heat lost during the initial reaction phase. [2]"
            )
        ]
    )

    p3_q2 = PracticalQuestion(
        number=2,
        title="Calorimetric Enthalpy of Neutralization: Strong Acid vs Strong Base",
        syllabus_ref="9701/33/O/N/23/Q2",
        total_marks=18,
        procedure_intro=(
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 3</b> is 2.00 mol dm<sup>-3</sup> hydrochloric acid, HCl.<br/>"
            "• <b>FA 4</b> is 2.00 mol dm<sup>-3</sup> sodium hydroxide, NaOH.<br/>"
            "• Two polystyrene cups with lids.<br/>"
            "• Measuring cylinder (50 cm<sup>3</sup>) and thermometer.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Measure 25.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> HCl (FA 3) and place into cup 1. Record its temperature T1.<br/>"
            "2. Measure 25.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> NaOH (FA 4) and place into cup 2. Record its temperature T2.<br/>"
            "3. Calculate the average initial temperature T_initial = (T1 + T2) / 2.<br/>"
            "4. Pour the NaOH quickly into the HCl cup, place the lid, stir with the thermometer, and record the highest temperature reached, T_max."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your temperature values T1, T2, T_initial, and T_max, and calculate the temperature rise ΔT.",
                marks=3,
                lines_count=4,
                mark_scheme="T1 and T2 recorded to 0.5 °C [1]; T_max recorded [1]; ΔT correctly calculated (e.g. T_initial = 21.0 °C, T_max = 34.5 °C, ΔT = 13.5 °C) [1]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Calculate the heat energy evolved, q, in Joules. [Total volume = 50.0 cm<sup>3</sup>; density = 1.00 g cm<sup>-3</sup>; c = 4.18 J g^-1 K^-1]",
                marks=2,
                lines_count=3,
                mark_scheme="q = m x c x ΔT = 50.0 x 4.18 x 13.5 = 2,821.5 J = 2.822 kJ. [2]"
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Calculate the amount, in moles, of water formed during this neutralization reaction: HCl + NaOH -> NaCl + H2O.",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of HCl = 2.00 x (25.0 / 1000) = 0.0500 mol. Moles of NaOH = 0.0500 mol. Moles of H2O formed = 0.0500 mol. [2]"
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Calculate the standard enthalpy change of neutralization, ΔH_neut, in kJ mol^-1. Include the sign and quote to 3 significant figures.",
                marks=2,
                lines_count=3,
                mark_scheme="ΔH_neut = - (2.822 kJ / 0.0500 mol) = - 56.4 kJ mol^-1. (Exothermic sign mandatory, 3 s.f.). [2]"
            ),
            PracticalSubQuestion(
                label="(e)",
                text="The literature value for ΔH_neut is -57.1 kJ mol^-1. Calculate the percentage difference between your experimental result and the literature value.",
                marks=2,
                lines_count=3,
                mark_scheme="% difference = (|56.4 - 57.1| / 57.1) x 100% = (0.7 / 57.1) x 100% = 1.23%. [2]"
            ),
            PracticalSubQuestion(
                label="(f)",
                text="State two modifications to the apparatus that would reduce heat loss and improve the accuracy of the result.",
                marks=2,
                lines_count=3,
                mark_scheme="1. Nest two polystyrene cups together (double-cupping) or place mineral wool insulation between cups. [1]<br/>2. Use a tight-fitting lid with a small hole for the thermometer to prevent convective heat loss and vapor escape. [1]"
            ),
            PracticalSubQuestion(
                label="(g)",
                text="Predict how the value of ΔH_neut would differ if 2.00 mol dm^-3 ethanoic acid (a weak acid) were used instead of hydrochloric acid. Explain your reasoning.",
                marks=3,
                lines_count=4,
                mark_scheme="The value of ΔH_neut would be less exothermic (less negative, ~ -54 kJ mol^-1). Ethanoic acid is only partially dissociated in aqueous solution. Energy must be absorbed from the surroundings to break covalent O-H bonds and fully dissociate the weak acid molecules into H^+ and ethanoate ions, reducing the net heat released during neutralization. [3]"
            ),
            PracticalSubQuestion(
                label="(h)",
                text="Suggest why using a glass beaker instead of a polystyrene cup produces a significantly larger error in calorimetric experiments.",
                marks=2,
                lines_count=3,
                mark_scheme="Glass has a much higher thermal conductivity than expanded polystyrene and a larger heat capacity, absorbing and dissipating significant heat to the air, causing a substantially lower recorded ΔT. [2]"
            )
        ]
    )

    p3_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Thermochemistry_Calorimetry.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, [p3_q1, p3_q2], include_qa_notes=False)

    # =========================================================================
    # 4. REACTION KINETICS (Gas Evolution & Disappearing Cross)
    # =========================================================================
    p4_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical 4: Reaction Kinetics",
        subtitle="Gas Syringe Volume Monitoring & Sodium Thiosulfate Disappearing Cross Rate Investigations",
        component_name="Paper 3 — Advanced Practical Skills (Physical Chemistry Suite)",
        duration="2 Hours",
        total_marks=40
    )

    p4_q1 = PracticalQuestion(
        number=1,
        title="Continuous Monitoring of Reaction Rate: Magnesium and Hydrochloric Acid",
        syllabus_ref="9701/35/M/J/23/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 1</b> is 1.00 mol dm<sup>-3</sup> hydrochloric acid, HCl.<br/>"
            "• Magnesium ribbon, Mg (cut into clean 5.0 cm strips, cleaned with emery paper).<br/>"
            "• Conical flask (100 cm<sup>3</sup>) fitted with a bung, delivery tube, and 100 cm<sup>3</sup> gas syringe.<br/>"
            "• Stopwatch.<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. Using a measuring cylinder, pour 25.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> HCl (FA 1) into the conical flask.<br/>"
            "2. Set up the gas syringe horizontally with the plunger set to 0.0 cm<sup>3</sup>.<br/>"
            "3. Add one 5.0 cm strip of magnesium ribbon to the flask, immediately insert the rubber bung, and start the stopwatch.<br/>"
            "4. Record the volume of hydrogen gas collected in the gas syringe every 10 seconds for 2 minutes."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Record your gas volume readings in the table below at 10-second intervals from t = 0 to t = 120 s.",
                marks=4,
                lines_count=0,
                table_data=Table([
                    [Paragraph("<b>Time / s</b>", styles['table_header']), Paragraph("0", styles['table_cell_center']), Paragraph("10", styles['table_cell_center']), Paragraph("20", styles['table_cell_center']), Paragraph("30", styles['table_cell_center']), Paragraph("40", styles['table_cell_center']), Paragraph("50", styles['table_cell_center']), Paragraph("60", styles['table_cell_center']), Paragraph("75", styles['table_cell_center']), Paragraph("90", styles['table_cell_center']), Paragraph("105", styles['table_cell_center']), Paragraph("120", styles['table_cell_center'])],
                    [Paragraph("<b>Vol / cm<sup>3</sup></b>", styles['table_header']), "0.0", "", "", "", "", "", "", "", "", "", ""]
                ], colWidths=[65, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38], style=[
                    ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
                    ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
                    ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ]),
                mark_scheme="Table formatted correctly, all readings recorded to 0.5 cm<sup>3</sup>, smooth progressive increase leveling off to constant volume [4]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="On the grid provided, plot a graph of volume of hydrogen gas (vertical axis) against time (horizontal axis). Draw a smooth curve of best fit through the points. Draw a tangent to the curve at t = 0 s and calculate the initial rate of reaction.",
                marks=6,
                lines_count=2,
                figure_path=r"z:\tests n quizes63\books\psycology\new styl\figures\kinetics_rate_graph_grid.png",
                figure_caption="Fig 1.2: Gas evolution curve with tangent at origin to calculate initial rate.",
                mark_scheme=(
                    "Axes labeled with quantity and unit (Volume of gas / cm<sup>3</sup>, Time / s) [1]<br/>"
                    "Appropriate linear scale covering >= 50% of grid [1]<br/>"
                    "All points plotted accurately within 0.5 small square [1]<br/>"
                    "Smooth curve of best fit drawn without kinks or double lines [1]<br/>"
                    "Tangent drawn accurately at t = 0 s [1]<br/>"
                    "Initial rate calculated from gradient: Gradient = ΔV / Δt with correct units (cm<sup>3</sup> s^-1) [1]"
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="State the value of the initial rate calculated from your tangent.",
                marks=1,
                lines_count=2,
                mark_scheme="Initial rate recorded with correct unit: ~2.00 cm<sup>3</sup> s^-1 (allow 1.80 to 2.20 cm<sup>3</sup> s^-1). [1]"
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Why does the rate of reaction decrease continuously as time progresses?",
                marks=2,
                lines_count=3,
                mark_scheme="As the reaction proceeds, reactant particles (Mg and H^+ ions) are consumed. The concentration of H^+ ions decreases, leading to fewer collisions per unit time between reactant particles, lowering collision frequency and reducing reaction rate. [2]"
            ),
            PracticalSubQuestion(
                label="(e)",
                text="State the maximum volume of hydrogen gas collected, and calculate the amount, in moles, of H2 produced. [Molar gas volume at r.t.p. = 24.0 dm<sup>3</sup> mol^-1]",
                marks=2,
                lines_count=3,
                mark_scheme="Max volume = 52.0 cm<sup>3</sup> = 0.0520 dm<sup>3</sup>. Moles of H2 = 0.0520 / 24.0 = 2.167 x 10<sup>-3</sup> mol. [2]"
            ),
            PracticalSubQuestion(
                label="(f)",
                text="Mg + 2HCl -> MgCl2 + H2. Calculate the mass of magnesium that reacted. [Ar: Mg = 24.3]",
                marks=2,
                lines_count=3,
                mark_scheme="Moles of Mg = Moles of H2 = 2.167 x 10<sup>-3</sup> mol. Mass of Mg = 2.167 x 10<sup>-3</sup> x 24.3 = 0.0527 g. [2]"
            ),
            PracticalSubQuestion(
                label="(g)",
                text="State one source of systematic error when inserting the bung and how the apparatus could be modified to eliminate this error.",
                marks=3,
                lines_count=4,
                mark_scheme="Gas escapes into the air between adding the magnesium strip and pushing the rubber bung into the flask neck [1]. Modification: Suspend the magnesium strip on a thread inside the flask clamped by the bung, or place the magnesium in a small test-tube inside the flask and invert/tilt to start the reaction after sealing [2]."
            )
        ]
    )

    p4_q2 = PracticalQuestion(
        number=2,
        title="Disappearing Cross Kinetics: Effect of Concentration on Sodium Thiosulfate Rate",
        syllabus_ref="9701/31/M/J/22/Q2",
        total_marks=20,
        procedure_intro=(
            "<b>Chemicals and Apparatus Provided:</b><br/>"
            "• <b>FA 2</b> is 0.100 mol dm<sup>-3</sup> sodium thiosulfate, Na2S2O3.<br/>"
            "• <b>FA 3</b> is 1.00 mol dm<sup>-3</sup> hydrochloric acid, HCl.<br/>"
            "• Conical flask (100 cm<sup>3</sup>) placed over a white tile marked with a black cross (X).<br/>"
            "• Distilled water and stopwatch.<br/><br/>"
            "<b>Reaction Equation:</b><br/>"
            "Na2S2O3(aq) + 2HCl(aq) -> 2NaCl(aq) + S(s) + SO2(g) + H2O(l)<br/><br/>"
            "<b>Experimental Procedure:</b><br/>"
            "1. In 5 separate experiments, measure the volumes of FA 2 and distilled water indicated in the table into the conical flask placed over the cross.<br/>"
            "2. Add 5.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> HCl (FA 3), swirl once, and start the stopwatch.<br/>"
            "3. Look vertically down through the flask from above.<br/>"
            "4. Stop the watch the instant the black cross is completely obscured by the yellow precipitate of sulfur.<br/>"
            "5. Record the reaction time, t, to the nearest second, and calculate 1/t (which is directly proportional to rate)."
        ),
        subquestions=[
            PracticalSubQuestion(
                label="(a)",
                text="Complete the experimental table below by recording time, t, and calculating 1/t (to 3 significant figures).",
                marks=5,
                lines_count=0,
                table_data=Table([
                    [Paragraph("<b>Expt</b>", styles['table_header']), Paragraph("<b>Vol Na2S2O3 / cm<sup>3</sup></b>", styles['table_header']), Paragraph("<b>Vol Water / cm<sup>3</sup></b>", styles['table_header']), Paragraph("<b>[Na2S2O3] / mol dm<sup>-3</sup></b>", styles['table_header']), Paragraph("<b>Time, t / s</b>", styles['table_header']), Paragraph("<b>Rate (1/t) / s<sup>-1</sup></b>", styles['table_header'])],
                    [Paragraph("1", styles['table_cell_center']), "50.0", "0.0", "0.100", "", ""],
                    [Paragraph("2", styles['table_cell_center']), "40.0", "10.0", "0.080", "", ""],
                    [Paragraph("3", styles['table_cell_center']), "30.0", "20.0", "0.060", "", ""],
                    [Paragraph("4", styles['table_cell_center']), "20.0", "30.0", "0.040", "", ""],
                    [Paragraph("5", styles['table_cell_center']), "10.0", "40.0", "0.020", "", ""]
                ], colWidths=[40, 95, 85, 95, 85, 90], style=[
                    ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
                    ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
                    ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('TOPPADDING', (0, 0), (-1, -1), 4.5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
                ]),
                mark_scheme="All 5 experiments completed, times recorded in integer seconds, 1/t calculated correctly to 3 s.f., times increase as concentration decreases [5]."
            ),
            PracticalSubQuestion(
                label="(b)",
                text="Plot a graph of Rate (1/t, vertical axis) against volume of Na2S2O3 (horizontal axis). Draw the line of best fit.",
                marks=5,
                lines_count=2,
                mark_scheme=(
                    "Axes labeled with quantity and unit (1/t / s^-1, Volume of Na2S2O3 / cm<sup>3</sup>) [1]<br/>"
                    "Linear scales using >= 50% of grid [1]<br/>"
                    "Points plotted accurately within 0.5 square [1]<br/>"
                    "Straight line of best fit drawn passing through the origin (0,0) [2]"
                )
            ),
            PracticalSubQuestion(
                label="(c)",
                text="Using your graph, deduce the order of reaction with respect to sodium thiosulfate. Explain your deduction.",
                marks=3,
                lines_count=4,
                mark_scheme="The order of reaction is 1 (first order) [1]. The graph of rate (1/t) against concentration (volume) is a straight line passing through the origin (0,0), demonstrating that rate is directly proportional to concentration: Rate proportional to [Na2S2O3]^1 [2]."
            ),
            PracticalSubQuestion(
                label="(d)",
                text="Explain why the total volume in the conical flask was kept constant at 55.0 cm<sup>3</sup> in all 5 experiments.",
                marks=2,
                lines_count=3,
                mark_scheme="To ensure the volume of sodium thiosulfate used is directly proportional to its concentration in the reaction mixture, and to keep the depth of liquid in the flask constant so that the same mass of sulfur precipitate is required to obscure the cross each time. [2]"
            ),
            PracticalSubQuestion(
                label="(e)",
                text="State one toxic gas produced in this reaction and the safety precaution required when disposing of the mixture.",
                marks=3,
                lines_count=4,
                mark_scheme="Toxic gas: Sulfur dioxide (SO2) [1]. Safety precaution: Carry out in a well-ventilated laboratory/fume cupboard; immediately pour the reaction mixture into a sodium carbonate / sodium hydrogencarbonate stop bath to neutralize SO2 and prevent it escaping into the room [2]."
            ),
            PracticalSubQuestion(
                label="(f)",
                text="State the main human error in determining the endpoint in this investigation and suggest an instrument that would eliminate this subjectivity.",
                marks=2,
                lines_count=3,
                mark_scheme="Human judgment of the exact moment the cross disappears is subjective and varies between observers [1]. Instrumental replacement: A colorimeter or light sensor / datalogger connected to a computer to measure transmitted light intensity objectively [1]."
            )
        ]
    )

    p4_pdf = os.path.join(base_dest, "Urwah_Chem_Paper3_Practical_Reaction_Kinetics.pdf")
    build_paper3_pdf(p4_pdf, p4_cfg, [p4_q1, p4_q2], include_qa_notes=False)

    print("=== Physical Chemistry Practical Suite Complete (4 Papers) ===")

if __name__ == "__main__":
    build_all_physical_practicals()
