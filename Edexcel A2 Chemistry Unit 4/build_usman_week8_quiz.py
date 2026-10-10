"""
build_usman_week8_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 8 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 13A.3: Factors Affecting Equilibrium Constants 1 (Temperature Effects on Kc & Kp)
  - 13A.4: Factors NOT Affecting Equilibrium Constants 2 (Why Pressure, Concentration & Catalysts Do Not Alter K)
  - 13A.5: Relating Entropy to Equilibrium Constants (Delta S_total = R ln K & van 't Hoff Equation)
  - 14A.1: The Brønsted-Lowry Theory (Conjugate Acid-Base Pairs & Amphiprotic Species)

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
    "Usman_Edexcel_Chem_U4_Week8_150M_Challenging_Quiz.pdf"
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
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="ln Kp", x_label="1/T / 10^-3 K^-1"):
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 8 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 8 (150 Marks)...")
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
                   "<b>[  0  ][  0  ][  8  ][  8  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W08</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 8 ASSESSMENT: FACTORS AFFECTING K, ΔS_total = R ln K & BRØNSTED-LOWRY THEORY</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 8 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 13A.3: Factors Affecting K (Temperature)<br/>Topic 13A.4: Factors NOT Affecting K (Pressure, Concentration, Catalysts)<br/>Topic 13A.5: Relating Entropy to K (ΔS_total = R ln K & van 't Hoff)<br/>Topic 14A.1: The Brønsted-Lowry Theory (Conjugate Pairs & Amphiprotic)", S['edx_meta'])],
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
        ("Which factor will change the numerical value of the equilibrium constant Kc for an endothermic reaction?",
         [("A", "Increasing the total pressure"),
          ("B", "Increasing the concentration of reactants"),
          ("C", "Increasing the temperature"),
          ("D", "Adding a finely divided catalyst")]),

        ("For the exothermic reaction: 2SO2(g) + O2(g) <==> 2SO3(g) (ΔH = -197 kJ mol^-1), how does an increase in temperature affect the equilibrium constant Kp and the position of equilibrium?",
         [("A", "Kp increases; equilibrium shifts right"),
          ("B", "Kp decreases; equilibrium shifts left"),
          ("C", "Kp remains constant; equilibrium shifts left"),
          ("D", "Kp increases; equilibrium shifts left")]),

        ("Which mathematical equation correctly relates the total entropy change, ΔS_total, to the equilibrium constant K?",
         [("A", "ΔS_total = R * ln K"),
          ("B", "ΔS_total = -R * T * ln K"),
          ("C", "ln K = R / ΔS_total"),
          ("D", "K = R * ln(ΔS_total)")]),

        # Page 3: Q4, Q5, Q6
        ("If a chemical reaction has an equilibrium constant K = 1.0 at 298 K, what is the value of ΔS_total?",
         [("A", "+8.314 J K^-1 mol^-1"),
          ("B", "-8.314 J K^-1 mol^-1"),
          ("C", "0 J K^-1 mol^-1"),
          ("D", "+298 J K^-1 mol^-1")]),

        ("A reaction has ΔS_total = +57.5 J K^-1 mol^-1 at 298 K. What is the value of the equilibrium constant K? (R = 8.314 J K^-1 mol^-1)",
         [("A", "6.92"),
          ("B", "1.01 x 10^3"),
          ("C", "1.00"),
          ("D", "4.82 x 10^-4")]),

        ("According to the Brønsted-Lowry theory, an acid is defined as a species that:",
         [("A", "Accepts a lone pair of electrons"),
          ("B", "Donates a proton (H+ ion)"),
          ("C", "Produces OH- ions in aqueous solution"),
          ("D", "Increases the oxidation state of hydrogen")]),

        # Page 4: Q7, Q8, Q9
        ("In the reaction: HSO4-(aq) + H2O(l) <==> SO4^2-(aq) + H3O+(aq), which pair represents a conjugate acid-base pair?",
         [("A", "HSO4- and H2O"),
          ("B", "HSO4- and SO4^2-"),
          ("C", "H2O and HSO4-"),
          ("D", "SO4^2- and H3O+")]),

        ("Which of the following chemical species is amphiprotic (can act as both a Brønsted-Lowry acid and base)?",
         [("A", "CO3^2-"),
          ("B", "HCO3-"),
          ("C", "H3O+"),
          ("D", "Cl-")]),

        ("Why does increasing the total pressure have NO effect on the value of Kp for the reaction: N2(g) + 3H2(g) <==> 2NH3(g)?",
         [("A", "The mole fractions of all gases remain constant"),
          ("B", "Kp depends strictly on temperature through the thermodynamic relation ΔS_total = R ln K"),
          ("C", "The catalyst prevents pressure from affecting the equilibrium constant"),
          ("D", "The compressibility of nitrogen gas is negligible at high pressure")]),

        # Page 5: Q10, Q11, Q12
        ("In a graph of ln Kp against 1/T for an endothermic reaction (ΔH > 0), what is the gradient of the straight line?",
         [("A", "Positive gradient (+ΔH / R)"),
          ("B", "Negative gradient (-ΔH / R)"),
          ("C", "Zero gradient"),
          ("D", "Gradient equal to -Ea / R")]),

        ("In liquid ammonia, self-ionisation occurs according to: 2NH3 <==> NH4+ + NH2-. What is the conjugate base of NH3 in this system?",
         [("A", "NH4+"),
          ("B", "NH2-"),
          ("C", "N^3-"),
          ("D", "H+")]),

        ("When ethanoic acid is dissolved in pure liquid sulfuric acid: CH3COOH + H2SO4 <==> CH3COOH2+ + HSO4-. What role does CH3COOH play?",
         [("A", "Brønsted-Lowry acid"),
          ("B", "Brønsted-Lowry base"),
          ("C", "Dehydrating agent"),
          ("D", "Lewis acid")]),

        # Page 6: Q13, Q14, Q15
        ("For the equilibrium: N2O4(g) <==> 2NO2(g), the volume is suddenly halved at constant temperature. Immediately after the change, what is the value of the reaction quotient Qp relative to Kp?",
         [("A", "Qp = Kp"),
          ("B", "Qp = 2 Kp"),
          ("C", "Qp = 0.5 Kp"),
          ("D", "Qp = 4 Kp")]),

        ("A reaction has a very large positive equilibrium constant (K = 1.0 x 10^12) at 298 K. What can be concluded about the reaction?",
         [("A", "The reaction occurs at a very rapid rate at 298 K"),
          ("B", "The activation energy of the reaction must be zero"),
          ("C", "The position of equilibrium lies almost entirely on the side of the products"),
          ("D", "The reaction must be endothermic")]),

        ("What is the conjugate acid of the dihydrogen phosphate ion, H2PO4-?",
         [("A", "HPO4^2-"),
          ("B", "PO4^3-"),
          ("C", "H3PO4"),
          ("D", "H4PO4+")]),

        # Page 7: Q16, Q17, Q18
        ("How does an increase in temperature affect an endothermic equilibrium in terms of entropy?",
         [("A", "ΔS_system increases"),
          ("B", "ΔS_surroundings (-ΔH/T) becomes less negative, so ΔS_total increases, increasing K"),
          ("C", "ΔS_surroundings becomes more negative, decreasing K"),
          ("D", "Both ΔS_system and ΔS_surroundings remain constant")]),

        ("For the Contact process: 2SO2(g) + O2(g) <==> 2SO3(g), Kp = 3.0 x 10^4 atm^-1 at 700 K. What is the value of ΔS_total at 700 K? (R = 8.314 J K^-1 mol^-1)",
         [("A", "+85.7 J K^-1 mol^-1"),
          ("B", "+28.8 J K^-1 mol^-1"),
          ("C", "-85.7 J K^-1 mol^-1"),
          ("D", "+103.5 J K^-1 mol^-1")]),

        ("When sodium ethanoate is dissolved in water, the solution becomes slightly alkaline (pH ≈ 8.9). Which equation represents the Brønsted-Lowry reaction responsible for this observation?",
         [("A", "Na+(aq) + H2O(l) <==> NaOH(aq) + H+(aq)"),
          ("B", "CH3COO-(aq) + H2O(l) <==> CH3COOH(aq) + OH-(aq)"),
          ("C", "CH3COOH(aq) + OH-(aq) <==> CH3COO-(aq) + H2O(l)"),
          ("D", "2H2O(l) <==> H3O+(aq) + OH-(aq)")]),

        # Page 8: Q19, Q20, Q21
        ("Why does the addition of a catalyst have NO effect on the value of ΔS_total for a reaction?",
         [("A", "A catalyst changes both ΔH and ΔS_system equally"),
          ("B", "State functions ΔH, ΔS_system, and ΔS_surroundings depend only on the initial and final states, not on the reaction pathway"),
          ("C", "Catalysts only function at absolute zero"),
          ("D", "A catalyst increases the entropy of the activation complex")]),

        ("In the equilibrium: NH3(aq) + H2O(l) <==> NH4+(aq) + OH-(aq), what is the role of H2O(l)?",
         [("A", "Brønsted-Lowry acid"),
          ("B", "Brønsted-Lowry base"),
          ("C", "Conjugate acid of NH4+"),
          ("D", "Catalyst")]),

        ("For a reaction with ΔH° = -100 kJ mol^-1, which sketch of ln K against 1/T is correct?",
         [("A", "A straight line with positive gradient (+ΔH°/R)"),
          ("B", "A straight line with negative gradient (-ΔH°/R)"),
          ("C", "A horizontal line parallel to the 1/T axis"),
          ("D", "An exponential curve concave upwards")]),

        # Page 9: Q22, Q23, Q24
        ("Which of the following species CANNOT act as a Brønsted-Lowry acid?",
         [("A", "NH4+"),
          ("B", "HSO3-"),
          ("C", "BF3"),
          ("D", "H2O")]),

        ("When nitric acid dissolves in concentrated sulfuric acid, the nitronium ion is formed: HNO3 + 2H2SO4 <==> NO2+ + H3O+ + 2HSO4-. Which species acts as a Brønsted-Lowry base in this reaction?",
         [("A", "H2SO4"),
          ("B", "HNO3"),
          ("C", "NO2+"),
          ("D", "HSO4-")]),

        ("If ΔS_total for a reaction is negative at a particular temperature, what is the value of K?",
         [("A", "K < 0"),
          ("B", "0 < K < 1"),
          ("C", "K = 1"),
          ("D", "K > 1")]),

        # Page 10: Q25, Q26, Q27
        ("Consider the water-gas shift reaction: CO(g) + H2O(g) <==> CO2(g) + H2(g) (ΔH° = -41.2 kJ mol^-1). How will the equilibrium yield of H2 and the value of Kc change if the temperature is lowered?",
         [("A", "Yield of H2 increases; Kc increases"),
          ("B", "Yield of H2 decreases; Kc decreases"),
          ("C", "Yield of H2 increases; Kc remains constant"),
          ("D", "Yield of H2 decreases; Kc increases")]),

        ("Which of the following represents the conjugate base of the ammonium ion, NH4+?",
         [("A", "NH3"),
          ("B", "NH2-"),
          ("C", "NH2OH"),
          ("D", "N2")]),

        ("At 500 K, Kp for a reaction is 10.0 atm. If the total pressure is doubled by compression at 500 K, what is the new value of Kp?",
         [("A", "20.0 atm"),
          ("B", "5.0 atm"),
          ("C", "10.0 atm"),
          ("D", "100.0 atm")]),

        # Page 11: Q28, Q29, Q30
        ("Why is the hydrogen carbonate ion, HCO3-, classified as amphiprotic?",
         [("A", "It can donate H+ to form CO3^2- and accept H+ to form H2CO3"),
          ("B", "It can form both ionic and covalent bonds"),
          ("C", "It dissolves in both polar and non-polar solvents"),
          ("D", "It can be oxidised to CO2 and reduced to C")]),

        ("A reaction has K = 2.5 x 10^-5 at 298 K. What is the value of ΔS_total at 298 K? (R = 8.314 J K^-1 mol^-1)",
         [("A", "+88.1 J K^-1 mol^-1"),
          ("B", "-88.1 J K^-1 mol^-1"),
          ("C", "-10.6 J K^-1 mol^-1"),
          ("D", "+10.6 J K^-1 mol^-1")]),

        ("In the reaction: CH3COOH + HClO4 <==> CH3COOH2+ + ClO4-, which species is the conjugate base?",
         [("A", "CH3COOH"),
          ("B", "HClO4"),
          ("C", "CH3COOH2+"),
          ("D", "ClO4-")])
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
    # QUESTION 31 (18 MARKS) — VAN 'T HOFF ANALYSIS: METHANOL SYNTHESIS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Methanol is produced industrially from synthesis gas (syngas) according to the reversible reaction:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CO(g) &nbsp;+&nbsp; 2H<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; CH<sub>3</sub>OH(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The equilibrium constant, <i>K</i><sub>p</sub>, was measured experimentally at several temperatures. The experimental data are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Temperature <i>T</i> / K</b>", S['tbl_th']), Paragraph("<b>500</b>", S['tbl_th']), Paragraph("<b>550</b>", S['tbl_th']), Paragraph("<b>600</b>", S['tbl_th']), Paragraph("<b>650</b>", S['tbl_th']), Paragraph("<b>700</b>", S['tbl_th'])],
        [Paragraph("<b>1/<i>T</i> / 10<sup>-3</sup> K<sup>-1</sup></b>", S['tbl_th']), Paragraph("2.00", S['tbl_td']), Paragraph("1.82", S['tbl_td']), Paragraph("1.67", S['tbl_td']), Paragraph("1.54", S['tbl_td']), Paragraph("1.43", S['tbl_td'])],
        [Paragraph("<b><i>K</i><sub>p</sub> / kPa<sup>-2</sup></b>", S['tbl_th']), Paragraph("6.23 × 10<sup>-3</sup>", S['tbl_td']), Paragraph("3.81 × 10<sup>-4</sup>", S['tbl_td']), Paragraph("3.42 × 10<sup>-5</sup>", S['tbl_td']), Paragraph("4.32 × 10<sup>-6</sup>", S['tbl_td']), Paragraph("7.14 × 10<sup>-7</sup>", S['tbl_td'])],
        [Paragraph("<b>ln <i>K</i><sub>p</sub></b>", S['tbl_th']), Paragraph("-5.08", S['tbl_td']), Paragraph("-7.87", S['tbl_td']), Paragraph("-10.28", S['tbl_td']), Paragraph("-12.35", S['tbl_td']), Paragraph("-14.15", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[4.2*cm] + [2.35*cm]*5)
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
        [Paragraph("<b>(a)</b> In the space below, sketch the graph of ln <i>K</i><sub>p</sub> against 1/<i>T</i>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(AVAIL_W, 6.2*cm, y_label="ln Kp", x_label="1/T / 10^-3 K^-1"))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The van 't Hoff equation states that:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; ln <i>K</i><sub>p</sub> = (-Δ<i>H</i>° / <i>R</i>) × (1/<i>T</i>) + (Δ<i>S</i>°<sub>system</sub> / <i>R</i>)<br/>"
                   "Calculate the gradient of the line using the data points at <i>T</i> = 500 K and <i>T</i> = 700 K. Include the sign and units of the gradient.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Gradient = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 31 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Using your gradient from (b), calculate the standard enthalpy change, Δ<i>H</i>°, for the reaction in kJ mol<sup>-1</sup>. Include a sign in your answer. (<i>R</i> = 8.314 J mol<sup>-1</sup> K<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i>° = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Use your value of Δ<i>H</i>° and the experimental value of ln <i>K</i><sub>p</sub> at 500 K to calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Explain why the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, is negative for this reaction, and why the value of <i>K</i><sub>p</sub> decreases so steeply as temperature increases.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — MATHEMATICAL PROOF: WHY PRESSURE DOES NOT ALTER Kp
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;A common misconception among chemistry students is that changing the pressure alters the value of the equilibrium constant <i>K</i><sub>p</sub>.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Consider the gas-phase dissociation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>O<sub>4</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NO<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("At 298 K, this system is at dynamic equilibrium inside a gas syringe. The equilibrium partial pressures are:<br/>"
                           "• <i>p</i>(N<sub>2</sub>O<sub>4</sub>) = 0.800 atm<br/>"
                           "• <i>p</i>(NO<sub>2</sub>) = 0.400 atm", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the value of <i>K</i><sub>p</sub> at 298 K, including units.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>p</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The plunger of the syringe is suddenly pushed in, halving the volume of the gas mixture at constant temperature.<br/>"
                   "(i) State the instantaneous partial pressure of each gas immediately after the volume is halved (before any reaction occurs).<br/>"
                   "(ii) Calculate the instantaneous reaction quotient, <i>Q</i><sub>p</sub>, immediately after compression.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>Q</i><sub>p</sub> = ..................................................................................... atm", S['ans_prompt']))
    story.append(PageBreak())

    # Question 32 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Compare your value of <i>Q</i><sub>p</sub> from (b) with the equilibrium constant <i>K</i><sub>p</sub> from (a).<br/>"
                   "Deduce, with mathematical reasoning, in which direction the reaction must proceed to re-establish dynamic equilibrium.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Explain clearly why the position of equilibrium shifted when pressure was increased, even though the numerical value of <i>K</i><sub>p</sub> remained completely unchanged.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> If the same compression experiment is repeated for the reaction H<sub>2</sub>(g) + I<sub>2</sub>(g) &lt;=&gt; 2HI(g), explain why halving the volume does NOT cause any shift in the position of equilibrium.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — THERMODYNAMIC CALCULATION OF K FROM TOTAL ENTROPY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;The thermal decomposition of calcium carbonate in an industrial lime kiln is represented by:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CaCO<sub>3</sub>(s) &nbsp;&lt;=&gt;&nbsp; CaO(s) &nbsp;+&nbsp; CO<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +178.3 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Thermodynamic data at 298 K are shown below:<br/>"
                           "• <i>S</i>°[CaCO<sub>3</sub>(s)] = 92.9 J K<sup>-1</sup> mol<sup>-1</sup><br/>"
                           "• <i>S</i>°[CaO(s)] = 38.2 J K<sup>-1</sup> mol<sup>-1</sup><br/>"
                           "• <i>S</i>°[CO<sub>2</sub>(g)] = 213.6 J K<sup>-1</sup> mol<sup>-1</sup>", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the standard entropy change of the system, Δ<i>S</i>°<sub>system</sub>, in J K<sup>-1</sup> mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i>°<sub>system</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> at 298 K.<br/>"
                   "Using the relationship Δ<i>S</i><sub>total</sub> = <i>R</i> ln <i>K</i>, calculate the equilibrium constant <i>K</i><sub>p</sub> at 298 K. (<i>R</i> = 8.314 J mol<sup>-1</sup> K<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ................................... J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>p</sub> (298 K) = ................................... atm", S['ans_prompt']))
    story.append(PageBreak())

    # Question 33 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate Δ<i>S</i><sub>total</sub> and <i>K</i><sub>p</sub> at 1200 K (approx 930 °C), assuming Δ<i>H</i>° and Δ<i>S</i>°<sub>system</sub> do not vary significantly with temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (1200 K) = ................................... J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>p</sub> (1200 K) = ................................... atm", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> For this heterogeneous reaction, write the expression for <i>K</i><sub>p</sub> in terms of partial pressures.<br/>"
                   "Using your value of <i>K</i><sub>p</sub> at 1200 K from (c), state the equilibrium partial pressure of carbon dioxide inside a sealed kiln at 1200 K.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>p</i>(CO<sub>2</sub>) = ..................................................................................... atm", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> In commercial lime kilns, air is continuously blown through the kiln to sweep away the carbon dioxide gas.<br/>"
                   "Explain how this engineering measure ensures 100 % conversion of limestone to quicklime at temperatures lower than 1200 K.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ASTERISKED (*) LEVEL OF RESPONSE: LE CHATELIER VS ΔS_total = R ln K
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*34</b>&nbsp;&nbsp;Two approaches are used to predict the effect of conditions on reversible reactions:<br/>"
                           "• Qualitative approach: Le Chatelier's Principle<br/>"
                           "• Quantitative thermodynamic approach: The Second Law of Thermodynamics (Δ<i>S</i><sub>total</sub> = <i>R</i> ln <i>K</i>)", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Consider the two industrial reactions:<br/>"
                           "<b>Reaction 1 (Exothermic):</b> N<sub>2</sub>(g) &nbsp;+&nbsp; 3H<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NH<sub>3</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -92 kJ mol<sup>-1</sup><br/>"
                           "<b>Reaction 2 (Endothermic):</b> N<sub>2</sub>O<sub>4</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NO<sub>2</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = +57 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> For Reaction 1, explain using Le Chatelier's principle how an increase in temperature affects the equilibrium yield of ammonia.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)* Level of Response
    story.append(Table([
        [Paragraph("<b>*(b)</b> Evaluate how the thermodynamic equation:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>S</i><sub>total</sub> = Δ<i>S</i><sub>system</sub> - (Δ<i>H</i> / <i>T</i>) = <i>R</i> ln <i>K</i><br/>"
                   "provides a fundamental explanation for the effect of temperature and catalysts on equilibrium that Le Chatelier's principle cannot provide.<br/>"
                   "In your answer, you should include:<br/>"
                   "• an explanation of how an increase in temperature changes Δ<i>S</i><sub>surroundings</sub> for both exothermic and endothermic reactions<br/>"
                   "• a deduction of how this temperature change affects Δ<i>S</i><sub>total</sub> and consequently the equilibrium constant <i>K</i><br/>"
                   "• a rigorous thermodynamic explanation of why adding a catalyst changes the rate of reaction but CANNOT change the value of <i>K</i> or the equilibrium yield.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> In Reaction 2, the brown gas NO<sub>2</sub> is produced from colorless N<sub>2</sub>O<sub>4</sub>.<br/>"
                   "A sealed syringe containing an equilibrium mixture at 20 °C is placed into hot water at 80 °C.<br/>"
                   "Describe the color change observed and explain the thermodynamic driving force for this change.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Chemical engineers designing Haber process plants use an operating temperature of approx 450 °C (723 K).<br/>"
                   "Explain the economic and thermodynamic rationale for selecting this temperature, resolving the conflict between equilibrium yield (thermodynamics) and reaction velocity (kinetics).", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — BRØNSTED-LOWRY ACID-BASE EQUILIBRIA & NON-AQUEOUS SOLVENTS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;The Brønsted-Lowry concept provides a comprehensive framework for understanding proton transfer reactions in both aqueous and non-aqueous media.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> For each of the following reactions, identify the two Brønsted-Lowry conjugate acid-base pairs:<br/>"
                   "(i) HNO<sub>2</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; NO<sub>2</sub><sup>-</sup>(aq) &nbsp;+&nbsp; H<sub>3</sub>O<sup>+</sup>(aq)<br/>"
                   "(ii) NH<sub>3</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>SO<sub>4</sub>(aq) &nbsp;&lt;=&gt;&nbsp; NH<sub>4</sub><sup>+</sup>(aq) &nbsp;+&nbsp; HSO<sub>4</sub><sup>-</sup>(aq)", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The hydrogencarbonate ion, HCO<sub>3</sub><sup>-</sup>, is amphiprotic.<br/>"
                   "(i) Write an equation showing HCO<sub>3</sub><sup>-</sup> acting as a Brønsted-Lowry acid in water.<br/>"
                   "(ii) Write an equation showing HCO<sub>3</sub><sup>-</sup> acting as a Brønsted-Lowry base in water.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> In pure liquid ammonia, ammonium chloride, NH<sub>4</sub>Cl, behaves as an acid, while sodium amide, NaNH<sub>2</sub>, behaves as a base.<br/>"
                   "(i) Write the autoionisation equilibrium equation for liquid ammonia.<br/>"
                   "(ii) Write an ionic equation for the neutralisation reaction between NH<sub>4</sub><sup>+</sup> and NH<sub>2</sub><sup>-</sup> in liquid ammonia.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(PageBreak())

    # Question 35 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> When pure nitric acid is dissolved in concentrated sulfuric acid (as in the preparation of nitrating mixtures for benzene electrophilic substitution), the following equilibrium is established:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; HNO<sub>3</sub> &nbsp;+&nbsp; 2H<sub>2</sub>SO<sub>4</sub> &nbsp;&lt;=&gt;&nbsp; NO<sub>2</sub><sup>+</sup> &nbsp;+&nbsp; H<sub>3</sub>O<sup>+</sup> &nbsp;+&nbsp; 2HSO<sub>4</sub><sup>-</sup><br/>"
                   "Identify which reactant acts as a Brønsted-Lowry base and explain why.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Water self-ionises according to: 2H<sub>2</sub>O(l) &lt;=&gt; H<sub>3</sub>O<sup>+</sup>(aq) + OH<sup>-</sup>(aq) (Δ<i>H</i>° = +57.0 kJ mol<sup>-1</sup>).<br/>"
                   "At 298 K, <i>K</i><sub>w</sub> = 1.00 × 10<sup>-14</sup> mol<sup>2</sup> dm<sup>-6</sup>.<br/>"
                   "At 373 K (100 °C), <i>K</i><sub>w</sub> = 5.13 × 10<sup>-13</sup> mol<sup>2</sup> dm<sup>-6</sup>.<br/>"
                   "Calculate the pH of pure neutral water at 100 °C. Explain why pure water at 100 °C is still strictly neutral despite having a pH below 7.0.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("pH of water at 100 °C = .....................................................................................", S['ans_prompt']))
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
    # QUESTION 36 (15 MARKS) — OCEAN ACIDIFICATION & CORAL REEF CALCIFICATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;The absorption of anthropogenic carbon dioxide by the world's oceans drives ocean acidification through a cascade of chemical equilibria:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("<b>Equilibrium 1:</b> CO<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; CO<sub>2</sub>(aq)<br/>"
                           "<b>Equilibrium 2:</b> CO<sub>2</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; H<sub>2</sub>CO<sub>3</sub>(aq)<br/>"
                           "<b>Equilibrium 3:</b> H<sub>2</sub>CO<sub>3</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; HCO<sub>3</sub><sup>-</sup>(aq) &nbsp;+&nbsp; H<sub>3</sub>O<sup>+</sup>(aq)<br/>"
                           "<b>Equilibrium 4:</b> HCO<sub>3</sub><sup>-</sup>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; CO<sub>3</sub><sup>2-</sup>(aq) &nbsp;+&nbsp; H<sub>3</sub>O<sup>+</sup>(aq)<br/>"
                           "<b>Equilibrium 5:</b> Ca<sup>2+</sup>(aq) &nbsp;+&nbsp; CO<sub>3</sub><sup>2-</sup>(aq) &nbsp;&lt;=&gt;&nbsp; CaCO<sub>3</sub>(s) (aragonite)", S['q_equation']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Since the Industrial Revolution, atmospheric <i>p</i>(CO<sub>2</sub>) has risen from 280 ppm (2.80 × 10<sup>-4</sup> atm) to 420 ppm (4.20 × 10<sup>-4</sup> atm).<br/>"
                   "Using Le Chatelier's principle, explain how this 50 % increase in atmospheric CO<sub>2</sub> shifts Equilibria 1, 2, and 3, and state the effect on oceanic [H<sub>3</sub>O<sup>+</sup>] and pH.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The added H<sub>3</sub>O<sup>+</sup> ions react with carbonate ions according to the net neutralization:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; H<sub>3</sub>O<sup>+</sup>(aq) + CO<sub>3</sub><sup>2-</sup>(aq) &lt;=&gt; HCO<sub>3</sub><sup>-</sup>(aq) + H<sub>2</sub>O(l)<br/>"
                   "Explain why ocean acidification causes the concentration of dissolved carbonate ions, [CO<sub>3</sub><sup>2-</sup>(aq)], to DECREASE rather than increase.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Marine corals and molluscs build exoskeletons of aragonite, CaCO<sub>3</sub>(s). The solubility product of aragonite is <i>K</i><sub>sp</sub> = 6.0 × 10<sup>-9</sup> mol<sup>2</sup> dm<sup>-6</sup>.<br/>"
                   "The saturation state, Ω, is defined as: &nbsp;&nbsp; Ω = [Ca<sup>2+</sup>][CO<sub>3</sub><sup>2-</sup>] / <i>K</i><sub>sp</sub><br/>"
                   "In pre-industrial surface seawater, [Ca<sup>2+</sup>] = 0.0102 mol dm<sup>-3</sup> and [CO<sub>3</sub><sup>2-</sup>] = 2.40 × 10<sup>-4</sup> mol dm<sup>-3</sup>.<br/>"
                   "(i) Calculate the pre-industrial saturation state, Ω.<br/>"
                   "(ii) If ocean acidification lowers [CO<sub>3</sub><sup>2-</sup>] to 5.0 × 10<sup>-7</sup> mol dm<sup>-3</sup>, calculate the new value of Ω and predict whether coral skeletons will form or dissolve.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Suggest one ecological and one economic consequence of the collapse of marine calcifying ecosystems.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — HABER-BOSCH OPTIMISATION & RECYCLE LOOPS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;In an industrial Haber ammonia synthesis loop:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>(g) &nbsp;+&nbsp; 3H<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NH<sub>3</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -92.2 kJ mol<sup>-1</sup> &nbsp;|&nbsp; Δ<i>S</i>°<sub>system</sub> = -198.8 J K<sup>-1</sup> mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate Δ<i>S</i><sub>total</sub> and <i>K</i><sub>p</sub> at 298 K (25 °C). (<i>R</i> = 8.314 J mol<sup>-1</sup> K<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (298 K) = ................................... J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>p</sub> (298 K) = ................................... atm<sup>-2</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate Δ<i>S</i><sub>total</sub> and <i>K</i><sub>p</sub> at 723 K (450 °C), the typical operating temperature of the reactor.<br/>"
                   "Assume Δ<i>H</i>° and Δ<i>S</i>°<sub>system</sub> remain constant.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> (723 K) = ................................... J K<sup>-1</sup> mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>p</sub> (723 K) = ................................... atm<sup>-2</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 37 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Compare your values of <i>K</i><sub>p</sub> at 298 K and 723 K.<br/>"
                   "Explain why the industrial synthesis is operated at 450 °C, where <i>K</i><sub>p</sub> is roughly ten orders of magnitude smaller than at room temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Under industrial conditions (450 °C, 200 atm), only approximately 15 % of the feed gas is converted to ammonia on a single pass through the catalytic reactor.<br/>"
                   "Describe the industrial engineering loop used to achieve an overall 98 % conversion of the nitrogen and hydrogen feed gases, explaining how ammonia is separated from unreacted gases.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 8 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Only temperature changes the numerical value of equilibrium constants (Kc and Kp).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("For exothermic reactions, increasing T decreases Kp and shifts equilibrium to the left.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Fundamental relation: ΔS_total = R * ln K => ln K = ΔS_total / R.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("When K = 1.0, ln K = 0, so ΔS_total = R * 0 = 0 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ln K = 57.5 / 8.314 = 6.916 => K = e^(6.916) = 1.008 x 10^3 ≈ 1.01 x 10^3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Brønsted-Lowry acid is a proton (H+) donor; base is a proton acceptor.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("HSO4- and SO4^2- differ by exactly one proton (H+), forming a conjugate acid-base pair.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("HCO3- can donate H+ to form CO3^2- and accept H+ to form H2CO3, so it is amphiprotic.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kp depends strictly on temperature via ΔS_total = R ln K; pressure alters position, not Kp.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("van 't Hoff plot: slope = -ΔH° / R; for ΔH° > 0, the slope is negative.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("In 2NH3 <=> NH4+ + NH2-, NH3 loses a proton to form NH2- (conjugate base).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("CH3COOH accepts a proton from H2SO4 to become CH3COOH2+, acting as a Brønsted base.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Halving V doubles all partial pressures: Qp = (2p_NO2)^2 / (2p_N2O4) = 4/2 * Kp = 2 Kp.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("A massive K (10^12) indicates almost 100% conversion to products at equilibrium.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Conjugate acid forms by adding one proton (H+) to H2PO4-, yielding H3PO4.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("For endothermic (ΔH > 0), ΔS_surr = -ΔH/T is negative; higher T makes it less negative, increasing ΔS_total and K.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔS_total = R * ln Kp = 8.314 * ln(3.0 x 10^4) = 8.314 * 10.309 = +85.7 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("CH3COO- accepts a proton from water to form CH3COOH and OH- (hydrolysis/alkaline).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Thermodynamic properties (state functions) depend only on initial and final states, not path.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Water donates a proton to NH3, acting as a Brønsted-Lowry acid.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Slope = -ΔH° / R; when ΔH° is negative (-100 kJ), -(-100)/R is positive, so slope is positive.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("BF3 has no protons to donate (it is a Lewis acid, not a Brønsted-Lowry acid).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("HNO3 accepts a proton from H2SO4 to form H2NO3+ (which loses water to form NO2+), so HNO3 acts as a base.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("When ΔS_total < 0, ln K = ΔS_total / R is negative, so 0 < K < 1 (equilibrium favours reactants).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Exothermic reaction: lowering T increases Kc and shifts equilibrium forward (higher H2 yield).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("NH4+ loses a proton to form ammonia, NH3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kp depends ONLY on temperature; doubling pressure leaves Kp unchanged at 10.0 atm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Definition of amphiprotic: can both donate H+ and accept H+.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_total = R * ln K = 8.314 * ln(2.5 x 10^-5) = 8.314 * (-10.597) = -88.1 J K^-1 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("HClO4 donates a proton to become ClO4- (its conjugate base).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Van 't Hoff Plot: Methanol Synthesis (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Axes labeled ln Kp on y-axis, 1/T / 10^-3 K^-1 on x-axis [1]<br/>"
         "• Straight line with positive slope (rising from left to right as 1/T increases) [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Gradient = Δ(ln Kp) / Δ(1/T) = (-5.08 - (-14.15)) / [(2.00 - 1.43) x 10^-3 K^-1] [1]<br/>"
         "• = (+9.07) / (0.57 x 10^-3 K^-1) = +15 912 K (accept +15 800 to +16 100 K) [1]<br/>"
         "• Sign is POSITIVE; units are Kelvin (K) [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Gradient = -ΔH° / R => ΔH° = -Gradient * R [1]<br/>"
         "• ΔH° = -(+15 912 K) * (8.314 J mol^-1 K^-1) = -132 300 J mol^-1 [1]<br/>"
         "• = -132.3 kJ mol^-1 (must include minus sign; accept -131 to -134 kJ mol^-1) [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• At 500 K: 1/T = 2.00 x 10^-3 K^-1; ln Kp = -5.08 [1]<br/>"
         "• -5.08 = (-ΔH° / R)*(1/T) + (ΔS°_sys / R) = (15 912 * 2.00 x 10^-3) + (ΔS°_sys / 8.314) [1]<br/>"
         "• -5.08 = 31.824 + (ΔS°_sys / 8.314) => ΔS°_sys / 8.314 = -5.08 - 31.824 = -36.904 [1]<br/>"
         "• ΔS°_sys = -36.904 * 8.314 = -306.8 J K^-1 mol^-1 (accept -305 to -310 J K^-1 mol^-1) [1].<br/><br/>"
         "<b>(e) [6 Marks]</b><br/>"
         "• 3 moles of gas reactants (1 CO + 2 H2) produce 1 mole of gas product (CH3OH) [2]<br/>"
         "• Substantial loss of translational disorder / fewer microstates makes ΔS°_system negative [1]<br/>"
         "• ΔS_total = ΔS_system - (ΔH° / T). Because ΔH° is negative, -ΔH°/T is positive (ΔS_surr > 0) [1]<br/>"
         "• As T increases, ΔS_surr decreases rapidly, making ΔS_total less positive (more negative) [1]<br/>"
         "• Because ln Kp = ΔS_total / R, Kp decreases exponentially with increasing temperature [1]."),

        ("Question 32: Mathematical Proof: Pressure Does Not Alter Kp (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Kp = p(NO2)^2 / p(N2O4) [1]<br/>"
         "• Kp = (0.400)^2 / (0.800) = 0.160 / 0.800 = 0.200 [1]<br/>"
         "• Units: atm (or 20.3 kPa if converted) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• (i) Halving volume doubles all concentrations/pressures: p(N2O4) = 1.600 atm; p(NO2) = 0.800 atm [2]<br/>"
         "• (ii) Qp = (p_NO2)^2 / p_N2O4 = (0.800)^2 / (1.600) = 0.640 / 1.600 = 0.400 atm [2].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Qp = 0.400 atm, which is greater than Kp = 0.200 atm (Qp = 2 Kp) [1]<br/>"
         "• Because Qp > Kp, the ratio of products to reactants is too high for equilibrium [1]<br/>"
         "• The system must shift to consume NO2 and produce N2O4 (shift to the LEFT) [1]<br/>"
         "• This decreases numerator and increases denominator until Qp returns to 0.200 atm = Kp [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Kp is a thermodynamic constant that depends solely on temperature: Kp = exp(ΔS_total / R) [1]<br/>"
         "• Compression temporarily perturbs the system away from equilibrium (Qp ≠ Kp) [1]<br/>"
         "• The position of equilibrium shifts to restore the ratio back to Kp [1]<br/>"
         "• Thus the composition changes, but the value of Kp remains strictly constant at 0.200 atm [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• For H2(g) + I2(g) <=> 2HI(g), Qp = (2p_HI)^2 / [(2p_H2)*(2p_I2)] = 4(p_HI)^2 / [4(p_H2)(p_I2)] [1]<br/>"
         "• The factor of 4 cancels out completely in numerator and denominator: Qp = Kp [1]<br/>"
         "• Because Qp remains exactly equal to Kp upon compression, no shift in equilibrium occurs [1]."),

        ("Question 33: Calculating K from Total Entropy for CaCO3 (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• ΔS°_system = S°(CaO) + S°(CO2) - S°(CaCO3) = 38.2 + 213.6 - 92.9 [1]<br/>"
         "• = +158.9 J K^-1 mol^-1 [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• ΔS_surr = -ΔH° / T = -(+178 300) / 298 = -598.32 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = +158.9 + (-598.32) = -439.42 J K^-1 mol^-1 [1]<br/>"
         "• ln Kp = ΔS_total / R = -439.42 / 8.314 = -52.853 [1]<br/>"
         "• Kp = exp(-52.853) = 1.1 x 10^-23 atm [2].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• At 1200 K: ΔS_surr = -(+178 300) / 1200 = -148.58 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = +158.9 + (-148.58) = +10.32 J K^-1 mol^-1 [1]<br/>"
         "• ln Kp = +10.32 / 8.314 = +1.2413 [1]<br/>"
         "• Kp = exp(+1.2413) = 3.46 atm (accept 3.4 to 3.5 atm) [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Kp = p(CO2) (solids omitted) [1]<br/>"
         "• Since Kp = 3.46 atm at 1200 K, the equilibrium partial pressure p(CO2) is 3.46 atm [2].<br/><br/>"
         "<b>(e) [4 Marks]</b><br/>"
         "• Blowing air continuously sweeps away CO2 gas, keeping p(CO2) effectively near zero [1]<br/>"
         "• Qp = p(CO2) < Kp at all times [1]<br/>"
         "• The equilibrium is continuously driven to the right according to Le Chatelier's principle [1]<br/>"
         "• 100% conversion is achieved without needing excessively high temperatures [1]."),

        ("Question 34: *Level of Response — Le Chatelier vs ΔS_total = R ln K (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Forward reaction is exothermic (releases heat) [1]<br/>"
         "• By Le Chatelier, increasing temperature causes system to shift in endothermic direction (reverse) to absorb added heat [1]<br/>"
         "• Yield of ammonia decreases [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive comparison between Le Chatelier and thermodynamics. Explains that Le Chatelier predicts direction of shift phenomenologically, but ΔS_total = R ln K provides quantitative, fundamental explanation. Explains that ΔS_surr = -ΔH/T. For exothermic reactions (ΔH < 0), higher T makes positive ΔS_surr smaller, reducing ΔS_total, which reduces K (fewer products). For endothermic (ΔH > 0), higher T makes negative ΔS_surr less negative, increasing ΔS_total, which increases K. Rigorous catalyst explanation: A catalyst lowers activation energy for BOTH forward and reverse pathways equally, speeding up both rates by identical factors. ΔH and ΔS_system are state functions that depend ONLY on reactant and product identities, not mechanism. Thus ΔS_surr and ΔS_total are completely unaffected by catalyst, meaning K and equilibrium yield cannot change.<br/>"
         "• Level 2 (3-4 marks): Correctly links ΔS_surroundings to temperature and explains catalyst effect on activation energy vs state functions with minor gaps.<br/>"
         "• Level 1 (1-2 marks): Descriptive restatement of Le Chatelier with superficial mention of entropy.<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Observation: Mixture turns darker brown [1]<br/>"
         "• Decomposition is endothermic (ΔH = +57 kJ mol^-1) [1]<br/>"
         "• Increasing T makes negative ΔS_surr less negative, increasing ΔS_total and Kp [1]<br/>"
         "• Equilibrium shifts right, producing more brown NO2 gas [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• Thermodynamic penalty: At 450 °C, Kp is small because reaction is exothermic, limiting single-pass yield to ~15% [2]<br/>"
         "• Kinetic requirement: At room temperature, rate is virtually zero because breaking the N≡N triple bond has a huge activation energy (945 kJ mol^-1) [2]<br/>"
         "• Economic compromise: 450 °C with iron catalyst gives an acceptable reaction velocity to reach equilibrium in seconds; unreacted gases are recycled [1]."),

        ("Question 35: Brønsted-Lowry Equilibria & Non-Aqueous Systems (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• (i) Pair 1: HNO2 (acid) / NO2- (base) [1]; Pair 2: H3O+ (acid) / H2O (base) [1]<br/>"
         "• (ii) Pair 1: H2SO4 (acid) / HSO4- (base) [1]; Pair 2: NH4+ (acid) / NH3 (base) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• (i) Acid: HCO3-(aq) + H2O(l) <=> CO3^2-(aq) + H3O+(aq) [2]<br/>"
         "• (ii) Base: HCO3-(aq) + H2O(l) <=> H2CO3(aq) + OH-(aq) [2].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• (i) Autoionisation: 2NH3(l) <=> NH4+(am) + NH2-(am) [2]<br/>"
         "• (ii) Neutralisation: NH4+ + NH2- —> 2NH3 [2].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Nitric acid, HNO3, acts as a Brønsted-Lowry base [1]<br/>"
         "• H2SO4 is a much stronger acid than HNO3 and forces HNO3 to accept a proton on its -OH group (forming H2NO3+) [1]<br/>"
         "• H2NO3+ subsequently loses water to generate the electrophilic nitronium ion, NO2+ [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• In pure water, [H+] = [OH-] = sqrt(Kw) = sqrt(5.13 x 10^-13) = 7.16 x 10^-7 mol dm^-3 [1]<br/>"
         "• pH = -log[H+] = -log(7.16 x 10^-7) = 6.14 [1]<br/>"
         "• Water is strictly neutral because [H+] equals [OH-]; neutral pH is 6.14 at 100 °C because dissociation is endothermic [1]."),

        ("Question 36: Ocean Acidification & Coral Calcification (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Rising atmospheric p(CO2) shifts Equilibrium 1 to the right (more CO2 dissolves) [1]<br/>"
         "• Increased [CO2(aq)] shifts Equilibrium 2 right to form more carbonic acid, H2CO3 [1]<br/>"
         "• Increased [H2CO3] shifts Equilibrium 3 right, releasing more H3O+ ions [1]<br/>"
         "• [H3O+] increases, causing seawater pH to fall (ocean acidification) [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Added H3O+ ions react with basic carbonate ions: H3O+ + CO3^2- -> HCO3- + H2O [1]<br/>"
         "• This neutralisation consumes carbonate ions, shifting Equilibrium 4 to the left [1]<br/>"
         "• Consequently, the concentration of free carbonate ions [CO3^2-] decreases substantially [1].<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• (i) Ω = (0.0102 * 2.40 x 10^-4) / (6.0 x 10^-9) = (2.448 x 10^-6) / (6.0 x 10^-9) = 408 (strongly supersaturated, Ω >> 1) [2]<br/>"
         "• (ii) New Ω = (0.0102 * 5.0 x 10^-7) / (6.0 x 10^-9) = (5.10 x 10^-9) / (6.0 x 10^-9) = 0.85 [2]<br/>"
         "• Since Ω < 1, seawater is undersaturated with respect to aragonite; existing coral skeletons spontaneously dissolve [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Ecological: Loss of marine biodiversity and habitats for 25% of all fish species supported by reefs [1]<br/>"
         "• Economic: Collapse of commercial coastal fisheries and loss of ecotourism revenue [2]."),

        ("Question 37: Haber-Bosch Thermodynamic Loop Optimisation (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• ΔS_surr = -(-92 200) / 298 = +309.40 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = -198.8 + 309.40 = +110.60 J K^-1 mol^-1 [1]<br/>"
         "• ln Kp = 110.60 / 8.314 = 13.303 [1]<br/>"
         "• Kp = exp(13.303) = 6.0 x 10^5 atm^-2 (accept 5.8 x 10^5 to 6.8 x 10^5) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• At 723 K: ΔS_surr = -(-92 200) / 723 = +127.52 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = -198.8 + 127.52 = -71.28 J K^-1 mol^-1 [1]<br/>"
         "• ln Kp = -71.28 / 8.314 = -8.5735 [1]<br/>"
         "• Kp = exp(-8.5735) = 1.9 x 10^-4 atm^-2 (accept 1.4 x 10^-4 to 2.0 x 10^-4) [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Kp at 723 K is roughly 10^9 times smaller than at 298 K [1]<br/>"
         "• At 298 K, reaction rate is imperceptibly slow due to high activation energy of N≡N bond [1]<br/>"
         "• High temperature (450 °C) ensures rapid kinetic collision rate to achieve equilibrium in seconds [1]<br/>"
         "• High pressure (200 atm) partially compensates for the thermodynamic penalty by shifting equilibrium right [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Gases leaving reactor are cooled under pressure, liquefying ammonia (bp -33 °C) while N2 and H2 remain gases [1]<br/>"
         "• Liquid ammonia is tapped off [1]<br/>"
         "• Unreacted N2 and H2 are recycled continuously back into the catalyst bed, achieving overall 98% yield [1].")
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
    print(f"[SUCCESS] Week 8 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")


if __name__ == '__main__':
    build_pdf()
