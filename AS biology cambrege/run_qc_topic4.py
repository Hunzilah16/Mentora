"""
Quality Control Verification Script for Topic 4: Cell Membranes and Transport
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy
"""

import os
from topic4_membranes_transport_data import get_topic4_questions, get_topic4_faqs

def run_qc():
    print("=" * 70)
    print("RUNNING STRICT QUALITY CONTROL: TOPIC 4 CELL MEMBRANES & TRANSPORT")
    print("=" * 70)

    questions = get_topic4_questions()
    faqs = get_topic4_faqs()

    # 1. Question Count & Marks
    total_q = len(questions)
    total_marks = sum(sum(p.marks for p in q.parts) for q in questions)
    print(f"Total Questions: {total_q} (Target: 50)")
    print(f"Total Marks:     {total_marks} (Target: 220)")
    assert total_q == 50, f"Expected 50 questions, got {total_q}"
    assert total_marks == 220, f"Expected 220 marks, got {total_marks}"

    # 2. Section Tariff Verification
    sec_a = questions[:20]
    sec_b = questions[20:40]
    sec_c = questions[40:50]

    marks_a = sum(sum(p.marks for p in q.parts) for q in sec_a)
    marks_b = sum(sum(p.marks for p in q.parts) for q in sec_b)
    marks_c = sum(sum(p.marks for p in q.parts) for q in sec_c)

    print(f"Section A (Qs 1-20):   {len(sec_a)} Qs | {marks_a} Marks (Target: 120m)")
    print(f"Section B (Qs 21-40):  {len(sec_b)} Qs | {marks_b} Marks (Target: 80m)")
    print(f"Section C (Qs 41-50):  {len(sec_c)} Qs | {marks_c} Marks (Target: 20m)")

    assert marks_a == 120, f"Section A must be 120 marks, got {marks_a}"
    assert marks_b == 80, f"Section B must be 80 marks, got {marks_b}"
    assert marks_c == 20, f"Section C must be 20 marks, got {marks_c}"

    for i, q in enumerate(sec_a, 1):
        q_m = sum(p.marks for p in q.parts)
        assert q_m == 6, f"Q{q.number} in Section A has {q_m} marks (expected 6)"

    for i, q in enumerate(sec_b, 21):
        q_m = sum(p.marks for p in q.parts)
        assert q_m == 4, f"Q{q.number} in Section B has {q_m} marks (expected 4)"

    for i, q in enumerate(sec_c, 41):
        q_m = sum(p.marks for p in q.parts)
        assert q_m == 2, f"Q{q.number} in Section C has {q_m} marks (expected 2)"

    # 3. FAQ Segment Verification
    print(f"Examiner FAQs:   {len(faqs)} FAQs (Target: 10)")
    assert len(faqs) == 10, f"Expected 10 FAQs, got {len(faqs)}"
    for idx, f in enumerate(faqs, 1):
        assert f['q_num'] == idx, f"FAQ {idx} number mismatch"
        assert len(f['title']) > 10, f"FAQ {idx} title too short"
        assert len(f['model_answer']) > 50, f"FAQ {idx} answer too short"
        assert 'examiner_trap' in f and len(f['examiner_trap']) > 20, f"FAQ {idx} trap warning missing"

    # 4. Mark Scheme Completeness
    ms_count = sum(len(q.mark_scheme) for q in questions)
    print(f"Mark Scheme Items: {ms_count} marking items across 50 questions.")
    assert ms_count >= 50, f"Expected at least 50 mark scheme entries, got {ms_count}"

    # 5. Past Paper Authenticity Ratio
    authentic_count = sum(1 for q in questions if "9700" in q.title)
    authentic_pct = (authentic_count / total_q) * 100
    print(f"Authentic Past Paper References: {authentic_count}/50 ({authentic_pct:.1f}%) [Target >= 80%]")
    assert authentic_pct >= 80.0, f"Authentic past paper ratio must be >= 80%, got {authentic_pct:.1f}%"

    print("=" * 70)
    print("[ALL 5 TOPIC 4 QC CHECKS PASSED PERFECTLY]")
    print("=" * 70)

if __name__ == "__main__":
    run_qc()
