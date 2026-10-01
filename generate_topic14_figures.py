"""
Generate high-DPI figures for Topic 14: Hydrocarbons.
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

def make_free_radical_mechanism():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Mechanism of Free-Radical Substitution (Chlorination of Methane)",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    stages = [
        ("1. Initiation (UV Light)", 0.18, "#0284c7",
         "Homolytic Bond Fission\n\n$Cl-Cl \\rightarrow 2Cl^\\bullet$\n(Initiated by UV light)\n\n• UV light provides energy to break\n  the $Cl-Cl$ bond homolytically\n• Produces two highly reactive\n  chlorine free radicals ($Cl^\\bullet$)"),
        ("2. Propagation (Chain Cycle)", 0.50, "#ea580c",
         "Chain Reaction Steps\n\nStep 1:\n$Cl^\\bullet + CH_4 \\rightarrow ^\\bullet CH_3 + HCl$\n\nStep 2:\n$^\\bullet CH_3 + Cl_2 \\rightarrow CH_3Cl + Cl^\\bullet$\n\n• $Cl^\\bullet$ radical is regenerated,\n  sustaining the chain reaction\n• Explains trace multi-substitution"),
        ("3. Termination", 0.82, "#7c3aed",
         "Radical Combination\n\n$Cl^\\bullet + Cl^\\bullet \\rightarrow Cl_2$\n\n$^\\bullet CH_3 + Cl^\\bullet \\rightarrow CH_3Cl$\n\n$^\\bullet CH_3 + ^\\bullet CH_3 \\rightarrow C_2H_6$\n\n• Two radicals combine to form\n  a stable covalent molecule\n• Formation of ethane ($C_2H_6$)\n  proves methyl radical presence")
    ]
    
    for title, cx, col, text in stages:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.15), w, 0.72, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.77), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.82, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(x0 + 0.015, 0.44, text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.28)
        
    ax.text(0.5, 0.05, "Limitation of free-radical substitution: Produces a mixture of mono-, di-, tri-, and tetra-chloromethanes.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/hydrocarbons_free_radical_substitution.png")
    plt.close()
    print("Generated figures/hydrocarbons_free_radical_substitution.png")

def make_electrophilic_addition():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Electrophilic Addition of $HBr$ to Propene: Markovnikov's Rule",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    # Left box: Major Pathway (Secondary Carbocation)
    ax.add_patch(plt.Rectangle((0.05, 0.16), 0.42, 0.70, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.8))
    ax.text(0.26, 0.80, r"MAJOR PRODUCT: 2-Bromopropane", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#15803d')
    p1 = (
        "Forms via Secondary (2°) Carbocation:\n\n"
        "  $CH_3-CH=CH_2 + H^{\\delta+}-Br^{\\delta-}$\n"
        "            ↓\n"
        "  $CH_3-CH^+-CH_3 + :Br^-$\n"
        "  (Secondary carbocation intermediate)\n\n"
        "• Two electron-releasing methyl groups\n"
        "  disperse positive charge by inductive effect\n"
        "• More stable intermediate → lower $E_a$\n"
        "• Nucleophilic attack by $:Br^-$ gives:\n"
        "  $CH_3-CH(Br)-CH_3$ (MAJOR, ~90%)"
    )
    ax.text(0.26, 0.46, p1, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    # Right box: Minor Pathway (Primary Carbocation)
    ax.add_patch(plt.Rectangle((0.53, 0.16), 0.42, 0.70, facecolor='#fef2f2', edgecolor='#dc2626', lw=1.8))
    ax.text(0.74, 0.80, r"MINOR PRODUCT: 1-Bromopropane", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#991b1b')
    p2 = (
        "Forms via Primary (1°) Carbocation:\n\n"
        "  $CH_3-CH=CH_2 + H^{\\delta+}-Br^{\\delta-}$\n"
        "            ↓\n"
        "  $CH_3-CH_2-CH_2^+ + :Br^-$\n"
        "  (Primary carbocation intermediate)\n\n"
        "• Only one electron-releasing ethyl group\n"
        "  attached to positive carbon\n"
        "• Less stable intermediate → higher $E_a$\n"
        "• Nucleophilic attack by $:Br^-$ gives:\n"
        "  $CH_3-CH_2-CH_2Br$ (MINOR, ~10%)"
    )
    ax.text(0.74, 0.46, p2, ha='center', va='center', fontsize=7.2, color='#1e293b', linespacing=1.25)
    
    ax.text(0.5, 0.05, "Markovnikov's rule: Hydrogen adds to the carbon with more hydrogen atoms already attached.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/hydrocarbons_electrophilic_addition_mechanism.png")
    plt.close()
    print("Generated figures/hydrocarbons_electrophilic_addition_mechanism.png")

def make_alkene_oxidation():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.96, "Oxidative Cleavage of Alkenes with Hot Concentrated Acidified $KMnO_4$",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    rules = [
        ("Terminal $=CH_2$ Group", 0.18, "#0284c7",
         "Oxidises to Carbon Dioxide\n\n$=CH_2 \\rightarrow [HCHO] \\rightarrow$\n$CO_2(g) + H_2O(l)$\n\n• Complete oxidation to $CO_2$\n• Produces effervescence\n• Confirms terminal double bond"),
        ("Monosubstituted $=CHR$", 0.50, "#ea580c",
         "Oxidises to Carboxylic Acid\n\n$=CHR \\rightarrow [R-CHO] \\rightarrow$\n$R-COOH$\n\n• Intermediate aldehyde oxidised\n  further to carboxylic acid\n• e.g. $=CH-CH_3 \\rightarrow CH_3COOH$"),
        ("Disubstituted $=CR_1R_2$", 0.82, "#7c3aed",
         "Oxidises to Ketone\n\n$=CR_1R_2 \\rightarrow$\n$R_1-C(=O)-R_2$\n\n• No C-H bond on alkene carbon;\n  cannot oxidise beyond ketone\n• e.g. $=C(CH_3)_2 \\rightarrow (CH_3)_2C=O$")
    ]
    
    for title, cx, col, text in rules:
        w = 0.28
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.18), w, 0.68, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.76), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.81, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax.text(x0 + 0.015, 0.46, text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.3)
        
    ax.text(0.5, 0.06, "Example: 2-methylbut-2-ene, $(CH_3)_2C=CHCH_3 \\rightarrow (CH_3)_2C=O$ (propanone) $+ CH_3COOH$ (ethanoic acid).",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/hydrocarbons_alkene_oxidation_cleavage.png")
    plt.close()
    print("Generated figures/hydrocarbons_alkene_oxidation_cleavage.png")

def make_addition_polymerisation():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.95, "Addition Polymerisation of Alkenes and Common Polymers",
            ha='center', va='top', fontsize=11, fontweight='bold', color='#0b1b36')
    
    polymers = [
        ("Poly(ethene) [LDPE / HDPE]", 0.2, "#0284c7",
         "Monomer: Ethene ($CH_2=CH_2$)\n\n"
         "Repeat unit:\n"
         "  ---[ CH2 - CH2 ]_n---\n\n"
         "• Plastic bags, clingfilm (LDPE)\n"
         "• Milk bottles, water pipes (HDPE)"),
        ("Poly(propene) [PP]", 0.5, "#ea580c",
         "Monomer: Propene ($CH_2=CHCH_3$)\n\n"
         "Repeat unit:\n"
         "  ---[ CH2 - CH(CH3) ]_n---\n\n"
         "• Food containers, thermal fibres\n"
         "• Car bumpers, ropes, carpets"),
        ("Poly(chloroethene) [PVC]", 0.8, "#16a34a",
         "Monomer: Chloroethene ($CH_2=CHCl$)\n\n"
         "Repeat unit:\n"
         "  ---[ CH2 - CH(Cl) ]_n---\n\n"
         "• Window frames, guttering, pipes\n"
         "• Electrical cable insulation")
    ]
    
    for title, cx, col, text in polymers:
        w = 0.27
        x0 = cx - w/2
        ax.add_patch(plt.Rectangle((x0, 0.16), w, 0.68, facecolor='#f8fafc', edgecolor=col, lw=1.8))
        ax.add_patch(plt.Rectangle((x0, 0.74), w, 0.10, facecolor=col, edgecolor=col, lw=1))
        ax.text(cx, 0.79, title, ha='center', va='center', fontsize=8.2, fontweight='bold', color='white')
        ax.text(x0 + 0.012, 0.44, text, ha='left', va='center', fontsize=7.2, color='#1e293b', linespacing=1.28)
        
    ax.text(0.5, 0.05, "Environmental hazard: Addition polymers are non-biodegradable due to unreactive strong C-C single bonds.",
            ha='center', va='bottom', fontsize=8.0, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef2f2', edgecolor='#f87171'))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig("figures/hydrocarbons_addition_polymerisation.png")
    plt.close()
    print("Generated figures/hydrocarbons_addition_polymerisation.png")

if __name__ == "__main__":
    make_free_radical_mechanism()
    make_electrophilic_addition()
    make_alkene_oxidation()
    make_addition_polymerisation()
