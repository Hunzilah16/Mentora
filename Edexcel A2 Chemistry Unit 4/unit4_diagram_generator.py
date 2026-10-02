import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\Edexcel A2 Chemistry Unit 4\diagrams"
os.makedirs(DIAGRAM_DIR, exist_ok=True)

NAVY = "#0b1b36"
CRIMSON = "#a81717"
STEEL_BLUE = "#1e3a8a"
DARK_GREY = "#334155"

def gen_arrhenius_plot():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    inv_t = np.linspace(0.0028, 0.0035, 100)
    ln_k = -9000 * inv_t + 22
    
    ax.plot(inv_t, ln_k, color=NAVY, linewidth=2.5)
    ax.scatter([0.0029, 0.0031, 0.0033, 0.0034], [-9000*np.array([0.0029, 0.0031, 0.0033, 0.0034])+22], color=CRIMSON, s=40, zorder=5)
    
    ax.set_title(r"Arrhenius Plot: ln k vs 1/T", fontsize=11, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlabel("1 / T (K^-1)", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("ln k", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    ax.annotate("Gradient = -Ea / R", xy=(0.0031, -5.9), xytext=(0.0032, -4.5),
                arrowprops=dict(facecolor=CRIMSON, shrink=0.05, width=1.5, headwidth=6),
                fontsize=9, fontweight='bold', color=CRIMSON)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "arrhenius_plot.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_maxwell_boltzmann():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    E = np.linspace(0, 10, 200)
    N = (E / 1.5) * np.exp(-E / 1.5)
    
    ax.plot(E, N, color=NAVY, linewidth=2.5, label='Number of molecules')
    ax.axvline(x=6.0, color=CRIMSON, linestyle='--', linewidth=2, label='Ea (Uncatalysed)')
    ax.axvline(x=4.0, color=STEEL_BLUE, linestyle='-', linewidth=2, label='Ea (Catalysed)')
    
    E_cat_shade = np.linspace(4.0, 10, 100)
    N_cat_shade = (E_cat_shade / 1.5) * np.exp(-E_cat_shade / 1.5)
    ax.fill_between(E_cat_shade, N_cat_shade, color=STEEL_BLUE, alpha=0.3, label='Extra molecules with E >= Ea(cat)')
    
    ax.set_title("Maxwell-Boltzmann Energy Distribution", fontsize=11, fontweight='bold', color=NAVY)
    ax.set_xlabel("Kinetic Energy, E", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Number of molecules with energy E", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "maxwell_boltzmann.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_rate_conc_graphs():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 3), dpi=300)
    conc = np.linspace(0, 5, 100)
    
    ax1.plot(conc, np.ones_like(conc)*2, color=NAVY, linewidth=2)
    ax1.set_title("Zero Order (Rate = k)", fontsize=9, fontweight='bold', color=NAVY)
    ax1.set_xlabel("[Reactant]", fontsize=8)
    ax1.set_ylabel("Rate", fontsize=8)
    ax1.set_ylim(0, 4)
    ax1.grid(True, linestyle=':', alpha=0.4)
    
    ax2.plot(conc, 0.6*conc, color=CRIMSON, linewidth=2)
    ax2.set_title("1st Order (Rate = k[A])", fontsize=9, fontweight='bold', color=CRIMSON)
    ax2.set_xlabel("[Reactant]", fontsize=8)
    ax2.set_ylabel("Rate", fontsize=8)
    ax2.set_ylim(0, 4)
    ax2.grid(True, linestyle=':', alpha=0.4)
    
    ax3.plot(conc, 0.15*conc**2, color=STEEL_BLUE, linewidth=2)
    ax3.set_title("2nd Order (Rate = k[A]^2)", fontsize=9, fontweight='bold', color=STEEL_BLUE)
    ax3.set_xlabel("[Reactant]", fontsize=8)
    ax3.set_ylabel("Rate", fontsize=8)
    ax3.set_ylim(0, 4)
    ax3.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "rate_conc_graphs.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_born_haber_nacl():
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)
    
    levels = [
        ("Na(s) + 1/2 Cl2(g)", 0),
        ("Na(g) + 1/2 Cl2(g)", 107),
        ("Na+(g) + e- + 1/2 Cl2(g)", 603),
        ("Na+(g) + Cl(g) + e-", 725),
        ("Na+(g) + Cl-(g)", 376),
        ("NaCl(s)", -411)
    ]
    
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.8)
    for name, val in levels:
        color = CRIMSON if val < 0 else NAVY
        ax.plot([1, 4], [val, val], color=color, linewidth=2)
        ax.text(4.2, val, f"{name} ({val:+d} kJ)", verticalalignment='center', fontsize=8, fontweight='bold', color=color)
        
    ax.set_xlim(0, 8)
    ax.set_ylim(-500, 800)
    ax.set_ylabel("Enthalpy / kJ mol^-1", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_title("Born-Haber Cycle for Sodium Chloride (NaCl)", fontsize=11, fontweight='bold', color=NAVY)
    ax.axis('off')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "born_haber_nacl.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_titration_curves():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    v = np.linspace(0, 50, 200)
    
    ph_sa = 1 + 12 / (1 + np.exp(-(v - 25)/0.8))
    ph_wa = 2.9 + 9.5 / (1 + np.exp(-(v - 25)/1.2))
    
    ax.plot(v, ph_sa, color=NAVY, linewidth=2, label='Strong Acid (HCl) vs Strong Base (NaOH)')
    ax.plot(v, ph_wa, color=CRIMSON, linewidth=2, linestyle='--', label='Weak Acid (CH3COOH) vs Strong Base (NaOH)')
    
    ax.axvline(x=25, color='gray', linestyle=':', linewidth=1)
    ax.scatter([25], [7.0], color=NAVY, s=30, zorder=5)
    ax.scatter([25], [8.8], color=CRIMSON, s=30, zorder=5)
    
    ax.set_title("Acid-Base Titration pH Curves", fontsize=11, fontweight='bold', color=NAVY)
    ax.set_xlabel("Volume of 0.10 mol dm^-3 NaOH added / cm^3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("pH", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylim(0, 14)
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "titration_curves.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_nmr_spectrum():
    fig, ax = plt.subplots(figsize=(7, 3), dpi=300)
    
    shift = np.linspace(0, 5, 1000)
    spectrum = np.zeros_like(shift)
    
    spectrum += 1.0 * np.exp(-((shift - 0.0)/0.02)**2)
    spectrum += 0.4 * np.exp(-((shift - 1.16)/0.015)**2)
    spectrum += 0.8 * np.exp(-((shift - 1.20)/0.015)**2)
    spectrum += 0.4 * np.exp(-((shift - 1.24)/0.015)**2)
    spectrum += 1.2 * np.exp(-((shift - 2.0)/0.02)**2)
    spectrum += 0.2 * np.exp(-((shift - 4.04)/0.015)**2)
    spectrum += 0.6 * np.exp(-((shift - 4.08)/0.015)**2)
    spectrum += 0.6 * np.exp(-((shift - 4.12)/0.015)**2)
    spectrum += 0.2 * np.exp(-((shift - 4.16)/0.015)**2)
    
    ax.plot(shift, spectrum, color=NAVY, linewidth=1.5)
    ax.set_xlim(5, -0.5)
    ax.set_title("1H NMR Spectrum of Ethyl Ethanoate (CH3COOCH2CH3)", fontsize=11, fontweight='bold', color=NAVY)
    ax.set_xlabel("Chemical Shift delta / ppm", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Intensity", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.annotate("TMS (0 ppm)", xy=(0, 1.05), fontsize=7, color=CRIMSON, ha='center')
    ax.annotate("Triplet (3H)\n-CH3", xy=(1.2, 0.9), fontsize=7, color=NAVY, ha='center')
    ax.annotate("Singlet (3H)\nCH3CO-", xy=(2.0, 1.3), fontsize=7, color=NAVY, ha='center')
    ax.annotate("Quartet (2H)\n-OCH2-", xy=(4.1, 0.7), fontsize=7, color=NAVY, ha='center')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "nmr_spectrum.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_mass_spectrum():
    fig, ax = plt.subplots(figsize=(6, 3), dpi=300)
    
    mz = [15, 29, 43, 58, 59]
    abundance = [35, 45, 100, 70, 2.5]
    
    ax.bar(mz, abundance, width=0.8, color=NAVY)
    ax.set_title("Mass Spectrum of Propanal (C3H6O, Mr=58)", fontsize=11, fontweight='bold', color=NAVY)
    ax.set_xlabel("m/z ratio", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Relative Abundance (%)", fontsize=9, fontweight='bold', color=DARK_GREY)
    
    ax.annotate("[CH3CO]+ or [C3H7]+ (m/z 43)", xy=(43, 102), fontsize=7, color=CRIMSON, ha='center')
    ax.annotate("M+ (m/z 58)", xy=(58, 72), fontsize=7, color=NAVY, ha='center')
    ax.annotate("M+1 (m/z 59)", xy=(59, 10), fontsize=6, color='gray', ha='center')
    
    ax.set_ylim(0, 115)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "mass_spectrum.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

if __name__ == "__main__":
    p1 = gen_arrhenius_plot()
    p2 = gen_maxwell_boltzmann()
    p3 = gen_rate_conc_graphs()
    p4 = gen_born_haber_nacl()
    p5 = gen_titration_curves()
    p6 = gen_nmr_spectrum()
    p7 = gen_mass_spectrum()
    print("All Edexcel Unit 4 diagram graphics generated successfully!")
