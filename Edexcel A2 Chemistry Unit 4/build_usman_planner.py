"""
build_usman_planner.py
Compiles the complete Pearson Edexcel IAL Unit 4 Chemistry (WCH14) Mastery Planner PDF
for candidate Usman at Mentora Academy.
Generates:
- Formal Prestigious Cover Page
- 15-Week Executive Roadmap & Syllabus Architecture
- Part 1: Weekly Overview Planner (1 page per week, 15 weeks)
- Part 2: Detailed Daily Planner (1 page per day, Days 1 to 101)
"""

import os
import sys
import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import daily content module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from usman_daily_content import WEEKS_META, get_daily_content

OUT_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Usman_Edexcel_Chem_U4_Mastery_Planner_2026_2027.pdf"
)
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

# ──────────────────────────────────────────────────────────────
# FONTS REGISTRATION
# ──────────────────────────────────────────────────────────────
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
        'Regular': 'Poppins-Regular', 'Bold': 'Poppins-Bold',
        'SemiBold': 'Poppins-SemiBold', 'Medium': 'Poppins-Medium',
        'Italic': 'Poppins-Italic', 'Mono': 'Courier'
    }

FONT = register_fonts()

# ──────────────────────────────────────────────────────────────
# COLOUR PALETTE (Mentora Academy Standards)
# ──────────────────────────────────────────────────────────────
NAVY      = colors.HexColor("#0b1b36")   # Primary Headings & Structure
CRIMSON   = colors.HexColor("#a81717")   # Accent, Traps & Test Days
STEEL     = colors.HexColor("#1e3a8a")   # Subheadings & Strategic Banners
LIGHT_BG  = colors.HexColor("#f8fafc")   # Card Background
TINT_BG   = colors.HexColor("#eef2f6")   # Objective & Table Tint
ALERT_BG  = colors.HexColor("#fef2f2")   # Examiner Trap Light BG
BORDER    = colors.HexColor("#cbd5e1")   # Dividing Borders
DARK_TXT  = colors.HexColor("#1e293b")   # Body Text
MUTED     = colors.HexColor("#64748b")   # Footnotes & Minor Info
GOLD      = colors.HexColor("#b45309")   # A* Achievement Highlights
WHITE     = colors.white

PAGE_W, PAGE_H = A4
L_MARGIN = R_MARGIN = 1.4 * cm
TOP_MARGIN = BOTTOM_MARGIN = 1.4 * cm
AVAIL_W = PAGE_W - L_MARGIN - R_MARGIN

# ──────────────────────────────────────────────────────────────
# HEADER & FOOTER CANVAS
# ──────────────────────────────────────────────────────────────
def draw_header_footer(canvas, doc):
    canvas.saveState()
    
    # Do not draw running header on cover page
    if doc.page > 1:
        # Top Running Header
        canvas.setFont(FONT['Bold'], 8)
        canvas.setFillColor(NAVY)
        canvas.drawString(L_MARGIN, PAGE_H - 0.85 * cm, "MENTORA ACADEMY")
        canvas.setFillColor(CRIMSON)
        canvas.drawString(L_MARGIN + 92, PAGE_H - 0.85 * cm, "A C A D E M Y")
        
        canvas.setFont(FONT['SemiBold'], 7.8)
        canvas.setFillColor(STEEL)
        canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 0.85 * cm,
                               "USMAN  —  EDEXCEL IAL CHEMISTRY UNIT 4 (WCH14)  —  A* PLANNER")
        
        # Header Dividing Line
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.6)
        canvas.line(L_MARGIN, PAGE_H - 0.98 * cm, PAGE_W - R_MARGIN, PAGE_H - 0.98 * cm)

    # Bottom Running Footer (All pages including cover has contact)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.6)
    canvas.line(L_MARGIN, 1.25 * cm, PAGE_W - R_MARGIN, 1.25 * cm)

    if doc.page > 1:
        canvas.setFont(FONT['Regular'], 7.5)
        canvas.setFillColor(NAVY)
        canvas.drawString(L_MARGIN, 0.95 * cm,
                          "Usman  •  Edexcel IAL Chemistry Unit 4  •  A* Mastery Study Planner (2026–2027)")
        
        canvas.setFont(FONT['Bold'], 8)
        canvas.setFillColor(NAVY)
        canvas.drawRightString(PAGE_W - R_MARGIN, 0.95 * cm, f"Page {doc.page}")

    # Official Mentora Contact Footer
    canvas.setFont(FONT['SemiBold'], 7.2)
    canvas.setFillColor(NAVY)
    canvas.drawCentredString(PAGE_W / 2.0, 0.45 * cm,
                             "mentoraonlineacademy@gmail.com   •   +923164586836")
    canvas.restoreState()


