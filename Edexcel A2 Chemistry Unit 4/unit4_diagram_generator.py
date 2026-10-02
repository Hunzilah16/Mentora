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
LIGHT_BG = "#f8fafc"

# ==============================================================================
# TOPIC 11: KINETICS 2 DIAGRAMS
# ==============================================================================

def gen_p1_q1_mg_hcl():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    t = np.linspace(0, 300, 200)
    v = 80 * (1 - np.exp(-0.015 * t))
    
    ax.plot(t, v, color=NAVY, linewidth=2.2, label='H2 Volume')
    # Tangent at t=0
    t_tan = np.linspace(0, 60, 50)
    v_tan = 1.2 * t_tan
    ax.plot(t_tan, v_tan, color=CRIMSON, linestyle='--', linewidth=1.8, label='Tangent at t=0s (Initial Rate = 1.20 cm3 s-1)')
    
    ax.set_title("Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)\nVolume of H2 Gas Produced vs Time", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    ax.set_xlabel("Time / s", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Volume of H2 / cm3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 300)
    ax.set_ylim(0, 90)
    ax.legend(fontsize=8, loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q1_mg_hcl.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q2_propanone_i2():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    t = np.linspace(0, 600, 100)
    abs_val = 1.20 - 0.0018 * t
    
    ax.plot(t, abs_val, color=CRIMSON, linewidth=2.2, label='Iodine Absorbance at 450 nm')
    ax.set_title("CH3COCH3 + I2 + H+ -> CH3COCH2I + 2H+ + I-\nAbsorbance vs Time (Colorimetry)", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    ax.set_xlabel("Time / s", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Absorbance (a.u.)", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 1.3)
    ax.annotate("Linear decrease -> Zero order w.r.t I2\nGradient = -k", xy=(300, 0.66), xytext=(350, 0.9),
                arrowprops=dict(facecolor=NAVY, shrink=0.05, width=1, headwidth=5),
                fontsize=8, fontweight='bold', color=NAVY)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q2_propanone_i2.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q6_zero_order_conctime():
    fig, ax = plt.subplots(figsize=(5.5, 3.5), dpi=300)
    t = np.linspace(0, 100, 100)
    conc = 1.0 - 0.008 * t
    
    ax.plot(t, conc, color=NAVY, linewidth=2.2)
    ax.set_title("Zero Order Reaction: Concentration vs Time", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Time / s", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("[Reactant] / mol dm-3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.1)
    ax.annotate("Constant rate = -gradient", xy=(50, 0.6), xytext=(55, 0.8),
                arrowprops=dict(facecolor=CRIMSON, shrink=0.05, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q6_zero_order_conctime.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q7_first_order_halflife():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    t = np.linspace(0, 400, 200)
    conc = 1.0 * np.exp(-0.005776 * t) # half-life = 120s
    
    ax.plot(t, conc, color=STEEL_BLUE, linewidth=2.2, label='[H2O2] Decay')
    
    # Half life marks
    ax.axhline(y=0.5, color=CRIMSON, linestyle='--', linewidth=1)
    ax.axvline(x=120, color=CRIMSON, linestyle='--', linewidth=1)
    ax.scatter([120], [0.5], color=CRIMSON, s=30, zorder=5)
    
    ax.axhline(y=0.25, color=CRIMSON, linestyle=':', linewidth=1)
    ax.axvline(x=240, color=CRIMSON, linestyle=':', linewidth=1)
    ax.scatter([240], [0.25], color=CRIMSON, s=30, zorder=5)
    
    ax.set_title("First Order Decay: 2H2O2 -> 2H2O + O2\nConstant Half-Life (t1/2 = 120 s)", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Time / s", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("[H2O2] / mol dm-3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 1.1)
    ax.annotate("t1/2 = 120 s", xy=(120, 0.5), xytext=(140, 0.55), fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax.annotate("2nd t1/2 = 120 s", xy=(240, 0.25), xytext=(260, 0.3), fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q7_first_order_halflife.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q20_arrhenius_n2o5():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    # 1/T points: 300K(0.00333), 310K(0.00323), 320K(0.00313), 330K(0.00303)
    inv_t = np.array([0.00303, 0.00313, 0.00323, 0.00333])
    ln_k = np.array([-3.90, -5.00, -6.10, -7.20])
    
    # Line fit
    x_line = np.linspace(0.00295, 0.00340, 100)
    y_line = -11000 * x_line + 29.43
    
    ax.plot(x_line, y_line, color=NAVY, linewidth=2.0, label='Best-Fit Line')
    ax.scatter(inv_t, ln_k, color=CRIMSON, s=50, zorder=5, label='Experimental Data Points')
    
    # Gradient triangle
    ax.plot([0.00303, 0.00333], [-7.20, -7.20], color=STEEL_BLUE, linestyle='--', linewidth=1.2)
    ax.plot([0.00303, 0.00303], [-3.90, -7.20], color=STEEL_BLUE, linestyle='--', linewidth=1.2)
    
    ax.set_title("Arrhenius Plot for 2N2O5 -> 4NO2 + O2\nln k against 1/T", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    ax.set_xlabel("1 / T (K^-1)", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("ln k", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.grid(True, linestyle=':', alpha=0.5)
    
    ax.annotate("Gradient = -Ea / R = -11000 K\nEa = +91.4 kJ mol-1", xy=(0.00318, -5.5), xytext=(0.00322, -4.5),
                arrowprops=dict(facecolor=CRIMSON, shrink=0.05, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax.legend(fontsize=8, loc='lower left')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q20_arrhenius_n2o5.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q23_maxwell_boltzmann_temp():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    E = np.linspace(0, 10, 200)
    
    N_300 = (E / 1.2) * np.exp(-E / 1.2)
    N_320 = (E / 1.6) * np.exp(-E / 1.6)
    
    ax.plot(E, N_300, color=NAVY, linewidth=2.2, label='T1 = 300 K')
    ax.plot(E, N_320, color=CRIMSON, linewidth=2.2, linestyle='--', label='T2 = 320 K (Higher Temperature)')
    
    ax.axvline(x=5.5, color=DARK_GREY, linestyle='-', linewidth=1.8, label='Ea (Activation Energy)')
    
    # Shade area for T2 > Ea
    E_shade = np.linspace(5.5, 10, 100)
    N_shade_320 = (E_shade / 1.6) * np.exp(-E_shade / 1.6)
    ax.fill_between(E_shade, N_shade_320, color=CRIMSON, alpha=0.25, label='Extra molecules with E >= Ea at 320 K')
    
    ax.set_title("Maxwell-Boltzmann Energy Distribution\nEffect of Increasing Temperature", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Kinetic Energy, E / arbitrary units", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Number of molecules with energy E", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q23_maxwell_boltzmann_temp.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

# ==============================================================================
# TOPIC 12: ENTROPY & LATTICE ENERGY DIAGRAMS
# ==============================================================================

def gen_p2_q15_entropy_vs_temp():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    
    # Solid region 0-100K
    T1 = np.linspace(0, 100, 50)
    S1 = 10 + 0.3 * T1
    # Melting jump at 100K
    T_m = [100, 100]
    S_m = [40, 70]
    # Liquid region 100-300K
    T2 = np.linspace(100, 300, 50)
    S2 = 70 + 0.25 * (T2 - 100)
    # Boiling jump at 300K
    T_b = [300, 300]
    S_b = [120, 220]
    # Gas region 300-450K
    T3 = np.linspace(300, 450, 50)
    S3 = 220 + 0.15 * (T3 - 300)
    
    ax.plot(T1, S1, color=NAVY, linewidth=2)
    ax.plot(T_m, S_m, color=CRIMSON, linewidth=2, linestyle='--')
    ax.plot(T2, S2, color=NAVY, linewidth=2)
    ax.plot(T_b, S_b, color=CRIMSON, linewidth=2, linestyle='--')
    ax.plot(T3, S3, color=NAVY, linewidth=2)
    
    ax.set_title("Standard Entropy, S°, vs Temperature, T\nPhase Transitions & Disorder Jumps", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Temperature / K", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Entropy, S° / J K-1 mol-1", fontsize=9, fontweight='bold', color=DARK_GREY)
    
    ax.annotate("Solid", xy=(50, 25), fontsize=8.5, fontweight='bold', color=NAVY)
    ax.annotate("Melting (Delta S_fusion)", xy=(100, 55), xytext=(120, 45), arrowprops=dict(arrowstyle="->", color=CRIMSON), fontsize=8, color=CRIMSON)
    ax.annotate("Liquid", xy=(200, 95), fontsize=8.5, fontweight='bold', color=NAVY)
    ax.annotate("Boiling (Delta S_vapourisation)", xy=(300, 170), xytext=(200, 180), arrowprops=dict(arrowstyle="->", color=CRIMSON), fontsize=8, color=CRIMSON)
    ax.annotate("Gas", xy=(380, 230), fontsize=8.5, fontweight='bold', color=NAVY)
    
    ax.grid(True, linestyle=':', alpha=0.4)
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p2_q15_entropy_vs_temp.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p3_q2_born_haber_nacl():
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
    
    # Energy levels for NaCl Born-Haber cycle
    levels = [
        ("Na(s) + 1/2 Cl2(g)", 0, NAVY),
        ("Na(g) + 1/2 Cl2(g)  [Delta_at H(Na) = +107]", 107, NAVY),
        ("Na+(g) + e- + 1/2 Cl2(g)  [IE1(Na) = +496]", 603, NAVY),
        ("Na+(g) + Cl(g) + e-  [1/2 Delta_at H(Cl2) = +122]", 725, NAVY),
        ("Na+(g) + Cl-(g)  [EA1(Cl) = -349]", 376, STEEL_BLUE),
        ("NaCl(s)  [Delta_f H = -411 kJ mol-1]", -411, CRIMSON)
    ]
    
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=0.8)
    for name, val, col in levels:
        ax.plot([1, 4.5], [val, val], color=col, linewidth=2.2)
        ax.text(4.7, val, name, verticalalignment='center', fontsize=7.5, fontweight='bold', color=col)
        
    # Lattice energy arrow
    ax.annotate("", xy=(2.75, -411), xytext=(2.75, 376),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2))
    ax.text(2.85, -10, "Delta_LE H(NaCl) = -787 kJ mol-1", fontsize=8.5, fontweight='bold', color=CRIMSON, rotation=90, verticalalignment='center')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(-500, 850)
    ax.set_ylabel("Enthalpy / kJ mol-1", fontsize=9.5, fontweight='bold', color=NAVY)
    ax.set_title("Born-Haber Cycle for Sodium Chloride, NaCl(s)", fontsize=10.5, fontweight='bold', color=NAVY)
    ax.axis('off')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p3_q2_born_haber_nacl.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p3_q10_born_haber_mgcl2():
    fig, ax = plt.subplots(figsize=(6.8, 5.0), dpi=300)
    
    levels = [
        ("Mg(s) + Cl2(g)", 0, NAVY),
        ("Mg(g) + Cl2(g)  [+148]", 148, NAVY),
        ("Mg+(g) + e- + Cl2(g)  [IE1 = +738]", 886, NAVY),
        ("Mg2+(g) + 2e- + Cl2(g)  [IE2 = +1451]", 2337, NAVY),
        ("Mg2+(g) + 2Cl(g) + 2e-  [2x122 = +244]", 2581, NAVY),
        ("Mg2+(g) + 2Cl-(g)  [2x(-349) = -698]", 1883, STEEL_BLUE),
        ("MgCl2(s)  [Delta_f H = -642 kJ mol-1]", -642, CRIMSON)
    ]
    
    for name, val, col in levels:
        ax.plot([1, 4.5], [val, val], color=col, linewidth=2.2)
        ax.text(4.7, val, name, verticalalignment='center', fontsize=7.2, fontweight='bold', color=col)
        
    ax.annotate("", xy=(2.75, -642), xytext=(2.75, 1883),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2))
    ax.text(2.85, 600, "Delta_LE H(MgCl2) = -2525 kJ mol-1", fontsize=8.5, fontweight='bold', color=CRIMSON, rotation=90, verticalalignment='center')
    
    ax.set_xlim(0, 11)
    ax.set_ylim(-800, 2800)
    ax.set_ylabel("Enthalpy / kJ mol-1", fontsize=9.5, fontweight='bold', color=NAVY)
    ax.set_title("Born-Haber Cycle for Magnesium Chloride, MgCl2(s)", fontsize=10.5, fontweight='bold', color=NAVY)
    ax.axis('off')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p3_q10_born_haber_mgcl2.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

# ==============================================================================
# TOPIC 14: ACID-BASE EQUILIBRIA & BUFFERS DIAGRAMS
# ==============================================================================

def gen_p6_q1_titration_ch3cooh_naoh():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    v = np.linspace(0, 50, 250)
    
    # CH3COOH vs NaOH titration curve
    ph_wa = 2.88 + (v/12.5)**0.4 * 1.88
    # steep jump near 25cm3
    idx_jump = (v >= 23.5) & (v <= 26.5)
    ph_wa[idx_jump] = 4.76 + (v[idx_jump] - 25.0) * 2.2
    ph_wa[v > 26.5] = 11.5 + (1 - np.exp(-0.15 * (v[v > 26.5] - 26.5))) * 1.5
    
    ax.plot(v, ph_wa, color=NAVY, linewidth=2.4, label='25.0 cm3 0.100 M CH3COOH vs 0.100 M NaOH')
    
    # Key points
    ax.scatter([0], [2.88], color=CRIMSON, s=35, zorder=5)
    ax.annotate("Initial pH = 2.88", xy=(0, 2.88), xytext=(2, 1.8), fontsize=8, fontweight='bold', color=CRIMSON)
    
    ax.scatter([12.5], [4.76], color=STEEL_BLUE, s=40, zorder=5)
    ax.annotate("Half-Equivalence Point\npH = pKa = 4.76", xy=(12.5, 4.76), xytext=(4, 6.2),
                arrowprops=dict(facecolor=STEEL_BLUE, shrink=0.05, width=1, headwidth=4),
                fontsize=8, fontweight='bold', color=STEEL_BLUE)
    
    ax.scatter([25.0], [8.72], color=CRIMSON, s=40, zorder=5)
    ax.annotate("Equivalence Point\n(V = 25.0 cm3, pH = 8.72)", xy=(25.0, 8.72), xytext=(27, 8.2),
                arrowprops=dict(facecolor=CRIMSON, shrink=0.05, width=1, headwidth=4),
                fontsize=8, fontweight='bold', color=CRIMSON)
    
    ax.axvline(x=25.0, color='gray', linestyle=':', linewidth=1)
    ax.set_title("Acid-Base Titration pH Curve\nWeak Acid (CH3COOH) vs Strong Base (NaOH)", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Volume of 0.100 mol dm-3 NaOH added / cm3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("pH", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.legend(fontsize=8, loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p6_q1_titration_ch3cooh_naoh.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p6_q15_titration_nh3_hcl():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    v = np.linspace(0, 50, 250)
    
    ph_wb = 11.1 - (v/12.5)**0.4 * 1.5
    idx_jump = (v >= 23.5) & (v <= 26.5)
    ph_wb[idx_jump] = 9.25 - (v[idx_jump] - 25.0) * 2.2
    ph_wb[v > 26.5] = 2.5 - (1 - np.exp(-0.15 * (v[v > 26.5] - 26.5))) * 1.2
    
    ax.plot(v, ph_wb, color=CRIMSON, linewidth=2.4, label='25.0 cm3 0.100 M NH3 vs 0.100 M HCl')
    
    ax.scatter([25.0], [5.28], color=NAVY, s=40, zorder=5)
    ax.annotate("Equivalence Point\n(V = 25.0 cm3, pH = 5.28)", xy=(25.0, 5.28), xytext=(28, 6.5),
                arrowprops=dict(facecolor=NAVY, shrink=0.05, width=1, headwidth=4),
                fontsize=8, fontweight='bold', color=NAVY)
    
    ax.set_title("Acid-Base Titration pH Curve\nWeak Base (NH3) vs Strong Acid (HCl)", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Volume of 0.100 mol dm-3 HCl added / cm3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("pH", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p6_q15_titration_nh3_hcl.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

# ==============================================================================
# TOPIC 15: SPECTROSCOPY & NMR DIAGRAMS
# ==============================================================================

def gen_p11_q1_nmr_ethyl_ethanoate():
    fig, ax = plt.subplots(figsize=(7, 3.2), dpi=300)
    shift = np.linspace(-0.5, 5.0, 1000)
    spectrum = np.zeros_like(shift)
    
    # TMS at 0.0 ppm
    spectrum += 1.0 * np.exp(-((shift - 0.0)/0.02)**2)
    # Triplet at 1.25 ppm (ratio 1:2:1)
    spectrum += 0.3 * np.exp(-((shift - 1.21)/0.012)**2)
    spectrum += 0.6 * np.exp(-((shift - 1.25)/0.012)**2)
    spectrum += 0.3 * np.exp(-((shift - 1.29)/0.012)**2)
    # Singlet at 2.04 ppm (ratio 3H)
    spectrum += 1.3 * np.exp(-((shift - 2.04)/0.02)**2)
    # Quartet at 4.12 ppm (ratio 1:3:3:1)
    spectrum += 0.2 * np.exp(-((shift - 4.06)/0.012)**2)
    spectrum += 0.6 * np.exp(-((shift - 4.10)/0.012)**2)
    spectrum += 0.6 * np.exp(-((shift - 4.14)/0.012)**2)
    spectrum += 0.2 * np.exp(-((shift - 4.18)/0.012)**2)
    
    ax.plot(shift, spectrum, color=NAVY, linewidth=1.6)
    ax.set_xlim(4.8, -0.3)
    ax.set_ylim(-0.1, 1.6)
    
    ax.set_title("1H High-Resolution NMR Spectrum of Ethyl Ethanoate (CH3COOCH2CH3)", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("Chemical Shift delta / ppm", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Relative Intensity", fontsize=9, fontweight='bold', color=DARK_GREY)
    
    ax.annotate("TMS Standard\n(0.0 ppm)", xy=(0.0, 1.05), fontsize=7, color=CRIMSON, ha='center')
    ax.annotate("Triplet (3H)\ndelta 1.25 ppm\n-CH3", xy=(1.25, 0.75), fontsize=7.5, color=NAVY, ha='center')
    ax.annotate("Singlet (3H)\ndelta 2.04 ppm\nCH3CO-", xy=(2.04, 1.38), fontsize=7.5, color=NAVY, ha='center')
    ax.annotate("Quartet (2H)\ndelta 4.12 ppm\n-OCH2-", xy=(4.12, 0.75), fontsize=7.5, color=NAVY, ha='center')
    
    ax.grid(True, linestyle=':', alpha=0.4)
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p11_q1_nmr_ethyl_ethanoate.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p11_q2_mass_spec_propanal():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=300)
    mz = [15, 28, 29, 57, 58, 59]
    abundance = [30, 40, 100, 15, 75, 2.5]
    
    ax.bar(mz, abundance, width=0.8, color=NAVY)
    ax.set_title("Mass Spectrum of Propanal (CH3CH2CHO, Mr = 58)", fontsize=10, fontweight='bold', color=NAVY)
    ax.set_xlabel("m/z ratio", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Relative Abundance (%)", fontsize=9, fontweight='bold', color=DARK_GREY)
    
    ax.annotate("Base Peak\n[C2H5]+ (m/z 29)", xy=(29, 102), fontsize=7.5, color=CRIMSON, ha='center')
    ax.annotate("Molecular Ion M+\n(m/z 58)", xy=(58, 77), fontsize=7.5, color=NAVY, ha='center')
    ax.annotate("M+1 (m/z 59)", xy=(59, 8), fontsize=6.5, color='gray', ha='center')
    
    ax.set_ylim(0, 115)
    ax.set_xlim(10, 65)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p11_q2_mass_spec_propanal.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q26_second_order_rateconc():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    conc = np.linspace(0, 1.0, 100)
    rate = 2.5 * (conc**2)
    
    ax.plot(conc, rate, color=NAVY, linewidth=2.2, label='Rate = k[A]^2')
    ax.set_title("Second Order Kinetics: Rate vs [A] Curve", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    ax.set_xlabel("[Reactant A] / mol dm-3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Initial Rate / mol dm-3 s-1", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 2.8)
    ax.annotate("Parabolic Curve\nDoubling [A] quadruples Rate (2^2 = 4)", xy=(0.6, 0.9), xytext=(0.15, 1.8),
                arrowprops=dict(facecolor=CRIMSON, shrink=0.05, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q26_second_order_rateconc.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p1_q30_initial_rates_plot():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
    t = np.linspace(0, 200, 100)
    c1 = 1.0 * np.exp(-0.01 * t)
    c2 = 0.5 * np.exp(-0.01 * t)
    c3 = 0.25 * np.exp(-0.01 * t)
    
    ax.plot(t, c1, color=NAVY, linewidth=2.0, label='Exp 1: [A]0 = 1.00 M')
    ax.plot(t, c2, color=CRIMSON, linewidth=2.0, label='Exp 2: [A]0 = 0.50 M')
    ax.plot(t, c3, color=STEEL_BLUE, linewidth=2.0, label='Exp 3: [A]0 = 0.25 M')
    
    # Tangents at t=0
    ax.plot([0, 50], [1.0, 0.5], color=NAVY, linestyle='--', linewidth=1.2)
    ax.plot([0, 50], [0.5, 0.25], color=CRIMSON, linestyle='--', linewidth=1.2)
    ax.plot([0, 50], [0.25, 0.125], color=STEEL_BLUE, linestyle='--', linewidth=1.2)
    
    ax.set_title("Initial Rates Method: [Reactant] vs Time Curves", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    ax.set_xlabel("Time / s", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("[Reactant A] / mol dm-3", fontsize=9, fontweight='bold', color=DARK_GREY)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p1_q30_initial_rates_plot.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p7_q1_chiral_enantiomer_3d():
    fig, ax = plt.subplots(figsize=(6, 3.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.25, 0.85, "(R)-Lactic Acid", fontsize=10, fontweight='bold', color=NAVY, ha='center')
    ax.text(0.75, 0.85, "(S)-Lactic Acid", fontsize=10, fontweight='bold', color=NAVY, ha='center')
    
    ax.plot([0.5, 0.5], [0.1, 0.9], color=CRIMSON, linestyle='--', linewidth=1.5)
    ax.text(0.5, 0.93, "Mirror Plane", fontsize=8.5, fontweight='bold', color=CRIMSON, ha='center')
    
    # Structure 1
    ax.text(0.25, 0.5, "COOH\n|\nCH3 — C* — OH\n|\nH", fontsize=10, fontweight='bold', color=DARK_GREY, ha='center', va='center')
    # Structure 2
    ax.text(0.75, 0.5, "COOH\n|\nHO — C* — CH3\n|\nH", fontsize=10, fontweight='bold', color=DARK_GREY, ha='center', va='center')
    
    ax.text(0.5, 0.05, "Non-Superimposable Mirror Image Enantiomers (Chiral Center *C)", fontsize=9, fontweight='bold', color=NAVY, ha='center')
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p7_q1_chiral_enantiomer_3d.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p8_q1_carbonyl_addition_mechanism():
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.15, 0.5, "R1\n \\\n  C = O: δ-\n /\nR2  δ+", fontsize=10, fontweight='bold', color=NAVY, ha='center', va='center')
    ax.text(0.35, 0.3, "+ :NC-  (Nucleophile)", fontsize=9.5, fontweight='bold', color=CRIMSON, ha='center', va='center')
    
    ax.annotate("", xy=(0.22, 0.5), xytext=(0.32, 0.35),
                arrowprops=dict(facecolor=CRIMSON, edgecolor=CRIMSON, arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=-0.3"))
    
    ax.text(0.52, 0.5, "--->", fontsize=14, fontweight='bold', color=DARK_GREY, ha='center', va='center')
    
    ax.text(0.80, 0.5, "    R1  :O:-\n    |  /\nCN— C*\n    |\n    R2\n(Tetrahedral Intermediate)", fontsize=9.5, fontweight='bold', color=NAVY, ha='center', va='center')
    
    ax.set_title("Nucleophilic Addition Mechanism to Carbonyl C=O Group", fontsize=10, fontweight='bold', color=NAVY, pad=10)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p8_q1_carbonyl_addition_mechanism.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p9_q1_carboxylic_acid_dimer():
    fig, ax = plt.subplots(figsize=(6, 3.0), dpi=300)
    ax.axis('off')
    
    dimer_text = "R — C = O • • • H — O\n     |               |\n     O — H • • • O = C — R"
    ax.text(0.5, 0.55, dimer_text, fontsize=11, fontweight='bold', color=NAVY, ha='center', va='center', family='monospace')
    ax.text(0.5, 0.15, "Carboxylic Acid Dimerisation via 2 Intermolecular Hydrogen Bonds (• • •)", fontsize=8.5, fontweight='bold', color=CRIMSON, ha='center')
    ax.set_title("Intermolecular Hydrogen Bonding in Carboxylic Acid Dimer", fontsize=10, fontweight='bold', color=NAVY, pad=8)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p9_q1_carboxylic_acid_dimer.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_p10_q1_pet_polyester_repeat_unit():
    fig, ax = plt.subplots(figsize=(6.5, 3.0), dpi=300)
    ax.axis('off')
    
    pet_text = "— [ O — CH2 — CH2 — O — C(=O) — C6H4 — C(=O) ] — n"
    ax.text(0.5, 0.55, pet_text, fontsize=10.5, fontweight='bold', color=NAVY, ha='center', va='center', family='monospace')
    ax.text(0.5, 0.15, "Terylene / PET Repeat Unit Showing Polar Ester Linkages (-COO-)", fontsize=8.5, fontweight='bold', color=CRIMSON, ha='center')
    ax.set_title("Repeat Unit Structure of Poly(ethylene terephthalate) PET", fontsize=10, fontweight='bold', color=NAVY, pad=8)
    
    plt.tight_layout()
    out_path = os.path.join(DIAGRAM_DIR, "p10_q1_pet_polyester_repeat_unit.png")
    plt.savefig(out_path)
    plt.close()
    return out_path

def gen_all_diagrams():
    p1 = gen_p1_q1_mg_hcl()
    p2 = gen_p1_q2_propanone_i2()
    p3 = gen_p1_q6_zero_order_conctime()
    p4 = gen_p1_q7_first_order_halflife()
    p5 = gen_p1_q20_arrhenius_n2o5()
    p6 = gen_p1_q23_maxwell_boltzmann_temp()
    p7 = gen_p2_q15_entropy_vs_temp()
    p8 = gen_p3_q2_born_haber_nacl()
    p9 = gen_p3_q10_born_haber_mgcl2()
    p10 = gen_p6_q1_titration_ch3cooh_naoh()
    p11 = gen_p6_q15_titration_nh3_hcl()
    p12 = gen_p11_q1_nmr_ethyl_ethanoate()
    p13 = gen_p11_q2_mass_spec_propanal()
    p14 = gen_p1_q26_second_order_rateconc()
    p15 = gen_p1_q30_initial_rates_plot()
    p16 = gen_p7_q1_chiral_enantiomer_3d()
    p17 = gen_p8_q1_carbonyl_addition_mechanism()
    p18 = gen_p9_q1_carboxylic_acid_dimer()
    p19 = gen_p10_q1_pet_polyester_repeat_unit()
    print("All custom question-specific diagram PNGs generated successfully!")

if __name__ == "__main__":
    gen_all_diagrams()

