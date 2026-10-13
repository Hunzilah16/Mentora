# -*- coding: utf-8 -*-
"""
build_full_week13_script.py
Generates the complete build_usman_week13_quiz.py script for Week 13 150M Mock Paper 1.
"""

import sys

content = r'''"""
build_usman_week13_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 13 ADVANCED SYNOPTIC TIMED MOCK EXAMINATION 1 (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Examination Time: 2 hours 30 minutes
Paper Reference: WCH14/01 (Mock 1)
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
    "Usman_Edexcel_Chem_U4_Week13_150M_Challenging_Quiz.pdf"
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
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="ln k", x_label="1 / T  /  10^-3 K^-1"):
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 13 Synoptic Mock 1")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 13 (150 Marks)...")
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
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W13</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 13: ADVANCED SYNOPTIC TIMED MOCK EXAMINATION PAPER 1 (150 MARKS)</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Full Unit 4 Synoptic Timed Mock 1)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Syllabus Scope:</b>", S['edx_meta']), Paragraph("Topic 11: Kinetics (Rate Equations, Arrhenius, Mechanisms)<br/>Topic 12: Entropy & Energetics (Total Entropy, Born-Haber, Lattice)<br/>Topic 13: Chemical Equilibria (Kc, Kp, Thermodynamic Links)<br/>Topic 14: Acid-Base Equilibria (pH, Kw, Ka, Buffers, Titration Curves)<br/>Topic 15: Organic Chemistry (Carbonyls, Carboxylic Derivatives, Chirality, Spectroscopy)", S['edx_meta'])],
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
        ("A reaction has the rate equation: rate = k[A]^2[B]. What are the units of the rate constant k?",
         [("A", "mol dm^-3 s^-1"),
          ("B", "dm^3 mol^-1 s^-1"),
          ("C", "dm^6 mol^-2 s^-1"),
          ("D", "s^-1")]),

        ("The decomposition of compound X is first order with a half-life of 240 s. What fraction of X remains unreacted after 720 s?",
         [("A", "1/3"),
          ("B", "1/4"),
          ("C", "1/8"),
          ("D", "1/16")]),

        ("In an Arrhenius plot of ln k against 1/T, the gradient of the line is -9.62 x 10^3 K. What is the activation energy, Ea, of the reaction? (R = 8.31 J mol^-1 K^-1)",
         [("A", "+79.9 kJ mol^-1"),
          ("B", "+1.16 kJ mol^-1"),
          ("C", "+80.0 J mol^-1"),
          ("D", "+7.99 x 10^4 kJ mol^-1")]),

        # Page 3: Q4, Q5, Q6 (Kinetics Topic 11 & Entropy Topic 12)
        ("For the reaction A + 2B --> C, the rate equation is rate = k[A]. Which statement about the mechanism is correct?",
         [("A", "The reaction occurs in a single termolecular collision"),
          ("B", "The rate-determining step involves one molecule of A and zero molecules of B"),
          ("C", "B acts as a catalyst in the reaction"),
          ("D", "The overall order of the reaction is 3")]),

        ("Which of the following processes has a POSITIVE change in system entropy, ΔS_system > 0?",
         [("A", "N2(g) + 3H2(g) --> 2NH3(g)"),
          ("B", "H2O(g) --> H2O(l)"),
          ("C", "CaCO3(s) --> CaO(s) + CO2(g)"),
          ("D", "Ag+(aq) + Cl-(aq) --> AgCl(s)")]),

        ("The standard molar entropies at 298 K are: S°[C(graphite)] = 5.7, S°[O2(g)] = 205.0, S°[CO2(g)] = 213.6 J mol^-1 K^-1.<br/>What is ΔS°_system for the combustion: C(graphite) + O2(g) --> CO2(g)?",
         [("A", "+2.9 J mol^-1 K^-1"),
          ("B", "-2.9 J mol^-1 K^-1"),
          ("C", "+424.3 J mol^-1 K^-1"),
          ("D", "-424.3 J mol^-1 K^-1")]),

        # Page 4: Q7, Q8, Q9 (Entropy & Energetics Topic 12)
        ("A reaction has ΔH = +85.0 kJ mol^-1 and ΔS_system = +170.0 J mol^-1 K^-1. At what temperature does the reaction become feasible (ΔS_total > 0)?",
         [("A", "Above 0.50 K"),
          ("B", "Above 500 K"),
          ("C", "Below 500 K"),
          ("D", "At all temperatures")]),

        ("Which ionic compound has the MOST EXOTHERMIC experimental lattice energy?",
         [("A", "Sodium chloride, NaCl"),
          ("B", "Magnesium chloride, MgCl2"),
          ("C", "Magnesium oxide, MgO"),
          ("D", "Calcium oxide, CaO")]),

        ("The experimental lattice energy of silver iodide, AgI, is significantly more exothermic than the theoretical value calculated using the ionic model. What is the explanation for this discrepancy?",
         [("A", "Silver ions are larger than sodium ions"),
          ("B", "The Ag+ cation polarises the large, polarisable iodide ion, introducing substantial covalent character"),
          ("C", "AgI is a giant covalent network substance like diamond"),
          ("D", "The theoretical model ignores electron affinity")]),

        # Page 5: Q10, Q11, Q12 (Equilibria Topic 13)
        ("For the equilibrium: N2(g) + 3H2(g) <=> 2NH3(g) (ΔH = -92 kJ mol^-1), what is the effect of increasing the temperature at constant pressure?",
         [("A", "Kp increases and the yield of NH3 increases"),
          ("B", "Kp decreases and the yield of NH3 decreases"),
          ("C", "Kp remains constant and the yield of NH3 increases"),
          ("D", "Kp increases but the yield of NH3 decreases")]),

        ("At 500 K, a reaction has Kp = 1.0 x 10^-4 atm^-1. What is the total entropy change, ΔS_total, at this temperature? (R = 8.31 J mol^-1 K^-1)",
         [("A", "-76.5 J mol^-1 K^-1"),
          ("B", "+76.5 J mol^-1 K^-1"),
          ("C", "-38.3 J mol^-1 K^-1"),
          ("D", "0 J mol^-1 K^-1")]),

        ("A mixture containing 0.20 mol of PCl5, 0.40 mol of PCl3, and 0.40 mol of Cl2 is at equilibrium in a vessel at total pressure 2.0 atm. What is the partial pressure of PCl5?",
         [("A", "0.20 atm"),
          ("B", "0.40 atm"),
          ("C", "0.80 atm"),
          ("D", "1.00 atm")]),

        # Page 6: Q13, Q14, Q15 (Equilibria & Acids Topic 13 & 14)
        ("Which factor WILL change the numerical value of the equilibrium constant Kc for a liquid-phase reaction?",
         [("A", "Adding a homogeneous acid catalyst"),
          ("B", "Doubling the concentration of all reactants"),
          ("C", "Changing the reaction temperature"),
          ("D", "Changing the total volume of the solvent")]),

        ("What is the pH of a 0.025 mol dm^-3 aqueous solution of barium hydroxide, Ba(OH)2, at 298 K? (Kw = 1.0 x 10^-14 mol^2 dm^-6)",
         [("A", "1.30"),
          ("B", "1.60"),
          ("C", "12.40"),
          ("D", "12.70")]),

        ("At 373 K (100 °C), pure water has Kw = 5.13 x 10^-13 mol^2 dm^-6. Which statement is correct for pure water at 373 K?",
         [("A", "The water is acidic because pH < 7.00"),
          ("B", "The water is alkaline because [OH-] > [H+]"),
          ("C", "The water is neutral with pH ≈ 6.14"),
          ("D", "The dissociation of water is exothermic")]),

        # Page 7: Q16, Q17, Q18 (Acids & Buffers Topic 14)
        ("A weak acid HA has pKa = 4.80. What is the pH of a 0.20 mol dm^-3 solution of HA at 298 K?",
         [("A", "2.40"),
          ("B", "2.75"),
          ("C", "4.80"),
          ("D", "5.50")]),

        ("Which mixture forms an effective buffer solution when mixed in equal volumes?",
         [("A", "0.10 mol dm^-3 HCl and 0.10 mol dm^-3 NaCl"),
          ("B", "0.20 mol dm^-3 CH3COOH and 0.10 mol dm^-3 NaOH"),
          ("C", "0.10 mol dm^-3 CH3COOH and 0.20 mol dm^-3 NaOH"),
          ("D", "0.10 mol dm^-3 HNO3 and 0.10 mol dm^-3 NH3")]),

        ("During the titration of 25.0 cm^3 of 0.10 mol dm^-3 ethanoic acid with 0.10 mol dm^-3 sodium hydroxide, what is the pH after 12.5 cm^3 of NaOH has been added?",
         [("A", "7.00"),
          ("B", "Equal to the pKa of ethanoic acid"),
          ("C", "Equal to 14 - pKa"),
          ("D", "Equal to the pKw of water")]),

        # Page 8: Q19, Q20, Q21 (Indicators & Chirality Topic 14 & 15)
        ("Methyl red has an indicator transition range of pH 4.4 to 6.2. For which titration is methyl red MOST suitable?",
         [("A", "Ethanoic acid (weak) with sodium hydroxide (strong)"),
          ("B", "Hydrochloric acid (strong) with ammonia (weak)"),
          ("C", "Methanoic acid (weak) with ammonia (weak)"),
          ("D", "Ethanedioic acid (weak) with sodium hydrogencarbonate (weak)")]),

        ("Which compound exhibits optical isomerism (enantiomerism)?",
         [("A", "Propane-1,2-diol"),
          ("B", "Propan-2-ol"),
          ("C", "2-methylpropan-2-ol"),
          ("D", "Butan-1-ol")]),

        ("A student prepares 2-hydroxy-2-methylbutanenitrile by reacting butanone with KCN and dilute sulfuric acid. Why is the reaction mixture optically inactive?",
         [("A", "The product does not contain a chiral carbon atom"),
          ("B", "The planar carbonyl group is attacked with equal probability from above and below, producing a 50:50 racemic mixture"),
          ("C", "The cyanide ion acts as an electrophile rather than a nucleophile"),
          ("D", "The reaction occurs via an SN2 mechanism with complete inversion")]),

        # Page 9: Q22, Q23, Q24 (Carbonyls & Carboxylic Acids Topic 15)
        ("Which test distinguishes between ethanal and propanone?",
         [("A", "Addition of 2,4-dinitrophenylhydrazine (Brady's reagent)"),
          ("B", "Warming with Tollens' reagent (ammoniacal silver nitrate)"),
          ("C", "Addition of phosphorus(V) chloride"),
          ("D", "Warming with iodine and aqueous sodium hydroxide")]),

        ("What organic product is formed when butanal is heated with acidified potassium dichromate(VI) under reflux?",
         [("A", "Butan-1-ol"),
          ("B", "Butanone"),
          ("C", "Butanoic acid"),
          ("D", "Butyl butanoate")]),

        ("Why does ethanoic acid have a higher boiling point (118 °C) than propan-1-ol (97 °C), despite having the same relative molecular mass (Mr = 60)?",
         [("A", "Ethanoic acid has stronger London dispersion forces"),
          ("B", "Ethanoic acid forms stable cyclic dimers held together by two hydrogen bonds"),
          ("C", "Propan-1-ol has a branched carbon chain"),
          ("D", "Ethanoic acid is completely ionised in the liquid state")]),

        # Page 10: Q25, Q26, Q27 (Acyl Chlorides & Esters Topic 15)
        ("What observation is made when ethanoyl chloride, CH3COCl, is added to water?",
         [("A", "A white precipitate of silver chloride forms"),
          ("B", "A vigorous exothermic reaction producing steamy acidic fumes of HCl"),
          ("C", "A sweet fruity odour is detected"),
          ("D", "Effervescence of hydrogen gas occurs")]),

        ("Which ester is formed by the reaction of methanol with propanoic acid in the presence of concentrated sulfuric acid?",
         [("A", "Ethyl methanoate"),
          ("B", "Methyl propanoate"),
          ("C", "Propyl methanoate"),
          ("D", "Methyl ethanoate")]),

        ("What are the products of the alkaline hydrolysis (saponification) of ethyl ethanoate with boiling aqueous sodium hydroxide?",
         [("A", "Ethanoic acid and ethanol"),
          ("B", "Sodium ethanoate and ethanol"),
          ("C", "Sodium propanoate and water"),
          ("D", "Ethanal and sodium ethoxide")]),

        # Page 11: Q28, Q29, Q30 (Spectroscopy & NMR Topic 15)
        ("How many non-equivalent carbon environments are present in pentan-3-one, CH3CH2COCH2CH3?",
         [("A", "2"),
          ("B", "3"),
          ("C", "4"),
          ("D", "5")]),

        ("In the high-resolution 1H NMR spectrum of methyl ethanoate, CH3COOCH3, what splitting pattern is observed for each signal?",
         [("A", "A triplet and a quartet"),
          ("B", "Two singlets"),
          ("C", "Two doublets"),
          ("D", "A singlet and a triplet")]),

        ("A compound has molecular formula C3H6O. Its infrared spectrum shows a strong absorption at 1715 cm^-1 and its 1H NMR spectrum consists of a single sharp singlet. What is the compound?",
         [("A", "Propanal"),
          ("B", "Propanone"),
          ("C", "Prop-2-en-1-ol"),
          ("D", "Methoxyethene")])
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
    # QUESTION 31 (18 MARKS) — ADVANCED KINETICS, MECHANISM & ARRHENIUS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Nitrogen monoxide reacts with hydrogen at 1000 K according to the equation:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>2NO(g) + 2H<sub>2</sub>(g) &longrightarrow; N<sub>2</sub>(g) + 2H<sub>2</sub>O(g)</b><br/>"
                           "A series of experiments was carried out to determine the kinetics of this reaction.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Data Table
    kin_data = [
        [Paragraph("<b>Experiment</b>", S['tbl_th']), Paragraph("<b>Initial [NO] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>Initial [H2] / mol dm^-3</b>", S['tbl_th']), Paragraph("<b>Initial Rate / mol dm^-3 s^-1</b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("1.50 x 10^-3", S['tbl_td']), Paragraph("2.00 x 10^-3", S['tbl_td']), Paragraph("4.80 x 10^-4", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("3.00 x 10^-3", S['tbl_td']), Paragraph("2.00 x 10^-3", S['tbl_td']), Paragraph("1.92 x 10^-3", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("1.50 x 10^-3", S['tbl_td']), Paragraph("6.00 x 10^-3", S['tbl_td']), Paragraph("1.44 x 10^-3", S['tbl_td'])],
    ]
    t_kin = Table(kin_data, colWidths=[2.5*cm, 4.5*cm, 4.5*cm, AVAIL_W - 11.5*cm])
    t_kin.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_kin)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Deduce the order of reaction with respect to NO and with respect to H<sub>2</sub>. Show all your reasoning clearly.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Write the overall rate equation and calculate the value of the rate constant, <i>k</i>, at 1000 K using Experiment 1. Include the units of <i>k</i>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: <i>k</i> = ..................................................... Units: .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>31 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A proposed two-step mechanism for the reaction is:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 1: &nbsp;&nbsp; 2NO(g) &rlhar; N<sub>2</sub>O<sub>2</sub>(g) &nbsp;&nbsp; (Fast equilibrium with constant <i>K</i><sub>c</sub>)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 2: &nbsp;&nbsp; N<sub>2</sub>O<sub>2</sub>(g) + H<sub>2</sub>(g) &longrightarrow; N<sub>2</sub>O(g) + H<sub>2</sub>O(g) &nbsp;&nbsp; (Slow, rate-determining step)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 3: &nbsp;&nbsp; N<sub>2</sub>O(g) + H<sub>2</sub>(g) &longrightarrow; N<sub>2</sub>(g) + H<sub>2</sub>O(g) &nbsp;&nbsp; (Fast)<br/>"
                           "Show that this mechanism is consistent with your deduced rate equation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The rate constant <i>k</i> was measured at several temperatures. A plot of ln <i>k</i> against 1/<i>T</i> gave a straight line with a gradient of -2.48 x 10^4 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Sketch the Arrhenius plot of ln <i>k</i> against 1/<i>T</i> on the axes provided below, indicating the gradient and intercept.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(width=AVAIL_W, height=5.5*cm, y_label="ln k", x_label="1 / T  /  10^-3 K^-1"))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the activation energy, <i>E</i><sub>a</sub>, for this reaction in kJ mol^-1. (<i>R</i> = 8.31 J mol^-1 K^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: <i>E</i><sub>a</sub> = ..................................................... kJ mol^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — ENERGETICS, TOTAL ENTROPY & BORN-HABER CYCLES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Titanium(IV) chloride, TiCl<sub>4</sub>, is an important intermediate in the industrial extraction of titanium metal and is a liquid at room temperature.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;The enthalpy data required to construct a Born-Haber cycle for TiCl<sub>4</sub> are given below:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    le_data = [
        [Paragraph("<b>Enthalpy Change</b>", S['tbl_th']), Paragraph("<b>Value / kJ mol^-1</b>", S['tbl_th'])],
        [Paragraph("Standard enthalpy of formation of TiCl4(l), ΔfH°", S['tbl_td_l']), Paragraph("-804.2", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of titanium, ΔatH°[Ti(s)]", S['tbl_td_l']), Paragraph("+473.0", S['tbl_td'])],
        [Paragraph("First ionisation energy of titanium, IE1", S['tbl_td_l']), Paragraph("+658.8", S['tbl_td'])],
        [Paragraph("Second ionisation energy of titanium, IE2", S['tbl_td_l']), Paragraph("+1309.8", S['tbl_td'])],
        [Paragraph("Third ionisation energy of titanium, IE3", S['tbl_td_l']), Paragraph("+2652.5", S['tbl_td'])],
        [Paragraph("Fourth ionisation energy of titanium, IE4", S['tbl_td_l']), Paragraph("+4174.6", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of chlorine, ΔatH°[1/2 Cl2(g)]", S['tbl_td_l']), Paragraph("+121.7", S['tbl_td'])],
        [Paragraph("First electron affinity of chlorine, EA1[Cl(g)]", S['tbl_td_l']), Paragraph("-348.8", S['tbl_td'])],
        [Paragraph("Enthalpy of vaporisation of TiCl4, ΔvapH°[TiCl4(l)]", S['tbl_td_l']), Paragraph("+40.0", S['tbl_td'])],
    ]
    t_le = Table(le_data, colWidths=[11.0*cm, AVAIL_W - 11.0*cm])
    t_le.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_le)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the experimental lattice energy, Δ<sub>LE</sub><i>H</i>, for TiCl<sub>4</sub>(s) using the data provided.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Experimental Lattice Energy = ..................................................... kJ mol^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;The theoretical lattice energy calculated assuming a purely ionic model is -8800 kJ mol^-1.<br/>"
                           "Compare the experimental and theoretical values. Explain the reasons for any difference in terms of the polarisation of the chloride ions by the Ti^4+ cation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>32 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In the Kroll process, titanium is extracted by the reduction of TiCl<sub>4</sub> with magnesium at 1073 K:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>TiCl<sub>4</sub>(g) + 2Mg(l) &longrightarrow; Ti(s) + 2MgCl<sub>2</sub>(l)</b><br/>"
                           "Data for this reaction at 1073 K:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Δ<i>H</i>° = -512.0 kJ mol^-1<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Δ<i>S</i>°_system = -142.5 J mol^-1 K^-1", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why the change in system entropy, Δ<i>S</i>°_system, is negative for this reaction.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the entropy change of the surroundings, Δ<i>S</i>°_surroundings, at 1073 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Δ<i>S</i>°_surroundings = ..................................................... J mol^-1 K^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the total entropy change, Δ<i>S</i>°_total, at 1073 K, and state whether the reaction is thermodynamically feasible at this temperature.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Δ<i>S</i>°_total = ..................................................... J mol^-1 K^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iv)&nbsp;&nbsp;Calculate the maximum temperature, in Kelvin, at which this reaction remains spontaneous (assuming Δ<i>H</i>° and Δ<i>S</i>°_system remain approximately constant with temperature).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Maximum Temperature = ..................................................... K", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — GAS-PHASE EQUILIBRIA, KP & THERMODYNAMIC COUPLING
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Methanol is manufactured on a multi-million tonne scale by the catalytic hydrogenation of carbon monoxide:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>CO(g) + 2H<sub>2</sub>(g) &rlhar; CH<sub>3</sub>OH(g)</b> &nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -90.8 kJ mol^-1", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;A reaction vessel of fixed volume at 500 K was charged with 1.00 mol of CO and 3.00 mol of H<sub>2</sub>. When equilibrium was established at a total pressure of 50.0 atm, 0.80 mol of methanol, CH<sub>3</sub>OH, was present.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the amounts (in moles) of CO and H<sub>2</sub> present at equilibrium.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Moles CO = ..................................... Moles H<sub>2</sub> = .....................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the mole fraction of each gas present at equilibrium.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: x(CO) = ..................... x(H<sub>2</sub>) = ..................... x(CH<sub>3</sub>OH) = .....................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the partial pressure of each gas at equilibrium at 50.0 atm.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: p(CO) = .............. atm, p(H<sub>2</sub>) = .............. atm, p(CH<sub>3</sub>OH) = .............. atm", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iv)&nbsp;&nbsp;Write the expression for the equilibrium constant, <i>K</i><sub>p</sub>, and calculate its value at 500 K. Include the units of <i>K</i><sub>p</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: <i>K</i><sub>p</sub> = ..................................................... Units = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>33 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Industrial methanol syntheses are typically operated at 500 K and 50–100 atm using a Cu/ZnO/Al<sub>2</sub>O<sub>3</sub> catalyst.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain, using Le Chatelier's principle and collision theory, why an operating temperature of 500 K is chosen as a compromise between rate and equilibrium yield.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using the relationship Δ<i>S</i>_total = <i>R</i> ln <i>K</i>, calculate the total entropy change, Δ<i>S</i>_total, for the methanol synthesis at 500 K using your calculated value of <i>K</i><sub>p</sub>. (<i>R</i> = 8.31 J mol^-1 K^-1).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Δ<i>S</i>_total = ..................................................... J mol^-1 K^-1", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ACID-BASE EQUILIBRIA, DIPROTIC ACIDS & BUFFERS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Ethanedioic acid (oxalic acid), H<sub>2</sub>C<sub>2</sub>O<sub>4</sub>, is a weak diprotic acid found in rhubarb leaves.<br/>"
                           "It dissociates in two successive stages in aqueous solution at 298 K:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stage 1: &nbsp;&nbsp; H<sub>2</sub>C<sub>2</sub>O<sub>4</sub>(aq) &rlhar; H+(aq) + HC<sub>2</sub>O<sub>4</sub>^-(aq) &nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>a1</sub> = 5.40 x 10^-2 mol dm^-3 &nbsp;&nbsp; (p<i>K</i><sub>a1</sub> = 1.27)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stage 2: &nbsp;&nbsp; HC<sub>2</sub>O<sub>4</sub>^-(aq) &rlhar; H+(aq) + C<sub>2</sub>O<sub>4</sub>^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>a2</sub> = 5.40 x 10^-5 mol dm^-3 &nbsp;&nbsp; (p<i>K</i><sub>a2</sub> = 4.27)", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Explain why the second acid dissociation constant, <i>K</i><sub>a2</sub>, is roughly 1000 times smaller than the first, <i>K</i><sub>a1</sub>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A 25.0 cm^3 sample of 0.0500 mol dm^-3 ethanedioic acid was titrated against 0.100 mol dm^-3 sodium hydroxide, NaOH(aq).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the volume of 0.100 mol dm^-3 NaOH required to reach the first equivalence point and the second equivalence point.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: First Equivalence Volume = ............ cm^3, Second Equivalence Volume = ............ cm^3", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;State the pH at the first half-equivalence point (after addition of half the volume required for the first equivalence point).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;The table lists three indicators and their pH transition ranges:", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))

    ind_data = [
        [Paragraph("<b>Indicator</b>", S['tbl_th']), Paragraph("<b>pH Range</b>", S['tbl_th']), Paragraph("<b>Colour in Acid</b>", S['tbl_th']), Paragraph("<b>Colour in Alkali</b>", S['tbl_th'])],
        [Paragraph("Methyl orange", S['tbl_td_l']), Paragraph("3.1 - 4.4", S['tbl_td']), Paragraph("Red", S['tbl_td']), Paragraph("Yellow", S['tbl_td'])],
        [Paragraph("Bromothymol blue", S['tbl_td_l']), Paragraph("6.0 - 7.6", S['tbl_td']), Paragraph("Yellow", S['tbl_td']), Paragraph("Blue", S['tbl_td'])],
        [Paragraph("Phenolphthalein", S['tbl_td_l']), Paragraph("8.3 - 10.0", S['tbl_td']), Paragraph("Colourless", S['tbl_td']), Paragraph("Pink", S['tbl_td'])],
    ]
    t_ind = Table(ind_data, colWidths=[4.0*cm, 3.5*cm, 4.0*cm, AVAIL_W - 11.5*cm])
    t_ind.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_ind)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("Select the most appropriate indicator to detect the SECOND equivalence point (pH ≈ 8.6) and justify your choice.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>34 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;A buffer solution was prepared by mixing 500 cm^3 of 0.200 mol dm^-3 sodium hydrogencarbonate, NaHCO<sub>3</sub>, and 500 cm^3 of 0.100 mol dm^-3 sodium carbonate, Na<sub>2</sub>CO<sub>3</sub>.<br/>"
                           "The equilibrium involved is:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCO<sub>3</sub>^-(aq) &rlhar; H+(aq) + CO<sub>3</sub>^2-(aq) &nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>a</sub> = 4.80 x 10^-11 mol dm^-3 (p<i>K</i><sub>a</sub> = 10.32 at 298 K)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the pH of this buffer solution at 298 K using the Henderson-Hasselbalch equation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the new pH of the solution when 5.00 x 10^-3 mol of solid sodium hydroxide, NaOH, is dissolved in 1.00 dm^3 of this buffer solution (assume no volume change).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: New pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — MULTI-STEP ORGANIC SYNTHESIS (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;<b>Multi-Step Synthesis and Stereochemical Control:</b><br/>"
                           "A pharmaceutical company plans to synthesise the local anaesthetic precursor <b>Compound Z</b> (ethyl 2-hydroxy-2-phenylpropanoate) from acetophenone (phenylethanone, C<sub>6</sub>H<sub>5</sub>COCH<sub>3</sub>).<br/>"
                           "The proposed synthetic pathway is:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 1:</b> &nbsp;&nbsp; C<sub>6</sub>H<sub>5</sub>COCH<sub>3</sub> + HCN &longrightarrow; C<sub>6</sub>H<sub>5</sub>C(OH)(CN)CH<sub>3</sub> &nbsp;&nbsp; (Compound W)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 2:</b> &nbsp;&nbsp; Compound W + dilute HCl(aq) + heat under reflux &longrightarrow; C<sub>6</sub>H<sub>5</sub>C(OH)(COOH)CH<sub>3</sub> &nbsp;&nbsp; (Compound X)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Step 3:</b> &nbsp;&nbsp; Compound X + ethanol + conc. H<sub>2</sub>SO<sub>4</sub> &longrightarrow; C<sub>6</sub>H<sub>5</sub>C(OH)(COOCH<sub>2</sub>CH<sub>3</sub>)CH<sub>3</sub> &nbsp;&nbsp; (Compound Z)", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;State the reagents and conditions used in the laboratory to safely generate hydrogen cyanide <i>in situ</i> for Step 1.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Draw the complete nucleophilic addition mechanism for Step 1.<br/>"
                           "Include relevant dipoles, lone pairs of electrons, curly arrows, and the structure of the intermediate.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for nucleophilic addition mechanism: acetophenone + cyanide ion"))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Compound W contains a chiral carbon atom. Explain why the product formed in Step 1 does not rotate the plane of plane-polarised light.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>*35 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;Describe an experimental procedure to synthesise and purify pure liquid <b>Compound Z</b> (ethyl 2-hydroxy-2-phenylpropanoate) from solid Compound X and ethanol (Step 3).<br/>"
                           "Your plan should include:<br/>"
                           "- The experimental setup for the reaction, including heating under reflux and the role of the concentrated sulfuric acid catalyst.<br/>"
                           "- Isolation of the crude organic ester using a separating funnel, including specific washing steps to remove unreacted acid catalyst and inorganic impurities.<br/>"
                           "- Drying of the organic layer with an appropriate anhydrous salt.<br/>"
                           "- Final purification of the ester by fractional or simple distillation, stating how purity would be confirmed.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Compound X (2-hydroxy-2-phenylpropanoic acid) can also react with phosphorus(V) chloride, PCl<sub>5</sub>.<br/>"
                           "State two observations made when anhydrous PCl<sub>5</sub> is added to solid Compound X, and write the formula of the organic product formed when both the -OH and -COOH groups react.", S['q_subpart']))
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
    # QUESTION 36 (15 MARKS) — GREEN CHEMISTRY: METHYL METHACRYLATE (PERSPEX)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Green Chemistry and Industrial Polymer Synthesis:</b><br/>"
                           "Methyl methacrylate (MMA, CH<sub>2</sub>=C(CH<sub>3</sub>)COOCH<sub>3</sub>, <i>M</i><sub>r</sub> = 100.12) is the monomer used to manufacture poly(methyl methacrylate) (PMMA, Perspex or Plexiglas).<br/>"
                           "Traditionally, MMA was synthesized via the <b>Acetone Cyanohydrin (ACH)</b> route:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;CH<sub>3</sub>COCH<sub>3</sub> + HCN + H<sub>2</sub>SO<sub>4</sub> + CH<sub>3</sub>OH &longrightarrow; CH<sub>2</sub>=C(CH<sub>3</sub>)COOCH<sub>3</sub> + NH<sub>4</sub>HSO<sub>4</sub><br/>"
                           "A modern, greener industrial process is the <b>Alpha Process</b> developed by Lucite International:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Stage 1: &nbsp;&nbsp; C<sub>2</sub>H<sub>4</sub> + CO + CH<sub>3</sub>OH &longrightarrow; CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub> &nbsp;&nbsp; (Methyl propanoate)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Stage 2: &nbsp;&nbsp; CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub> + HCHO &longrightarrow; CH<sub>2</sub>=C(CH<sub>3</sub>)COOCH<sub>3</sub> + H<sub>2</sub>O", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Calculate the atom economy of the traditional ACH route for the production of MMA, assuming ammonium hydrogensulfate is a waste byproduct.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Atom Economy (ACH Route) = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the overall atom economy of the two-stage Alpha Process.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Atom Economy (Alpha Process) = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>36 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Discuss three key environmental and economic advantages of the Alpha Process compared to the ACH route, referring to toxicity of feedstocks, waste disposal, and energy consumption.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Draw the displayed formula of two repeat units of the polymer poly(methyl methacrylate) (PMMA), and explain why PMMA cannot be chemically recycled via simple hydrolysis, unlike polyesters such as PET.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;PMMA can be thermally depolymerised (cracked) back into pure MMA monomer by heating to 400 °C in the absence of air.<br/>"
                           "State the sign of Δ<i>H</i> and Δ<i>S</i>_system for this depolymerisation process, and explain why high temperature favours the formation of monomer.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — FORENSIC PHARMACEUTICAL SPECTROSCOPY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Forensic Drug Analysis and Spectroscopic Elucidation:</b><br/>"
                           "A seized package containing an unknown white crystalline powder, <b>Compound Q</b>, was analysed by forensic scientists. Elemental analysis showed that <b>Compound Q</b> contains 70.59% carbon, 5.88% hydrogen, and 23.53% oxygen by mass.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Calculate the empirical formula of <b>Compound Q</b>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Empirical Formula = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;The mass spectrum of <b>Compound Q</b> displays a molecular ion peak, [M]+, at <i>m</i>/<i>z</i> = 136.0, and a base peak at <i>m</i>/<i>z</i> = 105.0.<br/>"
                           "Determine the molecular formula of <b>Compound Q</b>, and identify the fragment ion responsible for the peak at <i>m</i>/<i>z</i> = 105.0.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Molecular Formula = ......................... Fragment at <i>m</i>/<i>z</i> 105 = .........................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>37 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The spectroscopic data for <b>Compound Q</b> are summarised below:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Infrared spectrum:</b><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Sharp, strong absorption band at 1725 cm^-1.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Strong absorption band at 1280 cm^-1.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• No absorption in the regions 3200–3600 cm^-1 or 2500–3300 cm^-1.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>13C NMR spectrum:</b><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Peaks at δ = 52.0 ppm, 128.5 ppm, 129.8 ppm, 130.5 ppm, 133.0 ppm, and 167.0 ppm.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>High-resolution 1H NMR spectrum:</b><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Singlet at δ = 3.90 ppm (relative area = 3H)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Multiplet at δ = 7.40–7.60 ppm (relative area = 3H)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Multiplet at δ = 8.00–8.10 ppm (relative area = 2H)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Using the infrared spectrum, identify the two functional groups or bond types indicated by the absorptions at 1725 cm^-1 and 1280 cm^-1.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Analyse the 1H NMR spectrum by assigning each of the three signals to the protons responsible, explaining their chemical shift and splitting.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Deduce the structural formula and state the systematic IUPAC name of <b>Compound Q</b>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Systematic IUPAC Name = .....................................................", S['ans_prompt']))
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 13 Synoptic Mock 1 (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Units: rate / ([A]^2[B]) = (mol dm^-3 s^-1) / (mol^3 dm^-9) = dm^6 mol^-2 s^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("720 s = 3 half-lives (3 x 240 s) => fraction remaining = (1/2)^3 = 1/8.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Gradient = -Ea / R => Ea = -(-9.62 x 10^3) x 8.31 = 79942 J mol^-1 = +79.9 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Rate equation depends only on species in the rate-determining step.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Decomposition of CaCO3(s) produces 1 mole of gas from solid, giving positive ΔS_system.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔS°_system = S°[CO2] - (S°[C] + S°[O2]) = 213.6 - (5.7 + 205.0) = +2.9 J mol^-1 K^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("T_crossover = ΔH / ΔS_system = 85000 / 170.0 = 500 K. Feasible above 500 K.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("MgO contains Mg^2+ and O^2- ions (2+ and 2- charges), giving greatest electrostatic attraction.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ag+ has high polarising power and I- is large/polarisable, leading to significant covalent bonding.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Exothermic reaction: increasing T shifts equilibrium left, reducing Kp and equilibrium yield.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔS_total = R ln K = 8.31 x ln(1.0 x 10^-4) = 8.31 x (-9.21) = -76.5 J mol^-1 K^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Total moles = 0.20 + 0.40 + 0.40 = 1.00 mol. Mole fraction = 0.20/1.00 = 0.20. p = 0.20 x 2.0 = 0.40 atm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Only temperature alters the numerical value of equilibrium constants Kc and Kp.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("[OH-] = 2 x 0.025 = 0.050 mol dm^-3. pOH = 1.30 => pH = 14.00 - 1.30 = 12.70.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Kw) = sqrt(5.13 x 10^-13) = 7.16 x 10^-7 mol dm^-3 => pH = 6.14. Neutral since [H+] = [OH-].", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ka = 10^-4.80 = 1.58 x 10^-5. [H+] = sqrt(Ka x c) = sqrt(1.58 x 10^-5 x 0.20) = 1.78 x 10^-3 => pH = 2.75.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Partial neutralisation of weak acid by strong base forms CH3COOH/CH3COONa buffer mixture.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At half-neutralisation of a weak acid, [HA] = [A-], therefore pH = pKa.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Strong acid - weak base titration produces an acidic equivalence point (pH ~5), matching methyl red.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Propane-1,2-diol contains carbon-2 bonded to four different groups: -H, -CH3, -OH, -CH2OH.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Planar carbonyl carbon allows nucleophilic attack with 50:50 equal probability from either face.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Tollens' reagent is reduced to a silver mirror by aldehydes (ethanal) but not ketones (propanone).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Refluxing primary aldehyde butanal with acidified dichromate oxidises it fully to butanoic acid.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carboxylic acids form stable cyclic dimers via two intermolecular hydrogen bonds, raising bp.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Acyl chlorides violently hydrolyse with water, producing steamy acidic fumes of HCl gas.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Methanol (CH3OH) + propanoic acid (CH3CH2COOH) forms methyl propanoate (CH3CH2COOCH3).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Alkaline hydrolysis of ethyl ethanoate with NaOH produces sodium ethanoate and ethanol.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Symmetric pentan-3-one has 3 carbon environments: methyl (C1, C5), methylene (C2, C4), and C=O (C3).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Both methyl groups in CH3COOCH3 have zero adjacent protons, each appearing as a sharp singlet.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Propanone (CH3COCH3) has C=O absorption at 1715 cm^-1 and 6 equivalent protons as a single singlet.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Advanced Kinetics, Mechanism & Arrhenius (18 Marks)",
         "<b>(a)(i) [4 Marks]</b><br/>"
         "• Comparing Exp 1 and Exp 2: [H2] is constant; [NO] doubles (1.50x10^-3 to 3.00x10^-3) [1]<br/>"
         "• Rate increases by a factor of 1.92x10^-3 / 4.80x10^-4 = 4.0 = 2^2 => Order with respect to NO = 2 [1]<br/>"
         "• Comparing Exp 1 and Exp 3: [NO] is constant; [H2] triples (2.00x10^-3 to 6.00x10^-3) [1]<br/>"
         "• Rate increases by 1.44x10^-3 / 4.80x10^-4 = 3.0 = 3^1 => Order with respect to H2 = 1 [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Rate equation: rate = k[NO]^2[H2] [1]<br/>"
         "• k = rate / ([NO]^2[H2]) = 4.80x10^-4 / ((1.50x10^-3)^2 x (2.00x10^-3)) = 1.07 x 10^5 [1]<br/>"
         "• Units: (mol dm^-3 s^-1) / (mol^3 dm^-9) = dm^6 mol^-2 s^-1 [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• From Step 1 equilibrium: Kc = [N2O2] / [NO]^2 => [N2O2] = Kc[NO]^2 [1]<br/>"
         "• Rate of reaction is controlled by the slow rate-determining step: rate = k2[N2O2][H2] [1]<br/>"
         "• Substituting [N2O2]: rate = k2(Kc[NO]^2)[H2] = k_overall[NO]^2[H2] [1]<br/>"
         "• This matches the experimentally observed rate equation, confirming consistency [1].<br/><br/>"
         "<b>(c)(i) [3 Marks]</b><br/>"
         "• Graph drawn with straight line of negative slope [1]<br/>"
         "• Gradient labeled as -Ea / R [1]<br/>"
         "• y-intercept labeled as ln A [1].<br/><br/>"
         "<b>(c)(ii) [4 Marks]</b><br/>"
         "• Gradient = -Ea / R => -2.48 x 10^4 K = -Ea / 8.31 [1]<br/>"
         "• Ea = 2.48 x 10^4 x 8.31 = 206088 J mol^-1 [1]<br/>"
         "• Ea = +206.1 kJ mol^-1 (allow 206 kJ mol^-1) [1]<br/>"
         "• Correct sign (+) and units (kJ mol^-1) [1]."),

        ("Question 32: Energetics, Total Entropy & Born-Haber Cycles (18 Marks)",
         "<b>(a)(i) [5 Marks]</b><br/>"
         "• Born-Haber cycle equation: ΔfH°[TiCl4(l)] = ΔatH°[Ti] + (IE1 + IE2 + IE3 + IE4) + 4 x ΔatH°[Cl] + 4 x EA1[Cl] + ΔLEH[TiCl4(s)] - ΔvapH°[TiCl4] (or cycle formulated for solid) [2]<br/>"
         "• Sum of ionisations = 658.8 + 1309.8 + 2652.5 + 4174.6 = +8795.7 kJ mol^-1 [1]<br/>"
         "• 4 x atomisation Cl = 4 x (+121.7) = +486.8 kJ mol^-1; 4 x EA Cl = 4 x (-348.8) = -1395.2 kJ mol^-1 [1]<br/>"
         "• ΔLEH = -804.2 - [473.0 + 8795.7 + 486.8 - 1395.2 - 40.0] = -804.2 - 8320.3 = -9124.5 kJ mol^-1 (allow -9125 kJ mol^-1) [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Experimental lattice energy (-9125 kJ mol^-1) is significantly more exothermic than theoretical value (-8800 kJ mol^-1) [1]<br/>"
         "• The Ti^4+ cation has a very high charge (+4) and relatively small ionic radius, resulting in an exceptionally high charge density and polarising power [1]<br/>"
         "• Ti^4+ polarises the electron clouds of the adjacent chloride (Cl-) anions, distorting them towards the cation [1]<br/>"
         "• This introduces substantial covalent bonding character, which adds extra bonding strength not accounted for by the purely electrostatic ionic model [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• Reactants contain 1 mole of gas (TiCl4(g)) and 2 moles of liquid [1]<br/>"
         "• Products contain only solid (Ti(s)) and liquid (MgCl2(l)); loss of the gas phase results in a dramatic reduction in microstates/disorder [1].<br/><br/>"
         "<b>(b)(ii) [2 Marks]</b><br/>"
         "• ΔS_surroundings = -ΔH / T = -(-512000 J mol^-1) / 1073 K [1]<br/>"
         "• = +477.2 J mol^-1 K^-1 [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• ΔS_total = ΔS_system + ΔS_surroundings = -142.5 + 477.2 = +334.7 J mol^-1 K^-1 [1]<br/>"
         "• Since ΔS_total > 0, the reaction is thermodynamically feasible at 1073 K [1].<br/><br/>"
         "<b>(b)(iv) [3 Marks]</b><br/>"
         "• At maximum temperature, ΔS_total = 0 => ΔS_surroundings = -ΔS_system = +142.5 J mol^-1 K^-1 [1]<br/>"
         "• T_max = -ΔH / ΔS_system = 512000 / 142.5 [1]<br/>"
         "• T_max = 3593 K (approx. 3600 K) [1]."),

        ("Question 33: Gas-Phase Equilibria, Kp & Thermodynamic Coupling (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• ICE table: CO + 2H2 <=> CH3OH<br/>"
         "• Equilibrium moles of CH3OH = 0.80 mol [1]<br/>"
         "• Equilibrium moles of CO = 1.00 - 0.80 = 0.20 mol [1]<br/>"
         "• Equilibrium moles of H2 = 3.00 - 2(0.80) = 1.40 mol [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Total moles at equilibrium = 0.20 + 1.40 + 0.80 = 2.40 mol [1]<br/>"
         "• Mole fraction x(CO) = 0.20 / 2.40 = 0.0833 [1]<br/>"
         "• Mole fraction x(H2) = 1.40 / 2.40 = 0.5833; x(CH3OH) = 0.80 / 2.40 = 0.3333 [1].<br/><br/>"
         "<b>(a)(iii) [2 Marks]</b><br/>"
         "• p(CO) = 0.0833 x 50.0 = 4.17 atm [1]<br/>"
         "• p(H2) = 0.5833 x 50.0 = 29.17 atm; p(CH3OH) = 0.3333 x 50.0 = 16.67 atm [1].<br/><br/>"
         "<b>(a)(iv) [4 Marks]</b><br/>"
         "• Expression: Kp = p(CH3OH) / (p(CO) x p(H2)^2) [1]<br/>"
         "• Kp = 16.67 / (4.17 x (29.17)^2) = 16.67 / (4.17 x 850.89) = 16.67 / 3548.2 [1]<br/>"
         "• Kp = 4.70 x 10^-3 [1]<br/>"
         "• Units: atm / (atm x atm^2) = atm^-2 [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• The forward reaction is exothermic (ΔH = -90.8 kJ mol^-1) [1]<br/>"
         "• By Le Chatelier's principle, lower temperature favours the forward reaction and increases equilibrium yield of methanol [1]<br/>"
         "• However, at lower temperatures the rate is too slow because fewer particles have E >= Ea; 500 K provides an economically viable compromise between high rate and acceptable yield [1].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• ΔS_total = R ln Kp = 8.314 x ln(4.70 x 10^-3) [1]<br/>"
         "• ln(4.70 x 10^-3) = -5.360 [1]<br/>"
         "• ΔS_total = 8.314 x (-5.360) = -44.57 J mol^-1 K^-1 (approx. -44.6 J mol^-1 K^-1) [1]."),

        ("Question 34: Acid-Base Equilibria, Diprotic Acids & Buffers (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• In the second dissociation, a positively charged proton (H+) must be removed from a negatively charged anion (HC2O4^-) [1]<br/>"
         "• Electrostatic attraction between the opposite charges strongly opposes loss of the proton, making Ka2 much smaller [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• Moles of ethanedioic acid = 0.0250 x 0.0500 = 1.25 x 10^-3 mol [1]<br/>"
         "• 1st equivalence: moles NaOH = 1.25 x 10^-3 mol => V = (1.25 x 10^-3) / 0.100 = 0.0125 dm^3 = 12.5 cm^3 [1]<br/>"
         "• 2nd equivalence requires exactly double the volume: 2 x 12.5 = 25.0 cm^3 [1].<br/><br/>"
         "<b>(b)(ii) [2 Marks]</b><br/>"
         "• At half-equivalence 1 (V = 6.25 cm^3), [H2C2O4] = [HC2O4^-] [1]<br/>"
         "• Therefore, pH = pKa1 = 1.27 [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• Phenolphthalein [1]<br/>"
         "• The vertical pH jump at the second equivalence point spans pH 7.5 to 10.0, which entirely encompasses phenolphthalein's transition range (8.3 to 10.0) [1].<br/><br/>"
         "<b>(c)(i) [4 Marks]</b><br/>"
         "• In 1.00 dm^3: moles HCO3^- = 0.500 x 0.200 = 0.100 mol => [HCO3^-] = 0.100 mol dm^-3 [1]<br/>"
         "• Moles CO3^2- = 0.500 x 0.100 = 0.0500 mol => [CO3^2-] = 0.0500 mol dm^-3 [1]<br/>"
         "• Henderson-Hasselbalch: pH = pKa + log([CO3^2-] / [HCO3^-]) = 10.32 + log(0.0500 / 0.100) [1]<br/>"
         "• pH = 10.32 + log(0.50) = 10.32 - 0.301 = 10.02 (allow 10.0) [1].<br/><br/>"
         "<b>(c)(ii) [5 Marks]</b><br/>"
         "• Added OH- reacts: HCO3^- + OH- --> CO3^2- + H2O [1]<br/>"
         "• New moles HCO3^- = 0.100 - 0.0050 = 0.0950 mol [1]<br/>"
         "• New moles CO3^2- = 0.0500 + 0.0050 = 0.0550 mol [1]<br/>"
         "• New pH = 10.32 + log(0.0550 / 0.0950) = 10.32 + log(0.5789) = 10.32 - 0.237 [1]<br/>"
         "• New pH = 10.08 (resists pH change effectively, rising by only +0.06 units) [1]."),

        ("Question 35: Multi-Step Organic Synthesis (* Level of Response) (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Potassium cyanide, KCN (or NaCN) [1]<br/>"
         "• Dilute sulfuric acid (or dilute HCl) [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Dipoles shown on C=O (Cδ+, Oδ-) and lone pair on carbon of :CN- [1]<br/>"
         "• Curly arrow from lone pair on carbon of :CN- to carbonyl carbon [1]<br/>"
         "• Curly arrow from C=O double bond to oxygen forming tetrahedral intermediate C6H5C(O-)(CN)CH3 [1]<br/>"
         "• Curly arrow from lone pair on O- to H+ (or H-CN) forming -OH group [1].<br/><br/>"
         "<b>(a)(iii) [3 Marks]</b><br/>"
         "• The carbonyl group in acetophenone is planar around the sp2 hybridised carbonyl carbon [1]<br/>"
         "• Nucleophilic attack by cyanide ion is equally probable from above and below the plane [1]<br/>"
         "• Equal amounts of the two enantiomers are formed, producing a 50:50 racemic mixture that causes no net rotation of plane-polarised light [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Detailed, coherent and logically sequenced protocol covering all four stages. Reaction: mix solid Compound X with excess ethanol and concentrated H2SO4 catalyst in a round-bottomed flask; attach Liebig condenser vertically and heat under reflux for ~30–45 minutes. Separation: cool mixture, pour into separating funnel containing water/dilute aqueous NaHCO3; shake and invert with frequent venting to release CO2 gas from neutralising excess acid catalyst; discard aqueous layer; wash organic layer with saturated NaCl (brine) to remove residual ethanol and water. Drying: transfer organic ester layer to a conical flask, add anhydrous magnesium sulfate (MgSO4) or CaCl2; swirl until liquid becomes transparent and drying agent flows freely; gravity filter. Distillation: assemble distillation apparatus with thermometer bulb positioned opposite condenser side-arm; heat gently and collect liquid fraction distilling at the narrow literature boiling range of Compound Z. Purity check: verify narrow boiling point range or run 1H NMR / TLC showing single spot.<br/>"
         "• Level 2 (3-4 marks): Logical plan mentioning reflux with conc H2SO4, separating funnel with NaHCO3 wash, drying agent, and distillation, but lacking specific procedural detail or venting instructions.<br/>"
         "• Level 1 (1-2 marks): Basic list of steps with major omissions in washing, drying, or purification.<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Observations: Vigorous reaction / effervescence; dense steamy/misty acidic fumes of HCl gas [2]<br/>"
         "• Organic product: C6H5C(Cl)(COCl)CH3 (both -OH and -COOH react to form chloro and acyl chloride groups) [1]."),

        ("Question 36: Green Chemistry: Methyl Methacrylate (Perspex) (15 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Mr(MMA) = 100.12 [1]<br/>"
         "• Total Mr of reactants = Mr(CH3COCH3) + Mr(HCN) + Mr(H2SO4) + Mr(CH3OH) = 58.08 + 27.03 + 98.08 + 32.04 = 215.23 [1]<br/>"
         "• Atom Economy = (100.12 / 215.23) x 100% = 46.5% [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Overall reaction: C2H4 + CO + 2CH3OH + HCHO --> CH2=C(CH3)COOCH3 + H2O (or C2H4 + CO + CH3OH + HCHO --> MMA + H2O)<br/>"
         "• Mr(reactants) = Mr(C2H4) + Mr(CO) + Mr(CH3OH) + Mr(HCHO) = 28.05 + 28.01 + 32.04 + 30.03 = 118.13 [1]<br/>"
         "• Mr(desired product MMA) = 100.12 [1]<br/>"
         "• Atom Economy = (100.12 / 118.13) x 100% = 84.8% [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Feedstock toxicity: The Alpha Process avoids extremely hazardous, volatile, and highly lethal hydrogen cyanide (HCN) gas used in the ACH route [1]<br/>"
         "• Waste disposal: The ACH route produces an equimolar quantity of corrosive, hazardous ammonium hydrogensulfate (NH4HSO4) waste, whereas the Alpha process produces only water as byproduct [1]<br/>"
         "• Atom efficiency: Alpha process has almost double the atom economy (84.8% vs 46.5%), drastically conserving raw chemical resources [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Displayed formula of PMMA repeat units: -[CH2-C(CH3)(COOCH3)]- with open extension bonds [2]<br/>"
         "• PMMA is an addition polymer with an unreactive, all-carbon single-bond (C-C) saturated backbone that resists nucleophilic hydrolytic attack, unlike polyesters which possess polar ester bonds (-COO-) directly in the main chain [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• ΔH > 0 (endothermic, breaking strong C-C bonds) [1]<br/>"
         "• ΔS_system > 0 (depolymerisation converts one giant solid macromolecule into many small volatile monomer molecules, vastly increasing disorder) [1]<br/>"
         "• At high temperatures, the -TΔS_system term becomes very negative, overcoming positive ΔH and making ΔG < 0 (or ΔS_total > 0), driving spontaneous depolymerisation [1]."),

        ("Question 37: Forensic Pharmaceutical Spectroscopy (15 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Moles C = 70.59 / 12.0 = 5.8825 [1]<br/>"
         "• Moles H = 5.88 / 1.0 = 5.880; Moles O = 23.53 / 16.0 = 1.4706 [1]<br/>"
         "• Mole ratio: C = 5.8825/1.4706 = 4.0; H = 5.880/1.4706 = 4.0; O = 1.0 => Empirical formula = C4H4O [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Empirical formula mass of C4H4O = (4 x 12) + (4 x 1) + 16 = 68.0<br/>"
         "• Mr = 136.0 => 136.0 / 68.0 = 2 => Molecular formula = C8H8O2 [1]<br/>"
         "• Base peak at m/z = 105: [C6H5CO]+ (benzoyl cation) formed by loss of methoxy radical, .OCH3 (31 mass units) [2].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• 1725 cm^-1: Carbonyl group (C=O), specifically an ester carbonyl conjugated to an aromatic ring [1]<br/>"
         "• 1280 cm^-1: C-O ester stretch [1].<br/><br/>"
         "<b>(c)(ii) [4 Marks]</b><br/>"
         "• δ = 3.90 ppm (3H singlet): Methoxy protons (-O-CH3) attached directly to electronegative oxygen atom; no neighbouring protons on adjacent carbons gives singlet [2]<br/>"
         "• δ = 7.40–7.60 ppm (3H multiplet): Meta and para aromatic protons on monosubstituted benzene ring [1]<br/>"
         "• δ = 8.00–8.10 ppm (2H multiplet): Ortho aromatic protons on benzene ring, shifted downfield by electron-withdrawing ester carbonyl group [1].<br/><br/>"
         "<b>(c)(iii) [3 Marks]</b><br/>"
         "• Structural formula: C6H5COOCH3 (or displayed formula showing benzene ring attached to -COOCH3) [2]<br/>"
         "• Systematic IUPAC name: Methyl benzoate [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 13 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
'''

with open('build_usman_week13_quiz.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated build_usman_week13_quiz.py successfully.")
