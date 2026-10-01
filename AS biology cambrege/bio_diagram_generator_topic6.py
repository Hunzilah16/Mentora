"""
Cambridge International AS Level Biology (9700)
Topic 6: Nucleic Acids and Protein Synthesis — High-Precision Publication-Quality Diagram Generator
Enlarged High-Legibility Edition: Boosted font sizes and line weights for crystal-clear printing.

Generates 14 high-resolution 300 DPI figures for Topic 6:
1.  fig6_1_nucleotide_structure_atp.png
2.  fig6_2_purines_vs_pyrimidines.png
3.  fig6_3_dna_double_helix_antiparallel.png
4.  fig6_4_semiconservative_replication_fork.png
5.  fig6_5_meselson_stahl_experiment.png
6.  fig6_6_mrna_trna_rrna_structures.png
7.  fig6_7_transcription_mechanism.png
8.  fig6_8_ribosome_translation_cycle.png
9.  fig6_9_genetic_code_wheel_chart.png
10. fig6_10_gene_mutations_frameshift.png
11. fig6_11_sickle_cell_anaemia_mutation.png
12. fig6_12_polysome_electron_micrograph.png
13. fig6_13_trna_charging_aminoacyl_synthetase.png
14. fig6_14_dna_vs_rna_chemical_comparison.png
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
# FIG 6.1: NUCLEOTIDE STRUCTURE & ATP
# ==============================================================================
def generate_fig6_1(filename="fig6_1_nucleotide_structure_atp.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: General Mononucleotide (Phosphate, Pentose, Base)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: General Mononucleotide Monomer", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Phosphate group (circle at left)
    p_circ = Circle((22, 68), 10, facecolor="#fef08a", edgecolor=AMBER, lw=1.5)
    ax1.add_patch(p_circ)
    ax1.text(22, 68, "Phosphate\nGroup\n(PO₄³⁻)", fontsize=7.2, fontweight='bold', color="#854d0e", ha='center', va='center')

    # Pentose sugar (pentagon at center)
    pent_x = [48, 58, 54, 42, 38]
    pent_y = [58, 50, 36, 36, 50]
    pent_poly = Polygon(list(zip(pent_x, pent_y)), closed=True, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.5)
    ax1.add_patch(pent_poly)
    ax1.text(48, 46, "Pentose\nSugar", fontsize=7.6, fontweight='bold', color=NAVY, ha='center', va='center')
    ax1.text(48, 38, "(Deoxyribose / Ribose)", fontsize=6.2, color=DARK_GREY, ha='center')

    # Carbon numbering labels
    ax1.text(59, 52, "C1'", fontsize=6.8, fontweight='bold', color=NAVY)
    ax1.text(56, 34, "C2' (H or OH)", fontsize=6.2, color=CRIMSON)
    ax1.text(39, 34, "C3' (OH)", fontsize=6.2, color=DARK_GREY)
    ax1.text(35, 52, "C4'", fontsize=6.8, fontweight='bold', color=NAVY)
    ax1.text(36, 64, "C5'", fontsize=6.8, fontweight='bold', color=NAVY)

    # Nitrogenous base (rectangle at right)
    base_rect = FancyBboxPatch((70, 42), 24, 20, boxstyle="round,pad=0.4", facecolor="#bbf7d0", edgecolor=GREEN, lw=1.5)
    ax1.add_patch(base_rect)
    ax1.text(82, 52, "Nitrogenous\nOrganic Base\n(A, T, C, G / U)", fontsize=7.2, fontweight='bold', color="#14532d", ha='center', va='center')

    # Bonds
    # Phosphoester bond between C5' and phosphate
    ax1.plot([32, 42], [68, 58], color=NAVY, lw=1.8)
    ax1.text(34, 76, "Phosphoester\nbond", fontsize=6.6, color=NAVY, ha='center')

    # Glycosidic bond between C1' and Base
    ax1.plot([58, 70], [50, 50], color=NAVY, lw=1.8)
    ax1.text(64, 54, "Covalent\nC-N bond", fontsize=6.6, color=NAVY, ha='center')

    ax1.text(50, 14, "Monomer unit of nucleic acids; condensed via condensation reactions\nforming phosphodiester links between 3'-OH and 5'-phosphate",
             fontsize=7.2, color=DARK_GREY, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=0.8))

    # Panel B: ATP Structure (Adenosine Triphosphate)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: ATP (Adenosine Triphosphate) - Phosphorylated Nucleotide", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Three phosphate groups (alpha, beta, gamma)
    p_colors = ["#fef08a", "#fde047", "#facc15"]
    p_labels = ["α", "β", "γ"]
    for i, (col, lbl) in enumerate(zip(p_colors, p_labels)):
        px = 12 + i * 15
        p_c = Circle((px, 60), 6.5, facecolor=col, edgecolor=AMBER, lw=1.3)
        ax2.add_patch(p_c)
        ax2.text(px, 60, f"P\n({lbl})", fontsize=7.0, fontweight='bold', color="#854d0e", ha='center', va='center')
        if i < 2:
            # High energy phosphoanhydride bond symbol (~)
            ax2.plot([px + 6.5, px + 8.5], [60, 60], color=CRIMSON, lw=2.0)
            ax2.text(px + 7.5, 69, "~", fontsize=10.0, fontweight='bold', color=CRIMSON, ha='center')

    ax2.text(27, 78, "2 High-energy phosphoanhydride bonds\n(ΔG = -30.5 kJ mol⁻¹ upon hydrolysis)", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')

    # Ribose sugar
    rib_x = [54, 62, 59, 49, 46]
    rib_y = [52, 45, 33, 33, 45]
    rib_poly = Polygon(list(zip(rib_x, rib_y)), closed=True, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.4)
    ax2.add_patch(rib_poly)
    ax2.text(54, 42, "Ribose\nSugar", fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')
    ax2.text(54, 27, "2'-OH & 3'-OH groups", fontsize=6.4, color=DARK_GREY, ha='center')

    # Link from alpha-P to Ribose C5'
    ax2.plot([18.5, 48], [60, 48], color=NAVY, lw=1.6)

    # Adenine base (double ring)
    ad1 = FancyBboxPatch((72, 48), 12, 16, boxstyle="round,pad=0.2", facecolor="#fed7aa", edgecolor=AMBER, lw=1.2)
    ad2 = FancyBboxPatch((84, 52), 10, 12, boxstyle="round,pad=0.2", facecolor="#fed7aa", edgecolor=AMBER, lw=1.2)
    ax2.add_patch(ad1)
    ax2.add_patch(ad2)
    ax2.text(82, 56, "Adenine\n(Purine)", fontsize=7.4, fontweight='bold', color="#9a3412", ha='center', va='center')

    # Link from ribose C1' to Adenine
    ax2.plot([62, 72], [45, 54], color=NAVY, lw=1.6)

    # Bracket for Adenosine
    ax2.annotate("", xy=(46, 20), xytext=(94, 20), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.2))
    ax2.text(70, 14, "Adenosine (Ribose + Adenine)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.2: PURINES VS PYRIMIDINES & BASE PAIRING
# ==============================================================================
def generate_fig6_2(filename="fig6_2_purines_vs_pyrimidines.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Molecular Ring Structures (Purines vs Pyrimidines)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Purines (Double-Ring) vs Pyrimidines (Single-Ring)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Purines box (Top)
    ax1.add_patch(FancyBboxPatch((4, 52), 92, 42, boxstyle="round,pad=0.4", facecolor="#fef3c7", edgecolor=AMBER, lw=1.3))
    ax1.text(8, 88, "PURINES (Two Carbon-Nitrogen Rings: 6-membered + 5-membered)", fontsize=7.2, fontweight='bold', color="#854d0e")

    # Adenine (A)
    ax1.add_patch(FancyBboxPatch((12, 58), 16, 22, boxstyle="round,pad=0.2", facecolor="#fde68a", edgecolor=AMBER, lw=1.1))
    ax1.add_patch(FancyBboxPatch((28, 62), 12, 16, boxstyle="round,pad=0.2", facecolor="#fde68a", edgecolor=AMBER, lw=1.1))
    ax1.text(26, 69, "Adenine (A)\n6-amino purine", fontsize=7.0, fontweight='bold', color="#78350f", ha='center', va='center')

    # Guanine (G)
    ax1.add_patch(FancyBboxPatch((56, 58), 16, 22, boxstyle="round,pad=0.2", facecolor="#fde68a", edgecolor=AMBER, lw=1.1))
    ax1.add_patch(FancyBboxPatch((72, 62), 12, 16, boxstyle="round,pad=0.2", facecolor="#fde68a", edgecolor=AMBER, lw=1.1))
    ax1.text(70, 69, "Guanine (G)\n2-amino-6-oxy purine", fontsize=7.0, fontweight='bold', color="#78350f", ha='center', va='center')

    # Pyrimidines box (Bottom)
    ax1.add_patch(FancyBboxPatch((4, 6), 92, 42, boxstyle="round,pad=0.4", facecolor="#eff6ff", edgecolor=NAVY, lw=1.3))
    ax1.text(8, 42, "PYRIMIDINES (Single 6-membered Carbon-Nitrogen Ring)", fontsize=7.2, fontweight='bold', color=NAVY)

    # Cytosine (C)
    ax1.add_patch(FancyBboxPatch((10, 12), 22, 22, boxstyle="round,pad=0.2", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax1.text(21, 23, "Cytosine (C)\nDNA & RNA", fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # Thymine (T)
    ax1.add_patch(FancyBboxPatch((40, 12), 22, 22, boxstyle="round,pad=0.2", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax1.text(51, 23, "Thymine (T)\nDNA only (methylated)", fontsize=6.8, fontweight='bold', color=NAVY, ha='center', va='center')

    # Uracil (U)
    ax1.add_patch(FancyBboxPatch((70, 12), 22, 22, boxstyle="round,pad=0.2", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax1.text(81, 23, "Uracil (U)\nRNA only (unmethylated)", fontsize=6.8, fontweight='bold', color=NAVY, ha='center', va='center')

    # Panel B: Complementary Base Pairing & Hydrogen Bonds
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Complementary Base Pairing (A=T & G≡C)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Top: Adenine - Thymine Pair (2 H-bonds)
    ax2.add_patch(FancyBboxPatch((8, 56), 28, 32, boxstyle="round,pad=0.3", facecolor="#fde68a", edgecolor=AMBER, lw=1.2))
    ax2.text(22, 72, "Adenine (A)\n[Purine]", fontsize=7.6, fontweight='bold', color="#78350f", ha='center', va='center')

    ax2.add_patch(FancyBboxPatch((64, 56), 28, 32, boxstyle="round,pad=0.3", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.2))
    ax2.text(78, 72, "Thymine (T)\n[Pyrimidine]", fontsize=7.6, fontweight='bold', color=NAVY, ha='center', va='center')

    # 2 dashed H-bonds
    ax2.plot([36, 64], [78, 78], color=CRIMSON, lw=2.0, linestyle='--')
    ax2.plot([36, 64], [66, 66], color=CRIMSON, lw=2.0, linestyle='--')
    ax2.text(50, 83, "2 Hydrogen Bonds", fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')

    # Bottom: Guanine - Cytosine Pair (3 H-bonds)
    ax2.add_patch(FancyBboxPatch((8, 10), 28, 36, boxstyle="round,pad=0.3", facecolor="#fde68a", edgecolor=AMBER, lw=1.2))
    ax2.text(22, 28, "Guanine (G)\n[Purine]", fontsize=7.6, fontweight='bold', color="#78350f", ha='center', va='center')

    ax2.add_patch(FancyBboxPatch((64, 10), 28, 36, boxstyle="round,pad=0.3", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.2))
    ax2.text(78, 28, "Cytosine (C)\n[Pyrimidine]", fontsize=7.6, fontweight='bold', color=NAVY, ha='center', va='center')

    # 3 dashed H-bonds
    ax2.plot([36, 64], [38, 38], color=CRIMSON, lw=2.0, linestyle='--')
    ax2.plot([36, 64], [28, 28], color=CRIMSON, lw=2.0, linestyle='--')
    ax2.plot([36, 64], [18, 18], color=CRIMSON, lw=2.0, linestyle='--')
    ax2.text(50, 43, "3 Hydrogen Bonds (Higher Tm / Stability)", fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.3: DNA DOUBLE HELIX & ANTIPARALLEL STRANDS
# ==============================================================================
def generate_fig6_3(filename="fig6_3_dna_double_helix_antiparallel.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Antiparallel Sugar-Phosphate Backbones & Ladder Structure
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Antiparallel 5' to 3' and 3' to 5' Strands", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Left strand: 5' to 3' downwards
    ax1.add_patch(FancyBboxPatch((14, 88), 16, 8, boxstyle="round,pad=0.2", facecolor=CRIMSON, edgecolor=CRIMSON))
    ax1.text(22, 92, "5' End (PO₄³⁻)", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')

    ax1.plot([22, 22], [14, 88], color=NAVY, lw=4.0)

    ax1.add_patch(FancyBboxPatch((14, 4), 16, 8, boxstyle="round,pad=0.2", facecolor=NAVY, edgecolor=NAVY))
    ax1.text(22, 8, "3' End (-OH)", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')

    # Right strand: 3' to 5' downwards (5' at bottom)
    ax1.add_patch(FancyBboxPatch((70, 88), 16, 8, boxstyle="round,pad=0.2", facecolor=NAVY, edgecolor=NAVY))
    ax1.text(78, 92, "3' End (-OH)", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')

    ax1.plot([78, 78], [14, 88], color=NAVY, lw=4.0)

    ax1.add_patch(FancyBboxPatch((70, 4), 16, 8, boxstyle="round,pad=0.2", facecolor=CRIMSON, edgecolor=CRIMSON))
    ax1.text(78, 8, "5' End (PO₄³⁻)", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')

    # Base pairs connecting the strands
    base_pairs = [
        ("A", "T", 80, 2),
        ("G", "C", 68, 3),
        ("C", "G", 56, 3),
        ("T", "A", 44, 2),
        ("A", "T", 32, 2),
        ("G", "C", 20, 3),
    ]

    for b1, b2, y, h_count in base_pairs:
        # Left base
        ax1.add_patch(Rectangle((24, y-3), 20, 6, facecolor="#fef08a", edgecolor=AMBER, lw=1.0))
        ax1.text(34, y, b1, fontsize=7.4, fontweight='bold', color="#854d0e", ha='center', va='center')

        # Right base
        ax1.add_patch(Rectangle((56, y-3), 20, 6, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.0))
        ax1.text(66, y, b2, fontsize=7.4, fontweight='bold', color=NAVY, ha='center', va='center')

        # H bonds
        ls = ':' if h_count == 3 else '--'
        ax1.plot([44, 56], [y, y], color=CRIMSON, lw=2.0, linestyle=ls)

    # Phosphodiester bond callout
    ax1.annotate("Phosphodiester bond\n(joins 3'-C of one sugar\nto 5'-C of adjacent sugar)",
                 xy=(22, 60), xytext=(2, 60),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                 fontsize=6.6, fontweight='bold', color=NAVY, va='center')

    # Panel B: Double Helix Dimensions & Grooves
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Watson-Crick B-DNA Geometric Dimensions", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Helix representation using sinusoidal ribbons
    t = np.linspace(10, 90, 200)
    y_vals = t
    x1_vals = 50 + 22 * np.sin((y_vals - 10) * 2 * np.pi / 34)
    x2_vals = 50 + 22 * np.sin((y_vals - 10) * 2 * np.pi / 34 + np.pi)

    ax2.plot(x1_vals, y_vals, color=NAVY, lw=3.0)
    ax2.plot(x2_vals, y_vals, color="#0284c7", lw=3.0)

    # Rungs (base pairs)
    for ry in range(16, 88, 6):
        x_a = 50 + 22 * np.sin((ry - 10) * 2 * np.pi / 34)
        x_b = 50 + 22 * np.sin((ry - 10) * 2 * np.pi / 34 + np.pi)
        ax2.plot([x_a, x_b], [ry, ry], color=CRIMSON, lw=1.6, alpha=0.8)

    # Dimension annotations
    # Width = 2.0 nm
    ax2.plot([28, 72], [14, 14], color=DARK_GREY, lw=1.2)
    ax2.plot([28, 28], [11, 17], color=DARK_GREY, lw=1.2)
    ax2.plot([72, 72], [11, 17], color=DARK_GREY, lw=1.2)
    ax2.text(50, 9, "Helix Diameter = 2.0 nm", fontsize=7.2, fontweight='bold', color=NAVY, ha='center')

    # Pitch = 3.4 nm (10 bp per complete turn)
    ax2.plot([82, 82], [27, 61], color=DARK_GREY, lw=1.2)
    ax2.plot([79, 85], [27, 27], color=DARK_GREY, lw=1.2)
    ax2.plot([79, 85], [61, 61], color=DARK_GREY, lw=1.2)
    ax2.text(86, 44, "One Full Turn = 3.4 nm\n(10 base pairs per turn;\n0.34 nm per pair)", fontsize=6.8, color=DARK_GREY, va='center')

    # Major and Minor Grooves
    ax2.annotate("Major Groove\n(~2.2 nm wide)", xy=(50, 48), xytext=(12, 48),
                 arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=TEAL, ha='center')
    ax2.annotate("Minor Groove\n(~1.2 nm wide)", xy=(50, 78), xytext=(12, 78),
                 arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.1),
                 fontsize=6.8, fontweight='bold', color=TEAL, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.4: SEMI-CONSERVATIVE REPLICATION FORK
# ==============================================================================
def generate_fig6_4(filename="fig6_4_semiconservative_replication_fork.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Molecular Architecture of the DNA Replication Fork", fontsize=10.2, fontweight='bold', color=NAVY, pad=4)

    # Parental DNA entering from right
    ax.plot([70, 95], [54, 54], color=NAVY, lw=3.0)
    ax.plot([70, 95], [46, 46], color=NAVY, lw=3.0)
    for x in range(74, 94, 4):
        ax.plot([x, x], [46, 54], color=MID_GREY, lw=1.2, linestyle=':')
    ax.text(82, 58, "Parental Double Helix (Unreplicated)", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')

    # DNA Helicase unwinding at fork junction
    helicase = Polygon([(64, 60), (74, 50), (64, 40)], closed=True, facecolor="#f87171", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(helicase)
    ax.text(66, 50, "DNA\nHelicase", fontsize=6.8, fontweight='bold', color=WHITE, ha='center', va='center')
    ax.annotate("DNA Helicase:\nBreaks H-bonds between bases;\nunwinds parental duplex",
                xy=(69, 56), xytext=(69, 82),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2),
                fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')

    # Leading strand (continuous 5' to 3' synthesis toward fork - Top)
    # Parental template (3' to 5')
    ax.plot([10, 64], [80, 56], color=NAVY, lw=2.6)
    ax.text(8, 82, "3'", fontsize=7.8, fontweight='bold', color=NAVY)
    ax.text(66, 62, "5'", fontsize=7.4, fontweight='bold', color=NAVY)

    # Newly synthesised leading strand (5' to 3')
    ax.plot([16, 60], [74, 52], color=GREEN, lw=2.8)
    ax.text(14, 76, "5'", fontsize=7.4, fontweight='bold', color=GREEN)
    ax.text(62, 54, "3'", fontsize=7.4, fontweight='bold', color=GREEN)

    # DNA Polymerase on leading strand
    pol1 = Circle((52, 56), 6.5, facecolor="#86efac", edgecolor=GREEN, lw=1.4)
    ax.add_patch(pol1)
    ax.text(52, 56, "DNA Pol\nIII", fontsize=6.6, fontweight='bold', color="#14532d", ha='center', va='center')
    ax.text(34, 78, "Leading Strand (Continuous 5'->3' synthesis)", fontsize=7.4, fontweight='bold', color=GREEN)

    # Lagging strand (discontinuous Okazaki fragments away from fork - Bottom)
    # Parental template (5' to 3')
    ax.plot([10, 64], [20, 44], color=NAVY, lw=2.6)
    ax.text(8, 18, "5'", fontsize=7.8, fontweight='bold', color=NAVY)
    ax.text(66, 38, "3'", fontsize=7.4, fontweight='bold', color=NAVY)

    # Okazaki fragments (Green) with RNA primers (Amber)
    # Fragment 1
    ax.plot([46, 58], [34, 42], color=GREEN, lw=2.8)
    ax.plot([42, 46], [32, 34], color=AMBER, lw=3.4) # RNA primer
    # Fragment 2
    ax.plot([24, 38], [24, 30], color=GREEN, lw=2.8)
    ax.plot([20, 24], [22, 24], color=AMBER, lw=3.4) # RNA primer

    ax.text(34, 14, "Lagging Strand (Discontinuous Okazaki Fragments)", fontsize=7.4, fontweight='bold', color=CRIMSON)

    # DNA Ligase sealing nick
    ax.add_patch(FancyBboxPatch((38, 26), 6, 8, boxstyle="round,pad=0.1", facecolor="#fed7aa", edgecolor=AMBER, lw=1.1))
    ax.text(41, 30, "Ligase", fontsize=5.8, fontweight='bold', color="#9a3412", ha='center', va='center')

    # Direction arrow
    ax.annotate("", xy=(30, 27), xytext=(40, 33), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.6))
    ax.text(35, 36, "Synthesis away\nfrom fork", fontsize=6.2, color=CRIMSON, ha='center')

    # Single-strand DNA-binding proteins (SSBs)
    for sx in [35, 45, 55]:
        ax.add_patch(Circle((sx, 48 - (sx-35)*0.2), 2.2, facecolor="#c084fc", edgecolor=PURPLE, lw=0.9))
    ax.annotate("SSB Proteins:\nPrevent re-annealing\nof single strands",
                xy=(45, 48), xytext=(22, 50),
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.0),
                fontsize=6.6, color=PURPLE, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.5: MESELSON-STAHL DENSITY GRADIENT EXPERIMENT
# ==============================================================================
def generate_fig6_5(filename="fig6_5_meselson_stahl_experiment.png"):
    fig, axes = plt.subplots(1, 4, figsize=(9.4, 4.8), dpi=300)
    gens = [
        ("Generation 0", "Grown exclusively\nin ¹⁵N heavy medium", 15, "100% ¹⁵N-¹⁵N\nHeavy Band"),
        ("Generation 1", "Transferred to ¹⁴N\nlight medium (1 cycle)", 50, "100% ¹⁵N-¹⁴N\nHybrid Band"),
        ("Generation 2", "Continued in ¹⁴N\nmedium (2 cycles)", [50, 85], "50% Hybrid (¹⁵N-¹⁴N)\n50% Light (¹⁴N-¹⁴N)"),
        ("Theoretical Models", "Predictions after 1 gen:\n• Conservative: 2 bands\n• Dispersive: 1 band\n• Semiconservative: 1 hybrid", None, "Confirms Semiconservative\nReplication")
    ]

    for ax, (title, sub, band_y, desc) in zip(axes, gens):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.set_title(title, fontsize=8.8, fontweight='bold', color=NAVY, pad=4)
        ax.text(50, 89, sub, fontsize=6.6, color=DARK_GREY, ha='center')

    # Draw centrifuge tubes in axes 0, 1, 2
    for i in range(3):
        ax = axes[i]
        # Tube outline
        tube = FancyBboxPatch((35, 12), 30, 72, boxstyle="round,pad=0.8,rounding_size=6",
                              facecolor="#f8fafc", edgecolor=NAVY, lw=1.5)
        ax.add_patch(tube)
        # Meniscus & CsCl density gradient
        ax.plot([35, 65], [78, 78], color="#38bdf8", lw=1.2)
        ax.text(50, 81, "Meniscus (Low ρ)", fontsize=5.8, color=MID_GREY, ha='center')
        ax.text(50, 7, "Bottom (High ρ)", fontsize=5.8, color=MID_GREY, ha='center')

    # Gen 0: Heavy band at y=25
    axes[0].add_patch(Rectangle((37, 24), 26, 6, facecolor=NAVY, edgecolor=NAVY))
    axes[0].text(50, 27, "¹⁵N-¹⁵N Heavy", fontsize=6.4, fontweight='bold', color=WHITE, ha='center', va='center')
    axes[0].text(50, 4, "100% Heavy DNA (ρ = 1.724)", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')

    # Gen 1: Intermediate hybrid band at y=48
    axes[1].add_patch(Rectangle((37, 47), 26, 6, facecolor=PURPLE, edgecolor=PURPLE))
    axes[1].text(50, 50, "¹⁵N-¹⁴N Hybrid", fontsize=6.4, fontweight='bold', color=WHITE, ha='center', va='center')
    axes[1].text(50, 4, "100% Hybrid DNA (ρ = 1.717)", fontsize=6.8, fontweight='bold', color=PURPLE, ha='center')

    # Gen 2: Two bands: Hybrid at y=48 and Light at y=70
    axes[2].add_patch(Rectangle((37, 47), 26, 6, facecolor=PURPLE, edgecolor=PURPLE))
    axes[2].text(50, 50, "¹⁵N-¹⁴N Hybrid", fontsize=6.4, fontweight='bold', color=WHITE, ha='center', va='center')
    axes[2].add_patch(Rectangle((37, 69), 26, 6, facecolor="#38bdf8", edgecolor="#0284c7"))
    axes[2].text(50, 72, "¹⁴N-¹⁴N Light", fontsize=6.4, fontweight='bold', color=NAVY, ha='center', va='center')
    axes[2].text(50, 4, "50% Light : 50% Hybrid", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')

    # Axes 3: Model comparison diagram
    ax3 = axes[3]
    models = [
        ("Semiconservative\n(Observed)", "#dcfce7", GREEN, "1 Hybrid band (Gen 1)\n1 Light + 1 Hybrid (Gen 2)"),
        ("Conservative\n(Disproved)", "#fee2e2", CRIMSON, "2 bands in Gen 1:\n1 Heavy + 1 Light"),
        ("Dispersive\n(Disproved)", "#fef3c7", AMBER, "1 band in Gen 2\nshifting progressively light")
    ]
    for idx, (m_title, bg, tc, m_sub) in enumerate(models):
        my = 68 - idx * 28
        ax3.add_patch(FancyBboxPatch((4, my), 92, 24, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=tc, lw=1.2))
        ax3.text(8, my + 17, m_title, fontsize=6.8, fontweight='bold', color=tc)
        ax3.text(8, my + 5, m_sub, fontsize=6.0, color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.6: mRNA, tRNA, AND rRNA STRUCTURAL COMPARISON
# ==============================================================================
def generate_fig6_6(filename="fig6_6_mrna_trna_rrna_structures.png"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9.4, 4.8), dpi=300)

    # Panel 1: mRNA (Linear Single Strand)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Messenger RNA (mRNA)", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Linear ribbon strand
    ax1.plot([15, 85], [75, 75], color=CRIMSON, lw=3.5)
    ax1.text(10, 75, "5'", fontsize=8.0, fontweight='bold', color=CRIMSON, va='center')
    ax1.text(90, 75, "3'", fontsize=8.0, fontweight='bold', color=CRIMSON, va='center')

    # Codon triplet blocks
    codons = [("A U G", "Start"), ("G A C", "Asp"), ("U U C", "Phe"), ("U A A", "Stop")]
    for i, (cd, aa) in enumerate(codons):
        cx = 24 + i * 16
        ax1.add_patch(FancyBboxPatch((cx-6, 52), 12, 16, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.1))
        ax1.text(cx, 62, cd, fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center')
        ax1.text(cx, 55, aa, fontsize=6.0, color=DARK_GREY, ha='center')
        ax1.plot([cx, cx], [68, 75], color=CRIMSON, lw=1.2)

    ax1.text(50, 42, "Codons (triplets of bases)", fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(50, 20, "• Linear single-stranded RNA\n• Transcribed from antisense DNA\n• Transient template for translation\n• Unfolded, no base-pairing loops",
             fontsize=6.8, color=DARK_GREY, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=0.7))

    # Panel 2: tRNA (Cloverleaf Secondary Structure)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Transfer RNA (tRNA)", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # 3' Amino acid attachment site (CCA-OH) at top
    ax2.text(50, 94, "3' CCA-OH", fontsize=7.4, fontweight='bold', color=AMBER, ha='center')
    ax2.add_patch(Circle((50, 86), 4.5, facecolor="#fed7aa", edgecolor=AMBER, lw=1.2))
    ax2.text(50, 86, "Met", fontsize=6.2, fontweight='bold', color="#9a3412", ha='center', va='center')

    # Cloverleaf outline loops
    # Acceptor stem
    ax2.plot([47, 47], [70, 82], color=NAVY, lw=2.0)
    ax2.plot([53, 53], [70, 82], color=NAVY, lw=2.0)
    # T-loop (Right)
    ax2.add_patch(Circle((74, 55), 10, facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    ax2.text(74, 55, "TΨC\nLoop", fontsize=6.2, color=NAVY, ha='center', va='center')
    # D-loop (Left)
    ax2.add_patch(Circle((26, 55), 10, facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    ax2.text(26, 55, "D\nLoop", fontsize=6.2, color=NAVY, ha='center', va='center')
    # Central junction
    ax2.add_patch(Circle((50, 55), 7, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.0))
    # Anticodon loop (Bottom)
    ax2.add_patch(Circle((50, 28), 11, facecolor="#fef3c7", edgecolor=AMBER, lw=1.3))
    ax2.text(50, 31, "Anticodon\nLoop", fontsize=6.4, fontweight='bold', color="#854d0e", ha='center', va='center')
    ax2.text(50, 20, "U A C", fontsize=7.6, fontweight='bold', color=CRIMSON, ha='center')

    ax2.text(50, 6, "Specific amino acid esterified at 3' end;\nAnticodon pairs with complementary mRNA codon", fontsize=6.4, color=DARK_GREY, ha='center')

    # Panel 3: Ribosomal RNA (rRNA) & Ribosome Complex
    ax3.set_xlim(0, 100)
    ax3.set_ylim(0, 100)
    ax3.axis('off')
    ax3.set_title("C: Ribosomal RNA (rRNA) & Ribosome", fontsize=9.2, fontweight='bold', color=NAVY, pad=4)

    # Large subunit (60S eukaryotic / 50S prokaryotic)
    ax3.add_patch(Ellipse((50, 65), 56, 34, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.5))
    ax3.text(50, 72, "Large Subunit (60S)", fontsize=7.2, fontweight='bold', color="#14532d", ha='center')
    ax3.text(50, 64, "(28S, 5.8S, 5S rRNAs + proteins)", fontsize=6.0, color="#14532d", ha='center')

    # Small subunit (40S eukaryotic / 30S prokaryotic)
    ax3.add_patch(Ellipse((50, 38), 50, 24, facecolor="#86efac", edgecolor=GREEN, lw=1.5))
    ax3.text(50, 40, "Small Subunit (40S)", fontsize=7.2, fontweight='bold', color="#14532d", ha='center')
    ax3.text(50, 32, "(18S rRNA + proteins)", fontsize=6.0, color="#14532d", ha='center')

    # mRNA groove between subunits
    ax3.plot([14, 86], [50, 50], color=CRIMSON, lw=2.2, linestyle='--')
    ax3.text(50, 52, "mRNA binding groove", fontsize=6.4, fontweight='bold', color=CRIMSON, ha='center')

    ax3.text(50, 14, "• Synthesised in nucleolus\n• Catalytic ribozyme: peptidyl\ntransferase forms peptide bonds\n• Assembles into functional 80S complex",
             fontsize=6.6, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.7: TRANSCRIPTION MECHANISM
# ==============================================================================
def generate_fig6_7(filename="fig6_7_transcription_mechanism.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Transcription Elongation: RNA Polymerase and Nascent mRNA Synthesis", fontsize=10.2, fontweight='bold', color=NAVY, pad=4)

    # 1. Coding / Sense strand (5' to 3' - Non-transcribed duplex top)
    # Outside bubble: y = 74. In bubble (x=24 to 76): arches up to y = 85
    ax.plot([4, 24], [74, 74], color=NAVY, lw=2.2)
    ax.plot([24, 34, 66, 76], [74, 85, 85, 74], color=NAVY, lw=2.2)
    ax.plot([76, 96], [74, 74], color=NAVY, lw=2.2)
    ax.text(2, 74, "5'", fontsize=8.4, fontweight='bold', color=NAVY, va='center')
    ax.text(98, 74, "3'", fontsize=8.4, fontweight='bold', color=NAVY, va='center')
    ax.text(50, 90, "Coding (Sense) Strand (5' -> 3') [Non-transcribed]", fontsize=7.4, fontweight='bold', color=NAVY, ha='center')

    # Coding strand exposed bases inside bubble (y = 80)
    coding_bases = ["A", "T", "G", "C", "C", "T", "G", "A"]
    for i, cb in enumerate(coding_bases):
        bx = 35 + i * 4.4
        ax.text(bx, 80, cb, fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # 2. Template / Antisense strand (3' to 5' - Transcribed duplex bottom)
    # Outside bubble: y = 34. In bubble (x=24 to 76): sags down to y = 24
    ax.plot([4, 24], [34, 34], color=NAVY, lw=2.2)
    ax.plot([24, 34, 66, 76], [34, 24, 24, 34], color=NAVY, lw=2.2)
    ax.plot([76, 96], [34, 34], color=NAVY, lw=2.2)
    ax.text(2, 34, "3'", fontsize=8.4, fontweight='bold', color=NAVY, va='center')
    ax.text(98, 34, "5'", fontsize=8.4, fontweight='bold', color=NAVY, va='center')
    ax.text(50, 19, "Template (Antisense) Strand (3' -> 5') [Transcribed]", fontsize=7.4, fontweight='bold', color=NAVY, ha='center')

    # Template strand exposed bases inside bubble (y = 29)
    template_bases = ["T", "A", "C", "G", "G", "A", "C", "T"]
    for i, tb in enumerate(template_bases):
        bx = 35 + i * 4.4
        ax.text(bx, 29, tb, fontsize=7.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # 3. RNA Polymerase enzyme boundary (shaded oval)
    rna_pol = Ellipse((54, 55), 48, 52, facecolor="#fed7aa", edgecolor=AMBER, lw=1.8, alpha=0.50, zorder=1)
    ax.add_patch(rna_pol)
    ax.text(70, 71, "RNA\nPolymerase", fontsize=8.2, fontweight='bold', color="#9a3412", ha='center')

    # 4. Complementary base pairing & Hydrogen Bonds
    mrna_bases = ["A", "U", "G", "C", "C", "U", "G", "A"]
    for i, (tb, mb) in enumerate(zip(template_bases, mrna_bases)):
        bx = 35 + i * 4.4
        # Vertical dotted hydrogen bond line
        ax.plot([bx, bx], [32, 39], color=MID_GREY, lw=1.2, linestyle=':', zorder=2)
        # mRNA base text at y = 42
        ax.text(bx, 42, mb, fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center', va='center', zorder=4)
        # Vertical connection from base to mRNA backbone
        ax.plot([bx, bx], [44.5, 48], color=CRIMSON, lw=1.2, zorder=3)

    # 5. Nascent mRNA backbone (solid crimson line at y = 48)
    ax.plot([35, 66], [48, 48], color=CRIMSON, lw=2.6, zorder=3)
    # Sweeping exit of 5' single-stranded tail
    ax.plot([14, 25, 35], [62, 62, 48], color=CRIMSON, lw=2.6, zorder=3, solid_capstyle='round')
    ax.text(11, 62, "5'", fontsize=8.4, fontweight='bold', color=CRIMSON, va='center', ha='right')
    ax.text(68, 48, "3'-OH", fontsize=7.4, fontweight='bold', color=CRIMSON, va='center')

    # Label for nascent mRNA transcript
    ax.text(16, 68, "Nascent mRNA transcript (5' -> 3')", fontsize=7.2, fontweight='bold', color=CRIMSON)

    # Callout: Transient RNA-DNA hybrid
    ax.annotate("Transient RNA-DNA hybrid helix (~8 bp)",
                xy=(48, 36), xytext=(28, 52),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                fontsize=6.6, color=DARK_GREY, fontweight='bold')

    # Incoming activated rNTPs into catalytic active site
    ax.annotate("Incoming activated rNTPs\n(ATP, UTP, CTP, GTP)\njoined to 3'-OH",
                xy=(67, 48), xytext=(86, 38),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.3),
                fontsize=6.8, fontweight='bold', color=TEAL, ha='center')

    # Direction of transcription arrow (placed at upper right)
    ax.annotate("", xy=(90, 68), xytext=(78, 68), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.2))
    ax.text(84, 71, "Direction of\nTranscription (5'->3')", fontsize=6.2, fontweight='bold', color=NAVY, ha='center')

    # Bottom explanatory summary box
    ax.text(50, 7.5, "Key Cambridge Principles: RNA polymerase binds promoter -> unwinds DNA duplex -> reads template strand 3'->5'\nFree rNTPs pair with template bases by complementary H-bonding -> phosphodiester bonds formed 5'->3'\nDNA rewinds behind transcription bubble -> pre-mRNA is displaced and exits 5' first",
            fontsize=6.8, color=DARK_GREY, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.8: RIBOSOME TRANSLATION CYCLE (A, P, E SITES)
# ==============================================================================
def generate_fig6_8(filename="fig6_8_ribosome_translation_cycle.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Translation Elongation Cycle: A, P, and E Ribosomal Sites", fontsize=10.2, fontweight='bold', color=NAVY, pad=4)

    # Large subunit background (Top)
    ax.add_patch(FancyBboxPatch((18, 44), 64, 44, boxstyle="round,pad=0.6,rounding_size=10", facecolor="#bbf7d0", edgecolor=GREEN, lw=1.6))
    ax.text(50, 84, "Large Ribosomal Subunit (Peptidyl Transferase Centre)", fontsize=7.8, fontweight='bold', color="#14532d", ha='center')

    # Small subunit background (Bottom)
    ax.add_patch(FancyBboxPatch((18, 12), 64, 24, boxstyle="round,pad=0.6,rounding_size=8", facecolor="#86efac", edgecolor=GREEN, lw=1.6))
    ax.text(50, 18, "Small Ribosomal Subunit (mRNA Decoding Centre)", fontsize=7.4, fontweight='bold', color="#14532d", ha='center')

    # mRNA strand passing horizontally in interface (y=36)
    ax.plot([4, 96], [36, 36], color=CRIMSON, lw=3.0)
    ax.text(6, 40, "5'", fontsize=8.0, fontweight='bold', color=CRIMSON)
    ax.text(94, 40, "3'", fontsize=8.0, fontweight='bold', color=CRIMSON)

    # Three functional sites: E (Exit), P (Peptidyl), A (Aminoacyl)
    sites = [
        ("E Site\n(Exit)", 30, "#f1f5f9", MID_GREY, "Deacylated\ntRNA leaves"),
        ("P Site\n(Peptidyl)", 50, "#fef3c7", AMBER, "Peptidyl-tRNA\nholds chain"),
        ("A Site\n(Aminoacyl)", 70, "#eff6ff", NAVY, "Incoming\naminoacyl-tRNA")
    ]

    for name, sx, bg, tc, desc in sites:
        ax.add_patch(FancyBboxPatch((sx-8, 30), 16, 44, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=tc, lw=1.2, linestyle='--'))
        ax.text(sx, 70, name, fontsize=7.2, fontweight='bold', color=tc, ha='center')

    # P-site: tRNA with growing polypeptide chain
    ax.add_patch(FancyBboxPatch((46, 38), 8, 22, boxstyle="round,pad=0.2", facecolor="#fde68a", edgecolor=AMBER, lw=1.1))
    ax.text(50, 48, "tRNA", fontsize=6.6, fontweight='bold', color="#854d0e", ha='center')
    ax.text(50, 33, "UAC", fontsize=6.6, fontweight='bold', color=AMBER, ha='center') # Anticodon
    ax.text(50, 38, "AUG", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center') # Codon

    # Growing peptide chain exiting large subunit tunnel
    pep_coords = [(50, 62), (48, 70), (45, 78), (42, 86), (40, 93)]
    for i, (px, py) in enumerate(pep_coords):
        col = ["#f87171", "#fb923c", "#facc15", "#4ade80", "#60a5fa"][i]
        ax.add_patch(Circle((px, py), 3.2, facecolor=col, edgecolor=NAVY, lw=0.9))
    ax.text(32, 92, "Nascent\nPolypeptide\nChain", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')

    # A-site: incoming aminoacyl-tRNA delivering next amino acid
    ax.add_patch(FancyBboxPatch((66, 38), 8, 22, boxstyle="round,pad=0.2", facecolor="#bfdbfe", edgecolor=NAVY, lw=1.1))
    ax.text(70, 48, "tRNA", fontsize=6.6, fontweight='bold', color=NAVY, ha='center')
    ax.text(70, 33, "CUG", fontsize=6.6, fontweight='bold', color=NAVY, ha='center') # Anticodon
    ax.text(70, 38, "GAC", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center') # Codon
    # Incoming amino acid
    ax.add_patch(Circle((70, 62), 3.4, facecolor="#c084fc", edgecolor=PURPLE, lw=1.0))
    ax.text(70, 62, "Asp", fontsize=5.8, fontweight='bold', color=WHITE, ha='center', va='center')

    # Peptidyl transferase catalytic peptide bond arrow
    ax.annotate("Peptidyl transferase\nforms peptide bond",
                xy=(68, 62), xytext=(52, 60),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.4),
                fontsize=6.6, fontweight='bold', color=CRIMSON, ha='right')

    # E-site: empty deacylated tRNA exiting
    ax.add_patch(FancyBboxPatch((26, 38), 8, 22, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=MID_GREY, lw=0.9))
    ax.text(30, 48, "Empty\ntRNA", fontsize=6.0, color=MID_GREY, ha='center')
    ax.annotate("", xy=(16, 55), xytext=(26, 50), arrowprops=dict(arrowstyle="->", color=MID_GREY, lw=1.2))

    # Translocation arrow (Ribosome moves 5' to 3' by 1 codon)
    ax.annotate("", xy=(82, 10), xytext=(66, 10), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.8))
    ax.text(74, 5, "Translocation (5' -> 3')", fontsize=6.8, fontweight='bold', color=NAVY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.9: GENETIC CODE WHEEL / CHART & DEGENERACY
# ==============================================================================
def generate_fig6_9(filename="fig6_9_genetic_code_wheel_chart.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Simplified Radial Codon Wheel
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.axis('off')
    ax1.set_title("A: Radial Genetic Code Wheel (5' -> 3')", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Innermost ring: 1st base (U, C, A, G)
    bases1 = ["U", "C", "A", "G"]
    cols1 = ["#fecaca", "#bfdbfe", "#fde68a", "#bbf7d0"]
    for i, (b, c) in enumerate(zip(bases1, cols1)):
        wedge = Wedge((0, 0), 0.35, i * 90, (i + 1) * 90, facecolor=c, edgecolor=NAVY, lw=1.2)
        ax1.add_patch(wedge)
        angle = np.deg2rad(i * 90 + 45)
        ax1.text(0.22 * np.cos(angle), 0.22 * np.sin(angle), b, fontsize=9.0, fontweight='bold', color=NAVY, ha='center', va='center')

    # Middle ring: 2nd base (16 quadrants)
    bases2 = ["U", "C", "A", "G"] * 4
    for i in range(16):
        wedge = Wedge((0, 0), 0.65, i * 22.5, (i + 1) * 22.5, width=0.30, facecolor="#f8fafc", edgecolor="#94a3b8", lw=0.7)
        ax1.add_patch(wedge)
        angle = np.deg2rad(i * 22.5 + 11.25)
        ax1.text(0.50 * np.cos(angle), 0.50 * np.sin(angle), bases2[i], fontsize=6.8, fontweight='bold', color=NAVY, ha='center', va='center')

    # Outer ring: Key Amino Acid Callouts
    ax1.text(0, 0, "5'", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center', va='center')
    ax1.text(0.85, 0.85, "Phe / Leu", fontsize=6.8, color=DARK_GREY)
    ax1.text(-0.95, 0.85, "Ser / Pro", fontsize=6.8, color=DARK_GREY)
    ax1.text(-0.95, -0.85, "AUG (Met - START)", fontsize=6.8, fontweight='bold', color=GREEN)
    ax1.text(0.70, -0.85, "Gly / Ala", fontsize=6.8, color=DARK_GREY)

    # Panel B: Key Features of the Genetic Code
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Universal Characteristics of the Genetic Code", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    features = [
        ("Triplet Code", "Three consecutive bases (codon) code for exactly one amino acid (4³ = 64 codons for 20 amino acids).", "#eff6ff", NAVY),
        ("Degenerate (Redundant)", "Multiple distinct codons can code for the same amino acid (e.g. 6 codons for Leucine; 4 for Glycine). Buffers against harmful silent mutations.", "#fefce8", "#854d0e"),
        ("Non-Overlapping", "Each base is part of only one triplet codon; read sequentially from fixed start codon AUG without punctuation.", "#f0fdf4", GREEN),
        ("Universal", "Identical base triplets code for identical amino acids across almost all organisms (bacteria to humans); basis of genetic engineering.", "#faf5ff", PURPLE),
        ("Punctuation Codons", "1 Start Codon: AUG (codes for Methionine);\n3 Stop Codons: UAA, UAG, UGA (terminate translation via release factors; code for no amino acids).", "#fef2f2", CRIMSON)
    ]

    for idx, (title, body, bg, tc) in enumerate(features):
        fy = 78 - idx * 19
        ax2.add_patch(FancyBboxPatch((2, fy), 96, 17, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=tc, lw=1.1))
        ax2.text(6, fy + 12, title, fontsize=7.4, fontweight='bold', color=tc)
        ax2.text(6, fy + 3, body, fontsize=6.2, color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.10: GENE MUTATIONS & FRAMESHIFT
# ==============================================================================
def generate_fig6_10(filename="fig6_10_gene_mutations_frameshift.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Classification of Gene Mutations: Base Substitutions vs In/Del Frameshifts", fontsize=10.2, fontweight='bold', color=NAVY, pad=4)

    panels = [
        ("1. Wild-Type (Original Reference)",
         "DNA Template (3'->5'):  TAC - TTC - AAA - CCG - ACT\nmRNA Codons (5'->3'):   AUG - AAG - UUU - GGC - UGA\nPolypeptide Sequence:   Met - Lys - Phe - Gly - [STOP]",
         "#f8fafc", NAVY, "Normal functional protein"),
        ("2. Silent Substitution (Synonymous)",
         "DNA Template (3'->5'):  TAC - TTC - AAG - CCG - ACT  (A->G at codon 3)\nmRNA Codons (5'->3'):   AUG - AAG - UUC - GGC - UGA\nPolypeptide Sequence:   Met - Lys - Phe - Gly - [STOP]",
         "#f0fdf4", GREEN, "Same amino acid (Degenerate code)"),
        ("3. Missense Substitution (Non-synonymous)",
         "DNA Template (3'->5'):  TAC - TCC - AAA - CCG - ACT  (T->C at codon 2)\nmRNA Codons (5'->3'):   AUG - AGG - UUU - GGC - UGA\nPolypeptide Sequence:   Met - Arg - Phe - Gly - [STOP]",
         "#fefce8", AMBER, "Alters 1 amino acid (Lys -> Arg)"),
        ("4. Nonsense Substitution (Premature Stop)",
         "DNA Template (3'->5'):  TAC - TTC - ATT - CCG - ACT  (A->T at codon 3)\nmRNA Codons (5'->3'):   AUG - AAG - UAA - GGC - UGA\nPolypeptide Sequence:   Met - Lys - [STOP] (Truncated!)",
         "#fef2f2", CRIMSON, "Premature termination; non-functional"),
        ("5. Base Insertion (+1 Frameshift)",
         "DNA Template (3'->5'):  TAC - T[G]T - CAA - ACC - GAC - T  (G inserted in codon 2)\nmRNA Codons (5'->3'):   AUG - ACA - GUU - UGG - CUG - A...\nPolypeptide Sequence:   Met - Thr - Val - Trp - Leu... (ALL CHANGED)",
         "#fee2e2", CRIMSON, "Alters entire downstream reading frame")
    ]

    for idx, (title, seq, bg, tc, outcome) in enumerate(panels):
        py = 78 - idx * 15.5
        ax.add_patch(FancyBboxPatch((2, py), 96, 14.0, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=tc, lw=1.1))
        ax.text(5, py + 10.2, title, fontsize=7.2, fontweight='bold', color=tc)
        ax.text(5, py + 1.8, seq, fontsize=5.6, fontfamily='monospace', color=DARK_GREY, linespacing=1.15)
        ax.text(95, py + 7.0, outcome, fontsize=6.5, fontweight='bold', color=tc, ha='right', va='center')

    ax.text(50, 4.0, "Key Cambridge Rule: Base substitutions alter at most 1 codon; indels (insertions/deletions) shift the triplet frame,\nscrambling every downstream amino acid and frequently introducing an early premature stop codon.",
            fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.11: SICKLE CELL ANAEMIA MUTATION
# ==============================================================================
def generate_fig6_11(filename="fig6_11_sickle_cell_anaemia_mutation.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Molecular Genetic Basis (HbA vs HbS)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Molecular Genetic Basis (HbA vs HbS)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Normal HbA Allele
    ax1.add_patch(FancyBboxPatch((4, 52), 92, 43, boxstyle="round,pad=0.4", facecolor="#f0fdf4", edgecolor=GREEN, lw=1.3))
    ax1.text(8, 89, "NORMAL β-GLOBIN ALLELE (HbA)", fontsize=7.6, fontweight='bold', color=GREEN)
    ax1.text(8, 73, "DNA Coding (Sense) 5'->3':     ... C C T - G A G - G A G ...\nDNA Template (Antisense) 3'->5': ... G G A - C T C - C T C ...\nmRNA Transcript 5'->3':         ... C C U - G A G - G A G ...\n                                             │",
             fontsize=6.2, fontfamily='monospace', color=DARK_GREY, linespacing=1.2)
    ax1.text(8, 57, "Codon 6: GLUTAMIC ACID (Glu)\n• Polar, hydrophilic charged R-group (-CH₂-CH₂-COO⁻)\n• Soluble on external surface of globular tetramer",
             fontsize=6.4, fontweight='bold', color="#14532d")

    # Sickle HbS Allele
    ax1.add_patch(FancyBboxPatch((4, 4), 92, 44, boxstyle="round,pad=0.4", facecolor="#fef2f2", edgecolor=CRIMSON, lw=1.3))
    ax1.text(8, 42, "MUTANT SICKLE ALLELE (HbS) - Base Substitution", fontsize=7.6, fontweight='bold', color=CRIMSON)
    ax1.text(8, 26, "DNA Coding (Sense) 5'->3':     ... C C T - G T G - G A G ... (A->T)\nDNA Template (Antisense) 3'->5': ... G G A - C A C - C T C ... (T->A)\nmRNA Transcript 5'->3':         ... C C U - G U G - G A G ...\n                                             │",
             fontsize=6.2, fontfamily='monospace', color=DARK_GREY, linespacing=1.2)
    ax1.text(8, 10, "Codon 6: VALINE (Val)\n• Non-polar, hydrophobic hydrocarbon R-group (-CH(CH₃)₂)\n• Creates sticky hydrophobic contact patch on surface",
             fontsize=6.4, fontweight='bold', color=CRIMSON)

    # Panel B: Haemoglobin Polymerisation & Sickling Mechanism
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Deoxygenation, Polymerisation & Sickling", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Normal RBC (Biconcave disc)
    ax2.add_patch(Ellipse((26, 76), 28, 18, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.5))
    ax2.add_patch(Ellipse((26, 76), 14, 8, facecolor="#fecaca", edgecolor=CRIMSON, lw=0.8))
    ax2.text(26, 61, "Normal Erythrocyte (HbA)\nFlexible biconcave disc (7.5 µm)\nReadily deforms through capillaries", fontsize=6.4, color=DARK_GREY, ha='center')

    # Deoxygenation Trigger
    ax2.annotate("Low pO₂\n(tissues)", xy=(48, 76), xytext=(38, 76),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                 fontsize=6.2, fontweight='bold', color=CRIMSON, ha='center')

    # Polymerisation explanation
    ax2.add_patch(FancyBboxPatch((52, 60), 44, 34, boxstyle="round,pad=0.3", facecolor="#fef3c7", edgecolor=AMBER, lw=1.1))
    ax2.text(74, 88, "HbS Polymerisation", fontsize=7.2, fontweight='bold', color="#854d0e", ha='center')
    ax2.text(74, 64, "Valine 6 binds to complementary\nhydrophobic site on adjacent β-chain;\nDeoxy-HbS tetramers crystallise into\ninsoluble, rigid fibrous polymers",
             fontsize=5.8, color=DARK_GREY, ha='center')

    # Sickled RBC (Mathematically closed authentic crescent)
    theta = np.linspace(0, np.pi, 60)
    out_y = 28 + 16 * np.cos(theta)
    out_x = 84 - 18 * np.sin(theta)
    in_theta = np.linspace(np.pi, 0, 60)
    in_y = 28 + 16 * np.cos(in_theta)
    in_x = 84 - 10 * np.sin(in_theta)

    sickle_pts = np.vstack([np.column_stack([out_x, out_y]), np.column_stack([in_x, in_y])])
    sickle_poly = Polygon(sickle_pts, closed=True, facecolor="#dc2626", edgecolor=NAVY, lw=1.4)
    ax2.add_patch(sickle_poly)

    # Internal rigid fibres inside sickle cell
    ax2.plot([68, 77], [34, 18], color="#7f1d1d", lw=1.3, linestyle='--')
    ax2.plot([71, 80], [38, 22], color="#7f1d1d", lw=1.3, linestyle='--')

    ax2.text(76, 5, "Sickle Erythrocyte\nRigid, fragile crescent", fontsize=6.6, fontweight='bold', color=CRIMSON, ha='center')

    # Clinical Consequences Box
    ax2.add_patch(FancyBboxPatch((4, 8), 48, 44, boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.0))
    ax2.text(28, 46, "Clinical Pathology", fontsize=7.2, fontweight='bold', color=CRIMSON, ha='center')
    ax2.text(6, 12, "• Vaso-occlusion: Rigid cells block\n  capillaries -> tissue ischaemia & pain\n• Haemolysis: Fragile cells rupture\n  (lifespan 10-20 d vs 120 d)\n• Severe chronic haemolytic anaemia\n• Protection against severe malaria\n  (Plasmodium falciparum heterozygote)",
             fontsize=5.8, color=DARK_GREY)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.12: POLYSOME / POLYRIBOSOME ARCHITECTURE
# ==============================================================================
def generate_fig6_12(filename="fig6_12_polysome_electron_micrograph.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Diagrammatic Representation of a Polysome
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Polyribosome (Polysome) Molecular Architecture", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # mRNA strand running 5' to 3' across page
    ax1.plot([10, 90], [50, 50], color=CRIMSON, lw=3.0)
    ax1.text(6, 50, "5'", fontsize=8.4, fontweight='bold', color=CRIMSON, va='center')
    ax1.text(92, 50, "3'", fontsize=8.4, fontweight='bold', color=CRIMSON, va='center')

    # Multiple ribosomes along strand with growing polypeptides
    rib_x = [24, 40, 56, 72, 84]
    pep_lens = [8, 16, 26, 36, 44]

    for rx, plen in zip(rib_x, pep_lens):
        # Ribosome (Large + Small subunit)
        ax1.add_patch(Circle((rx, 56), 6.5, facecolor="#bbf7d0", edgecolor=GREEN, lw=1.2)) # Large
        ax1.add_patch(Circle((rx, 46), 4.5, facecolor="#86efac", edgecolor=GREEN, lw=1.0)) # Small

        # Polypeptide growing upward from large subunit
        py_top = 62 + plen * 0.6
        ax1.plot([rx, rx - plen*0.2], [62, py_top], color=PURPLE, lw=2.2)
        ax1.add_patch(Circle((rx - plen*0.2, py_top), 2.2, facecolor="#c084fc", edgecolor=PURPLE))

    ax1.text(24, 76, "Shortest\npeptide", fontsize=6.2, color=MID_GREY, ha='center')
    ax1.text(84, 94, "Longest peptide\n(near 3' stop codon)", fontsize=6.2, color=MID_GREY, ha='center')

    # Direction of ribosome movement
    ax1.annotate("", xy=(60, 36), xytext=(40, 36), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.8))
    ax1.text(50, 30, "Direction of translation (5' -> 3')", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')

    ax1.text(50, 12, "Multiple ribosomes translate a single mRNA molecule simultaneously,\ndrastically accelerating the rate of protein synthesis from one transcript",
             fontsize=6.8, color=DARK_GREY, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=0.7))

    # Panel B: Quantitative Polysome Efficiency Profile
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Polysome Efficiency & Ribosomal Density Data", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    headers = ["Parameter", "Single Ribosome", "Polysome (8 Ribosomes)"]
    cols_x = [22, 54, 82]
    ax2.add_patch(Rectangle((4, 76), 92, 9, facecolor=NAVY, edgecolor=NAVY))
    for h, x in zip(headers, cols_x):
        ax2.text(x, 80.5, h, fontsize=7.0, fontweight='bold', color=WHITE, ha='center', va='center')

    rows = [
        ("Polypeptides / min", "1.2", "9.6 (8x increase)"),
        ("Ribosome Spacing", "N/A", "~80 - 100 nucleotides"),
        ("mRNA Half-Life", "15 - 30 min", "Protected by dense ribosomes"),
        ("Cellular Location", "Free / Bound", "Cytosol / RER membrane"),
        ("Primary Benefit", "Standard flux", "Maximized translational yield")
    ]
    for idx, (p, s, poly) in enumerate(rows):
        y_pos = 69.5 - idx * 7.2
        bg = "#f8fafc" if idx % 2 == 0 else WHITE
        ax2.add_patch(Rectangle((4, y_pos - 2.8), 92, 6.6, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        ax2.text(cols_x[0], y_pos + 0.5, p, fontsize=6.8, fontweight='bold', color=DARK_GREY, ha='center')
        ax2.text(cols_x[1], y_pos + 0.5, s, fontsize=6.8, color=DARK_GREY, ha='center')
        ax2.text(cols_x[2], y_pos + 0.5, poly, fontsize=6.8, fontweight='bold', color=CRIMSON if idx == 0 else DARK_GREY, ha='center')

    ax2.text(50, 16, "In pancreatic acinar cells, polysomes on the RER synthesise\nthousands of digestive enzyme molecules per second prior to exocytosis",
             fontsize=6.8, color=NAVY, ha='center', bbox=dict(boxstyle="round,pad=0.35", facecolor="#eff6ff", edgecolor=NAVY, lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.13: tRNA CHARGING & AMINOACYL-tRNA SYNTHETASE
# ==============================================================================
def generate_fig6_13(filename="fig6_13_trna_charging_aminoacyl_synthetase.png"):
    fig, ax = plt.subplots(figsize=(9.4, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title("Two-Step Amino Acid Activation and tRNA Charging by Aminoacyl-tRNA Synthetase", fontsize=10.2, fontweight='bold', color=NAVY, pad=4)

    # Three progression panels
    # Step 1: Amino Acid Activation (Left)
    ax.add_patch(FancyBboxPatch((4, 20), 28, 70, boxstyle="round,pad=0.4", facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    ax.text(18, 84, "Step 1: Activation", fontsize=8.0, fontweight='bold', color=NAVY, ha='center')
    ax.text(18, 72, "Amino Acid + ATP\n        ↓\nAminoacyl-AMP + PPi", fontsize=7.0, fontfamily='monospace', color=DARK_GREY, ha='center')
    ax.text(18, 45, "• Enzyme active site binds\nspecific amino acid & ATP\n• Hydrolysis of ATP to AMP\nreleases pyrophosphate (PPi)\n• Creates high-energy\naminoacyl-AMP intermediate",
            fontsize=6.6, color=DARK_GREY, ha='center')

    # Step 2: Transfer to tRNA (Center)
    ax.add_patch(FancyBboxPatch((36, 20), 28, 70, boxstyle="round,pad=0.4", facecolor="#fefce8", edgecolor="#854d0e", lw=1.2))
    ax.text(50, 84, "Step 2: Transfer", fontsize=8.0, fontweight='bold', color="#854d0e", ha='center')
    ax.text(50, 72, "Aminoacyl-AMP + tRNA\n        ↓\nAminoacyl-tRNA + AMP", fontsize=7.0, fontfamily='monospace', color=DARK_GREY, ha='center')
    ax.text(50, 45, "• Uncharged tRNA binds enzyme\n• Ester bond formed between\namino acid carboxyl group\nand 3'-OH of CCA terminal\n• AMP is released\n• 'Charged' tRNA dissociates",
            fontsize=6.6, color=DARK_GREY, ha='center')

    # Step 3: High-Fidelity Proofreading (Right)
    ax.add_patch(FancyBboxPatch((68, 20), 28, 70, boxstyle="round,pad=0.4", facecolor="#fef2f2", edgecolor=CRIMSON, lw=1.2))
    ax.text(82, 84, "Step 3: Proofreading", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center')
    ax.text(82, 72, "Error Rate < 1 in 10,000\nDouble-Sieve Filter", fontsize=7.0, fontweight='bold', color=CRIMSON, ha='center')
    ax.text(82, 45, "• 20 distinct synthetases\n(one per amino acid)\n• Synthesis site rejects\nlarger incorrect amino acids\n• Separate editing site\nhydrolyses smaller incorrect\namino acids prematurely",
            fontsize=6.6, color=DARK_GREY, ha='center')

    ax.text(50, 8, "Aminoacyl-tRNA synthetases ensure the correct amino acid is matched to its cognate tRNA anticodon;\nessential for translational fidelity and maintaining the primary sequence integrity of the proteome",
            fontsize=7.0, fontweight='bold', color=NAVY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 6.14: DNA VS RNA CHEMICAL & STRUCTURAL COMPARISON
# ==============================================================================
def generate_fig6_14(filename="fig6_14_dna_vs_rna_chemical_comparison.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.8), dpi=300)

    # Panel A: Pentose Sugar Hydroxyl Difference (Deoxyribose vs Ribose)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("A: Pentose Ring Chemistry (C2' Carbon)", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    # Deoxyribose (Left)
    ax1.add_patch(FancyBboxPatch((4, 18), 44, 74, boxstyle="round,pad=0.4", facecolor="#eff6ff", edgecolor=NAVY, lw=1.3))
    ax1.text(26, 84, "2-Deoxyribose (DNA)", fontsize=7.6, fontweight='bold', color=NAVY, ha='center')
    # Pentose ring
    dx = [26, 34, 31, 21, 18]
    dy = [66, 60, 48, 48, 60]
    ax1.add_patch(Polygon(list(zip(dx, dy)), closed=True, facecolor="#bfdbfe", edgecolor=NAVY, lw=1.2))
    ax1.text(26, 56, "O", fontsize=7.0, fontweight='bold', color=NAVY, ha='center')
    # C2' has -H only (No OH)
    ax1.text(32, 42, "C2' - H", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(26, 26, "• Lacks oxygen at C2'\n• Highly stable against alkaline\nhydrolysis (long-term archive)",
             fontsize=6.6, color=DARK_GREY, ha='center')

    # Ribose (Right)
    ax1.add_patch(FancyBboxPatch((52, 18), 44, 74, boxstyle="round,pad=0.4", facecolor="#fef3c7", edgecolor=AMBER, lw=1.3))
    ax1.text(74, 84, "D-Ribose (RNA)", fontsize=7.6, fontweight='bold', color="#854d0e", ha='center')
    # Pentose ring
    rx = [74, 82, 79, 69, 66]
    ry = [66, 60, 48, 48, 60]
    ax1.add_patch(Polygon(list(zip(rx, ry)), closed=True, facecolor="#fde68a", edgecolor=AMBER, lw=1.2))
    ax1.text(74, 56, "O", fontsize=7.0, fontweight='bold', color=AMBER, ha='center')
    # C2' has -OH
    ax1.text(80, 42, "C2' - OH", fontsize=8.0, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(74, 26, "• Reactive 2'-OH group\n• Susceptible to self-cleavage;\nshort half-life for regulation",
             fontsize=6.6, color=DARK_GREY, ha='center')

    # Panel B: Summary Comparison Table
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title("B: Comprehensive Feature Comparison", fontsize=9.6, fontweight='bold', color=NAVY, pad=4)

    headers = ["Feature", "Deoxyribonucleic Acid (DNA)", "Ribonucleic Acid (RNA)"]
    cols_x = [18, 52, 84]
    ax2.add_patch(Rectangle((2, 78), 96, 9, facecolor=NAVY, edgecolor=NAVY))
    for h, x in zip(headers, cols_x):
        ax2.text(x, 82.5, h, fontsize=7.0, fontweight='bold', color=WHITE, ha='center', va='center')

    rows = [
        ("Pentose Sugar", "2-Deoxyribose (C5H10O4)", "D-Ribose (C5H10O5)"),
        ("Nitrogenous Bases", "A, C, G, Thymine (T)", "A, C, G, Uracil (U)"),
        ("Strand Structure", "Double-stranded helix", "Single-stranded (mRNA, tRNA)"),
        ("Stability & Lifetime", "Extremely stable (years)", "Transient (minutes to hours)"),
        ("Relative Length", "Millions of base pairs", "Tens to thousands of bases"),
        ("Primary Function", "Permanent genetic store", "Protein synthesis mediator")
    ]

    for idx, (f, d, r) in enumerate(rows):
        y_pos = 71.5 - idx * 7.4
        bg = "#f8fafc" if idx % 2 == 0 else WHITE
        ax2.add_patch(Rectangle((2, y_pos - 2.8), 96, 6.8, facecolor=bg, edgecolor="#cbd5e1", lw=0.7))
        ax2.text(cols_x[0], y_pos + 0.6, f, fontsize=6.8, fontweight='bold', color=DARK_GREY, ha='center')
        ax2.text(cols_x[1], y_pos + 0.6, d, fontsize=6.6, color=NAVY, ha='center')
        ax2.text(cols_x[2], y_pos + 0.6, r, fontsize=6.6, color=CRIMSON if "Uracil" in r else DARK_GREY, ha='center')

    ax2.text(50, 12, "Uracil is energetically cheaper to produce than thymine,\nmaking it ideal for short-lived messenger RNA transcripts",
             fontsize=6.8, color=NAVY, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=NAVY, lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("Generating Topic 6 High-Legibility Diagrams...")
    generate_fig6_1()
    generate_fig6_2()
    generate_fig6_3()
    generate_fig6_4()
    generate_fig6_5()
    generate_fig6_6()
    generate_fig6_7()
    generate_fig6_8()
    generate_fig6_9()
    generate_fig6_10()
    generate_fig6_11()
    generate_fig6_12()
    generate_fig6_13()
    generate_fig6_14()
    print("All 14 Topic 6 diagrams generated successfully.")

if __name__ == "__main__":
    main()
