"""
Dedicated Mentora Academy MCQ Topic PDF Generator
Builds authentic Cambridge 9701 Chemistry Paper 1 (Multiple Choice) packs with:
- Poppins typography
- Clean question badges with difficulty indicators and Cambridge Paper 1 codes
- 4 clear options (A, B, C, D)
- Embedded high-DPI scientific diagrams
- Quick-Check Answer Key Grid (Q1 to Q100) for rapid self-assessment
- Comprehensive Examiner Explanations & Distractor Analysis
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

PAGE_W, PAGE_H = A4  # 595.28 x 841.89 pt
MARGIN_L = 44
MARGIN_R = 44
MARGIN_T = 52
MARGIN_B = 42
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

@dataclass
class MCQQuestion:
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

def draw_header(c, page_type="Paper 1 — Multiple Choice"):
    c.saveState()
    # Left: Academy Logo / Title
    c.setFont("Poppins-Bold", 8.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, PAGE_H - 30, "MENTORA")

    c.setFont("Poppins-Bold", 5.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "ACADEMY", MARGIN_L, PAGE_H - 38, "Poppins-Bold", 5.0, CRIMSON, tracking=1.5)

    # Right: Candidate & Subject metadata
    right_text = "URWAH · CHEMISTRY — CAMBRIDGE INTERNATIONAL A LEVEL (9701)"
    c.setFont("Poppins-Bold", 5.5)
    c.setFillColor(CRIMSON)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 30, right_text)

    c.setFont("Poppins-Bold", 6.8)
    c.setFillColor(DEEP_NAVY)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 40, page_type)

    # Top dividing line
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    c.line(MARGIN_L, PAGE_H - 46, PAGE_W - MARGIN_R, PAGE_H - 46)

    c.restoreState()
    return PAGE_H - 56

def draw_footer(c, page_num, topic_label):
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, PAGE_W, 26, fill=1, stroke=0)

    c.setFont("Poppins", 6.2)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, 9, f"MENTORA ACADEMY · Urwah · Paper 1 MCQ Pack — {topic_label}")

    c.drawRightString(PAGE_W - MARGIN_R, 9, str(page_num))
    c.restoreState()

def draw_paragraph(c, text, x, y, width, font='Poppins', size=7.2, color=DARK_TEXT, leading=10.2):
    style = ParagraphStyle('style', fontName=font, fontSize=size, textColor=color, leading=leading)
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
    p = Paragraph(safe, style)
    w, h = p.wrap(width, PAGE_H)
    p.drawOn(c, x, y - h)
    return h

def generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions):
    draw_header(c, page_type="Paper 1 (Multiple Choice) Pack")

    y = PAGE_H - 76

    # Title Banner
    c.setFont("Poppins-Bold", 6.5)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL AS & A LEVEL CHEMISTRY (9701)", MARGIN_L, y, "Poppins-Bold", 6.5, CRIMSON, tracking=1.2)
    y -= 16

    c.setFont("Poppins-Bold", 14.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, topic_title)
    y -= 14
    c.setFont("Poppins-Medium", 8.2)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, y, f"Paper 1 (Multiple Choice) Topical Past Paper Pack · {total_questions} Questions & Detailed Solutions")
    y -= 26

    # Metadata Container Box
    box_h = 100
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.setStrokeColor(BORDER_GREY)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN_L, y - box_h, CONTENT_W, box_h, 4, fill=1, stroke=1)

    items = [
        ("CANDIDATE", "Urwah"),
        ("SYLLABUS", "Cambridge International AS Level Chemistry (9701)"),
        ("COMPONENT", "Paper 1: Multiple Choice (1 Hour 15 Minutes Exam Standard)"),
        ("TOPIC COVERAGE", topic_subtitle),
        ("TOTAL VOLUME", f"{total_questions} Authentic Multiple Choice Questions ({total_marks} Marks · 1 Mark Each)")
    ]

    iy = y - 18
    for label, val in items:
        c.setFont("Poppins-Bold", 5.6)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 14, iy, label)

        c.setFont("Poppins-Bold", 7.5)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 125, iy, val)
        iy -= 18

    c.restoreState()
    y -= (box_h + 24)

    # HOW TO USE THIS PACK
    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "HOW TO USE THIS PAPER 1 MCQ PACK")
    y -= 12

    instructions = [
        "1. Timing & Strategy: Spend approximately 1 minute to 1 minute 15 seconds per question under timed test conditions.",
        "2. Answering: For each question, select the one correct option from A, B, C, or D. Apply the elimination method to rule out obvious distractors.",
        "3. Authentic Exam Codes: Every question features authentic Cambridge reference codes (e.g. 9701/12/M/J/23) for cross-study verification.",
        f"4. Quick-Check Answer Grid: Use the {total_questions}-question matrix immediately following the questions for rapid scoring in under 60 seconds.",
        "5. Comprehensive Explanations: Review the detailed examiner rationale and distractor analysis at the back to eliminate conceptual errors."
    ]
    for inst in instructions:
        h = draw_paragraph(c, inst, MARGIN_L, y, CONTENT_W, size=7.0, leading=10.0)
        y -= (h + 4)

    y -= 10

    # SYLLABUS SUBTOPICS COVERED
    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "SYLLABUS SUBTOPICS COVERED IN THIS PACK")
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
        c.drawString(MARGIN_L + 180, y, f"— {desc}")
        c.restoreState()
        y -= 12

    # Bottom Academy Banner
    c.saveState()
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, 42, CONTENT_W, 24, 3, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 6.2)
    c.setFillColor(white)
    draw_spaced_text(c, "MENTORA ACADEMY · EXCELLENCE IN CAMBRIDGE ASSESSMENT", MARGIN_L + 20, 51, "Poppins-Bold", 6.2, white, tracking=1.5)
    c.restoreState()

    draw_footer(c, 1, topic_title)
    c.showPage()

def generate_mcq_pages(c, questions: List[MCQQuestion], subtopic_map: dict, topic_title: str):
    page_num = 2
    y = draw_header(c, page_type="Paper 1 — Multiple Choice")

    current_subtopic = None

    for q in questions:
        # Estimate height needed for this MCQ
        # Header (14 pt) + Stem (~12-30 pt) + 4 Options (4 * 12 pt = 48 pt) + Figure (if any: ~110 pt) + padding (10 pt)
        stem_style = ParagraphStyle('stem_calc', fontName='Poppins', fontSize=7.2, leading=10.2)
        safe_stem = q.stem.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
        p_stem = Paragraph(safe_stem, stem_style)
        sw, sh = p_stem.wrap(CONTENT_W - 20, PAGE_H)

        options_h = 0
        for opt in q.options:
            safe_opt = opt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            p_opt = Paragraph(safe_opt, stem_style)
            ow, oh = p_opt.wrap(CONTENT_W - 35, PAGE_H)
            options_h += max(oh, 11) + 2

        fig_h = 105 if (q.figure_path and os.path.exists(q.figure_path)) else 0
        banner_h = 24 if (q.syllabus_ref != current_subtopic) else 0

        total_q_h = 18 + sh + fig_h + options_h + 20 + banner_h

        # Page break check
        if y - total_q_h < MARGIN_B + 10:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="Paper 1 — Multiple Choice")

        # Subtopic banner if changed
        if q.syllabus_ref != current_subtopic:
            current_subtopic = q.syllabus_ref
            title = subtopic_map.get(current_subtopic, f"SUBTOPIC {current_subtopic}")

            c.saveState()
            c.setFillColor(LIGHT_BG)
            c.setStrokeColor(BORDER_GREY)
            c.setLineWidth(0.6)
            c.roundRect(MARGIN_L, y - 18, CONTENT_W, 18, 2, fill=1, stroke=1)
            c.setFont("Poppins-Bold", 6.2)
            c.setFillColor(CRIMSON)
            draw_spaced_text(c, title, MARGIN_L + 10, y - 13, "Poppins-Bold", 6.2, CRIMSON, tracking=1.0)
            c.restoreState()
            y -= 26

        # Draw Question Header
        c.saveState()
        # Question Number badge
        badge_w = 18 if q.number >= 100 else 16
        c.setFillColor(CRIMSON if q.number > 100 else NAVY)
        c.roundRect(MARGIN_L, y - 11, badge_w, 11, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.2 if q.number >= 100 else 6.5)
        c.setFillColor(white)
        c.drawCentredString(MARGIN_L + badge_w / 2, y - 8.5, str(q.number))

        # Difficulty Badge
        diff_col = FOREST_GREEN if q.difficulty == "EASY" else CRIMSON
        c.setFont("Poppins-Bold", 5.5)
        c.setFillColor(diff_col)
        c.drawString(MARGIN_L + badge_w + 6, y - 8.5, f"[{q.difficulty}]")

        # High-Frequency badge if Q > 100
        extra_w = 0
        if q.number > 100:
            c.setFillColor(CRIMSON)
            c.drawString(MARGIN_L + badge_w + 40, y - 8.5, "[HIGH-FREQUENCY EXAM REPEAT]")
            extra_w = 110

        # Title / Past Paper Code
        c.setFont("Poppins-Medium", 6.5)
        c.setFillColor(MUTED_TEXT)
        c.drawString(MARGIN_L + badge_w + 38 + extra_w, y - 8.5, q.title)

        # Mark Indicator
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(NAVY)
        c.drawRightString(PAGE_W - MARGIN_R, y - 8.5, "[1]")
        c.restoreState()
        y -= 15

        # Draw Stem
        stem_h = draw_paragraph(c, q.stem, MARGIN_L + 4, y, CONTENT_W - 8, size=7.2, leading=10.5)
        y -= (stem_h + 6)

        # Draw Figure if present
        if q.figure_path and os.path.exists(q.figure_path):
            try:
                img_w = 260
                img_h = 88
                img_x = MARGIN_L + (CONTENT_W - img_w) / 2
                c.drawImage(q.figure_path, img_x, y - img_h, width=img_w, height=img_h, preserveAspectRatio=True)
                y -= (img_h + 3)
                if q.figure_caption:
                    c.setFont("Poppins-Italic", 5.8)
                    c.setFillColor(MUTED_TEXT)
                    c.drawCentredString(PAGE_W / 2, y, q.figure_caption)
                    y -= 9
            except Exception:
                pass

        # Draw Options (A, B, C, D)
        for opt in q.options:
            # Parse letter prefix
            opt_letter = opt[:1] if len(opt) > 0 else ""
            opt_text = opt[3:] if len(opt) > 3 and opt[1:3] == ": " else opt

            c.saveState()
            # Option letter badge
            c.setFont("Poppins-Bold", 6.5)
            c.setFillColor(DEEP_NAVY)
            c.drawString(MARGIN_L + 14, y - 8.5, f"[{opt_letter}]")

            # Option text
            c.restoreState()
            opt_h = draw_paragraph(c, opt_text, MARGIN_L + 34, y, CONTENT_W - 40, size=7.0, leading=10.0)
            y -= (max(opt_h, 11) + 4)

        # Subtle divider rule between questions with comfortable breathing room
        c.saveState()
        c.setStrokeColor(HexColor("#e2e8f0"))
        c.setLineWidth(0.5)
        c.line(MARGIN_L, y - 5, PAGE_W - MARGIN_R, y - 5)
        c.restoreState()
        y -= 14  # Inter-question spacing

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num + 1

def generate_quick_answer_grid(c, questions: List[MCQQuestion], start_page: int, topic_title: str):
    y = draw_header(c, page_type="Quick-Check Answer Key")

    # Banner
    c.saveState()
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, y - 22, CONTENT_W, 22, 2, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 7.5)
    c.setFillColor(white)
    draw_spaced_text(c, f"QUICK-CHECK ANSWER KEY GRID (Q1 – Q{len(questions)})", MARGIN_L + 14, y - 15, "Poppins-Bold", 7.5, white, tracking=1.2)
    c.restoreState()
    y -= 30

    c.setFont("Poppins", 6.8)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, y, f"Official Cambridge 9701 Paper 1 Marking Matrix · 1 Mark Per Question · Total Marks: {len(questions)}")
    y -= 14

    # Render main 5-column x 20-row table for Q1-100
    num_cols = 5
    rows_per_col = 20
    col_w = CONTENT_W / num_cols
    table_top = y
    row_h = 15

    for col_idx in range(num_cols):
        cx = MARGIN_L + col_idx * col_w
        # Column header
        c.saveState()
        c.setFillColor(LIGHT_BG)
        c.setStrokeColor(BORDER_GREY)
        c.setLineWidth(0.6)
        c.rect(cx, table_top - 15, col_w, 15, fill=1, stroke=1)
        c.setFont("Poppins-Bold", 6.0)
        c.setFillColor(CRIMSON)
        start_q = col_idx * rows_per_col + 1
        end_q = (col_idx + 1) * rows_per_col
        c.drawCentredString(cx + col_w / 2, table_top - 10.5, f"Q{start_q} – Q{end_q}")
        c.restoreState()

        # Rows
        for r in range(rows_per_col):
            q_num = col_idx * rows_per_col + r + 1
            if q_num <= len(questions):
                q_obj = questions[q_num - 1]
                ry = table_top - 15 - (r + 1) * row_h

                # Alternating row background
                if r % 2 == 1:
                    c.saveState()
                    c.setFillColor(ALT_ROW_BG)
                    c.rect(cx, ry, col_w, row_h, fill=1, stroke=0)
                    c.restoreState()

                # Cell border
                c.saveState()
                c.setStrokeColor(BORDER_LIGHT)
                c.setLineWidth(0.4)
                c.rect(cx, ry, col_w, row_h, fill=0, stroke=1)

                # Question label
                c.setFont("Poppins-Bold", 6.0)
                c.setFillColor(DARK_TEXT)
                c.drawString(cx + 8, ry + 4.0, f"Q{q_num:02d}")

                # Answer badge
                c.setFillColor(NAVY)
                c.roundRect(cx + col_w - 24, ry + 2.0, 16, 11, 2, fill=1, stroke=0)
                c.setFont("Poppins-Bold", 6.5)
                c.setFillColor(white)
                c.drawCentredString(cx + col_w - 16, ry + 4.5, q_obj.correct_answer)
                c.restoreState()

    y = table_top - 15 - rows_per_col * row_h - 14

    # High-Frequency Questions Grid (Q101 - Q110) if present
    if len(questions) > 100:
        c.saveState()
        c.setFillColor(CRIMSON)
        c.roundRect(MARGIN_L, y - 16, CONTENT_W, 16, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(white)
        draw_spaced_text(c, "FREQUENTLY EXAMINED CORE QUESTIONS (Q101 – Q110)", MARGIN_L + 12, y - 11.5, "Poppins-Bold", 6.5, white, tracking=1.0)
        c.restoreState()
        y -= 22

        extra_count = len(questions) - 100
        ex_col_w = CONTENT_W / extra_count
        ex_top = y

        for e_idx in range(extra_count):
            q_num = 101 + e_idx
            q_obj = questions[q_num - 1]
            ex_x = MARGIN_L + e_idx * ex_col_w

            # Cell
            c.saveState()
            c.setFillColor(ALT_ROW_BG)
            c.setStrokeColor(CRIMSON)
            c.setLineWidth(0.6)
            c.rect(ex_x, ex_top - 20, ex_col_w, 20, fill=1, stroke=1)

            c.setFont("Poppins-Bold", 5.8)
            c.setFillColor(CRIMSON)
            c.drawCentredString(ex_x + ex_col_w / 2, ex_top - 8, f"Q{q_num}")

            c.setFillColor(CRIMSON)
            c.roundRect(ex_x + ex_col_w / 2 - 8, ex_top - 19, 16, 10, 2, fill=1, stroke=0)
            c.setFont("Poppins-Bold", 6.2)
            c.setFillColor(white)
            c.drawCentredString(ex_x + ex_col_w / 2, ex_top - 16.5, q_obj.correct_answer)
            c.restoreState()
    draw_footer(c, start_page, topic_title)
    c.showPage()
    return start_page + 1

def generate_explanations(c, questions: List[MCQQuestion], start_page: int, topic_title: str):
    page_num = start_page
    y = draw_header(c, page_type="Comprehensive Explanatory Guide")

    # Banner
    c.saveState()
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, y - 20, CONTENT_W, 20, 2, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 7.0)
    c.setFillColor(white)
    draw_spaced_text(c, "COMPREHENSIVE EXAMINER EXPLANATIONS & DISTRACTOR ANALYSIS", MARGIN_L + 12, y - 14, "Poppins-Bold", 7.0, white, tracking=1.0)
    c.restoreState()
    y -= 28

    # Table Header
    def draw_exp_header(curr_y):
        c.saveState()
        c.setFillColor(LIGHT_BG)
        c.setStrokeColor(BORDER_GREY)
        c.setLineWidth(0.6)
        c.rect(MARGIN_L, curr_y - 14, CONTENT_W, 14, fill=1, stroke=1)
        c.setFont("Poppins-Bold", 5.8)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 6, curr_y - 10, "Q")
        c.drawString(MARGIN_L + 28, curr_y - 10, "KEY")
        c.drawString(MARGIN_L + 56, curr_y - 10, "EXAMINER SCIENTIFIC RATIONALE & KEY CONCEPT TESTED")
        c.drawRightString(PAGE_W - MARGIN_R - 6, curr_y - 10, "MARKS")
        c.restoreState()
        return curr_y - 18

    y = draw_exp_header(y)

    for q in questions:
        # Calculate explanation paragraph height
        exp_style = ParagraphStyle('exp_style', fontName='Poppins', fontSize=6.5, leading=9.2, textColor=DARK_TEXT)
        safe_exp = q.explanation.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
        p_exp = Paragraph(safe_exp, exp_style)
        pw, ph = p_exp.wrap(CONTENT_W - 90, PAGE_H)

        row_h = max(ph + 8, 20)

        # Page break check
        if y - row_h < MARGIN_B + 10:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="Explanatory Guide (Continued)")
            y = draw_exp_header(y)

        # Draw Row
        c.saveState()
        # Alternating background
        if q.number % 2 == 1:
            c.setFillColor(ALT_ROW_BG)
            c.rect(MARGIN_L, y - row_h, CONTENT_W, row_h, fill=1, stroke=0)

        # Row border
        c.setStrokeColor(BORDER_LIGHT)
        c.setLineWidth(0.4)
        c.line(MARGIN_L, y - row_h, PAGE_W - MARGIN_R, y - row_h)

        # Q Number
        c.setFont("Poppins-Bold", 6.2)
        c.setFillColor(NAVY)
        c.drawString(MARGIN_L + 4, y - 12, str(q.number))

        # Correct Answer Badge
        c.setFillColor(NAVY)
        c.roundRect(MARGIN_L + 24, y - 13, 14, 11, 2, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(white)
        c.drawCentredString(MARGIN_L + 31, y - 10.5, q.correct_answer)

        # Mark
        c.setFont("Poppins-Bold", 6.0)
        c.setFillColor(MUTED_TEXT)
        c.drawRightString(PAGE_W - MARGIN_R - 8, y - 12, "[1]")
        c.restoreState()

        # Explanation Text
        p_exp.drawOn(c, MARGIN_L + 46, y - ph - 4)

        y -= row_h

    draw_footer(c, page_num, topic_title)
    c.showPage()

def build_mcq_pdf_document(output_path: str, topic_title: str, topic_subtitle: str,
                           subtopics_summary: list, subtopic_map: dict,
                           questions: List[MCQQuestion]):
    register_poppins()
    c = canvas.Canvas(output_path, pagesize=A4)

    total_marks = len(questions)
    total_questions = len(questions)

    print(f"Building {output_path}: {total_questions} MCQs, {total_marks} marks...")

    # 1. Cover Page
    generate_cover_page(c, topic_title, topic_subtitle, subtopics_summary, total_marks, total_questions)

    # 2. MCQ Question Pages
    next_page = generate_mcq_pages(c, questions, subtopic_map, topic_title)

    # 3. Quick-Check Answer Grid
    next_page = generate_quick_answer_grid(c, questions, next_page, topic_title)

    # 4. Comprehensive Explanations
    generate_explanations(c, questions, next_page, topic_title)

    c.save()
    size = os.path.getsize(output_path)
    print(f"[SUCCESS] Generated: {output_path} ({size} bytes)")
