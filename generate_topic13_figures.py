"""
Generate high-DPI figures for Topic 13: Introduction to AS Organic Chemistry.
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

def make_isomerism_tree():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Classification of Isomerism in Organic Chemistry",
            ha='center', va='top', fontsize=11.5, fontweight='bold', color='#0b1b36')
    
    # Root box: ISOMERISM
    ax.add_patch(plt.Rectangle((0.36, 0.80), 0.28, 0.10, facecolor='#0b1b36', edgecolor='#0b1b36', lw=1.5))
    ax.text(0.5, 0.85, "ISOMERISM\nSame molecular formula", ha='center', va='center', fontsize=8.2, fontweight='bold', color='white')
    
    # Left Branch: Structural Isomerism
    ax.add_patch(plt.Rectangle((0.04, 0.58), 0.42, 0.12, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.text(0.25, 0.65, "STRUCTURAL ISOMERISM", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0284c7')
    ax.text(0.25, 0.60, "Different structural formulas / connectivity", ha='center', va='center', fontsize=7.2, color='#475569')
    
    # Right Branch: Stereoisomerism
    ax.add_patch(plt.Rectangle((0.54, 0.58), 0.42, 0.12, facecolor='#f8fafc', edgecolor='#ea580c', lw=1.6))
    ax.text(0.75, 0.65, "STEREOISOMERISM", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#ea580c')
    ax.text(0.75, 0.60, "Same connectivity; different 3D spatial arrangement", ha='center', va='center', fontsize=7.2, color='#475569')
    
    # Connect root to branches
    ax.plot([0.5, 0.25, 0.25], [0.80, 0.74, 0.70], color='#0b1b36', lw=1.4)
    ax.plot([0.5, 0.75, 0.75], [0.80, 0.74, 0.70], color='#0b1b36', lw=1.4)
    
    # Sub-branches under Structural
    struct_subs = [
        ("Chain Isomerism", "Different arrangement of\ncarbon carbon skeleton\n(e.g. butane vs 2-methylpropane)", 0.10),
        ("Positional Isomerism", "Same skeleton; functional\ngroup on different carbon\n(e.g. propan-1-ol vs propan-2-ol)", 0.25),
        ("Functional Group", "Different functional groups\n(e.g. propanal vs propanone\nor ethanol vs methoxymethane)", 0.40)
    ]
    for title, desc, cx in struct_subs:
        w = 0.13
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.14), w, 0.36, facecolor='#f0f9ff', edgecolor='#0284c7', lw=1.2))
        ax.text(cx, 0.45, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0369a1')
        ax.text(cx, 0.28, desc, ha='center', va='center', fontsize=6.5, color='#1e293b', linespacing=1.25)
        ax.plot([cx, cx], [0.58, 0.50], color='#0284c7', lw=1.2)
        
    # Sub-branches under Stereo
    stereo_subs = [
        ("Geometric (cis / trans & E / Z)", "Restricted rotation about C=C bond\nTwo different groups on each carbon\n• E: higher CIP priorities opposite\n• Z: higher CIP priorities together", 0.64),
        ("Optical Isomerism", "Contains a chiral carbon\n(4 different groups attached)\nNon-superimposable mirror images\n(enantiomers) that rotate plane-\npolarised light in opposite directions", 0.86)
    ]
    for title, desc, cx in stereo_subs:
        w = 0.19
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.14), w, 0.36, facecolor='#fff7ed', edgecolor='#ea580c', lw=1.2))
        ax.text(cx, 0.45, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#c2410c')
        ax.text(cx, 0.28, desc, ha='center', va='center', fontsize=6.5, color='#1e293b', linespacing=1.25)
        ax.plot([cx, cx], [0.58, 0.50], color='#ea580c', lw=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/organic_isomerism_classification.png")
    plt.close()
    print("Generated figures/organic_isomerism_classification.png")

def make_bonding_hybridisation():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9.5, 3.8), dpi=300)
    for ax in (ax1, ax2, ax3):
        ax.axis('off')
        
    # Panel 1: sp3
    ax1.add_patch(plt.Rectangle((0.05, 0.05), 0.90, 0.90, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.5))
    ax1.text(0.5, 0.88, r"$\mathbf{sp^3}$ Hybridisation", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax1.text(0.5, 0.76, "Tetrahedral Geometry", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0284c7')
    info1 = (
        "• 4 equivalent $sp^3$ hybrid orbitals\n"
        "• Bond angle: 109.5°\n"
        "• Pure $\\sigma$ (sigma) bonds only\n"
        "• Free rotation about C-C single bond\n"
        "• Example: Methane ($CH_4$), Ethane"
    )
    ax1.text(0.5, 0.44, info1, ha='center', va='center', fontsize=7.5, color='#1e293b', linespacing=1.4)
    
    # Panel 2: sp2
    ax2.add_patch(plt.Rectangle((0.05, 0.05), 0.90, 0.90, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.5))
    ax2.text(0.5, 0.88, r"$\mathbf{sp^2}$ Hybridisation", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax2.text(0.5, 0.76, "Trigonal Planar Geometry", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#ea580c')
    info2 = (
        "• 3 $sp^2$ hybrid orbitals (trigonal planar)\n"
        "• 1 unhybridised $2p$ orbital per C\n"
        "• Bond angle: 120°\n"
        "• 1 $\\sigma$ bond (end-on overlap) +\n"
        "  1 $\\pi$ bond (sideways p overlap)\n"
        "• Restricted rotation (causes E/Z)\n"
        "• Example: Ethene ($H_2C=CH_2$)"
    )
    ax2.text(0.5, 0.44, info2, ha='center', va='center', fontsize=7.5, color='#1e293b', linespacing=1.35)
    
    # Panel 3: sp
    ax3.add_patch(plt.Rectangle((0.05, 0.05), 0.90, 0.90, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.5))
    ax3.text(0.5, 0.88, r"$\mathbf{sp}$ Hybridisation", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax3.text(0.5, 0.76, "Linear Geometry", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#7c3aed')
    info3 = (
        "• 2 $sp$ hybrid orbitals\n"
        "• 2 unhybridised $2p$ orbitals per C\n"
        "• Bond angle: 180°\n"
        "• 1 $\\sigma$ bond + 2 $\\pi$ bonds ($C\\equiv C$)\n"
        "• High electron density in cylindrical $\\pi$ cloud\n"
        "• Example: Ethyne ($HC\\equiv CH$)"
    )
    ax3.text(0.5, 0.44, info3, ha='center', va='center', fontsize=7.5, color='#1e293b', linespacing=1.4)
    
    plt.tight_layout()
    plt.savefig("figures/organic_bonding_hybridisation.png")
    plt.close()
    print("Generated figures/organic_bonding_hybridisation.png")

def make_cip_rules():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Cahn-Ingold-Prelog (CIP) Priority Rules for E / Z Stereoisomerism",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left Card: (Z)-isomer
    ax.add_patch(plt.Rectangle((0.06, 0.18), 0.41, 0.68, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.8))
    ax.text(0.265, 0.80, r"(Z)-Isomer ('Zusammen' = Together)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#15803d')
    z_desc = (
        "High-priority groups on the SAME side\nof the reference double bond axis:\n\n"
        "      High (1)           High (1)\n"
        "           \\                 /\n"
        "            C  ===  C\n"
        "           /                 \\\n"
        "       Low (2)            Low (2)\n\n"
        "Example: (Z)-1-bromo-2-chloroprop-1-ene\n"
        "• On C1: -Br (Z=35) > -H (Z=1)\n"
        "• On C2: -Cl (Z=17) > -CH3 (C has Z=6)\n"
        "Both high priorities (-Br, -Cl) on top"
    )
    ax.text(0.265, 0.48, z_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right Card: (E)-isomer
    ax.add_patch(plt.Rectangle((0.53, 0.18), 0.41, 0.68, facecolor='#eff6ff', edgecolor='#2563eb', lw=1.8))
    ax.text(0.735, 0.80, r"(E)-Isomer ('Entgegen' = Opposite)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#1d4ed8')
    e_desc = (
        "High-priority groups on OPPOSITE sides\nof the reference double bond axis:\n\n"
        "      High (1)            Low (2)\n"
        "           \\                 /\n"
        "            C  ===  C\n"
        "           /                 \\\n"
        "       Low (2)           High (1)\n\n"
        "Example: (E)-1-bromo-2-chloroprop-1-ene\n"
        "• On C1: -Br (Z=35) on top\n"
        "• On C2: -Cl (Z=17) on bottom\n"
        "High priorities (-Br, -Cl) on opposite sides"
    )
    ax.text(0.735, 0.48, e_desc, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    ax.text(0.5, 0.06, "Priority is assigned strictly by highest atomic number (Z) directly bonded to each alkene carbon.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/organic_cip_ez_rules.png")
    plt.close()
    print("Generated figures/organic_cip_ez_rules.png")

def make_reaction_mechanisms_overview():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Organic Reaction Terminology: Fission and Intermediates",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    terms = [
        ("Homolytic Fission", 0.18, "#0284c7",
         "Symmetrical Bond Cleavage\n\n$A-B \\rightarrow A^\\bullet + B^\\bullet$\n(Initiated by UV light)\n\n• Each atom retains 1 electron\n• Single-headed fish-hook arrows\n• Produces Free Radicals\n  (e.g. $Cl^\\bullet$ in alkane halogenation)"),
        ("Heterolytic Fission", 0.50, "#ea580c",
         "Unsymmetrical Bond Cleavage\n\n$A-B \\rightarrow A^+ + :B^-$\n\n• More electronegative atom takes\n  both bonding electrons\n• Double-headed curly arrow\n• Produces Ions / Carbocations\n  (e.g. $R^+$ in halogenoalkane hydrolysis)"),
        ("Reagents & Intermediates", 0.82, "#7c3aed",
         "Species Classifications\n\n• Electrophile ($E^+$):\n  Electron pair acceptor\n  (e.g. $Br^+$, $H^+$, $NO_2^+$)\n• Nucleophile ($:Nu^-$):\n  Electron pair donor with lone pair\n  (e.g. $:OH^-$, $:CN^-$, $:NH_3$)\n• Carbocation stability:\n  Tertiary > Secondary > Primary")
    ]
    
    for title, cx, col, details in terms:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.16), w, 0.68, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.74), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.79, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(x0 + 0.015, 0.44, details, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.3)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/organic_reaction_mechanisms_overview.png")
    plt.close()
    print("Generated figures/organic_reaction_mechanisms_overview.png")

if __name__ == "__main__":
    make_isomerism_tree()
    make_bonding_hybridisation()
    make_cip_rules()
    make_reaction_mechanisms_overview()