# ──────────────────────────────────────────────────────────────
# STYLES DEFINITION
# ──────────────────────────────────────────────────────────────
def get_planner_styles():
    def _s(name, **kw):
        defaults = dict(fontName=FONT['Regular'], fontSize=9, textColor=DARK_TXT,
                        leading=13, spaceAfter=0, spaceBefore=0)
        defaults.update(kw)
        return ParagraphStyle(name, **defaults)

    return {
        'cover_super': _s('CovSup', fontName=FONT['Bold'], fontSize=11, textColor=CRIMSON, alignment=1, spaceAfter=8),
        'cover_h1':    _s('CovH1',  fontName=FONT['Bold'], fontSize=22, textColor=NAVY, alignment=1, leading=26, spaceAfter=6),
        'cover_sub':   _s('CovSub', fontName=FONT['SemiBold'], fontSize=12, textColor=STEEL, alignment=1, leading=16, spaceAfter=14),
        'cover_desc':  _s('CovDsc', fontName=FONT['Regular'], fontSize=9.5, textColor=DARK_TXT, alignment=1, leading=14),
        
        'week_h1':     _s('WkH1',   fontName=FONT['Bold'], fontSize=16, textColor=NAVY, leading=20, spaceAfter=3),
        'week_sub':    _s('WkSub',  fontName=FONT['Bold'], fontSize=11, textColor=CRIMSON, leading=15, spaceAfter=8),
        'sec_h2':      _s('SecH2',  fontName=FONT['Bold'], fontSize=10, textColor=NAVY, leading=14, spaceBefore=4, spaceAfter=4),
        'sec_h2_c':    _s('SecH2C', fontName=FONT['Bold'], fontSize=10, textColor=CRIMSON, leading=14, spaceBefore=4, spaceAfter=4),
        
        'body':        _s('Body',   fontName=FONT['Regular'], fontSize=8.5, textColor=DARK_TXT, leading=12),
        'body_bold':   _s('BodyB',  fontName=FONT['Bold'], fontSize=8.5, textColor=NAVY, leading=12),
        'bullet':      _s('Blt',    fontName=FONT['Regular'], fontSize=8.2, textColor=DARK_TXT, leading=11.5, leftIndent=8),
        'bullet_c':    _s('BltC',   fontName=FONT['Regular'], fontSize=8.2, textColor=CRIMSON, leading=11.5, leftIndent=8),
        
        'day_h1':      _s('DayH1',  fontName=FONT['Bold'], fontSize=13, textColor=NAVY, leading=16),
        'day_type':    _s('DayTyp', fontName=FONT['Bold'], fontSize=8.5, textColor=WHITE, alignment=1),
        'topic_tag':   _s('TpcTag', fontName=FONT['Bold'], fontSize=9, textColor=CRIMSON, leading=12),
        'subtopic':    _s('SubTpc', fontName=FONT['Bold'], fontSize=11, textColor=NAVY, leading=15, spaceAfter=4),
        
        'obj_txt':     _s('ObjTxt', fontName=FONT['Medium'], fontSize=8.5, textColor=NAVY, leading=12),
        'res_txt':     _s('ResTxt', fontName=FONT['SemiBold'], fontSize=8.2, textColor=STEEL, leading=11),
        'check_txt':   _s('ChkTxt', fontName=FONT['Regular'], fontSize=8.0, textColor=DARK_TXT, leading=11),
    }

S = get_planner_styles()


