"""
Vector Diagram Generator for Topic 11: Immunity
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Generates 14 high-resolution 300 DPI scientific figures:
- fig11_1: Hematopoietic stem cell lineage: myeloid (phagocytes) vs lymphoid (B & T cells)
- fig11_2: Step-by-step mechanism of phagocytosis: chemotaxis, phagosome, lysosome fusion, MHC II
- fig11_3: Molecular structure of IgG antibody: heavy/light chains, disulfide bonds, hinge, V & C domains
- fig11_4: Four effector mechanisms of antibodies: neutralisation, agglutination, opsonisation, lysis
- fig11_5: Clonal selection and clonal expansion: naive B-cells -> plasma cells & memory cells
- fig11_6: Ultrastructure of a mature antibody-secreting plasma cell (extensive RER, Golgi, nucleus)
- fig11_7: Primary vs secondary immune response curves: antibody titre, lag time, IgG vs IgM
- fig11_8: T-lymphocyte activation: T-helper cytokine signaling vs T-cytotoxic perforin/granzyme lysis
- fig11_9: Hybridoma technology for monoclonal antibody production (Köhler-Milstein, HAT selection)
- fig11_10: Lateral flow diagnostic mechanism of home pregnancy test strip (hCG detection)
- fig11_11: Therapeutic monoclonal antibody mechanism (Trastuzumab / Herceptin targeted cancer therapy)
- fig11_12: Classification matrix of immunity: Active vs Passive (Natural vs Artificial)
- fig11_13: Herd immunity and breaking disease transmission chains in populations
- fig11_14: Autoimmune mechanism of Myasthenia Gravis at the neuromuscular junction
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mentora Styling Colors
NAVY = "#0b1b36"
STEEL_BLUE = "#1e3a8a"
CRIMSON = "#a81717"
DARK_GREY = "#20242e"
LIGHT_BG = "#f8fafc"
BORDER_COLOR = "#cbd5e1"
RED_VESSEL = "#dc2626"
BLUE_VESSEL = "#2563eb"
PURPLE_ACCENT = "#7c3aed"
YELLOW_ACCENT = "#d97706"
GREEN_ACCENT = "#059669"
TEAL_ACCENT = "#0d9488"

def set_plot_style(ax, title=""):
    ax.set_facecolor("white")
    if title:
        ax.set_title(title, fontsize=11, fontweight="bold", color=NAVY, pad=12, family="sans-serif")
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(1.0)

# -----------------------------------------------------------------------------
# Fig 11.1: Hematopoietic Lineage of Immune Cells
# -----------------------------------------------------------------------------
def generate_fig11_1():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 11.1: Differentiation Lineage of Human Leukocytes: Myeloid vs Lymphoid")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Stem cell at top
    ax.add_patch(patches.FancyBboxPatch((3.5, 8.2), 3.0, 1.2, boxstyle="round,pad=0.15", facecolor="#dbeafe", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(5.0, 8.8, "Multipotent Hematopoietic\nStem Cell (Bone Marrow)", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # 2 Progenitor branches
    # Left: Myeloid Progenitor
    ax.add_patch(patches.FancyBboxPatch((0.8, 5.8), 3.6, 1.2, boxstyle="round,pad=0.15", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
    ax.text(2.6, 6.4, "Common Myeloid Progenitor\n(Innate Immune Lineage)", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Right: Lymphoid Progenitor
    ax.add_patch(patches.FancyBboxPatch((5.6, 5.8), 3.6, 1.2, boxstyle="round,pad=0.15", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(7.4, 6.4, "Common Lymphoid Progenitor\n(Adaptive Immune Lineage)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)

    # Arrows from Stem cell to Progenitors
    ax.annotate("", xy=(2.6, 7.0), xytext=(4.2, 8.2), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax.annotate("", xy=(7.4, 7.0), xytext=(5.8, 8.2), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # Myeloid Cells (Bottom Left)
    cells_myeloid = [
        ("Neutrophil", "Multi-lobed nucleus;\nshort-lived; acute phagocytosis;\nmost abundant WBC (~60-70%)", 0.5, 3.2),
        ("Monocyte / Macrophage", "Kidney-shaped nucleus;\nlong-lived in tissues;\nphagocytosis & antigen presentation", 0.5, 1.0)
    ]
    for name, desc, x, y in cells_myeloid:
        ax.add_patch(patches.FancyBboxPatch((x, y), 4.0, 1.8, boxstyle="round,pad=0.1", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.2))
        ax.text(x + 2.0, y + 1.35, name, ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
        ax.text(x + 2.0, y + 0.65, desc, ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    # Lymphoid Cells (Bottom Right)
    cells_lymphoid = [
        ("B-Lymphocyte (Bone Marrow)", "Matures in bone marrow;\nexpresses membrane-bound BCRs;\ndifferentiates into plasma/memory cells", 5.5, 3.2),
        ("T-Lymphocyte (Thymus)", "Matures in thymus gland;\nexpresses TCRs (CD4 / CD8);\nT-helper & Cytotoxic T-killer cells", 5.5, 1.0)
    ]
    for name, desc, x, y in cells_lymphoid:
        ax.add_patch(patches.FancyBboxPatch((x, y), 4.0, 1.8, boxstyle="round,pad=0.1", facecolor="#e0e7ff", edgecolor=STEEL_BLUE, lw=1.2))
        ax.text(x + 2.0, y + 1.35, name, ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)
        ax.text(x + 2.0, y + 0.65, desc, ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_1.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.2: Phagocytosis Step-by-Step
# -----------------------------------------------------------------------------
def generate_fig11_2():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.2: Cellular Stages of Phagocytosis by Macrophages and Antigen Presentation")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    steps = [
        ("1. Chemotaxis & Binding", "Attracted by cytokines;\nPRRs bind PAMPs or\nFc receptors bind opsonins.", "#eff6ff", STEEL_BLUE, 0.5),
        ("2. Ingestion & Phagosome", "Pseudopodia engulf bacterium\nforming a membrane-bound\nphagosome vesicle.", "#fff7ed", "#ea580c", 2.8),
        ("3. Phagolysosome Lysis", "Lysosomes fuse; lysozyme,\nacid proteases & ROS\ndigest pathogen components.", "#fee2e2", CRIMSON, 5.1),
        ("4. Exocytosis & MHC II", "Indigestible debris exocytosed;\nepitopes loaded onto MHC II\nfor T-cell presentation.", "#dcfce7", GREEN_ACCENT, 7.4)
    ]

    for title, desc, bg, edge, x in steps:
        box = patches.FancyBboxPatch((x, 3.8), 2.1, 5.2, boxstyle="round,pad=0.15", facecolor=bg, edgecolor=edge, lw=1.5)
        ax.add_patch(box)
        ax.text(x + 1.05, 8.4, title, ha="center", va="center", fontsize=7.5, fontweight="bold", color=edge)
        ax.text(x + 1.05, 5.8, desc, ha="center", va="center", fontsize=7, color=DARK_GREY)

    for ax_pt in [2.65, 4.95, 7.25]:
        ax.annotate("", xy=(ax_pt + 0.15, 6.2), xytext=(ax_pt - 0.05, 6.2), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # Bottom Callout: Macrophage vs Neutrophil
    bot_box = patches.FancyBboxPatch((0.5, 0.5), 9.0, 2.6, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 2.6, "FUNCTIONAL COMPARISON: NEUTROPHILS VS MACROPHAGES", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.text(2.6, 1.4, "NEUTROPHILS:\n• Short-lived (~few days); die after phagocytosis (pus)\n• Strictly phagocytic; do NOT present antigens\n• Rapid response, abundant in acute bacterial infection", ha="center", va="center", fontsize=7, color=DARK_GREY)
    ax.text(7.4, 1.4, "MACROPHAGES:\n• Long-lived (months/years); survive multiple meals\n• Professional Antigen-Presenting Cells (APCs)\n• Display processed antigens on MHC II to activate Th cells", ha="center", va="center", fontsize=7, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_2.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.3: Molecular Anatomy of IgG Antibody
# -----------------------------------------------------------------------------
def generate_fig11_3():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 11.3: Molecular Structure of an IgG Antibody (Immunoglobulin)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Left Heavy Chain (Navy, thick)
    # Stem (bottom vertical) + Left arm (angled)
    ax.plot([4.6, 4.6], [1.5, 5.0], color=NAVY, lw=5)
    ax.plot([4.6, 2.2], [5.0, 8.2], color=NAVY, lw=5)

    # Right Heavy Chain (Navy, thick)
    ax.plot([5.4, 5.4], [1.5, 5.0], color=NAVY, lw=5)
    ax.plot([5.4, 7.8], [5.0, 8.2], color=NAVY, lw=5)

    # Left Light Chain (Steel Blue, outer)
    ax.plot([3.5, 1.6], [5.5, 8.2], color=STEEL_BLUE, lw=4)

    # Right Light Chain (Steel Blue, outer)
    ax.plot([6.5, 8.4], [5.5, 8.2], color=STEEL_BLUE, lw=4)

    # Disulfide bonds (-S-S-)
    # Between heavy chains in hinge
    ax.plot([4.6, 5.4], [4.6, 4.6], color=YELLOW_ACCENT, lw=3)
    ax.plot([4.6, 5.4], [4.9, 4.9], color=YELLOW_ACCENT, lw=3)
    ax.text(5.0, 4.4, "Interchain Disulfide\nBonds (-S-S-)", ha="center", va="top", fontsize=6.8, fontweight="bold", color="#854d0e")

    # Between heavy and light chains
    ax.plot([3.3, 3.6], [5.8, 6.2], color=YELLOW_ACCENT, lw=2.5)
    ax.plot([6.7, 6.4], [5.8, 6.2], color=YELLOW_ACCENT, lw=2.5)

    # Variable Regions (top of arms, highlighted in red)
    # Left Fab tip
    ax.plot([2.2, 2.8], [8.2, 7.4], color=CRIMSON, lw=7)
    ax.plot([1.6, 2.2], [8.2, 7.4], color=CRIMSON, lw=6)
    # Right Fab tip
    ax.plot([7.8, 7.2], [8.2, 7.4], color=CRIMSON, lw=7)
    ax.plot([8.4, 7.8], [8.2, 7.4], color=CRIMSON, lw=6)

    # Annotations:
    # 1. Antigen-binding sites
    ax.annotate("Antigen-Binding Site 1\n(VH + VL Domains)\nUnique complementary shape", xy=(1.9, 8.3), xytext=(0.5, 9.2),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                fontsize=7.5, fontweight="bold", color=CRIMSON)

    ax.annotate("Antigen-Binding Site 2\n(VH + VL Domains)\nIdentical to Site 1 (Bivalent)", xy=(8.1, 8.3), xytext=(6.5, 9.2),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                fontsize=7.5, fontweight="bold", color=CRIMSON)

    # 2. Hinge Region
    ax.annotate("Flexible Hinge Region\n(Proline-rich; allows arms\nto angle between 60°-180°)", xy=(4.6, 5.2), xytext=(1.2, 4.8),
                arrowprops=dict(arrowstyle="->", color=STEEL_BLUE, lw=1.5),
                fontsize=7.2, color=STEEL_BLUE)

    # 3. Constant Region / Fc Stem
    ax.annotate("Constant Region (Fc Stem)\n• Binds phagocyte Fc receptors (Opsonisation)\n• Activates Complement cascade (C1q)\n• Crosses placenta to fetus (IgG)",
                xy=(5.4, 2.8), xytext=(6.2, 2.8),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5),
                fontsize=7.2, color=NAVY)

    # 4. Chain labels
    ax.text(5.0, 1.0, "2 Identical Heavy (H) Chains  |  2 Identical Light (L) Chains", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_3.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.4: Four Effector Mechanisms of Antibodies
# -----------------------------------------------------------------------------
def generate_fig11_4():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.4: Four Effector Mechanisms of Antibodies in Pathogen Clearance")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    cards = [
        ("1. Neutralisation", "Antibodies bind bacterial toxins\n(antitoxins) or viral surface\nglycoproteins, blocking host\nreceptor binding and cell entry.", "#dbeafe", STEEL_BLUE, 0.5, 5.2),
        ("2. Agglutination", "Bivalent antibodies cross-link\nmultiple bacterial cells into\nlarge insoluble clumps, immobilising\nthem and facilitating phagocytosis.", "#fee2e2", CRIMSON, 5.3, 5.2),
        ("3. Opsonisation", "Antibody Fab binds bacterial\nantigen while Fc stem projects\noutward to bind Fc receptors\non phagocytes, stimulating ingestion.", "#fef3c7", "#ca8a04", 0.5, 0.5),
        ("4. Complement Lysis", "Fc regions bind complement C1q,\ntriggering enzyme cascade that\nassembles Membrane Attack\nComplex (MAC) pores in membrane.", "#f0fdf4", GREEN_ACCENT, 5.3, 0.5)
    ]

    for title, desc, bg, edge, x, y in cards:
        box = patches.FancyBboxPatch((x, y), 4.2, 4.2, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=edge, lw=1.5)
        ax.add_patch(box)
        ax.text(x + 2.1, y + 3.6, title, ha="center", va="center", fontsize=8.5, fontweight="bold", color=edge)
        ax.text(x + 2.1, y + 1.8, desc, ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_4.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.5: Clonal Selection and Clonal Expansion
# -----------------------------------------------------------------------------
def generate_fig11_5():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 11.5: Burnet's Clonal Selection Theory: Activation, Proliferation & Differentiation")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Step 1: Diverse Naive B-cell Clones (Top)
    ax.text(5.0, 9.4, "1. DIVERSE NAIVE B-CELL CLONES (Each clone has unique BCR specific for one epitope)", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    clones = [("Clone A (circle)", 2.0, "#dbeafe", STEEL_BLUE),
              ("Clone B (SELECTED)", 5.0, "#fee2e2", CRIMSON),
              ("Clone C (square)", 8.0, "#dcfce7", GREEN_ACCENT)]
    for label, cx, bg, edge in clones:
        ax.add_patch(patches.Circle((cx, 8.2), 0.6, facecolor=bg, edgecolor=edge, lw=2))
        ax.text(cx, 8.2, "B", ha="center", va="center", fontsize=8, fontweight="bold", color=edge)
        ax.text(cx, 7.3, label, ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    # Antigen selection on Clone B
    ax.plot(5.0, 9.0, "*", color=YELLOW_ACCENT, markersize=10)
    ax.text(5.0, 9.0, "   Foreign Antigen\n   binds Clone B!", ha="left", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    # Step 2: Clonal Selection & Mitotic Expansion
    ax.annotate("CLONAL SELECTION\n(Th cell cytokines IL-2 / IL-4)", xy=(5.0, 6.2), xytext=(5.0, 7.0),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.5),
                fontsize=7.5, fontweight="bold", color=CRIMSON, ha="center")

    ax.text(5.0, 5.8, "2. CLONAL EXPANSION (Repeated rounds of rapid mitosis yield thousands of identical daughter cells)", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    for mx in [3.8, 4.6, 5.4, 6.2]:
        ax.add_patch(patches.Circle((mx, 4.8), 0.35, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
        ax.text(mx, 4.8, "B", ha="center", va="center", fontsize=6.5, color=CRIMSON)

    # Step 3: Differentiation into Plasma Cells and Memory Cells
    ax.annotate("", xy=(3.0, 3.4), xytext=(4.5, 4.4), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax.annotate("", xy=(7.0, 3.4), xytext=(5.5, 4.4), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # Left: Plasma Cells
    p_box = patches.FancyBboxPatch((0.8, 0.8), 4.0, 2.4, boxstyle="round,pad=0.15", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(p_box)
    ax.text(2.8, 2.8, "PLASMA CELLS (Effector Cells)", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax.text(2.8, 1.8, "• Short-lived (~few days)\n• Extensive rough ER & Golgi\n• Secrete ~2,000 specific antibody\n  molecules per second into plasma\n• Destroy active pathogen", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Right: Memory B-Cells
    m_box = patches.FancyBboxPatch((5.2, 0.8), 4.0, 2.4, boxstyle="round,pad=0.15", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5)
    ax.add_patch(m_box)
    ax.text(7.2, 2.8, "MEMORY B-CELLS (Immunological Memory)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)
    ax.text(7.2, 1.8, "• Long-lived (survive decades)\n• Retain membrane-bound BCRs\n• Circulate in lymph & blood\n• Divide rapidly upon re-exposure\n• Drive rapid secondary response", ha="center", va="center", fontsize=7, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_5.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.6: Ultrastructure of Mature Plasma Cell
# -----------------------------------------------------------------------------
def generate_fig11_6():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 11.6: Ultrastructural Adaptations of an Antibody-Secreting Plasma Cell")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Cell membrane (outer ellipse)
    ax.add_patch(patches.Ellipse((5, 5), 8.5, 7.5, facecolor="#fff7ed", edgecolor=NAVY, lw=2.0))
    ax.text(5, 9.0, "PLASMA CELL SURFACE MEMBRANE", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Eccentric Nucleus with 'Clock-Face' / Cartwheel Chromatin
    ax.add_patch(patches.Circle((3.0, 5.0), 1.8, facecolor="#c7d2fe", edgecolor=NAVY, lw=1.5))
    ax.text(3.0, 5.0, "Nucleus\n('Clock-face'\nchromatin)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    # Heterochromatin wedges
    for angle in np.linspace(0, 360, 8, endpoint=False):
        rad = np.radians(angle)
        ax.plot([3.0, 3.0 + 1.6*np.cos(rad)], [5.0, 5.0 + 1.6*np.sin(rad)], color=NAVY, lw=2)

    # Extensive Parallel Rough Endoplasmic Reticulum (RER)
    for x in np.linspace(5.5, 8.2, 7):
        ax.plot([x, x], [2.2, 7.8], color=CRIMSON, lw=2.5)
        # Ribosomes on RER
        for ry in np.linspace(2.5, 7.5, 8):
            ax.plot(x + 0.1, ry, "o", color=NAVY, markersize=2)
            ax.plot(x - 0.1, ry, "o", color=NAVY, markersize=2)
    ax.text(6.8, 8.2, "Extensive Rough Endoplasmic Reticulum (RER)\n(Synthesises antibody heavy and light chains)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Golgi Apparatus
    for gy in [4.5, 5.0, 5.5]:
        ax.add_patch(patches.Arc((4.6, gy), 1.2, 0.4, angle=0, theta1=200, theta2=340, color=STEEL_BLUE, lw=2))
    ax.text(4.6, 3.8, "Prominent Golgi\n(Glycosylates &\npackages IgG)", ha="center", va="center", fontsize=7, color=STEEL_BLUE)

    # Abundant Mitochondria
    for mx, my in [(2.2, 2.4), (4.2, 2.0), (7.5, 1.8), (3.8, 7.6)]:
        ax.add_patch(patches.Ellipse((mx, my), 0.7, 0.35, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.2))
        ax.plot(mx, my, "x", color=CRIMSON, markersize=4)
    ax.text(2.2, 1.6, "Mitochondria (ATP)", ha="center", va="center", fontsize=6.8, color=CRIMSON)

    # Secretory Vesicles budding off (Antibody Exocytosis)
    for vx, vy in [(8.8, 6.0), (9.0, 4.5), (8.7, 3.2)]:
        ax.add_patch(patches.Circle((vx, vy), 0.2, facecolor="#bfdbfe", edgecolor=STEEL_BLUE, lw=1.2))
    ax.annotate("Exocytosis of IgG Antibodies\n(~2,000 molecules/second!)", xy=(8.9, 5.0), xytext=(7.5, 0.6),
                arrowprops=dict(arrowstyle="->", color=STEEL_BLUE, lw=2),
                fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_6.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.7: Primary vs Secondary Immune Response Curves
# -----------------------------------------------------------------------------
def generate_fig11_7():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.7: Primary vs Secondary Immune Response Dynamics (Antibody Titre)")

    days = np.linspace(0, 60, 600)
    # First exposure at Day 0: Lag of 7 days, peaks at day 16 (titre ~10), declines to baseline by day 28
    prim = np.zeros_like(days)
    for i, d in enumerate(days):
        if 7 <= d <= 28:
            prim[i] = 10 * np.exp(-((d - 16)/5)**2)

    # Second exposure at Day 30: Lag of 1 day, peaks at day 38 (titre ~100), stays elevated > 40 at day 60
    sec = np.zeros_like(days)
    for i, d in enumerate(days):
        if d >= 31:
            if d <= 38:
                sec[i] = 100 * ((d - 31)/7)**2
            else:
                sec[i] = 40 + 60 * np.exp(-0.06 * (d - 38))

    ax.plot(days, prim, color=STEEL_BLUE, lw=2.2, label="Primary Response (Mainly IgM; Low Titre)")
    ax.plot(days, sec, color=CRIMSON, lw=2.5, label="Secondary Response (Mainly IgG; High Titre)")

    ax.set_xlim(0, 60)
    ax.set_ylim(0, 115)
    ax.set_xlabel("Time / days", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.set_ylabel("Plasma Antibody Concentration / arbitrary units", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.legend(loc="upper left", fontsize=8)

    # Exposure arrows
    ax.annotate("Primary Antigen\nExposure (Day 0)", xy=(0, 5), xytext=(2, 35),
                arrowprops=dict(arrowstyle="->", color=STEEL_BLUE, lw=1.8),
                fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    ax.annotate("Secondary Re-Exposure\nIdentical Antigen (Day 30)", xy=(30, 5), xytext=(32, 70),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2),
                fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Key Comparative Metrics Box
    c_box = patches.FancyBboxPatch((15, 65), 18, 42, boxstyle="round,pad=0.5", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.2)
    ax.add_patch(c_box)
    ax.text(24, 102, "CRITICAL EXAM COMPARISONS", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    ax.text(24, 82, "• Lag Phase: Long (7-10d) vs Short (1-2d)\n• Rate of Synthesis: Slow vs Rapid & Steep\n• Peak Titre: Low (~10) vs 10x Higher (~100)\n• Dominant Isotype: IgM vs IgG\n• Duration: Transient vs Long-lasting",
            ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_7.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.8: T-Lymphocyte Activation & Cytotoxic Action
# -----------------------------------------------------------------------------
def generate_fig11_8():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: T-Helper Cell (CD4+) Activation
    set_plot_style(ax1, "T-Helper (CD4+) Activation & Signaling")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    c1 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5)
    ax1.add_patch(c1)
    ax1.text(5.0, 8.5, "T-HELPER (Th) CELL", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax1.text(5.0, 5.0, "1. ANTIGEN PRESENTATION:\n• Macrophage / Dendritic cell displays\n  antigen fragment on MHC CLASS II\n• T-cell Receptor (TCR) & CD4 co-receptor\n  bind specifically to MHC II-antigen complex\n\n2. CYTOKINE SECRETION:\n• Activated Th cell secretes INTERLEUKINS\n  (IL-2, IL-4, IFN-γ)\n\n3. COORDINATING IMMUNE ARM:\n• Activates B-cells -> clonal expansion\n• Stimulates Cytotoxic T-cells\n• Enhances macrophage phagocytosis",
             ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Ax2: Cytotoxic T-Killer (CD8+) Lysis
    set_plot_style(ax2, "Cytotoxic T-Killer (CD8+) Target Lysis")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    c2 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax2.add_patch(c2)
    ax2.text(5.0, 8.5, "CYTOTOXIC T-KILLER (Tc) CELL", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax2.text(5.0, 5.0, "1. TARGET RECOGNITION:\n• Virus-infected or cancer cell displays\n  foreign viral peptide on MHC CLASS I\n• Tc cell TCR & CD8 bind target complex\n\n2. RELEASE OF LETHAL GRANULES:\n• PERFORIN: Polymerises in target cell\n  membrane to create transmembrane pores\n• GRANZYMES: Serine proteases enter pores\n  and activate CASPASES\n\n3. APOPTOSIS:\n• Induces programmed cell death (lysis)\n• Pathogen destroyed inside dying cell",
             ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_8.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.9: Hybridoma Method for Monoclonal Antibody Production
# -----------------------------------------------------------------------------
def generate_fig11_9():
    fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
    set_plot_style(ax, "Fig. 11.9: The Köhler-Milstein Hybridoma Technology for Monoclonal Antibody Production")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Step 1: Immunisation of Mouse (Top Left)
    ax.add_patch(patches.FancyBboxPatch((0.5, 7.6), 4.2, 1.8, boxstyle="round,pad=0.15", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5))
    ax.text(2.6, 8.8, "1. IMMUNISE MOUSE", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax.text(2.6, 8.1, "• Inject target antigen\n• Harvest SPLEEN B-CELLS\n  (Produce specific Ab; mortal)", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Step 2: Myeloma Cells (Top Right)
    ax.add_patch(patches.FancyBboxPatch((5.3, 7.6), 4.2, 1.8, boxstyle="round,pad=0.15", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(7.4, 8.8, "2. MYELOMA CELLS", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)
    ax.text(7.4, 8.1, "• Mutant cancerous plasma cells\n• Divide indefinitely (IMMORTAL)\n• Lack HGPRT; produce no Ab", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Step 3: Fusion via PEG (Middle)
    ax.annotate("", xy=(4.5, 6.4), xytext=(2.6, 7.6), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax.annotate("", xy=(5.5, 6.4), xytext=(7.4, 7.6), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    fuse_box = patches.FancyBboxPatch((2.5, 4.8), 5.0, 1.5, boxstyle="round,pad=0.15", facecolor="#fef3c7", edgecolor="#ca8a04", lw=1.5)
    ax.add_patch(fuse_box)
    ax.text(5.0, 5.8, "3. FUSION (Polyethylene Glycol - PEG)", ha="center", va="center", fontsize=8, fontweight="bold", color="#854d0e")
    ax.text(5.0, 5.2, "Fuses plasma membranes to form HYBRIDOMA CELLS\n(Inherit antibody secretion from B-cell + immortality from myeloma)", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Step 4: HAT Selection & Screening (Bottom)
    hat_box = patches.FancyBboxPatch((0.5, 2.2), 9.0, 2.2, boxstyle="round,pad=0.15", facecolor="#f0fdf4", edgecolor=GREEN_ACCENT, lw=1.5)
    ax.add_patch(hat_box)
    ax.text(5.0, 3.8, "4. SELECTION ON HAT MEDIUM & CLONAL SCREENING", ha="center", va="center", fontsize=8, fontweight="bold", color=GREEN_ACCENT)
    ax.text(5.0, 2.8, "• HAT Medium: Unfused myeloma cells die (aminopterin blocks de novo synthesis; lack HGPRT for salvage)\n  Unfused spleen B-cells die naturally; ONLY HYBRIDOMAS SURVIVE!\n• Single-cell cloning via limiting dilution -> ELISA screening for desired antibody clone",
            ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Step 5: Large Scale Production (Bottom Banner)
    bot_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.4, boxstyle="round,pad=0.1", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 1.3, "5. INDUSTRIAL BIOREACTOR CULTURE", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(5.0, 0.8, "Positive hybridoma clone cultured indefinitely to produce massive quantities of pure, monospecific monoclonal antibodies", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_9.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.10: Pregnancy Test Kit Mechanism
# -----------------------------------------------------------------------------
def generate_fig11_10():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.10: Lateral Flow Diagnostic Mechanism of a Home Pregnancy Test Strip")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Lateral flow test strip body
    ax.add_patch(patches.Rectangle((0.5, 3.5), 9.0, 3.0, facecolor="#f8fafc", edgecolor=NAVY, lw=2.0))

    # Zone 1: Reaction Zone / Sample Pad (0.5 to 3.0)
    ax.add_patch(patches.Rectangle((0.5, 3.5), 2.5, 3.0, facecolor="#eff6ff", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.75, 5.8, "REACTION ZONE", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)
    ax.text(1.75, 4.6, "Mobile anti-hCG mAbs\nconjugated to blue\ncolloidal dye / gold\n(Free to move)", ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    # Zone 2: Test Line (5.0)
    ax.plot([5.0, 5.0], [3.5, 6.5], color=CRIMSON, lw=4)
    ax.text(5.0, 5.8, "TEST LINE (T)", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax.text(5.0, 4.2, "Immobilised anti-hCG\nmAbs bind hCG-mAb complex\n-> Blue Line (Pregnant!)", ha="center", va="top", fontsize=6.8, color=CRIMSON)

    # Zone 3: Control Line (7.5)
    ax.plot([7.5, 7.5], [3.5, 6.5], color=BLUE_VESSEL, lw=4)
    ax.text(7.5, 5.8, "CONTROL LINE (C)", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)
    ax.text(7.5, 4.2, "Immobilised anti-mouse\nantibodies bind mobile mAbs\n-> Proves test functioned", ha="center", va="top", fontsize=6.8, color=BLUE_VESSEL)

    # Urine flow arrow (capillary action)
    ax.annotate("Urine Capillary Flow (contains hCG in pregnancy)", xy=(8.5, 2.5), xytext=(1.5, 2.5),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5),
                fontsize=8, fontweight="bold", color=NAVY)

    # Interpretation Guide at bottom
    bot_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.6, boxstyle="round,pad=0.1", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.2)
    ax.add_patch(bot_box)
    ax.text(5.0, 1.6, "TEST INTERPRETATION", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(2.6, 0.9, "• 2 LINES (T + C): PREGNANT\n  (hCG present; sandwich formed at test line)", ha="center", va="center", fontsize=7.2, fontweight="bold", color=CRIMSON)
    ax.text(7.4, 0.9, "• 1 LINE (C only): NOT PREGNANT\n• NO LINES / T ONLY: INVALID TEST (Faulty)", ha="center", va="center", fontsize=7.2, fontweight="bold", color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_10.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.11: Therapeutic Monoclonal Antibodies (Trastuzumab / Herceptin)
# -----------------------------------------------------------------------------
def generate_fig11_11():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.11: Targeted Cancer Therapy: Trastuzumab (Herceptin) Blocking HER2 Receptors")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Breast cancer cell membrane (bottom half)
    ax.add_patch(patches.Rectangle((0.5, 1.0), 9.0, 4.0, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.8))
    ax.text(5.0, 2.0, "HER2-OVEREXPRESSING BREAST CANCER CELL CYTOPLASM", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # HER2 Receptors on membrane
    for hx in [3.0, 5.0, 7.0]:
        ax.plot([hx, hx], [4.5, 6.0], color=STEEL_BLUE, lw=4)
        ax.plot(hx, 6.2, "o", color=STEEL_BLUE, markersize=8)
    ax.text(5.0, 6.8, "Overexpressed HER2 Receptor Tyrosine Kinases", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # Trastuzumab (Herceptin) mAbs binding to HER2
    for hx in [3.0, 5.0, 7.0]:
        # Y-shaped mAb
        ax.plot([hx, hx-0.4], [6.2, 7.2], color=CRIMSON, lw=3)
        ax.plot([hx, hx+0.4], [6.2, 7.2], color=CRIMSON, lw=3)
        ax.plot([hx, hx], [7.2, 8.2], color=CRIMSON, lw=3)
    ax.text(5.0, 8.8, "Trastuzumab (Herceptin) Monoclonal Antibodies", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Mechanisms Callout
    m1 = patches.FancyBboxPatch((0.5, 0.4), 4.2, 1.2, boxstyle="round,pad=0.1", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.2)
    ax.add_patch(m1)
    ax.text(2.6, 1.0, "A. Blocks Receptor Dimerisation\nPrevents uncontrolled mitotic growth signals", ha="center", va="center", fontsize=6.8, fontweight="bold", color=STEEL_BLUE)

    m2 = patches.FancyBboxPatch((5.3, 0.4), 4.2, 1.2, boxstyle="round,pad=0.1", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.2)
    ax.add_patch(m2)
    ax.text(7.4, 1.0, "B. Antibody-Dependent Cytotoxicity (ADCC)\nFc domain recruits NK cells to lyse tumor", ha="center", va="center", fontsize=6.8, fontweight="bold", color=STEEL_BLUE)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_11.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.12: Immunity Classification Matrix
# -----------------------------------------------------------------------------
def generate_fig11_12():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 11.12: Classification Matrix of Immunity: Active vs Passive (Natural vs Artificial)")
    ax.axis("off")

    columns = ["Type", "Natural", "Artificial", "Memory Cells Formed?", "Duration of Protection"]
    rows = [
        ["Active Immunity\n(Host makes own antibodies)",
         "Natural Infection\n(e.g. contracting chickenpox\nor measles)",
         "Vaccination\n(e.g. injected with attenuated\npathogen, toxoid, or mRNA)",
         "YES (B & T memory\ncells persist)",
         "LONG-TERM\n(Years to lifetime)"],
        ["Passive Immunity\n(Host receives pre-formed Abs)",
         "Maternal Transfer\n(IgG across placenta;\nsecretory IgA in breast milk)",
         "Antitoxin / Antivenom\n(e.g. tetanus antitoxin,\nrabies Ig, snake antivenom)",
         "NO (Immune system\nnot activated)",
         "SHORT-TERM\n(Weeks to few months;\nAbs broken down)"]
    ]

    cell_colors = [
        ["#dbeafe", "#eff6ff", "#eff6ff", "#f0fdf4", "#f0fdf4"],
        ["#fee2e2", "#fef2f2", "#fef2f2", "#fff1f2", "#fff1f2"]
    ]

    table = ax.table(cellText=rows, colLabels=columns, cellColours=cell_colors,
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1.0, 2.5)

    for col in range(len(columns)):
        cell = table[0, col]
        cell.set_facecolor(NAVY)
        cell.set_text_props(color="white", fontweight="bold", fontsize=8)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_12.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.13: Population Epidemiology of Herd Immunity
# -----------------------------------------------------------------------------
def generate_fig11_13():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Low Vaccination Coverage (< 50%)
    set_plot_style(ax1, "Low Vaccination Coverage: Outbreak Spreads")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    c1 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5)
    ax1.add_patch(c1)
    ax1.text(5.0, 8.5, "CHAINS OF TRANSMISSION INTACT", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax1.text(5.0, 5.0, "• Few individuals vaccinated\n• Infected person easily contacts\n  susceptible individuals\n• Rapid transmission through population\n• High contagion rate (R > 1)\n• Outbreaks occur; vulnerable &\n  unvaccinated contract disease",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: High Vaccination Coverage (Herd Immunity > 90%)
    set_plot_style(ax2, "High Vaccination Coverage: Herd Immunity")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    c2 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#f0fdf4", edgecolor=GREEN_ACCENT, lw=1.5)
    ax2.add_patch(c2)
    ax2.text(5.0, 8.5, "TRANSMISSION CHAINS BROKEN", ha="center", va="center", fontsize=8, fontweight="bold", color=GREEN_ACCENT)
    ax2.text(5.0, 5.0, "• Majority (> 90%) vaccinated & immune\n• Infected person rarely contacts\n  a susceptible person\n• Pathogen cannot find new hosts (R < 1)\n• Transmission chain dies out\n• COCOON EFFECT: Protects individuals\n  who cannot be vaccinated (e.g. infants,\n  leukemia patients, immunosuppressed)",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_13.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 11.14: Autoimmune Pathogenesis of Myasthenia Gravis
# -----------------------------------------------------------------------------
def generate_fig11_14():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Normal Neuromuscular Junction
    set_plot_style(ax1, "Normal Neuromuscular Junction")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    # Axon terminal
    ax1.add_patch(patches.Rectangle((1.5, 6.5), 7.0, 2.5, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax1.text(5.0, 7.8, "Motor Neuron Axon Terminal", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # ACh vesicles
    for vx, vy in [(3.0, 7.0), (4.2, 6.8), (5.5, 7.1), (6.8, 6.9)]:
        ax1.add_patch(patches.Circle((vx, vy), 0.22, facecolor="#fed7aa", edgecolor="#ea580c", lw=1))
    ax1.text(5.0, 6.2, "ACh Released into Synaptic Cleft", ha="center", va="center", fontsize=7, color="#ea580c")

    # Postsynaptic Sarcolemma with abundant ACh Receptors
    ax1.add_patch(patches.Rectangle((1.5, 2.0), 7.0, 3.0, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
    ax1.text(5.0, 2.5, "Muscle Sarcolemma (Normal Contraction)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Abundant intact receptors
    for rx in [2.5, 3.8, 5.0, 6.2, 7.5]:
        ax1.add_patch(patches.Rectangle((rx-0.2, 4.8), 0.4, 0.6, facecolor=GREEN_ACCENT, edgecolor=NAVY, lw=1))
    ax1.text(5.0, 3.8, "Abundant Nicotinic ACh Receptors\n-> Normal End-Plate Potential -> Contraction", ha="center", va="center", fontsize=6.8, color=DARK_GREY)

    # Ax2: Myasthenia Gravis
    set_plot_style(ax2, "Myasthenia Gravis (Autoimmune)")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    # Axon terminal
    ax2.add_patch(patches.Rectangle((1.5, 6.5), 7.0, 2.5, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax2.text(5.0, 7.8, "Motor Neuron Axon Terminal\n(Normal ACh Release)", ha="center", va="center", fontsize=7.5, color=STEEL_BLUE)

    # Postsynaptic Sarcolemma with autoantibodies blocking receptors
    ax2.add_patch(patches.Rectangle((1.5, 2.0), 7.0, 3.0, facecolor="#fef2f2", edgecolor=CRIMSON, lw=1.5))
    ax2.text(5.0, 2.5, "Sarcolemma: Muscle Weakness / Fatigue", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Blocked and endocytosed receptors
    ax2.plot(3.5, 5.0, "x", color=CRIMSON, markersize=10, markeredgewidth=2)
    ax2.plot(5.0, 5.0, "x", color=CRIMSON, markersize=10, markeredgewidth=2)
    ax2.plot(6.5, 5.0, "x", color=CRIMSON, markersize=10, markeredgewidth=2)

    # Autoantibodies
    ax2.text(5.0, 4.2, "AUTOANTIBODIES bind ACh receptors:\n• Competitively block ACh binding\n• Complement-mediated receptor destruction\n• Receptor endocytosis & loss\n-> Progressive Muscle Weakness (Ptosis, Dysphagia)",
             ha="center", va="center", fontsize=6.8, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig11_14.png"), dpi=300)
    plt.close(fig)

def main():
    print("Generating 14 vector diagrams for Topic 11: Immunity...")
    generate_fig11_1()
    generate_fig11_2()
    generate_fig11_3()
    generate_fig11_4()
    generate_fig11_5()
    generate_fig11_6()
    generate_fig11_7()
    generate_fig11_8()
    generate_fig11_9()
    generate_fig11_10()
    generate_fig11_11()
    generate_fig11_12()
    generate_fig11_13()
    generate_fig11_14()
    print("All 14 Topic 11 figures generated successfully in 300 DPI!")

if __name__ == "__main__":
    main()
