"""
AS Chemistry Cambridge — Topical Worksheet PDF Generator
Replicates the Mentora Academy visual design for professional topical worksheets.
"""
import os
from dataclasses import dataclass, field
from typing import List, Optional
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch, mm

# ── Colour Palette (from Mentora Academy design) ──────────────────────────────
NAVY       = HexColor("#0b1b36")
DEEP_NAVY  = HexColor("#132646")
CRIMSON    = HexColor("#a81717")
DARK_TEXT   = HexColor("#20242e")
LIGHT_BG   = HexColor("#f5f3f0")
RULE_GREY  = HexColor("#cccccc")

# ── Page dimensions ───────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4  # 595.9 x 842.9 pts
MARGIN_L = 50
MARGIN_R = 50
MARGIN_T = 70
MARGIN_B = 50
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

# ── Data classes ──────────────────────────────────────────────────────────────
@dataclass
class Config:
    candidate_name: str
    subject: str = "Chemistry — Cambridge International A Level (9701)"
    week_number: int = 1
    topic_area: str = "Physical Chemistry — Topic 1: Atomic Structure"
    date_range: str = "Monday 17 August 2026 – Friday 21 August 2026"
    academy_name: str = "MENTORA ACADEMY"
    total_marks: int = 0
    how_to_use: List[str] = field(default_factory=lambda: [
        "One short set of questions per session, matching that day's topic from the schedule.",
        "Answer in the spaces / on the lines provided. Marks for each part are shown in [brackets].",
        "Mark schemes for the whole week are collected at the end of the pack.",
        "These are original questions written to match Cambridge's exact style and command words — not reproductions of real past paper text."
    ])

@dataclass
class QuestionPart:
    label: str          # "a", "b", "c" etc.
    text: str
    marks: int
    options: List[str] = field(default_factory=list)       # MCQ: ["A ...", "B ...", ...]
    sub_parts: List['QuestionPart'] = field(default_factory=list)

@dataclass
class Question:
    number: int
    title: str
    syllabus_ref: str   # e.g. "1.1" or "1.3"
    parts: List[QuestionPart]
    mark_scheme: List[dict] = field(default_factory=list)  # [{"part": "a", "points": "...", "marks": 2}, ...]
    preamble: str = ""  # Optional intro text before parts

@dataclass
class TopicSection:
    day_label: str      # e.g. "MONDAY · 17 AUG"
    topic_code: str     # e.g. "TOPIC 1.1"
    topic_name: str     # e.g. "PARTICLES IN THE ATOM & ATOMIC RADIUS"
    questions: List[Question] = field(default_factory=list)

# ── Font Registration ─────────────────────────────────────────────────────────
def register_fonts(font_dir):
    font_map = {
        'Poppins':           'Poppins-Regular.ttf',
        'Poppins-Bold':      'Poppins-Bold.ttf',
        'Poppins-SemiBold':  'Poppins-SemiBold.ttf',
        'Poppins-Medium':    'Poppins-Medium.ttf',
        'Poppins-Italic':    'Poppins-Italic.ttf',
        'Poppins-BoldItalic':'Poppins-BoldItalic.ttf',
        'Poppins-Light':     'Poppins-Light.ttf',
    }
    for name, filename in font_map.items():
        path = os.path.join(font_dir, filename)
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path))
        else:
            print(f"⚠ Font not found: {path}")

# ── Helper: letter-spaced text ────────────────────────────────────────────────
def draw_spaced_text(c, text, x, y, font, size, color, spacing=None):
    """Draw text with wide letter-spacing (like CSS letter-spacing)."""
    c.saveState()
    c.setFont(font, size)
    c.setFillColor(color)
    if spacing is None:
        # Default: space between each character equals ~60% of font size
        spacing = size * 0.6
    cx = x
    for ch in text:
        c.drawString(cx, y, ch)
        cx += c.stringWidth(ch, font, size) + spacing
    c.restoreState()
    return cx - x  # total width used

def draw_spaced_string(text, spacing_factor=0.6):
    """Convert 'HELLO' to 'H E L L O' with extra spaces for simple drawString."""
    return (" " * max(1, int(spacing_factor * 2))).join(text)

