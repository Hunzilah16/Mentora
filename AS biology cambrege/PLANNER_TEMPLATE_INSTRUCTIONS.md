# 📘 MENTORA ACADEMY — PERSONALISED PLANNER TEMPLATE
## Step-by-Step Instructions for Recreating This Planner for Any Student

> **Created:** October 2026  
> **Original planner:** `Hamna_AS_Biology_Planner_2026_2027.pdf`  
> **Purpose:** Reuse this exact recipe for any new student, subject, or timeline.

---

## 🗂️ FILES IN THIS TEMPLATE SYSTEM

| File | Purpose |
|------|---------|
| `build_hamna_planner.py` | Master PDF builder script (ReportLab) |
| `daily_content.py` | All meticulous daily content per sub-topic |
| `PLANNER_TEMPLATE_INSTRUCTIONS.md` | THIS FILE — the full recipe |

**To make a new planner, you will:**
1. Copy `build_hamna_planner.py` → rename it (e.g. `build_sara_planner.py`)
2. Copy `daily_content.py` → rename it (e.g. `sara_daily_content.py`)
3. Edit both files with the new student's details + new content
4. Run the script → PDF is generated

---

## 📋 STEP 1 — GATHER INFORMATION FROM THE STUDENT/TEACHER

Ask these questions BEFORE writing any code. Every answer directly changes the planner structure.

### Questions to Ask:
1. **Student name** — used on every header/footer and cover page
2. **Subject** — e.g. "Cambridge International AS Level Biology (9700)"
3. **Exam board + paper code** — e.g. Cambridge 9700, 9701, etc.
4. **Topics to cover** — list them in order with start topic and end topic
5. **Start date** — exact date the planner begins (e.g. "25 September 2026")
6. **End date** — target completion date (e.g. "15 February 2027")
7. **Target exam** — e.g. "Cambridge M/J 2027" or "O/N 2026"
8. **Daily study hours** — how many hours per day available for this subject
9. **School schedule** — does student attend school Mon–Fri? Or is it self-study only?
10. **Rest days** — are weekends off, half-day, or optional?
11. **Holidays** — any school breaks, national holidays, winter breaks within the timeline?
12. **Weekly practice format** — full timed simulation (50Q, 220M, 3hrs)? Or shorter drills?
13. **Which topics are already done** — don't re-plan covered material
14. **Output format** — PDF (Mentora style) is default

### Answers for Hamna's Planner (reference):
- Student: Hamna | Subject: AS Biology 9700 | Exam: Cambridge M/J 2027
- Start: 25 Sep 2026 (Topic 3 Enzymes) | End: 15 Feb 2027
- 1–2 hours/day self-study on top of Mentora tuition classes
- School Mon–Fri (full-time) | Sundays: optional | Saturdays: consolidation
- Holiday: Dec 25 – Jan 1 (flashcard review only)
- Weekly practice: Full 50Q simulation using pre-built topic PDFs
- Topics 1 & 2 already completed → planner starts from Topic 3

---

## 🖊️ STEP 2 — PLAN THE CURRICULUM TIMELINE

Map each topic to a date range before writing any code.

### How to Calculate Topic Date Ranges:
- Count working days Mon–Fri (skip Sundays and holiday blocks)
- Allocate 1 sub-topic per weekday (1 study session per sub-topic)
- Add 1–2 buffer days per topic for review
- Reserve end-of-topic Saturdays for full timed practice simulations
- Saturdays = consolidation (no new content)
- Sundays = optional / light review

### Hamna's Final Timeline (reference):
```
Topic 3 — Enzymes:                 25 Sep – 10 Oct 2026   (5 sub-topics, ~12 days)
Topic 4 — Membranes & Transport:   11 Oct – 31 Oct 2026   (5 sub-topics, ~15 days)
Topic 5 — Mitotic Cell Cycle:       1 Nov – 15 Nov 2026   (3 sub-topics, ~11 days)
Topic 6 — Nucleic Acids:           16 Nov –  5 Dec 2026   (4 sub-topics, ~15 days)
Topic 7 — Transport in Plants:      6 Dec – 19 Dec 2026   (4 sub-topics, ~10 days)
HOLIDAY:                           20 Dec – 1 Jan          (flashcard review only)
Topic 8 — Transport in Mammals:     2 Jan – 16 Jan 2027   (3 sub-topics, ~11 days)
Topic 9 — Gas Exchange:            17 Jan – 25 Jan 2027   (3 sub-topics, ~7 days)
Topic 10 — Infectious Diseases:    26 Jan –  5 Feb 2027   (3 sub-topics, ~8 days)
Topic 11 — Immunity:                6 Feb – 15 Feb 2027   (3 sub-topics, ~8 days)
```

