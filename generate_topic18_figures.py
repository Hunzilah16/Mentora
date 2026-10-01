"""
Generate high-DPI figures for Topic 18: Carboxylic Acids and Derivatives.
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

def make_dimer_and_resonance():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Carboxylic Acid Hydrogen-Bonded Dimer & Carboxylate Resonance",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Hydrogen-bonded Dimer (8-membered ring)
    ax.add_patch(plt.Rectangle((0.04, 0.12), 0.44, 0.78, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.04, 0.82), 0.44, 0.08, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.26, 0.86, "Planar Hydrogen-Bonded Dimer", ha='center', va='center',
            fontsize=8.2, fontweight='bold', color='white')
    
    dimer_text = (
        "In pure liquid and non-polar solvents (e.g. benzene),\n"
        "carboxylic acids pair into stable cyclic dimers:\n\n"
        "           $O \\cdot\\cdot\\cdot\\cdot\\cdot\\cdot\\cdot\\cdot H - O$\n"
        "         //                     \\\\\n"
        "    $R - C                       C - R$\n"
        "         \\\\                     //\n"
        "           $O - H \\cdot\\cdot\\cdot\\cdot\\cdot\\cdot\\cdot\\cdot O$\n\n"
        "• Forms an 8-membered cyclic ring\n"
        "• Contains TWO strong intermolecular H-bonds\n"
        "• Explains exceptionally high b.p. & apparent\n"
        "  doubling of Mr in non-polar cryoscopic solvents"
    )
    ax.text(0.06, 0.46, dimer_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Right: Resonance Delocalisation in Carboxylate Anion
    ax.add_patch(plt.Rectangle((0.52, 0.12), 0.44, 0.78, facecolor='#fffbeb', edgecolor='#f59e0b', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.82), 0.44, 0.08, facecolor='#f59e0b', edgecolor='#f59e0b'))
    ax.text(0.74, 0.86, "Resonance in Carboxylate Anion ($RCOO^-$)", ha='center', va='center',
            fontsize=8.2, fontweight='bold', color='#78350f')
    
    res_text = (
        "Acidity Origin: Deprotonation yields $RCOO^-$:\n"
        "  $R-COOH + H_2O \\rightleftharpoons R-COO^- + H_3O^+$\n\n"
        "Resonance Forms:\n"
        "      $O^-                  O$\n"
        "      /                     / \n"
        "  $R - C  \\longleftrightarrow  R - C$\n"
        "      \\\\                    \\\\-\n"
        "      $O                    O^-$\n\n"
        "Delocalised Hybrid:\n"
        "• Negative charge is dispersed equally over both\n"
        "  electronegative oxygen atoms (bond order 1.5)\n"
        "• Both C-O bond lengths are identical (0.127 nm)\n"
        "• Stablised anion explains why carboxylic acids\n"
        "  are far more acidic than alcohols"
    )
    ax.text(0.54, 0.46, res_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carboxylic_dimer_and_resonance.png")
    plt.close()
    print("Generated figures/carboxylic_dimer_and_resonance.png")

def make_substituent_acidity():
    fig, ax = plt.subplots(figsize=(7.8, 4.2), dpi=300)
    
    acids = ['Ethanoic\n$CH_3COOH$', 'Chloroethanoic\n$CH_2ClCOOH$', 'Dichloroethanoic\n$CHCl_2COOH$', 'Trichloroethanoic\n$CCl_3COOH$']
    pKa_values = [4.76, 2.86, 1.29, 0.65]
    colors = ['#0284c7', '#2563eb', '#7c3aed', '#dc2626']
    
    bars = ax.bar(acids, pKa_values, color=colors, width=0.55, edgecolor='#0b1b36', lw=1.2, zorder=3)
    ax.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
    
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.12, f'$pK_a$ = {h:.2f}',
                ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0b1b36')
        
    ax.set_ylabel(r"Acid Dissociation Constant ($pK_a$)", fontsize=9, fontweight='bold', color='#0b1b36')
    ax.set_title("Effect of Chlorine Substituents on Carboxylic Acid Strength (-I Inductive Effect)",
                 fontsize=10.5, fontweight='bold', color='#0b1b36', pad=12)
    ax.set_ylim(0, 5.8)
    
    # Explanatory annotation box
    expl_text = (
        "Trend: Acidity increases dramatically as chlorine atoms are added (lower $pK_a$ = stronger acid).\n"
        "Rationale: Strongly electronegative Cl atoms exert an electron-withdrawing negative inductive (-I) effect.\n"
        "This weakens the O-H bond and delocalises/disperses the negative charge over the carboxylate ion, stabilising it."
    )
    ax.text(0.5, 0.68, expl_text, transform=ax.transAxes, ha='center', va='center',
            fontsize=7.2, color='#1e293b', linespacing=1.25,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    plt.tight_layout()
    plt.savefig("figures/carboxylic_substituent_acidity.png")
    plt.close()
    print("Generated figures/carboxylic_substituent_acidity.png")

def make_reactions_map():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Comprehensive Reaction Pathways of Carboxylic Acids ($R-COOH$)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Central Box: R-COOH
    ax.add_patch(plt.Rectangle((0.36, 0.40), 0.28, 0.22, facecolor='#fef08a', edgecolor='#ca8a04', lw=2))
    ax.text(0.50, 0.51, "Carboxylic Acid\n$R-COOH$", ha='center', va='center',
            fontsize=10, fontweight='bold', color='#854d0e')
    
    # 5 Reaction Cards around central box
    rxns = [
        ("Reactive Metals ($Mg/Na$)", 0.18, 0.72, "#dc2626",
         "$2RCOOH + Mg \\rightarrow (RCOO)_2Mg + H_2$\nEffervescence; squeaky pop with flame"),
        ("Carbonates ($Na_2CO_3/NaHCO_3$)", 0.82, 0.72, "#0284c7",
         "$2RCOOH + Na_2CO_3 \\rightarrow 2RCOONa + H_2O + CO_2$\nEffervescence; gas turns limewater milky"),
        ("Reduction with $LiAlH_4$", 0.16, 0.18, "#16a34a",
         "$RCOOH + 4[H] \\rightarrow RCH_2OH + H_2O$\nIn dry ether $\\rightarrow$ Primary alcohol ($NaBH_4$ fails)"),
        ("Acyl Chlorides ($PCl_5 / SOCl_2$)", 0.50, 0.10, "#7c3aed",
         "$RCOOH + PCl_5 \\rightarrow RCOCl + POCl_3 + HCl(g)$\nMisty steamy fumes; test for -OH group"),
        ("Esterification ($R'OH / H^+$)", 0.84, 0.18, "#d97706",
         "$RCOOH + R'OH \\rightleftharpoons RCOOR' + H_2O$\nHeated under reflux with conc. $H_2SO_4$; fruity smell")
    ]
    
    for title, cx, cy, col, text in rxns:
        w = 0.30
        h = 0.24
        x0 = cx - w/2
        y0 = cy - h/2
        ax.add_patch(plt.Rectangle((x0, y0), w, h, facecolor='#f8fafc', edgecolor=col, lw=1.4))
        ax.add_patch(plt.Rectangle((x0, y0 + h - 0.05), w, 0.05, facecolor=col, edgecolor=col))
        ax.text(cx, y0 + h - 0.025, title, ha='center', va='center', fontsize=7.2, fontweight='bold', color='white')
        ax.text(cx, y0 + 0.08, text, ha='center', va='center', fontsize=6.2, color='#1e293b', linespacing=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carboxylic_chemical_reactions_map.png")
    plt.close()
    print("Generated figures/carboxylic_chemical_reactions_map.png")

def make_ester_hydrolysis():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Comparison: Acid vs Alkaline Hydrolysis (Saponification) of Esters",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Acid Hydrolysis
    ax.add_patch(plt.Rectangle((0.05, 0.16), 0.43, 0.70, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.05, 0.77), 0.43, 0.09, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.265, 0.815, "Acid Hydrolysis (Reversible Equilibrium)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    acid_text = (
        "Reaction:\n"
        "  $RCOOR' + H_2O \\rightleftharpoons RCOOH + R'OH$\n\n"
        "Reagents & Conditions:\n"
        "• Dilute strong acid (e.g. dilute $HCl$ or $H_2SO_4$)\n"
        "• Heat under reflux\n\n"
        "Characteristics:\n"
        "• Dynamic reversible equilibrium\n"
        "• Does NOT go to completion\n"
        "• Moderate yield; requires large excess of water\n"
        "  to drive equilibrium position to the right"
    )
    ax.text(0.07, 0.46, acid_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    # Right: Alkaline Hydrolysis (Saponification)
    ax.add_patch(plt.Rectangle((0.52, 0.16), 0.43, 0.70, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.77), 0.43, 0.09, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.735, 0.815, "Alkaline Hydrolysis (Irreversible Completion)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    alk_text = (
        "Reaction:\n"
        "  $RCOOR' + OH^- \\rightarrow RCOO^- + R'OH$\n\n"
        "Reagents & Conditions:\n"
        "• Aqueous sodium hydroxide ($NaOH(aq)$)\n"
        "• Heat under reflux\n\n"
        "Characteristics:\n"
        "• Goes to 100% completion (irreversible)\n"
        "• Acid is immediately converted to carboxylate salt\n"
        "• Carboxylate anion ($RCOO^-$) repels nucleophiles\n"
        "• Acid regenerated by adding dilute mineral acid:\n"
        "  $RCOO^- + H^+ \\rightarrow RCOOH$"
    )
    ax.text(0.54, 0.46, alk_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    ax.text(0.5, 0.05, "Alkaline hydrolysis of fats (triglycerides) is used industrially to manufacture soap and glycerol.",
            ha='center', va='bottom', fontsize=7.8, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/ester_hydrolysis_acid_vs_alkaline.png")
    plt.close()
    print("Generated figures/ester_hydrolysis_acid_vs_alkaline.png")

if __name__ == "__main__":
    make_dimer_and_resonance()
    make_substituent_acidity()
    make_reactions_map()
    make_ester_hydrolysis()
