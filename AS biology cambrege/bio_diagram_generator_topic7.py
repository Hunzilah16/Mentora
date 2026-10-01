"""
Cambridge International AS Level Biology (9700)
Topic 7: Transport in Plants — High-Precision Publication-Quality Diagram Generator
Enlarged High-Legibility Edition: Generates 14 high-resolution 300 DPI figures for Topic 7:

1.  fig7_1_stem_root_ts_plan_diagrams.png
2.  fig7_2_leaf_ts_plan_diagram.png
3.  fig7_3_xylem_vessel_element_anatomy.png
4.  fig7_4_phloem_sieve_tube_companion_cell.png
5.  fig7_5_root_water_pathways_casparian.png
6.  fig7_6_cohesion_tension_transpiration_pull.png
7.  fig7_7_potometer_apparatus_setup.png
8.  fig7_8_potometer_transpiration_rates_graph.png
9.  fig7_9_xerophyte_leaf_marram_grass.png
10. fig7_10_companion_cell_sucrose_loading.png
11. fig7_11_mass_flow_hypothesis_model.png
12. fig7_12_aphid_stylet_translocation_experiment.png
13. fig7_13_ringed_stem_bark_girdling.png
14. fig7_14_plant_transport_diagnostic_tree.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Rectangle, Polygon, PathPatch, Wedge
import numpy as np

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mentora Academy Palette
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
BLUE = "#1d4ed8"
PALE_BLUE = "#e0f2fe"
PALE_GREEN = "#dcfce7"
PALE_AMBER = "#fef3c7"
PALE_CRIMSON = "#ffe4e6"

# ==============================================================================
# FIG 7.1: TS DICOT STEM & ROOT PLAN DIAGRAMS
# ==============================================================================
def generate_fig7_1(filename="fig7_1_stem_root_ts_plan_diagrams.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Dicot Stem TS Plan
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: TS Dicot Stem (Herbaceous Eudicot)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Outer stem epidermis
    stem_circle = Circle((50, 50), 44, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.5)
    ax1.add_patch(stem_circle)
    # Inner cortex boundary
    cortex_inner = Circle((50, 50), 38, facecolor="none", edgecolor="#cbd5e1", lw=1.0, ls="--")
    ax1.add_patch(cortex_inner)
    # Central pith (medulla)
    pith_circle = Circle((50, 50), 22, facecolor="#f1f5f9", edgecolor=MID_GREY, lw=1.2, ls=":")
    ax1.add_patch(pith_circle)
    ax1.text(50, 50, "PITH\n(Parenchyma)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=MID_GREY)

    # Ring of vascular bundles (8 bundles arranged in a peripheral ring)
    n_bundles = 8
    for i in range(n_bundles):
        angle = i * (2 * np.pi / n_bundles)
        r_centre = 30
        bx = 50 + r_centre * np.cos(angle)
        by = 50 + r_centre * np.sin(angle)
        
        # Sclerenchyma cap (outer)
        r_cap = 35
        cx = 50 + r_cap * np.cos(angle)
        cy = 50 + r_cap * np.sin(angle)
        cap = Circle((cx, cy), 3.2, facecolor=PALE_CRIMSON, edgecolor=CRIMSON, lw=1.0)
        ax1.add_patch(cap)
        
        # Phloem (middle-outer)
        r_phloem = 31.5
        px = 50 + r_phloem * np.cos(angle)
        py = 50 + r_phloem * np.sin(angle)
        phloem = Circle((px, py), 2.8, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.0)
        ax1.add_patch(phloem)
        
        # Cambium (line)
        # Xylem (inner towards pith)
        r_xylem = 26
        xx = 50 + r_xylem * np.cos(angle)
        xy = 50 + r_xylem * np.sin(angle)
        xylem = Circle((xx, xy), 3.2, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.1)
        ax1.add_patch(xylem)

    # Callout annotations for Stem
    ax1.annotate("Epidermis", xy=(50, 94), xytext=(20, 96),
                 arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax1.annotate("Cortex (Collenchyma & Parenchyma)", xy=(50, 88), xytext=(2, 85),
                 arrowprops=dict(arrowstyle="->", color=MID_GREY, lw=1.0),
                 fontsize=7.0, color=MID_GREY)
    ax1.annotate("Sclerenchyma Fibres (Bundle Cap)", xy=(50 + 35*np.cos(np.pi/4), 50 + 35*np.sin(np.pi/4)),
                 xytext=(68, 86), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=7.0, fontweight='bold', color=CRIMSON)
    ax1.annotate("Phloem (Outer)", xy=(50 + 31.5*np.cos(np.pi/4), 50 + 31.5*np.sin(np.pi/4)),
                 xytext=(72, 75), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0),
                 fontsize=7.2, fontweight='bold', color=GREEN)
    ax1.annotate("Xylem (Inner)", xy=(50 + 26*np.cos(np.pi/4), 50 + 26*np.sin(np.pi/4)),
                 xytext=(72, 63), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0),
                 fontsize=7.2, fontweight='bold', color=BLUE)
    ax1.text(50, 4, "Diagnostic: Vascular bundles in a peripheral ring;\nxylem facing internally, phloem facing externally.",
             ha='center', fontsize=6.8, fontstyle='italic', color=DARK_GREY)

    # Panel B: Dicot Root TS Plan
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: TS Dicot Root (Herbaceous Eudicot)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Outer root epidermis (piliferous layer)
    root_circle = Circle((50, 50), 44, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.5)
    ax2.add_patch(root_circle)

    # Root hair extensions
    for ang in [0.2, 0.9, 1.8, 2.5, 3.4, 4.3, 5.1, 5.9]:
        hx = 50 + 44 * np.cos(ang)
        hy = 50 + 44 * np.sin(ang)
        tx = 50 + 52 * np.cos(ang)
        ty = 50 + 52 * np.sin(ang)
        ax2.plot([hx, tx], [hy, ty], color=DARK_GREY, lw=1.2)

    # Wide cortex
    # Endodermis ring around central stele
    endodermis = Circle((50, 50), 16, facecolor=PALE_AMBER, edgecolor=AMBER, lw=1.5)
    ax2.add_patch(endodermis)
    # Pericycle ring inside
    pericycle = Circle((50, 50), 14.5, facecolor="none", edgecolor=MID_GREY, lw=0.9, ls="--")
    ax2.add_patch(pericycle)

    # Xylem Star (Tetrarch or 4-armed star in centre)
    x_arm = 12
    x_width = 3.5
    # Central cross polygon
    cross_pts = [
        (50 - x_width/2, 50 + x_arm), (50 + x_width/2, 50 + x_arm),
        (50 + x_width/2, 50 + x_width/2), (50 + x_arm, 50 + x_width/2),
        (50 + x_arm, 50 - x_width/2), (50 + x_width/2, 50 - x_width/2),
        (50 + x_width/2, 50 - x_arm), (50 - x_width/2, 50 - x_arm),
        (50 - x_width/2, 50 - x_width/2), (50 - x_arm, 50 - x_width/2),
        (50 - x_arm, 50 + x_width/2), (50 - x_width/2, 50 + x_width/2),
    ]
    star_poly = Polygon(cross_pts, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.5)
    ax2.add_patch(star_poly)

    # Phloem clusters in the four notches between xylem arms
    p_rad = 7.5
    for ang in [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]:
        px = 50 + p_rad * np.cos(ang)
        py = 50 + p_rad * np.sin(ang)
        p_patch = Circle((px, py), 2.8, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.2)
        ax2.add_patch(p_patch)

    # Annotations for Root
    ax2.annotate("Root Hair (Epidermis / Piliferous)", xy=(50 + 44*np.cos(0.9), 50 + 44*np.sin(0.9)),
                 xytext=(15, 94), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=7.2, fontweight='bold', color=DARK_GREY)
    ax2.annotate("Broad Parenchyma Cortex", xy=(50, 75), xytext=(6, 80),
                 arrowprops=dict(arrowstyle="->", color=MID_GREY, lw=1.0),
                 fontsize=7.0, color=MID_GREY)
    ax2.annotate("Endodermis with Casparian Strip", xy=(50, 66), xytext=(55, 82),
                 arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.1),
                 fontsize=7.2, fontweight='bold', color=AMBER)
    ax2.annotate("Pericycle (Internal to Endodermis)", xy=(50 + 14.5*np.cos(0.3), 50 + 14.5*np.sin(0.3)),
                 xytext=(65, 68), arrowprops=dict(arrowstyle="->", color=MID_GREY, lw=1.0),
                 fontsize=6.9, color=MID_GREY)
    ax2.annotate("Xylem (Central 'Star' / 'X' Shape)", xy=(50, 50), xytext=(68, 54),
                 arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2),
                 fontsize=7.2, fontweight='bold', color=BLUE)
    ax2.annotate("Phloem (Between Xylem Arms)", xy=(50 + 7.5*np.cos(np.pi/4), 50 + 7.5*np.sin(np.pi/4)),
                 xytext=(68, 40), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2),
                 fontsize=7.2, fontweight='bold', color=GREEN)
    ax2.text(50, 4, "Diagnostic: Central vascular stele; xylem forms star/cross;\nphloem in clusters between arms; enclosed by endodermis.",
             ha='center', fontsize=6.8, fontstyle='italic', color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.2: TS DICOT LEAF PLAN DIAGRAM
# ==============================================================================
def generate_fig7_2(filename="fig7_2_leaf_ts_plan_diagram.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("TS Dicot Leaf (Lamina & Midrib Vascular Bundle)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Upper waxy cuticle & Upper epidermis
    ax.add_patch(Rectangle((5, 84), 90, 2.5, facecolor="#fef08a", edgecolor=AMBER, lw=1.0))
    ax.text(8, 88.5, "Upper Waxy Cuticle (Hydrophobic)", fontsize=6.8, fontweight='bold', color=AMBER)
    ax.add_patch(Rectangle((5, 78), 90, 6, facecolor="#f1f5f9", edgecolor=DARK_GREY, lw=1.1))
    ax.text(8, 80, "Upper Epidermis (Single Layer, No Chloroplasts)", fontsize=6.8, color=DARK_GREY)

    # Palisade mesophyll layer
    ax.add_patch(Rectangle((5, 52), 90, 26, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.2))
    # Palisade cells indications
    for x in range(8, 93, 4):
        ax.plot([x, x], [52, 78], color="#86efac", lw=0.9, ls=":")
    ax.text(8, 64, "Palisade Mesophyll (Densely packed columnar cells; 80% chloroplasts; max light absorption)",
            fontsize=7.0, fontweight='bold', color=GREEN)

    # Spongy mesophyll layer with intercellular air spaces
    ax.add_patch(Rectangle((5, 24), 90, 28, facecolor="#f0fdf4", edgecolor="#86efac", lw=1.0))
    for cx, cy, r in [(15, 38, 4), (25, 42, 3.5), (35, 35, 4.5), (75, 40, 4), (85, 36, 4.2)]:
        ax.add_patch(Circle((cx, cy), r, facecolor=WHITE, edgecolor="#bbf7d0", lw=1.0))
    ax.text(8, 28, "Spongy Mesophyll (Loosely packed rounded cells + large moist intercellular air spaces)",
            fontsize=7.0, color="#166534")

    # Lower epidermis & Cuticle with Stomata
    ax.add_patch(Rectangle((5, 18), 35, 6, facecolor="#f1f5f9", edgecolor=DARK_GREY, lw=1.1))
    ax.add_patch(Rectangle((55, 18), 40, 6, facecolor="#f1f5f9", edgecolor=DARK_GREY, lw=1.1))
    # Stomatal pore + Guard cells
    ax.add_patch(Ellipse((45, 21), 6, 4.5, facecolor="#dcfce7", edgecolor=GREEN, lw=1.2))
    ax.add_patch(Ellipse((45, 21), 2, 3, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))
    ax.text(45, 12, "Stomatal Pore & Guard Cells\n(Gas exchange & Transpiration)", ha='center', fontsize=6.8, fontweight='bold', color=GREEN)

    # Midrib Vascular Bundle in the center
    # Collenchyma bundle sheath
    midrib_bg = Circle((50, 45), 18, facecolor="#f8fafc", edgecolor=MID_GREY, lw=1.4)
    ax.add_patch(midrib_bg)
    # Upper Xylem (Adaxial)
    xylem_wedge = Wedge((50, 45), 15, 0, 180, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.4)
    ax.add_patch(xylem_wedge)
    ax.text(50, 52, "XYLEM (Upper / Adaxial)\nWater & mineral ions", ha='center', va='center',
            fontsize=7.2, fontweight='bold', color=BLUE)

    # Lower Phloem (Abaxial)
    phloem_wedge = Wedge((50, 45), 15, 180, 360, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.4)
    ax.add_patch(phloem_wedge)
    ax.text(50, 38, "PHLOEM (Lower / Abaxial)\nSucrose & amino acids", ha='center', va='center',
            fontsize=7.2, fontweight='bold', color=GREEN)

    # Key diagnostic note
    ax.text(50, 4, "Key Rule: In leaf veins, Xylem is always toward upper (adaxial) surface; Phloem toward lower (abaxial) surface.",
            ha='center', fontsize=7.2, fontweight='bold', color=CRIMSON,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PALE_CRIMSON, edgecolor=CRIMSON, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.3: XYLEM VESSEL ELEMENT ANATOMY & WALL ADAPTATIONS
# ==============================================================================
def generate_fig7_3(filename="fig7_3_xylem_vessel_element_anatomy.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Longitudinal Section of Xylem Vessel
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Longitudinal Section (Continuous Capillary Tube)", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Xylem tube walls
    ax1.add_patch(Rectangle((30, 10), 8, 80, facecolor="#cbd5e1", edgecolor=BLUE, lw=1.5))
    ax1.add_patch(Rectangle((62, 10), 8, 80, facecolor="#cbd5e1", edgecolor=BLUE, lw=1.5))
    # Hollow lumen
    ax1.add_patch(Rectangle((38, 10), 24, 80, facecolor=PALE_BLUE, edgecolor="none"))

    # Lignin thickenings (annular and spiral patterns)
    for y in [20, 35, 50, 65, 80]:
        ax1.plot([30, 38], [y, y], color=CRIMSON, lw=3.0)
        ax1.plot([62, 70], [y, y], color=CRIMSON, lw=3.0)
        # Bordered pits
        ax1.add_patch(Circle((34, y - 7), 2.2, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))
        ax1.add_patch(Circle((66, y - 7), 2.2, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))

    # Perforated / absent end plate (remnants)
    ax1.plot([30, 36], [50, 50], color=BLUE, lw=1.5)
    ax1.plot([64, 70], [50, 50], color=BLUE, lw=1.5)
    ax1.plot([38, 62], [50, 50], color=MID_GREY, lw=1.0, ls="--")

    # Water flow arrows up the lumen
    for y_arrow in [25, 45, 65]:
        ax1.annotate("", xy=(50, y_arrow + 12), xytext=(50, y_arrow),
                     arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.0))
    ax1.text(50, 38, "Unbroken\nWater Column\n(Mass Flow)", ha='center', fontsize=6.8, fontweight='bold', color=BLUE)

    # Callouts
    ax1.annotate("Lignified Secondary Wall\n(High tensile strength; prevents collapse under tension)",
                 xy=(30, 65), xytext=(2, 78), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.8, fontweight='bold', color=CRIMSON)
    ax1.annotate("Bordered Pit (Non-lignified primary wall;\nlateral water movement between vessels)",
                 xy=(34, 43), xytext=(2, 30), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=6.6, color=DARK_GREY)
    ax1.annotate("Perforated / Completely Absent End Wall\n(Zero resistance to longitudinal mass flow)",
                 xy=(50, 50), xytext=(55, 54), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=NAVY)
    ax1.annotate("Hollow Lumen (Dead cell;\nno cytoplasm, vacuole, or nucleus)",
                 xy=(50, 80), xytext=(55, 88), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0),
                 fontsize=6.8, color=BLUE)

    # Panel B: Transverse Section & Lignin Patterns
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Transverse Section & Lignification Types", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Thick polygonal xylem vessel in TS
    outer_pts = [(20, 50), (32, 76), (62, 76), (74, 50), (62, 24), (32, 24)]
    inner_pts = [(26, 50), (36, 70), (58, 70), (68, 50), (58, 30), (36, 30)]
    ax2.add_patch(Polygon(outer_pts, facecolor="#cbd5e1", edgecolor=BLUE, lw=2.0))
    ax2.add_patch(Polygon(inner_pts, facecolor=PALE_BLUE, edgecolor=CRIMSON, lw=1.5))
    ax2.text(47, 50, "Empty Lumen\n(Wide Diameter;\nMinimises friction)", ha='center', va='center',
             fontsize=7.2, fontweight='bold', color=BLUE)

    # Bordered pit pairs in lateral walls
    ax2.add_patch(Circle((23, 50), 2.5, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))
    ax2.add_patch(Circle((71, 50), 2.5, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))
    ax2.annotate("Pit Membrane", xy=(71, 50), xytext=(78, 62),
                 arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=6.8, color=DARK_GREY)

    # Small boxes showing 3 lignin patterns below
    ax2.text(50, 14, "Syllabus Lignification Patterns: Ring (Annular) • Spiral • Pitted / Reticulate",
             ha='center', fontsize=6.8, fontweight='bold', color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.4: PHLOEM SIEVE TUBE ELEMENT & COMPANION CELL
# ==============================================================================
def generate_fig7_4(filename="fig7_4_phloem_sieve_tube_companion_cell.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Phloem Tissue: Sieve Tube Element & Companion Cell Architecture (LS)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Companion Cell (Left Column: width 24, from x=12 to 36)
    ax.add_patch(Rectangle((12, 10), 24, 80, facecolor="#ecfdf5", edgecolor=GREEN, lw=1.5))
    # Sieve Tube Element (Right Column: width 38, from x=36 to 74)
    ax.add_patch(Rectangle((36, 10), 38, 80, facecolor="#eff6ff", edgecolor=BLUE, lw=1.5))

    # Shared cell wall & Plasmodesmata connections
    ax.plot([36, 36], [10, 90], color=DARK_GREY, lw=2.5)
    for py in [25, 35, 45, 55, 65, 75]:
        ax.plot([34, 38], [py, py], color=WHITE, lw=2.0)
        ax.plot([34, 38], [py, py], color=AMBER, lw=1.2, ls=":")

    # Companion Cell features:
    # 1. Large prominent nucleus
    ax.add_patch(Ellipse((24, 60), 12, 9, facecolor="#fef08a", edgecolor=AMBER, lw=1.5))
    ax.add_patch(Circle((24, 60), 2.8, facecolor=AMBER))
    ax.text(24, 60, "Nucleus", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color=DARK_GREY)

    # 2. Abundant Mitochondria (generating ATP for H+-ATPase)
    for my in [25, 40, 78]:
        ax.add_patch(Ellipse((24, my), 8, 4.5, facecolor="#fed7aa", edgecolor=CRIMSON, lw=1.0))
        ax.plot([21, 27], [my, my], color=CRIMSON, lw=0.8, ls="--")
    ax.text(24, 25, "Mitochondria", ha='center', va='center', fontsize=6.2, fontweight='bold', color=CRIMSON)

    # 3. Dense ribosomes / Rough ER
    ax.text(24, 48, "Dense Cytoplasm\n(High metabolic activity;\nDirects sieve tube)",
            ha='center', fontsize=6.4, color="#065f46")

    # Sieve Tube Element features:
    # 1. Sieve Plate at top and bottom (perforated end wall)
    for spy in [15, 85]:
        ax.plot([36, 74], [spy, spy], color=BLUE, lw=2.2)
        # Sieve pores
        for px in [42, 50, 58, 66]:
            ax.add_patch(Circle((px, spy), 2.2, facecolor=WHITE, edgecolor=DARK_GREY, lw=1.0))
    ax.text(55, 88, "Sieve Plate with Sieve Pores (Perforated)", ha='center', fontsize=6.8, fontweight='bold', color=BLUE)

    # 2. Thin peripheral cytoplasm layer (lining walls)
    ax.add_patch(Rectangle((37, 16), 4, 68, facecolor="#bfdbfe", edgecolor="none"))
    ax.add_patch(Rectangle((69, 16), 4, 68, facecolor="#bfdbfe", edgecolor="none"))
    ax.text(71, 50, "Peripheral Cytoplasm (No nucleus, ribosomes, vacuole, Golgi)",
            rotation=270, va='center', fontsize=6.5, color=MID_GREY)

    # 3. Central lumen with phloem sap
    for ay in [30, 50, 70]:
        ax.annotate("", xy=(53, ay - 10), xytext=(53, ay),
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.8))
    ax.text(53, 50, "Phloem Sap Flow\n(Sucrose + amino acids\ndown pressure gradient)",
            ha='center', va='center', fontsize=7.0, fontweight='bold', color="#166534")

    # Callouts
    ax.annotate("Plasmodesmata (Dense symplastic channels\nfor passive sucrose diffusion)",
                xy=(36, 45), xytext=(4, 40), arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2),
                fontsize=7.0, fontweight='bold', color=AMBER)
    ax.annotate("Mitochondria generate ATP\nfor active H+ extrusion",
                xy=(24, 78), xytext=(4, 84), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.8, color=CRIMSON)

    # Column titles
    ax.text(24, 94, "COMPANION CELL\n(Living, Full Protoplast)", ha='center', fontsize=7.8, fontweight='bold', color=GREEN)
    ax.text(55, 94, "SIEVE TUBE ELEMENT\n(Living, Reduced Cytoplasm)", ha='center', fontsize=7.8, fontweight='bold', color=BLUE)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.5: ROOT WATER PATHWAYS & CASPARIAN STRIP CHECKPOINT
# ==============================================================================
def generate_fig7_5(filename="fig7_5_root_water_pathways_casparian.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Water Pathways Across Root Cortex: Apoplast, Symplast & Casparian Strip", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Draw cells in a row from root hair to xylem
    # Cell 1: Root hair (x=6 to 22)
    ax.add_patch(Rectangle((14, 20), 8, 60, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.2))
    ax.plot([6, 14], [50, 50], color=DARK_GREY, lw=3.0) # root hair tip
    ax.text(14, 84, "Root Hair\n(Epidermis)", ha='center', fontsize=6.8, fontweight='bold', color=DARK_GREY)

    # Cell 2 & 3: Cortex Parenchyma Cells (x=26 to 42, x=46 to 62)
    ax.add_patch(Rectangle((26, 20), 16, 60, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.2))
    ax.text(34, 84, "Cortex\nParenchyma", ha='center', fontsize=6.8, color=MID_GREY)
    ax.add_patch(Rectangle((46, 20), 16, 60, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.2))
    ax.text(54, 84, "Inner Cortex", ha='center', fontsize=6.8, color=MID_GREY)

    # Cell 4: Endodermal Cell with Casparian Strip (x=66 to 78)
    ax.add_patch(Rectangle((66, 20), 12, 60, facecolor=PALE_AMBER, edgecolor=AMBER, lw=1.4))
    ax.text(72, 84, "ENDODERMIS\n(Checkpoint)", ha='center', fontsize=7.2, fontweight='bold', color=AMBER)

    # Casparian strip in radial and transverse walls
    ax.add_patch(Rectangle((70, 70), 4, 10, facecolor=CRIMSON, edgecolor=NAVY, lw=1.0))
    ax.add_patch(Rectangle((70, 20), 4, 10, facecolor=CRIMSON, edgecolor=NAVY, lw=1.0))
    ax.text(70, 14, "Casparian Strip\n(Suberin)", ha='center', fontsize=6.8, fontweight='bold', color=CRIMSON)

    # Cell 5: Pericycle (x=82 to 88)
    ax.add_patch(Rectangle((82, 20), 6, 60, facecolor="#f1f5f9", edgecolor=MID_GREY, lw=1.0))
    ax.text(85, 84, "Pericycle", ha='center', fontsize=6.4, color=MID_GREY)

    # Cell 6: Xylem Vessel (x=90 to 98)
    ax.add_patch(Rectangle((90, 20), 8, 60, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.5))
    ax.text(94, 84, "Xylem\nVessel", ha='center', fontsize=7.0, fontweight='bold', color=BLUE)

    # Plasmodesmata connecting cytoplasms
    for px in [22, 42, 62, 78, 88]:
        ax.plot([px, px+4], [50, 50], color=WHITE, lw=3.0)
        ax.plot([px, px+4], [50, 50], color="#93c5fd", lw=1.5)

    # Pathway 1: Symplast (Blue dashed arrow through cytoplasm & plasmodesmata)
    ax.annotate("", xy=(90, 50), xytext=(8, 50),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2, ls="-"))
    ax.text(34, 54, "Symplast Pathway (Cytoplasm & Plasmodesmata)", fontsize=7.0, fontweight='bold', color=BLUE)

    # Pathway 2: Apoplast (Red dashed arrow through cell walls, blocked at Casparian strip)
    # Wall path along top
    ax.plot([14, 70], [75, 75], color=CRIMSON, lw=2.0, ls="--")
    # Blocked by suberin, diverted DOWN into symplast
    ax.plot([70, 70], [75, 55], color=CRIMSON, lw=2.0, ls="--")
    ax.annotate("", xy=(72, 50), xytext=(70, 55),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.0))
    ax.text(34, 77, "Apoplast Pathway (Cell walls & intercellular spaces)", fontsize=7.0, fontweight='bold', color=CRIMSON)

    # Blocked sign at Casparian strip
    ax.plot([68, 76], [72, 78], color=NAVY, lw=2.0)
    ax.plot([68, 76], [78, 72], color=NAVY, lw=2.0)
    ax.annotate("Suberin blocks apoplast;\nforces water into symplast\nvia cell membrane",
                xy=(70, 75), xytext=(74, 64), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.8, fontweight='bold', color=CRIMSON)

    # Diagnostic banner
    ax.text(50, 6, "Biological Function: Forces selective uptake across plasma membrane carrier proteins; excludes toxins & pathogens.",
            ha='center', fontsize=7.2, fontweight='bold', color=NAVY,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.6: COHESION-TENSION THEORY & TRANSPIRATION PULL
# ==============================================================================
def generate_fig7_6(filename="fig7_6_cohesion_tension_transpiration_pull.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Leaf Meniscus Evaporation & Transpiration Tension
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Transpiration Pull at Leaf Mesophyll", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Mesophyll cells with curved water menisci in microfibril pores
    ax1.add_patch(Circle((30, 70), 14, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.2))
    ax1.text(30, 70, "Mesophyll\nCell", ha='center', va='center', fontsize=7.0, color=GREEN)
    ax1.add_patch(Circle((70, 70), 14, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.2))
    ax1.text(70, 70, "Mesophyll\nCell", ha='center', va='center', fontsize=7.0, color=GREEN)

    # Water film covering cell walls
    ax1.plot([44, 56], [70, 70], color=BLUE, lw=3.0)
    # Curved meniscus between cells creating tension
    meniscus = patches.Arc((50, 70), 12, 10, angle=0, theta1=180, theta2=360, color=BLUE, lw=2.2)
    ax1.add_patch(meniscus)
    ax1.text(50, 74, "Curved Meniscus\n(High Surface Tension)", ha='center', fontsize=6.6, fontweight='bold', color=BLUE)

    # Substomatal air space
    ax1.text(50, 52, "Substomatal Air Space\n(High Water Vapour Concentration)", ha='center', fontsize=6.8, color=MID_GREY)

    # Stoma open at bottom
    ax1.add_patch(Ellipse((40, 28), 8, 12, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.2))
    ax1.add_patch(Ellipse((60, 28), 8, 12, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.2))
    ax1.text(50, 28, "Stomatal\nPore", ha='center', va='center', fontsize=6.4, color=DARK_GREY)

    # Water vapour diffusion arrow
    ax1.annotate("", xy=(50, 10), xytext=(50, 36),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.2))
    ax1.text(50, 14, "Diffusion of Water Vapour\ndown water potential gradient", ha='center', fontsize=6.8, fontweight='bold', color=TEAL)

    # Panel B: Cohesion & Adhesion in Xylem Capillary Column
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Cohesion-Tension in Xylem Vessel", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Xylem vessel walls
    ax2.add_patch(Rectangle((30, 10), 8, 80, facecolor="#cbd5e1", edgecolor=BLUE, lw=1.5))
    ax2.add_patch(Rectangle((62, 10), 8, 80, facecolor="#cbd5e1", edgecolor=BLUE, lw=1.5))
    ax2.add_patch(Rectangle((38, 10), 24, 80, facecolor=PALE_BLUE, edgecolor="none"))

    # Water molecules (circles) linked by hydrogen bonds
    y_coords = [20, 32, 44, 56, 68, 80]
    for y in y_coords:
        ax2.add_patch(Circle((50, y), 4.0, facecolor=BLUE, edgecolor=NAVY, lw=1.0))
        ax2.text(50, y, "H₂O", ha='center', va='center', fontsize=5.8, fontweight='bold', color=WHITE)
        if y > 20:
            # Hydrogen bond between water molecules
            ax2.plot([50, 50], [y - 4, y - 8], color=CRIMSON, lw=2.0, ls=":")

    # Adhesion lines to wall
    ax2.plot([46, 38], [44, 44], color=GREEN, lw=1.8, ls="--")
    ax2.plot([54, 62], [44, 44], color=GREEN, lw=1.8, ls="--")

    # Tension arrow pulling upwards
    ax2.annotate("", xy=(50, 94), xytext=(50, 84),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.5))
    ax2.text(50, 96, "Tension / Negative Pressure", ha='center', fontsize=7.2, fontweight='bold', color=CRIMSON)

    # Annotations
    ax2.annotate("COHESION: Hydrogen bonds between\nwater molecules maintain continuous column",
                 xy=(50, 62), xytext=(4, 60), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.8, fontweight='bold', color=CRIMSON)
    ax2.annotate("ADHESION: Hydrogen bonds between\nwater and hydrophilic cellulose/lignin",
                 xy=(38, 44), xytext=(2, 36), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0),
                 fontsize=6.8, fontweight='bold', color=GREEN)
    ax2.annotate("Lignified Wall prevents vessel\nfrom buckling inwards under tension",
                 xy=(66, 32), xytext=(54, 20), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0),
                 fontsize=6.8, color=BLUE)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.7: POTOMETER APPARATUS SETUP
# ==============================================================================
def generate_fig7_7(filename="fig7_7_potometer_apparatus_setup.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Potometer Apparatus Setup (Measurement of Water Uptake Rate)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Leafy shoot in rubber stopper
    ax.add_patch(Rectangle((18, 55), 10, 15, facecolor="#475569", edgecolor=DARK_GREY, lw=1.2)) # rubber stopper
    ax.plot([23, 23], [60, 48], color="#166534", lw=4.0) # stem cut under water
    # Stem cut at angle
    ax.plot([21, 25], [48, 46], color="#166534", lw=3.0)

    # Leaves on shoot
    for lx, ly in [(15, 75), (20, 85), (28, 80), (18, 92), (26, 90)]:
        ax.add_patch(Ellipse((lx, ly), 8, 4, angle=30, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.0))
    ax.text(23, 96, "Cut Leafy Shoot\n(Slanted cut made underwater)", ha='center', fontsize=6.8, fontweight='bold', color=GREEN)

    # Vaseline / Petroleum jelly seal
    ax.add_patch(Rectangle((16, 68), 14, 4, facecolor="#fef08a", edgecolor=AMBER, lw=1.0))
    ax.annotate("Petroleum Jelly / Vaseline\n(Ensures completely airtight seal)",
                xy=(30, 70), xytext=(35, 78), arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.1),
                fontsize=6.8, fontweight='bold', color=AMBER)

    # Glass reservoir with tap
    ax.add_patch(Rectangle((42, 55), 14, 20, facecolor=PALE_BLUE, edgecolor=DARK_GREY, lw=1.2))
    ax.text(49, 65, "Water\nReservoir", ha='center', va='center', fontsize=6.8, color=BLUE)
    # Tap
    ax.add_patch(Rectangle((47, 45), 4, 10, facecolor="#94a3b8", edgecolor=DARK_GREY, lw=1.0))
    ax.text(49, 40, "Tap (Reset Bubble)", ha='center', fontsize=6.4, color=DARK_GREY)

    # Horizontal capillary tube
    ax.plot([18, 88], [35, 35], color=BLUE, lw=4.0)
    ax.plot([18, 88], [33, 33], color=DARK_GREY, lw=1.2)
    ax.plot([18, 88], [37, 37], color=DARK_GREY, lw=1.2)

    # Ruler / Millimetre scale below capillary tube
    ax.add_patch(Rectangle((52, 26), 32, 5, facecolor="#fef08a", edgecolor=AMBER, lw=1.0))
    for rx in range(54, 84, 2):
        ax.plot([rx, rx], [26, 28], color=DARK_GREY, lw=0.8)
    ax.text(68, 22, "Calibrated Scale (mm)", ha='center', fontsize=6.6, fontweight='bold', color=AMBER)

    # Air bubble in capillary tube
    ax.add_patch(Rectangle((62, 33.5), 5, 3, facecolor=WHITE, edgecolor=CRIMSON, lw=1.4))
    ax.annotate("Air Bubble (Index Mark)", xy=(64.5, 37), xytext=(55, 48),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.0, fontweight='bold', color=CRIMSON)
    # Movement arrow
    ax.annotate("", xy=(56, 35), xytext=(62, 35),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.0))
    ax.text(59, 31, "Direction of Movement", ha='center', fontsize=6.2, color=NAVY)

    # Beaker of water at far right
    ax.add_patch(Rectangle((86, 20), 10, 20, facecolor=PALE_BLUE, edgecolor=DARK_GREY, lw=1.2))
    ax.text(91, 14, "Beaker of\nWater", ha='center', fontsize=6.4, color=DARK_GREY)

    # Key syllabus note box
    ax.text(50, 6, "CRITICAL EXAMINER TRAP: Potometer measures WATER UPTAKE rate, NOT transpiration directly!\n(Small volume of water consumed in photosynthesis and retained for cell turgor/growth).",
            ha='center', fontsize=7.0, fontweight='bold', color=CRIMSON,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PALE_CRIMSON, edgecolor=CRIMSON, lw=1.1))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.8: POTOMETER TRANSPIRATION RATES GRAPH (ENVIRONMENTAL FACTORS)
# ==============================================================================
def generate_fig7_8(filename="fig7_8_potometer_transpiration_rates_graph.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Wind Speed & Humidity
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_title("A: Effect of Wind Speed & Humidity on Transpiration", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)
    ax1.set_xlabel("Environmental Factor Intensity (Arbitrary Units)", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax1.set_ylabel("Rate of Transpiration / mm min⁻¹", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax1.grid(True, linestyle=":", alpha=0.6)

    x = np.linspace(0.5, 9.5, 100)
    # Wind speed: increases and plateaus (removes boundary layer until stomatal diffusion is limiting)
    y_wind = 2.0 + 6.5 * (1 - np.exp(-0.5 * x))
    ax1.plot(x, y_wind, color=BLUE, lw=2.2, label="Wind Speed (Blows away humid boundary layer)")

    # Humidity: decreases linearly (flattens water potential gradient)
    y_hum = 8.5 - 0.7 * x
    ax1.plot(x, y_hum, color=CRIMSON, lw=2.2, label="Relative Humidity (Reduces Ψ gradient)")

    ax1.legend(loc='center right', fontsize=6.8, framealpha=0.9)
    ax1.text(5, 1.2, "Higher humidity reduces difference in water potential;\nsteep gradient disappears.",
             ha='center', fontsize=6.6, fontstyle='italic', color=DARK_GREY)

    # Panel B: Light Intensity & Temperature
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title("B: Effect of Light Intensity & Temperature", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)
    ax2.set_xlabel("Environmental Factor Intensity (Arbitrary Units)", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Rate of Transpiration / mm min⁻¹", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.grid(True, linestyle=":", alpha=0.6)

    # Light intensity: steep increase as stomata open, then plateaus when fully open
    y_light = 1.0 + 7.5 * (1 - np.exp(-0.7 * x))
    ax2.plot(x, y_light, color=AMBER, lw=2.2, label="Light Intensity (Triggers stomatal opening)")

    # Temperature: exponential increase (kinetic energy & evaporation) then drops if heat causes stomatal closure
    y_temp = 1.5 * np.exp(0.2 * x)
    # Beyond x=7.5, drops due to wilting/stomatal closure
    y_temp_real = np.where(x < 7.5, 1.5 * np.exp(0.2 * x), 1.5 * np.exp(0.2 * 7.5) - 3.5 * (x - 7.5))
    ax2.plot(x, y_temp_real, color=GREEN, lw=2.2, label="Temperature (Increases kinetic energy;\nexcess causes stomatal closure)")

    ax2.legend(loc='upper left', fontsize=6.8, framealpha=0.9)
    ax2.text(5, 1.2, "Excessive heat causes wilting; ABA triggers stomatal closure\nto conserve water.",
             ha='center', fontsize=6.6, fontstyle='italic', color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.9: XEROPHYTE LEAF ADAPTATIONS (MARRAM GRASS)
# ==============================================================================
def generate_fig7_9(filename="fig7_9_xerophyte_leaf_marram_grass.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("TS Rolled Leaf of Xerophyte (Marram Grass — Ammophila arenaria)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Outer curled boundary (abaxial surface with very thick cuticle)
    theta = np.linspace(0.15 * np.pi, 0.85 * np.pi, 200)
    r_outer = 40
    r_inner = 30
    cx, cy = 50, 42

    x_out = cx + r_outer * np.cos(theta)
    y_out = cy + r_outer * np.sin(theta)
    x_in = cx + r_inner * np.cos(theta)
    y_in = cy + r_inner * np.sin(theta)

    # Draw rolled leaf crescent
    leaf_poly = Polygon(list(zip(x_out, y_out)) + list(zip(x_in[::-1], y_in[::-1])),
                        facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.5)
    ax.add_patch(leaf_poly)

    # Thick waxy cuticle on outer curved surface (abaxial)
    ax.plot(x_out, y_out, color=AMBER, lw=3.5)
    ax.annotate("Thick Waxy Cuticle (Outer / Abaxial Surface)\nImpermeable to water; stops cuticular transpiration",
                xy=(cx, cy + r_outer), xytext=(12, 92), arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2),
                fontsize=7.0, fontweight='bold', color=AMBER)

    # Inward grooves / ridges with sunken stomata on inner (adaxial) surface
    for angle in np.linspace(0.25 * np.pi, 0.75 * np.pi, 7):
        gx = cx + (r_inner + 3) * np.cos(angle)
        gy = cy + (r_inner + 3) * np.sin(angle)
        # Trichomes / hairs in groove
        for dx, dy in [(-1, 2), (0, 3), (1, 2)]:
            ax.plot([gx, gx + dx], [gy, gy + dy], color=DARK_GREY, lw=1.0)
        # Sunken stoma
        ax.add_patch(Circle((gx, gy - 2), 1.5, facecolor=WHITE, edgecolor=CRIMSON, lw=1.0))

    # Hinge cells at bottom of grooves (bulliform cells)
    ax.add_patch(Circle((cx, cy + r_inner + 2), 3.0, facecolor="#93c5fd", edgecolor=BLUE, lw=1.0))
    ax.annotate("Hinge Cells (Bulliform Cells)\nLose turgor under water stress to curl leaf tightly",
                xy=(cx, cy + r_inner + 2), xytext=(52, 60), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1),
                fontsize=6.8, fontweight='bold', color=BLUE)

    # Trapped humid air chamber inside
    ax.text(cx, cy + 12, "Trapped Moist Humid Microclimate\n(Reduces water potential gradient\nbetween stoma and leaf interior)",
            ha='center', fontsize=7.2, fontweight='bold', color="#1e3a8a",
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.0))

    # Callouts
    ax.annotate("Epidermal Trichomes (Hairs)\nTrap boundary layer of humid air;\nreduce air movement / wind speed",
                xy=(cx - 15, cy + 22), xytext=(2, 40), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.1),
                fontsize=6.8, fontweight='bold', color=DARK_GREY)
    ax.annotate("Sunken Stomata in Pits\nShielded from wind currents;\nhumid air builds up in pit",
                xy=(cx + 15, cy + 22), xytext=(72, 40), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                fontsize=6.8, fontweight='bold', color=CRIMSON)

    # Summary box at bottom
    ax.text(50, 4, "Key Principle: Xerophytic adaptations work by increasing diffusion distance and reducing the water potential gradient.",
            ha='center', fontsize=7.0, fontstyle='italic', color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.10: COMPANION CELL SUCROSE ACTIVE LOADING (PROTON PUMP & COTRANSPORTER)
# ==============================================================================
def generate_fig7_10(filename="fig7_10_companion_cell_sucrose_loading.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Molecular Mechanism of Phloem Loading (Proton Pump & H⁺/Sucrose Cotransporter)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Three compartments:
    # 1. Apoplast / Cell Wall (x=5 to 30)
    ax.add_patch(Rectangle((5, 12), 25, 76, facecolor="#f1f5f9", edgecolor=DARK_GREY, lw=1.2))
    ax.text(17.5, 84, "APOPLAST / CELL WALL\n(High [H⁺] / Low pH)", ha='center', fontsize=7.2, fontweight='bold', color=DARK_GREY)

    # 2. Companion Cell Cytoplasm (x=30 to 70)
    ax.add_patch(Rectangle((30, 12), 40, 76, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.4))
    ax.text(50, 84, "COMPANION CELL CYTOPLASM\n(Low [H⁺] / High [Sucrose])", ha='center', fontsize=7.2, fontweight='bold', color=GREEN)

    # 3. Phloem Sieve Tube Element (x=70 to 95)
    ax.add_patch(Rectangle((70, 12), 25, 76, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.2))
    ax.text(82.5, 84, "SIEVE TUBE ELEMENT\n(Phloem Sap Translocation)", ha='center', fontsize=7.2, fontweight='bold', color=BLUE)

    # Protein 1: H+-ATPase Proton Pump in Companion Cell membrane (at x=30, y=60)
    ax.add_patch(Ellipse((30, 60), 6, 12, facecolor=PALE_CRIMSON, edgecolor=CRIMSON, lw=1.5))
    ax.text(30, 60, "H⁺-ATPase\nPump", ha='center', va='center', fontsize=6.2, fontweight='bold', color=CRIMSON)

    # Active transport arrow: H+ pumped OUT into apoplast
    ax.annotate("", xy=(18, 60), xytext=(40, 60),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.2))
    ax.text(29, 68, "H⁺ (Active Transport)", ha='center', fontsize=6.8, fontweight='bold', color=CRIMSON)
    ax.text(40, 52, "ATP → ADP + Pᵢ", ha='center', fontsize=6.4, fontweight='bold', color=CRIMSON)

    # Protein 2: H+/Sucrose Cotransporter (at x=30, y=32)
    ax.add_patch(Ellipse((30, 32), 6, 12, facecolor=PALE_AMBER, edgecolor=AMBER, lw=1.5))
    ax.text(30, 32, "Cotransporter\n(Symport)", ha='center', va='center', fontsize=6.0, fontweight='bold', color=AMBER)

    # Cotransport arrows: H+ diffuses IN down gradient, bringing Sucrose IN against gradient
    ax.annotate("", xy=(44, 35), xytext=(18, 35),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=2.0))
    ax.text(28, 40, "H⁺ (Facilitated Diffusion down gradient)", ha='center', fontsize=6.4, color=AMBER)

    ax.annotate("", xy=(44, 28), xytext=(18, 28),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.0))
    ax.text(28, 23, "Sucrose (Secondary Active Transport against gradient)", ha='center', fontsize=6.4, fontweight='bold', color=GREEN)

    # Plasmodesmata connecting companion cell to sieve tube (at x=70, y=45)
    ax.plot([68, 72], [45, 45], color=WHITE, lw=4.0)
    ax.plot([68, 72], [45, 45], color=AMBER, lw=2.0, ls=":")
    ax.annotate("", xy=(80, 45), xytext=(60, 45),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.2))
    ax.text(70, 50, "Plasmodesmata\n(Diffusion of Sucrose)", ha='center', fontsize=6.6, fontweight='bold', color=NAVY)

    # Resulting effect in sieve tube
    ax.text(82.5, 30, "Sucrose Accumulation:\n• Lowers Water Potential (Ψ)\n• Water enters by Osmosis\n• Generates High Hydrostatic\n  Pressure at Source",
            ha='center', fontsize=6.6, fontweight='bold', color=BLUE,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=WHITE, edgecolor=BLUE, lw=1.0))

    # Examiner warning banner at bottom
    ax.text(50, 4, "COMMON TRAP: H⁺ ions are pumped OUT of companion cell, creating electrochemical gradient; sucrose enters WITH H⁺.",
            ha='center', fontsize=7.0, fontweight='bold', color=CRIMSON)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.11: MASS FLOW HYPOTHESIS MODEL (SOURCE TO SINK)
# ==============================================================================
def generate_fig7_11(filename="fig7_11_mass_flow_hypothesis_model.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("The Mass Flow Hypothesis of Translocation (Source to Sink)", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Left Column: XYLEM (Water Flow Upwards)
    ax.add_patch(Rectangle((15, 12), 20, 76, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.5))
    ax.text(25, 84, "XYLEM VESSEL\n(Continuous tube)", ha='center', fontsize=7.2, fontweight='bold', color=BLUE)
    # Upward water flow
    for wy in [30, 50, 70]:
        ax.annotate("", xy=(25, wy + 10), xytext=(25, wy),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))
    ax.text(25, 45, "Transpiration\nStream\n(Tension)", ha='center', va='center', fontsize=6.8, color=BLUE)

    # Right Column: PHLOEM SIEVE TUBE (Mass Flow Downwards)
    ax.add_patch(Rectangle((65, 12), 20, 76, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.5))
    ax.text(75, 84, "PHLOEM SIEVE TUBE\n(Sieve plates)", ha='center', fontsize=7.2, fontweight='bold', color=GREEN)
    # Downward mass flow
    for py in [65, 45]:
        ax.annotate("", xy=(75, py - 10), xytext=(75, py),
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.2))
    ax.text(75, 50, "MASS FLOW\nof Phloem Sap\ndown ΔP gradient", ha='center', va='center', fontsize=6.8, fontweight='bold', color="#166534")

    # Top: SOURCE (e.g., Photosynthesising Leaf Mesophyll)
    ax.add_patch(FancyBboxPatch((40, 68), 20, 14, boxstyle="round,pad=0.5", facecolor=PALE_AMBER, edgecolor=AMBER, lw=1.2))
    ax.text(50, 75, "SOURCE (Leaf)\nSucrose loaded", ha='center', va='center', fontsize=6.8, fontweight='bold', color=DARK_GREY)

    # Osmosis from xylem to phloem at source
    ax.annotate("", xy=(65, 75), xytext=(35, 75),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.0))
    ax.text(50, 63, "Osmosis: Water enters phloem\n(High Hydrostatic Pressure, P₁)", ha='center', fontsize=6.6, fontweight='bold', color=TEAL)

    # Bottom: SINK (e.g., Root / Storage Tuber / Meristem)
    ax.add_patch(FancyBboxPatch((40, 20), 20, 14, boxstyle="round,pad=0.5", facecolor="#fed7aa", edgecolor=CRIMSON, lw=1.2))
    ax.text(50, 27, "SINK (Root/Tuber)\nSucrose unloaded", ha='center', va='center', fontsize=6.8, fontweight='bold', color=DARK_GREY)

    # Osmosis from phloem back to xylem at sink
    ax.annotate("", xy=(35, 27), xytext=(65, 27),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.0))
    ax.text(50, 15, "Osmosis: Water leaves phloem\n(Low Hydrostatic Pressure, P₂)", ha='center', fontsize=6.6, fontweight='bold', color=TEAL)

    # Gradient formula callout
    ax.text(50, 44, "Hydrostatic Pressure Gradient: ΔP = P(source) - P(sink)\nDrives bulk mass flow of sucrose and water together.",
            ha='center', fontsize=7.2, fontweight='bold', color=NAVY,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, edgecolor=NAVY, lw=1.2))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.12: APHID STYLET TRANSLOCATION EXPERIMENT
# ==============================================================================
def generate_fig7_12(filename="fig7_12_aphid_stylet_translocation_experiment.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Aphid Feeding & Severed Stylet
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Aphid Stylet Technique", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Plant stem cross section (cortex and phloem)
    ax1.add_patch(Rectangle((10, 10), 30, 80, facecolor="#f8fafc", edgecolor=DARK_GREY, lw=1.2))
    ax1.text(25, 84, "Stem Cortex", ha='center', fontsize=7.0, color=MID_GREY)

    # Phloem Sieve Tube (vertical cylinder)
    ax1.add_patch(Rectangle((40, 10), 16, 80, facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.4))
    ax1.text(48, 84, "Sieve\nTube", ha='center', fontsize=6.8, fontweight='bold', color=GREEN)

    # Aphid body (simplified cartoon outline at right)
    ax1.add_patch(Ellipse((80, 50), 18, 12, facecolor="#fed7aa", edgecolor=AMBER, lw=1.2))
    ax1.text(80, 50, "Aphid\nBody", ha='center', va='center', fontsize=6.8, color=DARK_GREY)

    # Fine stylet needle penetrating into sieve tube element
    ax1.plot([72, 48], [50, 50], color=CRIMSON, lw=2.2)
    ax1.add_patch(Circle((48, 50), 2.0, facecolor=CRIMSON))

    # Exuding sap droplet from severed stylet
    ax1.add_patch(Circle((65, 50), 3.5, facecolor="#93c5fd", edgecolor=BLUE, lw=1.0))
    ax1.annotate("Pure Phloem Sap Exuding\n(Positive Hydrostatic Pressure;\nHigh sucrose concentration)",
                 xy=(65, 50), xytext=(45, 68), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=BLUE)

    ax1.text(50, 4, "Stylet anaesthetised with CO₂ and severed with laser;\nsap collected without triggering wound response (callose).",
             ha='center', fontsize=6.6, fontstyle='italic', color=DARK_GREY)

    # Panel B: Radioactive 14C Translocation Velocity Curve
    ax2.set_xlim(0, 60)
    ax2.set_ylim(0, 100)
    ax2.set_title("B: Radioactivity Tracked Along Stem Over Time", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)
    ax2.set_xlabel("Distance Down Stem from Source Leaf / cm", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Radioactivity / Counts min⁻¹", fontsize=7.5, fontweight='bold', color=DARK_GREY)
    ax2.grid(True, linestyle=":", alpha=0.6)

    dist = np.linspace(0, 60, 100)
    # Curves at t = 1 hr, 2 hr, 3 hr
    y_1h = 90 * np.exp(-((dist - 10) / 6)**2)
    y_2h = 75 * np.exp(-((dist - 25) / 7)**2)
    y_3h = 60 * np.exp(-((dist - 40) / 8)**2)

    ax2.plot(dist, y_1h, color=BLUE, lw=2.0, label="After 1 hour (Peak at 10 cm)")
    ax2.plot(dist, y_2h, color=GREEN, lw=2.0, label="After 2 hours (Peak at 25 cm)")
    ax2.plot(dist, y_3h, color=CRIMSON, lw=2.0, label="After 3 hours (Peak at 40 cm)")

    ax2.legend(loc='upper right', fontsize=6.8, framealpha=0.9)
    ax2.text(30, 20, "Measured Velocity: ~15 cm h⁻¹ (0.5 - 1.0 m h⁻¹)\nProves mass flow; far too rapid for simple diffusion!",
             ha='center', fontsize=6.8, fontweight='bold', color=NAVY,
             bbox=dict(boxstyle='round,pad=0.2', facecolor=WHITE, edgecolor=NAVY, lw=1.0))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.13: RINGED STEM (BARK GIRDLING) EXPERIMENT
# ==============================================================================
def generate_fig7_13(filename="fig7_13_ringed_stem_bark_girdling.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Freshly Girdled Woody Stem
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Woody Stem Immediately After Ringing", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Stem cylinder
    ax1.add_patch(Rectangle((35, 10), 30, 80, facecolor="#fef3c7", edgecolor="#78350f", lw=1.4))
    # Ring removed (bark + phloem excised, central wood/xylem intact)
    ax1.add_patch(Rectangle((35, 45), 30, 12, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.5))
    ax1.text(50, 51, "Exposed Xylem (Wood)\n(Phloem & Bark completely removed)", ha='center', va='center',
             fontsize=6.8, fontweight='bold', color=BLUE)

    ax1.annotate("Bark + Phloem Ring Removed", xy=(65, 51), xytext=(70, 65),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=CRIMSON)

    # Panel B: After Several Weeks (Tissue Swelling Above Ring)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Stem After Several Weeks of Growth", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Upper stem with swelling
    upper_stem = Polygon([(35, 90), (65, 90), (69, 58), (31, 58)], facecolor="#fef3c7", edgecolor="#78350f", lw=1.4)
    ax2.add_patch(upper_stem)
    # Swelling bulge
    ax2.add_patch(Ellipse((50, 60), 40, 10, facecolor="#fde68a", edgecolor=AMBER, lw=1.5))
    ax2.text(50, 60, "TISSUE SWELLING\n(High Sucrose & Amino Acids)", ha='center', va='center',
             fontsize=7.0, fontweight='bold', color=CRIMSON)

    # Exposed xylem ring in middle
    ax2.add_patch(Rectangle((35, 45), 30, 12, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.5))
    ax2.text(50, 51, "Intact Xylem", ha='center', va='center', fontsize=6.8, color=BLUE)

    # Lower stem (normal or slightly starved)
    ax2.add_patch(Rectangle((35, 10), 30, 35, facecolor="#fef3c7", edgecolor="#78350f", lw=1.4))
    ax2.text(50, 25, "Lower Stem & Roots\n(Reduced sugar supply;\nRoot growth halted)", ha='center', va='center',
             fontsize=6.8, color=MID_GREY)

    # Annotations
    ax2.annotate("Downward translocation blocked;\nassimilates accumulate above ring",
                 xy=(50, 66), xytext=(10, 80), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=CRIMSON)
    ax2.annotate("Upward water transport continues uninterrupted\n(Leaves remain turgid & green)",
                 xy=(50, 51), xytext=(2, 38), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1),
                 fontsize=6.8, color=BLUE)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# FIG 7.14: PLANT TRANSPORT MECHANISMS DIAGNOSTIC TREE
# ==============================================================================
def generate_fig7_14(filename="fig7_14_plant_transport_diagnostic_tree.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Plant Transport Systems: Comparative Diagnostic Decision Matrix", fontsize=10, fontweight='bold', color=NAVY, pad=6)

    # Top Root Node
    ax.add_patch(FancyBboxPatch((35, 84), 30, 12, boxstyle="round,pad=0.5", facecolor=NAVY, edgecolor=NAVY, lw=1.5))
    ax.text(50, 90, "VASCULAR SYSTEM OF HERBACEOUS DICOT", ha='center', va='center', fontsize=7.5, fontweight='bold', color=WHITE)

    # Left Branch: XYLEM
    ax.plot([50, 25], [84, 72], color=BLUE, lw=2.0)
    ax.add_patch(FancyBboxPatch((10, 58), 30, 14, boxstyle="round,pad=0.4", facecolor=PALE_BLUE, edgecolor=BLUE, lw=1.4))
    ax.text(25, 65, "XYLEM TISSUE\n(Water & Dissolved Mineral Ions)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=BLUE)

    # Left Details Box
    ax.plot([25, 25], [58, 48], color=BLUE, lw=1.5)
    ax.add_patch(FancyBboxPatch((6, 12), 38, 36, boxstyle="round,pad=0.4", facecolor=WHITE, edgecolor=BLUE, lw=1.2))
    xylem_text = (
        "• Cell Types: Dead vessel elements & tracheids\n"
        "• Wall Structure: Heavily lignified secondary walls\n"
        "• End Walls: Perforated or absent (continuous tube)\n"
        "• Driving Force: Transpiration pull (negative tension)\n"
        "• Mechanism: Cohesion-tension theory + adhesion\n"
        "• Direction: Unidirectional (Root → Stem → Leaves)\n"
        "• Energy: Passive (Solar heat energy drives evaporation)"
    )
    ax.text(8, 30, xylem_text, va='center', fontsize=6.4, color=DARK_GREY)

    # Right Branch: PHLOEM
    ax.plot([50, 75], [84, 72], color=GREEN, lw=2.0)
    ax.add_patch(FancyBboxPatch((60, 58), 30, 14, boxstyle="round,pad=0.4", facecolor=PALE_GREEN, edgecolor=GREEN, lw=1.4))
    ax.text(75, 65, "PHLOEM TISSUE\n(Sucrose & Amino Acids / Assimilates)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=GREEN)

    # Right Details Box
    ax.plot([75, 75], [58, 48], color=GREEN, lw=1.5)
    ax.add_patch(FancyBboxPatch((56, 12), 38, 36, boxstyle="round,pad=0.4", facecolor=WHITE, edgecolor=GREEN, lw=1.2))
    phloem_text = (
        "• Cell Types: Living sieve tubes + companion cells\n"
        "• Wall Structure: Cellulose primary walls (non-lignified)\n"
        "• End Walls: Perforated sieve plates with callose pores\n"
        "• Driving Force: Hydrostatic pressure gradient (ΔP)\n"
        "• Mechanism: Mass flow hypothesis + active loading\n"
        "• Direction: Bidirectional (Source → Sink)\n"
        "• Energy: Active (ATP required for H⁺-ATPase pump)"
    )
    ax.text(58, 30, phloem_text, va='center', fontsize=6.4, color=DARK_GREY)

    # Center Comparison Note
    ax.text(50, 4, "Cambridge Marking Criterion: Always link tissue anatomy directly to biophysical transport physics!",
            ha='center', fontsize=6.8, fontstyle='italic', color=CRIMSON)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"Generated: {outpath}")

# ==============================================================================
# MAIN RUNNER
# ==============================================================================
if __name__ == "__main__":
    print("Generating all 14 publication-quality figures for Topic 7...")
    generate_fig7_1()
    generate_fig7_2()
    generate_fig7_3()
    generate_fig7_4()
    generate_fig7_5()
    generate_fig7_6()
    generate_fig7_7()
    generate_fig7_8()
    generate_fig7_9()
    generate_fig7_10()
    generate_fig7_11()
    generate_fig7_12()
    generate_fig7_13()
    generate_fig7_14()
    print("All 14 figures successfully created at 300 DPI!")
