"""
Dedicated Mentora Academy A2 MCQ Topic PDF Generator
Builds authentic Cambridge 9701 A Level Chemistry Multiple Choice packs with:
- Poppins typography
- Question badges with difficulty indicators and Cambridge Paper 4/1 reference codes
- 4 clear options (A, B, C, D)
- Embedded high-DPI scientific diagrams
- Quick-Check Answer Key Grid (Q1 to Q110) for rapid self-assessment
- Comprehensive Examiner Explanations & Distractor Analysis
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

NAVY        = HexColor("#0b1b36")
DEEP_NAVY   = HexColor("#132646")
CRIMSON     = HexColor("#a81717")
FOREST_GREEN= HexColor("#15803d")
DARK_TEXT   = HexColor("#20242e")
MUTED_TEXT  = HexColor("#64748b")
LIGHT_BG    = HexColor("#f8f7f5")
ALT_ROW_BG  = HexColor("#f1f5f9")
BORDER_GREY = HexColor("#dcd8d0")
BORDER_LIGHT= HexColor("#e2e8f0")

PAGE_W, PAGE_H = A4
MARGIN_L = 44
MARGIN_R = 44
MARGIN_T = 52
MARGIN_B = 42
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

@dataclass
class A2MCQQuestion:
    number: int
    title: str
    syllabus_ref: str
    difficulty: str  # "EASY" or "HARD"
    stem: str
    options: List[str]  # ["A: ...", "B: ...", "C: ...", "D: ..."]
    correct_answer: str  # "A", "B", "C", or "D"
    explanation: str
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None

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

def draw_header(c, page_type="A Level — Multiple Choice Pack"):
    c.saveState()
    c.setFont("Poppins-Bold", 8.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, PAGE_H - 30, "MENTORA")

    c.setFont("Poppins-Bold", 5.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "ACADEMY", MARGIN_L, PAGE_H - 38, "Poppins-Bold", 5.0, CRIMSON, tracking=1.5)

    right_text = "URWAH · CHEMISTRY — CAMBRIDGE INTERNATIONAL A LEVEL (9701)"
    c.setFont("Poppins-Bold", 5.5)
    c.setFillColor(CRIMSON)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 30, right_text)

    c.setFont("Poppins-Bold", 7.0)
    c.setFillColor(DEEP_NAVY)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 40, page_type)

    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    c.line(MARGIN_L, PAGE_H - 46, PAGE_W - MARGIN_R, PAGE_H - 46)
    c.restoreState()
    return PAGE_H - 54

def draw_footer(c, page_num, topic_label):
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, PAGE_W, 26, fill=1, stroke=0)

    c.setFont("Poppins", 6.2)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, 9, f"MENTORA ACADEMY · Urwah · A Level Multiple Choice Pack — {topic_label}")

    c.drawRightString(PAGE_W - MARGIN_R, 9, str(page_num))
    c.restoreState()

def draw_paragraph(c, text, x, y, width, font='Poppins', size=7.2, color=DARK_TEXT, leading=10.5):
    style = ParagraphStyle('style', fontName=font, fontSize=size, textColor=color, leading=leading)
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
    p = Paragraph(safe, style)
    w, h = p.wrap(width, PAGE_H)
    p.drawOn(c, x, y - h)
    return h

def generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions):
    draw_header(c, page_type="A Level — Multiple Choice Pack")
    y = PAGE_H - 74

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701)", MARGIN_L, y, "Poppins-Bold", 6.5, CRIMSON, tracking=1.2)
    y -= 16

    c.setFont("Poppins-Bold", 14.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, topic_title)
    y -= 13
    c.setFont("Poppins-Medium", 8.0)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, y, "Multiple Choice Master Pack · 100 Core + 10 High-Frequency Core Repeats")
    y -= 24

    box_h = 96
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.setStrokeColor(BORDER_GREY)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN_L, y - box_h, CONTENT_W, box_h, 4, fill=1, stroke=1)

    items = [
        ("CANDIDATE", "Urwah"),
        ("SYLLABUS", "Cambridge International A Level Chemistry (9701)"),
        ("TOPIC COVERAGE", topic_subtitle),
        ("QUESTION COUNT", f"{total_questions} Questions (100 Comprehensive + 10 High-Frequency Repeats)"),
        ("TOTAL MARKS", f"{total_marks} Marks (1 Mark Each · Standardized A Level Scoring)")
    ]

    iy = y - 16
    for label, val in items:
        c.setFont("Poppins-Bold", 5.6)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 12, iy, label)

        c.setFont("Poppins-Bold", 7.4)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 125, iy, val)
        iy -= 17

    c.restoreState()
    y -= (box_h + 24)

    c.setFont("Poppins-Bold", 7.8)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "HOW TO USE THIS A LEVEL MCQ PACK")
    y -= 12

    instructions = [
        "1. Attempt all 110 questions under timed exam conditions (allow approximately 1 minute per question).",
        "2. Record your selected option (A, B, C, or D) for each question clearly.",
        "3. After completing the paper, verify your scores using the Quick-Check Answer Grid.",
        "4. Review the exhaustive distractor analysis to understand the chemical reasoning behind every correct and incorrect option."
    ]
    for inst in instructions:
        h = draw_paragraph(c, inst, MARGIN_L, y, CONTENT_W, size=7.0, leading=10.0)
        y -= (h + 4)

    y -= 12

    c.setFont("Poppins-Bold", 7.8)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "SYLLABUS SUBTOPICS COVERED")
    y -= 12

    for code_name, desc in subtopics_summary:
        c.saveState()
        c.setFont("Poppins-Bold", 6.8)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L, y, "\u25b8")
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN_L + 10, y, code_name)
        c.setFont("Poppins", 6.5)
        c.setFillColor(DARK_TEXT)
        c.drawString(MARGIN_L + 195, y, f"— {desc}")
        c.restoreState()
        y -= 13

    c.saveState()
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, 42, CONTENT_W, 24, 3, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 6.2)
    c.setFillColor(white)
    draw_spaced_text(c, "MENTORA ACADEMY · EXCELLENCE IN CAMBRIDGE A LEVEL ASSESSMENT", MARGIN_L + 20, 51, "Poppins-Bold", 6.2, white, tracking=1.5)
    c.restoreState()

    draw_footer(c, 1, topic_title)
    c.showPage()

def generate_mcq_pages(c, questions, subtopic_map, topic_title):
    page_num = 2
    y = draw_header(c, page_type="A Level — Multiple Choice Pack")
    current_subtopic = None

    for q in questions:
        if q.syllabus_ref != current_subtopic:
            current_subtopic = q.syllabus_ref
            banner_h = 24
            if y - banner_h < MARGIN_B + 60:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="A Level — Multiple Choice Pack")

            title = subtopic_map.get(current_subtopic, f"SUBTOPIC {current_subtopic}")
            c.saveState()
            c.setFillColor(LIGHT_BG)
            c.setStrokeColor(BORDER_GREY)
            c.setLineWidth(0.6)
            c.roundRect(MARGIN_L, y - 16, CONTENT_W, 16, 2, fill=1, stroke=1)
            c.setFont("Poppins-Bold", 6.0)
            c.setFillColor(CRIMSON)
            draw_spaced_text(c, title, MARGIN_L + 8, y - 11, "Poppins-Bold", 6.0, CRIMSON, tracking=0.8)
            c.restoreState()
            y -= 24

        stem_style = ParagraphStyle('stem_s', fontName='Poppins', fontSize=7.2, textColor=DARK_TEXT, leading=10.5)
        p_stem = Paragraph(q.stem.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>"), stem_style)
        sw, sh = p_stem.wrap(CONTENT_W - 28, PAGE_H)

        opt_h = len(q.options) * 12.5
        fig_h = 110 if (q.figure_path and os.path.exists(q.figure_path)) else 0
        total_q_h = 18 + sh + 6 + fig_h + opt_h + 16

        if y - total_q_h < MARGIN_B + 10:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="A Level — Multiple Choice Pack")

        c.saveState()
        c.setFillColor(NAVY)
        c.roundRect(MARGIN_L, y - 14, 18, 14, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 7.0)
        c.setFillColor(white)
        c.drawCentredString(MARGIN_L + 9, y - 10.5, str(q.number))

        c.setFont("Poppins-Bold", 7.0)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 24, y - 10, q.title)

        c.setFont("Poppins-Bold", 5.8)
        diff_color = FOREST_GREEN if q.difficulty == "EASY" else CRIMSON
        c.setFillColor(diff_color)
        c.drawRightString(PAGE_W - MARGIN_R, y - 10, f"{q.difficulty} · Syllabus {q.syllabus_ref}")
        c.restoreState()
        y -= 20

        p_stem.drawOn(c, MARGIN_L + 20, y - sh)
        y -= (sh + 6)

        if q.figure_path and os.path.exists(q.figure_path):
            fw = 200
            fh = 95
            fx = MARGIN_L + (CONTENT_W - fw) / 2
            c.saveState()
            c.drawImage(q.figure_path, fx, y - fh, width=fw, height=fh)
            c.restoreState()
            y -= (fh + 6)

        for opt in q.options:
            c.saveState()
            c.setFont("Poppins", 6.9)
            c.setFillColor(DARK_TEXT)
            c.drawString(MARGIN_L + 30, y - 8, opt)
            c.restoreState()
            y -= 12.5

        y -= 4
        c.saveState()
        c.setStrokeColor(BORDER_LIGHT)
        c.setLineWidth(0.4)
        c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
        c.restoreState()
        y -= 10

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num + 1

def generate_quick_answer_grid(c, questions, start_page, topic_title):
    page_num = start_page
    y = draw_header(c, page_type="Quick-Check Answer Key Grid")

    c.setFont("Poppins-Bold", 10.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y - 6, f"Quick-Check Answer Key Grid — {topic_title}")
    y -= 14

    c.setFont("Poppins-Bold", 5.8)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701) — OFFICIAL ANSWER KEY MATRIX", MARGIN_L, y, "Poppins-Bold", 5.8, CRIMSON, tracking=0.8)
    y -= 18

    cols = 5
    per_col = 22
    col_w = (CONTENT_W - 30) / cols

    for col in range(cols):
        cx = MARGIN_L + col * (col_w + 7.5)
        cy = y

        c.saveState()
        c.setFillColor(NAVY)
        c.roundRect(cx, cy - 14, col_w, 14, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.0)
        c.setFillColor(white)
        c.drawString(cx + 4, cy - 10, "Q#")
        c.drawRightString(cx + col_w - 4, cy - 10, "ANS")
        c.restoreState()
        cy -= 18

        for row in range(per_col):
            idx = col * per_col + row
            if idx < len(questions):
                q = questions[idx]
                c.saveState()
                if row % 2 == 1:
                    c.setFillColor(ALT_ROW_BG)
                    c.rect(cx, cy - 11, col_w, 11, fill=1, stroke=0)

                c.setFont("Poppins-Bold", 6.2)
                c.setFillColor(DARK_TEXT)
                c.drawString(cx + 4, cy - 8.5, f"Q{q.number}")

                c.setFont("Poppins-Bold", 6.5)
                c.setFillColor(CRIMSON)
                c.drawRightString(cx + col_w - 6, cy - 8.5, q.correct_answer)
                c.restoreState()
                cy -= 12

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num + 1

def generate_explanations(c, questions, start_page, topic_title):
    page_num = start_page
    y = draw_header(c, page_type="Comprehensive Explanations & Distractor Analysis")

    c.setFont("Poppins-Bold", 10.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y - 6, f"Explanations & Distractor Analysis — {topic_title}")
    y -= 14

    c.setFont("Poppins-Bold", 5.8)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL A LEVEL CHEMISTRY (9701) — EXAMINER RATIONALE", MARGIN_L, y, "Poppins-Bold", 5.8, CRIMSON, tracking=0.8)
    y -= 18

    for q in questions:
        exp_style = ParagraphStyle('exp_s', fontName='Poppins', fontSize=6.8, textColor=DARK_TEXT, leading=9.5)
        p_exp = Paragraph(q.explanation.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>"), exp_style)
        pw, ph = p_exp.wrap(CONTENT_W - 46, PAGE_H)
        row_h = max(ph + 8, 22)

        if y - row_h < MARGIN_B + 10:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="Comprehensive Explanations & Distractor Analysis")

        c.saveState()
        c.setStrokeColor(BORDER_LIGHT)
        c.setLineWidth(0.4)
        c.line(MARGIN_L, y - row_h, PAGE_W - MARGIN_R, y - row_h)

        c.setFont("Poppins-Bold", 6.2)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 4, y - 12, str(q.number))

        c.setFillColor(NAVY)
        c.roundRect(MARGIN_L + 24, y - 13, 14, 11, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(white)
        c.drawCentredString(MARGIN_L + 31, y - 10.5, q.correct_answer)

        c.setFont("Poppins-Bold", 6.0)
        c.setFillColor(MUTED_TEXT)
        c.drawRightString(PAGE_W - MARGIN_R - 8, y - 12, "[1]")
        c.restoreState()

        p_exp.drawOn(c, MARGIN_L + 46, y - ph - 4)
        y -= row_h

    draw_footer(c, page_num, topic_title)
    c.showPage()

def build_a2_mcq_pdf(output_path: str, topic_title: str, topic_subtitle: str,
                     subtopics_summary: list, subtopic_map: dict,
                     questions: List[A2MCQQuestion]):
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    register_poppins()
    c = canvas.Canvas(output_path, pagesize=A4)
    total_marks = len(questions)
    total_questions = len(questions)

    print(f"Building A2 MCQs {output_path}: {total_questions} questions, {total_marks} marks...")

    generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions)
    next_page = generate_mcq_pages(c, questions, subtopic_map, topic_title)
    next_page = generate_quick_answer_grid(c, questions, next_page, topic_title)
    generate_explanations(c, questions, next_page, topic_title)

    c.save()
    print(f"[SUCCESS] Built A2 MCQ PDF: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == "__main__":
    print("A2 MCQ PDF Generation Engine Loaded.")