# ──────────────────────────────────────────────────────────────
# BUILDER FUNCTIONS
# ──────────────────────────────────────────────────────────────
def build_cover_page(story):
    story.append(Spacer(1, 1.2 * cm))
    
    # Institution Logo Text
    story.append(Paragraph("MENTORA ACADEMY", S['cover_h1']))
    story.append(Paragraph("E X C E L L E N C E   I N   A D V A N C E D   E D U C A T I O N", S['cover_super']))
    story.append(Spacer(1, 0.4 * cm))
    
    # Subject & Exam Board
    story.append(Paragraph("PEARSON EDEXCEL INTERNATIONAL ADVANCED LEVEL (IAL)", S['cover_sub']))
    story.append(Paragraph("CHEMISTRY UNIT 4: WCH14/01", S['cover_h1']))
    story.append(Paragraph("Rates, Equilibria and Further Organic Chemistry", S['cover_sub']))
    story.append(Paragraph("<b>Personalised A* Mastery Planner & Strategic Timeline</b>", S['cover_desc']))
    story.append(Spacer(1, 0.6 * cm))
    
    # Profile Card Table
    card_data = [
        [Paragraph("<b>Candidate Name:</b>", S['body_bold']), Paragraph("<b>USMAN</b> (Grade A* Scholar)", S['body'])],
        [Paragraph("<b>Exam Target:</b>", S['body_bold']), Paragraph("<b>Pearson Edexcel IAL January 2027 Series (WCH14/01)</b>", S['body'])],
        [Paragraph("<b>Target Result:</b>", S['body_bold']), Paragraph("<b>Grade A* (Top 1% Global Distinction / 100% UMS)</b>", S['body'])],
        [Paragraph("<b>Study Period:</b>", S['body_bold']), Paragraph("07 October 2026 — 15 January 2027 (101 Days Total)", S['body'])],
        [Paragraph("<b>Core Syllabus Completion:</b>", S['body_bold']), Paragraph("<b>26 December 2026 (At Least 20 Days Before Exam!)</b>", S['body'])],
        [Paragraph("<b>Weekly Rhythm:</b>", S['body_bold']), Paragraph("5 Teaching Sessions/Week (Mon–Fri) • Saturday Timed Test • Sunday Error Log", S['body'])],
        [Paragraph("<b>Pedagogical Architecture:</b>", S['body_bold']), Paragraph("15 Weeks • 101 Days • 5 Topics • 43 Detailed Sub-topics • 12 Saturday Tests • 10 Mocks", S['body'])],
        [Paragraph("<b>Institution:</b>", S['body_bold']), Paragraph("Mentora Academy • Online Advanced Sciences Division", S['body'])],
    ]
    
    t_card = Table(card_data, colWidths=[5.5 * cm, AVAIL_W - 5.5 * cm])
    t_card.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 1.2, NAVY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_card)
    story.append(Spacer(1, 0.8 * cm))
    
    # Core Strategy Highlights Box
    strat_data = [
        [Paragraph("<b>STRATEGIC THREE-PILLAR PHILOSOPHY FOR USMAN'S A* SUCCESS</b>", S['sec_h2_c'])],
        [Paragraph("<b>1. Active Recall & Zero Looping:</b> Every syllabus division is taught with authentic chemical equations, real numerical constants, and specific Edexcel past paper references. No passive re-reading.", S['body'])],
        [Paragraph("<b>2. Weekly Saturday Test Benchmarking:</b> Every Saturday features a timed assessment matching the exact questions and mark schemes from the Mentora 50-Question Topical Packs.", S['body'])],
        [Paragraph("<b>3. 20-Day Dedicated Past Paper Marathon:</b> Core teaching finishes strictly on 26 December 2026. The final 20 days are reserved exclusively for full-length WCH14/01 past paper mocks (2021–2024).", S['body'])],
    ]
    t_strat = Table(strat_data, colWidths=[AVAIL_W])
    t_strat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TINT_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, STEEL),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_strat)
    story.append(PageBreak())


