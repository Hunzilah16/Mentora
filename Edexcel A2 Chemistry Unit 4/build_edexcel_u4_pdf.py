import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, Image
)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

def register_fonts():
    fonts = {
        'Poppins-Regular': 'Poppins-Regular.ttf',
        'Poppins-Bold': 'Poppins-Bold.ttf',
        'Poppins-SemiBold': 'Poppins-SemiBold.ttf',
        'Poppins-Medium': 'Poppins-Medium.ttf',
        'Poppins-Italic': 'Poppins-Italic.ttf'
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
            'Regular': 'Helvetica',
            'Bold': 'Helvetica-Bold',
            'SemiBold': 'Helvetica-Bold',
            'Medium': 'Helvetica',
            'Italic': 'Helvetica-Oblique'
        }
    return {
        'Regular': 'Poppins-Regular',
        'Bold': 'Poppins-Bold',
        'SemiBold': 'Poppins-SemiBold',
        'Medium': 'Poppins-Medium',
        'Italic': 'Poppins-Italic'
    }

FONT_NAMES = register_fonts()

NAVY = colors.HexColor("#0b1b36")
CRIMSON = colors.HexColor("#a81717")
STEEL_BLUE = colors.HexColor("#1e3a8a")
LIGHT_BG = colors.HexColor("#f8fafc")
BORDER_COLOR = colors.HexColor("#cbd5e1")
DARK_TEXT = colors.HexColor("#1e293b")
WHITE = colors.HexColor("#ffffff")

def make_answer_lines(marks, left_indent=0):
    content_w = A4[0] - 3*cm - left_indent
    lines_count = 3 if marks <= 1 else (5 if marks == 2 else (7 if marks == 3 else (9 if marks == 4 else 12)))
    table_data = [[""] for _ in range(lines_count)]
    t_lines = Table(table_data, colWidths=[content_w], rowHeights=[0.58*cm]*lines_count)
    t_lines.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3)
    ]))
    return t_lines

