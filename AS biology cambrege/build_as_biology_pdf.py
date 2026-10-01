"""
Cambridge International AS Level Biology (9700) Examination Pack Generator
Candidate: Hamna | Mentora Academy
Target Folder: AS biology cambrege/

Features:
- Mentora Academy cover page tailored for Hamna
- Running headers: Navy (#0b1b36) and Crimson (#a81717)
- Running footers: Mentora Academy branding, page numbering, and low-opacity contact details:
    mentoraonlineacademy@gmail.com | +923164586836
- Dynamic figure embedding with high-DPI scaling and captions
- Dotted answer lines proportioned to mark tariff
- Two-column comprehensive worked mark schemes
"""

import os
import re
from dataclasses import dataclass, field
from typing import List, Optional
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

# ── Color Palette ─────────────────────────────────────────────────────────────
NAVY        = HexColor("#0b1b36")
DEEP_NAVY   = HexColor("#132646")
CRIMSON     = HexColor("#a81717")
DARK_TEXT   = HexColor("#20242e")
LIGHT_BG    = HexColor("#f8f7f5")
BORDER_GREY = HexColor("#dcd8d0")
DOTTED_LINE = HexColor("#b0aca4")

# High-contrast solid navy color for user contact footer (100% crisp printing)
FOOTER_CONTACT_COLOR = HexColor("#0b1b36")

# User Contact Information
USER_EMAIL = "mentoraonlineacademy@gmail.com"
USER_PHONE = "+923164586836"

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
    difficulty: str  # ADVANCED / CHALLENGING
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

def clean_text_for_poppins(text: str) -> str:
    if not text:
        return ""
    replacements = [
        ("α-", "alpha-"),
        ("α", "alpha"),
        ("β-", "beta-"),
        ("β", "beta"),
        ("γ", "gamma"),
        ("δ²⁻", "delta(2-)"),
        ("δ⁻", "delta(-)"),
        ("δ⁺", "delta(+)"),
        ("δ", "delta"),
        ("Δ", "Delta"),
        ("→", "->"),
        ("↔", "<->"),
        ("°C", " deg C"),
        ("°", " deg "),
        ("µm", "um"),
        ("μm", "um"),
        ("µ", "u"),
        ("μ", "u"),
        ("²", "2"),
        ("³", "3"),
        ("⁻¹", "-1"),
        ("⁻²", "-2"),
        ("⁻³", "-3"),
        ("⁻", "-"),
        ("⁺", "+"),
        ("—", " - "),
        ("–", "-"),
        ("“", '"'),
        ("”", '"'),
        ("‘", "'"),
        ("’", "'"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def draw_spaced_text(c, text, x, y, font, size, color, tracking=2.0):
    text = clean_text_for_poppins(text)
    c.saveState()
    c.setFont(font, size)
    c.setFillColor(color)
    cx = x
    for ch in text:
        c.drawString(cx, y, ch)
        cx += c.stringWidth(ch, font, size) + tracking
    c.restoreState()
    return cx - x

def draw_header(c, page_type="AS Level Biology - Paper 2 Theory"):
    page_type = clean_text_for_poppins(page_type)
    c.saveState()
    # Left: Academy Logo / Title
    c.setFont("Poppins-Bold", 8.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, PAGE_H - 32, "MENTORA")

    c.setFont("Poppins-Bold", 5.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "ACADEMY", MARGIN_L, PAGE_H - 40, "Poppins-Bold", 5.0, CRIMSON, tracking=1.5)

    # Right: Candidate & Subject metadata
    right_text = "HAMNA · BIOLOGY - CAMBRIDGE INTERNATIONAL AS LEVEL (9700)"
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
    topic_label = clean_text_for_poppins(topic_label)
    c.saveState()
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, PAGE_W, 30, fill=1, stroke=0)

    # Dividing hair-line
    c.setStrokeColor(BORDER_GREY)
    c.setLineWidth(0.4)
    c.line(MARGIN_L, 30, PAGE_W - MARGIN_R, 30)

    # Line 1 (y = 17): Academic title, candidate, and page number
    c.setFont("Poppins-Medium", 6.8)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, 17, f"MENTORA ACADEMY · Hamna · AS Level Biology (9700) - {topic_label}")

    c.setFont("Poppins-Bold", 7.2)
    c.setFillColor(NAVY)
    c.drawRightString(PAGE_W - MARGIN_R, 17, str(page_num))

    # Line 2 (y = 7): Amped up legible user contact details (mentoraonlineacademy@gmail.com | +923164586836)
    c.setFont("Poppins-SemiBold", 7.2)
    c.setFillColor(FOOTER_CONTACT_COLOR)
    contact_text = f"{USER_EMAIL}   •   {USER_PHONE}"
    c.drawString(MARGIN_L, 7, contact_text)

    c.restoreState()

