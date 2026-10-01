"""
Cambridge International AS Level Biology (9700)
Topic 4: Cell Membranes and Transport — High-Precision Publication-Quality Diagram Generator
Enlarged High-Legibility Edition: Boosted font sizes and line weights for crystal-clear printing.

Generates 14 high-resolution 300 DPI figures for Topic 4:
1.  fig4_1_fluid_mosaic_membrane.png
2.  fig4_2_cholesterol_fluidity.png
3.  fig4_3_cell_signalling_pathway.png
4.  fig4_4_simple_vs_facilitated_diffusion.png
5.  fig4_5_diffusion_kinetics_curve.png
6.  fig4_6_active_transport_nak_pump.png
7.  fig4_7_osmosis_plant_cells_plasmolysis.png
8.  fig4_8_osmosis_erythrocytes.png
9.  fig4_9_water_potential_calibration_curve.png
10. fig4_10_agar_cubes_sa_vol_ratio.png
11. fig4_11_visking_tubing_osmometer.png
12. fig4_12_endocytosis_and_exocytosis.png
13. fig4_13_beetroot_membrane_permeability.png
14. fig4_14_membrane_transport_decision_tree.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Rectangle, Polygon, PathPatch
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
TEAL = "#0d7685"
AMBER = "#d97706"
GREEN = "#15803d"
PURPLE = "#6b21a8"

# ==============================================================================
# FIG 4.1: FLUID MOSAIC MEMBRANE MODEL (ENLARGED HIGH-LEGIBILITY)
# ==============================================================================
def generate_fig4_1(filename="fig4_1_fluid_mosaic_membrane.png"):
    fig, ax = plt.subplots(figsize=(8.8, 5.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Fluid Mosaic Model of the Cell Surface Membrane (Cross-Section)",
            fontsize=11.0, fontweight='bold', color=NAVY, ha='center')

    # Background extracellular vs intracellular labels
    ax.text(4, 90, "EXTRACELLULAR FLUID (Aqueous)", fontsize=8.8, fontweight='bold', color=TEAL)
    ax.text(4, 8, "CYTOPLASM (Aqueous)", fontsize=8.8, fontweight='bold', color=DEEP_NAVY)

    # Membrane bilayer limits: Top heads y=64 to 68, bottom heads y=32 to 36
    # Hydrophobic core y=36 to 64
    x_positions = [x for x in range(6, 96, 3) if not (28 <= x <= 42 or 56 <= x <= 70)]

    for x in x_positions:
        # Upper monolayer
        ax.add_patch(Circle((x, 66), 1.3, facecolor="#60a5fa", edgecolor=NAVY, lw=0.7))
        ax.plot([x - 0.4, x - 0.6, x - 0.2, x - 0.4], [64.7, 60, 56, 52], color="#f59e0b", lw=1.1)
        ax.plot([x + 0.4, x + 0.6, x + 0.2, x + 0.4], [64.7, 60, 56, 52], color="#f59e0b", lw=1.1)

        # Lower monolayer
        ax.add_patch(Circle((x, 34), 1.3, facecolor="#60a5fa", edgecolor=NAVY, lw=0.7))
        ax.plot([x - 0.4, x - 0.6, x - 0.2, x - 0.4], [35.3, 40, 44, 48], color="#f59e0b", lw=1.1)
        ax.plot([x + 0.4, x + 0.6, x + 0.2, x + 0.4], [35.3, 40, 44, 48], color="#f59e0b", lw=1.1)

    # Integral Channel Protein (Transmembrane pore) at x=28..42
    p1 = FancyBboxPatch((28, 30), 5.5, 40, boxstyle="round,pad=0.5,rounding_size=2",
                         facecolor="#93c5fd", edgecolor=NAVY, lw=1.4)
    ax.add_patch(p1)
    p2 = FancyBboxPatch((36.5, 30), 5.5, 40, boxstyle="round,pad=0.5,rounding_size=2",
                         facecolor="#93c5fd", edgecolor=NAVY, lw=1.4)
    ax.add_patch(p2)
    ax.plot([34.5, 34.5], [30, 70], color="#2563eb", lw=1.3, linestyle="--")
    ax.text(35, 50, "Aqueous\nPore", fontsize=7.8, fontweight='bold', color="#1e3a8a", ha='center', va='center')

    # Integral Carrier Protein at x=56..70
    carrier = FancyBboxPatch((56, 30), 14, 40, boxstyle="round,pad=0.8,rounding_size=3",
                             facecolor="#c4b5fd", edgecolor=PURPLE, lw=1.4)
    ax.add_patch(carrier)
    cleft = Polygon([(60, 70), (63, 54), (67, 54), (70, 70)], closed=True, facecolor=WHITE, edgecolor=PURPLE, lw=1.2)
    ax.add_patch(cleft)
    ax.text(63, 40, "Carrier\nProtein", fontsize=8.0, fontweight='bold', color=PURPLE, ha='center')

    # Peripheral Protein on intracellular side at x=78..88, y=24..32
    periph = FancyBboxPatch((78, 22), 11, 9.5, boxstyle="round,pad=0.5,rounding_size=2",
                            facecolor="#fed7aa", edgecolor=AMBER, lw=1.3)
    ax.add_patch(periph)
    ax.text(83.5, 26.5, "Peripheral\nProtein", fontsize=7.6, fontweight='bold', color="#9a3412", ha='center')

    # Cholesterol molecules embedded between fatty acid tails
    for cx, cy in [(17.5, 52), (49, 46), (74.5, 52)]:
        chol = FancyBboxPatch((cx, cy), 2.4, 10.5, boxstyle="round,pad=0.2,rounding_size=1",
                              facecolor="#fef08a", edgecolor="#ca8a04", lw=1.2)
        ax.add_patch(chol)

    # Glycoprotein: carbohydrate chain attached to carrier protein at x=67, y=70
    sugar_nodes = [(67, 74), (69, 79), (67, 85), (73, 81), (71, 87)]
    for sx, sy in sugar_nodes:
        ax.add_patch(Polygon([(sx-1.1, sy-0.9), (sx, sy-1.4), (sx+1.1, sy-0.9),
                              (sx+1.1, sy+0.9), (sx, sy+1.4), (sx-1.1, sy+0.9)],
                             facecolor="#86efac", edgecolor=GREEN, lw=1.0))
    ax.plot([67, 67, 69, 67], [70, 74, 79, 85], color=GREEN, lw=1.4)
    ax.plot([69, 73, 71], [79, 81, 87], color=GREEN, lw=1.4)

    # Glycolipid: carbohydrate chain attached to phospholipid head at x=12, y=67
    glyco_nodes = [(12, 73), (11, 78), (14, 82)]
    for gx, gy in glyco_nodes:
        ax.add_patch(Polygon([(gx-1.0, gy-0.8), (gx, gy-1.3), (gx+1.0, gy-0.8),
                              (gx+1.0, gy+0.8), (gx, gy+1.3), (gx-1.0, gy+0.8)],
                             facecolor="#fbcfe8", edgecolor=CRIMSON, lw=1.0))
    ax.plot([12, 12, 11, 14], [67, 73, 78, 82], color=CRIMSON, lw=1.4)

    # Enlarged, High-Contrast Annotations with Non-Overlapping Spacing
    ax.annotate("Hydrophilic Phosphate Head\n(Polar / charged)", xy=(8, 67), xytext=(2, 74),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                fontsize=7.8, fontweight='bold', color=NAVY)

    ax.annotate("Hydrophobic Core\n(Fatty acid tails)", xy=(14, 48), xytext=(2, 42),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2),
                fontsize=7.8, fontweight='bold', color=DARK_GREY)

    ax.annotate("Cholesterol\n(Fluidity regulator)", xy=(18.5, 53), xytext=(22, 20),
                arrowprops=dict(arrowstyle="->", color="#854d0e", lw=1.2),
                fontsize=7.8, fontweight='bold', color="#854d0e")

    ax.annotate("Glycolipid\n(Cell recognition)", xy=(12, 80), xytext=(23, 83),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.8, fontweight='bold', color=CRIMSON)

    ax.annotate("Channel Protein\n(Aqueous pore for ions)", xy=(35, 71), xytext=(43, 87),
                arrowprops=dict(arrowstyle="->", color="#1e40af", lw=1.2),
                fontsize=7.8, fontweight='bold', color="#1e40af")

    ax.annotate("Glycoprotein\n(Receptor site / adhesion)", xy=(70, 84), xytext=(78, 87),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2),
                fontsize=7.8, fontweight='bold', color=GREEN)

    # Membrane thickness bracket (~7 nm)
    ax.plot([95, 95], [33, 67], color=DARK_GREY, lw=1.4)
    ax.plot([93.5, 96.5], [33, 33], color=DARK_GREY, lw=1.4)
    ax.plot([93.5, 96.5], [67, 67], color=DARK_GREY, lw=1.4)
    ax.text(96.5, 50, "~7 nm\nthickness", fontsize=7.6, fontweight='bold', color=DARK_GREY, va='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.2: CHOLESTEROL & MEMBRANE FLUIDITY (ENLARGED)
# ==============================================================================
def generate_fig4_2(filename="fig4_2_cholesterol_fluidity.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 4.4), dpi=300)

    # Left: High Temperature condition
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: High Temperature Condition (>37°C)", fontsize=9.6, fontweight='bold', color=CRIMSON, pad=6)

    for x in [15, 32, 50, 68, 85]:
        ax1.add_patch(Circle((x, 75), 3.0, facecolor="#93c5fd", edgecolor=NAVY, lw=1.1))
        ax1.plot([x - 1.0, x - 2.0, x - 0.5, x - 1.8], [72, 60, 50, 40], color="#f59e0b", lw=1.4)
        ax1.plot([x + 1.0, x + 2.2, x + 0.8, x + 2.0], [72, 60, 50, 40], color="#f59e0b", lw=1.4)

    c1 = FancyBboxPatch((40, 45), 4.5, 18, boxstyle="round,pad=0.3", facecolor="#fef08a", edgecolor="#ca8a04", lw=1.3)
    ax1.add_patch(c1)
    ax1.text(42.2, 54, "Cholesterol", fontsize=7.6, fontweight='bold', color="#854d0e", rotation=90, va='center', ha='center')

    ax1.annotate("Restrains fatty acid movement\n• Prevents excessive membrane fluidity\n• Preserves mechanical stability & reduces leakage",
                 xy=(42, 43), xytext=(50, 18),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                 fontsize=7.8, color=DARK_GREY, ha='center',
                 bbox=dict(boxstyle="round,pad=0.4", facecolor="#fef2f2", edgecolor=CRIMSON, lw=0.9))

    # Right: Low Temperature condition
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Low Temperature Condition (<10°C)", fontsize=9.6, fontweight='bold', color=TEAL, pad=6)

    for x in [18, 32, 50, 68, 82]:
        ax2.add_patch(Circle((x, 75), 3.0, facecolor="#93c5fd", edgecolor=NAVY, lw=1.1))
        ax2.plot([x - 0.8, x - 0.8, x - 0.8, x - 0.8], [72, 60, 50, 40], color="#f59e0b", lw=1.4)
        ax2.plot([x + 0.8, x + 0.8, x + 0.8, x + 0.8], [72, 60, 50, 40], color="#f59e0b", lw=1.4)

    c2 = FancyBboxPatch((40, 45), 4.5, 18, boxstyle="round,pad=0.3", facecolor="#fef08a", edgecolor="#ca8a04", lw=1.3)
    ax2.add_patch(c2)
    ax2.text(42.2, 54, "Cholesterol", fontsize=7.6, fontweight='bold', color="#854d0e", rotation=90, va='center', ha='center')

    ax2.annotate("Prevents close packing of fatty acid tails\n• Hinders hydrophobic crystallisation\n• Maintains fluidity in cold conditions",
                 xy=(42, 43), xytext=(50, 18),
                 arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2),
                 fontsize=7.8, color=DARK_GREY, ha='center',
                 bbox=dict(boxstyle="round,pad=0.4", facecolor="#f0fdfa", edgecolor=TEAL, lw=0.9))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.3: CELL SIGNALLING PATHWAY (ENLARGED)
# ==============================================================================
def generate_fig4_3(filename="fig4_3_cell_signalling_pathway.png"):
    fig, ax = plt.subplots(figsize=(8.8, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Stages of Cell Signalling: Ligand Reception, Transduction & Cellular Response",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Step 1: Signalling cell secretes ligand
    b1 = FancyBboxPatch((3, 50), 18, 34, boxstyle="round,pad=0.5", facecolor="#e0e7ff", edgecolor="#4338ca", lw=1.3)
    ax.add_patch(b1)
    ax.text(12, 76, "Signalling\nCell", fontsize=8.5, fontweight='bold', color="#312e81", ha='center')
    ax.text(12, 58, "1. Secretion of\nchemical ligand\n(e.g., glucagon)", fontsize=7.5, color="#1e1b4b", ha='center')

    # Ligand molecule (triangle)
    ax.add_patch(Polygon([(25, 66), (29, 73), (29, 59)], facecolor=CRIMSON, edgecolor=NAVY, lw=1.0))
    ax.annotate("Ligand transported in\nblood / extracellular fluid", xy=(29, 66), xytext=(35, 80),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                fontsize=7.4, fontweight='bold', color=CRIMSON, ha='center')

    # Target Cell Surface Membrane at x=47..53, y=10..88
    mem = Rectangle((48, 10), 3.5, 78, facecolor="#fed7aa", edgecolor=AMBER, lw=1.1)
    ax.add_patch(mem)
    ax.text(49.7, 13, "Plasma\nMembrane", fontsize=7.0, fontweight='bold', color="#7c2d12", ha='center')

    # Receptor on target cell membrane
    rec = FancyBboxPatch((46, 52), 7.5, 26, boxstyle="round,pad=0.3", facecolor="#bfdbfe", edgecolor="#1d4ed8", lw=1.4)
    ax.add_patch(rec)
    rec_cleft = Polygon([(46, 61), (49, 65), (46, 69)], facecolor=WHITE, edgecolor="#1d4ed8", lw=1.0)
    ax.add_patch(rec_cleft)
    ax.text(49.7, 46, "Receptor\nProtein", fontsize=7.6, fontweight='bold', color="#1e3a8a", ha='center')

    # Ligand bound
    ax.add_patch(Polygon([(46, 61), (49, 65), (46, 69)], facecolor=CRIMSON, edgecolor=NAVY, lw=0.9))
    ax.text(49.7, 83, "2. Binding to\ncomplementary\nreceptor site", fontsize=7.6, fontweight='bold', color="#1e40af", ha='center')

    # Step 3: G-protein and Adenylyl Cyclase activation
    gprot = FancyBboxPatch((57, 54), 8.5, 14, boxstyle="round,pad=0.3", facecolor="#bbf7d0", edgecolor=GREEN, lw=1.1)
    ax.add_patch(gprot)
    ax.text(61.2, 61, "G-protein\nActive", fontsize=7.2, fontweight='bold', color="#14532d", ha='center')

    ax.annotate("", xy=(57, 63), xytext=(53.5, 63), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.3))

    ac = FancyBboxPatch((68, 50), 9.5, 20, boxstyle="round,pad=0.3", facecolor="#fef08a", edgecolor=AMBER, lw=1.1)
    ax.add_patch(ac)
    ax.text(72.7, 60, "Adenylyl\nCyclase", fontsize=7.2, fontweight='bold', color="#713f12", ha='center')

    ax.annotate("", xy=(68, 60), xytext=(65.5, 60), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.3))

    # Step 4: Second messenger cAMP & cascade
    ax.text(72.7, 40, "ATP -> cAMP\n(Second Messenger)", fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center')
    ax.annotate("", xy=(72.7, 45), xytext=(72.7, 50), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.3))

    # Cascade box
    casc = FancyBboxPatch((56, 18), 41, 18, boxstyle="round,pad=0.4", facecolor="#f3e8ff", edgecolor=PURPLE, lw=1.2)
    ax.add_patch(casc)
    ax.text(76.5, 30, "4. Enzyme Phosphorylation Cascade", fontsize=8.2, fontweight='bold', color=PURPLE, ha='center')
    ax.text(76.5, 22, "cAMP activates Protein Kinase A -> Phosphorylase\n-> Signal amplification (millions of molecules)", fontsize=7.2, color=DARK_GREY, ha='center')

    # Step 5: Cellular response
    resp = FancyBboxPatch((56, 4), 41, 11, boxstyle="round,pad=0.3", facecolor="#ecfdf5", edgecolor=GREEN, lw=1.2)
    ax.add_patch(resp)
    ax.text(76.5, 9.5, "5. Cellular Response: Glycogen -> Glucose-1-phosphate", fontsize=7.8, fontweight='bold', color=GREEN, ha='center')

    ax.annotate("", xy=(76.5, 15), xytext=(76.5, 18), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.4: SIMPLE VS FACILITATED DIFFUSION (ENLARGED)
# ==============================================================================
def generate_fig4_4(filename="fig4_4_simple_vs_facilitated_diffusion.png"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9.0, 4.4), dpi=300)

    for ax, title, sub in zip([ax1, ax2, ax3],
                              ["A: Simple Diffusion", "B: Facilitated (Channel)", "C: Facilitated (Carrier)"],
                              ["Small non-polar solutes (O₂, CO₂)", "Inorganic ions (Na⁺, K⁺, Cl⁻)", "Polar molecules (Glucose)"]):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(title, fontsize=9.4, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 91, sub, fontsize=7.4, color=DARK_GREY, ha='center')

        # Bilayers across y=42 to 58
        ax.plot([5, 95], [58, 58], color=NAVY, lw=1.2)
        ax.plot([5, 95], [42, 42], color=NAVY, lw=1.2)
        ax.text(5, 78, "High [S]", fontsize=8.0, fontweight='bold', color=CRIMSON)
        ax.text(5, 24, "Low [S]", fontsize=8.0, fontweight='bold', color=TEAL)

    # Panel 1: Simple Diffusion
    for x, y in [(30, 80), (45, 84), (60, 78), (75, 82), (50, 70)]:
        ax1.add_patch(Circle((x, y), 2.5, facecolor="#f87171", edgecolor=CRIMSON, lw=0.9))
    ax1.add_patch(Circle((50, 50), 2.5, facecolor="#f87171", edgecolor=CRIMSON, lw=0.9))
    ax1.annotate("", xy=(50, 28), xytext=(50, 68), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.0))
    ax1.text(50, 11, "• Passive / Down gradient\n• Directly through lipid bilayer\n• Rate proportional to gradient",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 2: Facilitated Channel
    ch1 = FancyBboxPatch((35, 36), 11, 26, boxstyle="round,pad=0.3", facecolor="#93c5fd", edgecolor=NAVY, lw=1.2)
    ch2 = FancyBboxPatch((54, 36), 11, 26, boxstyle="round,pad=0.3", facecolor="#93c5fd", edgecolor=NAVY, lw=1.2)
    ax2.add_patch(ch1)
    ax2.add_patch(ch2)
    ax2.annotate("", xy=(50, 26), xytext=(50, 72), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2.0))
    ax2.text(50, 50, "Pore", fontsize=7.8, fontweight='bold', color="#1e3a8a", ha='center', va='center')
    ax2.text(50, 11, "• Hydrophilic aqueous pore\n• Fixed or gated channel\n• Specific charge/size filter",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 3: Facilitated Carrier
    car = FancyBboxPatch((36, 36), 28, 26, boxstyle="round,pad=0.4", facecolor="#ddd6fe", edgecolor=PURPLE, lw=1.2)
    ax3.add_patch(car)
    ax3.add_patch(Polygon([(46, 62), (54, 62), (50, 52)], closed=True, facecolor=WHITE, edgecolor=PURPLE, lw=1.1))
    ax3.add_patch(Circle((50, 56), 2.5, facecolor="#a855f7", edgecolor=PURPLE, lw=0.9))
    ax3.annotate("", xy=(50, 25), xytext=(50, 36), arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.8))
    ax3.text(50, 42, "Conformation\nShift", fontsize=7.2, fontweight='bold', color=PURPLE, ha='center')
    ax3.text(50, 11, "• Solute binds specific site\n• Conformational change\n• Shows saturation kinetics",
             fontsize=7.4, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.5: DIFFUSION KINETICS CURVE (ENLARGED)
# ==============================================================================
def generate_fig4_5(filename="fig4_5_diffusion_kinetics_curve.png"):
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Kinetics of Membrane Transport: Simple vs Facilitated Diffusion",
            fontsize=10.8, fontweight='bold', color=NAVY, ha='center')

    # Axes
    ax.annotate("", xy=(12, 92), xytext=(12, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.6))
    ax.text(7, 54, "Rate of Transport into Cell / arbitrary units", fontsize=8.8, fontweight='bold', color=DARK_GREY, rotation=90, va='center')

    ax.annotate("", xy=(94, 16), xytext=(12, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.6))
    ax.text(54, 7, "Concentration Difference Across Membrane ([S]outside - [S]inside)", fontsize=8.8, fontweight='bold', color=DARK_GREY, ha='center')

    x_vals = np.linspace(12, 90, 100)
    y_simple = 16 + 0.65 * (x_vals - 12)
    ax.plot(x_vals, y_simple, color=CRIMSON, lw=2.5, label="Simple Diffusion (Direct Bilayer Flux)")

    y_fac = 16 + 62 * ((x_vals - 12) / ((x_vals - 12) + 20))
    ax.plot(x_vals, y_fac, color="#2563eb", lw=2.6, label="Facilitated Diffusion (Carrier / Channel)")

    # Plateau Vmax line
    ax.plot([12, 92], [78, 78], 'k--', lw=1.2, alpha=0.7)
    ax.text(50, 81, "Vmax (All carrier/channel proteins saturated)", fontsize=7.8, fontweight='bold', color="#1e3a8a")

    ax.annotate("Facilitated diffusion plateaus:\nTransport proteins become saturated\n(limiting factor)",
                xy=(52, 67), xytext=(20, 68),
                arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.2),
                fontsize=7.8, color="#1e3a8a", fontweight='bold')

    ax.annotate("Simple diffusion is non-saturable:\nRate directly proportional to gradient",
                xy=(76, 57), xytext=(68, 28),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.8, color=CRIMSON, fontweight='bold', ha='center')

    ax.legend(loc="upper left", bbox_to_anchor=(0.14, 0.94), fontsize=8.0, framealpha=0.92)
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.6: ACTIVE TRANSPORT SODIUM-POTASSIUM PUMP (ENLARGED)
# ==============================================================================
def generate_fig4_6(filename="fig4_6_active_transport_nak_pump.png"):
    fig, axes = plt.subplots(1, 4, figsize=(9.0, 4.0), dpi=300)
    steps = [
        ("Step 1: 3 Na⁺ Bind", "3 Na⁺ bind intracellularly\nto high-affinity sites"),
        ("Step 2: ATP Hydrolysis", "ATP transfers Pi to pump;\nconformational flip occurs"),
        ("Step 3: 3 Na⁺ Expelled", "3 Na⁺ released outside;\n2 K⁺ bind extracellularly"),
        ("Step 4: 2 K⁺ Imported", "Dephosphorylation restores\noriginal shape, releasing K⁺")
    ]

    for ax, (st, sub) in zip(axes, steps):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(st, fontsize=8.8, fontweight='bold', color=NAVY, pad=3)
        ax.text(50, 87, sub, fontsize=6.8, color=DARK_GREY, ha='center')

        # Membrane bar
        ax.plot([0, 100], [60, 60], color=AMBER, lw=1.6)
        ax.plot([0, 100], [40, 40], color=AMBER, lw=1.6)
        ax.text(2, 63, "EXT", fontsize=6.6, fontweight='bold', color=TEAL)
        ax.text(2, 33, "CYT", fontsize=6.6, fontweight='bold', color=DEEP_NAVY)

    # Step 1: Open to inside (CYT)
    p1 = Polygon([(30, 60), (70, 60), (62, 40), (38, 40)], closed=True, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.2)
    axes[0].add_patch(p1)
    for nx in [44, 50, 56]:
        axes[0].add_patch(Circle((nx, 32), 2.2, facecolor="#f87171", edgecolor=CRIMSON, lw=0.7))
        axes[0].text(nx, 32, "+", fontsize=5.0, ha='center', va='center')
    axes[0].text(50, 23, "3 Na⁺ enter", fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')

    # Step 2: ATP binding & phosphorylation
    p2 = Polygon([(35, 60), (65, 60), (65, 40), (35, 40)], closed=True, facecolor="#ddd6fe", edgecolor=PURPLE, lw=1.2)
    axes[1].add_patch(p2)
    axes[1].text(50, 50, "P", fontsize=8.5, fontweight='bold', color=WHITE, ha='center', va='center',
                 bbox=dict(boxstyle="circle,pad=0.2", facecolor=CRIMSON, edgecolor=NAVY))
    axes[1].text(50, 25, "ATP -> ADP + Pi\n(Phosphorylation)", fontsize=7.0, fontweight='bold', color=PURPLE, ha='center')

    # Step 3: Open to outside (EXT)
    p3 = Polygon([(38, 60), (62, 60), (70, 40), (30, 40)], closed=True, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.2)
    axes[2].add_patch(p3)
    for nx in [44, 50, 56]:
        axes[2].add_patch(Circle((nx, 72), 2.2, facecolor="#f87171", edgecolor=CRIMSON, lw=0.7))
    axes[2].text(50, 80, "3 Na⁺ exit", fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')
    for kx in [46, 54]:
        axes[2].add_patch(Circle((kx, 64), 2.4, facecolor="#67e8f9", edgecolor=TEAL, lw=0.7))
    axes[2].text(50, 25, "2 K⁺ bind", fontsize=7.2, fontweight='bold', color=TEAL, ha='center')

    # Step 4: Dephosphorylation and release of 2 K+
    p4 = Polygon([(30, 60), (70, 60), (62, 40), (38, 40)], closed=True, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.2)
    axes[3].add_patch(p4)
    for kx in [46, 54]:
        axes[3].add_patch(Circle((kx, 30), 2.4, facecolor="#67e8f9", edgecolor=TEAL, lw=0.7))
    axes[3].text(50, 19, "2 K⁺ imported\nPi released", fontsize=7.0, fontweight='bold', color=TEAL, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.7: OSMOSIS IN PLANT CELLS & PLASMOLYSIS (ENLARGED)
# ==============================================================================
def generate_fig4_7(filename="fig4_7_osmosis_plant_cells_plasmolysis.png"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9.0, 4.4), dpi=300)

    conditions = [
        ("A: Pure Water (Hypotonic)", "Ψ external = 0 kPa", "Turgid Plant Cell (Ψp > 0)"),
        ("B: Isotonic Solution", "Ψ external = Ψ cell", "Incipient Plasmolysis (Ψp = 0)"),
        ("C: Concentrated Sucrose", "Ψ external < Ψ cell", "Fully Plasmolysed Cell")
    ]

    for ax, (t1, t2, t3) in zip([ax1, ax2, ax3], conditions):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(t1, fontsize=9.4, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 91, f"{t2}\n{t3}", fontsize=7.4, color=DARK_GREY, ha='center')

        # Rigid Cell Wall
        wall = Rectangle((15, 20), 70, 64, facecolor="#dcfce7", edgecolor="#15803d", lw=2.2)
        ax.add_patch(wall)

    # Panel 1: Turgid
    proto1 = Rectangle((18, 23), 64, 58, facecolor="#fef08a", edgecolor="#ca8a04", lw=1.3)
    ax1.add_patch(proto1)
    vac1 = Rectangle((26, 30), 48, 44, facecolor="#bfdbfe", edgecolor="#2563eb", lw=1.2)
    ax1.add_patch(vac1)
    ax1.text(50, 52, "Large Turgid\nVacuole", fontsize=7.8, fontweight='bold', color="#1e40af", ha='center')
    ax1.text(50, 25, "Protoplast pushes firmly on wall", fontsize=7.0, color="#854d0e", ha='center')
    ax1.annotate("Net water influx", xy=(50, 75), xytext=(50, 85),
                 arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.6),
                 fontsize=7.4, fontweight='bold', color="#2563eb", ha='center')
    ax1.text(50, 8, "• Protoplast fully swollen\n• High turgor pressure (Ψp > 0)\n• Wall prevents bursting",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 2: Incipient Plasmolysis
    proto2_pts = [(24, 25), (76, 25), (82, 35), (82, 75), (76, 80), (24, 80), (18, 70), (18, 35)]
    proto2 = Polygon(proto2_pts, closed=True, facecolor="#fef08a", edgecolor="#ca8a04", lw=1.3)
    ax2.add_patch(proto2)
    vac2 = Rectangle((28, 33), 44, 38, facecolor="#bfdbfe", edgecolor="#2563eb", lw=1.1)
    ax2.add_patch(vac2)
    ax2.text(50, 52, "Vacuole volume\ndecreased", fontsize=7.4, fontweight='bold', color="#1e40af", ha='center')
    ax2.text(50, 8, "• 50% cells detached\n• Turgor pressure Ψp = 0\n• Overall cell Ψ = Ψs",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 3: Fully Plasmolysed
    proto3 = Ellipse((50, 52), 38, 32, facecolor="#fef08a", edgecolor="#ca8a04", lw=1.3)
    ax3.add_patch(proto3)
    vac3 = Ellipse((50, 52), 22, 18, facecolor="#bfdbfe", edgecolor="#2563eb", lw=1.1)
    ax3.add_patch(vac3)
    ax3.text(50, 52, "Shrivelled\nprotoplast", fontsize=7.2, fontweight='bold', color="#854d0e", ha='center')
    ax3.annotate("Filled with external\nhypertonic sucrose solution\n(freely permeable wall)",
                 xy=(74, 68), xytext=(50, 78),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                 fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')
    ax3.text(50, 8, "• Protoplast torn from wall\n• Severe water efflux\n• Extreme negative Ψ",
             fontsize=7.4, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.8: OSMOSIS IN ANIMAL ERYTHROCYTES (ENLARGED)
# ==============================================================================
def generate_fig4_8(filename="fig4_8_osmosis_erythrocytes.png"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9.0, 4.2), dpi=300)

    conds = [
        ("A: Hypotonic (0.1% NaCl)", "Ψ external > Ψ internal", "Haemolysis (Cell Lysis)"),
        ("B: Isotonic (0.9% NaCl)", "Ψ external = Ψ internal", "Normal Biconcave Erythrocyte"),
        ("C: Hypertonic (3.0% NaCl)", "Ψ external < Ψ internal", "Crenation (Shrivelled Cell)")
    ]

    for ax, (t1, t2, t3) in zip([ax1, ax2, ax3], conds):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(t1, fontsize=9.4, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 91, f"{t2}\n{t3}", fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 1: Haemolysis
    ax1.plot([25, 35, 45, 50, 60, 75, 70, 55, 30, 25],
             [50, 72, 70, 78, 68, 48, 28, 24, 32, 50], 'r--', lw=1.6)
    for hx, hy in [(40, 62), (48, 54), (58, 60), (52, 42), (64, 46), (36, 44), (50, 72)]:
        ax1.add_patch(Circle((hx, hy), 2.0, facecolor=CRIMSON, edgecolor=NAVY, lw=0.6))
    ax1.text(50, 52, "Haemoglobin\nReleased", fontsize=7.8, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(50, 11, "• No rigid cell wall\n• Excessive water influx\n• Membrane ruptures (bursts)",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 2: Isotonic (Normal Biconcave)
    rbc = Ellipse((50, 52), 48, 30, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.6)
    ax2.add_patch(rbc)
    dimp = Ellipse((50, 52), 24, 14, facecolor="#f87171", edgecolor="#b91c1c", lw=1.1)
    ax2.add_patch(dimp)
    ax2.text(50, 52, "Biconcave\nDisc", fontsize=8.0, fontweight='bold', color=WHITE, ha='center', va='center')
    ax2.text(50, 11, "• Dynamic equilibrium\n• Water influx = efflux\n• Stable cell volume",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Panel 3: Hypertonic (Crenation)
    angles = np.linspace(0, 2*np.pi, 16, endpoint=False)
    r_spikes = [20 if i % 2 == 0 else 12 for i in range(16)]
    cx_pts = [50 + r * np.cos(a) for r, a in zip(r_spikes, angles)]
    cy_pts = [52 + r * np.sin(a) for r, a in zip(r_spikes, angles)]
    cren = Polygon(list(zip(cx_pts, cy_pts)), closed=True, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.5)
    ax3.add_patch(cren)
    ax3.text(50, 52, "Crenated\n(Spiky)", fontsize=7.8, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax3.text(50, 11, "• Net water efflux\n• Cytoplasm dehydrates\n• Membrane wrinkles / shrinks",
             fontsize=7.4, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.9: WATER POTENTIAL CALIBRATION CURVE (ENLARGED)
# ==============================================================================
def generate_fig4_9(filename="fig4_9_water_potential_calibration_curve.png"):
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Estimation of Plant Tissue Water Potential via Percentage Mass Change",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Axes
    ax.annotate("", xy=(14, 92), xytext=(14, 12), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(7, 52, "Percentage Change in Mass of Potato Cylinders (%)",
            fontsize=8.5, fontweight='bold', color=DARK_GREY, rotation=90, va='center')

    ax.plot([14, 94], [50, 50], 'k-', lw=1.3)
    ax.annotate("", xy=(94, 50), xytext=(14, 50), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(54, 8, "Sucrose Concentration / mol dm⁻³", fontsize=9.0, fontweight='bold', color=DARK_GREY, ha='center')

    y_labels = [("+15", 80), ("+10", 70), ("+5", 60), ("0", 50), ("-5", 40), ("-10", 30), ("-15", 20)]
    for lbl, y in y_labels:
        ax.plot([12.5, 14], [y, y], 'k-', lw=1.0)
        ax.text(11, y, lbl, fontsize=7.5, ha='right', va='center')

    x_ticks = [(0.0, 14), (0.2, 30), (0.4, 46), (0.6, 62), (0.8, 78), (1.0, 94)]
    for val, x in x_ticks:
        ax.plot([x, x], [48.5, 50], 'k-', lw=1.0)
        ax.text(x, 46.0, f"{val:.1f}", fontsize=7.5, ha='center', va='top')

    pts_x = [14, 30, 46, 62, 78, 94]
    pts_y = [78, 62, 44, 32, 24, 20]

    poly_fit = np.poly1d(np.polyfit(pts_x, pts_y, 3))
    x_smooth = np.linspace(14, 94, 100)
    y_smooth = poly_fit(x_smooth)
    ax.plot(x_smooth, y_smooth, color=DEEP_NAVY, lw=2.2)

    for px, py in zip(pts_x, pts_y):
        ax.errorbar(px, py, yerr=2.2, fmt='o', color=CRIMSON, ecolor=DARK_GREY, elinewidth=1.1, capsize=3.0, markersize=5.0)

    roots = (poly_fit - 50).roots
    real_roots = [float(r.real) for r in roots if np.isreal(r) and 25 <= r.real <= 60]
    zero_x = real_roots[0] if len(real_roots) > 0 else 41.2
    molarity = 0.0 + (zero_x - 14) / (94 - 14) * 1.0

    ax.plot([zero_x, zero_x], [16, 50], 'r--', lw=1.4)
    ax.plot(zero_x, 50, 'ro', markersize=7.0)

    ax.annotate(f"Zero Change Point: {molarity:.2f} mol dm⁻³\nTissue Ψ = Solution Ψ = -860 kPa\nNo net water movement by osmosis",
                xy=(zero_x, 50), xytext=(zero_x + 10, 68),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.3),
                fontsize=8.0, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.10: AGAR CUBES SURFACE AREA TO VOLUME RATIO (ENLARGED)
# ==============================================================================
def generate_fig4_10(filename="fig4_10_agar_cubes_sa_vol_ratio.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.4), dpi=300)

    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Agar-Phenolphthalein Acid Diffusion", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # 3 Cubes side-by-side
    ax1.add_patch(Rectangle((8, 42), 26, 26, facecolor="#fbcfe8", edgecolor=CRIMSON, lw=1.3))
    ax1.add_patch(Rectangle((12, 46), 18, 18, facecolor="#f43f5e", edgecolor=CRIMSON, lw=1.1))
    ax1.text(21, 55, "Pink Core\n(Unreached)", fontsize=6.8, fontweight='bold', color=WHITE, ha='center')
    ax1.text(21, 34, "Cube 1 (3 cm)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')

    ax1.add_patch(Rectangle((42, 42), 18, 18, facecolor="#fbcfe8", edgecolor=CRIMSON, lw=1.3))
    ax1.add_patch(Rectangle((46, 46), 10, 10, facecolor="#f43f5e", edgecolor=CRIMSON, lw=1.1))
    ax1.text(51, 51, "Core", fontsize=6.5, fontweight='bold', color=WHITE, ha='center')
    ax1.text(51, 34, "Cube 2 (2 cm)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')

    ax1.add_patch(Rectangle((72, 42), 10, 10, facecolor="#fbcfe8", edgecolor=CRIMSON, lw=1.3))
    ax1.text(77, 47, "100%\nClear", fontsize=6.5, fontweight='bold', color=DARK_GREY, ha='center')
    ax1.text(77, 34, "Cube 3 (1 cm)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')

    ax1.annotate("Diffusion penetration depth\nis constant (~1.5 mm in 10 min)", xy=(21, 68), xytext=(50, 83),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                 fontsize=7.8, color=NAVY, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=NAVY, lw=0.8))

    # Right: Data Table
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Quantitative Scaling & Surface Area:Volume", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    headers = ["Cube Size", "Surface Area", "Volume", "SA : V", "% Decoloured"]
    cols_x = [13, 32, 51, 68, 86]

    ax2.add_patch(Rectangle((4, 76), 92, 10, facecolor=NAVY, edgecolor=NAVY))
    for h, x in zip(headers, cols_x):
        ax2.text(x, 81, h, fontsize=7.5, fontweight='bold', color=WHITE, ha='center', va='center')

    rows = [
        ("3 × 3 × 3 cm", "54 cm²", "27 cm³", "2.0 : 1", "48.1%"),
        ("2 × 2 × 2 cm", "24 cm²", "8 cm³",  "3.0 : 1", "73.5%"),
        ("1 × 1 × 1 cm", "6 cm²",  "1 cm³",  "6.0 : 1", "100.0%")
    ]

    for idx, (sz, sa, vol, sav, pct) in enumerate(rows):
        y_pos = 64 - idx * 12
        bg = "#f8fafc" if idx % 2 == 0 else WHITE
        ax2.add_patch(Rectangle((4, y_pos - 4), 92, 11, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        ax2.text(cols_x[0], y_pos + 1.5, sz, fontsize=7.4, fontweight='bold', color=DARK_GREY, ha='center')
        ax2.text(cols_x[1], y_pos + 1.5, sa, fontsize=7.4, color=DARK_GREY, ha='center')
        ax2.text(cols_x[2], y_pos + 1.5, vol, fontsize=7.4, color=DARK_GREY, ha='center')
        ax2.text(cols_x[3], y_pos + 1.5, sav, fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center')
        ax2.text(cols_x[4], y_pos + 1.5, pct, fontsize=7.6, fontweight='bold', color=GREEN, ha='center')

    ax2.text(50, 13, "Conclusion: As cell size increases, SA:V ratio decreases steeply.\nLarge organisms require specialised internal gas exchange surfaces.",
             fontsize=7.0, color=DARK_GREY, ha='center',
             bbox=dict(boxstyle="round,pad=0.4", facecolor="#f1f5f9", edgecolor=MID_GREY, lw=0.9))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.11: VISKING TUBING OSMOMETER (ENLARGED)
# ==============================================================================
def generate_fig4_11(filename="fig4_11_visking_tubing_osmometer.png"):
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Visking (Dialysis) Tubing Osmometer: Model of Selective Permeability",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    beaker = Polygon([(26, 68), (26, 16), (74, 16), (74, 68)], closed=False, color=DARK_GREY, lw=2.2)
    ax.add_patch(beaker)
    ax.add_patch(Rectangle((27, 16), 46, 46, facecolor="#e0f2fe", edgecolor="none"))
    ax.text(68, 56, "Distilled Water\n(Ψ = 0 kPa)", fontsize=8.0, fontweight='bold', color="#0369a1", ha='right')

    ax.add_patch(Rectangle((48.8, 36), 2.4, 54, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.3))

    bag = FancyBboxPatch((41, 20), 18, 22, boxstyle="round,pad=0.5,rounding_size=3",
                         facecolor="#fef08a", edgecolor="#ca8a04", lw=1.5)
    ax.add_patch(bag)
    ax.add_patch(Circle((50, 19), 2.2, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    ax.plot([40, 60], [42, 42], color=CRIMSON, lw=1.8)
    ax.text(50, 31, "Concentrated\nSucrose Soln\n(Low Ψ)", fontsize=7.5, fontweight='bold', color="#854d0e", ha='center')

    ax.plot([48.8, 51.2], [46, 46], color=CRIMSON, lw=1.3)
    ax.text(54, 46, "h₁ (Time = 0)", fontsize=7.5, color=DARK_GREY, va='center')

    ax.add_patch(Rectangle((49.0, 46), 2.0, 36, facecolor="#fde047", edgecolor="none"))
    ax.plot([48.8, 51.2], [82, 82], color=CRIMSON, lw=1.5)
    ax.text(54, 82, "h₂ (Time = 30 min)", fontsize=7.8, fontweight='bold', color=CRIMSON, va='center')

    ax.annotate("", xy=(46, 82), xytext=(46, 46), arrowprops=dict(arrowstyle="<->", color=CRIMSON, lw=1.3))
    ax.text(44, 64, "Δh", fontsize=8.8, fontweight='bold', color=CRIMSON, ha='right', va='center')

    ax.annotate("", xy=(42, 28), xytext=(32, 28), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.8))
    ax.annotate("", xy=(58, 28), xytext=(68, 28), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.8))
    ax.text(50, 10, "Osmotic Influx: Water molecules move down Ψ gradient across dialysis pores.\nSucrose molecules are too large to pass through cellulose pores.",
            fontsize=7.5, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.12: BULK TRANSPORT - ENDOCYTOSIS & EXOCYTOSIS (ENLARGED)
# ==============================================================================
def generate_fig4_12(filename="fig4_12_endocytosis_and_exocytosis.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.4), dpi=300)

    # Left: Endocytosis
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Endocytosis (Bulk Uptake)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    ax1.plot([5, 30, 36, 64, 70, 95], [75, 75, 52, 52, 75, 75], color=NAVY, lw=2.2)
    ax1.text(50, 88, "Extracellular Space", fontsize=8.0, fontweight='bold', color=TEAL, ha='center')
    ax1.text(50, 20, "Cytoplasm (requires ATP)", fontsize=8.0, fontweight='bold', color=DEEP_NAVY, ha='center')

    bact = FancyBboxPatch((44, 58), 12, 10, boxstyle="round,pad=0.3", facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.1)
    ax1.add_patch(bact)
    ax1.text(50, 63, "Particle", fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')

    ves1 = Circle((50, 34), 8.5, facecolor="#fed7aa", edgecolor=AMBER, lw=1.3)
    ax1.add_patch(ves1)
    bact_in = FancyBboxPatch((45, 30), 10, 8, boxstyle="round,pad=0.2", facecolor="#fca5a5", edgecolor=CRIMSON, lw=0.9)
    ax1.add_patch(bact_in)
    ax1.text(50, 9, "Endocytic Vesicle / Phagosome\nPinches off from plasma membrane", fontsize=7.4, color=DARK_GREY, ha='center')

    # Right: Exocytosis
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Exocytosis (Bulk Secretion)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    ax2.plot([5, 35, 42, 58, 65, 95], [75, 75, 58, 58, 75, 75], color=NAVY, lw=2.2)
    ax2.text(50, 88, "Secreted to Extracellular Space", fontsize=8.0, fontweight='bold', color=TEAL, ha='center')

    ves2 = Circle((50, 32), 9, facecolor="#bfdbfe", edgecolor="#2563eb", lw=1.3)
    ax2.add_patch(ves2)
    for sx, sy in [(47, 34), (53, 34), (50, 29), (47, 28), (53, 28)]:
        ax2.add_patch(Circle((sx, sy), 1.3, facecolor=GREEN, edgecolor="none"))
    ax2.text(50, 18, "Secretory Vesicle (Golgi-derived)\nFuses with plasma membrane (ATP-dependent)", fontsize=7.4, color=DARK_GREY, ha='center')

    for sx, sy in [(48, 64), (52, 65), (50, 70), (46, 74), (54, 76)]:
        ax2.add_patch(Circle((sx, sy), 1.3, facecolor=GREEN, edgecolor="none"))
    ax2.annotate("", xy=(50, 82), xytext=(50, 62), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.8))
    ax2.text(50, 6, "Examples: Digestive enzymes, insulin, neurotransmitters", fontsize=7.2, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.13: BEETROOT MEMBRANE PERMEABILITY (ENLARGED)
# ==============================================================================
def generate_fig4_13(filename="fig4_13_beetroot_membrane_permeability.png"):
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Effect of Temperature on Beetroot (Beta vulgaris) Cell Membrane Permeability",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Axes
    ax.annotate("", xy=(14, 92), xytext=(14, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(7, 54, "Optical Absorbance at 520 nm (Betalain Leakage) / a.u.",
            fontsize=8.5, fontweight='bold', color=DARK_GREY, rotation=90, va='center')

    ax.annotate("", xy=(94, 16), xytext=(14, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(54, 7, "Incubation Temperature / °C", fontsize=8.8, fontweight='bold', color=DARK_GREY, ha='center')

    x_temps = [(0, 14), (20, 34), (40, 54), (60, 74), (80, 94)]
    for val, x in x_temps:
        ax.plot([x, x], [14.5, 16], 'k-', lw=1.0)
        ax.text(x, 11, str(val), fontsize=7.6, ha='center', va='top')

    y_absorb = [(0.0, 16), (0.2, 30), (0.4, 45), (0.6, 60), (0.8, 75), (1.0, 90)]
    for val, y in y_absorb:
        ax.plot([12.5, 14], [y, y], 'k-', lw=1.0)
        ax.text(11, y, f"{val:.1f}", fontsize=7.5, ha='right', va='center')

    temps = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80])
    x_mapped = 14 + (temps / 80.0) * (94 - 14)
    absorbance = np.array([0.04, 0.04, 0.05, 0.06, 0.09, 0.16, 0.32, 0.58, 0.78, 0.92, 0.96])
    y_mapped = 16 + (absorbance / 1.0) * (90 - 16)

    x_interp = np.linspace(14, 94, 200)
    poly_beet = np.poly1d(np.polyfit(x_mapped, y_mapped, 4))
    y_interp = np.clip(poly_beet(x_interp), 16, 90)
    ax.plot(x_interp, y_interp, color=CRIMSON, lw=2.6)
    ax.plot(x_mapped, y_mapped, 'o', color=NAVY, markersize=5.5)

    ax.annotate("0°C - 40°C: Low baseline leakage\n• Membrane intact & selectively permeable\n• Gradual fluidity increase",
                xy=(34, 21), xytext=(20, 44),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.1),
                fontsize=7.8, color=NAVY, fontweight='bold')

    ax.annotate("45°C - 60°C: Steep increase in permeability\n• Denaturation of transport proteins creates pores\n• Phospholipid bilayer disrupted\n• Massive betalain leakage from vacuole",
                xy=(69, 58), xytext=(40, 78),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=8.0, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 4.14: MEMBRANE TRANSPORT DECISION MATRIX (ENLARGED)
# ==============================================================================
def generate_fig4_14(filename="fig4_14_membrane_transport_decision_tree.png"):
    fig, ax = plt.subplots(figsize=(9.2, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Comparative Classification Matrix of Membrane Transport Mechanisms",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    headers = ["Transport Mechanism", "Direction Relative to Gradient", "Energy Source", "Membrane Protein?", "Typical Solutes"]
    cols_x = [15, 38, 57, 73, 89]

    ax.add_patch(Rectangle((3, 84), 94, 9, facecolor=NAVY, edgecolor=NAVY))
    for h, x in zip(headers, cols_x):
        ax.text(x, 88.5, h, fontsize=7.6, fontweight='bold', color=WHITE, ha='center', va='center')

    rows = [
        ("Simple Diffusion", "Down concentration gradient\n(High -> Low)", "Passive\n(Kinetic energy)", "None\n(Direct bilayer flux)", "O₂, CO₂, fatty acids,\nsteroid hormones"),
        ("Facilitated Diffusion\n(Channel Protein)", "Down electrochemical gradient\n(High -> Low)", "Passive\n(Kinetic energy)", "Channel protein\n(Aqueous pore)", "Na⁺, K⁺, Ca²⁺, Cl⁻\n(Inorganic ions)"),
        ("Facilitated Diffusion\n(Carrier Protein)", "Down concentration gradient\n(High -> Low)", "Passive\n(Kinetic energy)", "Carrier protein\n(Shape change)", "Glucose, amino acids"),
        ("Osmosis", "Down water potential gradient\n(Less negative -> More negative)", "Passive\n(Kinetic energy)", "Aquaporin channels\n& bilayer gaps", "Water molecules (H₂O)"),
        ("Active Transport\n(Primary / Secondary)", "Against concentration gradient\n(Low -> High)", "Active: ATP hydrolysis\n(Metabolic energy)", "Carrier / Pump protein\n(e.g., Na⁺/K⁺-ATPase)", "Na⁺, K⁺, H⁺ (protons),\nsucrose-H⁺ co-transport"),
        ("Endocytosis / Exocytosis\n(Bulk Transport)", "Bulk vesicular movement\n(Internal / External)", "Active: ATP required\nfor cytoskeletal motor", "Vesicle membrane\nfusion / fission", "Secretory proteins, mucus,\nmacromolecules, bacteria")
    ]

    for idx, (m, d, e, p, s) in enumerate(rows):
        y_pos = 73 - idx * 12
        bg = "#f8fafc" if idx % 2 == 0 else WHITE
        ax.add_patch(Rectangle((3, y_pos - 4.5), 94, 11, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        ax.text(cols_x[0], y_pos + 1.0, m, fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')
        ax.text(cols_x[1], y_pos + 1.0, d, fontsize=7.0, color=DARK_GREY, ha='center')
        ax.text(cols_x[2], y_pos + 1.0, e, fontsize=7.2, fontweight='bold',
                color=CRIMSON if "Active" in e else TEAL, ha='center')
        ax.text(cols_x[3], y_pos + 1.0, p, fontsize=7.0, color=DARK_GREY, ha='center')
        ax.text(cols_x[4], y_pos + 1.0, s, fontsize=6.8, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("Regenerating Topic 4 Enlarged High-Legibility Diagrams...")
    generate_fig4_1()
    generate_fig4_2()
    generate_fig4_3()
    generate_fig4_4()
    generate_fig4_5()
    generate_fig4_6()
    generate_fig4_7()
    generate_fig4_8()
    generate_fig4_9()
    generate_fig4_10()
    generate_fig4_11()
    generate_fig4_12()
    generate_fig4_13()
    generate_fig4_14()
    print("All 14 Topic 4 diagrams regenerated successfully with enlarged fonts.")

if __name__ == "__main__":
    main()
