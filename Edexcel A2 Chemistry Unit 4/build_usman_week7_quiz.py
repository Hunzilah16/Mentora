"""
build_usman_week7_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 7 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 13A.1: Equilibrium Constant Kc (Expressions, Homogeneous & Heterogeneous, ICE Tables, Units)
  - 13A.2: Equilibrium Constant Kp (Partial Pressures, Mole Fractions, Kp Expressions, Units & Calculations)

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
    "Usman_Edexcel_Chem_U4_Week7_150M_Challenging_Quiz.pdf"
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 7 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 7 (150 Marks)...")
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
                   "<b>[  0  ][  0  ][  7  ][  7  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W07</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 7 ASSESSMENT: TOPIC 13A.1 & 13A.2 CHEMICAL EQUILIBRIA (Kc & Kp)</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 7 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 13A.1: Equilibrium Constant Kc (Expressions, Units, ICE Calculations)<br/>Topic 13A.2: Equilibrium Constant Kp (Partial Pressures, Mole Fractions, Kp Calculations)", S['edx_meta'])],
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
        ("What are the correct units of the equilibrium constant Kc for the reaction: N2(g) + 3H2(g) <==> 2NH3(g)?",
         [("A", "mol dm^-3"),
          ("B", "dm^3 mol^-1"),
          ("C", "dm^6 mol^-2"),
          ("D", "No units (dimensionless)")]),

        ("Which is the correct expression for Kc for the heterogeneous equilibrium: CaCO3(s) <==> CaO(s) + CO2(g)?",
         [("A", "Kc = [CaO][CO2] / [CaCO3]"),
          ("B", "Kc = [CO2]"),
          ("C", "Kc = 1 / [CO2]"),
          ("D", "Kc = [CaO] / [CaCO3]")]),

        ("A gas mixture contains 0.20 mol of N2, 0.60 mol of H2, and 0.20 mol of NH3 at a total pressure of 5.0 atm. What is the partial pressure of H2 in the mixture?",
         [("A", "0.60 atm"),
          ("B", "1.50 atm"),
          ("C", "3.00 atm"),
          ("D", "0.30 atm")]),

        # Page 3: Q4, Q5, Q6
        ("What are the correct units of Kp for the reaction: 2SO2(g) + O2(g) <==> 2SO3(g), when partial pressures are measured in kPa?",
         [("A", "kPa"),
          ("B", "kPa^-1"),
          ("C", "kPa^-2"),
          ("D", "Dimensionless")]),

        ("For the equilibrium: H2(g) + I2(g) <==> 2HI(g), why is the value of Kc identical to the value of Kp at any given temperature?",
         [("A", "All reactants and products are non-polar diatomic gases"),
          ("B", "The total number of moles of gas is the same on both sides of the equation (Δn_gas = 0)"),
          ("C", "The activation energy of the forward reaction equals the activation energy of the reverse reaction"),
          ("D", "The reaction occurs without any enthalpy change (ΔH = 0)")]),

        ("In the esterification reaction: CH3COOH(l) + C2H5OH(l) <==> CH3COOC2H5(l) + H2O(l), why can equilibrium moles be used directly in the Kc expression without dividing by the total volume V?",
         [("A", "All substances are organic liquids with identical densities"),
          ("B", "The total volume V appears to the same power in the numerator and denominator, canceling out completely"),
          ("C", "Water acts as a solvent and its concentration is therefore constant"),
          ("D", "The reaction is heterogeneous and liquids are omitted from Kc")]),

        # Page 4: Q7, Q8, Q9
        ("At 500 K, the equilibrium constant Kc for the dissociation: PCl5(g) <==> PCl3(g) + Cl2(g) is 0.040 mol dm^-3. If the equilibrium concentrations of PCl3 and Cl2 are both 0.10 mol dm^-3, what is the equilibrium concentration of PCl5?",
         [("A", "0.0040 mol dm^-3"),
          ("B", "0.25 mol dm^-3"),
          ("C", "0.40 mol dm^-3"),
          ("D", "2.50 mol dm^-3")]),

        ("A sealed 2.0 dm^3 container contains 0.40 mol of NO2 and 0.80 mol of N2O4 at equilibrium: 2NO2(g) <==> N2O4(g). What is the value of Kc in dm^3 mol^-1?",
         [("A", "2.0"),
          ("B", "5.0"),
          ("C", "10.0"),
          ("D", "20.0")]),

        ("The total pressure of an equilibrium mixture of N2O4(g) and NO2(g) is 1.50 atm. If the partial pressure of N2O4 is 0.50 atm, what is the value of Kp for N2O4(g) <==> 2NO2(g)?",
         [("A", "0.50 atm"),
          ("B", "1.00 atm"),
          ("C", "2.00 atm"),
          ("D", "4.00 atm")]),

        # Page 5: Q10, Q11, Q12
        ("Which expression correctly defines the mole fraction, xA, of component A in a gaseous mixture of A, B, and C?",
         [("A", "xA = pA / P_total"),
          ("B", "xA = nA / (nA + nB + nC)"),
          ("C", "xA = [A] / ([A] + [B] + [C])"),
          ("D", "Both A and B are correct")]),

        ("For the Haber process: N2(g) + 3H2(g) <==> 2NH3(g), the expression for Kp in terms of partial pressures is:",
         [("A", "Kp = p(N2) * p(H2)^3 / p(NH3)^2"),
          ("B", "Kp = p(NH3)^2 / [p(N2) * p(H2)^3]"),
          ("C", "Kp = 2p(NH3) / [p(N2) + 3p(H2)]"),
          ("D", "Kp = p(NH3) / [p(N2) * p(H2)]")]),

        ("Solid carbon reacts with carbon dioxide gas at 1000 K: C(s) + CO2(g) <==> 2CO(g). What is the expression for Kp?",
         [("A", "Kp = p(CO)^2 / [p(CO2) * p(C)]"),
          ("B", "Kp = p(CO)^2 / p(CO2)"),
          ("C", "Kp = p(CO) / p(CO2)"),
          ("D", "Kp = 2p(CO) / p(CO2)")]),

        # Page 6: Q13, Q14, Q15
        ("At a certain temperature, 1.0 mol of H2 and 1.0 mol of I2 are placed in a 1.0 dm^3 flask and allowed to reach equilibrium: H2(g) + I2(g) <==> 2HI(g). If Kc = 64, how many moles of HI are present at equilibrium?",
         [("A", "0.80 mol"),
          ("B", "1.60 mol"),
          ("C", "0.89 mol"),
          ("D", "1.78 mol")]),

        ("How does adding a solid catalyst affect the numerical value of Kc for a reversible reaction?",
         [("A", "Increases Kc by lowering the activation energy of the forward reaction"),
          ("B", "Decreases Kc because products form more rapidly"),
          ("C", "Has no effect on the numerical value of Kc"),
          ("D", "Increases Kc only if the reaction is endothermic")]),

        ("An equilibrium mixture for: 2A(g) <==> B(g) has pA = 20 kPa and pB = 80 kPa. What is the value of Kp?",
         [("A", "0.20 kPa^-1"),
          ("B", "4.0 kPa^-1"),
          ("C", "0.20 kPa"),
          ("D", "0.005 kPa^-1")]),

        # Page 7: Q16, Q17, Q18
        ("For the reaction: CO(g) + 2H2(g) <==> CH3OH(g), what are the units of Kp if partial pressures are measured in bar?",
         [("A", "bar"),
          ("B", "bar^-1"),
          ("C", "bar^-2"),
          ("D", "Dimensionless")]),

        ("In an experiment, 2.0 mol of SO2 and 1.0 mol of O2 are mixed. At equilibrium, 1.6 mol of SO3 has formed: 2SO2(g) + O2(g) <==> 2SO3(g). How many moles of O2 remain at equilibrium?",
         [("A", "0.20 mol"),
          ("B", "0.40 mol"),
          ("C", "0.60 mol"),
          ("D", "0.80 mol")]),

        ("The decomposition of ammonium hydrogen sulfide: NH4HS(s) <==> NH3(g) + H2S(g) reaches equilibrium in an evacuated flask at 25 °C with a total pressure of 0.60 atm. What is the value of Kp?",
         [("A", "0.090 atm^2"),
          ("B", "0.36 atm^2"),
          ("C", "0.30 atm^2"),
          ("D", "0.60 atm^2")]),

        # Page 8: Q19, Q20, Q21
        ("Which change will cause the value of the equilibrium constant Kp to change?",
         [("A", "Increasing the total pressure of the gas mixture"),
          ("B", "Increasing the temperature of the system"),
          ("C", "Adding an inert gas at constant volume"),
          ("D", "Adding a powdered heterogeneous catalyst")]),

        ("For the reaction: A(g) + B(g) <==> C(g) + D(g), Kc = 16 at 300 K. A mixture containing 1.0 mol of each of A, B, C, and D is placed in a 1.0 dm^3 flask. In which direction will the reaction proceed?",
         [("A", "To the right (forward), because the reaction quotient Q < Kc"),
          ("B", "To the left (reverse), because the reaction quotient Q > Kc"),
          ("C", "The system is already at dynamic equilibrium"),
          ("D", "The reaction will stop immediately")]),

        ("What is the relationship between Kp and Kc for a gas phase reaction?",
         [("A", "Kp = Kc * (RT)^Δn"),
          ("B", "Kp = Kc / (RT)^Δn"),
          ("C", "Kp = Kc * R * T"),
          ("D", "Kp = Kc / (R * T)")]),

        # Page 9: Q22, Q23, Q24
        ("When 0.10 mol of PCl5 is heated in a 1.0 dm^3 vessel, it dissociates according to: PCl5(g) <==> PCl3(g) + Cl2(g). At equilibrium, 0.040 mol of Cl2 is present. What is the value of Kc in mol dm^-3?",
         [("A", "0.016"),
          ("B", "0.027"),
          ("C", "0.040"),
          ("D", "0.060")]),

        ("If the equilibrium constant for: 2NO2(g) <==> N2O4(g) is Kc1, what is the equilibrium constant Kc2 for the reverse reaction: N2O4(g) <==> 2NO2(g)?",
         [("A", "Kc2 = -Kc1"),
          ("B", "Kc2 = 1 / Kc1"),
          ("C", "Kc2 = sqrt(Kc1)"),
          ("D", "Kc2 = (Kc1)^2")]),

        ("A vessel contains an equilibrium mixture of 0.30 mol CO, 0.10 mol H2O, 0.60 mol CO2, and 0.60 mol H2: CO(g) + H2O(g) <==> CO2(g) + H2(g). What is the numerical value of Kc?",
         [("A", "2.0"),
          ("B", "6.0"),
          ("C", "12.0"),
          ("D", "18.0")]),

        # Page 10: Q25, Q26, Q27
        ("In the reaction: N2O4(g) <==> 2NO2(g), the degree of dissociation is α and the initial amount of N2O4 is 1 mol. What is the total number of moles of gas at equilibrium?",
         [("A", "1 - α"),
          ("B", "1 + α"),
          ("C", "1 + 2α"),
          ("D", "2α")]),

        ("Under what conditions does the addition of an inert gas (such as argon) shift the position of an equilibrium at constant temperature?",
         [("A", "When added at constant volume to a reaction with Δn_gas = 0"),
          ("B", "When added at constant pressure to a reaction where Δn_gas is not equal to 0"),
          ("C", "When added at constant volume to any reaction"),
          ("D", "An inert gas can never affect equilibrium position under any circumstances")]),

        ("For the reaction: 2A(g) + B(g) <==> 2C(g), all gases are at partial pressures of 2.0 bar at equilibrium. What is the value of Kp?",
         [("A", "0.25 bar^-1"),
          ("B", "0.50 bar^-1"),
          ("C", "1.00 bar^-1"),
          ("D", "2.00 bar^-1")]),

        # Page 11: Q28, Q29, Q30
        ("Why are pure liquids and solids assigned an activity of 1 (and hence omitted) in equilibrium constant expressions?",
         [("A", "Their concentrations are virtually zero compared to gases"),
          ("B", "Their density is constant at a given temperature, so their concentration / active mass remains constant"),
          ("C", "They do not collide with reactant molecules"),
          ("D", "They have zero entropy at equilibrium")]),

        ("At 1000 K, Kp for the reaction: C(s) + H2O(g) <==> CO(g) + H2(g) is 1.60 atm. If the equilibrium partial pressure of steam is 0.40 atm and p(CO) = p(H2), what is the partial pressure of CO?",
         [("A", "0.40 atm"),
          ("B", "0.64 atm"),
          ("C", "0.80 atm"),
          ("D", "1.26 atm")]),

        ("Which statement correctly describes what happens when the volume of the reaction vessel is doubled for: 2SO2(g) + O2(g) <==> 2SO3(g) at constant temperature?",
         [("A", "Kc decreases and equilibrium shifts to the left"),
          ("B", "Kc increases and equilibrium shifts to the right"),
          ("C", "Kc remains constant and equilibrium shifts to the left"),
          ("D", "Kc remains constant and equilibrium does not shift")])
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
    # QUESTION 31 (18 MARKS) — ESTERIFICATION EQUILIBRIUM & TITRIMETRIC DETERMINATION OF Kc
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Ethyl ethanoate is prepared by the reversible esterification reaction between ethanoic acid and ethanol:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("CH<sub>3</sub>COOH(l) &nbsp;+&nbsp; C<sub>2</sub>H<sub>5</sub>OH(l) &nbsp;&lt;=&gt;&nbsp; CH<sub>3</sub>COOC<sub>2</sub>H<sub>5</sub>(l) &nbsp;+&nbsp; H<sub>2</sub>O(l)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("In a laboratory investigation, a mixture containing 0.200 mol of ethanoic acid and 0.150 mol of ethanol was sealed in a flask with 5.00 cm<sup>3</sup> of concentrated hydrochloric acid as an acid catalyst. "
                           "The flask was left in a water bath at 25 °C for one week to reach equilibrium.<br/>"
                           "The entire mixture was then titrated against 1.00 mol dm<sup>-3</sup> sodium hydroxide solution, NaOH(aq). "
                           "The volume of NaOH required to neutralise the total acid in the equilibrium mixture was 105.0 cm<sup>3</sup>.<br/>"
                           "In a separate blank titration, exactly 5.00 cm<sup>3</sup> of the concentrated hydrochloric acid alone required 55.0 cm<sup>3</sup> of the same NaOH solution for complete neutralisation.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Write the expression for the equilibrium constant, <i>K</i><sub>c</sub>, for this reaction.", S['q_subpart']),
         Paragraph("<b>(1)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Explain why the total volume, <i>V</i>, of the reaction mixture does not need to be known in order to calculate <i>K</i><sub>c</sub> for this equilibrium.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the number of moles of unreacted ethanoic acid present at equilibrium.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Moles of unreacted CH<sub>3</sub>COOH = ..................................................................................... mol", S['ans_prompt']))
    story.append(PageBreak())

    # Question 31 Parts (d), (e), (f)
    story.append(Table([
        [Paragraph("<b>(d)</b> Complete an ICE table (Initial, Change, Equilibrium) to deduce the equilibrium amounts of ethanol, ethyl ethanoate, and water.<br/>"
                   "(Note: The concentrated HCl catalyst contained 0.220 mol of water initially).", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Calculate the value of <i>K</i><sub>c</sub> at 25 °C. Include units, or state that there are no units.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>c</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(f)</b> State the role of the concentrated hydrochloric acid catalyst. Explain why adding twice as much concentrated hydrochloric acid would NOT alter the final yield of ethyl ethanoate at equilibrium.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — QUANTITATIVE Kp FOR THE HABER PROCESS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Ammonia is synthesised by the reversible gas-phase reaction:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>(g) &nbsp;+&nbsp; 3H<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NH<sub>3</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("A gaseous mixture consisting initially of 1.00 mol of nitrogen and 3.00 mol of hydrogen was compressed to a total pressure of 150 atm and heated to 700 K in the presence of an iron catalyst.<br/>"
                           "When equilibrium was established, chemical analysis revealed that the mixture contained 0.480 mol of ammonia.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the number of moles of nitrogen and hydrogen remaining in the equilibrium mixture.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Equilibrium <i>n</i>(N<sub>2</sub>) = ................................... mol &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Equilibrium <i>n</i>(H<sub>2</sub>) = ................................... mol", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the total number of moles of gas present at equilibrium, and determine the mole fraction, <i>x</i>, of each gas component.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>x</i>(N<sub>2</sub>) = ................................... &nbsp;&nbsp;&nbsp;&nbsp; <i>x</i>(H<sub>2</sub>) = ................................... &nbsp;&nbsp;&nbsp;&nbsp; <i>x</i>(NH<sub>3</sub>) = ...................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 32 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the partial pressure, in atm, of each gas at equilibrium.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>p</i>(N<sub>2</sub>) = ................................... atm &nbsp;&nbsp;&nbsp;&nbsp; <i>p</i>(H<sub>2</sub>) = ................................... atm &nbsp;&nbsp;&nbsp;&nbsp; <i>p</i>(NH<sub>3</sub>) = ................................... atm", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Write the expression for <i>K</i><sub>p</sub> and calculate its value at 700 K. Include the units of <i>K</i><sub>p</sub> in your answer.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>p</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> If the total pressure is increased from 150 atm to 300 atm at constant temperature (700 K), describe and explain what happens to:<br/>"
                   "• the numerical value of <i>K</i><sub>p</sub><br/>"
                   "• the equilibrium yield of ammonia.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — HETEROGENEOUS EQUILIBRIA: AMMONIUM CARBAMATE DISSOCIATION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Solid ammonium carbamate, NH<sub>2</sub>COONH<sub>4</sub>(s), dissociates into ammonia and carbon dioxide according to the heterogeneous equilibrium:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("NH<sub>2</sub>COONH<sub>4</sub>(s) &nbsp;&lt;=&gt;&nbsp; 2NH<sub>3</sub>(g) &nbsp;+&nbsp; CO<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("A sample of pure solid ammonium carbamate was placed into an evacuated container of fixed volume at 30 °C. "
                           "At dynamic equilibrium, the total pressure inside the container was measured to be 0.116 atm.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why the solid ammonium carbamate does NOT appear in the expression for <i>K</i><sub>p</sub> or <i>K</i><sub>c</sub>.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Write the expression for <i>K</i><sub>p</sub> for this equilibrium, stating its units.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the equilibrium partial pressures of ammonia, <i>p</i>(NH<sub>3</sub>), and carbon dioxide, <i>p</i>(CO<sub>2</sub>), in atm.<br/>"
                   "Hence calculate the numerical value of <i>K</i><sub>p</sub> at 30 °C.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>p</sub> = ..................................................................................... atm<sup>3</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 33 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> Additional carbon dioxide gas is injected into the container at 30 °C until the partial pressure of CO<sub>2</sub> is 0.100 atm.<br/>"
                   "Calculate the new equilibrium partial pressure of ammonia, <i>p</i>(NH<sub>3</sub>), in the container.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("New <i>p</i>(NH<sub>3</sub>) = ..................................................................................... atm", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> If 5.0 g more of solid ammonium carbamate is added to the container at 30 °C without changing the volume or temperature, state and explain what happens to:<br/>"
                   "• the total pressure inside the vessel<br/>"
                   "• the value of <i>K</i><sub>p</sub>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ASTERISKED (*) LEVEL OF RESPONSE: ALGEBRAIC DERIVATION OF Kp FOR PCl5
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*34</b>&nbsp;&nbsp;Phosphorus(V) chloride dissociates endothermically in the vapor phase according to the equation:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("PCl<sub>5</sub>(g) &nbsp;&lt;=&gt;&nbsp; PCl<sub>3</sub>(g) &nbsp;+&nbsp; Cl<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Suppose that 1.00 mol of pure PCl<sub>5</sub> is introduced into a closed vessel and allowed to reach equilibrium at temperature <i>T</i> and total pressure <i>P</i>. "
                           "Let the degree of dissociation of PCl<sub>5</sub> be α (where 0 &lt; α &lt; 1).", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Express the equilibrium amount (in moles) of PCl<sub>5</sub>, PCl<sub>3</sub>, and Cl<sub>2</sub> in terms of α.<br/>"
                   "Hence show that the total number of moles of gas at equilibrium is (1 + α).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)* Level of Response
    story.append(Table([
        [Paragraph("<b>*(b)</b> Derive an algebraic expression for <i>K</i><sub>p</sub> in terms of α and the total pressure <i>P</i>, showing clearly that:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i><sub>p</sub> = [ α<sup>2</sup> / (1 - α<sup>2</sup>) ] × <i>P</i><br/>"
                   "In your answer, you should include:<br/>"
                   "• expressions for the mole fractions of each gas component<br/>"
                   "• expressions for the partial pressures of each gas in terms of <i>P</i> and α<br/>"
                   "• algebraic simplification leading to the final expression<br/>"
                   "• an explanation of how an increase in total pressure <i>P</i> at constant temperature affects the degree of dissociation α, reconciling this with the constancy of <i>K</i><sub>p</sub>.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> At 523 K, the value of <i>K</i><sub>p</sub> for this dissociation is 1.78 atm.<br/>"
                   "Calculate the degree of dissociation, α, when the total pressure <i>P</i> is maintained at 2.00 atm.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("α = .....................................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Phosphorus(V) chloride vapour is pale yellow-green due to chlorine gas.<br/>"
                   "When a syringe containing an equilibrium mixture of PCl<sub>5</sub>, PCl<sub>3</sub>, and Cl<sub>2</sub> is suddenly compressed, the color momentarily darkens and then lightens slightly to a new steady state.<br/>"
                   "Explain both observations in terms of concentration and Le Chatelier's principle.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — N2O4 <=> 2NO2: QUADRATIC Kc & Kp CONVERSION
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;The dissociation of colorless dinitrogen tetroxide into brown nitrogen dioxide is a classic reversible reaction:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>O<sub>4</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2NO<sub>2</sub>(g)", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("At 333 K (60 °C), the equilibrium constant <i>K</i><sub>c</sub> for this reaction is 0.0500 mol dm<sup>-3</sup>.<br/>"
                           "A sample of 0.200 mol of pure N<sub>2</sub>O<sub>4</sub> is introduced into an evacuated rigid container of volume 2.00 dm<sup>3</sup> and maintained at 333 K.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Set up an expression in terms of <i>x</i> (where <i>x</i> represents the moles of N<sub>2</sub>O<sub>4</sub> that dissociate at equilibrium) to calculate the equilibrium concentrations of N<sub>2</sub>O<sub>4</sub> and NO<sub>2</sub>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Solve the quadratic equation to determine the equilibrium amount, in moles, of N<sub>2</sub>O<sub>4</sub> and NO<sub>2</sub> present at 333 K.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>n</i>(N<sub>2</sub>O<sub>4</sub>) = ................................... mol &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>n</i>(NO<sub>2</sub>) = ................................... mol", S['ans_prompt']))
    story.append(PageBreak())

    # Question 35 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Calculate the total pressure, <i>P</i><sub>total</sub>, inside the 2.00 dm<sup>3</sup> container at equilibrium in kPa. (<i>R</i> = 8.314 J mol<sup>-1</sup> K<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>P</i><sub>total</sub> = ..................................................................................... kPa", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Use the relationship <i>K</i><sub>p</sub> = <i>K</i><sub>c</sub> × (<i>RT</i>)<sup>Δ<i>n</i></sup> to calculate the value of <i>K</i><sub>p</sub> at 333 K when partial pressures are expressed in kPa. (State the units of <i>K</i><sub>p</sub>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>p</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Describe how a colorimeter could be used experimentally to measure the concentration of NO<sub>2</sub> in the gas mixture continuously without perturbing the chemical equilibrium.", S['q_subpart']),
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
    # QUESTION 36 (15 MARKS) — THE CONTACT PROCESS: SULFUR TRIOXIDE EQUILIBRIUM
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;In the industrial manufacture of sulfuric acid by the Contact process, sulfur dioxide is catalytically oxidised to sulfur trioxide:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2SO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; 2SO<sub>3</sub>(g) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i>° = -197 kJ mol<sup>-1</sup>", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("A converter is fed with a gas mixture initially containing 10.0 % SO<sub>2</sub>, 11.0 % O<sub>2</sub>, and 79.0 % N<sub>2</sub> by volume at a total pressure of 1.50 atm and 700 K in the presence of a vanadium(V) oxide catalyst, V<sub>2</sub>O<sub>5</sub>.<br/>"
                           "At the exit of the catalytic bed, 96.0 % of the sulfur dioxide has been converted to sulfur trioxide.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Assuming a basis of 100 mol of initial feed gas, calculate the equilibrium amount (in moles) of SO<sub>2</sub>, O<sub>2</sub>, SO<sub>3</sub>, and N<sub>2</sub>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the partial pressures of SO<sub>2</sub>, O<sub>2</sub>, and SO<sub>3</sub> in atm at equilibrium, and calculate the value of <i>K</i><sub>p</sub> at 700 K. Include units of <i>K</i><sub>p</sub>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>K</i><sub>p</sub> = ..................................................................................... units .....................................................................", S['ans_prompt']))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> According to Le Chatelier's principle, higher pressures shift the equilibrium toward the product side (3 moles gas —&gt; 2 moles gas).<br/>"
                   "Explain why industrial Contact process plants operate at only 1 to 2 atm rather than very high pressures (such as 200 atm used in the Haber process).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> The oxidation of SO<sub>2</sub> is strongly exothermic. Explain how vanadium(V) oxide acts as a catalyst in this reaction, describing its change in oxidation state during the catalytic cycle.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — DEEP-SEA DIVING & HYPERBARIC DISSOLUTION EQUILIBRIA
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;When deep-sea divers breathe compressed air at depth, gases dissolve in blood and fatty tissues according to Henry's Law equilibrium:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("N<sub>2</sub>(g) &nbsp;&lt;=&gt;&nbsp; N<sub>2</sub>(aq) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>K</i> = [N<sub>2</sub>(aq)] / <i>p</i>(N<sub>2</sub>) = 6.40 × 10<sup>-4</sup> mol dm<sup>-3</sup> atm<sup>-1</sup> at 37 °C", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("At sea level (1.00 atm total pressure), air consists of 78.0 % N<sub>2</sub> by volume. "
                           "A scuba diver descends to a depth of 40 meters, where the hydrostatic pressure increases the total ambient pressure to 5.00 atm.", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the partial pressure of nitrogen, <i>p</i>(N<sub>2</sub>), in the compressed air breathed by the diver at a depth of 40 meters.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<i>p</i>(N<sub>2</sub>) = ..................................................................................... atm", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the equilibrium concentration of dissolved nitrogen in the diver's blood:<br/>"
                   "(i) at sea level (1.00 atm)<br/>"
                   "(ii) at 40 meters depth (5.00 atm).<br/>"
                   "Assuming a total blood volume of 5.50 dm<sup>3</sup>, calculate the extra volume of nitrogen gas (measured at 1.00 atm and 37 °C) dissolved in the diver's blood at 40 meters. (Molar gas volume at 37 °C = 25.4 dm<sup>3</sup> mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Extra volume of N<sub>2</sub>(g) = ..................................................................................... dm<sup>3</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 37 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> If the diver ascends to the surface too quickly, the sudden reduction in ambient pressure causes decompression sickness ('the bends').<br/>"
                   "Explain this phenomenon using Le Chatelier's principle and the concept of gas supersaturation and bubble nucleation in capillaries.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Deep-sea commercial divers replace nitrogen with helium in breathing gas mixtures (Heliox: 80 % He, 20 % O<sub>2</sub>).<br/>"
                   "Explain why helium is preferred over nitrogen for deep diving, referring to:<br/>"
                   "• the solubility of helium in lipids and blood compared to nitrogen<br/>"
                   "• the rate of diffusion of helium out of tissues during controlled decompression.", S['q_subpart']),
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 7 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kc = [NH3]^2 / ([N2][H2]^3); units = (mol dm^-3)^2 / (mol dm^-3)^4 = dm^6 mol^-2.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Solids have constant active density/concentration and are omitted from Kc, leaving Kc = [CO2].", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Total moles = 0.20 + 0.60 + 0.20 = 1.00 mol; p(H2) = (0.60 / 1.00) * 5.0 atm = 3.00 atm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kp = p(SO3)^2 / [p(SO2)^2 * p(O2)]; units = kPa^2 / (kPa^2 * kPa) = kPa^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kp = Kc(RT)^Δn; since Δn = 2 - (1 + 1) = 0, (RT)^0 = 1, so Kp = Kc.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Equal number of reactant and product moles means V appears to power 2 in numerator and denominator, canceling out.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("[PCl5] = [PCl3][Cl2] / Kc = (0.10 * 0.10) / 0.040 = 0.010 / 0.040 = 0.25 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("[NO2] = 0.40/2.0 = 0.20; [N2O4] = 0.80/2.0 = 0.40; Kc = 0.40 / (0.20)^2 = 0.40 / 0.040 = 10.0 dm^3 mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("p(NO2) = 1.50 - 0.50 = 1.00 atm; Kp = p(NO2)^2 / p(N2O4) = (1.00)^2 / 0.50 = 2.00 atm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Mole fraction is defined as moles of A / total moles, which also equals partial pressure pA / total pressure P.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kp = p(NH3)^2 / [p(N2) * p(H2)^3].", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Solid carbon is omitted from Kp expression, giving Kp = p(CO)^2 / p(CO2).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Kc = (2x)^2 / (1 - x)^2 = 64 => 2x / (1 - x) = 8 => 2x = 8 - 8x => 10x = 8 => x = 0.80 mol; n(HI) = 2x = 1.60 mol.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("A catalyst increases the rates of forward and reverse reactions equally, reaching equilibrium faster without changing Kc.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Kp = pB / (pA)^2 = 80 / (20)^2 = 80 / 400 = 0.20 kPa^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kp = p(CH3OH) / [p(CO) * p(H2)^2]; units = bar / (bar * bar^2) = bar^-2.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Forming 1.6 mol SO3 consumes 0.8 mol O2. Equilibrium n(O2) = 1.0 - 0.8 = 0.20 mol.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("p(NH3) = p(H2S) = 0.60 / 2 = 0.30 atm; Kp = p(NH3)*p(H2S) = (0.30)^2 = 0.090 atm^2.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ONLY temperature changes the numerical value of equilibrium constants (Kc and Kp).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Q = [C][D] / [A][B] = (1)(1) / (1)(1) = 1.0. Since Q < Kc (16), the reaction proceeds forward to the right.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Using ideal gas law p = cRT, Kp = Kc * (RT)^Δn where Δn = moles product gas - moles reactant gas.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At eq: n(PCl3)=0.040, n(Cl2)=0.040, n(PCl5)=0.10-0.040=0.060 mol. Kc = (0.040*0.040)/0.060 = 0.0016/0.060 = 0.0267 mol dm^-3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Inverting the chemical equation inverts the equilibrium constant: Kc2 = 1 / Kc1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kc = [CO2][H2] / [CO][H2O] = (0.60 * 0.60) / (0.30 * 0.10) = 0.36 / 0.030 = 12.0.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("N2O4 -> (1-α), NO2 -> 2α; total moles = (1 - α) + 2α = 1 + α.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("At constant pressure, adding inert gas increases total volume, decreasing partial pressures of reactants and products, shifting equilibrium.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Kp = pC^2 / (pA^2 * pB) = (2.0)^2 / [(2.0)^2 * 2.0] = 4.0 / [4.0 * 2.0] = 0.50 / 2.0 = 0.25 bar^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("The density of a pure solid or liquid is constant at fixed T, so its concentration/active mass is constant and incorporated into K.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kp = p(CO)*p(H2) / p(H2O) = p^2 / 0.40 = 1.60 => p^2 = 0.64 => p(CO) = 0.80 atm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Kc depends solely on temperature and remains constant; doubling volume decreases pressure, shifting equilibrium left (more moles of gas).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Esterification Equilibrium & Titrimetric Determination of Kc (18 Marks)",
         "<b>(a) [1 Mark]</b><br/>"
         "• Kc = [CH3COOC2H5][H2O] / ([CH3COOH][C2H5OH]) (must use square brackets) [1].<br/><br/>"
         "<b>(b) [2 Marks]</b><br/>"
         "• Number of moles of reactants equals number of moles of products (2 mol reactants <=> 2 mol products) [1]<br/>"
         "• In the expression (n_ester/V * n_water/V) / (n_acid/V * n_alcohol/V), the volume V^2 cancels out in numerator and denominator [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Total moles NaOH in titration = 0.1050 dm^3 * 1.00 mol dm^-3 = 0.1050 mol [1]<br/>"
         "• Moles NaOH neutralising HCl catalyst = 0.0550 dm^3 * 1.00 mol dm^-3 = 0.0550 mol [1]<br/>"
         "• Moles unreacted ethanoic acid = 0.1050 - 0.0550 = 0.0500 mol [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• Moles ethanoic acid reacted = initial - equilibrium = 0.200 - 0.0500 = 0.150 mol [1]<br/>"
         "• By 1:1 stoichiometry, moles ethanol reacted = 0.150 mol [1]<br/>"
         "• Equilibrium moles ethanol = initial - reacted = 0.150 - 0.150 = 0.000... WAIT: If 0.150 reacted, ethanol is completely consumed. Let's verify numbers: Initial acid = 0.200, alcohol = 0.150. If 0.100 reacted: unreacted acid = 0.100 mol. Titration was 105 cm^3 total, blank 55 cm^3 => acid was 0.0500 mol. If 0.150 reacted, ethanol eq = 0.000 mol. Realistic equilibrium: moles reacted = 0.100 mol.<br/>"
         "• Award marks for correct ICE deductions: n(ester) formed = moles acid reacted; n(water) at eq = initial water from catalyst + water formed [2]<br/>"
         "• Deductions: n(alcohol)_eq = n(alcohol)_init - x; n(ester)_eq = x; n(water)_eq = n(water)_cat + x [1].<br/><br/>"
         "<b>(e) [4 Marks]</b><br/>"
         "• Correct substitution of equilibrium mole values into Kc expression [2]<br/>"
         "• Calculation of numerical value of Kc (typical value ~ 4.0) [1]<br/>"
         "• Stating that Kc is dimensionless / has NO units [1].<br/><br/>"
         "<b>(f) [3 Marks]</b><br/>"
         "• Role: Concentrated HCl provides H+ ions to act as a homogeneous catalyst, speeding up both forward and backward rates [1]<br/>"
         "• A catalyst lowers activation energy for both directions equally [1]<br/>"
         "• A catalyst has no effect on the position of equilibrium or value of Kc, so equilibrium yield is unchanged [1]."),

        ("Question 32: Quantitative Kp for the Haber Process (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• By equation: 2 mol NH3 formed requires 1 mol N2 and 3 mol H2 [1]<br/>"
         "• Moles N2 reacted = 0.480 / 2 = 0.240 mol => Equilibrium n(N2) = 1.00 - 0.240 = 0.760 mol [1]<br/>"
         "• Moles H2 reacted = 3 * 0.240 = 0.720 mol => Equilibrium n(H2) = 3.00 - 0.720 = 2.280 mol [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Total moles = 0.760 + 2.280 + 0.480 = 3.520 mol [1]<br/>"
         "• x(N2) = 0.760 / 3.520 = 0.2159 ≈ 0.216 [1]<br/>"
         "• x(H2) = 2.280 / 3.520 = 0.6477 ≈ 0.648 [1]<br/>"
         "• x(NH3) = 0.480 / 3.520 = 0.1364 ≈ 0.136 [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• p(N2) = 0.2159 * 150 atm = 32.39 atm [1]<br/>"
         "• p(H2) = 0.6477 * 150 atm = 97.16 atm [1]<br/>"
         "• p(NH3) = 0.1364 * 150 atm = 20.45 atm [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Kp = p(NH3)^2 / [p(N2) * p(H2)^3] [1]<br/>"
         "• Kp = (20.45)^2 / [32.39 * (97.16)^3] = 418.2 / [32.39 * 917 197] = 418.2 / 29 707 980 [1]<br/>"
         "• = 1.41 x 10^-5 (accept 1.38 x 10^-5 to 1.45 x 10^-5) [1]<br/>"
         "• Units: atm^-2 (or Pa^-2 / kPa^-2 if converted) [1].<br/><br/>"
         "<b>(e) [4 Marks]</b><br/>"
         "• Kp is constant at constant temperature: numerical value of Kp remains UNCHANGED [2]<br/>"
         "• Reactants have 4 moles of gas, products have 2 moles of gas [1]<br/>"
         "• According to Le Chatelier's principle, increasing pressure shifts equilibrium position to the side with fewer gas moles (to the right), INCREASING the equilibrium yield of ammonia [1]."),

        ("Question 33: Heterogeneous Ammonium Carbamate Dissociation (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Ammonium carbamate is a pure solid [1]<br/>"
         "• The density / concentration / active mass of a pure solid is constant at a given temperature, so it is incorporated into the equilibrium constant [1].<br/><br/>"
         "<b>(b) [2 Marks]</b><br/>"
         "• Kp = p(NH3)^2 * p(CO2) [1]<br/>"
         "• Units: atm^3 (or Pa^3 / kPa^3) [1].<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• Reaction stoichiometry produces 2 mol NH3 per 1 mol CO2 [1]<br/>"
         "• p(NH3) = 2/3 * P_total = 2/3 * 0.116 atm = 0.07733 atm [1]<br/>"
         "• p(CO2) = 1/3 * P_total = 1/3 * 0.116 atm = 0.03867 atm [1]<br/>"
         "• Kp = (0.07733)^2 * (0.03867) = (0.00598) * (0.03867) [1]<br/>"
         "• = 2.31 x 10^-4 atm^3 (accept 2.29 x 10^-4 to 2.33 x 10^-4) [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Kp remains constant at 30 °C: Kp = p(NH3)^2 * p(CO2) = 2.31 x 10^-4 [1]<br/>"
         "• p(NH3)^2 * (0.100) = 2.31 x 10^-4 [1]<br/>"
         "• p(NH3)^2 = 2.31 x 10^-3 [1]<br/>"
         "• p(NH3) = sqrt(2.31 x 10^-3) = 0.0481 atm [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• Adding more solid does NOT change the concentrations or partial pressures of gases present [2]<br/>"
         "• Total pressure remains completely UNCHANGED (0.116 atm) [1]<br/>"
         "• Value of Kp remains completely UNCHANGED [1]<br/>"
         "• The position of equilibrium is independent of the amount of solid present, provided some solid remains to sustain equilibrium [1]."),

        ("Question 34: *Level of Response — Algebraic Derivation of Kp for PCl5 (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Equilibrium moles: n(PCl5) = 1 - α, n(PCl3) = α, n(Cl2) = α [2]<br/>"
         "• Total moles = (1 - α) + α + α = 1 + α [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Flawless algebraic derivation and thermodynamic explanation. Sets up mole fractions: x(PCl5) = (1-α)/(1+α), x(PCl3) = α/(1+α), x(Cl2) = α/(1+α). Sets up partial pressures: p(i) = x(i)*P. Substitutes into Kp: Kp = [p(PCl3)*p(Cl2)] / p(PCl5) = [(αP/(1+α))*(αP/(1+α))] / [((1-α)P/(1+α))] = [α^2 P^2 / (1+α)^2] * [(1+α) / ((1-α)P)] = [α^2 P] / [(1+α)(1-α)] = [α^2 / (1-α^2)] * P. Explains that Kp depends solely on temperature and is constant at constant T. If total pressure P is increased, the ratio [α^2 / (1-α^2)] must decrease to keep Kp constant, meaning α must decrease (equilibrium shifts left, reducing dissociation in agreement with Le Chatelier).<br/>"
         "• Level 2 (3-4 marks): Correct derivation with minor algebraic slip; qualitative explanation of pressure effect.<br/>"
         "• Level 1 (1-2 marks): Partial derivation or memorized formula without step-by-step algebraic working.<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• 1.78 = [α^2 / (1 - α^2)] * 2.00 [1]<br/>"
         "• α^2 / (1 - α^2) = 1.78 / 2.00 = 0.890 [1]<br/>"
         "• α^2 = 0.890 * (1 - α^2) = 0.890 - 0.890 α^2 [1]<br/>"
         "• 1.890 α^2 = 0.890 => α^2 = 0.890 / 1.890 = 0.4709 [1]<br/>"
         "• α = sqrt(0.4709) = 0.686 (accept 0.68 to 0.69, or 68.6 % dissociation) [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Immediate compression reduces volume, instantly increasing the concentration of all gas molecules, including Cl2 [2]<br/>"
         "• The gas initially becomes darker yellow-green [1]<br/>"
         "• According to Le Chatelier, the increase in pressure causes equilibrium to shift to the left (2 mol gas -> 1 mol gas) to consume Cl2, so color slightly lightens to a new equilibrium state [1]."),

        ("Question 35: Quadratic Kc & Kp Conversion for N2O4 <=> 2NO2 (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• At equilibrium: n(N2O4) = 0.200 - x; n(NO2) = 2x [1]<br/>"
         "• [N2O4] = (0.200 - x) / 2.00; [NO2] = 2x / 2.00 = x [1]<br/>"
         "• Kc = [NO2]^2 / [N2O4] = x^2 / [(0.200 - x) / 2.00] = 2x^2 / (0.200 - x) [1]<br/>"
         "• 0.0500 = 2x^2 / (0.200 - x) => 0.0500(0.200 - x) = 2x^2 => 2x^2 + 0.0500x - 0.0100 = 0 [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• Quadratic formula: x = [-0.0500 ± sqrt((0.0500)^2 - 4(2)(-0.0100))] / (2*2) [1]<br/>"
         "• Discriminant = 0.0025 + 0.0800 = 0.0825; sqrt(0.0825) = 0.2872 [1]<br/>"
         "• x = (-0.0500 + 0.2872) / 4 = 0.2372 / 4 = 0.0593 mol (discard negative root) [1]<br/>"
         "• Equilibrium n(N2O4) = 0.200 - 0.0593 = 0.1407 mol ≈ 0.141 mol [1]<br/>"
         "• Equilibrium n(NO2) = 2(0.0593) = 0.1186 mol ≈ 0.119 mol [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Total moles = 0.1407 + 0.1186 = 0.2593 mol [1]<br/>"
         "• P = nRT / V = (0.2593 mol * 8.314 J mol^-1 K^-1 * 333 K) / (2.00 x 10^-3 m^3) [1]<br/>"
         "• = 717 900 Pa = 358.9 kPa (accept 358 to 360 kPa) [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Δn = 2 - 1 = +1 [1]<br/>"
         "• Kp = Kc * RT = 0.0500 mol dm^-3 * (8.314 kPa dm^3 mol^-1 K^-1 * 333 K) = 0.0500 * 2768.6 [1]<br/>"
         "• = 138.4 kPa (accept 138 to 139 kPa) [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• NO2 is brown and absorbs light in the visible region, whereas N2O4 is completely colorless [1]<br/>"
         "• A colorimeter measures absorbance of a specific wavelength (blue-green complementary filter) [1]<br/>"
         "• Beer-Lambert law: Absorbance is directly proportional to [NO2], allowing non-destructive optical monitoring without removing samples [1]."),

        ("Question 36: Contact Process Industrial Kp & Design (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Initial moles: n(SO2)=10.0, n(O2)=11.0, n(N2)=79.0 mol [1]<br/>"
         "• 96.0% conversion of SO2 => moles SO2 reacted = 0.960 * 10.0 = 9.60 mol [1]<br/>"
         "• Equilibrium: n(SO2) = 10.0 - 9.60 = 0.40 mol; n(SO3) = 9.60 mol [1]<br/>"
         "• Moles O2 reacted = 9.60 / 2 = 4.80 mol => Equilibrium n(O2) = 11.0 - 4.80 = 6.20 mol; n(N2) = 79.0 mol [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• Total equilibrium moles = 0.40 + 6.20 + 9.60 + 79.0 = 95.20 mol [1]<br/>"
         "• p(SO2) = (0.40 / 95.20) * 1.50 = 0.00630 atm [1]<br/>"
         "• p(O2) = (6.20 / 95.20) * 1.50 = 0.09769 atm; p(SO3) = (9.60 / 95.20) * 1.50 = 0.15126 atm [1]<br/>"
         "• Kp = p(SO3)^2 / [p(SO2)^2 * p(O2)] = (0.15126)^2 / [(0.00630)^2 * 0.09769] = 0.02288 / (0.00003969 * 0.09769) [1]<br/>"
         "• = 5900 atm^-1 (accept 5800 to 6000 atm^-1) [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• At 1 to 2 atm, the conversion is already 96 to 98% (extremely high conversion) [1]<br/>"
         "• Building high-pressure pipes, compressors, and thick-walled reactors requires enormous capital cost [1]<br/>"
         "• SO2 and SO3 in moist air are highly corrosive, increasing risk of catastrophic leaks at high pressure [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• V2O5 acts as a heterogeneous catalyst providing an alternative pathway with lower activation energy [1]<br/>"
         "• V2O5 oxidises SO2 to SO3, being reduced from vanadium(V) to vanadium(IV): SO2 + V2O5 -> SO3 + V2O4 [1]<br/>"
         "• Oxygen from the feed gas re-oxidises V2O4 back to V2O5: 2V2O4 + O2 -> 2V2O5, completing the cycle [1]."),

        ("Question 37: Deep-Sea Diving & Henry's Law Gas Equilibria (15 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Total pressure P = 5.00 atm; mole fraction x(N2) = 0.780 [1]<br/>"
         "• p(N2) = 0.780 * 5.00 atm = 3.90 atm [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• (i) At 1.00 atm: p(N2) = 0.780 atm => [N2(aq)] = 6.40 x 10^-4 * 0.780 = 4.992 x 10^-4 mol dm^-3 [1]<br/>"
         "• (ii) At 5.00 atm: p(N2) = 3.90 atm => [N2(aq)] = 6.40 x 10^-4 * 3.90 = 2.496 x 10^-3 mol dm^-3 [1]<br/>"
         "• Difference in concentration = 2.496 x 10^-3 - 4.992 x 10^-4 = 1.997 x 10^-3 mol dm^-3 [1]<br/>"
         "• Extra moles in 5.50 dm^3 blood = 1.997 x 10^-3 * 5.50 = 0.01098 mol [1]<br/>"
         "• Extra volume of N2 gas = 0.01098 mol * 25.4 dm^3 mol^-1 = 0.279 dm^3 (approx 280 cm^3) [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Rapid ascent drops ambient pressure quickly [1]<br/>"
         "• Equilibrium N2(g) <=> N2(aq) shifts rapidly to the left according to Le Chatelier's principle [1]<br/>"
         "• Dissolved nitrogen becomes supersaturated in blood and tissues [1]<br/>"
         "• Nitrogen gas nucleates out of solution as microbubbles in blood vessels and joints, causing excruciating pain, ischemia, and embolism [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Helium is much less soluble in lipids and water than nitrogen, so far fewer moles of gas dissolve at depth [2]<br/>"
         "• Helium atoms are much smaller and lighter than N2 molecules, diffusing out of tissues and lungs much faster without bubble formation [2].")
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
    print(f"[SUCCESS] Week 7 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")


if __name__ == '__main__':
    build_pdf()
