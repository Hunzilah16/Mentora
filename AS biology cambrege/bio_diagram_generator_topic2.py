"""
Cambridge International AS Level Biology (9700)
Topic 2: Biological Molecules — High-Precision Publication-Quality Diagram Generator
Generates 14 high-resolution 300 DPI figures for Topic 2:
1.  fig2_1_benedicts_reducing_test.png
2.  fig2_2_alpha_beta_glucose.png
3.  fig2_3_maltose_condensation.png
4.  fig2_4_amylose_amylopectin_glycogen.png
5.  fig2_5_cellulose_microfibril.png
6.  fig2_6_triglyceride_condensation.png
7.  fig2_7_phospholipid_structure.png
8.  fig2_8_amino_acid_peptide_bond.png
9.  fig2_9_protein_tertiary_interactions.png
10. fig2_10_haemoglobin_quaternary.png
11. fig2_11_collagen_triple_helix.png
12. fig2_12_water_dipole_hbonding.png
13. fig2_13_biochemical_testing_flowchart.png
14. fig2_14_sucrose_condensation.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Rectangle, Polygon, PathPatch
from matplotlib.path import Path
import numpy as np

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mentora Palette
NAVY = "#0b1b36"
DEEP_NAVY = "#132646"
CRIMSON = "#a81717"
DARK_GREY = "#20242e"
MID_GREY = "#5a6275"
LIGHT_GREY = "#f0f2f5"
WHITE = "#ffffff"

# ==============================================================================
# FIG 2.1: BENEDICT'S TEST & COLORIMETRY CALIBRATION CURVE
# ==============================================================================
def generate_fig2_1(filename="fig2_1_benedicts_reducing_test.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.2]})
    
    # Left Panel: Test tubes colour progression
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 80)
    ax1.axis('off')
    ax1.text(50, 75, "Semi-Quantitative Benedict's Colour Standards", fontsize=8.5, fontweight='bold',
             color=NAVY, ha='center')
    
    tubes = [
        ("0.0%", "#2b75d6", "Blue\n(None)", 12),
        ("0.5%", "#48a868", "Green\n(Trace)", 31),
        ("1.0%", "#e6b800", "Yellow\n(Low)", 50),
        ("1.5%", "#e07822", "Orange\n(Moderate)", 69),
        ("2.0%+", "#b52b27", "Brick-Red\n(High)", 88)
    ]
    
    for conc, col, label, x in tubes:
        # Test tube body
        ax1.add_patch(FancyBboxPatch((x-6, 18), 12, 42, boxstyle="round,pad=1,rounding_size=4",
                                     facecolor="#f9fbfd", edgecolor=NAVY, linewidth=1.2))
        # Liquid fill
        ax1.add_patch(FancyBboxPatch((x-5.2, 19), 10.4, 26, boxstyle="round,pad=0.5,rounding_size=3",
                                     facecolor=col, edgecolor=col, alpha=0.85))
        # Precipitate base if >= 1.0%
        if conc in ["1.0%", "1.5%", "2.0%+"]:
            ax1.add_patch(FancyBboxPatch((x-5.2, 18.5), 10.4, 6, boxstyle="round,pad=0.5,rounding_size=2",
                                         facecolor=col, edgecolor=NAVY, linewidth=0.8, alpha=0.95))
        # Text labels
        ax1.text(x, 63, conc, fontsize=7.5, fontweight='bold', color=DEEP_NAVY, ha='center')
        ax1.text(x, 8, label, fontsize=6.5, color=DARK_GREY, ha='center')

    # Right Panel: Colorimeter Calibration Curve
    ax2.set_xlim(0, 2.5)
    ax2.set_ylim(0, 1.2)
    ax2.set_xlabel("Reducing Sugar Concentration / % (g / 100 cm³)", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Absorbance / Arbitrary Units (680 nm red filter)", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_title("Colorimeter Absorbance Calibration Curve", fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    # Standard points and curve
    x_pts = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    y_pts = np.array([0.05, 0.28, 0.54, 0.81, 1.08])
    ax2.plot(x_pts, y_pts, 'o', color=CRIMSON, markersize=5.5, label='Standard solutions')
    
    # Best-fit line
    m, b = np.polyfit(x_pts, y_pts, 1)
    x_line = np.linspace(0, 2.4, 50)
    ax2.plot(x_line, m*x_line + b, '-', color=NAVY, linewidth=1.5, label='Best-fit calibration line')
    
    # Unknown Sample reading demonstration
    unknown_abs = 0.65
    unknown_conc = (unknown_abs - b) / m
    ax2.plot([0, unknown_conc], [unknown_abs, unknown_abs], 'k--', linewidth=1.0)
    ax2.plot([unknown_conc, unknown_conc], [0, unknown_abs], 'k--', linewidth=1.0)
    ax2.plot(unknown_conc, unknown_abs, 's', color="#2b75d6", markersize=6, label=f'Sample X (Abs={unknown_abs})')
    ax2.annotate(f'Unknown Sample X\nConc = {unknown_conc:.2f}%', xy=(unknown_conc, unknown_abs),
                 xytext=(unknown_conc - 0.75, unknown_abs + 0.18),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                 fontsize=7.2, fontweight='bold', color=NAVY,
                 bbox=dict(boxstyle="round,pad=0.3", fc="#eef4fc", ec=NAVY, lw=0.8))
    
    ax2.legend(loc='lower right', fontsize=6.8, framealpha=0.9)
    ax2.tick_params(labelsize=7)
    
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.2: ALPHA-GLUCOSE AND BETA-GLUCOSE RING STRUCTURES
# ==============================================================================
def generate_fig2_2(filename="fig2_2_alpha_beta_glucose.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.8), dpi=300)
    
    def draw_glucose(ax, is_alpha, title):
        ax.set_xlim(-2.5, 3.5)
        ax.set_ylim(-3.0, 3.0)
        ax.axis('off')
        ax.set_title(title, fontsize=8.8, fontweight='bold', color=NAVY, pad=6)
        
        # Ring coordinates (Haworth pyranose projection)
        # Oxygen at top right, C1 right, C2 bottom right, C3 bottom left, C4 left, C5 top left
        ring = {
            'O': (0.8, 1.4),
            'C1': (1.8, 0.4),
            'C2': (1.1, -1.2),
            'C3': (-1.1, -1.2),
            'C4': (-1.8, 0.4),
            'C5': (-0.8, 1.4)
        }
        
        # Draw ring bonds
        ring_order = ['C5', 'O', 'C1', 'C2', 'C3', 'C4', 'C5']
        for i in range(len(ring_order)-1):
            p1 = ring[ring_order[i]]
            p2 = ring[ring_order[i+1]]
            # Thicker front edge (C2 to C3)
            lw = 2.4 if (ring_order[i] in ['C2', 'C3'] and ring_order[i+1] in ['C2', 'C3']) else 1.5
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=NAVY, linewidth=lw)
            
        # Draw Oxygen atom
        ax.text(ring['O'][0], ring['O'][1], 'O', fontsize=11, fontweight='bold', color=NAVY,
                ha='center', va='center', bbox=dict(boxstyle='circle', fc=WHITE, ec='none'))
        
        # C6 - CH2OH group at C5
        ax.plot([ring['C5'][0], ring['C5'][0]], [ring['C5'][1], ring['C5'][1]+0.9], color=NAVY, linewidth=1.4)
        ax.text(ring['C5'][0], ring['C5'][1]+1.15, 'CH₂OH (C6)', fontsize=7.2, fontweight='bold',
                color=DARK_GREY, ha='center')
        ax.text(ring['C5'][0]+0.3, ring['C5'][1]-0.4, 'H', fontsize=7.0, color=DARK_GREY)
        
        # C4 substituents (H above, OH below)
        ax.plot([ring['C4'][0], ring['C4'][0]-0.6], [ring['C4'][1], ring['C4'][1]+0.4], color=NAVY, linewidth=1.2)
        ax.text(ring['C4'][0]-0.8, ring['C4'][1]+0.5, 'H', fontsize=7.0, color=DARK_GREY, ha='center')
        ax.plot([ring['C4'][0], ring['C4'][0]-0.6], [ring['C4'][1], ring['C4'][1]-0.6], color=NAVY, linewidth=1.2)
        ax.text(ring['C4'][0]-0.9, ring['C4'][1]-0.8, 'OH', fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
        
        # C3 substituents (OH above, H below)
        ax.plot([ring['C3'][0], ring['C3'][0]], [ring['C3'][1], ring['C3'][1]+0.7], color=NAVY, linewidth=1.2)
        ax.text(ring['C3'][0], ring['C3'][1]+0.9, 'OH', fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
        ax.plot([ring['C3'][0], ring['C3'][0]], [ring['C3'][1], ring['C3'][1]-0.7], color=NAVY, linewidth=1.2)
        ax.text(ring['C3'][0], ring['C3'][1]-1.0, 'H', fontsize=7.0, color=DARK_GREY, ha='center')
        
        # C2 substituents (H above, OH below)
        ax.plot([ring['C2'][0], ring['C2'][0]], [ring['C2'][1], ring['C2'][1]+0.7], color=NAVY, linewidth=1.2)
        ax.text(ring['C2'][0], ring['C2'][1]+0.9, 'H', fontsize=7.0, color=DARK_GREY, ha='center')
        ax.plot([ring['C2'][0], ring['C2'][0]], [ring['C2'][1], ring['C2'][1]-0.7], color=NAVY, linewidth=1.2)
        ax.text(ring['C2'][0], ring['C2'][1]-1.0, 'OH', fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
        
        # C1 substituents (Key difference: alpha OH down, beta OH up)
        if is_alpha:
            # Alpha: H above, OH below
            ax.plot([ring['C1'][0], ring['C1'][0]+0.6], [ring['C1'][1], ring['C1'][1]+0.5], color=NAVY, linewidth=1.2)
            ax.text(ring['C1'][0]+0.8, ring['C1'][1]+0.6, 'H', fontsize=7.2, color=DARK_GREY)
            ax.plot([ring['C1'][0], ring['C1'][0]+0.7], [ring['C1'][1], ring['C1'][1]-0.6], color=CRIMSON, linewidth=2.0)
            ax.text(ring['C1'][0]+1.0, ring['C1'][1]-0.8, 'OH', fontsize=8.5, fontweight='bold', color=CRIMSON)
            ax.annotate("C1 -OH group\npoints BELOW ring", xy=(ring['C1'][0]+1.0, ring['C1'][1]-0.9),
                        xytext=(ring['C1'][0]+0.4, -2.5),
                        arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                        fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
        else:
            # Beta: OH above, H below
            ax.plot([ring['C1'][0], ring['C1'][0]+0.7], [ring['C1'][1], ring['C1'][1]+0.6], color=CRIMSON, linewidth=2.0)
            ax.text(ring['C1'][0]+1.0, ring['C1'][1]+0.8, 'OH', fontsize=8.5, fontweight='bold', color=CRIMSON)
            ax.plot([ring['C1'][0], ring['C1'][0]+0.6], [ring['C1'][1], ring['C1'][1]-0.5], color=NAVY, linewidth=1.2)
            ax.text(ring['C1'][0]+0.8, ring['C1'][1]-0.7, 'H', fontsize=7.2, color=DARK_GREY)
            ax.annotate("C1 -OH group\npoints ABOVE ring", xy=(ring['C1'][0]+1.0, ring['C1'][1]+0.9),
                        xytext=(ring['C1'][0]+0.4, 2.4),
                        arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                        fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
            
        # Carbon numbering indicators
        ax.text(ring['C1'][0]-0.25, ring['C1'][1]+0.1, '1', fontsize=6.2, fontweight='bold', color=NAVY)
        ax.text(ring['C2'][0]+0.2, ring['C2'][1]+0.2, '2', fontsize=6.2, fontweight='bold', color=NAVY)
        ax.text(ring['C3'][0]-0.25, ring['C3'][1]+0.2, '3', fontsize=6.2, fontweight='bold', color=NAVY)
        ax.text(ring['C4'][0]+0.2, ring['C4'][1]+0.1, '4', fontsize=6.2, fontweight='bold', color=NAVY)
        ax.text(ring['C5'][0]-0.3, ring['C5'][1]-0.2, '5', fontsize=6.2, fontweight='bold', color=NAVY)

    draw_glucose(ax1, True, "α-glucose (alpha-glucose)")
    draw_glucose(ax2, False, "β-glucose (beta-glucose)")
    
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.3: MALTOSE CONDENSATION & HYDROLYSIS
# ==============================================================================
def generate_fig2_3(filename="fig2_3_maltose_condensation.png"):
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 65)
    ax.axis('off')
    
    ax.text(50, 61, "Condensation of two α-glucose molecules to form Maltose", fontsize=8.8,
            fontweight='bold', color=NAVY, ha='center')
    
    # Top reaction: 2 separate alpha-glucoses
    def draw_mini_ring(x_c, y_c, show_c1_oh=True, show_c4_oh=True):
        # pyranose hexagon
        coords = [(x_c-4, y_c+2), (x_c-1, y_c+4.5), (x_c+3, y_c+3.5),
                  (x_c+4.5, y_c), (x_c+2, y_c-3.5), (x_c-2.5, y_c-3.5)]
        poly = Polygon(coords, closed=True, facecolor="#f4f7fb", edgecolor=NAVY, linewidth=1.3)
        ax.add_patch(poly)
        ax.text(x_c-1, y_c+4.5, "O", fontsize=7.5, fontweight='bold', color=NAVY, ha='center', va='center',
                bbox=dict(boxstyle='circle', fc=WHITE, ec='none', pad=0.1))
        ax.text(x_c-3, y_c+6, "CH₂OH", fontsize=6.0, fontweight='bold', color=DARK_GREY)
        ax.plot([x_c-2.5, x_c-2.5], [y_c+3.5, y_c+5.5], color=NAVY, linewidth=1.0)
        
        if show_c1_oh:
            ax.plot([x_c+4.5, x_c+6.5], [y_c, y_c-2.5], color=CRIMSON, linewidth=1.6)
            ax.text(x_c+7.2, y_c-3.5, "OH (C1)", fontsize=6.8, fontweight='bold', color=CRIMSON)
            
        if show_c4_oh:
            ax.plot([x_c-4, x_c-6], [y_c+2, y_c-0.5], color=CRIMSON, linewidth=1.6)
            ax.text(x_c-9.5, y_c-1.5, "(C4) HO", fontsize=6.8, fontweight='bold', color=CRIMSON)
            
    # Reactants
    draw_mini_ring(24, 44, show_c1_oh=True, show_c4_oh=False)
    ax.text(37, 44, "+", fontsize=14, fontweight='bold', color=NAVY, ha='center')
    draw_mini_ring(52, 44, show_c1_oh=False, show_c4_oh=True)
    
    # H2O loss highlight box
    ax.add_patch(FancyBboxPatch((30, 38.5), 16, 8, boxstyle="round,pad=1,rounding_size=3",
                               facecolor="#feeceb", edgecolor=CRIMSON, linewidth=1.2, linestyle='--'))
    ax.text(38, 36, "Condensation: - H₂O", fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')
    
    # Reaction Arrow down
    ax.annotate("", xy=(38, 24), xytext=(38, 33),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.0))
    ax.text(40, 28.5, "Condensation\n(synthase)", fontsize=6.5, fontweight='bold', color=NAVY)
    
    # Reverse arrow up
    ax.annotate("", xy=(46, 33), xytext=(46, 24),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5, linestyle='--'))
    ax.text(48, 28.5, "Hydrolysis\n(+ H₂O, maltase)", fontsize=6.5, fontweight='bold', color=CRIMSON)

    # Product: Maltose
    draw_mini_ring(24, 12, show_c1_oh=False, show_c4_oh=False)
    draw_mini_ring(52, 12, show_c1_oh=False, show_c4_oh=False)
    
    # Glycosidic bond connection
    ax.plot([28.5, 38], [12, 8], color=CRIMSON, linewidth=2.0)
    ax.plot([38, 48], [8, 14], color=CRIMSON, linewidth=2.0)
    ax.text(38, 7.5, "O", fontsize=9, fontweight='bold', color=CRIMSON, ha='center', va='center',
            bbox=dict(boxstyle='circle', fc=WHITE, ec='none', pad=0.1))
    
    ax.annotate("α(1→4)-glycosidic bond", xy=(38, 7.5), xytext=(38, 1.5),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.8, fontweight='bold', color=CRIMSON, ha='center')
    
    ax.text(78, 12, "+ H₂O", fontsize=10, fontweight='bold', color=NAVY, ha='center')
    ax.text(38, 20.5, "Maltose (disaccharide)", fontsize=8.0, fontweight='bold', color=DEEP_NAVY, ha='center')
    
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.4: AMYLOSE, AMYLOPECTIN & GLYCOGEN ARCHITECTURE
# ==============================================================================
def generate_fig2_4(filename="fig2_4_amylose_amylopectin_glycogen.png"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8.2, 3.8), dpi=300)
    
    for ax in [ax1, ax2, ax3]:
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        
    # (A) Amylose
    ax1.set_title("A: Amylose (Starch)", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    # Draw helical ribbon
    t = np.linspace(0, 5*np.pi, 200)
    x_helix = 50 + 28 * np.cos(t)
    y_helix = np.linspace(80, 20, 200)
    ax1.plot(x_helix, y_helix, color="#2b75d6", linewidth=4.0, alpha=0.85)
    # Glucose monomer beads
    for i in range(0, 200, 14):
        ax1.plot(x_helix[i], y_helix[i], 'o', color=NAVY, markersize=4.5)
    ax1.text(50, 10, "• Unbranched helix\n• α(1→4) bonds only\n• Compact storage\n• Iodine fits in helix core",
             fontsize=6.8, color=DARK_GREY, ha='center')

    # (B) Amylopectin
    ax2.set_title("B: Amylopectin (Starch)", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    # Main trunk
    ax2.plot([20, 80], [35, 35], color="#2b75d6", linewidth=3.0)
    # Branches
    ax2.plot([35, 55], [35, 65], color="#2b75d6", linewidth=2.5)
    ax2.plot([60, 85], [35, 60], color="#2b75d6", linewidth=2.5)
    ax2.plot([45, 68], [50, 75], color="#2b75d6", linewidth=2.0)
    
    # Highlight branch points
    for bx, by in [(35, 35), (60, 35), (45, 50)]:
        ax2.plot(bx, by, 's', color=CRIMSON, markersize=5.5)
        
    ax2.annotate("α(1→6) branch\n(every 24-30 units)", xy=(35, 35), xytext=(20, 52),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON)
    ax2.text(50, 10, "• Branched architecture\n• α(1→4) main chains\n• α(1→6) branch points\n• Multiple terminal ends",
             fontsize=6.8, color=DARK_GREY, ha='center')

    # (C) Glycogen
    ax3.set_title("C: Glycogen (Animal Starch)", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    # Highly dendritic tree
    def draw_branch(x0, y0, length, angle, depth):
        if depth == 0: return
        rad = np.radians(angle)
        x1 = x0 + length * np.cos(rad)
        y1 = y0 + length * np.sin(rad)
        ax3.plot([x0, x1], [y0, y1], color="#1a8754", linewidth=max(1.2, depth*0.9))
        ax3.plot(x0, y0, 'o', color=CRIMSON, markersize=3.0)
        draw_branch(x1, y1, length*0.75, angle - 28, depth - 1)
        draw_branch(x1, y1, length*0.75, angle + 28, depth - 1)
        
    draw_branch(50, 25, 22, 90, 4)
    ax3.annotate("Frequent α(1→6)\nbranches (8-12 units)", xy=(50, 47), xytext=(65, 75),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON, ha='center')
    ax3.text(50, 10, "• Highly branched\n• Higher solubility\n• Rapid mobilisation\n  by glycogen phosphorylase",
             fontsize=6.8, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.5: CELLULOSE MICROFIBRIL & HYDROGEN BONDING
# ==============================================================================
def generate_fig2_5(filename="fig2_5_cellulose_microfibril.png"):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.0, 4.6), dpi=300, gridspec_kw={'height_ratios': [1.2, 1.0]})
    
    # Top: Molecular structure with 180 deg flipped beta-glucoses & H-bonds
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 50)
    ax1.axis('off')
    ax1.set_title("Molecular Structure of Cellulose: Parallel Chains & Inter-Chain Hydrogen Bonding",
                  fontsize=8.5, fontweight='bold', color=NAVY, pad=4)
    
    def draw_cellulose_chain(y_base, flipped_start=False):
        # 5 glucose units connected by beta-1,4 bonds
        xs = [12, 28, 44, 60, 76]
        for i, x in enumerate(xs):
            flipped = (i % 2 == 1) if not flipped_start else (i % 2 == 0)
            # Hexagon
            y_shift = 1.5 if flipped else -1.5
            coords = [(x-5, y_base+y_shift), (x-2, y_base+3+y_shift), (x+2, y_base+3+y_shift),
                      (x+5, y_base+y_shift), (x+2, y_base-3+y_shift), (x-2, y_base-3+y_shift)]
            ax1.add_patch(Polygon(coords, closed=True, facecolor="#eef6ec", edgecolor="#1a8754", linewidth=1.2))
            
            # Label inverted
            if flipped:
                ax1.text(x, y_base+y_shift, "180°\ninv", fontsize=5.5, color="#1a8754", ha='center', va='center')
            else:
                ax1.text(x, y_base+y_shift, "β-glu", fontsize=5.8, fontweight='bold', color=NAVY, ha='center', va='center')
                
            # Connecting beta-1,4 bond
            if i < len(xs)-1:
                next_x = xs[i+1]
                ax1.plot([x+5, (x+next_x)/2], [y_base+y_shift, y_base], color=CRIMSON, linewidth=1.5)
                ax1.plot([(x+next_x)/2, next_x-5], [y_base, y_base-(1.5 if flipped else -1.5)], color=CRIMSON, linewidth=1.5)
                ax1.text((x+next_x)/2, y_base, "O", fontsize=6.5, fontweight='bold', color=CRIMSON,
                         ha='center', va='center', bbox=dict(boxstyle='circle', fc=WHITE, ec='none', pad=0.1))
                
    draw_cellulose_chain(36, False)
    draw_cellulose_chain(14, False)
    
    # Inter-chain hydrogen bonds (vertical dashed red lines)
    for x in [12, 28, 44, 60, 76]:
        ax1.plot([x, x], [19, 31], 'r--', linewidth=1.3)
        ax1.text(x+2.2, 25, "H-bond", fontsize=5.8, color=CRIMSON)
        
    ax1.annotate("β(1→4)-glycosidic bond", xy=(36, 36), xytext=(36, 45),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')
    
    # Bottom: Microfibril assembly hierarchy
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 35)
    ax2.axis('off')
    ax2.set_title("Hierarchical Assembly of Plant Cell Wall Microfibrils", fontsize=8.0, fontweight='bold', color=DEEP_NAVY)
    
    # Individual chains -> Microfibril -> Macrofibril -> Cell wall mesh
    ax2.add_patch(FancyBboxPatch((4, 6), 20, 20, boxstyle="round,pad=1,rounding_size=3", facecolor="#eef6ec", edgecolor="#1a8754", lw=1.2))
    ax2.text(14, 19, "Individual\nβ-glucose chains", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')
    ax2.text(14, 9, "(straight, unbranched)", fontsize=5.8, color=DARK_GREY, ha='center')
    
    ax2.annotate("", xy=(30, 16), xytext=(24, 16), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
    
    ax2.add_patch(FancyBboxPatch((32, 6), 22, 20, boxstyle="round,pad=1,rounding_size=3", facecolor="#e2f0dc", edgecolor="#1a8754", lw=1.4))
    ax2.text(43, 19, "Microfibril\n(~60–70 chains)", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')
    ax2.text(43, 9, "held by 1000s of H-bonds", fontsize=5.8, color=DARK_GREY, ha='center')
    
    ax2.annotate("", xy=(60, 16), xytext=(54, 16), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
    
    ax2.add_patch(FancyBboxPatch((62, 6), 34, 20, boxstyle="round,pad=1,rounding_size=3", facecolor="#d2e8cb", edgecolor="#1a8754", lw=1.6))
    ax2.text(79, 19, "Plant Cell Wall Mesh", fontsize=7.2, fontweight='bold', color=NAVY, ha='center')
    ax2.text(79, 10, "Criss-cross laminated layers\nImparts high tensile strength", fontsize=5.8, color=DARK_GREY, ha='center')
    
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.6: TRIGLYCERIDE CONDENSATION (ESTER BONDS)
# ==============================================================================
def generate_fig2_6(filename="fig2_6_triglyceride_condensation.png"):
    fig, ax = plt.subplots(figsize=(8.2, 4.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis('off')
    
    ax.text(50, 66, "Formation of a Triglyceride Molecule by Condensation (Esterification)",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # Left: Glycerol + 3 Fatty Acids
    # Glycerol backbone
    ax.text(12, 58, "Glycerol", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')
    for idx, (y, r_label, kink) in enumerate([(48, "Saturated R₁ (straight)", False),
                                              (35, "Monounsaturated R₂ (cis kink)", True),
                                              (22, "Saturated R₃ (straight)", False)]):
        ax.text(6, y, f"H₂C—OH" if idx in [0,2] else "HC—OH", fontsize=7.2, fontweight='bold', color=DARK_GREY)
        ax.plot([14.5, 17.5], [y+0.5, y+0.5], 'r--', linewidth=1.2)
        
        # Fatty acid carboxyl + hydrocarbon tail
        ax.text(20, y, "HO—C(=O)—", fontsize=7.2, fontweight='bold', color=CRIMSON)
        # Tail
        if not kink:
            # zigzag line
            zx = np.linspace(31, 46, 7)
            zy = [y + (1.2 if j%2==0 else -1.2) for j in range(len(zx))]
            ax.plot(zx, zy, color="#2b75d6", linewidth=1.8)
        else:
            # kinked zigzag line
            zx1 = np.linspace(31, 38, 4)
            zy1 = [y + (1.2 if j%2==0 else -1.2) for j in range(len(zx1))]
            ax.plot(zx1, zy1, color="#2b75d6", linewidth=1.8)
            # kink downwards ~30 deg
            zx2 = np.linspace(38, 45, 4)
            zy2 = [y - 1.2 - (j*1.6) for j in range(len(zx2))]
            ax.plot(zx2, zy2, color="#2b75d6", linewidth=1.8)
            ax.annotate("cis double bond\ncauses ~30° kink", xy=(38, y-1.2), xytext=(38, y-7.5),
                        arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=0.9),
                        fontsize=6.0, fontweight='bold', color=CRIMSON)

    # Condensation box (- 3 H2O)
    ax.add_patch(FancyBboxPatch((13, 16), 16, 38, boxstyle="round,pad=1,rounding_size=4",
                               facecolor="#feeceb", edgecolor=CRIMSON, linewidth=1.2, linestyle='--'))
    
    # Arrow to right
    ax.annotate("", xy=(56, 35), xytext=(48, 35), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.0))
    ax.text(52, 38, "- 3 H₂O\nCondensation", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
    
    # Right: Triglyceride formed with 3 Ester bonds
    ax.text(78, 58, "Triglyceride (Triacylglycerol)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')
    for idx, (y, kink) in enumerate([(48, False), (35, True), (22, False)]):
        ax.text(62, y, "CH₂—O—" if idx in [0,2] else "CH—O—", fontsize=7.2, fontweight='bold', color=DARK_GREY)
        ax.text(71, y, "C(=O)—", fontsize=7.2, fontweight='bold', color=CRIMSON)
        # Highlight ester linkage
        ax.add_patch(Rectangle((68, y-2.5), 9, 6, facecolor="none", edgecolor=CRIMSON, linewidth=1.2))
        
        # Tail
        if not kink:
            zx = np.linspace(80, 96, 7)
            zy = [y + (1.2 if j%2==0 else -1.2) for j in range(len(zx))]
            ax.plot(zx, zy, color="#2b75d6", linewidth=1.8)
        else:
            zx1 = np.linspace(80, 87, 4)
            zy1 = [y + (1.2 if j%2==0 else -1.2) for j in range(len(zx1))]
            ax.plot(zx1, zy1, color="#2b75d6", linewidth=1.8)
            zx2 = np.linspace(87, 94, 4)
            zy2 = [y - 1.2 - (j*1.6) for j in range(len(zx2))]
            ax.plot(zx2, zy2, color="#2b75d6", linewidth=1.8)

    ax.annotate("Covalent Ester Bond\n(-COO-)", xy=(72, 48), xytext=(72, 63),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')
    
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.7: PHOSPHOLIPID MOLECULAR STRUCTURE & BILAYER
# ==============================================================================
def generate_fig2_7(filename="fig2_7_phospholipid_structure.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.2]})
    
    # Left: Single phospholipid molecule
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("Phospholipid Molecular Architecture", fontsize=8.5, fontweight='bold', color=NAVY, pad=4)
    
    # Polar Head: Choline + Phosphate
    ax1.add_patch(Circle((50, 78), 14, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.8))
    ax1.text(50, 82, "Choline", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')
    ax1.text(50, 75, "Phosphate (PO₄³⁻)", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(50, 68, "Polar / Hydrophilic Head", fontsize=6.2, color=DARK_GREY, ha='center')
    
    # Glycerol bridge
    ax1.add_patch(FancyBboxPatch((40, 52), 20, 10, boxstyle="round,pad=1,rounding_size=3",
                                 facecolor="#f9fbfd", edgecolor=DARK_GREY, lw=1.2))
    ax1.text(50, 56, "Glycerol Backbone", fontsize=6.8, fontweight='bold', color=DARK_GREY, ha='center')
    
    # Two Hydrocarbon tails
    # Saturated (straight)
    ax1.plot([44, 44], [52, 12], color="#2b75d6", linewidth=2.8)
    ax1.text(34, 25, "Saturated\nTail (straight)", fontsize=6.2, fontweight='bold', color="#2b75d6", ha='center')
    
    # Unsaturated (kinked)
    ax1.plot([56, 56], [52, 34], color="#2b75d6", linewidth=2.8)
    ax1.plot([56, 70], [34, 14], color="#2b75d6", linewidth=2.8)
    ax1.annotate("cis double bond\ncreates kink", xy=(56, 34), xytext=(72, 34),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.0, fontweight='bold', color=CRIMSON)
    ax1.text(70, 20, "Unsaturated\nTail", fontsize=6.2, fontweight='bold', color="#2b75d6", ha='center')
    ax1.text(50, 4, "Non-polar / Hydrophobic Tails", fontsize=6.8, fontweight='bold', color=DARK_GREY, ha='center')

    # Right: Bilayer arrangement in aqueous medium
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("Spontaneous Phospholipid Bilayer in Water", fontsize=8.5, fontweight='bold', color=NAVY, pad=4)
    
    # Aqueous phase top & bottom
    ax2.add_patch(Rectangle((0, 80), 100, 20, facecolor="#eef5fc", edgecolor="none", alpha=0.7))
    ax2.text(50, 88, "AQUEOUS EXTRACELLULAR FLUID (Water)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')
    
    ax2.add_patch(Rectangle((0, 0), 100, 20, facecolor="#eef5fc", edgecolor="none", alpha=0.7))
    ax2.text(50, 8, "AQUEOUS CYTOPLASM (Water)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')
    
    # Top leaflet
    for hx in np.linspace(10, 90, 8):
        ax2.add_patch(Circle((hx, 74), 4.5, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.2))
        ax2.plot([hx-1.5, hx-1.5], [69.5, 54], color="#2b75d6", linewidth=1.6)
        ax2.plot([hx+1.5, hx+3.5], [69.5, 54], color="#2b75d6", linewidth=1.6)
        
    # Bottom leaflet
    for hx in np.linspace(10, 90, 8):
        ax2.add_patch(Circle((hx, 26), 4.5, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.2))
        ax2.plot([hx-1.5, hx-1.5], [30.5, 46], color="#2b75d6", linewidth=1.6)
        ax2.plot([hx+1.5, hx+3.5], [30.5, 46], color="#2b75d6", linewidth=1.6)
        
    ax2.annotate("Hydrophilic heads face water", xy=(50, 74), xytext=(50, 62),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=NAVY, ha='center')
    
    ax2.text(50, 50, "HYDROPHOBIC CORE\n(Fatty acid tails excluded from water)",
             fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.8: AMINO ACID GENERAL STRUCTURE & PEPTIDE BOND
# ==============================================================================
def generate_fig2_8(filename="fig2_8_amino_acid_peptide_bond.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=300, gridspec_kw={'width_ratios': [1.0, 1.4]})
    
    # Left: Generalized amino acid
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.axis('off')
    ax1.set_title("General Structure of an Amino Acid", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Central alpha-carbon
    ax1.text(0, 0, "C_α", fontsize=11, fontweight='bold', color=NAVY, ha='center', va='center')
    
    # Amine group left
    ax1.plot([-0.6, -1.6], [0, 0], color=NAVY, linewidth=1.5)
    ax1.text(-2.3, 0, "H₂N—", fontsize=9.5, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax1.text(-2.3, 1.0, "Amine\ngroup", fontsize=6.5, color=DARK_GREY, ha='center')
    
    # Carboxyl group right
    ax1.plot([0.6, 1.5], [0, 0], color=NAVY, linewidth=1.5)
    ax1.text(2.2, 0, "—COOH", fontsize=9.5, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax1.text(2.2, 1.0, "Carboxylic\nacid group", fontsize=6.5, color=DARK_GREY, ha='center')
    
    # Hydrogen top
    ax1.plot([0, 0], [0.5, 1.5], color=NAVY, linewidth=1.5)
    ax1.text(0, 1.9, "H", fontsize=10, fontweight='bold', color=DARK_GREY, ha='center', va='center')
    
    # Variable R-group bottom
    ax1.plot([0, 0], [-0.5, -1.4], color=NAVY, linewidth=2.0)
    ax1.add_patch(FancyBboxPatch((-0.8, -2.4), 1.6, 0.9, boxstyle="round,pad=0.2", facecolor="#fff2df", edgecolor="#d97706", lw=1.2))
    ax1.text(0, -2.0, "R", fontsize=11, fontweight='bold', color="#d97706", ha='center', va='center')
    ax1.text(0, -2.7, "Variable side-chain", fontsize=6.2, color=DARK_GREY, ha='center')

    # Right: Peptide bond condensation
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 60)
    ax2.axis('off')
    ax2.set_title("Formation of a Dipeptide (Peptide Bond Condensation)", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Top reactants
    ax2.text(18, 48, "Amino Acid 1\n...—C(=O)—OH", fontsize=7.2, fontweight='bold', color=NAVY, ha='center')
    ax2.text(48, 48, "Amino Acid 2\nH—N(H)—C_α...", fontsize=7.2, fontweight='bold', color=NAVY, ha='center')
    
    # Condensation dashed box
    ax2.add_patch(FancyBboxPatch((28, 40), 16, 14, boxstyle="round,pad=0.5", facecolor="#feeceb", edgecolor=CRIMSON, lw=1.2, linestyle='--'))
    ax2.text(36, 44, "- H₂O\nCondensation", fontsize=6.2, fontweight='bold', color=CRIMSON, ha='center')
    
    # Down arrow
    ax2.annotate("", xy=(36, 26), xytext=(36, 36), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.8))
    
    # Dipeptide product
    ax2.text(10, 16, "H₂N—CH(R₁)—", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.text(40, 16, "C(=O)—NH", fontsize=8.5, fontweight='bold', color=CRIMSON)
    ax2.text(68, 16, "—CH(R₂)—COOH", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.text(92, 16, "+ H₂O", fontsize=8.5, fontweight='bold', color=NAVY)
    
    # Highlight peptide bond
    ax2.add_patch(FancyBboxPatch((38, 10), 24, 12, boxstyle="round,pad=0.5", facecolor="none", edgecolor=CRIMSON, lw=1.5))
    ax2.annotate("Covalent Peptide Bond\n(-CO-NH-)", xy=(50, 10), xytext=(50, 2),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                 fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.9: PROTEIN TERTIARY STRUCTURE INTERACTIONS
# ==============================================================================
def generate_fig2_9(filename="fig2_9_protein_tertiary_interactions.png"):
    fig, ax = plt.subplots(figsize=(7.8, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 96, "Four Stabilising R-Group Interactions in Protein Tertiary Structure",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # Folded polypeptide backbone ribbon
    t = np.linspace(0, 2.5*np.pi, 300)
    x_backbone = 50 + 38 * np.sin(t) * np.cos(t*0.5)
    y_backbone = 48 + 36 * np.cos(t)
    ax.plot(x_backbone, y_backbone, color="#b0c4de", linewidth=6.5, alpha=0.6, zorder=1)
    ax.plot(x_backbone, y_backbone, color=NAVY, linewidth=1.5, zorder=2)
    
    # N-terminus and C-terminus
    ax.text(x_backbone[0]-4, y_backbone[0], "N-term", fontsize=7.0, fontweight='bold', color=NAVY)
    ax.text(x_backbone[-1]+4, y_backbone[-1], "C-term", fontsize=7.0, fontweight='bold', color=NAVY)
    
    # Interaction 1: Disulfide bridge
    ax.plot([32, 42], [74, 74], color=CRIMSON, linewidth=2.4, zorder=3)
    ax.plot(32, 74, 'o', color="#e6a100", markersize=6)
    ax.plot(42, 74, 'o', color="#e6a100", markersize=6)
    ax.annotate("1. Disulfide Bridge (Covalent)\n-CH₂-S-S-CH₂- (between Cysteine R-groups)\nStrongest bond, broken only by reducing agents",
                xy=(37, 74), xytext=(12, 88),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=6.5, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    # Interaction 2: Ionic Bond / Salt Bridge
    ax.plot([60, 72], [72, 72], 'k--', linewidth=1.8, zorder=3)
    ax.text(58, 72, "—NH₃⁺", fontsize=7.5, fontweight='bold', color="#2b75d6", ha='right', va='center')
    ax.text(74, 72, "—COO⁻", fontsize=7.5, fontweight='bold', color=CRIMSON, ha='left', va='center')
    ax.annotate("2. Ionic Bond / Salt Bridge\nElectrostatic attraction between -NH₃⁺ (Lys)\nand -COO⁻ (Asp/Glu); sensitive to pH shifts",
                xy=(66, 72), xytext=(68, 86),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                fontsize=6.5, fontweight='bold', color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", fc="#f0f4fa", ec=NAVY, lw=0.8))

    # Interaction 3: Hydrogen Bond
    ax.plot([28, 28], [35, 48], 'r:', linewidth=2.0, zorder=3)
    ax.text(28, 49, "—OH", fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
    ax.text(28, 33, "O=C—", fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
    ax.annotate("3. Hydrogen Bond\nBetween polar R-groups (e.g. Ser -OH)\nand carbonyl oxygens; broken by heat",
                xy=(28, 41), xytext=(6, 26),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2),
                fontsize=6.5, fontweight='bold', color=DARK_GREY,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fbfbfc", ec=DARK_GREY, lw=0.8))

    # Interaction 4: Hydrophobic Interactions
    ax.add_patch(FancyBboxPatch((46, 32), 18, 16, boxstyle="round,pad=1,rounding_size=5",
                               facecolor="#fff7ed", edgecolor="#ea580c", lw=1.4, zorder=2))
    ax.text(55, 41, "-CH(CH₃)₂\nVal / Leu", fontsize=6.2, fontweight='bold', color="#ea580c", ha='center')
    ax.text(55, 34, "(non-polar core)", fontsize=5.8, color=DARK_GREY, ha='center')
    ax.annotate("4. Hydrophobic Interactions\nNon-polar R-groups cluster together in\nthe protein interior away from aqueous solvent",
                xy=(55, 32), xytext=(55, 12),
                arrowprops=dict(arrowstyle="->", color="#ea580c", lw=1.2),
                fontsize=6.5, fontweight='bold', color="#ea580c", ha='center',
                bbox=dict(boxstyle="round,pad=0.3", fc="#fff7ed", ec="#ea580c", lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.10: HAEMOGLOBIN QUATERNARY STRUCTURE
# ==============================================================================
def generate_fig2_10(filename="fig2_10_haemoglobin_quaternary.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 96, "Quaternary Structure of Adult Haemoglobin (HbA: α₂β₂)",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # 4 Subunits: α1, α2, β1, β2
    subunits = [
        ("α₁ globin chain\n(141 amino acids)", 32, 68, "#e8f0fe", "#2b75d6"),
        ("β₁ globin chain\n(146 amino acids)", 68, 68, "#fce8e6", CRIMSON),
        ("β₂ globin chain\n(146 amino acids)", 32, 32, "#fce8e6", CRIMSON),
        ("α₂ globin chain\n(141 amino acids)", 68, 32, "#e8f0fe", "#2b75d6"),
    ]
    
    for label, cx, cy, fc, ec in subunits:
        ax.add_patch(FancyBboxPatch((cx-16, cy-14), 32, 28, boxstyle="round,pad=2,rounding_size=10",
                                     facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.9))
        ax.text(cx, cy+7, label, fontsize=7.2, fontweight='bold', color=ec, ha='center')
        
        # Prosthetic Haem Group
        ax.add_patch(FancyBboxPatch((cx-6, cy-10), 12, 12, boxstyle="round,pad=1,rounding_size=3",
                                     facecolor="#ffdedb", edgecolor=CRIMSON, linewidth=1.4))
        # Fe2+ ion
        ax.add_patch(Circle((cx, cy-4), 3.5, facecolor="#b52b27", edgecolor=NAVY, linewidth=1.0))
        ax.text(cx, cy-4, "Fe²⁺", fontsize=6.5, fontweight='bold', color=WHITE, ha='center', va='center')
        
    # Annotations
    ax.annotate("Prosthetic Haem Group\nPorphyrin ring with Fe²⁺\nBinds 1 O₂ molecule reversibly",
                xy=(32, 64), xytext=(2, 85),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=6.5, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    ax.annotate("Hydrophilic R-groups on outside\n(confers high water solubility)",
                xy=(50, 78), xytext=(50, 88),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                fontsize=6.8, fontweight='bold', color=NAVY, ha='center',
                bbox=dict(boxstyle="round,pad=0.3", fc="#f0f4fa", ec=NAVY, lw=0.8))

    ax.text(50, 50, "Total Capacity:\n4 Haem groups = 4 O₂ molecules\n(8 Oxygen atoms)",
            fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.4", fc=WHITE, ec=DARK_GREY, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.11: COLLAGEN TRIPLE HELIX & FIBRE FORMATION
# ==============================================================================
def generate_fig2_11(filename="fig2_11_collagen_triple_helix.png"):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.0, 4.8), dpi=300, gridspec_kw={'height_ratios': [1.1, 1.2]})
    
    # Top: Triple Helix (Tropocollagen)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 45)
    ax1.axis('off')
    ax1.set_title("Tropocollagen: Right-Handed Triple Helix of Three Left-Handed α-Chains",
                  fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    t = np.linspace(0, 6*np.pi, 300)
    x = np.linspace(10, 90, 300)
    y1 = 22 + 5 * np.sin(t)
    y2 = 22 + 5 * np.sin(t + 2*np.pi/3)
    y3 = 22 + 5 * np.sin(t + 4*np.pi/3)
    
    ax1.plot(x, y1, color="#2b75d6", linewidth=2.0, label='Chain 1')
    ax1.plot(x, y2, color=CRIMSON, linewidth=2.0, label='Chain 2')
    ax1.plot(x, y3, color="#1a8754", linewidth=2.0, label='Chain 3')
    
    ax1.annotate("Repeating Gly-X-Y triplet\nGlycine (-H R-group) is smallest\nFits into tight central axis",
                xy=(32, 22), xytext=(12, 36),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, fontweight='bold', color=NAVY)
    
    ax1.annotate("Tight H-bonding between\nadjacent chains holds helix",
                xy=(68, 22), xytext=(68, 36),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    # Bottom: Staggered Tropocollagen Assembly with Covalent Cross-links
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 50)
    ax2.axis('off')
    ax2.set_title("Staggered Arrangement of Tropocollagen Forming Collagen Fibril", fontsize=8.0, fontweight='bold', color=DEEP_NAVY)
    
    # Rows of staggered molecules
    stagger_rows = [
        [(10, 40), (45, 75), (80, 100)],
        [(20, 50), (55, 85)],
        [(10, 30), (35, 65), (70, 100)],
        [(25, 55), (60, 90)]
    ]
    
    y_coords = [38, 28, 18, 8]
    for r_idx, intervals in enumerate(stagger_rows):
        y = y_coords[r_idx]
        for start_x, end_x in intervals:
            ax2.plot([start_x, end_x], [y, y], color="#405270", linewidth=3.2)
            
    # Covalent cross links between staggered molecules
    cross_links = [(35, 38, 28), (48, 28, 18), (62, 18, 8), (42, 18, 8)]
    for cx, y_top, y_bot in cross_links:
        ax2.plot([cx, cx], [y_top, y_bot], color=CRIMSON, linewidth=2.0, linestyle='-')
        ax2.plot(cx, (y_top+y_bot)/2, 's', color=CRIMSON, markersize=4)

    ax2.annotate("Covalent Cross-links (Lysine)\nprevent slippage under tension",
                 xy=(48, 23), xytext=(58, 28),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax2.annotate("Staggered arrangement (~67 nm gap/overlap)\navoids line of weakness along fibril",
                 xy=(30, 38), xytext=(5, 46),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=NAVY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.12: WATER MOLECULE DIPOLE & HYDRATION SHELL
# ==============================================================================
def generate_fig2_12(filename="fig2_12_water_dipole_hbonding.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.3]})
    
    # Left: Dipolar Water Molecule & Hydrogen Bonding Network
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("Water Dipole & Hydrogen Bonding", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Central water
    ax1.add_patch(Circle((50, 58), 12, facecolor="#feeceb", edgecolor=CRIMSON, linewidth=1.8))
    ax1.text(50, 60, "O", fontsize=11, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax1.text(50, 50, "δ²⁻", fontsize=8.5, fontweight='bold', color=CRIMSON, ha='center')
    
    # Two Hydrogens
    ax1.plot([43, 34], [66, 76], color=NAVY, linewidth=2.2)
    ax1.add_patch(Circle((32, 78), 7, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.4))
    ax1.text(32, 78, "H (δ⁺)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')
    
    ax1.plot([57, 66], [66, 76], color=NAVY, linewidth=2.2)
    ax1.add_patch(Circle((68, 78), 7, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.4))
    ax1.text(68, 78, "H (δ⁺)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')
    
    ax1.text(50, 72, "104.5°", fontsize=6.8, color=DARK_GREY, ha='center')
    
    # Neighbour water molecule forming H-bond
    ax1.plot([50, 50], [46, 26], 'r--', linewidth=2.0)
    ax1.annotate("Hydrogen Bond\n(electrostatic attraction\nδ⁺ H ··· δ⁻ O)", xy=(50, 36), xytext=(68, 36),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON)
    
    ax1.add_patch(Circle((50, 18), 7, facecolor="#e8f0fe", edgecolor=NAVY, linewidth=1.4))
    ax1.text(50, 18, "H (δ⁺)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # Right: Hydration Shells around Na+ and Cl-
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("Solvent Action: Hydration Shells (Solvation)", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Na+ cation
    ax2.add_patch(Circle((30, 50), 10, facecolor="#e6f4ea", edgecolor="#1a8754", linewidth=1.8))
    ax2.text(30, 50, "Na⁺", fontsize=10, fontweight='bold', color="#1a8754", ha='center', va='center')
    # Water oxygens pointing inward towards Na+
    for angle in [0, 90, 180, 270]:
        rad = np.radians(angle)
        wx = 30 + 19 * np.cos(rad)
        wy = 50 + 19 * np.sin(rad)
        ax2.add_patch(Circle((wx, wy), 4.2, facecolor="#feeceb", edgecolor=CRIMSON, lw=1.0))
        ax2.text(wx, wy, "δ⁻", fontsize=6.0, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax2.text(30, 22, "Na⁺ (cation)\nδ⁻ Oxygens orient inward", fontsize=6.5, fontweight='bold', color=DARK_GREY, ha='center')

    # Cl- anion
    ax2.add_patch(Circle((75, 50), 12, facecolor="#feeceb", edgecolor=CRIMSON, linewidth=1.8))
    ax2.text(75, 50, "Cl⁻", fontsize=10, fontweight='bold', color=CRIMSON, ha='center', va='center')
    # Water hydrogens pointing inward towards Cl-
    for angle in [45, 135, 225, 315]:
        rad = np.radians(angle)
        wx = 75 + 21 * np.cos(rad)
        wy = 50 + 21 * np.sin(rad)
        ax2.add_patch(Circle((wx, wy), 4.2, facecolor="#e8f0fe", edgecolor=NAVY, lw=1.0))
        ax2.text(wx, wy, "δ⁺", fontsize=6.0, fontweight='bold', color=NAVY, ha='center', va='center')
    ax2.text(75, 22, "Cl⁻ (anion)\nδ⁺ Hydrogens orient inward", fontsize=6.5, fontweight='bold', color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.13: BIOCHEMICAL TESTING DIAGNOSTIC FLOWCHART
# ==============================================================================
def generate_fig2_13(filename="fig2_13_biochemical_testing_flowchart.png"):
    fig, ax = plt.subplots(figsize=(8.2, 5.0), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 96, "Diagnostic Protocol for Biological Molecules Testing",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    tests = [
        ("Starch Test", "Add Iodine in KI solution", "Yellow-brown → Blue-Black", 12, "#1a8754"),
        ("Reducing Sugar", "Add Benedict's reagent,\nheat 80–100°C for 5 min", "Blue → Green → Yellow →\nOrange → Brick-Red ppt", 31, "#2b75d6"),
        ("Non-Reducing Sugar", "1. Boil with dilute HCl\n2. Cool & neutralise with NaHCO₃\n3. Re-test with Benedict's", "Second test: Blue → Brick-Red\n(Hydrolysis into α-glu + β-fru)", 50, "#854d0e"),
        ("Emulsion Test (Lipids)", "1. Dissolve sample in ethanol\n2. Decant into water", "Clear → Cloudy / Milky-white\nemulsion of lipid droplets", 69, "#9333ea"),
        ("Biuret Test (Proteins)", "Add dilute NaOH, then\n1% CuSO₄ solution", "Blue → Purple / Lilac colour\n(Cu²⁺ complexes with peptide bonds)", 88, CRIMSON),
    ]
    
    for title, method, result, x, col in tests:
        # Title box
        ax.add_patch(FancyBboxPatch((x-8, 72), 16, 16, boxstyle="round,pad=1,rounding_size=3",
                                     facecolor="#f8fafc", edgecolor=col, linewidth=1.6))
        ax.text(x, 80, title, fontsize=7.2, fontweight='bold', color=col, ha='center', va='center')
        
        # Arrow down
        ax.annotate("", xy=(x, 58), xytext=(x, 70), arrowprops=dict(arrowstyle="->", color=col, lw=1.4))
        
        # Method box
        ax.add_patch(FancyBboxPatch((x-8.5, 36), 17, 21, boxstyle="round,pad=1,rounding_size=3",
                                     facecolor="#ffffff", edgecolor=DARK_GREY, linewidth=1.0))
        ax.text(x, 46.5, method, fontsize=5.8, color=DARK_GREY, ha='center', va='center')
        
        # Arrow down
        ax.annotate("", xy=(x, 24), xytext=(x, 34), arrowprops=dict(arrowstyle="->", color=col, lw=1.4))
        
        # Positive Result box
        ax.add_patch(FancyBboxPatch((x-8.5, 4), 17, 19, boxstyle="round,pad=1,rounding_size=3",
                                     facecolor="#fef2f2" if col==CRIMSON else "#f0fdf4", edgecolor=col, linewidth=1.4))
        ax.text(x, 13.5, result, fontsize=5.6, fontweight='bold', color=col, ha='center', va='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 2.14: SUCROSE CONDENSATION & NON-REDUCING PROPERTY
# ==============================================================================
def generate_fig2_14(filename="fig2_14_sucrose_condensation.png"):
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 65)
    ax.axis('off')
    
    ax.text(50, 61, "Condensation of α-Glucose and β-Fructose Forming Sucrose",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # Left: alpha-glucose ring
    coords_glu = [(16, 46), (19, 49), (24, 48), (26, 44), (23, 40), (18, 40)]
    ax.add_patch(Polygon(coords_glu, closed=True, facecolor="#f4f7fb", edgecolor=NAVY, linewidth=1.3))
    ax.text(21, 44, "α-glucose", fontsize=6.8, fontweight='bold', color=NAVY, ha='center', va='center')
    ax.text(26.5, 43, "C1-OH", fontsize=6.5, fontweight='bold', color=CRIMSON)
    
    ax.text(35, 44, "+", fontsize=14, fontweight='bold', color=NAVY, ha='center')
    
    # Fructose furanose 5-membered ring
    coords_fru = [(44, 46), (48, 49), (52, 46), (51, 41), (45, 41)]
    ax.add_patch(Polygon(coords_fru, closed=True, facecolor="#fef8ee", edgecolor="#d97706", linewidth=1.3))
    ax.text(48, 44, "β-fructose", fontsize=6.8, fontweight='bold', color="#d97706", ha='center', va='center')
    ax.text(42, 43, "HO-C2", fontsize=6.5, fontweight='bold', color=CRIMSON, ha='right')
    
    # Condensation box (- H2O)
    ax.add_patch(FancyBboxPatch((28, 38), 14, 10, boxstyle="round,pad=1,rounding_size=3",
                               facecolor="#feeceb", edgecolor=CRIMSON, lw=1.2, linestyle='--'))
    ax.text(35, 40, "Condensation\n(- H₂O)", fontsize=6.0, fontweight='bold', color=CRIMSON, ha='center')

    # Arrow down
    ax.annotate("", xy=(35, 25), xytext=(35, 34), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.8))
    
    # Sucrose disaccharide
    ax.add_patch(Polygon([(16, 16), (19, 19), (24, 18), (26, 14), (23, 10), (18, 10)],
                         closed=True, facecolor="#f4f7fb", edgecolor=NAVY, linewidth=1.3))
    ax.add_patch(Polygon([(44, 16), (48, 19), (52, 16), (51, 11), (45, 11)],
                         closed=True, facecolor="#fef8ee", edgecolor="#d97706", linewidth=1.3))
    
    # Glycosidic bond connecting C1 of glucose and C2 of fructose
    ax.plot([26, 35], [14, 11], color=CRIMSON, linewidth=2.0)
    ax.plot([35, 44], [11, 14], color=CRIMSON, linewidth=2.0)
    ax.text(35, 10.5, "O", fontsize=8.5, fontweight='bold', color=CRIMSON, ha='center', va='center',
            bbox=dict(boxstyle='circle', fc=WHITE, ec='none', pad=0.1))
    
    ax.annotate("α(1↔2)β-glycosidic bond", xy=(35, 10.5), xytext=(35, 3),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')
    
    # Right panel: explanation of non-reducing property
    ax.add_patch(FancyBboxPatch((60, 8), 36, 46, boxstyle="round,pad=1,rounding_size=4",
                                 facecolor="#f8fafc", edgecolor=NAVY, linewidth=1.4))
    ax.text(78, 48, "Why is Sucrose Non-Reducing?", fontsize=7.2, fontweight='bold', color=NAVY, ha='center')
    
    exp_text = (
        "1. In reducing sugars (glucose, maltose),\n"
        "   the anomeric carbon (C1) possesses a free\n"
        "   hemiacetal group that can open into an\n"
        "   active aldehyde (-CHO) group.\n\n"
        "2. In sucrose, the bond forms between C1 of\n"
        "   glucose AND C2 of fructose.\n\n"
        "3. Both reducing (anomeric) carbons are\n"
        "   locked in the glycosidic bond.\n\n"
        "4. No free carbonyl group is available to donate\n"
        "   electrons and reduce Cu²⁺ to Cu⁺.\n\n"
        "5. Acid hydrolysis cleaves the bond,\n"
        "   yielding free α-glucose and β-fructose."
    )
    ax.text(62, 27, exp_text, fontsize=5.8, color=DARK_GREY, va='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

def main():
    print("Generating all 14 Biological Diagrams for Topic 2...")
    generate_fig2_1()
    generate_fig2_2()
    generate_fig2_3()
    generate_fig2_4()
    generate_fig2_5()
    generate_fig2_6()
    generate_fig2_7()
    generate_fig2_8()
    generate_fig2_9()
    generate_fig2_10()
    generate_fig2_11()
    generate_fig2_12()
    generate_fig2_13()
    generate_fig2_14()
    print("All 14 diagrams successfully generated!")

if __name__ == "__main__":
    main()
