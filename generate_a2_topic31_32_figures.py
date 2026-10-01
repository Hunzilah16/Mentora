"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for:
- Topic 31: Halogen Compounds
- Topic 32: Hydroxy Compounds (Phenol)
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
# Topic 31: Figure 1: Relative Ease of Hydrolysis of Halogen Compounds
# -----------------------------------------------------------------------------
def create_halogen_hydrolysis_comparison():
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)

    compounds = ['Ethanoyl chloride\n(Acyl halide)', 'Chloroethane\n(Alkyl halide)', 'Chlorobenzene\n(Aryl halide)']
    # Relative reactivity scale (qualitative bar chart)
    reactivity = [100, 45, 0.5]
    colors = ['#c2185b', '#1565c0', '#777777']

    bars = ax.bar(compounds, reactivity, color=colors, width=0.45, edgecolor='#0b1b36', lw=1.0)

    ax.text(0, 103, 'Vigorous with cold H2O\n(steamy HCl fumes)', ha='center', fontsize=6.8, color='#c2185b', fontweight='bold')
    ax.text(1, 48, 'Requires warm NaOH(aq)\n(moderate rate)', ha='center', fontsize=6.8, color='#1565c0', fontweight='bold')
    ax.text(2, 6, 'Completely INERT\n(no reaction with refluxing alkali)', ha='center', fontsize=6.8, color='#555555', fontweight='bold')

    ax.set_ylabel('Relative Ease of Hydrolysis (arbitrary)', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Relative Reactivity of Chlorine-Containing Compounds towards Hydrolysis', fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_ylim(0, 125)
    ax.grid(True, linestyle=':', alpha=0.4, axis='y')

    out_file = os.path.join(fig_dir, "a2_t31_halogen_hydrolysis_trend.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Topic 32: Figure 1: Relative Acidity Scale (Ethanol vs Water vs Phenol vs Carboxylic Acid)
# -----------------------------------------------------------------------------
def create_phenol_acidity_spectrum():
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)

    # pKa scale
    # Ethanol: 16.0
    # Water: 14.0
    # Phenol: 10.0
    # Ethanoic acid: 4.76
    species = [
        ('Ethanol\n(CH3CH2OH)', 16.0, '#555555', 'Least acidic\n(Ethoxide ion destabilised\nby +I ethyl group)'),
        ('Water\n(H2O)', 14.0, '#1565c0', 'Neutral baseline\n(Kw = 1.0 x 10^-14)'),
        ('Phenol\n(C6H5OH)', 10.0, '#a81717', 'Weakly acidic\n(Phenoxide anion stabilised\nby pi-ring delocalisation)'),
        ('Ethanoic acid\n(CH3COOH)', 4.76, '#2e7d32', 'Moderately acidic\n(Carboxylate anion stabilised\nover two oxygen atoms)')
    ]

    ax.plot([2, 18], [1, 1], color='#0b1b36', lw=2.0) # axis line
    ax.annotate('', xy=(1.5, 1), xytext=(18.5, 1), arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.5))
    ax.text(10, 0.4, r'Increasing Acid Strength $\longrightarrow$' '\n' r'Decreasing $\mathrm{p}K_\mathrm{a} \ (\mathrm{p}K_\mathrm{a} = -\log_{10} K_\mathrm{a})$',
            ha='center', fontsize=7.2, fontweight='bold', color='#0b1b36')

    for name, pka, col, desc in species:
        ax.plot(pka, 1, 'o', color=col, markersize=8)
        ax.plot([pka, pka], [1, 1.4], '-', color=col, lw=1.2)
        ax.text(pka, 1.5, f"{name}\npKa = {pka}", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color=col)
        ax.text(pka, 0.85, desc, ha='center', va='top', fontsize=6.0, color='#333333')

    ax.set_xlim(1.5, 18.5)
    ax.set_ylim(0.0, 2.4)
    ax.axis('off')
    ax.set_title(r'Relative Acid Strength Spectrum: Ethanol, Water, Phenol, and Ethanoic Acid', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t32_phenol_acidity_spectrum.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Topic 32: Figure 2: Phenoxide Resonance Delocalisation Scheme
# -----------------------------------------------------------------------------
def create_phenoxide_resonance_scheme():
    fig, ax = plt.subplots(figsize=(6.2, 2.5), dpi=220)

    # Schematic boxes showing phenoxide ion delocalising negative charge onto 2, 4, 6 positions
    ax.text(1.2, 1.3, 'Phenoxide ion\nC6H5O-', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.annotate('', xy=(2.7, 1.3), xytext=(2.0, 1.3), arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.5))

    ax.text(3.5, 1.3, 'Resonance delocalisation\nOxygen lone pair overlaps with\nbenzene pi-cloud',
            ha='center', va='center', fontsize=6.8, color='#a81717', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#a81717', lw=0.8))

    ax.annotate('', xy=(5.0, 1.3), xytext=(4.3, 1.3), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.5))

    ax.text(5.8, 1.3, 'Negative charge dispersed\nonto ortho & para carbons\n(2, 4, 6 positions)',
            ha='center', va='center', fontsize=6.8, color='#2e7d32', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=0.8))

    # Consequence note
    ax.text(3.5, 0.4, 'Consequence: Phenoxide is significantly more stable than ethoxide (where charge is localised on oxygen).\nThus phenol readily loses H+ to act as an acid, and the activated ring rapidly brominates to 2,4,6-tribromophenol.',
            ha='center', va='center', fontsize=6.5, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.2, 6.8)
    ax.set_ylim(0.0, 2.2)
    ax.axis('off')
    ax.set_title(r'Delocalisation of Negative Charge in the Phenoxide Anion ($\mathrm{C_6H_5O^-}$)', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t32_phenoxide_resonance.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_halogen_hydrolysis_comparison()
    create_phenol_acidity_spectrum()
    create_phenoxide_resonance_scheme()
    print("All Topic 31 and 32 figures successfully generated.")
