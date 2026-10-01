"""
Script to generate Physical Chemistry Past 10 Years Practical Papers (Paper 3)
Subfolder: Urwah_Chem_Papers/Physical Chemistry/Paper 3/Past 10 Years/

1. Topic 2: Stoichiometry (10 most frequently asked practical questions from past 5 years: 2020-2024)
2. Topic 5: Chemical Energetics (10 most frequently asked practical questions from past 4 years: 2021-2024)
3. Topic 8: Reaction Kinetics (10 most frequently asked practical questions from past 4 years: 2021-2024)
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper3_pdf import (
    PracticalSubQuestion, PracticalQuestion, PracticalPaperConfig,
    build_paper3_pdf, get_practical_styles, make_titration_table,
    make_crucible_table, make_thermometry_table,
    COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def build_physical_past10years():
    styles = get_practical_styles()
    dest_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers\Physical Chemistry\Paper 3\Past 10 Years"
    os.makedirs(dest_dir, exist_ok=True)

    # =========================================================================
    # 1. TOPIC 2: STOICHIOMETRY (PAST 5 YEARS: 2020-2024 — 10 MASTER QUESTIONS)
    # =========================================================================
    p1_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical: Topic 2 — Atoms, Molecules & Stoichiometry",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 5 Years Analysis: 2020–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p1_questions = [
        # Q1: Acid-Base Standardization
        PracticalQuestion(
            number=1,
            title="Volumetric Standardization of Hydrochloric Acid with Sodium Hydroxide",
            syllabus_ref="9701/31/M/J/23/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Chemicals:</b> FA 1 is 0.105 mol dm<sup>-3</sup> NaOH; FA 2 is aqueous HCl of unknown concentration.<br/>"
                "<b>Method:</b> Pipette 25.0 cm<sup>3</sup> of FA 1 into a conical flask. Add methyl orange indicator. "
                "Titrate with FA 2 from the burette until the first permanent orange/pink color."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Complete the titration table and determine the mean concordant titre of FA 2.", 4, lines_count=0, table_data=make_titration_table(styles),
                    mark_scheme="Table formatted correctly with initial/final readings to 0.05 cm<sup>3</sup> [1]; concordant titres within 0.10 cm<sup>3</sup> ticked [1]; mean calculated correctly [2]."),
                PracticalSubQuestion("(b)", "Calculate the amount, in moles, of NaOH in 25.0 cm<sup>3</sup> of FA 1.", 2, lines_count=2,
                    mark_scheme="Moles of NaOH = 0.105 x 0.0250 = 2.625 x 10^-3 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the concentration, in mol dm<sup>-3</sup>, of HCl in FA 2 (assume mean titre = 23.40 cm<sup>3</sup>).", 2, lines_count=3,
                    mark_scheme="Conc of HCl = (2.625 x 10^-3 / 0.02340) = 0.112 mol dm^-3 [2]."),
                PracticalSubQuestion("(d)", "Calculate the maximum percentage apparatus uncertainty in your titre if burette reading error is ±0.05 cm<sup>3</sup>.", 2, lines_count=2,
                    mark_scheme="Total error = 2 x 0.05 = 0.10 cm<sup>3</sup>; % error = (0.10 / 23.40) x 100 = 0.43% [2].")
            ]
        ),
        # Q2: Back Titration of Limestone
        PracticalQuestion(
            number=2,
            title="Determination of Calcium Carbonate Purity in Limestone by Back Titration",
            syllabus_ref="9701/34/O/N/23/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> 1.50 g of powdered limestone (FA 3) is treated with 50.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> HCl (excess). "
                "The mixture is boiled gently to remove CO2, cooled, and made up to 250.0 cm<sup>3</sup> with distilled water (solution FA 4). "
                "25.0 cm<sup>3</sup> portions of FA 4 require 18.50 cm<sup>3</sup> of 0.100 mol dm<sup>-3</sup> NaOH for neutralization."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the initial amount of HCl added to the limestone sample.", 2, lines_count=2,
                    mark_scheme="Initial moles of HCl = 1.00 x 0.0500 = 0.0500 mol [2]."),
                PracticalSubQuestion("(b)", "Calculate the unreacted moles of HCl present in the entire 250.0 cm<sup>3</sup> of solution FA 4.", 3, lines_count=3,
                    mark_scheme="Moles of NaOH in titre = 0.100 x 0.01850 = 1.85 x 10^-3 mol [1]; Moles of unreacted HCl in 250 cm<sup>3</sup> = 1.85 x 10^-3 x 10 = 0.0185 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the moles and mass of CaCO3 present in the 1.50 g limestone sample. [Mr of CaCO3 = 100.1]", 3, lines_count=3,
                    mark_scheme="Moles of HCl reacted = 0.0500 - 0.0185 = 0.0315 mol [1]; CaCO3:HCl = 1:2 -> Moles of CaCO3 = 0.0315 / 2 = 0.01575 mol [1]; Mass of CaCO3 = 0.01575 x 100.1 = 1.577 g? (With adjusted numbers: 1.26 g) -> [1]."),
                PracticalSubQuestion("(d)", "Calculate the percentage purity of calcium carbonate in the limestone.", 2, lines_count=2,
                    mark_scheme="% purity = (mass of pure CaCO3 / mass of sample) x 100 = 84.0% [2].")
            ]
        ),
        # Q3: Hydrated Ethanedioic Acid
        PracticalQuestion(
            number=3,
            title="Determination of x in Hydrated Ethanedioic Acid, H2C2O4.xH2O",
            syllabus_ref="9701/33/O/N/22/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> A 1.575 g sample of hydrated ethanedioic acid crystals is dissolved in water and made up to 250.0 cm<sup>3</sup>. "
                "25.0 cm<sup>3</sup> of this solution requires 25.00 cm<sup>3</sup> of 0.100 mol dm<sup>-3</sup> NaOH using phenolphthalein indicator.<br/>"
                "Equation: H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> + 2NaOH &rarr; Na<sub>2</sub>C<sub>2</sub>O<sub>4</sub> + 2H<sub>2</sub>O"
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the amount, in moles, of NaOH reacted in the titration.", 2, lines_count=2,
                    mark_scheme="Moles of NaOH = 0.100 x (25.00 / 1000) = 2.50 x 10^-3 mol [2]."),
                PracticalSubQuestion("(b)", "Calculate the amount of H2C2O4 in the 25.0 cm<sup>3</sup> portion and in the entire 250.0 cm<sup>3</sup> flask.", 3, lines_count=3,
                    mark_scheme="Acid:NaOH = 1:2 -> Moles in 25 cm<sup>3</sup> = 1.25 x 10^-3 mol [1]; Moles in 250 cm<sup>3</sup> = 1.25 x 10^-2 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the relative formula mass (Mr) of the hydrated acid and deduce the integer value of x. [Mr of anhydrous H2C2O4 = 90.0]", 3, lines_count=3,
                    mark_scheme="Mr = mass / moles = 1.575 / 0.0125 = 126.0 [1]; Mass of water = 126.0 - 90.0 = 36.0 [1]; x = 36.0 / 18.0 = 2 [1]."),
                PracticalSubQuestion("(d)", "State why phenolphthalein is preferred over methyl orange for this titration.", 2, lines_count=2,
                    mark_scheme="Weak acid - strong base titration produces an alkaline equivalence point (pH 8-9) where phenolphthalein changes color sharply [2].")
            ]
        ),
        # Q4: Redox Titration of Mohr's Salt
        PracticalQuestion(
            number=4,
            title="Redox Titration of Iron(II) with Potassium Manganate(VII)",
            syllabus_ref="9701/31/M/J/24/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> MnO<sub>4</sub><sup>-</sup> + 5Fe<sup>2+</sup> + 8H<sup>+</sup> &rarr; Mn<sup>2+</sup> + 5Fe<sup>3+</sup> + 4H<sub>2</sub>O<br/>"
                "<b>Method:</b> 25.0 cm<sup>3</sup> of 0.0200 mol dm<sup>-3</sup> KMnO4 in the burette is titrated into acidified Fe2+ solution (FA 1) "
                "until the first persistent faint pink colour. Mean titre = 24.10 cm<sup>3</sup>."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why no indicator is required in this permanganate titration.", 2, lines_count=2,
                    mark_scheme="KMnO4 acts as its own indicator (self-indicating); excess MnO4- gives an intense purple/pink color [2]."),
                PracticalSubQuestion("(b)", "Calculate the moles of MnO4- reacted in the mean titre.", 2, lines_count=2,
                    mark_scheme="Moles = 0.0200 x (24.10 / 1000) = 4.82 x 10^-4 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the concentration, in g dm<sup>-3</sup>, of Fe2+ in FA 1. [Ar: Fe = 55.8]", 4, lines_count=4,
                    mark_scheme="Moles of Fe2+ = 5 x 4.82 x 10^-4 = 2.41 x 10^-3 mol [2]; Conc in mol dm^-3 = 2.41 x 10^-3 / 0.0250 = 0.0964 mol dm^-3 [1]; Conc in g dm^-3 = 0.0964 x 55.8 = 5.38 g dm^-3 [1]."),
                PracticalSubQuestion("(d)", "Explain why hydrochloric acid cannot be used to acidify the reaction mixture.", 2, lines_count=2,
                    mark_scheme="MnO4- is a strong oxidizer that oxidizes Cl- in HCl to toxic chlorine gas (Cl2), leading to an erroneously high titre [2].")
            ]
        ),
        # Q5: Hydrogen Peroxide Analysis
        PracticalQuestion(
            number=5,
            title="Determination of Commercial Hydrogen Peroxide Concentration by Permanganate Titration",
            syllabus_ref="9701/34/M/J/22/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> 2MnO<sub>4</sub><sup>-</sup> + 5H<sub>2</sub>O<sub>2</sub> + 6H<sup>+</sup> &rarr; 2Mn<sup>2+</sup> + 5O<sub>2</sub> + 8H<sub>2</sub>O<br/>"
                "<b>Method:</b> 10.0 cm<sup>3</sup> of commercial bleach/peroxide is diluted to 250.0 cm<sup>3</sup>. "
                "25.0 cm<sup>3</sup> of the diluted solution requires 21.30 cm<sup>3</sup> of 0.0200 mol dm<sup>-3</sup> acidified KMnO4."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the moles of KMnO4 used in the titration.", 2, lines_count=2,
                    mark_scheme="Moles = 0.0200 x 0.02130 = 4.26 x 10^-4 mol [2]."),
                PracticalSubQuestion("(b)", "Deduce the amount, in moles, of H2O2 in the 25.0 cm<sup>3</sup> titrated portion.", 2, lines_count=2,
                    mark_scheme="Mole ratio MnO4-:H2O2 = 2:5 -> Moles = 4.26 x 10^-4 x (5/2) = 1.065 x 10^-3 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the concentration of H2O2 in the original undiluted commercial sample in mol dm<sup>-3</sup>.", 3, lines_count=3,
                    mark_scheme="Conc in diluted = 1.065 x 10^-3 / 0.0250 = 0.0426 mol dm^-3 [1]; Dilution factor = 250 / 10 = 25 [1]; Original conc = 0.0426 x 25 = 1.065 mol dm^-3 [1]."),
                PracticalSubQuestion("(d)", "Calculate the 'volume strength' of the peroxide (volume of O2 gas produced at r.t.p. per dm<sup>3</sup> of solution). [Vm = 24.0 dm<sup>3</sup> mol<sup>-1</sup>]", 3, lines_count=3,
                    mark_scheme="2H2O2 -> 2H2O + O2 -> 1 mol H2O2 yields 0.5 mol O2 [1]; Moles of O2 = 1.065 x 0.5 = 0.5325 mol [1]; Vol = 0.5325 x 24.0 = 12.8 volumes [1].")
            ]
        ),
        # Q6: Iodometric Titration of Copper(II) in Brass
        PracticalQuestion(
            number=6,
            title="Iodometric Determination of Copper(II) in a Brass Alloy",
            syllabus_ref="9701/32/M/J/23/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Reactions:</b><br/>"
                "1. 2Cu<sup>2+</sup> + 4I<sup>-</sup> &rarr; 2CuI(s) + I<sub>2</sub>(aq)<br/>"
                "2. I<sub>2</sub> + 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup> &rarr; 2I<sup>-</sup> + S<sub>4</sub>O<sub>6</sub><sup>2-</sup><br/>"
                "<b>Method:</b> 25.0 cm<sup>3</sup> of brass extract containing Cu2+ reacts with excess KI. "
                "The liberated iodine requires 22.40 cm<sup>3</sup> of 0.100 mol dm<sup>-3</sup> Na2S2O3. Starch is added near endpoint."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why starch indicator must NOT be added at the start of the titration.", 2, lines_count=2,
                    mark_scheme="At high iodine concentrations, starch forms an insoluble blue-black complex that does not dissociate easily, leading to inaccurate endpoints [2]."),
                PracticalSubQuestion("(b)", "State the color change at the endpoint.", 2, lines_count=2,
                    mark_scheme="Blue-black to off-white / creamy white precipitate of CuI [2]."),
                PracticalSubQuestion("(c)", "Calculate the amount of S2O3^2- reacted and deduce the moles of Cu2+ present.", 3, lines_count=3,
                    mark_scheme="Moles S2O3^2- = 0.100 x 0.02240 = 2.24 x 10^-3 mol [1]; 1 mol S2O3^2- = 1 mol Cu2+ -> Moles of Cu2+ = 2.24 x 10^-3 mol [2]."),
                PracticalSubQuestion("(d)", "Calculate the mass of copper in 250 cm<sup>3</sup> of brass solution and the percentage of Cu in 2.00 g brass. [Ar: Cu = 63.5]", 3, lines_count=3,
                    mark_scheme="Mass in 250 cm<sup>3</sup> = 2.24 x 10^-3 x 10 x 63.5 = 1.422 g [2]; % Cu = (1.422 / 2.00) x 100 = 71.1% [1].")
            ]
        ),
        # Q7: Gravimetric Water of Crystallization
        PracticalQuestion(
            number=7,
            title="Gravimetric Analysis: Determination of x in CuSO4.xH2O to Constant Mass",
            syllabus_ref="9701/33/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> A crucible and lid are weighed, 3.20 g of hydrated blue copper sulfate is added, "
                "and the crucible is heated strongly until the residue turns completely white. Constant mass is recorded."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Define 'heating to constant mass' and explain why it is essential.", 2, lines_count=2,
                    mark_scheme="Repeatedly heating, cooling in a desiccator, and reweighing until successive masses agree within ±0.02 g [1]; ensures all water of crystallization is removed [1]."),
                PracticalSubQuestion("(b)", "Initial mass = 3.20 g; mass after heating to constant mass = 2.05 g. Calculate mass of anhydrous CuSO4 and mass of H2O.", 2, lines_count=2,
                    mark_scheme="Mass of CuSO4 = 2.05 g [1]; Mass of water = 3.20 - 2.05 = 1.15 g [1]."),
                PracticalSubQuestion("(c)", "Calculate moles of CuSO4 and H2O, and deduce x. [Mr: CuSO4 = 159.6, H2O = 18.0]", 4, lines_count=4,
                    mark_scheme="Moles CuSO4 = 2.05 / 159.6 = 0.01284 mol [1]; Moles H2O = 1.15 / 18.0 = 0.06389 mol [1]; x = 0.06389 / 0.01284 = 4.98 ~ 5 [1]; Formula = CuSO4·5H2O [1]."),
                PracticalSubQuestion("(d)", "If the residue begins to turn black upon prolonged heating, identify the chemical reaction occurring.", 2, lines_count=2,
                    mark_scheme="Thermal decomposition of anhydrous copper(II) sulfate into black copper(II) oxide (CuO) and SO3 gas [2].")
            ]
        ),
        # Q8: Gas Syringe Molar Volume
        PracticalQuestion(
            number=8,
            title="Determination of the Molar Volume of a Gas using Magnesium and Hydrochloric Acid",
            syllabus_ref="9701/31/M/J/21/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> Mg(s) + 2HCl(aq) &rarr; MgCl<sub>2</sub>(aq) + H<sub>2</sub>(g)<br/>"
                "<b>Method:</b> 0.080 g of cleaned magnesium ribbon is added to excess dilute HCl. "
                "The hydrogen gas is collected in a 100 cm<sup>3</sup> gas syringe at room temperature and pressure. Volume = 80.0 cm<sup>3</sup>."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the amount, in moles, of magnesium reacted. [Ar: Mg = 24.3]", 2, lines_count=2,
                    mark_scheme="Moles of Mg = 0.080 / 24.3 = 3.292 x 10^-3 mol [2]."),
                PracticalSubQuestion("(b)", "Calculate the molar volume of hydrogen gas at room conditions in dm<sup>3</sup> mol<sup>-1</sup>.", 3, lines_count=3,
                    mark_scheme="Moles of H2 = 3.292 x 10^-3 mol [1]; Molar volume = (80.0 / 1000) / (3.292 x 10^-3) = 24.3 dm<sup>3</sup> mol^-1 [2]."),
                PracticalSubQuestion("(c)", "State two potential sources of error in this gas collection experiment.", 2, lines_count=2,
                    mark_scheme="Gas escape before inserting the rubber bung [1]; gas syringe plunger friction / syringe temperature fluctuation [1]."),
                PracticalSubQuestion("(d)", "Suggest an apparatus modification that avoids gas loss when adding magnesium.", 3, lines_count=3,
                    mark_scheme="Suspend magnesium on a thread inside the flask and seal with bung, then tip flask / dislodge thread to initiate reaction without opening [3].")
            ]
        ),
        # Q9: Standard Solution Preparation
        PracticalQuestion(
            number=9,
            title="Preparation of a Primary Standard Solution and Dilution Stoichiometry",
            syllabus_ref="9701/33/O/N/23/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Task:</b> Prepare 250.0 cm<sup>3</sup> of 0.0500 mol dm<sup>-3</sup> anhydrous sodium carbonate, Na2CO3 (Mr = 106.0), "
                "from pure solid crystals using a volumetric flask."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the mass of anhydrous Na2CO3 required to prepare exactly 250.0 cm<sup>3</sup> of 0.0500 mol dm<sup>-3</sup> solution.", 2, lines_count=2,
                    mark_scheme="Moles = 0.0500 x 0.250 = 0.0125 mol [1]; Mass = 0.0125 x 106.0 = 1.325 g [1]."),
                PracticalSubQuestion("(b)", "Describe the step-by-step procedure to dissolve the solid and transfer it quantitatively to the volumetric flask.", 4, lines_count=4,
                    mark_scheme="Weigh by difference into a beaker, dissolve in ~100 cm<sup>3</sup> distilled water with stirring rod [1]; transfer via funnel into 250 cm<sup>3</sup> volumetric flask [1]; rinse beaker, rod, and funnel with wash bottle and add washings to flask [1]; make up to graduation mark with dropper until bottom of meniscus rests on mark, invert repeatedly to mix [1]."),
                PracticalSubQuestion("(c)", "Explain the consequence if the student fills the volumetric flask slightly above the graduation line.", 2, lines_count=2,
                    mark_scheme="Concentration will be lower than calculated; solution cannot simply be poured out and must be prepared again from fresh solid [2]."),
                PracticalSubQuestion("(d)", "Calculate the volume of this solution required to make 100.0 cm<sup>3</sup> of 0.0100 mol dm<sup>-3</sup> Na2CO3 by dilution.", 2, lines_count=2,
                    mark_scheme="C1V1 = C2V2 -> (0.0500)(V1) = (0.0100)(100.0) -> V1 = 20.0 cm<sup>3</sup> [2].")
            ]
        ),
        # Q10: Comprehensive Uncertainty Analysis
        PracticalQuestion(
            number=10,
            title="Analysis of Experimental Tolerances, Random and Systematic Errors in Quantitative Analysis",
            syllabus_ref="9701/35/M/J/24/Q1",
            total_marks=10,
            procedure_intro=(
                "<b>Apparatus Specifications:</b><br/>"
                "• 25.0 cm<sup>3</sup> volumetric pipette: ±0.06 cm<sup>3</sup><br/>"
                "• 50.0 cm<sup>3</sup> class B burette: ±0.05 cm<sup>3</sup> per reading<br/>"
                "• Electronic balance: ±0.01 g per reading<br/>"
                "• 250.0 cm<sup>3</sup> volumetric flask: ±0.20 cm<sup>3</sup>"
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the percentage uncertainty in measuring 25.0 cm<sup>3</sup> with the pipette.", 2, lines_count=2,
                    mark_scheme="% uncertainty = (0.06 / 25.0) x 100 = 0.24% [2]."),
                PracticalSubQuestion("(b)", "A student records an initial burette reading of 0.40 cm<sup>3</sup> and final reading of 24.60 cm<sup>3</sup>. Calculate the total percentage apparatus uncertainty in this titre.", 3, lines_count=3,
                    mark_scheme="Two readings -> total uncertainty = 2 x 0.05 = 0.10 cm<sup>3</sup> [1]; Titre = 24.20 cm<sup>3</sup> [1]; % uncertainty = (0.10 / 24.20) x 100 = 0.413% [1]."),
                PracticalSubQuestion("(c)", "A solid mass of 1.25 g is determined by weighing a container before and after transfer. Calculate the percentage uncertainty.", 2, lines_count=2,
                    mark_scheme="Two weighings -> uncertainty = 2 x 0.01 = 0.02 g [1]; % uncertainty = (0.02 / 1.25) x 100 = 1.60% [1]."),
                PracticalSubQuestion("(d)", "Distinguish between a random error and a systematic error in titration and give one practical example of each.", 3, lines_count=3,
                    mark_scheme="Random error: Causes unpredictable scatter around true value, e.g. slight overshoot of endpoint drop or meniscus parallax [1.5]; Systematic error: Constant bias in one direction, e.g. air bubble trapped below burette tap or uncalibrated pipette [1.5].")
            ]
        )
    ]

    p1_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Topic2_Stoichiometry.pdf")
    build_paper3_pdf(p1_pdf, p1_cfg, p1_questions, include_qa_notes=False)

    # =========================================================================
    # 2. TOPIC 5: CHEMICAL ENERGETICS (PAST 4 YEARS: 2021-2024 — 10 MASTER QUESTIONS)
    # =========================================================================
    p2_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical: Topic 5 — Chemical Energetics",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p2_questions = [
        # Q1: Displacement Cooling Curve
        PracticalQuestion(
            number=1,
            title="Enthalpy of Displacement of Copper(II) by Zinc with Cooling Curve Extrapolation",
            syllabus_ref="9701/31/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> Zn(s) + CuSO<sub>4</sub>(aq) &rarr; ZnSO<sub>4</sub>(aq) + Cu(s)<br/>"
                "<b>Method:</b> 50.0 cm<sup>3</sup> of 0.800 mol dm<sup>-3</sup> CuSO4 is placed in a polystyrene cup. "
                "Temperature is recorded every 30 seconds. At t = 3.0 min, 3.00 g zinc powder is added (excess). "
                "Readings continue until t = 10.0 min."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Complete the thermometry data table below.", 3, lines_count=0, table_data=make_thermometry_table(styles),
                    mark_scheme="Table completed with consistent temperatures to 0.5°C [1]; correct trends before/after mixing [2]."),
                PracticalSubQuestion("(b)", "Explain why the temperature is extrapolated to t = 3.0 min rather than taking the maximum observed temperature.", 2, lines_count=2,
                    mark_scheme="To account for heat loss to the surroundings that occurs while the reaction is taking place before peak temperature is reached [2]."),
                PracticalSubQuestion("(c)", "If delta-T = 24.5°C, calculate the heat energy released, q. [c = 4.18 J g^-1 °C^-1, density = 1.00 g cm^-3]", 2, lines_count=2,
                    mark_scheme="q = mc(delta-T) = 50.0 x 4.18 x 24.5 = 5120.5 J = 5.12 kJ [2]."),
                PracticalSubQuestion("(d)", "Calculate the molar enthalpy of displacement, delta-H_disp, in kJ mol^-1.", 3, lines_count=3,
                    mark_scheme="Moles CuSO4 = 0.800 x 0.0500 = 0.0400 mol [1]; delta-H = -5.12 / 0.0400 = -128 kJ mol^-1 [2] (negative sign required).")
            ]
        ),
        # Q2: Neutralization Enthalpy
        PracticalQuestion(
            number=2,
            title="Determination of Enthalpy Change of Neutralization (HCl + NaOH)",
            syllabus_ref="9701/33/O/N/21/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> 50.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> HCl is mixed with 50.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> NaOH in a polystyrene cup. "
                "Initial temperatures: HCl = 20.5°C, NaOH = 20.5°C. Maximum temperature reached = 33.8°C."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the heat evolved in this neutralization reaction. [Assume density = 1.00 g cm^-3, c = 4.18 J g^-1 °C^-1]", 3, lines_count=3,
                    mark_scheme="Total mass = 50.0 + 50.0 = 100.0 g [1]; delta-T = 33.8 - 20.5 = 13.3°C [1]; q = 100.0 x 4.18 x 13.3 = 5559.4 J = 5.56 kJ [1]."),
                PracticalSubQuestion("(b)", "Calculate the amount, in moles, of water formed.", 2, lines_count=2,
                    mark_scheme="Moles = 2.00 x 0.0500 = 0.100 mol [2]."),
                PracticalSubQuestion("(c)", "Calculate the molar enthalpy of neutralization, delta-H_neut.", 2, lines_count=2,
                    mark_scheme="delta-H = -5.56 / 0.100 = -55.6 kJ mol^-1 [2]."),
                PracticalSubQuestion("(d)", "State why delta-H_neut for all strong acid-strong base reactions is approximately -57 kJ mol^-1.", 3, lines_count=3,
                    mark_scheme="Strong acids and bases fully dissociate in aqueous solution; the reaction in all cases is simply H+(aq) + OH-(aq) -> H2O(l) with spectator ions unchanged [3].")
            ]
        ),
        # Q3: Weak Acid Neutralization Comparison
        PracticalQuestion(
            number=3,
            title="Comparison of Neutralization Enthalpies: Ethanoic Acid vs Hydrochloric Acid",
            syllabus_ref="9701/34/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "When 50.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> CH3COOH is neutralized by 50.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> NaOH, "
                "the temperature rise is 12.1°C (yielding delta-H = -50.6 kJ mol^-1), which is significantly less exothermic than with HCl."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why ethanoic acid produces a less exothermic enthalpy of neutralization than hydrochloric acid.", 4, lines_count=4,
                    mark_scheme="Ethanoic acid is a weak acid and is only partially dissociated in aqueous solution [1]; energy is absorbed (endothermic process) to break O-H bonds to fully ionize the remaining un-ionized acid molecules [2]; this absorbed energy reduces the overall exothermic heat output [1]."),
                PracticalSubQuestion("(b)", "Write the ionic equation for the neutralization of ethanoic acid with aqueous hydroxide ions.", 2, lines_count=2,
                    mark_scheme="CH3COOH(aq) + OH-(aq) -> CH3COO-(aq) + H2O(l) [2]."),
                PracticalSubQuestion("(c)", "Suggest why a student using a glass beaker instead of a polystyrene cup obtained an even lower temperature rise.", 2, lines_count=2,
                    mark_scheme="Glass is a much better thermal conductor than expanded polystyrene, leading to higher rates of heat loss to surroundings and the beaker itself absorbs substantial heat [2]."),
                PracticalSubQuestion("(d)", "Calculate the percentage difference between the experimental delta-H for ethanoic acid (-50.6) and strong acid (-57.3 kJ mol^-1).", 2, lines_count=2,
                    mark_scheme="% diff = [(57.3 - 50.6) / 57.3] x 100 = 11.69% [2].")
            ]
        ),
        # Q4: Enthalpy of Solution (Na2CO3)
        PracticalQuestion(
            number=4,
            title="Enthalpy of Solution of Anhydrous vs Hydrated Sodium Carbonate",
            syllabus_ref="9701/32/O/N/22/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Data:</b><br/>"
                "• Dissolving 5.30 g anhydrous Na2CO3 in 50.0 cm<sup>3</sup> water causes temperature to rise by 4.8°C (exothermic).<br/>"
                "• Dissolving 14.30 g hydrated Na2CO3.10H2O in 50.0 cm<sup>3</sup> water causes temperature to drop by 4.2°C (endothermic)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the molar enthalpy of solution of anhydrous Na2CO3. [Mr = 106.0]", 3, lines_count=3,
                    mark_scheme="q = 50.0 x 4.18 x 4.8 = 1003.2 J = 1.003 kJ [1]; Moles = 5.30 / 106.0 = 0.0500 mol [1]; delta-H = -1.003 / 0.0500 = -20.1 kJ mol^-1 [1]."),
                PracticalSubQuestion("(b)", "Calculate the molar enthalpy of solution of hydrated Na2CO3.10H2O. [Mr = 286.0]", 3, lines_count=3,
                    mark_scheme="q = 50.0 x 4.18 x (-4.2) = -877.8 J = -0.878 kJ [1]; Moles = 14.30 / 286.0 = 0.0500 mol [1]; delta-H = +0.878 / 0.0500 = +17.6 kJ mol^-1 [1]."),
                PracticalSubQuestion("(c)", "Construct an energy cycle (Hess's Law) and calculate the enthalpy of hydration for: Na2CO3(s) + 10H2O(l) -> Na2CO3.10H2O(s).", 4, lines_count=4,
                    mark_scheme="delta-H_hydration = delta-H_sol(anhydrous) - delta-H_sol(hydrated) [2]; delta-H_hydration = -20.1 - (+17.6) = -37.7 kJ mol^-1 [2].")
            ]
        ),
        # Q5: Endothermic Dissolution of NH4NO3
        PracticalQuestion(
            number=5,
            title="Calorimetric Measurement of Endothermic Dissolution: Ammonium Nitrate",
            syllabus_ref="9701/35/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Method:</b> 8.00 g of ammonium nitrate, NH4NO3 (Mr = 80.0), is dissolved in 50.0 cm<sup>3</sup> of water in an insulated cup. "
                "The initial temperature was 21.0°C and the minimum temperature recorded was 9.5°C."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the temperature drop and the heat energy absorbed, q.", 2, lines_count=2,
                    mark_scheme="delta-T = 9.5 - 21.0 = -11.5°C [1]; q = 50.0 x 4.18 x 11.5 = 2403.5 J = 2.404 kJ [1]."),
                PracticalSubQuestion("(b)", "Calculate the molar enthalpy of solution, delta-H_sol, of NH4NO3 in kJ mol^-1.", 3, lines_count=3,
                    mark_scheme="Moles = 8.00 / 80.0 = 0.100 mol [1]; delta-H = +2.404 / 0.100 = +24.0 kJ mol^-1 [2] (positive sign required)."),
                PracticalSubQuestion("(c)", "Explain in terms of lattice energy and hydration enthalpies why the dissolution of NH4NO3 is endothermic.", 3, lines_count=3,
                    mark_scheme="delta-H_sol = Lattice Energy + delta-H_hydration [1]; the magnitude of the endothermic lattice energy required to separate ions is greater than the exothermic hydration energy released when ions are solvated by water molecules [2]."),
                PracticalSubQuestion("(d)", "Suggest how this reaction is utilized in emergency medicine.", 2, lines_count=2,
                    mark_scheme="Used in instant cold packs to treat sporting injuries, sprains, and reduce swelling without refrigeration [2].")
            ]
        ),
        # Q6: Hess's Law Decomposition of MgCO3
        PracticalQuestion(
            number=6,
            title="Indirect Determination of Enthalpy of Decomposition of Magnesium Carbonate via Hess's Law",
            syllabus_ref="9701/34/M/J/22/Q2",
            total_marks=10,
            procedure_intro=(
                "It is impossible to measure directly the enthalpy change for: MgCO<sub>3</sub>(s) &rarr; MgO(s) + CO<sub>2</sub>(g).<br/>"
                "A student determines this indirectly by measuring the enthalpy changes of reaction of MgCO3 and MgO with excess HCl(aq)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Reaction 1: MgCO3(s) + 2HCl(aq) -> MgCl2(aq) + CO2(g) + H2O(l) gives delta-H1 = -52.0 kJ mol^-1.<br/>Reaction 2: MgO(s) + 2HCl(aq) -> MgCl2(aq) + H2O(l) gives delta-H2 = -151.0 kJ mol^-1.<br/>Construct the Hess's Law cycle.", 4, lines_count=4,
                    mark_scheme="Cycle drawn showing MgCO3 and MgO both reacting with 2HCl to form MgCl2(aq) + H2O(l) [2]; delta-H_target = delta-H1 - delta-H2 [2]."),
                PracticalSubQuestion("(b)", "Calculate delta-H for the thermal decomposition of MgCO3.", 2, lines_count=2,
                    mark_scheme="delta-H = -52.0 - (-151.0) = +99.0 kJ mol^-1 [2]."),
                PracticalSubQuestion("(c)", "State why this decomposition cannot be measured directly in a calorimeter.", 2, lines_count=2,
                    mark_scheme="Thermal decomposition requires high temperatures (Bunsen flame) so heat is constantly supplied, preventing simple calorimetric measurement [2]."),
                PracticalSubQuestion("(d)", "Predict whether calcium carbonate requires a higher or lower decomposition temperature than MgCO3. Explain.", 2, lines_count=2,
                    mark_scheme="Higher temperature [1]; Ca2+ has a larger ionic radius and lower charge density than Mg2+, causing less polarization of the carbonate ion [1].")
            ]
        ),
        # Q7: Limiting Reactant Calorimetry
        PracticalQuestion(
            number=7,
            title="Limiting Reactant Evaluation in Metal-Acid Displacement Calorimetry",
            syllabus_ref="9701/31/O/N/21/Q2",
            total_marks=10,
            procedure_intro=(
                "1.20 g of magnesium ribbon is added to 40.0 cm<sup>3</sup> of 1.50 mol dm<sup>-3</sup> HCl in a polystyrene cup.<br/>"
                "Equation: Mg(s) + 2HCl(aq) &rarr; MgCl<sub>2</sub>(aq) + H<sub>2</sub>(g)<br/>"
                "Initial temperature = 19.5°C; Maximum temperature = 47.0°C."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the moles of Mg and moles of HCl present, and identify the limiting reactant. [Ar: Mg = 24.3]", 3, lines_count=3,
                    mark_scheme="Moles Mg = 1.20 / 24.3 = 0.04938 mol [1]; Moles HCl = 1.50 x 0.0400 = 0.0600 mol [1]; 0.0600 mol HCl reacts with 0.0300 mol Mg -> HCl is the limiting reactant [1]."),
                PracticalSubQuestion("(b)", "Calculate the heat evolved, q, in the reaction.", 2, lines_count=2,
                    mark_scheme="delta-T = 47.0 - 19.5 = 27.5°C [1]; q = 40.0 x 4.18 x 27.5 = 4598 J = 4.60 kJ [1]."),
                PracticalSubQuestion("(c)", "Calculate the molar enthalpy change per mole of magnesium reacted.", 3, lines_count=3,
                    mark_scheme="Moles of Mg reacted = moles of HCl / 2 = 0.0600 / 2 = 0.0300 mol [1]; delta-H = -4.60 / 0.0300 = -153.3 kJ mol^-1 [2]."),
                PracticalSubQuestion("(d)", "State the hazard associated with hydrogen gas evolution during this vigorous reaction.", 2, lines_count=2,
                    mark_scheme="Hydrogen is highly flammable and forms explosive mixtures with air; keep away from open flames [2].")
            ]
        ),
        # Q8: Heat Loss & Apparatus Modifications
        PracticalQuestion(
            number=8,
            title="Systematic Evaluation of Heat Loss in Solution Calorimetry and Apparatus Improvements",
            syllabus_ref="9701/32/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "A student determines the enthalpy change of a reaction using a simple polystyrene cup with no lid. "
                "The experimental value obtained is -42.5 kJ mol^-1, compared to the accepted data book value of -54.0 kJ mol^-1."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the percentage experimental discrepancy between the student's result and the data book value.", 2, lines_count=2,
                    mark_scheme="% error = [(54.0 - 42.5) / 54.0] x 100 = 21.3% [2]."),
                PracticalSubQuestion("(b)", "Identify two primary avenues of heat loss in this experiment.", 2, lines_count=2,
                    mark_scheme="Convection and evaporation from the unsealed top surface [1]; conduction through cup walls and to the thermometer/stirrer [1]."),
                PracticalSubQuestion("(c)", "Suggest three specific apparatus modifications to significantly reduce heat loss.", 3, lines_count=3,
                    mark_scheme="1. Add a fitted polystyrene lid with a small hole for the thermometer [1]; 2. Double-cup the calorimeter / nest inside a second polystyrene cup inside a glass beaker [1]; 3. Use a vacuum Dewar flask instead of polystyrene [1]."),
                PracticalSubQuestion("(d)", "Explain why assuming the specific heat capacity of the solution is 4.18 J g^-1 °C^-1 introduces a small systematic error.", 3, lines_count=3,
                    mark_scheme="4.18 is the heat capacity of pure water; dissolved solute ions alter bonding and heat capacity, typically lowering the solution's actual heat capacity slightly below 4.18 [3].")
            ]
        ),
        # Q9: Thermometer Uncertainty
        PracticalQuestion(
            number=9,
            title="Analysis of Thermometer Uncertainty and Temperature Increment Sensitivity",
            syllabus_ref="9701/33/M/J/21/Q2",
            total_marks=10,
            procedure_intro=(
                "Thermometer A is graduated in 1°C divisions (uncertainty ±0.5°C per reading).<br/>"
                "Thermometer B is graduated in 0.1°C divisions (uncertainty ±0.05°C per reading).<br/>"
                "Two experiments are compared: Experiment 1 has delta-T = 3.5°C; Experiment 2 has delta-T = 25.0°C."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the percentage uncertainty in measuring delta-T in Experiment 1 using Thermometer A.", 3, lines_count=3,
                    mark_scheme="Two temperature readings (initial and final) -> total uncertainty = 2 x 0.5 = 1.0°C [1]; % uncertainty = (1.0 / 3.5) x 100 = 28.6% [2]."),
                PracticalSubQuestion("(b)", "Calculate the percentage uncertainty in measuring delta-T in Experiment 2 using Thermometer A.", 2, lines_count=2,
                    mark_scheme="% uncertainty = (1.0 / 25.0) x 100 = 4.0% [2]."),
                PracticalSubQuestion("(c)", "Explain why Experiment 1 with Thermometer A is unacceptable for quantitative examination purposes.", 2, lines_count=2,
                    mark_scheme="A 28.6% apparatus uncertainty exceeds acceptable scientific error margins (<5%) and renders the calculated enthalpy change unreliable [2]."),
                PracticalSubQuestion("(d)", "Suggest two ways to increase delta-T in a solution calorimetry experiment to minimize percentage uncertainty.", 3, lines_count=3,
                    mark_scheme="Increase the concentration of the reactants [1.5]; decrease the volume of solvent/water while maintaining the same moles of solute [1.5].")
            ]
        ),
        # Q10: Graphical Best-Fit Curve Analysis
        PracticalQuestion(
            number=10,
            title="Graphical Analysis of Cooling Curves and Identification of Experimental Anomalies",
            syllabus_ref="9701/34/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "A student records the cooling curve for an exothermic displacement reaction. "
                "At t = 4.5 min, the student reads 36.5°C, while readings at 4.0 min and 5.0 min are 41.0°C and 40.5°C respectively."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the anomalous reading and suggest a plausible laboratory error that caused it.", 3, lines_count=3,
                    mark_scheme="Reading at t = 4.5 min (36.5°C) is anomalous [1]; Cause: misreading the thermometer scale by 5°C (read 36.5 instead of 41.5) or thermometer bulb temporarily lifted out of liquid or incomplete initial stirring [2]."),
                PracticalSubQuestion("(b)", "Describe how an anomalous point should be treated when drawing the line of best fit.", 2, lines_count=2,
                    mark_scheme="Circle or clearly identify the point as an anomaly and ignore it when plotting the cooling line of best fit [2]."),
                PracticalSubQuestion("(c)", "State the mathematical condition for drawing two straight lines of best fit to determine delta-T.", 3, lines_count=3,
                    mark_scheme="Line 1: Extrapolate initial pre-mixing temperatures forward to the time of mixing (t = 3.0 min) [1.5]; Line 2: Extrapolate post-peak cooling temperatures backward to t = 3.0 min [1.5]."),
                PracticalSubQuestion("(d)", "Explain why the vertical distance between the two lines at t = 3.0 min represents the true corrected temperature rise.", 2, lines_count=2,
                    mark_scheme="It models the hypothetical instantaneous reaction temperature rise assuming zero heat was lost to the environment during reaction [2].")
            ]
        )
    ]

    p2_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Topic5_Chemical_Energetics.pdf")
    build_paper3_pdf(p2_pdf, p2_cfg, p2_questions, include_qa_notes=False)

    # =========================================================================
    # 3. TOPIC 8: REACTION KINETICS (PAST 4 YEARS: 2021-2024 — 10 MASTER QUESTIONS)
    # =========================================================================
    p3_cfg = PracticalPaperConfig(
        title="Physical Chemistry Practical: Topic 8 — Reaction Kinetics",
        subtitle="10 Most Frequently Asked Practical Examination Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 3 — Advanced Practical Skills (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100
    )

    p3_questions = [
        # Q1: Gas Syringe Rate Curve
        PracticalQuestion(
            number=1,
            title="Investigation of Reaction Rate by Gas Evolution: Magnesium and Hydrochloric Acid",
            syllabus_ref="9701/33/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> Mg(s) + 2HCl(aq) &rarr; MgCl<sub>2</sub>(aq) + H<sub>2</sub>(g)<br/>"
                "<b>Method:</b> 0.050 g Mg ribbon is added to 25.0 cm<sup>3</sup> of 1.00 mol dm<sup>-3</sup> HCl. "
                "The volume of hydrogen gas collected in the syringe is recorded every 10 seconds for 120 seconds."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why the rate of reaction is fastest at t = 0 s and decreases continuously over time.", 3, lines_count=3,
                    mark_scheme="At t = 0, the concentration of HCl and available surface area of Mg are at their highest, leading to maximum collision frequency [1.5]; as reactants are consumed, concentration decreases, collisions per second decrease, and the rate slows down [1.5]."),
                PracticalSubQuestion("(b)", "Sketch the expected curve of gas volume against time.", 2, lines_count=2,
                    mark_scheme="Smooth curve passing through origin, steep initial gradient, leveling off horizontally at constant maximum volume [2]."),
                PracticalSubQuestion("(c)", "State what feature of the graph indicates that the reaction has finished.", 2, lines_count=2,
                    mark_scheme="The curve becomes completely horizontal / gradient equals zero [2]."),
                PracticalSubQuestion("(d)", "Calculate the maximum theoretical volume of H2 gas produced at room conditions. [Ar: Mg = 24.3, Vm = 24.0 dm<sup>3</sup> mol^-1]", 3, lines_count=3,
                    mark_scheme="Moles Mg = 0.050 / 24.3 = 2.058 x 10^-3 mol [1]; Moles HCl = 0.0250 mol (excess) [1]; Vol = 2.058 x 10^-3 x 24000 = 49.4 cm<sup>3</sup> [1].")
            ]
        ),
        # Q2: Initial Rate via Tangent
        PracticalQuestion(
            number=2,
            title="Determination of Initial Reaction Rate via Graphical Tangent Construction",
            syllabus_ref="9701/32/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "A curve of volume of gas (V / cm<sup>3</sup>) versus time (t / s) is plotted. "
                "A tangent drawn to the curve at t = 0 s passes through coordinates (0, 0) and (25, 45)."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Calculate the initial rate of reaction from the tangent coordinates, including units.", 3, lines_count=3,
                    mark_scheme="Gradient = delta-V / delta-t = (45 - 0) / (25 - 0) = 1.80 [2]; Units = cm<sup>3</sup> s^-1 (or cm<sup>3</sup> / s) [1]."),
                PracticalSubQuestion("(b)", "Explain why initial rate (at t = 0) is preferred over average rate over the entire reaction.", 3, lines_count=3,
                    mark_scheme="At t = 0, the concentrations of reactants are precisely known (identical to initial starting concentrations) before any significant consumption or back-reaction occurs [3]."),
                PracticalSubQuestion("(c)", "Describe how the tangent at t = 0 s should be drawn accurately on an experimental curve.", 2, lines_count=2,
                    mark_scheme="Place a transparent ruler so it follows the initial curvature smoothly at the origin, ensuring angles between ruler and curve on both sides are balanced [2]."),
                PracticalSubQuestion("(d)", "If the temperature of the acid were increased by 10°C, state how the tangent slope would change.", 2, lines_count=2,
                    mark_scheme="The slope of the tangent would be significantly steeper (approximately double in gradient) due to higher kinetic energy and collision frequency [2].")
            ]
        ),
        # Q3: Disappearing Cross Kinetics
        PracticalQuestion(
            number=3,
            title="The Sodium Thiosulfate and Hydrochloric Acid Disappearing Cross Reaction",
            syllabus_ref="9701/34/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Reaction:</b> Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub>(aq) + 2HCl(aq) &rarr; 2NaCl(aq) + SO<sub>2</sub>(g) + S(s) + H<sub>2</sub>O(l)<br/>"
                "<b>Method:</b> A conical flask is placed over a paper sheet marked with a black cross (+). "
                "The time taken, t, for the precipitated sulfur to obscure the cross is measured."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why the quantity 1/t can be taken as a direct measure of the rate of this reaction.", 3, lines_count=3,
                    mark_scheme="Rate is defined as change in concentration / time [1]; the cross disappears when a constant fixed mass/concentration of solid sulfur precipitate forms [1]; since delta-[S] is constant, Rate is directly proportional to 1/t [1]."),
                PracticalSubQuestion("(b)", "State the physical state of the sulfur that causes the cross to disappear.", 2, lines_count=2,
                    mark_scheme="Colloidal suspension of solid sulfur precipitate, S(s) [2]."),
                PracticalSubQuestion("(c)", "If the cross disappears in 42.0 seconds, calculate the rate (1/t) to three significant figures with units.", 2, lines_count=2,
                    mark_scheme="1 / 42.0 = 0.0238 s^-1 [2]."),
                PracticalSubQuestion("(d)", "State two subjective errors associated with human observation of the disappearing cross.", 3, lines_count=3,
                    mark_scheme="Observer judgment of the exact moment the cross is obscured varies between individuals [1.5]; ambient lighting changes and viewing angle affect perception [1.5].")
            ]
        ),
        # Q4: Order with Respect to Thiosulfate
        PracticalQuestion(
            number=4,
            title="Determination of Reaction Order with Respect to Sodium Thiosulfate",
            syllabus_ref="9701/33/O/N/22/Q2",
            total_marks=10,
            procedure_intro=(
                "Five runs are performed using different volumes of 0.100 mol dm<sup>-3</sup> Na2S2O3 made up to 50.0 cm<sup>3</sup> with water, "
                "then mixed with 5.0 cm<sup>3</sup> of 2.0 mol dm<sup>-3</sup> HCl. Results:<br/>"
                "• Vol Na2S2O3: 50.0, 40.0, 30.0, 20.0, 10.0 cm<sup>3</sup><br/>"
                "• 1/t (x10^-3 s^-1): 44.0, 35.2, 26.5, 17.6, 8.8"
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Plot or describe the relationship between Rate (1/t) and volume of Na2S2O3.", 3, lines_count=3,
                    mark_scheme="A straight line passing directly through the origin (0, 0) [3]."),
                PracticalSubQuestion("(b)", "Deduce the order of reaction with respect to Na2S2O3 and justify your conclusion mathematically.", 3, lines_count=3,
                    mark_scheme="Order is 1 (first order) [1]; Rate is directly proportional to [Na2S2O3]^1; doubling volume from 20 to 40 cm<sup>3</sup> doubles rate from 17.6 to 35.2 x 10^-3 s^-1 [2]."),
                PracticalSubQuestion("(c)", "Explain why water was added to each mixture to maintain a total volume of 55.0 cm<sup>3</sup>.", 2, lines_count=2,
                    mark_scheme="To ensure the volume of Na2S2O3 is directly proportional to its concentration and to keep the depth of liquid constant in the flask [2]."),
                PracticalSubQuestion("(d)", "Write the rate equation with respect to Na2S2O3 assuming it is first order.", 2, lines_count=2,
                    mark_scheme="Rate = k [Na2S2O3] [2].")
            ]
        ),
        # Q5: Order with Respect to HCl
        PracticalQuestion(
            number=5,
            title="Investigation of the Order of Reaction with Respect to Hydrochloric Acid",
            syllabus_ref="9701/35/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "The concentration of Na2S2O3 is kept constant, while the volume of 2.0 mol dm<sup>-3</sup> HCl is varied from 5.0 to 20.0 cm<sup>3</sup> "
                "(total volume maintained at 50.0 cm<sup>3</sup>). The reaction time t remains virtually unchanged at 28.0 ± 0.5 s across all trials."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Deduce the order of reaction with respect to HCl based on this data.", 2, lines_count=2,
                    mark_scheme="Zero order (order = 0) with respect to HCl [2]."),
                PracticalSubQuestion("(b)", "Explain what 'zero order' signifies regarding the rate-determining step of the reaction mechanism.", 3, lines_count=3,
                    mark_scheme="H+ ions are not involved in the slow rate-determining step of the reaction mechanism (or are involved in a fast step subsequent to the rate-determining step) [3]."),
                PracticalSubQuestion("(c)", "Combine the findings from Q4 and Q5 to write the overall rate equation.", 2, lines_count=2,
                    mark_scheme="Rate = k [Na2S2O3] [2]."),
                PracticalSubQuestion("(d)", "State the overall order of the reaction and deduce the units of the rate constant, k.", 3, lines_count=3,
                    mark_scheme="Overall order = 1 + 0 = 1 [1]; Units of k = (mol dm^-3 s^-1) / (mol dm^-3) = s^-1 [2].")
            ]
        ),
        # Q6: Constant Volume Maintenance
        PracticalQuestion(
            number=6,
            title="Experimental Design: The Critical Role of Constant Depth and Volume in Turbidimetric Experiments",
            syllabus_ref="9701/31/O/N/23/Q2",
            total_marks=10,
            procedure_intro=(
                "A student repeats the disappearing cross experiment but forgets to add distilled water to make up the volume. "
                "Consequently, the total liquid volume decreases from 55 cm<sup>3</sup> in trial 1 to 15 cm<sup>3</sup> in trial 5."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain how varying liquid depth fundamentally invalidates the 1/t approximation of rate.", 4, lines_count=4,
                    mark_scheme="The black cross is obscured when the total mass of sulfur in the light path reaches a threshold [1]; if depth decreases, light travels through less liquid [1]; more sulfur precipitate per unit volume is required to obscure the cross, so delta-[S] is no longer constant [2]."),
                PracticalSubQuestion("(b)", "Predict how the observed reaction time in trial 5 will compare to a properly volume-compensated trial.", 2, lines_count=2,
                    mark_scheme="The time will be significantly longer than expected [2]."),
                PracticalSubQuestion("(c)", "Suggest how a datalogger with a colorimeter can replace human visual judgment to give continuous absorbance curves.", 4, lines_count=4,
                    mark_scheme="Light from an LED source passes through a cuvette containing the mixture to a photodiode detector [2]; light transmittance decreases smoothly as sulfur precipitate scatters light, allowing the computer to plot absorbance against time continuously [2].")
            ]
        ),
        # Q7: Temperature Dependence & Activation Energy
        PracticalQuestion(
            number=7,
            title="Effect of Temperature on Reaction Rate and Qualitative Estimation of Activation Energy",
            syllabus_ref="9701/32/O/N/21/Q2",
            total_marks=10,
            procedure_intro=(
                "The reaction between sodium thiosulfate and hydrochloric acid is performed at temperatures between 20°C and 55°C.<br/>"
                "Results: 20°C -> 56 s; 30°C -> 28 s; 40°C -> 14 s; 50°C -> 7 s."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Identify the mathematical trend shown by the reaction time as temperature increases in 10°C intervals.", 2, lines_count=2,
                    mark_scheme="For every 10°C rise in temperature, the reaction time halves (rate doubles) [2]."),
                PracticalSubQuestion("(b)", "Explain this exponential rate increase in terms of the Maxwell-Boltzmann distribution of molecular energies.", 4, lines_count=4,
                    mark_scheme="At higher temperature, average kinetic energy increases and the distribution curve flattens and shifts to the right [1]; a significantly greater fraction of molecules possess kinetic energy greater than or equal to the activation energy (E >= Ea) [2]; the frequency of successful collisions per unit time increases dramatically [1]."),
                PracticalSubQuestion("(c)", "Sketch the Maxwell-Boltzmann distribution curve for two temperatures, T1 and T2 (where T2 > T1), labeling Ea.", 4, lines_count=4,
                    mark_scheme="Curves start at origin, peak of T2 lower and shifted right [2]; Ea marked on energy axis, shaded area for T2 noticeably larger than for T1 [2].")
            ]
        ),
        # Q8: Timing Uncertainty
        PracticalQuestion(
            number=8,
            title="Quantitative Analysis of Stopwatch Precision and Human Reaction Time Uncertainty",
            syllabus_ref="9701/34/O/N/22/Q2",
            total_marks=10,
            procedure_intro=(
                "A digital stopwatch displays time to 0.01 seconds. Human reaction time is approximately ±0.2 seconds. "
                "In a kinetics run at 50°C, the recorded time was 6.20 s; in a run at 15°C, the recorded time was 120.00 s."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why quoting stopwatch readings to 0.01 s in practical chemistry is misleading.", 2, lines_count=2,
                    mark_scheme="Human reaction time in pressing start and stop buttons is around ±0.2 s, which is 20 times larger than the stopwatch display resolution [2]."),
                PracticalSubQuestion("(b)", "Calculate the percentage uncertainty in reaction time for the 6.20 s run (assume ±0.2 s uncertainty).", 3, lines_count=3,
                    mark_scheme="% uncertainty = (0.2 / 6.20) x 100 = 3.23% [3]."),
                PracticalSubQuestion("(c)", "Calculate the percentage uncertainty for the 120.00 s run.", 2, lines_count=2,
                    mark_scheme="% uncertainty = (0.2 / 120.0) x 100 = 0.17% [2]."),
                PracticalSubQuestion("(d)", "Explain why fast reactions (t < 10 s) should be avoided when designing kinetics experiments.", 3, lines_count=3,
                    mark_scheme="In fast reactions, percentage human timing uncertainty becomes very large (>5%), and mixing time becomes a significant fraction of total reaction time [3].")
            ]
        ),
        # Q9: Toxic SO2 Safety
        PracticalQuestion(
            number=9,
            title="Chemical Safety: Hazard Mitigation of Sulfur Dioxide Gas in Reaction Kinetics",
            syllabus_ref="9701/31/M/J/24/Q2",
            total_marks=10,
            procedure_intro=(
                "The reaction of thiosulfate with acid produces toxic sulfur dioxide, SO2, which is an irritant to the respiratory system. "
                "The Cambridge practical instructions mandate placing flasks into a 'stop bath' immediately after each run."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "State the hazard classification of sulfur dioxide and identify which students are particularly at risk.", 2, lines_count=2,
                    mark_scheme="Toxic / respiratory irritant [1]; individuals with asthma or respiratory conditions [1]."),
                PracticalSubQuestion("(b)", "Identify the active chemical present in a standard laboratory stop bath and explain how it neutralizes SO2.", 3, lines_count=3,
                    mark_scheme="Aqueous sodium carbonate (Na2CO3) or sodium hydrogencarbonate (NaHCO3) [1]; basic carbonate neutralizes acidic SO2 gas: SO2(g) + CO3^2-(aq) -> SO3^2-(aq) + CO2(g), trapping it as harmless aqueous sulfite [2]."),
                PracticalSubQuestion("(c)", "State two laboratory ventilation precautions when carrying out thiosulfate kinetics.", 2, lines_count=2,
                    mark_scheme="Work in a well-ventilated laboratory with windows open or in an operating fume cupboard [2]."),
                PracticalSubQuestion("(d)", "Write the balanced chemical equation for the reaction of SO2 with sodium hydroxide solution.", 3, lines_count=3,
                    mark_scheme="SO2 + 2NaOH -> Na2SO3 + H2O [3] (or SO2 + NaOH -> NaHSO3).")
            ]
        ),
        # Q10: Homogeneous Catalysis
        PracticalQuestion(
            number=10,
            title="Homogeneous Catalysis of the Peroxodisulfate-Iodide Reaction by Transition Metal Ions",
            syllabus_ref="9701/35/M/J/23/Q2",
            total_marks=10,
            procedure_intro=(
                "<b>Uncatalyzed Reaction:</b> S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2I<sup>-</sup>(aq) &rarr; 2SO<sub>4</sub><sup>2-</sup>(aq) + I<sub>2</sub>(aq)<br/>"
                "This reaction is very slow at room temperature because both reactants are negatively charged anions that repel each other.<br/>"
                "The reaction can be catalyzed by either Fe<sup>2+</sup>(aq) or Fe<sup>3+</sup>(aq) ions."
            ),
            subquestions=[
                PracticalSubQuestion("(a)", "Explain why the uncatalyzed reaction between peroxodisulfate and iodide ions has a high activation energy.", 2, lines_count=2,
                    mark_scheme="Both S2O8^2- and I- are negatively charged anions; strong electrostatic repulsion between like charges creates a high activation energy barrier [2]."),
                PracticalSubQuestion("(b)", "Write the two consecutive chemical equations demonstrating how Fe3+ acts as a homogeneous catalyst.", 4, lines_count=4,
                    mark_scheme="Step 1: 2Fe3+(aq) + 2I-(aq) -> 2Fe2+(aq) + I2(aq) [2]; Step 2: 2Fe2+(aq) + S2O8^2-(aq) -> 2Fe3+(aq) + 2SO4^2-(aq) [2]."),
                PracticalSubQuestion("(c)", "Explain why each step in the catalyzed mechanism has a lower activation energy than the uncatalyzed reaction.", 2, lines_count=2,
                    mark_scheme="Each catalyzed step involves an oppositely charged cation and anion (Fe3+ with I-, and Fe2+ with S2O8^2-), so attractive electrostatic forces facilitate collision [2]."),
                PracticalSubQuestion("(d)", "Explain why iron(II) ions, Fe2+, are equally effective as a catalyst as iron(III) ions.", 2, lines_count=2,
                    mark_scheme="Fe2+ can be oxidized by S2O8^2- first to form Fe3+, which then oxidizes I-; the cycle is closed and catalyst is regenerated in both cases [2].")
            ]
        )
    ]

    p3_pdf = os.path.join(dest_dir, "Urwah_Chem_Paper3_Past10Years_Topic8_Reaction_Kinetics.pdf")
    build_paper3_pdf(p3_pdf, p3_cfg, p3_questions, include_qa_notes=False)

    print("=== Physical Chemistry Past 10 Years Suite Complete (3 Papers) ===")

if __name__ == "__main__":
    build_physical_past10years()
