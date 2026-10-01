"""
Generate high-DPI figures for Topic 16: Hydroxy Compounds (Alcohols).
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

def make_oxidation_routes():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Oxidation Pathways for Primary, Secondary, and Tertiary Alcohols",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # 3 Boxes: 1°, 2°, 3° Alcohols
    classes = [
        ("Primary (1°) Alcohol", 0.18, "#0284c7",
         "$R-CH_2OH$\n(e.g. Ethanol)\n\n"
         "• Distil with $K_2Cr_2O_7 / H^+$:\n"
         "  $\\rightarrow R-CHO$ (Aldehyde)\n"
         "  (orange $\\rightarrow$ green $Cr^{3+}$)\n\n"
         "• Reflux with excess $K_2Cr_2O_7 / H^+$:\n"
         "  $\\rightarrow R-COOH$ (Carboxylic acid)"),
        ("Secondary (2°) Alcohol", 0.50, "#ea580c",
         "$R_1-CH(OH)-R_2$\n(e.g. Propan-2-ol)\n\n"
         "• Reflux with $K_2Cr_2O_7 / H^+$:\n"
         "  $\\rightarrow R_1-CO-R_2$ (Ketone)\n"
         "  (orange $\\rightarrow$ green $Cr^{3+}$)\n\n"
         "• Cannot oxidise further\n"
         "  (no C-H bond on carbonyl C)"),
        ("Tertiary (3°) Alcohol", 0.82, "#7c3aed",
         "$R_1R_2R_3C-OH$\n(e.g. 2-methylpropan-2-ol)\n\n"
         "• Heated with $K_2Cr_2O_7 / H^+$:\n"
         "  $\\rightarrow$ NO REACTION\n"
         "  (solution remains ORANGE)\n\n"
         "• No hydrogen atom on the\n"
         "  carbinol carbon atom\n"
         "  (C-C bonds cannot cleave)")
    ]
    
    for title, cx, col, text in classes:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.15), w, 0.72, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.77), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.82, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(x0 + 0.015, 0.44, text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.28)
        
    ax.text(0.5, 0.05, "Colour change for 1° and 2° alcohols: Orange dichromate(VI), $Cr_2O_7^{2-}$, is reduced to green chromium(III), $Cr^{3+}$.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/alcohols_oxidation_routes.png")
    plt.close()
    print("Generated figures/alcohols_oxidation_routes.png")

def make_dehydration_apparatus():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Laboratory Catalytic Dehydration of Ethanol to Ethene",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Boiling tube
    ax.add_patch(plt.Rectangle((0.10, 0.45), 0.45, 0.22, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    
    # Mineral wool soaked in ethanol (left inside tube)
    ax.add_patch(plt.Rectangle((0.11, 0.47), 0.10, 0.18, facecolor='#fef08a', edgecolor='#ca8a04', lw=1))
    ax.text(0.16, 0.56, "Mineral wool\nsoaked in\nethanol", ha='center', va='center', fontsize=6.5, color='#854d0e')
    
    # Al2O3 catalyst granules (center inside tube)
    ax.add_patch(plt.Rectangle((0.30, 0.47), 0.12, 0.18, facecolor='#cbd5e1', edgecolor='#475569', lw=1))
    ax.text(0.36, 0.56, "Pumice / Al₂O₃\ncatalyst\ngranules", ha='center', va='center', fontsize=6.5, fontweight='bold', color='#1e293b')
    
    # Heat arrow under Al2O3
    ax.annotate("Heat strongly\n(Bunsen flame)", xy=(0.36, 0.45), xytext=(0.36, 0.25),
                arrowprops=dict(arrowstyle='->', lw=1.6, color='#dc2626'),
                ha='center', va='top', fontsize=7.5, fontweight='bold', color='#dc2626')
    
    # Delivery tube
    ax.plot([0.55, 0.70, 0.70], [0.56, 0.56, 0.38], color='#0b1b36', lw=2)
    
    # Water trough (right)
    ax.add_patch(plt.Rectangle((0.62, 0.18), 0.32, 0.20, facecolor='#e0f2fe', edgecolor='#0284c7', lw=1.4))
    ax.text(0.78, 0.22, "Water trough", ha='center', va='center', fontsize=7.2, color='#0369a1')
    
    # Inverted test tube collecting gas
    ax.add_patch(plt.Rectangle((0.67, 0.26), 0.08, 0.35, facecolor='#ecfdf5', edgecolor='#15803d', lw=1.4))
    ax.text(0.71, 0.54, "Ethene gas\n(C₂H₄)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#15803d')
    
    # Equation note
    ax.text(0.5, 0.08, "Reaction: $CH_3CH_2OH \\rightarrow CH_2=CH_2 + H_2O$  (heated over $Al_2O_3$ catalyst at $300^\\circ\\mathrm{C}$)",
            ha='center', va='bottom', fontsize=8.2, fontweight='bold', color='#0b1b36',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/alcohols_dehydration_apparatus.png")
    plt.close()
    print("Generated figures/alcohols_dehydration_apparatus.png")

def make_esterification():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Acid-Catalysed Esterification Equilibrium and Work-Up",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Reaction Box (top)
    ax.add_patch(plt.Rectangle((0.06, 0.54), 0.88, 0.34, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    eq_text = (
        "Reversible Condensation Reaction:\n\n"
        "  $CH_3COOH(l) + CH_3CH_2OH(l) \\rightleftharpoons CH_3COOCH_2CH_3(l) + H_2O(l)$\n"
        "  Ethanoic acid          Ethanol                                Ethyl ethanoate             Water\n\n"
        "• Catalyst: Concentrated $H_2SO_4$ (acts as acid catalyst and dehydrating agent)\n"
        "• Condition: Heat under reflux"
    )
    ax.text(0.50, 0.70, eq_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.2)
    
    # Purification steps (bottom cards)
    steps = [
        ("1. Neutralisation", 0.22, "#0284c7", "Shake in separating funnel\nwith aqueous $Na_2CO_3$\nto remove unreacted acid"),
        ("2. Washing", 0.50, "#ea580c", "Wash organic layer with\naqueous $CaCl_2$ to remove\nunreacted ethanol"),
        ("3. Drying & Distil", 0.78, "#16a34a", "Dry with anhydrous $MgSO_4$;\nfractionally distil ester\n(b.p. 77 °C; fruity aroma)")
    ]
    for title, cx, col, text in steps:
        w = 0.26
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.12), w, 0.35, facecolor='#f8fafc', edgecolor=col, lw=1.4))
        ax.add_patch(plt.Rectangle((x0, 0.40), w, 0.07, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.435, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='white')
        ax.text(cx, 0.26, text, ha='center', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/alcohols_esterification_equilibrium.png")
    plt.close()
    print("Generated figures/alcohols_esterification_equilibrium.png")

def make_iodoform_test():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "The Tri-iodomethane (Iodoform) Diagnostic Test for Alcohols",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left box: Structural Requirement
    ax.add_patch(plt.Rectangle((0.05, 0.18), 0.42, 0.68, facecolor='#fffbeb', edgecolor='#f59e0b', lw=1.8))
    ax.text(0.26, 0.80, "Specific Structural Requirement", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#b45309')
    req_text = (
        "Must contain the group:\n\n"
        "           H\n"
        "           |\n"
        "    $CH_3 - C - OH$\n"
        "           |\n"
        "           R\n\n"
        "Where R = H (Ethanol) or\n"
        "      R = alkyl group (secondary methyl alcohol)\n\n"
        "• Positive alcohols: Ethanol, Propan-2-ol, Butan-2-ol\n"
        "• Negative alcohols: Methanol, Propan-1-ol, Butan-1-ol,\n"
        "                     2-methylpropan-2-ol (tertiary)"
    )
    ax.text(0.26, 0.48, req_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right box: Chemistry and Observations
    ax.add_patch(plt.Rectangle((0.53, 0.18), 0.42, 0.68, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    ax.text(0.74, 0.80, "Reagents, Steps & Observation", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0b1b36')
    obs_text = (
        "Reagents:\n"
        "• Aqueous iodine ($I_2$) and aqueous $NaOH$\n"
        "  (warm gently)\n\n"
        "Chemical Steps:\n"
        "1. Oxidation to methyl ketone: $CH_3-CO-R$\n"
        "2. Tri-iodination: $CI_3-CO-R$\n"
        "3. Alkaline cleavage: $\\rightarrow CHI_3 + RCOO^-$\n\n"
        "Observation:\n"
        "• Pale yellow crystalline precipitate of $CHI_3$\n"
        "• Characteristic medicinal / antiseptic smell"
    )
    ax.text(0.74, 0.48, obs_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.22)
    
    ax.text(0.5, 0.06, "Equation: $CH_3CH(OH)CH_3 + 4I_2 + 6NaOH \\rightarrow CHI_3(s) + CH_3COONa + 5NaI + 5H_2O$",
            ha='center', va='bottom', fontsize=7.8, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/alcohols_iodoform_test_reaction.png")
    plt.close()
    print("Generated figures/alcohols_iodoform_test_reaction.png")

if __name__ == "__main__":
    make_oxidation_routes()
    make_dehydration_apparatus()
    make_esterification()
    make_iodoform_test()