# ── Helper: wrapped paragraph ─────────────────────────────────────────────────
def draw_paragraph(c, text, x, y, max_width, font='Poppins', size=6.9,
                   color=DARK_TEXT, leading=11, bold_font='Poppins-Bold'):
    """Draw a text paragraph with word wrapping. Returns height consumed."""
    style = ParagraphStyle(
        'body',
        fontName=font,
        fontSize=size,
        textColor=color,
        leading=leading,
        spaceAfter=0,
        spaceBefore=0,
    )
    # Convert basic markup
    safe_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    safe_text = safe_text.replace("\n", "<br/>")
    p = Paragraph(safe_text, style)
    w, h = p.wrap(max_width, PAGE_H)
    p.drawOn(c, x, y - h)
    return h

# ── Header (every page) ──────────────────────────────────────────────────────
def draw_header(c, config):
    """Draw the top header block: MENTORA / A C A D E M Y / subject line."""
    c.saveState()
    top = PAGE_H - 30

    # "MENTORA"
    c.setFont("Poppins-Bold", 8.6)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, top, "MENTORA")

    # "A C A D E M Y"
    top -= 10
    c.setFont("Poppins-Bold", 5.2)
    c.setFillColor(CRIMSON)
    c.drawString(MARGIN_L, top, draw_spaced_string("ACADEMY", 0.5))

    # Subject line: "U R W A H · C H E M I S T R Y — C A M B R I D G E ..."
    top -= 12
    c.setFont("Poppins-Bold", 6.0)
    c.setFillColor(CRIMSON)
    subject_line = f"{config.candidate_name.upper()} · CHEMISTRY — CAMBRIDGE INTERNATIONAL A LEVEL (9701)"
    c.drawString(MARGIN_L, top, draw_spaced_string(subject_line, 0.3))

    # Thin crimson rule
    top -= 6
    c.setStrokeColor(CRIMSON)
    c.setLineWidth(0.6)
    c.line(MARGIN_L, top, PAGE_W - MARGIN_R, top)

    c.restoreState()
    return top - 8  # return Y position below the rule

# ── Footer (every page) ──────────────────────────────────────────────────────
def draw_footer(c, config, page_num, override_text=None):
    """Draw the bottom footer with page number."""
    c.saveState()
    c.setFont("Poppins", 6)
    c.setFillColor(DARK_TEXT)
    if override_text:
        footer = override_text
    else:
        footer = f"{config.academy_name} · {config.candidate_name} · Week {config.week_number} Topical Pack"
    c.drawString(MARGIN_L, 30, footer)
    c.drawRightString(PAGE_W - MARGIN_R, 30, str(page_num))
    c.restoreState()

# ── Section Banner ────────────────────────────────────────────────────────────
def draw_section_banner(c, y, day_label, topic_code, topic_name):
    """Draw a topic day banner like: M O N D A Y · 1 7 A U G — T O P I C 1 . 1 : ..."""
    c.saveState()
    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(CRIMSON)
    banner_text = f"{day_label} — {topic_code}: {topic_name}"
    c.drawString(MARGIN_L, y, draw_spaced_string(banner_text.upper(), 0.25))
    c.restoreState()
    return y - 20

