"""
build_usman_week9_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 9 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 14A.2: Hydrogen Ion Concentration and the pH Scale (Strong Acids, Diprotic Acids, Dilutions)
  - 14A.3: Ionic Product of Water, Kw (Thermodynamics of Auto-ionisation, Neutrality at Non-298K, Strong Alkalis)
  - 14A.4: Weak Acids, Ka and pKa (Ostwald's Dilution Law, Approximations Breakdown, Quadratic Solutions & Inductive Effects)

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
    "Usman_Edexcel_Chem_U4_Week9_150M_Challenging_Quiz.pdf"
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
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="[H+]^2 / 10^-5 mol^2 dm^-6", x_label="[HA] / mol dm^-3"):
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

        ox = 50
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
        self.canv.translate(ox - 22, oy + ax_h / 2)
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 9 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 9 (150 Marks)...")
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
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W09</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 9 ASSESSMENT: STRONG & WEAK ACIDS, pH SCALE, Kw & Ka EQUILIBRIA</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 9 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 14A.2: Hydrogen Ion Concentration and the pH Scale (Strong Acids & Bases, Dilutions)<br/>Topic 14A.3: Ionic Product of Water, Kw (Thermodynamics, Neutrality at Varying T, Strong Alkalis)<br/>Topic 14A.4: Weak Acids, Ka and pKa (Ostwald's Dilution Law, Approximations Breakdown, Quadratic Solutions & Inductive Effects)", S['edx_meta'])],
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
        ("What is the concentration of hydrogen ions, [H+], in an aqueous hydrochloric acid solution of pH 2.60 at 298 K?",
         [("A", "2.51 x 10^-3 mol dm^-3"),
          ("B", "3.98 x 10^-3 mol dm^-3"),
          ("C", "2.60 x 10^-3 mol dm^-3"),
          ("D", "1.58 x 10^-2 mol dm^-3")]),

        ("Assuming complete dissociation of both protons, what is the pH of a 0.0250 mol dm^-3 aqueous sulfuric acid solution, H2SO4(aq), at 298 K?",
         [("A", "1.60"),
          ("B", "1.30"),
          ("C", "1.00"),
          ("D", "2.00")]),

        ("A 10.0 cm^3 sample of 0.100 mol dm^-3 hydrochloric acid is diluted with distilled water to a final volume of 1000 cm^3. What is the pH of the resulting solution at 298 K?",
         [("A", "2.00"),
          ("B", "3.00"),
          ("C", "4.00"),
          ("D", "5.00")]),

        # Page 3: Q4, Q5, Q6
        ("What are the units of the ionic product of water, Kw = [H+][OH-]?",
         [("A", "mol dm^-3"),
          ("B", "mol^2 dm^-6"),
          ("C", "dm^6 mol^-2"),
          ("D", "Dimensionless")]),

        ("The self-ionisation of water, H2O(l) <==> H+(aq) + OH-(aq), has a standard enthalpy change of ΔH° = +57.1 kJ mol^-1. As the temperature of pure water increases, how do Kw and the neutral pH change?",
         [("A", "Kw increases; neutral pH increases"),
          ("B", "Kw decreases; neutral pH decreases"),
          ("C", "Kw increases; neutral pH decreases"),
          ("D", "Kw remains constant; neutral pH remains 7.00")]),

        ("Barium hydroxide, Ba(OH)2, is fully dissociated in aqueous solution. What is the pH of a 0.0150 mol dm^-3 Ba(OH)2 solution at 298 K? (Kw = 1.00 x 10^-14 mol^2 dm^-6)",
         [("A", "12.18"),
          ("B", "12.48"),
          ("C", "11.82"),
          ("D", "13.00")]),

        # Page 4: Q7, Q8, Q9
        ("Which expression represents the acid dissociation constant, Ka, for propanoic acid, CH3CH2COOH?",
         [("A", "Ka = [CH3CH2COO-][H+] / [CH3CH2COOH]"),
          ("B", "Ka = [CH3CH2COOH] / ([CH3CH2COO-][H+])"),
          ("C", "Ka = [CH3CH2COO-][H+]"),
          ("D", "Ka = [CH3CH2COO-][OH-] / [CH3CH2COOH]")]),

        ("A weak monobasic acid X has Ka = 2.0 x 10^-5 mol dm^-3, while acid Y has Ka = 5.0 x 10^-4 mol dm^-3. Which statement comparing these acids is correct?",
         [("A", "Acid X is stronger than acid Y and has a lower pKa"),
          ("B", "Acid X is weaker than acid Y and has a higher pKa"),
          ("C", "Acid X is stronger than acid Y and has a higher pKa"),
          ("D", "Acid X is weaker than acid Y and has a lower pKa")]),

        ("What is the pH of a 0.120 mol dm^-3 ethanoic acid solution at 298 K, given that Ka = 1.75 x 10^-5 mol dm^-3? (Assume standard approximations apply)",
         [("A", "2.84"),
          ("B", "2.34"),
          ("C", "3.12"),
          ("D", "4.76")]),

        # Page 5: Q10, Q11, Q12
        ("When calculating the pH of a weak monobasic acid HA using [H+] = sqrt(Ka * c), one assumption is that [HA]eq ≈ c. Under which condition does this assumption break down most significantly?",
         [("A", "When the acid is very concentrated and Ka is very small (Ka < 10^-6)"),
          ("B", "When the acid is moderately strong (Ka > 10^-2) or the solution is very dilute"),
          ("C", "When the temperature is maintained strictly at 298 K"),
          ("D", "When the conjugate base forms insoluble precipitates")]),

        ("A second fundamental assumption made in deriving [H+] = sqrt(Ka * c) is that [H+]eq ≈ [A-]eq. What source of hydrogen ions is neglected by this assumption?",
         [("A", "Hydrogen ions produced by the auto-ionisation of water"),
          ("B", "Hydrogen ions absorbed by atmospheric carbon dioxide"),
          ("C", "Hydrogen ions provided by the undissociated acid HA"),
          ("D", "Hydrogen ions generated by redox disproportionation")]),

        ("At 60 °C (333 K), the ionic product of water is Kw = 9.31 x 10^-14 mol^2 dm^-6. What is the pH of pure water at 60 °C, and is the water acidic, neutral, or alkaline?",
         [("A", "pH = 6.52; water is slightly acidic"),
          ("B", "pH = 6.52; water is strictly neutral"),
          ("C", "pH = 7.00; water is strictly neutral"),
          ("D", "pH = 7.48; water is slightly alkaline")]),

        # Page 6: Q13, Q14, Q15
        ("Consider the following four carboxylic acids: (I) Ethanoic acid, (II) Chloroethanoic acid, (III) Dichloroethanoic acid, (IV) Trichloroethanoic acid. What is the correct order of INCREASING acid strength (lowest Ka to highest Ka)?",
         [("A", "I < II < III < IV"),
          ("B", "IV < III < II < I"),
          ("C", "I < III < II < IV"),
          ("D", "II < I < III < IV")]),

        ("2-chlorobutanoic acid is a significantly stronger acid than 4-chlorobutanoic acid. What is the primary physical reason for this difference?",
         [("A", "The inductive electron-withdrawing effect of chlorine decreases with distance from the carboxyl group"),
          ("B", "4-chlorobutanoic acid forms stronger intermolecular hydrogen bonds"),
          ("C", "The C-Cl bond in 2-chlorobutanoic acid is ionic rather than covalent"),
          ("D", "2-chlorobutanoic acid has a higher molar mass than 4-chlorobutanoic acid")]),

        ("A 0.0500 mol dm^-3 solution of methanoic acid, HCOOH, has Ka = 1.80 x 10^-4 mol dm^-3 at 298 K. What is the degree of dissociation, α, of methanoic acid in this solution?",
         [("A", "0.0180"),
          ("B", "0.0600"),
          ("C", "0.120"),
          ("D", "0.00300")]),

        # Page 7: Q16, Q17, Q18
        ("If a solution of a weak monobasic acid HA is diluted by a factor of 10 with distilled water, how does the pH change (assuming the approximation [H+] = sqrt(Ka * c) remains valid)?",
         [("A", "Increases by exactly 1.0 pH unit"),
          ("B", "Increases by approximately 0.5 pH unit"),
          ("C", "Decreases by approximately 0.5 pH unit"),
          ("D", "Remains completely unchanged")]),

        ("At 298 K, an aqueous solution of sodium hydroxide has a pH of 13.40. What is the concentration of hydroxide ions, [OH-], in this solution? (Kw = 1.00 x 10^-14 mol^2 dm^-6)",
         [("A", "0.251 mol dm^-3"),
          ("B", "0.400 mol dm^-3"),
          ("C", "0.100 mol dm^-3"),
          ("D", "0.0251 mol dm^-3")]),

        ("Which of the following carboxylic acids has the SMALLEST pKa value at 298 K?",
         [("A", "Ethanoic acid (CH3COOH)"),
          ("B", "Propanoic acid (CH3CH2COOH)"),
          ("C", "Fluoroethanoic acid (CH2FCOOH)"),
          ("D", "Bromoethanoic acid (CH2BrCOOH)")]),

        # Page 8: Q19, Q20, Q21
        ("50.0 cm^3 of 0.100 mol dm^-3 HCl is mixed with 50.0 cm^3 of 0.060 mol dm^-3 NaOH at 298 K. What is the pH of the resulting mixture?",
         [("A", "1.40"),
          ("B", "1.70"),
          ("C", "2.00"),
          ("D", "2.40")]),

        ("25.0 cm^3 of 0.100 mol dm^-3 barium hydroxide, Ba(OH)2, is mixed with 25.0 cm^3 of 0.150 mol dm^-3 hydrochloric acid, HCl, at 298 K. What is the pH of the resulting solution? (Kw = 1.00 x 10^-14 mol^2 dm^-6)",
         [("A", "12.00"),
          ("B", "12.40"),
          ("C", "12.70"),
          ("D", "1.60")]),

        ("At 0 °C (273 K), the ionic product of water is Kw = 1.14 x 10^-15 mol^2 dm^-6. What is the concentration of H+(aq) in pure water at 0 °C?",
         [("A", "1.00 x 10^-7 mol dm^-3"),
          ("B", "3.38 x 10^-8 mol dm^-3"),
          ("C", "1.14 x 10^-8 mol dm^-3"),
          ("D", "5.70 x 10^-8 mol dm^-3")]),

        # Page 9: Q22, Q23, Q24
        ("A weak monobasic acid has pKa = 3.75 at 298 K. What is the numerical value of its acid dissociation constant, Ka?",
         [("A", "1.78 x 10^-4 mol dm^-3"),
          ("B", "5.62 x 10^-4 mol dm^-3"),
          ("C", "1.00 x 10^-3 mol dm^-3"),
          ("D", "3.75 x 10^-4 mol dm^-3")]),

        ("Fluoroethanoic acid (pKa = 2.59) is a stronger acid than chloroethanoic acid (pKa = 2.87). What is the main explanation for this fact?",
         [("A", "Fluorine is more electronegative than chlorine, withdrawing electron density more strongly and stabilizing the carboxylate anion"),
          ("B", "The C-F bond is weaker than the C-Cl bond, making it easier to break"),
          ("C", "Fluorine has more lone pairs of electrons than chlorine"),
          ("D", "Fluoroethanoic acid has a higher boiling point than chloroethanoic acid")]),

        ("According to Ostwald's dilution law, what happens to the percentage dissociation of a weak acid when water is added to its aqueous solution at constant temperature?",
         [("A", "Percentage dissociation decreases because dilution suppresses ionisation"),
          ("B", "Percentage dissociation increases because dilution favours the side with more moles of particles"),
          ("C", "Percentage dissociation remains constant because Ka is constant"),
          ("D", "Percentage dissociation first decreases and then remains constant")]),

        # Page 10: Q25, Q26, Q27
        ("A sample of acid rain has a hydrogen ion concentration of [H+] = 4.20 x 10^-5 mol dm^-3. What is the pH of this rainwater?",
         [("A", "4.38"),
          ("B", "4.20"),
          ("C", "5.38"),
          ("D", "3.38")]),

        ("A student dissolves 0.200 g of sodium hydroxide (Mr = 40.0) in distilled water to make 250 cm^3 of solution. What is the pH of this solution at 298 K? (Kw = 1.00 x 10^-14 mol^2 dm^-6)",
         [("A", "12.00"),
          ("B", "12.30"),
          ("C", "12.70"),
          ("D", "13.00")]),

        ("A weak acid HA has Ka = 2.50 x 10^-5 mol dm^-3. At what concentration c will the acid be exactly 5.0% dissociated (α = 0.050)?",
         [("A", "9.50 x 10^-3 mol dm^-3"),
          ("B", "5.00 x 10^-3 mol dm^-3"),
          ("C", "1.00 x 10^-2 mol dm^-3"),
          ("D", "2.50 x 10^-4 mol dm^-3")]),

        # Page 11: Q28, Q29, Q30
        ("Which of the following plots will yield a straight line passing through the origin for a weak monobasic acid that obeys the approximation [H+] = sqrt(Ka * c)?",
         [("A", "pH against concentration c"),
          ("B", "[H+]^2 against concentration c"),
          ("C", "log[H+] against 1/c"),
          ("D", "[H+] against concentration c")]),

        ("The auto-ionisation of pure liquid ammonia at -50 °C is: 2NH3(l) <==> NH4+ + NH2-. In this solvent system, what is the species analogous to H3O+ in water?",
         [("A", "NH2-"),
          ("B", "NH4+"),
          ("C", "NH3"),
          ("D", "N2H4")]),

        ("A weak acid has Ka = 4.00 x 10^-2 mol dm^-3. In a 0.0400 mol dm^-3 solution, using the simplified formula [H+] = sqrt(Ka * c) gives [H+] = 0.0400 mol dm^-3 (100% dissociation). Why is this result fundamentally erroneous?",
         [("A", "The approximation [HA]eq ≈ c is invalid because significant dissociation has depleted [HA]eq"),
          ("B", "Water auto-ionisation dominates at this concentration"),
          ("C", "Ka is too small for the simplified formula to apply"),
          ("D", "The acid behaves as a strong diprotic acid in dilute solution")])
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
    # QUESTION 31 (18 MARKS) — THE pH SCALE, DIPROTIC ACIDS & MIXTURES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;The pH scale is used as a convenient measure of aqueous hydrogen ion concentration.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Define pH mathematically and explain why Soren Sorensen introduced this logarithmic definition in 1909.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Calculate the concentration of hydrogen ions, [H+], in a solution of gastric juice with a measured pH of 1.85.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: [H+] = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Sulfuric acid, H<sub>2</sub>SO<sub>4</sub>, is a diprotic acid. A standard solution is prepared by dissolving 4.904 g of pure anhydrous sulfuric acid (M<sub>r</sub> = 98.08) in distilled water to make exactly 500.0 cm^3 of solution.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Assuming that both protons completely dissociate in aqueous solution according to:<br/>"
                           "H<sub>2</sub>SO<sub>4</sub>(aq) &nbsp;&rarr;&nbsp; 2H<sup>+</sup>(aq) &nbsp;+&nbsp; SO<sub>4</sub><sup>2-</sup>(aq)<br/>"
                           "calculate the concentration of sulfuric acid and the pH of this solution.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In reality, the first proton is fully dissociated, but the hydrogensulfate ion, HSO<sub>4</sub><sup>-</sup>, is a weak acid that only partially dissociates:<br/>"
                           "HSO<sub>4</sub><sup>-</sup>(aq) &nbsp;&lt;=&gt;&nbsp; H<sup>+</sup>(aq) &nbsp;+&nbsp; SO<sub>4</sub><sup>2-</sup>(aq) &nbsp;&nbsp;&nbsp;&nbsp; K<sub>a2</sub> = 1.20 x 10^-2 mol dm^-3<br/>"
                           "Using this equilibrium constant, set up an equilibrium expression to calculate the exact concentration of H<sup>+</sup> and the true pH of this 0.100 mol dm^-3 sulfuric acid solution. Calculate the percentage error in [H+] caused by assuming complete second dissociation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7))
    story.append(Paragraph("Answer: True pH = ..................................... Percentage Error = ................................. %", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;A titration mixture is prepared by mixing 35.0 cm^3 of 0.200 mol dm^-3 nitric acid, HNO<sub>3</sub>, with 65.0 cm^3 of 0.120 mol dm^-3 potassium hydroxide, KOH, at 298 K. Calculate the pH of the final mixture. (K<sub>w</sub> = 1.00 x 10^-14 mol^2 dm^-6 at 298 K)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: Final pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;A student dilutes a 0.0500 mol dm^-3 solution of hydrochloric acid by adding 90.0 cm^3 of distilled water to 10.0 cm^3 of the acid. Explain, showing all mathematical calculations, the exact effect of this dilution on the pH.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: pH change = ..................................................... units", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — THE IONIC PRODUCT OF WATER (Kw) & STRONG BASES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Water undergoes self-ionisation to a very small extent according to the equilibrium:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; H<sub>3</sub>O<sup>+</sup>(aq) &nbsp;+&nbsp; OH<sup>-</sup>(aq) &nbsp;&nbsp;&nbsp;&nbsp; &Delta;H&deg; = +57.1 kJ mol^-1", S['q_equation']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the expression for the equilibrium constant Kc for this reaction, and explain why this expression is simplified to give the ionic product of water, Kw. State the units of Kw.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using the standard enthalpy change &Delta;H&deg; = +57.1 kJ mol^-1 and Le Chatelier's principle, explain how the value of Kw varies as the temperature of water is increased from 298 K to 373 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;At 373 K (100 &deg;C), the value of Kw is 5.13 x 10^-13 mol^2 dm^-6.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the concentration of hydrogen ions, [H+], and the pH of pure boiling water at 373 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: [H+] = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;A student states: <i>'Because the pH of pure water at 100 &deg;C is less than 7.00, boiling water is acidic and will turn blue litmus paper red.'</i><br/>"
                           "Evaluate this statement from a rigorous chemical perspective, explaining why pure water remains strictly neutral at all temperatures.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Barium hydroxide, Ba(OH)<sub>2</sub>, is a strong base that dissociates completely into Ba<sup>2+</sup> and 2OH<sup>-</sup> ions in aqueous solution.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the pH at 298 K of a solution prepared by dissolving 2.142 g of anhydrous Ba(OH)<sub>2</sub> (M<sub>r</sub> = 171.3) in distilled water to make exactly 250.0 cm^3 of solution. (K<sub>w</sub> = 1.00 x 10^-14 mol^2 dm^-6 at 298 K)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the volume of distilled water that must be added to 50.0 cm^3 of the barium hydroxide solution prepared in (c)(i) to lower its pH to exactly 12.00 at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Volume of water = ..................................................... cm^3", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — WEAK ACIDS: Ka, pKa & QUADRATIC DERIVATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Ethanoic acid, CH<sub>3</sub>COOH, and chloroethanoic acid, CH<sub>2</sub>ClCOOH, are weak monobasic acids.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the chemical equation for the dissociation of ethanoic acid in aqueous solution and write the expression for its acid dissociation constant, Ka.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;A 0.150 mol dm^-3 solution of ethanoic acid has a measured pH of 2.79 at 298 K. Calculate the values of Ka and pKa for ethanoic acid at this temperature.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Ka = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pKa = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In deriving the simplified expression [H+] = sqrt(Ka * c), two approximations are made:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Approximation 1: [H+]<sub>eq</sub> &approx; [A-]<sub>eq</sub><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Approximation 2: [HA]<sub>eq</sub> &approx; [HA]<sub>initial</sub> = c<br/>"
                           "Explain the chemical justification for each approximation and state the conditions under which Approximation 2 becomes invalid.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Dichloroethanoic acid, CHCl<sub>2</sub>COOH, has Ka = 3.32 x 10^-2 mol dm^-3 at 298 K. Consider a 0.0500 mol dm^-3 solution of this acid.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the value of [H+] and the pH using the simplified formula [H+] = sqrt(Ka * c).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: [H+] = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;By setting up and solving the exact quadratic equilibrium expression without making Approximation 2:<br/>"
                           "Ka = [H+]^2 / (c - [H+])<br/>"
                           "calculate the true concentration of H+ and the true pH of this solution.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: True [H+] = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; True pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the percentage error in [H+] caused by using the simplified formula instead of the quadratic expression, and explain why this acid exhibits such a large deviation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Percentage error = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — DEGREE OF DISSOCIATION (α) & INDUCTIVE EFFECTS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;The degree of dissociation, &alpha;, represents the fraction of acid molecules that have ionised in solution.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;For a weak monobasic acid HA with initial concentration c mol dm^-3 and degree of dissociation &alpha;, show that the acid dissociation constant can be expressed as:<br/>"
                           "Ka = (c * &alpha;^2) / (1 - &alpha;)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Deduce Ostwald's approximation &alpha; &approx; sqrt(Ka / c) when &alpha; &lt;&lt; 1. Using this expression, explain why diluting an aqueous weak acid solution increases its percentage ionization.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A 0.0200 mol dm^-3 solution of methanoic acid, HCOOH, is found to be 8.65% dissociated (&alpha; = 0.0865) at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the values of Ka and pKa for methanoic acid using the exact Ostwald expression.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Ka = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pKa = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the degree of dissociation and the pH when this methanoic acid solution is diluted 100-fold to a concentration of 2.00 x 10^-4 mol dm^-3 at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: &alpha; = ........................................ &nbsp;&nbsp;&nbsp;&nbsp; pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The table below lists the pKa values of five substituted carboxylic acids at 298 K:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    acid_table = [
        [Paragraph("<b>Acid</b>", S['tbl_th']), Paragraph("<b>Formula</b>", S['tbl_th']), Paragraph("<b>pKa at 298 K</b>", S['tbl_th'])],
        [Paragraph("Ethanoic acid", S['tbl_td_l']), Paragraph("CH<sub>3</sub>COOH", S['tbl_td']), Paragraph("4.76", S['tbl_td'])],
        [Paragraph("Propanoic acid", S['tbl_td_l']), Paragraph("CH<sub>3</sub>CH<sub>2</sub>COOH", S['tbl_td']), Paragraph("4.87", S['tbl_td'])],
        [Paragraph("Fluoroethanoic acid", S['tbl_td_l']), Paragraph("CH<sub>2</sub>FCOOH", S['tbl_td']), Paragraph("2.59", S['tbl_td'])],
        [Paragraph("Chloroethanoic acid", S['tbl_td_l']), Paragraph("CH<sub>2</sub>ClCOOH", S['tbl_td']), Paragraph("2.87", S['tbl_td'])],
        [Paragraph("Trichloroethanoic acid", S['tbl_td_l']), Paragraph("CCl<sub>3</sub>COOH", S['tbl_td']), Paragraph("0.65", S['tbl_td'])],
    ]
    t_acids = Table(acid_table, colWidths=[5.5*cm, 5.5*cm, 4.0*cm])
    t_acids.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_acids)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why propanoic acid is a weaker acid than ethanoic acid by referring to the electronic inductive effect of the alkyl group.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why fluoroethanoic acid is a stronger acid than chloroethanoic acid, and why trichloroethanoic acid has a much lower pKa than chloroethanoic acid.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — EXPERIMENTAL DETERMINATION OF Ka (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;A research student investigated the dissociation constant of an unknown crystalline weak organic acid, X. A mass of 1.832 g of solid acid X was dissolved in distilled water and made up to exactly 250.0 cm^3 in a volumetric flask.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;The molar mass of acid X was previously determined by sodium hydroxide titration to be 122.1 g mol^-1. Calculate the concentration of the acid solution in mol dm^-3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Concentration = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;The pH of this solution was measured at 298 K using a calibrated digital pH probe and found to be 2.70. Calculate the values of Ka and pKa for acid X at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Ka = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pKa = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;The student was asked to verify Ka by performing a serial dilution of acid X and measuring the pH of each solution at 298 K.<br/>"
                           "Describe a full laboratory procedure to:<br/>"
                           "- Calibrate the digital pH probe using two standard buffer solutions.<br/>"
                           "- Prepare four serial dilutions (0.0600, 0.0300, 0.0150, and 0.00750 mol dm^-3) from the original solution using a 25.0 cm^3 pipette and a 50.0 cm^3 volumetric flask.<br/>"
                           "- Measure the pH of each diluted solution systematically.<br/>"
                           "- Identify two significant experimental errors in measuring pH of weak acids and describe how to minimize them.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The student plotted a graph of [H+]^2 on the y-axis against the acid concentration [HA] on the x-axis, as shown below:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(width=AVAIL_W, height=6.0*cm, y_label="[H+]^2 / 10^-6 mol^2 dm^-6", x_label="[HA] / mol dm^-3"))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why the gradient of this straight line is equal to the acid dissociation constant, Ka.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Given that the gradient of the student's line of best fit is 6.50 x 10^-5 mol dm^-3, calculate the pH of a 0.0400 mol dm^-3 solution of this acid.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Explain why measuring the pH of an extremely dilute weak acid solution (e.g. 1.00 x 10^-6 mol dm^-3) left open to the laboratory air leads to a measured pH value noticeably lower than predicted by theory.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
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
    # QUESTION 36 (15 MARKS) — ATMOSPHERIC ACID RAIN & OCEAN CARBONATE EQUILIBRIA
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Atmospheric Chemistry and Ocean Acidification:</b><br/>"
                           "Unpolluted natural rainwater is slightly acidic due to the dissolution of atmospheric carbon dioxide. Industrial emissions of sulfur dioxide, SO<sub>2</sub>, form sulfurous acid, H<sub>2</sub>SO<sub>3</sub>, leading to acid rain. Dissolved CO<sub>2</sub> also causes ocean acidification.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Atmospheric carbon dioxide dissolves in cloud water according to Henry's law constant K<sub>H</sub> = 3.40 x 10^-2 mol dm^-3 bar^-1 at 298 K. The partial pressure of CO<sub>2</sub> in air is 4.15 x 10^-4 bar. Dissolved CO<sub>2</sub> hydrates to form carbonic acid, H<sub>2</sub>CO<sub>3</sub>:<br/>"
                           "CO<sub>2</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; H<sub>2</sub>CO<sub>3</sub>(aq) &nbsp;&nbsp;&nbsp;&nbsp; K<sub>a1</sub> = 4.47 x 10^-7 mol dm^-3", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the equilibrium concentration of dissolved carbonic acid, [H<sub>2</sub>CO<sub>3</sub>], in unpolluted rainwater at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: [H2CO3] = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using K<sub>a1</sub> = 4.47 x 10^-7 mol dm^-3, calculate the concentration of hydrogen ions and the natural pH of unpolluted rainwater.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: [H+] = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In an industrial region, rainwater contains sulfurous acid, H<sub>2</sub>SO<sub>3</sub>, at a concentration of 2.40 x 10^-3 mol dm^-3. Sulfurous acid is a moderately strong weak acid with K<sub>a1</sub> = 1.40 x 10^-2 mol dm^-3 at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical equation for the first dissociation of sulfurous acid in water.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(1)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why the approximation [H<sub>2</sub>SO<sub>3</sub>]<sub>eq</sub> &approx; 2.40 x 10^-3 mol dm^-3 CANNOT be used in this calculation. By setting up and solving the exact quadratic expression, calculate the true pH of this acid rain.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Exact pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Marine coral reefs are constructed from solid calcium carbonate, CaCO<sub>3</sub>(s), which exists in equilibrium with seawater ions:<br/>"
                           "CaCO<sub>3</sub>(s) &nbsp;&lt;=&gt;&nbsp; Ca<sup>2+</sup>(aq) &nbsp;+&nbsp; CO<sub>3</sub><sup>2-</sup>(aq)<br/>"
                           "As atmospheric CO<sub>2</sub> increases, ocean pH has dropped from 8.20 to 8.08.<br/>"
                           "Using Le Chatelier's principle and conjugate acid-base equilibria involving CO<sub>3</sub><sup>2-</sup> and HCO<sub>3</sub><sup>-</sup>, explain how ocean acidification leads to the dissolution of calcium carbonate skeletons in coral reefs.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — ASPIRIN PHARMACOKINETICS & LACTIC ACIDOSIS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Pharmaceutical Chemistry and Human Physiology:</b><br/>"
                           "Aspirin (acetylsalicylic acid, 2-acetoxybenzoic acid, C<sub>9</sub>H<sub>8</sub>O<sub>4</sub>, M<sub>r</sub> = 180.16) is a weak monobasic acid with pKa = 3.50 at body temperature (310 K). Non-ionised drug molecules (HA) diffuse across biological lipid membranes much faster than charged ions (A<sup>-</sup>).", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the chemical equation for the dissociation of acetylsalicylic acid (HA) in water and write the expression for its acid dissociation constant, Ka.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the value of Ka for aspirin at 310 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("Answer: Ka = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Gastric juice in the human stomach has a resting pH of 1.50, whereas the blood plasma in mucosal capillaries has a physiological pH of 7.40.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Using the Henderson-Hasselbalch equation:<br/>"
                           "pH = pKa + log([A-] / [HA])<br/>"
                           "calculate the ratio of ionised to non-ionised aspirin, [A-] / [HA], in the stomach fluid at pH 1.50.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: [A-] / [HA] in stomach = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the percentage of aspirin that exists in the non-ionised (HA) form in the stomach, and explain why aspirin is rapidly absorbed directly through the stomach lining into the bloodstream.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Percentage non-ionised = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;During intense anaerobic exercise, glycogen is metabolised to lactic acid (2-hydroxypropanoic acid, CH<sub>3</sub>CH(OH)COOH, pKa = 3.86).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;A muscle biopsy reveals a localized lactic acid concentration of 8.00 x 10^-3 mol dm^-3. Calculate the pH of an unbuffered aqueous solution of lactic acid at this concentration at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In a healthy human athlete, the pH of the blood drops only slightly from 7.40 to approximately 7.25 during vigorous sprinting. Explain briefly why the blood pH does not fall to the value calculated in (c)(i).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
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
        [Paragraph("<b>Physical Constant / Formula</b>", S['tbl_th']), Paragraph("<b>Symbol / Value</b>", S['tbl_th']), Paragraph("<b>SI Units</b>", S['tbl_th'])],
        [Paragraph("Gas Constant", S['tbl_td_l']), Paragraph("R = 8.31", S['tbl_td']), Paragraph("J K^-1 mol^-1", S['tbl_td'])],
        [Paragraph("Ionic Product of Water (298 K)", S['tbl_td_l']), Paragraph("Kw = 1.00 x 10^-14", S['tbl_td']), Paragraph("mol^2 dm^-6", S['tbl_td'])],
        [Paragraph("Avogadro Constant", S['tbl_td_l']), Paragraph("L = 6.02 x 10^23", S['tbl_td']), Paragraph("mol^-1", S['tbl_td'])],
        [Paragraph("Standard Temperature and Pressure", S['tbl_td_l']), Paragraph("T = 298 K, P = 100 kPa (1 bar)", S['tbl_td']), Paragraph("K, kPa", S['tbl_td'])],
        [Paragraph("pH Definition", S['tbl_td_l']), Paragraph("pH = -log10[H+(aq)]", S['tbl_td']), Paragraph("dimensionless", S['tbl_td'])],
        [Paragraph("Acid Dissociation Constant", S['tbl_td_l']), Paragraph("Ka = [H+][A-] / [HA]", S['tbl_td']), Paragraph("mol dm^-3", S['tbl_td'])],
        [Paragraph("pKa Definition", S['tbl_td_l']), Paragraph("pKa = -log10(Ka)", S['tbl_td']), Paragraph("dimensionless", S['tbl_td'])],
        [Paragraph("Henderson-Hasselbalch Equation", S['tbl_td_l']), Paragraph("pH = pKa + log10([A-] / [HA])", S['tbl_td']), Paragraph("dimensionless", S['tbl_td'])],
    ]
    t_const = Table(const_rows, colWidths=[6.0*cm, 6.0*cm, AVAIL_W - 12.0*cm])
    t_const.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_const)
    story.append(Spacer(1, 0.4 * cm))

    # Periodic Table
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 9 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("[H+] = 10^-pH = 10^-2.60 = 2.51 x 10^-3 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Diprotic acid: [H+] = 2 x 0.0250 = 0.0500 mol dm^-3 => pH = -log(0.0500) = 1.30.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Dilution factor = 1000/10 = 100. New [H+] = 0.100/100 = 1.00 x 10^-3 mol dm^-3 => pH = 3.00.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kw = [H+][OH-]; units = (mol dm^-3) x (mol dm^-3) = mol^2 dm^-6.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Endothermic: higher T shifts right, increasing Kw. Thus [H+] increases and pH = -log[H+] decreases.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[OH-] = 2 x 0.0150 = 0.0300 mol dm^-3. [H+] = 1.00x10^-14 / 0.0300 = 3.33 x 10^-13 => pH = 12.48.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Ka = [products] / [reactant] = [CH3CH2COO-][H+] / [CH3CH2COOH].", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Smaller Ka means less dissociated (weaker acid), which gives a higher pKa = -log Ka.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Ka * c) = sqrt(1.75x10^-5 * 0.120) = 1.449 x 10^-3 => pH = 2.84.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Approximation breaks down when dissociation exceeds ~5%, i.e. when Ka is large or c is very low.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Neglects the auto-ionisation of water (Kw = [H+][OH-] produces 10^-7 mol dm^-3 of H+).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Kw) = sqrt(9.31x10^-14) = 3.05 x 10^-7 => pH = 6.52. Neutral because [H+] = [OH-].", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Increasing chlorine substituents increases inductive electron withdrawal, increasing Ka.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Inductive electron-withdrawing effect operates through sigma bonds and diminishes with distance.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("α = sqrt(Ka / c) = sqrt(1.80x10^-4 / 0.0500) = sqrt(3.60x10^-3) = 0.0600 (6.0%).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Ka * c). Diluting 10x divides [H+] by sqrt(10) ≈ 3.16, so pH increases by log10(sqrt(10)) = 0.5.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("pOH = 14.00 - 13.40 = 0.60 => [OH-] = 10^-0.60 = 0.251 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Fluorine is the most electronegative halogen, so fluoroethanoic acid has the highest Ka and lowest pKa.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Moles H+ = 0.00500; moles OH- = 0.00300. Excess H+ = 0.00200 mol in 100 cm^3 => [H+] = 0.0200 => pH = 1.70.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Moles OH- = 2 x 0.025 x 0.100 = 0.00500; moles H+ = 0.00375. Excess OH- = 0.00125 in 50 cm^3 => [OH-] = 0.0250 => pOH = 1.60 => pH = 12.40.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Kw) = sqrt(1.14x10^-15) = 3.38 x 10^-8 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Ka = 10^-pKa = 10^-3.75 = 1.78 x 10^-4 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Higher electronegativity of F withdraws electron density, dispersing negative charge on carboxylate.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ostwald dilution law: α = sqrt(Ka / c). As c decreases, α increases (Le Chatelier shift).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("pH = -log(4.20 x 10^-5) = 4.38.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Moles NaOH = 0.200/40.0 = 5.00x10^-3 mol. [OH-] = 5.00x10^-3 / 0.250 = 0.0200 mol dm^-3 => pOH = 1.70 => pH = 12.30.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Ka = (c * α^2)/(1 - α) => 2.50x10^-5 = (c * 0.0025)/0.95 => c = (2.50x10^-5 * 0.95)/0.0025 = 9.50 x 10^-3 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[H+] = sqrt(Ka * c) => [H+]^2 = Ka * c. Plotting [H+]^2 against c gives a line with gradient Ka.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("NH4+ is the protonated solvent cation (solvated proton), analogous to H3O+ in water.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("When Ka is large, dissociation is high, so [HA]eq is significantly less than initial c.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: The pH Scale, Diprotic Acids & Dilutions (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• pH = -log10[H+(aq)] [1]<br/>"
         "• Sørensen introduced logarithmic scale to handle concentrations that span many orders of magnitude (from 1 to 10^-14 mol dm^-3) using manageable small numbers [1]<br/>"
         "• [H+] = 10^-1.85 = 1.41 x 10^-2 mol dm^-3 (allow 1.4 x 10^-2) [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• Moles H2SO4 = 4.904 / 98.08 = 0.05000 mol [1]<br/>"
         "• [H2SO4] = 0.05000 / 0.5000 = 0.1000 mol dm^-3 [1]<br/>"
         "• Assuming full dissociation: [H+] = 2 x 0.1000 = 0.2000 mol dm^-3 => pH = -log(0.2000) = 0.70 [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• Step 1 dissociation gives 0.100 mol dm^-3 H+ and 0.100 mol dm^-3 HSO4- [1]<br/>"
         "• Let x = [H+] from second dissociation: [H+] = 0.100 + x, [SO4^2-] = x, [HSO4-] = 0.100 - x [1]<br/>"
         "• Ka2 = ((0.100 + x) * x) / (0.100 - x) = 1.20 x 10^-2 => x^2 + 0.112x - 1.20 x 10^-3 = 0 [1]<br/>"
         "• Solving quadratic: x = 9.84 x 10^-3 mol dm^-3 => [H+]total = 0.100 + 0.00984 = 0.1098 mol dm^-3 => True pH = 0.96 [1]<br/>"
         "• Error = ((0.2000 - 0.1098) / 0.1098) x 100% = +82.1% (overestimation of [H+] by 82%) [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Moles HNO3 = 0.0350 x 0.200 = 0.00700 mol H+ [1]<br/>"
         "• Moles KOH = 0.0650 x 0.120 = 0.00780 mol OH- [1]<br/>"
         "• Excess OH- = 0.00780 - 0.00700 = 0.00080 mol in 100.0 cm^3 (0.100 dm^3) => [OH-] = 8.00 x 10^-3 mol dm^-3 [1]<br/>"
         "• [H+] = Kw / [OH-] = 1.00 x 10^-14 / 8.00 x 10^-3 = 1.25 x 10^-12 mol dm^-3 => pH = 11.90 [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Initial [HCl] = 0.0500 mol dm^-3 => Initial pH = -log(0.0500) = 1.30 [1]<br/>"
         "• Total volume = 10.0 + 90.0 = 100.0 cm^3 (10-fold dilution) => New [HCl] = 0.00500 mol dm^-3 => Final pH = 2.30 [1]<br/>"
         "• pH increases by exactly 1.00 unit because each 10-fold decrease in [H+] adds 1 unit to -log10[H+] [1]."),

        ("Question 32: Ionic Product of Water (Kw) & Strong Bases (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Kc = [H+][OH-] / [H2O]^2 (or [H3O+][OH-]/[H2O]^2) [1]<br/>"
         "• Water is in immense excess and its degree of ionisation is negligible, so [H2O] is effectively constant [1]<br/>"
         "• Combining constant [H2O] with Kc gives Kw = [H+][OH-]; units are mol^2 dm^-6 [1].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• The forward auto-ionisation reaction is endothermic (&Delta;H&deg; > 0) [1]<br/>"
         "• By Le Chatelier's principle, increasing temperature shifts the equilibrium in the forward (endothermic) direction to absorb heat, so Kw increases [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• In pure water, [H+] = [OH-] => Kw = [H+]^2 [1]<br/>"
         "• [H+] = sqrt(5.13 x 10^-13) = 7.16 x 10^-7 mol dm^-3 [1]<br/>"
         "• pH = -log10(7.16 x 10^-7) = 6.14 [1].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Neutrality is defined strictly by the condition [H+] = [OH-], NOT by pH = 7.00 [1]<br/>"
         "• In boiling pure water, every H+ generated is accompanied by an OH- ion, so [H+] = [OH-] exactly [1]<br/>"
         "• Because [H+] = [OH-], the solution cannot turn litmus red or exhibit acidic chemical properties [1].<br/><br/>"
         "<b>(c)(i) [4 Marks]</b><br/>"
         "• Moles Ba(OH)2 = 2.142 / 171.3 = 0.01250 mol [1]<br/>"
         "• [Ba(OH)2] = 0.01250 / 0.250 = 0.0500 mol dm^-3 [1]<br/>"
         "• Ba(OH)2 fully dissociates to 2OH-: [OH-] = 2 x 0.0500 = 0.100 mol dm^-3 [1]<br/>"
         "• [H+] = 1.00 x 10^-14 / 0.100 = 1.00 x 10^-13 mol dm^-3 => pH = 13.00 [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• At target pH = 12.00, pOH = 2.00 => Target [OH-] = 0.0100 mol dm^-3 [1]<br/>"
         "• Initial moles of OH- in 50.0 cm^3 = 0.0500 dm^3 x 0.100 mol dm^-3 = 0.00500 mol [1]<br/>"
         "• Final total volume = moles / target conc = 0.00500 / 0.0100 = 0.500 dm^3 = 500 cm^3 => Volume of water added = 500 - 50 = 450 cm^3 [1]."),

        ("Question 33: Weak Acids: Ka, pKa & Quadratic Derivations (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• CH3COOH(aq) <=> CH3COO-(aq) + H+(aq) (allow with H2O <=> CH3COO- + H3O+) [1]<br/>"
         "• Ka = [CH3COO-][H+] / [CH3COOH] [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• [H+] = 10^-2.79 = 1.622 x 10^-3 mol dm^-3 [1]<br/>"
         "• Assuming [CH3COO-] = [H+] and [CH3COOH]eq = 0.150 - 0.00162 ≈ 0.150 mol dm^-3 [1]<br/>"
         "• Ka = (1.622 x 10^-3)^2 / 0.150 = 1.75 x 10^-5 mol dm^-3 [1]<br/>"
         "• pKa = -log10(1.75 x 10^-5) = 4.76 [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Approximation 1 assumes all H+ comes from HA, justified because water auto-ionisation produces negligible [H+] (10^-7 mol dm^-3) compared to typical weak acid [H+] [1]<br/>"
         "• Approximation 2 assumes dissociation is negligible so [HA]eq ≈ initial conc c, justified when Ka is small (< 10^-4) and initial c is high [1]<br/>"
         "• Approximation 2 breaks down when the acid is moderately strong (Ka > 10^-2) or the solution is very dilute (c < 10^-3 mol dm^-3), where % dissociation exceeds 5% [2].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• [H+] = sqrt(Ka * c) = sqrt(3.32 x 10^-2 * 0.0500) = sqrt(1.66 x 10^-3) = 0.04074 mol dm^-3 [1]<br/>"
         "• pH = -log10(0.04074) = 1.39 [1].<br/><br/>"
         "<b>(c)(ii) [4 Marks]</b><br/>"
         "• Ka = [H+]^2 / (c - [H+]) => 3.32 x 10^-2 = [H+]^2 / (0.0500 - [H+]) [1]<br/>"
         "• [H+]^2 + 0.0332[H+] - 1.66 x 10^-3 = 0 [1]<br/>"
         "• Solving quadratic: [H+] = (-0.0332 + sqrt((0.0332)^2 - 4(1)(-1.66 x 10^-3))) / 2 = (-0.0332 + 0.0880) / 2 = 0.0274 mol dm^-3 [1]<br/>"
         "• True pH = -log10(0.0274) = 1.56 [1].<br/><br/>"
         "<b>(c)(iii) [2 Marks]</b><br/>"
         "• Percentage error = ((0.04074 - 0.0274) / 0.0274) x 100% = +48.7% [1]<br/>"
         "• Dichloroethanoic acid is over 50% dissociated at this concentration (0.0274/0.0500 = 54.8%), making the assumption [HA]eq ≈ c completely invalid [1]."),

        ("Question 34: Degree of Dissociation (α) & Inductive Effects (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• At equilibrium: [H+] = cα, [A-] = cα, [HA] = c(1 - α) [1]<br/>"
         "• Ka = [H+][A-] / [HA] = (cα * cα) / (c(1 - α)) [1]<br/>"
         "• Simplifying numerator and denominator: Ka = (c * α^2) / (1 - α) [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• When α << 1, (1 - α) ≈ 1, so Ka ≈ c * α^2 => α ≈ sqrt(Ka / c) [1]<br/>"
         "• As concentration c decreases (dilution), the denominator in sqrt(Ka / c) decreases, so α must increase [1]<br/>"
         "• In Le Chatelier terms: dilution lowers all concentrations, so the equilibrium shifts to the side with more moles of particles (dissociation) [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• Ka = (0.0200 * (0.0865)^2) / (1 - 0.0865) = (0.0200 * 0.007482) / 0.9135 [1]<br/>"
         "• Ka = 1.50 x 10^-4 / 0.9135 = 1.638 x 10^-4 ≈ 1.64 x 10^-4 mol dm^-3 [1]<br/>"
         "• pKa = -log10(1.638 x 10^-4) = 3.79 [1].<br/><br/>"
         "<b>(b)(ii) [4 Marks]</b><br/>"
         "• At c = 2.00 x 10^-4 mol dm^-3: 1.638 x 10^-4 = (2.00 x 10^-4 * α^2) / (1 - α) [1]<br/>"
         "• α^2 / (1 - α) = 0.819 => α^2 + 0.819α - 0.819 = 0 [1]<br/>"
         "• α = (-0.819 + sqrt((0.819)^2 + 4(0.819))) / 2 = (-0.819 + 1.987) / 2 = 0.584 (58.4% dissociated) [1]<br/>"
         "• [H+] = cα = 2.00 x 10^-4 * 0.584 = 1.168 x 10^-4 mol dm^-3 => pH = -log10(1.168 x 10^-4) = 3.93 [1].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• Propanoic acid has a larger alkyl group (ethyl vs methyl) [1]<br/>"
         "• Alkyl groups are electron-donating (+I inductive effect), which pushes electron density onto the carboxylate group, destabilising the conjugate base and strengthening the O-H bond, making propanoic acid weaker (higher pKa) [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• Fluorine has a higher electronegativity (4.0) than chlorine (3.0), exerting a stronger electron-withdrawing (-I) inductive effect [1]<br/>"
         "• This disperses the negative charge on the carboxylate group more effectively, stabilising the conjugate base and lowering pKa [1]<br/>"
         "• Trichloroethanoic acid has three highly electronegative chlorine atoms withdrawing electron density simultaneously, drastically stabilising the carboxylate anion and reducing pKa to 0.65 [1]."),

        ("Question 35: Experimental Determination of Ka (* Level of Response) (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Moles acid X = 1.832 / 122.1 = 0.01500 mol [1]<br/>"
         "• Concentration = 0.01500 / 0.2500 = 0.0600 mol dm^-3 [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• [H+] = 10^-2.70 = 1.995 x 10^-3 mol dm^-3 [1]<br/>"
         "• Ka = [H+]^2 / c = (1.995 x 10^-3)^2 / 0.0600 = 6.63 x 10^-5 mol dm^-3 [1]<br/>"
         "• pKa = -log10(6.63 x 10^-5) = 4.18 [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive, logically structured practical protocol. Includes two-point calibration of pH meter using fresh standard buffers (pH 4.00 and 7.00), rinsing electrode with deionised water and blotting dry between buffers. Explains serial dilution: pipette 25.0 cm^3 of 0.0600 mol dm^-3 into 50.0 cm^3 flask and make up to mark with deionised water (0.0300 M); repeat consecutively to produce 0.0150 M and 0.00750 M. Details temperature control (thermostatted water bath at 298 K) and waiting for steady digital readout before recording. Identifies two critical errors: temperature fluctuations altering Ka and probe reading, and atmospheric CO2 dissolving to form carbonic acid in dilute solutions, with practical mitigations (water bath, stoppered flasks).<br/>"
         "• Level 2 (3-4 marks): Describes calibration and serial dilution accurately but with minor procedural gaps (e.g. omitting probe rinsing or omitting one dilution step). Identifies at least one error with mitigation.<br/>"
         "• Level 1 (1-2 marks): Brief outline of pH measurement and basic dilution with incomplete calibration or error analysis.<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• From [H+] = sqrt(Ka * [HA]), squaring both sides gives [H+]^2 = Ka * [HA] [1]<br/>"
         "• Comparing with y = mx, plotting y = [H+]^2 against x = [HA] gives a straight line through the origin with gradient m = Ka [1].<br/><br/>"
         "<b>(c)(ii) [2 Marks]</b><br/>"
         "• [H+]^2 = Ka * [HA] = (6.50 x 10^-5) * (0.0400) = 2.60 x 10^-6 mol^2 dm^-6 [1]<br/>"
         "• [H+] = sqrt(2.60 x 10^-6) = 1.612 x 10^-3 mol dm^-3 => pH = 2.79 [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• At 1.00 x 10^-6 mol dm^-3, theoretical weak acid produces only ~10^-6 mol dm^-3 of H+ [1]<br/>"
         "• Atmospheric CO2 dissolves in the open beaker, forming carbonic acid: CO2 + H2O <=> H+ + HCO3- [1]<br/>"
         "• Dissolved CO2 adds extra H+ ions (~2.5 x 10^-6 mol dm^-3), significantly lowering the measured pH [1]."),

        ("Question 36: Acid Rain & Ocean Carbonate Equilibria (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• [CO2(aq)] = KH * P_CO2 = (3.40 x 10^-2) * (4.15 x 10^-4) = 1.411 x 10^-5 mol dm^-3 [1]<br/>"
         "• Since all dissolved CO2 is in equilibrium with H2CO3, [H2CO3] = 1.41 x 10^-5 mol dm^-3 [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• [H+] = sqrt(Ka1 * [H2CO3]) = sqrt((4.47 x 10^-7) * (1.411 x 10^-5)) = sqrt(6.307 x 10^-12) [1]<br/>"
         "• [H+] = 2.511 x 10^-6 mol dm^-3 [1]<br/>"
         "• pH = -log10(2.511 x 10^-6) = 5.60 [1].<br/><br/>"
         "<b>(b)(i) [1 Mark]</b><br/>"
         "• H2SO3(aq) <=> H+(aq) + HSO3-(aq) [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• Ka1 = 1.40 x 10^-2 is larger than the concentration c = 2.40 x 10^-3, so the acid is predominantly dissociated and [H2SO3]eq << c [1]<br/>"
         "• Ka1 = [H+]^2 / (c - [H+]) => 0.0140 = [H+]^2 / (0.00240 - [H+]) [1]<br/>"
         "• [H+]^2 + 0.0140[H+] - 3.36 x 10^-5 = 0 [1]<br/>"
         "• [H+] = (-0.0140 + sqrt((0.0140)^2 + 4(3.36 x 10^-5))) / 2 = (-0.0140 + 0.01817) / 2 = 2.085 x 10^-3 mol dm^-3 [1]<br/>"
         "• Exact pH = -log10(2.085 x 10^-3) = 2.68 [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Increasing atmospheric CO2 forms excess H+ ions in seawater [1]<br/>"
         "• Added H+ reacts with carbonate ions: H+ + CO3^2- <=> HCO3- (protonation to hydrogencarbonate) [1]<br/>"
         "• This significantly depletes the concentration of free CO3^2- in seawater [1]<br/>"
         "• By Le Chatelier's principle, the equilibrium CaCO3(s) <=> Ca^2+(aq) + CO3^2-(aq) shifts to the right, dissolving solid calcium carbonate coral structures [1]."),

        ("Question 37: Aspirin Pharmacokinetics & Lactic Acidosis (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• C9H8O4(aq) <=> H+(aq) + C9H7O4-(aq) (or HA <=> H+ + A-) [1]<br/>"
         "• Ka = [H+][A-] / [HA] [1].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• Ka = 10^-pKa = 10^-3.50 [1]<br/>"
         "• = 3.16 x 10^-4 mol dm^-3 [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• pH - pKa = log10([A-] / [HA]) => 1.50 - 3.50 = -2.00 [1]<br/>"
         "• [A-] / [HA] = 10^-2.00 = 0.0100 (or 1 / 100) [2].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Fraction non-ionised = [HA] / ([HA] + [A-]) = 1 / (1 + 0.0100) = 1 / 1.01 = 0.9901 => 99.0% [1]<br/>"
         "• In the strongly acidic stomach, 99% of aspirin molecules are uncharged (HA) [1]<br/>"
         "• Uncharged, non-polar molecules readily dissolve into and diffuse across the hydrophobic phospholipid bilayer of stomach epithelial cells, facilitating rapid absorption [1].<br/><br/>"
         "<b>(c)(i) [3 Marks]</b><br/>"
         "• Ka = 10^-3.86 = 1.38 x 10^-4 mol dm^-3 [1]<br/>"
         "• [H+] = sqrt(Ka * c) = sqrt((1.38 x 10^-4) * (8.00 x 10^-3)) = sqrt(1.104 x 10^-6) = 1.051 x 10^-3 mol dm^-3 [1]<br/>"
         "• pH = -log10(1.051 x 10^-3) = 2.98 [1].<br/><br/>"
         "<b>(c)(ii) [2 Marks]</b><br/>"
         "• Human blood contains a carbonic acid/hydrogencarbonate buffer system (H2CO3 / HCO3-) [1]<br/>"
         "• Added H+ ions from lactic acid react with excess HCO3- ions (H+ + HCO3- <=> H2CO3 <=> CO2 + H2O), neutralizing the acid and preventing a catastrophic drop in blood pH [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 9 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
