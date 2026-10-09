"""
build_usman_week6_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 6 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 12B.2: Experimental and Theoretical Lattice Energies (Fajans' Rules, Polarisability, Covalent Character)
  - 12B.3: Enthalpy Changes of Solution and Hydration (Energy Cycles, Group 2 Solubility Trends)

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
    "Usman_Edexcel_Chem_U4_Week6_150M_Challenging_Quiz.pdf"
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


class SolutionCycleBox(Flowable):
    """Draws a dedicated Hess solution enthalpy cycle box."""
    def __init__(self, width=AVAIL_W, height=7.2*cm, title="Enthalpy Cycle"):
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

        self.canv.setFont(FONT['Bold'], 8)
        self.canv.setFillColor(NAVY)
        self.canv.drawString(10, self.height - 14, self.title)

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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 6 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 6 (150 Marks)...")
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
                   "<b>[  0  ][  0  ][  6  ][  6  ]</b>", S['edx_meta']),
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W06</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 6 ASSESSMENT: TOPIC 12B.2 & 12B.3 ENERGETICS & SOLUTIONS</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 6 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 12B.2: Experimental vs Theoretical Lattice Energies (Fajans' Rules & Covalency)<br/>Topic 12B.3: Enthalpies of Solution & Hydration (Energy Cycles & Group 2 Solubility)", S['edx_meta'])],
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
        ("Which of the following assumptions is made in the purely theoretical ionic model of lattice energy?",
         [("A", "Ions are polarisable soft spheres with overlapping electron clouds"),
          ("B", "Ions are point charges that are perfectly spherical with purely electrostatic attraction"),
          ("C", "Ions share pairs of electrons through coordinate covalent bonds"),
          ("D", "Ions undergo zero-point quantum mechanical fluctuations at 0 K")]),

        ("The experimental lattice energy of silver iodide, AgI, is -887 kJ mol^-1, whereas its theoretical value calculated using the purely ionic model is -778 kJ mol^-1. What is the reason for this large discrepancy?",
         [("A", "The ionic radius of silver is smaller than predicted by X-ray crystallography"),
          ("B", "Significant polarisation of the large iodide anion electron cloud by the silver cation introduces covalent character"),
          ("C", "Experimental measurement of the Born-Haber cycle for silver halides is inherently inaccurate"),
          ("D", "Silver iodide forms a face-centred cubic lattice with high coordination number")]),

        ("According to Fajans' rules, which combination of cation and anion properties results in the GREATEST covalent character in an ionic solid?",
         [("A", "Large cation with low charge; small anion with low charge"),
          ("B", "Small cation with high charge; small anion with high charge"),
          ("C", "Small cation with high charge; large anion with high charge"),
          ("D", "Large cation with high charge; large anion with low charge")]),

        # Page 3: Q4, Q5, Q6
        ("Which chemical equation defines the standard enthalpy change of hydration of the chloride ion, ΔhydH°[Cl-]?",
         [("A", "Cl2(g) + aq —> 2Cl-(aq)"),
          ("B", "Cl-(g) + aq —> Cl-(aq)"),
          ("C", "Cl-(s) + aq —> Cl-(aq)"),
          ("D", "HCl(g) + aq —> H+(aq) + Cl-(aq)")]),

        ("Which relationship correctly connects standard enthalpy of solution (ΔsolH°), standard lattice energy of formation (ΔH_LE°), and standard enthalpies of hydration (ΔhydH°)?",
         [("A", "ΔsolH° = ΣΔhydH° + ΔH_LE°"),
          ("B", "ΔsolH° = ΣΔhydH° - ΔH_LE°"),
          ("C", "ΔsolH° = ΔH_LE° - ΣΔhydH°"),
          ("D", "ΔsolH° = ΣΔhydH° + TΔS_system")]),

        ("Why does the standard enthalpy of hydration become LESS exothermic from fluoride (F-) to iodide (I-)?",
         [("A", "The ionic radius increases down the group, so charge density decreases and ion-dipole attractions weaken"),
          ("B", "Iodide ions form stronger hydrogen bonds with water molecules than fluoride ions"),
          ("C", "The electronegativity of halogens increases down the group"),
          ("D", "Fluoride ions carry a higher negative charge than iodide ions")]),

        # Page 4: Q7, Q8, Q9
        ("Given: ΔH_LE°[NaCl(s)] = -787 kJ mol^-1, ΔhydH°[Na+] = -406 kJ mol^-1, ΔhydH°[Cl-] = -378 kJ mol^-1. What is the standard enthalpy of solution, ΔsolH°, of sodium chloride?",
         [("A", "+3 kJ mol^-1"),
          ("B", "-3 kJ mol^-1"),
          ("C", "+1571 kJ mol^-1"),
          ("D", "-1571 kJ mol^-1")]),

        ("Why is the dissolution of sodium chloride in water spontaneous at 298 K, even though the enthalpy of solution is slightly endothermic (+3 kJ mol^-1)?",
         [("A", "Water molecules break down into H+ and OH- ions upon dissolution"),
          ("B", "The breakdown of the rigid 3D ionic lattice causes a large positive entropy change of the system (ΔS_system > 0)"),
          ("C", "The hydration enthalpy of sodium ions releases enormous heat"),
          ("D", "The entropy of the surroundings becomes strongly positive")]),

        ("Which of the following Group 2 sulfates is the LEAST soluble in water at 298 K?",
         [("A", "MgSO4"),
          ("B", "CaSO4"),
          ("C", "SrSO4"),
          ("D", "BaSO4")]),

        # Page 5: Q10, Q11, Q12
        ("Which of the following Group 2 hydroxides is the MOST soluble in water at 298 K?",
         [("A", "Mg(OH)2"),
          ("B", "Ca(OH)2"),
          ("C", "Sr(OH)2"),
          ("D", "Ba(OH)2")]),

        ("Why does the solubility of Group 2 sulfates DECREASE down the group from MgSO4 to BaSO4?",
         [("A", "The lattice energy increases dramatically down the group"),
          ("B", "The sulfate ion is large, so lattice energy changes very little, while hydration enthalpy of the cation becomes significantly less exothermic"),
          ("C", "Barium ions have higher charge density than magnesium ions"),
          ("D", "Barium sulfate forms an acidic solution with water")]),

        ("Why does the solubility of Group 2 hydroxides INCREASE down the group from Mg(OH)2 to Ba(OH)2?",
         [("A", "The hydroxide ion is small, so lattice energy decreases more rapidly down the group than cation hydration enthalpy"),
          ("B", "Barium hydroxide is a covalent molecular solid"),
          ("C", "The hydration enthalpy of Ba2+ is more exothermic than that of Mg2+"),
          ("D", "Magnesium hydroxide completely hydrolyses into magnesium oxide and water")]),

        # Page 6: Q13, Q14, Q15
        ("For which halide is the difference between experimental and theoretical lattice energy the SMALLEST?",
         [("A", "LiI"),
          ("B", "NaCl"),
          ("C", "AgCl"),
          ("D", "AgI")]),

        ("Given standard hydration enthalpies: ΔhydH°[Mg2+] = -1926 kJ mol^-1, ΔhydH°[Cl-] = -378 kJ mol^-1, and ΔsolH°[MgCl2(s)] = -155 kJ mol^-1. What is the standard lattice energy of formation of MgCl2(s)?",
         [("A", "-2527 kJ mol^-1"),
          ("B", "+2527 kJ mol^-1"),
          ("C", "-2149 kJ mol^-1"),
          ("D", "-2837 kJ mol^-1")]),

        ("Which factor best explains why silver fluoride, AgF, is highly soluble in water, whereas silver chloride, AgCl, is virtually insoluble?",
         [("A", "AgF is a covalent network solid"),
          ("B", "The very high hydration enthalpy of the small fluoride ion makes ΔsolH° of AgF exothermic"),
          ("C", "Silver chloride has a much smaller lattice energy than silver fluoride"),
          ("D", "Silver fluoride does not contain silver ions in aqueous solution")]),

        # Page 7: Q16, Q17, Q18
        ("How does the polarizing power of Group 2 cations change down the group from Be2+ to Ba2+?",
         [("A", "Increases, because nuclear charge increases"),
          ("B", "Decreases, because ionic radius increases while ionic charge remains constant at 2+"),
          ("C", "Remains constant, because all Group 2 cations possess an outer s-orbital"),
          ("D", "Decreases, because electron shielding decreases down the group")]),

        ("Which pair of experimental vs theoretical lattice energies would show the GREATEST percentage discrepancy?",
         [("A", "KCl: Experimental = -711 kJ mol^-1, Theoretical = -701 kJ mol^-1"),
          ("B", "KBr: Experimental = -679 kJ mol^-1, Theoretical = -667 kJ mol^-1"),
          ("C", "AgCl: Experimental = -905 kJ mol^-1, Theoretical = -833 kJ mol^-1"),
          ("D", "AgI: Experimental = -887 kJ mol^-1, Theoretical = -778 kJ mol^-1")]),

        ("When calcium chloride, CaCl2, dissolves in water, the temperature of the solution increases. What can be deduced about the energetics of dissolution?",
         [("A", "Lattice energy of formation is more exothermic than the sum of hydration enthalpies"),
          ("B", "Sum of hydration enthalpies is more exothermic than the lattice energy of formation is endothermic"),
          ("C", "ΔsolH° is positive"),
          ("D", "ΔS_surroundings is negative")]),

        # Page 8: Q19, Q20, Q21
        ("Why does the standard entropy of hydration of the Fe3+ ion (-393 J K^-1 mol^-1) have a much more negative value than that of the Fe2+ ion (-271 J K^-1 mol^-1)?",
         [("A", "Fe3+ has a higher charge and smaller radius, attracting and ordering solvent water molecules into a more rigid hydration shell"),
          ("B", "Fe3+ is a stronger reducing agent than Fe2+"),
          ("C", "Fe2+ forms covalent bonds with solvent water molecules"),
          ("D", "Fe3+ has more unpaired electrons in its 3d subshell")]),

        ("Which compound would be predicted to have the lowest thermal decomposition temperature for its carbonate?",
         [("A", "BaCO3"),
          ("B", "SrCO3"),
          ("C", "CaCO3"),
          ("D", "MgCO3")]),

        ("The dissolution of ammonium chloride in water is endothermic (ΔsolH° = +14.8 kJ mol^-1). What is the sign of ΔS_surroundings at 298 K?",
         [("A", "Positive (+)"),
          ("B", "Negative (-)"),
          ("C", "Zero"),
          ("D", "Cannot be determined without knowing the volume of water")]),

        # Page 9: Q22, Q23, Q24
        ("Which cation has the highest charge density?",
         [("A", "Li+ (radius = 0.076 nm)"),
          ("B", "Na+ (radius = 0.102 nm)"),
          ("C", "Mg2+ (radius = 0.072 nm)"),
          ("D", "Al3+ (radius = 0.054 nm)")]),

        ("What happens to the theoretical lattice energy of ionic compounds as the sum of the ionic radii (r+ + r-) increases?",
         [("A", "Becomes more exothermic (larger magnitude)"),
          ("B", "Becomes less exothermic (smaller magnitude)"),
          ("C", "Remains unchanged because charges remain constant"),
          ("D", "Fluctuates depending on the electronegativity difference")]),

        ("Why does aluminium chloride, AlCl3, sublimate at 180 °C as a covalent dimer, Al2Cl6, rather than forming a high-melting ionic lattice?",
         [("A", "Al3+ has an extremely high charge density which severely polarises chloride anions, causing bonds to become largely covalent"),
          ("B", "Chlorine atoms lack d-orbitals to accept electrons from aluminium"),
          ("C", "Aluminium has a lower ionization energy than sodium"),
          ("D", "Aluminium chloride cannot form crystal lattices due to steric hindrance")]),

        # Page 10: Q25, Q26, Q27
        ("In an experiment to measure the enthalpy of solution of potassium chloride, KCl, 3.73 g of KCl was dissolved in 50.0 cm^3 of water. The temperature fell by 4.2 °C. What is the calculated value of ΔsolH°? (Molar mass of KCl = 74.6 g mol^-1, c = 4.18 J g^-1 K^-1)",
         [("A", "+17.6 kJ mol^-1"),
          ("B", "-17.6 kJ mol^-1"),
          ("C", "+0.878 kJ mol^-1"),
          ("D", "+35.1 kJ mol^-1")]),

        ("Which statement regarding the enthalpy of hydration of ions is always TRUE?",
         [("A", "Enthalpy of hydration is always endothermic because bonds between water molecules are broken"),
          ("B", "Enthalpy of hydration is always exothermic because ion-dipole electrostatic attractions are formed"),
          ("C", "Enthalpy of hydration is zero for neutral species in water"),
          ("D", "Enthalpy of hydration is independent of ionic charge")]),

        ("Why is the lattice energy of sodium iodide (-700 kJ mol^-1) less exothermic than that of sodium fluoride (-918 kJ mol^-1)?",
         [("A", "The iodide ion has a smaller radius than the fluoride ion"),
          ("B", "The iodide ion has a larger radius than the fluoride ion, increasing inter-ionic separation"),
          ("C", "Sodium fluoride contains covalent double bonds"),
          ("D", "Iodine is a solid whereas fluorine is a gas under standard conditions")]),

        # Page 11: Q28, Q29, Q30
        ("Which of the following salts produces an alkaline solution when dissolved in water?",
         [("A", "NaCl"),
          ("B", "NH4Cl"),
          ("C", "CH3COONa"),
          ("D", "AlCl3")]),

        ("The enthalpy of solution of anhydrous copper(II) sulfate is -66.5 kJ mol^-1, whereas that of hydrated copper(II) sulfate, CuSO4·5H2O, is +11.5 kJ mol^-1. By applying Hess's Law, what is the enthalpy of hydration of anhydrous CuSO4(s) to CuSO4·5H2O(s)?",
         [("A", "-78.0 kJ mol^-1"),
          ("B", "+78.0 kJ mol^-1"),
          ("C", "-55.0 kJ mol^-1"),
          ("D", "+55.0 kJ mol^-1")]),

        ("When calcium sulfate dissolves in water, the entropy change of the system is -140 J K^-1 mol^-1. Why is ΔS_system negative?",
         [("A", "Dissolving an ionic solid always decreases system entropy"),
          ("B", "Water molecules become highly ordered in hydration shells around Ca2+ and SO4^2- ions, outweighing lattice breakdown entropy"),
          ("C", "Calcium sulfate precipitates rapidly as an insoluble hydrate"),
          ("D", "The solution expands significantly, reducing particle collisions")])
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
    # QUESTION 31 (18 MARKS) — THEORETICAL VS EXPERIMENTAL LATTICE ENERGIES & FAJANS' RULES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Lattice energies can be determined experimentally using Born-Haber cycles or calculated theoretically using electrostatics (the Kapustinskii equation) based on a purely ionic model.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The experimental and theoretical lattice energies of formation for several metal halides are given below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t31_data = [
        [Paragraph("<b>Halide</b>", S['tbl_th']), Paragraph("<b>Experimental Lattice Energy / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>Theoretical Lattice Energy / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>Difference / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>% Difference</b>", S['tbl_th'])],
        [Paragraph("NaCl", S['tbl_td_l']), Paragraph("-787", S['tbl_td']), Paragraph("-769", S['tbl_td']), Paragraph("18", S['tbl_td']), Paragraph("2.3 %", S['tbl_td'])],
        [Paragraph("AgCl", S['tbl_td_l']), Paragraph("-905", S['tbl_td']), Paragraph("-833", S['tbl_td']), Paragraph("72", S['tbl_td']), Paragraph("8.6 %", S['tbl_td'])],
        [Paragraph("AgI", S['tbl_td_l']), Paragraph("-887", S['tbl_td']), Paragraph("-778", S['tbl_td']), Paragraph("109", S['tbl_td']), Paragraph("14.0 %", S['tbl_td'])],
    ]
    t31 = Table(t31_data, colWidths=[3.2*cm, 4.4*cm, 4.4*cm, 2.8*cm, 2.6*cm])
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t31)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> State the two key assumptions of the purely ionic model used to calculate theoretical lattice energies.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Explain why the experimental lattice energy of sodium chloride is in very close agreement with its theoretical value (only 2.3 % difference).", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (c)
    story.append(Table([
        [Paragraph("<b>(c)</b> The experimental lattice energy of silver chloride is 72 kJ mol<sup>-1</sup> more exothermic than its theoretical value.<br/>"
                   "Using Fajans' rules, explain why silver chloride exhibits significant covalent character.<br/>"
                   "In your answer, refer to the polarizing power of the Ag<sup>+</sup> cation and its electronic configuration (4d<sup>10</sup> vs 2p<sup>6</sup> for Na<sup>+</sup>).", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(PageBreak())

    # Question 31 Parts (d), (e)
    story.append(Table([
        [Paragraph("<b>(d)</b> Explain why the discrepancy between experimental and theoretical lattice energies is significantly larger for silver iodide (14.0 %) than for silver chloride (8.6 %).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Silver fluoride, AgF, has an experimental lattice energy of -958 kJ mol<sup>-1</sup> and a theoretical lattice energy of -946 kJ mol<sup>-1</sup> (only 1.3 % difference).<br/>"
                   "State how this comparison across the silver halides supports the concept of anion polarisability, and predict how the water solubility of AgF compares to that of AgI.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — ENTHALPY OF SOLUTION & HYDRATION ENERGY CYCLES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;When potassium fluoride, KF, dissolves in water, heat is released, whereas dissolving potassium chloride, KCl, absorbs heat.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("The enthalpy changes of hydration and lattice energies of formation at 298 K are shown below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t32_data = [
        [Paragraph("<b>Ion / Compound</b>", S['tbl_th']), Paragraph("<b>Δ<i>H</i><sub>hyd</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>Δ<i>H</i><sub>LE</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("K<sup>+</sup>(g)", S['tbl_td_l']), Paragraph("-322", S['tbl_td']), Paragraph("—", S['tbl_td'])],
        [Paragraph("F<sup>-</sup>(g)", S['tbl_td_l']), Paragraph("-506", S['tbl_td']), Paragraph("—", S['tbl_td'])],
        [Paragraph("Cl<sup>-</sup>(g)", S['tbl_td_l']), Paragraph("-378", S['tbl_td']), Paragraph("—", S['tbl_td'])],
        [Paragraph("KF(s)", S['tbl_td_l']), Paragraph("—", S['tbl_td']), Paragraph("-817", S['tbl_td'])],
        [Paragraph("KCl(s)", S['tbl_td_l']), Paragraph("—", S['tbl_td']), Paragraph("-711", S['tbl_td'])],
    ]
    t32 = Table(t32_data, colWidths=[5.5*cm, 5.5*cm, 4.8*cm])
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
        [Paragraph("<b>(a)</b> In the box below, construct a complete Hess's Law energy cycle linking lattice energy, enthalpies of hydration, and the enthalpy of solution for potassium fluoride, KF(s). Include chemical species with state symbols and label all enthalpy arrows.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(SolutionCycleBox(AVAIL_W, 6.8*cm, title="Hess's Law Solution Enthalpy Cycle for KF"))
    story.append(Spacer(1, 0.3 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Calculate the standard enthalpy of solution, Δ<i>H</i><sub>sol</sub>°, in kJ mol<sup>-1</sup>:<br/>"
                   "(i) for potassium fluoride, KF(s)<br/>"
                   "(ii) for potassium chloride, KCl(s).<br/>"
                   "Include signs in both answers.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>sol</sub>°[KF(s)] = ................................... kJ mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>sol</sub>°[KCl(s)] = ................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 32 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Explain why the enthalpy of hydration of the fluoride ion (-506 kJ mol<sup>-1</sup>) is significantly more exothermic than that of the chloride ion (-378 kJ mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> For the dissolution of KCl(s), Δ<i>S</i>°<sub>system</sub> = +75.3 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>"
                   "Calculate Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub> for the dissolution of KCl(s) at 298 K.<br/>"
                   "Deduce whether potassium chloride is soluble in water at room temperature.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub> = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> When water is added to solid anhydrous potassium fluoride in a test tube, the tube becomes hot to the touch.<br/>"
                   "Explain why dissolving KF(s) is exothermic, referring to the balance between lattice energy and hydration enthalpies.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — GROUP 2 SULFATE SOLUBILITY TRENDS: MgSO4 vs BaSO4
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Magnesium sulfate, MgSO<sub>4</sub> (Epsom salts), is readily soluble in water (approx 350 g dm<sup>-3</sup> at 20 °C), whereas barium sulfate, BaSO<sub>4</sub>, is practically insoluble (approx 0.002 g dm<sup>-3</sup>).", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Thermodynamic data at 298 K are tabulated below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t33_data = [
        [Paragraph("<b>Compound / Ion</b>", S['tbl_th']), Paragraph("<b>Δ<i>H</i><sub>LE</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_th']), Paragraph("<b>Δ<i>H</i><sub>hyd</sub>° / kJ mol<sup>-1</sup></b>", S['tbl_th'])],
        [Paragraph("MgSO<sub>4</sub>(s)", S['tbl_td_l']), Paragraph("-2884", S['tbl_td']), Paragraph("—", S['tbl_td'])],
        [Paragraph("BaSO<sub>4</sub>(s)", S['tbl_td_l']), Paragraph("-2469", S['tbl_td']), Paragraph("—", S['tbl_td'])],
        [Paragraph("Mg<sup>2+</sup>(g)", S['tbl_td_l']), Paragraph("—", S['tbl_td']), Paragraph("-1926", S['tbl_td'])],
        [Paragraph("Ba<sup>2+</sup>(g)", S['tbl_td_l']), Paragraph("—", S['tbl_td']), Paragraph("-1305", S['tbl_td'])],
        [Paragraph("SO<sub>4</sub><sup>2-</sup>(g)", S['tbl_td_l']), Paragraph("—", S['tbl_td']), Paragraph("-1045", S['tbl_td'])],
    ]
    t33 = Table(t33_data, colWidths=[5.5*cm, 5.5*cm, 4.8*cm])
    t33.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), STEEL),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t33)
    story.append(Spacer(1, 0.3 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Calculate the standard enthalpy of solution, Δ<i>H</i><sub>sol</sub>°, in kJ mol<sup>-1</sup>:<br/>"
                   "(i) for magnesium sulfate, MgSO<sub>4</sub>(s)<br/>"
                   "(ii) for barium sulfate, BaSO<sub>4</sub>(s).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>sol</sub>°[MgSO<sub>4</sub>(s)] = ................................... kJ mol<sup>-1</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>sol</sub>°[BaSO<sub>4</sub>(s)] = ................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The lattice energy of BaSO<sub>4</sub> is only 415 kJ mol<sup>-1</sup> less exothermic than that of MgSO<sub>4</sub>.<br/>"
                   "In contrast, the hydration enthalpy of Ba<sup>2+</sup> is 621 kJ mol<sup>-1</sup> less exothermic than that of Mg<sup>2+</sup>.<br/>"
                   "Explain why the lattice energy decreases much less down the group than the cation hydration enthalpy, referring to the relative sizes of Mg<sup>2+</sup>, Ba<sup>2+</sup>, and SO<sub>4</sub><sup>2-</sup>.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(10, AVAIL_W))
    story.append(PageBreak())

    # Question 33 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> For the dissolution of BaSO<sub>4</sub>(s), Δ<i>S</i>°<sub>system</sub> = -12.0 J K<sup>-1</sup> mol<sup>-1</sup>.<br/>"
                   "Using your value of Δ<i>H</i><sub>sol</sub>° from (a), calculate Δ<i>S</i><sub>total</sub> for the dissolution of barium sulfate at 298 K.<br/>"
                   "Explain how your calculated value accounts for the extreme insolubility of BaSO<sub>4</sub>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>S</i><sub>total</sub>[BaSO<sub>4</sub>] = ..................................................................................... J K<sup>-1</sup> mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> For the dissolution of MgSO<sub>4</sub>(s), Δ<i>S</i>°<sub>system</sub> is also negative (-108.0 J K<sup>-1</sup> mol<sup>-1</sup>).<br/>"
                   "Explain why MgSO<sub>4</sub> dissolves readily despite having a significantly negative Δ<i>S</i>°<sub>system</sub>, referring to Δ<i>S</i><sub>surroundings</sub> and Δ<i>S</i><sub>total</sub>.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> State the expected observation when a few drops of aqueous barium chloride, BaCl<sub>2</sub>(aq), are added to an aqueous solution containing sulfate ions, and write the ionic equation for the reaction.", S['q_subpart']),
         Paragraph("<b>(2)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — ASTERISKED (*) LEVEL OF RESPONSE: CONTRASTING GROUP 2 SOLUBILITY TRENDS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*34</b>&nbsp;&nbsp;The solubility of Group 2 compounds exhibits contrasting trends down the group:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("• <b>Hydroxides:</b> Mg(OH)<sub>2</sub> is sparingly soluble (suspension in water is milk of magnesia), while Ba(OH)<sub>2</sub> is moderately soluble.<br/>"
                           "• <b>Sulfates:</b> MgSO<sub>4</sub> is highly soluble, while BaSO<sub>4</sub> is virtually insoluble.", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Ionic radii are given in the table below:", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    t34_data = [
        [Paragraph("<b>Ion</b>", S['tbl_th']), Paragraph("<b>Mg<sup>2+</sup></b>", S['tbl_th']), Paragraph("<b>Ba<sup>2+</sup></b>", S['tbl_th']), Paragraph("<b>OH<sup>-</sup></b>", S['tbl_th']), Paragraph("<b>SO<sub>4</sub><sup>2-</sup></b>", S['tbl_th'])],
        [Paragraph("<b>Ionic Radius / nm</b>", S['tbl_th']), Paragraph("0.072", S['tbl_td']), Paragraph("0.135", S['tbl_td']), Paragraph("0.140", S['tbl_td']), Paragraph("0.230", S['tbl_td'])],
    ]
    t34 = Table(t34_data, colWidths=[3.8*cm] + [3.0*cm]*4)
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
        [Paragraph("<b>(a)</b> State how the enthalpy of hydration of Group 2 cations changes from Mg<sup>2+</sup> to Ba<sup>2+</sup>, and explain this trend in terms of ionic properties.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)* Level of Response
    story.append(Table([
        [Paragraph("<b>*(b)</b> Explain why the solubility of Group 2 hydroxides INCREASES down the group, whereas the solubility of Group 2 sulfates DECREASES down the group.<br/>"
                   "In your answer, you should include:<br/>"
                   "• a discussion of the relationship between Δ<i>H</i><sub>sol</sub>°, lattice energy, and hydration enthalpies<br/>"
                   "• the effect of anion size (OH<sup>-</sup> is relatively small, while SO<sub>4</sub><sup>2-</sup> is very large) on how lattice energy changes down Group 2<br/>"
                   "• how the competing changes in lattice energy and cation hydration enthalpy dictate whether Δ<i>H</i><sub>sol</sub>° becomes more exothermic or more endothermic down each series<br/>"
                   "• the role of entropy (Δ<i>S</i><sub>total</sub>) in governing the overall solubility.", S['q_subpart']),
         Paragraph("<b>(6)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(13, AVAIL_W))
    story.append(PageBreak())

    # Question 34 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Magnesium hydroxide is safely ingested as an antacid (milk of magnesia) to neutralise excess stomach acid (HCl), whereas barium hydroxide is caustic and toxic.<br/>"
                   "(i) Write an equation for the neutralisation reaction between Mg(OH)<sub>2</sub> and HCl.<br/>"
                   "(ii) Explain why the low solubility of Mg(OH)<sub>2</sub> makes it safe to ingest, while Ba(OH)<sub>2</sub> is dangerous.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Predict the solubility trend of Group 2 carbonates (MgCO<sub>3</sub> to BaCO<sub>3</sub>) down the group. Justify your prediction by comparing the size of the carbonate ion, CO<sub>3</sub><sup>2-</sup> (radius = 0.185 nm), with the sulfate and hydroxide ions.", S['q_subpart']),
         Paragraph("<b>(5)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(9, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — CALORIMETRIC DETERMINATION OF HYDRATION ENTHALPY OF MgSO4
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>35</b>&nbsp;&nbsp;A student carried out two separate calorimetry experiments to determine the enthalpy of hydration of anhydrous magnesium sulfate to magnesium sulfate heptahydrate:", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("MgSO<sub>4</sub>(s) &nbsp;+&nbsp; 7H<sub>2</sub>O(l) &nbsp;—&gt;&nbsp; MgSO<sub>4</sub>·7H<sub>2</sub>O(s) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Δ<i>H</i><sub>hydr_salt</sub>°", S['q_equation']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("<b>Experiment 1:</b> A sample of 0.0500 mol (6.02 g) of anhydrous MgSO<sub>4</sub>(s) was dissolved in 50.0 cm<sup>3</sup> of deionised water in an insulated polystyrene cup. The temperature rose from 20.2 °C to 29.8 °C.<br/>"
                           "<b>Experiment 2:</b> A sample of 0.0500 mol (12.33 g) of hydrated MgSO<sub>4</sub>·7H<sub>2</sub>O(s) was dissolved in 50.0 cm<sup>3</sup> of deionised water in an identical polystyrene cup. The temperature fell from 20.4 °C to 18.2 °C.<br/>"
                           "(Assume the specific heat capacity of all solutions is 4.18 J g<sup>-1</sup> K<sup>-1</sup> and density is 1.00 g cm<sup>-3</sup>).", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> For Experiment 1, calculate:<br/>"
                   "(i) the heat energy released, <i>q</i><sub>1</sub>, in Joules<br/>"
                   "(ii) the standard enthalpy of solution, Δ<i>H</i><sub>1</sub>, of anhydrous MgSO<sub>4</sub>(s) in kJ mol<sup>-1</sup>. Include a sign.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>1</sub> = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> For Experiment 2, calculate:<br/>"
                   "(i) the heat energy absorbed, <i>q</i><sub>2</sub>, in Joules<br/>"
                   "(ii) the standard enthalpy of solution, Δ<i>H</i><sub>2</sub>, of hydrated MgSO<sub>4</sub>·7H<sub>2</sub>O(s) in kJ mol<sup>-1</sup>. Include a sign.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>2</sub> = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 35 Parts (c), (d), (e)
    story.append(Table([
        [Paragraph("<b>(c)</b> Construct a Hess's Law cycle linking Δ<i>H</i><sub>1</sub>, Δ<i>H</i><sub>2</sub>, and Δ<i>H</i><sub>hydr_salt</sub>°.<br/>"
                   "Using your values from (a) and (b), calculate Δ<i>H</i><sub>hydr_salt</sub>° for the hydration of anhydrous magnesium sulfate in kJ mol<sup>-1</sup>.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Δ<i>H</i><sub>hydr_salt</sub>° = ..................................................................................... kJ mol<sup>-1</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Explain why the direct enthalpy of hydration (adding liquid water directly to anhydrous MgSO<sub>4</sub> to form solid hydrated crystals) cannot be measured accurately in a school laboratory.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(e)</b> Identify two experimental sources of error in Experiment 1 and suggest one practical modification that would improve the accuracy of the temperature measurement.", S['q_subpart']),
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
    # QUESTION 36 (15 MARKS) — MEDICAL DIAGNOSTICS & BARIUM MEAL THERMODYNAMICS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;Barium sulfate, BaSO<sub>4</sub>, is administered orally to patients as a dense radiopaque suspension (a 'barium meal') to visualise the digestive tract under X-ray radiography.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Free aqueous barium ions, Ba<sup>2+</sup>(aq), are potent systemic poisons that cause cardiac arrhythmia and muscular paralysis. The solubility product, <i>K</i><sub>sp</sub>, of BaSO<sub>4</sub> at 298 K is 1.08 × 10<sup>-10</sup> mol<sup>2</sup> dm<sup>-6</sup>.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Write the expression for the solubility product, <i>K</i><sub>sp</sub>, of barium sulfate and calculate the concentration of Ba<sup>2+</sup>(aq) ions in a saturated aqueous solution in mol dm<sup>-3</sup> and in g dm<sup>-3</sup>. (Molar mass of Ba = 137.3 g mol<sup>-1</sup>).", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("[Ba<sup>2+</sup>(aq)] = ................................... mol dm<sup>-3</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = ................................... g dm<sup>-3</sup>", S['ans_prompt']))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> The lethal dose of soluble barium salts in humans is approximately 1.0 g of Ba<sup>2+</sup>.<br/>"
                   "Using your answer to (a), calculate the volume of saturated barium sulfate solution, in dm<sup>3</sup>, a patient would have to ingest to reach this lethal dose.<br/>"
                   "Comment on what this shows about the safety of barium meals.", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("Volume = ..................................................................................... dm<sup>3</sup>", S['ans_prompt']))
    story.append(PageBreak())

    # Question 36 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> A patient accidentally swallows barium carbonate, BaCO<sub>3</sub>, instead of barium sulfate.<br/>"
                   "Unlike BaSO<sub>4</sub>, barium carbonate causes fatal poisoning in the stomach.<br/>"
                   "Explain why barium carbonate dissolves readily in stomach acid (approx 0.10 mol dm<sup>-3</sup> HCl), whereas barium sulfate does not.<br/>"
                   "Include ionic equations in your explanation.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> If a patient suffers from barium salt poisoning, doctors administer an aqueous solution of sodium sulfate, Na<sub>2</sub>SO<sub>4</sub>(aq), as an immediate emergency antidote.<br/>"
                   "Explain the chemical basis of this treatment, referring to Le Chatelier's principle and the common ion effect on solubility.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.2 * cm))
    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — THERMAL DECOMPOSITION OF GROUP 1 & 2 NITRATES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;The thermal decomposition of metal nitrates depends markedly on the charge and size of the metal cation.", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("• When anhydrous potassium nitrate, KNO<sub>3</sub>, is heated, it decomposes without forming brown fumes:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp; 2KNO<sub>3</sub>(s) &nbsp;—&gt;&nbsp; 2KNO<sub>2</sub>(s) &nbsp;+&nbsp; O<sub>2</sub>(g)<br/>"
                           "• When anhydrous lithium nitrate, LiNO<sub>3</sub>, or magnesium nitrate, Mg(NO<sub>3</sub>)<sub>2</sub>, is heated, pungent brown fumes of NO<sub>2</sub> gas are evolved:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp; 4LiNO<sub>3</sub>(s) &nbsp;—&gt;&nbsp; 2Li<sub>2</sub>O(s) &nbsp;+&nbsp; 4NO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g)<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp; 2Mg(NO<sub>3</sub>)<sub>2</sub>(s) &nbsp;—&gt;&nbsp; 2MgO(s) &nbsp;+&nbsp; 4NO<sub>2</sub>(g) &nbsp;+&nbsp; O<sub>2</sub>(g)", S['q_stem']))
    story.append(Spacer(1, 0.25 * cm))

    # Part (a)
    story.append(Table([
        [Paragraph("<b>(a)</b> Explain why lithium nitrate decomposes in an anomalous manner compared to the other Group 1 nitrates (such as NaNO<sub>3</sub> and KNO<sub>3</sub>), decomposing like a Group 2 nitrate.<br/>"
                   "Refer to the diagonal relationship between lithium and magnesium and the polarizing power of the Li<sup>+</sup> ion.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    # Part (b)
    story.append(Table([
        [Paragraph("<b>(b)</b> Explain the mechanism of thermal decomposition of the nitrate ion, NO<sub>3</sub><sup>-</sup>:<br/>"
                   "• how a small, highly charged cation polarises the nitrate electron cloud<br/>"
                   "• which covalent bond within the nitrate ion is weakened<br/>"
                   "• why greater polarisation leads to decomposition into the metal oxide rather than the metal nitrite.", S['q_subpart']),
         Paragraph("<b>(4)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(8, AVAIL_W))
    story.append(PageBreak())

    # Question 37 Parts (c), (d)
    story.append(Table([
        [Paragraph("<b>(c)</b> Describe how you would experimentally test for the gases evolved during the thermal decomposition of magnesium nitrate:<br/>"
                   "(i) the brown gas, NO<sub>2</sub>(g)<br/>"
                   "(ii) the colourless gas, O<sub>2</sub>(g).", S['q_subpart']),
         Paragraph("<b>(3)</b>", S['q_submark'])]
    ], colWidths=[AVAIL_W - 1.2*cm, 1.2*cm]))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6, AVAIL_W))
    story.append(Spacer(1, 0.35 * cm))

    story.append(Table([
        [Paragraph("<b>(d)</b> Predict and explain the trend in thermal stability of the Group 2 nitrates down the group from Mg(NO<sub>3</sub>)<sub>2</sub> to Ba(NO<sub>3</sub>)<sub>2</sub>.<br/>"
                   "State how the decomposition temperature changes and explain the trend in terms of the lattice energies of the reactants and products.", S['q_subpart']),
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 6 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Purely ionic model assumes ions are rigid, perfectly spherical point charges with purely electrostatic attraction.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ag+ polarises the large, polarisable electron cloud of I-, introducing substantial covalent character (Fajans' rules).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Maximum covalent character occurs with small cation + high charge (high polarizing power) and large anion + high charge (high polarisability).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Enthalpy of hydration is the enthalpy change when 1 mol of gaseous ions dissolves in water to form infinitely dilute aqueous ions: Cl-(g) + aq -> Cl-(aq).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Hess cycle: ΔsolH° = ΣΔhydH° - ΔH_LE°(formation) = ΣΔhydH° + ΔH_LE°(dissociation).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Down Group 7, ionic radius increases while charge stays -1; charge density decreases, weakening ion-dipole attractions.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔsolH° = ΣΔhydH° - ΔH_LE° = [(-406) + (-378)] - (-787) = -784 - (-787) = +3 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Dissolving a solid crystal lattice releases ions into solution, creating a massive positive ΔS_system that easily overcomes the slight +ΔH.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Solubility of Group 2 sulfates decreases down the group; BaSO4 is insoluble (white precipitate).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Solubility of Group 2 hydroxides increases down the group; Ba(OH)2 is the most soluble.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("SO4^2- is huge, so lattice energy changes little down Group 2, while cation hydration enthalpy becomes significantly less exothermic.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("OH- is small, so lattice energy decreases rapidly down Group 2, more than compensating for the decrease in cation hydration enthalpy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("NaCl has hard, non-polarisable ions (Na+ and Cl-), making it nearly 100% ionic with minimal discrepancy (2.3%).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔH_LE° = ΣΔhydH° - ΔsolH° = [-1926 + 2(-378)] - (-155) = [-1926 - 756] + 155 = -2682 + 155 = -2527 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("F- is very small with high charge density, giving immense exothermic hydration enthalpy that makes dissolution of AgF highly favorable.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Polarizing power decreases down Group 2 as ionic radius increases with constant 2+ charge (charge density drops).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("AgI has 14.0% discrepancy due to extreme polarisation of large I- by polarizing Ag+ (4d^10).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Temperature increases => exothermic dissolution (ΔsolH° < 0), meaning sum of hydration enthalpies outweighs lattice energy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Fe3+ has higher charge and smaller radius than Fe2+, ordering surrounding water dipole molecules into a more rigid shell (large -ΔS).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Mg2+ is smallest with highest charge density, polarizing CO3^2- most strongly and facilitating decomposition at lowest T.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("ΔS_surroundings = -ΔH / T; since ΔH is positive (+14.8 kJ mol^-1), ΔS_surr is negative.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("Al3+ has 3+ charge and tiny radius (0.054 nm), giving the highest charge density among the options.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Lattice energy is inversely proportional to (r+ + r-); larger inter-ionic distance weakens electrostatic attraction.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("High charge density of Al3+ polarises chloride electron clouds so strongly that AlCl3 forms covalent molecules rather than an ionic lattice.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("q = m c ΔT = 50 * 4.18 * 4.2 = 877.8 J; moles = 3.73 / 74.6 = 0.0500 mol; ΔsolH° = +0.8778 / 0.0500 = +17.56 ≈ +17.6 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Hydration forms attractive ion-dipole interactions between ions and water dipoles, which is always exothermic.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("I- is larger than F-, resulting in greater inter-ionic separation (r+ + r-) in NaI, lowering electrostatic lattice energy.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("CH3COONa contains CH3COO- (conjugate base of weak acid), which hydrolyses in water to produce OH- ions.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("ΔH_hydr = ΔsolH(anhydrous) - ΔsolH(hydrated) = -66.5 - (+11.5) = -78.0 kJ mol^-1.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Divalent Ca2+ and SO4^2- ions order many water molecules into rigid hydration shells, causing a net loss of disorder.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Theoretical vs Experimental Lattice Energy & Covalency (18 Marks)",
         "<b>(a) [2 Marks]</b><br/>"
         "• Ions are point charges / spherical charges [1]<br/>"
         "• Bonding is 100% purely electrostatic / no electron sharing / no covalent character [1].<br/><br/>"
         "<b>(b) [2 Marks]</b><br/>"
         "• Na+ and Cl- are spherical ions with complete octets and low polarisation [1]<br/>"
         "• The bonding is almost 100% purely ionic, so the theoretical model matches experiment [1].<br/><br/>"
         "<b>(c) [5 Marks]</b><br/>"
         "• Ag+ has a 4d^10 pseudo-noble gas configuration, which is less effective at shielding nuclear charge than 2s^2 2p^6 in Na+ [2]<br/>"
         "• Ag+ has a higher effective nuclear charge and higher polarising power than Na+ [1]<br/>"
         "• Ag+ distorts / polarises the electron cloud of the chloride ion [1]<br/>"
         "• This distortion introduces covalent character into the bonding, providing additional bonding energy that makes experimental LE more exothermic [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Iodide (I-) has a significantly larger ionic radius than chloride (Cl-) [1]<br/>"
         "• The outer electron cloud of I- is further from its nucleus and more shielded [1]<br/>"
         "• Hence I- has a much higher polarisability than Cl- [1]<br/>"
         "• Polarization by Ag+ is much greater in AgI, producing substantial covalent character and a large 109 kJ mol^-1 (14%) discrepancy [1].<br/><br/>"
         "<b>(e) [5 Marks]</b><br/>"
         "• F- is very small and holds its electrons tightly (extremely low polarisability) [1]<br/>"
         "• Even the polarizing Ag+ cation cannot significantly distort F-, so AgF remains almost purely ionic (only 1.3% discrepancy) [1]<br/>"
         "• This trend confirms that covalency increases as anion size/polarisability increases (F- < Cl- < Br- < I-) [1]<br/>"
         "• Water solubility: AgF is highly soluble in water, whereas AgI is virtually insoluble [1]<br/>"
         "• Ionic AgF is readily hydrated, whereas covalent AgI has strong orbital overlap and insoluble covalent lattice [1]."),

        ("Question 32: Solution Enthalpy & Hydration Energy Cycles (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Cycle diagram showing solid KF(s) at bottom left, gaseous ions K+(g) + F-(g) at top, aqueous ions K+(aq) + F-(aq) at bottom right [1]<br/>"
         "• Arrow from K+(g) + F-(g) down to KF(s) labeled ΔH_LE°(formation) (or arrow up labeled ΔH_LE°(dissociation)) [1]<br/>"
         "• Arrow from K+(g) + F-(g) down to aqueous ions labeled ΣΔH_hyd° = ΔH_hyd°(K+) + ΔH_hyd°(F-) [1]<br/>"
         "• Arrow from KF(s) across to aqueous ions labeled ΔH_sol° [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• (i) For KF: ΔH_sol° = [ΔH_hyd°(K+) + ΔH_hyd°(F-)] - ΔH_LE° = [-322 + (-506)] - (-817) [1]<br/>"
         "• = -828 - (-817) = -11 kJ mol^-1 (exothermic, must have minus sign) [1]<br/>"
         "• (ii) For KCl: ΔH_sol° = [ΔH_hyd°(K+) + ΔH_hyd°(Cl-)] - ΔH_LE° = [-322 + (-378)] - (-711) [1]<br/>"
         "• = -700 - (-711) = +11 kJ mol^-1 (endothermic, must have plus sign) [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• F- has a much smaller ionic radius than Cl- (0.133 nm vs 0.181 nm) [1]<br/>"
         "• Both carry the same 1- charge, so F- has a much higher charge density [1]<br/>"
         "• F- forms much stronger ion-dipole attractions with the partial positive hydrogen atoms of water molecules [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• ΔS_surr = -ΔH_sol / T = -(+11 000 J mol^-1) / 298 K = -36.91 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = ΔS_sys + ΔS_surr = +75.3 + (-36.91) = +38.39 J K^-1 mol^-1 [2]<br/>"
         "• Since ΔS_total > 0, dissolution is spontaneous / KCl is soluble in water at 298 K [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• For KF, the combined hydration enthalpy (-828 kJ mol^-1) is more exothermic than the lattice energy is endothermic (+817 kJ mol^-1) [1]<br/>"
         "• Net heat is released to the water when bonds/interactions form [1]<br/>"
         "• The temperature of the solution rises, making the test tube feel hot [1]."),

        ("Question 33: Group 2 Sulfate Solubility Trends (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• (i) MgSO4: ΔH_sol° = [ΔH_hyd°(Mg2+) + ΔH_hyd°(SO4^2-)] - ΔH_LE° = [-1926 + (-1045)] - (-2884) [1]<br/>"
         "• = -2971 - (-2884) = -87 kJ mol^-1 (exothermic) [1]<br/>"
         "• (ii) BaSO4: ΔH_sol° = [ΔH_hyd°(Ba2+) + ΔH_hyd°(SO4^2-)] - ΔH_LE° = [-1305 + (-1045)] - (-2469) [1]<br/>"
         "• = -2350 - (-2469) = +119 kJ mol^-1 (endothermic) [1].<br/><br/>"
         "<b>(b) [5 Marks]</b><br/>"
         "• Lattice energy is proportional to 1 / (r_cation + r_anion) [1]<br/>"
         "• Sulfate SO4^2- is a very large anion (radius 0.230 nm) compared to cations [1]<br/>"
         "• The increase in cation radius from Mg2+ to Ba2+ makes only a small fractional difference to (r_cation + r_anion), so LE decreases only slightly (by 415 kJ mol^-1) [1]<br/>"
         "• Hydration enthalpy is proportional to 1 / r_cation alone [1]<br/>"
         "• Cation radius nearly doubles from Mg2+ to Ba2+, so hydration enthalpy decreases drastically (by 621 kJ mol^-1), dominating the enthalpy trend [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• ΔS_surr = -ΔH_sol / T = -(+119 000 J mol^-1) / 298 K = -399.33 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = -12.0 + (-399.33) = -411.33 J K^-1 mol^-1 [2]<br/>"
         "• ΔS_total is overwhelmingly negative, meaning BaSO4 dissolution is completely non-spontaneous / virtually insoluble [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• For MgSO4, ΔH_sol° is strongly exothermic (-87 kJ mol^-1) [1]<br/>"
         "• ΔS_surr = -(-87 000) / 298 = +291.95 J K^-1 mol^-1 [1]<br/>"
         "• ΔS_total = -108.0 + 291.95 = +183.95 J K^-1 mol^-1 > 0, so dissolution is spontaneous and highly soluble [1].<br/><br/>"
         "<b>(e) [2 Marks]</b><br/>"
         "• Observation: Dense white precipitate forms [1]<br/>"
         "• Equation: Ba^2+(aq) + SO4^2-(aq) —> BaSO4(s) [1]."),

        ("Question 34: *Level of Response — Contrasting Group 2 Solubility Trends (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Cation hydration enthalpy becomes less exothermic down the group from Mg2+ to Ba2+ [1]<br/>"
         "• Ionic radius increases while ionic charge remains 2+ [1]<br/>"
         "• Charge density decreases, weakening electrostatic attraction between cation and water dipoles [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive thermodynamic comparison. States ΔH_sol = ΣΔH_hyd - ΔH_LE. Explains that for hydroxides, OH- is small, so increasing cation radius significantly increases inter-ionic distance (r+ + r-), causing lattice energy to decrease rapidly down the group. This decrease in LE outweighs the decrease in cation hydration enthalpy, so ΔH_sol becomes more exothermic (or less endothermic), making ΔS_total more positive and solubility INCREASES. Explains that for sulfates, SO4^2- is very large, so (r+ + r-) changes very little, meaning LE decreases slowly down the group. The rapid decrease in cation hydration enthalpy outweighs the change in LE, so ΔH_sol becomes significantly more endothermic, making ΔS_total more negative and solubility DECREASES.<br/>"
         "• Level 2 (3-4 marks): Links anion size to lattice energy changes; gives correct trend in ΔH_sol with minor omissions in entropy reasoning.<br/>"
         "• Level 1 (1-2 marks): States solubility trends correctly with simple qualitative statements.<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• (i) Mg(OH)2(s) + 2HCl(aq) —> MgCl2(aq) + 2H2O(l) [1]<br/>"
         "• (ii) Mg(OH)2 has very low solubility, so [OH-(aq)] in solution is very low and does not burn mouth/throat tissues [1]<br/>"
         "• As stomach acid neutralises OH-, equilibrium Mg(OH)2(s) <=> Mg2+(aq) + 2OH-(aq) shifts right, neutralising acid gradually [1]<br/>"
         "• Ba(OH)2 is soluble and produces high [OH-] (highly alkaline/caustic), and Ba2+(aq) is a lethal systemic poison [1].<br/><br/>"
         "<b>(d) [5 Marks]</b><br/>"
         "• Prediction: Solubility of Group 2 carbonates DECREASES down the group (MgCO3 is slightly soluble, BaCO3 is insoluble) [1]<br/>"
         "• Carbonate CO3^2- (radius 0.185 nm) is a large polyatomic anion, similar to sulfate SO4^2- [1]<br/>"
         "• Because the anion is large, lattice energy changes relatively little down the group [1]<br/>"
         "• Cation hydration enthalpy decreases significantly down the group from Mg2+ to Ba2+ [1]<br/>"
         "• Therefore ΔH_sol becomes more endothermic down the group, reducing solubility [1]."),

        ("Question 35: Calorimetric Hydration Enthalpy of MgSO4 (18 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• (i) q1 = m c ΔT = 50.0 g * 4.18 J g^-1 K^-1 * (29.8 - 20.2) K = 50.0 * 4.18 * 9.6 = 2006.4 J [2]<br/>"
         "• (ii) Moles = 0.0500 mol; ΔH1 = -q / n = -2.0064 kJ / 0.0500 mol = -40.13 kJ mol^-1 (must be negative) [2].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• (i) q2 = m c ΔT = 50.0 g * 4.18 * (20.4 - 18.2) = 50.0 * 4.18 * 2.2 = 459.8 J [2]<br/>"
         "• (ii) Moles = 0.0500 mol; ΔH2 = +q / n = +0.4598 kJ / 0.0500 mol = +9.20 kJ mol^-1 (must be positive) [2].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Hess cycle: ΔH_hydr_salt° = ΔH1 - ΔH2 [1]<br/>"
         "• = (-40.13) - (+9.20) [2]<br/>"
         "• = -49.33 kJ mol^-1 (accept -49.1 to -49.5 kJ mol^-1) [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Adding exact stoichiometric amount of water (7 mol H2O per mol MgSO4) does not wet the solid uniformly [1]<br/>"
         "• Reaction is slow and incomplete (some anhydrous salt remains unhydrated, or other hydrates form) [1]<br/>"
         "• Solid crystals do not have a uniform temperature, making heat loss immense and accurate thermometer reading impossible [1].<br/><br/>"
         "<b>(e) [3 Marks]</b><br/>"
         "• Errors: Heat loss to surroundings / air / polystyrene cup; assuming solution heat capacity is exactly 4.18 J g^-1 K^-1 [2]<br/>"
         "• Modification: Record temperature every 30 seconds for 3 minutes before mixing, mix at minute 4, record temperature every 30 seconds, and extrapolate cooling curve back to time of mixing [1]."),

        ("Question 36: Barium Meal Diagnostics & Toxicology (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Ksp = [Ba^2+(aq)][SO4^2-(aq)] [1]<br/>"
         "• In pure water, [Ba^2+] = [SO4^2-] = s => s = sqrt(Ksp) = sqrt(1.08 x 10^-10) = 1.039 x 10^-5 mol dm^-3 [1]<br/>"
         "• In g dm^-3: 1.039 x 10^-5 mol dm^-3 * 137.3 g mol^-1 [1]<br/>"
         "• = 1.427 x 10^-3 g dm^-3 (approx 1.43 mg dm^-3) [1].<br/><br/>"
         "<b>(b) [3 Marks]</b><br/>"
         "• Volume = mass / concentration = 1.0 g / (1.427 x 10^-3 g dm^-3) [1]<br/>"
         "• = 701 dm^-3 (approx 700 litres) [1]<br/>"
         "• Comment: A patient would need to drink over 700 litres of saturated BaSO4 solution to receive a lethal dose, proving it is completely safe for clinical radiography [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Stomach acid contains H+(aq) ions from HCl [1]<br/>"
         "• BaCO3 reacts with acid: BaCO3(s) + 2H+(aq) —> Ba^2+(aq) + H2O(l) + CO2(g) [1]<br/>"
         "• CO2 gas escapes, driving the reaction to completion and releasing massive concentrations of toxic free Ba^2+ ions [1]<br/>"
         "• BaSO4 does not react with dilute acid because SO4^2- is the conjugate base of a strong acid and does not accept protons [1].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Na2SO4 is soluble and dissolves to provide a high concentration of sulfate ions, SO4^2-(aq) [1]<br/>"
         "• Equilibrium: BaSO4(s) <=> Ba^2+(aq) + SO4^2-(aq) [1]<br/>"
         "• By Le Chatelier's principle / common ion effect, the high [SO4^2-] shifts equilibrium heavily to the left [1]<br/>"
         "• This precipitates toxic Ba^2+ ions out of solution as harmless, insoluble BaSO4 solid [1]."),

        ("Question 37: Thermal Decomposition of Group 1 & 2 Nitrates (15 Marks)",
         "<b>(a) [4 Marks]</b><br/>"
         "• Li+ has a tiny ionic radius (0.076 nm), much smaller than other Group 1 cations [1]<br/>"
         "• Li+ has an unusually high charge density, comparable to Mg2+ (diagonal relationship) [1]<br/>"
         "• Li+ strongly polarises the nitrate electron cloud, weakening N-O bonds within the nitrate ion [1]<br/>"
         "• Hence it decomposes fully to oxide (Li2O), NO2, and O2, rather than stopping at nitrite [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Cation polarises the electron cloud of the nitrate anion, pulling electron density toward itself [1]<br/>"
         "• This weakens one of the N-O bonds in the nitrate ion [1]<br/>"
         "• The oxygen atom is stripped from the nitrate ion, forming an oxide ion (O^2-) in the metal oxide lattice [1]<br/>"
         "• The remaining fragment decomposes into brown NO2 gas and O2 gas [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• (i) NO2: Pungent brown gas; turns damp blue litmus paper red (acidic gas) [1]<br/>"
         "• (ii) O2: Colourless gas; relights a glowing splint [2].<br/><br/>"
         "<b>(d) [4 Marks]</b><br/>"
         "• Thermal stability INCREASES down Group 2 (decomposition temperature increases) [1]<br/>"
         "• Cation radius increases from Mg2+ to Ba2+ while charge remains 2+ [1]<br/>"
         "• Charge density and polarising power of the cation decrease down the group [1]<br/>"
         "• Nitrate ion electron cloud is less polarised/distorted, so more thermal energy is needed to break N-O bonds [1].")
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
    print(f"[SUCCESS] Week 6 Real Past Paper PDF generated successfully! Size: {size_mb:.2f} MB")


if __name__ == '__main__':
    build_pdf()
