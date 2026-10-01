"""
Cambridge International A Level Chemistry (9701) Paper 5 (Planning, Analysis and Evaluation)
Inorganic Chemistry — Past 10 Years Master Examination Suite (Past 4 Years Analysis: 2021-2024)
Candidate: Urwah | Mentora Academy
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from build_paper5_pdf import (
    Paper5SubQuestion, Paper5Question, Paper5PaperConfig,
    build_paper5_pdf, get_paper5_styles,
    COLOR_BG_LIGHT, COLOR_BORDER, COLOR_NAVY
)

def make_simple_table(header_list, row_list, col_widths, styles):
    data = [[Paragraph(f"<b>{h}</b>", styles['table_header']) for h in header_list]]
    for row in row_list:
        data.append([Paragraph(str(c), styles['table_cell_center']) for c in row])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t

def build_a2_past10years_inorganic():
    styles = get_paper5_styles()
    
    cfg = Paper5PaperConfig(
        title="Inorganic Chemistry Practical: Paper 5 Master Suite",
        subtitle="10 Most Frequently Tested Planning, Analysis & Evaluation Questions (Past 4 Years Analysis: 2021–2024)",
        component_name="Paper 5 — Planning, Analysis and Evaluation (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100,
        candidate_name="Urwah"
    )

    questions = [
        # Q1: Job's Method Continuous Variation
        Paper5Question(
            number=1,
            title="Planning a Colorimetric Determination of Complex Formula via Job's Method",
            syllabus_ref="9701/52/M/J/24/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Iron(III) ions react with thiocyanate ions in acidic solution to form an intense blood-red complex:<br/>"
                "Fe<sup>3+</sup>(aq) + <i>n</i>SCN<sup>-</sup>(aq) &rightleftharpoons; [Fe(SCN)<sub><i>n</i></sub>]<sup>(3-<i>n</i>)+</sup>(aq).<br/>"
                "In Job's method of continuous variation, the total molar concentration ([Fe<sup>3+</sup>] + [SCN<sup>-</sup>]) is kept constant "
                "while the mole fraction of thiocyanate, <i>x</i><sub>SCN</sub>, is varied from 0.0 to 1.0.<br/>"
                "Plan an experiment to determine the value of <i>n</i> using a colorimeter."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Specify the concentrations and volumes of equimolar solutions of Fe(NO<sub>3</sub>)<sub>3</sub> and KSCN (0.0020 mol dm<sup>-3</sup> in 0.1 mol dm<sup>-3</sup> HNO<sub>3</sub>) to prepare seven mixtures of total volume 25.0 cm<sup>3</sup>.", 3, lines_count=0,
                    table_data=make_simple_table(
                        ["Mixture", "Vol Fe(NO3)3 / cm3", "Vol KSCN / cm3", "x(SCN)"],
                        [["1", "22.5", "2.5", "0.10"],
                         ["2", "17.5", "7.5", "0.30"],
                         ["3", "12.5", "12.5", "0.50"],
                         ["4", "10.0", "15.0", "0.60"],
                         ["5", "7.5", "17.5", "0.70"],
                         ["6", "5.0", "20.0", "0.80"],
                         ["7", "2.5", "22.5", "0.90"]],
                        [100, 130, 130, 120], styles
                    ),
                    mark_scheme="Table showing total volume = 25.0 cm3 for all runs [1]; equimolar solutions ensuring volume ratio equals mole ratio [1]; acidified with HNO3 to prevent Fe3+ hydrolysis to Fe(OH)3 [1]."),
                Paper5SubQuestion("(b)", "State the appropriate colorimeter filter to choose and how to zero the instrument.", 2, lines_count=2,
                    mark_scheme="Use a blue / green-blue filter (approx 480-500 nm, complementary to blood-red colour) [1]; zero colorimeter using cuvette filled with distilled water / 0.1 mol dm^-3 HNO3 blank [1]."),
                Paper5SubQuestion("(c)", "Describe how the value of <i>n</i> is determined from a plot of absorbance against <i>x</i><sub>SCN</sub>.", 3, lines_count=3,
                    mark_scheme="Plot absorbance on y-axis against <i>x</i>(SCN) on x-axis [1]; draw two intersecting lines of best fit through rising and falling points [1]; read <i>x</i>_max at intersection; <i>n</i> = <i>x</i>_max / (1 - <i>x</i>_max) [1]."),
                Paper5SubQuestion("(d)", "If the maximum absorbance occurs at <i>x</i><sub>SCN</sub> = 0.50, deduce the formula of the complex.", 2, lines_count=2,
                    mark_scheme="<i>n</i> = 0.50 / (1 - 0.50) = 1.0 &rArr; <i>n</i> = 1 [1]; formula: [Fe(SCN)]^2+ (or [Fe(H2O)5(SCN)]^2+) [1].")
            ]
        ),

        # Q2: Thermal Decomposition Malachite
        Paper5Question(
            number=2,
            title="Analysis and Evaluation of the Stoichiometry of Malachite Thermal Decomposition",
            syllabus_ref="9701/51/O/N/23/Q1",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "Basic copper(II) carbonate, malachite, has the empirical formula CuCO<sub>3</sub>&middot;Cu(OH)<sub>2</sub>.<br/>"
                "Upon strong heating in a porcelain crucible, it undergoes thermal decomposition according to:<br/>"
                "CuCO<sub>3</sub>&middot;Cu(OH)<sub>2</sub>(s) &rarr; 2CuO(s) + CO<sub>2</sub>(g) + H<sub>2</sub>O(g).<br/>"
                "Molar masses: CuCO<sub>3</sub>&middot;Cu(OH)<sub>2</sub> = 221.0 g mol<sup>-1</sup>; CuO = 79.5 g mol<sup>-1</sup>; "
                "CO<sub>2</sub> = 44.0 g mol<sup>-1</sup>; H<sub>2</sub>O = 18.0 g mol<sup>-1</sup>."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Calculate the theoretical percentage mass loss expected when malachite decomposes completely.", 2, lines_count=2,
                    mark_scheme="Total mass of gases evolved = 44.0 + 18.0 = 62.0 g mol^-1 [1]; % mass loss = (62.0 / 221.0) &times; 100% = 28.05% [1]."),
                Paper5SubQuestion("(b)", "A student heated 4.420 g of malachite and recorded a final constant mass of residue of 3.280 g. Calculate the experimental percentage mass loss.", 2, lines_count=2,
                    mark_scheme="Mass lost = 4.420 - 3.280 = 1.140 g [1]; % mass loss = (1.140 / 4.420) &times; 100% = 25.79% [1]."),
                Paper5SubQuestion("(c)", "Suggest two distinct reasons why the experimental percentage mass loss is lower than theoretical.", 2, lines_count=3,
                    mark_scheme="1. Incomplete decomposition (crucible not heated strongly or long enough) [1]; 2. Residue reabsorbed moisture from air while cooling without desiccator [1]."),
                Paper5SubQuestion("(d)", "Explain the role of the crucible lid and why it must be slightly ajar during heating but closed during cooling.", 2, lines_count=2,
                    mark_scheme="Slightly ajar during heating to allow evolved CO2 and H2O steam to escape while preventing spitting [1]; fully closed during cooling in desiccator to prevent reabsorption of atmospheric moisture [1]."),
                Paper5SubQuestion("(e)", "Suggest a chemical test to confirm that the black residue is pure CuO and contains no unreacted malachite.", 2, lines_count=2,
                    mark_scheme="Add dilute sulfuric acid: CuO dissolves forming blue solution without effervescence [1]; if unreacted carbonate is present, effervescence / gas turning limewater cloudy occurs [1].")
            ]
        ),

        # Q3: Redox Ferrochrome Alloy
        Paper5Question(
            number=3,
            title="Planning a Redox Titrimetric Analysis of Chromium Content in Ferrochrome Alloy",
            syllabus_ref="9701/53/M/J/23/Q2",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Ferrochrome is an alloy of iron and chromium. Plan an investigation to determine the percentage of chromium "
                "by mass in a sample of ferrochrome.<br/>"
                "The alloy is dissolved in hot concentrated sulfuric acid to yield Fe<sup>2+</sup> and Cr<sup>3+</sup>.<br/>"
                "Cr<sup>3+</sup> is oxidised to Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> using ammonium peroxodisulfate, (NH<sub>4</sub>)<sub>2</sub>S<sub>2</sub>O<sub>8</sub>, "
                "in the presence of a silver nitrate catalyst.<br/>"
                "The dichromate(VI) formed is titrated with standardized iron(II) ammonium sulfate."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain why the mixture must be boiled vigorously after adding (NH<sub>4</sub>)<sub>2</sub>S<sub>2</sub>O<sub>8</sub> before titration begins.", 2, lines_count=2,
                    mark_scheme="To decompose and destroy all excess unreacted peroxodisulfate ions [1]; otherwise, excess S2O8^2- would react with the standard Fe2+ titrant, leading to an overestimation of chromium [1]."),
                Paper5SubQuestion("(b)", "Write the balanced ionic equation for the reaction between Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> and Fe<sup>2+</sup> in acidic solution.", 2, lines_count=2,
                    mark_scheme="Cr2O7^2- + 6Fe^2+ + 14H^+ &rarr; 2Cr^3+ + 6Fe^3+ + 7H2O [2]."),
                Paper5SubQuestion("(c)", "State a suitable indicator for this titration and state the colour change at the end-point.", 2, lines_count=2,
                    mark_scheme="Barium diphenylamine sulfonate (or sodium diphenylamine sulfonate) [1]; colour change: violet / purple to green (or green to purple if titrating into Fe2+) [1]."),
                Paper5SubQuestion("(d)", "Outline the mathematical steps to calculate the percentage by mass of Cr in the alloy from the mean titre of Fe<sup>2+</sup>.", 3, lines_count=3,
                    mark_scheme="1. Moles Fe2+ = conc &times; titre; 2. Moles Cr2O7^2- = (1/6) &times; moles Fe2+ [1]; 3. Moles Cr in sample = 2 &times; moles Cr2O7^2- [1]; 4. Mass Cr = moles Cr &times; 52.0 g mol^-1; % Cr = (mass Cr / mass alloy) &times; 100% [1]."),
                Paper5SubQuestion("(e)", "State the hazard associated with dichromate(VI) solutions and the corresponding safety measure.", 1, lines_count=2,
                    mark_scheme="Carcinogenic / mutagenic / toxic; wear nitrile gloves and handle in designated fume area [1].")
            ]
        ),

        # Q4: Hexaamminecobalt(III) Synthesis
        Paper5Question(
            number=4,
            title="Planning the Synthesis and Recrystallisation of Hexaamminecobalt(III) Chloride",
            syllabus_ref="9701/52/O/N/22/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Hexaamminecobalt(III) chloride, [Co(NH<sub>3</sub>)<sub>6</sub>]Cl<sub>3</sub> (orange-yellow crystals), is prepared by "
                "the oxidation of cobalt(II) chloride in the presence of ammonia, ammonium chloride, and activated charcoal catalyst:<br/>"
                "2CoCl<sub>2</sub> + 2NH<sub>4</sub>Cl + 10NH<sub>3</sub> + H<sub>2</sub>O<sub>2</sub> &rarr; 2[Co(NH<sub>3</sub>)<sub>6</sub>]Cl<sub>3</sub> + 2H<sub>2</sub>O.<br/>"
                "The crude precipitate contains both [Co(NH<sub>3</sub>)<sub>6</sub>]Cl<sub>3</sub> and charcoal."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain the role of activated charcoal in this preparation.", 2, lines_count=2,
                    mark_scheme="Acts as a heterogeneous catalyst for ligand exchange / ligand substitution [1]; facilitates replacement of aqua ligands by ammonia to favour formation of [Co(NH3)6]^3+ over pentaammine aquo complexes [1]."),
                Paper5SubQuestion("(b)", "Describe how the crude product containing charcoal is separated from the reaction mixture.", 2, lines_count=2,
                    mark_scheme="Cool mixture in ice bath to maximize precipitation of product [1]; filter crude solid mixture using Buchner funnel under reduced pressure [1]."),
                Paper5SubQuestion("(c)", "Describe how pure [Co(NH<sub>3</sub>)<sub>6</sub>]Cl<sub>3</sub> is separated from the charcoal catalyst during recrystallisation.", 3, lines_count=3,
                    mark_scheme="Dissolve crude product in minimum volume of hot boiling dilute HCl (complex dissolves, charcoal remains insoluble) [1]; perform hot gravity filtration to remove insoluble charcoal [1]; cool filtrate in ice bath, precipitating pure orange crystals of [Co(NH3)6]Cl3, and filter under vacuum [1]."),
                Paper5SubQuestion("(d)", "Explain why hot dilute HCl is used instead of pure water for dissolving the complex.", 2, lines_count=2,
                    mark_scheme="Common ion effect (Cl-) reduces solubility of [Co(NH3)6]Cl3 upon cooling, enhancing yield [1]; acidic medium prevents base hydrolysis of ammine ligands [1]."),
                Paper5SubQuestion("(e)", "State how the crystals should be dried to obtain constant mass without decomposition.", 1, lines_count=2,
                    mark_scheme="Wash with cold ethanol, then dry in a desiccator over anhydrous calcium chloride / vacuum oven at &le; 50 &deg;C [1].")
            ]
        ),

        # Q5: Stability Constant Kstab Spectrophotometry
        Paper5Question(
            number=5,
            title="Analysis and Evaluation of the Stability Constant (Kstab) of Copper(II) Ammine Complex",
            syllabus_ref="9701/51/M/J/22/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "The stepwise substitution of water by ammonia in aqueous copper(II) forms [Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup>:<br/>"
                "[Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup>(aq) + 4NH<sub>3</sub>(aq) &rightleftharpoons; [Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l).<br/>"
                "The overall stability constant expression is: <i>K</i><sub>stab</sub> = [[Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup>] / ([Cu<sup>2+</sup>][NH<sub>3</sub>]<sup>4</sup>)."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain why [H<sub>2</sub>O] is omitted from the <i>K</i><sub>stab</sub> expression.", 2, lines_count=2,
                    mark_scheme="Water is the solvent and its concentration is effectively constant (~55.5 mol dm^-3) [1]; it is incorporated into the equilibrium constant value [1]."),
                Paper5SubQuestion("(b)", "In an equilibrium mixture, [[Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup>] = 0.0480 mol dm<sup>-3</sup>, [Cu<sup>2+</sup>] = 2.40 &times; 10<sup>-14</sup> mol dm<sup>-3</sup>, and [NH<sub>3</sub>] = 0.250 mol dm<sup>-3</sup>. Calculate <i>K</i><sub>stab</sub> and state its units.", 3, lines_count=3,
                    mark_scheme="<i>K</i>stab = (0.0480) / [(2.40 &times; 10^-14) &times; (0.250)^4] = 0.0480 / [9.375 &times; 10^-17] = 5.12 &times; 10^14 [2]; units: mol^-4 dm^12 [1]."),
                Paper5SubQuestion("(c)", "Calculate the standard Gibbs free energy change, &Delta;<i>G</i><sup>&deg;</sup>, for this complex formation at 298 K (&Delta;<i>G</i><sup>&deg;</sup> = -<i>RT</i> ln <i>K</i><sub>stab</sub>).", 2, lines_count=3,
                    mark_scheme="&Delta;G^&deg; = -8.314 &times; 298 &times; ln(5.12 &times; 10^14) = -2477.6 &times; 33.87 = -83.9 kJ mol^-1 [2]."),
                Paper5SubQuestion("(d)", "Explain in terms of the chelate effect why the complex with 1,2-diaminoethane (en), [Cu(en)<sub>3</sub>]<sup>2+</sup>, has a substantially higher <i>K</i><sub>stab</sub> than the tetraammine complex.", 3, lines_count=3,
                    mark_scheme="1,2-diaminoethane is a bidentate ligand [1]; substitution of unidentate ligands by bidentate ligands increases total number of free particles in solution [1]; results in a large positive entropy change of reaction (&Delta;S_sys > 0), driving &Delta;G^&deg; significantly more negative [1].")
            ]
        ),

        # Q6: Gravimetric Sulfate in Fertilizer
        Paper5Question(
            number=6,
            title="Planning Gravimetric Determination of Sulfate Content in Agricultural Fertilizer",
            syllabus_ref="9701/52/M/J/21/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Agricultural fertilizer contains ammonium sulfate, (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>.<br/>"
                "Sulfate ions can be quantitatively precipitated as insoluble barium sulfate:<br/>"
                "Ba<sup>2+</sup>(aq) + SO<sub>4</sub><sup>2-</sup>(aq) &rarr; BaSO<sub>4</sub>(s).<br/>"
                "Plan an experiment to determine the percentage by mass of sulfate in a fertilizer sample using gravimetric analysis."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain why the fertilizer solution must be acidified with dilute HCl before adding barium chloride.", 2, lines_count=2,
                    mark_scheme="To prevent the co-precipitation of other insoluble barium salts such as BaCO3 or Ba3(PO4)2 which are acid-soluble [2]."),
                Paper5SubQuestion("(b)", "Describe the 'digestion' process after precipitation and explain why it is essential for accurate filtration.", 2, lines_count=2,
                    mark_scheme="Maintain the precipitate in contact with the hot mother liquor near 80-90 &deg;C for 1 hour without boiling [1]; allows Ostwald ripening (dissolution of small particles and redeposition onto larger crystals), facilitating retention on filter paper and preventing colloidal loss [1]."),
                Paper5SubQuestion("(c)", "Specify the grade of filter paper required and describe how the precipitate is transferred without loss.", 2, lines_count=3,
                    mark_scheme="Ashless filter paper (e.g. Whatman 42) [1]; use rubber-tipped glass rod ('policeman') and hot distilled water wash bottle to rinse all precipitate from beaker walls onto filter [1]."),
                Paper5SubQuestion("(d)", "Describe how the precipitate is heated to constant mass in a crucible.", 2, lines_count=2,
                    mark_scheme="Heat crucible gently to char and burn off filter paper without flame, then heat strongly with blue Bunsen flame [1]; cool in desiccator, weigh, and repeat heating until two successive weighings agree within &plusmn;0.002 g [1]."),
                Paper5SubQuestion("(e)", "State how the student should test the filtrate to confirm that all sulfate has been precipitated.", 2, lines_count=2,
                    mark_scheme="Add a few drops of BaCl2 solution to the clear supernatant / filtrate [1]; absence of cloudiness confirms complete precipitation [1].")
            ]
        ),

        # Q7: Decomposition Group 2 Nitrates
        Paper5Question(
            number=7,
            title="Quantitative Analysis of Decomposition Trends in Group 2 Nitrates",
            syllabus_ref="9701/53/O/N/21/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "Group 2 nitrates decompose on heating according to:<br/>"
                "2M(NO<sub>3</sub>)<sub>2</sub>(s) &rarr; 2MO(s) + 4NO<sub>2</sub>(g) + O<sub>2</sub>(g).<br/>"
                "A student investigated the decomposition temperature of anhydrous nitrates of Mg, Ca, Sr, and Ba.<br/>"
                "The table lists the ionic radius of M<sup>2+</sup> and the minimum decomposition temperature <i>T</i><sub>decomp</sub>."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Complete the table by calculating charge density (2 / radius in nm) for each cation.", 2, lines_count=0,
                    table_data=make_simple_table(
                        ["Cation", "Ionic Radius / nm", "Charge Density / nm-1", "T(decomp) / K"],
                        [["Mg2+", "0.065", "30.8", "623"],
                         ["Ca2+", "0.099", "20.2", "834"],
                         ["Sr2+", "0.113", "17.7", "871"],
                         ["Ba2+", "0.135", "14.8", "923"]],
                        [120, 120, 120, 120], styles
                    ),
                    mark_scheme="Charge density values correct: 30.8, 20.2, 17.7, 14.8 nm^-1 [2]."),
                Paper5SubQuestion("(b)", "Plot a graph of <i>T</i><sub>decomp</sub> against ionic radius and describe the relationship.", 2, lines_count=2,
                    mark_scheme="Straight/smooth curve plotted with positive slope [1]; as ionic radius increases, decomposition temperature increases (thermal stability increases down Group 2) [1]."),
                Paper5SubQuestion("(c)", "Explain this trend in thermal stability in terms of cation polarising power.", 3, lines_count=3,
                    mark_scheme="Smaller cations have higher charge density / higher polarising power [1]; Mg2+ distorts the electron cloud of the nitrate anion (N-O bond) more strongly than Ba2+ [1]; weakens the N-O bond, requiring less thermal energy to break the bond and decompose [1]."),
                Paper5SubQuestion("(d)", "State the hazard associated with the gaseous product NO<sub>2</sub> and the safety precaution required.", 2, lines_count=2,
                    mark_scheme="NO2 is toxic / severe respiratory irritant [1]; carry out heating inside a well-ventilated fume cupboard [1]."),
                Paper5SubQuestion("(e)", "Suggest why anhydrous nitrates must be used rather than hydrated nitrates.", 1, lines_count=2,
                    mark_scheme="Hydrated nitrates release steam which condenses and creates thermal shock cracking hot boiling tube / causes basic nitrate hydrolysis [1].")
            ]
        ),

        # Q8: Potentiometric Titration Fe2+ with MnO4-
        Paper5Question(
            number=8,
            title="Planning a Potentiometric Redox Titration of Iron(II) with Permanganate",
            syllabus_ref="9701/51/M/J/20/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Potentiometric titrations are used when solutions are cloudy or coloured, preventing visual indicator observation.<br/>"
                "Plan an experiment to determine the concentration of Fe<sup>2+</sup> in an opaque mineral leachate using "
                "potentiometric titration with standardized 0.0200 mol dm<sup>-3</sup> KMnO<sub>4</sub> in acidic medium."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Draw a labelled diagram of the electrochemical apparatus including electrodes and voltmeter.", 3, lines_count=0,
                    mark_scheme="Burette containing standard KMnO4 clamped over titration beaker [1]; platinum indicator electrode and reference electrode (calomel / Ag-AgCl) immersed in solution [1]; high-resistance digital voltmeter / pH-meter connected across electrodes [1]."),
                Paper5SubQuestion("(b)", "State the role of the platinum electrode in this potentiometric measurement.", 2, lines_count=2,
                    mark_scheme="Inert electron conductor that does not participate chemically in the reaction [1]; adopts potential determined by ratio of oxidised and reduced forms in solution: [Fe3+]/[Fe2+] or [MnO4-]/[Mn2+] [1]."),
                Paper5SubQuestion("(c)", "Describe how the titration should be carried out as the equivalence point is approached.", 2, lines_count=2,
                    mark_scheme="Add KMnO4 in 1.0 cm3 increments initially; when rapid potential changes occur near equivalence, add titrant dropwise (0.05 or 0.10 cm3 increments) while stirring constantly [2]."),
                Paper5SubQuestion("(d)", "Explain how the exact equivalence volume is determined graphically from the titration data.", 2, lines_count=2,
                    mark_scheme="Plot cell potential <i>E</i> against volume <i>V</i> (inflection point of S-shaped curve) OR plot first derivative &Delta;<i>E</i>/&Delta;<i>V</i> against <i>V</i> where peak maximum corresponds to exact equivalence volume [2]."),
                Paper5SubQuestion("(e)", "Explain why hydrochloric acid cannot be used to acidify the iron solution in this titration.", 1, lines_count=2,
                    mark_scheme="KMnO4 is a strong enough oxidising agent to oxidise Cl- to toxic chlorine gas, causing an erroneously high titre [1].")
            ]
        ),

        # Q9: Iodometric Copper Determination Brass
        Paper5Question(
            number=9,
            title="Analysis of Systematic Errors in the Iodometric Determination of Copper in Brass",
            syllabus_ref="9701/52/O/N/24/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "Brass alloy was dissolved in concentrated nitric acid, neutralised with sodium carbonate, and acidified with ethanoic acid.<br/>"
                "Excess KI was added to liberate iodine: 2Cu<sup>2+</sup>(aq) + 4I<sup>-</sup>(aq) &rarr; 2CuI(s) + I<sub>2</sub>(aq).<br/>"
                "The liberated iodine was titrated with 0.100 mol dm<sup>-3</sup> Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub> using starch indicator:<br/>"
                "2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + I<sub>2</sub>(aq) &rarr; S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2I<sup>-</sup>(aq)."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "State at what point in the titration starch indicator must be added and explain why.", 2, lines_count=2,
                    mark_scheme="Add starch when solution becomes pale straw-yellow (near endpoint) [1]; if added too early, iodine binds irreversibly to starch complex, preventing sharp decolorisation and underestimating titre [1]."),
                Paper5SubQuestion("(b)", "Copper(I) iodide, CuI, precipitates as a white precipitate that adsorbs iodine on its surface. State how potassium thiocyanate (KSCN) resolves this error.", 2, lines_count=2,
                    mark_scheme="Add KSCN near endpoint; SCN- replaces adsorbed I2 on CuI surface (forming CuSCN) [1]; releases bound iodine into solution, ensuring complete reaction with thiosulfate and a sharp milky-white endpoint [1]."),
                Paper5SubQuestion("(c)", "Explain why nitric acid used to dissolve the brass must be completely removed or neutralized before adding KI.", 2, lines_count=2,
                    mark_scheme="Residual HNO3 / NO2- oxidises iodide ions to iodine (2I- + 4H+ + 2NO2- &rarr; I2 + 2NO + 2H2O) [1]; causes extra iodine liberation, resulting in falsely high copper percentage [1]."),
                Paper5SubQuestion("(d)", "Calculate the percentage apparatus uncertainty if burette reading is 24.60 cm<sup>3</sup> (&plusmn;0.05 cm<sup>3</sup>) and mass of brass is 1.450 g (&plusmn;0.001 g).", 2, lines_count=2,
                    mark_scheme="Burette % uncertainty = (0.10 / 24.60) &times; 100% = 0.407% [1]; Balance % uncertainty = (0.002 / 1.450) &times; 100% = 0.138%; Total = 0.55% [1]."),
                Paper5SubQuestion("(e)", "State the observation at the final stoichiometric endpoint in the presence of KSCN.", 2, lines_count=2,
                    mark_scheme="Disappearance of blue-black colour leaving a persistent milky-white / cream precipitate of CuSCN [2].")
            ]
        ),

        # Q10: Synthesis of Tetraamminecopper(II)
        Paper5Question(
            number=10,
            title="Planning the Synthesis and Anti-Solvent Precipitation of [Cu(NH3)4]SO4·H2O",
            syllabus_ref="9701/53/M/J/24/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Tetraamminecopper(II) sulfate monohydrate, [Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&middot;H<sub>2</sub>O, is a deep royal blue "
                "crystalline solid prepared from copper(II) sulfate pentahydrate and concentrated ammonia.<br/>"
                "CuSO<sub>4</sub>&middot;5H<sub>2</sub>O + 4NH<sub>3</sub> &rarr; [Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&middot;H<sub>2</sub>O + 4H<sub>2</sub>O.<br/>"
                "The complex is soluble in water but insoluble in ethanol."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Describe the colour and appearance changes observed as concentrated ammonia is added dropwise until in excess.", 2, lines_count=2,
                    mark_scheme="Pale blue solution forms light blue precipitate of Cu(OH)2 [1]; with excess ammonia, precipitate dissolves to give a deep royal blue solution [1]."),
                Paper5SubQuestion("(b)", "Explain the role of ethanol addition (anti-solvent precipitation) in this preparation.", 2, lines_count=2,
                    mark_scheme="Ethanol decreases the dielectric constant of the solvent mixture [1]; lowers the solubility of the ionic complex, causing [Cu(NH3)4]SO4&middot;H2O crystals to precipitate rapidly [1]."),
                Paper5SubQuestion("(c)", "Describe the filtration and washing technique to maximize yield and purity.", 3, lines_count=3,
                    mark_scheme="Filter using Buchner funnel and suction flask under vacuum [1]; wash crystals with equal-volume mixture of ethanol and concentrated ammonia (to prevent ligand loss) [1]; final wash with cold diethyl ether to facilitate drying [1]."),
                Paper5SubQuestion("(d)", "Calculate the percentage yield if 5.00 g of CuSO<sub>4</sub>&middot;5H<sub>2</sub>O (<i>M</i><sub>r</sub> = 249.6) produces 4.12 g of [Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&middot;H<sub>2</sub>O (<i>M</i><sub>r</sub> = 245.6).", 3, lines_count=3,
                    mark_scheme="Moles CuSO4&middot;5H2O = 5.00 / 249.6 = 0.02003 mol [1]; Theoretical mass = 0.02003 &times; 245.6 = 4.920 g [1]; % yield = (4.12 / 4.920) &times; 100% = 83.7% [1].")
            ]
        )
    ]

    out1 = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Inorganic Chemistry\Paper 5 (Planning & Analysis)\Past 10 Years\Urwah_Chem_Paper5_Past10Years_Inorganic_Chemistry.pdf"
    out2 = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Paper 5\Past 10 Years\Urwah_Chem_Paper5_Past10Years_Inorganic_Chemistry.pdf"
    
    os.makedirs(os.path.dirname(out1), exist_ok=True)
    os.makedirs(os.path.dirname(out2), exist_ok=True)
    
    build_paper5_pdf(out1, cfg, questions)
    
    import shutil
    shutil.copy2(out1, out2)
    print(f"[MIRRORED] Copied to {out2}")

if __name__ == "__main__":
    build_a2_past10years_inorganic()