def build_roadmap_page(story):
    story.append(Paragraph("EXECUTIVE 15-WEEK SYLLABUS ROADMAP", S['week_h1']))
    story.append(Paragraph("Strategic Timeline & Milestone Overview for Candidate Usman", S['week_sub']))
    story.append(Spacer(1, 0.2 * cm))
    
    headers = [
        Paragraph("<b>Week</b>", S['body_bold']),
        Paragraph("<b>Dates</b>", S['body_bold']),
        Paragraph("<b>Topic & Syllabus Coverage</b>", S['body_bold']),
        Paragraph("<b>Saturday Assessment</b>", S['body_bold']),
        Paragraph("<b>Milestone</b>", S['body_bold'])
    ]
    
    rows = [headers]
    milestones = [
        "11A.1–11A.2 Rates",
        "11A.3–11A.4 Orders",
        "11A.5–11A.6 Arrhenius",
        "Topic 11 Complete / 12A",
        "12A.3 Feasibility / 12B.1",
        "Topic 12 Complete",
        "13A.1–13A.2 Kc & Kp",
        "Topic 13 Complete / 14A.1",
        "14A.2–14A.4 Weak Acids",
        "Topic 14 Complete",
        "15A–15B Carbonyls",
        "CORE SYLLABUS COMPLETE!",
        "Past Paper Mocks 1–4",
        "Past Paper Mocks 5–8",
        "OFFICIAL EXAM DAY!"
    ]
    
    for w in WEEKS_META:
        w_num = w['week']
        m_tag = milestones[w_num - 1]
        bg_col = WHITE if w_num % 2 == 1 else LIGHT_BG
        if w_num == 12:
            m_style = S['body_bold']
        elif w_num == 15:
            m_style = ParagraphStyle('ExTag', fontName=FONT['Bold'], fontSize=8, textColor=CRIMSON)
        else:
            m_style = S['body']
            
        rows.append([
            Paragraph(f"<b>W{w_num}</b>", S['body_bold']),
            Paragraph(w['date_range'].split(' – ')[0] + "<br/>" + w['date_range'].split(' – ')[1], S['body']),
            Paragraph(f"<b>{w['title']}</b><br/>{w['focus']}", S['body']),
            Paragraph(w['test_title'], S['body']),
            Paragraph(m_tag, m_style)
        ])
        
    t_road = Table(rows, colWidths=[1.1*cm, 2.5*cm, 6.2*cm, 5.0*cm, 3.4*cm])
    t_road.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BOX', (0, 0), (-1, -1), 1, NAVY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    for idx in range(1, len(rows)):
        if idx % 2 == 0:
            t_road.setStyle(TableStyle([('BACKGROUND', (0, idx), (-1, idx), LIGHT_BG)]))
        if idx == 12:  # Week 12 highlight
            t_road.setStyle(TableStyle([('BACKGROUND', (0, idx), (-1, idx), colors.HexColor("#fef3c7"))]))
        if idx == 15:  # Week 15 highlight
            t_road.setStyle(TableStyle([('BACKGROUND', (0, idx), (-1, idx), ALERT_BG)]))
            
    story.append(t_road)
    story.append(PageBreak())


