"""
build_usman_week1_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 1 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN
Coverage:
  - 11A.1: Techniques for Measuring the Rate of Reaction
  - 11A.2: Rate Equations, Rate Constants and Orders of Reaction

Structure:
  - Section A: 30 Multiple Choice Questions (30 Marks)
  - Section B: 5 Structured Core Questions (90 Marks, 18 marks each)
  - Section C: 2 Contemporary Synoptic & Experimental Data Response Questions (30 Marks, 15 marks each)
  - Full Point-by-Point Official Mark Scheme & Examiner Trap Commentary
"""

import os
import sys
import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ──────────────────────────────────────────────────────────────
# FONTS REGISTRATION
# ──────────────────────────────────────────────────────────────
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

def register_fonts():
    fonts = {
        'Poppins-Regular':  'Poppins-Regular.ttf',
        'Poppins-Bold':     'Poppins-Bold.ttf',
        'Poppins-SemiBold': 'Poppins-SemiBold.ttf',
        'Poppins-Medium':   'Poppins-Medium.ttf',
        'Poppins-Italic':   'Poppins-Italic.ttf',
    }
    has_poppins = True
    for name, filename in fonts.items():
        font_path = os.path.join(FONT_DIR, filename)
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(name, font_path))
            except Exception:
                has_poppins = False
        else:
            has_poppins = False

    if not has_poppins:
        return {
            'Regular': 'Helvetica',
            'Bold': 'Helvetica-Bold',
            'SemiBold': 'Helvetica-Bold',
            'Medium': 'Helvetica',
            'Italic': 'Helvetica-Oblique',
            'Mono': 'Courier'
        }
    return {
        'Regular': 'Poppins-Regular',
        'Bold': 'Poppins-Bold',
        'SemiBold': 'Poppins-SemiBold',
        'Medium': 'Poppins-Medium',
        'Italic': 'Poppins-Italic',
        'Mono': 'Courier'
    }

FONT = register_fonts()

# ──────────────────────────────────────────────────────────────
# COLOUR PALETTE (Mentora Formal Branding)
# ──────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0b1b36")
CRIMSON    = colors.HexColor("#a81717")
STEEL      = colors.HexColor("#1e3a8a")
LIGHT_BG   = colors.HexColor("#f8fafc")
MID_BG     = colors.HexColor("#f1f5f9")
BORDER     = colors.HexColor("#cbd5e1")
DARK_TXT   = colors.HexColor("#1e293b")
LINE_CLR   = colors.HexColor("#94a3b8")
EQ_BG      = colors.HexColor("#eef2f6")
TAG_BG     = colors.HexColor("#fee2e2")
GOLD_BG    = colors.HexColor("#fef3c7")
WHITE      = colors.white

PAGE_W, PAGE_H = A4
L_MARGIN = R_MARGIN = 1.5 * cm
TOP_MARGIN = BOTTOM_MARGIN = 1.5 * cm
AVAIL_W = PAGE_W - L_MARGIN - R_MARGIN

OUT_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Usman_Edexcel_Chem_U4_Week1_150M_Challenging_Quiz.pdf"
)

# ──────────────────────────────────────────────────────────────
# STYLES
# ──────────────────────────────────────────────────────────────
def _ps(name, **kw):
    defaults = dict(fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT,
                    leading=13.5, spaceAfter=0, spaceBefore=0)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

S = {
    'cov_brand':   _ps('CovBrand',  fontName=FONT['Bold'], fontSize=16, textColor=NAVY, alignment=1),
    'cov_sub':     _ps('CovSub',    fontName=FONT['SemiBold'], fontSize=8.5, textColor=CRIMSON, alignment=1, spaceAfter=15),
    'cov_h1':      _ps('CovH1',     fontName=FONT['Bold'], fontSize=20, textColor=NAVY, alignment=1, leading=24),
    'cov_h2':      _ps('CovH2',     fontName=FONT['Bold'], fontSize=11, textColor=STEEL, alignment=1, spaceAfter=15),
    'cov_meta':    _ps('CovMeta',   fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=14),
    'cov_meta_b':  _ps('CovMetaB',  fontName=FONT['Bold'], fontSize=9, textColor=NAVY),

    'sec_banner':  _ps('SecBan',    fontName=FONT['Bold'], fontSize=10.5, textColor=WHITE, leading=14, alignment=1),
    'q_hdr_l':     _ps('QHdrL',     fontName=FONT['Bold'], fontSize=9.5, textColor=NAVY),
    'q_hdr_r':     _ps('QHdrR',     fontName=FONT['SemiBold'], fontSize=8.5, textColor=CRIMSON, alignment=2),
    'q_stem':      _ps('QStem',     fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=13.5),
    'q_subpart':   _ps('QSubPart',  fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=13.5, leftIndent=15),
    'q_submark':   _ps('QSubMark',  fontName=FONT['Bold'], fontSize=8.5, textColor=NAVY, alignment=2),
    'q_mcq_opt':   _ps('QMcqOpt',   fontName=FONT['Regular'], fontSize=8.8, textColor=DARK_TXT, leading=12.5, leftIndent=12),
    'q_equation':  _ps('QEqn',      fontName=FONT['Mono'], fontSize=8.8, textColor=NAVY, leading=13, alignment=1),

    'tbl_th':      _ps('TblTH',     fontName=FONT['Bold'], fontSize=8.0, textColor=WHITE, alignment=1),
    'tbl_td':      _ps('TblTD',     fontName=FONT['Regular'], fontSize=8.0, textColor=DARK_TXT, alignment=1),
    'tbl_td_l':    _ps('TblTDL',   fontName=FONT['Regular'], fontSize=8.0, textColor=DARK_TXT, alignment=0),

    'ms_qtitle':   _ps('MSQTitle',  fontName=FONT['Bold'], fontSize=9, textColor=NAVY),
    'ms_text':     _ps('MSText',    fontName=FONT['Regular'], fontSize=8.2, textColor=DARK_TXT, leading=12),
    'ms_mark':     _ps('MSMark',    fontName=FONT['Bold'], fontSize=8.2, textColor=CRIMSON, alignment=2),
    'ms_trap':     _ps('MSTrap',    fontName=FONT['SemiBold'], fontSize=8.0, textColor=CRIMSON),
}

# ──────────────────────────────────────────────────────────────
# HEADER / FOOTER
# ──────────────────────────────────────────────────────────────
def draw_header_footer(canvas, doc):
    if doc.page == 1:
        return
    canvas.saveState()

    # Top Running Header
    canvas.setFont(FONT['Bold'], 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(L_MARGIN, PAGE_H - 1.0 * cm, "MENTORA ACADEMY")
    canvas.setFont(FONT['SemiBold'], 7.5)
    canvas.setFillColor(CRIMSON)
    canvas.drawString(L_MARGIN + 3.2 * cm, PAGE_H - 1.0 * cm, "•   A LEVEL CHEMISTRY (WCH14/01)")

    canvas.setFont(FONT['Medium'], 7.5)
    canvas.setFillColor(STEEL)
    canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 1.0 * cm, "USMAN  •  WEEK 1 ADVANCED QUIZ (150 MARKS)")

    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.6)
    canvas.line(L_MARGIN, PAGE_H - 1.15 * cm, PAGE_W - R_MARGIN, PAGE_H - 1.15 * cm)

    # Bottom Footer
    canvas.line(L_MARGIN, 1.25 * cm, PAGE_W - R_MARGIN, 1.25 * cm)
    canvas.setFont(FONT['Regular'], 7)
    canvas.setFillColor(DARK_TXT)
    canvas.drawString(L_MARGIN, 0.85 * cm, "Edexcel IAL Unit 4 Kinetics · Strict Examination Conditions · Candidate: Usman")

    canvas.setFont(FONT['Bold'], 7.5)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"Page {doc.page}")

    canvas.setFont(FONT['SemiBold'], 6.5)
    canvas.setFillColor(STEEL)
    canvas.drawCentredString(PAGE_W / 2.0, 0.50 * cm, "mentoraonlineacademy@gmail.com   •   +923164586836")

    canvas.restoreState()

def make_answer_lines(marks: int, avail_width: float):
    n = {1: 3, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12}.get(marks, 6)
    rows = [[""] for _ in range(n)]
    t = Table(rows, colWidths=[avail_width], rowHeights=[0.55 * cm] * n)
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, LINE_CLR),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    return t

