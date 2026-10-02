import importlib
import glob
import os

try:
    from fpdf import FPDF
except ImportError:
    print("Please install fpdf: pip install fpdf")
    exit(1)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_text_color(11, 27, 54) # Mentora Navy #0b1b36
        self.cell(0, 10, 'Mentora Academy', 0, 1, 'C')
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

def create_pdf(module_name):
    # Import the module
    mod = importlib.import_module(module_name)
    meta = mod.PACK_META
    questions = mod.QUESTIONS
    faqs = mod.FAQS
    
    pdf = PDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(168, 23, 23) # Mentora Crimson #a81717
    pdf.cell(0, 10, f"Topic {meta['topic_code']}: {meta['topic_name']} - {meta['subtopic_code']} {meta['subtopic_name']}", 0, 1, 'C')
    
    pdf.set_font('Arial', 'I', 11)
    pdf.set_text_color(30, 58, 138) # Steel Blue #1e3a8a
    pdf.cell(0, 8, f"Candidate: {meta['candidate']} | {meta['contact']}", 0, 1, 'C')
    
    pdf.ln(10)
    
    # Questions
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, 'Exam Questions:', 0, 1)
    
    pdf.set_font('Arial', '', 11)
    for i, q in enumerate(questions, 1):
        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(0, 8, f"Q{i}. {q['question']} ({q['marks']} marks)")
        if q['type'] == 'MCQ':
            pdf.set_font('Arial', '', 10)
            for opt in q['options']:
                pdf.cell(0, 6, opt, 0, 1)
        pdf.set_font('Arial', 'I', 10)
        pdf.multi_cell(0, 6, f"Mark Scheme: {q['answer'] if q['type'] == 'MCQ' else q['mark_scheme']}")
        pdf.ln(5)
        
    # FAQs
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Examiner FAQs & Common Traps:', 0, 1)
    
    for i, f in enumerate(faqs, 1):
        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(0, 8, f"Q: {f['question']}")
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 6, f"A: {f['answer']}")
        pdf.ln(5)
        
    filename = f"{meta['candidate']}_Edexcel_Chem_U4_{meta['subtopic_code'].replace('.', '')}_{meta['subtopic_name'].replace(' ', '_')}.pdf"
    pdf.output(filename, 'F')
    print(f"Generated {filename}")

if __name__ == "__main__":
    modules = [
        "t12_1_intro_entropy",
        "t12_2_total_entropy",
        "t12_3_understanding_entropy",
        "t12_4_lattice_energy",
        "t12_5_lattice_energies",
        "t12_6_solution_hydration"
    ]
    for m in modules:
        try:
            create_pdf(m)
        except Exception as e:
            print(f"Failed to generate PDF for {m}: {e}")
