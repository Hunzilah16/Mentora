"""
Cambridge International AS Chemistry (9701) Paper 3 (Advanced Practical Skills)
High-Quality PDF Generation Engine for Mentora Academy.
Candidate: Urwah
"""
import os
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict, Any

import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# -------------------------------------------------------------------------
# FONT REGISTRATION
# -------------------------------------------------------------------------

def register_poppins():
    font_dir = r"z:\tests n quizes63\books\psycology\new styl\fonts"
    fonts = {
        'Poppins':           'Poppins-Regular.ttf',
        'Poppins-Bold':      'Poppins-Bold.ttf',
        'Poppins-SemiBold':  'Poppins-SemiBold.ttf',
        'Poppins-Medium':    'Poppins-Medium.ttf',
        'Poppins-Italic':    'Poppins-Italic.ttf',
    }
    for name, filename in fonts.items():
        path = os.path.join(font_dir, filename)
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
            except Exception:
                pass

register_poppins()

# Color definitions
COLOR_NAVY = colors.HexColor("#0b1b36")
COLOR_CRIMSON = colors.HexColor("#a81717")
COLOR_DARK = colors.HexColor("#1e293b")
COLOR_MUTED = colors.HexColor("#64748b")
COLOR_BORDER = colors.HexColor("#cbd5e1")
COLOR_BG_LIGHT = colors.HexColor("#f8fafc")
COLOR_TEAL = colors.HexColor("#0f766e")
COLOR_RULE = colors.HexColor("#e2e8f0")

# -------------------------------------------------------------------------
# DATA STRUCTURES
# -------------------------------------------------------------------------

@dataclass
class PracticalSubQuestion:
    label: str               # e.g. "(a)", "(b)(i)", "(c)"
    text: str                # Question text
    marks: int               # e.g. 2
    lines_count: int = 3     # Number of dotted lines for response
    table_data: Optional[Any] = None  # Optional pre-built Flowable or Table data
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None
    mark_scheme: str = ""    # Full examiner marking points

@dataclass
class PracticalQuestion:
    number: int              # 1, 2, 3
    title: str               # e.g. "Titration of Iron(II) with Potassium Manganate(VII)"
    syllabus_ref: str        # e.g. "9701/33/M/J/23/Q1"
    total_marks: int         # e.g. 15
    procedure_intro: str     # Multi-line procedure, chemicals, apparatus, and safety advice
    subquestions: List[PracticalSubQuestion] = field(default_factory=list)

@dataclass
class PracticalPaperConfig:
    title: str
    subtitle: str
    component_name: str = "Paper 3 — Advanced Practical Skills"
    duration: str = "2 Hours"
    total_marks: int = 40
    candidate_name: str = "Urwah"
    centre_number: str = "PK082"
    candidate_number: str = "0142"

