import os
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from daily_content import DAILY_CONTENT

OUT_FILE = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\Hamna_AS_Biology_Planner_2026_2027.pdf"
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

def register_fonts():
    fonts = {
        'Poppins-Regular': 'Poppins-Regular.ttf',
        'Poppins-Bold': 'Poppins-Bold.ttf',
        'Poppins-SemiBold': 'Poppins-SemiBold.ttf',
        'Poppins-Medium': 'Poppins-Medium.ttf'
    }
    has_poppins = True
    for name, filename in fonts.items():
        font_path = os.path.join(FONT_DIR, filename)
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(name, font_path))
            except:
                has_poppins = False
        else:
            has_poppins = False
            
    if not has_poppins:
        return {'Regular': 'Helvetica', 'Bold': 'Helvetica-Bold', 'SemiBold': 'Helvetica-Bold', 'Medium': 'Helvetica'}
    return {'Regular': 'Poppins-Regular', 'Bold': 'Poppins-Bold', 'SemiBold': 'Poppins-SemiBold', 'Medium': 'Poppins-Medium'}

font_names = register_fonts()
NAVY = colors.HexColor("#0b1b36")
CRIMSON = colors.HexColor("#a81717")

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(font_names['Bold'], 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(1.5*cm, A4[1] - 1*cm, "MENTORA ACADEMY")
    canvas.setFillColor(CRIMSON)
    canvas.drawString(1.5*cm + 100, A4[1] - 1*cm, "A C A D E M Y")
    canvas.setFont(font_names['Regular'], 8)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(A4[0] - 1.5*cm, A4[1] - 1*cm, "HAMNA — BIOLOGY — AS LEVEL (9700)")

    canvas.setFont(font_names['Regular'], 8)
    canvas.drawString(1.5*cm, 1*cm, "Hamna · AS Level Biology (9700) — Study Planner 2026–2027")
    canvas.setFont(font_names['Bold'], 8)
    canvas.drawRightString(A4[0] - 1.5*cm, 1*cm, f"{doc.page}")
    canvas.setFont(font_names['SemiBold'], 7)
    canvas.drawCentredString(A4[0]/2.0, 0.5*cm, "mentoraonlineacademy@gmail.com   •   +923164586836")
    canvas.restoreState()

def build_pdf():
    doc = BaseDocTemplate(OUT_FILE, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 1*cm, id='normal')
    template = PageTemplate(id='test', frames=frame, onPage=header_footer)
    doc.addPageTemplates([template])
    
    h1 = ParagraphStyle('H1', fontName=font_names['Bold'], fontSize=24, textColor=NAVY, leading=28, spaceAfter=20, alignment=1)
    h2 = ParagraphStyle('H2', fontName=font_names['Bold'], fontSize=16, textColor=CRIMSON, leading=20, spaceAfter=10)
    p = ParagraphStyle('P', fontName=font_names['Regular'], fontSize=11, textColor=NAVY, leading=16, spaceAfter=8)
    p_bold = ParagraphStyle('PB', fontName=font_names['Bold'], fontSize=11, textColor=NAVY, leading=16, spaceAfter=8)
    bullet_style = ParagraphStyle('Bullet', fontName=font_names['Regular'], fontSize=10, textColor=NAVY, leading=14, spaceAfter=4)
    tip_style = ParagraphStyle('Tip', fontName=font_names['Regular'], fontSize=10, textColor=CRIMSON, leading=14, spaceAfter=4)
    
    story = []
    
    # Cover Page
    story.append(Spacer(1, 4*cm))
    story.append(Paragraph("MENTORA ACADEMY", h1))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("Cambridge International AS Level Biology (9700)", h2))
    story.append(Paragraph("Personalised Mastery Planner", h1))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("<b>Student:</b> HAMNA", p_bold))
    story.append(Paragraph("<b>Target Exam:</b> Cambridge M/J 2027", p))
    story.append(Paragraph("<b>Date Range:</b> 25 September 2026 — 15 February 2027", p))
    story.append(Paragraph("<b>Total:</b> 21 Weeks · 144 Study Days · 11 Topics · 550 Practice Questions", p))
    story.append(PageBreak())

    topics = [
        {"num": 3, "title": "ENZYMES", "start": datetime.date(2026, 9, 25), "end": datetime.date(2026, 10, 10), "n_subs": 5},
        {"num": 4, "title": "CELL MEMBRANES AND TRANSPORT", "start": datetime.date(2026, 10, 11), "end": datetime.date(2026, 10, 31), "n_subs": 5},
        {"num": 5, "title": "THE MITOTIC CELL CYCLE", "start": datetime.date(2026, 11, 1), "end": datetime.date(2026, 11, 15), "n_subs": 3},
        {"num": 6, "title": "NUCLEIC ACIDS AND PROTEIN SYNTHESIS", "start": datetime.date(2026, 11, 16), "end": datetime.date(2026, 12, 5), "n_subs": 4},
        {"num": 7, "title": "TRANSPORT IN PLANTS", "start": datetime.date(2026, 12, 6), "end": datetime.date(2026, 12, 19), "n_subs": 4},
        {"num": 8, "title": "TRANSPORT IN MAMMALS", "start": datetime.date(2027, 1, 2), "end": datetime.date(2027, 1, 16), "n_subs": 3},
        {"num": 9, "title": "GAS EXCHANGE", "start": datetime.date(2027, 1, 17), "end": datetime.date(2027, 1, 25), "n_subs": 3},
        {"num": 10, "title": "INFECTIOUS DISEASES", "start": datetime.date(2027, 1, 26), "end": datetime.date(2027, 2, 5), "n_subs": 3},
        {"num": 11, "title": "IMMUNITY", "start": datetime.date(2027, 2, 6), "end": datetime.date(2027, 2, 15), "n_subs": 4}
    ]

    start_date = datetime.date(2026, 9, 25)
    end_date = datetime.date(2027, 2, 15)
    
    current_date = start_date
    week_num = 1
    
    topic_day_indices = {t["num"]: 0 for t in topics}
    
    while current_date <= end_date:
        week_end = current_date + datetime.timedelta(days=6)
        if week_end > end_date:
            week_end = end_date
        
        current_topic = None
        for t in topics:
            if t["start"] <= current_date <= t["end"] or (current_date < t["start"] and week_end >= t["start"]):
                current_topic = t
                break
        
        topic_title = current_topic['title'] if current_topic else "HOLIDAY / REVISION"
        
        # WEEKLY PAGE
        story.append(Paragraph(f"WEEK {week_num}: {current_date.strftime('%d %b %Y')} - {week_end.strftime('%d %b %Y')}", h1))
        story.append(Paragraph(f"Topic: {topic_title}", h2))
        story.append(Paragraph("<b>Weekly Learning Objective:</b> Master the sub-topics allocated for this week and consolidate understanding.", p))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("<b>Weekly Goal Checklist:</b>", p_bold))
        story.append(Paragraph("☐ Complete daily reading", p))
        story.append(Paragraph("☐ Review class notes", p))
        story.append(Paragraph("☐ Complete Saturday consolidation", p))
        story.append(Paragraph("☐ Optional Sunday review", p))
        story.append(Spacer(1, 0.5*cm))
        if current_topic and (current_topic["end"] >= current_date and current_topic["end"] <= week_end):
            story.append(Paragraph(f"<b>Weekly Practice:</b> Hamna_Bio_Topic{current_topic['num']}_{current_topic['title'].replace(' ', '_')}.pdf (50 Qs, 220 Marks, 3 hrs)", p_bold))
        
        story.append(PageBreak())
        
        # DAILY PAGES
        day_date = current_date
        while day_date <= week_end:
            is_holiday = (datetime.date(2026, 12, 20) <= day_date <= datetime.date(2027, 1, 1))
            day_name = day_date.strftime('%A')
            story.append(Paragraph(f"DAY {(day_date - start_date).days + 1} — {day_name}, {day_date.strftime('%d %b %Y')}", h2))
            
            if is_holiday:
                story.append(Paragraph("<b>HOLIDAY LIGHT REVIEW</b>", p_bold))
                story.append(Paragraph("Flashcard/FAQ review of Topics 3–7 only, no new content.", p))
            elif day_name == 'Saturday':
                story.append(Paragraph("<b>CONSOLIDATION DAY</b>", p_bold))
                story.append(Paragraph("Review the whole week, attempt 5 Qs from the pack, re-read Section D FAQs.", p))
            elif day_name == 'Sunday':
                story.append(Paragraph("<b>OPTIONAL REVIEW</b>", p_bold))
                story.append(Paragraph("Flashcards / light revision, flexible.", p))
            else:
                day_topic = None
                for t in topics:
                    if t["start"] <= day_date <= t["end"]:
                        day_topic = t
                        break
                
                if day_topic:
                    t_num = day_topic["num"]
                    idx = topic_day_indices[t_num] % day_topic["n_subs"]
                    topic_day_indices[t_num] += 1
                    
                    content = DAILY_CONTENT.get((t_num, idx))
                    if content:
                        story.append(Paragraph(f"<b>Topic {t_num} — {day_topic['title']} ({content['syllabus_ref']})</b>", p_bold))
                        story.append(Paragraph(f"Today's Sub-topic: {content['subtopic']}", p))
                        story.append(Paragraph(f"<b>Learning Objective:</b> {content['learning_objective']}", p))
                        
                        story.append(Spacer(1, 0.3*cm))
                        story.append(Paragraph("<b>What to Learn:</b>", p_bold))
                        for pt in content['what_to_learn']:
                            story.append(Paragraph(pt, bullet_style))
                            
                        story.append(Spacer(1, 0.3*cm))
                        story.append(Paragraph("<b>How to Outstand:</b>", p_bold))
                        for tip in content['how_to_outstand']:
                            story.append(Paragraph(f"• {tip}", tip_style))
                            
                        story.append(Spacer(1, 0.3*cm))
                        story.append(Paragraph(f"<b>Resources:</b> {content['resources']}", p_bold))
                    else:
                        story.append(Paragraph(f"<b>Topic {t_num} — {day_topic['title']}</b>", p_bold))
                        story.append(Paragraph("General revision / Continued practice.", p))
                        
            story.append(Spacer(1, 0.5*cm))
            story.append(Paragraph("<b>Self-Assessment:</b>", p_bold))
            story.append(Paragraph("☐ Can explain this to someone else", p))
            story.append(Paragraph("☐ Attempted practice questions", p))
            story.append(Paragraph("☐ Reviewed mark scheme", p))
            story.append(Spacer(1, 0.5*cm))
            story.append(Paragraph("<b>Notes:</b>", p_bold))
            story.append(Paragraph("-" * 80, p))
            story.append(Paragraph("-" * 80, p))
            story.append(Paragraph("-" * 80, p))
            
            story.append(PageBreak())
            day_date += datetime.timedelta(days=1)
            
        current_date = day_date
        week_num += 1

    doc.build(story)

if __name__ == "__main__":
    build_pdf()
    print(f"Generated specific detailed PDF successfully at {OUT_FILE}")
