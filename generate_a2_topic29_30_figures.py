"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for:
- Topic 29: Intro to A2 Organic Chemistry
- Topic 30: Hydrocarbons (Arenes)
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
# Topic 29: Figure 1: 3D Wedge-Dash Enantiomers of Lactic Acid (Mirror Images)
# -----------------------------------------------------------------------------
def create_chiral_enantiomers_figure():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.2, 2.8), dpi=220)

    # Left: (R)-lactic acid
    ax1.plot([0, 0], [0, 1.2], color='#0b1b36', lw=1.8) # C-COOH
    ax1.plot([0, -1.1], [0, -0.6], color='#0b1b36', lw=1.8) # C-CH3
    ax1.plot([0, 0.9], [0, -0.7], color='#c2185b', lw=3.2) # C-OH (wedge)
    ax1.plot([0, 0.4], [0, -0.3], ':', color='#555555', lw=2.5) # C-H (dash)

    ax1.plot(0, 0, 'o', color='#1565c0', markersize=8)
    ax1.text(0, 0, 'C*', color='white', ha='center', va='center', fontsize=6.5, fontweight='bold')
    ax1.text(0, 1.35, r'$\mathrm{-COOH}$', color='#0b1b36', ha='center', fontsize=7.5, fontweight='bold')
    ax1.text(-1.2, -0.75, r'$\mathrm{-CH_3}$', color='#0b1b36', ha='right', fontsize=7.5, fontweight='bold')
    ax1.text(1.0, -0.85, r'$\mathrm{-OH}$' '\n(wedge)', color='#c2185b', ha='left', fontsize=6.8, fontweight='bold')
    ax1.text(0.5, -0.2, r'$\mathrm{-H}$ (dash)', color='#555555', ha='left', fontsize=6.5)

    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.4, 1.8)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title(r'$\mathbf{Enantiomer\ 1}$' '\n(+)-lactic acid', fontsize=7.5, color='#0b1b36')

    # Right: (S)-lactic acid (mirror image)
    ax2.plot([0, 0], [0, 1.2], color='#0b1b36', lw=1.8)
    ax2.plot([0, 1.1], [0, -0.6], color='#0b1b36', lw=1.8)
    ax2.plot([0, -0.9], [0, -0.7], color='#c2185b', lw=3.2)
    ax2.plot([0, -0.4], [0, -0.3], ':', color='#555555', lw=2.5)

    ax2.plot(0, 0, 'o', color='#1565c0', markersize=8)
    ax2.text(0, 0, 'C*', color='white', ha='center', va='center', fontsize=6.5, fontweight='bold')
    ax2.text(0, 1.35, r'$\mathrm{-COOH}$', color='#0b1b36', ha='center', fontsize=7.5, fontweight='bold')
    ax2.text(1.2, -0.75, r'$\mathrm{-CH_3}$', color='#0b1b36', ha='left', fontsize=7.5, fontweight='bold')
    ax2.text(-1.0, -0.85, r'$\mathrm{-OH}$' '\n(wedge)', color='#c2185b', ha='right', fontsize=6.8, fontweight='bold')
    ax2.text(-0.5, -0.2, r'$\mathrm{-H}$ (dash)', color='#555555', ha='right', fontsize=6.5)

    ax2.set_xlim(-1.8, 1.8)
    ax2.set_ylim(-1.4, 1.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title(r'$\mathbf{Enantiomer\ 2}$' '\n(-)-lactic acid', fontsize=7.5, color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t29_chiral_enantiomers.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Topic 30: Figure 1: Benzene Enthalpy of Hydrogenation & Resonance Stability
# -----------------------------------------------------------------------------
def create_benzene_resonance_energy():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)

    # Cyclohexene: -120 kJ/mol
    # Theoretical Kekule (cyclohexa-1,3,5-triene): 3 x (-120) = -360 kJ/mol
    # Real Benzene: -208 kJ/mol
    # Resonance energy: 152 kJ/mol
    levels = [
        ('Cyclohexene + H2', 0, 1.0, '#555555'),
        ('Cyclohexane (product)', -120, 1.0, '#555555'),
        ('Theoretical Kekulé\n(3 x double bonds)', 0, 4.0, '#c2185b'),
        ('Real Benzene\n(delocalised ring)', -152, 6.5, '#1565c0'),
        ('Cyclohexane (product)', -360, 5.2, '#2e7d32')
    ]

    # Reference baseline (reactants at top)
    ax.plot([0.5, 2.5], [0, 0], color='#555555', lw=2.0)
    ax.text(1.5, 12, 'Cyclohexene + H2', ha='center', fontsize=6.8, fontweight='bold', color='#555555')

    ax.plot([0.5, 2.5], [-120, -120], color='#555555', lw=2.0)
    ax.text(1.5, -135, 'Cyclohexane', ha='center', fontsize=6.8, color='#555555')
    ax.annotate(r'$\Delta H = -120\ \mathrm{kJ\ mol^{-1}}$', xy=(1.5, -60), fontsize=6.8, ha='center', color='#555555')
    ax.annotate('', xy=(2.0, -120), xytext=(2.0, 0), arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))

    # Theoretical Kekule
    ax.plot([3.5, 5.5], [0, 0], color='#c2185b', lw=2.0)
    ax.text(4.5, 12, r'$\mathbf{Kekul\acute{e}\ Triene}$' '\n(Theoretical)', ha='center', fontsize=6.8, fontweight='bold', color='#c2185b')

    # Real Benzene (lower by 152 kJ/mol)
    ax.plot([5.5, 7.5], [-152, -152], color='#1565c0', lw=2.5)
    ax.text(6.5, -140, r'$\mathbf{Real\ Benzene}$' '\n(Delocalised &pi; ring)', ha='center', fontsize=7.2, fontweight='bold', color='#1565c0')

    # Common product Cyclohexane
    ax.plot([3.5, 7.5], [-360, -360], color='#2e7d32', lw=2.0)
    ax.text(5.5, -380, 'Cyclohexane (from 3 H2)', ha='center', fontsize=6.8, color='#2e7d32')

    # Arrows
    # Kekule to product: -360 kJ/mol
    ax.annotate('', xy=(4.2, -360), xytext=(4.2, 0), arrowprops=dict(arrowstyle='->', color='#c2185b', lw=1.2))
    ax.text(3.4, -180, r'$\mathbf{Theoretical}$' '\n' r'$-360\ \mathrm{kJ\ mol^{-1}}$', ha='center', fontsize=6.5, color='#c2185b')

    # Real benzene to product: -208 kJ/mol
    ax.annotate('', xy=(7.0, -360), xytext=(7.0, -152), arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.2))
    ax.text(7.9, -250, r'$\mathbf{Experimental}$' '\n' r'$-208\ \mathrm{kJ\ mol^{-1}}$', ha='center', fontsize=6.5, color='#1565c0')

    # Resonance stabilisation energy arrow
    ax.annotate('', xy=(5.0, -152), xytext=(5.0, 0), arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.5))
    ax.text(5.1, -76, r'$\mathbf{Resonance\ Energy}$' '\n' r'$= 152\ \mathrm{kJ\ mol^{-1}}$' '\n(extra stability)', ha='left', fontsize=6.8, color='#a81717', fontweight='bold')

    ax.set_xlim(0, 8.5)
    ax.set_ylim(-410, 45)
    ax.set_ylabel(r'Enthalpy / $\mathrm{kJ\ mol^{-1}}$', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Enthalpy of Hydrogenation: Benzene vs Theoretical Kekulé Structure', fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_xticks([])
    ax.grid(True, linestyle=':', alpha=0.3, axis='y')

    out_file = os.path.join(fig_dir, "a2_t30_benzene_resonance_energy.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Topic 30: Figure 2: Electrophilic Aromatic Substitution Mechanism (Wheland Intermediate)
# -----------------------------------------------------------------------------
def create_electrophilic_substitution_mechanism():
    fig, ax = plt.subplots(figsize=(6.2, 2.6), dpi=220)

    # Step 1: Benzene + NO2+
    # Step 2: Wheland intermediate (horseshoe with + charge inside, H and NO2 attached)
    # Step 3: Nitrobenzene + H+
    ax.text(1.0, 1.5, r'$\mathbf{Benzene}$' '\n+ ' r'$\mathrm{NO_2^+}$', ha='center', va='center', fontsize=7.2, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.annotate('', xy=(2.4, 1.5), xytext=(1.7, 1.5), arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.5))
    ax.text(2.05, 1.8, r'$\mathbf{Slow\ (RDS)}$' '\nElectrophilic attack', ha='center', fontsize=6.2, color='#c2185b', fontweight='bold')

    ax.text(3.5, 1.5, r'$\mathbf{Arenium\ Intermediate}$' '\n' r'(Horseshoe $\pi$-system)' '\n' r'$[\mathrm{C_6H_6NO_2}]^+$',
            ha='center', va='center', fontsize=7.0, fontweight='bold', color='#c2185b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#c2185b', lw=0.8))

    ax.annotate('', xy=(5.0, 1.5), xytext=(4.4, 1.5), arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.5))
    ax.text(4.7, 1.8, 'Fast\nLoss of H+', ha='center', fontsize=6.5, color='#2e7d32', fontweight='bold')

    ax.text(6.0, 1.5, 'Nitrobenzene\n+ H+', ha='center', va='center', fontsize=7.2, fontweight='bold', color='#2e7d32',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=0.8))

    # Notes below
    note = "Key Features: Electrophile generated by HNO3 + 2H2SO4 <=> NO2+ + 2HSO4- + H3O+\nDelocalised pi-system temporarily broken in intermediate, then restored upon losing H+."
    ax.text(3.5, 0.4, note,
            ha='center', va='center', fontsize=6.8, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.2, 6.8)
    ax.set_ylim(0.0, 2.3)
    ax.axis('off')
    ax.set_title(r'Electrophilic Aromatic Substitution (Nitration of Benzene Mechanism)', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t30_nitration_mechanism.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_chiral_enantiomers_figure()
    create_benzene_resonance_energy()
    create_electrophilic_substitution_mechanism()
    print("All Topic 29 and 30 figures successfully generated.")
