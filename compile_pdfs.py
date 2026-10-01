"""
Compile all question batches into final styled PDFs.
Generates one PDF per major section (Physical, Inorganic, Organic, Analysis)
and one combined master PDF.
"""
import sys
import os
sys.path.insert(0, r"z:\tests n quizes63\books\psycology\new styl")

from generate_pdf import (
    Config, TopicSection, Question, QuestionPart,
    register_fonts, generate_worksheet
)

FONT_DIR = r"z:\tests n quizes63\books\psycology\new styl\fonts"
OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\output"

def load_all_batches():
    """Load and merge all question batches."""
    all_topics = []
    for batch_num in range(1, 6):
        mod = __import__(f"questions_batch{batch_num}")
        all_topics.extend(mod.topics)
    return all_topics

def renumber_questions(topics):
    """Renumber all questions sequentially across topics."""
    q_num = 1
    for topic in topics:
        for q in topic.questions:
            q.number = q_num
            q_num += 1
    return topics

def generate_section_pdf(section_name, topic_indices, all_topics, week_num, topic_area, date_range):
    """Generate a PDF for a specific section of topics."""
    section_topics = [all_topics[i] for i in topic_indices if i < len(all_topics)]
    
    # Renumber questions within this section
    q_num = 1
    for topic in section_topics:
        for q in topic.questions:
            q.number = q_num
            q_num += 1
    
    total_marks = sum(
        sum(p.marks for p in q.parts)
        for t in section_topics
        for q in t.questions
    )
    
    config = Config(
        candidate_name="Urwah",
        subject="Chemistry -- Cambridge International A Level (9701)",
        week_number=week_num,
        topic_area=topic_area,
        date_range=date_range,
        academy_name="MENTORA ACADEMY",
        total_marks=total_marks,
    )
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"Urwah_Chem_{section_name.replace(' ', '_')}.pdf"
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    generate_worksheet(output_path, config, section_topics, FONT_DIR)
    return output_path

def main():
    register_fonts(FONT_DIR)
    all_topics = load_all_batches()
    
    print(f"Loaded {len(all_topics)} topic sections, {sum(len(t.questions) for t in all_topics)} total questions")
    print()
    
    # Generate individual section PDFs
    sections = [
        {
            "name": "Physical_Chemistry",
            "indices": list(range(0, 9)),  # Topics 1-9 (batches 1+2)
            "week": 1,
            "area": "Physical Chemistry -- Topics 1-9: Atomic Structure to Reaction Kinetics",
            "dates": "AS Level Chemistry 9701 -- 2025-2027 Syllabus",
        },
        {
            "name": "Inorganic_Chemistry",
            "indices": list(range(9, 13)),  # Topics 10-12 + some of 13
            "week": 2,
            "area": "Inorganic Chemistry -- Topics 9-12: Periodicity to Nitrogen & Sulfur",
            "dates": "AS Level Chemistry 9701 -- 2025-2027 Syllabus",
        },
        {
            "name": "Organic_Chemistry",
            "indices": list(range(13, 21)),  # Topics 13-21
            "week": 3,
            "area": "Organic Chemistry -- Topics 13-21: Introduction to Organic Synthesis",
            "dates": "AS Level Chemistry 9701 -- 2025-2027 Syllabus",
        },
        {
            "name": "Analytical_Techniques",
            "indices": [21],  # Topic 22
            "week": 4,
            "area": "Analysis -- Topic 22: Analytical Techniques (IR & MS)",
            "dates": "AS Level Chemistry 9701 -- 2025-2027 Syllabus",
        },
    ]
    
    generated = []
    for section in sections:
        print(f"Generating: {section['name']}...")
        path = generate_section_pdf(
            section["name"],
            section["indices"],
            all_topics,
            section["week"],
            section["area"],
            section["dates"],
        )
        generated.append(path)
    
    # Generate master PDF with ALL topics
    print("\nGenerating: MASTER (all topics)...")
    master_topics = load_all_batches()  # Fresh load
    q_num = 1
    for topic in master_topics:
        for q in topic.questions:
            q.number = q_num
            q_num += 1
    
    total_marks = sum(
        sum(p.marks for p in q.parts)
        for t in master_topics
        for q in t.questions
    )
    
    master_config = Config(
        candidate_name="Urwah",
        subject="Chemistry -- Cambridge International A Level (9701)",
        week_number=1,
        topic_area="AS Level Chemistry -- Complete Topical Question Bank (Topics 1-22)",
        date_range="Cambridge 9701 Syllabus 2025-2027",
        academy_name="MENTORA ACADEMY",
        total_marks=total_marks,
    )
    
    master_path = os.path.join(OUTPUT_DIR, "Urwah_Chem_COMPLETE_Topical_Bank.pdf")
    generate_worksheet(master_path, master_config, master_topics, FONT_DIR)
    generated.append(master_path)
    
    print("\n" + "="*60)
    print("ALL PDFs GENERATED SUCCESSFULLY!")
    print("="*60)
    for path in generated:
        size = os.path.getsize(path)
        print(f"  {os.path.basename(path)} ({size//1024} KB)")


if __name__ == "__main__":
    main()
