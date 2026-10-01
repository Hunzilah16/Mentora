"""
Generate high-DPI figures for Topic 19: Nitrogen Compounds (Amines and Nitriles).
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

def make_basicity_comparison():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Relative Basicity of Nitrogen Compounds: Lone Pair Availability",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 3 Cards: Ethylamine, Ammonia, Phenylamine
    bases = [
        ("Ethylamine\n$CH_3CH_2NH_2$", 0.18, "#16a34a",
         "• Strongest Base ($pK_b \\approx 3.3$)\n\n"
         "• Structure: Ethyl group attached\n"
         "  to $-NH_2$\n\n"
         "• Inductive Effect (+I):\n"
         "  The electron-releasing ethyl\n"
         "  group pushes electron density\n"
         "  onto the nitrogen atom\n\n"
         "• Result:\n"
         "  Nitrogen lone pair is more\n"
         "  readily donated to a proton ($H^+$)"),
        ("Ammonia\n$NH_3$", 0.50, "#0284c7",
         "• Intermediate Base ($pK_b \\approx 4.75$)\n\n"
         "• Structure: Three hydrogen atoms\n"
         "  bonded to nitrogen\n\n"
         "• Reference Standard:\n"
         "  No alkyl groups to release\n"
         "  electrons; no aromatic ring to\n"
         "  delocalise the lone pair\n\n"
         "• Result:\n"
         "  Intermediate electron density\n"
         "  on the nitrogen lone pair"),
        ("Phenylamine\n$C_6H_5NH_2$", 0.82, "#dc2626",
         "• Weakest Base ($pK_b \\approx 9.4$)\n\n"
         "• Structure: Benzene ring attached\n"
         "  to $-NH_2$\n\n"
         "• $\\pi$-Delocalisation:\n"
         "  The nitrogen lone pair overlaps\n"
         "  with the delocalised $\\pi$ cloud\n"
         "  of the benzene ring\n\n"
         "• Result:\n"
         "  Lone pair is significantly less\n"
         "  available to accept a proton ($H^+$)")
    ]
    
    for title, cx, col, text in bases:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.12), w, 0.78, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.78), w, 0.12, facecolor=col, edgecolor=col))
        ax.text(cx, 0.84, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.44, text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.25)
        
    ax.text(0.5, 0.04, "Overall Basicity Order: Ethylamine (primary aliphatic) > Ammonia > Phenylamine (aromatic)",
            ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/amines_basicity_comparison.png")
    plt.close()
    print("Generated figures/amines_basicity_comparison.png")

def make_synthesis_pathways():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Comparative Synthetic Routes to Primary Aliphatic Amines",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Route 1 (Top Box)
    ax.add_patch(plt.Rectangle((0.05, 0.52), 0.90, 0.36, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.5))
    ax.add_patch(plt.Rectangle((0.05, 0.81), 0.90, 0.07, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.50, 0.845, "Route 1: Halogenoalkane + Excess Ammonia (Nucleophilic Substitution)",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color='white')
    
    r1_text = (
        "• Reagents: Halogenoalkane + EXCESS concentrated ethanolic $NH_3$, heated under pressure in a sealed tube\n"
        "• Equation: $CH_3CH_2Br + 2NH_3 \\rightarrow CH_3CH_2NH_2 + NH_4Br$\n"
        "• Critical Feature: Excess ammonia is required to suppress consecutive nucleophilic substitutions\n"
        "  (otherwise $2^\\circ, 3^\\circ$ amines and quaternary ammonium salts $(R_4N^+X^-)$ contaminate the product)"
    )
    ax.text(0.07, 0.66, r1_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    # Route 2 (Bottom Box)
    ax.add_patch(plt.Rectangle((0.05, 0.08), 0.90, 0.38, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.5))
    ax.add_patch(plt.Rectangle((0.05, 0.39), 0.90, 0.07, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.50, 0.425, "Route 2: Two-Step Nitrile Pathway (+1 Carbon Atom Chain Extension)",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color='white')
    
    r2_text = (
        "• Step 1 (Chain Extension): $CH_3Br + KCN \\rightarrow CH_3CN + KBr$  (reflux in aqueous ethanol)\n"
        "• Step 2 (Reduction): $CH_3CN + 4[H] \\rightarrow CH_3CH_2NH_2$  ($LiAlH_4$ in dry ether OR $H_2 / Ni$ catalyst)\n"
        "• Major Advantage: Produces SOLELY the primary amine with NO contaminating secondary or tertiary amines;\n"
        "  adds exactly one additional carbon atom to the starting alkyl chain."
    )
    ax.text(0.07, 0.23, r2_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/amines_synthesis_pathways.png")
    plt.close()
    print("Generated figures/amines_synthesis_pathways.png")

def make_nitriles_reactions():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Chemical Reactions and Transformations of Nitriles ($R-C\\equiv N$)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Central Box: R-CN
    ax.add_patch(plt.Rectangle((0.36, 0.40), 0.28, 0.22, facecolor='#fef08a', edgecolor='#ca8a04', lw=2))
    ax.text(0.50, 0.51, "Nitrile\n$R - C\\equiv N$", ha='center', va='center',
            fontsize=10.5, fontweight='bold', color='#854d0e')
    
    # Left Card: Acid Hydrolysis
    ax.add_patch(plt.Rectangle((0.04, 0.18), 0.28, 0.66, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.5))
    ax.add_patch(plt.Rectangle((0.04, 0.74), 0.28, 0.10, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.18, 0.79, "Acid Hydrolysis", ha='center', va='center', fontsize=8.0, fontweight='bold', color='white')
    ah_text = (
        "Reagents:\n"
        "• Dilute $HCl(aq)$ or\n"
        "  dilute $H_2SO_4(aq)$\n"
        "• Heat under reflux\n\n"
        "Equation:\n"
        "$RCN + 2H_2O + H^+ \\rightarrow$\n"
        "  $RCOOH + NH_4^+$\n\n"
        "Product:\n"
        "• Carboxylic acid +\n"
        "  ammonium salt"
    )
    ax.text(0.06, 0.45, ah_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Right Card: Alkaline Hydrolysis
    ax.add_patch(plt.Rectangle((0.68, 0.18), 0.28, 0.66, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.5))
    ax.add_patch(plt.Rectangle((0.68, 0.74), 0.28, 0.10, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.82, 0.79, "Alkaline Hydrolysis", ha='center', va='center', fontsize=8.0, fontweight='bold', color='white')
    bh_text = (
        "Reagents:\n"
        "• Aqueous $NaOH(aq)$\n"
        "• Heat under reflux\n\n"
        "Equation:\n"
        "$RCN + H_2O + OH^- \\rightarrow$\n"
        "  $RCOO^- + NH_3(g)$\n\n"
        "Observation & Acidify:\n"
        "• $NH_3$ turns litmus blue\n"
        "• Add dilute $HCl$ to\n"
        "  liberate $RCOOH$"
    )
    ax.text(0.70, 0.45, bh_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Bottom Note Box: Reduction
    ax.add_patch(plt.Rectangle((0.32, 0.08), 0.36, 0.24, facecolor='#f8fafc', edgecolor='#7c3aed', lw=1.4))
    ax.text(0.50, 0.25, "Reduction to Primary Amine", ha='center', va='center',
            fontsize=7.8, fontweight='bold', color='#6d28d9')
    red_text = "$R-CN + 4[H] \\rightarrow R-CH_2NH_2$\n• $LiAlH_4$ in dry ether OR $H_2/Ni$"
    ax.text(0.50, 0.14, red_text, ha='center', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/nitriles_synthetic_reactions.png")
    plt.close()
    print("Generated figures/nitriles_synthetic_reactions.png")

def make_amines_acylation():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Key Reactions of Primary Amines: Salt Formation, Acylation & Complexation",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    rxns = [
        ("Salt Formation with Acids", 0.18, "#0284c7",
         "Reaction with mineral acids:\n"
         "  $RNH_2 + HCl \\rightarrow RNH_3^+Cl^-$\n\n"
         "• Reversible reaction\n"
         "• Forms crystalline ionic salt\n"
         "• Water-soluble ammonium salt\n"
         "• Adding $NaOH$ liberates free amine:\n"
         "  $RNH_3^+ + OH^- \\rightarrow RNH_2 + H_2O$"),
        ("Acylation with Acyl Chlorides", 0.50, "#dc2626",
         "Reaction with $R'COCl$:\n"
         "  $R'COCl + RNH_2 \\rightarrow R'CONHR + HCl$\n\n"
         "• Produces secondary substituted amide\n"
         "• Forms peptide / amide link ($-CONH-$)\n"
         "• Vigorous reaction at room temperature\n"
         "• Second equivalent of amine reacts with $HCl$\n"
         "  to form $RNH_3^+Cl^-$ salt"),
        ("Copper(II) Complexation", 0.82, "#2563eb",
         "With aqueous copper(II) sulfate:\n\n"
         "• Dropwise amine:\n"
         "  Pale blue precipitate of $Cu(OH)_2$\n"
         "  (amine acts as Bronsted base)\n\n"
         "• Excess amine:\n"
         "  Precipitate dissolves forming\n"
         "  deep royal-blue solution of complex:\n"
         "  $[Cu(RNH_2)_4(H_2O)_2]^{2+}$")
    ]
    
    for title, cx, col, text in rxns:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.08), w, 0.80, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.76), w, 0.12, facecolor=col, edgecolor=col))
        ax.text(cx, 0.82, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.42, text, ha='left', va='center', fontsize=6.6, color='#1e293b', linespacing=1.22)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/amines_acylation_and_salts.png")
    plt.close()
    print("Generated figures/amines_acylation_and_salts.png")

if __name__ == "__main__":
    make_basicity_comparison()
    make_synthesis_pathways()
    make_nitriles_reactions()
    make_amines_acylation()