def draw_paragraph(c, text, x, y, width, font='Poppins', size=7.2, color=DARK_TEXT, leading=10.5):
    text = clean_text_for_poppins(text)
    style = ParagraphStyle('style', fontName=font, fontSize=size, textColor=color, leading=leading)
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
    draw_header(c, page_type="AS Level Biology — Structured Examination Pack")

    y = PAGE_H - 80

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(CRIMSON)
    draw_spaced_text(c, "CAMBRIDGE INTERNATIONAL AS LEVEL BIOLOGY (9700)", MARGIN_L, y, "Poppins-Bold", 6.5, CRIMSON, tracking=1.2)
    y -= 18

    c.setFont("Poppins-Bold", 15.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, topic_title)
    y -= 14
    c.setFont("Poppins-Medium", 8.5)
    c.setFillColor(DARK_TEXT)
    c.drawString(MARGIN_L, y, topic_subtitle)
    y -= 18

    # Metadata badges
    badge_w = (CONTENT_W - 20) / 3
    badges = [
        ("CANDIDATE", "Hamna (Grade A* Scholar)"),
        ("SPECIFICATION", "Cambridge 9700 AS Level"),
        ("TOTAL MARKS / QUESTIONS", f"{total_marks} Marks · {total_questions} Questions"),
    ]
    for i, (label, val) in enumerate(badges):
        bx = MARGIN_L + i * (badge_w + 10)
        c.setFillColor(LIGHT_BG)
        c.roundRect(bx, y - 40, badge_w, 40, 4, fill=1, stroke=0)
        c.setStrokeColor(BORDER_GREY)
        c.setLineWidth(0.5)
        c.roundRect(bx, y - 40, badge_w, 40, 4, fill=0, stroke=1)

        c.setFont("Poppins-Bold", 5.5)
        c.setFillColor(CRIMSON)
        draw_spaced_text(c, label, bx + 8, y - 14, "Poppins-Bold", 5.2, CRIMSON, tracking=1.0)

        c.setFont("Poppins-SemiBold", 7.5)
        c.setFillColor(NAVY)
        c.drawString(bx + 8, y - 28, val)
    y -= 54

    # Structure & Tariff Box
    c.setFillColor(LIGHT_BG)
    c.roundRect(MARGIN_L, y - 90, CONTENT_W, 90, 4, fill=1, stroke=0)
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN_L, y - 90, CONTENT_W, 90, 4, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L + 12, y - 18, "EXAMINATION STRUCTURE & 80/20 QUESTION TARIFF")

    tariff_items = [
        "Section A — Extended High-Tariff Questions: 20 × 6 Marks (120 Marks total) [Multi-part synoptic evaluation]",
        "Section B — Data Interpretation & Structured Explanations: 20 × 4 Marks (80 Marks total)",
        "Section C — Core Definitions & Quantitative Calculations: 10 × 2 Marks (20 Marks total)",
        "Section D — 10 High-Frequency Core Repeated Questions for Exam Mastery & Knowledge Consolidation",
        "Division: 80% Authentic Cambridge 9700 Past Paper references + 20% Original A* Extension Problems"
    ]
    ty = y - 32
    for item in tariff_items:
        c.setFont("Poppins", 6.8)
        c.setFillColor(DARK_TEXT)
        c.drawString(MARGIN_L + 16, ty, f"•  {item}")
        ty -= 12
    y -= 105

    # Subtopics Syllabus Specification
    c.setFont("Poppins-Bold", 8.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y, "SYLLABUS SUBTOPICS COVERED IN THIS PACK")
    y -= 8
    c.setStrokeColor(CRIMSON)
    c.setLineWidth(1.0)
    c.line(MARGIN_L, y, MARGIN_L + 180, y)
    y -= 14

    for st in subtopics_summary:
        c.setFont("Poppins-SemiBold", 7.2)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 6, y, "▸")
        h = draw_paragraph(c, st, MARGIN_L + 18, y + 2, CONTENT_W - 24, font='Poppins', size=6.8, leading=9.5)
        y -= (h + 6)

    # Academic Notice Box
    y -= 10
    c.setFillColor(HexColor("#fff8e7"))
    c.roundRect(MARGIN_L, y - 48, CONTENT_W, 48, 4, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#e0a800"))
    c.setLineWidth(0.6)
    c.roundRect(MARGIN_L, y - 48, CONTENT_W, 48, 4, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 7.0)
    c.setFillColor(HexColor("#7a5200"))
    c.drawString(MARGIN_L + 10, y - 14, "EXAMINER'S DIRECTIVE FOR CANDIDATE HAMNA")
    c.setFont("Poppins", 6.6)
    c.drawString(MARGIN_L + 10, y - 26, "Write legibly in the dotted spaces provided. Pay strict attention to Cambridge command words (Explain, Describe, Deduce, Calculate).")
    c.drawString(MARGIN_L + 10, y - 38, "Where biological diagrams or graphs are provided, extract exact qualitative and quantitative coordinates to support your answers.")

    draw_footer(c, 1, topic_title)
    c.showPage()

def generate_question_pages(c, questions: List[Question], topic_title: str):
    register_poppins()
    page_num = 2
    y = draw_header(c, page_type="AS Level Biology — Paper 2 Theory")

    current_section = None

    for q in questions:
        # Check if new section banner needed
        if q.section_key and q.section_key != current_section:
            current_section = q.section_key
            if y < MARGIN_B + 100:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="AS Level Biology — Paper 2 Theory")

            # Section Banner
            y -= 6
            c.setFillColor(NAVY)
            c.roundRect(MARGIN_L, y - 18, CONTENT_W, 18, 3, fill=1, stroke=0)
            c.setFont("Poppins-Bold", 7.5)
            c.setFillColor(white)
            c.drawString(MARGIN_L + 10, y - 13, current_section.upper())
            y -= 26

        # Estimate space needed for this question
        fig_h = 180 if q.figure_path and os.path.exists(q.figure_path) else 0
        preamble_h = 24 if q.preamble else 0
        parts_h = sum(20 + (p.num_answer_lines * 13) for p in q.parts)
        needed_h = 28 + fig_h + preamble_h + min(parts_h, 110)

        if y - needed_h < MARGIN_B + 30:
            draw_footer(c, page_num, topic_title)
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="AS Level Biology — Paper 2 Theory")

        # Question Header Box
        q_marks = sum(p.marks for p in q.parts)
        c.setFillColor(LIGHT_BG)
        c.roundRect(MARGIN_L, y - 20, CONTENT_W, 20, 3, fill=1, stroke=0)
        c.setStrokeColor(BORDER_GREY)
        c.setLineWidth(0.5)
        c.roundRect(MARGIN_L, y - 20, CONTENT_W, 20, 3, fill=0, stroke=1)

        # Question badge
        c.setFillColor(NAVY)
        c.circle(MARGIN_L + 12, y - 10, 8, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 7.5)
        c.setFillColor(white)
        c.drawCentredString(MARGIN_L + 12, y - 12.5, str(q.number))

        # Title & Reference
        c.setFont("Poppins-Bold", 7.2)
        c.setFillColor(NAVY)
        ref_text = f"[{q_marks} Marks]  {clean_text_for_poppins(q.syllabus_ref)}"
        ref_w = c.stringWidth(ref_text, "Poppins-Medium", 6.5)
        max_title_w = CONTENT_W - 32 - ref_w - 12
        title_str = clean_text_for_poppins(q.title)
        if c.stringWidth(title_str, "Poppins-Bold", 7.2) > max_title_w:
            while len(title_str) > 5 and c.stringWidth(title_str + "...", "Poppins-Bold", 7.2) > max_title_w:
                title_str = title_str[:-1]
            title_str += "..."
        c.drawString(MARGIN_L + 26, y - 12.5, title_str)

        c.setFont("Poppins-Medium", 6.5)
        c.setFillColor(CRIMSON)
        c.drawRightString(PAGE_W - MARGIN_R - 8, y - 12.5, ref_text)
        y -= 26

        # Preamble text
        if q.preamble:
            h = draw_paragraph(c, q.preamble, MARGIN_L + 4, y, CONTENT_W - 8, font='Poppins', size=7.2, leading=10.5)
            y -= (h + 8)

        # Figure embedding (if available) - enlarged for high-clarity printing
        if q.figure_path and os.path.exists(q.figure_path):
            fig_w = 400
            fig_h = 168
            if y - (fig_h + 20) < MARGIN_B + 30:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="AS Level Biology — Paper 2 Theory")

            fig_x = MARGIN_L + (CONTENT_W - fig_w) / 2.0
            fig_y = y - fig_h
            c.drawImage(q.figure_path, fig_x, fig_y, width=fig_w, height=fig_h, preserveAspectRatio=True, mask='auto')
            y -= (fig_h + 4)

            if q.figure_caption:
                c.setFont("Poppins-Italic", 7.2)
                c.setFillColor(DARK_TEXT)
                c.drawCentredString(PAGE_W / 2.0, y, clean_text_for_poppins(q.figure_caption))
                y -= 10

        # Subparts
        for part in q.parts:
            part_h_est = 22 + (part.num_answer_lines * 13)
            if y - part_h_est < MARGIN_B + 20:
                draw_footer(c, page_num, topic_title)
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="AS Level Biology — Paper 2 Theory")

            # Part label & text
            c.setFont("Poppins-Bold", 7.2)
            c.setFillColor(NAVY)
            c.drawString(MARGIN_L + 6, y - 8, part.label)

            text_w = CONTENT_W - 46
            th = draw_paragraph(c, part.text, MARGIN_L + 24, y, text_w, font='Poppins', size=7.2, leading=10.5)

            # Marks tag
            c.setFont("Poppins-Bold", 6.8)
            c.setFillColor(CRIMSON)
            c.drawRightString(PAGE_W - MARGIN_R - 4, y - 8, f"[{part.marks}]")
            y -= (th + 6)

            # Dotted writing lines
            if part.num_answer_lines > 0:
                draw_dotted_lines(c, MARGIN_L + 24, y, CONTENT_W - 28, count=part.num_answer_lines, spacing=13)
                y -= (part.num_answer_lines * 13 + 6)

        y -= 8

    draw_footer(c, page_num, topic_title)
    c.showPage()
    return page_num + 1

