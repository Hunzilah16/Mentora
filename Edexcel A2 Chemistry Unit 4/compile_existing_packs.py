import os
import sys
import importlib
from build_edexcel_u4_pdf import build_pdf_pack

modules_to_build = [
    # Topic 11
    ("t11_1_rate_measurement", "Usman_Edexcel_Chem_U4_11A1_Rate_Measurement.pdf"),
    ("t11_2_rate_equations", "Usman_Edexcel_Chem_U4_11A2_Rate_Equations.pdf"),
    ("t11_3_determining_orders", "Usman_Edexcel_Chem_U4_11A3_Determining_Orders.pdf"),
    ("t11_4_mechanisms", "Usman_Edexcel_Chem_U4_11A4_Mechanisms.pdf"),
    ("t11_5_activation_energy", "Usman_Edexcel_Chem_U4_11A5_Activation_Energy.pdf"),
    ("t11_6_arrhenius_equation", "Usman_Edexcel_Chem_U4_11A6_Arrhenius_Equation.pdf"),
    
    # Topic 12
    ("t12_1_intro_entropy", "Usman_Edexcel_Chem_U4_12A1_Intro_Entropy.pdf"),
    ("t12_2_total_entropy", "Usman_Edexcel_Chem_U4_12A2_Total_Entropy.pdf"),
    ("t12_3_understanding_entropy", "Usman_Edexcel_Chem_U4_12A3_Entropy_Changes.pdf"),
    ("t12_4_lattice_energy", "Usman_Edexcel_Chem_U4_12B1_Lattice_Energy_Born_Haber.pdf"),
    ("t12_5_lattice_energies", "Usman_Edexcel_Chem_U4_12B2_Experimental_Theoretical_Lattice.pdf"),
    ("t12_6_solution_hydration", "Usman_Edexcel_Chem_U4_12B3_Solution_Hydration.pdf"),
    
    # Topic 13
    ("t13_1_kc", "Usman_Edexcel_Chem_U4_13A1_Equilibrium_Kc.pdf"),
    ("t13_2_kp", "Usman_Edexcel_Chem_U4_13A2_Equilibrium_Kp.pdf"),
    ("t13_3_factors1", "Usman_Edexcel_Chem_U4_13A3_Factors_Affecting_K1.pdf"),
    ("t13_4_factors2", "Usman_Edexcel_Chem_U4_13A4_Factors_Affecting_K2.pdf"),
    ("t13_5_entropy_k", "Usman_Edexcel_Chem_U4_13A5_Entropy_And_Equilibrium_Constants.pdf"),
    
    # Topic 14
    ("t14_1_bronsted", "Usman_Edexcel_Chem_U4_14A1_Bronsted_Lowry.pdf"),
    ("t14_2_ph_scale", "Usman_Edexcel_Chem_U4_14A2_pH_Scale.pdf"),
    ("t14_3_kw", "Usman_Edexcel_Chem_U4_14A3_Kw.pdf"),
    ("t14_4_ka_pka", "Usman_Edexcel_Chem_U4_14A4_Ka_pKa.pdf"),
    ("t14_5_titrations", "Usman_Edexcel_Chem_U4_14B1_Titrations_pH_Curves_Indicators.pdf"),
    ("t14_6_buffers", "Usman_Edexcel_Chem_U4_14B2_Buffer_Solutions.pdf"),
    ("t14_7_buffers_ph_curves", "Usman_Edexcel_Chem_U4_14B3_Buffers_and_pH_Curves.pdf"),
]

if __name__ == "__main__":
    count = 0
    for mod_name, pdf_name in modules_to_build:
        try:
            mod = importlib.import_module(mod_name)
            meta = mod.PACK_META
            questions = mod.QUESTIONS
            faqs = mod.FAQS
            
            build_pdf_pack(pdf_name, meta, questions, faqs)
            count += 1
            print(f"[{count}/{len(modules_to_build)}] Built {pdf_name}")
        except Exception as e:
            print(f"Error building {pdf_name}: {e}")
