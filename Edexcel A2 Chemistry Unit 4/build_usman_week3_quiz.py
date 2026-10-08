"""
build_usman_week3_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 3 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 11A.5: Activation Energy and Catalysis (Maxwell-Boltzmann Distributions, Homogeneous & Heterogeneous Catalysis)
  - 11A.6: Effect of Temperature on the Rate Constant (The Arrhenius Equation, ln k vs 1/T Graphs)

Structure:
  - Page 1: Official Pearson Edexcel Candidate Front Cover & Number Grid
  - Pages 2–11: Section A — Multiple Choice Questions (Q1 to Q30, 30 Marks, 3 per page with checkbox blanks)
  - Pages 12–24: Section B — Core Structured Questions (Q31 to Q35, 90 Marks, 18 marks each)
  - Pages 25–28: Section C — Contemporary Synoptic & Practical Data Response (Q36 to Q37, 30 Marks, 15 marks each)
  - Page 29: Data Sheet — Periodic Table of Elements & Formulae / Constants
  - Pages 30–35: Confidential Teacher Mark Scheme & Examiner Trap Commentary (150 Marks)
"""

import os
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Table, TableStyle, HRFlowable, Flowable, KeepTogether
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
# COLOUR PALETTE
# ──────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0b1b36")
CRIMSON    = colors.HexColor("#a81717")
STEEL      = colors.HexColor("#1e3a8a")
LIGHT_BG   = colors.HexColor("#f8fafc")
MID_BG     = colors.HexColor("#f1f5f9")
BORDER     = colors.HexColor("#cbd5e1")
DARK_TXT   = colors.HexColor("#1e293b")
LINE_CLR   = colors.HexColor("#94a3b8")
WHITE      = colors.white

PAGE_W, PAGE_H = A4
L_MARGIN = R_MARGIN = 1.5 * cm
TOP_MARGIN = BOTTOM_MARGIN = 1.5 * cm
AVAIL_W = PAGE_W - L_MARGIN - R_MARGIN

OUT_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Usman_Edexcel_Chem_U4_Week3_150M_Challenging_Quiz.pdf"
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
    'edx_top':     _ps('EdxTop',     fontName=FONT['Bold'], fontSize=8.5, textColor=DARK_TXT),
    'edx_title':   _ps('EdxTitle',   fontName=FONT['Bold'], fontSize=20, textColor=NAVY, leading=24),
    'edx_sub':     _ps('EdxSub',     fontName=FONT['Bold'], fontSize=11, textColor=STEEL, spaceAfter=8),
    'edx_unit':    _ps('EdxUnit',    fontName=FONT['Bold'], fontSize=13, textColor=NAVY, leading=16),
    'edx_meta':    _ps('EdxMeta',    fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=14),
    'edx_meta_b':  _ps('EdxMetaB',  fontName=FONT['Bold'], fontSize=9, textColor=DARK_TXT),

    'sec_header':  _ps('SecHdr',    fontName=FONT['Bold'], fontSize=12, textColor=NAVY, spaceAfter=4),
    'sec_instr':   _ps('SecIns',    fontName=FONT['Regular'], fontSize=8.8, textColor=DARK_TXT, leading=13),

    'q_num':       _ps('QNum',      fontName=FONT['Bold'], fontSize=10, textColor=NAVY),
    'q_stem':      _ps('QStem',     fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=14),
    'q_equation':  _ps('QEqn',      fontName=FONT['Mono'], fontSize=9, textColor=NAVY, leading=14, alignment=1),
    'q_subpart':   _ps('QSubPart',  fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT, leading=14, leftIndent=16),
    'q_submark':   _ps('QSubMark',  fontName=FONT['Bold'], fontSize=8.5, textColor=NAVY, alignment=2),
    'q_total':     _ps('QTotal',    fontName=FONT['Bold'], fontSize=8.8, textColor=NAVY, alignment=2),

    'opt_letter':  _ps('OptLet',    fontName=FONT['Bold'], fontSize=9, textColor=NAVY, alignment=1),
    'opt_text':    _ps('OptTxt',    fontName=FONT['Regular'], fontSize=8.8, textColor=DARK_TXT, leading=12.5),

    'ans_prompt':  _ps('AnsPrm',    fontName=FONT['Bold'], fontSize=8.8, textColor=NAVY, leftIndent=16),

    'tbl_th':      _ps('TblTH',     fontName=FONT['Bold'], fontSize=8.2, textColor=WHITE, alignment=1),
    'tbl_td':      _ps('TblTD',     fontName=FONT['Regular'], fontSize=8.2, textColor=DARK_TXT, alignment=1),
    'tbl_td_l':    _ps('TblTDL',   fontName=FONT['Regular'], fontSize=8.2, textColor=DARK_TXT, alignment=0),

    'ms_qtitle':   _ps('MSQTitle',  fontName=FONT['Bold'], fontSize=9, textColor=NAVY),
    'ms_text':     _ps('MSText',    fontName=FONT['Regular'], fontSize=8.2, textColor=DARK_TXT, leading=12),
    'ms_mark':     _ps('MSMark',    fontName=FONT['Bold'], fontSize=8.2, textColor=CRIMSON, alignment=2),

    'cov_h1':      _ps('CovH1',     fontName=FONT['Bold'], fontSize=16, textColor=NAVY, alignment=1, leading=20),
    'cov_h2':      _ps('CovH2',     fontName=FONT['Bold'], fontSize=11, textColor=STEEL, spaceAfter=8),
}

# ──────────────────────────────────────────────────────────────
# CUSTOM FLOWABLES FOR REAL EXAM BOOKLET
# ──────────────────────────────────────────────────────────────
class DottedAnswerLines(Flowable):
    """Draws authentic Edexcel exam dotted handwriting lines spaced at 7.2 mm."""
    def __init__(self, num_lines, width=AVAIL_W, line_height=0.72*cm, color=LINE_CLR):
        super().__init__()
        self.num_lines = num_lines
        self.width = width
        self.line_height = line_height
        self.color = color

    def wrap(self, availWidth, availHeight):
        return self.width, self.num_lines * self.line_height

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(0.6)
        self.canv.setDash(1, 2.5)
        for i in range(self.num_lines):
            y = (self.num_lines - 1 - i) * self.line_height + 2
            self.canv.line(0, y, self.width, y)
        self.canv.restoreState()


class GraphSketchBox(Flowable):
    """Draws a clean coordinate graph sketch box with labeled axes for student drawings."""
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="ln k", x_label="1/T / 10^-3 K^-1"):
        super().__init__()
        self.width = width
        self.height = height
        self.y_label = y_label
        self.x_label = x_label

    def wrap(self, availWidth, availHeight):
        return self.width, self.height

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(BORDER)
        self.canv.setLineWidth(0.8)
        self.canv.rect(0, 0, self.width, self.height)

        ox = 45
        oy = 26
        ax_w = self.width - ox - 30
        ax_h = self.height - oy - 25

        self.canv.setStrokeColor(NAVY)
        self.canv.setLineWidth(1.2)
        self.canv.line(ox, oy, ox, oy + ax_h)
        self.canv.line(ox, oy, ox + ax_w, oy)

        self.canv.line(ox, oy + ax_h, ox - 3, oy + ax_h - 6)
        self.canv.line(ox, oy + ax_h, ox + 3, oy + ax_h - 6)
        self.canv.line(ox + ax_w, oy, ox + ax_w - 6, oy - 3)
        self.canv.line(ox + ax_w, oy, ox + ax_w - 6, oy + 3)

        self.canv.setFont(FONT['Regular'], 8)
        self.canv.setFillColor(NAVY)
        self.canv.drawRightString(ox - 5, oy - 10, "0")

        self.canv.setFont(FONT['Bold'], 8)
        self.canv.drawCentredString(ox + ax_w / 2, oy - 18, self.x_label)

        self.canv.saveState()
        self.canv.translate(ox - 20, oy + ax_h / 2)
        self.canv.rotate(90)
        self.canv.drawCentredString(0, 0, self.y_label)
        self.canv.restoreState()

        self.canv.restoreState()


def make_mcq_row(letter, text, width=AVAIL_W):
    t = Table([
        ['', Paragraph(f"<b>{letter}</b>", S['opt_letter']), Paragraph(text, S['opt_text'])]
    ], colWidths=[0.38*cm, 0.45*cm, width - 0.83*cm])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (0, 0), 0.8, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