def generate_faq_pages(c, faqs: List[dict], topic_title: str, start_page: int):
    register_poppins()
    page_num = start_page
    y = draw_header(c, page_type="Section D: 10 High-Frequency Examiner FAQs & Revision Insights")

    # Section Banner
    c.setFillColor(NAVY)
    c.roundRect(MARGIN_L, y - 18, CONTENT_W, 18, 3, fill=1, stroke=0)
    c.setFont("Poppins-Bold", 7.6)
    c.setFillColor(white)
    c.drawString(MARGIN_L + 10, y - 12.5, "SECTION D: 10 HIGH-FREQUENCY EXAMINER FAQs & CRITICAL REVISION PITFALLS")
    y -= 24

    c.setFont("Poppins-Medium", 6.6)
    c.setFillColor(CRIMSON)
    c.drawString(MARGIN_L, y - 2, "Essential Cambridge International AS Level Biology (9700) Mark-Scheme Traps, Core Misconceptions, and Model Answers")
    y -= 12

    for faq in faqs:
        q_num = faq.get('q_num', 1)
        q_title = clean_text_for_poppins(faq.get('title', ''))
        q_cat = clean_text_for_poppins(faq.get('category', 'Examiner Insight'))
        examiner_trap = clean_text_for_poppins(faq.get('examiner_trap', ''))
        model_ans = clean_text_for_poppins(faq.get('model_answer', ''))

        # Title paragraph
        title_style = ParagraphStyle('faq_t', fontName='Poppins-Bold', fontSize=7.2, textColor=NAVY, leading=9.8)
        title_p = Paragraph(f"<b>FAQ {q_num}: {q_title}</b>", title_style)
        tw, th = title_p.wrap(CONTENT_W - 24, PAGE_H)

        trap_h = 0
        trap_p = None
        if examiner_trap:
            trap_style = ParagraphStyle('faq_trap', fontName='Poppins-Medium', fontSize=6.3, textColor=HexColor("#7f1d1d"), leading=8.6)
            trap_p = Paragraph(f"<b>Cambridge Examiner Warning:</b> {examiner_trap}", trap_style)
            trw, trh = trap_p.wrap(CONTENT_W - 24, PAGE_H)
            trap_h = trh + 6

        ans_style = ParagraphStyle('faq_ans', fontName='Poppins', fontSize=6.6, textColor=DARK_TEXT, leading=9.0)
        ans_formatted = model_ans.replace("\n", "<br/>").replace("•", "&bull;").replace("->", "&rarr;")
        ans_formatted = re.sub(r'&(?!(?:amp|lt|gt|bull|rarr|Delta|times|deg|plusmn|le|ge|middot|infin|rightleftharpoons|harr|#[0-9]+|#x[0-9a-fA-F]+);)', '&amp;', ans_formatted)
        ans_p = Paragraph(ans_formatted, ans_style)
        aw, ah = ans_p.wrap(CONTENT_W - 24, PAGE_H)

        # Card height calculation
        card_h = 13 + th + (trap_h + 4 if trap_p else 0) + ah + 8

        # Page break check
        if y - card_h < MARGIN_B + 16:
            draw_footer(c, page_num, f"{topic_title} (Examiner FAQs)")
            c.showPage()
            page_num += 1
            y = draw_header(c, page_type="Section D: 10 High-Frequency Examiner FAQs & Revision Insights")

        card_y = y - card_h

        # Card Background
        c.setFillColor(LIGHT_BG)
        c.roundRect(MARGIN_L, card_y, CONTENT_W, card_h, 3, fill=1, stroke=0)
        c.setStrokeColor(BORDER_GREY)
        c.setLineWidth(0.4)
        c.roundRect(MARGIN_L, card_y, CONTENT_W, card_h, 3, fill=0, stroke=1)

        # Left Accent Bar
        accent_color = CRIMSON if (q_num % 2 == 1) else NAVY
        c.setFillColor(accent_color)
        c.roundRect(MARGIN_L, card_y, 3.5, card_h, 1.5, fill=1, stroke=0)

        # 1. Top Category Tag on its own distinct line
        c.setFont("Poppins-Bold", 5.6)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN_L + 12, y - 9.5, q_cat.upper())

        # 2. Title Paragraph drawn below category tag
        title_p.drawOn(c, MARGIN_L + 12, y - 13 - th)
        cur_y = y - 13 - th - 4

        # 3. Examiner Trap Callout (if present)
        if trap_p:
            c.setFillColor(HexColor("#fff1f2"))
            c.roundRect(MARGIN_L + 8, cur_y - trh - 3, CONTENT_W - 16, trh + 3, 2, fill=1, stroke=0)
            c.setStrokeColor(HexColor("#fecaca"))
            c.setLineWidth(0.4)
            c.roundRect(MARGIN_L + 8, cur_y - trh - 3, CONTENT_W - 16, trh + 3, 2, fill=0, stroke=1)
            trap_p.drawOn(c, MARGIN_L + 12, cur_y - trh)
            cur_y -= (trh + 6)

        # 4. Model Answer
        ans_p.drawOn(c, MARGIN_L + 12, cur_y - ah)

        y -= (card_h + 6)

    draw_footer(c, page_num, f"{topic_title} (Examiner FAQs)")
    c.showPage()
    return page_num + 1

