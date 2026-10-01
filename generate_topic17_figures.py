"""
Generate high-DPI figures for Topic 17: Carbonyl Compounds (Aldehydes and Ketones).
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

def make_nucleophilic_addition():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Mechanism: Nucleophilic Addition of HCN to Carbonyl Compounds",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Step 1 Box
    ax.add_patch(plt.Rectangle((0.04, 0.48), 0.44, 0.42, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.5))
    ax.add_patch(plt.Rectangle((0.04, 0.83), 0.44, 0.07, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.26, 0.865, "Step 1: Nucleophilic Attack (Rate-Determining)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    step1_text = (
        "• Planar carbonyl carbon ($sp^2$ hybridized, 120° angles)\n"
        "• Polar bond: $C^{\\delta+} = O^{\\delta-}$ creates electrophilic center\n"
        "• Cyanide ion ($:C\\equiv N^-$) attacks planar $C^{\\delta+}$:\n\n"
        "         $R_1$\n"
        "           \\   \\delta+\n"
        "    :CN^- + C = O^{\\delta-}  \\rightarrow  [Tetrahedral intermediate]\n"
        "           /\n"
        "         $R_2$\n\n"
        "• Attack is equally likely from top or bottom face\n"
        "  $\\rightarrow$ Leads to a racemic mixture (if $R_1 \\neq R_2$)"
    )
    ax.text(0.06, 0.65, step1_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Step 2 Box
    ax.add_patch(plt.Rectangle((0.52, 0.48), 0.44, 0.42, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.5))
    ax.add_patch(plt.Rectangle((0.52, 0.83), 0.44, 0.07, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.74, 0.865, "Step 2: Protonation & Catalyst Regeneration", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    step2_text = (
        "• The alkoxide intermediate is strongly basic\n"
        "• Oxygen lone pair accepts $H^+$ from $HCN$ or $H_2O$:\n\n"
        "         $R_1$                    $R_1$\n"
        "           |                      |\n"
        "     $NC - C - O^- + H-CN \\rightarrow NC - C - OH + :CN^-$\n"
        "           |                      |\n"
        "         $R_2$                    $R_2$\n\n"
        "• Forms 2-hydroxynitrile (cyanohydrin)\n"
        "• Regenerates $:CN^-$ catalyst (pH ~ 8 is optimal)"
    )
    ax.text(0.54, 0.65, step2_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Bottom Note Box: Synthetic utility of hydroxynitriles
    ax.add_patch(plt.Rectangle((0.04, 0.06), 0.92, 0.36, facecolor='#fffbeb', edgecolor='#f59e0b', lw=1.4))
    ax.text(0.50, 0.38, "Synthetic Versatility of 2-Hydroxynitriles (Carbon Chain Extension by +1 C)",
            ha='center', va='center', fontsize=8.2, fontweight='bold', color='#b45309')
    
    synth_text = (
        "1. Acid Hydrolysis: Reflux with dilute $HCl(aq)$ or $H_2SO_4(aq)$:\n"
        "   $R-CH(OH)-CN + 2H_2O + H^+ \\rightarrow R-CH(OH)-COOH + NH_4^+$  (Produces a 2-hydroxycarboxylic acid)\n\n"
        "2. Reduction: Heat with $LiAlH_4$ in dry ether (or $H_2 / Ni$):\n"
        "   $R-CH(OH)-CN + 4[H] \\rightarrow R-CH(OH)-CH_2NH_2$  (Produces a 2-hydroxyalkylamine)"
    )
    ax.text(0.06, 0.21, synth_text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carbonyl_nucleophilic_addition_mechanism.png")
    plt.close()
    print("Generated figures/carbonyl_nucleophilic_addition_mechanism.png")

def make_diagnostic_tests():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Diagnostic Chemical Tests for Carbonyl Compounds",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 4 Columns of tests
    tests = [
        ("2,4-DNPH\n(Brady's Reagent)", 0.16, "#dc2626",
         "• Tests for: Carbonyl ($C=O$)\n"
         "  in both aldehydes & ketones\n\n"
         "• Reaction: Condensation\n"
         "  (Addition-elimination)\n\n"
         "• Observation:\n"
         "  Bright orange / yellow\n"
         "  crystalline precipitate\n\n"
         "• Value: Filter, purify,\n"
         "  measure m.p. of hydrazone\n"
         "  to identify specific compound"),
        ("Tollens' Reagent\n$[Ag(NH_3)_2]^+$", 0.39, "#2563eb",
         "• Tests for: Aldehydes\n"
         "  (Ketones = negative)\n\n"
         "• Reaction: Mild oxidation\n"
         "  $R-CHO + 2Ag^+ + 3OH^-\\rightarrow$\n"
         "  $R-COO^- + 2Ag(s) + 2H_2O$\n\n"
         "• Observation:\n"
         "  Silver mirror formed\n"
         "  on clean test-tube walls\n"
         "  (or grey precipitate)"),
        ("Fehling's Solution\n($Cu^{2+}$ in alkali)", 0.62, "#059669",
         "• Tests for: Aldehydes\n"
         "  (Ketones = negative)\n\n"
         "• Reaction: Mild oxidation\n"
         "  $R-CHO + 2Cu^{2+} + 5OH^-\\rightarrow$\n"
         "  $R-COO^- + Cu_2O(s) + 3H_2O$\n\n"
         "• Observation:\n"
         "  Deep blue solution turns to\n"
         "  brick-red precipitate\n"
         "  of copper(I) oxide ($Cu_2O$)"),
        ("Tri-iodomethane\n($I_2$ in $NaOH$)", 0.85, "#d97706",
         "• Tests for: Methyl carbonyl\n"
         "  $CH_3-C(=O)-$ group\n\n"
         "• Substrates: Ethanal\n"
         "  and all methyl ketones\n"
         "  ($CH_3-CO-R$)\n\n"
         "• Observation:\n"
         "  Pale yellow crystalline\n"
         "  precipitate of $CHI_3$\n"
         "  with antiseptic smell")
    ]
    
    for title, cx, col, text in tests:
        w = 0.21
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.08), w, 0.80, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.76), w, 0.12, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.82, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.42, text, ha='left', va='center', fontsize=6.5, color='#1e293b', linespacing=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carbonyl_diagnostic_tests_summary.png")
    plt.close()
    print("Generated figures/carbonyl_diagnostic_tests_summary.png")

def make_reduction_and_hcn():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Reduction of Aldehydes & Ketones using Sodium Borohydride ($NaBH_4$)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Aldehyde Reduction
    ax.add_patch(plt.Rectangle((0.06, 0.18), 0.42, 0.68, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.06, 0.76), 0.42, 0.10, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.27, 0.81, "Aldehyde Reduction -> Primary (1°) Alcohol", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    ald_text = (
        "Reaction:\n"
        "  $R-CHO + 2[H] \\rightarrow R-CH_2OH$\n\n"
        "Reagent & Conditions:\n"
        "• Sodium borohydride ($NaBH_4$)\n"
        "  in aqueous ethanol at room temperature\n\n"
        "Role of Reagent:\n"
        "• Source of nucleophilic hydride ion ($:H^-$)\n"
        "• Attacks electron-deficient carbonyl carbon\n"
        "• Followed by protonation from solvent ($H_2O$)"
    )
    ax.text(0.08, 0.47, ald_text, ha='left', va='center', fontsize=7.0, color='#1e293b', linespacing=1.25)
    
    # Right: Ketone Reduction
    ax.add_patch(plt.Rectangle((0.52, 0.18), 0.42, 0.68, facecolor='#f8fafc', edgecolor='#7c3aed', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.76), 0.42, 0.10, facecolor='#7c3aed', edgecolor='#7c3aed'))
    ax.text(0.73, 0.81, "Ketone Reduction -> Secondary (2°) Alcohol", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    ket_text = (
        "Reaction:\n"
        "  $R_1-CO-R_2 + 2[H] \\rightarrow R_1-CH(OH)-R_2$\n\n"
        "Reagent & Conditions:\n"
        "• Sodium borohydride ($NaBH_4$)\n"
        "  (safer, water-tolerant than $LiAlH_4$)\n\n"
        "Stereochemical Note:\n"
        "• Unsymmetrical ketones ($R_1 \\neq R_2$)\n"
        "  form a new chiral carbon centre\n"
        "• Equal attack on either face yields a\n"
        "  racemic mixture of enantiomers"
    )
    ax.text(0.54, 0.47, ket_text, ha='left', va='center', fontsize=7.0, color='#1e293b', linespacing=1.25)
    
    ax.text(0.5, 0.07, "Contrast: $LiAlH_4$ is a much stronger reducing agent used in dry ether (reacts violently with water).",
            ha='center', va='bottom', fontsize=7.8, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carbonyl_reduction_and_hcn_routes.png")
    plt.close()
    print("Generated figures/carbonyl_reduction_and_hcn_routes.png")

def make_iodoform_cleavage():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Alkaline Tri-iodomethane (Iodoform) Cleavage of Methyl Carbonyls",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left Box: Structural Criterion
    ax.add_patch(plt.Rectangle((0.06, 0.16), 0.42, 0.70, facecolor='#fffbeb', edgecolor='#f59e0b', lw=1.6))
    ax.text(0.27, 0.80, "Structural Requirement: $CH_3-CO-$", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='#b45309')
    
    crit_text = (
        "Must contain the methyl carbonyl group:\n\n"
        "           O\n"
        "           ||\n"
        "    $CH_3 - C - R$\n\n"
        "• Only ONE aldehyde responds: Ethanal ($CH_3CHO$)\n"
        "• All methyl ketones respond ($R-CO-CH_3$):\n"
        "  e.g. Propanone, Butanone, Pentan-2-one\n\n"
        "• Compounds giving negative results:\n"
        "  Methanal, Propanal, Pentan-3-one"
    )
    ax.text(0.08, 0.46, crit_text, ha='left', va='center', fontsize=7.0, color='#1e293b', linespacing=1.25)
    
    # Right Box: Reaction Steps & Observation
    ax.add_patch(plt.Rectangle((0.52, 0.16), 0.42, 0.70, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    ax.text(0.73, 0.80, "Three Chemical Stages & Observation", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='#0b1b36')
    
    stages_text = (
        "Stage 1: Base deprotonation of alpha-methyl group\n"
        "  followed by tri-iodination:\n"
        "  $CH_3-CO-R + 3I_2 + 3OH^- \\rightarrow CI_3-CO-R + 3I^- + 3H_2O$\n\n"
        "Stage 2: Nucleophilic attack of $OH^-$ on carbonyl\n"
        "  carbon and cleavage of $C-C$ bond:\n"
        "  $CI_3-CO-R + OH^- \\rightarrow R-COO^- + CHI_3(s)$\n\n"
        "Observation:\n"
        "• Pale yellow crystalline precipitate of $CHI_3$\n"
        "• Distinctive antiseptic / hospital smell"
    )
    ax.text(0.54, 0.46, stages_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.text(0.5, 0.05, "Overall Equation: $RCOCH_3 + 3I_2 + 4NaOH \\rightarrow CHI_3(s) + RCOONa + 3NaI + 3H_2O$",
            ha='center', va='bottom', fontsize=7.6, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/carbonyl_iodoform_cleavage.png")
    plt.close()
    print("Generated figures/carbonyl_iodoform_cleavage.png")

if __name__ == "__main__":
    make_nucleophilic_addition()
    make_diagnostic_tests()
    make_reduction_and_hcn()
    make_iodoform_cleavage()
