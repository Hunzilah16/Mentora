"""
Generate high-DPI figures for Topic 11: Group 17 (The Halogens).
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

def make_physical_trends():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=300)
    
    halogens = ['F', 'Cl', 'Br', 'I']
    # Boiling points of X2 in Kelvin: F2: 85K, Cl2: 239K, Br2: 332K, I2: 457K
    bp_x2 = [85, 239, 332, 457]
    # Boiling points of HX in Kelvin: HF: 293K (H-bonding), HCl: 188K, HBr: 206K, HI: 238K
    bp_hx = [293, 188, 206, 238]
    
    x = np.arange(len(halogens))
    
    ax1.plot(x, bp_x2, marker='o', color='#0b1b36', linewidth=2.2, label=r'Halogens, $X_2$')
    ax1.plot(x, bp_hx, marker='s', color='#a81717', linewidth=2.2, linestyle='--', label=r'Hydrogen Halides, $HX$')
    ax1.set_xticks(x)
    ax1.set_xticklabels([r'$\mathbf{F}$', r'$\mathbf{Cl}$', r'$\mathbf{Br}$', r'$\mathbf{I}$'], fontsize=10)
    ax1.set_ylabel("Boiling Point / K", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax1.set_title("Boiling Points of $X_2$ and $HX$", fontsize=10.5, fontweight='bold', color='#0b1b36', pad=10)
    ax1.grid(True)
    ax1.legend(loc='lower right', fontsize=8.5, frameon=True, facecolor='white', edgecolor='#0b1b36')
    ax1.annotate("HF anomalous due\nto Hydrogen Bonding", xy=(0, 293), xytext=(0.2, 360),
                 arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
                 fontsize=7.8, fontweight='bold', color='#a81717')
    
    # Bond enthalpies: X-X vs H-X
    # X-X: F-F: 158, Cl-Cl: 242, Br-Br: 193, I-I: 151
    # H-X: H-F: 562, H-Cl: 431, H-Br: 366, H-I: 299
    be_xx = [158, 242, 193, 151]
    be_hx = [562, 431, 366, 299]
    
    ax2.plot(x, be_hx, marker='^', color='#0284c7', linewidth=2.2, label=r'$H-X$ Bond Enthalpy (Thermal Stability)')
    ax2.plot(x, be_xx, marker='d', color='#e11d48', linewidth=2.2, label=r'$X-X$ Bond Enthalpy')
    ax2.set_xticks(x)
    ax2.set_xticklabels([r'$\mathbf{F}$', r'$\mathbf{Cl}$', r'$\mathbf{Br}$', r'$\mathbf{I}$'], fontsize=10)
    ax2.set_ylabel(r"Bond Enthalpy / $\mathrm{kJ\cdot mol^{-1}}$", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax2.set_title(r"Bond Enthalpies: $H-X$ and $X-X$", fontsize=10.5, fontweight='bold', color='#0b1b36', pad=10)
    ax2.grid(True)
    ax2.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='white', edgecolor='#0b1b36')
    ax2.annotate("F-F weakened by\nlone-pair repulsion", xy=(0, 158), xytext=(0.1, 80),
                 arrowprops=dict(arrowstyle='->', color='#e11d48', lw=1.2),
                 fontsize=7.8, fontweight='bold', color='#e11d48')
    
    plt.tight_layout()
    plt.savefig("figures/group17_physical_trends.png")
    plt.close()
    print("Generated figures/group17_physical_trends.png")

def make_displacement_solvent():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, "Halogen Colors in Aqueous vs Non-Polar (Cyclohexane) Layers", 
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 3 Test tubes: Chlorine, Bromine, Iodine
    tubes = [
        ("Chlorine ($Cl_2$)", 0.2, '#ecfdf5', '#d1fae5', "Pale yellow-green", "Pale green"),
        ("Bromine ($Br_2$)", 0.5, '#fff7ed', '#f97316', "Orange / yellow", "Orange / red-brown"),
        ("Iodine ($I_2$)", 0.8, '#f5f3ff', '#a855f7', "Brown / yellow-brown", "Deep Violet / Purple")
    ]
    
    for title, cx, col_aq, col_org, desc_aq, desc_org in tubes:
        w, h = 0.16, 0.55
        x0 = cx - w/2
        y0 = 0.22
        
        # Lower aqueous layer
        ax.add_patch(plt.Rectangle((x0, y0), w, h*0.5, facecolor=col_aq, edgecolor='#64748b', lw=1))
        # Upper organic (cyclohexane) layer
        ax.add_patch(plt.Rectangle((x0, y0 + h*0.5), w, h*0.4, facecolor=col_org, edgecolor='#64748b', lw=1))
        # Test tube outline
        ax.plot([x0, x0, x0+w, x0+w], [y0+h, y0, y0, y0+h], color='#0b1b36', lw=1.8)
        
        # Labels
        ax.text(cx, y0 + h + 0.05, title, ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#0b1b36')
        ax.text(cx, y0 + h*0.7, desc_org, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0b1b36')
        ax.text(cx, y0 + h*0.25, desc_aq, ha='center', va='center', fontsize=7.5, color='#334155')
        
    # Layer annotations on left
    ax.annotate("Upper Organic Layer\n(Cyclohexane)", xy=(0.12, 0.55), xytext=(0.02, 0.65),
                arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
                fontsize=8, fontweight='bold', color='#0b1b36')
    ax.annotate("Lower Aqueous Layer\n(Water)", xy=(0.12, 0.32), xytext=(0.02, 0.22),
                arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
                fontsize=8, fontweight='bold', color='#0b1b36')
    
    # Bottom note
    ax.text(0.5, 0.08, "Oxidising power: $Cl_2 > Br_2 > I_2$. Adding cyclohexane extracts halogens, giving distinctive non-polar colors.",
            ha='center', va='bottom', fontsize=8.2, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/group17_displacement_solvent.png")
    plt.close()
    print("Generated figures/group17_displacement_solvent.png")

def make_halides_conc_h2so4():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Reactions of Solid Sodium Halides with Concentrated Sulfuric Acid",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    cols = [
        ("Sodium Chloride ($NaCl$)", 0.18, "#0284c7",
         "Acid-base only\n(Cl⁻ cannot reduce H₂SO₄)",
         "• Steamy acidic fumes of HCl\n• White solid NaHSO₄\n• No redox reaction (S remains +6)"),
        ("Sodium Bromide ($NaBr$)", 0.50, "#ea580c",
         "Acid-base + Mild Redox\n(Br⁻ reduces S⁺⁶ to S⁺⁴)",
         "• Steamy fumes of HBr\n• Orange-brown fumes of Br₂\n• Choking gas SO₂ (S: +6 → +4)"),
        ("Sodium Iodide ($NaI$)", 0.82, "#7c3aed",
         "Acid-base + Strong Redox\n(I⁻ reduces S⁺⁶ to S⁺⁴, S⁰, S⁻²)",
         "• Steamy fumes of HI\n• Purple I₂ vapour / black solid\n• Choking gas SO₂ (S⁺⁴)\n• Yellow solid Sulfur (S⁰)\n• Bad-egg smell H₂S (S⁻²)")
    ]
    
    for title, cx, col, subtitle, details in cols:
        w = 0.28
        x0 = cx - w/2
        # Card
        ax.add_patch(plt.Rectangle((x0, 0.15), w, 0.70, facecolor='#f8fafc', edgecolor=col, lw=1.8, linestyle='-'))
        ax.add_patch(plt.Rectangle((x0, 0.75), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.80, title, ha='center', va='center', fontsize=8.8, fontweight='bold', color='white')
        ax.text(cx, 0.68, subtitle, ha='center', va='center', fontsize=7.8, fontweight='bold', color=col)
        ax.text(x0 + 0.015, 0.40, details, ha='left', va='center', fontsize=7.5, color='#1e293b', linespacing=1.4)
        
    ax.text(0.5, 0.05, "Reducing power of halide ions increases down Group 17:  $Cl^- < Br^- < I^-$\nLarger ionic radius → electrons held less tightly → lost more readily.",
            ha='center', va='bottom', fontsize=8.2, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/group17_halides_conc_h2so4.png")
    plt.close()
    print("Generated figures/group17_halides_conc_h2so4.png")

def make_silver_halides_nh3():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Qualitative Testing of Halide Ions ($AgNO_3$ followed by Aqueous $NH_3$)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    tests = [
        ("Chloride ($Cl^-$)", 0.2, '#f8fafc', '#0284c7', "White ppt\n($AgCl$)", "Dissolves\n(Colourless solution)", "Dissolves\n(Colourless solution)"),
        ("Bromide ($Br^-$)", 0.5, '#fef9c3', '#d97706', "Cream ppt\n($AgBr$)", "Insoluble\n(Remains cream)", "Dissolves\n(Colourless solution)"),
        ("Iodide ($I^-$)", 0.8, '#fef08a', '#a855f7', "Yellow ppt\n($AgI$)", "Insoluble\n(Remains yellow)", "Insoluble\n(Remains yellow)")
    ]
    
    for title, cx, col_bg, col_border, ppt_desc, dil_desc, conc_desc in tests:
        w = 0.26
        x0 = cx - w/2
        
        ax.add_patch(plt.Rectangle((x0, 0.16), w, 0.68, facecolor=col_bg, edgecolor=col_border, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.74), w, 0.10, facecolor=col_border, edgecolor=col_border, lw=1))
        ax.text(cx, 0.79, title, ha='center', va='center', fontsize=8.8, fontweight='bold', color='white')
        
        ax.text(cx, 0.65, r"$\mathbf{+ AgNO_3(aq):}$", ha='center', va='center', fontsize=7.8, color='#0b1b36')
        ax.text(cx, 0.56, ppt_desc, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0b1b36')
        
        ax.text(cx, 0.44, r"$\mathbf{+ Dilute\ NH_3(aq):}$", ha='center', va='center', fontsize=7.8, color='#0b1b36')
        ax.text(cx, 0.36, dil_desc, ha='center', va='center', fontsize=7.5, color='#334155')
        
        ax.text(cx, 0.26, r"$\mathbf{+ Conc\ NH_3(aq):}$", ha='center', va='center', fontsize=7.8, color='#0b1b36')
        ax.text(cx, 0.19, conc_desc, ha='center', va='center', fontsize=7.5, color='#334155')
        
    ax.text(0.5, 0.05, "Silver halide complexation: $AgX(s) + 2NH_3(aq) \\rightleftharpoons [Ag(NH_3)_2]^+(aq) + X^-(aq)$\nStability: $AgCl > AgBr > AgI$ in terms of solubility product $K_{sp}$.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/group17_silver_halides_nh3.png")
    plt.close()
    print("Generated figures/group17_silver_halides_nh3.png")

if __name__ == "__main__":
    make_physical_trends()
    make_displacement_solvent()
    make_halides_conc_h2so4()
    make_silver_halides_nh3()
