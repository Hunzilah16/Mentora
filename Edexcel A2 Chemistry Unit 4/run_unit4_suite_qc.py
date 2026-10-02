import os
import sys

def run_pack_qc(pack_module):
    """
    Validates a single topical pack data module.
    """
    meta = pack_module.PACK_META
    questions = pack_module.QUESTIONS
    faqs = pack_module.FAQS
    
    errors = []
    
    # 1. Meta check
    for key in ['candidate', 'topic_code', 'topic_name', 'subtopic_code', 'subtopic_name']:
        if key not in meta or not meta[key]:
            errors.append(f"Missing metadata key: {key}")
            
    # 2. Candidate name check
    if meta.get('candidate') != 'Usman':
        errors.append(f"Incorrect candidate name: {meta.get('candidate')} (expected Usman)")
        
    # 3. Question check
    if len(questions) < 4:
        errors.append(f"Insufficient questions: {len(questions)} (minimum 4 required)")
        
    total_marks = sum(q.get('marks', 0) for q in questions)
    if total_marks < 20:
        errors.append(f"Total marks too low: {total_marks} (minimum 20 required)")
        
    # 4. Reference check
    edexcel_refs = [q for q in questions if 'WCH14' in q.get('ref', '') or 'Edexcel' in q.get('ref', '')]
    if len(edexcel_refs) / len(questions) < 0.75:
        errors.append(f"Low Edexcel past paper reference ratio: {len(edexcel_refs)}/{len(questions)}")
        
    # 5. Mark Scheme check
    for idx, q in enumerate(questions, 1):
        if not q.get('mark_scheme'):
            errors.append(f"Q{idx} missing mark scheme")
            
    # 6. FAQ check
    if len(faqs) < 3:
        errors.append(f"Insufficient FAQs: {len(faqs)} (minimum 3 required)")
        
    return errors, total_marks, len(questions), len(faqs)

if __name__ == "__main__":
    print("Master Unit 4 Suite QC Runner Initialized.")
