"""
Vector Diagram Generator for Topic 8: Transport in Mammals
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Generates 14 high-resolution 300 DPI scientific figures:
- fig8_1: Plan of closed double circulation (pulmonary vs systemic circuits)
- fig8_2: Histological cross-section of artery, vein, and capillary
- fig8_3: Capillary bed ultrafiltration & tissue fluid dynamics (Starling forces)
- fig8_4: Formed elements of mammalian blood (erythrocyte, neutrophil, monocyte, lymphocyte)
- fig8_5: Internal coronal anatomy of mammalian heart (chambers, valves, wall thickness)
- fig8_6: Wiggers diagram of the cardiac cycle (pressures, volume, valve states)
- fig8_7: Electrical conduction system of the heart (SAN, AVN, Purkyne tissue)
- fig8_8: Oxygen dissociation curve of adult haemoglobin (cooperativity & physiological saturation)
- fig8_9: The Bohr effect (rightward shift under elevated pCO2 and lower pH)
- fig8_10: CO2 transport in erythrocytes & the chloride shift (carbonic anhydrase, HHb, HCO3-/Cl-)
- fig8_11: Comparative dissociation curves: Adult Hb vs Fetal Hb vs Myoglobin
- fig8_12: Arteriole cross-section & vasomotor regulation (vasoconstriction vs vasodilation)
- fig8_13: Blind-ended lymphatic capillary & interstitial drainage
- fig8_14: Pressure changes across the mammalian systemic circulatory vascular tree
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
PURPLE_CAPILLARY = "#7c3aed"
YELLOW_ACCENT = "#d97706"
GREEN_LYMPH = "#059669"

def set_plot_style(ax, title=""):
    ax.set_facecolor("white")
    if title:
        ax.set_title(title, fontsize=11, fontweight="bold", color=NAVY, pad=12, family="sans-serif")
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(1.0)

# -----------------------------------------------------------------------------
# Fig 8.1: Closed Double Circulation Plan
# -----------------------------------------------------------------------------
def generate_fig8_1():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 8.1: Schematic Plan of Closed Double Circulation in Mammals")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Lungs Capillary Bed (top)
    lungs_box = patches.FancyBboxPatch((3.5, 8.2), 3.0, 1.2, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=RED_VESSEL, linewidth=1.5)
    ax.add_patch(lungs_box)
    ax.text(5.0, 8.8, "Pulmonary Capillaries (Lungs)\nGas Exchange: O2 uptake, CO2 loss", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)

    # Body Tissues Capillary Bed (bottom)
    body_box = patches.FancyBboxPatch((3.0, 0.6), 4.0, 1.3, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=RED_VESSEL, linewidth=1.5)
    ax.add_patch(body_box)
    ax.text(5.0, 1.25, "Systemic Capillaries (Body Tissues)\nMetabolic Exchange: O2 release, CO2 uptake", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)

    # Heart (center)
    heart_box = patches.FancyBboxPatch((3.2, 3.6), 3.6, 3.0, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, linewidth=2.0)
    ax.add_patch(heart_box)
    ax.text(5.0, 6.2, "MAMMALIAN HEART", ha="center", va="center", fontsize=9.5, fontweight="bold", color=NAVY)

    # 4 Chambers
    # Right Atrium (blue)
    ax.add_patch(patches.Rectangle((3.5, 4.8), 1.3, 1.0, facecolor="#dbeafe", edgecolor=BLUE_VESSEL, lw=1.2))
    ax.text(4.15, 5.3, "Right\nAtrium", ha="center", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)
    # Left Atrium (red)
    ax.add_patch(patches.Rectangle((5.2, 4.8), 1.3, 1.0, facecolor="#fee2e2", edgecolor=RED_VESSEL, lw=1.2))
    ax.text(5.85, 5.3, "Left\nAtrium", ha="center", va="center", fontsize=7.5, fontweight="bold", color=RED_VESSEL)
    # Right Ventricle (blue)
    ax.add_patch(patches.Rectangle((3.5, 3.8), 1.3, 0.9, facecolor="#bfdbfe", edgecolor=BLUE_VESSEL, lw=1.2))
    ax.text(4.15, 4.25, "Right\nVentricle", ha="center", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)
    # Left Ventricle (red)
    ax.add_patch(patches.Rectangle((5.2, 3.8), 1.3, 0.9, facecolor="#fecaca", edgecolor=RED_VESSEL, lw=1.2))
    ax.text(5.85, 4.25, "Left\nVentricle", ha="center", va="center", fontsize=7.5, fontweight="bold", color=RED_VESSEL)

    # Septum
    ax.plot([4.95, 4.95], [3.8, 5.8], color=NAVY, lw=2.5, linestyle="--")
    ax.text(5.0, 3.65, "Septum", ha="center", va="top", fontsize=7, color=DARK_GREY)

    # Vessels & Arrows
    # 1. Pulmonary Artery: RV -> Lungs (Deoxygenated, Blue)
    ax.annotate("", xy=(4.2, 8.2), xytext=(4.0, 4.7), arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=2.5, connectionstyle="arc3,rad=-0.25"))
    ax.text(3.1, 6.8, "Pulmonary Artery\n(Low O2, High CO2)", ha="right", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)

    # 2. Pulmonary Vein: Lungs -> LA (Oxygenated, Red)
    ax.annotate("", xy=(5.8, 5.8), xytext=(5.8, 8.2), arrowprops=dict(arrowstyle="->", color=RED_VESSEL, lw=2.5, connectionstyle="arc3,rad=-0.25"))
    ax.text(6.8, 7.2, "Pulmonary Vein\n(High O2, Low CO2)", ha="left", va="center", fontsize=7.5, fontweight="bold", color=RED_VESSEL)

    # 3. Aorta: LV -> Body Tissues (High Pressure, Oxygenated, Red)
    ax.annotate("", xy=(5.8, 1.9), xytext=(5.8, 3.8), arrowprops=dict(arrowstyle="->", color=RED_VESSEL, lw=3.0, connectionstyle="arc3,rad=0.25"))
    ax.text(7.2, 2.8, "Aorta & Systemic Arteries\n(High pressure, ~120 mmHg)", ha="left", va="center", fontsize=7.5, fontweight="bold", color=RED_VESSEL)

    # 4. Vena Cava: Body Tissues -> RA (Deoxygenated, Blue)
    ax.annotate("", xy=(4.0, 3.8), xytext=(4.0, 1.9), arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=2.5, connectionstyle="arc3,rad=0.25"))
    ax.text(2.6, 2.7, "Vena Cava & Veins\n(Low pressure, ~5 mmHg)", ha="right", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)

    # Circuit labels
    ax.text(1.2, 8.5, "PULMONARY\nCIRCUIT\n(Low pressure ~25 mmHg)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE, bbox=dict(boxstyle="square,pad=0.3", fc="#eff6ff", ec=STEEL_BLUE))
    ax.text(1.2, 1.2, "SYSTEMIC\nCIRCUIT\n(High pressure ~120 mmHg)", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON, bbox=dict(boxstyle="square,pad=0.3", fc="#fff1f2", ec=CRIMSON))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_1_circulatory_system_plan.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.2: Cross-Sections of Artery, Vein, and Capillary
# -----------------------------------------------------------------------------
def generate_fig8_2():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4.2), dpi=300)
    fig.suptitle("Fig. 8.2: Histological Cross-Sections of Artery, Vein, and Capillary (TS)", fontsize=11, fontweight="bold", color=NAVY, y=0.98)

    # 1. Artery
    set_plot_style(ax1, "Muscular / Elastic Artery")
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.axis("off")

    # Tunica externa (collagen)
    c_ext = plt.Circle((0, 0), 4.2, color="#fed7aa", ec="#ea580c", lw=1.5, label="Tunica externa (collagen)")
    ax1.add_patch(c_ext)
    # Tunica media (thick smooth muscle & elastic fibres)
    c_med = plt.Circle((0, 0), 3.5, color="#fca5a5", ec="#dc2626", lw=1.8, label="Tunica media (thick muscle/elastic)")
    ax1.add_patch(c_med)
    # Tunica intima (endothelium + internal elastic lamina)
    c_int = plt.Circle((0, 0), 1.8, color="#fef08a", ec="#ca8a04", lw=1.2, label="Tunica intima")
    ax1.add_patch(c_int)
    # Narrow regular lumen
    c_lum = plt.Circle((0, 0), 1.4, color="white", ec=NAVY, lw=1.2)
    ax1.add_patch(c_lum)
    ax1.text(0, 0, "Narrow\nLumen", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    ax1.text(0, -4.7, "Thick wall : narrow lumen\nResists high pulse pressure", ha="center", va="top", fontsize=7.5, color=DARK_GREY)

    # 2. Vein
    set_plot_style(ax2, "Vein with Semilunar Valve")
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    ax2.axis("off")

    # Tunica externa
    c_vext = plt.Circle((0, 0), 4.3, color="#fed7aa", ec="#ea580c", lw=1.2)
    ax2.add_patch(c_vext)
    # Tunica media (thin muscle & few elastic fibres)
    c_vmed = plt.Circle((0, 0), 3.9, color="#fca5a5", ec="#dc2626", lw=1.2)
    ax2.add_patch(c_vmed)
    # Tunica intima
    c_vint = plt.Circle((0, 0), 3.5, color="#fef08a", ec="#ca8a04", lw=1.0)
    ax2.add_patch(c_vint)
    # Wide irregular lumen
    c_vlum = plt.Circle((0, 0), 3.3, color="white", ec=NAVY, lw=1.2)
    ax2.add_patch(c_vlum)

    # Semilunar valve flaps inside vein
    valv_l = patches.Arc((-1.5, 0), 2.5, 2.5, angle=0, theta1=270, theta2=90, color=BLUE_VESSEL, lw=2.0)
    valv_r = patches.Arc((1.5, 0), 2.5, 2.5, angle=0, theta1=90, theta2=270, color=BLUE_VESSEL, lw=2.0)
    ax2.add_patch(valv_l)
    ax2.add_patch(valv_r)
    ax2.text(0, 1.2, "Semilunar\nValve Flaps", ha="center", va="center", fontsize=7, fontweight="bold", color=BLUE_VESSEL)
    ax2.text(0, -1.2, "Wide Lumen\n(Low resistance)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    ax2.text(0, -4.7, "Thin wall : wide lumen\nValves prevent backflow", ha="center", va="top", fontsize=7.5, color=DARK_GREY)

    # 3. Capillary
    set_plot_style(ax3, "Blood Capillary")
    ax3.set_xlim(-5, 5)
    ax3.set_ylim(-5, 5)
    ax3.axis("off")

    # Single endothelial cell layer (7 um lumen)
    c_cap_out = plt.Circle((0, 0), 2.2, color="#fef08a", ec="#ca8a04", lw=1.5)
    ax3.add_patch(c_cap_out)
    c_cap_in = plt.Circle((0, 0), 1.8, color="white", ec=NAVY, lw=1.0)
    ax3.add_patch(c_cap_in)

    # Endothelial cell nucleus
    nuc = patches.Ellipse((0, 1.95), 1.5, 0.45, color="#7c3aed", ec=NAVY, lw=0.8)
    ax3.add_patch(nuc)
    ax3.text(0, 3.0, "Endothelial cell nucleus", ha="center", va="bottom", fontsize=7, color="#7c3aed")
    ax3.annotate("", xy=(0, 2.2), xytext=(0, 2.9), arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=1))

    # Single erythrocyte squeezed through lumen (~7 um)
    rbc = patches.Ellipse((0, -0.2), 1.5, 1.1, color="#ef4444", ec="#991b1b", lw=1.0)
    ax3.add_patch(rbc)
    ax3.text(0, -0.2, "RBC\n(~7 µm)", ha="center", va="center", fontsize=7, fontweight="bold", color="white")
    ax3.text(0, -4.7, "One cell thick (squamous)\nShort diffusion distance (~0.5 µm)", ha="center", va="top", fontsize=7.5, color=DARK_GREY)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_2_artery_vein_capillary_ts.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.3: Capillary Bed Ultrafiltration & Tissue Fluid Formation
# -----------------------------------------------------------------------------
def generate_fig8_3():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), dpi=300)
    set_plot_style(ax, "Fig. 8.3: Tissue Fluid Dynamics across a Capillary Bed (Starling Forces)")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Background tissue cells
    for x in [2.5, 4.5, 6.5, 8.5]:
        for y in [6.2, 1.8]:
            cell = patches.FancyBboxPatch((x-0.7, y-0.6), 1.4, 1.2, boxstyle="round,pad=0.1", facecolor="#f3e8ff", edgecolor="#c084fc", lw=1)
            ax.add_patch(cell)
            ax.plot(x, y, "o", color="#9333ea", markersize=4)
            ax.text(x, y-0.3, "Body Cell", ha="center", va="top", fontsize=6.5, color="#6b21a8")

    # Capillary tube spanning across center
    cap_top = patches.Rectangle((1.0, 3.8), 10.0, 0.2, facecolor="#fde047", edgecolor="#ca8a04", lw=1.2)
    cap_bot = patches.Rectangle((1.0, 3.0), 10.0, 0.2, facecolor="#fde047", edgecolor="#ca8a04", lw=1.2)
    cap_lumen = patches.Rectangle((1.0, 3.2), 10.0, 0.6, facecolor="#fff1f2", edgecolor="none")
    ax.add_patch(cap_top)
    ax.add_patch(cap_bot)
    ax.add_patch(cap_lumen)

    # Blood flow arrow
    ax.annotate("Blood flow", xy=(9.5, 3.5), xytext=(2.0, 3.5), arrowprops=dict(arrowstyle="->", color=RED_VESSEL, lw=2.5))

    # Arteriole End (Left)
    ax.text(1.2, 4.5, "ARTERIAL END", ha="left", va="bottom", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax.text(1.2, 5.3, "Hydrostatic Pressure = +4.3 kPa\nOncotic Pressure = -3.3 kPa\nNet Filtration Pressure = +1.0 kPa", ha="left", va="bottom", fontsize=7.5, color=DARK_GREY, bbox=dict(boxstyle="square,pad=0.3", fc="#fff1f2", ec=CRIMSON))
    # Outward filtration arrows
    for fx in [2.2, 3.2, 4.2]:
        ax.annotate("", xy=(fx, 4.7), xytext=(fx, 3.9), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2))
        ax.annotate("", xy=(fx, 2.3), xytext=(fx, 3.1), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2))
    ax.text(3.2, 5.0, "Ultrafiltration\n(Water, glucose, O2)", ha="center", va="bottom", fontsize=7, fontweight="bold", color=CRIMSON)

    # Venous End (Right)
    ax.text(10.8, 4.5, "VENOUS END", ha="right", va="bottom", fontsize=8.5, fontweight="bold", color=BLUE_VESSEL)
    ax.text(10.8, 5.3, "Hydrostatic Pressure = +1.6 kPa\nOncotic Pressure = -3.3 kPa\nNet Absorption Pressure = -1.7 kPa", ha="right", va="bottom", fontsize=7.5, color=DARK_GREY, bbox=dict(boxstyle="square,pad=0.3", fc="#eff6ff", ec=BLUE_VESSEL))
    # Inward reabsorption arrows
    for rx in [8.0, 9.0, 10.0]:
        ax.annotate("", xy=(rx, 3.9), xytext=(rx, 4.7), arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=2))
        ax.annotate("", xy=(rx, 3.1), xytext=(rx, 2.3), arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=2))
    ax.text(9.0, 5.0, "Reabsorption\n(Water, urea, CO2)", ha="center", va="bottom", fontsize=7, fontweight="bold", color=BLUE_VESSEL)

    # Lymphatic Capillary (draining excess ~10% fluid)
    lymph = patches.FancyBboxPatch((4.5, 0.4), 3.5, 0.6, boxstyle="round,pad=0.1", facecolor="#d1fae5", edgecolor=GREEN_LYMPH, lw=1.5)
    ax.add_patch(lymph)
    ax.text(6.25, 0.7, "Blind-ended Lymphatic Capillary", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_LYMPH)
    ax.annotate("", xy=(5.5, 0.9), xytext=(5.5, 2.0), arrowprops=dict(arrowstyle="->", color=GREEN_LYMPH, lw=1.8))
    ax.text(5.5, 1.4, "Excess fluid (~10%)\ndrained into lymph", ha="left", va="center", fontsize=7, color=GREEN_LYMPH)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_3_capillary_bed_tissue_fluid.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.4: Formed Elements of Mammalian Blood
# -----------------------------------------------------------------------------
def generate_fig8_4():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(7.5, 6.0), dpi=300)
    fig.suptitle("Fig. 8.4: Formed Cellular Elements of Mammalian Blood", fontsize=11, fontweight="bold", color=NAVY, y=0.98)

    # 1. Erythrocyte (RBC)
    set_plot_style(ax1, "Erythrocyte (Red Blood Cell)")
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-4, 4)
    ax1.axis("off")
    # Outer circle
    ax1.add_patch(plt.Circle((0, 0), 3.0, color="#f87171", ec="#b91c1c", lw=2.0))
    # Biconcave central dip
    ax1.add_patch(plt.Circle((0, 0), 1.6, color="#fca5a5", ec="#dc2626", lw=1.2, linestyle="--"))
    ax1.text(0, 0, "Biconcave\nCentral Pallor\n(No nucleus)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#7f1d1d")
    ax1.text(0, -3.6, "Diameter: 7.0–7.5 µm | Thickness: 2.0 µm\nFilled with ~280 million Hb molecules", ha="center", va="top", fontsize=7, color=DARK_GREY)

    # 2. Neutrophil (Granulocyte)
    set_plot_style(ax2, "Neutrophil (Phagocyte)")
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)
    ax2.axis("off")
    # Cytoplasm with granules
    ax2.add_patch(plt.Circle((0, 0), 3.2, color="#e0e7ff", ec="#6366f1", lw=1.5))
    # Multilobed nucleus (3-5 lobes connected by chromatin strands)
    l1 = patches.Circle((-1.2, 0.8), 0.9, color="#4338ca", ec=NAVY, lw=1)
    l2 = patches.Circle((0.8, 1.0), 0.8, color="#4338ca", ec=NAVY, lw=1)
    l3 = patches.Circle((0.4, -0.9), 1.0, color="#4338ca", ec=NAVY, lw=1)
    ax2.add_patch(l1)
    ax2.add_patch(l2)
    ax2.add_patch(l3)
    ax2.plot([-0.5, 0.2], [0.8, 0.9], color="#4338ca", lw=3)
    ax2.plot([0.5, 0.4], [0.3, -0.2], color="#4338ca", lw=3)
    # Granules
    np.random.seed(42)
    gx = np.random.uniform(-2.5, 2.5, 25)
    gy = np.random.uniform(-2.5, 2.5, 25)
    for x, y in zip(gx, gy):
        if x**2 + y**2 < 2.5**2 and not ((x+1)**2 + (y-1)**2 < 1 or (x-0.4)**2 + (y+0.9)**2 < 1):
            ax2.plot(x, y, "o", color="#818cf8", markersize=2)
    ax2.text(0, -3.6, "Multilobed nucleus (3–5 lobes)\nGranular cytoplasm | Phagocytosis", ha="center", va="top", fontsize=7, color=DARK_GREY)

    # 3. Monocyte (Agranulocyte / Macrophage Precursor)
    set_plot_style(ax3, "Monocyte (Largest Leukocyte)")
    ax3.set_xlim(-4, 4)
    ax3.set_ylim(-4, 4)
    ax3.axis("off")
    # Cytoplasm
    ax3.add_patch(plt.Circle((0, 0), 3.4, color="#ede9fe", ec="#8b5cf6", lw=1.5))
    # Kidney/bean-shaped nucleus
    path_data = [
        (Path.MOVETO, (-1.5, -1.2)),
        (Path.CURVE4, (-2.2, 0.5)),
        (Path.CURVE4, (-1.0, 2.0)),
        (Path.CURVE4, (0.8, 1.8)),
        (Path.CURVE4, (1.8, 1.0)),
        (Path.CURVE4, (1.2, -0.5)),
        (Path.CURVE4, (0.0, 0.2)), # indentation
        (Path.CURVE4, (-0.8, -0.8)),
        (Path.CLOSEPOLY, (-1.5, -1.2))
    ]
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor="#5b21b6", edgecolor=NAVY, lw=1.2)
    ax3.add_patch(patch)
    ax3.text(0, -3.6, "Kidney / horseshoe-shaped nucleus\nAgranular | Migrates to form macrophages", ha="center", va="top", fontsize=7, color=DARK_GREY)

    # 4. Lymphocyte (B & T cells)
    set_plot_style(ax4, "Lymphocyte (Adaptive Immunity)")
    ax4.set_xlim(-4, 4)
    ax4.set_ylim(-4, 4)
    ax4.axis("off")
    # Small cell, massive round nucleus
    ax4.add_patch(plt.Circle((0, 0), 2.5, color="#dbeafe", ec="#3b82f6", lw=1.5))
    ax4.add_patch(plt.Circle((0, 0), 2.0, color="#1e40af", ec=NAVY, lw=1.2))
    ax4.text(0, 0, "Massive\nSpherical\nNucleus", ha="center", va="center", fontsize=7.5, fontweight="bold", color="white")
    ax4.text(0, -3.6, "Thin crescent rim of cytoplasm\nDiameter: 6–9 µm | B and T lymphocytes", ha="center", va="top", fontsize=7, color=DARK_GREY)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_4_blood_formed_elements.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.5: Internal Coronal Anatomy of Mammalian Heart
# -----------------------------------------------------------------------------
def generate_fig8_5():
    fig, ax = plt.subplots(figsize=(8.0, 6.2), dpi=300)
    set_plot_style(ax, "Fig. 8.5: Internal Anatomy of Mammalian Heart (Coronal Section)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Outer Heart Wall Profile
    # Left ventricle wall is 3x thicker than right ventricle wall
    heart_shape = patches.Polygon([[2.0, 7.5], [1.5, 3.5], [4.5, 0.8], [7.5, 3.5], [8.0, 7.5], [5.0, 7.8]], closed=True, facecolor="#fee2e2", edgecolor=NAVY, lw=2.5)
    ax.add_patch(heart_shape)

    # Ventricular Cavities & Thick Myocardium
    # Right Ventricle (thinner wall ~5 mm)
    rv_cavity = patches.Polygon([[2.8, 6.0], [2.4, 3.8], [4.0, 2.0], [4.4, 4.0], [4.4, 6.0]], closed=True, facecolor="#dbeafe", edgecolor=BLUE_VESSEL, lw=1.5)
    ax.add_patch(rv_cavity)
    ax.text(3.3, 4.2, "Right\nVentricle\n(Wall ~0.5 cm)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)

    # Interventricular Septum
    ax.add_patch(patches.Rectangle((4.4, 1.8), 0.8, 4.5, facecolor="#fca5a5", edgecolor=NAVY, lw=1.2))
    ax.text(4.8, 3.2, "Septum", ha="center", va="center", fontsize=7, rotation=90, fontweight="bold", color=NAVY)

    # Left Ventricle (much thicker wall ~15 mm = 3x thicker!)
    lv_cavity = patches.Polygon([[5.4, 6.0], [5.4, 4.0], [5.0, 2.0], [6.6, 3.8], [6.6, 6.0]], closed=True, facecolor="#fee2e2", edgecolor=RED_VESSEL, lw=1.5)
    ax.add_patch(lv_cavity)
    ax.text(6.0, 4.2, "Left\nVentricle\n(Wall ~1.5 cm)\n3× Thicker!", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Atria (Top)
    # Right Atrium
    ra = patches.Rectangle((2.0, 6.5), 2.2, 1.8, facecolor="#bfdbfe", edgecolor=BLUE_VESSEL, lw=1.5)
    ax.add_patch(ra)
    ax.text(3.1, 7.4, "Right Atrium\n(Thin wall)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)

    # Left Atrium
    la = patches.Rectangle((5.8, 6.5), 2.2, 1.8, facecolor="#fecaca", edgecolor=RED_VESSEL, lw=1.5)
    ax.add_patch(la)
    ax.text(6.9, 7.4, "Left Atrium\n(Thin wall)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=RED_VESSEL)

    # Valves
    # Tricuspid valve (Right AV)
    ax.plot([2.8, 4.2], [6.2, 6.2], color=NAVY, lw=2.5)
    ax.text(2.6, 6.0, "Tricuspid\nAV Valve", ha="right", va="center", fontsize=7, fontweight="bold", color=NAVY)

    # Bicuspid / Mitral valve (Left AV)
    ax.plot([5.6, 6.8], [6.2, 6.2], color=NAVY, lw=2.5)
    ax.text(7.2, 6.0, "Bicuspid / Mitral\nAV Valve", ha="left", va="center", fontsize=7, fontweight="bold", color=NAVY)

    # Chordae tendineae & Papillary muscles
    ax.plot([3.5, 3.3], [6.2, 4.8], color=DARK_GREY, lw=1.2, linestyle=":")
    ax.plot([3.7, 3.5], [6.2, 4.8], color=DARK_GREY, lw=1.2, linestyle=":")
    ax.text(2.2, 5.0, "Chordae tendineae &\nPapillary muscle", ha="right", va="center", fontsize=6.5, color=DARK_GREY)

    ax.plot([5.8, 6.0], [6.2, 4.8], color=DARK_GREY, lw=1.2, linestyle=":")
    ax.plot([6.0, 6.2], [6.2, 4.8], color=DARK_GREY, lw=1.2, linestyle=":")

    # Great vessels exiting top
    # Aorta
    ax.add_patch(patches.Rectangle((4.8, 8.0), 1.0, 1.5, facecolor="#fca5a5", edgecolor=RED_VESSEL, lw=1.5))
    ax.text(5.3, 9.7, "Aorta (to systemic)", ha="center", va="bottom", fontsize=8, fontweight="bold", color=RED_VESSEL)
    # Pulmonary Artery
    ax.add_patch(patches.Rectangle((3.6, 8.0), 0.9, 1.4, facecolor="#93c5fd", edgecolor=BLUE_VESSEL, lw=1.5))
    ax.text(4.0, 9.6, "Pulmonary Artery\n(to lungs)", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=BLUE_VESSEL)

    # Semilunar valves
    ax.plot([4.9, 5.7], [8.0, 8.0], color=RED_VESSEL, lw=2.5)
    ax.text(6.0, 8.4, "Aortic Semilunar Valve", ha="left", va="center", fontsize=7, color=RED_VESSEL)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_5_heart_internal_anatomy.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.6: Wiggers Diagram of the Cardiac Cycle
# -----------------------------------------------------------------------------
def generate_fig8_6():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 6.2), dpi=300, sharex=True, gridspec_kw={'height_ratios': [2.5, 1]})
    set_plot_style(ax1, "Fig. 8.6: The Cardiac Cycle: Pressure and Volume Changes (Wiggers Diagram)")
    set_plot_style(ax2)

    # Time axis: 0.0 to 0.8 s (one full cardiac cycle at 75 bpm)
    t = np.linspace(0, 0.8, 500)

    # Left Ventricular Pressure (0 to 120 mmHg)
    # Atrial systole (0-0.1), Ventricular systole (0.1-0.4), Diastole (0.4-0.8)
    p_lv = np.piecewise(t, [
        t < 0.1,
        (t >= 0.1) & (t < 0.25),
        (t >= 0.25) & (t < 0.4),
        t >= 0.4
    ], [
        lambda x: 5 + 5 * np.sin(np.pi * x / 0.1),
        lambda x: 5 + 115 * np.sin(0.5 * np.pi * (x - 0.1) / 0.15),
        lambda x: 120 * np.cos(0.5 * np.pi * (x - 0.25) / 0.15),
        lambda x: 5 * np.exp(-10 * (x - 0.4)) + 3
    ])

    # Aortic Pressure (80 to 120 mmHg)
    p_ao = np.piecewise(t, [
        t < 0.15,
        (t >= 0.15) & (t < 0.25),
        (t >= 0.25) & (t < 0.38),
        (t >= 0.38) & (t < 0.42),
        t >= 0.42
    ], [
        lambda x: 82 - 20 * x,
        lambda x: 80 + 40 * np.sin(0.5 * np.pi * (x - 0.15) / 0.1),
        lambda x: 120 - 30 * (x - 0.25) / 0.13,
        lambda x: 90 + 8 * np.sin(np.pi * (x - 0.38) / 0.04), # Dicrotic notch
        lambda x: 95 - 35 * (x - 0.42) / 0.38
    ])

    # Left Atrial Pressure (2 to 12 mmHg)
    p_la = np.piecewise(t, [
        t < 0.1,
        (t >= 0.1) & (t < 0.4),
        t >= 0.4
    ], [
        lambda x: 4 + 7 * np.sin(np.pi * x / 0.1), # a-wave
        lambda x: 4 + 6 * (x - 0.1) / 0.3,         # v-wave
        lambda x: 10 - 6 * (x - 0.4) / 0.4
    ])

    ax1.plot(t, p_lv, color=CRIMSON, lw=2.2, label="Left Ventricle Pressure")
    ax1.plot(t, p_ao, color=NAVY, lw=2.0, linestyle="--", label="Aorta Pressure")
    ax1.plot(t, p_la, color="#2563eb", lw=1.5, linestyle=":", label="Left Atrium Pressure")

    ax1.set_ylabel("Pressure / mmHg", fontsize=9, fontweight="bold", color=NAVY)
    ax1.set_ylim(-5, 140)
    ax1.legend(loc="upper right", fontsize=8)
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Key valve events
    # AV valve closes at t = 0.11 (when LV pressure exceeds LA pressure)
    ax1.axvline(0.11, color="#6b7280", linestyle=":", lw=1.2)
    ax1.text(0.11, 20, "AV valve closes\n(1st heart sound 'lub')", fontsize=7, color=CRIMSON, ha="right")

    # Aortic valve opens at t = 0.15 (when LV pressure exceeds Aorta pressure)
    ax1.axvline(0.15, color="#6b7280", linestyle=":", lw=1.2)
    ax1.text(0.16, 75, "Aortic valve opens", fontsize=7, color=NAVY, ha="left")

    # Aortic valve closes at t = 0.38 (when LV pressure falls below Aorta pressure)
    ax1.axvline(0.38, color="#6b7280", linestyle=":", lw=1.2)
    ax1.text(0.38, 105, "Aortic valve closes\n(2nd sound 'dub')", fontsize=7, color=NAVY, ha="right")

    # AV valve opens at t = 0.45
    ax1.axvline(0.45, color="#6b7280", linestyle=":", lw=1.2)
    ax1.text(0.46, 25, "AV valve opens", fontsize=7, color="#2563eb", ha="left")

    # Ventricular Volume (ml)
    v_lv = np.piecewise(t, [
        t < 0.1,
        (t >= 0.1) & (t < 0.15),
        (t >= 0.15) & (t < 0.38),
        (t >= 0.38) & (t < 0.45),
        t >= 0.45
    ], [
        lambda x: 110 + 15 * np.sin(np.pi * x / 0.1), # End-diastolic volume ~125 ml
        lambda x: 125,                                 # Isovolumetric contraction
        lambda x: 125 - 65 * (x - 0.15) / 0.23,        # Ventricular ejection (Stroke vol ~65 ml)
        lambda x: 60,                                  # Isovolumetric relaxation (End-systolic vol ~60 ml)
        lambda x: 60 + 50 * (1 - np.exp(-12 * (x - 0.45))) # Rapid filling
    ])

    ax2.plot(t, v_lv, color=STEEL_BLUE, lw=2.0)
    ax2.set_ylabel("Ventricular\nVolume / cm³", fontsize=8.5, fontweight="bold", color=NAVY)
    ax2.set_xlabel("Time / seconds", fontsize=9, fontweight="bold", color=NAVY)
    ax2.set_ylim(40, 140)
    ax2.grid(True, linestyle="--", alpha=0.5)

    # Phases bands
    ax1.text(0.05, 132, "Atrial\nSystole", ha="center", fontsize=7, fontweight="bold", color=NAVY)
    ax1.text(0.25, 132, "Ventricular Systole\n(Ejection)", ha="center", fontsize=7, fontweight="bold", color=CRIMSON)
    ax1.text(0.60, 132, "Ventricular Diastole\n(Filling)", ha="center", fontsize=7, fontweight="bold", color=STEEL_BLUE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_6_cardiac_cycle_wiggers.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.7: Electrical Conduction System of the Heart
# -----------------------------------------------------------------------------
def generate_fig8_7():
    fig, ax = plt.subplots(figsize=(8.0, 5.8), dpi=300)
    set_plot_style(ax, "Fig. 8.7: Electrical Conduction System Coordinating the Cardiac Cycle")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Heart outline
    heart = patches.Polygon([[2.5, 7.8], [2.0, 4.0], [5.0, 1.2], [8.0, 4.0], [7.5, 7.8], [5.0, 8.0]], closed=True, facecolor="#f8fafc", edgecolor=NAVY, lw=2.0)
    ax.add_patch(heart)

    # Septum
    ax.plot([5.0, 5.0], [2.0, 6.5], color=NAVY, lw=3.0, linestyle="--")

    # 1. Sinoatrial Node (SAN) - Right Atrium
    san = patches.Ellipse((3.3, 7.4), 0.9, 0.6, color="#ef4444", ec=NAVY, lw=1.5)
    ax.add_patch(san)
    ax.text(3.3, 7.4, "SAN", ha="center", va="center", fontsize=8, fontweight="bold", color="white")
    ax.text(1.2, 7.8, "1. Sinoatrial Node (SAN)\n'Pacemaker' initiates wave\nof myogenic excitation\n(~72 bpm)", ha="left", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON, bbox=dict(boxstyle="round,pad=0.2", fc="#fff1f2", ec=CRIMSON))

    # Waves across atria
    for r in [0.7, 1.2, 1.7]:
        arc = patches.Arc((3.3, 7.4), r*2, r*2, angle=0, theta1=220, theta2=330, color="#f87171", lw=1.5, linestyle="--")
        ax.add_patch(arc)
    ax.text(5.0, 7.2, "Atria contract from top down", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # 2. Atrioventricular Node (AVN)
    avn = patches.Ellipse((4.7, 6.2), 0.7, 0.5, color="#f59e0b", ec=NAVY, lw=1.5)
    ax.add_patch(avn)
    ax.text(4.7, 6.2, "AVN", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    ax.text(6.8, 6.5, "2. Atrioventricular Node (AVN)\nDelays impulse by ~0.1 s\nAllows atria to empty\nbefore ventricles contract", ha="left", va="center", fontsize=7.5, fontweight="bold", color="#d97706", bbox=dict(boxstyle="round,pad=0.2", fc="#fef3c7", ec="#f59e0b"))

    # Non-conducting fibrous ring (separating atria and ventricles)
    ax.plot([2.2, 7.8], [6.0, 6.0], color="#94a3b8", lw=4.0)
    ax.text(8.0, 5.8, "Non-conducting\nfibrous ring", ha="left", va="center", fontsize=7, color="#64748b")

    # 3. Bundle of His (AV Bundle)
    ax.plot([4.8, 4.8], [6.0, 4.5], color="#2563eb", lw=3.0)
    ax.text(3.6, 5.2, "3. Bundle of His\n(Down septum)", ha="right", va="center", fontsize=7.5, fontweight="bold", color="#2563eb")

    # 4. Left and Right Bundle Branches
    ax.plot([4.8, 4.2, 3.8], [4.5, 3.2, 2.0], color="#2563eb", lw=2.5)
    ax.plot([4.8, 5.4, 5.8], [4.5, 3.2, 2.0], color="#2563eb", lw=2.5)

    # 5. Purkyne (Purkinje) Tissue
    # Spreads up ventricular walls from apex
    ax.plot([3.8, 3.0, 2.5], [2.0, 2.5, 4.0], color="#7c3aed", lw=2.0, linestyle="-.")
    ax.plot([5.8, 6.6, 7.1], [2.0, 2.5, 4.0], color="#7c3aed", lw=2.0, linestyle="-.")
    ax.text(5.0, 1.2, "Ventricular Apex", ha="center", va="top", fontsize=7.5, fontweight="bold", color=NAVY)
    ax.text(1.2, 2.8, "4. Purkyne Fibres\nConduct wave rapidly\nto apex so ventricles\ncontract upwards\ntowards arteries", ha="left", va="center", fontsize=7.5, fontweight="bold", color="#7c3aed", bbox=dict(boxstyle="round,pad=0.2", fc="#f5f3ff", ec="#7c3aed"))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_7_heart_conduction_system.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.8: Oxygen Dissociation Curve of Adult Haemoglobin
# -----------------------------------------------------------------------------
def generate_fig8_8():
    fig, ax = plt.subplots(figsize=(8.0, 5.2), dpi=300)
    set_plot_style(ax, "Fig. 8.8: Oxygen Dissociation Curve of Adult Haemoglobin (HbA)")

    # Hill equation for cooperative binding
    po2 = np.linspace(0, 14, 500)
    # P50 ~ 3.6 kPa, Hill coefficient n ~ 2.8
    p50 = 3.6
    n = 2.8
    sat = 100 * (po2**n) / (po2**n + p50**n)

    ax.plot(po2, sat, color=CRIMSON, lw=2.5, label="Adult Haemoglobin (HbA)")

    # Key physiological regions
    # Lungs (pO2 ~ 12 kPa, Sat ~ 98%)
    ax.plot([12, 12, 0], [0, 98, 98], color="#059669", linestyle=":", lw=1.2)
    ax.plot(12, 98, "o", color="#059669", markersize=6)
    ax.text(12.2, 95, "Pulmonary Capillaries (Lungs)\npO2 ≈ 12 kPa | Saturation ≈ 98%\nHigh affinity, loading O2", fontsize=7.5, color="#059669", fontweight="bold")

    # Resting tissues (pO2 ~ 5.3 kPa, Sat ~ 75%)
    sat_rest = 100 * (5.3**n) / (5.3**n + p50**n)
    ax.plot([5.3, 5.3, 0], [0, sat_rest, sat_rest], color="#2563eb", linestyle=":", lw=1.2)
    ax.plot(5.3, sat_rest, "o", color="#2563eb", markersize=6)
    ax.text(5.5, sat_rest-5, f"Resting Muscle / Tissues\npO2 ≈ 5.3 kPa | Saturation ≈ {sat_rest:.0f}%\n~25% O2 unloaded", fontsize=7.5, color="#2563eb", fontweight="bold")

    # Exercising tissues (pO2 ~ 2.5 kPa, Sat ~ 25%)
    sat_ex = 100 * (2.5**n) / (2.5**n + p50**n)
    ax.plot([2.5, 2.5, 0], [0, sat_ex, sat_ex], color=CRIMSON, linestyle=":", lw=1.2)
    ax.plot(2.5, sat_ex, "o", color=CRIMSON, markersize=6)
    ax.text(2.7, sat_ex-6, f"Actively Exercising Tissue\npO2 ≈ 2.5 kPa | Saturation ≈ {sat_ex:.0f}%\n~75% O2 unloaded!", fontsize=7.5, color=CRIMSON, fontweight="bold")

    # P50 (50% saturation)
    ax.plot([p50, p50, 0], [0, 50, 50], color="#6b7280", linestyle="--", lw=1.0)
    ax.text(p50+0.2, 52, f"P50 = {p50} kPa\n(Measure of affinity)", fontsize=7, color="#4b5563")

    ax.set_xlabel("Partial Pressure of Oxygen (pO2) / kPa", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylabel("Percentage Saturation of Haemoglobin with O2 (%)", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 105)
    ax.grid(True, linestyle="--", alpha=0.5)

    # Explanation note on S-shape
    ax.text(0.5, 80, "Sigmoidal (S-shaped) Curve:\nReflects positive cooperativity;\nbinding of 1st O2 alters 3D quaternary\nconformation, exposing remaining haem groups", fontsize=7.5, color=DARK_GREY, bbox=dict(boxstyle="square,pad=0.3", fc="#f8fafc", ec=BORDER_COLOR))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_8_oxygen_dissociation_curve.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.9: The Bohr Effect (Bohr Shift)
# -----------------------------------------------------------------------------
def generate_fig8_9():
    fig, ax = plt.subplots(figsize=(8.0, 5.2), dpi=300)
    set_plot_style(ax, "Fig. 8.9: The Bohr Effect: Rightward Shift of Oxygen Dissociation Curve")

    po2 = np.linspace(0, 14, 500)
    n = 2.8

    # 3 curves: Low CO2 (P50 = 2.8), Normal CO2 (P50 = 3.6), High CO2 (P50 = 4.8)
    sat_low = 100 * (po2**n) / (po2**n + 2.8**n)
    sat_norm = 100 * (po2**n) / (po2**n + 3.6**n)
    sat_high = 100 * (po2**n) / (po2**n + 4.8**n)

    ax.plot(po2, sat_low, color="#059669", lw=2.0, linestyle="--", label="Low pCO2 / Alkaline pH (Lungs)")
    ax.plot(po2, sat_norm, color=NAVY, lw=2.2, label="Normal Resting pCO2 (Blood)")
    ax.plot(po2, sat_high, color=CRIMSON, lw=2.2, label="Elevated pCO2 / Acidic pH (Respiring Muscle)")

    # Rightward arrow representing Bohr Shift
    ax.annotate("BOHR SHIFT\n(Rightward displacement)", xy=(5.5, 60), xytext=(2.8, 60), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.5), fontsize=8, fontweight="bold", color=CRIMSON, va="center")

    # Vertical comparison at tissue pO2 = 4.0 kPa
    s_norm_4 = 100 * (4.0**n) / (4.0**n + 3.6**n)
    s_high_4 = 100 * (4.0**n) / (4.0**n + 4.8**n)
    ax.plot([4.0, 4.0], [s_high_4, s_norm_4], color=CRIMSON, lw=2, linestyle="-")
    ax.text(4.2, (s_norm_4 + s_high_4)/2, f"Extra O2 unloaded:\n{s_norm_4 - s_high_4:.0f}% more O2\nreleased to cells", fontsize=7.5, fontweight="bold", color=CRIMSON, va="center")

    ax.set_xlabel("Partial Pressure of Oxygen (pO2) / kPa", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylabel("Percentage Saturation of Haemoglobin (%)", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 105)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.5)

    ax.text(0.5, 82, "Biochemical Mechanism:\n• High pCO2 generates H+ via carbonic anhydrase\n• H+ binds to allosteric sites on globin chains\n• Forms haemoglobinic acid (HHb)\n• Lowers affinity for O2, releasing O2 where needed most", fontsize=7.5, color=DARK_GREY, bbox=dict(boxstyle="square,pad=0.3", fc="#fff1f2", ec=CRIMSON))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_9_bohr_shift_curves.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.10: CO2 Transport in Erythrocyte & The Chloride Shift
# -----------------------------------------------------------------------------
def generate_fig8_10():
    fig, ax = plt.subplots(figsize=(8.8, 5.6), dpi=300)
    set_plot_style(ax, "Fig. 8.10: Carbon Dioxide Transport & The Chloride Shift inside an Erythrocyte")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Respiring tissue cell (Left)
    ax.add_patch(patches.FancyBboxPatch((0.4, 1.5), 1.8, 5.0, boxstyle="round,pad=0.2", facecolor="#f3e8ff", edgecolor="#9333ea", lw=1.5))
    ax.text(1.3, 5.8, "Respiring\nTissue Cell", ha="center", va="center", fontsize=8, fontweight="bold", color="#6b21a8")
    ax.text(1.3, 4.0, "Cellular\nRespiration:\nProduces CO2", ha="center", va="center", fontsize=7.5, color="#6b21a8")

    # Plasma area
    ax.text(3.2, 7.3, "BLOOD PLASMA", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#d97706")

    # Erythrocyte (Large membrane boundary)
    rbc = patches.FancyBboxPatch((4.5, 0.8), 6.8, 6.4, boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor=RED_VESSEL, lw=2.2)
    ax.add_patch(rbc)
    ax.text(7.9, 6.8, "RED BLOOD CELL (ERYTHROCYTE)", ha="center", va="center", fontsize=9, fontweight="bold", color=CRIMSON)

    # 1. CO2 diffusion from tissue into plasma and RBC
    ax.annotate("CO2 diffuses\ndown gradient", xy=(4.6, 4.8), xytext=(2.2, 4.8), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=2.0), fontsize=7.5, fontweight="bold", color=DARK_GREY)

    # 2. Inside RBC: Carbonic Anhydrase reaction
    rxn_box = patches.FancyBboxPatch((5.0, 3.8), 5.8, 2.2, boxstyle="square,pad=0.2", facecolor="white", edgecolor=BORDER_COLOR, lw=1.0)
    ax.add_patch(rxn_box)
    ax.text(7.9, 5.4, "CO2  +  H2O  <=====>  H2CO3  <=====>  H+  +  HCO3-", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(6.4, 4.8, "[Carbonic Anhydrase]", ha="center", va="center", fontsize=7, color=CRIMSON, fontweight="bold")
    ax.text(7.9, 4.2, "Carbonic acid rapidly dissociates into H+ and HCO3-", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # 3. Buffering by Haemoglobin
    ax.annotate("", xy=(6.5, 2.6), xytext=(6.5, 3.8), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5))
    ax.text(6.5, 2.2, "H+  +  HbO8  ----->  HHb  +  4 O2\n(Haemoglobinic acid buffers H+,\npromoting oxygen unloading!)", ha="center", va="top", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # 4. Chloride Shift (HCO3- out, Cl- in)
    ax.annotate("", xy=(3.8, 3.4), xytext=(5.2, 3.4), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2.2))
    ax.text(4.5, 3.6, "HCO3- exits", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color="#2563eb")

    ax.annotate("", xy=(5.2, 2.8), xytext=(3.8, 2.8), arrowprops=dict(arrowstyle="->", color="#059669", lw=2.2))
    ax.text(4.5, 2.6, "Cl- enters", ha="center", va="top", fontsize=7.5, fontweight="bold", color="#059669")

    # Label: Anion Exchanger Band 3 / Chloride Shift
    ax.text(4.5, 1.8, "THE CHLORIDE SHIFT\n(Maintains electrochemical neutrality\nvia Band 3 anion exchanger)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY, bbox=dict(boxstyle="round,pad=0.2", fc="#f1f5f9", ec=NAVY))

    # 5. Carbaminohaemoglobin pathway
    ax.text(9.5, 2.2, "CO2  +  Hb-NH2  ----->  Hb-NHCOOH\n(Carbaminohaemoglobin ~10%)", ha="center", va="top", fontsize=7, color=DARK_GREY)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_10_co2_transport_rbc_chloride_shift.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.11: Comparative Curves: Adult Hb vs Fetal Hb vs Myoglobin
# -----------------------------------------------------------------------------
def generate_fig8_11():
    fig, ax = plt.subplots(figsize=(8.0, 5.2), dpi=300)
    set_plot_style(ax, "Fig. 8.11: Comparison of Oxygen Dissociation Curves: HbA, HbF, and Myoglobin")

    po2 = np.linspace(0, 14, 500)

    # 1. Myoglobin (hyperbolic curve, extreme affinity, P50 ~ 0.4 kPa, n = 1)
    sat_mb = 100 * po2 / (po2 + 0.4)

    # 2. Fetal Haemoglobin (HbF, sigmoidal, higher affinity than HbA, P50 ~ 2.4 kPa, n = 2.6)
    sat_hbf = 100 * (po2**2.6) / (po2**2.6 + 2.4**2.6)

    # 3. Adult Haemoglobin (HbA, sigmoidal, P50 ~ 3.6 kPa, n = 2.8)
    sat_hba = 100 * (po2**2.8) / (po2**2.8 + 3.6**2.8)

    ax.plot(po2, sat_mb, color="#7c3aed", lw=2.2, label="Myoglobin (Muscle O2 storage - Hyperbolic)")
    ax.plot(po2, sat_hbf, color="#d97706", lw=2.2, label="Fetal Haemoglobin (HbF - Higher affinity)")
    ax.plot(po2, sat_hba, color=CRIMSON, lw=2.2, label="Adult Haemoglobin (HbA - Cooperative sigmoidal)")

    # Placenta exchange line at pO2 ~ 4.0 kPa
    sat_f_4 = 100 * (4.0**2.6) / (4.0**2.6 + 2.4**2.6)
    sat_a_4 = 100 * (4.0**2.8) / (4.0**2.8 + 3.6**2.8)
    ax.plot([4.0, 4.0], [0, sat_f_4], color="#6b7280", linestyle=":", lw=1.2)
    ax.annotate(f"Placental transfer:\nMaternal HbA unloads ({sat_a_4:.0f}%)\nFetal HbF binds ({sat_f_4:.0f}%)", xy=(4.0, sat_f_4), xytext=(5.5, 60), arrowprops=dict(arrowstyle="->", color="#d97706", lw=1.5), fontsize=7.5, fontweight="bold", color="#d97706")

    ax.set_xlabel("Partial Pressure of Oxygen (pO2) / kPa", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylabel("Percentage Saturation (%)", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 105)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.5)

    ax.text(0.5, 78, "Key Adaptations:\n• Myoglobin: Single polypeptide with 1 haem; binds O2\n  tenaciously, only releasing at extreme low pO2 in hypoxia\n• Fetal Hb: Contains 2 gamma chains instead of beta chains;\n  binds 2,3-BPG weakly, yielding higher affinity than maternal\n  blood, ensuring net transfer across placenta", fontsize=7.5, color=DARK_GREY, bbox=dict(boxstyle="square,pad=0.3", fc="#f8fafc", ec=BORDER_COLOR))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_11_fetal_adult_myoglobin_curves.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.12: Vasomotor Regulation in Arterioles
# -----------------------------------------------------------------------------
def generate_fig8_12():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300)
    fig.suptitle("Fig. 8.12: Vasomotor Regulation in Arterioles Controlling Peripheral Blood Flow", fontsize=11, fontweight="bold", color=NAVY, y=0.98)

    # 1. Vasoconstriction
    set_plot_style(ax1, "Vasoconstriction")
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-4, 4)
    ax1.axis("off")
    # Contracted thick muscle
    ax1.add_patch(plt.Circle((0, 0), 3.2, color="#fca5a5", ec="#dc2626", lw=2.0))
    # Constricted narrow lumen
    ax1.add_patch(plt.Circle((0, 0), 1.0, color="white", ec=NAVY, lw=1.5))
    ax1.text(0, 0, "Constricted\nLumen", ha="center", va="center", fontsize=7, fontweight="bold", color=NAVY)
    ax1.text(0, -3.6, "Circular smooth muscle CONTRACTED\n• Lumen diameter reduced\n• High vascular resistance\n• Drastically reduced blood flow", ha="center", va="top", fontsize=7.5, color=DARK_GREY)

    # 2. Vasodilation
    set_plot_style(ax2, "Vasodilation")
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)
    ax2.axis("off")
    # Relaxed muscle
    ax2.add_patch(plt.Circle((0, 0), 3.2, color="#fed7aa", ec="#ea580c", lw=1.5))
    # Dilated wide lumen
    ax2.add_patch(plt.Circle((0, 0), 2.2, color="white", ec=NAVY, lw=1.5))
    ax2.text(0, 0, "Dilated Wide\nLumen", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    ax2.text(0, -3.6, "Circular smooth muscle RELAXED\n• Lumen diameter enlarged\n• Low vascular resistance\n• Increased local perfusion / flow", ha="center", va="top", fontsize=7.5, color=DARK_GREY)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_12_arteriole_vasoconstriction.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.13: Blind-Ended Lymphatic Capillary
# -----------------------------------------------------------------------------
def generate_fig8_13():
    fig, ax = plt.subplots(figsize=(8.0, 4.8), dpi=300)
    set_plot_style(ax, "Fig. 8.13: Architecture of a Blind-Ended Lymphatic Capillary")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Lymphatic tube closed at one end
    # Overlapping endothelial cells acting as one-way flap valves
    ax.add_patch(patches.FancyBboxPatch((2.0, 1.8), 7.0, 2.4, boxstyle="round,pad=0.2", facecolor="#d1fae5", edgecolor=GREEN_LYMPH, lw=2.0))
    ax.text(2.3, 3.0, "Blind End\n(Closed)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_LYMPH)
    ax.text(5.5, 3.0, "Lumen of Lymphatic Capillary\n(Filled with clear lymph: no RBCs, few proteins)", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Flap valves & fluid entry
    for x in [3.8, 5.2, 6.6]:
        ax.plot([x, x+0.6], [4.2, 4.5], color=GREEN_LYMPH, lw=2.5)
        ax.annotate("", xy=(x+0.3, 3.8), xytext=(x+0.3, 5.0), arrowprops=dict(arrowstyle="->", color=GREEN_LYMPH, lw=2))
        ax.plot([x, x+0.6], [1.8, 1.5], color=GREEN_LYMPH, lw=2.5)
        ax.annotate("", xy=(x+0.3, 2.2), xytext=(x+0.3, 1.0), arrowprops=dict(arrowstyle="->", color=GREEN_LYMPH, lw=2))

    ax.text(5.2, 5.4, "Interstitial Tissue Fluid enters via one-way flap valves\n(High interstitial pressure pushes flaps open)", ha="center", va="bottom", fontsize=7.5, color=DARK_GREY)

    # Anchoring filaments
    ax.plot([4.0, 4.0], [4.2, 4.8], color="#94a3b8", lw=1.2, linestyle=":")
    ax.text(8.5, 4.8, "Anchoring collagen filaments\nprevent capillary collapse", ha="center", va="center", fontsize=7, color="#64748b")

    # Flow direction to lymph nodes
    ax.annotate("To subclavian veins\nvia lymph nodes", xy=(9.5, 3.0), xytext=(7.8, 3.0), arrowprops=dict(arrowstyle="->", color=GREEN_LYMPH, lw=2.5), fontsize=7.5, fontweight="bold", color=GREEN_LYMPH, va="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_13_lymphatic_system_drainage.png"), dpi=300)
    plt.close()

# -----------------------------------------------------------------------------
# Fig 8.14: Pressure Changes across Systemic Circulation
# -----------------------------------------------------------------------------
def generate_fig8_14():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), dpi=300)
    set_plot_style(ax, "Fig. 8.14: Blood Pressure Profile Across the Mammalian Systemic Vascular Tree")

    # Vessels: Aorta, Large Arteries, Small Arteries, Arterioles, Capillaries, Venules, Veins, Vena Cava
    x = np.linspace(0, 10, 1000)

    # Pulsatile pressure in Aorta and Arteries (0 to 3.5), dropping steeply in Arterioles (3.5 to 5.5)
    # Non-pulsatile low pressure in Capillaries, Venules, Veins (5.5 to 10)
    p_systolic = np.piecewise(x, [
        x < 2.0,
        (x >= 2.0) & (x < 3.5),
        (x >= 3.5) & (x < 5.5),
        (x >= 5.5) & (x < 7.0),
        x >= 7.0
    ], [
        lambda v: 120 + 2 * np.sin(2 * np.pi * 3 * v),
        lambda v: 120 - 15 * (v - 2.0) / 1.5 + 2 * np.sin(2 * np.pi * 3 * v),
        lambda v: 105 - 70 * (v - 3.5) / 2.0,
        lambda v: 35 - 20 * (v - 5.5) / 1.5,
        lambda v: 15 - 12 * (v - 7.0) / 3.0
    ])

    p_diastolic = np.piecewise(x, [
        x < 2.0,
        (x >= 2.0) & (x < 3.5),
        (x >= 3.5) & (x < 5.5),
        (x >= 5.5) & (x < 7.0),
        x >= 7.0
    ], [
        lambda v: 80 - 1 * np.sin(2 * np.pi * 3 * v),
        lambda v: 80 - 5 * (v - 2.0) / 1.5 - 1 * np.sin(2 * np.pi * 3 * v),
        lambda v: 75 - 40 * (v - 3.5) / 2.0,
        lambda v: 35 - 20 * (v - 5.5) / 1.5,
        lambda v: 15 - 12 * (v - 7.0) / 3.0
    ])

    # Plot pulsatile envelope
    ax.fill_between(x, p_diastolic, p_systolic, color="#fee2e2", alpha=0.6, label="Pulse Pressure (Systolic - Diastolic)")
    ax.plot(x, p_systolic, color=CRIMSON, lw=2.0)
    ax.plot(x, p_diastolic, color=CRIMSON, lw=2.0)

    # Mean arterial pressure curve
    p_mean = (p_systolic + 2 * p_diastolic) / 3
    ax.plot(x, p_mean, color=NAVY, lw=2.0, linestyle="--", label="Mean Blood Pressure")

    ax.set_ylabel("Blood Pressure / mmHg", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylim(-5, 140)
    ax.set_xlim(0, 10)
    ax.set_xticks([0.8, 2.5, 4.5, 6.2, 7.8, 9.2])
    ax.set_xticklabels(["Aorta", "Large\nArteries", "Arterioles\n(Resistance)", "Capillaries", "Venules\n& Veins", "Vena\nCava"], fontsize=8, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper right", fontsize=8)

    # Highlight steep pressure drop in arterioles
    ax.annotate("Steepest pressure drop\nin ARTERIOLES\n(Major site of resistance)", xy=(4.5, 60), xytext=(5.2, 100), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2), fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Highlight non-pulsatile flow in capillaries
    ax.text(6.8, 45, "Pulse extinguished\nSmooth, non-pulsatile\ncapillary flow protects\ndelicate exchange walls", fontsize=7, color=DARK_GREY)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig8_14_cardiac_output_pressures.png"), dpi=300)
    plt.close()

def main():
    print("Generating 14 diagrams for Topic 8: Transport in Mammals...")
    generate_fig8_1()
    generate_fig8_2()
    generate_fig8_3()
    generate_fig8_4()
    generate_fig8_5()
    generate_fig8_6()
    generate_fig8_7()
    generate_fig8_8()
    generate_fig8_9()
    generate_fig8_10()
    generate_fig8_11()
    generate_fig8_12()
    generate_fig8_13()
    generate_fig8_14()
    print("All 14 Topic 8 diagrams generated successfully at 300 DPI!")

if __name__ == "__main__":
    main()
