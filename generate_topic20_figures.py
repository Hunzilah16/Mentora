"""
Generate high-DPI figures for Topic 20: Polymerisation (Addition Polymerisation).
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

def make_addition_mechanism():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Addition Polymerisation: Alkene Monomers to Saturated Polymers",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Top Box: General Equation and Mechanism
    ax.add_patch(plt.Rectangle((0.04, 0.54), 0.92, 0.36, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.04, 0.83), 0.92, 0.07, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.50, 0.865, "General Principle: Opening of the Carbon-Carbon Double Bond",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color='white')
    
    top_text = (
        "Reaction:  $n\\ CH_2=CH(R) \\rightarrow -[CH_2-CH(R)]-_n$  (Atom Economy = 100%)\n\n"
        "• Unsaturation is lost: the weak $\\pi$-bond in each alkene monomer breaks\n"
        "• New strong $C-C\\ \\sigma$-bonds form between adjacent monomer units\n"
        "• The polymer contains ONLY single bonds along its carbon backbone\n"
        "• Repeat unit is enclosed in brackets with continuation bonds passing through"
    )
    ax.text(0.06, 0.68, top_text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Bottom: 4 Common Polymers
    polys = [
        ("Poly(ethene)", 0.16, "#16a34a", "Monomer: $CH_2=CH_2$\nRepeat: $-[CH_2-CH_2]-$\nUses: Plastic bags,\nbottles, pipes"),
        ("Poly(propene)", 0.39, "#0284c7", "Monomer: $CH_2=CHCH_3$\nRepeat: $-[CH_2-CH(CH_3)]-$\nUses: Ropes, carpets,\nfood containers"),
        ("Poly(chloroethene) (PVC)", 0.62, "#ea580c", "Monomer: $CH_2=CHCl$\nRepeat: $-[CH_2-CH(Cl)]-$\nUses: Window frames,\ninsulation, piping"),
        ("PTFE (Teflon)", 0.85, "#7c3aed", "Monomer: $CF_2=CF_2$\nRepeat: $-[CF_2-CF_2]-$\nUses: Non-stick pans,\nchemical gaskets")
    ]
    for title, cx, col, text in polys:
        w = 0.21
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.08), w, 0.40, facecolor='#f8fafc', edgecolor=col, lw=1.4))
        ax.add_patch(plt.Rectangle((x0, 0.41), w, 0.07, facecolor=col, edgecolor=col))
        ax.text(cx, 0.445, title, ha='center', va='center', fontsize=7.2, fontweight='bold', color='white')
        ax.text(cx, 0.24, text, ha='center', va='center', fontsize=6.5, color='#1e293b', linespacing=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/polymers_addition_mechanism_and_repeat_units.png")
    plt.close()
    print("Generated figures/polymers_addition_mechanism_and_repeat_units.png")

def make_ldpe_vs_hdpe():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Structure & Properties: Low Density (LDPE) vs High Density Polyethene (HDPE)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: LDPE
    ax.add_patch(plt.Rectangle((0.05, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.05, 0.78), 0.43, 0.08, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.265, 0.82, "Low Density Polyethene (LDPE)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    ldpe_text = (
        "Polymerisation Conditions:\n"
        "• High pressure (~1500-3000 atm)\n"
        "• High temperature (~200 °C, trace $O_2$ initiator)\n\n"
        "Molecular Architecture:\n"
        "• Highly branched chains (frequent side chains)\n"
        "• Branches prevent polymer chains from packing\n"
        "  closely and regularly together\n\n"
        "Physical Properties:\n"
        "• Weaker London dispersion forces\n"
        "• Lower density (~0.92 g cm⁻³)\n"
        "• Lower melting point (~105 °C)\n"
        "• Flexible, soft (used in cling film, plastic bags)"
    )
    ax.text(0.07, 0.46, ldpe_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    # Right: HDPE
    ax.add_patch(plt.Rectangle((0.52, 0.14), 0.43, 0.72, facecolor='#f8fafc', edgecolor='#16a34a', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.78), 0.43, 0.08, facecolor='#16a34a', edgecolor='#16a34a'))
    ax.text(0.735, 0.82, "High Density Polyethene (HDPE)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    hdpe_text = (
        "Polymerisation Conditions:\n"
        "• Low pressure (~2-10 atm)\n"
        "• Moderate temperature (~60 °C)\n"
        "• Ziegler-Natta catalyst ($TiCl_4 / Al(C_2H_5)_3$)\n\n"
        "Molecular Architecture:\n"
        "• Highly linear unbranched chains\n"
        "• Chains pack tightly in close parallel alignment\n\n"
        "Physical Properties:\n"
        "• Stronger London dispersion forces\n"
        "• Higher density (~0.96 g cm⁻³)\n"
        "• Higher melting point (~135 °C)\n"
        "• Rigid, hard, tough (used in milk crates, buckets)"
    )
    ax.text(0.54, 0.46, hdpe_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/polymers_ldpe_vs_hdpe_structure.png")
    plt.close()
    print("Generated figures/polymers_ldpe_vs_hdpe_structure.png")

def make_pvc_plasticisers():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Structure of PVC: Dipole Attractions & Effect of Plasticisers",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left: Unplasticised PVC (uPVC)
    ax.add_patch(plt.Rectangle((0.05, 0.16), 0.43, 0.70, facecolor='#f8fafc', edgecolor='#dc2626', lw=1.6))
    ax.add_patch(plt.Rectangle((0.05, 0.78), 0.43, 0.08, facecolor='#dc2626', edgecolor='#dc2626'))
    ax.text(0.265, 0.82, "Unplasticised PVC (uPVC)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    upvc_text = (
        "Intermolecular Forces:\n"
        "• Highly polar $C^{\\delta+} - Cl^{\\delta-}$ bonds along the chain\n"
        "• Strong permanent dipole-dipole attractions\n"
        "  lock adjacent chains firmly together\n\n"
        "Properties:\n"
        "• Rigid, hard, and stiff polymer\n"
        "• High tensile strength\n\n"
        "Applications:\n"
        "• Rigid drainage pipes, window frame profiles,\n"
        "  and exterior building cladding"
    )
    ax.text(0.07, 0.47, upvc_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    # Right: Plasticised PVC
    ax.add_patch(plt.Rectangle((0.52, 0.16), 0.43, 0.70, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.6))
    ax.add_patch(plt.Rectangle((0.52, 0.78), 0.43, 0.08, facecolor='#0284c7', edgecolor='#0284c7'))
    ax.text(0.735, 0.82, "Plasticised Flexible PVC", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='white')
    
    flex_text = (
        "Action of Plasticisers (e.g. Phthalate Esters):\n"
        "• Small ester molecules insert between chains\n"
        "• Pushes polymer chains further apart\n"
        "• Significantly weakens dipole-dipole attractions\n"
        "• Allows chains to slide smoothly over each other\n\n"
        "Properties:\n"
        "• Flexible, bendable, rubber-like\n\n"
        "Applications:\n"
        "• Electrical cable insulation, flexible garden hoses,\n"
        "  waterproof clothing, artificial leather"
    )
    ax.text(0.54, 0.47, flex_text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
    
    ax.text(0.5, 0.05, "Plasticisers act as internal molecular lubricants, lowering the glass transition temperature ($T_g$).",
            ha='center', va='bottom', fontsize=7.8, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/polymers_pvc_plasticisers_dipoles.png")
    plt.close()
    print("Generated figures/polymers_pvc_plasticisers_dipoles.png")

def make_disposal_and_recycling():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Disposal and Waste Management Strategies for Synthetic Polymers",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    strategies = [
        ("1. Landfill Disposal", 0.18, "#64748b",
         "• Disadvantage:\n"
         "  Non-biodegradable; non-polar\n"
         "  saturated C-C bonds resist\n"
         "  bacterial enzymes\n"
         "• Consequence:\n"
         "  Persists for centuries;\n"
         "  consumes scarce land volume"),
        ("2. Incineration & Energy", 0.50, "#dc2626",
         "• Advantage:\n"
         "  High calorific value generates\n"
         "  valuable electricity\n"
         "• Hazards & Scrubbing:\n"
         "  PVC produces acidic $HCl(g)$\n"
         "  must scrub with base ($CaO$):\n"
         "  $CaO + 2HCl \\rightarrow CaCl_2 + H_2O$"),
        ("3. Recycling & Feedstock", 0.82, "#16a34a",
         "• Mechanical Recycling:\n"
         "  Sort by resin code, clean,\n"
         "  melt, and remould\n"
         "• Chemical Feedstock (Pyrolysis):\n"
         "  Thermal cracking converts\n"
         "  polymers back to monomers\n"
         "  or chemical feedstocks")
    ]
    
    for title, cx, col, text in strategies:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.10), w, 0.76, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.74), w, 0.12, facecolor=col, edgecolor=col))
        ax.text(cx, 0.80, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.42, text, ha='left', va='center', fontsize=6.8, color='#1e293b', linespacing=1.22)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/polymers_recycling_and_disposal.png")
    plt.close()
    print("Generated figures/polymers_recycling_and_disposal.png")

if __name__ == "__main__":
    make_addition_mechanism()
    make_ldpe_vs_hdpe()
    make_pvc_plasticisers()
    make_disposal_and_recycling()