# -------------------------------------------------------------------------
# NUMBERED CANVAS FOR DYNAMIC PAGE NUMBERING
# -------------------------------------------------------------------------

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        page_num = self._pageNumber
        w, h = A4

        # Cover page has custom footer
        if page_num == 1:
            self.saveState()
            self.setFont("Poppins", 8.0)
            self.setFillColor(COLOR_MUTED)
            self.drawCentredString(w / 2.0, 36, "MENTORA ACADEMY · EXCELLENCE IN CAMBRIDGE ADVANCED LEVEL EDUCATION")
            self.setFont("Poppins-Medium", 7.5)
            self.setFillColor(COLOR_CRIMSON)
            self.drawCentredString(w / 2.0, 24, "CONFIDENTIAL LABORATORY ASSESSMENT PACK · AUTHORIZED FOR REGISTERED CANDIDATES")
            self.restoreState()
            return

        # Running Header on pages 2+
        self.saveState()
        # Navy line top
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.65)
        self.line(40, h - 42, w - 40, h - 42)

        # Header titles
        self.setFont("Poppins-Bold", 8.2)
        self.setFillColor(COLOR_NAVY)
        self.drawString(40, h - 36, "MENTORA ACADEMY")

        self.setFont("Poppins-Bold", 7.0)
        self.setFillColor(COLOR_CRIMSON)
        self.drawString(135, h - 36, "·  A D V A N C E D  P R A C T I C A L  S K I L L S")

        self.setFont("Poppins", 7.2)
        self.setFillColor(COLOR_MUTED)
        self.drawRightString(w - 40, h - 36, "Cambridge International AS Chemistry (9701/3)")

        # Running Footer
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.65)
        self.line(40, 44, w - 40, 44)

        self.setFont("Poppins", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawString(40, 32, "Candidate: Urwah  ·  Mentora Academy Chemistry Laboratory Suite")

        page_str = f"Page {page_num} of {total_pages}"
        self.setFont("Poppins-Medium", 7.5)
        self.setFillColor(COLOR_NAVY)
        self.drawRightString(w - 40, 32, page_str)
        self.restoreState()

# -------------------------------------------------------------------------
# STYLES SETUP
# -------------------------------------------------------------------------

def get_practical_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Poppins-Bold',
        fontSize=18,
        leading=22,
        textColor=COLOR_NAVY,
        alignment=0,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Poppins-Medium',
        fontSize=9.5,
        leading=14,
        textColor=COLOR_CRIMSON,
        alignment=0,
        spaceAfter=14
    )

    body_style = ParagraphStyle(
        'PracticalBody',
        parent=styles['Normal'],
        fontName='Poppins',
        fontSize=8.8,
        leading=13.0,
        textColor=COLOR_DARK,
        spaceAfter=5
    )

    bold_body_style = ParagraphStyle(
        'PracticalBoldBody',
        parent=styles['Normal'],
        fontName='Poppins-Bold',
        fontSize=8.8,
        leading=13.0,
        textColor=COLOR_NAVY,
        spaceAfter=5
    )

    q_title_style = ParagraphStyle(
        'PracticalQTitle',
        parent=styles['Normal'],
        fontName='Poppins-Bold',
        fontSize=11.5,
        leading=15,
        textColor=COLOR_NAVY,
        spaceBefore=8,
        spaceAfter=4
    )

    q_ref_style = ParagraphStyle(
        'PracticalQRef',
        parent=styles['Normal'],
        fontName='Poppins-SemiBold',
        fontSize=8.0,
        leading=10,
        textColor=COLOR_CRIMSON,
        spaceAfter=6
    )

    sub_q_style = ParagraphStyle(
        'PracticalSubQ',
        parent=styles['Normal'],
        fontName='Poppins',
        fontSize=8.6,
        leading=12.5,
        textColor=COLOR_DARK,
        spaceBefore=4,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Poppins-Bold',
        fontSize=7.8,
        leading=10,
        textColor=COLOR_NAVY,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Poppins',
        fontSize=7.6,
        leading=9.5,
        textColor=COLOR_DARK,
        alignment=0
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Poppins',
        fontSize=7.6,
        leading=9.5,
        textColor=COLOR_DARK,
        alignment=1
    )

    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'body': body_style,
        'bold_body': bold_body_style,
        'q_title': q_title_style,
        'q_ref': q_ref_style,
        'sub_q': sub_q_style,
        'table_header': table_header_style,
        'table_cell': table_cell_style,
        'table_cell_center': table_cell_center
    }

# -------------------------------------------------------------------------
# UTILITY GENERATORS FOR AUTHENTIC LABORATORY TABLES
# -------------------------------------------------------------------------

