"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 28: Chemistry of Transition Elements
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
# Figure 1: Octahedral d-Orbital Splitting Diagram (t2g and eg)
# -----------------------------------------------------------------------------
def create_d_orbital_splitting():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)

    # 5 degenerate d-orbitals in isolated ion
    # Bar positions: x = 1 to 5
    for x in [1.0, 1.6, 2.2, 2.8, 3.4]:
        ax.plot([x, x + 0.4], [3.0, 3.0], color='#1565c0', lw=2.5)
    ax.text(2.4, 2.5, r'$\mathbf{Isolated\ Free\ Ion}$' '\n(5 degenerate 3d orbitals)', ha='center', fontsize=6.8, color='#1565c0', fontweight='bold')

    # Octahedral field splitting
    # Lower set: 3 orbitals (dxy, dyz, dxz) at y = 1.8
    for x in [5.5, 6.1, 6.7]:
        ax.plot([x, x + 0.4], [1.8, 1.8], color='#a81717', lw=2.5)
    ax.text(6.3, 1.2, r'$t_{2\mathrm{g}}\ (d_{xy},\ d_{yz},\ d_{xz})$' '\n' r'($-0.4\,\Delta_{\mathrm{oct}}$)', ha='center', fontsize=7.0, color='#a81717', fontweight='bold')

    # Upper set: 2 orbitals (dz2, dx2-y2) at y = 4.8
    for x in [5.8, 6.4]:
        ax.plot([x, x + 0.4], [4.8, 4.8], color='#c2185b', lw=2.5)
    ax.text(6.3, 5.2, r'$e_{\mathrm{g}}\ (d_{z^2},\ d_{x^2-y^2})$' '\n' r'($+0.6\,\Delta_{\mathrm{oct}}$)', ha='center', fontsize=7.0, color='#c2185b', fontweight='bold')

    # Barycentre dashed line
    ax.axhline(3.0, xmin=0.5, xmax=0.85, color='#777777', linestyle='--', lw=0.9)
    ax.text(7.6, 3.0, r'$\mathrm{Barycentre}$', va='center', fontsize=6.8, color='#777777', fontstyle='italic')

    # Arrow for Delta E / Delta_oct
    ax.annotate('', xy=(5.2, 4.8), xytext=(5.2, 1.8), arrowprops=dict(arrowstyle='<->', color='#0b1b36', lw=1.2))
    ax.text(4.8, 3.3, r'$\Delta E = h\nu$' '\n' r'$= \frac{hc}{\lambda}$', ha='right', va='center', fontsize=7.5, color='#0b1b36', fontweight='bold')

    # Electron promotion photon
    ax.annotate(r'$\mathrm{Visible\ light\ absorbed}$', xy=(5.5, 2.0), xytext=(3.5, 4.5),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.2, connectionstyle="arc3,rad=-0.2"),
                fontsize=7.0, color='#2e7d32', fontweight='bold')

    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(0.5, 6.0)
    ax.axis('off')
    ax.set_title(r'Crystal Field Splitting of 3d Orbitals in an Octahedral Complex Ion $[M(\mathrm{H_2O})_6]^{n+}$', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t28_d_orbital_splitting.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Stereoisomerism: Cisplatin vs Transplatin (Square Planar)
# -----------------------------------------------------------------------------
def create_cisplatin_stereoisomers():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.2, 2.8), dpi=220)

    # Cis-platin [Pt(NH3)2Cl2]
    # Pt at (0, 0)
    ax1.plot([0, -1], [0, 1], color='#0b1b36', lw=1.5)
    ax1.plot([0, 1], [0, 1], color='#0b1b36', lw=1.5)
    ax1.plot([0, -1], [0, -1], color='#0b1b36', lw=1.5)
    ax1.plot([0, 1], [0, -1], color='#0b1b36', lw=1.5)
    ax1.plot(0, 0, 'o', color='#1565c0', markersize=10)
    ax1.text(0, 0, 'Pt', color='white', ha='center', va='center', fontsize=7.5, fontweight='bold')

    # Cis: Cl and Cl adjacent (top left and bottom left)
    ax1.text(-1.1, 1.1, r'$\mathrm{Cl}$', color='#c2185b', ha='right', va='bottom', fontsize=8.0, fontweight='bold')
    ax1.text(-1.1, -1.1, r'$\mathrm{Cl}$', color='#c2185b', ha='right', va='top', fontsize=8.0, fontweight='bold')
    ax1.text(1.1, 1.1, r'$\mathrm{NH_3}$', color='#1565c0', ha='left', va='bottom', fontsize=8.0, fontweight='bold')
    ax1.text(1.1, -1.1, r'$\mathrm{NH_3}$', color='#1565c0', ha='left', va='top', fontsize=8.0, fontweight='bold')

    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title(r'$\mathbf{cis\text{-}platin}$' '\n' r'Bond angle $\mathrm{Cl\text{-}Pt\text{-}Cl} = 90^\circ$' '\n(Active anti-cancer drug)', fontsize=7.5, color='#a81717')

    # Trans-platin [Pt(NH3)2Cl2]
    ax2.plot([0, -1], [0, 1], color='#0b1b36', lw=1.5)
    ax2.plot([0, 1], [0, 1], color='#0b1b36', lw=1.5)
    ax2.plot([0, -1], [0, -1], color='#0b1b36', lw=1.5)
    ax2.plot([0, 1], [0, -1], color='#0b1b36', lw=1.5)
    ax2.plot(0, 0, 'o', color='#1565c0', markersize=10)
    ax2.text(0, 0, 'Pt', color='white', ha='center', va='center', fontsize=7.5, fontweight='bold')

    # Trans: Cl and Cl opposite (top left and bottom right)
    ax2.text(-1.1, 1.1, r'$\mathrm{Cl}$', color='#c2185b', ha='right', va='bottom', fontsize=8.0, fontweight='bold')
    ax2.text(1.1, -1.1, r'$\mathrm{Cl}$', color='#c2185b', ha='left', va='top', fontsize=8.0, fontweight='bold')
    ax2.text(1.1, 1.1, r'$\mathrm{NH_3}$', color='#1565c0', ha='left', va='bottom', fontsize=8.0, fontweight='bold')
    ax2.text(-1.1, -1.1, r'$\mathrm{NH_3}$', color='#1565c0', ha='right', va='top', fontsize=8.0, fontweight='bold')

    ax2.set_xlim(-1.8, 1.8)
    ax2.set_ylim(-1.8, 1.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title(r'$\mathbf{trans\text{-}platin}$' '\n' r'Bond angle $\mathrm{Cl\text{-}Pt\text{-}Cl} = 180^\circ$' '\n(Inactive therapeutically)', fontsize=7.5, color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t28_cisplatin_isomers.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Visible Light Absorption Spectrum & Complementary Colour Wheel
# -----------------------------------------------------------------------------
def create_colour_absorption_spectrum():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8), dpi=220)

    # Left: Absorption curve for [Cu(H2O)6]2+ (absorbs red/orange around 600-700 nm, transmits pale blue)
    wavelength = np.linspace(400, 750, 200)
    # Gaussian peak centered at 650 nm
    absorbance = 0.9 * np.exp(-((wavelength - 650) / 70)**2) + 0.05

    ax1.plot(wavelength, absorbance, color='#1565c0', lw=2.2)
    ax1.fill_between(wavelength, absorbance, color='#90caf9', alpha=0.3)
    ax1.axvline(650, color='#c2185b', linestyle=':', lw=1.0)
    ax1.text(650, 0.95, r'$\lambda_{\max} \approx 650\ \mathrm{nm}$' '\n(Absorbs red/orange light)', ha='center', fontsize=6.8, color='#c2185b', fontweight='bold')
    ax1.text(450, 0.35, r'$\mathbf{Transmitted}$' '\n' r'$\mathbf{light:}$' '\nPale blue', ha='center', fontsize=7.2, color='#1565c0', fontweight='bold')

    ax1.set_xlim(400, 750)
    ax1.set_ylim(0, 1.1)
    ax1.set_xlabel(r'Wavelength $\lambda$ / $\mathrm{nm}$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax1.set_ylabel(r'Absorbance', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax1.set_title(r'Absorption Spectrum of $[Cu(\mathrm{H_2O})_6]^{2+}$', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax1.grid(True, linestyle=':', alpha=0.4)

    # Right: Complementary colour wheel / pairs
    # Simple table or chart of absorbed vs transmitted
    colours_data = [
        ("Violet (~400 nm)", "Yellow-green (~560 nm)"),
        ("Blue (~450 nm)", "Yellow (~590 nm)"),
        ("Cyan (~490 nm)", "Orange-red (~620 nm)"),
        ("Green (~520 nm)", "Purple / Magenta"),
        ("Yellow (~580 nm)", "Dark blue (~450 nm)"),
        ("Red (~650 nm)", "Pale blue / Cyan (~490 nm)"),
    ]
    ax2.axis('off')
    table_text = "COMPLEMENTARY COLOUR PAIRS\n" + "-"*35 + "\n"
    for abs_c, trans_c in colours_data:
        table_text += f"Absorbed: {abs_c:<18} -> Appears: {trans_c}\n"
    ax2.text(0.05, 0.5, table_text, fontsize=6.5, family='monospace', va='center', color='#0b1b36',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', edgecolor='#0b1b36', lw=0.8))
    ax2.set_title(r'Light Absorption & Observed Colour', fontsize=7.8, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t28_colour_absorption_spectrum.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_d_orbital_splitting()
    create_cisplatin_stereoisomers()
    create_colour_absorption_spectrum()
    print("All Topic 28 figures successfully generated.")
