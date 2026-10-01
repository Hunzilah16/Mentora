"""
Cambridge International AS Level Biology (9700)
Topic 5: The Mitotic Cell Cycle — High-Precision Publication-Quality Diagram Generator
Enlarged High-Legibility Edition: Boosted font sizes and line weights for crystal-clear printing.

Generates 14 high-resolution 300 DPI figures for Topic 5:
1.  fig5_1_chromosome_structure_telomeres.png
2.  fig5_2_cell_cycle_pie_chart.png
3.  fig5_3_dna_mass_ploidy_graph.png
4.  fig5_4_mitosis_four_stages_diagram.png
5.  fig5_5_root_tip_squash_photomicrograph.png
6.  fig5_6_telomere_shortening_senescence.png
7.  fig5_7_stem_cell_hierarchy_potency.png
8.  fig5_8_carcinogenesis_tumour_formation.png
9.  fig5_9_cytokinesis_animal_vs_plant.png
10. fig5_10_kinetochore_spindle_microtubules.png
11. fig5_11_mitotic_inhibitors_microtubule_poisons.png
12. fig5_12_mitotic_index_grid_counting.png
13. fig5_13_centrosome_centriole_duplication.png
14. fig5_14_cell_cycle_checkpoints_cyclin_cdk.png
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
# FIG 5.1: REPLICATED CHROMOSOME STRUCTURE & TELOMERES
# ==============================================================================
def generate_fig5_1(filename="fig5_1_chromosome_structure_telomeres.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.8), dpi=300)

    # Left: Replicated Metaphase Chromosome
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Replicated Metaphase Chromosome", fontsize=10.0, fontweight='bold', color=NAVY, pad=4)

    # Left chromatid
    c1_p = FancyBboxPatch((38, 54), 8.5, 32, boxstyle="round,pad=0.5,rounding_size=3", facecolor="#93c5fd", edgecolor=NAVY, lw=1.4)
    c1_q = FancyBboxPatch((38, 14), 8.5, 34, boxstyle="round,pad=0.5,rounding_size=3", facecolor="#93c5fd", edgecolor=NAVY, lw=1.4)
    ax1.add_patch(c1_p)
    ax1.add_patch(c1_q)

    # Right chromatid
    c2_p = FancyBboxPatch((52, 54), 8.5, 32, boxstyle="round,pad=0.5,rounding_size=3", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.4)
    c2_q = FancyBboxPatch((52, 14), 8.5, 34, boxstyle="round,pad=0.5,rounding_size=3", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.4)
    ax1.add_patch(c2_p)
    ax1.add_patch(c2_q)

    # Centromere (Primary Constriction)
    centro = Circle((49.2, 50), 5.5, facecolor=AMBER, edgecolor=NAVY, lw=1.4)
    ax1.add_patch(centro)
    ax1.text(49.2, 50, "C", fontsize=8.0, fontweight='bold', color=WHITE, ha='center', va='center')

    # Kinetochore protein complexes on sides
    k1 = Rectangle((36.5, 47), 2.5, 6, facecolor=CRIMSON, edgecolor=NAVY, lw=0.9)
    k2 = Rectangle((59.5, 47), 2.5, 6, facecolor=CRIMSON, edgecolor=NAVY, lw=0.9)
    ax1.add_patch(k1)
    ax1.add_patch(k2)

    # Telomeres at chromosome ends (bright red caps)
    for tx in [38, 52]:
        t_top = FancyBboxPatch((tx, 81), 8.5, 5.5, boxstyle="round,pad=0.2", facecolor="#ef4444", edgecolor=NAVY, lw=1.1)
        t_bot = FancyBboxPatch((tx, 13.5), 8.5, 5.5, boxstyle="round,pad=0.2", facecolor="#ef4444", edgecolor=NAVY, lw=1.1)
        ax1.add_patch(t_top)
        ax1.add_patch(t_bot)

    # Labels and annotations - positioned well within margins
    ax1.annotate("Telomeres (TTAGGG repeats)\n• Prevent end degradation\n• Prevent fusion with other DNA",
                 xy=(42, 84), xytext=(4, 91),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                 fontsize=7.4, fontweight='bold', color=CRIMSON, ha='left')

    ax1.annotate("Centromere:\n• Primary constriction\n• Holds sister chromatids\n• Kinetochore site",
                 xy=(44, 50), xytext=(2, 50),
                 arrowprops=dict(arrowstyle="->", color="#854d0e", lw=1.2),
                 fontsize=6.8, fontweight='bold', color="#854d0e", ha='left', va='center')

    ax1.annotate("Sister Chromatids\n(Identical DNA copies from S phase)",
                 xy=(60, 70), xytext=(68, 76),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                 fontsize=7.4, fontweight='bold', color=NAVY, ha='left')

    ax1.annotate("Short arm (p arm)", xy=(60, 60), xytext=(68, 60),
                 arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=7.2, color=DARK_GREY, ha='left')

    ax1.annotate("Long arm (q arm)", xy=(60, 28), xytext=(68, 28),
                 arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                 fontsize=7.2, color=DARK_GREY, ha='left')

    # Right: DNA Packing & Nucleosome Ultrastructure
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Chromatin Hierarchy & Nucleosome Model", fontsize=10.0, fontweight='bold', color=NAVY, pad=4)

    # DNA double helix ribbon at top
    ax2.plot([10, 90], [86, 86], color="#2563eb", lw=2.2)
    ax2.plot([10, 90], [82, 82], color="#2563eb", lw=2.2)
    for x in range(15, 88, 7):
        ax2.plot([x, x], [82, 86], color="#93c5fd", lw=1.5)
    ax2.text(50, 91, "2 nm: Naked DNA Double Helix", fontsize=8.0, fontweight='bold', color="#1e40af", ha='center')

    # Nucleosomes (beads on a string)
    ax2.text(50, 68, "11 nm: 'Beads on a String' (Nucleosomes)", fontsize=8.0, fontweight='bold', color=PURPLE, ha='center')
    ax2.plot([10, 90], [56, 56], color="#2563eb", lw=1.8, linestyle='--')
    for nx in [22, 42, 62, 82]:
        nuc = Circle((nx, 56), 6.5, facecolor="#e9d5ff", edgecolor=PURPLE, lw=1.3)
        ax2.add_patch(nuc)
        ax2.text(nx, 56, "Histone\nOctamer", fontsize=6.2, fontweight='bold', color="#581c87", ha='center', va='center')
        # Linker DNA wrapping
        ax2.plot([nx-6.5, nx+6.5], [59, 59], color=CRIMSON, lw=1.6)
        ax2.plot([nx-6.5, nx+6.5], [53, 53], color=CRIMSON, lw=1.6)

    # 30 nm Chromatin solenoid & looped domains
    ax2.add_patch(Rectangle((6, 18), 88, 26, facecolor="#f1f5f9", edgecolor=MID_GREY, lw=1.1, linestyle=':'))
    ax2.text(50, 39, "30 nm Chromatin Fibre -> 300 nm Looped Domains", fontsize=8.0, fontweight='bold', color=DARK_GREY, ha='center')
    ax2.text(50, 29, "• Histone H1 clamps DNA to octamer core\n• Non-histone scaffold proteins organise loops\n• Maximally condensed into chromosome during mitosis",
             fontsize=7.3, color=DARK_GREY, ha='center')

    ax2.text(50, 7, "Chromosome Composition by Dry Mass:\n~40% DNA + ~60% Protein (Histones & Scaffolds)",
             fontsize=7.3, fontweight='bold', color=NAVY, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=NAVY, lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.2: MITOTIC CELL CYCLE PIE CHART & PHASES
# ==============================================================================
def generate_fig5_2(filename="fig5_2_cell_cycle_pie_chart.png"):
    fig, ax = plt.subplots(figsize=(8.8, 5.0), dpi=300)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.axis('off')

    ax.text(0, 1.28, "The Eukaryotic Mitotic Cell Cycle & Regulatory Checkpoints",
            fontsize=11.0, fontweight='bold', color=NAVY, ha='center')

    # Proportions: G1 (~40%), S (~30%), G2 (~15%), M (~10%), Cytokinesis (~5%)
    # Total Interphase = 85%, M phase + C = 15%
    phases = [
        ("G₁ Phase\n(Growth 1)", 40, "#93c5fd", NAVY, "Cell growth, RNA & protein synthesis,\norganelle duplication (centrioles begin)"),
        ("S Phase\n(Synthesis)", 30, "#86efac", GREEN, "Semi-conservative DNA replication;\nhistone synthesis; DNA mass 2C -> 4C"),
        ("G₂ Phase\n(Growth 2)", 15, "#fde047", "#854d0e", "Spindle tubulin synthesised;\nATP accumulated; error checking"),
        ("Mitosis (M)", 10, "#fca5a5", CRIMSON, "Nuclear division: Prophase, Metaphase,\nAnaphase, Telophase"),
        ("Cytokinesis", 5, "#c4b5fd", PURPLE, "Division of cytoplasm;\ncleavage furrow (animals) / cell plate (plants)")
    ]

    start_angle = 90
    for name, pct, col, text_col, desc in phases:
        angle_width = (pct / 100.0) * 360
        end_angle = start_angle - angle_width

        wedge = Wedge((0, 0), 1.0, end_angle, start_angle, width=0.45,
                      facecolor=col, edgecolor=WHITE, lw=2.0)
        ax.add_patch(wedge)

        # Label position
        mid_angle = np.deg2rad(start_angle - angle_width / 2.0)
        lx = 0.77 * np.cos(mid_angle)
        ly = 0.77 * np.sin(mid_angle)
        ax.text(lx, ly, name, fontsize=7.8, fontweight='bold', color=text_col, ha='center', va='center')

        start_angle = end_angle

    # Center Hub
    center_circle = Circle((0, 0), 0.55, facecolor="#f8fafc", edgecolor=NAVY, lw=1.6)
    ax.add_patch(center_circle)
    ax.text(0, 0.16, "INTERPHASE", fontsize=9.2, fontweight='bold', color=NAVY, ha='center')
    ax.text(0, 0.02, "(~90% of Total Cycle Time)", fontsize=7.4, color=DARK_GREY, ha='center')
    ax.text(0, -0.16, "Metabolically active phase\nNo visible chromosomes", fontsize=7.0, color=DARK_GREY, ha='center')

    # Arrow indicating direction of cycle
    ax.annotate("", xy=(0.85, 0.65), xytext=(0.65, 0.85),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.2, connectionstyle="arc3,rad=-0.3"))

    # Checkpoint Flags
    # G1/S Restriction Checkpoint
    ax.text(1.22, 0.20, "G₁ Checkpoint (Restriction Point)\n• Checks DNA damage & cell size\n• Commitment to divide or enter G₀",
            fontsize=7.4, fontweight='bold', color=NAVY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=NAVY, lw=0.9))
    ax.plot([0.88, 1.05], [0.12, 0.18], color=NAVY, lw=1.3)

    # G2/M Checkpoint
    ax.text(-1.35, -0.85, "G₂/M Checkpoint\n• Checks DNA replication completeness\n• Repaired errors before mitosis starts",
            fontsize=7.4, fontweight='bold', color="#854d0e",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fefce8", edgecolor="#ca8a04", lw=0.9))
    ax.plot([-0.75, -0.92], [-0.55, -0.72], color="#ca8a04", lw=1.3)

    # Spindle Assembly Checkpoint (M Checkpoint)
    ax.text(-1.35, 0.85, "Spindle Checkpoint (Metaphase SAC)\n• Checks all kinetochores attached to spindle\n• Prevents nondisjunction / aneuploidy",
            fontsize=7.4, fontweight='bold', color=CRIMSON,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef2f2", edgecolor=CRIMSON, lw=0.9))
    ax.plot([-0.50, -0.78], [0.82, 0.82], color=CRIMSON, lw=1.3)

    # G0 phase branch
    ax.annotate("G₀ Phase: Resting / Quiescent\n(e.g., neurons, memory cells)",
                xy=(0.95, 0.35), xytext=(1.05, 0.72),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2, linestyle='--'),
                fontsize=7.2, color=DARK_GREY,
                bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE, edgecolor=MID_GREY, lw=0.7))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.3: DNA MASS & PLOIDY CHANGES ACROSS CELL CYCLE
# ==============================================================================
def generate_fig5_3(filename="fig5_3_dna_mass_ploidy_graph.png"):
    fig, ax = plt.subplots(figsize=(8.8, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Quantitative Changes in DNA Mass & Chromosome/Chromatid Number",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Axes
    ax.annotate("", xy=(26, 92), xytext=(26, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.6))
    ax.text(3.5, 54, "Quantity per Cell / arbitrary units (C or n)", fontsize=8.2, fontweight='bold', color=DARK_GREY, rotation=90, va='center')

    ax.annotate("", xy=(96, 16), xytext=(26, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.6))
    ax.text(61, 7, "Phases of the Mitotic Cell Cycle", fontsize=9.0, fontweight='bold', color=DARK_GREY, ha='center')

    # Y ticks: 2C / 2n, 4C / 4n
    ax.plot([24.5, 26], [42, 42], 'k-', lw=1.2)
    ax.text(23.5, 42, "2C (Diploid DNA)\n2n (46 chromosomes)", fontsize=6.8, fontweight='bold', color=NAVY, ha='right', va='center')

    ax.plot([24.5, 26], [76, 76], 'k-', lw=1.2)
    ax.text(23.5, 76, "4C (Replicated DNA)\n92 chromatids", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='right', va='center')

    # Phase vertical boundaries: G1: 26..40, S: 40..56, G2: 56..72, M: 72..88, C: 88..96
    phases_bounds = [
        ("G₁ Phase", 26, 40, "#eff6ff"),
        ("S Phase", 40, 56, "#f0fdf4"),
        ("G₂ Phase", 56, 72, "#fefce8"),
        ("Mitosis (M)", 72, 88, "#fef2f2"),
        ("Cytokinesis", 88, 96, "#faf5ff")
    ]

    for p_name, x0, x1, bg in phases_bounds:
        ax.add_patch(Rectangle((x0, 16), x1 - x0, 74, facecolor=bg, edgecolor="#cbd5e1", lw=0.6, alpha=0.6))
        ax.text((x0 + x1) / 2.0, 19, p_name, fontsize=7.6, fontweight='bold', color=DARK_GREY, ha='center')

    # Curve 1: DNA Mass (Solid Blue/Navy)
    dna_x = [26, 40, 56, 72, 88, 92, 96]
    dna_y = [42, 42, 76, 76, 76, 42, 42]
    ax.plot(dna_x, dna_y, color="#2563eb", lw=2.8, label="Mass of DNA per Cell (C)")

    # Curve 2: Number of Chromosomes (Dashed Crimson)
    chr_x = [26, 40, 56, 72, 80, 80.1, 88, 92, 96]
    chr_y = [42, 42, 42, 42, 42, 76, 76, 42, 42]
    ax.plot(chr_x, chr_y, color=CRIMSON, lw=2.2, linestyle='--', label="Number of Chromosomes per Cell")

    # Key explanatory annotations
    ax.annotate("S Phase: DNA replication\nDNA mass doubles (2C -> 4C)\nChromosome count remains 46\n(each has 2 sister chromatids)",
                xy=(48, 59), xytext=(28, 81),
                arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.2),
                fontsize=7.2, fontweight='bold', color="#1e40af",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor="#2563eb", lw=0.8))

    ax.annotate("Anaphase: Centromeres divide\nSister chromatids become individual\nchromosomes (temporarily 92)",
                xy=(80.1, 76), xytext=(57, 85),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.2, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef2f2", edgecolor=CRIMSON, lw=0.8))

    ax.annotate("Cytokinesis: Cell divides\nDNA mass & chromosome count\nhalved back to original 2C & 2n",
                xy=(92, 42), xytext=(72, 32),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2),
                fontsize=7.2, fontweight='bold', color=DARK_GREY)

    ax.legend(loc="lower left", bbox_to_anchor=(0.28, 0.22), fontsize=7.8, framealpha=0.92)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.4: THE FOUR MAIN STAGES OF MITOSIS (P-M-A-T)
# ==============================================================================
def generate_fig5_4(filename="fig5_4_mitosis_four_stages_diagram.png"):
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 4.4), dpi=300)
    stages = [
        ("1. PROPHASE", "Chromatin condenses;\nnuclear envelope breaks down"),
        ("2. METAPHASE", "Chromosomes align at equator;\nspindle fibers attach"),
        ("3. ANAPHASE", "Centromeres divide;\nchromatids pulled to poles"),
        ("4. TELOPHASE", "Chromosomes decondense;\nnuclear envelopes reform")
    ]

    for ax, (title, sub) in zip(axes, stages):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(title, fontsize=9.2, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 90, sub, fontsize=7.0, color=DARK_GREY, ha='center')

        # Cell border - Ellipse with width 74, height 40 counteracts 1x4 subplot vertical stretch
        cell = Ellipse((50, 53), 74, 40, facecolor="#f8fafc", edgecolor=NAVY, lw=1.5)
        ax.add_patch(cell)

    # Panel 1: Prophase
    axes[0].add_patch(Circle((24, 65), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    axes[0].add_patch(Circle((76, 65), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    # Disintegrating nuclear envelope
    axes[0].add_patch(Ellipse((50, 53), 50, 26, facecolor="#eff6ff", edgecolor=NAVY, lw=1.1, linestyle=':'))
    # Condensed chromosomes (X-shapes)
    for cx, cy in [(43, 58), (57, 56), (50, 45)]:
        axes[0].plot([cx-4, cx+4], [cy-4, cy+4], color="#2563eb", lw=2.4)
        axes[0].plot([cx-4, cx+4], [cy+4, cy-4], color="#2563eb", lw=2.4)
        axes[0].plot(cx, cy, 'o', color=AMBER, markersize=3.2)
    axes[0].text(50, 14, "• Centrosomes move to poles\n• Spindle begins assembly\n• Nucleolus disappears",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Panel 2: Metaphase
    axes[1].add_patch(Circle((20, 53), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    axes[1].add_patch(Circle((80, 53), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    for my in [43, 53, 63]:
        axes[1].plot([20, 50], [53, my], color="#94a3b8", lw=1.0, linestyle='--')
        axes[1].plot([80, 50], [53, my], color="#94a3b8", lw=1.0, linestyle='--')
        axes[1].plot([50, 50], [my-4, my+4], color="#2563eb", lw=2.6)
        axes[1].plot([47, 53], [my, my], color="#2563eb", lw=2.2)
        axes[1].plot(50, my, 'o', color=CRIMSON, markersize=3.6)
    axes[1].text(50, 14, "• Equator / Metaphase plate\n• Kinetochores attach to spindle\n• Max chromosome condensation",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Panel 3: Anaphase
    axes[2].add_patch(Circle((18, 53), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    axes[2].add_patch(Circle((82, 53), 2.5, facecolor=AMBER, edgecolor=NAVY, lw=0.9))
    for my in [43, 53, 63]:
        # Left moving
        axes[2].plot([18, 32], [53, my], color="#94a3b8", lw=0.9, linestyle='--')
        axes[2].plot([32, 38, 38], [my, my+3.5, my-3.5], color="#2563eb", lw=2.2)
        axes[2].plot(32, my, 'o', color=CRIMSON, markersize=3.0)
        # Right moving
        axes[2].plot([82, 68], [53, my], color="#94a3b8", lw=0.9, linestyle='--')
        axes[2].plot([68, 62, 62], [my, my+3.5, my-3.5], color="#2563eb", lw=2.2)
        axes[2].plot(68, my, 'o', color=CRIMSON, markersize=3.0)
    axes[2].text(50, 14, "• Centromeres divide\n• Spindle fibres shorten\n• Sister chromatids pulled to poles",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Panel 4: Telophase
    axes[3].add_patch(Ellipse((34, 53), 28, 34, facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    axes[3].add_patch(Ellipse((66, 53), 28, 34, facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    axes[3].plot([50, 50], [33, 40], color=CRIMSON, lw=2.0)
    axes[3].plot([50, 50], [66, 73], color=CRIMSON, lw=2.0)
    for nx in [34, 66]:
        axes[3].add_patch(Circle((nx, 53), 7.5, facecolor="#bfdbfe", edgecolor=NAVY, lw=0.9, linestyle='--'))
        axes[3].plot([nx-3.5, nx+3.5], [51, 55], color="#1e40af", lw=1.3)
        axes[3].plot([nx-3.0, nx+3.0], [55, 51], color="#1e40af", lw=1.3)
        axes[3].add_patch(Circle((nx+1.5, 54), 1.6, facecolor=NAVY, edgecolor="none"))
    axes[3].text(50, 14, "• Nuclear membranes reform\n• Nucleoli reappear\n• Chromosomes uncoil to chromatin",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.5: ROOT TIP SQUASH PHOTOMICROGRAPH & IDENTIFICATION (2-PANEL LAYOUT)
# ==============================================================================
def generate_fig5_5(filename="fig5_5_root_tip_squash_photomicrograph.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.8), gridspec_kw={'width_ratios': [1.1, 1.0]}, dpi=300)

    # Left: High-Power Microscopic Field
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Meristematic Cells (Allium Root Squash)", fontsize=9.8, fontweight='bold', color=NAVY, pad=4)

    # Microscope Field of View
    ax1.add_patch(Rectangle((4, 14), 92, 78, facecolor="#fdf2f8", edgecolor=NAVY, lw=1.6))

    # Grid of meristematic cells (6 columns x 4 rows)
    np.random.seed(42)
    stages_map = {
        (0, 0): "I", (0, 1): "I", (0, 2): "P", (0, 3): "I",
        (1, 0): "I", (1, 1): "M", (1, 2): "I", (1, 3): "A",
        (2, 0): "P", (2, 1): "I", (2, 2): "I", (2, 3): "T",
        (3, 0): "I", (3, 1): "A", (3, 2): "I", (3, 3): "I",
        (4, 0): "M", (4, 1): "I", (4, 2): "P", (4, 3): "I",
        (5, 0): "I", (5, 1): "I", (5, 2): "I", (5, 3): "I"
    }

    cw = 92 / 6.0
    ch = 78 / 4.0

    for col in range(6):
        for row in range(4):
            x = 4 + col * cw
            y = 14 + row * ch
            ax1.add_patch(Rectangle((x, y), cw, ch, facecolor="#fae8ff", edgecolor="#c084fc", lw=0.9))

            st = stages_map.get((col, row), "I")
            cx, cy = x + cw/2.0, y + ch/2.0

            if st == "I":
                ax1.add_patch(Circle((cx, cy), 5.5, facecolor="#c084fc", edgecolor=PURPLE, lw=0.9, alpha=0.7))
                ax1.add_patch(Circle((cx+1.2, cy+1.0), 1.5, facecolor="#581c87", edgecolor="none"))
            elif st == "P":
                for a in [0, 45, 90, 135]:
                    rad = np.deg2rad(a)
                    ax1.plot([cx - 4.2*np.cos(rad), cx + 4.2*np.cos(rad)],
                             [cy - 4.2*np.sin(rad), cy + 4.2*np.sin(rad)], color="#6b21a8", lw=1.9)
            elif st == "M":
                ax1.plot([cx-5.5, cx+5.5], [cy, cy], color="#581c87", lw=3.2)
                for tx in np.linspace(cx-4.5, cx+4.5, 5):
                    ax1.plot([tx, tx], [cy-1.8, cy+1.8], color="#3b0764", lw=1.6)
            elif st == "A":
                ax1.plot([cx-4.5, cx+4.5], [cy+3.0, cy+3.0], color="#581c87", lw=2.2)
                ax1.plot([cx-4.5, cx+4.5], [cy-3.0, cy-3.0], color="#581c87", lw=2.2)
            elif st == "T":
                ax1.add_patch(Circle((cx, cy+3.5), 3.2, facecolor="#d8b4fe", edgecolor=PURPLE, lw=0.8))
                ax1.add_patch(Circle((cx, cy-3.5), 3.2, facecolor="#d8b4fe", edgecolor=PURPLE, lw=0.8))
                ax1.plot([cx-4.5, cx+4.5], [cy, cy], color=GREEN, lw=1.3, linestyle='--')

    # Exemplar Badges (A, B, C, D, E) on specific cells
    exemplars = [
        ("A", 1, 3, CRIMSON),  # Anaphase
        ("B", 1, 1, NAVY),     # Metaphase
        ("C", 0, 2, PURPLE),   # Prophase
        ("D", 2, 3, GREEN),    # Telophase
        ("E", 5, 1, DARK_GREY) # Interphase
    ]

    for label, col, row, color in exemplars:
        bx = 4 + col * cw + 3.2
        by = 14 + (row + 1) * ch - 3.2
        ax1.add_patch(Circle((bx, by), 3.0, facecolor=color, edgecolor=WHITE, lw=1.0))
        ax1.text(bx, by, label, fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')

    ax1.text(50, 6, "Stain: Aceto-orcein (chromosomes stain purple-red)\nLabeled cells A-E correspond to stages in Table B",
             fontsize=7.2, color=DARK_GREY, ha='center')

    # Right: Stage Identification & Key Microscopic Features Table
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Stage Identification & Microscopic Features", fontsize=9.8, fontweight='bold', color=NAVY, pad=4)

    # Table Header
    ax2.add_patch(Rectangle((2, 84), 96, 9, facecolor=NAVY, edgecolor=NAVY))
    ax2.text(9, 88.5, "Cell", fontsize=7.6, fontweight='bold', color=WHITE, ha='center', va='center')
    ax2.text(28, 88.5, "Stage", fontsize=7.6, fontweight='bold', color=WHITE, ha='center', va='center')
    ax2.text(68, 88.5, "Diagnostic Microscopic Features", fontsize=7.6, fontweight='bold', color=WHITE, ha='center', va='center')

    rows_info = [
        ("A", "Anaphase", "Sister chromatids separated; pulled to poles (V-shaped)", CRIMSON),
        ("B", "Metaphase", "Condensed chromosomes aligned at equatorial plate", NAVY),
        ("C", "Prophase", "Chromatin condensed to visible threads; nucleolus gone", PURPLE),
        ("D", "Telophase", "Two daughter nuclei at poles; cell plate forming", GREEN),
        ("E", "Interphase", "Granular chromatin; intact envelope; visible nucleolus", DARK_GREY)
    ]

    for idx, (lbl, st_name, feat, colr) in enumerate(rows_info):
        y_r = 75 - idx * 9.5
        bg = "#f8fafc" if idx % 2 == 0 else WHITE
        ax2.add_patch(Rectangle((2, y_r - 3.5), 96, 9.0, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        ax2.add_patch(Circle((9, y_r + 1.0), 3.0, facecolor=colr, edgecolor=WHITE, lw=0.8))
        ax2.text(9, y_r + 1.0, lbl, fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')
        ax2.text(28, y_r + 1.0, st_name, fontsize=7.2, fontweight='bold', color=NAVY, ha='center', va='center')
        ax2.text(48, y_r + 1.0, feat, fontsize=6.5, color=DARK_GREY, ha='left', va='center')

    # Formula Box at bottom
    ax2.add_patch(Rectangle((2, 10), 96, 21, facecolor="#eff6ff", edgecolor=NAVY, lw=1.0))
    ax2.text(50, 24, "Mitotic Index (MI) Quantitative Formula:", fontsize=7.4, fontweight='bold', color=NAVY, ha='center')
    ax2.text(50, 18, r"$\mathbf{MI = \frac{\text{Number of cells in mitosis (P + M + A + T)}}{\text{Total number of cells observed}} \times 100\%}$",
             fontsize=7.2, color=CRIMSON, ha='center')
    ax2.text(50, 13, "Enables assessment of meristematic proliferation & tumour growth rate",
             fontsize=6.6, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.6: TELOMERE SHORTENING & CELLULAR SENESCENCE
# ==============================================================================
def generate_fig5_6(filename="fig5_6_telomere_shortening_senescence.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.6), dpi=300)

    # Left: End replication problem
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: The End-Replication Problem", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Leading strand vs Lagging strand (Okazaki fragment gap)
    ax1.plot([10, 85], [75, 75], color=NAVY, lw=2.2)
    ax1.text(8, 75, "3'", fontsize=8.0, fontweight='bold', color=NAVY, ha='right', va='center')
    ax1.text(87, 75, "5'", fontsize=8.0, fontweight='bold', color=NAVY, ha='left', va='center')
    ax1.text(50, 80, "Template DNA Strand", fontsize=7.8, color=NAVY, ha='center')

    ax1.plot([10, 68], [65, 65], color="#2563eb", lw=2.2)
    ax1.text(8, 65, "5'", fontsize=8.0, fontweight='bold', color="#2563eb", ha='right', va='center')
    ax1.text(70, 65, "3'", fontsize=8.0, fontweight='bold', color="#2563eb", ha='left', va='center')
    ax1.text(40, 60, "Newly synthesised daughter strand", fontsize=7.4, color="#2563eb", ha='center')

    # RNA primer removed leaves gap
    ax1.plot([68, 85], [65, 65], color=CRIMSON, lw=1.8, linestyle=':')
    ax1.annotate("Unreplicated End Gap\nRNA primer removed;\nDNA polymerase cannot\nextend without 3'-OH",
                 xy=(77, 65), xytext=(50, 40),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                 fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CRIMSON, lw=0.9))

    ax1.text(50, 12, "Telomeres act as non-coding buffers (TTAGGG repeats):\nEnd shortening consumes telomeric repeats instead of vital coding genes.",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Right: Hayflick limit vs Telomerase graph
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Telomere Length vs Number of Cell Divisions", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Axes
    ax2.annotate("", xy=(12, 90), xytext=(12, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax2.text(6, 52, "Telomere Length / kilobases (kb)", fontsize=8.5, fontweight='bold', color=DARK_GREY, rotation=90, va='center')

    ax2.annotate("", xy=(94, 16), xytext=(12, 16), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax2.text(54, 7, "Number of Cell Divisions (Rounds of Mitosis)", fontsize=8.8, fontweight='bold', color=DARK_GREY, ha='center')

    # Normal somatic cell curve (steady decline to senescence)
    divs = np.linspace(12, 70, 50)
    normal_t = 82 - 0.85 * (divs - 12)
    ax2.plot(divs, normal_t, color=CRIMSON, lw=2.4, label="Normal Somatic Cells (Telomerase -)")

    # Cancer / Stem cell curve (maintained by telomerase)
    cancer_divs = np.linspace(12, 90, 50)
    cancer_t = 82 * np.ones_like(cancer_divs)
    ax2.plot(cancer_divs, cancer_t, color=GREEN, lw=2.4, label="Stem / Cancer Cells (Telomerase +)")

    # Hayflick limit threshold
    ax2.plot([12, 92], [32, 32], 'k--', lw=1.2, alpha=0.8)
    ax2.text(14, 35, "Hayflick Limit / Critical Shortening Threshold (~50 divisions)", fontsize=7.4, fontweight='bold', color=DARK_GREY)

    ax2.annotate("Cellular Senescence / Apoptosis\n(p53 triggered DNA damage arrest)",
                 xy=(70, 32), xytext=(65, 48),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                 fontsize=7.4, fontweight='bold', color=CRIMSON)

    ax2.annotate("Active Telomerase maintains\ntelomere length -> Replicative immortality",
                 xy=(55, 82), xytext=(45, 68),
                 arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1),
                 fontsize=7.4, fontweight='bold', color=GREEN)

    ax2.legend(loc="lower left", bbox_to_anchor=(0.14, 0.20), fontsize=7.6, framealpha=0.92)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.7: STEM CELL POTENCY HIERARCHY & DIFFERENTIATION
# ==============================================================================
def generate_fig5_7(filename="fig5_7_stem_cell_hierarchy_potency.png"):
    fig, ax = plt.subplots(figsize=(9.2, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "The Hierarchy of Stem Cell Potency & Lineage Differentiation",
            fontsize=10.8, fontweight='bold', color=NAVY, ha='center')

    # Level 1: Totipotent (Zygote)
    b1 = FancyBboxPatch((20, 76), 60, 17, boxstyle="round,pad=0.3", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.3)
    ax.add_patch(b1)
    ax.text(50, 88.5, "TOTIPOTENT STEM CELL", fontsize=8.2, fontweight='bold', color=CRIMSON, ha='center')
    ax.text(50, 83.5, "Zygote & Early Cleavage Morula (up to 8 cells)", fontsize=7.0, color=DARK_GREY, ha='center')
    ax.text(50, 78.5, "Can form ALL embryonic tissues + placenta & extraembryonic membranes", fontsize=6.8, color=DARK_GREY, ha='center')

    ax.annotate("", xy=(50, 68), xytext=(50, 76), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.6))

    # Level 2: Pluripotent (Blastocyst ICM)
    b2 = FancyBboxPatch((15, 47), 70, 20, boxstyle="round,pad=0.3", facecolor="#fef3c7", edgecolor=AMBER, lw=1.3)
    ax.add_patch(b2)
    ax.text(50, 62.5, "PLURIPOTENT STEM CELL", fontsize=8.2, fontweight='bold', color="#854d0e", ha='center')
    ax.text(50, 56.5, "Inner Cell Mass (ICM) of Blastocyst (Embryonic Stem Cells)", fontsize=7.1, color=DARK_GREY, ha='center')
    ax.text(50, 50.5, "Can differentiate into ALL somatic cell lineages (ectoderm, mesoderm, endoderm)\nCannot form extraembryonic placenta or chorion", fontsize=6.7, color=DARK_GREY, ha='center')

    ax.annotate("", xy=(22, 38), xytext=(35, 47), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.4))
    ax.annotate("", xy=(78, 38), xytext=(65, 47), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.4))

    # Level 3: Multipotent (Adult Stem Cells)
    # Left: Hematopoietic Stem Cell
    b3a = FancyBboxPatch((4, 22), 38, 16, boxstyle="round,pad=0.3", facecolor="#e0e7ff", edgecolor="#4338ca", lw=1.2)
    ax.add_patch(b3a)
    ax.text(23, 33.5, "MULTIPOTENT: Bone Marrow HSC", fontsize=7.8, fontweight='bold', color="#312e81", ha='center')
    ax.text(23, 26.5, "Hematopoietic stem cell produces limited lineages:\nErythrocytes, neutrophils, lymphocytes, platelets", fontsize=6.7, color=DARK_GREY, ha='center')

    # Right: Epidermal / Neural Stem Cell
    b3b = FancyBboxPatch((58, 22), 38, 16, boxstyle="round,pad=0.3", facecolor="#dcfce7", edgecolor=GREEN, lw=1.2)
    ax.add_patch(b3b)
    ax.text(77, 33.5, "MULTIPOTENT: Epidermal / Neural", fontsize=7.8, fontweight='bold', color="#14532d", ha='center')
    ax.text(77, 26.5, "Basal layer skin stem cells replace keratinocytes;\nNeural stem cells form neurons, astrocytes, glia", fontsize=6.7, color=DARK_GREY, ha='center')

    # Down to Unipotent / Terminally Differentiated
    ax.annotate("", xy=(23, 14), xytext=(23, 22), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.4))
    ax.annotate("", xy=(77, 14), xytext=(77, 22), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.4))

    b4a = FancyBboxPatch((4, 4), 38, 10, boxstyle="round,pad=0.3", facecolor="#f1f5f9", edgecolor=MID_GREY, lw=0.9)
    ax.add_patch(b4a)
    ax.text(23, 9, "Terminally Differentiated Blood Cells\n(Erythrocytes, Phagocytes, Lymphocytes)", fontsize=7.0, fontweight='bold', color=DARK_GREY, ha='center')

    b4b = FancyBboxPatch((58, 4), 38, 10, boxstyle="round,pad=0.3", facecolor="#f1f5f9", edgecolor=MID_GREY, lw=0.9)
    ax.add_patch(b4b)
    ax.text(77, 9, "Terminally Differentiated Somatic Cells\n(Mature Keratinocytes, Motor Neurons)", fontsize=7.0, fontweight='bold', color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.8: CARCINOGENESIS & TUMOUR FORMATION
# ==============================================================================
def generate_fig5_8(filename="fig5_8_carcinogenesis_tumour_formation.png"):
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 4.4), dpi=300)
    steps = [
        ("Step 1: Oncogenic Mutation", "Carcinogen induces mutation in\nproto-oncogene or tumour suppressor"),
        ("Step 2: Hyperplasia", "Uncontrolled mitotic division;\nloss of contact inhibition"),
        ("Step 3: Angiogenesis", "VEGF secretion stimulates new\nblood vessel growth to supply tumour"),
        ("Step 4: Metastasis", "Malignant cells invade blood/lymph\nand colonise secondary tissues")
    ]

    for ax, (title, sub) in zip(axes, steps):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(title, fontsize=8.8, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 89, sub, fontsize=6.8, color=DARK_GREY, ha='center')

        # Basement membrane at y=34
        ax.plot([0, 100], [34, 34], color=MID_GREY, lw=1.6)

    axes[0].text(50, 27, "Basement Membrane", fontsize=6.4, color=MID_GREY, ha='center')
    axes[1].text(50, 27, "Basement Membrane", fontsize=6.4, color=MID_GREY, ha='center')

    # Step 1: Single mutant cell
    for x in range(15, 90, 15):
        axes[0].add_patch(Circle((x, 42), 5.0, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.0))
    axes[0].add_patch(Circle((45, 42), 5.0, facecolor="#f87171", edgecolor=CRIMSON, lw=1.4))
    axes[0].text(45, 42, "*", fontsize=9.0, fontweight='bold', color=WHITE, ha='center', va='center')
    axes[0].annotate("Mutant Cell\n(e.g. TP53)", xy=(45, 47), xytext=(45, 62),
                     arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                     fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
    axes[0].text(50, 7, "• DNA damage bypasses G1/S check\n• Proto-oncogene -> Oncogene\n• Failure of apoptosis",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Step 2: Benign mass (Hyperplasia)
    for x, y in [(30, 41), (42, 41), (54, 41), (66, 41), (36, 50), (48, 50), (60, 50), (42, 59), (54, 59)]:
        axes[1].add_patch(Circle((x, y), 4.8, facecolor="#f87171", edgecolor=CRIMSON, lw=1.0))
    axes[1].text(48, 69, "Benign Tumour", fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center')
    axes[1].text(50, 7, "• Encapsulated growth\n• Confined within membrane\n• Does not invade surrounding tissues",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Step 3: Angiogenesis
    for x, y in [(25, 41), (37, 41), (49, 41), (61, 41), (73, 41), (31, 50), (43, 50), (55, 50), (67, 50), (37, 59), (49, 59), (61, 59)]:
        axes[2].add_patch(Circle((x, y), 4.8, facecolor="#ef4444", edgecolor=CRIMSON, lw=1.0))
    # Capillary vessel below membrane (y=16..22)
    axes[2].add_patch(Rectangle((5, 16), 90, 7, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.0))
    axes[2].text(50, 19.5, "Capillary Bed", fontsize=6.4, fontweight='bold', color=CRIMSON, ha='center', va='center')
    # Capillary sprouting lines into tumour base
    axes[2].plot([30, 40, 45], [23, 29, 36], color=CRIMSON, lw=2.0)
    axes[2].plot([70, 60, 55], [23, 29, 36], color=CRIMSON, lw=2.0)
    axes[2].text(50, 69, "Angiogenesis (VEGF)", fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center')
    axes[2].text(50, 7, "• VEGF secreted by tumour cells\n• Capillary sprouting fuels growth\n• Delivers O₂ & glucose; removes waste",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    # Step 4: Malignant Invasion & Metastasis
    axes[3].plot([0, 38], [34, 34], color=MID_GREY, lw=1.6)
    axes[3].plot([62, 100], [34, 34], color=MID_GREY, lw=1.6)
    # Blood vessel underneath
    axes[3].add_patch(Rectangle((0, 15), 100, 10, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.1))
    axes[3].text(22, 20, "Capillary Lumen", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center', va='center')
    # Tumour cells breaching
    for x, y in [(40, 42), (52, 42), (46, 51), (58, 51), (50, 33), (50, 20), (78, 20)]:
        axes[3].add_patch(Circle((x, y), 4.2, facecolor="#dc2626", edgecolor=NAVY, lw=0.9))
    axes[3].annotate("Extravasation", xy=(78, 24), xytext=(66, 44),
                     arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.1),
                     fontsize=6.8, fontweight='bold', color=CRIMSON)
    axes[3].text(50, 69, "Malignancy & Metastasis", fontsize=7.4, fontweight='bold', color=CRIMSON, ha='center')
    axes[3].text(50, 7, "• Intravasation into bloodstream\n• Circulates to secondary sites\n• Extravasation forms metastases",
                 fontsize=6.8, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.9: CYTOKINESIS IN ANIMAL VS PLANT CELLS
# ==============================================================================
def generate_fig5_9(filename="fig5_9_cytokinesis_animal_vs_plant.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.4), dpi=300)

    # Left: Animal Cell Cytokinesis (Cleavage Furrow)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Animal Cell Cytokinesis (Cleavage Furrow)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Constricted animal cell boundary
    ax1.add_patch(Ellipse((28, 50), 34, 44, facecolor="#eff6ff", edgecolor=NAVY, lw=1.6))
    ax1.add_patch(Ellipse((72, 50), 34, 44, facecolor="#eff6ff", edgecolor=NAVY, lw=1.6))
    ax1.add_patch(Circle((28, 50), 10, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax1.add_patch(Circle((72, 50), 10, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax1.text(28, 50, "Daughter\nNucleus", fontsize=7.2, color=NAVY, ha='center', va='center')
    ax1.text(72, 50, "Daughter\nNucleus", fontsize=7.2, color=NAVY, ha='center', va='center')

    # Contractile ring arrows pinching inward
    ax1.annotate("", xy=(50, 40), xytext=(50, 18), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.0))
    ax1.annotate("", xy=(50, 60), xytext=(50, 82), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.0))
    ax1.text(50, 87, "Cleavage Furrow", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center')

    ax1.text(50, 8, "• Contractile ring of actin microfilaments & myosin\n• Pinches plasma membrane inward (centripetal direction)\n• Cleaves parent cell into two separate daughter cells",
             fontsize=7.4, color=DARK_GREY, ha='center')

    # Right: Plant Cell Cytokinesis (Cell Plate Formation)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Plant Cell Cytokinesis (Cell Plate Formation)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Rigid rectangular plant cell wall
    ax2.add_patch(Rectangle((8, 20), 84, 60, facecolor="#f0fdf4", edgecolor="#15803d", lw=2.2))
    ax2.add_patch(Circle((26, 50), 10, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.1))
    ax2.add_patch(Circle((74, 50), 10, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.1))
    ax2.text(26, 50, "Daughter\nNucleus", fontsize=7.2, color="#14532d", ha='center', va='center')
    ax2.text(74, 50, "Daughter\nNucleus", fontsize=7.2, color="#14532d", ha='center', va='center')

    # Golgi-derived vesicles coalescing at equator
    for vy in range(25, 76, 7):
        ax2.add_patch(Circle((50, vy), 2.4, facecolor=AMBER, edgecolor="#ca8a04", lw=0.9))
    ax2.annotate("", xy=(50, 78), xytext=(50, 22), arrowprops=dict(arrowstyle="<->", color=AMBER, lw=1.8))
    ax2.text(50, 86, "Cell Plate (Phragmoplast)", fontsize=8.0, fontweight='bold', color="#854d0e", ha='center')

    ax2.text(50, 8, "• Golgi-derived vesicles containing pectins & cellulose\n• Coalesce outward from centre (centrifugal direction)\n• Forms middle lamella and primary cell walls; no pinching",
             fontsize=7.4, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.10: KINETOCHORE ULTRASTRUCTURE & SPINDLE MICROTUBULE ATTACHMENT
# ==============================================================================
def generate_fig5_10(filename="fig5_10_kinetochore_spindle_microtubules.png"):
    fig, ax = plt.subplots(figsize=(8.8, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Ultrastructure of Kinetochore-Microtubule Attachment at the Centromere",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Centromeric Heterochromatin block at centre
    ax.add_patch(FancyBboxPatch((38, 20), 24, 60, boxstyle="round,pad=0.5", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.6))
    ax.text(50, 50, "Centromeric\nDNA\n(Heterochromatin)", fontsize=8.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # Left Kinetochore complex
    ax.add_patch(Rectangle((32, 35), 6, 30, facecolor=CRIMSON, edgecolor=NAVY, lw=1.2))
    ax.text(35, 50, "Inner\nPlate", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center', rotation=90)
    ax.add_patch(Rectangle((26, 33), 6, 34, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.2))
    ax.text(29, 50, "Outer Plate\n(Corona)", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center', va='center', rotation=90)

    # Right Kinetochore complex
    ax.add_patch(Rectangle((62, 35), 6, 30, facecolor=CRIMSON, edgecolor=NAVY, lw=1.2))
    ax.text(65, 50, "Inner\nPlate", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center', rotation=90)
    ax.add_patch(Rectangle((68, 33), 6, 34, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.2))
    ax.text(71, 50, "Outer Plate\n(Corona)", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center', va='center', rotation=90)

    # Spindle Microtubules extending to poles
    # Left bundles (to Left Pole)
    for my in [38, 44, 50, 56, 62]:
        ax.plot([5, 26], [my, my], color="#0284c7", lw=2.2)
        # alpha/beta tubulin heterodimer indication
        for tx in range(8, 25, 4):
            ax.plot(tx, my, 'o', color="#38bdf8", markersize=3.0)

    # Right bundles (to Right Pole)
    for my in [38, 44, 50, 56, 62]:
        ax.plot([74, 95], [my, my], color="#0284c7", lw=2.2)
        for tx in range(76, 93, 4):
            ax.plot(tx, my, 'o', color="#38bdf8", markersize=3.0)

    ax.text(5, 72, "<- To Spindle Pole A\n(Centrosome / Aster)", fontsize=7.6, fontweight='bold', color="#0369a1")
    ax.text(95, 72, "To Spindle Pole B ->\n(Centrosome / Aster)", fontsize=7.6, fontweight='bold', color="#0369a1", ha='right')

    ax.annotate("Kinetochore Microtubules (K-fibres)\nFormed from alpha & beta tubulin dimers",
                xy=(18, 56), xytext=(22, 85),
                arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.2),
                fontsize=7.8, fontweight='bold', color="#0284c7")

    ax.annotate("Motor proteins (dynein/kinesin) & depolymerisation\nof tubulin subunits pull sister chromatids to poles",
                xy=(82, 50), xytext=(55, 12),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=7.8, fontweight='bold', color=CRIMSON)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.11: CHEMOTHERAPEUTIC MITOTIC INHIBITORS (COLCHICINE VS TAXOL)
# ==============================================================================
def generate_fig5_11(filename="fig5_11_mitotic_inhibitors_microtubule_poisons.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.4), dpi=300)

    # Left: Colchicine / Vincristine (Inhibits Tubulin Polymerisation)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Colchicine / Vinca Alkaloids (Vincristine)", fontsize=9.4, fontweight='bold', color=CRIMSON, pad=4)

    # Free tubulin heterodimers blocked from assembling
    ax1.text(50, 88, "Mechanism: Prevents Microtubule Assembly", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center')

    # Spindle pole
    ax1.add_patch(Circle((15, 50), 4.0, facecolor=AMBER, edgecolor=NAVY, lw=1.1))
    ax1.text(15, 42, "Centrosome", fontsize=7.0, color=DARK_GREY, ha='center')

    # Fragmented short microtubule stub
    ax1.plot([19, 36], [50, 50], color="#94a3b8", lw=2.4)
    ax1.plot([36, 40], [50, 50], color=CRIMSON, lw=2.6, linestyle=':')

    # Blocked free subunits floating around with inhibitor drug binding
    for dx, dy in [(45, 65), (60, 55), (52, 40), (70, 70), (75, 45), (65, 30)]:
        ax1.add_patch(Circle((dx, dy), 3.0, facecolor="#67e8f9", edgecolor="#0e7490", lw=0.9))
        ax1.add_patch(Circle((dx+2, dy), 1.8, facecolor=CRIMSON, edgecolor=NAVY, lw=0.7))

    ax1.annotate("Colchicine binds free tubulin dimers;\nblocks spindle microtubule elongation",
                 xy=(54, 40), xytext=(50, 22),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                 fontsize=7.6, color=CRIMSON, fontweight='bold', ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CRIMSON, lw=0.8))

    ax1.text(50, 8, "Consequence: No mitotic spindle formed;\ncells arrested in metaphase; prevents division",
             fontsize=7.2, color=DARK_GREY, ha='center')

    # Right: Paclitaxel / Taxol (Prevents Depolymerisation)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Taxanes (Paclitaxel / Taxol)", fontsize=9.4, fontweight='bold', color="#1e40af", pad=4)

    ax2.text(50, 88, "Mechanism: Freezes Microtubule Disassembly", fontsize=8.0, fontweight='bold', color="#1e40af", ha='center')

    # Spindle pole and frozen hyper-stable microtubules
    ax2.add_patch(Circle((15, 50), 4.0, facecolor=AMBER, edgecolor=NAVY, lw=1.1))
    ax2.text(15, 42, "Centrosome", fontsize=7.0, color=DARK_GREY, ha='center')

    for my in [36, 50, 64]:
        ax2.plot([19, 80], [50, my], color="#2563eb", lw=2.4)
        for tx in range(25, 75, 12):
            ax2.add_patch(Rectangle((tx, my-1.5), 4, 3, facecolor="#fde047", edgecolor="#ca8a04", lw=0.6))

    ax2.annotate("Taxol binds and stabilises microtubule polymer;\nprevents depolymerisation during anaphase",
                 xy=(55, 50), xytext=(50, 22),
                 arrowprops=dict(arrowstyle="->", color="#1e40af", lw=1.2),
                 fontsize=7.6, color="#1e40af", fontweight='bold', ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor="#2563eb", lw=0.8))

    ax2.text(50, 8, "Consequence: Spindle cannot shorten;\nchromatids cannot separate to poles; apoptosis",
             fontsize=7.2, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.12: MITOTIC INDEX COUNTING GRID WITH TALLY TABLE
# ==============================================================================
def generate_fig5_12(filename="fig5_12_mitotic_index_grid_counting.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.6), dpi=300)

    # Left: Grid View
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Meristem High-Power Field (Counting Grid)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Grid box from y=12 to y=88 (height 76, width 88)
    ax1.add_patch(Rectangle((6, 12), 88, 76, facecolor="#faf5ff", edgecolor=NAVY, lw=1.6))

    # 5x5 sub-grid
    step_x = 88 / 5.0
    step_y = 76 / 5.0
    for i in range(1, 5):
        ax1.plot([6 + i * step_x, 6 + i * step_x], [12, 88], color="#cbd5e1", lw=0.8, linestyle='--')
        ax1.plot([6, 94], [12 + i * step_y, 12 + i * step_y], color="#cbd5e1", lw=0.8, linestyle='--')

    # Draw 25 sample cells with symbols
    cell_types = [
        ("I", 0, 0), ("I", 0, 1), ("P", 0, 2), ("I", 0, 3), ("I", 0, 4),
        ("I", 1, 0), ("M", 1, 1), ("I", 1, 2), ("I", 1, 3), ("P", 1, 4),
        ("I", 2, 0), ("I", 2, 1), ("A", 2, 2), ("I", 2, 3), ("I", 2, 4),
        ("I", 3, 0), ("P", 3, 1), ("I", 3, 2), ("T", 3, 3), ("I", 3, 4),
        ("I", 4, 0), ("I", 4, 1), ("I", 4, 2), ("I", 4, 3), ("I", 4, 4)
    ]

    for st, r, c in cell_types:
        cx = 6 + (c + 0.5) * step_x
        cy = 12 + (r + 0.5) * step_y

        if st == "I":
            ax1.add_patch(Circle((cx, cy), 4.2, facecolor="#c084fc", edgecolor=PURPLE, lw=0.9, alpha=0.6))
            ax1.text(cx, cy, "I", fontsize=6.8, fontweight='bold', color="#4c1d95", ha='center', va='center')
        elif st == "P":
            ax1.add_patch(Rectangle((cx-4.2, cy-4.2), 8.4, 8.4, facecolor="#fde047", edgecolor="#ca8a04", lw=1.1))
            ax1.text(cx, cy, "P", fontsize=6.8, fontweight='bold', color="#854d0e", ha='center', va='center')
        elif st == "M":
            ax1.add_patch(Circle((cx, cy), 4.4, facecolor="#f87171", edgecolor=CRIMSON, lw=1.2))
            ax1.text(cx, cy, "M", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')
        elif st == "A":
            poly_tri = Polygon([(cx, cy+4.5), (cx-4.5, cy-4), (cx+4.5, cy-4)], closed=True, facecolor="#60a5fa", edgecolor=NAVY, lw=1.1)
            ax1.add_patch(poly_tri)
            ax1.text(cx, cy-1, "A", fontsize=6.5, fontweight='bold', color=WHITE, ha='center', va='center')
        elif st == "T":
            poly_dia = Polygon([(cx, cy+4.5), (cx-4.5, cy), (cx, cy-4.5), (cx+4.5, cy)], closed=True, facecolor="#4ade80", edgecolor=GREEN, lw=1.1)
            ax1.add_patch(poly_dia)
            ax1.text(cx, cy, "T", fontsize=6.8, fontweight='bold', color="#14532d", ha='center', va='center')

    ax1.text(50, 5, "Total Sampled Cells in Grid Field = 25 (6 Dividing + 19 Interphase)", fontsize=7.6, fontweight='bold', color=NAVY, ha='center')

    # Right: Quantitative Calculation & Tally Table
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Phase Distribution & Mitotic Index Data", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    headers = ["Stage", "Tally Count", "% of Cells", "Duration (24 h)"]
    cols_x = [16, 38, 60, 82]

    ax2.add_patch(Rectangle((2, 76), 96, 9, facecolor=NAVY, edgecolor=NAVY))
    for h, x in zip(headers, cols_x):
        ax2.text(x, 80.5, h, fontsize=7.2, fontweight='bold', color=WHITE, ha='center', va='center')

    rows = [
        ("Interphase (I)", "19", "76.0%", "18.24 h"),
        ("Prophase (P)",   "3",  "12.0%", "2.88 h"),
        ("Metaphase (M)",  "1",  "4.0%",  "0.96 h"),
        ("Anaphase (A)",   "1",  "4.0%",  "0.96 h"),
        ("Telophase (T)",  "1",  "4.0%",  "0.96 h"),
        ("TOTAL",          "25", "100.0%","24.00 h")
    ]

    for idx, (st, tc, pct, tm) in enumerate(rows):
        y_pos = 69.5 - idx * 6.8
        bg = "#eff6ff" if idx == 5 else ("#f8fafc" if idx % 2 == 0 else WHITE)
        ax2.add_patch(Rectangle((2, y_pos - 2.8), 96, 6.4, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        fw = 'bold' if idx == 5 else 'normal'
        fc = CRIMSON if idx == 5 else DARK_GREY
        ax2.text(cols_x[0], y_pos + 0.4, st, fontsize=7.0, fontweight=fw, color=fc, ha='center')
        ax2.text(cols_x[1], y_pos + 0.4, tc, fontsize=7.0, fontweight=fw, color=fc, ha='center')
        ax2.text(cols_x[2], y_pos + 0.4, pct, fontsize=7.0, fontweight=fw, color=fc, ha='center')
        ax2.text(cols_x[3], y_pos + 0.4, tm, fontsize=7.0, fontweight=fw, color=fc, ha='center')

    # Formula Box cleanly positioned below table
    calc_text = "Calculation of Mitotic Index (MI):\nMI = (P + M + A + T) / Total Cells × 100%\nMI = (3 + 1 + 1 + 1) / 25 × 100% = 6 / 25 × 100% = 24.0%\nStage Duration = (% of cells / 100) × 24.0 h"
    ax2.text(50, 14, calc_text, fontsize=7.2, fontweight='bold', color=NAVY, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.4", facecolor="#eff6ff", edgecolor=NAVY, lw=0.9))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.13: CENTROSOME & CENTRIOLE DUPLICATION CYCLE
# ==============================================================================
def generate_fig5_13(filename="fig5_13_centrosome_centriole_duplication.png"):
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 4.2), dpi=300)
    steps = [
        ("G₁ Phase: 1 Centrosome", "Pair of perpendicular\ncentrioles (9x3 triplets)"),
        ("S Phase: Duplication", "Procentrioles bud at right\nangles to mother centrioles"),
        ("G₂ Phase: Maturation", "Centrosomes separate &\naccumulate pericentriolar PCM"),
        ("Prophase: Bipolar Spindle", "Migrate to opposite poles;\nradial aster microtubules form")
    ]

    for ax, (title, sub) in zip(axes, steps):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(title, fontsize=8.8, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 88, sub, fontsize=6.8, color=DARK_GREY, ha='center')

    # Step 1: Single centrosome (mother + daughter centriole perpendicular)
    axes[0].add_patch(Rectangle((42, 42), 6, 20, facecolor=AMBER, edgecolor=NAVY, lw=1.2))
    axes[0].add_patch(Rectangle((50, 48), 18, 6, facecolor=AMBER, edgecolor=NAVY, lw=1.2))
    axes[0].add_patch(Circle((50, 52), 16, facecolor="#fef3c7", edgecolor=AMBER, lw=1.0, linestyle='--', alpha=0.4))
    axes[0].text(50, 22, "Centrosome: 2 Centrioles\nMTOC in animal cells;\nabsent in higher plant cells",
                 fontsize=7.0, color=DARK_GREY, ha='center')

    # Step 2: S phase budding procentrioles
    axes[1].add_patch(Rectangle((38, 42), 6, 20, facecolor=AMBER, edgecolor=NAVY, lw=1.2))
    axes[1].add_patch(Rectangle((46, 48), 18, 6, facecolor=AMBER, edgecolor=NAVY, lw=1.2))
    # Buds
    axes[1].add_patch(Rectangle((38, 64), 6, 9, facecolor=CRIMSON, edgecolor=NAVY, lw=1.0))
    axes[1].add_patch(Rectangle((66, 48), 9, 6, facecolor=CRIMSON, edgecolor=NAVY, lw=1.0))
    axes[1].text(50, 22, "Centrioles duplicate in S phase\nsynchronously with DNA;\nprocentriole elongation",
                 fontsize=7.0, color=DARK_GREY, ha='center')

    # Step 3: G2 phase two mature centrosomes
    # Centrosome 1
    axes[2].add_patch(Rectangle((26, 46), 5, 16, facecolor=AMBER, edgecolor=NAVY, lw=1.0))
    axes[2].add_patch(Rectangle((32, 50), 14, 5, facecolor=AMBER, edgecolor=NAVY, lw=1.0))
    axes[2].add_patch(Circle((32, 54), 12, facecolor="#fef3c7", edgecolor=AMBER, lw=0.9, linestyle='--', alpha=0.4))
    # Centrosome 2
    axes[2].add_patch(Rectangle((62, 46), 5, 16, facecolor=AMBER, edgecolor=NAVY, lw=1.0))
    axes[2].add_patch(Rectangle((68, 50), 14, 5, facecolor=AMBER, edgecolor=NAVY, lw=1.0))
    axes[2].add_patch(Circle((68, 54), 12, facecolor="#fef3c7", edgecolor=AMBER, lw=0.9, linestyle='--', alpha=0.4))
    axes[2].text(50, 22, "PCM recruitment;\nprotein kinase activation;\nprepares for separation",
                 fontsize=7.0, color=DARK_GREY, ha='center')

    # Step 4: Prophase bipolar spindle poles
    # Pole 1 (Left)
    axes[3].add_patch(Circle((18, 52), 4.5, facecolor=AMBER, edgecolor=NAVY, lw=1.1))
    for a in range(0, 360, 45):
        rad = np.deg2rad(a)
        axes[3].plot([18, 18 + 12*np.cos(rad)], [52, 52 + 12*np.sin(rad)], color="#38bdf8", lw=1.1)

    # Pole 2 (Right)
    axes[3].add_patch(Circle((82, 52), 4.5, facecolor=AMBER, edgecolor=NAVY, lw=1.1))
    for a in range(0, 360, 45):
        rad = np.deg2rad(a)
        axes[3].plot([82, 82 + 12*np.cos(rad)], [52, 52 + 12*np.sin(rad)], color="#38bdf8", lw=1.1)

    # Spindle fibres meeting
    for y in [46, 52, 58]:
        axes[3].plot([18, 82], [52, y], color="#0284c7", lw=1.5, linestyle='--')
    axes[3].text(50, 22, "Bipolar spindle apparatus;\nensures equal segregation\nof sister chromatids",
                 fontsize=7.0, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 5.14: CELL CYCLE CONTROL & CYCLIN-CDK CHECKPOINT REGULATION
# ==============================================================================
def generate_fig5_14(filename="fig5_14_cell_cycle_checkpoints_cyclin_cdk.png"):
    fig, ax = plt.subplots(figsize=(9.2, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Molecular Control of the Mitotic Cell Cycle: Cyclin-CDK Complexes & Checkpoint Cascades",
            fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

    # Three major checkpoint panels side-by-side
    panels = [
        ("G₁ / S Checkpoint (Restriction)", 4, 32, "#eff6ff", NAVY),
        ("G₂ / M Checkpoint (Entry to Mitosis)", 36, 64, "#fefce8", "#854d0e"),
        ("M Checkpoint (Spindle Assembly SAC)", 68, 96, "#fef2f2", CRIMSON)
    ]

    for title, x0, x1, bg, tc in panels:
        w = x1 - x0
        ax.add_patch(FancyBboxPatch((x0, 12), w, 78, boxstyle="round,pad=0.5", facecolor=bg, edgecolor=tc, lw=1.3))
        ax.text((x0 + x1) / 2.0, 84, title, fontsize=8.2, fontweight='bold', color=tc, ha='center')

    # Panel 1 details: G1/S Checkpoint
    ax.text(18, 74, "Key Regulators:\nCyclin D/E + CDK4/2\np53 & Retinoblastoma (Rb)", fontsize=7.4, fontweight='bold', color=NAVY, ha='center')
    ax.text(18, 52, "• DNA damage triggers p53\n• p53 activates p21 (CDK inhibitor)\n• Prevents Rb phosphorylation\n• E2F transcription factor stays blocked\n• Cell cycle halts in G₁",
            fontsize=7.0, color=DARK_GREY, ha='center')
    ax.text(18, 22, "Significance in Cancer:\n>50% human tumours carry\nloss-of-function TP53 mutations",
            fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center',
            bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE, edgecolor=CRIMSON, lw=0.7))

    # Panel 2 details: G2/M Checkpoint
    ax.text(50, 74, "Key Regulators:\nCyclin B + CDK1\n(Maturation Promoting Factor - MPF)", fontsize=7.4, fontweight='bold', color="#854d0e", ha='center')
    ax.text(50, 52, "• Verifies complete DNA replication\n• Checks for double-strand breaks\n• Wee1 vs Cdc25 phosphatase control\n• Active MPF phosphorylates:\n  - Lamins -> Nuclear envelope breakdown\n  - Condensins -> Chromatin packaging",
            fontsize=7.0, color=DARK_GREY, ha='center')
    ax.text(50, 22, "Outcome:\nIrreparable DNA damage initiates\napoptosis (programmed cell death)",
            fontsize=7.0, fontweight='bold', color="#854d0e", ha='center',
            bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE, edgecolor="#ca8a04", lw=0.7))

    # Panel 3 details: Spindle Assembly Checkpoint (SAC)
    ax.text(82, 74, "Key Regulators:\nMAD2, BUBR1, APC/C\n(Anaphase-Promoting Complex)", fontsize=7.4, fontweight='bold', color=CRIMSON, ha='center')
    ax.text(82, 52, "• Unattached kinetochores recruit MAD2\n• MAD2 inhibits APC/C activator Cdc20\n• When ALL kinetochores have tension:\n  - APC/C ubiquitylates Securin\n  - Active Separase cleaves Cohesin rings\n  - Sister chromatids separate!",
            fontsize=7.0, color=DARK_GREY, ha='center')
    ax.text(82, 22, "Biological Importance:\nPrevents lagging chromosomes,\naneuploidy & nondisjunction",
            fontsize=7.0, fontweight='bold', color=GREEN, ha='center',
            bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE, edgecolor=GREEN, lw=0.7))

    ax.text(50, 4, "Normal tissue homeostasis requires strict balance between cell proliferation (mitosis) and apoptosis",
            fontsize=7.4, fontweight='bold', color=NAVY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("Generating Topic 5 Enlarged High-Legibility Diagrams...")
    generate_fig5_1()
    generate_fig5_2()
    generate_fig5_3()
    generate_fig5_4()
    generate_fig5_5()
    generate_fig5_6()
    generate_fig5_7()
    generate_fig5_8()
    generate_fig5_9()
    generate_fig5_10()
    generate_fig5_11()
    generate_fig5_12()
    generate_fig5_13()
    generate_fig5_14()
    print("All 14 Topic 5 diagrams generated successfully with enlarged fonts.")

if __name__ == "__main__":
    main()
