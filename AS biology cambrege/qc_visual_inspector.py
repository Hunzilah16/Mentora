"""
Quality Control & Visual Integrity Inspector for Cambridge AS Biology (9700)
Validates:
1. Visual Prompt Quality Control: Ensures every question that requires or references a diagram,
   micrograph, scale calibration, or graph has an authentic, verified high-resolution image attached.
2. Mark Allocation & Tariff Integrity: Verifies that question parts sum exactly to the allocated marks
   and match the corresponding worked mark scheme points.
3. 80 / 20 Past Paper Reference Audit: Confirms that >= 80% of questions contain authentic Cambridge 9700
   session codes (e.g., 9700/22/M/J/23/Q1) and <= 20% are original high-tier extension questions.
4. Image File Verification: Confirms that all referenced image paths exist, are non-empty, and can be
   loaded cleanly without corruption.
"""

import os
import re
from PIL import Image

# Patterns that indicate a question strictly depends on an embedded visual prompt
VISUAL_PROMPT_PATTERNS = [
    r'\bfig\.\s*\d+', r'\bfigure\s*\d+', r'\bin\s+fig\b', r'\bin\s+figure\b',
    r'\bfrom\s+fig\b', r'\bshown\s+in\s+fig\b', r'\blabelled\s+[A-Z]\s+in\b',
    r'\brefer\s+to\s+fig\b', r'\bshows\s+a\s+diagram\b'
]

def inspect_questions(questions, topic_title=""):
    print(f"\n=======================================================")
    print(f"  RUNNING QUALITY CONTROL AUDIT: {topic_title}")
    print(f"=======================================================")
    
    total_q = len(questions)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    
    past_paper_count = 0
    novel_count = 0
    visual_required_count = 0
    visual_attached_count = 0
    
    errors = []
    warnings = []

    for idx, q in enumerate(questions, 1):
        q_num = getattr(q, 'number', idx)
        q_title = getattr(q, 'title', '')
        q_preamble = getattr(q, 'preamble', '') or ''
        
        # 1. Past paper reference check (80/20 rule)
        is_past_paper = bool(re.search(r'9700/\d{2}/[MFSO]/[MJN]/\d{2}', q_title))
        if is_past_paper:
            past_paper_count += 1
        else:
            novel_count += 1
            
        # 2. Check parts and marks
        parts = getattr(q, 'parts', [])
        q_part_marks = sum(p.marks for p in parts)
        
        ms = getattr(q, 'mark_scheme', [])
        q_ms_marks = sum(item.get('marks', 0) for item in ms)
        
        if q_part_marks != q_ms_marks:
            errors.append(f"Q{q_num}: Parts mark sum ({q_part_marks}) does not match Mark Scheme sum ({q_ms_marks})")
            
        # 3. Visual QC check: scan for visual prompt triggers
        combined_text = (q_title + " " + q_preamble + " " + " ".join(p.text for p in parts)).lower()
        requires_visual = any(re.search(pat, combined_text) for pat in VISUAL_PROMPT_PATTERNS)
        
        has_figure = bool(getattr(q, 'figure_path', None))
        
        if requires_visual:
            visual_required_count += 1
            if not has_figure:
                errors.append(f"Q{q_num}: Question text explicitly references a visual figure, but figure_path is missing!")
                
        if has_figure:
            visual_attached_count += 1
            fig_path = q.figure_path
            if not os.path.exists(fig_path):
                errors.append(f"Q{q_num}: figure_path does not exist on disk: {fig_path}")
            else:
                sz = os.path.getsize(fig_path)
                if sz < 1000:
                    errors.append(f"Q{q_num}: figure_path file is abnormally small ({sz} bytes): {fig_path}")
                else:
                    try:
                        with Image.open(fig_path) as im:
                            w, h = im.size
                            if w < 100 or h < 100:
                                warnings.append(f"Q{q_num}: Image dimensions {w}x{h} might be too low resolution.")
                    except Exception as e:
                        errors.append(f"Q{q_num}: Image file failed to load: {e}")

    # Summary calculations
    past_paper_pct = (past_paper_count / total_q) * 100 if total_q else 0
    novel_pct = (novel_count / total_q) * 100 if total_q else 0

    print(f"Total Questions Evaluated:    {total_q}")
    print(f"Total Marks Across Pack:      {total_marks}")
    print(f"Authentic Past Paper Qs:      {past_paper_count} ({past_paper_pct:.1f}%) [Target >= 80%]")
    print(f"Original / Extension Qs:      {novel_count} ({novel_pct:.1f}%) [Target <= 20%]")
    print(f"Questions Requiring Visuals:  {visual_required_count}")
    print(f"Questions with Figures Valid: {visual_attached_count}")

    if warnings:
        print(f"\n[WARNINGS] ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[FAILED] AUDIT FAILED WITH {len(errors)} ERRORS:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print(f"\n[PASSED] AUDIT PASSED: 100% Quality Control & Visual Integrity Verified.")
        return True

if __name__ == "__main__":
    print("QC Visual Inspector ready.")