def question_total(qnum, marks):
    text = f"<b>(Total for Question {qnum} = {marks} mark{'s' if marks > 1 else ''})</b>"
    t = Table([
        [HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=4)],
        [Paragraph(text, S['q_total'])]
    ], colWidths=[AVAIL_W])
    t.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


# ──────────────────────────────────────────────────────────────
# RUNNING HEADER / FOOTER
# ──────────────────────────────────────────────────────────────
def draw_page_chrome(canvas, doc):
    if doc.page == 1:
        return
    canvas.saveState()

    canvas.setFont(FONT['Bold'], 7.5)
    canvas.setFillColor(NAVY)
    canvas.drawString(L_MARGIN, PAGE_H - 1.0 * cm, "Pearson Edexcel International Advanced Level")

    canvas.setFont(FONT['Medium'], 7.5)
    canvas.setFillColor(STEEL)
    canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 1.0 * cm, "Chemistry Unit 4 - Week 3 Challenge Assessment")

    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(L_MARGIN, PAGE_H - 1.12 * cm, PAGE_W - R_MARGIN, PAGE_H - 1.12 * cm)

    canvas.line(L_MARGIN, 1.25 * cm, PAGE_W - R_MARGIN, 1.25 * cm)
    canvas.setFont(FONT['Regular'], 7)
    canvas.setFillColor(DARK_TXT)
    canvas.drawString(L_MARGIN, 0.85 * cm, "Candidate: Usman  |  Mentora Academy Examination Protocol")

    canvas.setFont(FONT['Bold'], 7.5)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.setFont(FONT['SemiBold'], 6.5)
    canvas.setFillColor(STEEL)
    canvas.drawCentredString(PAGE_W / 2.0, 0.50 * cm, "mentoraonlineacademy@gmail.com   |   +923164586836")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# STORY BUILDER
