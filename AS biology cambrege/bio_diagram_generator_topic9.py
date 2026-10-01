"""
Vector Diagram Generator for Topic 9: Gas Exchange
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Generates 14 high-resolution 300 DPI scientific figures:
- fig9_1: Gross anatomy of human respiratory system (trachea, bronchi, bronchioles, lungs, diaphragm)
- fig9_2: Histological cross-section (TS) of trachea wall (cartilage C-ring, epithelium, glands)
- fig9_3: Ultrastructure of ciliated epithelial cells, goblet cells & mucociliary escalator
- fig9_4: Comparative histology: TS bronchus (cartilage plates) vs TS bronchiole (no cartilage)
- fig9_5: Alveolar-capillary diffusion barrier (type I/II pneumocytes, endothelial cells, 0.5 µm path)
- fig9_6: Alveolar elastic fibre dynamics (inhalation expansion vs passive recoil)
- fig9_7: Spirometry lung volume trace (VT, IRV, ERV, RV, VC, TLC)
- fig9_8: Fick's Law of Diffusion applied to alveolar partial pressure gradients
- fig9_9: Histopathology of chronic bronchitis (goblet hyperplasia, ciliostasis, mucus plugs)
- fig9_10: Pathogenesis of emphysema (elastase destruction of septa, loss of recoil, coalescence)
- fig9_11: Tobacco smoke triad: Nicotine, Carbon Monoxide, and Tar modes of action
- fig9_12: Multi-step bronchogenic carcinoma progression (normal -> metaplasia -> invasive tumor)
- fig9_13: Mechanics of ventilation: thoracic volume and pressure dynamics during breathing
- fig9_14: Tissue distribution matrix across the respiratory tract (trachea to alveoli)
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
CARTILAGE_COLOR = "#c7d2fe"

def set_plot_style(ax, title=""):
    ax.set_facecolor("white")
    if title:
        ax.set_title(title, fontsize=11, fontweight="bold", color=NAVY, pad=12, family="sans-serif")
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(1.0)

# -----------------------------------------------------------------------------
# Fig 9.1: Gross Anatomy of Respiratory System
# -----------------------------------------------------------------------------
def generate_fig9_1():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.1: Gross Anatomy of the Human Gas Exchange System")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Larynx
    ax.add_patch(patches.Rectangle((4.6, 8.8), 0.8, 0.6, facecolor="#e2e8f0", edgecolor=NAVY, lw=1.5))
    ax.text(5.0, 9.1, "Larynx", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Trachea with cartilage C-rings
    ax.add_patch(patches.Rectangle((4.7, 6.6), 0.6, 2.2, facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5))
    for y in np.linspace(6.8, 8.6, 7):
        ax.add_patch(patches.Arc((5.0, y), 0.55, 0.2, angle=0, theta1=200, theta2=340, color=STEEL_BLUE, lw=2.0))
    ax.text(5.0, 7.7, "Trachea\n(C-rings)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # Left & Right Bronchi
    ax.plot([4.7, 3.2], [6.6, 5.2], color=NAVY, lw=4)
    ax.plot([5.3, 6.8], [6.6, 5.2], color=NAVY, lw=4)
    ax.text(3.5, 6.2, "Right Main\nBronchus", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    ax.text(6.5, 6.2, "Left Main\nBronchus", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Lungs outlines
    # Right Lung (3 lobes)
    right_lung = patches.Polygon([[1.8, 2.2], [1.5, 4.5], [2.2, 6.2], [4.4, 5.8], [4.3, 2.2], [3.2, 1.8]],
                                 closed=True, facecolor="#fee2e2", edgecolor=CRIMSON, lw=2.0, alpha=0.6)
    ax.add_patch(right_lung)
    ax.text(2.8, 3.8, "Right Lung\n(3 Lobes)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)

    # Left Lung (2 lobes + cardiac notch)
    left_lung = patches.Polygon([[8.2, 2.2], [8.5, 4.5], [7.8, 6.2], [5.6, 5.8], [5.8, 3.8], [6.8, 2.8], [6.8, 1.8]],
                                closed=True, facecolor="#fee2e2", edgecolor=CRIMSON, lw=2.0, alpha=0.6)
    ax.add_patch(left_lung)
    ax.text(7.3, 4.0, "Left Lung\n(2 Lobes +\nCardiac Notch)", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Bronchiole Tree (branching within lungs)
    for bx, by in [(3.2, 5.2), (6.8, 5.2)]:
        sign = -1 if bx < 5 else 1
        ax.plot([bx, bx + sign*0.8], [by, by - 1.0], color=STEEL_BLUE, lw=2)
        ax.plot([bx, bx + sign*0.4], [by, by - 1.4], color=STEEL_BLUE, lw=2)
        ax.plot([bx + sign*0.8, bx + sign*1.2], [by - 1.0, by - 1.8], color=TEAL_ACCENT, lw=1.5)
        ax.plot([bx + sign*0.8, bx + sign*0.6], [by - 1.0, by - 2.0], color=TEAL_ACCENT, lw=1.5)

    # Alveoli clusters
    for ax_pt, ay_pt in [(2.0, 2.6), (2.4, 2.2), (7.8, 2.6), (8.2, 2.2)]:
        ax.add_patch(patches.Circle((ax_pt, ay_pt), 0.22, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.2))
    ax.text(2.2, 1.4, "Terminal\nAlveolar Sacs", ha="center", va="center", fontsize=7.5, color=DARK_GREY)
    ax.text(7.8, 1.4, "Terminal\nAlveolar Sacs", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Diaphragm (dome-shaped muscle)
    x_diaph = np.linspace(1.2, 8.8, 50)
    y_diaph = 1.6 + 0.5 * np.sin(np.pi * (x_diaph - 1.2) / 7.6)
    ax.plot(x_diaph, y_diaph, color=NAVY, lw=3, linestyle="-")
    ax.text(5.0, 1.9, "Diaphragm (Muscular Sheet)", ha="center", va="bottom", fontsize=8, fontweight="bold", color=NAVY)

    # Pleural Cavity note
    ax.annotate("Pleural Cavity &\nFluid (low friction)", xy=(1.6, 4.2), xytext=(0.2, 5.0),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2),
                fontsize=7.5, fontweight="bold", color=DARK_GREY)

    # Rib cage note
    ax.annotate("Intercostal Muscles\n& Rib Cage", xy=(8.4, 4.6), xytext=(8.6, 5.8),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.2),
                fontsize=7.5, fontweight="bold", color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_1.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.2: Histological Cross-Section (TS) of Trachea Wall
# -----------------------------------------------------------------------------
def generate_fig9_2():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.2: Histological Plan Diagram of Trachea Wall (Transverse Section)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Lumen area on top
    ax.add_patch(patches.Rectangle((0.5, 8.2), 9.0, 1.3, facecolor="#f8fafc", edgecolor="none"))
    ax.text(5.0, 8.8, "TRACHEAL LUMEN (Airway Space)", ha="center", va="center", fontsize=9.5, fontweight="bold", color=STEEL_BLUE)

    # Layer 1: Pseudostratified Ciliated Columnar Epithelium (7.0 to 8.2)
    ax.add_patch(patches.Rectangle((0.5, 7.2), 9.0, 1.0, facecolor="#fed7aa", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.2, 7.7, "Ciliated Epithelium", ha="left", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.text(8.8, 7.7, "Mucociliary escalator", ha="right", va="center", fontsize=7.5, color=DARK_GREY)

    # Draw individual cilia tufts on surface
    for x in np.linspace(0.8, 9.2, 45):
        ax.plot([x, x], [8.2, 8.4], color="#b45309", lw=1.5)
    # Goblet cells
    for gx in [2.5, 4.2, 6.0, 7.8]:
        ax.add_patch(patches.Polygon([[gx-0.15, 7.2], [gx-0.25, 8.2], [gx+0.25, 8.2], [gx+0.15, 7.2]],
                                     closed=True, facecolor="#bfdbfe", edgecolor=STEEL_BLUE, lw=1.2))
        ax.text(gx, 7.5, "GC", ha="center", va="center", fontsize=6.5, fontweight="bold", color=STEEL_BLUE)

    # Layer 2: Lamina Propria & Elastic Fibres (6.4 to 7.2)
    ax.add_patch(patches.Rectangle((0.5, 6.4), 9.0, 0.8, facecolor="#fef08a", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.2, 6.8, "Lamina Propria (Rich in Elastic Fibres & Capillaries)", ha="left", va="center", fontsize=8, fontweight="bold", color="#854d0e")

    # Layer 3: Submucosa with Seromucous Glands (5.0 to 6.4)
    ax.add_patch(patches.Rectangle((0.5, 5.0), 9.0, 1.4, facecolor="#e0e7ff", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.2, 5.7, "Submucosa (Connective Tissue & Seromucous Glands)", ha="left", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)
    # Gland acini
    for ax_pt in [4.5, 5.5, 6.8, 7.5]:
        ax.add_patch(patches.Circle((ax_pt, 5.7), 0.35, facecolor="#c7d2fe", edgecolor=STEEL_BLUE, lw=1.2))
        ax.text(ax_pt, 5.7, "Gland", ha="center", va="center", fontsize=6, color=STEEL_BLUE)

    # Layer 4: Hyaline Cartilage C-Ring (2.4 to 5.0)
    ax.add_patch(patches.Rectangle((0.5, 2.4), 9.0, 2.6, facecolor=CARTILAGE_COLOR, edgecolor=NAVY, lw=2.0))
    ax.text(1.2, 3.7, "Hyaline Cartilage C-Ring", ha="left", va="center", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.text(1.2, 3.2, "• Chondrocytes in lacunae embedded in basophilic collagenous matrix\n• Provides rigidity; prevents airway collapse during inspiration", ha="left", va="center", fontsize=7.5, color=DARK_GREY)
    # Chondrocytes
    for cx, cy in [(6.5, 4.2), (7.5, 3.8), (8.2, 4.3), (7.0, 3.0), (8.0, 2.8), (8.8, 3.4)]:
        ax.add_patch(patches.Ellipse((cx, cy), 0.35, 0.25, facecolor="white", edgecolor=NAVY, lw=1))
        ax.plot(cx, cy, "o", color=NAVY, markersize=3)

    # Layer 5: Perichondrium & Adventitia (1.0 to 2.4)
    ax.add_patch(patches.Rectangle((0.5, 1.0), 9.0, 1.4, facecolor="#f1f5f9", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.2, 1.7, "Adventitia & Perichondrium (Fibroelastic Outer Coat)", ha="left", va="center", fontsize=8, fontweight="bold", color=DARK_GREY)
    ax.text(1.2, 1.3, "• Binds trachea to surrounding tissues; contains systemic nerves & blood vessels", ha="left", va="center", fontsize=7, color=DARK_GREY)

    # Posterior Trachealis muscle callout
    trach_box = patches.FancyBboxPatch((6.0, 0.4), 3.5, 0.5, boxstyle="round,pad=0.1", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.2)
    ax.add_patch(trach_box)
    ax.text(7.75, 0.65, "Posterior: Trachealis Smooth Muscle bridges C-gap", ha="center", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_2.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.3: Ultrastructure of Ciliated & Goblet Cells (Mucociliary Escalator)
# -----------------------------------------------------------------------------
def generate_fig9_3():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.3: Ultrastructure of Ciliated Epithelium, Goblet Cells & Mucus Layer")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Mucus layer & trapped particles
    ax.add_patch(patches.Rectangle((0.5, 8.0), 9.0, 1.2, facecolor="#e0f2fe", edgecolor=STEEL_BLUE, lw=1.5, alpha=0.7))
    ax.text(1.0, 8.6, "Mucus Layer (Hydrated Mucin Glycoproteins)", ha="left", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax.text(9.0, 8.6, "Propelled upward -> Pharynx", ha="right", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Trapped bacteria and dust particles
    for px, py in [(3.0, 8.4), (3.8, 8.8), (5.5, 8.3), (7.2, 8.7), (8.0, 8.3)]:
        ax.add_patch(patches.Circle((px, py), 0.1, facecolor="#b91c1c", edgecolor=NAVY, lw=1))
    ax.text(3.5, 8.4, "Trapped\nPathogen", ha="left", va="center", fontsize=6.5, color=CRIMSON)

    # Cilia protruding into mucus
    for cx in np.linspace(0.8, 4.0, 20):
        # Wave-like slant to show coordinated metachronal wave
        ax.plot([cx, cx + 0.15], [7.2, 8.1], color=STEEL_BLUE, lw=2.2)
    for cx in np.linspace(6.0, 9.2, 18):
        ax.plot([cx, cx + 0.15], [7.2, 8.1], color=STEEL_BLUE, lw=2.2)
    ax.text(2.2, 7.6, "Cilia (9+2 Microtubule Axoneme; ~200/cell)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # Ciliated Epithelial Cell (Left)
    ax.add_patch(patches.Rectangle((0.8, 1.8), 3.5, 5.4, facecolor="#fff7ed", edgecolor=NAVY, lw=1.5))
    ax.text(2.55, 6.8, "Ciliated Columnar Cell", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)

    # Basal bodies (centriole-derived)
    for bx in np.linspace(1.0, 4.1, 15):
        ax.plot(bx, 7.15, "s", color=NAVY, markersize=3)
    ax.text(2.55, 6.3, "Basal Bodies (anchor cilia)", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Abundant Mitochondria (ATP for dynein ATPase arms)
    for mx, my in [(1.5, 5.4), (2.3, 5.6), (3.2, 5.3), (1.8, 4.6), (2.8, 4.8)]:
        ax.add_patch(patches.Ellipse((mx, my), 0.5, 0.25, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1))
        ax.plot(mx, my, "x", color=CRIMSON, markersize=3)
    ax.text(2.55, 4.1, "Abundant Mitochondria\n(ATP for Dynein Arms)", ha="center", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    # Nucleus (oval, basal)
    ax.add_patch(patches.Ellipse((2.55, 2.8), 1.6, 1.0, facecolor="#c7d2fe", edgecolor=NAVY, lw=1.5))
    ax.text(2.55, 2.8, "Nucleus", ha="center", va="center", fontsize=8, color=NAVY)

    # Goblet Cell (Middle, 4.5 to 6.0)
    goblet_pts = [[4.5, 1.8], [4.6, 4.0], [4.3, 7.2], [6.2, 7.2], [5.9, 4.0], [6.0, 1.8]]
    ax.add_patch(patches.Polygon(goblet_pts, closed=True, facecolor="#eff6ff", edgecolor=NAVY, lw=1.5))
    ax.text(5.25, 6.8, "Goblet Cell", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)

    # Mucinogen droplets / secretory vesicles
    for gx, gy in [(4.8, 6.2), (5.3, 6.4), (5.7, 6.1), (5.0, 5.4), (5.5, 5.6), (4.7, 4.8), (5.4, 4.9)]:
        ax.add_patch(patches.Circle((gx, gy), 0.22, facecolor="#bfdbfe", edgecolor=STEEL_BLUE, lw=1.2))
    ax.text(5.25, 4.3, "Mucin Granules\n(Exocytosis of\nMucin)", ha="center", va="center", fontsize=6.8, fontweight="bold", color=STEEL_BLUE)

    # Goblet cell nucleus & RER (basal)
    ax.add_patch(patches.Ellipse((5.25, 2.5), 1.0, 0.7, facecolor="#c7d2fe", edgecolor=NAVY, lw=1.2))
    ax.text(5.25, 2.5, "Nucleus\n& RER", ha="center", va="center", fontsize=6.5, color=NAVY)

    # Another Ciliated cell (Right, 6.2 to 9.2)
    ax.add_patch(patches.Rectangle((6.2, 1.8), 3.0, 5.4, facecolor="#fff7ed", edgecolor=NAVY, lw=1.5))
    ax.text(7.7, 6.8, "Ciliated Columnar Cell", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.add_patch(patches.Ellipse((7.7, 2.8), 1.6, 1.0, facecolor="#c7d2fe", edgecolor=NAVY, lw=1.5))
    ax.text(7.7, 2.8, "Nucleus", ha="center", va="center", fontsize=8, color=NAVY)

    # Basement Membrane & Lamina Propria (bottom)
    ax.add_patch(patches.Rectangle((0.5, 0.8), 9.0, 1.0, facecolor="#fef08a", edgecolor=BORDER_COLOR, lw=1.5))
    ax.plot([0.5, 9.5], [1.8, 1.8], color=NAVY, lw=2.5)
    ax.text(1.0, 1.3, "Basement Membrane (Collagen & Glycoproteins) & Lamina Propria", ha="left", va="center", fontsize=8, fontweight="bold", color="#854d0e")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_3.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.4: Comparative Histology: TS Bronchus vs TS Bronchiole
# -----------------------------------------------------------------------------
def generate_fig9_4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: TS Bronchus
    set_plot_style(ax1, "TS Bronchus (Conducting Airway)")
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.axis("off")

    # Outer wall
    ax1.add_patch(patches.Circle((0, 0), 4.2, facecolor="#f8fafc", edgecolor=BORDER_COLOR, lw=1.2))

    # Irregular Cartilage Plates (Key identifying feature!)
    cart_angles = [(20, 70), (100, 150), (180, 240), (270, 330)]
    for start, end in cart_angles:
        rad_start, rad_end = np.radians(start), np.radians(end)
        theta = np.linspace(rad_start, rad_end, 30)
        r_outer = 4.0
        r_inner = 3.2
        x_out, y_out = r_outer * np.cos(theta), r_outer * np.sin(theta)
        x_in, y_in = r_inner * np.cos(theta[::-1]), r_inner * np.sin(theta[::-1])
        verts = list(zip(np.concatenate([x_out, x_in]), np.concatenate([y_out, y_in])))
        poly = patches.Polygon(verts, closed=True, facecolor=CARTILAGE_COLOR, edgecolor=NAVY, lw=1.5)
        ax1.add_patch(poly)
    ax1.text(0, 3.6, "Irregular Cartilage Plates", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Smooth Muscle ring (continuous/interlacing)
    sm_ring = patches.Wedge((0, 0), 3.0, 0, 360, width=0.6, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.2)
    ax1.add_patch(sm_ring)
    ax1.text(0, -2.7, "Smooth Muscle & Elastic Fibres", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Mucosa with folded lumen
    ax1.add_patch(patches.Circle((0, 0), 2.2, facecolor="#fed7aa", edgecolor=BORDER_COLOR, lw=1))
    ax1.add_patch(patches.Circle((0, 0), 1.5, facecolor="white", edgecolor=NAVY, lw=1.5))
    ax1.text(0, 0, "Lumen\n(Ciliated +\nGoblet)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # Submucosa glands note
    ax1.text(0, -4.5, "• Cartilage: IRREGULAR PLATES\n• Epithelium: Ciliated pseudostratified\n• Goblet cells & glands PRESENT",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: TS Bronchiole
    set_plot_style(ax2, "TS Bronchiole (Terminal Airway)")
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    ax2.axis("off")

    # Outer adventitia
    ax2.add_patch(patches.Circle((0, 0), 3.8, facecolor="#f8fafc", edgecolor=BORDER_COLOR, lw=1.2))

    # NO CARTILAGE BANNER!
    no_cart_box = patches.FancyBboxPatch((-3.6, 3.2), 7.2, 0.7, boxstyle="round,pad=0.1", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax2.add_patch(no_cart_box)
    ax2.text(0, 3.55, "NO CARTILAGE PLATES PRESENT!", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Prominent Smooth Muscle Ring (controlling bronchoconstriction)
    sm_ring2 = patches.Wedge((0, 0), 3.0, 0, 360, width=0.9, facecolor="#fee2e2", edgecolor=CRIMSON, lw=2.0)
    ax2.add_patch(sm_ring2)
    ax2.text(0, 2.5, "Prominent Smooth Muscle", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Highly folded stellate mucosa
    # Star-like inner lumen
    t = np.linspace(0, 2*np.pi, 200)
    r_fold = 1.4 + 0.4 * np.sin(6 * t)
    x_fold = r_fold * np.cos(t)
    y_fold = r_fold * np.sin(t)
    ax2.fill(x_fold, y_fold, facecolor="white", edgecolor=NAVY, lw=1.8)
    ax2.text(0, 0, "Folded\nLumen", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Elastic fibre halo
    ax2.text(0, -2.5, "Elastic Fibres in Wall", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Key differences summary
    ax2.text(0, -4.5, "• Cartilage: COMPLETELY ABSENT\n• Smooth muscle: ABUNDANT (regulates airflow)\n• Goblet cells & glands: ABSENT in terminal",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_4.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.5: Microscopic Alveolar-Capillary Diffusion Barrier
# -----------------------------------------------------------------------------
def generate_fig9_5():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.5: Ultrastructure of the Alveolar-Capillary Gas Exchange Barrier")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Alveolar Air Space (Top, 5.5 to 10)
    ax.add_patch(patches.Rectangle((0.5, 5.5), 9.0, 4.0, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(5.0, 9.0, "ALVEOLAR AIR SPACE (Freshly Ventilated Air)\npO2 = 104 mmHg (13.7 kPa)  |  pCO2 = 40 mmHg (5.3 kPa)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)

    # Surfactant monolayer (green dashed)
    ax.plot([0.5, 9.5], [5.5, 5.5], color=GREEN_ACCENT, lw=2.5, linestyle="--")
    ax.text(1.0, 5.75, "Surfactant Film (Phospholipids reduce surface tension; prevents alveolar collapse)", ha="left", va="center", fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    # Type II Pneumocyte (Great alveolar cell, secretory)
    t2_pts = [[7.2, 5.5], [7.4, 7.0], [8.6, 7.0], [8.8, 5.5]]
    ax.add_patch(patches.Polygon(t2_pts, closed=True, facecolor="#dcfce7", edgecolor=GREEN_ACCENT, lw=1.5))
    ax.text(8.0, 6.25, "Type II Pneumocyte\n(Secretes Surfactant)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    # Alveolar Macrophage (Dust cell)
    ax.add_patch(patches.Ellipse((2.2, 7.0), 1.4, 0.8, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.2))
    ax.text(2.2, 7.0, "Alveolar Macrophage\n(Phagocytoses debris)", ha="center", va="center", fontsize=6.8, fontweight="bold", color=CRIMSON)

    # The 0.5 µm Barrier Layers (4.2 to 5.5)
    # Layer 1: Type I Pneumocyte (Squamous cell cytoplasm)
    ax.add_patch(patches.Rectangle((0.5, 4.9), 9.0, 0.6, facecolor="#fed7aa", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.0, 5.2, "1. Squamous Alveolar Epithelium (Type I Pneumocyte Cytoplasm)", ha="left", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Layer 2: Fused Basement Membrane
    ax.add_patch(patches.Rectangle((0.5, 4.6), 9.0, 0.3, facecolor="#cbd5e1", edgecolor="none"))
    ax.text(1.0, 4.75, "2. Fused Extracellular Basement Membrane (Collagen & Glycoproteins)", ha="left", va="center", fontsize=7, fontweight="bold", color=DARK_GREY)

    # Layer 3: Capillary Endothelium
    ax.add_patch(patches.Rectangle((0.5, 4.0), 9.0, 0.6, facecolor="#fee2e2", edgecolor=BORDER_COLOR, lw=1))
    ax.text(1.0, 4.3, "3. Capillary Endothelial Cell Cytoplasm", ha="left", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Bracket showing Total Diffusion Distance = 0.5 µm
    ax.annotate("", xy=(9.4, 5.5), xytext=(9.4, 4.0), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=2))
    ax.text(9.5, 4.75, "Total Diffusion\nBarrier: < 0.5 µm!", ha="left", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Pulmonary Capillary Lumen (0.8 to 4.0)
    ax.add_patch(patches.Rectangle((0.5, 0.8), 9.0, 3.2, facecolor="#fef2f2", edgecolor=RED_VESSEL, lw=1.5))
    ax.text(5.0, 3.4, "PULMONARY CAPILLARY LUMEN (Continuous Perfusion)\npO2 = 40 mmHg (deoxygenated) -> 104 mmHg (oxygenated)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=RED_VESSEL)

    # Red Blood Cells in single file (~7 µm diameter matching capillary lumen)
    for rx, label in [(2.2, "Deoxy-RBC"), (5.0, "Oxygenating RBC"), (7.8, "Oxy-RBC")]:
        color = BLUE_VESSEL if "Deoxy" in label else (PURPLE_ACCENT if "Oxygenating" in label else RED_VESSEL)
        ax.add_patch(patches.Ellipse((rx, 2.0), 1.8, 0.9, facecolor=color, edgecolor=NAVY, lw=1.5, alpha=0.8))
        ax.text(rx, 2.0, label, ha="center", va="center", fontsize=7, fontweight="bold", color="white")

    # Gas Diffusion Arrows
    # O2 moving into capillary
    ax.annotate("O2 Diffusion (steep gradient)", xy=(4.5, 2.7), xytext=(3.5, 6.5),
                arrowprops=dict(arrowstyle="->", color=RED_VESSEL, lw=3),
                fontsize=8.5, fontweight="bold", color=RED_VESSEL)
    # CO2 moving into alveolus
    ax.annotate("CO2 Diffusion", xy=(6.5, 6.5), xytext=(6.5, 2.7),
                arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=3),
                fontsize=8.5, fontweight="bold", color=BLUE_VESSEL)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_5.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.6: Alveolar Elastic Fibre Dynamics (Inhalation vs Recoil)
# -----------------------------------------------------------------------------
def generate_fig9_6():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Inhalation (Expansion)
    set_plot_style(ax1, "Inhalation: Active Expansion")
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.axis("off")

    # Alveolar sac expanded
    ax1.add_patch(patches.Circle((0, 0), 3.5, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=2.0))
    ax1.text(0, 0.5, "ALVEOLAR SAC\nEXPANDED", ha="center", va="center", fontsize=9, fontweight="bold", color=STEEL_BLUE)
    ax1.text(0, -0.6, "Volume Increases\nPressure Drops (-1 mmHg)\nAir flows IN", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Stretched elastic fibres (taut lines around circumference)
    for angle in np.linspace(0, 360, 16, endpoint=False):
        rad = np.radians(angle)
        x1, y1 = 3.5 * np.cos(rad), 3.5 * np.sin(rad)
        x2, y2 = 4.3 * np.cos(rad), 4.3 * np.sin(rad)
        ax1.plot([x1, x2], [y1, y2], color=CRIMSON, lw=2.5)
        # Outward expansion arrows
        ax1.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5))
    ax1.text(0, 4.4, "Elastic Fibres STRETCHED under tension", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Mechanics note
    ax1.text(0, -4.5, "• Diaphragm contracts & flattens\n• External intercostals contract\n• Requires metabolic energy (ATP)",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: Exhalation (Passive Elastic Recoil)
    set_plot_style(ax2, "Exhalation: Passive Elastic Recoil")
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    ax2.axis("off")

    # Alveolar sac recoiled
    ax2.add_patch(patches.Circle((0, 0), 2.2, facecolor="#fef2f2", edgecolor=CRIMSON, lw=2.0))
    ax2.text(0, 0.4, "ALVEOLAR SAC\nRECOILED", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax2.text(0, -0.5, "Volume Decreases\nPressure Rises (+1 mmHg)\nAir forced OUT", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Inward recoil arrows
    for angle in np.linspace(0, 360, 16, endpoint=False):
        rad = np.radians(angle)
        x1, y1 = 3.2 * np.cos(rad), 3.2 * np.sin(rad)
        x2, y2 = 2.3 * np.cos(rad), 2.3 * np.sin(rad)
        ax2.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax2.text(0, 4.4, "Elastic Recoil Forces Air Out Passively", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Clinical pathology note
    ax2.text(0, -4.5, "• PASSIVE process at rest (no ATP required)\n• In emphysema, elastase destroys fibres\n• Results in air-trapping & barrel chest",
             ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_6.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.7: Spirometry Trace: Lung Volumes & Capacities
# -----------------------------------------------------------------------------
def generate_fig9_7():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 9.7: Spirometry Trace — Lung Volumes and Capacities")

    time = np.linspace(0, 24, 600)
    # Baseline 2.5L to 3.0L for Tidal Volume (0.5L)
    # First 3 normal breaths
    vol = np.zeros_like(time)
    for i, t in enumerate(time):
        if t < 8:
            vol[i] = 2.6 + 0.25 * np.sin(2 * np.pi * t / 2.5)
        elif t < 12:  # Maximal inspiration (to 5.5L)
            phase = (t - 8) / 4.0
            vol[i] = 2.6 + 3.0 * np.sin(np.pi * phase)
        elif t < 16:  # Maximal expiration (down to 1.2L)
            phase = (t - 12) / 4.0
            vol[i] = 2.6 - 1.4 * np.sin(np.pi * phase)
        else:  # Return to tidal breathing
            vol[i] = 2.6 + 0.25 * np.sin(2 * np.pi * (t - 16) / 2.5)

    ax.plot(time, vol, color=STEEL_BLUE, lw=2.2)
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 6.5)
    ax.set_xlabel("Time / s", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylabel("Lung Volume / dm³", fontsize=9, fontweight="bold", color=NAVY)

    # Shaded Volume Zones
    # Residual Volume (0 to 1.2 dm3)
    ax.axhspan(0, 1.2, facecolor="#e2e8f0", alpha=0.6)
    ax.text(20, 0.6, "Residual Volume (RV = 1.2 dm³)\n(Cannot be exhaled)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)

    # Expiratory Reserve Volume (1.2 to 2.4 dm3)
    ax.axhspan(1.2, 2.35, facecolor="#fee2e2", alpha=0.5)
    ax.text(20, 1.75, "Expiratory Reserve (ERV = 1.1 dm³)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Tidal Volume (2.35 to 2.85 dm3)
    ax.axhspan(2.35, 2.85, facecolor="#dbeafe", alpha=0.6)
    ax.text(4, 3.2, "Tidal Volume (VT = 0.5 dm³)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)

    # Inspiratory Reserve Volume (2.85 to 5.6 dm3)
    ax.axhspan(2.85, 5.6, facecolor="#dcfce7", alpha=0.5)
    ax.text(20, 4.2, "Inspiratory Reserve (IRV = 2.7 dm³)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    # Brackets for Capacities
    # Vital Capacity (1.2 to 5.6 dm3)
    ax.annotate("", xy=(10.5, 5.6), xytext=(10.5, 1.2), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=2))
    ax.text(10.8, 3.4, "Vital Capacity (VC = 4.4 dm³)\nVC = IRV + VT + ERV", ha="left", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Total Lung Capacity (0 to 5.6 dm3)
    ax.annotate("", xy=(1.5, 5.6), xytext=(1.5, 0.0), arrowprops=dict(arrowstyle="<->", color=CRIMSON, lw=2))
    ax.text(1.8, 4.8, "Total Lung Capacity\n(TLC = 5.6 dm³)\nTLC = VC + RV", ha="left", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_7.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.8: Fick's Law of Diffusion & Alveolar Partial Pressures
# -----------------------------------------------------------------------------
def generate_fig9_8():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.8: Fick's Law of Diffusion Applied to Gas Exchange")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Formula Header Box
    fick_box = patches.FancyBboxPatch((1.0, 7.8), 8.0, 1.6, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, lw=2.0)
    ax.add_patch(fick_box)
    ax.text(5.0, 8.9, r"$\mathbf{Rate\ of\ Diffusion \propto \frac{A \times \Delta P}{x}}$", ha="center", va="center", fontsize=14, color=NAVY)
    ax.text(5.0, 8.2, "A = Surface Area (~100 m²)  |  ΔP = Partial Pressure Gradient  |  x = Diffusion Distance (< 0.5 µm)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)

    # 3 Factor Cards
    # Card 1: Surface Area (A)
    c1 = patches.FancyBboxPatch((0.5, 3.8), 2.8, 3.6, boxstyle="round,pad=0.2", facecolor="#dbeafe", edgecolor=STEEL_BLUE, lw=1.5)
    ax.add_patch(c1)
    ax.text(1.9, 7.0, "1. SURFACE AREA (A)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax.text(1.9, 5.4, "• 500-700 million alveoli\n• Total area ~100 m²\n(size of tennis court)\n• Extensive network of\ninterlocking capillaries\n• Alveoli spherical shape\nmaximises SA:V ratio",
            ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Card 2: Partial Pressure Gradient (ΔP)
    c2 = patches.FancyBboxPatch((3.6, 3.8), 2.8, 3.6, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(c2)
    ax.text(5.0, 7.0, "2. GRADIENT (ΔP)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax.text(5.0, 5.4, "• Oxygen:\n  Alveoli: 104 mmHg\n  Capillary: 40 mmHg\n  ΔP = 64 mmHg\n• Carbon Dioxide:\n  Capillary: 45 mmHg\n  Alveoli: 40 mmHg\n  ΔP = 5 mmHg\n(CO2 is 20x more soluble)",
            ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Card 3: Diffusion Distance (x)
    c3 = patches.FancyBboxPatch((6.7, 3.8), 2.8, 3.6, boxstyle="round,pad=0.2", facecolor="#dcfce7", edgecolor=GREEN_ACCENT, lw=1.5)
    ax.add_patch(c3)
    ax.text(8.1, 7.0, "3. DISTANCE (x)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=GREEN_ACCENT)
    ax.text(8.1, 5.4, "• Ultra-thin barrier:\n  Type I pneumocyte\n  Basement membrane\n  Capillary endothelium\n• Total x < 0.5 µm\n• RBCs squeeze single-\nfile (lumen 7 µm)\nminimising plasma gap",
            ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Bottom Maintaining Gradient Mechanism
    bot_box = patches.FancyBboxPatch((0.5, 0.6), 9.0, 2.6, boxstyle="round,pad=0.2", facecolor="#fff7ed", edgecolor="#d97706", lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 2.7, "HOW THE STEEP CONCENTRATION GRADIENT IS ACTIVELY MAINTAINED", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#d97706")
    ax.text(2.8, 1.6, "A. CONTINUOUS VENTILATION\n• Fresh air brought into alveoli (high O2, low CO2)\n• Stale air exhaled (removes accumulated CO2)", ha="center", va="center", fontsize=7.5, color=DARK_GREY)
    ax.text(7.2, 1.6, "B. CONTINUOUS PERFUSION\n• Pulmonary circulation brings deoxygenated blood\n• Rapidly carries oxygenated blood away to heart", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_8.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.9: Histopathology of Chronic Bronchitis
# -----------------------------------------------------------------------------
def generate_fig9_9():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Normal Bronchial Wall
    set_plot_style(ax1, "Normal Healthy Bronchial Mucosa")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    # Lumen
    ax1.text(5.0, 9.2, "Lumen (Clear Airway)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)

    # Healthy Cilia
    for cx in np.linspace(1.0, 9.0, 30):
        ax1.plot([cx, cx], [7.6, 8.4], color=STEEL_BLUE, lw=1.8)
    ax1.text(5.0, 8.6, "Dense, active cilia (~200/cell)", ha="center", va="center", fontsize=7, color=STEEL_BLUE)

    # Normal Epithelium (few goblet cells)
    ax1.add_patch(patches.Rectangle((0.5, 4.5), 9.0, 3.1, facecolor="#eff6ff", edgecolor=NAVY, lw=1.2))
    ax1.text(5.0, 6.0, "Pseudostratified Ciliated Columnar Epithelium\n(Goblet cells: ~1 per 5 ciliated cells)", ha="center", va="center", fontsize=7.5, color=NAVY)

    # Normal Submucosa & Seromucous Glands
    ax1.add_patch(patches.Rectangle((0.5, 1.5), 9.0, 3.0, facecolor="#f8fafc", edgecolor=BORDER_COLOR, lw=1.0))
    ax1.text(5.0, 3.0, "Submucosa\nNormal Reid Index < 0.4 (glands occupy < 40% wall)", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: Chronic Bronchitis
    set_plot_style(ax2, "Chronic Bronchitis (Smoker's Airway)")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    # Lumen plugged with thick mucus & bacteria
    ax2.add_patch(patches.Rectangle((0.5, 7.5), 9.0, 2.0, facecolor="#fef08a", edgecolor="#ca8a04", lw=1.5, alpha=0.8))
    ax2.text(5.0, 8.8, "MUCUS PLUG & BACTERIAL INFECTION", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#854d0e")
    ax2.text(5.0, 8.0, "Stagnant, viscous mucus culture medium for H. influenzae", ha="center", va="center", fontsize=7, color="#854d0e")

    # Destroyed & Paralysed Cilia (Ciliostasis)
    for cx in np.linspace(1.0, 9.0, 10):
        ax2.plot([cx, cx+0.1], [7.2, 7.4], color="#94a3b8", lw=1.0, linestyle=":")
    ax2.text(5.0, 7.3, "Cilia damaged, paralysed, or destroyed by tar!", ha="center", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    # Hypertrophied Epithelium & Hyperplasia of Goblet Cells
    ax2.add_patch(patches.Rectangle((0.5, 4.0), 9.0, 3.2, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
    ax2.text(5.0, 5.6, "GOBLET CELL HYPERPLASIA\nExcessive mucin production; squamous metaplasia", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    # Submucosa with enlarged mucous glands & chronic inflammatory infiltrate
    ax2.add_patch(patches.Rectangle((0.5, 1.0), 9.0, 3.0, facecolor="#fecaca", edgecolor=CRIMSON, lw=1.2))
    ax2.text(5.0, 2.5, "Submucosa: Hypertrophied Glands (Reid Index > 0.6)\nInfiltration by Neutrophils & Macrophages\nChronic productive cough for >= 3 months / 2 yrs", ha="center", va="center", fontsize=7.2, fontweight="bold", color=NAVY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_9.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.10: Pathogenesis of Emphysema
# -----------------------------------------------------------------------------
def generate_fig9_10():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 9.10: Molecular & Cellular Pathogenesis of Emphysema")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Step 1: Cigarette Smoke Irritation (Top Left)
    s1 = patches.FancyBboxPatch((0.5, 7.2), 4.2, 2.2, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(s1)
    ax.text(2.6, 8.8, "1. CIGARETTE SMOKE IRRITATION", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax.text(2.6, 7.9, "• Particulates settle in terminal bronchioles\n• Alveolar macrophages phagocytose smoke\n• Release chemotactic factors (IL-8, LTB4)\n• Attract massive influx of NEUTROPHILS", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Step 2: Elastase-Antiprotease Imbalance (Top Right)
    s2 = patches.FancyBboxPatch((5.3, 7.2), 4.2, 2.2, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(s2)
    ax.text(7.4, 8.8, "2. PROTEASE-ANTIPROTEASE IMBALANCE", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax.text(7.4, 7.9, "• Neutrophils secrete ELASTASE (protease)\n• Smoke oxidants INACTIVATE α1-antitrypsin\n  (the natural protective elastase inhibitor)\n• Unchecked elastase digests ELASTIN fibres!", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Step 3: Breakdown of Alveolar Septa (Bottom Left)
    s3 = patches.FancyBboxPatch((0.5, 3.8), 4.2, 2.6, boxstyle="round,pad=0.2", facecolor="#ffedd5", edgecolor="#ea580c", lw=1.5)
    ax.add_patch(s3)
    ax.text(2.6, 5.9, "3. DESTRUCTION OF ALVEOLAR WALLS", ha="center", va="center", fontsize=8, fontweight="bold", color="#ea580c")
    ax.text(2.6, 4.8, "• Alveolar septa lyse and coalesce\n• Forms large, irregular air sacs (bullae)\n• Massive loss of gas exchange surface area\n• Destruction of capillary beds -> hypoxia", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Step 4: Loss of Elastic Recoil & Airway Collapse (Bottom Right)
    s4 = patches.FancyBboxPatch((5.3, 3.8), 4.2, 2.6, boxstyle="round,pad=0.2", facecolor="#ffedd5", edgecolor="#ea580c", lw=1.5)
    ax.add_patch(s4)
    ax.text(7.4, 5.9, "4. LOSS OF ELASTIC RECOIL", ha="center", va="center", fontsize=8, fontweight="bold", color="#ea580c")
    ax.text(7.4, 4.8, "• Lungs cannot recoil passively during exhalation\n• Bronchioles lack cartilage and COLLAPSE\n• Air becomes trapped in lungs (air trapping)\n• Extreme breathlessness (dyspnea), barrel chest", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Arrows connecting steps
    ax.annotate("", xy=(5.3, 8.3), xytext=(4.7, 8.3), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))
    ax.annotate("", xy=(2.6, 6.4), xytext=(2.6, 7.2), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))
    ax.annotate("", xy=(5.3, 5.1), xytext=(4.7, 5.1), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))

    # Bottom Comparison: Normal Alveoli vs Emphysematous Bullae
    bot_box = patches.FancyBboxPatch((0.5, 0.6), 9.0, 2.6, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 2.8, "HISTOLOGICAL COMPARISON", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)

    # Left: Many small alveoli
    for ax_pt, ay_pt in [(2.0, 1.7), (2.6, 1.7), (2.3, 2.1), (2.9, 2.1), (1.7, 2.1), (2.0, 1.2), (2.6, 1.2)]:
        ax.add_patch(patches.Circle((ax_pt, ay_pt), 0.25, facecolor="#dbeafe", edgecolor=STEEL_BLUE, lw=1.2))
    ax.text(2.3, 0.8, "Normal: Millions of tiny alveoli\nHigh surface area (~100 m²)", ha="center", va="center", fontsize=7, fontweight="bold", color=STEEL_BLUE)

    # Right: Large confluent air space
    ax.add_patch(patches.Ellipse((7.4, 1.7), 2.2, 1.2, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.8))
    ax.text(7.4, 1.7, "EMPHYSEMATOUS\nBULLA", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax.text(7.4, 0.8, "Diseased: Coalesced large space\nSeverely reduced surface area", ha="center", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_10.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.11: Tobacco Smoke Triad: Nicotine, CO, and Tar
# -----------------------------------------------------------------------------
def generate_fig9_11():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 5), dpi=300)

    # Ax1: Nicotine
    set_plot_style(ax1, "1. NICOTINE\n(Addictive Alkaloid)")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")
    c1 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5)
    ax1.add_patch(c1)
    ax1.text(5.0, 8.5, "MODE OF ACTION", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax1.text(5.0, 5.0, "• Mimics acetylcholine\nat nicotinic receptors\n• Highly addictive\n\n• Stimulates adrenal medulla\nto secrete ADRENALINE\n\n• Systemic Effects:\n  - Arteriolar vasoconstriction\n  - Elevated blood pressure\n  - Increased heart rate\n  - Increased platelet stickiness\n    -> thrombosis risk\n  - Atheroma formation",
             ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Ax2: Carbon Monoxide (CO)
    set_plot_style(ax2, "2. CARBON MONOXIDE\n(Toxic Gas)")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")
    c2 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5)
    ax2.add_patch(c2)
    ax2.text(5.0, 8.5, "MODE OF ACTION", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax2.text(5.0, 5.0, "• Diffuses across alveoli\ninto erythrocytes\n\n• Binds IRREVERSIBLY to\nhaemoglobin with 250x\nhigher affinity than O2\n\n• Forms stable\nCARBOXYHAEMOGLOBIN\n(HbCO)\n\n• Reduces oxygen-carrying\ncapacity of blood\n\n• Damages arterial endothelium\naccelerating plaque deposit\n\n• Crosses placenta -> fetal hypoxia",
             ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Ax3: Tar
    set_plot_style(ax3, "3. TAR\n(Carcinogenic Particulate)")
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.axis("off")
    c3 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fefce8", edgecolor="#ca8a04", lw=1.5)
    ax3.add_patch(c3)
    ax3.text(5.0, 8.5, "MODE OF ACTION", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#854d0e")
    ax3.text(5.0, 5.0, "• Sticky brown residue\nsettles in lining of airways\n\n• Respiratory Effects:\n  - Paralyses & destroys cilia\n  - Hypertrophy of goblet cells\n  - Excessive mucus pooling\n    -> Chronic Bronchitis\n\n• Carcinogenic Effects:\n  - Contains benzo[a]pyrene\n  - Mutates TP53 gene\n  - Uncontrolled mitosis\n    -> Lung Cancer",
             ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_11.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.12: Multi-Step Bronchogenic Carcinoma Progression
# -----------------------------------------------------------------------------
def generate_fig9_12():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 9.12: Multi-Step Pathogenesis of Bronchogenic Carcinoma (Lung Cancer)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    stages = [
        ("1. Normal Epithelium", "Ciliated columnar cells\nwith active cilia and\nnormal goblet cells.", "#eff6ff", STEEL_BLUE, 0.5),
        ("2. Squamous Metaplasia", "Cilia lost; columnars\nreplaced by stratified\nsquamous cells (hardier).", "#fff7ed", "#ea580c", 2.8),
        ("3. Dysplasia & Atypia", "Cellular atypia; high\nnuclear-to-cytoplasmic\nratio; mitotic figures.", "#fef2f2", CRIMSON, 5.1),
        ("4. Invasive Carcinoma", "Tumor breaches basement\nmembrane; invades tissues,\nblood & lymph nodes.", "#fee2e2", "#7f1d1d", 7.4)
    ]

    for title, desc, bg, edge, x_pos in stages:
        box = patches.FancyBboxPatch((x_pos, 4.0), 2.1, 4.8, boxstyle="round,pad=0.15", facecolor=bg, edgecolor=edge, lw=1.5)
        ax.add_patch(box)
        ax.text(x_pos + 1.05, 8.4, title, ha="center", va="center", fontsize=8, fontweight="bold", color=edge)
        ax.text(x_pos + 1.05, 5.8, desc, ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Connecting arrows
    for ax_pt in [2.65, 4.95, 7.25]:
        ax.annotate("", xy=(ax_pt + 0.15, 6.4), xytext=(ax_pt - 0.05, 6.4), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # Bottom Genetic & Molecular Mechanisms
    bot_box = patches.FancyBboxPatch((0.5, 0.5), 9.0, 3.0, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 3.0, "MOLECULAR DRIVERS OF TOBACCO-INDUCED CARCINOGENESIS", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.text(2.8, 1.8, "• Benzo[a]pyrene in tar binds DNA forming adducts\n• G -> T transversion mutations in TP53 gene\n• Loss of p53 tumor suppressor function\n  (no cell cycle arrest at G1/S, no apoptosis)", ha="center", va="center", fontsize=7.2, color=DARK_GREY)
    ax.text(7.2, 1.8, "• Activating mutations in KRAS oncogene\n• Secretion of VEGF -> tumour angiogenesis\n• Penetration of pulmonary venules & lymphatic vessels\n• Secondary metastases in brain, liver, bone", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_12.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.13: Mechanics of Ventilation: Thoracic Pressure & Volume
# -----------------------------------------------------------------------------
def generate_fig9_13():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Inspiration
    set_plot_style(ax1, "Inspiration (Active Process)")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    c1 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5)
    ax1.add_patch(c1)
    ax1.text(5.0, 8.8, "INSPIRATION DYNAMICS", ha="center", va="center", fontsize=9, fontweight="bold", color=STEEL_BLUE)

    ax1.text(5.0, 5.2, "1. MUSCLE ACTIONS:\n• External intercostal muscles CONTRACT\n• Internal intercostals relax\n• Ribs move UP and OUT\n• Diaphragm CONTRACTS and flattens\n\n2. VOLUME & PRESSURE CHANGES:\n• Thoracic cavity volume INCREASES\n• Intrapleural pressure drops (-8 mmHg)\n• Intrapulmonary pressure falls below atmospheric\n  (down to -1 mmHg / -0.13 kPa)\n\n3. AIRFLOW:\n• Air rushes down pressure gradient into lungs\n• Alveoli expand, stretching elastic fibres",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: Expiration
    set_plot_style(ax2, "Expiration at Rest (Passive Process)")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    c2 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5)
    ax2.add_patch(c2)
    ax2.text(5.0, 8.8, "EXPIRATION DYNAMICS", ha="center", va="center", fontsize=9, fontweight="bold", color=CRIMSON)

    ax2.text(5.0, 5.2, "1. MUSCLE ACTIONS:\n• External intercostal muscles RELAX\n• Ribs fall DOWN and IN under gravity\n• Diaphragm RELAXES, doming upwards\n  into thoracic cavity\n\n2. VOLUME & PRESSURE CHANGES:\n• Thoracic cavity volume DECREASES\n• Passive ELASTIC RECOIL of alveolar fibres\n• Intrapulmonary pressure rises above atmospheric\n  (up to +1 mmHg / +0.13 kPa)\n\n3. AIRFLOW:\n• Air forced out of lungs down pressure gradient\n• Forced expiration (exercise): internal intercostals\n  & abdominal muscles contract actively",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_13.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 9.14: Tissue Distribution Matrix Across Respiratory Tract
# -----------------------------------------------------------------------------
def generate_fig9_14():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 9.14: Distribution of Tissues Across the Human Gas Exchange System")
    ax.axis("off")

    # Table data
    columns = ["Region", "Cartilage", "Ciliated Epithelium", "Goblet Cells", "Smooth Muscle", "Elastic Fibres"]
    rows = [
        ["Trachea", "C-shaped Rings", "Abundant (Pseudostratified)", "Abundant", "Trachealis (Dorsal)", "Abundant in Lamina Propria"],
        ["Bronchus", "Irregular Plates", "Abundant (Columnar)", "Present", "Interlacing Bands", "Abundant"],
        ["Terminal Bronchiole", "ABSENT", "Ciliated Cuboidal", "Very Few / Absent", "Complete Circular Ring", "Abundant"],
        ["Respiratory Bronchiole", "ABSENT", "Cuboidal (Few Cilia)", "ABSENT", "Scattered Bundles", "Abundant"],
        ["Alveolus", "ABSENT", "ABSENT (Squamous Type I)", "ABSENT", "ABSENT", "Dense Network (Recoil)"]
    ]

    cell_colors = [
        ["#dbeafe", "#e0e7ff", "#eff6ff", "#eff6ff", "#fee2e2", "#fef9c3"],
        ["#dbeafe", "#e0e7ff", "#eff6ff", "#eff6ff", "#fee2e2", "#fef9c3"],
        ["#dbeafe", "#fee2e2", "#eff6ff", "#fee2e2", "#fca5a5", "#fef9c3"],
        ["#dbeafe", "#fee2e2", "#f1f5f9", "#fee2e2", "#fee2e2", "#fef9c3"],
        ["#dbeafe", "#fee2e2", "#fee2e2", "#fee2e2", "#fee2e2", "#fef08a"]
    ]

    table = ax.table(cellText=rows, colLabels=columns, cellColours=cell_colors,
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1.0, 2.0)

    # Style header row
    for col in range(len(columns)):
        cell = table[0, col]
        cell.set_facecolor(NAVY)
        cell.set_text_props(color="white", fontweight="bold", fontsize=8)

    # Highlight notes at bottom
    note_box = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.16, boxstyle="round,pad=0.05", facecolor="#fff1f2", edgecolor=CRIMSON, lw=1.5, transform=ax.transAxes)
    ax.add_patch(note_box)
    ax.text(0.5, 0.13, "CRITICAL CAMBRIDGE EXAMINER MANDATE: Cartilage is NEVER present in bronchioles!",
            ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON, transform=ax.transAxes)
    ax.text(0.5, 0.08, "Elastic fibres are present throughout the entire respiratory tract from trachea to alveoli.",
            ha="center", va="center", fontsize=7.5, color=DARK_GREY, transform=ax.transAxes)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig9_14.png"), dpi=300)
    plt.close(fig)

def main():
    print("Generating 14 vector diagrams for Topic 9: Gas Exchange...")
    generate_fig9_1()
    generate_fig9_2()
    generate_fig9_3()
    generate_fig9_4()
    generate_fig9_5()
    generate_fig9_6()
    generate_fig9_7()
    generate_fig9_8()
    generate_fig9_9()
    generate_fig9_10()
    generate_fig9_11()
    generate_fig9_12()
    generate_fig9_13()
    generate_fig9_14()
    print("All 14 Topic 9 figures generated successfully in 300 DPI!")

if __name__ == "__main__":
    main()
