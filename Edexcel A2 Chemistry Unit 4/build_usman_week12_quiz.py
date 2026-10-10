"""
build_usman_week12_quiz.py
Mentora Academy — Pearson Edexcel International Advanced Level Chemistry
Unit 4: Rates, Equilibria and Further Organic Chemistry (WCH14/01)
WEEK 12 ADVANCED MASTERY & A* SCHOLAR CHALLENGE ASSESSMENT (150 MARKS)

Candidate: USMAN (Grade A* Scholar)
Topic Focus:
  - 15C: Carboxylic Acids (Dimerisation, Physical Properties, Reactions with PCl5, Carbonates, Alcohols)
  - 15D: Carboxylic Acid Derivatives (Acyl Chlorides Addition-Elimination, Esters, Saponification, Biodiesel, Polyesters)
  - 15E: Spectroscopy & Chromatography (TLC, GC-MS, 13C NMR Decoupling, High-Res 1H NMR, n+1 Rule, D2O Shake)
  - CORE SYLLABUS COMPLETION ASSESSMENT!

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
    "Usman_Edexcel_Chem_U4_Week12_150M_Challenging_Quiz.pdf"
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
    """Draws an authentic bordered box for organic reaction mechanisms and spectral structures."""
    def __init__(self, width=AVAIL_W, height=6.0*cm, caption="Space for structural drawings, mechanism, or NMR splitting trees"):
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
    canvas.drawString(L_MARGIN, 0.85 * cm, "Mentora Academy  |  Candidate: USMAN (Grade A* Scholar)  |  Week 12 Assessment")

    canvas.setFont(FONT['Bold'], 8)
    canvas.drawRightString(PAGE_W - R_MARGIN, 0.85 * cm, f"{doc.page}")

    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# MAIN DOCUMENT BUILDER
# ──────────────────────────────────────────────────────────────
def build_pdf():
    print("[1/2] Building authentic Edexcel past-paper story for Week 12 (150 Marks)...")
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
         Paragraph("Mentora Academy Internal Candidate Ref:<br/><b>MEN-EDX-2026-U4-W12</b>", S['edx_meta_b'])]
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
    story.append(Paragraph("<b>WEEK 12 ASSESSMENT: CARBOXYLIC DERIVATIVES, POLYESTERS & SPECTROSCOPY — SYLLABUS COMPLETION</b>", S['edx_sub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=10, spaceBefore=4))

    # Paper Specs Table
    specs = [
        [Paragraph("<b>Assessment Paper:</b>", S['edx_meta']), Paragraph("WCH14/01 (Week 12 Core Syllabus Completion)", S['edx_meta_b'])],
        [Paragraph("<b>Time Allowed:</b>", S['edx_meta']), Paragraph("<b>2 hours 30 minutes</b>", S['edx_meta_b'])],
        [Paragraph("<b>Total Marks:</b>", S['edx_meta']), Paragraph("<b>150 Marks</b>", S['edx_meta_b'])],
        [Paragraph("<b>Topics Examined:</b>", S['edx_meta']), Paragraph("Topic 15C: Carboxylic Acids (Physical Properties, Dimerisation, Reactions with PCl5, Alcohols)<br/>Topic 15D: Carboxylic Derivatives (Acyl Chlorides Addition-Elimination, Esters, Saponification, Polyesters)<br/>Topic 15E: Spectroscopy & Chromatography (TLC, GC-MS, 13C NMR Decoupling, High-Res 1H NMR, n+1 Rule, D2O Shake)", S['edx_meta'])],
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
        ("Which reagent is used to convert ethanoic acid directly into ethanoyl chloride at room temperature?",
         [("A", "Phosphorus(V) chloride, PCl5"),
          ("B", "Dilute hydrochloric acid, HCl(aq)"),
          ("C", "Sodium chloride, NaCl"),
          ("D", "Chlorine gas in UV light, Cl2 / UV")]),

        ("What observation is made when water is added dropwise to pure ethanoyl chloride, CH3COCl?",
         [("A", "A white precipitate forms and the solution turns alkaline"),
          ("B", "A vigorous exothermic reaction producing dense steamy acidic fumes of HCl"),
          ("C", "Effervescence of carbon dioxide gas occurs"),
          ("D", "A sweet fruity odour is immediately produced")]),

        ("Ethanoyl chloride reacts with ethanol at room temperature. What are the products of this reaction?",
         [("A", "Ethyl ethanoate and water"),
          ("B", "Ethyl ethanoate and hydrogen chloride"),
          ("C", "Ethanoic acid and chloroethane"),
          ("D", "Diethyl ether and hydrogen chloride")]),

        # Page 3: Q4, Q5, Q6
        ("What is the organic product formed when benzoyl chloride, C6H5COCl, reacts with concentrated aqueous ammonia?",
         [("A", "Phenylamine, C6H5NH2"),
          ("B", "Benzamide, C6H5CONH2"),
          ("C", "Benzenecarboxylic acid, C6H5COOH"),
          ("D", "Benzylamine, C6H5CH2NH2")]),

        ("Why are acyl chlorides much more reactive towards nucleophiles than carboxylic acids?",
         [("A", "The chlorine atom has a larger atomic radius than oxygen"),
          ("B", "The carbonyl carbon is more electrophilic and chloride (Cl-) is a much better leaving group than hydroxide (OH-)"),
          ("C", "Acyl chlorides form strong intermolecular hydrogen bonds"),
          ("D", "Acyl chlorides are completely non-polar molecules")]),

        ("What type of reaction occurs when an ester is boiled under reflux with aqueous sodium hydroxide?",
         [("A", "Electrophilic substitution"),
          ("B", "Irreversible alkaline hydrolysis (saponification)"),
          ("C", "Reversible acid-catalysed condensation"),
          ("D", "Free-radical addition")]),

        # Page 4: Q7, Q8, Q9
        ("Biodiesel is manufactured industrially by transesterification. What is the chemical composition of biodiesel?",
         [("A", "A mixture of long-chain branched alkanes and alkenes"),
          ("B", "A mixture of methyl esters of long-chain fatty acids"),
          ("C", "Pure propane-1,2,3-triol (glycerol)"),
          ("D", "A condensation polymer of lactic acid")]),

        ("Why are polyesters like PET biodegradable in the environment, whereas polyalkenes like poly(ethene) are non-biodegradable?",
         [("A", "Polyesters have polar ester linkages that can be hydrolysed by water and microbial enzymes"),
          ("B", "Poly(ethene) is soluble in rainwater, whereas polyesters form dense insoluble crystalline sheets"),
          ("C", "Polyesters are formed by addition polymerisation"),
          ("D", "Polyalkenes contain unstable aromatic rings that prevent microbial digestion")]),

        ("Which pair of monomers undergoes condensation polymerisation to produce Terylene (PET)?",
         [("A", "Benzene-1,4-dicarboxylic acid and ethane-1,2-diol"),
          ("B", "Hexanedioic acid and hexane-1,6-diamine"),
          ("C", "Phenol and methanal"),
          ("D", "Propene and phenylethene")]),

        # Page 5: Q10, Q11, Q12
        ("In thin-layer chromatography (TLC) using a silica gel plate, why does a more polar compound have a lower Rf value than a less polar compound?",
         [("A", "The polar silica stationary phase forms stronger dipole-dipole attractions with the polar compound, retarding its movement"),
          ("B", "The polar compound evaporates more rapidly from the plate"),
          ("C", "The less polar compound dissolves into the silica gel crystals"),
          ("D", "The mobile phase is completely stationary for polar compounds")]),

        ("In a mass spectrum, what causes the small M+1 peak observed immediately to the right of the molecular ion peak M+?",
         [("A", "The presence of naturally occurring carbon-13 (^13C) atoms"),
          ("B", "Loss of a single proton from the molecular ion"),
          ("C", "Capture of an extra electron by the detector"),
          ("D", "The presence of deuterium (^2H) in the carrier gas")]),

        ("A haloalkane displays two molecular ion peaks in its mass spectrum at m/z = 156 and m/z = 158 in an approximate 1:1 intensity ratio. Which halogen atom is present?",
         [("A", "Fluorine (^19F)"),
          ("B", "Chlorine (^35Cl and ^37Cl)"),
          ("C", "Bromine (^79Br and ^81Br)"),
          ("D", "Iodine (^127I)")]),

        # Page 6: Q13, Q14, Q15
        ("In gas chromatography (GC), which two factors primarily determine the retention time of a compound in the capillary column?",
         [("A", "Boiling point (volatility) and relative solubility/affinity for the stationary liquid phase"),
          ("B", "The colour of the compound and its molar mass"),
          ("C", "The pH of the carrier gas and atmospheric pressure"),
          ("D", "The volume of sample injected and room humidity")]),

        ("Why is tetramethylsilane, Si(CH3)4 (TMS), universally used as the reference standard in NMR spectroscopy?",
         [("A", "It gives a single sharp singlet at 0.0 ppm, is chemically inert, non-toxic, and volatile (bp 27 °C)"),
          ("B", "It reacts reversibly with all organic functional groups"),
          ("C", "It absorbs in the ultraviolet-visible region"),
          ("D", "It acts as a deuterated solvent that dissolves ionic salts")]),

        ("Why is deuterated trichloromethane, CDCl3, used as a solvent in 1H NMR spectroscopy instead of regular CHCl3?",
         [("A", "Deuterium (^2H) has an even mass number and does not produce a signal in the 1H NMR frequency range"),
          ("B", "Deuterium increases the sensitivity of the radiofrequency pulse by a factor of 10"),
          ("C", "Regular CHCl3 is an explosive liquid at room temperature"),
          ("D", "CDCl3 shifts all sample peaks downfield by exactly 5.0 ppm")]),

        # Page 7: Q16, Q17, Q18
        ("How many peaks are observed in the broad-band decoupled 13C NMR spectrum of propan-2-ol, (CH3)2CHOH?",
         [("A", "1"),
          ("B", "2 (one for the two equivalent methyl carbons, one for CH-OH)"),
          ("C", "3"),
          ("D", "4")]),

        ("How many distinct carbon environments are present in methyl propanoate, CH3CH2COOCH3?",
         [("A", "2"),
          ("B", "3"),
          ("C", "4"),
          ("D", "5")]),

        ("In the high-resolution 1H NMR spectrum of propanal, CH3CH2CHO, what is the splitting pattern of the methyl (CH3) protons?",
         [("A", "Singlet"),
          ("B", "Doublet"),
          ("C", "Triplet (split by the two adjacent CH2 protons)"),
          ("D", "Quartet")]),

        # Page 8: Q19, Q20, Q21
        ("In the 1H NMR spectrum of ethyl ethanoate, CH3COOCH2CH3, what is the splitting pattern of the -CH2- protons?",
         [("A", "Singlet"),
          ("B", "Doublet"),
          ("C", "Triplet"),
          ("D", "Quartet (split by the three adjacent CH3 protons)")]),

        ("What happens to the broad O-H proton peak in an alcohol's 1H NMR spectrum when a drop of D2O is added and the tube is shaken (the D2O shake test)?",
         [("A", "The peak splits into a doublet"),
          ("B", "The peak shifts downfield to 12.0 ppm"),
          ("C", "The peak completely disappears due to rapid exchange: R-OH + D2O <==> R-OD + HOD"),
          ("D", "The peak area doubles in size")]),

        ("In a 1H NMR spectrum, what fundamental information is provided by the integration trace (area under each peak)?",
         [("A", "The coupling constant J between interacting nuclei"),
          ("B", "The relative ratio of hydrogen atoms in each chemical environment"),
          ("C", "The exact molar mass of the compound"),
          ("D", "The percentage purity of the solvent")]),

        # Page 9: Q22, Q23, Q24
        ("Which compound displays only TWO singlets with relative peak areas 9 : 3 in its 1H NMR spectrum?",
         [("A", "Methyl 2,2-dimethylpropanoate, (CH3)3CCOOCH3"),
          ("B", "Ethyl ethanoate, CH3COOCH2CH3"),
          ("C", "Diethyl ether, CH3CH2OCH2CH3"),
          ("D", "Pentan-3-one, CH3CH2COCH2CH3")]),

        ("What is the splitting pattern of the non-equivalent protons in 1,2-dichloroethane, Cl-CH2-CH2-Cl?",
         [("A", "A single sharp singlet (all 4 protons are chemically and magnetically equivalent)"),
          ("B", "Two doublets"),
          ("C", "A triplet and a quartet"),
          ("D", "A multiplet with 5 sub-peaks")]),

        ("In the mass spectrum of propanone, CH3COCH3, what is the m/z value of the base peak formed by alpha-cleavage?",
         [("A", "15 ([CH3]+)"),
          ("B", "29 ([CHO]+)"),
          ("C", "43 ([CH3CO]+, the stable acylium ion)"),
          ("D", "58 ([M]+)")]),

        # Page 10: Q25, Q26, Q27
        ("A colourless liquid reacts vigorously with water to produce steamy fumes of HCl and shows only TWO peaks in its 13C NMR spectrum. What is the compound?",
         [("A", "Chloroethane, CH3CH2Cl"),
          ("B", "Ethanoyl chloride, CH3COCl"),
          ("C", "Propanoyl chloride, CH3CH2COCl"),
          ("D", "Dichloroethanoic acid, CHCl2COOH")]),

        ("An unknown ester has molecular formula C5H10O2. Its 1H NMR spectrum shows a singlet at δ = 8.0 ppm (1H) and a singlet at δ = 1.4 ppm (9H). What is the ester?",
         [("A", "Methyl butanoate"),
          ("B", "tert-butyl methanoate, HCOOC(CH3)3"),
          ("C", "Ethyl propanoate"),
          ("D", "Propyl ethanoate")]),

        ("Why is High Performance Liquid Chromatography (HPLC) preferred over Gas Chromatography (GC) for the separation of non-volatile pharmaceuticals such as penicillin?",
         [("A", "GC operates at high temperatures that would thermally decompose heat-labile molecules"),
          ("B", "HPLC uses radioactive carrier gases that increase detection limits"),
          ("C", "Penicillin is a gas at room temperature"),
          ("D", "GC columns cannot separate molecules containing nitrogen")]),

        # Page 11: Q28, Q29, Q30
        ("How many non-equivalent proton environments are present in butanone, CH3COCH2CH3?",
         [("A", "2"),
          ("B", "3 (CH3-CO, -CH2-, and -CH3)"),
          ("C", "4"),
          ("D", "8")]),

        ("In mass spectrometry, what common structural feature is indicated by a prominent fragment ion peak at m/z = 77?",
         [("A", "An ethyl ester group"),
          ("B", "A phenyl ring cation, [C6H5]+"),
          ("C", "A chlorine atom"),
          ("D", "A carboxylic acid dimer")]),

        ("What is the systematic IUPAC name of the repeat unit of the polyester formed from ethane-1,2-diol and butanedioic acid?",
         [("A", "-[O-CH2-CH2-O-CO-(CH2)2-CO]-"),
          ("B", "-[O-CH2-CO-O-CH2-CH2]-"),
          ("C", "-[CH2-CH2-CO-O-CH2]-"),
          ("D", "-[CO-C6H4-CO-O-CH2-CH2-O]-")])
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
    # QUESTION 31 (18 MARKS) — ACYL CHLORIDES: MECHANISM & REACTIVITY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>31</b>&nbsp;&nbsp;Acyl chlorides are versatile organic intermediates that react vigorously with nucleophiles via nucleophilic addition-elimination.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Ethanoyl chloride, CH<sub>3</sub>COCl, reacts vigorously at room temperature with ethanol and with concentrated aqueous ammonia.<br/>"
                           "Write balanced chemical equations for both reactions, state the systematic name of the organic product formed in each case, and describe what is observed.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Compare the reaction of ethanol with ethanoyl chloride to the reaction of ethanol with ethanoic acid.<br/>"
                           "Contrast the two reactions with respect to: rate, reversibility / equilibrium yield, necessity of an acid catalyst, and the nature of the inorganic byproduct.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>31 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;(i)&nbsp;&nbsp;Draw the complete mechanism for the hydrolysis of ethanoyl chloride, CH<sub>3</sub>COCl, with water.<br/>"
                           "Include all partial charges (dipoles), lone pairs of electrons, curly arrows showing the formation of the tetrahedral intermediate, the elimination of the chloride ion, and loss of the proton.", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=6.5*cm, caption="Space for nucleophilic addition-elimination mechanism: ethanoyl chloride + water"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Chlorobenzene, C<sub>6</sub>H<sub>5</sub>Cl, is completely resistant to nucleophilic attack by water at room temperature, whereas ethanoyl chloride hydrolyses violently.<br/>"
                           "Explain this immense difference in reactivity by considering:<br/>"
                           "- The delocalisation of chlorine lone-pair electrons into the aromatic pi system in chlorobenzene.<br/>"
                           "- The electrophilicity of the carbonyl carbon in ethanoyl chloride.<br/>"
                           "- The relative leaving-group abilities of the chlorine atoms in both compounds.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(31, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 32 (18 MARKS) — ESTERS, SAPONIFICATION, BIODIESEL & POLYESTERS
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>32</b>&nbsp;&nbsp;Esters and polyesters are widely used in flavourings, biofuels, and synthetic fibres.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Ethyl propanoate, CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub>, can be hydrolysed using dilute acid or dilute alkali.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical equation for the acid-catalysed hydrolysis of ethyl propanoate using dilute sulfuric acid. Explain why this reaction does NOT go to completion.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Write the chemical equation for the alkaline hydrolysis of ethyl propanoate with aqueous sodium hydroxide. Explain why alkaline hydrolysis (saponification) goes to 100% completion.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>32 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Biodiesel is manufactured industrially from vegetable oil triglycerides.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write a general equation showing the transesterification of a triglyceride (glyceryl triester) with methanol in the presence of an alkali catalyst, showing the structures of propane-1,2,3-triol (glycerol) and the fatty acid methyl ester (biodiesel).", S['q_subpart']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(DiagramBox(width=AVAIL_W, height=5.5*cm, caption="Space for transesterification reaction scheme: triglyceride + 3CH3OH --> glycerol + 3RCOOCH3"))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;State two major environmental advantages of using biodiesel over fossil-derived petrodiesel.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Condensation polymers contain repeating functional linkages.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Poly(lactic acid) (PLA) is manufactured from 2-hydroxypropanoic acid, CH<sub>3</sub>CH(OH)COOH. Draw the structure of two repeat units of PLA.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Terylene (PET) is synthesized from benzene-1,4-dicarboxylic acid and ethane-1,2-diol. Draw the repeat unit of PET.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Explain why polyesters like PLA and PET are biodegradable, whereas addition polymers like poly(ethene) persist in landfill for hundreds of years.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(32, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 33 (18 MARKS) — HIGH-RESOLUTION 1H NMR & SPIN-SPIN COUPLING
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>33</b>&nbsp;&nbsp;High-resolution 1H NMR spectroscopy provides detailed structural information via chemical shift, peak integration, and spin-spin splitting.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Explain the physical cause of spin-spin coupling in high-resolution 1H NMR, and state the <i>n + 1</i> rule for splitting by <i>n</i> adjacent non-equivalent protons.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Compound <b>W</b> is an ester with molecular formula C<sub>4</sub>H<sub>8</sub>O<sub>2</sub>. Its 1H NMR spectrum displays three signals:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal 1:</b> &delta; = 1.25 ppm, triplet, relative area = 3<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal 2:</b> &delta; = 2.05 ppm, singlet, relative area = 3<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal 3:</b> &delta; = 4.12 ppm, quartet, relative area = 2", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Deduce the structural fragment responsible for each of the three signals. For each signal, fully justify:<br/>"
                           "- The chemical shift (&delta; value).<br/>"
                           "- The splitting pattern using the <i>n + 1</i> rule.<br/>"
                           "- The relative integration area.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(7))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Deduce the complete displayed formula of compound <b>W</b> and give its systematic IUPAC name.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(2))
    story.append(Paragraph("Answer: Name = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>33 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;An isomeric ester, <b>X</b>, also has molecular formula C<sub>4</sub>H<sub>8</sub>O<sub>2</sub>. Its 1H NMR spectrum shows:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal A:</b> &delta; = 1.15 ppm, triplet, relative area = 3<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal B:</b> &delta; = 2.35 ppm, quartet, relative area = 2<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Signal C:</b> &delta; = 3.65 ppm, singlet, relative area = 3<br/>"
                           "Deduce the structure of ester <b>X</b>, explain how its chemical shifts distinguish it from compound <b>W</b>, and give its systematic IUPAC name.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Name of X = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;Explain what happens when a drop of deuterium oxide, D<sub>2</sub>O, is added to an NMR sample tube containing an unknown carboxylic acid or alcohol prior to recording the spectrum (the D<sub>2</sub>O shake test).<br/>"
                           "Write a chemical equation for the proton-deuterium exchange reaction and explain why the labial peak disappears from the 1H spectrum.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(33, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 34 (18 MARKS) — 13C NMR & GC-MS SPECTROMETRY
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>34</b>&nbsp;&nbsp;Carbon-13 NMR spectroscopy and gas chromatography-mass spectrometry (GC-MS) provide complementary analytical data.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Explain why carbon-13 NMR spectra are recorded with broad-band proton decoupling, and state why 13C NMR signals do not show splitting.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Predict the exact number of peaks that will appear in the broad-band decoupled 13C NMR spectra of the following three isomeric alcohols of formula C<sub>4</sub>H<sub>10</sub>O:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Isomer 1:</b> Butan-1-ol<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Isomer 2:</b> Butan-2-ol<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Isomer 3:</b> 2-methylpropan-2-ol<br/>"
                           "Explain how 13C NMR spectroscopy allows a chemist to distinguish unambiguously between these three isomers without recording 1H NMR spectra.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>34 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Gas Chromatography - Mass Spectrometry (GC-MS) is an indispensable analytical technique in forensic toxicology and environmental monitoring.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Describe the operation of a hyphenated GC-MS instrument, clearly explaining the specific role of the gas chromatography capillary column and the role of the mass spectrometer detector.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;A sample of an unknown solvent was analysed by GC-MS. The mass spectrum of the primary component exhibits:<br/>"
                           "- Molecular ion peak at m/z = 88 [M]+<br/>"
                           "- Fragment ion peaks at m/z = 73, 59, 43 (base peak, 100% abundance), and 29.<br/>"
                           "Identify the compound (molecular formula C<sub>4</sub>H<sub>8</sub>O<sub>2</sub>) and write the formulae of the positively charged fragment ions responsible for each of the peaks at m/z = 73, 59, 43, and 29.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(6))
    story.append(Paragraph("Answer: Identity = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(5)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(iii)&nbsp;&nbsp;Explain why GC-MS is preferred over gas chromatography alone (with flame ionisation detection) in sports anti-doping testing.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(34, 18))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 35 (18 MARKS) — MULTI-SPECTRAL ELUCIDATION (* LEVEL OF RESPONSE)
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>*35</b>&nbsp;&nbsp;An unknown volatile organic compound, <b>Y</b>, has an empirical formula of C<sub>2</sub>H<sub>4</sub>O and was subjected to multiple spectroscopic techniques.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;The mass spectrum of <b>Y</b> displays a molecular ion peak [M]+ at m/z = 88.0 and an [M+1]+ peak at m/z = 89.0 with relative peak heights of 100% and 4.4% respectively.<br/>"
                           "The infrared spectrum shows a sharp, strong absorption band at 1740 cm^-1, but no absorption in the ranges 3200–3600 cm^-1 or 2500–3300 cm^-1.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Calculate the number of carbon atoms in a molecule of <b>Y</b> using the relative heights of the [M]+ and [M+1]+ peaks, and deduce the molecular formula of <b>Y</b>.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Molecular formula = .....................................................", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Using the infrared data, deduce the functional group present in <b>Y</b> and state two functional groups that are definitely absent.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("*(b)&nbsp;&nbsp;The chemist synthesises pure compound <b>Y</b> (ethyl ethanoate) in the laboratory starting from ethanoyl chloride and ethanol.<br/>"
                           "Describe a full experimental protocol to:<br/>"
                           "- React pure anhydrous ethanol with ethanoyl chloride safely in a fume cupboard.<br/>"
                           "- Wash and isolate the crude ester using a separating funnel with aqueous sodium hydrogencarbonate (to remove acidic HCl byproduct) and saturated brine.<br/>"
                           "- Dry the organic layer using anhydrous magnesium sulfate or anhydrous calcium chloride.<br/>"
                           "- Purify the dry ester by simple distillation, specifying the collection temperature range (bp 77 °C).<br/>"
                           "- State two major safety hazards associated with ethanoyl chloride and ethoxyethane/ester and explain how risk is minimized.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(11))
    story.append(Paragraph("<b>(6)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>*35 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;In the mass spectrum of ethyl ethanoate, <b>Y</b>, the base peak occurs at m/z = 43.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical formula and draw the structure of the resonance-stabilised acylium ion responsible for the m/z = 43 peak.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Write a fragmentation equation showing how the molecular ion [CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>]+ forms the base peak ion at m/z = 43 by loss of a radical.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(d)&nbsp;&nbsp;High-Performance Liquid Chromatography (HPLC) is often chosen over GC for analyzing pharmaceuticals.<br/>"
                           "Explain why HPLC is suitable for thermally unstable biomolecules like penicillin or insulin, and describe how a reverse-phase HPLC column separates polar and non-polar compounds.", S['q_subpart']))
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
    # QUESTION 36 (15 MARKS) — SUSTAINABLE POLYMERS: BIO-PET & PLA RECYCLING
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>36</b>&nbsp;&nbsp;<b>Sustainable Materials and Circular Plastics:</b><br/>"
                           "Global annual production of poly(ethylene terephthalate) (PET) exceeds 80 million tonnes. PET is synthesized from benzene-1,4-dicarboxylic acid (terephthalic acid, PTA, C<sub>8</sub>H<sub>6</sub>O<sub>4</sub>) and ethane-1,2-diol (ethylene glycol, EG, C<sub>2</sub>H<sub>6</sub>O<sub>2</sub>). Chemical recycling via glycolysis breaks down PET back into monomers.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;(i)&nbsp;&nbsp;Write the chemical equation for the condensation polymerisation of benzene-1,4-dicarboxylic acid with ethane-1,2-diol. Draw the displayed formula of two repeat units of PET and state the small molecule eliminated.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;In 'Bio-PET', the ethane-1,2-diol monomer is synthesized from renewable sugarcane bio-ethanol, whereas terephthalic acid is derived from petroleum. Calculate the percentage of the carbon atoms in Bio-PET that originate from renewable biological sources.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("Answer: Renewable Carbon Percentage = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>36 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;In industrial glycolysis recycling, waste PET flakes are heated with excess ethane-1,2-diol at 200 °C in the presence of a zinc acetate catalyst.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write an equation for the glycolysis of a PET repeat unit, -[CO-C<sub>6</sub>H<sub>4</sub>-CO-O-CH<sub>2</sub>CH<sub>2</sub>-O]-, with ethane-1,2-diol to form bis(2-hydroxyethyl) terephthalate (BHET).", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain two key thermodynamic and environmental advantages of chemical glycolysis recycling over mechanical melting and remoulding of waste plastics.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;Poly(lactic acid) (PLA) breaks down rapidly in industrial composting facilities at 60 °C and high humidity within 90 days.<br/>"
                           "Using collision theory and ester bond polarity, explain why alkaline composting accelerates the rate of PLA hydrolysis compared to ambient neutral soil.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(question_total(36, 15))
    story.append(PageBreak())

    # ──────────────────────────────────────────────────────────
    # QUESTION 37 (15 MARKS) — PHARMACEUTICAL SYNTHESIS: PARACETAMOL & ASPIRIN
    # ──────────────────────────────────────────────────────────
    story.append(Paragraph("<b>37</b>&nbsp;&nbsp;<b>Pharmaceutical Synthesis and Quality Assurance:</b><br/>"
                           "Paracetamol (N-(4-hydroxyphenyl)ethanamide, C<sub>8</sub>H<sub>9</sub>NO<sub>2</sub>, Mr = 151.16) and Aspirin (2-ethanoyloxybenzoic acid, C<sub>9</sub>H<sub>8</sub>O<sub>4</sub>, Mr = 180.16) are among the most widely manufactured analgesic medicines in the world.", S['q_stem']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(a)&nbsp;&nbsp;Paracetamol is manufactured by reacting 4-aminophenol with ethanoic anhydride, (CH<sub>3</sub>CO)<sub>2</sub>O.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;Write the chemical equation for the synthesis of paracetamol from 4-aminophenol and ethanoic anhydride.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(3))
    story.append(Paragraph("<b>(2)</b>", S['q_submark']))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;Explain why ethanoic anhydride is preferred in industrial pharmaceutical production over ethanoyl chloride, considering safety hazards, rate of reaction, and the nature of the byproduct.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(PageBreak())

    story.append(Paragraph("<b>37 (continued)</b>", S['q_stem']))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("(b)&nbsp;&nbsp;Aspirin is synthesized by the reaction of 2-hydroxybenzoic acid (salicylic acid, Mr = 138.12) with excess ethanoic anhydride.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(Paragraph("(i)&nbsp;&nbsp;A student reacts 13.81 g of 2-hydroxybenzoic acid with excess ethanoic anhydride in the presence of 5 drops of concentrated phosphoric acid. After recrystallisation from water, 14.41 g of pure dry aspirin is obtained. Calculate the percentage yield of aspirin.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(5))
    story.append(Paragraph("Answer: Percentage Yield = ..................................................... %", S['ans_prompt']))
    story.append(Paragraph("<b>(4)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(ii)&nbsp;&nbsp;The student tests the recrystallised aspirin product with neutral iron(III) chloride solution, FeCl<sub>3</sub>(aq). Unreacted salicylic acid produces a deep purple colouration, whereas pure aspirin produces no colour change.<br/>"
                           "Explain the chemical basis of this test by referring to functional groups present in salicylic acid and aspirin.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
    story.append(Paragraph("<b>(3)</b>", S['q_submark']))
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("(c)&nbsp;&nbsp;In the electron-ionisation mass spectrum of aspirin (Mr = 180.16), prominent fragment ion peaks are observed at m/z = 138 and m/z = 120.<br/>"
                           "Deduce the identity and draw the structures of the fragment ions responsible for each of these two peaks.", S['q_subpart']))
    story.append(Spacer(1, 0.1 * cm))
    story.append(DottedAnswerLines(4))
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
        [Paragraph("1H NMR: Carboxylic Acid O-H", S['tbl_td_l']), Paragraph("10.0 - 12.5 ppm", S['tbl_td']), Paragraph("R-COOH (broad singlet, D2O exchange)", S['tbl_td'])],
        [Paragraph("13C NMR: Alkyl C-C", S['tbl_td_l']), Paragraph("0 - 50 ppm", S['tbl_td']), Paragraph("Alkyl carbons (sp3)", S['tbl_td'])],
        [Paragraph("13C NMR: C-O Ether / Ester / Alcohol", S['tbl_td_l']), Paragraph("50 - 90 ppm", S['tbl_td']), Paragraph("Carbons bonded to oxygen", S['tbl_td'])],
        [Paragraph("13C NMR: C=O Ester / Acid", S['tbl_td_l']), Paragraph("160 - 185 ppm", S['tbl_td']), Paragraph("Carbonyl carbon in R-COOR / R-COOH", S['tbl_td'])],
        [Paragraph("Infrared C=O Stretch (Ester)", S['tbl_td_l']), Paragraph("1750 - 1735 cm^-1", S['tbl_td']), Paragraph("Sharp, intense absorption", S['tbl_td'])],
        [Paragraph("Infrared C-O Stretch (Ester)", S['tbl_td_l']), Paragraph("1300 - 1000 cm^-1", S['tbl_td']), Paragraph("Strong absorption band", S['tbl_td'])],
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
    story.append(Paragraph("<b>Pearson Edexcel International Advanced Level Chemistry — Unit 4 (WCH14/01) — Week 12 Assessment (150 Marks)</b>", S['sec_instr']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=CRIMSON, spaceAfter=8, spaceBefore=4))

    # Section A Mark Scheme Table
    ms_a = [
        [Paragraph("<b>Q</b>", S['tbl_th']), Paragraph("<b>Correct Answer</b>", S['tbl_th']), Paragraph("<b>Key Concept & Examiner Guidance</b>", S['tbl_th']), Paragraph("<b>Mark</b>", S['tbl_th'])],
        [Paragraph("<b>1</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("PCl5 converts carboxylic acids to acyl chlorides: RCOOH + PCl5 --> RCOCl + POCl3 + HCl.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>2</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Hydrolysis is violent and releases dense steamy fumes of hydrogen chloride gas.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>3</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Acyl chloride + alcohol --> ester + HCl: CH3COCl + C2H5OH --> CH3COOC2H5 + HCl.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>4</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Benzoyl chloride reacts with excess ammonia to form benzamide: C6H5COCl + 2NH3 --> C6H5CONH2 + NH4Cl.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>5</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Carbonyl carbon is highly delta-positive and chloride ion is a very stable leaving group.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>6</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Alkaline hydrolysis (saponification) converts ester to carboxylate salt and alcohol irreversibly.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>7</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Biodiesel is chemically composed of fatty acid methyl esters (FAME) from triglyceride transesterification.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>8</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Polar ester bonds are susceptible to nucleophilic attack by water/enzymes (hydrolysis).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>9</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("PET is synthesized from benzene-1,4-dicarboxylic acid (terephthalic acid) and ethane-1,2-diol.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>10</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Silica gel is polar; polar solutes bind strongly via dipole-dipole forces, retarding travel (low Rf).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>11</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Carbon-13 has a natural abundance of ~1.1%, giving an M+1 peak proportional to carbon count.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>12</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Bromine exists as ^79Br and ^81Br in approximately equal abundance (1:1), giving twin M/M+2 peaks.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>13</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Retention time depends on volatility (boiling point) and affinity/partitioning with stationary liquid phase.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>14</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("TMS is inert, volatile (bp 27 °C), and its 12 equivalent protons absorb far upfield at 0.0 ppm.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>15</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Deuterium has a different nuclear spin frequency, producing zero signal in the 1H NMR region.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>16</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("(CH3)2CHOH has two equivalent methyl carbons (peak 1) and one CH-OH carbon (peak 2).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>17</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Methyl propanoate: CH3-CH2-COO-CH3 has 4 unique carbon environments (4 peaks).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>18</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("CH3 group is adjacent to CH2 (2 protons), splitting into 2 + 1 = 3 peaks (triplet).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>19</b>", S['tbl_td']), Paragraph("<b>D</b>", S['tbl_td']), Paragraph("-O-CH2- protons are adjacent to CH3 (3 protons), splitting into 3 + 1 = 4 peaks (quartet).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>20</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Deuterium exchange: R-OH + D2O <=> R-OD + HOD replaces 1H with 2H, eliminating the peak.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>21</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Integration area is directly proportional to the relative number of protons in that environment.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>22</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Methyl 2,2-dimethylpropanoate has a tert-butyl group (9H singlet) and a methoxy group (3H singlet).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>23</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("In 1,2-dichloroethane, all 4 protons are chemically and structurally equivalent, giving a singlet.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>24</b>", S['tbl_td']), Paragraph("<b>C</b>", S['tbl_td']), Paragraph("Alpha-cleavage of propanone produces the resonance-stabilised acylium ion [CH3CO]+ at m/z = 43.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>25</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Ethanoyl chloride has 2 carbons (CH3 and C=O), giving exactly two 13C peaks.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>26</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("tert-butyl methanoate: HCOOC(CH3)3 has formate H (1H singlet) and 9 equivalent tert-butyl protons (9H singlet).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>27</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("GC requires heating sample into gas phase, which thermally destroys fragile biomolecules like penicillin.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>28</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("Butanone (CH3-CO-CH2-CH3) has 3 distinct proton environments: 3H singlet, 2H quartet, 3H triplet.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>29</b>", S['tbl_td']), Paragraph("<b>B</b>", S['tbl_td']), Paragraph("m/z = 77 corresponds to the phenyl carbocation [C6H5]+ (12x6 + 5 = 77).", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
        [Paragraph("<b>30</b>", S['tbl_td']), Paragraph("<b>A</b>", S['tbl_td']), Paragraph("Diol (-O-CH2-CH2-O-) and dicarboxylic acid (-CO-(CH2)2-CO-) condense to form the ester repeat unit.", S['tbl_td_l']), Paragraph("1", S['tbl_td'])],
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
        ("Question 31: Acyl Chlorides Addition-Elimination (18 Marks)",
         "<b>(a)(i) [4 Marks]</b><br/>"
         "• Equation 1: CH3COCl + C2H5OH --> CH3COOC2H5 + HCl [1]. Product: Ethyl ethanoate; steamy acidic fumes of HCl [1]<br/>"
         "• Equation 2: CH3COCl + 2NH3 --> CH3CONH2 + NH4Cl [1]. Product: Ethanamide; white smoke / solid ammonium chloride [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• Rate: Acyl chloride reaction is rapid and violent at room temperature; carboxylic acid reaction is very slow and requires prolonged heating under reflux [1]<br/>"
         "• Equilibrium: Acyl chloride reaction is irreversible and goes to 100% completion; carboxylic acid esterification is reversible and achieves an equilibrium yield of only ~67% [1]<br/>"
         "• Catalyst: Acyl chloride requires no catalyst; carboxylic acid requires concentrated H2SO4 catalyst [1]<br/>"
         "• Byproduct: Acyl chloride produces HCl(g); carboxylic acid produces H2O [1].<br/><br/>"
         "<b>(b)(i) [5 Marks]</b><br/>"
         "• Dipoles shown correctly on C=O (Cδ+, Oδ-) and lone pair on oxygen of water [1]<br/>"
         "• Curly arrow from lone pair on water oxygen to carbonyl carbon [1]<br/>"
         "• Curly arrow from C=O bond to oxygen, forming tetrahedral intermediate: CH3-C(O-)(Cl)-OH2+ [1]<br/>"
         "• Curly arrow from O- lone pair reforming C=O double bond AND curly arrow expelling Cl- [1]<br/>"
         "• Curly arrow from O-H bond of protonated acid to oxygen / Cl- removing H+, giving CH3COOH and HCl [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• In chlorobenzene, a lone pair of electrons on the chlorine atom overlaps with the delocalised pi system of the benzene ring [1]<br/>"
         "• This delocalisation gives the C-Cl bond partial double bond character, making it significantly stronger and shorter, resisting cleavage [1]<br/>"
         "• In ethanoyl chloride, the carbonyl oxygen withdraws electron density, creating a strongly electrophilic carbon (Cδ+) that attracts nucleophiles [1]<br/>"
         "• The tetrahedral intermediate in acyl chloride addition-elimination expels chloride readily as a stable, weak conjugate base leaving group [1]<br/>"
         "• In chlorobenzene, backside nucleophilic attack is blocked by the high electron density of the aromatic pi cloud, preventing substitution [1]."),

        ("Question 32: Esters, Saponification, Biodiesel & Polyesters (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• CH3CH2COOCH2CH3 + H2O <=> CH3CH2COOH + CH3CH2OH [1]<br/>"
         "• Reversible equilibrium where the reverse esterification reaction occurs at a comparable rate [1]<br/>"
         "• Equilibrium constant Kc is finite (~4), so both reactants and products coexist at equilibrium [1].<br/><br/>"
         "<b>(a)(ii) [4 Marks]</b><br/>"
         "• CH3CH2COOCH2CH3 + NaOH --> CH3CH2COONa + CH3CH2OH (or with OH- --> CH3CH2COO- + C2H5OH) [2]<br/>"
         "• Propanoate ion, CH3CH2COO-, is negatively charged and resonance-stabilised [1]<br/>"
         "• Because the carboxylate anion cannot be attacked by the neutral alcohol molecule, the reverse reaction cannot occur, driving conversion to 100% [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• Triglyceride + 3CH3OH <=> Glycerol (propane-1,2,3-triol) + 3 Fatty acid methyl esters [2]<br/>"
         "• Balanced stoichiometric coefficient of 3 for methanol and 3 for methyl ester [1].<br/><br/>"
         "<b>(b)(ii) [2 Marks]</b><br/>"
         "• Carbon-neutral lifecycle: CO2 released upon combustion was recently absorbed by the feedstock plants during photosynthesis [1]<br/>"
         "• Negligible sulfur content, drastically reducing sulfur dioxide emissions and acid rain formation [1].<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• Structure of PLA repeat unit: -[O-CH(CH3)-CO]- with open extension bonds [2].<br/><br/>"
         "<b>(c)(ii) [2 Marks]</b><br/>"
         "• Structure of PET repeat unit: -[O-CH2-CH2-O-CO-C6H4-CO]- with benzene ring and ester linkages [2].<br/><br/>"
         "<b>(c)(iii) [2 Marks]</b><br/>"
         "• Polyesters contain polar C-O and C=O ester linkages susceptible to hydrolysis by water and microbial enzymes [1]<br/>"
         "• Addition polymers like poly(ethene) possess an entirely non-polar, unreactive C-C saturated alkane backbone with high bond enthalpy, completely resisting hydrolytic breakdown [1]."),

        ("Question 33: High-Resolution 1H NMR Spectroscopy (18 Marks)",
         "<b>(a) [3 Marks]</b><br/>"
         "• Protons have nuclear spin (spin +1/2 or -1/2), generating tiny magnetic fields that align with or against the applied field B0 [1]<br/>"
         "• These local fields split the energy levels of neighbouring non-equivalent protons via intervening bonding electrons [1]<br/>"
         "• n non-equivalent protons on adjacent carbons split the peak into n + 1 sub-peaks with Pascal's triangle intensity ratios [1].<br/><br/>"
         "<b>(b)(i) [6 Marks]</b><br/>"
         "• Signal 1 (δ = 1.25, 3H triplet): -CH3 group adjacent to a -CH2- group (2 adjacent H => 2+1 = 3); chemical shift typical of alkyl C-H [2]<br/>"
         "• Signal 2 (δ = 2.05, 3H singlet): -CH3 group attached directly to C=O (no adjacent H => singlet); chemical shift shifted downfield by carbonyl [2]<br/>"
         "• Signal 3 (δ = 4.12, 2H quartet): -CH2- group attached directly to electronegative ester oxygen (-O-CH2-), shifted downfield to ~4.1 ppm; adjacent to -CH3 (3 adjacent H => 3+1 = 4) [2].<br/><br/>"
         "<b>(b)(ii) [2 Marks]</b><br/>"
         "• Formula: CH3-COO-CH2-CH3 [1]<br/>"
         "• Name: Ethyl ethanoate [1].<br/><br/>"
         "<b>(c) [4 Marks]</b><br/>"
         "• Structure of X: CH3-CH2-COO-CH3 (Methyl propanoate) [1]<br/>"
         "• Justification: Signal C is a singlet with area 3 at δ = 3.65 ppm, indicating a methoxy group (-O-CH3) attached to oxygen [1]<br/>"
         "• Signal B is a quartet at δ = 2.35 ppm, indicating -CH2- attached to C=O (shifted to ~2.4 rather than ~4.1 in W) [1]<br/>"
         "• In W, the -CH2- is attached to oxygen (δ = 4.12), whereas in X, the -CH3 is attached to oxygen (δ = 3.65) [1].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• Adding D2O causes rapid isotopic proton-deuterium exchange with labile protons: R-OH + D2O <=> R-OD + HOD (or RCOOH) [1]<br/>"
         "• Deuterium (^2H) has a nuclear spin of 1 and resonates at a completely different frequency outside the 1H sweep range [1]<br/>"
         "• Consequently, the labile O-H (or N-H) signal completely disappears from the 1H spectrum, confirming its identity [1]."),

        ("Question 34: 13C NMR & GC-MS Spectrometry (18 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• Broad-band decoupling irradiates the sample with a continuous radiofrequency that averages all 1H-13C spin coupling to zero [1]<br/>"
         "• This collapses all complex multiplets into clean, sharp singlets, vastly increasing signal-to-noise ratio and simplifying spectrum interpretation [1].<br/><br/>"
         "<b>(a)(ii) [5 Marks]</b><br/>"
         "• Butan-1-ol (CH3CH2CH2CH2OH): 4 unique carbon environments => 4 peaks [1]<br/>"
         "• Butan-2-ol (CH3CH(OH)CH2CH3): 4 unique carbon environments => 4 peaks [1]<br/>"
         "• 2-methylpropan-2-ol ((CH3)3COH): 3 equivalent methyl carbons and 1 central C-OH carbon => exactly 2 peaks [1]<br/>"
         "• 2-methylpropan-2-ol is instantly identified by showing only 2 peaks [1]<br/>"
         "• Butan-1-ol and butan-2-ol are differentiated by chemical shift: C-OH in primary alcohol appears at δ ~60 ppm, whereas C-OH in secondary alcohol appears further downfield at δ ~70 ppm [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• GC column separates mixture components based on volatility (boiling point) and partitioning with liquid stationary phase [2]<br/>"
         "• Separated components elute sequentially into the mass spectrometer ion source at specific retention times [1]<br/>"
         "• The mass spectrometer bombards molecules with high-energy electrons (70 eV), creating molecular ions and characteristic fragmentation patterns to provide unequivocal identification [1].<br/><br/>"
         "<b>(b)(ii) [5 Marks]</b><br/>"
         "• Identity: Ethyl ethanoate, CH3COOCH2CH3 (Mr = 88) [1]<br/>"
         "• m/z = 73: [M - 15]+, loss of methyl radical => [CH3COOCH2]+ or [CH3CH2COO]+ [1]<br/>"
         "• m/z = 59: [COOCH3]+ or [CH3CH2CH2O]+ [1]<br/>"
         "• m/z = 43 (base peak): [CH3CO]+ (stable acylium ion formed by alpha-cleavage of ester bond) [1]<br/>"
         "• m/z = 29: [CH3CH2]+ (ethyl cation) or [CHO]+ [1].<br/><br/>"
         "<b>(b)(iii) [2 Marks]</b><br/>"
         "• GC with FID only provides retention times, which can overlap between isomers and complex metabolites [1]<br/>"
         "• MS provides an unequivocal fragmentation mass fingerprint matching computerized spectral libraries with near 100% legal certainty [1]."),

        ("Question 35: Multi-Spectral Elucidation (* Level of Response) (18 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• Number of carbon atoms n = (100 / 1.1) * (height of M+1 / height of M) = (100 / 1.1) * (4.4 / 100) = 4.4 / 1.1 = 4.0 [1]<br/>"
         "• Empirical formula C2H4O has formula mass 44; Mr = 88 = 2 x 44 [1]<br/>"
         "• Molecular formula is (C2H4O)2 = C4H8O2 [1].<br/><br/>"
         "<b>(a)(ii) [2 Marks]</b><br/>"
         "• Strong absorption at 1740 cm^-1 indicates a carbonyl group (C=O), specifically an ester carbonyl [1]<br/>"
         "• Absence of 3200-3600 cm^-1 rules out alcohols; absence of 2500-3300 cm^-1 rules out carboxylic acids [1].<br/><br/>"
         "<b>*(b) [6 Marks — Level of Response]</b><br/>"
         "• Level 3 (5-6 marks): Comprehensive synthetic and purification protocol. Reaction: mix anhydrous ethanol with ethanoyl chloride slowly in an ice bath inside a fume cupboard (exothermic, violent evolution of acidic HCl gas). Separation: transfer to separating funnel, add aqueous NaHCO3 and shake with frequent venting to neutralise and release CO2 from excess HCl; separate organic ester layer; wash with saturated NaCl (brine) to remove residual water and ethanol. Drying: transfer organic layer to conical flask, add anhydrous MgSO4, swirl until liquid is clear and drying agent flows freely, filter. Distillation: set up simple distillation apparatus with thermometer bulb level with side-arm; collect distillate in the boiling range 75–78 °C. Hazards & safety: ethanoyl chloride is highly corrosive and lachrymatory (fume cupboard, nitrile gloves); ethoxyethane and ester are highly flammable (electric heating mantle, no open flames).<br/>"
         "• Level 2 (3-4 marks): Logical plan describing reaction, separating funnel wash with NaHCO3, drying, and distillation, but with minor omissions in venting or safety controls.<br/>"
         "• Level 1 (1-2 marks): Basic list of steps with incomplete washing, drying, or hazard analysis.<br/><br/>"
         "<b>(c)(i) [2 Marks]</b><br/>"
         "• Formula: [CH3CO]+ (or [CH3-C=O]+) [1]<br/>"
         "• Structure: CH3-C≡O:+ with positive charge on oxygen (resonance stabilised) [1].<br/><br/>"
         "<b>(c)(ii) [2 Marks]</b><br/>"
         "• [CH3COOCH2CH3]+. --> [CH3CO]+ + .OCH2CH3 (loss of ethoxy radical) [2].<br/><br/>"
         "<b>(d) [3 Marks]</b><br/>"
         "• HPLC operates at ambient temperatures, avoiding thermal decomposition of delicate biomolecules like penicillin [1]<br/>"
         "• In reverse-phase HPLC, the stationary phase is non-polar (C18 hydrocarbon chains) and the mobile phase is polar (water/methanol) [1]<br/>"
         "• Polar compounds interact weakly with C18 and elute first (short retention time); non-polar compounds partition strongly into C18 and elute last [1]."),

        ("Question 36: Sustainable Polymers & Recycling (15 Marks)",
         "<b>(a)(i) [3 Marks]</b><br/>"
         "• n HOOC-C6H4-COOH + n HO-CH2CH2-OH --> -[CO-C6H4-CO-O-CH2CH2-O]n- + (2n-1) H2O [2]<br/>"
         "• Small molecule eliminated is water (H2O) [1].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Ethane-1,2-diol (EG) contributes 2 carbon atoms [1]<br/>"
         "• Terephthalic acid (PTA) contributes 8 carbon atoms [1]<br/>"
         "• Total carbons per repeat unit = 2 + 8 = 10 => Renewable carbon % = (2 / 10) x 100% = 20.0% [1].<br/><br/>"
         "<b>(b)(i) [3 Marks]</b><br/>"
         "• -[CO-C6H4-CO-O-CH2CH2-O]- + HO-CH2CH2-OH --> HO-CH2CH2-O-CO-C6H4-CO-O-CH2CH2-OH (BHET) [3].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Glycolysis regenerates pure virgin-grade monomer (BHET), removing all chemical contaminants, dyes, and degradation products that degrade mechanical properties in mechanical recycling [2]<br/>"
         "• Infinitely circular: polymers can be recycled indefinitely without downcycling into lower-grade carpet or fleece [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• Hydroxide ions (OH-) are much stronger nucleophiles than neutral water molecules [1]<br/>"
         "• OH- rapidly attacks the carbonyl carbon (Cδ+) in the ester linkage via nucleophilic addition-elimination [1]<br/>"
         "• Higher temperature (60 °C) provides more molecules with energy exceeding activation energy (Ea), increasing collision frequency and accelerating chain cleavage [1]."),

        ("Question 37: Paracetamol & Aspirin Synthesis (15 Marks)",
         "<b>(a)(i) [2 Marks]</b><br/>"
         "• 4-H2N-C6H4-OH + (CH3CO)2O --> 4-CH3CONH-C6H4-OH + CH3COOH [2].<br/><br/>"
         "<b>(a)(ii) [3 Marks]</b><br/>"
         "• Rate: Reaction with anhydride is easily controlled and less violently exothermic than acyl chloride [1]<br/>"
         "• Byproduct: Anhydride produces non-corrosive ethanoic acid; acyl chloride produces corrosive, toxic, lachrymatory HCl gas [1]<br/>"
         "• Cost: Ethanoic anhydride is cheaper and easier to handle in bulk chemical plants [1].<br/><br/>"
         "<b>(b)(i) [4 Marks]</b><br/>"
         "• Moles salicylic acid = 13.81 / 138.12 = 0.099986 mol ≈ 0.1000 mol [1]<br/>"
         "• Theoretical yield of aspirin = 0.1000 mol x 180.16 g mol^-1 = 18.016 g [1]<br/>"
         "• Percentage yield = (14.41 g / 18.016 g) x 100% [1]<br/>"
         "• = 79.98% ≈ 80.0% [1].<br/><br/>"
         "<b>(b)(ii) [3 Marks]</b><br/>"
         "• Salicylic acid contains a free phenolic -OH group directly attached to the benzene ring [1]<br/>"
         "• Phenols react with aqueous Fe3+ to form a deep purple iron(III) phenolate complex [1]<br/>"
         "• In pure aspirin, the phenolic -OH has been converted into an ester linkage (-OCOCH3), so it cannot complex with Fe3+ (remains yellow/colourless) [1].<br/><br/>"
         "<b>(c) [3 Marks]</b><br/>"
         "• m/z = 138: Loss of ketene (CH2=C=O, mass 42) or acetyl group, leaving the radical cation of salicylic acid, [HO-C6H4-COOH]+ [2]<br/>"
         "• m/z = 120: Subsequent loss of water (H2O, mass 18) from the salicylic acid fragment, forming the acylium cation [HO-C6H4-CO]+ [1].")
    ]

    for title, content in ms_struct:
        story.append(Paragraph(f"<b>{title}</b>", S['ms_qtitle']))
        story.append(Spacer(1, 0.15 * cm))
        story.append(Paragraph(content, S['ms_text']))
        story.append(Spacer(1, 0.35 * cm))
        story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=4))

    print("[2/2] Compiling publication-grade PDF to " + OUT_FILE + " ...")
    doc.build(story)
    print(f"[SUCCESS] Week 12 Real Past Paper PDF generated successfully! Size: {os.path.getsize(OUT_FILE)/(1024*1024):.2f} MB")


if __name__ == "__main__":
    build_pdf()
