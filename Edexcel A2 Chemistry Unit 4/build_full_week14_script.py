# -*- coding: utf-8 -*-
"""
build_full_week14_script.py
Generates the complete build_usman_week14_quiz.py script for Week 14 150M Mock Paper 2.
"""

import sys

content = r'''"""
build_usman_week14_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 14 ADVANCED SYNOPTIC TIMED MOCK EXAMINATION 2 (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Examination Time: 2 hours 30 minutes
Paper Reference: WCH14/01 (Mock 2)
Total Marks: 150 Marks

Structure:
  - Page 1: Official Pearson Edexcel Candidate Front Cover & Number Grid
  - Pages 2–11: Section A — Multiple Choice Questions (Q1 to Q30, 30 Marks, 3 per page with checkbox blanks)
  - Pages 12–24: Section B — Core Structured Questions (Q31 to Q35, 90 Marks, 18 marks each)
  - Pages 25–28: Section C — Contemporary Synoptic Case Studies (Q36 to Q37, 30 Marks, 15 marks each)
  - Page 29: Data Sheet — Periodic Table of Elements & Physical Constants
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
            'Regular': 'Helvetica', 'Bold': 'Helvetica-Bold',
            'SemiBold': 'Helvetica-Bold', 'Medium': 'Helvetica',
            'Italic': 'Helvetica-Oblique', 'Mono': 'Courier'
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
    "Usman_Edexcel_Chem_U4_Week14_150M_Challenging_Quiz.pdf"
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


class DiagramBox(Flowable):
    """Draws an authentic bordered box for organic reaction mechanisms and diagrams."""
    def __init__(self, width=AVAIL_W, height=6.0*cm, caption="Space for structural drawings, mechanisms, or calculations"):
        super().__init__()
        self.width = width
        self.height = height
        self.caption = caption

    def wrap(self, availWidth, availHeight):
        return self.width, self.height

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(BORDER)
        self.canv.setLineWidth(0.8)
        self.canv.rect(0, 0, self.width, self.height)

        self.canv.setFont(FONT['Regular'], 8)
        self.canv.setFillColor(LINE_CLR)
        self.canv.drawCentredString(self.width / 2, self.height / 2, self.caption)
        self.canv.restoreState()


class GraphSketchBox(Flowable):
    """Draws a clean coordinate graph sketch box with labeled axes for student drawings."""
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="[I2] / mol dm^-3", x_label="Time / s"):
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

    canvas.setFont(FONT['Regular'], 7.5)
    canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 1.0 * cm, "WCH14/01 -- Unit 4 Chemistry")

    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.4)
    canvas.line(L_MARGIN, PAGE_H - 1.1 * cm, PAGE_W - R_MARGIN, PAGE_H - 1.1 * cm)

    canvas.line(L_MARGIN, 1.25 * cm, PAGE_W - R_MARGIN, 1.25 * cm)

    canvas.setFont(FONT['Regular'], 7.5)
    canvas.setFillColor(DARK_TXT)
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 14 Synoptic Mock 2")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 14 (150 Marks)...")
    doc = BaseDocTemplate(
        OUT_FILE,
        pagesize=A4,
        leftMargin=L_MARGIN,
        rightMargin=R_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    frame = Frame(L_MARGIN, BOTTOM_MARGIN, AVAIL_W, PAGE_H - TOP_MARGIN - BOTTOM_MARGIN,
                  id='main_frame', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    template = PageTemplate(id='exam_page', frames=frame, onPage=draw_page_chrome)
    doc.addPageTemplates([template])

    story = []

    # ══════════════════════════════════════════════════════════
    # PAGE 1: COVER PAGE
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>Please check the examination details below before entering your candidate information</b>", S['edx_top']))
    story.append(Spacer(1, 0.3 * cm))

    tbl_cand = Table([
        [Paragraph("Candidate surname", S['edx_meta']), Paragraph("Other names", S['edx_meta'])],
        [Paragraph("<b>USMAN</b>", S['edx_meta_b']), Paragraph("<b>Grade A* Scholar</b>", S['edx_meta_b'])],
        [Paragraph("Centre Number &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Candidate Number<br/>"
                   "<b>[  9  ][  5  ][  1  ][  0  ][  2  ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
                   "<b>[  0  ][  0  ][  8  ][  8  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W14</b>", S['edx_meta_b'])]
    ], colWidths=[AVAIL_W * 0.55, AVAIL_W * 0.45])
    tbl_cand.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1.0, NAVY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl_cand)
    story.append(Spacer(1, 0.6 * cm))

    story.append(Paragraph("Pearson Edexcel International Advanced Level", S['cov_h2']))
    story.append(Paragraph("Chemistry", S['edx_title']))
    story.append(Paragraph("International Advanced Level<br/>UNIT 4: Rates, Equilibria and Further Organic Chemistry", S['edx_unit']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("<b>WEEK 14: ADVANCED SYNOPTIC TIMED MOCK EXAMINATION PAPER 2 (150 MARKS)</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Full Unit 4 Synoptic Timed Mock 2)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Syllabus Scope:</b>", S['edx_meta']), Paragraph("Topic 11: Kinetics (Continuous Monitoring, Orders, Enolisation Mechanisms)<br/>Topic 12: Solution Energetics (Hydration Enthalpy, Sulfate Solubility Trends)<br/>Topic 13: Equilibria (Contact Process, Multi-stage Kp, Thermodynamic Links)<br/>Topic 14: Acid-Base (Polyprotic Dissociation, Salt Hydrolysis, Indicators)<br/>Topic 15: Organic Chemistry (Carbonyl Addition, PLA Polyesters, Atmospheric Catalysis)", S['edx_meta'])],
    ]
    t_specs = Table(specs, colWidths=[3.8*cm, AVAIL_W - 3.8*cm])
    t_specs.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_specs)
    story.append(Spacer(1, 0.5 * cm))

    instr_text = (
        "<b>INSTRUCTIONS TO CANDIDATES</b><br/>"
        "- Use black ink or ball-point pen. Fill in the boxes at the top of this page.<br/>"
        "- Answer <b>ALL</b> questions in Section A, Section B, and Section C.<br/>"
        "- In Section A (Questions 1 to 30), select your answer by placing a clear cross in the box <b>[X]</b>.<br/>"
        "- In Section B and C, show all working in calculation questions. Include appropriate units where required.<br/>"
        "- Questions marked with an asterisk (<b>*</b>) are those where your quality of written communication and logical sequence of structure will be assessed.<br/>"
        "- A Periodic Table and physical constants are printed on the back page of this booklet.<br/><br/>"
        "<b>INFORMATION FOR CANDIDATES</b><br/>"
        "- The total mark for this paper is <b>150</b>.<br/>"
        "- Section A: 30 marks; Section B: 90 marks; Section C: 30 marks.<br/>"
        "- Full worked confidential teacher mark scheme is provided at the rear for post-assessment diagnostic."
    )
    t_instr = Table([[Paragraph(instr_text, S['edx_meta'])]], colWidths=[AVAIL_W])
    t_instr.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1.0, STEEL),
        ('BACKGROUND', (0, 0), (-1, -1), MID_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_instr)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION A: MULTIPLE CHOICE QUESTIONS (QUESTIONS 1 TO 30)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION A</b>", S['sec_header']))
    story.append(Paragraph("<b>Answer ALL questions. For each question, make a selection by putting a cross in one box [X]. "
                           "If you change your mind, put a line through the box and then mark your new choice with a cross.</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=8, spaceBefore=4))

    mcqs = [
        # Page 2: Q1, Q2, Q3 (Kinetics Topic 11)
        ("In the reaction between propanone and iodine in acidic solution, the reaction is zero order with respect to iodine. What does a concentration-time graph for iodine look like?",
         [("A", "An exponential curve with constant half-life"),
          ("B", "A downward straight line with a constant negative gradient"),
          ("C", "A horizontal line at constant concentration"),
          ("D", "An upward curve showing increasing rate")]),

        ("The rate equation for the alkaline hydrolysis of an ester is: rate = k[ester][OH-]. Which of the following changes will DOUBLE the initial rate?",
         [("A", "Doubling the volume of water used to dissolve the reactants"),
          ("B", "Doubling the concentration of ester while halving the concentration of OH-"),
          ("C", "Doubling the concentration of ester while keeping [OH-] constant"),
          ("D", "Increasing the temperature by 1 °C")]),

        ("In the Arrhenius equation, k = A e^(-Ea/RT), what does the pre-exponential factor A represent physically?",
         [("A", "The fraction of collisions with energy exceeding Ea"),
          ("B", "The frequency of collisions occurring with the correct spatial orientation"),
          ("C", "The enthalpy change of the reaction"),
          ("D", "The molar gas constant per molecule")]),

        # Page 3: Q4, Q5, Q6 (Kinetics Topic 11 & Energetics Topic 12)
        ("A reaction profile shows an intermediate in a potential energy well between two transition states. The first transition state is higher in energy than the second. Which step is the rate-determining step?",
         [("A", "The first step (conversion of reactants to intermediate)"),
          ("B", "The second step (conversion of intermediate to products)"),
          ("C", "Both steps proceed at the same rate"),
          ("D", "Neither step requires activation energy")]),

        ("Which enthalpy change is defined as the enthalpy change when one mole of gaseous ions dissolves in water to form an infinitely dilute solution?",
         [("A", "Standard enthalpy of solution, ΔsolH"),
          ("B", "Standard enthalpy of hydration, ΔhydH"),
          ("C", "Standard lattice enthalpy, ΔLEH"),
          ("D", "Standard enthalpy of atomisation, ΔatH")]),

        ("Why does the standard enthalpy of hydration, ΔhydH, become LESS EXOTHERMIC descending Group 2 from Mg^2+ to Ba^2+?",
         [("A", "The ionic charge increases down the group"),
          ("B", "The ionic radius increases, so charge density decreases and ion-dipole attractions to water weaken"),
          ("C", "The electronegativity of the alkaline earth metals increases"),
          ("D", "Barium ions have more filled electron shells that attract water more strongly")]),

        # Page 4: Q7, Q8, Q9 (Energetics Topic 12)
        ("For which of the following reactions is the entropy change of the surroundings, ΔS_surroundings, NEGATIVE at 298 K?",
         [("A", "Combustion of methane: CH4(g) + 2O2(g) --> CO2(g) + 2H2O(l) (ΔH = -890 kJ mol^-1)"),
          ("B", "Neutralisation: HCl(aq) + NaOH(aq) --> NaCl(aq) + H2O(l) (ΔH = -57 kJ mol^-1)"),
          ("C", "Thermal decomposition of limestone: CaCO3(s) --> CaO(s) + CO2(g) (ΔH = +178 kJ mol^-1)"),
          ("D", "Condensation of steam: H2O(g) --> H2O(l) (ΔH = -44 kJ mol^-1)")]),

        ("The experimental lattice energy of magnesium chloride is -2526 kJ mol^-1, while the theoretical ionic model gives -2326 kJ mol^-1. What accounts for the 200 kJ mol^-1 difference?",
         [("A", "The chloride ion is completely non-polarisable"),
          ("B", "Magnesium has a small, highly charged cation (Mg^2+) that polarises the chloride electron cloud, imparting partial covalent character"),
          ("C", "Magnesium chloride forms a simple molecular lattice"),
          ("D", "The experimental method fails to measure electron affinity accurately")]),

        ("Why does the solubility of Group 2 sulfates DECREASE down the group from MgSO4 to BaSO4?",
         [("A", "Lattice energy decreases much more rapidly than hydration enthalpy"),
          ("B", "Hydration enthalpy of the cation decreases much more rapidly than the lattice energy, making ΔsolH increasingly endothermic"),
          ("C", "Barium sulfate has a much lower melting point than magnesium sulfate"),
          ("D", "Sulfate ions become more polarisable down the group")]),

        # Page 5: Q10, Q11, Q12 (Equilibria Topic 13)
        ("In the Contact Process: 2SO2(g) + O2(g) <=> 2SO3(g) (ΔH = -196 kJ mol^-1), what happens to the equilibrium constant Kp when the total pressure is doubled at constant temperature?",
         [("A", "Kp doubles"),
          ("B", "Kp quadruples"),
          ("C", "Kp remains unchanged"),
          ("D", "Kp is halved")]),

        ("For the heterogeneous decomposition: CaCO3(s) <=> CaO(s) + CO2(g), what is the correct expression for Kp?",
         [("A", "Kp = p(CaO) x p(CO2) / p(CaCO3)"),
          ("B", "Kp = p(CO2)"),
          ("C", "Kp = [CO2]"),
          ("D", "Kp = p(CO2) / p(CaCO3)")]),

        ("Under what thermodynamic conditions is a chemical reaction spontaneous at ALL temperatures?",
         [("A", "ΔH > 0 and ΔS_system > 0"),
          ("B", "ΔH < 0 and ΔS_system > 0"),
          ("C", "ΔH < 0 and ΔS_system < 0"),
          ("D", "ΔH > 0 and ΔS_system < 0")]),

        # Page 6: Q13, Q14, Q15 (Equilibria & Acids Topic 13 & 14)
        ("The relation between the equilibrium constant K and standard Gibbs free energy change is ΔG° = -RT ln K. If a reaction has ΔG° = -40.0 kJ mol^-1 at 298 K, what can be deduced about K?",
         [("A", "K = 1.0"),
          ("B", "K is very small (K << 1)"),
          ("C", "K is very large (K >> 1, reaction essentially goes to completion)"),
          ("D", "K is negative")]),

        ("What is the concentration of hydrogen ions, [H+], in a solution of sulfuric acid, H2SO4, of concentration 0.050 mol dm^-3, assuming complete dissociation of both protons?",
         [("A", "0.025 mol dm^-3"),
          ("B", "0.050 mol dm^-3"),
          ("C", "0.100 mol dm^-3"),
          ("D", "0.200 mol dm^-3")]),

        ("A sample of pure water at 50 °C has pH = 6.63. Which deduction is correct?",
         [("A", "The water is acidic because pH < 7.00"),
          ("B", "The water is neutral because [H+] = [OH-]"),
          ("C", "The dissociation of water into H+ and OH- is exothermic"),
          ("D", "Kw at 50 °C is smaller than Kw at 25 °C")]),

        # Page 7: Q16, Q17, Q18 (Acids & Buffers Topic 14)
        ("What is the pH of a buffer solution prepared by mixing 50 cm^3 of 0.10 mol dm^-3 ethanoic acid (pKa = 4.76) with 50 cm^3 of 0.20 mol dm^-3 sodium ethanoate?",
         [("A", "4.46"),
          ("B", "4.76"),
          ("C", "5.06"),
          ("D", "5.36")]),

        ("In human blood, the pH is maintained between 7.35 and 7.45 primarily by the carbonic acid / hydrogencarbonate buffer system: H2CO3(aq) <=> H+(aq) + HCO3-(aq). How does the body compensate when excess lactic acid enters the bloodstream?",
         [("A", "Lactic acid reacts with H2CO3 to produce CO2"),
          ("B", "Lactic acid reacts with HCO3- ions to form H2CO3, which is then eliminated as CO2 through increased breathing rate"),
          ("C", "The kidneys excrete all hydrogencarbonate ions"),
          ("D", "The pH rises above 7.80 to neutralise the acid")]),

        ("Which indicator is MOST suitable for the titration of 25 cm^3 of 0.10 mol dm^-3 aqueous ammonia (weak base) with 0.10 mol dm^-3 nitric acid (strong acid)?",
         [("A", "Phenolphthalein (pH range 8.3 - 10.0)"),
          ("B", "Thymol blue (pH range 8.0 - 9.6)"),
          ("C", "Methyl orange (pH range 3.1 - 4.4)"),
          ("D", "Alizarin yellow (pH range 10.1 - 12.0)")]),

        # Page 8: Q19, Q20, Q21 (Chirality & Mechanisms Topic 15)
        ("Which of the following molecules has exactly ONE asymmetric (chiral) carbon atom?",
         [("A", "2-chloropropane"),
          ("B", "2-chlorobutane"),
          ("C", "3-chloropentane"),
          ("D", "1-chlorobutane")]),

        ("When (R)-2-bromobutane reacts with aqueous sodium hydroxide via an SN2 mechanism, what is the stereochemical outcome of the butan-2-ol product?",
         [("A", "A 50:50 racemic mixture with zero optical rotation"),
          ("B", "Complete inversion of configuration giving pure (S)-butan-2-ol (Walden inversion)"),
          ("C", "Complete retention of configuration giving pure (R)-butan-2-ol"),
          ("D", "An optically inactive meso compound")]),

        ("Which reagent reacts with both aldehydes and ketones to form a yellow/orange crystalline precipitate that can be purified to determine its melting point?",
         [("A", "Tollens' reagent"),
          ("B", "Fehling's solution"),
          ("C", "2,4-dinitrophenylhydrazine (Brady's reagent)"),
          ("D", "Acidified potassium manganate(VII)")]),

        # Page 9: Q22, Q23, Q24 (Carbonyls & Carboxylic Acids Topic 15)
        ("Which compound gives a POSITIVE tri-iodomethane (iodoform) test forming a yellow precipitate of CHI3?",
         [("A", "Pentan-3-one"),
          ("B", "Pentan-2-one"),
          ("C", "Propan-1-ol"),
          ("D", "Methanoic acid")]),

        ("Which of the following organic compounds has the LOWEST boiling point?",
         [("A", "Butanoic acid, CH3CH2CH2COOH (Mr = 88)"),
          ("B", "Pentan-1-ol, CH3(CH2)4OH (Mr = 88)"),
          ("C", "Ethyl ethanoate, CH3COOCH2CH3 (Mr = 88)"),
          ("D", "Hexane, CH3(CH2)4CH3 (Mr = 86)")]),

        ("What gas is evolved when ethanoic acid is added to solid sodium carbonate, Na2CO3?",
         [("A", "Hydrogen gas, H2"),
          ("B", "Carbon monoxide, CO"),
          ("C", "Carbon dioxide, CO2"),
          ("D", "Methane, CH4")]),

        # Page 10: Q25, Q26, Q27 (Acyl Chlorides & Esters Topic 15)
        ("Why does ethanoyl chloride react with nucleophiles much faster than chloroethane?",
         [("A", "Ethanoyl chloride is a non-polar compound"),
          ("B", "The carbonyl oxygen is strongly electronegative, making the carbonyl carbon much more delta-positive than the carbon in chloroethane"),
          ("C", "The C-Cl bond in ethanoyl chloride is a triple bond"),
          ("D", "Ethanoyl chloride forms intermolecular hydrogen bonds with nucleophiles")]),

        ("What type of polymer is formed by the reaction of benzene-1,4-dicarboxylic acid with ethane-1,2-diol?",
         [("A", "An addition polymer"),
          ("B", "A polyester (condensation polymer)"),
          ("C", "A polyamide"),
          ("D", "A polyalkene")]),

        ("Which catalyst is used in the industrial manufacture of biodiesel by transesterification of vegetable oils with methanol?",
         [("A", "Concentrated hydrochloric acid"),
          ("B", "Sodium hydroxide or potassium hydroxide"),
          ("C", "Vanadium(V) oxide"),
          ("D", "Nickel on alumina")]),

        # Page 11: Q28, Q29, Q30 (Spectroscopy & NMR Topic 15)
        ("How many signals are observed in the broadband-decoupled 13C NMR spectrum of 1,4-dimethylbenzene (p-xylene)?",
         [("A", "2"),
          ("B", "3"),
          ("C", "4"),
          ("D", "6")]),

        ("In the high-resolution 1H NMR spectrum of 1,1-dichloroethane, CH3-CHCl2, what splitting pattern is observed for the -CHCl2 proton?",
         [("A", "Singlet"),
          ("B", "Doublet"),
          ("C", "Triplet"),
          ("D", "Quartet (split by the 3 neighbouring methyl protons)")]),

        ("An organic compound has an [M]+ peak at m/z = 74 and an [M+1]+ peak with relative intensity 3.3% of the molecular ion. How many carbon atoms are present in a molecule of this compound?",
         [("A", "1"),
          ("B", "2"),
          ("C", "3"),
          ("D", "4")])
    ]

    for i, (stem, opts) in enumerate(mcqs, 1):
        qnum = i
        p_q = Paragraph(f"<b>{qnum}</b>&nbsp;&nbsp;{stem.replace(chr(10), '<br/>')}", S['q_stem'])

        q_block = []
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
    # QUESTION 31 (18 MARKS) — KINETICS: PROPANONE IODINATION & ENOLISATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;The iodination of propanone in aqueous acid is represented by the equation:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>CH<sub>3</sub>COCH<sub>3</sub>(aq) + I<sub>2</sub>(aq) + H+(aq) &longrightarrow; CH<sub>3</sub>COCH<sub>2</sub>I(aq) + H+(aq) + I-(aq)</b><br/>"
                           "The progress of the reaction can be monitored continuously by colorimetry, measuring the absorbance of the brown aqueous iodine solution over time.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;When propanone and acid are present in large excess, the absorbance of iodine decreases linearly with time until all iodine is consumed.<br/>"
                           "Sketch a graph of [I<sub>2</sub>] against time on the grid provided, and deduce the order of reaction with respect to iodine.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(width=AVAIL_W, height=5.5*cm, y_label="[I2] / mol dm^-3", x_label="Time / s"))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In a separate series of initial rate experiments, the following data were obtained:", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    kin_table = [
        [Paragraph("<b>Experiment</b>", S['tbl_th']), Paragraph("<b>[CH3COCH3] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>[I2] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>[H+] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>Initial Rate / mol dm^-3 s^-1</b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("0.40", S['tbl_td']), Paragraph("0.020", S['tbl_td']), Paragraph("0.20", S['tbl_td']), Paragraph("5.60 x 10^-6", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("0.80", S['tbl_td']), Paragraph("0.020", S['tbl_td']), Paragraph("0.20", S['tbl_td']), Paragraph("1.12 x 10^-5", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("0.40", S['tbl_td']), Paragraph("0.040", S['tbl_td']), Paragraph("0.20", S['tbl_td']), Paragraph("5.60 x 10^-6", S['tbl_td'])],
        [Paragraph("4", S['tbl_td']), Paragraph("0.40", S['tbl_td']), Paragraph("0.020", S['tbl_td']), Paragraph("0.60", S['tbl_td']), Paragraph("1.68 x 10^-5", S['tbl_td'])],
    ]
    t_kin = Table(kin_table, colWidths=[2.2*cm, 3.8*cm, 3.2*cm, 3.0*cm, AVAIL_W - 12.2*cm])
    t_kin.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_kin)
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("Deduce the rate equation for the reaction, and calculate the rate constant <i>k</i> at 298 K using Experiment 1. Include units for <i>k</i>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: <i>k</i> = ..................................................... Units = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>31 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A proposed three-step mechanism for this reaction is shown below:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 1:</b> &nbsp;&nbsp; CH<sub>3</sub>COCH<sub>3</sub> + H+ &rlhar; CH<sub>3</sub>C(OH+)CH<sub>3</sub> &nbsp;&nbsp;&nbsp;&nbsp; (Fast equilibrium)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 2:</b> &nbsp;&nbsp; CH<sub>3</sub>C(OH+)CH<sub>3</sub> + H<sub>2</sub>O &longrightarrow; CH<sub>2</sub>=C(OH)CH<sub>3</sub> + H<sub>3</sub>O+ &nbsp;&nbsp;&nbsp;&nbsp; (Slow, rate-determining step: acid-catalysed enolisation)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 3:</b> &nbsp;&nbsp; CH<sub>2</sub>=C(OH)CH<sub>3</sub> + I<sub>2</sub> &longrightarrow; CH<sub>3</sub>COCH<sub>2</sub>I + H+ + I- &nbsp;&nbsp;&nbsp;&nbsp; (Fast bromination/iodination of enol)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why this mechanism is entirely consistent with the observed orders of reaction with respect to propanone, H+, and iodine.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;The rate constant <i>k</i> was measured at 298 K (<i>k</i><sub>1</sub> = 7.00 x 10^-5 dm^3 mol^-1 s^-1) and at 318 K (<i>k</i><sub>2</sub> = 4.20 x 10^-4 dm^3 mol^-1 s^-1).<br/>"
                           "Using the Arrhenius relationship ln(<i>k</i><sub>2</sub>/<i>k</i><sub>1</sub>) = (<i>E</i><sub>a</sub>/<i>R</i>)(1/<i>T</i><sub>1</sub> - 1/<i>T</i><sub>2</sub>), calculate the activation energy, <i>E</i><sub>a</sub>, in kJ mol^-1. (<i>R</i> = 8.31 J mol^-1 K^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Activation Energy, <i>E</i><sub>a</sub> = ..................................................... kJ mol^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;State the role of H+ ions in this reaction and explain how its presence lowers the activation energy.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — SOLUTION ENERGETICS & GROUP 2 SULFATES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;The solubility of Group 2 sulfates decreases markedly down the group from magnesium sulfate to barium sulfate.<br/>"
                           "Enthalpy changes can be linked using an energy cycle relating standard lattice energy, Δ<sub>LE</sub><i>H</i>, and standard enthalpies of hydration, Δ<sub>hyd</sub><i>H</i>.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    sol_data = [
        [Paragraph("<b>Ionic Compound / Ion</b>", S['tbl_th']), Paragraph("<b>Lattice Energy, ΔLEH / kJ mol^-1</b>", S['tbl_th']), Paragraph("<b>Enthalpy of Hydration, ΔhydH / kJ mol^-1</b>", S['tbl_th'])],
        [Paragraph("Magnesium ion, Mg^2+", S['tbl_td_l']), Paragraph("-", S['tbl_td']), Paragraph("-1926", S['tbl_td'])],
        [Paragraph("Barium ion, Ba^2+", S['tbl_td_l']), Paragraph("-", S['tbl_td']), Paragraph("-1305", S['tbl_td'])],
        [Paragraph("Sulfate ion, SO4^2-", S['tbl_td_l']), Paragraph("-", S['tbl_td']), Paragraph("-1099", S['tbl_td'])],
        [Paragraph("Magnesium sulfate, MgSO4(s)", S['tbl_td_l']), Paragraph("-2934", S['tbl_td']), Paragraph("-", S['tbl_td'])],
        [Paragraph("Barium sulfate, BaSO4(s)", S['tbl_td_l']), Paragraph("-2378", S['tbl_td']), Paragraph("-", S['tbl_td'])],
    ]
    t_sol = Table(sol_data, colWidths=[6.5*cm, 5.0*cm, AVAIL_W - 11.5*cm])
    t_sol.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_sol)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Draw a fully labelled Hess's law energy cycle connecting the standard enthalpy of solution, Δ<sub>sol</sub><i>H</i>°, of an ionic solid MX(s) with its lattice energy and enthalpies of hydration.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for Hess's law Born-Haber / Solution cycle"))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the standard enthalpy of solution, Δ<sub>sol</sub><i>H</i>°, for magnesium sulfate, MgSO<sub>4</sub>(s), and for barium sulfate, BaSO<sub>4</sub>(s), in kJ mol^-1.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: Δ<sub>sol</sub><i>H</i>°(MgSO<sub>4</sub>) = ................ kJ mol^-1 &nbsp;&nbsp;&nbsp;&nbsp; Δ<sub>sol</sub><i>H</i>°(BaSO<sub>4</sub>) = ................ kJ mol^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>32 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Explain why the solubility of Group 2 sulfates decreases down the group from MgSO<sub>4</sub> to BaSO<sub>4</sub>.<br/>"
                           "In your answer, you should refer to:<br/>"
                           "- The trend in ionic radii and charge densities of the Group 2 cations.<br/>"
                           "- The relative rates at which the lattice energy and hydration enthalpies change.<br/>"
                           "- The sign and magnitude of Δ<sub>sol</sub><i>H</i>° and its influence on total entropy, Δ<i>S</i>_total.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;For the dissolution of barium sulfate at 298 K: BaSO<sub>4</sub>(s) &rlhar; Ba^2+(aq) + SO<sub>4</sub>^2-(aq):<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Δ<i>S</i>°_system = -140.0 J mol^-1 K^-1", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why the change in system entropy, Δ<i>S</i>°_system, is negative when solid barium sulfate dissolves, even though two aqueous ions are produced from one solid formula unit.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using your calculated value of Δ<sub>sol</sub><i>H</i>° for BaSO<sub>4</sub> from (a)(ii), calculate Δ<i>S</i>°_surroundings and Δ<i>S</i>°_total at 298 K, and confirm that BaSO<sub>4</sub> is insoluble.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Δ<i>S</i>°_total = ..................................................... J mol^-1 K^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — CONTACT PROCESS EQUILIBRIA & ACID DISSOCIATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;In Stage 2 of the industrial Contact Process for sulfuric acid, sulfur dioxide is oxidised to sulfur trioxide:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>2SO<sub>2</sub>(g) + O<sub>2</sub>(g) &rlhar; 2SO<sub>3</sub>(g)</b> &nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -196 kJ mol^-1", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;A closed reaction vessel of fixed volume was filled with 2.00 mol of SO<sub>2</sub> and 2.00 mol of O<sub>2</sub>. When equilibrium was reached at 700 K under a constant total pressure of 1.50 atm, 1.60 mol of SO<sub>3</sub> had formed.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the equilibrium amounts (in moles) of SO<sub>2</sub> and O<sub>2</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Moles SO<sub>2</sub> = ..................................... Moles O<sub>2</sub> = .....................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the partial pressure of each gas present at equilibrium.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: p(SO<sub>2</sub>) = ........... atm, p(O<sub>2</sub>) = ........... atm, p(SO<sub>3</sub>) = ........... atm", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Write the expression for the equilibrium constant <i>K</i><sub>p</sub>, and calculate its value at 700 K. State the units of <i>K</i><sub>p</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: <i>K</i><sub>p</sub> = ..................................................... Units = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>33 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In industrial operation, the converter is maintained at 400–450 °C (673–723 K) and 1–2 atm in the presence of a vanadium(V) oxide catalyst, V<sub>2</sub>O<sub>5</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why a relatively low pressure (1–2 atm) is used commercially, even though higher pressure increases the equilibrium yield of SO<sub>3</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using the relation Δ<i>S</i>_total = <i>R</i> ln <i>K</i><sub>p</sub>, calculate the total entropy change, Δ<i>S</i>_total, for the forward reaction at 700 K. (<i>R</i> = 8.31 J mol^-1 K^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Δ<i>S</i>_total = ..................................................... J mol^-1 K^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Sulfuric acid is a strong diprotic acid in aqueous solution. The first proton dissociates completely:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H<sub>2</sub>SO<sub>4</sub>(aq) &longrightarrow; H+(aq) + HSO<sub>4</sub>^-(aq)<br/>"
                           "The hydrogensulfate ion, HSO<sub>4</sub>^-, behaves as a weak acid:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSO<sub>4</sub>^-(aq) &rlhar; H+(aq) + SO<sub>4</sub>^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>a2</sub> = 1.20 x 10^-2 mol dm^-3 at 298 K<br/>"
                           "Calculate the pH of a 0.0500 mol dm^-3 solution of sulfuric acid at 298 K, taking into account the partial dissociation of the second proton.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — CARBONYL CHEMISTRY & CHIRAL INVERSION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Compound <b>J</b>, 2-phenylbutanal (C<sub>6</sub>H<sub>5</sub>CH(CH<sub>2</sub>CH<sub>3</sub>)CHO), is an aromatic aldehyde containing a chiral carbon centre.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Identify the chiral carbon atom in Compound <b>J</b> and draw three-dimensional stereochemical representations of the two enantiomers.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for 3D enantiomer representations of 2-phenylbutanal"))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Compound <b>J</b> is reduced with sodium tetrahydridoborate(III), NaBH<sub>4</sub>, in aqueous ethanol to form alcohol <b>K</b>.<br/>"
                           "State the IUPAC name of alcohol <b>K</b>, and explain why the product <b>K</b> retains optical activity if pure (R)-2-phenylbutanal is used as the starting material.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Compound <b>J</b> reacts with a mixture of KCN and dilute sulfuric acid to form a hydroxynitrile, <b>L</b>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Draw the complete curly-arrow mechanism for the nucleophilic addition of cyanide to the aldehyde group in Compound <b>J</b>.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for nucleophilic addition mechanism: cyanide attack on 2-phenylbutanal"))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>34 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain how many stereoisomers of hydroxynitrile <b>L</b> exist, and explain whether the mixture of stereoisomers obtained from optically pure (R)-2-phenylbutanal would be optically active.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Describe a chemical test to distinguish between 2-phenylbutanal (Compound <b>J</b>) and 1-phenylbutan-2-one (an isomeric ketone).<br/>"
                           "Give the reagents, conditions, and observations for each compound.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — POLYESTERS & RECYCLING (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;<b>Poly(lactic acid) (PLA) and Sustainable Polymer Chemistry:</b><br/>"
                           "Poly(lactic acid) is an aliphatic polyester manufactured from fermented corn starch. It is widely used in 3D printing filaments, biodegradable sutures, and food packaging.<br/>"
                           "Lactic acid (2-hydroxypropanoic acid, CH<sub>3</sub>CH(OH)COOH, <i>M</i><sub>r</sub> = 90.08) polymerises via condensation polymerisation:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<i>n</i> CH<sub>3</sub>CH(OH)COOH &longrightarrow; -[O-CH(CH<sub>3</sub>)-CO]<sub><i>n</i></sub>- + (<i>n</i> - 1) H<sub>2</sub>O", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Draw the displayed formula of two repeat units of poly(lactic acid).", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=4.5*cm, caption="Space for displayed formula of two repeat units of PLA"))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In industrial manufacturing, direct polycondensation of lactic acid produces only low molecular weight oligomers because the reaction is reversible.<br/>"
                           "Explain how the equilibrium can be manipulated to shift the position of equilibrium towards high molecular weight polymer chains.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;A sample of poly(lactic acid) polymer was synthesised in the laboratory. A chemist determines the number-average molar mass (<i>M</i><sub>n</sub>) of the polymer by end-group analysis titration.<br/>"
                           "Each PLA chain has exactly one terminal carboxylic acid group (-COOH).<br/>"
                           "Describe a complete experimental method to determine <i>M</i><sub>n</sub> by titrating a dissolved sample of PLA against standardized 0.0500 mol dm^-3 potassium hydroxide solution, KOH(aq).<br/>"
                           "In your answer, include:<br/>"
                           "- The preparation of the polymer solution using an appropriate dry organic solvent (e.g. propanone or trichloromethane).<br/>"
                           "- The choice of indicator with justification.<br/>"
                           "- The step-by-step titration procedure to obtain concordant titres.<br/>"
                           "- How the average molar mass (<i>M</i><sub>n</sub>) would be calculated from the mass of PLA, titre volume, and stoichiometry.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>*35 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;In a titration experiment, 1.440 g of solid PLA was dissolved and required an average titre of 16.00 cm^3 of 0.0500 mol dm^-3 KOH for complete neutralisation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the amount (in moles) of terminal -COOH groups present in the 1.440 g sample.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Moles of -COOH = ..................................................... mol", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the number-average molar mass (<i>M</i><sub>n</sub>) of the PLA polymer, and determine the average degree of polymerisation, <i>n</i> (molar mass of repeat unit = 72.06 g mol^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: <i>M</i><sub>n</sub> = ......................... g mol^-1 &nbsp;&nbsp;&nbsp;&nbsp; Degree of polymerisation <i>n</i> = .........................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Explain why polyesters such as PLA degrade readily in landfill sites, whereas addition polymers like poly(propene) persist unchanged for centuries.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(35, 18))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION C: SYNOPTIC CONTEMPORARY CASE STUDIES (Q36 & Q37)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION C</b>", S['sec_header']))
    story.append(Paragraph("<b>Answer ALL questions. Write your answers in the spaces provided.</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=12, spaceBefore=4))

    # ──────────────────────────────────────────────────────────
    # QUESTION 36 (15 MARKS) — ATMOSPHERIC CATALYSIS: STRATOSPHERIC OZONE
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Atmospheric Chemistry and Catalytic Ozone Depletion:</b><br/>"
                           "The stratospheric ozone layer filters harmful solar ultraviolet radiation (UV-B, 280–315 nm). Ozone is continually formed and destroyed in the Chapman cycle.<br/>"
                           "Chlorofluorocarbons (CFCs), such as CCl<sub>2</sub>F<sub>2</sub> (CFC-12), release chlorine free radicals (Cl•) under intense UV radiation:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCl<sub>2</sub>F<sub>2</sub> + <i>h</i>ν &longrightarrow; •CClF<sub>2</sub> + Cl•<br/>"
                           "Chlorine radicals act as a homogeneous catalyst for the decomposition of ozone via a two-step radical chain mechanism:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 1:</b> &nbsp;&nbsp; Cl•(g) + O<sub>3</sub>(g) &longrightarrow; ClO•(g) + O<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp; <i>E</i><sub>a1</sub> = +2.1 kJ mol^-1<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 2:</b> &nbsp;&nbsp; ClO•(g) + O(g) &longrightarrow; Cl•(g) + O<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp; <i>E</i><sub>a2</sub> = +0.4 kJ mol^-1<br/>"
                           "Overall reaction: &nbsp;&nbsp; O<sub>3</sub>(g) + O(g) &longrightarrow; 2O<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp; <i>E</i><sub>a,uncatalysed</sub> = +17.1 kJ mol^-1, Δ<i>H</i>° = -392 kJ mol^-1", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Explain why chlorine radicals act as a homogeneous catalyst in this atmospheric system.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Sketch an enthalpy profile diagram comparing the uncatalysed and catalysed pathways on the grid provided, indicating <i>E</i><sub>a,uncatalysed</sub>, <i>E</i><sub>a1</sub>, <i>E</i><sub>a2</sub>, and Δ<i>H</i>°.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for enthalpy profile diagram: catalysed vs uncatalysed ozone destruction"))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>36 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;At a stratospheric temperature of 220 K (-53 °C), calculate the ratio of the rate constant for the catalysed Step 1 to the uncatalysed reaction, using the Arrhenius equation <i>k</i> = <i>A</i> e^(-<i>E</i><sub>a</sub>/<i>RT</i>).<br/>"
                           "Assume the pre-exponential factors <i>A</i> are approximately identical. (<i>R</i> = 8.31 J mol^-1 K^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: Rate Constant Ratio (<i>k</i><sub>cat</sub> / <i>k</i><sub>uncat</sub>) = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Chlorine radicals are eventually deactivated into 'reservoir species' such as chlorine nitrate, ClONO<sub>2</sub>, and hydrogen chloride, HCl.<br/>"
                           "Write a balanced equation for the reaction of a chlorine radical with methane in the stratosphere to form HCl, and explain why this termination step reduces the ozone depletion potential.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Nitrogen monoxide radicals, NO•, emitted by supersonic aircraft engines, also catalyse ozone destruction via a similar cycle.<br/>"
                           "Write the two propagation steps for the catalytic destruction of ozone by NO• radicals.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — MARINE GEOCHEMISTRY & OCEAN ACIDIFICATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Marine Geochemistry and Ocean Acidification:</b><br/>"
                           "The absorption of anthropogenic atmospheric CO<sub>2</sub> by seawater drives a series of coupled chemical equilibria that lower ocean pH and decrease the carbonate ion concentration, [CO<sub>3</sub>^2-]:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Equilibrium 1: &nbsp;&nbsp; CO<sub>2</sub>(g) &rlhar; CO<sub>2</sub>(aq)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Equilibrium 2: &nbsp;&nbsp; CO<sub>2</sub>(aq) + H<sub>2</sub>O(l) &rlhar; H+(aq) + HCO<sub>3</sub>^-(aq) &nbsp;&nbsp;&nbsp;&nbsp; p<i>K</i><sub>a1</sub> = 5.86 at 298 K in seawater<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Equilibrium 3: &nbsp;&nbsp; HCO<sub>3</sub>^-(aq) &rlhar; H+(aq) + CO<sub>3</sub>^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp; p<i>K</i><sub>a2</sub> = 8.92 at 298 K in seawater<br/>"
                           "Marine organisms (corals, molluscs) precipitate calcium carbonate, CaCO<sub>3</sub>, as aragonite:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Equilibrium 4: &nbsp;&nbsp; CaCO<sub>3</sub>(s, aragonite) &rlhar; Ca^2+(aq) + CO<sub>3</sub>^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>sp</sub> = 6.50 x 10^-7 mol^2 dm^-6", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Combine Equilibria 2 and 3 to write an overall ionic equation showing how increasing [H+] from absorbed CO<sub>2</sub> reacts with carbonate ions, CO<sub>3</sub>^2-, in seawater.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using Le Chatelier's principle, explain why ocean acidification lowers the concentration of dissolved carbonate ions, CO<sub>3</sub>^2-.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>37 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In a typical surface seawater sample at 298 K:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;[Ca^2+] = 1.02 x 10^-2 mol dm^-3<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;[HCO<sub>3</sub>^-] = 2.00 x 10^-3 mol dm^-3<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Seawater pH = 8.10", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate [H+] in seawater at pH = 8.10.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("Answer: [H+] = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using Equilibrium 3 and p<i>K</i><sub>a2</sub> = 8.92 (<i>K</i><sub>a2</sub> = 1.20 x 10^-9 mol dm^-3), calculate the concentration of carbonate ions, [CO<sub>3</sub>^2-], in this seawater sample.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: [CO<sub>3</sub>^2-] = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;The saturation state, Ω, for aragonite is defined as: Ω = ([Ca^2+] x [CO<sub>3</sub>^2-]) / <i>K</i><sub>sp</sub>.<br/>"
                           "Calculate Ω for this seawater sample, and explain whether coral reefs will dissolve (Ω < 1) or precipitate (Ω > 1) aragonite under these conditions.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Saturation State, Ω = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;If atmospheric CO<sub>2</sub> causes the ocean surface pH to decline from 8.10 to 7.75 by the year 2100:<br/>"
                           "Calculate the new concentration of [CO<sub>3</sub>^2-] and determine whether the saturation state Ω falls below the critical dissolution threshold of 1.0 (assuming [Ca^2+] and [HCO<sub>3</sub>^-] remain approximately constant).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: New [CO<sub>3</sub>^2-] = ......................... New Ω = .........................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(37, 15))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # PAGE 29: DATA SHEET — PERIODIC TABLE OF ELEMENTS
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>DATA SHEET: THE PERIODIC TABLE OF ELEMENTS & PHYSICAL CONSTANTS</b>", S['sec_header']))
    story.append(Paragraph("<b>Values of fundamental physical constants and relative atomic masses (Ar) for Pearson Edexcel Unit 4 Chemistry</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=8, spaceBefore=4))

    const_rows = [
        [Paragraph("<b>Spectroscopic / Physical Constant</b>", S['tbl_th']), Paragraph("<b>Chemical Shift / Wavenumber Range</b>", S['tbl_th']), Paragraph("<b>Type of Proton / Carbon Environment</b>", S['tbl_th'])],
        [Paragraph("1H NMR: Alkyl C-H", S['tbl_td_l']), Paragraph("0.7 - 1.2 ppm", S['tbl_td']), Paragraph("R-CH3", S['tbl_td'])],
        [Paragraph("1H NMR: Adjacent to C=O", S['tbl_td_l']), Paragraph("2.0 - 2.8 ppm", S['tbl_td']), Paragraph("R-CO-CH2- / R-CO-CH3", S['tbl_td'])],
        [Paragraph("1H NMR: Ester -O-CH2- / -O-CH3", S['tbl_td_l']), Paragraph("3.7 - 4.2 ppm", S['tbl_td']), Paragraph("R-COO-CH2-R / R-COO-CH3", S['tbl_td'])],
        [Paragraph("1H NMR: Aromatic C-H", S['tbl_td_l']), Paragraph("6.5 - 8.5 ppm", S['tbl_td']), Paragraph("C6H5- / Ar-H", S['tbl_td'])],
        [Paragraph("1H NMR: Carboxylic Acid O-H", S['tbl_td_l']), Paragraph("10.0 - 12.5 ppm", S['tbl_td']), Paragraph("R-COOH (broad singlet, D2O exchange)", S['tbl_td'])],
        [Paragraph("13C NMR: Alkyl C-C", S['tbl_td_l']), Paragraph("0 - 50 ppm", S['tbl_td']), Paragraph("Alkyl carbons (sp3)", S['tbl_td'])],
        [Paragraph("13C NMR: C-O Ether / Ester / Alcohol", S['tbl_td_l']), Paragraph("50 - 90 ppm", S['tbl_td']), Paragraph("Carbons bonded to oxygen", S['tbl_td'])],
        [Paragraph("13C NMR: Aromatic Ring Carbons", S['tbl_td_l']), Paragraph("110 - 145 ppm", S['tbl_td']), Paragraph("Benzene ring carbons (sp2)", S['tbl_td'])],
        [Paragraph("13C NMR: C=O Ester / Acid", S['tbl_td_l']), Paragraph("160 - 185 ppm", S['tbl_td']), Paragraph("Carbonyl carbon in R-COOR / R-COOH", S['tbl_td'])],
    ]
    t_const = Table(const_rows, colWidths=[5.5*cm, 5.5*cm, AVAIL_W - 11.0*cm])
    t_const.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_const)
    story.append(Spacer(1, 0.4 * cm))

    story.append(Paragraph("<b>Periodic Table of the Elements</b>", S['q_num']))
    story.append(Spacer(1, 0.15 * cm))

    pt_rows = [
        [Paragraph("<b>Group</b>", S['tbl_th']), Paragraph("<b>1</b>", S['tbl_th']), Paragraph("<b>2</b>", S['tbl_th']), Paragraph("<b>3</b>", S['tbl_th']), Paragraph("<b>4</b>", S['tbl_th']), Paragraph("<b>5</b>", S['tbl_th']), Paragraph("<b>6</b>", S['tbl_th']), Paragraph("<b>7</b>", S['tbl_th']), Paragraph("<b>0 / 8</b>", S['tbl_th'])],
        [Paragraph("<b>Period 1</b>", S['tbl_td']), Paragraph("H<br/>1.0", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("", S['tbl_td']), Paragraph("He<br/>4.0", S['tbl_td'])],
        [Paragraph("<b>Period 2</b>", S['tbl_td']), Paragraph("Li<br/>6.9", S['tbl_td']), Paragraph("Be<br/>9.0", S['tbl_td']), Paragraph("B<br/>10.8", S['tbl_td']), Paragraph("C<br/>12.0", S['tbl_td']), Paragraph("N<br/>14.0", S['tbl_td']), Paragraph("O<br/>16.0", S['tbl_td']), Paragraph("F<br/>19.0", S['tbl_td']), Paragraph("Ne<br/>20.2", S['tbl_td'])],
        [Paragraph("<b>Period 3</b>", S['tbl_td']), Paragraph("Na<br/>23.0", S['tbl_td']), Paragraph("Mg<br/>24.3", S['tbl_td']), Paragraph("Al<br/>27.0", S['tbl_td']), Paragraph("Si<br/>28.1", S['tbl_td']), Paragraph("P<br/>31.0", S['tbl_td']), Paragraph("S<br/>32.1", S['tbl_td']), Paragraph("Cl<br/>35.5", S['tbl_td']), Paragraph("Ar<br/>39.9", S['tbl_td'])],
        [Paragraph("<b>Period 4</b>", S['tbl_td']), Paragraph("K<br/>39.1", S['tbl_td']), Paragraph("Ca<br/>40.1", S['tbl_td']), Paragraph("Ga<br/>69.7", S['tbl_td']), Paragraph("Ge<br/>72.6", S['tbl_td']), Paragraph("As<br/>74.9", S['tbl_td']), Paragraph("Se<br/>79.0", S['tbl_td']), Paragraph("Br<br/>79.9", S['tbl_td']), Paragraph("Kr<br/>83.8", S['tbl_td'])],
        [Paragraph("<b>Period 5</b>", S['tbl_td']), Paragraph("Rb<br/>85.5", S['tbl_td']), Paragraph("Sr<br/>87.6", S['tbl_td']), Paragraph("In<br/>114.8", S['tbl_td']), Paragraph("Sn<br/>118.7", S['tbl_td']), Paragraph("Sb<br/>121.8", S['tbl_td']), Paragraph("Te<br/>127.6", S['tbl_td']), Paragraph("I<br/>126.9", S['tbl_td']), Paragraph("Xe<br/>131.3", S['tbl_td'])],
        [Paragraph("<b>Period 6</b>", S['tbl_td']), Paragraph("Cs<br/>132.9", S['tbl_td']), Paragraph("Ba<br/>137.3", S['tbl_td']), Paragraph("Tl<br/>204.4", S['tbl_td']), Paragraph("Pb<br/>207.2", S['tbl_td']), Paragraph("Bi<br/>209.0", S['tbl_td']), Paragraph("Po<br/>[209]", S['tbl_td']), Paragraph("At<br/>[210]", S['tbl_td']), Paragraph("Rn<br/>[222]", S['tbl_td'])],
    ]
    t_pt = Table(pt_rows, colWidths=[2.2*cm] + [1.87*cm]*8)
    t_pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_pt)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # MARK SCHEME & EXAMINER TRAP COMMENTARY
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>CONFIDENTIAL TEACHER MARK SCHEME & EXAMINER TRAP COMMENTARY</b>", S['sec_header']))
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 14 Synoptic Mock 2 (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Zero-order reactions feature a constant rate of reaction, producing a straight line of constant negative gradient on a concentration-time graph.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Rate is first order in ester and first order in OH-. Doubling [ester] at constant [OH-] doubles the rate.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("A is the frequency factor, representing the frequency of collisions with correct orientation.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("The step passing over the highest transition state barrier represents the slowest rate-determining step.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Enthalpy of hydration is the energy released when one mole of gaseous ions forms hydrated ions in water.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Descending Group 2, ionic radius increases at constant 2+ charge; lower charge density weakens ion-dipole attractions.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("ΔS_surroundings = -ΔH / T. For endothermic reactions (ΔH > 0), ΔS_surroundings is negative.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Mg^2+ has high charge density, polarising chloride ions and introducing covalent bonding character.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Hydration enthalpy falls much faster than lattice energy due to the large, constant size of the sulfate ion.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Pressure changes shift equilibrium position, but Kp is temperature-dependent only; Kp remains constant.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Solids have unit activity and are omitted from Kp expressions: Kp = p(CO2).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Exothermic (ΔH < 0) and disorder-increasing (ΔS_sys > 0) reactions have ΔS_total > 0 at all temperatures.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("A large negative ΔG° corresponds to a very large positive ln K, so K >> 1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Complete dissociation of dibasic H2SO4 yields [H+] = 2 x 0.050 = 0.100 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Pure water remains neutral at all temperatures because dissociation produces equal amounts of H+ and OH-.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("pH = pKa + log([A-] / [HA]) = 4.76 + log(0.20 / 0.10) = 4.76 + 0.301 = 5.06.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Excess H+ ions react with HCO3- buffer conjugate base, forming H2CO3, which is vented as CO2 via hyperventilation.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Strong acid - weak base titrations produce an acidic equivalence point (pH ~4–5), matching methyl orange.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carbon-2 in 2-chlorobutane is bonded to -H, -CH3, -Cl, and -CH2CH3 (four distinct groups).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("SN2 backside attack causes complete stereochemical inversion (Walden inversion) of configuration.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("2,4-DNPH reacts with carbonyl groups in both aldehydes and ketones to give orange 2,4-dinitrophenylhydrazones.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Pentan-2-one possesses a methyl carbonyl group (CH3-CO-), yielding a yellow precipitate of tri-iodomethane.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Hexane is completely non-polar with only weak London dispersion forces; all others have polar or hydrogen-bonding groups.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Carboxylic acids react with carbonates to evolve carbon dioxide gas with effervescence: 2RCOOH + CO3^2- --> 2RCOO- + CO2 + H2O.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carbonyl oxygen withdraws electron density, generating a strongly electrophilic carbonyl carbon attractive to nucleophiles.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Condensation of dicarboxylic acid with diol eliminates water, forming a polyester backbone.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Transesterification is catalysed by alkaline metal hydroxides (NaOH/KOH) or sodium methoxide.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("p-Xylene possesses high symmetry with only 3 carbon environments: methyl, ipso-ring, and ortho-ring carbons.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("By the n + 1 rule, the 3 adjacent protons of the methyl group split the -CHCl2 proton into 3 + 1 = 4 peaks (quartet).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Number of carbons = (100 / 1.1) x (3.3 / 100) = 3.3 / 1.1 = 3 carbons.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
    ]
    t_ms_a = Table(ms_a, colWidths=[1.0*cm, 1.8*cm, 13.0*cm, 1.4*cm])
    t_ms_a.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_ms_a)
    story.append(Spacer(1, 0.4 * cm))

    # Structured Mark Schemes
    ms_struct = [
        ("Question 31: Kinetics: Propanone Iodination & Enolisation (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Sketch: Straight line starting on y-axis with constant negative slope down to zero on x-axis [1]<br/>"
         "• Gradient is constant throughout [1]<br/>"
         "• Order with respect to iodine = 0 (zero order) [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Comparing Exp 1 and Exp 2: [CH3COCH3] doubles, rate doubles => Order in propanone = 1 [1]<br/>"
         "• Comparing Exp 1 and Exp 4: [H+] triples, rate triples => Order in H+ = 1 [1]<br/>"
         "• Rate equation: rate = k[CH3COCH3][H+] [1]<br/>"
         "• k = 5.60 x 10^-6 / (0.40 x 0.20) = 7.00 x 10^-5 dm^3 mol^-1 s^-1 (with correct units) [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• The slow rate-determining step (Step 2) involves the protonated propanone intermediate [1]<br/>"
         "• Protonated propanone is formed in pre-equilibrium Step 1 from CH3COCH3 and H+, so rate depends directly on [CH3COCH3] and [H+] (first order in each) [1]<br/>"
         "• Iodine only enters the mechanism in Step 3, which is fast and occurs AFTER the rate-determining step [1]<br/>"
         "• Therefore, the concentration of iodine has zero effect on the overall rate (zero order in I2) [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• k2 / k1 = (4.20 x 10^-4) / (7.00 x 10^-5) = 6.00 => ln(6.00) = 1.7918 [1]<br/>"
         "• 1/T1 - 1/T2 = (1 / 298) - (1 / 318) = 3.3557 x 10^-3 - 3.1447 x 10^-3 = 2.110 x 10^-4 K^-1 [1]<br/>"
         "• Ea / R = 1.7918 / (2.110 x 10^-4) = 8492 K [1]<br/>"
         "• Ea = 8492 x 8.31 = 70568 J mol^-1 [1]<br/>"
         "• Ea = +70.6 kJ mol^-1 (allow 70.5 to 70.7 kJ mol^-1) [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• H+ acts as a homogeneous acid catalyst [1]<br/>"
         "• It protonates the carbonyl oxygen, increasing the polarization of the C-H bonds and providing an alternative pathway with a lower activation energy [1]."),

        ("Question 32: Solution Energetics & Group 2 Sulfates (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Cycle correctly drawn: MX(s) at top-left, gaseous ions M^2+(g) + X^2-(g) at top-right, aqueous ions M^2+(aq) + X^2-(aq) at bottom [1]<br/>"
         "• Arrows correctly directed: MX(s) -> M^2+(g) + X^2-(g) labelled -ΔLEH (or LE dissociation); gaseous ions -> aqueous ions labelled ΔhydH(cation) + ΔhydH(anion) [1]<br/>"
         "• MX(s) -> aqueous ions labelled ΔsolH° [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Relationship: ΔsolH° = -ΔLEH + ΔhydH(cation) + ΔhydH(anion) [1]<br/>"
         "• MgSO4: ΔsolH° = -(-2934) + (-1926) + (-1099) = 2934 - 3025 = -91 kJ mol^-1 (exothermic) [1]<br/>"
         "• BaSO4: ΔsolH° = -(-2378) + (-1305) + (-1099) = 2378 - 2404 = -26 kJ mol^-1 (slightly exothermic / endothermic in theoretical cycles) [2].<br/><br/>"
         "<b>(b) [6 Marks]</b><br/>"
         "• Down Group 2, ionic radius increases (Mg^2+ < Ca^2+ < Sr^2+ < Ba^2+) at constant 2+ charge, so cation charge density decreases significantly [1]<br/>"
         "• Hydration enthalpy of the cation becomes substantially less exothermic down the group because electrostatic attraction to water dipoles weakens [1]<br/>"
         "• The sulfate anion (SO4^2-) is very large compared to the cations, so the percentage change in interionic distance (r+ + r-) in the crystal lattice is small [1]<br/>"
         "• As a result, lattice energy decreases only slightly down the group [1]<br/>"
         "• Because cation hydration enthalpy decreases much more rapidly than the lattice energy, ΔsolH° becomes less exothermic / more endothermic [1]<br/>"
         "• This causes ΔS_surroundings (-ΔsolH/T) and ΔS_total to become increasingly negative, rendering dissolution non-feasible and making BaSO4 insoluble [1].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• The small, highly charged Ba^2+ and SO4^2- ions attract water molecules strongly by ion-dipole interactions [1]<br/>"
         "• This tightly orders/orients multiple shells of water molecules around each ion, causing a net decrease in the disorder (microstates) of the solvent [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• ΔS_surroundings = -ΔsolH / T = -(-26000) / 298 = +87.2 J mol^-1 K^-1 (or using literature ΔsolH = +19 kJ/mol => -63.8 J/K/mol) [1]<br/>"
         "• ΔS_total = ΔS_system + ΔS_surroundings = -140.0 + 87.2 = -52.8 J mol^-1 K^-1 [1]<br/>"
         "• Since ΔS_total is negative, the dissolution is thermodynamically non-feasible, confirming BaSO4 is insoluble [1]."),

        ("Question 33: Contact Process Equilibria & Acid Dissociation (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• ICE table: 2SO2 + O2 <=> 2SO3<br/>"
         "• Moles SO3 at equilibrium = 1.60 mol<br/>"
         "• Equilibrium moles SO2 = 2.00 - 1.60 = 0.40 mol [1]<br/>"
         "• Equilibrium moles O2 = 2.00 - 0.5(1.60) = 1.20 mol [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Total equilibrium moles = 0.40 + 1.20 + 1.60 = 3.20 mol [1]<br/>"
         "• p(SO2) = (0.40 / 3.20) x 1.50 = 0.1875 atm ≈ 0.188 atm [1]<br/>"
         "• p(O2) = (1.20 / 3.20) x 1.50 = 0.5625 atm ≈ 0.563 atm [1]<br/>"
         "• p(SO3) = (1.60 / 3.20) x 1.50 = 0.750 atm [1].<br/><br/>"
         "<b>(a)(iii) [4 Marks]</b><br/>"
         "• Kp expression: Kp = p(SO3)^2 / (p(SO2)^2 x p(O2)) [1]<br/>"
         "• Kp = (0.750)^2 / ((0.1875)^2 x 0.5625) = 0.5625 / (0.035156 x 0.5625) = 1 / 0.035156 [1]<br/>"
         "• Kp = 28.4 (allow 28.3 to 28.5) [1]<br/>"
         "• Units: atm^2 / (atm^2 x atm) = atm^-1 [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• Even at 1–2 atm, the equilibrium conversion of SO2 to SO3 exceeds 98% [1]<br/>"
         "• Operating at higher pressures is economically unwarranted due to high capital expenditure for thick-walled pipes and safety hazards [1].<br/><br/>"
         "<b>(b)(ii) [2 Marks]</b><br/>"
         "• ΔS_total = R ln Kp = 8.314 x ln(28.44) = 8.314 x 3.348 [1]<br/>"
         "• = +27.8 J mol^-1 K^-1 [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Stage 1 complete: [H+]1 = 0.0500 mol dm^-3, [HSO4-] = 0.0500 mol dm^-3 [1]<br/>"
         "• Stage 2: HSO4- <=> H+ + SO4^2-. Let x = additional [H+]: Ka2 = (0.0500 + x)(x) / (0.0500 - x) = 0.0120 [1]<br/>"
         "• Solving quadratic: x^2 + 0.0620 x - 0.000600 = 0 => x = 0.00845 mol dm^-3 [1]<br/>"
         "• Total [H+] = 0.0500 + 0.00845 = 0.05845 mol dm^-3 => pH = -log(0.05845) = 1.23 [1]."),

        ("Question 34: Carbonyl Chemistry & Chiral Inversion (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Chiral centre identified: C2 bonded to -H, -C6H5, -CH2CH3, and -CHO [1]<br/>"
         "• Two 3D tetrahedral structures drawn with wedges and dashes [1]<br/>"
         "• Structures are non-superimposable mirror images [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• IUPAC name: 2-phenylbutan-1-ol [1]<br/>"
         "• The reduction with NaBH4 converts the achiral -CHO group into -CH2OH [1]<br/>"
         "• None of the four bonds to the chiral carbon C2 are broken during the reaction, so the stereochemical configuration at C2 is fully preserved, maintaining optical rotation [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• Dipoles on C=O (Cδ+, Oδ-) and lone pair on carbon of :CN- [1]<br/>"
         "• Curly arrow from lone pair on carbon of :CN- to carbonyl carbon [1]<br/>"
         "• Curly arrow from C=O double bond to oxygen forming tetrahedral alkoxide intermediate [1]<br/>"
         "• Curly arrow from lone pair on O- to H+ (or H-CN) forming -OH group [1].<br/><br/>"
         "<b>(b)(ii) [4 Marks]</b><br/>"
         "• The product has 2 chiral carbons: C2 (existing chiral centre) and C1 (newly formed chiral centre) [1]<br/>"
         "• 2^2 = 4 possible stereoisomers (two pairs of diastereomers) [1]<br/>"
         "• Attack at the planar carbonyl carbon C1 occurs from both faces with approximately equal probability, creating a 50:50 mixture of (R,R) and (R,S) diastereomers [1]<br/>"
         "• Because the starting material was pure (R)-2-phenylbutanal, the existing C2 centre remains strictly (R); diastereomers have non-cancelling optical rotations, so the product mixture REMAINS OPTICALLY ACTIVE [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Reagent: Tollens' reagent (ammoniacal silver nitrate) OR Fehling's solution [1]<br/>"
         "• Conditions: Warm gently in a water bath [1]<br/>"
         "• Observation with 2-phenylbutanal (aldehyde): Silver mirror formed (or brick-red precipitate with Fehling's) [1]<br/>"
         "• Observation with 1-phenylbutan-2-one (ketone): Remains colourless (no reaction) [1]."),

        ("Question 35: Polyesters & Recycling (* Level of Response) (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Structure of two repeat units: -[O-CH(CH3)-CO-O-CH(CH3)-CO]- with open extension bonds [2].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• Continuous removal of water byproduct (e.g. by applying high vacuum or using Dean-Stark apparatus) [1]<br/>"
         "• By Le Chatelier's principle, removing a product drives the position of equilibrium towards higher polymerisation [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive, well-structured analytical procedure. Sample preparation: accurately weigh ~1.0–1.5 g of dry PLA using a 4-decimal balance into a conical flask; dissolve in ~25 cm^3 of dry, neutralised propanone or chloroform. Indicator: add 3–4 drops of phenolphthalein indicator; justified because titrating a weak carboxylic acid end-group with a strong base (KOH) gives an equivalence point at pH ~8.5–9.0. Titration: fill burette with standardized 0.0500 mol dm^-3 KOH; titrate slowly with swirling to the first permanent pale pink colour persisting for 30 seconds; repeat to achieve concordant titres within 0.10 cm^3. Calculation: moles KOH = C x V = moles of terminal -COOH = moles of PLA polymer chains; number-average molar mass Mn = mass of PLA sample / moles of -COOH. Purity / blank correction: run a solvent blank titration without polymer.<br/>"
         "• Level 2 (3-4 marks): Clear plan outlining dissolution, phenolphthalein titration, and formula for Mn, but missing blank titration or detailed indicator justification.<br/>"
         "• Level 1 (1-2 marks): Partial description with incomplete calculation or inappropriate indicator choice.<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• Moles KOH = (16.00 / 1000) x 0.0500 = 8.00 x 10^-4 mol [1]<br/>"
         "• 1:1 stoichiometry => Moles of -COOH = 8.00 x 10^-4 mol [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• Mn = mass / moles = 1.440 g / (8.00 x 10^-4 mol) = 1800 g mol^-1 [2]<br/>"
         "• Average degree of polymerisation n = 1800 / 72.06 = 25.0 ≈ 25 repeat units [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• PLA contains polar ester linkages (-COO-) in its polymer backbone [1]<br/>"
         "• The carbonyl carbon is susceptible to nucleophilic attack by water (hydrolysis) and microbial esterase enzymes [1]<br/>"
         "• In contrast, poly(propene) has an entirely non-polar, unreactive C-C saturated alkane backbone with high bond enthalpies, completely resisting enzymatic and hydrolytic degradation [1]."),

        ("Question 36: Atmospheric Catalysis: Stratospheric Ozone (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• A catalyst that is in the same physical phase (gas phase) as the reacting ozone and oxygen species [1]<br/>"
         "• Cl• participates in Step 1 and is regenerated unchanged at the end of Step 2 [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Profile shows reactants O3 + O at high energy, products 2O2 at much lower energy (exothermic, ΔH° = -392 kJ mol^-1) [1]<br/>"
         "• Uncatalysed single high energy barrier labelled Ea,uncatalysed (+17.1 kJ mol^-1) [1]<br/>"
         "• Catalysed double-humped pathway with an intermediate dip (ClO• + O2) [1]<br/>"
         "• Both catalysed activation energies Ea1 (+2.1) and Ea2 (+0.4) clearly lower than uncatalysed barrier [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• k_cat / k_uncat = e^(-Ea1/RT) / e^(-Ea,uncat/RT) = e^((Ea,uncat - Ea1) / RT) [1]<br/>"
         "• ΔEa = 17100 - 2100 = 15000 J mol^-1 [1]<br/>"
         "• Exponent = 15000 / (8.314 x 220) = 15000 / 1829.08 = 8.201 [1]<br/>"
         "• Ratio = e^(8.201) = 3644 ≈ 3.6 x 10^3 (catalysed reaction is ~3600 times faster!) [1].<br/><br/>"
         "<b>(c) [2 Marks]</b><br/>"
         "• Cl• + CH4 --> •CH3 + HCl [1]<br/>"
         "• HCl is a stable reservoir species that does not react with ozone, temporarily removing active chlorine radicals from the catalytic cycle [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Step 1: NO• + O3 --> NO2• + O2 [1]<br/>"
         "• Step 2: NO2• + O --> NO• + O2 [1]<br/>"
         "• Overall: O3 + O --> 2O2 (with NO• regenerated) [1]."),

        ("Question 37: Marine Geochemistry & Ocean Acidification (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• CO2(aq) + H2O(l) + CO3^2-(aq) <=> 2HCO3-(aq) (or H+ + CO3^2- <=> HCO3-) [2].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• Increasing atmospheric CO2 increases [H+] in surface waters [1]<br/>"
         "• By Le Chatelier's principle, added H+ reacts with CO3^2- to form HCO3-, shifting the equilibrium and driving down [CO3^2-] [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• [H+] = 10^-pH = 10^-8.10 = 7.94 x 10^-9 mol dm^-3 [2].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Ka2 = [H+][CO3^2-] / [HCO3-] => [CO3^2-] = Ka2 x [HCO3-] / [H+] [1]<br/>"
         "• [CO3^2-] = (1.20 x 10^-9 x 2.00 x 10^-3) / (7.94 x 10^-9) [1]<br/>"
         "• [CO3^2-] = 3.02 x 10^-4 mol dm^-3 [1].<br/><br/>"
         "<b>(b)(iii) [3 Marks]</b><br/>"
         "• Ion product = [Ca^2+][CO3^2-] = (1.02 x 10^-2) x (3.02 x 10^-4) = 3.08 x 10^-6 mol^2 dm^-6 [1]<br/>"
         "• Ω = (3.08 x 10^-6) / (6.50 x 10^-7) = 4.74 [1]<br/>"
         "• Since Ω > 1, seawater is supersaturated with respect to aragonite; corals can precipitate calcium carbonate [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• At pH = 7.75: [H+] = 10^-7.75 = 1.778 x 10^-8 mol dm^-3 [1]<br/>"
         "• New [CO3^2-] = (1.20 x 10^-9 x 2.00 x 10^-3) / (1.778 x 10^-8) = 1.35 x 10^-4 mol dm^-3 [1]<br/>"
         "• New Ω = ((1.02 x 10^-2) x (1.35 x 10^-4)) / (6.50 x 10^-7) = (1.38 x 10^-6) / (6.50 x 10^-7) = 2.12 (declines severely by >55%, stressing reef calcifiers though remains above 1.0) [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 14 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
'''

with open('build_usman_week14_quiz.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated build_usman_week14_quiz.py successfully.")
