"""
Generate high-DPI figures for Topic 21: Organic Synthesis.
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

def make_master_fgi_roadmap():
    fig, ax = plt.subplots(figsize=(8.2, 4.6), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Comprehensive AS Organic Functional Group Interconversion (FGI) Roadmap",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 6 Key Functional Group Boxes in a ring/network layout
    boxes = [
        ("Alkane", 0.14, 0.75, "#64748b"),
        ("Halogenoalkane", 0.40, 0.75, "#0284c7"),
        ("Alkene", 0.14, 0.35, "#16a34a"),
        ("Alcohol", 0.40, 0.35, "#d97706"),
        ("Carbonyl (Ald/Ket)", 0.68, 0.35, "#7c3aed"),
        ("Carboxylic Acid", 0.90, 0.35, "#dc2626"),
        ("Nitrile (+1 C)", 0.68, 0.75, "#ca8a04"),
        ("Primary Amine", 0.90, 0.75, "#059669")
    ]
    
    for title, cx, cy, col in boxes:
        w, h = 0.19, 0.12
        ax.add_patch(plt.Rectangle((cx - w/2, cy - h/2), w, h, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.text(cx, cy, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color=col)
        
    # Key transformation notes below
    ax.add_patch(plt.Rectangle((0.04, 0.05), 0.92, 0.22, facecolor='#fffbeb', edgecolor='#f59e0b', lw=1.4))
    ax.text(0.50, 0.22, "Key Reagents & Conditions Summary", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='#b45309')
    notes = (
        "• Alkane -> Halogenoalkane: $Br_2$ / $Cl_2$, UV light (Free-radical substitution)\n"
        "• Halogenoalkane -> Alcohol: $NaOH(aq)$, heat under reflux (Nucleophilic substitution, $S_N1$ or $S_N2$)\n"
        "• Alcohol -> Alkene: Hot conc. $H_2SO_4$ (170 °C) or $Al_2O_3$ (300 °C) (Elimination / Dehydration)\n"
        "• Alkene -> Alcohol: Steam + conc. $H_3PO_4$ (300 °C, 60 atm) (Electrophilic addition)\n"
        "• 1° Alcohol -> Aldehyde -> Acid: $K_2Cr_2O_7 / H^+$, distil (aldehyde) or reflux (acid); 2° Alcohol -> Ketone (reflux)\n"
        "• Carbonyl -> Alcohol: $NaBH_4$ in aqueous ethanol (Reduction via hydride $:H^-$)"
    )
    ax.text(0.06, 0.12, notes, ha='left', va='center', fontsize=6.2, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/synthesis_master_fgi_roadmap.png")
    plt.close()
    print("Generated figures/synthesis_master_fgi_roadmap.png")

def make_chain_modification():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Techniques for Modifying Carbon Chain Length in Organic Synthesis",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Chain Lengthening (+1 C)
    ax.add_patch(plt.Rectangle((0.05, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.6))
    ax.add_patch(plt.Rectangle((0.05, 0.78), 0.43, 0.08, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.265, 0.82, "Chain Lengthening (+1 C Extension)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    len_text = (
        "Method A: Halogenoalkane + Cyanide Ion\n"
        "  $R-Br + KCN \\rightarrow R-CN + KBr$\n"
        "  (Reagents: Ethanolic $KCN$, heat under reflux)\n\n"
        "Method B: Carbonyl + Hydrogen Cyanide\n"
        "  $R-CHO + HCN \\rightarrow R-CH(OH)-CN$\n"
        "  (Reagents: $HCN / NaCN$, room temp, pH ~ 8)\n\n"
        "Subsequent Transformations:\n"
        "• Hydrolysis (reflux dil. $HCl$): $\\rightarrow R-COOH$\n"
        "• Reduction ($LiAlH_4$ in ether): $\\rightarrow R-CH_2NH_2$"
    )
    ax.text(0.07, 0.46, len_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Right: Chain Shortening (-1 C)
    ax.add_patch(plt.Rectangle((0.52, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#dc2626', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.78), 0.43, 0.08, facecolor='#dc2626', edgecolor='#dc2626'))
    ax.text(0.735, 0.82, "Chain Shortening (-1 C Cleavage)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    short_text = (
        "Tri-iodomethane (Iodoform) Reaction:\n"
        "  $R-CO-CH_3 + 3I_2 + 4NaOH \\rightarrow$\n"
        "    $R-COONa + CHI_3(s) + 3NaI + 3H_2O$\n\n"
        "Mechanism of Cleavage:\n"
        "• Tri-iodination forms $R-CO-CI_3$\n"
        "• Nucleophilic attack of $OH^-$ cleaves the\n"
        "  $C-C$ bond, expelling $:CI_3^-$\n"
        "• Acidification with dilute $HCl$ liberates\n"
        "  $R-COOH$ (one fewer carbon atom than $RCOCH_3$)"
    )
    ax.text(0.54, 0.46, short_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/synthesis_carbon_chain_modification.png")
    plt.close()
    print("Generated figures/synthesis_carbon_chain_modification.png")

def make_retrosynthesis():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Retrosynthetic Analysis: Working Backwards from Target Molecule",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 3 Sequential Steps
    steps = [
        ("Target Molecule", 0.18, "#7c3aed",
         "Example Target:\n"
         "Ethyl propanoate\n"
         "($CH_3CH_2COOCH_2CH_3$)\n\n"
         "Disconnection:\n"
         "Cleave ester bond\n"
         "$\\Longrightarrow$ Acid + Alcohol:\n"
         "• Propanoic acid\n"
         "• Ethanol"),
        ("Precursor Precursors", 0.50, "#0284c7",
         "Retrosynthetic Step 2:\n\n"
         "• Propanoic acid $\\Longleftarrow$\n"
         "  Propanenitrile or\n"
         "  Propan-1-ol\n\n"
         "• Propanenitrile $\\Longleftarrow$\n"
         "  Bromoethane ($+1$ C)\n\n"
         "• Ethanol $\\Longleftarrow$\n"
         "  Bromoethane ($S_N2$)"),
        ("Forward Synthetic Plan", 0.82, "#16a34a",
         "Forward Route:\n"
         "From Bromoethane ($C_2H_5Br$):\n\n"
         "1. $C_2H_5Br + KCN \\rightarrow$\n"
         "   $C_2H_5CN$ (reflux eth)\n"
         "2. $C_2H_5CN + H_2O/H^+ \\rightarrow$\n"
         "   $C_2H_5COOH$ (reflux)\n"
         "3. $C_2H_5Br + NaOH(aq) \\rightarrow$\n"
         "   $C_2H_5OH$\n"
         "4. Esterify with conc. $H_2SO_4$")
    ]
    
    for title, cx, col, text in steps:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.08), w, 0.78, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.76), w, 0.10, facecolor=col, edgecolor=col))
        ax.text(cx, 0.81, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.42, text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/synthesis_retrosynthetic_disconnection.png")
    plt.close()
    print("Generated figures/synthesis_retrosynthetic_disconnection.png")

def make_green_chemistry():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Green Chemistry Metrics: Percentage Yield vs Percentage Atom Economy",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Percentage Yield
    ax.add_patch(plt.Rectangle((0.05, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.05, 0.78), 0.43, 0.08, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.265, 0.82, "Percentage Yield (%)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    yield_text = (
        "Formula:\n"
        "  $\\mathrm{\\%\\ Yield} = \\frac{\\mathrm{Actual\\ Mass\\ Obtained}}{\\mathrm{Theoretical\\ Maximum\\ Mass}} \\times 100\\%$\n\n"
        "Practical Significance:\n"
        "• Measures laboratory/industrial efficiency\n"
        "• Quantifies material lost through:\n"
        "  - Incomplete reaction (dynamic equilibrium)\n"
        "  - Competing side reactions\n"
        "  - Physical losses during purification\n"
        "    (separation funnels, recrystallisation, distillation)"
    )
    ax.text(0.07, 0.46, yield_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Right: Atom Economy
    ax.add_patch(plt.Rectangle((0.52, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.78), 0.43, 0.08, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.735, 0.82, "Percentage Atom Economy (%)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    ae_text = (
        "Formula:\n"
        "  $\\mathrm{\\%\\ Atom\\ Economy} = \\frac{M_r\\ \\mathrm{of\\ Desired\\ Product}}{\\sum M_r\\ \\mathrm{of\\ All\\ Reactants}} \\times 100\\%$\n\n"
        "Green Chemistry Significance:\n"
        "• Measures theoretical efficiency of the reaction pathway\n"
        "• Addition polymerisation & additions = 100% atom economy\n"
        "• Substitutions & eliminations produce by-product waste\n"
        "• Maximising atom economy minimizes hazardous waste\n"
        "  generation and conserves raw materials"
    )
    ax.text(0.54, 0.46, ae_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/synthesis_green_chemistry_metrics.png")
    plt.close()
    print("Generated figures/synthesis_green_chemistry_metrics.png")

if __name__ == "__main__":
    make_master_fgi_roadmap()
    make_chain_modification()
    make_retrosynthesis()
    make_green_chemistry()
