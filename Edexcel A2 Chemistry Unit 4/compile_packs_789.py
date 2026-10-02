import sys
import os

# Add the directory to sys.path to allow importing local modules
sys.path.append(r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4")

from build_edexcel_u4_pdf import build_pdf_pack
import pack7_15A
import pack8_15B
import pack9_15C

def compile_pdfs():
    # Pack 7
    pack_meta, questions, faqs = pack7_15A.get_pack_data()
    out_file = os.path.join(r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4", "Usman_Edexcel_Chem_U4_15A_Chirality.pdf")
    build_pdf_pack(out_file, pack_meta, questions, faqs)
    print("Built Pack 7 PDF")
    
    # Pack 8
    pack_meta, questions, faqs = pack8_15B.get_pack_data()
    out_file = os.path.join(r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4", "Usman_Edexcel_Chem_U4_15B_Carbonyl_Compounds.pdf")
    build_pdf_pack(out_file, pack_meta, questions, faqs)
    print("Built Pack 8 PDF")
    
    # Pack 9
    pack_meta, questions, faqs = pack9_15C.get_pack_data()
    out_file = os.path.join(r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4", "Usman_Edexcel_Chem_U4_15C_Carboxylic_Acids.pdf")
    build_pdf_pack(out_file, pack_meta, questions, faqs)
    print("Built Pack 9 PDF")

if __name__ == "__main__":
    compile_pdfs()