def make_titration_table(styles, default_runs=3):
    """Generates an authentic Cambridge Burette Reading Table with candidate check boxes."""
    headers = [
        Paragraph("<b>Burette Readings</b>", styles['table_header']),
        Paragraph("<b>Rough</b>", styles['table_header']),
        Paragraph("<b>Titration 1</b>", styles['table_header']),
        Paragraph("<b>Titration 2</b>", styles['table_header']),
        Paragraph("<b>Titration 3</b>", styles['table_header'])
    ]

    row1 = [Paragraph("Final burette reading / cm<sup>3</sup>", styles['table_cell']), "", "", "", ""]
    row2 = [Paragraph("Initial burette reading / cm<sup>3</sup>", styles['table_cell']), "", "", "", ""]
    row3 = [Paragraph("<b>Titre / cm<sup>3</sup></b>", styles['table_header']), "", "", "", ""]
    row4 = [Paragraph("Best titration results (&#10003;)", styles['table_cell']), "", "", "", ""]

    data = [headers, row1, row2, row3, row4]
    col_widths = [190, 75, 75, 75, 75]

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor("#f1f5f9")),
    ]))
    return t

def make_crucible_table(styles):
    """Generates an authentic Cambridge Gravimetric Constant-Mass Weighing Table."""
    headers = [
        Paragraph("<b>Measurement Description</b>", styles['table_header']),
        Paragraph("<b>Mass / g</b>", styles['table_header'])
    ]
    rows = [
        [Paragraph("Mass of empty crucible + lid", styles['table_cell']), ""],
        [Paragraph("Mass of crucible + lid + hydrated sample before heating", styles['table_cell']), ""],
        [Paragraph("Mass of crucible + lid + sample after 1st heating", styles['table_cell']), ""],
        [Paragraph("Mass of crucible + lid + sample after 2nd heating (to constant mass)", styles['table_cell']), ""],
        [Paragraph("<b>Mass of anhydrous salt residue</b>", styles['table_header']), ""],
        [Paragraph("<b>Mass of water of crystallization lost</b>", styles['table_header']), ""]
    ]
    t = Table([headers] + rows, colWidths=[360, 130])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('BACKGROUND', (0, 4), (-1, 5), colors.HexColor("#f1f5f9")),
    ]))
    return t

def make_thermometry_table(styles):
    """Generates an authentic Cambridge Thermometer Cooling-Curve Data Table."""
    headers = [
        Paragraph("<b>Time / min</b>", styles['table_header']),
        Paragraph("<b>Temp / °C</b>", styles['table_header']),
        Paragraph("<b>Time / min</b>", styles['table_header']),
        Paragraph("<b>Temp / °C</b>", styles['table_header']),
        Paragraph("<b>Time / min</b>", styles['table_header']),
        Paragraph("<b>Temp / °C</b>", styles['table_header'])
    ]
    data = [
        headers,
        [Paragraph("0.0", styles['table_cell_center']), "", Paragraph("3.5", styles['table_cell_center']), "", Paragraph("7.0", styles['table_cell_center']), ""],
        [Paragraph("0.5", styles['table_cell_center']), "", Paragraph("4.0", styles['table_cell_center']), "", Paragraph("7.5", styles['table_cell_center']), ""],
        [Paragraph("1.0", styles['table_cell_center']), "", Paragraph("4.5", styles['table_cell_center']), "", Paragraph("8.0", styles['table_cell_center']), ""],
        [Paragraph("1.5", styles['table_cell_center']), "", Paragraph("5.0", styles['table_cell_center']), "", Paragraph("8.5", styles['table_cell_center']), ""],
        [Paragraph("2.0", styles['table_cell_center']), "", Paragraph("5.5", styles['table_cell_center']), "", Paragraph("9.0", styles['table_cell_center']), ""],
        [Paragraph("2.5", styles['table_cell_center']), "", Paragraph("6.0", styles['table_cell_center']), "", Paragraph("9.5", styles['table_cell_center']), ""],
        [Paragraph("3.0 (mix)", styles['table_cell_center']), "X", Paragraph("6.5", styles['table_cell_center']), "", Paragraph("10.0", styles['table_cell_center']), ""]
    ]
    t = Table(data, colWidths=[70, 93, 70, 93, 70, 93])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.8),
        ('BACKGROUND', (1, 7), (1, 7), colors.HexColor("#e2e8f0")),
    ]))
    return t

