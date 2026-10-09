"""
build_usman_week5_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 5 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 12A.3: Understanding Entropy Changes (Feasibility, Crossover Temperature, Enthalpy vs Entropy Driven)
  - 12B.1: Lattice Energy and Born-Haber Cycles (Definitions, Standard Enthalpies, Group 1 & 2 Halides/Oxides)

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
    "Usman_Edexcel_Chem_U4_Week5_150M_Challenging_Quiz.pdf"
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
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="ΔS_total / J K^-1 mol^-1", x_label="Temperature T / K"):
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


class BornHaberCycleBox(Flowable):
    """Draws a dedicated energy level diagram sketch box for Born-Haber cycle construction."""
    def __init__(self, width=AVAIL_W, height=7.2*cm, title="Energy / Enthalpy"):
        super().__init__()
        self.width = width
        self.height = height
        self.title = title

    def wrap(self, availWidth, availHeight):
        return self.width, self.height

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(BORDER)
        self.canv.setLineWidth(0.8)
        self.canv.rect(0, 0, self.width, self.height)

        # Draw vertical energy arrow on far left
        ox = 32
        oy = 15
        h = self.height - 30
        self.canv.setStrokeColor(NAVY)
        self.canv.setLineWidth(1.2)
        self.canv.line(ox, oy, ox, oy + h)
        self.canv.line(ox, oy + h, ox - 3, oy + h - 6)
        self.canv.line(ox, oy + h, ox + 3, oy + h - 6)

        self.canv.saveState()
        self.canv.setFont(FONT['Bold'], 8)
        self.canv.setFillColor(NAVY)
        self.canv.translate(ox - 14, oy + h / 2)
        self.canv.rotate(90)
        self.canv.drawCentredString(0, 0, self.title)
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 5 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 5 (150 Marks)...")
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

    # Candidate Grid
    tbl_cand = Table([
        [Paragraph("Candidate surname", S['edx_meta']), Paragraph("Other names", S['edx_meta'])],
        [Paragraph("<b>USMAN</b>", S['edx_meta_b']), Paragraph("<b>Grade A* Scholar</b>", S['edx_meta_b'])],
        [Paragraph("Centre Number &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Candidate Number<br/>"
                   "<b>[  9  ][  5  ][  1  ][  0  ][  2  ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
                   "<b>[  0  ][  0  ][  5  ][  5  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W05</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 5 ASSESSMENT: TOPIC 12A.3 FEASIBILITY & 12B.1 BORN-HABER CYCLES</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 5 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 12A.3: Understanding Entropy Changes (Feasibility & Crossover T)<br/>Topic 12B.1: Lattice Energy, ΔLE H and Born-Haber Cycles (Standard Cycles & Definitions)", S['edx_meta'])],
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

    # Instructions Box
    instr_text = (
        "<b>INSTRUCTIONS TO CANDIDATES</b><br/>"
        "- Use black ink or ball-point pen. Fill in the boxes at the top of this page.<br/>"
        "- Answer <b>ALL</b> questions in Section A, Section B, and Section C.<br/>"
        "- In Section A (Questions 1 to 30), select your answer by placing a clear cross in the box <b>[X]</b>.<br/>"
        "- In Section B and C, show all working in calculation questions. Include appropriate signs and units where required.<br/>"
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
        # Page 2: Q1, Q2, Q3
        ("Which equation represents the standard lattice energy of sodium chloride, using the formation definition?",
         [("A", "Na(s) + 1/2 Cl2(g) —> NaCl(s)"),
          ("B", "Na+(g) + Cl-(g) —> NaCl(s)"),
          ("C", "NaCl(s) —> Na+(g) + Cl-(g)"),
          ("D", "Na+(aq) + Cl-(aq) —> NaCl(s)")]),

        ("Which equation defines the first electron affinity of oxygen?",
         [("A", "O(g) + e- —> O-(g)"),
          ("B", "1/2 O2(g) + e- —> O-(g)"),
          ("C", "O-(g) + e- —> O2-(g)"),
          ("D", "O(s) + e- —> O-(g)")]),

        ("Why is the second electron affinity of oxygen, O-(g) + e- —> O2-(g), endothermic (ΔH > 0)?",
         [("A", "Energy is required to break the covalent O=O bond"),
          ("B", "Work must be done to overcome electrostatic repulsion between the incoming electron and the negative O- ion"),
          ("C", "The O2- ion has an unstable noble gas electron configuration"),
          ("D", "The second electron enters a higher principal quantum shell (n = 3)")]),

        # Page 3: Q4, Q5, Q6
        ("Which enthalpy change corresponds to the standard enthalpy of atomisation of chlorine, ΔatH°?",
         [("A", "Cl2(g) —> 2Cl(g)"),
          ("B", "1/2 Cl2(g) —> Cl(g)"),
          ("C", "Cl2(l) —> 2Cl(g)"),
          ("D", "Cl-(g) —> Cl(g) + e-")]),

        ("Which ionisation enthalpy requires the greatest amount of energy per mole?",
         [("A", "First ionisation energy of sodium, Na(g) —> Na+(g) + e-"),
          ("B", "First ionisation energy of magnesium, Mg(g) —> Mg+(g) + e-"),
          ("C", "Second ionisation energy of magnesium, Mg+(g) —> Mg2+(g) + e-"),
          ("D", "Second ionisation energy of sodium, Na+(g) —> Na2+(g) + e-")]),

        ("A reaction has ΔH = +90 kJ mol^-1 and ΔS_system = +250 J K^-1 mol^-1. At what temperature does the reaction become feasible?",
         [("A", "Below 360 K"),
          ("B", "Above 360 K"),
          ("C", "Above 2780 K"),
          ("D", "It is feasible at all temperatures")]),

        # Page 4: Q7, Q8, Q9
        ("For a reaction where ΔH < 0 and ΔS_system < 0, what is the shape of the graph of ΔS_total against temperature T?",
         [("A", "A horizontal straight line with constant positive slope"),
          ("B", "A curve that starts high and decreases as temperature increases"),
          ("C", "A curve that starts low and increases linearly as temperature increases"),
          ("D", "A vertical line intersecting the temperature axis at 298 K")]),

        ("Given data: ΔfH°[NaCl(s)] = -411 kJ mol^-1, ΔatH°[Na] = +107 kJ mol^-1, 1st IE[Na] = +496 kJ mol^-1, ΔatH°[Cl] = +122 kJ mol^-1, 1st EA[Cl] = -349 kJ mol^-1. What is the lattice energy of formation of NaCl(s)?",
         [("A", "-787 kJ mol^-1"),
          ("B", "+787 kJ mol^-1"),
          ("C", "-545 kJ mol^-1"),
          ("D", "-889 kJ mol^-1")]),

        ("Which of the following compounds would be expected to have the most exothermic lattice energy of formation?",
         [("A", "NaCl"),
          ("B", "MgCl2"),
          ("C", "MgO"),
          ("D", "BaO")]),

        # Page 5: Q10, Q11, Q12
        ("Which enthalpy change is represented by the downward arrow in a standard Born-Haber cycle from gaseous ions to the ionic solid?",
         [("A", "Enthalpy of formation"),
          ("B", "Lattice energy of formation"),
          ("C", "Enthalpy of atomisation"),
          ("D", "Enthalpy of hydration")]),

        ("Consider the hypothetical compound calcium(I) chloride, CaCl(s). Why does CaCl(s) spontaneously disproportionate into Ca(s) and CaCl2(s) under standard conditions?",
         [("A", "The first ionisation energy of calcium is endothermic"),
          ("B", "The lattice energy of CaCl2 is much more exothermic than that of CaCl due to the 2+ charge of Ca2+"),
          ("C", "Calcium(I) chloride has a covalent molecular structure"),
          ("D", "Chlorine cannot form negative chloride ions in the presence of Ca+")]),

        ("Which statement regarding the crossover temperature, T_crossover, is correct?",
         [("A", "At T = T_crossover, the equilibrium constant K must equal 0"),
          ("B", "At T = T_crossover, ΔS_total = 0 and ΔS_surroundings = -ΔS_system"),
          ("C", "At T = T_crossover, the reaction stops occurring at the molecular level"),
          ("D", "T_crossover can be calculated for reactions where ΔH and ΔS_system have opposite signs")]),

        # Page 6: Q13, Q14, Q15
        ("For the reaction: 2SO2(g) + O2(g) <==> 2SO3(g), ΔH = -197 kJ mol^-1 and ΔS_system = -188 J K^-1 mol^-1. Above what temperature does this reaction cease to be spontaneous?",
         [("A", "1048 K"),
          ("B", "1.05 K"),
          ("C", "955 K"),
          ("D", "298 K")]),

        ("Which reaction is entropy-driven (spontaneous because ΔS_system is positive and outweighs an unfavourable endothermic ΔH)?",
         [("A", "H2(g) + 1/2 O2(g) —> H2O(l)    ΔH = -286 kJ mol^-1"),
          ("B", "NH4NO3(s) + aq —> NH4+(aq) + NO3-(aq)    ΔH = +25.7 kJ mol^-1"),
          ("C", "CH4(g) + 2O2(g) —> CO2(g) + 2H2O(l)    ΔH = -890 kJ mol^-1"),
          ("D", "2Na(s) + Cl2(g) —> 2NaCl(s)    ΔH = -822 kJ mol^-1")]),

        ("Which factor causes barium chloride, BaCl2, to have a less exothermic lattice energy than magnesium chloride, MgCl2?",
         [("A", "Barium has a higher first ionisation energy than magnesium"),
          ("B", "Ba2+ has a larger ionic radius than Mg2+, resulting in weaker electrostatic attraction to Cl-"),
          ("C", "Barium chloride is more covalent than magnesium chloride"),
          ("D", "Ba2+ has a higher charge density than Mg2+")]),

        # Page 7: Q16, Q17, Q18
        ("The first electron affinity of chlorine is -349 kJ mol^-1, whereas that of bromine is -325 kJ mol^-1. Why is the electron affinity of chlorine more exothermic?",
         [("A", "The incoming electron in chlorine enters a 3p subshell closer to the nucleus than the 4p subshell in bromine"),
          ("B", "Chlorine has a lower nuclear charge than bromine"),
          ("C", "Chlorine has greater electron-electron repulsion than fluorine"),
          ("D", "Bromine is a liquid under standard conditions")]),

        ("When potassium fluoride, KF, is compared to potassium iodide, KI, what is the expected trend in their lattice energies of formation?",
         [("A", "KF is more exothermic than KI because F- is smaller than I-"),
          ("B", "KI is more exothermic than KF because iodide has more electrons"),
          ("C", "Both have identical lattice energies because the cation is K+ in both"),
          ("D", "KI is more exothermic because iodide is more polarisable")]),

        ("A reaction has ΔH = +150 kJ mol^-1 and ΔS_system = -80 J K^-1 mol^-1. Which statement is correct?",
         [("A", "The reaction is feasible above 1875 K"),
          ("B", "The reaction is feasible below 1875 K"),
          ("C", "The reaction is not feasible at any temperature"),
          ("D", "The reaction is feasible at all temperatures")]),

        # Page 8: Q19, Q20, Q21
        ("In a Born-Haber cycle for magnesium oxide, MgO, which of the following represents the correct expression for ΔfH°[MgO(s)]?",
         [("A", "ΔatH[Mg] + 1st IE[Mg] + 2nd IE[Mg] + ΔatH[O] + 1st EA[O] + 2nd EA[O] + ΔLE H[MgO]"),
          ("B", "ΔatH[Mg] + 1st IE[Mg] + ΔatH[O] + 1st EA[O] - ΔLE H[MgO]"),
          ("C", "ΔLE H[MgO] - [ΔatH[Mg] + 1st IE[Mg] + 2nd IE[Mg] + ΔatH[O]]"),
          ("D", "ΔatH[Mg] + 2nd IE[Mg] + ΔatH[O] + 2nd EA[O] + ΔLE H[MgO]")]),

        ("Why is the standard enthalpy of atomisation of magnesium (+148 kJ mol^-1) greater than that of sodium (+107 kJ mol^-1)?",
         [("A", "Magnesium atoms are smaller and contribute 2 delocalised electrons per cation to metallic bonding"),
          ("B", "Magnesium has a higher electronegativity than sodium"),
          ("C", "Magnesium has a lower second ionisation energy than sodium"),
          ("D", "Magnesium has a hexagonal close-packed crystal structure")]),

        ("What happens to the value of ΔS_total as the temperature of an exothermic reaction approaches absolute zero (0 K)?",
         [("A", "ΔS_total approaches zero"),
          ("B", "ΔS_total approaches negative infinity"),
          ("C", "ΔS_surroundings approaches positive infinity, making ΔS_total very large and positive"),
          ("D", "ΔS_total becomes equal to ΔS_system")]),

        # Page 9: Q22, Q23, Q24
        ("Given: 1st EA[O] = -141 kJ mol^-1 and 2nd EA[O] = +798 kJ mol^-1. What is the overall enthalpy change for the process: O(g) + 2e- —> O2-(g)?",
         [("A", "+657 kJ mol^-1"),
          ("B", "-657 kJ mol^-1"),
          ("C", "+939 kJ mol^-1"),
          ("D", "-939 kJ mol^-1")]),

        ("If a chemical reaction has a positive ΔS_total at 298 K, which of the following MUST be true?",
         [("A", "The reaction must be exothermic (ΔH < 0)"),
          ("B", "The reaction must proceed with an increase in entropy of the system (ΔS_system > 0)"),
          ("C", "The reaction is thermodynamically feasible at 298 K"),
          ("D", "The rate of reaction must be extremely rapid at 298 K")]),

        ("For the thermal decomposition of potassium chlorate: 2KClO3(s) —> 2KCl(s) + 3O2(g), ΔH = -78 kJ mol^-1. What are the signs of ΔS_system and ΔS_surroundings at 298 K?",
         [("A", "ΔS_system: Positive (+)  |  ΔS_surroundings: Positive (+)"),
          ("B", "ΔS_system: Positive (+)  |  ΔS_surroundings: Negative (-)"),
          ("C", "ΔS_system: Negative (-)  |  ΔS_surroundings: Positive (+)"),
          ("D", "ΔS_system: Negative (-)  |  ΔS_surroundings: Negative (-)")]),

        # Page 10: Q25, Q26, Q27
        ("Which of the following processes has ΔH = 0 and ΔS_system > 0, making it entirely entropy-driven at all temperatures?",
         [("A", "Evaporation of water"),
          ("B", "Expansion of an ideal gas into an evacuated flask at constant temperature"),
          ("C", "Combustion of propane"),
          ("D", "Dissolution of sodium hydroxide in water")]),

        ("In the Born-Haber cycle for aluminium oxide, Al2O3(s), how many moles of electrons are involved in the electron affinity step?",
         [("A", "2 moles"),
          ("B", "3 moles"),
          ("C", "5 moles"),
          ("D", "6 moles")]),

        ("Which of the following compounds has the highest melting temperature, primarily due to its lattice energy?",
         [("A", "NaF"),
          ("B", "CaO"),
          ("C", "KBr"),
          ("D", "CsI")]),

        # Page 11: Q28, Q29, Q30
        ("When a reaction with ΔH > 0 and ΔS_system > 0 reaches its crossover temperature T_crossover, what is the value of the equilibrium constant K?",
         [("A", "K = 0"),
          ("B", "K = 1"),
          ("C", "K = infinity"),
          ("D", "K = -1")]),

        ("Which species requires the enthalpy of atomisation of a diatomic gas to be multiplied by 1/2 in its Born-Haber cycle?",
         [("A", "Formation of 1 mole of NaCl(s) from Na(s) and Cl2(g)"),
          ("B", "Formation of 1 mole of MgCl2(s) from Mg(s) and Cl2(g)"),
          ("C", "Formation of 1 mole of AlCl3(s) from Al(s) and Cl2(g)"),
          ("D", "Formation of 1 mole of CCl4(l) from C(s) and Cl2(g)")]),

        ("Why does calcium oxide, CaO, adopt an ionic lattice rather than existing as discrete neutral CaO molecules?",
         [("A", "The oxygen atom has a high electronegativity"),
          ("B", "The huge lattice energy released when Ca2+ and O2- pack into a crystal lattice outweighs the endothermic cost of forming Ca2+ and O2- ions"),
          ("C", "The second electron affinity of oxygen is exothermic"),
          ("D", "Calcium metal easily reacts with atmospheric nitrogen")])
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
    # QUESTION 31 (18 MARKS) — BORN-HABER CYCLE FOR MAGNESIUM CHLORIDE
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Magnesium chloride, MgCl<sub>2</sub>, is an ionic compound widely used in the industrial manufacture of magnesium metal by molten electrolysis.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The table below lists thermodynamic data required to construct a Born-Haber cycle for magnesium chloride at 298 K:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Enthalpy Change</b>", S['tbl_th']), Paragraph("<b>Symbol / Process</b>", S['tbl_th']), Paragraph("<b>Value / kJ mol<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("Standard enthalpy of formation of MgCl<sub>2</sub>(s)", S['tbl_td_l']), Paragraph("Δ<i>H</i><sub>f</sub>°[MgCl<sub>2</sub>(s)]", S['tbl_td']), Paragraph("-641.3", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of magnesium", S['tbl_td_l']), Paragraph("Δ<i>H</i><sub>at</sub>°[Mg(s)]", S['tbl_td']), Paragraph("+147.7", S['tbl_td'])],
        [Paragraph("First ionisation energy of magnesium", S['tbl_td_l']), Paragraph("1st IE [Mg]", S['tbl_td']), Paragraph("+737.7", S['tbl_td'])],
        [Paragraph("Second ionisation energy of magnesium", S['tbl_td_l']), Paragraph("2nd IE [Mg]", S['tbl_td']), Paragraph("+1450.7", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of chlorine", S['tbl_td_l']), Paragraph("Δ<i>H</i><sub>at</sub>°[1/2 Cl<sub>2</sub>(g)]", S['tbl_td']), Paragraph("+121.7", S['tbl_td'])],
        [Paragraph("First electron affinity of chlorine", S['tbl_td_l']), Paragraph("1st EA [Cl(g)]", S['tbl_td']), Paragraph("-348.8", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[7.0*cm, 5.0*cm, 3.8*cm])
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t31)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Define standard lattice energy (using the lattice formation convention).", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> In the box below, complete the Born-Haber cycle for magnesium chloride by:<br/>"
                   "• writing chemical species (including state symbols) on each horizontal energy level<br/>"
                   "• labelling each arrow with the appropriate enthalpy term.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(BornHaberCycleBox(AVAIL_W, 7.5*cm, title="Enthalpy / Energy"))
    story.append(PageBreak())

    # Question 31 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the standard lattice energy of formation, Δ<i>H</i><sub>LE</sub>°[MgCl<sub>2</sub>(s)], in kJ mol<sup>-1</sup>. Include a sign in your answer.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>LE</sub>°[MgCl<sub>2</sub>(s)] = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Explain why the standard enthalpy of atomisation of chlorine is exactly half the bond dissociation enthalpy of the Cl-Cl bond in Cl<sub>2</sub>(g).", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> The lattice energy of barium chloride, BaCl<sub>2</sub>, is -2056 kJ mol<sup>-1</sup>.<br/>"
                   "Explain, in terms of ionic properties, why the lattice energy of magnesium chloride is significantly more exothermic than that of barium chloride.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — BORN-HABER CYCLE FOR CALCIUM OXIDE & 2ND ELECTRON AFFINITY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Calcium oxide, CaO(s), is a basic refractory oxide with a very high melting temperature (2613 °C).", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Thermodynamic data for calcium oxide at 298 K are shown below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t32_data = [
        [Paragraph("<b>Enthalpy Change</b>", S['tbl_th']), Paragraph("<b>Value / kJ mol<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("Standard enthalpy of formation of CaO(s)", S['tbl_td_l']), Paragraph("-635.1", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of calcium, Ca(s)", S['tbl_td_l']), Paragraph("+178.2", S['tbl_td'])],
        [Paragraph("First ionisation energy of calcium", S['tbl_td_l']), Paragraph("+589.8", S['tbl_td'])],
        [Paragraph("Second ionisation energy of calcium", S['tbl_td_l']), Paragraph("+1145.4", S['tbl_td'])],
        [Paragraph("Standard enthalpy of atomisation of oxygen, 1/2 O<sub>2</sub>(g)", S['tbl_td_l']), Paragraph("+249.2", S['tbl_td'])],
        [Paragraph("First electron affinity of oxygen, O(g)", S['tbl_td_l']), Paragraph("-141.1", S['tbl_td'])],
        [Paragraph("Second electron affinity of oxygen, O<sup>-</sup>(g)", S['tbl_td_l']), Paragraph("+798.0", S['tbl_td'])],
    ]
    t32 = Table(t32_data, colWidths=[10.5*cm, 5.3*cm])
    t32.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t32)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Write the chemical equation, including state symbols, that represents the second electron affinity of oxygen.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Explain why the first electron affinity of oxygen is exothermic (-141.1 kJ mol<sup>-1</sup>), whereas the second electron affinity is highly endothermic (+798.0 kJ mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the lattice energy of formation of calcium oxide, Δ<i>H</i><sub>LE</sub>°[CaO(s)], in kJ mol<sup>-1</sup>. Include a sign in your answer.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>LE</sub>°[CaO(s)] = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 32 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> The lattice energy of sodium oxide, Na<sub>2</sub>O, is -2488 kJ mol<sup>-1</sup>, which is considerably less exothermic than that of calcium oxide (approx -3400 kJ mol<sup>-1</sup>).<br/>"
                   "Given that Na<sup>+</sup> (0.102 nm) and Ca<sup>2+</sup> (0.100 nm) have almost identical ionic radii, explain why the lattice energy of CaO is roughly 1000 kJ mol<sup>-1</sup> more exothermic than that of Na<sub>2</sub>O.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Despite the formation of O<sup>2-</sup>(g) ions requiring an overall input of +656.9 kJ mol<sup>-1</sup> of energy from neutral O(g) atoms, ionic metal oxides containing O<sup>2-</sup> ions are universally stable solid compounds.<br/>"
                   "Explain this thermodynamic paradox by considering the energetic contribution of the crystal lattice.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — BAKING SODA DECOMPOSITION & CROSSOVER FEASIBILITY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Sodium hydrogencarbonate (baking soda), NaHCO<sub>3</sub>, acts as a leavening agent in baking because it decomposes upon heating to release carbon dioxide gas:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2NaHCO<sub>3</sub>(s) &nbsp;—&gt;&nbsp; Na<sub>2</sub>CO<sub>3</sub>(s) &nbsp;+&nbsp; H<sub>2</sub>O(g) &nbsp;+&nbsp; CO<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +135.6 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Standard molar entropies at 298 K are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t33_data = [
        [Paragraph("<b>Substance</b>", S['tbl_th']), Paragraph("<b>NaHCO<sub>3</sub>(s)</b>", S['tbl_th']), Paragraph("<b>Na<sub>2</sub>CO<sub>3</sub>(s)</b>", S['tbl_th']), Paragraph("<b>H<sub>2</sub>O(g)</b>", S['tbl_th']), Paragraph("<b>CO<sub>2</sub>(g)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("102.1", S['tbl_td']), Paragraph("136.0", S['tbl_td']), Paragraph("188.7", S['tbl_td']), Paragraph("213.6", S['tbl_td'])],
    ]
    t33 = Table(t33_data, colWidths=[3.8*cm] + [3.0*cm]*4)
    t33.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t33)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why the entropy change of the system, Δ<i>S</i>°<sub>system</sub>, is expected to be large and positive for this reaction.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i>°<sub>system</sub> for this reaction in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for the reaction at 298 K (25 °C).<br/>"
                   "Hence explain why baking soda can be stored in an airtight kitchen cupboard for years without decomposing.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 33 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the minimum temperature, in °C, at which the decomposition of sodium hydrogencarbonate becomes thermodynamically feasible.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Minimum temperature = ..................................................................................... °C", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> In the space below, sketch a graph of Δ<i>S</i><sub>total</sub> against temperature <i>T</i> (from 250 K to 500 K) for this decomposition.<br/>"
                   "Clearly label the crossover temperature on the temperature axis and the region where the reaction is feasible.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(AVAIL_W, 6.2*cm, y_label="ΔS_total / J K^-1 mol^-1", x_label="Temperature T / K"))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ASTERISKED (*) LEVEL OF RESPONSE: FORMATION OF MgCl vs MgCl2 vs MgCl3
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*34</b>&nbsp;&nbsp;Magnesium forms the stable divalent ionic halide magnesium chloride, MgCl<sub>2</sub>.<br/>"
                           "Neither magnesium(I) chloride, MgCl, nor magnesium(III) chloride, MgCl<sub>3</sub>, can be isolated as stable compounds under standard conditions.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Theoretical and experimental thermodynamic values are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t34_data = [
        [Paragraph("<b>Compound / Ion</b>", S['tbl_th']), Paragraph("<b>Estimated Lattice Energy / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>Estimated Δ<i>H</i><sub>f</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("MgCl(s)", S['tbl_td_l']), Paragraph("-753", S['tbl_td']), Paragraph("-125", S['tbl_td'])],
        [Paragraph("MgCl<sub>2</sub>(s)", S['tbl_td_l']), Paragraph("-2526", S['tbl_td']), Paragraph("-641", S['tbl_td'])],
        [Paragraph("MgCl<sub>3</sub>(s)", S['tbl_td_l']), Paragraph("-5440", S['tbl_td']), Paragraph("+3920", S['tbl_td'])],
        [Paragraph("Ionisation Energies of Mg: &nbsp;&nbsp; 1st IE = +738 &nbsp;|&nbsp; 2nd IE = +1451 &nbsp;|&nbsp; 3rd IE = +7733 kJ mol<sup>-1</sup>", S['tbl_td_l']), "", ""],
    ]
    t34 = Table(t34_data, colWidths=[5.5*cm, 5.5*cm, 4.8*cm])
    t34.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, 3), LIGHT_BG),
        ('BACKGROUND', (0, 4), (-1, 4), MID_BG),
        ('SPAN', (0, 4), (-1, 4)),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t34)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why the estimated lattice energy of MgCl<sub>2</sub> (-2526 kJ mol<sup>-1</sup>) is more than three times as exothermic as that of MgCl (-753 kJ mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)* Level of Response
    story.append(Table([
        [Paragraph("<b>*(b)</b> Using the thermodynamic data in the table and principles of Born-Haber cycles, explain why magnesium chloride forms as MgCl<sub>2</sub> and NOT as MgCl or MgCl<sub>3</sub>.<br/>"
                   "In your answer, you should include:<br/>"
                   "• an explanation of why MgCl<sub>3</sub> is thermodynamically unstable with respect to its elements, referring to the 3rd ionisation energy of magnesium<br/>"
                   "• an evaluation of why MgCl is thermodynamically unstable, including the calculation of the enthalpy change for the disproportionation reaction:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; 2MgCl(s) —&gt; Mg(s) + MgCl<sub>2</sub>(s)<br/>"
                   "• a deduction of why MgCl<sub>2</sub> is the uniquely stable product.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why the third ionisation energy of magnesium (+7733 kJ mol<sup>-1</sup>) is so drastically greater than the second ionisation energy (+1451 kJ mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> If a chemist attempted to synthesise MgCl(s) at low temperatures where disproportionation is kinetically inhibited, predict whether the compound would be diamagnetic or paramagnetic. Justify your answer using electronic configuration.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — BLAST FURNACE THERMODYNAMICS: REDUCTION OF IRON ORE
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;In the industrial extraction of iron inside a blast furnace, haematite (iron(III) oxide) is reduced by carbon monoxide:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Fe<sub>2</sub>O<sub>3</sub>(s) &nbsp;+&nbsp; 3CO(g) &nbsp;—&gt;&nbsp; 2Fe(s) &nbsp;+&nbsp; 3CO<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -24.8 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Thermodynamic data at 298 K are provided in the table below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t35_data = [
        [Paragraph("<b>Substance</b>", S['tbl_th']), Paragraph("<b>Fe<sub>2</sub>O<sub>3</sub>(s)</b>", S['tbl_th']), Paragraph("<b>CO(g)</b>", S['tbl_th']), Paragraph("<b>Fe(s)</b>", S['tbl_th']), Paragraph("<b>CO<sub>2</sub>(g)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("87.4", S['tbl_td']), Paragraph("197.6", S['tbl_td']), Paragraph("27.3", S['tbl_td']), Paragraph("213.6", S['tbl_td'])],
    ]
    t35 = Table(t35_data, colWidths=[3.8*cm] + [3.0*cm]*4)
    t35.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t35)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, in J K<sup>-1</sup> mol<sup>-1</sup>, for the reduction of iron(III) oxide by carbon monoxide.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for this reaction at 298 K.<br/>"
                   "State whether the reaction is thermodynamically feasible at room temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 35 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> At the base of the blast furnace, temperatures exceed 1800 K (approx 1500 °C).<br/>"
                   "Calculate Δ<i>S</i><sub>total</sub> for the reduction of iron(III) oxide by carbon monoxide at 1800 K, assuming Δ<i>H</i>° and Δ<i>S</i>°<sub>system</sub> are independent of temperature.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (1800 K) = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> At these very high temperatures, iron(III) oxide can also be reduced directly by solid coke (carbon):<br/>"
                   "Fe<sub>2</sub>O<sub>3</sub>(s) &nbsp;+&nbsp; 3C(s) &nbsp;—&gt;&nbsp; 2Fe(s) &nbsp;+&nbsp; 3CO(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +490.7 kJ mol<sup>-1</sup><br/>"
                   "Given that <i>S</i>°[C(s)] = 5.7 J K<sup>-1</sup> mol<sup>-1</sup>, calculate Δ<i>S</i>°<sub>system</sub> for this direct reduction.<br/>"
                   "Hence determine the crossover temperature, in K, above which direct reduction by carbon becomes thermodynamically feasible.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>T</i><sub>crossover</sub> = ..................................................................................... K", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Explain why the direct reduction of iron(III) oxide by carbon has a vastly larger positive Δ<i>S</i>°<sub>system</sub> (+541 J K<sup>-1</sup> mol<sup>-1</sup>) than the reduction by carbon monoxide (+15 J K<sup>-1</sup> mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(35, 18))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # SECTION C: SYNOPTIC CONTEMPORARY CASE STUDIES (QUESTIONS 36 & 37)
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>SECTION C</b>", S['sec_header']))
    story.append(Paragraph("<b>Answer ALL questions. Write your answers in the spaces provided.</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=12, spaceBefore=4))

    # ──────────────────────────────────────────────────────────
    # QUESTION 36 (15 MARKS) — BARIUM CHLORIDE HYDRATE DEHYDRATION THERMODYNAMICS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;Hydrated barium chloride, BaCl<sub>2</sub>·2H<sub>2</sub>O(s), loses its water of crystallisation upon heating:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("BaCl<sub>2</sub>·2H<sub>2</sub>O(s) &nbsp;—&gt;&nbsp; BaCl<sub>2</sub>(s) &nbsp;+&nbsp; 2H<sub>2</sub>O(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Because the direct enthalpy change of dehydration cannot be measured accurately in a school calorimeter, an indirect Hess cycle is constructed using enthalpies of solution:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("BaCl<sub>2</sub>(s) &nbsp;+&nbsp; aq &nbsp;—&gt;&nbsp; BaCl<sub>2</sub>(aq) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>1</sub> = -12.6 kJ mol<sup>-1</sup><br/>"
                           "BaCl<sub>2</sub>·2H<sub>2</sub>O(s) &nbsp;+&nbsp; aq &nbsp;—&gt;&nbsp; BaCl<sub>2</sub>(aq) &nbsp;+&nbsp; 2H<sub>2</sub>O(l) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>2</sub> = +8.8 kJ mol<sup>-1</sup><br/>"
                           "H<sub>2</sub>O(l) &nbsp;—&gt;&nbsp; H<sub>2</sub>O(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>vap</sub> = +40.7 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Construct a Hess's Law cycle linking the reactions above, and calculate the standard enthalpy change of dehydration, Δ<i>H</i>°<sub>dehyd</sub>, for:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; BaCl<sub>2</sub>·2H<sub>2</sub>O(s) —&gt; BaCl<sub>2</sub>(s) + 2H<sub>2</sub>O(g)", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i>°<sub>dehyd</sub> = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Literature values for standard molar entropies at 298 K are:<br/>"
                   "<i>S</i>°[BaCl<sub>2</sub>·2H<sub>2</sub>O(s)] = 203.0 &nbsp;|&nbsp; <i>S</i>°[BaCl<sub>2</sub>(s)] = 123.7 &nbsp;|&nbsp; <i>S</i>°[H<sub>2</sub>O(g)] = 188.7 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>"
                   "Calculate Δ<i>S</i>°<sub>system</sub> for this dehydration in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the dehydration temperature (in °C) at which barium chloride dihydrate begins to lose its water of crystallisation spontaneously into the gas phase (where Δ<i>S</i><sub>total</sub> &gt;= 0).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Dehydration temperature = ..................................................................................... °C", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> In an industrial drying oven operated at 120 °C, the partial pressure of water vapour is 0.20 atm.<br/>"
                   "Explain how reducing the ambient atmospheric pressure inside a vacuum drying oven lowers the temperature needed to completely dehydrate barium chloride crystals.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — TITANIUM EXTRACTION: THE KROLL PROCESS & THERMODYNAMICS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;Titanium is a vital aerospace metal. Unlike iron, titanium cannot be extracted from its mineral rutile, TiO<sub>2</sub>, by direct reduction with carbon because it forms brittle titanium carbide, TiC.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Instead, the Kroll process is employed in two distinct stages:<br/>"
                           "<b>Stage 1:</b> TiO<sub>2</sub>(s) &nbsp;+&nbsp; 2C(s) &nbsp;+&nbsp; 2Cl<sub>2</sub>(g) &nbsp;—&gt;&nbsp; TiCl<sub>4</sub>(l) &nbsp;+&nbsp; 2CO(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (at 900 °C)<br/>"
                           "<b>Stage 2:</b> TiCl<sub>4</sub>(g) &nbsp;+&nbsp; 2Mg(l) &nbsp;—&gt;&nbsp; Ti(s) &nbsp;+&nbsp; 2MgCl<sub>2</sub>(l) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (at 1000 °C under argon)", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t37_data = [
        [Paragraph("<b>Species</b>", S['tbl_th']), Paragraph("<b>TiCl<sub>4</sub>(g)</b>", S['tbl_th']), Paragraph("<b>Mg(l)</b>", S['tbl_th']), Paragraph("<b>Ti(s)</b>", S['tbl_th']), Paragraph("<b>MgCl<sub>2</sub>(l)</b>", S['tbl_th'])],
        [Paragraph("<b>Δ<i>H</i><sub>f</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_td_l']), Paragraph("-763.2", S['tbl_td']), Paragraph("+8.9", S['tbl_td']), Paragraph("0.0", S['tbl_td']), Paragraph("-601.2", S['tbl_td'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_td_l']), Paragraph("354.9", S['tbl_td']), Paragraph("41.8", S['tbl_td']), Paragraph("30.7", S['tbl_td']), Paragraph("128.4", S['tbl_td'])],
    ]
    t37 = Table(t37_data, colWidths=[3.8*cm] + [3.0*cm]*4)
    t37.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t37)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> For Stage 2 of the Kroll process at 1273 K (1000 °C):<br/>"
                   "(i) Calculate the standard enthalpy change of reaction, Δ<i>H</i>°, in kJ mol<sup>-1</sup>.<br/>"
                   "(ii) Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i>° = ................................... kJ mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i>°<sub>system</sub> = ................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 37 Parts (b), (c), (d)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for Stage 2 at 1273 K. Deduce whether this reduction reaction is thermodynamically feasible at 1000 °C.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>surroundings</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why Stage 2 must be carried out under an inert atmosphere of pure argon gas rather than in air.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Titanium is significantly more expensive than iron. Identify two major factors that make the Kroll process an expensive industrial operation, referring to the thermodynamic and operational requirements of the process.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(37, 15))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════
    # DATA SHEET: PERIODIC TABLE & CONSTANTS
    # ══════════════════════════════════════════════════════════
    story.append(Paragraph("<b>DATA SHEET: PERIODIC TABLE OF THE ELEMENTS & PHYSICAL CONSTANTS</b>", S['sec_header']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceAfter=8, spaceBefore=2))

    const_data = [
        [Paragraph("<b>Physical Constant</b>", S['tbl_th']), Paragraph("<b>Symbol</b>", S['tbl_th']), Paragraph("<b>Numerical Value & Units</b>", S['tbl_th'])],
        [Paragraph("Gas constant", S['tbl_td_l']), Paragraph("<i>R</i>", S['tbl_td']), Paragraph("8.314 J mol<sup>-1</sup> K<sup>-1</sup>", S['tbl_td'])],
        [Paragraph("Avogadro constant", S['tbl_td_l']), Paragraph("<i>L</i> or <i>N</i><sub>A</sub>", S['tbl_td']), Paragraph("6.022 × 10<sup>23</sup> mol<sup>-1</sup>", S['tbl_td'])],
        [Paragraph("Ionic product of water (298 K)", S['tbl_td_l']), Paragraph("<i>K</i><sub>w</sub>", S['tbl_td']), Paragraph("1.00 × 10<sup>-14</sup> mol<sup>2</sup> dm<sup>-6</sup>", S['tbl_td'])],
        [Paragraph("Specific heat capacity of water", S['tbl_td_l']), Paragraph("<i>c</i>", S['tbl_td']), Paragraph("4.18 J g<sup>-1</sup> K<sup>-1</sup> = 4.18 kJ kg<sup>-1</sup> K<sup>-1</sup>", S['tbl_td'])],
        [Paragraph("Standard pressure", S['tbl_td_l']), Paragraph("<i>p</i>°", S['tbl_td']), Paragraph("1.00 × 10<sup>5</sup> Pa = 100 kPa = 1.00 bar", S['tbl_td'])],
        [Paragraph("Standard temperature", S['tbl_td_l']), Paragraph("<i>T</i>°", S['tbl_td']), Paragraph("298.15 K = 25.0 °C", S['tbl_td'])],
    ]
    t_const = Table(const_data, colWidths=[6.0*cm, 3.2*cm, 8.0*cm])
    t_const.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_const)
    story.append(Spacer(1, 0.4 * cm))

    # Periodic Table Summary Matrix
    pt_rows = [
        [Paragraph("<b>Group -></b>", S['tbl_th']), Paragraph("<b>1</b>", S['tbl_th']), Paragraph("<b>2</b>", S['tbl_th']), Paragraph("<b>3</b>", S['tbl_th']), Paragraph("<b>4</b>", S['tbl_th']), Paragraph("<b>5</b>", S['tbl_th']), Paragraph("<b>6</b>", S['tbl_th']), Paragraph("<b>7</b>", S['tbl_th']), Paragraph("<b>0 / 8</b>", S['tbl_th'])],
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 5 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Lattice energy of formation is the enthalpy change when 1 mol of ionic solid is formed from gaseous ions: Na+(g) + Cl-(g) -> NaCl(s).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("1st electron affinity is the enthalpy change when 1 mol of electrons is added to 1 mol of gaseous atoms: O(g) + e- -> O-(g).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Second EA is endothermic due to strong electrostatic repulsion between incoming e- and negative O- anion.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Enthalpy of atomisation forms 1 mole of gaseous atoms from the element in standard state: 1/2 Cl2(g) -> Cl(g).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("2nd IE of sodium removes an electron from a stable, inner noble gas shell (2p^6) with high effective nuclear charge.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Feasible when ΔS_total >= 0 => T >= ΔH / ΔS_sys = 90 000 / 250 = 360 K (above 360 K).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_total = ΔS_sys - ΔH/T; as T increases, -ΔH/T decreases, so ΔS_total decreases from high to low.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔLE H = ΔfH - [ΔatH(Na) + IE(Na) + ΔatH(Cl) + EA(Cl)] = -411 - [107 + 496 + 122 - 349] = -411 - 376 = -787 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("MgO contains small Mg2+ and small O2- with high charges (+2 and -2). Lattice energy scales with (q1*q2)/r.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("The final arrow from gaseous ions down to the solid crystal lattice represents lattice energy of formation.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("The lattice energy of MgCl2 (-2526 kJ mol^-1) releases massive energy due to 2+ charge, making disproportionation favourable.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At crossover temperature, ΔS_total = 0, meaning ΔS_surroundings = -ΔS_system.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("T_crossover = ΔH / ΔS_sys = (-197 000) / (-188) = 1047.9 K ≈ 1048 K.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ammonium nitrate dissolving is endothermic (ΔH > 0), yet spontaneous because lattice breakdown increases system entropy immensely.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ba2+ has a much larger ionic radius than Mg2+, reducing electrostatic attraction to chloride ions.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Cl is smaller than Br, so the incoming electron is closer to the nucleus and attracted more strongly.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("F- is significantly smaller than I-, so inter-ionic distance is shorter and lattice energy is more exothermic.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("ΔH > 0 and ΔS_sys < 0: ΔS_surr < 0 and ΔS_sys < 0 => ΔS_total is negative at all temperatures (never feasible).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Standard Hess sum for formation: sum of all upward atomisation/IE/EA steps plus downward lattice energy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Mg2+ has higher charge (+2 vs +1) and smaller ionic radius than Na+, yielding stronger metallic bonding.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("As T -> 0 K, -ΔH/T approaches +infinity for exothermic reactions, making ΔS_total enormously positive.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Overall EA = 1st EA + 2nd EA = -141 + 798 = +657 kJ mol^-1 (net endothermic).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("ΔS_total > 0 is the universal condition for thermodynamic feasibility.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Gas produced (3 mol O2 from 2 mol solid) => ΔS_sys > 0; Exothermic (ΔH < 0) => ΔS_surr > 0.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Free expansion of ideal gas has ΔH = 0 (no intermolecular forces) and ΔS_sys > 0 (greater volume/microstates).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Al2O3 contains 3 O2- ions per formula unit; each O atom gains 2 electrons => total 6 moles of electrons.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("CaO has divalent ions (Ca2+ and O2-) with small radii, producing immense lattice energy and very high melting point.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At crossover temperature, ΔS_total = 0; since ΔS_total = R ln K, ln K = 0 => K = 1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("NaCl contains 1 Cl atom per formula unit, so 1/2 mole of Cl2(g) is atomised: 1/2 Cl2(g) -> Cl(g).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("The huge lattice energy of formation of Ca2+O2- (-3400 kJ mol^-1) easily pays back the endothermic cost of forming Ca2+ and O2-.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Born-Haber Cycle for Magnesium Chloride (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• The enthalpy change when one mole of an ionic crystalline solid [1]<br/>"
         "• is formed from its constituent gaseous ions under standard conditions [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• Correct energy level sequence: Mg(s) + Cl2(g) at datum level, Mg(g) + Cl2(g), Mg+(g) + Cl2(g) + e-, Mg2+(g) + Cl2(g) + 2e- [2]<br/>"
         "• Dissociation/atomisation of chlorine: Mg2+(g) + 2Cl(g) + 2e- [1]<br/>"
         "• Electron affinity step: Mg2+(g) + 2Cl-(g) [1]<br/>"
         "• Downward arrow to MgCl2(s) labeled ΔH_LE° and downward arrow from elements to MgCl2(s) labeled ΔfH° [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Hess expression: ΔfH° = ΔatH°(Mg) + 1st IE(Mg) + 2nd IE(Mg) + 2*ΔatH°(Cl) + 2*1st EA(Cl) + ΔH_LE° [1]<br/>"
         "• -641.3 = +147.7 + 737.7 + 1450.7 + 2(121.7) + 2(-348.8) + ΔH_LE° [1]<br/>"
         "• -641.3 = +2336.1 + 243.4 - 697.6 + ΔH_LE° = +1881.9 + ΔH_LE° [1]<br/>"
         "• ΔH_LE° = -641.3 - 1881.9 = -2523.2 kJ mol^-1 (accept -2523 to -2526 kJ mol^-1) [1].<br/>"
         "<i>Examiner Trap: Omitting the factor of 2 for chlorine atomisation or electron affinity loses 2 marks!</i><br/><br/>"
         "<b>(d) [2 Marks]</b><br/>"
         "• Bond enthalpy represents breaking 1 mole of Cl-Cl bonds to form 2 moles of Cl atoms: Cl2(g) -> 2Cl(g) [1]<br/>"
         "• Standard enthalpy of atomisation is defined as forming 1 mole of gaseous Cl atoms: 1/2 Cl2(g) -> Cl(g) [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Mg2+ has a much smaller ionic radius than Ba2+ (0.072 nm vs 0.135 nm) [1]<br/>"
         "• Both cations possess the same +2 ionic charge [1]<br/>"
         "• Therefore Mg2+ has a much higher charge density than Ba2+ [1]<br/>"
         "• The electrostatic attraction between Mg2+ and Cl- ions is much stronger / shorter inter-ionic distance [1]<br/>"
         "• Since lattice energy is proportional to (q1*q2)/r, MgCl2 has a substantially more exothermic lattice energy [1]."),

        ("Question 32: Calcium Oxide Born-Haber Cycle & 2nd Electron Affinity (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• O-(g) + e- —> O2-(g) [1]<br/>"
         "• Correct state symbols (g) on both oxygen species [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• 1st EA is exothermic because the incoming electron is attracted to the positively charged nucleus of the neutral oxygen atom [1]<br/>"
         "• 2nd EA involves adding a negative electron to an already negatively charged O- anion [1]<br/>"
         "• Strong electrostatic repulsion between like negative charges requires large energy input to force the electron into the orbital [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• ΔfH° = ΔatH(Ca) + 1st IE(Ca) + 2nd IE(Ca) + ΔatH(O) + 1st EA(O) + 2nd EA(O) + ΔH_LE° [1]<br/>"
         "• -635.1 = +178.2 + 589.8 + 1145.4 + 249.2 + (-141.1) + (+798.0) + ΔH_LE° [1]<br/>"
         "• -635.1 = +2819.5 + ΔH_LE° [1]<br/>"
         "• ΔH_LE° = -635.1 - 2819.5 = -3454.6 kJ mol^-1 (accept -3454 to -3455 kJ mol^-1) [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Ca2+ has a +2 charge whereas Na+ has a +1 charge [1]<br/>"
         "• Both have almost identical ionic radii (~0.10 nm), so Ca2+ has double the charge density of Na+ [1]<br/>"
         "• Electrostatic force / lattice energy is proportional to (q_cation * q_anion) [1]<br/>"
         "• In CaO, charges are (+2)(-2) = -4, whereas in Na2O charges are (+1)(-2) = -2, making CaO lattice energy ~1000 kJ mol^-1 more exothermic [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Forming O2-(g) from O(g) requires net endothermic energy (-141.1 + 798.0 = +656.9 kJ mol^-1) [1]<br/>"
         "• Removing 2 electrons from Ca requires +1735.2 kJ mol^-1 of ionisation energy [1]<br/>"
         "• Total endothermic hurdle to create Ca2+(g) and O2-(g) is over +2800 kJ mol^-1 [1]<br/>"
         "• However, the condensation of Ca2+ and O2- into a solid crystal lattice releases -3455 kJ mol^-1 of lattice energy [1]<br/>"
         "• The immense lattice energy easily exceeds the endothermic barrier, making overall formation ΔfH° strongly exothermic (-635 kJ mol^-1) [1]."),

        ("Question 33: Baking Soda Decomposition & Crossover Feasibility (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• 2 moles of solid reactant produce 1 mole of solid and 2 moles of gas (H2O(g) + CO2(g)) [1]<br/>"
         "• Gaseous particles possess much greater disorder / translational freedom / dispersion of energy quanta [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• ΔS°_system = [S°(Na2CO3) + S°(H2O) + S°(CO2)] - 2*S°(NaHCO3) [1]<br/>"
         "• = [136.0 + 188.7 + 213.6] - 2(102.1) = 538.3 - 204.2 [1]<br/>"
         "• = +334.1 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• ΔS_surr = -ΔH / T = -(+135 600 J mol^-1) / 298 K = -455.03 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = +334.1 + (-455.03) = -120.93 J K^-1 mol^-1 [2]<br/>"
         "• Because ΔS_total is negative at 298 K, decomposition is thermodynamically non-feasible / cannot occur spontaneously at room temperature [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Reaction becomes feasible when ΔS_total >= 0 => T_min = ΔH / ΔS_system [1]<br/>"
         "• T_min = 135 600 J mol^-1 / 334.1 J K^-1 mol^-1 = 405.87 K [2]<br/>"
         "• In °C: 405.87 - 273.15 = 132.7 °C ≈ 133 °C [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Graph axes: y-axis labeled ΔS_total, x-axis labeled T / K [1]<br/>"
         "• Curve shape: Starts negative at low T, rises non-linearly (or asymptotically) as T increases [1]<br/>"
         "• Intersection with T-axis at T = 406 K (labeled T_crossover) [1]<br/>"
         "• Region above 406 K clearly labeled 'Feasible (ΔS_total > 0)' [1]<br/>"
         "• Region below 406 K clearly labeled 'Non-feasible (ΔS_total < 0)' [1]."),

        ("Question 34: *Level of Response — MgCl vs MgCl2 vs MgCl3 Stability (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Mg2+ has twice the charge of Mg+ (+2 vs +1) [1]<br/>"
         "• Mg2+ has a smaller ionic radius than Mg+ because the same nuclear charge pulls fewer electrons [1]<br/>"
         "• Lattice energy is directly proportional to charge product and inversely to radius, so (2*1)/r_small >> (1*1)/r_large [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Evaluates all three compounds with thorough thermodynamic reasoning. Calculates disproportionation enthalpy: ΔH = ΔfH(MgCl2) - 2*ΔfH(MgCl) = -641 - 2(-125) = -391 kJ mol^-1 (highly exothermic, so MgCl spontaneously disproportionates). Explains that MgCl3 requires removing a 3rd electron from the 2p core shell (+7733 kJ mol^-1), which cannot be compensated by lattice energy (-5440 kJ mol^-1), resulting in massive positive ΔfH (+3920 kJ mol^-1). Concludes MgCl2 is uniquely stable.<br/>"
         "• Level 2 (3-4 marks): Correctly calculates disproportionation enthalpy with minor slip; explains 3rd IE barrier for MgCl3; basic comparison.<br/>"
         "• Level 1 (1-2 marks): Mentions octet rule or ion charges without quantitative thermodynamic analysis.<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• 1st and 2nd IEs remove outer 3s valence electrons [1]<br/>"
         "• 3rd IE removes an electron from an inner complete 2p subshell (noble gas neon core) [1]<br/>"
         "• The 2p electron is much closer to the nucleus (lower principal quantum number n = 2) [1]<br/>"
         "• Experiences much less shielding from inner shells, so attraction by 12 protons is immense [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• Electronic configuration of Mg atom: 1s^2 2s^2 2p^6 3s^2 [1]<br/>"
         "• Electronic configuration of Mg+ ion in MgCl: 1s^2 2s^2 2p^6 3s^1 [1]<br/>"
         "• Mg+ possesses one unpaired electron in the 3s orbital [1]<br/>"
         "• Substances with unpaired electrons are paramagnetic (attracted into magnetic fields) [1]<br/>"
         "• In contrast, MgCl2 contains Mg2+ (1s^2 2s^2 2p^6) with all paired electrons, which is diamagnetic [1]."),

        ("Question 35: Blast Furnace Thermodynamics: Reduction of Iron Ore (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• ΔS°_system = [2*S°(Fe) + 3*S°(CO2)] - [S°(Fe2O3) + 3*S°(CO)] [1]<br/>"
         "• = [2(27.3) + 3(213.6)] - [87.4 + 3(197.6)] = [54.6 + 640.8] - [87.4 + 592.8] = 695.4 - 680.2 [1]<br/>"
         "• = +15.2 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• ΔS_surr = -(-24 800 J mol^-1) / 298 K = +83.22 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total = +15.2 + 83.22 = +98.42 J K^-1 mol^-1 [1]<br/>"
         "• Since ΔS_total > 0, the reaction is thermodynamically feasible at 298 K [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• At 1800 K: ΔS_surr = -(-24 800) / 1800 = +13.78 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = +15.2 + 13.78 = +28.98 J K^-1 mol^-1 [1]<br/>"
         "• Feasible at 1800 K, but ΔS_total is smaller than at 298 K because reaction is exothermic [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• ΔS°_system = [2*S°(Fe) + 3*S°(CO)] - [S°(Fe2O3) + 3*S°(C)] [1]<br/>"
         "• = [2(27.3) + 3(197.6)] - [87.4 + 3(5.7)] = [54.6 + 592.8] - [87.4 + 17.1] = 647.4 - 104.5 [1]<br/>"
         "• = +542.9 J K^-1 mol^-1 [1]<br/>"
         "• T_crossover = ΔH / ΔS_system = 490 700 J mol^-1 / 542.9 J K^-1 mol^-1 = 903.8 K (approx 631 °C) [2].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• Reduction by CO: 3 moles of gas (CO) produce 3 moles of gas (CO2), so Δn_gas = 0 (small ΔS_sys) [1]<br/>"
         "• Direct reduction by C: 0 moles of gas produce 3 moles of gas (CO) from solid reactants (Δn_gas = +3) [1]<br/>"
         "• Creating 3 moles of gas from purely solid reactants creates an enormous increase in disorder / microstates [1]."),

        ("Question 36: Barium Chloride Dehydration Calorimetry (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• By Hess's Law: ΔH°_dehyd = ΔH2 - ΔH1 + 2*ΔHvap [1]<br/>"
         "• = (+8.8) - (-12.6) + 2(+40.7) [2]<br/>"
         "• = +21.4 + 81.4 = +102.8 kJ mol^-1 [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• ΔS°_system = [S°(BaCl2) + 2*S°(H2O(g))] - S°(BaCl2·2H2O) [1]<br/>"
         "• = [123.7 + 2(188.7)] - 203.0 = [123.7 + 377.4] - 203.0 = 501.1 - 203.0 [1]<br/>"
         "• = +298.1 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Dehydration occurs when ΔS_total >= 0 => T_min = ΔH°_dehyd / ΔS°_system [1]<br/>"
         "• T_min = 102 800 J mol^-1 / 298.1 J K^-1 mol^-1 = 344.85 K [2]<br/>"
         "• In °C: 344.85 - 273.15 = 71.7 °C ≈ 72 °C [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Dehydration produces 2 moles of water gas: BaCl2·2H2O(s) <=> BaCl2(s) + 2H2O(g) [1]<br/>"
         "• Lowering pressure removes water vapour from above the solid / decreases partial pressure of H2O(g) [1]<br/>"
         "• According to Le Chatelier's principle, equilibrium shifts to the side with more moles of gas (to the right) [1]<br/>"
         "• Thermodynamically, water gas at low partial pressure has higher molar entropy, increasing ΔS_system and lowering crossover T [1]."),

        ("Question 37: The Kroll Process for Titanium Extraction (15 Marks)",
         "<b>(a) [5 Marks]</b><br/>"
         "• (i) ΔH° = [ΔfH(Ti) + 2*ΔfH(MgCl2)] - [ΔfH(TiCl4) + 2*ΔfH(Mg)] [1]<br/>"
         "• = [0 + 2(-601.2)] - [-763.2 + 2(8.9)] = -1202.4 - [-763.2 + 17.8] = -1202.4 - (-745.4) [1]<br/>"
         "• = -457.0 kJ mol^-1 [1]<br/>"
         "• (ii) ΔS°_system = [S°(Ti) + 2*S°(MgCl2)] - [S°(TiCl4) + 2*S°(Mg)] = [30.7 + 2(128.4)] - [354.9 + 2(41.8)] [1]<br/>"
         "• = [30.7 + 256.8] - [354.9 + 83.6] = 287.5 - 438.5 = -151.0 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• At 1273 K: ΔS_surr = -(-457 000 J mol^-1) / 1273 K = +359.0 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total = -151.0 + 359.0 = +208.0 J K^-1 mol^-1 [1]<br/>"
         "• Since ΔS_total > 0, the reaction IS thermodynamically feasible at 1000 °C [1].<br/><br/>"
         "<b>(c) [2 Marks]</b><br/>"
         "• Titanium and molten magnesium react vigorously with oxygen and nitrogen in air at 1000 °C to form oxides and nitrides [1]<br/>"
         "• This would ruin the purity and mechanical properties of the titanium metal [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Expensive reagents: Magnesium metal is itself expensive to produce via electrolysis [2]<br/>"
         "• Batch process & high energy costs: Operating at 1000 °C for days under pure argon is a slow batch process requiring immense electrical heating and argon gas [2].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.3 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=6, spaceBefore=2))

    print(f"[2/2] Compiling publication-grade PDF to {OUT_FILE} ...")
    doc.build(story)
    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"[SUCCESS] Week 5 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")


if __name__ == '__main__':
    build_pdf()
