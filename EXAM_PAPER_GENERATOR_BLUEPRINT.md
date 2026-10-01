# Universal Exam Paper Generator Blueprint & System Replication Guide

## 1. Executive Summary & Purpose

This document serves as the master blueprint and reference model for autonomously generating publication-grade, syllabus-authentic topical past paper packs and mark schemes.
Originally engineered for **Mentora Academy** and candidate **Urwah** for **Cambridge International AS Chemistry (9701)**, this architecture is fully modular, parameterized, and designed for instant replication across:
- **Examination Boards**: Cambridge (CAIE), Pearson Edexcel, AQA, OCR (A & B), Scottish Highers, IB, and national curricula.
- **Academic Levels**: IGCSE / GCSE (O Level), AS Level, A Level (A2), International Baccalaureate (SL/HL).
- **Subjects**: Chemistry, Physics, Biology, Mathematics, Psychology, Economics, Computer Science, and more.

---

## 2. Visual Identity & Design System (Mentora Academy Standards)

### 2.1 Typography
All typography is powered by Google's **Poppins** geometric sans-serif family, registered locally via ReportLab's `TTFont`:
- `Poppins-Bold`: Primary headings, candidate names, question numbers, emphasis.
- `Poppins-SemiBold`: Sub-headers, section titles, table header labels.
- `Poppins-Medium`: Difficulty tags, metadata labels, mark scheme identifiers.
- `Poppins-Regular`: Body question text, syllabus descriptions, explanatory notes.
- `Poppins-Italic` & `Poppins-BoldItalic`: Chemical formulas, annotations, footnotes.

### 2.2 Palette & Color Tokens
- **Brand Navy (Primary):** `#0b1b36` (Cover title, main question numbers, primary headers, major rules).
- **Deep Navy (Accent):** `#132646` (Section banners, cover metadata borders).
- **Crimson Red (Brand Accent / Hard Badge):** `#a81717` (Letter-spaced academy sub-title, difficulty `HARD` badge, warning alerts).
- **Forest Green (Easy Badge / Success):** `#15803d` (Difficulty `EASY` badge, verification checkmarks).
- **Neutral Dark (Body Text):** `#20242e` (Question prompts, sub-parts, options).
- **Neutral Tint (Background Fill):** `#f5f3f0` or `#f8fafc` (Cover info card backgrounds, summary card fills).
- **Divider Gray:** `#cbd5e1` (Header/footer divider lines, table interior gridlines).

### 2.3 Page Geometry & Layout Specs
- **Page Format:** Standard A4 (`595.27 pt x 841.89 pt`).
- **Margins:** Left: `40 pt`, Right: `40 pt`, Top: `36 pt`, Bottom: `36 pt`.
- **Usable Content Width:** `515.27 pt`.
- **Usable Content Height:** `769.89 pt`.
- **Dotted Answer Line Spacing:** `14 pt` per line, dot radius `0.6 pt` spaced `3.0 pt` apart.
- **Multiple Choice Options:** Indented `32 pt` from left, vertical spacing `12 pt`.

---

## 3. Core Software Engine & Architecture

### 3.1 Data Model (Dataclasses)
```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class QuestionPart:
    label: str                   # e.g. "(a)", "(b)(i)"
    text: str                    # Full text with formatting & units
    marks: int                   # Raw mark allocation [n]
    num_answer_lines: int = 2    # Dotted lines rendered for student work
    options: List[str] = field(default_factory=list)  # MCQ options ["A: ...", "B: ..."]

@dataclass
class Question:
    number: int                  # Question sequence number (1, 2, ..., N)
    title: str                   # Topic title + authentic past paper reference code
    syllabus_ref: str            # e.g. "1.1", "22.2"
    difficulty: str              # "EASY" (#15803d) or "HARD" (#a81717)
    preamble: str                # Contextual stem / scenario / data table
    parts: List[QuestionPart]    # Structured subparts
    mark_scheme: List[dict]      # List of {"part": "(a)", "points": [...], "marks": n}
    figure_path: Optional[str] = None      # High-DPI diagram path
    figure_caption: Optional[str] = None   # "Fig. X.X: ..."
```

### 3.2 Dynamic Flow & Pagination Engine (`build_topic_pdf.py`)
1. **Cover Page Generator (`generate_cover_page`):**
   - Letter-spaced Academy title header (`M E N T O R A   A C A D E M Y`).
   - Dynamic candidate banner (`CANDIDATE: Urwah`).
   - Rounded metadata card (Subject, syllabus code, total marks, question count).
   - "How to Use This Pack" instructions.
   - "This Week at a Glance" syllabus syllabus bullet points with crimson triangle glyphs (`▸`).
   - Bottom branding & date range footer.
2. **Question Flow Generator (`generate_question_pages`):**
   - Running header with divider line on every page.
   - Section transition banners triggered when `syllabus_ref` changes.
   - Dynamic height budgeting: Calculates required height for preamble + figure + subparts + dotted lines. If `y - required_height < bottom_margin`, advances page automatically.
   - Running footer with academy name, candidate name, topic name, and page number.
3. **Mark Scheme Flow Generator (`generate_mark_scheme`):**
   - Auto-appended at the back of the pack.
   - Clean 3-column table format (`Q` | `EXAMINER MARKING POINTS / INDICATIVE CONTENT` | `MARKS`).
   - Sub-part labeling: `f"{q.number}({part_label})"`.
   - Auto-continuation header: `Mark Scheme (Continued)` on subsequent pages.
   - Right-aligned mark tallies.