def make_observation_table(styles, rows_list):
    """Generates an authentic Cambridge 3-column Qualitative Analysis Observation Table."""
    headers = [
        Paragraph("<b>Test</b>", styles['table_header']),
        Paragraph("<b>Observations</b>", styles['table_header']),
        Paragraph("<b>Deductions</b>", styles['table_header'])
    ]
    data = [headers]
    for row in rows_list:
        test_txt, obs_txt, ded_txt = row
        data.append([
            Paragraph(test_txt, styles['table_cell']),
            Paragraph(obs_txt, styles['table_cell']),
            Paragraph(ded_txt, styles['table_cell'])
        ])

    t = Table(data, colWidths=[170, 180, 140])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    return t

def make_dotted_lines(count=2, width=490):
    """Generates authentic dotted answer lines."""
    line_html = "&nbsp;" * 130
    elements = []
    for _ in range(count):
        elements.append(Paragraph(
            "<font color='#94a3b8'>.........................................................................................................................................................................................</font>",
            ParagraphStyle('DottedLine', fontName='Poppins', fontSize=6.5, leading=9)
        ))
        elements.append(Spacer(1, 2))
    return elements

# -------------------------------------------------------------------------
# QUALITATIVE ANALYSIS NOTES BUILDER (Official Cambridge Reference)
# -------------------------------------------------------------------------