def generate_mark_scheme_pages(c, questions: List[Question], topic_title: str, start_page: int):
    register_poppins()
    page_num = start_page
    y = draw_header(c, page_type="Comprehensive Examiner Mark Scheme")

    c.setFont("Poppins-Bold", 10.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN_L, y - 4, "EXAMINER MARK SCHEME & MARKING GUIDELINES")
    y -= 14
    c.setFont("Poppins-Medium", 7.0)
    c.setFillColor(CRIMSON)
    c.drawString(MARGIN_L, y - 2, f"{topic_title} — Cambridge International AS Level Biology (9700)")
    y -= 18

    # Table Header
    col_q = 28
    col_part = 24
    col_marks = 36
    col_ans = CONTENT_W - col_q - col_part - col_marks

    def draw_ms_header(curr_y):
        c.setFillColor(NAVY)
        c.rect(MARGIN_L, curr_y - 14, CONTENT_W, 14, fill=1, stroke=0)
        c.setFont("Poppins-Bold", 6.5)
        c.setFillColor(white)
        c.drawString(MARGIN_L + 4, curr_y - 10, "Q")
        c.drawString(MARGIN_L + col_q + 2, curr_y - 10, "PART")
        c.drawString(MARGIN_L + col_q + col_part + 4, curr_y - 10, "EXAMINER MARKING PRINCIPLES & ACCEPTED ANSWERS")
        c.drawRightString(PAGE_W - MARGIN_R - 4, curr_y - 10, "MARKS")
        return curr_y - 18

    y = draw_ms_header(y)

    for q in questions:
        for ms_item in q.mark_scheme:
            part_label = ms_item.get('part', '')
            points_text = clean_text_for_poppins(ms_item.get('points', ''))
            marks_val = ms_item.get('marks', 1)

            # Estimate row height
            style = ParagraphStyle('ms', fontName='Poppins', fontSize=6.8, leading=9.5, textColor=DARK_TEXT)
            formatted = points_text.replace("\n", "<br/>")
            formatted = re.sub(r'&(?!(?:amp|lt|gt|bull|rarr|Delta|times|deg|plusmn|le|ge|middot|infin|rightleftharpoons|harr|#[0-9]+|#x[0-9a-fA-F]+);)', '&amp;', formatted)
            p = Paragraph(formatted, style)
            pw, ph = p.wrap(col_ans - 8, PAGE_H)
            row_h = max(ph + 6, 14)

            if y - row_h < MARGIN_B + 20:
                draw_footer(c, page_num, f"{topic_title} (Mark Scheme)")
                c.showPage()
                page_num += 1
                y = draw_header(c, page_type="Comprehensive Examiner Mark Scheme")
                y = draw_ms_header(y)

            # Row background
            c.setStrokeColor(BORDER_GREY)
            c.setLineWidth(0.4)
            c.line(MARGIN_L, y - row_h, PAGE_W - MARGIN_R, y - row_h)

            c.setFont("Poppins-Bold", 7.0)
            c.setFillColor(NAVY)
            c.drawString(MARGIN_L + 4, y - 10, str(q.number))

            c.setFont("Poppins-SemiBold", 6.8)
            c.setFillColor(CRIMSON)
            c.drawString(MARGIN_L + col_q + 2, y - 10, part_label)

            p.drawOn(c, MARGIN_L + col_q + col_part + 4, y - ph - 2)

            c.setFont("Poppins-Bold", 6.8)
            c.setFillColor(CRIMSON)
            c.drawRightString(PAGE_W - MARGIN_R - 4, y - 10, f"[{marks_val}]")

            y -= row_h

    draw_footer(c, page_num, f"{topic_title} (Mark Scheme)")
    c.showPage()
    return page_num

def build_topic_pdf(output_pdf_path: str, topic_title: str, topic_subtitle: str,
                    subtopics: List[str], questions: List[Question],
                    faqs: Optional[List[dict]] = None):
    register_poppins()
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    total_questions = len(questions)

    # 1. Cover Page
    generate_cover_page(c, topic_title, topic_subtitle, subtopics, total_marks, total_questions)

    # 2. Question Pages (Sections A, B, C)
    next_page = generate_question_pages(c, questions, topic_title)

    # 3. Section D: 10 FAQs Pages (if supplied)
    if faqs:
        next_page = generate_faq_pages(c, faqs, topic_title, next_page)

    # 4. Mark Scheme Pages
    total_pages = generate_mark_scheme_pages(c, questions, topic_title, next_page)

    c.save()
    print(f"Generated PDF: {output_pdf_path} ({total_pages} pages, {total_questions} Qs, {total_marks} Marks)")
    return output_pdf_path