# ── Cover Page ────────────────────────────────────────────────────────────────
def generate_cover_page(c, config, topics):
    """Generate the first (cover) page of the worksheet pack."""
    y = draw_header(c, config)

    # "Question Pack" or "Weekly Topical Worksheet Pack"
    y -= 10
    c.setFont("Poppins-Bold", 7.1)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN_L, y, "Weekly Topical Worksheet Pack")

    # ── Info box area ──
    y -= 35
    box_x = MARGIN_L
    box_w = CONTENT_W

    # Light background rectangle
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.roundRect(box_x, y - 90, box_w, 110, 4, fill=1, stroke=0)
    c.restoreState()

    # CANDIDATE
    y -= 5
    c.setFont("Poppins-Bold", 5.6)
    c.setFillColor(CRIMSON)
    c.drawString(box_x + 15, y, draw_spaced_string("CANDIDATE", 0.4))
    y -= 16
    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(DEEP_NAVY)
    c.drawString(box_x + 15, y, config.candidate_name)

    # SUBJECT
    y -= 22
    c.setFont("Poppins-Bold", 5.6)
    c.setFillColor(CRIMSON)
    c.drawString(box_x + 15, y, draw_spaced_string("SUBJECT", 0.4))
    y -= 16
    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(DEEP_NAVY)
    c.drawString(box_x + 15, y, config.subject)

    # TOTAL MARKS
    y -= 22
    c.setFont("Poppins-Bold", 5.6)
    c.setFillColor(CRIMSON)
    c.drawString(box_x + 15, y, draw_spaced_string("TOTAL MARKS (WEEK)", 0.4))
    y -= 16
    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(DEEP_NAVY)
    c.drawString(box_x + 15, y, f"{config.total_marks} marks")

    # ── HOW TO USE THIS PACK ──
    y -= 40
    c.setFont("Poppins-Bold", 7.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "HOW TO USE THIS PACK")
    y -= 15

    for line in config.how_to_use:
        h = draw_paragraph(c, line, MARGIN_L, y, CONTENT_W, size=6.9, leading=10)
        y -= (h + 5)

    # ── THIS WEEK AT A GLANCE ──
    y -= 15
    c.setFont("Poppins-Bold", 7.2)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN_L, y, "THIS WEEK AT A GLANCE")
    y -= 15

    for topic in topics:
        c.saveState()
        c.setFont("Poppins", 6.8)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L, y, "\u25b8")  # ▸ triangle bullet
        c.setFillColor(DARK_TEXT)
        total = sum(sum(p.marks for p in q.parts) for q in topic.questions)
        glance = f"{topic.day_label} — {topic.topic_code}: {topic.topic_name} ({total} marks)"
        c.drawString(MARGIN_L + 12, y, glance)
        c.restoreState()
        y -= 14

    # ── Bottom block ──
    y -= 25
    c.setFont("Poppins-Bold", 5.6)
    c.setFillColor(CRIMSON)
    c.drawString(MARGIN_L, y, f"{config.academy_name} · EXCELLENCE IN EDUCATION.")

    y -= 22
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.roundRect(MARGIN_L, y - 35, CONTENT_W, 40, 4, fill=1, stroke=0)
    c.restoreState()

    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(CRIMSON)
    c.drawString(MARGIN_L + 15, y, draw_spaced_string(f"TOPICAL PRACTICE — WEEK {config.week_number}", 0.3))
    y -= 14
    c.setFont("Poppins-Bold", 7.5)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN_L + 15, y, config.topic_area)
    y -= 12
    c.setFont("Poppins", 6.5)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L + 15, y, config.date_range)

    draw_footer(c, config, 1, f"{config.academy_name} · {config.candidate_name} · Week {config.week_number} Topical Pack")
    c.showPage()