def build_qualitative_analysis_notes_flowables(styles):
    flowables = []
    flowables.append(PageBreak())

    title_p = Paragraph("<b>Qualitative Analysis Notes</b>", styles['q_title'])
    sub_p = Paragraph("<b>Tables for the reactions of aqueous cations, anions, and tests for gases (Cambridge 9701 Syllabus Reference)</b>", styles['subtitle'])
    flowables.extend([title_p, sub_p, Spacer(1, 4)])

    # Table 1: Cations
    flowables.append(Paragraph("<b>1. Reactions of Aqueous Cations</b>", styles['bold_body']))
    cat_headers = [
        Paragraph("<b>Cation</b>", styles['table_header']),
        Paragraph("<b>Reaction with NaOH(aq)</b>", styles['table_header']),
        Paragraph("<b>Reaction with NH<sub>3</sub>(aq)</b>", styles['table_header'])
    ]
    cat_data = [
        cat_headers,
        [Paragraph("<b>Aluminium, Al<sup>3+</sup></b>", styles['table_cell']), Paragraph("White ppt., soluble in excess giving a colorless solution", styles['table_cell']), Paragraph("White ppt., insoluble in excess", styles['table_cell'])],
        [Paragraph("<b>Ammonium, NH<sub>4</sub><sup>+</sup></b>", styles['table_cell']), Paragraph("Ammonia gas produced on warming (turns damp red litmus blue)", styles['table_cell']), Paragraph("No reaction", styles['table_cell'])],
        [Paragraph("<b>Barium, Ba<sup>2+</sup></b>", styles['table_cell']), Paragraph("Faint white ppt. or no ppt. (high [Ba<sup>2+</sup>])", styles['table_cell']), Paragraph("No ppt.", styles['table_cell'])],
        [Paragraph("<b>Calcium, Ca<sup>2+</sup></b>", styles['table_cell']), Paragraph("White ppt. with high [Ca<sup>2+</sup>], insoluble in excess", styles['table_cell']), Paragraph("No ppt. with dilute solutions", styles['table_cell'])],
        [Paragraph("<b>Chromium(III), Cr<sup>3+</sup></b>", styles['table_cell']), Paragraph("Grey-green ppt., soluble in excess giving dark green solution", styles['table_cell']), Paragraph("Grey-green ppt., insoluble in excess", styles['table_cell'])],
        [Paragraph("<b>Copper(II), Cu<sup>2+</sup></b>", styles['table_cell']), Paragraph("Pale blue ppt., insoluble in excess", styles['table_cell']), Paragraph("Pale blue ppt., soluble in excess giving intense deep blue solution", styles['table_cell'])],
        [Paragraph("<b>Iron(II), Fe<sup>2+</sup></b>", styles['table_cell']), Paragraph("Green ppt., insoluble in excess; turns brown on standing near surface", styles['table_cell']), Paragraph("Green ppt., insoluble in excess; turns brown on standing", styles['table_cell'])],
        [Paragraph("<b>Iron(III), Fe<sup>3+</sup></b>", styles['table_cell']), Paragraph("Red-brown ppt., insoluble in excess", styles['table_cell']), Paragraph("Red-brown ppt., insoluble in excess", styles['table_cell'])],
        [Paragraph("<b>Magnesium, Mg<sup>2+</sup></b>", styles['table_cell']), Paragraph("White ppt., insoluble in excess", styles['table_cell']), Paragraph("White ppt., insoluble in excess", styles['table_cell'])],
        [Paragraph("<b>Manganese(II), Mn<sup>2+</sup></b>", styles['table_cell']), Paragraph("Off-white ppt., insoluble in excess; rapidly darkens to brown", styles['table_cell']), Paragraph("Off-white ppt., insoluble in excess; darkens to brown", styles['table_cell'])],
        [Paragraph("<b>Zinc, Zn<sup>2+</sup></b>", styles['table_cell']), Paragraph("White ppt., soluble in excess giving a colorless solution", styles['table_cell']), Paragraph("White ppt., soluble in excess giving a colorless solution", styles['table_cell'])],
    ]
    t_cat = Table(cat_data, colWidths=[105, 192, 193])
    t_cat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    flowables.extend([t_cat, Spacer(1, 8)])

    # Table 2: Anions
    flowables.append(Paragraph("<b>2. Reactions of Aqueous Anions</b>", styles['bold_body']))
    ani_headers = [
        Paragraph("<b>Ion</b>", styles['table_header']),
        Paragraph("<b>Test</b>", styles['table_header']),
        Paragraph("<b>Observation</b>", styles['table_header'])
    ]
    ani_data = [
        ani_headers,
        [Paragraph("<b>Carbonate, CO<sub>3</sub><sup>2-</sup></b>", styles['table_cell']), Paragraph("Add dilute acid", styles['table_cell']), Paragraph("Effervescence; gas turns limewater milky (CO<sub>2</sub>)", styles['table_cell'])],
        [Paragraph("<b>Chloride, Cl<sup>-</sup>(aq)</b>", styles['table_cell']), Paragraph("Add dilute HNO<sub>3</sub>, then aqueous AgNO<sub>3</sub>", styles['table_cell']), Paragraph("White ppt., soluble in dilute aqueous ammonia", styles['table_cell'])],
        [Paragraph("<b>Bromide, Br<sup>-</sup>(aq)</b>", styles['table_cell']), Paragraph("Add dilute HNO<sub>3</sub>, then aqueous AgNO<sub>3</sub>", styles['table_cell']), Paragraph("Cream ppt., insoluble in dilute NH<sub>3</sub>, soluble in conc. NH<sub>3</sub>", styles['table_cell'])],
        [Paragraph("<b>Iodide, I<sup>-</sup>(aq)</b>", styles['table_cell']), Paragraph("Add dilute HNO<sub>3</sub>, then aqueous AgNO<sub>3</sub>", styles['table_cell']), Paragraph("Yellow ppt., insoluble in dilute and conc. aqueous NH<sub>3</sub>", styles['table_cell'])],
        [Paragraph("<b>Nitrate, NO<sub>3</sub><sup>-</sup>(aq)</b>", styles['table_cell']), Paragraph("Warm with aqueous NaOH, then add Al foil", styles['table_cell']), Paragraph("Ammonia produced; pungent gas turns damp red litmus blue", styles['table_cell'])],
        [Paragraph("<b>Sulfate, SO<sub>4</sub><sup>2-</sup>(aq)</b>", styles['table_cell']), Paragraph("Add dilute HNO<sub>3</sub>, then aqueous Ba(NO<sub>3</sub>)<sub>2</sub> / BaCl<sub>2</sub>", styles['table_cell']), Paragraph("Dense white ppt. (insoluble in dilute strong acids)", styles['table_cell'])],
        [Paragraph("<b>Sulfite, SO<sub>3</sub><sup>2-</sup>(aq)</b>", styles['table_cell']), Paragraph("Add dilute acid, warm gently and test gas", styles['table_cell']), Paragraph("Gas produced (SO<sub>2</sub>) turns acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> from orange to green", styles['table_cell'])],
    ]
    t_ani = Table(ani_data, colWidths=[90, 200, 200])
    t_ani.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    flowables.extend([t_ani, Spacer(1, 8)])

    # Table 3: Gases
    flowables.append(Paragraph("<b>3. Tests for Gases</b>", styles['bold_body']))
    gas_headers = [
        Paragraph("<b>Gas</b>", styles['table_header']),
        Paragraph("<b>Test and Test Result</b>", styles['table_header'])
    ]
    gas_data = [
        gas_headers,
        [Paragraph("<b>Ammonia, NH<sub>3</sub></b>", styles['table_cell']), Paragraph("Turns damp red litmus paper blue; choking pungent smell", styles['table_cell'])],
        [Paragraph("<b>Carbon dioxide, CO<sub>2</sub></b>", styles['table_cell']), Paragraph("Gives a white precipitate with limewater (calcium hydroxide solution turns milky)", styles['table_cell'])],
        [Paragraph("<b>Chlorine, Cl<sub>2</sub></b>", styles['table_cell']), Paragraph("Bleaches damp litmus paper white; pale green choking gas", styles['table_cell'])],
        [Paragraph("<b>Hydrogen, H<sub>2</sub></b>", styles['table_cell']), Paragraph("'Pops' with a lighted wooden splint", styles['table_cell'])],
        [Paragraph("<b>Oxygen, O<sub>2</sub></b>", styles['table_cell']), Paragraph("Relights a glowing wooden splint", styles['table_cell'])],
        [Paragraph("<b>Sulfur dioxide, SO<sub>2</sub></b>", styles['table_cell']), Paragraph("Turns acidified potassium dichromate(VI) paper from orange to green", styles['table_cell'])],
    ]
    t_gas = Table(gas_data, colWidths=[120, 370])
    t_gas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    flowables.append(t_gas)

    return flowables

