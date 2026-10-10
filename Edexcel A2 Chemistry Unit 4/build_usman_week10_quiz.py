"""
build_usman_week10_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 10 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 14B.1: Acid-Base Titrations, pH Curves and Indicators (The 4 Titration Curves, Indicator Theory pKin)
  - 14B.2: Buffer Solutions (Acidic & Basic Buffers, Buffer Mechanism, Henderson-Hasselbalch, Buffer Capacity)
  - 14B.3: Buffer Solutions & pH Curves (Buffer Region, Half-Equivalence Point pH = pKa, Blood Buffering System)

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
    "Usman_Edexcel_Chem_U4_Week10_150M_Challenging_Quiz.pdf"
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
    def __init__(self, width=AVAIL_W, height=6.5*cm, y_label="pH", x_label="Volume of NaOH / cm^3"):
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 10 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 10 (150 Marks)...")
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
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W10</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 10 ASSESSMENT: TITRATIONS, pH CURVES, INDICATORS & BUFFER SOLUTIONS</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 10 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 14B.1: Acid-Base Titrations, pH Curves and Indicators (The 4 Curves, pKin Selection)<br/>Topic 14B.2: Buffer Solutions (Acidic & Basic Buffers, Henderson-Hasselbalch, Action Mechanisms)<br/>Topic 14B.3: Buffer Solutions & pH Curves (Buffer Region, Half-Equivalence pH = pKa, Blood Buffering)", S['edx_meta'])],
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
        ("Which of the following defines a buffer solution?",
         [("A", "A solution that maintains a completely constant pH of exactly 7.00 under all conditions"),
          ("B", "A solution that resists changes in pH when small amounts of acid or base are added"),
          ("C", "A solution formed by mixing equimolar amounts of a strong acid and a strong base"),
          ("D", "A solution whose pH changes proportionally with the volume of solvent added")]),

        ("Which mixture will produce an acidic buffer solution?",
         [("A", "50 cm^3 of 0.10 mol dm^-3 HCl and 50 cm^3 of 0.10 mol dm^-3 NaOH"),
          ("B", "50 cm^3 of 0.20 mol dm^-3 CH3COOH and 25 cm^3 of 0.20 mol dm^-3 NaOH"),
          ("C", "25 cm^3 of 0.20 mol dm^-3 CH3COOH and 50 cm^3 of 0.20 mol dm^-3 NaOH"),
          ("D", "50 cm^3 of 0.10 mol dm^-3 HNO3 and 50 cm^3 of 0.10 mol dm^-3 NH3")]),

        ("At 298 K, 25.0 cm^3 of 0.100 mol dm^-3 ethanoic acid, CH3COOH, is titrated with 0.100 mol dm^-3 sodium hydroxide, NaOH. What is the approximate pH at the equivalence point?",
         [("A", "pH = 5.2"),
          ("B", "pH = 7.0"),
          ("C", "pH = 8.7"),
          ("D", "pH = 11.4")]),

        # Page 3: Q4, Q5, Q6
        ("An indicator HIn has a pKin value of 9.0. Over which pH range does this indicator change colour?",
         [("A", "pH 4.0 to 6.0"),
          ("B", "pH 7.0 to 9.0"),
          ("C", "pH 8.0 to 10.0"),
          ("D", "pH 9.0 to 11.0")]),

        ("Why is methyl orange (pH transition range 3.1 to 4.4) an UNSUITABLE indicator for the titration of aqueous ethanoic acid with sodium hydroxide?",
         [("A", "Methyl orange is destroyed by weak organic acids"),
          ("B", "The transition range falls entirely in the buffer region before the vertical inflection occurs"),
          ("C", "The equivalence point occurs below pH 3.0"),
          ("D", "Methyl orange only changes colour in the presence of chloride ions")]),

        ("At the half-equivalence point during the titration of a weak monobasic acid HA with sodium hydroxide, which relationship is strictly satisfied?",
         [("A", "pH = 7.00"),
          ("B", "pH = pKa"),
          ("C", "[H+] = [OH-]"),
          ("D", "[HA] = 0 mol dm^-3")]),

        # Page 4: Q7, Q8, Q9
        ("A buffer solution contains 0.200 mol dm^-3 propanoic acid and 0.100 mol dm^-3 sodium propanoate. Given that Ka for propanoic acid is 1.30 x 10^-5 mol dm^-3 at 298 K, what is the pH of this buffer?",
         [("A", "4.59"),
          ("B", "4.89"),
          ("C", "5.19"),
          ("D", "3.89")]),

        ("When a small amount of dilute hydrochloric acid, HCl, is added to an ethanoic acid / sodium ethanoate buffer, which ionic reaction primarily neutralises the added H+ ions?",
         [("A", "CH3COOH + H+ --> CH3COOH2+"),
          ("B", "CH3COO- + H+ --> CH3COOH"),
          ("C", "Na+ + Cl- --> NaCl"),
          ("D", "OH- + H+ --> H2O")]),

        ("When a small amount of aqueous sodium hydroxide, NaOH, is added to an ammonia / ammonium chloride basic buffer, which reaction primarily neutralises the added OH- ions?",
         [("A", "NH3 + OH- --> NH2- + H2O"),
          ("B", "NH4+ + OH- --> NH3 + H2O"),
          ("C", "Cl- + OH- --> HOCl + e-"),
          ("D", "H+ + OH- --> H2O (from pure water auto-ionisation)")]),

        # Page 5: Q10, Q11, Q12
        ("An equimolar basic buffer solution contains 0.100 mol dm^-3 NH3 and 0.100 mol dm^-3 NH4Cl at 298 K. Given that Kb for ammonia is 1.80 x 10^-5 mol dm^-3, what is the pH of this buffer? (Kw = 1.00 x 10^-14 mol^2 dm^-6)",
         [("A", "4.74"),
          ("B", "7.00"),
          ("C", "9.26"),
          ("D", "11.13")]),

        ("In the titration of hydrochloric acid, HCl(aq), with aqueous ammonia, NH3(aq), why is the pH at the equivalence point less than 7.00?",
         [("A", "The ammonium ion, NH4+, undergoes acidic hydrolysis: NH4+ + H2O <==> NH3 + H3O+"),
          ("B", "Chloride ions donate protons to water molecules"),
          ("C", "Hydrochloric acid is a dibasic acid in the presence of ammonia"),
          ("D", "Ammonia completely evaporates from the solution at the end-point")]),

        ("Why is NO chemical acid-base indicator suitable for the titration of methanoic acid with aqueous ammonia?",
         [("A", "Both reactants are volatile and evaporate rapidly"),
          ("B", "The titration curve lacks a steep, vertical inflection at the equivalence point"),
          ("C", "Methanoic acid decomposes into carbon monoxide and water"),
          ("D", "Ammonia precipitates ammonium methanoate as a dense solid")]),

        # Page 6: Q13, Q14, Q15
        ("Human arterial blood is buffered primarily by the H2CO3 / HCO3- conjugate pair. At normal blood pH of 7.40 and 310 K (where pKa of carbonic acid is 6.10), what is the ratio of [HCO3-] to [H2CO3]?",
         [("A", "1 : 20"),
          ("B", "1 : 1"),
          ("C", "10 : 1"),
          ("D", "20 : 1")]),

        ("During rapid hyperventilation, large volumes of CO2 are exhaled from the lungs. How does this affect blood pH and the equilibrium: CO2(aq) + H2O(l) <==> H2CO3(aq) <==> H+(aq) + HCO3-(aq)?",
         [("A", "Equilibrium shifts right; [H+] increases; blood pH drops (acidosis)"),
          ("B", "Equilibrium shifts left; [H+] decreases; blood pH rises (alkalosis)"),
          ("C", "Equilibrium does not shift because CO2 is non-polar"),
          ("D", "Equilibrium shifts left; [H+] increases; blood pH rises")]),

        ("An indicator HIn is red in its acid form and yellow in its conjugate base form, In-. If its pKin is 5.20, what colour will the indicator display in a solution buffered at pH 5.20?",
         [("A", "Bright red"),
          ("B", "Bright yellow"),
          ("C", "Orange"),
          ("D", "Colourless")]),

        # Page 7: Q16, Q17, Q18
        ("A buffer solution is prepared by mixing 50.0 cm^3 of 0.300 mol dm^-3 methanoic acid, HCOOH (pKa = 3.75), with 50.0 cm^3 of 0.150 mol dm^-3 sodium methanoate. What is the pH of the resulting solution at 298 K?",
         [("A", "3.45"),
          ("B", "3.75"),
          ("C", "4.05"),
          ("D", "4.35")]),

        ("What happens to the pH of an acidic buffer solution containing 0.10 mol dm^-3 CH3COOH and 0.10 mol dm^-3 CH3COONa when diluted with an equal volume of pure water at 298 K?",
         [("A", "The pH increases by exactly 1.0 unit"),
          ("B", "The pH decreases by exactly 0.5 unit"),
          ("C", "The pH remains virtually unchanged"),
          ("D", "The pH becomes exactly 7.00")]),

        ("Under which of the following conditions is the buffer capacity of a weak acid / conjugate base buffer at its MAXIMUM?",
         [("A", "When [A-] >> [HA] and the solution is highly alkaline"),
          ("B", "When [HA] = [A-] and the absolute concentrations of both components are high"),
          ("C", "When [HA] >> [A-] and the solution is very concentrated"),
          ("D", "When the total concentration of the buffer is less than 0.001 mol dm^-3")]),

        # Page 8: Q19, Q20, Q21
        ("A 500 cm^3 buffer solution contains 0.100 mol of HA (pKa = 4.80) and 0.100 mol of NaA. If 0.020 mol of gaseous HCl is completely absorbed into this solution without volume change, what is the new pH?",
         [("A", "4.62"),
          ("B", "4.80"),
          ("C", "4.98"),
          ("D", "5.10")]),

        ("In a titration of 25.0 cm^3 of 0.0800 mol dm^-3 ethanoic acid with 0.100 mol dm^-3 NaOH, what volume of NaOH is required to reach the half-equivalence point?",
         [("A", "20.0 cm^3"),
          ("B", "10.0 cm^3"),
          ("C", "12.5 cm^3"),
          ("D", "5.0 cm^3")]),

        ("Which of the following salts dissolves in water at 298 K to form a solution with pH GREATER than 7.00?",
         [("A", "Ammonium chloride, NH4Cl"),
          ("B", "Potassium nitrate, KNO3"),
          ("C", "Sodium ethanoate, CH3COONa"),
          ("D", "Sodium chloride, NaCl")]),

        # Page 9: Q22, Q23, Q24
        ("Which of the following salts dissolves in water at 298 K to produce an acidic solution (pH < 7.00)?",
         [("A", "Sodium methanoate, HCOONa"),
          ("B", "Ammonium nitrate, NH4NO3"),
          ("C", "Potassium sulfate, K2SO4"),
          ("D", "Barium chloride, BaCl2")]),

        ("Phenolphthalein transitions from colourless in acid to pink in alkali (pH range 8.3 to 10.0). Which chemical change is responsible for the appearance of the pink colour?",
         [("A", "Loss of two protons creates an extended conjugated pi-electron system that absorbs visible light"),
          ("B", "Oxidation of the aromatic rings by atmospheric oxygen"),
          ("C", "Reduction of phenolphthalein by hydroxide ions"),
          ("D", "Precipitation of sodium phenolphthaleinate microcrystals")]),

        ("How does an increase in temperature affect the end-point of an acid-base indicator whose dissociation, HIn <==> H+ + In-, is endothermic?",
         [("A", "Kin increases, so pKin decreases and the indicator changes colour at a lower pH"),
          ("B", "Kin decreases, so pKin increases and the indicator changes colour at a higher pH"),
          ("C", "Kin remains constant, but the colour intensity doubles"),
          ("D", "Temperature has zero effect on indicator dissociation equilibria")]),

        # Page 10: Q25, Q26, Q27
        ("A student mixes 40.0 cm^3 of 0.200 mol dm^-3 CH3COOH (Ka = 1.74 x 10^-5 mol dm^-3) with 20.0 cm^3 of 0.200 mol dm^-3 NaOH at 298 K. What is the pH of the resulting mixture?",
         [("A", "4.76"),
          ("B", "5.06"),
          ("C", "7.00"),
          ("D", "8.72")]),

        ("50.0 cm^3 of 0.100 mol dm^-3 hydrochloric acid, HCl, is mixed with 50.0 cm^3 of 0.100 mol dm^-3 aqueous ammonia, NH3, at 298 K. What is the nature of the resulting solution?",
         [("A", "A basic buffer solution of pH ≈ 9.25"),
          ("B", "An equimolar solution of ammonium chloride having pH < 7.00"),
          ("C", "A neutral solution of pH = 7.00"),
          ("D", "An acidic buffer solution of pH ≈ 4.75")]),

        ("A buffer solution has [HA] = 0.050 mol dm^-3 and [A-] = 0.025 mol dm^-3. If Ka = 2.0 x 10^-5 mol dm^-3, what is the concentration of hydrogen ions, [H+]?",
         [("A", "1.0 x 10^-5 mol dm^-3"),
          ("B", "2.0 x 10^-5 mol dm^-3"),
          ("C", "4.0 x 10^-5 mol dm^-3"),
          ("D", "5.0 x 10^-5 mol dm^-3")]),

        # Page 11: Q28, Q29, Q30
        ("In the titration curve of a diprotic acid like ethanedioic acid, H2C2O4, with sodium hydroxide, how many distinct buffer regions and equivalence points are observed?",
         [("A", "1 buffer region and 1 equivalence point"),
          ("B", "2 buffer regions and 1 equivalence point"),
          ("C", "2 buffer regions and 2 equivalence points"),
          ("D", "3 buffer regions and 2 equivalence points")]),

        ("Why is bromothymol blue (pH range 6.0 to 7.6) ideal for a strong acid - strong base titration, but unsuitable for a weak acid - strong base titration?",
         [("A", "Strong acid titrations require a yellow indicator"),
          ("B", "The vertical inflection for a weak acid - strong base titration only begins above pH 7.5, so bromothymol blue changes colour before the equivalence point"),
          ("C", "Bromothymol blue reacts irreversibly with sodium ethanoate"),
          ("D", "Bromothymol blue is only active in alcoholic solutions")]),

        ("Equal volumes of 0.200 mol dm^-3 methanoic acid, HCOOH, and 0.100 mol dm^-3 barium hydroxide, Ba(OH)2, are mixed at 298 K. What is the pH of the resulting solution?",
         [("A", "pH < 7.00 (acidic)"),
          ("B", "pH = 7.00 (strictly neutral)"),
          ("C", "pH > 7.00 (alkaline due to methanoate ion hydrolysis)"),
          ("D", "pH = 1.00 (strongly acidic)")])
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
    # QUESTION 31 (18 MARKS) — THE FOUR TITRATION CURVES & INDICATOR SELECTION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;The shape of a pH titration curve depends on the relative strengths of the acid and base used.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;On the coordinate axes provided below, sketch the pH titration curves obtained when:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Curve 1:</b> 25.0 cm^3 of 0.100 mol dm^-3 HCl(aq) is titrated with 0.100 mol dm^-3 NaOH(aq).<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Curve 2:</b> 25.0 cm^3 of 0.100 mol dm^-3 CH3COOH(aq) is titrated with 0.100 mol dm^-3 NaOH(aq).<br/>"
                           "Clearly label Curve 1 and Curve 2, their initial pH values, the equivalence point volumes, and the vertical sections.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(width=AVAIL_W, height=6.5*cm, y_label="pH", x_label="Volume of NaOH added / cm^3"))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Explain why the equivalence point pH for Curve 1 is exactly 7.00, whereas the equivalence point pH for Curve 2 is approximately 8.72 at 298 K. Include a balanced ionic equation to support your explanation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The table below shows three acid-base indicators and their working pH ranges:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    ind_table = [
        [Paragraph("<b>Indicator</b>", S['tbl_th']), Paragraph("<b>Acid Colour</b>", S['tbl_th']), Paragraph("<b>Alkaline Colour</b>", S['tbl_th']), Paragraph("<b>pH Range of Colour Change</b>", S['tbl_th'])],
        [Paragraph("Methyl yellow", S['tbl_td_l']), Paragraph("Red", S['tbl_td']), Paragraph("Yellow", S['tbl_td']), Paragraph("2.9 to 4.0", S['tbl_td'])],
        [Paragraph("Bromothymol blue", S['tbl_td_l']), Paragraph("Yellow", S['tbl_td']), Paragraph("Blue", S['tbl_td']), Paragraph("6.0 to 7.6", S['tbl_td'])],
        [Paragraph("Phenolphthalein", S['tbl_td_l']), Paragraph("Colourless", S['tbl_td']), Paragraph("Pink", S['tbl_td']), Paragraph("8.3 to 10.0", S['tbl_td'])],
    ]
    t_ind = Table(ind_table, colWidths=[4.2*cm, 3.2*cm, 3.2*cm, 4.4*cm])
    t_ind.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_ind)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("Select, with detailed reasons based on the vertical inflection ranges of the curves, the most suitable indicator for:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;(i) Titration Curve 1 (HCl vs NaOH)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;(ii) Titration Curve 2 (CH3COOH vs NaOH)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Explain why no common chemical indicator can be used to detect the end-point of a titration between 0.100 mol dm^-3 ethanoic acid, CH3COOH, and 0.100 mol dm^-3 aqueous ammonia, NH3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — BUFFER ACTION & HENDERSON-HASSELBALCH
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;A buffer solution resists changes in pH when small quantities of acid or alkali are added.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Explain the chemical mechanism of buffer action in an aqueous buffer containing ethanoic acid, CH3COOH, and sodium ethanoate, CH3COONa, when:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;(i) A small volume of hydrochloric acid, HCl(aq), is added.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;(ii) A small volume of sodium hydroxide, NaOH(aq), is added.<br/>"
                           "Write ionic equations for both reactions and explain why the pH changes only negligibly.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A student prepares an acidic buffer by mixing 60.0 cm^3 of 0.250 mol dm^-3 ethanoic acid (Ka = 1.74 x 10^-5 mol dm^-3 at 298 K) with 40.0 cm^3 of 0.350 mol dm^-3 sodium ethanoate.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the concentrations of ethanoic acid and ethanoate ions in the mixed buffer, and calculate the pH of the buffer solution at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the new pH of the buffer after 2.00 cm^3 of 1.00 mol dm^-3 hydrochloric acid, HCl, is added to the 100.0 cm^3 buffer mixture prepared in (b)(i). Assume no significant volume contraction occurs.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: New pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Calculate the pH of the solution formed when 2.00 cm^3 of the same 1.00 mol dm^-3 hydrochloric acid is added to 100.0 cm^3 of pure unbuffered water at 298 K (Kw = 1.00 x 10^-14 mol^2 dm^-6). Compare this pH change with that observed in the buffer in (b)(ii) and comment on the buffer's effectiveness.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Unbuffered pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — PARTIAL NEUTRALISATION & HALF-EQUIVALENCE POINT
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Buffer solutions can also be synthesized conveniently by the partial neutralisation of a weak acid with a strong base.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;50.0 cm^3 of 0.400 mol dm^-3 propanoic acid, CH3CH2COOH (pKa = 4.87 at 298 K), is reacted with 30.0 cm^3 of 0.250 mol dm^-3 sodium hydroxide, NaOH.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical equation for the neutralization reaction occurring.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(1)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the amount in moles of unreacted propanoic acid and the amount in moles of sodium propanoate present in the resulting buffer solution.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Moles CH3CH2COOH = ................................ mol &nbsp;&nbsp;&nbsp;&nbsp; Moles CH3CH2COONa = ................................ mol", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the pH of this buffer solution at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>33 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(b)&nbsp;&nbsp;In a separate experiment, a 25.0 cm^3 aliquot of 0.100 mol dm^-3 propanoic acid is titrated with 0.100 mol dm^-3 sodium hydroxide.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;State the volume of NaOH required to reach the equivalence point and the volume required to reach the half-equivalence point.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Show mathematically, by referring to the expression for Ka, why the pH of the solution at the half-equivalence point is exactly equal to the pKa of the weak acid.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;State how a research chemist can determine the Ka of an unknown weak acid directly from a single recorded pH titration curve without performing any calculations.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Calculate the pH of the solution at the equivalence point when 25.0 cm^3 of 0.100 mol dm^-3 propanoic acid has reacted with exactly 25.0 cm^3 of 0.100 mol dm^-3 NaOH. (Ka = 1.35 x 10^-5 mol dm^-3, Kw = 1.00 x 10^-14 mol^2 dm^-6 at 298 K)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Equivalence pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — BASIC BUFFERS (AMMONIA/AMMONIUM) & SALT HYDROLYSIS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Aqueous ammonia is a weak base that ionises in water according to the equilibrium:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("NH<sub>3</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; NH<sub>4</sub><sup>+</sup>(aq) &nbsp;+&nbsp; OH<sup>-</sup>(aq) &nbsp;&nbsp;&nbsp;&nbsp; K<sub>b</sub> = 1.78 x 10^-5 mol dm^-3", S['q_equation']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the expression for the base dissociation constant, Kb, for ammonia.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;By considering the equilibrium expressions for Ka of the ammonium ion (NH4+) and Kb of ammonia (NH3), prove that:<br/>"
                           "Ka x Kb = Kw", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the values of Ka and pKa for the ammonium ion, NH4+, at 298 K. (Kw = 1.00 x 10^-14 mol^2 dm^-6)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Ka = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pKa = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>34 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(b)&nbsp;&nbsp;A basic buffer solution is prepared by dissolving 5.350 g of solid ammonium chloride, NH4Cl (Mr = 53.50), in 500.0 cm^3 of 0.150 mol dm^-3 aqueous ammonia at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the concentration of ammonium ions, [NH4+], and the pH of this basic buffer solution at 298 K.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: [NH4+] = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pH = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the new pH after 5.00 cm^3 of 0.500 mol dm^-3 sodium hydroxide, NaOH, is added to 250.0 cm^3 of this basic buffer solution. Assume the total volume becomes 255.0 cm^3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: New pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — CONTINUOUS pH TITRATION (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;A student investigated an unknown monobasic organic acid, HA, by carrying out a continuous pH titration using a computer-interfaced digital pH probe and burette.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;A 25.0 cm^3 sample of the acid HA was titrated with 0.100 mol dm^-3 sodium hydroxide, NaOH. The data logger recorded an equivalence point after the addition of exactly 22.40 cm^3 of NaOH.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the concentration of the unknown acid HA in mol dm^-3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Concentration = ..................................................... mol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;From the recorded titration curve, the pH at the half-equivalence point (11.20 cm^3 of NaOH added) was 3.82 at 298 K. Calculate the values of Ka and pKa for acid HA.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: Ka = ........................................ mol dm^-3 &nbsp;&nbsp;&nbsp;&nbsp; pKa = ........................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;The teacher asked the student to perform a second titration with enhanced precision to verify the pKa value.<br/>"
                           "Describe a detailed experimental procedure to:<br/>"
                           "- Calibrate the digital pH probe using two standard buffer solutions (pH 4.00 and pH 9.20).<br/>"
                           "- Set up the apparatus (magnetic stirrer, burette, pH electrode) to ensure continuous, homogenous mixing without damaging the probe.<br/>"
                           "- Collect pH readings systematically, explaining why the volume increments of NaOH must be reduced from 1.00 cm^3 to dropwise (0.05–0.10 cm^3) near the equivalence point.<br/>"
                           "- Identify two significant systematic errors in pH measurement and describe how to minimize them.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>*35 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(c)&nbsp;&nbsp;On the coordinate axes provided below, sketch the complete pH titration curve for this titration (addition of 0.100 mol dm^-3 NaOH to 25.0 cm^3 of HA), clearly marking:<br/>"
                           "- The initial pH (~2.4)<br/>"
                           "- The half-equivalence point (11.20 cm^3, pH 3.82)<br/>"
                           "- The equivalence point (22.40 cm^3, pH ~8.6)<br/>"
                           "- The final plateau region at excess base.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(GraphSketchBox(width=AVAIL_W, height=6.5*cm, y_label="pH", x_label="Volume of 0.100 M NaOH added / cm^3"))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Explain how calculating and plotting the first derivative of the titration curve, &Delta;pH / &Delta;V, against volume of NaOH allows the equivalence point to be determined with significantly greater precision than reading directly from the S-shaped pH curve.", S['q_subpart']))
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
    # QUESTION 36 (15 MARKS) — PHYSIOLOGICAL BLOOD BUFFERING & ACIDOSIS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Human Physiology and Clinical Biochemistry:</b><br/>"
                           "Normal human arterial blood pH is tightly regulated within the narrow physiological range of 7.35 to 7.45. The primary extracellular buffering system is the carbonic acid - hydrogencarbonate equilibrium:<br/>"
                           "CO<sub>2</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; H<sub>2</sub>CO<sub>3</sub>(aq) &nbsp;&lt;=&gt;&nbsp; H<sup>+</sup>(aq) &nbsp;+&nbsp; HCO<sub>3</sub><sup>-</sup>(aq)<br/>"
                           "At body temperature (310 K), the effective pKa for this equilibrium is 6.10, and normal plasma [HCO3-] is 24.0 mmol dm^-3.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the Henderson-Hasselbalch equation for the carbonic acid / hydrogencarbonate buffer system.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(1)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the concentration of dissolved carbonic acid, [H2CO3], in healthy arterial blood at pH 7.40.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("Answer: [H2CO3] = ..................................................... mmol dm^-3", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Calculate the exact numerical ratio of [HCO3-] to [H2CO3] in healthy arterial blood.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("Answer: Ratio = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;A chemist points out that an ideal buffer has a 1:1 ratio of acid to conjugate base (where pH = pKa = 6.10). Explain why the human body operates the blood buffer at a 20:1 ratio (pH 7.40) and why this is vital for survival.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>36 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(c)&nbsp;&nbsp;A patient suffering from diabetic ketoacidosis produces large amounts of acetoacetic acid and beta-hydroxybutyric acid, reducing plasma [HCO3-] to 12.0 mmol dm^-3.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;If dissolved [H2CO3] remains temporarily at 1.20 mmol dm^-3, calculate the patient's arterial blood pH and state whether this condition represents acidosis or alkalosis.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Blood pH = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;The patient immediately begins rapid, deep breathing (Kussmaul respiration). Explain, using Le Chatelier's principle and equilibrium shifts, how hyperventilation acts as respiratory compensation to restore blood pH towards normal.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — CITRIC ACID FERMENTATION & OCEAN ALKALINITY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Industrial Biotechnology and Ocean Carbon Removal:</b><br/>"
                           "In industrial biotechnology, citric acid (2-hydroxypropane-1,2,3-tricarboxylic acid, C6H8O7) is manufactured by fermentation using the fungus <i>Aspergillus niger</i>. The fermentation broth must be buffered around pH 3.00. Citric acid is a tribasic acid with pKa values: pKa1 = 3.13, pKa2 = 4.76, pKa3 = 6.40 at 298 K.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;State the formulae of the primary conjugate acid-base pair that acts as the buffer in the pH range 2.80 to 3.20.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Calculate the mass of monosodium citrate, C6H7O7Na (Mr = 214.1), that must be dissolved in 1.00 dm^3 of 0.250 mol dm^-3 citric acid, C6H8O7 (Mr = 192.1), to produce a fermentation buffer solution of exactly pH 3.00 at 298 K. (Use pKa1 = 3.13)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Mass of C6H7O7Na = ..................................................... g", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>37 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("(b)&nbsp;&nbsp;Ocean Alkalinity Enhancement (OAE) is a proposed geoengineering technique where alkaline minerals like calcium hydroxide, Ca(OH)2, are added to ocean surface water to increase carbon dioxide uptake.<br/>"
                           "In seawater, dissolved inorganic carbon exists in equilibrium:<br/>"
                           "CO<sub>2</sub>(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; HCO<sub>3</sub><sup>-</sup>(aq) &nbsp;+&nbsp; H<sup>+</sup>(aq)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain, using Le Chatelier's principle and conjugate acid-base neutralization, how adding Ca(OH)2 increases the capacity of seawater to absorb atmospheric CO2 while preventing ocean acidification.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;If local addition of Ca(OH)2 is poorly mixed, surface pH can spike above 9.0. Explain why this causes the spontaneous precipitation of solid calcium carbonate, CaCO3(s), and explain how this reverse reaction releases CO2 back into the atmosphere, negating the carbon capture benefit.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
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
        [Paragraph("Henderson-Hasselbalch Equation", S['tbl_td_l']), Paragraph("pH = pKa + log10([A-] / [HA])", S['tbl_td']), Paragraph("dimensionless", S['tbl_td'])],
        [Paragraph("Base Dissociation Constant Relation", S['tbl_td_l']), Paragraph("Ka x Kb = Kw", S['tbl_td']), Paragraph("mol^2 dm^-6", S['tbl_td'])],
        [Paragraph("Indicator Transition Constant", S['tbl_td_l']), Paragraph("Kin = [H+][In-] / [HIn]", S['tbl_td']), Paragraph("mol dm^-3", S['tbl_td'])],
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 10 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Definition: resists pH changes when small amounts of acid or base are added.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Excess weak acid (0.010 mol) partially neutralized by limited strong base (0.005 mol) yields buffer.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Equivalence point of weak acid-strong base is alkaline (pH ≈ 8.7) due to ethanoate anion hydrolysis.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Indicator operating range is pKin ± 1 => 9.0 ± 1.0 = pH 8.0 to 10.0.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Methyl orange changes colour at pH 3.1–4.4, which lies on the buffer plateau long before equivalence.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At half-equivalence: [HA] = [A-] => log([A-]/[HA]) = log(1) = 0 => pH = pKa.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("pKa = -log(1.30x10^-5) = 4.886. pH = 4.886 + log(0.100/0.200) = 4.886 - 0.301 = 4.59.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Added H+ is consumed by ethanoate conjugate base: CH3COO- + H+ --> CH3COOH.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Added OH- is consumed by ammonium conjugate acid: NH4+ + OH- --> NH3 + H2O.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("pKb = -log(1.80x10^-5) = 4.74 => pOH = 4.74 + log(1) = 4.74 => pH = 14.00 - 4.74 = 9.26.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Ammonium ion hydrolyses: NH4+ + H2O <=> NH3 + H3O+, producing excess H3O+ (pH < 7).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Weak acid-weak base titration curve has no steep vertical inflection, so no indicator changes sharply.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("pH = pKa + log([HCO3-]/[H2CO3]) => 7.40 = 6.10 + 1.30 => ratio = 10^1.30 = 20 : 1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Exhaling CO2 drives equilibrium left, consuming H+ ions and causing respiratory alkalosis (pH rises).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("At pH = pKin, [HIn] = [In-], so red and yellow mix equally to form orange.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("pH = 3.75 + log(0.150/0.300) = 3.75 - 0.301 = 3.45.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Diluting a buffer dilutes both [HA] and [A-] by the same factor; ratio is unchanged, so pH is constant.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Buffer capacity is maximized when [HA] = [A-] (pH = pKa) and concentrations are high.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Added HCl converts 0.020 mol A- to HA: new [HA] = 0.120, [A-] = 0.080 => pH = 4.80 + log(0.080/0.120) = 4.62.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Moles acid = 0.025 x 0.0800 = 0.00200 mol => Equivalence vol = 0.00200/0.100 = 20.0 cm^3 => Half-equiv = 10.0 cm^3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("CH3COONa is the salt of a weak acid and strong base; ethanoate hydrolyses to produce OH- (pH > 7).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("NH4NO3 is the salt of a weak base and strong acid; NH4+ hydrolyses to produce H3O+ (pH < 7).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Deprotonation delocalises electrons over an extended conjugated pi system, absorbing visible green light.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Endothermic dissociation: increasing T increases Kin and decreases pKin, shifting transition to lower pH.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Moles acid = 0.0080; moles base = 0.0040. Exactly half neutralized => [HA] = [A-] => pH = pKa = 4.76.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Equal moles of strong acid and weak base produce ammonium chloride; NH4+ hydrolyses to give pH < 7.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("[H+] = Ka * ([HA]/[A-]) = (2.0 x 10^-5) * (0.050/0.025) = 4.0 x 10^-5 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Diprotic acid has two protons: neutralises sequentially giving 2 buffer regions and 2 equivalence points.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Weak acid-strong base vertical jump occurs between pH ~7 and ~11; bromothymol blue changes prematurely.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("0.100 M Ba(OH)2 provides 0.200 M OH-, exactly neutralizing 0.200 M HCOOH to barium methanoate (pH > 7).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Titration Curves & Indicator Selection (18 Marks)",
         "<b>(a) [6 Marks]</b><br/>"
         "• Curve 1 (HCl): starts at pH 1.0, flat until ~20 cm^3, steep vertical jump from pH 3 to 11 at 25.0 cm^3, levels off at pH ~12.7 [2]<br/>"
         "• Curve 2 (CH3COOH): starts at pH ~2.9, rises initially then shows flat buffer region, half-equivalence point at 12.5 cm^3 (pH 4.76), steep vertical jump from pH 7 to 11 at 25.0 cm^3, levels off at pH ~12.7 [2]<br/>"
         "• Both curves share equivalence point volume at exactly 25.0 cm^3 [1]<br/>"
         "• Axes correctly labeled with scales (pH 0-14, volume 0-50 cm^3) [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• In Curve 1, the salt formed is NaCl; neither Na+ nor Cl- hydrolyses in water, so [H+] = [OH-] and pH = 7.00 [1]<br/>"
         "• In Curve 2, the salt formed is sodium ethanoate, CH3COONa [1]<br/>"
         "• The ethanoate ion acts as a Brønsted base and reacts with water: CH3COO-(aq) + H2O(l) <=> CH3COOH(aq) + OH-(aq) [1]<br/>"
         "• Hydrolysis generates excess OH- ions at equivalence, driving the pH above 7 to ~8.72 [1].<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• (i) Curve 1: Bromothymol blue OR phenolphthalein is suitable [1]. Reason: Vertical section spans pH 3 to 11; both indicators have transition ranges (6.0-7.6 and 8.3-10.0) that fall completely within this vertical section [2].<br/>"
         "• (ii) Curve 2: ONLY phenolphthalein is suitable [1]. Reason: The vertical section spans only pH 7 to 11; phenolphthalein (8.3-10.0) falls within this range. Methyl yellow and bromothymol blue change colour before the vertical jump in the buffer region, giving false early endpoints [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• The titration of a weak acid with a weak base lacks a steep vertical section (pH changes very gradually across equivalence) [1]<br/>"
         "• No indicator has a colour range narrow enough to change sharply with a single drop of titrant [1]<br/>"
         "• The endpoint can only be located accurately using a pH meter or electrical conductivity probe [1]."),

        ("Question 32: Buffer Mechanisms & Henderson-Hasselbalch (18 Marks)",
         "<b>(a) [5 Marks]</b><br/>"
         "• (i) Added H+ reacts with the large reservoir of ethanoate conjugate base: CH3COO-(aq) + H+(aq) --> CH3COOH(aq) [1]<br/>"
         "• Added H+ is consumed, forming weakly dissociated ethanoic acid, so [H+] barely changes [1]<br/>"
         "• (ii) Added OH- reacts with the large reservoir of undissociated ethanoic acid: CH3COOH(aq) + OH-(aq) --> CH3COO-(aq) + H2O(l) [1]<br/>"
         "• Added OH- is consumed, forming water and ethanoate, so [OH-] barely changes [1]<br/>"
         "• Because the concentrations of CH3COOH and CH3COO- are large compared to added acid/alkali, the ratio [A-]/[HA] changes minimally [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• Total volume = 60.0 + 40.0 = 100.0 cm^3 [1]<br/>"
         "• Moles CH3COOH = 0.0600 x 0.250 = 0.0150 mol => [CH3COOH] = 0.150 mol dm^-3 [1]<br/>"
         "• Moles CH3COO- = 0.0400 x 0.350 = 0.0140 mol => [CH3COO-] = 0.140 mol dm^-3 [1]<br/>"
         "• pH = -log(1.74x10^-5) + log(0.140 / 0.150) = 4.759 - 0.030 = 4.73 [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• Moles HCl added = 0.00200 x 1.00 = 0.00200 mol [1]<br/>"
         "• Reaction: CH3COO- + H+ --> CH3COOH [1]<br/>"
         "• New moles CH3COO- = 0.0140 - 0.00200 = 0.0120 mol [1]<br/>"
         "• New moles CH3COOH = 0.0150 + 0.00200 = 0.0170 mol [1]<br/>"
         "• New pH = 4.759 + log(0.0120 / 0.0170) = 4.759 - 0.151 = 4.61 (pH drops by only 0.12 units) [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• In unbuffered water, total volume = 100.0 + 2.0 = 102.0 cm^3 [1]<br/>"
         "• [H+] = 0.00200 mol / 0.102 dm^3 = 0.0196 mol dm^-3 [1]<br/>"
         "• pH = -log(0.0196) = 1.71 [1]<br/>"
         "• Unbuffered pH collapses from 7.00 to 1.71 (drop of 5.29 units), whereas the buffer resisted with a drop of only 0.12 units, demonstrating exceptional buffer capacity [1]."),

        ("Question 33: Partial Neutralisation & Half-Equivalence Point (18 Marks)",
         "<b>(a)(i) [1 Mark]</b><br/>"
         "• CH3CH2COOH + NaOH --> CH3CH2COONa + H2O [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Initial moles acid = 0.0500 x 0.400 = 0.0200 mol [1]<br/>"
         "• Initial moles base = 0.0300 x 0.250 = 0.00750 mol [1]<br/>"
         "• Moles salt formed = 0.00750 mol [1]<br/>"
         "• Moles unreacted acid = 0.0200 - 0.00750 = 0.0125 mol [1].<br/><br/>"
         "<b>(a)(iii) [3 Marks]</b><br/>"
         "• In 80.0 cm^3: ratio [A-]/[HA] = 0.00750 / 0.0125 = 0.600 [1]<br/>"
         "• pH = pKa + log([A-]/[HA]) = 4.87 + log(0.600) [1]<br/>"
         "• pH = 4.87 - 0.222 = 4.65 [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• Moles acid = 0.0250 x 0.100 = 0.00250 mol => V_eq = 0.00250 / 0.100 = 25.0 cm^3 [1]<br/>"
         "• Half-equivalence volume = 25.0 / 2 = 12.5 cm^3 [1].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• At half-equivalence, exactly half the initial HA has been converted to A-, so [HA] = [A-] [1]<br/>"
         "• Ka = [H+][A-] / [HA] => [H+] = Ka * ([HA] / [A-]) [1]<br/>"
         "• Since [HA]/[A-] = 1, [H+] = Ka, and taking negative logs gives pH = pKa [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• Locate the equivalence point volume on the titration curve, halve it to find the half-equivalence point volume, and read off the pH directly from the y-axis (pH = pKa => Ka = 10^-pH) [2].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• At equivalence: total volume = 50.0 cm^3; moles salt = 0.00250 mol => [CH3CH2COO-] = 0.00250 / 0.0500 = 0.0500 mol dm^-3 [1]<br/>"
         "• Kh = Kw / Ka = 1.00x10^-14 / 1.35x10^-5 = 7.407 x 10^-10 => [OH-] = sqrt(Kh * [A-]) = sqrt(7.407x10^-10 * 0.0500) = 6.086 x 10^-6 mol dm^-3 [1]<br/>"
         "• pOH = 5.22 => pH = 14.00 - 5.22 = 8.78 [1]."),

        ("Question 34: Basic Buffers & Salt Hydrolysis (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Kb = [NH4+][OH-] / [NH3] [2].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Ka = [NH3][H+] / [NH4+] and Kb = [NH4+][OH-] / [NH3] [1]<br/>"
         "• Ka x Kb = ([NH3][H+] / [NH4+]) * ([NH4+][OH-] / [NH3]) [1]<br/>"
         "• All species cancel except [H+][OH-], which equals Kw [1].<br/><br/>"
         "<b>(a)(iii) [3 Marks]</b><br/>"
         "• Ka = Kw / Kb = 1.00 x 10^-14 / 1.78 x 10^-5 = 5.62 x 10^-10 mol dm^-3 [2]<br/>"
         "• pKa = -log10(5.62 x 10^-10) = 9.25 [1].<br/><br/>"
         "<b>(b)(i) [5 Marks]</b><br/>"
         "• Moles NH4Cl = 5.350 / 53.50 = 0.1000 mol [1]<br/>"
         "• [NH4+] = 0.1000 / 0.5000 = 0.2000 mol dm^-3 [1]<br/>"
         "• [NH3] = 0.1500 mol dm^-3 [1]<br/>"
         "• Using Henderson-Hasselbalch: pH = pKa + log([base] / [acid]) = 9.25 + log(0.150 / 0.200) [1]<br/>"
         "• pH = 9.25 + (-0.125) = 9.125 ≈ 9.13 [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• In 250 cm^3: moles NH3 = 0.250 x 0.150 = 0.0375 mol; moles NH4+ = 0.250 x 0.200 = 0.0500 mol [1]<br/>"
         "• Moles NaOH added = 0.00500 x 0.500 = 0.00250 mol [1]<br/>"
         "• Reaction: NH4+ + OH- --> NH3 + H2O [1]<br/>"
         "• New moles NH4+ = 0.0500 - 0.00250 = 0.0475 mol; new moles NH3 = 0.0375 + 0.00250 = 0.0400 mol [1]<br/>"
         "• New pH = 9.25 + log(0.0400 / 0.0475) = 9.25 - 0.075 = 9.175 ≈ 9.18 [1]."),

        ("Question 35: Continuous pH Titration (* Level of Response) (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Moles NaOH = 0.02240 x 0.100 = 2.24 x 10^-3 mol [1]<br/>"
         "• [HA] = 2.24 x 10^-3 / 0.0250 = 0.0896 mol dm^-3 [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• At half-equivalence point: pH = pKa => pKa = 3.82 [1]<br/>"
         "• Ka = 10^-pKa = 10^-3.82 [1]<br/>"
         "• Ka = 1.51 x 10^-4 mol dm^-3 [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive practical protocol. Covers two-buffer calibration (pH 4.00 and 9.20) with rinsing probe with deionised water and blotting with lint-free tissue between buffers. Details apparatus setup: clamp probe with bulb submerged above rotating magnetic stirring flea, ensuring flea cannot hit glass membrane; burette tip positioned near beaker wall. Systematic data collection: record baseline pH; add 1.00 cm^3 portions of NaOH away from equivalence, recording stable pH after each addition; switch to dropwise additions (0.05–0.10 cm^3) as pH rises rapidly near inflection point (from ~20 to 24 cm^3) to precisely define the vertical inflection. Identifies two systematic errors: temperature variance (mitigated by constant water bath or probe temperature compensation) and delayed equilibrium response/flea vortex creating air bubbles on glass bulb (mitigated by moderate stir speed and waiting 5-10 s for steady digital readout).<br/>"
         "• Level 2 (3-4 marks): Clear procedure with calibration and titration details but minor omissions in probe care or dropwise rate near equivalence.<br/>"
         "• Level 1 (1-2 marks): Basic description of pH meter usage and burette additions with superficial calibration.<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Initial pH marked at ~2.4 [1]<br/>"
         "• Buffer plateau showing half-equivalence point at (11.20 cm^3, pH 3.82) [1]<br/>"
         "• Sharp vertical inflection at 22.40 cm^3 with midpoint at pH ~8.6 [1]<br/>"
         "• High pH plateau curving asymptotically towards ~12.5 at excess NaOH [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• The derivative ΔpH / ΔV represents the instantaneous gradient (rate of change of pH) [1]<br/>"
         "• The inflection point on the S-curve corresponds to a sharp, well-defined maximum peak on the first derivative plot [1]<br/>"
         "• The peak maximum can be identified unambiguously to within ±0.05 cm^3, avoiding subjective estimation of the vertical midpoint [1]."),

        ("Question 36: Blood Buffering & Acidosis (15 Marks)",
         "<b>(a)(i) [1 Mark]</b><br/>"
         "• pH = pKa + log10([HCO3-] / [H2CO3]) [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• 7.40 = 6.10 + log10(24.0 / [H2CO3]) => log10(24.0 / [H2CO3]) = 1.30 [1]<br/>"
         "• 24.0 / [H2CO3] = 10^1.30 = 19.95 [1]<br/>"
         "• [H2CO3] = 24.0 / 19.95 = 1.20 mmol dm^-3 [1].<br/><br/>"
         "<b>(a)(iii) [2 Marks]</b><br/>"
         "• Ratio [HCO3-] / [H2CO3] = 24.0 / 1.20 = 20.0 (or 20 : 1) [2].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Cellular metabolism generates continuous large amounts of acidic waste (lactic acid, ketoacids, CO2) but negligible alkaline waste [1]<br/>"
         "• A massive 20-fold excess of base (HCO3-) provides an enormous buffer capacity against acidosis [1]<br/>"
         "• The open respiratory system can rapidly eliminate CO2 to regulate [H2CO3], maintaining stability despite the skewed ratio [1].<br/><br/>"
         "<b>(c)(i) [3 Marks]</b><br/>"
         "• pH = 6.10 + log10(12.0 / 1.20) = 6.10 + log10(10.0) [1]<br/>"
         "• pH = 6.10 + 1.00 = 7.10 [1]<br/>"
         "• This represents severe metabolic acidosis (pH < 7.35) [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• Kussmaul breathing blows off gaseous CO2 from the lungs at an accelerated rate [1]<br/>"
         "• By Le Chatelier's principle, the equilibrium H+(aq) + HCO3-(aq) <=> H2CO3(aq) <=> CO2(aq) + H2O shifts to the right [1]<br/>"
         "• This consumes excess H+ ions, lowering [H2CO3] and elevating blood pH back towards the normal 7.35-7.45 range [1]."),

        ("Question 37: Fermentation Buffers & Ocean Alkalinity (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Citric acid, C6H8O7, and dihydrogen citrate ion, C6H7O7- (or monosodium citrate, C6H7O7Na) [2].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• pH = pKa1 + log([A-] / [HA]) => 3.00 = 3.13 + log([A-] / 0.250) [1]<br/>"
         "• log([A-] / 0.250) = -0.13 => [A-] / 0.250 = 10^-0.13 = 0.7413 [1]<br/>"
         "• [A-] = 0.250 x 0.7413 = 0.1853 mol dm^-3 [1]<br/>"
         "• Mass C6H7O7Na = 0.1853 mol x 214.1 g mol^-1 = 39.68 ≈ 39.7 g [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• Adding Ca(OH)2 supplies hydroxide ions, OH-(aq) [1]<br/>"
         "• OH- neutralises H+ ions in seawater: H+ + OH- --> H2O [1]<br/>"
         "• By Le Chatelier, CO2(aq) + H2O <=> HCO3- + H+ shifts to the right to replenish H+ [1]<br/>"
         "• More atmospheric CO2 dissolves to form bicarbonate, safely storing carbon without lowering ocean pH [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• When pH exceeds 9.0, bicarbonate is converted to carbonate: HCO3- + OH- <=> CO3^2- + H2O [1]<br/>"
         "• High [CO3^2-] and [Ca^2+] exceed the solubility product (Ksp), causing precipitation: Ca^2+(aq) + CO3^2-(aq) --> CaCO3(s) [1]<br/>"
         "• Overall precipitation reaction: Ca^2+(aq) + 2HCO3-(aq) --> CaCO3(s) + CO2(aq) + H2O(l) [2]<br/>"
         "• Precipitation releases gaseous CO2 back into seawater and atmosphere, directly undoing the carbon capture benefit [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 10 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
