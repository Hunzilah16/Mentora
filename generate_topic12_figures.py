"""
Generate high-DPI figures for Topic 12: Nitrogen and Sulfur.
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

def make_contact_process():
    fig, ax = plt.subplots(figsize=(7.8, 4.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "The Contact Process: Industrial Manufacture of Sulfuric Acid",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    steps = [
        ("Stage 1: Production of $SO_2$", 0.18, "#0284c7",
         "Combustion of Sulfur or Roasting of Sulfide Ores\n\n$S(s) + O_2(g) \\rightarrow SO_2(g)$\n\nor $4FeS_2 + 11O_2 \\rightarrow 2Fe_2O_3 + 8SO_2$"),
        ("Stage 2: Catalytic Oxidation", 0.50, "#ea580c",
         "Reversible Exothermic Equilibrium\n\n$2SO_2(g) + O_2(g) \\rightleftharpoons 2SO_3(g)$\n$\\Delta H = -196\\ \\mathrm{kJ\\cdot mol^{-1}}$\n• Temperature: $450\\ ^\\circ\\mathrm{C}$\n• Pressure: $1 - 2\\ \\mathrm{atm}$\n• Catalyst: $V_2O_5$ (Vanadium(V) oxide)"),
        ("Stage 3: Absorption & Dilution", 0.82, "#7c3aed",
         "Formation of Oleum & Dilution\n\n$SO_3(g) + H_2SO_4(l) \\rightarrow H_2S_2O_7(l)$\n(Oleum / Fuming Sulfuric Acid)\n\n$H_2S_2O_7(l) + H_2O(l) \\rightarrow 2H_2SO_4(l)$\n(Yields 98% Concentrated $H_2SO_4$)")
    ]
    
    for title, cx, col, details in steps:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.15), w, 0.70, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.75), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.80, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(x0 + 0.015, 0.44, details, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.35)
        
    ax.text(0.5, 0.05, "Why $SO_3$ is not added directly to water: Reaction is violently exothermic, creating a corrosive mist of $H_2SO_4$ that cannot be condensed.",
            ha='center', va='bottom', fontsize=7.8, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/nitrogen_sulfur_contact_process.png")
    plt.close()
    print("Generated figures/nitrogen_sulfur_contact_process.png")

def make_catalytic_converter():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Automotive Three-Way Catalytic Converter Reactions",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Engine emissions box (left)
    ax.add_patch(plt.Rectangle((0.04, 0.28), 0.24, 0.52, facecolor='#fee2e2', edgecolor='#b91c1c', lw=1.6))
    ax.text(0.16, 0.73, "Engine Exhaust", ha='center', va='center', fontsize=9, fontweight='bold', color='#991b1b')
    ax.text(0.16, 0.50, "Harmful Pollutants:\n• $NO_x$ ($NO$, $NO_2$)\n• $CO$ (Carbon monoxide)\n• Unburnt Hydrocarbons\n  ($C_xH_y$)", 
            ha='center', va='center', fontsize=8, color='#1e293b', linespacing=1.4)
    
    # Arrow to converter
    ax.annotate("", xy=(0.35, 0.54), xytext=(0.28, 0.54),
                arrowprops=dict(arrowstyle='->', lw=2, color='#0b1b36'))
    
    # Catalytic converter chamber (center)
    ax.add_patch(plt.Rectangle((0.35, 0.22), 0.30, 0.64, facecolor='#f1f5f9', edgecolor='#0b1b36', lw=2))
    ax.text(0.50, 0.78, "Catalytic Converter", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.text(0.50, 0.69, "Honeycomb Pt / Rh / Pd Catalyst", ha='center', va='center', fontsize=7.5, style='italic', color='#475569')
    
    reactions = (
        "Reactions on surface:\n"
        "$2NO + 2CO \\rightarrow N_2 + 2CO_2$\n\n"
        "$2CO + O_2 \\rightarrow 2CO_2$\n\n"
        "$C_xH_y + (x + \\frac{y}{4})O_2 \\rightarrow$\n"
        "           $xCO_2 + \\frac{y}{2}H_2O$"
    )
    ax.text(0.50, 0.44, reactions, ha='center', va='center', fontsize=7.2, fontweight='bold', color='#0b1b36', linespacing=1.2)
    
    # Arrow to clean exhaust
    ax.annotate("", xy=(0.72, 0.54), xytext=(0.65, 0.54),
                arrowprops=dict(arrowstyle='->', lw=2, color='#0b1b36'))
    
    # Clean tailpipe emissions box (right)
    ax.add_patch(plt.Rectangle((0.72, 0.28), 0.24, 0.52, facecolor='#dcfce7', edgecolor='#15803d', lw=1.6))
    ax.text(0.84, 0.73, "Tailpipe Output", ha='center', va='center', fontsize=9, fontweight='bold', color='#166534')
    ax.text(0.84, 0.50, "Less Harmful Gases:\n• $N_2$ (Harmless)\n• $CO_2$ (Greenhouse gas)\n• $H_2O$ (Water vapour)",
            ha='center', va='center', fontsize=8, color='#1e293b', linespacing=1.4)
    
    ax.text(0.5, 0.08, "High temperatures in car engines cause atmospheric $N_2$ and $O_2$ to combine: $N_2 + O_2 \\rightarrow 2NO$.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/nitrogen_oxides_catalytic_converter.png")
    plt.close()
    print("Generated figures/nitrogen_oxides_catalytic_converter.png")

def make_eutrophication():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Sequence of Events in Environmental Eutrophication",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    steps = [
        ("1. Leaching", 0.12, "#38bdf8", "Excess nitrate ($NO_3^-$)\nfertilisers washed\nfrom fields by rain into\nrivers and lakes"),
        ("2. Algal Bloom", 0.37, "#22c55e", "Rapid growth of algae\non water surface;\nsunlight blocked from\nsubmerged aquatic plants"),
        ("3. Plant Death", 0.63, "#f59e0b", "Submerged aquatic\nplants die due to lack\nof light; algae die\nwhen nutrients depleted"),
        ("4. Deoxygenation", 0.88, "#ef4444", "Aerobic bacteria\ndecompose dead plants;\ndissolved $O_2$ depleted;\nfish & aquatic life die")
    ]
    
    for title, cx, col, text in steps:
        w = 0.21
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.22), w, 0.58, facecolor='#f8fafc', edgecolor=col, lw=1.6))
        ax.add_patch(plt.Rectangle((x0, 0.70), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.75, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(cx, 0.45, text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.3)
        
    for i in range(len(steps)-1):
        x1 = steps[i][1] + 0.105
        x2 = steps[i+1][1] - 0.105
        ax.annotate("", xy=(x2, 0.51), xytext=(x1, 0.51),
                    arrowprops=dict(arrowstyle='->', lw=1.6, color='#64748b'))
        
    ax.text(0.5, 0.06, "Eutrophication is caused by high solubility of nitrate salts ($NH_4NO_3$) which are easily leached from topsoil.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/nitrogen_cycle_eutrophication.png")
    plt.close()
    print("Generated figures/nitrogen_cycle_eutrophication.png")

def make_acid_rain_catalysis():
    fig, ax = plt.subplots(figsize=(7.5, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Atmospheric Oxidation of $SO_2$ Catalysed by Nitrogen Oxides ($NO_2$)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left box: Catalytic Cycle
    ax.add_patch(plt.Rectangle((0.05, 0.18), 0.42, 0.68, facecolor='#f8fafc', edgecolor='#0b1b36', lw=1.6))
    ax.text(0.26, 0.80, "Homogeneous Catalytic Cycle", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#0b1b36')
    cycle_text = (
        "Step 1: Oxidation of $SO_2$\n"
        "$SO_2(g) + NO_2(g) \\rightarrow SO_3(g) + NO(g)$\n\n"
        "Step 2: Regeneration of $NO_2$\n"
        "$2NO(g) + O_2(g) \\rightarrow 2NO_2(g)$\n\n"
        "Overall Reaction (catalysed by $NO_2$):\n"
        "$2SO_2(g) + O_2(g) \\rightarrow 2SO_3(g)$\n\n"
        "Formation of Acid Rain:\n"
        "$SO_3(g) + H_2O(l) \\rightarrow H_2SO_4(aq)$\n"
        "$4NO_2(g) + 2H_2O(l) + O_2(g) \\rightarrow 4HNO_3(aq)$"
    )
    ax.text(0.26, 0.48, cycle_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right box: Environmental Impacts
    ax.add_patch(plt.Rectangle((0.53, 0.18), 0.42, 0.68, facecolor='#fff1f2', edgecolor='#e11d48', lw=1.6))
    ax.text(0.74, 0.80, "Environmental Consequences", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#9f1239')
    impact_text = (
        "• Chemical weathering of limestone & marble:\n"
        "  $CaCO_3(s) + H_2SO_4(aq) \\rightarrow$\n"
        "     $CaSO_4(s) + CO_2(g) + H_2O(l)$\n\n"
        "• Leaching of toxic aluminium ions:\n"
        "  $Al^{3+}(aq)$ leached from soil into waterways,\n"
        "  damaging fish gills and aquatic systems\n\n"
        "• Defoliation of forests:\n"
        "  Damages leaf cuticle and leaches nutrients\n"
        "  ($Mg^{2+}, Ca^{2+}$) essential for chlorophyll"
    )
    ax.text(0.74, 0.48, impact_text, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/atmospheric_acid_rain_catalysis.png")
    plt.close()
    print("Generated figures/atmospheric_acid_rain_catalysis.png")

if __name__ == "__main__":
    make_contact_process()
    make_catalytic_converter()
    make_eutrophication()
    make_acid_rain_catalysis()
