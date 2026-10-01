"""
Cambridge International A Level Chemistry (9701) Paper 5 (Planning, Analysis and Evaluation)
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
class Paper5SubQuestion:
    label: str               # e.g. "(a)", "(b)(i)", "(c)"
    text: str                # Question text
    marks: int               # e.g. 2
    lines_count: int = 3     # Number of dotted lines for response
    table_data: Optional[Any] = None  # Optional pre-built Table
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None
    mark_scheme: str = ""    # Full examiner marking points

@dataclass
class Paper5Question:
    number: int              # 1 (Planning), 2 (Analysis & Evaluation)
    title: str               # e.g. "Planning an Electrochemical Determination of the Faraday Constant"
    syllabus_ref: str        # e.g. "9701/52/M/J/23/Q1"
    question_type: str       # "PLANNING" or "ANALYSIS & EVALUATION"
    total_marks: int         # e.g. 15
    context_intro: str       # Comprehensive experimental scenario & problem description
    subquestions: List[Paper5SubQuestion] = field(default_factory=list)

@dataclass
class Paper5PaperConfig:
    title: str
    subtitle: str
    component_name: str = "Paper 5 — Planning, Analysis and Evaluation"
    duration: str = "1 Hour 15 Minutes"
    total_marks: int = 30
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

        # Cover page custom footer
        if page_num == 1:
            self.saveState()
            self.setFont("Poppins", 8.0)
            self.setFillColor(COLOR_MUTED)
            self.drawCentredString(w / 2.0, 36, "MENTORA ACADEMY · EXCELLENCE IN CAMBRIDGE ADVANCED LEVEL EDUCATION")
            self.setFont("Poppins-Medium", 7.5)
            self.setFillColor(COLOR_CRIMSON)
            self.drawCentredString(w / 2.0, 24, "A LEVEL PAPER 5 PLANNING & ANALYSIS PACK · AUTHORIZED FOR REGISTERED CANDIDATES")
            self.restoreState()
            return

        # Running Header on pages 2+
        self.saveState()
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.65)
        self.line(40, h - 42, w - 40, h - 42)

        self.setFont("Poppins-Bold", 8.2)
        self.setFillColor(COLOR_NAVY)
        self.drawString(40, h - 36, "MENTORA ACADEMY")

        self.setFont("Poppins-Bold", 7.0)
        self.setFillColor(COLOR_CRIMSON)
        self.drawString(135, h - 36, "·  P L A N N I N G ,  A N A L Y S I S  &  E V A L U A T I O N")

        self.setFont("Poppins", 7.2)
        self.setFillColor(COLOR_MUTED)
        self.drawRightString(w - 40, h - 36, "Cambridge International A Level Chemistry (9701/5)")

        # Running Footer
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.65)
        self.line(40, 44, w - 40, 44)

        self.setFont("Poppins", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawString(40, 32, "Candidate: Urwah  ·  Mentora Academy A Level Laboratory Suite")

        page_str = f"Page {page_num} of {total_pages}"
        self.setFont("Poppins-Medium", 7.5)
        self.setFillColor(COLOR_NAVY)
        self.drawRightString(w - 40, 32, page_str)
        self.restoreState()

# -------------------------------------------------------------------------
# STYLES SETUP
# -------------------------------------------------------------------------

def get_paper5_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Poppins-Bold',
        fontSize=17,
        leading=21,
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

def make_dotted_lines(count=2):
    elements = []
    for _ in range(count):
        elements.append(Paragraph(
            "<font color='#94a3b8'>.........................................................................................................................................................................................</font>",
            ParagraphStyle('DottedLine', fontName='Poppins', fontSize=6.5, leading=9)
        ))
        elements.append(Spacer(1, 2))
    return elements

# -------------------------------------------------------------------------
# MASTER PDF BUILDER FUNCTION FOR PAPER 5
# -------------------------------------------------------------------------

def build_paper5_pdf(
    output_path: str,
    config: Paper5PaperConfig,
    questions: List[Paper5Question]
):
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=54,
        bottomMargin=54
    )

    styles = get_paper5_styles()
    story = []

    # -------------------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------------------
    story.append(Paragraph("<b>M E N T O R A&nbsp;&nbsp;&nbsp;&nbsp;A C A D E M Y</b>", ParagraphStyle(
        'CoverBrand', fontName='Poppins-Bold', fontSize=14, leading=17, textColor=COLOR_NAVY, alignment=1
    )))
    story.append(Paragraph("<b>DEPARTMENT OF ADVANCED CHEMISTRY · CAMBRIDGE INTERNATIONAL A LEVEL (9701)</b>", ParagraphStyle(
        'CoverSubBrand', fontName='Poppins-SemiBold', fontSize=7.0, leading=9, textColor=COLOR_CRIMSON, alignment=1
    )))
    story.append(Spacer(1, 14))

    # Paper Title Box
    story.append(Paragraph(f"<b>{config.title}</b>", styles['title']))
    story.append(Paragraph(f"<b>{config.subtitle}</b>", styles['subtitle']))

    # Metadata Grid
    meta_data = [
        [
            Paragraph("<b>CANDIDATE NAME:</b>", styles['table_header']),
            Paragraph(f"<b>{config.candidate_name}</b>", styles['table_cell']),
            Paragraph("<b>CENTRE NUMBER:</b>", styles['table_header']),
            Paragraph(f"<b>{config.centre_number}</b>", styles['table_cell']),
            Paragraph("<b>CANDIDATE NO:</b>", styles['table_header']),
            Paragraph(f"<b>{config.candidate_number}</b>", styles['table_cell'])
        ],
        [
            Paragraph("<b>COMPONENT:</b>", styles['table_header']),
            Paragraph(f"{config.component_name}", styles['table_cell']),
            Paragraph("<b>DURATION:</b>", styles['table_header']),
            Paragraph(f"{config.duration}", styles['table_cell']),
            Paragraph("<b>MAX MARKS:</b>", styles['table_header']),
            Paragraph(f"<b>{config.total_marks} Marks</b>", styles['table_cell'])
        ]
    ]
    t_meta = Table(meta_data, colWidths=[95, 115, 85, 75, 75, 70])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.75, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.2, COLOR_NAVY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 14))

    # Candidate Instructions Banner
    story.append(Paragraph("<b>READ THESE INSTRUCTIONS FIRST</b>", ParagraphStyle(
        'InstrHeader', fontName='Poppins-Bold', fontSize=9, leading=12, textColor=COLOR_CRIMSON
    )))
    instructions_text = (
        "• Write your name, Centre number, and candidate number in the boxes above.<br/>"
        "• Answer <b>all</b> questions in the spaces provided on the question paper.<br/>"
        "• In Question 1 (Planning): define independent, dependent, and controlled variables; describe step-by-step procedures with apparatus diagrams; calculate required quantities; state hazard risk assessments.<br/>"
        "• In Question 2 (Analysis, Conclusions & Evaluation): process raw experimental data into derived columns; quote values to consistent significant figures; plot graphs with appropriate linear scales; determine gradients and intercepts; identify anomalous points; evaluate uncertainties.<br/>"
        "• You may use an approved scientific calculator. The Periodic Table is provided as standard reference."
    )
    story.append(Paragraph(instructions_text, styles['body']))
    story.append(Spacer(1, 12))

    # Assessment Breakdown Table
    story.append(Paragraph("<b>EXAMINATION BREAKDOWN & SYLLABUS SKILLS TESTED</b>", styles['bold_body']))
    breakdown_data = [
        [
            Paragraph("<b>Question</b>", styles['table_header']),
            Paragraph("<b>Investigation Title & Focus</b>", styles['table_header']),
            Paragraph("<b>Syllabus Ref</b>", styles['table_header']),
            Paragraph("<b>Type of Task</b>", styles['table_header']),
            Paragraph("<b>Marks</b>", styles['table_header'])
        ]
    ]
    for q in questions:
        breakdown_data.append([
            Paragraph(f"<b>Question {q.number}</b>", styles['table_cell_center']),
            Paragraph(q.title, styles['table_cell']),
            Paragraph(q.syllabus_ref, styles['table_cell_center']),
            Paragraph(q.question_type, styles['table_cell_center']),
            Paragraph(f"<b>{q.total_marks}</b>", styles['table_cell_center'])
        ])

    t_breakdown = Table(breakdown_data, colWidths=[65, 215, 80, 100, 55])
    t_breakdown.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.65, COLOR_BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_breakdown)
    story.append(Spacer(1, 16))

    # Mentora Certification Seal
    story.append(Paragraph(
        "<b>MENTORA ACADEMY · OFFICIAL A LEVEL ADVANCED CHEMISTRY EXPERIMENTAL SUITE</b>",
        ParagraphStyle('Seal', fontName='Poppins-SemiBold', fontSize=7.0, leading=9, textColor=COLOR_MUTED, alignment=1)
    ))

    # -------------------------------------------------------------------------
    # QUESTION PAGES
    # -------------------------------------------------------------------------
    for q in questions:
        story.append(PageBreak())

        # Question Header Banner
        q_banner = Table([
            [
                Paragraph(f"<b>QUESTION {q.number}</b>", ParagraphStyle('QBannerTitle', fontName='Poppins-Bold', fontSize=10, textColor=colors.white)),
                Paragraph(f"<b>{q.question_type}</b>", ParagraphStyle('QBannerType', fontName='Poppins-SemiBold', fontSize=8, textColor=colors.white, alignment=2)),
                Paragraph(f"<b>[Total: {q.total_marks} Marks]</b>", ParagraphStyle('QBannerMarks', fontName='Poppins-Bold', fontSize=8.5, textColor=colors.white, alignment=2))
            ]
        ], colWidths=[130, 255, 130])
        q_banner.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), COLOR_NAVY),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(q_banner)
        story.append(Spacer(1, 6))

        story.append(Paragraph(f"<b>{q.title}</b>", styles['q_title']))
        story.append(Paragraph(f"<b>Cambridge Syllabus Reference:</b> {q.syllabus_ref}", styles['q_ref']))
        story.append(HRFlowable(width="100%", thickness=0.6, color=COLOR_RULE, spaceBefore=2, spaceAfter=6))

        # Context Introduction
        story.append(Paragraph(q.context_intro, styles['body']))
        story.append(Spacer(1, 8))

        # Subquestions
        for sq in q.subquestions:
            sq_header = Table([
                [
                    Paragraph(f"<b>{sq.label}</b>", styles['bold_body']),
                    Paragraph(sq.text, styles['sub_q']),
                    Paragraph(f"<b>[{sq.marks}]</b>", ParagraphStyle('MarkStyle', fontName='Poppins-Bold', fontSize=8.5, textColor=COLOR_CRIMSON, alignment=2))
                ]
            ], colWidths=[24, 455, 36])
            sq_header.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            story.append(sq_header)

            if sq.figure_path and os.path.exists(sq.figure_path):
                story.append(Spacer(1, 4))
                img = Image(sq.figure_path, width=490, height=200)
                story.append(img)
                if sq.figure_caption:
                    story.append(Paragraph(f"<i>{sq.figure_caption}</i>", ParagraphStyle('FigCap', fontName='Poppins-Italic', fontSize=7.0, textColor=COLOR_MUTED, alignment=1)))
                story.append(Spacer(1, 4))

            if sq.table_data:
                story.append(Spacer(1, 4))
                story.append(sq.table_data)
                story.append(Spacer(1, 4))

            if sq.lines_count > 0:
                story.append(Spacer(1, 3))
                story.extend(make_dotted_lines(sq.lines_count))
                story.append(Spacer(1, 4))
            else:
                story.append(Spacer(1, 4))

    # -------------------------------------------------------------------------
    # EXAMINER MARK SCHEME PAGES
    # -------------------------------------------------------------------------
    story.append(PageBreak())
    ms_title = Paragraph("<b>Comprehensive Examiner Mark Scheme</b>", styles['q_title'])
    ms_subtitle = Paragraph("<b>Marking points, indicative responses, and error-carried-forward (ECF) guidelines</b>", styles['subtitle'])
    story.extend([ms_title, ms_subtitle, Spacer(1, 6)])

    for q in questions:
        q_banner = Table([
            [
                Paragraph(f"<b>MARK SCHEME: QUESTION {q.number} ({q.question_type}) — {q.title}</b>", ParagraphStyle('MSBanner', fontName='Poppins-Bold', fontSize=8, textColor=colors.white)),
                Paragraph(f"<b>[{q.total_marks} Marks]</b>", ParagraphStyle('MSBannerM', fontName='Poppins-Bold', fontSize=8, textColor=colors.white, alignment=2))
            ]
        ], colWidths=[420, 95])
        q_banner.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), COLOR_NAVY),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(q_banner)
        story.append(Spacer(1, 4))

        ms_data = [
            [
                Paragraph("<b>Part</b>", styles['table_header']),
                Paragraph("<b>Examiner Marking Points / Indicative Content</b>", styles['table_header']),
                Paragraph("<b>Marks</b>", styles['table_header'])
            ]
        ]

        for sq in q.subquestions:
            ms_data.append([
                Paragraph(f"<b>{sq.label}</b>", styles['table_cell_center']),
                Paragraph(sq.mark_scheme if sq.mark_scheme else "Award marks for scientifically valid method.", styles['table_cell']),
                Paragraph(f"<b>[{sq.marks}]</b>", styles['table_cell_center'])
            ])

        t_ms = Table(ms_data, colWidths=[35, 435, 45])
        t_ms.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_BG_LIGHT),
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
            ('BOX', (0, 0), (-1, -1), 0.8, COLOR_NAVY),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ]))
        story.append(t_ms)
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] Built Paper 5 PDF: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == "__main__":
    print("Paper 5 PDF Generation Engine Loaded.")
