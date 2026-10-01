"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for:
- Topic 33: Carboxylic Acids & Acyl Chlorides
- Topic 34: Nitrogen Compounds
- Topic 35: Polymerisation
- Topic 36: Organic Synthesis
- Topic 37: Analytical Techniques
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

# =============================================================================
# Topic 33 Figures
# =============================================================================
def create_topic33_figures():
    # 1. Chloroethanoic acid acidity trend
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)
    acids = ['CH3COOH\nEthanoic', 'CH2ClCOOH\nMonochloro-', 'CHCl2COOH\nDichloro-', 'CCl3COOH\nTrichloro-']
    pka = [4.76, 2.86, 1.29, 0.65]
    colors = ['#555555', '#1565c0', '#00838f', '#c2185b']

    bars = ax.bar(acids, pka, color=colors, width=0.45, edgecolor='#0b1b36', lw=1.0)
    for bar, val in zip(bars, pka):
        y = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, y + 0.15, f"pKa = {val:.2f}", ha='center', fontsize=7.2, fontweight='bold', color='#0b1b36')

    ax.annotate('', xy=(3.3, 4.5), xytext=(0.2, 4.5),
                arrowprops=dict(arrowstyle='->', color='#c2185b', lw=1.5))
    ax.text(1.75, 4.75, r'Increasing Acid Strength $\longrightarrow$ (Greater $-I$ Inductive Delocalisation)',
            ha='center', fontsize=7.2, fontweight='bold', color='#c2185b')

    ax.set_ylabel(r'$\mathrm{p}K_\mathrm{a}$ Value (lower = stronger acid)', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Effect of Chlorine Substitution on the Acid Strength of Ethanoic Acid', fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_ylim(0, 5.5)
    ax.grid(True, linestyle=':', alpha=0.4, axis='y')

    out_file = os.path.join(fig_dir, "a2_t33_chloroethanoic_acidity_trend.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 2. Acyl chloride addition-elimination scheme
    fig, ax = plt.subplots(figsize=(6.2, 2.5), dpi=220)
    ax.text(1.0, 1.4, "Ethanoyl Chloride\nCH3-C(=O)-Cl\n+ H2O", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.annotate('Nucleophilic\nAttack (step 1)', xy=(2.5, 1.4), xytext=(1.8, 1.4),
                arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.5),
                ha='center', va='bottom', fontsize=6.2, color='#1565c0', fontweight='bold')

    ax.text(3.3, 1.4, "Tetrahedral\nIntermediate\n[CH3-C(O-)(OH2+)-Cl]", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#a81717',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#a81717', lw=0.8))

    ax.annotate('Elimination of\nCl- & H+ (step 2)', xy=(4.8, 1.4), xytext=(4.1, 1.4),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.5),
                ha='center', va='bottom', fontsize=6.2, color='#2e7d32', fontweight='bold')

    ax.text(5.5, 1.4, "Products\nCH3COOH\n+ HCl(g) fumes", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#2e7d32',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=0.8))

    ax.text(3.25, 0.4, "Key point: Carbonyl carbon is bonded to two electronegative atoms (O and Cl), creating a large delta+ charge.\nAddition occurs readily, followed by rapid loss of chloride as an excellent leaving group.",
            ha='center', va='center', fontsize=6.5, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.2, 6.3)
    ax.set_ylim(0.0, 2.2)
    ax.axis('off')
    ax.set_title(r'Nucleophilic Addition-Elimination Mechanism for Ethanoyl Chloride Hydrolysis', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t33_acyl_chloride_mechanism.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# =============================================================================
# Topic 34 Figures
# =============================================================================
def create_topic34_figures():
    # 1. Amine basicity scale
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)
    bases = [
        ('Phenylamine\n(C6H5NH2)', 4.6, '#a81717', 'Weakest base\nN lone pair delocalised\ninto benzene pi-system'),
        ('Ammonia\n(NH3)', 9.25, '#1565c0', 'Reference standard\nNo alkyl or aryl groups'),
        ('Ethylamine\n(CH3CH2NH2)', 10.7, '#2e7d32', 'Strongest base\n+I inductive effect of\nethyl pushes electrons to N')
    ]

    ax.plot([3, 12], [1, 1], color='#0b1b36', lw=2.0)
    ax.annotate('', xy=(12.2, 1), xytext=(3.0, 1), arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.5))
    ax.text(7.5, 0.4, r'Increasing Basicity (Greater Availability of Nitrogen Lone Pair) $\longrightarrow$' '\n' r'Increasing $\mathrm{p}K_\mathrm{b}$ of Conjugate Acid ($\mathrm{p}K_\mathrm{a}$ of $\mathrm{BH}^+$)',
            ha='center', fontsize=7.2, fontweight='bold', color='#0b1b36')

    for name, pka, col, desc in bases:
        ax.plot(pka, 1, 'o', color=col, markersize=8)
        ax.plot([pka, pka], [1, 1.35], '-', color=col, lw=1.2)
        ax.text(pka, 1.45, f"{name}\npKa(BH+) = {pka}", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color=col)
        ax.text(pka, 0.85, desc, ha='center', va='top', fontsize=6.0, color='#333333')

    ax.set_xlim(2.5, 12.8)
    ax.set_ylim(0.0, 2.3)
    ax.axis('off')
    ax.set_title(r'Relative Base Strengths of Phenylamine, Ammonia, and Ethylamine', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t34_amine_basicity_scale.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 2. Azo dye formation scheme
    fig, ax = plt.subplots(figsize=(6.2, 2.5), dpi=220)
    ax.text(1.2, 1.4, "Benzenediazonium ion\n[C6H5-N#N]+\n(formed at < 10 deg C)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#1565c0',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.text(2.6, 1.4, "+", ha='center', va='center', fontsize=10, fontweight='bold', color='#0b1b36')

    ax.text(3.5, 1.4, "Alkaline Phenol\n(C6H5O- in NaOH)\n(Electron-rich ring)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#c2185b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#c2185b', lw=0.8))

    ax.annotate('Coupling\n(0-10 deg C)', xy=(4.8, 1.4), xytext=(4.3, 1.4),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.5),
                ha='center', va='bottom', fontsize=6.2, color='#2e7d32', fontweight='bold')

    ax.text(5.5, 1.4, "Azo Dye (Yellow-Orange)\n4-hydroxyazobenzene\nC6H5-N=N-C6H4OH", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#e65100',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff3e0', edgecolor='#e65100', lw=0.8))

    ax.text(3.35, 0.4, "The azo group (-N=N-) bridges the two aromatic systems, creating an extended delocalised pi-system.\nThis absorbs visible light (blue-violet) and transmits bright yellow-orange light.",
            ha='center', va='center', fontsize=6.4, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.2, 6.5)
    ax.set_ylim(0.0, 2.2)
    ax.axis('off')
    ax.set_title(r'Electrophilic Coupling of Benzenediazonium Chloride with Phenol', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t34_azo_dye_coupling.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 3. Amino acid zwitterion titration / forms
    fig, ax = plt.subplots(figsize=(6.2, 2.6), dpi=220)
    ax.text(1.2, 1.5, "Low pH (< 2)\nCationic Form\n+H3N-CH(R)-COOH\n(Net charge +1)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#c2185b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#c2185b', lw=0.8))

    ax.annotate('+ OH-\n(loss of H+)', xy=(2.6, 1.5), xytext=(2.0, 1.5),
                arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
                ha='center', va='bottom', fontsize=5.8, color='#0b1b36')

    ax.text(3.3, 1.5, "Isoelectric Pt (pH ~6)\nZwitterion\n+H3N-CH(R)-COO-\n(Net charge 0)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#1565c0',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.annotate('+ OH-\n(loss of H+)', xy=(4.6, 1.5), xytext=(4.1, 1.5),
                arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
                ha='center', va='bottom', fontsize=5.8, color='#0b1b36')

    ax.text(5.4, 1.5, "High pH (> 10)\nAnionic Form\nH2N-CH(R)-COO-\n(Net charge -1)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#2e7d32',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=0.8))

    ax.text(3.3, 0.45, "In gel electrophoresis at buffer pH > isoelectric point, amino acid is negatively charged and moves to anode (+).\nAt buffer pH < isoelectric point, amino acid is positively charged and moves to cathode (-).",
            ha='center', va='center', fontsize=6.3, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.3, 6.3)
    ax.set_ylim(0.0, 2.3)
    ax.axis('off')
    ax.set_title(r'Ionic Forms of an Amino Acid as a Function of Solution pH', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t34_amino_acid_zwitterion.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# =============================================================================
# Topic 35 Figures
# =============================================================================
def create_topic35_figures():
    # 1. Condensation Polymers (Nylon 6,6 and Terylene)
    fig, ax = plt.subplots(figsize=(6.2, 2.7), dpi=220)
    ax.text(0.1, 2.0, "A. Nylon 6,6 (Polyamide)", fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax.text(0.3, 1.5, "Monomers: 1,6-diaminohexane + Hexanedioic acid\nRepeat unit: -[NH-(CH2)6-NH-CO-(CH2)4-CO]n-   (with elimination of H2O)\nLinkage: Amide / Peptide bond (-CO-NH-)", fontsize=6.8, color='#1565c0',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.text(0.1, 0.9, "B. Terylene / PET (Polyester)", fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax.text(0.3, 0.4, "Monomers: Benzene-1,4-dicarboxylic acid + Ethane-1,2-diol\nRepeat unit: -[CO-(C6H4)-CO-O-(CH2)2-O]n-   (with elimination of H2O)\nLinkage: Ester bond (-COO-)", fontsize=6.8, color='#c2185b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#c2185b', lw=0.8))

    ax.set_xlim(0, 6.0)
    ax.set_ylim(0, 2.4)
    ax.axis('off')
    ax.set_title(r'Structures and Repeat Units of Synthetic Condensation Polymers', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t35_condensation_polymers.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 2. Polymer Degradability Comparison
    fig, ax = plt.subplots(figsize=(6.2, 2.5), dpi=220)
    categories = ['Addition Polyalkenes\n(e.g. Polyethene)', 'Condensation Polyesters\n(e.g. Terylene)', 'Condensation Polyamides\n(e.g. Nylon 6,6)']
    ax.text(1.0, 1.5, "Addition Polymers\n- Non-polar C-C backbone\n- Resistant to chemical attack\n- Non-biodegradable\n- Persist in environment", ha='center', va='center', fontsize=6.6, color='#555555',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f5f5', edgecolor='#777777', lw=0.8))

    ax.text(3.3, 1.5, "Polyesters\n- Polar ester bond (C=O)\n- Readily hydrolysed by alkali\n  or strong acid\n- Biodegradable / Photodegradable", ha='center', va='center', fontsize=6.6, color='#c2185b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#c2185b', lw=0.8))

    ax.text(5.5, 1.5, "Polyamides\n- Polar amide bond (-CONH-)\n- Hydrolysed by hot aqueous\n  acid (HCl) or alkali (NaOH)\n- Cleavable into monomer salts", ha='center', va='center', fontsize=6.6, color='#1565c0',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.text(3.25, 0.35, "Environmental summary: Ester and amide linkages are vulnerable to nucleophilic attack by water/hydroxide ions,\nwhereas saturated hydrocarbon backbones have no delta+ carbon and do not hydrolyse.",
            ha='center', va='center', fontsize=6.3, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#b0aca4', lw=0.6))

    ax.set_xlim(0.0, 6.5)
    ax.set_ylim(0.0, 2.2)
    ax.axis('off')
    ax.set_title(r'Comparison of Chemical Degradability of Addition vs Condensation Polymers', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t35_polymer_degradability.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# =============================================================================
# Topic 36 Figure
# =============================================================================
def create_topic36_figures():
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)

    # Multi-step synthesis flowchart: Benzene -> Nitrobenzene -> Phenylamine -> Paracetamol / Benzenediazonium
    ax.text(0.9, 1.5, "Benzene\nC6H6", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f5f5', edgecolor='#0b1b36', lw=0.8))

    ax.annotate('Conc. HNO3 +\nConc. H2SO4\n(55 deg C)', xy=(2.0, 1.5), xytext=(1.4, 1.5),
                arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.2),
                ha='center', va='bottom', fontsize=5.8, color='#1565c0')

    ax.text(2.6, 1.5, "Nitrobenzene\nC6H5NO2", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#1565c0',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=0.8))

    ax.annotate('Sn + conc. HCl,\nthen NaOH(aq)', xy=(3.9, 1.5), xytext=(3.2, 1.5),
                arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.2),
                ha='center', va='bottom', fontsize=5.8, color='#2e7d32')

    ax.text(4.6, 1.5, "Phenylamine\nC6H5NH2", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#2e7d32',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=0.8))

    # Two branches from phenylamine
    ax.annotate('CH3COCl\n(Room temp)', xy=(5.8, 2.1), xytext=(5.1, 1.8),
                arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
                ha='center', va='bottom', fontsize=5.8, color='#a81717')
    ax.text(5.8, 2.1, "N-phenylethanamide\n(Acetanilide)", ha='left', va='center', fontsize=6.6, fontweight='bold', color='#a81717',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fce4ec', edgecolor='#a81717', lw=0.8))

    ax.annotate('HNO2 / HCl\n(< 10 deg C)', xy=(5.8, 0.9), xytext=(5.1, 1.2),
                arrowprops=dict(arrowstyle='->', color='#e65100', lw=1.2),
                ha='center', va='top', fontsize=5.8, color='#e65100')
    ax.text(5.8, 0.9, "Benzenediazonium ion\n[C6H5N2]+ (Azo precursor)", ha='left', va='center', fontsize=6.6, fontweight='bold', color='#e65100',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fff3e0', edgecolor='#e65100', lw=0.8))

    ax.set_xlim(0.2, 7.5)
    ax.set_ylim(0.2, 2.6)
    ax.axis('off')
    ax.set_title(r'Synthetic Pathway: Multi-Step Synthesis of Aromatic Derivatives from Benzene', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t36_multistep_synthesis_flowchart.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# =============================================================================
# Topic 37 Figures (Analytical Techniques)
# =============================================================================
def create_topic37_figures():
    # 1. TLC Plate
    fig, ax = plt.subplots(figsize=(5.5, 3.2), dpi=220)
    # Draw TLC plate outline
    ax.plot([1, 1, 4, 4, 1], [0.5, 5.0, 5.0, 0.5, 0.5], color='#0b1b36', lw=1.5)
    # Solvent front line
    ax.plot([1, 4], [4.5, 4.5], '--', color='#1565c0', lw=1.2)
    ax.text(4.1, 4.5, 'Solvent front\n(distance b = 4.0 cm)', va='center', fontsize=6.8, color='#1565c0', fontweight='bold')
    # Baseline line
    ax.plot([1, 4], [1.0, 1.0], ':', color='#555555', lw=1.2)
    ax.text(4.1, 1.0, 'Baseline (origin)', va='center', fontsize=6.8, color='#555555', fontweight='bold')

    # Spot A
    ax.plot(2.0, 2.6, 'o', color='#c2185b', markersize=9)
    ax.text(2.0, 2.6, 'Spot X', ha='center', va='center', fontsize=6.0, color='white', fontweight='bold')
    ax.annotate('', xy=(1.5, 2.6), xytext=(1.5, 1.0), arrowprops=dict(arrowstyle='<->', color='#c2185b', lw=1.0))
    ax.text(1.4, 1.8, 'a = 1.6 cm\nRf = 0.40', ha='right', va='center', fontsize=6.5, color='#c2185b', fontweight='bold')

    # Spot B
    ax.plot(3.0, 3.8, 'o', color='#2e7d32', markersize=9)
    ax.text(3.0, 3.8, 'Spot Y', ha='center', va='center', fontsize=6.0, color='white', fontweight='bold')
    ax.annotate('', xy=(3.5, 3.8), xytext=(3.5, 1.0), arrowprops=dict(arrowstyle='<->', color='#2e7d32', lw=1.0))
    ax.text(3.6, 2.4, 'c = 2.8 cm\nRf = 0.70', ha='left', va='center', fontsize=6.5, color='#2e7d32', fontweight='bold')

    ax.text(2.5, 0.2, r'$R_\mathrm{f} = \frac{\text{distance moved by compound}}{\text{distance moved by solvent front}}$',
            ha='center', fontsize=7.2, fontweight='bold', color='#0b1b36')

    ax.set_xlim(0.2, 5.8)
    ax.set_ylim(0.0, 5.4)
    ax.axis('off')
    ax.set_title(r'Thin-Layer Chromatography (TLC) Plate with $R_\mathrm{f}$ Measurements', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t37_tlc_chromatogram.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 2. GLC Chromatogram
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)
    t = np.linspace(0, 12, 1000)
    peak1 = 4.0 * np.exp(-0.5 * ((t - 3.2)/0.25)**2)
    peak2 = 8.5 * np.exp(-0.5 * ((t - 6.5)/0.35)**2)
    peak3 = 2.2 * np.exp(-0.5 * ((t - 9.8)/0.40)**2)
    baseline = 0.2 + 0.05 * np.sin(t)
    signal = peak1 + peak2 + peak3 + baseline

    ax.plot(t, signal, color='#0b1b36', lw=1.2)
    ax.fill_between(t, baseline, peak1 + baseline, color='#1565c0', alpha=0.3)
    ax.fill_between(t, baseline, peak2 + baseline, color='#c2185b', alpha=0.3)
    ax.fill_between(t, baseline, peak3 + baseline, color='#2e7d32', alpha=0.3)

    ax.text(3.2, 4.4, 'Component A\nt_R = 3.2 min\nArea = 25%', ha='center', fontsize=6.8, color='#1565c0', fontweight='bold')
    ax.text(6.5, 9.0, 'Component B\nt_R = 6.5 min\nArea = 60%', ha='center', fontsize=6.8, color='#c2185b', fontweight='bold')
    ax.text(9.8, 2.8, 'Component C\nt_R = 9.8 min\nArea = 15%', ha='center', fontsize=6.8, color='#2e7d32', fontweight='bold')

    ax.set_xlabel('Retention Time / minutes', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_ylabel('Detector Response / mV', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Gas-Liquid Chromatogram (GLC) Trace with Retention Times and Peak Areas', fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10.5)
    ax.grid(True, linestyle=':', alpha=0.4)

    out_file = os.path.join(fig_dir, "a2_t37_glc_chromatogram.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

    # 3. 1H NMR Splitting Spectrum Schematic
    fig, ax = plt.subplots(figsize=(6.2, 2.8), dpi=220)
    # Ethyl ethanoate NMR: CH3COOCH2CH3
    # delta 1.25: triplet (3H, -CH2CH3)
    # delta 2.05: singlet (3H, CH3COO-)
    # delta 4.12: quartet (2H, -COOCH2CH3)
    # delta 0.00: TMS singlet (0H, reference)

    ppm = np.linspace(-0.5, 5.5, 1200)
    # TMS at 0.0
    tms = 2.0 * np.exp(-0.5 * ((ppm - 0.0)/0.02)**2)
    # Singlet at 2.05
    singlet = 5.0 * np.exp(-0.5 * ((ppm - 2.05)/0.02)**2)
    # Triplet at 1.25 (1:2:1)
    trip = 2.5 * np.exp(-0.5 * ((ppm - 1.22)/0.015)**2) + 5.0 * np.exp(-0.5 * ((ppm - 1.25)/0.015)**2) + 2.5 * np.exp(-0.5 * ((ppm - 1.28)/0.015)**2)
    # Quartet at 4.12 (1:3:3:1)
    q_spacing = 0.025
    quart = (1.5 * np.exp(-0.5 * ((ppm - (4.12 - 1.5*q_spacing))/0.012)**2) +
             4.5 * np.exp(-0.5 * ((ppm - (4.12 - 0.5*q_spacing))/0.012)**2) +
             4.5 * np.exp(-0.5 * ((ppm - (4.12 + 0.5*q_spacing))/0.012)**2) +
             1.5 * np.exp(-0.5 * ((ppm - (4.12 + 1.5*q_spacing))/0.012)**2))

    y = tms + singlet + trip + quart

    ax.plot(ppm, y, color='#0b1b36', lw=1.1)
    ax.invert_xaxis()

    ax.text(0.0, 2.3, 'TMS\n0.00 ppm\n(standard)', ha='center', fontsize=6.2, color='#777777')
    ax.text(1.25, 5.5, 'Triplet (1:2:1)\ndelta = 1.25 ppm\n3H (-CH3 adjacent to -CH2-)', ha='center', fontsize=6.5, color='#1565c0', fontweight='bold')
    ax.text(2.05, 5.5, 'Singlet\ndelta = 2.05 ppm\n3H (CH3-C=O)', ha='center', fontsize=6.5, color='#c2185b', fontweight='bold')
    ax.text(4.12, 5.0, 'Quartet (1:3:3:1)\ndelta = 4.12 ppm\n2H (-O-CH2- adjacent to -CH3)', ha='center', fontsize=6.5, color='#2e7d32', fontweight='bold')

    ax.set_xlabel(r'Chemical Shift, $\delta$ / ppm', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_ylabel('Signal Intensity (arbitrary)', fontsize=7.8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'High-Resolution $^1\mathrm{H}\ \mathrm{NMR}$ Spectrum of Ethyl Ethanoate ($\mathrm{CH_3COOCH_2CH_3}$)', fontsize=8.5, fontweight='bold', color='#0b1b36')
    ax.set_xlim(5.0, -0.5)
    ax.set_ylim(0, 6.8)
    ax.grid(True, linestyle=':', alpha=0.3)

    out_file = os.path.join(fig_dir, "a2_t37_nmr_splitting_spectrum.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_topic33_figures()
    create_topic34_figures()
    create_topic35_figures()
    create_topic36_figures()
    create_topic37_figures()
    print("All Figures for Topics 33 through 37 generated successfully!")
