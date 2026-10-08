"""
build_usman_week2_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 2 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 11A.3: Determining Orders of Reaction (Graphical Methods, Initial Rates, Half-Lives)
  - 11A.4: Rate Equations and Mechanisms (Rate-Determining Step, Molecularity, SN1 vs SN2, Pre-equilibria)

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
    "Usman_Edexcel_Chem_U4_Week2_150M_Challenging_Quiz.pdf"
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
        self.canv.setDash(1, 2.5)  # 1pt dot, 2.5pt space
        for i in range(self.num_lines):
            y = (self.num_lines - 1 - i) * self.line_height + 2
            self.canv.line(0, y, self.width, y)
        self.canv.restoreState()


class GraphSketchBox(Flowable):
    """Draws a clean coordinate graph sketch box with labeled axes for student drawings."""
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="[N2O5] / mol dm^-3", x_label="Time / s"):
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

        # Arrowheads
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
    canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 1.0 * cm, "Chemistry Unit 4 - Week 2 Challenge Assessment")

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
        [Paragraph("<b>Paper Reference:</b> WCH14/01/W2-REV", S['edx_meta_b']),
         Paragraph("<b>Time Allowed:</b> 2 hours 30 minutes", S['edx_meta_b'])],
        [Paragraph("<b>Topic Focus:</b> 11A.3 Determining Orders & 11A.4 Reaction Mechanisms", S['edx_meta']),
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
                  "<font color='#a81717'><b>WEEK 2 KINETICS & MECHANISMS MASTERY EXAM</b></font><br/>"
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
        (1, "The decomposition of hydrogen peroxide, 2H2O2(aq) -> 2H2O(l) + O2(g), is first order with respect to H2O2. The half-life of H2O2 is 240 s. What fraction of the original H2O2 remains after 720 s?",
         [('A', "1/3"), ('B', "1/4"), ('C', "1/8"), ('D', "1/16")]),

        (2, "For a second-order reaction with respect to reactant A, what happens to the half-life (t1/2) if the initial concentration of A is tripled?",
         [('A', "The half-life triples (3x)."), ('B', "The half-life decreases to one-third (1/3x)."), ('C', "The half-life decreases to one-ninth (1/9x)."), ('D', "The half-life remains unchanged.")]),

        (3, "Which of the following graphs produces a straight line for a first-order reaction with respect to reactant X?",
         [('A', "[X] against time t"), ('B', "ln[X] against time t"), ('C', "1/[X] against time t"), ('D', "1/[X]^2 against time t")]),

        (4, "For a reaction with rate = k[A]^0, how does the half-life vary with the initial concentration [A]0?",
         [('A', "t1/2 is directly proportional to [A]0."), ('B', "t1/2 is inversely proportional to [A]0."), ('C', "t1/2 is independent of [A]0."), ('D', "t1/2 is proportional to [A]0^2.")]),

        (5, "A plot of 1/[A] against time t for a reaction gives a straight line with a positive slope equal to 0.084 dm^3 mol^-1 s^-1. What is the overall order of the reaction with respect to A?",
         [('A', "Zero order"), ('B', "First order"), ('C', "Second order"), ('D', "Third order")]),

        (6, "The reaction between 2-bromo-2-methylpropane and aqueous sodium hydroxide follows the rate law rate = k[(CH3)3CBr]. What is the rate-determining step?",
         [('A', "Nucleophilic attack of OH- on the central carbon atom."), ('B', "Heterolytic fission of the C-Br bond to form a carbocation intermediate."), ('C', "Proton transfer from the alcohol to form water."), ('D', "Simultaneous bond making and bond breaking in a pentacoordinate transition state.")]),

        (7, "When (R)-2-bromobutane reacts with aqueous hydroxide ions via an SN2 mechanism, what is the stereochemical outcome of the product, butan-2-ol?",
         [('A', "A 50:50 racemic mixture of (R) and (S) enantiomers."), ('B', "100% (S)-butan-2-ol due to complete Walden inversion of configuration."), ('C', "100% (R)-butan-2-ol with full retention of configuration."), ('D', "An optically inactive meso compound.")]),

        (8, "Consider the reaction mechanism:<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 1: NO(g) + Cl2(g) -&gt; NOCl2(g) &nbsp;&nbsp;&nbsp;&nbsp;(Slow)<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 2: NOCl2(g) + NO(g) -&gt; 2NOCl(g) &nbsp;&nbsp;&nbsp;&nbsp;(Fast)<br/>What is the expected rate equation for this mechanism?",
         [('A', "rate = k[NO]^2 [Cl2]"), ('B', "rate = k[NO][Cl2]"), ('C', "rate = k[NOCl2][NO]"), ('D', "rate = k[NO]^2")]),

        (9, "The reaction 2NO(g) + O2(g) -> 2NO2(g) follows the rate law rate = k[NO]^2 [O2]. A proposed mechanism is:<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 1: NO + NO &lt;=&gt; N2O2 &nbsp;&nbsp;&nbsp;&nbsp;(Fast pre-equilibrium, Kc)<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 2: N2O2 + O2 -&gt; 2NO2 &nbsp;&nbsp;&nbsp;&nbsp;(Slow, k2)<br/>What is the molecularity of the rate-determining step (Step 2)?",
         [('A', "Unimolecular"), ('B', "Bimolecular"), ('C', "Termolecular"), ('D', "Zero-molecular")]),

        (10, "In a reaction profile (energy vs reaction coordinate), what feature represents an intermediate in a multi-step mechanism?",
         [('A', "A potential energy maximum."), ('B', "A local potential energy minimum between two transition states."), ('C', "The difference in energy between reactants and products."), ('D', "The highest point on the curve.")]),

        (11, "A reaction has the rate equation rate = k[P][Q]. In which case could this rate equation be consistent with a multi-step mechanism?",
         [('A', "P and Q collide in the slow first step of the mechanism."), ('B', "P decomposes in a slow first step and Q is added in a fast second step."), ('C', "P and Q are both involved in a fast step after the rate-determining step."), ('D', "Two molecules of P react in the rate-determining step.")]),

        (12, "Why are elementary reaction steps involving termolecular collisions (three species colliding simultaneously) exceedingly rare in chemistry?",
         [('A', "Termolecular collisions are strictly forbidden by thermodynamics."), ('B', "The probability of three independent particles colliding simultaneously with correct orientation and sufficient energy is extremely low."), ('C', "Termolecular collisions only occur in solids."), ('D', "Termolecular steps always have zero activation energy.")]),

        (13, "A student determines the initial rate of reaction from a concentration-time curve by drawing a tangent. At which point must the tangent be constructed to obtain the initial rate?",
         [('A', "At t = t1/2"), ('B', "At t = 0"), ('C', "At the point of inflection"), ('D', "At the completion of the reaction")]),

        (14, "For a reaction A -> products, the time taken for [A] to fall from 0.80 to 0.40 mol dm^-3 is 50 s. The time taken for [A] to fall from 0.40 to 0.20 mol dm^-3 is also 50 s. What is the value of the rate constant k?",
         [('A', "0.0139 s^-1"), ('B', "0.0080 s^-1"), ('C', "0.0200 s^-1"), ('D', "0.693 s^-1")]),

        (15, "Consider the reaction between propanone and bromine in acid: CH3COCH3 + Br2 -> CH3COCH2Br + H+ + Br-. The rate equation is rate = k[CH3COCH3][H+]. What is the order of reaction with respect to Br2?",
         [('A', "0"), ('B', "1"), ('C', "2"), ('D', "-1")]),

        (16, "A reaction between species X and Y is investigated. When [X] is kept constant, a plot of rate against [Y] gives a horizontal straight line. What is the order with respect to Y?",
         [('A', "0"), ('B', "1"), ('C', "2"), ('D', "0.5")]),

        (17, "When log10(rate) is plotted against log10[reactant], what information does the gradient of the straight line provide?",
         [('A', "The rate constant k"), ('B', "The activation energy Ea"), ('C', "The order of reaction with respect to that reactant"), ('D', "The half-life of the reaction")]),

        (18, "For a second-order reaction rate = k[A]^2 with k = 0.25 dm^3 mol^-1 s^-1 and [A]0 = 0.50 mol dm^-3, what is the initial half-life?",
         [('A', "2.0 s"), ('B', "4.0 s"), ('C', "8.0 s"), ('D', "1.39 s")]),

        (19, "In an SN1 mechanism for the hydrolysis of a tertiary bromoalkane, what is the geometry of the carbocation intermediate?",
         [('A', "Trigonal bipyramidal"), ('B', "Trigonal planar with bond angles of 120°"), ('C', "Tetrahedral with bond angles of 109.5°"), ('D', "Pyramidal with bond angles of 107°")]),

        (20, "The reaction 2NO2(g) + F2(g) -> 2NO2F(g) has the experimental rate law rate = k[NO2][F2]. Which of the following mechanisms is consistent with this rate law?",
         [('A', "NO2 + F2 -> NO2F + F (Slow); &nbsp; NO2 + F -> NO2F (Fast)"), ('B', "2NO2 -> N2O4 (Fast); &nbsp; N2O4 + F2 -> 2NO2F (Slow)"), ('C', "2NO2 + F2 -> 2NO2F (One-step termolecular)"), ('D', "F2 -> 2F (Slow); &nbsp; NO2 + F -> NO2F (Fast)")]),

        (21, "Why does an SN1 substitution reaction at a chiral carbon centre typically result in a racemic mixture?",
         [('A', "The nucleophile can only attack from the back face."), ('B', "The planar carbocation intermediate can be attacked by the nucleophile with equal probability from either face."), ('C', "The leaving group shields both faces equally."), ('D', "The carbocation undergoes rapid tautomerisation.")]),

        (22, "For the reaction A + B -> C, the rate equation is rate = k[A]^2. If the initial concentration of B is doubled, what happens to the initial rate of reaction?",
         [('A', "Doubles (2x)"), ('B', "Quadruples (4x)"), ('C', "Halves (0.5x)"), ('D', "Remains unchanged")]),

        (23, "A reaction has a rate equation rate = k[A][B]^2. In an experiment, [A] is doubled and [B] is halved. By what factor does the rate change?",
         [('A', "Multiplied by 2"), ('B', "Multiplied by 0.5 (halved)"), ('C', "Multiplied by 4"), ('D', "Unchanged")]),

        (24, "For a first-order reaction A -> B, the initial rate is 0.040 mol dm^-3 s^-1 when [A] = 0.20 mol dm^-3. What is the rate of reaction when [A] has decreased to 0.050 mol dm^-3?",
         [('A', "0.010 mol dm^-3 s^-1"), ('B', "0.020 mol dm^-3 s^-1"), ('C', "0.005 mol dm^-3 s^-1"), ('D', "0.040 mol dm^-3 s^-1")]),

        (25, "In the mechanism:<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 1: A + B &lt;=&gt; C &nbsp;&nbsp;&nbsp;&nbsp;(Fast equilibrium, Kc = [C]/([A][B]))<br/>&nbsp;&nbsp;&nbsp;&nbsp;Step 2: C + D -&gt; E &nbsp;&nbsp;&nbsp;&nbsp;(Slow, k2)<br/>What is the overall rate equation in terms of the original reactants?",
         [('A', "rate = k2[C][D]"), ('B', "rate = k[A][B][D]"), ('C', "rate = k[A][B]"), ('D', "rate = k[C]")]),

        (26, "A student measures the rate of reaction by drawing a tangent to a curve of [A] vs t. If the tangent at t = 20 s has delta[A] = -0.15 mol dm^-3 over delta t = 60 s, what is the rate of reaction at t = 20 s?",
         [('A', "0.0025 mol dm^-3 s^-1"), ('B', "0.0050 mol dm^-3 s^-1"), ('C', "0.0075 mol dm^-3 s^-1"), ('D', "0.15 mol dm^-3 s^-1")]),

        (27, "Which statement about the transition state of an elementary reaction is correct?",
         [('A', "It can be isolated and bottled in the laboratory."), ('B', "It has a lower potential energy than both reactants and products."), ('C', "It is a transient arrangement of atoms at maximum potential energy with partially formed and partially broken bonds."), ('D', "It is identical in structure to a reaction intermediate.")]),

        (28, "The reaction 2A + B -> C follows the rate law rate = k[A]^2 [B]. Which proposed mechanism is INCONSISTENT with this rate law?",
         [('A', "A + A &lt;=&gt; A2 (Fast); &nbsp; A2 + B -&gt; C (Slow)"), ('B', "A + B &lt;=&gt; AB (Fast); &nbsp; AB + A -&gt; C (Slow)"), ('C', "A + B -&gt; AB (Slow); &nbsp; AB + A -&gt; C (Fast)"), ('D', "2A + B -&gt; C (Single termolecular step)")]),

        (29, "For the gas-phase reaction H2 + I2 -> 2HI, the reaction is first order in H2 and first order in I2. What happens to the rate if the pressure of the system is tripled at constant temperature?",
         [('A', "Increases by 3x"), ('B', "Increases by 6x"), ('C', "Increases by 9x"), ('D', "Remains unchanged")]),

        (30, "A first-order reaction has k = 3.5 x 10^-4 s^-1. How long will it take for the concentration of the reactant to decrease to 25% of its initial value?",
         [('A', "990 s"), ('B', "1980 s"), ('C', "3960 s"), ('D', "2857 s")]),
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
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Dinitrogen pentoxide decomposes in tetrachloromethane solvent according to the stoichiometric equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2N<sub>2</sub>O<sub>5</sub>(solv) &nbsp;—&gt;&nbsp; 4NO<sub>2</sub>(solv) &nbsp;+&nbsp; O<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The concentration of N<sub>2</sub>O<sub>5</sub> was measured at 318 K over time. The experimental data are shown below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Time <i>t</i> / s</b>", S['tbl_th']), Paragraph("0", S['tbl_td']), Paragraph("400", S['tbl_td']), Paragraph("800", S['tbl_td']), Paragraph("1200", S['tbl_td']), Paragraph("1600", S['tbl_td']), Paragraph("2000", S['tbl_td']), Paragraph("2400", S['tbl_td']), Paragraph("2800", S['tbl_td'])],
        [Paragraph("<b>[N<sub>2</sub>O<sub>5</sub>] / mol dm<sup>-3</sup></b>", S['tbl_th']), Paragraph("1.000", S['tbl_td']), Paragraph("0.669", S['tbl_td']), Paragraph("0.448", S['tbl_td']), Paragraph("0.300", S['tbl_td']), Paragraph("0.201", S['tbl_td']), Paragraph("0.134", S['tbl_td']), Paragraph("0.090", S['tbl_td']), Paragraph("0.060", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[3.6*cm] + [1.55*cm]*8)
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t31)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a) (i)</b> On the axes below, sketch the concentration-time curve for the decomposition of N<sub>2</sub>O<sub>5</sub>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(AVAIL_W, 6.2*cm, y_label="[N2O5] / mol dm-3", x_label="Time / s"))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Table([
        [Paragraph("<b>(ii)</b> Show that the reaction is first-order with respect to N<sub>2</sub>O<sub>5</sub> by determining two successive half-lives from the data in the table.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "First half-life, <i>t</i><sub>1/2</sub>(1) = .................................................................................................... s<br/>"
        "Second half-life, <i>t</i><sub>1/2</sub>(2) = ................................................................................................ s",
        S['ans_prompt']
    ))
    story.append(PageBreak())

    # Question 31 Parts (b), (c), (d)
    story.append(Table([
        [Paragraph("<b>(b)</b> A student draws a tangent to the curve at <i>t</i> = 0 s. The tangent intersects the concentration axis at 1.000 mol dm<sup>-3</sup> and the time axis at 1440 s. Calculate the initial rate of reaction in mol dm<sup>-3</sup> s<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Initial rate = ......................................................................................................................... mol dm<sup>-3</sup> s<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(c)</b> Using your value for the half-life from (a)(ii), calculate the rate constant, <i>k</i>, at 318 K. Include units in your answer.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>k</i> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Explain why the stoichiometric coefficient of N<sub>2</sub>O<sub>5</sub> in the balanced equation is 2, yet the reaction is only first order with respect to N<sub>2</sub>O<sub>5</sub>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> State the mathematical expression for the gradient of a plot of ln[N<sub>2</sub>O<sub>5</sub>] against time <i>t</i>, and state whether this gradient is positive or negative.", S['q_subpart']),
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
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Nitrogen monoxide reacts with bromine vapour at 273 K according to the equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2NO(g) &nbsp;+&nbsp; Br<sub>2</sub>(g) &nbsp;—&gt;&nbsp; 2NOBr(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Kinetic experiments demonstrate that the reaction is second order with respect to NO and first order with respect to Br<sub>2</sub>:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Rate = <i>k</i> [NO]<sup>2</sup> [Br<sub>2</sub>].", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> A chemist suggests that the reaction occurs via a single termolecular collision between two molecules of NO and one molecule of Br<sub>2</sub>. Explain why termolecular elementary steps are extremely improbable in gas-phase kinetics.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Paragraph("<b>(b)</b> Another chemist proposes Mechanism A:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 1: NO(g) + Br<sub>2</sub>(g) —&gt; NOBr<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;(Slow)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 2: NOBr<sub>2</sub>(g) + NO(g) —&gt; 2NOBr(g) &nbsp;&nbsp;&nbsp;&nbsp;(Fast)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Table([
        [Paragraph("Explain why Mechanism A is completely inconsistent with the experimentally determined rate equation.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Paragraph("<b>(c)</b> A third chemist proposes Mechanism B involving a rapid pre-equilibrium:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 1: NO(g) + Br<sub>2</sub>(g) &lt;=&gt; NOBr<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;(Fast pre-equilibrium, rate constants <i>k</i><sub>1</sub> and <i>k</i><sub>-1</sub>)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 2: NOBr<sub>2</sub>(g) + NO(g) —&gt; 2NOBr(g) &nbsp;&nbsp;&nbsp;&nbsp;(Slow, rate constant <i>k</i><sub>2</sub>)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Table([
        [Paragraph("Derive the overall rate equation from Mechanism B. Show clearly how the concentration of the intermediate NOBr<sub>2</sub> is expressed in terms of the reactants, and relate the observed rate constant <i>k</i> to the elementary constants <i>k</i><sub>1</sub>, <i>k</i><sub>-1</sub>, and <i>k</i><sub>2</sub>.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12, AVAIL_W))
    story.append(PageBreak())

    # Question 32 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> State the molecularity of Step 1 in the forward direction and the molecularity of Step 2 in Mechanism B.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Molecularity of Step 1 = .............................................................................................................<br/>"
        "Molecularity of Step 2 = .............................................................................................................",
        S['ans_prompt']
    ))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> In an experiment at 273 K, the initial concentrations were [NO] = 2.50 × 10<sup>-3</sup> mol dm<sup>-3</sup> and [Br<sub>2</sub>] = 1.20 × 10<sup>-3</sup> mol dm<sup>-3</sup>. The initial rate of formation of NOBr was 1.80 × 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup>.<br/>"
                   "Calculate the rate constant, <i>k</i>, for the consumption of bromine, and state its units.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>k</i> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Halogenoalkanes undergo nucleophilic substitution with aqueous hydroxide ions by two distinct mechanisms, S<sub>N</sub>1 and S<sub>N</sub>2.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> 1-bromobutane reacts with aqueous sodium hydroxide to form butan-1-ol via an S<sub>N</sub>2 mechanism.<br/>"
                   "<b>(i)</b> Write the rate equation for this reaction.<br/>"
                   "<b>(ii)</b> Describe the mechanism of this reaction. In your answer, refer to the attacking nucleophile, the transition state, bond formation/breaking, and explain why the mechanism is classified as 'bimolecular'.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Rate equation = .............................................................................................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> 2-bromo-2-methylpropane reacts with aqueous sodium hydroxide to form 2-methylpropan-2-ol via an S<sub>N</sub>1 mechanism.<br/>"
                   "<b>(i)</b> Write the rate equation for this reaction.<br/>"
                   "<b>(ii)</b> Outline the two elementary steps of this mechanism and identify the rate-determining step.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Rate equation = .............................................................................................................................................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 33 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Optically active (<i>R</i>)-2-bromobutane is hydrolysed by warm aqueous sodium hydroxide.<br/>"
                   "Predict and explain the stereochemical outcome of the product butan-2-ol if the reaction proceeds entirely by an S<sub>N</sub>2 mechanism. Contrast this with the stereochemical outcome if the reaction proceeded via an S<sub>N</sub>1 mechanism.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> In two separate experiments, the concentration of aqueous sodium hydroxide is doubled while the concentration of the halogenoalkane is kept constant.<br/>"
                   "State and explain the effect of doubling [OH<sup>-</sup>] on:<br/>"
                   "<b>(i)</b> The rate of hydrolysis of 1-bromobutane (S<sub>N</sub>2).<br/>"
                   "<b>(ii)</b> The rate of hydrolysis of 2-bromo-2-methylpropane (S<sub>N</sub>1).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Phenolphthalein (P<sup>2-</sup>) is pink in alkaline solution. In strongly alkaline conditions ([OH<sup>-</sup>] &gt; 0.1 mol dm<sup>-3</sup>), it reacts slowly with hydroxide ions to form a colourless carbinol compound (POH<sup>3-</sup>):", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("P<sup>2-</sup>(aq) [pink] &nbsp;+&nbsp; OH<sup>-</sup>(aq) &nbsp;—&gt;&nbsp; POH<sup>3-</sup>(aq) [colourless]", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Rate = <i>k</i> [P<sup>2-</sup>]<sup><i>m</i></sup> [OH<sup>-</sup>]<sup><i>n</i></sup>.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part *(a) - Level of Response
    story.append(Table([
        [Paragraph("<b>*(a) Extended Writing:</b> A chemist wishes to determine the order of reaction, <i>m</i>, with respect to phenolphthalein by graphical analysis of continuous colorimetric data.<br/>"
                   "Compare and evaluate three distinct graphical methods for determining the order <i>m</i> from concentration-time data:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 1:</b> Determining rates from tangents at various concentrations and plotting rate vs [P<sup>2-</sup>].<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 2:</b> Measuring successive half-lives from the concentration-time curve.<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 3:</b> Testing integrated rate law plots (ln[P<sup>2-</sup>] vs <i>t</i> and 1/[P<sup>2-</sup>] vs <i>t</i>).<br/>"
                   "Discuss the advantages, apparatus limitations, and precision of each method.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(14, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (b), (c)
    story.append(Paragraph("<b>(b)</b> In Experiment 1, [OH<sup>-</sup>] is kept in large excess at 0.500 mol dm<sup>-3</sup> while [P<sup>2-</sup>]<sub>0</sub> = 5.00 × 10<sup>-5</sup> mol dm<sup>-3</sup>. The following absorbance data were recorded:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    t34_data = [
        [Paragraph("<b>Time <i>t</i> / s</b>", S['tbl_th']), Paragraph("0", S['tbl_td']), Paragraph("60", S['tbl_td']), Paragraph("120", S['tbl_td']), Paragraph("180", S['tbl_td']), Paragraph("240", S['tbl_td']), Paragraph("300", S['tbl_td'])],
        [Paragraph("<b>Absorbance, <i>A</i></b>", S['tbl_th']), Paragraph("1.200", S['tbl_td']), Paragraph("0.849", S['tbl_td']), Paragraph("0.600", S['tbl_td']), Paragraph("0.424", S['tbl_td']), Paragraph("0.300", S['tbl_td']), Paragraph("0.212", S['tbl_td'])],
        [Paragraph("<b>ln <i>A</i></b>", S['tbl_th']), Paragraph("0.182", S['tbl_td']), Paragraph("-0.164", S['tbl_td']), Paragraph("-0.511", S['tbl_td']), Paragraph("-0.858", S['tbl_td']), Paragraph("-1.204", S['tbl_td']), Paragraph("-1.551", S['tbl_td'])],
    ]
    t34 = Table(t34_data, colWidths=[3.2*cm] + [2.13*cm]*6)
    t34.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t34)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Table([
        [Paragraph("<b>(i)</b> Using the half-life method, show that the reaction is first-order with respect to phenolphthalein (<i>m</i> = 1).<br/>"
                   "<b>(ii)</b> Calculate the pseudo-first-order rate constant, <i>k'</i>, from the gradient of the ln <i>A</i> vs <i>t</i> data.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Half-life = ................................................................................................................................. s<br/>"
        "<i>k'</i> = ................................................................................................................................... s<sup>-1</sup>",
        S['ans_prompt']
    ))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Paragraph("<b>(c)</b> The experiment was repeated at four different concentrations of sodium hydroxide. The apparent pseudo-rate constants <i>k'</i> are tabulated below:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    t34c_data = [
        [Paragraph("<b>[OH<sup>-</sup>] / mol dm<sup>-3</sup></b>", S['tbl_th']), Paragraph("0.100", S['tbl_td']), Paragraph("0.200", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("0.800", S['tbl_td'])],
        [Paragraph("<b><i>k'</i> / 10<sup>-3</sup> s<sup>-1</sup></b>", S['tbl_th']), Paragraph("1.15", S['tbl_td']), Paragraph("2.31", S['tbl_td']), Paragraph("4.62", S['tbl_td']), Paragraph("9.23", S['tbl_td'])],
    ]
    t34c = Table(t34c_data, colWidths=[4.8*cm] + [2.8*cm]*4)
    t34c.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t34c)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Table([
        [Paragraph("Deduce the order of reaction, <i>n</i>, with respect to hydroxide ions. Write the overall rate equation and calculate the true rate constant <i>k</i> with units.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Order with respect to OH<sup>-</sup> = .....................................................................................................<br/>"
        "Rate equation = .............................................................................................................................................................<br/>"
        "<i>k</i> = ..................................................................................... units .....................................................................",
        S['ans_prompt']
    ))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;The decomposition of ozone into oxygen occurs in the stratosphere according to the equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2O<sub>3</sub>(g) &nbsp;—&gt;&nbsp; 3O<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Kinetic investigations establish that the reaction has the unusual empirical rate equation:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Rate = <i>k</i> [O<sub>3</sub>]<sup>2</sup> [O<sub>2</sub>]<sup>-1</sup>.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a) (i)</b> State the overall order of the reaction.<br/>"
                   "<b>(ii)</b> Explain the physical meaning of a negative order of reaction with respect to oxygen.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Overall order = ..............................................................................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Paragraph("<b>(b)</b> The following two-step mechanism is proposed:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 1: O<sub>3</sub>(g) &lt;=&gt; O<sub>2</sub>(g) + O(g) &nbsp;&nbsp;&nbsp;&nbsp;(Fast equilibrium, forward <i>k</i><sub>1</sub>, reverse <i>k</i><sub>-1</sub>)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Step 2: O<sub>3</sub>(g) + O(g) —&gt; 2O<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;(Slow, rate constant <i>k</i><sub>2</sub>)", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Table([
        [Paragraph("Derive the rate equation from this mechanism. Show that it is identical in form to the empirical rate equation, and express the observed rate constant <i>k</i> in terms of <i>k</i><sub>1</sub>, <i>k</i><sub>-1</sub>, and <i>k</i><sub>2</sub>.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(12, AVAIL_W))
    story.append(PageBreak())

    # Question 35 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> At a certain altitude in the stratosphere, [O<sub>3</sub>] = 4.00 × 10<sup>-8</sup> mol dm<sup>-3</sup> and [O<sub>2</sub>] = 8.00 × 10<sup>-6</sup> mol dm<sup>-3</sup>. The rate constant <i>k</i> at this temperature is 5.00 × 10<sup>11</sup> s<sup>-1</sup>.<br/>"
                   "<b>(i)</b> Calculate the rate of decomposition of ozone under these conditions in mol dm<sup>-3</sup> s<sup>-1</sup>.<br/>"
                   "<b>(ii)</b> Calculate the rate of formation of oxygen, d[O<sub>2</sub>]/dt.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Rate of decomposition of O<sub>3</sub> = ........................................................................................ mol dm<sup>-3</sup> s<sup>-1</sup><br/>"
        "d[O<sub>2</sub>]/dt = ....................................................................................................................... mol dm<sup>-3</sup> s<sup>-1</sup>",
        S['ans_prompt']
    ))
    story.append(Spacer(1, 0.35 * cm))

    # Part (d)
    story.append(Table([
        [Paragraph("<b>(d)</b> Chlorine free radicals (Cl<sup>•</sup>) catalytically destroy ozone via a two-step cycle:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;Step 1: Cl<sup>•</sup> + O<sub>3</sub> —&gt; ClO<sup>•</sup> + O<sub>2</sub><br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;Step 2: ClO<sup>•</sup> + O —&gt; Cl<sup>•</sup> + O<sub>2</sub><br/>"
                   "<b>(i)</b> Explain how this catalytic cycle provides an alternative reaction pathway with a lower activation energy.<br/>"
                   "<b>(ii)</b> Why does the chlorine radical not appear in the overall chemical equation?", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
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
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;The fast complexation reaction between iron(III) ions and thiocyanate ions in acidic solution produces an intensely red complex:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Fe<sup>3+</sup>(aq) &nbsp;+&nbsp; SCN<sup>-</sup>(aq) &nbsp;&lt;=&gt;&nbsp; [Fe(SCN)]<sup>2+</sup>(aq) &nbsp;&nbsp;&nbsp;&nbsp;[forward <i>k</i><sub>f</sub>, reverse <i>k</i><sub>r</sub>]", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Because the reaction is complete in less than 200 milliseconds, it is studied using the stopped-flow spectrophotometric technique at 450 nm.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Describe the principles of the stopped-flow technique. Explain how rapid mixing and the stopping syringe allow reactions occurring on the millisecond timescale to be measured spectrophotometrically.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b) - Table
    story.append(Paragraph("<b>(b)</b> In a series of stopped-flow runs at 298 K, [SCN<sup>-</sup>]<sub>0</sub> = 1.00 × 10<sup>-4</sup> mol dm<sup>-3</sup> and [Fe<sup>3+</sup>] was present in large excess. The measured pseudo-first-order rate constants <i>k</i><sub>obs</sub> are given below:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    t36_data = [
        [Paragraph("<b>[Fe<sup>3+</sup>] / 10<sup>-2</sup> mol dm<sup>-3</sup></b>", S['tbl_th']), Paragraph("1.00", S['tbl_td']), Paragraph("2.00", S['tbl_td']), Paragraph("4.00", S['tbl_td']), Paragraph("6.00", S['tbl_td'])],
        [Paragraph("<b><i>k</i><sub>obs</sub> / s<sup>-1</sup></b>", S['tbl_th']), Paragraph("6.10", S['tbl_td']), Paragraph("10.80", S['tbl_td']), Paragraph("20.20", S['tbl_td']), Paragraph("29.60", S['tbl_td'])],
    ]
    t36 = Table(t36_data, colWidths=[4.8*cm] + [2.8*cm]*4)
    t36.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t36)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Table([
        [Paragraph("For this reversible reaction under pseudo-first-order conditions:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<i>k</i><sub>obs</sub> = <i>k</i><sub>f</sub> [Fe<sup>3+</sup>] + <i>k</i><sub>r</sub><br/>"
                   "<b>(i)</b> Determine the value of the forward rate constant, <i>k</i><sub>f</sub>, from the gradient of <i>k</i><sub>obs</sub> against [Fe<sup>3+</sup>], including units.<br/>"
                   "<b>(ii)</b> Determine the reverse rate constant, <i>k</i><sub>r</sub>, from the y-intercept, including units.<br/>"
                   "<b>(iii)</b> Calculate the equilibrium constant, <i>K</i><sub>c</sub> = <i>k</i><sub>f</sub> / <i>k</i><sub>r</sub>, for the complexation.", S['q_subpart']),
         Paragraph("<b>(8)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "<i>k</i><sub>f</sub> = ..................................................................................... units .....................................................................<br/>"
        "<i>k</i><sub>r</sub> = ..................................................................................... units .....................................................................<br/>"
        "<i>K</i><sub>c</sub> = ..................................................................................... units .....................................................................",
        S['ans_prompt']
    ))
    story.append(PageBreak())

    # Question 36 Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> State what optical wavelength filter should be chosen for following the concentration of [Fe(SCN)]<sup>2+</sup> by colorimetry, and justify your choice with reference to complementary colours.", S['q_subpart']),
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
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;Propan-2-ol is oxidised to propanone by acidified potassium dichromate(VI) in aqueous solution:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("3CH<sub>3</sub>CH(OH)CH<sub>3</sub> &nbsp;+&nbsp; Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> &nbsp;+&nbsp; 8H<sup>+</sup> &nbsp;—&gt;&nbsp; 3CH<sub>3</sub>COCH<sub>3</sub> &nbsp;+&nbsp; 2Cr<sup>3+</sup> &nbsp;+&nbsp; 7H<sub>2</sub>O", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The kinetics of this redox reaction were studied at 298 K using continuous colorimetry.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain how colorimetry can monitor the progress of this reaction. State the colour change observed and specify which absorbing species can be followed.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b) - Table
    story.append(Paragraph("<b>(b)</b> The following initial rate data were obtained at 298 K:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    t37_data = [
        [Paragraph("<b>Exp</b>", S['tbl_th']), Paragraph("<b>[propan-2-ol] / M</b>", S['tbl_th']), Paragraph("<b>[Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>] / M</b>", S['tbl_th']), Paragraph("<b>[H<sup>+</sup>] / M</b>", S['tbl_th']), Paragraph("<b>Initial Rate / 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("1", S['tbl_td']), Paragraph("0.200", S['tbl_td']), Paragraph("0.0100", S['tbl_td']), Paragraph("0.500", S['tbl_td']), Paragraph("1.60", S['tbl_td'])],
        [Paragraph("2", S['tbl_td']), Paragraph("0.400", S['tbl_td']), Paragraph("0.0100", S['tbl_td']), Paragraph("0.500", S['tbl_td']), Paragraph("3.20", S['tbl_td'])],
        [Paragraph("3", S['tbl_td']), Paragraph("0.200", S['tbl_td']), Paragraph("0.0200", S['tbl_td']), Paragraph("0.500", S['tbl_td']), Paragraph("3.20", S['tbl_td'])],
        [Paragraph("4", S['tbl_td']), Paragraph("0.200", S['tbl_td']), Paragraph("0.0100", S['tbl_td']), Paragraph("1.000", S['tbl_td']), Paragraph("6.40", S['tbl_td'])],
    ]
    t37 = Table(t37_data, colWidths=[1.8*cm, 3.8*cm, 3.4*cm, 3.0*cm, 4.0*cm])
    t37.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t37)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Table([
        [Paragraph("Deduce the order of reaction with respect to propan-2-ol, dichromate(VI), and hydrogen ions. Write the rate equation and calculate the rate constant <i>k</i> with units.", S['q_subpart']),
         Paragraph("<b>(8)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph(
        "Order with respect to propan-2-ol = ............................................................................................<br/>"
        "Order with respect to Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> = ................................................................................................<br/>"
        "Order with respect to H<sup>+</sup> = ...................................................................................................................<br/>"
        "Rate equation = .............................................................................................................................................................<br/>"
        "<i>k</i> = ..................................................................................... units .....................................................................",
        S['ans_prompt']
    ))
    story.append(PageBreak())

    # Question 37 Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> When the reaction is carried out with deuterated propan-2-ol, (CH<sub>3</sub>)<sub>2</sub>CD(OH), the initial rate decreases by a factor of 6.7 (primary kinetic isotope effect).<br/>"
                   "Explain what this observation reveals about the bond broken in the rate-determining step of the mechanism.", S['q_subpart']),
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
        [Paragraph("First-order half-life relationship", S['tbl_td_l']), Paragraph("<i>t</i><sub>1/2</sub>", S['tbl_td']), Paragraph("<i>t</i><sub>1/2</sub> = ln 2 / <i>k</i> = 0.693 / <i>k</i>", S['tbl_td'])],
        [Paragraph("Second-order half-life relationship", S['tbl_td_l']), Paragraph("<i>t</i><sub>1/2</sub>", S['tbl_td']), Paragraph("<i>t</i><sub>1/2</sub> = 1 / (<i>k</i> [A]<sub>0</sub>)", S['tbl_td'])],
        [Paragraph("Integrated first-order rate equation", S['tbl_td_l']), Paragraph("ln[A]", S['tbl_td']), Paragraph("ln[A]<sub><i>t</i></sub> = -<i>k t</i> + ln[A]<sub>0</sub>", S['tbl_td'])],
        [Paragraph("Integrated second-order rate equation", S['tbl_td_l']), Paragraph("1/[A]", S['tbl_td']), Paragraph("1/[A]<sub><i>t</i></sub> = <i>k t</i> + 1/[A]<sub>0</sub>", S['tbl_td'])],
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
        ("Q1", "C", "720 s represents exactly 3 half-lives (720 / 240 = 3). Fraction remaining = (1/2)^3 = 1/8. (1)"),
        ("Q2", "B", "For second order, t1/2 = 1 / (k[A]0). Tripling initial concentration divides the half-life by 3 (1/3x). (1)"),
        ("Q3", "B", "Integrated first-order rate law: ln[X] = -kt + ln[X]0; a plot of ln[X] vs t yields a straight line with slope -k. (1)"),
        ("Q4", "A", "For zero order, rate = -d[A]/dt = k => [A]t = -kt + [A]0. At half-life, [A] = [A]0/2 => t1/2 = [A]0 / (2k). Directly proportional to [A]0. (1)"),
        ("Q5", "C", "Integrated second order: 1/[A] = kt + 1/[A]0; linear 1/[A] vs t plot confirms second order with slope = k. (1)"),
        ("Q6", "B", "SN1 is unimolecular; the rate-determining step is slow heterolytic bond fission of C-Br forming a stable tertiary carbocation. (1)"),
        ("Q7", "B", "SN2 occurs via backside attack of OH- opposite the departing Br-, causing complete inversion of configuration (Walden inversion). (1)"),
        ("Q8", "B", "Step 1 is the slow rate-determining step, so rate depends only on the reactants in Step 1: rate = k[NO][Cl2]. (1)"),
        ("Q9", "B", "Step 2 involves the collision of two particles (N2O2 and O2), so its molecularity is bimolecular (molecularity = 2). (1)"),
        ("Q10", "B", "An intermediate is a real chemical species located at a local potential energy minimum between two transition state activation energy peaks. (1)"),
        ("Q11", "A", "If rate = k[P][Q], the rate-determining step must involve one molecule of P and one molecule of Q colliding. (1)"),
        ("Q12", "B", "The simultaneous collision of three particles with proper orientation and sufficient kinetic energy has negligible statistical probability. (1)"),
        ("Q13", "B", "Initial rate is determined by drawing a tangent at time t = 0 s. (1)"),
        ("Q14", "A", "Constant half-life of 50 s confirms first-order kinetics. k = ln 2 / t1/2 = 0.693 / 50 = 0.0139 s^-1. (1)"),
        ("Q15", "A", "Bromine does not appear in the rate equation, so the reaction is zero order with respect to Br2 (involved after the RDS). (1)"),
        ("Q16", "A", "A horizontal rate vs [Y] line means rate does not change when [Y] varies => zero order in Y. (1)"),
        ("Q17", "C", "log10(rate) = log10(k) + n log10[reactant]; gradient = n (the order of reaction). (1)"),
        ("Q18", "C", "For second order, t1/2 = 1 / (k[A]0) = 1 / (0.25 * 0.50) = 1 / 0.125 = 8.0 s. (1)"),
        ("Q19", "B", "A carbocation has 3 bonding pairs and zero lone pairs on carbon (sp2 hybridised), adopting a trigonal planar geometry with 120° bond angles. (1)"),
        ("Q20", "A", "In mechanism A, the slow step is bimolecular with one NO2 and one F2, giving rate = k[NO2][F2], matching experimental observation. (1)"),
        ("Q21", "B", "The intermediate carbocation is planar; the nucleophile has an equal 50% probability of attacking from the front or back face, yielding a racemate. (1)"),
        ("Q22", "D", "Rate equation is rate = k[A]^2; reactant B is zero order, so doubling [B] has no effect on the rate. (1)"),
        ("Q23", "B", "New rate proportional to [2A] * [0.5 B]^2 = 2 * 0.25 = 0.5 (the initial rate halves). (1)"),
        ("Q24", "A", "For first order, rate is directly proportional to [A]. When [A] drops by 4x (0.20 -> 0.050), rate drops by 4x: 0.040 / 4 = 0.010 mol dm^-3 s^-1. (1)"),
        ("Q25", "B", "From pre-equilibrium, [C] = Kc[A][B]. Rate = k2[C][D] = k2 Kc [A][B][D] = k[A][B][D]. (1)"),
        ("Q26", "A", "Rate = -gradient = -(-0.15 mol dm^-3 / 60 s) = +0.0025 mol dm^-3 s^-1. (1)"),
        ("Q27", "C", "A transition state is an activated complex at maximum potential energy with partial bonds that cannot be isolated. (1)"),
        ("Q28", "C", "If Step 1 (A + B -> AB) were slow, the rate law would be rate = k[A][B], which contradicts the experimental second order in A. (1)"),
        ("Q29", "C", "Tripling pressure triples all gas concentrations: new rate = k(3[H2])(3[I2]) = 9x original rate. (1)"),
        ("Q30", "C", "For [A] to fall to 25% requires two half-lives (100% -> 50% -> 25%). t1/2 = ln 2 / (3.5x10^-4) = 1980 s. Two half-lives = 2 * 1980 = 3960 s. (1)")
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
        ("QUESTION 31: Graphical Kinetics of N2O5 Decomposition (18 Marks)", [
            ("(a) Graph Sketch & Half-Lives", "(i) Smooth curve starting at (0, 1.000) showing exponential decay approaching zero asymptotically (2).\n(ii) First half-life: [N2O5] falls from 1.000 to 0.500 mol dm^-3 at t approx 690 s (t1/2(1) = 690 s) (2).\nSecond half-life: falls from 0.500 to 0.250 mol dm^-3 at t approx 1380 s (t1/2(2) = 1380 - 690 = 690 s) (1).\nSuccessive half-lives are constant within experimental error, confirming first-order kinetics (1).", 6),
            ("(b) Initial Rate from Tangent", "Initial rate = -gradient at t = 0 s = -(0 - 1.000) / (1440 - 0) (2).\n= 6.94 x 10^-4 mol dm^-3 s^-1 (1).", 3),
            ("(c) Rate Constant k", "k = ln 2 / t1/2 = 0.693 / 690 s = 1.00 x 10^-3 (or 1.01 x 10^-3) (2).\nUnits: s^-1 (1).", 3),
            ("(d) Stoichiometry vs Order", "Reaction is multi-step; the rate-determining step involves only one molecule of N2O5 undergoing unimolecular fission (N2O5 -> NO2 + NO3) (2).\nStoichiometric coefficients represent overall mole balance and do not indicate reaction order or mechanism (1).", 3),
            ("(e) ln[N2O5] Plot Gradient", "Integrated first-order law: ln[N2O5]t = -k t + ln[N2O5]0 (1).\nGradient = -k (1).\nGradient is negative because reactant concentration decreases over time (1).", 3),
        ]),

        ("QUESTION 32: Rate Laws and Reaction Mechanisms (18 Marks)", [
            ("(a) Improbability of Termolecular Step", "Simultaneous collision of three particles requires all three to be in the same spatial volume at the same instant (1).\nAll three particles must have kinetic energy >= Ea and correct molecular collision orientations (1).\nStatistical probability of this is negligible compared to successive bimolecular collisions (1).", 3),
            ("(b) Inconsistency of Mechanism A", "If Step 1 were rate-determining, the rate equation would be rate = k[NO][Br2] (2).\nThis is first order in NO, which directly contradicts the experimental second-order dependence in NO (1).", 3),
            ("(c) Derivation from Mechanism B", "Step 2 is the slow RDS: Rate = k2 [NOBr2][NO] (1).\nFrom fast pre-equilibrium Step 1: rate_forward = rate_reverse => k1 [NO][Br2] = k-1 [NOBr2] (2).\nExpress intermediate: [NOBr2] = (k1 / k-1) [NO][Br2] = Kc [NO][Br2] (1).\nSubstitute into rate equation: Rate = k2 (k1 / k-1) [NO][Br2] [NO] = (k2 k1 / k-1) [NO]^2 [Br2] (1).\nMatches experimental rate law with k = (k2 k1 / k-1) (1).", 6),
            ("(d) Molecularity of Steps", "Step 1 forward molecularity: Bimolecular (two molecules: NO and Br2) (1).\nStep 2 molecularity: Bimolecular (two molecules: NOBr2 and NO) (1).", 2),
            ("(e) Calculation of Rate Constant", "Rate of consumption of Br2 = 0.5 * rate of formation of NOBr = 0.5 * (1.80 x 10^-5) = 9.00 x 10^-6 mol dm^-3 s^-1 (1).\nk = Rate / ([NO]^2 [Br2]) = 9.00 x 10^-6 / ((2.50 x 10^-3)^2 * (1.20 x 10^-3)) (1).\n= 9.00 x 10^-6 / 7.50 x 10^-9 = 1.20 x 10^3 (or 1200) (1).\nUnits: dm^6 mol^-2 s^-1 (1).", 4),
        ]),

        ("QUESTION 33: Kinetics & Stereochemistry of Halogenoalkanes (18 Marks)", [
            ("(a) SN2 Mechanism & Rate", "(i) Rate = k[1-bromobutane][OH-] (1).\n(ii) OH- nucleophile attacks carbon bonded to Br from the back (opposite to Br) (1).\nForms a single pentacoordinate transition state with partially formed C-OH bond and partially broken C-Br bond (2).\nClassified as bimolecular because two species (halogenoalkane and hydroxide) are involved in the single rate-determining step (2).", 6),
            ("(b) SN1 Mechanism & Rate", "(i) Rate = k[2-bromo-2-methylpropane] (1).\n(ii) Step 1: Slow heterolytic fission of C-Br bond to form planar (CH3)3C+ carbocation and Br- (RDS) (2).\nStep 2: Fast attack of OH- nucleophile on carbocation to form alcohol (1).", 4),
            ("(c) Stereochemical Outcomes", "SN2 mechanism on (R)-2-bromobutane gives complete inversion of configuration (Walden inversion) yielding 100% (S)-butan-2-ol, maintaining optical activity (2).\nIn an SN1 mechanism, the planar carbocation intermediate can be attacked from either face with equal probability (50% front, 50% back) (2).\nThis yields an equimolar (50:50) racemic mixture of enantiomers, resulting in complete loss of optical activity (optically inactive) (1).", 5),
            ("(d) Effect of Doubling [OH-]", "(i) 1-bromobutane (SN2): Rate doubles because the reaction is first order with respect to OH- (1.5).\n(ii) 2-bromo-2-methylpropane (SN1): Rate remains unchanged because the reaction is zero order with respect to OH- (OH- is involved only in the fast step after the RDS) (1.5).", 3),
        ]),

        ("QUESTION 34: Phenolphthalein Kinetics & Integrated Laws (18 Marks)", [
            ("*(a) Level of Response Evaluation", "Level 3 (5-6 marks): Comprehensive comparative evaluation addressing all 3 methods with clear links to experimental precision:\n(1) Tangent method: Direct determination of instantaneous rates, but drawing tangents by hand has high subjective error and tangent errors propagate when plotting rate vs conc.\n(2) Half-life method: Fast and non-mathematical; constancy of t1/2 uniquely identifies 1st order, but requires following the reaction across at least 2 full half-lives, and background absorbance drift can distort V_inf.\n(3) Integrated plots: Most rigorous; linear regression of ln A vs t (1st order) vs 1/A vs t (2nd order) uses all data points simultaneously, minimizing random scatter and identifying subtle deviations.\nLevel 2 (3-4 marks): Discusses 2-3 methods with valid points.\nLevel 1 (1-2 marks): Superficial description of one or two methods.", 6),
            ("(b) Half-Life & Pseudo-Rate Constant", "(i) A falls from 1.200 to 0.600 in 120 s (t1/2(1) = 120 s); falls from 0.600 to 0.300 in 120 s (240 - 120 = 120 s) (2).\nConstant half-life proves reaction is first order in phenolphthalein (1).\n(ii) Gradient of ln A vs t = (-1.551 - 0.182) / (300 - 0) = -1.733 / 300 = -5.78 x 10^-3 s^-1 (2).\nk' = -gradient = 5.78 x 10^-3 s^-1 (1).", 6),
            ("(c) Order in OH- and True k", "Doubling [OH-] (0.100 -> 0.200 -> 0.400 -> 0.800) causes k' to double consecutively (1.15 -> 2.31 -> 4.62 -> 9.23 x 10^-3) (2).\nTherefore, order n = 1 with respect to OH- (1).\nOverall rate equation: Rate = k[P^2-][OH-] (1).\nk = k' / [OH-] = (1.15 x 10^-3) / 0.100 = 0.0115 (or 1.15 x 10^-2) (1).\nUnits: dm^3 mol^-1 s^-1 (1).", 6),
        ]),

        ("QUESTION 35: Ozone Decomposition & Catalytic Cycles (18 Marks)", [
            ("(a) Negative Order Meaning", "(i) Overall order = 2 + (-1) = 1 (first order overall) (1).\n(ii) A negative order means that increasing the concentration of oxygen retards / slows down the rate of decomposition (1).\nOxygen acts as an inhibitor because it shifts the pre-equilibrium step backwards (1).", 3),
            ("(b) Derivation of Rate Law", "Step 2 is slow RDS: Rate = k2 [O3][O] (1).\nStep 1 fast equilibrium: k1 [O3] = k-1 [O2][O] (2).\nSolve for intermediate oxygen atom concentration: [O] = (k1 / k-1) [O3] / [O2] (1).\nSubstitute [O] into rate equation: Rate = k2 ((k1 / k-1) [O3] / [O2]) [O3] (1).\nRate = (k2 k1 / k-1) [O3]^2 [O2]^-1 = k [O3]^2 [O2]^-1 with k = (k2 k1 / k-1) (1).", 6),
            ("(c) Numerical Rate Calculations", "(i) Rate = (5.00 x 10^11) * (4.00 x 10^-8)^2 / (8.00 x 10^-6) (1).\n= (5.00 x 10^11) * (1.60 x 10^-15) / (8.00 x 10^-6) = 1.00 x 10^-7 mol dm^-3 s^-1 (1).\n(ii) Stoichiometric ratio: 2 moles O3 consumed produces 3 moles O2 (1).\nd[O2]/dt = (3/2) * rate of O3 decomposition = 1.5 * (1.00 x 10^-7) = 1.50 x 10^-7 mol dm^-3 s^-1 (1).", 4),
            ("(d) Catalytic Destruction by Cl Radical", "(i) Alternate two-step mechanism replaces high activation energy O3 + O collision with two lower activation energy radical steps (2).\nChlorine radicals react rapidly with O3 to form ClO, which reacts rapidly with O atoms to regenerate Cl (1).\n(ii) Cl radical is consumed in Step 1 and regenerated in Step 2; it acts as a homogeneous catalyst and cancels out of the overall reaction (2).", 5),
        ]),

        ("QUESTION 36: Stopped-Flow Kinetics of Fe3+ and SCN- (15 Marks)", [
            ("(a) Stopped-Flow Technique", "Pneumatic drive syringes rapidly force reactant solutions through a high-efficiency mixing chamber into an optical flow cell (2).\nFlow is stopped abruptly by a stopping syringe pushing against a mechanical limit switch, triggering spectrophotometric recording (1).\nAllows dead time to be reduced to < 2 milliseconds, capturing rapid initial kinetics before equilibrium is established (1).", 4),
            ("(b) Determination of kf, kr and Kc", "(i) k_obs = kf [Fe3+] + kr is a straight line y = mx + c with slope = kf and intercept = kr (1).\nSlope kf = (29.60 - 6.10) / (0.0600 - 0.0100) = 23.50 / 0.0500 = 470 dm^3 mol^-1 s^-1 (2).\nUnits: dm^3 mol^-1 s^-1 (1).\n(ii) y-intercept kr = 6.10 - (470 * 0.0100) = 6.10 - 4.70 = 1.40 s^-1 (2).\nUnits: s^-1 (1).\n(iii) Kc = kf / kr = 470 / 1.40 = 336 (or 335.7) dm^3 mol^-1 (1).", 8),
            ("(c) Colorimetry Filter Selection", "Complementary filter: Blue filter (wavelength 440-470 nm) (1).\nThe [Fe(SCN)]2+ complex is blood-red because it absorbs complementary blue light strongly (1).\nA blue filter ensures maximum absorbance change per mole of complex formed, maximizing signal sensitivity (1).", 3),
        ]),

        ("QUESTION 37: Kinetics of Alcohol Oxidation by Cr2O7^2- (15 Marks)", [
            ("(a) Colorimetric Monitoring", "Orange dichromate(VI) ions (Cr2O7^2-) are reduced to green chromium(III) ions (Cr3+) (1).\nAbsorbance can be monitored at 440 nm (decrease in orange Cr2O7^2-) or at 630 nm (increase in green Cr3+) (1).\nContinuous monitoring records absorbance without withdrawing or quenching aliquots (1).", 3),
            ("(b) Order Deductions, Rate Law & k", "Compare Exp 1 & 2: [Cr2O7^2-] and [H+] constant; [propan-2-ol] doubles, rate doubles => Order in propan-2-ol = 1 (1.5).\nCompare Exp 1 & 3: [propan-2-ol] and [H+] constant; [Cr2O7^2-] doubles, rate doubles => Order in Cr2O7^2- = 1 (1.5).\nCompare Exp 1 & 4: [propan-2-ol] and [Cr2O7^2-] constant; [H+] doubles (0.500 -> 1.000), rate quadruples (1.60 -> 6.40) => Order in H+ = 2 (2).\nRate equation: Rate = k[CH3CH(OH)CH3][Cr2O7^2-][H+]^2 (1).\nk = Rate / ([propan-2-ol][Cr2O7^2-][H+]^2) = 1.60 x 10^-5 / (0.200 * 0.0100 * 0.500^2) (1).\n= 1.60 x 10^-5 / (5.00 x 10^-4) = 0.0320 (or 3.20 x 10^-2) (1).\nUnits: (mol dm^-3 s^-1) / (mol dm^-3)^4 = dm^9 mol^-3 s^-1 (1).", 8),
            ("(c) Kinetic Isotope Effect Interpretation", "The large rate decrease (6.7-fold slower) when C-H is replaced by C-D indicates a primary kinetic isotope effect (2).\nDeuterium is heavier than protium, so the C-D bond has a lower zero-point energy and higher bond dissociation energy (1).\nThis proves conclusively that the C-H bond of the secondary alcohol carbon is cleaved in the slow rate-determining step of the mechanism (1).", 4),
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

    print("[1/2] Building authentic Edexcel past-paper story for Week 2 (150 Marks)...")
    story = build_exam_story()

    print(f"[2/2] Compiling publication-grade PDF to {OUT_FILE} ...")
    doc.build(story)

    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"[SUCCESS] Week 2 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")
    return OUT_FILE


if __name__ == "__main__":
    compile_quiz_pdf()