### Template Calculation Formula:
```
days_per_topic = num_subtopics + 2 buffer days
topic_end_date = topic_start_date + timedelta(days=days_per_topic + weekends)
next_topic_start = topic_end_date + timedelta(days=1)
```

---

## 📂 STEP 3 — WRITE THE DAILY CONTENT FILE (`daily_content.py`)

This is the most important and time-consuming step. Every sub-topic gets its own content block.

### Structure of `DAILY_CONTENT` Dictionary:
```python
DAILY_CONTENT = {
    (topic_number, day_index): {
        "subtopic":            "3.1 Enzyme action",
        "syllabus_ref":        "9700 Syllabus 3.1",
        "learning_objective":  "One precise, measurable sentence about what student will achieve today.",
        "what_to_learn": [
            "(1) First specific syllabus point — exact facts, equations, named examples.",
            "(2) Second point — go down to sub-sub-topic level.",
            "(3) Third point — include named scientists, named experiments, named molecules.",
            "(4) Fourth point...",
            "(5) Fifth point — include practical/application angles.",
            "(6) Sixth point — include any calculations or graph interpretations.",
        ],
        "how_to_outstand": [
            "EXAMINER TRAP: [state the common mistake and the correct answer].",
            "Cambridge awards marks for [specific vocabulary/phrase] — not vague alternatives.",
            "For A*: [advanced mechanism/link that distinguishes A* from A].",
            "Key command word: [describe vs explain vs state vs calculate — what each requires].",
            "Calculation/graph tip: [specific method Cambridge expects].",
        ],
        "resources": "Q1–Q5 Section A in Hamna_Bio_TopicN_Title.pdf",
    },
    (topic_number, 1): { ... },
    ...
}
```

### Indexing Rule:
- `topic_number` = the Cambridge topic number (e.g. 3, 4, 5...)
- `day_index` = 0 for the first sub-topic, 1 for the second, etc.
- The builder script maps weekdays to day_index using a running counter per topic

### Quality Rules for Content — MUST FOLLOW:
1. **Learning objective**: must be specific and measurable. BAD: "Learn about enzymes." GOOD: "Explain how enzymes lower activation energy and distinguish lock-and-key from induced-fit at molecular level."
2. **What to Learn**: minimum 5 bullet points per sub-topic. Each must name exact molecules, equations, diagrams, or experiments. No vague phrases like "study the chapter."
3. **How to Outstand**: every sub-topic must have at least one "EXAMINER TRAP:" tip starting with that exact phrase. These are the most valuable marks for A* students.
4. **Resources**: reference exact question numbers in the pre-built PDF exam packs if they exist.
5. **Depth**: go to sub-sub-topic level — not just topic level. E.g. not "enzymes" but "Michaelis-Menten kinetics and Km definition."

### Template for Writing Content (copy-paste and fill in):
```python
(TOPIC_NUM, DAY_INDEX): {
    "subtopic":            "X.X Sub-topic name",
    "syllabus_ref":        "XXXX Syllabus X.X",
    "learning_objective":  "[One precise sentence]",
    "what_to_learn": [
        "(1) [Exact point 1]",
        "(2) [Exact point 2]",
        "(3) [Exact point 3]",
        "(4) [Exact point 4]",
        "(5) [Exact point 5]",
        "(6) [Exact point 6 — optional but recommended for complex topics]",
    ],
    "how_to_outstand": [
        "EXAMINER TRAP: [Common mistake → correct answer]",
        "[Specific vocabulary Cambridge awards marks for]",
        "[A* level mechanism/detail]",
        "[Command word distinction]",
        "[Calculation or graph method]",
    ],
    "resources": "QX–QX Section X in [PDF pack name]",
},
```

---

## 🔧 STEP 4 — WRITE THE BUILD SCRIPT (`build_studentname_planner.py`)

Copy `build_hamna_planner.py` and change the following:

