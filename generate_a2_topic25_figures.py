"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 25: Equilibria
Candidate: Urwah | Mentora Academy
"""
import os
import matplotlib.pyplot as plt
import numpy as np

fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"
os.makedirs(fig_dir, exist_ok=True)

plt.rcParams.update({
    'font.sans-serif': 'Arial',
    'font.family': 'sans-serif',
    'figure.autolayout': True,
    'axes.edgecolor': '#0b1b36',
    'axes.linewidth': 1.0,
})

# -----------------------------------------------------------------------------
# Figure 1: Weak Acid - Strong Base Titration Curve (Q1 / Q41)
# -----------------------------------------------------------------------------
def create_titration_curve_wa_sb():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    
    # 25.0 cm3 of 0.10 M CH3COOH (pKa = 4.76) titrated with 0.10 M NaOH
    V = np.linspace(0, 50, 200)
    # Simulated realistic titration curve
    pH = []
    for v in V:
        if v == 0:
            pH.append(2.88)
        elif v < 24.9:
            # Buffer region: pH = pKa + log(v / (25 - v))
            ratio = v / (25.0 - v)
            val = 4.76 + np.log10(ratio)
            pH.append(max(2.88, min(val, 7.0)))
        elif v <= 25.1:
            # Equivalence jump
            pH.append(8.87)
        else:
            # Excess NaOH: pOH = -log10((v - 25)*0.1 / (25 + v))
            excess_OH = ((v - 25.0) * 0.10) / (25.0 + v)
            pOH = -np.log10(excess_OH)
            pH.append(14.0 - pOH)

    pH = np.array(pH)
    ax.plot(V, pH, color='#a81717', lw=2.2, label=r'$\mathrm{CH_3COOH(aq)\ vs\ NaOH(aq)}$')

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.set_xlabel(r'Volume of $0.100\ \mathrm{mol\ dm^{-3}}\ \mathrm{NaOH}$ added / $\mathrm{cm^3}$', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'$\mathrm{pH}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Titration Curve of $25.0\ \mathrm{cm^3}$ of $0.100\ \mathrm{mol\ dm^{-3}}\ \mathrm{CH_3COOH}$ with $\mathrm{NaOH}$', fontsize=8.5, fontweight='bold', color='#0b1b36')

    # Half-equivalence point
    ax.plot(12.5, 4.76, 'o', color='#1565c0', markersize=5)
    ax.axvline(12.5, color='#1565c0', linestyle=':', lw=0.9)
    ax.axhline(4.76, color='#1565c0', linestyle=':', lw=0.9)
    ax.annotate(r'$\mathbf{Half\text{-}equivalence\ point}$' '\n' r'$V = 12.5\ \mathrm{cm^3},\ \mathrm{pH} = \mathrm{p}K_\mathrm{a} = 4.76$' '\n' r'$[\mathrm{CH_3COOH}] = [\mathrm{CH_3COO^-}]$',
                xy=(12.5, 4.76), xytext=(2, 6.8),
                arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.0), fontsize=6.8, color='#1565c0', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#1565c0', lw=0.6))

    # Equivalence point
    ax.plot(25.0, 8.87, 's', color='#2e7d32', markersize=5)
    ax.axvline(25.0, color='#2e7d32', linestyle=':', lw=0.9)
    ax.annotate(r'$\mathbf{Equivalence\ point}$' '\n' r'$V = 25.0\ \mathrm{cm^3},\ \mathrm{pH} = 8.87$' '\n(Alkaline due to salt hydrolysis)',
                xy=(25.0, 8.87), xytext=(28, 7.5),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.0), fontsize=6.8, color='#2e7d32', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#2e7d32', lw=0.6))

    # Phenolphthalein indicator range (pH 8.2 - 10.0)
    ax.axhspan(8.2, 10.0, color='#e91e63', alpha=0.15, label='Phenolphthalein range (pH 8.2–10.0)')
    ax.text(48, 9.1, 'Phenolphthalein', fontsize=6.2, color='#c2185b', ha='right', fontstyle='italic')

    # Methyl orange indicator range (pH 3.1 - 4.4)
    ax.axhspan(3.1, 4.4, color='#ff9800', alpha=0.15, label='Methyl orange range (pH 3.1–4.4 · Unsuitable)')
    ax.text(48, 3.7, 'Methyl orange (unsuitable)', fontsize=6.2, color='#e65100', ha='right', fontstyle='italic')

    # Buffer region shade
    ax.axvspan(5.0, 20.0, color='#1565c0', alpha=0.08)
    ax.text(12.5, 1.2, r'$\mathbf{Buffer\ Region}$' '\n' r'($\Delta\mathrm{pH}$ resisted)', ha='center', fontsize=6.5, color='#1565c0')

    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=6.5, loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')

    out_file = os.path.join(fig_dir, "a2_t25_titration_curves.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Comparative Four Acid-Base Titration Curves (Q2 / Q42)
# -----------------------------------------------------------------------------
def create_titration_four_types():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(6.2, 3.6), dpi=220)

    V = np.linspace(0, 50, 100)

    # 1. Strong Acid - Strong Base (HCl vs NaOH)
    pH1 = np.where(V < 24.9, 1.0 + (V/25.0)*0.5, np.where(V > 25.1, 13.0 - ((50-V)/25.0)*0.5, 7.0))
    # smooth curve
    pH1 = 1.0 + 12.0 / (1.0 + np.exp(-1.5 * (V - 25.0)))
    ax1.plot(V, pH1, color='#a81717', lw=1.8)
    ax1.set_title('Strong Acid – Strong Base (pH jump 3–11)', fontsize=7.2, fontweight='bold', color='#0b1b36')
    ax1.axhline(7.0, color='#2e7d32', linestyle=':', lw=0.8)
    ax1.set_ylim(0, 14); ax1.set_xlim(0, 50)
    ax1.grid(True, linestyle=':', alpha=0.4)

    # 2. Weak Acid - Strong Base (CH3COOH vs NaOH)
    pH2 = 2.8 + 10.0 / (1.0 + np.exp(-1.1 * (V - 25.0)))
    ax2.plot(V, pH2, color='#1565c0', lw=1.8)
    ax2.set_title('Weak Acid – Strong Base (Eq. pH = 8.9)', fontsize=7.2, fontweight='bold', color='#0b1b36')
    ax2.axhline(8.9, color='#2e7d32', linestyle=':', lw=0.8)
    ax2.axhspan(8.2, 10.0, color='#e91e63', alpha=0.15)
    ax2.set_ylim(0, 14); ax2.set_xlim(0, 50)
    ax2.grid(True, linestyle=':', alpha=0.4)

    # 3. Strong Acid - Weak Base (HCl vs NH3)
    pH3 = 1.0 + 8.5 / (1.0 + np.exp(-1.1 * (V - 25.0)))
    ax3.plot(V, pH3, color='#e65100', lw=1.8)
    ax3.set_title('Strong Acid – Weak Base (Eq. pH = 5.2)', fontsize=7.2, fontweight='bold', color='#0b1b36')
    ax3.axhline(5.2, color='#2e7d32', linestyle=':', lw=0.8)
    ax3.axhspan(3.1, 4.4, color='#ff9800', alpha=0.15)
    ax3.set_ylim(0, 14); ax3.set_xlim(0, 50)
    ax3.grid(True, linestyle=':', alpha=0.4)

    # 4. Weak Acid - Weak Base (CH3COOH vs NH3)
    pH4 = 3.0 + 6.0 / (1.0 + np.exp(-0.35 * (V - 25.0)))
    ax4.plot(V, pH4, color='#558b2f', lw=1.8)
    ax4.set_title('Weak Acid – Weak Base (No sharp jump)', fontsize=7.2, fontweight='bold', color='#0b1b36')
    ax4.axhline(7.0, color='#2e7d32', linestyle=':', lw=0.8)
    ax4.set_ylim(0, 14); ax4.set_xlim(0, 50)
    ax4.grid(True, linestyle=':', alpha=0.4)

    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_ylabel(r'$\mathrm{pH}$', fontsize=6.5)
        ax.set_xlabel(r'Volume added / $\mathrm{cm^3}$', fontsize=6.5)
        ax.tick_params(labelsize=6)

    out_file = os.path.join(fig_dir, "a2_t25_titration_four_types.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Solvent Extraction Partition Apparatus (Q10 / Q43)
# -----------------------------------------------------------------------------
def create_solvent_extraction():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Separating funnel body
    # Top stopper
    ax.plot([4.6, 5.4, 5.4, 4.6, 4.6], [9.2, 9.2, 9.6, 9.6, 9.2], color='#0b1b36', lw=1.5)
    ax.text(5.0, 9.75, 'Ground glass stopper', fontsize=6.5, ha='center', color='#0b1b36')

    # Pear-shaped funnel
    funnel_x = [4.6, 4.6, 3.0, 3.0, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 7.0, 7.0, 5.4, 5.4]
    funnel_y = [9.2, 8.5, 7.0, 5.0, 2.5, 2.0, 1.0, 1.0, 2.0, 2.5, 5.0, 7.0, 8.5, 9.2]
    ax.plot([4.6, 3.0, 3.0, 4.7, 4.7], [8.5, 7.0, 4.8, 2.5, 1.0], color='#0b1b36', lw=1.8)
    ax.plot([5.4, 7.0, 7.0, 5.3, 5.3], [8.5, 7.0, 4.8, 2.5, 1.0], color='#0b1b36', lw=1.8)
    ax.plot([4.6, 5.4], [8.5, 8.5], color='#0b1b36', lw=1.5)

    # Stopcock tap
    circle = plt.Circle((5.0, 2.0), 0.35, color='#a81717', fill=True, facecolor='#ffffff', lw=1.5)
    ax.add_patch(circle)
    ax.plot([4.4, 5.6], [2.0, 2.0], color='#a81717', lw=2.0)
    ax.text(6.3, 2.0, 'Stopcock tap', fontsize=6.5, color='#a81717', va='center')

    # Upper Layer (Organic solvent, e.g. ethoxyethane, d < 1.0 g/cm3)
    ax.fill_between([3.05, 6.95], 5.2, 7.2, color='#fff9c4', alpha=0.6)
    ax.plot([3.05, 6.95], [7.2, 7.2], color='#0b1b36', lw=0.8, linestyle='--')
    ax.plot([3.05, 6.95], [5.2, 5.2], color='#a81717', lw=1.2) # Meniscus / Interface
    ax.text(5.0, 6.2, r'$\mathbf{Organic\ Layer\ (Upper)}$' '\n' r'Solvent: $\mathrm{CH_3CH_2OCH_2CH_3}$' '\n' r'$[\mathrm{X}]_\mathrm{org} = C_1$', fontsize=6.8, ha='center', color='#f57f17', fontweight='bold')

    # Lower Layer (Aqueous phase, d = 1.0 g/cm3)
    ax.fill_between([3.05, 6.95], 4.8, 5.2, color='#bbdefb', alpha=0.6)
    # tapered lower fill
    ax.fill_between([4.7, 5.3], 2.5, 4.8, color='#bbdefb', alpha=0.6)
    ax.text(5.0, 3.8, r'$\mathbf{Aqueous\ Layer\ (Lower)}$' '\n' r'Water phase' '\n' r'$[\mathrm{X}]_\mathrm{aq} = C_2$', fontsize=6.8, ha='center', color='#1565c0', fontweight='bold')

    # Meniscus line label
    ax.annotate(r'$\mathbf{Phase\ Interface}$', xy=(3.5, 5.2), xytext=(1.2, 5.2),
                arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.0), fontsize=6.8, color='#a81717', fontweight='bold')

    # Partition Equilibrium Formula Box
    ax.text(5.0, 0.4, r'$\mathbf{Partition\ Coefficient:\ } K_\mathrm{pc} = \frac{[\mathrm{solute}]_\mathrm{organic}}{[\mathrm{solute}]_\mathrm{aqueous}} = \mathrm{constant}\quad (\mathrm{at\ constant\ } T)$',
            fontsize=7.2, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#0b1b36', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t25_solvent_extraction.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 4: Solubility Product & Common Ion Effect (Q14 / Q44)
# -----------------------------------------------------------------------------
def create_ksp_common_ion():
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)

    # Ca(OH)2: Ksp = 5.5 x 10^-6 mol3 dm-9
    # Ca(OH)2(s) <=> Ca2+(aq) + 2OH-(aq)
    # In pure water: [Ca2+] = s, [OH-] = 2s => Ksp = 4s^3 => s = (5.5e-6 / 4)^(1/3) = 0.0111 M
    # In presence of added NaOH [OH-]: s = Ksp / [OH-]^2
    c_OH = np.linspace(0.02, 0.50, 100)
    Ksp = 5.5e-6
    s = Ksp / (c_OH**2)

    ax.plot(c_OH, s * 1000, color='#a81717', lw=2.2, label=r'Solubility of $\mathrm{Ca(OH)_2}$')
    ax.set_xlim(0, 0.52)
    ax.set_ylim(0, 12)
    ax.set_xlabel(r'Concentration of added common ion $[\mathrm{OH^-}]_\mathrm{added}$ / $\mathrm{mol\ dm^{-3}}$', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Solubility of $\mathrm{Ca(OH)_2}$ / $\mathrm{10^{-3}\ mol\ dm^{-3}}$', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Common Ion Effect: Drastic Reduction in Molar Solubility ($K_\mathrm{sp}$ Constant)', fontsize=8.5, fontweight='bold', color='#0b1b36')

    # Pure water point
    s_pure = (Ksp / 4.0)**(1.0/3.0) * 1000 # 11.1 x 10^-3 M
    ax.plot(0, s_pure, 'o', color='#1565c0', markersize=6)
    ax.text(0.015, s_pure - 0.5, r'Pure water: $s = 1.11 \times 10^{-2}\ \mathrm{mol\ dm^{-3}}$', fontsize=7.0, color='#1565c0', fontweight='bold')

    # Added common ion point
    ax.plot(0.20, (Ksp / (0.20**2)) * 1000, 's', color='#2e7d32', markersize=6)
    ax.annotate(r'$[\mathrm{OH^-}] = 0.20\ \mathrm{M}\ \Rightarrow\ s = 1.38 \times 10^{-4}\ \mathrm{M}$' '\n(Solubility drops by > 98%)',
                xy=(0.20, (Ksp / (0.20**2)) * 1000), xytext=(0.22, 4.5),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.0), fontsize=6.8, color='#2e7d32', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#2e7d32', lw=0.6))

    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.0, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')

    out_file = os.path.join(fig_dir, "a2_t25_ksp_common_ion.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 5: Carbonate-Hydrogencarbonate Blood Buffer Equilibrium (Q5 / Q45)
# -----------------------------------------------------------------------------
def create_buffer_action():
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Central Box: Blood Buffer System
    ax.text(5.0, 5.8, r'$\mathbf{Carbonic\ Acid\ \text{--}\ Hydrogencarbonate\ Blood\ Buffer\ System}$' '\n'
                     r'$\mathbf{H_2CO_3(aq) \rightleftharpoons H^+(aq) + HCO_3^-(aq)}\quad (\mathrm{p}K_\mathrm{a} = 6.1,\ \mathrm{pH} = 7.40)$',
            fontsize=7.5, ha='center', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f1f5f9', edgecolor='#0b1b36', lw=1.2))

    # Left Box: Addition of H+ (Acidosis threat)
    ax.text(2.2, 2.4, r'$\mathbf{When\ Acid\ (H^+)\ is\ Added:}$' '\n'
                     r'$\mathrm{HCO_3^-(aq) + H^+(aq) \rightarrow H_2CO_3(aq)}$' '\n'
                     r'Excess $\mathrm{H_2CO_3}$ exhaled via lungs:' '\n'
                     r'$\mathrm{H_2CO_3 \rightarrow H_2O + CO_2(g)\uparrow}$' '\n'
                     r'$\mathbf{[\mathrm{H^+}]\ and\ \mathrm{pH}\ maintained}$',
            fontsize=6.8, ha='center', color='#1565c0',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#e3f2fd', edgecolor='#1565c0', lw=1.0))

    # Right Box: Addition of OH- (Alkalosis threat)
    ax.text(7.8, 2.4, r'$\mathbf{When\ Base\ (OH^-)\ is\ Added:}$' '\n'
                     r'$\mathrm{H_2CO_3(aq) + OH^-(aq) \rightarrow HCO_3^-(aq) + H_2O}$' '\n'
                     r'Depleted $\mathrm{H_2CO_3}$ replenished by' '\n'
                     r'dissolving metabolic $\mathrm{CO_2}$:' '\n'
                     r'$\mathbf{[\mathrm{H^+}]\ and\ \mathrm{pH}\ maintained}$',
            fontsize=6.8, ha='center', color='#a81717',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#ffebee', edgecolor='#a81717', lw=1.0))

    # Connectors
    ax.annotate('', xy=(2.2, 4.4), xytext=(3.5, 5.0), arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.3))
    ax.annotate('', xy=(7.8, 4.4), xytext=(6.5, 5.0), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.3))

    out_file = os.path.join(fig_dir, "a2_t25_buffer_action.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_titration_curve_wa_sb()
    create_titration_four_types()
    create_solvent_extraction()
    create_ksp_common_ion()
    create_buffer_action()
    print("All Topic 25 figures successfully generated.")
