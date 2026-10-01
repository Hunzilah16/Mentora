"""
Cambridge International A Level Chemistry (9701) — A2 Suite
PAPER 5: PLANNING, ANALYSIS AND EVALUATION (PHYSICAL CHEMISTRY)
Generates:
Urwah_Chem_Paper5_Planning_Physical_Chemistry.pdf

Candidate: Urwah | Mentora Academy
"""
import os
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from build_paper5_pdf import (
    Paper5PaperConfig, Paper5Question, Paper5SubQuestion, build_paper5_pdf,
    COLOR_NAVY, COLOR_CRIMSON, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_DARK
)

def create_kinetics_table():
    styles = getSampleStyleSheet()
    header_style = ParagraphStyle('TH', fontName='Poppins-Bold', fontSize=7.0, leading=9, textColor=COLOR_NAVY, alignment=1)
    cell_style = ParagraphStyle('TC', fontName='Poppins', fontSize=7.0, leading=9, textColor=COLOR_DARK, alignment=1)
    cell_bold = ParagraphStyle('TCB', fontName='Poppins-Bold', fontSize=7.0, leading=9, textColor=COLOR_DARK, alignment=1)

    table_data = [
        [
            Paragraph("<b>Expt</b>", header_style),
            Paragraph("<b>Temperature<br/>θ / °C</b>", header_style),
            Paragraph("<b>Temperature<br/>T / K</b>", header_style),
            Paragraph("<b>(1 / T) x 10³<br/>/ K⁻¹</b>", header_style),
            Paragraph("<b>Time<br/>t / s</b>", header_style),
            Paragraph("<b>(1 / t)<br/>/ s⁻¹</b>", header_style),
            Paragraph("<b>ln(1 / t)<br/>[t in s]</b>", header_style)
        ],
        [Paragraph("1", cell_style), Paragraph("20.0", cell_style), Paragraph("293.2", cell_bold), Paragraph("3.411", cell_bold), Paragraph("88.4", cell_style), Paragraph("0.0113", cell_bold), Paragraph("-4.48", cell_bold)],
        [Paragraph("2", cell_style), Paragraph("25.0", cell_style), Paragraph("298.2", cell_bold), Paragraph("3.353", cell_bold), Paragraph("62.2", cell_style), Paragraph("0.0161", cell_bold), Paragraph("-4.13", cell_bold)],
        [Paragraph("3", cell_style), Paragraph("30.0", cell_style), Paragraph("303.2", cell_bold), Paragraph("3.298", cell_bold), Paragraph("44.6", cell_style), Paragraph("0.0224", cell_bold), Paragraph("-3.80", cell_bold)],
        [Paragraph("4", cell_style), Paragraph("35.0", cell_style), Paragraph("308.2", cell_bold), Paragraph("3.245", cell_bold), Paragraph("32.5", cell_style), Paragraph("0.0308", cell_bold), Paragraph("-3.48", cell_bold)],
        [Paragraph("5", cell_style), Paragraph("40.0", cell_style), Paragraph("313.2", cell_bold), Paragraph("3.193", cell_bold), Paragraph("23.8", cell_style), Paragraph("0.0420", cell_bold), Paragraph("-3.17", cell_bold)],
        [Paragraph("6", cell_style), Paragraph("45.0", cell_style), Paragraph("318.2", cell_bold), Paragraph("3.143", cell_bold), Paragraph("18.0", cell_style), Paragraph("0.0556", cell_bold), Paragraph("-2.89", cell_bold)],
        [Paragraph("7", cell_style), Paragraph("50.0", cell_style), Paragraph("323.2", cell_bold), Paragraph("3.094", cell_bold), Paragraph("14.5", cell_style), Paragraph("0.0690", cell_bold), Paragraph("-2.67", cell_bold)],
        [Paragraph("8", cell_style), Paragraph("55.0", cell_style), Paragraph("328.2", cell_bold), Paragraph("3.047", cell_bold), Paragraph("12.4", cell_style), Paragraph("0.0806", cell_bold), Paragraph("-2.52", cell_bold)],
    ]

    t = Table(table_data, colWidths=[35, 75, 75, 85, 65, 75, 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.9, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t

def build_physical_paper5():
    out_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Physical Chemistry\Paper 5 (Planning & Analysis)"
    out_path = os.path.join(out_dir, "Urwah_Chem_Paper5_Planning_Physical_Chemistry.pdf")

    config = Paper5PaperConfig(
        title="Physical Chemistry Experimental Suite",
        subtitle="Planning, Analysis and Evaluation · Faraday Constant · Arrhenius Activation Energy",
        component_name="Paper 5 — Planning, Analysis and Evaluation",
        duration="1 Hour 15 Minutes",
        total_marks=30,
        candidate_name="Urwah",
        centre_number="PK082",
        candidate_number="0142"
    )

    # ─────────────────────────────────────────────────────────────────────────
    # QUESTION 1: PLANNING (15 MARKS)
    # ─────────────────────────────────────────────────────────────────────────
    q1 = Paper5Question(
        number=1,
        title="Planning an Electrochemical Determination of the Faraday and Avogadro Constants",
        syllabus_ref="9701/52/M/J/23/Q1 · Syllabus 24.1",
        question_type="PLANNING",
        total_marks=15,
        context_intro="An electric current passing through an aqueous solution of copper(II) sulfate, CuSO₄(aq), causes copper atoms to dissolve from the anode and copper ions to be deposited at the cathode according to the reduction half-equation:<br/><b>Cu²⁺(aq) + 2e⁻ → Cu(s)</b><br/>"
                      "The Faraday constant, F, represents the electric charge carried by one mole of electrons, and is related to the Avogadro constant, L, and the elementary charge, e (1.602 x 10⁻¹⁹ C), by the fundamental equation:<br/>"
                      "<b>F = L · e</b><br/>"
                      "You are required to plan an experimental procedure to determine accurate experimental values of the Faraday constant, F, and the Avogadro constant, L, by measuring the mass of copper deposited at the cathode when a constant current is passed through aqueous copper(II) sulfate for a measured time interval.<br/>"
                      "You are provided with: pure copper foil electrodes, 1.0 mol dm⁻³ aqueous copper(II) sulfate, a variable DC power supply (0–12 V), an ammeter, a rheostat (variable resistor), an electric switch, connecting leads, a digital stopwatch, an analytical balance (± 0.001 g), emery paper, distilled water, and propanone.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="Identify:<br/>"
                     "(i) the independent variable in this investigation<br/>"
                     "(ii) the dependent variable in this investigation<br/>"
                     "(iii) two variables that must be controlled to ensure reliable, accurate results.",
                marks=3,
                lines_count=4,
                mark_scheme="(i) Time of electrolysis, t (or current, I) [1]<br/>"
                            "(ii) Mass of copper deposited on the cathode, Δm [1]<br/>"
                            "(iii) Controlled variables: Current I maintained strictly constant (using rheostat), temperature of electrolyte, concentration/volume of CuSO4 solution, depth of immersion of electrodes [1]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="Draw a fully labelled circuit and apparatus diagram of the electrolytic cell suitable for this experiment. Include all electrical components necessary to control, maintain, and measure a steady electric current.",
                marks=3,
                lines_count=5,
                mark_scheme="Fully labelled circuit showing DC power supply in series with ammeter, rheostat / variable resistor, switch, and electrolytic cell [1];<br/>"
                            "Cell correctly labelled with cathode (-) and anode (+) immersed in aqueous copper(II) sulfate [1];<br/>"
                            "Correct polarity indicated (cathode connected to negative terminal of DC supply, anode to positive terminal) [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="Describe a detailed step-by-step procedure for preparing, cleaning, drying, and weighing the copper cathode before and after the electrolysis to prevent systematic errors in mass measurement.",
                marks=3,
                lines_count=5,
                mark_scheme="Before electrolysis: Clean copper electrode with emery paper to remove surface oxide layer, rinse with distilled water, rinse with propanone to remove water, dry thoroughly in a warm oven/stream of air, and weigh accurately to 3 d.p. on analytical balance [1];<br/>"
                            "During electrolysis: Start stopwatch simultaneously with closing switch, monitor ammeter continuously, adjust rheostat to keep current strictly constant [1];<br/>"
                            "After electrolysis: Switch off circuit and record exact elapsed time; carefully remove cathode, wash gently with distilled water (avoid dislodging deposit), rinse with propanone, dry thoroughly, and re-weigh to 3 d.p. to determine mass increase Δm [1]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Show clearly how your experimental measurements of current (I), time (t), mass of copper deposited (Δm), relative atomic mass of copper (Ar = 63.55), and electron charge (e = 1.602 x 10⁻¹⁹ C) are mathematically processed to calculate:<br/>"
                     "(i) the Faraday constant, F<br/>"
                     "(ii) the Avogadro constant, L.",
                marks=3,
                lines_count=5,
                mark_scheme="(i) Total charge Q = I · t (in coulombs) [1]; Moles of Cu = Δm / 63.55; Moles of electrons required = 2 · (Δm / 63.55); Faraday constant F = Q / n(e⁻) = (I · t · 63.55) / (2 · Δm) [1];<br/>"
                            "(ii) Avogadro constant L = F / e = F / (1.602 x 10⁻¹⁹ C) [1]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="State two significant laboratory hazards associated with the chemicals used in this experiment, and state the specific safety precautions required to minimize risk.",
                marks=3,
                lines_count=4,
                mark_scheme="Hazard 1: Copper(II) sulfate is harmful if swallowed and causes skin/eye irritation [1]; Precaution: Wear nitrile gloves and safety goggles, wash skin immediately if contact occurs [1];<br/>"
                            "Hazard 2: Propanone is highly volatile and flammable [1]; Precaution: Ensure no open flames/Bunsen burners nearby, handle in a well-ventilated laboratory / fume cupboard [1]."
            )
        ]
    )

    # ─────────────────────────────────────────────────────────────────────────
    # QUESTION 2: ANALYSIS & EVALUATION (15 MARKS)
    # ─────────────────────────────────────────────────────────────────────────
    q2 = Paper5Question(
        number=2,
        title="Kinetics and Activation Energy Determination of the Peroxydisulfate–Iodide Reaction",
        syllabus_ref="9701/51/O/N/23/Q2 · Syllabus 26.2",
        question_type="ANALYSIS & EVALUATION",
        total_marks=15,
        context_intro="A student investigated the effect of temperature on the rate of reaction between peroxydisulfate ions and iodide ions:<br/>"
                      "<b>S₂O₈²⁻(aq) + 2I⁻(aq) → 2SO₄²⁻(aq) + I₂(aq)</b><br/>"
                      "The reaction was monitored using the iodine clock method. A small, fixed amount of sodium thiosulfate, Na₂S₂O₃(aq), and starch indicator were added to the reaction mixture. The iodine produced reacts instantaneously with thiosulfate until all thiosulfate is consumed, after which free iodine reacts with starch to produce an intense blue-black coloration.<br/>"
                      "The time, t, taken for the blue-black color to appear was recorded at eight different temperatures between 20.0 °C and 55.0 °C. The rate of reaction is directly proportional to (1 / t).<br/>"
                      "The temperature dependence of the rate constant is described by the Arrhenius equation in linear form:<br/>"
                      "<b>ln(1 / t) = - (Ea / R) · (1 / T) + constant</b><br/>"
                      "where Ea is the activation energy in J mol⁻¹, R = 8.314 J K⁻¹ mol⁻¹, and T is absolute temperature in Kelvin.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="Complete the table of results below by calculating the values of absolute temperature T / K, (1 / T) x 10³ / K⁻¹, (1 / t) / s⁻¹, and ln(1 / t). Record all calculated values to appropriate significant figures.",
                marks=3,
                lines_count=0,
                table_data=create_kinetics_table(),
                mark_scheme="All T / K correctly calculated (θ + 273.2) to 1 d.p. [1];<br/>"
                            "All (1 / T) x 10³ calculated correctly to 3 or 4 significant figures [1];<br/>"
                            "All (1 / t) and ln(1 / t) values correctly calculated to 3 significant figures with correct negative signs [1]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="A graph of ln(1 / t) on the vertical y-axis against (1 / T) x 10³ / K⁻¹ on the horizontal x-axis was plotted.<br/>"
                     "(i) Describe the expected shape of the graph.<br/>"
                     "(ii) Explain how a student identifies an anomalous data point on this graph.<br/>"
                     "(iii) State the correct procedure for handling an anomalous data point when drawing the line of best fit.",
                marks=3,
                lines_count=4,
                mark_scheme="(i) Straight line of negative slope (downward slope from left to right) [1];<br/>"
                            "(ii) A point that lies distinctly away from / significantly off the straight line of best fit compared to all other data points [1];<br/>"
                            "(iii) Circle or flag the anomalous point, ignore it / exclude it when drawing the line of best fit, and do not use its coordinates to calculate the gradient [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="Using the data from the table, calculate the gradient of the line of best fit. State the coordinates of the two points on the line of best fit used in your calculation, and include appropriate units for the gradient.",
                marks=3,
                lines_count=5,
                mark_scheme="Two points on line clearly identified, separated by at least half the length of the drawn line (e.g. (3.050, -2.53) and (3.410, -4.48)) [1];<br/>"
                            "Gradient = Δy / Δx = [-2.53 - (-4.48)] / [(3.050 - 3.410) x 10⁻³] = +1.95 / (-0.360 x 10⁻³) = -5417 K [1];<br/>"
                            "Units of gradient: K (Kelvin) or K⁻¹ properly accounted for with 10⁻³ factor [1]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Use your gradient from (c) and the gas constant R = 8.314 J K⁻¹ mol⁻¹ to calculate the experimental activation energy, Ea, for the peroxydisulfate–iodide reaction. Give your answer in kJ mol⁻¹ to 3 significant figures.",
                marks=3,
                lines_count=4,
                mark_scheme="Gradient = -Ea / R => Ea = -gradient x R [1];<br/>"
                            "Ea = -(-5417 K) x 8.314 J K⁻¹ mol⁻¹ = +45037 J mol⁻¹ [1];<br/>"
                            "Ea = +45.0 kJ mol⁻¹ (allow 44.0 to 46.0 kJ mol⁻¹ with positive sign) [1]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="(i) The digital stopwatch used has an uncertainty of ± 0.2 s, and human reaction time introduces an additional uncertainty of ± 0.3 s. Calculate the percentage uncertainty in the reaction time recorded for Experiment 8 (t = 12.4 s).<br/>"
                     "(ii) Explain why temperature control is more critical at higher temperatures, and suggest one improvement to the apparatus to ensure temperature remains constant throughout each run.",
                marks=3,
                lines_count=4,
                mark_scheme="(i) Total timing uncertainty = ± 0.2 + 0.3 = ± 0.5 s; Percentage uncertainty = (0.5 / 12.4) x 100% = 4.03% (or 4.0%) [1];<br/>"
                            "(ii) At higher temperatures (e.g. 55 °C), the reaction mixture cools down more rapidly to the ambient laboratory temperature during the run [1];<br/>"
                            "Improvement: Keep the reaction vessel inside a thermostatically controlled water bath throughout the entire course of the reaction [1]."
            )
        ]
    )

    build_paper5_pdf(
        output_path=out_path,
        config=config,
        questions=[q1, q2]
    )

if __name__ == "__main__":
    build_physical_paper5()