### Variables to Update:
```python
# Line 1 — Output file path
OUT_FILE = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\[STUDENT]_[SUBJECT]_Planner_[YEAR].pdf"

# Line 2 — Font directory (stays the same for Mentora)
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

# Import the correct daily content file
from [student]_daily_content import DAILY_CONTENT

# Header right side — student name and subject
canvas.drawRightString(A4[0] - 1.5*cm, A4[1] - 1*cm, "[STUDENT NAME] — [SUBJECT] — [LEVEL] ([CODE])")

# Footer left — student and subject
canvas.drawString(1.5*cm, 1*cm, "[Student] · [Subject] ([Code]) — Study Planner [Year]–[Year]")

# Cover page text
Paragraph("[Student Name]", h1)
Paragraph("Cambridge International [Level] [Subject] ([Code])", h2)
Paragraph("Personalised Mastery Planner", h1)
Paragraph("<b>Student:</b> [STUDENT NAME]", p_bold)
Paragraph("<b>Target Exam:</b> Cambridge [M/J or O/N] [Year]", p)
Paragraph("<b>Date Range:</b> [Start Date] — [End Date]", p)
Paragraph("<b>Total:</b> [N] Weeks · [N] Study Days · [N] Topics · [N] Practice Questions", p)

# Topics list — update with new student's curriculum
topics = [
    {"num": 3, "title": "ENZYMES", "start": datetime.date(YYYY, M, D), "end": datetime.date(YYYY, M, D), "n_subs": 5},
    # ... add all topics
]

# Start and end dates
start_date = datetime.date(YYYY, M, D)
end_date = datetime.date(YYYY, M, D)

# Holiday date range — update for new student
is_holiday = (datetime.date(YYYY, M, D) <= day_date <= datetime.date(YYYY, M, D))
```

### Visual Design — DO NOT CHANGE (Mentora standard):
```python
NAVY        = colors.HexColor("#0b1b36")   # Primary colour — all headers, body text
CRIMSON     = colors.HexColor("#a81717")   # Accent — section labels, examiner traps
STEEL_BLUE  = colors.HexColor("#1e3a8a")   # Sub-headers, date labels
LIGHT_GOLD  = colors.HexColor("#f5e6c3")   # Background for special days
LIGHT_NAVY_BG = colors.HexColor("#e8edf5") # Alternating row backgrounds
WHITE       = colors.HexColor("#ffffff")
```

### Font Registration (DO NOT CHANGE — Mentora standard):
```python
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"
# Registers: Poppins-Regular, Poppins-Bold, Poppins-SemiBold, Poppins-Medium
# Falls back to Helvetica if fonts not found
```

### Contact Footer (DO NOT CHANGE — Mentora standard):
```python
canvas.drawCentredString(A4[0]/2.0, 0.5*cm,
    "mentoraonlineacademy@gmail.com   •   +923164586836")
# Font: Poppins-SemiBold, 7pt, Navy #0b1b36, 100% opacity — NEVER translucent
```

---

## 📄 STEP 5 — PAGE STRUCTURE (DO NOT CHANGE THE LOGIC)

Every page follows this exact structure. The script loops through days automatically.

### Weekly Overview Page (one per week):
```
WEEK N: DD Mon YYYY - DD Mon YYYY
Topic: [TOPIC TITLE]
Weekly Learning Objective: [auto-generated]
Weekly Goal Checklist:
  ☐ Complete daily reading
  ☐ Review class notes
  ☐ Complete Saturday consolidation
  ☐ Optional Sunday review
[If week ends a topic → Weekly Practice: [PDF name] (50 Qs, 220 Marks, 3 hrs)]
--- PAGE BREAK ---
```

### Normal Weekday Page (Mon–Fri, non-holiday):
```
DAY N — Weekday, DD Mon YYYY
Topic N — [TITLE] ([Syllabus Ref])
Today's Sub-topic: [sub-topic name]
Learning Objective: [one specific sentence]

What to Learn:
  (1) [specific point] ☐
  (2) [specific point] ☐
  ...

How to Outstand:
  • EXAMINER TRAP: [in crimson] ...
  • [examiner tip 2] ...
  • [examiner tip 3] ...

Resources: [Q numbers in PDF pack]

Self-Assessment:
  ☐ Can explain this to someone else
  ☐ Attempted practice questions
  ☐ Reviewed mark scheme

Notes:
  ................................................................
  ................................................................
  ................................................................
--- PAGE BREAK ---
```

### Saturday — Consolidation Day:
```
DAY N — Saturday, DD Mon YYYY
CONSOLIDATION DAY
Review the whole week, attempt 5 Qs from the pack, re-read Section D FAQs.
[Self-assessment checkboxes]
[Notes lines]
--- PAGE BREAK ---
```

### Saturday — End-of-Topic Practice (when a topic ends):
```
DAY N — Saturday, DD Mon YYYY
TIMED EXAM SIMULATION
Attempt full 50-question timed simulation: [PDF name] (220 Marks, 3 hrs exam conditions)
[Self-assessment checkboxes]
--- PAGE BREAK ---
```

