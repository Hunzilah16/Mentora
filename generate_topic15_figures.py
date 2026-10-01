"""
Generate high-DPI figures for Topic 15: Halogen Compounds (Halogenoalkanes).
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

def make_sn1_vs_sn2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.4), dpi=300)
    for ax in (ax1, ax2):
        ax.axis('off')
        
    # Panel 1: SN2
    ax1.add_patch(plt.Rectangle((0.04, 0.08), 0.92, 0.86, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.8))
    ax1.text(0.5, 0.88, r"$\mathbf{S_N2}$ Mechanism (Bimolecular)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#15803d')
    ax1.text(0.5, 0.80, "Primary (1°) Halogenoalkanes", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#166534')
    sn2_text = (
        "• Single concerted step via a transition state\n\n"
        "  $Nu:^- + CH_3-Br \\rightarrow [Nu\\cdots CH_3 \\cdots Br]^\\ddagger \\rightarrow Nu-CH_3 + :Br^-$\n\n"
        "• Backside attack by nucleophile ($180^\\circ$ to C-Br bond)\n"
        "• Penta-coordinate transition state\n"
        "• Complete stereochemical inversion (Walden inversion)\n"
        "• Rate law: $\\mathrm{Rate} = k[RBr][:Nu^-]$\n"
        "• Favoured by: Little steric hindrance around C"
    )
    ax1.text(0.5, 0.44, sn2_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.35)
    
    # Panel 2: SN1
    ax2.add_patch(plt.Rectangle((0.04, 0.08), 0.92, 0.86, facecolor='#eff6ff', edgecolor='#2563eb', lw=1.8))
    ax2.text(0.5, 0.88, r"$\mathbf{S_N1}$ Mechanism (Unimolecular)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#1d4ed8')
    ax2.text(0.5, 0.80, "Tertiary (3°) Halogenoalkanes", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e40af')
    sn1_text = (
        "• Two-step mechanism via a carbocation intermediate\n\n"
        "  Step 1 (Slow, r.d.s.):\n"
        "  $(CH_3)_3C-Br \\rightarrow (CH_3)_3C^+ + :Br^-$\n\n"
        "  Step 2 (Fast):\n"
        "  $(CH_3)_3C^+ + :Nu^- \\rightarrow (CH_3)_3C-Nu$\n\n"
        "• Planar carbocation intermediate\n"
        "• Attack from either face with equal probability (racemisation)\n"
        "• Rate law: $\\mathrm{Rate} = k[RBr]$\n"
        "• Favoured by: 3 alkyl groups stabilizing $C^+$"
    )
    ax2.text(0.5, 0.44, sn1_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.3)
    
    plt.tight_layout()
    plt.savefig("figures/halogenoalkanes_sn1_vs_sn2_mechanisms.png")
    plt.close()
    print("Generated figures/halogenoalkanes_sn1_vs_sn2_mechanisms.png")

def make_hydrolysis_rates():
    fig, ax1 = plt.subplots(figsize=(7.5, 4.2), dpi=300)
    
    halogens = ['1-chlorobutane', '1-bromobutane', '1-iodobutane']
    # Bond enthalpies in kJ/mol: C-Cl: 340, C-Br: 280, C-I: 240
    bond_enthalpy = [340, 280, 240]
    # Relative rate of hydrolysis (approx relative values: 1, 10, 100)
    rel_rate = [1, 15, 80]
    
    x = np.arange(len(halogens))
    width = 0.35
    
    rects1 = ax1.bar(x - width/2, bond_enthalpy, width, label=r'$C-X$ Bond Enthalpy / $\mathrm{kJ\cdot mol^{-1}}$',
                     color='#0b1b36', edgecolor='#0b1b36', lw=1.2)
    ax1.set_ylabel(r'$C-X$ Bond Enthalpy / $\mathrm{kJ\cdot mol^{-1}}$', color='#0b1b36', fontsize=9.5, fontweight='bold')
    ax1.set_ylim(0, 420)
    ax1.set_xticks(x)
    ax1.set_xticklabels([r'$\mathbf{R-Cl}$' + '\n(White ppt AgCl\nforms slowly)', 
                         r'$\mathbf{R-Br}$' + '\n(Cream ppt AgBr\nforms moderately)', 
                         r'$\mathbf{R-I}$' + '\n(Yellow ppt AgI\nforms rapidly)'], fontsize=9)
    
    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, rel_rate, width, label='Relative Rate of Hydrolysis',
                     color='#a81717', edgecolor='#a81717', lw=1.2)
    ax2.set_ylabel('Relative Rate of Hydrolysis with $AgNO_3(aq)$', color='#a81717', fontsize=9.5, fontweight='bold')
    ax2.set_ylim(0, 100)
    
    # Annotate bond enthalpies
    for r in rects1:
        h = r.get_height()
        ax1.annotate(f'{h}', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0b1b36')
    for r in rects2:
        h = r.get_height()
        ax2.annotate(f'{h}x', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#a81717')
        
    plt.title(r"Rate of Hydrolysis Governed by $C-X$ Bond Enthalpy, NOT Bond Polarity", fontsize=10.5, fontweight='bold', color='#0b1b36', pad=12)
    
    # Note
    ax1.text(0.05, 0.82, "Lower bond enthalpy ($C-I < C-Br < C-Cl$)\n→ Weaker bond breaks more easily\n→ Lower activation energy ($E_a$)\n→ Fastest hydrolysis rate for iodoalkanes",
             transform=ax1.transAxes, fontsize=7.8, verticalalignment='top',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    plt.tight_layout()
    plt.savefig("figures/halogenoalkanes_hydrolysis_rates_agplus.png")
    plt.close()
    print("Generated figures/halogenoalkanes_hydrolysis_rates_agplus.png")

def make_substitution_vs_elimination():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Nucleophilic Substitution vs Elimination of Halogenoalkanes",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Center: Starting Material Box
    ax.add_patch(plt.Rectangle((0.36, 0.42), 0.28, 0.18, facecolor='#0b1b36', edgecolor='#0b1b36', lw=1.5))
    ax.text(0.5, 0.53, "Halogenoalkane\n$CH_3-CH_2-Br$", ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
    ax.text(0.5, 0.45, "(Bromoethane)", ha='center', va='center', fontsize=7.5, color='#93c5fd')
    
    # Left Branch: Substitution
    ax.add_patch(plt.Rectangle((0.04, 0.20), 0.28, 0.60, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.8))
    ax.text(0.18, 0.74, "SUBSTITUTION", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#15803d')
    sub_desc = (
        "Reagent & Conditions:\n"
        "• Aqueous $NaOH$ or $KOH$\n"
        "• Warm under reflux\n"
        "• Solvent: Water ($H_2O$)\n\n"
        "Role of $OH^-$:\n"
        "• Acts as a Nucleophile\n"
        "  (attacks $C^{\\delta+}$ carbon)\n\n"
        "Product:\n"
        "$CH_3CH_2OH$ (Ethanol)"
    )
    ax.text(0.18, 0.44, sub_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right Branch: Elimination
    ax.add_patch(plt.Rectangle((0.68, 0.20), 0.28, 0.60, facecolor='#fef2f2', edgecolor='#dc2626', lw=1.8))
    ax.text(0.82, 0.74, "ELIMINATION", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#991b1b')
    elim_desc = (
        "Reagent & Conditions:\n"
        "• Ethanolic $NaOH$ or $KOH$\n"
        "• Hot under reflux\n"
        "• Solvent: Ethanol ($C_2H_5OH$)\n\n"
        "Role of $OH^-$:\n"
        "• Acts as a Base\n"
        "  (removes $H^+$ from adjacent C)\n\n"
        "Product:\n"
        "$CH_2=CH_2$ (Ethene)"
    )
    ax.text(0.82, 0.44, elim_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Arrows
    ax.annotate("", xy=(0.32, 0.51), xytext=(0.36, 0.51), arrowprops=dict(arrowstyle='<-', lw=2, color='#16a34a'))
    ax.annotate("", xy=(0.68, 0.51), xytext=(0.64, 0.51), arrowprops=dict(arrowstyle='->', lw=2, color='#dc2626'))
    
    ax.text(0.5, 0.06, "Summary: Water favours substitution (forming alcohol); ethanol + high heat favours elimination (forming alkene).",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/halogenoalkanes_substitution_vs_elimination.png")
    plt.close()
    print("Generated figures/halogenoalkanes_substitution_vs_elimination.png")

def make_cfcs_ozone_depletion():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Stratospheric Ozone Depletion by Chlorofluorocarbons (CFCs)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left box: Photolysis of CFCs
    ax.add_patch(plt.Rectangle((0.05, 0.16), 0.42, 0.70, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    ax.text(0.26, 0.80, "Photolysis of CFC in Stratosphere", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0b1b36')
    c_desc = (
        "• CFCs (e.g. $CCl_2F_2$) are chemically unreactive\n"
        "  and diffuse into the stratosphere.\n\n"
        "• High-energy UV radiation ($h\\nu$) cleaves\n"
        "  the weaker $C-Cl$ bond homolytically:\n\n"
        "  $CCl_2F_2 \\rightarrow ^\\bullet CClF_2 + Cl^\\bullet$\n"
        "  ($C-Cl$ breaks: 340 kJ/mol vs $C-F$: 467 kJ/mol)\n\n"
        "• Produces reactive chlorine free radicals ($Cl^\\bullet$)."
    )
    ax.text(0.26, 0.46, c_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right box: Catalytic Cycle
    ax.add_patch(plt.Rectangle((0.53, 0.16), 0.42, 0.70, facecolor='#fff1f2', edgecolor='#e11d48', lw=1.6))
    ax.text(0.74, 0.80, "Catalytic Ozone Destruction Cycle", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#9f1239')
    o_desc = (
        "Step 1: Chlorine radical attacks ozone:\n"
        "  $Cl^\\bullet + O_3 \\rightarrow ClO^\\bullet + O_2$\n\n"
        "Step 2: Regeneration of chlorine radical:\n"
        "  $ClO^\\bullet + O \\rightarrow Cl^\\bullet + O_2$\n\n"
        "Overall Reaction:\n"
        "  $O_3 + O \\rightarrow 2O_2$\n\n"
        "• One $Cl^\\bullet$ radical can destroy thousands\n"
        "  of ozone molecules before terminating.\n"
        "• Replaced by HFCs (contain no $C-Cl$ bonds)."
    )
    ax.text(0.74, 0.46, o_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/halogenoalkanes_cfcs_ozone_depletion.png")
    plt.close()
    print("Generated figures/halogenoalkanes_cfcs_ozone_depletion.png")

if __name__ == "__main__":
    make_sn1_vs_sn2()
    make_hydrolysis_rates()
    make_substitution_vs_elimination()
    make_cfcs_ozone_depletion()