def section_banner(title: str, bg_color):
    t = Table([[Paragraph(title, S['sec_banner'])]], colWidths=[AVAIL_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_color),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return t

# ──────────────────────────────────────────────────────────────
# BUILD THE EXAMINATION STORY
# ──────────────────────────────────────────────────────────────
def build_exam_story():
    story = []

    # ══════════════════════════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════════════════════════
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("MENTORA ACADEMY", S['cov_brand']))
    story.append(Paragraph("PRESTIGIOUS ONLINE TUITION & ADVANCED SCHOLAR ARCHITECTURE", S['cov_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=15))

    story.append(Paragraph("PEARSON EDEXCEL INTERNATIONAL ADVANCED LEVEL", S['cov_h2']))
    story.append(Paragraph("CHEMISTRY UNIT 4 (WCH14/01)<br/>WEEK 1 MASTERY & A* SCHOLAR CHALLENGE QUIZ", S['cov_h1']))
    story.append(Spacer(1, 0.4 * cm))

    # Assessment Meta Box
    meta_data = [
        [
            Paragraph("<b>Candidate Name:</b>", S['cov_meta_b']),
            Paragraph("<b>USMAN</b> (Grade A* Scholar)", S['cov_meta']),
            Paragraph("<b>Paper Code:</b>", S['cov_meta_b']),
            Paragraph("WCH14/01/W1-REV", S['cov_meta'])
        ],
        [
            Paragraph("<b>Target Exam:</b>", S['cov_meta_b']),
            Paragraph("January 2027", S['cov_meta']),
            Paragraph("<b>Date of Exam:</b>", S['cov_meta_b']),
            Paragraph("October 2026", S['cov_meta'])
        ],
        [
            Paragraph("<b>Topics Covered:</b>", S['cov_meta_b']),
            Paragraph("11A.1 (Rate Measurement) & 11A.2 (Rate Laws)", S['cov_meta']),
            Paragraph("<b>Time Allowed:</b>", S['cov_meta_b']),
            Paragraph("<b>2 Hours 30 Minutes</b>", S['cov_meta'])
        ],
        [
            Paragraph("<b>Total Marks:</b>", S['cov_meta_b']),
            Paragraph("<font color='#a81717'><b>150 MARKS</b></font>", S['cov_meta']),
            Paragraph("<b>A* Benchmark:</b>", S['cov_meta_b']),
            Paragraph("<b>>= 130 / 150 (86.7%)</b>", S['cov_meta'])
        ]
    ]
    t_meta = Table(meta_data, colWidths=[3.2*cm, 5.0*cm, 3.2*cm, 4.6*cm])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 0.6 * cm))

    # Instructions Box
    instr_text = (
        "<b>INSTRUCTIONS TO CANDIDATES:</b><br/>"
        "• Answer <b>ALL</b> questions in Section A, Section B, and Section C.<br/>"
        "• Use black ink or ball-point pen. An approved scientific calculator may be used.<br/>"
        "• Show all steps in calculations. Clearly state mathematical expressions before substituting numerical values.<br/>"
        "• Ensure all rate constants ($k$), gradients, and rates are quoted with appropriate significant figures and <b>explicit units</b>.<br/>"
        "• Relevant data: Gas constant $R = 8.314\\text{ J mol}^{-1}\\text{ K}^{-1}$; Molar volume of gas at r.t.p. $V_m = 24.0\\text{ dm}^3\\text{ mol}^{-1}$ ($24,000\\text{ cm}^3\\text{ mol}^{-1}$)."
    )
    t_instr = Table([[Paragraph(instr_text, S['cov_meta'])]], colWidths=[AVAIL_W])
    t_instr.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, STEEL),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_instr)
    story.append(Spacer(1, 0.5 * cm))

    # Paper Structure Summary Table
    struct_data = [
        [Paragraph("<b>SECTION</b>", S['tbl_th']), Paragraph("<b>QUESTION TYPES & CONTENT</b>", S['tbl_th']), Paragraph("<b>QUESTIONS</b>", S['tbl_th']), Paragraph("<b>MARKS</b>", S['tbl_th'])],
        [Paragraph("<b>Section A</b>", S['tbl_td_l']), Paragraph("Multiple Choice Questions (Rate techniques, orders, units, graphs)", S['tbl_td_l']), Paragraph("Q1 – Q30", S['tbl_td']), Paragraph("<b>30 Marks</b>", S['tbl_td'])],
        [Paragraph("<b>Section B</b>", S['tbl_td_l']), Paragraph("Core Structured Questions (Experimental data, rate equations, mechanisms)", S['tbl_td_l']), Paragraph("Q31 – Q35", S['tbl_td']), Paragraph("<b>90 Marks</b>", S['tbl_td'])],
        [Paragraph("<b>Section C</b>", S['tbl_td_l']), Paragraph("Contemporary Synoptic & Practical Data Response (Colorimetry & Polarimetry)", S['tbl_td_l']), Paragraph("Q36 – Q37", S['tbl_td']), Paragraph("<b>30 Marks</b>", S['tbl_td'])],
        [Paragraph("<b>TOTAL</b>", S['tbl_td_l']), Paragraph("<b>Full Unit 4 Week 1 Kinetics Mastery Assessment</b>", S['tbl_td_l']), Paragraph("<b>37 Questions</b>", S['tbl_td']), Paragraph("<font color='#a81717'><b>150 Marks</b></font>", S['tbl_td'])],
    ]
    t_struct = Table(struct_data, colWidths=[2.8*cm, 8.2*cm, 2.5*cm, 2.5*cm])
    t_struct.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, -1), (-1, -1), GOLD_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_struct)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION A: MULTIPLE CHOICE QUESTIONS (30 MARKS)
    # ══════════════════════════════════════════════════════════
    story.append(section_banner("SECTION A — MULTIPLE CHOICE QUESTIONS (30 MARKS) • 1 MARK EACH", NAVY))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("<i>Select the single correct answer (A, B, C, or D). Each question carries 1 mark.</i>", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    mcqs = [
        (1, "A reaction has the rate equation: rate = k[A]^0.5 [B]^2. What are the correct SI units for the rate constant k?",
         ["A  mol^-1.5 dm^4.5 s^-1", "B  mol^-0.5 dm^1.5 s^-1", "C  mol^-2 dm^6 s^-1", "D  dm^3 mol^-1 s^-1"]),

        (2, "For the gas-phase reaction 2NO(g) + O2(g) -> 2NO2(g), the rate equation is rate = k[NO]^2 [O2]. The volume of the closed reaction vessel is doubled at constant temperature. By what factor does the initial rate change?",
         ["A  Halves (0.5x)", "B  Decreases to one-quarter (0.25x)", "C  Decreases to one-eighth (0.125x)", "D  Remains unchanged"]),

        (3, "In the acid-catalysed reaction between propanone and iodine, the rate equation is rate = k[propanone][H+]. Why does the concentration of iodine NOT appear in the rate equation?",
         ["A  Iodine acts as a heterogeneous catalyst.", "B  Iodine is involved in a fast step after the rate-determining step.", "C  Iodine is in zero-order large excess in all experiments.", "D  The reaction between iodine and propanone is reversible."]),

        (4, "A student uses a colorimeter to follow the oxidation of ethanedioic acid by acidified potassium manganate(VII). Manganate(VII) ions are intensely purple, absorbing light strongly between 520 nm and 550 nm. Which colour filter should be chosen for maximum sensitivity?",
         ["A  Purple filter", "B  Red filter", "C  Green filter", "D  Blue filter"]),

        (5, "In a sampling and titrimetric study of the alkaline hydrolysis of ethyl ethanoate, CH3COOCH2CH3 + OH- -> CH3COO- + CH3CH2OH, aliquots are withdrawn at regular intervals. What is the most reliable method to quench the reaction immediately?",
         ["A  Add the aliquot to an excess of ice-cold standard hydrochloric acid.", "B  Cool the aliquot rapidly in an ice-water bath without adding chemicals.", "C  Add an excess of ethanol to shift the equilibrium position.", "D  Filter the aliquot immediately to remove unreacted ester."]),

        (6, "A reaction produces 120 cm^3 of gas at r.t.p. On an electronic balance reading to +/- 0.01 g, why is the 'loss-in-mass' method completely unsuited for reactions evolving hydrogen gas (H2) compared to carbon dioxide (CO2)?",
         ["A  Hydrogen gas dissolves completely in aqueous acid.", "B  The mass of 120 cm^3 of H2 is 0.010 g, giving an unacceptable percentage uncertainty (~100%).", "C  Hydrogen gas reacts with atmospheric oxygen on escaping the flask.", "D  Hydrogen gas is too dense to leave the cotton wool plug."]),

        (7, "The reaction CH3COOCH2CH3(aq) + NaOH(aq) -> CH3COONa(aq) + CH3CH2OH(aq) is monitored using a conductivity meter. Why does electrical conductivity decrease steadily as the reaction proceeds?",
         ["A  Covalent ethyl ethanoate is converted into ions.", "B  Highly mobile hydroxide ions (OH-) are replaced by less mobile ethanoate ions (CH3COO-).", "C  Sodium ions are precipitated as insoluble sodium ethanoate.", "D  The total concentration of charged ions drops to zero at the end."]),

        (8, "When the concentration of reactant X is increased by a factor of 4, the initial rate of reaction increases by a factor of 8. What is the order of reaction with respect to X?",
         ["A  1", "B  1.5", "C  2", "D  3"]),

        (9, "A reaction A + 2B -> C follows the rate law rate = k[A][B]^2, with k = 4.5 x 10^-3 dm^6 mol^-2 s^-1. When [B] is held in vast excess at 2.0 mol dm^-3, the reaction displays pseudo-first-order kinetics with rate = k_obs [A]. What is the numerical value of k_obs?",
         ["A  9.0 x 10^-3 s^-1", "B  1.8 x 10^-2 s^-1", "C  4.5 x 10^-3 s^-1", "D  3.6 x 10^-2 s^-1"]),

        (10, "In the peroxodisulfate-iodide clock reaction, which assumption is essential for the relationship (initial rate proportional to 1/t) to remain valid?",
         ["A  The reaction goes to 100% completion before the colour change occurs.", "B  The amount of thiosulfate consumes a very small fraction (<10%) of the total reactants.", "C  The starch indicator acts as an active catalyst.", "D  The reaction is zero order with respect to all reactants."]),

        (11, "A tangent drawn to a concentration-time curve at t = 0 passes through (0 s, 0.40 mol dm^-3) and (80 s, 0.00 mol dm^-3). What is the initial rate of reaction?",
         ["A  5.0 x 10^-3 mol dm^-3 s^-1", "B  2.0 x 10^-3 mol dm^-3 s^-1", "C  3.2 x 10^-2 mol dm^-3 s^-1", "D  0.40 mol dm^-3 s^-1"]),

        (12, "In the iodine clock reaction S2O8^2- + 2I- -> 2SO4^2- + I2, what is the exact chemical role of the added sodium thiosulfate (Na2S2O3)?",
         ["A  It oxidises sulfate ions to regenerate persulfate.", "B  It reacts instantaneously with I2 to regenerate I- until thiosulfate is completely consumed.", "C  It complexes with starch to create the blue-black species.", "D  It buffers the pH of the aqueous solution at pH 7.0."]),

        (13, "Which of the following experimental techniques allows continuous monitoring of reaction rate WITHOUT the need to withdraw and quench reaction samples?",
         ["A  Sampling followed by acid-base titration", "B  Sampling followed by iodine titration", "C  Continuous measurement of electrical conductivity", "D  Precipitation and gravimetric weighing"]),

        (14, "Dilatometry is an experimental technique that measures the rate of reaction by monitoring:",
         ["A  The small volume change of a liquid reaction mixture inside a precision capillary.", "B  The change in refractive index of the solution.", "C  The rate of heat dissipation to the surroundings.", "D  The pressure of an evolved gas in a manometer."]),

        (15, "Consider the initial rate data: Exp 1: [A]=0.1, [B]=0.1, Rate=2x10^-4; Exp 2: [A]=0.2, [B]=0.1, Rate=4x10^-4; Exp 3: [A]=0.3, [B]=0.2, Rate=2.4x10^-3. What is the overall order of the reaction?",
         ["A  1", "B  2", "C  3", "D  4"]),

        (16, "When the temperature of an aqueous reaction mixture is increased by 10 K at constant reactant concentrations, what happens to the rate constant k and the reaction orders?",
         ["A  Both k and the reaction orders double.", "B  k increases substantially (approx. doubles); reaction orders remain unchanged.", "C  k remains unchanged; reaction orders increase.", "D  k increases; reaction orders decrease to zero."]),

        (17, "A plot of log10(initial rate) against log10[A] yields a straight line with gradient = +2.0 and y-intercept = -1.30. What is the value of the rate constant k?",
         ["A  0.050 dm^3 mol^-1 s^-1", "B  0.20 dm^3 mol^-1 s^-1", "C  1.30 dm^3 mol^-1 s^-1", "D  2.00 dm^3 mol^-1 s^-1"]),

        (18, "When calcium carbonate chips react with dilute hydrochloric acid in a conical flask connected to a gas syringe, why is there often a noticeable delay (lag phase) before gas volume begins to register?",
         ["A  Friction in the syringe plunger prevents immediate movement.", "B  Carbon dioxide is moderately soluble in water and the solution must become saturated before gas is evolved.", "C  The activation energy of the reaction increases initially.", "D  The reaction is initially endothermic and cools the flask."]),

        (19, "The acid-catalysed hydrolysis of sucrose to glucose and fructose is called the 'inversion of sucrose'. Which optical instrument can be used to follow the reaction rate continuously?",
         ["A  Colorimeter", "B  Spectrophotometer", "C  Polarimeter", "D  Refractometer"]),

        (20, "In a titrimetric study of the decomposition of hydrogen peroxide, 2H2O2(aq) -> 2H2O(l) + O2(g), aliquots are titrated with standard KMnO4. Why is quenching in ice-cold dilute H2SO4 highly effective?",
         ["A  Sulfuric acid acts as an inhibitor and destroys the MnO2 catalyst, while low temperature slows the reaction.", "B  Sulfuric acid precipitates the hydrogen peroxide as an insoluble sulfate.", "C  Sulfuric acid oxidises water to stop the backward reaction.", "D  Sulfuric acid acts as an indicator in the titration."]),

        (21, "Marble chips (CaCO3) react with excess 1.0 mol dm^-3 HCl. What is the order of reaction with respect to solid calcium carbonate?",
         ["A  Zero order", "B  First order", "C  Second order", "D  Half order"]),

        (22, "For a reaction rate = k[P]^2 [Q], where rate is measured in mol dm^-3 min^-1 and concentrations in mol dm^-3, what are the units of k?",
         ["A  dm^6 mol^-2 min^-1", "B  dm^3 mol^-1 min^-1", "C  mol^-2 dm^6 s^-1", "D  min^-1"]),

        (23, "For a zero-order reaction A -> products, which of the following plots gives a straight line with a negative gradient?",
         ["A  [A] against time t", "B  ln[A] against time t", "C  1/[A] against time t", "D  rate against [A]"]),

        (24, "For a second-order reaction with respect to reactant A, which plot yields a straight line with a POSITIVE gradient equal to k?",
         ["A  [A] against time t", "B  ln[A] against time t", "C  1/[A] against time t", "D  [A]^2 against time t"]),

        (25, "Why must a colorimeter be calibrated with a cuvette containing only pure solvent (a 'blank') before recording absorbance data?",
         ["A  To set the absorbance to 1.00 before the reaction begins.", "B  To compensate for light absorption, reflection, and scattering by the solvent and cuvette walls.", "C  To heat the cuvette to the reaction temperature.", "D  To ensure the detector operates at maximum wavelength."]),

        (26, "In a clock reaction investigation using varying volumes of potassium iodide, why MUST deionised water be added to keep the total volume constant across all runs?",
         ["A  To maintain constant ionic strength and ensure volume of reactant is directly proportional to concentration.", "B  To prevent the solution from overheating during the reaction.", "C  To dilute the starch indicator so it does not coagulate.", "D  To keep the pH strictly buffered at pH 4.0."]),

        (27, "For the stoichiometric reaction 2A + B -> 3C, the rate of consumption of A is -d[A]/dt = 0.048 mol dm^-3 s^-1. What is the rate of formation of C (d[C]/dt)?",
         ["A  0.024 mol dm^-3 s^-1", "B  0.032 mol dm^-3 s^-1", "C  0.072 mol dm^-3 s^-1", "D  0.048 mol dm^-3 s^-1"]),

        (28, "The nucleophilic substitution CH3Br + OH- -> CH3OH + Br- has the rate law rate = k[CH3Br][OH-]. If [CH3Br] is tripled and [OH-] is divided by 3, what happens to the rate?",
         ["A  Increases by a factor of 9", "B  Decreases by a factor of 9", "C  Remains exactly the same", "D  Increases by a factor of 3"]),

        (29, "Why is the half-life of a first-order reaction completely independent of the starting concentration?",
         ["A  Because rate is inversely proportional to concentration.", "B  Because rate is directly proportional to concentration, so as concentration doubles, the reaction proceeds twice as fast.", "C  Because the rate constant k decreases as concentration falls.", "D  Because the activation energy decreases as the reaction proceeds."]),

        (30, "A student carries out a continuous colorimetric rate experiment with iodine in a colorimeter without temperature control. Over 15 minutes, the cell temperature rises by 4.2 °C due to lamp heating. What systematic error does this introduce?",
         ["A  The calculated rate constant k will be progressively overestimated as the run proceeds.", "B  The order with respect to iodine will change from zero to second order.", "C  The absorbance reading will become negative.", "D  The rate of reaction will decrease towards the end of the run."]),
    ]

    for qnum, qtext, opts in mcqs:
        p_q = Paragraph(f"<b>Q{qnum}.</b>&nbsp; {qtext}", S['q_stem'])
        story.append(p_q)
        story.append(Spacer(1, 0.08 * cm))
        for opt in opts:
            story.append(Paragraph(opt, S['q_mcq_opt']))
        story.append(Spacer(1, 0.22 * cm))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION B: STRUCTURED CORE QUESTIONS (90 MARKS)
    # ══════════════════════════════════════════════════════════
    story.append(section_banner("SECTION B — STRUCTURED CORE QUESTIONS (90 MARKS) • 5 QUESTIONS", NAVY))
    story.append(Spacer(1, 0.3 * cm))

    # ──────────────────────────────────────────────────────────
    # QUESTION 31 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 31: Acid-Catalysed Iodination of Propanone</b>", S['q_hdr_l']),
         Paragraph("<b>[18 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P31</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=STEEL, spaceAfter=6))

    story.append(Paragraph(
        "Propanone reacts with iodine in aqueous acid according to the equation:<br/>"
        "<font color='#0b1b36'><b>CH3COCH3(aq) + I2(aq) —[H+(aq)]—&gt; CH3COCH2I(aq) + H+(aq) + I-(aq)</b></font><br/>"
        "A student investigates the kinetics of this reaction at 298 K.",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> State why colorimetry is an ideal experimental technique for continuously monitoring the rate of this reaction. Identify the species responsible for the color change, suggest a suitable filter wavelength range, and state what is plotted to calibrate the colorimeter.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b) - Data Table & Deductions
    story.append(Paragraph("<b>(b)</b> The student performs four initial rate experiments at 298 K. The results are shown below:", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    t31_data = [
        [Paragraph("<b>Exp</b>", S['tbl_th']), Paragraph("<b>[CH3COCH3] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>[I2] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>[H+] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>Initial Rate / mol dm^-3 s^-1</b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("0.00200", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("1.40 x 10^-6", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("0.800", S['tbl_td']), Paragraph("0.00200", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("2.80 x 10^-6", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("0.00400", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("1.40 x 10^-6", S['tbl_td'])],
        [Paragraph("4", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("0.00200", S['tbl_td']), Paragraph("0.800", S['tbl_td']), Paragraph("2.80 x 10^-6", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[1.8*cm, 3.8*cm, 3.2*cm, 3.2*cm, 4.0*cm])
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t31)
    story.append(Spacer(1, 0.15 * cm))

    story.append(Table([
        [Paragraph("Deduce the order of reaction with respect to propanone, iodine, and hydrogen ions. Fully justify your deduction for each reactant by comparing appropriate experiments.", S['q_subpart']),
         Paragraph("<b>[6]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(6, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Write the overall rate equation for the reaction. Calculate the rate constant, <i>k</i>, at 298 K using data from Experiment 1, and state its units.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Sketch the shape of the graph of [I2] against time when propanone and H+ are present in large excess. Explain the feature of the graph that confirms the order with respect to iodine.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (e)
    story.append(Table([
        [Paragraph("<b>(e)</b> Explain why [H+] appears in the rate equation even though hydrogen ions are regenerated in the stoichiometric equation and do not appear as a net reactant.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))

    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 32: The Peroxodisulfate(VI)–Iodide Clock Reaction</b>", S['q_hdr_l']),
         Paragraph("<b>[18 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P32</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=STEEL, spaceAfter=6))

    story.append(Paragraph(
        "Persulfate ions oxidise iodide ions according to the reaction:<br/>"
        "<font color='#0b1b36'><b>S2O8^2-(aq) + 2I-(aq) -&gt; 2SO4^2-(aq) + I2(aq) &nbsp;&nbsp;&nbsp;&nbsp;[Reaction 1]</b></font><br/>"
        "In a clock experiment, a small fixed amount of sodium thiosulfate (Na2S2O3) and starch indicator are added:<br/>"
        "<font color='#0b1b36'><b>I2(aq) + 2S2O3^2-(aq) -&gt; 2I-(aq) + S4O6^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp;[Reaction 2 (Fast)]</b></font>",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain the mechanism of the colour change in this clock reaction. Why does the solution remain colourless initially, and what causes the sudden sudden appearance of a dark blue-black colour at time <i>t</i>?", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b) - Table & Rate calculations
    story.append(Paragraph("<b>(b)</b> A series of experiments is conducted at 20 °C. In every run, exactly 5.0 cm^3 of 0.010 mol dm^-3 Na2S2O3 and starch are added, and deionised water is used to keep the total volume at exactly 50.0 cm^3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    t32_data = [
        [Paragraph("<b>Run</b>", S['tbl_th']), Paragraph("<b>Vol 0.050 M S2O8^2- / cm^3</b>", S['tbl_th']), Paragraph("<b>Vol 0.100 M I- / cm^3</b>", S['tbl_th']), Paragraph("<b>Vol Water / cm^3</b>", S['tbl_th']), Paragraph("<b>Time t / s</b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("10.0", S['tbl_td']), Paragraph("10.0", S['tbl_td']), Paragraph("25.0", S['tbl_td']), Paragraph("88.0", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("20.0", S['tbl_td']), Paragraph("10.0", S['tbl_td']), Paragraph("15.0", S['tbl_td']), Paragraph("44.0", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("10.0", S['tbl_td']), Paragraph("20.0", S['tbl_td']), Paragraph("15.0", S['tbl_td']), Paragraph("44.0", S['tbl_td'])],
        [Paragraph("4", S['tbl_td']), Paragraph("15.0", S['tbl_td']), Paragraph("20.0", S['tbl_td']), Paragraph("10.0", S['tbl_td']), Paragraph("29.3", S['tbl_td'])],
    ]
    t32 = Table(t32_data, colWidths=[1.8*cm, 4.0*cm, 3.6*cm, 3.6*cm, 3.0*cm])
    t32.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t32)
    story.append(Spacer(1, 0.15 * cm))

    story.append(Table([
        [Paragraph("<b>(i)</b> Deduce the order with respect to S2O8^2- and I-, showing full reasoning.<br/>"
                   "<b>(ii)</b> Calculate the concentration of S2O8^2- and I- in Run 1.<br/>"
                   "<b>(iii)</b> Calculate the initial rate in Run 1 in mol dm^-3 s^-1, given that 5.0 x 10^-5 mol of S2O3^2- was consumed.<br/>"
                   "<b>(iv)</b> Calculate the rate constant <i>k</i> at 20 °C, including units.", S['q_subpart']),
         Paragraph("<b>[8]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(8, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why the amount of thiosulfate added must be significantly less than the amounts of persulfate and iodide present.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> State two distinct reasons why deionised water was added to maintain a constant total volume across all runs.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))

    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 33: Alkaline Hydrolysis of an Ester (Conductimetry & Titrimetry)</b>", S['q_hdr_l']),
         Paragraph("<b>[18 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P33</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=STEEL, spaceAfter=6))

    story.append(Paragraph(
        "Ethyl ethanoate is hydrolysed by sodium hydroxide according to the second-order reaction:<br/>"
        "<font color='#0b1b36'><b>CH3COOCH2CH3(aq) + OH-(aq) -&gt; CH3COO-(aq) + CH3CH2OH(aq)</b></font><br/>"
        "Rate = <i>k</i> [ester] [OH-].",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain in terms of ionic mobilities why electrical conductivity decreases as this reaction progresses, and why conductimetry provides continuous data without altering the reaction mixture.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> In a sampling study, a student withdraws 10.0 cm^3 aliquots every 2 minutes. Describe the precise procedure to quench each aliquot, and explain why pouring into ice-cold water alone is inadequate compared to quenching in excess standard acid followed by back-titration.", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> In Experiment 1, the student uses [ester]0 = 0.0150 mol dm^-3 and [OH-]0 = 0.600 mol dm^-3.<br/>"
                   "<b>(i)</b> Explain why the reaction obeys pseudo-first-order kinetics under these conditions.<br/>"
                   "<b>(ii)</b> A plot of ln[ester] against time <i>t</i> gives a straight line with gradient = -0.0660 s^-1. Calculate the apparent pseudo-rate constant <i>k'</i> and the true second-order rate constant <i>k</i> with units.", S['q_subpart']),
         Paragraph("<b>[7]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(7, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the half-life (t1/2) of ethyl ethanoate in Experiment 1. State and explain what happens to the half-life if the initial concentration of sodium hydroxide is doubled to 1.20 mol dm^-3.", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))

    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 34: Decomposition of Hydrogen Peroxide & Practical Evaluation</b>", S['q_hdr_l']),
         Paragraph("<b>[18 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P34</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=STEEL, spaceAfter=6))

    story.append(Paragraph(
        "Hydrogen peroxide decomposes catalytically according to the equation:<br/>"
        "<font color='#0b1b36'><b>2H2O2(aq) —[MnO2(s)]—&gt; 2H2O(l) + O2(g)</b></font>",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a) - Level of response
    story.append(Table([
        [Paragraph("<b>*(a) Extended Response:</b> A teacher presents two methods to follow the rate of this reaction:<br/>"
                   "<b>Method 1:</b> Collecting oxygen gas in a 100 cm^3 gas syringe.<br/>"
                   "<b>Method 2:</b> Monitoring the loss in mass on an electronic balance reading to 0.01 g.<br/>"
                   "Compare and evaluate both methods. In your response, discuss: gas solubility, temperature and friction errors, apparatus percentage uncertainties, and aerosol spray loss.", S['q_subpart']),
         Paragraph("<b>[6]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(6, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b) - Table & Half life
    story.append(Paragraph("<b>(b)</b> A student collects oxygen in a gas syringe using 25.0 cm^3 of H2O2 at 298 K. The total volume at completion (V_inf) was 68.0 cm^3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    t34_data = [
        [Paragraph("<b>Time t / s</b>", S['tbl_th']), Paragraph("0", S['tbl_td']), Paragraph("30", S['tbl_td']), Paragraph("60", S['tbl_td']), Paragraph("90", S['tbl_td']), Paragraph("120", S['tbl_td']), Paragraph("150", S['tbl_td']), Paragraph("180", S['tbl_td']), Paragraph("240", S['tbl_td']), Paragraph("300", S['tbl_td']), Paragraph("inf", S['tbl_td'])],
        [Paragraph("<b>V(O2) / cm^3</b>", S['tbl_th']), Paragraph("0.0", S['tbl_td']), Paragraph("18.0", S['tbl_td']), Paragraph("31.5", S['tbl_td']), Paragraph("41.5", S['tbl_td']), Paragraph("49.0", S['tbl_td']), Paragraph("54.5", S['tbl_td']), Paragraph("58.5", S['tbl_td']), Paragraph("63.5", S['tbl_td']), Paragraph("66.0", S['tbl_td']), Paragraph("68.0", S['tbl_td'])],
        [Paragraph("<b>(V_inf - V) / cm^3</b>", S['tbl_th']), Paragraph("68.0", S['tbl_td']), Paragraph("50.0", S['tbl_td']), Paragraph("36.5", S['tbl_td']), Paragraph("26.5", S['tbl_td']), Paragraph("19.0", S['tbl_td']), Paragraph("13.5", S['tbl_td']), Paragraph("9.5", S['tbl_td']), Paragraph("4.5", S['tbl_td']), Paragraph("2.0", S['tbl_td']), Paragraph("0.0", S['tbl_td'])],
    ]
    t34 = Table(t34_data, colWidths=[3.2*cm] + [1.28*cm]*10)
    t34.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t34)
    story.append(Spacer(1, 0.15 * cm))

    story.append(Table([
        [Paragraph("Show that the reaction is first-order with respect to H2O2 by determining two successive half-lives from the data above. Clearly state the values of both half-lives.", S['q_subpart']),
         Paragraph("<b>[6]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(6, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> A tangent drawn to the V(O2) vs time curve at t = 0 passes through (0 s, 0 cm^3) and (50 s, 32.0 cm^3). Calculate the initial rate in cm^3 s^-1, and convert this into mol dm^-3 s^-1 of H2O2 consumed in the 25.0 cm^3 solution (Vm = 24,000 cm^3 mol^-1).", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the rate constant <i>k</i> for this decomposition from your average half-life using t1/2 = ln 2 / k.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))

    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 35: Gas-Phase Kinetics of Nitrogen Monoxide & Hydrogen</b>", S['q_hdr_l']),
         Paragraph("<b>[18 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P35</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=STEEL, spaceAfter=6))

    story.append(Paragraph(
        "Nitrogen monoxide reacts with hydrogen at 1000 K:<br/>"
        "<font color='#0b1b36'><b>2NO(g) + 2H2(g) -&gt; N2(g) + 2H2O(g)</b></font>",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain how monitoring the total pressure of the reaction vessel at constant volume allows the reaction rate to be determined, and state why the reaction temperature must be kept strictly above 100 °C.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b) - Table & Deductions
    story.append(Paragraph("<b>(b)</b> The following initial rate data were obtained at 1000 K:", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    t35_data = [
        [Paragraph("<b>Exp</b>", S['tbl_th']), Paragraph("<b>[NO] / 10^-3 mol dm^-3</b>", S['tbl_th']), Paragraph("<b>[H2] / 10^-3 mol dm^-3</b>", S['tbl_th']), Paragraph("<b>Initial Rate / 10^-5 mol dm^-3 s^-1</b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("1.50", S['tbl_td']), Paragraph("2.00", S['tbl_td']), Paragraph("3.60", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("3.00", S['tbl_td']), Paragraph("2.00", S['tbl_td']), Paragraph("14.40", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("1.50", S['tbl_td']), Paragraph("6.00", S['tbl_td']), Paragraph("10.80", S['tbl_td'])],
        [Paragraph("4", S['tbl_td']), Paragraph("4.50", S['tbl_td']), Paragraph("4.00", S['tbl_td']), Paragraph("R4", S['tbl_td'])],
    ]
    t35 = Table(t35_data, colWidths=[2.0*cm, 4.5*cm, 4.5*cm, 5.0*cm])
    t35.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t35)
    story.append(Spacer(1, 0.15 * cm))

    story.append(Table([
        [Paragraph("<b>(i)</b> Deduce the orders with respect to NO and H2 with full reasoning.<br/>"
                   "<b>(ii)</b> Write the rate equation and calculate the rate constant <i>k</i> at 1000 K with units.<br/>"
                   "<b>(iii)</b> Calculate the predicted initial rate, R4, in Experiment 4.", S['q_subpart']),
         Paragraph("<b>[9]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(9, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> The reaction mixture is placed in a cylinder with a movable piston. The volume of the cylinder is compressed to one-third of its original volume at constant temperature.<br/>"
                   "<b>(i)</b> State what happens to the concentration of each gas.<br/>"
                   "<b>(ii)</b> Calculate the factor by which the initial rate will increase.<br/>"
                   "<b>(iii)</b> State and explain whether the rate constant <i>k</i> changes.", S['q_subpart']),
         Paragraph("<b>[6]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(6, AVAIL_W))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION C: SYNOPTIC & EXPERIMENTAL DATA RESPONSE (30 MARKS)
    # ══════════════════════════════════════════════════════════
    story.append(section_banner("SECTION C — SYNOPTIC & EXPERIMENTAL DATA RESPONSE (30 MARKS) • 2 QUESTIONS", CRIMSON))
    story.append(Spacer(1, 0.3 * cm))

    # ──────────────────────────────────────────────────────────
    # QUESTION 36 (15 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 36: Spectrophotometric Study of Crystal Violet Decolorisation</b>", S['q_hdr_l']),
         Paragraph("<b>[15 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P36</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=CRIMSON, spaceAfter=6))

    story.append(Paragraph(
        "Crystal violet (CV+) is an intensely violet triphenylmethane dye. It reacts with hydroxide ions to form a colourless carbinol base (CV-OH):<br/>"
        "<font color='#0b1b36'><b>CV+(aq) [violet] + OH-(aq) -&gt; CV-OH(aq) [colourless]</b></font><br/>"
        "Rate = <i>k</i> [CV+]^m [OH-]^n.",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Describe how a student prepares a calibration curve of absorbance vs [CV+] using a stock solution of 1.00 x 10^-4 mol dm^-3 crystal violet, a 590 nm yellow filter, and serial dilution with volumetric glassware.", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> In the kinetic run, [CV+]0 = 2.00 x 10^-5 mol dm^-3 and [OH-]0 = 0.100 mol dm^-3. Explain why this 5000-fold excess of OH- allows the isolation method to be used.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Prove mathematically that for a first-order reaction obeying Beer-Lambert's Law (A = eps * l * c), a plot of ln(Absorbance) against time gives a straight line of gradient = -k'. If the gradient is -0.0185 s^-1, state the order <i>m</i> and calculate <i>k'</i>.", S['q_subpart']),
         Paragraph("<b>[5]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(5, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> When [OH-] is increased from 0.100 mol dm^-3 to 0.200 mol dm^-3, the gradient becomes -0.0370 s^-1. Deduce the order <i>n</i> with respect to OH-, write the overall rate equation, and calculate <i>k</i>.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))

    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Table([
        [Paragraph("<b>QUESTION 37: Acid-Catalysed Inversion of Sucrose (Polarimetry & Dilatometry)</b>", S['q_hdr_l']),
         Paragraph("<b>[15 Marks]</b><br/><font color='#a81717'><b>WCH14/01/P37</b></font>", S['q_hdr_r'])]
    ], colWidths=[AVAIL_W - 3.5*cm, 3.5*cm]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=CRIMSON, spaceAfter=6))

    story.append(Paragraph(
        "Sucrose hydrolyses in aqueous acid to produce glucose and fructose:<br/>"
        "<font color='#0b1b36'><b>C12H22O11(aq) + H2O(l) —[H+]—&gt; C6H12O6(aq) [glucose] + C6H12O6(aq) [fructose]</b></font><br/>"
        "Sucrose is dextrorotatory (+66.5°), but the equimolar product mixture is laevorotatory (-19.7°).",
        S['q_stem']
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain how a polarimeter works to continuously follow this reaction, and why the process is referred to historically as the 'inversion of sucrose'.", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b) - Table & Half life
    story.append(Paragraph("<b>(b)</b> The angle of rotation alpha_t was recorded over time at 298 K. The concentration of unreacted sucrose is directly proportional to (alpha_t - alpha_inf):", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    t37_data = [
        [Paragraph("<b>Time t / min</b>", S['tbl_th']), Paragraph("0", S['tbl_td']), Paragraph("20", S['tbl_td']), Paragraph("40", S['tbl_td']), Paragraph("60", S['tbl_td']), Paragraph("80", S['tbl_td']), Paragraph("120", S['tbl_td'])],
        [Paragraph("<b>(alpha_t - alpha_inf) / deg</b>", S['tbl_th']), Paragraph("32.0", S['tbl_td']), Paragraph("22.6", S['tbl_td']), Paragraph("16.0", S['tbl_td']), Paragraph("11.3", S['tbl_td']), Paragraph("8.0", S['tbl_td']), Paragraph("4.0", S['tbl_td'])],
    ]
    t37 = Table(t37_data, colWidths=[4.0*cm] + [2.0*cm]*6)
    t37.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t37)
    story.append(Spacer(1, 0.15 * cm))

    story.append(Table([
        [Paragraph("Prove that the reaction is first-order with respect to sucrose by determining two successive half-lives from this data. Calculate the rate constant <i>k</i> in min^-1.", S['q_subpart']),
         Paragraph("<b>[4]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(4, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why a dilatometer can follow this reaction even though no gas is evolved and no colour changes occur.", S['q_subpart']),
         Paragraph("<b>[3]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(3, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Explain why measuring electrical conductivity is completely unsuitable for following the rate of this reaction.", S['q_subpart']),
         Paragraph("<b>[2]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(2, AVAIL_W))
    story.append(Spacer(1, 0.25 * cm))

    # Part (e)
    story.append(Table([
        [Paragraph("<b>(e)</b> Compare the initial rate of inversion when 1.0 mol dm^-3 HCl is used as catalyst compared to 1.0 mol dm^-3 CH3COOH. Explain your answer with reference to [H+].", S['q_subpart']),
         Paragraph("<b>[2]</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(make_answer_lines(2, AVAIL_W))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # COMPLETE MARK SCHEME & EXAMINER COMMENTARY
    # ══════════════════════════════════════════════════════════
    story.append(section_banner("TEACHER'S MARK SCHEME & EXAMINER TRAP COMMENTARY (150 MARKS)", STEEL))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("<b>CONFIDENTIAL: Mentora Academy A* Examiner Guidance & Point Allocations</b>", S['cov_h2']))
    story.append(Spacer(1, 0.2 * cm))

    # Section A Mark Scheme Table
    ms_a = [
        ("Q1", "A", "Overall order = 0.5 + 2 = 2.5. Units of k = (mol dm^-3 s^-1) / (mol dm^-3)^2.5 = mol^-1.5 dm^4.5 s^-1. (1)"),
        ("Q2", "C", "Doubling volume halves all concentrations: rate = k(0.5[NO])^2(0.5[O2]) = (0.5)^3 = 0.125x (decreases by factor of 8). (1)"),
        ("Q3", "B", "Iodine is involved in a fast step AFTER the rate-determining step, so its concentration does not affect the rate. (1)"),
        ("Q4", "C", "Manganate(VII) absorbs strongly in the green region (520-550 nm); complementary green filter provides maximum absorbance sensitivity. (1)"),
        ("Q5", "A", "Adding excess standard ice-cold acid removes OH- instantaneously (quenching) and cools mixture; unreacted acid is back-titrated. (1)"),
        ("Q6", "B", "Mass of 120 cm^3 of H2 is only 0.010 g. On a +/- 0.01 g balance, % uncertainty is 100%, destroying reliability. (1)"),
        ("Q7", "B", "Highly mobile OH- ions (ionic conductivity 198 S cm^2 mol^-1) are replaced by bulky, slower CH3COO- ions (41 S cm^2 mol^-1). (1)"),
        ("Q8", "B", "4^n = 8 => (2^2)^n = 2^3 => 2n = 3 => n = 1.5. (1)"),
        ("Q9", "B", "k_obs = k[B]^2 = (4.5 x 10^-3)(2.0)^2 = 1.8 x 10^-2 s^-1. (1)"),
        ("Q10", "B", "Initial rate approx 1/t requires delta[reactant] to be negligible (<10%) so concentrations remain constant during time t. (1)"),
        ("Q11", "A", "Gradient magnitude = 0.40 / 80 = 5.0 x 10^-3 mol dm^-3 s^-1. (1)"),
        ("Q12", "B", "Thiosulfate rapidly reduces I2 back to I- as fast as it forms until all S2O3^2- is exhausted, then free I2 forms blue-black starch complex. (1)"),
        ("Q13", "C", "Electrical conductivity probe stays in the reaction vessel and measures continuously without removing or quenching any liquid. (1)"),
        ("Q14", "A", "Dilatometry measures small liquid volume changes in a narrow capillary due to bond formation/breakage and hydration changes. (1)"),
        ("Q15", "C", "From Exp 1 & 2: doubling [A] doubles rate => order in A = 1. Exp 1 & 3: [A] triples (3x) and rate increases 12x => (3)^1 * (2)^n = 12 => 2^n = 4 => n = 2. Overall order = 1 + 2 = 3. (1)"),
        ("Q16", "B", "k increases exponentially with temperature due to more molecules having E >= Ea; reaction orders depend strictly on mechanism and remain unchanged. (1)"),
        ("Q17", "A", "log10(rate) = log10(k) + 2 log10[A]. Intercept = log10(k) = -1.30 => k = 10^-1.30 = 0.050 dm^3 mol^-1 s^-1. (1)"),
        ("Q18", "B", "CO2 is moderately soluble in water; bubbles only evolve once the liquid becomes saturated with dissolved CO2. (1)"),
        ("Q19", "C", "Polarimeter measures rotation of plane-polarised light as sucrose (+66.5 deg) hydrolyses to invert sugar (-19.7 deg). (1)"),
        ("Q20", "A", "Cold acid stops the catalytic activity of MnO2 and lowers temperature drastically so decomposition freezes before titration. (1)"),
        ("Q21", "A", "Pure solid reactants have constant chemical activity/concentration; reaction rate depends only on exposed surface area, which is zero order. (1)"),
        ("Q22", "A", "Units of k = (mol dm^-3 min^-1) / (mol dm^-3)^3 = dm^6 mol^-2 min^-1. (1)"),
        ("Q23", "A", "For zero order, rate = -d[A]/dt = k => [A]t = -k t + [A]0 (linear negative slope). (1)"),
        ("Q24", "C", "Integrated second order rate law: 1/[A]t = kt + 1/[A]0 (linear positive slope). (1)"),
        ("Q25", "B", "Blank calibration eliminates absorbance, reflection, and scatter from cuvette walls and solvent. (1)"),
        ("Q26", "A", "Total volume must be constant so that volume of reactant solution is directly proportional to its concentration. (1)"),
        ("Q27", "C", "Rate of formation of C = (3/2) * rate of consumption of A = 1.5 * 0.048 = 0.072 mol dm^-3 s^-1. (1)"),
        ("Q28", "C", "New rate proportional to (3) * (1/3) = 1. Rate remains completely unchanged. (1)"),
        ("Q29", "B", "Rate is proportional to [A]; doubling [A] doubles rate, so the time taken to halve any concentration is constant (t1/2 = ln 2 / k). (1)"),
        ("Q30", "A", "Reaction accelerates as temperature rises, so measured rates and apparent k will increase over time. (1)")
    ]

    story.append(Paragraph("<b>SECTION A ANSWER KEY & EXPLANATIONS (30 MARKS)</b>", S['cov_h2']))
    t_ms_a_data = [[Paragraph(f"<b>{q}</b>", S['tbl_th']), Paragraph(f"<b>Key: {ans}</b>", S['tbl_th']), Paragraph(exp, S['tbl_td_l'])] for q, ans, exp in ms_a]
    t_ms_a = Table(t_ms_a_data, colWidths=[1.5*cm, 2.2*cm, 12.3*cm])
    t_ms_a.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_ms_a)
    story.append(Spacer(1, 0.4 * cm))

    # Section B & C Mark Schemes
    ms_long = [
        ("QUESTION 31: Acid-Catalysed Iodination of Propanone (18 Marks)", [
            ("(a) Suitability of Colorimetry", "Brown/yellow iodine is consumed so absorbance decreases continuously without opening reaction vessel (1).\nFilter: 400-470 nm / blue filter (complementary colour to yellow/brown) (1).\nCalibration: Absorbance plotted against known standard concentrations of I2 to verify Beer-Lambert straight line (1).", 3),
            ("(b) Order Deductions", "Compare Exp 1 & 2: [I2] and [H+] constant; [propanone] doubles (0.400 -> 0.800), rate doubles (1.40x10^-6 -> 2.80x10^-6) => Order with respect to propanone = 1 (2).\nCompare Exp 1 & 3: [propanone] and [H+] constant; [I2] doubles (0.00200 -> 0.00400), rate unchanged (1.40x10^-6) => Order with respect to I2 = 0 (2).\nCompare Exp 1 & 4: [propanone] and [I2] constant; [H+] doubles (0.400 -> 0.800), rate doubles (1.40x10^-6 -> 2.80x10^-6) => Order with respect to H+ = 1 (2).", 6),
            ("(c) Rate Equation & k", "Rate = k[CH3COCH3][H+] (1).\nk = Rate / ([CH3COCH3][H+]) = 1.40 x 10^-6 / (0.400 * 0.400) = 8.75 x 10^-6 (1).\nUnits: mol dm^-3 s^-1 / (mol dm^-3)^2 = dm^3 mol^-1 s^-1 (1).", 3),
            ("(d) [I2] vs Time Graph", "Straight line with constant negative gradient down to zero (1).\nZero order means rate of consumption of I2 is constant (-d[I2]/dt = constant) and independent of [I2] (2).", 3),
            ("(e) Role of H+ Catalyst", "H+ acts as a homogeneous catalyst (1).\nParticipates in the slow rate-determining step (protonation of propanone / enol formation) (1).\nRegenerated in a fast step when enol reacts with iodine, so it does not appear in the overall stoichiometric equation (1).", 3),
        ]),

        ("QUESTION 32: Peroxodisulfate–Iodide Clock Reaction (18 Marks)", [
            ("(a) Mechanism of Clock", "Reaction 1 produces I2 slowly. Reaction 2 consumes I2 instantaneously by reacting with S2O3^2- to form I- and S4O6^2- (1).\nAs long as S2O3^2- remains, no free I2 can accumulate, so solution remains colourless (1).\nThe instant all S2O3^2- is completely exhausted, the very next trace of I2 formed reacts with starch indicator (1) to form a dark blue-black starch-triiodide complex at time t (1).", 4),
            ("(b) Data Analysis & k", "(i) Compare Runs 1 & 2: [I-] constant; [S2O8^2-] doubles, time t halves (88 -> 44 s) so rate doubles => Order in S2O8^2- = 1 (1). Compare Runs 1 & 3: [S2O8^2-] constant; [I-] doubles, time halves => Order in I- = 1 (1).\n(ii) In Run 1: [S2O8^2-] = (10.0 x 0.050) / 50.0 = 0.010 mol dm^-3 (1); [I-] = (10.0 x 0.100) / 50.0 = 0.020 mol dm^-3 (1).\n(iii) Moles S2O8^2- reacted = 0.5 * moles S2O3^2- = 2.5 x 10^-5 mol. Delta[S2O8^2-] = 2.5 x 10^-5 / 0.050 dm^3 = 5.0 x 10^-4 mol dm^-3. Initial rate = 5.0 x 10^-4 / 88.0 s = 5.68 x 10^-6 mol dm^-3 s^-1 (2).\n(iv) k = Rate / ([S2O8^2-][I-]) = 5.68 x 10^-6 / (0.010 * 0.020) = 0.0284 (or 2.84 x 10^-2) dm^3 mol^-1 s^-1 (2).", 8),
            ("(c) Thiosulfate Amount", "Thiosulfate must be in small limiting amount so only a tiny fraction (<10%) of persulfate and iodide react before the colour change (1).\nThis ensures concentrations of S2O8^2- and I- remain practically constant, so average rate measured equals the true initial rate (2).", 3),
            ("(d) Constant Total Volume", "(1) Ensures the volume of each reactant solution is directly proportional to its concentration (1).\n(2) Keeps total ionic strength and depth of solution constant across all runs (2).", 3),
        ]),

        ("QUESTION 33: Alkaline Hydrolysis of an Ester (18 Marks)", [
            ("(a) Conductimetry", "OH- ions have very high molar conductivity (mobility), whereas CH3COO- ions formed have much lower mobility (1).\nAs OH- is consumed and replaced by CH3COO-, total conductance decreases linearly with conversion (1).\nConductivity probe is non-invasive and provides continuous real-time data without removing samples (1).", 3),
            ("(b) Quenching Procedure", "Pipette 10.0 cm^3 aliquot into a known excess of ice-cold standard dilute HCl (1).\nAcid neutralises OH- instantaneously, stopping the forward reaction immediately (1).\nIce-water alone only slows the reaction by lowering temperature, but hydrolysis continues during titration, introducing systematic error (1).\nUnreacted HCl is back-titrated with standard NaOH using phenolphthalein indicator (1).", 4),
            ("(c) Pseudo-First-Order & k", "(i) [OH-] is in 40-fold excess (0.600 vs 0.0150 mol dm^-3); change in [OH-] is negligible (<2.5%), so [OH-] is virtually constant (2).\nRate = k[ester][OH-] = k'[ester] where k' = k[OH-] (1).\n(ii) Gradient of ln[ester] vs t = -k' => k' = 0.0660 s^-1 (2).\nk = k' / [OH-] = 0.0660 / 0.600 = 0.110 dm^3 mol^-1 s^-1 (2).", 7),
            ("(d) Half-Life Evaluation", "t1/2 = ln 2 / k' = 0.693 / 0.0660 = 10.5 s (2).\nIf [OH-] doubles to 1.20 mol dm^-3, k' doubles (k' = k[OH-]) (1).\nSince t1/2 = ln 2 / k', the half-life will halve to 5.25 s (1).", 4),
        ]),

        ("QUESTION 34: Decomposition of H2O2 & Practical Evaluation (18 Marks)", [
            ("*(a) Level of Response Evaluation", "Level 3 (5-6 marks): Comprehensive comparative evaluation addressing both methods across all 4 key descriptors:\n(1) Gas syringe: Direct, non-invasive volume reading; errors include friction in plunger causing sticking/pressure build-up, and gas volume sensitivity to temperature fluctuations (PV=nRT).\n(2) Loss-in-mass: Low sensitivity because O2 has low molar mass (32 g/mol); for 100 cm^3 O2, mass lost is only 0.133 g, which on a 0.01 g balance has ~7.5% apparatus uncertainty.\n(3) Aerosol/spray loss: Effervescence ejects liquid droplets causing overestimated mass loss unless a loose cotton wool plug is used.\n(4) Solubility: O2 has slight aqueous solubility in both methods, causing minor lag at start.\nLevel 2 (3-4 marks): Discusses both methods with 2-3 valid points.\nLevel 1 (1-2 marks): Superficial comparison with single valid point.", 6),
            ("(b) Half-Life Verification", "V_inf = 68.0 cm^3. (V_inf - V) represents unreacted [H2O2] (1).\nAt t = 0: (V_inf - V) = 68.0 cm^3.\nFirst half-life: value drops to 34.0 cm^3. Occurs at t = 68 s (t1/2(1) = 68 s) (2).\nSecond half-life: value drops to 17.0 cm^3. Occurs at t = 136 s (t1/2(2) = 136 - 68 = 68 s) (2).\nSuccessive half-lives are constant (68 s and 68 s) within experimental error, confirming first-order kinetics with respect to H2O2 (1).", 6),
            ("(c) Initial Rate Calculation", "Initial rate in gas volume = 32.0 cm^3 / 50 s = 0.640 cm^3 s^-1 (1).\nMoles of O2 per second = 0.640 / 24,000 = 2.67 x 10^-5 mol s^-1 (1).\nMoles of H2O2 consumed = 2 * 2.67 x 10^-5 = 5.33 x 10^-5 mol s^-1.\nRate of H2O2 consumption = (5.33 x 10^-5) / 0.0250 dm^3 = 2.13 x 10^-3 mol dm^-3 s^-1 (1).", 3),
            ("(d) Rate Constant k", "k = ln 2 / t1/2 = 0.693 / 68 s = 0.0102 s^-1 (or 1.02 x 10^-2 s^-1) (2).\nUnits: s^-1 (1).", 3),
        ]),

        ("QUESTION 35: Gas-Phase Kinetics of NO and H2 (18 Marks)", [
            ("(a) Pressure Monitoring", "4 moles of gaseous reactants (2NO + 2H2) produce 3 moles of gaseous products (N2 + 2H2O at T > 100 °C) (1).\nTotal moles of gas decrease, so total pressure drops at constant volume and temperature, directly proportional to reaction extent (1).\nTemperature must exceed 100 °C to prevent water vapour from condensing to liquid water, which would cause an unpredictable large pressure drop (1).", 3),
            ("(b) Rate Law, k and R4", "(i) Compare Exp 1 & 2: [H2] constant; [NO] doubles, rate quadruples (3.60 -> 14.40 x 10^-5) => Order with respect to NO = 2 (2).\nCompare Exp 1 & 3: [NO] constant; [H2] triples (2.00 -> 6.00), rate triples (3.60 -> 10.80 x 10^-5) => Order with respect to H2 = 1 (2).\n(ii) Rate = k[NO]^2 [H2] (1).\nk = Rate / ([NO]^2 [H2]) = 3.60 x 10^-5 / ((1.50 x 10^-3)^2 * (2.00 x 10^-3)) = 8.00 x 10^3 (or 8000) (2).\nUnits: (mol dm^-3 s^-1) / (mol dm^-3)^3 = dm^6 mol^-2 s^-1 (1).\n(iii) R4 = (8000) * (4.50 x 10^-3)^2 * (4.00 x 10^-3) = 6.48 x 10^-4 mol dm^-3 s^-1 (1).", 9),
            ("(c) Compression Effects", "(i) Compressing volume to 1/3 triples the concentration of each gas (3x) (1).\n(ii) Rate proportional to [NO]^2 [H2] => new rate = (3)^2 * (3)^1 = 27 times initial rate (3).\n(iii) The rate constant k is unaffected because k is strictly constant at a fixed temperature and is independent of concentration or volume changes (2).", 6),
        ]),

        ("QUESTION 36: Decolorisation of Crystal Violet (15 Marks)", [
            ("(a) Calibration Protocol", "Pipette precise volumes of 1.00 x 10^-4 mol dm^-3 stock CV+ into volumetric flasks to produce 5 standard concentrations (e.g. 2.0, 4.0, 6.0, 8.0, 10.0 x 10^-5 mol dm^-3) (1).\nZero colorimeter using cuvette of pure deionised water (blank) (1).\nMeasure absorbance of each standard at 590 nm (1).\nPlot absorbance against [CV+] to confirm a straight line passing through the origin (Beer-Lambert Law) (1).", 4),
            ("(b) Isolation Method", "[OH-] is 5000 times greater than [CV+] (0.100 vs 2.00 x 10^-5 mol dm^-3) (1).\nEven after complete reaction, [OH-] drops by at most 0.02%, so [OH-] is effectively constant (1).\nRate = k[CV+]^m [OH-]^n = k'[CV+]^m where k' = k[OH-]^n (pseudo-order rate law) (1).", 3),
            ("(c) Proof & k'", "A = eps * l * [CV+] => [CV+] = A / (eps * l) (1).\nFor first-order: ln[CV+]t = -k' t + ln[CV+]0 (1).\nSubstituting gives ln(At / eps*l) = -k' t + ln(A0 / eps*l) => ln At - ln(eps*l) = -k' t + ln A0 - ln(eps*l) => ln At = -k' t + ln A0 (1).\nLinear plot confirms order m = 1 with respect to crystal violet (1).\nk' = -gradient = 0.0185 s^-1 (1).", 5),
            ("(d) Order in OH- and k", "When [OH-] doubles from 0.100 to 0.200 mol dm^-3, gradient k' doubles from 0.0185 to 0.0370 s^-1 => Order n = 1 with respect to OH- (1).\nRate = k[CV+][OH-] (1).\nk = k' / [OH-] = 0.0185 / 0.100 = 0.185 dm^3 mol^-1 s^-1 (1).", 3),
        ]),

        ("QUESTION 37: Acid-Catalysed Inversion of Sucrose (15 Marks)", [
            ("(a) Polarimeter Principles", "Monochromatic light passes through a polarising filter to produce plane-polarised light (1).\nLight passes through the sample cell containing optically active sugar solution; plane of polarisation is rotated by angle alpha (1).\nAnalyser prism rotated until light transmission matches reference point (1).\nNamed 'inversion' because optical rotation inverts from positive dextrorotatory (+66.5 deg) to net negative laevorotatory (-19.7 deg) because fructose rotates light more strongly to the left (-92.4 deg) than glucose rotates to the right (+52.7 deg) (1).", 4),
            ("(b) Half-Life Proof & k", "At t = 0 min: (alpha_0 - alpha_inf) = 32.0 deg.\nFirst half-life: drops to 16.0 deg at t = 40 min => t1/2(1) = 40 min (1).\nSecond half-life: drops to 8.0 deg at t = 80 min => t1/2(2) = 80 - 40 = 40 min (1).\nConstant half-life (40 min) confirms first order with respect to sucrose (1).\nk = ln 2 / t1/2 = 0.693 / 40 min = 0.0173 min^-1 (or 2.89 x 10^-4 s^-1) (1).", 4),
            ("(c) Dilatometry Justification", "During hydrolysis, a molecule of water is consumed and incorporated into two separate monosaccharide molecules (1).\nThe glucose and fructose molecules pack differently with water, forming more compact hydration shells (1).\nThis causes a slight net volume contraction of the solution, which can be measured precisely as a meniscus fall in a narrow capillary dilatometer (1).", 3),
            ("(d) Conductivity Unsuitability", "All reactants (sucrose, water) and products (glucose, fructose) are neutral non-ionic covalent molecules (1).\nThe catalyst H+ and its counterion remain constant in concentration, so electrical conductivity remains completely unchanged throughout the reaction (1).", 2),
            ("(e) HCl vs CH3COOH", "HCl is a strong acid that fully dissociates ([H+] = 1.0 mol dm^-3), whereas CH3COOH is a weak acid that only partially dissociates ([H+] approx 0.0042 mol dm^-3) (1).\nSince rate is directly proportional to [H+], the initial rate using HCl will be roughly 240 times faster than with ethanoic acid (1).", 2),
        ]),
    ]

    for qtitle, parts in ms_long:
        story.append(Paragraph(f"<b>{qtitle}</b>", S['cov_h2']))
        rows = []
        for plbl, pans, pmrk in parts:
            p_lbl_cell = Paragraph(f"<b>{plbl}</b>", S['ms_qtitle'])
            p_ans_cell = Paragraph(pans.replace('\n', '<br/>'), S['ms_text'])
            p_mrk_cell = Paragraph(f"<b>[{pmrk}]</b>", S['ms_mark'])
            rows.append([p_lbl_cell, p_ans_cell, p_mrk_cell])

        t_ms = Table(rows, colWidths=[4.2*cm, 10.3*cm, 1.5*cm])
        t_ms.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), LIGHT_BG),
            ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
            ('INNERGRID', (0, 0), (-1, -1), 0.4, BORDER),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(t_ms)
        story.append(Spacer(1, 0.3 * cm))

    return story

def compile_quiz_pdf():
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    doc = BaseDocTemplate(
        OUT_FILE, pagesize=A4,
        leftMargin=L_MARGIN, rightMargin=R_MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id='normal'
    )
    template = PageTemplate(id='main', frames=frame, onPage=draw_header_footer)
    doc.addPageTemplates([template])

    print("[1/2] Generating document story for Week 1 150-Mark Quiz...")
    story = build_exam_story()

    print(f"[2/2] Compiling PDF to {OUT_FILE} ...")
    doc.build(story)

    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"[SUCCESS] Week 1 150-Mark Quiz generated successfully! Size: {size_mb:.2f} MB")
    return OUT_FILE

if __name__ == "__main__":
    compile_quiz_pdf()