---

## 4. Scientific Figure & Diagram Generation Pipeline

All diagrams, apparatus setups, graphs, and spectra are generated using Matplotlib with high-resolution settings:
- **Format:** High-DPI PNG (`dpi=300`), transparent or solid `#ffffff` background.
- **Mathtext Rendering Rules:**
  - Standard LaTeX math symbols only (`\Delta H`, `\rightleftharpoons`, `\rightarrow`, `^13\text{C}`).
  - **CRITICAL RESTRICTION:** Never use `\xrightarrow` or `\overset` (unsupported by Matplotlib's mathtext parser).
  - Explicit string concatenation or raw triple-quotes to prevent newline breakage.
- **Standardized Figure Types:**
  1. *Spectra:* IR correlation bar charts, simulated FTIR transmittance profiles, mass spectrometry bar spectra with molecular ion $[M]^+$, $[M+1]^+$, and isotopic clusters.
  2. *Thermodynamic / Kinetic Graphs:* Reaction pathway profiles, Maxwell-Boltzmann distributions, titration curves, Hess's Law cycles.
  3. *Apparatus & Organic Mechanisms:* Reaction roadmaps, distillation/reflux setups, polymer repeat unit schematics, retrosynthetic trees.

---

## 5. Multi-Board Reference Code Schemas

To adapt this generator for any other board, configure the question title schema as follows:

| Exam Board | Qualification Level | Standard Paper Reference Code Format | Example Code |
|---|---|---|---|
| **Cambridge (CAIE)** | AS & A Level | `[Syllabus]/[Component]/[Session]/[Year]/Q[Num]` | `9701/22/M/J/23/Q4` |
| **Cambridge (CAIE)** | IGCSE / O Level | `[Syllabus]/[Component]/[Session]/[Year]/Q[Num]` | `0620/42/M/J/23/Q2` |
| **Pearson Edexcel** | GCE AS & A Level | `[Spec Code]/[Paper Number]/[Session][Year]/Q[Num]` | `9CH0/01/Jun23/Q5` |
| **Pearson Edexcel** | International A Level (IAL) | `WCH1[Unit]/01/[Session][Year]/Q[Num]` | `WCH12/01/Jan23/Q3` |
| **AQA** | AS & A Level | `[Spec Code]/[Paper Number]/[Session][Year]/Q[Num]` | `7405/1/Jun23/Q4` |
| **AQA** | GCSE (9-1) | `[Spec Code]/[Paper Number]/[Tier]/[Session][Year]/Q[Num]` | `8462/1H/Jun23/Q6` |
| **OCR** | OCR A Level (Chemistry A) | `H432/[Paper Number]/[Session][Year]/Q[Num]` | `H432/01/Jun23/Q3` |
| **OCR** | OCR B (Salters Chemistry) | `H433/[Paper Number]/[Session][Year]/Q[Num]` | `H433/02/Jun23/Q5` |
| **IBO** | International Baccalaureate (IB) | `[Level]/[Subject]/Paper [Num]/[Session][Year]/TZ[Zone]/Q[Num]` | `HL/CHEM/P2/MAY23/TZ1/Q4` |

---

## 6. Multi-Subject Adaptation Protocols

| Subject | Core Layout Adaptations | Diagram / Equation Engine Requirements |
|---|---|---|
| **Chemistry** | Periodic tables, molecular structures, reaction pathways, spectra | Matplotlib organic roadmaps, mass spectra, IR tables, dot-and-cross |
| **Physics** | Circuit diagrams, vector polygons, wave profiles, field lines | Coordinate axes, force vectors, lens/ray diagrams, circuit components |
| **Biology** | Cell schematics, phylogenetic trees, genetic crosses, data graphs | Histological line diagrams, metabolic pathways, ecology food webs |
| **Mathematics** | Geometric coordinate plots, trigonometric waves, statistical trees | Function plots, normal distribution curves, Venn diagrams |
| **Psychology** | Case studies, methodology boxes, evaluation tables (AO1/AO2/AO3) | Research design flowcharts, brain structure diagrams, statistical bar charts |

---

## 7. Phase Two: Paper 1 (100-MCQ Edition) Architecture

### 7.1 Specifications for Phase Two
- **Target Papers:** Paper 1 (Multiple Choice) for all 22 topics.
- **Volume:** **Exactly 100 Multiple Choice Questions (MCQs)** per document.
- **Total Deliverable:** 22 Documents $\times$ 100 MCQs = **2,200 MCQs total**.
- **Candidate Branding:** `Urwah` | **Academy:** `Mentora Academy`.
- **Question Structure:**
  - 4 Options: `A`, `B`, `C`, `D`.
  - Authentic past paper reference code for every question.
  - Difficulty tag (`EASY` / `HARD`).
  - Diagram / graph stems where applicable.
- **Answer Key & Explanatory Guide:**
  - Compact quick-check answer grid at the back (e.g. 1: B, 2: D, 3: A, ...).
  - Detailed examiner explanation and distractor rationale for every question.
- **Pagination Optimization:**
  - Compact two-column or optimized single-column layout targeting ~20–25 pages per 100-MCQ pack.