### Sunday — Optional Review:
```
DAY N — Sunday, DD Mon YYYY
OPTIONAL REVIEW
Flashcards / light revision, flexible.
[Self-assessment checkboxes]
--- PAGE BREAK ---
```

### Holiday Days:
```
DAY N — Weekday, DD Mon YYYY
HOLIDAY LIGHT REVIEW
Flashcard/FAQ review of Topics X–Y only, no new content.
[Self-assessment checkboxes]
--- PAGE BREAK ---
```

---

## ▶️ STEP 6 — RUN THE SCRIPT

```powershell
# Navigate to the working directory
cd "z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"

# Run the build script
python build_[student]_planner.py

# Expected output:
# Generated specific detailed PDF successfully at [path]
```

### Verify the Output:
```python
# Quick page count check
python -c "
with open('[student]_planner.pdf', 'rb') as f:
    data = f.read()
pages = data.count(b'/Type /Page') - data.count(b'/Type /Pages')
print('Page count:', pages)
print('File size KB:', round(len(data)/1024, 1))
"
```

### Expected Output Ranges:
- A 21-week planner → ~160–200 pages
- File size → 200–400 KB

---

## 🔁 ADAPTING FOR A NEW STUDENT — CHECKLIST

Use this checklist every time you create a planner for a new student:

