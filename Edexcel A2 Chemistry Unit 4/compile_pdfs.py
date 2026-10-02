import os
import sys

# Ensure current directory is in path
sys.path.append(os.path.dirname(__file__))

import pack3_12B
import pack4_13A
from build_edexcel_u4_pdf import build_pdf_pack

def compile():
    # Build Pack 3
    print("Building Pack 3...")
    build_pdf_pack(
        pack3_12B.PACK_META,
        pack3_12B.QUESTIONS,
        pack3_12B.FAQS,
        output_filename="Usman_Edexcel_Chem_U4_12B_Lattice_Energy.pdf"
    )
    print("Pack 3 built successfully.")

    # Build Pack 4
    print("Building Pack 4...")
    build_pdf_pack(
        pack4_13A.PACK_META,
        pack4_13A.QUESTIONS,
        pack4_13A.FAQS,
        output_filename="Usman_Edexcel_Chem_U4_13A_Chemical_Equilibria.pdf"
    )
    print("Pack 4 built successfully.")

if __name__ == "__main__":
    compile()
