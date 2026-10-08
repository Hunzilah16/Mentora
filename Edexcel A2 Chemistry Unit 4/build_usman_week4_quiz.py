"""
build_usman_week4_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 4 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - Topic 11 Synoptic Kinetics Synthesis (Rate Equations, Mechanisms, Activation Energy & Arrhenius)
  - 12A.1: Introduction to Entropy (S, Units, States of Matter, Delta S_system = Sigma S_prod - Sigma S_react)
  - 12A.2: Total Entropy (Delta S_surroundings = -Delta H / T, Delta S_total = Delta S_sys + Delta S_surr, Feasibility Delta S_total > 0)

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
    "Usman_Edexcel_Chem_U4_Week4_150M_Challenging_Quiz.pdf"
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 4 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 4 (150 Marks)...")
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
                   "<b>[  0  ][  0  ][  4  ][  4  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W04</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 4 ASSESSMENT: TOPIC 11 SYNOPTIC & TOPIC 12A ENTROPY</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 4 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 11 Kinetics Grand Synthesis (11A.1-11A.6)<br/>Topic 12A.1: Introduction to Entropy (S, Disorder, Molar Entropies)<br/>Topic 12A.2: Total Entropy (Surroundings, Feasibility Criteria)", S['edx_meta'])],
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
        # Page 2: Q1, Q2, Q3
        ("Which of the following represents the correct SI units for standard molar entropy, S°?",
         [("A", "kJ mol^-1"),
          ("B", "J K^-1"),
          ("C", "J mol^-1 K^-1"),
          ("D", "kJ mol^-1 K^-1")]),

        ("Which substance has the highest standard molar entropy at 298 K?",
         [("A", "Diamond, C(s)"),
          ("B", "Liquid water, H2O(l)"),
          ("C", "Graphite, C(s)"),
          ("D", "Steam, H2O(g)")]),

        ("Consider the reaction: N2O4(g) —> 2NO2(g). Which statement correctly predicts and explains the sign of ΔS_system?",
         [("A", "Positive, because one mole of gas reactant produces two moles of gas products, increasing disorder"),
          ("B", "Negative, because heat is absorbed during the endothermic bond dissociation"),
          ("C", "Positive, because nitrogen dioxide is a brown gas with higher kinetic energy"),
          ("D", "Negative, because the total number of nitrogen atoms remains constant")]),

        # Page 3: Q4, Q5, Q6
        ("For the industrial synthesis of ammonia: N2(g) + 3H2(g) —> 2NH3(g), what is the sign of ΔS_system and the physical rationale?",
         [("A", "Positive, because ammonia molecules are polar and possess dipole-dipole interactions"),
          ("B", "Negative, because 4 moles of gaseous reactants form 2 moles of gaseous product"),
          ("C", "Positive, because energy is released to the surroundings during this exothermic reaction"),
          ("D", "Zero, because all reacting species and products remain in the gas phase")]),

        ("When solid magnesium sulfate, MgSO4(s), dissolves in water, the entropy change of the system, ΔS_system, is unexpectedly negative. What is the most plausible explanation for this observation?",
         [("A", "Dissolving an ionic solid always decreases the entropy of the system"),
          ("B", "The hydration of Mg2+ and SO4^2- ions causes a high degree of ordering of surrounding water molecules"),
          ("C", "The magnesium sulfate precipitates out of solution as an insoluble hydrate"),
          ("D", "The lattice enthalpy of magnesium sulfate is greater than its enthalpy of hydration")]),

        ("Given standard molar entropies at 298 K:\nS°[CaCO3(s)] = 92.9 J K^-1 mol^-1, S°[CaO(s)] = 38.2 J K^-1 mol^-1, S°[CO2(g)] = 213.6 J K^-1 mol^-1.\nWhat is the value of ΔS°_system for the thermal decomposition: CaCO3(s) —> CaO(s) + CO2(g)?",
         [("A", "-158.9 J K^-1 mol^-1"),
          ("B", "+158.9 J K^-1 mol^-1"),
          ("C", "+268.3 J K^-1 mol^-1"),
          ("D", "+344.7 J K^-1 mol^-1")]),

        # Page 4: Q7, Q8, Q9
        ("The combustion of methane is represented by:\nCH4(g) + 2O2(g) —> CO2(g) + 2H2O(l)    ΔH° = -890.3 kJ mol^-1\nGiven standard molar entropies:\nS°[CH4(g)] = 186.2, S°[O2(g)] = 205.0, S°[CO2(g)] = 213.6, S°[H2O(l)] = 69.9 J K^-1 mol^-1.\nWhat is the value of ΔS°_system for this combustion at 298 K?",
         [("A", "-242.8 J K^-1 mol^-1"),
          ("B", "+242.8 J K^-1 mol^-1"),
          ("C", "-107.7 J K^-1 mol^-1"),
          ("D", "+107.7 J K^-1 mol^-1")]),

        ("Which mathematical expression correctly defines the entropy change of the surroundings, ΔS_surroundings?",
         [("A", "ΔS_surroundings = +ΔH / T"),
          ("B", "ΔS_surroundings = -ΔH / T"),
          ("C", "ΔS_surroundings = -T / ΔH"),
          ("D", "ΔS_surroundings = ΔS_system - (ΔH / T)")]),

        ("A reaction has an enthalpy change ΔH = -286 kJ mol^-1. What is the value of ΔS_surroundings at 298 K?",
         [("A", "-0.960 J K^-1 mol^-1"),
          ("B", "+0.960 J K^-1 mol^-1"),
          ("C", "-959.7 J K^-1 mol^-1"),
          ("D", "+959.7 J K^-1 mol^-1")]),

        # Page 5: Q10, Q11, Q12
        ("An endothermic reaction absorbs 178 kJ mol^-1 of heat at 500 K. What is the entropy change of the surroundings, ΔS_surroundings?",
         [("A", "+356 J K^-1 mol^-1"),
          ("B", "-356 J K^-1 mol^-1"),
          ("C", "+0.356 J K^-1 mol^-1"),
          ("D", "-0.356 J K^-1 mol^-1")]),

        ("What is the fundamental thermodynamic criterion for a reaction to be spontaneous (feasible) under constant temperature and pressure?",
         [("A", "ΔS_system > 0"),
          ("B", "ΔS_surroundings > 0"),
          ("C", "ΔS_total > 0"),
          ("D", "ΔH < 0")]),

        ("A reaction is exothermic (ΔH < 0) and results in a decrease in system entropy (ΔS_system < 0). How does feasibility change as temperature increases?",
         [("A", "Feasible at high temperatures, non-feasible at low temperatures"),
          ("B", "Feasible at low temperatures, non-feasible at high temperatures"),
          ("C", "Feasible at all temperatures"),
          ("D", "Non-feasible at all temperatures")]),

        # Page 6: Q13, Q14, Q15
        ("A reaction is endothermic (ΔH > 0) and has a positive entropy change of the system (ΔS_system > 0). At which temperatures is this reaction feasible?",
         [("A", "Only below a certain crossover temperature"),
          ("B", "Only above a certain crossover temperature"),
          ("C", "At all temperatures"),
          ("D", "It can never be feasible at any temperature")]),

        ("Under which set of thermodynamic parameters is a chemical reaction feasible at ALL temperatures?",
         [("A", "ΔH is positive and ΔS_system is positive"),
          ("B", "ΔH is negative and ΔS_system is negative"),
          ("C", "ΔH is negative and ΔS_system is positive"),
          ("D", "ΔH is positive and ΔS_system is negative")]),

        ("Under which set of thermodynamic conditions can a chemical reaction NEVER be feasible at any temperature?",
         [("A", "ΔH is positive and ΔS_system is positive"),
          ("B", "ΔH is negative and ΔS_system is negative"),
          ("C", "ΔH is negative and ΔS_system is positive"),
          ("D", "ΔH is positive and ΔS_system is negative")]),

        # Page 7: Q16, Q17, Q18
        ("Synoptic Kinetics: Initial rate data for the reaction 2A + B —> C show that doubling [A] while keeping [B] constant quadruples the rate. Doubling [B] while keeping [A] constant doubles the rate. What is the overall order of reaction?",
         [("A", "1"),
          ("B", "2"),
          ("C", "3"),
          ("D", "4")]),

        ("Synoptic Kinetics: A reaction has the rate equation: rate = k[X]^2[Y]. What are the correct units of the rate constant, k?",
         [("A", "mol dm^-3 s^-1"),
          ("B", "dm^3 mol^-1 s^-1"),
          ("C", "dm^6 mol^-2 s^-1"),
          ("D", "s^-1")]),

        ("How does an increase in temperature affect the rate constant k and the total entropy change ΔS_total for an exothermic reaction with ΔS_system < 0?",
         [("A", "k increases; ΔS_total increases"),
          ("B", "k increases; ΔS_total decreases"),
          ("C", "k decreases; ΔS_total increases"),
          ("D", "k decreases; ΔS_total decreases")]),

        # Page 8: Q19, Q20, Q21
        ("Synoptic Kinetics: For the multistep reaction:\nStep 1: NO2 + NO2 —> NO3 + NO (slow)\nStep 2: NO3 + CO —> NO2 + CO2 (fast)\nWhich is the experimentally deduced rate equation?",
         [("A", "rate = k[NO2][CO]"),
          ("B", "rate = k[NO2]^2"),
          ("C", "rate = k[NO3][CO]"),
          ("D", "rate = k[NO2]^2[CO]")]),

        ("Synoptic Kinetics: In an Arrhenius plot of ln k against 1/T, the line has a gradient of -9.62 x 10^3 K. What is the activation energy, Ea, of the reaction? (R = 8.314 J K^-1 mol^-1)",
         [("A", "+1.16 kJ mol^-1"),
          ("B", "+79.98 kJ mol^-1"),
          ("C", "-79.98 kJ mol^-1"),
          ("D", "+1157 kJ mol^-1")]),

        ("Graphite has a standard molar entropy S° = 5.7 J K^-1 mol^-1, whereas diamond has S° = 2.4 J K^-1 mol^-1. What is the main structural reason for this difference?",
         [("A", "Diamond has weaker London dispersion forces between layers"),
          ("B", "Graphite has a lower density and its layers have vibrational freedom to slide"),
          ("C", "Diamond contains ionic impurities that restrict microstates"),
          ("D", "Graphite undergoes rapid sublimation at room temperature")]),

        # Page 9: Q22, Q23, Q24
        ("For a reaction at 298 K, ΔS_system = -198.5 J K^-1 mol^-1 and ΔH = -92.2 kJ mol^-1. What is the value of ΔS_total?",
         [("A", "-507.9 J K^-1 mol^-1"),
          ("B", "+110.9 J K^-1 mol^-1"),
          ("C", "-110.9 J K^-1 mol^-1"),
          ("D", "+507.9 J K^-1 mol^-1")]),

        ("For the vaporisation of water: H2O(l) —> H2O(g), ΔH_vap = +40.7 kJ mol^-1 and ΔS_vap = +109.1 J K^-1 mol^-1. What is the boiling temperature of water at 1 atm pressure deduced from these thermodynamic data?",
         [("A", "373.0 K"),
          ("B", "2.68 K"),
          ("C", "0.373 K"),
          ("D", "443.6 K")]),

        ("A mixture of methane and oxygen is stored at 298 K. The reaction CH4(g) + 2O2(g) —> CO2(g) + 2H2O(l) has a very large positive ΔS_total (+2745 J K^-1 mol^-1), yet no reaction is observed for decades. Why?",
         [("A", "The reaction is thermodynamically non-feasible at room temperature"),
          ("B", "The activation energy is very high, so the reaction is kinetically inert"),
          ("C", "Methane molecules do not possess any kinetic energy at 298 K"),
          ("D", "The products undergo rapid reverse dissociation back to reactants")]),

        # Page 10: Q25, Q26, Q27
        ("Trouton's rule states that the entropy of vaporisation for most normal liquids is approximately +88 J K^-1 mol^-1. Why is the entropy of vaporisation of water (ΔS_vap = +109 J K^-1 mol^-1) significantly higher than this value?",
         [("A", "Water vapour molecules are diatomic and have higher rotational freedom"),
          ("B", "Extensive hydrogen bonding in liquid water makes it unusually ordered"),
          ("C", "Water decomposes into hydrogen and oxygen gas upon boiling"),
          ("D", "The covalent O-H bonds break completely during vaporisation")]),

        ("Synoptic Kinetics: A radioactive isotope decays by a first-order process with rate constant k = 2.82 x 10^-3 s^-1. What is the half-life of this isotope?",
         [("A", "123 s"),
          ("B", "246 s"),
          ("C", "354 s"),
          ("D", "709 s")]),

        ("Synoptic Kinetics: When the temperature of a reaction mixture is increased by 10 K (e.g. from 300 K to 310 K), the rate of reaction approximately doubles. What is the primary reason for this dramatic increase?",
         [("A", "The average kinetic energy of the molecules doubles"),
          ("B", "The collision frequency between reactant molecules doubles"),
          ("C", "The fraction of molecules with energy E >= Ea increases significantly"),
          ("D", "The activation energy of the reaction is halved")]),

        # Page 11: Q28, Q29, Q30
        ("When ammonium nitrate, NH4NO3(s), dissolves in water at 298 K, the temperature drops noticeably. Which row correctly gives the signs of ΔH, ΔS_system, and ΔS_surroundings for this process?",
         [("A", "ΔH: Positive (+)  |  ΔS_system: Positive (+)  |  ΔS_surroundings: Negative (-)"),
          ("B", "ΔH: Negative (-)  |  ΔS_system: Positive (+)  |  ΔS_surroundings: Positive (+)"),
          ("C", "ΔH: Positive (+)  |  ΔS_system: Negative (-)  |  ΔS_surroundings: Positive (+)"),
          ("D", "ΔH: Negative (-)  |  ΔS_system: Negative (-)  |  ΔS_surroundings: Negative (-)")]),

        ("Liquid water freezes to ice at 268 K (-5 °C). Given that freezing is exothermic (ΔH = -6.01 kJ mol^-1) and ΔS_system = -22.0 J K^-1 mol^-1, what is the value of ΔS_total at 268 K?",
         [("A", "-0.43 J K^-1 mol^-1"),
          ("B", "+0.43 J K^-1 mol^-1"),
          ("C", "+44.4 J K^-1 mol^-1"),
          ("D", "-44.4 J K^-1 mol^-1")]),

        ("Why is the standard entropy of hydration of the magnesium ion, Mg2+(aq) (-268 J K^-1 mol^-1), significantly more negative than that of the barium ion, Ba2+(aq) (-158 J K^-1 mol^-1)?",
         [("A", "Mg2+ has a smaller ionic radius and higher charge density, attracting and immobilising water molecules more tightly"),
          ("B", "Ba2+ forms covalent bonds with surrounding water molecules"),
          ("C", "Mg2+ hydrolyses water molecules into hydrogen ions and magnesium oxide"),
          ("D", "Ba2+ has more electrons and therefore causes greater dispersion of solvent energy")])
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
    # QUESTION 31 (18 MARKS) — HABER PROCESS THERMODYNAMICS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Ammonia is synthesised industrially from nitrogen and hydrogen via the Haber process:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>(g) &nbsp;+&nbsp; 3H<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NH<sub>3</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -92.22 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Standard molar entropies, <i>S</i>°, at 298 K are provided in the table below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Substance</b>", S['tbl_th']), Paragraph("<b>N<sub>2</sub>(g)</b>", S['tbl_th']), Paragraph("<b>H<sub>2</sub>(g)</b>", S['tbl_th']), Paragraph("<b>NH<sub>3</sub>(g)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("191.6", S['tbl_td']), Paragraph("130.6", S['tbl_td']), Paragraph("192.3", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[5.0*cm, 3.6*cm, 3.6*cm, 3.6*cm])
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
        [Paragraph("<b>(a)</b> Explain why the standard molar entropy of ammonia (192.3 J K<sup>-1</sup> mol<sup>-1</sup>) is greater than that of hydrogen (130.6 J K<sup>-1</sup> mol<sup>-1</sup>), referring to molecular complexity and microstates.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, for the forward reaction in J K<sup>-1</sup> mol<sup>-1</sup>. Include a sign in your answer.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 31 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the entropy change of the surroundings, Δ<i>S</i><sub>surroundings</sub>, in J K<sup>-1</sup> mol<sup>-1</sup>:<br/>"
                   "(i) at 298 K<br/>"
                   "(ii) at 700 K (typical industrial operating temperature).<br/>"
                   "Assume that Δ<i>H</i>° remains independent of temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>surroundings</sub> (298 K) = ................................................. J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>surroundings</sub> (700 K) = ................................................. J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the total entropy change, Δ<i>S</i><sub>total</sub>, at 298 K and at 700 K. Hence deduce whether the forward reaction is thermodynamically feasible at each temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ............................................................. Feasible? ....................<br/>"
                           "Δ<i>S</i><sub>total</sub> (700 K) = ............................................................. Feasible? ....................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Calculate the crossover temperature, <i>T</i><sub>crossover</sub>, in Kelvin, above which the forward synthesis of ammonia ceases to be thermodynamically feasible.<br/>"
                   "Explain why chemical engineers operate the Haber reactor at 700 K (approx 430 °C), despite the thermodynamic penalty on feasibility.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>T</i><sub>crossover</sub> = ..................................................................................... K", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — THERMAL DECOMPOSITION OF CARBONATES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Limestone undergoes thermal decomposition in industrial lime kilns according to the equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CaCO<sub>3</sub>(s) &nbsp;—&gt;&nbsp; CaO(s) &nbsp;+&nbsp; CO<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +178.3 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Standard molar entropies at 298 K are shown below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t32_data = [
        [Paragraph("<b>Compound</b>", S['tbl_th']), Paragraph("<b>CaCO<sub>3</sub>(s)</b>", S['tbl_th']), Paragraph("<b>CaO(s)</b>", S['tbl_th']), Paragraph("<b>CO<sub>2</sub>(g)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("92.9", S['tbl_td']), Paragraph("38.2", S['tbl_td']), Paragraph("213.6", S['tbl_td'])],
    ]
    t32 = Table(t32_data, colWidths=[5.0*cm, 3.6*cm, 3.6*cm, 3.6*cm])
    t32.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t32)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain, in terms of arrangement of particles and quanta of energy, why the entropy change of the system, Δ<i>S</i>°<sub>system</sub>, is positive for this reaction.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i>°<sub>system</sub> for this thermal decomposition in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for this reaction at 298 K.<br/>"
                   "State why limestone blocks used in ancient buildings have persisted for thousands of years without decomposing.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 32 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate the minimum temperature, in °C, required for the thermal decomposition of calcium carbonate to become thermodynamically feasible.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Minimum temperature = ..................................................................................... °C", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Magnesium carbonate, MgCO<sub>3</sub>, decomposes at a significantly lower temperature (approx 300 °C) than calcium carbonate, CaCO<sub>3</sub> (approx 840 °C).<br/>"
                   "Explain this difference in thermal stability with reference to:<br/>"
                   "• the ionic radii of Mg<sup>2+</sup> and Ca<sup>2+</sup><br/>"
                   "• charge density and polarisation of the carbonate ion<br/>"
                   "• the relative lattice energies of the reactants and products.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — DISSOLUTION THERMODYNAMICS & EXPERIMENTAL CALORIMETRY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;A student investigated the thermochemistry of dissolving ammonium nitrate in water for use in instant chemical cold packs:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("NH<sub>4</sub>NO<sub>3</sub>(s) &nbsp;+&nbsp; aq &nbsp;—&gt;&nbsp; NH<sub>4</sub><sup>+</sup>(aq) &nbsp;+&nbsp; NO<sub>3</sub><sup>-</sup>(aq)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("A mass of 8.00 g of ammonium nitrate was dissolved in 50.0 cm<sup>3</sup> of deionised water in an expanded polystyrene cup. "
                           "The temperature of the water dropped by 12.4 °C.<br/>"
                           "(Assume the specific heat capacity of the solution is 4.18 J g<sup>-1</sup> K<sup>-1</sup> and the density of the solution is 1.00 g cm<sup>-3</sup>. Molar mass of NH<sub>4</sub>NO<sub>3</sub> = 80.0 g mol<sup>-1</sup>).", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the enthalpy change of solution, Δ<i>H</i><sub>sol</sub>°, in kJ mol<sup>-1</sup>. Include a sign in your answer.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>sol</sub>° = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Literature data state that the standard entropy change of the system for this dissolution is Δ<i>S</i>°<sub>system</sub> = +108.7 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>"
                   "Using your value of Δ<i>H</i><sub>sol</sub>° from (a), calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for the dissolution at 298 K.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>surroundings</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 33 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why this dissolution process occurs spontaneously at 298 K despite being endothermic, making explicit reference to the Second Law of Thermodynamics.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> In contrast to ammonium nitrate, when anhydrous copper(II) sulfate dissolves in water:<br/>"
                   "CuSO<sub>4</sub>(s) &nbsp;+&nbsp; aq &nbsp;—&gt;&nbsp; Cu<sup>2+</sup>(aq) &nbsp;+&nbsp; SO<sub>4</sub><sup>2-</sup>(aq) &nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>sol</sub>° = -66.5 kJ mol<sup>-1</sup><br/>"
                   "The entropy change of the system, Δ<i>S</i>°<sub>system</sub>, is negative (-156.0 J K<sup>-1</sup> mol<sup>-1</sup>).<br/>"
                   "Explain why dissolving an ionic solid can result in a negative entropy change of the system.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Calculate the temperature, in °C, above which the dissolution of anhydrous copper(II) sulfate ceases to be thermodynamically feasible. State one assumption made in your calculation.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Maximum temperature = ..................................................................................... °C", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ASTERISKED (*) LEVEL OF RESPONSE: COMBUSTION THERMODYNAMICS & FUELS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*34</b>&nbsp;&nbsp;Methane, CH<sub>4</sub>, and ethanol, C<sub>2</sub>H<sub>5</sub>OH, are widely utilised fuels. Their combustion reactions under standard conditions are represented by:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CH<sub>4</sub>(g) &nbsp;+&nbsp; 2O<sub>2</sub>(g) &nbsp;—&gt;&nbsp; CO<sub>2</sub>(g) &nbsp;+&nbsp; 2H<sub>2</sub>O(l) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -890.3 kJ mol<sup>-1</sup><br/>"
                           "C<sub>2</sub>H<sub>5</sub>OH(l) &nbsp;+&nbsp; 3O<sub>2</sub>(g) &nbsp;—&gt;&nbsp; 2CO<sub>2</sub>(g) &nbsp;+&nbsp; 3H<sub>2</sub>O(l) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -1367.3 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Thermodynamic data at 298 K are shown below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t34_data = [
        [Paragraph("<b>Substance</b>", S['tbl_th']), Paragraph("<b>CH<sub>4</sub>(g)</b>", S['tbl_th']), Paragraph("<b>C<sub>2</sub>H<sub>5</sub>OH(l)</b>", S['tbl_th']), Paragraph("<b>O<sub>2</sub>(g)</b>", S['tbl_th']), Paragraph("<b>CO<sub>2</sub>(g)</b>", S['tbl_th']), Paragraph("<b>H<sub>2</sub>O(l)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("186.2", S['tbl_td']), Paragraph("160.7", S['tbl_td']), Paragraph("205.0", S['tbl_td']), Paragraph("213.6", S['tbl_td']), Paragraph("69.9", S['tbl_td'])],
    ]
    t34 = Table(t34_data, colWidths=[3.2*cm] + [2.8*cm]*5)
    t34.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t34)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> For the combustion of methane at 298 K, calculate:<br/>"
                   "(i) Δ<i>S</i>°<sub>system</sub> in J K<sup>-1</sup> mol<sup>-1</sup><br/>"
                   "(ii) Δ<i>S</i><sub>surroundings</sub> in J K<sup>-1</sup> mol<sup>-1</sup><br/>"
                   "(iii) Δ<i>S</i><sub>total</sub> in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ................................... &nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>surroundings</sub> = ................................... &nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = ................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 34 Parts (b)* LoR, (c), (d)
    story.append(Table([
        [Paragraph("<b>*(b)</b> For the combustion of ethanol, Δ<i>S</i>°<sub>system</sub> = -138.1 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>"
                   "Compare and evaluate the thermodynamic feasibility and energy output of burning methane versus bioethanol.<br/>"
                   "In your answer, you should include:<br/>"
                   "• calculation of Δ<i>S</i><sub>total</sub> for ethanol at 298 K<br/>"
                   "• an explanation of why both reactions have large positive Δ<i>S</i><sub>total</sub> despite Δ<i>S</i>°<sub>system</sub> being negative<br/>"
                   "• the effect of an increase in combustion temperature on Δ<i>S</i><sub>surroundings</sub> and overall feasibility<br/>"
                   "• a comparison of the environmental impact (carbon neutrality and greenhouse warming potential).", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(c)</b> Natural gas pipelines transport methane and oxygen mixtures without explosion occurring at 298 K, despite Δ<i>S</i><sub>total</sub> being overwhelmingly positive (+2745 J K<sup>-1</sup> mol<sup>-1</sup>).<br/>"
                   "Distinguish clearly between thermodynamic feasibility and kinetic stability, referring to collision theory and activation energy.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Water is produced as a liquid in standard combustion reactions. Given that the enthalpy of vaporisation of water is Δ<i>H</i><sub>vap</sub> = +40.7 kJ mol<sup>-1</sup> at its normal boiling point (373 K), calculate the entropy of vaporisation, Δ<i>S</i><sub>vap</sub>, of water in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>vap</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — SYNOPTIC KINETICS & ENTROPY INTEGRATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;Dinitrogen pentoxide decomposes in the gas phase according to the stoichiometric equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2N<sub>2</sub>O<sub>5</sub>(g) &nbsp;—&gt;&nbsp; 4NO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +109.5 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The reaction is first order with respect to N<sub>2</sub>O<sub>5</sub>. Experimental rate constants at two different temperatures are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t35_data = [
        [Paragraph("<b>Temperature <i>T</i> / K</b>", S['tbl_th']), Paragraph("<b>298 K</b>", S['tbl_th']), Paragraph("<b>338 K</b>", S['tbl_th'])],
        [Paragraph("<b>Rate constant <i>k</i> / s<sup>-1</sup></b>", S['tbl_th']), Paragraph("3.46 × 10<sup>-5</sup>", S['tbl_td']), Paragraph("4.87 × 10<sup>-3</sup>", S['tbl_td'])],
    ]
    t35 = Table(t35_data, colWidths=[6.0*cm, 5.6*cm, 5.6*cm])
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
        [Paragraph("<b>(a)</b> Calculate the half-life, <i>t</i><sub>1/2</sub>, of the decomposition of N<sub>2</sub>O<sub>5</sub> at 298 K in seconds and in hours.<br/>"
                   "Explain how a concentration-time graph can be used to confirm that the reaction is first order.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>t</i><sub>1/2</sub> = ................................................. s &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = ................................................. hours", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Use the two-point form of the Arrhenius equation:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; ln(<i>k</i><sub>2</sub> / <i>k</i><sub>1</sub>) = (<i>E</i><sub>a</sub> / <i>R</i>) × (1/<i>T</i><sub>1</sub> - 1/<i>T</i><sub>2</sub>)<br/>"
                   "to calculate the activation energy, <i>E</i><sub>a</sub>, of the decomposition in kJ mol<sup>-1</sup>. (<i>R</i> = 8.314 J K<sup>-1</sup> mol<sup>-1</sup>)", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>E</i><sub>a</sub> = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 35 Parts (c), (d), (e)
    story.append(Paragraph("Standard molar entropies at 298 K: <i>S</i>°[N<sub>2</sub>O<sub>5</sub>(g)] = 356.0, <i>S</i>°[NO<sub>2</sub>(g)] = 240.0, <i>S</i>°[O<sub>2</sub>(g)] = 205.0 J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, for the decomposition in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for this reaction at 298 K. Hence deduce whether the decomposition is thermodynamically feasible at room temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>surroundings</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> When the temperature is raised to 350 K, N<sub>2</sub>O<sub>5</sub> decomposes rapidly with evolution of brown NO<sub>2</sub> fumes.<br/>"
                   "Explain this rapid decomposition by evaluating BOTH:<br/>"
                   "• the kinetic effect (Maxwell-Boltzmann distribution and fraction of molecules with <i>E</i> &gt;= <i>E</i><sub>a</sub>)<br/>"
                   "• the thermodynamic feasibility effect (how an increase in temperature impacts Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
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
    # QUESTION 36 (15 MARKS) — INDUSTRIAL STEAM REFORMING OF METHANE
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;The transition to a hydrogen fuel economy depends heavily on the industrial production of hydrogen via the steam reforming of natural gas:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CH<sub>4</sub>(g) &nbsp;+&nbsp; H<sub>2</sub>O(g) &nbsp;&lt;=&gt;&nbsp; CO(g) &nbsp;+&nbsp; 3H<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +206.1 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Standard molar entropies at 298 K are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t36_data = [
        [Paragraph("<b>Substance</b>", S['tbl_th']), Paragraph("<b>CH<sub>4</sub>(g)</b>", S['tbl_th']), Paragraph("<b>H<sub>2</sub>O(g)</b>", S['tbl_th']), Paragraph("<b>CO(g)</b>", S['tbl_th']), Paragraph("<b>H<sub>2</sub>(g)</b>", S['tbl_th'])],
        [Paragraph("<b><i>S</i>° / J K<sup>-1</sup> mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("186.2", S['tbl_td']), Paragraph("188.7", S['tbl_td']), Paragraph("197.6", S['tbl_td']), Paragraph("130.6", S['tbl_td'])],
    ]
    t36 = Table(t36_data, colWidths=[3.6*cm] + [3.4*cm]*4)
    t36.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (0, -1), MID_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t36)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, for the steam reforming reaction in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the minimum temperature, in °C, required for steam reforming of methane to become thermodynamically feasible (Δ<i>S</i><sub>total</sub> &gt;= 0).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Minimum temperature = ..................................................................................... °C", S['ans_prompt']))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Industrial reforming plants operate at 850 °C and 25 atm in the presence of a nickel catalyst.<br/>"
                   "(i) Explain why high temperatures (850 °C) are chosen despite the massive energy costs, referring to Δ<i>S</i><sub>total</sub> and equilibrium yield.<br/>"
                   "(ii) Using Le Chatelier's principle, explain why operating at high pressure (25 atm) decreases the equilibrium yield of hydrogen.<br/>"
                   "(iii) Suggest why high pressure is nevertheless used commercially in industrial plants.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> In a secondary stage, carbon monoxide reacts with steam via the water-gas shift reaction:<br/>"
                   "CO(g) &nbsp;+&nbsp; H<sub>2</sub>O(g) &nbsp;&lt;=&gt;&nbsp; CO<sub>2</sub>(g) &nbsp;+&nbsp; H<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -41.2 kJ mol<sup>-1</sup><br/>"
                   "Given that Δ<i>S</i>°<sub>system</sub> = -42.1 J K<sup>-1</sup> mol<sup>-1</sup>, calculate Δ<i>S</i><sub>total</sub> at 500 K.<br/>"
                   "Explain why the water-gas shift converter must be operated at a much lower temperature (200 - 350 °C) than the primary reformer.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (500 K) = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — BIOPHYSICAL THERMODYNAMICS: PROTEIN FOLDING & DENATURATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;Biochemical macromolecules such as the enzyme lysozyme undergo reversible folding and unfolding in aqueous solution:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Unfolded (random coil) &nbsp;&lt;=&gt;&nbsp; Folded (native globular conformation)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Calorimetric measurements of lysozyme folding at 298 K yield the following thermodynamic parameters:<br/>"
                           "• Enthalpy of folding: Δ<i>H</i>°<sub>fold</sub> = -280.0 kJ mol<sup>-1</sup><br/>"
                           "• Entropy of folding of the polypeptide system: Δ<i>S</i>°<sub>system</sub> = -752.0 J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why the folding of an extended, flexible polypeptide chain into a rigid, compact globular enzyme causes a large negative entropy change of the system (Δ<i>S</i>°<sub>system</sub> &lt; 0).", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for the folding of lysozyme at 298 K (25 °C).<br/>"
                   "Deduce whether the enzyme is thermodynamically stable in its folded native conformation at physiological room temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>surroundings</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = ................................................. J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 37 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> When heated, the enzyme undergoes thermal denaturation. Calculate the melting temperature, <i>T</i><sub>m</sub>, in °C, at which the folded and unfolded forms exist in equal concentrations at equilibrium (where Δ<i>S</i><sub>total</sub> = 0).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>T</i><sub>m</sub> = ..................................................................................... °C", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> In aqueous solution, non-polar hydrophobic amino acid side chains (such as leucine and phenylalanine) are buried within the interior core of the folded protein.<br/>"
                   "Explain the 'hydrophobic effect' in terms of entropy:<br/>"
                   "• how water molecules arrange themselves around non-polar side chains in the unfolded state<br/>"
                   "• what happens to these water molecules when the protein folds<br/>"
                   "• why this release of water molecules provides an entropic driving force that helps overcome the conformational ordering of the polypeptide backbone.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 4 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("SI units of entropy are J K<sup>-1</sup> mol<sup>-1</sup> (or J mol<sup>-1</sup> K<sup>-1</sup>). kJ is used for enthalpy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Steam, H2O(g), has gaseous state with rapid translational movement and highest disorder.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("1 mol of gas reactant forms 2 mol of gas products: Δn_gas = +1 > 0 => ΔS_system > 0.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("4 mol gas (1 N2 + 3 H2) -> 2 mol gas (2 NH3): Δn_gas = -2 => ΔS_system is negative.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("High charge density of Mg2+ and SO4^2- polarises and orders hydration shell water molecules.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS° = S°(CaO) + S°(CO2) - S°(CaCO3) = 38.2 + 213.6 - 92.9 = +158.9 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔS° = [213.6 + 2(69.9)] - [186.2 + 2(205.0)] = 353.4 - 596.2 = -242.8 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Definition of surroundings entropy: ΔS_surroundings = -ΔH / T.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("ΔS_surr = -(-286 000 J mol^-1) / 298 K = +959.7 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_surr = -(+178 000 J mol^-1) / 500 K = -356 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Second Law of Thermodynamics: Feasibility requires ΔS_total > 0.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Exothermic with ΔS_sys < 0: ΔS_surr is large positive at low T (feasible), but decreases as T rises.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Endothermic with ΔS_sys > 0: -ΔH/T becomes less negative as T rises, so ΔS_total > 0 at high T.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("ΔH < 0 (ΔS_surr > 0) and ΔS_sys > 0 => ΔS_total = ΔS_sys + ΔS_surr is positive at all T.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("ΔH > 0 (ΔS_surr < 0) and ΔS_sys < 0 => ΔS_total is negative at all T (never feasible).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Rate = k[A]^2[B]^1 => overall order = 2 + 1 = 3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Units of k for 3rd order: (mol dm^-3 s^-1) / (mol dm^-3)^3 = dm^6 mol^-2 s^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("k always increases with T (Arrhenius); for exothermic, ΔS_surr = -ΔH/T decreases => ΔS_total decreases.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Step 1 is slow RDS involving 2 molecules of NO2 => rate = k[NO2]^2. CO is in fast Step 2.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Gradient = -Ea / R => Ea = -(-9.62 x 10^3) * 8.314 = +79 980 J mol^-1 = +79.98 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Graphite has layer structure with weak inter-layer forces and more vibrational microstates.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_surr = -(-92 200) / 298 = +309.4 J K^-1 mol^-1; ΔS_total = -198.5 + 309.4 = +110.9 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("At boiling point ΔS_total = 0 => T = ΔH_vap / ΔS_vap = 40 700 / 109.1 = 373.0 K.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("High activation energy Ea creates a massive kinetic barrier; reaction is kinetically inert.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Liquid water contains hydrogen-bonded networks, giving it unusually low liquid entropy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("For first-order decay: t_1/2 = ln 2 / k = 0.69315 / 0.00282 = 245.8 s ≈ 246 s.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Higher T shifts Maxwell-Boltzmann distribution, exponentially increasing molecules with E >= Ea.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Dissolving absorbs heat (ΔH > 0), increases disorder (ΔS_sys > 0), takes heat from surroundings (ΔS_surr < 0).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_surr = -(-6010 J mol^-1) / 268 K = +22.43; ΔS_total = -22.0 + 22.43 = +0.43 J K^-1 mol^-1 (spontaneous!).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Small Mg2+ has high charge density, immobilising hydration water molecules into ordered shell.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Haber Process Thermodynamics & Crossover Feasibility (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Ammonia has more atoms / more bonds per molecule (4 atoms vs 2 in H2) [1]<br/>"
         "• Hence NH3 has more vibrational, rotational, and translational modes / more microstates to disperse quanta of energy [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• ΔS°_system = ΣS°(products) - ΣS°(reactants) = 2(192.3) - [191.6 + 3(130.6)] [1]<br/>"
         "• = 384.6 - [191.6 + 391.8] = 384.6 - 583.4 [1]<br/>"
         "• = -198.8 J K^-1 mol^-1 (must include minus sign and correct value) [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• (i) At 298 K: ΔS_surr = -(-92 220 J mol^-1) / 298 K = +309.46 J K^-1 mol^-1 [2]<br/>"
         "• (ii) At 700 K: ΔS_surr = -(-92 220 J mol^-1) / 700 K = +131.74 J K^-1 mol^-1 [2]<br/>"
         "<i>Examiner Trap: Forgetting to multiply ΔH by 1000 loses 1 mark per calculation!</i><br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• At 298 K: ΔS_total = -198.8 + 309.46 = +110.66 J K^-1 mol^-1 => ΔS_total > 0, feasible [2]<br/>"
         "• At 700 K: ΔS_total = -198.8 + 131.74 = -67.06 J K^-1 mol^-1 => ΔS_total < 0, non-feasible [2].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Crossover when ΔS_total = 0 => ΔS_surr = -ΔS_sys => -ΔH/T = -ΔS_sys => T = ΔH / ΔS_sys [1]<br/>"
         "• T = (-92 220) / (-198.8) = 463.9 K (approx 191 °C) [2]<br/>"
         "• Compromise explanation: At 298 K / low T, reaction is feasible but rate is imperceptibly slow due to high activation energy of breaking N≡N triple bond [1]<br/>"
         "• 700 K with iron catalyst provides acceptable rate of reaction; unreacted gases are recycled [1]."),

        ("Question 32: Thermal Decomposition of Calcium Carbonate (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• 1 mole of solid forms 1 mole of solid plus 1 mole of gas [1]<br/>"
         "• Gases have vastly more disordered particles / higher microstate distribution of kinetic energy [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• ΔS°_system = S°(CaO) + S°(CO2) - S°(CaCO3) [1]<br/>"
         "• = 38.2 + 213.6 - 92.9 [1]<br/>"
         "• = +158.9 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• ΔS_surr = -(+178 300) / 298 = -598.32 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = +158.9 + (-598.32) = -439.42 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total is strongly negative, so the reaction is completely non-spontaneous at room temperature [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Feasibility when ΔS_total >= 0 => T_min = ΔH / ΔS_system [1]<br/>"
         "• T_min = 178 300 / 158.9 = 1122.1 K [2]<br/>"
         "• In °C: 1122.1 - 273.15 = 848.9 °C ≈ 849 °C [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Mg2+ has a smaller ionic radius than Ca2+ (0.072 nm vs 0.100 nm) [1]<br/>"
         "• Both have +2 charge, so Mg2+ has a much higher charge density [1]<br/>"
         "• Mg2+ exerts greater polarising power on the large, polarisable CO3^2- electron cloud [1]<br/>"
         "• This weakens the C-O bond within carbonate, facilitating release of CO2 [1]<br/>"
         "• Lattice energy difference between MgO and MgCO3 is more favourable than CaO and CaCO3 [1]."),

        ("Question 33: Dissolution Calorimetry & Thermodynamic Driving Forces (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Mass of solution = 50.0 g (from volume 50 cm^3 and density 1.0 g cm^-3) [1]<br/>"
         "• q = m c ΔT = 50.0 g * 4.18 J g^-1 K^-1 * 12.4 K = 2591.6 J = 2.5916 kJ [1]<br/>"
         "• Moles of NH4NO3 = 8.00 / 80.0 = 0.100 mol [1]<br/>"
         "• ΔH_sol° = +q / n = +2.5916 / 0.100 = +25.92 kJ mol^-1 (endothermic, must have + sign) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• ΔS_surr = -ΔH / T = -25 916 J mol^-1 / 298 K = -86.97 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total = ΔS_system + ΔS_surr = +108.7 + (-86.97) = +21.73 J K^-1 mol^-1 [2].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Feasibility is dictated by ΔS_total, NOT ΔH alone [1]<br/>"
         "• Although heat is taken from surroundings (ΔS_surr < 0), the breakdown of the crystal lattice creates immense disorder (ΔS_sys = +108.7) [1]<br/>"
         "• Because ΔS_system outweighs the negative ΔS_surroundings, ΔS_total > 0, satisfying the 2nd Law [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Dissolving releases free ions, but Cu2+ has high charge (+2) and relatively small radius [1]<br/>"
         "• Water dipoles are strongly attracted to Cu2+ and SO4^2-, forming rigid, highly ordered hydration shells [1]<br/>"
         "• The loss of disorder from ordering of solvent water molecules exceeds the gain in disorder from crystal lattice breakdown [1].<br/><br/>"
         "<b>(e) [4 Marks]</b><br/>"
         "• Feasible when ΔS_total >= 0 => ΔS_sys - ΔH/T >= 0 => -156.0 - (-66 500 / T) >= 0 [1]<br/>"
         "• 66 500 / T >= 156.0 => T <= 66 500 / 156.0 = 426.28 K [2]<br/>"
         "• In °C: 426.28 - 273.15 = 153.1 °C [1].<br/>"
         "• Assumption: ΔH and ΔS_system do not change significantly with temperature."),

        ("Question 34: *Level of Response — Combustion Thermodynamics & Fuels (18 Marks)",
         "<b>(a) [5 Marks]</b><br/>"
         "• (i) ΔS°_system = [213.6 + 2(69.9)] - [186.2 + 2(205.0)] = 353.4 - 596.2 = -242.8 J K^-1 mol^-1 [2]<br/>"
         "• (ii) ΔS_surr = -(-890 300) / 298 = +2987.58 J K^-1 mol^-1 [2]<br/>"
         "• (iii) ΔS_total = -242.8 + 2987.58 = +2744.78 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Correctly calculates ethanol ΔS_surr = +4588.26 and ΔS_total = +4450.16 J K^-1 mol^-1. Explains that massive exothermic enthalpy releases heat into surroundings, generating huge positive ΔS_surr that overwhelms negative ΔS_sys. Explains that higher temperature reduces ΔS_surr (-ΔH/T), slightly decreasing ΔS_total (though still huge positive). Evaluates bioethanol as renewable / potentially carbon neutral vs fossil methane.<br/>"
         "• Level 2 (3-4 marks): Correct calculations with minor slip; explains dominance of ΔS_surroundings; basic comparison of environmental impact.<br/>"
         "• Level 1 (1-2 marks): Partial calculation; identifies that both are feasible.<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Thermodynamic feasibility indicates the direction of spontaneous change (ΔS_total > 0), but says nothing about reaction rate [1]<br/>"
         "• C-H bonds in methane (413 kJ mol^-1) and O=O in oxygen (498 kJ mol^-1) require large energy to break [1]<br/>"
         "• At 298 K, negligible fraction of molecules have energy E >= Ea (kinetic stability / inertness) [1]<br/>"
         "• A spark or flame provides energy to overcome Ea, triggering self-sustaining reaction [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• At boiling point (373 K), liquid and vapour are in dynamic equilibrium: ΔS_total = 0 [1]<br/>"
         "• ΔS_vap = ΔH_vap / T_b = +40 700 J mol^-1 / 373 K [1]<br/>"
         "• = +109.12 J K^-1 mol^-1 (acceptable range: +109.0 to +109.2) [1]."),

        ("Question 35: Synoptic N2O5 Decomposition — Kinetics & Thermodynamics (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• t_1/2 = ln 2 / k = 0.69315 / (3.46 x 10^-5 s^-1) = 20 033 s [2]<br/>"
         "• In hours: 20 033 / 3600 = 5.56 hours [1]<br/>"
         "• Successive half-lives on a [N2O5] vs time graph are constant, which is unique diagnostic for 1st order [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• ln(k2 / k1) = ln(4.87 x 10^-3 / 3.46 x 10^-5) = ln(140.75) = 4.9470 [1]<br/>"
         "• (1/T1 - 1/T2) = (1/298 - 1/338) = 0.0033557 - 0.0029586 = 3.971 x 10^-4 K^-1 [1]<br/>"
         "• Ea / R = 4.9470 / (3.971 x 10^-4) = 12 457.8 K [1]<br/>"
         "• Ea = 12 457.8 * 8.314 = 103 574 J mol^-1 = +103.6 kJ mol^-1 [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• ΔS°_system = [4*S°(NO2) + S°(O2)] - 2*S°(N2O5) = [4(240.0) + 205.0] - 2(356.0) [1]<br/>"
         "• = [960.0 + 205.0] - 712.0 = 1165.0 - 712.0 [1]<br/>"
         "• = +453.0 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• ΔS_surr = -ΔH / T = -(+109 500) / 298 = -367.45 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total = +453.0 + (-367.45) = +85.55 J K^-1 mol^-1 [1]<br/>"
         "• Since ΔS_total > 0, reaction IS thermodynamically feasible at 298 K [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• Kinetics: Higher T shifts Maxwell-Boltzmann curve to right, exponentially increasing fraction of molecules with E >= Ea (103.6 kJ mol^-1), multiplying reaction rate dramatically [2]<br/>"
         "• Thermodynamics: Higher T decreases magnitude of negative ΔS_surr (-ΔH/T), making ΔS_total even more positive (+140 J K^-1 mol^-1 at 350 K), shifting equilibrium further toward products [1]."),

        ("Question 36: Steam Reforming of Methane & Industrial Hydrogen (15 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• ΔS°_system = [S°(CO) + 3*S°(H2)] - [S°(CH4) + S°(H2O)] [1]<br/>"
         "• = [197.6 + 3(130.6)] - [186.2 + 188.7] = [197.6 + 391.8] - 374.9 = 589.4 - 374.9 [1]<br/>"
         "• = +214.5 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Feasible when ΔS_total >= 0 => T >= ΔH / ΔS_system [1]<br/>"
         "• T_min = 206 100 J mol^-1 / 214.5 J K^-1 mol^-1 = 960.84 K [2]<br/>"
         "• In °C: 960.84 - 273.15 = 687.7 °C ≈ 688 °C [1].<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• (i) Endothermic: Higher T increases ΔS_total (less negative ΔS_surr), substantially increasing Kp and equilibrium yield of H2; also increases rate to reach equilibrium quickly [2]<br/>"
         "• (ii) Reactants = 2 mol gas; Products = 4 mol gas. Increasing pressure shifts position of equilibrium to side with fewer moles of gas (to left), reducing yield of H2 [2]<br/>"
         "• (iii) High pressure increases collision frequency / rate of reaction, reduces reactor volume required (capital cost), and delivers H2 at high pressure for downstream processing [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• ΔS_surr = -(-41 200) / 500 = +82.4 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = -42.1 + 82.4 = +40.3 J K^-1 mol^-1 [1]<br/>"
         "• Reaction is exothermic: operating at lower temperature increases ΔS_surroundings and ΔS_total, maximising conversion of poisonous CO to CO2 and H2 [1]."),

        ("Question 37: Biophysical Thermodynamics of Protein Folding (15 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Unfolded protein exists as flexible random coil with billions of possible conformational states [1]<br/>"
         "• Native folded state is a single, highly constrained 3D tertiary structure, drastically reducing conformational microstates (ΔS_chain < 0) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• ΔS_surr = -(-280 000 J mol^-1) / 298 K = +939.60 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total = -752.0 + 939.60 = +187.60 J K^-1 mol^-1 [1]<br/>"
         "• Since ΔS_total > 0, the folded enzyme is thermodynamically stable and spontaneous at 298 K [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• At melting temperature Tm, folded and unfolded states in equilibrium: ΔS_total = 0 [1]<br/>"
         "• Tm = ΔH°_fold / ΔS°_system = (-280 000) / (-752.0) = 372.34 K [2]<br/>"
         "• In °C: 372.34 - 273.15 = 99.2 °C [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• In unfolded polypeptide, water molecules form highly ordered hydrogen-bonded 'clathrate cages' around exposed non-polar side chains, lowering water entropy [2]<br/>"
         "• Upon folding, non-polar side chains cluster into internal core, releasing ordered cage water molecules into bulk liquid [2]<br/>"
         "• The immense increase in solvent water entropy (positive ΔS_solvent) compensates for the loss of polypeptide conformational entropy, driving spontaneous folding [1].")
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
    print(f"[SUCCESS] Week 4 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")


if __name__ == '__main__':
    build_pdf()