# ── Question Pages ────────────────────────────────────────────────────────────
def generate_question_pages(c, topics, config, start_page=2):
    """Generate all question pages. Returns next available page number."""
    page_num = start_page
    current_section_label = "Question Pack"

    for topic in topics:
        # Start topic — may or may not start new page
        y = draw_header(c, config)

        # Section type label
        c.setFont("Poppins-Bold", 7.1)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN_L, y - 5, current_section_label)
        y -= 25

        # Topic banner
        y = draw_section_banner(c, y, topic.day_label, topic.topic_code, topic.topic_name)

        for qi, q in enumerate(topic.questions):
            # Check if we need a new page (leave room for at least question header + 1 part)
            needed = 80  # minimum space for a question
            if y < MARGIN_B + needed:
                draw_footer(c, config, page_num)
                c.showPage()
                page_num += 1
                y = draw_header(c, config)
                c.setFont("Poppins-Bold", 7.1)
                c.setFillColor(DEEP_NAVY)
                c.drawString(MARGIN_L, y - 5, current_section_label)
                y -= 25

            # Question number (large bold)
            c.saveState()
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(NAVY)
            c.drawString(MARGIN_L, y, str(q.number))
            c.restoreState()

            # Question title + syllabus ref
            c.saveState()
            c.setFont("Poppins-Bold", 7.5)
            c.setFillColor(NAVY)
            c.drawString(MARGIN_L + 25, y + 1, q.title)
            c.setFont("Poppins", 7.0)
            c.setFillColor(DARK_TEXT)
            title_w = c.stringWidth(q.title, "Poppins-Bold", 7.5)
            c.drawString(MARGIN_L + 25 + title_w + 15, y + 1, f"Syllabus {q.syllabus_ref}")
            c.restoreState()
            y -= 16

            # Preamble text (if any)
            if q.preamble:
                h = draw_paragraph(c, q.preamble, MARGIN_L + 25, y, CONTENT_W - 25, size=6.9, leading=10)
                y -= (h + 8)

            # Parts
            for part in q.parts:
                if y < MARGIN_B + 40:
                    draw_footer(c, config, page_num)
                    c.showPage()
                    page_num += 1
                    y = draw_header(c, config)
                    c.setFont("Poppins-Bold", 7.1)
                    c.setFillColor(DEEP_NAVY)
                    c.drawString(MARGIN_L, y - 5, current_section_label)
                    y -= 25

                # Part label "(a)"
                c.saveState()
                c.setFont("Poppins-Bold", 6.9)
                c.setFillColor(NAVY)
                c.drawString(MARGIN_L + 25, y, f"({part.label})")
                c.restoreState()

                # Part text
                text_x = MARGIN_L + 48
                text_w = CONTENT_W - 48 - 30  # leave room for [marks] on right
                h = draw_paragraph(c, part.text, text_x, y, text_w, size=6.9, leading=10)

                # Mark allocation [n]
                c.saveState()
                c.setFont("Poppins-Bold", 6.9)
                c.setFillColor(NAVY)
                c.drawRightString(PAGE_W - MARGIN_R, y, f"[{part.marks}]")
                c.restoreState()

                y -= (h + 6)

                # MCQ options
                if part.options:
                    for opt in part.options:
                        if y < MARGIN_B + 20:
                            draw_footer(c, config, page_num)
                            c.showPage()
                            page_num += 1
                            y = draw_header(c, config)
                            c.setFont("Poppins-Bold", 7.1)
                            c.setFillColor(DEEP_NAVY)
                            c.drawString(MARGIN_L, y - 5, current_section_label)
                            y -= 25
                        c.saveState()
                        c.setFont("Poppins", 6.9)
                        c.setFillColor(DARK_TEXT)
                        c.drawString(text_x + 10, y, opt)
                        c.restoreState()
                        y -= 12

                # Sub-parts
                for sp in part.sub_parts:
                    if y < MARGIN_B + 30:
                        draw_footer(c, config, page_num)
                        c.showPage()
                        page_num += 1
                        y = draw_header(c, config)
                        y -= 25
                    c.saveState()
                    c.setFont("Poppins-Bold", 6.9)
                    c.setFillColor(NAVY)
                    c.drawString(text_x, y, f"({sp.label})")
                    c.restoreState()
                    sp_h = draw_paragraph(c, sp.text, text_x + 22, y, text_w - 22, size=6.9, leading=10)
                    c.saveState()
                    c.setFont("Poppins-Bold", 6.9)
                    c.setFillColor(NAVY)
                    c.drawRightString(PAGE_W - MARGIN_R, y, f"[{sp.marks}]")
                    c.restoreState()
                    y -= (sp_h + 6)

                y -= 4  # extra gap between parts

            y -= 12  # gap between questions

        draw_footer(c, config, page_num)
        c.showPage()
        page_num += 1

    return page_num

