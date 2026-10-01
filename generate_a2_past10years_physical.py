"""
Cambridge International A Level Chemistry (9701) Paper 5 (Planning, Analysis and Evaluation)
Physical Chemistry — Past 10 Years Master Examination Suite (Past 5 Years Analysis: 2020-2024)
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

def build_a2_past10years_physical():
    styles = get_paper5_styles()
    
    cfg = Paper5PaperConfig(
        title="Physical Chemistry Practical: Paper 5 Master Suite",
        subtitle="10 Most Frequently Tested Planning, Analysis & Evaluation Questions (Past 5 Years Analysis: 2020–2024)",
        component_name="Paper 5 — Planning, Analysis and Evaluation (Past 10 Years Archive)",
        duration="2 Hours 30 Minutes",
        total_marks=100,
        candidate_name="Urwah"
    )

    questions = [
        # Q1: Faraday Constant & Electrolysis
        Paper5Question(
            number=1,
            title="Planning an Electrochemical Determination of the Faraday Constant",
            syllabus_ref="9701/52/M/J/23/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "A student plans an experiment to determine the Faraday constant, <i>F</i>, by the electrolysis of "
                "aqueous copper(II) sulfate using weighed copper electrodes.<br/>"
                "The half-equation at the cathode is: Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> &rarr; Cu(s).<br/>"
                "The relationship is given by: <i>m</i> = (<i>M</i> &times; <i>I</i> &times; <i>t</i>) / (<i>z</i> &times; <i>F</i>), "
                "where <i>m</i> is mass of copper deposited, <i>M</i> = 63.5 g mol<sup>-1</sup>, <i>I</i> is current, "
                "<i>t</i> is time in seconds, and <i>z</i> = 2."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Draw a fully labelled diagram of the complete electrical circuit and electrolytic cell required for this experiment.", 3, lines_count=0,
                    mark_scheme="Direct current power supply connected in series with variable resistor / rheostat, ammeter, and electrolytic cell [1]; copper anode and copper cathode immersed in aqueous CuSO4 [1]; cathode clearly labelled as negative electrode where mass increases [1]."),
                Paper5SubQuestion("(b)", "Identify the independent variable, dependent variable, and one variable that must be kept constant.", 3, lines_count=3,
                    mark_scheme="Independent variable: time of electrolysis <i>t</i> (or current <i>I</i>) [1]; Dependent variable: change in mass of cathode &Delta;<i>m</i> [1]; Controlled variable: constant current / temperature of solution / surface area of immersion [1]."),
                Paper5SubQuestion("(c)", "State the procedure to clean and dry the cathode before and after electrolysis to ensure mass accuracy.", 2, lines_count=3,
                    mark_scheme="Clean electrode surface with fine emery paper / sand paper before electrolysis to remove oxide layer, rinse with distilled water [1]; after electrolysis, wash gently with propanone / ethanol and allow to dry in a desiccator / gentle warm air stream without dislodging deposit [1]."),
                Paper5SubQuestion("(d)", "Explain how the student should use the measured values to calculate an experimental value for <i>F</i>.", 2, lines_count=2,
                    mark_scheme="Rearrange formula: <i>F</i> = (<i>M</i> &times; <i>I</i> &times; <i>t</i>) / (2 &times; &Delta;<i>m</i>) [1]; substitute measured current (A), time (s), and mass gained (g) to evaluate <i>F</i> in C mol<sup>-1</sup> [1].")
            ]
        ),

        # Q2: Kinetics Persulfate-Iodide
        Paper5Question(
            number=2,
            title="Analysis and Graphical Evaluation of Persulfate–Iodide Reaction Kinetics",
            syllabus_ref="9701/51/O/N/23/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "The rate of oxidation of iodide ions by peroxodisulfate ions was investigated using the iodine clock method:<br/>"
                "S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2I<sup>-</sup>(aq) &rarr; 2SO<sub>4</sub><sup>2-</sup>(aq) + I<sub>2</sub>(aq).<br/>"
                "A small fixed amount of sodium thiosulfate and starch indicator were added. The time <i>t</i> taken for the blue-black "
                "color to appear was recorded at various concentrations of S<sub>2</sub>O<sub>8</sub><sup>2-</sup>, with [I<sup>-</sup>] kept in large excess."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain why 1/<i>t</i> is directly proportional to the initial rate of reaction.", 2, lines_count=2,
                    mark_scheme="The amount of iodine produced to react with the fixed amount of thiosulfate is constant (&Delta;[I2] is constant) [1]; initial rate = &Delta;[I2]/&Delta;<i>t</i> &prop; 1/<i>t</i> [1]."),
                Paper5SubQuestion("(b)", "The student plotted log(1/<i>t</i>) on the y-axis against log[S<sub>2</sub>O<sub>8</sub><sup>2-</sup>] on the x-axis. State how the order of reaction with respect to S<sub>2</sub>O<sub>8</sub><sup>2-</sup> is determined from this graph.", 2, lines_count=2,
                    mark_scheme="Rate = <i>k</i>'[S2O8^2-]^<i>m</i> &rArr; log(rate) = log(<i>k</i>') + <i>m</i> log[S2O8^2-] [1]; the order <i>m</i> is equal to the gradient of the best-fit straight line [1]."),
                Paper5SubQuestion("(c)", "The gradient of the line was found to be +0.97. Deduce the order with respect to S<sub>2</sub>O<sub>8</sub><sup>2-</sup> and explain the significance of the 0.03 deviation.", 2, lines_count=2,
                    mark_scheme="Order is 1 (first order) [1]; deviation of 0.03 is within experimental / timing uncertainty of the clock endpoint [1]."),
                Paper5SubQuestion("(d)", "Identify one anomalous result on the student's graph and suggest a specific experimental error that could have caused the blue-black color to appear too slowly.", 2, lines_count=3,
                    mark_scheme="Identify point lying below the line of best fit (longer time <i>t</i>) [1]; cause: temperature decreased during run / student inadvertently added extra thiosulfate volume / delayed starch addition [1]."),
                Paper5SubQuestion("(e)", "Suggest how the precision of timing the endpoint could be significantly improved.", 2, lines_count=2,
                    mark_scheme="Use a colorimeter / spectrophotometer coupled to a datalogger [1]; eliminate subjective visual judgment of colour transition [1].")
            ]
        ),

        # Q3: Arrhenius Activation Energy
        Paper5Question(
            number=3,
            title="Planning Activation Energy Determination via Arrhenius Temperature Kinetics",
            syllabus_ref="9701/52/M/J/22/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "The Arrhenius equation describes the variation of rate constant <i>k</i> with absolute temperature <i>T</i>:<br/>"
                "ln <i>k</i> = ln <i>A</i> - (<i>E</i><sub>a</sub> / <i>RT</i>).<br/>"
                "For a reaction where initial rate &prop; 1/<i>t</i>, the equation can be written as: ln(1/<i>t</i>) = -(<i>E</i><sub>a</sub> / <i>R</i>)(1/<i>T</i>) + constant.<br/>"
                "Plan an investigation to determine the activation energy, <i>E</i><sub>a</sub>, of the reaction between sodium thiosulfate "
                "and hydrochloric acid over the temperature range 20 &deg;C to 60 &deg;C."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Specify the apparatus and temperature control method to ensure thermal equilibrium between reactants before mixing.", 3, lines_count=3,
                    mark_scheme="Thermostatically controlled water bath with stirrer [1]; separate boiling tubes / conical flasks containing Na2S2O3 and HCl placed in water bath for at least 5 minutes [1]; thermometer to measure temperature of reactant mixture immediately before mixing [1]."),
                Paper5SubQuestion("(b)", "Describe the step-by-step procedure to measure the reaction rate proxy at each temperature.", 3, lines_count=4,
                    mark_scheme="Place conical flask over printed black cross on white tile [1]; mix equal specified volumes of preheated solutions and immediately start stopwatch [1]; swirl once, view vertically downwards through solution, and stop stopwatch when cross is obscured by precipitated sulfur [1]."),
                Paper5SubQuestion("(c)", "State the columns that must be included in the student's processed data table.", 2, lines_count=2,
                    mark_scheme="Columns for: Temperature <i>T</i> in &deg;C, Absolute temperature <i>T</i> in K, 1/<i>T</i> in K<sup>-1</sup>, Time <i>t</i> in s, 1/<i>t</i> in s<sup>-1</sup>, and ln(1/<i>t</i>) [2]."),
                Paper5SubQuestion("(d)", "Explain how <i>E</i><sub>a</sub> is calculated from the gradient of the graph of ln(1/<i>t</i>) against 1/<i>T</i>.", 2, lines_count=2,
                    mark_scheme="Gradient = -<i>E</i><sub>a</sub> / <i>R</i> [1]; <i>E</i><sub>a</sub> = -gradient &times; 8.314 J K<sup>-1</sup> mol<sup>-1</sup> (convert to kJ mol<sup>-1</sup> by dividing by 1000) [1].")
            ]
        ),

        # Q4: Solubility Product Ksp of Ca(OH)2
        Paper5Question(
            number=4,
            title="Analysis and Evaluation of the Solubility Product (Ksp) of Calcium Hydroxide",
            syllabus_ref="9701/53/O/N/22/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "A saturated solution of calcium hydroxide was prepared at 298 K according to the equilibrium:<br/>"
                "Ca(OH)<sub>2</sub>(s) &rightleftharpoons; Ca<sup>2+</sup>(aq) + 2OH<sup>-</sup>(aq).<br/>"
                "The solubility product expression is: <i>K</i><sub>sp</sub> = [Ca<sup>2+</sup>][OH<sup>-</sup>]<sup>2</sup>.<br/>"
                "A 25.0 cm<sup>3</sup> portion of the filtered saturated solution was titrated against 0.0500 mol dm<sup>-3</sup> HCl "
                "using phenolphthalein indicator."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain why the saturated solution must be filtered before titration, and state a precaution during filtration.", 2, lines_count=2,
                    mark_scheme="Filter to remove undissolved solid Ca(OH)2 which would otherwise dissolve during titration and react with acid [1]; discard the first few cm3 of filtrate because filter paper can adsorb solute ions [1]."),
                Paper5SubQuestion("(b)", "If the mean titre of 0.0500 mol dm<sup>-3</sup> HCl is 17.40 cm<sup>3</sup>, calculate [OH<sup>-</sup>] and [Ca<sup>2+</sup>] in the saturated solution.", 3, lines_count=4,
                    mark_scheme="Moles HCl = 0.0500 &times; (17.40 / 1000) = 8.70 &times; 10^-4 mol [1]; Moles OH- in 25.0 cm3 = 8.70 &times; 10^-4 mol &rArr; [OH-] = 8.70 &times; 10^-4 / 0.0250 = 0.0348 mol dm^-3 [1]; [Ca2+] = 0.5 &times; [OH-] = 0.0174 mol dm^-3 [1]."),
                Paper5SubQuestion("(c)", "Calculate the numerical value of <i>K</i><sub>sp</sub> for Ca(OH)<sub>2</sub> at 298 K and state its units.", 3, lines_count=3,
                    mark_scheme="<i>K</i>sp = [Ca2+][OH-]^2 = (0.0174) &times; (0.0348)^2 = 2.11 &times; 10^-5 [2]; units: mol^3 dm^-9 [1]."),
                Paper5SubQuestion("(d)", "Predict and explain the effect on the calculated <i>K</i><sub>sp</sub> if the solution absorbed atmospheric CO<sub>2</sub> prior to titration.", 2, lines_count=2,
                    mark_scheme="CO2 reacts with OH- to form CaCO3 precipitate: Ca(OH)2 + CO2 &rarr; CaCO3 + H2O [1]; reduces [OH-] in solution, requiring smaller titre of HCl, leading to an underestimated <i>K</i>sp [1].")
            ]
        ),

        # Q5: Enthalpy of Solution Hess's Law
        Paper5Question(
            number=5,
            title="Planning Calorimetric Determination of the Hydration Enthalpy via Hess's Law",
            syllabus_ref="9701/51/M/J/24/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "Hydrated magnesium chloride, MgCl<sub>2</sub>&middot;6H<sub>2</sub>O, cannot have its enthalpy of hydration "
                "measured directly by calorimetry.<br/>"
                "However, the enthalpy of solution of anhydrous MgCl<sub>2</sub>(s) (&Delta;<i>H</i><sub>1</sub>) and "
                "the enthalpy of solution of hydrated MgCl<sub>2</sub>&middot;6H<sub>2</sub>O(s) (&Delta;<i>H</i><sub>2</sub>) can both be measured.<br/>"
                "Plan two calorimetry experiments using a simple polystyrene cup calorimeter to determine &Delta;<i>H</i><sub>1</sub> and &Delta;<i>H</i><sub>2</sub>."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Draw a Hess's Law energy cycle connecting anhydrous MgCl<sub>2</sub>(s), hydrated MgCl<sub>2</sub>&middot;6H<sub>2</sub>O(s), and MgCl<sub>2</sub>(aq).", 3, lines_count=0,
                    mark_scheme="Anhydrous MgCl2(s) + 6H2O(l) &rarr; MgCl2&middot;6H2O(s) (&Delta;H_hyd) [1]; MgCl2(s) + aq &rarr; MgCl2(aq) (&Delta;H1) [1]; MgCl2&middot;6H2O(s) + aq &rarr; MgCl2(aq) (&Delta;H2), correctly oriented with &Delta;H_hyd = &Delta;H1 - &Delta;H2 [1]."),
                Paper5SubQuestion("(b)", "State the mass of water and mass of salts to use to ensure a measurable temperature change of at least 5 &deg;C without exceeding solubility limits.", 2, lines_count=3,
                    mark_scheme="50.0 cm3 / 50.0 g of distilled water [1]; approximately 0.025 to 0.050 mol of solid (e.g. 2.4 g to 4.8 g anhydrous MgCl2, and stoichiometric equivalent 5.1 g to 10.2 g MgCl2&middot;6H2O) [1]."),
                Paper5SubQuestion("(c)", "Describe how cooling curve graphical extrapolation should be used to correct for heat loss.", 3, lines_count=3,
                    mark_scheme="Record temperature of water every 30 seconds for 3 minutes before addition of solid [1]; add solid at minute 3.5, stir continuously, record temperature every 30 seconds from minute 4 to minute 10 [1]; plot temperature vs time and extrapolate cooling curve back to time of mixing (minute 3.5) to find theoretical maximum temperature T_max [1]."),
                Paper5SubQuestion("(d)", "Explain why anhydrous MgCl<sub>2</sub> must be stored in a tightly stoppered container until immediately before weighing.", 2, lines_count=2,
                    mark_scheme="Anhydrous MgCl2 is highly hygroscopic / deliquescent [1]; absorbs water vapor from air, causing error in calculated moles and releasing partial hydration heat before calorimetry [1].")
            ]
        ),

        # Q6: Decomposition Kinetics of H2O2
        Paper5Question(
            number=6,
            title="Analysis and Evaluation of the Catalytic Decomposition of Hydrogen Peroxide",
            syllabus_ref="9701/52/O/N/21/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "A student investigated the catalytic decomposition of hydrogen peroxide:<br/>"
                "2H<sub>2</sub>O<sub>2</sub>(aq) &rarr; 2H<sub>2</sub>O(l) + O<sub>2</sub>(g), catalysed by solid manganese(IV) oxide, MnO<sub>2</sub>.<br/>"
                "The volume of oxygen evolved was collected in a 100 cm<sup>3</sup> gas syringe and recorded every 30 seconds."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Explain how the volume of O<sub>2</sub> evolved at time <i>t</i>, <i>V</i><sub>t</sub>, and the final volume at infinity, <i>V</i><sub>&infin;</sub>, are used to find [H<sub>2</sub>O<sub>2</sub>] remaining.", 2, lines_count=2,
                    mark_scheme="<i>V</i>_&infin; represents initial amount of H2O2 [1]; (<i>V</i>_&infin; - <i>V</i>_t) is directly proportional to concentration of H2O2 remaining at time <i>t</i> [1]."),
                Paper5SubQuestion("(b)", "Describe how successive half-lives (<i>t</i><sub>1/2</sub>) are determined from a graph of (<i>V</i><sub>&infin;</sub> - <i>V</i><sub>t</sub>) against time.", 2, lines_count=2,
                    mark_scheme="Measure time taken for (<i>V</i>_&infin; - <i>V</i>_t) to fall to half its initial value (t1/2_1) [1]; then measure time taken to halve again (t1/2_2); if t1/2 is constant, the reaction is first-order [1]."),
                Paper5SubQuestion("(c)", "State two reasons why the recorded volume of oxygen gas might be lower than the theoretical volume.", 2, lines_count=2,
                    mark_scheme="Oxygen gas has slight solubility in aqueous solution [1]; gas leakage around the syringe plunger / delivery tube connection [1]."),
                Paper5SubQuestion("(d)", "Explain the effect of doubling the mass of MnO<sub>2</sub> catalyst on the rate of reaction and on the final volume <i>V</i><sub>&infin;</sub>.", 2, lines_count=2,
                    mark_scheme="Doubling catalyst mass doubles available active surface area, doubling initial rate of reaction [1]; final volume <i>V</i>_&infin; remains unchanged because catalyst does not alter stoichiometry / moles of reactant [1]."),
                Paper5SubQuestion("(e)", "Suggest how the reaction can be stopped instantly if an aliquot method were used instead of continuous gas collection.", 2, lines_count=2,
                    mark_scheme="Rapid filtration to remove solid catalyst / quenching by adding excess ice-cold sulfuric acid [2].")
            ]
        ),

        # Q7: Partition Coefficient Kpc
        Paper5Question(
            number=7,
            title="Planning the Determination of Partition Coefficient (Kpc) of Ethanoic Acid",
            syllabus_ref="9701/53/M/J/21/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "When ethanoic acid is shaken with water and an immiscible organic solvent such as octan-1-ol, it distributes "
                "between the two layers according to the partition equilibrium:<br/>"
                "CH<sub>3</sub>COOH(aq) &rightleftharpoons; CH<sub>3</sub>COOH(octan-1-ol).<br/>"
                "The partition coefficient is given by: <i>K</i><sub>pc</sub> = [CH<sub>3</sub>COOH]<sub>org</sub> / [CH<sub>3</sub>COOH]<sub>aq</sub>.<br/>"
                "Plan an experiment to determine <i>K</i><sub>pc</sub> at room temperature."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Describe how the two layers should be mixed and brought to equilibrium in a separating funnel.", 2, lines_count=3,
                    mark_scheme="Add measured volumes of aqueous ethanoic acid and octan-1-ol to separating funnel [1]; stopper, invert and shake vigorously for 5 minutes, periodically opening tap to release pressure, then clamp in retort stand and allow distinct layers to separate fully [1]."),
                Paper5SubQuestion("(b)", "Explain how a sample of the lower aqueous layer should be obtained without contamination by the upper organic layer.", 2, lines_count=2,
                    mark_scheme="Remove stopper, open tap slowly and run out lower aqueous layer into clean beaker, discarding small boundary layer [2]."),
                Paper5SubQuestion("(c)", "State the volumetric titration method to determine the concentration of ethanoic acid in the separated layers.", 3, lines_count=3,
                    mark_scheme="Pipette 10.0 cm3 aliquot of each layer into separate conical flasks [1]; titrate with standardized 0.100 mol dm^-3 NaOH solution [1]; use phenolphthalein indicator (colourless to permanent pale pink endpoint) [1]."),
                Paper5SubQuestion("(d)", "State the safety precautions required when handling octan-1-ol and concentrated ethanoic acid.", 2, lines_count=2,
                    mark_scheme="Wear nitrile gloves and eye protection (ethanoic acid is corrosive); handle organic solvent in fume cupboard away from naked flames (flammable vapour) [2]."),
                Paper5SubQuestion("(e)", "State the assumption made regarding the molecular state of ethanoic acid in both solvents.", 1, lines_count=2,
                    mark_scheme="Assumes ethanoic acid has the same molecular form (monomer) in both water and the organic solvent (does not dimerise significantly) [1].")
            ]
        ),

        # Q8: Nernst Equation & Cell Potentials
        Paper5Question(
            number=8,
            title="Quantitative Analysis of Cell Potentials and Verification of the Nernst Equation",
            syllabus_ref="9701/51/O/N/24/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "A student investigated the relationship between copper half-cell potential and [Cu<sup>2+</sup>(aq)] using "
                "a cell consisting of a Cu<sup>2+</sup>/Cu half-cell and a standard hydrogen electrode (SHE).<br/>"
                "According to the Nernst equation at 298 K: <i>E</i> = <i>E</i><sup>&deg;</sup> + (0.059 / <i>z</i>) log[Cu<sup>2+</sup>].<br/>"
                "The table below shows the measured cell potentials for five different concentrations of Cu<sup>2+</sup>."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Complete the table by calculating log[Cu<sup>2+</sup>] to two decimal places.", 2, lines_count=0,
                    table_data=make_simple_table(
                        ["[Cu2+] / mol dm-3", "log[Cu2+]", "Ecell / V"],
                        [["1.00", "0.00", "+0.340"],
                         ["0.10", "-1.00", "+0.311"],
                         ["0.010", "-2.00", "+0.281"],
                         ["0.0010", "-3.00", "+0.250"],
                         ["0.00010", "-4.00", "+0.222"]],
                        [160, 160, 160], styles
                    ),
                    mark_scheme="All log values correct: 0.00, -1.00, -2.00, -3.00, -4.00 [2]."),
                Paper5SubQuestion("(b)", "State what graph should be plotted to confirm the validity of the Nernst equation.", 2, lines_count=2,
                    mark_scheme="Plot <i>E</i>cell on y-axis against log[Cu2+] on x-axis [2]."),
                Paper5SubQuestion("(c)", "Calculate the theoretical gradient of this graph for <i>z</i> = 2.", 2, lines_count=2,
                    mark_scheme="Theoretical gradient = 0.059 / 2 = +0.0295 V (or +0.030 V per decade) [2]."),
                Paper5SubQuestion("(d)", "Explain how the standard electrode potential <i>E</i><sup>&deg;</sup>(Cu<sup>2+</sup>/Cu) is determined from the graph.", 2, lines_count=2,
                    mark_scheme="<i>E</i>^&deg; is the y-intercept where log[Cu2+] = 0.00 (i.e. [Cu2+] = 1.00 mol dm^-3) [2]."),
                Paper5SubQuestion("(e)", "Explain why a high-resistance digital voltmeter must be used to measure cell potential.", 2, lines_count=2,
                    mark_scheme="Prevents any significant current from flowing through the cell [1]; ensures the concentrations of ions at the electrode surface remain unchanged (retains equilibrium conditions) [1].")
            ]
        ),

        # Q9: Dumas Method Molar Mass
        Paper5Question(
            number=9,
            title="Planning the Determination of Molar Mass of a Volatile Liquid via the Dumas Method",
            syllabus_ref="9701/52/M/J/20/Q1",
            question_type="PLANNING",
            total_marks=10,
            context_intro=(
                "The molar mass of an unknown volatile organic liquid can be determined by vaporising a known mass inside "
                "a gas syringe placed inside a temperature-controlled heating jacket or water oven.<br/>"
                "The ideal gas equation relates the variables: <i>pV</i> = (<i>m</i>/<i>M</i>)<i>RT</i> &rArr; <i>M</i> = <i>mRT</i> / <i>pV</i>.<br/>"
                "Plan an experiment to determine the molar mass of liquid hexane (boiling point 69 &deg;C)."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Specify the apparatus setup to inject a micro-sample of liquid into the gas syringe without gas leakage.", 2, lines_count=3,
                    mark_scheme="Self-sealing rubber septum fitted to syringe nozzle [1]; hypodermic micro-syringe used to puncture septum and inject volatile liquid [1]."),
                Paper5SubQuestion("(b)", "Describe the mass measurement technique using weighing by difference.", 2, lines_count=2,
                    mark_scheme="Weigh micro-syringe containing hexane on balance (3 or 4 decimal places) [1]; inject liquid into gas syringe, re-weigh empty micro-syringe; mass injected = initial mass - final mass [1]."),
                Paper5SubQuestion("(c)", "State the temperature at which the syringe oven must be maintained and explain why.", 2, lines_count=2,
                    mark_scheme="Maintain temperature well above boiling point of hexane (e.g. 85 &deg;C to 95 &deg;C) [1]; ensures hexane vaporises completely and behaves ideally as a gas [1]."),
                Paper5SubQuestion("(d)", "List the four experimental measurements required to calculate <i>M</i>.", 2, lines_count=2,
                    mark_scheme="1. Mass of injected liquid <i>m</i> (g); 2. Volume of vapor <i>V</i> (cm3 / m3); 3. Temperature of oven <i>T</i> (K); 4. Atmospheric pressure <i>p</i> (Pa) [2]."),
                Paper5SubQuestion("(e)", "Explain the effect on the calculated molar mass if the vapor does not behave ideally due to significant intermolecular forces.", 2, lines_count=2,
                    mark_scheme="Intermolecular attractions cause the measured volume <i>V</i> to be smaller than ideal [1]; since <i>M</i> &prop; 1/<i>V</i>, the calculated molar mass will be higher than true value [1].")
            ]
        ),

        # Q10: Error Propagation Calorimetry
        Paper5Question(
            number=10,
            title="Analysis of Apparatus Errors, Anomalies, and Standard Deviation in Calorimetry",
            syllabus_ref="9701/51/M/J/23/Q2",
            question_type="ANALYSIS & EVALUATION",
            total_marks=10,
            context_intro=(
                "A student carries out repeated calorimetric runs to determine the enthalpy of neutralization between "
                "25.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> NaOH and 25.0 cm<sup>3</sup> of 2.00 mol dm<sup>-3</sup> HCl.<br/>"
                "Apparatus used: 50 cm<sup>3</sup> measuring cylinder (&plusmn;0.5 cm<sup>3</sup>), thermometer graduated in 0.2 &deg;C (&plusmn;0.1 &deg;C)."
            ),
            subquestions=[
                Paper5SubQuestion("(a)", "Calculate the percentage uncertainty in measuring 25.0 cm<sup>3</sup> of solution with the measuring cylinder.", 2, lines_count=2,
                    mark_scheme="% uncertainty = (0.5 / 25.0) &times; 100% = 2.0% [2]."),
                Paper5SubQuestion("(b)", "If the temperature rise recorded was &Delta;<i>T</i> = 13.4 &deg;C, calculate the percentage uncertainty in &Delta;<i>T</i>.", 2, lines_count=2,
                    mark_scheme="Total reading error = 2 &times; 0.1 = 0.2 &deg;C; % uncertainty = (0.2 / 13.4) &times; 100% = 1.49% (or 1.5%) [2]."),
                Paper5SubQuestion("(c)", "Calculate the overall combined apparatus percentage uncertainty for this experiment.", 2, lines_count=2,
                    mark_scheme="Total % uncertainty = 2.0% (cylinder 1) + 2.0% (cylinder 2) + 1.49% (&Delta;T) = 5.49% (or 5.5%) [2]."),
                Paper5SubQuestion("(d)", "The student obtained neutralization enthalpies: -54.2, -58.1, -53.9, -54.0 kJ mol<sup>-1</sup>. Identify the anomaly and calculate the mean of concordant values.", 2, lines_count=3,
                    mark_scheme="Anomaly: -58.1 kJ mol^-1 [1]; Mean concordant = (-54.2 - 53.9 - 54.0) / 3 = -54.03 kJ mol^-1 (accept -54.0 kJ mol^-1) [1]."),
                Paper5SubQuestion("(e)", "Suggest two apparatus modifications that would significantly improve the accuracy of the result.", 2, lines_count=2,
                    mark_scheme="Use a volumetric pipette / burette instead of measuring cylinders for solution volumes [1]; use a vacuum Dewar flask / expanded polystyrene with lid to minimize heat loss to surroundings [1].")
            ]
        )
    ]

    # Save to both target locations
    out1 = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 5 (Planning & Analysis)\Past 10 Years\Urwah_Chem_Paper5_Past10Years_Physical_Chemistry.pdf"
    out2 = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Paper 5\Past 10 Years\Urwah_Chem_Paper5_Past10Years_Physical_Chemistry.pdf"
    
    os.makedirs(os.path.dirname(out1), exist_ok=True)
    os.makedirs(os.path.dirname(out2), exist_ok=True)
    
    build_paper5_pdf(out1, cfg, questions)
    
    import shutil
    shutil.copy2(out1, out2)
    print(f"[MIRRORED] Copied to {out2}")

if __name__ == "__main__":
    build_a2_past10years_physical()