# -------------------------------------------------------------------------
# MASTER PDF BUILDER FUNCTION
# -------------------------------------------------------------------------

def build_paper3_pdf(
    output_path: str,
    config: PracticalPaperConfig,
    questions: List[PracticalQuestion],
    include_qa_notes: bool = True
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=54,
        bottomMargin=54
    )

    styles = get_practical_styles()
    story = []

    # -------------------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------------------
    # Top Brand Header
    story.append(Paragraph("<b>M E N T O R A&nbsp;&nbsp;&nbsp;&nbsp;A C A D E M Y</b>", ParagraphStyle(
        'CoverBrand', fontName='Poppins-Bold', fontSize=14, leading=17, textColor=COLOR_NAVY, alignment=1
    )))
    story.append(Paragraph("<b>DEPARTMENT OF ADVANCED CHEMISTRY · CAMBRIDGE INTERNATIONAL AS LEVEL (9701)</b>", ParagraphStyle(
        'CoverSubBrand', fontName='Poppins-SemiBold', fontSize=7.0, leading=9, textColor=COLOR_CRIMSON, alignment=1
    )))
    story.append(Spacer(1, 14))

    # Paper Title Box
    story.append(Paragraph(f"<b>{config.title}</b>", styles['title']))
    story.append(Paragraph(f"<b>{config.subtitle}</b>", styles['subtitle']))
    story.append(Spacer(1, 4))

    # Candidate Identification Box
    cand_info = [
        [Paragraph("<b>CANDIDATE NAME</b>", styles['table_header']), Paragraph(f"<b>{config.candidate_name.upper()}</b>", styles['table_cell']),
         Paragraph("<b>CENTRE NUMBER</b>", styles['table_header']), Paragraph(f"<b>{config.centre_number}</b>", styles['table_cell'])],
        [Paragraph("<b>COMPONENT</b>", styles['table_header']), Paragraph(f"<b>{config.component_name}</b>", styles['table_cell']),
         Paragraph("<b>CANDIDATE NUMBER</b>", styles['table_header']), Paragraph(f"<b>{config.candidate_number}</b>", styles['table_cell'])],
        [Paragraph("<b>TIME ALLOWED</b>", styles['table_header']), Paragraph(f"<b>{config.duration}</b>", styles['table_cell']),
         Paragraph("<b>TOTAL MARKS</b>", styles['table_header']), Paragraph(f"<b>{config.total_marks} Marks</b>", styles['table_cell'])]
    ]
    t_cand = Table(cand_info, colWidths=[110, 150, 110, 120])
    t_cand.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), COLOR_BG_LIGHT),
        ('BACKGROUND', (2, 0), (2, -1), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.2, COLOR_NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_cand)
    story.append(Spacer(1, 14))

    # Instructions Box
    instr_text = (
        "<b>INSTRUCTIONS TO CANDIDATES:</b><br/>"
        "• Answer <b>all</b> questions in the spaces provided on the question paper.<br/>"
        "• Give working for all calculations and record all experimental readings to the required precision:<br/>"
        "&nbsp;&nbsp;– Burette readings to the nearest <b>0.05 cm<sup>3</sup></b>; balance readings to <b>0.01 g / 0.001 g</b>.<br/>"
        "&nbsp;&nbsp;– Thermometer readings to the nearest <b>0.5 °C</b>.<br/>"
        "• You may use an HB pencil for any rough working, graphs, or apparatus diagrams.<br/>"
        "• Non-exact numerical answers should be given to <b>three significant figures</b> unless stated otherwise.<br/>"
        "• You will need a scientific calculator and the <b>Qualitative Analysis Notes</b> provided on pages at the back."
    )
    t_instr = Table([[Paragraph(instr_text, styles['body'])]], colWidths=[490])
    t_instr.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_BORDER),
        ('LINELEFT', (0, 0), (0, -1), 3.0, COLOR_CRIMSON),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_instr)
    story.append(Spacer(1, 14))

    # Practical Overview Section
    story.append(Paragraph("<b>LABORATORY INVESTIGATION OVERVIEW:</b>", styles['bold_body']))
    overview_text = (
        "This laboratory pack contains authentic Cambridge Advanced Practical examinations. "
        "Each practical scenario provides complete procedures, chemical specifications (FA codes), hazard warnings, "
        "structured data collection tables, graphical plotting grids, and comprehensive multi-step mathematical and observational deductions."
    )
    story.append(Paragraph(overview_text, styles['body']))
    story.append(Spacer(1, 10))

    # Page Break to Questions
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # QUESTIONS & PROCEDURES
    # -------------------------------------------------------------------------
    for q_idx, q in enumerate(questions, 1):
        if q_idx > 1:
            story.append(PageBreak())

        # Question Header
        q_head = Paragraph(f"<b>Question {q.number}: {q.title}</b>", styles['q_title'])
        q_ref = Paragraph(f"<b>Cambridge Syllabus Reference: {q.syllabus_ref}  ·  [{q.total_marks} Marks]</b>", styles['q_ref'])
        story.extend([q_head, q_ref, Spacer(1, 4)])

        # Procedure & Chemicals Intro
        intro_box = Table([[Paragraph(q.procedure_intro, styles['body'])]], colWidths=[490])
        intro_box.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
            ('BOX', (0, 0), (-1, -1), 0.75, COLOR_BORDER),
            ('LINELEFT', (0, 0), (0, -1), 3.0, COLOR_NAVY),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('LEFTPADDING', (0, 0), (-1, -1), 9),
            ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ]))
        story.append(intro_box)
        story.append(Spacer(1, 10))

        # Sub-questions
        for sq in q.subquestions:
            # Sub-question text with mark badge
            sq_p = Paragraph(f"<b>{sq.label}</b> {sq.text} <font color='#a81717'><b>[{sq.marks}]</b></font>", styles['sub_q'])
            story.append(sq_p)

            # Optional table (e.g. Titration table, Weighing table, Observation table)
            if sq.table_data is not None:
                story.append(Spacer(1, 4))
                story.append(sq.table_data)
                story.append(Spacer(1, 5))

            # Optional figure
            if sq.figure_path and os.path.exists(sq.figure_path):
                story.append(Spacer(1, 4))
                img = Image(sq.figure_path, width=470, height=290)
                story.append(img)
                if sq.figure_caption:
                    cap = Paragraph(f"<i>{sq.figure_caption}</i>", ParagraphStyle('Cap', fontName='Poppins-Italic', fontSize=7.5, leading=10, textColor=COLOR_MUTED, alignment=1))
                    story.append(cap)
                story.append(Spacer(1, 5))

            # Dotted lines for student answer
            if sq.lines_count > 0:
                story.append(Spacer(1, 3))
                story.extend(make_dotted_lines(sq.lines_count))
                story.append(Spacer(1, 4))

            # Divider between subparts
            story.append(HRFlowable(width="100%", thickness=0.4, color=COLOR_RULE, spaceBefore=4, spaceAfter=6))

    # -------------------------------------------------------------------------
    # QUALITATIVE ANALYSIS NOTES (IF ENABLED)
    # -------------------------------------------------------------------------
    if include_qa_notes:
        qa_flowables = build_qualitative_analysis_notes_flowables(styles)
        story.extend(qa_flowables)

    # -------------------------------------------------------------------------
    # MARK SCHEME & EXAMINER OBSERVATION GUIDE
    # -------------------------------------------------------------------------
    story.append(PageBreak())
    ms_title = Paragraph("<b>Examiner Mark Scheme & Indicative Observation Guide</b>", styles['q_title'])
    ms_sub = Paragraph(f"<b>Confidential Marking Points & Error Tolerances for {config.title}</b>", styles['subtitle'])
    story.extend([ms_title, ms_sub, Spacer(1, 6)])

    for q in questions:
        q_banner = Paragraph(f"<b>Question {q.number}: {q.title} [{q.total_marks} Marks]</b>", styles['bold_body'])
        story.append(q_banner)
        story.append(Spacer(1, 3))

        ms_rows = [[Paragraph("<b>Part</b>", styles['table_header']), Paragraph("<b>Marking Points & Expected Observations</b>", styles['table_header']), Paragraph("<b>Marks</b>", styles['table_header'])]]
        for sq in q.subquestions:
            ms_rows.append([
                Paragraph(f"<b>{sq.label}</b>", styles['table_cell_center']),
                Paragraph(sq.mark_scheme, styles['table_cell']),
                Paragraph(f"<b>[{sq.marks}]</b>", styles['table_cell_center'])
            ])
        t_ms = Table(ms_rows, colWidths=[45, 400, 45])
        t_ms.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
            ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t_ms)
        story.append(Spacer(1, 10))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    file_size = os.path.getsize(output_path)
    print(f"[SUCCESS] Built Paper 3 PDF: {output_path} ({file_size:,d} bytes)")
    return output_path
