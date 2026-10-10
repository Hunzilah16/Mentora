"""
build_usman_week11_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 11 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 15A.1: Chirality and Enantiomers (Asymmetric Carbon, Non-superimposable Mirror Images, 3D Wedge-Dash)
  - 15A.2: Optical Activity (Plane-polarised Light, Polarimetry, Dextro/Laevo, Racemic Mixtures)
  - 15A.3: Optical Activity & Reaction Mechanisms (SN1 Racemisation, SN2 Walden Inversion, Planar Carbonyl Addition)
  - 15B.1: Carbonyl Compounds & Physical Properties (Aldehydes, Ketones, Polarity, Boiling Points & Solubility)
  - 15B.2: Redox Reactions of Carbonyls (Oxidation with Tollens', Fehling's, Dichromate; Reduction with NaBH4/LiAlH4)

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
    "Usman_Edexcel_Chem_U4_Week11_150M_Challenging_Quiz.pdf"
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
    """Draws an authentic bordered box for organic reaction mechanisms and 3D structures."""
    def __init__(self, width=AVAIL_W, height=6.0*cm, caption="Space for structural drawings and mechanism"):
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 11 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 11 (150 Marks)...")
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
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W11</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 11 ASSESSMENT: CHIRALITY, OPTICAL ACTIVITY & CARBONYL CHEMISTRY</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 11 In-Depth Mastery)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 15A.1: Chirality and Enantiomers (Asymmetric Carbon, Non-superimposable Mirror Images)<br/>Topic 15A.2: Optical Activity & Polarimetry (Plane-polarised Light, Racemic Mixtures)<br/>Topic 15A.3: Optical Activity & Mechanisms (SN1 Racemisation vs SN2 Walden Inversion)<br/>Topic 15B.1: Carbonyl Compounds & Physical Properties (Dipole-Dipole, Boiling Points & Solubility)<br/>Topic 15B.2: Redox Reactions of Carbonyls (Tollens', Fehling's, Dichromate & Hydride Reductions)", S['edx_meta'])],
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
        ("Which of the following molecules possesses an asymmetric (chiral) carbon atom?",
         [("A", "Propan-2-ol"),
          ("B", "2-chlorobutane"),
          ("C", "1-bromopropane"),
          ("D", "Pentan-3-ol")]),

        ("Which statement correctly describes a racemic mixture (racemate)?",
         [("A", "An equimolar mixture of two diastereomers that rotates plane-polarised light"),
          ("B", "An equimolar mixture of two enantiomers that has no net optical rotation"),
          ("C", "A 100% pure sample of the dextrorotatory enantiomer"),
          ("D", "A mixture of structural isomers that have identical boiling points")]),

        ("How many chiral carbon atoms are present in a molecule of 2,3-dihydroxybutanoic acid, CH3CH(OH)CH(OH)COOH?",
         [("A", "1"),
          ("B", "2"),
          ("C", "3"),
          ("D", "4")]),

        # Page 3: Q4, Q5, Q6
        ("Why is propane-1,2-diol chiral while propane-1,3-diol is achiral?",
         [("A", "Propane-1,2-diol has a carbon bonded to four different groups: -H, -OH, -CH3, and -CH2OH"),
          ("B", "Propane-1,2-diol forms stronger intermolecular hydrogen bonds"),
          ("C", "Propane-1,3-diol possesses an internal plane of symmetry through carbon-1"),
          ("D", "Propane-1,2-diol contains an sp2 hybridised central carbon atom")]),

        ("The alkaline hydrolysis of pure (R)-2-bromobutane with aqueous sodium hydroxide proceeds via an SN2 mechanism. What is the stereochemical nature of the resulting butan-2-ol?",
         [("A", "100% (S)-butan-2-ol with complete inversion of configuration (Walden inversion)"),
          ("B", "100% (R)-butan-2-ol with complete retention of configuration"),
          ("C", "A 50:50 racemic mixture of (R)- and (S)-butan-2-ol"),
          ("D", "An optically inactive meso compound")]),

        ("When 2-bromo-2-methylbutane is hydrolysed by an SN1 mechanism in aqueous ethanol, the alcohol product is optically inactive. What is the reason for this observation?",
         [("A", "The carbocation intermediate is planar and is attacked with equal probability from either face"),
          ("B", "The leaving group attacks the opposite face of the carbon skeleton"),
          ("C", "The product undergoes immediate racemisation by keto-enol tautomerism"),
          ("D", "The starting material does not contain an asymmetric carbon atom")]),

        # Page 4: Q7, Q8, Q9
        ("When ethanal reacts with hydrogen cyanide, HCN, in the presence of KCN, the 2-hydroxypropanenitrile product is optically inactive. Why?",
         [("A", "The product molecule does not have a chiral centre"),
          ("B", "The planar carbonyl group is attacked equally from above and below, yielding a 50:50 racemate"),
          ("C", "The cyanide ion destroys the asymmetric centre during nucleophilic attack"),
          ("D", "2-hydroxypropanenitrile is a meso compound with internal symmetry")]),

        ("Which of the following compounds exhibits optical isomerism?",
         [("A", "CH3CH2CH2CHO"),
          ("B", "CH3CH(OH)CH2CH3"),
          ("C", "CH3COCH2CH3"),
          ("D", "(CH3)2CHCOOH")]),

        ("What happens to plane-polarised light when it passes through a solution containing a single enantiomer of an optically active compound?",
         [("A", "The plane of polarisation is rotated clockwise or anticlockwise by a specific angle"),
          ("B", "The light is completely absorbed and converted into infrared heat"),
          ("C", "The light is refracted into multiple beams of differing wavelengths"),
          ("D", "The light emerges unpolarised in all transverse directions")]),

        # Page 5: Q10, Q11, Q12
        ("Butanal (Mr = 72, bp 75 °C) has a significantly higher boiling point than pentane (Mr = 72, bp 36 °C). What is the primary reason?",
         [("A", "Butanal forms intermolecular hydrogen bonds between its molecules"),
          ("B", "Butanal has permanent dipole-dipole attractions due to the polar C=O group"),
          ("C", "Pentane has stronger London dispersion forces than butanal"),
          ("D", "Butanal forms cyclic dimers in the liquid phase")]),

        ("Why does butan-1-ol (Mr = 74, bp 117 °C) have a higher boiling point than butanal (Mr = 72, bp 75 °C)?",
         [("A", "Butan-1-ol has a more branched carbon chain"),
          ("B", "Butan-1-ol can form intermolecular hydrogen bonds between its own molecules, whereas butanal cannot"),
          ("C", "The C-O single bond in butan-1-ol is more polar than the C=O double bond in butanal"),
          ("D", "Butanal decomposes at temperatures above 80 °C")]),

        ("Why are propanal and propanone completely miscible with water, whereas hexanal and hexan-2-one are virtually insoluble?",
         [("A", "Lower carbonyls form hydrogen bonds with water molecules via the oxygen lone pair, whereas longer alkyl chains disrupt water's H-bond network"),
          ("B", "Higher carbonyls react with water to form insoluble polymers"),
          ("C", "Hexanal molecules are ionic and form insoluble lattices"),
          ("D", "Propanone undergoes rapid hydration to form propane-2,2-diol crystals")]),

        # Page 6: Q13, Q14, Q15
        ("Which reagent can be used to distinguish between propanal and propanone?",
         [("A", "2,4-dinitrophenylhydrazine (Brady's reagent)"),
          ("B", "Tollens' reagent (ammoniacal silver nitrate)"),
          ("C", "Sodium tetrahydridoborate(III), NaBH4"),
          ("D", "Phosphorus pentachloride, PCl5")]),

        ("What observation is recorded when propanal is warmed with Tollens' reagent in a clean test tube?",
         [("A", "An orange precipitate forms"),
          ("B", "A silver mirror (or grey precipitate) is deposited on the test tube wall"),
          ("C", "A deep blue solution turns clear and colourless"),
          ("D", "Steamy acidic fumes of hydrogen chloride are evolved")]),

        ("What is the observation when butanal is heated with Fehling's solution?",
         [("A", "The deep blue solution forms a brick-red precipitate of copper(I) oxide, Cu2O"),
          ("B", "A purple solution is decolourised"),
          ("C", "A yellow precipitate of tri-iodomethane is formed"),
          ("D", "Effervescence of carbon dioxide gas occurs")]),

        # Page 7: Q16, Q17, Q18
        ("Which reducing agent is used in aqueous or alcoholic solution to reduce aldehydes and ketones safely without reducing C=C bonds?",
         [("A", "Sodium tetrahydridoborate(III), NaBH4"),
          ("B", "Concentrated sulfuric acid, H2SO4"),
          ("C", "Potassium dichromate(VI), K2Cr2O7"),
          ("D", "Tin and concentrated hydrochloric acid, Sn / HCl")]),

        ("What organic product is formed when butanone is reduced with NaBH4 in aqueous ethanol?",
         [("A", "Butan-1-ol"),
          ("B", "Butan-2-ol"),
          ("C", "Butanoic acid"),
          ("D", "2-methylpropan-2-ol")]),

        ("What species acts as the nucleophile in the first step of the reduction of a carbonyl compound by NaBH4?",
         [("A", "Hydride ion, H- (transferred from BH4-)"),
          ("B", "Boron cation, B3+"),
          ("C", "Hydroxide ion, OH-"),
          ("D", "Proton, H+")]),

        # Page 8: Q19, Q20, Q21
        ("Why must Tollens' reagent be freshly prepared and discarded safely immediately after use?",
         [("A", "It evaporates rapidly and loses all ammonia"),
          ("B", "On standing or drying, it forms explosive silver fulminate / silver nitride compounds"),
          ("C", "It is rapidly oxidised by air to nitric acid"),
          ("D", "It turns permanently black and loses its basicity")]),

        ("A carbonyl compound X (C5H10O) gives a silver mirror with Tollens' reagent and contains a chiral carbon atom. What is compound X?",
         [("A", "Pentan-2-one"),
          ("B", "2-methylbutanal"),
          ("C", "3-methylbutanal"),
          ("D", "Pentan-3-one")]),

        ("How many optical stereoisomers are theoretically possible for a molecule containing 3 non-identical chiral centres?",
         [("A", "3"),
          ("B", "6"),
          ("C", "8"),
          ("D", "9")]),

        # Page 9: Q22, Q23, Q24
        ("When butanone is reduced by NaBH4, why is the resulting butan-2-ol optically inactive?",
         [("A", "The product molecule does not contain an asymmetric carbon atom"),
          ("B", "Hydride attack on the planar carbonyl group occurs with equal probability from either face, producing an equimolar racemate"),
          ("C", "NaBH4 acts as an optically pure catalyst"),
          ("D", "The alcohol product rapidly undergoes dehydration to but-2-ene")]),

        ("Which of the following compounds will NOT react with acidified potassium dichromate(VI) under reflux?",
         [("A", "Propanal"),
          ("B", "Propan-1-ol"),
          ("C", "Propanone"),
          ("D", "Propan-2-ol")]),

        ("In Fehling's solution, what is the role of the sodium potassium tartrate?",
         [("A", "To act as the primary oxidising agent"),
          ("B", "To complex copper(II) ions and keep them in solution in strongly alkaline conditions"),
          ("C", "To lower the boiling point of the mixture"),
          ("D", "To neutralise the carboxylic acid formed")]),

        # Page 10: Q25, Q26, Q27
        ("A sample of pure (+)-lactic acid has a specific optical rotation of +3.8°. What is the specific optical rotation of a 50:50 mixture of (+)-lactic acid and (-)-lactic acid?",
         [("A", "+3.8°"),
          ("B", "-3.8°"),
          ("C", "0.0°"),
          ("D", "+1.9°")]),

        ("During the oxidation of an aldehyde by acidified potassium dichromate(VI), what is the oxidation state change of chromium?",
         [("A", "+7 to +2"),
          ("B", "+6 to +3"),
          ("C", "+6 to 0"),
          ("D", "+5 to +3")]),

        ("Compound Z has molecular formula C3H6O. It forms an orange precipitate with 2,4-DNPH, but does NOT react with Fehling's solution. What is Z?",
         [("A", "Propanal"),
          ("B", "Propanone"),
          ("C", "Prop-2-en-1-ol"),
          ("D", "Methoxyethene")]),

        # Page 11: Q28, Q29, Q30
        ("How many chiral carbon atoms are present in a molecule of 3-methylhexane?",
         [("A", "0"),
          ("B", "1 (carbon-3)"),
          ("C", "2"),
          ("D", "3")]),

        ("Why was administering only the pure (R)-enantiomer of thalidomide ineffective at preventing birth defects in pregnant patients?",
         [("A", "The (R)-enantiomer is biologically inert and has no sedative effect"),
          ("B", "The (R)-enantiomer undergoes rapid racemisation in vivo at physiological blood pH to form the teratogenic (S)-enantiomer"),
          ("C", "The (R)-enantiomer is converted to toxic cyanide ions in the liver"),
          ("D", "Enantiomers cannot be separated by any chemical technique")]),

        ("What type of intermolecular forces exist between molecules of pure ethanal in the liquid state?",
         [("A", "London dispersion forces and permanent dipole-dipole attractions only"),
          ("B", "Hydrogen bonds and London dispersion forces only"),
          ("C", "Ionic bonds and covalent bonds"),
          ("D", "Hydrogen bonds, dipole-dipole attractions, and London forces")])
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
    # QUESTION 31 (18 MARKS) — CHIRALITY, 3D ENANTIOMERS & SN1 vs SN2 MECHANISMS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Stereoisomerism arises when molecules have the same structural formula but different spatial arrangements of atoms.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Define what is meant by a <i>chiral centre</i> and state the relationship between a pair of <i>enantiomers</i>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In the box below, draw three-dimensional wedge-and-dash tetrahedral representations of the two enantiomers of butan-2-ol, CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub>. Clearly indicate the mirror plane.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for 3D tetrahedral enantiomer drawings and mirror plane"))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Explain how a polarimeter is used to distinguish between a single pure enantiomer and a racemic mixture of the same compound. Explain why a racemic mixture shows zero net optical rotation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>31 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;The stereochemical outcome of nucleophilic substitution reactions depends on the reaction mechanism.<br/>"
                           "A sample of optically pure (R)-2-bromobutane is hydrolysed by heating with aqueous sodium hydroxide, NaOH(aq).<br/>"
                           "The resulting butan-2-ol is found to be optically active, consisting of 85% (S)-butan-2-ol and 15% (R)-butan-2-ol.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(i)&nbsp;&nbsp;Explain, with the aid of a curly arrow mechanism and drawing of the transition state, why the predominant mechanism is S<sub>N</sub>2, leading to inversion of configuration (Walden inversion).", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for SN2 mechanism, curly arrows, and pentacoordinate transition state"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why the product is NOT 100% (S)-butan-2-ol, identifying the competing reaction mechanism and describing the intermediate responsible for the partial racemisation.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Contrast this with the hydrolysis of 2-bromo-2-methylpropane under identical conditions. State the stereochemical outcome and justify your answer by referring to carbocation geometry.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — CARBONYL PHYSICAL PROPERTIES & INTERMOLECULAR FORCES
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;The physical properties of carbonyl compounds are governed by the polar carbon-oxygen double bond.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;The table below shows the boiling points of three organic compounds of similar relative molecular mass:", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))

    bp_table = [
        [Paragraph("<b>Compound</b>", S['tbl_th']), Paragraph("<b>Formula</b>", S['tbl_th']), Paragraph("<b>Mr</b>", S['tbl_th']), Paragraph("<b>Boiling Point / °C</b>", S['tbl_th'])],
        [Paragraph("Butane", S['tbl_td_l']), Paragraph("CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>", S['tbl_td']), Paragraph("58.1", S['tbl_td']), Paragraph("-0.5", S['tbl_td'])],
        [Paragraph("Propanal", S['tbl_td_l']), Paragraph("CH<sub>3</sub>CH<sub>2</sub>CHO", S['tbl_td']), Paragraph("58.1", S['tbl_td']), Paragraph("48.8", S['tbl_td'])],
        [Paragraph("Propan-1-ol", S['tbl_td_l']), Paragraph("CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", S['tbl_td']), Paragraph("60.1", S['tbl_td']), Paragraph("97.2", S['tbl_td'])],
    ]
    t_bp = Table(bp_table, colWidths=[4.2*cm, 5.8*cm, 2.5*cm, 3.5*cm])
    t_bp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_bp)
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("Identify the specific intermolecular forces present in each pure liquid, and explain how the nature and strength of these forces account for the trend in boiling points.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Propanone is miscible with water in all proportions, whereas hexan-2-one is virtually insoluble in water.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why propanone dissolves readily in water. In the space below, draw a diagram showing a propanone molecule forming hydrogen bonds with two water molecules. Include all partial charges and lone pairs involved.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for hydrogen bonding diagram: propanone and two water molecules"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>32 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why hexan-2-one is virtually insoluble in water, despite containing the same polar carbonyl group.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Explain why butanal molecules can act as hydrogen bond acceptors from water molecules, but CANNOT act as hydrogen bond donors to other butanal molecules.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Compare the boiling points of 2-methylpropanal and butanal. Explain why branched-chain carbonyl isomers have lower boiling points than their straight-chain counterparts.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — REDOX REACTIONS OF CARBONYL COMPOUNDS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;Aldehydes and ketones show distinct redox behavior due to the presence or absence of a hydrogen atom bonded directly to the carbonyl carbon.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;A technician has three unlabelled bottles: <b>A</b> (pentanal), <b>B</b> (pentan-2-one), and <b>C</b> (pentan-3-one).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Describe the preparation of Tollens' reagent starting from aqueous silver nitrate, and explain why it must be prepared freshly and never stored.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;State the observation when pentanal is warmed with Tollens' reagent and write a balanced ionic equation for the reaction, showing the organic product and the reduction of the silver complex.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Describe the reaction of pentanal when heated with Fehling's solution. State the initial and final appearance of the mixture and write an ionic equation for the reduction of copper(II) ions.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>33 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Reduction reactions can convert carbonyl compounds into alcohols.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;State the reagent and solvent required to reduce pentan-2-one to pentan-2-ol safely at room temperature.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Draw the mechanism for the reduction of pentan-2-one by NaBH4 in aqueous ethanol. Include all relevant dipole charges, lone pairs, curly arrows, and the intermediate alkoxide ion.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for curly arrow reduction mechanism: nucleophilic hydride attack and protonation"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Lithium tetrahydridoaluminate(III), LiAlH4, is a stronger reducing agent than NaBH4. Explain why LiAlH4 must be used in dry ethoxyethane (dry ether) and must NEVER come into contact with water. Write an equation for the vigorous reaction of LiAlH4 with water.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — STEREOCHEMISTRY OF CARBONYL REACTIONS (PLANAR C=O)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;The stereochemical outcome of nucleophilic addition to carbonyl groups depends critically on the planar geometry of the sp2 hybridised carbonyl carbon.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Butanal and butanone are both reduced by NaBH4 to form alcohols.<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Butanal &rarr; Butan-1-ol<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;Butanone &rarr; Butan-2-ol", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Explain why butan-1-ol is optically inactive.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Butan-2-ol possesses an asymmetric carbon atom (carbon-2). Explain, with the aid of a diagram showing the trigonal planar carbonyl group, why the butan-2-ol formed by the reduction of butanone is completely optically inactive.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for planar C=O diagram showing hydride attack with equal probability from both faces"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>34 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Propanal reacts with hydrogen cyanide, HCN, in the presence of potassium cyanide, KCN, at room temperature to form 2-hydroxybutanenitrile, CH<sub>3</sub>CH<sub>2</sub>CH(OH)CN.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical equation for the formation of 2-hydroxybutanenitrile from propanal and HCN.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Identify the attacking nucleophile and draw the full curly arrow mechanism for this reaction, showing the formation of the intermediate and its subsequent protonation.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.0*cm, caption="Space for nucleophilic addition mechanism: cyanide attack on propanal"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Explain why the 2-hydroxybutanenitrile product is a racemic mixture and predict its effect on plane-polarised light.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;If the reaction in (b) is carried out using an optically pure chiral aldehyde, such as (R)-2-methylbutanal, the resulting hydroxynitrile mixture is optically active and does NOT consist of an equimolar racemate. Explain why equal attack from both faces does NOT occur in this case.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — EXPERIMENTAL CHARACTERISATION (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;A research chemist investigated an unlabelled colourless liquid, <b>Q</b>, known to have the molecular formula C<sub>4</sub>H<sub>8</sub>O.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Draw the skeletal formulae and state the systematic IUPAC names of the two carbonyl isomers having molecular formula C<sub>4</sub>H<sub>8</sub>O.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Outline a simple test-tube reaction that would distinguish between these two isomers. State the reagent used and the observation for each isomer.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;The student is tasked with confirming the identity of isomer <b>Q</b> and investigating whether its reduction product is optically active.<br/>"
                           "Describe a detailed experimental plan to:<br/>"
                           "- Confirm whether <b>Q</b> is an aldehyde or ketone using Tollens' reagent.<br/>"
                           "- Reduce compound <b>Q</b> to the corresponding alcohol using sodium tetrahydridoborate(III), NaBH4, in ethanol.<br/>"
                           "- Separate and purify the alcohol product from the reaction mixture using solvent extraction and fractional distillation.<br/>"
                           "- Test the purified alcohol using a polarimeter to determine whether it is optically active or a racemate.<br/>"
                           "- Identify two key hazards in this multi-step synthesis and explain the precautions taken to minimize risk.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>*35 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Infrared (IR) spectroscopy is used to monitor the progress of the reduction reaction in (b).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;State the characteristic wavenumber absorption range that will disappear from the spectrum when compound <b>Q</b> is completely converted.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;State the characteristic wavenumber absorption range that will appear in the spectrum of the purified alcohol product, and describe the appearance of this peak.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Aldehydes are generally significantly more reactive towards nucleophiles than ketones.<br/>"
                           "Explain this difference in reactivity by considering:<br/>"
                           "- The electronic inductive effect of the alkyl groups.<br/>"
                           "- Steric hindrance around the carbonyl carbon atom.", S['q_subpart']))
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
    # QUESTION 36 (15 MARKS) — PHARMACEUTICAL CHIRALITY: THALIDOMIDE & IBUPROFEN
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Pharmaceutical Chemistry and Enantiopurity:</b><br/>"
                           "Enantiomers often exhibit dramatically different pharmacological activities because drug receptors and metabolic enzymes in the human body are chiral proteins.<br/>"
                           "<b>Thalidomide</b> (C<sub>13</sub>H<sub>10</sub>N<sub>2</sub>O<sub>4</sub>, Mr = 258.2) was prescribed in the late 1950s as a sedative and morning sickness remedy. The (R)-enantiomer acts as an effective sedative, whereas the (S)-enantiomer is teratogenic, causing severe limb deformities (phocomelia).<br/>"
                           "<b>Ibuprofen</b> (2-(4-isobutylphenyl)propanoic acid, Mr = 206.3) is an anti-inflammatory drug where (S)-ibuprofen is 160 times more active than (R)-ibuprofen.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;In the space below, draw the skeletal structure of ibuprofen and mark the chiral centre with an asterisk (*). Draw 3D representations of the two enantiomers.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for ibuprofen structure with chiral carbon (*) and 3D enantiomers"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why pharmaceutical manufacturers market ibuprofen as a racemic mixture rather than purifying the active (S)-enantiomer, considering both human liver metabolism and manufacturing cost.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>36 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Following the thalidomide tragedy, pharmaceutical chemists suggested that tragedy could have been prevented by administering pure (R)-thalidomide.<br/>"
                           "Explain, from a chemical equilibrium perspective, why administering enantiopure (R)-thalidomide does NOT protect pregnant patients against teratogenic birth defects.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Modern drug development relies heavily on <i>enantioselective (asymmetric) synthesis</i>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Define what is meant by an <i>enantioselective synthesis</i>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;State two economic or environmental advantages to the pharmaceutical industry of using chiral catalysts to produce single enantiomers directly, rather than synthesizing and resolving a racemic mixture.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — ATMOSPHERIC FORMALDEHYDE & BIO-VANILLIN PURITY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Atmospheric Chemistry and Bio-based Flavourings:</b><br/>"
                           "Formaldehyde (methanal, HCHO) is a volatile organic pollutant involved in photochemical smog formation. In industrial flavouring chemistry, vanillin (4-hydroxy-3-methoxybenzaldehyde, C<sub>8</sub>H<sub>8</sub>O<sub>3</sub>, Mr = 152.15) is extracted from biomass or synthesized from lignin.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the chemical equation for the industrial manufacture of formaldehyde by the catalytic oxidation of methanol with oxygen over a silver catalyst at 600 °C.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In aqueous solution (formalin), formaldehyde exists over 99.9% as methanediol, CH<sub>2</sub>(OH)<sub>2</sub>, via hydration:<br/>"
                           "HCHO(aq) &nbsp;+&nbsp; H<sub>2</sub>O(l) &nbsp;&lt;=&gt;&nbsp; CH<sub>2</sub>(OH)<sub>2</sub>(aq)<br/>"
                           "In contrast, propanone in water is less than 0.2% hydrated at equilibrium.<br/>"
                           "Explain this immense difference in equilibrium position, referring to both electronic inductive effects and steric hindrance around the carbonyl carbon.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>37 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Vanillin contains an aromatic aldehyde group that can be reduced to vanillyl alcohol (4-(hydroxymethyl)-2-methoxyphenol).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;State the reagents and conditions to reduce vanillin into vanillyl alcohol.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;A sample of synthetic vanillin is tested for purity. A 1.522 g sample of the vanillin is dissolved in ethanol and treated with excess Tollens' reagent.<br/>"
                           "The metallic silver precipitate is collected, washed with deionised water, dried, and weighed. The mass of metallic silver obtained is 2.050 g.<br/>"
                           "Given that 1 mole of vanillin reduces 2 moles of Ag+ to Ag(s), calculate the percentage purity of the vanillin sample by mass. (Ar: Ag = 107.9, C = 12.0, H = 1.0, O = 16.0)", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Percentage Purity = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;State how a chemist could verify using thin-layer chromatography (TLC) that the reduction of vanillin to vanillyl alcohol has gone to completion.", S['q_subpart']))
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
        [Paragraph("Avogadro Constant", S['tbl_td_l']), Paragraph("L = 6.02 x 10^23", S['tbl_td']), Paragraph("mol^-1", S['tbl_td'])],
        [Paragraph("Specific Optical Rotation", S['tbl_td_l']), Paragraph("[α] = α / (c * l)", S['tbl_td']), Paragraph("deg dm^-1 g^-1 cm^3", S['tbl_td'])],
        [Paragraph("Standard Temperature and Pressure", S['tbl_td_l']), Paragraph("T = 298 K, P = 100 kPa (1 bar)", S['tbl_td']), Paragraph("K, kPa", S['tbl_td'])],
        [Paragraph("Infrared C=O Aldehyde/Ketone", S['tbl_td_l']), Paragraph("1740 - 1690", S['tbl_td']), Paragraph("cm^-1", S['tbl_td'])],
        [Paragraph("Infrared O-H Alcohol (broad)", S['tbl_td_l']), Paragraph("3750 - 3200", S['tbl_td']), Paragraph("cm^-1", S['tbl_td'])],
        [Paragraph("Infrared C-H Aldehyde (doublet)", S['tbl_td_l']), Paragraph("2900 - 2820 and 2775 - 2700", S['tbl_td']), Paragraph("cm^-1", S['tbl_td'])],
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 11 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("2-chlorobutane has carbon-2 bonded to four distinct groups: -H, -Cl, -CH3, and -CH2CH3.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Definition: equimolar mixture of enantiomers where equal and opposite optical rotations cancel.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carbon-2 and Carbon-3 each have four different groups attached, giving 2 chiral centres.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Propane-1,2-diol has carbon-2 bonded to 4 different groups; propane-1,3-diol has two identical -CH2OH groups.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("SN2 mechanism proceeds by backside attack (180° to leaving group), causing Walden inversion.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("SN1 proceeds via a planar carbocation; attack from top and bottom faces occurs equally.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ethanal has a trigonal planar carbonyl group; attack of CN- from both faces gives a 50:50 racemate.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Butan-2-ol has carbon-2 bonded to -H, -OH, -CH3, and -C2H5, displaying optical activity.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Chiral molecules rotate the plane of polarisation by an angle α measured on a polarimeter.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("The polar C=O bond creates permanent dipole-dipole attractions, stronger than pentane's London forces.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Alcohols form strong intermolecular hydrogen bonds; carbonyl molecules lack an O-H bond.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Small carbonyls form H-bonds with water via O lone pair; long hydrophobic tails prevent solubility.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Tollens' reagent oxidises aldehydes to carboxylates (silver mirror); ketones do not react.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ag+ is reduced to metallic silver, forming a specular mirror on clean glass.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Fehling's blue Cu2+ is reduced to a brick-red precipitate of copper(I) oxide, Cu2O.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("NaBH4 is mild, selectively reducing C=O to alcohols in aqueous/ethanolic media without touching C=C.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ketones are reduced to secondary alcohols; butanone gives butan-2-ol.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Hydride ion, H-, is transferred from BH4- to attack the electrophilic carbonyl carbon.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Dry Tollens' residue forms fulminating silver (Ag3N / AgN3), which detonates on touch.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("2-methylbutanal has an aldehyde group (silver mirror) and carbon-2 is chiral.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Number of stereoisomers = 2^n = 2^3 = 8.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Butanone is planar around C=O; attack by H- from both faces is equally probable, forming a racemate.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Ketones have no hydrogen on the carbonyl carbon and resist oxidation by acidified dichromate.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Tartrate acts as a bidentate ligand, chelating Cu2+ and preventing precipitation of Cu(OH)2 in alkali.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("A 50:50 mixture is a racemate; the clockwise and anticlockwise rotations cancel to give 0.0°.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Orange dichromate(VI) (Cr = +6) is reduced to green chromium(III) (Cr = +3).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Propanone gives orange 2,4-DNP derivative (carbonyl present), but is a ketone (no Tollens' reaction).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carbon-3 in 3-methylhexane is bonded to -H, -CH3, -CH2CH3, and -CH2CH2CH3 (4 different groups).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Thalidomide racemises rapidly in blood via enolisation, generating the teratogenic (S)-enantiomer.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Pure liquid ethanal has London forces and dipole-dipole attractions; it cannot form intermolecular H-bonds.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Chirality & Reaction Mechanisms (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Chiral centre: a carbon atom bonded to four different atoms or groups of atoms [1]<br/>"
         "• Enantiomers: non-superimposable mirror images of each other [1].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• Two 3D tetrahedral drawings shown with wedge, dash, and two solid lines [1]<br/>"
         "• Mirror-image reflection correct with central C bonded to -H, -OH, -CH3, -CH2CH3 and mirror plane indicated [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Monochromatic light is passed through a polarising filter to produce plane-polarised light [1]<br/>"
         "• Pure single enantiomer rotates the plane of plane-polarised light clockwise (+) or anticlockwise (-) by angle α [1]<br/>"
         "• Racemic mixture contains equal concentrations (50:50) of both (+) and (-) enantiomers [1]<br/>"
         "• The equal and opposite rotations cancel each other out completely, producing zero net optical rotation [1].<br/><br/>"
         "<b>(c)(i) [4 Marks]</b><br/>"
         "• Curly arrow from lone pair of OH- attacking back of C-Br bond (180° to Br) [1]<br/>"
         "• Curly arrow showing C-Br bond breaking with electrons moving to Br [1]<br/>"
         "• Pentacoordinate transition state drawn with partial bonds to OH and Br, brackets, and negative charge [1]<br/>"
         "• Backside attack forces the remaining three groups to flip like an umbrella, inverting the configuration to (S)-butan-2-ol [1].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• Competing SN1 mechanism operates simultaneously [1]<br/>"
         "• Loss of Br- forms a planar carbocation intermediate [1]<br/>"
         "• Nucleophilic attack on the planar carbocation occurs from both sides, producing a racemic component that reduces enantiopurity from 100% to 85% [1].<br/><br/>"
         "<b>(c)(iii) [3 Marks]</b><br/>"
         "• 2-bromo-2-methylpropane is a tertiary halogenoalkane and hydrolyses 100% via SN1 [1]<br/>"
         "• The intermediate tertiary carbocation is trigonal planar around C+ [1]<br/>"
         "• Nucleophile attacks equally from both faces, producing an optically inactive 50:50 racemic mixture [1]."),

        ("Question 32: Carbonyl Physical Properties (18 Marks)",
         "<b>(a) [6 Marks]</b><br/>"
         "• Butane: London dispersion forces only [1]. Instantaneous dipole-induced dipole forces are relatively weak, requiring little thermal energy to overcome, giving lowest bp (-0.5 °C) [1]<br/>"
         "• Propanal: London forces AND permanent dipole-dipole attractions [1]. The polar C=O bond produces significant permanent dipoles that attract neighbouring molecules, requiring more energy to separate than butane (bp 48.8 °C) [1]<br/>"
         "• Propan-1-ol: London forces, dipole-dipole, AND hydrogen bonding [1]. The O-H group allows intermolecular hydrogen bonding between alcohol molecules; hydrogen bonds are significantly stronger than dipole-dipole forces, giving highest bp (97.2 °C) [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• Propanone dissolves because the oxygen atom has two lone pairs and forms hydrogen bonds with water molecules [1]<br/>"
         "• Diagram correctly shows propanone C=O with lone pairs and partial charges (Cδ+, Oδ-) [1]<br/>"
         "• Two water molecules shown with Hδ+ interacting with oxygen lone pairs via dashed lines [1]<br/>"
         "• H-O-H bond angle around water depicted as non-linear (~104.5°) with correct dipoles [1].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Hexan-2-one has a long non-polar hydrophobic hydrocarbon chain (5 carbons) [1]<br/>"
         "• The long alkyl chain cannot form hydrogen bonds and disrupts the extensive hydrogen-bonded network of water [1]<br/>"
         "• Energy released by forming H-bonds with the C=O group is insufficient to compensate for breaking water-water hydrogen bonds and overcoming alkyl-alkyl London forces [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Carbonyl oxygen has lone pairs of electrons and a partial negative charge (Oδ-), enabling it to accept hydrogen bonds from species with Hδ+ [1]<br/>"
         "• Butanal has no hydrogen atom bonded directly to oxygen (no O-H bond); all H atoms are bonded to carbon (C-H), which are not sufficiently polarised to donate hydrogen bonds [1]<br/>"
         "• Thus pure carbonyl compounds cannot hydrogen bond with themselves, resulting in much higher volatility than alcohols of similar mass [1].<br/><br/>"
         "<b>(d) [2 Marks]</b><br/>"
         "• 2-methylpropanal has a branched, spherical shape with smaller molecular surface contact area [1]<br/>"
         "• Less surface contact leads to weaker London dispersion forces compared to the elongated straight chain of butanal, lowering the boiling point [1]."),

        ("Question 33: Redox Reactions of Carbonyls (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Add dilute sodium hydroxide to aqueous silver nitrate to form brown precipitate of silver(I) oxide, Ag2O [1]<br/>"
         "• Add dilute aqueous ammonia dropwise with swirling until the precipitate completely dissolves to form clear [Ag(NH3)2]+ [1]<br/>"
         "• Must be prepared freshly because dry residues on standing form explosive silver fulminate / silver nitride [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Observation: Silver mirror forms on the inner wall of the test tube (or grey precipitate) [1]<br/>"
         "• Equation: RCHO + 2[Ag(NH3)2]+ + 3OH- --> RCOO- + 2Ag + 4NH3 + 2H2O (or RCHO + 2Ag+ + H2O --> RCOOH + 2Ag + 2H+) [2].<br/><br/>"
         "<b>(a)(iii) [3 Marks]</b><br/>"
         "• Observation: Deep blue solution turns to a brick-red precipitate [1]<br/>"
         "• Precipitate is copper(I) oxide, Cu2O [1]<br/>"
         "• Ionic equation: RCHO + 2Cu2+ + 5OH- --> RCOO- + Cu2O + 3H2O (or 2Cu2+ + 2OH- + 2e- --> Cu2O + H2O) [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• Reagent: Sodium tetrahydridoborate(III), NaBH4 [1]<br/>"
         "• Solvent: Aqueous ethanol (or methanol / water) [1].<br/><br/>"
         "<b>(b)(ii) [4 Marks]</b><br/>"
         "• Curly arrow from lone pair / bond of H- (or B-H bond in BH4-) to the carbonyl carbon atom [1]<br/>"
         "• Curly arrow from C=O double bond to oxygen atom [1]<br/>"
         "• Structure of tetrahedral alkoxide intermediate: CH3CH2CH2CH(O-)CH3 [1]<br/>"
         "• Curly arrow from O- lone pair to H of H2O / alcohol, forming pentan-2-ol [1].<br/><br/>"
         "<b>(b)(iii) [3 Marks]</b><br/>"
         "• LiAlH4 is a much stronger base/reducing agent that reacts violently/explosively with water, releasing flammable hydrogen gas [1]<br/>"
         "• Dry ethoxyethane is aprotic and does not contain acidic protons [1]<br/>"
         "• Equation: LiAlH4 + 4H2O --> LiOH + Al(OH)3 + 4H2 [1]."),

        ("Question 34: Stereochemistry of Carbonyl Reactions (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Butan-1-ol has formula CH3CH2CH2CH2OH; carbon-1 is bonded to two identical hydrogen atoms [1]<br/>"
         "• It possesses no asymmetric carbon atom (chiral centre), so it cannot exhibit optical activity [1].<br/><br/>"
         "<b>(a)(ii) [5 Marks]</b><br/>"
         "• Carbonyl carbon in butanone is sp2 hybridised with trigonal planar geometry (120° bond angles) [1]<br/>"
         "• Hydride ion (H-) can attack the planar carbonyl group from the top face or bottom face [1]<br/>"
         "• The two faces are completely unhindered and structurally equivalent, so attack from either face occurs with equal probability (50% from top, 50% from bottom) [1]<br/>"
         "• Top attack yields (R)-butan-2-ol while bottom attack yields (S)-butan-2-ol in equal amounts [1]<br/>"
         "• The resulting product is an equimolar racemic mixture; the equal and opposite rotations cancel out completely, producing no optical activity [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• CH3CH2CHO + HCN --> CH3CH2CH(OH)CN [2].<br/><br/>"
         "<b>(b)(ii) [4 Marks]</b><br/>"
         "• Attacking nucleophile: Cyanide ion, :CN- (with lone pair on carbon) [1]<br/>"
         "• Curly arrow from lone pair on carbon of CN- to carbonyl carbon Cδ+ of propanal [1]<br/>"
         "• Curly arrow from C=O bond to oxygen atom, forming alkoxide intermediate [1]<br/>"
         "• Intermediate CH3CH2CH(O-)CN protonated by HCN (or H+), regenerating CN- catalyst [1].<br/><br/>"
         "<b>(b)(iii) [3 Marks]</b><br/>"
         "• Carbonyl group of propanal is planar [1]<br/>"
         "• Attack by CN- from both faces is equally likely, generating a 50:50 racemic mixture of enantiomers [1]<br/>"
         "• The racemate shows zero net rotation of plane-polarised light (optically inactive) [1].<br/><br/>"
         "<b>(c) [2 Marks]</b><br/>"
         "• (R)-2-methylbutanal already possesses a chiral centre adjacent to the carbonyl group [1]<br/>"
         "• The bulky asymmetric alkyl substituent creates steric hindrance that blocks one face more than the other, causing attack to occur preferentially from the less hindered face to form diastereomers in unequal amounts [1]."),

        ("Question 35: Experimental Characterisation (* Level of Response) (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Butanal (CH3CH2CH2CHO) and butanone (CH3COCH2CH3) [2].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Reagent: Tollens' reagent (ammoniacal silver nitrate) warmed in water bath [1]<br/>"
         "• Butanal: Silver mirror deposited on test tube wall [1]<br/>"
         "• Butanone: No change / solution remains colourless [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive, logically structured experimental procedure. Diagnostic test: warm sample Q with Tollens' reagent in 60 °C water bath; silver mirror confirms butanal, no mirror confirms butanone. Reduction step: dissolve Q in ethanol, add NaBH4 portionwise with stirring and cooling in an ice bath to control the mild exotherm. Separation & purification: add dilute HCl to hydrolyse borate esters, extract alcohol with ethoxyethane using a separating funnel; wash organic layer with brine, dry over anhydrous MgSO4, filter, and purify by fractional distillation (collecting distillate at the alcohol's boiling point: butan-1-ol at 117 °C or butan-2-ol at 99 °C). Polarimetry test: place pure alcohol in polarimeter tube, measure optical rotation; both butan-1-ol (achiral) and butan-2-ol (racemate) show 0° rotation. Hazards & safety: Tollens' residues acidified with dilute HNO3 before disposal to prevent explosive fulminates; ethoxyethane is highly flammable (no naked flames, use electric heating mantle).<br/>"
         "• Level 2 (3-4 marks): Logical plan describing Tollens' test, NaBH4 reduction, distillation, and polarimeter test, but with minor omissions in purification or safety details.<br/>"
         "• Level 1 (1-2 marks): Basic list of reagents with incomplete purification or safety steps.<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• Carbonyl peak at 1740–1690 cm^-1 (sharp, strong C=O stretch) disappears completely [2].<br/><br/>"
         "<b>(c)(ii) [2 Marks]</b><br/>"
         "• Alcohol O-H stretch appears in the region 3750–3200 cm^-1 [1]<br/>"
         "• Appearance: broad, intense absorption band due to hydrogen bonding [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Electronic effect: Ketones have two electron-releasing alkyl groups (+I effect), which donate electron density to the carbonyl carbon, reducing its partial positive charge (Cδ+) and making it less attractive to nucleophiles compared to aldehydes which have only one alkyl group [2]<br/>"
         "• Steric effect: Ketones have two bulky alkyl groups attached to the carbonyl carbon, which crowd the reaction centre and hinder the approach of the incoming nucleophile [1]."),

        ("Question 36: Pharmaceutical Chirality (15 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Skeletal structure of ibuprofen drawn correctly with benzene ring, isobutyl group at position 4, and -CH(CH3)COOH at position 1 [1]<br/>"
         "• Asterisk (*) correctly placed on CH(CH3)COOH chiral carbon [1]<br/>"
         "• 3D representations of both enantiomers shown with wedge and dash bonds [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• The human liver contains an isomerase enzyme (alpha-methylacyl-CoA racemase) that rapidly converts inactive (R)-ibuprofen into active (S)-ibuprofen in vivo [1]<br/>"
         "• Over 60% of the inactive (R)-enantiomer is bio-inverted to the therapeutic (S)-form in the body [1]<br/>"
         "• Producing a single enantiomer requires expensive asymmetric catalysts or resolution processes, which are not economically justifiable when the body naturally activates the racemate [1].<br/><br/>"
         "<b>(b) [4 Marks]</b><br/>"
         "• Thalidomide possesses an acidic proton at the chiral centre [1]<br/>"
         "• At physiological pH (7.40), the molecule undergoes base-catalysed keto-enol tautomerism / deprotonation [1]<br/>"
         "• Deprotonation forms an achiral planar enol intermediate that is reprotonated equally from both sides [1]<br/>"
         "• Thus pure (R)-thalidomide rapidly racemises in the bloodstream into an equimolar mixture of (R) and (S) within 4 to 5 hours, generating the teratogenic (S)-form inside the patient [1].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• A chemical synthesis that produces predominantly or exclusively a single optical enantiomer of a chiral product [2].<br/><br/>"
         "<b>(c)(ii) [3 Marks]</b><br/>"
         "• 100% atom economy with respect to the desired enantiomer (no 50% waste of the unwanted isomer) [1]<br/>"
         "• Eliminates expensive and solvent-intensive chiral separation/resolution steps (TLC, chiral HPLC, fractional crystallisation) [1]<br/>"
         "• Lower dosage required, reducing risk of toxic side-effects and environmental pharmaceutical contamination [1]."),

        ("Question 37: Formaldehyde & Bio-Vanillin Purity (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• CH3OH + 1/2 O2 --> HCHO + H2O (or 2CH3OH + O2 --> 2HCHO + 2H2O) [2].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Formaldehyde has two small hydrogen atoms attached to C=O (no electron-donating alkyl groups), making the carbonyl carbon extremely electrophilic (large Cδ+) [1]<br/>"
         "• The small H atoms exert negligible steric hindrance, allowing water molecules to attack the carbonyl carbon unhindered [1]<br/>"
         "• Propanone has two bulky, electron-donating methyl groups (+I effect) that reduce the electrophilicity of Cδ+ and sterically shield the carbonyl carbon from attack by water [1]<br/>"
         "• Converting planar C=O (120°) to tetrahedral C(OH)2 (109.5°) increases steric crowding in propanone, making hydration thermodynamically unfavourable [1].<br/><br/>"
         "<b>(b)(i) [2 Marks]</b><br/>"
         "• Reagents: Sodium tetrahydridoborate(III), NaBH4, in aqueous ethanol (or LiAlH4 in dry ether followed by dilute acid) [2].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• Moles of metallic silver collected = 2.050 g / 107.9 g mol^-1 = 0.018999 mol Ag [1]<br/>"
         "• Stoichiometry: 1 mole vanillin reduces 2 moles Ag+ => Moles vanillin = 0.018999 / 2 = 9.4995 x 10^-3 mol [1]<br/>"
         "• Mr of vanillin (C8H8O3) = (8x12.0) + (8x1.0) + (3x16.0) = 96.0 + 8.0 + 48.0 = 152.0 g mol^-1 [1]<br/>"
         "• Mass of pure vanillin in sample = (9.4995 x 10^-3 mol) x 152.0 g mol^-1 = 1.4439 g [1]<br/>"
         "• Percentage purity = (1.4439 g / 1.522 g) x 100% = 94.87% ≈ 94.9% [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• Spot the reaction mixture alongside a reference sample of pure vanillin on a TLC plate [1]<br/>"
         "• Complete reaction is confirmed when the spot corresponding to vanillin (with higher Rf) has completely disappeared under UV light, leaving only the more polar vanillyl alcohol spot [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 11 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
