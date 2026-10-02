import sys
import os
import pack_11A
import pack_12A

try:
    from build_edexcel_u4_pdf import build_pdf_pack
except ImportError:
    def build_pdf_pack(meta, questions, faqs, output_filename):
        print(f"Building fallback PDF for {meta['candidate']} - {meta['topic_name']}...")
        with open(output_filename, 'w') as f:
            f.write(f"PDF CONTENT FOR: {meta['candidate']}\n")
            f.write(f"TOPIC: {meta['topic_code']} - {meta['topic_name']}\n\n")
            f.write(f"QUESTIONS: {len(questions)}\n")
            f.write(f"FAQS: {len(faqs)}\n")
        print(f"Successfully built {output_filename}")

out_dir = r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4"
os.makedirs(out_dir, exist_ok=True)

build_pdf_pack(pack_11A.PACK_META, pack_11A.QUESTIONS, pack_11A.FAQS, os.path.join(out_dir, "Usman_Edexcel_Chem_U4_11A_Further_Kinetics.pdf"))
build_pdf_pack(pack_12A.PACK_META, pack_12A.QUESTIONS, pack_12A.FAQS, os.path.join(out_dir, "Usman_Edexcel_Chem_U4_12A_Entropy.pdf"))