def build_weekly_overview_page(story, week_meta):
    w_num = week_meta['week']
    d_range = week_meta['date_range']
    title = week_meta['title']
    focus = week_meta['focus']
    obj = week_meta['objective']
    checklist = week_meta['checklist']
    test_title = week_meta['test_title']
    test_res = week_meta['test_resource']
    
    # Week Header Banner Table
    banner_data = [
        [
            Paragraph(f"<b>WEEK {w_num} OVERVIEW & STRATEGIC GOALS</b>", S['week_h1']),
            Paragraph(f"<b>{d_range}</b>", ParagraphStyle('WkDte', fontName=FONT['Bold'], fontSize=10, textColor=CRIMSON, alignment=2))
        ],
        [
            Paragraph(f"<b>Primary Topic:</b> {title}", S['sec_h2']),
            Paragraph(f"<b>Focus:</b> {focus}", ParagraphStyle('WkFoc', fontName=FONT['SemiBold'], fontSize=8.5, textColor=STEEL, alignment=2))
        ]
    ]
    t_banner = Table(banner_data, colWidths=[AVAIL_W - 5.5*cm, 5.5*cm])
    t_banner.setStyle(TableStyle([
        ('LINEBELOW', (0, -1), (-1, -1), 1.2, NAVY),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_banner)
    story.append(Spacer(1, 0.3 * cm))
    
    # Weekly Learning Objective Box
    obj_box = [
        [Paragraph("<b>WEEKLY STRATEGIC LEARNING OBJECTIVE</b>", S['sec_h2'])],
        [Paragraph(obj, S['obj_txt'])]
    ]
    t_obj = Table(obj_box, colWidths=[AVAIL_W])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TINT_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, STEEL),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_obj)
    story.append(Spacer(1, 0.35 * cm))
    
    # Weekly Goal Checklist Box
    story.append(Paragraph("<b>WEEKLY GOAL CHECKLIST & MASTERY MILESTONES:</b>", S['sec_h2']))
    check_rows = []
    for item in checklist:
        check_rows.append([
            Paragraph("☐", ParagraphStyle('Box', fontName=FONT['Bold'], fontSize=11, textColor=NAVY, alignment=1)),
            Paragraph(item, S['body'])
        ])
    t_check = Table(check_rows, colWidths=[0.8*cm, AVAIL_W - 0.8*cm])
    t_check.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, colors.HexColor("#e2e8f0")),
    ]))
    story.append(t_check)
    story.append(Spacer(1, 0.4 * cm))
    
    # Saturday Test & Sunday Plan Cards
    test_box = [
        [
            Paragraph("<b>SATURDAY TEST DAY OBJECTIVE</b>", S['sec_h2_c']),
            Paragraph("<b>SUNDAY CONSOLIDATION PLAN</b>", S['sec_h2'])
        ],
        [
            Paragraph(f"<b>Assessment:</b> {test_title}<br/><b>Target:</b> >= 85% Score<br/><b>Assigned Pack:</b> {test_res}", S['body']),
            Paragraph("<b>Diagnostic Routine:</b> Enter lost marks into A* Error Registry.<br/><b>Active Recall:</b> Re-solve missed problems from scratch.<br/><b>Reinforcement:</b> Review Section D Examiner FAQs.", S['body'])
        ]
    ]
    t_test = Table(test_box, colWidths=[AVAIL_W/2.0, AVAIL_W/2.0])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), ALERT_BG),
        ('BACKGROUND', (1, 0), (1, -1), LIGHT_BG),
        ('BOX', (0, 0), (0, -1), 1, CRIMSON),
        ('BOX', (1, 0), (1, -1), 1, NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 0.4 * cm))
    
    # Weekly Reflection & Teacher/Candidate Observation Box
    obs_box = [
        [Paragraph("<b>WEEKLY REFLECTION, STUDY TIME & TUTOR OBSERVATIONS:</b>", S['sec_h2'])],
        [Paragraph("Total Hours Studied: ________ hrs   |   Saturday Test Raw Score: _______ / _______   (____%)   |   Target Achieved:  ☐ YES   ☐ NO", S['body_bold'])],
        [Spacer(1, 0.15*cm)],
        [Paragraph("Key Strengths & Triumphs This Week:", S['body'])],
        [HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=8)],
        [Paragraph("Specific Weaknesses / Priority Remedial Areas for Sunday Drill:", S['body'])],
        [HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=8)],
        [Paragraph("Tutor Sign-off & Recommendations:", S['body'])],
        [HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=4)],
    ]
    t_obs = Table(obs_box, colWidths=[AVAIL_W])
    t_obs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), WHITE),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_obs)
    story.append(PageBreak())


