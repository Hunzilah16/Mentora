from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz

pdfmetrics.registerFont(TTFont('Poppins', r'z:\tests n quizes63\books\psycology\new styl\fonts\Poppins-Regular.ttf'))

c = canvas.Canvas('test_greek.pdf')
style_poppins = ParagraphStyle('poppins', fontName='Poppins', fontSize=10, leading=14)

# Test 1: Symbol font tag
p1 = Paragraph('Test 1: <font name="Symbol">a</font>-glucose and <font name="Symbol">b</font>-glucose', style_poppins)
p1.wrap(300, 50)
p1.drawOn(c, 50, 750)

# Test 2: Standard words alpha and beta
p2 = Paragraph('Test 2: alpha-glucose and beta-glucose', style_poppins)
p2.wrap(300, 50)
p2.drawOn(c, 50, 700)

# Test 3: Arrow and symbols
p3 = Paragraph('Test 3: alpha(1->4)-glycosidic bond, 80 deg C, 1.0 um', style_poppins)
p3.wrap(300, 50)
p3.drawOn(c, 50, 650)

c.save()
print("Saved test_greek.pdf")

doc = fitz.open('test_greek.pdf')
pix = doc[0].get_pixmap(dpi=150)
pix.save('test_greek.png')
print("Saved test_greek.png")
