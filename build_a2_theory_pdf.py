"""
Modular Mentora Academy A2 Topical Worksheet Generator (Paper 4 Theory)
Builds authentic Cambridge 9701 A Level Chemistry Paper 4 packs with:
- Poppins typography
- Dark circular question badges
- Embedded publication-quality Matplotlib figures
- Dotted writing lines for answers
- Multi-page mark scheme table
- Candidate: Urwah | Mentora Academy
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

# ── Color Palette ─────────────────────────────────────────────────────────────
NAVY       = HexColor("#0b1b36")
DEEP_NAVY  = HexColor("#132646")
CRIMSON    = HexColor("#a81717")
DARK_TEXT  = HexColor("#20242e")
LIGHT_BG   = HexColor("#f8f7f5")
BORDER_GREY= HexColor("#dcd8d0")
DOTTED_LINE= HexColor("#b0aca4")

PAGE_W, PAGE_H = A4  # 595.28 x 841.89 pt
MARGIN_L = 48
MARGIN_R = 48
MARGIN_T = 54
MARGIN_B = 44
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

@dataclass
class QuestionPart:
    label: str
    text: str
    marks: int
    num_answer_lines: int = 2
    options: List[str] = field(default_factory=list)

@dataclass
class Question:
    number: int
    title: str
    syllabus_ref: str
    difficulty: str  # EASY or HARD
    preamble: str = ""
    parts: List[QuestionPart] = field(default_factory=list)
    mark_scheme: List[dict] = field(default_factory=list)
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None
    section_key: Optional[str] = None

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

def draw_spaced_text(c, text, x, y, font, size, color, tracking=2.0):
    c.saveState()
    c.setFont(font, size)
    c.setFillColor(color)
    cx = x
    for ch in text:
        c.drawString(cx, y, ch)
        cx += c.stringWidth(ch, font, size) + tracking
    c.restoreState()
    return cx - x

def draw_header(c, page_type="Paper 4 — A Level Theory"):
    c.saveState()
    # Left: Academy Logo / Title
    c.setFont("Poppins-Bold", 8.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, PAGE_H - 32, "MENTORA")

    c.setFont("Poppins-Bold", 5.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "ACADEMY", MARGIN_L, PAGE_H - 40, "Poppins-Bold", 5.0, CRIMSON, tracking=1.5)

    # Right: Candidate & Subject metadata
    right_text = "URWAH · CHEMISTRY — CAMBRIDGE INTERNATIONAL A LEVEL (9701)"
    c.setFont("Poppins-Bold", 5.5)
    c.setFillColor(CRIMSON)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 32, right_text)

    c.setFont("Poppins-Bold", 7.0)
    c.setFillColor(DEEP_NAVY)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 42, page_type)

    # Top dividing line
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    c.line(MARGIN_L, PAGE_H - 48, PAGE_W - MARGIN_R, PAGE_H - 48)

    c.restoreState()
    return PAGE_H - 58

def draw_footer(c, page_num, topic_label):
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, PAGE_W, 28, fill=1, stroke=0)

    c.setFont("Poppins", 6.5)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, 10, f"MENTORA ACADEMY · Urwah · A Level Theory Pack (Paper 4) — {topic_label}")

    c.drawRightString(PAGE_W - MARGIN_R, 10, str(page_num))
    c.restoreState()

def draw_paragraph(c, text, x, y, width, font='Poppins', size=7.2, color=DARK_TEXT, leading=10.5):
    style = ParagraphStyle('style', fontName=font, fontSize=size, textColor=color, leading=leading)
    import re
    formatted = text.replace("\n", "<br/>")
    formatted = re.sub(r'&(?!(?:amp|lt|gt|bull|rarr|Delta|times|deg|plusmn|le|ge|middot|infin|rightleftharpoons|harr|#[0-9]+|#x[0-9a-fA-F]+);)', '&amp;', formatted)
    try:
        p = Paragraph(formatted, style)
        w, h = p.wrap(width, PAGE_H)
    except Exception:
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
        p = Paragraph(safe, style)
        w, h = p.wrap(width, PAGE_H)
    p.drawOn(c, x, y - h)
    return h

def draw_dotted_lines(c, x, y, width, count=3, spacing=14):
    c.saveState()
    c.setStrokeColor(DOTTED_LINE)
    c.setLineWidth(0.6)
    c.setDash(1.5, 3.5)
    for i in range(count):
        ly = y - (i * spacing)
        c.line(x, ly, x + width, ly)
    c.restoreState()
    return count * spacing

def generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions):
    draw_header(c, page_type="Paper 4 — A Level Theory Pack")

    y = PAGE_H - 80

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701)", MARGIN_L, y, "Poppins-Bold", 6.5, CRIMSON, tracking=1.2)
    y -= 18

    c.setFont("Poppins-Bold", 15.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, topic_title)
    y -= 14
    c.setFont("Poppins-Medium", 8.5)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, y, "Paper 4 Topical Examination Pack & Comprehensive Examiner Mark Scheme")
    y -= 28

    box_h = 100
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.setStrokeColor(BORDER_GREY)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN_L, y - box_h, CONTENT_W, box_h, 4, fill=1, stroke=1)

    items = [
        ("CANDIDATE", "Urwah"),
        ("SYLLABUS", "Cambridge International A Level Chemistry (9701) — Paper 4"),
        ("TOPIC COVERAGE", topic_subtitle),
        ("COMPONENT", "Paper 4 — A Level Structured Questions (Theory & Calculations)"),
        ("TOTAL MARKS", f"{total_marks} Marks ({total_questions} Comprehensive Questions)")
    ]

    iy = y - 18
    for label, val in items:
        c.setFont("Poppins-Bold", 5.8)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 14, iy, label)

        c.setFont("Poppins-Bold", 7.8)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 130, iy, val)
        iy -= 18

    c.restoreState()
    y -= (box_h + 30)

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "HOW TO USE THIS A LEVEL PAPER 4 PACK")
    y -= 14

    instructions = [
        "1. Complete each structured question thoroughly in the answer spaces provided, adhering strictly to mark allocations.",
        "2. Questions are classified into Core and Advanced tiers, covering multi-step chemical derivations, mechanisms, and numerical proofs.",
        "3. Every question features authentic Cambridge A Level Paper 4 examination references (e.g. 9701/42/M/J/23) for benchmark cross-referencing.",
        "4. Full point-by-point examiner mark schemes with step-by-step working and error-carried-forward (ECF) criteria are detailed at the end."
    ]
    for inst in instructions:
        h = draw_paragraph(c, inst, MARGIN_L, y, CONTENT_W, size=7.2, leading=11)
        y -= (h + 5)

    y -= 15

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "SYLLABUS SUBTOPICS COVERED")
    y -= 14

    for code_name, desc in subtopics_summary:
        c.saveState()
        c.setFont("Poppins-Bold", 7.0)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L, y, "\u25b8")
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN_L + 12, y, code_name)
        c.setFont("Poppins", 6.8)
        c.setFillColor(DARK_TEXT)
        c.drawString(MARGIN_L + 210, y, f"— {desc}")
        c.restoreState()
        y -= 14

    c.saveState()
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, 46, CONTENT_W, 26, 3, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(white)
    draw_spaced_text(c, "MENTORA ACADEMY · EXCELLENCE IN CAMBRIDGE A LEVEL ASSESSMENT", MARGIN_L + 20, 56, "Poppins-Bold", 6.5, white, tracking=1.5)
    c.restoreState()

    draw_footer(c, 1, topic_title)
    c.showPage()

def generate_question_pages(c, questions, subtopic_map, topic_title):
    page_num = 2
    y = draw_header(c, page_type="Paper 4 — A Level Theory Pack")
    current_subtopic = None

    for q in questions:
        banner_key = getattr(q, 'section_key', None) or q.syllabus_ref
        if banner_key != current_subtopic:
            current_subtopic = banner_key
            banner_h = 30
            if y - banner_h < MARGIN_B + 60:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="Paper 4 — A Level Theory Pack")

            title = subtopic_map.get(current_subtopic, f"SUBTOPIC {current_subtopic}")
            c.saveState()
            c.setFillColor(LIGHT_BG)
            c.setStrokeColor(BORDER_GREY)
            c.setLineWidth(0.6)
            c.roundRect(MARGIN_L, y - 20, CONTENT_W, 20, 2, fill=1, stroke=1)
            c.setFont("Poppins-Bold", 6.5)
            c.setFillColor(CRIMSON)
            draw_spaced_text(c, title, MARGIN_L + 10, y - 14, "Poppins-Bold", 6.5, CRIMSON, tracking=1.0)
            c.restoreState()
            y -= 30

        if y < MARGIN_B + 80:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="Paper 4 — A Level Theory Pack")

        c.saveState()
        badge_radius = 8.5
        badge_x = MARGIN_L + badge_radius
        badge_y = y - 4
        c.setFillColor(NAVY)
        c.circle(badge_x, badge_y, badge_radius, fill=1, stroke=0)

        c.setFont("Poppins-Bold", 7.5)
        c.setFillColor(white)
        q_str = str(q.number)
        qw = c.stringWidth(q_str, "Poppins-Bold", 7.5)
        c.drawString(badge_x - (qw / 2), badge_y - 2.8, q_str)

        c.setFont("Poppins-Bold", 7.5)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 24, y - 6, q.title)

        c.setFont("Poppins-Bold", 6.2)
        diff_color = HexColor("#2e7d32") if q.difficulty == "EASY" else CRIMSON
        c.setFillColor(diff_color)
        c.drawRightString(PAGE_W - MARGIN_R, y - 6, f"{q.difficulty}  ·  Syllabus {q.syllabus_ref}")
        c.restoreState()
        y -= 20

        if q.preamble:
            h = draw_paragraph(c, q.preamble, MARGIN_L + 24, y, CONTENT_W - 24, size=7.2, leading=10.5)
            y -= (h + 8)

        if q.figure_path and os.path.exists(q.figure_path):
            fig_w = 260
            fig_h = 135
            fig_x = MARGIN_L + (CONTENT_W - fig_w) / 2

            if y - fig_h - 20 < MARGIN_B:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="Paper 4 — A Level Theory Pack")

            c.saveState()
            c.setStrokeColor(BORDER_GREY)
            c.setFillColor(white)
            c.setLineWidth(0.6)
            c.roundRect(fig_x - 4, y - fig_h - 4, fig_w + 8, fig_h + 8, 3, fill=1, stroke=1)
            c.drawImage(q.figure_path, fig_x, y - fig_h, width=fig_w, height=fig_h)
            c.restoreState()
            y -= (fig_h + 8)

            if q.figure_caption:
                c.saveState()
                c.setFont("Poppins-Italic", 6.2)
                c.setFillColor(DARK_TEXT)
                c.drawCentredString(PAGE_W / 2, y, q.figure_caption)
                c.restoreState()
                y -= 16

        for part in q.parts:
            line_space = part.num_answer_lines * 14
            opt_space = len(part.options) * 12 if part.options else 0
            part_h = 24 + line_space + opt_space

            if y - part_h < MARGIN_B + 10:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="Paper 4 — A Level Theory Pack")

            c.saveState()
            c.setFont("Poppins-Bold", 7.2)
            c.setFillColor(NAVY)
            lbl = part.label if part.label.startswith("(") else f"({part.label})"
            c.drawString(MARGIN_L + 24, y, lbl)

            c.setFillColor(CRIMSON)
            c.drawRightString(PAGE_W - MARGIN_R, y, f"[{part.marks}]")
            c.restoreState()

            text_x = MARGIN_L + 42
            text_w = CONTENT_W - 42 - 28
            th = draw_paragraph(c, part.text, text_x, y, text_w, size=7.2, leading=10.5)
            y -= (th + 6)

            if part.options:
                for opt in part.options:
                    c.saveState()
                    c.setFont("Poppins", 7.0)
                    c.setFillColor(DARK_TEXT)
                    c.drawString(text_x + 8, y, opt)
                    c.restoreState()
                    y -= 12
                y -= 4

            if part.num_answer_lines > 0:
                y -= 4
                dh = draw_dotted_lines(c, text_x, y, text_w + 14, count=part.num_answer_lines, spacing=14)
                y -= (dh + 6)

            y -= 4

        y -= 14

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num + 1

def generate_mark_scheme(c, questions, start_page, topic_title):
    page_num = start_page
    y = draw_header(c, page_type="Paper 4 — Mark Scheme")

    c.setFont("Poppins-Bold", 10.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y - 8, f"Mark Scheme — {topic_title}")
    y -= 16

    c.setFont("Poppins-Bold", 6.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701) — PAPER 4 MARKING CRITERIA", MARGIN_L, y, "Poppins-Bold", 6.0, CRIMSON, tracking=1.0)
    y -= 18

    def draw_ms_header(curr_y):
        c.saveState()
        c.setFillColor(LIGHT_BG)
        c.rect(MARGIN_L, curr_y - 14, CONTENT_W, 16, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 6, curr_y - 9, "Q")
        c.drawString(MARGIN_L + 42, curr_y - 9, "EXAMINER MARKING POINTS / WORKED MATHEMATICAL DERIVATIONS")
        c.drawRightString(PAGE_W - MARGIN_R - 6, curr_y - 9, "MARKS")
        c.setStrokeColor(NAVY)
        c.setLineWidth(0.8)
        c.line(MARGIN_L, curr_y - 14, PAGE_W - MARGIN_R, curr_y - 14)
        c.restoreState()
        return curr_y - 22

    y = draw_ms_header(y)

    for q in questions:
        for item in q.mark_scheme:
            part_label = item.get("part", "").strip("()")
            points = item.get("points", "")
            if isinstance(points, list):
                points = "<br/>".join(str(p) for p in points)
            marks = item.get("marks", 0)

            style = ParagraphStyle('test', fontName='Poppins', fontSize=6.8, leading=9.5)
            p = Paragraph(points, style)
            pw, ph = p.wrap(CONTENT_W - 85, PAGE_H)

            needed = ph + 10
            if y - needed < MARGIN_B + 15:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="Paper 4 — Mark Scheme (Continued)")
                y = draw_ms_header(y)

            q_str = f"{q.number}({part_label})" if part_label else str(q.number)
            c.saveState()
            c.setFont("Poppins-Bold", 6.8)
            c.setFillColor(NAVY)
            c.drawString(MARGIN_L + 6, y, q_str)
            c.restoreState()

            draw_paragraph(c, points, MARGIN_L + 42, y, CONTENT_W - 85, size=6.8, leading=9.5)

            c.saveState()
            c.setFont("Poppins-Bold", 6.8)
            c.setFillColor(CRIMSON)
            c.drawRightString(PAGE_W - MARGIN_R - 6, y, str(marks))
            c.restoreState()

            y -= (ph + 8)

            c.saveState()
            c.setStrokeColor(BORDER_GREY)
            c.setLineWidth(0.4)
            c.line(MARGIN_L, y + 2, PAGE_W - MARGIN_R, y + 2)
            c.restoreState()
            y -= 4

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num

def build_a2_theory_pdf(output_path, topic_title, topic_subtitle, subtopics_summary, subtopic_map, questions):
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    register_poppins()
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle(f"Mentora Academy - Urwah - {topic_title}")
    c.setAuthor("Mentora Academy")

    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_questions = len(questions)

    print(f"Building Paper 4 {output_path}: {total_questions} questions, {total_marks} marks...")

    generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions)
    next_page = generate_question_pages(c, questions, subtopic_map, topic_title)
    generate_mark_scheme(c, questions, next_page, topic_title)

    c.save()
    print(f"[SUCCESS] Built Paper 4 PDF: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == "__main__":
    print("Paper 4 Theory PDF Generation Engine Loaded.")