### Information Gathering:
- [ ] Student name confirmed
- [ ] Subject, level, and paper code confirmed
- [ ] Start date confirmed (and which topic to start from)
- [ ] End date confirmed
- [ ] Target exam session confirmed (M/J or O/N, year)
- [ ] Daily study hours confirmed
- [ ] School schedule confirmed (full-time school? tuition only?)
- [ ] Rest/off days confirmed
- [ ] Holiday dates confirmed
- [ ] Weekly practice format confirmed (full 50Q simulation vs short drill)
- [ ] Topics already completed confirmed (don't re-plan these)
- [ ] Existing PDF exam packs available? (for resources references)

### Script Customisation:
- [ ] `OUT_FILE` path updated with new student name
- [ ] `from [student]_daily_content import DAILY_CONTENT` updated
- [ ] Header right side updated with student name + subject
- [ ] Footer left side updated with student name + subject
- [ ] Cover page text updated (student, exam, dates, totals)
- [ ] `topics` list updated with new curriculum and date ranges
- [ ] `start_date` and `end_date` updated
- [ ] Holiday date range updated
- [ ] Contact footer unchanged (Mentora standard)
- [ ] Colours unchanged (Mentora standard)
- [ ] Font directory unchanged (Mentora standard)

### Content (`daily_content.py`):
- [ ] All topic numbers match the new syllabus
- [ ] Every sub-topic has a specific `learning_objective`
- [ ] Every sub-topic has ≥5 `what_to_learn` bullets (syllabus-specific)
- [ ] Every sub-topic has ≥3 `how_to_outstand` tips
- [ ] Every sub-topic has at least one `EXAMINER TRAP:` tip
- [ ] All `resources` reference actual question numbers in existing PDF packs
- [ ] `day_index` values start at 0 per topic and are sequential

### Final QC:
- [ ] Script runs with exit code 0 (no errors)
- [ ] Page count is within expected range
- [ ] PDF opens and pages render correctly
- [ ] Header/footer appears on every page
- [ ] Contact details visible on every page footer
- [ ] Special days (Saturday, Sunday, Holiday) render with correct labels

---

## 🎨 MENTORA BRAND REFERENCE (DO NOT CHANGE FOR ANY STUDENT)

| Element | Value |
|---------|-------|
| Primary Navy | `#0b1b36` |
| Crimson Accent | `#a81717` |
| Steel Blue | `#1e3a8a` |
| Light Gold BG | `#f5e6c3` |
| Light Navy BG | `#e8edf5` |
| Font — Body | Poppins-Regular, 11pt |
| Font — Headings | Poppins-Bold, 16–24pt |
| Font — Sub-headings | Poppins-SemiBold, 11–12pt |
| Font — Tips | Poppins-Regular, 10pt, Crimson |
| Font — Footer contact | Poppins-SemiBold, 7pt, Navy, centred |
| Page Size | A4 Portrait |
| Margins | 1.5 cm all sides |
| Header | MENTORA ACADEMY (navy) + A C A D E M Y (crimson, letter-spaced) |
| Footer contact | `mentoraonlineacademy@gmail.com   •   +923164586836` |
| Font directory | `z:\tests n quizes63\books\psycology\new styl\fonts\` |

---

## 📌 TIPS FOR WRITING A*-QUALITY CONTENT

These rules apply universally — for any Cambridge subject:

1. **Always write "EXAMINER TRAP:" tips first.** These are the highest-value tips for A* students. Find the top 1–2 mistakes examiners penalise in that sub-topic and flag them explicitly.

2. **Be specific about vocabulary.** Cambridge examiners use mark schemes with specific expected vocabulary. Don't say "the enzyme changes shape" — say "the conformational change OPTIMALLY POSITIONS CATALYTIC RESIDUES."

3. **Distinguish command words.** "State" = one or two words. "Describe" = say what happens. "Explain" = say what happens AND why/how. "Suggest" = use reasoning without needing to know the exact fact. Include command word guidance for complex topics.

4. **Include calculation methods.** Whenever a topic involves numbers, graphs, or equations — include the exact method Cambridge expects (e.g. "draw tangent at t=0; gradient = rate").

5. **Link structure to function.** Cambridge Biology and Chemistry questions frequently ask students to link structural features to their functions. Embed these links explicitly in the What to Learn bullets.

6. **Use named examples.** "Aquaporins" not just "channel proteins." "Hexokinase" not just "an enzyme." Named examples earn marks.

7. **Go to sub-sub-topic depth.** Don't write "osmosis" as a topic. Break it into: water potential equation, Ψ = Ψs + Ψp, plant cell behaviour, animal cell behaviour, calculations.

8. **Cover practical investigations.** Cambridge marks are allocated to practical skills. Include experimental protocols, control variables, and data analysis methods in the relevant sub-topic entries.

---

## 🗃️ FILE NAMING CONVENTION

For new planners, follow this naming convention:

```
Script:   build_[FirstName]_[Subject]_planner.py
Content:  [firstname]_[subject]_daily_content.py
PDF:      [FirstName]_[ExamBoard]_[Subject]_Planner_[StartYear]_[EndYear].pdf

Examples:
  build_sara_biology_planner.py
  sara_biology_daily_content.py
  Sara_AS_Biology_Planner_2026_2027.pdf

  build_ali_chemistry_planner.py
  ali_chemistry_daily_content.py
  Ali_AS_Chemistry_Planner_2026_2027.pdf
```

---

## 📝 QUICK-START TEMPLATE FOR A NEW STUDENT

To start a new planner from scratch, copy the following shell and fill in the blanks:

### `build_STUDENT_planner.py` skeleton:
```python
import os, datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from STUDENT_daily_content import DAILY_CONTENT  # ← CHANGE THIS

OUT_FILE = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\STUDENT_SUBJECT_Planner.pdf"
FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"

NAVY      = colors.HexColor("#0b1b36")
CRIMSON   = colors.HexColor("#a81717")
STEEL_BLUE = colors.HexColor("#1e3a8a")

def register_fonts():
    # [copy exact font registration block from build_hamna_planner.py]
    pass

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Poppins-Bold', 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(1.5*cm, A4[1] - 1*cm, "MENTORA ACADEMY")
    canvas.setFillColor(CRIMSON)
    canvas.drawString(1.5*cm + 100, A4[1] - 1*cm, "A C A D E M Y")
    canvas.setFont('Poppins-Regular', 8)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(A4[0] - 1.5*cm, A4[1] - 1*cm, "STUDENT — SUBJECT — LEVEL (CODE)")  # ← CHANGE
    canvas.setFont('Poppins-Regular', 8)
    canvas.drawString(1.5*cm, 1*cm, "Student · Subject (Code) — Study Planner YEAR")  # ← CHANGE
    canvas.setFont('Poppins-Bold', 8)
    canvas.drawRightString(A4[0] - 1.5*cm, 1*cm, f"{doc.page}")
    canvas.setFont('Poppins-SemiBold', 7)
    canvas.drawCentredString(A4[0]/2.0, 0.5*cm, "mentoraonlineacademy@gmail.com   •   +923164586836")
    canvas.restoreState()

def build_pdf():
    # [copy full build_pdf() function from build_hamna_planner.py]
    # Update: topics list, start_date, end_date, holiday range, cover page text
    pass

if __name__ == "__main__":
    build_pdf()
    print(f"Generated PDF: {OUT_FILE}")
```

---

*Template created by Antigravity (AGY) for Mentora Academy — October 2026*  
*Reference PDF: `Hamna_AS_Biology_Planner_2026_2027.pdf` (171 pages, 287.9 KB)*