# ── Mark Scheme Pages ─────────────────────────────────────────────────────────
def generate_mark_scheme(c, topics, config, start_page):
    """Generate mark scheme section. Returns next page number."""
    page_num = start_page
    y = draw_header(c, config)

    # Section type label
    c.setFont("Poppins-Bold", 7.1)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN_L, y - 5, "Mark Scheme")
    y -= 25

    # Banner
    c.saveState()
    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(CRIMSON)
    banner = f"MARK SCHEME — WEEK {config.week_number}"
    c.drawString(MARGIN_L, y, draw_spaced_string(banner, 0.25))
    c.restoreState()
    y -= 20

    # Table header
    c.saveState()
    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "Q")
    c.drawString(MARGIN_L + 40, y, "MARKING POINTS")
    c.drawRightString(PAGE_W - MARGIN_R, y, "MARKS")
    c.restoreState()
    y -= 5
    c.setStrokeColor(RULE_GREY)
    c.setLineWidth(0.4)
    c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
    y -= 12

    continued = False
    for topic in topics:
        for q in topic.questions:
            for ms_entry in q.mark_scheme:
                part_label = ms_entry.get("part", "")
                points = ms_entry.get("points", "")
                marks = ms_entry.get("marks", 0)

                # Check space
                if y < MARGIN_B + 40:
                    draw_footer(c, config, page_num)
                    c.showPage()
                    page_num += 1
                    y = draw_header(c, config)
                    c.setFont("Poppins-Bold", 7.1)
                    c.setFillColor(DEEP_NAVY)
                    c.drawString(MARGIN_L, y - 5, "Mark Scheme")
                    y -= 25
                    c.saveState()
                    c.setFont("Poppins-Bold", 6.5)
                    c.setFillColor(CRIMSON)
                    cont_banner = f"MARK SCHEME — WEEK {config.week_number} (CONTINUED)"
                    c.drawString(MARGIN_L, y, draw_spaced_string(cont_banner, 0.25))
                    c.restoreState()
                    y -= 20
                    # Re-draw table header
                    c.saveState()
                    c.setFont("Poppins-Bold", 6.5)
                    c.setFillColor(NAVY)
                    c.drawString(MARGIN_L, y, "Q")
                    c.drawString(MARGIN_L + 40, y, "MARKING POINTS")
                    c.drawRightString(PAGE_W - MARGIN_R, y, "MARKS")
                    c.restoreState()
                    y -= 5
                    c.setStrokeColor(RULE_GREY)
                    c.setLineWidth(0.4)
                    c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
                    y -= 12

                # Question number + part
                q_label = f"{q.number}({part_label})" if part_label else str(q.number)
                c.saveState()
                c.setFont("Poppins-Bold", 6.9)
                c.setFillColor(NAVY)
                c.drawString(MARGIN_L, y, q_label)
                c.restoreState()

                # Marking points text
                h = draw_paragraph(c, points, MARGIN_L + 40, y, CONTENT_W - 80, size=6.9, leading=10)

                # Marks value
                c.saveState()
                c.setFont("Poppins", 6.9)
                c.setFillColor(DARK_TEXT)
                c.drawRightString(PAGE_W - MARGIN_R, y, str(marks))
                c.restoreState()

                y -= (h + 8)

            # Light rule between questions
            y -= 2
            c.setStrokeColor(RULE_GREY)
            c.setLineWidth(0.3)
            c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
            y -= 8

    draw_footer(c, config, page_num)
    c.showPage()
    return page_num + 1

# ── Main Generator ────────────────────────────────────────────────────────────
def generate_worksheet(output_path, config, topics, font_dir=None):
    """Generate the complete worksheet PDF."""
    if font_dir:
        register_fonts(font_dir)

    # Auto-calculate total marks
    if config.total_marks == 0:
        config.total_marks = sum(
            sum(p.marks for p in q.parts)
            for t in topics for q in t.questions
        )

    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle(f"{config.academy_name} - {config.candidate_name} - Week {config.week_number}")
    c.setAuthor(config.academy_name)

    generate_cover_page(c, config, topics)
    next_page = generate_question_pages(c, topics, config, start_page=2)
    generate_mark_scheme(c, topics, config, start_page=next_page)

    c.save()
    print(f"[OK] Generated: {output_path}")
    print(f"  Pages: {next_page + 1}")  # approximate
    print(f"  Total marks: {config.total_marks}")
    return output_path


