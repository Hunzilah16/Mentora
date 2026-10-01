"""
Generate high-DPI figures for Topic 22: Analytical Techniques.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial'],
    'axes.edgecolor': '#0b1b36',
    'axes.linewidth': 1.2,
    'grid.color': '#e2e8f0',
    'grid.linestyle': '--',
    'grid.alpha': 0.7,
})

def make_ir_correlation_chart():
    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=300)
    
    # Characteristic absorption ranges: (Bond, Class, Min cm-1, Max cm-1, Appearance, Color)
    absorptions = [
        ("O-H (alcohol)", "Hydrogen-bonded alcohols/phenols", 3200, 3600, "Strong, broad", "#0284c7"),
        ("O-H (carboxylic acid)", "Carboxylic acid dimer envelope", 2500, 3000, "Very broad, jagged", "#dc2626"),
        ("N-H (amine / amide)", "Primary/secondary amines & amides", 3300, 3500, "Medium, sharp / doublet", "#7c3aed"),
        ("C-H (alkene / arene)", "$sp^2$ C-H stretch", 3000, 3100, "Medium, sharp", "#059669"),
        ("C-H (alkane)", "$sp^3$ C-H stretch", 2850, 2950, "Strong / sharp", "#475569"),
        ("C=N (nitrile)", "Nitriles ($R-C\\equiv N$)", 2200, 2250, "Medium, sharp", "#d97706"),
        ("C=O (carbonyl)", "Aldehydes, ketones, acids, esters", 1640, 1750, "Very strong, sharp", "#b91c1c"),
        ("C=C (alkene)", "Alkenes ($R_2C=CR_2$)", 1620, 1680, "Variable, medium", "#16a34a"),
        ("C-O (alcohol/ester)", "Alcohols, esters, carboxylic acids", 1040, 1300, "Strong, sharp", "#ea580c"),
        ("Fingerprint Region", "Complex bending & skeletal modes", 400, 1500, "Unique identity barcode", "#94a3b8")
    ]
    
    y_positions = np.arange(len(absorptions))
    
    for i, (bond, desc, w_min, w_max, app, col) in enumerate(absorptions):
        width = w_max - w_min
        ax.barh(i, width, left=w_min, height=0.55, color=col, alpha=0.85, edgecolor='#0b1b36', lw=1.1)
        # Label inside or next to bar
        center = (w_min + w_max) / 2
        ax.text(center, i, f"{bond} ({w_min}-{w_max})", ha='center', va='center',
                fontsize=7.2, fontweight='bold', color='white' if col != "#94a3b8" else '#0b1b36')
        ax.text(4000, i, f"{app} - {desc}", ha='left', va='center', fontsize=6.3, color='#334155')
        
    ax.set_xlim(4100, 350)  # Inverted wavenumber axis (standard IR presentation)
    ax.set_ylim(-0.8, len(absorptions))
    ax.set_yticks(y_positions)
    ax.set_yticklabels([a[0] for a in absorptions], fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax.set_xlabel("Wavenumber / $\\mathrm{cm}^{-1}$ (Standard Inverted Scale)", fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_title("Cambridge International AS Chemistry (9701) Characteristic Infrared Absorption Ranges",
                 fontsize=10.5, fontweight='bold', color='#0b1b36', pad=12)
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig("figures/analysis_ir_spectra_correlation.png")
    plt.close()
    print("Generated figures/analysis_ir_spectra_correlation.png")

def make_ir_profiles():
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8.2, 5.8), sharex=True, dpi=300)
    
    wn = np.linspace(4000, 500, 1000)
    
    # 1. Propan-1-ol: Broad OH at 3350, CH at 2950, C-O at 1050
    t1 = np.ones_like(wn) * 95
    t1 -= 65 * np.exp(-((wn - 3350) / 160)**2)  # Broad O-H
    t1 -= 45 * np.exp(-((wn - 2960) / 35)**2)   # C-H stretch
    t1 -= 35 * np.exp(-((wn - 2880) / 30)**2)
    t1 -= 70 * np.exp(-((wn - 1050) / 45)**2)   # C-O stretch
    t1 -= 20 * np.exp(-((wn - 1460) / 25)**2)   # CH2 bend
    ax1.plot(wn, t1, color='#0284c7', lw=1.4)
    ax1.set_ylim(10, 105)
    ax1.set_ylabel("Transmittance / %", fontsize=7.5, fontweight='bold')
    ax1.set_title("Compound A: Propan-1-ol, $\\mathrm{CH_3CH_2CH_2OH}$ (Broad hydrogen-bonded O-H peak at 3200-3600 $\\mathrm{cm}^{-1}$, no C=O)",
                  fontsize=8.2, fontweight='bold', color='#0369a1', pad=4)
    ax1.annotate("Broad O-H stretch\n(3200-3600 $\\mathrm{cm}^{-1}$)", xy=(3350, 30), xytext=(3550, 45),
                 arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.2), fontsize=6.8, fontweight='bold', color='#0284c7')
    ax1.annotate("C-O stretch\n(1050 $\\mathrm{cm}^{-1}$)", xy=(1050, 25), xytext=(1250, 40),
                 arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.2), fontsize=6.8, fontweight='bold', color='#0284c7')
    ax1.grid(True, linestyle=':', alpha=0.5)

    # 2. Propanoic acid: Very broad OH at 2500-3000, C=O at 1715, C-O at 1240
    t2 = np.ones_like(wn) * 95
    t2 -= 55 * np.exp(-((wn - 3000) / 320)**2)  # Very broad carboxylic O-H envelope
    t2 -= 35 * np.exp(-((wn - 2950) / 30)**2)   # Jagged overlapping C-H
    t2 -= 25 * np.exp(-((wn - 2650) / 40)**2)   # O-H sub-band
    t2 -= 80 * np.exp(-((wn - 1715) / 22)**2)   # Sharp intense C=O
    t2 -= 50 * np.exp(-((wn - 1240) / 35)**2)   # C-O stretch
    ax2.plot(wn, t2, color='#dc2626', lw=1.4)
    ax2.set_ylim(10, 105)
    ax2.set_ylabel("Transmittance / %", fontsize=7.5, fontweight='bold')
    ax2.set_title("Compound B: Propanoic acid, $\\mathrm{CH_3CH_2COOH}$ (Very broad carboxylic O-H envelope 2500-3000 $\\mathrm{cm}^{-1}$ + sharp C=O at 1715 $\\mathrm{cm}^{-1}$)",
                  fontsize=8.2, fontweight='bold', color='#b91c1c', pad=4)
    ax2.annotate("Carboxylic O-H envelope\n(2500-3000 $\\mathrm{cm}^{-1}$)", xy=(2900, 35), xytext=(3300, 50),
                 arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.2), fontsize=6.8, fontweight='bold', color='#dc2626')
    ax2.annotate("Intense C=O stretch\n(1715 $\\mathrm{cm}^{-1}$)", xy=(1715, 15), xytext=(1950, 30),
                 arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.2), fontsize=6.8, fontweight='bold', color='#dc2626')
    ax2.grid(True, linestyle=':', alpha=0.5)

    # 3. Propanal: No OH, sharp C=O at 1730, aldehydic C-H Fermi doublet at 2720 & 2820
    t3 = np.ones_like(wn) * 95
    t3 -= 45 * np.exp(-((wn - 2970) / 30)**2)   # Alkyl C-H
    t3 -= 30 * np.exp(-((wn - 2820) / 25)**2)   # Aldehydic C-H doublet 1
    t3 -= 32 * np.exp(-((wn - 2720) / 25)**2)   # Aldehydic C-H doublet 2
    t3 -= 82 * np.exp(-((wn - 1730) / 20)**2)   # Aldehydic C=O
    t3 -= 25 * np.exp(-((wn - 1390) / 25)**2)
    ax3.plot(wn, t3, color='#7c3aed', lw=1.4)
    ax3.set_ylim(10, 105)
    ax3.set_ylabel("Transmittance / %", fontsize=7.5, fontweight='bold')
    ax3.set_xlabel("Wavenumber / $\\mathrm{cm}^{-1}$ (Inverted Scale)", fontsize=8.5, fontweight='bold')
    ax3.set_title("Compound C: Propanal, $\\mathrm{CH_3CH_2CHO}$ (No O-H absorption; strong C=O at 1730 $\\mathrm{cm}^{-1}$; twin aldehydic C-H at 2720 & 2820 $\\mathrm{cm}^{-1}$)",
                  fontsize=8.2, fontweight='bold', color='#6d28d9', pad=4)
    ax3.annotate("Aldehydic C-H doublet\n(2720 & 2820 $\\mathrm{cm}^{-1}$)", xy=(2720, 60), xytext=(2400, 35),
                 arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=1.2), fontsize=6.8, fontweight='bold', color='#7c3aed')
    ax3.annotate("Aldehyde C=O\n(1730 $\\mathrm{cm}^{-1}$)", xy=(1730, 13), xytext=(1500, 35),
                 arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=1.2), fontsize=6.8, fontweight='bold', color='#7c3aed')
    ax3.grid(True, linestyle=':', alpha=0.5)

    ax3.set_xlim(4000, 500)
    plt.tight_layout()
    plt.savefig("figures/analysis_ir_functional_group_profiles.png")
    plt.close()
    print("Generated figures/analysis_ir_functional_group_profiles.png")

def make_mass_spec_molecular_ion():
    fig, ax = plt.subplots(figsize=(8.2, 4.6), dpi=300)
    
    # Propan-2-one (Acetone, C3H6O, Mr = 58)
    # Peaks: m/z = 15 [CH3]+ (25%), 43 [CH3CO]+ (100% base peak), 58 [M]+ (28%), 59 [M+1]+ (0.92%)
    peaks = [
        (15, 25, "$[\\mathrm{CH_3}]^+$"),
        (27, 8, "$[\\mathrm{C_2H_3}]^+$"),
        (42, 12, "$[\\mathrm{CH_2CO}]^{+\\bullet}$"),
        (43, 100, "$[\\mathrm{CH_3CO}]^+$ (Base Peak)"),
        (58, 28, "$[\\mathrm{M}]^{+\\bullet} (M_r=58)$"),
        (59, 0.95, "$[\\mathrm{M+1}]^+$ ($^{13}\\mathrm{C}$)")
    ]
    
    for mz, abund, label in peaks:
        ax.vlines(mz, 0, abund, color='#0b1b36' if abund < 100 else '#dc2626', lw=2.2 if mz in (58, 59) else 1.8)
        if mz in (43, 58):
            ax.text(mz, abund + 2.5, f"{label}\nm/z = {mz} ({abund}%)", ha='center', va='bottom',
                    fontsize=7.2, fontweight='bold', color='#dc2626' if abund==100 else '#0b1b36')
        elif mz == 59:
            ax.text(mz + 0.8, abund + 12.0, f"{label}\nm/z = 59 (0.95%)", ha='left', va='bottom',
                    fontsize=7.0, fontweight='bold', color='#b45309')
            ax.annotate("", xy=(59, abund), xytext=(61, abund + 10),
                        arrowprops=dict(arrowstyle="->", color='#b45309', lw=1.2))
        else:
            ax.text(mz, abund + 2.0, f"m/z {mz}", ha='center', va='bottom', fontsize=6.5, color='#475569')
            
    # Cambridge Formula Box
    formula_text = (
        "Cambridge [M+1] Carbon-13 Calculation:\n"
        "$n = \\frac{100 \\times \\mathrm{abundance\\ of\\ [M+1]^+}}{1.1 \\times \\mathrm{abundance\\ of\\ [M]^+}}$\n"
        "$n = \\frac{100 \\times 0.95}{1.1 \\times 28.0} = \\frac{95}{30.8} = 3.08 \\approx 3\\ \\mathrm{carbon\\ atoms}$\n"
        "Molecular Formula Confirmed: $\\mathrm{C_3H_6O}$ ($M_r = 58$)"
    )
    ax.add_patch(plt.Rectangle((62, 45), 24, 50, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.5))
    ax.text(74, 70, formula_text, ha='center', va='center', fontsize=6.8, color='#14532d', linespacing=1.3)
    
    ax.set_xlim(10, 90)
    ax.set_ylim(0, 115)
    ax.set_xlabel("Mass-to-charge ratio ($m/z$)", fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_ylabel("Relative Abundance / %", fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_title("Mass Spectrum of Propan-2-one: Molecular Ion Peak $[M]^+$, Fragment Ions & $[M+1]^+$ Ratio",
                 fontsize=10.0, fontweight='bold', color='#0b1b36', pad=10)
    ax.grid(axis='y', linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig("figures/analysis_mass_spec_molecular_ion.png")
    plt.close()
    print("Generated figures/analysis_mass_spec_molecular_ion.png")

def make_mass_spec_isotope_patterns():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 4.4), dpi=300)
    
    # 1. Chlorine Isotopic Signatures (35Cl : 37Cl = 3 : 1)
    # Monochloroalkane: [M] : [M+2] = 3 : 1 (height 75 : 25 or 100 : 33.3)
    # Dichloroalkane: [M] : [M+2] : [M+4] = 9 : 6 : 1 (height 100 : 66.7 : 11.1)
    labels_cl = ['[M]^+ (35Cl)', '[M+2]^+ (37Cl)']
    heights_mono_cl = [75.0, 25.0]
    ax1.bar([1, 2], heights_mono_cl, color=['#0284c7', '#38bdf8'], width=0.45, edgecolor='#0b1b36', lw=1.2)
    ax1.text(1, 77, "35-Cl (100%)\nRatio 3", ha='center', va='bottom', fontsize=7.0, fontweight='bold', color='#0369a1')
    ax1.text(2, 27, "37-Cl (33.3%)\nRatio 1", ha='center', va='bottom', fontsize=7.0, fontweight='bold', color='#0284c7')
    
    # Dichloro sub-bars
    ax1.bar([3.2, 4.2, 5.2], [56.25, 37.5, 6.25], color=['#059669', '#10b981', '#6ee7b7'], width=0.45, edgecolor='#0b1b36', lw=1.2)
    ax1.text(3.2, 58, "[M]\nRatio 9", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#047857')
    ax1.text(4.2, 39, "[M+2]\nRatio 6", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#059669')
    ax1.text(5.2, 8, "[M+4]\nRatio 1", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#065f46')
    
    ax1.set_xticks([1.5, 4.2])
    ax1.set_xticklabels(["Monochloro (1 Cl atom)\n[M] : [M+2] = 3 : 1", "Dichloro (2 Cl atoms)\n[M] : [M+2] : [M+4] = 9 : 6 : 1"],
                        fontsize=7.2, fontweight='bold')
    ax1.set_ylim(0, 100)
    ax1.set_ylabel("Relative Intensity / %", fontsize=8.0, fontweight='bold')
    ax1.set_title("Chlorine ($^{35}\\mathrm{Cl}$ : $^{37}\\mathrm{Cl} \\approx 3:1$)\nIsotopic Multiplicity",
                  fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax1.grid(axis='y', linestyle=':', alpha=0.5)

    # 2. Bromine Isotopic Signatures (79Br : 81Br = 1 : 1)
    # Monobromoalkane: [M] : [M+2] = 1 : 1 (equal peak heights 50 : 50 or 100 : 100)
    # Dibromoalkane: [M] : [M+2] : [M+4] = 1 : 2 : 1 (height 25 : 50 : 25)
    heights_mono_br = [50.0, 50.0]
    ax2.bar([1, 2], heights_mono_br, color=['#dc2626', '#f87171'], width=0.45, edgecolor='#0b1b36', lw=1.2)
    ax2.text(1, 52, "79-Br\nRatio 1", ha='center', va='bottom', fontsize=7.0, fontweight='bold', color='#b91c1c')
    ax2.text(2, 52, "81-Br\nRatio 1", ha='center', va='bottom', fontsize=7.0, fontweight='bold', color='#b91c1c')
    
    # Dibromo sub-bars
    ax2.bar([3.2, 4.2, 5.2], [25.0, 50.0, 25.0], color=['#d97706', '#f59e0b', '#fcd34d'], width=0.45, edgecolor='#0b1b36', lw=1.2)
    ax2.text(3.2, 27, "[M]\nRatio 1", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#b45309')
    ax2.text(4.2, 52, "[M+2]\nRatio 2", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#d97706')
    ax2.text(5.2, 27, "[M+4]\nRatio 1", ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#b45309')
    
    ax2.set_xticks([1.5, 4.2])
    ax2.set_xticklabels(["Monobromo (1 Br atom)\n[M] : [M+2] = 1 : 1 (Twin)", "Dibromo (2 Br atoms)\n[M] : [M+2] : [M+4] = 1 : 2 : 1"],
                        fontsize=7.2, fontweight='bold')
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("Relative Intensity / %", fontsize=8.0, fontweight='bold')
    ax2.set_title("Bromine ($^{79}\\mathrm{Br}$ : $^{81}\\mathrm{Br} \\approx 1:1$)\nIsotopic Multiplicity",
                  fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax2.grid(axis='y', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig("figures/analysis_mass_spec_isotope_patterns.png")
    plt.close()
    print("Generated figures/analysis_mass_spec_isotope_patterns.png")

if __name__ == "__main__":
    make_ir_correlation_chart()
    make_ir_profiles()
    make_mass_spec_molecular_ion()
    make_mass_spec_isotope_patterns()