def header_footer(canvas, doc):
    canvas.saveState()
    # Running Header
    canvas.setFont(FONT_NAMES['Bold'], 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(1.5*cm, A4[1] - 1*cm, "MENTORA")
    canvas.setFillColor(CRIMSON)
    canvas.drawString(1.5*cm + 48, A4[1] - 1*cm, "A C A D E M Y")
    
    canvas.setFont(FONT_NAMES['Regular'], 8)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(A4[0] - 1.5*cm, A4[1] - 1*cm, "USMAN — EDEXCEL IAL CHEMISTRY A2 (WCH14)")

    # Running Footer
    canvas.setFont(FONT_NAMES['Regular'], 7.5)
    canvas.setFillColor(NAVY)
    canvas.drawString(1.5*cm, 1*cm, "Usman · Edexcel IAL Chemistry Unit 4 (WCH14) — Mentora Academy")
    canvas.setFont(FONT_NAMES['Bold'], 8)
    canvas.drawRightString(A4[0] - 1.5*cm, 1*cm, f"Page {doc.page}")
    
    # Solid Contact Line (100% opacity, Poppins-SemiBold 7.2pt)
    canvas.setFont(FONT_NAMES['SemiBold'], 7.2)
    canvas.setFillColor(NAVY)
    canvas.drawCentredString(A4[0]/2.0, 0.45*cm, "mentoraonlineacademy@gmail.com   •   +923164586836")
    
    canvas.restoreState()

def build_pdf_pack(out_filename, pack_meta, questions, faqs):
    doc = BaseDocTemplate(
        out_filename,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )
    
    content_w = A4[0] - 3*cm
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 1*cm, id='normal')
    template = PageTemplate(id='main', frames=frame, onPage=header_footer)
    doc.addPageTemplates([template])
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        fontName=FONT_NAMES['Bold'],
        fontSize=20,
        textColor=NAVY,
        leading=24,
        alignment=1,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        fontName=FONT_NAMES['SemiBold'],
        fontSize=12,
        textColor=CRIMSON,
        leading=16,
        alignment=1,
        spaceAfter=25
    )
    
    meta_label = ParagraphStyle('MetaLabel', fontName=FONT_NAMES['Bold'], fontSize=9, textColor=CRIMSON, leading=12)
    meta_val = ParagraphStyle('MetaVal', fontName=FONT_NAMES['SemiBold'], fontSize=10, textColor=NAVY, leading=13)
    
    h2_style = ParagraphStyle('SectionBanner', fontName=FONT_NAMES['Bold'], fontSize=11, textColor=WHITE, leading=15)
    q_title_style = ParagraphStyle('QTitle', fontName=FONT_NAMES['Bold'], fontSize=9.5, textColor=NAVY, leading=13.5)
    q_text_style = ParagraphStyle('QText', fontName=FONT_NAMES['Regular'], fontSize=8.8, textColor=DARK_TEXT, leading=12.5)
    ms_text_style = ParagraphStyle('MSText', fontName=FONT_NAMES['Regular'], fontSize=8.2, textColor=DARK_TEXT, leading=11.5)
    
    story = []
    
    # ------------------ COVER PAGE ------------------
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("MENTORA ACADEMY", ParagraphStyle('TopHeader', fontName=FONT_NAMES['Bold'], fontSize=24, textColor=NAVY, alignment=1)))
    story.append(Paragraph("EXCELLENCE IN EDUCATION", ParagraphStyle('SubHeader', fontName=FONT_NAMES['Bold'], fontSize=10, textColor=CRIMSON, alignment=1, spaceAfter=25)))
    
    story.append(Paragraph("Edexcel International A Level Chemistry (WCH14)", title_style))
    story.append(Paragraph(f"UNIT 4 — MASTER TOPICAL PRACTICE PACK: {pack_meta.get('subtopic_code', '')}", subtitle_style))
    story.append(Paragraph(f"<b>{pack_meta.get('subtopic_name', '').upper()}</b>", ParagraphStyle('SubtopicBig', fontName=FONT_NAMES['Bold'], fontSize=13, textColor=NAVY, alignment=1, spaceAfter=20)))
    
    tot_marks = sum(q.get('marks', 1) for q in questions)
    
    meta_data = [
        [Paragraph("CANDIDATE NAME:", meta_label), Paragraph(pack_meta.get('candidate', 'Usman'), meta_val)],
        [Paragraph("SUBJECT & CODE:", meta_label), Paragraph("Chemistry Unit 4 — Rates, Equilibria & Organic (WCH14)", meta_val)],
        [Paragraph("TOPIC AREA:", meta_label), Paragraph(f"{pack_meta.get('topic_code', '')}: {pack_meta.get('topic_name', '')}", meta_val)],
        [Paragraph("SUB-TOPIC:", meta_label), Paragraph(f"{pack_meta.get('subtopic_code', '')}: {pack_meta.get('subtopic_name', '')}", meta_val)],
        [Paragraph("TOTAL QUESTIONS:", meta_label), Paragraph(f"{len(questions)} Authentic Past Paper Questions (Tier 1 & Tier 2)", meta_val)],
        [Paragraph("TOTAL MARKS:", meta_label), Paragraph(f"{tot_marks} Marks", meta_val)],
        [Paragraph("EXAMINER FAQs:", meta_label), Paragraph(f"{len(faqs)} Empirical Examiner Traps & Model Answers Included", meta_val)]
    ]
    
    t_meta = Table(meta_data, colWidths=[4*cm, 12*cm])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 1.2*cm))
    
    how_to_use = [
        [Paragraph("<b>HOW TO USE THIS A* TOPICAL PACK:</b>", ParagraphStyle('HTUHeading', fontName=FONT_NAMES['Bold'], fontSize=10, textColor=NAVY))],
        [Paragraph("1. <b>Tier 1 (Q1–Q25)</b>: Mid-Easy to Moderate foundational questions (1–3 marks, MCQs, core calculations).<br/>2. <b>Tier 2 (Q26–Q50)</b>: Hard & A* Challenge questions (4–6 marks, multi-step calculations, multi-spectral NMR, extended answers).<br/>3. Review the complete worked mark scheme in Section C after attempting each tier.<br/>4. Master the 10 Empirical Examiner FAQs in Section D to eliminate common candidate traps.", q_text_style)]
    ]
    t_htu = Table(how_to_use, colWidths=[16*cm])
    t_htu.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 1, STEEL_BLUE),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_htu)
    story.append(PageBreak())
    
    # ------------------ SECTION A: TIER 1 QUESTIONS (Q1-Q25) ------------------
    banner_t1 = Table([[Paragraph(f"SECTION A: TIER 1 PRACTICE QUESTIONS (FOUNDATIONAL TO MODERATE) — Q1 to Q25", h2_style)]], colWidths=[content_w])
    banner_t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    story.append(banner_t1)
    story.append(Spacer(1, 0.3*cm))
    
    for idx, q in enumerate(questions, 1):
        if idx == 26:
            story.append(PageBreak())
            banner_t2 = Table([[Paragraph(f"SECTION B: TIER 2 A* CHALLENGE QUESTIONS (HARD & EXTENDED) — Q26 to Q50", h2_style)]], colWidths=[content_w])
            banner_t2.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), CRIMSON),
                ('PADDING', (0,0), (-1,-1), 6),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')
            ]))
            story.append(banner_t2)
            story.append(Spacer(1, 0.3*cm))
            
        q_title = q.get('title') or q.get('question') or f"Question {idx}"
        q_ref = q.get('ref') or q.get('reference') or "WCH14/01"
        q_marks = q.get('marks', 1)
        
        q_header = [
            [
                Paragraph(f"<b>Q{idx}. {q_title}</b>", q_title_style),
                Paragraph(f"<b>[{q_marks} Marks]</b> &nbsp; <font color='#a81717'><b>{q_ref}</b></font>", ParagraphStyle('QRef', fontName=FONT_NAMES['SemiBold'], fontSize=8.5, alignment=2))
            ]
        ]
        t_qhead = Table(q_header, colWidths=[11*cm, 5*cm])
        t_qhead.setStyle(TableStyle([
            ('LINEBELOW', (0,0), (-1,-1), 1, STEEL_BLUE),
            ('PADDING', (0,0), (-1,-1), 2),
            ('VALIGN', (0,0), (-1,-1), 'BOTTOM')
        ]))
        story.append(t_qhead)
        story.append(Spacer(1, 0.15*cm))
        
        # Stem
        if q.get('stem'):
            story.append(Paragraph(q['stem'], q_text_style))
            story.append(Spacer(1, 0.1*cm))
            
        # Diagram rendering (ONLY when explicitly provided via diagram_img or image)
        img_file = q.get('diagram_img') or q.get('image')

        if img_file:
            if not os.path.isabs(img_file):
                img_file = os.path.join(os.path.dirname(__file__), img_file)
            if os.path.exists(img_file):
                img_w = 12 * cm
                img_h = 5.5 * cm
                if 'rate_conc' in img_file or 'nmr' in img_file:
                    img_w = 14 * cm
                    img_h = 5 * cm
                elif 'arrhenius' in img_file or 'boltzmann' in img_file or 'titration' in img_file:
                    img_w = 11 * cm
                    img_h = 6 * cm
                
                img_flow = Image(img_file, width=img_w, height=img_h)
                t_img = Table([[img_flow]], colWidths=[content_w])
                t_img.setStyle(TableStyle([
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                    ('PADDING', (0,0), (-1,-1), 2),
                ]))
                story.append(t_img)
                story.append(Spacer(1, 0.2*cm))
        elif q.get('diagram'):
            d_box = Table([[Paragraph(f"<i>[DIAGRAM / FIGURE: {q['diagram']}]</i>", ParagraphStyle('DiagText', fontName=FONT_NAMES['Italic'], fontSize=8.2, textColor=STEEL_BLUE, alignment=1))]], colWidths=[14*cm])
            d_box.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
                ('PADDING', (0,0), (-1,-1), 8),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')
            ]))
            story.append(d_box)
            story.append(Spacer(1, 0.2*cm))
            
        # Options for MCQ questions
        if q.get('options'):
            for opt in q['options']:
                story.append(Paragraph(opt, ParagraphStyle('MCQOptDirect', fontName=FONT_NAMES['Regular'], fontSize=8.5, textColor=DARK_TEXT, leading=12, leftIndent=12)))
            story.append(Spacer(1, 0.15*cm))
            
        # Parts and write-in answer lines
        has_parts = bool(q.get('parts'))
        if has_parts:
            for part in q.get('parts', []):
                if isinstance(part, str):
                    story.append(Paragraph(part, q_text_style))
                elif isinstance(part, dict):
                    part_label = f"<b>({part.get('label', '')})</b> " if part.get('label') else ""
                    part_marks = part.get('marks', 1)
                    marks_str = f" <b>[{part_marks}]</b>" if part.get('marks') else ""
                    story.append(Paragraph(f"{part_label}{part.get('text', '')}{marks_str}", ParagraphStyle('PartText', fontName=FONT_NAMES['Regular'], fontSize=8.8, textColor=DARK_TEXT, leading=12.5, leftIndent=12)))
                    
                    if part.get('mcq_options'):
                        for opt in part['mcq_options']:
                            story.append(Paragraph(f"<b>{opt['key']}</b> {opt['text']}", ParagraphStyle('MCQOpt', fontName=FONT_NAMES['Regular'], fontSize=8.5, textColor=DARK_TEXT, leading=12, leftIndent=24)))
                    elif part.get('subparts'):
                        for subpart in part.get('subparts', []):
                            sub_label = f"<b>({subpart.get('label', '')})</b> " if subpart.get('label') else ""
                            sub_marks_val = subpart.get('marks', 1)
                            sub_marks = f" <b>[{sub_marks_val}]</b>" if subpart.get('marks') else ""
                            story.append(Paragraph(f"{sub_label}{subpart.get('text', '')}{sub_marks}", ParagraphStyle('SubpartText', fontName=FONT_NAMES['Regular'], fontSize=8.5, textColor=DARK_TEXT, leading=12.5, leftIndent=24)))
                            story.append(Spacer(1, 0.1*cm))
                            story.append(make_answer_lines(sub_marks_val, left_indent=0.8*cm))
                            story.append(Spacer(1, 0.15*cm))
                    else:
                        story.append(Spacer(1, 0.1*cm))
                        story.append(make_answer_lines(part_marks, left_indent=0.4*cm))
                        story.append(Spacer(1, 0.15*cm))
        else:
            if not q.get('options'):
                story.append(Spacer(1, 0.1*cm))
                story.append(make_answer_lines(q_marks, left_indent=0))
                story.append(Spacer(1, 0.15*cm))

        story.append(Spacer(1, 0.55*cm))
        
    story.append(PageBreak())
    
    # ------------------ SECTION C: WORKED MARK SCHEME ------------------
    banner_ms = Table([[Paragraph(f"SECTION C: WORKED MARK SCHEME (Q1–Q{len(questions)}) — {pack_meta.get('subtopic_code', '')}", h2_style)]], colWidths=[content_w])
    banner_ms.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    story.append(banner_ms)
    story.append(Spacer(1, 0.3*cm))
    
    ms_table_data = [[
        Paragraph("<b>Q</b>", ParagraphStyle('MSHead1', fontName=FONT_NAMES['Bold'], fontSize=8.5, textColor=WHITE)),
        Paragraph("<b>MARKING SCHEME & ACCEPTABLE ANSWERS</b>", ParagraphStyle('MSHead2', fontName=FONT_NAMES['Bold'], fontSize=8.5, textColor=WHITE)),
        Paragraph("<b>MARKS</b>", ParagraphStyle('MSHead3', fontName=FONT_NAMES['Bold'], fontSize=8.5, textColor=WHITE, alignment=1))
    ]]
    
    for idx, q in enumerate(questions, 1):
        q_title = q.get('title') or q.get('question') or f"Question {idx}"
        q_marks = q.get('marks', 1)
        ms_text = f"<b>Q{idx}: {q_title}</b><br/>"
        
        ms_content = q.get('mark_scheme') or q.get('answer') or ""
        if isinstance(ms_content, str):
            ms_text += f"{ms_content}<br/>"
        elif isinstance(ms_content, list):
            for ms_item in ms_content:
                if isinstance(ms_item, str):
                    ms_text += f"• {ms_item}<br/>"
                elif isinstance(ms_item, dict):
                    label = f"<b>({ms_item.get('label', '')})</b> " if ms_item.get('label') else ""
                    ms_text += f"{label}{ms_item.get('points', '')}<br/>"
        
        ms_table_data.append([
            Paragraph(f"<b>Q{idx}</b>", ParagraphStyle('QNumCell', fontName=FONT_NAMES['Bold'], fontSize=8.5, textColor=NAVY)),
            Paragraph(ms_text, ms_text_style),
            Paragraph(f"<b>[{q_marks}]</b>", ParagraphStyle('QMarksCell', fontName=FONT_NAMES['Bold'], fontSize=8.5, textColor=CRIMSON, alignment=1))
        ])
        
    t_ms = Table(ms_table_data, colWidths=[1.1*cm, 13.5*cm, 1.4*cm])
    t_ms.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG])
    ]))
    story.append(t_ms)
    story.append(PageBreak())
    
    # ------------------ SECTION D: EMPIRICAL EXAMINER FAQS (10 FAQS) ------------------
    banner_faq = Table([[Paragraph(f"SECTION D: EMPIRICAL EXAMINER FAQS & COMMON TRAPS (10 FAQS) — {pack_meta.get('subtopic_code', '')}", h2_style)]], colWidths=[content_w])
    banner_faq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), STEEL_BLUE),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    story.append(banner_faq)
    story.append(Spacer(1, 0.3*cm))
    
    for idx, faq in enumerate(faqs, 1):
        faq_title = faq.get('title') or faq.get('question') or f"FAQ {idx}"
        faq_cat = faq.get('category') or "Examiner Trap & Technique"
        faq_trap = faq.get('examiner_trap') or faq.get('question') or ""
        faq_answer = faq.get('model_answer') or faq.get('answer') or ""
        
        faq_head = Table([[
            Paragraph(f"<b>FAQ #{idx}: {faq_title}</b>", ParagraphStyle('FAQTitle', fontName=FONT_NAMES['Bold'], fontSize=9, textColor=NAVY)),
            Paragraph(f"<font color='#a81717'><b>Category: {faq_cat}</b></font>", ParagraphStyle('FAQCat', fontName=FONT_NAMES['SemiBold'], fontSize=8, alignment=2))
        ]], colWidths=[11*cm, 5*cm])
        faq_head.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#e2e8f0")),
            ('PADDING', (0,0), (-1,-1), 3),
            ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR)
        ]))
        story.append(faq_head)
        
        faq_body = [
            [Paragraph("<b>COMMON EXAMINER TRAP / MISTAKE:</b>", ParagraphStyle('TrapLabel', fontName=FONT_NAMES['Bold'], fontSize=8.2, textColor=CRIMSON))],
            [Paragraph(faq_trap, q_text_style)],
            [Spacer(1, 0.08*cm)],
            [Paragraph("<b>MODEL ANSWER / EXAMINER EXPECTATION:</b>", ParagraphStyle('ModelLabel', fontName=FONT_NAMES['Bold'], fontSize=8.2, textColor=NAVY))],
            [Paragraph(faq_answer, q_text_style)]
        ]
        t_faq_body = Table(faq_body, colWidths=[16*cm])
        t_faq_body.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
            ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('PADDING', (0,0), (-1,-1), 5),
        ]))
        story.append(t_faq_body)
        story.append(Spacer(1, 0.25*cm))
        
    doc.build(story)
    print(f"Compiled PDF successfully: {out_filename}")

if __name__ == "__main__":
    print("Edexcel Unit 4 PDF framework loaded successfully.")