def build_daily_planner_page(story, day_num, date_obj):
    content = get_daily_content(day_num, date_obj)
    d_str = content['date_str']
    d_type = content['day_type']
    t_code = content['topic_code']
    sub = content['subtopic']
    obj = content['learning_objective']
    learn_pts = content['what_to_learn']
    outstand_pts = content['how_to_outstand']
    res = content['resources']
    checks = content['self_assessment']
    
    # Determine badge color and label
    badge_labels = {
        'TEACHING': ('CORE TUITION SESSION', NAVY),
        'SATURDAY_TEST': ('SATURDAY TEST DAY (TIMED)', CRIMSON),
        'SUNDAY_CONSOLIDATION': ('SUNDAY ERROR AUDIT & REVIEW', STEEL),
        'MOCK_EXAM': ('OFFICIAL PAST PAPER MOCK', CRIMSON),
        'FINAL_PREPARATION': ('PRE-EXAM PREPARATION', GOLD),
        'EXAM_DAY': ('OFFICIAL PEARSON EDEXCEL EXAM', CRIMSON)
    }
    b_text, b_col = badge_labels.get(d_type, ('STUDY SESSION', NAVY))
    
    # Header bar table
    hdr_data = [
        [
            Paragraph(f"<b>DAY {day_num} — {d_str}</b>", S['day_h1']),
            Paragraph(f"<b>{b_text}</b>", ParagraphStyle('Bdg', fontName=FONT['Bold'], fontSize=8, textColor=WHITE, alignment=1))
        ]
    ]
    t_hdr = Table(hdr_data, colWidths=[AVAIL_W - 5.2*cm, 5.2*cm])
    t_hdr.setStyle(TableStyle([
        ('BACKGROUND', (1, 0), (1, 0), b_col),
        ('BOX', (1, 0), (1, 0), 0.5, b_col),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_hdr)
    story.append(Spacer(1, 0.15 * cm))
    
    # Topic Code & Sub-topic Title
    story.append(Paragraph(t_code, S['topic_tag']))
    story.append(Paragraph(sub, S['subtopic']))
    story.append(Spacer(1, 0.1 * cm))
    
    # Learning Objective Card
    obj_data = [
        [Paragraph(f"<b>Learning Objective:</b> {obj}", S['obj_txt'])]
    ]
    t_obj = Table(obj_data, colWidths=[AVAIL_W])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TINT_BG),
        ('BOX', (0, 0), (-1, -1), 0.6, STEEL),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_obj)
    story.append(Spacer(1, 0.25 * cm))
    
    # What to Learn Section
    story.append(Paragraph("<b>WHAT TO LEARN (CORE SYLLABUS SPECIFICATION):</b>", S['sec_h2']))
    learn_rows = []
    for pt in learn_pts:
        learn_rows.append([Paragraph(pt, S['bullet'])])
    t_learn = Table(learn_rows, colWidths=[AVAIL_W])
    t_learn.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_learn)
    story.append(Spacer(1, 0.25 * cm))
    
    # How to Outstand (A* Examiner Edge) Section
    outstand_box = [
        [Paragraph("<b>HOW TO OUTSTAND (A* EXAMINER EDGE & TRAP ALERTS):</b>", S['sec_h2_c'])]
    ]
    for opt in outstand_pts:
        outstand_box.append([Paragraph(f"• {opt}", S['bullet_c'])])
    t_out = Table(outstand_box, colWidths=[AVAIL_W])
    t_out.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ALERT_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, CRIMSON),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_out)
    story.append(Spacer(1, 0.25 * cm))
    
    # Assigned Resources Box
    res_box = [
        [Paragraph(f"<b>Assigned Practice Material & References:</b> {res}", S['res_txt'])]
    ]
    t_res = Table(res_box, colWidths=[AVAIL_W])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 0.25 * cm))
    
    # Self-Assessment Checkpoints
    story.append(Paragraph("<b>DAILY SELF-ASSESSMENT & PROGRESS AUDIT:</b>", S['sec_h2']))
    chk_rows = []
    for chk in checks:
        chk_rows.append([
            Paragraph("☐", ParagraphStyle('BoxD', fontName=FONT['Bold'], fontSize=10, textColor=NAVY, alignment=1)),
            Paragraph(chk, S['check_txt'])
        ])
    t_chk = Table(chk_rows, colWidths=[0.7*cm, AVAIL_W - 0.7*cm])
    t_chk.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(t_chk)
    story.append(Spacer(1, 0.25 * cm))
    
    # Student Reflection & Notes Lines
    story.append(Paragraph("<b>DAILY NOTES & PROBLEM LOG:</b>", S['body_bold']))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=8))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=8))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=4))
    
    story.append(PageBreak())


def build_usman_planner_pdf():
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    
    doc = BaseDocTemplate(
        OUT_FILE, pagesize=A4,
        leftMargin=L_MARGIN, rightMargin=R_MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id='normal'
    )
    template = PageTemplate(id='main', frames=frame, onPage=draw_header_footer)
    doc.addPageTemplates([template])
    
    story = []
    
    # 1. Title / Cover Page
    print("[1/4] Building Cover Page...")
    build_cover_page(story)
    
    # 2. Executive 15-Week Roadmap
    print("[2/4] Building Executive Roadmap Table...")
    build_roadmap_page(story)
    
    # 3. Part 1: Weekly Overview Pages (15 weeks)
    print("[3/4] Building Part 1: Weekly Overview Pages (15 Weeks)...")
    for w in WEEKS_META:
        build_weekly_overview_page(story, w)
        
    # 4. Part 2: Detailed Daily Planner Pages (101 days)
    print("[4/4] Building Part 2: Detailed Daily Planner Pages (101 Days)...")
    start_date = datetime.date(2026, 10, 7)
    for day_num in range(1, 102):
        d_obj = start_date + datetime.timedelta(days=day_num - 1)
        build_daily_planner_page(story, day_num, d_obj)
        
    print(f"Compiling document story into PDF: {OUT_FILE} ...")
    doc.build(story)
    
    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"[SUCCESS] Usman Mastery Planner generated successfully! Size: {size_mb:.2f} MB")
    return OUT_FILE


if __name__ == "__main__":
    build_usman_planner_pdf()