# ── TEST / DEMO ───────────────────────────────────────────────────────────────
def create_test_pdf():
    """Generate a sample PDF to verify layout."""
    font_dir = r"z:\tests n quizes63\books\psycology\new styl\fonts"
    register_fonts(font_dir)

    config = Config(
        candidate_name="Urwah",
        week_number=1,
        topic_area="Physical Chemistry — Topic 1: Atomic Structure",
        date_range="Monday 17 August 2026 – Friday 21 August 2026",
    )

    topics = [
        TopicSection(
            day_label="MONDAY · 17 AUG",
            topic_code="TOPIC 1.1",
            topic_name="PARTICLES IN THE ATOM & ATOMIC RADIUS",
            questions=[
                Question(
                    number=1,
                    title="Multiple Choice",
                    syllabus_ref="1.1",
                    preamble="For each question, put a cross in the box next to your chosen answer.",
                    parts=[
                        QuestionPart(
                            label="a",
                            text="Which particle has a relative charge of +1 and is found in the nucleus?",
                            marks=1,
                            options=[
                                "A electron",
                                "B neutron",
                                "C proton",
                                "D positron"
                            ]
                        ),
                        QuestionPart(
                            label="b",
                            text="An atom has proton number 15 and nucleon number 31. How many neutrons does it contain?",
                            marks=1,
                            options=[
                                "A 15",
                                "B 16",
                                "C 31",
                                "D 46"
                            ]
                        ),
                    ],
                    mark_scheme=[
                        {"part": "a", "points": "C (proton has relative charge +1 and is found in the nucleus)", "marks": 1},
                        {"part": "b", "points": "B (31 - 15 = 16 neutrons)", "marks": 1},
                    ]
                ),
                Question(
                    number=2,
                    title="Sub-Atomic Particles",
                    syllabus_ref="1.1",
                    preamble="Complete the table to show the relative charge and relative mass of each sub-atomic particle.",
                    parts=[
                        QuestionPart(
                            label="a",
                            text="State the relative charge and relative mass of a proton, neutron, and electron.",
                            marks=3,
                        ),
                    ],
                    mark_scheme=[
                        {"part": "a", "points": "Proton: charge +1, mass 1; Neutron: charge 0, mass 1; Electron: charge -1, mass 1/1840 (or negligible). 1 mark per correct row.", "marks": 3},
                    ]
                ),
                Question(
                    number=3,
                    title="Behaviour in an Electric Field",
                    syllabus_ref="1.1",
                    preamble="A beam containing protons, neutrons and electrons is passed through a uniform electric field created by two charged parallel plates.",
                    parts=[
                        QuestionPart(
                            label="a",
                            text="Describe and explain what happens to the protons as they pass through the field.",
                            marks=2,
                        ),
                        QuestionPart(
                            label="b",
                            text="Explain why the neutrons are undeflected.",
                            marks=1,
                        ),
                    ],
                    mark_scheme=[
                        {"part": "a", "points": "Protons are deflected towards the negative plate (1); because they have a positive charge and are attracted to the oppositely charged plate (1).", "marks": 2},
                        {"part": "b", "points": "Neutrons have no charge / are electrically neutral, so there is no electrostatic force acting on them (1).", "marks": 1},
                    ]
                ),
            ]
        ),
        TopicSection(
            day_label="TUESDAY · 18 AUG",
            topic_code="TOPIC 1.2",
            topic_name="ISOTOPES",
            questions=[
                Question(
                    number=4,
                    title="Defining & Representing Isotopes",
                    syllabus_ref="1.2",
                    parts=[
                        QuestionPart(
                            label="a",
                            text="Define the term isotope.",
                            marks=2,
                        ),
                        QuestionPart(
                            label="b",
                            text="Chlorine exists as two isotopes. Using the correct notation, write the full isotopic symbol for chlorine-35 and chlorine-37.",
                            marks=2,
                        ),
                    ],
                    mark_scheme=[
                        {"part": "a", "points": "Atoms of the same element (same number of protons / same proton number) (1); with different numbers of neutrons (different nucleon number / mass number) (1).", "marks": 2},
                        {"part": "b", "points": "Correct isotopic notation showing mass number and atomic number for both Cl-35 and Cl-37 (1 mark each).", "marks": 2},
                    ]
                ),
            ]
        ),
    ]

    output_path = r"z:\tests n quizes63\books\psycology\new styl\test_output.pdf"
    generate_worksheet(output_path, config, topics, font_dir)


if __name__ == "__main__":
    create_test_pdf()
