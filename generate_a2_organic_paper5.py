"""
Cambridge International A Level Chemistry (9701) — A2 Suite
PAPER 5: PLANNING, ANALYSIS AND EVALUATION (ORGANIC CHEMISTRY)
Generates:
Urwah_Chem_Paper5_Planning_Organic_Chemistry.pdf

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

def create_saponification_table():
    styles = getSampleStyleSheet()
    header_style = ParagraphStyle('TH', fontName='Poppins-Bold', fontSize=7.0, leading=9, textColor=COLOR_NAVY, alignment=1)
    cell_style = ParagraphStyle('TC', fontName='Poppins', fontSize=7.0, leading=9, textColor=COLOR_DARK, alignment=1)
    cell_bold = ParagraphStyle('TCB', fontName='Poppins-Bold', fontSize=7.0, leading=9, textColor=COLOR_DARK, alignment=1)

    table_data = [
        [
            Paragraph("<b>Sample</b>", header_style),
            Paragraph("<b>Time<br/>t / min</b>", header_style),
            Paragraph("<b>Titre of HCl<br/>V / cm³</b>", header_style),
            Paragraph("<b>[OH⁻]<br/>/ mol dm⁻³</b>", header_style),
            Paragraph("<b>1 / [OH⁻]<br/>/ dm³ mol⁻¹</b>", header_style)
        ],
        [Paragraph("1", cell_style), Paragraph("0.0", cell_style), Paragraph("25.00", cell_style), Paragraph("0.0500", cell_bold), Paragraph("20.0", cell_bold)],
        [Paragraph("2", cell_style), Paragraph("5.0", cell_style), Paragraph("20.80", cell_style), Paragraph("0.0416", cell_bold), Paragraph("24.0", cell_bold)],
        [Paragraph("3", cell_style), Paragraph("10.0", cell_style), Paragraph("17.85", cell_style), Paragraph("0.0357", cell_bold), Paragraph("28.0", cell_bold)],
        [Paragraph("4", cell_style), Paragraph("15.0", cell_style), Paragraph("15.60", cell_style), Paragraph("0.0312", cell_bold), Paragraph("32.1", cell_bold)],
        [Paragraph("5", cell_style), Paragraph("20.0", cell_style), Paragraph("13.90", cell_style), Paragraph("0.0278", cell_bold), Paragraph("36.0", cell_bold)],
        [Paragraph("6", cell_style), Paragraph("25.0", cell_style), Paragraph("12.50", cell_style), Paragraph("0.0250", cell_bold), Paragraph("40.0", cell_bold)],
        [Paragraph("7", cell_style), Paragraph("30.0", cell_style), Paragraph("11.35", cell_style), Paragraph("0.0227", cell_bold), Paragraph("44.1", cell_bold)],
        [Paragraph("8", cell_style), Paragraph("35.0", cell_style), Paragraph("10.40", cell_style), Paragraph("0.0208", cell_bold), Paragraph("48.1", cell_bold)],
    ]

    t = Table(table_data, colWidths=[60, 85, 115, 115, 115])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.9, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t

def build_organic_paper5():
    out_dir = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Organic Chemistry\Paper 5 (Planning & Analysis)"
    out_path = os.path.join(out_dir, "Urwah_Chem_Paper5_Planning_Organic_Chemistry.pdf")

    config = Paper5PaperConfig(
        title="Organic Chemistry Experimental Suite",
        subtitle="Planning, Analysis and Evaluation · Multi-Step Aspirin Synthesis & Recrystallisation · Saponification Kinetics",
        component_name="Paper 5 — Planning, Analysis and Evaluation",
        duration="1 Hour 15 Minutes",
        total_marks=30,
        candidate_name="Urwah",
        centre_number="PK082",
        candidate_number="0142"
    )

    q1 = Paper5Question(
        number=1,
        title="Planning the Preparative Synthesis, Purification, and Purity Analysis of Aspirin",
        syllabus_ref="9701/52/M/J/23/Q1 · Syllabus 32.2 / 33.3 / 36.1",
        question_type="PLANNING",
        total_marks=15,
        context_intro="Aspirin (2-ethanoyloxybenzoic acid, Mr = 180.2) is prepared in the laboratory by the acylation of 2-hydroxybenzoic acid (salicylic acid, Mr = 138.1) using ethanoic anhydride ((CH₃CO)₂O, Mr = 102.1, density = 1.08 g cm⁻³) in the presence of concentrated phosphoric(V) acid catalyst:<br/>"
                      "<b>2-HOC₆H₄COOH + (CH₃CO)₂O → 2-CH₃COOC₆H₄COOH + CH₃COOH</b><br/>"
                      "You are required to plan an experimental procedure to:<br/>"
                      "1. Synthesise crude aspirin starting from exactly 5.00 g of 2-hydroxybenzoic acid.<br/>"
                      "2. Purify the crude aspirin product by recrystallisation from a water/ethanol solvent mixture.<br/>"
                      "3. Calculate the maximum theoretical yield of aspirin.<br/>"
                      "4. Assess the purity of the recrystallised aspirin using capillary melting point determination and thin-layer chromatography (TLC).<br/>"
                      "You are provided with: solid 2-hydroxybenzoic acid, liquid ethanoic anhydride, concentrated H₃PO₄, ethanol, distilled water, 1% aqueous iron(III) chloride, TLC plates (silica gel on aluminium foil), UV lamp (254 nm), melting point apparatus, capillary tubes, Büchner funnel, vacuum filtration flask, and standard laboratory glassware.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="Calculate the theoretical mass of aspirin produced from 5.00 g of 2-hydroxybenzoic acid, and calculate the minimum volume of ethanoic anhydride required if a 50% stoichiometric excess is used.",
                marks=3,
                lines_count=4,
                mark_scheme="Moles of 2-hydroxybenzoic acid = 5.00 / 138.1 = 0.03621 mol [1];<br/>"
                            "Theoretical mass of aspirin = 0.03621 x 180.2 = 6.52 g [1];<br/>"
                            "Moles of anhydride needed (50% excess) = 0.03621 x 1.50 = 0.0543 mol; Mass = 0.0543 x 102.1 = 5.54 g; Volume = 5.54 / 1.08 = 5.13 cm³ (allow 5.1 to 5.2 cm³) [1]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="Describe the apparatus setup and procedure for heating the reaction mixture to ensure complete conversion without loss of volatile reagents.",
                marks=3,
                lines_count=4,
                mark_scheme="Add 5.00 g salicylic acid and 5.2 cm³ ethanoic anhydride to a pear-shaped flask, add 5 drops of concentrated H3PO4 [1];<br/>"
                            "Fit a vertical Liebig condenser (reflux setup) with cold water entering at the bottom and leaving at the top [1];<br/>"
                            "Heat in a boiling water bath at 85–90 °C for 15 minutes to allow condensation of vapors back into the flask without loss of volatile reagents [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="Detail the recrystallisation procedure used to purify the crude aspirin, specifying solvent choice, filtration steps, and drying.",
                marks=4,
                lines_count=5,
                mark_scheme="Dissolve crude product in the minimum volume of hot ethanol/water solvent mixture [1];<br/>"
                            "Filter while hot through fluted filter paper to remove any insoluble impurities [1];<br/>"
                            "Allow filtrate to cool slowly to room temperature, then chill in an ice bath to crystallise aspirin [1];<br/>"
                            "Filter crystals using a Büchner funnel under reduced pressure (vacuum filtration), wash with small volume of ice-cold solvent, and dry between filter papers / in a desiccator [1]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Describe how the melting point of the purified aspirin is determined, and state two characteristics of the melting point that confirm high purity.",
                marks=3,
                lines_count=4,
                mark_scheme="Pack a small amount of dry powder into a thin capillary tube sealed at one end [1];<br/>"
                            "Place in melting point apparatus (e.g. electrical block or Thiele tube), heat slowly near expected m.p. (138–140 °C), and record initial melting and complete melting temperatures [1];<br/>"
                            "High purity is confirmed by: (1) sharp melting point over a narrow range (< 1–2 °C), and (2) melting point value matches the literature value (138–140 °C) without depression [1]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="Describe a chemical test using aqueous iron(III) chloride to confirm that the purified aspirin is free from unreacted 2-hydroxybenzoic acid.",
                marks=2,
                lines_count=3,
                mark_scheme="Add a few drops of neutral FeCl3(aq) to an aqueous solution of the purified aspirin [1];<br/>"
                            "Unreacted 2-hydroxybenzoic acid contains a phenolic -OH group and gives an intense purple/violet coloration; absence of purple color (solution remains yellow) confirms that no salicylic acid impurity is present [1]."
            )
        ]
    )

    q2 = Paper5Question(
        number=2,
        title="Kinetics and Thermodynamic Analysis of the Alkaline Hydrolysis of Ethyl Benzoate",
        syllabus_ref="9701/51/O/N/23/Q2 · Syllabus 26.1 / 33.2",
        question_type="ANALYSIS & EVALUATION",
        total_marks=15,
        context_intro="The alkaline hydrolysis (saponification) of ethyl benzoate is a second-order reaction:<br/>"
                      "<b>C₆H₅COOCH₂CH₃ + OH⁻ → C₆H₅COO⁻ + CH₃CH₂OH</b><br/>"
                      "Equal initial concentrations of ethyl benzoate and sodium hydroxide ([ester]₀ = [OH⁻]₀ = 0.0500 mol dm⁻³) were mixed at 25.0 °C.<br/>"
                      "At measured time intervals, 10.0 cm³ samples were withdrawn using a pipette, immediately discharged into excess ice-cold water to quench the reaction, and titrated with standard 0.0200 mol dm⁻³ hydrochloric acid to determine [OH⁻].<br/>"
                      "For equal initial reactant concentrations, the second-order integrated rate law is:<br/>"
                      "<b>(1 / [OH⁻]) = k · t + (1 / [OH⁻]₀)</b><br/>"
                      "where k is the rate constant in dm³ mol⁻¹ min⁻¹ and t is time in minutes.",
        subquestions=[
            Paper5SubQuestion(
                label="(a)",
                text="The experimental data collected is displayed in the table below. Explain why the rate of reaction decreases as time progresses.",
                marks=2,
                lines_count=3,
                table_data=create_saponification_table(),
                mark_scheme="As the reaction proceeds, reactant concentrations ([ester] and [OH⁻]) decrease steadily [1];<br/>"
                            "The collision frequency between ester molecules and hydroxide ions decreases, causing rate (rate = k [ester][OH⁻]) to drop [1]."
            ),
            Paper5SubQuestion(
                label="(b)",
                text="A graph of (1 / [OH⁻]) on the y-axis against time t / min on the x-axis was plotted.<br/>"
                     "(i) State why this graph yields a straight line for a second-order reaction.<br/>"
                     "(ii) State what the y-intercept of the line represents.",
                marks=2,
                lines_count=3,
                mark_scheme="(i) The equation (1/[OH⁻]) = k·t + (1/[OH⁻]₀) is of the linear form y = mx + c, where slope m = k and y-intercept c = 1/[OH⁻]₀ [1];<br/>"
                            "(ii) The y-intercept represents 1 / [OH⁻]₀ (the reciprocal of the initial hydroxide ion concentration at t = 0) [1]."
            ),
            Paper5SubQuestion(
                label="(c)",
                text="Using the data from the table, calculate the gradient of the line of best fit and hence determine the rate constant k at 25 °C, including its units.",
                marks=3,
                lines_count=4,
                mark_scheme="Two points on line selected (e.g. (0.0, 20.0) and (35.0, 48.1)) [1];<br/>"
                            "Gradient = Δy / Δx = (48.1 - 20.0) / (35.0 - 0.0) = 28.1 / 35.0 = 0.803 dm³ mol⁻¹ min⁻¹ [1];<br/>"
                            "Rate constant k = 0.803 dm³ mol⁻¹ min⁻¹ (or 0.0134 dm³ mol⁻¹ s⁻¹) with correct units [1]."
            ),
            Paper5SubQuestion(
                label="(d)",
                text="Explain the physical principle of 'quenching' used in this experiment, and explain why discharging the aliquot into ice-cold water effectively freezes the reaction.",
                marks=4,
                lines_count=5,
                mark_scheme="Quenching rapidly stops or dramatically slows down the reaction so that the concentration of reactants does not change during the subsequent titration [1];<br/>"
                            "Dilution with a large volume of water drastically lowers the concentrations of ester and OH⁻, reducing collision frequency [1];<br/>"
                            "Low temperature (near 0 °C) significantly reduces average kinetic energy, drastically lowering the fraction of molecules with energy E >= Ea [2]."
            ),
            Paper5SubQuestion(
                label="(e)",
                text="Suggest an alternative continuous instrumental technique to monitor the reaction rate without requiring sampling or chemical quenching, explaining your reasoning.",
                marks=4,
                lines_count=4,
                mark_scheme="Electrical conductivity measurement [1];<br/>"
                            "High-mobility hydroxide ions (OH⁻) are replaced one-for-one by bulky benzoate ions (C6H5COO⁻) of much lower ionic mobility [1];<br/>"
                            "The electrical conductivity of the solution decreases steadily and continuously over time, allowing real-time monitoring without disturbing the equilibrium [2]."
            )
        ]
    )

    build_paper5_pdf(out_path, config, [q1, q2])

if __name__ == "__main__":
    build_organic_paper5()