# ──────────────────────────────────────────────────────────────
def build_exam_story():
    story = []

    # ══════════════════════════════════════════════════════════
    # PAGE 1: OFFICIAL EDEXCEL CANDIDATE COVER PAGE
    # ══════════════════════════════════════════════════════════
    box_w = 0.52 * cm
    t_cgrid = Table([[
        Paragraph("Please check the examination details below before entering your candidate information", S['edx_meta']),
        ''
    ], [
        Table([
            [Paragraph("<b>Candidate surname:</b>", S['edx_top']), Paragraph("USMAN", S['edx_meta_b'])],
            [Paragraph("<b>Other names:</b>", S['edx_top']), Paragraph("Grade A* Scholar", S['edx_meta'])]
        ], colWidths=[3.5*cm, 4.5*cm]),
        Table([
            [Paragraph("<b>Centre Number</b>", S['edx_top']), Paragraph("<b>Candidate Number</b>", S['edx_top'])],
            [
                Table([['', '', '', '', '']], colWidths=[box_w]*5, rowHeights=[0.55*cm],
                      style=[('BOX', (0,0), (-1,-1), 0.8, NAVY), ('INNERGRID', (0,0), (-1,-1), 0.5, NAVY)]),
                Table([['', '', '', '']], colWidths=[box_w]*4, rowHeights=[0.55*cm],
                      style=[('BOX', (0,0), (-1,-1), 0.8, NAVY), ('INNERGRID', (0,0), (-1,-1), 0.5, NAVY)])
            ]
        ], colWidths=[4.2*cm, 3.6*cm])
    ]], colWidths=[8.5*cm, 7.5*cm])
    t_cgrid.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1.0, NAVY),
        ('SPAN', (0, 0), (1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), MID_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_cgrid)
    story.append(Spacer(1, 0.4 * cm))

    story.append(Paragraph("Pearson Edexcel International Advanced Level", S['edx_sub']))
    story.append(Paragraph("Chemistry", S['edx_title']))
    story.append(Paragraph("International Advanced Level<br/>UNIT 4: Rates, Equilibria and Further Organic Chemistry", S['edx_unit']))
    story.append(Spacer(1, 0.2 * cm))

    p_meta_tbl = Table([
        [Paragraph("<b>Paper Reference:</b> WCH14/01/W3-REV", S['edx_meta_b']),
         Paragraph("<b>Time Allowed:</b> 2 hours 30 minutes", S['edx_meta_b'])],
        [Paragraph("<b>Topic Focus:</b> 11A.5 Activation Energy & 11A.6 The Arrhenius Equation", S['edx_meta']),
         Paragraph("<b>Total Marks:</b> 150 Marks", S['edx_meta_b'])],
    ], colWidths=[AVAIL_W/2, AVAIL_W/2])
    p_meta_tbl.setStyle(TableStyle([
        ('LINEBELOW', (0, -1), (-1, -1), 1.0, NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(p_meta_tbl)
    story.append(Spacer(1, 0.4 * cm))

    edx_instructions = (
        "<b>INSTRUCTIONS</b><br/>"
        "• <b>Use black ink</b> or black ball-point pen.<br/>"
        "• <b>Fill in the boxes</b> at the top of this page with your name, centre number and candidate number.<br/>"
        "• <b>Answer all questions.</b><br/>"
        "• <b>Answer the questions in the spaces provided</b> — there may be more space than you need.<br/>"
        "• <b>Show all the steps in any calculations</b> and state the units of numerical values.<br/>"
        "• <b>Calculators may be used.</b><br/><br/>"
        "<b>INFORMATION</b><br/>"
        "• The total mark for this paper is <b>150</b>.<br/>"
        "• The marks for each question are shown in brackets — <i>use this as a guide as to how much time to spend on each question.</i><br/>"
        "• In questions marked with an asterisk (<b>*</b>), marks will be awarded for your ability to structure your answer logically, showing how the points that you make are related or follow on from each other.<br/>"
        "• A Periodic Table is printed on the back page of this question paper.<br/><br/>"
        "<b>ADVICE</b><br/>"
        "• Read each question carefully before you start to answer it.<br/>"
        "• Keep an eye on the time.<br/>"
        "• Try to answer every question.<br/>"
        "• Check your answers if you have time at the end."
    )
    t_ins = Table([[Paragraph(edx_instructions, S['sec_instr'])]], colWidths=[AVAIL_W])
    t_ins.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1.0, NAVY),
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_ins)
    story.append(Spacer(1, 0.5 * cm))

    m_badge = Table([[
        Paragraph("<font color='#0b1b36'><b>MENTORA ACADEMY</b></font> &nbsp;•&nbsp; "
                  "<font color='#a81717'><b>WEEK 3 ACTIVATION ENERGY & ARRHENIUS MASTERY EXAM</b></font><br/>"
                  "Prepared exclusively for candidate <b>USMAN</b> · Strict timed simulation conditions",
                  S['tbl_td'])
    ]], colWidths=[AVAIL_W])
    m_badge.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.8, STEEL),
        ('BACKGROUND', (0, 0), (-1, -1), MID_BG),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(m_badge)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION A: MULTIPLE CHOICE QUESTIONS (QUESTIONS 1 TO 30)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION A</b>", S['sec_header']))
    story.append(Paragraph(
        "<b>Answer ALL questions in this section.</b><br/>"
        "You should spend no more than <b>40 minutes</b> on this section.<br/>"
        "Use the spaces provided in this question paper.<br/>"
        "For each question, select one answer from A to D and put a cross in the box [X].<br/>"
        "If you change your mind, put a line through the box and then mark your new answer with a cross.<br/>",
        S['sec_instr']
    ))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=8, spaceBefore=4))

    mcqs = [
        (1, "In the Arrhenius equation, k = A e^(-Ea / RT), what does the pre-exponential factor A represent?",
         [('A', "The minimum energy required for reaction."), ('B', "The fraction of collisions that possess energy greater than or equal to Ea."), ('C', "The frequency of collisions occurring with the correct spatial orientation."), ('D', "The rate of reaction at absolute zero.")]),

        (2, "A plot of ln k against 1/T for a reaction yields a straight line with a gradient of -9620 K. What is the activation energy of the reaction in kJ mol^-1? (R = 8.314 J mol^-1 K^-1)",
         [('A', "+80.0 kJ mol^-1"), ('B', "+1.16 kJ mol^-1"), ('C', "-80.0 kJ mol^-1"), ('D', "+9.62 kJ mol^-1")]),

        (3, "When a catalyst is added to a reaction mixture at constant temperature, what is the effect on the Maxwell-Boltzmann distribution curve and the activation energy?",
         [('A', "The curve peak shifts to the right; the activation energy line remains fixed."), ('B', "The curve shape remains unchanged; the activation energy line shifts to the left."), ('C', "The curve peak shifts downwards; the activation energy line shifts to the right."), ('D', "The total area under the curve increases.")]),

        (4, "For a reaction with activation energy Ea = 52.0 kJ mol^-1, what happens to the rate constant k when the temperature is raised from 300 K to 310 K? (R = 8.314 J mol^-1 K^-1)",
         [('A', "k increases by a factor of approx. 1.03"), ('B', "k approximately doubles (factor of approx. 1.96)"), ('C', "k increases by a factor of 10"), ('D', "k remains unchanged")]),

        (5, "In a heterogeneous catalytic reaction on a solid metal surface, which step involves the attachment of reactant molecules to active sites with bond weakening?",
         [('A', "Diffusion"), ('B', "Chemisorption"), ('C', "Desorption"), ('D', "Condensation")]),

        (6, "Why does leaded petrol ruin a vehicle's catalytic converter?",
         [('A', "Lead burns inside the converter causing thermal cracking."), ('B', "Lead coats the platinum/rhodium active sites irreversibly (catalytic poisoning)."), ('C', "Lead oxidises nitrogen monoxide to nitrogen dioxide."), ('D', "Lead reacts with oxygen to form volatile lead oxide.")]),

        (7, "The reaction S2O8^2- + 2I- -> 2SO4^2- + I2 is very slow uncatalysed because of:",
         [('A', "High positive enthalpy of reaction."), ('B', "High activation energy due to electrostatic repulsion between two negatively charged ions."), ('C', "Iodide ions precipitating from solution."), ('D', "Sulfate ions decomposing rapidly.")]),

        (8, "When Fe^2+ ions catalyse the reaction between S2O8^2- and I-, why is the catalysed pathway much faster?",
         [('A', "Iron ions are in a different physical state."), ('B', "Both steps involve collisions between oppositely charged ions (Fe^2+ with S2O8^2- and Fe^3+ with I-), avoiding like-charge repulsion."), ('C', "Iron ions shift the position of equilibrium towards products."), ('D', "Iron ions increase the temperature of the mixture.")]),

        (9, "In the titration of ethanedioic acid with potassium manganate(VII), the reaction starts very slowly but accelerates rapidly after a few seconds. This is an example of:",
         [('A', "Heterogeneous catalysis"), ('B', "Autocatalysis by Mn^2+ ions formed during the reaction"), ('C', "Enzymatic inhibition"), ('D', "Thermal runaway")]),

        (10, "What are the units of the Arrhenius pre-exponential factor A for a second-order reaction?",
         [('A', "s^-1"), ('B', "mol dm^-3 s^-1"), ('C', "dm^3 mol^-1 s^-1"), ('D', "dm^6 mol^-2 s^-1")]),

        (11, "Which of the following expressions correctly relates the rate constants k1 and k2 at temperatures T1 and T2?",
         [('A', "ln(k2 / k1) = (Ea / R) * (1/T1 - 1/T2)"), ('B', "ln(k2 / k1) = (Ea / R) * (1/T2 - 1/T1)"), ('C', "ln(k2 / k1) = -(R / Ea) * (T2 - T1)"), ('D', "k2 / k1 = e^(-Ea / R(T2 - T1))")]),

        (12, "Why does the rate of an enzyme-catalysed reaction collapse catastrophically when the temperature rises above 60 °C?",
         [('A', "The substrate concentration falls to zero."), ('B', "Thermal energy breaks hydrogen bonds and tertiary folding, denaturing the enzyme's active site."), ('C', "The activation energy of the reaction becomes negative."), ('D', "The enzyme converts into a heterogeneous catalyst.")]),

        (13, "On a Maxwell-Boltzmann distribution, what does the area under the curve to the right of Ea represent?",
         [('A', "The total number of molecules in the system."), ('B', "The fraction of molecules possessing kinetic energy greater than or equal to the activation energy."), ('C', "The average kinetic energy of the molecules."), ('D', "The rate constant of the reaction.")]),

        (14, "When temperature increases, what happens to the peak of the Maxwell-Boltzmann distribution curve?",
         [('A', "Shifts upwards and to the left."), ('B', "Shifts downwards and to the right."), ('C', "Remains at the same energy but increases in height."), ('D', "Shifts to the right with no change in height.")]),

        (15, "A reaction has zero activation energy (Ea = 0). What is the relationship between the rate constant k and temperature T?",
         [('A', "k is directly proportional to T."), ('B', "k is completely independent of temperature (k = A)."), ('C', "k decreases exponentially with temperature."), ('D', "k drops to zero.")]),

        (16, "For a reaction with Ea = 100 kJ mol^-1, which of the following changes will produce the largest percentage increase in the rate constant k?",
         [('A', "Increasing T from 300 K to 310 K"), ('B', "Increasing T from 500 K to 510 K"), ('C', "Increasing T from 700 K to 710 K"), ('D', "All 10 K increases produce the exact same percentage increase")]),

        (17, "In the contact process, sulfur dioxide is oxidised to sulfur trioxide using vanadium(V) oxide (V2O5) catalyst. What is the oxidation state of vanadium in the reduced intermediate?",
         [('A', "+2"), ('B', "+3"), ('C', "+4"), ('D', "+5")]),

        (18, "Which transition metal property is most responsible for their effectiveness as homogeneous and heterogeneous catalysts?",
         [('A', "High electrical conductivity"), ('B', "Variable oxidation states and partially filled d-orbitals that can donate or accept electrons"), ('C', "High melting and boiling points"), ('D', "Low first ionisation energies")]),

        (19, "A student plots ln k against 1/T and forgets to convert temperatures from °C to Kelvin. What will be the consequence for the plotted line?",
         [('A', "The line will still be straight with the exact same gradient."), ('B', "The plot will become curved and the calculated activation energy will be meaningless."), ('C', "The gradient will be doubled."), ('D', "The y-intercept will become zero.")]),

        (20, "In the Sabatier principle for heterogeneous catalysis, why is a metal that adsorbs reactants extremely strongly unsuitable as an effective catalyst?",
         [('A', "Reactants cannot diffuse to the surface."), ('B', "Product molecules cannot desorb from the active sites, permanently blocking the catalyst surface."), ('C', "The metal dissolves in the gas phase."), ('D', "The activation energy increases above the uncatalysed value.")]),

        (21, "For a reaction with Ea = 60.0 kJ mol^-1, by what factor does k increase when a catalyst is added that reduces Ea to 30.0 kJ mol^-1 at 298 K? (R = 8.314 J mol^-1 K^-1)",
         [('A', "2"), ('B', "100"), ('C', "approx. 1.8 x 10^5"), ('D', "approx. 1.2 x 10^2")]),

        (22, "What is the physical significance of the y-intercept in an Arrhenius plot of ln k against 1/T?",
         [('A', "Activation energy Ea"), ('B', "ln A (the natural logarithm of the pre-exponential factor)"), ('C', "The rate at T = 298 K"), ('D', "-Ea / R")]),

        (23, "Why does a 10 K temperature rise have a much greater percentage effect on a reaction with high Ea compared to a reaction with low Ea?",
         [('A', "Because high Ea reactions have higher pre-exponential factors."), ('B', "Because the exponential term e^(-Ea/RT) changes by a much larger fraction when Ea is large."), ('C', "Because high Ea reactions are always endothermic."), ('D', "Because collision frequency increases faster for high Ea reactions.")]),

        (24, "In an industrial reactor, an iron catalyst becomes poisoned by sulfur impurities in the feed gas. What type of catalytic inhibition has occurred?",
         [('A', "Reversible homogeneous competitive inhibition"), ('B', "Irreversible heterogeneous surface blocking"), ('C', "Enzyme allosteric feedback"), ('D', "Thermal denaturation")]),

        (25, "Which statement correctly describes the action of a catalyst on an equilibrium reaction?",
         [('A', "Increases the rate of the forward reaction more than the reverse reaction, increasing Kc."), ('B', "Lowers Ea for both forward and reverse reactions by the exact same amount, leaving Kc unchanged."), ('C', "Decreases the time taken to reach equilibrium and increases product yield."), ('D', "Increases the activation energy of the reverse reaction.")]),

        (26, "The rate constant of a reaction is 1.2 x 10^-3 s^-1 at 300 K and 4.8 x 10^-3 s^-1 at 320 K. What is the activation energy of the reaction?",
         [('A', "55.3 kJ mol^-1"), ('B', "11.2 kJ mol^-1"), ('C', "28.5 kJ mol^-1"), ('D', "82.4 kJ mol^-1")]),

        (27, "Which method is commonly used to regenerate a coked (carbon-fouled) zeolite catalyst in petroleum cracking?",
         [('A', "Washing with liquid nitrogen"), ('B', "Burning off the deposited carbon in a stream of hot air (oxygen)"), ('C', "Dissolving the zeolite in concentrated acid"), ('D', "Exposing the zeolite to gamma radiation")]),

        (28, "For the reaction 2HI -> H2 + I2, gold surfaces act as a heterogeneous catalyst. When the concentration of HI is very high, the reaction becomes zero order. Why?",
         [('A', "Gold atoms evaporate from the surface."), ('B', "All active catalytic sites on the gold surface are completely saturated with adsorbed HI molecules."), ('C', "The reaction mechanism changes to SN1."), ('D', "The reaction reaches chemical equilibrium instantaneously.")]),

        (29, "A reaction has k = 0.050 s^-1 at 300 K and Ea = 40.0 kJ mol^-1. What is the value of k at 350 K?",
         [('A', "0.45 s^-1"), ('B', "0.050 s^-1"), ('C', "0.82 s^-1"), ('D', "0.10 s^-1")]),

        (30, "A catalyst provides an alternative pathway with an activation energy that is 20 kJ mol^-1 lower. At 300 K, the rate increases by a factor of approx. 3000. At 600 K, the rate enhancement factor is:",
         [('A', "Much larger (approx. 10^6)"), ('B', "Much smaller (approx. 55)"), ('C', "Exactly the same (3000)"), ('D', "Zero (no catalysis occurs at 600 K)")]),
    ]

    for i, (qnum, qtext, opts) in enumerate(mcqs, 1):
        q_block = []
        p_q = Paragraph(f"<b>{qnum}</b>&nbsp;&nbsp;{qtext}", S['q_stem'])
        q_block.append(p_q)
        q_block.append(Spacer(1, 0.15 * cm))

        for ltr, otxt in opts:
            q_block.append(make_mcq_row(ltr, otxt))
            q_block.append(Spacer(1, 0.08 * cm))

        q_block.append(Spacer(1, 0.15 * cm))
        q_block.append(Paragraph(f"<b>(Total for Question {qnum} = 1 mark)</b>", S['q_total']))
        q_block.append(Spacer(1, 0.3 * cm))

        if i < len(mcqs):
            q_block.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=2))

        story.append(KeepTogether(q_block))

        if i % 3 == 0 and i < len(mcqs):
            story.append(PageBreak())

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION B: STRUCTURED CORE QUESTIONS (QUESTIONS 31 TO 35)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION B</b>", S['sec_header']))
    story.append(Paragraph("<b>Answer ALL questions. Write your answers in the spaces provided.</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=12, spaceBefore=4))

    # ──────────────────────────────────────────────────────────
    # QUESTION 31 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Nitrogen monoxide reacts with ozone in the gas phase according to the reaction:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("NO(g) &nbsp;+&nbsp; O<sub>3</sub>(g) &nbsp;—&gt;&nbsp; NO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The rate constant, <i>k</i>, was measured at five different temperatures. The experimental data are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Temperature <i>T</i> / K</b>", S['tbl_th']), Paragraph("200", S['tbl_td']), Paragraph("220", S['tbl_td']), Paragraph("240", S['tbl_td']), Paragraph("260", S['tbl_td']), Paragraph("280", S['tbl_td'])],
        [Paragraph("<b>1/<i>T</i> / 10<sup>-3</sup> K<sup>-1</sup></b>", S['tbl_th']), Paragraph("5.00", S['tbl_td']), Paragraph("4.55", S['tbl_td']), Paragraph("4.17", S['tbl_td']), Paragraph("3.85", S['tbl_td']), Paragraph("3.57", S['tbl_td'])],
        [Paragraph("<b><i>k</i> / dm<sup>3</sup> mol<sup>-1</sup> s<sup>-1</sup></b>", S['tbl_th']), Paragraph("1.30 × 10<sup>5</sup>", S['tbl_td']), Paragraph("3.25 × 10<sup>5</sup>", S['tbl_td']), Paragraph("7.10 × 10<sup>5</sup>", S['tbl_td']), Paragraph("1.41 × 10<sup>6</sup>", S['tbl_td']), Paragraph("2.56 × 10<sup>6</sup>", S['tbl_td'])],
        [Paragraph("<b>ln <i>k</i></b>", S['tbl_th']), Paragraph("11.78", S['tbl_td']), Paragraph("12.69", S['tbl_td']), Paragraph("13.47", S['tbl_td']), Paragraph("14.16", S['tbl_td']), Paragraph("14.76", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[4.0*cm] + [2.4*cm]*5)
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t31)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> On the axes below, sketch the graph of ln <i>k</i> against 1/<i>T</i>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(AVAIL_W, 6.2*cm, y_label="ln k", x_label="1/T / 10^-3 K^-1"))
    story.append(Spacer(1, 0.25 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the gradient of the line from the data points at <i>T</i> = 200 K and <i>T</i> = 280 K. Include the sign and units of the gradient.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Gradient = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 31 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Using your gradient from (b), calculate the activation energy, <i>E</i><sub>a</sub>, of the reaction in kJ mol<sup>-1</sup>. (<i>R</i> = 8.314 J mol<sup>-1</sup> K<sup>-1</sup>)", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>E</i><sub>a</sub> = ................................................................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the pre-exponential factor, <i>A</i>, for the reaction using data at <i>T</i> = 200 K. State the units of <i>A</i>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>A</i> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Explain the physical meaning of the pre-exponential factor <i>A</i>. Why is the experimental value of <i>A</i> for this reaction smaller than the total collision frequency calculated from simple kinetic collision theory?", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(f)</b> State the assumption made about the activation energy, <i>E</i><sub>a</sub>, and the pre-exponential factor, <i>A</i>, across the temperature range studied.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;The Maxwell-Boltzmann distribution describes the distribution of molecular energies in gases and liquids.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> On the axes below, sketch the Maxwell-Boltzmann energy distribution curves for a fixed mass of gas at two temperatures, <i>T</i><sub>1</sub> and <i>T</i><sub>2</sub>, where <i>T</i><sub>2</sub> &gt; <i>T</i><sub>1</sub>.<br/>"
                   "Label your curves clearly. Mark the activation energy for the uncatalysed reaction, <i>E</i><sub>a</sub>, and the catalysed reaction, <i>E</i><sub>cat</sub>. Shade the region representing molecules that react at <i>T</i><sub>1</sub> in the presence of a catalyst.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(AVAIL_W, 6.8*cm, y_label="Fraction of molecules", x_label="Molecular kinetic energy / E"))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The fraction of molecules with energy greater than or equal to the activation energy is given by <i>f</i> = e<sup>-<i>E</i><sub>a</sub> / <i>RT</i></sup>.<br/>"
                   "For a reaction with <i>E</i><sub>a</sub> = 55.0 kJ mol<sup>-1</sup>:<br/>"
                   "<b>(i)</b> Calculate the fraction <i>f</i><sub>1</sub> at 298 K.<br/>"
                   "<b>(ii)</b> Calculate the fraction <i>f</i><sub>2</sub> at 308 K.<br/>"
                   "<b>(iii)</b> Hence show that a 10 K rise in temperature approximately doubles the number of reacting particles.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "<i>f</i><sub>1</sub> (at 298 K) = .........................................................................................................................<br/>"
        "<i>f</i><sub>2</sub> (at 308 K) = .........................................................................................................................<br/>"
        "Ratio <i>f</i><sub>2</sub> / <i>f</i><sub>1</sub> = .....................................................................................................................",
        S['ans_prompt']
    ))
    story.append(PageBreak())

    # Question 32 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> When temperature increases, collision frequency increases slightly (by approx. 2% for a 10 K rise), yet reaction rate often increases by over 100%. Explain why the increase in collision frequency contributes so little to the rate increase compared to the change in the fraction <i>f</i>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Contrast how an increase in temperature accelerates a reaction compared to how the addition of a catalyst accelerates a reaction. In your answer, refer explicitly to the Maxwell-Boltzmann distribution and the potential energy reaction coordinate.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Heterogeneous catalysts are used extensively in motor vehicle catalytic converters and industrial chemical synthesis.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Describe the five successive stages of the mechanism by which a solid heterogeneous catalyst (such as platinum) catalyses a gas-phase reaction. Your answer should explain the difference between adsorption and absorption.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> According to the Sabatier principle, an effective heterogeneous catalyst must have an optimum strength of chemisorption.<br/>"
                   "Explain why:<br/>"
                   "<b>(i)</b> Metals that adsorb reactants too weakly (such as silver) are ineffective catalysts.<br/>"
                   "<b>(ii)</b> Metals that adsorb reactants too strongly (such as tungsten) are ineffective catalysts.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(PageBreak())

    # Question 33 Parts (c), (d)
    story.append(Paragraph("<b>(c)</b> In a three-way catalytic converter, platinum, palladium, and rhodium convert toxic exhaust gases into harmless emissions:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Reaction 1: 2NO(g) + 2CO(g) —&gt; N<sub>2</sub>(g) + 2CO<sub>2</sub>(g)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Reaction 2: 2C<sub>8</sub>H<sub>18</sub>(g) + 25O<sub>2</sub>(g) —&gt; 16CO<sub>2</sub>(g) + 18H<sub>2</sub>O(g)", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Table([
        [Paragraph("<b>(i)</b> Explain why the catalyst in a converter is supported as an ultra-thin washcoat on a ceramic honeycomb honeycomb structure rather than used as solid metal pellets.<br/>"
                   "<b>(ii)</b> Explain why catalytic converters are completely ineffective when an engine is first started from cold.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Catalytic poisoning is a major cause of catalyst deactivation.<br/>"
                   "<b>(i)</b> Explain how sulfur compounds present in fossil fuels poison iron catalysts in the Haber process.<br/>"
                   "<b>(ii)</b> Distinguish between reversible catalyst poisoning and irreversible catalyst poisoning.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Homogeneous catalysts operate in the same physical state as the reacting species.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part *(a) - Level of Response
    story.append(Table([
        [Paragraph("<b>*(a) Extended Writing:</b> Transition metal ions frequently act as homogeneous catalysts in redox reactions.<br/>"
                   "Compare and evaluate the catalytic mechanisms and kinetic rate profiles of:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<b>Case 1:</b> The catalysis of the reaction between peroxodisulfate(VI) and iodide ions by Fe<sup>2+</sup> or Fe<sup>3+</sup> ions.<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<b>Case 2:</b> The autocatalysis of the reaction between acidified manganate(VII) ions and ethanedioate ions by Mn<sup>2+</sup> ions.<br/>"
                   "In your answer, discuss: ionic charge repulsion, variable oxidation states, two-stage catalytic cycles, induction periods, and sketch the shape of the concentration-time curve for an autocatalytic reaction.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(14, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (b), (c)
    story.append(Table([
        [Paragraph("<b>(b)</b> Write two balanced equations showing the two-stage catalytic cycle when Fe<sup>2+</sup> catalyses the oxidation of iodide by peroxodisulfate:", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Stage 1 (reduction of persulfate): ....................................................................................................................................................<br/>"
                           "Stage 2 (oxidation of iodide): ..........................................................................................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why the reaction between acidified manganate(VII) and ethanedioate ions exhibits a noticeable 'induction period' where the purple colour remains for several seconds before suddenly decolourising rapidly.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> In an uncatalysed reaction, the activation energy is 82.0 kJ mol<sup>-1</sup>. In the presence of a homogeneous catalyst, the activation energy is reduced to 46.0 kJ mol<sup>-1</sup>.<br/>"
                   "Assuming the pre-exponential factor <i>A</i> remains identical, calculate the factor by which the rate constant <i>k</i> increases at 298 K.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Rate enhancement factor = .................................................................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;The industrial synthesis of sulfur trioxide in the Contact process is an exothermic equilibrium reaction:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2SO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2SO<sub>3</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;Δ<i>H</i> = -196 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The reaction is catalysed by solid vanadium(V) oxide (V<sub>2</sub>O<sub>5</sub>). The rate constant for the catalysed forward reaction was measured at two temperatures:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;At <i>T</i><sub>1</sub> = 650 K, &nbsp;<i>k</i><sub>1</sub> = 1.20 × 10<sup>-2</sup> dm<sup>3</sup> mol<sup>-1</sup> s<sup>-1</sup><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;At <i>T</i><sub>2</sub> = 720 K, &nbsp;<i>k</i><sub>2</sub> = 4.80 × 10<sup>-2</sup> dm<sup>3</sup> mol<sup>-1</sup> s<sup>-1</sup>", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> State the two-point form of the Arrhenius equation relating <i>k</i><sub>1</sub>, <i>k</i><sub>2</sub>, <i>T</i><sub>1</sub>, <i>T</i><sub>2</sub>, and <i>E</i><sub>a</sub>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Arrhenius equation: .....................................................................................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the activation energy, <i>E</i><sub>a</sub>, of the catalysed reaction in kJ mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>E</i><sub>a</sub> = ................................................................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the rate constant, <i>k</i><sub>3</sub>, at the operating temperature of 700 K.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>k</i><sub>3</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 35 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> Write two equations to show how V<sub>2</sub>O<sub>5</sub> acts as a catalyst by undergoing a cyclic redox change involving V(IV) oxide (VO<sub>2</sub>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> An industrial chemist considers raising the temperature of the converter to 800 K to achieve a faster rate of reaction.<br/>"
                   "Explain why an excessively high temperature is disadvantageous in this industrial process, referring to both reaction kinetics and equilibrium yield.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(35, 18))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION C: SYNOPTIC & EXPERIMENTAL DATA RESPONSE (30 MARKS)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION C</b>", S['sec_header']))
    story.append(Paragraph("<b>Answer ALL questions. Write your answers in the spaces provided.</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=12, spaceBefore=4))

    # ──────────────────────────────────────────────────────────
    # QUESTION 36 (15 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;The temperature dependence of the reaction between bromate(V) ions and bromide ions in acidic solution was investigated using an iodine clock variation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("BrO<sub>3</sub><sup>-</sup>(aq) &nbsp;+&nbsp; 5Br<sup>-</sup>(aq) &nbsp;+&nbsp; 6H<sup>+</sup>(aq) &nbsp;—&gt;&nbsp; 3Br<sub>2</sub>(aq) &nbsp;+&nbsp; 3H<sub>2</sub>O(l)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Phenol and methyl red indicator were added. Bromine reacts instantaneously with phenol. When all phenol is consumed, free bromine bleaches the methyl red indicator permanently. The time taken, <i>t</i>, for bleaching was measured at various temperatures:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t36_data = [
        [Paragraph("<b>Temperature θ / °C</b>", S['tbl_th']), Paragraph("20.0", S['tbl_td']), Paragraph("28.0", S['tbl_td']), Paragraph("36.0", S['tbl_td']), Paragraph("44.0", S['tbl_td']), Paragraph("52.0", S['tbl_td'])],
        [Paragraph("<b>Temperature <i>T</i> / K</b>", S['tbl_th']), Paragraph("293.0", S['tbl_td']), Paragraph("301.0", S['tbl_td']), Paragraph("309.0", S['tbl_td']), Paragraph("317.0", S['tbl_td']), Paragraph("325.0", S['tbl_td'])],
        [Paragraph("<b>1/<i>T</i> / 10<sup>-3</sup> K<sup>-1</sup></b>", S['tbl_th']), Paragraph("3.41", S['tbl_td']), Paragraph("3.32", S['tbl_td']), Paragraph("3.24", S['tbl_td']), Paragraph("3.15", S['tbl_td']), Paragraph("3.08", S['tbl_td'])],
        [Paragraph("<b>Time <i>t</i> / s</b>", S['tbl_th']), Paragraph("142.0", S['tbl_td']), Paragraph("78.0", S['tbl_td']), Paragraph("45.0", S['tbl_td']), Paragraph("26.0", S['tbl_td']), Paragraph("16.0", S['tbl_td'])],
        [Paragraph("<b>ln(1/<i>t</i>)</b>", S['tbl_th']), Paragraph("-4.96", S['tbl_td']), Paragraph("-4.36", S['tbl_td']), Paragraph("-3.81", S['tbl_td']), Paragraph("-3.26", S['tbl_td']), Paragraph("-2.77", S['tbl_td'])],
    ]
    t36 = Table(t36_data, colWidths=[3.8*cm] + [2.44*cm]*5)
    t36.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t36)
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why 1/<i>t</i> can be taken as a direct measure of the initial rate of reaction in this investigation.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Since rate ∝ 1/<i>t</i>, the Arrhenius relationship can be written as ln(1/<i>t</i>) = -<i>E</i><sub>a</sub> / <i>RT</i> + constant.<br/>"
                   "Calculate the gradient of the line from the data at <i>T</i> = 293 K and <i>T</i> = 325 K, and determine the activation energy, <i>E</i><sub>a</sub>, in kJ mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Gradient = ............................................................................................................................. K<br/>"
        "<i>E</i><sub>a</sub> = ................................................................................................................................... kJ mol<sup>-1</sup>",
        S['ans_prompt']
    ))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> State two major experimental difficulties encountered when carrying out this experiment at temperatures above 50 °C.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Suggest one modification to the experimental apparatus to improve the accuracy of temperature control throughout the run.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;The catalytic decomposition of hydrogen peroxide was investigated using three different catalyst regimes:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2H<sub>2</sub>O<sub>2</sub>(aq) &nbsp;—&gt;&nbsp; 2H<sub>2</sub>O(l) &nbsp;+&nbsp; O<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The activation energies for the reaction under the three conditions are:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Regime 1 (Uncatalysed):</b> &nbsp;<i>E</i><sub>a</sub> = 75.0 kJ mol<sup>-1</sup><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Regime 2 (MnO<sub>2</sub> solid catalyst):</b> &nbsp;<i>E</i><sub>a</sub> = 54.0 kJ mol<sup>-1</sup><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Regime 3 (Catalase enzyme):</b> &nbsp;<i>E</i><sub>a</sub> = 8.0 kJ mol<sup>-1</sup>", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Assuming the pre-exponential factor <i>A</i> is the same for all three pathways, calculate the factor by which the rate constant <i>k</i> increases at 298 K when:<br/>"
                   "<b>(i)</b> Solid MnO<sub>2</sub> is added to uncatalysed H<sub>2</sub>O<sub>2</sub>.<br/>"
                   "<b>(ii)</b> Catalase enzyme is added to uncatalysed H<sub>2</sub>O<sub>2</sub>.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Rate factor increase with MnO<sub>2</sub> = ............................................................................................<br/>"
        "Rate factor increase with Catalase = ............................................................................................",
        S['ans_prompt']
    ))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Sketch the rate against temperature curve for the reaction catalysed by MnO<sub>2</sub> and the reaction catalysed by catalase on the same axes. Explain the dramatic difference between the two curves at temperatures above 50 °C.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(PageBreak())

    # Question 37 Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why biological enzymes achieve far greater reductions in activation energy than inorganic solid catalysts. In your response, refer to induced-fit transition state stabilisation.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(37, 15))
    story.append(Spacer(1, 0.4 * cm))

    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=8, spaceBefore=4))
    story.append(Table([
        [Paragraph("<b>TOTAL FOR SECTION C = 30 MARKS</b>", S['tbl_td_l']),
         Paragraph("<b>TOTAL FOR PAPER = 150 MARKS</b>", S['q_total'])],
        [Paragraph("<b>END OF QUESTION PAPER</b>", S['edx_title']), '']
    ], colWidths=[AVAIL_W/2, AVAIL_W/2]))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # DATA SECTION: PERIODIC TABLE OF THE ELEMENTS
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>DATA SHEET - THE PERIODIC TABLE OF THE ELEMENTS</b>", S['cov_h2']))
    story.append(Spacer(1, 0.15 * cm))

    ptable_raw = [
        ["1\nH\n1.0", "", "", "", "", "", "", "2\nHe\n4.0"],
        ["3\nLi\n6.9", "4\nBe\n9.0", "5\nB\n10.8", "6\nC\n12.0", "7\nN\n14.0", "8\nO\n16.0", "9\nF\n19.0", "10\nNe\n20.2"],
        ["11\nNa\n23.0", "12\nMg\n24.3", "13\nAl\n27.0", "14\nSi\n28.1", "15\nP\n31.0", "16\nS\n32.1", "17\nCl\n35.5", "18\nAr\n39.9"],
        ["19\nK\n39.1", "20\nCa\n40.1", "31\nGa\n69.7", "32\nGe\n72.6", "33\nAs\n74.9", "34\nSe\n79.0", "35\nBr\n79.9", "36\nKr\n83.8"],
        ["37\nRb\n85.5", "38\nSr\n87.6", "49\nIn\n114.8", "50\nSn\n118.7", "51\nSb\n121.8", "52\nTe\n127.6", "53\nI\n126.9", "54\nXe\n131.3"],
        ["55\nCs\n132.9", "56\nBa\n137.3", "81\nTl\n204.4", "82\nPb\n207.2", "83\nBi\n209.0", "84\nPo\n[209]", "85\nAt\n[210]", "86\nRn\n[222]"],
    ]
    pt_rows = [[Paragraph("<b>Group 1</b>", S['tbl_th']), Paragraph("<b>Group 2</b>", S['tbl_th']),
                Paragraph("<b>Group 3</b>", S['tbl_th']), Paragraph("<b>Group 4</b>", S['tbl_th']),
                Paragraph("<b>Group 5</b>", S['tbl_th']), Paragraph("<b>Group 6</b>", S['tbl_th']),
                Paragraph("<b>Group 7</b>", S['tbl_th']), Paragraph("<b>Group 0</b>", S['tbl_th'])]]
    for r in ptable_raw:
        pt_rows.append([Paragraph(cell.replace('\n', '<br/>'), S['tbl_td']) if cell else Paragraph('-', S['tbl_td']) for cell in r])

    t_pt = Table(pt_rows, colWidths=[AVAIL_W/8]*8)
    t_pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_pt)
    story.append(Spacer(1, 0.4 * cm))

    const_data = [
        [Paragraph("<b>Physical Constant / Formula</b>", S['tbl_th']), Paragraph("<b>Symbol / Expression</b>", S['tbl_th']), Paragraph("<b>Value & Units</b>", S['tbl_th'])],
        [Paragraph("Gas constant", S['tbl_td_l']), Paragraph("<i>R</i>", S['tbl_td']), Paragraph("8.314 J mol<sup>-1</sup> K<sup>-1</sup>", S['tbl_td'])],
        [Paragraph("Molar volume of gas at r.t.p.", S['tbl_td_l']), Paragraph("<i>V</i><sub>m</sub>", S['tbl_td']), Paragraph("24.0 dm<sup>3</sup> mol<sup>-1</sup> (24,000 cm<sup>3</sup> mol<sup>-1</sup>)", S['tbl_td'])],
        [Paragraph("Arrhenius equation", S['tbl_td_l']), Paragraph("<i>k</i>", S['tbl_td']), Paragraph("<i>k</i> = <i>A</i> e<sup>-<i>E</i><sub>a</sub> / <i>RT</i></sup>", S['tbl_td'])],
        [Paragraph("Arrhenius logarithmic form", S['tbl_td_l']), Paragraph("ln <i>k</i>", S['tbl_td']), Paragraph("ln <i>k</i> = -<i>E</i><sub>a</sub> / <i>R</i> (1/<i>T</i>) + ln <i>A</i>", S['tbl_td'])],
        [Paragraph("Arrhenius two-temperature form", S['tbl_td_l']), Paragraph("ln(<i>k</i><sub>2</sub>/<i>k</i><sub>1</sub>)", S['tbl_td']), Paragraph("ln(<i>k</i><sub>2</sub>/<i>k</i><sub>1</sub>) = (<i>E</i><sub>a</sub> / <i>R</i>)(1/<i>T</i><sub>1</sub> - 1/<i>T</i><sub>2</sub>)", S['tbl_td'])],
    ]
    t_const = Table(const_data, colWidths=[6.0*cm, 4.0*cm, 6.0*cm])
    t_const.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_const)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # TEACHER'S MARK SCHEME & EXAMINER COMMENTARY (CONFIDENTIAL)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>PEARSON EDEXCEL INTERNATIONAL ADVANCED LEVEL</b>", S['cov_h2']))
    story.append(Paragraph("CHEMISTRY UNIT 4 (WCH14/01) — ADVANCED MASTERY QUIZ", S['cov_h1']))
    story.append(Paragraph("<b>CONFIDENTIAL TEACHER'S MARK SCHEME & EXAMINER GUIDANCE (150 MARKS)</b>", S['sec_header']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    ms_a = [
        ("Q1", "C", "A is the pre-exponential factor, representing collision frequency with correct orientation. (1)"),
        ("Q2", "A", "Gradient = -Ea / R => -9620 = -Ea / 8.314 => Ea = 9620 * 8.314 = 79,980 J mol^-1 = +80.0 kJ mol^-1. (1)"),
        ("Q3", "B", "A catalyst provides an alternative pathway with lower Ea; the distribution curve of molecular kinetic energies is unchanged at constant T. (1)"),
        ("Q4", "B", "ln(k2/k1) = (52000 / 8.314) * (1/300 - 1/310) = 6254.5 * (1.075 x 10^-4) = 0.672 => k2/k1 = e^0.672 = 1.96 (doubles). (1)"),
        ("Q5", "B", "Chemisorption is the chemical bonding of reactant molecules to catalyst surface active sites. (1)"),
        ("Q6", "B", "Lead forms strong irreversible bonds with catalytic metal sites, preventing reactants from adsorbing. (1)"),
        ("Q7", "B", "Both S2O8^2- and I- carry negative charges, creating strong electrostatic repulsion and high Ea. (1)"),
        ("Q8", "B", "Iron alternates between Fe^2+ and Fe^3+; in each step, a positive iron ion reacts with a negative ion, avoiding repulsion. (1)"),
        ("Q9", "B", "Mn^2+ produced during the reaction acts as a homogeneous catalyst, accelerating the reaction (autocatalysis). (1)"),
        ("Q10", "C", "In k = A e^(-Ea/RT), the exponential term is dimensionless, so A must have the exact same units as k (dm^3 mol^-1 s^-1 for second order). (1)"),
        ("Q11", "A", "ln(k2/k1) = -Ea/R (1/T2 - 1/T1) = (Ea/R)(1/T1 - 1/T2). (1)"),
        ("Q12", "B", "High temperatures disrupt weak hydrogen bonds and tertiary folding, permanently destroying active site complementarity. (1)"),
        ("Q13", "B", "The shaded area beyond Ea represents the proportion of molecules with sufficient energy to react. (1)"),
        ("Q14", "B", "Increasing T spreads the distribution to higher energies; the peak flattens (lowers) and moves to the right. (1)"),
        ("Q15", "B", "When Ea = 0, e^(-Ea/RT) = e^0 = 1, so k = A, completely independent of temperature. (1)"),
        ("Q16", "A", "The fractional increase in e^(-Ea/RT) is greatest at lower temperatures (300 -> 310 K). (1)"),
        ("Q17", "C", "V2O5 is reduced by SO2 to vanadium(IV) oxide (VO2), where V is in the +4 oxidation state. (1)"),
        ("Q18", "B", "Variable oxidation states allow transition metals to accept and donate electrons in multi-step catalytic cycles. (1)"),
        ("Q19", "B", "The Arrhenius equation requires absolute thermodynamic temperature in Kelvin; using °C makes the plot non-linear. (1)"),
        ("Q20", "B", "If adsorption is too strong, product molecules cannot desorb, permanently blocking surface active sites. (1)"),
        ("Q21", "C", "k_cat / k_uncat = e^(Delta Ea / RT) = e^(30000 / (8.314 * 298)) = e^12.11 = 1.8 x 10^5. (1)"),
        ("Q22", "B", "In ln k = -Ea/R (1/T) + ln A, at 1/T = 0, the y-intercept is ln A. (1)"),
        ("Q23", "B", "e^(-Ea/RT) has a steeper temperature gradient when Ea is large, producing a greater proportional rate acceleration. (1)"),
        ("Q24", "B", "Sulfur bonds irreversibly to surface active sites of iron, causing irreversible heterogeneous poisoning. (1)"),
        ("Q25", "B", "A catalyst lowers Ea by the same amount in both directions, speeding up forward and reverse rates equally without altering Kc. (1)"),
        ("Q26", "A", "ln(4.8/1.2) = ln(4) = 1.3863 = (Ea / 8.314) * (1/300 - 1/320) = (Ea/8.314)*(2.083 x 10^-4) => Ea = 55.3 kJ mol^-1. (1)"),
        ("Q27", "B", "Coke deposits are oxidised by heating in air: C(s) + O2(g) -> CO2(g), restoring clear pores. (1)"),
        ("Q28", "B", "At high reactant concentration, all available surface catalytic sites become fully occupied (saturated), making rate independent of concentration. (1)"),
        ("Q29", "A", "ln(k2 / 0.050) = (40000 / 8.314) * (1/300 - 1/350) = 4811 * 4.76 x 10^-4 = 2.29 => k2 = 0.050 * e^2.29 = 0.45 s^-1. (1)"),
        ("Q30", "B", "Rate enhancement factor = e^(20000 / (8.314 * 600)) = e^4.01 = 55. (Much smaller than at 300 K). (1)")
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

    # Long Questions Mark Scheme
    ms_long = [
        ("QUESTION 31: Arrhenius Kinetics of NO + O3 Reaction (18 Marks)", [
            ("(a) ln k vs 1/T Graph", "Straight line with constant negative gradient (2).\nProperly oriented axes with negative slope passing through plotted points (1).", 2),
            ("(b) Gradient Calculation", "Gradient = (14.76 - 11.78) / (3.57 x 10^-3 - 5.00 x 10^-3) = 2.98 / (-1.43 x 10^-3) (2).\n= -2084 K (allow -2070 to -2100 K) (1).", 3),
            ("(c) Activation Energy Ea", "Gradient = -Ea / R => -2084 = -Ea / 8.314 (1).\nEa = 2084 * 8.314 = 17,326 J mol^-1 = +17.3 kJ mol^-1 (allow +17.2 to +17.5 kJ mol^-1) (2).", 3),
            ("(d) Pre-Exponential Factor A", "ln k = ln A - Ea/RT => 11.78 = ln A - (17326 / (8.314 * 200)) (1).\n11.78 = ln A - 10.42 => ln A = 22.20 (1).\nA = e^22.20 = 4.38 x 10^9 (allow 4.0 x 10^9 to 4.8 x 10^9) (1).\nUnits: dm^3 mol^-1 s^-1 (same units as k for second order) (1).", 4),
            ("(e) Physical Meaning of A", "A represents the frequency of collisions with proper spatial orientation (1).\nA is smaller than simple collision frequency because not all collisions have the correct steric alignment: the nitrogen atom of NO must collide directly with an oxygen atom of O3 for reaction to occur (steric factor p < 1) (2).", 3),
            ("(f) Assumptions Made", "Ea is constant and independent of temperature over 200-280 K (1.5).\nA is constant and independent of temperature over this range (1.5).", 3),
        ]),

        ("QUESTION 32: Maxwell-Boltzmann Distributions (18 Marks)", [
            ("(a) Curves and Shading", "Both curves start at origin (0,0) (1).\nT2 curve peak is lower and shifted to the right of T1 peak (2).\nT2 curve is above T1 curve at high kinetic energies and crosses T1 once (1).\nEcat marked to the left of Ea (1).\nShaded area under T1 to the right of Ecat represents reacting molecules (1).", 6),
            ("(b) Fraction f Calculations", "(i) f1 = e^(-55000 / (8.314 * 298)) = e^(-22.20) = 2.28 x 10^-10 (2).\n(ii) f2 = e^(-55000 / (8.314 * 308)) = e^(-21.48) = 4.70 x 10^-10 (2).\n(iii) Ratio f2 / f1 = (4.70 x 10^-10) / (2.28 x 10^-10) = 2.06 (approx. 2.1x), confirming that the number of particles with E >= Ea approximately doubles (2).", 6),
            ("(c) Collision Frequency vs Fraction", "Collision frequency is proportional to sqrt(T), which increases by only sqrt(308/298) = 1.017 (a 1.7% increase) (1.5).\nHowever, the fraction of collisions with E >= Ea increases exponentially by >100%, which completely dominates the rate acceleration (1.5).", 3),
            ("(d) Temperature vs Catalyst Action", "Temperature increases molecular kinetic energy, shifting the Maxwell-Boltzmann distribution curve so more molecules exceed the unchanged threshold Ea (1.5).\nA catalyst provides an alternative mechanism with a lower activation energy barrier, shifting the threshold line to the left while the distribution curve remains unchanged (1.5).", 3),
        ]),

        ("QUESTION 33: Heterogeneous Catalysis & Converters (18 Marks)", [
            ("(a) Five Stages of Mechanism", "1. Diffusion of gaseous reactant molecules to the catalyst surface (1).\n2. Chemisorption of reactants onto active surface sites with bond weakening (1).\n3. Chemical reaction between adsorbed species on the surface (1).\n4. Desorption of product molecules from active sites (1).\n5. Diffusion of products away from the catalyst surface (1).\nAdsorption is attachment to the surface; absorption is penetration into the bulk interior (1).", 6),
            ("(b) Sabatier Principle", "(i) Weak chemisorption: Reactant molecules do not bind long enough or strongly enough for bonds to weaken, so no catalytic activation occurs (2).\n(ii) Strong chemisorption: Product molecules or reactant fragments remain permanently bound to active sites, blocking them and preventing further catalysis (2).", 4),
            ("(c) Catalytic Converter Engineering", "(i) Honeycomb washcoat provides an enormous surface area of active catalyst with minimal precious metal mass and low exhaust gas back-pressure (2).\n(ii) At cold start, temperature is well below the catalyst light-off temperature (approx. 250 °C); thermal energy is insufficient to overcome Ea (2).", 4),
            ("(d) Poisoning Mechanisms", "(i) Sulfur oxidises to SO2/SO3 which reacts with iron to form stable, non-catalytic iron sulfides/sulfates, irreversibly blocking active sites (2).\n(ii) Reversible poisoning: inhibitor can be desorbed by heating or changing gas flow; Irreversible poisoning: permanent chemical bonding destroys active sites permanently (2).", 4),
        ]),

        ("QUESTION 34: Homogeneous Catalysis & Autocatalysis (18 Marks)", [
            ("*(a) Level of Response Evaluation", "Level 3 (5-6 marks): Comprehensive comparative evaluation addressing both cases with clear links to kinetic curves:\n(1) Fe2+/Fe3+: Avoids like-charge negative repulsion between S2O8^2- and I-; variable oxidation states enable two-stage cycle.\n(2) Autocatalysis: Mn2+ produced in reaction acts as catalyst; reaction exhibits initial induction lag followed by rapid acceleration as [Mn2+] builds up, and finally slows as reactants deplete (sigmoidal S-shaped curve).\nLevel 2 (3-4 marks): Discusses both cases with 2-3 valid points.\nLevel 1 (1-2 marks): Superficial description of one case.", 6),
            ("(b) Two-Stage Fe Cycle Equations", "Stage 1: S2O8^2- + 2Fe^2+ -> 2SO4^2- + 2Fe^3+ (2).\nStage 2: 2Fe^3+ + 2I- -> 2Fe^2+ + I2 (2).", 4),
            ("(c) Induction Period Explanation", "Initially, no Mn^2+ catalyst is present, so the uncatalysed reaction is very slow due to repulsion between negative MnO4^- and C2O4^2- ions (1.5).\nAs soon as initial Mn^2+ ions are produced, they catalyse the reaction, causing rapid autocatalytic acceleration (1.5).", 3),
            ("(d) Rate Enhancement Calculation", "Delta Ea = 82.0 - 46.0 = 36.0 kJ mol^-1 = 36,000 J mol^-1 (1).\nk_cat / k_uncat = e^(Delta Ea / RT) (1).\n= e^(36000 / (8.314 * 298)) = e^(14.53) (2).\n= 2.04 x 10^6 (rate increases by approx. 2 million times) (1).", 5),
        ]),

        ("QUESTION 35: Contact Process Kinetics & Arrhenius (18 Marks)", [
            ("(a) Two-Point Arrhenius Form", "ln(k2 / k1) = (Ea / R) * (1/T1 - 1/T2) (or ln(k2/k1) = -Ea/R (1/T2 - 1/T1)) (2).", 2),
            ("(b) Calculation of Ea", "ln(0.0480 / 0.0120) = ln(4.0) = 1.3863 (1).\n1/T1 - 1/T2 = 1/650 - 1/720 = 1.5385 x 10^-3 - 1.3889 x 10^-3 = 1.496 x 10^-4 K^-1 (1).\n1.3863 = (Ea / 8.314) * (1.496 x 10^-4) (1).\nEa = (1.3863 * 8.314) / (1.496 x 10^-4) = 77,040 J mol^-1 = 77.0 kJ mol^-1 (allow 76.8 to 77.2) (2).", 5),
            ("(c) Rate Constant at 700 K", "ln(k3 / 0.0120) = (77040 / 8.314) * (1/650 - 1/700) (1).\n= 9266 * (1.5385 x 10^-3 - 1.4286 x 10^-3) = 9266 * (1.099 x 10^-4) = 1.018 (1).\nk3 / 0.0120 = e^1.018 = 2.768 => k3 = 0.0120 * 2.768 = 0.0332 dm^3 mol^-1 s^-1 (1).\nUnits: dm^3 mol^-1 s^-1 (1).", 4),
            ("(d) Cyclic Redox Reactions of V2O5", "1. SO2 + V2O5 -> SO3 + 2VO2 (1.5).\n2. 2VO2 + 0.5O2 -> V2O5 (1.5).", 3),
            ("(e) Industrial Temperature Compromise", "Kinetics: Higher temperature increases rate constant k, reaching equilibrium faster (1).\nEquilibrium: The forward reaction is exothermic (Delta H = -196 kJ mol^-1); by Le Chatelier's principle, higher temperature shifts equilibrium to the left, decreasing SO3 yield (2).\nExcessively high temperature also shortens catalyst lifetime by sintering (1).", 4),
        ]),

        ("QUESTION 36: Bromate-Bromide Clock & Arrhenius (15 Marks)", [
            ("(a) 1/t as Rate Measure", "A fixed amount of bromine is produced before bleaching the methyl red indicator (1).\nRate is change in concentration over time: delta[Br2] / t (1).\nSince delta[Br2] is held constant in every run, rate is directly proportional to 1/t (1).", 3),
            ("(b) Gradient & Ea Calculation", "Gradient = (-2.77 - (-4.96)) / (3.08 x 10^-3 - 3.41 x 10^-3) = 2.19 / (-0.33 x 10^-3) = -6636 K (allow -6500 to -6800 K) (3).\nGradient = -Ea / R => -6636 = -Ea / 8.314 (1).\nEa = 6636 * 8.314 = 55,170 J mol^-1 = 55.2 kJ mol^-1 (allow 54.0 to 56.5 kJ mol^-1) (2).", 6),
            ("(c) Experimental Difficulties at High T", "1. Reaction is extremely fast (t = 16 s), making timing errors with a stopwatch a significant percentage uncertainty (1.5).\n2. Evaporation of volatile bromine or phenol, and rapid cooling of solution in an open vessel (1.5).", 3),
            ("(d) Apparatus Improvement", "Use a thermostatted water bath with continuous stirring and pre-equilibrate all reactant solutions before mixing (3).", 3),
        ]),

        ("QUESTION 37: Enzyme vs Inorganic Catalysis of H2O2 (15 Marks)", [
            ("(a) Rate Factor Increases", "(i) Delta Ea(MnO2) = 75.0 - 54.0 = 21.0 kJ mol^-1 = 21,000 J mol^-1.\nFactor = e^(21000 / (8.314 * 298)) = e^(8.476) = 4.80 x 10^3 (approx. 4,800x) (3).\n(ii) Delta Ea(catalase) = 75.0 - 8.0 = 67.0 kJ mol^-1 = 67,000 J mol^-1.\nFactor = e^(67000 / (8.314 * 298)) = e^(27.04) = 5.54 x 10^11 (approx. 550 billion times faster) (3).", 6),
            ("(b) Rate vs Temperature Comparison", "For MnO2, rate increases continuously and exponentially with temperature as more particles exceed Ea (2).\nFor catalase, rate increases up to optimum temperature (approx. 40 °C), then drops sharply to zero because thermal energy breaks tertiary hydrogen bonds, causing irreversible active site denaturation (3).", 5),
            ("(c) Induced-Fit Transition State Theory", "Enzymes have flexible active sites that undergo conformational changes to fit the transition state with precision (induced fit) (2).\nExtensive non-covalent bonding (H-bonds, electrostatic interactions) to the transition state releases large binding energy, dramatically lowering the activation energy compared to rigid metal surfaces (2).", 4),
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
    template = PageTemplate(id='main', frames=frame, onPage=draw_page_chrome)
    doc.addPageTemplates([template])

    print("[1/2] Building authentic Edexcel past-paper story for Week 3 (150 Marks)...")
    story = build_exam_story()

    print(f"[2/2] Compiling publication-grade PDF to {OUT_FILE} ...")
    doc.build(story)

    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"[SUCCESS] Week 3 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")
    return OUT_FILE


if __name__ == "__main__":
    compile_quiz_pdf()
